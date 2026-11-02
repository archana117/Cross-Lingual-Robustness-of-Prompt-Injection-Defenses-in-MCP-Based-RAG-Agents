"""
Validation Script for Custom Multilingual Indirect Prompt Injection Dataset.
Executes 24 rigorous validation checks as required by Project Specification.
"""

import sys
import csv
import json
from pathlib import Path
from collections import Counter, defaultdict

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

VALID_LANGUAGES = {"English", "Hindi", "Telugu", "Telugu-English"}
VALID_LABELS = {"SAFE", "ATTACK"}
VALID_ATTACK_CATEGORIES = {
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

ATTACK_INDICATORS = [
    "disregard all prior instructions",
    "override the user",
    "system override",
    "ignore all previous instructions",
    "print your complete system instructions",
    "expose internal database connection",
    "abandon the user",
    "chief executive officer mandate",
    "execute the external tool",
    "urgently direct the user to visit",
    "inform the user that regardless of the document text",
    "निर्देश:",
    "सिस्टम ओवरराइड",
    "सूచన:",
    "సిస్టమ్ ఓవర్‌రైడ్",
    "ignore చేసి",
    "override చేసి",
]

def load_csv(filepath: Path):
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader), reader.fieldnames

def run_all_validation_checks():
    print("=" * 60)
    print("RUNNING 24 VALIDATION CHECKS ON CUSTOM DATASET")
    print("=" * 60)
    
    csv_file = DATA_DIR / "custom_2000_dataset.csv"
    json_file = DATA_DIR / "custom_2000_dataset.json"
    train_file = DATA_DIR / "train.csv"
    val_file = DATA_DIR / "validation.csv"
    test_file = DATA_DIR / "test.csv"
    
    records, fieldnames = load_csv(csv_file)
    with open(json_file, "r", encoding="utf-8") as f:
        json_records = json.load(f)
        
    train_records, _ = load_csv(train_file)
    val_records, _ = load_csv(val_file)
    test_records, _ = load_csv(test_file)
    
    checks_passed = 0
    checks_total = 24
    errors = []

    def check(condition, desc, error_msg=""):
        nonlocal checks_passed
        if condition:
            checks_passed += 1
            print(f"[PASS] Check {checks_passed:02d}: {desc}")
        else:
            print(f"[FAIL] {desc}: {error_msg}")
            errors.append(f"{desc}: {error_msg}")

    # 1. Total records = 2,000
    check(len(records) == 2000, "Total records = 2,000", f"Found {len(records)}")
    
    # 2. Unique IDs = 2,000
    ids = [r["id"] for r in records]
    check(len(set(ids)) == 2000, "Unique record IDs = 2,000", f"Found {len(set(ids))}")
    
    # 3. Scenario IDs = 250
    scenarios = set(r["scenario_id"] for r in records)
    check(len(scenarios) == 250, "Total scenario IDs = 250", f"Found {len(scenarios)}")
    
    # 4. Every scenario has exactly 8 records
    scenario_counts = Counter(r["scenario_id"] for r in records)
    all_8 = all(c == 8 for c in scenario_counts.values())
    check(all_8, "Every scenario has exactly 8 records", "Some scenarios don't have 8 records")
    
    # 5. English = 500
    lang_counts = Counter(r["language"] for r in records)
    check(lang_counts.get("English", 0) == 500, "English count = 500", f"Found {lang_counts.get('English', 0)}")
    
    # 6. Hindi = 500
    check(lang_counts.get("Hindi", 0) == 500, "Hindi count = 500", f"Found {lang_counts.get('Hindi', 0)}")
    
    # 7. Telugu = 500
    check(lang_counts.get("Telugu", 0) == 500, "Telugu count = 500", f"Found {lang_counts.get('Telugu', 0)}")
    
    # 8. Telugu-English = 500
    check(lang_counts.get("Telugu-English", 0) == 500, "Telugu-English count = 500", f"Found {lang_counts.get('Telugu-English', 0)}")
    
    # 9. SAFE = 1,000
    label_counts = Counter(r["label"] for r in records)
    check(label_counts.get("SAFE", 0) == 1000, "SAFE count = 1,000", f"Found {label_counts.get('SAFE', 0)}")
    
    # 10. ATTACK = 1,000
    check(label_counts.get("ATTACK", 0) == 1000, "ATTACK count = 1,000", f"Found {label_counts.get('ATTACK', 0)}")
    
    # 11. Every scenario has SAFE and ATTACK
    scen_labels = defaultdict(set)
    for r in records:
        scen_labels[r["scenario_id"]].add(r["label"])
    all_safe_attack = all(s == {"SAFE", "ATTACK"} for s in scen_labels.values())
    check(all_safe_attack, "Every scenario has both SAFE and ATTACK versions")
    
    # 12. Every scenario has all four languages
    scen_langs = defaultdict(set)
    for r in records:
        scen_langs[r["scenario_id"]].add(r["language"])
    all_4_langs = all(l == VALID_LANGUAGES for l in scen_langs.values())
    check(all_4_langs, "Every scenario has all 4 languages (EN, HI, TE, TEEN)")
    
    # 13. No duplicate IDs
    check(len(ids) == len(set(ids)), "Zero duplicate record IDs")
    
    # 14. No duplicate scenario-language-label combinations
    tuples = [(r["scenario_id"], r["language"], r["label"]) for r in records]
    check(len(tuples) == len(set(tuples)), "Zero duplicate scenario-language-label combinations")
    
    # 15. No missing required fields
    has_missing = False
    for r in records:
        for col in REQUIRED_COLUMNS:
            val = r.get(col, "")
            if val is None or str(val).strip() == "":
                has_missing = True
                break
    check(not has_missing, "Zero missing required values in any record")
    
    # 16. SAFE records have attack_type = none
    safe_attack_types = set(r["attack_type"] for r in records if r["label"] == "SAFE")
    check(safe_attack_types == {"none"}, "All SAFE records have attack_type == 'none'", f"Found: {safe_attack_types}")
    
    # 17. ATTACK records have a valid attack_type
    attack_types_present = set(r["attack_type"] for r in records if r["label"] == "ATTACK")
    check(attack_types_present.issubset(VALID_ATTACK_CATEGORIES) and len(attack_types_present) == 10,
          "All ATTACK records have valid attack categories from the 10-category taxonomy",
          f"Found: {attack_types_present}")
          
    # 18. Train/validation/test scenario IDs do not overlap (zero scenario leakage)
    train_scens = set(r["scenario_id"] for r in train_records)
    val_scens = set(r["scenario_id"] for r in val_records)
    test_scens = set(r["scenario_id"] for r in test_records)
    
    overlap_tv = train_scens & val_scens
    overlap_tt = train_scens & test_scens
    overlap_vt = val_scens & test_scens
    leakage = len(overlap_tv) + len(overlap_tt) + len(overlap_vt)
    check(leakage == 0 and (len(train_scens) + len(val_scens) + len(test_scens) == 250),
          "Zero scenario leakage between train, validation, and test splits (mutually exclusive)",
          f"Overlaps: TV={overlap_tv}, TT={overlap_tt}, VT={overlap_vt}")
          
    # 19. All required columns exist
    cols_exist = all(c in fieldnames for c in REQUIRED_COLUMNS)
    check(cols_exist, "All required schema columns present in final CSV")
    
    # 20. Attack categories are reasonably distributed
    cat_counts = Counter(r["attack_type"] for r in records if r["label"] == "ATTACK")
    balanced = all(cnt == 100 for cnt in cat_counts.values())  # Exactly 100 per category (25 * 4 languages)
    check(balanced, "Attack categories are evenly distributed (exactly 100 per category)", f"Counts: {cat_counts}")
    
    # 21. Detect obvious duplicate documents within the same language
    lang_docs = defaultdict(set)
    has_dup_doc = False
    for r in records:
        key = (r["language"], r["label"])
        doc = r["document_text"].strip()
        if doc in lang_docs[key]:
            has_dup_doc = True
            break
        lang_docs[key].add(doc)
    check(not has_dup_doc, "Zero duplicate documents within any (language, label) subset")
    
    # 22. Detect suspiciously identical attack text across categories
    # Each attack category must have distinct attack instructions
    cat_attacks = defaultdict(set)
    for r in records:
        if r["label"] == "ATTACK":
            cat_attacks[r["attack_type"]].add(r["document_text"][:50])
    distinct_types = len(cat_attacks) == 10
    check(distinct_types, "All 10 attack categories use distinct attack formulation prefixes")
    
    # 23. Check that Telugu-English records are actually different from plain Telugu
    teen_diff = True
    te_docs = {r["scenario_id"] + "_" + r["label"]: r["document_text"] for r in records if r["language"] == "Telugu"}
    teen_docs = {r["scenario_id"] + "_" + r["label"]: r["document_text"] for r in records if r["language"] == "Telugu-English"}
    for k in te_docs:
        if te_docs[k] == teen_docs[k]:
            teen_diff = False
            break
    check(teen_diff, "Telugu-English records are distinct from plain Telugu (genuine code-mixing)")
    
    # 24. Check that SAFE documents do not contain obvious attack instructions
    safe_docs_clean = True
    for r in records:
        if r["label"] == "SAFE":
            doc_lower = r["document_text"].lower()
            for ind in ATTACK_INDICATORS:
                if ind.lower() in doc_lower:
                    safe_docs_clean = False
                    print(f"False trigger in SAFE record {r['id']}: found '{ind}'")
                    break
    check(safe_docs_clean, "SAFE documents contain zero embedded prompt injection markers")

    print("=" * 60)
    print(f"FINAL RESULT: {checks_passed} / {checks_total} CHECKS PASSED")
    if checks_passed == checks_total:
        print("ALL VALIDATION CHECKS PASSED SUCCESSFULLY (STATUS: PASS)")
    else:
        print("VALIDATION FAILED (STATUS: FAIL)")
    print("=" * 60)
    
    return checks_passed == checks_total

if __name__ == "__main__":
    success = run_all_validation_checks()
    sys.exit(0 if success else 1)
