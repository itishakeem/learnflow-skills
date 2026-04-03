# Gamified Learning System - Reference

## File Structure (Scaffolded)

```
lib/
└── gamification.ts          # XP rules, level thresholds, streak logic

hooks/
└── useGamification.ts       # React hook — reads/writes gamification state

components/gamification/
├── XpToast.tsx              # Floating "+10 XP ✨" pop-up animation
├── StreakBadge.tsx           # 🔥 N days streak counter pill
├── LevelBadge.tsx            # Level pill with icon
├── XpProgressBar.tsx         # Progress bar to next level
├── DailyGoals.tsx            # Checklist of daily goals with progress
├── ConfettiBlast.tsx         # Full-screen confetti on level-up
└── HookBanner.tsx            # Motivational nudge banner ("1 step to level up!")

app/dashboard/
└── page.tsx                 # Extended with XP card, streak card, daily goals panel
```

---

## Core Config — `lib/gamification.ts`

```ts
// lib/gamification.ts

export const XP_REWARDS = {
  completeExercise: 10,
  correctAnswer:    5,
  learnConcept:     8,
  dailyLogin:       5,
} as const;

export type XpAction = keyof typeof XP_REWARDS;

export const LEVELS = [
  { level: 1, min: 0,   max: 100,  label: "Beginner"     },
  { level: 2, min: 100, max: 250,  label: "Apprentice"   },
  { level: 3, min: 250, max: 500,  label: "Explorer"     },
  { level: 4, min: 500, max: 900,  label: "Practitioner" },
  { level: 5, min: 900, max: 1500, label: "Expert"       },
] as const;

export function getLevelForXp(xp: number) {
  return LEVELS.findLast((l) => xp >= l.min) ?? LEVELS[0];
}

export function getProgressToNextLevel(xp: number) {
  const current = getLevelForXp(xp);
  const range = current.max - current.min;
  const earned = xp - current.min;
  return Math.min(earned / range, 1);
}

export const STREAK_RESET_HOURS = 24;

export const DAILY_GOALS = [
  { id: "concept", label: "Learn 1 concept",    target: 1 },
  { id: "exercise", label: "Complete 3 exercises", target: 3 },
] as const;
```

---

## React Hook — `hooks/useGamification.ts`

```ts
// hooks/useGamification.ts
"use client";

import { useState, useEffect, useCallback } from "react";
import { XP_REWARDS, type XpAction, getLevelForXp, getProgressToNextLevel } from "@/lib/gamification";

interface GamificationState {
  xp: number;
  streak: number;
  lastActiveDate: string | null;
  dailyCompleted: Record<string, number>;
}

const STORAGE_KEY = "learnflow_gamification";
const DEFAULT_STATE: GamificationState = {
  xp: 0, streak: 0, lastActiveDate: null, dailyCompleted: {},
};

export function useGamification() {
  const [state, setState] = useState<GamificationState>(DEFAULT_STATE);
  const [lastXpGain, setLastXpGain] = useState<number | null>(null);
  const [leveledUp, setLeveledUp] = useState(false);

  useEffect(() => {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) setState(JSON.parse(saved));
  }, []);

  function save(next: GamificationState) {
    setState(next);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
  }

  const awardXp = useCallback((action: XpAction) => {
    setState((prev) => {
      const gained = XP_REWARDS[action];
      const prevLevel = getLevelForXp(prev.xp).level;
      const newXp = prev.xp + gained;
      const newLevel = getLevelForXp(newXp).level;

      setLastXpGain(gained);
      setTimeout(() => setLastXpGain(null), 2500);

      if (newLevel > prevLevel) {
        setLeveledUp(true);
        setTimeout(() => setLeveledUp(false), 3000);
      }

      const next = { ...prev, xp: newXp };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
      return next;
    });
  }, []);

  const tickDailyGoal = useCallback((goalId: string) => {
    setState((prev) => {
      const next = {
        ...prev,
        dailyCompleted: {
          ...prev.dailyCompleted,
          [goalId]: (prev.dailyCompleted[goalId] ?? 0) + 1,
        },
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
      return next;
    });
  }, []);

  const checkStreak = useCallback(() => {
    const today = new Date().toDateString();
    setState((prev) => {
      if (prev.lastActiveDate === today) return prev;
      const yesterday = new Date(Date.now() - 86400000).toDateString();
      const streak = prev.lastActiveDate === yesterday ? prev.streak + 1 : 1;
      const next = { ...prev, streak, lastActiveDate: today };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
      return next;
    });
  }, []);

  const level = getLevelForXp(state.xp);
  const progress = getProgressToNextLevel(state.xp);

  return { ...state, level, progress, lastXpGain, leveledUp, awardXp, tickDailyGoal, checkStreak };
}
```

---

## Components

### XpToast
```tsx
// components/gamification/XpToast.tsx
"use client";
import { AnimatePresence, motion } from "framer-motion";

export function XpToast({ amount }: { amount: number | null }) {
  return (
    <AnimatePresence>
      {amount !== null && (
        <motion.div
          initial={{ opacity: 0, y: 20, scale: 0.85 }}
          animate={{ opacity: 1, y: -10, scale: 1 }}
          exit={{ opacity: 0, y: -30, scale: 0.9 }}
          transition={{ type: "spring", stiffness: 400, damping: 20 }}
          className="fixed bottom-8 left-1/2 -translate-x-1/2 z-50 pointer-events-none
                     bg-brand/10 border border-brand/30 text-brand-300 font-bold text-sm
                     px-5 py-2.5 rounded-full shadow-glow-sm backdrop-blur-sm"
        >
          +{amount} XP ✨
        </motion.div>
      )}
    </AnimatePresence>
  );
}
```

### StreakBadge
```tsx
// components/gamification/StreakBadge.tsx
export function StreakBadge({ streak }: { streak: number }) {
  const isWarning = streak > 0 && streak < 3;
  return (
    <div className={`flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold
                     border transition-all duration-300
                     ${streak === 0
                       ? "bg-surface-raised border-surface-border text-ink-disabled"
                       : isWarning
                         ? "bg-warning/10 border-warning/30 text-warning-light"
                         : "bg-orange-500/10 border-orange-500/30 text-orange-400"}`}>
      🔥 {streak} day{streak !== 1 ? "s" : ""}
    </div>
  );
}
```

### LevelBadge
```tsx
// components/gamification/LevelBadge.tsx
import type { LEVELS } from "@/lib/gamification";

export function LevelBadge({ level }: { level: typeof LEVELS[number] }) {
  return (
    <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold
                    bg-brand/10 border border-brand/30 text-brand-300">
      ⭐ Lv.{level.level} · {level.label}
    </div>
  );
}
```

### XpProgressBar
```tsx
// components/gamification/XpProgressBar.tsx
export function XpProgressBar({ xp, progress, level }: { xp: number; progress: number; level: { max: number } }) {
  return (
    <div>
      <div className="flex justify-between text-xs text-ink-disabled mb-1.5">
        <span>{xp} XP</span>
        <span>{level.max} XP to next level</span>
      </div>
      <div className="h-2 bg-surface-border rounded-full overflow-hidden">
        <div
          className="h-full bg-gradient-brand rounded-full transition-all duration-700 ease-out"
          style={{ width: `${progress * 100}%` }}
        />
      </div>
    </div>
  );
}
```

### DailyGoals
```tsx
// components/gamification/DailyGoals.tsx
import { DAILY_GOALS } from "@/lib/gamification";
import { CheckCircle2, Circle } from "lucide-react";

export function DailyGoals({ completed }: { completed: Record<string, number> }) {
  return (
    <div className="space-y-2">
      {DAILY_GOALS.map((goal) => {
        const done = (completed[goal.id] ?? 0) >= goal.target;
        return (
          <div key={goal.id} className="flex items-center gap-3">
            {done
              ? <CheckCircle2 size={15} className="text-success-light shrink-0" />
              : <Circle      size={15} className="text-ink-disabled shrink-0" />}
            <span className={`text-xs ${done ? "text-success-light line-through opacity-70" : "text-ink-secondary"}`}>
              {goal.label}
            </span>
            <span className="ml-auto text-2xs text-ink-disabled">
              {Math.min(completed[goal.id] ?? 0, goal.target)}/{goal.target}
            </span>
          </div>
        );
      })}
    </div>
  );
}
```

### HookBanner
```tsx
// components/gamification/HookBanner.tsx
import { motion } from "framer-motion";

interface HookBannerProps { message: string; emoji?: string; }

export function HookBanner({ message, emoji = "🎯" }: HookBannerProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: -6 }}
      animate={{ opacity: 1, y: 0 }}
      className="bg-brand/8 border border-brand/20 rounded-xl px-4 py-2.5
                 flex items-center gap-2.5 text-xs text-brand-300"
    >
      <span>{emoji}</span>
      <span>{message}</span>
    </motion.div>
  );
}
```

---

## Dashboard Integration

```tsx
// Extend dashboard to consume gamification
import { useGamification } from "@/hooks/useGamification";
import { XpToast } from "@/components/gamification/XpToast";
import { StreakBadge } from "@/components/gamification/StreakBadge";
import { LevelBadge } from "@/components/gamification/LevelBadge";
import { XpProgressBar } from "@/components/gamification/XpProgressBar";
import { DailyGoals } from "@/components/gamification/DailyGoals";
import { HookBanner } from "@/components/gamification/HookBanner";

// Inside component:
const { xp, streak, level, progress, dailyCompleted, lastXpGain, leveledUp, checkStreak } = useGamification();

// On mount — tick streak:
useEffect(() => { checkStreak(); }, []);

// Render:
<XpToast amount={lastXpGain} />
<StreakBadge streak={streak} />
<LevelBadge level={level} />
<XpProgressBar xp={xp} progress={progress} level={level} />
<DailyGoals completed={dailyCompleted} />
{progress > 0.8 && <HookBanner message={`You're ${Math.round((1 - progress) * (level.max - level.min))} XP away from leveling up!`} emoji="⚡" />}
{streak > 0 && <HookBanner message={`Don't break your ${streak}-day streak! 🔥`} emoji="🔥" />}
```

---

## Awarding XP in Feature Pages

```tsx
// On concept explained:
const { awardXp, tickDailyGoal } = useGamification();
awardXp("learnConcept");
tickDailyGoal("concept");

// On exercise generated + submitted:
awardXp("completeExercise");
tickDailyGoal("exercise");
```

---

## Dependencies

```bash
npm install framer-motion   # XpToast animation, HookBanner fade-in
npm install lucide-react    # CheckCircle2, Circle icons in DailyGoals
```

---

## Useful Commands

```bash
# Run dev server to test gamification UI
npm run dev

# Clear gamification state in browser console (testing)
localStorage.removeItem("learnflow_gamification")

# Type-check all gamification components
npx tsc --noEmit
```

---

## XP Rules Quick Reference

| Action | XP Gained |
|---|---|
| Complete exercise | +10 XP |
| Correct answer | +5 XP |
| Learn new concept | +8 XP |
| Daily login | +5 XP |

## Level Thresholds

| Level | XP Range | Label |
|---|---|---|
| 1 | 0 – 100 | Beginner |
| 2 | 100 – 250 | Apprentice |
| 3 | 250 – 500 | Explorer |
| 4 | 500 – 900 | Practitioner |
| 5 | 900 – 1500 | Expert |

## Component Checklist

| Component | Purpose |
|---|---|
| `XpToast` | Floating XP gain popup |
| `StreakBadge` | Daily streak counter |
| `LevelBadge` | Current level pill |
| `XpProgressBar` | Progress to next level |
| `DailyGoals` | Checklist with completion state |
| `HookBanner` | Motivational nudge messages |
| `ConfettiBlast` | Level-up celebration effect |
