"""Falsifier tests for engine/substrate/stubwire.py — the P1 stub-wire primitive (ED-IN-0091,
`audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md` §2.1).

Three claims, one fixture, one mutation (§0.1 point 3 "name the falsifier"):
  1. `stub_resolve` bumps the module-level `invocations` counter — the telemetry
     `engine/mc_v18.py`'s `CampaignResult.stub_hits` folds the same way as the existing F7
     `npcs_generated` counter.
  2. `structure_audit.py`'s `stub_wired` node attribute (derived from the SAME AST import pass
     `build_g_code` already runs — no second parser) sees a module that imports
     `engine.substrate.stubwire`.
  3. `tools/review_core.py`'s `stubs.count` report-only signal — via the REAL registered CHECKS
     row and the REAL `_run_check` codepath (subprocess + its own `count_re`), not a hand-rolled
     regex re-implementation — counts it too.

MUTATION CHECK (the falsifier, not just a claim, per §0.1 point 5 "if you cannot write the guard
you have not understood the pattern"): ONE fixture module (`engine/fixture_consumer.py` under a
synthetic repo root) is built in two variants — WITH the `from engine.substrate import stubwire`
import plus a `stubwire.stub_resolve(...)` call, and WITHOUT it (the import AND the call deleted,
standing in for a stub site that was never actually converted). `test_stub_wired_fixture_seen_by_all_three_surfaces`
asserts all three claims TRUE for the WITH variant; `test_mutation_deleting_the_import_fails_all_three`
asserts all three flip to FALSE/zero for the WITHOUT variant — so a broken/no-op detector on any of
the three surfaces fails a test here, not silently reports nothing.
"""
import importlib.util
import os
from pathlib import Path

import pytest

from engine.substrate import stubwire

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_SA_SCRIPT = os.path.join(_ROOT, 'skills', 'valoria-vector-audit', 'scripts', 'structure_audit.py')
_RC_SCRIPT = os.path.join(_ROOT, 'tools', 'review_core.py')
_CI_COMMON_SCRIPT = os.path.join(_ROOT, 'tools', 'ci_common.py')


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sa = _load('structure_audit_for_stubwire_test', _SA_SCRIPT)
rc = _load('review_core_for_stubwire_test', _RC_SCRIPT)


# ── StubResult / stub_resolve contract (frozen shape, §2.1 pin) ─────────────────────────────────

def test_stub_result_is_frozen_and_always_stub_true():
    r = stubwire.stub_resolve('m.mod', 'io.contract', reason='unit test')
    assert r.stub is True
    assert r.module == 'm.mod'
    assert r.io_contract == 'io.contract'
    assert r.reason == 'unit test'
    with pytest.raises(Exception):
        r.stub = False  # frozen dataclass — mutation must raise
    with pytest.raises(TypeError):
        stubwire.StubResult('m', 'c', 'r', stub=False)  # init=False — never caller-settable


def test_stub_resolve_returns_typed_no_op_not_a_raise():
    # A converted stub call site must be able to return in place of the NotImplementedError it
    # replaces — never fabricate a value (§0.1 / CLAUDE.md §7 no-fabrication), never raise.
    r = stubwire.stub_resolve('m', 'c', reason='r')
    assert isinstance(r, stubwire.StubResult)


# ── invocations counter + reset helper ───────────────────────────────────────────────────────────

def test_invocations_counter_and_reset_helper():
    stubwire.reset_invocations()
    assert stubwire.invocations == 0
    stubwire.stub_resolve('a', 'b', reason='x')
    stubwire.stub_resolve('a', 'b', reason='y')
    assert stubwire.invocations == 2
    stubwire.reset_invocations()
    assert stubwire.invocations == 0


# ── the fixture + mutation check (the falsifier) ─────────────────────────────────────────────────

def _fixture_source(with_stubwire: bool) -> str:
    """The one fixture module, in its two variants. WITH: imports stubwire and calls
    stub_resolve — a real converted stub call site. WITHOUT (the mutation): the import AND the
    call deleted — a stub site that was never actually converted."""
    if with_stubwire:
        return (
            '"""Fixture — tests/valoria/test_stubwire.py (mutation-verified)."""\n'
            'from engine.substrate import stubwire\n\n\n'
            'def use():\n'
            "    return stubwire.stub_resolve('engine.fixture_consumer', 'fixture.contract', "
            "reason='tests/valoria/test_stubwire.py fixture')\n"
        )
    return (
        '"""Fixture — tests/valoria/test_stubwire.py (mutation-verified: import deleted)."""\n\n\n'
        'def use():\n'
        '    return None\n'
    )


def _write_synthetic_repo(tmp_path: Path, with_stubwire: bool) -> Path:
    """A minimal synthetic repo root: real `engine/` code-root layout (so
    `structure_audit.collect_py_modules` walks it exactly as it would the live tree),
    `references/module_contracts.yaml` (so `structure_audit.main()`'s repo-root sanity check
    passes), and a copy of the REAL structure_audit.py script at its real relative path (so
    `review_core`'s `stubs.count` row — which shells out to that relative path — finds it).
    Also stages a copy of tools/ci_common.py at its real relative path (OI-54, ED-IN-0097, W4):
    structure_audit.py imports it at module level (the single-owner has_main_guard adoption) via
    the same sys.path-relative-to-`__file__` idiom the real tree uses, so a subprocess run from
    THIS synthetic root needs the real tools/ci_common.py reachable the same way — otherwise the
    subprocess crashes at import time with ModuleNotFoundError before it can even parse
    --stub-count/--contracts-join, which would silently break every review_core signal that
    shells out to this script, not just the ones this fixture is actually testing."""
    (tmp_path / 'references').mkdir(parents=True)
    (tmp_path / 'references' / 'module_contracts.yaml').write_text('modules: []\n', encoding='utf-8')

    engine_dir = tmp_path / 'engine'
    (engine_dir / 'substrate').mkdir(parents=True)
    (engine_dir / 'substrate' / '__init__.py').write_text('', encoding='utf-8')
    (engine_dir / 'substrate' / 'stubwire.py').write_text(
        '"""Synthetic stand-in — structure_audit only needs this module NODE to exist so the '
        'AST import edge resolves; this file is never executed (the fixture consumer\'s actual '
        'import resolves to the REAL production engine.substrate.stubwire via sys.path)."""\n',
        encoding='utf-8')
    (engine_dir / 'fixture_consumer.py').write_text(_fixture_source(with_stubwire), encoding='utf-8')

    sa_dst = tmp_path / 'skills' / 'valoria-vector-audit' / 'scripts' / 'structure_audit.py'
    sa_dst.parent.mkdir(parents=True)
    sa_dst.write_text(Path(_SA_SCRIPT).read_text(encoding='utf-8'), encoding='utf-8')

    ci_common_dst = tmp_path / 'tools' / 'ci_common.py'
    ci_common_dst.parent.mkdir(parents=True, exist_ok=True)
    ci_common_dst.write_text(Path(_CI_COMMON_SCRIPT).read_text(encoding='utf-8'), encoding='utf-8')
    return tmp_path


def _run_fixture(tmp_path: Path, with_stubwire: bool, monkeypatch):
    """Exercise all three surfaces against ONE fixture variant."""
    root = _write_synthetic_repo(tmp_path, with_stubwire)

    # 1. invocations counter — actually EXECUTE the fixture module (dynamically loaded from disk;
    #    its `from engine.substrate import stubwire` resolves to the REAL production module via
    #    sys.path — the synthetic engine/substrate/stubwire.py above exists only so
    #    structure_audit's static scan below has a node to resolve the edge against).
    stubwire.reset_invocations()
    fixture_mod = _load('fixture_consumer_for_stubwire_test',
                         str(root / 'engine' / 'fixture_consumer.py'))
    fixture_mod.use()
    invocations_delta = stubwire.invocations

    # 2. audit attribute — structure_audit's stub_wired, over the SAME AST import pass
    #    (build_g_code) `run()` uses, on the synthetic root.
    modules = sa.collect_py_modules(root)
    g_code, errs = sa.build_g_code(root, modules)
    assert errs == []
    audit_hit = 'engine.fixture_consumer' in sa.stub_wired_modules(g_code)

    # 3. review_core signal — the REAL registered CHECKS row + its REGISTERED count_re, via the
    #    REAL _run_check codepath (subprocess), against the synthetic root.
    monkeypatch.setattr(rc, 'ROOT', root)
    chk = next(c for c in rc.CHECKS if c['id'] == 'stubs.count')
    sig = rc._run_check(chk)

    return invocations_delta, audit_hit, sig


def test_stub_wired_fixture_seen_by_all_three_surfaces(tmp_path, monkeypatch):
    invocations_delta, audit_hit, sig = _run_fixture(tmp_path, with_stubwire=True,
                                                       monkeypatch=monkeypatch)
    assert invocations_delta == 1, "the fixture's stub_resolve call did not bump invocations"
    assert audit_hit, "structure_audit's stub_wired attribute did not see the fixture's import"
    assert sig['verdict'] == 'fail' and sig['count'] == 1, (
        f"review_core's stubs.count signal did not count the fixture: {sig}")


def test_mutation_deleting_the_import_fails_all_three(tmp_path, monkeypatch):
    """The falsifier: with the fixture's `from engine.substrate import stubwire` import (and its
    call) DELETED, all three assertions above must flip to false/zero in the SAME test — proving
    none of the three checks can pass on a fixture that never actually converted."""
    invocations_delta, audit_hit, sig = _run_fixture(tmp_path, with_stubwire=False,
                                                       monkeypatch=monkeypatch)
    assert invocations_delta == 0, "invocations counted a call the mutated fixture never made"
    assert not audit_hit, "structure_audit's stub_wired attribute still saw the mutated fixture"
    assert sig['verdict'] == 'pass' and sig['count'] == 0, (
        f"review_core's stubs.count signal still counted the mutated fixture: {sig}")
