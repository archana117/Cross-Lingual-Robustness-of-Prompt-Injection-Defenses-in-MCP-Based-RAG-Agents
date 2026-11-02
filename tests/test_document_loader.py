import pytest
from pathlib import Path
from src.rag.document_loader import DocumentLoader, Document

def test_document_loader():
    loader = DocumentLoader()
    docs = loader.load_documents()
    assert len(docs) >= 5
    first_doc = docs[0]
    assert isinstance(first_doc, Document)
    assert first_doc.doc_id.startswith("doc_")
    assert first_doc.source.endswith(".txt")
    assert len(first_doc.text) > 0
