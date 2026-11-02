import pytest
from src.embeddings import EmbeddingManager

def test_embedding_manager_mock_backend():
    em = EmbeddingManager(model_name="mock")
    assert em.backend_name == "MOCK"
    vec = em.embed_text("Test query")
    assert vec.shape[0] == 384

def test_embedding_manager_default_backend():
    em = EmbeddingManager()
    assert em.backend_name in ["REAL_BGE_M3", "MOCK"]
