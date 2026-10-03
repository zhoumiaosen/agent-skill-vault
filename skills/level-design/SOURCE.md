# Source and compatibility: level-design

## Provenance

- Upstream: [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)
- Pinned revision: `d4b0e35550c55ae70bdfcab4ef5a0e94610438a9`
- Original package: [skills/disciplines/level-design](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/d4b0e35550c55ae70bdfcab4ef5a0e94610438a9/skills/disciplines/level-design)
- Retrieved: 2026-10-03
- License: [Apache-2.0](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/d4b0e35550c55ae70bdfcab4ef5a0e94610438a9/LICENSE); the complete upstream LICENSE is included here
- Every upstream file in this skill directory is copied unchanged. Root license notices are copied unchanged alongside it. This SOURCE.md is vault-authored and separate from upstream instructions
- Git blob hashes and paths are recorded in [UPSTREAMS.json](../../UPSTREAMS.json)

## Included files

- `SKILL.md`
- `references/pacing-and-flow.md`
- `LICENSE`
- `NOTICE`

The complete upstream NOTICE is included. Retain LICENSE, NOTICE, and upstream attribution when redistributing.

## Compatibility and requirements

- Engine-neutral authored-level guidance: blockout, traversal metrics, critical paths, encounters, gating, pacing, and playtesting. GDScript examples are illustrative data; adapt them to Unity/C# or another engine
- No engine integration, level assets, or executable validation tools are bundled. Meaningful validation requires the actual movement rules, collision geometry, camera, and playtests
- Upstream's `unity-tilemap-2d` pointer is not the name of the vault's existing `unity-tilemap` skill; that existing package provides related Unity tilemap coverage. Other named companion skills are optional pointers, not automatically bundled

## Known limitations and safety

- The sample room graph requires `red_key` before the boss without showing a source for that key. It illustrates a validation problem; it is not a complete, proven-solvable level
- Connectivity alone does not establish progression. Validate states that include keys/abilities, resource costs, one-way transitions, and legal return/reset paths, using the player's actual traversal metrics
- Pacing curves, safe-gap percentages, encounter ordering, and teaching rules are starting heuristics. Adapt them to the intended RPG experience instead of treating them as universal requirements
- Blockout and dressing changes affect project assets. Preserve authored content and use measured playtest evidence before claiming a level works

## Verification performed for this copy

- Checked the complete pinned directory inventory and all local reference-file targets
- Compared every copied file's UTF-8 bytes with its upstream Git blob SHA; LICENSE and any NOTICE are included in that check
- Reviewed the instructions and examples statically. No upstream code, Unity/Godot project, engine tests, or cross-agent runtime behavior was executed or validated
- These instructions do not grant permission to install software, modify unrelated assets, publish data, or perform destructive actions
