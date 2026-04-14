# BAAgents Workspace Instructions

## Project Purpose
This repo collects BA/PM agent and skill files from global BAs for the BA Agent challenge session. Contributions are evaluated against defined criteria.

## File Naming Convention
**All agent and skill files must be named:**
```
firstname_lastname_<agentname_or_skillname>.ext
```
- Prefix = EPAM email ID (part before `@epam.com`)
- Lowercase letters and underscores only — no spaces, hyphens, or special characters

Examples: `john_smith_lead_qualifier.py`, `priya_kumar_requirements_extractor.md`

## Contribution Workflow
Always follow this order:
1. `git pull origin main` — sync before any changes
2. Add/edit your file
3. `git add <file>` then `git commit -m "Add <agentname> agent by <firstname_lastname>"`
4. `git push origin main`

## Branch Policy
- Single branch: `main`
- Never create new branches
- Never push without pulling first

## Agent Files
- Stored in `.github/agents/`
- Must be `.agent.md` format with valid YAML frontmatter (`name`, `description`, `tools`)

## BA Best Practices — BABOK Alignment
All BA activities, agent behaviors, and skill outputs must follow **BABOK (Business Analysis Body of Knowledge)** best practices:
- **Requirements elicitation**: Use structured techniques (interviews, workshops, observation, surveys)
- **Requirements analysis & design**: Classify requirements by type (Business, Stakeholder, Solution, Transition)
- **Requirements life cycle management**: Trace, prioritize, and maintain requirements through changes
- **Solution evaluation**: Validate that outputs meet business needs and acceptance criteria
- **Stakeholder engagement**: Identify stakeholders, understand their needs, and communicate appropriately
- Agents generating user stories, acceptance criteria, or gap analyses should reference the relevant BABOK knowledge area where applicable

## What NOT to Do
- Do not create branches
- Do not commit files with spaces or hyphens in the name
- Do not push without a `git pull` first
- Do not duplicate README content — see [README.md](../README.md) for full details
