"""
Multilingual Dataset Loader Module.

Loads adapted multilingual InjecAgent test sets (English, Hindi, Telugu, Code-Mixed)
from custom_dataset/multilingual/.
"""

import json
from pathlib import Path
from typing import Dict, Any, List, Optional
import config


class MultilingualDatasetLoader:
    def __init__(self, base_dir: Optional[Path] = None):
        self.base_dir = Path(base_dir) if base_dir else config.CUSTOM_MULTILINGUAL_DIR

    def get_supported_languages(self) -> List[str]:
        return ["english", "hindi", "telugu", "code_mixed"]

    def load_language_cases(self, language: str) -> List[Dict[str, Any]]:
        lang_key = language.lower().replace("-", "_")
        target_file = self.base_dir / lang_key / "test_cases.json"
        if not target_file.exists():
            raise FileNotFoundError(
                f"Multilingual test cases for language '{language}' not found at {target_file}. "
                "Run scripts/generate_multilingual_benchmark.py to generate them."
            )
        with open(target_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def load_case_by_id(self, language: str, case_id: str) -> Optional[Dict[str, Any]]:
        cases = self.load_language_cases(language)
        for c in cases:
            if c.get("case_id") == case_id or c.get("original_case_id") == case_id:
                return c
        return None
