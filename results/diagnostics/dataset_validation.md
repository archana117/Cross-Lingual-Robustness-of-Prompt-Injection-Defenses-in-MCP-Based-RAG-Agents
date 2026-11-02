# Dataset Validation Audit Report

**Target Dataset**: Multilingual Enterprise RAG Prompt Injection Benchmark  
**Dataset Directory**: `data/custom_dataset/`  
**Audit Date**: 2026-10-07  
**Validation Script**: [`scripts/validate_custom_dataset.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/scripts/validate_custom_dataset.py)  

---

## 1. Summary of Dataset Validation Checks

All **24 / 24** formal integrity and leakage prevention checks passed successfully.

| Check # | Verification Dimension | Expected Value | Observed Value | Status |
| :---: | :--- | :---: | :---: | :---: |
| 1 | Total Records | 2,000 | 2,000 | **PASS** |
| 2 | Unique Record IDs | 2,000 | 2,000 | **PASS** |
| 3 | Total Enterprise Scenarios | 250 | 250 | **PASS** |
| 4 | Records per Scenario | Exactly 8 | Exactly 8 | **PASS** |
| 5 | English Record Count | 500 | 500 | **PASS** |
| 6 | Hindi Record Count | 500 | 500 | **PASS** |
| 7 | Telugu Record Count | 500 | 500 | **PASS** |
| 8 | Telugu-English Record Count | 500 | 500 | **PASS** |
| 9 | SAFE Sample Count | 1,000 | 1,000 | **PASS** |
| 10 | ATTACK Sample Count | 1,000 | 1,000 | **PASS** |
| 11 | SAFE / ATTACK Pairing | 100% paired per scenario | 100% paired | **PASS** |
| 12 | 4-Language Representation | 100% scenarios in 4 langs | 100% scenarios | **PASS** |
| 13 | Record ID Uniqueness | Zero duplicates | Zero duplicates | **PASS** |
| 14 | Tuple Uniqueness `(scenario, lang, label)` | Unique | Unique | **PASS** |
| 15 | Null / Missing Value Check | Zero nulls in core fields | Zero nulls | **PASS** |
| 16 | SAFE Attack Label Integrity | `attack_type == 'none'` | 1,000 / 1,000 | **PASS** |
| 17 | ATTACK Taxonomy Integrity | Valid 10 categories | 1,000 / 1,000 | **PASS** |
| 18 | **Scenario Leakage Across Splits** | **Zero leakage** | **0 scenarios shared** | **PASS** |
| 19 | Schema Column Conformance | All 10 schema fields | Conforming | **PASS** |
| 20 | Attack Category Balance | 100 records / category | 100 records each | **PASS** |
| 21 | Document Text Uniqueness | Zero duplicates per subset | Distinct | **PASS** |
| 22 | Injection Prefix Variety | Distinct formulation prefixes | Distinct | **PASS** |
| 23 | Code-Mixed Script Separation | Distinct Latin vs Telugu | Verified | **PASS** |
| 24 | Clean Baseline Integrity | Zero injection tokens in SAFE | 0 markers | **PASS** |

---

## 2. Partitioning Strategy & Leakage Verification

Data splits are strictly partitioned at the **`scenario_id`** level. All language versions and safe/attack pairs for any scenario are grouped into the same partition:

- **Train Split (`train.csv`)**: 175 scenarios $\times$ 8 records = **1,400 records** (70.0%)
- **Validation Split (`validation.csv`)**: 38 scenarios $\times$ 8 records = **304 records** (15.2%)
- **Held-Out Test Split (`test.csv`)**: 37 scenarios $\times$ 8 records = **296 records** (14.8%)

$$\text{Leakage}(\text{Train} \cap \text{Val}) = \emptyset, \quad \text{Leakage}(\text{Train} \cap \text{Test}) = \emptyset, \quad \text{Leakage}(\text{Val} \cap \text{Test}) = \emptyset$$

Zero scenario overlap exists across any data splits.

---

## 3. Conclusion

The dataset is fully valid, structurally intact, balanced across all four target languages, and free from cross-split leakage. No dataset regeneration is required.
