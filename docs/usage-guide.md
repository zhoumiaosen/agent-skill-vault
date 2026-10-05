# Task-based usage guide

[Chinese version](usage-guide.zh-CN.md)

Start with the task you need to complete, then read the relevant skill package.
The [catalog](../README.md) remains the list of available skills; this guide shows
how to choose and combine them. These are instructions and supporting material,
not an installed game framework. No engine or model execution is claimed here.

## Start with a small scope

Choose one primary skill. Add another only when the task crosses its boundary;
do not load every skill into every request. Read its `SKILL.md`, `SOURCE.md` and
needed references/resources before acting. When copying a package, retain all
supporting files and its license/NOTICE. Your host determines how instructions
are loaded; mentioning a skill name in a prompt does not install it or prove the
host discovered it. If discovery is unavailable, provide the package as context.

Include the actual project root, engine/package versions, target platform,
reproduction or desired behavior, affected files, and available test tools.
The prompts below are starting requests: replace bracketed inputs with real
values and keep the work inside the permissions you granted.

| What you need | Start here |
|---|---|
| Decide what to build | [Game direction](#game-direction) |
| Plan a change | [Map and plan](#map-and-plan), [versions and contracts](#versions-and-contracts) |
| Build RPG systems | [Inventory and saves](#inventory-and-saves), [combat and enemies](#combat-and-enemies), [dialogue and audio](#dialogue-localization-and-audio) |
| Build player-facing controls | [UI](#ui-and-accessibility), [input](#input), [animation](#animation-and-cutscenes) |
| Build worlds and assets | [Levels](#levels-and-generation), [tilemaps and pixel art](#tilemaps-pixel-art-and-assets) |
| Investigate or verify | [Debugging or profiling](#debugging-or-profiling), [tests and review](#tests-and-code-review) |
| Start in Godot, document, or split work | [Godot](#godot-starter), [documentation](#documentation), [parallel work](#parallel-work) |

## Game direction

Start with [game-design](../skills/game-design/SKILL.md)
([caveats](../skills/game-design/SOURCE.md)) for mechanics, progression and a
small playable loop. Use [rpg](../skills/rpg/SKILL.md)
([caveats](../skills/rpg/SOURCE.md)) when stats, equipment, combat or quest rules
need an RPG model. If a technical choice is unresolved, use
[create-technical-spike](../skills/create-technical-spike/SKILL.md)
([caveats](../skills/create-technical-spike/SOURCE.md)) for a bounded experiment.

**Context:** Player goals, one representative encounter, existing
rules and scope; for a spike, the question, time limit and available sandbox.

**Evidence:** A concrete loop and acceptance examples; then actual
playtest observations or experiment output when tools exist. Formula sketches
alone do not establish balance.

> Example: Read game-design. Propose one playable loop for [RPG concept], with a concrete encounter and acceptance criteria. List what needs a playtest; do not claim the design has been tested.

## Map and plan

Use [context-map](../skills/context-map/SKILL.md)
([caveats](../skills/context-map/SOURCE.md)) to find affected files and owners;
then [create-implementation-plan](../skills/create-implementation-plan/SKILL.md)
([caveats](../skills/create-implementation-plan/SOURCE.md)) for ordered work and
verification. Record a consequential choice with
[create-architectural-decision-record](../skills/create-architectural-decision-record/SKILL.md)
([caveats](../skills/create-architectural-decision-record/SOURCE.md)), rather than
creating an ADR for every small edit. Map review is part of context-map's process.

**Context:** Repository access, actual task, current tests, relevant
assets/assemblies and constraints. Replace upstream input placeholders and
document paths with your project's conventions.

**Evidence:** File-backed dependency map, reviewed plan, explicit
acceptance commands and decision alternatives. A plan is not implementation or
permission to merge.

> Example: Read context-map. Map the files and tests affected by [quest change], explain the dependencies, and stop for map review before implementation. Preserve unrelated work.

## Versions and contracts

Use [source-driven-development](../skills/source-driven-development/SKILL.md)
([adaptation notes](../skills/source-driven-development/SOURCE.md)) for unfamiliar
or version-sensitive APIs. Use [api-and-interface-design](../skills/api-and-interface-design/SKILL.md)
([adaptation notes](../skills/api-and-interface-design/SOURCE.md)) for state
ownership, module/event/lifetime and save contracts. Use
[constraint-driven-development](../skills/constraint-driven-development/SKILL.md)
([adaptation notes](../skills/constraint-driven-development/SOURCE.md)) when
project-owned correctness or performance gates need definition or protection.
These are adapted instructions, not installed guards or hooks.

**Context:** Unity project/version files and resolved package evidence,
target platform, current callers, save fixtures and approved budgets. Use
documentation matching the actual stack; do not substitute a remembered version.

**Evidence:** Requested/resolved versions, source citations, contract
acceptance cases and gate artifacts. Separate documented support, compilation
and runtime observations. Unknown thresholds stay proposals or measurements,
not invented delivery gates.

> Example: Read source-driven-development. For [Unity package integration], inspect requested and resolved versions and cite matching API documentation. Separate verified facts from missing compile/runtime evidence; do not install anything.

## Inventory and saves

Start with the RPG rules above for capacity, stacking, equipment and rewards.
Use [unity-scriptableobjects](../skills/unity-scriptableobjects/SKILL.md)
([caveats](../skills/unity-scriptableobjects/SOURCE.md)) for shared item/quest
definitions, and [save-systems](../skills/save-systems/SKILL.md)
([caveats](../skills/save-systems/SOURCE.md)) for durable player state, versioning
and recovery. Keep per-character mutable state separate from shared definitions.
Use an explicit operation/save contract when retries could grant a reward twice.

**Context:** Item IDs/assets, current inventory owner, serializer, old
save samples and a disposable save location; Unity Editor/tests if available.

**Evidence:** Round trip and migration outcomes, full-inventory rejection,
repeat-claim behavior, interrupted-write recovery and unchanged shared definitions.
For static channels/runtime sets, test scene changes and a second Play session
with the project's domain-reload settings.

> Example: Read the complete save-systems package. Design migration for [old save fixture] and preserve the original on failure. Specify round-trip, duplicate-reward and interrupted-write checks; report which can actually run here.

## Combat and enemies

Use RPG rules for damage/resource invariants. Select
[game-ai](../skills/game-ai/SKILL.md) ([caveats](../skills/game-ai/SOURCE.md)) for
enemy decisions and paths; [collision-layers](../skills/collision-layers/SKILL.md)
([caveats](../skills/collision-layers/SOURCE.md)) for allowed/blocked interaction
categories; or [game-feel](../skills/game-feel/SKILL.md)
([caveats](../skills/game-feel/SOURCE.md)) for hit feedback. Choose the layer that
is actually changing. A collision permission does not itself authorize damage.

**Context:** Combat rules, decision states, 2D/3D layer assignments,
movement/navigation integration and a reproducible encounter. Engine navigation
or physics implementations are not bundled by these skills.

**Evidence:** Allowed and rejected hits, one-time damage, state
interruptions, reachability/stuck behavior and feedback after pause/overlap.
Preserve serialized layer IDs. Verify hit-stop restores the intended time state.

> Example: Read collision-layers. For [2D combat scene], propose an interaction matrix using existing layer IDs, including blocked friendly hits. Distinguish collision candidates from damage rules and list engine tests still needed.

## Dialogue, localization and audio

Select [dialogue-systems](../skills/dialogue-systems/SKILL.md)
([caveats](../skills/dialogue-systems/SOURCE.md)) for branches and narrative
state; [game-localization](../skills/game-localization/SKILL.md)
([caveats](../skills/game-localization/SOURCE.md)) for stable text IDs, fallback
and live language switching; [audio-design](../skills/audio-design/SKILL.md)
([caveats](../skills/audio-design/SOURCE.md)) for mix, ducking and transitions.
Ink/Yarn, audio middleware and runtime integrations are not supplied.

**Context:** Dialogue graph, state mutations, locale tables/fonts,
existing runner/audio system and representative conversation. For Unity audio,
adapt the Godot-oriented sketches to the project's actual audio APIs.

**Evidence:** Reachable choices, explicit continue input, no repeated
reward/flag mutation, fallback glyphs, language switching without resetting game
state, and measured/listened-to audio transitions. Separate a dialogue graph
inspection from actual playback or sample-accurate synchronization claims.

> Example: Read game-localization. Design an English/Chinese switch for [quest dialogue], preserving stable quest and line IDs. Specify font fallback and state-preservation checks; do not claim a runtime switch was tested.

## UI and accessibility

Use [game-ui-ux](../skills/game-ui-ux/SKILL.md)
([caveats](../skills/game-ui-ux/SOURCE.md)) for HUDs, menus, safe areas, focus and
screen flow. Add [a11y-controls](../skills/a11y-controls/SKILL.md)
([caveats](../skills/a11y-controls/SOURCE.md)) for scoped input/readability/motion
preferences. Use [frontend-design](../skills/frontend-design/SKILL.md)
([caveats](../skills/frontend-design/SOURCE.md)) for a browser site or launcher web
page's visual direction. A web-design review does not verify native game UI.

**Context:** Chosen UI system, viewport/safe-area scale, screen stack,
state events, devices, fonts and relevant preferences; browser tools only for a
web surface. Concrete engine widgets/remappers are not bundled.

**Evidence:** Screenshots at relevant sizes, controller/keyboard focus
traversal, back/pause restoration, event updates and non-color cues. Include
representative user checks when evaluating accessibility; this is not certification.

> Example: Read game-ui-ux. Review [inventory menu] for safe-area layout and controller focus, including return from settings. Separate observed screenshots/input traces from proposed fixes and unavailable runtime checks.

## Input

Use [unity-input-system](../skills/unity-input-system/SKILL.md)
([caveats](../skills/unity-input-system/SOURCE.md)) for action maps, devices and
rebinding. Start from the project's existing package and Input Actions; this
vault does not install `com.unity.inputsystem`.

**Context:** Resolved Input System version, action assets, map owners,
save preferences and available keyboard/controller or Input Debugger.

**Evidence:** Gameplay/menu map isolation, press/hold semantics, cancel
and overlapping-rebind behavior, disable/destroy cleanup and persistence.
The upstream rebinding sketch needs lifecycle/cancellation handling.

> Example: Read unity-input-system. Audit [rebinding flow] for cancel, overlapping operations and disable/destroy cleanup using the installed package. Preserve current bindings and report tests actually performed.

## Animation and cutscenes

Use [unity-animation](../skills/unity-animation/SKILL.md)
([caveats](../skills/unity-animation/SOURCE.md)) for Animator transitions, layers
and IK. Use [cutscene-handoff](../skills/cutscene-handoff/SKILL.md)
([caveats](../skills/cutscene-handoff/SOURCE.md)) when input, camera, UI or game
state changes owners during a cinematic. Clips, rigs and Timeline integrations
are not bundled; elapsed animation length is not proof of combat completion.

**Context:** Controller parameters/clips, rig/Avatar, root-motion
policy, ownership before/after the cutscene and skip/interruption policy.

**Evidence:** Actual transition/interruption traces, required IK setup,
skip/focus-loss/scene-unload restoration and idempotent callbacks. Rewards and
flags must not be duplicated by skip or repeated completion callbacks.

> Example: Read cutscene-handoff. For [quest cinematic], define entry, skip and scene-unload restoration of input/camera/UI, with one-time reward handling. List the runtime cases; do not implement a new cinematic framework.

## Levels and generation

Use [level-design](../skills/level-design/SKILL.md)
([caveats](../skills/level-design/SOURCE.md)) for authored traversal, encounters
and gates; [procedural-gen](../skills/procedural-gen/SKILL.md)
([caveats](../skills/procedural-gen/SOURCE.md)) for seeded generation and validation.
A connected graph is not proof that a player can traverse it or obtain every key.

**Context:** Movement metrics, collision/camera rules, gate/key
locations, seed, bounds and generation retry limits. No level assets or complete
generator are supplied.

**Evidence:** Reproducible seeds, reachable objectives under actual
traversal rules, key-before-gate ordering, bounded failures and playtest pacing.
Retain failing seeds for regression rather than rerolling until one succeeds.

> Example: Read procedural-gen. Specify validation for [seeded dungeon], including key-before-lock reachability and bounded retries. Keep failing seeds as fixtures and distinguish graph checks from engine traversal tests.

## Tilemaps, pixel art and assets

Use [unity-tilemap](../skills/unity-tilemap/SKILL.md)
([caveats](../skills/unity-tilemap/SOURCE.md)) for palettes/RuleTiles;
[unity-2d-pixel-perfect](../skills/unity-2d-pixel-perfect/SKILL.md)
([caveats](../skills/unity-2d-pixel-perfect/SOURCE.md)) for pixel sampling,
camera/import/pipeline issues; [create-game-assets](../skills/create-game-assets/SKILL.md)
([caveats](../skills/create-game-assets/SOURCE.md)) for art direction, provenance
and optional raster inspection. They do not supply art, a generator or an engine.

**Context:** Unity version, actual render pipeline, camera setup,
sprite settings, grid/tiles and asset ownership. RuleTile templates need the
project's Tilemap Extras package. Optional raster utilities need their documented
Python/Pillow environment; inspect before running and choose disposable outputs.

**Evidence:** Asset dimensions/licenses, import diff, tile adjacency and
colliders, still captures plus motion at target resolution. Do not treat a still
PNG as proof that shimmering is fixed. Independently check color limits because
the bundled asset checker has a documented off-by-one caveat.

> Example: Read unity-2d-pixel-perfect. Investigate [moving-sprite shimmer] using the project's actual pipeline and camera. Propose a minimal change and a motion capture check; preserve asset import settings unless the change requires them.

## Debugging or profiling

Use [unity-debug](../skills/unity-debug/SKILL.md)
([caveats](../skills/unity-debug/SOURCE.md)) for functional failures and trustworthy
runtime evidence. Use [unity-profiling](../skills/unity-profiling/SKILL.md)
([caveats](../skills/unity-profiling/SOURCE.md)) when behavior works but you need
comparable frame/work measurements. If "it feels wrong" could mean either, ask
for a reproducible symptom before choosing. A slow failure can need both, in
stages, after the run itself is trusted.

**Context:** Fresh logs/results tied to the current run, reproduction,
project version and available Editor/test harness. Performance work also needs
instrument/build/device, seed, workload and comparable windows. Optional live
Editor commands need separate tooling; the vault does not install it.

**Evidence:** For debugging, actual discovered/executed tests and fresh
artifacts; exit zero or stale XML is insufficient. For profiling, before/after
windows under comparable conditions, distributions and missing-counter notes.
Editor diagnostics do not establish device-player performance.

> Example: Read unity-debug. Diagnose [reproduction] and verify the harness produced fresh logs/results for this run. Report observed evidence, missing tools and unrun checks; do not infer success from exit zero.

## Tests and code review

Use [test-driven-development](../skills/test-driven-development/SKILL.md)
([caveats](../skills/test-driven-development/SOURCE.md)) for a behavior change
with the project's test runner; [verification-before-completion](../skills/verification-before-completion/SKILL.md)
([caveats](../skills/verification-before-completion/SOURCE.md)) before a passing
or completion claim. Use [requesting-code-review](../skills/requesting-code-review/SKILL.md)
([caveats](../skills/requesting-code-review/SOURCE.md)) to prepare an independent
review, and [receiving-code-review](../skills/receiving-code-review/SKILL.md)
([caveats](../skills/receiving-code-review/SOURCE.md)) to evaluate comments already
received. They are different review stages.

**Context:** Requirements, failure case, actual test commands, explicit
base/head revisions and intended staged/unstaged work. Independent review needs
a supported reviewer mechanism or a human; name that limitation if unavailable.
Do not assume `HEAD~1` covers the full change.

**Evidence:** Relevant failing/passing test output, current full-check
results, review coverage and technically verified responses to feedback.
Review readiness does not authorize merge or publication.

> Example: Read requesting-code-review. Prepare a review of [base SHA] through [head SHA] against [requirements], including test evidence and any uncommitted work outside that range. If no independent reviewer is available, provide the request and mark the review not run.

## Godot starter

Use [godot-fundamentals](../skills/godot-fundamentals/SKILL.md)
([caveats](../skills/godot-fundamentals/SOURCE.md)) for a Godot 4.x project,
nodes/scenes/resources, Input Map and editor workflow. Add the relevant
engine-neutral RPG, save or UI skill only for the feature being built; Unity
packages are not drop-in Godot implementations.

**Context:** Existing `project.godot`, installed engine version, scene
tree, resource ownership and relevant input actions. No engine or add-on is
installed by this repository.

**Evidence:** Actual parser/import results, then scene launch, input and
node lifecycle observations. Headless import alone does not prove gameplay.

> Example: Read godot-fundamentals. Inspect [existing Godot project] and propose the smallest scene/input setup for [feature]. Use the installed version, preserve resources, and separate import checks from unrun gameplay checks.

## Documentation

Use [documentation-writer](../skills/documentation-writer/SKILL.md)
([caveats](../skills/documentation-writer/SOURCE.md)) when a feature needs a
tutorial, how-to, reference or explanation. Follow its clarification and outline
review steps; document what the current project actually does.

**Context:** Audience, current implementation, supported versions,
existing docs and verified commands. No PDF/Word conversion tools are bundled.

**Evidence:** Source-backed steps, checked links and examples actually
run or clearly marked unrun. Documentation is not runtime certification.

> Example: Read documentation-writer. Draft a how-to for [implemented feature] for [audience], starting with an outline for review. Use verified commands and label examples that have not been run.

## Parallel work

Use [dispatching-parallel-agents](../skills/dispatching-parallel-agents/SKILL.md)
([caveats](../skills/dispatching-parallel-agents/SOURCE.md)) only for independent
tasks when the host supports authorized subagents. Avoid concurrent edits to the
same assets or shared state. If dispatch is unavailable, work sequentially or
provide a handoff plan; do not claim agents were launched.

**Context:** Clear boundaries, file ownership, shared constraints,
available dispatch mechanism and integration owner.

**Evidence:** Each task's concrete deliverable and checks, then integrated
diff/tests. Separate plans from completed delegated work.

> Example: Read dispatching-parallel-agents. Assess whether [tasks] are independent and identify shared-file risks. Propose ownership and integration checks; dispatch only if authorized and supported here.

## When a skill or test tool is missing

A named upstream companion is not automatically in this vault. For example,
there is no bundled Unity CLI installer, general Unity C# implementation skill,
NavMesh runtime, Timeline integration or engine-specific UI adapter. Use the
project's existing owners and version-matched documentation for the missing
implementation boundary, or ask for the specific missing capability. Do not
pretend a related conceptual skill fills every gap or install tools automatically.

Without an engine, device, browser, test runner or independent reviewer, finish
the useful static work: map code, inspect fixtures, draft contracts and propose
the exact verification protocol. Report the missing tool and mark the relevant
checks **not run**. Keep documented support, compilation, automated tests,
manual observation and target-device measurements as separate claims.

For example: "Save migration fixture inspection completed; Unity PlayMode tests
not run because no Editor is available. Next evidence needed: execute the named
round-trip and interrupted-write tests on the target environment." This states
an actual boundary rather than claiming the feature works.

The [vault validator](validation.md) checks static packaging/provenance. The
[bilingual evaluation protocol](evaluations.md) supplies authored routing and
synthetic evidence cases, with honest run records. Neither establishes real
agent routing quality or engine behavior. The example prompts in this guide are
original documentation examples, statically reviewed; no model or engine runs
were performed to validate them.
