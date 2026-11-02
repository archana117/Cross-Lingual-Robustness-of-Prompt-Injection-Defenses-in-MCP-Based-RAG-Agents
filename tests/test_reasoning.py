import pytest
from src.reasoning import extract_reasoning_steps

def test_extract_reasoning_steps_standard():
    text = (
        "STEP 1: Identify entity.\n"
        "STEP 2: Query database.\n"
        "STEP 3: Format output."
    )
    steps = extract_reasoning_steps(text)
    assert len(steps) == 3
    assert steps[0] == "Identify entity."
    assert steps[1] == "Query database."
    assert steps[2] == "Format output."

def test_extract_reasoning_steps_numbered():
    text = (
        "1. First step text.\n"
        "2. Second step text."
    )
    steps = extract_reasoning_steps(text)
    assert len(steps) == 2
    assert steps[0] == "First step text."
    assert steps[1] == "Second step text."

def test_extract_reasoning_steps_fallback():
    text = "Understand task. Access database. Produce final answer."
    steps = extract_reasoning_steps(text)
    assert len(steps) >= 2
