"""B15.04 (`PC_B`): the deep tier follows the window it is drawn in.

`combat_systems.commit_depth` draws a depth in a window that room contracts (`_commit_range_factor`): an exchange is fought closed, so
the window is about [2, 4.03], not [2, 5]. A threshold on a drawn quantity is stated in the quantity's own range: `deep_commit` and
`lunge_commit` are the lower edge of the window's upper third (`DEEP_FRAC`, `LUNGE_FRAC` = 2/3), which at full room is 4.0.

  (1) at full room the edge is exactly 4.0, as the two absolute keys shipped it;
  (2) below full room the edge moves with the window, an upper third;
  (3) gate 1: for every roster weapon between a quarter and two fifths of the exchanges are drawn at or above the edge
      (the keys it replaced sat in the top 1.5% of the window: about 1%);
  (4) gate 2: forcing the aggressor's depth does not pay: no forced depth fells its fighter less often than another forced depth
      by more than the interval of the difference (it read 45 / 49 / 54 % felled at 3.9 / 3.0 / 2.3 when the tier was unreachable).

The reading of a fight is `workbench/scale_census.py::read`; a depth is recorded or forced at `combat_systems.commit_depth`, the one
draw of it.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1', 'workbench'))
import scale_census as SC   # noqa: E402

from engine.dice_engine import draw           # noqa: E402
from modules.combat import combat_systems as S, combatant, weapons, wrapper   # noqa: E402
from modules.combat.config import CFG          # noqa: E402

_ROSTER = sorted(k for k in weapons.WEAPONS if not k.endswith('_halfsword'))   # the startable weapons: a half-sword form is a switched FORM, never a loadout


def _combatant(room):
    c = combatant.Combatant('A')
    c.range_avail = room
    return c




def test_deep_edge_follows_the_window():
    """Below full room the window's top falls (`commit_depth`'s `2 + 3 * factor`); the edge stays the lower edge of its upper third."""
    rooms = [CFG['RANGE_AVAIL_FLOOR'] + i * (CFG['RANGE_COMMIT_PEAK'] - CFG['RANGE_AVAIL_FLOOR']) / 6 for i in range(6)]   # the floor up to just below the peak
    last, checked = 0.0, 0
    for room in rooms:
        c = _combatant(room)
        top = 2.0 + 3.0 * S._commit_range_factor(room, CFG)
        for edge in (S.deep_commit(c, CFG), S.lunge_commit(c, CFG)):
            assert 2.0 < edge < 4.0, (room, edge)                      # strictly inside the contracted window, below the full-room 4.0
            assert math.isclose(top - edge, (top - 2.0) / 3.0), (room, top, edge)
            checked += 1
        assert S.deep_commit(c, CFG) > last, (room, last)               # a wider window carries a deeper edge
        last = S.deep_commit(c, CFG)
    assert checked >= 12
    assert 3.3 < S.deep_commit(_combatant(CFG['RANGE_AVAIL_FLOOR']), CFG) < 3.4   # closed measure, equal reach: the 3.35 the plan reads


def _fight(weapon, seed, force=None, record=None, cfg=None):
    """One lethal mirror of `weapon` at light armour. `record` collects (commit, deep edge) per draw; `force` fixes A's depth when A is the aggressor."""
    A = combatant.Combatant('A', weapon=weapon, score=2)
    B = combatant.Combatant('B', weapon=weapon, score=2)
    trace = []
    drawn = S.commit_depth

    def seam(aggressor, defender, cfg_, rng, TR):
        out = drawn(aggressor, defender, cfg_, rng, TR)         # the draw is always taken, so the stream is the same with or without a force
        commit = out[0]
        if force is not None and aggressor is A:
            commit = force
        if record is not None:
            record.append((commit, S.deep_commit(aggressor, cfg_)))
        return (commit,) + tuple(out[1:])

    S.commit_depth = seam
    try:
        result = wrapper.fight(A, B, cfg or CFG, draw.seeded(draw.H2('deep_commit', seed)), trace=trace.append)
    finally:
        S.commit_depth = drawn
    return result, trace


def test_share_at_deep_edge_between_a_quarter_and_two_fifths():
    """Gate 1: the share of exchanges drawn at or above the deep edge, per roster weapon (mirror, light armour, 100 fights each)."""
    checked = 0
    for w in _ROSTER:
        drawn = []
        for seed in range(100):
            _fight(w, seed, record=drawn)
        share = sum(c >= edge for c, edge in drawn) / len(drawn)
        assert 0.25 <= share <= 0.40, (w, share, len(drawn))
        checked += 1
    assert checked >= len(_ROSTER) >= 40


def test_forced_depths_within_interval_after_change():
    """Gate 2, the falsifier's direction: A's depth forced to 3.9, 3.0 and 2.3 against a B who draws his own, 3,000 season-default mirrors
    each (arming sword, light armour, skill score 2). The deepest forced depth (3.9, in the deep tier) is not felled LESS often than
    either other by more than the interval of the difference: depth is not free. (With the edge back at 4.0 the tier is out of reach
    and the three read monotone, 46 / 50 / 54 % felled: the deepest is the safest.)"""
    n, z = 3000, 1.96
    felled = {}
    for depth in (3.9, 3.0, 2.3):
        hits = 0
        for seed in range(n):
            result, trace = _fight('arming', seed, force=depth)
            hits += SC.read(result, trace)['felled_winner'] == 'B'   # A was felled
        felled[depth] = hits / n
    checked = 0
    for other in (3.0, 2.3):
        interval = z * math.sqrt(felled[3.9] * (1 - felled[3.9]) / n + felled[other] * (1 - felled[other]) / n)
        assert felled[other] - felled[3.9] <= interval, (other, felled)   # 3.9 felled less often than `other` by more than the interval
        checked += 1
    assert checked >= 2
