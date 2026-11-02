"""
Document Loader Module.
Discovers and loads text files from data/documents/, assigning unique document IDs
and preserving source file metadata.
"""
import os
from pathlib import Path
from typing import List, Dict, Any
import config

class Document:
    def __init__(self, doc_id: str, text: str, source: str, metadata: Dict[str, Any] = None):
        self.doc_id = doc_id
        self.text = text
        self.source = source
        self.metadata = metadata or {}
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            "doc_id": self.doc_id,
            "text": self.text,
            "source": self.source,
            "metadata": self.metadata
        }

class DocumentLoader:
    def __init__(self, documents_dir: Path = None):
        self.documents_dir = Path(documents_dir) if documents_dir else config.DOCUMENTS_DIR

    def load_documents(self) -> List[Document]:
        """
        Discovers all .txt files in documents_dir, reads their contents,
        and constructs Document objects.
        
        Returns:
            List[Document]: List of loaded document objects.
        """
        documents = []
        if not self.documents_dir.exists():
            print(f"[Warning] Documents directory not found: {self.documents_dir}")
            return documents

        file_paths = sorted(list(self.documents_dir.glob("*.txt")))
        
        for idx, file_path in enumerate(file_paths, start=1):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read().strip()
                
                doc_id = f"doc_{idx:03d}"
                source_name = file_path.name
                
                doc = Document(
                    doc_id=doc_id,
                    text=text,
                    source=source_name,
                    metadata={
                        "file_path": str(file_path),
                        "char_count": len(text),
                        "file_name": source_name
                    }
                )
                documents.append(doc)
            except Exception as e:
                print(f"[Error] Failed to load document '{file_path}': {e}")

        print(f"[Info] DocumentLoader successfully loaded {len(documents)} documents from {self.documents_dir}")
        return documents
