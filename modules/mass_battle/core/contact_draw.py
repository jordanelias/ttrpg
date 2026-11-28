"""core/contact_draw.py -- the contact draw (MBA-04) and the melee pair that calls it; the pursuit.

`ContactVector` and `contact_casualties` (B19.11, MBA-04 step 1) are the contact draw itself, a pure function of the vector, the
measured table and a handed-in `z`. `resolve_melee_pair` (moved out of `resolve_engagements` at B19.10, ED-1043) builds the two vectors
of one contact per tick (B19.12, MBA-04 step 2: `contact_vector`, the builder) and draws each side's casualties: the pool, the sigma
head, the opposed degree and the degree-to-damage table left the melee pair here. Each draw's `z` is keyed `(field, bout, tick, pair, side,
"contact")` on the field's `Draw` (`contact_z`, A-30), so it takes nothing from the field's stream and a change elsewhere never re-keys
it. `pursuit_damage` is the fast pursuer's attack on a routed body (its own draw until MBA-04 step 5). `_momentum_speed`,
`_cell_damage_weights` and `_accum_cell_damage` are the helpers only the pair's block calls: they moved with it so this module imports
nothing from `orchestration` (no cycle). A flag or a value read here is read from THIS module's namespace: a test or an instrument that
flips one (the planted `EXPOSURE_BASE = 0`, MBA §4.2) patches it here."""
from dataclasses import dataclass

from engine.dice_engine import draw as _draw  # the one keyed draw (B06): the contact draw's `z`
from engine.dice_engine import fmath  # the one owner of `sqrt`, `powf` and the left-to-right sum
from engine.dice_engine.dice_engine import degree_label  # the one degree ladder (A-5); the field grades nothing of its own
from modules.mass_battle import rngsource  # single owner of engine randomness (see rngsource.py)
from modules.mass_battle.config import *
from modules.mass_battle.core import contact_table  # the measured felling chances the draw reads (passed in as `table`)
from modules.mass_battle.core.attrition import engaged_files
from modules.mass_battle.core.exchange import _pair_troops
from modules.mass_battle.equipment.armour import TIERS as _ARMOUR_TIERS, dr_vs_piercing
from modules.mass_battle.geometry import _oriented, _oriented_abs_map
from modules.mass_battle.hierarchy.units import COL_WIDTH
from modules.mass_battle.percell import _defender_depth, column_stamina_share
from modules.mass_battle.resolution import (_charge_shock_sigma, _morale_sigma, _subunit_braced, _wall_prep,
                                            roll_pool, trace_event)
from modules.mass_battle.troop_types.registry import charge_for, reach_for
from modules.mass_battle.troop_types.table import loadout_for_names

__all__ = ['ContactVector', 'contact_mu_var', 'contact_casualties', 'contact_vector', 'contact_z', 'fighter', 'fights',
           'commitment', 'resolve_melee_pair', 'pursuit_damage', 'REARGUARD_PENALTY', 'EXPOSURE_BASE',
           '_momentum_speed', '_cell_damage_weights', '_accum_cell_damage']

# ─── the vector's factors (MBA §1.3 step 2, §1.4), read from the exported troop file (`references/troops.yaml: contact`) ───────────
EXPOSURE_BASE_SEED = 0.1   # [seed, B19.12: the troop file's `contact.exposure.base` is null (uncalibrated; MBA-08 sets it by T-1 and
#   T-2). 0.1 rounds a tick is the value at which the reference mirror field reads its pre-B19.12 casualties: the gauge's Line tier-3
#   mirror, friction off, n 60, mean casualties 5.6% against 5.5% on the pool (0.05: 3.0%; 0.2: 10.8%). Well under one round a tick,
#   as MBA §1.4 requires. Read only while the troop file's value is null; MBA-08 writes the calibrated value there and deletes this.]
EXPOSURE_BASE = contact_table.value('contact.exposure.base')         # duel rounds a front man fights a tick in an even, faced contact
if EXPOSURE_BASE is None:
    EXPOSURE_BASE = EXPOSURE_BASE_SEED
POSTURE_K = contact_table.value('contact.exposure.posture_k')        # posture = 1 + POSTURE_K x (cA + cB)
COVER_WALLS = contact_table.value('contact.exposure.cover.walls')    # the defender's cover behind walls (`massbattle._run_and_grade`)
LEVEL_INTENT_OFFENSE = contact_table.value('contact.levels.intent_offense')
LEVEL_INTENT_DEFENSE = contact_table.value('contact.levels.intent_defense')
LEVEL_TERRAIN_DIE = contact_table.value('contact.levels.terrain_die')
LEVEL_CHARGE_CAP = contact_table.value('contact.levels.charge_cap')
LEVEL_MORALE_NEAR_ROUT = contact_table.value('contact.levels.morale_near_rout')
POSTURE_FLOOR = 0.25   # [seed: MBA §1.4 "floored at 0.25" -- the troop file carries no row for it; two holders still trade]
FALLBACK_ARM = 'arming'   # [ASSUMPTION: a body whose troop row names no arm (the unmustered `infantry`) fights with the arming sword,
#                           the duel's reference weapon -- basis: the troop file's `arming` arm; reversible: this name]


def _momentum_speed(atom, contact_abs_cells):
    """F-ii: mean cell_last_speed for contact cells.
    [canonical: Jordan handoff §(2)]"""
    if not contact_abs_cells: return 0.0
    speeds = []
    op = _oriented(atom)
    for abs_r, abs_c in contact_abs_cells:
        for orig_r, orig_c, or_r, or_c in op:
            comp_r = (atom.starting_position[0] + or_r
                      + atom.cell_offsets.get((orig_r, orig_c), 0) * atom.advance_dir)
            comp_c = (atom.starting_position[1] + or_c
                      + atom.cell_offsets_c.get((orig_r, orig_c), 0))
            if MB_NODE_COHESION and hasattr(atom, '_node_pos'):
                _pr, _pc = atom._node_pos.get((orig_r, orig_c), (0.0, 0.0))
                # [migration H] file-bin the column on ON so comp matches the file-binned cells()/contact
                # cells; OFF = verbatim int(round). FIELD_MOVEMENT/COL_WIDTH via units star-import.
                comp_r, comp_c = (int(round(_pr)), int(round(_pc / COL_WIDTH))) if FIELD_MOVEMENT else (int(round(_pr)), int(round(_pc)))
            if (comp_r, comp_c) == (abs_r, abs_c):
                speeds.append(atom.cell_last_speed.get((orig_r, orig_c), 0))
                break
    return sum(speeds) / len(speeds) if speeds else 0.0


def _cell_damage_weights(atom, cell_mods, red):
    """[ED-MB-0040] Per-cell casualty-allocation weights for one defender in one contact pair.
    weight(cell) = troops_in_cell x that cell's OWN facing multiplier (front 1.0 / flank 1.5 / rear 2.0,
    interpolated from its own arc mod exactly as the subunit scalar is). Jordan: "the cell is the
    primitive... each cell has its own octagon facing... its own capacity to receive damage" — so a rear
    cell of a subunit dies ~2x faster than a front-facing sibling in the SAME subunit, and an enveloped
    body is stripped shell-inward. Troops are read live (`cell_troops` via the identity map), so an
    already-hollowed cell stops attracting casualties it no longer has."""
    if not cell_mods:
        return {}
    amap = _oriented_abs_map(atom)
    out = {}
    for abs_cell, m in cell_mods.items():
        orig = amap.get(abs_cell)
        troops = atom.cell_troops.get(orig, 0.0) if orig else 0.0
        if troops <= 0:
            continue
        out[abs_cell] = troops * min(red, 1.0 - m * (red - 1.0) / 2.0)
    return out


def _accum_cell_damage(store, atom, weights, dmg):
    """[ED-MB-0040] Split `dmg` across `weights` (see _cell_damage_weights) into
    store[id(atom)] = (atom, {abs_cell: dmg}). No weights (all cells empty) -> the caller's aggregate
    total still stands and the residual is reconciled by the aggregate spread at apply time."""
    if dmg <= 0 or not weights:
        return
    tot = sum(weights.values())
    if tot <= 0:
        return
    slot = store.get(id(atom))
    if slot is None:
        slot = (atom, {}); store[id(atom)] = slot
    acc = slot[1]
    for cell, w in weights.items():
        acc[cell] = acc.get(cell, 0.0) + dmg * (w / tot)


def fighter(atom):
    """`(arm, armour, skill)` of the men of `atom` as the measured table keys them (MBA §1.1): the duel weapon of the troop row's
    primary arm (`contact_table.duel_arm`: its `duel_key`, or a missile arm's `sidearm`), the row's armour tier, and the men's martial
    skill (`eff_power`, the troop row's `skill` through the loader's alias until MBA-04 step 8) clipped to the table's grid [1, 5].
    A body whose row names no kit (the unmustered `infantry`) fights with `FALLBACK_ARM`, its armour the catalogue tier its own `dr`
    reads on the catalogue's DR scale (`equipment/armour.py::dr_vs_piercing`: none 0, light 1, medium 2, heavy 3).
    [ASSUMPTION: skill outside [1, 5] is clipped, not refused -- basis: the table refuses it, and a field must not raise on a body the
    order of battle allowed; reversible: refuse instead]"""
    arm, armour = loadout_for_names(getattr(atom, 'troop_type', None))
    if armour is None:
        dr = atom.eff_dr
        armour = next((t for t in _ARMOUR_TIERS if dr_vs_piercing(t) >= dr), _ARMOUR_TIERS[-1])
    return contact_table.duel_arm(arm or FALLBACK_ARM), armour, min(max(float(atom.eff_power), 1.0), 5.0)


def fights(unit, atom):
    """True when `atom` has fighting men (MBA-04 step 4: the routed / broken / disordered tests of the retired per-subunit combat pool,
    moved here unchanged): a routed or disordered body, or one of a routed or disordered army, contributes no attacker (`m = 0`).
    A body at Discipline 0 has lost its formation (§A.4 "Formation broken; cannot attack"): it is marked disordered HERE, and its army
    when every one of its units is (ED-1020: a single disordered section does not zero its healthy siblings)."""
    if unit.routed or unit.disordered or atom.routed or atom.disordered:
        return False
    if atom.eff_discipline <= 0:
        atom.disordered = True
        if all(s.disordered for s in unit.units):
            unit.disordered = True
        return False
    return True


def commitment(atom):
    """The body's signed commitment `c` (`STANCE_COMMITMENT` through `eff_stance`, MB-04): aggressive +1, balanced 0, hold and retreat
    -1. A yielding body (`yield_active`, not pocketed) fights in the posture `retreat` (MBA-04 step 4: the retired yield malus). 0 with
    MB_INTENT_RESOLUTION off (the posture and the intent levels are both inert)."""
    if not MB_INTENT_RESOLUTION:
        return 0
    if getattr(atom, 'yield_active', False) and not getattr(atom, 'pocketed', False):
        return STANCE_COMMITMENT['retreat']
    return STANCE_COMMITMENT.get(atom.eff_stance, 0)


def contact_z(bout, t, slot_a, slot_b, side):
    """The standard normal of one side of one contact in one tick (MBA §1.3 step 5): the field's `Draw` key re-mixed with
    `contact|bout|tick|pair|side` (`draw.H2`) and read by `Draw.normal` on its own key. One key per purpose (A-30): it takes nothing
    from the field's stream, so a replay reproduces the tick and no other draw re-keys it. `bout` is the army's `run_battle` count
    (`battle_loop.run_battle` bumps it), `slot_a`/`slot_b` the two bodies' places in their armies, `side` the receiving side."""
    key = _draw.H2(rngsource.get().key, f"contact|{bout}|{t}|{slot_a}|{slot_b}|{side}")
    return _draw.seeded(key).normal(0.0, 1.0)


def contact_vector(atom_d, unit_d, d_cells, d_share, atom_a, unit_a, a_cells, a_front, a_share, fight_a,
                   exposure_d, levels_d):
    """The matchup vector of receiving side `d` of one contact (MBA §1.1; the builder MBA-04 step 2 names, "which state is which
    field"):
      `arm_a`, `armour_d`, `skill_a`, `skill_d`, `arm_d`, `armour_a` -- `fighter` of the two bodies;
      `rounds_d` -- `1 + (K - 1) x (1 - s)`, `s` the column stamina share of d's contact files (`percell.column_stamina_share`, the one
          ledger), `K` the table's last round: a fresh front fights its first round, a spent one its K-th;
      `support_a` -- `(front + support) / front` of the attacker in this contact (`exchange._pair_troops`: its contact cells' men and its
          depth-weighted ranks behind, `support_weight`): 1 for a one-rank front, more where ranks behind reach; 0 for a body with no
          fighting men (`fights`);
      `exposure_d`, `levels_d` -- the caller's (they need both bodies' arcs, postures and the charge read of the pair);
      `frontage` -- the men of the two fronts facing each other, counted on the ATTACKER's front: `engaged_files` of a's contact cells
          (each at `1 / m` of the pairs it is in; on the field path a's own engaged width): each of a's front men fights one duel a
          round against the man before him, so the felled are a's front men times the felling chance. This is the retired owner's own
          direction (`_lanchester_strength` of A's contact set the casualties to B), re-stated as men. [ASSUMPTION: the attacker's front,
          not the smaller of the two -- basis: a body struck obliquely by a front it does not face has a near-zero engaged width of its
          own (the OBB overlap is per side), and the smaller of the two would spare it the blows of the front that faces it; measured
          on the flank row's own field, the defender's losses FELL when a flanker joined. Reversible: this line];
      `men_d` -- d's men in its contact cells at the same shares, the draw's upper clip."""
    arm_a, armour_a, skill_a = fighter(atom_a)
    arm_d, armour_d, skill_d = fighter(atom_d)
    k = contact_table.rounds_k()
    s = column_stamina_share(unit_d, {c for _r, c in d_cells})
    front_a, engaged_a = _pair_troops(atom_a, a_cells)
    support_a = engaged_a / front_a if fight_a and front_a > 0 else 0.0
    men_d = engaged_files(d_cells, atom_d, None, d_share)
    frontage = engaged_files(a_cells, atom_a, a_front, a_share)
    return ContactVector(arm_a=arm_a, armour_d=armour_d, skill_a=skill_a, skill_d=skill_d, rounds_d=1.0 + (k - 1) * (1.0 - s),
                         support_a=support_a, exposure_d=exposure_d, levels_d=tuple(levels_d), frontage=frontage, men_d=men_d,
                         arm_d=arm_d, armour_a=armour_a)


def _morale_level(unit, atom):
    """The body's own morale as a level in skill steps (<= 0): `_morale_sigma`'s graded shape (0 at full morale, the full scale near
    rout) scaled to `contact.levels.morale_near_rout`. It lowers what the body inflicts, as it lowered its offence net."""
    return _morale_sigma(unit, atom) / MORALE_SIGMA_SCALE * LEVEL_MORALE_NEAR_ROUT if MORALE_SIGMA_SCALE else 0.0


def _charge_level(defender, def_cells, zone, atom, t):
    """A charge's moral shock on the struck body as a level in skill steps (<= 0): `_charge_shock_sigma`'s preparedness-gated shape
    scaled to `contact.levels.charge_cap` at its cap (`MB_CHARGE_SIGMA`). It lowers what the shocked body inflicts."""
    sig = _charge_shock_sigma(defender, def_cells, zone, atom, t)
    return sig / MB_CHARGE_SIGMA * LEVEL_CHARGE_CAP if MB_CHARGE_SIGMA else 0.0


def resolve_melee_pair(p, atom_a, atom_b, unit_a, unit_b, a_angle_mod, b_angle_mod, a_fixed_other, b_fixed_other, eng_counts,
                       _atom_sides, _octagon_cell_mods, cell_dmg_a, cell_dmg_b, t=None):
    """One contact pair's melee resolution, by the contact draw (B19.12, MBA-04 step 2): each side's casualties are the other side's
    measured felling chance over its exposure and support, drawn once on its own key, and land on the receiving side's contact cells.
    Returns `(cas_a, cas_b, shocked_a, shocked_b)`: the casualties to A and to B (the caller accumulates them) and the two
    envelopment-shock flags the pair set. `cell_dmg_a`/`cell_dmg_b` are the caller's per-cell accumulators, written in place.
    `_octagon_cell_mods` is the caller's closure (it closes over the tick `t`).

    THE LEVELS (MBA §1.3 step 2), in skill steps, one step a die-equivalent (the tree's conversion: `SIGMA_PER_D` sigma a die, one die
    a point of skill). Each is a term of the retired sigma head, kept in the role and the sign it had there: a term that raised a side's
    offence net is a level on the OTHER side's felling chance (`on_b` collects A's offence terms, `on_a` B's). So the vector of the
    receiving side carries every level of the contact that bears on it -- its own posture against the attacker's, the attacker's
    terrain, morale, momentum and the shock or recoil the attacker suffered -- and there is no `levels_a` (the attacker's terms ARE
    `levels_d`'s; the other side's are the mirror vector's). Intent (`contact.levels.intent_*`), terrain dice (`terrain_die`), charge
    shock (`charge_cap`) and morale (`morale_near_rout`) read the troop file's seeds; the puncture and the recoil, which have no row there,
    keep their die counts (`PUNCTURE_CAP`, `MB_CHARGE_RECOIL`) at one step a die. `RANGED_MELEE_SIGMA` is dropped (a missile troop
    fights with its own sidearm, in the table) and `MB_STAM_SIGMA` is dropped (fatigue is `rounds_d`).

    THE EXPOSURE (MBA §1.4): `EXPOSURE_BASE x posture x arc_d x crowding_d x cover_d`; `posture = 1 + POSTURE_K x (cA + cB)` floored at
    `POSTURE_FLOOR`; `arc_d` the octagon multiplier of d's contact cells (front 1.0, flank 1.5, rear 2.0, the mean arc as the retired
    damage multiplier read it); `crowding_d = 1 + MULTI_SIDE_SHOCK x (sides - 1)` on the faces d is struck on; `cover_d` the army's
    `cover` (walls, `massbattle._run_and_grade`). Under MB_OCTAGON_DMG off the arc is 1 and the legacy angle and encirclement penalties
    are levels (one step a die), as they were dice."""
    shocked_a = shocked_b = False
    on_a, on_b = [], []          # levels in skill steps on A's felling chance (B's offence terms) and on B's (A's offence terms)
    fight_a, fight_b = fights(unit_a, atom_a), fights(unit_b, atom_b)
    if not MB_OCTAGON_DMG:
        # [ED-MB-0018] legacy path: the octagon is an angle penalty on the struck side's own offence (a_angle_mod <= 0 when A
        # flanked) and the encirclement penalty fires on >= 2 pairs; under MB_OCTAGON_DMG both are the arc and the crowding below.
        on_b.append(a_angle_mod)
        on_a.append(b_angle_mod)
        if eng_counts.get(id(atom_a), 0) >= 2: on_b.append(-ENCIRCLEMENT_PENALTY)
        if eng_counts.get(id(atom_b), 0) >= 2: on_a.append(-ENCIRCLEMENT_PENALTY)
    if PUNCTURE_ENABLED:
        a_mom = _momentum_speed(atom_a, p["a_cells"])
        b_mom = _momentum_speed(atom_b, p["b_cells"])
        a_pen = (a_mom - b_mom) if a_mom > b_mom else 0.0
        b_pen = (b_mom - a_mom) if b_mom > a_mom else 0.0
        if PER_CELL:
            # Increment 5: intrinsic charge (cavalry) presses while out-momentuming; the
            # DEFENDER's engaged-column depth absorbs the charge — deep absorbs, thin is punched through.
            if a_pen > 0: a_pen += atom_a.charge_pen
            if b_pen > 0: b_pen += atom_b.charge_pen
            a_pen = max(0.0, a_pen - _defender_depth(unit_b, p["b_cells"]))
            b_pen = max(0.0, b_pen - _defender_depth(unit_a, p["a_cells"]))
        if a_pen > 0: on_b.append(min(PUNCTURE_CAP, int(a_pen)))
        if b_pen > 0: on_a.append(min(PUNCTURE_CAP, int(b_pen)))
        # Phase 3: a landed charge also delivers a DEFENDER moral shock (du Picq), gated by the defender's preparedness
        # (facing/brace/depth/shaken): the charger's PHYSICAL penetration (the puncture above) is distinct from the defender's
        # MORAL collapse, which lowers what the shocked body inflicts. Zone = defender's octagon facing-vs-charger (GREEN 0 /
        # YELLOW -1 / RED -2 via ANGLE_DEF_MOD).
        if PER_CELL:
            if a_pen > 0:
                _zb = "GREEN" if b_angle_mod > -0.5 else ("YELLOW" if b_angle_mod > -1.5 else "RED")  # [canonical: config.py:148 ANGLE_DEF_MOD GREEN 0/YELLOW -1/RED -2; -0.5, -1.5 are the zone-value midpoints re-binning the per-cell-averaged angle_mod to a zone: -0.5=mid(0,-1), -1.5=mid(-1,-2)]
                on_a.append(_charge_level(unit_b, p["b_cells"], _zb, atom_b, t))
            elif MB_ENVELOP_SHOCK and b_fixed_other and b_angle_mod <= -0.5:
                # B (envelopment shock): a subunit FIXED frontally by a separate body and struck on its flank/rear cannot face
                # the new threat. [ED-MB-0075 option (2)] Flag only: a contributing cause of morale collapse, checked against
                # Discipline once per UNIT per TICK in run_battle's loop, not a second combat-effectiveness term.
                # [canonical: Cannae 216 BC; du Picq Battle Studies -- the unfaceable attack on a pinned line.]
                shocked_b = True
            if b_pen > 0:
                _za = "GREEN" if a_angle_mod > -0.5 else ("YELLOW" if a_angle_mod > -1.5 else "RED")  # [canonical: config.py:148 ANGLE_DEF_MOD zone midpoints — see the _zb line above]
                on_b.append(_charge_level(unit_a, p["a_cells"], _za, atom_a, t))
            elif MB_ENVELOP_SHOCK and a_fixed_other and a_angle_mod <= -0.5:
                shocked_a = True   # A (envelopment shock), mirror of the B branch above
            # Reciprocal charge-recoil: a charge driven home into a BRACED + deep + disciplined wall shatters the charger
            # (Courtrai/Swiss/Waterloo squares), scaled by the wall's prep (discipline x depth), gated by the 'brace' INSTRUCTION.
            # [ED-1091] MB_RECOIL_FRONTAL: only the wall's frontal (GREEN) zone recoils. [ED-1095] MB_RECOIL_CHARGER_GATE: the
            # charger must be a charging troop type (`charge_for > 0`) and the wall's reach >= the charger's.
            # [ED-MB-0041 Tier-2] CHARGER-ROLE LATCH: `a_mom > b_mom` identifies the charger on the tick of impact (momentum is an
            # impulse); the role is latched while the pair stays in contact (`_pressing`, cleared by `_expire_charger_latches`),
            # and every other gate is re-tested each tick, so the wall stops repelling the moment it is broken, flanked or out-reached.
            _a_press = getattr(atom_a, '_pressing', None)
            if _a_press is None: _a_press = atom_a._pressing = set()
            _b_press = getattr(atom_b, '_pressing', None)
            if _b_press is None: _b_press = atom_b._pressing = set()
            if a_mom > b_mom: _a_press.add(id(atom_b))
            if b_mom > a_mom: _b_press.add(id(atom_a))
            a_charging = (a_mom > b_mom) or (id(atom_b) in _a_press)
            b_charging = (b_mom > a_mom) or (id(atom_a) in _b_press)
            if MB_BRACE_ENABLED:
                if (a_charging and _subunit_braced(atom_b, t) and (not MB_RECOIL_FRONTAL or b_angle_mod > -0.5)
                        and (not MB_RECOIL_CHARGER_GATE or (charge_for(atom_a.troop_type) > 0
                                                             and reach_for(atom_b.troop_type) >= reach_for(atom_a.troop_type)))):
                    on_b.append(-MB_CHARGE_RECOIL * _wall_prep(unit_b, p["b_cells"], atom_b))
                elif (b_charging and _subunit_braced(atom_a, t) and (not MB_RECOIL_FRONTAL or a_angle_mod > -0.5)
                        and (not MB_RECOIL_CHARGER_GATE or (charge_for(atom_b.troop_type) > 0
                                                             and reach_for(atom_a.troop_type) >= reach_for(atom_b.troop_type)))):
                    on_a.append(-MB_CHARGE_RECOIL * _wall_prep(unit_a, p["a_cells"], atom_a))
    # INTENT [ED-MB-0029]: a body's own commitment raises what it inflicts (cX x intent_offense) and what it suffers (cX x
    # intent_defense: aggressive EXPOSES, holding BLUNTS); with the posture factor below, two holders grind slowly and two aggressors
    # trade fast and bloody. Balanced = 0 -> inert.
    c_a, c_b = commitment(atom_a), commitment(atom_b)
    if c_a or c_b:
        on_b.append(c_a * LEVEL_INTENT_OFFENSE + c_b * LEVEL_INTENT_DEFENSE)
        on_a.append(c_b * LEVEL_INTENT_OFFENSE + c_a * LEVEL_INTENT_DEFENSE)
    # [MB-05] A.9 terrain dice (`Army.terrain_off_d`/`terrain_def_d`, set by `massbattle._run_and_grade`): a side's own offence dice,
    # less the enemy's defence dice. Guarded so an untouched pair adds nothing.
    _ta = unit_a.terrain_off_d - unit_b.terrain_def_d
    _tb = unit_b.terrain_off_d - unit_a.terrain_def_d
    if _ta: on_b.append(_ta * LEVEL_TERRAIN_DIE)
    if _tb: on_a.append(_tb * LEVEL_TERRAIN_DIE)
    _ma, _mb = _morale_level(unit_a, atom_a), _morale_level(unit_b, atom_b)   # graded morale effectiveness (du Picq), per subunit
    if _ma: on_b.append(_ma)
    if _mb: on_a.append(_mb)
    # [ED-MB-0018] The octagon arc of each side's contact cells (`_octagon_cell_mods`, the single owner: 0 front .. -2 rear per cell,
    # reaction-gated) read as exposure: a man struck from the flank cannot keep his distance (MBA §1.4). The subunit scalar is the
    # MEAN of the map (1 - arc x (RED - 1) / 2, capped at RED); under MB_CELL_DAMAGE the same map yields the per-cell allocation weights.
    _red = OCTAGON_DMG_MULT["RED"]
    _a_cw = _b_cw = None
    arc_a = arc_b = crowd_a = crowd_b = 1.0
    if MB_OCTAGON_DMG:
        _a_cm = _octagon_cell_mods(atom_a, list(set(p["a_cells"])), list(set(p["b_cells"])))
        _b_cm = _octagon_cell_mods(atom_b, list(set(p["b_cells"])), list(set(p["a_cells"])))
        a_arc = sum(_a_cm.values()) / len(_a_cm) if _a_cm else 0.0
        b_arc = sum(_b_cm.values()) / len(_b_cm) if _b_cm else 0.0
        arc_a = min(_red, 1.0 - a_arc * (_red - 1.0) / 2.0)
        arc_b = min(_red, 1.0 - b_arc * (_red - 1.0) / 2.0)
        if MB_CELL_DAMAGE:
            _a_cw = _cell_damage_weights(atom_a, _a_cm, _red)
            _b_cw = _cell_damage_weights(atom_b, _b_cm, _red)
        # MULTI-SIDE crowding, GRADED by the number of DISTINCT faces struck (`_atom_sides`): 2 sides x1.5, 3 x2.0, 4 x2.5.
        _na = len(_atom_sides.get(id(atom_a), ()))
        _nb = len(_atom_sides.get(id(atom_b), ()))
        if _na >= 2: crowd_a = 1.0 + MULTI_SIDE_SHOCK * (_na - 1)
        if _nb >= 2: crowd_b = 1.0 + MULTI_SIDE_SHOCK * (_nb - 1)
    posture = max(POSTURE_FLOOR, 1.0 + POSTURE_K * (c_a + c_b))
    exp_a = EXPOSURE_BASE * posture * arc_a * crowd_a * getattr(unit_a, 'cover', 1.0)
    exp_b = EXPOSURE_BASE * posture * arc_b * crowd_b * getattr(unit_b, 'cover', 1.0)
    # [B19.13, MBA-04 step 6] The pair carries each side's exposure on the contact, as a multiple of the base, to the column ledger
    # (`percell.update_stamina` scales the tick's drain by it, MBA §1.4): a man in a hot contact tires faster. At `EXPOSURE_BASE = 0`
    # (the plant) the ratio is 1 `[ASSUMPTION: no division by the planted zero -- the plant empties the draw, not the ledger]`.
    p["stamina_scale_a"] = exp_a / EXPOSURE_BASE if EXPOSURE_BASE else 1.0
    p["stamina_scale_b"] = exp_b / EXPOSURE_BASE if EXPOSURE_BASE else 1.0
    a_share, b_share = p.get("a_share"), p.get("b_share")
    vec_a = contact_vector(atom_a, unit_a, p["a_cells"], a_share, atom_b, unit_b, p["b_cells"], p.get("b_front"), b_share, fight_b,
                           exp_a, on_a)
    vec_b = contact_vector(atom_b, unit_b, p["b_cells"], b_share, atom_a, unit_a, p["a_cells"], p.get("a_front"), a_share, fight_a,
                           exp_b, on_b)
    bout = getattr(unit_a, '_bout', 0)
    slot_a = next(i for i, u in enumerate(unit_a.units) if u is atom_a)
    slot_b = next(i for i, u in enumerate(unit_b.units) if u is atom_b)
    z_a = contact_z(bout, t, slot_a, slot_b, 'A')
    z_b = contact_z(bout, t, slot_a, slot_b, 'B')
    cas_a = contact_casualties(vec_a, contact_table, z_a)
    cas_b = contact_casualties(vec_b, contact_table, z_b)
    if MB_CELL_DAMAGE:
        # [ED-MB-0040] Land THIS pair's casualties on the defender's CONTACT CELLS, split by each cell's own exposure weight
        # (troops x its own facing multiplier) — the cell is the primitive. Unchanged by the draw (MBA §1.3 step 6).
        _accum_cell_damage(cell_dmg_a, atom_a, _a_cw, cas_a)
        _accum_cell_damage(cell_dmg_b, atom_b, _b_cw, cas_b)
    trace_event('melee', exp_a=round(exp_a, 4), exp_b=round(exp_b, 4), z_a=round(z_a, 3), z_b=round(z_b, 3),
                cas_a=round(cas_a, 2), cas_b=round(cas_b, 2))
    return cas_a, cas_b, shocked_a, shocked_b


REARGUARD_PENALTY = 2  # [canonical: §A.12 — "Fast may rearguard at −2D Off"]


def pursuit_damage(pursuer, routing_unit, pool_of):
    """Fast pursuer attacks routing unit. Routing unit has no defence
    unless it is also Fast (rearguard at -2D Off).
    Returns HP damage dealt. `pool_of(army)` is the caller's army pool function: the module holds none of its
    own, so the one multi-unit loop (systems/mass_battle/sim/multi.py) passes its `base_combat_pool`.
    [canonical: designs/provincial/mass_battle_v30.md §A.12]"""
    if pursuer.speed != "Fast":
        return 0  # Only Fast units can pursue
    if pursuer.routed or pursuer.disordered:
        return 0
    if not routing_unit.routed:
        return 0

    # [canonical: params/mass_combat.md PP-233 — Pool = min(Size,Cmd)+Cmd]
    a_pool = pool_of(pursuer)
    a_net = roll_pool(a_pool)
    trace_event('draw', tick=None, side=getattr(pursuer, 'faction', '?'), unit=getattr(pursuer, 'name', '?'), kind='pursuit', band=degree_label(a_net, 1))

    # Fast routing unit may rearguard at -2D Off
    # [canonical: §A.12 — "Fast may rearguard at −2D Off"]
    if routing_unit.speed == "Fast":
        rg_pool = max(1, pool_of(routing_unit) - REARGUARD_PENALTY)
        rg_net = roll_pool(rg_pool)
        # Rearguard acts as partial defence — reduce pursuer net
        a_net = max(0, a_net - max(0, rg_net))

    # No defence roll for Slow/Standard routing units
    # [canonical: §A.12 — "Slow/Standard cannot fight back"]

    # Damage = net successes × (1 + Power), minus DR
    # [canonical: params/mass_combat.md PP-233]
    if a_net <= 0:
        return 0
    raw_dmg = CASUALTY_SCALE * a_net * (1 + pursuer.power)
    dmg = max(0, raw_dmg - routing_unit.dr)
    return dmg


@dataclass(frozen=True)
class ContactVector:
    """The matchup vector: one contact and one receiving side `d` (the other is `a`), per tick (MBA §1.1). Every field belongs to the two bodies
    in contact; there is no side-wide value. `arm_d` and `armour_a` are the defender's arm and the attacker's armour: the table is keyed on
    the whole ordered pair of fighter types and a felling chance marginalised over either is undefined (`contact_table`'s signature).
    `men_d` is the men of the defender in the contact cells, the draw's upper clip (§1.3 step 5). `levels_d` are the named levels in
    skill steps that bear on the defender's felling chance (§1.3 step 2), the attacker's offence terms among them; there is no
    `levels_a` (B19.12: the attacker's levels ARE the defender's, and the other side's are the mirror vector's; `resolve_melee_pair`)."""
    arm_a: str
    armour_d: str
    skill_a: float
    skill_d: float
    rounds_d: float
    support_a: float
    exposure_d: float
    levels_d: tuple
    frontage: float
    men_d: float
    arm_d: str
    armour_a: str


def contact_mu_var(vec, table):
    """`(mu, var)` of the defender's casualties in one tick of one contact (§1.3 steps 1-4): the felling chance `h` read from `table` at
    `(arm_a, armour_d, skill_a, skill_d, rounds_d)`; `logit(h') = logit(h) + beta x sum(levels_d)`; `q = 1 - (1 - h')^(r x m)` with
    `r = exposure_d`, `m = support_a`; `mu = F x q`, `var = F x q x (1 - q)` with `F = frontage`. No second variance layer (A-77)."""
    if vec.frontage < 0 or vec.exposure_d < 0 or vec.support_a < 0:
        raise ValueError(f'frontage, exposure_d and support_a are counts and may not be negative: {vec!r}')
    pair = dict(arm_d=vec.arm_d, armour_a=vec.armour_a)
    h = table.felling_chance(vec.arm_a, vec.armour_d, vec.skill_a, vec.skill_d, vec.rounds_d, **pair)
    slope = table.beta(vec.arm_a, vec.armour_d, vec.skill_a, vec.skill_d, **pair)
    h2 = contact_table.expit(contact_table.logit(h) + slope * fmath.ltr_sum(vec.levels_d))
    q = 1.0 - fmath.powf(1.0 - h2, vec.exposure_d * vec.support_a)
    return vec.frontage * q, vec.frontage * q * (1.0 - q)


def contact_casualties(vec, table, z):
    """The defender's casualties in one tick of one contact: `clip(mu + z x sqrt(var), 0, men_d)` (§1.3 step 5), a continuous count (A-29).
    Pure: no RNG inside; `z` is the standard normal the keyed draw owner hands in (one key per purpose, A-30), and the vector is the only input."""
    mu, var = contact_mu_var(vec, table)
    return min(max(mu + z * fmath.sqrt(var), 0.0), max(vec.men_d, 0.0))
