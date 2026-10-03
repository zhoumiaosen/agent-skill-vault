# Source and compatibility: unity-input-system

## Provenance

- Upstream: [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)
- Pinned revision: `d4b0e35550c55ae70bdfcab4ef5a0e94610438a9`
- Original package: [skills/unity/unity-input-system](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/d4b0e35550c55ae70bdfcab4ef5a0e94610438a9/skills/unity/unity-input-system)
- Retrieved: 2026-10-03
- License: [Apache-2.0](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/d4b0e35550c55ae70bdfcab4ef5a0e94610438a9/LICENSE); the complete upstream LICENSE is included here
- Every upstream file in this skill directory is copied unchanged. Root license notices are copied unchanged alongside it. This SOURCE.md is vault-authored and separate from upstream instructions
- Git blob hashes and paths are recorded in [UPSTREAMS.json](../../UPSTREAMS.json)

## Included files

- `SKILL.md`
- `references/rebinding.md`
- `LICENSE`
- `NOTICE`

The complete upstream NOTICE is included. Retain LICENSE, NOTICE, and upstream attribution when redistributing.

## Compatibility and requirements

- Targets Unity 6.3 LTS and `com.unity.inputsystem` 1.x. Check the installed Unity and package versions before using the examples
- Requires a Unity project, configured Input Actions, suitable device bindings, and access to the Editor/Input Debugger for interactive verification. No package, Editor integration, or input asset is installed by this vault
- The `input-systems`, `unity-csharp-scripting`, and `unity-physics` names are optional upstream companion pointers, not bundled dependencies. The vault's existing save-systems skill can help with persistence

## Known limitations and safety

- The rebinding snippet disposes its operation on successful completion only. Add cancellation handling and disable/destroy cleanup, prevent overlapping operations, restore the intended action/map state, and handle composite parts and invalid binding indices
- The event-callback example unsubscribes in OnDisable but does not disable the map there. Give subscriptions, maps, and rebinding operations an explicit lifecycle owner
- Polling held values and detecting press edges serve different purposes. Configure action types and interactions deliberately; `performed` is not universally a once-per-press event
- The movement example is an illustration, not a collision-aware character controller. Adapt it to the project's physics and update loop
- Examples write rebinding preferences and change enabled input contexts when used. Review those changes, preserve existing bindings, and test keyboard/gamepad/menu transitions and cancel paths

## Verification performed for this copy

- Checked the complete pinned directory inventory and all local reference-file targets
- Compared every copied file's UTF-8 bytes with its upstream Git blob SHA; LICENSE and any NOTICE are included in that check
- Reviewed the instructions and examples statically. No upstream code, Unity/Godot project, engine tests, or cross-agent runtime behavior was executed or validated
- These instructions do not grant permission to install software, modify unrelated assets, publish data, or perform destructive actions
