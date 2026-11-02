"""
Evaluation Module.
Runs detector over sample dataset, computes performance metrics (Accuracy, Precision, Recall, F1),
generates confusion matrix, saves CSV results, and creates plots.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any, List
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import config
from src.utils import load_sample_dataset
from src.detector import ThoughtDefender

def run_evaluation_pipeline(detector: ThoughtDefender = None, dataset_path=None) -> Dict[str, Any]:
    """
    Evaluates detector against dataset and exports results CSV and figures.
    """
    defender = detector or ThoughtDefender()
    dataset = load_sample_dataset(dataset_path)
    backend_name = defender.embedding_manager.backend_name
    
    results = []
    y_true = []
    y_pred = []
    
    print(f"[Info] Active Embedding Backend: {backend_name}")
    print(f"[Info] Running evaluation on {len(dataset)} dataset samples...")
    
    for sample in dataset:
        sample_id = sample["id"]
        prompt = sample["prompt"]
        reasoning_trace = sample.get("reasoning_trace", "")
        # Map label 'safe' -> 'SAFE', 'injection' -> 'PROMPT_INJECTION'
        true_label = "PROMPT_INJECTION" if sample["label"].lower() in ["injection", "attack", "prompt_injection"] else "SAFE"
        
        # Analyze sample
        eval_res = defender.analyze_trace(reasoning_trace, prompt=prompt)
        pred_label = eval_res["prediction"]
        
        y_true.append(true_label)
        y_pred.append(pred_label)
        
        results.append({
            "sample_id": sample_id,
            "language": sample.get("language", "en"),
            "embedding_backend": backend_name,
            "true_label": true_label,
            "predicted_label": pred_label,
            "anomaly_score": round(eval_res["anomaly_score"], 4),
            "path_consistency": round(eval_res["path_consistency"], 4),
            "suspicious_step_idx": eval_res["suspicious_step_idx"],
            "suspicious_step_text": eval_res["suspicious_step_text"] or "N/A"
        })
        
    df_results = pd.DataFrame(results)
    csv_path = config.RESULTS_DIR / "week2_results.csv"
    df_results.to_csv(csv_path, index=False)
    print(f"[Info] Evaluation results exported to {csv_path}")
    
    # Compute Metrics
    labels = ["SAFE", "PROMPT_INJECTION"]
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, pos_label="PROMPT_INJECTION", zero_division=0)
    rec = recall_score(y_true, y_pred, pos_label="PROMPT_INJECTION", zero_division=0)
    f1 = f1_score(y_true, y_pred, pos_label="PROMPT_INJECTION", zero_division=0)
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    
    metrics = {
        "embedding_backend": backend_name,
        "accuracy": float(acc),
        "precision": float(prec),
        "recall": float(rec),
        "f1_score": float(f1),
        "confusion_matrix": cm.tolist()
    }
    
    # Generate Figures
    generate_figures(df_results, cm, labels)
    
    return {
        "metrics": metrics,
        "results_table": df_results
    }

def generate_figures(df_results: pd.DataFrame, cm: np.ndarray, labels: List[str]):
    """
    Generates required matplotlib figures under results/figures/
    1. Step-wise/Sample anomaly score distribution plot
    2. Confusion matrix plot
    """
    config.FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Anomaly Score Distribution Plot
    plt.figure(figsize=(8, 5))
    safe_scores = df_results[df_results["true_label"] == "SAFE"]["anomaly_score"]
    attack_scores = df_results[df_results["true_label"] == "PROMPT_INJECTION"]["anomaly_score"]
    
    plt.scatter(df_results[df_results["true_label"] == "SAFE"]["sample_id"], safe_scores, label="SAFE (Ground Truth)", marker="o", s=80)
    plt.scatter(df_results[df_results["true_label"] == "PROMPT_INJECTION"]["sample_id"], attack_scores, label="PROMPT_INJECTION (Ground Truth)", marker="x", s=100)
    
    plt.axhline(y=config.ANOMALY_THRESHOLD, linestyle="--", label=f"Threshold ({config.ANOMALY_THRESHOLD})")
    plt.title("Thought Defender - Sample Anomaly Score Distribution")
    plt.xlabel("Sample ID")
    plt.ylabel("Anomaly Score")
    plt.ylim(-0.05, 1.05)
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.savefig(config.FIGURES_DIR / "anomaly_score_distribution.png", dpi=300)
    plt.close()
    
    # 2. Confusion Matrix Plot
    plt.figure(figsize=(6, 5))
    plt.imshow(cm, interpolation="nearest")
    plt.title("Thought Defender - Confusion Matrix")
    plt.colorbar()
    tick_marks = np.arange(len(labels))
    plt.xticks(tick_marks, labels)
    plt.yticks(tick_marks, labels)
    
    thresh = cm.max() / 2. if cm.max() > 0 else 1.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, format(cm[i, j], 'd'),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
                     
    plt.ylabel("True Label")
    plt.xlabel("Predicted Label")
    plt.tight_layout()
    plt.savefig(config.FIGURES_DIR / "confusion_matrix.png", dpi=300)
    plt.close()
    
    # 3. Step Similarity Comparison Plot (Case A vs Case B)
    plt.figure(figsize=(8, 5))
    # Plot path consistency values
    plt.bar(df_results["sample_id"], df_results["path_consistency"])
    plt.title("Thought Defender - Reasoning Path Consistency Scores")
    plt.xlabel("Sample ID")
    plt.ylabel("Path Semantic Consistency")
    plt.ylim(0.0, 1.05)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(config.FIGURES_DIR / "path_consistency_comparison.png", dpi=300)
    plt.close()
    
    print(f"[Info] Plots saved successfully to {config.FIGURES_DIR}")
