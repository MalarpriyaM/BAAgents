---
name: venera_evteeva_requirements_to_jira_stories
description: "Transform requirement input into high-quality Jira-ready user stories with acceptance criteria, priority hints, and traceability."
argument-hint: "Paste requirements and optionally include domain context, constraints, and non-functional requirements."
---
Convert provided requirements into Jira-ready user stories.

## Input
Use the user-provided requirements as the source of truth.
If present, use:
- Product/domain context
- Functional requirements
- Non-functional requirements
- Dependencies
- Constraints
- Stakeholders

## Transformation Rules
1. Break requirements into independent, vertically sliced user stories.
2. Generate only user stories for Jira `Story` issue type (no Epics, Tasks, Bugs, or Sub-tasks).
3. Use standard story format: 
   - **Title**
   - **User Story**: "As a <role>, I want <capability>, so that <benefit>."
   - **Acceptance Criteria** (prefer Given/When/Then)
   - **Definition of Done Notes** (optional)

4. Keep each story testable, unambiguous, and implementable in one sprint when possible.
5. If information is missing, add an **Open Questions** section instead of guessing to the comments.
6. If non-functional requirements are present, create separate stories for them with clear acceptance criteria.
7. Follow INVEST principles: Independent, Negotiable, Valuable, Estimable, Small, Testable.

## Quality Bar
- Stories should follow INVEST as much as possible.
- Acceptance criteria must be measurable and test-oriented.
- Use precise language; avoid vague terms like "fast" or "user-friendly" without criteria.

## Output Format
Return:
1. `User Stories` (numbered list with full fields)
2. `Open Questions / Assumptions`
3. `Suggested Jira Labels` (optional)

After generating stories, hand off to Jira publishing instructions for actual issue creation when requested.
