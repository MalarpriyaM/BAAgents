---
description: "Reusable prompt blocks for requirement-to-story generation and related BA outputs."
---
# Requirements Story Writer Prompt Library

This file contains reusable prompt blocks that can be invoked by one or more agents.

## Prompt Block: User Story and Acceptance Criteria Generator
### Use When
- Converting functional requirements and non-functional requirements into user stories and add testable acceptance criteria.

### Prompt Text
Read the referenced requirements source and generate user stories and strict Acceptance Criteria using only that source.

Output constraints:
- One primary user intent per story.
- Story format: As a <persona>, I want <capability>, so that <business value>.
- Story ID format: US-###.
- Acceptance Criteria format: Scenario: <name> Given <precondition> When <event> Then <outcome> And <additional outcome>
- Avoid implementation details unless explicitly present in requirements.

Quality rules:
- Include positive and negative paths where relevant.
- Include edge cases where relevant.
- Express non-functional checks as measurable criteria.

Required output section:
- User Stories with Acceptance Criteria (Gherkin)

For each story include:
- Story ID
- Story
- All applicable Acceptance Criteria (Gherkin)
- Notes (dependencies, assumptions, risks, open questions)

## Prompt Block: Mermaid Process Flow Generator
### Use When
- A process or user journey should be visualized from requirements.

### Prompt Text
Generate a Mermaid flowchart that represents the process described in the requirements.

Rules:
- Use clear action and decision labels.
- Keep the flow logically ordered.
- Render only as Mermaid fenced code block.

Required output section:
- Process Flow Diagram

## Prompt Block: INVEST Review
### Use When
- Story quality review and refinements are required.

### Prompt Text
Evaluate each story against INVEST and revise if needed.

Review format per story:
- I: Pass/Fail with one-line reason
- N: Pass/Fail with one-line reason
- V: Pass/Fail with one-line reason
- E: Pass/Fail with one-line reason
- S: Pass/Fail with one-line reason
- T: Pass/Fail with one-line reason
- Revisions made: <what changed>

Required output section:
- INVEST Review

## Prompt Block: Full Structured Output
### Use When
- End-to-end response is required from requirements source to final validated stories.

### Prompt Text
Return output in this exact order:

1) Requirement Summary
- Requirement source file(s)
- Functional requirements found
- Non-functional requirements found
- Assumptions and gaps

2) User Stories
- Story ID
- Story
- Notes
- Acceptance Criteria (Gherkin)

3) INVEST Review
- I/N/V/E/S/T per story
- Revisions made

4) Process Flow Diagram
- Mermaid fenced code block

## Prompt Block: JIRA Ticket Generator
### Use When
- User stories and acceptance criteria need to be pushed to a JIRA board as tickets.

### Prompt Text
Convert the provided user stories and acceptance criteria into JIRA-formatted tickets. For each story:

1) Extract story details:
   - Story ID and title from the user story
   - Full Acceptance Criteria (Gherkin format)
   - Notes including dependencies, assumptions, and risks

2) Format for JIRA:
   - Summary: Use the story statement (As a..., I want..., so that...)
   - Description: Include business context and acceptance criteria
   - Issue Type: Story
   - Labels: Apply relevant labels based on story context

3) Use JIRA API tools to create tickets with:
   - Project key (to be provided by user)
   - Summary and description fields
   - Acceptance criteria as structured content

Required actions:
- Create JIRA tickets for each confirmed user story
- Return confirmation with ticket IDs and links
- Surface any errors or validation failures

Required output section:
- JIRA Tickets Created (with ticket IDs and links)
- Any failed tickets with error details
