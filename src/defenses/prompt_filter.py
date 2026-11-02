"""
Prompt Filter Perimeter Defense Module.
A heuristic rule-based defense checking for system prompt override tokens,
jailbreak delimiters, and imperative hijack phrases across English, Hindi, and Telugu.
"""

import re
from typing import Dict, Any, Optional, List
from src.defenses.base import BaseDefense


class PromptFilterDefense(BaseDefense):
    def __init__(self, name: str = "PromptFilter_Perimeter"):
        super().__init__(name=name)
        # Multilingual injection indicator patterns
        self.injection_keywords = [
            # English
            r"\bignore\s+(?:all\s+)?previous\s+instructions?\b",
            r"\bstrictly\s+adhere\s+to\b",
            r"\bsystem\s+prompt\b",
            r"\bdisregard\s+the\s+above\b",
            r"\bconfidential\s+system\b",
            r"\bimportant\s*!*:\s*ignore\b",
            r"\badmin(?:istrative)?\s+notice\b",
            # Hindi
            r"पिछला\s+निर्देश\s+अनदेखा",
            r"निर्देश\s+अनदेखा\s+करें",
            r"गोपनीय\s+निर्देश",
            r"सिस्टम\s+प्रॉम्प्ट",
            # Telugu
            r"మునుపటి\s+సూచనలను\s+విస్మరించండి",
            r"రహస్య\s+సూచనలు",
            r"సిస్టమ్\s+ప్రాంప్ట్"
        ]
        self._compiled_regexes = [re.compile(pat, re.IGNORECASE) for pat in self.injection_keywords]

    def inspect(
        self,
        user_instruction: str,
        retrieved_context: str,
        reasoning_trace: Optional[str] = None
    ) -> Dict[str, Any]:
        matched_indicators = []
        text_to_scan = f"{retrieved_context}\n{reasoning_trace or ''}"

        for regex in self._compiled_regexes:
            if regex.search(text_to_scan):
                matched_indicators.append(regex.pattern)

        is_detected = len(matched_indicators) > 0
        anomaly_score = 1.0 if is_detected else 0.0
        action = "BLOCK" if is_detected else "ALLOW"

        return {
            "defense_name": self.name,
            "is_attack_detected": is_detected,
            "anomaly_score": anomaly_score,
            "action_taken": action,
            "sanitized_context": "[BLOCKED DUE TO SUSPICIOUS INSTRUCTION]" if is_detected else retrieved_context,
            "details": {
                "matched_patterns": matched_indicators,
                "matches_count": len(matched_indicators)
            }
        }
