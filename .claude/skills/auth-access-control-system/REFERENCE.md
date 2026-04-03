# Auth Access Control System - Reference

---

## File Structure (Scaffolded)

```
lib/
└── auth.tsx                        # AuthProvider, useAuth hook, guest/user state

components/
└── auth/
    ├── GuestGate.tsx               # LockedOverlay + UpgradeModal components
    └── GuestUsageBadge.tsx         # Shows "N/max uses remaining" pill

middleware.ts                       # Next.js middleware — redirects unauthenticated users
```

---

## Auth Context — `lib/auth.tsx`

```tsx
// lib/auth.tsx
"use client";
import { createContext, useContext, useState, useEffect } from "react";

export interface User { id: string; name: string; email: string; }

export const GUEST_LIMITS = {
  concepts:  3,
  exercises: 3,
} as const;

interface AuthState {
  user: User | null;
  isGuest: boolean;
  usage: { concepts: number; exercises: number };
  login: (user: User) => void;
  logout: () => void;
  consumeGuestUsage: (feature: keyof typeof GUEST_LIMITS) => boolean;
}

const Ctx = createContext<AuthState | null>(null);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [usage, setUsage] = useState({ concepts: 0, exercises: 0 });

  const isGuest = user === null;

  function login(u: User) {
    setUser(u);
    localStorage.setItem("learnflow_user", JSON.stringify(u));
  }

  function logout() {
    setUser(null);
    localStorage.removeItem("learnflow_user");
  }

  function consumeGuestUsage(feature: keyof typeof GUEST_LIMITS): boolean {
    if (!isGuest) return true; // authenticated users always pass
    if (usage[feature] >= GUEST_LIMITS[feature]) return false;
    setUsage((prev) => ({ ...prev, [feature]: prev[feature] + 1 }));
    return true;
  }

  // Restore session on mount
  useEffect(() => {
    const saved = localStorage.getItem("learnflow_user");
    if (saved) setUser(JSON.parse(saved));
  }, []);

  return (
    <Ctx.Provider value={{ user, isGuest, usage, login, logout, consumeGuestUsage }}>
      {children}
    </Ctx.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(Ctx);
  if (!ctx) throw new Error("useAuth must be inside AuthProvider");
  return ctx;
}
```

---

## GuestGate Components — `components/auth/GuestGate.tsx`

```tsx
// components/auth/GuestGate.tsx
"use client";
import { motion } from "framer-motion";
import { Lock } from "lucide-react";

// Blurs child content and shows unlock CTA for guests
export function LockedOverlay({
  locked, title, onUnlock, children,
}: {
  locked: boolean;
  title: string;
  onUnlock: () => void;
  children: React.ReactNode;
}) {
  if (!locked) return <>{children}</>;
  return (
    <div className="relative">
      <div className="blur-sm pointer-events-none select-none">{children}</div>
      <div className="absolute inset-0 flex flex-col items-center justify-center gap-3">
        <Lock size={20} className="text-ink-disabled" />
        <p className="text-sm font-medium text-ink-secondary">{title}</p>
        <button
          onClick={onUnlock}
          className="px-4 py-2 rounded-xl text-xs font-semibold bg-brand text-white
                     hover:bg-brand-400 transition-colors"
        >
          Sign up free
        </button>
      </div>
    </div>
  );
}

// Modal shown when guest hits usage limit
export function UpgradeModal({ onClose }: { onClose: () => void }) {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4"
      onClick={onClose}
    >
      <motion.div
        initial={{ scale: 0.92, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        exit={{ scale: 0.92, opacity: 0 }}
        onClick={(e) => e.stopPropagation()}
        className="bg-surface-raised border border-surface-border rounded-2xl p-8 max-w-sm w-full shadow-card-hover"
      >
        <p className="text-2xl mb-1">🔒</p>
        <h2 className="text-xl font-bold text-ink-primary mb-2">Unlock Full Access</h2>
        <ul className="text-sm text-ink-tertiary space-y-1.5 mb-6">
          <li>✓ Unlimited concept explanations</li>
          <li>✓ Unlimited exercises</li>
          <li>✓ Progress tracking dashboard</li>
          <li>✓ Save your work</li>
        </ul>
        <a
          href="/signup"
          className="block w-full text-center py-3 rounded-xl bg-brand text-white
                     font-semibold text-sm hover:bg-brand-400 transition-colors"
        >
          Sign Up Free
        </a>
        <button
          onClick={onClose}
          className="mt-3 w-full text-center text-xs text-ink-disabled hover:text-ink-secondary transition-colors"
        >
          Continue as guest
        </button>
      </motion.div>
    </motion.div>
  );
}
```

---

## GuestUsageBadge — `components/auth/GuestUsageBadge.tsx`

```tsx
// components/auth/GuestUsageBadge.tsx
import { useAuth, GUEST_LIMITS } from "@/lib/auth";

export function GuestUsageBadge({ feature }: { feature: "concepts" | "exercises" }) {
  const { isGuest, usage } = useAuth();
  if (!isGuest) return null;

  const used = usage[feature];
  const max  = GUEST_LIMITS[feature];
  const left = max - used;
  const exhausted = left === 0;

  return (
    <div className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs font-medium
                     border transition-colors ${exhausted
                       ? "bg-danger/10 border-danger/25 text-danger-light"
                       : "bg-surface-raised border-surface-border text-ink-disabled"}`}
    >
      {exhausted ? "🔒 Limit reached" : `${left}/${max} free`}
    </div>
  );
}
```

---

## Next.js Middleware — `middleware.ts`

```ts
// middleware.ts (project root)
import { NextRequest, NextResponse } from "next/server";

const PROTECTED = ["/dashboard"];

export function middleware(req: NextRequest) {
  const user = req.cookies.get("learnflow_user");
  const isProtected = PROTECTED.some((p) => req.nextUrl.pathname.startsWith(p));

  if (isProtected && !user) {
    return NextResponse.redirect(new URL("/login", req.url));
  }
  return NextResponse.next();
}

export const config = { matcher: ["/dashboard/:path*"] };
```

---

## Usage Pattern in Feature Pages

```tsx
// In concepts/page.tsx or exercise/page.tsx
const { isGuest, consumeGuestUsage, usage } = useAuth();
const [showModal, setShowModal] = useState(false);

const limitReached = isGuest && usage.concepts >= GUEST_LIMITS.concepts;

async function handleAction() {
  if (!consumeGuestUsage("concepts")) {
    setShowModal(true);
    return;
  }
  // proceed with API call
}

// In JSX:
{showModal && <UpgradeModal onClose={() => setShowModal(false)} />}
<GuestUsageBadge feature="concepts" />
```

---

## Access Rules Quick Reference

| Feature | Guest | Authenticated |
|---------|-------|---------------|
| Home / About / Contact | ✓ Full | ✓ Full |
| Concept Explainer | Max 3/session | ✓ Unlimited |
| Exercise Generator | Max 3/session | ✓ Unlimited |
| Dashboard | Demo data only | ✓ Real data |
| Progress Tracking | ✗ | ✓ |
| Save Work | ✗ | ✓ |
| Kafka/Dapr events | ✗ (stateless) | ✓ |

---

## Validation Checklist

| Item | Check |
|------|-------|
| Guest usage counter increments correctly | [ ] |
| Usage limit blocks further requests | [ ] |
| UpgradeModal appears on limit hit | [ ] |
| LockedOverlay blurs content for guests | [ ] |
| Authenticated users bypass all limits | [ ] |
| Session restores from localStorage on reload | [ ] |
| Middleware redirects unauthenticated /dashboard | [ ] |
