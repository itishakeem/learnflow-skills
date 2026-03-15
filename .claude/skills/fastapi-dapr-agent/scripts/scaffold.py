#!/usr/bin/env python3
"""Scaffold a FastAPI + Dapr microservice for LearnFlow."""

import os
import sys

def scaffold(service_name: str, port: int = 8000):
    base = os.path.join("services", service_name)
    os.makedirs(base, exist_ok=True)

    # main.py
    with open(os.path.join(base, "main.py"), "w") as f:
        f.write(f'''from fastapi import FastAPI
from dapr.clients import DaprClient
import uvicorn

app = FastAPI(title="{service_name}")

PUBSUB_NAME = "kafka-pubsub"

@app.get("/health")
def health():
    return {{"status": "ok", "service": "{service_name}"}}

@app.post("/invoke")
async def invoke(payload: dict):
    """Main agent invocation endpoint."""
    with DaprClient() as client:
        # Publish result event
        client.publish_event(
            pubsub_name=PUBSUB_NAME,
            topic_name="learning.events",
            data=str(payload)
        )
    return {{"result": "processed", "service": "{service_name}"}}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port={port})
''')

    # requirements.txt
    with open(os.path.join(base, "requirements.txt"), "w") as f:
        f.write("fastapi\nuvicorn\ndapr\nopenai\n")

    # Dockerfile
    with open(os.path.join(base, "Dockerfile"), "w") as f:
        f.write(f'''FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE {port}
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "{port}"]
''')

    # K8s deployment manifest
    k8s_dir = os.path.join("k8s", "services", service_name)
    os.makedirs(k8s_dir, exist_ok=True)

    with open(os.path.join(k8s_dir, "deployment.yaml"), "w") as f:
        f.write(f'''apiVersion: apps/v1
kind: Deployment
metadata:
  name: {service_name}
  namespace: learnflow
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {service_name}
  template:
    metadata:
      labels:
        app: {service_name}
      annotations:
        dapr.io/enabled: "true"
        dapr.io/app-id: "{service_name}"
        dapr.io/app-port: "{port}"
    spec:
      containers:
      - name: {service_name}
        image: {service_name}:latest
        imagePullPolicy: Never
        ports:
        - containerPort: {port}
---
apiVersion: v1
kind: Service
metadata:
  name: {service_name}
  namespace: learnflow
spec:
  selector:
    app: {service_name}
  ports:
  - port: {port}
    targetPort: {port}
''')

    print(f"✓ Scaffolded service '{service_name}' at {base}/")
    print(f"✓ K8s manifests at {k8s_dir}/")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scaffold.py <service-name> [port]")
        sys.exit(1)
    service_name = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
    scaffold(service_name, port)
