# Task Tracker Application — User Stories
**Generated:** 2026-04-14 | **Source:** Requirements 1.txt + create_task_flow.drawio + task_state_diagram.drawio
**Label:** ba-agent-generated

---

## Story Summary

| ID | Title | Epic | Priority | Effort |
|---|---|---|---|---|
| US-01 | Enter or Select a Username | User Session Management | High | S |
| US-02 | Resume an Active Session | User Session Management | Medium | XS |
| US-03 | Create a New Task | Task Creation | High | M |
| US-04 | Validate Required Fields on Task Submission | Task Creation | High | S |
| US-05 | View All Tasks | Task List View & Sorting | High | S |
| US-06 | Sort Task List by Priority Then Status | Task List View & Sorting | Medium | S |
| US-07 | Start Work on a Task | Task Status Transitions | High | S |
| US-08 | Mark a Task as Complete | Task Status Transitions | High | S |
| US-09 | Reset a Task to "To Do" | Task Status Transitions | Medium | XS |
| US-10 | Reopen a Completed Task | Task Status Transitions | Medium | XS |
| US-11 | Archive a Task | Task Archiving & Restoration | Medium | S |
| US-12 | View and Restore Archived Tasks | Task Archiving & Restoration | Low | M |
| US-13 | Persist Tasks via Local Storage | Local Storage Persistence | High | S |

---

## EPIC 1 — User Session Management

---

### US-01 — Enter or Select a Username

**As a** user,
**I want to** enter or select a username before accessing the task list,
**so that** my tasks are associated with my identity and I can resume my session across visits.

**Priority:** High | **Effort:** S | **Labels:** ba-agent-generated

**Acceptance Criteria:**
- Given the app is opened and no active session exists, when the user lands on the page, then a username prompt is displayed before the task list is accessible.
- Given the username prompt is displayed, when the user types a new name and confirms, then the session is created, the username is stored in local storage, and the task list is shown.
- Given the app has been used before with a saved username, when the user opens the app, then previously used usernames are available for selection in addition to the option to enter a new one.
- Given the user selects an existing username, when confirmed, then the session is set and the task list is displayed immediately.
- Given the username prompt is shown, when the user submits an empty name, then an error message is shown and the task list remains inaccessible.

**Diagram Links:**
- `create_task_flow.drawio` — session check and username entry flow

**Open Gap:** G-9: Username UX (dropdown vs. autocomplete) pending stakeholder decision.

---

### US-02 — Resume an Active Session

**As a** returning user,
**I want** my session to be automatically recognized when I revisit the app,
**so that** I do not have to re-enter my username on every visit.

**Priority:** Medium | **Effort:** XS | **Labels:** ba-agent-generated

**Acceptance Criteria:**
- Given the user has a saved session in local storage, when the app is opened, then the username prompt is skipped and the task list is shown directly.
- Given an active session is present, when the task list loads, then the current username is visible in the UI.
- Given an active session exists, when the user navigates away and returns, then the session is still active and tasks are displayed without requiring re-login.

**Diagram Links:**
- `create_task_flow.drawio` — "session active?" decision branch

---

## EPIC 2 — Task Creation

---

### US-03 — Create a New Task

**As a** user with an active session,
**I want to** create a new task by filling in a form with a title, description, and priority,
**so that** the task is saved and visible in my task list.

**Priority:** High | **Effort:** M | **Labels:** ba-agent-generated

**Acceptance Criteria:**
- Given the user is on the task list page, when they click "Add Task", then a task creation form is displayed with fields: Title (required), Description (required), and Priority (optional).
- Given the form is displayed, when the user fills in all required fields and clicks Submit, then the task is saved to local storage with status set to "To Do" and appears at the appropriate position in the task list.
- Given a task is successfully created, when it appears in the task list, then it displays the title, description, priority, and status "To Do".
- Given the form is open, when the user does not fill in the Title or Description and clicks Submit, then the task is not saved and validation errors are shown.
- Given Priority is not selected, when the task is saved, then the task is created with a default or empty priority without error.

**Diagram Links:**
- `create_task_flow.drawio` — end-to-end task creation process flow
- `task_state_diagram.drawio` — initial state "To Do" on task creation

---

### US-04 — Validate Required Fields on Task Submission

**As a** user,
**I want** to be notified when I submit the task form with missing required fields,
**so that** I can correct the errors before the task is saved.

**Priority:** High | **Effort:** S | **Labels:** ba-agent-generated

**Acceptance Criteria:**
- Given the task form is displayed, when the user clicks Submit without entering a Title, then an inline validation error is shown on the Title field and the form is not submitted.
- Given the task form is displayed, when the user clicks Submit without entering a Description, then an inline validation error is shown on the Description field and the form is not submitted.
- Given validation errors are displayed, when the user corrects the fields and clicks Submit again, then the form is submitted successfully and the task is saved.
- Given validation errors have been shown, when the user begins typing in an errored field, then the error on that field is cleared.

**Diagram Links:**
- `create_task_flow.drawio` — "All required fields filled?" validation branch

---

## EPIC 3 — Task List View & Sorting

---

### US-05 — View All Tasks

**As a** user,
**I want to** see all my tasks in a list,
**so that** I have a complete overview of my work.

**Priority:** High | **Effort:** S | **Labels:** ba-agent-generated

**Acceptance Criteria:**
- Given the user has an active session, when the task list page loads, then all tasks belonging to the current session are displayed.
- Given no tasks exist yet, when the task list page loads, then an empty state message is shown (e.g., "No tasks yet. Click 'Add Task' to get started.").
- Given tasks exist, when each task is rendered in the list, then the title, description, priority, and current status are visible for each task.
- Given archived tasks exist, when the main task list is displayed, then archived tasks are not shown in the default view.

**Diagram Links:**
- `create_task_flow.drawio` — "View Task List" step in the main flow
- `task_state_diagram.drawio` — defines which statuses are "active" vs. "archived"

---

### US-06 — Sort Task List by Priority Then Status

**As a** user,
**I want** my task list to be automatically sorted by priority (highest first) and then by status,
**so that** the most urgent and actionable tasks are always at the top.

**Priority:** Medium | **Effort:** S | **Labels:** ba-agent-generated

**Acceptance Criteria:**
- Given tasks with different priorities exist, when the task list is displayed, then High priority tasks appear before Medium, and Medium before Low.
- Given tasks with the same priority exist, when the task list is displayed, then tasks are further sorted by status in the order: To Do → In Progress → Done.
- Given a new task is created, when it appears in the list, then it is inserted in the correct sorted position without requiring a page refresh.
- Given a task's status or priority changes, when the change is saved, then the list re-sorts to reflect the new order.

**Diagram Links:**
- `create_task_flow.drawio` — final step shows "sorted by Priority, then Status"
- `task_state_diagram.drawio` — defines the status values used in sort order

**Assumptions:**
- Sort order for priority: High → Medium → Low → (empty)
- Sort order for status: To Do → In Progress → Done

---

## EPIC 4 — Task Status Transitions

---

### US-07 — Start Work on a Task

**As a** user,
**I want to** move a task from "To Do" to "In Progress",
**so that** I can signal that I have begun working on it.

**Priority:** High | **Effort:** S | **Labels:** ba-agent-generated

**Acceptance Criteria:**
- Given a task is in "To Do" status, when the user triggers "Start work", then the task status changes to "In Progress" and persists to local storage.
- Given a task is in "In Progress" status, when the task list is viewed, then the "Start work" action is no longer available for that task.
- Given a task is in "Done" or "Archived" status, when the task is displayed, then the "Start work" action is not available.

**Diagram Links:**
- `task_state_diagram.drawio` — "Start work" transition: To Do → In Progress

---

### US-08 — Mark a Task as Complete

**As a** user,
**I want to** mark an in-progress task as "Done",
**so that** I can record that the work has been completed.

**Priority:** High | **Effort:** S | **Labels:** ba-agent-generated

**Acceptance Criteria:**
- Given a task is in "In Progress" status, when the user triggers "Mark complete", then the task status changes to "Done" and the change is persisted to local storage.
- Given a task is in "To Do" status, when the task is displayed, then the "Mark complete" action is not directly available (user must first start work).
- Given a task is marked "Done", when the task list is viewed, then the task visually distinguishes itself from active tasks (e.g., different styling).

**Diagram Links:**
- `task_state_diagram.drawio` — "Mark complete" transition: In Progress → Done

---

### US-09 — Reset a Task to "To Do"

**As a** user,
**I want to** reset an in-progress task back to "To Do",
**so that** I can re-queue work that was started prematurely or needs to be restarted.

**Priority:** Medium | **Effort:** XS | **Labels:** ba-agent-generated

**Acceptance Criteria:**
- Given a task is "In Progress", when the user triggers "Reset", then the task status changes to "To Do" and is persisted to local storage.
- Given a task is in "To Do", "Done", or "Archived" status, when the task is displayed, then the "Reset" action is not available.
- Given a task is reset to "To Do", when the list re-renders, then the task is repositioned according to the sort order.

**Diagram Links:**
- `task_state_diagram.drawio` — "Reset" transition: In Progress → To Do

---

### US-10 — Reopen a Completed Task

**As a** user,
**I want to** move a "Done" task back to "In Progress",
**so that** I can continue work on a task that was closed prematurely.

**Priority:** Medium | **Effort:** XS | **Labels:** ba-agent-generated

**Acceptance Criteria:**
- Given a task is in "Done" status, when the user triggers "Reopen", then the task status changes to "In Progress" and is persisted to local storage.
- Given a task is in "To Do", "In Progress", or "Archived" status, when the task is displayed, then the "Reopen" action is not available.
- Given a task is reopened, when the list re-renders, then the task is repositioned according to the sort order.

**Diagram Links:**
- `task_state_diagram.drawio` — "Reopen" transition: Done → In Progress

---

## EPIC 5 — Task Archiving & Restoration

---

### US-11 — Archive a Task

**As a** user,
**I want to** archive a task from any active state,
**so that** I can remove it from my working view without permanently deleting it.

**Priority:** Medium | **Effort:** S | **Labels:** ba-agent-generated

**Acceptance Criteria:**
- Given a task is in "To Do" status, when the user triggers "Archive", then the task status changes to "Archived" and is removed from the main task list.
- Given a task is "In Progress", when the user triggers "Archive", then the task moves directly to "Archived" and is removed from the main list.
- Given a task is "Done", when the user triggers "Archive", then the task moves to "Archived" and is removed from the main list.
- Given a task is already "Archived", when the main task list is displayed, then the Archive action is not available for that task.
- Given a task is archived, when the change is triggered, then it is persisted to local storage before the task disappears from the list.

**Diagram Links:**
- `task_state_diagram.drawio` — "Archive" transitions from To Do, In Progress, and Done → Archived

---

### US-12 — View and Restore Archived Tasks

**As a** user,
**I want to** view archived tasks and restore them to "To Do" when needed,
**so that** I can recover tasks that were archived by mistake or need to be restarted.

**Priority:** Low | **Effort:** M | **Labels:** ba-agent-generated

**Acceptance Criteria:**
- Given archived tasks exist, when the user navigates to the archive view, then all tasks with "Archived" status are displayed.
- Given an archived task is displayed, when the user triggers "Restore", then the task status changes to "To Do", it is persisted to local storage, and it reappears in the main task list.
- Given a task is restored, when the main task list is viewed, then the restored task appears sorted correctly by priority and status.
- Given no archived tasks exist, when the archive view is accessed, then an empty state message is shown.

**Diagram Links:**
- `task_state_diagram.drawio` — "Restore" transition: Archived → To Do

**Open Gap:** G-5: Archive view UI design (tab, filter, or separate page?) pending stakeholder decision. ACs are written implementation-agnostic.

---

## EPIC 6 — Local Storage Persistence

---

### US-13 — Persist Tasks Across Sessions Using Local Storage

**As a** user,
**I want** my tasks to be saved in the browser's local storage,
**so that** my data is retained when I close and reopen the app without needing a server or database.

**Priority:** High | **Effort:** S | **Labels:** ba-agent-generated

**Acceptance Criteria:**
- Given a task is created, when the page is closed and reopened, then the task is still present in the task list with all fields and status intact.
- Given a task's status is changed, when the page is reloaded, then the updated status is reflected correctly.
- Given a task is archived, when the page is reloaded, then the task remains archived and absent from the main list.
- Given the username session is saved, when the app is reopened, then the session is restored from local storage and no username prompt is shown.

**Diagram Links:**
- `create_task_flow.drawio` — "Save Task to Local Storage" step
- `task_state_diagram.drawio` — all state changes require persistence

---

## Open Gaps Register

| ID | Description | Affected Stories | Resolution |
|---|---|---|---|
| G-1 | Priority field absent from requirements; added by flow diagram | US-03, US-06 | Treated as optional field (High/Medium/Low) |
| G-2 | Requirements describe binary status; diagrams define 4-state lifecycle | All status stories | 4-state model from diagram is authoritative |
| G-3 | User session not in requirements; gates entire flow in diagram | US-01, US-02 | Username-based session via localStorage |
| G-4 | Sorting not in requirements; specified in flow diagram | US-06 | Sort by Priority then Status |
| G-5 | Archive view UI design undefined | US-12 | **OPEN — stakeholder decision required** |
| G-6 | Priority sort order undefined | US-06 | Assumed: High → Medium → Low |
| G-7 | Status sort order undefined | US-06 | Assumed: To Do → In Progress → Done |
| G-8 | No edit/delete capability defined | — | Confirmed out of scope |
| G-9 | Username selection UX undefined | US-01 | **OPEN — stakeholder decision required** |
