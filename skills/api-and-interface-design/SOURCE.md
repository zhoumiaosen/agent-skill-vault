# Source and adaptation

This package is an adapted and substantially rewritten derivative of `api-and-interface-design` from **Addy Osmani's agent-skills** repository. It is not an unmodified upstream release.

- Upstream repository: https://github.com/addyosmani/agent-skills
- Pinned source revision: `1401c8b8030e023baeebb31781a6653fe8e93026`
- Original copyright: Copyright (c) 2025 Addy Osmani
- License: MIT; the original full notice is retained in [LICENSE](LICENSE)
- Adaptation date: 2026-10-04 (UTC)
- Adaptation purpose: Unity RPG/game-development workflows, with portable principles for Godot, Unreal Engine and backend work
- Status: review draft; not installed or published to a repository

## Source files read

- [skills/api-and-interface-design/SKILL.md](https://github.com/addyosmani/agent-skills/blob/1401c8b8030e023baeebb31781a6653fe8e93026/skills/api-and-interface-design/SKILL.md)
- [LICENSE](https://github.com/addyosmani/agent-skills/blob/1401c8b8030e023baeebb31781a6653fe8e93026/LICENSE)

## Changes

Reframed the skill around Unity C# module boundaries, commands/results/events, object and asynchronous lifetimes, resource ownership, save compatibility and durable reward deduplication. Made backend/network semantics conditional. Removed HTTP-first naming defaults, universal pagination rules, and blanket assumptions that additive fields or internal data are always safe.

The upstream concepts and licensed material retain their original attribution. New adaptation text is provided under the same MIT terms. No endorsement by Addy Osmani, Unity, Godot, Epic Games or any other vendor is stated or implied.

## Packaging boundaries

This package contains instructions and attribution only. It has no automatic installation, hooks, plugin configuration, executable guard, or dependency on another skill. Official documentation links are reading references, not permission to execute examples. Operational instructions are self-contained in SKILL.md; LICENSE and SOURCE.md travel with that file when copied.

