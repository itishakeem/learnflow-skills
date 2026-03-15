---
name: mcp-code-execution
description: Wrap MCP server calls in executable scripts to minimize context token usage
---

# MCP Code Execution Pattern

## When to Use
- Integrating MCP servers efficiently without context bloat
- Wrapping repeated MCP tool calls in scripts
- Any operation that would load large datasets into agent context

## Instructions
1. Identify the MCP tool call to wrap
2. Generate script wrapper: `python scripts/wrap_mcp.py <tool-name>`
3. Verify token efficiency: `python scripts/verify_tokens.py`

## Validation
- [ ] Script executes MCP call outside context window
- [ ] Only minimal result returned to agent context
- [ ] Token usage reduced vs direct MCP call

See [REFERENCE.md](./REFERENCE.md) for MCP wrapping patterns.
