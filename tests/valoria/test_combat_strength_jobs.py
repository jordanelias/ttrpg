"""PC-20, ED-IN-0347 (AR-10, AR-12): Strength's jobs in personal combat, one swept coefficient per commit.

(1) Damage by weapon head. `core.strike_impact = K_STR_HEAD[head]*strength + heft`, additive (ED-1040's reverted
multiplicative form is not reintroduced): a blunt head turns Strength into damage most fully, a point least, an edge
between. Every head at 1.0 is the control and reproduces the pre-PC-20 `strength + heft`.

Falsifier (CLAUDE.md §0.1 pt 3), run at the build: `K_STR_HEAD[weapon_head]*` deleted from `strike_impact` reddens
`test_a_blunt_head_gains_more_damage_per_strength_point_than_a_point` and
`test_the_point_damage_gain_from_strength_falls_through_strike` (the slopes come out equal); with it present and every
head at 1.0 the control tests stay green (`test_all_ones_is_the_pre_item_impact`)."""
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'modules', 'combat')
sys.path.insert(0, ENGINE)

import core  # noqa: E402
from combatant import Combatant  # noqa: E402
from config import CFG  # noqa: E402
import vocabulary as V  # noqa: E402

EDGE_HEADS = (V.HEAD_STRAIGHT_CUT, V.HEAD_CURVED_CUT, V.HEAD_CUT, V.HEAD_CUT_THRUST)
CONTROL = {h: 1.0 for h in V.HEADS}


@pytest.fixture
def control_k(monkeypatch):
    """Every head at 1.0: the pre-PC-20 tree."""
    monkeypatch.setattr(core, 'K_STR_HEAD', dict(CONTROL))


def _slope(head, heft=1.0, lo=2, hi=8):
    """Impact gained per Strength point, read off the owner."""
    return (core.strike_impact(hi, heft, head) - core.strike_impact(lo, heft, head)) / (hi - lo)


# ── (1) damage by weapon head ────────────────────────────────────────────────────────────────────────────────────
def test_every_head_token_has_a_weight():
    """A head missing from the table would KeyError in the damage path; an extra key would be read by nothing."""
    assert set(core.K_STR_HEAD) == set(V.HEADS)
    assert all(k > 0.0 for k in core.K_STR_HEAD.values()), core.K_STR_HEAD   # a point gets LESS from Strength, not none


def test_a_blunt_head_gains_more_damage_per_strength_point_than_a_point():
    """The EXIT: at equal Strength a blunt head gains more impact per Strength point than a point, and an edge lies
    between, at every heft and Strength the roster spans."""
    checked = 0
    for heft in (0.3, 1.0, 2.0):
        for lo, hi in ((1, 2), (2, 6), (4, 5), (6, 9)):
            b = _slope(V.HEAD_BLUNT, heft, lo, hi)
            p = _slope(V.HEAD_POINT, heft, lo, hi)
            for e in EDGE_HEADS:
                assert b > _slope(e, heft, lo, hi) > p, (heft, lo, hi, e)
            assert b == pytest.approx(core.K_STR_HEAD[V.HEAD_BLUNT], abs=1e-12)
            assert p == pytest.approx(core.K_STR_HEAD[V.HEAD_POINT], abs=1e-12)
            checked += 1
    assert checked == 12


def test_the_term_is_additive_not_multiplicative():
    """ED-1040: Strength's share does not scale with heft. The gain per Strength point is the same at every heft."""
    for head in V.HEADS:
        assert _slope(head, 0.3) == pytest.approx(_slope(head, 2.0), abs=1e-12), head


def test_all_ones_is_the_pre_item_impact(control_k):
    """CONTROL: every head at 1.0 reproduces the pre-PC-20 `strength + heft` for every head, bitwise, and the planted
    failure holds — at the control a blunt and a point gain the same per Strength point, so the exit reads false."""
    checked = 0
    for head in V.HEADS:
        for heft in (0.0, 0.5, 1.0, 2.5):
            for s in (0, 1, 2, 4, 7):
                assert core.strike_impact(s, heft, head) == s + core.strike_impact(0, heft, head), (head, heft, s)
                checked += 1
    assert checked == 6 * 4 * 5
    assert _slope(V.HEAD_BLUNT) == _slope(V.HEAD_POINT) == 1.0


def _poleaxe_damage(head, strength):
    """`core.strike` on a poleaxe holder whose selected head is `head` (the hammer is 'blunt', the spike 'point'),
    against an unarmoured defender at an overwhelming degree with no sigma tail: the call site, not the owner."""
    a = Combatant('a', attrs={'strength': strength}, weapon='poleaxe', armor='none')
    a.sel_head = head
    d = Combatant('d', weapon='arming', armor='none')
    return core.strike(a, d, 'overwhelming', CFG)


def test_the_point_damage_gain_from_strength_falls_through_strike(monkeypatch):
    """Through `core.strike` -> `damage` -> `strike_impact`: Strength 2 -> 9 adds as much damage to the hammer at the
    shipped weights as at the control (blunt is 1.0), and less to the spike."""
    def gain(head):
        return _poleaxe_damage(head, 9) - _poleaxe_damage(head, 2)
    shipped = {h: gain(h) for h in (V.HEAD_BLUNT, V.HEAD_POINT)}
    monkeypatch.setattr(core, 'K_STR_HEAD', dict(CONTROL))
    control = {h: gain(h) for h in (V.HEAD_BLUNT, V.HEAD_POINT)}
    assert control[V.HEAD_POINT] > 0 and control[V.HEAD_BLUNT] > 0, control
    assert shipped[V.HEAD_BLUNT] == control[V.HEAD_BLUNT], (shipped, control)
    assert shipped[V.HEAD_POINT] < control[V.HEAD_POINT], (shipped, control)
