# Build Script — Advanced UI Enhancements

Step-by-step prompts to implement the full advanced UI system.

---

## Step 1 — Global Background Consistency

```
Update app/layout.tsx to apply a unified dark gradient background:
- Set body background to: linear-gradient(180deg, #0a0a0f 0%, #050508 100%)
- Ensure it covers all pages: dashboard, concepts, exercise
- Remove any page-level background overrides that conflict
```

---

## Step 2 — GlowCard Component

```
Create components/ui/GlowCard.tsx with:
- Props: children, color ("brand" | "accent" | "success" | "warning"), className
- Use Framer Motion whileHover scale: 1.02 with spring transition
- Apply colored gradient background + matching border + outer glow shadow
- Export as named export GlowCard
```

---

## Step 3 — LoadingSkeleton Component

```
Create components/ui/LoadingSkeleton.tsx with:
- Props: lines (number, default 4)
- Render N shimmer bars with varying widths (60%–100%)
- Use CSS keyframe shimmer animation: background slides left to right
- Apply bg-surface-border base color
```

---

## Step 4 — Add Shimmer + Glow Utilities to globals.css

```
Add to app/globals.css:
- .skeleton class: shimmer animation with gradient background
- @keyframes shimmer: background-position from -200% to 200%
- .hover-lift class: translateY(-2px) scale(1.01) on hover
- .glow-brand, .glow-accent, .glow-success utility box-shadow classes
```

---

## Step 5 — Dashboard Enhancement

```
Update app/dashboard/page.tsx to:
1. Replace plain stat cards with GlowCard components (brand/success/accent colors)
2. Add useCountUp hook to animate numbers from 0 to target on load
3. Add loading skeletons while data fetches
4. Add hover lift effect on quick action cards
5. Ensure all cards fade-in with staggered Framer Motion animation
```

---

## Step 6 — Concept Explainer Page Enhancement

```
Update app/concepts/page.tsx to:
1. Add copy-to-clipboard button on the explanation result card
2. Add Regenerate button next to the result header
3. Wrap result text in a reveal animation (opacity 0→1, y 8→0)
4. Add top gradient accent line above result card
5. Show LoadingSkeleton while explanation is loading
```

---

## Step 7 — Exercise Page Enhancement

```
Update app/exercise/page.tsx to:
1. Add show/hide solution toggle button with Eye/EyeOff icons
2. Add animated height collapse/expand for solution panel (AnimatePresence)
3. Add difficulty indicator badge on exercise card
4. Apply green glow on correct answer feedback, red glow on error
5. Add retry button after submission
```

---

## Step 8 — Code Editor Theme Switcher

```
Add to app/exercise/page.tsx:
1. Define EDITOR_THEMES array: vs-dark, dracula, monokai, light
2. Add defineCustomThemes(monaco) function for dracula + monokai token colors
3. Add theme picker dropdown button (Palette icon) in the toolbar
4. Use AnimatePresence for dropdown open/close animation
5. Persist selected theme to localStorage key "learnflow_editor_theme"
6. Load saved theme on mount with useEffect
```

---

## Step 9 — Micro-interactions

```
Apply across all interactive elements:
1. Buttons: add whileHover scale 1.03, whileTap scale 0.97 via Framer Motion
2. Cards: add hover:scale-[1.02] transition-all duration-300
3. Inputs: add focus glow ring using focus:ring-2 focus:ring-brand/20
4. Nav links: add smooth color transition on hover
5. Page transitions: wrap page content in motion.div with fade-in animation
```

---

## Step 10 — Validation

```
Run: npx tsc --noEmit
Check:
- All pages share the same background gradient
- Dashboard counters animate on load
- Skeleton shows while loading
- Code editor theme switcher works and persists
- Hover effects work on all cards and buttons
- Solution toggle works on exercise page
- Copy button works on concepts page
```

---

## Validation Checklist

- [ ] Global background consistent across all pages
- [ ] GlowCard component working with all 4 color variants
- [ ] LoadingSkeleton shimmer animation smooth
- [ ] Dashboard animated counters working
- [ ] Concept page copy + regenerate buttons functional
- [ ] Exercise page solution toggle functional
- [ ] Code editor supports 4 themes with persistence
- [ ] All buttons have micro-interaction scale effects
- [ ] TypeScript compiles clean
