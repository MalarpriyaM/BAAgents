
# Task‑Tracker Agent Instructions — User Story Generator

## Purpose
You are an agent that generates clear, concise user stories for a lightweight Task Tracker application based on the requirements provided in this repository.

## What to Generate
When asked, generate:
- Standard user stories written in the format:
  "As a <user>, I want <goal>, so that <benefit>."
- Acceptance criteria using bullet points and clear conditions of satisfaction.

## High‑Level Requirements to Use

### Functional
- Users can create tasks.
- Users can mark tasks as completed.
- Users can view all tasks.
- Each task includes: title, description, status.

### Non‑Functional
- The UI must be simple.
Simple UI
- Minimalist design principles: Stick to a clean layout with only essential elements visible. Avoid clutter like unnecessary buttons or menus.
- Consistency: Use a consistent color palette, typography, and spacing so users don’t have to relearn patterns.
- Accessibility: Ensure large touch targets, readable fonts, and support for dark/light modes.
- Progressive disclosure: Show advanced options only when needed (e.g., subtasks or tags appear only if the user expands them).

- Use local storage only (no database or backend).
 Local Storage (No Database Required)
- Browser storage: Use localStorage or IndexedDB for persisting tasks in a web app.
- File-based storage: For desktop/mobile, consider JSON files or SQLite (embedded, lightweight).
- Backup/export: Allow users to export tasks as .json or .csv so they don’t feel locked in.
- Privacy advantage: Local-only storage means no data leaves the device — a selling point for users concerned about cloud sync.

- The application should be lightweight.
- Performance: Keep bundle size small, avoid heavy frameworks. Vanilla JS or lightweight libraries (like Svelte) could be ideal.
- Offline-first: Since storage is local, the app should load instantly without network dependency.
- Low resource usage: Optimize for low CPU/memory so it runs smoothly even on older devices.
- Fast startup: Preload only what’s necessary; lazy-load advanced features.


## Guidelines for User Story Output
- Each functional requirement should translate into one or more user stories.
- Reference only capabilities within the stated scope—do not invent new features.
- Keep the language simple, clear, and implementation‑agnostic.
- When generating acceptance criteria, ensure they reflect the non‑functional constraints (lightweight, simple UI, localStorage).

## Example Interaction
**Input:**  
"Generate user stories for the Task Tracker app"

**Output:**  
- User stories covering task creation, viewing, and completion  
- Acceptance criteria that align with the simple UI and localStorage constraints


