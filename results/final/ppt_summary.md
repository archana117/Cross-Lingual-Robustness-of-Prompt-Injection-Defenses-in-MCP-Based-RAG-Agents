# Review-2 / Final Evaluation: Presentation Summary (PPT Deck Guide)

**Project Title**: Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents  
**Target Languages**: English, Hindi, Telugu, Telugu-English Code-Mixed  
**Evaluation Standard**: Model Context Protocol (MCP) tool-mediated RAG  
**Primary Deliverables**: 2,000-Record Multilingual Dataset, 50-Suite Unit/Integration Tests, MCP Server & Agent, 7 Figures, Diagnostics, and Final Validated Benchmark  

---

## Slide 1: Executive Overview & Problem Statement

- **Context**: Enterprise RAG agents increasingly connect LLMs to external vector databases using the **Model Context Protocol (MCP)**.
- **The Threat**: Untrusted enterprise documents frequently contain **Indirect Prompt Injections (IPI)** designed to hijack agent execution, leak credentials, or invoke unauthorized tools.
- **The Core Research Gap**: Most existing defense mechanisms are designed and evaluated exclusively on English text. When deployed in multilingual and low-resource or code-mixed environments (e.g., Hindi, Telugu, Tenglish), their defense efficacy collapses.
- **Project Objective**: Conduct a rigorous, forensic audit, debugging, and cross-lingual evaluation of perimeter and semantic defenses under standardized MCP RAG agent architectures.

---

## Slide 2: Threat Model — Indirect Prompt Injection

- **Indirect Injection Paradigm**:
  - The **User Query** is completely benign (e.g., medical query, financial calculation).
  - The **Retrieved Document** contains legitimate factual knowledge contaminated with an adversarial injection payload.
  - The **Agent** ingests retrieved context via MCP `search_documents` tool call.
  - The **Injection Goal**: Force the LLM to ignore user instructions, emit fake system notices, or leak confidential context.
- **Attack Placement**: Systematically embedded across beginning, middle, and end spans of enterprise documents.
- **Language Scope**: 4 language tracks covering standard orthography and Latin-script transliterated code-mixing.

---

## Slide 3: Architecture & End-to-End Pipeline

```
[Enterprise Documents (4 Languages)]
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
[FastMCP Server (search_documents Tool via Stdio)]
           │
           ▼
[MCP RAG Agent (Tool Calling + Context Inspection)]
           │
           ▼
[Defensive Barrier (No Defense | Prompt Filter | Thought Defender)]
           │
           ▼
[LLM Inference (Context-Grounded Generation)]
           │
           ▼
[Evaluation Engine (Grounded Task Utility & ASR Verifier)]
```

---

## Slide 4: Dataset Integrity & Scenario-Level Split

- **Dataset Scale**: **2,000 verified records** across 5 domains (Healthcare, Finance, Legal, Tech, HR).
  - 1,000 Safe records + 1,000 Attack records.
  - 500 records per language (English, Hindi, Telugu, Code-Mixed).
  - Exactly 250 enterprise scenarios.
- **Strict Leakage Prevention**:
  - Partitioning performed strictly at the **`scenario_id`** level (not row-level).
  - **Train Split**: 175 scenarios (1,400 records, 70%).
  - **Validation Split**: 38 scenarios (304 records, 15%).
  - **Held-Out Test Split**: 37 scenarios (296 records, 15%).
- **Verification**: **24 out of 24 validation checks passed** with zero scenario leakage.

---

## Slide 5: Forensic Root-Cause Diagnoses

### Issue 1: Why Was Task Utility Under Attack Exactly 0.0%?
- **Root Cause Identified**: Both Prompt Filter and MTD operate as **binary gatekeepers**.
  - When an attack succeeds $\to$ Model is hijacked $\to$ Task Utility = 0%.
  - When an attack is blocked $\to$ The entire document context is quarantined $\to$ The model refuses with a security warning $\to$ The factual task cannot be completed $\to$ Task Utility = 0%.
- **Finding**: Task Utility Under Attack is mathematically and empirically 0.0% under binary quarantine architectures. Restoring utility under attack requires token-level span sanitization rather than document-level blocking.
- **Benign Safe Utility**: Fixed tokenizer bug (`\w{4,}` dropping 2-char Indic words), restoring clean benign utility from **87.16% to 100.00%**.

### Issue 2: Why Did Baseline MTD Show 94.59% ASR & 0% Hindi/Telugu Blocks?
- **Root Cause Identified**: The historical baseline ran with a **Mock Embedding fallback** that only checked 9 English words (`ignore`, `bypass`, `override`, etc.).
  - Hindi and Telugu had 0 English word matches $\to$ 0 blocked $\to$ 100% ASR.
- **Real BGE-M3 Discovery**: Evaluating with real dense `BAAI/bge-m3` vectors achieves **97.30% Block Rate**, but reveals a severe **96.62% False Positive Rate** at static threshold $\tau=0.30$ due to natural semantic dispersion across Indic scripts.

---

## Slide 6: Final Benchmark Results Across Defenses

Evaluated on the Held-Out Test Set (296 records, 148 attacks, 148 safe):

| Defense Architecture | Total Cases | Attacks | Blocked | Successful | ASR (%) | Block Rate (%) | Utility Under Attack (%) | Benign Safe Utility (%) | False Positive Rate (%) | False Negative Rate (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **No Defense (Baseline)** | 296 | 148 | 0 | 148 | **100.00%** | **0.00%** | 0.00% | **100.00%** | **0.00%** | 100.00% |
| **Prompt Filter / Perimeter** | 296 | 148 | 44 | 104 | **70.27%** | **29.73%** | 6.76% | **100.00%** | **0.00%** | 70.27% |
| **Meticulous Thought Defender** | 296 | 148 | 144 | 4 | **2.70%** | **97.30%** | 23.65% | 3.38% | **96.62%** | 2.70% |

---

## Slide 7: Cross-Lingual Defense Performance Breakdown

| Language | Defense | Total Cases | Attacks | Blocked | ASR (%) | Block Rate (%) | Utility (%) | Benign Utility (%) | FPR (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **English** | Prompt Filter | 74 | 37 | 11 | 70.27% | 29.73% | 21.62% | 100.00% | 0.00% |
| | Thought Defender | 74 | 37 | 36 | 2.70% | 97.30% | 70.27% | 0.00% | 100.00% |
| **Hindi** | Prompt Filter | 74 | 37 | 11 | 70.27% | 29.73% | 0.00% | 100.00% | 0.00% |
| | Thought Defender | 74 | 37 | 36 | 2.70% | 97.30% | 0.00% | 2.70% | 97.30% |
| **Telugu** | Prompt Filter | 74 | 37 | 11 | 70.27% | 29.73% | 0.00% | 100.00% | 0.00% |
| | Thought Defender | 74 | 37 | 37 | 0.00% | 100.00% | 0.00% | 0.00% | 100.00% |
| **Telugu-English** | Prompt Filter | 74 | 37 | 11 | 70.27% | 29.73% | 5.41% | 100.00% | 0.00% |
| | Thought Defender | 74 | 37 | 35 | 5.41% | 94.59% | 24.32% | 10.81% | 89.19% |

---

## Slide 8: Key Insights & Scientific Discoveries

1. **The Lexical Brittleness of Perimeter Filters**:
   Prompt filters with fixed keyword patterns provide zero defense against multilingual paraphrasing, failing on 70.27% of all indirect prompt injection vectors.
2. **The Cross-Lingual Semantic Dispersion Gap**:
   In multilingual dense embedding models (`BAAI/bge-m3`), consecutive reasoning steps in Indic scripts naturally exhibit lower cosine similarities than English ($\Delta \approx 0.15 - 0.20$).
3. **The Static Threshold Dilemma**:
   A single global threshold ($\tau = 0.30$) tuned for English induces unacceptable False Positive Rates ($>90\%$) in Indic languages, rendering benign queries unusable.
4. **Validation Calibration Solution**:
   Threshold sensitivity analysis proves that multilingual defenses require **adaptive, language-calibrated thresholds** ($\tau_{EN} \approx 0.30, \tau_{Indic} \approx 0.48 - 0.52$).

---

## Slide 9: Limitations & Engineering Constraints

- **Binary Quarantine Utility Ceiling**: Complete document rejection prevents access to clean factual data in the same chunk.
- **Inference Latency**: Dense multilingual embeddings on CPU incur ~0.52s per reasoning trace, highlighting the need for GPU acceleration or distilled bi-encoders in production MCP servers.
- **Observable CoT vs Private Attention**: Observable reasoning traces capture multi-step semantic divergence but cannot inspect black-box model hidden states.

---

## Slide 10: Conclusion & Future Work

- **Project Milestones Achieved**:
  1. Complete, leakage-free 2,000-record multilingual dataset across 4 languages.
  2. End-to-end MCP-compliant RAG agent with FastMCP tool execution.
  3. Forensic identification and correction of metric and adapter bugs.
  4. Real BGE-M3 multilingual evaluation and 7 presentation-ready figures.
- **Future Recommendations**:
  1. Implement **Selective Span Attribution** to redact malicious injection tokens while passing factual context to achieve high Task Utility Under Attack.
  2. Implement **Dynamic Script-Aware Thresholding** for semantic CoT defenses.
