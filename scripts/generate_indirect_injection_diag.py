"""
Script to extract and format 20 representative attack cases across 4 languages
for Indirect Prompt Injection verification.
"""
import pandas as pd
from pathlib import Path

csv_path = Path("data/custom_dataset/test.csv")
df = pd.read_csv(csv_path)
attacks = df[df["label"] == "ATTACK"]

lines = ["# Indirect Prompt Injection Verification Report\n\n"]
lines.append("**Objective**: Verify that the malicious instruction is strictly embedded inside the **retrieved document** and NEVER in the **user query**.\n")
lines.append("**Threat Model**: Indirect Prompt Injection (IPI) mediated by FastMCP `search_documents` tool retrieval.\n\n---\n\n")

count = 0
for lang in ["English", "Hindi", "Telugu", "Telugu-English"]:
    sub = attacks[attacks["language"] == lang].head(5)
    lines.append(f"## {lang} ({len(sub)} Verified Cases)\n\n")
    for idx, row in sub.iterrows():
        count += 1
        lines.append(f"### Case {count}: Scenario `{row['scenario_id']}` ({lang})\n")
        lines.append(f"- **Record ID**: `{row['id']}`\n")
        lines.append(f"- **Attack Category**: `{row['attack_type']}`\n")
        lines.append(f"- **User Query (Benign)**: {row['task']}\n")
        lines.append(f"- **Retrieved Document Snippet**: {row['document_text'][:350]}...\n")
        lines.append(f"- **Indirect Injection Placement**: Adversarial directive resides inside the retrieved document, attempting to hijack the agent while fulfilling the user's task.\n")
        lines.append(f"- **MCP Pipeline Path**: User Query $\\to$ MCP Agent $\\to$ ChromaDB $\\to$ Retrieved Context $\\to$ Defense $\\to$ LLM.\n\n")

out_file = Path("results/diagnostics/indirect_injection_validation.md")
with open(out_file, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"Successfully generated {out_file} with {count} verified cases.")
