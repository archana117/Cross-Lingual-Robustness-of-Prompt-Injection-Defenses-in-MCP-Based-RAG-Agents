"""
RAG Retriever Module.
Executes semantic retrieval for user queries against the VectorStoreManager.
Returns structured chunk records with similarity scores and metadata.
"""
from typing import List, Dict, Any, Optional
import config
from src.rag.document_loader import DocumentLoader
from src.rag.chunker import DocumentChunker
from src.rag.vector_store import VectorStoreManager

class RAGRetriever:
    def __init__(self, vector_store: Optional[VectorStoreManager] = None):
        self.vector_store = vector_store or VectorStoreManager()
        self.is_indexed = False

    def index_documents_if_needed(self, force_reindex: bool = False):
        """
        Loads documents, chunks them, and indexes them into the vector store.
        """
        if self.is_indexed and not force_reindex:
            return

        loader = DocumentLoader()
        documents = loader.load_documents()

        chunker = DocumentChunker()
        chunks = chunker.chunk_documents(documents)

        self.vector_store.add_chunks(chunks)
        self.is_indexed = True

    def retrieve(self, query: str, top_k: int = None) -> List[Dict[str, Any]]:
        """
        Retrieves top_k relevant document chunks for a query string.
        
        Args:
            query (str): User question.
            top_k (int): Number of chunks to retrieve.
            
        Returns:
            List[Dict[str, Any]]: List of dictionary retrieval records.
        """
        if not self.is_indexed:
            self.index_documents_if_needed()

        k = top_k if top_k is not None else config.TOP_K
        results = self.vector_store.search(query, top_k=k)

        formatted_results = []
        for chunk, score in results:
            formatted_results.append({
                "chunk_id": chunk.chunk_id,
                "doc_id": chunk.doc_id,
                "source": chunk.source,
                "text": chunk.text,
                "score": float(score),
                "metadata": chunk.metadata
            })

        return formatted_results
