# PostgreSQL Kubernetes Setup - Reference

## Helm Chart Configuration

- Chart: `bitnami/postgresql`
- Namespace: `postgres`
- Default storage: 8Gi

## Key Helm Values

| Value | Default | Description |
|-------|---------|-------------|
| `auth.postgresPassword` | `learnflow` | Superuser password |
| `auth.database` | `learnflow` | Default database name |
| `primary.persistence.size` | `8Gi` | Storage for primary |
| `readReplicas.replicaCount` | `0` | Read replicas (0 for dev) |

## LearnFlow Database Schema

| Table | Purpose |
|-------|---------|
| `users` | Student and teacher accounts |
| `sessions` | Auth sessions |
| `progress` | Per-topic mastery scores |
| `submissions` | Code submission history |
| `exercises` | Generated exercises and grades |

## Connection Details

```bash
# Connection string (inside cluster)
postgresql://postgres:learnflow@postgres-postgresql.postgres.svc.cluster.local:5432/learnflow

# Port-forward for local access
kubectl port-forward -n postgres svc/postgres-postgresql 5432:5432
```

## Script Reference

| Script | Purpose | Output |
|--------|---------|--------|
| `deploy.sh` | Installs PostgreSQL via Helm | Pod running in `postgres` namespace |
| `migrate.py` | Runs SQL migration files in order | Schema applied |
| `verify.py` | Checks pod status and schema exists | Pass/Fail |

## Useful Commands

```bash
# Connect to PostgreSQL pod
kubectl exec -it -n postgres postgres-postgresql-0 -- psql -U postgres -d learnflow

# List tables
kubectl exec -n postgres postgres-postgresql-0 -- psql -U postgres -d learnflow -c '\dt'

# Check pod status
kubectl get pods -n postgres
```
