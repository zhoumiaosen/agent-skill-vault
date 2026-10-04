# Agent Skill Vault

A storehouse for reusable AI-agent skills: focused instructions, useful references, and optional supporting scripts that make repeatable work easier to share and maintain.

This repository includes thirty-four public, licensed upstream skills. No installer or runtime integrations are included.

## Skill catalog

- [frontend-design](skills/frontend-design/SKILL.md) — Design guidance for distinctive web UIs. Requires a frontend-capable agent; screenshot/browser tools help with visual review. No runtime or assets bundled. License: Apache-2.0. [Source and compatibility](skills/frontend-design/SOURCE.md)
- [verification-before-completion](skills/verification-before-completion/SKILL.md) — Evidence-first completion checks. Requires access to the project's actual test/build commands; no tests are bundled. License: MIT. [Source and compatibility](skills/verification-before-completion/SOURCE.md)
- [receiving-code-review](skills/receiving-code-review/SKILL.md) — Evaluate review feedback before changing code. Requires repository context and test tools. GitHub reply examples assume gh CLI and appropriate authorization; these are not bundled. License: MIT. [Source and compatibility](skills/receiving-code-review/SOURCE.md)
- [create-technical-spike](skills/create-technical-spike/SKILL.md) — Time-boxed technical research documents. Uses Copilot-style ${input:...} placeholders and tool names; substitute actual values and map tools for other agents. Research and code execution access depend on the task. License: MIT. [Source and compatibility](skills/create-technical-spike/SOURCE.md)
- [documentation-writer](skills/documentation-writer/SKILL.md) — Diataxis tutorials, how-to guides, reference and explanations. Includes clarification/outline approval steps and restricts external browsing unless requested. No document conversion or PDF tools bundled. License: MIT. [Source and compatibility](skills/documentation-writer/SOURCE.md)

- [test-driven-development](skills/test-driven-development/SKILL.md) — Red/green/refactor and behavioral tests. Uses your existing test runner; npm examples are illustrative. Includes writing-good-tests.md. Its mention of superpowers:writing-skills applies only to testing agent-instruction documents; that separate skill is not bundled. License: MIT. [Source and compatibility](skills/test-driven-development/SOURCE.md)
- [dispatching-parallel-agents](skills/dispatching-parallel-agents/SKILL.md) — Split independent work into focused agents and verify integration. Requires a harness with subagent support; map dispatch examples to its tools. License: MIT. [Source and compatibility](skills/dispatching-parallel-agents/SOURCE.md)
- [create-implementation-plan](skills/create-implementation-plan/SKILL.md) — Phased implementation plans with dependencies, risks and tests. Replace Copilot-style input placeholders and adapt /plan/ to the intended workspace. POSIX command examples allow platform equivalents. License: MIT. [Source and compatibility](skills/create-implementation-plan/SOURCE.md)
- [create-architectural-decision-record](skills/create-architectural-decision-record/SKILL.md) — Record architecture decisions, alternatives and consequences. Replace Copilot-style input placeholders; adapt /docs/adr/ to your workspace. Requests missing context. License: MIT. [Source and compatibility](skills/create-architectural-decision-record/SOURCE.md)
- [context-map](skills/context-map/SKILL.md) — Map affected files, dependencies, tests and risks. Replace {{task_description}}; requires repository search/read and waits for map review before implementation. License: MIT. [Source and compatibility](skills/context-map/SOURCE.md)

### Game development

- [unity-debug](skills/unity-debug/SKILL.md) — Unity 6 debugging using Editor logs and Test Framework. Optional live-Editor commands need Unity CLI and com.unity.pipeline; neither is installed by this repository. [Source and compatibility](skills/unity-debug/SOURCE.md)
- [unity-profiling](skills/unity-profiling/SKILL.md) — Unity 6 performance analysis with bundled C# profiling templates and a Python 3 standard-library comparison script. Produces local diagnostic captures; validate APIs and performance claims on your project. [Source and compatibility](skills/unity-profiling/SOURCE.md)
- [unity-tilemap](skills/unity-tilemap/SKILL.md) — Unity 6 tilemap and RuleTile workflows for 2D levels. RuleTile templates require com.unity.2d.tilemap.extras. Editor utilities modify project assets; inspect paths and back up work first. [Source and compatibility](skills/unity-tilemap/SOURCE.md)
- [unity-2d-pixel-perfect](skills/unity-2d-pixel-perfect/SKILL.md) — Unity 6 pixel-art camera and sprite-import workflows. Choose the URP or built-in pipeline template for your project; do not copy both camera setups blindly. [Source and compatibility](skills/unity-2d-pixel-perfect/SOURCE.md)
- [game-design](skills/game-design/SKILL.md) — Engine-neutral guidance for mechanics, balance, progression and player experience. Markdown only; no engine integration required. [Source and compatibility](skills/game-design/SOURCE.md)

These are third-party instructions, not permission to act. Review cleanup and package commands before use: upstream examples may delete generated outputs or Temp files, restore package files, stop an Editor, or modify assets. Preserve unsaved work and local changes; adapt paths and obtain any required approval. Optional pointers to other upstream skills are not bundled. Templates have not been compiled in Unity or runtime-tested here.

### Additional game workflows

- [game-feel](skills/game-feel/SKILL.md) — Feedback, hit-stop, camera shake and responsive interactions. Apache-2.0. [Compatibility and known limitations](skills/game-feel/SOURCE.md)
- [save-systems](skills/save-systems/SKILL.md) — Save formats, versioning, backups and migration. Apache-2.0. [Compatibility and known limitations](skills/save-systems/SOURCE.md)
- [create-game-assets](skills/create-game-assets/SKILL.md) — Art direction, provenance and optional raster inspection/preview utilities. Apache-2.0. [Compatibility and known limitations](skills/create-game-assets/SOURCE.md)
- [game-ui-ux](skills/game-ui-ux/SKILL.md) — HUDs, menus, navigation and accessible layout. Apache-2.0. [Compatibility and known limitations](skills/game-ui-ux/SOURCE.md)

The asset utilities optionally require Python 3.10+ and Pillow >=10,<13. The upstream color-limit checker has a known off-by-one issue; verify color limits independently. Preview output can overwrite the specified file. Save-system and game-feel code are illustrative sketches, not production-ready drop-ins. No runtime tests have been performed.

### RPG systems additions

- [rpg](skills/rpg/SKILL.md) — Stats and leveling, inventory/equipment, combat formulas and quest state models. Engine-neutral pseudocode that composes with the existing save and UI skills. Apache-2.0. [Compatibility and known limitations](skills/rpg/SOURCE.md)
- [dialogue-systems](skills/dialogue-systems/SKILL.md) — Branching NPC conversations, narrative variables and localization, with Ink/Yarn guidance and a custom-runner reference. Apache-2.0. [Compatibility and known limitations](skills/dialogue-systems/SOURCE.md)
- [game-ai](skills/game-ai/SKILL.md) — NPC state machines, behavior trees, steering and A* pathfinding. Portable concepts with GDScript/Python examples; adapt to the project engine. Apache-2.0. [Compatibility and known limitations](skills/game-ai/SOURCE.md)
- [unity-scriptableobjects](skills/unity-scriptableobjects/SKILL.md) — Unity 6.3 LTS data assets, event channels and runtime registries, with C# examples. Keep shared definitions separate from per-character state and saves. Apache-2.0. [Compatibility and known limitations](skills/unity-scriptableobjects/SOURCE.md)
- [audio-design](skills/audio-design/SKILL.md) — Mixer/bus architecture, dialogue ducking, SFX variation and adaptive exploration/combat music. Adapt Godot-oriented examples to the chosen audio engine. Apache-2.0. [Compatibility and known limitations](skills/audio-design/SOURCE.md)

These five additions contain instruction and reference Markdown only; no installer, runtime integration or audio assets are bundled. Examples are guides to adapt and test, not production-ready drop-ins.

### Controls, levels and Godot foundations

- [unity-input-system](skills/unity-input-system/SKILL.md) — Unity Input Actions, gameplay/menu maps, device bindings and saved rebinding. Requires com.unity.inputsystem; add cancellation and lifecycle cleanup to the examples. Apache-2.0. [Compatibility and known limitations](skills/unity-input-system/SOURCE.md)
- [unity-animation](skills/unity-animation/SKILL.md) — Animator state transitions, locomotion blend trees, layers and humanoid IK. Treat completion timing as illustrative and test interruptions with the actual clips. Apache-2.0. [Compatibility and known limitations](skills/unity-animation/SOURCE.md)
- [level-design](skills/level-design/SKILL.md) — Authored blockouts, encounter pacing, exploration branches and key/ability gates. Validate progression with the actual traversal rules. Apache-2.0. [Compatibility and known limitations](skills/level-design/SOURCE.md)
- [procedural-gen](skills/procedural-gen/SKILL.md) — Seeded dungeons, noise, weighted loot and connectivity checks. Algorithm sketches need input validation, bounds checks, bounded retries and engine adaptation. Apache-2.0. [Compatibility and known limitations](skills/procedural-gen/SOURCE.md)
- [godot-fundamentals](skills/godot-fundamentals/SKILL.md) — Godot 4.x nodes, scenes, shared resources, typed GDScript, Input Map and editor verification. Check the installed engine version; headless import alone does not prove gameplay correctness. MIT. [Compatibility and known limitations](skills/godot-fundamentals/SOURCE.md)

These five packages contain instruction and reference Markdown only, with license notices and separate compatibility notes. No engine, integration, installer or executable is added. The copied examples have not been run in Unity or Godot. Related-skill names are optional pointers; upstream unity-tilemap-2d maps conceptually to the vault's existing unity-tilemap package.

### Localization, accessibility and integration checks

- [game-localization](skills/game-localization/SKILL.md) — Stable string IDs, locale/font fallbacks, dynamic formatting, and language changes that preserve gameplay state. Engine-neutral checklist; no translation service or engine integration bundled. MIT. [Source and compatibility](skills/game-localization/SOURCE.md)
- [a11y-controls](skills/a11y-controls/SKILL.md) — Action remapping, hold/toggle alternatives, scalable text, non-color cues, and reduced-flash/motion checks. Adapt to supported devices and preferences; not accessibility certification. MIT. [Source and compatibility](skills/a11y-controls/SOURCE.md)
- [cutscene-handoff](skills/cutscene-handoff/SKILL.md) — Safe cinematic entry, skip, interruption, and restoration of input, camera, UI, and gameplay state. No Timeline/Sequencer implementation included. MIT. [Source and compatibility](skills/cutscene-handoff/SOURCE.md)
- [collision-layers](skills/collision-layers/SKILL.md) — Stable collision/query categories and an interaction matrix for actors, attacks, hazards, camera probes, and IK. Map the policy to the actual engine's layers/masks; it does not implement physics or damage resolution. MIT. [Source and compatibility](skills/collision-layers/SOURCE.md)
- [requesting-code-review](skills/requesting-code-review/SKILL.md) — Independent review against requirements and an explicit Git revision range, including the complete reviewer prompt template. Requires Git and subagent support; review findings do not authorize merging. MIT. [Source and compatibility](skills/requesting-code-review/SOURCE.md)

The first four are unchanged, attributed discipline extracts from jammyfu/open-game-skills, whose full-pack installation guidance differs from this curated vault layout. Their directories contain only SKILL.md, with no direct local file links or runtime dependencies; named sibling skills are ownership pointers rather than bundled integrations. The vault does not include that pack's dispatcher, shared contract, or engine adapters. All five additions contain Markdown instructions and license notices only. They have been statically reviewed, not runtime-tested. See each SOURCE.md for packaging, engine, dispatch, and review-range limitations.

### Verification and licensing

The skill text is copied unchanged from pinned public upstream revisions. License copies and provenance accompany each skill. See [UPSTREAMS.json](UPSTREAMS.json) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). The original ten skills are instruction-only. The game-development collection also includes upstream C# templates and a Python comparison script; adding them here does not install or execute them. Content and links were reviewed, but cross-agent runtime behavior has not been tested. Each upstream license applies to its corresponding files; no blanket relicense is implied.

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
