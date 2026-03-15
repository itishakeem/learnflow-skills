# Setup Backend Services

This recipe deploys all LearnFlow FastAPI microservices with Dapr sidecars.

## Steps

1. Create Triage Agent Service

Use skill: fastapi-dapr-agent

2. Create Concepts Agent Service

Use skill: fastapi-dapr-agent

3. Create Exercise Agent Service

Use skill: fastapi-dapr-agent

4. Setup MCP Code Execution

Use skill: mcp-code-execution

## Expected Result

All FastAPI agent microservices running in Kubernetes with Dapr pub/sub connected to Kafka topics.
