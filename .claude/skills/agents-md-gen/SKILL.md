---
name: agents-md-gen
description: Generate AGENTS.md file for a repository to help AI agents understand codebase structure and conventions
---

# AGENTS.md Generator

## When to Use
- Setting up a new repository for AI agent development
- Onboarding AI agents to an existing codebase
- User asks to generate or create an AGENTS.md file

## Instructions
1. Analyze the repository structure: `python scripts/analyze_repo.py`
2. Generate the AGENTS.md file: `python scripts/generate_agents_md.py`
3. Verify the output: `python scripts/verify_agents_md.py`

## Validation
- [ ] AGENTS.md exists at repo root
- [ ] File describes repo structure, conventions, and guidelines
- [ ] AI agents can understand codebase from the file

See [REFERENCE.md](./REFERENCE.md) for AGENTS.md format specification.
