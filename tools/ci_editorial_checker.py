#!/usr/bin/env python3
"""
ci_editorial_checker.py
Runs in CI. Checks that commits to editorial-governed paths contain
[EDITORIAL] or [PROVISIONAL] markers for substantive content.

Editorial paths: designs/npcs/, designs/worldbuilding/, designs/setting/,
                 gm_ref/, canon/03_ (timeline)

Short stubs (< 200 chars) are exempt.
Mechanical-only content (tables, formulas) is NOT exempt — the rule is path-based.
"""
import subprocess, sys, os, re

EDITORIAL_PATHS = (
    'designs/npcs/',
    'designs/worldbuilding/',
    'designs/setting/',
    'gm_ref/',
    'canon/03_',
)
MARKERS = ('[EDITORIAL:', '[PROVISIONAL:', '[EDITORIAL GATE]')
MIN_LEN  = 200  # below this = stub, exempt

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
violations = []

# Check deleted editorial files — deletion also requires a marker in the commit message
# (can't check deleted file content, so check git log message instead)
deleted = set()
r_del = subprocess.run(['git', 'diff', '--name-only', '--diff-filter=D',
                         os.environ.get('GITHUB_EVENT_BEFORE', 'HEAD~1'),
                         os.environ.get('GITHUB_SHA', 'HEAD')],
                        capture_output=True, text=True)
if r_del.returncode == 0:
    for path in r_del.stdout.strip().splitlines():
        if any(path.startswith(p) for p in EDITORIAL_PATHS):
            deleted.add(path)

if deleted:
    # Get commit message to check for [EDITORIAL] marker
    r_msg = subprocess.run(['git', 'log', '-1', '--pretty=%B'],
                            capture_output=True, text=True)
    commit_msg = r_msg.stdout if r_msg.returncode == 0 else ''
    for path in sorted(deleted):
        if not any(m in commit_msg for m in MARKERS):
            violations.append(path + ' (DELETED — commit message needs [EDITORIAL] marker)')
            print(f"FAIL {path}: deleted from editorial path without [EDITORIAL] in commit message")
        else:
            print(f"OK   {path}: deleted, [EDITORIAL] in commit message")

for path in sorted(changed):
    if not any(path.startswith(p) for p in EDITORIAL_PATHS):
        continue
    if not os.path.exists(path):
        continue  # deleted (already handled above)
    with open(path, encoding='utf-8', errors='strict') as f:
        try:
            content = f.read()
        except UnicodeDecodeError:
            violations.append(f"{path}: encoding error — cannot verify editorial markers")
            print(f"FAIL {path}: UnicodeDecodeError")
            continue
    if len(content) < MIN_LEN:
        print(f"SKIP {path}: stub (<{MIN_LEN} chars)")
        continue
    has_marker = any(m in content for m in MARKERS)
    if has_marker:
        print(f"OK   {path}: editorial marker present")
    else:
        violations.append(path)
        print(f"FAIL {path}: editorial path, no [EDITORIAL] or [PROVISIONAL] marker")

if violations:
    print(f"\n[EDITORIAL VIOLATIONS: {len(violations)}]")
    for v in violations:
        print(f"  {v}")
    print("\n  User retains exclusive authority over: setting, worldbuilding, characters,")
    print("  narrative, faction behaviour, ambiguous design intent.")
    print("  Add [EDITORIAL: ED-NNN — description] flags before committing.")
    sys.exit(1)
else:
    print("\nEditorial check: all governed files properly flagged.")
    sys.exit(0)
