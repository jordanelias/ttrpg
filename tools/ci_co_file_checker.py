#!/usr/bin/env python3
"""
ci_co_file_checker.py
Runs in CI. Checks that commits satisfy co-file requirements:
- Design doc change → canonical_sources.yaml must change (or be unchanged and already correct)
- Patch content → patch_register_active.yaml must change
- Simulation output → coverage_matrix.md must change
- Mechanical value change → corresponding params file must change

Uses git diff to get changed files. Exits 1 on violation.
"""
import sys, os, re

# Shared diff oracle — one definition of "what changed", used by CI, the
# pre-commit hook, and the tests. (Was previously copy-pasted into this file
# and ci_editorial_checker.py byte-for-byte.)
try:
    import ci_common
except ImportError:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ci_common

_mode = 'staged' if '--staged' in sys.argv else ('local' if '--local' in sys.argv else 'ci')
changed = ci_common.get_changed_files(_mode)
if not changed:
    print("No changed files detected. Skipping co-file check.")
    sys.exit(0)

print(f"Changed files ({len(changed)}):")
for f in sorted(changed):
    print(f"  {f}")
print()

violations = []

# ── Rule 1: design doc change → canonical_sources.yaml ───────────────────────
# A pure rename (git mv with no content edit) appears in `changed` at its new path
# but has NO added lines in the diff — the co-file rules are about *content* changes
# (mechanical values → params; source authority → canonical_sources), so a path-only
# move must not trip them. Load-bearing for the ED-IN-0071 P4 reorg, which relocates
# params-bearing _v30 docs wholesale as renames. A rename that ALSO edits content still
# has added lines, so it stays governed.
_added = ci_common.get_added_lines(_mode)
design_docs = [f for f in changed
               if re.match(r'(?:designs|systems)/.+_v30\.md$', f) and 'infill' not in f
               and f in _added]
if design_docs and 'references/canonical_sources.yaml' not in changed:
    violations.append(
        f"DESIGN DOCS changed but canonical_sources.yaml not in commit.\n"
        f"  Changed: {design_docs}\n"
        f"  Required: references/canonical_sources.yaml (update if source authority changed)"
    )

# ── Rule 2: patch register write → propagation_map.md ────────────────────────
register_writes = [f for f in changed if f.startswith('registers/patch_register')]
if register_writes and 'references/propagation_map.md' not in changed:
    violations.append(
        f"PATCH REGISTER changed but propagation_map.md not in commit.\n"
        f"  Changed: {register_writes}\n"
        f"  Required: references/propagation_map.md"
    )

# ── Rule 3: sim output → coverage_matrix.md ──────────────────────────────────
# README.md is directory-level housekeeping, not a sim run output — exclude it so
# adding/updating a folder README doesn't false-positive this rule.
# tests/audit/ was retired 2026-07-18 (audit corpus relocated to audit/lane-*/,
# organized by lane rather than treated as sim output) — no replacement clause needed.
sim_outputs = [
    f for f in changed
    if f.startswith('tests/sim/')
    and os.path.basename(f) != 'README.md'
]
if sim_outputs and 'tests/coverage_matrix.md' not in changed:
    violations.append(
        f"SIMULATION OUTPUT added but coverage_matrix.md not updated.\n"
        f"  Outputs: {sim_outputs}\n"
        f"  Required: tests/coverage_matrix.md"
    )

# ── Rule 4: RETIRED 2026-08-12 (plan step G2, ED-IN-0159 §1.6) ────────────────
#
# It required a design-doc change to co-change `engine/params/{system}.md`. That
# TREE WAS EVACUATED on 2026-08-05 (ED-IN-0145) to fork ref c451bcb, so both of
# the candidate paths it built are unconditionally absent, `existing` is
# unconditionally empty, and every candidate hit the `continue`. The rule has
# EXAMINED ZERO ITEMS since — a blocking gate reporting clean over nothing, which
# is §1.6's whole pattern.
#
# WHY IT IS SAFE TO REMOVE, stated accurately (CORRECTED after an adversarial
# pass, ED-IN-0164). The first version of this note said six --check gates "now
# carry" Rule 4's mechanism and were "strictly stronger". Both halves overreached
# and the correction matters, because a tombstone that misstates why a gate was
# removed is how a removal gets re-litigated from the wrong premise:
#
#   · Those six run CODE -> GENERATED ARTIFACT (export_engine_params --check,
#     export_key_types --check, export_sim_params, build_engine_atlas --check,
#     build_test_register, build_contract_index). Rule 4 ran DESIGN DOC -> PARAMS
#     PROSE. Different mechanism, not a stronger form of the same one.
#   · All six PRE-EXISTED this retirement. Nothing was transferred.
#
# The accurate reason is simpler and sufficient: **Rule 4's SUBJECT LEFT THE TREE.**
# There is no `engine/params/` file for any design doc to co-change, so the rule
# cannot fire for any commit. Separately — and as reassurance rather than as
# justification — the corpus retains strong code-to-artifact freshness gating
# through the six above, each of which byte-compares a committed artifact against a
# fresh build.
#
# Rules 1-3 above are untouched and still blocking, and
# `tests/valoria/test_co_file_rules.py` now asserts that each of them can still
# FAIL — not merely still run. That test did not exist when Rule 4 was removed,
# which was itself a violation of the plan's rule that every blocking-gate
# migration ships its own expected-delta test.


if violations:
    print(f"[CO-FILE VIOLATIONS: {len(violations)}]\n")
    for i, v in enumerate(violations, 1):
        print(f"  [{i}] {v}\n")
    sys.exit(1)
else:
    print("Co-file check: all rules satisfied.")
    sys.exit(0)
