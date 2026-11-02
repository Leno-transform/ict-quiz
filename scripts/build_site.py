"""Build the multi-file hosted website: small pages, one JSON bank, image files.

Why: the single-file build is ~22 MB because the bank, explanations, images and the
materials zip are base64-embedded. GitHub Pages web upload rejects huge files, and a
phone on mobile data should not download 22 MB before the first question.

Layout of the generated site (also copied to the repository root for GitHub Pages):
    index.html  quiz.html  mobile.html
    app.js  style.css  offline.js
    questions.json                 full bank, answers + explanations (also the structured export)
    assets/                        one file per question figure
    exports-explanations.md  exports-cleaning.md
    sw.js  manifest.webmanifest  icon-192.png  icon-512.png  mobile-qr.png  .nojekyll
"""
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "mobile-site" / "dist"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_mobile import icon_png  # noqa: E402  (same folder, avoids duplicating the icon painter)

SITE_FILES = ("index.html", "quiz.html", "mobile.html", "app.js", "style.css", "offline.js",
              "questions.json", "sw.js", "manifest.webmanifest", "icon-192.png", "icon-512.png",
              ".nojekyll", "mobile-qr.png", "exports-explanations.md", "exports-cleaning.md")
EXPORTS = {"explanations": "题库及解析.md", "cleaning": "题库清理报告.md"}
PWA_META = ('<meta name="theme-color" content="#142c35"><meta name="apple-mobile-web-app-capable" content="yes">'
            '<link rel="manifest" href="./manifest.webmanifest"><link rel="apple-touch-icon" href="./icon-192.png">')


def js_string(value):
    return json.dumps(value, ensure_ascii=False)


def build_page(bank):
    """Desktop/mobile practice page, rewritten to load local files instead of the Python API."""
    count = len(bank["questions"])
    page = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
    page = page.replace('href="/"', 'href="./index.html"')
    page = page.replace('<link rel="stylesheet" href="/style.css"><script src="/app.js" defer></script>',
                        '<link rel="stylesheet" href="./style.css">'
                        '<script src="./offline.js" defer></script><script src="./app.js" defer></script>')
    # The static build has no server-side exports: drop the materials zip, point the rest at real files.
    page = page.replace('<a href="/exports/materials.zip" download>完整资料包 · 含全部解析与图片</a>', "")
    page = page.replace('href="/exports/explanations.md" download', 'href="./exports-explanations.md" download')
    page = page.replace('href="/exports/questions.json" download', 'href="./questions.json" download')
    page = page.replace('href="/exports/cleaning.md" download', 'href="./exports-cleaning.md" download')
    page = page.replace('<a href="/api/backup" download>我的学习记录 · JSON</a>',
                        '<a href="#" data-export="backup" download>我的学习记录 · JSON</a>')
    page = page.replace("<title>ICT 练习室</title>", f"<title>ICT 练习室 · {count} 题</title>")
    page = page.replace("本地运行 · 记录自动保存", "网页版 · 记录保存在本机")
    page = page.replace('<section class="page-heading">',
                        f'<p class="mobile-edition">手机版 · {count} 题 · 解析与图片均已内置</p><section class="page-heading">')
    status = ('<div id="mobile-status" class="mobile-status" role="status"></div>'
              '<button id="mobile-install" class="secondary-button install-button" hidden>安装到主屏幕</button>'
              '<details class="mobile-help"><summary>手机安装与保存说明</summary>'
              '<p>iPhone：用 Safari 打开网址，点击分享 → 添加到主屏幕。安卓：使用 Chrome 菜单里的“安装应用”或“添加到主屏幕”。'
              '首次打开后等上方显示“离线就绪”，题库与图片就缓存到本机了。</p>'
              '<p>学习记录保存在这台设备的当前浏览器中，不与电脑版自动同步。清除网站数据会删除记录，建议定期从“导出资料”备份。</p></details>')
    page = page.replace('<div class="bank-note" id="bank-note"></div>',
                        '<div class="bank-note" id="bank-note"></div>' + status)
    return page.replace("</head>", PWA_META + "</head>")


def build_portal(bank):
    """Phone entry page (no 22 MB download card: the site itself works offline)."""
    count = len(bank["questions"])
    portal = (ROOT / "web" / "mobile.html").read_text(encoding="utf-8")
    for key, value in {"QUESTION_COUNT": count, "FIGURE_COUNT": bank["summary"]["image_count"],
                       "BANK_VERSION": bank["version"], "RELEASE_FILENAME": ""}.items():
        portal = portal.replace("{{" + key + "}}", str(value))
    portal = re.sub(r'\n  <section class="card">\n    <h2>也保留单文件离线版</h2>.*?</section>', "", portal, flags=re.S)
    portal = portal.replace('<span class="badge">手机独立版 ·', '<span class="badge">手机版 ·')
    return portal


def build_service_worker(version, assets):
    precache = ["./index.html", "./quiz.html", "./mobile.html", "./questions.json", "./app.js", "./style.css",
                "./offline.js", "./manifest.webmanifest", "./icon-192.png", "./icon-512.png"] + assets
    template = """const CACHE = "ict-site-__VERSION__";
const PRECACHE = __PRECACHE__;
self.addEventListener("install", event => event.waitUntil((async () => {
  const cache = await caches.open(CACHE);
  await cache.addAll(PRECACHE.slice(0, 10));
  for (const url of PRECACHE.slice(10)) await cache.add(url).catch(() => {});
  await self.skipWaiting();
})()));
self.addEventListener("activate", event => event.waitUntil((async () => {
  const keys = await caches.keys();
  await Promise.all(keys.filter(k => k.startsWith("ict-") && k !== CACHE).map(k => caches.delete(k)));
  await self.clients.claim();
})()));
self.addEventListener("fetch", event => {
  const url = new URL(event.request.url);
  if (event.request.method !== "GET" || url.origin !== self.location.origin) return;
  if (event.request.mode === "navigate") {
    const pageKey = url.pathname.endsWith("/mobile.html") ? "./mobile.html" : "./index.html";
    event.respondWith(fetch(event.request).then(response => {
      if (response.ok && response.headers.get("content-type")?.includes("text/html")) {
        const copy = response.clone();
        event.waitUntil(caches.open(CACHE).then(cache => cache.put(pageKey, copy)));
      }
      return response;
    }).catch(() => caches.match(pageKey)));
    return;
  }
  event.respondWith(caches.match(event.request).then(hit => hit || fetch(event.request).then(response => {
    if (response.ok) {
      const copy = response.clone();
      event.waitUntil(caches.open(CACHE).then(cache => cache.put(event.request, copy)));
    }
    return response;
  })));
});
"""
    return template.replace("__VERSION__", version).replace("__PRECACHE__", js_string(precache))


def main():
    raw = (ROOT / "data" / "questions.json").read_bytes()
    bank = json.loads(raw.decode("utf-8"))
    bank["version"] = hashlib.sha256(raw).hexdigest()[:12]
    count = len(bank["questions"])
    for question in bank["questions"]:
        image = question.get("image")
        if image:
            # 配图沿用仓库里已有的 web/assets/，发布时不必再上传一份 206 个文件。
            image["src"] = "web/assets/" + Path(image["src"]).name
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    (DIST / "questions.json").write_text(json.dumps(bank, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    shutil.copytree(ROOT / "web" / "assets", DIST / "web" / "assets")
    for name in ("app.js", "style.css", "offline.js"):
        (DIST / name).write_bytes((ROOT / "web" / name).read_bytes())
    for key, filename in EXPORTS.items():
        (DIST / f"exports-{key}.md").write_text((ROOT / "exports" / filename).read_text(encoding="utf-8"), encoding="utf-8")
    (DIST / "mobile-qr.png").write_bytes((ROOT / "mobile-qr.png").read_bytes())
    page = build_page(bank)
    (DIST / "index.html").write_text(page, encoding="utf-8")
    (DIST / "quiz.html").write_text(page, encoding="utf-8")
    (DIST / "mobile.html").write_text(build_portal(bank), encoding="utf-8")
    manifest = {"id": "./", "name": "ICT 练习室", "short_name": "ICT刷题", "start_url": "./index.html", "scope": "./",
                "display": "standalone", "lang": "zh-CN", "background_color": "#f7f8fa", "theme_color": "#142c35",
                "icons": [{"src": f"./icon-{s}.png", "sizes": f"{s}x{s}", "type": "image/png", "purpose": "any maskable"} for s in (192, 512)]}
    (DIST / "manifest.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    for size in (192, 512):
        (DIST / f"icon-{size}.png").write_bytes(icon_png(size))
    (DIST / ".nojekyll").write_text("", encoding="ascii")
    assets = ["./web/assets/" + path.name for path in sorted((DIST / "web" / "assets").iterdir()) if path.is_file()]
    version = hashlib.sha256((page.encode() + json.dumps(bank, sort_keys=True, ensure_ascii=False).encode())).hexdigest()[:12]
    (DIST / "sw.js").write_text(build_service_worker(version, assets), encoding="utf-8")
    # Publish from the repository root, which is what GitHub Pages serves.
    for name in SITE_FILES:
        (ROOT / name).write_bytes((DIST / name).read_bytes())
    shutil.rmtree(ROOT / "assets", ignore_errors=True)   # 旧的多文件布局，已改为复用 web/assets/
    sizes = sorted(((p.stat().st_size, p.relative_to(DIST).as_posix()) for p in DIST.rglob("*") if p.is_file()), reverse=True)
    total = sum(size for size, _ in sizes)
    print(f"Hosted site: {count} questions, {len(assets)} figures, {len(sizes)} files, {total / 1024 / 1024:.1f} MB total")
    print(f"Largest files: " + ", ".join(f"{name} {size / 1024 / 1024:.2f} MB" for size, name in sizes[:3]))
    print(f"Cache version: {version}")


if __name__ == "__main__":
    main()
