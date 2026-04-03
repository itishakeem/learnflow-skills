# Build Script — Profile Management System

Step-by-step prompts to build the user profile page.

---

## Step 1 — ProfileCard Component

```
Create components/profile/ProfileCard.tsx with:
- Props: user { name, email, avatarUrl? }, levelInfo { level, title, progress }, totalXP
- Avatar: 80x80 rounded-2xl — show user image if avatarUrl exists, else User icon
- Show name (bold, large), email (muted below name)
- Level badge: gradient pill showing "Level N · Title"
- XP progress bar: thin 6px bar with brand→accent gradient fill
- XP total text below bar: "N XP total"
- Apply brand glow card style (border + box-shadow)
```

---

## Step 2 — AvatarUpload Component

```
Create components/profile/AvatarUpload.tsx with:
- Hidden file input (accept="image/*") triggered by button click
- "Upload Photo" button with Upload icon
- On file selected: read as DataURL using FileReader
- Show preview image (80x80 rounded) once file is loaded
- Call onSelect(dataUrl) prop to pass result to parent
```

---

## Step 3 — EditProfileForm Component

```
Create components/profile/EditProfileForm.tsx with:
- Props: user { name, email }, onDone callback
- Pre-fill Name and Email inputs with current values
- Optional Password field (leave blank to keep current password)
- Client-side validation on password if filled:
  - Min 8 characters
  - Must contain letters and numbers
- Show inline error message if validation fails
- On save: call PATCH /api/svc/auth/profile/:userId (or update local auth state)
- Show Save Changes button (loading state while saving) and Cancel button
- Cancel button calls onDone without saving
```

---

## Step 4 — Profile Page

```
Create app/profile/page.tsx with:
- Import useAuth and redirect to /login if no user
- Import useGamification and getLevelInfo to display level
- Show page heading "Your Profile"
- Render ProfileCard with user, levelInfo, totalXP
- Show "Edit Profile" button below the card
- On click: toggle to show EditProfileForm in place of button
- On EditProfileForm onDone: switch back to showing the Edit button
- Fade-in animation with Framer Motion on page load
```

---

## Step 5 — Add Profile to Navigation

```
Update components/Nav.tsx:
- Add "Profile" link to APP_LINKS array pointing to /profile
- Show it only when user is authenticated (not guest)
- OR: make the user avatar in the nav clickable, linking to /profile
```

---

## Step 6 — Backend Profile Endpoint (Optional)

```
Add to services/auth/main.py:
- PATCH /profile/{user_id} endpoint
- Request body: name (optional), email (optional), password (optional)
- Find user by user_id in the users dict
- Update only the provided fields
- If password provided: validate and re-hash before storing
- Return updated { id, name, email }
Add "auth" to SERVICE_URLS in app/api/svc/[service]/[...path]/route.ts if not already done
```

---

## Step 7 — Validation

```
Test the following:
1. Visit /profile while logged in → see name, email, level, XP bar
2. Level badge matches current XP from gamification state
3. Click "Edit Profile" → form appears with current values pre-filled
4. Enter weak password → validation error shown
5. Leave password blank → saves without changing password
6. Submit valid changes → profile card updates immediately
7. Upload avatar → preview appears before saving
8. Visit /profile while not logged in → redirect or "please log in" message
```

---

## Validation Checklist

- [ ] Profile card renders name, email, avatar placeholder
- [ ] Level and XP bar reflect gamification state
- [ ] Edit form pre-fills current user data
- [ ] Password left blank skips password update
- [ ] Password validation enforced when filled
- [ ] Avatar upload shows preview
- [ ] Changes reflected immediately in UI after save
- [ ] Profile link accessible from nav
