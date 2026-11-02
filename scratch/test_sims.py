import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
from src.embeddings import EmbeddingManager
from src.reasoning import extract_reasoning_steps
from src.consistency import compute_consecutive_similarities

em = EmbeddingManager()
df = pd.read_csv('data/custom_dataset/test.csv')

te_safe = df[(df['scenario_id']=='S209') & (df['language']=='Telugu') & (df['label']=='SAFE')].iloc[0]
te_att = df[(df['scenario_id']=='S209') & (df['language']=='Telugu') & (df['label']=='ATTACK')].iloc[0]

for name, rec in [('TELUGU SAFE', te_safe), ('TELUGU ATTACK', te_att)]:
    print('=== ' + name + ' ===')
    q = rec['task'][:120]
    d = rec['document_text'][:200]
    trace = f"STEP 1: Parse user query: {q}\nSTEP 2: Ingest retrieved tool context: {d}\nSTEP 3: Plan response and next tool action grounded strictly in user task."
    steps = extract_reasoning_steps(trace)
    step_embs = em.embed_steps(steps)
    sims = compute_consecutive_similarities(step_embs)
    for s in sims:
        print(f"  Step {s['prev_step_idx']} -> Step {s['curr_step_idx']}: sim={s['similarity']:.4f}")
