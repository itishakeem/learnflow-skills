# Profile Management System - Reference

---

## File Structure (Scaffolded)

```
app/
└── profile/
    └── page.tsx              # Profile page — view + edit user data

components/
└── profile/
    ├── ProfileCard.tsx       # Displays name, email, avatar, level badge
    ├── EditProfileForm.tsx   # Inline edit form for name/email/password
    └── AvatarUpload.tsx      # Image upload with preview before save

services/
└── auth/
    └── main.py               # Add PATCH /profile/:user_id endpoint
```

---

## Profile Page — `app/profile/page.tsx`

```tsx
// app/profile/page.tsx
"use client";
import { useState } from "react";
import { useAuth } from "@/lib/auth";
import { useGamification, getLevelInfo } from "@/lib/gamification";
import { ProfileCard } from "@/components/profile/ProfileCard";
import { EditProfileForm } from "@/components/profile/EditProfileForm";
import { motion } from "framer-motion";

export default function ProfilePage() {
  const { user } = useAuth();
  const { state } = useGamification();
  const levelInfo = getLevelInfo(state.totalXP);
  const [editing, setEditing] = useState(false);

  if (!user) return <p className="text-ink-disabled p-8">Please log in to view your profile.</p>;

  return (
    <div className="max-w-2xl mx-auto px-4 py-10">
      <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }}>
        <h1 className="text-3xl font-bold text-ink-primary mb-8">Your Profile</h1>

        <ProfileCard user={user} levelInfo={levelInfo} totalXP={state.totalXP} />

        <div className="mt-6">
          {editing
            ? <EditProfileForm user={user} onDone={() => setEditing(false)} />
            : <button
                onClick={() => setEditing(true)}
                className="px-5 py-2.5 rounded-xl bg-brand text-white text-sm font-semibold
                           hover:bg-brand-400 transition-colors"
              >
                Edit Profile
              </button>
          }
        </div>
      </motion.div>
    </div>
  );
}
```

---

## ProfileCard Component

```tsx
// components/profile/ProfileCard.tsx
import { User } from "lucide-react";

interface Props {
  user: { name: string; email: string; avatarUrl?: string };
  levelInfo: { level: number; title: string; progress: number };
  totalXP: number;
}

export function ProfileCard({ user, levelInfo, totalXP }: Props) {
  return (
    <div className="bg-surface-raised border border-surface-border rounded-2xl p-6
                    flex items-start gap-6"
         style={{ boxShadow: "0 0 30px rgba(139,92,246,0.08)" }}
    >
      {/* Avatar */}
      <div className="w-20 h-20 rounded-2xl bg-brand/10 border border-brand/20
                      flex items-center justify-center shrink-0 overflow-hidden">
        {user.avatarUrl
          ? <img src={user.avatarUrl} alt="avatar" className="w-full h-full object-cover" />
          : <User size={32} className="text-brand-300" />
        }
      </div>

      {/* Info */}
      <div className="flex-1 min-w-0">
        <h2 className="text-xl font-bold text-ink-primary truncate">{user.name}</h2>
        <p className="text-sm text-ink-tertiary mb-3">{user.email}</p>

        {/* Level badge */}
        <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-xl
                        bg-gradient-to-r from-brand/15 to-accent/10
                        border border-brand/25 mb-3">
          <span className="text-sm font-bold text-brand-300">Level {levelInfo.level}</span>
          <span className="text-xs text-ink-disabled">·</span>
          <span className="text-xs text-ink-secondary">{levelInfo.title}</span>
        </div>

        {/* XP progress bar */}
        <div className="h-1.5 bg-surface-border rounded-full overflow-hidden">
          <div
            className="h-full rounded-full transition-all duration-700"
            style={{
              width: `${levelInfo.progress}%`,
              background: "linear-gradient(90deg, #8b5cf6, #22d3ee)",
            }}
          />
        </div>
        <p className="text-2xs text-ink-disabled mt-1">{totalXP} XP total</p>
      </div>
    </div>
  );
}
```

---

## EditProfileForm Component

```tsx
// components/profile/EditProfileForm.tsx
"use client";
import { useState } from "react";
import { useAuth } from "@/lib/auth";

interface Props { user: { name: string; email: string }; onDone: () => void; }

export function EditProfileForm({ user, onDone }: Props) {
  const { login } = useAuth();
  const [name, setName] = useState(user.name);
  const [email, setEmail] = useState(user.email);
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [saving, setSaving] = useState(false);

  function validatePassword(p: string) {
    if (!p) return null; // password optional on edit
    if (p.length < 8)             return "Password must be at least 8 characters";
    if (!/[a-zA-Z]/.test(p))      return "Password must include letters";
    if (!/[0-9]/.test(p))         return "Password must include numbers";
    return null;
  }

  async function handleSave(e: React.FormEvent) {
    e.preventDefault();
    const pwErr = validatePassword(password);
    if (pwErr) { setError(pwErr); return; }
    setSaving(true);
    // Call PATCH /api/svc/auth/profile in production
    // For now update local auth state:
    login({ ...user, name, email } as { id: string; name: string; email: string });
    setSaving(false);
    onDone();
  }

  return (
    <form onSubmit={handleSave} className="bg-surface-raised border border-surface-border
                                           rounded-2xl p-6 space-y-4">
      <h3 className="text-sm font-semibold text-ink-primary">Edit Profile</h3>
      {/* Name, Email, Password inputs — use Input component from ui/ */}
      {error && <p className="text-xs text-danger-light">{error}</p>}
      <div className="flex gap-3">
        <button type="submit" disabled={saving}
          className="px-5 py-2.5 rounded-xl bg-brand text-white text-sm font-semibold
                     hover:bg-brand-400 transition-colors disabled:opacity-50">
          {saving ? "Saving…" : "Save Changes"}
        </button>
        <button type="button" onClick={onDone}
          className="px-5 py-2.5 rounded-xl bg-surface-hover text-ink-secondary
                     text-sm font-medium hover:bg-surface-border transition-colors">
          Cancel
        </button>
      </div>
    </form>
  );
}
```

---

## AvatarUpload Component

```tsx
// components/profile/AvatarUpload.tsx
"use client";
import { useState, useRef } from "react";
import { Upload } from "lucide-react";

interface Props { onSelect: (dataUrl: string) => void; }

export function AvatarUpload({ onSelect }: Props) {
  const [preview, setPreview] = useState<string | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  function handleFile(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => {
      const result = reader.result as string;
      setPreview(result);
      onSelect(result);
    };
    reader.readAsDataURL(file);
  }

  return (
    <div className="flex flex-col items-center gap-3">
      {preview && (
        <img src={preview} alt="preview"
             className="w-20 h-20 rounded-2xl object-cover border border-surface-border" />
      )}
      <button type="button" onClick={() => inputRef.current?.click()}
        className="flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-medium
                   bg-surface-raised border border-surface-border text-ink-secondary
                   hover:border-brand/30 transition-colors">
        <Upload size={13} /> Upload Photo
      </button>
      <input ref={inputRef} type="file" accept="image/*" onChange={handleFile} className="hidden" />
    </div>
  );
}
```

---

## Backend — PATCH /profile Endpoint

```python
# Add to services/auth/main.py
class UpdateProfileRequest(BaseModel):
    user_id: str
    name: str | None = None
    email: str | None = None
    password: str | None = None

@app.patch("/profile/{user_id}")
def update_profile(user_id: str, req: UpdateProfileRequest):
    # Find user by id
    user = next((u for u in users_db.values() if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if req.name:  user["name"]  = req.name
    if req.email: user["email"] = req.email
    if req.password:
        if len(req.password) < 8:
            raise HTTPException(status_code=422, detail="Password too short")
        user["password"] = hash_password(req.password)
    return {"status": "ok", "user": {"id": user["id"], "name": user["name"], "email": user["email"]}}
```

---

## Validation Checklist

| Item | Check |
|------|-------|
| Profile page shows name, email, avatar, level | [ ] |
| Level badge reflects current XP | [ ] |
| XP progress bar shown correctly | [ ] |
| Edit form pre-fills current values | [ ] |
| Password validation enforced on edit | [ ] |
| Empty password field skips password update | [ ] |
| Avatar upload shows preview before save | [ ] |
| Changes persist after page refresh | [ ] |
