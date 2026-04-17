# Custom Agents Registry

This document registers all custom agents available in the BAAgents workspace.

## Active Agents

### venera_evteeva_requirements_jira_story_publisher

**Name**: `venera_evteeva_requirements_jira_story_publisher`

**Location**: `.github/agents/venera_evteeva_requirements_jira_story_publisher.agent.md`

**Purpose**: Analyze business requirements and generate high-quality Jira user stories, then publish them to Jira via MCP.

**When to Use**:
- Converting requirements into Jira-ready user stories
- Creating backlog items from business requirements
- Publishing stories to Jira with acceptance criteria and traceability
- BA-driven story generation workflows

**Trigger Phrases**:
- requirements to user stories
- write Jira stories
- publish to Jira
- backlog creation
- BA story generation

**Key Behavior**:
1. Always previews stories before publishing
2. Requires explicit confirmation to publish
3. Generates only Jira `Story` issue type (no Epics, Tasks, or Bugs)
4. Enforces review checkpoint for story refinement
5. Uses MCP Atlassian/Jira integration for publication

**Tools**:
- `vscode` — VS Code environment
- `read` — File reading
- `com.atlassian/atlassian-mcp-server/*` — Jira MCP integration
- `search` — Text/semantic search
- `azure-mcp/search` — Azure search (for context)

**Input Requirements**:
- Business requirements text
- Jira project key (e.g., `GitHub Copilot VE`)
- Jira cloud/site identifier (e.g., `veneraevteeva.atlassian.net`)

**Output**:
- Preview of generated user stories
- Review confirmation state
- Created Jira issue keys/IDs
- Traceability map to requirements
- Risk/assumption summary

**Supporting Files**:
- `.github/prompts/venera_evteeva_requirements_to_jira_stories.prompt.md` — Story transformation rules
- `.github/instructions/venera_evteeva_publish_user_stories_to_jira.instructions.md` — Jira publishing playbook

---

## Agent Configuration Standards

All custom agents in this workspace follow these standards:

- **Location**: `.github/agents/<agent-name>.agent.md`
- **Naming**: `firstname_lastname_<agent-name>.agent.md`
- **Frontmatter**: Required fields: `name`, `description`, `tools`, `user-invocable`
- **Discovery**: Registered in this AGENTS.md file with trigger phrases and behavior summary
- **Tools**: Explicit tool list to enforce scope and prevent misuse
- **Documentation**: Linked supporting files (prompts, instructions, skills)

---

## How to Invoke

### From Chat
Select the agent from the agent picker (Ctrl+Shift+;) and search for `venera_evteeva_requirements_jira_story_publisher`.

### As a Subagent
Other agents can delegate to this agent by referencing its name in their subagent declarations.

### Example Prompts
- "Analyze these requirements and generate Jira user stories in preview mode."
- "Convert these business requirements into Story issues for project `GitHub Copilot VE`."
- "Create stories with INVEST principles and publish to Jira after review."
