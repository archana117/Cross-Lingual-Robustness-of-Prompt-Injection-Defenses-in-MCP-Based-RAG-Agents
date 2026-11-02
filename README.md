# Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents
## Week 2: Core Meticulous Thought Defender Prototype & Week 3: MCP + RAG Baseline Integration

### 1. Project Overview
This repository contains the **Week 2 core prototype** and **Week 3 MCP + RAG baseline implementation** for the research project *Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents*.

### 2. Objectives
- **Week 2 Objective**: Construct a modular, reproducible prototype that demonstrates prompt injection detection by analyzing step-by-step semantic flow in LLM reasoning traces.
- **Week 3 Objective**: Establish a clean, working **Model Context Protocol (MCP)** research prototype server and **Retrieval-Augmented Generation (RAG)** pipeline. Ingest 5 safe factual documents, chunk and index them using `BAAI/bge-m3` vectors in ChromaDB, expose retrieval via an MCP tool (`search_documents`), and execute safe baseline RAG agent queries.

---

### 3. Relation to Base Paper
The prototype is inspired by the IEEE Access 2025 paper:
> **Meticulous Thought Defender: Fine-Grained Chain-of-Thought (CoT) for Detecting Prompt Injection Attacks of Large Language Models**  
> *Authors:* Lijuan Shi, Yajing Kang, Jie Hu, Xinchi Li, Mingchuan Yang  
> *DOI:* [10.1109/ACCESS.2025.3583759](https://doi.org/10.1109/ACCESS.2025.3583759)

> **Research Integrity & Reproduction Disclaimer**:  
> This software is a **simplified research prototype** inspired by the core semantic consistency and anomaly backtracking concepts of the *Meticulous Thought Defender* framework.  
> - It is **NOT** an exact reproduction of the base paper's 4×A100 GPU supervised fine-tuning suite.  
> - It does **NOT** claim access to hidden/private internal Chain-of-Thought tokens of proprietary models.  
> - It relies on controlled explicit output reasoning traces (`STEP 1: ...`, `STEP 2: ...`) to analyze step-by-step semantic flow.

---

### 4. Implemented vs Deferred Components

| Component / Concept | Implementation Status | Notes |
| :--- | :--- | :--- |
| **Reasoning Step Extraction** | **Implemented** (`src/reasoning.py`) | Regex & fallback parsing for `STEP 1:` formatted traces |
| **BGE-M3 Embedding Manager** | **Implemented** (`src/embeddings.py`) | Pretrained `BAAI/bge-m3` (1024-dim) via SentenceTransformers |
| **Consecutive Cosine Similarity** | **Implemented** (`src/consistency.py`) | Pairwise cosine similarity calculation |
| **Step & Path Consistency** | **Implemented** (`src/consistency.py`) | Local step consistency and mean path flow |
| **Anomaly Scoring & Classification** | **Implemented** (`src/detector.py`) | Heuristic prototype anomaly formulation |
| **Reasoning Tree & DFS Backtracking** | **Implemented** (`src/reasoning_tree.py`) | Simplified sequential tree prototype representation |
| **Offline Deterministic Mock Mode** | **Implemented** (`src/embeddings.py`) | Deterministic fallback for fast offline unit testing |
| **Document Ingestion & Chunking** | **Implemented** (`src/rag/`) | Fixed-size window chunking (`chunk_size=500`, `overlap=50`) |
| **ChromaDB Vector Store** | **Implemented** (`src/rag/vector_store.py`) | Persistent local vector store with dynamic collection naming |
| **RAG Retriever** | **Implemented** (`src/rag/retriever.py`) | Semantic similarity retrieval over document chunks |
| **MCP Tool Server** | **Implemented** (`src/mcp/server.py`) | Built with FastMCP (`mcp>=1.30.0,<2.0.0`), exposing `search_documents` |
| **MCP RAG Agent & Orchestration** | **Implemented** (`src/agent.py`) | Context grounding, tool invocation, and LLM output generation |
| **Supervised Fine-Tuning (SFT)** | **NOT Implemented** | Base paper's 4×A100 SFT is out of project scope |
| **Indirect Prompt Injection Attacks** | **NOT Implemented** | Deferred to Week 4 |
| **Telugu / Hindi / Code-Mixed Benchmark**| **NOT Implemented** | Deferred to Week 4 |

---

### 5. Week 3 Architecture (MCP + RAG Baseline)

```
Documents (data/documents/)
   ↓
Document Loader & Chunker (src/rag/document_loader.py, src/rag/chunker.py)
   ↓
BGE-M3 Embeddings (src/embeddings.py)
   ↓
ChromaDB Vector Database (src/rag/vector_store.py)
   ↓
RAG Retriever (src/rag/retriever.py)
   ↓
MCP Server [FastMCP] (src/mcp/server.py) → Tool: search_documents(query, top_k)
   ↓
MCP Agent Orchestrator (src/agent.py)
   ↓
LLM Context-Grounded Answer (src/llm.py)
   ↓ (Optional Monitoring)
Thought Defender Detector (src/detector.py)
```

---

### 6. Installation & Setup

```bash
# 1. Create and activate Python 3.10+ virtual environment
python -m venv venv

# PowerShell (Windows):
.\venv\Scripts\Activate.ps1
# Bash (Linux/macOS):
source venv/bin/activate

# 2. Install required dependencies
pip install -r requirements.txt
```

---

### 7. Environment Configuration
Copy `.env.example` to `.env`:
```env
LLM_PROVIDER=mock
BGE_MODEL_NAME=BAAI/bge-m3
ANOMALY_THRESHOLD=0.30
DOCUMENTS_DIR=data/documents
VECTOR_DB_DIR=data/vector_db
CHUNK_SIZE=500
CHUNK_OVERLAP=50
TOP_K=3
MCP_SERVER_NAME=ArchanaRAGServer
```

---

### 8. Reproduction & Verification Commands

#### A. Dedicated MCP Protocol Verification Paths
The framework provides two distinct verification scripts for research transparency:
1. **Actual Stdio MCP Client/Server Transport Verification (Process-Separated)**:
   ```bash
   python scripts/verify_mcp_e2e.py
   ```
   *Spawns `src/mcp/server.py` as a standalone subprocess via stdio JSON-RPC transport. Uses `mcp.client.stdio.stdio_client` and `ClientSession` to initialize, discover tools (`search_documents`), execute retrieval, and verify metadata/scores over the actual wire protocol.*

2. **In-Process FastMCP Registry Verification (Fast Unit Testing)**:
   ```bash
   python scripts/verify_mcp_server.py
   ```
   *Directly tests the FastMCP tool registry manager (`mcp_server._tool_manager.call_tool`) in-process for lightweight local unit testing.*

#### B. Running Standalone Stdio MCP Server
To launch the server directly for standard external MCP hosts (e.g., Claude Desktop, Cursor, or MCP Inspector):
```bash
# Direct Python stdio server:
python src/mcp/server.py

# Or via FastMCP CLI Inspector:
mcp dev src/mcp/server.py
```

#### C. Running Week 3 Baseline MCP + RAG Demo (Mock & Real BGE-M3 Modes)
- **Fast Offline Mock Mode**:
  ```powershell
  $env:BGE_MODEL_NAME="mock"; $env:LLM_PROVIDER="mock"; python scripts/run_mcp_rag.py
  ```
- **Real BGE-M3 Mode**:
  ```powershell
  $env:BGE_MODEL_NAME="BAAI/bge-m3"; $env:LLM_PROVIDER="mock"; python scripts/run_mcp_rag.py
  ```
*Ingests 5 safe documents, initializes ChromaDB vector store (`rag_docs_1024` for BGE-M3 or `rag_docs_384` for Mock), executes MCP tool `search_documents`, and runs 5 baseline factual queries (`Hyderabad`, `Solar Energy`, `Relational Databases`, `Machine Learning`, `Cloud Computing`).*

#### D. Running Complete Test Suite (21 Tests)
```bash
python -m pytest tests/
```
*Runs all 21 unit and integration tests across Week 2 (extraction, cosine similarity, anomaly detection, tree backtracking, embedding loader) and Week 3 (document loader, chunker, vector store, retriever, MCP server tool, MCP agent execution).*

#### E. Running Week 2 Thought Defender Detection Demo & Evaluation
```bash
python scripts/run_demo.py
python scripts/run_evaluation.py
```

---

### 9. RAG Benchmark Corpus (5 Safe Factual Documents)
Located under `data/documents/`:
1. `hyderabad.txt`: Historical facts, landmarks (Charminar, Golconda), IT hub profile.
2. `renewable_energy.txt`: Overview of solar, wind, hydroelectric power, and global transitions.
3. `databases.txt`: Relational SQL vs NoSQL document stores and ACID transactions.
4. `machine_learning.txt`: Supervised, unsupervised, reinforcement learning, and neural networks.
5. `cloud_computing.txt`: Infrastructure as a Service (IaaS), PaaS, SaaS, and hybrid deployments.

---

### 10. Summary of Evaluation & Verification Results

#### A. Week 3 Baseline MCP RAG Verification
- **Total Safe Queries Tested**: 5
- **Tool Calls Executed**: 5 (`search_documents` invoked for all queries)
- **Retrieval Precision**: 100% (Top chunks retrieved matched target domain facts)
- **Answer Generation**: Clean, context-grounded factual answers produced without security triggers.

#### B. Week 2 Real BGE-M3 Detector Performance (12 Development Samples)
- **Active Backend**: `REAL_BGE_M3` (`BAAI/bge-m3` 1024-dimensional vectors)
- **Accuracy**: **83.33%** (10 / 12 correct)
- **Precision**: **71.43%** (5 True Positives / 7 Predicted Injections)
- **Recall**: **100.00%** (5 / 5 Prompt Injections detected)
- **F1-Score**: **83.33%**

---

### 11. Project Directory Layout

```
PROJECT ARCHANA/
├── config.py                 # Centralized configuration (RAG, MCP, Embeddings, LLM)
├── requirements.txt          # Production & research dependencies (mcp, chromadb, sentence-transformers)
├── README.md                 # Complete documentation & reproduction guide
├── data/
│   ├── sample_prompts.json   # 12 synthetic reasoning trace development samples
│   └── documents/            # 5 safe factual domain text files for Week 3 RAG
├── src/
│   ├── embeddings.py         # BGE-M3 and deterministic mock embedding manager
│   ├── reasoning.py          # Reasoning step parser & regex extractor
│   ├── consistency.py        # Pairwise cosine similarity and path consistency
│   ├── detector.py           # Anomaly scoring & SAFE vs PROMPT_INJECTION classification
│   ├── reasoning_tree.py     # Sequential reasoning trace DFS backtracking
│   ├── llm.py                # LLM response and RAG answer generator
│   ├── agent.py              # MCPAgent orchestrator executing MCP tools and RAG flows
│   ├── rag/
│   │   ├── document_loader.py # Text file loader
│   │   ├── chunker.py         # Deterministic overlapping chunker
│   │   ├── vector_store.py    # ChromaDB persistent store with dynamic collection fallback
│   │   └── retriever.py       # Similarity search retriever
│   └── mcp/
│       └── server.py          # FastMCP server exposing search_documents tool
├── scripts/
│   ├── run_demo.py           # Week 2 reasoning trace detection demo
│   ├── run_evaluation.py     # Week 2 detector evaluation script
│   └── run_mcp_rag.py        # Week 3 MCP RAG baseline execution script
└── tests/                    # 21 automated unit and integration tests
```

---

### 12. InjecAgent Multilingual Benchmark Integration (Week 4 Implementation)

The project integrates the complete **InjecAgent** benchmark and extends it cross-lingually to evaluate prompt-injection defenses:

1. **Benchmark Datasets (`data/existing_dataset/InjecAgent/`)**:
   - `user_cases.jsonl`: 17 legitimate user cases
   - `attacker_cases_dh.jsonl`: 30 Direct Harm attack cases
   - `attacker_cases_ds.jsonl`: 32 Data Stealing attack cases
   - `test_cases_dh_base.json` & `test_cases_dh_enhanced.json`: 510 + 510 = 1,020 Direct Harm cases
   - `test_cases_ds_base.json` & `test_cases_ds_enhanced.json`: 544 + 544 = 1,088 Data Stealing cases
   - `tools.json`: 38 toolkits defining 330 tools (100% matched)
   - `attacker_simulated_responses.json`: 2,347 precomputed simulated tool return values

2. **Multilingual Test Sets (`data/custom_dataset/multilingual/`)**:
   - `english/`: 2,108 cases (baseline)
   - `hindi/`: 2,108 high-fidelity cases with exact `original_case_id` traceability
   - `telugu/`: 2,108 high-fidelity cases with exact `original_case_id` traceability
   - `code_mixed/`: 2,108 Hinglish / Tenglish cases with exact `original_case_id` traceability

3. **Evaluation Defenses (`src/defenses/`)**:
   - `NoDefense`: Baseline measuring unmitigated agent vulnerability
   - `PromptFilterDefense`: Heuristic perimeter keyword & delimiter defense
   - `ThoughtDefenderDefense`: CoT semantic consistency defense via BGE-M3 reasoning step transitions

4. **Running Benchmark Evaluations**:
   ```bash
   # Run quick 20-sample benchmark across all 4 languages with all defenses:
   python scripts/run_injecagent_benchmark.py --language all --defense all --max-cases 20

   # Run complete evaluation on Hindi:
   python scripts/run_injecagent_benchmark.py --language hindi --defense thought_defender --max-cases 0
   ```

5. **Running Full Test Suite (43 Automated Tests)**:
   ```bash
   python -m pytest tests/
   ```


