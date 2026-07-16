#!/usr/bin/env python3
"""
ci_editorial_checker.py
Runs in CI. Checks that commits to editorial-governed paths contain
[EDITORIAL] or [PROVISIONAL] markers for substantive content.

Editorial paths: designs/npcs/, designs/world/,
                 arcs/gm_ref/, canon/03_ (timeline)

Short stubs (< 200 chars) are exempt.
Mechanical-only content (tables, formulas) is NOT exempt — the rule is path-based.
"""
import subprocess, sys, os, re

# Shared diff oracle — one definition of "what changed" (was previously copy-pasted
# byte-for-byte into this file and ci_co_file_checker.py).
try:
    import ci_common
except ImportError:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import ci_common

EDITORIAL_PATHS = (
    'designs/npcs/',
    'designs/world/',
    'arcs/gm_ref/',
    'canon/03_',
)
MARKERS = ('[EDITORIAL:', '[PROVISIONAL:', '[EDITORIAL GATE]')
MIN_LEN  = 200  # below this = stub, exempt
SKELETON_EXEMPT = '_skeleton.md'  # auto-generated, exempt from editorial markers

_mode = 'staged' if '--staged' in sys.argv else ('local' if '--local' in sys.argv else 'ci')
changed = ci_common.get_changed_files(_mode)
violations = []

# Check deleted editorial files — deletion also requires a marker in the commit message
# (can't check deleted file content, so check git log message instead)
deleted = {p for p in ci_common.get_changed_files_filtered(_mode, diff_filter='D')
           if any(p.startswith(ep) for ep in EDITORIAL_PATHS)}

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
