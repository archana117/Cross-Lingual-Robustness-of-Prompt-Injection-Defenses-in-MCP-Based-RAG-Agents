import json
from src.dataset.injecagent_loader import InjecAgentLoader

loader = InjecAgentLoader()
user_cases = loader.load_user_cases()
dh_cases = loader.load_attacker_cases("dh")
ds_cases = loader.load_attacker_cases("ds")

data = {
    "user_cases": [
        {"id": u["user_case_id"], "tool": u["user_tool"], "instruction": u["user_instruction"]}
        for u in user_cases
    ],
    "dh_cases": [
        {"id": a["attacker_case_id"], "tools": a["attacker_tools"], "type": a["attack_type"], "instruction": a["attacker_instruction"]}
        for a in dh_cases
    ],
    "ds_cases": [
        {"id": a["attacker_case_id"], "tools": a["attacker_tools"], "type": a["attack_type"], "instruction": a["attacker_instruction"]}
        for a in ds_cases
    ]
}

with open("scratch/cases_manifest.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Dumped {len(user_cases)} user cases, {len(dh_cases)} DH cases, {len(ds_cases)} DS cases.")
