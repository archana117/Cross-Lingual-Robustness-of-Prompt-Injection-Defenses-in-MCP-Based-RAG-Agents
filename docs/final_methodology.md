# Final Methodology: Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents

**Project**: Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents  
**Target Languages**: English, Hindi (हिन्दी), Telugu (తెలుగు), Telugu-English Code-Mixed (Tenglish)  
**Threat Model**: Indirect Prompt Injection embedded in retrieved enterprise documents  
**Architecture Standard**: Model Context Protocol (MCP) tool-mediated Retrieval-Augmented Generation (RAG)  

---

## 1. System Architecture Overview

The system evaluates the vulnerability of enterprise LLM agents to indirect prompt injections across high-resource and Indic languages. The full end-to-end architecture is structured into eight decoupled stages:

```
[Enterprise Documents]
         │
         ▼
[Semantic Chunker (Recursive Token Split)]
         │
         ▼
[BGE-M3 Multilingual Dense Embedding (1024-dim)]
         │
         ▼
[ChromaDB Vector Store (Cosine Similarity Metric)]
         │
         ▼
[MCP Server (FastMCP / search_documents Tool)]
         │ (JSON-RPC 2.0 via Stdio)
         ▼
[MCP RAG Agent (Client Tool Invocation)]
         │
         ▼
[Defense Layer (No Defense | Prompt Filter | Meticulous Thought Defender)]
         │
         ▼
[LLM Inference (Context-Grounded Generation)]
         │
         ▼
[Evaluation Engine (Grounded Task Utility & Attack Success Verifier)]
```

### Component Details
1. **Document Corpus**: Synthesized multilingual corpus spanning 5 enterprise domains: Healthcare, Finance, Legal, Technology, and Human Resources.
2. **Chunker**: Implemented in [`src/chunker.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/chunker.py). Uses recursive token chunking (`chunk_size=500`, `chunk_overlap=50`) preserving sentence boundaries.
3. **Multilingual Embedder**: Implemented in [`src/embeddings.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/embeddings.py). Uses `BAAI/bge-m3` generating 1024-dimensional normalized dense vectors supporting cross-lingual alignment.
4. **Vector Store**: Implemented in [`src/vector_store.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/vector_store.py) and [`src/retriever.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/retriever.py) using ChromaDB with cosine distance indexing.
5. **MCP Server**: Implemented in [`src/mcp_server.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/mcp_server.py) using `FastMCP`. Exposes `search_documents(query, top_k)` tool over standard stdio transport.
6. **MCP Client Agent**: Implemented in [`src/agent.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/agent.py). Orchestrates query formulation, MCP tool execution, retrieved context inspection, and defensive mediation.

---

## 2. Threat Model: Indirect Prompt Injection

In this benchmark, attacks are strictly **indirect prompt injections** (IPI):
- **User Query**: Legitimate, benign user task asking for factual information (e.g., medical dosage, leave balance, account terms).
- **Retrieved Context**: Contains factual text alongside an embedded, untrusted injection payload designed to hijack execution.
- **Attack Placement**: Injections are embedded at natural locations (start, middle, or end of retrieved chunks).
- **Attack Goals**:
  1. *Exfiltration*: System prompt or confidential data leak.
  2. *Instruction Override*: Override standard protocol and force arbitrary confirmation signatures.
  3. *Unauthorized Tool Invocation*: Trigger privileged sub-agent actions.

---

## 3. Defense Mechanisms

We evaluate three experimental defense conditions:

### 3.1. No Defense (Baseline Control)
- Passes user query and retrieved context directly to the LLM with no filtering or inspection.
- Serves as the negative control showing intrinsic agent vulnerability.

### 3.2. Prompt Filter / Perimeter Defense
- Implemented in [`src/defenses/prompt_filter.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/defenses/prompt_filter.py).
- Lexical regex scanner operating at the context perimeter.
- Inspects retrieved text against 18 explicit override patterns (e.g., `ignore previous instructions`, `system override`, `disregard above`).
- **Limitation**: Lexical rigidity. Injections without exact English trigger phrases or expressed in Indic vernacular bypass this filter completely.

### 3.3. Meticulous Thought Defender (MTD)
- Implemented in [`src/detector.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/detector.py) and adapted via [`src/defenses/thought_defender_adapter.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/defenses/thought_defender_adapter.py).
- Analyzes Chain-of-Thought (CoT) reasoning steps using semantic trajectory continuity.
- Extracts steps $S = [s_1, s_2, \dots, s_k]$ and computes step embeddings $E = [e_1, e_2, \dots, e_k]$ via BGE-M3.
- Computes consecutive cosine similarities:
  $$\text{sim}(e_i, e_{i+1}) = \frac{e_i \cdot e_{i+1}}{\|e_i\| \|e_{i+1}\|}$$
- Computes step consistency $C(s_i)$ and global path consistency $P(S)$:
  $$P(S) = \frac{1}{k-1} \sum_{i=1}^{k-1} \text{sim}(e_i, e_{i+1})$$
- Determines anomaly score:
  $$\alpha = 1.0 - \min_{i} \text{sim}(e_i, e_{i+1})$$
- If $\alpha > \tau$ (where $\tau = 0.30$ is the operational threshold), the sample is flagged as an indirect injection anomaly and quarantined.

---

## 4. Evaluation Metrics & Formal Definitions

Evaluation is grounded using [`src/evaluation/task_utility.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/evaluation/task_utility.py) and [`src/evaluation/benchmark_runner.py`](file:///c:/Users/91799/Downloads/MAJOR%20PROJECT%201/src/evaluation/benchmark_runner.py).

Let $N_{att}$ be the total attack samples, $N_{safe}$ be the total benign safe samples, $B_{att}$ be attacks blocked by the defense, $S_{att}$ be attacks successfully executed by the LLM, $U_{att}$ be attack samples where the legitimate user task was successfully answered, $U_{safe}$ be safe samples successfully answered, $FP$ be safe samples blocked by the defense (False Positives), and $FN$ be attacks that bypassed defense and executed (False Negatives).

1. **Attack Success Rate (ASR)**:
   $$\text{ASR} = \frac{S_{att}}{N_{att}} \times 100\%$$
   Measures the fraction of attacks that bypassed defense and successfully hijacked model output. Lower is better.

2. **Defense Block Rate (DBR)**:
   $$\text{DBR} = \frac{B_{att}}{N_{att}} \times 100\%$$
   Measures the fraction of attack samples identified and quarantined by the defense. Higher is better.

3. **Task Utility Under Attack**:
   $$\text{Utility}_{attack} = \frac{U_{att}}{N_{att}} \times 100\%$$
   Measures whether the user's original query was correctly answered when an attack was present. Under binary blocking, unblocked attacks hijack the model (0% utility) and blocked attacks quarantine the context with a security alert refusal (0% utility), giving 0.0% utility unless fine-grained sanitization is applied.

4. **Benign Safe Utility**:
   $$\text{Utility}_{safe} = \frac{U_{safe}}{N_{safe}} \times 100\%$$
   Measures task completion rate on clean, un-attacked enterprise documents. Evaluated via factual token recall against reference ground truth.

5. **False Positive Rate (FPR)**:
   $$\text{FPR} = \frac{FP}{N_{safe}} \times 100\%$$
   Fraction of legitimate, safe user requests incorrectly blocked by the defense.

6. **False Negative Rate (FNR)**:
   $$\text{FNR} = \frac{FN}{N_{att}} \times 100\%$$
   Fraction of malicious injections that slipped past the defense undetected.

---

## 5. Dataset Partitioning & Leakage Prevention

The benchmark dataset consists of 2,000 verified records distributed across 250 enterprise scenarios:
- **English**: 500 records (250 safe, 250 attack)
- **Hindi**: 500 records (250 safe, 250 attack)
- **Telugu**: 500 records (250 safe, 250 attack)
- **Telugu-English Code-Mixed**: 500 records (250 safe, 250 attack)

**Strict Scenario-Level Split**:
Splits are partitioned strictly by `scenario_id` to prevent cross-split data leakage:
- **Train Split**: 175 scenarios (70%, 1,400 records)
- **Validation Split**: 38 scenarios (~15%, 304 records)
- **Held-Out Test Split**: 37 scenarios (~15%, 296 records)

All final evaluation metrics are computed exclusively on the held-out test split (`data/custom_dataset/test.csv`).
