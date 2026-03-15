#!/usr/bin/env python3
"""Verify PostgreSQL pods are running in the postgres namespace."""

import subprocess
import json
import sys

def verify():
    result = subprocess.run(
        ["kubectl", "get", "pods", "-n", "postgres", "-o", "json"],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        print(f"✗ kubectl error: {result.stderr.strip()}")
        sys.exit(1)

    pods = json.loads(result.stdout).get("items", [])
    if not pods:
        print("✗ No pods found in postgres namespace")
        sys.exit(1)

    running = sum(1 for p in pods if p["status"].get("phase") == "Running")
    total = len(pods)

    if running == total:
        print(f"✓ All {total} PostgreSQL pods running")
    else:
        print(f"✗ {running}/{total} PostgreSQL pods running")
        sys.exit(1)

if __name__ == "__main__":
    verify()
