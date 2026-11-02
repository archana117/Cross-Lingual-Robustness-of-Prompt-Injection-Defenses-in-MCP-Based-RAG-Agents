"""
Reasoning Step Extractor.
Parses multi-step text into clean individual reasoning strings.
Handles patterns like STEP 1:, Step 1:, 1., numbered lines, and newline separators.
"""
import re
from typing import List

def extract_reasoning_steps(text: str) -> List[str]:
    """
    Extracts individual reasoning step strings from raw LLM reasoning output.
    
    Args:
        text (str): Raw reasoning trace string.
        
    Returns:
        List[str]: Clean list of reasoning steps.
    """
    if not text or not isinstance(text, str):
        return []
        
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    steps = []
    
    # Pattern matching STEP 1:, Step 1:, 1., [Step 1], etc.
    step_pattern = re.compile(r'^(?:(?:STEP|Step)\s*\d+[\:\.\-]?|\d+[\:\.\)]|\[Step\s*\d+\])\s*(.*)', re.IGNORECASE)
    
    for line in lines:
        match = step_pattern.match(line)
        if match:
            extracted = match.group(1).strip()
            if extracted:
                steps.append(extracted)
        else:
            # If line doesn't start with explicit label but steps were already accumulating, 
            # append to previous step or treat as standalone step line
            if len(steps) > 0 and not re.match(r'^[A-Z\s]{4,}:', line):
                # Continuation of previous step or line without number
                steps[-1] += " " + line
            else:
                steps.append(line)
                
    # Fallback to sentence splitting if fewer than 2 steps extracted
    if len(steps) < 2:
        sentence_candidates = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if len(s.strip()) > 10]
        if len(sentence_candidates) >= 2:
            return sentence_candidates
            
    # Final fallback if nothing else works
    if not steps and text.strip():
        steps = [text.strip()]
        
    return steps
