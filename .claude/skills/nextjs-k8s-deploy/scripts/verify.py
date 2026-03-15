#!/usr/bin/env python3
"""Verify Next.js frontend deployment is running in Kubernetes."""

import subprocess
import json
import sys

def verify():
    namespace = "learnflow"

    result = subprocess.run(
        ["kubectl", "get", "pods", "-n", namespace, "-l", "app=frontend", "-o", "json"],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        print(f"✗ kubectl error: {result.stderr.strip()}")
        sys.exit(1)

    pods = json.loads(result.stdout).get("items", [])
    if not pods:
        print(f"✗ No frontend pods found in {namespace} namespace")
        sys.exit(1)

    running = sum(1 for p in pods if p["status"].get("phase") == "Running")
    total = len(pods)

    if running == total:
        print(f"✓ All {total} frontend pod(s) running")
    else:
        print(f"✗ {running}/{total} frontend pods running")
        sys.exit(1)

    # Get NodePort URL
    svc_result = subprocess.run(
        ["kubectl", "get", "svc", "frontend-service", "-n", namespace,
         "-o", "jsonpath={.spec.ports[0].nodePort}"],
        capture_output=True, text=True
    )
    ip_result = subprocess.run(["minikube", "ip"], capture_output=True, text=True)

    if svc_result.returncode == 0 and ip_result.returncode == 0:
        print(f"✓ Frontend accessible at http://{ip_result.stdout.strip()}:{svc_result.stdout.strip()}")

if __name__ == "__main__":
    verify()
