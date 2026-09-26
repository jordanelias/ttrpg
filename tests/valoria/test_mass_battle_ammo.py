"""A6, ED-MB-0067 Part A (proposals/2026-09-25-squad-engagement-synthesis.md) — missile ammunition
and resupply.

`Subunit.volleys`/`eff_volleys`/`drain_volleys`/`resupply_volleys` (hierarchy/units.py) -- a
per-SUBUNIT ledger mirroring `stamina`'s own existing own-else-inherited-Unit pattern exactly.
`orchestration.volley_phase`'s `fire()` gates on it before target selection and drains it on every
real shot; `between_turn_recovery` resupplies it, per-subunit, at the between-turn lull.

[adversarial-pass rework] A first version put this on percell._ColBlock (per-column-block, matching
stamina's OTHER, column-block-granularity ledger). Reworked after review found that structurally
unsound: a column position is shared across whatever subunits currently occupy it (see
percell.build_column_grid/sync_col_grid), so ammo tracked there could regenerate for free (a
subunit shifting onto a new column under MB_CLOSE_RANKS=1) or silently stop being metered at all
(an empty column lookup under MB_CLOSE_RANKS=0). Ammo belongs to the shooter, not to a column other
subunits pass through.

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
import random

import pytest

import systems.mass_battle.sim.orchestration as _orch
from systems.mass_battle.sim.config import (SIDE_A_START_ROW, SIDE_B_START_ROW, MB_VOLLEYS_START,
                                             MB_VOLLEYS_RESUPPLY, MB_KITE_STANDOFF, VOLLEY_MAX_RANGE)
from systems.mass_battle.sim.engine import build_army
from systems.mass_battle.sim.hierarchy.units import Subunit, Unit
from systems.mass_battle.sim.orchestration import volley_phase, between_turn_recovery


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
    su = Subunit(shape='Line', troop_type='archers', tier=2,
                 starting_position=(row, col), advance_dir=(-1 if faction == 'A' else 1),
                 stance='hold', unit_type='ranged')
    return Unit(name=f'{faction}_archers', faction=faction, power=4, command=4, discipline=5,
                discipline_start=5, morale=6, morale_start=6, subunits=[su])


def _target(faction='B', row=SIDE_A_START_ROW - 5, col=25):
    su = Subunit(shape='Line', troop_type='infantry', tier=2,
                 starting_position=(row, col), advance_dir=(-1 if faction == 'A' else 1),
                 stance='hold', unit_type='melee')
    return Unit(name=f'{faction}_target', faction=faction, power=4, command=4, discipline=5,
                discipline_start=5, morale=6, morale_start=6, subunits=[su])


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
        [sys.executable, '-c', 'from systems.mass_battle.sim.config import MB_AMMO_ENABLED; print(MB_AMMO_ENABLED)'],
        cwd=os.path.join(os.path.dirname(__file__), '..', '..'), env=env, capture_output=True, text=True, timeout=30)
    assert out.stdout.strip() == 'True', f"MB_AMMO_ENABLED must default ON; got {out.stdout!r} / {out.stderr[-300:]}"


def test_subunit_starts_at_the_configured_volley_count():
    ua = _archers()
    su = ua.subunits[0]
    assert su.eff_volleys == pytest.approx(MB_VOLLEYS_START)


def test_volley_phase_is_in_range_control():
    """Control: the two formations are actually within volley range before any ammo assertion is
    trusted -- otherwise 'stops firing' would be indistinguishable from 'was never in range'."""
    ua, ub = _archers(), _target()
    random.seed(4_100_001)
    r = volley_phase(ua, ub)
    assert r['shots'] >= 1, f"control failed: no shots fired at all (out of range?) -- {r}"


def test_ranged_atom_stops_contributing_damage_once_volleys_are_exhausted():
    ua, ub = _archers(), _target()
    su = ua.subunits[0]
    random.seed(4_100_002)
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


def test_between_turn_recovery_resupplies_some_volleys():
    ua = _archers()
    su = ua.subunits[0]
    su.volleys = 0.0
    between_turn_recovery(ua)
    assert su.eff_volleys == pytest.approx(min(MB_VOLLEYS_START, MB_VOLLEYS_RESUPPLY))
    assert su.eff_volleys > 0


def test_resupply_does_not_exceed_the_starting_count():
    ua = _archers()
    su = ua.subunits[0]
    between_turn_recovery(ua)   # already at MB_VOLLEYS_START -- must clamp, not overshoot
    assert su.eff_volleys == pytest.approx(MB_VOLLEYS_START)


def test_melee_atoms_are_never_gated_by_ammo():
    """Control: a melee atom's own volleys count (present via the same own-else-inherited-Unit
    ledger every Subunit has) is never read -- unit_type != 'ranged' short-circuits fire() before
    the ammo check. Drain it to 0 directly and confirm melee combat is unaffected by calling
    volley_phase (which must simply not involve this atom at all -- it is not 'ranged')."""
    ua, ub = _target(faction='A', row=SIDE_A_START_ROW), _target(faction='B', row=SIDE_A_START_ROW - 5)
    ua.subunits[0].volleys = 0.0
    random.seed(4_100_003)
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
    su = ua.subunits[0]
    su.drain_volleys(4)
    assert su.eff_volleys == pytest.approx(MB_VOLLEYS_START - 4)
    # Simulate a formation reshuffle: the subunit's cells move to entirely different absolute
    # columns (what MB_CLOSE_RANKS's file-shifting looks like from the ammo ledger's point of view).
    for cid in list(su.cell_offsets_c.keys()):
        su.cell_offsets_c[cid] = su.cell_offsets_c[cid] + 50
    assert su.eff_volleys == pytest.approx(MB_VOLLEYS_START - 4), \
        "ammo must be unaffected by a column-identity shift -- it lives on the subunit, not a column"


def test_eff_volleys_inherits_from_the_parent_unit_when_unseeded():
    """Same own-else-inherited-Unit pattern as eff_stamina: an unseeded subunit (volleys=None, the
    dataclass default) reads the parent Unit's own pool, not a fixed constant."""
    su = Subunit(shape='Line', troop_type='archers', tier=2, starting_position=(SIDE_A_START_ROW, 25),
                 advance_dir=-1, stance='hold', unit_type='ranged')
    assert su.volleys is None
    u = Unit(name='u', faction='A', power=4, command=4, discipline=5, discipline_start=5,
             morale=6, morale_start=6, subunits=[su])
    u.volleys = 17.0   # override the Unit's own pool directly
    assert su.eff_volleys == pytest.approx(17.0), "an unseeded subunit must read the parent Unit's pool"
    su.drain_volleys(5)
    assert u.volleys == pytest.approx(12.0), "draining an inheriting subunit must write back to the Unit"


# ─── Adversarial-review round 2: F4 (the real army builder) + F7 (kite) ─────

def test_build_army_gives_a_ranged_subunit_its_own_ammo_pool_not_shared_with_melee_siblings():
    """F4 [HIGH]: build_army's per-subunit kwarg-forwarding tuple was MISSING 'volleys' entirely --
    not merely unseeded like morale used to be before DG-4, never forwarded at all -- so every
    ranged subunit built through the PUBLIC, workbench-facing army constructor fell through to
    Subunit.volleys=None -> eff_volleys inherits the ONE shared parent Unit pool, and
    between_turn_recovery's per-subunit resupply call runs for every OTHER subunit too (melee
    siblings included, unconditionally) -- a full refill every turn instead of the intended
    trickle. The exact column-block-style sharing bug A6's own ledger move already fixed once,
    relocated one level up from 'per-column' to 'per-Unit'. Uses build_army directly (not raw
    Subunit/Unit construction), per the review's own instruction, since this is a defect in the
    CONSTRUCTOR, not in the ledger primitives the other tests above already cover directly."""
    u = build_army([
        {'shape': 'Line', 'troop_type': 'archers', 'tier': 2, 'unit_type': 'ranged'},
        {'shape': 'Line', 'troop_type': 'infantry', 'tier': 2, 'unit_type': 'melee'},
        {'shape': 'Line', 'troop_type': 'infantry', 'tier': 2, 'unit_type': 'melee'},
    ], name='mix', faction='A')
    archer, m1, m2 = u.subunits
    assert archer.volleys is not None, "a ranged subunit built via build_army must get its OWN pool, not inherit"
    assert archer.eff_volleys == pytest.approx(MB_VOLLEYS_START)
    archer.drain_volleys(4)
    # Every OTHER subunit (melee, unconditionally) also gets a resupply call every turn, matching
    # between_turn_recovery's own per-atom loop shape -- simulated directly here.
    for atom in u.subunits:
        atom.resupply_volleys(MB_VOLLEYS_RESUPPLY)
    assert archer.eff_volleys == pytest.approx(min(MB_VOLLEYS_START, MB_VOLLEYS_START - 4 + MB_VOLLEYS_RESUPPLY)), \
        "the archer's own pool must reflect exactly ITS OWN drain+resupply, not inflated by siblings' calls"
    assert u.volleys == pytest.approx(MB_VOLLEYS_START), \
        "melee siblings still inherit the shared Unit pool (harmless -- never read for combat), " \
        "untouched by the archer's own now-separate pool"


def test_build_army_spec_can_still_override_volleys_explicitly():
    """The per-subunit forwarding tuple fix must not just ADD seeding -- an explicit spec override
    must still win, the same precedence every other per-subunit stat in this constructor has."""
    u = build_army([{'shape': 'Line', 'troop_type': 'archers', 'tier': 2, 'unit_type': 'ranged',
                      'volleys': 3.0}], name='u', faction='A')
    assert u.subunits[0].eff_volleys == pytest.approx(3.0)


def test_kiter_closes_to_melee_once_out_of_ammo():
    """F7: a ranged kiter's far standoff bound used to key on unit_type=='ranged' alone,
    unconditionally -- an empty kiter (Subunit.eff_volleys <= 0) kept holding the WIDE volley-range
    standoff band forever, 'keeping volleying' a weapon that can no longer fire: a decorative unit
    for the rest of the battle. Must fall back to the melee reach bound once out of ammo, so it
    closes in and re-engages instead."""
    su = Subunit(shape='Line', troop_type='archers', tier=2, starting_position=(SIDE_A_START_ROW, 25),
                 advance_dir=-1, stance='hold', unit_type='ranged', instructions=('kite',))
    Unit(name='u', faction='A', power=4, command=4, discipline=5, discipline_start=5,
         morale=6, morale_start=6, subunits=[su])
    ar, ac = su._node_anchor
    assert MB_KITE_STANDOFF < 6 < VOLLEY_MAX_RANGE, \
        "control: this distance must fall inside the OLD (ammo-blind) in-band volley window"
    enemy_cells = [(ar, ac - 6)]
    assert su.eff_volleys > 0
    assert su._kite_goal(enemy_cells) == (ar, ac), "control: with ammo, must still hold the wide volley band (in-band)"
    su.volleys = 0.0
    assert su._kite_goal(enemy_cells) is None, \
        "out of ammo, far_bound must fall back to melee reach -- 6 is far beyond reach_for('archers') -> close in (None)"
