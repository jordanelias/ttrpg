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
        ('ci_names_consistency.py',     [],          True),   # index <-> registry mirrors agree
        ('ci_names_check.py',           [mode_flag], False),  # report-only naming-drift lint
        ('ci_co_file_checker.py',       [mode_flag], True),
        ('ci_editorial_checker.py',     [mode_flag], True),
        ('ci_register_size_check.py',   [],          True),
        ('ci_vetting_check.py',         [],          True),
        ('ci_sim_fabrication_check.py', [mode_flag], True),
        ('ci_supersession_check.py',    [mode_flag], False),  # warn-only churn guard
        ('ci_generation_consistency.py', [],         False),  # warn-only v40 currency gate
        ('ci_module_shape_check.py',    [],          False),  # report-only container/shape hygiene (ED-1085)
        ('export_engine_params.py',     ['--check'], True),   # oracle -> typed-JSON round-trip (ED-1052; blocking)
        ('currency_consistency_check.py', [],        False),  # report-only recency gate (ED-1087)
        ('ci_audit_registry_check.py',   [],          False),  # report-only audit-registry freshness gate
        ('wiring_map_check.py',          ['--check'], False),  # report-only wiring-manifest tag/coverage gate (ED-IN-0074)
        ('ci_formula_prose_check.py',    [],          False),  # A18 report-only formula prose-drift (ED-1052 / OPT-AV-5)
        ('ci_claim_provenance_check.py', [mode_flag], True),   # a MEASURED ledger claim must name a re-runnable instrument (ED-PC-0040; blocking)
        # ED-IN-0086: the .claude/wf_*.js run-discipline prelude has one owner (tools/wf_harness.js)
        # and is COPIED into each script, because workflow scripts run in a sandbox with no imports.
        # A copied rule rots, so this is the guard. Blocking: an out-of-date copy is not a style
        # nit — it silently changes what a 40-agent audit does, and `--fix` makes it a one-liner.
        ('ci_wf_harness_check.py',       [mode_flag], True),   # workflow harness present/current/wired (ED-IN-0086; blocking)
        ('ci_claude_workflow_paths.py',  [],          True),   # every .claude/ path reference resolves (ED-IN-0085; blocking)
        # ED-PC-0040: freshness was CI-only, so five consecutive local-green commits shipped a stale
        # canonical_sha__ pin (ED-PC-0035 edited references/module_contracts.yaml without refreshing it) and it
        # only surfaced when a PR finally ran the integrity job. Report-only here — CI stays the blocking
        # boundary — but local-green now at least SEES it. Refresh with `python3 tools/freshness_gate.py --update`.
        ('freshness_gate.py',            [],          False),  # report-only canonical-SHA staleness (blocking in CI's integrity job)
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
