"""Package a portable website without any user's practice records or QA files."""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
output = ROOT / "ICT练习室.zip"
included = [ROOT / name for name in ("README.md", "app.py", "启动网站.cmd", "手机独立版.html", "使用说明.md", ".gitignore", ".gitattributes", ".nojekyll", "index.html", "quiz.html", "manifest.webmanifest", "sw.js", "icon-192.png", "icon-512.png")]
included.extend(ROOT.glob("*.docx"))
included.extend(ROOT.glob("*.pdf"))
for name in ("web", "exports", "review", "scripts", "tests", "data", "mobile-site/dist"):
    included.extend(file for file in (ROOT / name).rglob("*")
                    if file.is_file() and "__pycache__" not in file.parts
                    and ".sqlite3" not in file.name and file.suffix != ".pyc")
with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
    for file in sorted(set(included)):
        archive.write(file, Path("ICT练习室") / file.relative_to(ROOT))
with zipfile.ZipFile(output) as archive:
    assert archive.testzip() is None
    assert not any("sqlite3" in name or "/qa/" in name for name in archive.namelist())
print(f"Packaged {len(set(included))} files: {output.name} ({output.stat().st_size:,} bytes)")
