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

    # SHARDING (--shard i/n) — for LOCAL pre-push verification, deliberately NOT for
    # collapsing the CI workflow. That collapse was attempted and abandoned on a real
    # design conflict, recorded here so nobody re-attempts it without seeing the trap:
    #
    #   `--ci` derives its work-list FROM the workflow's job bodies (ci_gate_coverage's
    #   TOOL_CMD_RE scans each job for `python tools/X.py`). Replacing the ~27 validator
    #   jobs with a few shard jobs that call THIS function deletes the very lines the
    #   function reads. Measured: a collapsed workflow yields exactly ONE parsed command —
    #   valoria_local itself. The 27 validators become invisible, and a tool that reports
    #   "all CI validators passed" over an empty set is the silently-dead-gate class
    #   (ED-IN-0103 §2.0) built on purpose.
    #
    #   The escape — move the validator list into a data file — trades a property worth
    #   more than the saving: today the list CANNOT drift, because it is the workflow. A
    #   hand-maintained roster is a second owner of "what CI runs" and would go stale on
    #   the next job added. ~27 runner setups is not worth that.
    #
    # So the collapse is REJECTED on evidence, not deferred. Sharding survives because it
    # is genuinely useful locally: `--ci --shard 1/3` verifies a third of the gate in about
    # a minute instead of running all 31 invocations sequentially.
    #
    # The split is round-robin over the workflow's own job order, which is stable because
    # ci_gate_coverage parses the file top-to-bottom. Deterministic, so a failure is always
    # reproducible with the same shard argument.
    shard_arg = None
    for i, a in enumerate(argv or []):
        if a == '--shard' and i + 1 < len(argv):
            shard_arg = argv[i + 1]
        elif a.startswith('--shard='):
            shard_arg = a.split('=', 1)[1]
    if shard_arg:
        try:
            idx, total = (int(x) for x in shard_arg.split('/'))
        except ValueError:
            print(f"[valoria --ci] bad --shard {shard_arg!r}; expected i/n", file=sys.stderr)
            return 2
        if not (1 <= idx <= total):
            print(f"[valoria --ci] --shard {idx}/{total} out of range", file=sys.stderr)
            return 2
        jobs = [j for k, j in enumerate(jobs) if k % total == (idx - 1)]
        print(f"[valoria --ci] shard {idx}/{total}: {len(jobs)} job(s)")
        if not jobs:
            # An empty shard means the split is wrong, not that everything passed.
            print(f"[valoria --ci] shard {idx}/{total} is EMPTY — refusing to report success "
                  f"on an empty run", file=sys.stderr)
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
        ('ci_pp_frozen_check.py',       [],          True),   # PP frozen vocabulary (ED-IN-0190, Jordan 2026-08-14)
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
        ('export_key_types.py',         ['--check'], True),   # key registry md -> typed-JSON round-trip (ED-IN-0136; blocking)
        # MIGRATION-WINDOW gate: retire with engine/params/ (ED-IN-0139). See evacuation_plan R-PARAMS-DUMPED.
        # ED-IN-0142: the register went stale 3x in one session and CI caught it every time,
        # because --check could not fail and this list did not run it. Both fixed.
        ('build_test_register.py',      ['--check'], True),   # params prose -> YAML capture, byte-lossless (ED-IN-0139; blocking)
        ('currency_consistency_check.py', [],        False),  # report-only recency gate (ED-1087)
        ('ci_audit_registry_check.py',   [],          False),  # report-only audit-registry freshness gate
        ('wiring_map_check.py',          ['--check'], False),  # report-only wiring-manifest tag/coverage gate (ED-IN-0074)
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
        # ED-IN-0112: the SCOPE ratchet. Wired HERE rather than as a new CI job, deliberately —
        # this repo's problem is too many jobs, not too few, and valoria_local already runs both
        # locally (pre-commit) and in CI (generation-consistency-check), so one line buys both
        # surfaces at zero job cost.
        #
        # REPORT-ONLY, AND THAT IS LOAD-BEARING. An adversarial pass found the first version of
        # this scaffolding asserting the ratchet's --check inside the BLOCKING pytest suite, at
        # zero headroom: the next PR to file an ED would have broken the build for an unrelated
        # author. Scope growth is a signal for the author to see and answer, never a reason to
        # refuse someone else's commit. If it ever becomes blocking, that is Jordan's call with
        # a loud ED-1094 call-out, not a quiet flag change.
        ('scope_ratchet.py',             ['--check'], False),  # scope ceilings + G13 activity control (ED-IN-0112)
        # ────────────────────────────────────────────────────────────────────────────────
        # THE CI-ONLY RESIDUAL, CLOSED (ED-IN-0176). Four validators sat in CI's BLOCKING
        # `validators` job and in no local list, so `valoria_local` could report "all local
        # gates passed" on a tree CI was about to red. It did exactly that on PR #307: the
        # identifier census drifted when three tools were retired, local went green, CI failed.
        #
        # THIS IS THE THIRD RECORDED INSTANCE OF ONE PATTERN, which is why it is swept rather
        # than patched. ED-IN-0142 fixed it for `build_test_register` ("the register went stale
        # 3x in one session and CI caught it every time, because --check could not fail and this
        # list did not run it"); ED-PC-0040 fixed it for `freshness_gate` ("five consecutive
        # local-green commits shipped a stale canonical_sha__ pin"). Each was fixed as an
        # incident. MEASURED here instead: 18 CI validator invocations against this list left
        # exactly these four unrun, and `tests/valoria/test_gate_coverage.py` now fails on a
        # fifth (§0.1 point 5 — the guard is the deliverable, not the wiring).
        #
        # `compliance_check.py` stays deliberately absent and is NOT part of this residual —
        # ci_checks_registry.yaml:262 records that call ("local-green != compliance-green").
        #
        # Report-only, following the freshness_gate/wf_harness precedent above: all four scan
        # the WHOLE tree rather than the changeset, so a blocking local copy would hold an
        # unrelated commit hostage to a file the author is still writing. CI remains the
        # unbypassable boundary (CLAUDE.md §8) and all four are blocking there, so nothing is
        # weakened — what changes is that local-green now SEES them. Measured cost: 4.9s total.
        ('ci_hooks_verifier.py',         [],          False),  # enforcement architecture intact (BLOCKING in CI)
        ('build_identifier_census.py',   ['--check'], False),  # census + roll-up freshness (ED-IN-0172; BLOCKING in CI)
        ('validate_ed_citations.py',     [],          False),  # anti-fabrication citation integrity (BLOCKING in CI; plan step G11)
        ('broken_dependency_checker.py', [],          False),  # ledger path refs resolve (BLOCKING in CI)
        # ED-IN-0180. Reports modules that read a registry directly when a single owner exists.
        # Report-only and it REDS ON DAY ONE by design — 14 known bypasses are the finding, not a
        # regression, and blocking on them would refuse unrelated commits for a pre-existing
        # condition (ED-IN-0112 paid for that once). The tight assertion lives in
        # tests/valoria/test_single_owner_check.py, which fails when the count GROWS.
        ('single_owner_check.py',        ['--check'], False),  # CLAUDE.md §8 "every rule lives once"
    ]

    # Force UTF-8 in child validators so their output never crashes on the
    # Windows console (cp1252) when printing design-corpus text (em-dashes, etc.).
    child_env = dict(os.environ, PYTHONUTF8='1', PYTHONIOENCODING='utf-8')

    failed = []
    # Report-only failures were previously DISCARDED, not merely unreported — the `and blocking`
    # guard threw the result away, so the summary below could not have mentioned them even if it
    # had wanted to. See the note at the summary (ED-IN-0177).
    failed_reportonly = []
    for script, extra, blocking in checks:
        path = os.path.join(HERE, script)
        if not os.path.exists(path):
            continue
        print(f"\n--- {script} ---")
        r = subprocess.run([sys.executable, path] + extra, env=child_env)
        if r.returncode != 0:
            (failed if blocking else failed_reportonly).append(script)

    print()
    if failed:
        print(f"[valoria check] FAILED: {', '.join(failed)}")
        print("Fix the above, or `git commit --no-verify` to bypass locally (CI still enforces on the PR).")
        return 1
    # A REPORT-ONLY FAILURE MUST NOT PRINT AS AN UNQUALIFIED PASS (ED-IN-0177).
    #
    # This line read "all local gates passed" whenever no BLOCKING check failed — including when
    # a report-only validator had just failed twenty lines up. That is the operator-visible half
    # of the PR #307 incident and it survived the fix that was supposed to close it: ED-IN-0176
    # wired four CI-only validators in here as report-only, which puts MORE failures in exactly
    # the class this summary was hiding. An author reads the last line, sees a green claim, pushes,
    # and CI reds on something local already knew.
    #
    # `run_ci_validators` has printed a report-only summary since it was written (:134-135); only
    # `main()` was silent. Same information, same file, two exits — one of them lying by omission.
    #
    # NOT a promotion to blocking: report-only stays non-gating, the return code is unchanged, and
    # nothing new can refuse a commit. What changes is that the last line stops asserting something
    # the run does not support.
    if failed_reportonly:
        print(f"[valoria check] blocking gates passed — but {len(failed_reportonly)} REPORT-ONLY "
              f"check(s) failed: {', '.join(failed_reportonly)}")
        print("  Not gating locally. Several ARE blocking in CI (ED-IN-0176), so read them before pushing.")
        return 0
    print("[valoria check] all local gates passed.")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
