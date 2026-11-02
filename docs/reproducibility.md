# Reproducibility Guide

**Project**: Cross-Lingual Robustness of Prompt-Injection Defenses in MCP-Based RAG Agents  
**Environment**: Python 3.12.6, Windows / Linux / macOS  
**Dependencies**: `sentence-transformers`, `chromadb`, `mcp`, `pandas`, `numpy`, `matplotlib`, `pytest`  

---

## 1. System Requirements

- **Operating System**: Windows 10/11, Ubuntu 20.04+, or macOS 12+
- **CPU**: Minimum 4 physical cores (recommended: 8 cores)
- **RAM**: Minimum 8 GB (recommended: 16 GB)
- **Disk Space**: ~3.5 GB for local `BAAI/bge-m3` model cache and ChromaDB vector store
- **GPU**: Optional (CPU inference fully supported and optimized)

---

## 2. Environment Setup

Activate the local project virtual environment:

```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Linux / macOS
source venv/bin/activate
```

Verify that required dependencies are installed:

```powershell
pip install -r requirements.txt
```

Set UTF-8 encoding environment variable (critical for Windows console Indic script display):

```powershell
$env:PYTHONIOENCODING="utf-8"
```

---

## 3. Step-by-Step Reproduction Pipeline

### Step 1: Validate Dataset Integrity & Leakage Prevention
Verify that all 2,000 records, 250 scenarios, and train/val/test splits pass the 24-point validation audit:

```powershell
python scripts/validate_custom_dataset.py
```
*Expected Output*: `24/24 checks passed. 0 scenario leakage.`

### Step 2: Run Automated Test Suite
Execute the unit and integration tests across all modules:

```powershell
pytest tests/ -v
```
*Expected Output*: `50 passed in ~3-7 seconds.`

### Step 3: Verify End-to-End MCP Integration
Verify that the FastMCP server, stdio JSON-RPC transport, and RAG agent operate correctly:

```powershell
python scripts/verify_mcp_e2e.py
```
*Expected Output*: `MCP Server E2E Verification PASSED.`

### Step 4: Run the Complete Final Benchmark
Execute the master benchmark across all 4 languages, 3 defenses, and 296 test records:

```powershell
python scripts/run_final_benchmark.py
```
*Output Artifacts Produced*:
- `results/final/final_benchmark_results_<timestamp>.csv`
- `results/final/final_defense_summary_<timestamp>.csv`
- `results/final/final_language_summary_<timestamp>.csv`
- `results/final/final_error_analysis_<timestamp>.csv`
- `results/raw/final_results.csv`
- `results/summaries/defense_summary.csv`
- `results/summaries/language_summary.csv`
- `results/tables/final_comparison.csv`
- `results/figures/*.png` (7 figures)

### Step 5: Regenerate Benchmark Figures Separately (Optional)
If you wish to update or re-render figures directly from existing evaluation CSVs:

```powershell
python -c "
import pandas as pd
from src.evaluation.visualizer import generate_benchmark_figures
df_raw = pd.read_csv('results/raw/final_results.csv')
df_lang = pd.read_csv('results/summaries/language_summary.csv')
df_defense = pd.read_csv('results/summaries/defense_summary.csv')
generate_benchmark_figures(df_raw, df_lang, df_defense)
"
```

---

## 4. Determinism & Offline Safety

1. **No External API Dependencies**:
   All benchmark evaluations run locally without requiring paid OpenAI or HuggingFace API tokens.
2. **Local HuggingFace Cache**:
   The embedding manager utilizes pre-cached weights for `BAAI/bge-m3` located in the user `.cache/huggingface/hub/` directory, reinforced by `HF_HUB_OFFLINE=1`.
3. **Reproducible Splits**:
   Scenario partitioning uses a deterministic scenario hash seed, guaranteeing identical test sample selection across runs.
