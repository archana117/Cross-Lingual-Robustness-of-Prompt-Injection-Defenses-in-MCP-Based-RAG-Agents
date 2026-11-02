import json
from pathlib import Path

injecagent_dir = Path("data/existing_dataset/InjecAgent")

with open(injecagent_dir / "tools.json", encoding="utf-8") as f:
    tools_data = json.load(f)

with open(injecagent_dir / "user_cases.jsonl", encoding="utf-8") as f:
    user_cases = [json.loads(line) for line in f if line.strip()]

with open(injecagent_dir / "attacker_cases_dh.jsonl", encoding="utf-8") as f:
    dh_cases = [json.loads(line) for line in f if line.strip()]

with open(injecagent_dir / "attacker_cases_ds.jsonl", encoding="utf-8") as f:
    ds_cases = [json.loads(line) for line in f if line.strip()]

with open(injecagent_dir / "test_cases_dh_base.json", encoding="utf-8") as f:
    dh_base = json.load(f)

with open(injecagent_dir / "test_cases_ds_base.json", encoding="utf-8") as f:
    ds_base = json.load(f)

# Check tool names mapping
toolkit_tools = {}
for tk in tools_data:
    tk_name = tk["toolkit"]
    for t in tk.get("tools", []):
        full_tool_name = f"{tk_name}{t['name']}"
        toolkit_tools[full_tool_name] = {
            "toolkit": tk_name,
            "tool_name": t["name"],
            "description": t.get("description", ""),
            "parameters": t.get("parameters", {})
        }

print(f"Total mapped tool functions: {len(toolkit_tools)}")

# Check User Tools in toolkit_tools
user_tools = set(uc["User Tool"] for uc in user_cases)
print(f"Unique User Tools in user_cases ({len(user_tools)}):", user_tools)
missing_user_tools = [ut for ut in user_tools if ut not in toolkit_tools]
print("Missing User Tools from tools.json:", missing_user_tools)

# Check Attacker Tools in toolkit_tools
attacker_tools = set()
for ac in dh_cases + ds_cases:
    for at in ac.get("Attacker Tools", []):
        attacker_tools.add(at)
print(f"Unique Attacker Tools ({len(attacker_tools)}):", attacker_tools)
missing_attacker_tools = [at for at in attacker_tools if at not in toolkit_tools]
print("Missing Attacker Tools from tools.json:", missing_attacker_tools)

# Check how test_cases are constructed from user_cases and attacker_cases:
print("\n--- TEST CASE COMPOSITION VERIFICATION ---")
# Check if dh_base[0] matches dh_cases[0] and user_cases[0]
first_tc = dh_base[0]
print("Test Case 0:")
print("  User Instruction matches user_cases[0]:", first_tc["User Instruction"] == user_cases[0]["User Instruction"])
print("  Attacker Instruction matches dh_cases[0]:", first_tc["Attacker Instruction"] == dh_cases[0]["Attacker Instruction"])
print("  User Tool:", first_tc["User Tool"])
print("  Attacker Tools:", first_tc["Attacker Tools"])

# Check how Tool Response is filled
template = user_cases[0]["Tool Response Template"]
attacker_inst = dh_cases[0]["Attacker Instruction"]
filled_template = template.replace("<Attacker Instruction>", attacker_inst)
print("Does filled template match Tool Response in dh_base[0]?", filled_template in first_tc["Tool Response"] or first_tc["Tool Response"] in filled_template)
print("Tool Response Template snippet:", repr(template[:80]))
print("Tool Response snippet in dh_base[0]:", repr(first_tc["Tool Response"][:80]))

# Let's inspect test_cases_dh_enhanced[0] vs test_cases_dh_base[0]
with open(injecagent_dir / "test_cases_dh_enhanced.json", encoding="utf-8") as f:
    dh_enh = json.load(f)

print("\n--- ENHANCED PROMPT TEMPLATE EXTRACTION ---")
# Find what prefix/suffix was added around Attacker Instruction
inst = dh_cases[0]["Attacker Instruction"]
enh_resp = dh_enh[0]["Tool Response"]
base_resp = dh_base[0]["Tool Response"]
enh_pos = enh_resp.find(inst)
if enh_pos >= 0:
    prefix = enh_resp[enh_resp.rfind("'", 0, enh_pos)+1:enh_pos]
    print(f"Enhanced prompt prefix before instruction: {repr(prefix)}")
