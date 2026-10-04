"""Contract regressions using disposable original fixtures, no agent execution."""
import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.check_evaluations import (Invalid, check_criterion, digest, load, package_inventory,
                                     template, validate_dataset, validate_report)

ROOT = Path(__file__).resolve().parents[1]


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / "evaluations", self.root / "evaluations")
        shutil.copytree(ROOT / "skills", self.root / "skills")
        shutil.copy2(ROOT / "UPSTREAMS.json", self.root / "UPSTREAMS.json")
        self.data = load(self.root / "evaluations/cases.json")

    def save(self):
        path = self.root / "evaluations/cases.json"
        path.write_bytes((json.dumps(self.data, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))

    def bad_dataset(self, expected):
        self.save()
        with self.assertRaisesRegex(Invalid, expected):
            validate_dataset(self.root)

    def executed_report(self, kind="behavior"):
        data = validate_dataset(self.root)
        report = template(self.root, data)
        case = next(c for c in data["cases"] if c["kind"] == kind)
        run = next(r for r in report["runs"] if r["case_id"] == case["id"])
        skills = case["expected"]["acceptable_skill_sets"][0]
        fixtures = sorted({c["fixture"] for c in case["evidence_criteria"]})
        report["runs"] = [run]
        report["environment"] = {"provider": "synthetic-test-only", "model": "fixture-test-double", "model_version": "v1",
                                 "settings": {}, "run_date": "2026-10-04", "vault_revision": "a" * 40,
                                 "operator": "unittest; no real model invoked"}
        run.update(status="executed", reason=None, cost_usd=0,
                   context={"catalog_sha256": digest(self.root / "UPSTREAMS.json"), "loaded_skills": skills,
                            "files": package_inventory(self.root, skills),
                            "fixtures": [{"path": p, "sha256": digest(self.root / p)} for p in fixtures]},
                   output={"action": "select", "skills": skills, "response": "Synthetic record for schema tests only.",
                           "evidence_ids": [c["id"] for c in case["evidence_criteria"]]})
        return data, report, run

    def test_authored_dataset_has_bilingual_pairs_and_behavior_facts(self):
        data = validate_dataset(self.root)
        self.assertEqual(len(data["cases"]), 38)
        self.assertEqual(sum(c["kind"] == "behavior" for c in data["cases"]), 6)

    def test_unicode_roundtrip_preserves_chinese_and_punctuation(self):
        path = self.root / "evaluations/cases.json"
        before = path.read_bytes()
        self.assertIn("请".encode("utf-8"), before)
        self.assertIn("yesterday’s".encode("utf-8"), before)
        self.save()
        self.assertEqual(before, path.read_bytes())
        self.assertEqual(validate_dataset(self.root), self.data)

    def test_invalid_case_schema_and_unknown_fields(self):
        for mutation, expected in [(lambda c: c.update(language="zh"), "language"),
                                   (lambda c: c.update(prompt=" "), "nonblank"),
                                   (lambda c: c.update(kind="benchmark"), "case kind"),
                                   (lambda c: c.update(typo=True), "expected keys")]:
            original = copy.deepcopy(self.data)
            with self.subTest(expected=expected):
                mutation(self.data["cases"][0])
                self.bad_dataset(expected)
            self.data = original

    def test_missing_duplicate_or_inconsistent_pair(self):
        self.data["cases"].pop(1)
        self.bad_dataset("English/Chinese pair")
        self.data = load(ROOT / "evaluations/cases.json")
        self.data["cases"][1]["id"] = self.data["cases"][0]["id"]
        self.bad_dataset("duplicate case id")
        self.data = load(ROOT / "evaluations/cases.json")
        self.data["cases"][1]["expected"]["forbidden_skills"] = []
        self.bad_dataset("paired expected outcomes differ")

    def test_chinese_prompt_is_not_english_copy(self):
        self.data["cases"][1]["prompt"] = "English only"
        self.bad_dataset("CJK")

    def test_expectation_unknown_conflicting_empty_and_duplicate_skills(self):
        for sets, forbidden, expected in [([["not-in-vault"]], [], "unknown skill"),
                                           ([["unity-debug"]], ["unity-debug"], "conflict"),
                                           ([], [], "only select"),
                                           ([["unity-debug", "unity-debug"]], [], "duplicate skill"),
                                           ([["unity-debug"], ["unity-debug"]], [], "duplicate acceptable")]:
            original = copy.deepcopy(self.data)
            with self.subTest(expected=expected):
                self.data["cases"][0]["expected"].update(acceptable_skill_sets=sets, forbidden_skills=forbidden)
                self.bad_dataset(expected)
            self.data = original

    def test_clarification_and_action_contracts(self):
        case = next(c for c in self.data["cases"] if c["expected"]["action"] == "clarify")
        case["expected"]["clarification"] = None
        self.bad_dataset("nonblank")

    def test_behavior_fixture_facts_must_exist_and_match(self):
        case = next(c for c in self.data["cases"] if c["kind"] == "behavior")
        criterion = case["evidence_criteria"][0]
        for key, value, expected in [("fixture", "../outside.json", "unsafe"),
                                     ("fixture", "evaluations/fixtures/missing.json", "missing file"),
                                     ("pointer", "/missing", "pointer not found"),
                                     ("equals", "wrong", "fixture fact changed")]:
            original = criterion[key]
            with self.subTest(key=key):
                criterion[key] = value
                self.bad_dataset(expected)
                criterion[key] = original

    def test_json_pointer_escaped_keys(self):
        path = self.root / "evaluations/fixtures/escaped.json"
        path.write_text('{"a/b~c": true}', encoding="utf-8")
        c = {"id": "escaped", "fixture": "evaluations/fixtures/escaped.json", "pointer": "/a~1b~0c",
             "equals": True, "meaning": "Pointer supports escaped slash and tilde."}
        check_criterion(c, self.root, set())
        c["equals"] = 1
        with self.assertRaisesRegex(Invalid, "fixture fact changed"):
            check_criterion(c, self.root, set())

    def test_duplicate_json_keys_and_nonfinite_numbers_are_rejected(self):
        path = self.root / "evaluations/cases.json"
        for content in ('{"a": 1, "a": 2}', '{"cost": NaN}', '{"cost": Infinity}', '{"cost": 1e1000}'):
            with self.subTest(content=content):
                path.write_text(content, encoding="utf-8")
                with self.assertRaises(Invalid):
                    load(path)

    def test_invalid_json_pointer_array_indices(self):
        case = next(c for c in self.data["cases"] if c["pair_id"] == "task-review-contract")
        c = copy.deepcopy(case["evidence_criteria"][0])
        for index in ("-1", "01", "+1"):
            with self.subTest(index=index):
                c["pointer"] = f"/callers/{index}/count"
                with self.assertRaisesRegex(Invalid, "array index"):
                    check_criterion(c, self.root, set())

    def test_template_is_all_not_run_without_score(self):
        data = validate_dataset(self.root)
        report = template(self.root, data)
        summary = validate_report(self.root, data, report)
        self.assertEqual(summary["executed"], 0)
        self.assertEqual(summary["not_run"], 38)
        self.assertIsNone(summary["quality_score"])
        self.assertEqual(summary["unrecorded"], 0)

    def test_unrun_environment_nullable_types_and_dates(self):
        data = validate_dataset(self.root)
        for key, value in [("provider", []), ("model", False), ("model_version", {}), ("settings", 7),
                           ("run_date", ["invalid"]), ("run_date", "2026-02-30"),
                           ("vault_revision", 12), ("operator", True)]:
            report = template(self.root, data)
            with self.subTest(key=key, value=value):
                report["environment"][key] = value
                with self.assertRaises(Invalid):
                    validate_report(self.root, data, report)

    def test_executed_run_date_must_be_iso_calendar_date(self):
        data, report, run = self.executed_report()
        for value in ("this is not a date", "2026-02-30", "20261004"):
            with self.subTest(value=value):
                report["environment"]["run_date"] = value
                with self.assertRaises(Invalid):
                    validate_report(self.root, data, report)

    def test_baseline_records_no_real_execution(self):
        data = validate_dataset(self.root)
        summary = validate_report(self.root, data, load(self.root / "evaluations/not-run.json"))
        self.assertEqual(summary["recorded"], 6)
        self.assertEqual(summary["executed"], 0)
        self.assertEqual(summary["not_run"], 6)
        self.assertEqual(summary["unrecorded"], 32)

    def test_unrun_cannot_contain_fabricated_pass_or_output(self):
        data = validate_dataset(self.root)
        for key, value in [("output", {}), ("cost_usd", 0),
                           ("assessment", {"verdict": "pass", "reviewer": "test", "notes": "claimed pass"})]:
            report = template(self.root, data)
            with self.subTest(key=key):
                report["runs"][0][key] = value
                with self.assertRaises(Invalid):
                    validate_report(self.root, data, report)

    def test_record_schema_only_has_no_quality_score(self):
        data, report, run = self.executed_report()
        summary = validate_report(self.root, data, report)
        self.assertEqual(summary["executed"], 1)
        self.assertIsNone(summary["quality_score"])
        self.assertEqual(summary["unrecorded"], 37)

    def test_executed_record_requires_identity_context_and_cost(self):
        for mutate in [lambda r, x: r["environment"].update(model_version=None),
                       lambda r, x: r["environment"].update(settings=None),
                       lambda r, x: x.update(cost_usd=None), lambda r, x: x.update(cost_usd=True),
                       lambda r, x: x.update(cost_usd=float("nan")),
                       lambda r, x: x["context"]["files"].pop(),
                       lambda r, x: x["context"]["fixtures"].clear()]:
            data, report, run = self.executed_report()
            mutate(report, run)
            with self.assertRaises(Invalid):
                validate_report(self.root, data, report)

    def test_stale_dataset_and_unknown_report_cases(self):
        data, report, run = self.executed_report()
        report["dataset_sha256"] = "0" * 64
        with self.assertRaisesRegex(Invalid, "stale"):
            validate_report(self.root, data, report)
        report["dataset_sha256"] = digest(self.root / "evaluations/cases.json")
        run["case_id"] = "unknown"
        with self.assertRaisesRegex(Invalid, "unknown or duplicate"):
            validate_report(self.root, data, report)

    def test_human_pass_requires_expected_outcome_and_evidence(self):
        data, report, run = self.executed_report()
        run["assessment"] = {"verdict": "pass", "reviewer": "synthetic-test-reviewer", "notes": "Only testing record schema."}
        validate_report(self.root, data, report)
        run["output"]["evidence_ids"].pop()
        with self.assertRaisesRegex(Invalid, "every evidence"):
            validate_report(self.root, data, report)
        data, report, run = self.executed_report("routing")
        run["assessment"] = {"verdict": "pass", "reviewer": "synthetic", "notes": "Schema test only."}
        run["output"].update(action="clarify", skills=[])
        with self.assertRaisesRegex(Invalid, "authored action"):
            validate_report(self.root, data, report)

    def test_context_inventory_includes_references_resources_and_provenance(self):
        records = package_inventory(self.root, ["unity-debug"])
        paths = {r["path"] for r in records}
        self.assertIn("skills/unity-debug/reference/harness-trust.md", paths)
        self.assertIn("skills/unity-debug/resources/DevDebug.cs", paths)
        self.assertIn("skills/unity-debug/SOURCE.md", paths)
        self.assertIn("skills/unity-debug/LICENSE.txt", paths)

    def test_cli_check_and_failure(self):
        script = ROOT / "tools/check_evaluations.py"
        result = subprocess.run([sys.executable, str(script), "--root", str(self.root), "check"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout)["agent_runs"], 0)
        self.data["cases"][0]["expected"]["action"] = "unknown"
        self.save()
        result = subprocess.run([sys.executable, str(script), "--root", str(self.root), "check"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
