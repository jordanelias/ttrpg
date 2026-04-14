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

for path in sorted(changed):
    if not any(path.startswith(p) for p in EDITORIAL_PATHS):
        continue
    if not os.path.exists(path):
        continue  # deleted file
    with open(path, encoding='utf-8', errors='replace') as f:
        content = f.read()
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
