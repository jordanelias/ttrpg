"""core/volley.py -- Phase 2 volley, moved out of `orchestration.py` unchanged (B19.10, ED-1043).

`_roll_volley_pool`, `_atom_distance` and `_volley_density_mult` are the helpers only `volley_phase` calls; they moved with it
so this module imports nothing from `orchestration` (no cycle). `orchestration` re-imports the names its callers use, so they are
unchanged. A flag read here is read from THIS module's namespace: a test that flips one patches it here."""
from engine.dice_engine import fmath
from modules.mass_battle.config import *
from modules.mass_battle.resolution import roll_pool, trace_event

__all__ = ['volley_phase', '_roll_volley_pool', '_atom_distance', '_volley_density_mult']


# [canonical: mass_battle_v30.md §A.7 Phase 2 — Volley fires before Manoeuvre.
#  PP-503: Volley pool = Power dice. Net successes − ranged DR = Size loss.
#  ⚠ PP-503's "vs TN 6" is SUPERSEDED — TN is 7 always (ED-MB-0066, under ED-IN-0196).
#  Damage recorded in Phase 2 but APPLIED at Phase 6 Step 1 (simultaneous with engagement).]

def _atom_distance(atom_a, atom_b):
    """Nearest-cell distance between two atoms. Chebyshev (king-move) on the integer grid; EUCLIDEAN on the
    coordinate field (FIELD_MOVEMENT) so a diagonal approach is not counted 'free' — circular range rings
    (movement-substrate review 06, finding 1 / migration S2). Byte-exact OFF (the Chebyshev branch)."""
    cells_a = atom_a.cells()
    cells_b = atom_b.cells()
    if not cells_a or not cells_b:
        return float('inf')
    best = float('inf')
    for (ra, ca) in cells_a:
        for (rb, cb) in cells_b:
            d = fmath.hypot(ra - rb, ca - cb) if FIELD_MOVEMENT else max(abs(ra - rb), abs(ca - cb))
            if d < best:
                best = d
                if best == 0:
                    return 0
    return best


def _roll_volley_pool(power_dice):
    """Roll power_dice d10s at TN 7, floored at 0. Returns net successes.

    [canonical: mass_battle_v30.md §A.1 dice engine — 1=-1, 7-9=+1, 10=+2]
    [canonical: Jordan ruling 2026-08-25 "TN7 always. Never change TN anywhere ever." — ED-MB-0066]

    Delegates to resolution.roll_pool: one die rule, one rngsource draw per die. The `power_dice <= 0`
    guard is retained deliberately — roll_pool clamps to a 1-die minimum (PP-273), which is an
    engagement-pool rule that volley must not inherit. The max(0, …) floor is likewise retained.
    """
    if power_dice <= 0:
        return 0
    return max(0, roll_pool(power_dice))


def _volley_density_mult(target_unit):
    """Missile-vulnerability of the TARGET formation: packed/deep columns catch overshoot and
    cannot disperse, so they bleed more under volley (Carrhae/Agincourt/Crecy); a dispersed or
    shallow line takes far fewer hits. 1.0 at the reference line density. Ranged-only path ->
    the melee gauge never reaches it (byte-exact).
    [bottom-up: col_grid density = troops/cell x ranks. historical anchor: massed-formation missile losses.]"""
    if not MB_VOLLEY_DENSITY_ENABLED:
        return 1.0
    grid = getattr(target_unit, 'col_grid', None)
    if not grid:
        return 1.0
    mean_density = sum(b.density for b in grid) / len(grid)
    return max(MB_VOLLEY_DENSITY_FLOOR, min(MB_VOLLEY_DENSITY_CAP, mean_density / MB_VOLLEY_DENSITY_REF))

def volley_phase(unit_a, unit_b):
    """Phase 2 Volley. Each ranged atom selects nearest in-range enemy atom and fires.
    Returns dict of total Size-loss to each side (applied simultaneously at end of turn).
    Pool = Power; TN 7 (ED-MB-0066); ranged DR subtracts from net successes.
    [canonical: mass_battle_v30.md §A.7 Phase 2 Volley; params/mass_combat.md §Ranged DR Table]
    """
    if not VOLLEY_ENABLED:
        return {"loss_a": 0, "loss_b": 0, "shots": 0}

    loss_a = loss_b = 0
    shots = 0

    def fire(shooter_atom, shooter_unit, target_unit):
        """Pick nearest in-range target atom, roll Power vs TN, return Size loss inflicted.
        Volley loss scales with the TARGET formation's density (_volley_density_mult)."""
        if shooter_atom.unit_type != "ranged":
            return 0, None, False
        # [DG-2 §2.3/2.5, Jordan-ruled "build it now" 2026-07-08] "No volleying while yielding" --
        # a body actively repositioning doesn't also fire, matching the existing 'kite' precedent.
        # `yield_active` is already melee-only-gated, so this only ever fires for a ranged atom in
        # the (currently unreachable, by construction) case its unit_type somehow flips mid-battle;
        # kept for defence-in-depth, not because it's expected to trigger today.
        if shooter_atom.yield_active:
            return 0, None, False
        # [A6, ED-MB-0067 Part A -- squad-engagement synthesis, "Missile ammunition and resupply"]
        # Ammunition: a subunit out of volleys stops contributing missile output entirely -- there
        # is no melee-fallback concept for a 'ranged' unit_type in this sim (confirmed by grep for a
        # stance/profile switch keyed on ammo), so "stops firing" is the whole effect.
        # Unit.eff_volleys (own-else-inherited-Army) -- NOT a per-column-block
        # ledger: ammo tracked on a column position other units could occupy would either regenerate for free
        # (MB_CLOSE_RANKS=1) or stop being metered (MB_CLOSE_RANKS=0) -- see percell._ColBlock's own note and
        # Unit.volleys' own note.
        if MB_AMMO_ENABLED and shooter_atom.eff_volleys <= 0:
            return 0, None, False
        target_atoms = target_unit.units
        # E (atomized archer targeting): an archer ORDERED to a specific or weakest target fires at IT when
        # in range, else the nearest -- so archers can be directed at a flanker / priority unit. Gated by
        # MB_VOLLEY_TARGETING + an explicit order; default (no order) = nearest (the exact prior logic) ->
        # byte-exact. The ORDERED portion is concentrated on the target subunit downstream (apply_to_subunit);
        # unordered fire stays faction-spread. [canonical: longbow fire discipline, Crecy/Agincourt; §A.7.]
        _ordered = None
        if MB_VOLLEY_TARGETING:
            _oti = getattr(shooter_atom, 'order_target_idx', None)
            if _oti is not None and _oti < len(target_atoms):
                _ordered = target_atoms[_oti]
            elif getattr(shooter_atom, 'target_condition', None) == 'weakest':
                _cand = [t for t in target_atoms
                         if VOLLEY_MIN_RANGE <= _atom_distance(shooter_atom, t) <= VOLLEY_MAX_RANGE]
                if _cand:
                    _ordered = min(_cand, key=lambda t: sum(t.cell_troops.values()) if t.cell_troops else 0)
        best_target = None
        best_dist = float('inf')
        was_ordered = False
        if _ordered is not None and VOLLEY_MIN_RANGE <= _atom_distance(shooter_atom, _ordered) <= VOLLEY_MAX_RANGE:
            best_target = _ordered
            best_dist = _atom_distance(shooter_atom, _ordered)
            was_ordered = True
        else:
            for t in target_atoms:
                d = _atom_distance(shooter_atom, t)
                if VOLLEY_MIN_RANGE <= d <= VOLLEY_MAX_RANGE and d < best_dist:
                    best_dist = d
                    best_target = t
        if best_target is None:
            return 0, None, False
        # Pool = unit Power dice (PP-503). Discipline penalty applies (per §A.4).
        _vdisc = shooter_atom.eff_discipline   # per-subunit volley pool (Jordan directive): shooter subunit's power + discipline
        _vpen = 0 if _vdisc >= 5 else (1 if _vdisc >= 3 else (2 if _vdisc >= 1 else 99))  # [canonical: mass_battle_v30.md §A.4 — volley discipline penalty tiers]
        pool = max(1, shooter_atom.eff_power - _vpen)
        net = _roll_volley_pool(pool)
        # DR subtracts from net successes (Ranged DR Table)
        # [ED-MB-0041 FIX] Use the TARGET's OWN armour, not a global constant. This line previously read
        # `max(0, net - RANGED_DR_DEFAULT)`, so a target's real `dr` never reduced incoming fire — armour
        # had no protective effect at all in the volley phase. RANGED_DR_DEFAULT remains the fallback for
        # a target with no own dr. [canonical: mass_battle_v30.md §A.4 Ranged DR table — DR subtracts from
        # net successes; None 0 / Light 1 / Medium 2 / Heavy 3 vs Piercing.]
        _tdr = getattr(best_target, 'eff_dr', None)
        net_after_dr = max(0, net - (_tdr if _tdr is not None else RANGED_DR_DEFAULT))
        if LANCHESTER_ENABLED:
            # P-L Square Law: aimed fire lifts the frontage cap — every shooter engages the
            # target area, so volley effectiveness scales with SHOOTER COUNT (toward N²-type
            # concentration over the integral). Distinct from the frontage-capped melee linear
            # term. [spec mb_lanchester_design.md §3b; Lanchester Square Law = ranged/aimed fire.]
            net_after_dr = net_after_dr * K_SQUARE * shooter_atom.eff_size
        dens = _volley_density_mult(target_unit)
        out = net_after_dr * dens
        # [A6] Decrement THIS shooter's own ammo on every tick it actually fires (a real target was
        # found and a shot resolved) -- not merely eligible to. drain_volleys floors at 0.
        if MB_AMMO_ENABLED:
            shooter_atom.drain_volleys(1)
        trace_event('volley', shooter=getattr(shooter_unit, 'name', '?'), d=best_dist,
                    pool=pool, net=net, net_dr=round(net_after_dr, 2),
                    dens=round(dens, 3), loss=round(out, 2))
        return out, best_target, was_ordered

    ordered_a = []
    ordered_b = []
    for atom in unit_a.units:
        dmg, tgt, was_ordered = fire(atom, unit_a, unit_b)
        if tgt is not None:
            loss_b += dmg
            shots += 1
            if was_ordered:
                ordered_b.append((tgt, dmg))
    for atom in unit_b.units:
        dmg, tgt, was_ordered = fire(atom, unit_b, unit_a)
        if tgt is not None:
            loss_a += dmg
            shots += 1
            if was_ordered:
                ordered_a.append((tgt, dmg))

    return {"loss_a": loss_a, "loss_b": loss_b, "shots": shots,
            "ordered_a": ordered_a, "ordered_b": ordered_b}
