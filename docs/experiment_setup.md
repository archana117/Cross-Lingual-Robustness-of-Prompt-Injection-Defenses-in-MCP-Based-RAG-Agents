# Experimental Setup Documentation

**Project**: *Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents*  
**Script**: `scripts/run_final_benchmark.py`

---

## 1. Experimental Matrix

The benchmark evaluates the complete $4 \times 3$ factorial design on the held-out test split:

$$\mathbf{4\text{ Languages}} \times \mathbf{3\text{ Defense Conditions}} \times \mathbf{74\text{ Test Cases/Lang}} = \mathbf{888\text{ Full Experimental Trials}}$$

| Dimension | Levels | Specific Configurations |
| :--- | :--- | :--- |
| **Languages** | 4 | English, Hindi, Telugu, Telugu-English Code-Mixed |
| **Defenses** | 3 | No Defense, Prompt Filter / Perimeter, Meticulous Thought Defender |
| **Sample Distribution** | — | 37 Scenarios $\times$ 2 Labels (SAFE / ATTACK) = 74 records per language |
| **Total Test Dataset** | — | 296 unique evaluation records (`data/custom_dataset/test.csv`) |
| **Embedding Engine** | — | `BAAI/bge-m3` (1,024-dimensional normalized dense vectors) |
| **Vector Store** | — | ChromaDB (`data/vector_store_data/chroma_db`) |
| **MCP Protocol** | — | FastMCP (`mcp>=1.30.0,<2.0.0`) via stdio JSON-RPC transport |

---

## 2. Execution Pipeline

```
User Query (Language L)
      │
      ▼
MCP Agent Orchestrator (src/agent.py)
      │
      ▼
MCP Tool Call: search_documents(query, top_k)
      │
      ▼
RAG Retriever & ChromaDB Vector Store
      │
      ▼
Retrieved Knowledge Chunks (with potential embedded injection)
      │
      ▼
Prompt-Injection Defense Layer (src/defenses/)
      ├── No Defense
      ├── Prompt Filter / Perimeter
      └── Meticulous Thought Defender (BGE-M3 CoT Flow Analysis)
      │
      ▼
LLM Answer Generation
      │
      ▼
Evaluation Engine (src/evaluation/)
      ├── Attack Success Evaluation
      ├── Task Utility Evaluation
      └── Summary CSV & Presentation Figure Generation
```

---

## 3. Reproduction Command

```bash
# Execute full final benchmark on test split:
python scripts/run_final_benchmark.py
```
