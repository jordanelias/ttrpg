"""Spatial-model v2 Stage E acceptance: weapon-class reach wired to the front face + the pike type.

Stage E (ED-MB-0014, Jordan P-DEC-1) replaces the flat REACH_SHORT=0.5 placeholder that Stages B/C
carried with the ruled per-troop-type front-face reach: non-pole melee 0.1, pole/spear 0.2, PIKE 0.3,
cavalry/knights lance 0.2, ranged = projectile band + 0.1 melee sidearm. It also authors a `pike`
troop type (stats mirror heavy_infantry so reach 0.3 is the sole differentiator; pike weapon + roles).

The reach values feed geometry.obb_front_reach_overlap (contact, Stage B) and resolve_toi_and_commit
(the TOI halt, Stage C). Two measured facts this file pins:

  * The reach ADVANTAGE emerges through the already-wired charge-recoil reach gate
    (PC_RECOIL_CHARGER_GATE: a braced defender whose reach >= the charger's reach repels the charge;
    a shorter-reach defender does not). Before Stage E every troop shared reach 0.5, so the gate fired
    for everyone; with the differentiated values it is CONDITIONAL — pike (0.3) and spear/heavy_infantry
    (0.2) stop a cavalry lance (0.2), levy (0.1) does not. This is the historically-correct anti-cavalry
    role of the pike, emergent from the reach data, not a special case.
  * Standing melee is UNCHANGED by reach differentiation (the exchange is symmetric-mutual once contact
    fires; reach only shifts WHEN contact fires) — a disclosed finding, documented here so a future
    reader knows reach is a charge/brace lever, not a standing-melee one, in this engine.

Facing-away cells get no reach bonus (I7); ranged volley range is reach-independent (VOLLEY_MAX_RANGE).
Deterministic + seeded; movement toggles saved/restored in the field_path fixture.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))  # tests/sim on path

import pytest  # noqa: E402

import mass_battle.hierarchy.units as _hu  # noqa: E402
import mass_battle.orchestration as _orch  # noqa: E402
import mass_battle.troop_types.registry as _reg  # noqa: E402
from mass_battle.troop_types.registry import reach_for, stats_for, unit_type_for  # noqa: E402
from mass_battle.equipment import loadout_for  # noqa: E402
from mass_battle.engine import build_unit  # noqa: E402
from mass_battle import validators as _val  # noqa: E402
from mass_battle.config import FOV_HALF_DEG, VOLLEY_MAX_RANGE  # noqa: E402


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


def _unit_troops(unit):
    return sum(sum(su.cell_troops.values()) for su in unit.subunits)


# ─── the P-DEC-1 reach map ────────────────────────────────────────────────────

def test_reach_by_weapon_class():
    """Jordan P-DEC-1: non-pole melee 0.1, pole/spear 0.2, PIKE 0.3, lance (cavalry/knights) 0.2,
    ranged + 0.1 melee sidearm. Bare 'infantry' (engine default) and any unmapped type -> 0.1."""
    assert reach_for('levy') == 0.1
    assert reach_for('light_infantry') == 0.1
    assert reach_for('heavy_infantry') == 0.2
    assert reach_for('pike') == 0.3
    assert reach_for('cavalry') == 0.2
    assert reach_for('knights_templar') == 0.2
    assert reach_for('archers') == 0.1 and reach_for('crossbow') == 0.1
    assert reach_for('infantry') == 0.1          # bare engine default
    assert reach_for('totally_unknown') == 0.1   # fallthrough = non-pole melee
    assert reach_for(None) == 0.1
    # pike is the strict longest melee reach
    assert reach_for('pike') > reach_for('heavy_infantry') > reach_for('levy')


def test_pike_troop_type_authored():
    """The pike troop type exists end-to-end: stats (mirror heavy_infantry), a pike weapon (pole,
    melee), and defensive/anti-cavalry roles."""
    s = stats_for('pike')
    assert s == stats_for('heavy_infantry'), "pike stats should mirror heavy_infantry (reach is the differentiator)"
    weapon, armour = loadout_for('pike')
    assert weapon is not None and weapon.get('reach') == 'melee'
    assert 'pole' in (weapon.get('keywords') or ())
    assert unit_type_for('pike') == 'melee'
    assert _reg.role_allowed('pike', 'ShieldWall') and _reg.role_allowed('pike', 'Anvil')


# ─── the reach ADVANTAGE (charge-recoil reach gate) ──────────────────────────

def _charge_vs_brace(def_type, n=16):
    """Braced defender of `def_type` holding vs a Fast cavalry charge; returns mean defender hp retained."""
    import random
    tot = 0.0
    for s in range(n):
        random.seed(700 + s)
        d = build_unit('Line', 3, 'DEF', 'A', 9, troop_type=def_type, stance='hold',
                       instructions=('brace', 'hold'))
        c = build_unit('Line', 3, 'CAV', 'B', 9, troop_type='cavalry', speed='Fast',
                       instructions=('charge',))
        h0 = d.hp
        _orch.run_battle(d, c, max_turns=18)
        tot += d.hp / h0
    return tot / n


def test_pike_reach_advantage_vs_cavalry(field_path):
    """The reach advantage EMERGES: a pike wall (reach 0.3 >= cavalry lance 0.2) repels the charge and
    retains materially more troops than a levy line (reach 0.1 < 0.2, charge lands). Spear/heavy_infantry
    (0.2 == 0.2) also stops it. This is the recoil gate made CONDITIONAL by the differentiated reach —
    the anti-cavalry pike role, emergent from the reach data."""
    pike_hp = _charge_vs_brace('pike')
    levy_hp = _charge_vs_brace('levy')
    heavy_hp = _charge_vs_brace('heavy_infantry')
    assert pike_hp > levy_hp + 0.02, f"pike ({pike_hp:.4f}) should out-retain levy ({levy_hp:.4f}) vs a charge"
    assert heavy_hp > levy_hp + 0.02, f"spear/heavy ({heavy_hp:.4f}) should out-retain levy ({levy_hp:.4f})"
    # pike (0.3) and heavy (0.2) both clear the lance (0.2), so both fully repel — near-equal
    assert math.isclose(pike_hp, heavy_hp, abs_tol=1e-6)


def test_standing_melee_reach_independent(field_path):
    """Disclosed finding: reach differentiation does NOT change symmetric standing melee (the exchange
    is mutual once contact fires; reach only shifts contact TIMING). pike-vs-levy standing == levy-vs-levy
    standing. Documents that reach is a charge/brace lever here, not a standing-melee one."""
    import random

    def _standing(ta, tb, n=12):
        ha = hb = 0.0
        for s in range(n):
            random.seed(500 + s)
            a = build_unit('Line', 3, 'A', 'A', 9, troop_type=ta)
            b = build_unit('Line', 3, 'B', 'B', 9, troop_type=tb)
            h0a, h0b = a.hp, b.hp
            _orch.run_battle(a, b, max_turns=18)
            ha += a.hp / h0a; hb += b.hp / h0b
        return round(ha / n, 4), round(hb / n, 4)

    assert _standing('pike', 'levy') == _standing('levy', 'levy')


# ─── I7: facing gate + ranged independence ───────────────────────────────────

def test_facing_away_gets_no_reach():
    """I7: a cell's weapon reach only threatens within its forward FOV arc. A cell facing +row gets its
    full reach against an enemy ahead, ZERO against one directly behind."""
    base = reach_for('pike')  # 0.3
    facing = (1.0, 0.0)       # facing +row
    ahead = _hu._effective_reach(base, facing, 1.0, 0.0)    # enemy ahead
    behind = _hu._effective_reach(base, facing, -1.0, 0.0)  # enemy directly behind
    assert ahead == base
    assert behind == 0.0
    # sanity: the FOV boundary is the documented gate
    assert FOV_HALF_DEG < 180.0


def test_ranged_volley_range_reach_independent():
    """Ranged units' projectile range is VOLLEY_MAX_RANGE, independent of the (melee sidearm) reach_for
    value — so shrinking archers' melee reach to 0.1 does not touch their volley reach."""
    assert unit_type_for('archers') == 'ranged'
    assert reach_for('archers') == 0.1          # melee sidearm only
    assert VOLLEY_MAX_RANGE > reach_for('archers')  # the projectile band is the governing range


# ─── I1 / I2 with a pike unit on the field path ──────────────────────────────

@pytest.mark.parametrize("seed", [3, 19, 44])
def test_conservation_with_pike(field_path, seed):
    """I1: Sum cell_troops == hp for every non-routed/broken unit at battle end, in a battle that
    actually fields the new pike type."""
    import random
    random.seed(seed)
    a = build_unit('Line', 3, 'PIKE', 'A', 9, troop_type='pike', instructions=('brace', 'hold'))
    b = build_unit('Line', 3, 'CAV', 'B', 9, troop_type='cavalry', speed='Fast', instructions=('charge',))
    _orch.run_battle(a, b, max_turns=18)
    for unit in (a, b):
        if unit.routed or unit.broken:
            continue
        assert math.isclose(_unit_troops(unit), unit.hp, rel_tol=1e-6, abs_tol=1e-3), \
            f"seed={seed} {unit.name}: {_unit_troops(unit)} != {unit.hp}"


def test_determinism_with_pike(field_path):
    import random

    def _run():
        random.seed(808)
        a = build_unit('Line', 3, 'PIKE', 'A', 9, troop_type='pike', instructions=('brace', 'hold'))
        b = build_unit('Line', 3, 'CAV', 'B', 9, troop_type='cavalry', speed='Fast', instructions=('charge',))
        res = _orch.run_battle(a, b, max_turns=18)
        return (res['winner'], res['turns'], round(a.hp, 6), round(b.hp, 6))

    assert _run() == _run()
