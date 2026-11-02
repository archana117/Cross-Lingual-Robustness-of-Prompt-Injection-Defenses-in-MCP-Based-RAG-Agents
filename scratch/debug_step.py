import sys
import os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.embeddings import load_embedding_model

model = load_embedding_model()
print("Model loaded:", type(model))

print("Encoding simple text...")
emb = model.encode(["hello world"], convert_to_numpy=True)
print("Encoded shape:", emb.shape)

print("Encoding Telugu text...")
emb_te = model.encode(["వినియోగదారు ప్రశ్నను విశ్లేషించండి"], convert_to_numpy=True)
print("Encoded shape Telugu:", emb_te.shape)
