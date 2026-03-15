#!/usr/bin/env python3
"""Analyze repository structure and output summary for AGENTS.md generation."""

import os
import sys
import json

def analyze(root="."):
    structure = {}
    ignored = {".git", "node_modules", "__pycache__", ".next", "dist", "build", "venv", ".venv"}

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ignored]
        rel = os.path.relpath(dirpath, root)
        if rel == ".":
            rel = "root"
        structure[rel] = filenames

    # Detect tech stack
    all_files = []
    for files in structure.values():
        all_files.extend(files)

    stack = []
    if "package.json" in all_files:
        stack.append("Node.js")
    if any(f.endswith(".py") for f in all_files):
        stack.append("Python")
    if "next.config.js" in all_files or "next.config.ts" in all_files:
        stack.append("Next.js")
    if any("fastapi" in f.lower() or "main.py" == f for f in all_files):
        stack.append("FastAPI")
    if any(f.endswith(".yaml") or f.endswith(".yml") for f in all_files):
        stack.append("Kubernetes/YAML")
    if "Dockerfile" in all_files:
        stack.append("Docker")

    result = {
        "root": root,
        "stack": stack,
        "top_level_dirs": [d for d in os.listdir(root)
                           if os.path.isdir(os.path.join(root, d)) and d not in ignored],
        "key_files": [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]
    }

    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    analyze(root)
