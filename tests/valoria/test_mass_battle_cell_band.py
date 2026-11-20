"""The cell band and the unit's minimum, as Jordan ruled them (ED-MB-0101, 2026-11-20): a cell holds 50 to 100 troops
at its start, a unit is a minimum of four cells, and the army floors (three units, 1,000 troops) are named constants
the form-time advisories read. [B17.15]"""
from modules.mass_battle import config
from modules.mass_battle.config import CELL_CAP, CELL_FLOOR, MIN_ARMY_TROOPS, MIN_CELLS_PER_UNIT, MIN_UNITS_PER_ARMY
from modules.mass_battle.geometry import footprint_for
from modules.mass_battle.hierarchy.units import Unit

FOOT = ('infantry', 'spearmen', 'light_infantry', 'heavy_infantry', 'archers', 'pike', 'levy')
SHAPES = ('Line', 'Column', 'Arrowhead', 'GappedLine')


def _unit(troops, troop_type='infantry', shape='Line', concentration=None):
    return Unit(shape=shape, troop_type=troop_type, tier=3, starting_position=(10, 10), troops=troops,
                concentration=float(CELL_CAP if concentration is None else concentration))


def test_the_ruled_band_is_the_shipped_band():
    assert (CELL_FLOOR, CELL_CAP) == (50, 100)
    assert (MIN_CELLS_PER_UNIT, MIN_UNITS_PER_ARMY, MIN_ARMY_TROOPS) == (4, 3, 1000)


def test_every_cell_starts_between_fifty_and_a_hundred():
    checked = 0
    for troops in (200, 201, 250, 333, 400, 777, 1000, 1234, 4000, 9999):
        for troop_type in FOOT:
            for shape in SHAPES:
                for conc in (None, 50, 75):
                    u = _unit(troops, troop_type, shape, conc)
                    for cid, t in u.cell_troops.items():
                        checked += 1
                        assert 50 - 1e-9 <= t <= 100 + 1e-9, (troops, troop_type, shape, conc, cid, t)
    assert checked >= 1000


def test_a_horse_cell_never_exceeds_its_own_cap():
    checked = 0
    for troops in (200, 333, 400, 1234, 4000):
        for troop_type in ('cavalry', 'light_cavalry', 'knights_templar', 'mounted_archers'):
            u = _unit(troops, troop_type)
            assert u.cell_troops and max(u.cell_troops.values()) <= 50 + 1e-9, (troops, troop_type)
            checked += 1
    assert checked >= 1


def test_a_horse_unit_of_whole_fifties_starts_every_cell_at_fifty():
    """The horse half of the band, as far as it holds: a horse cap (50) is the cell floor, so a unit whose troops are a multiple of 50 starts
    every cell at exactly 50. One whose troops are not starts UNDER 50 (333 troops: 7 cells of 47.6), which the two rulings (P-DEC-3,
    ED-MB-0101) cannot both avoid; that case is Jordan's and is not asserted here."""
    checked = 0
    for troops in (200, 400, 1000, 4000):
        for troop_type in ('cavalry', 'light_cavalry', 'knights_templar', 'mounted_archers'):
            u = _unit(troops, troop_type)
            assert min(u.cell_troops.values()) >= CELL_FLOOR - 1e-9, (troops, troop_type, min(u.cell_troops.values()))
            checked += 1
    assert checked == 16


def test_a_unit_of_two_hundred_has_four_cells():
    checked = 0
    for troops in (200, 250, 400, 600, 1000, 4000):
        for troop_type in FOOT + ('cavalry', 'mounted_archers'):
            for shape in SHAPES:
                for conc in (None, 50, 75, 100, 200):
                    n = len(footprint_for(shape, troops, conc if conc is not None else CELL_CAP, troop_type))
                    checked += 1
                    assert n >= 4, (troops, troop_type, shape, conc, n)
    assert checked >= 1
    assert len(_unit(400).cell_troops) >= 4          # the plan's falsifier: 400 foot with fewer than four cells


def test_a_unit_under_the_minimum_keeps_the_footprint_rule_it_had():
    # below MIN_CELLS_PER_UNIT x CELL_FLOOR the unit is below the ruled minimum; its footprint is the old rule's
    assert len(footprint_for('Line', 120, 100, 'infantry')) == 2
    assert len(footprint_for('Line', 60, 100, 'infantry')) == 1


def test_an_explicit_grid_below_four_cells_is_widened_to_four():
    assert len(footprint_for('Line', 400, None, None, width=1, depth=1)) == 4
    assert len(footprint_for('Line', 400, None, None, width=2, depth=1)) == 4
    assert len(footprint_for('Line', 400, None, None, width=8, depth=2)) == 16    # a grid of four or more is the caller's
    assert len(footprint_for('Line', 120, None, None, width=1, depth=1)) == 1     # under the ruled minimum, untouched


def test_the_troop_file_caps_agree_with_the_band():
    from modules.mass_battle.troop_types import table
    assert config.cell_cap_for('infantry') == CELL_CAP == 100
    assert config.cell_cap_for('cavalry') == 50
    assert all(table.cell_cap_of(t) <= CELL_CAP for t in FOOT + ('cavalry',))


def test_the_form_time_warnings_read_the_ruled_minimums():
    from modules.mass_battle import armyrecord as A
    from modules.mass_battle.armyrecord import options
    from engine.season.queries.inputs import ArmyOptionsQuery
    rec = A.form(A.new('fac_x'), 'tiny', 'spearmen')
    rec = A.raised(rec, 'c1', 'spearmen', 150)
    rec = A.assign(rec, 'tiny', 'c1', 150)
    kinds = {a[0]: a for a in options(ArmyOptionsQuery(record=rec, cohorts=(), full=1.0, others=()))['advisories']}
    assert kinds['unit_routs'][1:] == ('tiny', 150, MIN_CELLS_PER_UNIT * CELL_FLOOR)
    assert kinds['army_units'][2:] == (1, MIN_UNITS_PER_ARMY)
    assert kinds['army_troops'][2:] == (150, MIN_ARMY_TROOPS)
    big = A.new('fac_x')
    for i in range(3):
        big = A.assign(A.form(A.raised(big, 'c1', 'spearmen', 400), f'u{i}', 'spearmen'), f'u{i}', 'c1', 400)
    got = {a[0] for a in options(ArmyOptionsQuery(record=big, cohorts=(), full=1.0, others=()))['advisories']}
    assert not got & {'unit_routs', 'army_units', 'army_troops'}, got       # the control: three units, 1,200 troops
