# Build Script — Basic Auth System

Step-by-step prompts to implement signup, login, and session.

---

## Step 1 — Auth Service (Backend)

```
Create services/auth/main.py with FastAPI:
- POST /signup: accepts name, email, password
  - Validate password: min 8 chars, must contain letters and numbers
  - Hash password with salt + SHA256 (format: "salt:hash")
  - Store user in dict keyed by email
  - Return 409 if email already exists
  - Return { status: "ok", user: { id, name, email } }
- POST /login: accepts email, password
  - Look up user by email
  - Verify hashed password
  - Return 401 if not found or password wrong
  - Return { status: "ok", user: { id, name, email } }
Create services/auth/requirements.txt: fastapi, uvicorn, pydantic[email]
Create services/auth/Dockerfile following the same pattern as other services
```

---

## Step 2 — Auth API Proxy Route

```
Update app/api/svc/[service]/[...path]/route.ts:
- Add "auth" entry to SERVICE_URLS map pointing to http://auth:8000
  (or http://localhost:8006 for local dev)
- This allows /api/svc/auth/signup and /api/svc/auth/login to proxy correctly
```

---

## Step 3 — AuthProvider (Client)

```
Create lib/auth.tsx with:
- User interface: { id: string; name: string; email: string }
- AuthProvider with useState for user (null = guest)
- login(user): saves to state + localStorage "learnflow_user"
- logout(): clears state + localStorage
- useEffect to restore session from localStorage on mount
- isGuest computed as user === null
- Export AuthProvider, useAuth hook
Wrap app/layout.tsx with <AuthProvider>
```

---

## Step 4 — Signup Page

```
Create app/signup/page.tsx with:
- Form fields: Name, Email, Password, Confirm Password
- Client-side validation before submit:
  - Password >= 8 characters
  - Password contains at least one letter and one number
  - Password matches Confirm Password
  - Show inline error message if validation fails
- On valid submit: POST to /api/svc/auth/signup
- On success: call login(data.user) then router.push("/dashboard")
- On API error: show error message from response
- Link to /login at the bottom
Apply modern-ui-system styles (AuthCard, Input, Button components)
```

---

## Step 5 — Login Page

```
Create app/login/page.tsx with:
- Form fields: Email, Password
- On submit: POST to /api/svc/auth/login
- On success: call login(data.user) then router.push("/dashboard")
- On 401: show "Invalid email or password" error
- Link to /signup at the bottom
Apply modern-ui-system styles matching signup page
```

---

## Step 6 — Dashboard Welcome Message

```
Update app/dashboard/page.tsx:
- Import useAuth from lib/auth
- Destructure user from useAuth()
- In the page header, show: "Welcome, {user.name} 👋" when user is logged in
- Keep existing guest/demo handling for non-authenticated users
```

---

## Step 7 — Logout Button

```
Update components/Nav.tsx:
- Import useAuth
- Show user's name in the nav when logged in
- Add logout button (LogOut icon) that calls logout() and redirects to /
- For guests: show Login and Sign Up buttons
```

---

## Step 8 — Validation

```
Test all scenarios:
1. Signup with weak password → client error shown
2. Signup with mismatched passwords → client error shown
3. Signup with duplicate email → API 409 error shown
4. Successful signup → redirected to dashboard with name shown
5. Login with wrong password → 401 error shown
6. Successful login → redirected to dashboard
7. Refresh page → session restored from localStorage
8. Logout → redirected to home, guest mode
```

---

## Validation Checklist

- [ ] Signup validates password strength client-side
- [ ] Signup validates password confirmation match
- [ ] Duplicate email shows error
- [ ] Passwords hashed on backend (never stored plain)
- [ ] Login with wrong credentials returns 401
- [ ] Successful auth redirects to dashboard
- [ ] User name shown on dashboard after login
- [ ] Session restores on page refresh
- [ ] Logout clears session and redirects
