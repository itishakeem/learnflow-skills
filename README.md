# Learnflow-skills (Skills Library)

Reusable AI agent skills for building the LearnFlow platform. Skills work across Claude Code, Goose, and OpenAI Codex.

## Structure

```
Learnflow-skills/
├── .claude/
│   └── skills/                  # Works on Claude Code + Goose + Codex
│       ├── agents-md-gen/        # Generate AGENTS.md for repositories
│       ├── kafka-k8s-setup/      # Deploy Kafka on Kubernetes
│       ├── postgres-k8s-setup/   # Deploy PostgreSQL on Kubernetes
│       ├── fastapi-dapr-agent/   # FastAPI + Dapr microservice
│       ├── mcp-code-execution/   # MCP Code Execution pattern
│       ├── nextjs-k8s-deploy/    # Deploy Next.js to Kubernetes
│       └── docusaurus-deploy/    # Deploy Docusaurus docs site
├── recipes/                     # Goose recipes
│   ├── deploy-learnflow-platform/
│   ├── setup-infrastructure/
│   ├── setup-backend-services/
│   └── setup-frontend/
└── docs/
    └── skill-development-guide.md
```

## Skill Pattern (MCP Code Execution)

Each skill follows the token-efficient pattern:

| Component    | Tokens | Notes                     |
|--------------|--------|---------------------------|
| SKILL.md     | ~100   | Loaded when triggered     |
| REFERENCE.md | 0      | Loaded only if needed     |
| scripts/     | 0      | Executed, never loaded    |
| Final output | ~10    | Only result enters context|

## Usage

**Claude Code:**
```
Deploy Kafka on Kubernetes
```

**Goose:**
```
goose run recipes/deploy-learnflow-platform/RECIPE.md
```
