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


def test_a_spent_column_tires_the_units_standing_in_it():
    """The column ledger feeds the contact draw's `rounds_d` (B19.12; it fed the exhausted -1 die until the pool left the melee pair):
    a unit whose contact files include a spent one fights at a later duel round, and a unit standing in other columns does not."""
    from modules.mass_battle.config import SIDE_A_START_ROW
    from modules.mass_battle.core import contact_draw as cd
    army = build_army([_spec(starting_position=(SIDE_A_START_ROW, 10)),
                       _spec(starting_position=(SIDE_A_START_ROW, 30))], 'A', 'A')
    left, right = army.units
    cells_l, cells_r = (sorted({c for _p, c, t in u.iter_cells() if t > 0}) for u in (left, right))
    assert cells_l and cells_r and not ({c for _r, c in cells_l} & {c for _r, c in cells_r})

    def rounds(sub, cells):
        other = right if sub is left else left
        return cd.contact_vector(sub, army, cells, None, other, army, cells, None, None, True, 0.1, ()).rounds_d
    fresh = (rounds(left, cells_l), rounds(right, cells_r))
    assert fresh == (1.0, 1.0)                         # a fresh front fights its first round
    one = min(c for _r, c in cells_l)
    for b in army.col_grid:
        if b.col == one:
            b.stamina = 0.0                            # one file of the left unit is spent
    assert rounds(left, cells_l) > fresh[0]
    assert rounds(right, cells_r) == fresh[1]          # control: the right unit's files are fresh


def test_returned_stamina_below_100_after_a_fought_field():
    """`run_battle`'s `a_stamina` / `b_stamina` are `agg_stamina()` of the column ledger, the one the contact
    draw's `rounds_d` reads (step 2): after eighteen ticks of contact the number returned is below STAMINA_MAX for both sides,
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


# ---- B19.13: the column's drain scales with the exposure of its contact (MBA-04 step 6) -----------------------------------

def _tired_after_six_ticks(face, seed):
    """B's column stamina (its `agg_stamina()`) after six ticks of one contact with A, B turned to `face` (toward A = struck front,
    68 degrees off = struck on the flank). One body a side, the same footprint; only B's facing differs. Every tick is resolved at the
    one `t`, so B's wheel clock does not tick and the arc it was struck at holds for the six ticks (the drain is the thing under test,
    not the wheel). Returns (B's stamina, B's exposure on the contact, B's engaged-column drain per tick before the arc)."""
    import importlib
    from modules.mass_battle import orchestration as orch, rngsource
    from modules.mass_battle.core import contact
    from modules.mass_battle.hierarchy.units import Army, Unit
    from modules.mass_battle.percell import update_stamina
    resolution = importlib.import_module('modules.mass_battle.resolution')

    def body(pos, adv, fac):
        su = Unit(shape='Line', troop_type='infantry', tier=2, starting_position=pos, advance_dir=adv)
        return Army(name=fac, faction=fac, power=4, command=4, discipline=5, discipline_start=5, morale=6, morale_start=6, units=[su], dr=1), su
    with rngsource.using(draw_seeded(seed)), resolution.tracing() as ev:
        ub, sub_b = body((25, 12), -1, 'B')
        for cid in list(sub_b.cell_troops):
            sub_b.cell_facing_vec[cid] = face
        ua, _ = body((22, 12), +1, 'A')
        pairs = contact.find_contacts(ua, ub)
        assert pairs, "no contact: the geometry is wrong"
        for _ in range(6):
            orch.resolve_engagements(ua, ub, pairs, t=5)
            update_stamina(ua, pairs)
            update_stamina(ub, pairs)
    melee = [e for e in ev if e['cat'] == 'melee']
    return ub.agg_stamina(), melee[0]['exp_b'], ub


_FLANK = (-0.3746, 0.9272)   # B turned 68 degrees off the attacker: the octagon's flank read, `arc_d` 1.5 on the contact


def draw_seeded(seed):
    from engine.dice_engine import draw
    return draw.seeded(draw.H2("test_mass_battle_entry_stamina_b1913", seed))


def test_a_flank_contact_drains_faster_than_a_frontal_one():
    """Two equal columns struck by the one attacker, one front (`arc_d` 1.0) and one on the flank (`arc_d` 1.5): after six ticks the
    flank column's stamina share is lower (the drain is scaled by `exposure_d / EXPOSURE_BASE`, MBA §1.4). Control, on the same runs:
    the frontal contact is at `exposure_d = EXPOSURE_BASE` (no posture, arc 1, no crowding, no cover) and drains exactly the
    `MB_STAMINA_DRAIN` it drained before the edit."""
    from modules.mass_battle.config import MB_DEPTH_ROTATE, MB_STAMINA_DRAIN
    from modules.mass_battle.core.contact_draw import EXPOSURE_BASE
    checked = 0
    for seed in range(100):
        front, e_front, ub_front = _tired_after_six_ticks((-1.0, 0.0), seed)
        flank, e_flank, _ = _tired_after_six_ticks(_FLANK, seed)
        assert e_flank == pytest.approx(1.5 * e_front), (seed, e_front, e_flank)       # the arc is the only difference
        assert flank < front, (seed, front, flank)
        if seed == 0:
            assert e_front == EXPOSURE_BASE                                              # the control contact
            engaged = [b for b in ub_front.col_grid if b.stamina < STAMINA_MAX]
            assert engaged and all(b.stamina == STAMINA_MAX - 6 * MB_STAMINA_DRAIN / (1.0 + MB_DEPTH_ROTATE * (b.depth - 1))
                                   for b in engaged)
        checked += 1
    assert checked >= 100
