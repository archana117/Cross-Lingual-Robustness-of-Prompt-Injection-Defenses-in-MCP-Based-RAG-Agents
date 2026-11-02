import pytest
import numpy as np
from src.consistency import (
    compute_consecutive_similarities,
    compute_step_consistency,
    compute_path_consistency
)

def test_compute_consecutive_similarities():
    embeddings = np.array([
        [1.0, 0.0],
        [1.0, 0.0],
        [0.0, 1.0]
    ])
    sims = compute_consecutive_similarities(embeddings)
    assert len(sims) == 2
    assert abs(sims[0]["similarity"] - 1.0) < 1e-5
    assert abs(sims[1]["similarity"] - 0.0) < 1e-5

def test_compute_step_consistency():
    sims = [
        {"pair_index": 0, "prev_step_idx": 1, "curr_step_idx": 2, "similarity": 0.8},
        {"pair_index": 1, "prev_step_idx": 2, "curr_step_idx": 3, "similarity": 0.2}
    ]
    scores = compute_step_consistency(sims, n_steps=3)
    assert len(scores) == 3
    assert abs(scores[0] - 0.8) < 1e-5
    assert abs(scores[1] - 0.5) < 1e-5
    assert abs(scores[2] - 0.2) < 1e-5

def test_compute_path_consistency():
    sims = [
        {"pair_index": 0, "similarity": 0.8},
        {"pair_index": 1, "similarity": 0.4}
    ]
    path_score = compute_path_consistency(sims)
    assert abs(path_score - 0.6) < 1e-5
