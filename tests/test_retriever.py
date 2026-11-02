import pytest
from src.rag.retriever import RAGRetriever

def test_rag_retriever():
    retriever = RAGRetriever()
    retriever.index_documents_if_needed()
    results = retriever.retrieve("What is Hyderabad?", top_k=2)
    assert len(results) == 2
    first_res = results[0]
    assert "chunk_id" in first_res
    assert "doc_id" in first_res
    assert "source" in first_res
    assert "score" in first_res
    assert "text" in first_res
