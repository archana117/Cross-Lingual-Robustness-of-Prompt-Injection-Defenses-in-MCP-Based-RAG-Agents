"""
No-Defense Baseline Module.
Acts as a pass-through baseline for evaluating raw agent vulnerability under attack.
"""

from typing import Dict, Any, Optional
from src.defenses.base import BaseDefense


class NoDefense(BaseDefense):
    def __init__(self):
        super().__init__(name="NoDefense_Baseline")

    def inspect(
        self,
        user_instruction: str,
        retrieved_context: str,
        reasoning_trace: Optional[str] = None
    ) -> Dict[str, Any]:
        return {
            "defense_name": self.name,
            "is_attack_detected": False,
            "anomaly_score": 0.0,
            "action_taken": "ALLOW",
            "sanitized_context": retrieved_context,
            "details": {
                "message": "Pass-through baseline without filtering or detection."
            }
        }
