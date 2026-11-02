import pytest
import shutil
from pathlib import Path
from src.embeddings import EmbeddingManager
from src.rag.chunker import DocumentChunk
from src.rag.vector_store import VectorStoreManager

def test_vector_store_indexing_and_search(tmp_path):
    test_db_dir = tmp_path / "test_vector_db"
    em = EmbeddingManager(model_name="mock")
    vs = VectorStoreManager(embedding_manager=em, vector_db_dir=test_db_dir)
    
    chunks = [
        DocumentChunk("chunk_001", "doc_001", "Hyderabad is the capital of Telangana.", "hyderabad.txt", 0, 40),
        DocumentChunk("chunk_002", "doc_002", "Solar power converts sunlight to energy.", "solar.txt", 0, 40)
    ]
    vs.add_chunks(chunks)
    
    results = vs.search("Tell me about Hyderabad", top_k=1)
    assert len(results) == 1
    top_chunk, score = results[0]
    assert top_chunk.source == "hyderabad.txt"
    assert score > 0.0
