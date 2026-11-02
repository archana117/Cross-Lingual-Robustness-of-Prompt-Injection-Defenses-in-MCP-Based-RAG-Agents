"""
Dedicated MCP End-to-End Client/Server Transport Verification Script for PROJECT ARCHANA.

Tests actual MCP protocol communication over stdio transport:
MCP Client process <--- stdio JSON-RPC transport ---> Subprocess MCP Server (src/mcp/server.py)
"""
import sys
import os
import json
import asyncio
from typing import Dict, Any, List

# Ensure project root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp import ClientSession

async def run_mcp_e2e_verification():
    print("=" * 50)
    print("MCP END-TO-END VERIFICATION")
    print("=" * 50)

    # 1. Configure stdio server parameters
    server_script = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src", "mcp", "server.py"))
    
    server_env = dict(os.environ)
    # Ensure offline mock or current environment is passed
    if "BGE_MODEL_NAME" not in server_env:
        server_env["BGE_MODEL_NAME"] = "mock"
    if "LLM_PROVIDER" not in server_env:
        server_env["LLM_PROVIDER"] = "mock"

    server_params = StdioServerParameters(
        command=sys.executable,
        args=[server_script],
        env=server_env
    )

    print("MCP Server: STARTING...")
    
    # 2. Launch server process and establish stdio transport client session
    async with stdio_client(server_params) as (read_stream, write_stream):
        print("MCP Server: RUNNING")
        
        async with ClientSession(read_stream, write_stream) as session:
            # 3. Client initialization
            await session.initialize()
            print("MCP Client: CONNECTED")

            # 4. Discover tools
            tools_response = await session.list_tools()
            tool_names = [tool.name for tool in tools_response.tools]
            
            if "search_documents" not in tool_names:
                print("Tool discovered: FAILED (search_documents not found)")
                print("MCP END-TO-END TEST: FAILED")
                return False
                
            print("Tool discovered: search_documents")

            # 5. Call search_documents tool over stdio MCP transport
            query = "What is Hyderabad?"
            top_k = 2
            
            result = await session.call_tool("search_documents", arguments={"query": query, "top_k": top_k})
            
            if not result or not result.content:
                print("Tool call: FAILED (Empty response)")
                print("MCP END-TO-END TEST: FAILED")
                return False
                
            print("Tool call: SUCCESS")

            # 6. Parse returned chunks JSON from TextContent
            raw_text = result.content[0].text
            chunks = json.loads(raw_text)
            
            num_chunks = len(chunks)
            print(f"Retrieved chunks: {num_chunks}")

            # 7. Verify source metadata and similarity scores
            has_metadata = all("source" in c and "doc_id" in c for c in chunks)
            has_scores = all("score" in c for c in chunks)

            print(f"Source metadata: {'PRESENT' if has_metadata else 'MISSING'}")
            print(f"Similarity scores: {'PRESENT' if has_scores else 'MISSING'}")

            if num_chunks > 0 and has_metadata and has_scores:
                print("\nMCP END-TO-END TEST: PASSED")
                print("=" * 50)
                return True
            else:
                print("\nMCP END-TO-END TEST: FAILED")
                print("=" * 50)
                return False

def main():
    try:
        success = asyncio.run(run_mcp_e2e_verification())
        if not success:
            sys.exit(1)
    except Exception as e:
        print(f"\nError during MCP E2E verification: {e}")
        print("MCP END-TO-END TEST: FAILED")
        print("=" * 50)
        sys.exit(1)

if __name__ == "__main__":
    main()
