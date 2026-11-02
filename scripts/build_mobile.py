"""Build the self-contained single-file phone edition (one HTML file, ~22 MB).

This is only for copying the whole course to a phone by hand (USB, WeChat file
transfer, cloud drive). The published website is built by scripts/build_site.py,
which keeps the page, the bank and the figures as separate small files.
"""
import base64
import hashlib
import json
import mimetypes
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


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
    bank = json.loads((ROOT / "data" / "questions.json").read_text(encoding="utf-8"))
    bank["version"] = hashlib.sha256((ROOT / "data" / "questions.json").read_bytes()).hexdigest()[:12]
    count = len(bank["questions"])
    release_filename = f"ICT手机独立版-{count}题.html"
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
    print(f"Single-file edition: {count} questions, {len(page.encode('utf-8')):,} bytes, figures embedded ({release_filename})")


if __name__ == "__main__":
    main()
