#!/bin/bash
set -e

NAMESPACE="learnflow"

echo "Installing Dapr on Kubernetes..."
dapr init --kubernetes --wait

echo "Creating namespace '$NAMESPACE'..."
kubectl create namespace $NAMESPACE --dry-run=client -o yaml | kubectl apply -f -

echo "Applying Dapr Kafka pubsub component..."
cat <<EOF | kubectl apply -f -
apiVersion: dapr.io/v1alpha1
kind: Component
metadata:
  name: kafka-pubsub
  namespace: $NAMESPACE
spec:
  type: pubsub.kafka
  version: v1
  metadata:
  - name: brokers
    value: "kafka.kafka.svc.cluster.local:9092"
  - name: consumerGroup
    value: "learnflow"
  - name: authRequired
    value: "false"
EOF

echo "Applying Dapr state store component..."
cat <<EOF | kubectl apply -f -
apiVersion: dapr.io/v1alpha1
kind: Component
metadata:
  name: statestore
  namespace: $NAMESPACE
spec:
  type: state.postgresql
  version: v1
  metadata:
  - name: connectionString
    value: "host=postgres-postgresql.postgres.svc.cluster.local user=postgres password=learnflow_password dbname=learnflow sslmode=disable"
EOF

echo "✓ Dapr components applied to namespace '$NAMESPACE'"
