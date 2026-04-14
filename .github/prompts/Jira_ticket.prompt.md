---
description: "Create Jira tickets on the software team board from requirements, with short user stories and clear acceptance criteria"
name: "Jira_ticket"
argument-hint: "Paste requirements, epic context, or feature notes to create Jira tickets"
agent: "Jira Agent"
---
Create Jira tickets for my software team board.

Task:
- Convert the provided requirement text into Jira-ready tickets.
- Keep stories short, clear, and easy to read.
- Include testable acceptance criteria.
- Use Jira tooling to create tickets when enough board/project info is available.

Inputs:
- Feature or requirement text
- Optional: project key, issue type defaults, priority defaults, assignee, labels, sprint/epic
- Optional: target board/team name

Process:
1. Identify distinct deliverables and split them into right-sized Jira tickets.
2. Write concise user stories in this format:
   - As a <user>, I want <goal>, so that <benefit>.
3. Add 3-5 acceptance criteria per ticket using Given/When/Then.
4. Keep wording simple and implementation-neutral.
5. If project/board details are missing, ask one concise clarification before creating issues.
6. If details are sufficient, create tickets directly in Jira.

Output format:

## Ticket Plan
- Project: <project key or name>
- Ticket Count: <number>
- Assumptions: <bullets or None>

## Tickets
For each ticket:
- Summary: <short title>
- Issue Type: <Story/Task/Bug>
- Description:
  - User Story: As a..., I want..., so that...
- Acceptance Criteria:
  - Given ... When ... Then ...
  - Given ... When ... Then ...
  - Given ... When ... Then ...
- Priority: <High/Medium/Low>
- Labels: <comma-separated or None>

## Jira Execution
- If created: list created issue keys.
- If not created: provide a minimal "Missing Info" list and ready-to-run ticket payload.

Quality bar:
- Stories must be short and non-technical.
- Acceptance criteria must be testable and unambiguous.
- Avoid combining multiple independent outcomes in one ticket.
