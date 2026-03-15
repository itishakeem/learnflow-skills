---
name: docusaurus-deploy
description: Deploy a Docusaurus documentation site to Kubernetes
---

# Docusaurus Deploy

## When to Use
- Deploying documentation site for LearnFlow
- Setting up auto-generated docs from codebase
- User asks to create or update documentation site

## Instructions
1. Build docs site: `./scripts/build.sh`
2. Deploy to Kubernetes: `./scripts/deploy.sh`
3. Verify site: `python scripts/verify.py`

## Validation
- [ ] Docusaurus build succeeds
- [ ] Pod in Running state
- [ ] Documentation site accessible

See [REFERENCE.md](./REFERENCE.md) for configuration and deployment options.
