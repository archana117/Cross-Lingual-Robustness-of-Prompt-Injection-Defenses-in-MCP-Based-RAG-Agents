"""
Visualization Module for Cross-Lingual Prompt Injection Defenses.

Generates 7 presentation-quality figures under results/figures/:
1. asr_by_language.png
2. defense_block_rate_by_language.png
3. task_utility_by_language.png
4. asr_comparison_across_defenses.png
5. cross_lingual_defense_comparison.png
6. overall_defense_performance.png
7. safe_vs_attack_classification.png
"""

from pathlib import Path
from typing import Dict, Any, Optional
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import config


def generate_benchmark_figures(
    df_raw: pd.DataFrame,
    df_lang: pd.DataFrame,
    df_defense: pd.DataFrame,
    output_dir: Optional[Path] = None
):
    out_dir = Path(output_dir) if output_dir else (config.RESULTS_DIR / "figures")
    out_dir.mkdir(parents=True, exist_ok=True)

    # Clean matplotlib styling
    plt.rcParams["font.sans-serif"] = "DejaVu Sans"
    plt.rcParams["font.family"] = "sans-serif"
    colors = {
        "No Defense": "#d9534f",
        "Prompt Filter / Perimeter": "#f0ad4e",
        "Meticulous Thought Defender": "#5cb85c",
        "English": "#4285F4",
        "Hindi": "#EA4335",
        "Telugu": "#FBBC05",
        "Telugu-English": "#34A853"
    }

    # 1. ASR by Language (Bar Chart across languages for each defense)
    plt.figure(figsize=(10, 6))
    languages = df_lang["language"].unique()
    defenses = df_lang["defense"].unique()
    x = np.arange(len(languages))
    width = 0.25

    for i, d in enumerate(defenses):
        sub = df_lang[df_lang["defense"] == d]
        asrs = [sub[sub["language"] == l]["asr_percent"].values[0] if len(sub[sub["language"] == l]) > 0 else 0 for l in languages]
        plt.bar(x + (i - 1) * width, asrs, width, label=d, color=colors.get(d, "#333333"), alpha=0.9, edgecolor="black")

    plt.xlabel("Language", fontsize=12, fontweight="bold")
    plt.ylabel("Attack Success Rate (%)", fontsize=12, fontweight="bold")
    plt.title("Figure 1: Attack Success Rate (ASR) by Language", fontsize=14, fontweight="bold", pad=12)
    plt.xticks(x, languages, fontsize=11)
    plt.ylim(0, 105)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.savefig(out_dir / "asr_by_language.png", dpi=300)
    plt.close()

    # 2. Defense Block Rate by Language
    plt.figure(figsize=(10, 6))
    col_block = "defense_block_rate_percent" if "defense_block_rate_percent" in df_lang.columns else "block_rate_percent"
    for i, d in enumerate(defenses):
        sub = df_lang[df_lang["defense"] == d]
        block_rates = [sub[sub["language"] == l][col_block].values[0] if len(sub[sub["language"] == l]) > 0 else 0 for l in languages]
        plt.bar(x + (i - 1) * width, block_rates, width, label=d, color=colors.get(d, "#333333"), alpha=0.9, edgecolor="black")

    plt.xlabel("Language", fontsize=12, fontweight="bold")
    plt.ylabel("Defense Block Rate (%)", fontsize=12, fontweight="bold")
    plt.title("Figure 2: Defense Block Rate by Language", fontsize=14, fontweight="bold", pad=12)
    plt.xticks(x, languages, fontsize=11)
    plt.ylim(0, 105)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.savefig(out_dir / "defense_block_rate_by_language.png", dpi=300)
    plt.close()

    # 3. Task Utility Under Attack by Language
    plt.figure(figsize=(10, 6))
    col_util = "task_utility_under_attack_percent" if "task_utility_under_attack_percent" in df_lang.columns else "task_utility_percent"
    for i, d in enumerate(defenses):
        sub = df_lang[df_lang["defense"] == d]
        utils = [sub[sub["language"] == l][col_util].values[0] if len(sub[sub["language"] == l]) > 0 else 0 for l in languages]
        plt.bar(x + (i - 1) * width, utils, width, label=d, color=colors.get(d, "#333333"), alpha=0.9, edgecolor="black")

    plt.xlabel("Language", fontsize=12, fontweight="bold")
    plt.ylabel("Task Utility Under Attack (%)", fontsize=12, fontweight="bold")
    plt.title("Figure 3: Task Utility Under Attack by Language", fontsize=14, fontweight="bold", pad=12)
    plt.xticks(x, languages, fontsize=11)
    plt.ylim(0, 105)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.savefig(out_dir / "task_utility_by_language.png", dpi=300)
    plt.close()

    # 4. ASR Comparison Across Defenses (Overall Bar)
    plt.figure(figsize=(8, 5))
    defense_names = df_defense["defense"].tolist()
    asr_values = df_defense["asr_percent"].tolist()
    bars = plt.bar(defense_names, asr_values, color=[colors.get(d, "#555") for d in defense_names], edgecolor="black", width=0.55)
    for bar in bars:
        h = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., h + 2, f"{h:.1f}%", ha="center", va="bottom", fontweight="bold")

    plt.ylabel("Overall Attack Success Rate (%)", fontsize=12, fontweight="bold")
    plt.title("Figure 4: ASR Comparison Across Defenses", fontsize=14, fontweight="bold", pad=12)
    plt.ylim(0, 115)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(out_dir / "asr_comparison_across_defenses.png", dpi=300)
    plt.close()

    # 5. Cross-Lingual Defense Comparison (Line Chart)
    plt.figure(figsize=(10, 6))
    for d in defenses:
        sub = df_lang[df_lang["defense"] == d]
        y_vals = [sub[sub["language"] == l]["asr_percent"].values[0] if len(sub[sub["language"] == l]) > 0 else 0 for l in languages]
        plt.plot(languages, y_vals, marker="o", linewidth=2.5, markersize=8, label=d, color=colors.get(d, "#333"))

    plt.xlabel("Language", fontsize=12, fontweight="bold")
    plt.ylabel("Attack Success Rate (%)", fontsize=12, fontweight="bold")
    plt.title("Figure 5: Cross-Lingual Defense Robustness Profile", fontsize=14, fontweight="bold", pad=12)
    plt.ylim(0, 105)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.savefig(out_dir / "cross_lingual_defense_comparison.png", dpi=300)
    plt.close()

    # 6. Overall Defense Performance Radar / Grouped Summary
    plt.figure(figsize=(9, 5.5))
    metrics_names = ["ASR (%)", "Block Rate (%)", "Task Utility (%)"]
    x_m = np.arange(len(metrics_names))
    w_m = 0.25

    for i, d in enumerate(defense_names):
        d_row = df_defense[df_defense["defense"] == d].iloc[0]
        vals = [d_row["asr_percent"], d_row["defense_block_rate_percent"], d_row["task_utility_under_attack_percent"]]
        plt.bar(x_m + (i - 1) * w_m, vals, w_m, label=d, color=colors.get(d, "#333"), edgecolor="black")

    plt.xticks(x_m, metrics_names, fontsize=11, fontweight="bold")
    plt.ylabel("Percentage (%)", fontsize=12, fontweight="bold")
    plt.title("Figure 6: Overall Defense Trade-Off Profile", fontsize=14, fontweight="bold", pad=12)
    plt.ylim(0, 115)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.savefig(out_dir / "overall_defense_performance.png", dpi=300)
    plt.close()

    # 7. Safe vs Attack Classification (Anomaly Score Distribution)
    plt.figure(figsize=(9, 5.5))
    df_mtd = df_raw[df_raw["defense"] == "Meticulous Thought Defender"]
    safe_scores = df_mtd[df_mtd["label"] == "SAFE"]["defense_anomaly_score"]
    attack_scores = df_mtd[df_mtd["label"] == "ATTACK"]["defense_anomaly_score"]

    plt.hist(safe_scores, bins=15, alpha=0.6, label="SAFE Samples", color="#4285F4", edgecolor="black")
    plt.hist(attack_scores, bins=15, alpha=0.6, label="ATTACK Samples", color="#EA4335", edgecolor="black")
    plt.axvline(x=config.ANOMALY_THRESHOLD, color="black", linestyle="--", linewidth=2, label=f"Threshold (tau={config.ANOMALY_THRESHOLD})")

    plt.xlabel("Semantic Anomaly Score", fontsize=12, fontweight="bold")
    plt.ylabel("Sample Count", fontsize=12, fontweight="bold")
    plt.title("Figure 7: Safe vs Attack Anomaly Score Distribution (Thought Defender)", fontsize=14, fontweight="bold", pad=12)
    plt.legend(frameon=True)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(out_dir / "safe_vs_attack_classification.png", dpi=300)
    plt.close()

    print(f"[Visualizer] Successfully generated 7 benchmark figures in {out_dir}")
