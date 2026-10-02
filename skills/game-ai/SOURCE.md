# Source and compatibility

- Upstream: https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/d4b0e35550c55ae70bdfcab4ef5a0e94610438a9/skills/disciplines/game-ai
- Revision: d4b0e35550c55ae70bdfcab4ef5a0e94610438a9
- Retrieved: 2026-10-02
- License: Apache-2.0; complete upstream [LICENSE](LICENSE) and [NOTICE](NOTICE) are included
- All files from the upstream skill directory are copied byte-for-byte, including its references. Source blob hashes are recorded in [UPSTREAMS.json](../../UPSTREAMS.json)
- This SOURCE.md is vault-authored provenance and compatibility guidance; it is not an upstream file

## Compatibility and limitations

- Engine-neutral algorithms with GDScript/Python examples. Unity needs a C# adaptation and an appropriate movement/navigation integration; no navigation package or runnable AI framework is bundled.
- For 3D Unity navigation, the optional unity-navmesh companion and AI Navigation package are separate. The grid A* material can guide tile-based RPG pathfinding without adding that package.
- Examples are instructional rather than a complete reactive behavior-tree runtime. Define and test Running-state retention, resets, interruption/abort policy and action side effects; adapt heuristic/node representations consistently for the actual graph.

These are third-party instructions, not permission to install packages, modify projects or take external actions. Review and adapt examples before use. Source bytes and local reference completeness were checked; no engine runtime, code snippets or cross-agent behavior were tested here.
