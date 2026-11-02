"""
Master Final Benchmark Runner for Weeks 4-8.

Executes the complete experimental matrix:
- 4 Languages: English, Hindi, Telugu, Telugu-English Code-Mixed
- 3 Defense Conditions:
    1. No Defense (Baseline)
    2. Prompt Filter / Perimeter
    3. Meticulous Thought Defender (Semantic CoT)
- Dataset: Held-Out Test Set (data/custom_dataset/test.csv, 296 records)
- Metrics: ASR, Defense Block Rate, Task Utility Under Attack, Benign Task Utility, FPR, FNR.
- Exports all raw, summary, and comparison CSV tables.
- Generates 7 presentation-quality figures under results/figures/.

Usage:
  python scripts/run_final_benchmark.py
"""

import sys
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import config
from src.evaluation.benchmark_runner import MultilingualBenchmarkRunner
from src.evaluation.visualizer import generate_benchmark_figures


def main():
    print("==========================================================================")
    print("RUNNING FINAL MULTILINGUAL PROMPT INJECTION BENCHMARK (WEEKS 4-8)")
    print("==========================================================================")
    test_csv = config.DATA_DIR / "custom_dataset" / "test.csv"
    print(f"Target Dataset: {test_csv}")

    runner = MultilingualBenchmarkRunner(data_file=test_csv)
    results = runner.run_full_benchmark()

    # Load raw and summary DataFrames for figure generation
    raw_path = Path(results["raw_path"])
    df_raw = pd.read_csv(raw_path)
    df_lang = results["summaries"]["language_summary"]
    df_defense = results["summaries"]["defense_summary"]

    print("\n[Figures] Generating 7 presentation-quality figures...")
    generate_benchmark_figures(df_raw, df_lang, df_defense)

    print("\n==========================================================================")
    print("FINAL BENCHMARK COMPARISON TABLE (ACROSS DEFENSES)")
    print("==========================================================================")
    print(df_defense.to_string(index=False))

    print("\n==========================================================================")
    print("LANGUAGE COMPARISON TABLE (CROSS-LINGUAL PERFORMANCE)")
    print("==========================================================================")
    print(df_lang.to_string(index=False))
    print("==========================================================================")
    print("FINAL BENCHMARK EXECUTION COMPLETE.")


if __name__ == "__main__":
    main()
