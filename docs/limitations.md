# Project Limitations & Constraints

**Project**: Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents  

---

## 1. Architectural Limitations

### 1.1. The Binary Quarantine Utility Ceiling
Under current enterprise RAG security paradigms, defenses act as **binary gatekeepers**:
- When an injection is detected, the defense discards or quaranines the entire retrieved chunk, emitting an alert:
  `"[SECURITY ALERT]: Indirect prompt injection detected. The untrusted retrieved context has been quarantined."`
- Consequently, even though the attack is successfully neutralized (ASR = 0%), the LLM cannot access the legitimate factual data contained within the same retrieved chunk.
- **Empirical Impact**: Task Utility Under Attack is mathematically and practically **0.0%** for all successful blocks. Achieving non-zero utility under attack requires **fine-grained token-level span attribution and selective redacting**, which is outside the scope of binary perimeter/adapter defenses.

### 1.2. The Static Threshold Assumption
Meticulous Thought Defender operates with a single global anomaly threshold ($\tau = 0.30$).
- As proven by our threshold sensitivity analysis (`results/diagnostics/mtd_threshold_analysis.md`), multilingual dense embedding models like `BAAI/bge-m3` do not possess isotropic embedding spaces across scripts.
- English embeddings cluster more tightly than Telugu or Hindi embeddings.
- Imposing a single static threshold across all languages creates an intractable trade-off: either excessive False Negatives in English or excessive False Positives in Indic languages.

---

## 2. Computational & Runtime Constraints

### 2.1. CPU vs GPU Inference Latency in RAG Agents
- In production MCP RAG pipelines, sub-second latency is critical for agent tool invocation.
- Generating 1024-dimensional dense embeddings for multi-step reasoning traces using `BAAI/bge-m3` on multi-core CPU incurs an overhead of **~0.52 seconds per trace**.
- For multi-turn agent interactions with multiple MCP tool calls, embedding latency accumulates, requiring dedicated GPU acceleration or student-teacher distilled bi-encoders for real-time deployment.

### 2.2. Offline Environment & Model Caching
- To guarantee reproducibility and eliminate third-party API instability or rate-limiting, experiments were conducted using local model caches and offline HuggingFace flags (`HF_HUB_OFFLINE=1`).
- Embedding sequence length was constrained to `max_seq_length=256` to maintain computational feasibility on CPU architectures while capturing essential step semantics.

---

## 3. Threat Model & Data Constraints

### 3.1. Proxy Reasoning Trace Representation
- In closed-weight, API-accessible LLMs (e.g., GPT-4, Claude 3.5), intermediate hidden-state token activations and private scratchpads are inaccessible.
- Our implementation analyzes the **observable, structured Chain-of-Thought (CoT)** reasoning trace generated across agent workflow stages.
- While effective at capturing semantic discontinuities between retrieved contexts and tool invocations, this proxy representation may not detect adversarial sub-token manipulations occurring inside black-box attention heads.

### 3.2. Synthetic Benchmark Scope
- The 2,000-record dataset was systematically generated and validated across 5 enterprise domains (Healthcare, Finance, Legal, Tech, HR).
- While covering five primary attack categories and code-mixed vernacular, real-world attacks in enterprise environments may exhibit novel multimodal artifacts, homoglyph substitution attacks, or multi-step indirect injections distributed across multiple fragmented vector chunks.
