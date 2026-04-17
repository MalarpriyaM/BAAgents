---
name: task-tracker-process-flow
description: "Instructions for generating user stories, acceptance criteria, and process flow diagrams for the Task Tracker application. Use when decomposing Task Tracker requirements into structured stories and visualizing task management workflows."
applyTo: "**/*task-tracker*"
---

# Task Tracker Process Flow Instructions

## Scope
**IN:** Create tasks, mark complete, view tasks, local storage, simple UI, lightweight  
**OUT:** Multi-user, backend, databases, auth, notifications, filtering, subtasks

---

## User Stories
Format: `As a <user>, I want <goal>, so that <benefit>.`

Keep stories:
- Small (one capability per story)  
- Independent (no hard dependencies)  
- Testable (clear acceptance criteria)  

Example:
- "As a user, I want to create a task with title and description, so that I can organize my work."
- "As a user, I want to mark a task complete, so that I can track progress."

---

## Acceptance Criteria
Use Gherkin format: `Given X, When Y, Then Z`

Example for Create Task:
- Given the app is open, when I click "Create Task", then a form appears.
- Given the form is open, when I enter title and description, then fields accept text.
- Given I click "Save", when the task is valid, then it's added to the list.
- Given a task is created, when I close the app, then the task persists.

---

## Process Diagram (Mermaid)
Use `flowchart TD` showing task lifecycle:

```
Start → Create Task Form → Enter Data → Save → Persist to Storage → Update UI → End
```

Include:
- User actions (rectangles)  
- Decisions (diamonds, if any)  
- Local storage step  
- Clear labels  

---

## Rules
✅ **DO:**
- Keep features within scope only  
- Include local storage persistence in stories  
- Use simple, clear language  

❌ **DON'T:**
- Invent features  
- Reference databases, backends, or cloud services  
- Mix implementation details into criteria  
- Create multi-user scenarios  
