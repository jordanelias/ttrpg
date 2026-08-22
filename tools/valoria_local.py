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
    """RETIRED 2026-08-21 (culling wave 3, ED-IN-0194). `--ci` no longer exists.

    This mode derived its work-list from `tools/ci_gate_coverage.py`, which parsed
    `.github/workflows/valoria-ci.yml` and was the single owner of "what CI runs". Both are
    retired: their subject was this repository's gate wiring, which §0.1 pt 5 excludes.

    CI now runs its validators directly from the workflow, which is where they were always
    actually invoked; this mode existed to MIRROR that list locally, and a mirror of a list is
    the duplication §8 forbids. `--staged` and `--local` are unaffected and are what the
    pre-commit hook uses.
    """
    print('[valoria] --ci was retired 2026-08-21 (culling wave 3). Use --staged or --local; '
          'CI runs its validators directly from .github/workflows/valoria-ci.yml.')
    return 2


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
        ('ci_generation_consistency.py', [],         False),  # warn-only v40 currency gate
        ('ci_module_shape_check.py',    [],          False),  # report-only container/shape hygiene (ED-1085)
        ('export_engine_params.py',     ['--check'], True),   # oracle -> typed-JSON round-trip (ED-1052; blocking)
        ('export_key_types.py',         ['--check'], True),   # key registry md -> typed-JSON round-trip (ED-IN-0136; blocking)
        ('export_game_constants.py',    ['--check'], True),   # oracle -> Godot-facing constants round-trip (blocking)
        ('export_descriptors.py',       ['--check'], True),   # descriptor registry -> the artifact the engine reads at runtime (blocking)
        ('export_composition.py',       ['--check'], True),   # composition roles -> the map mc_v18 resolves through (blocking)
        # MIGRATION-WINDOW gate: retire with engine/params/ (ED-IN-0139). See evacuation_plan R-PARAMS-DUMPED.
        # ED-IN-0142: the register went stale 3x in one session and CI caught it every time,
        # because --check could not fail and this list did not run it. Both fixed.
        ('currency_consistency_check.py', [],        False),  # report-only recency gate (ED-1087)
        ('wiring_map_check.py',          ['--check'], False),  # report-only wiring-manifest tag/coverage gate (ED-IN-0074)
        ('ci_claim_provenance_check.py', [mode_flag], True),   # a MEASURED ledger claim must name a re-runnable instrument (ED-PC-0040; blocking)
        # RETIRED culling wave 2/3 (ED-IN-0194, 2026-08-21). Two rationale blocks stood here and
        # both argued the posture of gates that no longer exist: `ci_wf_harness_check` /
        # `ci_claude_workflow_paths` (report-only here, blocking in CI, guarding the `.claude/wf_*.js`
        # prelude copied from `tools/wf_harness.js`), and `ci_workplan_pointer_check` (ED-IN-0103,
        # the workplans pointer convention). Subject and guard went together.
        #
        # ONE THING IN THEM IS STILL TRUE AND IS KEPT: ED-IN-0103 measured plan LIVENESS to be
        # un-inferable — a `## Status:` heading is a signal in neither direction — so nothing here
        # ever checked "every live plan has a pointer", and deleting the guard does not answer that
        # question. It remains open, and it is the reason the pointer files were retired rather
        # than repaired.
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
        # exactly these four unrun. ⚠ THE RECURRENCE GUARD IS GONE: this read "and
        # `tests/valoria/test_gate_coverage.py` now fails on a fifth", and that test was retired
        # 2026-08-21 (ED-IN-0194). A pattern with THREE recorded instances now has no guard, and
        # nothing detects a fifth CI-only validator. Recorded rather than dropped silently; the
        # mitigation is the note in valoria-ci.yml — add a validator to BOTH lists in one commit.
        #
        # `compliance_check.py` stays deliberately absent and is NOT part of this residual —
        # ci_checks_registry.yaml:262 records that call ("local-green != compliance-green").
        #
        # Report-only, following the freshness_gate/wf_harness precedent above: all four scan
        # the WHOLE tree rather than the changeset, so a blocking local copy would hold an
        # unrelated commit hostage to a file the author is still writing. CI remains the
        # unbypassable boundary (CLAUDE.md §8) and all four are blocking there, so nothing is
        # weakened — what changes is that local-green now SEES them. Measured cost: 4.9s total.
        ('build_identifier_census.py',   ['--check'], False),  # census + roll-up freshness (ED-IN-0172; BLOCKING in CI)
        ('validate_ed_citations.py',     [],          False),  # anti-fabrication citation integrity (BLOCKING in CI; plan step G11)
        ('broken_dependency_checker.py', [],          False),  # ledger path refs resolve (BLOCKING in CI)
        # ED-IN-0180. Reports modules that read a registry directly when a single owner exists.
        # Report-only and it REDS ON DAY ONE by design — 14 known bypasses are the finding, not a
        # regression, and blocking on them would refuse unrelated commits for a pre-existing
        # condition (ED-IN-0112 paid for that once). The tight assertion lives in
        # tests/valoria/test_single_owner_check.py — RETIRED 2026-08-21 with single_owner_check.py
        # itself (ED-IN-0194), so the count-GROWS check is gone too.
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
