"""
CLI Evaluation Script - Meticulous Thought Defender Prototype
Runs evaluation pipeline, outputs metrics summary table, generates CSV results and figures.
"""
import sys
import os

# Pre-set PyTorch DLL loading flags for Windows
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["OMP_NUM_THREADS"] = "1"

try:
    import torch
    _ = torch.tensor([1.0])
except Exception:
    pass

from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.evaluate import run_evaluation_pipeline

def main():
    print("=" * 60)
    print("   METICULOUS THOUGHT DEFENDER - WEEK 2 EVALUATION   ")
    print("=" * 60)
    
    eval_output = run_evaluation_pipeline()
    metrics = eval_output["metrics"]
    backend = metrics.get("embedding_backend", "UNKNOWN")
    
    print("\n" + "-" * 40)
    print("         PERFORMANCE METRICS SUMMARY         ")
    print("-" * 40)
    print(f"Embedding Backend: {backend}")
    if backend == "MOCK":
        print("Note: [Toy/prototype validation result using mock embeddings]")
    else:
        print("Note: [Prototype validation result using REAL BGE-M3 model]")
    print(f"Accuracy:          {metrics['accuracy'] * 100:.2f}%")
    print(f"Precision:         {metrics['precision'] * 100:.2f}%")
    print(f"Recall:            {metrics['recall'] * 100:.2f}%")
    print(f"F1-Score:          {metrics['f1_score'] * 100:.2f}%")
    print("-" * 40)
    print("Confusion Matrix [SAFE, PROMPT_INJECTION]:")
    print(f"  SAFE -> {metrics['confusion_matrix'][0]}")
    print(f"  INJ  -> {metrics['confusion_matrix'][1]}")
    print("-" * 40)
    
    print("\n[Success] CSV results saved to results/week2_results.csv")
    print("[Success] Figures generated in results/figures/\n")
    print("=" * 60)

if __name__ == "__main__":
    main()
