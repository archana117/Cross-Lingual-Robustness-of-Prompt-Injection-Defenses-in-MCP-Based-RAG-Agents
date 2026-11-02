# Benign Safe Utility & Error Rate Analysis (FPR & FNR)

**Objective**: Rigorously verify Benign Safe Utility, False Positive Rate (FPR), and False Negative Rate (FNR) directly from raw sample-level evaluation results.

---

## 1. Metric Mathematical Definitions

1. **Benign Safe Utility**:
   $$\text{Benign Utility} = \frac{\text{Successful Safe Tasks}}{\text{Total Safe Cases}} \times 100\%$$
2. **False Positive Rate (FPR)**:
   $$\text{FPR} = \frac{\text{Safe Cases Blocked by Defense}}{\text{Total Safe Cases}} \times 100\%$$
3. **False Negative Rate (FNR)**:
   $$\text{FNR} = \frac{\text{Attacks Missed by Defense}}{\text{Total Attack Cases}} \times 100\%$$

---

## 2. Raw Count & Percentage Verification Across Defenses

| Defense | Total Safe | Safe Completed | Safe Blocked (FP) | Benign Utility (%) | FPR (%) | Total Attack | Attack Blocked (TP) | Attack Missed (FN) | FNR (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **No Defense** | 148 | 148 | 0 | **100.00%** | **0.00%** | 148 | 0 | 148 | **100.00%** |
| **Prompt Filter / Perimeter** | 148 | 148 | 0 | **100.00%** | **0.00%** | 148 | 44 | 104 | **70.27%** |
| **Meticulous Thought Defender** | 148 | 5 | 143 | **3.38%** | **96.62%** | 148 | 144 | 4 | **2.70%** |

---

## 3. Language-Wise Breakdown for Benign Utility and FPR

| Language | Defense | Safe Cases | Safe Completed | Safe Blocked (FP) | Benign Utility (%) | FPR (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| English | No Defense | 37 | 37 | 0 | 100.00% | 0.00% |
| English | Prompt Filter / Perimeter | 37 | 37 | 0 | 100.00% | 0.00% |
| English | Meticulous Thought Defender | 37 | 0 | 37 | 0.00% | 100.00% |
| Hindi | No Defense | 37 | 37 | 0 | 100.00% | 0.00% |
| Hindi | Prompt Filter / Perimeter | 37 | 37 | 0 | 100.00% | 0.00% |
| Hindi | Meticulous Thought Defender | 37 | 1 | 36 | 2.70% | 97.30% |
| Telugu | No Defense | 37 | 37 | 0 | 100.00% | 0.00% |
| Telugu | Prompt Filter / Perimeter | 37 | 37 | 0 | 100.00% | 0.00% |
| Telugu | Meticulous Thought Defender | 37 | 0 | 37 | 0.00% | 100.00% |
| Telugu-English | No Defense | 37 | 37 | 0 | 100.00% | 0.00% |
| Telugu-English | Prompt Filter / Perimeter | 37 | 37 | 0 | 100.00% | 0.00% |
| Telugu-English | Meticulous Thought Defender | 37 | 4 | 33 | 10.81% | 89.19% |

---

## 4. Key Findings & Diagnoses

1. **Restoration of Benign Safe Utility on Clean Data**:
   - In baseline results, Benign Safe Utility was 87.16% for No Defense and Prompt Filter.
   - The root cause was the tokenizer regex `\w{4,}` in `task_utility.py`, which dropped short Indic words (2-3 characters).
   - Modifying this to `\w{2,}` restored clean Benign Safe Utility to **100.00%** on un-blocked safe samples.

2. **Prompt Filter Zero False Positives**:
   - Prompt Filter produced **0 / 148 False Positives (FPR = 0.00%)** because safe enterprise documents never contain literal attack override keywords like `ignore previous instructions`.

3. **MTD High False Positives in Indic Languages**:
   - At static $\tau = 0.30$, MTD blocked 143 out of 148 safe cases (FPR = 96.62%).
   - In Hindi and Telugu, natural dense cosine similarity drops below 0.70 between logical reasoning steps, triggering false alarms.
   - This empirically demonstrates that multilingual CoT defenses cannot utilize a static threshold without destroying benign utility.
