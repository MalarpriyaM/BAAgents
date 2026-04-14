---
description: "Analyse a requirements file and generate user stories with Jira publishing"
agent: "Aliona BA Story Publisher"
tools: [read, search, web, todo]
---

Analyse the requirements file and generate professional user stories.

## Input Context

- **Requirements file**: [Req.txt](../../Req.txt)
- **Jira Project Name**: ${input:Dream team}
- **Jira Project Key**: ${input:SCRUM}

## Task

1. Read the requirements file referenced above.
2. Extract all functional and non-functional requirements.
3. Group them into Epics.
4. Generate user stories with: US-ID, Name, Description, rule-based use-case scenarios (NOT Gherkin), edge cases, and open questions.
5. Generate a Mermaid process diagram and draw.io-compatible flow.
6. Present everything inline in chat and ask for my confirmation.
7. Only after I confirm, publish the approved user stories to the Jira project specified above.
