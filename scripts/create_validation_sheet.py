"""
Script to create/regenerate the manual human validation sheet (manual_validation.csv).
Allows human evaluators and annotators to record review notes on task validity,
translation fidelity, attack intent preservation, and code-mixing naturalness.
"""

import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "custom_dataset"
INPUT_DATASET = DATA_DIR / "custom_2000_dataset.csv"
OUTPUT_SHEET = DATA_DIR / "manual_validation.csv"

VALIDATION_COLUMNS = [
    "scenario_id",
    "language",
    "task_ok",
    "translation_ok",
    "attack_intent_preserved",
    "document_relevant",
    "label_correct",
    "code_mix_natural",
    "reviewer_notes",
]

def create_validation_sheet():
    if not INPUT_DATASET.exists():
        raise FileNotFoundError(f"Input dataset not found: {INPUT_DATASET}")
        
    with open(INPUT_DATASET, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        records = list(reader)
        
    rows = []
    # Distinct scenario-language pairs (250 scenarios * 4 languages = 1,000 scenario-language audit items, or all 2,000 records)
    for r in records:
        rows.append({
            "scenario_id": r["scenario_id"],
            "language": r["language"],
            "task_ok": "pending",
            "translation_ok": "pending",
            "attack_intent_preserved": "pending",
            "document_relevant": "pending",
            "label_correct": "pending",
            "code_mix_natural": "pending",
            "reviewer_notes": ""
        })
        
    with open(OUTPUT_SHEET, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=VALIDATION_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Manual validation review sheet created with {len(rows)} entries at: {OUTPUT_SHEET}")

if __name__ == "__main__":
    create_validation_sheet()
