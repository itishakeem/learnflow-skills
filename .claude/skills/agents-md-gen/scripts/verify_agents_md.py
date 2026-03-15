#!/usr/bin/env python3
"""Verify AGENTS.md exists and has required sections."""

import os
import sys

REQUIRED_SECTIONS = ["## Repository Overview", "## Tech Stack", "## Directory Structure", "## Conventions"]

def verify(root="."):
    path = os.path.join(root, "AGENTS.md")

    if not os.path.exists(path):
        print(f"✗ AGENTS.md not found at {path}")
        sys.exit(1)

    with open(path) as f:
        content = f.read()

    missing = [s for s in REQUIRED_SECTIONS if s not in content]
    if missing:
        print(f"✗ AGENTS.md missing sections: {missing}")
        sys.exit(1)

    print(f"✓ AGENTS.md verified — all required sections present")

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    verify(root)
