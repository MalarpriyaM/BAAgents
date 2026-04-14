---
description: "Use when publishing generated user stories to Jira via MCP tools. Enforces a safe and consistent publish flow."
applyTo: "**"
---
# Publish User Stories to Jira (MCP)

Follow this sequence whenever the task includes publishing stories to Jira.

## 0) MCP Atlassian Setup (Prerequisites)
Before any Jira operations, ensure MCP Atlassian connection is available:
- **MCP Server**: `com.atlassian` (Jira MCP integration)
- **Authentication**: Requires valid Atlassian cloud credentials and API token/OAuth access
- **Required Parameters**:
  - `cloudId`: Jira cloud instance ID (UUID or site hostname, e.g., `veneraevteeva.atlassian.net`)
  - `projectKey`: Target Jira project key (e.g., `PROJ` or `GitHub Copilot VE`)

If MCP Atlassian tools are unavailable, stop and request user enable Jira MCP integration.

## 1) Generate Preview First (Mandatory)
Before any publish attempt:
- Generate and present a preview of user stories.
- Ask for explicit review decision:
  - `confirm_publish` to proceed, or
  - `reiterate_stories` to refine and preview again.

Never publish before explicit `confirm_publish`.

## 2) Validate Required Inputs
Before publishing, ensure you have:
- Jira cloud/site identifier (`https://veneraevteeva.atlassian.net`)
- Jira project key (e.g., `GitHub Copilot VE`)
- Issue type fixed to `Story`
- Story payloads (title, story text, acceptance criteria)

If any required input is missing, stop and request only missing values.

## 3) Build Jira Issue Payload
For each story:
- `summary` = story title
- `description` = combine:
  - user story statement
  - acceptance criteria
  - UI notes (if present)
- `issueTypeName` = `Story`
- Include labels/components if available and supported

 

Use Markdown content format unless the user requests ADF.

## 4) Publish via MCP
Create each issue using Jira MCP create issue capability:

**MCP Tool**: `mcp_com_atlassian_createJiraIssue` (or equivalent)

**Parameters**:
- `cloudId` — Jira cloud instance ID (e.g., `veneraevteeva.atlassian.net`)
- `projectKey` — Target project key (e.g., `PROJ` or `GitHub Copilot VE`)
- `issueTypeName` — Set to `Story` only
- `summary` — Story title
- `description` — Combined story details (story text + acceptance criteria + dependencies)
- `labels` (optional) — Story-relevant labels from prompt output
- `components` (optional) — If applicable

**MCP Call Format**:
```
mcp_com_atlassian_createJiraIssue(
  cloudId="veneraevteeva.atlassian.net",
  projectKey="GitHub Copilot VE",
  issueTypeName="Story",
  summary="<story title>",
  description="<story body with acceptance criteria>"
)
```

If labels/components are available and supported, include them in the MCP call.

## 5) Failure Handling
- If one story fails, continue with remaining stories unless user says stop-on-error.
- Capture and report per-story failure reason.
- Provide retry recommendations for failed items.

## 6) Final Report
Always return:
- Publish mode used (`preview` or `publish`)
- Review decision (`confirm_publish` or `reiterate_stories`)
- Created issue keys/IDs
- Failed items with reasons
- Next actions (e.g., add links, assign owners, transition status)

## 7) Safety and Quality
- Never fabricate Jira IDs, keys, or success statuses.
- Never claim publication unless issue creation returned success.
- Preserve requirement intent; do not alter business meaning during publish formatting.
- Never create Jira issue types other than `Story`.
