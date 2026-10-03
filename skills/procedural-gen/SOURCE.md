# Source and compatibility: procedural-gen

## Provenance

- Upstream: [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)
- Pinned revision: `d4b0e35550c55ae70bdfcab4ef5a0e94610438a9`
- Original package: [skills/disciplines/procedural-gen](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/d4b0e35550c55ae70bdfcab4ef5a0e94610438a9/skills/disciplines/procedural-gen)
- Retrieved: 2026-10-03
- License: [Apache-2.0](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/d4b0e35550c55ae70bdfcab4ef5a0e94610438a9/LICENSE); the complete upstream LICENSE is included here
- Every upstream file in this skill directory is copied unchanged. Root license notices are copied unchanged alongside it. This SOURCE.md is vault-authored and separate from upstream instructions
- Git blob hashes and paths are recorded in [UPSTREAMS.json](../../UPSTREAMS.json)

## Included files

- `SKILL.md`
- `references/dungeon-generation.md`
- `references/noise.md`
- `LICENSE`
- `NOTICE`

The complete upstream NOTICE is included. Retain LICENSE, NOTICE, and upstream attribution when redistributing.

## Compatibility and requirements

- Engine-neutral algorithm guidance with Python/GDScript sketches for seeded RNG, noise, rooms/corridors, BSP, caves, reachability, and loot tables. Adapt the data structures and APIs to the project
- Noise-library names are optional implementation choices, not installed dependencies. Pin the chosen engine, RNG, noise library, generator version, and parameters when reproducibility matters
- Upstream's `unity-tilemap-2d` pointer differs from the vault's existing `unity-tilemap` name. Existing game-ai, save-systems, and RPG skills provide adjacent coverage; other named skills are optional upstream pointers

## Known limitations and safety

- Treat the snippets as sketches, including those described upstream as a complete generator. Helpers such as clamp, carving functions, rectangle operations, and BSP node methods are not implemented in the package
- Add bounds checks to reachable_floor before indexing. Closed-border assumptions must be explicit; malformed inputs or an open boundary can invalidate the sample's safety
- Bound random-walk iterations and validate dimensions, target ratios, room sizes, and retry budgets. The shown drunkard walk can fail to terminate when the target exceeds the reachable interior; diagonal steps also do not establish four-neighbor connectivity
- Validate weighted tables for empty input, invalid/negative/non-finite weights, and a positive total before selection. Add failure/repair behavior instead of relying on the fallback return
- Prefer an owned RNG instance. The suggested UnityEngine.Random.InitState changes global RNG state and conflicts with the isolation principle elsewhere in the skill. A seed alone does not guarantee identical output across engine/library/generator versions or changed draw order
- Validate spawn safety, exit reachability, key/ability order, and a stated corpus of seeds. Record and reproduce failed seeds; do not infer correctness for every seed from a small successful sample

## Verification performed for this copy

- Checked the complete pinned directory inventory and all local reference-file targets
- Compared every copied file's UTF-8 bytes with its upstream Git blob SHA; LICENSE and any NOTICE are included in that check
- Reviewed the instructions and examples statically. No upstream code, Unity/Godot project, engine tests, or cross-agent runtime behavior was executed or validated
- These instructions do not grant permission to install software, modify unrelated assets, publish data, or perform destructive actions
