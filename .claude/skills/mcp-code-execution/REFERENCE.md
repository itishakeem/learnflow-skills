# MCP Code Execution Pattern - Reference

## The Core Problem

Direct MCP tool calls load full data into the agent context window:

| Approach | Token Cost | Notes |
|----------|-----------|-------|
| Direct MCP (5 servers) | ~50,000 tokens | Loaded before conversation starts |
| Direct MCP tool result | Full dataset size | Flows through context twice |
| Skills + Scripts | ~100 tokens | Only final result enters context |

## The Pattern

```
SKILL.md (~100 tokens)         scripts/tool.py (0 tokens — executed)
     |                                  |
     | "run scripts/tool.py"            | calls MCP server or executes locally
     |                                  | filters/processes data
     v                                  v
Agent Context <————— minimal result ————————————————
```

## Script Wrapping Template

```python
#!/usr/bin/env python3
"""
Wrap an MCP tool call — only the filtered result enters agent context.
"""
import subprocess, json, sys

# Execute MCP call or local equivalent
result = subprocess.run(
    ["<tool-command>", "<args>"],
    capture_output=True, text=True
)

data = json.loads(result.stdout)

# Filter — ONLY relevant subset
filtered = [item for item in data["items"] if item["status"] == "pending"]

# Print minimal result — this is ALL that enters context
if filtered:
    print(f"✓ {len(filtered)} pending items: {[i['id'] for i in filtered[:5]]}")
else:
    print("✓ No pending items")
    sys.exit(0)
```

## When to Use Each Approach

| Use MCP Directly | Use Skills + Scripts |
|-----------------|----------------------|
| Simple, single API call | Complex multi-step workflows |
| Infrequent tool use | Repeated operations |
| Small response payload | Large datasets (>1,000 rows) |
| Quick lookups | Data processing / validation |

## Script Reference

| Script | Purpose | Usage |
|--------|---------|-------|
| `wrap_mcp.py` | Generates a script wrapper for a given MCP tool | `python scripts/wrap_mcp.py <tool-name>` |
| `verify_tokens.py` | Estimates token usage before and after wrapping | `python scripts/verify_tokens.py <script>` |

## Token Efficiency Targets

| Component | Target Tokens |
|-----------|--------------|
| SKILL.md | ~100 |
| REFERENCE.md | 0 (loaded on-demand) |
| scripts/*.py | 0 (executed, never loaded) |
| Final output to context | <50 tokens |

## Useful Commands

```bash
# Wrap an existing MCP tool call
python scripts/wrap_mcp.py kubernetes.getPods

# Verify token reduction
python scripts/verify_tokens.py scripts/get_pods.py
```
