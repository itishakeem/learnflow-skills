# Next.js Kubernetes Deploy - Reference

## Dockerfile Template

```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
COPY --from=builder /app/public ./public
EXPOSE 3000
CMD ["node", "server.js"]
```

## Kubernetes Manifest Template

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: frontend
        image: learnflow-frontend:latest
        imagePullPolicy: Never   # use local Minikube image
        ports:
        - containerPort: 3000
        env:
        - name: NEXT_PUBLIC_API_URL
          value: "http://triage.default.svc.cluster.local:8000"
---
apiVersion: v1
kind: Service
metadata:
  name: frontend
  namespace: default
spec:
  type: NodePort
  selector:
    app: frontend
  ports:
  - port: 3000
    targetPort: 3000
    nodePort: 30300
```

## Monaco Editor Integration

```tsx
// Install: npm install @monaco-editor/react
import Editor from "@monaco-editor/react";

<Editor
  height="400px"
  defaultLanguage="python"
  defaultValue="# Write your Python here"
  theme="vs-dark"
  options={{ minimap: { enabled: false }, fontSize: 14 }}
  onChange={(value) => setCode(value ?? "")}
/>
```

## Script Reference

| Script | Purpose | Usage |
|--------|---------|-------|
| `build.sh` | Builds Docker image using Minikube's Docker daemon | `./scripts/build.sh` |
| `deploy.sh` | Applies K8s deployment and service manifests | `./scripts/deploy.sh` |
| `verify.py` | Checks pod status and NodePort accessibility | `python scripts/verify.py` |

## Useful Commands

```bash
# Build image into Minikube (no registry needed)
eval $(minikube docker-env)
docker build -t learnflow-frontend:latest ./frontend

# Get NodePort URL
minikube service frontend --url

# Watch pod startup
kubectl get pods -w -l app=frontend

# View frontend logs
kubectl logs -l app=frontend -f
```
