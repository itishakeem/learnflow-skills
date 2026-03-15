#!/usr/bin/env python3
"""Verify Kafka pods are running in the kafka namespace."""

import subprocess
import json
import sys

def verify():
    result = subprocess.run(
        ["kubectl", "get", "pods", "-n", "kafka", "-o", "json"],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        print(f"✗ kubectl error: {result.stderr.strip()}")
        sys.exit(1)

    pods = json.loads(result.stdout).get("items", [])
    if not pods:
        print("✗ No pods found in kafka namespace")
        sys.exit(1)

    running = sum(1 for p in pods if p["status"].get("phase") == "Running")
    total = len(pods)

    if running == total:
        print(f"✓ All {total} Kafka pods running")
    else:
        print(f"✗ {running}/{total} Kafka pods running")
        sys.exit(1)

if __name__ == "__main__":
    verify()
