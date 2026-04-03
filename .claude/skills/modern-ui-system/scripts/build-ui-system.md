# Build Script — Modern UI System

Step-by-step prompts to set up the global design system.

---

## Step 1 — Tailwind Config

```
Update tailwind.config.ts with:
- colors.surface: base (#050508), DEFAULT (#0a0a0f), raised (#0f0f18), border (#1a1a2e), hover (#13131e)
- colors.brand: full 50–900 scale + DEFAULT (#8b5cf6)
- colors.accent: light (#67e8f9), DEFAULT (#22d3ee), dark (#06b6d4)
- colors.success/warning/danger: each with DEFAULT, light, muted variants
- colors.ink: primary (#f0f0ff), secondary (#a0a0c0), tertiary (#60607a), disabled (#3e3e54)
- fontFamily.sans: ["Inter", "system-ui", "sans-serif"]
- fontFamily.mono: ["JetBrains Mono", "Fira Code", "Consolas", "monospace"]
- fontSize["2xs"]: ["0.625rem", { lineHeight: "1rem" }]
- boxShadow: glow-brand, glow-accent, glow-sm, card, card-hover, nav
- backgroundImage: gradient-brand, gradient-brand-v, gradient-surface, gradient-radial
- animation: fade-in, slide-up, slide-down, pulse-slow, shimmer, spin-slow
- keyframes for: fadeIn, slideUp, slideDown, shimmer
- borderRadius: 2xl (1rem), 3xl (1.5rem), 4xl (2rem)
- transitionTimingFunction: spring, smooth
```

---

## Step 2 — Global CSS

```
Update app/globals.css with:
- @import for Inter and JetBrains Mono from Google Fonts
- CSS custom properties on :root for all design tokens (--color-brand, etc.)
- Base body styles: bg-surface, text-ink-primary, antialiased
- .text-gradient class: background-clip text with brand gradient
- .bg-gradient-brand class: linear-gradient 135deg brand→accent
- .section-label class: text-2xs uppercase tracking-widest font-semibold
- .skeleton class: shimmer animation for loading states
- .tab-active / .tab-inactive classes for tab bar components
- .prose-dark class: readable text styling for long-form content
- .input-base class: shared input field styles
- Scrollbar styling: thin, dark-colored scrollbar
```

---

## Step 3 — Button Component

```
Create components/ui/Button.tsx with:
- Props: variant ("primary" | "secondary" | "ghost" | "warning" | "danger"), size ("sm" | "md" | "lg"), fullWidth, loading, disabled, children, onClick
- primary: bg-brand, hover:bg-brand-400, text-white, shadow-glow-sm on hover
- secondary: bg-surface-raised, border border-surface-border, text-ink-primary
- ghost: transparent background, text-ink-secondary, hover:bg-surface-raised
- warning: bg-warning/15, border-warning/30, text-warning-light
- danger: bg-danger/15, border-danger/30, text-danger-light
- loading: show spinner icon, disable pointer events
- All variants: rounded-xl, font-medium, transition-all duration-200
- Size sm: px-3 py-1.5 text-xs | md: px-4 py-2 text-sm | lg: px-5 py-2.5 text-sm
```

---

## Step 4 — Card Component

```
Create components/ui/Card.tsx with:
- Props: children, className, hover (boolean)
- Base: bg-surface-raised, border border-surface-border, rounded-2xl, shadow-card, p-6
- hover=true: adds hover:shadow-card-hover hover:border-brand/20 transition-all duration-300
- Export as default and named export
```

---

## Step 5 — Input Component

```
Create components/ui/Input.tsx with:
- Props: label, placeholder, value, onChange, onKeyDown, leftIcon, error, disabled, type
- Container: flex flex-col gap-1.5
- Label: text-xs font-medium text-ink-secondary
- Input wrapper: relative (for icon positioning)
- Input base: w-full bg-surface-base border border-surface-border rounded-xl
  px-3 py-2.5 text-sm text-ink-primary placeholder:text-ink-disabled
  focus:outline-none focus:border-brand/60 focus:ring-2 focus:ring-brand/15
  disabled:opacity-50 disabled:cursor-not-allowed
- leftIcon: absolute left-3 top-1/2 -translate-y-1/2, pl-9 on input when icon present
- error: text-xs text-danger-light below input
```

---

## Step 6 — Badge Component

```
Create components/ui/Badge.tsx with:
- Props: variant ("brand" | "success" | "warning" | "danger" | "neutral"), size ("sm" | "md"), children
- brand: bg-brand/10 text-brand-300 border-brand/20
- success: bg-success/10 text-success-light border-success/20
- warning: bg-warning/10 text-warning-light border-warning/20
- danger: bg-danger/10 text-danger-light border-danger/20
- neutral: bg-surface-raised text-ink-secondary border-surface-border
- All: inline-flex items-center rounded-lg border font-medium
- sm: px-2 py-0.5 text-2xs | md: px-2.5 py-1 text-xs
```

---

## Step 7 — Alert Component

```
Create components/ui/Alert.tsx with:
- Props: variant ("error" | "success" | "warning" | "info"), className, children
- error: bg-danger/10 border-danger/20 text-danger-light
- success: bg-success/10 border-success/20 text-success-light
- warning: bg-warning/10 border-warning/20 text-warning-light
- info: bg-brand/10 border-brand/20 text-brand-300
- Base: rounded-xl border px-4 py-3 text-sm
```

---

## Step 8 — Root Layout

```
Update app/layout.tsx with:
- <html lang="en" className="dark">
- <body className="bg-surface text-ink-primary min-h-screen antialiased">
- Import and render Navbar
- Wrap children in <main className="min-h-[calc(100vh-4rem)]">
- Import globals.css
- Set metadata: title and description
```

---

## Step 9 — Install Dependencies

```
Run in the frontend directory:
npm install framer-motion lucide-react
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p (if not already initialized)
```

---

## Step 10 — Validation

```
Run: npx tsc --noEmit
Visually check:
- Background is deep dark (#0a0a0f)
- Brand color (violet #8b5cf6) used on buttons and accents
- Accent color (cyan #22d3ee) used on secondary elements
- Cards have subtle border + glow shadow
- Inputs have focus ring matching brand color
- Badges render in all 5 variants
- Buttons render in all 5 variants at all 3 sizes
```

---

## Validation Checklist

- [ ] Tailwind config has all color tokens
- [ ] globals.css has section-label, skeleton, text-gradient utilities
- [ ] Button component has all 5 variants + loading state
- [ ] Card component with optional hover effect
- [ ] Input component with icon, label, error support
- [ ] Badge component with 5 variants and 2 sizes
- [ ] Alert component with 4 variants
- [ ] Root layout applies dark background globally
- [ ] TypeScript compiles clean
