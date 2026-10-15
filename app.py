"""ICT practice: local-only, no third-party runtime dependencies."""
import argparse
import hashlib
import json
import mimetypes
import sqlite3
import threading
import time
import webbrowser
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
WEB = ROOT / "web"


class Store:
    def __init__(self, bank_path, db_path):
        raw = Path(bank_path).read_bytes()
        self.bank = json.loads(raw)
        self.questions = {q["id"]: q for q in self.bank["questions"]}
        self.version = hashlib.sha256(raw).hexdigest()[:12]
        self.db_path = str(db_path)
        with self.connect() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS attempts (
                    token TEXT PRIMARY KEY, question_id INTEGER NOT NULL,
                    selected TEXT NOT NULL, correct INTEGER NOT NULL,
                    feedback TEXT NOT NULL, created_at REAL NOT NULL
                );
                CREATE TABLE IF NOT EXISTS progress (
                    question_id INTEGER PRIMARY KEY, wrong_count INTEGER NOT NULL,
                    right_streak INTEGER NOT NULL, last_correct INTEGER NOT NULL
                );
            """)

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.db_path, timeout=15)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def public_bank(self):
        return {"version": self.version, "summary": self.bank["summary"], "questions": [
            {k: q[k] for k in ("id", "stem", "options", "type", "topic", "image")}
            for q in self.questions.values()]}

    def answer(self, payload):
        token = payload.get("token")
        qid = payload.get("question_id")
        selected = payload.get("selected")
        if not isinstance(token, str) or not 8 <= len(token) <= 100:
            raise ValueError("作答标识无效，请刷新页面后重试。")
        if type(qid) is not int or qid not in self.questions:
            raise ValueError("这道题不在可用题库中。")
        q = self.questions[qid]
        if (not isinstance(selected, list) or not selected or
            not all(isinstance(v, str) and v in q["options"] for v in selected) or
            len(set(selected)) != len(selected) or
            (q["type"] != "multiple" and len(selected) != 1)):
            raise ValueError("请选择有效的答案。")
        selected = sorted(selected)
        correct = selected == sorted(q["answer"])
        feedback = {"question_id": qid, "correct": correct, "selected": selected,
                    "answer": list(q["answer"]), "explanation": q["explanation"],
                    "sources": q.get("sources", [])}
        with self.connect() as db:
            # Reserve the write lock so retries and simultaneous tabs cannot double count.
            db.execute("BEGIN IMMEDIATE")
            old = db.execute("SELECT * FROM attempts WHERE token=?", (token,)).fetchone()
            if old:
                if old["question_id"] != qid or json.loads(old["selected"]) != selected:
                    raise ValueError("同一次作答已提交，请使用“重新作答”。")
                return json.loads(old["feedback"])
            db.execute("INSERT INTO attempts VALUES(?,?,?,?,?,?)", (
                token, qid, json.dumps(selected), int(correct),
                json.dumps(feedback, ensure_ascii=False), time.time()))
            db.execute("""INSERT INTO progress VALUES(?,?,?,?)
                ON CONFLICT(question_id) DO UPDATE SET
                wrong_count=wrong_count+excluded.wrong_count,
                right_streak=CASE WHEN excluded.last_correct=1 THEN right_streak+1 ELSE 0 END,
                last_correct=excluded.last_correct""", (qid, int(not correct), int(correct), int(correct)))
        return feedback

    def stats(self):
        valid = set(self.questions)
        with self.connect() as db:
            rows = db.execute("SELECT question_id,correct FROM attempts").fetchall()
            rows = [r for r in rows if r["question_id"] in valid]
            mistakes = [{"id": r["question_id"], "wrong_count": r["wrong_count"],
                         "mastered": r["right_streak"] >= 2}
                        for r in db.execute("SELECT * FROM progress WHERE wrong_count>0 ORDER BY wrong_count DESC")
                        if r["question_id"] in valid]
        return {"attempts": len(rows), "correct": sum(r["correct"] for r in rows),
                "practiced": len({r["question_id"] for r in rows}), "mistakes": mistakes}


def handler_for(store):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            pass

        def send_data(self, status, data, mime="application/json; charset=utf-8", attachment=None):
            if isinstance(data, (dict, list)):
                data = json.dumps(data, ensure_ascii=False).encode("utf-8")
            elif isinstance(data, str):
                data = data.encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", mime)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'self'; style-src 'self'; script-src 'self'; img-src 'self'; connect-src 'self'; object-src 'none'; frame-ancestors 'none'")
            if attachment:
                self.send_header("Content-Disposition", f'attachment; filename="{attachment}"')
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            path = urlsplit(self.path).path
            if path == "/api/questions":
                return self.send_data(200, store.public_bank())
            if path == "/api/stats":
                return self.send_data(200, store.stats())
            downloads = {"/exports/questions.json": (ROOT / "exports" / "题库及解析.json", "ict-questions.json"),
                         "/exports/materials.zip": (ROOT / "exports" / "题库资料.zip", "ict-materials.zip"),
                         "/exports/explanations.md": (ROOT / "exports" / "题库及解析.md", "ict-explanations.md"),
                         "/exports/cleaning.md": (ROOT / "exports" / "题库清理报告.md", "ict-cleaning.md")}
            if path in downloads:
                file, name = downloads[path]
                return self.send_data(200, file.read_bytes(), "application/octet-stream", name)
            if path == "/api/backup":
                with store.connect() as db:
                    attempts = [dict(r) for r in db.execute("SELECT * FROM attempts ORDER BY created_at")]
                    progress = [dict(r) for r in db.execute("SELECT * FROM progress")]
                return self.send_data(200, {"bank_version": store.version, "attempts": attempts, "progress": progress}, attachment="ict-progress.json")
            allowed = {"/": "index.html", "/index.html": "index.html", "/app.js": "app.js", "/style.css": "style.css"}
            if path in allowed:
                file = WEB / allowed[path]
            elif path.startswith("/assets/"):
                file = (WEB / path.lstrip("/")).resolve()
                if not file.is_relative_to((WEB / "assets").resolve()):
                    return self.send_data(404, {"error": "页面不存在"})
            else:
                return self.send_data(404, {"error": "页面不存在"})
            if not file.is_file():
                return self.send_data(404, {"error": "文件不存在"})
            mime = mimetypes.guess_type(file.name)[0] or "application/octet-stream"
            if file.suffix in (".html", ".css", ".js", ".svg"):
                mime += "; charset=utf-8"
            self.send_data(200, file.read_bytes(), mime)

        def do_POST(self):
            if urlsplit(self.path).path != "/api/answer":
                return self.send_data(404, {"error": "接口不存在"})
            # Restrict browser requests to our own local origin.
            origin = self.headers.get("Origin")
            if origin and origin != f"http://{self.headers.get('Host')}":
                return self.send_data(403, {"error": "请从本地网站提交答案。"})
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 8192:
                    raise ValueError("请求格式无效。")
                payload = json.loads(self.rfile.read(length))
                if not isinstance(payload, dict):
                    raise ValueError("请求格式无效。")
                self.send_data(200, store.answer(payload))
            except (ValueError, TypeError, KeyError) as error:
                self.send_data(400, {"error": str(error)})
            except sqlite3.Error:
                self.send_data(503, {"error": "记录暂时无法保存，请稍后重试。"})
    return Handler


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument("--db", default=str(ROOT / "data" / "practice.sqlite3"))
    args = parser.parse_args()
    bank = ROOT / "data" / "questions.json"
    if not bank.exists():
        raise SystemExit("题库尚未生成，请先运行 scripts/build_bank.py。")
    store = Store(bank, args.db)
    try:
        server = ThreadingHTTPServer(("127.0.0.1", args.port), handler_for(store))
    except OSError as error:
        raise SystemExit(f"端口 {args.port} 无法使用：{error}。可以用 --port 8766 更换端口。")
    url = f"http://127.0.0.1:{args.port}"
    print(f"ICT practice ready: {url}", flush=True)
    if not args.no_browser:
        threading.Timer(0.7, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
