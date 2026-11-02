"""
Unit tests for MultilingualDatasetLoader.
Verifies loading across English, Hindi, Telugu, and Code-Mixed,
traceability to original English cases, and field schemas.
"""

import pytest
from src.dataset.multilingual_loader import MultilingualDatasetLoader

@pytest.fixture
def multi_loader():
    return MultilingualDatasetLoader()

def test_supported_languages(multi_loader):
    langs = multi_loader.get_supported_languages()
    assert "english" in langs
    assert "hindi" in langs
    assert "telugu" in langs
    assert "code_mixed" in langs

def test_language_case_counts(multi_loader):
    for lang in ["english", "hindi", "telugu", "code_mixed"]:
        cases = multi_loader.load_language_cases(lang)
        assert len(cases) == 2108, f"Expected 2108 cases for {lang}, got {len(cases)}"

def test_case_traceability_schema(multi_loader):
    hi_cases = multi_loader.load_language_cases("hindi")
    sample = hi_cases[0]
    
    assert "original_case_id" in sample
    assert "case_id" in sample
    assert sample["language"] == "Hindi"
    assert sample["source"] == "InjecAgent"
    assert "user_task" in sample
    assert "attack_content" in sample
    assert "attacker_tools" in sample
    assert "tool_response" in sample
    assert sample["case_id"] == f"{sample['original_case_id']}_hi"

def test_telugu_and_code_mixed_content(multi_loader):
    te_cases = multi_loader.load_language_cases("telugu")
    cm_cases = multi_loader.load_language_cases("code_mixed")
    
    assert len(te_cases[0]["user_task"]) > 0
    assert len(cm_cases[0]["user_task"]) > 0
    assert te_cases[0]["original_case_id"] == cm_cases[0]["original_case_id"]
