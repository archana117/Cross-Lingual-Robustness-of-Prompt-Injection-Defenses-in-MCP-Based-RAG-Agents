import sys
import os
import json
from typing import List, Dict, Any, Optional

# Ensure project root is in sys.path when executed directly as standalone process
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    class FastMCP:
        def __init__(self, name: str):
            self.name = name
            self._tool_manager = self
            self._tools = {}
        def tool(self):
            def decorator(func):
                self._tools[func.__name__] = func
                return func
            return decorator
        async def call_tool(self, name, args):
            if name in self._tools:
                return [self._tools[name](**args)]
            return []
        def run(self):
            pass

import config
from src.rag.retriever import RAGRetriever


# Global RAG Retriever instance
_RETRIEVER_INSTANCE: Optional[RAGRetriever] = None

def get_retriever() -> RAGRetriever:
    global _RETRIEVER_INSTANCE
    if _RETRIEVER_INSTANCE is None:
        _RETRIEVER_INSTANCE = RAGRetriever()
        _RETRIEVER_INSTANCE.index_documents_if_needed()
    return _RETRIEVER_INSTANCE

# Initialize FastMCP Server
mcp_server = FastMCP(config.MCP_SERVER_NAME)

@mcp_server.tool()
def search_documents(query: str, top_k: int = 3) -> str:
    """
    Search indexed knowledge base documents for relevant factual information.
    
    Args:
        query (str): The search query or question.
        top_k (int): Number of relevant document chunks to return (default: 3).
        
    Returns:
        str: JSON formatted string containing retrieved chunks, source metadata, and similarity scores.
    """
    retriever = get_retriever()
    results = retriever.retrieve(query, top_k=top_k)
    return json.dumps(results, indent=2, ensure_ascii=False)

def execute_mcp_tool_direct(tool_name: str, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Direct in-process invocation of MCP tool for agent testing and local CLI demonstration.
    """
    if tool_name == "search_documents":
        query = arguments.get("query", "")
        top_k = arguments.get("top_k", config.TOP_K)
        retriever = get_retriever()
        return retriever.retrieve(query, top_k=top_k)
    else:
        raise ValueError(f"Unknown MCP tool: {tool_name}")

if __name__ == "__main__":
    # Standard MCP server stdio transport runner
    mcp_server.run()

