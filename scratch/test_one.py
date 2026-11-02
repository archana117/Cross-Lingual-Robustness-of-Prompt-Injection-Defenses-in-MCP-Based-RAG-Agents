import sys
from pathlib import Path
import traceback
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

try:
    from src.embeddings import EmbeddingManager
    from src.defenses.thought_defender_adapter import ThoughtDefenderDefense

    em = EmbeddingManager()
    df_val = pd.read_csv("data/custom_dataset/validation.csv")
    defense = ThoughtDefenderDefense(embedding_manager=em)

    row = df_val.iloc[0]
    task = row["task"]
    doc = row["document_text"]
    lang = row["language"]
    label = row["label"]
    atk_type = row["attack_type"]

    print("Running inspect...")
    res = defense.inspect(user_instruction=task, retrieved_context=doc)
    print("Inspect result:", res)
except Exception:
    traceback.print_exc()
