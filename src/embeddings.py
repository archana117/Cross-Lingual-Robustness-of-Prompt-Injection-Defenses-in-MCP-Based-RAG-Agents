"""
BGE-M3 Embedding Module using SentenceTransformers.
Handles text and step embedding generation, vector normalization, and cosine similarity calculations.
Supports English and Unicode text (Telugu, Hindi, Code-mixed).
Includes deterministic Mock embedding fallback for 100% offline / fast testing.
"""
import os
import sys
import hashlib
import numpy as np
from typing import List, Union
import config

# Pre-set Windows PyTorch DLL environment flags and offline mode
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["OMP_NUM_THREADS"] = str(os.cpu_count() or 4)
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

_EMBEDDING_MODEL_CACHE = None

def load_embedding_model(model_name: str = None):
    """
    Loads and caches the SentenceTransformer model (defaults to BAAI/bge-m3).
    If model_name == "mock", returns None (uses mock embedding generation).
    """
    global _EMBEDDING_MODEL_CACHE
    target_model = model_name or config.BGE_MODEL_NAME
    
    if target_model.lower() == "mock":
        return "MOCK"
        
    if _EMBEDDING_MODEL_CACHE is None:
        try:
            # Force torch DLL initialization prior to SentenceTransformers
            import torch
            _ = torch.tensor([1.0])
            from sentence_transformers import SentenceTransformer
            print(f"[Info] Loading embedding model: {target_model}...")
            _EMBEDDING_MODEL_CACHE = SentenceTransformer(target_model)
            _EMBEDDING_MODEL_CACHE.max_seq_length = 256
            print("[Info] REAL BGE-M3 embedding model loaded successfully (max_seq_length=256).")
        except Exception as e:
            print(f"[Warning] Could not load SentenceTransformer '{target_model}' ({e}). Falling back to Mock Embeddings.")
            _EMBEDDING_MODEL_CACHE = "MOCK"
            
    return _EMBEDDING_MODEL_CACHE

def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Computes cosine similarity between two 1D vector arrays.
    
    Args:
        vec1 (np.ndarray): First embedding vector.
        vec2 (np.ndarray): Second embedding vector.
        
    Returns:
        float: Cosine similarity score bounded in [-1.0, 1.0].
    """
    v1 = np.asarray(vec1, dtype=np.float32).flatten()
    v2 = np.asarray(vec2, dtype=np.float32).flatten()
    
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    
    if norm1 == 0.0 or norm2 == 0.0:
        return 0.0
        
    sim = np.dot(v1, v2) / (norm1 * norm2)
    return float(np.clip(sim, -1.0, 1.0))

class EmbeddingManager:
    def __init__(self, model_name: str = None):
        self.model_name = model_name or config.BGE_MODEL_NAME
        self.model = load_embedding_model(self.model_name)
        self.dim = 1024 if self.model != "MOCK" else 384

    @property
    def backend_name(self) -> str:
        """Returns the active embedding backend name: REAL_BGE_M3 or MOCK."""
        return "REAL_BGE_M3" if self.model != "MOCK" else "MOCK"
        
    def _get_mock_embedding(self, text: str) -> np.ndarray:
        """
        Generates deterministic pseudo-semantic embeddings based on text content hash and key phrases.
        Used when running in offline/mock mode.
        """
        if not text:
            text = " "
            
        text_lower = text.lower()

        # Check for attack keywords (English, Hindi, Telugu, and Code-Mixed)
        if any(k in text_lower for k in [
            "ignore", "bypass", "confidential", "reveal", "sql", "leak", "pwned", "override", "shell",
            "अनदेखा", "गोपनीय", "रद्द", "निलंबित", "निर्देश:", "सिस्टम ओवरराइड", "आदेश",
            "విస్మరించండి", "రహస్య", "చెల్లదు", "నిలిపివేయబడింది", "సూచన:", "సిస్టమ్ ఓవర్‌రైడ్", "ఆదేశం",
            "ignore చేసి", "override చేసి", "secret token"
        ]):
            base_vec = np.ones(384, dtype=np.float32) * -0.6
        # Check for domain RAG query keywords
        elif "hyderabad" in text_lower or "telangana" in text_lower:
            base_vec = np.zeros(384, dtype=np.float32)
            base_vec[0:100] = 0.9
        elif "solar" in text_lower or "wind" in text_lower or "renewable" in text_lower:
            base_vec = np.zeros(384, dtype=np.float32)
            base_vec[100:200] = 0.9
        elif "index" in text_lower or "rdbms" in text_lower or "relational" in text_lower:
            base_vec = np.zeros(384, dtype=np.float32)
            base_vec[200:300] = 0.9
        elif "machine learning" in text_lower or "learning" in text_lower or "neural" in text_lower:
            base_vec = np.zeros(384, dtype=np.float32)
            base_vec[250:350] = 0.9
        elif "cloud" in text_lower or "iaas" in text_lower or "saas" in text_lower:
            base_vec = np.zeros(384, dtype=np.float32)
            base_vec[280:380] = 0.9
        else:
            base_vec = np.ones(384, dtype=np.float32) * 0.75

        # Add deterministic perturbation from sha256 of text
        hash_digest = hashlib.sha256(text.encode("utf-8")).digest()
        seed = int.from_bytes(hash_digest[:4], "big")
        rng = np.random.RandomState(seed)
        noise = rng.normal(0, 0.02, size=384).astype(np.float32)
        
        vec = base_vec + noise
        norm = np.linalg.norm(vec)
        return vec / norm if norm > 0 else vec

    def embed_text(self, text: str) -> np.ndarray:
        """
        Embeds a single string into a 1D numpy array.
        """
        if self.model == "MOCK":
            return self._get_mock_embedding(text)
            
        if not text:
            text = " "
        embedding = self.model.encode(text, convert_to_numpy=True, normalize_embeddings=True)
        return embedding
        
    def embed_steps(self, steps: List[str]) -> np.ndarray:
        """
        Embeds a list of reasoning step strings into a 2D numpy array of shape (N, d).
        """
        if not steps:
            return np.zeros((0, self.dim), dtype=np.float32)
            
        if self.model == "MOCK":
            return np.array([self._get_mock_embedding(s) for s in steps], dtype=np.float32)
            
        embeddings = self.model.encode(steps, convert_to_numpy=True, normalize_embeddings=True)
        return embeddings
