"""[ED-MB-0041] Army-level break by contagion, and the inertness of its default.

`Unit.derive_rout` required ALL subunits routed before the unit broke, and `run_battle` only stops when
a unit routs — so with per-subunit breaking at the historical 15-30% band, the sections that have
already broken sit on the field absorbing casualties while their siblings fight on. The casualty
scoreboard measured the consequence: the loser reaches 61-87% total casualties on EVERY gauge row,
against a 15-30% expectation. Armies do not do that. They come apart once a decisive portion of the
line goes (du Picq: the end of a battle is moral, not physical).

`ROUT_CASCADE_FRAC` generalises `all(...)` to a fraction of SPAWN strength. It defaults to 1.0, which
must reproduce the old behaviour EXACTLY — including the float equality, since `>= 1.0` on a computed
ratio is the kind of thing that silently becomes `0.9999999` and changes when an army breaks. These
tests pin both the mechanism and that inertness.
"""
import os
import sys

import pytest

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

from mass_battle.config import ROUT_CASCADE_FRAC
from mass_battle.engine import build_army, SIDE_A_START_ROW


def _unit(n_sub=3, troops=300.0):
    return build_army(
        [{'shape': 'Line', 'troop_type': 'infantry', 'troops': troops, 'concentration': 100.0,
          'starting_position': (SIDE_A_START_ROW, 8 + i * 5)} for i in range(n_sub)],
        'A', 'A')


@pytest.mark.parametrize('n_sub', [2, 3, 4, 5, 7])
def test_broken_share_is_exactly_one_when_every_subunit_has_routed(n_sub):
    """The float-equality guard. `>= 1.0` must fire when the last section goes, at every army size.

    `gone` and `tot` sum the same addends in the same order once all subunits are routed, so the ratio
    is exactly 1.0 rather than a hair under it. If that ever stops holding, an army with every section
    broken would keep fighting — and the default would no longer be inert.
    """
    u = _unit(n_sub)
    for a in u.subunits:
        a.routed = True
    assert u._broken_share() == 1.0


def test_broken_share_measures_against_THIS_battle_s_starting_strength():
    """`_start_troops` is re-based at each campaign boundary; the share must follow it.

    A unit entering its third battle already depleted should measure collapse against the strength it
    started THAT battle with, not against its original spawn size — otherwise a worn army looks like it
    is only fractionally broken when in fact its whole remaining line has gone.

    (Note `troop_count`, the fallback, is itself a static nominal — it returns `self.troops` — so both
    weights are strength-at-start. Neither shrinks as the body takes casualties, which is exactly the
    property required: the numerator must grow monotonically as sections break.)
    """
    u = _unit(2)
    a, b = u.subunits
    # simulate a campaign boundary after heavy attrition: this battle starts at a fraction of spawn
    a._start_troops = a.troop_count * 0.25
    b._start_troops = b.troop_count
    a.routed = True
    share = u._broken_share()
    assert share == pytest.approx(0.25 / 1.25), (
        "the broken share must weight by this battle's starting strength, not the original spawn size")


def test_broken_share_does_not_move_as_a_broken_section_bleeds_out():
    """The numerator must be monotone in sections-broken, never eroded by their ongoing casualties."""
    u = _unit(2)
    a, _b = u.subunits
    a.routed = True
    before = u._broken_share()
    for cid in list(a.cell_troops):
        a.cell_troops[cid] *= 0.1
    assert u._broken_share() == pytest.approx(before)


def test_default_is_inert():
    """The shipped default must reproduce `all(a.routed ...)`, so goldens and gauge are untouched."""
    assert ROUT_CASCADE_FRAC == 1.0
    u = _unit(3)
    u.subunits[0].routed = True
    u.subunits[1].routed = True
    u.derive_rout()
    assert not u.routed, "two of three broken must NOT break the army at the inert default"
    u.subunits[2].routed = True
    u.derive_rout()
    assert u.routed, "the last section breaking must break the army"


def test_a_lowered_threshold_breaks_the_army_early():
    """The mechanism itself: below 1.0, a decisive portion breaking is enough."""
    import mass_battle.hierarchy.units as U
    u = _unit(3)
    u.subunits[0].routed = True
    assert u._broken_share() == pytest.approx(1 / 3)
    orig = U.ROUT_CASCADE_FRAC
    try:
        U.ROUT_CASCADE_FRAC = 0.33
        u.derive_rout()
        assert u.routed, "one third of the line broken must break the army at a 0.33 threshold"
        assert all(a.routed for a in u.subunits), \
            "an army that breaks takes its remaining sections with it (the whole body flees)"
    finally:
        U.ROUT_CASCADE_FRAC = orig
