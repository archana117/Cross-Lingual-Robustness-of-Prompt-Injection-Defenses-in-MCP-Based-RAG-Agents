import pytest
import json
from src.mcp.server import execute_mcp_tool_direct, mcp_server

def test_mcp_search_documents_tool():
    results = execute_mcp_tool_direct("search_documents", {"query": "What is machine learning?", "top_k": 2})
    assert isinstance(results, list)
    assert len(results) == 2
    assert "source" in results[0]
    assert "score" in results[0]

def test_mcp_server_initialization():
    assert mcp_server.name == "rag-mcp-server"
