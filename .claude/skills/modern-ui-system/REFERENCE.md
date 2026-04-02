# Modern UI System - Reference

## Component Structure (Scaffolded)

```
components/ui/
├── Navbar.tsx        # Top navigation bar with logo and links
├── Footer.tsx        # Page footer with social links
├── Button.tsx        # Primary, secondary, and gradient variants
├── Card.tsx          # Dark surface card with rounded corners
├── FormInput.tsx     # Input field with icon, label, error state
├── Badge.tsx         # Small pill for tags and status indicators
└── Sidebar.tsx       # Collapsible sidebar navigation

styles/
└── globals.css       # Dark theme baseline, font, body background
```

## Tailwind Config Extension

```ts
// tailwind.config.ts
import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        background: "#0B0F19",
        primary:    "#6366F1",
        accent:     "#22D3EE",
        highlight:  "#F59E0B",
        foreground: "#E5E7EB",
      },
    },
  },
  plugins: [],
};

export default config;
```

## Global CSS Baseline

```css
/* styles/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  background-color: #0B0F19;
  color: #E5E7EB;
  font-family: system-ui, sans-serif;
}
```

## Core Component Patterns

### Button
```tsx
// components/ui/Button.tsx
type Variant = "primary" | "secondary" | "gradient";

const variants: Record<Variant, string> = {
  primary:   "bg-primary text-white hover:bg-indigo-500",
  secondary: "border border-primary text-primary hover:bg-primary hover:text-white",
  gradient:  "bg-gradient-to-r from-primary to-accent text-white",
};

export function Button({ variant = "primary", children, ...props }) {
  return (
    <button
      className={`px-6 py-2 rounded-2xl font-semibold transition-all ${variants[variant]}`}
      {...props}
    >
      {children}
    </button>
  );
}
```

### Card
```tsx
// components/ui/Card.tsx
export function Card({ children, className = "" }) {
  return (
    <div className={`bg-[#111827] border border-white/10 rounded-2xl p-6 shadow-lg ${className}`}>
      {children}
    </div>
  );
}
```

### FormInput
```tsx
// components/ui/FormInput.tsx
export function FormInput({ label, icon, error, ...props }) {
  return (
    <div className="flex flex-col gap-1">
      {label && <label className="text-sm text-foreground/70">{label}</label>}
      <div className="relative">
        {icon && <span className="absolute left-3 top-1/2 -translate-y-1/2 text-foreground/40">{icon}</span>}
        <input
          className={`w-full bg-[#1F2937] border ${error ? "border-red-500" : "border-white/10"} rounded-xl px-4 ${icon ? "pl-10" : ""} py-2 text-foreground focus:outline-none focus:border-primary`}
          {...props}
        />
      </div>
      {error && <p className="text-xs text-red-400">{error}</p>}
    </div>
  );
}
```

## Framer Motion Patterns

```tsx
// Fade-in on scroll
import { motion } from "framer-motion";

const fadeIn = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5 } },
};

<motion.section variants={fadeIn} initial="hidden" whileInView="visible" viewport={{ once: true }}>
  {/* content */}
</motion.section>

// Button hover scale
<motion.button whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.97 }}>
  Click me
</motion.button>

// Page transition wrapper
<motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.3 }}>
  {children}
</motion.div>
```

## Dependencies

```bash
npm install framer-motion
npm install tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

## Useful Commands

```bash
# Verify Tailwind is processing custom colors
npx tailwindcss --input styles/globals.css --output /dev/null --dry-run

# Check for unused Tailwind classes (production build)
npm run build

# Run dev server to preview design system
npm run dev
```

## Design Token Quick Reference

| Token | Value | Usage |
|---|---|---|
| `background` | `#0B0F19` | Page background |
| `primary` | `#6366F1` | Buttons, links, active states |
| `accent` | `#22D3EE` | Highlights, gradients, icons |
| `highlight` | `#F59E0B` | Badges, warnings, CTAs |
| `foreground` | `#E5E7EB` | Body text |
| `rounded-2xl` | `1rem` | Standard border radius |
