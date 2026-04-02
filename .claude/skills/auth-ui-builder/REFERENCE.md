# Auth UI Builder - Reference

## Page Structure (Scaffolded)

```
app/
├── login/
│   └── page.tsx     # Login page (email, password, social login)
└── signup/
    └── page.tsx     # Signup page (name, email, password, social login)

components/
└── auth/
    ├── AuthCard.tsx        # Centered card wrapper for auth pages
    ├── SocialButton.tsx    # Google / GitHub provider buttons
    └── AuthDivider.tsx     # "or continue with" divider line
```

## Page Templates

### Login Page
```tsx
// app/login/page.tsx
"use client";
import { motion } from "framer-motion";
import { AuthCard } from "@/components/auth/AuthCard";
import { SocialButton } from "@/components/auth/SocialButton";
import { AuthDivider } from "@/components/auth/AuthDivider";
import { FormInput } from "@/components/ui/FormInput";
import { Button } from "@/components/ui/Button";
import Link from "next/link";
import { Mail, Lock } from "lucide-react";

export default function LoginPage() {
  return (
    <main className="min-h-screen flex items-center justify-center px-4">
      <motion.div
        initial={{ opacity: 0, y: 24 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
        className="w-full max-w-md"
      >
        <AuthCard title="Welcome back" subtitle="Sign in to your account">
          <form className="flex flex-col gap-4">
            <FormInput label="Email" type="email" icon={<Mail size={16} />} placeholder="you@example.com" />
            <FormInput label="Password" type="password" icon={<Lock size={16} />} placeholder="••••••••" />
            <div className="flex items-center justify-between text-sm">
              <label className="flex items-center gap-2 text-foreground/60">
                <input type="checkbox" className="accent-primary" /> Remember me
              </label>
              <Link href="#" className="text-primary hover:underline">Forgot password?</Link>
            </div>
            <Button variant="gradient" className="w-full">Sign In</Button>
          </form>
          <AuthDivider />
          <div className="flex gap-3">
            <SocialButton provider="google" />
            <SocialButton provider="github" />
          </div>
          <p className="text-center text-sm text-foreground/60 mt-4">
            Don&apos;t have an account?{" "}
            <Link href="/signup" className="text-primary hover:underline">Sign up</Link>
          </p>
        </AuthCard>
      </motion.div>
    </main>
  );
}
```

### Signup Page
```tsx
// app/signup/page.tsx
"use client";
// Same imports as login...

export default function SignupPage() {
  return (
    <main className="min-h-screen flex items-center justify-center px-4">
      <motion.div initial={{ opacity: 0, y: 24 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.4 }} className="w-full max-w-md">
        <AuthCard title="Create account" subtitle="Join LearnFlow today">
          <form className="flex flex-col gap-4">
            <FormInput label="Name" icon={<User size={16} />} placeholder="Your name" />
            <FormInput label="Email" type="email" icon={<Mail size={16} />} placeholder="you@example.com" />
            <FormInput label="Password" type="password" icon={<Lock size={16} />} placeholder="••••••••" />
            <label className="flex items-center gap-2 text-sm text-foreground/60">
              <input type="checkbox" className="accent-primary" />
              I agree to the <Link href="#" className="text-primary hover:underline">Terms & Conditions</Link>
            </label>
            <Button variant="gradient" className="w-full">Create Account</Button>
          </form>
          <AuthDivider />
          <div className="flex gap-3">
            <SocialButton provider="google" />
            <SocialButton provider="github" />
          </div>
          <p className="text-center text-sm text-foreground/60 mt-4">
            Already have an account?{" "}
            <Link href="/login" className="text-primary hover:underline">Sign in</Link>
          </p>
        </AuthCard>
      </motion.div>
    </main>
  );
}
```

## Reusable Auth Components

### AuthCard
```tsx
// components/auth/AuthCard.tsx
export function AuthCard({ title, subtitle, children }) {
  return (
    <div className="bg-[#111827] border border-white/10 rounded-2xl p-8 shadow-xl">
      <div className="text-center mb-6">
        <h1 className="text-2xl font-bold text-foreground">{title}</h1>
        {subtitle && <p className="text-foreground/60 text-sm mt-1">{subtitle}</p>}
      </div>
      {children}
    </div>
  );
}
```

### SocialButton
```tsx
// components/auth/SocialButton.tsx
const providers = {
  google: { label: "Google",  icon: "🌐" },
  github: { label: "GitHub",  icon: "🐙" },
};

export function SocialButton({ provider }: { provider: "google" | "github" }) {
  const { label, icon } = providers[provider];
  return (
    <button className="flex-1 flex items-center justify-center gap-2 py-2 px-4 border border-white/10 rounded-xl text-sm text-foreground/70 hover:border-primary/50 hover:text-foreground transition-colors">
      <span>{icon}</span> {label}
    </button>
  );
}
```

### AuthDivider
```tsx
// components/auth/AuthDivider.tsx
export function AuthDivider() {
  return (
    <div className="flex items-center gap-3 my-4">
      <div className="flex-1 h-px bg-white/10" />
      <span className="text-xs text-foreground/40">or continue with</span>
      <div className="flex-1 h-px bg-white/10" />
    </div>
  );
}
```

## Dependencies

```bash
npm install lucide-react   # Mail, Lock, User icons
npm install framer-motion  # fade-in animation (from modern-ui-system)
```

## Script Reference

| Script | Purpose |
|---|---|
| `scripts/build-auth.md` | Step-by-step prompts to build login and signup pages |

## Useful Commands

```bash
# Preview auth pages locally
npm run dev
# then visit: http://localhost:3000/login
#             http://localhost:3000/signup

# Type-check components
npx tsc --noEmit
```

## Page Checklist

| Page | Elements |
|---|---|
| `/login` | Email, Password, Remember Me, Forgot Password, Login Button, Google, GitHub, Link to Signup |
| `/signup` | Name, Email, Password, Terms Checkbox, Signup Button, Google, GitHub, Link to Login |
