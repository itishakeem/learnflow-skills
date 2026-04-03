---
name: basic-auth-system
description: Simple authentication system with signup, login, and validation
---

# Basic Auth System

## Purpose
Create authentication with name, email, and password.

---

## Signup Requirements
- Fields:
  - Name
  - Email
  - Password
  - Confirm Password

## Validation Rules
- Password must be:
  - At least 8 characters
  - Include letters and numbers
- Password and Confirm Password must match
- Email must be valid

---

## Login Requirements
- Email
- Password

---

## Behavior
- Store user in database (PostgreSQL)
- Hash password before saving
- After login/signup → redirect to dashboard

---

## Dashboard Requirement
- Show logged-in user name:
  - Example: "Welcome, Abdulhakeem 👋"

---

## Instructions
1. Create signup and login forms
2. Add validation rules
3. Store user securely
4. Display user name on dashboard

---

## Output Expectation
- Working auth system
- Validations applied
- User name visible on dashboard