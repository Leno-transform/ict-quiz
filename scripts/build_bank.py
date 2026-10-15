"""Combine human-reviewed explanations, deduplicate, and export all decisions."""
import json
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from import_questions import normalize

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main():
    source = load(ROOT / "data" / "source_questions.json")
    reviews = []
    for letter in "abc":
        reviews.extend(load(ROOT / "review" / f"review_{letter}.json"))
    reviewed = {r["id"]: r for r in reviews}
    if len(reviewed) != len(source) or len(reviews) != len(source) or set(reviewed) != {q["id"] for q in source}:
        raise ValueError("审核记录数量或题号与原题库不一致，拒绝生成。")
    for qid, changes in load(ROOT / "review" / "main_overrides.json").items():
        reviewed[int(qid)].update(changes)
    semantic = {int(k): v for k, v in load(ROOT / "review" / "semantic_duplicates.json").items()}
    groups = {q["id"]: q["id"] for q in source}

    def find(i):
        while groups[i] != i:
            groups[i] = groups[groups[i]]
            i = groups[i]
        return i

    def union(a, b):
        a, b = find(a), find(b)
        groups[max(a, b)] = min(a, b)

    for q in source:
        for reason in q["initial_exclusion_reasons"]:
            match = re.match(r"与原题 (\d+) 重复", reason)
            if match:
                union(q["id"], int(match[1]))
    for duplicate, original in semantic.items():
        union(duplicate, original)
    for r in reviews:
        if r.get("duplicate_of"):
            union(r["id"], int(r["duplicate_of"]))
    seen_keys = {}
    prepared = {}
    for original in source:
        q, r = dict(original), reviewed[original["id"]]
        if r.get("corrected_stem"):
            q["stem"] = r["corrected_stem"]
        if r.get("corrected_options"):
            q["options"] = r["corrected_options"]
        if r.get("corrected_answer"):
            q["answer"] = r["corrected_answer"]
        q["explanation"], q["topic"] = r["explanation"].strip(), r["topic"]
        q["sources"] = list(dict.fromkeys(r.get("sources", [])))
        q["image"] = None
        q["original_answer"] = original["answer"]
        q["type"] = ("judge" if {normalize(v) for v in q["options"].values()} == {"正确", "错误"}
                     else "multiple" if len(q["answer"]) > 1 and q["answer"] != "空" else "single")
        if q["id"] in (12, 157, 498) and r["status"] == "keep":
            labels = {12: "交换机与主机连接示意图", 157: "Telnet 与 FTP 的业务关系示意图", 498: "题干给出的 RADIUS 配置"}
            q["image"] = {"src": f"/assets/question-{q['id']}.svg", "alt": labels[q["id"]],
                          "caption": "依据题干文字重绘的示意图，非原图复原；未补入缺失的网络参数。"}
        reasons = []
        if r["status"] == "exclude":
            reasons.append(r["reason"] or "无法可靠判定")
        if not re.fullmatch(r"[A-F]+", q["answer"]) or not set(q["answer"]) <= set(q["options"]):
            reasons.append("答案缺失或不对应选项")
        if len(q["options"]) < 2 or not q["stem"].strip() or any(not v.strip() for v in q["options"].values()):
            reasons.append("题干或选项残缺")
        if re.search(r"如图|上图|下图|图中|图示", q["stem"]) and not q["image"]:
            reasons.append("缺少必需图示，无法可靠恢复")
        if not q["explanation"] and not reasons:
            raise ValueError(f"原题 {q['id']} 尚无解析")
        if not q["sources"] and not reasons:
            raise ValueError(f"原题 {q['id']} 尚无核对来源")
        key = normalize(q["stem"]) + "|" + "|".join(sorted(normalize(v) for v in q["options"].values()))
        if key in seen_keys:
            union(q["id"], seen_keys[key])
        else:
            seen_keys[key] = q["id"]
        prepared[q["id"]] = (q, reasons)
    # Keep the first valid representative, even if an earlier copy was damaged.
    representatives = {}
    for q, reasons in prepared.values():
        if not reasons:
            representatives.setdefault(find(q["id"]), q["id"])
    kept, removed, corrections = [], [], []
    for original in source:
        q, reasons = prepared[original["id"]]
        representative = representatives.get(find(q["id"]))
        if representative and representative != q["id"]:
            removed.append({"id": q["id"], "category": "duplicate", "reason": f"与保留的原题 {representative} 为重复题（含选项换序、标点及 OCR 差异）", "duplicate_of": representative, "stem": original["stem"]})
        elif reasons:
            removed.append({"id": q["id"], "category": "invalid", "reason": "；".join(dict.fromkeys(reasons)), "stem": original["stem"]})
        else:
            kept.append({k: v for k, v in q.items() if k != "initial_exclusion_reasons"})
            changes = {}
            for field in ("stem", "options", "answer"):
                if original[field] != q[field]:
                    changes[field] = {"before": original[field], "after": q[field]}
            if changes:
                corrections.append({"id": q["id"], "changes": changes, "explanation": q["explanation"], "sources": q["sources"]})
    summary = {"source_count": len(source), "kept_count": len(kept),
               "duplicate_count": sum(r["category"] == "duplicate" for r in removed),
               "invalid_count": sum(r["category"] == "invalid" for r in removed),
               "answer_correction_count": sum("answer" in r["changes"] for r in corrections),
               "text_correction_count": sum("stem" in r["changes"] or "options" in r["changes"] for r in corrections),
               "image_count": sum(bool(q["image"]) for q in kept), "types": dict(Counter(q["type"] for q in kept))}
    assert summary["source_count"] == summary["kept_count"] + summary["duplicate_count"] + summary["invalid_count"]
    payload = {"title": "ICT 网络赛道题库与简短解析", "summary": summary, "questions": kept}
    (ROOT / "data" / "questions.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    exports = ROOT / "exports"
    exports.mkdir(exist_ok=True)
    (exports / "题库及解析.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    markdown = ["# ICT 网络赛道题库与简短解析", "", f"原题 {len(source)} 道，清理后保留 {len(kept)} 道。原题号保留，便于核对。", "",
                "图示依据题干文字重绘，已在图下标注；答案、文字修正与剔除明细见《题库清理报告》。", ""]
    names = {"single": "单选", "multiple": "多选", "judge": "判断"}
    for q in kept:
        markdown.extend([f"## 原题 {q['id']} · {names[q['type']]} · {q['topic']}", "", q["stem"], ""])
        if q["image"]:
            markdown.extend([f"![{q['image']['alt']}](图片/question-{q['id']}.svg)", "", q["image"]["caption"], ""])
        markdown.extend(f"- **{k}.** {v}" for k, v in q["options"].items())
        markdown.extend(["", f"**答案：{'、'.join(q['answer'])}**", "", f"**解析：** {q['explanation']}", ""])
        markdown.append("参考依据：" + "；".join(f"[来源 {i+1}]({url})" for i, url in enumerate(q["sources"])))
        markdown.append("")
    (exports / "题库及解析.md").write_text("\n".join(markdown), encoding="utf-8")
    images_dir = exports / "图片"
    images_dir.mkdir(exist_ok=True)
    for q in kept:
        if q["image"]:
            path = ROOT / "web" / q["image"]["src"].lstrip("/")
            (images_dir / path.name).write_bytes(path.read_bytes())
    report = ["# ICT 题库清理与修正报告", "", "原始 Word 文档未修改。题目和答案按协议或产品资料核对，无法可靠判断的题目剔除。", "",
              f"原题 {summary['source_count']} 道；保留 {summary['kept_count']} 道；剔除重复 {summary['duplicate_count']} 道、残缺或存疑 {summary['invalid_count']} 道。", "",
              f"保留题中修正答案 {summary['answer_correction_count']} 道，修复文字或选项 {summary['text_correction_count']} 道，配图 {summary['image_count']} 道。", "",
              "去重规则：题干和选项进行 Unicode、空白、标点与大小写归一化；选项换序仍视为重复。相似文本再逐对检查，保留条件和语义相同的第一道可用题。不会把仅考点相同、条件不同的题合并。", "",
              "所有保留题都有简短解析与参考资料链接。资料核对使用协议标准和厂家官方资料；部分华为详细页面直接访问返回 403，但官方搜索结果能提供相关正文，这不代表已读取该页面全部内容。题库包含华为设备相关题，资料版本或设备型号可能影响行为；缺少必要条件时不纳入练习。", "",
              "## 剔除明细", "", "| 原题号 | 分类 | 原因 |", "| --- | --- | --- |"]
    report.extend(f"| {r['id']} | {'重复' if r['category']=='duplicate' else '残缺或存疑'} | {r['reason'].replace('|','／')} |" for r in removed)
    report.extend(["", "## 保留题的答案修正", "", "| 原题号 | 原答案 | 修正答案 | 依据与解析 |", "| --- | --- | --- | --- |"])
    for r in corrections:
        if "answer" in r["changes"]:
            change = r["changes"]["answer"]
            report.append(f"| {r['id']} | {change['before']} | {change['after']} | {r['explanation'].replace('|','／')} " + " ".join(f"[依据 {i+1}]({u})" for i,u in enumerate(r["sources"])) + " |")
    report.extend(["", "## 文字修复记录", ""])
    for r in corrections:
        for field in ("stem", "options"):
            if field in r["changes"]:
                change = r["changes"][field]
                report.extend([f"### 原题 {r['id']} {'题干' if field=='stem' else '选项'}", "", "修复前：" + json.dumps(change["before"], ensure_ascii=False), "", "修复后：" + json.dumps(change["after"], ensure_ascii=False), ""])
    (exports / "题库清理报告.md").write_text("\n".join(report), encoding="utf-8")
    (exports / "题库清理明细.json").write_text(json.dumps({"summary": summary, "removed": removed, "corrections": corrections}, ensure_ascii=False, indent=2), encoding="utf-8")
    with zipfile.ZipFile(exports / "题库资料.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        for file in sorted(exports.rglob("*")):
            if file.is_file() and file.suffix != ".zip":
                archive.write(file, file.relative_to(exports))
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
