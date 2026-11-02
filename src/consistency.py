"""
Consistency Metrics Module.
Calculates consecutive step cosine similarities, step-level consistency,
and overall path-level consistency.
"""
import numpy as np
from typing import List, Dict, Any, Tuple
from src.embeddings import cosine_similarity

def compute_consecutive_similarities(step_embeddings: np.ndarray) -> List[Dict[str, Any]]:
    """
    Calculates cosine similarity between adjacent pairs of steps: step_i and step_(i+1).
    
    Args:
        step_embeddings (np.ndarray): Array of shape (N, d) containing step vectors.
        
    Returns:
        List[Dict[str, Any]]: List of dictionary pair similarity records.
    """
    n_steps = len(step_embeddings)
    similarities = []
    
    if n_steps < 2:
        return similarities
        
    for i in range(n_steps - 1):
        vec1 = step_embeddings[i]
        vec2 = step_embeddings[i + 1]
        sim = cosine_similarity(vec1, vec2)
        similarities.append({
            "pair_index": i,
            "prev_step_idx": i + 1,
            "curr_step_idx": i + 2,
            "similarity": float(sim)
        })
        
    return similarities

def compute_step_consistency(similarities: List[Dict[str, Any]], n_steps: int) -> List[float]:
    """
    Calculates a local consistency score for each step (1..N).
    
    For step i (1-indexed):
    - First step (i=1): similarity(step 1, step 2)
    - Last step (i=N): similarity(step N-1, step N)
    - Intermediate step (i): average(similarity(step i-1, step i), similarity(step i, step i+1))
    
    Returns:
        List[float]: Local consistency score for each step.
    """
    if n_steps <= 0:
        return []
    if n_steps == 1 or not similarities:
        return [1.0] * n_steps
        
    step_scores = [0.0] * n_steps
    sim_values = [s["similarity"] for s in similarities]
    
    # First step
    step_scores[0] = sim_values[0]
    
    # Last step
    step_scores[-1] = sim_values[-1]
    
    # Middle steps
    for i in range(1, n_steps - 1):
        prev_sim = sim_values[i - 1] # step i-1 -> step i
        next_sim = sim_values[i]     # step i -> step i+1
        step_scores[i] = float((prev_sim + next_sim) / 2.0)
        
    return step_scores

def compute_path_consistency(similarities: List[Dict[str, Any]]) -> float:
    """
    Calculates overall reasoning-path semantic consistency score.
    Path consistency = mean of all valid neighboring-step similarities.
    
    Returns:
        float: Path consistency score in [0.0, 1.0].
    """
    if not similarities:
        return 1.0
    sim_values = [s["similarity"] for s in similarities]
    mean_sim = float(np.mean(sim_values))
    return float(np.clip(mean_sim, 0.0, 1.0))
