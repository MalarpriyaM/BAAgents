# BAAgents

## Project Description

BAAgents is the repo to enable the BA Agent challenge session, collect agents from global BAs, and evaluate based on the criteria defined.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MalarpriyaM/BAAgents.git
cd BAAgents
```

---

## 📁 File Naming Convention

All agent and skill files **must follow this naming convention**:

```
firstname_lastname_<agentname or skillname>.ext
```

This prefix should match your **EPAM email ID** (the part before `@epam.com`).

### Examples

| EPAM Email | Agent/Skill Name | File Name |
|---|---|---|
| `john.smith@epam.com` | lead_qualifier | `john_smith_lead_qualifier.py` |
| `priya.kumar@epam.com` | requirements_extractor | `priya_kumar_requirements_extractor.py` |
| `alex.jones@epam.com` | story_writer | `alex_jones_story_writer.md` |

> **Note:** Use lowercase letters and underscores only. No spaces, hyphens, or special characters.

---

## Adding Your File to the Repository

Once your agent or skill file is ready, follow these steps to contribute:

### Step 1 — Pull the Latest Changes

Always sync with the remote before making changes:

```bash
git pull origin main
```

### Step 2 — Add Your File

Place your file in the appropriate folder and stage it:

```bash
git add your_filename_here.py
```

Or to stage all new/modified files at once:

```bash
git add .
```

### Step 3 — Commit Your Changes

Write a clear, descriptive commit message:

```bash
git commit -m "Add <agentname> agent by <firstname_lastname>"
```

**Example:**
```bash
git commit -m "Add lead_qualifier agent by john_smith"
```

### Step 4 — Push to the Repository

```bash
git push origin main
```

---

## Branch Policy

This repository uses a **single branch (`main`)**.

- Do **not** create new branches.
- Always push directly to `main`.
- Always do a `git pull` before you start working to avoid conflicts.

---

## Need Help?

Reach out to the repository owner Malar priya
