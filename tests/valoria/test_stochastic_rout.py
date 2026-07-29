"""ED-MB-0031 — stochastic rout breakpoint at the historical 15-30% casualty band
(Jordan historical research 2026-07-23: "routs would occur as early as 15% losses with 30% the
upper hand"). Verifies the break-point draw lands in the band, resilience skews it, a subunit routs
once its casualties cross it, the loser now breaks near the historical band (not ~90%), and it is
inert/byte-exact when gated off.

[ED-MB-0041, 2026-07-25] The DEFAULT IS NOW ON. It shipped OFF, and the casualty scoreboard measured
what that cost: the loser reached 61-87% casualties on every gauge row against this band's own 15-30%
expectation. Turning it on gives 29-41%. The flip drops the win-share count 10/20 -> 7/20 and is still
correct — see config.py's note at the flag. The on/off toggle below is unchanged and still exercises
both paths; only the assertion about which way it points has moved.
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


def test_default_is_on():
    """[ED-MB-0041] Ratified ON. This assertion previously read `is False`.

    It was not wrong when written — the flag moved the goldens, so gating it off kept them stable. What
    changed is the evidence: with the casualty scoreboard in place, OFF measurably means the loser is
    annihilated (61-87%) against this very band's 15-30% claim. A test that pins a default is pinning a
    DECISION, so when the decision is re-made on evidence the test moves with it — and says why, rather
    than being quietly deleted.
    """
    assert C.PC_STOCHASTIC_ROUT is True, (
        "stochastic rout is ratified ON (ED-MB-0041): OFF leaves the loser at 61-87% casualties against "
        "the 15-30% band this module tests. Reversible via PC_STOCHASTIC_ROUT=0.")


def test_band_is_historical():
    assert C.ROUT_ONSET_FRAC == pytest.approx(0.15)
    assert C.ROUT_CAP_FRAC == pytest.approx(0.30)


def test_breakpoint_in_band():
    random.seed(12345)
    for disc in (2, 3, 4, 5):
        su = _unit('A', disc=disc).subunits[0]
        assert getattr(su, '_rout_breakpoint', None) is None
        S._stochastic_break(su, 0.0)  # draws the break-point lazily
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
            S._stochastic_break(su, 0.0)
            bps.append(su._rout_breakpoint)
        return statistics.mean(bps)
    assert mean_bp(5) > mean_bp(2) + 0.01, "disciplined units must break later on average"


def test_break_fires_when_casualties_cross():
    su = _unit('A', disc=5).subunits[0]
    su._rout_breakpoint = 0.20  # pin a known break-point
    assert S._stochastic_break(su, 0.10) is False   # 10% losses -> below the point -> no break
    assert S._stochastic_break(su, 0.25) is True    # 25% losses -> past the point -> break


def _mean_loser_casualties(on, n=16, cells=False):
    """`cells` controls PC_CELL_MORALE, which must be pinned rather than inherited — see
    test_loser_breaks_near_historical_band and test_per_cell_break_subsumes_the_body_level_one."""
    import mass_battle.hierarchy.units as U
    prev = S.PC_STOCHASTIC_ROUT
    prev_cells = U.PC_CELL_MORALE
    S.PC_STOCHASTIC_ROUT = on
    U.PC_CELL_MORALE = cells       # read by Subunit.__post_init__ to decide whether to seed cells
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
        U.PC_CELL_MORALE = prev_cells


def test_loser_breaks_near_historical_band():
    """With the gate ON the loser breaks far earlier than the ~90% grind — into/near the 15-30% band.

    Pinned to PC_CELL_MORALE=OFF, and that pin is the point: this test measures the BODY-LEVEL
    break-point, and per-cell morale supplies its own break-point one scale down. Were per-cell
    morale on, the OFF arm would already be broken by the cells and this would read as a no-op — see
    test_per_cell_break_subsumes_the_body_level_one, which asserts exactly that and is the reason for
    the pin rather than a separate curiosity.

    [ED-MB-0045 S7, corrected 2026-07-29] This docstring used to describe per-cell morale as "default
    ON since 2026-07-25". **That is false.** The flip was RETRACTED the same day it landed (the
    confounded measurement that produced CLAUDE.md §0.1), and `config.py:100` reads
    `PC_CELL_MORALE = environ.get('PC_CELL_MORALE', '0') == '1'   # RETRACTED to OFF 2026-07-25`.
    The pin here therefore matches the shipped default rather than departing from it — which changes
    nothing about the pin's correctness, but the reason given for it was wrong.
    """
    off = _mean_loser_casualties(False, cells=False)
    on = _mean_loser_casualties(True, cells=False)
    assert off > 60.0, f"baseline should grind to high casualties (got {off:.1f})"
    assert on < 45.0, f"stochastic rout must break the loser far earlier (got {on:.1f})"
    assert on < off - 30.0


def test_per_cell_break_subsumes_the_body_level_one():
    """[ED-MB-0042] With cells carrying their own break-points, the body-level flag stops mattering.

    Measured 2026-07-25: with PC_CELL_MORALE ON, the loser reaches ~35.6% casualties with stochastic
    body-rout OFF and ~36.1% with it ON — no separation at all. The cells break first (each drawing from
    the same 15-30% band, discipline-skewed) and CELL_BREAK_ROUT_FRAC ends the body before the
    subunit-level draw is ever consulted.

    This is recorded rather than quietly acted on. Read it for exactly what it measures: a CONDITIONAL
    about the arm this test pins ON, `PC_CELL_MORALE=1`.

    [ED-MB-0045 S7, corrected 2026-07-29] This paragraph used to conclude that PC_STOCHASTIC_ROUT "is
    now inert in the SHIPPED configuration ... so it is a retirement CANDIDATE". **That is false, and
    inverted.** It inherited the same mistaken premise as the docstring above — that per-cell morale
    ships ON. It does not (`config.py:100`, default `'0'`, RETRACTED 2026-07-25). In the SHIPPED
    configuration `atom.cell_morale` is empty, so the entire per-cell break block at
    `core/state.py:137-149` (`check_cell_breaks` / `propagate_cell_breaks` / `cohere_cells` /
    `CELL_BREAK_ROUT_FRAC`) is skipped, and `PC_STOCHASTIC_ROUT` at `core/state.py:150` — itself
    defaulted ON (`config.py:167`) — is the ONLY early break-point the engine ships. Far from being a
    retirement candidate, it is the single mechanism keeping shipped battles out of the ~90% grind;
    the subsumption measured below is what WOULD happen if the cell flag were flipped back on, which
    is why it is worth pinning, not evidence that the body-level flag is dead.
    """
    off = _mean_loser_casualties(False, cells=True)
    on = _mean_loser_casualties(True, cells=True)
    assert abs(on - off) < 10.0, (
        f"per-cell breaks should already be doing this work (off {off:.1f} vs on {on:.1f}); if these "
        f"have separated again, the cell break-point has stopped firing before the body-level one")
    assert off < 45.0, f"cells alone must break the loser well short of the grind (got {off:.1f})"
