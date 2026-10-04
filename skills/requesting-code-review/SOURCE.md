# Source and compatibility

- Upstream repository: [obra/superpowers](https://github.com/obra/superpowers)
- Pinned revision: [`8ca22dba9a94f28898bbce59f2537ff4d87c747d`](https://github.com/obra/superpowers/commit/8ca22dba9a94f28898bbce59f2537ff4d87c747d)
- Entry point: [skills/requesting-code-review/SKILL.md](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/requesting-code-review/SKILL.md)
- Retrieved: 2026-10-04
- License: MIT; complete upstream [LICENSE](LICENSE) copied unchanged from [obra/superpowers/LICENSE](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/LICENSE)
- Copied source files: `SKILL.md`, `code-reviewer.md`, `LICENSE`
- Upstream instruction and reference bytes are unchanged. This SOURCE.md is vault-authored documentation, not an upstream file. Exact Git blob hashes are recorded in ../../UPSTREAMS.json. No endorsement is implied.

## Purpose and compatibility

Structures an independent code review against requirements, a Git revision range, and quality/test criteria. The complete upstream `code-reviewer.md` template is included. This complements `receiving-code-review`, which concerns evaluating feedback after a review arrives.

- Requires repository read access, Git, and a host with subagent support. Map `general-purpose` dispatch and prompt placeholders to the available harness. If the host cannot dispatch an independent reviewer, disclose that limitation rather than claim an independent review occurred.
- Set the actual base and head revisions explicitly. `HEAD~1` is only an example; it can omit earlier feature commits and all uncommitted or staged work. Review intended working-tree changes separately or use an approved committed snapshot. Do not infer the review boundary from a commit-message grep alone.
- Review instructions are read-only for the active checkout. The template's optional temporary worktree command changes Git metadata and creates a directory; use it only when authorized and supported by the host. It must not move the active checkout's HEAD or discard local work.
- Calibrate requirements and severity to the actual project. A reviewer finding or merge-readiness verdict is not authorization to edit, push, publish, or merge. Report actual checks and unrun tests; static review does not replace Unity/Godot/Unreal or platform validation.
- No external review service, GitHub action, runtime integration, test suite, or installer is bundled.

## Verification and safety

All files in the selected upstream skill directory and the upstream license were read and copied from the pinned revision. Directory inventory, Git blob hashes, frontmatter, and local file links were checked. Static content review only: no upstream script was installed or executed, no engine code was compiled, and cross-agent runtime behavior was not tested. Instructions do not grant permission for external actions, edits, destructive operations, data sharing, or publication; the user's scope and the host's permission policy still apply.
