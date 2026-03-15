#!/bin/bash
set -e

NAMESPACE="kafka"
RELEASE_NAME="kafka"

echo "Adding Bitnami Helm repo..."
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

echo "Creating namespace '$NAMESPACE'..."
kubectl create namespace $NAMESPACE --dry-run=client -o yaml | kubectl apply -f -

echo "Installing Kafka via Helm..."
helm upgrade --install $RELEASE_NAME bitnami/kafka \
  --namespace $NAMESPACE \
  --set replicaCount=1 \
  --set zookeeper.replicaCount=1 \
  --set persistence.size=2Gi \
  --wait --timeout=5m

echo "✓ Kafka deployed to namespace '$NAMESPACE'"
