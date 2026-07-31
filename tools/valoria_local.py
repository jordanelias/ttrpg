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


def run_ci_validators(argv=None):
    """--ci: run EVERY validator CI runs, in one process, and report a table.

    WHY (ED-IN-0112). The workflow spends ~28 separate GitHub jobs to run validators that
    each take about two seconds. Every one of those jobs pays a full runner setup —
    checkout + setup-python + pip — so the wall clock is dominated by boot cost, not by
    checking. Collapsing them into one job pays setup once.

    THE PROPERTY THIS MUST NOT LOSE. valoria-ci.yml's header states the current design's
    rationale: "every gate is its own job that depends only on syntax-check, so a hiccup
    in one gate can never silently skip another." That is a real guarantee and it is
    preserved here by construction: this runner NEVER fails fast. Every validator runs,
    every result is recorded, and the exit code is decided at the end. A collapsed job
    that stopped at the first failure WOULD lose the property — this one does not.

    THE LIST IS NOT MAINTAINED HERE. It is derived from the workflow itself via
    ci_gate_coverage.jobs(), the single owner of workflow parsing. A hand-copied list
    would be a second owner of "what CI runs" and would drift the moment a job changed —
    the §8 violation this repo keeps rediscovering.
    """
    sys.path.insert(0, HERE)
    import ci_gate_coverage  # single owner of workflow parsing

    jobs = [j for j in ci_gate_coverage.jobs() if j['tool_commands']]
    if not jobs:
        print("[valoria --ci] no validator jobs parsed from the workflow — refusing to "
              "report success on an empty run", file=sys.stderr)
        return 2

    child_env = dict(os.environ, PYTHONUTF8='1', PYTHONIOENCODING='utf-8')
    results = []
    for job in jobs:
        for cmd in job['tool_commands']:
            path = os.path.join(os.path.dirname(HERE), cmd['script'])
            if not os.path.exists(path):
                results.append((job, cmd, None))
                continue
            print(f"\n--- {job['id']}: {cmd['script']} {' '.join(cmd['args'])} ---", flush=True)
            r = subprocess.run([sys.executable, path] + cmd['args'],
                               env=child_env, cwd=os.path.dirname(HERE))
            results.append((job, cmd, r.returncode))

    print("\n" + "=" * 72)
    print(f"  {'job':30s} {'validator':34s} result")
    print("  " + "-" * 30 + " " + "-" * 34 + " ------")
    failed_blocking, failed_reportonly, missing = [], [], []
    for job, cmd, rc in results:
        tool = cmd['script'].replace('tools/', '')
        if rc is None:
            state, missing = 'MISSING', missing + [tool]
        elif rc == 0:
            state = 'pass'
        elif job['blocking']:
            state, failed_blocking = 'FAIL', failed_blocking + [f"{job['id']}:{tool}"]
        else:
            state, failed_reportonly = 'fail(report-only)', failed_reportonly + [tool]
        print(f"  {job['id']:30s} {tool:34s} {state}")

    print("=" * 72)
    print(f"  {len(results)} validator invocation(s) across {len(jobs)} job(s); "
          f"{len(failed_blocking)} blocking failure(s)")
    if missing:
        # A missing tool is NOT a pass. Reported separately so it can never be read as one.
        print(f"  MISSING (not run, not passed): {', '.join(missing)}")
    if failed_reportonly:
        print(f"  report-only failures (do not gate): {', '.join(failed_reportonly)}")
    if failed_blocking:
        print(f"\n[valoria --ci] FAILED: {', '.join(failed_blocking)}")
        return 1
    if missing:
        print("\n[valoria --ci] INCOMPLETE — a declared validator was absent.")
        return 1
    print("\n[valoria --ci] all CI validators passed.")
    return 0


def main(argv):
    if '--ci' in argv:
        return run_ci_validators(argv)

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
        # ED-IN-0087: the .claude/wf_*.js run-discipline prelude has one owner (tools/wf_harness.js)
        # and is COPIED into each script, because workflow scripts run in a sandbox with no imports.
        # A copied rule rots, so this is the guard. Blocking: an out-of-date copy is not a style
        # nit — it silently changes what a 40-agent audit does, and `--fix` makes it a one-liner.
        # REPORT-ONLY LOCALLY, BLOCKING IN CI (ED-IN-0088). Both were blocking here for about an hour
        # and that was the wrong call: neither guards a canon invariant, both scan the WHOLE .claude/
        # tree rather than the changeset, and a half-edited workflow script would therefore block an
        # unrelated commit. CI is the unbypassable boundary (CLAUDE.md §8) and still fails on either,
        # so nothing is weakened — what changes is that a local commit is never held hostage by a
        # file the author is still writing. Same posture as freshness_gate below.
        ('ci_wf_harness_check.py',       [mode_flag], False),  # workflow harness present/current/wired (ED-IN-0087; report-only here, BLOCKING in CI)
        ('ci_claude_workflow_paths.py',  [],          False),  # every .claude/ path reference resolves (ED-IN-0085; report-only here, BLOCKING in CI)
        # ED-IN-0103: the workplans pointer convention (Jordan, 2026-07-29 — every plan is reachable
        # from workplans/). Guards the DETERMINISTIC half only: fields present, lane real, no duplicate
        # targets, every target resolves on disk. It deliberately does NOT check "every live plan has a
        # pointer" — liveness was measured un-inferable, so a guessing guard would be wrong in both
        # directions. Report-only on the names-drift graduation lane while the convention beds in.
        ('ci_workplan_pointer_check.py', [],          False),  # workplans pointer integrity (ED-IN-0103; report-only)
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
