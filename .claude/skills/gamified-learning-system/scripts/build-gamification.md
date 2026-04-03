# Build Script — Gamified Learning System

Step-by-step prompts to implement the full gamification system.

---

## Step 1 — Core Config

```
Create the file lib/gamification.ts with:
- XP_REWARDS map: completeExercise=10, correctAnswer=5, learnConcept=8, dailyLogin=5
- LEVELS array: 5 levels from Beginner (0–100 XP) to Expert (900–1500 XP)
- getLevelForXp(xp) helper
- getProgressToNextLevel(xp) returning 0–1 float
- DAILY_GOALS array: "Learn 1 concept" and "Complete 3 exercises"
- STREAK_RESET_HOURS = 24
Export all as named exports.
```

---

## Step 2 — Gamification Hook

```
Create the file hooks/useGamification.ts with:
- Load/save state from localStorage key "learnflow_gamification"
- State: xp, streak, lastActiveDate, dailyCompleted
- awardXp(action) — adds XP, detects level-up, triggers lastXpGain toast state
- tickDailyGoal(goalId) — increments daily completion counter
- checkStreak() — increments or resets streak based on lastActiveDate vs today
- Returns: xp, streak, level, progress, dailyCompleted, lastXpGain, leveledUp, awardXp, tickDailyGoal, checkStreak
```

---

## Step 3 — XpToast Component

```
Create components/gamification/XpToast.tsx:
- Props: amount (number | null)
- Use AnimatePresence + motion.div
- Animate: slide up from bottom, fade out after 2.5s
- Style: floating pill, brand/indigo colors, "✨ +N XP" text
- Position: fixed bottom-8, centered horizontally, z-50, pointer-events-none
```

---

## Step 4 — StreakBadge Component

```
Create components/gamification/StreakBadge.tsx:
- Props: streak (number)
- Show "🔥 N days" in a rounded pill
- Color: orange when streak >= 3, warning-yellow for 1–2 days, gray for 0
```

---

## Step 5 — LevelBadge + XpProgressBar

```
Create components/gamification/LevelBadge.tsx:
- Props: level object from LEVELS
- Display "⭐ Lv.N · Label" in a brand-colored pill

Create components/gamification/XpProgressBar.tsx:
- Props: xp, progress (0–1), level
- Show current XP / max XP as text above a gradient progress bar
- Animate the bar width with transition-all duration-700
```

---

## Step 6 — DailyGoals Component

```
Create components/gamification/DailyGoals.tsx:
- Props: completed (Record<string, number>)
- Render each DAILY_GOALS entry as a row:
  - CheckCircle2 icon (green) when done, Circle icon (gray) when pending
  - Strike-through text when completed
  - Progress counter N/target on the right
```

---

## Step 7 — HookBanner + ConfettiBlast

```
Create components/gamification/HookBanner.tsx:
- Props: message (string), emoji (string, default "🎯")
- Animated fade-in banner with brand/indigo tint
- Used for: "1 step to level up", "Don't break your streak" messages

Create components/gamification/ConfettiBlast.tsx:
- Shown when leveledUp === true
- Use canvas-confetti or a CSS-only burst of colored divs
- Auto-hides after 3 seconds
```

---

## Step 8 — Dashboard Integration

```
Update app/dashboard/page.tsx to:
1. Import and call useGamification()
2. Call checkStreak() on mount (useEffect)
3. Render XpToast with lastXpGain prop
4. Add a gamification row under the stat cards with:
   - StreakBadge
   - LevelBadge
   - XpProgressBar (full width)
5. Add a DailyGoals section in the sidebar or below quick actions
6. Show HookBanner when progress > 0.8 or streak > 0
7. Show ConfettiBlast when leveledUp is true
```

---

## Step 9 — Wire XP to Feature Pages

```
Update app/concepts/page.tsx:
- Import useGamification
- After a successful explain API call, call:
  awardXp("learnConcept")
  tickDailyGoal("concept")

Update app/exercise/page.tsx:
- After successful generateExercise, call awardXp("completeExercise")
- After successful submitCode, call tickDailyGoal("exercise")
```

---

## Step 10 — TypeScript Check

```
Run: npx tsc --noEmit
Fix any type errors in gamification components.
Ensure all imports resolve correctly.
```

---

## Validation

After all steps:

- [ ] XP increases when completing exercises and learning concepts
- [ ] XpToast pops up with correct amount
- [ ] Streak increments on daily return, resets after 24h gap
- [ ] Level badge and progress bar update as XP grows
- [ ] Daily goals check off as features are used
- [ ] HookBanner shows relevant motivational message
- [ ] ConfettiBlast fires on level-up
- [ ] State persists across page refreshes (localStorage)
