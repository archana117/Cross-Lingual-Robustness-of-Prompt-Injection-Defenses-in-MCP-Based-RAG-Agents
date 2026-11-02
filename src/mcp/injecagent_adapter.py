"""
InjecAgent MCP Adapter Module.

Bridges InjecAgent benchmark tools and simulated responses into the MCP architecture.
Allows the MCPAgent to execute benchmark user tools and attacker tools via MCP protocols,
routing responses from test case payloads or precomputed simulated responses in attacker_simulated_responses.json.
"""

import json
from typing import Dict, Any, List, Optional
from src.dataset.injecagent_loader import InjecAgentLoader
from src.mcp.server import mcp_server


class InjecAgentMCPAdapter:
    def __init__(self, loader: Optional[InjecAgentLoader] = None):
        self.loader = loader or InjecAgentLoader()
        self.tools_schema = self.loader.load_tools()
        self.simulated_responses = self.loader.load_simulated_responses()
        self.active_test_case: Optional[Dict[str, Any]] = None
        self.execution_history: List[Dict[str, Any]] = []

    def set_active_test_case(self, test_case: Dict[str, Any]):
        """
        Sets the active test case context for the current evaluation instance.
        """
        self.active_test_case = test_case
        self.execution_history = []

    def execute_tool(self, tool_name: str, arguments: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Executes a benchmark tool call.
        - If the tool is the user tool for the active test case, returns the simulated tool response
          which contains the legitimate response + the indirect injection.
        - If the tool is an attacker tool or secondary action, returns the simulated response from
          attacker_simulated_responses.json.
        """
        args = arguments or {}
        call_record = {
            "tool_name": tool_name,
            "arguments": args,
            "active_case_id": self.active_test_case.get("case_id") if self.active_test_case else None
        }
        self.execution_history.append(call_record)

        # 1. Check if tool is the active test case's primary User Tool
        if self.active_test_case and self.active_test_case.get("user_tool") == tool_name:
            response_text = self.active_test_case.get("tool_response", "")
            return {
                "status": "success",
                "tool_name": tool_name,
                "source": "injecagent_test_case",
                "output": response_text
            }

        # 2. Check if precomputed simulated response exists
        sim_resp = self.loader.get_simulated_response(tool_name, args)
        if sim_resp is not None:
            return {
                "status": "success",
                "tool_name": tool_name,
                "source": "simulated_cache",
                "output": sim_resp
            }

        # 3. Fallback for recognized tools without custom cached simulation
        if tool_name in self.tools_schema:
            return {
                "status": "success",
                "tool_name": tool_name,
                "source": "schema_mock",
                "output": f"Tool '{tool_name}' executed successfully with arguments: {json.dumps(args)}."
            }

        return {
            "status": "error",
            "tool_name": tool_name,
            "source": "unknown_tool",
            "output": f"Tool '{tool_name}' not found in InjecAgent benchmark tools."
        }

    def get_tool_declaration(self, tool_name: str) -> Optional[Dict[str, Any]]:
        """
        Returns the tool schema definition for prompt injection or agent tool calling.
        """
        return self.tools_schema.get(tool_name)

    def was_attacker_tool_called(self, attacker_tools: List[str]) -> bool:
        """
        Checks whether any of the target attacker tools were invoked in the current session.
        """
        called_names = [call["tool_name"] for call in self.execution_history]
        return any(at in called_names for at in attacker_tools)
