#!/bin/bash
set -e

NAMESPACE="learnflow"
IMAGE_NAME="${1:-learnflow-frontend}"
IMAGE_TAG="${2:-latest}"

echo "Creating namespace '$NAMESPACE'..."
kubectl create namespace $NAMESPACE --dry-run=client -o yaml | kubectl apply -f -

echo "Deploying Next.js frontend to Kubernetes..."
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  namespace: $NAMESPACE
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
        image: $IMAGE_NAME:$IMAGE_TAG
        imagePullPolicy: Never
        ports:
        - containerPort: 3000
        env:
        - name: NEXT_PUBLIC_API_URL
          value: "http://triage-service:8000"
---
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
  namespace: $NAMESPACE
spec:
  type: NodePort
  selector:
    app: frontend
  ports:
  - port: 3000
    targetPort: 3000
    nodePort: 30080
EOF

echo "Waiting for frontend pod to be ready..."
kubectl rollout status deployment/frontend -n $NAMESPACE --timeout=3m

echo "✓ Next.js frontend deployed — access at: $(minikube ip):30080"
