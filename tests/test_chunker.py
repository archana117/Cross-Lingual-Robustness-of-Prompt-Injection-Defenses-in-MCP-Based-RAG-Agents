import pytest
from src.rag.document_loader import Document
from src.rag.chunker import DocumentChunker, DocumentChunk

def test_document_chunker():
    doc = Document(
        doc_id="doc_001",
        text="A " * 300,  # 600 characters
        source="test.txt",
        metadata={"file_name": "test.txt"}
    )
    chunker = DocumentChunker(chunk_size=200, chunk_overlap=50)
    chunks = chunker.chunk_document(doc)
    assert len(chunks) >= 3
    first_chunk = chunks[0]
    assert isinstance(first_chunk, DocumentChunk)
    assert first_chunk.doc_id == "doc_001"
    assert first_chunk.source == "test.txt"
    assert len(first_chunk.text) <= 200
