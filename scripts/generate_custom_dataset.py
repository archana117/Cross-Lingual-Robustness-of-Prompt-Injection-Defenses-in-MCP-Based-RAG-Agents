"""
Script to Generate the 2,000-Record Custom Multilingual Indirect Prompt Injection Dataset.

Specifications:
- 250 distinct scenarios across 25 domains (10 per domain)
- 4 languages: English, Hindi, Telugu, Telugu-English
- 2 labels per scenario per language: SAFE, ATTACK
- 250 * 4 * 2 = 2,000 records
- Attack categories: 10 formal categories, exactly 25 scenarios (100 attack records) per category
- Attack injection embedded INSIDE the retrieved document (indirect prompt injection)
- Scenario-based split: Train (175 scenarios, 1,400 records), Val (38 scenarios, 304 records), Test (37 scenarios, 296 records)
"""

import os
import sys
import json
import csv
from pathlib import Path
from typing import List, Dict, Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.domain_builder_1 import BUILDER1_DOMAINS
from scripts.domain_builder_2 import BUILDER2_DOMAINS
from scripts.domain_builder_3 import BUILDER3_DOMAINS
from scripts.domain_builder_4 import BUILDER4_DOMAINS
from scripts.domain_builder_5 import BUILDER5_DOMAINS
from scripts.attack_templates import ATTACK_CATEGORIES, ATTACK_TEMPLATES, embed_injection

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "custom_dataset"
DATA_DIR.mkdir(parents=True, exist_ok=True)

SCHEMA_COLUMNS = [
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

def collect_all_scenarios():
    all_domains = (
        BUILDER1_DOMAINS +
        BUILDER2_DOMAINS +
        BUILDER3_DOMAINS +
        BUILDER4_DOMAINS +
        BUILDER5_DOMAINS
    )
    
    flat_scenarios = []
    scenario_idx = 1
    for domain_obj in all_domains:
        domain_name = domain_obj["domain"]
        for s in domain_obj["scenarios"]:
            s_id = f"S{scenario_idx:03d}"
            # Deterministic attack category assignment (10 categories, 25 scenarios each)
            cat_idx = (scenario_idx - 1) % len(ATTACK_CATEGORIES)
            attack_cat = ATTACK_CATEGORIES[cat_idx]
            # Varied template pattern index (0..4) and placement index (0..3)
            template_idx = ((scenario_idx - 1) // len(ATTACK_CATEGORIES)) % 5
            placement_idx = (scenario_idx - 1) % 4
            
            flat_scenarios.append({
                "scenario_id": s_id,
                "domain": domain_name,
                "topic": s["topic"],
                "attack_type": attack_cat,
                "template_idx": template_idx,
                "placement_idx": placement_idx,
                "task_en": s["task_en"],
                "task_hi": s["task_hi"],
                "task_te": s["task_te"],
                "task_teen": s["task_teen"],
                "doc_en": s["doc_en"],
                "doc_hi": s["doc_hi"],
                "doc_te": s["doc_te"],
                "doc_teen": s["doc_teen"],
            })
            scenario_idx += 1
            
    return flat_scenarios

def generate_records(scenarios):
    all_records = []
    
    for s in scenarios:
        s_id = s["scenario_id"]
        attack_type = s["attack_type"]
        t_idx = s["template_idx"]
        p_idx = s["placement_idx"]
        
        # Injections per language
        inj_en = ATTACK_TEMPLATES[attack_type]["en"][t_idx]
        inj_hi = ATTACK_TEMPLATES[attack_type]["hi"][t_idx]
        inj_te = ATTACK_TEMPLATES[attack_type]["te"][t_idx]
        inj_teen = ATTACK_TEMPLATES[attack_type]["teen"][t_idx]
        
        # 1. English Pair
        # SAFE
        all_records.append({
            "id": f"{s_id}_EN_SAFE",
            "scenario_id": s_id,
            "language": "English",
            "task": s["task_en"],
            "document_text": s["doc_en"],
            "attack_type": "none",
            "label": "SAFE",
            "source": "custom_synthetic",
            "translation_method": "original",
            "code_mix_type": "none",
            "validation_status": "needs_manual_validation",
        })
        # ATTACK
        attack_doc_en = embed_injection(s["doc_en"], inj_en, p_idx)
        all_records.append({
            "id": f"{s_id}_EN_ATTACK",
            "scenario_id": s_id,
            "language": "English",
            "task": s["task_en"],
            "document_text": attack_doc_en,
            "attack_type": attack_type,
            "label": "ATTACK",
            "source": "custom_synthetic",
            "translation_method": "original",
            "code_mix_type": "none",
            "validation_status": "needs_manual_validation",
        })
        
        # 2. Hindi Pair
        # SAFE
        all_records.append({
            "id": f"{s_id}_HI_SAFE",
            "scenario_id": s_id,
            "language": "Hindi",
            "task": s["task_hi"],
            "document_text": s["doc_hi"],
            "attack_type": "none",
            "label": "SAFE",
            "source": "custom_synthetic",
            "translation_method": "custom_multilingual_engine",
            "code_mix_type": "none",
            "validation_status": "needs_manual_validation",
        })
        # ATTACK
        attack_doc_hi = embed_injection(s["doc_hi"], inj_hi, p_idx)
        all_records.append({
            "id": f"{s_id}_HI_ATTACK",
            "scenario_id": s_id,
            "language": "Hindi",
            "task": s["task_hi"],
            "document_text": attack_doc_hi,
            "attack_type": attack_type,
            "label": "ATTACK",
            "source": "custom_synthetic",
            "translation_method": "custom_multilingual_engine",
            "code_mix_type": "none",
            "validation_status": "needs_manual_validation",
        })
        
        # 3. Telugu Pair
        # SAFE
        all_records.append({
            "id": f"{s_id}_TE_SAFE",
            "scenario_id": s_id,
            "language": "Telugu",
            "task": s["task_te"],
            "document_text": s["doc_te"],
            "attack_type": "none",
            "label": "SAFE",
            "source": "custom_synthetic",
            "translation_method": "custom_multilingual_engine",
            "code_mix_type": "none",
            "validation_status": "needs_manual_validation",
        })
        # ATTACK
        attack_doc_te = embed_injection(s["doc_te"], inj_te, p_idx)
        all_records.append({
            "id": f"{s_id}_TE_ATTACK",
            "scenario_id": s_id,
            "language": "Telugu",
            "task": s["task_te"],
            "document_text": attack_doc_te,
            "attack_type": attack_type,
            "label": "ATTACK",
            "source": "custom_synthetic",
            "translation_method": "custom_multilingual_engine",
            "code_mix_type": "none",
            "validation_status": "needs_manual_validation",
        })
        
        # 4. Telugu-English Code-Mixed Pair
        # SAFE
        all_records.append({
            "id": f"{s_id}_TEEN_SAFE",
            "scenario_id": s_id,
            "language": "Telugu-English",
            "task": s["task_teen"],
            "document_text": s["doc_teen"],
            "attack_type": "none",
            "label": "SAFE",
            "source": "custom_synthetic",
            "translation_method": "natural_code_mix",
            "code_mix_type": "natural lexical/code-mixed",
            "validation_status": "needs_manual_validation",
        })
        # ATTACK
        attack_doc_teen = embed_injection(s["doc_teen"], inj_teen, p_idx)
        all_records.append({
            "id": f"{s_id}_TEEN_ATTACK",
            "scenario_id": s_id,
            "language": "Telugu-English",
            "task": s["task_teen"],
            "document_text": attack_doc_teen,
            "attack_type": attack_type,
            "label": "ATTACK",
            "source": "custom_synthetic",
            "translation_method": "natural_code_mix",
            "code_mix_type": "natural lexical/code-mixed",
            "validation_status": "needs_manual_validation",
        })
        
    return all_records

def write_csv(filepath: Path, records: List[Dict[str, Any]], fieldnames: List[str]):
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

def create_scenario_splits(scenarios):
    """
    Splits 250 scenarios deterministically into:
    - Train: 175 scenarios (70.0%) -> 1,400 records
    - Validation: 38 scenarios (15.2%) -> 304 records
    - Test: 37 scenarios (14.8%) -> 296 records
    Stratified across all 10 attack categories.
    """
    by_category = {cat: [] for cat in ATTACK_CATEGORIES}
    for s in scenarios:
        by_category[s["attack_type"]].append(s["scenario_id"])
        
    train_ids = set()
    val_ids = set()
    test_ids = set()
    
    for i, cat in enumerate(ATTACK_CATEGORIES):
        s_ids = by_category[cat]  # Exactly 25 scenarios
        # 175 train total: first 5 categories get 18, next 5 get 17 (5*18 + 5*17 = 175)
        n_train = 18 if i < 5 else 17
        # 38 val total: categories 0..7 get 4, categories 8..9 get 3 (8*4 + 2*3 = 38)
        n_val = 4 if i < 8 else 3
        
        train_slice = s_ids[:n_train]
        val_slice = s_ids[n_train:n_train + n_val]
        test_slice = s_ids[n_train + n_val:]
        
        train_ids.update(train_slice)
        val_ids.update(val_slice)
        test_ids.update(test_slice)
        
    return train_ids, val_ids, test_ids

def main():
    print("[1/6] Collecting 250 scenarios across 25 domains...")
    scenarios = collect_all_scenarios()
    print(f"      Loaded {len(scenarios)} scenarios.")
    
    print("[2/6] Generating 2,000 paired safe/attack records...")
    records = generate_records(scenarios)
    print(f"      Generated {len(records)} records.")
    
    print("[3/6] Exporting language-specific master files...")
    en_records = [r for r in records if r["language"] == "English"]
    hi_records = [r for r in records if r["language"] == "Hindi"]
    te_records = [r for r in records if r["language"] == "Telugu"]
    teen_records = [r for r in records if r["language"] == "Telugu-English"]
    
    write_csv(DATA_DIR / "english_master.csv", en_records, SCHEMA_COLUMNS)
    write_csv(DATA_DIR / "hindi_dataset.csv", hi_records, SCHEMA_COLUMNS)
    write_csv(DATA_DIR / "telugu_dataset.csv", te_records, SCHEMA_COLUMNS)
    write_csv(DATA_DIR / "telugu_english_dataset.csv", teen_records, SCHEMA_COLUMNS)
    print("      Exported english_master.csv (500 records)")
    print("      Exported hindi_dataset.csv (500 records)")
    print("      Exported telugu_dataset.csv (500 records)")
    print("      Exported telugu_english_dataset.csv (500 records)")
    
    print("[4/6] Exporting complete dataset CSV and JSON...")
    write_csv(DATA_DIR / "custom_2000_dataset.csv", records, SCHEMA_COLUMNS)
    with open(DATA_DIR / "custom_2000_dataset.json", "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
    print("      Exported custom_2000_dataset.csv (2,000 records)")
    print("      Exported custom_2000_dataset.json (2,000 records)")
    
    print("[5/6] Partitioning train, validation, and test splits by scenario_id...")
    train_ids, val_ids, test_ids = create_scenario_splits(scenarios)
    train_records = [r for r in records if r["scenario_id"] in train_ids]
    val_records = [r for r in records if r["scenario_id"] in val_ids]
    test_records = [r for r in records if r["scenario_id"] in test_ids]
    
    write_csv(DATA_DIR / "train.csv", train_records, SCHEMA_COLUMNS)
    write_csv(DATA_DIR / "validation.csv", val_records, SCHEMA_COLUMNS)
    write_csv(DATA_DIR / "test.csv", test_records, SCHEMA_COLUMNS)
    print(f"      Train split: {len(train_ids)} scenarios, {len(train_records)} records")
    print(f"      Val split:   {len(val_ids)} scenarios, {len(val_records)} records")
    print(f"      Test split:  {len(test_ids)} scenarios, {len(test_records)} records")
    
    print("[6/6] Generating manual validation review file...")
    validation_rows = []
    for r in records:
        validation_rows.append({
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
    val_cols = [
        "scenario_id", "language", "task_ok", "translation_ok",
        "attack_intent_preserved", "document_relevant", "label_correct",
        "code_mix_natural", "reviewer_notes"
    ]
    write_csv(DATA_DIR / "manual_validation.csv", validation_rows, val_cols)
    print("      Exported manual_validation.csv (2,000 review rows)")
    print("\nDataset generation complete!")

if __name__ == "__main__":
    main()
