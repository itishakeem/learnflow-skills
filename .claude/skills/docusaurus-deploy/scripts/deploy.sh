#!/bin/bash
set -e

NAMESPACE="learnflow"
IMAGE_NAME="${1:-learnflow-docs}"
IMAGE_TAG="${2:-latest}"

echo "Creating namespace '$NAMESPACE'..."
kubectl create namespace $NAMESPACE --dry-run=client -o yaml | kubectl apply -f -

echo "Deploying Docusaurus docs to Kubernetes..."
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: docs
  namespace: $NAMESPACE
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
        image: $IMAGE_NAME:$IMAGE_TAG
        imagePullPolicy: Never
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: docs-service
  namespace: $NAMESPACE
spec:
  type: NodePort
  selector:
    app: docs
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30081
EOF

echo "Waiting for docs pod to be ready..."
kubectl rollout status deployment/docs -n $NAMESPACE --timeout=3m

echo "✓ Docusaurus docs deployed — access at: $(minikube ip):30081"
