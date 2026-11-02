"""
CLI Script - Week 3 MCP + RAG Baseline Demonstration.
Executes complete end-to-end MCP RAG pipeline across 5 safe baseline queries.
"""
import sys
import io
import os
import json
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

from src.agent import MCPAgent
from src.llm import LLMProvider

BASELINE_QUESTIONS = [
    "What is Hyderabad?",
    "What are the benefits of renewable energy?",
    "What is a database index?",
    "What is machine learning?",
    "What is cloud computing?"
]

def main():
    print("=" * 60)
    print("     PROJECT ARCHANA - WEEK 3 MCP + RAG BASELINE      ")
    print("=" * 60)

    agent = MCPAgent()
    backend = agent.retriever.vector_store.embedding_manager.backend_name
    provider = agent.llm_provider.provider

    print(f"Embedding Backend: {backend}")
    print(f"LLM Provider:      {provider.upper()}")
    print("=" * 60)

    for idx, question in enumerate(BASELINE_QUESTIONS, start=1):
        print(f"\n[Test Query {idx}/5]")
        print(f"User Question: {question}")
        print("-" * 50)

        res = agent.answer_question(question)
        retrieved = res["retrieved_chunks"]

        print("Retrieved Documents:")
        for r_idx, chunk in enumerate(retrieved, start=1):
            print(f"  {r_idx}. Source: {chunk['source']} (Score: {chunk['score']:.4f})")
            snippet = chunk['text'].replace('\n', ' ')
            if len(snippet) > 120:
                snippet = snippet[:117] + "..."
            print(f"     Text: \"{snippet}\"")

        print("\nGenerated Answer:")
        print(f"  {res['generated_answer']}")

        print("\nTrace Log:")
        print(f"  {json.dumps(res['trace_log'])}")
        print("=" * 60)

    print("\n[Success] Week 3 MCP + RAG Baseline demonstration completed successfully.")

if __name__ == "__main__":
    main()
