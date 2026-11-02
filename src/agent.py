import json
import uuid
import asyncio
import datetime
from typing import Dict, Any, List, Optional
import config
from src.llm import LLMProvider
from src.mcp.server import mcp_server, execute_mcp_tool_direct
from src.rag.retriever import RAGRetriever

from src.defenses.base import BaseDefense
from src.defenses.no_defense import NoDefense

def execute_mcp_tool(tool_name: str, arguments: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Executes an MCP tool via the FastMCP tool manager registry.
    Falls back to direct in-process retriever if needed.
    """
    try:
        # Execute tool via FastMCP Tool Manager API
        res = asyncio.run(mcp_server._tool_manager.call_tool(tool_name, arguments))
        if res and len(res) > 0:
            item = res[0]
            text_content = item if isinstance(item, str) else getattr(item, "text", str(item))
            return json.loads(text_content)
    except Exception as e:
        # Fallback to direct call if event loop issues occur
        pass
    return execute_mcp_tool_direct(tool_name, arguments)


class MCPAgent:
    def __init__(
        self,
        llm_provider: Optional[LLMProvider] = None,
        retriever: Optional[RAGRetriever] = None,
        defense: Optional[BaseDefense] = None
    ):
        self.llm_provider = llm_provider or LLMProvider()
        self.retriever = retriever or RAGRetriever()
        self.defense = defense or NoDefense()
        
    def answer_question(
        self,
        query: str,
        top_k: int = None,
        retrieved_chunks: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        Orchestrates full MCP RAG pipeline for a given user question.
        
        Flow: User -> MCP Agent -> MCP Server (search_documents) -> Vector DB -> Retrieved Context -> LLM -> Answer.
        If retrieved_chunks is explicitly provided (e.g. during benchmark evaluation), it uses those chunks directly.
        """
        request_id = f"req_{uuid.uuid4().hex[:8]}"
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        k = top_k if top_k is not None else config.TOP_K

        # 1. MCP Server Retrieval Tool Invocation (or explicitly provided evaluation chunks)
        if retrieved_chunks is None:
            retrieved_chunks = execute_mcp_tool("search_documents", {"query": query, "top_k": k})

        # 2. Defense Inspection on Retrieved Context
        formatted_context = "\n".join([c.get("text", "") for c in (retrieved_chunks or [])])
        defense_result = self.defense.inspect(user_instruction=query, retrieved_context=formatted_context)
        is_blocked = (defense_result.get("action_taken") == "BLOCK")

        # 3. LLM Answer Generation Grounded in Context (or security notice if blocked)
        if is_blocked:
            answer = f"[SECURITY ALERT]: Indirect prompt injection detected by {defense_result.get('defense_name')}. The untrusted retrieved context has been quarantined."
        else:
            answer = self.llm_provider.generate_rag_answer(query, retrieved_chunks)

        # 4. Structured Research Trace Log
        sources = [c.get("source", "unknown") for c in (retrieved_chunks or [])]
        scores = [c.get("score", 0.0) for c in (retrieved_chunks or [])]
        embedding_backend = getattr(getattr(self.retriever, "vector_store", None), "embedding_manager", None)
        backend_name = embedding_backend.backend_name if embedding_backend else "UNKNOWN"

        trace_log = {
            "request_id": request_id,
            "timestamp": timestamp,
            "query": query,
            "top_k": k,
            "embedding_backend": backend_name,
            "llm_provider": self.llm_provider.provider,
            "retrieved_sources": sources,
            "retrieval_scores": scores,
            "num_chunks_retrieved": len(retrieved_chunks or [])
        }

        return {
            "request_id": request_id,
            "query": query,
            "embedding_backend": backend_name,
            "llm_provider": self.llm_provider.provider,
            "defense_result": defense_result,
            "retrieved_chunks": retrieved_chunks,
            "generated_answer": answer,
            "trace_log": trace_log
        }

