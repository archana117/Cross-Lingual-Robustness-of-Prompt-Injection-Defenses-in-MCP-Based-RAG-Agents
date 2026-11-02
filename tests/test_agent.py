import pytest
from src.agent import MCPAgent

def test_mcp_agent_answer_question():
    agent = MCPAgent()
    res = agent.answer_question("What is cloud computing?", top_k=2)
    assert "request_id" in res
    assert "generated_answer" in res
    assert "retrieved_chunks" in res
    assert "trace_log" in res
    assert len(res["retrieved_chunks"]) == 2
    assert "cloud" in res["generated_answer"].lower() or "computing" in res["generated_answer"].lower()
