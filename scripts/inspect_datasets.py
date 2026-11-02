"""
Dataset Inspection Script.
Inspects raw external source datasets and custom project datasets.
Reports:
- filename
- record count
- columns
- language
- labels
- safe/attack distribution
- missing values
- duplicate records
- relevant fields
"""

import sys
import csv
import json
from pathlib import Path
from collections import Counter

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

def inspect_file(filepath: Path):
    print(f"\n==================================================")
    print(f"INSPECTING: {filepath.relative_to(PROJECT_ROOT)}")
    print(f"==================================================")
    
    if not filepath.exists():
        print(f"File does not exist: {filepath}")
        return
        
    records = []
    fieldnames = []
    
    if filepath.suffix.lower() == ".csv":
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames or []
            records = list(reader)
    elif filepath.suffix.lower() == ".json":
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                records = data
                if records:
                    fieldnames = list(records[0].keys())
            elif isinstance(data, dict):
                records = [data]
                fieldnames = list(data.keys())
    else:
        print(f"Unsupported format: {filepath.suffix}")
        return

    total_records = len(records)
    print(f"Total Records: {total_records}")
    print(f"Columns ({len(fieldnames)}): {', '.join(fieldnames)}")
    
    # Missing values
    missing_counts = {col: 0 for col in fieldnames}
    for r in records:
        for col in fieldnames:
            val = r.get(col, "")
            if val is None or str(val).strip() == "":
                missing_counts[col] += 1
    total_missing = sum(missing_counts.values())
    print(f"Missing Values: {total_missing}")
    if total_missing > 0:
        for col, count in missing_counts.items():
            if count > 0:
                print(f"  - {col}: {count} missing")

    # Duplicate check on 'id' if present, or all keys
    if "id" in fieldnames:
        ids = [r["id"] for r in records]
        dup_ids = len(ids) - len(set(ids))
        print(f"Duplicate IDs: {dup_ids}")
    else:
        tuples = [tuple(r.get(c, "") for c in fieldnames) for r in records]
        dup_rows = len(tuples) - len(set(tuples))
        print(f"Duplicate Rows: {dup_rows}")

    # Language distribution if present
    if "language" in fieldnames:
        lang_counts = Counter(r.get("language", "") for r in records)
        print(f"Language Distribution: {dict(lang_counts)}")

    # Label distribution if present
    if "label" in fieldnames:
        label_counts = Counter(r.get("label", "") for r in records)
        print(f"Label Distribution: {dict(label_counts)}")

    # Attack type distribution if present
    if "attack_type" in fieldnames:
        attack_counts = Counter(r.get("attack_type", "") for r in records if r.get("label") == "ATTACK")
        print(f"Attack Type Distribution (ATTACK records): {dict(attack_counts)}")

def main():
    print("DATASET INSPECTION UTILITY")
    print("Project: Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents")
    
    # 1. Inspect raw datasets directory
    raw_dir = DATA_DIR / "raw_datasets"
    raw_files = list(raw_dir.glob("**/*.csv")) + list(raw_dir.glob("**/*.json"))
    if raw_files:
        print(f"\nFound {len(raw_files)} raw dataset files in data/raw_datasets/:")
        for f in raw_files:
            inspect_file(f)
    else:
        print("\nNo raw external dataset files currently deposited in data/raw_datasets/.")
        print("Subdirectories ready for external ingestion: hindi_hinglish/, comi_lingua/, tenglish/.")

    # 2. Inspect custom project dataset
    custom_dir = DATA_DIR / "custom_dataset"
    if custom_dir.exists():
        custom_files = [
            custom_dir / "custom_2000_dataset.csv",
            custom_dir / "english_master.csv",
            custom_dir / "hindi_dataset.csv",
            custom_dir / "telugu_dataset.csv",
            custom_dir / "telugu_english_dataset.csv",
            custom_dir / "train.csv",
            custom_dir / "validation.csv",
            custom_dir / "test.csv",
        ]
        for f in custom_files:
            if f.exists():
                inspect_file(f)

if __name__ == "__main__":
    main()
