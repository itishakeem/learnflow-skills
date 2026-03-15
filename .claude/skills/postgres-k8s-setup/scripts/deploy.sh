#!/bin/bash
set -e

NAMESPACE="postgres"
RELEASE_NAME="postgres"

echo "Adding Bitnami Helm repo..."
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

echo "Creating namespace '$NAMESPACE'..."
kubectl create namespace $NAMESPACE --dry-run=client -o yaml | kubectl apply -f -

echo "Installing PostgreSQL via Helm..."
helm upgrade --install $RELEASE_NAME bitnami/postgresql \
  --namespace $NAMESPACE \
  --set auth.postgresPassword=learnflow_password \
  --set auth.database=learnflow \
  --set primary.persistence.size=2Gi \
  --wait --timeout=5m

echo "✓ PostgreSQL deployed to namespace '$NAMESPACE'"
