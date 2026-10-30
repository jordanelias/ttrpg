"""ED-IN-0304 phase 1 -- a faction's ORDER OF BATTLE reaches the mass-battle engine.

`modules/mass_battle/orderofbattle.py` turns named subformations (troop type, size, role, stance) plus a strategy
into the multi-subunit Unit the engine fights, and `massbattle.resolve_field` takes one per side from the input
record's `orders_of_battle`. What this proves, and the control beside each claim:

  * THE CONTROL: a record with no orders of battle is the field as it was (the single headcount line), so the
    existing goldens still bind it -- compared against an explicit `(None, None)`, and `_weighted_unit` is the path.
  * THE FALSIFIER: two orders of battle of EQUAL headcount and different troop types fight differently. If the
    types never reached the engine the two would be identical on every seed.
  * Refusals at the boundary, deployment without overlap, strategy and tactic fields reaching the Subunit, and the
    new generic roster (spearmen, skirmishers, light cavalry) carrying what makes it a different type.
"""
import random

import pytest

from engine.season.queries.inputs import MassBattleInput
from modules.mass_battle import massbattle
from modules.mass_battle.config import TROOP_TYPE_ROLES
from modules.mass_battle.equipment import loadout_for
from modules.mass_battle.orderofbattle import (STRATEGIES, OrderOfBattle, Subformation, build_unit, class_of,
                                               validate)
from modules.mass_battle.troop_types.registry import (MOUNTED_TYPES, is_mounted, reach_for, stats_for,
                                                      support_ranks_for, unit_type_for)

SEEDS = tuple(range(40, 52))     # twelve: the engine's losses are one-sided per seed, so a type's effect shows in the aggregate


def _record(oobs=None, **kw):
    base = dict(weights=((10,), (10,)), territory=None, fort_level=0.0, stances=(0.0, 0.0), walls_dr=None,
                origin=None, loyalties=(0.0, 0.0), loyalty_gain=0, geography={})
    base.update(kw)
    return MassBattleInput(**base, **({} if oobs is None else {'orders_of_battle': oobs}))


def _oob(*parts, strategy='line'):
    return OrderOfBattle(tuple(Subformation(n, t, q, **kw) for n, t, q, kw in parts), strategy)


def _line(troop_type, n=1000):
    return _oob(('body', troop_type, n, {}))


# --------------------------------------------------------------------------------------- the control
def test_no_orders_of_battle_is_the_field_as_it_was():
    plain = massbattle.resolve_field(_record(), random.Random(5))
    explicit = massbattle.resolve_field(_record(oobs=(None, None)), random.Random(5))
    assert plain == explicit
    assert massbattle._weighted_unit("side_a", 10).subunits[0].troop_type == 'infantry', (
        "the control is vacuous if the headcount line stopped being the single infantry subunit")


# ------------------------------------------------------------------------------------- the falsifier
def _fight(oob_a, seed):
    return massbattle.resolve_field(_record(oobs=(oob_a, _line('heavy_infantry'))), random.Random(seed))


def _tally(troop_type):
    rs = [_fight(_line(troop_type), s) for s in SEEDS]
    assert len(rs) == len(SEEDS)
    return sum(r['attacker_wins'] for r in rs), sum(r['attacker_size_pct'] for r in rs) / len(rs)


def test_equal_headcount_of_different_troop_types_fights_differently():
    heavy_wins, heavy_kept = _tally('heavy_infantry')
    levy_wins, levy_kept = _tally('levy')
    assert (heavy_wins, heavy_kept) != (levy_wins, levy_kept), (
        "1000 heavy infantry and 1000 levy fought identically over twelve seeds: troop types never arrived")
    # and the direction is the stat table's (power 4 against power 1): the heavy line wins more and keeps more
    assert heavy_wins > levy_wins and heavy_kept > levy_kept
    assert heavy_kept < 1.0 and levy_kept < 1.0, "vacuous if neither line took a casualty (the lines never joined)"


def test_an_order_of_battle_side_and_a_headcount_side_both_deploy():
    """A side with no order of battle, once the other has one, is a deployed levy line, not a crash."""
    r = massbattle.resolve_field(_record(oobs=(_line('archers', 400), None), weights=((10,), (400,))),
                                 random.Random(3))
    assert set(r) >= {'attacker_wins', 'degree', 'attacker_size_pct', 'defender_size_pct'}


# ---------------------------------------------------------------------------------------- refusals
@pytest.mark.parametrize("bad, why", [
    (OrderOfBattle((), 'line'), "at least one"),
    (OrderOfBattle((Subformation('a', 'heavy_infantry', 10),), 'nope'), "unknown strategy"),
    (OrderOfBattle((Subformation('a', 'heavy_infantry', 10), Subformation('a', 'archers', 10))), "duplicate"),
    (OrderOfBattle((Subformation('a', 'dragons', 10),)), "no stat preset"),
    (OrderOfBattle((Subformation('a', 'heavy_infantry', 0),)), "positive"),
    (OrderOfBattle((Subformation('a', 'heavy_infantry', 10, role='Kite'),)), "menu"),
    (OrderOfBattle((Subformation('a', 'heavy_infantry', 10, stance='retreat'),)), "stance"),
    (OrderOfBattle((Subformation('a', 'heavy_infantry', 10, target='strongest'),)), "target"),
    (OrderOfBattle((Subformation('a', 'heavy_infantry', 10, fall_back_at=1.0),)), "fall_back_at"),
    (OrderOfBattle(tuple(Subformation(f's{i}', 'levy', 10) for i in range(12))), "cap"),
])
def test_boundary_refusals(bad, why):
    with pytest.raises(ValueError, match=why):
        validate(bad)
    with pytest.raises(ValueError):
        build_unit(bad, 'x', 'A', morale_start=5)


# --------------------------------------------------------------------------------------- deployment
def _mixed(strategy='line'):
    return _oob(('spears', 'spearmen', 600, {}), ('swords', 'heavy_infantry', 500, {}),
                ('bows', 'archers', 300, {}), ('scouts', 'light_cavalry', 200, {}),
                ('horse', 'cavalry', 200, {}), strategy=strategy)


def test_deployment_puts_melee_front_ranged_behind_and_horse_on_the_flanks():
    for side, advance in (('A', -1), ('B', 1)):
        u = build_unit(_mixed(), 'u', side, morale_start=5)
        by = {s.troop_type: s for s in u.subunits}
        front_row = by['heavy_infantry'].starting_position[0]
        assert by['spearmen'].starting_position[0] == front_row
        # behind the line is opposite the direction of advance
        assert (by['archers'].starting_position[0] - front_row) * advance < 0
        melee_cols = [by[t].starting_position[1] for t in ('spearmen', 'heavy_infantry')]
        lo, hi = min(melee_cols), max(melee_cols)
        for horse in (by['light_cavalry'], by['cavalry']):
            assert horse.starting_position[1] < lo or horse.starting_position[1] > hi
        assert {by['light_cavalry'].starting_position[1] < lo, by['cavalry'].starting_position[1] < lo} == {True, False}


def test_no_two_subformations_start_on_the_same_cell():
    for side in ('A', 'B'):
        u = build_unit(_mixed(), 'u', side, morale_start=5)
        seen = {}
        for s in u.subunits:
            for cell in s.cells():
                key = tuple(cell[:2])
                assert key not in seen, f"{s.troop_type} and {seen[key]} both start on {key}"
                seen[key] = s.troop_type
        assert len(seen) > 10, "the overlap check is vacuous if the footprints are empty"


def test_the_two_sides_start_on_opposite_rows():
    a = build_unit(_line('heavy_infantry'), 'a', 'A', morale_start=5).subunits[0]
    b = build_unit(_line('heavy_infantry'), 'b', 'B', morale_start=5).subunits[0]
    assert a.starting_position[0] > b.starting_position[0] and a.advance_dir == -1 and b.advance_dir == 1


# ------------------------------------------------------------------------- strategy and tactic fields
def test_strategy_sets_the_stance_of_each_class_and_an_explicit_stance_wins():
    for strategy, table in STRATEGIES.items():
        u = build_unit(_mixed(strategy), 'u', 'A', morale_start=5)
        for s in u.subunits:
            assert s.stance == table[class_of(s.troop_type)], (strategy, s.troop_type)
    assert STRATEGIES['advance']['melee'] != STRATEGIES['defend']['melee'], "vacuous if two strategies are one"
    o = _oob(('w', 'heavy_infantry', 300, {'stance': 'hold'}), strategy='advance')
    assert build_unit(o, 'u', 'A', morale_start=5).subunits[0].stance == 'hold'


def test_tactic_fields_reach_the_subunit():
    o = _oob(('w', 'light_cavalry', 300, {'target': 'weakest', 'fall_back_at': 0.4, 'role': 'Pursue'}))
    s = build_unit(o, 'u', 'A', morale_start=5).subunits[0]
    assert s.target_condition == 'weakest' and s.role == 'Pursue'
    assert [(od.trigger, od.behavior) for od in s.orders] == [('own_strength:0.4', {'stance': 'retreat'})]


def test_a_mounted_archers_body_with_no_role_stands_off_as_kite_and_any_other_type_stays_a_plain_line():
    """ED-1095 (`build_army`'s implicit default) must survive the order-of-battle path, which names a shape for a body
    with no role. The control beside it: the same subformation of another type has no role and no instructions."""
    kite = build_unit(_oob(('m', 'mounted_archers', 300, {})), 'u', 'A', morale_start=5).subunits[0]
    assert kite.role == 'Kite' and kite.instructions, (kite.role, kite.instructions)
    plain = build_unit(_oob(('c', 'light_cavalry', 300, {})), 'u', 'A', morale_start=5).subunits[0]
    assert plain.role is None and not plain.instructions
    named = build_unit(_oob(('m', 'mounted_archers', 300, {'role': 'Harass'})), 'u', 'A', morale_start=5).subunits[0]
    assert named.role == 'Harass', "an explicit role still wins"


def test_side_morale_reaches_every_subunit_and_the_type_stats_still_differ():
    u = build_unit(_mixed(), 'u', 'A', morale_start=3)
    assert {s.eff_morale for s in u.subunits} == {3}
    assert len({s.eff_power for s in u.subunits}) > 1


# ----------------------------------------------------------------------------------- generic roster
def test_the_generic_roster_is_complete_and_distinct():
    new = ('spearmen', 'skirmishers', 'light_cavalry')
    for t in new:
        assert stats_for(t) is not None and t in TROOP_TYPE_ROLES
        weapon, armour = loadout_for(t)
        assert weapon is not None and armour is not None, t
    assert unit_type_for('skirmishers') == 'ranged' and unit_type_for('spearmen') == 'melee'
    assert reach_for('spearmen') == 0.2 > reach_for('light_infantry') == 0.1
    assert support_ranks_for('spearmen') == 2 and support_ranks_for('light_cavalry') == 1
    assert is_mounted('light_cavalry') and not is_mounted('spearmen')
    assert 'Shock' not in TROOP_TYPE_ROLES['light_cavalry'], "light cavalry carries no lance, so no charge role"
    # the mounted set is what the engine's inline ('cavalry', 'mounted_archers') checks were, plus the new type
    assert MOUNTED_TYPES == {'cavalry', 'mounted_archers', 'light_cavalry'}


def test_every_stat_preset_has_a_loadout_and_a_reach():
    """The tables a troop type must appear in agree, so a type cannot be half-registered. A role menu is NOT one of
    them: levy, the missile troops and artillery fall to the 'any' menu by design (`config.TROOP_TYPE_ROLES`)."""
    from modules.mass_battle.troop_types.registry import TROOP_TYPE_REACH, TROOP_TYPE_STATS
    for t in TROOP_TYPE_STATS:
        assert loadout_for(t)[0] is not None, f"{t}: no loadout"
        assert t in TROOP_TYPE_REACH, f"{t}: no reach"


def test_the_unit_baseline_matches_the_season_adapters():
    from modules.mass_battle import orderofbattle as ob
    assert ob._UNIT_POWER == massbattle._SEASON_FORCE_POWER
    assert ob._UNIT_COMMAND == massbattle._MVP_UNIT_COMMAND['command']
    assert ob._UNIT_DISCIPLINE == massbattle._MVP_UNIT_COMMAND['discipline']


def test_survivor_shares_of_an_order_of_battle_never_exceed_one():
    """A side's survivor share is its troops left over its troops at the start. Counted as `effective_size /
    size_max` it passed 1.0 for an army that is not a whole number of 100-troop blocks (120 troops: 1.2 blocks against
    a floored 1), and `march` then RAISED a loser's body. FALSIFIER: set `by_troops=False` in `resolve_field` and the
    120-troop seeds below read above 1."""
    seen = []
    for seed in range(12):
        r = massbattle.resolve_field(_record(oobs=(_line('heavy_infantry', 120), _line('heavy_infantry', 120))),
                                     random.Random(seed))
        seen += [r['attacker_size_pct'], r['defender_size_pct']]
    assert max(seen) <= 1.0 and min(seen) >= 0.0, seen
    assert min(seen) < 1.0, "vacuous if no side took a casualty in twelve fields"


def _stance_of(sf, strategy='line'):
    unit = build_unit(OrderOfBattle((sf,), strategy), 'x', 'A', morale_start=5)
    return unit.subunits[0].eff_stance


def test_a_role_sets_the_stance_its_instructions_name_unless_the_subformation_says_otherwise():
    """Precedence: the subformation's own stance, then its role's, then the strategy's. Writing the strategy's stance
    unconditionally made a role unable to set one. FALSIFIER: restore `stance=sf.stance or STRATEGIES[...]` in
    `_spec_for` and the first line reads 'balanced'."""
    wall = Subformation('w', 'heavy_infantry', 120, role='ShieldWall')
    assert _stance_of(wall) == 'hold', "ShieldWall under the neutral strategy must hold"
    assert _stance_of(Subformation('w', 'heavy_infantry', 120, role='ShieldWall', stance='aggressive')) == 'aggressive'
    plain = Subformation('w', 'heavy_infantry', 120)
    assert _stance_of(plain, 'advance') == 'aggressive' and _stance_of(plain) == 'balanced', "control: no role, the strategy"


def test_one_site_is_shared_by_every_type_trained_at_it():
    """A quarter-built barracks trains a quarter of the cap BETWEEN its types, not a quarter each."""
    from modules.mass_battle.troop_types import recruitment as R
    cap = R.under_arms_cap(12)
    sites = {'barracks': 250}
    first = R.recruit_limit('heavy_infantry', 12, sites, {}, 1000)
    assert first == cap // 4
    assert R.recruit_limit('spearmen', 12, sites, {'heavy_infantry': first}, 1000) == 0, "the barracks is spent"
    assert R.recruit_limit('archers', 12, {**sites, 'archery_range': 250}, {'heavy_infantry': first}, 1000) == cap // 4, (
        "control: a different kind of site is not spent by the barracks's troops")
