# Deploy LearnFlow Platform

This recipe deploys the full LearnFlow AI learning platform end-to-end.

## Steps

1. Setup Infrastructure

Use recipe: setup-infrastructure

2. Setup Backend Services

Use recipe: setup-backend-services

3. Setup Frontend

Use recipe: setup-frontend

4. Verify Platform

Check that:
- Kafka is running in `kafka` namespace
- PostgreSQL is running in `postgres` namespace
- Dapr control plane is running in `dapr-system` namespace
- All FastAPI microservices are Running
- Next.js frontend is accessible
- Docusaurus docs site is accessible

## Expected Result

LearnFlow platform fully deployed on Kubernetes with all services healthy.
