"""
InjecAgent Benchmark Runner Script.

Executes cross-lingual prompt injection evaluation across:
Languages: English, Hindi, Telugu, Code-Mixed
Defenses: NoDefense (Baseline), PromptFilter (Perimeter), ThoughtDefender (Semantic CoT)
Metrics: Attack Success Rate (ASR) & Task Utility Under Attack

Usage:
  python scripts/run_injecagent_benchmark.py --language english --defense none --max-cases 20
  python scripts/run_injecagent_benchmark.py --language all --defense thought_defender --max-cases 10
"""

import sys
import argparse
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import config
from src.defenses import NoDefense, PromptFilterDefense, ThoughtDefenderDefense
from src.evaluation import InjecAgentEvaluator


def main():
    parser = argparse.ArgumentParser(description="Run Cross-Lingual Prompt Injection Benchmark")
    parser.add_argument("--language", type=str, default="english", choices=["english", "hindi", "telugu", "code_mixed", "all"], help="Language to evaluate")
    parser.add_argument("--defense", type=str, default="all", choices=["none", "prompt_filter", "thought_defender", "all"], help="Defense to evaluate")
    parser.add_argument("--max-cases", type=int, default=20, help="Max test cases per language (0 for full 2,108 cases)")
    parser.add_argument("--save-results", action="store_true", default=True, help="Save CSV results under results/")

    args = parser.parse_args()

    max_c = args.max_cases if args.max_cases > 0 else None
    languages = ["english", "hindi", "telugu", "code_mixed"] if args.language == "all" else [args.language]

    defenses_map = {
        "none": NoDefense(),
        "prompt_filter": PromptFilterDefense(),
        "thought_defender": ThoughtDefenderDefense()
    }

    active_defenses = list(defenses_map.values()) if args.defense == "all" else [defenses_map[args.defense]]

    print("==========================================================================")
    print("CROSS-LINGUAL PROMPT INJECTION BENCHMARK EVALUATION")
    print(f"Languages: {languages}")
    print(f"Defenses: {[d.name for d in active_defenses]}")
    print(f"Cases per run: {max_c if max_c else 'FULL (2108)'}")
    print("==========================================================================")

    summary_records = []

    for def_obj in active_defenses:
        evaluator = InjecAgentEvaluator(defense=def_obj)
        for lang in languages:
            res = evaluator.run_benchmark(language=lang, max_cases=max_c, save_results=args.save_results)
            m = res["metrics"]
            summary_records.append({
                "Defense": def_obj.name,
                "Language": lang.capitalize(),
                "Total Cases": m["total_cases"],
                "ASR (%)": f"{m['attack_success_rate'] * 100:.1f}%",
                "Task Utility (%)": f"{m['task_utility_under_attack'] * 100:.1f}%",
                "Defense Block Rate (%)": f"{m['defense_block_rate'] * 100:.1f}%",
                "Results File": res["results_file"]
            })

    print("\n==========================================================================")
    print("SUMMARY OF BENCHMARK RESULTS")
    print("==========================================================================")
    import pandas as pd
    df_sum = pd.DataFrame(summary_records)
    print(df_sum.to_string(index=False))
    print("==========================================================================")

if __name__ == "__main__":
    main()
