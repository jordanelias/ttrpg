#!/usr/bin/env python3
"""
valoria_local.py — run the SAME tools/ci_*.py validators CI runs, against the
local changeset, for fast pre-commit feedback.

ONE VALIDATOR, MANY CALLERS: this orchestrator shells the authoritative
validators; it never re-implements a rule. The git pre-commit hook
(.githooks/pre-commit) calls this with --staged; you can also run it by hand.

Modes:
  --staged  (default) — the git index: what `git commit` is about to record.
  --local             — HEAD~1..HEAD.

Exit 0 if all BLOCKING validators pass; 1 otherwise. Supersession is warn-only.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main(argv):
    mode_flag = '--local' if '--local' in argv else '--staged'

    # (script, extra_args, blocking)
    checks = [
        ('ci_naming_check.py',          [mode_flag], True),
        ('ci_co_file_checker.py',       [mode_flag], True),
        ('ci_editorial_checker.py',     [mode_flag], True),
        ('ci_register_size_check.py',   [],          True),
        ('ci_vetting_check.py',         [],          True),
        ('ci_sim_fabrication_check.py', [mode_flag], True),
        ('ci_supersession_check.py',    [mode_flag], False),  # warn-only churn guard
    ]

    # Force UTF-8 in child validators so their output never crashes on the
    # Windows console (cp1252) when printing design-corpus text (em-dashes, etc.).
    child_env = dict(os.environ, PYTHONUTF8='1', PYTHONIOENCODING='utf-8')

    failed = []
    for script, extra, blocking in checks:
        path = os.path.join(HERE, script)
        if not os.path.exists(path):
            continue
        print(f"\n--- {script} ---")
        r = subprocess.run([sys.executable, path] + extra, env=child_env)
        if r.returncode != 0 and blocking:
            failed.append(script)

    print()
    if failed:
        print(f"[valoria check] FAILED: {', '.join(failed)}")
        print("Fix the above, or `git commit --no-verify` to bypass locally (CI still enforces on the PR).")
        return 1
    print("[valoria check] all local gates passed.")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
