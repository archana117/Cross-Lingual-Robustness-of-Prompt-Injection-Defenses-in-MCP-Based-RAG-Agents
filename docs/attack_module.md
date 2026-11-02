# Indirect Prompt Injection Attack Module

**Project**: *Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents*  
**Module**: `src/attack/indirect_attack.py`

---

## 1. Overview

The Indirect Prompt Injection Attack module provides a reusable, programmatic framework for generating, formatting, and embedding prompt injections into retrieved knowledge documents.

In contrast to direct jailbreaks (where a malicious user submits an adversarial prompt directly to the LLM), indirect prompt injections occur when untrusted third-party content is ingested by the RAG retriever and processed by the agent.

---

## 2. Capabilities

1. **Attack Taxonomy Support**: Programmatically generates payloads across all 10 formal attack categories:
   - `instruction_override`
   - `ignore_previous_instruction`
   - `system_prompt_extraction`
   - `confidential_information_disclosure`
   - `task_redirection`
   - `fake_authority`
   - `context_manipulation`
   - `tool_use_manipulation`
   - `malicious_action`
   - `misleading_document_instruction`

2. **Multilingual Phrasing**:
   - `en`: Standard English imperative directives
   - `hi`: Fluent Devanagari Hindi directives
   - `te`: Fluent Telugu script directives
   - `teen`: Natural Telugu-English code-mixed phrases (e.g., using Telugu postpositions with English technical terms: *"User commands ni override చేసి..."*)

3. **Position Embedding Modes**:
   - `prefix`: Injection prepended before the factual text.
   - `middle`: Injection woven between legitimate domain sentences.
   - `suffix`: Injection appended after the factual text under administrative or system notices.

---

## 3. Programmatic Usage Example

```python
from src.attack.indirect_attack import IndirectAttackGenerator

generator = IndirectAttackGenerator()

# Generate an attack sample
sample = generator.create_attack_sample(
    scenario_id="S001",
    user_query="What is the prerequisite for CS101?",
    clean_document="Students must complete Math 100 before enrolling in CS101.",
    attack_type="instruction_override",
    language="teen",
    position="middle"
)

print(sample.injected_document)
```
