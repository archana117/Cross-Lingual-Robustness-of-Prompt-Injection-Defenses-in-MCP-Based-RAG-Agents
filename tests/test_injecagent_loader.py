"""
Unit tests for InjecAgentLoader.
Verifies file presence, record counts, tool schemas, simulated response lookup,
and test case relationship mapping.
"""
import pytest
from src.dataset.injecagent_loader import InjecAgentLoader

@pytest.fixture
def loader():
    return InjecAgentLoader()

def test_loader_tools(loader):
    tools = loader.load_tools()
    assert len(tools) == 330
    assert "AmazonGetProductDetails" in tools
    assert "AugustSmartLockGrantGuestAccess" in tools
    assert tools["AmazonGetProductDetails"]["toolkit"] == "Amazon"

def test_loader_user_cases(loader):
    user_cases = loader.load_user_cases()
    assert len(user_cases) == 17
    assert user_cases[0]["user_case_id"] == "user_case_00"
    assert "User Tool" not in user_cases[0]  # Standardized key names
    assert user_cases[0]["user_tool"] == "AmazonGetProductDetails"
    assert "<Attacker Instruction>" in user_cases[0]["tool_response_template"]

def test_loader_attacker_cases(loader):
    dh_cases = loader.load_attacker_cases("dh")
    assert len(dh_cases) == 30
    assert dh_cases[0]["attacker_case_id"] == "dh_attacker_00"
    assert len(dh_cases[0]["attacker_tools"]) > 0

    ds_cases = loader.load_attacker_cases("ds")
    assert len(ds_cases) == 32
    assert ds_cases[0]["attacker_case_id"] == "ds_attacker_00"
    assert len(ds_cases[0]["attacker_tools"]) > 0

def test_loader_test_cases_relationship(loader):
    dh_base = loader.load_test_cases("dh_base")
    assert len(dh_base) == 510
    
    first = dh_base[0]
    assert first["case_id"] == "dh_base_u00_a00"
    assert first["user_case_id"] == "user_case_00"
    assert first["attacker_case_id"] == "dh_attacker_00"
    assert first["user_tool"] == "AmazonGetProductDetails"
    assert first["attacker_instruction"] in first["tool_response"]

def test_loader_simulated_responses(loader):
    sim = loader.load_simulated_responses()
    assert len(sim) == 2347
    
    resp = loader.get_simulated_response("AmazonViewSavedAddresses", {})
    assert resp is not None
    assert "123 Main St" in resp

def test_loader_summary(loader):
    summary = loader.get_benchmark_summary()
    assert summary["validation_status"] == "VALIDATED"
    assert summary["total_test_cases"] == 2108
