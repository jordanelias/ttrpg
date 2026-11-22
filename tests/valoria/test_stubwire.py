"""Falsifier tests for engine/substrate/stubwire.py — the P1 stub-wire primitive (ED-IN-0091,
`audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md` §2.1).

TWO claims as of 2026-08-21. A third — `tools/review_core.py`'s `stubs.count` report-only signal —
was dropped when culling wave 2 retired `review_core.py` (ED-IN-0194). The two that remain are the
two whose subject is the executable model; the retired one's subject was the repository-state
ratchet.

Two claims, one fixture, one mutation (§0.1 point 3 "name the falsifier"):
  1. `stub_resolve` bumps the module-level `invocations` counter — the counter
     `tools/m1_acceptance.py`'s probe reads as a before/after delta.
  2. `structure_audit.py`'s `stub_wired` node attribute (derived from the SAME AST import pass
     `build_g_code` already runs — no second parser) sees a module that imports
     `engine.substrate.stubwire`.

MUTATION CHECK (the falsifier, not just a claim, per §0.1 point 5 "if you cannot write the guard
you have not understood the pattern"): ONE fixture module (`engine/fixture_consumer.py` under a
synthetic repo root) is built in two variants — WITH the `from engine.substrate import stubwire`
import plus a `stubwire.stub_resolve(...)` call, and WITHOUT it (the import AND the call deleted,
standing in for a stub site that was never actually converted). `test_stub_wired_fixture_seen_by_both_surfaces`
asserts both claims TRUE for the WITH variant; `test_mutation_deleting_the_import_fails_both`
asserts both flip to FALSE/zero for the WITHOUT variant — so a broken/no-op detector on either of
the two surfaces fails a test here, not silently reports nothing.
"""
import pytest

from engine.substrate import stubwire


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
