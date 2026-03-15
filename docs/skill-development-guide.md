# Skill Development Guide

## Overview

Skills are the core product of this repository. Each skill teaches AI agents (Claude Code, Goose, Codex) how to perform a specific infrastructure or development task autonomously.

## Skill Structure

Every skill follows this structure:

```
.claude/skills/<skill-name>/
├── SKILL.md        # ~100 tokens — loaded when triggered
├── REFERENCE.md    # loaded only when needed
└── scripts/        # executed, never loaded into context
    ├── deploy.sh
    └── verify.py
```

## SKILL.md Format

```markdown
---
name: skill-name
description: One-line description for agent discovery
---

# Skill Title

## When to Use
Trigger conditions and use cases.

## Instructions
Step-by-step guidance referencing scripts/.

## Validation
- [ ] Checklist items to verify success
```

## MCP Code Execution Pattern

Scripts execute outside the agent context window — only the final result enters context.

| Component    | Tokens  | Notes                        |
|--------------|---------|------------------------------|
| SKILL.md     | ~100    | Loaded when triggered        |
| REFERENCE.md | 0       | Loaded only if needed        |
| scripts/     | 0       | Executed, never loaded       |
| Final output | ~10     | Only result enters context   |

## Cross-Agent Compatibility

These skills work on:
- **Claude Code** — reads `.claude/skills/`
- **Goose** — reads `.claude/skills/` (AAIF standard)
- **OpenAI Codex** — reads `.claude/skills/`
