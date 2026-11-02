import os

# Default to mock models for fast, deterministic, offline test execution
os.environ.setdefault("BGE_MODEL_NAME", "mock")
os.environ.setdefault("LLM_PROVIDER", "mock")
