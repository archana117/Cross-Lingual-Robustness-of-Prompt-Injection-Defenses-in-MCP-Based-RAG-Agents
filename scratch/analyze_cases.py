import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
import json
from src.evaluation.benchmark_runner import MultilingualBenchmarkRunner
from src.evaluation.task_utility import TaskEvaluator, ATTACK_SIGNATURES

test_file = Path("data/custom_dataset/test.csv")
df = pd.read_csv(test_file)

runner = MultilingualBenchmarkRunner(data_file=test_file)
evaluator = TaskEvaluator()

# Select 8 attack records per language (8 * 4 = 32 records)
sample_attacks = []
for lang in ["English", "Hindi", "Telugu", "Telugu-English"]:
    sub = df[(df["language"] == lang) & (df["label"] == "ATTACK")].head(8)
    sample_attacks.append(sub)

df_samples = pd.concat(sample_attacks, ignore_index=True)

inspected_cases = []

for idx, rec in df_samples.iterrows():
    task = rec["task"]
    doc_text = rec["document_text"]
    lang = rec["language"]
    attack_type = rec["attack_type"]
    scen_id = rec["scenario_id"]
    rec_id = rec["id"]
    
    # Trace through runner for each defense
    case_info = {
        "id": rec_id,
        "scenario_id": scen_id,
        "language": lang,
        "attack_type": attack_type,
        "task": task,
        "document_text_snippet": doc_text[:150],
        "defenses": {}
    }
    
    for d_name, d_obj in runner.defenses.items():
        res = runner.run_single_evaluation(rec, d_name, d_obj)
        case_info["defenses"][d_name] = {
            "is_blocked": res["is_blocked"],
            "response_text": res["response_text"],
            "attack_success": res["attack_success"],
            "task_success": res["task_success"],
            "verdict": res["execution_verdict"]
        }
        
    inspected_cases.append(case_info)

with open("scratch/inspected_32_cases.json", "w", encoding="utf-8") as f:
    json.dump(inspected_cases, f, indent=2, ensure_ascii=False)

print(f"Successfully analyzed {len(inspected_cases)} attack cases across 4 languages.")
