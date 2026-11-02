"""
Meticulous Thought Defender Detector Module.
Integrates reasoning extraction, BGE-M3 embedding, step & path consistency computation,
anomaly scoring, suspicious step localization, and threshold classification.
"""
import numpy as np
from typing import Dict, Any, List, Optional
import config
from src.reasoning import extract_reasoning_steps
from src.embeddings import EmbeddingManager
from src.consistency import (
    compute_consecutive_similarities,
    compute_step_consistency,
    compute_path_consistency
)

class ThoughtDefender:
    def __init__(self, threshold: float = None, embedding_manager: Optional[EmbeddingManager] = None):
        self.threshold = threshold if threshold is not None else config.ANOMALY_THRESHOLD
        self.embedding_manager = embedding_manager or EmbeddingManager()
        
    def analyze_trace(self, reasoning_text: str, prompt: str = "") -> Dict[str, Any]:
        """
        Runs complete Thought Defender pipeline on a given reasoning trace string.
        
        Args:
            reasoning_text (str): Multi-step reasoning trace.
            prompt (str): Optional user prompt for logging context.
            
        Returns:
            Dict[str, Any]: Detection result dictionary.
        """
        backend_name = self.embedding_manager.backend_name

        # 1. Step Extraction
        steps = extract_reasoning_steps(reasoning_text)
        n_steps = len(steps)
        
        if n_steps < 2:
            return {
                "prompt": prompt,
                "embedding_backend": backend_name,
                "reasoning_steps": steps,
                "step_similarities": [],
                "step_consistency_scores": [1.0] * max(1, n_steps),
                "path_consistency": 1.0,
                "anomaly_score": 0.0,
                "suspicious_step_idx": None,
                "suspicious_step_text": None,
                "suspicious_similarity": None,
                "suspicious_reason": "Insufficient reasoning steps to compute semantic transition.",
                "prediction": "SAFE"
            }
            
        # 2. Embedding Generation
        step_embeddings = self.embedding_manager.embed_steps(steps)
        
        # 3. Consecutive Similarities & Consistency Scores
        consecutive_sims = compute_consecutive_similarities(step_embeddings)
        step_consistencies = compute_step_consistency(consecutive_sims, n_steps)
        path_consistency = compute_path_consistency(consecutive_sims)
        
        sim_values = [s["similarity"] for s in consecutive_sims]
        min_transition_sim = min(sim_values) if sim_values else 1.0
        
        # 4. Initial Prototype Anomaly Formulation (Heuristic Configuration)
        # In real embedding space (BGE-M3), prompt injection attacks exhibit either:
        # a) Negative / near-zero cosine similarity (in mock/extreme mode), or
        # b) Severe consecutive step similarity drops (prev_step_sim -> curr_step_sim drop > 0.10), or
        # c) Minimum transition similarity dropping significantly below 0.52.
        
        max_transition_drop = 0.0
        for i in range(1, len(sim_values)):
            drop = sim_values[i - 1] - sim_values[i]
            if drop > max_transition_drop:
                max_transition_drop = drop
                
        # Handle cases where min similarity is negative or near zero (mock mode)
        if min_transition_sim < 0.0:
            anomaly_score = 1.0
        else:
            # Heuristic Prototype Anomaly components:
            # 1. Minimum transition similarity deficit below 0.52
            min_sim_deficit = max(0.0, 0.52 - min_transition_sim) / 0.25
            
            # 2. Maximum consecutive transition drop relative to 0.10 threshold
            drop_deficit = max(0.0, max_transition_drop - 0.10) / 0.15
            
            # 3. Path consistency deficit below 0.58
            path_deficit = max(0.0, 0.58 - path_consistency) / 0.20
            
            anomaly_score = float(0.45 * min_sim_deficit + 0.45 * drop_deficit + 0.10 * path_deficit)
            anomaly_score = float(np.clip(anomaly_score, 0.0, 1.0))
            
        # 5. Localize Suspicious Step
        suspicious_step_idx = None
        suspicious_step_text = None
        suspicious_similarity = None
        suspicious_reason = None
        
        if consecutive_sims:
            # Identify pair with minimum similarity or maximum transition drop
            min_pair = min(consecutive_sims, key=lambda x: x["similarity"])
            
            if anomaly_score >= self.threshold:
                suspicious_step_idx = min_pair["curr_step_idx"]  # 1-indexed step number
                suspicious_step_text = steps[suspicious_step_idx - 1]
                suspicious_similarity = min_pair["similarity"]
                suspicious_reason = (
                    f"Low semantic consistency with previous step (similarity: {suspicious_similarity:.4f}). "
                    "Abrupt transition detected in reasoning flow."
                )
                
        # 6. Classification
        prediction = "PROMPT_INJECTION" if anomaly_score >= self.threshold else "SAFE"
        
        return {
            "prompt": prompt,
            "embedding_backend": backend_name,
            "reasoning_steps": steps,
            "step_similarities": consecutive_sims,
            "step_consistency_scores": step_consistencies,
            "path_consistency": path_consistency,
            "anomaly_score": anomaly_score,
            "suspicious_step_idx": suspicious_step_idx,
            "suspicious_step_text": suspicious_step_text,
            "suspicious_similarity": suspicious_similarity,
            "suspicious_reason": suspicious_reason,
            "prediction": prediction
        }
