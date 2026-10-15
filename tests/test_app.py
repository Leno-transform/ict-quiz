"""Integration checks use temporary databases, never the user's learning records."""
import concurrent.futures
import json
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app import Store, handler_for


class PracticeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.store = Store(ROOT / "data" / "questions.json", Path(cls.temp.name) / "test.sqlite3")
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), handler_for(cls.store))
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()
        cls.temp.cleanup()

    def request(self, path, body=None, origin=None):
        headers = {"Content-Type": "application/json"}
        if origin:
            headers["Origin"] = origin
        req = urllib.request.Request(self.url + path, data=json.dumps(body).encode() if body is not None else None, headers=headers)
        return urllib.request.urlopen(req)

    def pick(self, kind):
        return next(q for q in self.store.questions.values() if q["type"] == kind)

    def test_bank_contract_and_exports(self):
        bank = self.store.bank
        summary = bank["summary"]
        self.assertEqual(summary["source_count"], summary["kept_count"] + summary["duplicate_count"] + summary["invalid_count"])
        self.assertEqual(len(self.store.questions), summary["kept_count"])
        for q in self.store.questions.values():
            self.assertTrue(q["explanation"].strip())
            self.assertTrue(q["sources"])
            self.assertGreaterEqual(len(q["options"]), 2)
            self.assertTrue(set(q["answer"]) <= set(q["options"]))
            if q["image"]:
                self.assertTrue((ROOT / "web" / q["image"]["src"].lstrip("/")).is_file())
        with self.request("/api/questions") as response:
            public = json.load(response)
        self.assertEqual(len(public["questions"]), len(self.store.questions))
        self.assertTrue(all("answer" not in q and "explanation" not in q for q in public["questions"]))
        for path in ("/", "/style.css", "/app.js", "/exports/questions.json", "/exports/explanations.md", "/exports/cleaning.md", "/exports/materials.zip"):
            with self.request(path) as response:
                self.assertEqual(response.status, 200)
                self.assertGreater(len(response.read()), 100)

    def test_single_and_judge(self):
        for kind in ("single", "judge"):
            q = self.pick(kind)
            result = self.store.answer({"token": "correct-" + kind, "question_id": q["id"], "selected": list(q["answer"])})
            self.assertTrue(result["correct"])
            self.assertEqual(result["explanation"], q["explanation"])
            wrong = next(k for k in q["options"] if k not in q["answer"])
            result = self.store.answer({"token": "incorrect-" + kind, "question_id": q["id"], "selected": [wrong]})
            self.assertFalse(result["correct"])
            self.assertIn(q["id"], {r["id"] for r in self.store.stats()["mistakes"]})

    def test_multiselect_exact_match_and_order(self):
        q = next(q for q in self.store.questions.values() if q["type"] == "multiple" and len(q["answer"]) >= 2)
        result = self.store.answer({"token": "multiple-reversed", "question_id": q["id"], "selected": list(reversed(q["answer"]))})
        self.assertTrue(result["correct"])
        result = self.store.answer({"token": "multiple-incomplete", "question_id": q["id"], "selected": list(q["answer"][:-1])})
        self.assertFalse(result["correct"])

    def test_idempotent_concurrent_submit(self):
        q = self.pick("single")
        payload = {"token": "concurrent-one-attempt", "question_id": q["id"], "selected": list(q["answer"])}
        before = self.store.stats()["attempts"]
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
            results = list(pool.map(lambda _: self.store.answer(payload), range(5)))
        self.assertTrue(all(r == results[0] for r in results))
        self.assertEqual(self.store.stats()["attempts"], before + 1)
        with self.assertRaises(ValueError):
            self.store.answer({**payload, "selected": [next(k for k in q["options"] if k not in q["answer"])]})

    def test_persistence_and_mastery(self):
        q = self.pick("single")
        wrong = next(k for k in q["options"] if k not in q["answer"])
        for suffix, selected in [("wrong", [wrong]), ("right1", list(q["answer"])), ("right2", list(q["answer"]))]:
            self.store.answer({"token": "mastery-" + suffix, "question_id": q["id"], "selected": selected})
        reopened = Store(ROOT / "data" / "questions.json", self.store.db_path)
        mistake = next(r for r in reopened.stats()["mistakes"] if r["id"] == q["id"])
        self.assertTrue(mistake["mastered"])
        self.assertEqual(reopened.stats(), self.store.stats())

    def test_invalid_requests_and_private_files(self):
        q = self.pick("single")
        for selected in ([], ["Z"], ["A", "A"], "A", None):
            with self.assertRaises(ValueError):
                self.store.answer({"token": "bad-selection", "question_id": q["id"], "selected": selected})
        for path in ("/data/practice.sqlite3", "/app.py", "/assets/../../app.py"):
            with self.assertRaises(urllib.error.HTTPError) as error:
                self.request(path)
            self.assertEqual(error.exception.code, 404)
            error.exception.close()
        with self.assertRaises(urllib.error.HTTPError) as error:
            self.request("/api/answer", {"token": "cross-origin-test", "question_id": q["id"], "selected": list(q["answer"])}, "https://example.org")
        self.assertEqual(error.exception.code, 403)
        error.exception.close()


if __name__ == "__main__":
    unittest.main()
