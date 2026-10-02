# Source and compatibility

- Upstream: https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/d4b0e35550c55ae70bdfcab4ef5a0e94610438a9/skills/unity/unity-scriptableobjects
- Revision: d4b0e35550c55ae70bdfcab4ef5a0e94610438a9
- Retrieved: 2026-10-02
- License: Apache-2.0; complete upstream [LICENSE](LICENSE) and [NOTICE](NOTICE) are included
- All files from the upstream skill directory are copied byte-for-byte, including its references. Source blob hashes are recorded in [UPSTREAMS.json](../../UPSTREAMS.json)
- This SOURCE.md is vault-authored provenance and compatibility guidance; it is not an upstream file

## Compatibility and limitations

- Targets Unity 6.3 LTS (6000.3). The core ScriptableObject patterns use Unity APIs and C# without an extra runtime package. Examples require adaptation to the project and are not precompiled assets.
- Treat ScriptableObjects as shared definitions or deliberate channels, not per-character mutable state or save files. Check runtime set/listener cleanup and behavior across scene changes.
- Test a second Play session with domain reload disabled. Do not assume OnEnable alone reliably resets state for every Enter Play Mode configuration; choose and verify an explicit reset strategy.

These are third-party instructions, not permission to install packages, modify projects or take external actions. Review and adapt examples before use. Source bytes and local reference completeness were checked; no engine runtime, code snippets or cross-agent behavior were tested here.
