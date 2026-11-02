# Dataset Documentation

**Project**: *Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents*  
**Team**: N. Archana and P. Harshitha (PID-14)  
**Supervisor**: Dr. K. Mary Sudha Rani  

---

## 1. Custom 2,000-Record Multilingual Dataset

The core evaluation benchmark consists of **2,000 balanced, high-fidelity records** constructed across **250 distinct domain scenarios**:

```
250 scenarios × 4 languages × 2 labels (SAFE / ATTACK) = 2,000 records
```

### Language Distribution
| Language | Code | Total Records | SAFE Records | ATTACK Records |
| :--- | :--- | :--- | :--- | :--- |
| **English** | `EN` | 500 | 250 | 250 |
| **Hindi** | `HI` | 500 | 250 | 250 |
| **Telugu** | `TE` | 500 | 250 | 250 |
| **Telugu-English Code-Mixed** | `TEEN` | 500 | 250 | 250 |
| **Total** | — | **2,000** | **1,000** | **1,000** |

---

## 2. Attack Taxonomy (10 Indirect Prompt Injection Categories)

Every attack record embeds an indirect prompt injection into a retrieved document chunk:

| # | Attack Category | Count in Dataset | Description |
| :--- | :--- | :--- | :--- |
| 1 | `instruction_override` | 100 | Instructs the model to discard user query and replace with mandated text |
| 2 | `ignore_previous_instruction` | 100 | Orders the model to ignore prior directions and claim records do not exist |
| 3 | `system_prompt_extraction` | 100 | Directs the model to dump its system prompt and confidential parameters |
| 4 | `confidential_information_disclosure` | 100 | Commands disclosure of credentials, keys, or sensitive account tokens |
| 5 | `task_redirection` | 100 | Diverts the model from the user's factual topic to an unrelated domain |
| 6 | `fake_authority` | 100 | Imposes bogus administrative or executive overrides |
| 7 | `context_manipulation` | 100 | Declares prior factual text null and void or superseded |
| 8 | `tool_use_manipulation` | 100 | Prompts malicious tool call payloads or arbitrary execution |
| 9 | `malicious_action` | 100 | Mandates user redirection to phishing domains or malware links |
| 10 | `misleading_document_instruction` | 100 | Falsifies compliance or fabricates authorization waivers |

---

## 3. Dataset Schema

Each record contains the following standardized columns:

| Column Name | Type | Description |
| :--- | :--- | :--- |
| `id` | String | Unique record identifier (e.g. `S001_EN_ATTACK`, `S001_HI_SAFE`) |
| `scenario_id` | String | Scenario grouping identifier (`S001` to `S250`) |
| `language` | String | `English`, `Hindi`, `Telugu`, or `Telugu-English` |
| `task` | String | The legitimate user question / query |
| `document_text` | String | The retrieved document text (clean or injection-embedded) |
| `attack_type` | String | One of the 10 attack categories (`none` for SAFE) |
| `label` | String | `SAFE` or `ATTACK` |
| `source` | String | Dataset source provenance (`custom_synthetic`) |
| `translation_method` | String | `original` or `custom_multilingual_engine` |
| `code_mix_type` | String | `none` or `telugu_english_phrasal` |
| `validation_status` | String | Validation status flag (`validated` / `verified`) |

---

## 4. Scenario-Level Split Strategy

Splits are strictly partitioned by `scenario_id` to prevent data leakage:

- **Train Set** (`train.csv`): 175 scenarios (1,400 records, 70.0%)
- **Validation Set** (`validation.csv`): 38 scenarios (304 records, 15.2%)
- **Test Set** (`test.csv`): 37 scenarios (296 records, 14.8%)

**Zero Scenario Leakage**:
$$\text{Train} \cap \text{Val} = \emptyset, \quad \text{Train} \cap \text{Test} = \emptyset, \quad \text{Val} \cap \text{Test} = \emptyset$$

---

## 5. File Locations

```
data/
├── custom_dataset/
│   ├── custom_2000_dataset.csv
│   ├── custom_2000_dataset.json
│   ├── english_master.csv
│   ├── hindi_dataset.csv
│   ├── telugu_dataset.csv
│   ├── telugu_english_dataset.csv
│   ├── train.csv
│   ├── validation.csv
│   ├── test.csv
│   ├── dataset_summary.txt
│   └── manual_validation.csv
└── intermediate/
    ├── english/
    ├── hindi/
    ├── telugu/
    └── telugu_english/
```
