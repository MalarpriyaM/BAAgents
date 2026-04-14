---
description: "Create a Jira-ready process diagram for a ticket and include draw.io XML attachment content"
name: "diagram_prompt"
argument-hint: "Paste Jira ticket summary, user story, and acceptance criteria"
agent: "agent"
---
Create a clear, lightweight diagram package for the provided Jira ticket.

Goal:
- Make each ticket easier to understand visually.
- Output a process-flow style diagram (or a better-fitting diagram type when needed).
- Provide draw.io XML that can be saved as a .drawio attachment.

Inputs:
- Ticket summary
- User story
- Acceptance criteria
- Optional: preferred diagram type (process flow, state flow, sequence, swimlane)

Instructions:
1. Read the ticket details and identify the main user/system flow.
2. Choose the best diagram type:
   - Use process flow by default.
   - Use state flow when status transitions are central.
   - Use sequence when actor/system interactions are central.
3. Keep the diagram simple and readable for Jira viewers.
4. Ensure every acceptance criterion is represented directly or implied by the flow.
5. Include persistence/local-storage steps when relevant.
6. If multiple tickets are provided, create one diagram package per ticket.

Output format (use exactly this structure):

## Ticket
- Summary: <text>
- Diagram Type: <text>

## Diagram Notes
- Scope: <what this covers>
- Assumptions: <short bullets or "None">

## Mermaid
```mermaid
<diagram markup>
```

## Draw.io Filename
- <ticket-slug>.drawio

## Draw.io XML
```xml
<mxfile>...</mxfile>
```

## Jira Attachment Guidance
- Save the XML as the filename above.
- Attach it to the Jira issue.
- Optional description text: "Process diagram for this ticket."

Quality bar:
- Keep story language short and plain.
- Avoid unnecessary branches.
- Use action-first labels (Create Task, Validate Input, Save Task, etc.).
