# Agent Skill Vault

A storehouse for reusable AI-agent skills: focused instructions, useful references, and optional supporting scripts that make repeatable work easier to share and maintain.

This repository includes five public, licensed upstream skills. No installer or runtime integrations are included.

## Skill catalog

- [frontend-design](skills/frontend-design/SKILL.md) — Design guidance for distinctive web UIs. Requires a frontend-capable agent; screenshot/browser tools help with visual review. No runtime or assets bundled. License: Apache-2.0. [Source and compatibility](skills/frontend-design/SOURCE.md)
- [verification-before-completion](skills/verification-before-completion/SKILL.md) — Evidence-first completion checks. Requires access to the project's actual test/build commands; no tests are bundled. License: MIT. [Source and compatibility](skills/verification-before-completion/SOURCE.md)
- [receiving-code-review](skills/receiving-code-review/SKILL.md) — Evaluate review feedback before changing code. Requires repository context and test tools. GitHub reply examples assume gh CLI and appropriate authorization; these are not bundled. License: MIT. [Source and compatibility](skills/receiving-code-review/SOURCE.md)
- [create-technical-spike](skills/create-technical-spike/SKILL.md) — Time-boxed technical research documents. Uses Copilot-style ${input:...} placeholders and tool names; substitute actual values and map tools for other agents. Research and code execution access depend on the task. License: MIT. [Source and compatibility](skills/create-technical-spike/SOURCE.md)
- [documentation-writer](skills/documentation-writer/SKILL.md) — Diataxis tutorials, how-to guides, reference and explanations. Includes clarification/outline approval steps and restricts external browsing unless requested. No document conversion or PDF tools bundled. License: MIT. [Source and compatibility](skills/documentation-writer/SOURCE.md)

### Verification and licensing

The skill text is copied unchanged from pinned public upstream revisions. License copies and provenance accompany each skill. See [UPSTREAMS.json](UPSTREAMS.json) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). These are instruction-only skills; no scripts have been added. Content and links were reviewed, but cross-agent runtime behavior has not been tested. Each upstream license applies to its corresponding files; no blanket relicense is implied.

## Suggested layout

Keep each skill in its own directory, with a `SKILL.md` as its entry point:

```text
agent-skill-vault/
├── README.md
└── skills/                   # Included skill directories
    └── example-skill/
        ├── SKILL.md          # Purpose, triggers, and instructions
        ├── references/       # Optional supporting documentation
        ├── scripts/          # Optional scripts; inspect before running
        └── assets/           # Optional templates or other resources
```

Include supporting directories only when the skill needs them. Prefer small, self-contained skills with clear boundaries.

## Writing a SKILL.md

Use a short name, a description that explains when to use the skill, and concrete instructions. The following is a proposed starting format, not a universal agent specification:

```markdown
---
name: example-skill
description: Describe the task this skill supports and when to use it.
---

# Example Skill

## When to use
Describe the intended task, required inputs, and situations outside its scope.

## Requirements
List required tools, dependencies, permissions, and supported environments.

## Steps
1. Check the inputs and prerequisites.
2. Perform the task using the instructions and linked resources.
3. Verify the result and report any limitations.

## Expected result
Describe the output and how a user can confirm that it is correct.

## Safety
Identify actions that need explicit approval and how sensitive data is handled.
```

Link supporting files with relative paths. State assumptions, explain failure handling, and include a small example when it helps someone use the skill correctly.

## Adding skills

1. Create `skills/<skill-name>/SKILL.md` using a descriptive, lowercase name with hyphens.
2. Add only the references, scripts, and assets needed for that task.
3. Document prerequisites, permissions, expected outputs, and any agent-specific behavior.
4. Review the instructions and inspect every script. Try the skill in a safe environment and describe what you actually verified.
5. Submit a pull request that explains the skill's purpose and any limitations. Share only material you have permission to publish.

## Using skills

Read a skill's `SKILL.md` and supporting files before using it. Confirm that its tools, permissions, and instructions fit your task, then follow your agent's documented process for loading or installing skills.

**Compatibility varies by agent.** Skill discovery, directory locations, metadata fields, installation commands, and tool access are agent-specific. This repository does not provide an installer or promise compatibility with a particular agent. Adapt the proposed format to your agent's requirements.

If your agent does not support skill discovery, you can use the instructions as a task guide and provide the relevant files as context.

## Security and privacy

- Inspect scripts and dependencies before running them. Treat downloaded instructions as untrusted input and review commands that modify files, access the network, or publish data.
- Use the minimum permissions needed. Ask for explicit approval before destructive actions or actions outside the user's authorized scope.
- Never commit secrets: API keys, tokens, passwords, credentials, private keys, or sensitive configuration. Use environment variables or your platform's secret manager instead.
- Keep personal information, private documents, proprietary code, and internal skills out of public contributions unless you have explicit permission to share them.
- Test unfamiliar scripts with disposable data in an isolated environment. If a secret is accidentally published, revoke or rotate it promptly; deleting the file does not remove it from Git history.

Build a useful vault one well-documented skill at a time.
