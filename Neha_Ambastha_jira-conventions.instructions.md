---
applyTo: "**/*.agent.md,**/*.prompt.md"
description: "Jira field conventions for the SCRUM project. Apply when creating or updating Jira issues."
---

# Jira Field Conventions — SCRUM Project

## Default Project
- **Project Key**: `SCRUM`
- Always verify with `getVisibleJiraProjects` if uncertain

## Issue Type
- Default type: **Story**
- Only create Epics, Tasks, or Bugs when explicitly requested

## Summary Format
- Always prefix with `[GHCP Demo]`: `[GHCP Demo] As a <role>, I want <goal> so that <benefit>`

## Story Points
- Use **Fibonacci scale**: 1, 2, 3, 5, 8, 13
- Default estimate when not specified: **3**
- Do not exceed 13 — split stories larger than 13 points

## Labels
- Always include: `AI-generated` (note: Jira does not allow spaces in labels)
- Add additional labels only when the user specifies them

## Description Format
- Always pass `contentFormat: "markdown"` when calling `createJiraIssue` or `editJiraIssue`
- `"html"` is NOT a valid value for `contentFormat` — it will cause a validation error
- Write descriptions as a single continuous multiline string with REAL newline characters — do NOT use `\n` escape sequences, they render as literal text in Jira

## Acceptance Criteria Format
Render as a markdown bullet list inside the description:
```
**Acceptance Criteria**
- condition one
- condition two
- condition three
```

## Description Template
```html
<p><strong>User Story</strong></p>
<p>As a &lt;role&gt;, I want &lt;goal&gt; so that &lt;benefit&gt;.</p>
<p><strong>Context</strong></p>
<p>&lt;background or scope notes&gt;</p>
<strong>Acceptance Criteria</strong>
<ul>
  <li>&lt;condition&gt;</li>
</ul>
```

## Field Mapping Reminders
- `summary` → one-line title (with `[GHCP Demo]` prefix)
- `description` → full formatted body (Jira wiki markup or markdown)
- `labels` → always `["AI-generated"]` minimum (no spaces allowed in Jira labels)
- `story_points` → `story_points` or `customfield_10016` depending on the Jira instance
- Do NOT set `assignee`, `sprint`, or `priority` unless the user asks
