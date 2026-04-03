# Build Script — Marketing Pages Builder

Step-by-step prompts to build the Home, About, and Contact pages.

---

## Step 1 — Navbar Component

```
Create components/Nav.tsx (or update if exists) with:
- Sticky top navigation: h-16, bg-surface/85, backdrop-blur-xl
- Left: Logo mark (LF gradient badge) + "LearnFlow" brand text
- Center: navigation links (Home, About, Contact) with active state pill
- Right: "Log in" text link + "Sign up" gradient CTA button
- Mobile: hamburger menu button, slide-down drawer with same links
- Fade-in animation on mount with Framer Motion
- Active link detection using usePathname()
```

---

## Step 2 — Footer Component

```
Create components/marketing/Footer.tsx with:
- Dark background matching page
- Left: Logo + one-line product description
- Center: navigation links (Home, About, Contact)
- Right: social icons (GitHub, LinkedIn, Twitter/X) as icon-only links
- Bottom bar: copyright text "© 2024 LearnFlow"
- Divider line above footer using surface-border color
```

---

## Step 3 — Home Page Hero Section

```
Create components/marketing/Hero.tsx with:
- Full-viewport-height section, centered content
- Eyebrow label: "AI-Powered Python Tutor" (small brand-colored pill)
- Headline: large bold gradient text (text-5xl → text-7xl)
  Example: "Learn Python Faster with AI"
- Subheadline: 1-2 sentences describing the platform (text-lg, ink-tertiary)
- Two CTA buttons: "Start Learning Free" (primary) + "See How It Works" (ghost/outline)
- Background: subtle radial gradient glow orb (brand color, blurred, top-center)
- Fade-in + slide-up animation on headline and buttons (staggered)
```

---

## Step 4 — Features Section

```
Create components/marketing/Features.tsx with:
- Section heading: "Everything You Need to Master Python"
- Grid of 3–4 feature cards (responsive: 1 col mobile, 3 col desktop)
- Each card:
  - Icon (from lucide-react) in a colored glow circle
  - Feature title (bold)
  - Short description (2 sentences, ink-tertiary)
  - Hover lift effect (scale + glow)
Features to include:
  - AI Concept Explainer (Brain icon)
  - Exercise Generator (Zap icon)
  - Debug Helper (Bug icon)
  - Progress Tracking (BarChart icon)
- Stagger fade-in animation as cards enter viewport
```

---

## Step 5 — How It Works Section

```
Create components/marketing/HowItWorks.tsx with:
- Section heading: "How It Works"
- 3 numbered steps in a row (or vertical on mobile):
  1. "Ask any Python question" — type concept or paste code
  2. "Get AI explanation" — clear, level-appropriate answer
  3. "Practice with exercises" — AI-generated challenges
- Each step: large step number (gradient text), title, description
- Connecting line or arrow between steps (desktop only)
- Fade-in animation
```

---

## Step 6 — CTA Banner Section

```
Create components/marketing/CtaBanner.tsx with:
- Full-width section with brand gradient background
- Centered heading: "Ready to Start Learning?"
- Subtext: "Join thousands of developers improving their Python skills"
- "Get Started Free" button (white text on transparent/dark button)
- Subtle animated background: slow-pulsing radial glow
```

---

## Step 7 — Home Page Assembly

```
Assemble app/page.tsx with sections in order:
1. Hero
2. Features
3. HowItWorks
4. CtaBanner
5. Footer
Each section separated by consistent vertical spacing (py-20 or py-24)
Import and use Navbar at top (handled by layout.tsx)
```

---

## Step 8 — About Page

```
Create app/about/page.tsx with:
- Page header: "About LearnFlow" with brand label above
- Mission section: 2-3 paragraph description of the platform
- Key features list with icons
- Tech stack section (Next.js, FastAPI, Kafka, Dapr, PostgreSQL)
- Clean card layout, consistent spacing
- Fade-in animation on page load
```

---

## Step 9 — Contact Page

```
Create app/contact/page.tsx with:
- Page header: "Get in Touch"
- Contact form card (left or centered):
  - Name input
  - Email input
  - Message textarea (min 4 rows)
  - "Send Message" submit button
- Social links section (right column or below form):
  - GitHub icon + link
  - LinkedIn icon + link
  - Twitter/X icon + link
- Form submission: show success message after submit (no backend needed)
- Fade-in animation on card
```

---

## Step 10 — Responsiveness Check

```
Test all three pages at:
- Mobile (375px): single column, readable font sizes, stacked buttons
- Tablet (768px): 2-column features grid, proper spacing
- Desktop (1280px): full 3-column features, hero at full scale
Ensure Navbar hamburger menu works on mobile
Ensure Footer links are accessible on small screens
```

---

## Validation Checklist

- [ ] Home page: Hero, Features, HowItWorks, CTA, Footer all render
- [ ] About page complete with mission and platform description
- [ ] Contact page has form + social links
- [ ] Navbar active state highlights current page
- [ ] Mobile hamburger menu opens and closes
- [ ] All pages responsive at mobile/tablet/desktop
- [ ] Animations play on section entry
- [ ] CTA buttons link to /signup
