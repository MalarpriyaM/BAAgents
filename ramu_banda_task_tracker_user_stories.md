# Task Tracker User Stories (Draft for Review)

Project target: EPMCBACC
Issue type target: Story (id: 7)
Publishing scope: Stories only (Epic creation/linking is manual)

## Requirements Mapping

- FR-1: Users can create tasks
- FR-2: Users can mark tasks as completed
- FR-3: Users can view all tasks
- FR-4: Each task has title, description, status
- NFR-1: Simple UI
- NFR-2: Local storage (no database required)
- NFR-3: Should be lightweight

## US-1 Create a Task

Jira Summary:
Create task with title and description

User Story:
As a User I want to create a task with title and description so that I can capture work items to track.

Acceptance Criteria:
Given the task creation form is visible
When the user enters a title and submits
Then a new task is created and displayed in the task list.

Given the user creates a task
When the task is saved
Then the task has a status field initialized to New.

Given the user submits the form without a title
When validation is applied
Then the task is not created and the user is prompted to provide a title.

Traces to: FR-1, FR-4

Jira Description:
Objective:
Allow users to create new tasks for tracking.

Context:
Satisfies FR-1 and FR-4 from Requirements.txt.

Acceptance Criteria:
Given the task creation form is visible
When the user enters a title and submits
Then a new task is created and displayed in the task list.

Given the user creates a task
When the task is saved
Then the task has a status field initialized to New.

Given the user submits the form without a title
When validation is applied
Then the task is not created and the user is prompted to provide a title.

Out of Scope:
Task editing and deletion.

---

## US-2 View All Tasks

Jira Summary:
Display all tasks with task fields

User Story:
As a User I want to view all tasks in one list so that I can quickly understand my pending and completed work.

Acceptance Criteria:
Given tasks exist in storage
When the user opens the task list view
Then all tasks are displayed in a single list.

Given tasks are displayed
When the list is rendered
Then each task row shows title, description, and status.

Given no tasks exist
When the user opens the task list view
Then an empty state message is shown.

Traces to: FR-3, FR-4

Jira Description:
Objective:
Provide a complete and readable task list view.

Context:
Satisfies FR-3 and FR-4 from Requirements.txt.

Acceptance Criteria:
Given tasks exist in storage
When the user opens the task list view
Then all tasks are displayed in a single list.

Given tasks are displayed
When the list is rendered
Then each task row shows title, description, and status.

Given no tasks exist
When the user opens the task list view
Then an empty state message is shown.

Out of Scope:
Filtering, sorting, and search.

---

## US-3 Mark Task as Completed

Jira Summary:
Mark task status as completed

User Story:
As a User I want to mark a task as completed so that I can track progress accurately.

Acceptance Criteria:
Given a task exists with status New
When the user marks the task as completed
Then the task status changes to Completed.

Given the status was updated to Completed
When the task list is refreshed
Then the task remains in Completed status.

Given a task is already Completed
When the user views the task
Then its completed state is clearly visible.

Traces to: FR-2, FR-4

Jira Description:
Objective:
Allow users to complete tasks and reflect progress.

Context:
Satisfies FR-2 and FR-4 from Requirements.txt.

Acceptance Criteria:
Given a task exists with status New
When the user marks the task as completed
Then the task status changes to Completed.

Given the status was updated to Completed
When the task list is refreshed
Then the task remains in Completed status.

Given a task is already Completed
When the user views the task
Then its completed state is clearly visible.

Out of Scope:
Additional status values beyond New and Completed.

---

## US-4 Persist Tasks Locally

Jira Summary:
Persist tasks in local storage

User Story:
As a User I want tasks to persist locally so that my data remains available after page reload or app reopen.

Acceptance Criteria:
Given one or more tasks were created or updated
When the app writes data
Then task data is stored in local storage without using a backend database.

Given tasks exist in local storage
When the user reloads or reopens the app
Then the tasks are loaded and displayed.

Given local storage is unavailable or empty
When the app starts
Then the app still loads with a safe empty state.

Traces to: NFR-2, FR-1, FR-2, FR-3

Jira Description:
Objective:
Persist task data on the client device using browser storage.

Context:
Satisfies NFR-2 and supports FR-1/FR-2/FR-3 continuity across sessions.

Acceptance Criteria:
Given one or more tasks were created or updated
When the app writes data
Then task data is stored in local storage without using a backend database.

Given tasks exist in local storage
When the user reloads or reopens the app
Then the tasks are loaded and displayed.

Given local storage is unavailable or empty
When the app starts
Then the app still loads with a safe empty state.

Out of Scope:
Server-side persistence and synchronization.

---

## US-5 Keep UI Simple and Lightweight

Jira Summary:
Keep task UI simple and lightweight

User Story:
As a User I want a simple and lightweight UI so that task tracking is fast and easy to use.

Acceptance Criteria:
Given the task tracker screen is opened
When the page loads
Then the primary actions (create, view, complete) are visible without extra navigation.

Given normal usage on a typical workstation
When the user performs create, view, and complete actions
Then interactions feel responsive and do not require heavy page transitions.

Given implementation choices are reviewed
When dependencies are selected
Then no backend database dependency is introduced.

Traces to: NFR-1, NFR-3, NFR-2

Jira Description:
Objective:
Ensure usability and performance for day-to-day task tracking.

Context:
Satisfies NFR-1 and NFR-3 while preserving NFR-2 constraints.

Acceptance Criteria:
Given the task tracker screen is opened
When the page loads
Then the primary actions (create, view, complete) are visible without extra navigation.

Given normal usage on a typical workstation
When the user performs create, view, and complete actions
Then interactions feel responsive and do not require heavy page transitions.

Given implementation choices are reviewed
When dependencies are selected
Then no backend database dependency is introduced.

Out of Scope:
Advanced UI styling patterns and animations.

---

## Published User Stories

All user stories have been successfully created and published to JIRA project EPMCBACC:

| Story ID | JIRA Key | Title | Traces To |
|----------|----------|-------|-----------|
| US-1 | EPMCBACC-4131 | Create task with title and description | FR-1, FR-4 |
| US-2 | EPMCBACC-4132 | Display all tasks with task fields | FR-3, FR-4 |
| US-3 | EPMCBACC-4133 | Mark task status as completed | FR-2, FR-4 |
| US-4 | EPMCBACC-4134 | Persist tasks in local storage | NFR-2, FR-1, FR-2, FR-3 |
| US-5 | EPMCBACC-4135 | Keep task UI simple and lightweight | NFR-1, NFR-3, NFR-2 |

All stories include:
- User story statement (As a... I want... so that...)
- 3 Given/When/Then acceptance criteria each
- Full Jira descriptions with objectives, context, ACs, and out-of-scope sections
- Traceability tags linking to Requirements.txt
