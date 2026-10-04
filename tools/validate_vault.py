"""Offline, read-only validation of the vault's metadata and packaged bytes."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

import yaml


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently hiding earlier values."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        if not isinstance(key, str) or key in result:
            raise ValueError("mapping keys must be unique strings")
        result[key] = loader.construct_object(value_node, deep=True)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def unique_json(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def blob_hash(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def package_path(package, relative):
    """Manifest paths must be portable, contained paths, never symlinks."""
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise ValueError("expected a nonempty POSIX relative path")
    path = PurePosixPath(relative)
    if path.is_absolute() or ".." in path.parts or ":" in relative or str(path) != relative:
        raise ValueError(f"unsafe or noncanonical path: {relative}")
    target = package / relative
    if any(p.is_symlink() for p in [target, *target.parents]):
        raise ValueError(f"symlink path: {relative}")
    return target


def prose(text):
    """Remove fenced/inline examples before looking for actual Markdown links."""
    lines, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return re.sub(r"(`+).*?\1", "", "\n".join(lines))


def link_targets(text):
    # Inline links/images and reference definitions; titles are optional.
    text = prose(text)
    pattern = r"!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)"
    targets = [m[1].strip("<>") for m in re.finditer(pattern, text)]
    targets += [m[1].strip("<>") for m in re.finditer(
        r"^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)", text, re.MULTILINE)]
    return targets


def stated_count(token):
    """Read the numeric or English counts used in collection prose (0..99)."""
    if token.isdigit():
        return int(token)
    units = dict(zip("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split(), range(20)))
    tens = dict(zip("twenty thirty forty fifty sixty seventy eighty ninety".split(), range(20, 100, 10)))
    if token in units:
        return units[token]
    parts = token.split("-")
    if parts[0] in tens and (len(parts) == 1 or len(parts) == 2 and parts[1] in units and 0 < units[parts[1]] < 10):
        return tens[parts[0]] + (units[parts[1]] if len(parts) == 2 else 0)
    raise ValueError(f"unsupported collection count '{token}'; use digits")


def validate(root):
    root = Path(root).resolve()
    errors = []

    def fail(where, message):
        errors.append(f"{where}: {message}")

    def read(path):
        return path.read_text(encoding="utf-8")

    try:
        manifest = json.loads(read(root / "UPSTREAMS.json"), object_pairs_hook=unique_json)
        if not isinstance(manifest, dict) or not isinstance(manifest.get("skills"), list):
            raise ValueError("expected an object containing a skills array")
    except (OSError, UnicodeError, ValueError) as exc:
        return [f"UPSTREAMS.json: {exc}"]
    skills_dir = root / "skills"
    if not skills_dir.is_dir() or skills_dir.is_symlink():
        return ["skills: expected a real directory"]
    packages = {p.name: p for p in skills_dir.iterdir() if p.is_dir()}
    entries = {}
    for entry in manifest["skills"]:
        if not isinstance(entry, dict) or not isinstance(entry.get("name"), str):
            fail("UPSTREAMS.json", "each skill must be an object with a string name")
            continue
        name = entry["name"]
        if name in entries:
            fail(name, "duplicate manifest entry")
        entries[name] = entry
    for name in sorted(packages.keys() ^ entries.keys()):
        fail(name, "package/UPSTREAMS.json coverage mismatch")

    for name, package in sorted(packages.items()):
        entry = entries.get(name, {})
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            fail(name, "directory name must be lowercase hyphenated ASCII, at most 64 characters")
        if package.is_symlink():
            fail(name, "package must not be a symlink")
            continue
        for path in package.rglob("*"):
            if path.is_symlink():
                fail(name, f"symlink is not a portable packaged file: {path.relative_to(package)}")
        try:
            text = read(package / "SKILL.md")
            match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)(.*)\Z", text, re.DOTALL)
            if not match:
                raise ValueError("missing opening/closing YAML frontmatter delimiters")
            meta = yaml.load(match[1], Loader=UniqueLoader)
            if not isinstance(meta, dict):
                raise ValueError("frontmatter must be a mapping")
            if meta.get("name") != name:
                fail(name, "frontmatter name must match directory name")
            description = meta.get("description")
            if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                fail(name, "description must be a nonblank string of at most 1024 characters")
            if not match[2].strip():
                fail(name, "SKILL.md must contain instructions after frontmatter")
        except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
            fail(name, f"SKILL.md: {exc}")
        licenses = [package / p for p in ("LICENSE", "LICENSE.txt", "LICENSE.md")]
        if not any(p.is_file() and p.stat().st_size for p in licenses):
            fail(name, "missing nonempty per-skill license")
        try:
            source = read(package / "SOURCE.md")
            for key in ("repository", "revision", "license"):
                if not isinstance(entry.get(key), str) or not entry[key] or entry[key] not in source:
                    fail(name, f"SOURCE.md must identify manifest {key}")
        except (OSError, UnicodeError) as exc:
            fail(name, f"SOURCE.md: {exc}")
        if not re.fullmatch(r"[\w.-]+/[\w.-]+", str(entry.get("repository", ""))):
            fail(name, "repository must be owner/repository")
        if not re.fullmatch(r"[0-9a-f]{40}", str(entry.get("revision", ""))):
            fail(name, "revision must be a pinned Git SHA-1")
        try:
            path = entry.get("path")
            package_path(package, path)
            if PurePosixPath(path).name != "SKILL.md":
                fail(name, "upstream path must identify SKILL.md")
        except (ValueError, TypeError) as exc:
            fail(name, f"upstream path: {exc}")
        modified = entry.get("modified")
        if type(modified) is not bool:
            fail(name, "modified must be a JSON boolean")
        files = entry.get("files", {})
        if not isinstance(files, dict):
            fail(name, "files must be a path-to-Git-blob-hash object")
            files = {}
        files = dict(files)
        if "blob_sha" in entry:
            if "SKILL.md" in files and files["SKILL.md"] != entry["blob_sha"]:
                fail(name, "blob_sha disagrees with files.SKILL.md")
            files.setdefault("SKILL.md", entry["blob_sha"])
        if "SKILL.md" not in files:
            fail(name, "missing delivered SKILL.md hash")
        actual = {p.relative_to(package).as_posix() for p in package.rglob("*") if p.is_file()}
        # Legacy unchanged entries omit vault-authored provenance and root license copies.
        required = actual if modified is True else actual - {"SOURCE.md", "LICENSE", "LICENSE.txt", "LICENSE.md", "NOTICE"}
        for missing in sorted(required - files.keys()):
            fail(name, f"file missing from hash inventory: {missing}")
        for relative, expected in files.items():
            try:
                path = package_path(package, relative)
                if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{40}", expected):
                    raise ValueError("expected a Git blob SHA-1")
                if blob_hash(path.read_bytes()) != expected:
                    fail(name, f"Git blob hash mismatch: {relative}")
            except (OSError, ValueError) as exc:
                fail(name, f"files.{relative}: {exc}")
        if modified is True:
            upstream = entry.get("upstream_files")
            sha256 = entry.get("sha256")
            if "blob_sha" in entry:
                fail(name, "adaptations must separate upstream_files from delivered files; omit blob_sha")
            summary = entry.get("adaptation_summary")
            if entry.get("content_kind") != "adapted-and-rewritten" or not isinstance(summary, str) or not summary.strip():
                fail(name, "adaptations require content_kind and adaptation_summary")
            if not isinstance(upstream, dict) or entry.get("path") not in upstream:
                fail(name, "upstream_files must include the original upstream SKILL.md path")
            else:
                for relative, record in upstream.items():
                    try:
                        package_path(package, relative)  # Syntax only; consulted inputs need not be bundled.
                        if not isinstance(record, dict) or not re.fullmatch(r"[0-9a-f]{40}", str(record.get("git_blob_sha", ""))) or not isinstance(record.get("role"), str) or not record["role"].strip():
                            raise ValueError("upstream record requires Git blob SHA-1 and role")
                        if record["role"] == "copied unchanged" and files.get(relative) != record["git_blob_sha"]:
                            fail(name, f"copied unchanged upstream hash disagrees with delivered hash: {relative}")
                    except ValueError as exc:
                        fail(name, f"upstream_files.{relative}: {exc}")
            if not isinstance(sha256, dict) or set(sha256) != set(files):
                fail(name, "adaptation sha256 inventory must match delivered files")
            else:
                for relative, expected in sha256.items():
                    try:
                        path = package_path(package, relative)
                        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected) or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                            fail(name, f"SHA-256 mismatch: {relative}")
                    except (OSError, ValueError) as exc:
                        fail(name, f"sha256.{relative}: {exc}")
        elif "upstream_files" in entry or "sha256" in entry:
            fail(name, "separate adaptation hash fields require modified: true")
        for doc in sorted(package.rglob("*.md")):
            if doc.is_symlink():
                continue
            try:
                for target in link_targets(read(doc)):
                    url = urlsplit(target)
                    if url.scheme or url.netloc or not url.path:
                        continue
                    relative = unquote(url.path)
                    destination = doc.parent / relative
                    boundary = root if doc.name == "SOURCE.md" and doc.parent == package else package
                    if "\\" in relative or not destination.resolve().is_relative_to(boundary.resolve()):
                        fail(name, f"local reference escapes {'repository' if boundary == root else 'isolated package'}: {target}")
                    elif not destination.exists():
                        fail(name, f"missing local reference in {doc.relative_to(package)}: {target}")
            except (OSError, UnicodeError, ValueError) as exc:
                fail(name, f"{doc.relative_to(package)}: {exc}")
    try:
        readme = read(root / "README.md")
        catalog = re.findall(r"^- \[([^\]]+)\]\(skills/([^/]+)/SKILL\.md\)", readme, re.MULTILINE)
        if len(catalog) != len(packages) or {b for _, b in catalog} != set(packages) or any(a != b for a, b in catalog):
            fail("README.md", "catalog must list every package exactly once with matching labels")
        for filename in ("README.md", "THIRD_PARTY_NOTICES.md"):
            text = read(root / filename)
            number = r"\d+|(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand)(?:-[a-z]+)?"
            for token, kind in re.findall(rf"\b({number}) (public, licensed skills|curated upstream skills|(?:clearly marked |explicitly marked )?adapt(?:ed (?:engineering )?skills|ations))", text):
                try:
                    count = stated_count(token)
                except ValueError as exc:
                    fail(filename, str(exc))
                    continue
                expected = len(packages) if kind == "public, licensed skills" else sum(e.get("modified") is False for e in entries.values()) if kind == "curated upstream skills" else sum(e.get("modified") is True for e in entries.values())
                if count != expected:
                    fail(filename, f"stale {kind} count: {count}, expected {expected}")
    except (OSError, UnicodeError) as exc:
        fail("catalog", str(exc))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"Validation failed: {len(errors)} error(s)")
        return 1
    print("Vault validation passed (metadata, references, provenance, hashes, catalog).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
