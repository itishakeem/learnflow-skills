# Build Script — Auth UI Builder

Step-by-step prompts to build login and signup pages.

---

## Step 1 — AuthCard Component

```
Create components/auth/AuthCard.tsx with:
- Props: title (string), subtitle (string), children
- Centered card layout: max-w-md, mx-auto
- Dark glass style: bg-surface-raised, border border-surface-border, rounded-2xl, shadow-card
- Title: text-2xl font-bold text-ink-primary
- Subtitle: text-sm text-ink-tertiary below title
- Children rendered below the heading block
- Fade-in + slide-up animation with Framer Motion on mount
```

---

## Step 2 — SocialButton Component

```
Create components/auth/SocialButton.tsx with:
- Props: provider ("google" | "github")
- For Google: show Google "G" colored icon + "Continue with Google"
- For GitHub: show GitHub mark icon + "Continue with GitHub"
- Style: full-width, bg-surface-raised, border border-surface-border, rounded-xl
- Hover: border-brand/30 + slight scale (1.01)
- onClick: placeholder (no backend yet — just UI)
```

---

## Step 3 — AuthDivider Component

```
Create components/auth/AuthDivider.tsx with:
- Horizontal rule with "or continue with" text centered
- Line color: surface-border
- Text: text-2xs text-ink-disabled uppercase tracking-widest
- Layout: flex items-center gap-3, lines grow with flex-1
```

---

## Step 4 — Login Page

```
Create app/login/page.tsx with:
- Full-height centered layout: min-h-screen flex items-center justify-center
- Use AuthCard with title "Welcome back" + subtitle "Sign in to your account"
- Form fields inside card:
  - Email input with Mail icon
  - Password input with Lock icon + show/hide toggle (Eye/EyeOff)
  - "Remember me" checkbox + "Forgot password?" link (right-aligned)
  - "Sign In" primary gradient button (full width)
- AuthDivider between form and social buttons
- Two SocialButtons: Google + GitHub (side by side)
- "Don't have an account? Sign up" link at bottom pointing to /signup
- Fade-in animation on the card
```

---

## Step 5 — Signup Page

```
Create app/signup/page.tsx with:
- Same centered layout as login page
- Use AuthCard with title "Create your account" + subtitle "Start learning Python today"
- Form fields inside card:
  - Name input with User icon
  - Email input with Mail icon
  - Password input with Lock icon + show/hide toggle
  - "I agree to the Terms & Conditions" checkbox (required)
  - "Create Account" primary gradient button (full width)
- AuthDivider between form and social buttons
- Two SocialButtons: Google + GitHub (side by side)
- "Already have an account? Sign in" link at bottom pointing to /login
- Same fade-in animation
```

---

## Step 6 — PasswordInput Enhancement

```
Create components/auth/PasswordInput.tsx:
- Extends the base Input component
- Adds show/hide toggle button inside the input (Eye/EyeOff icons from lucide-react)
- Toggles input type between "password" and "text" on click
- Icon button: absolute right-3, p-1.5, text-ink-disabled hover:text-ink-secondary
Use this component for all password fields on login and signup pages
```

---

## Step 7 — Form Input Enhancements

```
Ensure components/ui/Input.tsx supports:
- label prop: renders label above input
- leftIcon prop: renders icon inside left edge of input
- error prop: renders red error message below input
- Focus glow: focus:ring-2 focus:ring-brand/20 focus:border-brand/60
- Disabled state: opacity-50 cursor-not-allowed
```

---

## Step 8 — Responsive Polish

```
Final polish pass on both pages:
1. Test on mobile (< 640px): card should use full width with px-4 margin
2. Ensure all inputs are touch-friendly (min height 44px)
3. Add smooth transition on social buttons hover
4. Verify "Tab" key navigation works across all form fields
5. Verify Enter key submits the form
```

---

## Validation Checklist

- [ ] Login page renders with email, password, remember me, forgot password
- [ ] Signup page renders with name, email, password, terms checkbox
- [ ] Both pages show Google + GitHub social buttons
- [ ] Password show/hide toggle works
- [ ] Navigation links between login ↔ signup work
- [ ] AuthCard animation plays on page load
- [ ] Pages are fully responsive on mobile
- [ ] Tab navigation works through all form fields
