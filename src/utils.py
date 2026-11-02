"""
Utility Functions Module.
Dataset loaders, directory helpers, and formatting utilities.
"""
import json
from pathlib import Path
from typing import List, Dict, Any
import config

def load_sample_dataset(file_path: Path = None) -> List[Dict[str, Any]]:
    """
    Loads sample benchmark dataset JSON.
    """
    target_path = file_path or (config.DATA_DIR / "sample_prompts.json")
    if not target_path.exists():
        raise FileNotFoundError(f"Dataset file not found at {target_path}")
        
    with open(target_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def save_json(data: Any, file_path: Path):
    """
    Saves python object as formatted JSON file.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
