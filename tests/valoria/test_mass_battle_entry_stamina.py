"""One stamina ledger (`16_PESSIMIST_MB_one_stamina_ledger` step 1): the column ledger
(`percell._ColBlock.stamina`) is the only store, so a per-unit `stamina` / `stamina_max` key on a
`build_army` spec is refused with a message naming `entry_stamina`, not forwarded to a field that is gone."""
import pytest

from modules.mass_battle.armies import build_army
from modules.mass_battle.config import STAMINA_MAX


def _spec(**extra):
    return {'shape': 'Line', 'troop_type': 'infantry', 'unit_type': 'melee', 'width': 3, 'depth': 5, 'troops': 1500.0, **extra}


@pytest.mark.parametrize('key', ['stamina', 'stamina_max'])
def test_a_unit_stamina_spec_key_is_refused(key):
    with pytest.raises(ValueError, match='entry_stamina'):
        build_army([_spec(**{key: 50})], 'A', 'A')
    # control: the same spec without the key builds, and its column ledger starts at the ceiling
    army = build_army([_spec()], 'A', 'A')
    assert army.col_grid and all(b.stamina == STAMINA_MAX for b in army.col_grid)
    assert army.agg_stamina() == STAMINA_MAX


def test_a_spent_column_costs_the_units_standing_in_it_one_die():
    """The exhausted -1 die reads the column ledger (`percell.column_exhausted`): a unit loses one die when the
    lowest live column block it stands in is at 0, and a unit standing in other columns does not."""
    from modules.mass_battle.config import SIDE_A_START_ROW, STAMINA_EXHAUSTED_POOL_PENALTY
    from modules.mass_battle.core.exchange import subunit_combat_pool
    army = build_army([_spec(starting_position=(SIDE_A_START_ROW, 10)),
                       _spec(starting_position=(SIDE_A_START_ROW, 30))], 'A', 'A')
    left, right = army.units
    cols_l, cols_r = ({c for _p, (_r, c), t in u.iter_cells() if t > 0} for u in (left, right))
    assert cols_l and cols_r and not (cols_l & cols_r)
    fresh = (subunit_combat_pool(army, left), subunit_combat_pool(army, right))
    assert fresh[0] > 1 and fresh[1] > 1               # above the floor, so a lost die is visible
    one = min(cols_l)
    for b in army.col_grid:
        if b.col == one:
            b.stamina = 0.0                            # one file of the left unit is spent
    assert subunit_combat_pool(army, left) == fresh[0] + STAMINA_EXHAUSTED_POOL_PENALTY
    assert subunit_combat_pool(army, right) == fresh[1]   # control: the right unit's files are fresh


def test_returned_stamina_below_100_after_a_fought_field():
    """`run_battle`'s `a_stamina` / `b_stamina` are `agg_stamina()` of the column ledger, the one the fatigue
    malus reads (step 2): after eighteen ticks of contact the number returned is below STAMINA_MAX for both sides,
    and it is the very number `agg_stamina()` reads off the armies afterwards."""
    from engine.dice_engine import draw
    from modules.mass_battle import rngsource
    from modules.mass_battle.battle_loop import run_battle
    from systems.mass_battle.sim.engine import build_unit
    a, b = build_unit('Line', 3, 'A', 'A', 9), build_unit('Line', 3, 'B', 'B', 9)
    hp0 = (a.hp, b.hp)
    with rngsource.using(draw.seeded(draw.H2("test_mass_battle_entry_stamina", 1))):
        res = run_battle(a, b, max_ticks=18)
    assert a.hp < hp0[0] and b.hp < hp0[1], "no contact: the field was not fought, so the stamina reading means nothing"
    assert res["a_stamina"] < STAMINA_MAX and res["b_stamina"] < STAMINA_MAX
    assert (res["a_stamina"], res["b_stamina"]) == (a.agg_stamina(), b.agg_stamina())


# ---- B19.28: a field may be entered tired -- `MassBattleInput.entry_stamina` ----------------------------------------------

def _mirror(**extra):
    """A mirror field: two headcount sides of the one weight on open ground (`resolve_field`'s own record, hand-built)."""
    import yaml
    from engine.season.data import files
    from engine.season.queries.inputs import MassBattleInput
    with open(files.GEOGRAPHY_YAML, encoding="utf-8") as f:
        geo = yaml.safe_load(f)
    return MassBattleInput(weights=((3.0,), (3.0,)), territory=None, fort_level=0.0, stances=(0.0, 0.0), walls_dr=None,
                           origin=None, loyalties=(0.0, 0.0), loyalty_gain=0, geography=geo, condition_scale=100,
                           members=(("a",), ("b",)), **extra)


def _fight(inp, seed):
    from engine.dice_engine import draw
    from modules.mass_battle.massbattle import resolve_field
    return resolve_field(inp, draw.seeded(draw.H2("test_mass_battle_entry_stamina_b1928", seed)))


def test_entry_stamina_half_loses_more(monkeypatch):
    """A side entered at half stamina loses a mirror field more often than the side entered fresh (`CR D3`). 100 seeds, friction pinned
    off (`MB_FRICTION`: the per-side log-normal draw would otherwise swamp a stamina share of this size), the attacker's entry the one
    thing that differs. `lost` is the attacker ending below the defender's share. The gap must clear twice the standard error of the
    difference of two shares of 100, and the loop asserts it fought every seed."""
    import dataclasses
    import modules.mass_battle.orchestration as orch
    monkeypatch.setattr(orch, "MB_FRICTION", False)
    n, tired, fresh, checked = 100, 0, 0, 0
    for seed in range(n):
        for entry, is_tired in (((0.5, 1.0), True), ((1.0, 1.0), False)):
            got = _fight(dataclasses.replace(_mirror(), entry_stamina=entry), seed)
            lost = got.attacker.share < got.defender.share
            tired += lost and is_tired
            fresh += lost and not is_tired
            checked += 1
    sampling_band = 2 * (2 * 0.25 * n) ** 0.5       # 2 s.e. of a difference of two win counts, p = 1/2, n each
    assert checked >= 100 and checked == 2 * n
    assert tired - fresh > sampling_band, (tired, fresh, sampling_band)


def test_default_equals_omitted(monkeypatch):
    """`entry_stamina=(1.0, 1.0)` is the field with the argument omitted, field for field: the whole `FieldOutcome` equal, seed for seed (12 seeds: the arms are one code path, and a fight is 0.2 s)."""
    import dataclasses
    import modules.mass_battle.orchestration as orch
    monkeypatch.setattr(orch, "MB_FRICTION", False)
    checked = 0
    for seed in range(12):
        omitted = _fight(_mirror(), seed)
        stated = _fight(dataclasses.replace(_mirror(), entry_stamina=(1.0, 1.0)), seed)
        assert stated == omitted, seed
        checked += 1
    assert checked >= 12
