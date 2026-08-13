"""Guard for tools/ci_gate_coverage.py (ED-IN-0098).

The tool exists because the W4 gate ran `tests/valoria` and forgot `engine/tests` (a separate
blocking job, `sim-regression`) and `tests/contracts` (also in `unit-tests`). Its one job is to
never let a pytest root that CI runs go unlisted, so that is what these tests pin — including the
count, so a root being ADDED to CI and silently missed here fails rather than passes.
"""
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import ci_gate_coverage as g  # noqa: E402

# MEASURED 2026-07-30 against .github/workflows/valoria-ci.yml. If CI gains a pytest root, this
# set must grow in the SAME commit — that is the regression this pin exists to force.
# UPDATED 2026-08-05 (ED-IN-0145), per this test's own instruction to say so in the same commit:
# `tests/contracts` EVACUATED and its CI step is removed. Two roots remain.
#
# ⚠ AND A NEAR-MISS WORTH RECORDING, because I got this right for the wrong reason first. When this
# assertion failed I dropped `tests/contracts` from the pin — but at that moment the CI STEP STILL
# EXISTED (valoria-ci.yml:298) and `ci_gate_coverage` simply could not see it: the parser takes ONE
# pytest root per job, and `unit-tests` had two. So I aligned the pin to the PARSER rather than to
# reality, which is precisely the failure this test exists to catch (the W4 gate forgot a root).
# The step is now genuinely gone, so pin and reality agree — but the parser's one-root-per-job
# blind spot is real and survives. If a job ever runs two pytest roots again, this test will pass
# while silently ignoring the second.
EXPECTED_ROOTS = {'tests/valoria', 'engine/tests'}


def test_workflow_parses_into_jobs():
    jobs = g.jobs()
    # Floor lowered 20 -> 8 on 2026-08-01: the 25 fast validator jobs collapsed into two, so the
    # workflow legitimately holds ~11 jobs. The assertion's PURPOSE is unchanged — catch "the YAML
    # shape changed and we now parse nothing" — and 8 still does that. It is deliberately not
    # pinned to the exact count: job composition is expected to change, whereas the COMMAND set is
    # the invariant that matters, and that is pinned exactly by EXPECTED_COMMANDS below.
    assert len(jobs) > 8, f'only parsed {len(jobs)} jobs — the workflow format may have changed'
    ids = {j['id'] for j in jobs}
    # `ed-citations` collapsed into `validators` on 2026-08-01. Its COMMAND is still pinned
    # exactly by EXPECTED_COMMANDS below — the job that HOSTS a validator is not the invariant,
    # the fact that CI still runs it is.
    for required in ('unit-tests', 'sim-regression', 'compliance-check', 'validators'):
        assert required in ids, f'known CI job {required!r} not parsed'


def test_every_ci_pytest_root_is_discovered():
    """THE regression: the two roots the W4 gate forgot must both be found."""
    roots = {r for j in g.jobs() for r in j['pytest_roots']}
    assert roots == EXPECTED_ROOTS, (
        f'CI pytest roots changed: found {sorted(roots)}, pinned {sorted(EXPECTED_ROOTS)}. If CI '
        f'legitimately gained or lost a root, update EXPECTED_ROOTS in this commit and say so — '
        f'do not delete the assertion.')


def test_engine_tests_is_recognised_as_blocking():
    """sim-regression has no continue-on-error, so a local gate skipping it is skipping a gate."""
    sim = next(j for j in g.jobs() if j['id'] == 'sim-regression')
    assert sim['blocking'] is True
    assert 'engine/tests' in sim['pytest_roots']


def test_continue_on_error_jobs_are_classified_non_blocking():
    """Precision: report-only jobs must not be presented as unbypassable gates."""
    jobs = g.jobs()
    advisory = [j['id'] for j in jobs if not j['blocking']]
    assert advisory, 'no advisory jobs detected — continue-on-error parsing is broken'
    # `currency-consistency` was its own continue-on-error job until the 2026-08-01 collapse;
    # it is now one of ten commands inside `validators-report`, which carries the key at JOB
    # level. Property unchanged — a report-only surface must not read as an unbypassable gate.
    assert 'validators-report' in advisory


def test_every_discovered_root_actually_exists_on_disk():
    """A root parsed out of YAML but absent from the tree would send a session chasing nothing."""
    checked = 0
    for r in {r for j in g.jobs() for r in j['pytest_roots']}:
        assert os.path.isdir(os.path.join(ROOT, r)) or os.path.isfile(os.path.join(ROOT, r)), r
        checked += 1
    assert checked == len(EXPECTED_ROOTS) == 2, f'checked {checked} roots'


def test_base_distance_reports_an_integer_or_none():
    d = g.base_distance('origin/main')
    assert d is None or (isinstance(d[0], int) and d[0] >= 0)
    # An unknown ref must degrade to None, not crash a pre-commit advisory.
    assert g.base_distance('definitely/not/a/ref') is None


def test_tool_is_report_only():
    assert g.main(['--base', 'HEAD']) == 0


# ── Command preservation across the 2026-08-01 job collapse ──────────────────
#
# 25 validator jobs were merged into two (`validators` blocking, `validators-report`
# non-blocking) because 29 of 31 validator nodes did 5.17s of compute in total while
# paying 25 runner boots. The ENTIRE safety argument for that is this: `valoria_local
# --ci` derives what it runs from `jobs()`, which regex-scans each job BODY, so as long
# as every `python3 tools/<name>.py` line survives verbatim, the work-list still IS the
# workflow and cannot drift. A roster in a data file would have broken exactly that,
# which is why it was rejected.
#
# So the collapse is only safe while the command SET is unchanged. This pins it.
# MEASURED before and after the collapse: 31 distinct (script, args), 0 lost, 0 gained.
EXPECTED_COMMANDS = {
    ('tools/broken_dependency_checker.py', ''),
    ('tools/canon_coverage_check.py', '--strict --json'),
    ('tools/ci_audit_registry_check.py', ''),
    ('tools/ci_claim_provenance_check.py', ''),
    ('tools/ci_claude_workflow_paths.py', ''),
    ('tools/ci_co_file_checker.py', ''),
    ('tools/ci_editorial_checker.py', ''),
    ('tools/ci_generation_consistency.py', ''),
    ('tools/ci_golden_modes_check.py', ''),
    ('tools/ci_hooks_verifier.py', ''),
    ('tools/ci_module_shape_check.py', ''),
    ('tools/ci_names_check.py', ''),
    ('tools/ci_names_consistency.py', ''),
    ('tools/ci_naming_check.py', ''),
    ('tools/ci_program_claim_check.py', ''),        # wired 2026-08-01 (ED-IN-0118)
    ('tools/ci_quantity_vocabulary_check.py', ''),
    ('tools/ci_register_size_check.py', ''),
    ('tools/ci_sim_fabrication_check.py', ''),
    ('tools/ci_supersession_check.py', ''),
    ('tools/ci_vacuous_assertion_check.py', ''),    # wired 2026-08-01 (ED-IN-0118)
    ('tools/scope_ratchet.py', '--check'),          # wired 2026-08-01 (ED-IN-0118)
    ('tools/ci_vetting_check.py', ''),
    ('tools/ci_wf_harness_check.py', ''),
    ('tools/ci_workplan_pointer_check.py', ''),
    ('tools/compliance_check.py', '--check-only --repo-state .'),
    ('tools/currency_consistency_check.py', ''),
    ('tools/export_engine_params.py', '--check'),
    ('tools/export_key_types.py', '--check'),      # ED-IN-0136: key registry md -> typed JSON round-trip
    ('tools/build_test_register.py', '--check'),
    ('tools/build_identifier_census.py', '--check'),   # ED-IN-0172: moved out of pytest (racy whole-tree read under -n auto)   # ED-IN-0142: drift gate, now able to fail
    ('tools/freshness_gate.py', ''),
    ('tools/mechanics_index_gen.py', '--strict'),
    ('tools/review_core.py', '--check'),
    ('tools/validate_ed_citations.py', ''),
    ('tools/wiring_map_check.py', '--check'),
}


def _live_commands():
    return {(c['script'], ' '.join(c['args'])) for j in g.jobs() for c in j['tool_commands']}


def test_no_validator_was_dropped_by_the_collapse():
    """A validator silently vanishing from CI is the whole risk of merging jobs."""
    live = _live_commands()
    assert live, 'jobs() returned no tool commands at all — the parser or workflow is broken'
    missing = sorted(EXPECTED_COMMANDS - live)
    assert not missing, (
        f'{len(missing)} CI validator invocation(s) disappeared from the workflow:\n  ' +
        '\n  '.join(f'{s} {a}'.strip() for s, a in missing) +
        '\n\nIf a validator was deliberately retired, remove it from EXPECTED_COMMANDS in the '
        'SAME commit and say why. Silence here means CI stopped running it.')


def test_no_phantom_command_was_introduced():
    """The other direction, and it caught a real bug during the collapse.

    Writing the report-only step as `echo "::group::python3 tools/X.py"; python3 tools/X.py`
    made the parser capture the CLOSING QUOTE into the args, yielding 10 phantom commands like
    `python3 tools/ci_names_check.py "`. `--ci` would then have tried to execute them. Caught
    by diffing the command set before/after rather than by reading the YAML.
    """
    extra = sorted(_live_commands() - EXPECTED_COMMANDS)
    assert not extra, (
        f'{len(extra)} unexpected CI command(s):\n  ' +
        '\n  '.join(f'{s} {a!r}'.strip() for s, a in extra) +
        '\n\nA new validator is fine — add it here. An entry with a stray quote or shell '
        'fragment in its args means the workflow line is not parseable as written.')


def test_the_two_collapsed_jobs_keep_their_blocking_tiers_apart():
    """Mixing tiers in one job would silently downgrade every blocking validator.

    `jobs()` computes `blocking` as `'continue-on-error' not in body` over the WHOLE job
    body. Put report-only validators (which carry that key) in the same job as blocking
    ones and the entire job reads non-blocking, so `valoria_local --ci` reclassifies real
    failures as report-only and exits 0 — the silently-dead-gate class the collapse was
    designed to avoid. Two jobs is not a style choice; it is the mechanism.
    """
    by_id = {j['id']: j for j in g.jobs()}
    for jid, want in (('validators', True), ('validators-report', False)):
        assert jid in by_id, f'{jid} job is gone — the collapse was undone or renamed'
        assert by_id[jid]['blocking'] is want, (
            f'{jid}.blocking is {by_id[jid]["blocking"]}, expected {want}. If a '
            f'continue-on-error step was added to the blocking job, every validator in it '
            f'just stopped gating.')
        assert by_id[jid]['tool_commands'], f'{jid} runs no validators at all'
    assert by_id['validators']['compiles_only'] is False, (
        'the blocking validator job now contains py_compile, which makes jobs() return ZERO '
        'commands for it — --ci would run nothing and report success over an empty set')


# ───────────────────────────────────────── the parser must not read PROSE as configuration

def test_a_comment_mentioning_py_compile_does_not_zero_a_jobs_command_list(tmp_path, monkeypatch):
    """REGRESSION (ED-IN-0118). `compiles_only` was computed from the RAW job body, so a job whose
    COMMENT merely mentioned py_compile was classified compile-only and had its ENTIRE command list
    discarded.

    It was not hypothetical: adding three validators to validators-report, with a comment
    explaining that valoria_local is only py_compile'd, took that job from 10 parsed commands to 0.
    `valoria_local --ci` would then have silently stopped running ten validators and reported
    success. The command matcher already stripped comments for exactly this reason; the two
    derivations have to read the same text or they disagree.
    """
    wf = tmp_path / 'valoria-ci.yml'
    wf.write_text(
        "on:\n  push:\n\njobs:\n"
        "  demo:\n"
        "    steps:\n"
        "      - run: |\n"
        "          # note: valoria_local is only reached via py_compile, never executed\n"
        "          python3 tools/ci_naming_check.py\n",
        encoding='utf-8')
    monkeypatch.setattr(g, 'WORKFLOW', str(wf))
    demo = [j for j in g.jobs() if j['id'] == 'demo']
    assert demo, 'the fixture job did not parse'
    assert demo[0]['compiles_only'] is False, \
        'a comment mentioning py_compile classified the job as compile-only'
    assert [c['script'] for c in demo[0]['tool_commands']] == ['tools/ci_naming_check.py']


def test_a_real_py_compile_job_is_still_classified_compile_only(tmp_path, monkeypatch):
    """The other direction — the fix must not disable the classification it repairs."""
    wf = tmp_path / 'valoria-ci.yml'
    wf.write_text(
        "on:\n  push:\n\njobs:\n"
        "  syntax:\n"
        "    steps:\n"
        "      - run: |\n"
        "          python3 -m py_compile tools/ci_naming_check.py\n",
        encoding='utf-8')
    monkeypatch.setattr(g, 'WORKFLOW', str(wf))
    syn = [j for j in g.jobs() if j['id'] == 'syntax']
    assert syn and syn[0]['compiles_only'] is True
    assert syn[0]['tool_commands'] == []


def test_the_live_validators_report_job_still_carries_its_commands():
    """Pins the live tree against the failure above, not just a fixture."""
    rep = [j for j in g.jobs() if j['id'] == 'validators-report']
    assert rep, 'validators-report did not parse'
    # floor 13 -> 12 on 2026-08-05 (ED-IN-0145): ci_formula_prose_check RETIRED with its subject —
    # both its census input and its whole live-scan surface (engine/params) evacuated, so it was a
    # report-only gate printing "no drift" over nothing. Purpose unchanged: catch the parser
    # silently discovering nothing.
    assert len(rep[0]['tool_commands']) >= 12, (
        f"validators-report parsed only {len(rep[0]['tool_commands'])} command(s) — its report-only "
        f"validators have stopped being discovered by --ci")
