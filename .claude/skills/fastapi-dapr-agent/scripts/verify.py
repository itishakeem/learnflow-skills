#!/usr/bin/env python3
"""Verify a FastAPI + Dapr service is running in the learnflow namespace."""

import subprocess
import json
import sys

def verify(service_name=None):
    namespace = "learnflow"

    result = subprocess.run(
        ["kubectl", "get", "pods", "-n", namespace, "-o", "json"],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        print(f"✗ kubectl error: {result.stderr.strip()}")
        sys.exit(1)

    pods = json.loads(result.stdout).get("items", [])

    if service_name:
        pods = [p for p in pods if service_name in p["metadata"]["name"]]

    if not pods:
        label = f"'{service_name}'" if service_name else "any"
        print(f"✗ No pods found for {label} in {namespace} namespace")
        sys.exit(1)

    running = sum(1 for p in pods if p["status"].get("phase") == "Running")
    total = len(pods)

    if running == total:
        print(f"✓ All {total} pod(s) running in {namespace}")
    else:
        print(f"✗ {running}/{total} pods running in {namespace}")
        sys.exit(1)

    # Check Dapr sidecar
    for pod in pods:
        containers = [c["name"] for c in pod["spec"]["containers"]]
        if "daprd" in containers:
            print(f"✓ Dapr sidecar injected in {pod['metadata']['name']}")
        else:
            print(f"⚠ Dapr sidecar not found in {pod['metadata']['name']}")

if __name__ == "__main__":
    service_name = sys.argv[1] if len(sys.argv) > 1 else None
    verify(service_name)
