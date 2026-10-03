# Source and compatibility: godot-fundamentals

## Provenance

- Upstream: [pbzona/godot-skills](https://github.com/pbzona/godot-skills)
- Pinned revision: `0ad8f3c58d54580a57a1a6de3cd345a1d9376e3d`
- Original package: [skills/godot-fundamentals](https://github.com/pbzona/godot-skills/tree/0ad8f3c58d54580a57a1a6de3cd345a1d9376e3d/skills/godot-fundamentals)
- Retrieved: 2026-10-03
- License: [MIT](https://github.com/pbzona/godot-skills/blob/0ad8f3c58d54580a57a1a6de3cd345a1d9376e3d/LICENSE); the complete upstream LICENSE is included here
- Every upstream file in this skill directory is copied unchanged. Root license notices are copied unchanged alongside it. This SOURCE.md is vault-authored and separate from upstream instructions
- Git blob hashes and paths are recorded in [UPSTREAMS.json](../../UPSTREAMS.json)

## Included files

- `SKILL.md`
- `references/editor-debugging.md`
- `references/nodes-scenes-resources.md`
- `references/typed-gdscript-input.md`
- `LICENSE`

Retain the complete MIT copyright and permission notice when redistributing.

## Compatibility and requirements

- Targets Godot 4.x and typed GDScript. Inspect the actual installed editor version and project conventions; project.godot feature markers alone may not establish an exact patch version
- Execution requires an appropriate Godot editor and project. No editor, MCP bridge, plugin installer, scenes, or runtime scripts are bundled
- The programming-patterns and game-architecture names are optional upstream scope pointers, not included skill dependencies. This package covers the foundational node/scene/resource/input workflow

## Known limitations and safety

- This is a small, relatively new upstream package. Treat its examples as guidance to validate in the selected Godot release, not a compatibility guarantee
- Headless editor import/parse checks do not prove visual layout, input, audio, physics, or gameplay correctness. Run the affected scene, the project entry point, existing tests, and relevant device/editor checks separately
- A failed `instantiate() as Node2D` cast can discard the reference to an already allocated node. When adapting the spawning examples, keep the original Node reference, validate its type, and free rejected instances safely; validate nullable PackedScene slots as well
- Runtime parent/lifetime responsibility and Godot's Node.owner serialization property are related but distinct. Set and verify Node.owner explicitly when tooling needs generated children saved into a PackedScene
- Preserve source assets, .uid files, project settings, and existing input bindings. The suggested headless editor command may generate import/cache data; it has not been run for this publication

## Verification performed for this copy

- Checked the complete pinned directory inventory and all local reference-file targets
- Compared every copied file's UTF-8 bytes with its upstream Git blob SHA; LICENSE and any NOTICE are included in that check
- Reviewed the instructions and examples statically. No upstream code, Unity/Godot project, engine tests, or cross-agent runtime behavior was executed or validated
- These instructions do not grant permission to install software, modify unrelated assets, publish data, or perform destructive actions
