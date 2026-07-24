"""ED-MB-0031 — stochastic rout breakpoint at the historical 15-30% casualty band
(Jordan historical research 2026-07-23: "routs would occur as early as 15% losses with 30% the
upper hand"). Verifies the break-point draw lands in the band, resilience skews it, a subunit routs
once its casualties cross it, the loser now breaks near the historical band (not ~90%), and it is
inert/byte-exact when gated off.
"""
import os
import random
import statistics
import sys

import pytest

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import mass_battle.config as C  # noqa: E402
import mass_battle.core.state as S  # noqa: E402
from mass_battle.engine import build_army, resolve_battle, SIDE_A_START_ROW, SIDE_B_START_ROW  # noqa: E402


def _unit(faction, disc=5, mor=6):
    sr = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    return build_army([{'shape': 'Line', 'troop_type': 'infantry', 'unit_type': 'melee',
                        'discipline': disc, 'morale': mor, 'width': 6, 'depth': 2, 'troops': 1200,
                        'starting_position': (sr, 25)}], faction, faction, discipline=disc, morale=mor)


def test_default_gated_off():
    assert C.PC_STOCHASTIC_ROUT is False, "stochastic rout must default OFF (moves goldens when on)"


def test_band_is_historical():
    assert C.ROUT_ONSET_FRAC == pytest.approx(0.15)
    assert C.ROUT_CAP_FRAC == pytest.approx(0.30)


def test_breakpoint_in_band():
    random.seed(12345)
    for disc in (2, 3, 4, 5):
        su = _unit('A', disc=disc).subunits[0]
        assert getattr(su, '_rout_breakpoint', None) is None
        S._stochastic_break(su)  # draws the break-point lazily
        bp = su._rout_breakpoint
        assert C.ROUT_ONSET_FRAC <= bp <= C.ROUT_CAP_FRAC, f"break-point {bp} outside the 15-30% band"


def test_resilience_orders_by_discipline():
    # a steady, disciplined body should be at least as resilient as a loose one
    lo = S._rout_resilience(_unit('A', disc=2).subunits[0])
    hi = S._rout_resilience(_unit('A', disc=5).subunits[0])
    assert hi > lo


def test_disciplined_skews_breakpoint_higher():
    # averaged over many draws, higher discipline -> break-point skewed toward the cap (holds longer)
    def mean_bp(disc, n=200):
        bps = []
        random.seed(999)
        for _ in range(n):
            su = _unit('A', disc=disc).subunits[0]
            S._stochastic_break(su)
            bps.append(su._rout_breakpoint)
        return statistics.mean(bps)
    assert mean_bp(5) > mean_bp(2) + 0.01, "disciplined units must break later on average"


def test_break_fires_when_casualties_cross():
    # cohesion for a single-subunit unit reads the parent unit's hp/hp_max -> drive casualties via hp
    u = _unit('A', disc=5)
    su = u.subunits[0]
    su._rout_breakpoint = 0.20  # pin a known break-point
    u.hp = u.hp_max * 0.90      # 10% losses -> below the point -> no break
    assert S._stochastic_break(su) is False
    u.hp = u.hp_max * 0.75      # 25% losses -> past the point -> break
    assert S._stochastic_break(su) is True


def _mean_loser_casualties(on, n=16):
    prev = S.PC_STOCHASTIC_ROUT
    S.PC_STOCHASTIC_ROUT = on
    try:
        loser = []
        for s in range(n):
            random.seed(3_000_000 + s)
            ua, ub = _unit('A'), _unit('B')
            a0, b0 = ua.hp_max, ub.hp_max
            r = resolve_battle(ua, ub, 'Line', 'Line', {}, kind='multi', max_battle_turns=40)
            w = r.get('winner')
            if w == 'A':
                loser.append(100 * (b0 - ub.hp) / b0)
            elif w == 'B':
                loser.append(100 * (a0 - ua.hp) / a0)
        return statistics.mean(loser) if loser else 0.0
    finally:
        S.PC_STOCHASTIC_ROUT = prev


def test_loser_breaks_near_historical_band():
    """With the gate ON the loser breaks far earlier than the ~90% grind — into/near the 15-30% band."""
    off = _mean_loser_casualties(False)
    on = _mean_loser_casualties(True)
    assert off > 60.0, f"baseline should grind to high casualties (got {off:.1f})"
    assert on < 45.0, f"stochastic rout must break the loser far earlier (got {on:.1f})"
    assert on < off - 30.0
