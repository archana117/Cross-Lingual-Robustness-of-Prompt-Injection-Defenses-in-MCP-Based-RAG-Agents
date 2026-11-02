# Current Project Audit

**Project**: Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents  
**Audit Date**: 2026-10-07  
**Auditor**: Antigravity Assistant  

---

## 1. Current Architecture

The project implements an end-to-end multilingual RAG framework connected to a Model Context Protocol (MCP) server. The overall data and inference pipeline comprises:
1. **Document Corpus**: Synthesized enterprise documents across 5 domains (Healthcare, Finance, Legal, Tech/DevOps, Human Resources).
2. **Chunker**: Recursive character/token boundary splitting (`chunk_size=500`, `chunk_overlap=50`) in [`src/chunker.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/chunker.py).
3. **Embeddings**: `BAAI/bge-m3` dense multilingual 1024-dimensional bi-encoder with mock fallback in [`src/embeddings.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/embeddings.py).
4. **Vector Store**: ChromaDB with cosine similarity indexing in [`src/vector_store.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/vector_store.py) and [`src/retriever.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/retriever.py).
5. **MCP Server**: FastMCP server in [`src/mcp_server.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/mcp_server.py) exposing `search_documents(query, top_k)` over stdio JSON-RPC transport.
6. **MCP Client/Agent**: LLM agent in [`src/agent.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/agent.py) discovering tools, issuing queries, and managing context retrieval.
7. **Defenses**:
   - Condition 1: No Defense (pass-through baseline).
   - Condition 2: Prompt Filter / Perimeter (lexical regex scanner matching 18 English trigger patterns).
   - Condition 3: Meticulous Thought Defender (semantic Chain-of-Thought anomaly detector measuring consecutive step similarities).
8. **Evaluation Engine**: Grounded evaluator in [`src/evaluation/task_utility.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/evaluation/task_utility.py) and benchmark orchestrator in [`src/evaluation/benchmark_runner.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/evaluation/benchmark_runner.py).

---

## 2. Current Dataset

Located in `data/custom_dataset/`:
- **Total Records**: 2,000 records.
- **Language Balance**: 500 English, 500 Hindi, 500 Telugu, 500 Telugu-English Code-Mixed.
- **Label Balance**: 1,000 Safe records, 1,000 Attack records (250 Safe + 250 Attack per language).
- **Enterprise Scenarios**: 250 distinct scenario IDs (50 per domain).
- **Partitioning**:
  - `train.csv`: 175 scenarios (70%, 1,400 records).
  - `validation.csv`: 38 scenarios (~15%, 304 records).
  - `test.csv`: 37 scenarios (~15%, 296 records).
- **Leakage Status**: Strictly split by `scenario_id` with 0 leakage across splits.

---

## 3. Current Attack Implementation

- **Threat Model**: Indirect Prompt Injection (IPI) exclusively.
- **Mechanism**: The user query is benign (e.g., asking for factual company policies or clinical dosages). The retrieved document contains normal factual text contaminated with an injection payload.
- **Attack Types**: Instruction Override, Data Exfiltration, Privilege Escalation, Unauthorized Tool Invocation, Policy Violation.
- **Placement**: Payloads inserted at start, middle, or end of retrieved context chunks.

---

## 4. Current MCP-RAG Flow

1. Client agent sends user instruction to FastMCP server via JSON-RPC `tools/call`.
2. FastMCP server runs `search_documents`, queries ChromaDB via BGE-M3 dense embeddings.
3. Retrieved chunks containing similarity scores and source metadata are returned to agent.
4. Agent submits context through the defense layer.
5. If defense flags an anomaly, context is quarantined and an alert is emitted; otherwise, LLM synthesizes answer.
6. Evaluator validates whether attack succeeded and whether legitimate task was completed.

---

## 5. Current Defense Implementations

1. **No Defense**: Passes prompt and retrieved document directly to generation engine without inspection.
2. **Prompt Filter / Perimeter**: Lexical pattern matcher checking 18 English keywords. Detects overt English injections but is completely blind to non-English or subtle injections.
3. **Meticulous Thought Defender**: Analyzes 3-step reasoning traces (`Step 1: User query analysis`, `Step 2: Context ingestion`, `Step 3: Response planning`). Computes consecutive cosine similarities and flags anomaly if score exceeds threshold $\tau$.

---

## 6. Current Evaluation Implementation

- **Attack Success Rate (ASR)**: Proportion of attack cases where model response exhibits known attack signatures.
- **Defense Block Rate (DBR)**: Proportion of attack cases quarantined by defense.
- **Task Utility Under Attack**: Proportion of attacked cases where the legitimate user task was completed.
- **Benign Safe Utility**: Proportion of safe queries accurately answered using factual tokens.
- **FPR / FNR**: Standard binary classification error metrics.

---

## 7. Current Result Files

- Preserved Baseline: `results/baseline_before_fix/` and `results/baseline_results/`.
- Raw Logs: `results/raw/final_results.csv`.
- Summaries: `results/summaries/defense_summary.csv`, `language_summary.csv`, `benchmark_summary.csv`, `error_analysis.csv`.
- Tables: `results/tables/final_comparison.csv`, `defense_comparison.csv`, `language_comparison.csv`.
- Figures: 7 figures in `results/figures/`.
- Final Run: Timestamped exports in `results/final/`.

---

## 8. Problems Discovered

1. **Task Utility = 0% Under Attack**:
   - Defenses act as binary quarantines. When attacks are blocked, factual context is suppressed, leading to 0% task completion. When unblocked, attacks hijack execution (0% utility).
2. **Tokenizer Unicode Truncation in Benign Utility**:
   - Original utility evaluator used regex `\w{4,}`, stripping 2- and 3-letter Indic tokens, which lowered clean benign utility to 87.16% on safe data.
3. **Baseline MTD Mock Fallback**:
   - Baseline MTD ran with mock embeddings that checked only 9 English words, causing 0% block rate in Hindi and Telugu.
4. **Cross-Script Semantic Dispersion in Real BGE-M3**:
   - Evaluating with real BGE-M3 at static threshold $\tau=0.30$ blocks 97.30% of attacks, but produces a 96.62% False Positive Rate in Indic languages because consecutive Indic steps naturally have lower cosine similarity than English.

---

## 9. Recommended Fixes

1. Update tokenizer in `task_utility.py` to `\w{2,}` to properly evaluate Indic words (implemented & verified).
2. Use language-consistent phrasing in MTD reasoning steps to prevent artificial language-boundary drops (implemented & verified).
3. Conduct validation-set threshold calibration to determine language-specific thresholds (implemented & documented in `mtd_threshold_analysis.md`).
4. Maintain strict scientific honesty: report that under binary blocking, Task Utility Under Attack is 0.0%, and static threshold MTD produces high FPR in Indic languages.
