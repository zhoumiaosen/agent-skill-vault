"""Validate authored evaluation fixtures and manual run records; never call a model."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from datetime import date
from pathlib import Path, PurePosixPath


class Invalid(ValueError):
    """An evaluation contract or fixture is invalid."""


def require(condition, message):
    if not condition:
        raise Invalid(message)


def text(value, label):
    require(isinstance(value, str) and bool(value.strip()), f"{label}: expected nonblank string")


def keys(value, required, label):
    require(isinstance(value, dict) and set(value) == set(required.split()), f"{label}: expected keys {required}")


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def finite_float(value):
    number = float(value)
    require(math.isfinite(number), "JSON number must be finite")
    return number


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs, parse_float=finite_float,
                          parse_constant=lambda value: (_ for _ in ()).throw(Invalid(f"invalid JSON constant: {value}")))
    except (OSError, UnicodeError, ValueError) as exc:
        raise Invalid(f"{path.name}: {exc}") from exc


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_file(root, relative, prefix=None):
    text(relative, "path")
    path = PurePosixPath(relative)
    require(not path.is_absolute() and ".." not in path.parts and "\\" not in relative and ":" not in relative
            and str(path) == relative, f"unsafe path: {relative}")
    require(prefix is None or relative.startswith(prefix), f"path must start with {prefix}: {relative}")
    target = root / relative
    require(not any(p.is_symlink() for p in (target, *target.parents)), f"symlink path: {relative}")
    require(target.is_file(), f"missing file: {relative}")
    return target


def skill_list(value, available, label, nonempty=False):
    require(isinstance(value, list) and (bool(value) or not nonempty), f"{label}: expected skill list")
    require(all(isinstance(s, str) and s in available for s in value), f"{label}: unknown skill")
    require(len(value) == len(set(value)), f"{label}: duplicate skill")


def catalog(root):
    data = load(root / "UPSTREAMS.json")
    require(isinstance(data, dict) and isinstance(data.get("skills"), list), "invalid upstream manifest")
    names = [e.get("name") for e in data["skills"] if isinstance(e, dict)]
    require(all(isinstance(n, str) for n in names) and len(names) == len(data["skills"])
            and len(names) == len(set(names)), "invalid upstream skill names")
    for name in names:
        local_file(root, f"skills/{name}/SKILL.md", "skills/")
    return set(names)


def check_expectation(expected, available, label):
    keys(expected, "action acceptable_skill_sets forbidden_skills rationale clarification", label)
    require(expected["action"] in ("select", "no_skill", "clarify"), f"{label}: invalid action")
    text(expected["rationale"], f"{label}.rationale")
    skill_list(expected["forbidden_skills"], available, f"{label}.forbidden_skills")
    sets = expected["acceptable_skill_sets"]
    require(isinstance(sets, list), f"{label}: acceptable_skill_sets must be a list")
    require(bool(sets) == (expected["action"] == "select"), f"{label}: only select has acceptable skill sets")
    seen = set()
    for skills in sets:
        skill_list(skills, available, f"{label}.acceptable_skill_sets", nonempty=True)
        normalized = frozenset(skills)
        require(normalized not in seen, f"{label}: duplicate acceptable skill set")
        seen.add(normalized)
        require(not normalized.intersection(expected["forbidden_skills"]), f"{label}: acceptable/forbidden conflict")
    if expected["action"] == "clarify":
        text(expected["clarification"], f"{label}.clarification")
    else:
        require(expected["clarification"] is None, f"{label}: clarification must be null")


def check_criterion(criterion, root, ids):
    keys(criterion, "id fixture pointer equals meaning", "criterion")
    text(criterion["id"], "criterion.id")
    require(criterion["id"] not in ids, "duplicate evidence criterion")
    ids.add(criterion["id"])
    text(criterion["meaning"], "criterion.meaning")
    fixture = local_file(root, criterion["fixture"], "evaluations/fixtures/")
    value = load(fixture)
    pointer = criterion["pointer"]
    require(isinstance(pointer, str) and pointer.startswith("/"), "criterion pointer must be a JSON Pointer")
    try:
        for token in pointer[1:].split("/"):
            require(not re.search(r"~[^01]|~$", token), "invalid JSON Pointer escape")
            token = token.replace("~1", "/").replace("~0", "~")
            if isinstance(value, list):
                require(re.fullmatch(r"0|[1-9][0-9]*", token) is not None, "invalid JSON Pointer array index")
                value = value[int(token)]
            else:
                value = value[token]
    except Invalid:
        raise
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        raise Invalid(f"criterion pointer not found: {pointer}") from exc
    # JSON booleans and numbers must not compare equal accidentally (True == 1).
    require(type(value) is type(criterion["equals"]) and value == criterion["equals"],
            f"fixture fact changed: {criterion['id']}")


def validate_dataset(root):
    available = catalog(root)
    data = load(root / "evaluations/cases.json")
    keys(data, "schema_version context_policy cases", "dataset")
    require(type(data["schema_version"]) is int and data["schema_version"] == 1, "unsupported dataset schema_version")
    require(data["context_policy"] == "catalog-then-complete-packages", "unsupported context policy")
    require(isinstance(data["cases"], list) and bool(data["cases"]), "cases must be a nonempty list")
    ids, pairs = set(), {}
    for case in data["cases"]:
        keys(case, "id pair_id language kind boundary prompt expected evidence_criteria", "case")
        text(case["id"], "case.id")
        require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", case["id"]) is not None, "invalid case id")
        require(case["id"] not in ids, f"duplicate case id: {case['id']}")
        ids.add(case["id"])
        text(case["pair_id"], "case.pair_id")
        require(case["language"] in ("en", "zh-CN"), "case.language must be en or zh-CN")
        require(case["kind"] in ("routing", "behavior"), "invalid case kind")
        text(case["boundary"], "case.boundary")
        text(case["prompt"], "case.prompt")
        if case["language"] == "zh-CN":
            require(re.search(r"[\u3400-\u9fff]", case["prompt"]) is not None, "Chinese prompt must contain CJK text")
        check_expectation(case["expected"], available, case["id"])
        criteria = case["evidence_criteria"]
        require(isinstance(criteria, list), "evidence_criteria must be a list")
        require(bool(criteria) == (case["kind"] == "behavior"), "only behavior cases require evidence criteria")
        criterion_ids = set()
        for criterion in criteria:
            check_criterion(criterion, root, criterion_ids)
        pairs.setdefault(case["pair_id"], []).append(case)
    for pair_id, cases in pairs.items():
        require(len(cases) == 2 and {c["language"] for c in cases} == {"en", "zh-CN"}, f"{pair_id}: requires one English/Chinese pair")
        first, second = cases
        for key in ("kind", "boundary", "evidence_criteria"):
            require(first[key] == second[key], f"{pair_id}: paired {key} differs")
        for key in ("action", "acceptable_skill_sets", "forbidden_skills"):
            require(first["expected"][key] == second["expected"][key], f"{pair_id}: paired expected outcomes differ")
    for boundary in ("unity-debug/unity-profiling", "game-ui-ux/frontend-design", "requesting-code-review/receiving-code-review"):
        selected = [c for c in data["cases"] if c["boundary"] == boundary and c["kind"] == "routing"]
        require({c["expected"]["action"] for c in selected} == {"select", "no_skill", "clarify"}, f"{boundary}: missing positive/negative/ambiguous cases")
        for skill in boundary.split("/"):
            require(any([skill] in c["expected"]["acceptable_skill_sets"] for c in selected), f"{boundary}: missing positive case for {skill}")
    return data


def package_inventory(root, skills):
    """Manifest every file, including supporting content, SOURCE and license."""
    records = []
    for skill in sorted(skills):
        package = root / "skills" / skill
        for path in sorted(package.rglob("*")):
            require(not path.is_symlink(), f"symlink in context: {path}")
            if path.is_file():
                records.append({"path": path.relative_to(root).as_posix(), "sha256": digest(path)})
    return records


def template(root, dataset):
    return {
        "schema_version": 1, "dataset_sha256": digest(root / "evaluations/cases.json"),
        "environment": {"provider": None, "model": None, "model_version": None, "settings": None,
                        "run_date": None, "vault_revision": None, "operator": None},
        "runs": [{"case_id": c["id"], "status": "not_run", "reason": "No agent/model execution performed.",
                  "cost_usd": None, "context": None, "output": None,
                  "assessment": {"verdict": "not_assessed", "reviewer": None, "notes": None}}
                 for c in dataset["cases"]],
    }


def validate_report(root, dataset, report):
    """Validate recording integrity; do not infer behavior quality from prose."""
    keys(report, "schema_version dataset_sha256 environment runs", "report")
    require(type(report["schema_version"]) is int and report["schema_version"] == 1, "unsupported report schema_version")
    require(report["dataset_sha256"] == digest(root / "evaluations/cases.json"), "report dataset hash is stale")
    env = report["environment"]
    keys(env, "provider model model_version settings run_date vault_revision operator", "environment")
    for key in ("provider", "model", "model_version", "operator"):
        if env[key] is not None:
            text(env[key], f"environment.{key}")
    require(env["settings"] is None or isinstance(env["settings"], dict), "environment.settings must be null or an object")
    if env["vault_revision"] is not None:
        require(isinstance(env["vault_revision"], str) and re.fullmatch(r"[0-9a-f]{40}", env["vault_revision"]) is not None,
                "environment.vault_revision must be null or an exact Git SHA-1")
    if env["run_date"] is not None:
        require(isinstance(env["run_date"], str) and re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", env["run_date"]) is not None,
                "environment.run_date must be null or YYYY-MM-DD")
        try:
            date.fromisoformat(env["run_date"])
        except ValueError as exc:
            raise Invalid("environment.run_date must be a valid calendar date") from exc
    cases = {c["id"]: c for c in dataset["cases"]}
    require(isinstance(report["runs"], list) and bool(report["runs"]), "report runs must be a nonempty list")
    seen = set()
    for run in report["runs"]:
        keys(run, "case_id status reason cost_usd context output assessment", "run")
        case_id = run["case_id"]
        require(isinstance(case_id, str) and case_id in cases and case_id not in seen, "unknown or duplicate report case_id")
        seen.add(case_id)
        require(run["status"] in ("not_run", "blocked", "executed"), "invalid execution status")
        assessment = run["assessment"]
        keys(assessment, "verdict reviewer notes", "assessment")
        require(assessment["verdict"] in ("not_assessed", "pass", "fail"), "invalid assessment verdict")
        if run["status"] != "executed":
            text(run["reason"], "unrun reason")
            require(run["output"] is None and run["context"] is None and run["cost_usd"] is None,
                    "unrun cases cannot have output, loaded context or charged cost")
            require(assessment == {"verdict": "not_assessed", "reviewer": None, "notes": None}, "unrun cases cannot be assessed")
            continue
        for key in ("provider", "model", "model_version", "operator", "run_date"):
            text(env[key], f"environment.{key}")
        require(isinstance(env["settings"], dict), "executed runs require model settings (use {} if none)")
        require(isinstance(env["vault_revision"], str) and re.fullmatch(r"[0-9a-f]{40}", env["vault_revision"]) is not None,
                "executed runs require exact vault revision")
        cost = run["cost_usd"]
        require(type(cost) in (int, float) and (type(cost) is int or math.isfinite(cost)) and cost >= 0,
                "executed runs require actual nonnegative cost_usd")
        require(run["reason"] is None, "executed reason must be null")
        context = run["context"]
        keys(context, "catalog_sha256 loaded_skills files fixtures", "context")
        require(context["catalog_sha256"] == digest(root / "UPSTREAMS.json"), "catalog context hash is stale")
        available = catalog(root)
        skill_list(context["loaded_skills"], available, "context.loaded_skills")
        require(context["files"] == package_inventory(root, context["loaded_skills"]), "loaded package file inventory incomplete or stale")
        needed = sorted({c["fixture"] for c in cases[case_id]["evidence_criteria"]})
        require(context["fixtures"] == [{"path": p, "sha256": digest(root / p)} for p in needed], "fixture context incomplete or stale")
        output = run["output"]
        keys(output, "action skills response evidence_ids", "output")
        require(output["action"] in ("select", "no_skill", "clarify"), "invalid recorded action")
        skill_list(output["skills"], available, "output.skills")
        require(bool(output["skills"]) == (output["action"] == "select"), "only select may record skills")
        require(set(output["skills"]).issubset(context["loaded_skills"]), "selected skills require complete package context")
        text(output["response"], "output.response")
        evidence = output["evidence_ids"]
        allowed = {c["id"] for c in cases[case_id]["evidence_criteria"]}
        require(isinstance(evidence, list) and all(isinstance(e, str) and e in allowed for e in evidence)
                and len(evidence) == len(set(evidence)), "invalid evidence_ids")
        if assessment["verdict"] != "not_assessed":
            text(assessment["reviewer"], "assessment.reviewer")
            text(assessment["notes"], "assessment.notes")
            if assessment["verdict"] == "pass":
                expected = cases[case_id]["expected"]
                require(output["action"] == expected["action"], "pass disagrees with authored action")
                if output["action"] == "select":
                    require(set(output["skills"]) in [set(s) for s in expected["acceptable_skill_sets"]], "pass disagrees with authored skill sets")
                require(set(evidence) == allowed, "behavior pass must account for every evidence criterion")
        else:
            require(assessment["reviewer"] is None and assessment["notes"] is None, "unassessed reviewer/notes must be null")
    return {"dataset_cases": len(cases), "recorded": len(seen), "unrecorded": len(cases) - len(seen),
            "executed": sum(r["status"] == "executed" for r in report["runs"]),
            "not_run": sum(r["status"] == "not_run" for r in report["runs"]),
            "blocked": sum(r["status"] == "blocked" for r in report["runs"]),
            "quality_score": None, "scope": "record integrity only; responses and human assessments are not independently verified"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check")
    commands.add_parser("template")
    commands.add_parser("context")
    record = commands.add_parser("report")
    record.add_argument("file", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        dataset = validate_dataset(root)
        if args.command == "template":
            result = template(root, dataset)
        elif args.command == "context":
            result = {"catalog_sha256": digest(root / "UPSTREAMS.json"),
                      "files": package_inventory(root, catalog(root)),
                      "note": "Inventory only. Read full SKILL.md and supporting files; this command does not load them into a model."}
        elif args.command == "report":
            result = validate_report(root, dataset, load(args.file))
        else:
            result = {"fixture_validation": "passed", "cases": len(dataset["cases"]),
                      "languages": ["en", "zh-CN"], "agent_runs": 0, "quality_score": None,
                      "scope": "authored fixture/schema checks only; no model or engine executed"}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (Invalid, OSError, UnicodeError) as exc:
        print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
