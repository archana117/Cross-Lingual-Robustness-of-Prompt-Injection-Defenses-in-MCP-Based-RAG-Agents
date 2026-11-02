import sys
from pathlib import Path
import pandas as pd
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.embeddings import EmbeddingManager
from src.defenses.thought_defender_adapter import ThoughtDefenderDefense

em = EmbeddingManager()
df_val = pd.read_csv("data/custom_dataset/validation.csv")

print(f"Loaded validation set: {len(df_val)} records")
defense = ThoughtDefenderDefense(embedding_manager=em)

# Sample 3 safe and 3 attack from each language
sample_records = []
for lang in ["English", "Hindi", "Telugu", "Telugu-English"]:
    sub = df_val[df_val["language"] == lang]
    safe_samples = sub[sub["label"] == "SAFE"].head(3)
    att_samples = sub[sub["label"] == "ATTACK"].head(3)
    sample_records.extend(safe_samples.to_dict("records"))
    sample_records.extend(att_samples.to_dict("records"))

for r in sample_records:
    task = r["task"]
    doc = r["document_text"]
    lang = r["language"]
    label = r["label"]
    atk_type = r["attack_type"]
    
    res = defense.inspect(user_instruction=task, retrieved_context=doc)
    susp = det["suspicious_similarity"]
    susp_str = f"{susp:.4f}" if susp is not None else "None"
    print(f"[{lang:14}] [{label:6}] [{atk_type:20}] Score: {res['anomaly_score']:.4f} | Action: {res['action_taken']} | PathSim: {det['path_consistency']:.4f} | SuspSim: {susp_str}")
