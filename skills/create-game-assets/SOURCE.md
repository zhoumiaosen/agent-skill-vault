# Source and compatibility

- Upstream: https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/d4b0e35550c55ae70bdfcab4ef5a0e94610438a9/skills/disciplines/create-game-assets
- Revision: d4b0e35550c55ae70bdfcab4ef5a0e94610438a9
- License: Apache-2.0; see LICENSE and NOTICE
- Retrieved: 2026-10-02
- Upstream source copied unchanged

Complete 11-file Agent Skills package, including optional OpenAI UI metadata, four references, two templates, and two Python scripts. Optional raster utilities require Python 3.10+ and Pillow>=10,<13 (range is not locked/hash-pinned). No generator, engine, DCC, or external skill is installed. Static audit found no network, credential, subprocess, delete, eval, or dynamic-execution API in utilities. asset_report.py reads selected local images and prints report; build_preview_sheet.py creates output parents and overwrites explicit --out. Known static caveat: asset_report.py --max-colors permits exactly limit+1 colors because only a string color_count triggers failure. No downloaded code executed.

Review all commands before use; preserve project data. Publishing these files does not install or run them. Examples need adaptation to your engine version and project. Static inspection only; no runtime validation.
