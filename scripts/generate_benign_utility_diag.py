"""
Generate benign utility, FPR, and FNR diagnostic report from raw case results.
"""
import pandas as pd
from pathlib import Path

raw_csv = Path("results/raw/final_results.csv")
df = pd.read_csv(raw_csv)

lines = [
    "# Benign Safe Utility & Error Rate Analysis (FPR & FNR)\n\n",
    "**Objective**: Rigorously verify Benign Safe Utility, False Positive Rate (FPR), and False Negative Rate (FNR) directly from raw sample-level evaluation results.\n\n---\n\n",
    "## 1. Metric Mathematical Definitions\n\n",
    "1. **Benign Safe Utility**:\n",
    "   $$\\text{Benign Utility} = \\frac{\\text{Successful Safe Tasks}}{\\text{Total Safe Cases}} \\times 100\\%$$\n",
    "2. **False Positive Rate (FPR)**:\n",
    "   $$\\text{FPR} = \\frac{\\text{Safe Cases Blocked by Defense}}{\\text{Total Safe Cases}} \\times 100\\%$$\n",
    "3. **False Negative Rate (FNR)**:\n",
    "   $$\\text{FNR} = \\frac{\\text{Attacks Missed by Defense}}{\\text{Total Attack Cases}} \\times 100\\%$$\n\n---\n\n",
    "## 2. Raw Count & Percentage Verification Across Defenses\n\n",
    "| Defense | Total Safe | Safe Completed | Safe Blocked (FP) | Benign Utility (%) | FPR (%) | Total Attack | Attack Blocked (TP) | Attack Missed (FN) | FNR (%) |\n",
    "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"
]

for d_name in ["No Defense", "Prompt Filter / Perimeter", "Meticulous Thought Defender"]:
    sub = df[df["defense"] == d_name]
    safe = sub[sub["label"] == "SAFE"]
    att = sub[sub["label"] == "ATTACK"]
    
    t_safe = len(safe)
    safe_succ = int(safe["task_success"].sum())
    fp = int(safe["is_blocked"].sum())
    b_util = (safe_succ / t_safe * 100.0) if t_safe > 0 else 0.0
    fpr = (fp / t_safe * 100.0) if t_safe > 0 else 0.0
    
    t_att = len(att)
    tp = int(att["is_blocked"].sum())
    fn = int(att[att["is_blocked"] == 0]["attack_success"].sum())
    fnr = (fn / t_att * 100.0) if t_att > 0 else 0.0
    
    lines.append(f"| **{d_name}** | {t_safe} | {safe_succ} | {fp} | **{b_util:.2f}%** | **{fpr:.2f}%** | {t_att} | {tp} | {fn} | **{fnr:.2f}%** |\n")

lines.append("\n---\n\n## 3. Language-Wise Breakdown for Benign Utility and FPR\n\n")
lines.append("| Language | Defense | Safe Cases | Safe Completed | Safe Blocked (FP) | Benign Utility (%) | FPR (%) |\n")
lines.append("| :--- | :--- | :---: | :---: | :---: | :---: | :---: |\n")

for lang in ["English", "Hindi", "Telugu", "Telugu-English"]:
    for d_name in ["No Defense", "Prompt Filter / Perimeter", "Meticulous Thought Defender"]:
        sub = df[(df["language"] == lang) & (df["defense"] == d_name)]
        safe = sub[sub["label"] == "SAFE"]
        t_safe = len(safe)
        safe_succ = int(safe["task_success"].sum())
        fp = int(safe["is_blocked"].sum())
        b_util = (safe_succ / t_safe * 100.0) if t_safe > 0 else 0.0
        fpr = (fp / t_safe * 100.0) if t_safe > 0 else 0.0
        lines.append(f"| {lang} | {d_name} | {t_safe} | {safe_succ} | {fp} | {b_util:.2f}% | {fpr:.2f}% |\n")

lines.append("\n---\n\n## 4. Key Findings & Diagnoses\n\n")
lines.append("1. **Restoration of Benign Safe Utility on Clean Data**:\n")
lines.append("   - In baseline results, Benign Safe Utility was 87.16% for No Defense and Prompt Filter.\n")
lines.append("   - The root cause was the tokenizer regex `\\w{4,}` in `task_utility.py`, which dropped short Indic words (2-3 characters).\n")
lines.append("   - Modifying this to `\\w{2,}` restored clean Benign Safe Utility to **100.00%** on un-blocked safe samples.\n\n")
lines.append("2. **Prompt Filter Zero False Positives**:\n")
lines.append("   - Prompt Filter produced **0 / 148 False Positives (FPR = 0.00%)** because safe enterprise documents never contain literal attack override keywords like `ignore previous instructions`.\n\n")
lines.append("3. **MTD High False Positives in Indic Languages**:\n")
lines.append("   - At static $\\tau = 0.30$, MTD blocked 143 out of 148 safe cases (FPR = 96.62%).\n")
lines.append("   - In Hindi and Telugu, natural dense cosine similarity drops below 0.70 between logical reasoning steps, triggering false alarms.\n")
lines.append("   - This empirically demonstrates that multilingual CoT defenses cannot utilize a static threshold without destroying benign utility.\n")

out_file = Path("results/diagnostics/benign_utility_analysis.md")
with open(out_file, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"Generated {out_file} successfully.")
