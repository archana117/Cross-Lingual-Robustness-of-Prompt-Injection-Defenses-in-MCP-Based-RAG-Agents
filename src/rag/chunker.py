"""
Document Chunker Module.
Splits documents into overlapping chunks while preserving document IDs and source metadata.
"""
from typing import List, Dict, Any
import config
from src.rag.document_loader import Document

class DocumentChunk:
    def __init__(self, chunk_id: str, doc_id: str, text: str, source: str, start_char: int, end_char: int, metadata: Dict[str, Any] = None):
        self.chunk_id = chunk_id
        self.doc_id = doc_id
        self.text = text
        self.source = source
        self.start_char = start_char
        self.end_char = end_char
        self.metadata = metadata or {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "chunk_id": self.chunk_id,
            "doc_id": self.doc_id,
            "text": self.text,
            "source": self.source,
            "start_char": self.start_char,
            "end_char": self.end_char,
            "metadata": self.metadata
        }

class DocumentChunker:
    def __init__(self, chunk_size: int = None, chunk_overlap: int = None):
        self.chunk_size = chunk_size if chunk_size is not None else config.CHUNK_SIZE
        self.chunk_overlap = chunk_overlap if chunk_overlap is not None else config.CHUNK_OVERLAP

    def chunk_document(self, document: Document) -> List[DocumentChunk]:
        """
        Splits a single Document into a list of DocumentChunk objects.
        """
        text = document.text
        doc_len = len(text)
        chunks = []

        if not text:
            return chunks

        if doc_len <= self.chunk_size:
            chunk_id = f"{document.doc_id}_c001"
            chunk = DocumentChunk(
                chunk_id=chunk_id,
                doc_id=document.doc_id,
                text=text,
                source=document.source,
                start_char=0,
                end_char=doc_len,
                metadata=dict(document.metadata)
            )
            return [chunk]

        step = self.chunk_size - self.chunk_overlap
        chunk_idx = 1

        for start in range(0, doc_len, step):
            end = min(start + self.chunk_size, doc_len)
            chunk_text = text[start:end].strip()

            if chunk_text:
                chunk_id = f"{document.doc_id}_c{chunk_idx:03d}"
                meta = dict(document.metadata)
                meta["chunk_index"] = chunk_idx

                chunk = DocumentChunk(
                    chunk_id=chunk_id,
                    doc_id=document.doc_id,
                    text=chunk_text,
                    source=document.source,
                    start_char=start,
                    end_char=end,
                    metadata=meta
                )
                chunks.append(chunk)
                chunk_idx += 1

            if end >= doc_len:
                break

        return chunks

    def chunk_documents(self, documents: List[Document]) -> List[DocumentChunk]:
        """
        Splits a list of Document objects into a list of DocumentChunk objects.
        """
        all_chunks = []
        for doc in documents:
            doc_chunks = self.chunk_document(doc)
            all_chunks.extend(doc_chunks)

        print(f"[Info] DocumentChunker produced {len(all_chunks)} chunks from {len(documents)} documents.")
        return all_chunks
