"""
Automated Pytest Suite for Custom Multilingual Indirect Prompt Injection Dataset.
Verifies all schema constraints, scenario balances, split integrity, and data quality.
"""

import csv
import json
from pathlib import Path
from collections import Counter, defaultdict
import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "custom_dataset"

REQUIRED_COLUMNS = [
    "id",
    "scenario_id",
    "language",
    "task",
    "document_text",
    "attack_type",
    "label",
    "source",
    "translation_method",
    "code_mix_type",
    "validation_status",
]

EXPECTED_LANGUAGES = {"English", "Hindi", "Telugu", "Telugu-English"}
EXPECTED_LABELS = {"SAFE", "ATTACK"}
EXPECTED_ATTACK_CATEGORIES = {
    "instruction_override",
    "ignore_previous_instruction",
    "system_prompt_extraction",
    "confidential_information_disclosure",
    "task_redirection",
    "fake_authority",
    "context_manipulation",
    "tool_use_manipulation",
    "malicious_action",
    "misleading_document_instruction",
}

@pytest.fixture(scope="module")
def dataset_records():
    csv_file = DATA_DIR / "custom_2000_dataset.csv"
    assert csv_file.exists(), f"Dataset CSV missing: {csv_file}"
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader), reader.fieldnames

@pytest.fixture(scope="module")
def json_records():
    json_file = DATA_DIR / "custom_2000_dataset.json"
    assert json_file.exists(), f"Dataset JSON missing: {json_file}"
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)

def test_dataset_size_and_columns(dataset_records, json_records):
    records, fieldnames = dataset_records
    assert len(records) == 2000, f"Expected 2000 records in CSV, found {len(records)}"
    assert len(json_records) == 2000, f"Expected 2000 records in JSON, found {len(json_records)}"
    assert fieldnames == REQUIRED_COLUMNS, f"Columns mismatch: {fieldnames}"

def test_scenario_counts_and_completeness(dataset_records):
    records, _ = dataset_records
    scenario_counts = Counter(r["scenario_id"] for r in records)
    assert len(scenario_counts) == 250, f"Expected 250 unique scenarios, found {len(scenario_counts)}"
    
    # Every scenario must have exactly 8 records
    for s_id, count in scenario_counts.items():
        assert count == 8, f"Scenario {s_id} has {count} records instead of 8"

def test_language_distribution(dataset_records):
    records, _ = dataset_records
    lang_counts = Counter(r["language"] for r in records)
    assert set(lang_counts.keys()) == EXPECTED_LANGUAGES
    assert lang_counts["English"] == 500
    assert lang_counts["Hindi"] == 500
    assert lang_counts["Telugu"] == 500
    assert lang_counts["Telugu-English"] == 500

def test_label_distribution(dataset_records):
    records, _ = dataset_records
    label_counts = Counter(r["label"] for r in records)
    assert set(label_counts.keys()) == EXPECTED_LABELS
    assert label_counts["SAFE"] == 1000
    assert label_counts["ATTACK"] == 1000

def test_unique_ids_and_tuples(dataset_records):
    records, _ = dataset_records
    ids = [r["id"] for r in records]
    assert len(ids) == len(set(ids)), "Found duplicate record IDs"
    
    tuples = [(r["scenario_id"], r["language"], r["label"]) for r in records]
    assert len(tuples) == len(set(tuples)), "Found duplicate scenario-language-label pairs"

def test_attack_categories_and_safe_records(dataset_records):
    records, _ = dataset_records
    for r in records:
        if r["label"] == "SAFE":
            assert r["attack_type"] == "none", f"SAFE record {r['id']} has attack_type={r['attack_type']}"
        elif r["label"] == "ATTACK":
            assert r["attack_type"] in EXPECTED_ATTACK_CATEGORIES, f"ATTACK record {r['id']} has invalid attack_type={r['attack_type']}"

    attack_counts = Counter(r["attack_type"] for r in records if r["label"] == "ATTACK")
    assert len(attack_counts) == 10, f"Expected 10 attack categories, found {len(attack_counts)}"
    for cat, count in attack_counts.items():
        assert count == 100, f"Category {cat} has {count} records instead of 100"

def test_no_empty_fields(dataset_records):
    records, _ = dataset_records
    for r in records:
        for col in REQUIRED_COLUMNS:
            val = r.get(col, "")
            assert val is not None and str(val).strip() != "", f"Empty value for column '{col}' in record {r.get('id')}"

def test_split_integrity_and_no_leakage():
    train_file = DATA_DIR / "train.csv"
    val_file = DATA_DIR / "validation.csv"
    test_file = DATA_DIR / "test.csv"
    
    assert train_file.exists() and val_file.exists() and test_file.exists()
    
    with open(train_file, "r", encoding="utf-8") as f:
        train_records = list(csv.DictReader(f))
    with open(val_file, "r", encoding="utf-8") as f:
        val_records = list(csv.DictReader(f))
    with open(test_file, "r", encoding="utf-8") as f:
        test_records = list(csv.DictReader(f))
        
    assert len(train_records) == 1400, f"Expected 1400 train records, found {len(train_records)}"
    assert len(val_records) == 304, f"Expected 304 val records, found {len(val_records)}"
    assert len(test_records) == 296, f"Expected 296 test records, found {len(test_records)}"
    assert len(train_records) + len(val_records) + len(test_records) == 2000
    
    train_scens = set(r["scenario_id"] for r in train_records)
    val_scens = set(r["scenario_id"] for r in val_records)
    test_scens = set(r["scenario_id"] for r in test_records)
    
    assert len(train_scens) == 175, f"Expected 175 train scenarios, found {len(train_scens)}"
    assert len(val_scens) == 38, f"Expected 38 val scenarios, found {len(val_scens)}"
    assert len(test_scens) == 37, f"Expected 37 test scenarios, found {len(test_scens)}"
    
    # Absolute zero scenario leakage
    assert len(train_scens & val_scens) == 0, f"Train and Val overlap: {train_scens & val_scens}"
    assert len(train_scens & test_scens) == 0, f"Train and Test overlap: {train_scens & test_scens}"
    assert len(val_scens & test_scens) == 0, f"Val and Test overlap: {val_scens & test_scens}"

def test_language_master_files():
    masters = {
        "english_master.csv": ("English", 500),
        "hindi_dataset.csv": ("Hindi", 500),
        "telugu_dataset.csv": ("Telugu", 500),
        "telugu_english_dataset.csv": ("Telugu-English", 500),
    }
    for filename, (lang, expected_count) in masters.items():
        filepath = DATA_DIR / filename
        assert filepath.exists(), f"File {filename} missing"
        with open(filepath, "r", encoding="utf-8") as f:
            records = list(csv.DictReader(f))
            assert len(records) == expected_count, f"{filename} has {len(records)} records, expected {expected_count}"
            for r in records:
                assert r["language"] == lang, f"Incorrect language in {filename}: {r['language']}"
