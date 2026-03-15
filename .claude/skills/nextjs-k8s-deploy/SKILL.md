---
name: nextjs-k8s-deploy
description: Build and deploy a Next.js application to Kubernetes with Monaco editor support
---

# Next.js Kubernetes Deploy

## When to Use
- Deploying Next.js frontend to Kubernetes
- Setting up the LearnFlow frontend with Monaco code editor
- Containerizing and deploying a Next.js app

## Instructions
1. Build Docker image: `./scripts/build.sh`
2. Deploy to Kubernetes: `./scripts/deploy.sh`
3. Verify deployment: `python scripts/verify.py`

## Validation
- [ ] Docker image built successfully
- [ ] Pod in Running state
- [ ] Frontend accessible via NodePort or Ingress
- [ ] Monaco editor loading correctly

See [REFERENCE.md](./REFERENCE.md) for Dockerfile and K8s manifest templates.
