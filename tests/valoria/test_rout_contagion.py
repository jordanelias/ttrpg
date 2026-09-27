"""[ED-MB-0041] Army-level break by contagion, and the inertness of its default.

`Unit.derive_rout` required ALL subunits routed before the unit broke, and `run_battle` only stops when
a unit routs — so with per-subunit breaking at the historical 15-30% band, the sections that have
already broken sit on the field absorbing casualties while their siblings fight on. The casualty
scoreboard measured the consequence: the loser reaches 61-87% total casualties on EVERY gauge row,
against a 15-30% expectation. Armies do not do that. They come apart once a decisive portion of the
line goes (du Picq: the end of a battle is moral, not physical).

`ROUT_CASCADE_FRAC` generalises `all(...)` to a fraction of SPAWN strength. 1.0 must reproduce the old
behaviour EXACTLY — including the float equality, since `>= 1.0` on a computed ratio is the kind of
thing that silently becomes `0.9999999` and changes when an army breaks. These tests pin both the
mechanism and that boundary.

[A8, ED-MB-0067 Part A / ED-MB-0071, 2026-09-27] The default is no longer 1.0 — chosen by sweep
(workbench/rout_cascade_sweep.py) to be 0.5, deliberately NOT inert (see config.py's own comment on
the constant). `test_threshold_1_0_is_inert` pins the boundary value directly rather than the shipped
default, so this file's own meaning survives the next default change too.
"""
import os
import sys

import pytest

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

from systems.mass_battle.sim.config import ROUT_CASCADE_FRAC
from systems.mass_battle.sim.engine import build_army, SIDE_A_START_ROW


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


def test_threshold_1_0_is_inert():
    """1.0 must always reproduce `all(a.routed ...)` exactly — the property the mechanism generalises
    from, independent of whatever value is currently shipped as the default.

    [A8, ED-MB-0067 Part A / ED-MB-0071, 2026-09-27] This test previously asserted
    `ROUT_CASCADE_FRAC == 1.0` and read the module's live default directly, i.e. it tested "the
    shipped default is inert" rather than "1.0 is inert" — true only as long as those two things
    happened to be the same value. They no longer are: the sweep (workbench/rout_cascade_sweep.py)
    chose 0.5, which is DELIBERATELY not inert (that is the whole finding — see config.py's own
    comment on the constant). Rewritten to pin the boundary value explicitly, the same pattern
    `test_a_lowered_threshold_breaks_the_army_early` immediately below already uses, so this test
    keeps meaning "1.0 is inert" regardless of any future default change."""
    import systems.mass_battle.sim.hierarchy.units as U
    u = _unit(3)
    u.subunits[0].routed = True
    u.subunits[1].routed = True
    orig = U.ROUT_CASCADE_FRAC
    try:
        U.ROUT_CASCADE_FRAC = 1.0
        u.derive_rout()
        assert not u.routed, "two of three broken must NOT break the army at threshold 1.0"
        u.subunits[2].routed = True
        u.derive_rout()
        assert u.routed, "the last section breaking must break the army"
    finally:
        U.ROUT_CASCADE_FRAC = orig


def test_shipped_default_is_no_longer_inert():
    """[A8, ED-MB-0067 Part A / ED-MB-0071] The new default (0.6) is deliberately NOT inert: this is
    the mechanism actually doing something, which is the point of the sweep. Companion to
    `test_threshold_1_0_is_inert` above — together they pin both ends of what changed.

    [CORRECTED 2026-09-27] The shipped value was briefly 0.5 (this test asserted that, and the
    boundary numbers below were unchanged either way — 0.5 and 0.6 both sit strictly between a
    3-subunit army's 1/3 and 2/3 breakpoints). Adversarial review found 0.5 under-evidenced once the
    sweep's own row set was corrected to include two previously-dropped rows (C4/C7): 0.6 achieves
    the identical casualty-realism gain with zero win-share-control cost, where 0.5 cost one row.
    See config.py's own comment on the constant for the full comparison."""
    assert ROUT_CASCADE_FRAC == 0.6, (
        "this test's own assertions below assume the shipped default; if it changed again, that's "
        "fine, but re-derive the numbers here rather than silently reinterpreting them")
    u = _unit(3)
    u.subunits[0].routed = True
    u.derive_rout()
    assert not u.routed, "one of three broken (share 1/3) must NOT break the army at threshold 0.6"
    u.subunits[1].routed = True
    u.derive_rout()
    assert u.routed, "two of three broken (share 2/3) must break the army at threshold 0.6"


def test_a_two_body_army_at_exactly_half_does_not_cascade_at_the_shipped_default():
    """[R11, adversarial review round 1] The exact-half boundary this test's own module docstring
    names as the hazard to pin (float-equality on `>=`) was never actually exercised for a body count
    where the break happens to land AT the threshold. An even split is the case that matters: a
    2-subunit army's single break is share EXACTLY 0.5 — strictly BELOW the shipped 0.6 default (0.6
    was chosen over 0.5 specifically because 0.5's exact-half hit was pulling the gauge's H5 row out
    of its win-share band; see config.py's own comment) — so it must NOT cascade at 0.6, where it
    WOULD have at 0.5. Also the asymmetry the review flagged: a body count's breakpoint fraction
    depends on ITS OWN split, not on the threshold alone — a 2-equal-body army needs BOTH broken
    (share 1.0) to reach 0.6, while a 3-equal-body army needs only 2 of 3 (~0.667). This test pins the
    shipped default's one genuinely marginal case: an even split landing exactly at the share the
    earlier, rejected 0.5 candidate would have caught."""
    u = _unit(2)
    u.subunits[0].routed = True
    assert u._broken_share() == 0.5
    u.derive_rout()
    assert not u.routed, "one of two equal bodies broken (share exactly 0.5) must NOT cascade at 0.6"
    u.subunits[1].routed = True
    u.derive_rout()
    assert u.routed, "both bodies broken (share 1.0) must cascade at any threshold in (0, 1]"


def test_a_lowered_threshold_breaks_the_army_early():
    """The mechanism itself: below 1.0, a decisive portion breaking is enough."""
    import systems.mass_battle.sim.hierarchy.units as U
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
