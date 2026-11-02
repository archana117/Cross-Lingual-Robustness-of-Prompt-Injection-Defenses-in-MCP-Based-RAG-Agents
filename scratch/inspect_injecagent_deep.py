import json
from pathlib import Path
from collections import Counter

injecagent_dir = Path("data/existing_dataset/InjecAgent")

print("==================================================")
print("INJECAGENT DEEP INSPECTION")
print("==================================================")

# 1. user_cases.jsonl
user_cases = [json.loads(line) for line in open(injecagent_dir / "user_cases.jsonl", encoding="utf-8") if line.strip()]
print(f"\n1. USER CASES: {len(user_cases)} records")
for idx, uc in enumerate(user_cases):
    print(f"[{idx}] User Tool: {uc.get('User Tool')}")
    print(f"    Level: {uc.get('Level')}")
    print(f"    Instruction: {uc.get('User Instruction')}")
    print(f"    Parameters: {uc.get('Tool Parameters')}")
    print(f"    Response Template: {uc.get('Tool Response Template')[:100]}...")

# 2. attacker_cases_dh.jsonl
dh_cases = [json.loads(line) for line in open(injecagent_dir / "attacker_cases_dh.jsonl", encoding="utf-8") if line.strip()]
print(f"\n2. ATTACKER CASES DH (Direct Harm): {len(dh_cases)} records")
dh_attack_types = Counter(c.get('Attack Type') for c in dh_cases)
print(f"    Attack Types: {dict(dh_attack_types)}")
for idx in range(min(3, len(dh_cases))):
    c = dh_cases[idx]
    print(f"    [{idx}] Attack Type: {c.get('Attack Type')}, Modified: {c.get('Modifed')}")
    print(f"        Tools: {c.get('Attacker Tools')}")
    print(f"        Instruction: {c.get('Attacker Instruction')}")
    print(f"        Expected: {c.get('Expected Achievements')}")

# 3. attacker_cases_ds.jsonl
ds_cases = [json.loads(line) for line in open(injecagent_dir / "attacker_cases_ds.jsonl", encoding="utf-8") if line.strip()]
print(f"\n3. ATTACKER CASES DS (Data Stealing): {len(ds_cases)} records")
ds_attack_types = Counter(c.get('Attack Type') for c in ds_cases)
print(f"    Attack Types: {dict(ds_attack_types)}")
for idx in range(min(3, len(ds_cases))):
    c = ds_cases[idx]
    print(f"    [{idx}] Attack Type: {c.get('Attack Type')}, Modified: {c.get('Modifed')}")
    print(f"        Tools: {c.get('Attacker Tools')}")
    print(f"        Instruction: {c.get('Attacker Instruction')}")
    print(f"        Expected: {c.get('Expected Achievements')}")

# 4. test_cases_dh_base.json and test_cases_dh_enhanced.json
with open(injecagent_dir / "test_cases_dh_base.json", encoding="utf-8") as f:
    dh_base = json.load(f)
with open(injecagent_dir / "test_cases_dh_enhanced.json", encoding="utf-8") as f:
    dh_enh = json.load(f)
print(f"\n4. DH TEST CASES: Base={len(dh_base)}, Enhanced={len(dh_enh)}")

# 5. test_cases_ds_base.json and test_cases_ds_enhanced.json
with open(injecagent_dir / "test_cases_ds_base.json", encoding="utf-8") as f:
    ds_base = json.load(f)
with open(injecagent_dir / "test_cases_ds_enhanced.json", encoding="utf-8") as f:
    ds_enh = json.load(f)
print(f"\n5. DS TEST CASES: Base={len(ds_base)}, Enhanced={len(ds_enh)}")

# 6. Check relationship: Are test cases the Cartesian product of user_cases and attacker_cases?
print("\n6. CARTESIAN PRODUCT VERIFICATION:")
print(f"DH: {len(user_cases)} user cases * {len(dh_cases)} attacker cases = {len(user_cases) * len(dh_cases)} (matches {len(dh_base)})")
print(f"DS: {len(user_cases)} user cases * {len(ds_cases)} attacker cases = {len(user_cases) * len(ds_cases)} (matches {len(ds_base)})")

# Let's verify ordering: is it user_case-first or attacker_case-first?
# Let's inspect test_cases 0, 1, 2, 17, 30...
print(f"Case 0 User Instruction: {dh_base[0]['User Instruction'][:40]}")
print(f"Case 0 Attacker Instruction: {dh_base[0]['Attacker Instruction'][:40]}")
print(f"Case 1 User Instruction: {dh_base[1]['User Instruction'][:40]}")
print(f"Case 1 Attacker Instruction: {dh_base[1]['Attacker Instruction'][:40]}")
print(f"Case 17 User Instruction: {dh_base[17]['User Instruction'][:40]}")
print(f"Case 17 Attacker Instruction: {dh_base[17]['Attacker Instruction'][:40]}")

# 7. tools.json
with open(injecagent_dir / "tools.json", encoding="utf-8") as f:
    tools_data = json.load(f)
print(f"\n7. TOOLS.JSON: {len(tools_data)} toolkits")
total_tools = sum(len(tk.get("tools", [])) for tk in tools_data)
print(f"    Total individual tools across toolkits: {total_tools}")
tool_names = []
for tk in tools_data:
    for t in tk.get("tools", []):
        tool_names.append(t.get("name"))
print(f"    Sample individual tool names: {tool_names[:10]}")

# 8. attacker_simulated_responses.json
with open(injecagent_dir / "attacker_simulated_responses.json", encoding="utf-8") as f:
    sim_resp = json.load(f)
print(f"\n8. ATTACKER SIMULATED RESPONSES: {len(sim_resp)} response mappings")
sample_sim_keys = list(sim_resp.keys())[:5]
for sk in sample_sim_keys:
    print(f"    Key: {sk} -> Value snippet: {repr(sim_resp[sk])[:80]}")

# 9. Check how enhanced prompt wraps base instruction:
base_inst = dh_base[0]["Attacker Instruction"]
base_resp = dh_base[0]["Tool Response"]
enh_resp = dh_enh[0]["Tool Response"]
print(f"\n9. BASE vs ENHANCED WRAPPING:")
print(f"    Base instruction: {base_inst}")
# Find where the instruction is in base_resp and enh_resp
idx_b = base_resp.find(base_inst)
idx_e = enh_resp.find(base_inst)
if idx_b >= 0:
    print(f"    In Base Tool Response prefix before instruction: {repr(base_resp[max(0, idx_b-30):idx_b])}")
if idx_e >= 0:
    print(f"    In Enh Tool Response prefix before instruction: {repr(enh_resp[max(0, idx_e-80):idx_e])}")
