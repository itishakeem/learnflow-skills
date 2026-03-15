#!/bin/bash
set -e

NAMESPACE="kafka"
BOOTSTRAP="kafka.kafka.svc.cluster.local:9092"

TOPICS=(
  "learning.events"
  "code.submissions"
  "exercise.events"
  "struggle.alerts"
)

for TOPIC in "${TOPICS[@]}"; do
  echo "Creating topic: $TOPIC"
  kubectl exec -n $NAMESPACE kafka-0 -- \
    kafka-topics.sh --create \
    --if-not-exists \
    --topic "$TOPIC" \
    --bootstrap-server localhost:9092 \
    --partitions 1 \
    --replication-factor 1
done

echo "✓ All LearnFlow Kafka topics created"
