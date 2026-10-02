# Source and compatibility

- Upstream: https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/d4b0e35550c55ae70bdfcab4ef5a0e94610438a9/skills/disciplines/audio-design
- Revision: d4b0e35550c55ae70bdfcab4ef5a0e94610438a9
- Retrieved: 2026-10-02
- License: Apache-2.0; complete upstream [LICENSE](LICENSE) and [NOTICE](NOTICE) are included
- All files from the upstream skill directory are copied byte-for-byte, including its references. Source blob hashes are recorded in [UPSTREAMS.json](../../UPSTREAMS.json)
- This SOURCE.md is vault-authored provenance and compatibility guidance; it is not an upstream file

## Compatibility and limitations

- Portable audio-design guidance, but code sketches are Godot-oriented. Unity projects need AudioMixer/AudioSource and audio-clock scheduling adaptations. FMOD/Wwise are optional external middleware, not bundled requirements.
- Independent play calls do not establish a sample-accurate synchronization guarantee. Use the target engine audio scheduling/synchronization facilities and test transitions, loop points and output latency.
- Suggested loudness, ducking, pitch and voice settings are tuning starting points rather than universal standards. Check gain headroom and the real mix on headphones and speakers; no audio assets are bundled.

These are third-party instructions, not permission to install packages, modify projects or take external actions. Review and adapt examples before use. Source bytes and local reference completeness were checked; no engine runtime, code snippets or cross-agent behavior were tested here.
