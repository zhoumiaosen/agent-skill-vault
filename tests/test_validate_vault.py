"""Synthetic packages: no upstream instructions or hooks are executed."""
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.validate_vault import blob_hash, validate


class VaultTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.package = self.root / "skills" / "example"
        self.package.mkdir(parents=True)
        self.write("SKILL.md", "---\nname: example\ndescription: >-\n  Use when checking a\n  synthetic package.\nmetadata:\n  author: test\n---\n# Example\n\nRead [guide](references/guide.md).\n")
        self.write("references/guide.md", "# Guide\n\nRead [entry](../SKILL.md).\n")
        self.write("LICENSE", "MIT License\nCopyright (c) 2026 Fixture Authors\nPermission is hereby granted, free of charge.\n")
        self.write("SOURCE.md", "Upstream: https://github.com/example/fixture\nRevision: " + "a" * 40 + "\nLicense: MIT\n[Manifest](../../UPSTREAMS.json)\n")
        self.entry = {"name": "example", "repository": "example/fixture", "revision": "a" * 40,
                      "path": "skills/example/SKILL.md", "license": "MIT", "modified": False}
        self.refresh()
        (self.root / "README.md").write_text("- [example](skills/example/SKILL.md)\n", encoding="utf-8")
        (self.root / "THIRD_PARTY_NOTICES.md").write_text("Fixture notices\n", encoding="utf-8")

    def write(self, name, text):
        path = self.package / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode("utf-8"))

    def save(self, entries=None):
        (self.root / "UPSTREAMS.json").write_text(json.dumps({"skills": entries if entries is not None else [self.entry]}), encoding="utf-8")

    def refresh(self):
        self.entry["files"] = {p.relative_to(self.package).as_posix(): blob_hash(p.read_bytes())
                               for p in self.package.rglob("*") if p.is_file() and p.name != "SOURCE.md"}
        self.save()

    def assert_error(self, expected):
        errors = validate(self.root)
        self.assertTrue(any(expected in error for error in errors), errors)

    def adapt(self):
        self.entry.update(modified=True, content_kind="adapted-and-rewritten", adaptation_summary="Original fixture adaptation",
                          upstream_files={self.entry["path"]: {"git_blob_sha": "b" * 40, "role": "adaptation input"},
                                          "LICENSE": {"git_blob_sha": self.entry["files"]["LICENSE"], "role": "copied unchanged"}})
        self.entry["files"]["SOURCE.md"] = blob_hash((self.package / "SOURCE.md").read_bytes())
        self.entry["sha256"] = {p: hashlib.sha256((self.package / p).read_bytes()).hexdigest() for p in self.entry["files"]}
        self.save()

    def test_valid_folded_frontmatter_and_nested_metadata(self):
        self.assertEqual(validate(self.root), [])

    def test_valid_quoted_descriptions_and_literal_blocks(self):
        for value in ("'Use when: testing # quoted text'", '"Use when testing"', "|\n  Use when testing.\n  More text."):
            with self.subTest(value=value):
                self.write("SKILL.md", f"---\nname: example\ndescription: {value}\n---\nInstructions\n")
                self.refresh()
                self.assertEqual(validate(self.root), [])

    def test_valid_legacy_blob_only(self):
        (self.package / "references/guide.md").unlink()
        self.write("SKILL.md", "---\nname: example\ndescription: Use when testing\n---\nInstructions\n")
        self.entry.pop("files")
        self.entry["blob_sha"] = blob_hash((self.package / "SKILL.md").read_bytes())
        self.save()
        self.assertEqual(validate(self.root), [])

    def test_adaptation_checks_delivered_hashes_not_upstream_inputs(self):
        self.adapt()
        self.assertEqual(validate(self.root), [])
        self.entry["files"]["SKILL.md"] = "b" * 40
        self.save()
        self.assert_error("Git blob hash mismatch: SKILL.md")

    def test_adaptation_sha256_and_inventory(self):
        self.adapt()
        self.entry["sha256"]["SOURCE.md"] = "0" * 64
        self.save()
        self.assert_error("SHA-256 mismatch: SOURCE.md")
        del self.entry["sha256"]["SOURCE.md"]
        self.save()
        self.assert_error("sha256 inventory")

    def test_adaptation_requires_original_source_record(self):
        self.adapt()
        self.entry["upstream_files"] = {}
        self.save()
        self.assert_error("original upstream SKILL.md")

    def test_copied_license_keeps_original_hash(self):
        self.adapt()
        self.entry["upstream_files"]["LICENSE"]["git_blob_sha"] = "0" * 40
        self.save()
        self.assert_error("copied unchanged upstream hash")

    def test_bad_frontmatter(self):
        cases = [
            ("name: example\ndescription: test", "delimiters"),
            ("---\nname: example\ndescription: test\n", "delimiters"),
            ("---\nname: wrong\ndescription: test\n---\nBody", "name must match"),
            ("---\nname: example\nname: example\ndescription: test\n---\nBody", "unique strings"),
            ("---\nname: example\ndescription: [test]\n---\nBody", "description must"),
            ("---\nname: example\ndescription: ' '\n---\nBody", "description must"),
            ("---\nname: example\ndescription: " + "x" * 1025 + "\n---\nBody", "description must"),
            ("---\nname: example\ndescription: !!python/object:bad {}\n---\nBody", "constructor"),
            ("---\nname: example\ndescription: [broken\n---\nBody", "SKILL.md:"),
            ("---\nname: example\ndescription: test\n---\n", "instructions"),
        ]
        for text, expected in cases:
            with self.subTest(expected=expected):
                self.write("SKILL.md", text)
                self.assert_error(expected)

    def test_missing_license_and_source(self):
        (self.package / "LICENSE").unlink()
        (self.package / "SOURCE.md").unlink()
        self.assert_error("per-skill license")
        self.assert_error("SOURCE.md:")

    def test_source_metadata_mismatch(self):
        self.write("SOURCE.md", "Wrong source")
        self.assert_error("identify manifest revision")

    def test_missing_link_and_reference_definition(self):
        self.write("references/guide.md", "Read [guide][g].\n\n[g]: missing.md\n")
        self.refresh()
        self.assert_error("missing local reference")

    def test_empty_alt_image_requires_bundled_asset(self):
        self.write("references/guide.md", "![](missing.png)\n")
        self.refresh()
        self.assert_error("missing local reference")

    def test_isolated_package_does_not_allow_repo_reference(self):
        self.write("references/guide.md", "[root](../../../README.md)\n")
        self.refresh()
        self.assert_error("escapes isolated package")

    def test_examples_and_external_links_are_not_dependencies(self):
        self.write("references/guide.md", "```python\nx = a[b](missing)\n```\n`[code](missing.md)`\n[web](https://example.com/no.md)\n[anchor](#heading)\n")
        self.refresh()
        self.assertEqual(validate(self.root), [])

    def test_deleted_supporting_file(self):
        (self.package / "references/guide.md").unlink()
        self.assert_error("files.references/guide.md:")

    def test_untracked_supporting_file_is_not_silently_unhashed(self):
        self.write("scripts/new.py", "# Never executed\n")
        self.assert_error("file missing from hash inventory")

    def test_byte_changes_and_crlf_are_detected(self):
        path = self.package / "SKILL.md"
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        self.assert_error("Git blob hash mismatch")

    def test_manifest_coverage_and_duplicates(self):
        self.save([])
        self.assert_error("coverage mismatch")
        self.save([self.entry, self.entry])
        self.assert_error("duplicate manifest entry")

    def test_malformed_manifest_reports_errors(self):
        for content in ('{"skills": [{"name": "example", "name": "hidden"}]}', '{"skills": {}}', '[]', '{broken'):
            with self.subTest(content=content):
                (self.root / "UPSTREAMS.json").write_text(content, encoding="utf-8")
                self.assert_error("UPSTREAMS.json:")

    def test_malformed_manifest_fields(self):
        for key, value, expected in [("files", [], "files must"), ("modified", "false", "JSON boolean"),
                                     ("revision", "main", "pinned Git"), ("repository", "invalid", "owner/repository"),
                                     ("path", "../SKILL.md", "unsafe"), ("files", {"../outside": "0" * 40}, "unsafe"),
                                     ("files", {"SKILL.md": 5}, "Git blob SHA-1")]:
            with self.subTest(key=key, value=value):
                original = self.entry[key]
                self.entry[key] = value
                self.save()
                self.assert_error(expected)
                self.entry[key] = original

    def test_conflicting_blob_alias(self):
        self.entry["blob_sha"] = "0" * 40
        self.save()
        self.assert_error("blob_sha disagrees")

    def test_catalog_missing_duplicate_and_wrong_label(self):
        for text in ("", "- [wrong](skills/example/SKILL.md)\n", "- [example](skills/example/SKILL.md)\n" * 2):
            with self.subTest(text=text):
                (self.root / "README.md").write_text(text, encoding="utf-8")
                self.assert_error("catalog must list")

    def test_stale_prose_counts(self):
        for filename in ("README.md", "THIRD_PARTY_NOTICES.md"):
            with self.subTest(filename=filename):
                path = self.root / filename
                path.write_text(path.read_text(encoding="utf-8") + "thirty-four curated upstream skills\n", encoding="utf-8")
                self.assert_error("stale curated upstream skills count")

    def test_new_spelled_and_unsupported_counts_are_not_ignored(self):
        for token in ("thirty-eight", "forty-two", "hundred", "38"):
            with self.subTest(token=token):
                (self.root / "THIRD_PARTY_NOTICES.md").write_text(f"{token} public, licensed skills\n", encoding="utf-8")
                self.assertTrue(validate(self.root))

    def test_adaptation_summary_requires_nonblank_string(self):
        self.adapt()
        for summary in (" ", ["summary"], None):
            with self.subTest(summary=summary):
                self.entry["adaptation_summary"] = summary
                self.save()
                self.assert_error("adaptation_summary")

    def test_cli_success_and_failure_exit_status(self):
        script = Path(__file__).resolve().parents[1] / "tools/validate_vault.py"
        result = subprocess.run([sys.executable, str(script), "--root", str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        (self.package / "SKILL.md").unlink()
        result = subprocess.run([sys.executable, str(script), "--root", str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("SKILL.md", result.stdout)


if __name__ == "__main__":
    unittest.main()
