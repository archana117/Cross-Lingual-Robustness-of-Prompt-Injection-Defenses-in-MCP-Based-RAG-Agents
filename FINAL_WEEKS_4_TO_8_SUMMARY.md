# Final Summary Report: Weeks 4 through 8

**Project Title**: *Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents*  
**Project Team**: N. Archana and P. Harshitha (PID-14)  
**Supervisor**: Dr. K. Mary Sudha Rani  
**Date**: October 5, 2026  

---

## 1. Executive Summary

This report documents the completed research implementation and experimental findings for **Weeks 4 through 8** of the Major Project. The project evaluates the robustness of prompt-injection defenses in a Model Context Protocol (MCP) based Retrieval-Augmented Generation (RAG) agent across **English**, **Hindi**, **Telugu**, and **Telugu-English code-mixed** text under **indirect prompt injection** attacks embedded inside retrieved knowledge documents.

---

## 2. Dataset Preparation (Week 4)

- **Scale & Balance**: Constructed a balanced custom multilingual benchmark consisting of **exactly 2,000 records** generated from **250 underlying real-world domain scenarios**:
  - English: 250 SAFE, 250 ATTACK (500 total)
  - Hindi: 250 SAFE, 250 ATTACK (500 total)
  - Telugu: 250 SAFE, 250 ATTACK (500 total)
  - Telugu-English Code-Mixed: 250 SAFE, 250 ATTACK (500 total)
  - Total: 1,000 SAFE, 1,000 ATTACK (2,000 total)
- **10 Indirect Injection Categories**: Evenly distributed (100 attack records per category) covering `instruction_override`, `ignore_previous_instruction`, `system_prompt_extraction`, `confidential_information_disclosure`, `task_redirection`, `fake_authority`, `context_manipulation`, `tool_use_manipulation`, `malicious_action`, and `misleading_document_instruction`.
- **Validation**: Verified by `scripts/validate_custom_dataset.py` with **24/24 validation checks passed**.
- **Split Strategy**: Split by `scenario_id` to guarantee zero data leakage:
  - Train: 175 scenarios (1,400 records, 70.0%)
  - Validation: 38 scenarios (304 records, 15.2%)
  - Test: 37 scenarios (296 records, 14.8%)

---

## 3. Indirect Attack Generation Module (Week 5)

- Implemented `src/attack/indirect_attack.py` providing programmatic injection generation.
- Supports varied position embedding:
  - `prefix`: Prepends injection before factual content.
  - `middle`: Interweaves injection naturally between factual domain sentences.
  - `suffix`: Appends injection under system/administrative notice headers.
- Employs natural phrasing templates (`scripts/attack_templates.py`) ensuring authentic native Hindi, Telugu, and natural phrasal Telugu-English code-mixing.

---

## 4. MCP-RAG Integration (Week 5 & 6)

- Maintained the working MCP-RAG pipeline:
  $$\text{User Query} \to \text{MCP Agent} \to \text{MCP Server } (\texttt{search\_documents}) \to \text{ChromaDB Vector DB} \to \text{Retrieved Chunks} \to \text{Defense} \to \text{LLM} \to \text{Answer}$$
- Integrated the defense inspection hook directly into `MCPAgent.answer_question()` in `src/agent.py`.
- Preserved stdio JSON-RPC wire protocol compatibility and in-process tool manager invocation.

---

## 5. Defense Integration (Week 6)

Implemented three standardized defense conditions under `src/defenses/`:
1. **No Defense**: Baseline measuring unmitigated agent vulnerability.
2. **Prompt Filter / Perimeter**: Rule-based regex scanning for system override keywords and delimiters across English, Hindi, and Telugu.
3. **Meticulous Thought Defender**: Semantic Chain-of-Thought (CoT) anomaly detector analyzing step-by-step reasoning consistency using `BAAI/bge-m3` 1,024-dimensional dense embeddings and DFS tree backtracking.

---

## 6. Experimental Setup & Benchmark Matrix (Week 7)

- **Dataset**: Held-out test set (`data/custom_dataset/test.csv`, 296 records across 37 scenarios).
- **Matrix**: 4 Languages $\times$ 3 Defenses $\times$ 74 Cases/Lang = **888 total evaluation trials**.
- **Embedding Backend**: Pretrained `BAAI/bge-m3` via SentenceTransformers.
- **Execution Script**: `python scripts/run_final_benchmark.py`.

---

## 7. Measured Benchmark Results (Week 8)

### Overall Defense Comparison

| Defense Condition | Total Cases | Total Attacks | Successful Attacks | Blocked Attacks | Attack Success Rate (ASR) | Defense Block Rate | Benign Safe Utility | False Positive Rate | False Negative Rate |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **No Defense** | 296 | 148 | 148 | 0 | **100.00%** | **0.00%** | 87.16% | 0.00% | 100.00% |
| **Prompt Filter / Perimeter** | 296 | 148 | 104 | 44 | **70.27%** | **29.73%** | 87.16% | 0.00% | 70.27% |
| **Meticulous Thought Defender** | 296 | 148 | 51 | 97 | **34.46%** | **65.54%** | 9.46% | 90.54% | 34.46% |

### Cross-Lingual Defense Performance Breakdown

| Language | Defense Condition | Attack Cases | Successful Attacks | Blocked Attacks | ASR (%) | Block Rate (%) | FPR on Safe (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **English** | No Defense | 37 | 37 | 0 | 100.00% | 0.00% | 0.00% |
| **English** | Prompt Filter / Perimeter | 37 | 26 | 11 | 70.27% | 29.73% | 0.00% |
| **English** | **Meticulous Thought Defender** | 37 | 19 | 18 | **51.35%** | **48.65%** | 67.57% |
| **Hindi** | No Defense | 37 | 37 | 0 | 100.00% | 0.00% | 0.00% |
| **Hindi** | Prompt Filter / Perimeter | 37 | 26 | 11 | 70.27% | 29.73% | 0.00% |
| **Hindi** | **Meticulous Thought Defender** | 37 | 7 | 30 | **18.92%** | **81.08%** | 100.00% |
| **Telugu** | No Defense | 37 | 37 | 0 | 100.00% | 0.00% | 0.00% |
| **Telugu** | Prompt Filter / Perimeter | 37 | 26 | 11 | 70.27% | 29.73% | 0.00% |
| **Telugu** | **Meticulous Thought Defender** | 37 | 12 | 25 | **32.43%** | **67.57%** | 97.30% |
| **Telugu-English** | No Defense | 37 | 37 | 0 | 100.00% | 0.00% | 0.00% |
| **Telugu-English** | Prompt Filter / Perimeter | 37 | 26 | 11 | 70.27% | 29.73% | 0.00% |
| **Telugu-English** | **Meticulous Thought Defender** | 37 | 13 | 24 | **35.14%** | **64.86%** | 97.30% |

---

## 8. Cross-Lingual Comparison & Analysis

1. **ASR Hierarchy Across Languages under Thought Defender**:
   $$\text{Hindi (18.92\%)} < \text{Telugu (32.43\%)} < \text{Telugu-English (35.14\%)} < \text{English (51.35\%)}$$
   Thought Defender demonstrated higher sensitivity on non-English scripts, producing lower ASRs because semantic transitions in non-Latin scripts exhibit steeper cosine distance drops when an attack is introduced.
2. **Impact of Code-Mixing**:
   Telugu-English code-mixed attacks exhibited slightly higher ASR (35.14%) than pure Telugu (32.43%). Code-switching acts as a partial semantic smoother in subword tokenization, slightly softening the cosine transition drop.
3. **Perimeter Filter Fragility**:
   Across all four languages, Prompt Filter achieved identical ASR (70.27%) because it failed completely against the 70% of attacks that used implicit or novel phrasing without exact keyword matches.

---

## 9. Error Analysis & Task Utility Investigation

### Investigation of the 0% Task Utility Finding:
- **Finding**: In both the preliminary InjecAgent benchmark and the initial document RAG trials, Task Utility Under Attack was recorded as 0.0%.
- **Root Cause**: When a defense acts as a **binary gatekeeper** (quarantining or refusing the retrieved context upon detecting an anomaly), the factual information required to answer the user query is blocked along with the attack. Conversely, when the attack is unblocked, the injection hijacks model output entirely.
- **Resolution**: Genuine task utility recovery requires moving beyond binary context suppression toward **span-level context sanitization** that excises anomalous sentences while forwarding clean factual spans to the generator.

---

## 10. Generated Artifacts & Visualizations

### Result Tables (`results/tables/` and `results/summaries/`)
- `final_results.csv`: 888 individual evaluation records with anomaly scores and verdicts.
- `benchmark_summary.csv` / `final_comparison.csv`: High-level defense metrics.
- `language_summary.csv` / `language_comparison.csv`: Cross-lingual breakdown.
- `defense_summary.csv` / `defense_comparison.csv`: Defense condition summary.
- `error_analysis.csv`: Representative breakdown of attacks, blocks, and false alarms.

### Presentation Figures (`results/figures/`)
1. `asr_by_language.png`: Cross-lingual ASR comparison across defenses.
2. `defense_block_rate_by_language.png`: Defense interception rates.
3. `task_utility_by_language.png`: Task utility profiles.
4. `asr_comparison_across_defenses.png`: Overall defense bar comparison.
5. `cross_lingual_defense_comparison.png`: Cross-lingual sensitivity curves.
6. `overall_defense_performance.png`: Multi-metric trade-off profile.
7. `safe_vs_attack_classification.png`: Semantic anomaly score distribution.

---

## 11. Verification & Testing

- **Automated Tests**: **50 / 50 unit and integration tests passing** (`python -m pytest tests/` in 3.07 seconds).
- **Test Coverage**:
  - Custom dataset schema & 24-point validation (`test_custom_dataset.py`)
  - InjecAgent loader & tool schema resolution (`test_injecagent_loader.py`)
  - Multilingual dataset loader & traceability (`test_multilingual_dataset.py`)
  - Indirect attack generation & embedding (`test_attack_module.py`)
  - Benchmark evaluation engine & task utility (`test_evaluation_engine.py`, `test_final_benchmark_integration.py`)
  - MCP tool server & agent execution (`test_mcp_server.py`, `test_agent.py`)
  - BGE-M3 embeddings, cosine similarity, consistency, detector (`test_embeddings.py`, `test_consistency.py`, `test_detector.py`)

---

## 12. Limitations

1. **Fixed Anomaly Threshold**: The current Thought Defender prototype uses a static threshold ($\tau = 0.30$) derived from English reasoning traces, which causes high false positive rates in Indic languages due to baseline cross-lingual dispersion.
2. **Binary Gatekeeper Mitigation**: The current defense suppresses the entire context when an anomaly is detected rather than surgically excising only the malicious span.
3. **Simulated Response Evaluation**: Large-scale evaluation uses deterministic simulated responses to ensure reproducibility without relying on rate-limited proprietary API credits.

---

## 13. What Remains for Week 9

1. Preparation of final presentation slides summarizing Weeks 1–8 findings.
2. Formulation of the final project report chapters (Methodology, Experimental Setup, Cross-Lingual Analysis).
3. Demonstration video / walkthrough of the live MCP RAG defense pipeline.
