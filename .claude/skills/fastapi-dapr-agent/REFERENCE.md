# FastAPI + Dapr Agent Microservice - Reference

## Service Structure (Scaffolded)

```
services/<service-name>/
├── main.py           # FastAPI app + Dapr pub/sub handlers
├── Dockerfile        # Container image definition
└── requirements.txt  # Python dependencies
```

## Dapr Component Templates

### Kafka PubSub Component (`k8s/dapr/kafka-pubsub.yaml`)

```yaml
apiVersion: dapr.io/v1alpha1
kind: Component
metadata:
  name: kafka-pubsub
  namespace: default
spec:
  type: pubsub.kafka
  version: v1
  metadata:
  - name: brokers
    value: "kafka.kafka.svc.cluster.local:9092"
  - name: consumerGroup
    value: "learnflow"
```

## LearnFlow Agent Services

| Service | Kafka Topics (Subscribe) | Kafka Topics (Publish) |
|---------|--------------------------|------------------------|
| `triage` | `learning.events` | `learning.concepts`, `learning.debug` |
| `concepts` | `learning.concepts` | — |
| `debug` | `learning.debug` | — |
| `exercise` | `exercise.events` | — |
| `progress` | `learning.events`, `exercise.events` | `struggle.alerts` |

## Dapr Pub/Sub Pattern in FastAPI

```python
from fastapi import FastAPI
import httpx, os

app = FastAPI()
DAPR_PORT = os.getenv("DAPR_HTTP_PORT", "3500")

# Subscribe handler
@app.post("/learning-events")
async def handle_event(event: dict):
    # process event
    return {"status": "SUCCESS"}

# Publish event
async def publish(topic: str, data: dict):
    async with httpx.AsyncClient() as client:
        await client.post(
            f"http://localhost:{DAPR_PORT}/v1.0/publish/kafka-pubsub/{topic}",
            json=data
        )
```

## Script Reference

| Script | Purpose | Usage |
|--------|---------|-------|
| `scaffold.py` | Creates service directory with FastAPI + Dapr boilerplate | `python scripts/scaffold.py <service-name>` |
| `apply_dapr_components.sh` | Applies Dapr component YAMLs to cluster | `./scripts/apply_dapr_components.sh` |
| `verify.py` | Checks pod running and Dapr sidecar injected | `python scripts/verify.py <service-name>` |

## Kubernetes Deployment Annotations (Required for Dapr)

```yaml
annotations:
  dapr.io/enabled: "true"
  dapr.io/app-id: "<service-name>"
  dapr.io/app-port: "8000"
```

## Useful Commands

```bash
# Check Dapr sidecar injected
kubectl get pods -n default -o jsonpath='{.items[*].spec.containers[*].name}'

# View Dapr logs for a service
kubectl logs -n default <pod-name> -c daprd

# List Dapr components
kubectl get components -n default
```
