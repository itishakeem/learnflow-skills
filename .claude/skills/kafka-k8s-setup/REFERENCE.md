# Kafka Kubernetes Setup - Reference

## Helm Chart Configuration

- Chart: `bitnami/kafka`
- Namespace: `kafka`
- Default replica count: 1 (dev), 3 (prod)

## Key Helm Values

| Value | Default | Description |
|-------|---------|-------------|
| replicaCount | 1 | Number of Kafka brokers |
| zookeeper.replicaCount | 1 | Number of ZooKeeper nodes |
| persistence.size | 8Gi | Storage per broker |

## Kafka Topics for LearnFlow

| Topic | Purpose |
|-------|---------|
| learning.events | Student learning activity |
| code.submissions | Code execution results |
| exercise.events | Exercise completions |
| struggle.alerts | Struggle detection triggers |

## Useful Commands

```bash
# List topics
kubectl exec -n kafka kafka-0 -- kafka-topics.sh --list --bootstrap-server localhost:9092

# Create topic
kubectl exec -n kafka kafka-0 -- kafka-topics.sh --create --topic learning.events --bootstrap-server localhost:9092
```
