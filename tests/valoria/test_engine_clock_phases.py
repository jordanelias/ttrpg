"""The tick's three phases happen in the right order, in the right module (ED-IN-0199).

WHAT THIS PINS, AND WHY IT IS NOT APPARATUS-GUARDING-APPARATUS.
`propagation_spec_v1.md` §O.1 makes engine_clock the owner of SEASON_TICK -> ACTION ->
ACCOUNTING_BOUNDARY. CLAUDE.md §0.1 pt 5's predicate admits this guard: the artifact is the
tick's phase ordering, which is load-bearing on the game (it decides when an accounting effect
lands relative to the action phase) and on the port (Godot re-implements this loop). It is not a
test of a checker.

⚠ THIS FILE LOST HALF ITS CASES ON 2026-09-16 (ED-IN-0232, Jordan: *"anything key-based gets
retired"*), and the half it lost is worth naming so nobody reads the remainder as the whole test.
The original subject was a REAL and subtle defect: the Key scheduler's `accounting_boundary()`
and `next_tick()` calls used to sit at the tail of `mc_v18._faction_actions_callback` — inside
the ACTION phase's own body — so the scheduler was in `_PHASE_ACTION` for the whole of
accounting, and `keys.py:_emit_at_depth` deferred an `apply` precisely when the phase was
ACTION. An accounting-phase emission carrying a settlement effect would have been queued to the
NEXT season's boundary: a silent one-tick lag. Four cases pinned that (the deferred apply landing
before accounting rather than after, the action body leaving the phase alone, the tick closing
back into ACTION, the emission counter spanning both phases) and all four observed a scheduler
phase. With the substrate retired there is no scheduler, no emission counter and no deferred
apply, so those four cases have no subject — they are DELETED, not weakened into something that
passes.

WHAT SURVIVES is the ordering claim itself, which never needed Keys: accounting's body runs after
the action callback and exactly once per tick, and the season advances exactly once. That is the
falsifier `engine/autoload/engine_clock.py`'s own docstring now cites.
"""
from __future__ import annotations

import pytest

from engine.autoload import engine_clock
from engine.autoload.game_state import create_world
from engine.substrate import composition
from systems.overview.sim import accounting as accounting_module


@pytest.fixture
def world():
    return create_world(seed=0)


@pytest.fixture
def spy_accounting(monkeypatch):
    """Record the order of events from INSIDE accounting's body.

    `composition.require` memoises per role, so replacing the module attribute is not
    enough on its own — the cache entry has to go too, and be restored, or a later test
    in the same process would keep the spy. `monkeypatch.setitem`/`delitem` handle the
    restore; the explicit pop covers the case where nothing had resolved the role yet.
    """
    calls = []

    def _spy(w):
        calls.append('accounting')
        return accounting_module.run_accounting(w)

    composition._CACHE.pop('accounting', None)
    monkeypatch.setitem(composition._CACHE, 'accounting', _spy)
    yield calls
    composition._CACHE.pop('accounting', None)


# ── Ordering ──────────────────────────────────────────────────────────────────────────

def test_accounting_runs_after_the_action_callback(world, spy_accounting):
    """§O.1's order: the ACTION phase's body closes before accounting's body opens.

    The spy appends 'accounting'; the action callback appends 'action'. Asserting the SEQUENCE
    rather than a phase flag is what makes this observable now that no scheduler carries one —
    and it is the same claim: accounting must not run while the action phase is still open.
    """
    engine_clock.run_tick(world, action_callback=lambda w: spy_accounting.append('action'))

    assert spy_accounting == ['action', 'accounting'], (
        f"expected the action body then accounting, got {spy_accounting}"
    )


def test_accounting_runs_exactly_once_per_tick(world, spy_accounting):
    """One tick, one accounting pass.

    ⚠ THE JUSTIFICATION THIS TEST FIRST CARRIED WAS FALSE, and is kept corrected rather than
    quietly reworded: it claimed to be the §0.1-pt-2 non-vacuity guard for the ordering case
    above, on the reasoning that a spy which never fired would leave that test "vacuous on an
    empty list". It would not — `assert [] == [...]` FAILS. The ordering case is already
    non-vacuous by construction, and a guard that cannot fail for the reason it states is
    worse than no guard.

    What this DOES catch is a real defect the ordering case cannot see: accounting running twice.
    `run_tick` resolves the role and calls it once; a future edit that also left a call in the
    action callback would still satisfy the order and double every accounting effect.
    """
    engine_clock.run_tick(world, action_callback=lambda w: None)
    assert spy_accounting.count('accounting') == 1, (
        f"accounting ran {spy_accounting.count('accounting')} times in one tick"
    )


def test_a_tick_runs_with_no_action_callback_at_all(world, spy_accounting):
    """`action_callback=None` is legal and still reaches accounting."""
    before = world.season
    result = engine_clock.run_tick(world)

    assert spy_accounting == ['accounting']
    assert world.season == before + 1
    assert result.season == world.season


def test_run_tick_advances_the_season_exactly_once():
    """engine_clock is "the only module that may advance the season counter" (§O.1)."""
    w = create_world(seed=0)
    start = w.season
    for _ in range(3):
        engine_clock.run_tick(w)
    assert w.season == start + 3


def test_the_phase_roster_is_the_spec_s_three(world):
    """§O.1 names exactly three phases, in this order. A fourth is a spec change, not an edit."""
    assert engine_clock.PHASES == (
        engine_clock.PHASE_SEASON_TICK,
        engine_clock.PHASE_ACTION,
        engine_clock.PHASE_ACCOUNTING_BOUNDARY,
    )
