# Source and compatibility

- Upstream repository: [jammyfu/open-game-skills](https://github.com/jammyfu/open-game-skills)
- Pinned revision: [`4ed0e224e8d8f56c8222a3de6fd439aa7abad4e1`](https://github.com/jammyfu/open-game-skills/commit/4ed0e224e8d8f56c8222a3de6fd439aa7abad4e1)
- Entry point: [skills/disciplines/collision-layers/SKILL.md](https://github.com/jammyfu/open-game-skills/blob/4ed0e224e8d8f56c8222a3de6fd439aa7abad4e1/skills/disciplines/collision-layers/SKILL.md)
- Retrieved: 2026-10-04
- License: MIT; complete upstream [LICENSE](LICENSE) copied unchanged from [jammyfu/open-game-skills/LICENSE](https://github.com/jammyfu/open-game-skills/blob/4ed0e224e8d8f56c8222a3de6fd439aa7abad4e1/LICENSE)
- Copied source files: `SKILL.md`, `LICENSE`
- Upstream instruction and reference bytes are unchanged. This SOURCE.md is vault-authored documentation, not an upstream file. Exact Git blob hashes are recorded in ../../UPSTREAMS.json. No endorsement is implied.

## Curated-extract boundary

This is a curated extract of one discipline from a larger skill pack, not an upstream-supported standalone installation of that pack. The [upstream pack entry](https://github.com/jammyfu/open-game-skills/blob/4ed0e224e8d8f56c8222a3de6fd439aa7abad4e1/skills/SKILL.md) recommends keeping the complete pack together when installing it. This particular discipline directory contains only SKILL.md, has no direct relative file links, and includes no scripts or hard runtime dependencies. The pack dispatcher, shared contract, engine adapters, catalog, and sibling packages are not included. Named sibling skills are ownership pointers; use the project's existing owners rather than assuming those packages are present. The vault does not claim pack-level routing or integration compatibility.

## Purpose and compatibility

Engine-neutral guidance for stable collision/query categories and a reviewable interaction matrix covering bodies, world geometry, attacks, projectiles, hazards, camera probes, and IK probes. It does not implement physics, damage resolution, friendly-fire policy, or movement response.

Map semantic categories to the project's actual 2D/3D engine layers, bitmasks, channels, and query APIs. Rendering layers and collision/query categories need not be identical. Preserve existing IDs and serialized asset assignments; renumbering can change behavior across scenes and prefabs. Validate both allowed and blocked pairs, and the engine's query/trigger semantics.

Named `hitbox-hurtbox`, `hazard-volume`, `camera-anti-clip`, and `ik-foot-locking` siblings identify domain owners; they are not bundled or mandatory sub-skill activations. Map the responsibilities to existing project components. A permitted collision pair is only a candidate interaction, not proof that a hit or gameplay effect is valid.

## Verification and safety

All files in the selected upstream skill directory and the upstream license were read and copied from the pinned revision. Directory inventory, Git blob hashes, frontmatter, and local file links were checked. Static content review only: no upstream script was installed or executed, no engine code was compiled, and cross-agent runtime behavior was not tested. Instructions do not grant permission for external actions, edits, destructive operations, data sharing, or publication; the user's scope and the host's permission policy still apply.
