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
import subprocess, sys, os, re

def get_changed_files():
    """
    Get changed files using GitHub event context (accurate for push, PR, squash merge).
    Falls back to HEAD~1 for local runs.
    """
    event   = os.environ.get('GITHUB_EVENT_NAME', '')
    before  = os.environ.get('GITHUB_EVENT_BEFORE', '')
    sha     = os.environ.get('GITHUB_SHA', '')
    base    = os.environ.get('GITHUB_BASE_REF', '')

    if event == 'push' and before and sha and before != '0' * 40:
        # Push event: diff from before SHA to current SHA (accurate for all push types)
        r = subprocess.run(['git', 'diff', '--name-only', before, sha],
                           capture_output=True, text=True)
        if r.returncode == 0:
            return set(r.stdout.strip().splitlines())

    if event == 'pull_request' and base:
        # PR event: all files changed in this PR branch vs base
        r = subprocess.run(['git', 'diff', '--name-only', f'origin/{base}...HEAD'],
                           capture_output=True, text=True)
        if r.returncode == 0:
            return set(r.stdout.strip().splitlines())

    # Fallback (local run or initial push): HEAD~1 or empty tree
    r = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'],
                       capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip():
        return set(r.stdout.strip().splitlines())
    r2 = subprocess.run(
        ['git', 'diff', '--name-only', '4b825dc642cb6eb9a060e54bf8d69288fbee4904', 'HEAD'],
        capture_output=True, text=True)
    return set(r2.stdout.strip().splitlines()) if r2.returncode == 0 else set()

changed = get_changed_files()
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
sim_outputs = [f for f in changed if f.startswith('tests/sim/') or f.startswith('tests/audit/')]
if sim_outputs and 'tests/coverage_matrix.md' not in changed:
    violations.append(
        f"SIMULATION OUTPUT added but coverage_matrix.md not updated.\n"
        f"  Outputs: {sim_outputs}\n"
        f"  Required: tests/coverage_matrix.md"
    )

# ── Rule 4: design doc change → params file ───────────────────────────────────
for doc in design_docs:
    # Extract system name from path: designs/{category}/{system}_v30.md
    basename = os.path.basename(doc).replace('_v30.md', '')
    params_candidates = [
        f'params/{basename}.md',
        f'params/{basename.replace("_design","")}.md',
    ]
    if not any(p in changed for p in params_candidates):
        # Hard check: SPECIFIC params file required, not just any params file
        violations.append(
            f"DESIGN DOC {doc} changed but its params file not in commit.\n"
            f"  Expected one of: {params_candidates}\n"
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
