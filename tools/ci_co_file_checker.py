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
design_docs = [f for f in changed
               if re.match(r'designs/.+_v30\.md$', f) and 'infill' not in f]
if design_docs and 'references/canonical_sources.yaml' not in changed:
    violations.append(
        f"DESIGN DOCS changed but canonical_sources.yaml not in commit.\n"
        f"  Changed: {design_docs}\n"
        f"  Required: references/canonical_sources.yaml (update if source authority changed)"
    )

# ── Rule 2: patch register write → propagation_map.md ────────────────────────
register_writes = [f for f in changed if f.startswith('canon/patch_register')]
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

# ── Rule 4: design doc change → params file (only for params-bearing systems) ──
# Conditional, not blanket: many design docs legitimately have NO params file, so
# the old hard requirement false-positived on every prose-only design. We now
# require the co-change only when a params file for this system actually exists in
# the repo (i.e. the system is params-bearing). If a candidate exists on disk but
# is absent from the changeset, that is the real co-file violation we want to catch.
for doc in design_docs:
    # Extract system name from path: designs/{category}/{system}_v30.md
    basename = os.path.basename(doc).replace('_v30.md', '')
    params_candidates = [
        f'params/{basename}.md',
        f'params/{basename.replace("_design","")}.md',
    ]
    existing = [p for p in params_candidates if os.path.exists(p)]
    if not existing:
        continue  # params-less system — nothing to require
    if not any(p in changed for p in existing):
        violations.append(
            f"DESIGN DOC {doc} changed but its params file not in commit.\n"
            f"  This system is params-bearing; expected one of: {existing}\n"
            f"  Include the params file if mechanical values changed."
        )

if violations:
    print(f"[CO-FILE VIOLATIONS: {len(violations)}]\n")
    for i, v in enumerate(violations, 1):
        print(f"  [{i}] {v}\n")
    sys.exit(1)
else:
    print("Co-file check: all rules satisfied.")
    sys.exit(0)
