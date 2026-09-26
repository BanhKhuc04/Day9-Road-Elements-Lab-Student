"""Gộp gold_part.csv + cards_part.md của 4 thành viên vào project/ (nhóm trưởng chạy trước make freeze).

Chạy trong guideline-challenge/:  python3 team_work/merge_gold.py [--write]
Không có --write thì chỉ kiểm và in thống kê.
"""
import csv
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
TEAM = BASE / "team_work"
PARTS = {
    "tv1_Chien27803": {"VN12", "VN15"},
    "tv2_BanhKhuc04": {"VN13"},
    "tv3_congmanhbui0804": {"VN16"},
    "tv4_Yuh5124": {"VN14"},
}
FIELDS = ["sample_id", "decision_id", "expected", "severity", "rationale"]
SEVERITY = {"critical", "major", "minor"}
CARD_HEADER = "`make status` đếm số dòng `CASE ID:` đã điền (đã thay placeholder). Copy khối dưới cho mỗi case."


def load_parts():
    rows, errors = [], []
    for folder, samples in PARTS.items():
        path = TEAM / folder / "gold_part.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != FIELDS:
                errors.append(f"{path.relative_to(BASE)}: header phải là {','.join(FIELDS)}")
                continue
            part = [row for row in reader if any((value or "").strip() for value in row.values())]
        seen_samples = set()
        for number, row in enumerate(part, start=2):
            where = f"{folder}/gold_part.csv dòng {number}"
            if None in row:
                errors.append(f"{where}: thừa cột (có dấu phẩy trong expected/rationale?)")
                continue
            if any(not (row[field] or "").strip() for field in FIELDS):
                errors.append(f"{where}: thiếu cột")
            if row["sample_id"] not in samples:
                errors.append(f"{where}: {row['sample_id']} không phải ảnh của {folder}")
            if row["severity"] not in SEVERITY:
                errors.append(f"{where}: severity '{row['severity']}' không hợp lệ")
            if "TODO" in ",".join(row.values()):
                errors.append(f"{where}: còn TODO")
            seen_samples.add(row["sample_id"])
            rows.append(row)
        for sample in sorted(samples - seen_samples):
            errors.append(f"{folder}: {sample} chưa có decision nào")
    keys = [(row["sample_id"], row["decision_id"]) for row in rows]
    for key in sorted({key for key in keys if keys.count(key) > 1}):
        errors.append(f"trùng decision {key[0]}/{key[1]}")
    return rows, errors


def load_cards():
    blocks, errors = [], []
    for folder in PARTS:
        text = (TEAM / folder / "cards_part.md").read_text(encoding="utf-8")
        text = text.split("## Câu hỏi cho nhóm trưởng")[0]
        for block in re.findall(r"^CASE ID:.*?(?=\n---|\Z)", text, flags=re.S | re.M):
            block = block.strip()
            if "TODO" in block:
                errors.append(f"{folder}/cards_part.md: card {block.splitlines()[0]} còn TODO")
            blocks.append(block)
    return blocks, errors


def main():
    rows, errors = load_parts()
    cards, card_errors = load_cards()
    errors += card_errors
    critical = sum(row["severity"] == "critical" for row in rows)
    geometry = sum(row["expected"].strip().lower().startswith("geometry:") for row in rows)
    print(f"decisions={len(rows)} critical={critical} geometry={geometry} cards={len(cards)}")
    if len(rows) < 10:
        errors.append("gold cần ≥ 10 decision")
    if critical < 2:
        errors.append("gold cần ≥ 2 critical")
    if geometry < 1:
        errors.append("gold cần ≥ 1 decision bắt đầu bằng 'geometry:'")
    if len(cards) < 8:
        errors.append("edge_case_cards cần ≥ 8 card")
    for error in errors:
        print(f"✗ {error}")
    if errors:
        return 1
    if "--write" not in sys.argv:
        print("✓ Hợp lệ. Chạy lại với --write để ghi vào project/.")
        return 0
    gold = BASE / "project" / "04_edge_cases" / "gold_decisions.csv"
    with gold.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    cards_path = BASE / "project" / "04_edge_cases" / "edge_case_cards.md"
    head = cards_path.read_text(encoding="utf-8").split(CARD_HEADER)[0] + CARD_HEADER + "\n"
    cards_path.write_text(head + "".join(f"\n---\n\n{card}\n" for card in cards) + "\n---\n", encoding="utf-8")
    print(f"✓ Đã ghi {gold.relative_to(BASE)} và {cards_path.relative_to(BASE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
