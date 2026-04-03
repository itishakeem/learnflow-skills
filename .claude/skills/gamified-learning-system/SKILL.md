---
name: gamified-learning-system
description: Add Duolingo-style gamification including streaks, XP, levels, rewards, and engagement loops
---

# Gamified Learning System

## Purpose
Increase user engagement and retention using gamification mechanics.

---

# 1. XP SYSTEM (Core)

## Rules
- Earn XP for actions:
  - Complete exercise → +10 XP
  - Correct answer → +5 XP
  - Learn new concept → +8 XP
  - Daily login → +5 XP

## UI
- Show XP gained animation (+10 ✨)
- Display total XP in dashboard

---

# 2. STREAK SYSTEM 🔥

## Rules
- Track daily activity
- Increase streak if user returns daily
- Reset if inactive for 24h

## UI
- Show streak counter (🔥 5 days)
- Highlight streak on dashboard
- Show warning if streak about to break

---

# 3. LEVEL SYSTEM

## Rules
- XP → Levels
- Example:
  - Level 1: 0–100 XP
  - Level 2: 100–250 XP

## UI
- Progress bar to next level
- Level badge

---

# 4. DAILY GOALS

## Example Goals
- Complete 3 exercises
- Learn 1 concept

## UI
- Checklist
- Progress tracker

---

# 5. REWARDS & FEEDBACK

## Add:
- Success animations (confetti)
- Sound/visual feedback
- Achievement badges

---

# 6. PROGRESS VISUALIZATION

## Dashboard
- XP graph
- Streak history
- Activity timeline

---

# 7. HOOK SYSTEM (VERY IMPORTANT)

## Add:
- “Continue where you left off”
- “You’re 1 step away from leveling up!”
- “Don’t break your streak 🔥”

---

# 8. MICRO-INTERACTIONS

- Button feedback
- Answer correct/incorrect animations
- Glow effects on success

---

# 9. BACKEND LOGIC

- Store:
  - XP
  - Streak
  - Level
  - Activity logs

- Update on every action

---

# 10. AGENT INTEGRATION

- Concept agent → reward XP
- Exercise agent → reward XP
- Progress agent → track streak

---

# 11. VALIDATION CHECKLIST

- [ ] XP updates correctly
- [ ] Streak logic works
- [ ] Level progression visible
- [ ] UI feedback engaging
- [ ] Dashboard reflects progress

---

# OUTPUT EXPECTATION

- Addictive user experience
- Increased retention
- Gamified learning flow