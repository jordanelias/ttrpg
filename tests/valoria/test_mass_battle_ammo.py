"""A6, ED-MB-0067 Part A (proposals/2026-09-25-squad-engagement-synthesis.md) — missile ammunition
and resupply.

`Unit.volleys`/`eff_volleys`/`drain_volleys`/`resupply_volleys` (hierarchy/units.py) -- a
per-SUBUNIT ledger, own-else-inherited-Army (stamina, which once shared the pattern, is the column ledger alone, B19.07).
`orchestration.volley_phase`'s `fire()` gates on it before target selection and drains it on every
real shot; `between_turn_recovery` resupplies it, per-subunit, at the between-turn lull.

[adversarial-pass rework] A first version put this on percell._ColBlock (per-column-block, matching
stamina's OTHER, column-block-granularity ledger). Reworked after review found that structurally
unsound: a column position is shared across whatever units currently occupy it (see
percell.build_column_grid/sync_col_grid), so ammo tracked there could regenerate for free (a
subunit shifting onto a new column under MB_CLOSE_RANKS=1) or silently stop being metered at all
(an empty column lookup under MB_CLOSE_RANKS=0). Ammo belongs to the shooter, not to a column other
units pass through.

[adversarial-pass round 2, 2026-09-26] MB_AMMO_ENABLED DEFAULTS ON, per this file's own flags-ON
precedent. Round 1 shipped it OFF on the (wrong) premise that this sandbox could not produce a
CI-reference-accurate bat.py digest at all -- that premise was measured with a hand-rolled
invocation missing most of tools/ci_golden_modes_check.py's real pin vector, so it never actually
tested what it claimed to. Properly pinned (the real tool), this sandbox DOES reproduce the
committed golden for every mode the tool covers; see config.py's own note at MB_AMMO_ENABLED and
bat.py's EXPECTED comment for the actual re-recording. Every test below still sets the flag
explicitly (belt-and-braces against a future default change, and so this file never silently
depends on ambient state).

Campaign-adapter armies are melee-only (`massbattle.py`'s `_faction_to_unit`), so this path is
confirmed unreachable from the campaign seam separately (see the two engine/tests files run
alongside this one).
"""

import pytest

import modules.mass_battle.orchestration as _orch
from modules.mass_battle.config import (SIDE_A_START_ROW, SIDE_B_START_ROW, MB_VOLLEYS_START,
                                             MB_VOLLEYS_RESUPPLY, MB_KITE_STANDOFF)
from modules.mass_battle.troop_types.table import volley_range
from systems.mass_battle.sim.engine import build_army
from modules.mass_battle.hierarchy.units import Unit, Army
from modules.mass_battle.orchestration import volley_phase
from engine.dice_engine import draw  # noqa: E402
from modules.mass_battle import rngsource  # noqa: E402


@pytest.fixture(autouse=True)
def _ammo_on():
    """MB_AMMO_ENABLED now defaults ON (see module docstring) -- explicit here anyway so this file
    never depends on ambient state, restored after so a test elsewhere that expects the flag
    untouched can't be affected by import order."""
    saved = _orch.MB_AMMO_ENABLED
    _orch.MB_AMMO_ENABLED = True
    try:
        yield
    finally:
        _orch.MB_AMMO_ENABLED = saved


def _archers(faction='A', row=SIDE_A_START_ROW, col=25):
    su = Unit(shape='Line', troop_type='archers', tier=2,
                 starting_position=(row, col), advance_dir=(-1 if faction == 'A' else 1),
                 stance='hold', unit_type='ranged')
    return Army(name=f'{faction}_archers', faction=faction, power=4, command=4, discipline=5,
                discipline_start=5, morale=6, morale_start=6, units=[su])


def _target(faction='B', row=SIDE_A_START_ROW - 5, col=25):
    su = Unit(shape='Line', troop_type='infantry', tier=2,
                 starting_position=(row, col), advance_dir=(-1 if faction == 'A' else 1),
                 stance='hold', unit_type='melee')
    return Army(name=f'{faction}_target', faction=faction, power=4, command=4, discipline=5,
                discipline_start=5, morale=6, morale_start=6, units=[su])


def test_ammo_defaults_on_at_the_source():
    """[REVERSED at adversarial-pass round 2 -- see module docstring] The SHIPPED default is ON --
    checked against a subprocess with the env var unset entirely, not the runtime value this
    file's own autouse fixture mutates."""
    import os
    import subprocess
    import sys
    env = dict(os.environ)
    env.pop('MB_AMMO_ENABLED', None)
    out = subprocess.run(
        [sys.executable, '-c', 'from modules.mass_battle.config import MB_AMMO_ENABLED; print(MB_AMMO_ENABLED)'],
        cwd=os.path.join(os.path.dirname(__file__), '..', '..'), env=env, capture_output=True, text=True, timeout=30)
    assert out.stdout.strip() == 'True', f"MB_AMMO_ENABLED must default ON; got {out.stdout!r} / {out.stderr[-300:]}"


def test_subunit_starts_at_the_configured_volley_count():
    ua = _archers()
    su = ua.units[0]
    assert su.eff_volleys == pytest.approx(MB_VOLLEYS_START)


def test_volley_phase_is_in_range_control():
    """Control: the two formations are actually within volley range before any ammo assertion is
    trusted -- otherwise 'stops firing' would be indistinguishable from 'was never in range'."""
    ua, ub = _archers(), _target()
    with rngsource.using(draw.seeded(draw.H2("test_mass_battle_ammo", 4_100_001))):
        r = volley_phase(ua, ub)
        assert r['shots'] >= 1, f"control failed: no shots fired at all (out of range?) -- {r}"


def test_ranged_atom_stops_contributing_damage_once_volleys_are_exhausted():
    ua, ub = _archers(), _target()
    su = ua.units[0]
    with rngsource.using(draw.seeded(draw.H2("test_mass_battle_ammo", 4_100_002))):
        fired_ticks = 0
        exhausted_at = None
        for tick in range(1, int(MB_VOLLEYS_START) + 10):
            r = volley_phase(ua, ub)
            if r['shots'] >= 1:
                fired_ticks += 1
            if exhausted_at is None and su.eff_volleys <= 0:
                exhausted_at = tick
            if exhausted_at is not None and tick > exhausted_at:
                # past exhaustion: this atom must contribute nothing (loss_b stays 0 from unit A's side)
                assert r['loss_b'] == 0, f"tick {tick}: exhausted archer still dealt {r['loss_b']} loss"
                assert r['shots'] == 0, f"tick {tick}: exhausted archer still recorded a shot"
        assert exhausted_at is not None, "volleys never reached 0 across the whole loop -- test setup is wrong"
        assert fired_ticks >= 1, "the archer must have actually fired before running out"


def test_melee_atoms_are_never_gated_by_ammo():
    """Control: a melee atom's own volleys count (present via the same own-else-inherited-Army
    ledger every Unit has) is never read -- unit_type != 'ranged' short-circuits fire() before
    the ammo check. Drain it to 0 directly and confirm melee combat is unaffected by calling
    volley_phase (which must simply not involve this atom at all -- it is not 'ranged')."""
    ua, ub = _target(faction='A', row=SIDE_A_START_ROW), _target(faction='B', row=SIDE_A_START_ROW - 5)
    ua.units[0].volleys = 0.0
    with rngsource.using(draw.seeded(draw.H2("test_mass_battle_ammo", 4_100_003))):
        r = volley_phase(ua, ub)
        assert r['shots'] == 0 and r['loss_a'] == 0 and r['loss_b'] == 0, \
            "neither side is 'ranged' -- volley_phase must be a pure no-op regardless of ammo state"


# ─── Adversarial-review round 2: the per-subunit ledger itself ──────────────

def test_ammo_is_independent_of_column_identity():
    """Regression for the exact defect that moved ammo off percell._ColBlock: shifting which
    absolute columns a subunit's cells occupy (simulated directly here, since a real MB_CLOSE_RANKS
    reshuffle is a much larger apparatus to construct) must not touch its ammo at all -- there is no
    column lookup left in the ammo path to desync."""
    ua = _archers()
    su = ua.units[0]
    su.drain_volleys(4)
    assert su.eff_volleys == pytest.approx(MB_VOLLEYS_START - 4)
    # Simulate a formation reshuffle: the subunit's cells move to entirely different absolute
    # columns (what MB_CLOSE_RANKS's file-shifting looks like from the ammo ledger's point of view).
    for cid in list(su.cell_offsets_c.keys()):
        su.cell_offsets_c[cid] = su.cell_offsets_c[cid] + 50
    assert su.eff_volleys == pytest.approx(MB_VOLLEYS_START - 4), \
        "ammo must be unaffected by a column-identity shift -- it lives on the subunit, not a column"


def test_eff_volleys_inherits_from_the_parent_unit_when_unseeded():
    """Own-else-inherited-Army pattern: an unseeded subunit (volleys=None, the
    dataclass default) reads the parent Army's own pool, not a fixed constant."""
    su = Unit(shape='Line', troop_type='archers', tier=2, starting_position=(SIDE_A_START_ROW, 25),
                 advance_dir=-1, stance='hold', unit_type='ranged')
    assert su.volleys is None
    u = Army(name='u', faction='A', power=4, command=4, discipline=5, discipline_start=5,
             morale=6, morale_start=6, units=[su])
    u.volleys = 17.0   # override the Army's own pool directly
    assert su.eff_volleys == pytest.approx(17.0), "an unseeded subunit must read the parent Army's pool"
    su.drain_volleys(5)
    assert u.volleys == pytest.approx(12.0), "draining an inheriting subunit must write back to the Army"


# ─── Adversarial-review round 2: F4 (the real army builder) + F7 (kite) ─────

def test_build_army_gives_a_ranged_subunit_its_own_ammo_pool_not_shared_with_melee_siblings():
    """F4 [HIGH]: build_army's per-subunit kwarg-forwarding tuple was MISSING 'volleys' entirely --
    not merely unseeded like morale used to be before DG-4, never forwarded at all -- so every
    ranged subunit built through the PUBLIC, workbench-facing army constructor fell through to
    Unit.volleys=None -> eff_volleys inherits the ONE shared parent Army pool, and
    between_turn_recovery's per-subunit resupply call runs for every OTHER subunit too (melee
    siblings included, unconditionally) -- a full refill every turn instead of the intended
    trickle. The exact column-block-style sharing bug A6's own ledger move already fixed once,
    relocated one level up from 'per-column' to 'per-Army'. Uses build_army directly (not raw
    Unit/Army construction), per the review's own instruction, since this is a defect in the
    CONSTRUCTOR, not in the ledger primitives the other tests above already cover directly."""
    u = build_army([
        {'shape': 'Line', 'troop_type': 'archers', 'tier': 2, 'unit_type': 'ranged'},
        {'shape': 'Line', 'troop_type': 'infantry', 'tier': 2, 'unit_type': 'melee'},
        {'shape': 'Line', 'troop_type': 'infantry', 'tier': 2, 'unit_type': 'melee'},
    ], name='mix', faction='A')
    archer, m1, m2 = u.units
    assert archer.volleys is not None, "a ranged subunit built via build_army must get its OWN pool, not inherit"
    assert archer.eff_volleys == pytest.approx(MB_VOLLEYS_START)
    archer.drain_volleys(4)
    # Every OTHER subunit (melee, unconditionally) also gets a resupply call every turn, matching
    # between_turn_recovery's own per-atom loop shape -- simulated directly here.
    for atom in u.units:
        atom.resupply_volleys(MB_VOLLEYS_RESUPPLY)
    assert archer.eff_volleys == pytest.approx(min(MB_VOLLEYS_START, MB_VOLLEYS_START - 4 + MB_VOLLEYS_RESUPPLY)), \
        "the archer's own pool must reflect exactly ITS OWN drain+resupply, not inflated by siblings' calls"
    assert u.volleys == pytest.approx(MB_VOLLEYS_START), \
        "melee siblings still inherit the shared Army pool (harmless -- never read for combat), " \
        "untouched by the archer's own now-separate pool"


def test_build_army_spec_can_still_override_volleys_explicitly():
    """The per-subunit forwarding tuple fix must not just ADD seeding -- an explicit spec override
    must still win, the same precedence every other per-subunit stat in this constructor has."""
    u = build_army([{'shape': 'Line', 'troop_type': 'archers', 'tier': 2, 'unit_type': 'ranged',
                      'volleys': 3.0}], name='u', faction='A')
    assert u.units[0].eff_volleys == pytest.approx(3.0)


def test_kiter_closes_to_melee_once_out_of_ammo():
    """F7: a ranged kiter's far standoff bound used to key on unit_type=='ranged' alone,
    unconditionally -- an empty kiter (Unit.eff_volleys <= 0) kept holding the WIDE volley-range
    standoff band forever, 'keeping volleying' a weapon that can no longer fire: a decorative unit
    for the rest of the battle. Must fall back to the melee reach bound once out of ammo, so it
    closes in and re-engages instead."""
    su = Unit(shape='Line', troop_type='archers', tier=2, starting_position=(SIDE_A_START_ROW, 25),
                 advance_dir=-1, stance='hold', unit_type='ranged', instructions=('kite',))
    Army(name='u', faction='A', power=4, command=4, discipline=5, discipline_start=5,
         morale=6, morale_start=6, units=[su])
    ar, ac = su._node_anchor
    assert MB_KITE_STANDOFF < 6 < volley_range('archers')[1], \
        "control: this distance must fall inside the OLD (ammo-blind) in-band volley window"
    enemy_cells = [(ar, ac - 6)]
    assert su.eff_volleys > 0
    assert su._kite_goal(enemy_cells) == (ar, ac), "control: with ammo, must still hold the wide volley band (in-band)"
    su.volleys = 0.0
    assert su._kite_goal(enemy_cells) is None, \
        "out of ammo, far_bound must fall back to melee reach -- 6 is far beyond reach_for('archers') -> close in (None)"


# ─── B19.21: a missile arm's reach is its own column (`references/troops.yaml: arms.<key>.range`) ──────────────
# Each test below sets the SOURCED ranges (`range_stated`: javelin [1, 6], bow and crossbow [2, 40]) in the loaded document, in this
# process only, so it reads the flipped data (B19.24) and is green at the control ([2, 8] for every arm) all the same.

def _with_arm_ranges(monkeypatch, opening_rows=None, **ranges):
    """The loaded troop file with `arms.<key>.range` set for each key given (and `formations.line.opening_rows`, if given), as the one document
    `table` reads."""
    import copy
    from modules.mass_battle.troop_types import table
    doc = copy.deepcopy(table._data())
    for arm, rng in ranges.items():
        doc['arms'][arm]['range'] = list(rng)
    if opening_rows is not None:
        doc['formations']['line']['opening_rows'] = opening_rows
    table.check(doc)
    monkeypatch.setattr(table, '_data', lambda: doc)
    return doc


def _shooter(troop_type, row=SIDE_A_START_ROW, col=25):
    su = Unit(shape='Line', troop_type=troop_type, tier=2, starting_position=(row, col), advance_dir=-1,
              stance='hold', unit_type='ranged')
    return Army(name='A_shooters', faction='A', power=4, command=4, discipline=5, discipline_start=5,
                morale=6, morale_start=6, units=[su])


def _foe_at(shooter, distance, col=25):
    """An enemy body whose nearest cell is exactly `distance` from the shooter's (`volley._atom_distance`)."""
    from modules.mass_battle.core.volley import _atom_distance
    for back in range(0, 60):
        foe = _target(row=SIDE_A_START_ROW - back, col=col)
        if _atom_distance(shooter.units[0], foe.units[0]) == distance:
            return foe
    raise AssertionError(f"no row puts an enemy body exactly {distance} cells off")


def _shots(shooter, foe, seed):
    with rngsource.using(draw.seeded(draw.H2("test_mass_battle_ammo", seed))):
        return volley_phase(shooter, foe)['shots']


def test_javelin_range_is_six(monkeypatch):
    """CLASS game-state, lane mass_battle. A javelin body does not shoot at an enemy seven cells off; a bow body does (gate 4).
    THE CONTROL IS THE SAME ENEMY: the javelin body does shoot it at six, and the bow body's ammunition falls by the shot it fired, so the
    silence at seven is the arm's range and not a body that cannot fire."""
    _with_arm_ranges(monkeypatch, javelin=(1, 6), bow=(2, 40))
    jav, bow = _shooter('skirmishers'), _shooter('archers')
    assert _shots(jav, _foe_at(jav, 7), 4_210_001) == 0, "a javelin body shot an enemy seven cells off"
    assert jav.units[0].eff_volleys == pytest.approx(MB_VOLLEYS_START), "a javelin body that did not shoot spent a volley"
    assert _shots(jav, _foe_at(jav, 6), 4_210_002) == 1, "control: the javelin body does not shoot at six"
    assert jav.units[0].eff_volleys == pytest.approx(MB_VOLLEYS_START - 1)
    assert _shots(bow, _foe_at(bow, 7), 4_210_003) == 1, "a bow body did not shoot an enemy seven cells off"
    assert bow.units[0].eff_volleys == pytest.approx(MB_VOLLEYS_START - 1)


def test_a_body_in_contact_does_not_volley(monkeypatch):
    """CLASS game-state, lane mass_battle. An archer body with no switch order whose only enemy is in contact (one cell off, inside its arm's
    least range) fires nothing: its volley count after the tick is zero and its stock is unspent (gate 3). THE CONTROL IS THE SAME BODY: at
    its arm's least range it fires, so the silence is the contact and not a body out of ammunition. NOT OBSERVED, because the mechanism is not
    in the tree: `04_MB_unit_loadout_and_weapon_in_hand_B.md`'s rule 'as amended' (a body in contact does not volley at ANOTHER body in
    range); today a body in contact with one enemy body can still shoot a second one, and no test here says it cannot."""
    from modules.mass_battle.troop_types import table
    _with_arm_ranges(monkeypatch, bow=(3, 40))      # least 3, not the stated 2, so the arm's column and not the old one band (2) is what is read
    least = table.volley_range('archers')[0]
    assert least == 3
    archers = _shooter('archers')
    for near in (1, least - 1):                     # in contact, and inside the least range
        assert _shots(archers, _foe_at(archers, near), 4_210_004 + near) == 0, f"a body with an enemy {near} cell(s) off volleyed"
        assert archers.units[0].eff_volleys == pytest.approx(MB_VOLLEYS_START), "a body in contact spent a volley"
    assert _shots(archers, _foe_at(archers, least), 4_210_005) == 1, "control: the body does not shoot at its arm's least range"
    assert archers.units[0].eff_volleys == pytest.approx(MB_VOLLEYS_START - 1)


def _volleys_before_contact(oob_a, oob_b, n, first):
    """Per field of `n` seeds: the 'volley' events the engine traced before its first 'melee' event (the first pair in contact)."""
    from engine.season.queries.inputs import MassBattleInput
    from modules.mass_battle import massbattle
    from modules.mass_battle.resolution import tracing
    rec = MassBattleInput(weights=((10,), (10,)), territory=None, fort_level=0.0, stances=(0.0, 0.0), walls_dr=None, origin=None,
                          loyalties=(0.0, 0.0), loyalty_gain=0, geography={}, condition_scale=1.0, orders_of_battle=(oob_a, oob_b))
    out = []
    for s in range(first, first + n):
        with tracing() as events:
            massbattle.resolve_field(rec, draw.seeded(draw.H2("test_mass_battle_ammo", s)))
        seen = 0
        for e in events:
            if e['cat'] == 'melee':
                break
            seen += e['cat'] == 'volley'
        out.append(seen)
    return out


def test_bows_shoot_before_contact(monkeypatch):
    """CLASS game-state, lane mass_battle. Bows at their stated [2, 40] against foot, n 200: volley events before the first contact are above
    zero in every field, and above the control's (gate 2). THE CONTROL IS THE SAME 200 SEEDS on the shipped data ([2, 8], three rows apart).
    The stated world is the flipped one: `opening_rows: auto` too (B19.24 and B19.25 flip the two, and the opening is what puts the bows out of
    reach of the enemy at the start). DEVIATION FROM THE GATE'S TEXT, measured: the gate says the control's bows shoot 'at most two ticks'
    worth' before contact; the tree's control fires FOUR (the archers stand seven cells from the enemy line from the first tick, inside
    [2, 8]), so the bound is read against the stated world's count, not against two."""
    from modules.mass_battle.orderofbattle import OrderOfBattle, UnitRow
    bows = OrderOfBattle((UnitRow('wall', 'heavy_infantry', 300), UnitRow('bows', 'archers', 200)))
    foot = OrderOfBattle((UnitRow('wall', 'heavy_infantry', 500),))
    n = 200
    control = _volleys_before_contact(bows, foot, n, 7_000)
    _with_arm_ranges(monkeypatch, opening_rows='auto', bow=(2, 40))
    stated = _volleys_before_contact(bows, foot, n, 7_000)
    assert len(control) == len(stated) == n
    assert min(stated) > 0, f"a field where the bows shot nothing before contact at [2, 40]: {sorted(set(stated))}"
    assert max(control) < min(stated), f"the stated bows shot no more before contact than the control's: {sorted(set(control))} vs {sorted(set(stated))}"
