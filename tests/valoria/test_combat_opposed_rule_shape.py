"""B15.03 (`29_DICE` item 29-3, A-31, A-71, A-79): the fight opposes at the one rate, and a Success is one Wound Interval.

Five readings of the fight's SCALE at module scale (`wrapper.fight` with the trace seam, arming sword and light armour, lethal
terms; the skill score is the only thing two sides differ in), each ending on `assert checked >= <cells>`:

  (a) fight length and blows  `test_season_mirror_length_blows_and_reversals`  (the mirror at score 2: rounds, wounding blows, lead change)
  (b) the better fighter      `test_the_better_fighter_wins_on_the_stated_curve`
  (c) defence is real, and no attrition by rank
                              `test_each_rank_of_defence_lowers_the_wounding_share`, `test_the_mirror_is_level_across_ranks`
  and the scale itself        `test_a_success_is_one_wound_interval`

A "round" is the engine's `round_start` count (A-101). The reading of a fight is `workbench/scale_census.py::read`, the one owner of
it. The windows are the plan's (`29_DICE` item 29-3 step 4); the live arm is rate `MU_PER_DIE`, `DMG_SCALE` 1.07, the control arm
(`scale_census.arm('control')`) is the 2026-08-14 rate 0.5 and scale 1.55, which reads outside them.

Every fight is read TO ITS FELLING, with the yield roll (B15.10, `PC_A`) held at Success (`scale_census.no_yield`): the windows measure the
exchange rule and its scale, and the yield decision has its own measure (`test_combat_yield_draw.py`). With the roll live the death-terms
mirror's mean falls to about 3.4 rounds, under the (a) window; the two readings are not the same fight, and neither stands in for the other.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1', 'workbench'))
import scale_census as SC   # noqa: E402

from modules.combat import combatant as C   # noqa: E402
from modules.combat import core             # noqa: E402
from modules.combat.config import CFG       # noqa: E402


def test_a_success_is_one_wound_interval():
    """`core.strike(A, B, 'success', CFG)` is B's Wound Interval for default fighters (arming sword, light armour)."""
    A, B = C.Combatant('A'), C.Combatant('B')
    assert (A.weapon, A.armor) == ('arming', 'light') == (B.weapon, B.armor)
    assert core.strike(A, B, 'success', CFG) == B.wt.wi, (core.strike(A, B, 'success', CFG), B.wt.wi)


def test_season_mirror_length_blows_and_reversals():
    """The season's even fight (skill score 2 both, seeds 0-1,199): its length, its wounding blows and whether the lead turns."""
    t = SC.Tally(2, 2, 0, 1200)
    assert t.fights == 1200
    assert 4.0 <= t.mean_turns() <= 5.0, t.mean_turns()
    assert t.mean_wounds() >= 4.3, t.mean_wounds()
    assert t.lead_change() >= 0.40, t.lead_change()
    assert t.undecided() <= 0.02, t.undecided()
    assert t.bloodless_turns() <= 0.45, t.bloodless_turns()
    assert 0.45 <= t.wounds_per_roll() <= 0.57, t.wounds_per_roll()




def test_the_mirror_is_level_across_ranks():
    """Ranks 0, 2, 5, 7 each fight their own rank, 1,000 fights each: no rank's mirror runs longer, stalls or fails more."""
    tallies = {r: SC.Tally(r, r, 0, 1000) for r in (0, 2, 5, 7)}
    turns = [t.mean_turns() for t in tallies.values()]
    assert max(turns) - min(turns) <= 0.5, turns
    checked = 0
    for r, t in tallies.items():
        assert t.undecided() <= 0.02, (r, t.undecided())
        assert t.fail_share() <= 0.25, (r, t.fail_share())
        checked += 1
    assert checked >= 4


def test_each_rank_of_defence_lowers_the_wounding_share():
    """The attacker at rank 2 against defenders of rank 0 to 4, 600 fights each: the share of his rolls that wound falls at every rank."""
    shares = [SC.Tally(2, d, 0, 600).wounds_per_roll('A') for d in range(5)]
    checked = 0
    for lo, hi in zip(shares, shares[1:]):
        assert lo - hi >= 0.04, shares
        checked += 1
    assert checked >= 4
