---
name: kafka-k8s-setup
description: Deploy Apache Kafka on Kubernetes using Helm
---

# Kafka Kubernetes Setup

## When to Use
- User asks to deploy Kafka
- Setting up event-driven microservices
- Configuring pub/sub messaging infrastructure

## Instructions
1. Run deployment: `./scripts/deploy.sh`
2. Verify status: `python scripts/verify.py`
3. Confirm all pods Running before proceeding

## Validation
- [ ] All pods in Running state
- [ ] Can create test topic
- [ ] Services accessible within cluster

See [REFERENCE.md](./REFERENCE.md) for configuration options.
