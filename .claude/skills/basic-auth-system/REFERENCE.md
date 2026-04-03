# Basic Auth System - Reference

---

## File Structure (Scaffolded)

```
app/
├── login/page.tsx          # Login form (email + password)
└── signup/page.tsx         # Signup form (name + email + password + confirm)

services/
└── auth/
    └── main.py             # FastAPI auth service: /signup, /login endpoints

lib/
└── auth.tsx                # Client-side AuthProvider + useAuth hook
```

---

## Backend — FastAPI Auth Service

```python
# services/auth/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import hashlib, os
from datetime import datetime

app = FastAPI(title="auth", version="1.0.0")

# In-memory store (replace with PostgreSQL in production)
users_db: dict[str, dict] = {}

class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

def hash_password(password: str) -> str:
    salt = os.urandom(16).hex()
    hashed = hashlib.sha256(f"{salt}{password}".encode()).hexdigest()
    return f"{salt}:{hashed}"

def verify_password(password: str, stored: str) -> bool:
    salt, hashed = stored.split(":")
    return hashlib.sha256(f"{salt}{password}".encode()).hexdigest() == hashed

@app.post("/signup")
def signup(req: SignupRequest):
    if req.email in users_db:
        raise HTTPException(status_code=409, detail="Email already registered")
    if len(req.password) < 8:
        raise HTTPException(status_code=422, detail="Password must be at least 8 characters")
    if not any(c.isalpha() for c in req.password) or not any(c.isdigit() for c in req.password):
        raise HTTPException(status_code=422, detail="Password must include letters and numbers")

    user_id = f"user-{len(users_db) + 1}"
    users_db[req.email] = {
        "id": user_id, "name": req.name,
        "email": req.email, "password": hash_password(req.password),
        "created_at": datetime.utcnow().isoformat(),
    }
    return {"status": "ok", "user": {"id": user_id, "name": req.name, "email": req.email}}

@app.post("/login")
def login(req: LoginRequest):
    user = users_db.get(req.email)
    if not user or not verify_password(req.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"status": "ok", "user": {"id": user["id"], "name": user["name"], "email": user["email"]}}
```

---

## Frontend — Signup Page

```tsx
// app/signup/page.tsx  (key logic)
"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/lib/auth";

export default function SignupPage() {
  const router = useRouter();
  const { login } = useAuth();
  const [form, setForm] = useState({ name: "", email: "", password: "", confirm: "" });
  const [error, setError] = useState("");

  function validate() {
    if (form.password.length < 8)          return "Password must be at least 8 characters";
    if (!/[a-zA-Z]/.test(form.password))   return "Password must include letters";
    if (!/[0-9]/.test(form.password))      return "Password must include numbers";
    if (form.password !== form.confirm)    return "Passwords do not match";
    return null;
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    const err = validate();
    if (err) { setError(err); return; }

    const res = await fetch("/api/svc/auth/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: form.name, email: form.email, password: form.password }),
    });
    const data = await res.json();
    if (!res.ok) { setError(data.detail); return; }
    login(data.user);
    router.push("/dashboard");
  }
  // ... render form
}
```

---

## Frontend — Login Page

```tsx
// app/login/page.tsx  (key logic)
async function handleLogin(e: React.FormEvent) {
  e.preventDefault();
  const res = await fetch("/api/svc/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  const data = await res.json();
  if (!res.ok) { setError("Invalid email or password"); return; }
  login(data.user);
  router.push("/dashboard");
}
```

---

## Validation Rules

| Rule | Detail |
|------|--------|
| Password length | Minimum 8 characters |
| Password content | Must contain letters AND numbers |
| Confirm password | Must match password field |
| Email format | Valid email format required |
| Duplicate email | Returns 409 on signup |

---

## Password Hashing

```python
# Salt + SHA256 (upgrade to bcrypt for production)
def hash_password(password: str) -> str:
    salt = os.urandom(16).hex()
    hashed = hashlib.sha256(f"{salt}{password}".encode()).hexdigest()
    return f"{salt}:{hashed}"
```

---

## Dashboard Welcome

```tsx
// app/dashboard/page.tsx
const { user } = useAuth();

// Show in header:
<h1>Welcome, {user?.name} 👋</h1>
```

---

## Dependencies

```bash
# Backend
pip install fastapi uvicorn pydantic[email]

# Frontend (already in project)
# useAuth from lib/auth.tsx
# next/navigation for redirect
```

---

## Validation Checklist

| Item | Check |
|------|-------|
| Signup form validates all fields client-side | [ ] |
| Password hashed before storage | [ ] |
| Duplicate email returns error | [ ] |
| Login with wrong password returns 401 | [ ] |
| Successful login redirects to dashboard | [ ] |
| Dashboard shows logged-in user name | [ ] |
| Session persists on page refresh | [ ] |
