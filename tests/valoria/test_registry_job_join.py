"""The registry->job invocation join must bite, and must never go quiet (ED-IN-0118/0119).

`references/ci_checks_registry.yaml` rows carry a `ci_job:` value. Before ED-IN-0118,
`broken_dependency_checker` asserted only that the value NAMES a job that exists — never that the
job invokes the tool. That is how `scope_ratchet.py` carried `ci_job: validators-report` through the
entire period in which no workflow invoked it: the row recorded intent, and a registry that records
intent is read as evidence of coverage.

WHY THIS FILE EXISTS AT ALL. The join shipped with no test. It was verified once, by hand, by
planting a false row — and a mutation sweep then deleted the whole branch with every test still
green. A guard nobody can observe failing is indistinguishable from one that cannot fail, which is
the defect this join was written to detect, reproduced in the fix for it. These tests are the
falsifier that was missing.
"""
import importlib.util
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TOOLS = os.path.join(ROOT, 'tools')


@pytest.fixture()
def bdc():
    if TOOLS not in sys.path:
        sys.path.insert(0, TOOLS)
    spec = importlib.util.spec_from_file_location(
        'broken_dependency_checker', os.path.join(TOOLS, 'broken_dependency_checker.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _run(mod):
    return mod.check_ci_registry_coverage(mod.get_all_repo_files())


# ───────────────────────────────────────────────────────────────────── the live tree is honest

def test_the_live_registry_passes(bdc):
    """If this fails, some row is claiming CI coverage the workflow does not provide right now."""
    violations, _ = _run(bdc)
    bad = [v for v in violations if 'ci_job' in v]
    assert not bad, f"live registry rows claim false coverage: {bad[:3]}"


# ─────────────────────────────────────────────────────── planted false claims must be rejected

def test_a_row_pointing_at_a_compiles_only_job_is_rejected(bdc, monkeypatch):
    """THE LAUNDERING PATH. Compiling a tool is not running it.

    `scope_ratchet`'s row claimed coverage via `valoria_local`, which CI only ever py_compile's —
    so aiming a row at `syntax-check` would satisfy a check that merely required the job to exist.
    """
    real = bdc._gate_jobs()
    fake = [dict(j, compiles_only=True, tool_commands=[]) if j['id'] == 'validators-report' else j
            for j in real]
    monkeypatch.setattr(bdc, '_gate_jobs', lambda: fake)
    violations, _ = _run(bdc)
    assert any('only COMPILES' in v for v in violations), \
        'a row pointing at a compile-only job was accepted as coverage'


def test_a_row_naming_a_job_that_never_invokes_it_is_rejected(bdc, monkeypatch):
    """The plain case: the job is real and runs tools, just not this one."""
    real = bdc._gate_jobs()
    fake = [dict(j, tool_commands=[{'script': 'tools/ci_naming_check.py', 'args': []}])
            if j['id'] == 'validators-report' else j for j in real]
    monkeypatch.setattr(bdc, '_gate_jobs', lambda: fake)
    violations, _ = _run(bdc)
    assert any('never invokes it' in v for v in violations)


# ─────────────────────────────────────────── and the check must never SKIP without saying so

def test_an_unparseable_job_name_is_reported_not_skipped(bdc, monkeypatch):
    """TWO PARSERS, TWO GRAMMARS. `job_ids` accepts `[a-zA-Z][\\w-]*`; ci_gate_coverage's JOB_RE
    accepts only `[a-z0-9][a-z0-9-]*`. A job named `my_job` is a real id to one and invisible to the
    other, so `job` is None — and before this branch existed the row skipped BOTH checks in silence.
    Latent today, because every job name happens to be lowercase-hyphen.
    """
    real = [j for j in bdc._gate_jobs() if j['id'] != 'validators-report']
    monkeypatch.setattr(bdc, '_gate_jobs', lambda: real)
    _, errors = _run(bdc)
    assert any('UNVERIFIED' in e for e in errors), \
        'a row whose job could not be parsed was skipped silently'


def test_an_import_failure_is_reported_not_skipped(bdc, monkeypatch):
    """The other silence: if ci_gate_coverage cannot be imported the join cannot run at all."""
    monkeypatch.setattr(bdc, '_gate_jobs', lambda: [])
    _, errors = _run(bdc)
    assert any('SKIPPED' in e for e in errors)


def test_the_skip_notice_is_emitted_once_not_per_row(bdc, monkeypatch):
    """Thirty identical lines would bury the finding they exist to surface."""
    monkeypatch.setattr(bdc, '_gate_jobs', lambda: [])
    _, errors = _run(bdc)
    assert len([e for e in errors if 'could not be imported' in e]) == 1


# ──────────────────────────────────────────────────────────── and it must not over-reject

def test_a_job_invoking_its_script_as_a_MODULE_is_not_flagged(bdc):
    """`lanchester-signature` runs `python3 -m mass_battle.lanchester_signature`, which parses to
    NO tool_commands. An earlier, broader version of this branch ("no tools/ script and no pytest
    root") flagged it — a false positive on a legitimately-covered row. Both directions matter.
    """
    violations, _ = _run(bdc)
    assert not [v for v in violations if 'lanchester' in v]


def test_a_row_claiming_a_pytest_only_job_is_rejected(bdc, monkeypatch):
    """THE SAFE HARBOR. A job with no PARSED tools/ command used to pass any row unchallenged.

    `unit-tests` runs pytest and nothing else, so `invoked` was empty and the emptiness guard let
    the row through — laundering a false claim exactly as `ci_job: syntax-check` did before the
    compiles-only branch closed that path. One job over from the defect this join was built for.
    """
    real = bdc._gate_jobs()
    fake = [dict(j, tool_commands=[], compiles_only=False, runnable='python -m pytest tests/valoria')
            if j['id'] == 'validators-report' else j for j in real]
    monkeypatch.setattr(bdc, '_gate_jobs', lambda: fake)
    violations, _ = _run(bdc)
    assert any('nor mentions it anywhere' in v for v in violations)


def test_a_module_invoked_script_is_still_accepted(bdc, monkeypatch):
    """Both directions, and this one is why the stem test exists rather than a bare emptiness
    rejection: `lanchester-signature` runs `python3 -m mass_battle.lanchester_signature`, which
    TOOL_CMD_RE cannot parse. 'No parsed commands' is not 'covers nothing'."""
    real = bdc._gate_jobs()
    fake = [dict(j, tool_commands=[], compiles_only=False,
                 runnable='PYTHONPATH=. python3 -m mass_battle.lanchester_signature || true')
            if j['id'] == 'lanchester-signature' else j for j in real]
    monkeypatch.setattr(bdc, '_gate_jobs', lambda: fake)
    violations, _ = _run(bdc)
    assert not [v for v in violations if 'lanchester' in v]
