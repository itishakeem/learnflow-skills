#!/usr/bin/env python3
"""Run database migrations for LearnFlow on Kubernetes PostgreSQL."""

import subprocess
import sys

NAMESPACE = "postgres"
SECRET_NAME = "postgres-postgresql"

MIGRATIONS = [
    """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255) UNIQUE NOT NULL,
        role VARCHAR(50) NOT NULL DEFAULT 'student',
        created_at TIMESTAMP DEFAULT NOW()
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS progress (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        module INTEGER NOT NULL,
        topic VARCHAR(255) NOT NULL,
        mastery_score FLOAT DEFAULT 0.0,
        updated_at TIMESTAMP DEFAULT NOW()
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS code_submissions (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        code TEXT NOT NULL,
        result TEXT,
        passed BOOLEAN,
        submitted_at TIMESTAMP DEFAULT NOW()
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS exercises (
        id SERIAL PRIMARY KEY,
        module INTEGER NOT NULL,
        topic VARCHAR(255) NOT NULL,
        prompt TEXT NOT NULL,
        solution TEXT,
        difficulty VARCHAR(50) DEFAULT 'beginner'
    );
    """
]

def get_postgres_password():
    result = subprocess.run(
        ["kubectl", "get", "secret", SECRET_NAME, "-n", NAMESPACE,
         "-o", "jsonpath={.data.postgres-password}"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"✗ Could not get PostgreSQL password: {result.stderr.strip()}")
        sys.exit(1)

    import base64
    return base64.b64decode(result.stdout).decode()

def run_migration(sql, index):
    password = get_postgres_password()
    pod = f"{SECRET_NAME}-0"

    result = subprocess.run(
        ["kubectl", "exec", "-n", NAMESPACE, pod, "--",
         "psql", "-U", "postgres", "-d", "learnflow", "-c", sql],
        capture_output=True, text=True,
        env={**__import__("os").environ, "PGPASSWORD": password}
    )
    if result.returncode != 0:
        print(f"✗ Migration {index} failed: {result.stderr.strip()}")
        sys.exit(1)
    print(f"✓ Migration {index} applied")

if __name__ == "__main__":
    print("Running LearnFlow database migrations...")
    for i, sql in enumerate(MIGRATIONS, 1):
        run_migration(sql, i)
    print("✓ All migrations completed")
