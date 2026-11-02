"""
Unit tests for evaluation metrics and InjecAgent evaluator.
"""

import pytest
from src.evaluation.metrics import compute_benchmark_metrics
from src.evaluation.injecagent_evaluator import InjecAgentEvaluator
from src.defenses.no_defense import NoDefense
from src.defenses.prompt_filter import PromptFilterDefense

def test_compute_benchmark_metrics_empty():
    res = compute_benchmark_metrics([])
    assert res["total_cases"] == 0
    assert res["attack_success_rate"] == 0.0

def test_compute_benchmark_metrics_calculation():
    sample_records = [
        {"attack_succeeded": 1, "task_completed": 0, "defense_action": "ALLOW", "language": "English", "attack_type": "Physical Harm"},
        {"attack_succeeded": 0, "task_completed": 1, "defense_action": "BLOCK", "language": "English", "attack_type": "Physical Harm"},
        {"attack_succeeded": 0, "task_completed": 0, "defense_action": "BLOCK", "language": "Hindi", "attack_type": "Financial Harm"},
        {"attack_succeeded": 1, "task_completed": 0, "defense_action": "ALLOW", "language": "Hindi", "attack_type": "Financial Harm"}
    ]
    metrics = compute_benchmark_metrics(sample_records)
    assert metrics["total_cases"] == 4
    assert metrics["attacks_succeeded"] == 2
    assert metrics["attack_success_rate"] == 0.50
    assert metrics["task_utility_under_attack"] == 0.25
    assert metrics["defense_block_rate"] == 0.50
    assert "English" in metrics["breakdown_by_language"]
    assert "Hindi" in metrics["breakdown_by_language"]

def test_injecagent_evaluator_run_small():
    evaluator = InjecAgentEvaluator(defense=NoDefense())
    result = evaluator.run_benchmark(language="english", max_cases=5, save_results=False)
    assert result["total_evaluated"] == 5
    assert len(result["records"]) == 5
    # No defense means attacks execute
    assert result["metrics"]["attack_success_rate"] > 0
