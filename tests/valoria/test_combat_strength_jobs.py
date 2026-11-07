"""PC-20, ED-IN-0347 (AR-10, AR-12): Strength's jobs in personal combat, one swept coefficient per commit.

(1) Damage by weapon head. `core.strike_impact = K_STR_HEAD[head]*strength + heft`, additive (ED-1040's reverted
multiplicative form is not reintroduced): a blunt head turns Strength into damage most fully, a point least, an edge
between. Every head at 1.0 is the control and reproduces the pre-PC-20 `strength + heft`.

Falsifier (CLAUDE.md §0.1 pt 3), run at the build: `K_STR_HEAD[weapon_head]*` deleted from `strike_impact` reddens
`test_a_blunt_head_gains_more_damage_per_strength_point_than_a_point` and
`test_the_point_damage_gain_from_strength_falls_through_strike` (the slopes come out equal); with it present and every
head at 1.0 the control tests stay green (`test_all_ones_is_the_pre_item_impact`).

(2) The weapon's weight. `combat_systems.str_demand` adds `D_MASS*mass` (kg) beside the swing inertia `wield_heft`
already carries, so a heavier weapon of equal inertia handles worse for a fighter short of its demand. D_MASS = 0 is
the control.

Falsifier, run at the build: `+cfg['D_MASS']*w['mass']` deleted from `str_demand` reddens
`test_a_heavier_weapon_of_equal_inertia_handles_worse_for_a_weaker_fighter` (the twin and the greatsword handle
alike) and the shipped-minus-control half of `test_d_mass_zero_is_the_pre_item_demand` (the demand no longer moves
by D_MASS*mass); with it present and D_MASS = 0 the twin and the greatsword read one demand bitwise.

(3) The harness. `combat_systems.act_cost` adds `ACT_WEIGHT/D_WT * max(0, ARMOR_DEMAND[armor] - strength)` (AR-10,
adj §3.1 (8): handling_penalty's form, a Strength shortfall against a demand, paid in stamina at the price of a unit
of weapon heft), so an armoured weak fighter tires faster than an unarmoured one. Every tier at 0 is the control.

Falsifier, run at the build: the shortfall term deleted from `act_cost` reddens
`test_an_armoured_weak_fighter_tires_faster_than_an_unarmoured_one` and
`test_a_weak_fighter_in_heavy_armour_runs_dry_in_fewer_acts`; with it present and every tier at 0 those two and
`test_every_armour_tier_has_a_demand_rising_with_the_tier` are red and the control test green."""
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'modules', 'combat')
sys.path.insert(0, ENGINE)

import combat_systems as S  # noqa: E402
import core  # noqa: E402
from combatant import WEAPONS, Combatant  # noqa: E402
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


# ── (2) the weapon's weight in the Strength demand ──────────────────────────────────────────────────────────────────
TWIN = 'pc20_heavy_twin'


@pytest.fixture
def heavy_twin(monkeypatch):
    """A greatsword record half again as HEAVY with the same parts: the greatsword's derived inertia (wield_heft),
    balance (WP.handling), reach and rear clearance read its parts, not its `mass` field, so the twin is a heavier
    weapon of EQUAL inertia. The fixture asserts that premise rather than assuming it."""
    base = WEAPONS['greatsword']
    monkeypatch.setitem(WEAPONS, TWIN, dict(base, mass=base['mass'] * 1.5))
    a, b = Combatant('light', weapon='greatsword'), Combatant('heavy', weapon=TWIN)
    assert S.wield_heft(a, CFG) == S.wield_heft(b, CFG)
    assert S.WP.handling(a.w) == S.WP.handling(b.w)
    assert S.reach_base(a, CFG) == S.reach_base(b, CFG)
    assert S.rear_clearance(a, CFG) == S.rear_clearance(b, CFG)
    assert b.w['mass'] > a.w['mass']
    return base['mass'], base['mass'] * 1.5


def _penalty(weapon, strength, cfg, fat=0.0):
    return S.handling_penalty(Combatant('x', attrs={'strength': strength}, weapon=weapon), fat, cfg)


def test_a_heavier_weapon_of_equal_inertia_handles_worse_for_a_weaker_fighter(heavy_twin):
    """The EXIT: a weak fighter (in deficit on both) handles the heavier twin worse, by HANDLE_K*D_MASS per kg; a
    strong fighter (in deficit on neither) handles the two alike — weight is a Strength job, not a flat tax."""
    assert CFG['D_MASS'] > 0.0, CFG['D_MASS']
    light, heavy = heavy_twin
    checked = 0
    for s in (1, 2, 3):
        assert S.str_demand(Combatant('x', attrs={'strength': s}, weapon=TWIN), CFG) - s > 0.0   # in deficit on both
        lp, hp = _penalty('greatsword', s, CFG), _penalty(TWIN, s, CFG)
        assert hp > lp, s
        assert hp - lp == pytest.approx(CFG['HANDLE_K'] * CFG['D_MASS'] * (heavy - light), abs=1e-12), s
        checked += 1
    assert checked == 3
    strong = 12
    assert S.str_demand(Combatant('x', attrs={'strength': strong}, weapon=TWIN), CFG) < strong
    assert _penalty('greatsword', strong, CFG) == _penalty(TWIN, strong, CFG)


def test_d_mass_zero_is_the_pre_item_demand(heavy_twin):
    """CONTROL: at D_MASS = 0 mass has no channel into the demand — the heavier twin reads the greatsword's demand
    bitwise (the planted failure: the exit reads false) — and every roster weapon's demand moves by exactly
    D_MASS*mass between the control and the shipped value."""
    off = dict(CFG, D_MASS=0.0)
    for s in (1, 2, 3, 4):
        assert _penalty('greatsword', s, off) == _penalty(TWIN, s, off), s
    checked = 0
    for k in sorted(WEAPONS):
        if k == TWIN:
            continue
        c = Combatant('x', weapon=k)
        assert S.str_demand(c, CFG) - S.str_demand(c, off) == pytest.approx(CFG['D_MASS'] * c.w['mass'], abs=1e-12), k
        checked += 1
    assert checked >= 50


# ── (3) the harness's Strength demand, paid in stamina ──────────────────────────────────────────────────────────────
TIERS = (V.TIER_NONE, V.TIER_LIGHT, V.TIER_MEDIUM, V.TIER_HEAVY)
ARMOURED = TIERS[1:]


def _act(strength, armor, cfg, weapon='arming', commit=3.0):
    return S.act_cost(Combatant('x', attrs={'strength': strength}, weapon=weapon, armor=armor), commit, cfg)


def _pre_item_act(c, commit, cfg):
    """The PC-20 (2) per-act stamina cost, written out: no armour channel."""
    return (cfg['ACT_BASE'] + cfg['ACT_WEIGHT'] * S.wield_heft(c, cfg) + cfg['ACT_COMMIT'] * commit) * cfg['COST_SCALE']


def test_every_armour_tier_has_a_demand_rising_with_the_tier():
    """A tier missing from the table would KeyError in act_cost; 'none' demands nothing; the demand rises with the
    tier, and the strongest fighter on the scale (7) bears every tier free (else the harness is a flat tax)."""
    d = CFG['ARMOR_DEMAND']
    assert set(d) == set(V.ARMOUR_TIERS)
    assert d[V.TIER_NONE] == 0.0
    ladder = [d[t] for t in TIERS]
    assert all(lo < hi for lo, hi in zip(ladder, ladder[1:])), ladder
    assert d[V.TIER_HEAVY] <= 7, d


def test_an_armoured_weak_fighter_tires_faster_than_an_unarmoured_one():
    """The EXIT: a fighter short of a tier's demand pays more stamina per act in it than out of armour, by the
    shortfall priced at a unit of heft (COST_SCALE*ACT_WEIGHT/D_WT per Strength point); a fighter at or over the
    demand pays the same in it as out of it — the harness is a Strength job, not a flat tax."""
    k = CFG['COST_SCALE'] * CFG['ACT_WEIGHT'] / CFG['D_WT']
    checked = 0
    for tier in ARMOURED:
        demand = CFG['ARMOR_DEMAND'][tier]
        for s in range(1, 8):
            for weapon in ('dagger', 'arming', 'greatsword'):
                gap = _act(s, tier, CFG, weapon) - _act(s, V.TIER_NONE, CFG, weapon)
                if s < demand:
                    assert gap > 0.0, (tier, s, weapon)
                    assert gap == pytest.approx(k * (demand - s), abs=1e-12), (tier, s, weapon)
                    checked += 1
                else:
                    assert gap == 0.0, (tier, s, weapon)
    assert checked >= 3 * len(ARMOURED)   # every armoured tier is short for at least the weakest fighter


def test_a_weak_fighter_in_heavy_armour_runs_dry_in_fewer_acts():
    """The exit read as the wrapper spends it (`aggressor.stamina -= S.act_cost(...)`, wrapper.engagement): from a
    full reserve, a Strength-1 fighter in plate reaches zero stamina in fewer acts than the same fighter unarmoured,
    and a Strength-7 fighter does so in the same number either way."""
    def acts_to_empty(strength, armor):
        c = Combatant('x', attrs={'strength': strength}, weapon='arming', armor=armor)
        stamina, acts = float(c.stamina_max), 0
        while stamina > 0:
            stamina -= S.act_cost(c, 4.0, CFG)
            acts += 1
        return acts
    assert acts_to_empty(1, V.TIER_HEAVY) < acts_to_empty(1, V.TIER_NONE)
    assert acts_to_empty(7, V.TIER_HEAVY) == acts_to_empty(7, V.TIER_NONE)


def test_armour_demand_zero_is_the_pre_item_cost():
    """CONTROL: every tier at 0 reproduces the PC-20 (2) per-act cost bitwise, in every tier at every Strength (the
    planted failure: armour then costs a weak fighter nothing, so the exit reads false)."""
    off = dict(CFG, ARMOR_DEMAND={t: 0.0 for t in TIERS})
    checked = 0
    for tier in TIERS:
        for s in (1, 2, 4, 7):
            for weapon in ('dagger', 'arming', 'greatsword', 'guandao'):
                for commit in (2.0, 3.5, 5.0):
                    c = Combatant('x', attrs={'strength': s}, weapon=weapon, armor=tier)
                    assert S.act_cost(c, commit, off) == _pre_item_act(c, commit, off), (tier, s, weapon, commit)
                    checked += 1
    assert checked == 4 * 4 * 4 * 3
    assert _act(1, V.TIER_HEAVY, off) == _act(1, V.TIER_NONE, off)
