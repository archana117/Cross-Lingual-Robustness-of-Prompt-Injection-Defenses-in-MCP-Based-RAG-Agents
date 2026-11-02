"""
Stage 1 Verification Script:
Runs a small, genuine evaluation test using at least one benign and one attack example
from test.csv across all 3 defenses with live Ollama Qwen2.5:7b.
"""
import sys
import io
from pathlib import Path

# Setup paths and stdout encoding
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import config
from src.llm import LLMProvider
from src.evaluation.benchmark_runner import MultilingualBenchmarkRunner

def main():
    print("=" * 80)
    print("      STAGE 1: GENUINE OLLAMA BENCHMARK EXECUTION VERIFICATION TEST")
    print("=" * 80)

    # 1. Initialize Runner in genuine mode with Ollama
    llm = LLMProvider(provider="ollama", model="qwen2.5:7b")
    runner = MultilingualBenchmarkRunner(mode="genuine", llm_provider=llm)
    dataset = runner.load_dataset()
    print(f"[Dataset] Total records available in test.csv: {len(dataset)}")

    # 2. Pick 1 Benign (SAFE) and 1 Attack (ATTACK) sample
    safe_sample = next((r for r in dataset if r.get("id") == "S209_EN_SAFE"), dataset[0])
    attack_sample = next((r for r in dataset if r.get("id") == "S209_EN_ATTACK"), dataset[1])

    test_samples = [safe_sample, attack_sample]
    defenses = ["No Defense", "Prompt Filter / Perimeter", "Meticulous Thought Defender"]

    for s_idx, sample in enumerate(test_samples, start=1):
        sample_id = sample.get("id")
        label = sample.get("label")
        lang = sample.get("language")
        task = sample.get("task")
        doc_text = sample.get("document_text")
        attack_type = sample.get("attack_type")

        print("\n" + "#" * 80)
        print(f"SAMPLE {s_idx}/2: ID={sample_id} | LABEL={label} | LANG={lang} | ATTACK_TYPE={attack_type}")
        print("#" * 80)
        print(f"[User Query]:\n{task}\n")
        print(f"[Document Text Injected Into Context]:\n{doc_text[:300]}...\n")

        for defense_name in defenses:
            print("-" * 80)
            print(f"--> EVALUATING DEFENSE: [{defense_name}]")
            defense_obj = runner.defenses[defense_name]

            # Run genuine evaluation
            res = runner.run_single_evaluation(sample, defense_name=defense_name, defense_obj=defense_obj)

            print(f"  Defense Action:     {'BLOCKED' if res['is_blocked'] else 'ALLOWED'}")
            print(f"  Anomaly Score:      {res['defense_anomaly_score']}")
            print(f"  Execution Verdict:  {res['execution_verdict']}")
            print(f"  Attack Success:     {res['attack_success']}")
            print(f"  Task Success:       {res['task_success']}")
            print(f"  Response Generated (Preview):")
            print(f"  \"{res['response_text']}\"")
            print("-" * 80)

    print("\n" + "=" * 80)
    print("STAGE 1 TEST COMPLETE: Genuine Ollama Qwen2.5:7b execution verified.")
    print("=" * 80)

if __name__ == "__main__":
    main()
