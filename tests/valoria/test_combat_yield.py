"""PC-01 (`ED-PC-0056`): §11.4 Yield, built as a declaration on `wrapper.fight`, NO fourth band.

The two falsifiers are the workplan position's own (`valoria_master_workplan_v9_part7.md`, PC-01):
  (a) a planted yield ends the exchange with ZERO further rolls -- the bout count is asserted, and
      the RNG is counted, so a yield that "ends" the fight after one more draw is seen;
  (b) a yield accepted while the yielder's objective is still contested in the zone is REFUSED --
      the fight runs exactly as the no-yield control does.
Both were run red on the base tree (no yield resolver existed) before the build.

The mapping decision is asserted too: a yielder is read by the EXISTING `combat_degree` walk as
`Untouched`/`Wounded` (never `Felled`), and the surrender rides on the seam's result.
"""
import os
import random
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

ROLL_KINDS = ('roll', 'stophit', 'commit', 'read', 'contact', 'disengage')


class _CountingRandom(random.Random):
    """Counts every draw the engine takes (`random()` and `randrange()` are the two it uses)."""

    def __init__(self, seed):
        super().__init__(seed)
        self.draws = 0

    def random(self):
        self.draws += 1
        return super().random()

    def randrange(self, *a, **k):
        self.draws += 1
        return super().randrange(*a, **k)


def _fight(seed, yield_decl=None, max_bouts=12):
    import wrapper
    import combatant as C
    from config import CFG
    A, B = C.Combatant('A'), C.Combatant('B')
    if yield_decl is not None:
        yield_decl = yield_decl(A, B)
    trace = []
    prev = wrapper._TRACE
    rng = _CountingRandom(seed)
    try:
        # each event carries the draws taken so far, so "no draw after the declaration" is observable at any turn
        wrapper._TRACE = lambda e: trace.append(dict(e, _draws=rng.draws))
        kw = {} if yield_decl is None else {'yield_decl': yield_decl}
        result = wrapper.fight(A, B, CFG, rng, max_bouts=max_bouts, **kw)
    finally:
        wrapper._TRACE = prev
    return result, trace, rng, A, B


def _bouts(trace):
    return sum(1 for e in trace if e['kind'] == 'turn_start')


def _seed_lasting(min_bouts):
    """A seed whose no-yield fight runs at least `min_bouts` bouts, found rather than assumed."""
    for seed in range(200):
        _, trace, _, _, _ = _fight(seed)
        if _bouts(trace) >= min_bouts:
            return seed
    raise AssertionError(f"no seed in 0..199 runs {min_bouts} bouts")


def test_a_planted_yield_ends_the_exchange_with_zero_further_rolls():
    import wrapper
    checked = 0
    for turn in (1, 2, 3):
        seed = _seed_lasting(turn)                    # the control reaches the yield's turn
        _, ctrl_trace, ctrl_rng, _, _ = _fight(seed)
        result, trace, rng, A, B = _fight(
            seed, lambda A, B: wrapper.Yield(by=B, turn=turn, accepted=True))
        # THE BOUT COUNT: the yield is declared at Phase 1 of `turn`, so exactly turn-1 bouts ran.
        assert _bouts(trace) == turn - 1, (turn, _bouts(trace))
        ylds = [i for i, e in enumerate(trace) if e['kind'] == 'yield']
        assert len(ylds) == 1, trace[-5:]
        ev = trace[ylds[0]]
        assert ev['by'] == 'B' and ev['accepted'] is True and ev['refused'] is None
        # ZERO FURTHER ROLLS: no draw-bearing event after the yield, and no engagement after it.
        after = [e['kind'] for e in trace[ylds[0] + 1:]]
        assert not [k for k in after if k in ROLL_KINDS + ('turn_start', 'engagement_start')], after
        # ...and the RNG is not touched after the declaration: the total draws equal the draws the
        # yield event itself recorded (an extra draw at any turn, e.g. the UPSET_FLOOR roll, breaks
        # this); every bout before `turn` is the control's, draw for draw.
        assert rng.draws == trace[ylds[0]]['_draws'], (rng.draws, trace[ylds[0]]['_draws'])
        assert rng.draws < ctrl_rng.draws, (rng.draws, ctrl_rng.draws)
        assert trace[:ylds[0]] == ctrl_trace[:ylds[0]]
        # The combat ENDS with the yielder standing: the opponent's result, no felling.
        assert result == 1 and not B.felled
        checked += 1
    assert checked == 3


def test_a_planted_yield_takes_no_draw_after_the_declaration():
    """The strictest form of (a): a yield at turn 1 is declared before any draw is taken."""
    import wrapper
    result, trace, rng, A, B = _fight(7, lambda A, B: wrapper.Yield(by=A, turn=1, accepted=True))
    assert rng.draws == 0, rng.draws
    assert _bouts(trace) == 0
    assert result == -1 and not A.felled


def test_a_yield_the_opponent_refuses_still_ends_the_fight_with_no_further_roll():
    """`accepted=False` is the OPPONENT declining the yield: the yielder is unresisting, so no contest roll
    resolves anything further and the fight ends exactly as an accepted yield does. The engine has no
    decider and no free-strike resolver (that would be a fourth resolver); the opponent's disposition
    is the caller's, carried on the `yield` event. Pinned so the two cannot drift apart unnoticed."""
    import wrapper
    from engine.season.seam.wrappers.combat import surrender_of
    result, trace, rng, A, B = _fight(7, lambda A, B: wrapper.Yield(by=A, turn=1, accepted=False))
    assert rng.draws == 0 and _bouts(trace) == 0
    assert result == -1 and not A.felled
    assert surrender_of(trace) == dict(by='A', turn=1, accepted=False)
    ok_result, ok_trace, ok_rng, _, _ = _fight(7, lambda A, B: wrapper.Yield(by=A, turn=1, accepted=True))
    assert (result, rng.draws) == (ok_result, ok_rng.draws)


def test_a_yield_that_could_never_fire_is_refused_loudly():
    import pytest
    import wrapper
    import combatant as C
    from config import CFG
    A, B = C.Combatant('A'), C.Combatant('B')
    other = C.Combatant('C')
    for bad in (wrapper.Yield(by=other, turn=1),        # neither combatant: would silently award A the win
                wrapper.Yield(by=A, turn=0),             # before the first turn
                wrapper.Yield(by=A, turn=13)):           # after max_bouts
        with pytest.raises(ValueError):
            wrapper.fight(A, B, CFG, random.Random(0), max_bouts=12, yield_decl=bad)
    with pytest.raises(ValueError):
        wrapper.fight(A, B, CFG, random.Random(0), max_bouts=12, yield_decl=wrapper.Yield(by='A', turn=1))


def test_a_yield_while_the_objective_is_contested_in_the_zone_is_refused():
    import wrapper
    checked = 0
    for seed in range(5):
        ctrl_result, ctrl_trace, ctrl_rng, _, _ = _fight(seed)
        result, trace, rng, _, _ = _fight(
            seed, lambda A, B: wrapper.Yield(by=B, turn=1, accepted=True, objective_contested=True))
        ylds = [e for e in trace if e['kind'] == 'yield']
        assert len(ylds) == 1 and ylds[0]['refused'] == 'objective_contested', ylds
        # REFUSED means the fight is the control's, bout for bout and draw for draw.
        assert result == ctrl_result
        assert rng.draws == ctrl_rng.draws
        assert [e for e in trace if e['kind'] != 'yield'] == ctrl_trace
        assert _bouts(trace) >= 1
        checked += 1
    assert checked == 5


def test_a_yielder_is_read_by_the_existing_bands_never_a_fourth():
    """The mapping: no band is added. A yielder is standing, so the shipped walk reads it as
    `Untouched` (no wounds) or `Wounded`; the surrender is on the result, not in the band."""
    import wrapper
    from engine.season.data.rosters import COMBAT_BANDS, WOUND_QUANTITIES
    from engine.season.seam.ladder import combat_degree
    from engine.season.seam.wrappers.combat import surrender_of
    assert len(COMBAT_BANDS) == 3
    seen = set()
    for turn in (1, 3):
        seed = _seed_lasting(turn)
        result, trace, _, A, B = _fight(seed, lambda A, B: wrapper.Yield(by=B, turn=turn, accepted=True))
        st = dict(available=True, **{q: getattr(B.wt, q) for q in WOUND_QUANTITIES})
        band = combat_degree(dict(wound_state={'B': st}), 'B')
        assert band in COMBAT_BANDS[1:], band
        seen.add(band)
        sur = surrender_of(trace)
        assert sur == dict(by='B', turn=turn, accepted=True), sur
    assert seen
    assert surrender_of([{'kind': 'turn_start'}]) is None
