# Validation report

Date: 2026-10-04 (UTC)

## Scope

This report concerns the three instruction packages in this bundle. It does not certify a Unity project, a gameplay implementation or an automated quality gate.

## Completed checks

| Check | Result | Scope |
|---|---|---|
| Required YAML/frontmatter | Pass | Three `SKILL.md` files parse; names match folders; descriptions identify triggers; MIT license field present |
| Discovery size | Pass | Each frontmatter is below 1,024 characters and each description below 500 characters |
| Local references | Pass | All Markdown links to local files resolve within the bundle; each package is independently copyable |
| License retention | Pass | Four license copies match the fetched upstream MIT license byte-for-byte; Git blob SHA `d67778ada6b9cda6227e9130da182c13e73c8b2e` |
| Provenance | Pass | Each `SOURCE.md` identifies the exact upstream revision, source files, copyright, adaptation date and changes |
| Package boundary | Pass | Documentation/license files only; no executable guard, hook, installer, plugin configuration or external skill dependency |
| Independent document review | Pass as a draft | Reviewed scope, triggers, failure handling, budgets, lifetimes, persistence and evidence language; minor discovery/manual-verdict wording improvements incorporated |
| Fictional application reviews | No concrete behavioral defect in the three main cases | Source mismatch/no editor; unmeasured budgets/no install authority; offline reward duplication/scene lifetime/old saves |
| Legacy-save edge case | Clarification incorporated | Missing historical receipts cannot mean unclaimed; unresolved legacy history requires a migration-policy decision rather than an ordinary pending retry |
| Archive integrity | Pass | ZIP entries read back and compared with the final local package files; no absolute or parent-traversal paths |

The structural validator was run against each final skill. Separate checks inspected naming, local links, forbidden package contents, license blob identity and ZIP integrity.

## Evidence limits

- The original-source baseline also produced cautious, useful answers. The scenario reviews do not establish a measured behavioral improvement over upstream, a statistical reliability score or universal robustness under pressure
- Scenario reviews used fictional project facts. They were document-application exercises, not execution in Unity, Godot, Unreal or a backend
- No game code, editor/player build, device benchmark, save implementation or live API was run. Runtime approaches and test suggestions in these skills remain unimplemented and untested in a real project
- Official Unity references were read for package resolution, serialization, profiling, assemblies, domain reload and Addressables ownership. Their linked versions are examples; each real use must select and verify the project's actual version
- The pinned upstream source files and floor-guard reference were read. No upstream script, hook or installer was executed
- No skill was installed and no GitHub repository was changed or pushed

## Recommended first real-project trial

Use one small, existing Unity feature with known editor/package versions and available tests. Keep performance thresholds report-only until the project chooses its workload, hardware and budgets. Exercise one unload/rebind failure path and one old-save fixture, recording actual artifacts. Review the results before adopting these drafts as team-wide defaults.
