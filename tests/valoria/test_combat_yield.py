"""PC-01 (`ED-PC-0056`): §11.4 Yield, built as a declaration on `wrapper.fight`, NO fourth band.

The two falsifiers are the workplan position's own (`valoria_master_workplan_v9_part7.md`, PC-01):
  (a) a planted yield ends the exchange with ZERO further rolls -- the bout count is asserted, and
      every engine-level draw is counted (`_draw_stream.RecordingRandom`, which also sees the `gauss`
      draws a `random()` counter would miss), so a yield that "ends" the fight after one more draw is seen;
  (b) a yield accepted while the yielder's objective is still contested in the zone is REFUSED --
      the fight runs exactly as the no-yield control does.
Both were run red on the base tree (no yield resolver existed) before the build.

The mapping decision is asserted too: a yielder is read by the EXISTING `combat_degree` walk as
`Untouched`/`Wounded` (never `Felled`), and the surrender rides on the seam's result.
"""
import functools
import os
import random
import sys

import pytest

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_ENGINE = os.path.join(_ROOT, 'systems', 'combat', 'combat_engine_v1')
for _p in (_ROOT, _ENGINE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from valoria import _draw_stream as DS          # noqa: E402  the single owner of the draw instrument (CLAUDE.md §8)

import combatant as C                            # noqa: E402
import wrapper                                   # noqa: E402
from config import CFG                           # noqa: E402


def _fight(seed, by=None, max_bouts=12, **yield_kw):
    """One fight on `seed`; `by` ('A' | 'B') plants a `Yield` declared by that combatant. Every trace event
    carries `_draws`, the engine-level draws taken so far, so "no draw after the declaration" is observable."""
    A, B = C.Combatant('A'), C.Combatant('B')
    kw = {} if by is None else {'yield_decl': wrapper.Yield(by={'A': A, 'B': B}[by], **yield_kw)}
    trace = []
    prev = wrapper._TRACE
    rng = DS.RecordingRandom(seed)
    try:
        wrapper._TRACE = lambda e: trace.append(dict(e, _draws=len(rng.trace)))
        result = wrapper.fight(A, B, CFG, rng, max_bouts=max_bouts, **kw)
    finally:
        wrapper._TRACE = prev
    return result, trace, rng, A, B


def _bouts(trace):
    return sum(1 for e in trace if e['kind'] == 'turn_start')


@functools.lru_cache(maxsize=None)
def _seed_lasting(min_bouts):
    """A seed whose no-yield fight runs at least `min_bouts` bouts, found rather than assumed."""
    for seed in range(200):
        if _bouts(_fight(seed)[1]) >= min_bouts:
            return seed
    raise AssertionError(f"no seed in 0..199 runs {min_bouts} bouts")


@pytest.mark.parametrize('by', ['A', 'B'])
@pytest.mark.parametrize('turn', [1, 2, 3])
def test_a_planted_yield_ends_the_exchange_with_zero_further_rolls(turn, by):
    seed = _seed_lasting(turn)                        # the control reaches the yield's turn
    _, ctrl_trace, ctrl_rng, _, _ = _fight(seed)
    result, trace, rng, A, B = _fight(seed, by=by, turn=turn, accepted=True)
    yielder = {'A': A, 'B': B}[by]
    # THE BOUT COUNT: the yield is declared at Phase 1 of `turn`, so exactly turn-1 bouts ran.
    assert _bouts(trace) == turn - 1, (turn, _bouts(trace))
    ylds = [i for i, e in enumerate(trace) if e['kind'] == 'yield']
    assert len(ylds) == 1, trace[-5:]
    ev = trace[ylds[0]]
    assert ev['by'] == by and ev['accepted'] is True and ev['refused'] is None
    # ZERO FURTHER ROLLS: nothing but the result follows the declaration, and the RNG is not touched after
    # it -- an extra draw at any turn (the UPSET_FLOOR roll, say) breaks the equality.
    assert [e['kind'] for e in trace[ylds[0] + 1:]] == ['fight_result']
    assert len(rng.trace) == ev['_draws'], (len(rng.trace), ev['_draws'])
    assert len(rng.trace) < len(ctrl_rng.trace)
    # every bout before `turn` is the control's, draw for draw
    assert trace[:ylds[0]] == ctrl_trace[:ylds[0]]
    # The combat ENDS with the yielder standing: the opponent's result, no felling.
    assert result == (1 if by == 'B' else -1) and not yielder.felled


def test_a_yield_at_turn_one_takes_no_draw_at_all():
    """The strictest form of (a): a yield at turn 1 is declared before any draw is taken."""
    result, trace, rng, A, B = _fight(7, by='A', turn=1, accepted=True)
    assert len(rng.trace) == 0 and rng.underlying == 0
    assert _bouts(trace) == 0
    assert result == -1 and not A.felled


def test_a_yield_the_opponent_refuses_still_ends_the_fight_with_no_further_roll():
    """`accepted=False` is the OPPONENT declining the yield: the yielder is unresisting, so no contest roll
    resolves anything further and the fight ends exactly as an accepted yield does. The engine has no
    decider and no free-strike resolver (that would be a fourth resolver); the opponent's disposition
    is the caller's, carried on the `yield` event. Pinned so the two cannot drift apart unnoticed."""
    from engine.season.seam.wrappers.combat import surrender_of
    result, trace, rng, A, B = _fight(7, by='A', turn=1, accepted=False)
    assert len(rng.trace) == 0 and _bouts(trace) == 0
    assert result == -1 and not A.felled
    assert surrender_of(trace) == dict(by='A', turn=1, accepted=False)
    ok_result, _, ok_rng, _, _ = _fight(7, by='A', turn=1, accepted=True)
    assert (result, len(rng.trace)) == (ok_result, len(ok_rng.trace))


def test_a_yield_that_could_never_fire_is_refused_loudly():
    A, B, other = C.Combatant('A'), C.Combatant('B'), C.Combatant('C')
    for bad in (wrapper.Yield(by=other, turn=1),        # neither combatant: would silently award A the win
                wrapper.Yield(by=A, turn=0),             # before the first turn
                wrapper.Yield(by=A, turn=13),            # after max_bouts
                wrapper.Yield(by='A', turn=1)):          # not a combatant at all
        with pytest.raises(ValueError):
            wrapper.fight(A, B, CFG, random.Random(0), max_bouts=12, yield_decl=bad)


def test_a_yield_while_the_objective_is_contested_in_the_zone_is_refused():
    for seed in range(5):
        ctrl_result, ctrl_trace, ctrl_rng, _, _ = _fight(seed)
        result, trace, rng, _, _ = _fight(seed, by='B', turn=1, accepted=True, objective_contested=True)
        ylds = [e for e in trace if e['kind'] == 'yield']
        assert len(ylds) == 1 and ylds[0]['refused'] == 'objective_contested', ylds
        # REFUSED means the fight is the control's, bout for bout and draw for draw.
        assert result == ctrl_result
        assert len(rng.trace) == len(ctrl_rng.trace)
        assert [e for e in trace if e['kind'] != 'yield'] == ctrl_trace
        assert _bouts(trace) >= 1


def test_a_yielder_is_read_by_the_existing_bands_never_a_fourth():
    """The mapping: no band is added. A yielder is standing, so the shipped walk reads it as
    `Untouched` (no wounds) or `Wounded`; the surrender is on the result, not in the band."""
    from engine.season.data.rosters import COMBAT_BANDS, WOUND_QUANTITIES
    from engine.season.seam.ladder import combat_degree
    from engine.season.seam.wrappers.combat import surrender_of
    assert len(COMBAT_BANDS) == 3
    for turn in (1, 3):
        _, trace, _, _, B = _fight(_seed_lasting(turn), by='B', turn=turn, accepted=True)
        st = dict(available=True, **{q: getattr(B.wt, q) for q in WOUND_QUANTITIES})
        assert combat_degree(dict(wound_state={'B': st}), 'B') in COMBAT_BANDS[1:]
        assert surrender_of(trace) == dict(by='B', turn=turn, accepted=True)
    assert surrender_of([{'kind': 'turn_start'}]) is None
