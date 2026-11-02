import pytest
import numpy as np
from src.embeddings import cosine_similarity, EmbeddingManager

def test_cosine_similarity_identical():
    v1 = np.array([1.0, 2.0, 3.0])
    v2 = np.array([1.0, 2.0, 3.0])
    sim = cosine_similarity(v1, v2)
    assert abs(sim - 1.0) < 1e-5

def test_cosine_similarity_orthogonal():
    v1 = np.array([1.0, 0.0])
    v2 = np.array([0.0, 1.0])
    sim = cosine_similarity(v1, v2)
    assert abs(sim - 0.0) < 1e-5

def test_embedding_manager_shape():
    em = EmbeddingManager()
    steps = ["Step one text.", "Step two text."]
    embeddings = em.embed_steps(steps)
    assert embeddings.shape[0] == 2
    assert embeddings.shape[1] > 0
