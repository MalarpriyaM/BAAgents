---
name: jira-user-story-publisher
description: "Use when creating Jira Epics, User Stories, and Acceptance Criteria for the Task Tracker app and publishing them via MCP. Trigger for Jira backlog generation, story-to-Jira publishing, epic creation, and MCP Jira automation."
applyTo: "**/*task-tracker*"
---

# Task Tracker – Jira User Story Generator & Publisher

## Purpose
Convert Task Tracker requirements into a structured backlog (Epics, User Stories, Acceptance Criteria) and publish them to Jira using MCP Server actions.

---

## Scope

**IN:**
- Create tasks, mark tasks as completed, view all tasks
- Task fields: title, description, status
- Simple UI, local storage only, lightweight app

**OUT:**
- Multi-user, authentication, backend, cloud sync, notifications, filtering, subtasks
- Any feature not explicitly stated in the requirements below

---

## Source Requirements (Do Not Deviate)

### Functional
- Users can create tasks.
- Users can mark tasks as completed.
- Users can view all tasks.
- Each task has: title, description, status.

### Non-Functional
- Simple, minimalist UI with no unnecessary elements.
- Local storage only — no database or backend.
- Lightweight — small footprint, fast startup, offline-first.

---

## Step 1 — Generate the Backlog

### Epic
One Epic covering the full Task Tracker feature set.

Format:
```
Epic Summary: Task Tracker – Core Task Management
Epic Description: Deliver a lightweight, browser-based task management tool with create, view, and complete capabilities using local storage.
```

### User Stories
One story per functional requirement. Use this format exactly:

```
As a <user>, I want <goal>, so that <benefit>.
```

Required stories (minimum):
1. Create a task with title, description, and status.
2. View all existing tasks in a list.
3. Mark a task as completed.
4. Persist tasks across sessions using local storage.

### Acceptance Criteria
Use Gherkin format for every story:

```
Given <precondition>
When <action>
Then <expected result>
```

Each story must have at least 3 acceptance criteria. Non-functional constraints (lightweight, simple UI, local storage) must be reflected in at least one criterion per story.

---

## Step 2 — Produce Jira-Ready JSON

After generating all backlog items, structure them in the following JSON format exactly. Do not alter the schema.

```json
{
  "epic": {
    "summary": "<epic title>",
    "description": "<epic description>",
    "projectKey": "<JIRA_PROJECT_KEY>"
  },
  "stories": [
    {
      "summary": "<story title>",
      "description": "As a <user>, I want <goal>, so that <benefit>.",
      "acceptanceCriteria": [
        "Given ... When ... Then ...",
        "Given ... When ... Then ...",
        "Given ... When ... Then ..."
      ],
      "projectKey": "<JIRA_PROJECT_KEY>",
      "labels": ["task-tracker", "generated-by-agent"]
    }
  ]
}
```

- `projectKey` must be provided by the user or retrieved from context before publishing.
- `labels` must always include `"task-tracker"` and `"generated-by-agent"`. Do not remove them.

---

## Step 3 — Publish to Jira via MCP

After producing the JSON, call MCP actions in this sequence:

1. **Create the Epic**
   ```
   jira.createEpic(epic)
   ```
   Capture the returned `epicKey`.

2. **Create each Story**
   ```
   jira.createIssue(story)
   ```
   Capture each returned `issueKey`.

3. **Link each Story to the Epic**
   ```
   jira.attachStoryToEpic(issueKey, epicKey)
   ```

Do not skip step 3. All stories must be linked to the epic before the task is considered complete.

If any MCP call fails, report the error with the failed item's summary and stop. Do not partially publish.

---

## Output Order

Return sections in this exact order:
1. Generated backlog (Epic + Stories + Acceptance Criteria in readable format)
2. Jira-ready JSON block
3. MCP publish results (success confirmations or error details per item)

---

## Rules

✅ **DO:**
- Use only the requirements listed above as source of truth.
- Always include all 3 labels fields: `task-tracker`, `generated-by-agent`.
- Always link every story to the epic via `jira.attachStoryToEpic`.
- Write Gherkin criteria that reference local storage persistence where relevant.
- Ask the user for `projectKey` if it is not present in context.

❌ **DON'T:**
- Invent features outside the stated scope.
- Omit the MCP publish step when the user requests Jira publication.
- Partially publish — either all items succeed or report what failed.
- Use a database, backend, or cloud reference in any story or criterion.
- Skip labels on any story.
