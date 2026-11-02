"""
CLI Demo Script - Meticulous Thought Defender Prototype
Runs interactive / automated demonstration on Case A (Normal), Case B (Prompt Injection),
and Case C (False Positive test case).
"""
import sys
import io
import os
from pathlib import Path

# Pre-set PyTorch DLL loading flags for Windows
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["OMP_NUM_THREADS"] = "1"

try:
    import torch
    _ = torch.tensor([1.0])
except Exception:
    pass

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Ensure stdout uses utf-8 encoding for Windows terminals
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from src.llm import LLMProvider
from src.detector import ThoughtDefender
from src.reasoning_tree import ReasoningTree
from src.utils import load_sample_dataset

def main():
    print("=" * 60)
    print("      METICULOUS THOUGHT DEFENDER - WEEK 2 DEMO      ")
    print("=" * 60)
    
    # Initialize components
    llm = LLMProvider()
    defender = ThoughtDefender()
    dataset = load_sample_dataset()
    backend = defender.embedding_manager.backend_name
    
    print(f"Active Embedding Backend: {backend}")
    if backend == "MOCK":
        print("Note: [Running in offline MOCK embedding mode]")
    else:
        print("Note: [Running in REAL BGE-M3 embedding mode]")
    print("=" * 60)
    
    for sample in dataset:
        sample_id = sample["id"]
        prompt = sample["prompt"]
        true_label = sample["label"].upper()
        
        print("\n" + "-" * 60)
        print(f"Sample ID: {sample_id} | Ground Truth: {true_label}")
        print(f"Prompt: {prompt}")
        print("-" * 60)
        
        # 1. Generate / Retrieve Reasoning Trace
        reasoning_trace = sample.get("reasoning_trace")
        if not reasoning_trace:
            reasoning_trace = llm.generate_reasoning_trace(prompt, sample_id=sample_id)
            
        # 2. Run Thought Defender Detection
        result = defender.analyze_trace(reasoning_trace, prompt=prompt)
        
        print("\nReasoning Steps:")
        for idx, step in enumerate(result["reasoning_steps"], start=1):
            print(f"  {idx}. {step}")
            
        print("\nConsecutive Step Similarities:")
        for sim in result["step_similarities"]:
            print(f"  Step {sim['prev_step_idx']} -> Step {sim['curr_step_idx']}: {sim['similarity']:.4f}")
            
        print(f"\nPath Semantic Consistency: {result['path_consistency']:.4f}")
        print(f"Anomaly Score:            {result['anomaly_score']:.4f} (Threshold: {defender.threshold})")
        
        if result["suspicious_step_idx"]:
            print(f"\nSuspicious Step Localized:")
            print(f"  Step Number: {result['suspicious_step_idx']}")
            print(f"  Step Text:   '{result['suspicious_step_text']}'")
            print(f"  Reason:      {result['suspicious_reason']}")
        else:
            print("\nSuspicious Step: None detected.")
            
        # 3. Reasoning Tree DFS Traversal Demo
        tree = ReasoningTree(result["reasoning_steps"], result["step_similarities"], threshold=defender.threshold)
        dfs_res = tree.dfs_backtracking()
        print(f"\nDFS Backtracking Traversal:")
        print(f"  Visited Nodes:   {len(dfs_res['visited_nodes'])}")
        print(f"  Anomalous Nodes: {len(dfs_res['anomalous_nodes'])}")
        if dfs_res["anomalous_nodes"]:
            for an in dfs_res["anomalous_nodes"]:
                print(f"    -> [Node {an['node_id']}] '{an['step_text']}' (Anomaly: {an['anomaly_value']:.4f})")
                
        print("\n" + "=" * 30)
        print(f"FINAL DECISION: {result['prediction']}")
        print("=" * 30)
        
    print("\n" + "=" * 60)
    print("Demo completed successfully.")
    print("=" * 60)

if __name__ == "__main__":
    main()
