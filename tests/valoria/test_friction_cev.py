"""DG-6 resolution acceptance: per-battle combat-effectiveness (CEV) friction restores scale-invariant
outcome variance (ED-MB-0016).

The melee pool sums N independent dice, so its coefficient of variation collapses as ~1/sqrt(N) — large
battles become near-deterministic and lopsided matchups resolve 100%/0% where history shows bands. The
fix (config.PC_FRICTION_CEV) multiplies each side's combat pool by a per-BATTLE, per-side LogNormal
combat-effectiveness factor drawn ONCE per battle (Dupuy CEV / Clausewitzian friction), whose variance is
force-INDEPENDENT — so a large advantage stays decisive-but-uncertain (banded) rather than certain.
Grounding + calibration: audit/2026-07-22-mass-battle-stress-test/dg6_friction_resolution.md.

This file pins the MECHANISM (not the gauge bands, which are validated separately): default-inert /
byte-exact when off; drawn once per battle (not per turn); scale-invariant (a 2:1 matchup does NOT
approach 100% as troop count grows once friction is on); deterministic (I2); conservation (I1).
"""
import math
import os
import statistics
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))  # tests/sim on path

import pytest  # noqa: E402

import mass_battle.config as _cfg  # noqa: E402
import mass_battle.core.exchange as _exch  # noqa: E402
import mass_battle.hierarchy.units as _hu  # noqa: E402
import mass_battle.orchestration as _orch  # noqa: E402
from mass_battle.engine import build_unit, build_army  # noqa: E402
from mass_battle import validators as _val  # noqa: E402


@pytest.fixture
def field_path():
    saved = [(m, m.FIELD_MOVEMENT, m.PC_NODE_COHESION) for m in (_hu, _orch)]
    _val._set_movement_path('node')
    try:
        yield
    finally:
        for m, fm, nc in saved:
            m.FIELD_MOVEMENT = fm
            m.PC_NODE_COHESION = nc


@pytest.fixture
def friction(field_path):
    """Enable PC_FRICTION_CEV across the modules that read it (config is star-imported), restore after."""
    mods = [_cfg, _exch, _orch]
    saved = [(m, getattr(m, 'PC_FRICTION_CEV', False), getattr(m, 'PC_FRICTION_SIGMA', 1.1)) for m in mods]
    for m in mods:
        if hasattr(m, 'PC_FRICTION_CEV'):
            m.PC_FRICTION_CEV = True
    try:
        yield
    finally:
        for m, cev, sig in saved:
            if hasattr(m, 'PC_FRICTION_CEV'):
                m.PC_FRICTION_CEV = cev
                m.PC_FRICTION_SIGMA = sig


def _unit_troops(u):
    return sum(sum(s.cell_troops.values()) for s in u.subunits)


def _ratio_winrate(ratio, base, n, seed0=9000):
    """Attacker (A, `ratio`x troops) decisive win-rate over n seeded Line-vs-Line battles."""
    import random
    aw = bw = 0
    for s in range(n):
        random.seed(seed0 + s)
        a = build_army([{'shape': 'Line', 'troops': int(base * ratio), 'concentration': 100}], 'A', 'A')
        b = build_army([{'shape': 'Line', 'troops': base, 'concentration': 100}], 'B', 'B')
        r = _orch.run_multi_turn_battle(a, b, 'Line', 'Line', {'A': 9, 'B': 9}, max_battle_turns=20)
        w = r.get('winner')
        if w == 'A':
            aw += 1
        elif w == 'B':
            bw += 1
    dec = aw + bw
    return 100.0 * aw / dec if dec else 50.0


# ─── default-inert (byte-exact when off) ─────────────────────────────────────

def test_default_off_is_inert(field_path):
    """PC_FRICTION_CEV defaults OFF: _draw_friction_cev sets the factor to exactly 1.0 (no pool change),
    so the mechanism is byte-exact / behaviourless until explicitly enabled."""
    assert _cfg.PC_FRICTION_CEV is False, "friction must default OFF (grid-oracle / byte-exact safety)"
    a = build_unit('Line', 3, 'A', 'A', 9)
    _orch._draw_friction_cev(a)
    assert a._friction_cev == 1.0


# ─── drawn ONCE per battle, not per turn ─────────────────────────────────────

def test_drawn_once_per_battle(friction):
    """The friction factor is a per-BATTLE latent: a fresh unit draws it exactly once, and a second
    _draw_friction_cev call (as happens on every turn of a multi-turn battle) does NOT redraw it.
    (Per-turn redraws would self-average the shock away — the very thing this restores.)"""
    import random
    random.seed(1)
    a = build_unit('Line', 3, 'A', 'A', 9)
    _orch._draw_friction_cev(a)
    first = a._friction_cev
    assert first != 1.0  # a real LogNormal draw (prob. 1)
    _orch._draw_friction_cev(a); _orch._draw_friction_cev(a)
    assert a._friction_cev == first, "friction redrawn within a battle -> variance would self-average away"


def test_lognormal_positive_zero_mean_log(friction):
    """The factor is LogNormal(0, sigma): strictly positive, and log-symmetric about 0 (mean of log ~ 0
    — neither side is advantaged in expectation of log-effectiveness). Tested on log (the sample median
    of a heavy-tailed LogNormal is noisy; mean-of-log is the robust check, SE = sigma/sqrt(n))."""
    import random
    random.seed(7)
    logs = []
    for i in range(400):
        u = build_unit('Line', 3, 'A', 'A', 9)
        u._friction_cev = None
        _orch._draw_friction_cev(u)
        assert u._friction_cev > 0
        logs.append(math.log(u._friction_cev))
    assert abs(statistics.mean(logs)) < 0.15   # ~ mu = 0, well within ~3 SE (1.1/sqrt(400)=0.055)


# ─── the core property: scale-invariant outcome variance ─────────────────────

def test_variance_does_not_collapse_at_scale(friction):
    """THE fix, tested at scale. Without friction, a 2:1 matchup's win-rate collapses to ~certainty
    (~100%) as troop count grows — the 1/sqrt(N) attrition self-averaging that IS the DG-6 over-
    decisiveness. WITH friction, the once-per-battle shock keeps a force-INDEPENDENT variance component,
    so even at LARGE troop counts the 2:1 win-rate stays BANDED (well below certainty) rather than
    approaching 100%. Assert the mechanism (banded, not the exact band — that is the gauge's job)."""
    base = 1600   # a large force where attrition has fully self-averaged
    on = _ratio_winrate(2.0, base, n=40)
    for m in (_cfg, _exch, _orch):
        if hasattr(m, 'PC_FRICTION_CEV'):
            m.PC_FRICTION_CEV = False
    off = _ratio_winrate(2.0, base, n=40)
    for m in (_cfg, _exch, _orch):
        if hasattr(m, 'PC_FRICTION_CEV'):
            m.PC_FRICTION_CEV = True
    assert off >= 95.0, f"large-force 2:1 should collapse to ~certain without friction ({off}%) — the DG-6 defect"
    assert on < 90.0, f"friction failed to band the large-force 2:1 ({on}%) — variance collapsed at scale"
    assert off - on >= 10.0, f"friction barely moved the large-force outcome ({off}->{on}%)"


def test_friction_reduces_decisiveness(friction):
    """Directly A/B the mechanism: enabling friction lowers a lopsided matchup's win-rate away from
    certainty (toward the historical band)."""
    on = _ratio_winrate(2.0, 400, n=40)
    # turn it off within this test and compare
    for m in (_cfg, _exch, _orch):
        if hasattr(m, 'PC_FRICTION_CEV'):
            m.PC_FRICTION_CEV = False
    off = _ratio_winrate(2.0, 400, n=40)
    for m in (_cfg, _exch, _orch):
        if hasattr(m, 'PC_FRICTION_CEV'):
            m.PC_FRICTION_CEV = True
    assert off > on, f"friction OFF ({off}%) should be MORE decisive than ON ({on}%)"
    assert off >= 90.0, f"baseline 2:1 should be over-decisive ({off}%) — the DG-6 defect"


# ─── I1 / I2 with friction on ────────────────────────────────────────────────

def test_conservation_with_friction(friction):
    import random
    random.seed(2026)
    a = build_unit('Line', 3, 'A', 'A', 9)
    b = build_unit('Line', 3, 'B', 'B', 9)
    _orch.run_battle(a, b, max_turns=18)
    for u in (a, b):
        if u.routed or u.broken:
            continue
        assert math.isclose(_unit_troops(u), u.hp, rel_tol=1e-6, abs_tol=1e-3)


def test_determinism_with_friction(friction):
    import random

    def _run():
        random.seed(414)
        a = build_unit('Line', 3, 'A', 'A', 9)
        b = build_unit('Line', 3, 'B', 'B', 9)
        r = _orch.run_battle(a, b, max_turns=18)
        return (r['winner'], r['turns'], round(a.hp, 6), round(b.hp, 6),
                round(a._friction_cev, 6), round(b._friction_cev, 6))

    assert _run() == _run()
