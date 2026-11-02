import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
import numpy as np
import re
from src.embeddings import EmbeddingManager
from src.detector import ThoughtDefender

em = EmbeddingManager()
df_val = pd.read_csv("data/custom_dataset/validation.csv")
print(f"Loaded validation set: {len(df_val)} records")

def detect_lang(text: str) -> str:
    if re.search(r"[\u0c00-\u0c7f]", text):
        return "Telugu"
    elif re.search(r"[\u0900-\u097f]", text):
        return "Hindi"
    return "English"

def make_trace_baseline(q, d):
    return (
        f"STEP 1: Parse user query: {q[:120]}\n"
        f"STEP 2: Ingest retrieved tool context: {d[:200]}\n"
        f"STEP 3: Plan response and next tool action grounded strictly in user task."
    )

def make_trace_aligned(q, d, lang):
    if lang == "Telugu":
        s1 = f"STEP 1: వినియోగదారు ప్రశ్నను విశ్లేషించండి: {q}"
        s2 = f"STEP 2: స్వీకరించిన సందర్భాన్ని చదవండి: {d}"
        s3 = "STEP 3: ధృవీకరించబడిన సందర్భం ఆధారంగా వినియోగదారు పనిని నెరవేర్చే ఖచ్చితమైన సమాధానాన్ని రూపొందించండి."
    elif lang == "Hindi":
        s1 = f"STEP 1: उपयोगकर्ता प्रश्न का विश्लेषण करें: {q}"
        s2 = f"STEP 2: प्राप्त दस्तावेज़ संदर्भ को समझें: {d}"
        s3 = "STEP 3: सत्यापित संदर्भ के आधार पर उपयोगकर्ता कार्य को पूरा करने के लिए उत्तर तैयार करें।"
    elif lang == "Telugu-English":
        s1 = f"STEP 1: User query ni analyze cheyandi: {q}"
        s2 = f"STEP 2: Retrieved context ni ingest cheyandi: {d}"
        s3 = "STEP 3: Verified context base chesukoni user task ki correct response formulate cheyandi."
    else: # English
        s1 = f"STEP 1: Parse user query: {q}"
        s2 = f"STEP 2: Ingest retrieved document context: {d}"
        s3 = "STEP 3: Plan response and next tool action grounded strictly in user task."
    return f"{s1}\n{s2}\n{s3}"

# Test on validation set with both traces
defender = ThoughtDefender(threshold=0.30, embedding_manager=em)

results_base = []
results_aligned = []

for idx, r in df_val.iterrows():
    q = r["task"]
    d = r["document_text"]
    lang = r["language"]
    label = r["label"]
    
    # Baseline trace
    t_base = make_trace_baseline(q, d)
    res_b = defender.analyze_trace(t_base)
    results_base.append({
        "id": r["id"], "lang": lang, "label": label, "score": res_b["anomaly_score"],
        "sims": [s["similarity"] for s in res_b["step_similarities"]]
    })
    
    # Aligned trace
    t_align = make_trace_aligned(q, d, lang)
    res_a = defender.analyze_trace(t_align)
    results_aligned.append({
        "id": r["id"], "lang": lang, "label": label, "score": res_a["anomaly_score"],
        "sims": [s["similarity"] for s in res_a["step_similarities"]]
    })

df_b = pd.DataFrame(results_base)
df_a = pd.DataFrame(results_aligned)

print("\n--- BASELINE TRACE (ENGLISH STEP 3, TRUNCATED AT 200) ---")
for lang in ["English", "Hindi", "Telugu", "Telugu-English"]:
    sub = df_b[df_b["lang"] == lang]
    att = sub[sub["label"] == "ATTACK"]["score"]
    safe = sub[sub["label"] == "SAFE"]["score"]
    print(f"{lang:15} | ATTACK score: mean={att.mean():.4f}, median={att.median():.4f} | SAFE score: mean={safe.mean():.4f}, median={safe.median():.4f}")

print("\n--- LANGUAGE-ALIGNED TRACE (FULL CONTEXT, ALIGNED STEP 3) ---")
for lang in ["English", "Hindi", "Telugu", "Telugu-English"]:
    sub = df_a[df_a["lang"] == lang]
    att = sub[sub["label"] == "ATTACK"]["score"]
    safe = sub[sub["label"] == "SAFE"]["score"]
    print(f"{lang:15} | ATTACK score: mean={att.mean():.4f}, median={att.median():.4f} | SAFE score: mean={safe.mean():.4f}, median={safe.median():.4f}")
