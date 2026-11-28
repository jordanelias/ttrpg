"""ED-IN-0306 phase 1 -- a faction's ORDER OF BATTLE reaches the mass-battle engine.

`modules/mass_battle/orderofbattle.py` turns named units (troop type, size, role, posture) plus a strategy
into the multi-subunit Army the engine fights, and `massbattle.resolve_field` takes one per side from the input
record's `orders_of_battle`. What this proves, and the control beside each claim:

  * THE CONTROL: a record with no orders of battle is the field as it was (the single headcount line), so the
    existing goldens still bind it -- compared against an explicit `(None, None)`, and `_weighted_unit` is the path.
  * THE FALSIFIER: two orders of battle of EQUAL headcount and different troop types fight differently. If the
    types never reached the engine the two would be identical on every seed.
  * Refusals at the boundary, deployment without overlap, strategy and tactic fields reaching the Unit, and the
    new generic roster (spearmen, skirmishers, light cavalry) carrying what makes it a different type.
"""
from engine.dice_engine import draw

import pytest

from engine.season.data.rosters import WON
from engine.season.queries.inputs import MassBattleInput
from engine.season.seam.ladder import field_degree
from modules.mass_battle import massbattle
from modules.mass_battle.config import TROOP_TYPE_ROLES
from modules.mass_battle.equipment import loadout_for
from modules.mass_battle.orderofbattle import (STRATEGIES, OrderOfBattle, UnitRow, build_unit, class_of,
                                               subformations, validate)
from modules.mass_battle.troop_types.registry import (MOUNTED_TYPES, is_mounted, reach_for, stats_for,
                                                      support_ranks_for, unit_type_for)

from engine.season.tests._field_outcomes import SCALE

SEEDS = tuple(range(40, 52))     # twelve: the engine's losses are one-sided per seed, so a type's effect shows in the aggregate


def _record(oobs=None, **kw):
    base = dict(weights=((10,), (10,)), territory=None, fort_level=0.0, stances=(0.0, 0.0), walls_dr=None,
                origin=None, loyalties=(0.0, 0.0), loyalty_gain=0, geography={}, condition_scale=SCALE)
    base.update(kw)
    return MassBattleInput(**base, **({} if oobs is None else {'orders_of_battle': oobs}))


def _oob(*parts, strategy='line'):
    return OrderOfBattle(tuple(UnitRow(n, t, q, **kw) for n, t, q, kw in parts), strategy)


def _line(troop_type, n=1000):
    return _oob(('body', troop_type, n, {}))


# --------------------------------------------------------------------------------------- the control
def test_no_orders_of_battle_is_the_field_as_it_was():
    plain = massbattle.resolve_field(_record(), draw.seeded(draw.H2("test_mass_battle_order_of_battle", 5)))
    explicit = massbattle.resolve_field(_record(oobs=(None, None)), draw.seeded(draw.H2("test_mass_battle_order_of_battle", 5)))
    assert plain == explicit
    assert massbattle._weighted_unit("side_a", 10, 'A').units[0].troop_type == 'infantry', (
        "the control is vacuous if the headcount line stopped being the single infantry subunit")


# ------------------------------------------------------------------------------------- the falsifier
def _fight(oob_a, seed):
    return massbattle.resolve_field(_record(oobs=(oob_a, _line('heavy_infantry'))), draw.seeded(draw.H2("test_mass_battle_order_of_battle", seed)))


def _tally(troop_type):
    rs = [_fight(_line(troop_type), s) for s in SEEDS]
    assert len(rs) == len(SEEDS)
    return sum(field_degree(r) == WON for r in rs), sum(r.attacker.share for r in rs) / len(rs) / SCALE


def test_equal_headcount_of_different_troop_types_fights_differently():
    heavy_wins, heavy_kept = _tally('heavy_infantry')
    levy_wins, levy_kept = _tally('levy')
    assert (heavy_wins, heavy_kept) != (levy_wins, levy_kept), (
        "1000 heavy infantry and 1000 levy fought identically over twelve seeds: troop types never arrived")
    # and the direction is the stat table's (power 4 against power 1): the heavy line wins more and keeps more
    assert heavy_wins > levy_wins and heavy_kept > levy_kept
    assert heavy_kept < 1.0 and levy_kept < 1.0, "vacuous if neither line took a casualty (the lines never joined)"


def test_an_order_of_battle_side_and_a_headcount_side_both_deploy():
    """A side with no order of battle, once the other has one, is a deployed light-infantry line, not a crash. (B17.16: the headcount
    side is weight 9, 9,000 troops, the line it was at 30 a weight and weight 300; at 1,000 a weight it is cut into three units.)"""
    r = massbattle.resolve_field(_record(oobs=(_line('archers', 400), None), weights=((10,), (9,))),
                                 draw.seeded(draw.H2("test_mass_battle_order_of_battle", 3)))
    assert type(r).__name__ == 'FieldOutcome' and r.attacker.parts == () and r.defender.parts == ()


# ---------------------------------------------------------------------------------------- refusals
@pytest.mark.parametrize("bad, why", [
    (OrderOfBattle((), 'line'), "at least one"),
    (OrderOfBattle((UnitRow('a', 'heavy_infantry', 10),), 'nope'), "unknown strategy"),
    (OrderOfBattle((UnitRow('a', 'heavy_infantry', 10), UnitRow('a', 'archers', 10))), "duplicate"),
    (OrderOfBattle((UnitRow('a', 'dragons', 10),)), "no stat preset"),
    (OrderOfBattle((UnitRow('a', 'heavy_infantry', 0),)), "positive"),
    (OrderOfBattle((UnitRow('a', 'heavy_infantry', 10, role='Kite'),)), "menu"),
    (OrderOfBattle((UnitRow('a', 'heavy_infantry', 10, posture='retreat'),)), "posture"),
    (OrderOfBattle((UnitRow('a', 'heavy_infantry', 10, target='strongest'),)), "target"),
    (OrderOfBattle((UnitRow('a', 'heavy_infantry', 10, fall_back_at=1.0),)), "fall_back_at"),
    (OrderOfBattle(tuple(UnitRow(f's{i}', 'levy', 10) for i in range(12))), "cap"),
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
        by = {s.troop_type: s for s in u.units}
        front_row = by['heavy_infantry'].starting_position[0]
        assert by['spearmen'].starting_position[0] == front_row
        # behind the line is opposite the direction of advance
        assert (by['archers'].starting_position[0] - front_row) * advance < 0
        melee_cols = [by[t].starting_position[1] for t in ('spearmen', 'heavy_infantry')]
        lo, hi = min(melee_cols), max(melee_cols)
        for horse in (by['light_cavalry'], by['cavalry']):
            assert horse.starting_position[1] < lo or horse.starting_position[1] > hi
        assert {by['light_cavalry'].starting_position[1] < lo, by['cavalry'].starting_position[1] < lo} == {True, False}


def test_no_two_units_start_on_the_same_cell():
    for side in ('A', 'B'):
        u = build_unit(_mixed(), 'u', side, morale_start=5)
        seen = {}
        for s in u.units:
            for cell in s.cells():
                key = tuple(cell[:2])
                assert key not in seen, f"{s.troop_type} and {seen[key]} both start on {key}"
                seen[key] = s.troop_type
        assert len(seen) > 10, "the overlap check is vacuous if the footprints are empty"


def test_the_two_sides_start_on_opposite_rows():
    a = build_unit(_line('heavy_infantry'), 'a', 'A', morale_start=5).units[0]
    b = build_unit(_line('heavy_infantry'), 'b', 'B', morale_start=5).units[0]
    assert a.starting_position[0] > b.starting_position[0] and a.advance_dir == -1 and b.advance_dir == 1


# ------------------------------------------------------------------------- strategy and tactic fields
def test_strategy_sets_the_posture_of_each_class_and_an_explicit_posture_wins():
    for strategy, table in STRATEGIES.items():
        u = build_unit(_mixed(strategy), 'u', 'A', morale_start=5)
        for s in u.units:
            assert s.stance == table[class_of(s.troop_type)], (strategy, s.troop_type)
    assert STRATEGIES['advance']['melee'] != STRATEGIES['defend']['melee'], "vacuous if two strategies are one"
    o = _oob(('w', 'heavy_infantry', 300, {'posture': 'hold'}), strategy='advance')
    assert build_unit(o, 'u', 'A', morale_start=5).units[0].stance == 'hold'


def test_tactic_fields_reach_the_subunit():
    o = _oob(('w', 'light_cavalry', 300, {'target': 'weakest', 'fall_back_at': 0.4, 'role': 'Flanker'}))
    s = build_unit(o, 'u', 'A', morale_start=5).units[0]
    assert s.target_condition == 'weakest' and s.role == 'Flanker'
    assert [(od.trigger, od.behavior) for od in s.orders] == [('own_strength:0.4', {'stance': 'retreat'})]


def test_a_mounted_archers_body_with_no_role_stands_off_as_kite_and_any_other_type_stays_a_plain_line():
    """ED-1095 (`build_army`'s implicit default) must survive the order-of-battle path, which names a shape for a body
    with no role. The control beside it: the same unit of another type has no role and no instructions."""
    kite = build_unit(_oob(('m', 'mounted_archers', 300, {})), 'u', 'A', morale_start=5).units[0]
    assert kite.role == 'Kite' and kite.instructions, (kite.role, kite.instructions)
    plain = build_unit(_oob(('c', 'light_cavalry', 300, {})), 'u', 'A', morale_start=5).units[0]
    assert plain.role is None and not plain.instructions
    # B17.07: `Harass` is off every menu, so naming it for mounted archers is refused (the menu is Kite alone)
    with pytest.raises(ValueError):
        build_unit(_oob(('m', 'mounted_archers', 300, {'role': 'Harass'})), 'u', 'A', morale_start=5)


def test_side_morale_reaches_every_subunit_and_the_type_stats_still_differ():
    u = build_unit(_mixed(), 'u', 'A', morale_start=3)
    assert {s.eff_morale for s in u.units} == {3}
    assert len({s.eff_power for s in u.units}) > 1


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
    them: levy, the missile troops and artillery fall to the 'any' menu by design (`config.TROOP_TYPE_ROLES`). Reach
    is no table of its own (B17.11): it is the class of the primary arm, so a type has one exactly when it has an arm."""
    from modules.mass_battle.troop_types import table
    from modules.mass_battle.troop_types.registry import TROOP_TYPE_STATS
    for t in TROOP_TYPE_STATS:
        assert loadout_for(t)[0] is not None, f"{t}: no loadout"
        assert table.reach_of(t) is not None, f"{t}: no reach"


def test_the_unit_baseline_matches_the_season_adapters():
    from modules.mass_battle import orderofbattle as ob
    assert ob._UNIT_POWER == massbattle._SEASON_FORCE_POWER
    from modules.mass_battle.config import COMMAND_DEFAULT
    assert ob._UNIT_COMMAND == massbattle._MVP_UNIT_COMMAND['command'] == COMMAND_DEFAULT
    assert ob._UNIT_DISCIPLINE == massbattle._MVP_UNIT_COMMAND['discipline']


def test_survivor_shares_of_an_order_of_battle_never_exceed_one():
    """A side's survivor share is its troops left over its troops at the start. Counted as `effective_size /
    size_max` it passed 1.0 for an army that is not a whole number of 100-troop blocks (120 troops: 1.2 blocks against
    a floored 1), and `march` then RAISED a loser's body. B17.01 made `hp / hp_max` the one reading on every path (the
    `by_troops` switch is gone). FALSIFIER: read `effective_size / size_max` in `_grade` and the 120-troop seeds below read above 1."""
    seen = []
    for seed in range(12):
        r = massbattle.resolve_field(_record(oobs=(_line('heavy_infantry', 120), _line('heavy_infantry', 120))),
                                     draw.seeded(draw.H2("test_mass_battle_order_of_battle", seed)))
        seen += [r.attacker.share, r.defender.share]
    assert max(seen) <= SCALE and min(seen) >= 0, seen
    assert min(seen) < SCALE, "vacuous if no side took a casualty in twelve fields"


def _stance_of(sf, strategy='line'):
    unit = build_unit(OrderOfBattle((sf,), strategy), 'x', 'A', morale_start=5)
    return unit.units[0].eff_stance


def test_a_role_sets_the_posture_its_instructions_name_unless_the_unit_says_otherwise():
    """Precedence: the unit's own posture, then its role's, then the strategy's. Writing the strategy's posture
    unconditionally made a role unable to set one. FALSIFIER: restore `stance=sf.posture or STRATEGIES[...]` (the engine spec key) in
    `_spec_for` and the first line reads 'balanced'."""
    wall = UnitRow('w', 'heavy_infantry', 120, role='ShieldWall')
    assert _stance_of(wall) == 'hold', "ShieldWall under the neutral strategy must hold"
    assert _stance_of(UnitRow('w', 'heavy_infantry', 120, role='ShieldWall', posture='aggressive')) == 'aggressive'
    plain = UnitRow('w', 'heavy_infantry', 120)
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


# ------------------------------------------------------------ a troop type is a row (B17.11): no name is spelled in code
@pytest.fixture
def new_rows(monkeypatch):
    """The loaded troop file with two rows added that no code names: `cataphracts` (the `cavalry` row under another name:
    mounted, charge 3, wheel) and `steppe_archers` (the `mounted_archers` row under another name: default role Kite). The
    loader's tables are cleared on the way in and out, so the doc is the only thing that changed."""
    import copy
    from modules.mass_battle.troop_types import table
    doc = copy.deepcopy(table._data())
    doc['troops']['cataphracts'] = dict(doc['troops']['cavalry'])
    doc['troops']['cataphracts_unlanced'] = dict(doc['troops']['cavalry'], charge=0)
    doc['troops']['steppe_archers'] = dict(doc['troops']['mounted_archers'])
    table.check(doc)

    def clear():
        for f in (table._stats, table._mounted, table._menus, table._sites):
            f.cache_clear()
        from modules.mass_battle.troop_types import registry as _reg
        _reg.reach_for.cache_clear()
        _reg.support_ranks_for.cache_clear()
    monkeypatch.setattr(table, '_data', lambda: doc)
    clear()
    yield doc
    monkeypatch.undo()
    clear()


def test_a_new_row_charges_and_wheels_with_no_code_edit(new_rows):
    """A row `cataphracts` with `mounted: true, charge: 3, wheel: true` charges, recoils and wheels with no code edit; the
    same row with `charge: 0` is the control that each of the three reads is the column and not the spelling of a name.
    FALSIFIER: restore `troop_type == 'cavalry'` at `Unit.charge_pen` or at either recoil site, or the name tuple at
    `_envelop_goal`, and the matching assertion below reads the old answer."""
    from types import SimpleNamespace
    from modules.mass_battle import rngsource
    import modules.mass_battle.hierarchy.units as hu
    import modules.mass_battle.orchestration as orch
    from systems.mass_battle.sim import validators as val
    from systems.mass_battle.sim.engine import build_unit as sim_unit

    # charges: the penetration is the column
    assert sim_unit('Line', 3, 'A', 'A', 9, troop_type='cataphracts').units[0].charge_pen == 3
    assert sim_unit('Line', 3, 'A', 'A', 9, troop_type='cataphracts_unlanced').units[0].charge_pen == 0
    assert sim_unit('Line', 3, 'A', 'A', 9, troop_type='pike').units[0].charge_pen == 0

    # wheels: the fast enveloping wheel is the column (the control takes the infantry's flank face instead)
    enemy = [(r, c) for r in range(10, 13) for c in range(10, 13)]

    def goal(tt):
        me = SimpleNamespace(troop_type=tt, unit_type='melee', _node_anchor=(30.0, 11.0),
                             _envelop_wheel_goal=lambda cells: 'WHEEL', _envelop_goal_legacy=lambda cells: 'LEGACY')
        return hu.Unit._envelop_goal(me, enemy)
    assert goal('cataphracts') == 'WHEEL' and goal('cavalry') == 'WHEEL' and goal('light_cavalry') == 'WHEEL'
    assert goal('cataphracts_unlanced') == 'WHEEL', "wheel is its own column, not charge"
    assert goal('pike') not in ('WHEEL', 'LEGACY')

    # recoils: a braced pike wall repels a charge from the new row exactly as it repels the `cavalry` row's, and not at all
    # when the new row's charge is 0 (same seeds, same everything else)
    saved = [(m, m.FIELD_MOVEMENT, m.MB_NODE_COHESION) for m in (hu, orch)]
    val._set_movement_path('node')
    try:
        def wall_hp(charger, seeds=(700, 701, 702)):
            tot = 0.0
            for s in seeds:
                with rngsource.using(draw.seeded(draw.H2("test_mass_battle_order_of_battle", s))):
                    d = sim_unit('Line', 3, 'DEF', 'A', 9, troop_type='pike', stance='hold', instructions=('brace', 'hold'))
                    c = sim_unit('Line', 3, 'CAV', 'B', 9, troop_type=charger, speed='Fast', instructions=('charge',))
                    h0 = d.hp
                    orch.run_battle(d, c, max_ticks=18)
                tot += d.hp / h0
            return tot / len(seeds)
        lanced, named, unlanced = wall_hp('cavalry'), wall_hp('cataphracts'), wall_hp('cataphracts_unlanced')
    finally:
        for m, fm, nc in saved:
            m.FIELD_MOVEMENT = fm
            m.MB_NODE_COHESION = nc
    assert named == lanced, "the renamed row recoils as `cavalry` does"
    assert unlanced != lanced, "control: with charge 0 the wall does not repel it, so the read is the column"


def test_a_new_row_with_a_default_role_stands_off_with_no_code_edit(new_rows):
    """`default_role: Kite` on a row of another name stands the body off as Kite on both build paths (`build_army` and the
    order-of-battle path) when no role, shape or instructions are named; a row without it stays a plain line."""
    from systems.mass_battle.sim.engine import build_army
    kite = build_unit(_oob(('s', 'steppe_archers', 300, {})), 'u', 'A', morale_start=5).units[0]
    assert kite.role == 'Kite' and kite.instructions, (kite.role, kite.instructions)
    assert build_army([dict(troop_type='steppe_archers', troops=300.0, concentration=200.0)], 'u', 'A').units[0].role == 'Kite'
    assert build_army([dict(troop_type='steppe_archers', troops=300.0, concentration=200.0, shape='Line')], 'u', 'A').units[0].role is None, (
        "an explicit shape still wins")
    plain = build_unit(_oob(('c', 'cataphracts', 300, {})), 'u', 'A', morale_start=5).units[0]
    assert plain.role is None and not plain.instructions


# ------------------------------------------------------------------------------- depth is a lever (B19.17, gate 4)
def test_depth_is_a_lever():
    """Two equal heavy-infantry bodies, one `depth: 2` and one `depth: 6` (each laid on the grid rule, `orderofbattle.cells_for`, whatever
    the troop file's `deployment.arm` says), fight the same defender on the same 200 seeds. THE CONTROL IS IN THE SAME RUN: the depth-2
    body again, on 200 other seeds -- the spread two samples of one body show. The claim is that the win counts or the mean loss shares
    of the two depths differ by more than the control's. THE RESULT IS RECORDED, NOT TARGETED: nothing here says which depth is better
    or by how much, only that depth moves a field at all (if it did not, `depth` would be a column no field reads)."""
    n, troops = 200, 600
    deep, shallow = (_oob(('body', 'heavy_infantry', troops, {'depth': d})) for d in (6, 2))

    def tally(oob, first):
        wins, kept, checked = 0, 0.0, 0
        for s in range(first, first + n):
            r = massbattle.resolve_field(_record(oobs=(oob, _line('heavy_infantry', troops))),
                                         draw.seeded(draw.H2("test_mass_battle_order_of_battle", s)))
            wins += field_degree(r) == WON
            kept += r.attacker.share / SCALE
            checked += 1
        assert checked >= 200
        return wins, 1.0 - kept / n

    for oob, depth in ((deep, 6), (shallow, 2)):      # the lever reached the footprint: `depth` rows, whatever the width
        rows = {cell[0] for u in build_unit(oob, 'a', 'A', morale_start=5).units for cell in u.cells()}
        assert len(rows) == depth, (depth, sorted(rows))
    (w2, l2), (w6, l6), (wc, lc) = tally(shallow, 1000), tally(deep, 1000), tally(shallow, 5000)
    print(f"[depth lever, n={n}] depth 2: wins {w2}, loss share {l2:.4f}; depth 6: wins {w6}, loss share {l6:.4f}; "
          f"control (depth 2, other seeds): wins {wc}, loss share {lc:.4f}")
    assert l2 > 0 and l6 > 0 and lc > 0, "vacuous if the lines never joined (no casualties)"
    assert abs(w6 - w2) > abs(wc - w2) or abs(l6 - l2) > abs(lc - l2), (
        f"depth 2 vs depth 6 moved no more than the control's own spread: wins {w2}/{w6}/{wc}, loss {l2:.4f}/{l6:.4f}/{lc:.4f}")


# ------------------------------------------------------------------------------- a unit's post, the army's formation (B19.18)
def _cols(unit):
    return [cell[1] for cell in unit.cells()]


def test_a_left_post_starts_left_of_the_front():
    """A unit posted `left` in `line` starts left of the centre line's left edge, level with it, on either side. THE CONTROL: the same two
    units with no post, the one named last: it stands in the centre line, to the RIGHT of the other, so the post (and not the unit's order
    in the list) put it left. A post the formation has no row for is refused at the boundary."""
    posted = _oob(('wall', 'heavy_infantry', 500, {}), ('hook', 'spearmen', 300, {'post': 'left'}))
    plain = _oob(('wall', 'heavy_infantry', 500, {}), ('hook', 'spearmen', 300, {}))
    for side in ('A', 'B'):
        wall, hook = build_unit(posted, 'u', side, morale_start=5).units
        assert max(_cols(hook)) < min(_cols(wall)), (side, "the left post is not left of the front's left edge")
        assert hook.starting_position[0] == wall.starting_position[0]
        wall, hook = build_unit(plain, 'u', side, morale_start=5).units
        assert min(_cols(hook)) > max(_cols(wall)), (side, "the control: with no post the second unit stands to the right")
    with pytest.raises(ValueError):
        validate(_oob(('hook', 'spearmen', 300, {'post': 'flank_guard'})))


def test_envelopment_row_equals_the_harness_builder():
    """An army with `formation: envelopment` starts with both wings wide of the centre (the left wing left of it and the right wing right of
    it, a clear gap each), and the harness's own `build_envelopment`, given the same specs, starts every unit on the same cells -- compared
    relative to the centre's row, since the season and the harness base their rows differently. THE CONTROL: the same army in `line` is not
    the envelopment's shape, so the equality is not a property of any two layouts."""
    from systems.mass_battle.sim.engine import build_envelopment
    from modules.mass_battle.orderofbattle import _spec_for
    oob = OrderOfBattle((UnitRow('centre', 'heavy_infantry', 500), UnitRow('lw', 'light_cavalry', 200, post='left'),
                         UnitRow('rw', 'light_cavalry', 200, post='right')), 'line', formation='envelopment')
    specs = [_spec_for(sf, 'line') for sf in oob.units]

    def shape(units):
        base = units[0].starting_position[0]
        return [sorted((cell[0] - base, cell[1]) for cell in u.cells()) for u in units]

    checked = 0
    for side in ('A', 'B'):
        season = build_unit(oob, 'u', side, morale_start=5)
        centre, lw, rw = season.units
        assert max(_cols(lw)) < min(_cols(centre)) - 1 and min(_cols(rw)) > max(_cols(centre)) + 1, "the wings are not wide of the centre"
        harness = build_envelopment([specs[0]], specs[1:], 'h', side)
        assert shape(season.units) == shape(harness.units), side
        line = build_unit(OrderOfBattle(oob.units, 'line'), 'u', side, morale_start=5)
        assert shape(line.units) != shape(harness.units), "the control: `line` is not the envelopment"
        checked += 1
    assert checked == 2


def test_subformations_group_units_by_post():
    """B19.19: a subformation is READ over the unit rows (nothing is stored): the units at one post, the posts in the formation's order."""
    oob = _oob(('a', 'heavy_infantry', 100, {'post': 'left'}), ('b', 'heavy_infantry', 100, {'post': 'centre'}),
               ('c', 'heavy_infantry', 100, {'post': 'left'}))
    assert subformations(oob) == (('centre', ('b',)), ('left', ('a', 'c')))
    assert 'subformations' not in OrderOfBattle.__dataclass_fields__          # read, not stored


# ------------------------------------------------------------------------- the opening distance (B19.21)
def _with_table(monkeypatch, arm_ranges=(), opening_rows=None):
    """The loaded troop file with some `arms.<key>.range` and `formations.line.opening_rows` set, as the one document `table` reads."""
    import copy
    from modules.mass_battle.troop_types import table
    doc = copy.deepcopy(table._data())
    for arm, rng in arm_ranges:
        doc['arms'][arm]['range'] = list(rng)
    if opening_rows is not None:
        doc['formations']['line']['opening_rows'] = opening_rows
    table.check(doc)
    monkeypatch.setattr(table, '_data', lambda: doc)


def _opening_between(oob_a, oob_b):
    """(clear rows between the two foremost faces, the lowest row any cell of B stands on, the highest row any cell of A stands on),
    each army built by `build_unit` against the other as `massbattle` builds them."""
    a = build_unit(oob_a, 'a', 'A', morale_start=5, foe=oob_b)
    b = build_unit(oob_b, 'b', 'B', morale_start=5, foe=oob_a)
    front_a = min(c[0] for u in a.units for c in u.cells() if u.troop_type == 'heavy_infantry')
    front_b = max(c[0] for u in b.units for c in u.cells() if u.troop_type == 'heavy_infantry')
    return (front_a - front_b - 1, min(c[0] for u in b.units for c in u.cells()), max(c[0] for u in a.units for c in u.cells()))


def test_opening_rows_auto_is_the_longest_missile_range_with_a_floor(monkeypatch):
    """CLASS game-state, lane mass_battle. With `opening_rows: auto` two armies start the longest `range[1]` among the missile arms on EITHER
    side apart, floor 3, capped so both lines fit the field. THE CONTROLS: the value `3` as shipped keeps three rows whatever the arms
    carry (the rule is behind the value `auto`), and two armies with no missiles start three rows apart with `auto` as well."""
    from modules.mass_battle.config import BATTLEFIELD_SIZE
    wall = ('wall', 'heavy_infantry', 400, {})
    plain = _oob(wall)
    with_bows = _oob(wall, ('bows', 'archers', 200, {}))
    with_javelins = _oob(wall, ('darts', 'skirmishers', 200, {}))
    with_slings = _oob(wall, ('slings', 'sling', 200, {}))
    ranges = [('bow', (2, 5)), ('javelin', (1, 6)), ('sling', (2, 2))]
    _with_table(monkeypatch, arm_ranges=ranges, opening_rows=3)
    assert _opening_between(with_bows, plain)[0] == 3, "control: the value 3 gave way to a missile arm's range"
    _with_table(monkeypatch, arm_ranges=ranges, opening_rows='auto')
    assert _opening_between(plain, plain)[0] == 3, "control: two armies with no missiles are not three rows apart"
    assert _opening_between(with_bows, plain)[0] == 5, "bows on the attacker's side only: not the bow's range[1]"
    assert _opening_between(plain, with_bows)[0] == 5, "bows on the defender's side only: not the bow's range[1]"
    assert _opening_between(with_bows, with_javelins)[0] == 6, "bows against javelins: not the longest range[1] of either side"
    assert _opening_between(with_slings, plain)[0] == 3, "a range shorter than the floor moved the opening below it"
    _with_table(monkeypatch, arm_ranges=[('bow', (2, 40))], opening_rows='auto')
    gap, b_low, a_high = _opening_between(with_bows, plain)
    assert 3 < gap < 40, f"a 40-cell bow was not capped to the field: {gap}"
    assert b_low <= 1 and a_high <= BATTLEFIELD_SIZE - 2, f"the cap left room it could have used or went off the field: B from row {b_low}, A to row {a_high}"
