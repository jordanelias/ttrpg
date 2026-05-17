#!/usr/bin/env python3
"""
mechanics_index_gen.py — Valoria mechanics index validator and generator (v1)

Pass 2j authoring deliverable. Operates against canon/mechanics_index.yaml.

v1 SCOPE (this version):
  - YAML round-trip validation (yaml.safe_load + re-dump for malformed-YAML detection)
  - Schema validation per mechanic entry (required fields present)
  - Cross-reference validation:
      - sim_module path: resolve relative to repo root; warn if file does not exist
      - canon_sources: resolve each path; warn if missing (section anchors not verified)
  - Drift report:
      - Count mechanics by test_status
      - List contested mechanics
      - List mechanics with canon_authoring_target but no canon_sources
      - Group by pending Pass-N authoring
  - GD-constraint coverage check:
      - Every gd_applicable entry must reference a GD declared in gd_constraints

v2 SCOPE (deferred):
  - Auto-population: scan designs/ for canonical-tagged sections, extract mechanic names,
    propose new index entries
  - sim/ module scanning: extract docstring Canon source / Status to cross-check against index
  - Section-anchor verification (#section-N-M actually exists in target doc)
  - Integration with safe_commit hook: enforce index update when sim_module or canon doc touched

USAGE:
  python3 tools/mechanics_index_gen.py [--repo-root /path/to/ttrpg] [--strict] [--update]

  --repo-root  defaults to current working directory if it contains canon/ and sim/
  --strict     warnings become errors (exit code 1 on any drift)
  --update     write back the drift_report section into mechanics_index.yaml

EXIT CODES:
  0  validation passed (warnings may have been emitted to stderr)
  1  --strict mode + drift detected, OR YAML malformed, OR schema violation
  2  CLI / IO error
"""

from __future__ import annotations

import argparse
import io
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("[FATAL] PyYAML not installed. pip install pyyaml --break-system-packages", file=sys.stderr)
    sys.exit(2)


# ── Schema definitions ──────────────────────────────────────────────────────

REQUIRED_TOP_LEVEL_KEYS = {
    "schema_version",
    "last_authored",
    "scales",
    "gd_constraints",
    "test_status_values",
    "mechanics",
    "categories",
}

REQUIRED_MECHANIC_KEYS = {"scale", "sim_module", "test_status"}

# faction is required for scale=personal|provincial|peninsular|world|cross_scale
# canon_sources is required for everything except mechanics with canon_authoring_target
OPTIONAL_MECHANIC_KEYS = {
    "faction",
    "canon_sources",
    "canon_authoring_target",
    "unified_canon_target",
    "params",
    "pp",
    "notes",
    "dependencies",
    "primitives",
    "tiers",
    "gd_applicable",
    "test_results",
    "v22_features_pending",
    "integration_plan_doc",
    "open_editorial",
}

VALID_SCALES = {
    "primitive",
    "service",
    "personal",
    "thread",
    "provincial",
    "territory",
    "peninsular",
    "world",
    "cross_scale",
}

VALID_TEST_STATUS = {
    "not_implemented",
    "provisional",
    "validated_n100",
    "validated_n500",
    "validated_n1000",
    "validated_n1000_v12c",
    "canonical",
    "contested",
    "superseded",
}


# ── Validation ──────────────────────────────────────────────────────────────


class ValidationError:
    def __init__(self, level: str, location: str, message: str):
        self.level = level  # "error" | "warning"
        self.location = location
        self.message = message

    def __str__(self) -> str:
        return f"[{self.level.upper()}] {self.location}: {self.message}"


def validate_yaml_roundtrip(content: str) -> tuple[Any, list[ValidationError]]:
    """Load YAML, re-dump it, and check round-trip viability."""
    errors: list[ValidationError] = []
    try:
        parsed = yaml.safe_load(content)
    except yaml.YAMLError as e:
        errors.append(ValidationError("error", "<file>", f"YAML parse failed: {e}"))
        return None, errors

    if parsed is None:
        errors.append(ValidationError("error", "<file>", "YAML empty or all-comments"))
        return None, errors

    # Attempt re-dump to detect lossy parse
    try:
        yaml.safe_dump(parsed, default_flow_style=False, sort_keys=False)
    except yaml.YAMLError as e:
        errors.append(ValidationError("warning", "<file>", f"YAML re-dump failed: {e}"))

    return parsed, errors


def validate_top_level(index: dict) -> list[ValidationError]:
    """Check required top-level keys present."""
    errors: list[ValidationError] = []
    missing = REQUIRED_TOP_LEVEL_KEYS - set(index.keys())
    for key in missing:
        errors.append(ValidationError("error", "<top-level>", f"missing required key: {key}"))

    if "schema_version" in index and index["schema_version"] != 1:
        errors.append(
            ValidationError("warning", "<top-level>",
                            f"schema_version={index['schema_version']} - validator written for v1")
        )

    return errors


def validate_mechanic(name: str, entry: dict, gd_constraints: dict) -> list[ValidationError]:
    """Validate a single mechanic entry."""
    errors: list[ValidationError] = []
    loc = f"mechanics.{name}"

    if not isinstance(entry, dict):
        errors.append(ValidationError("error", loc, "entry is not a mapping"))
        return errors

    # Required fields
    missing = REQUIRED_MECHANIC_KEYS - set(entry.keys())
    for key in missing:
        errors.append(ValidationError("error", loc, f"missing required key: {key}"))

    # Conditional required: canon_sources OR canon_authoring_target
    if "canon_sources" not in entry and "canon_authoring_target" not in entry:
        errors.append(
            ValidationError("error", loc,
                            "must have either 'canon_sources' or 'canon_authoring_target'")
        )

    # Unknown keys
    known_keys = REQUIRED_MECHANIC_KEYS | OPTIONAL_MECHANIC_KEYS
    unknown = set(entry.keys()) - known_keys
    for key in unknown:
        errors.append(ValidationError("warning", loc, f"unknown key: {key}"))

    # scale value
    scale = entry.get("scale")
    if scale and scale not in VALID_SCALES:
        errors.append(
            ValidationError("error", loc, f"invalid scale: {scale!r} (valid: {sorted(VALID_SCALES)})")
        )

    # test_status value
    ts = entry.get("test_status")
    if ts and ts not in VALID_TEST_STATUS:
        errors.append(
            ValidationError("error", loc, f"invalid test_status: {ts!r}")
        )

    # gd_applicable references valid GDs
    gd_list = entry.get("gd_applicable", [])
    for gd in gd_list:
        if gd not in gd_constraints:
            errors.append(
                ValidationError("error", loc,
                                f"gd_applicable references unknown constraint: {gd}")
            )

    # canon_sources type
    if "canon_sources" in entry and not isinstance(entry["canon_sources"], list):
        errors.append(ValidationError("error", loc, "canon_sources must be a list"))

    # sim_module type
    if "sim_module" in entry and not isinstance(entry["sim_module"], str):
        errors.append(ValidationError("error", loc, "sim_module must be a string"))

    # faction required for non-primitive, non-service scales
    if scale in {"personal", "thread", "provincial", "territory", "peninsular", "world", "cross_scale"}:
        if "faction" not in entry:
            errors.append(ValidationError("warning", loc, f"scale={scale} entries usually declare faction"))

    return errors


def validate_cross_references(index: dict, repo_root: Path) -> list[ValidationError]:
    """Resolve sim_module and canon_sources paths; warn on missing files."""
    errors: list[ValidationError] = []
    mechanics = index.get("mechanics", {})

    for name, entry in mechanics.items():
        loc = f"mechanics.{name}"

        sim_module = entry.get("sim_module")
        if sim_module:
            path = repo_root / sim_module
            if not path.exists():
                errors.append(
                    ValidationError("warning", loc, f"sim_module path does not exist: {sim_module}")
                )

        canon_sources = entry.get("canon_sources", [])
        for canon in canon_sources:
            # Strip section anchor (#section-X-Y)
            canon_path = canon.split("#", 1)[0]
            path = repo_root / canon_path
            if not path.exists():
                errors.append(
                    ValidationError("warning", loc, f"canon_sources path does not exist: {canon_path}")
                )

    return errors


def validate_gd_singularity(index: dict) -> list[ValidationError]:
    """GD-1 requires victory_paths category to contain exactly 1 entry."""
    errors: list[ValidationError] = []
    categories = index.get("categories", {})
    victory_paths = categories.get("victory_paths", [])

    if len(victory_paths) != 1:
        errors.append(
            ValidationError(
                "error",
                "categories.victory_paths",
                f"GD-1 requires exactly 1 victory path; found {len(victory_paths)}: {victory_paths}",
            )
        )
    elif victory_paths[0] != "peninsular_sovereignty":
        errors.append(
            ValidationError(
                "error",
                "categories.victory_paths",
                f"GD-1 requires victory_paths == ['peninsular_sovereignty']; got {victory_paths}",
            )
        )

    return errors


# ── Drift report generation ─────────────────────────────────────────────────


def compute_drift_report(index: dict) -> dict:
    """Compute the drift_report section based on current index state."""
    mechanics = index.get("mechanics", {})
    report: dict[str, Any] = {}

    report["last_generation"] = index.get("last_authored", "unknown")
    report["mechanics_total"] = len(mechanics)

    # by_test_status
    ts_counter: Counter = Counter()
    for entry in mechanics.values():
        ts = entry.get("test_status", "missing")
        ts_counter[ts] += 1
    report["by_test_status"] = dict(ts_counter)

    # contamination_flags
    contested = []
    for name, entry in mechanics.items():
        if entry.get("test_status") == "contested":
            note = entry.get("notes", "")
            # Truncate long notes
            short = note.split(".")[0][:80] if note else "no note"
            contested.append({name: short})
    report["contamination_flags"] = contested

    # gd_constraint_coverage
    gd_coverage: dict = defaultdict(list)
    for name, entry in mechanics.items():
        for gd in entry.get("gd_applicable", []):
            gd_coverage[gd].append(name)
    report["gd_constraint_coverage"] = dict(gd_coverage)

    # missing_canon_doc - has canon_authoring_target but empty canon_sources
    missing_canon = []
    for name, entry in mechanics.items():
        canon_sources = entry.get("canon_sources", [])
        if not canon_sources and "canon_authoring_target" in entry:
            missing_canon.append(name)
    report["missing_canon_doc"] = missing_canon

    return report


# ── Output formatting ───────────────────────────────────────────────────────


def emit_report(parsed: dict, all_errors: list[ValidationError]) -> str:
    """Pretty-print a validation summary."""
    out = io.StringIO()
    out.write("━" * 70 + "\n")
    out.write("Valoria Mechanics Index — Validation Report\n")
    out.write("━" * 70 + "\n\n")

    mechanics = parsed.get("mechanics", {}) if parsed else {}
    out.write(f"Mechanics registered: {len(mechanics)}\n")

    errors = [e for e in all_errors if e.level == "error"]
    warnings = [e for e in all_errors if e.level == "warning"]

    out.write(f"Errors:   {len(errors)}\n")
    out.write(f"Warnings: {len(warnings)}\n\n")

    if errors:
        out.write("─── Errors ──────────────────────────────────────\n")
        for e in errors:
            out.write(f"  {e}\n")
        out.write("\n")

    if warnings:
        out.write("─── Warnings ────────────────────────────────────\n")
        for w in warnings[:50]:  # cap at 50 for readability
            out.write(f"  {w}\n")
        if len(warnings) > 50:
            out.write(f"  ... and {len(warnings) - 50} more\n")
        out.write("\n")

    if parsed:
        drift = compute_drift_report(parsed)
        out.write("─── Drift Report ────────────────────────────────\n")
        out.write(f"  Total mechanics: {drift['mechanics_total']}\n")
        out.write("  By test_status:\n")
        for ts, count in sorted(drift["by_test_status"].items(), key=lambda x: -x[1]):
            out.write(f"    {ts}: {count}\n")
        if drift["contamination_flags"]:
            out.write("  Contamination flags:\n")
            for flag in drift["contamination_flags"]:
                for name, note in flag.items():
                    out.write(f"    {name}: {note}\n")
        if drift["missing_canon_doc"]:
            out.write("  Missing canon docs (canon_authoring_target set, canon_sources empty):\n")
            for name in drift["missing_canon_doc"]:
                out.write(f"    {name}\n")
        out.write("  GD constraint coverage:\n")
        for gd, mechs in sorted(drift["gd_constraint_coverage"].items()):
            out.write(f"    {gd}: {len(mechs)} mechanic(s)\n")
        out.write("\n")

    return out.getvalue()


# ── Main ────────────────────────────────────────────────────────────────────


def find_repo_root(start: Path) -> Path | None:
    """Walk up looking for canon/ and sim/ siblings."""
    cur = start.resolve()
    for _ in range(8):
        if (cur / "canon").is_dir() and (cur / "sim").is_dir():
            return cur
        if cur.parent == cur:
            return None
        cur = cur.parent
    return None


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--repo-root", default=None,
                   help="Path to ttrpg repo root (must contain canon/ and sim/). "
                        "Defaults to walking up from cwd.")
    p.add_argument("--strict", action="store_true",
                   help="Treat warnings as errors (exit 1 on any drift)")
    p.add_argument("--update", action="store_true",
                   help="Write drift_report back into mechanics_index.yaml")
    p.add_argument("--index-path", default=None,
                   help="Override path to mechanics_index.yaml")
    args = p.parse_args()

    # Resolve repo root
    if args.repo_root:
        repo_root = Path(args.repo_root).resolve()
    else:
        repo_root = find_repo_root(Path.cwd())
        if repo_root is None:
            print("[FATAL] Could not find repo root (no canon/ + sim/ in walk). "
                  "Use --repo-root.", file=sys.stderr)
            return 2

    # Resolve index path
    if args.index_path:
        index_path = Path(args.index_path).resolve()
    else:
        index_path = repo_root / "canon" / "mechanics_index.yaml"

    if not index_path.exists():
        print(f"[FATAL] mechanics_index.yaml not found at {index_path}", file=sys.stderr)
        return 2

    content = index_path.read_text(encoding="utf-8")

    # YAML round-trip
    parsed, yaml_errors = validate_yaml_roundtrip(content)
    if parsed is None:
        for e in yaml_errors:
            print(e, file=sys.stderr)
        return 1

    all_errors: list[ValidationError] = list(yaml_errors)

    # Top-level schema
    all_errors.extend(validate_top_level(parsed))

    # Per-mechanic
    gd_constraints = parsed.get("gd_constraints", {})
    mechanics = parsed.get("mechanics", {})
    for name, entry in mechanics.items():
        all_errors.extend(validate_mechanic(name, entry, gd_constraints))

    # Cross-references
    all_errors.extend(validate_cross_references(parsed, repo_root))

    # GD-1 singularity invariant
    all_errors.extend(validate_gd_singularity(parsed))

    # Emit report
    print(emit_report(parsed, all_errors))

    # --update: write drift_report back
    if args.update:
        drift = compute_drift_report(parsed)
        parsed["drift_report"] = drift
        new_content = yaml.safe_dump(parsed, default_flow_style=False, sort_keys=False,
                                     width=120, allow_unicode=True)
        index_path.write_text(new_content, encoding="utf-8")
        print(f"[OK] Wrote drift_report back to {index_path}", file=sys.stderr)

    # Exit code
    errors = [e for e in all_errors if e.level == "error"]
    warnings = [e for e in all_errors if e.level == "warning"]

    if errors:
        return 1
    if args.strict and warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
