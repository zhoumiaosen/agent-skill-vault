# Vault validation

This validator and its regression tests were written from scratch for this
repository. They do not reuse upstream validation code or execute skill content.

Use Python 3.10 or newer. From the repository root:

```sh
python -m venv .venv
# POSIX: .venv/bin/python; Windows: .venv/Scripts/python
.venv/bin/python -m pip install -r requirements-validation.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python tools/validate_vault.py
```

`--root PATH` validates another checkout. Failure prints file/package diagnostics
and exits with status 1. Validation never writes repository files. PyYAML is the
only dependency, pinned for reproducibility; its safe loader rejects executable
YAML tags, and the validator rejects duplicate mapping keys.

Checks cover YAML frontmatter (including folded/quoted descriptions and nested
upstream metadata), matching names, nonblank descriptions of at most 1024
characters, instruction bodies, per-package licenses and source attribution,
manifest coverage, supporting-file inventory, local Markdown links and reference
definitions, and README catalog membership and stated collection counts.
Operational links must remain within the skill package so it can be copied in
isolation. A package's root SOURCE.md may link to repository provenance files.
Fenced examples and inline code are excluded from link checks. External links,
anchors, optional named companion skills, runtime project paths and illustrative
commands are not treated as bundled dependencies. This is a focused Markdown
link scanner, not a complete CommonMark renderer or semantic dependency analysis.

## Provenance rules

- Unchanged entries use `modified: false`. `blob_sha` is a legacy alias for the
  delivered SKILL.md Git blob hash; `files` records unchanged packaged source
  bytes. Every supporting file must be inventoried. Legacy vault-authored
  SOURCE.md and root license/NOTICE copies may be absent from that inventory;
  their presence and attribution are still checked. Recorded notices are hashed.
- Adaptations use `modified: true`, `content_kind: adapted-and-rewritten`, and an
  adaptation summary. `files` and `sha256` must cover every delivered file,
  including SOURCE.md and LICENSE. `upstream_files` records original adaptation
  inputs by their upstream paths, with pinned Git blob hashes and roles. Those
  inputs are not compared to rewritten local files. A `copied unchanged` record
  must agree with the corresponding delivered hash. Do not use `blob_sha` for
  adaptations or overwrite original source hashes with adaptation hashes.
- Hashes use exact bytes. Git blob SHA-1 includes Git's `blob <length>\0` header;
  SHA-256 hashes raw file bytes. No line-ending normalization is performed.
  On Windows, clone with `git -c core.autocrlf=false clone URL` to preserve bytes.
  Avoid changing upstream content to satisfy formatting preferences.
- Add/remove a package by updating UPSTREAMS.json, README catalog and collection
  count statements together. The validator derives counts; it does not lock the
  collection permanently to 37 skills. Full upstream inventories and correctness
  of claimed source revisions still need human review when importing content.

GitHub Actions runs tests and validation on push and pull requests with read-only
contents permission and checkout credential persistence disabled. It installs
only the pinned parser and executes repository-owned validation/tests. It needs
no secrets, model calls, external service APIs, upstream skill hooks, or runtime
installations. Downloading the Python runtime, actions and parser needs network
access; validation itself is offline.

Passing means tooling/static packaging checks passed. It does not establish
license interpretation, source authenticity beyond recorded hashes, engine API
correctness, security of bundled code, or runtime behavior of any skill.
