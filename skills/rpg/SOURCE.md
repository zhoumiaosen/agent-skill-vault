# Source and compatibility

- Upstream: https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/d4b0e35550c55ae70bdfcab4ef5a0e94610438a9/skills/genres/rpg
- Revision: d4b0e35550c55ae70bdfcab4ef5a0e94610438a9
- Retrieved: 2026-10-02
- License: Apache-2.0; complete upstream [LICENSE](LICENSE) and [NOTICE](NOTICE) are included
- All files from the upstream skill directory are copied byte-for-byte, including its references. Source blob hashes are recorded in [UPSTREAMS.json](../../UPSTREAMS.json)
- This SOURCE.md is vault-authored provenance and compatibility guidance; it is not an upstream file

## Compatibility and limitations

- Engine-neutral guidance and Python-like pseudocode, not a runnable inventory, quest or combat package. No engine, installer or runtime dependency is bundled.
- The skill composes with dialogue-systems, game-ai and unity-scriptableobjects added here, and with the existing save-systems and game-ui-ux skills. Other named companion skills are optional pointers and are not implicitly installed.
- Tune the illustrated damage and XP formulas through playtests. Implement and test inventory capacity/stack rules, reversible modifiers and one-time quest rewards for the actual game.

These are third-party instructions, not permission to install packages, modify projects or take external actions. Review and adapt examples before use. Source bytes and local reference completeness were checked; no engine runtime, code snippets or cross-agent behavior were tested here.
