---
name: fastapi-dapr-agent
description: Create a FastAPI microservice with Dapr sidecar and AI agent integration
---

# FastAPI + Dapr Agent Microservice

## When to Use
- Creating a new AI-powered microservice
- Setting up Dapr pub/sub for a FastAPI service
- Building triage, concepts, debug, or exercise agents for LearnFlow

## Instructions
1. Scaffold service: `python scripts/scaffold.py <service-name>`
2. Apply Dapr components: `./scripts/apply_dapr_components.sh`
3. Verify service: `python scripts/verify.py <service-name>`

## Validation
- [ ] FastAPI service running
- [ ] Dapr sidecar injected
- [ ] Pub/sub topics connected
- [ ] Agent endpoints responding

See [REFERENCE.md](./REFERENCE.md) for Dapr component templates.
