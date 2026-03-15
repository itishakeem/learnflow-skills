---
name: postgres-k8s-setup
description: Deploy PostgreSQL on Kubernetes and run database migrations
---

# PostgreSQL Kubernetes Setup

## When to Use
- User asks to deploy PostgreSQL
- Setting up database for microservices
- Running database migrations

## Instructions
1. Run deployment: `./scripts/deploy.sh`
2. Run migrations: `python scripts/migrate.py`
3. Verify schema: `python scripts/verify.py`

## Validation
- [ ] PostgreSQL pod in Running state
- [ ] Migrations completed successfully
- [ ] Database schema verified

See [REFERENCE.md](./REFERENCE.md) for configuration options.
