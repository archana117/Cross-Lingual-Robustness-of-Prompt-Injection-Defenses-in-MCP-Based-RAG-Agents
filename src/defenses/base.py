"""
Base Defense Interface Module.

Defines the standard abstract contract for evaluating prompt-injection defenses
consistently across English, Telugu, Hindi, and Code-mixed RAG/MCP pipelines.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class BaseDefense(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def inspect(
        self,
        user_instruction: str,
        retrieved_context: str,
        reasoning_trace: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Evaluates input query, retrieved context (tool response / RAG chunk),
        and optional reasoning trace for potential prompt injection.

        Returns:
            Dict[str, Any]: Standard defense decision dictionary:
                - defense_name (str): Unique name of the defense
                - is_attack_detected (bool): True if injection is detected
                - anomaly_score (float): Normalized anomaly score in [0.0, 1.0]
                - action_taken (str): 'ALLOW', 'BLOCK', or 'SANITIZED'
                - sanitized_context (str): Context with malicious segments stripped or replaced
                - details (dict): Component-specific diagnostic logs
        """
        pass
