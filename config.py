import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file if available
load_dotenv()

# Base directories
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DOCUMENTS_DIR = DATA_DIR / "documents"
RESULTS_DIR = BASE_DIR / "results"
FIGURES_DIR = RESULTS_DIR / "figures"
VECTOR_DB_DIR = BASE_DIR / "vector_store_data"

# InjecAgent Benchmark Directory
INJECAGENT_DIR = DATA_DIR / "existing_dataset" / "InjecAgent"
if not INJECAGENT_DIR.exists():
    alt_injecagent = BASE_DIR / "existing_dataset" / "InjecAgent"
    if alt_injecagent.exists():
        INJECAGENT_DIR = alt_injecagent

# Custom Multilingual Dataset Directory
CUSTOM_MULTILINGUAL_DIR = DATA_DIR / "custom_dataset" / "multilingual"
if not (DATA_DIR / "custom_dataset").exists() and (BASE_DIR / "custom_dataset").exists():
    CUSTOM_MULTILINGUAL_DIR = BASE_DIR / "custom_dataset" / "multilingual"
CUSTOM_MULTILINGUAL_DIR.mkdir(parents=True, exist_ok=True)

# Ensure output directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
FIGURES_DIR.mkdir(parents=True, exist_ok=True)
VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)

# LLM Configurations
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")
LLM_MODEL = os.getenv("LLM_MODEL", "qwen2.5:7b")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.0"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "512"))

# Embedding Configurations
BGE_MODEL_NAME = os.getenv("BGE_MODEL_NAME", "BAAI/bge-m3")

# Detection Configurations (Week 2 Prototype)
ANOMALY_THRESHOLD = float(os.getenv("ANOMALY_THRESHOLD", "0.30"))

# RAG Configurations (Week 3 Baseline)
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "500"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "50"))
TOP_K = int(os.getenv("TOP_K", "3"))

# MCP Configurations (Week 3 Baseline)
MCP_SERVER_NAME = os.getenv("MCP_SERVER_NAME", "rag-mcp-server")
MCP_PORT = int(os.getenv("MCP_PORT", "8000"))

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
HF_TOKEN = os.getenv("HF_TOKEN", "")
