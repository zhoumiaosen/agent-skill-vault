# Source and compatibility

- Upstream repository: [jammyfu/open-game-skills](https://github.com/jammyfu/open-game-skills)
- Pinned revision: [`4ed0e224e8d8f56c8222a3de6fd439aa7abad4e1`](https://github.com/jammyfu/open-game-skills/commit/4ed0e224e8d8f56c8222a3de6fd439aa7abad4e1)
- Entry point: [skills/disciplines/a11y-controls/SKILL.md](https://github.com/jammyfu/open-game-skills/blob/4ed0e224e8d8f56c8222a3de6fd439aa7abad4e1/skills/disciplines/a11y-controls/SKILL.md)
- Retrieved: 2026-10-04
- License: MIT; complete upstream [LICENSE](LICENSE) copied unchanged from [jammyfu/open-game-skills/LICENSE](https://github.com/jammyfu/open-game-skills/blob/4ed0e224e8d8f56c8222a3de6fd439aa7abad4e1/LICENSE)
- Copied source files: `SKILL.md`, `LICENSE`
- Upstream instruction and reference bytes are unchanged. This SOURCE.md is vault-authored documentation, not an upstream file. Exact Git blob hashes are recorded in ../../UPSTREAMS.json. No endorsement is implied.

## Curated-extract boundary

This is a curated extract of one discipline from a larger skill pack, not an upstream-supported standalone installation of that pack. The [upstream pack entry](https://github.com/jammyfu/open-game-skills/blob/4ed0e224e8d8f56c8222a3de6fd439aa7abad4e1/skills/SKILL.md) recommends keeping the complete pack together when installing it. This particular discipline directory contains only SKILL.md, has no direct relative file links, and includes no scripts or hard runtime dependencies. The pack dispatcher, shared contract, engine adapters, catalog, and sibling packages are not included. Named sibling skills are ownership pointers; use the project's existing owners rather than assuming those packages are present. The vault does not claim pack-level routing or integration compatibility.

## Purpose and compatibility

Engine-neutral accessibility preference and testing guidance for action remapping, hold/toggle alternatives, text scaling, non-color cues, reduced flashes/motion, and explicitly scoped gameplay assists. It complements the vault's input and UI skills. No input remapper, accessibility middleware, assistive-device driver, or engine integration is bundled.

Named `input-design`, `hud-feedback`, and UI/gameplay owners describe architectural responsibilities; those sibling packages are not bundled or mandatory sub-skill activations. `game-localization` is included separately in this vault. Adapt the capability matrix to the actual engine, devices, settings, and persistence model. This is not a comprehensive accessibility audit, legal opinion, or platform certification checklist; verify applicable current platform guidance and test with representative users.

## Verification and safety

All files in the selected upstream skill directory and the upstream license were read and copied from the pinned revision. Directory inventory, Git blob hashes, frontmatter, and local file links were checked. Static content review only: no upstream script was installed or executed, no engine code was compiled, and cross-agent runtime behavior was not tested. Instructions do not grant permission for external actions, edits, destructive operations, data sharing, or publication; the user's scope and the host's permission policy still apply.
