# Existing Benchmark Dataset: InjecAgent

This directory contains the original, pristine benchmark files from **InjecAgent**:
> **InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents**  
> *Reference:* Zhang et al., 2024.

---

## 1. Dataset Overview

- **Dataset Name**: InjecAgent Benchmark
- **Source**: Public research benchmark for tool-integrated Large Language Model agents.
- **Formats**: JSON (`.json`) and JSON Lines (`.jsonl`).
- **Original Language**: English (`en`).
- **Integrity**: Unmodified, preserved as external supplementary baseline.

---

## 2. File Inventory and Statistics

| File Name | Format | Record Count | Description |
| :--- | :--- | :--- | :--- |
| `user_cases.jsonl` | JSONL | 17 | Legitimate user tasks with tool invocation specifications and response templates |
| `attacker_cases_dh.jsonl` | JSONL | 30 | Direct Harm (DH) attack targets across Physical, Financial, and Data Security harms |
| `attacker_cases_ds.jsonl` | JSONL | 32 | Data Stealing (DS) multi-step exfiltration attacks across Physical, Financial, and Other data |
| `test_cases_dh_base.json` | JSON | 510 | Direct Harm base (unprompted) test cases (17 user cases × 30 attacker cases) |
| `test_cases_dh_enhanced.json` | JSON | 510 | Direct Harm enhanced (jailbreak-prefixed) test cases |
| `test_cases_ds_base.json` | JSON | 544 | Data Stealing base (unprompted) test cases (17 user cases × 32 attacker cases) |
| `test_cases_ds_enhanced.json` | JSON | 544 | Data Stealing enhanced (jailbreak-prefixed) test cases |
| `tools.json` | JSON | 38 toolkits (330 tools) | Full API function declarations and JSON schemas |
| `attacker_simulated_responses.json` | JSON | 2,347 entries | Precomputed simulated tool return values keyed by `(ToolName, {params})` |

**Total Test Cases**: $510 + 510 + 544 + 544 = \mathbf{2,108}$ evaluation cases.

---

## 3. How InjecAgent Differs from the Custom 2,000-Record Multilingual Dataset

| Dimension | InjecAgent Benchmark (`existing_dataset/`) | Custom Multilingual Dataset (`custom_dataset/`) |
| :--- | :--- | :--- |
| **Primary Paradigm** | Tool-integrated agent benchmark (Function calling) | RAG Agent Benchmark (Document retrieval + Grounded Q&A) |
| **Injection Source** | Mock external tool responses (API return payloads, emails, reviews) | Retrieved knowledge documents (unstructured text chunks) |
| **Languages** | English only (original benchmark) | English, Hindi, Telugu, and Telugu-English Code-Mixed (500 each) |
| **Total Samples** | 2,108 attack test cases | 2,000 balanced samples (1,000 SAFE, 1,000 ATTACK) |
| **Scenarios** | 17 user cases × 62 attacker profiles | 250 diverse domain scenarios (HR, academic, finance, healthcare, legal, etc.) |
| **Attack Taxonomy** | 2 major classes (DH, DS) split into 6 sub-types | 10 formal indirect injection categories (override, system extraction, fake authority, etc.) |
| **Splits** | Monolithic test sets | Scenario-isolated splits (Train: 70%, Val: 15%, Test: 15%) with zero leakage |
