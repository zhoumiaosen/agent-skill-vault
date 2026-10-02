# Source and compatibility

- Upstream: https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/d4b0e35550c55ae70bdfcab4ef5a0e94610438a9/skills/disciplines/dialogue-systems
- Revision: d4b0e35550c55ae70bdfcab4ef5a0e94610438a9
- Retrieved: 2026-10-02
- License: Apache-2.0; complete upstream [LICENSE](LICENSE) and [NOTICE](NOTICE) are included
- All files from the upstream skill directory are copied byte-for-byte, including its references. Source blob hashes are recorded in [UPSTREAMS.json](../../UPSTREAMS.json)
- This SOURCE.md is vault-authored provenance and compatibility guidance; it is not an upstream file

## Compatibility and limitations

- Engine-neutral guidance with GDScript/Python sketches. Ink or Yarn Spinner are optional external authoring/runtime integrations, not bundled dependencies; verify the integration and version used by the project.
- The short SKILL.md runner sketch immediately follows linear next links; the fuller references/runner.md waits for continue input. Use explicit line/input progression rather than copying the short sketch as a complete runner.
- Validate target nodes, reachable branches, choice conditions and repeated state mutations. Localize line IDs and persist narrative state separately from the UI. The custom evaluator is illustrative and is not a security boundary for untrusted content.

These are third-party instructions, not permission to install packages, modify projects or take external actions. Review and adapt examples before use. Source bytes and local reference completeness were checked; no engine runtime, code snippets or cross-agent behavior were tested here.
