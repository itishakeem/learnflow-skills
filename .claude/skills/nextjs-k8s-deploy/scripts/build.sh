#!/bin/bash
set -e

SERVICE_DIR="${1:-frontend}"
IMAGE_NAME="${2:-learnflow-frontend}"
IMAGE_TAG="${3:-latest}"

echo "Building Next.js Docker image: $IMAGE_NAME:$IMAGE_TAG"

# Point Docker to Minikube's daemon so image is available in cluster
eval $(minikube docker-env)

docker build -t "$IMAGE_NAME:$IMAGE_TAG" "$SERVICE_DIR"

echo "✓ Docker image '$IMAGE_NAME:$IMAGE_TAG' built successfully"
