---
name: auth-access-control-system
description: Manage feature access for authenticated and non-authenticated users across UI, backend, and agents
---

# Auth Access Control System

## Purpose
Define and enforce differences between guest users and authenticated users.

---

## User Types

### 1. Guest (Non-authenticated)
- Temporary session
- No persistent storage
- Limited feature access

### 2. Authenticated User
- Logged-in user
- Full access
- Persistent data and personalization

---

## Access Rules

### Guest محدود access

Allow:
- View Home, About, Contact pages
- Generate limited concepts (max 2 per session)
- Generate limited exercises (max 2 per session)

Restrict:
- No progress tracking
- No saved data
- No dashboard access (show demo only)
- No history

---

### Authenticated Full access

Allow:
- Unlimited concept generation
- Unlimited exercises
- Dashboard with real data
- Progress tracking
- Save concepts and exercises
- Personalized experience

---

## UI Behavior

### For Guests:
- Show locked features with blur/overlay
- Display CTA: "Sign up to unlock"
- Show demo data in dashboard

### Locked Feature UI:
- Blur cards or sections
- Add lock icon 🔒
- Show upgrade modal

---

## Modal Example

Title:
🔒 Unlock Full Learning Experience

Content:
- Track your progress
- Unlimited exercises
- Save your work

CTA:
[ Sign Up Free ]

---

## Backend Logic

- Identify user via auth token/session
- If guest:
  - Apply rate limits
  - Do NOT store data
- If authenticated:
  - Enable full database writes
  - Enable progress tracking

---

## Agent Behavior

### Guest Mode:
- Stateless responses
- No event publishing (or minimal)

### Auth Mode:
- Enable event-driven flow (Kafka/Dapr)
- Publish progress events
- Store results

---

## Middleware Rules

Implement:
- Auth middleware to detect user type
- Access control layer before agent execution

---

## Rate Limiting

Guest:
- Max 2–3 requests per feature

Authenticated:
- No strict limit (or higher threshold)

---

## Instructions

1. Add auth check middleware
2. Implement feature gating logic
3. Update UI for locked features
4. Add upgrade/sign-up prompts
5. Connect backend with user state
6. Ensure agents behave based on user type

---

## Validation Checklist

- [ ] Guest limits enforced
- [ ] Auth users have full access
- [ ] Locked UI visible for guests
- [ ] Modal prompts working
- [ ] Backend respects auth state
- [ ] Agents adapt behavior

---

## Output Expectation

- Clear separation between guest and authenticated flows
- Improved user conversion
- Scalable access control system