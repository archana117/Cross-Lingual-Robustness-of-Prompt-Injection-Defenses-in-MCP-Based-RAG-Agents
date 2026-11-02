"""
Vector Store Module.
Manages vector storage, indexing, and similarity search for document chunks.
Integrates with ChromaDB and provides a lightweight local fallback if needed.
Reuses existing EmbeddingManager from src/embeddings.py.
"""
import os
import json
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Tuple
import config
from src.embeddings import EmbeddingManager, cosine_similarity
from src.rag.chunker import DocumentChunk

class LocalVectorStore:
    """
    Lightweight, in-memory/file-backed vector store fallback.
    Computes cosine similarity over indexed chunk embeddings.
    """
    def __init__(self, storage_dir: Path):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.chunks: List[DocumentChunk] = []
        self.embeddings: List[np.ndarray] = []

    def add_chunks(self, chunks: List[DocumentChunk], embeddings: np.ndarray):
        self.chunks = chunks
        self.embeddings = [vec for vec in embeddings]

    def search(self, query_vec: np.ndarray, top_k: int = 3) -> List[Tuple[DocumentChunk, float]]:
        if not self.chunks or len(self.embeddings) == 0:
            return []

        results = []
        for chunk, vec in zip(self.chunks, self.embeddings):
            sim = cosine_similarity(query_vec, vec)
            results.append((chunk, float(sim)))

        # Sort descending by similarity score
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_k]

class VectorStoreManager:
    def __init__(self, embedding_manager: EmbeddingManager = None, vector_db_dir: Path = None):
        self.embedding_manager = embedding_manager or EmbeddingManager()
        self.vector_db_dir = Path(vector_db_dir) if vector_db_dir else config.VECTOR_DB_DIR
        self.vector_db_dir.mkdir(parents=True, exist_ok=True)
        
        self.chroma_client = None
        self.collection = None
        self.local_fallback = LocalVectorStore(self.vector_db_dir)
        self.use_chroma = False

        self._init_store()

    def _init_store(self):
        try:
            import chromadb
            client_path = str(self.vector_db_dir / "chroma_db")
            self.chroma_client = chromadb.PersistentClient(path=client_path)
            # Create collection specific to embedding dimension to prevent dimension mismatch warnings
            collection_name = f"rag_docs_{self.embedding_manager.dim}"
            self.collection = self.chroma_client.get_or_create_collection(name=collection_name)
            self.use_chroma = True
            print(f"[Info] Initialized ChromaDB collection '{collection_name}' at {client_path}")
        except Exception as e:
            print(f"[Warning] Could not initialize ChromaDB ({e}). Using Local Vector Store.")
            self.use_chroma = False

    def add_chunks(self, chunks: List[DocumentChunk]):
        """
        Embeds document chunks using EmbeddingManager and indexes them into the vector store.
        """
        if not chunks:
            return

        chunk_texts = [c.text for c in chunks]
        print(f"[Info] Generating embeddings for {len(chunks)} chunks using {self.embedding_manager.backend_name}...")
        embeddings = self.embedding_manager.embed_steps(chunk_texts)

        # Always update local fallback
        self.local_fallback.add_chunks(chunks, embeddings)

        if self.use_chroma and self.collection is not None:
            try:
                ids = [c.chunk_id for c in chunks]
                metadatas = [
                    {
                        "doc_id": c.doc_id,
                        "source": c.source,
                        "start_char": c.start_char,
                        "end_char": c.end_char
                    }
                    for c in chunks
                ]
                embeddings_list = [vec.tolist() for vec in embeddings]
                
                # Upsert into ChromaDB
                self.collection.upsert(
                    ids=ids,
                    documents=chunk_texts,
                    embeddings=embeddings_list,
                    metadatas=metadatas
                )
                print(f"[Info] Upserted {len(chunks)} chunks into ChromaDB ({self.collection.name}).")
            except Exception as e:
                print(f"[Warning] ChromaDB upsert failed ({e}). Defaulting to Local Vector Store.")
                self.use_chroma = False

    def search(self, query: str, top_k: int = 3) -> List[Tuple[DocumentChunk, float]]:
        """
        Embeds a user query and searches the vector store for top_k relevant chunks.
        
        Returns:
            List[Tuple[DocumentChunk, float]]: List of (chunk, similarity_score) tuples.
        """
        query_vec = self.embedding_manager.embed_text(query)

        if self.use_chroma and self.collection is not None and self.collection.count() > 0:
            try:
                query_vec_list = query_vec.tolist()
                results = self.collection.query(
                    query_embeddings=[query_vec_list],
                    n_results=top_k,
                    include=["documents", "metadatas", "distances"]
                )

                chunk_results = []
                if results and results["ids"] and len(results["ids"][0]) > 0:
                    for idx in range(len(results["ids"][0])):
                        chunk_id = results["ids"][0][idx]
                        text = results["documents"][0][idx]
                        meta = results["metadatas"][0][idx]
                        # Cosine distance conversion: similarity = 1.0 - distance
                        dist = results["distances"][0][idx] if "distances" in results and results["distances"] else 0.0
                        similarity = float(1.0 - dist) if dist <= 1.0 else float(1.0 / (1.0 + dist))

                        chunk = DocumentChunk(
                            chunk_id=chunk_id,
                            doc_id=meta.get("doc_id", "unknown"),
                            text=text,
                            source=meta.get("source", "unknown"),
                            start_char=meta.get("start_char", 0),
                            end_char=meta.get("end_char", len(text)),
                            metadata=meta
                        )
                        chunk_results.append((chunk, similarity))
                    return chunk_results
            except Exception as e:
                print(f"[Warning] ChromaDB query failed ({e}). Falling back to Local Vector Store.")

        # Fallback to local vector search
        return self.local_fallback.search(query_vec, top_k=top_k)
