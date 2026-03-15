#!/usr/bin/env python3
"""
MCP Code Execution Pattern — wraps an MCP tool call in a script.
Instead of loading full MCP tool results into agent context,
this script executes the call and returns only minimal output.
"""

import sys
import json
import subprocess


def wrap_mcp(tool_name: str, params: dict) -> str:
    """
    Execute an MCP tool call via subprocess and return minimal result.
    Only the final summary string enters the agent context window.
    """
    # Build the mcp call command
    mcp_input = json.dumps({"tool": tool_name, "params": params})

    result = subprocess.run(
        ["npx", "@modelcontextprotocol/cli", "call", tool_name],
        input=mcp_input,
        capture_output=True,
        text=True,
        timeout=30
    )

    if result.returncode != 0:
        return f"✗ MCP call failed: {result.stderr.strip()[:200]}"

    # Parse and summarise — only minimal result returned to context
    try:
        data = json.loads(result.stdout)
        items = data if isinstance(data, list) else data.get("items", [data])
        count = len(items)
        return f"✓ {tool_name} returned {count} item(s)"
    except json.JSONDecodeError:
        lines = result.stdout.strip().splitlines()
        return f"✓ {tool_name} completed — {lines[-1] if lines else 'done'}"


def filter_and_return(tool_name: str, params: dict, filter_fn):
    """
    Execute MCP call, filter results in script (not in context),
    return only filtered summary.
    """
    mcp_input = json.dumps({"tool": tool_name, "params": params})

    result = subprocess.run(
        ["npx", "@modelcontextprotocol/cli", "call", tool_name],
        input=mcp_input,
        capture_output=True,
        text=True,
        timeout=30
    )

    if result.returncode != 0:
        print(f"✗ MCP call failed: {result.stderr.strip()[:200]}")
        sys.exit(1)

    data = json.loads(result.stdout)
    items = data if isinstance(data, list) else data.get("items", [data])

    # Filter happens HERE in script — not in agent context
    filtered = [item for item in items if filter_fn(item)]

    # Only return minimal summary to context
    print(f"✓ Filtered {len(filtered)}/{len(items)} items from {tool_name}")
    return filtered


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python wrap_mcp.py <tool-name> [params-json]")
        sys.exit(1)

    tool = sys.argv[1]
    params = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    result = wrap_mcp(tool, params)
    print(result)
