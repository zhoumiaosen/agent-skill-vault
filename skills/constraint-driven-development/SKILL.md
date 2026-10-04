---
name: constraint-driven-development
description: Use when a game project or backend service needs explicit quality gates, performance or memory budgets, compatibility guarantees, or protection against weakened tests and checks; also applies when reviewing changes to existing project constraints.
license: MIT
---

# Constraint-Driven Development

Define what this project must preserve and how to measure it. A written target is a proposal until its owner accepts it and its check is demonstrably operational.

## Inputs and scope

Read existing constraints, project/CI instructions, engine and package pins, test assemblies, build targets and relevant recent results. Preserve the current approved bar. An existing result needs a revision, environment and artifact before it can support today's claim.

For a Unity RPG, inspect relevant `.asmdef` boundaries, EditMode/PlayMode suites, save fixtures, content validators and existing build/profiling workflows. Use the equivalent test, profiler and packaging tools for Godot or Unreal; keep backend service gates separate from client budgets.

Do not turn a narrow feature request into a tooling migration. Drafting a constraint plan does not authorize installing packages, changing CI/hooks or making repository policy edits. Use existing approved tooling; request only the missing setup required for the chosen gate.

## 1. Separate existing requirements from unknowns

Summarize what is already enforced, what is merely documented and what has no measurement. Ask only for unresolved choices that affect the work:

- Target platform, representative minimum hardware, resolution and quality preset
- Relevant gameplay workload and desired player experience
- Which checks block delivery, which report measurements, and who owns exceptions
- Acceptable feedback time locally and in CI

Never invent a universal FPS, coverage percentage, memory cap or allowable regression. If the user has no number, propose a baseline experiment and keep that metric **measured-only** until its threshold and gate mode are agreed. A baseline is evidence, not automatic approval for a ratchet. In unattended work, preserve existing gates, flag missing decisions and continue only independent checks.

## 2. Make each constraint reproducible

Use the project's existing location, or propose `CONSTRAINTS.md`. Each active rule needs:

`ID; owner; rationale; scope/platform; metric and unit; comparator/limit; scenario/fixture; environment and build configuration; command or manual protocol; verdict rule/parser; result artifact; run stage; gate mode; baseline revision; approved exception policy.`

Use stable rule IDs so a renamed label cannot conceal a changed threshold. Keep a single canonical rule/configuration source and link wrappers to it. Any drift between prose, scripts and CI is a finding to resolve, not permission to choose whichever passes.

Select only dimensions relevant to the change:

| Dimension | Meaningful game evidence |
|---|---|
| Correctness | Discovered/executed EditMode and PlayMode tests; battle, inventory, quest and progression invariants |
| Frame cost | CPU and GPU frame-time distributions for a named combat/traversal scene, actor count and duration |
| Allocation/memory | Managed allocation rate, peak memory and retained growth over a defined repeated load/unload sequence |
| Persistence | Old-save migration fixtures, round trips, interrupted-write recovery and duplicate-reward prevention |
| Loading/content | Defined cold/warm loading time, build size, address/asset validation and broken-reference checks |
| Architecture | Runtime/editor separation and allowed assembly/module dependencies |
| Accessibility | Relevant input remapping, controller focus, text/readability and information-without-color protocols |
| Backend, if present | Measured service latency/load, schema compatibility, authorization and retry correctness |

For performance, fix the build type, device, OS, scene/content revision, resolution, quality, warm-up, measurement window, sample count and aggregation method. Define noise/tolerance from repeated measurements and the accepted requirement. Report frame-time percentiles/tails when relevant; an average can hide hitches. Record profiler overhead and thermal/power conditions that affect comparability. Editor measurements are diagnostic; [target-player profiling](https://docs.unity3d.com/2022.3/Documentation/Manual/profiler-profiling-applications.html) is needed for target-device conclusions.

Coverage must name its scope and exclusions; it does not establish assertion quality. Native game accessibility requires appropriate game checks, not a browser audit pretending to cover the player.

## 3. Protect the approved bar

Review the actual change against a verified base: committed changes, staged and unstaged work, untracked files, renames and deletions. An unavailable comparison is **blocked**, not clean.

Inspect both code and check configuration for:

- Deleted/ignored tests, removed assertions, altered fixtures, discovery/category filters or conditional compilation that stops tests running
- New warning/analyzer/coverage suppressions, empty error handling or unfinished production paths
- Relaxed budgets, changed sampling/aggregation, reduced scenario difficulty or moved/disabled CI gates
- New or expanded exceptions and allowlists

C#/NUnit examples include `[Ignore]`, `Assert.Ignore`, conditional test exclusions and `#pragma warning disable`; they are review signals, not automatic proof of a violation. Legitimate refactors can move assertions or replace tests. Compare semantics and replacement coverage, record the reason and use the project's approval policy. Do not silently weaken a check to make a feature pass.

Keep exceptions explicit: affected rule and paths, rationale, risk, owner, reviewer/approval, expiry or removal condition and remediation issue. Preserve existing exceptions; do not create a new exemption on someone's behalf.

### Limits of automated diff guards

No guard implementation ships with this skill. The upstream Node regex example is not a C#/Unity enforcement tool. Adding regexes does not validate test discovery, assertion semantics, multiline syntax, quoting of unusual filenames, binary/serialized assets, merge-base selection or configuration changes.

If a guard is separately requested, define its supported inputs and test fixtures for staged, unstaged, untracked, renamed and deleted files, plus valid refactors and actual violations. Prefer structural/configuration-aware checks where available; retain human review for uncovered cases. A useful result contract distinguishes **clean within checked scope**, **finding**, and **could not evaluate**. A missing base, parser failure or missing tool must never become a passing verdict. Redact potential secrets from output and artifacts.

## 4. Run, diagnose and hand back

Place quick checks near edits and slower builds/device runs at meaningful milestones; choose timings from measured project cost. Narrow checks speed iteration but do not replace required final/CI suites.

For each check, retain revision, invocation/protocol, environment, discovered/executed/skipped counts where applicable, artifact, measured value and verdict. Test a new gate with a controlled failing fixture before trusting its green result; restore the fixture afterward. Diagnose failures against an equivalent baseline before attributing them to the change. Do not repeatedly rerun flaky checks until one green sample appears.

If a check is unavailable, report **blocked** with the missing prerequisite; if it was not attempted, report **not run**. Continue independent checks. Never call an EditMode-only run a complete player or performance pass.

## Deliverable

Provide the constraint proposal or approved changes, provenance for every threshold, per-rule status (**proposed, measured-only, pass, fail, blocked, not run**), evidence and unresolved decisions. Stop dependent work when it needs a new threshold, exception or setup authorization; preserve the agreed bar.

Attribution and adaptation history: [SOURCE.md](SOURCE.md). License: [LICENSE](LICENSE).
