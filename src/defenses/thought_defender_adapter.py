"""
Thought Defender Adapter Module.

Wraps the Meticulous Thought Defender implementation (src/detector.py)
into the unified BaseDefense interface.
Analyzes fine-grained Chain-of-Thought (CoT) reasoning traces and semantic
consistency using BGE-M3 embeddings.
"""

import re
from typing import Dict, Any, Optional
from src.defenses.base import BaseDefense
from src.detector import ThoughtDefender
from src.embeddings import EmbeddingManager
import config


class ThoughtDefenderDefense(BaseDefense):
    def __init__(
        self,
        threshold: Optional[float] = None,
        embedding_manager: Optional[EmbeddingManager] = None,
        name: str = "MeticulousThoughtDefender"
    ):
        super().__init__(name=name)
        self.threshold = threshold if threshold is not None else config.ANOMALY_THRESHOLD
        self.detector = ThoughtDefender(threshold=self.threshold, embedding_manager=embedding_manager)

    def inspect(
        self,
        user_instruction: str,
        retrieved_context: str,
        reasoning_trace: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Inspects reasoning trace. If explicit trace is not provided, forms
        a standard multi-step sequence connecting user query, retrieved data, and planned tool call.
        Aligns step phrasing with the target language to prevent artificial cross-script cosine drops.
        """
        trace = reasoning_trace
        if not trace:
            clean_inst = (user_instruction or "").strip()[:200]
            clean_ctx = (retrieved_context or "").strip()[:512]
            combined = f"{clean_inst} {clean_ctx}"

            has_telugu = bool(re.search(r"[\u0c00-\u0c7f]", combined))
            has_hindi = bool(re.search(r"[\u0900-\u097f]", combined))
            is_teen = any(k in clean_inst.lower() for k in ["enti", "emiti", "cheyandi", "pettali", "lo", "ki", "gurinchi", "cheyadaniki"])

            if has_telugu:
                trace = (
                    f"STEP 1: వినియోగదారు ప్రశ్నను విశ్లేషించండి: {clean_inst}\n"
                    f"STEP 2: స్వీకరించిన సందర్భాన్ని చదవండి: {clean_ctx}\n"
                    f"STEP 3: ధృవీకరించబడిన సందర్భం ఆధారంగా వినియోగదారు పనిని నెరవేర్చే ఖచ్చితమైన సమాధానాన్ని రూపొందించండి."
                )
            elif has_hindi:
                trace = (
                    f"STEP 1: उपयोगकर्ता प्रश्न का विश्लेषण करें: {clean_inst}\n"
                    f"STEP 2: प्राप्त दस्तावेज़ संदर्भ को समझें: {clean_ctx}\n"
                    f"STEP 3: सत्यापित संदर्भ के आधार पर उपयोगकर्ता कार्य को पूरा करने के लिए उत्तर तैयार करें।"
                )
            elif is_teen:
                trace = (
                    f"STEP 1: User query ni analyze cheyandi: {clean_inst}\n"
                    f"STEP 2: Retrieved context ni ingest cheyandi: {clean_ctx}\n"
                    f"STEP 3: Verified context base chesukoni user task ki correct response formulate cheyandi."
                )
            else:
                trace = (
                    f"STEP 1: Parse user query: {clean_inst}\n"
                    f"STEP 2: Ingest retrieved document context: {clean_ctx}\n"
                    f"STEP 3: Plan response and next tool action grounded strictly in user task."
                )

        analysis = self.detector.analyze_trace(trace, prompt=user_instruction)
        is_attack = (analysis["prediction"] == "PROMPT_INJECTION")
        action = "BLOCK" if is_attack else "ALLOW"

        return {
            "defense_name": self.name,
            "is_attack_detected": is_attack,
            "anomaly_score": analysis["anomaly_score"],
            "action_taken": action,
            "sanitized_context": "[BLOCKED: Thought Defender detected anomalous reasoning transition]" if is_attack else retrieved_context,
            "details": {
                "embedding_backend": analysis["embedding_backend"],
                "path_consistency": analysis["path_consistency"],
                "suspicious_step_idx": analysis["suspicious_step_idx"],
                "suspicious_step_text": analysis["suspicious_step_text"],
                "suspicious_similarity": analysis["suspicious_similarity"],
                "suspicious_reason": analysis["suspicious_reason"],
                "threshold": self.threshold
            }
        }
