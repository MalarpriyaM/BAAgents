---
applyTo: "**/*"
description: "Guidelines for creating and updating Jira user stories, including field values, story template, and acceptance criteria template"
---

# Jira User Story Creation Guidelines

Use these guidelines whenever creating or updating a user story.

## JIRA Field Mapping
1. Space - Choose 'My Product'
2. Work Type - Choose 'Story'
3. Status - Choose 'New'
4. Summary - Summary as per the guidelines provided.
5. Description - Description as per the guidelines provided.
6. Story Point Estimate - Story points as per the guidelines provided.

## Field Guidelines

### Summary
- Format: [EPIC_name] [Verb] [object] [context]
- Length: 10 to 80 characters
- Tone: concise, user-focused, and specific
- Bad examples: Login stuff, Fix bug
- Good example: [Authentication] Reset Password via email link

### Description

#### User Story:
Use this exact structure:
As a [role], I want [goal], so that [benefit].

Template:
- Role: who needs the capability
- Goal: what they want to do
- Benefit: why it matters

Example:
As a registered user, I want to reset my password by email link, so that I can regain access without contacting support.

#### Task
- Add a concise bullet list of tasks needed to complete the user story
- Keep each task action-oriented and implementation-light
- Recommended count: 3 to 7 tasks

#### Pre-requisite
- List conditions that must be true before the story can be started
- Include dependencies such as upstream features, access, environments, or approvals
- If none, explicitly state: None

#### Acceptance Criteria
Use the Gherkins format: Given/When/Then 

Template:
- Given [context]
- When [action]
- Then [outcome]

Guidelines:
- 2 to 8 criteria per story
- Testable and observable outcomes
- Include happy path and at least one edge/error case
- Avoid implementation details

Example:
- Given a registered user on the login page
- When they request a password reset with a valid email
- Then a reset link is sent within 2 minutes


#### Story Points
- Use numeric estimate
- Recommended scale: 1, 2, 3, 5, 8, 13
- If 13, split story before sprint commitment

#### Epic Link (Optional)
- Use parent epic key, for example PROJ-123
- Leave blank if no applicable epic

## Example

Summary
Reset Password from Login Page

Description
User Story:
As a registered user, I want to request a password reset link, so that I can regain access to my account when I forget my password.

Task:
- Add Forgot Password entry point on login page
- Validate email input and trigger reset link generation
- Handle expired or invalid reset link scenario
- Add neutral message for unregistered emails

Pre-requisite:
- Email service configuration is complete
- User account table includes verified email flag
- Security policy for reset link expiry is approved

Notes (Optional)
- Dependencies: Email delivery service is operational.
- Assumptions: Reset links expire after 24 hours.
- Out of scope: Multi-factor authentication reset flow.

Acceptance Criteria:
1. Given a registered user is on the login page, when they select Forgot Password and submit a valid email, then a reset link is sent within 2 minutes.
2. Given a user submits an unregistered email, when they request a reset link, then the system shows a neutral confirmation message without revealing account existence.
3. Given a user opens an expired reset link, when they attempt to set a new password, then the system blocks the action and prompts them to request a new link.

Story Points
5

Epic Link (Optional)
AUTH-120

## Definition of Ready Checklist
- Summary is clear and action-oriented
- Description follows As a / I want / so that
- Acceptance criteria are testable
- Story points are assigned
- Dependencies and assumptions are documented