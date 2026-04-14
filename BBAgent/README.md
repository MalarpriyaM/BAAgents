# BBAgent

This folder contains Business Analyst helpers for writing Jira-ready stories, generating acceptance criteria, and producing ticket diagrams.

## Contents

- `.github/agents/`
  - `shorena_bartaia_jira_agent.agent.md`: Creates or updates Jira-ready tickets from requirements.
  - `shorena_bartaia_story_writer.agent.md`: Converts requirements into short user stories with acceptance criteria.
  - `shorena_bartaia_acceptance_criteria_agent.agent.md`: Generates Gherkin acceptance criteria from a user story.
- `.github/prompts/`
  - `Jira_ticket.prompt.md`: Turns requirement text into Jira-ready tickets.
  - `diagram_prompt.prompt.md`: Produces a Mermaid diagram and draw.io XML for a Jira ticket.
- `diagrams/drawio/`
  - Reusable draw.io files for the Task Tracker example stories.

## How To Use

1. Open this repository in VS Code with GitHub Copilot Chat enabled.
2. Use the custom agents from `.github/agents/` when you want specialized BA output.
3. Use the prompt files from `.github/prompts/` as slash commands for repeatable ticket and diagram workflows.
4. Attach the `.drawio` files to Jira tickets when a visual flow is useful.

## Recommended Workflow

1. Start with the story writer agent to break requirements into stories.
2. Use the acceptance criteria agent to refine story testability.
3. Use the Jira ticket prompt or Jira agent to prepare or create tickets.
4. Use the diagram prompt and draw.io files to attach visuals to tickets.

## Notes

- The files in this folder are workspace-scoped customizations.
- Prompt and agent discovery depends on their frontmatter `description` fields.
- Jira labels and issue creation depend on your Jira permissions and project access.