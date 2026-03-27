# Docusaurus Deploy - Reference

## Project Setup

```bash
# Scaffold a new Docusaurus site
npx create-docusaurus@latest docs classic --typescript
```

## Recommended Directory Structure

```
docs/
├── docusaurus.config.ts   # Site config (title, navbar, footer)
├── sidebars.ts            # Sidebar navigation structure
├── docs/                  # Markdown documentation files
│   ├── intro.md
│   ├── skills/
│   │   ├── kafka-k8s-setup.md
│   │   ├── postgres-k8s-setup.md
│   │   └── ...
│   └── learnflow/
│       ├── architecture.md
│       └── services.md
└── static/                # Static assets (images, etc.)
```

## Dockerfile Template

```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

## Kubernetes Manifest Template

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: docs
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: docs
  template:
    metadata:
      labels:
        app: docs
    spec:
      containers:
      - name: docs
        image: learnflow-docs:latest
        imagePullPolicy: Never
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: docs
  namespace: default
spec:
  type: NodePort
  selector:
    app: docs
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30380
```

## Script Reference

| Script | Purpose | Usage |
|--------|---------|-------|
| `build.sh` | Installs deps and builds static site, then builds Docker image | `./scripts/build.sh` |
| `deploy.sh` | Applies K8s deployment and service manifests | `./scripts/deploy.sh` |
| `verify.py` | Checks pod status and site accessibility | `python scripts/verify.py` |

## Useful Commands

```bash
# Build image into Minikube
eval $(minikube docker-env)
docker build -t learnflow-docs:latest ./docs

# Get NodePort URL
minikube service docs --url

# Watch pod startup
kubectl get pods -w -l app=docs

# Local dev preview
cd docs && npm start
```
