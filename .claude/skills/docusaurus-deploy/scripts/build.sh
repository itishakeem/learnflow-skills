#!/bin/bash
set -e

DOCS_DIR="${1:-docs}"
IMAGE_NAME="${2:-learnflow-docs}"
IMAGE_TAG="${3:-latest}"

echo "Building Docusaurus Docker image: $IMAGE_NAME:$IMAGE_TAG"

# Create Dockerfile if it doesn't exist
if [ ! -f "$DOCS_DIR/Dockerfile" ]; then
  cat > "$DOCS_DIR/Dockerfile" <<DOCKERFILE
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
DOCKERFILE
  echo "✓ Dockerfile created in $DOCS_DIR"
fi

# Point Docker to Minikube's daemon
eval $(minikube docker-env)

docker build -t "$IMAGE_NAME:$IMAGE_TAG" "$DOCS_DIR"

echo "✓ Docusaurus image '$IMAGE_NAME:$IMAGE_TAG' built successfully"
