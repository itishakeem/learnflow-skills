# AGENTS.md Generator - Reference

## AGENTS.md Format Specification

An `AGENTS.md` file lives at the repository root and describes the codebase to AI agents.

### Required Sections

| Section | Purpose |
|---------|---------|
| `## Overview` | Project summary, tech stack, and purpose |
| `## Repository Structure` | Directory tree with descriptions |
| `## Conventions` | Naming conventions, code style, patterns |
| `## Key Files` | Critical files every agent should know |
| `## Development Workflow` | How to build, test, and run locally |
| `## Agent Instructions` | Specific guidance for AI coding agents |

### Minimal Example

```markdown
# Repository: learnflow-app

## Overview
AI-powered Python tutoring platform. Built with Next.js frontend,
FastAPI microservices, Kafka pub/sub, Dapr sidecar, on Kubernetes.

## Repository Structure
learnflow-app/
├── frontend/        # Next.js + Monaco editor
├── services/        # FastAPI microservices
│   ├── triage/      # Routes queries to specialist agents
│   ├── concepts/    # Explains Python concepts
│   ├── debug/       # Debugs student code errors
│   ├── exercise/    # Generates and grades exercises
│   └── progress/    # Tracks student mastery scores
├── k8s/             # Kubernetes manifests
│   ├── dapr/        # Dapr component configs
│   ├── kafka/       # Kafka deployment
│   └── services/    # Per-service deployments
└── AGENTS.md

## Conventions
- Services use FastAPI with Dapr sidecar pattern
- All inter-service communication via Kafka topics
- Python services: snake_case, PEP 8
- TypeScript frontend: camelCase, functional components

## Agent Instructions
- Never write code manually — use skills in .claude/skills/
- Always verify Kubernetes pods are Running before proceeding
- Use `kubectl -n <namespace>` for all cluster operations
```

## Script Reference

| Script | Purpose | Output |
|--------|---------|--------|
| `analyze_repo.py` | Scans directory tree, detects languages and frameworks | JSON summary |
| `generate_agents_md.py` | Creates AGENTS.md from analysis output | `AGENTS.md` at repo root |
| `verify_agents_md.py` | Checks required sections exist and are non-empty | Pass/Fail |

## Useful Commands

```bash
# Run full pipeline
python scripts/analyze_repo.py && python scripts/generate_agents_md.py && python scripts/verify_agents_md.py

# Regenerate for a specific path
python scripts/analyze_repo.py --path ./services/triage
```
