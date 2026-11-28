"""core/contact_draw.py -- the melee pair's resolution and the pursuit, moved out of `orchestration.py` unchanged (B19.10, ED-1043).

`resolve_melee_pair` is the body `resolve_engagements` ran per contact pair after the pool and the per-cell angle read; the
pair's casualties are `_pair_a`/`_pair_b`, accumulated by the caller. `pursuit_damage` is the fast pursuer's attack on a routed
body. `_momentum_speed`, `_cell_damage_weights` and `_accum_cell_damage` are the helpers only the pair's block calls: they
moved with it so this module imports nothing from `orchestration` (no cycle). `orchestration` re-imports the names its callers use, so
they are unchanged. A flag read here is read from THIS module's namespace: a test that flips one patches it here."""
from engine.dice_engine.dice_engine import degree_label  # the one degree ladder (A-5); the field grades nothing of its own
from engine.dice_engine.sigma_leverage import roll_net_continuous  # the one sampler; the mu-shift is `resolution._net_boost`
from modules.mass_battle import rngsource  # single owner of engine randomness (see rngsource.py)
from modules.mass_battle.config import *
from modules.mass_battle.core.attrition import _lanchester_strength
from modules.mass_battle.geometry import _oriented, _oriented_abs_map
from modules.mass_battle.hierarchy.units import COL_WIDTH
from modules.mass_battle.percell import _defender_depth, _fatigue_sigma
from modules.mass_battle.resolution import (_charge_shock_sigma, _morale_sigma, _net_boost, _subunit_braced, _wall_prep,
                                            roll_pool, trace_event)
from modules.mass_battle.troop_types.registry import charge_for, reach_for

__all__ = ['resolve_melee_pair', 'pursuit_damage', 'REARGUARD_PENALTY', '_momentum_speed', '_cell_damage_weights', '_accum_cell_damage']


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


def resolve_melee_pair(p, atom_a, atom_b, unit_a, unit_b, a_pool, b_pool, a_pool_raw, b_pool_raw, a_dead, b_dead,
                       a_angle_mod, b_angle_mod, a_fixed_other, b_fixed_other, eng_counts, _atom_sides,
                       _octagon_cell_mods, cell_dmg_a, cell_dmg_b, t=None):
    """One contact pair's melee resolution (moved verbatim out of `resolve_engagements`, B19.10, ED-1043): the sigma head
    and the roll, the degree, the octagon's damage multipliers, the pair's casualties and their landing on the contact cells.
    Returns `(_pair_a, _pair_b, shocked_a, shocked_b)`: the casualties to A and to B (the caller accumulates them) and the two
    envelopment-shock flags the pair set. `cell_dmg_a`/`cell_dmg_b` are the caller's per-cell accumulators, written in place.
    `_octagon_cell_mods` is the caller's closure (it closes over the tick `t`)."""
    shocked_a = shocked_b = False

    # === SIGMA-LEVERAGE HEAD (prototype) ===
    # Advantages (octagon angle, puncture, encirclement, ranged-in-melee) enter as a
    # delta-sigma net-boost on the offensive net successes (uniform impact across pool
    # size), NOT as pool modifiers (non-uniform impact). Bare pool above = pure capacity.
    # Spine (degree -> DAMAGE_BY_DEGREE -> casualties) unchanged.
    # [canonical resolution: mass_combat.md §A.4 net-success exchange; sigma math:
    #  params/core.md continuous engine + modifier_system_spec.md §2.1/§3.1]
    ns_a = ns_b = 0.0   # legacy-path default so the mechanical trace can read these uniformly
    if SIGMA_HEAD_ENABLED:
        # [ED-MB-0018] Under MB_OCTAGON_DMG the octagon is a DAMAGE-RECEIVED MULTIPLIER (applied to
        # dmg_a/dmg_b below), NOT a net-successes penalty -- so it is REMOVED from the sigma head here
        # to avoid double-counting. The zone is still read for charge-shock / brace gating below.
        ns_a = 0.0 if MB_OCTAGON_DMG else a_angle_mod * SIGMA_PER_D     # a_angle_mod<=0 when A flanked
        ns_b = 0.0 if MB_OCTAGON_DMG else b_angle_mod * SIGMA_PER_D
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
            if a_pen > 0: ns_a += min(PUNCTURE_CAP, int(a_pen)) * SIGMA_PER_D
            if b_pen > 0: ns_b += min(PUNCTURE_CAP, int(b_pen)) * SIGMA_PER_D
            # Phase 3: a landed charge also delivers a DEFENDER moral shock (du Picq), gated by the
            # defender's preparedness (facing/brace/depth/shaken). Charger A out-momentums B -> B is
            # shocked (applied to B's offence); and vice versa. Distinct from puncture: puncture is the
            # charger's PHYSICAL penetration (depth-absorbed, boosts charger); shock is the defender's
            # MORAL collapse (discipline/stance/facing-gated, lowers defender). Zone = defender's octagon
            # facing-vs-charger (b_angle_mod for B: GREEN 0 / YELLOW -1 / RED -2 via ANGLE_DEF_MOD).
            if PER_CELL:
                if a_pen > 0:
                    _zb = "GREEN" if b_angle_mod > -0.5 else ("YELLOW" if b_angle_mod > -1.5 else "RED")  # [canonical: config.py:148 ANGLE_DEF_MOD GREEN 0/YELLOW -1/RED -2; -0.5, -1.5 are the zone-value midpoints re-binning the per-cell-averaged angle_mod to a zone: -0.5=mid(0,-1), -1.5=mid(-1,-2)]
                    ns_b += _charge_shock_sigma(unit_b, p["b_cells"], _zb, atom_b, t)
                elif MB_ENVELOP_SHOCK and b_fixed_other and b_angle_mod <= -0.5:
                    # B (envelopment shock): a subunit FIXED frontally by a separate body and struck on
                    # its flank/rear cannot face the new threat -- the du Picq moral shock of envelopment
                    # fires even WITHOUT a momentum charge (the charge path's gap). elif -> mutually
                    # exclusive with the charge path (no double-count); b_fixed_other -> provably inert
                    # single-subunit. [canonical: Cannae 216 BC; du Picq Battle Studies -- the
                    # unfaceable attack on a pinned line.]
                    # [ED-MB-0075 option (2)] Flag only, here: the rear/flank damage is a CONTRIBUTING CAUSE of morale
                    # collapse, checked against Discipline (ED-MB-0067 Part C, C2/C3), not a second combat-effectiveness
                    # penalty. The roll-gated erosion (discipline_check_cascade against dmg / (agg_discipline x command),
                    # the same formula the multi-unit loop's freed_attacker path uses) applies once per UNIT per TICK in
                    # run_battle's per-tick loop, after damage commits.
                    shocked_b = True
                if b_pen > 0:
                    _za = "GREEN" if a_angle_mod > -0.5 else ("YELLOW" if a_angle_mod > -1.5 else "RED")  # [canonical: config.py:148 ANGLE_DEF_MOD zone midpoints — see the _zb line above]
                    ns_a += _charge_shock_sigma(unit_a, p["a_cells"], _za, atom_a, t)
                elif MB_ENVELOP_SHOCK and a_fixed_other and a_angle_mod <= -0.5:
                    # A (envelopment shock), mirror of the B branch above — see its comment for the
                    # [ED-MB-0075 option (2)] rationale: flag only, no pre-combat net-successes penalty.
                    shocked_a = True
                # Reciprocal charge-recoil (the missing historical term): a charge driven home into a
                # BRACED + deep + disciplined wall shatters the charger (Courtrai/Swiss/Waterloo squares).
                # Charger = higher-momentum side; recoil scales with the wall's prep (discipline x depth).
                # Gated by the 'brace' INSTRUCTION -> instruction-less scenarios stay byte-exact. Emergent:
                # pikes break a cavalry charge, a loose/shallow line is still ridden down.
                # [ED-1091, Jordan-approved 2026-07-02] MB_RECOIL_FRONTAL zone-gates the recoil to the
                # wall's frontal (GREEN) octagon zone -- a brace cannot repel what it cannot face
                # (Burkholder 2007), so a flank/rear charge into a braced wall is not recoiled. Zone read: the defender's
                # per-cell-averaged angle_mod, same GREEN midpoint re-binning as the charge-shock above.
                # [canonical: config.py:148 ANGLE_DEF_MOD GREEN 0/YELLOW -1/RED -2; -0.5=mid(0,-1)]
                # [ED-1095, Jordan-ruled 2026-07-02] MB_RECOIL_CHARGER_GATE additionally requires the
                # CHARGING atom to actually be cavalry (mounted_archers -- who should never be closing
                # at all, see T4 -- explicitly excluded) AND the defender's reach >= the charger's reach
                # (a longer-reaching charger, e.g. a lance, can strike a wall whose weapons can't reach
                # reach_for is live: reach_for('infantry')=0.1 < reach_for('cavalry')=0.2, so a braced GENERIC-INFANTRY wall
                # fails `reach_for(defender) >= reach_for(charger)` and MB_CHARGE_RECOIL never fires; a brace IS a hedge of
                # set poles, so a braced defender should carry a pole-armed troop type (pike 0.3 >= 0.2 passes).
                # [ED-MB-0041 Tier-2] CHARGER-ROLE LATCH. `a_mom > b_mom` is how the engine identifies WHO is the charger;
                # it is not itself the cause of the recoil. The cause is a mounted body being pressed onto a hedge of set
                # poles, and a wall does not stop repelling after one tick. Momentum is an impulse (units.py: a halted cell
                # records 0), so the differential is true only on the tick of impact.
                #
                # So the ROLE is latched at impact and held while the pair stays in contact: the atom
                # remembers which opponents it charged. Everything else about the gate is unchanged —
                # brace, frontal zone, cavalry-only and the reach test all still have to pass every tick,
                # so the wall stops repelling the moment it is broken, flanked or out-reached. Cleared
                # when the pair leaves contact (below) and at the battle boundary.
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
                        ns_a -= MB_CHARGE_RECOIL * _wall_prep(unit_b, p["b_cells"], atom_b) * SIGMA_PER_D
                    elif (b_charging and _subunit_braced(atom_a, t) and (not MB_RECOIL_FRONTAL or a_angle_mod > -0.5)
                            and (not MB_RECOIL_CHARGER_GATE or (charge_for(atom_b.troop_type) > 0
                                                                 and reach_for(atom_a.troop_type) >= reach_for(atom_b.troop_type)))):
                        ns_b -= MB_CHARGE_RECOIL * _wall_prep(unit_a, p["a_cells"], atom_a) * SIGMA_PER_D
        # [ED-MB-0018] The legacy ENCIRCLEMENT_PENALTY fires on the SAME >=2 trigger as the multi-side damage
        # shock, so under the octagon flag it is gated off: the octagon multi-side shock is the single owner of
        # the multi-engagement effect.
        if not MB_OCTAGON_DMG:
            if eng_counts.get(id(atom_a), 0) >= 2: ns_a -= ENCIRCLEMENT_PENALTY * SIGMA_PER_D
            if eng_counts.get(id(atom_b), 0) >= 2: ns_b -= ENCIRCLEMENT_PENALTY * SIGMA_PER_D
        if atom_a.unit_type == 'ranged': ns_a += RANGED_MELEE_SIGMA
        if atom_b.unit_type == 'ranged': ns_b += RANGED_MELEE_SIGMA
        ns_a += _morale_sigma(unit_a, atom_a)    # graded morale effectiveness (du Picq): per-subunit morale
        ns_b += _morale_sigma(unit_b, atom_b)
        if PER_CELL:    # Increment 3: fatigue of the engaged front (depth-damped) as delta-sigma
            ns_a += _fatigue_sigma(unit_a, set(c for r, c in p["a_cells"]))
            ns_b += _fatigue_sigma(unit_b, set(c for r, c in p["b_cells"]))
        # Overhang/flank pressure is delivered by the octagon flank multiplier + graded multi-side shock (B6) +
        # the perimeter/orbital-wheel envelopment (ED-MB-0035); there is no separate envelopment sigma term.
        if MB_INTENT_RESOLUTION:
            # [ED-MB-0029] INTENT as an offence/defence commitment (mass_battle_v30 §A Offensive/
            # Defensive axis). A subunit's own commitment cX (aggressive +1 / balanced 0 / hold,
            # retreat -1) shifts its OWN offence (cX·INTENT_OFFENSE_D) and the ENEMY's offence against
            # it (cX·INTENT_DEFENSE_D — aggressive EXPOSES, defensive BLUNTS). So A's offence net rises
            # with A's aggression and with B's exposure, and falls when B holds: ns_a gains
            # (cA·OFF + cB·DEF). Symmetric for B. A holding pin (cA=-1) vs a pressing foe (cB=+1) nets
            # ~even at OFF≈DEF — the pin is NOT crushed, it survives to buy time (Cannae centre); two
            # holders grind slowly; two aggressors trade fast and bloody. Delta-sigma (uniform-impact),
            # like every other advantage above — NOT a raw damage multiplier. Gated; balanced=0 -> inert.
            cA = STANCE_COMMITMENT.get(atom_a.eff_stance, 0)   # [MB-04] role keyword reads through eff_stance
            cB = STANCE_COMMITMENT.get(atom_b.eff_stance, 0)
            ns_a += (cA * INTENT_OFFENSE_D + cB * INTENT_DEFENSE_D) * SIGMA_PER_D
            ns_b += (cB * INTENT_OFFENSE_D + cA * INTENT_DEFENSE_D) * SIGMA_PER_D
        # [MB-05] A.9 terrain dice (`Army.terrain_off_d`/`terrain_def_d`, set by
        # `massbattle._run_and_grade`): a side's own offence dice, less the enemy's defence dice --
        # the same Off/Def reading as the INTENT term above. Guarded so an untouched pair adds nothing.
        _ta = unit_a.terrain_off_d - unit_b.terrain_def_d
        _tb = unit_b.terrain_off_d - unit_a.terrain_def_d
        if _ta: ns_a += _ta * SIGMA_PER_D
        if _tb: ns_b += _tb * SIGMA_PER_D
        if MB_FRACTIONAL_POOL:
            # [ED-MB-0032] roll the CONTINUOUS pool without flooring: the one sampler takes the pool as it is, and the
            # one boost reads the same pool (a dead atom's net is forced to 0 below regardless, same as the integer path).
            _apr = a_pool_raw if not a_dead else 0.0
            _bpr = b_pool_raw if not b_dead else 0.0
            a_net = roll_net_continuous(_apr, rng=rngsource.get()) + _net_boost(ns_a, _apr)
            b_net = roll_net_continuous(_bpr, rng=rngsource.get()) + _net_boost(ns_b, _bpr)
        else:
            a_net = roll_pool(a_pool) + _net_boost(ns_a, a_pool)
            b_net = roll_pool(b_pool) + _net_boost(ns_b, b_pool)
    else:
        # === LEGACY POOL-MODIFIER PATH (baseline; advantages modify the pool) ===
        # [ED-MB-0018] octagon = damage multiplier under MB_OCTAGON_DMG -> not a pool penalty here
        a_pool = max(1, a_pool + (0 if MB_OCTAGON_DMG else round(a_angle_mod)))
        b_pool = max(1, b_pool + (0 if MB_OCTAGON_DMG else round(b_angle_mod)))
        if PUNCTURE_ENABLED:
            a_mom = _momentum_speed(atom_a, p["a_cells"])
            b_mom = _momentum_speed(atom_b, p["b_cells"])
            if a_mom > b_mom:   a_pool += min(PUNCTURE_CAP, int(a_mom - b_mom))
            elif b_mom > a_mom: b_pool += min(PUNCTURE_CAP, int(b_mom - a_mom))
        if not MB_OCTAGON_DMG:   # [ED-MB-0018] see the sigma-head gate above — no double-count
            if eng_counts.get(id(atom_a), 0) >= 2: a_pool = max(1, a_pool - ENCIRCLEMENT_PENALTY)
            if eng_counts.get(id(atom_b), 0) >= 2: b_pool = max(1, b_pool - ENCIRCLEMENT_PENALTY)
        if atom_a.unit_type == 'ranged': a_pool = max(1, a_pool // 3)
        if atom_b.unit_type == 'ranged': b_pool = max(1, b_pool // 3)
        # [MB-05] A.9 terrain dice, whole dice on the pool (this path's currency) -- see the sigma head.
        _ta = round(unit_a.terrain_off_d - unit_b.terrain_def_d)
        _tb = round(unit_b.terrain_off_d - unit_a.terrain_def_d)
        if _ta: a_pool = max(1, a_pool + _ta)
        if _tb: b_pool = max(1, b_pool + _tb)
        a_net = roll_pool(a_pool)
        b_net = roll_pool(b_pool)
    # `roll_pool` (the whole-die path) floors its own pool argument to a minimum of 1
    # internally, so zeroing `a_pool`/`b_pool` above (for a routed/broken atom) has NO effect on `a_net`/
    # `b_net`. Force the net directly here: a dead atom always resolves to the owner's `net<=0` ->
    # "Failure" -> `DAMAGE_BY_DEGREE["Failure"]` = 0 damage.
    if a_dead: a_net = 0
    if b_dead: b_net = 0
    a_deg = degree_label(a_net, max(1, b_net))
    b_deg = degree_label(b_net, max(1, a_net))
    # [ED-MB-0018] Octagon = DAMAGE-RECEIVED MULTIPLIER (Jordan): the arc the attacker strikes from
    # multiplies the DEFENDER's casualties -- front 1.0x, flank 1.5x, rear 2.0x -- interpolated from the
    # dedicated per-cell FACING-ARC (`_octagon_cell_mods`, 0..-2 -> mult = 1 - arc*(RED-1)/2, capped at
    # RED). This is the pure octagon arc (local-centroid, reaction-gated), NOT the legacy
    # `a_angle_mod`/`b_angle_mod` bundle (which also carries wrapper/pocket/roll-up pool penalties and
    # spuriously reads a wide line's wings as flanked head-on). Under MB_OCTAGON_DMG the legacy pool
    # angle-penalty is zeroed above, so this multiplier + MULTI-SIDE SHOCK are the single envelopment
    # model. MULTI-SIDE SHOCK: a subunit engaged from >=2 sides has its rank-relief divided AND
    # shock-compromised -> an extra COMPOUNDING factor (1+MULTI_SIDE_SHOCK), not a mere halving.
    # `a_arc`/`b_arc` are each side's own exposure, scaling that side's incoming damage (dmg_a = A's).
    _red = OCTAGON_DMG_MULT["RED"]
    _a_cw = _b_cw = None
    if MB_OCTAGON_DMG:
        # [ED-MB-0040] One evaluation of the per-cell arcs; the subunit scalar is their MEAN
        # (the retired `_octagon_dmg_mod` scalar, byte-exact), and under MB_CELL_DAMAGE the SAME map also
        # yields the per-cell allocation weights. The pair TOTAL is unchanged either way; the flag only
        # changes WHERE those casualties land (see _cell_damage_weights).
        _a_cm = _octagon_cell_mods(atom_a, list(set(p["a_cells"])), list(set(p["b_cells"])))
        _b_cm = _octagon_cell_mods(atom_b, list(set(p["b_cells"])), list(set(p["a_cells"])))
        a_arc = sum(_a_cm.values()) / len(_a_cm) if _a_cm else 0.0
        b_arc = sum(_b_cm.values()) / len(_b_cm) if _b_cm else 0.0
        _a_dmg_mult = min(_red, 1.0 - a_arc * (_red - 1.0) / 2.0)
        _b_dmg_mult = min(_red, 1.0 - b_arc * (_red - 1.0) / 2.0)
        if MB_CELL_DAMAGE:
            _a_cw = _cell_damage_weights(atom_a, _a_cm, _red)
            _b_cw = _cell_damage_weights(atom_b, _b_cm, _red)
        # MULTI-SIDE SHOCK, GRADED by the number of DISTINCT sides struck (`_atom_sides` above): the
        # rotate-in/out relief system is progressively more compromised the more directions a body is
        # engaged from -- 2 sides -> x1.5, 3 -> x2.0, 4 -> x2.5. Compounds on the arc AFTER the cap, so a rear pair on a 2-sided
        # body reaches ~3.0x -- the annihilation-by-encirclement regime (du Picq / Cannae).
        _na = len(_atom_sides.get(id(atom_a), ()))
        _nb = len(_atom_sides.get(id(atom_b), ()))
        if _na >= 2: _a_dmg_mult *= (1.0 + MULTI_SIDE_SHOCK * (_na - 1))
        if _nb >= 2: _b_dmg_mult *= (1.0 + MULTI_SIDE_SHOCK * (_nb - 1))
    else:
        _a_dmg_mult = _b_dmg_mult = 1   # int 1 (not 1.0): `X * 1` preserves X's exact type -> the
        #                                 legacy MB_OCTAGON_DMG=0 path stays byte-exact (a float 1.0
        #                                 would coerce integer casualties to float and move the digest)
    if LANCHESTER_ENABLED:
        # P-L Linear Law: casualties to X scale with the ENEMY's engaged strength in
        # contact (frontage-capped); DAMAGE_BY_DEGREE retained as per-soldier exchange
        # quality. Numbers-in-contact lives ONLY here under Lanchester (the run_battle
        # opp_frac post-scaler is skipped) — one variable, one role (role-conflation, Phase 3d).
        # [v2 Stage D, ED-MB-0013] Pass the continuous engaged frontage width (OBB front-overlap)
        # when the FIELD_MOVEMENT contact path recorded it; p.get(...) is None on the grid/OFF path
        # (whose pairs carry no *_front key) -> _lanchester_strength falls back to the legacy integer
        # column count, keeping the byte-exact grid oracle untouched (I4).
        lin_b = _lanchester_strength(p["b_cells"], unit_b, p.get("b_front"))   # B's contacting strength -> casualties to A
        lin_a = _lanchester_strength(p["a_cells"], unit_a, p.get("a_front"))   # A's contacting strength -> casualties to B
        _pair_a = K_LINEAR * lin_b * max(0, DAMAGE_BY_DEGREE[b_deg](atom_b.eff_power) - atom_a.eff_dr) * _a_dmg_mult
        _pair_b = K_LINEAR * lin_a * max(0, DAMAGE_BY_DEGREE[a_deg](atom_a.eff_power) - atom_b.eff_dr) * _b_dmg_mult
    else:
        _pair_a = CASUALTY_SCALE * max(0, DAMAGE_BY_DEGREE[b_deg](atom_b.eff_power) - atom_a.eff_dr) * _a_dmg_mult
        _pair_b = CASUALTY_SCALE * max(0, DAMAGE_BY_DEGREE[a_deg](atom_a.eff_power) - atom_b.eff_dr) * _b_dmg_mult
    if MB_CELL_DAMAGE:
        # [ED-MB-0040] Land THIS pair's casualties on the defender's CONTACT CELLS, split by each cell's
        # own exposure weight (troops x its own facing multiplier) — the cell is the primitive. Totals are
        # identical to the aggregate path; only the placement differs.
        _accum_cell_damage(cell_dmg_a, atom_a, _a_cw, _pair_a)
        _accum_cell_damage(cell_dmg_b, atom_b, _b_cw, _pair_b)
    trace_event('melee', a_pool=a_pool, b_pool=b_pool,
                ns_a=round(ns_a, 3), ns_b=round(ns_b, 3),
                a_net=round(a_net, 2), b_net=round(b_net, 2),
                a_deg=a_deg, b_deg=b_deg)
    return _pair_a, _pair_b, shocked_a, shocked_b


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
