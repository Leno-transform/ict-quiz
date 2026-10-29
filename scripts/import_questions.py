"""Read the source DOCX without changing it; flag defects and exact duplicates."""
import json
import re
import unicodedata
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def normalize(text):
    # Preserve IP separators, prefix lengths, decimal points and minus signs.
    # Erasing all punctuation could incorrectly merge 1.01 with 10.1 or -1 with 1.
    text = unicodedata.normalize("NFKC", text).lower()
    return re.sub(r"[\s，,。；;？?！!、\"'“”‘’（）()]+", "", text)


def main():
    source = ROOT / "ICT网络赛道知识题库(1).docx"
    with zipfile.ZipFile(source) as archive:
        xml = ET.fromstring(archive.read("word/document.xml"))
    lines = ["".join(t.text or "" for t in p.findall(".//w:t", NS)).strip()
             for p in xml.findall(".//w:body//w:p", NS)]
    questions = []
    current = None
    active_option = None
    for text in lines:
        if not text:
            continue
        start = re.match(r"^(\d+)[．.、]\s*(.*)", text)
        option = re.match(r"^([A-F])[．.、]\s*(.*)", text)
        answer = re.match(r"^答案\s*[:：]\s*(.*)", text)
        if start:
            if current:
                questions.append(current)
            current = {"id": int(start[1]), "stem": start[2], "options": {}, "answer": ""}
            active_option = None
        elif current and answer:
            current["answer"] = re.sub(r"\s", "", answer[1]).upper()
            active_option = None
        elif current and option:
            active_option = option[1]
            current["options"][active_option] = option[2]
        elif current:
            if active_option:
                current["options"][active_option] += " " + text
            elif not current["answer"]:
                current["stem"] += " " + text
    if current:
        questions.append(current)
    seen = {}
    for q in questions:
        values = [normalize(v) for v in q["options"].values()]
        q["type"] = ("judge" if set(values) == {"正确", "错误"} else
                     "multiple" if len(q["answer"]) > 1 and q["answer"] != "空" else "single")
        reasons = []
        if not q["stem"].strip() or len(q["options"]) < 2 or any(not v.strip() for v in q["options"].values()):
            reasons.append("题干或选项残缺")
        if not re.fullmatch(r"[A-F]+", q["answer"]) or not set(q["answer"]) <= set(q["options"]):
            reasons.append("答案缺失或不对应选项")
        if re.search(r"如图|上图|下图|图中|图示", q["stem"]):
            reasons.append("原文缺少题目引用的图示")
        # Sort option texts: identical questions with reordered options are duplicates.
        key = normalize(q["stem"]) + "|" + "|".join(sorted(values))
        if key in seen:
            reasons.append(f"与原题 {seen[key]} 重复")
        else:
            seen[key] = q["id"]
        q["initial_exclusion_reasons"] = reasons
    out = ROOT / "data"
    out.mkdir(exist_ok=True)
    (out / "source_questions.json").write_text(json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8")
    chunks = ROOT / "review"
    chunks.mkdir(exist_ok=True)
    for name, low, high in [("a", 1, 264), ("b", 265, 528), ("c", 529, 792)]:
        chunk = [q for q in questions if low <= q["id"] <= high]
        (chunks / f"questions_{name}.json").write_text(json.dumps(chunk, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"source": len(questions), "flagged": sum(bool(q["initial_exclusion_reasons"]) for q in questions)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
