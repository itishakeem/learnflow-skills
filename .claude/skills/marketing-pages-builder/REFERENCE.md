# Marketing Pages Builder - Reference

## Page Structure (Scaffolded)

```
app/
├── page.tsx              # Home page (Hero, Features, How It Works, CTA)
├── about/
│   └── page.tsx          # About page (Mission, Vision, Platform)
└── contact/
    └── page.tsx          # Contact page (Form, Social links)

components/
└── marketing/
    ├── Hero.tsx           # Hero section with headline and CTA
    ├── Features.tsx       # Feature cards grid
    ├── HowItWorks.tsx     # Numbered steps section
    ├── CtaBanner.tsx      # Full-width call-to-action banner
    └── SocialLinks.tsx    # Social media icon row
```

## Page Section Templates

### Hero Section
```tsx
// components/marketing/Hero.tsx
import { motion } from "framer-motion";
import { Button } from "@/components/ui/Button";

export function Hero() {
  return (
    <section className="min-h-[90vh] flex flex-col items-center justify-center text-center px-6">
      <motion.h1
        className="text-5xl md:text-6xl font-bold text-foreground mb-6"
        initial={{ opacity: 0, y: 32 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
      >
        Learn smarter with{" "}
        <span className="bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">
          LearnFlow
        </span>
      </motion.h1>
      <p className="text-foreground/60 text-lg max-w-xl mb-10">
        AI-powered learning platform for developers.
      </p>
      <div className="flex gap-4">
        <Button variant="gradient">Get Started</Button>
        <Button variant="secondary">Learn More</Button>
      </div>
    </section>
  );
}
```

### Features Section
```tsx
// components/marketing/Features.tsx
import { motion } from "framer-motion";
import { Card } from "@/components/ui/Card";

const features = [
  { icon: "🧠", title: "AI Exercises", description: "Auto-generated coding exercises tailored to your level." },
  { icon: "🐛", title: "Smart Debugger", description: "Paste your error and get instant root cause analysis." },
  { icon: "📈", title: "Progress Tracking", description: "Track your learning journey over time." },
];

export function Features() {
  return (
    <section className="py-24 px-6">
      <h2 className="text-3xl font-bold text-center text-foreground mb-16">Features</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
        {features.map((f, i) => (
          <motion.div
            key={f.title}
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: i * 0.1 }}
          >
            <Card className="text-center hover:border-primary/40 transition-colors">
              <div className="text-4xl mb-4">{f.icon}</div>
              <h3 className="text-lg font-semibold text-foreground mb-2">{f.title}</h3>
              <p className="text-foreground/60 text-sm">{f.description}</p>
            </Card>
          </motion.div>
        ))}
      </div>
    </section>
  );
}
```

### Contact Form
```tsx
// app/contact/page.tsx (form section)
<form className="flex flex-col gap-4 max-w-lg mx-auto">
  <FormInput label="Name" placeholder="Your name" />
  <FormInput label="Email" type="email" placeholder="you@example.com" />
  <textarea
    className="w-full bg-[#1F2937] border border-white/10 rounded-xl px-4 py-3 text-foreground focus:outline-none focus:border-primary resize-none"
    rows={5}
    placeholder="Your message..."
  />
  <Button variant="gradient">Send Message</Button>
</form>
```

## Social Icons Row

```tsx
// components/marketing/SocialLinks.tsx
import { Github, Linkedin, Twitter } from "lucide-react";

const links = [
  { href: "#", icon: <Github size={20} />, label: "GitHub" },
  { href: "#", icon: <Linkedin size={20} />, label: "LinkedIn" },
  { href: "#", icon: <Twitter size={20} />, label: "Twitter" },
];

export function SocialLinks() {
  return (
    <div className="flex gap-4 justify-center">
      {links.map((l) => (
        <a
          key={l.label}
          href={l.href}
          aria-label={l.label}
          className="p-2 rounded-xl border border-white/10 text-foreground/60 hover:text-accent hover:border-accent transition-colors"
        >
          {l.icon}
        </a>
      ))}
    </div>
  );
}
```

## Dependencies

```bash
npm install lucide-react   # icons for features, social, nav
npm install framer-motion  # animations (from modern-ui-system)
```

## Script Reference

| Script | Purpose |
|---|---|
| `scripts/build-landing.md` | Step-by-step prompts to build all 3 pages |

## Useful Commands

```bash
# Preview all pages locally
npm run dev
# then visit: http://localhost:3000
#             http://localhost:3000/about
#             http://localhost:3000/contact

# Check responsive layout
# Chrome DevTools → Toggle device toolbar → 375px (iPhone SE)
```

## Page Checklist

| Page | Sections |
|---|---|
| `/` | Navbar, Hero, Features, How It Works, CTA Banner, Footer |
| `/about` | Navbar, Hero (title), Mission, Vision, Platform, Footer |
| `/contact` | Navbar, Hero (title), Contact Form, Social Links, Footer |
