# Advanced UI Enhancements - Reference

## Dependency
Requires: modern-ui-system

---

## File Structure (Scaffolded)

```
app/
├── layout.tsx                     # Global layout wrapper with shared background
├── dashboard/page.tsx             # Enhanced with glow cards + animated counters
├── concepts/page.tsx              # Structured layout + copy/regenerate buttons
└── exercise/page.tsx              # Improved cards + show solution toggle

components/
└── ui/
    ├── GlowCard.tsx               # Glass/glow card with hover lift effect
    ├── LoadingSkeleton.tsx        # Shimmer skeleton for loading states
    └── PageTransition.tsx         # Framer Motion page wrapper

styles/
└── globals.css                    # Global background + glow utility classes
```

---

## Global Background — `app/layout.tsx`

```tsx
// Apply consistent dark gradient background across all pages
<body className="min-h-screen bg-surface text-ink-primary antialiased"
  style={{ background: "linear-gradient(180deg, #0a0a0f 0%, #050508 100%)" }}
>
```

---

## GlowCard Component

```tsx
// components/ui/GlowCard.tsx
"use client";
import { motion } from "framer-motion";

interface GlowCardProps {
  children: React.ReactNode;
  color?: "brand" | "accent" | "success" | "warning";
  className?: string;
}

const GLOW = {
  brand:   { bg: "rgba(139,92,246,0.08)",  border: "rgba(139,92,246,0.2)",  shadow: "rgba(139,92,246,0.12)"  },
  accent:  { bg: "rgba(34,211,238,0.08)",  border: "rgba(34,211,238,0.2)",  shadow: "rgba(34,211,238,0.12)"  },
  success: { bg: "rgba(52,211,153,0.08)",  border: "rgba(52,211,153,0.2)",  shadow: "rgba(52,211,153,0.12)"  },
  warning: { bg: "rgba(245,158,11,0.08)",  border: "rgba(245,158,11,0.2)",  shadow: "rgba(245,158,11,0.12)"  },
};

export function GlowCard({ children, color = "brand", className = "" }: GlowCardProps) {
  const g = GLOW[color];
  return (
    <motion.div
      whileHover={{ scale: 1.02 }}
      transition={{ type: "spring", stiffness: 400, damping: 25 }}
      className={`rounded-2xl p-6 backdrop-blur-sm ${className}`}
      style={{
        background: `linear-gradient(135deg, ${g.bg} 0%, transparent 100%)`,
        border: `1px solid ${g.border}`,
        boxShadow: `0 0 30px ${g.shadow}, 0 2px 16px rgba(0,0,0,0.3)`,
      }}
    >
      {children}
    </motion.div>
  );
}
```

---

## LoadingSkeleton Component

```tsx
// components/ui/LoadingSkeleton.tsx
export function LoadingSkeleton({ lines = 4 }: { lines?: number }) {
  return (
    <div className="space-y-3 animate-pulse">
      {Array.from({ length: lines }).map((_, i) => (
        <div
          key={i}
          className="h-3 rounded-lg bg-surface-border"
          style={{ width: `${60 + Math.random() * 40}%` }}
        />
      ))}
    </div>
  );
}
```

---

## Code Editor Themes

```tsx
// In exercise/page.tsx — define themes for Monaco Editor
const EDITOR_THEMES = [
  { id: "vs-dark",  label: "Dark",    bg: "#1e1e1e" },
  { id: "dracula",  label: "Dracula", bg: "#282a36" },
  { id: "monokai",  label: "Monokai", bg: "#272822" },
  { id: "light",    label: "Light",   bg: "#ffffff" },
];

// Persist to localStorage:
const THEME_KEY = "learnflow_editor_theme";
localStorage.setItem(THEME_KEY, selectedTheme);
const saved = localStorage.getItem(THEME_KEY);
```

---

## Glow Utility Classes (globals.css)

```css
/* Add to globals.css */
.glow-brand  { box-shadow: 0 0 24px rgba(139,92,246,0.22); }
.glow-accent { box-shadow: 0 0 20px rgba(34,211,238,0.18); }
.glow-success{ box-shadow: 0 0 20px rgba(52,211,153,0.18); }

.hover-lift {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.hover-lift:hover {
  transform: translateY(-2px) scale(1.01);
}

.skeleton {
  background: linear-gradient(90deg, #1a1a2e 25%, #1f1f35 50%, #1a1a2e 75%);
  background-size: 200% 100%;
  animation: shimmer 1.8s linear infinite;
}

@keyframes shimmer {
  from { background-position: -200% 0; }
  to   { background-position:  200% 0; }
}
```

---

## Micro-interactions Pattern

```tsx
// Button ripple / scale on click
<motion.button
  whileHover={{ scale: 1.03 }}
  whileTap={{ scale: 0.97 }}
  transition={{ type: "spring", stiffness: 500, damping: 20 }}
>

// Answer feedback glow — correct
<div className="border border-success/40 shadow-[0_0_20px_rgba(52,211,153,0.2)]" />

// Answer feedback glow — incorrect
<div className="border border-danger/40 shadow-[0_0_20px_rgba(239,68,68,0.2)]" />
```

---

## Animated Counter Hook

```ts
// hooks/useCountUp.ts
import { useState, useEffect, useRef } from "react";

export function useCountUp(target: number, duration = 1200): number {
  const [count, setCount] = useState(0);
  const raf = useRef<number | null>(null);

  useEffect(() => {
    if (target === 0) { setCount(0); return; }
    let start: number | null = null;
    const easeOut = (t: number) => 1 - Math.pow(1 - t, 3);

    const step = (ts: number) => {
      if (!start) start = ts;
      const p = Math.min((ts - start) / duration, 1);
      setCount(Math.floor(easeOut(p) * target));
      if (p < 1) raf.current = requestAnimationFrame(step);
      else setCount(target);
    };
    raf.current = requestAnimationFrame(step);
    return () => { if (raf.current) cancelAnimationFrame(raf.current); };
  }, [target, duration]);

  return count;
}
```

---

## Dependencies

```bash
npm install framer-motion    # Animations + transitions
npm install lucide-react     # Icons
npm install @monaco-editor/react  # Code editor with theme support
```

---

## Validation Checklist

| Item | Check |
|------|-------|
| All pages share same dark background | [ ] |
| Dashboard cards have glow + hover lift | [ ] |
| Loading skeletons show before data | [ ] |
| Code editor has 4 theme options | [ ] |
| Theme persists in localStorage | [ ] |
| Buttons have scale micro-interaction | [ ] |
| Correct/incorrect answers glow green/red | [ ] |
| Counters animate on load | [ ] |
