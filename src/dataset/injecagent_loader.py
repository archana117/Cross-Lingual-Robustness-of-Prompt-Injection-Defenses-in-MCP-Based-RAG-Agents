"""
InjecAgent Dataset Loader Module.

Loads, validates, and resolves the 9 benchmark files from the InjecAgent dataset:
- user_cases.jsonl (17 legitimate user cases)
- attacker_cases_dh.jsonl (30 Direct Harm attack cases)
- attacker_cases_ds.jsonl (32 Data Stealing attack cases)
- test_cases_dh_base.json (510 DH base test cases)
- test_cases_dh_enhanced.json (510 DH enhanced test cases)
- test_cases_ds_base.json (544 DS base test cases)
- test_cases_ds_enhanced.json (544 DS enhanced test cases)
- tools.json (38 toolkits, 330 tools)
- attacker_simulated_responses.json (2,347 precomputed simulated responses)
"""

import json
import ast
from pathlib import Path
from typing import Dict, Any, List, Optional, Union
import config


class InjecAgentLoader:
    def __init__(self, dataset_dir: Optional[Union[str, Path]] = None):
        self.dataset_dir = Path(dataset_dir) if dataset_dir else config.INJECAGENT_DIR
        self._validate_directory()

        self._tools_cache: Optional[Dict[str, Any]] = None
        self._simulated_responses_cache: Optional[Dict[str, str]] = None
        self._user_cases_cache: Optional[List[Dict[str, Any]]] = None
        self._dh_cases_cache: Optional[List[Dict[str, Any]]] = None
        self._ds_cases_cache: Optional[List[Dict[str, Any]]] = None

    def _validate_directory(self):
        if not self.dataset_dir.exists():
            raise FileNotFoundError(
                f"InjecAgent dataset directory not found at: {self.dataset_dir}. "
                f"Please ensure existing_dataset/InjecAgent/ is present."
            )

    def _load_jsonl(self, filename: str) -> List[Dict[str, Any]]:
        file_path = self.dataset_dir / filename
        if not file_path.exists():
            raise FileNotFoundError(f"Required InjecAgent file missing: {file_path}")
        records = []
        with open(file_path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError as e:
                    raise ValueError(f"Malformed JSONL on line {line_no} of {file_path}: {e}")
        return records

    def _load_json(self, filename: str) -> Any:
        file_path = self.dataset_dir / filename
        if not file_path.exists():
            raise FileNotFoundError(f"Required InjecAgent file missing: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"Malformed JSON in {file_path}: {e}")

    # =========================================================================
    # 1. Tools Loader
    # =========================================================================
    def load_tools(self, force_reload: bool = False) -> Dict[str, Dict[str, Any]]:
        """
        Loads and indexes tools from tools.json into a flat dictionary keyed by
        canonical tool name: f"{toolkit}{tool_name}".
        Example: "AmazonGetProductDetails", "AugustSmartLockGrantGuestAccess".
        """
        if self._tools_cache is not None and not force_reload:
            return self._tools_cache

        raw_toolkits = self._load_json("tools.json")
        if not isinstance(raw_toolkits, list):
            raise ValueError(f"Expected list in tools.json, got {type(raw_toolkits)}")

        tools_map = {}
        for tk in raw_toolkits:
            toolkit_name = tk.get("toolkit", "")
            category = tk.get("category", "")
            description_for_model = tk.get("description_for_model", "")
            for tool in tk.get("tools", []):
                tool_func_name = tool.get("name", "")
                canonical_name = f"{toolkit_name}{tool_func_name}"
                tools_map[canonical_name] = {
                    "canonical_name": canonical_name,
                    "toolkit": toolkit_name,
                    "function_name": tool_func_name,
                    "category": category,
                    "toolkit_description": description_for_model,
                    "description": tool.get("description", ""),
                    "parameters": tool.get("parameters", {}),
                    "raw_tool_def": tool
                }

        self._tools_cache = tools_map
        return self._tools_cache

    # =========================================================================
    # 2. Simulated Responses Cache
    # =========================================================================
    def load_simulated_responses(self, force_reload: bool = False) -> Dict[str, str]:
        """
        Loads precomputed simulated tool responses from attacker_simulated_responses.json.
        Keys are formatted as: '(ToolName,{"param": "val"})' or '(ToolName,{})'.
        """
        if self._simulated_responses_cache is not None and not force_reload:
            return self._simulated_responses_cache

        raw_responses = self._load_json("attacker_simulated_responses.json")
        if not isinstance(raw_responses, dict):
            raise ValueError(f"Expected dictionary in attacker_simulated_responses.json, got {type(raw_responses)}")

        self._simulated_responses_cache = raw_responses
        return self._simulated_responses_cache

    def get_simulated_response(self, tool_name: str, parameters: Optional[Dict[str, Any]] = None) -> Optional[str]:
        """
        Looks up a simulated response for a tool call.
        """
        responses = self.load_simulated_responses()
        params = parameters or {}
        # Try exact json formatting (standard compact separators)
        param_str = json.dumps(params, separators=(', ', ': '))
        key_standard = f"({tool_name},{param_str})"
        if key_standard in responses:
            return responses[key_standard]

        # Alternative compact formatting
        param_str_compact = json.dumps(params, separators=(',', ':'))
        key_compact = f"({tool_name},{param_str_compact})"
        if key_compact in responses:
            return responses[key_compact]

        # Fallback empty params match
        empty_key = f"({tool_name},{{}})"
        if empty_key in responses:
            return responses[empty_key]

        return None

    # =========================================================================
    # 3. User Cases
    # =========================================================================
    def load_user_cases(self, force_reload: bool = False) -> List[Dict[str, Any]]:
        """
        Loads legitimate user cases from user_cases.jsonl.
        Attaches unique identifier: user_case_00 .. user_case_16.
        """
        if self._user_cases_cache is not None and not force_reload:
            return self._user_cases_cache

        raw_cases = self._load_jsonl("user_cases.jsonl")
        tools_map = self.load_tools()

        user_cases = []
        for idx, item in enumerate(raw_cases):
            user_tool = item.get("User Tool")
            if not user_tool:
                raise ValueError(f"Missing 'User Tool' in user_cases.jsonl record {idx}")

            if user_tool not in tools_map:
                print(f"[Warning] User tool '{user_tool}' not explicitly found in tools.json")

            user_case = {
                "user_case_id": f"user_case_{idx:02d}",
                "index": idx,
                "user_tool": user_tool,
                "user_instruction": item.get("User Instruction", ""),
                "tool_parameters_raw": item.get("Tool Parameters", ""),
                "tool_response_template": item.get("Tool Response Template", ""),
                "expected_thought": item.get("Thought", ""),
                "risk_level": item.get("Level", "Normal")
            }
            user_cases.append(user_case)

        self._user_cases_cache = user_cases
        return self._user_cases_cache

    # =========================================================================
    # 4. Attacker Cases (Direct Harm & Data Stealing)
    # =========================================================================
    def load_attacker_cases(self, attack_mode: str = "all", force_reload: bool = False) -> List[Dict[str, Any]]:
        """
        Loads attacker cases from attacker_cases_dh.jsonl and/or attacker_cases_ds.jsonl.
        attack_mode options: 'dh', 'ds', 'all'.
        """
        cases = []
        tools_map = self.load_tools()

        if attack_mode in ["dh", "all"]:
            if self._dh_cases_cache is None or force_reload:
                raw_dh = self._load_jsonl("attacker_cases_dh.jsonl")
                dh_list = []
                for idx, item in enumerate(raw_dh):
                    c = {
                        "attacker_case_id": f"dh_attacker_{idx:02d}",
                        "index": idx,
                        "attack_setting": "dh",
                        "attack_type": item.get("Attack Type", "Direct Harm"),
                        "attacker_tools": item.get("Attacker Tools", []),
                        "attacker_instruction": item.get("Attacker Instruction", ""),
                        "expected_achievements": item.get("Expected Achievements", ""),
                        "modified": item.get("Modifed", 0)
                    }
                    dh_list.append(c)
                self._dh_cases_cache = dh_list
            cases.extend(self._dh_cases_cache)

        if attack_mode in ["ds", "all"]:
            if self._ds_cases_cache is None or force_reload:
                raw_ds = self._load_jsonl("attacker_cases_ds.jsonl")
                ds_list = []
                for idx, item in enumerate(raw_ds):
                    c = {
                        "attacker_case_id": f"ds_attacker_{idx:02d}",
                        "index": idx,
                        "attack_setting": "ds",
                        "attack_type": item.get("Attack Type", "Data Stealing"),
                        "attacker_tools": item.get("Attacker Tools", []),
                        "attacker_instruction": item.get("Attacker Instruction", ""),
                        "expected_achievements": item.get("Expected Achievements", ""),
                        "modified": item.get("Modifed", 0)
                    }
                    ds_list.append(c)
                self._ds_cases_cache = ds_list
            cases.extend(self._ds_cases_cache)

        return cases

    # =========================================================================
    # 5. Full Benchmark Test Cases
    # =========================================================================
    def load_test_cases(self, split: str = "dh_base") -> List[Dict[str, Any]]:
        """
        Loads test cases for a specific benchmark split or 'all'.
        Supported splits:
        - 'dh_base' (510 cases)
        - 'dh_enhanced' (510 cases)
        - 'ds_base' (544 cases)
        - 'ds_enhanced' (544 cases)
        - 'all' (2108 cases total)
        """
        split_files = {
            "dh_base": ("test_cases_dh_base.json", "dh", "base"),
            "dh_enhanced": ("test_cases_dh_enhanced.json", "dh", "enhanced"),
            "ds_base": ("test_cases_ds_base.json", "ds", "base"),
            "ds_enhanced": ("test_cases_ds_enhanced.json", "ds", "enhanced"),
        }

        if split == "all":
            all_cases = []
            for s in split_files.keys():
                all_cases.extend(self.load_test_cases(split=s))
            return all_cases

        if split not in split_files:
            raise ValueError(f"Unknown split: '{split}'. Valid options: {list(split_files.keys()) + ['all']}")

        filename, attack_setting, enhancement = split_files[split]
        raw_cases = self._load_json(filename)
        if not isinstance(raw_cases, list):
            raise ValueError(f"Expected list in {filename}, got {type(raw_cases)}")

        # Ensure user cases and attacker cases are loaded for relationship mapping
        user_cases = self.load_user_cases()
        attacker_cases = self.load_attacker_cases(attack_mode=attack_setting)
        num_user = len(user_cases)  # 17

        resolved_cases = []
        for idx, item in enumerate(raw_cases):
            # InjecAgent ordering: attacker_idx = idx // 17, user_idx = idx % 17
            u_idx = idx % num_user
            a_idx = idx // num_user
            u_case_id = f"user_case_{u_idx:02d}"
            a_case_id = f"{attack_setting}_attacker_{a_idx:02d}"
            case_id = f"{attack_setting}_{enhancement}_u{u_idx:02d}_a{a_idx:02d}"

            # Safely parse tool parameters string
            param_raw = item.get("Tool Parameters", "{}")
            try:
                # Parameters in InjecAgent are often single-quoted python dict strings
                parsed_params = ast.literal_eval(param_raw) if param_raw else {}
            except Exception:
                parsed_params = {"raw": param_raw}

            test_case = {
                "case_id": case_id,
                "split": split,
                "attack_setting": attack_setting,
                "enhancement": enhancement,
                "user_case_id": u_case_id,
                "attacker_case_id": a_case_id,
                "user_instruction": item.get("User Instruction", ""),
                "user_tool": item.get("User Tool", ""),
                "user_tool_parameters": parsed_params,
                "attacker_instruction": item.get("Attacker Instruction", ""),
                "attacker_tools": item.get("Attacker Tools", []),
                "attack_type": item.get("Attack Type", ""),
                "expected_achievements": item.get("Expected Achievements", ""),
                "thought": item.get("Thought", ""),
                "tool_response_template": item.get("Tool Response Template", ""),
                "tool_response": item.get("Tool Response", ""),
                "source": "InjecAgent",
                "language": "en"
            }
            resolved_cases.append(test_case)

        return resolved_cases

    # =========================================================================
    # 6. Benchmark Summary Reporter
    # =========================================================================
    def get_benchmark_summary(self) -> Dict[str, Any]:
        """
        Validates the entire InjecAgent dataset and returns structural statistics.
        """
        tools = self.load_tools()
        sim_responses = self.load_simulated_responses()
        user_cases = self.load_user_cases()
        dh_cases = self.load_attacker_cases("dh")
        ds_cases = self.load_attacker_cases("ds")

        dh_base = self.load_test_cases("dh_base")
        dh_enh = self.load_test_cases("dh_enhanced")
        ds_base = self.load_test_cases("ds_base")
        ds_enh = self.load_test_cases("ds_enhanced")

        return {
            "dataset_directory": str(self.dataset_dir),
            "num_toolkits": len(set(t["toolkit"] for t in tools.values())),
            "total_tools": len(tools),
            "num_user_cases": len(user_cases),
            "num_dh_attacker_cases": len(dh_cases),
            "num_ds_attacker_cases": len(ds_cases),
            "num_dh_base_test_cases": len(dh_base),
            "num_dh_enhanced_test_cases": len(dh_enh),
            "num_ds_base_test_cases": len(ds_base),
            "num_ds_enhanced_test_cases": len(ds_enh),
            "total_test_cases": len(dh_base) + len(dh_enh) + len(ds_base) + len(ds_enh),
            "num_simulated_responses": len(sim_responses),
            "validation_status": "VALIDATED"
        }
