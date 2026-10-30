"""Build a self-contained mobile file and installable static PWA."""
import base64
import hashlib
import json
import mimetypes
import re
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "mobile-site" / "dist"


def script_json(value):
    return json.dumps(value, ensure_ascii=False).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def icon_png(size):
    # A simple code-native icon, with ample maskable padding.
    rows = bytearray()
    for y in range(size):
        rows.append(0)
        for x in range(size):
            dot = (x - size * .5) ** 2 + (y - size * .31) ** 2 < (size * .045) ** 2
            bar = size * .455 < x < size * .545 and size * .42 < y < size * .7
            rows.extend((190, 219, 202, 255) if dot or bar else (20, 44, 53, 255))
    def chunk(name, data):
        return struct.pack(">I", len(data)) + name + data + struct.pack(">I", zlib.crc32(name + data) & 0xffffffff)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(rows)) + chunk(b"IEND", b"")


def main():
    DIST.mkdir(parents=True, exist_ok=True)
    bank = json.loads((ROOT / "data" / "questions.json").read_text(encoding="utf-8"))
    bank["version"] = hashlib.sha256((ROOT / "data" / "questions.json").read_bytes()).hexdigest()[:12]
    count = len(bank["questions"])
    release_filename = f"ICT手机独立版-{count}题.html"
    portal = (ROOT / "web" / "mobile.html").read_text(encoding="utf-8")
    for key, value in {"QUESTION_COUNT": count, "FIGURE_COUNT": bank["summary"]["image_count"], "BANK_VERSION": bank["version"], "RELEASE_FILENAME": release_filename}.items():
        portal = portal.replace("{{" + key + "}}", str(value))
    (DIST / "mobile.html").write_text(portal, encoding="utf-8")
    (DIST / "mobile-qr.png").write_bytes((ROOT / "mobile-qr.png").read_bytes())
    for q in bank["questions"]:
        if q["image"]:
            path = ROOT / "web" / q["image"]["src"].lstrip("/")
            mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            q["image"]["src"] = "data:" + mime + ";base64," + base64.b64encode(path.read_bytes()).decode("ascii")
    page = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
    page = page.replace('href="/"', 'href="./index.html"')
    page = page.replace('<link rel="stylesheet" href="/style.css"><script src="/app.js" defer></script>',
                        '<style>' + (ROOT / "web" / "style.css").read_text(encoding="utf-8") + '</style>')
    page = page.replace("本地运行 · 记录自动保存", "手机独立版 · 记录保存在本机")
    page = page.replace("<title>ICT 练习室</title>", f"<title>ICT 练习室 · 手机独立版（{count}题）</title>")
    page = page.replace('<section class="page-heading">', f'<p class="mobile-edition">手机独立版 · {count} 题 · 解析与图片均已内置</p><section class="page-heading">')
    help_html = '''<div id="mobile-status" class="mobile-status" role="status"></div>
    <button id="mobile-install" class="secondary-button install-button" hidden>安装到主屏幕</button>
    <details class="mobile-help"><summary>手机安装与保存说明</summary><p>iPhone：用 Safari 打开网址，点击分享 → 添加到主屏幕。安卓：使用 Chrome 菜单里的“安装应用”或“添加到主屏幕”。首次打开后，等待上方显示“离线就绪”。</p><p>学习记录保存在这台手机的当前浏览器中，不与电脑版自动同步。清除网站数据会删除记录，建议定期从“导出资料”备份。</p></details>'''
    page = page.replace('<div class="bank-note" id="bank-note"></div>', '<div class="bank-note" id="bank-note"></div>' + help_html)
    embedded = '<script id="ict-bank" type="application/json">' + script_json(bank) + '</script>'
    for name, filename in [("explanations", "题库及解析.md"), ("cleaning", "题库清理报告.md")]:
        embedded += f'<script id="ict-{name}" type="application/json">' + script_json((ROOT / "exports" / filename).read_text(encoding="utf-8")) + '</script>'
    embedded += '<script id="ict-materials" type="text/plain">' + base64.b64encode((ROOT / "exports" / "题库资料.zip").read_bytes()).decode("ascii") + '</script>'
    for name in ("offline.js", "app.js"):
        embedded += '<script>' + (ROOT / "web" / name).read_text(encoding="utf-8").replace('</script', '<\\/script') + '</script>'
    page = page.replace('</body>', embedded + '</body>')
    (ROOT / "手机独立版.html").write_text(page, encoding="utf-8")
    (ROOT / release_filename).write_text(page, encoding="utf-8")
    (DIST / release_filename).write_text(page, encoding="utf-8")
    metadata = '<meta name="theme-color" content="#142c35"><meta name="apple-mobile-web-app-capable" content="yes"><link rel="manifest" href="./manifest.webmanifest"><link rel="apple-touch-icon" href="./icon-192.png">'
    hosted = page.replace('</head>', metadata + '</head>')
    (DIST / "index.html").write_text(hosted, encoding="utf-8")
    manifest = {"id": "./", "name": "ICT 练习室", "short_name": "ICT刷题", "start_url": "./index.html", "scope": "./", "display": "standalone", "lang": "zh-CN", "background_color": "#f7f8fa", "theme_color": "#142c35", "icons": [{"src": f"./icon-{s}.png", "sizes": f"{s}x{s}", "type": "image/png", "purpose": "any maskable"} for s in (192, 512)]}
    (DIST / "manifest.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    for size in (192, 512):
        (DIST / f"icon-{size}.png").write_bytes(icon_png(size))
    version = hashlib.sha256((hosted + portal).encode("utf-8")).hexdigest()[:12]
    sw = '''const CACHE = "ict-mobile-VERSION";
const ASSETS = ["./index.html", "./mobile.html", "./mobile-qr.png", "./manifest.webmanifest", "./icon-192.png", "./icon-512.png"];
self.addEventListener("install", event => event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(ASSETS)).then(() => self.skipWaiting())));
self.addEventListener("activate", event => event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k.startsWith("ict-mobile-") && k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())));
self.addEventListener("fetch", event => {
  const url = new URL(event.request.url);
  if (event.request.method !== "GET" || url.origin !== self.location.origin) return;
  if (event.request.mode === "navigate") {
    const pageKey = url.pathname === new URL("./mobile.html", self.location.href).pathname ? "./mobile.html" : "./index.html";
    event.respondWith(fetch(event.request).then(response => {
      if (response.ok && response.headers.get("content-type")?.includes("text/html")) {
        const copy = response.clone(); event.waitUntil(caches.open(CACHE).then(cache => cache.put(pageKey, copy)));
      }
      return response;
    }).catch(() => caches.match(pageKey)));
  } else event.respondWith(caches.match(event.request).then(response => response || fetch(event.request)));
});
'''.replace("VERSION", version)
    (DIST / "sw.js").write_text(sw, encoding="utf-8")
    # Root files support GitHub Pages from main / (root), plus the old quiz URL.
    for filename in ("index.html", "mobile.html", "manifest.webmanifest", "sw.js", "icon-192.png", "icon-512.png"):
        (ROOT / filename).write_bytes((DIST / filename).read_bytes())
    (ROOT / "quiz.html").write_bytes((DIST / "index.html").read_bytes())
    (ROOT / ".nojekyll").write_text("", encoding="ascii")
    print(f"Mobile build: {len(bank['questions'])} questions, {len(page.encode('utf-8')):,} bytes, offline images embedded")


if __name__ == "__main__":
    main()
