import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import json
from src.embeddings import EmbeddingManager, cosine_similarity
from src.reasoning import extract_reasoning_steps

em = EmbeddingManager('BAAI/bge-m3')
with open('data/sample_prompts.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"{'SAMPLE ID':<25} | {'LABEL':<10} | {'PATH MEAN':<10} | {'MIN SIM':<10} | PAIR SIMILARITIES")
print("-" * 90)

for s in data:
    steps = extract_reasoning_steps(s['reasoning_trace'])
    vecs = em.embed_steps(steps)
    if len(vecs) > 1:
        sims = [cosine_similarity(vecs[i], vecs[i+1]) for i in range(len(vecs)-1)]
        path_mean = sum(sims) / len(sims)
        min_sim = min(sims)
        sim_str = ", ".join([f"{x:.3f}" for x in sims])
        print(f"{s['id']:<25} | {s['label']:<10} | {path_mean:<10.4f} | {min_sim:<10.4f} | [{sim_str}]")
