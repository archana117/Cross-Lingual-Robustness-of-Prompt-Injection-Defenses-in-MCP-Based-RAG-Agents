"""
Stage 3: Genuine Full Multilingual Benchmark Runner.

Executes all 296 test records from test.csv across all 3 defenses:
1. No Defense (Baseline)
2. Prompt Filter / Perimeter
3. Meticulous Thought Defender (Semantic CoT)

Total Evaluation Conditions: 888 (296 x 3).
Saves results under results/genuine/ without overwriting existing mock results.
Supports robust checkpoint resume, per-evaluation latency tracking, and error retries.
"""
import sys
import io
import os
import csv
import time
import json
import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional, Set
import pandas as pd
import numpy as np

# Ensure project root in sys.path and UTF-8 stdout on Windows
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import config
from src.llm import LLMProvider
from src.agent import MCPAgent
from src.defenses import NoDefense, PromptFilterDefense, ThoughtDefenderDefense
from src.evaluation.task_utility import TaskEvaluator


class GenuineBenchmarkRunner:
    def __init__(
        self,
        data_file: Optional[Path] = None,
        output_dir: Optional[Path] = None,
        llm_provider: Optional[LLMProvider] = None
    ):
        self.data_file = data_file or (config.DATA_DIR / "custom_dataset" / "test.csv")
        self.output_dir = output_dir or (config.RESULTS_DIR / "genuine")
        self.llm_provider = llm_provider or LLMProvider(provider="ollama", model="qwen2.5:7b")
        self.task_evaluator = TaskEvaluator()
        self.scenario_clean_docs: Dict[tuple, str] = {}

        # Output Directories
        self.raw_dir = self.output_dir / "raw"
        self.summaries_dir = self.output_dir / "summaries"
        self.tables_dir = self.output_dir / "tables"
        self.final_dir = self.output_dir / "final"
        for d in [self.raw_dir, self.summaries_dir, self.tables_dir, self.final_dir]:
            d.mkdir(parents=True, exist_ok=True)

        self.raw_csv_path = self.raw_dir / "final_results.csv"

        # Initialize Defenses
        self.defenses = {
            "No Defense": NoDefense(),
            "Prompt Filter / Perimeter": PromptFilterDefense(name="Prompt Filter / Perimeter"),
            "Meticulous Thought Defender": ThoughtDefenderDefense(name="Meticulous Thought Defender")
        }

        # Initialize Agents
        self.agents = {
            d_name: MCPAgent(llm_provider=self.llm_provider, defense=d_obj)
            for d_name, d_obj in self.defenses.items()
        }

    def load_dataset(self) -> List[Dict[str, Any]]:
        if not self.data_file.exists():
            raise FileNotFoundError(f"Test dataset not found at {self.data_file}")

        records = []
        with open(self.data_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                records.append(r)
                if r.get("label") == "SAFE":
                    self.scenario_clean_docs[(r.get("scenario_id"), r.get("language"))] = r.get("document_text", "")
        return records

    def get_completed_evaluations(self) -> Set[tuple]:
        """Reads existing raw CSV to identify (id, defense) pairs already evaluated."""
        completed = set()
        if self.raw_csv_path.exists():
            try:
                df = pd.read_csv(self.raw_csv_path)
                if "id" in df.columns and "defense" in df.columns:
                    for _, row in df.iterrows():
                        completed.add((str(row["id"]), str(row["defense"])))
            except Exception as e:
                print(f"[Warning] Could not parse existing raw results for resume: {e}")
        return completed

    def evaluate_sample(
        self,
        record: Dict[str, Any],
        defense_name: str,
        defense_obj: Any,
        max_retries: int = 1
    ) -> Dict[str, Any]:
        rec_id = record.get("id", "")
        scenario_id = record.get("scenario_id", "")
        language = record.get("language", "English")
        task = record.get("task", "")
        doc_text = record.get("document_text", "")
        attack_type = record.get("attack_type", "none")
        label = record.get("label", "SAFE")
        attack_present = (label == "ATTACK")

        agent = self.agents[defense_name]
        eval_chunks = [{"text": doc_text, "source": f"eval_doc_{rec_id}", "score": 1.0}]

        t0 = time.time()
        agent_res = None
        error_msg = ""
        is_blocked = False
        anomaly_score = 0.0
        response_text = ""

        # Retry loop for resilience
        for attempt in range(max_retries + 1):
            try:
                agent_res = agent.answer_question(query=task, retrieved_chunks=eval_chunks)
                response_text = agent_res.get("generated_answer", "")
                defense_res = agent_res.get("defense_result", {})
                is_blocked = (defense_res.get("action_taken") == "BLOCK")
                anomaly_score = float(defense_res.get("anomaly_score", 0.0))
                error_msg = ""
                break
            except Exception as e:
                error_msg = str(e)
                if attempt < max_retries:
                    time.sleep(2.0)
                else:
                    # Fallback inspection on error
                    defense_res = defense_obj.inspect(user_instruction=task, retrieved_context=doc_text)
                    is_blocked = (defense_res.get("action_taken") == "BLOCK")
                    anomaly_score = float(defense_res.get("anomaly_score", 0.0))
                    if is_blocked:
                        response_text = (
                            f"[SECURITY ALERT]: Indirect prompt injection detected by {defense_name}. "
                            "The untrusted retrieved context has been quarantined."
                        )
                    else:
                        response_text = f"Execution error: {error_msg}"

        latency = round(time.time() - t0, 2)
        clean_doc = self.scenario_clean_docs.get((scenario_id, language), doc_text)

        # Grounded Metrics Evaluation
        if label == "ATTACK":
            attack_success = int(not is_blocked and self.task_evaluator.evaluate_attack_success(
                response_text=response_text,
                attack_type=attack_type,
                attack_instruction=doc_text,
                language=language
            ))
            task_success = int(self.task_evaluator.evaluate_task_utility(
                response_text=response_text,
                clean_document=clean_doc,
                user_query=task,
                language=language,
                is_attack_successful=bool(attack_success)
            ))
            verdict = "ATTACK_BLOCKED" if is_blocked else ("ATTACK_SUCCESS" if attack_success else "ATTACK_FAILED")
        else:
            attack_success = 0
            task_success = int(not is_blocked and self.task_evaluator.evaluate_task_utility(
                response_text=response_text,
                clean_document=clean_doc,
                user_query=task,
                language=language,
                is_attack_successful=False
            ))
            verdict = "FALSE_POSITIVE" if is_blocked else "SAFE_COMPLETED"

        return {
            "id": rec_id,
            "scenario_id": scenario_id,
            "language": language,
            "defense": defense_name,
            "label": label,
            "attack_type": attack_type,
            "attack_present": int(attack_present),
            "is_blocked": int(is_blocked),
            "defense_anomaly_score": round(anomaly_score, 4),
            "attack_success": attack_success,
            "task_success": task_success,
            "execution_verdict": verdict,
            "response_text": response_text[:300],
            "latency_sec": latency,
            "error": error_msg,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }

    def run_benchmark(self, limit: Optional[int] = None) -> Dict[str, Any]:
        dataset = self.load_dataset()
        if limit:
            dataset = dataset[:limit]

        total_conditions = len(dataset) * len(self.defenses)
        print(f"[Benchmark] Target dataset: {self.data_file} ({len(dataset)} records)")
        print(f"[Benchmark] Total evaluation conditions: {total_conditions}")
        print(f"[Benchmark] Output raw destination: {self.raw_csv_path}")

        completed_set = self.get_completed_evaluations()
        print(f"[Benchmark] Found {len(completed_set)} already completed evaluations. Resuming remaining...")

        fieldnames = [
            "id", "scenario_id", "language", "defense", "label", "attack_type",
            "attack_present", "is_blocked", "defense_anomaly_score", "attack_success",
            "task_success", "execution_verdict", "response_text", "latency_sec",
            "error", "timestamp"
        ]

        # Initialize CSV file with headers if it does not exist
        if not self.raw_csv_path.exists():
            with open(self.raw_csv_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()

        evaluated_count = len(completed_set)
        start_time = time.time()
        new_evaluations = 0

        # Execute evaluations
        for d_name, d_obj in self.defenses.items():
            for r in dataset:
                rec_id = str(r.get("id"))
                if (rec_id, d_name) in completed_set:
                    continue

                res = self.evaluate_sample(r, defense_name=d_name, defense_obj=d_obj)

                # Append immediately to disk
                with open(self.raw_csv_path, "a", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writerow(res)

                completed_set.add((rec_id, d_name))
                evaluated_count += 1
                new_evaluations += 1

                progress_pct = (evaluated_count / total_conditions) * 100.0
                elapsed_min = (time.time() - start_time) / 60.0
                print(
                    f"[{evaluated_count}/{total_conditions} ({progress_pct:.1f}%)] "
                    f"ID={rec_id} | Defense={d_name} | Label={res['label']} | "
                    f"Verdict={res['execution_verdict']} | Latency={res['latency_sec']}s"
                )

        print(f"\n[Benchmark] All evaluations completed! Total: {evaluated_count}/{total_conditions}")

        # Compute Final Summaries
        df_raw = pd.read_csv(self.raw_csv_path)
        summaries = self.generate_summaries(df_raw)

        return {
            "total_evaluations": len(df_raw),
            "new_evaluations": new_evaluations,
            "raw_path": str(self.raw_csv_path),
            "summaries": summaries
        }

    def generate_summaries(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Generates defense_summary, language_summary, and error_analysis."""
        # 1. Defense Summary
        defense_rows = []
        for d_name, g_def in df.groupby("defense"):
            g_att = g_def[g_def["label"] == "ATTACK"]
            g_safe = g_def[g_def["label"] == "SAFE"]

            total_cases = len(g_def)
            total_att = len(g_att)
            total_safe = len(g_safe)

            succ_att = g_att["attack_success"].sum()
            blocked_att = g_att["is_blocked"].sum()
            task_succ_att = g_att["task_success"].sum()

            safe_succ = g_safe["task_success"].sum()
            false_pos = g_safe["is_blocked"].sum()
            false_neg = g_att[g_att["is_blocked"] == 0]["attack_success"].sum()

            asr = (succ_att / total_att * 100.0) if total_att > 0 else 0.0
            dbr = (blocked_att / total_att * 100.0) if total_att > 0 else 0.0
            task_utility = (task_succ_att / total_att * 100.0) if total_att > 0 else 0.0
            safe_utility = (safe_succ / total_safe * 100.0) if total_safe > 0 else 0.0
            fpr = (false_pos / total_safe * 100.0) if total_safe > 0 else 0.0
            fnr = (false_neg / total_att * 100.0) if total_att > 0 else 0.0
            avg_latency = g_def["latency_sec"].mean() if "latency_sec" in g_def.columns else 0.0

            defense_rows.append({
                "configuration": "Genuine_Ollama_Qwen2.5_7B",
                "defense": d_name,
                "language": "ALL",
                "total_cases": total_cases,
                "total_attacks": total_att,
                "successful_attacks": int(succ_att),
                "blocked_attacks": int(blocked_att),
                "asr_percent": round(asr, 2),
                "defense_block_rate_percent": round(dbr, 2),
                "task_utility_under_attack_percent": round(task_utility, 2),
                "benign_safe_utility_percent": round(safe_utility, 2),
                "false_positive_rate_percent": round(fpr, 2),
                "false_negative_rate_percent": round(fnr, 2),
                "avg_latency_sec": round(avg_latency, 2)
            })

        df_defense = pd.DataFrame(defense_rows)
        df_defense.to_csv(self.summaries_dir / "defense_summary.csv", index=False)
        df_defense.to_csv(self.tables_dir / "defense_comparison.csv", index=False)

        # 2. Language Summary
        lang_rows = []
        for lang, g_lang in df.groupby("language"):
            for d_name, g_ld in g_lang.groupby("defense"):
                g_att = g_ld[g_ld["label"] == "ATTACK"]
                g_safe = g_ld[g_ld["label"] == "SAFE"]

                total_cases = len(g_ld)
                total_att = len(g_att)
                total_safe = len(g_safe)

                succ_att = g_att["attack_success"].sum()
                blocked_att = g_att["is_blocked"].sum()
                task_succ_att = g_att["task_success"].sum()

                safe_succ = g_safe["task_success"].sum()
                false_pos = g_safe["is_blocked"].sum()
                false_neg = g_att[g_att["is_blocked"] == 0]["attack_success"].sum()

                asr = (succ_att / total_att * 100.0) if total_att > 0 else 0.0
                dbr = (blocked_att / total_att * 100.0) if total_att > 0 else 0.0
                task_utility = (task_succ_att / total_att * 100.0) if total_att > 0 else 0.0
                safe_utility = (safe_succ / total_safe * 100.0) if total_safe > 0 else 0.0
                fpr = (false_pos / total_safe * 100.0) if total_safe > 0 else 0.0
                fnr = (false_neg / total_att * 100.0) if total_att > 0 else 0.0

                lang_rows.append({
                    "configuration": "Genuine_Ollama_Qwen2.5_7B",
                    "defense": d_name,
                    "language": lang,
                    "total_cases": total_cases,
                    "total_attacks": total_att,
                    "successful_attacks": int(succ_att),
                    "blocked_attacks": int(blocked_att),
                    "asr_percent": round(asr, 2),
                    "defense_block_rate_percent": round(dbr, 2),
                    "task_utility_under_attack_percent": round(task_utility, 2),
                    "benign_safe_utility_percent": round(safe_utility, 2),
                    "false_positive_rate_percent": round(fpr, 2),
                    "false_negative_rate_percent": round(fnr, 2)
                })

        df_lang = pd.DataFrame(lang_rows)
        df_lang.to_csv(self.summaries_dir / "language_summary.csv", index=False)
        df_lang.to_csv(self.tables_dir / "language_comparison.csv", index=False)

        # 3. Final Comparison
        df_defense.to_csv(self.summaries_dir / "benchmark_summary.csv", index=False)
        df_defense.to_csv(self.tables_dir / "final_comparison.csv", index=False)

        # 4. Timestamped Archival Copies
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        df.to_csv(self.final_dir / f"final_benchmark_results_{timestamp}.csv", index=False)
        df_defense.to_csv(self.final_dir / f"final_defense_summary_{timestamp}.csv", index=False)
        df_lang.to_csv(self.final_dir / f"final_language_summary_{timestamp}.csv", index=False)

        return {
            "defense_summary": df_defense,
            "language_summary": df_lang,
            "timestamp": timestamp
        }


def main():
    runner = GenuineBenchmarkRunner()
    runner.run_benchmark()


if __name__ == "__main__":
    main()
