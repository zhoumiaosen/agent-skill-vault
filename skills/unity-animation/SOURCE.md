# Source and compatibility: unity-animation

## Provenance

- Upstream: [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)
- Pinned revision: `d4b0e35550c55ae70bdfcab4ef5a0e94610438a9`
- Original package: [skills/unity/unity-animation](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/d4b0e35550c55ae70bdfcab4ef5a0e94610438a9/skills/unity/unity-animation)
- Retrieved: 2026-10-03
- License: [Apache-2.0](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/d4b0e35550c55ae70bdfcab4ef5a0e94610438a9/LICENSE); the complete upstream LICENSE is included here
- Every upstream file in this skill directory is copied unchanged. Root license notices are copied unchanged alongside it. This SOURCE.md is vault-authored and separate from upstream instructions
- Git blob hashes and paths are recorded in [UPSTREAMS.json](../../UPSTREAMS.json)

## Included files

- `SKILL.md`
- `references/blend-trees-and-ik.md`
- `LICENSE`
- `NOTICE`

The complete upstream NOTICE is included. Retain LICENSE, NOTICE, and upstream attribution when redistributing.

## Compatibility and requirements

- Targets Unity 6.3 LTS Animator/Animator Controller workflows. Humanoid IK requires a valid Humanoid Avatar and an enabled IK Pass on the intended layer
- Existing animation clips, rigs, controller parameters, layers, and masks must be configured in the project. No clips, models, Animator assets, or runtime integration are bundled
- `unity-csharp-scripting` and `unity-physics` are optional upstream companion pointers, not bundled dependencies. The vault already includes game-ai. Timeline is outside this skill's scope

## Known limitations and safety

- `WaitForSeconds(stateInfo.length)` is only an approximate sketch, not a reliable completion or combat-authority signal. It does not establish the correct state, transition progress, playback speed, interruptions, or looping behavior. Use an appropriate state/event contract and test cancellation and interruption
- The CrossFade example's "0.1s normalized" comment is ambiguous: [Animator.CrossFade](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Animator.CrossFade.html) uses normalized transition duration; CrossFadeInFixedTime uses seconds
- Animator.StringToHash caches a string hash; it does not validate that a parameter exists or make a misspelled name correct. Validate controller/parameter contracts explicitly
- The main workflow favors parameter-driven transitions, while a later example uses a direct CrossFade for a deliberate hit reaction. Pick and document the intended authority rather than treating the workflow's "never" as an absolute rule
- Coordinate animation/root motion with gameplay movement and clear unused IK/layer weights. Test actual clips in the intended Unity version before relying on them

## Verification performed for this copy

- Checked the complete pinned directory inventory and all local reference-file targets
- Compared every copied file's UTF-8 bytes with its upstream Git blob SHA; LICENSE and any NOTICE are included in that check
- Reviewed the instructions and examples statically. No upstream code, Unity/Godot project, engine tests, or cross-agent runtime behavior was executed or validated
- These instructions do not grant permission to install software, modify unrelated assets, publish data, or perform destructive actions
