# Build Script — Auth Access Control System

Step-by-step prompts to implement guest vs authenticated access control.

---

## Step 1 — Auth Context

```
Create lib/auth.tsx with:
- User interface: { id, name, email }
- GUEST_LIMITS constant: { concepts: 3, exercises: 3 }
- AuthProvider component with state: user, usage { concepts, exercises }
- login(user) — sets user, saves to localStorage
- logout() — clears user and localStorage
- consumeGuestUsage(feature) — returns false if limit reached, increments counter and returns true otherwise
- isGuest computed as user === null
- useEffect to restore session from localStorage on mount
- useAuth() hook that throws if used outside provider
Export: AuthProvider, useAuth, GUEST_LIMITS, User
```

---

## Step 2 — LockedOverlay Component

```
Create components/auth/GuestGate.tsx with LockedOverlay:
- Props: locked (boolean), title (string), onUnlock (() => void), children
- When locked=false: render children as-is
- When locked=true:
  - Wrap children in blur-sm + pointer-events-none div
  - Overlay with Lock icon, title text, and "Sign up free" button
  - Center overlay absolutely over the blurred content
  - Button calls onUnlock on click
```

---

## Step 3 — UpgradeModal Component

```
Add UpgradeModal to components/auth/GuestGate.tsx:
- Props: onClose (() => void)
- Full-screen backdrop: fixed inset-0, bg-black/60, backdrop-blur-sm
- Click backdrop to close
- Centered card with:
  - Lock emoji + "Unlock Full Access" heading
  - 4 benefit bullet points (unlimited concepts, exercises, progress, save work)
  - "Sign Up Free" link button pointing to /signup
  - "Continue as guest" dismiss text button
- Animate with Framer Motion scale + opacity on mount/unmount
```

---

## Step 4 — GuestUsageBadge Component

```
Create components/auth/GuestUsageBadge.tsx:
- Props: feature ("concepts" | "exercises")
- Import useAuth and GUEST_LIMITS
- If user is authenticated: render nothing (return null)
- If guest: show "N/max free" pill in neutral style
- If limit reached: show "🔒 Limit reached" pill in danger/red style
```

---

## Step 5 — Wire AuthProvider into Layout

```
Update app/layout.tsx:
- Import AuthProvider from lib/auth
- Wrap entire app content with <AuthProvider>
- Place it as the outermost provider (outside GamificationProvider if present)
```

---

## Step 6 — Gate Concepts Page

```
Update app/concepts/page.tsx:
- Import useAuth, GUEST_LIMITS from lib/auth
- Import GuestUsageBadge, UpgradeModal from components/auth/GuestGate
- Add showModal state
- Add limitReached computed: isGuest && usage.concepts >= GUEST_LIMITS.concepts
- In handleExplain: call consumeGuestUsage("concepts") — if false, setShowModal(true) and return
- Add <UpgradeModal> in JSX when showModal is true
- Add <GuestUsageBadge feature="concepts" /> in page header area
- Show guest warning banner with remaining usage count
```

---

## Step 7 — Gate Exercise Page

```
Update app/exercise/page.tsx:
- Import useAuth, GUEST_LIMITS from lib/auth
- Import GuestUsageBadge, UpgradeModal from components/auth/GuestGate
- Add showModal state, limitReached computed
- In handleGenerate: call consumeGuestUsage("exercises") — if false show modal and return
- Add <UpgradeModal> in JSX when showModal is true
- Add <GuestUsageBadge feature="exercises" /> in toolbar
- Disable generate button and show "🔒 Limit reached" label when limitReached
```

---

## Step 8 — Lock Dashboard for Guests

```
Update app/dashboard/page.tsx:
- Import LockedOverlay, UpgradeModal from components/auth/GuestGate
- For guests: show DEMO_PROGRESS data instead of calling the API
- Wrap "Recent Activity" section with <LockedOverlay locked={isGuest}>
- Show guest demo banner at top of dashboard
- Add upgrade modal trigger for locked sections
```

---

## Step 9 — Middleware (Optional)

```
Create middleware.ts in the project root:
- Import NextRequest, NextResponse from next/server
- Check for learnflow_user cookie on /dashboard routes
- Redirect to /login if unauthenticated and accessing protected route
- Export config matcher: ["/dashboard/:path*"]
```

---

## Step 10 — Validation

```
Test the following scenarios:
1. As guest: use concepts 3 times → modal appears on 4th attempt
2. As guest: dashboard shows demo data + locked overlay on recent activity
3. As authenticated: no limits enforced anywhere
4. Refresh page → user session restores from localStorage
5. Logout → user cleared, guest mode resumes
```

---

## Validation Checklist

- [ ] Guest limited to 3 concepts and 3 exercises per session
- [ ] UpgradeModal appears when limit is hit
- [ ] LockedOverlay blurs dashboard recent activity for guests
- [ ] GuestUsageBadge shows correct remaining count
- [ ] Authenticated users have unlimited access
- [ ] Session persists across page refresh
- [ ] Logout clears session correctly
