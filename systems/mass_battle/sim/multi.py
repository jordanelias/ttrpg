"""systems/mass_battle/sim/multi.py: the two multi-battle loops and what only they call (workbench code).

The season reaches one battle path, `massbattle.resolve_field`. These loops chain several engagements
(`run_multi_turn_battle`, `run_multi_unit_battle`) and are entered only by the harnesses beside this file
(`engine.py::resolve_battle`, `bat.py`, `validators.py`, `workbench/trace.py`) and by tests. They import the
module; the module does not import them. Every game constant is read from `orchestration`'s namespace at call
time (`_orch.NAME`), as these functions read it when they lived there, so a test that sets one there still
moves them.

Not moved: `pursuit_damage`, `recall_check`, `feigned_retreat_recognized`, `feigned_retreat_check` and
`resolve_feigned_retreat` stay in `orchestration.py`, where the rout-exit and manoeuvre-order work edits them.
`pursuit_damage` takes the pool function as an argument, so the module needs no import from this file:
`run_multi_unit_battle` passes `base_combat_pool` below.
"""
import math

import modules.mass_battle.hierarchy.units as _hu
import modules.mass_battle.orchestration as _orch


def between_turn_recovery(unit):
    """Apply between-turn state changes. Called after each engagement turn.
    [canonical: params/mass_combat.md §PP-712 — discipline persists]"""
    if unit.routed or unit.disordered:
        return
    for atom in unit.units:
        atom.recover_stamina(_orch.BETWEEN_TURN_STAMINA_RECOVERY)
        # [A6, ED-MB-0067 Part A] Resupply at the between-turn lull. Per-subunit (Unit.resupply_volleys,
        # capped at MB_VOLLEYS_START), same loop as stamina immediately above and the SAME reasoning: not singled
        # out by troop type (a melee atom's volleys count is simply never read -- see fire()'s own
        # unit_type=='ranged' gate).
        if _orch.MB_AMMO_ENABLED:
            atom.resupply_volleys(_orch.MB_VOLLEYS_RESUPPLY)
    # [ED-MB-0042 sweep] Deliberately a BARE write, not unit.set_morale. Recovery is a bounded INCREMENT,
    # not an absolute statement about the body — and once cells own the state this pool is STALE (erosion
    # goes to the cells and never updates it), so broadcasting it downward would RE-INFLATE damaged cells
    # to the pool's old value. The pool is kept current here for the unseeded path, which still reads it.
    unit.morale = min(unit.morale_start, unit.morale + _orch.BETWEEN_TURN_MORALE_RECOVERY)
    for atom in unit.units:        # per-subunit Morale recovery (own-Morale units; inert at RECOVERY=0)
        # [ED-MB-0058, resolving ED-MB-0046] ONE owner, both ownership kinds: `pull_morale`, the RELATIVE
        # owner. Recovery is a bounded INCREMENT, so it must not go through `set_morale` (the ABSOLUTE writer,
        # which sets EVERY cell to one value and would flatten per-cell morale divergence to the mean at every
        # turn boundary). `pull_morale` caps against `eff_morale_start`, derives ONE shift from the aggregate
        # and applies that same shift to every cell, so the body recovers by the right amount and the divergence
        # between its cells survives. Unseeded it reduces to `min(eff_morale_start, eff_morale + R)` written to
        # the scalar.
        #
        # The `or atom.cell_morale` keeps an inheriting-but-cellular body in scope; a body that is NEITHER stays
        # out of it — the unit-pool line above is that body's recovery, and calling `pull_morale` for it would
        # write the unit pool once per subunit and compound the increment.
        if atom.morale is not None or atom.cell_morale:
            atom.pull_morale(_orch.BETWEEN_TURN_MORALE_RECOVERY)
    # [ED-MB-0024, DG-2 §2.4 RALLY exit] The between-turn boundary IS the lull (units have disengaged for
    # the turn break -> no active engaged pair). A yielding subunit whose morale has recovered above
    # YIELD_RALLY_MORALE_FRAC of its start reverts to normal combat/stance ("gave ground, pressure
    # relieved, reformed"). Gated OFF -> inert. `pocketed` is cleared alongside (fresh next engagement).
    if _orch.MB_YIELD_RALLY:
        for atom in unit.units:
            if atom.yielding and not atom.routed and not atom.disordered:
                if atom.eff_morale >= _orch.YIELD_RALLY_MORALE_FRAC * atom.eff_morale_start:
                    atom.yielding = False
                    atom.pocketed = False


def reset_morale_between_battles(unit):
    """Campaign-boundary reset: Morale resets between battles; the unit reforms.
    [canonical: designs/provincial/mass_battle_v30.md §A.4; params/mass_combat.md §PP-711 (Morale resets between battles), §PP-712 (Discipline persists between battles)]
    Resets the unit's Morale and each own-Morale subunit's Morale to its nominal start, and clears the
    routed/broken flags -- rout is DERIVED from Morale reaching zero, so resetting Morale without clearing
    the flags would leave an incoherent routed-but-full-Morale unit (derive_rout only ever SETS the flag).
    Discipline is NOT reset (it persists per the citation above). Inherited-Morale units (own Morale is
    None) are covered by the unit-level reset via eff_morale. Called by the campaign layer at the battle
    boundary -- NOT within a single battle: between_turn_recovery handles the within-battle turn boundary,
    this handles the battle-to-battle boundary. A single-subunit unit reduces to the unit-level reset."""
    unit.set_morale(unit.morale_start)   # [ED-MB-0042 sweep] reaches inheriting units' cells
    unit.routed = False
    unit.disordered = False
    # ED-MB-0022: Feigned Retreat is a per-battle tactic; clear its transient flags at the battle
    # boundary so a feint/overextension does not leak into the next battle (inert when the toggle is OFF).
    unit.feigned = False
    unit.overextended = False
    # [A4, ED-MB-0067 Part A] Go-codes are a per-BATTLE tactic too, same reasoning as feigned/overextended
    # immediately above: a signal fired in one battle must not release every order watching for that name
    # on tick 1 of the next.
    unit.fired_signals = set()
    for atom in unit.units:
        if atom.morale is not None:
            atom.set_morale(atom.eff_morale_start)  # own Morale -> nominal start [ED-MB-0042 sweep: via set_morale so the cells reset too]
        atom.routed = False
        atom.disordered = False
        # Clear the cached stochastic-rout break-point (ED-MB-0031) and re-base the casualty denominator to this
        # battle's starting strength: a rout is a per-BATTLE will-to-fight collapse, and a subunit that ended the
        # prior battle past its drawn break-point would otherwise auto-rout on phase 1 of every later battle.
        # (Only consumed under MB_STOCHASTIC_ROUT; between-battle only -> single-battle goldens inert.)
        atom._rout_breakpoint = None
        atom._start_troops = atom.cur_troops
        # [ED-MB-0024, DG-2] pocketed is a live per-tick yield signal — clear it at the battle boundary
        # (a fresh battle re-derives it during the yield movement pass; inert when MB_YIELD_POCKET is off).
        atom.pocketed = False
        # [ED-MB-0041 Tier-2] `yielding` is the other half of the DG-2 yield signal: a per-battle transient,
        # cleared at the same boundary as pocketed/feigned/overextended (with MB_YIELD_RALLY off nothing else
        # clears it, and it would carry its yield-state pool malus into every later battle).
        atom.yielding = False
        # [ED-MB-0041 Tier-2] The charger-role latch is per-engagement state: a body that charged a wall
        # in the last battle must not open the next one already flagged as its charger.
        _p = getattr(atom, '_pressing', None)
        if _p is not None: _p.clear()
        # [ED-MB-0018] A new battle is a fresh engagement -> clear the facing-reaction clock (per-engagement
        # transient state must not survive the battle boundary onto a persistent atom).
        _rs = getattr(atom, '_react_since', None)
        if _rs is not None:
            _rs.clear()


def reset_positions(unit, shape, anchor_map):
    """Reset subunit positions for re-engagement after disengagement -- LEGACY GRID PATH ONLY.
    Units return to their starting rows for fresh approach.

    Each subunit returns to its OWN spawn column (Unit._spawn_position, snapshotted once at
    construction), not a single shape-keyed anchor shared by every subunit in the unit: a shared anchor
    would collapse any wide-placed wing/escort of a multi-subunit army (build_army/build_envelopment/
    build_refused_flank) back onto the center. `shape`/`anchor_map` are used only as a defensive fallback
    for a subunit that lacks a spawn snapshot.

    Node-path atoms are SKIPPED: this function writes only the legacy grid fields (starting_position/
    cell_offsets/cell_offsets_c), which _node_cells()/cells() never read once MB_NODE_COHESION is on (node
    position lives in _node_pos). Per Jordan's ruling (2026-07-02, verbatim): "an army only has subunits
    reset to initial positions... at the start of a new battle. it is nonsensical for them to return to
    starting positions within the same battle" -- within a battle the node path does nothing to position
    at all."""
    start_row = _orch.SIDE_A_START_ROW if unit.faction == 'A' else _orch.SIDE_B_START_ROW
    fallback_col = anchor_map.get((shape, unit.units[0].tier), 10) if unit.units else 10
    for atom in unit.units:
        if _orch.MB_NODE_COHESION and hasattr(atom, '_node_pos'):
            continue
        spawn = getattr(atom, '_spawn_position', None)
        anchor_col = spawn[1] if spawn is not None else fallback_col
        atom.starting_position = (start_row, anchor_col)
        atom.cell_offsets = {}
        atom.cell_offsets_c = {}
        # [ED-MB-0018] A GRID re-approach is a FRESH engagement -> clear the per-cell
        # facing-reaction clock so a stamp from the prior turn cannot mis-score the opening ticks. (Field/
        # node atoms hit the `continue` above -> their continuous engagement correctly keeps the clock.)
        _rs = getattr(atom, '_react_since', None)
        if _rs is not None:
            _rs.clear()


def run_multi_turn_battle(unit_a, unit_b, shape_a, shape_b, anchor_map,
                          max_battle_turns=8):  # [canonical: mass_battle_v30.md §A.7 — battle-turn cap]
    """Run a multi-turn battle. Each turn = 3 phases of engagement.
    Returns list of per-turn result dicts + final outcome.
    [canonical: Jordan direction — 5-8 turns per battle, 3 phases per turn]"""
    log = []
    for battle_turn in range(1, max_battle_turns + 1):
        hp_a_before = unit_a.hp
        hp_b_before = unit_b.hp

        # Reset positions for re-engagement
        reset_positions(unit_a, shape_a, anchor_map)
        reset_positions(unit_b, shape_b, anchor_map)

        # Run one engagement turn (3 phases max)
        # Simultaneous resolution makes run_battle symmetric regardless of argument order.
        r = _orch.run_battle(unit_a, unit_b)

        a_loss_turn = (hp_a_before - unit_a.hp) / unit_a.hp_max if unit_a.hp_max else 0
        b_loss_turn = (hp_b_before - unit_b.hp) / unit_b.hp_max if unit_b.hp_max else 0
        a_loss_cum = 1.0 - (unit_a.hp / unit_a.hp_max) if unit_a.hp_max else 1.0
        b_loss_cum = 1.0 - (unit_b.hp / unit_b.hp_max) if unit_b.hp_max else 1.0

        log.append({
            'turn': battle_turn,
            'a_loss_turn': a_loss_turn, 'b_loss_turn': b_loss_turn,
            'a_loss_cum': a_loss_cum, 'b_loss_cum': b_loss_cum,
            'a_pool': base_combat_pool(unit_a), 'b_pool': base_combat_pool(unit_b),
            'a_eff_size': unit_a.effective_size, 'b_eff_size': unit_b.effective_size,
            'a_morale': unit_a.morale, 'b_morale': unit_b.morale,
            'a_stamina': unit_a.agg_stamina(), 'b_stamina': unit_b.agg_stamina(),
            'a_routed': unit_a.routed, 'b_routed': unit_b.routed,
            'ticks': r['turns'], 'phases': r['phases'],
        })

        if unit_a.routed or unit_b.routed:
            break

        # Between-turn recovery
        between_turn_recovery(unit_a)
        between_turn_recovery(unit_b)

    # Determine winner
    if unit_a.routed and not unit_b.routed:
        winner = 'B'
    elif unit_b.routed and not unit_a.routed:
        winner = 'A'
    else:
        winner = 'draw'

    return {
        'winner': winner,
        'battle_turns': len(log),
        'log': log,
        'a_loss_final': 1.0 - (unit_a.hp / unit_a.hp_max) if unit_a.hp_max else 1.0,
        'b_loss_final': 1.0 - (unit_b.hp / unit_b.hp_max) if unit_b.hp_max else 1.0,
    }


def unit_in_reserve(unit):
    """True if the unit is held in Reserve (any subunit carries the 'reserve' instruction).
    [canonical: mass_battle_v30.md §A.6 — Reserve formation: 'cannot engage; commits Phase 3 next turn']"""
    return any('reserve' in getattr(a, 'instructions', ()) for a in unit.units)


def freed_attacker_damage(freed_unit, target_unit):
    """Freed unit attacks target from the flank.
    The freed unit rolls its full pool. Target defends at -1D (flank).
    Returns damage dealt to target.
    [canonical: designs/provincial/mass_battle_v30.md §A.12 — implied by
     rout freeing the victor to attack adjacent enemies]"""
    if freed_unit.routed or freed_unit.disordered:
        return 0
    if target_unit.routed or target_unit.disordered:
        return 0
    # [canonical: params/mass_combat.md PP-233 — Pool = min(Size,Cmd)+Cmd]
    a_pool = base_combat_pool(freed_unit)
    # [canonical: designs/provincial/mass_battle_v30.md §A.4 — YELLOW zone -1D]
    b_pool = max(1, base_combat_pool(target_unit) - _orch.FREED_ATTACKER_FLANK_PENALTY)
    a_net = _orch.roll_pool(a_pool)
    b_net = _orch.roll_pool(b_pool)
    a_deg = _orch.degree_label(a_net, max(1, b_net))
    # [canonical: params/mass_combat.md PP-233 — Damage = successes × (1+Power)]
    dmg = _orch.CASUALTY_SCALE * max(0, _orch.DAMAGE_BY_DEGREE[a_deg](freed_unit.power) - target_unit.dr)
    return dmg


def run_multi_unit_battle(side_a, side_b, pairings, shapes_a, shapes_b,
                          anchor_map, max_battle_turns=8):  # [canonical: mass_battle_v30.md §A.7 — battle-turn cap]
    """Run a multi-unit battle with morale cascade and freed-attacker.

    Args:
        side_a: list of Army objects for side A
        side_b: list of Army objects for side B
        pairings: list of (a_idx, b_idx) — initial engagement pairings.
            Indices into side_a / side_b. Pairs are ordered spatially
            (adjacent pairs = adjacent on battlefield).
        shapes_a, shapes_b: dicts {unit_idx: shape_name}
        anchor_map: position anchor mapping for reset_positions
        max_battle_turns: turn cap

    Returns: dict with winner ('A'|'B'|'draw'), per-turn log, casualties.
    [canonical: designs/provincial/mass_battle_v30.md §A.12 — Morale Cascade,
     Rout contagion brake; Phase 6 Steps 1-3]
    """
    log = []
    # Track active pairings and freed units
    active_pairs = list(range(len(pairings)))
    freed_units = []  # (unit, owner_side, source_pair_idx)
    pursuing_units = []  # (pursuer, routing_unit, pursuer_side, source_pair_idx)

    # ED-MB-0023: Reserve formation (PP-MB-04 / PP-499, §A.6). A pair whose unit is held in Reserve
    # "cannot engage" its first turn -> it is benched now and its pairing COMMITS (re-activates) at
    # RESERVE_COMMIT_TURN (Phase 3 of the next battle-turn), engaging from that turn on. Gated OFF ->
    # reserve is inert and every pair is active from turn 1 (byte-exact).
    reserve_pairs = {}  # pair_idx -> commit battle-turn
    if _orch.MB_RESERVE_COMMIT:
        for _pi, (_ai, _bi) in enumerate(pairings):
            if unit_in_reserve(side_a[_ai]) or unit_in_reserve(side_b[_bi]):
                reserve_pairs[_pi] = _orch.RESERVE_COMMIT_TURN
        active_pairs = [p for p in active_pairs if p not in reserve_pairs]

    for battle_turn in range(1, max_battle_turns + 1):
        turn_log = {
            'turn': battle_turn,
            'engagements': [],
            'cascades': [],
            'freed_attacks': [],
            'pursuits': [],
            'routs_this_turn': [],
        }

        # ── Reserve commitment: a benched reserve pair commits at Phase 3 of its commit turn and may
        #    engage from Phase 5 of that same turn. Its first engagement uses the default equal Off/Def
        #    split (no Phase 1 window) — already this path's behaviour. [canonical: §A.6 P3-02, PP-MB-04]
        if reserve_pairs:
            for _pi, _commit in list(reserve_pairs.items()):
                if battle_turn >= _commit:
                    active_pairs.append(_pi)
                    turn_log.setdefault('reserve_commits', []).append({'pair': _pi, 'turn': battle_turn})
                    del reserve_pairs[_pi]

        # ── Pursuit phase: Fast units pursuing routing enemies ──
        # [canonical: §A.12 L513 — "Routing unit loses Size equal to pursuer
        #  net Offence successes (no Defence) each turn."]
        for pursuer, routing, p_side, p_pair in list(pursuing_units):
            if routing.hp <= 0:
                # Routing unit destroyed — pursuer becomes freed
                pursuing_units.remove((pursuer, routing, p_side, p_pair))
                freed_units.append((pursuer, p_side, p_pair))
                continue
            # Recall check — general tries to pull unit back
            # [canonical: §A.12 — "Recall: Command Ob 2"]
            if _orch.recall_check(pursuer):
                pursuing_units.remove((pursuer, routing, p_side, p_pair))
                freed_units.append((pursuer, p_side, p_pair))
                turn_log['pursuits'].append({
                    'pursuer': pursuer.name, 'target': routing.name,
                    'damage': 0, 'recalled': True,
                })
                continue
            # Pursuit damage
            dmg = _orch.pursuit_damage(pursuer, routing, base_combat_pool)
            if dmg > 0:
                _pursuit_before = routing.hp                       # [ED-MB-0052 / C1]
                routing.hp = max(0, routing.hp - dmg)
                _orch.attribute_hp_loss(routing, _pursuit_before, routing.hp, 'pursuit')
                # [ED-MB-0041] Mirror the loss onto the cells: hp and cells feed DIFFERENT mechanics (hp ->
                # _lanchester_strength, recalc_size, the single-subunit cohesion fast path; cells ->
                # pair_pool_contribution, troop_total()'s UNIT_ROUT_FLOOR check), so both ledgers must move.
                _orch.distribute_casualties(routing, dmg, [])
                routing.recalc_size()
            turn_log['pursuits'].append({
                'pursuer': pursuer.name, 'target': routing.name,
                'damage': dmg, 'recalled': False,
            })
            if routing.hp <= 0:
                pursuing_units.remove((pursuer, routing, p_side, p_pair))
                freed_units.append((pursuer, p_side, p_pair))

        # ── Phase: run each active engagement ──
        # [canonical: designs/provincial/mass_battle_v30.md — Phase 2-5 per pair]
        for pair_idx in list(active_pairs):
            a_idx, b_idx = pairings[pair_idx]
            ua, ub = side_a[a_idx], side_b[b_idx]
            if ua.routed or ub.routed:
                continue

            # Reset positions for this turn's engagement
            reset_positions(ua, shapes_a[a_idx], anchor_map)
            reset_positions(ub, shapes_b[b_idx], anchor_map)

            # Run 3-phase engagement
            r = _orch.run_battle(ua, ub)
            turn_log['engagements'].append({
                'pair': pair_idx, 'a_idx': a_idx, 'b_idx': b_idx,
                'result': r['winner'], 'ticks': r['turns'],
            })

        # ── Freed-attacker bonus damage (from PREVIOUS turn's freed units) ──
        # [canonical: §A.12 — freed unit attacks adjacent enemy from flank]
        for freed_unit, owner_side, source_pair in list(freed_units):
            if freed_unit.routed or freed_unit.disordered:
                freed_units.remove((freed_unit, owner_side, source_pair))
                continue
            # Find adjacent active engagement with an enemy to flank
            target = None
            for adj_offset in [-1, 1]:
                adj_pair = source_pair + adj_offset
                if adj_pair not in active_pairs:
                    continue
                a_idx, b_idx = pairings[adj_pair]
                if owner_side == 'A':
                    # Freed A unit flanks the B unit in adjacent pair
                    enemy = side_b[b_idx]
                else:
                    # Freed B unit flanks the A unit in adjacent pair
                    enemy = side_a[a_idx]
                if not enemy.routed and not enemy.disordered:
                    target = enemy
                    break

            if target:
                dmg = freed_attacker_damage(freed_unit, target)
                if dmg > 0:
                    # [canonical: params/mass_combat.md PP-233 — simultaneous damage]
                    _freed_before = target.hp                      # [ED-MB-0052 / C1]
                    target.hp = max(0, target.hp - dmg)
                    _orch.attribute_hp_loss(target, _freed_before, target.hp, 'freed_attacker')
                    # [ED-MB-0041] mirror the loss onto the cells (as in the pursuit path above) so sum(cell_troops) tracks hp.
                    _orch.distribute_casualties(target, dmg, [])
                    target.recalc_size()
                    # Morale erosion from flanking damage
                    # [canonical: designs/provincial/mass_battle_v30.md §A.4]
                    _disc = target.agg_discipline()   # per-subunit-aware resistance (== unit.discipline if homogeneous)
                    if _disc > 0 and target.command > 0:
                        erosion = dmg / (_disc * target.command)
                        target.cascade_morale_hit(erosion)
                    for atom in target.units:
                        if not atom.routed and atom.eff_morale <= 0:
                            atom.routed = True
                    target.derive_rout()
                    turn_log['freed_attacks'].append({
                        'freed': freed_unit.name, 'target': target.name,
                        'damage': dmg,
                    })

        # ── Check for new routs ──
        newly_routed = []
        for pair_idx in active_pairs:
            a_idx, b_idx = pairings[pair_idx]
            ua, ub = side_a[a_idx], side_b[b_idx]
            if ua.routed:
                newly_routed.append(('A', a_idx, pair_idx))
            if ub.routed:
                newly_routed.append(('B', b_idx, pair_idx))
        turn_log['routs_this_turn'] = [(s, i) for s, i, _ in newly_routed]

        # ── Phase 6 Step 3: Morale Cascade ──
        # [canonical: designs/provincial/mass_battle_v30.md §A.12]
        for routed_side, routed_idx, pair_idx in newly_routed:
            # All friendly units in the SAME engagement check Discipline Ob 1
            a_idx, b_idx = pairings[pair_idx]
            if routed_side == 'A':
                # Check other A units in this pair (for future 2v1 support)
                # For now, same-engagement only has one unit per side
                pass
            else:
                pass
            # Adjacent friendly units: rout contagion (-1, braked)
            # [canonical: designs/provincial/mass_battle_v30.md L167]
            for adj_offset in [-1, 1]:
                adj_pair = pair_idx + adj_offset
                if adj_pair < 0 or adj_pair >= len(pairings):
                    continue
                if adj_pair not in active_pairs:
                    continue
                adj_a, adj_b = pairings[adj_pair]
                if routed_side == 'A':
                    friend = side_a[adj_a]
                else:
                    friend = side_b[adj_b]
                if friend.routed:
                    continue
                # Morale cascade: Discipline check Ob 1
                if not _orch.discipline_check_cascade(friend):
                    friend.cascade_morale_hit(1)
                    turn_log['cascades'].append({
                        'unit': friend.name, 'trigger': f'{routed_side}{routed_idx} routed',
                        'result': 'failed — morale -1',
                    })
                else:
                    turn_log['cascades'].append({
                        'unit': friend.name, 'trigger': f'{routed_side}{routed_idx} routed',
                        'result': 'passed',
                    })
                # Rout contagion: additional -1, braked
                # [canonical: L167 — "Rout causes −1 Morale to adjacent units"]
                friend.cascade_morale_hit(_orch.ROUT_CONTAGION_MORALE_HIT)
                # Brake: this morale loss cannot cause rout this turn
                # (rout check deferred to next turn's engagement resolution)

        # ── Freed-attacker: victor from resolved pair becomes free ──
        # G-11: Fast victors PURSUE routing unit (§A.12). Non-Fast join adjacent.
        for routed_side, routed_idx, pair_idx in newly_routed:
            a_idx, b_idx = pairings[pair_idx]
            victor = None
            routing = None
            if routed_side == 'A' and not side_b[b_idx].routed:
                victor = side_b[b_idx]
                routing = side_a[a_idx]
                victor_side = 'B'
            elif routed_side == 'B' and not side_a[a_idx].routed:
                victor = side_a[a_idx]
                routing = side_b[b_idx]
                victor_side = 'A'

            if victor:
                if victor.speed == "Fast" and routing.hp > 0:
                    # Fast unit pursues — track for ongoing pursuit
                    # [canonical: §A.12 L513 — "Pursuit: Fast units only"]
                    # ED-MB-0022: if the "routing" unit is actually feigning (Feigned Retreat, PP-256),
                    # the pursuer may be deceived and overextend. Inert unless MB_FEIGNED_RETREAT is ON.
                    fr = _orch.resolve_feigned_retreat(victor, routing)
                    if fr is not None:
                        turn_log.setdefault('feigned_retreats', []).append({
                            'pursuer': victor.name, 'feigning': routing.name,
                            'recognized': fr['recognized'], 'overextended': fr['overextended'],
                        })
                    pursuing_units.append((victor, routing, victor_side, pair_idx))
                else:
                    # Non-Fast: freed attacker joins adjacent engagement
                    freed_units.append((victor, victor_side, pair_idx))

        # ── Remove resolved pairs ──
        active_pairs = [p for p in active_pairs
                        if not (side_a[pairings[p][0]].routed or
                                side_b[pairings[p][1]].routed)]

        # ── Log state ──
        turn_log['active_pairs'] = len(active_pairs)
        turn_log['freed_count'] = len(freed_units)
        turn_log['pursuing_count'] = len(pursuing_units)
        for side, units in [('A', side_a), ('B', side_b)]:
            for i, u in enumerate(units):
                turn_log[f'{side}{i}_hp'] = round(u.hp / u.hp_max * 100, 1) if u.hp_max else 0
                turn_log[f'{side}{i}_morale'] = round(u.morale, 3)
                turn_log[f'{side}{i}_routed'] = u.routed
        log.append(turn_log)

        # ── Check termination ──
        # [canonical: §A.12 — pursuit continues until recall or routing unit destroyed]
        # Battle ends when: both sides fully routed, OR no activity remains
        # (no active pairs, no pursuit, no freed attackers with targets)
        a_all_routed = all(u.routed for u in side_a)
        b_all_routed = all(u.routed for u in side_b)
        if a_all_routed and b_all_routed:
            break  # mutual rout — no one left to pursue
        if not active_pairs and not pursuing_units and not reserve_pairs:
            # No engagements, no pursuit, and no reserve still waiting to commit (ED-MB-0023) —
            # freed attackers can't do anything.
            break

        # ── Between-turn recovery ──
        for u in side_a + side_b:
            if not u.routed:
                between_turn_recovery(u)

    # ── Determine winner ──
    a_surviving = sum(1 for u in side_a if not u.routed)
    b_surviving = sum(1 for u in side_b if not u.routed)
    if a_surviving > b_surviving:
        winner = 'A'
    elif b_surviving > a_surviving:
        winner = 'B'
    else:
        winner = 'draw'

    return {
        'winner': winner,
        'battle_turns': len(log),
        'log': log,
        'a_surviving': a_surviving,
        'b_surviving': b_surviving,
        'a_casualties': {i: 1.0 - (u.hp / u.hp_max) if u.hp_max else 1.0
                         for i, u in enumerate(side_a)},
        'b_casualties': {i: 1.0 - (u.hp / u.hp_max) if u.hp_max else 1.0
                         for i, u in enumerate(side_b)},
    }


def base_combat_pool(army):
    if army.routed or army.disordered: return 0
    pen = army.discipline_penalty()
    if pen == -99: army.disordered = True; return 0  # [canonical: mass_battle_v30.md §A.4 — sentinel: -99 disordered-formation flag]
    # Pool uses continuous effective_size (float), floored for dice count.
    # [canonical: mass_battle_v30.md §A.4 Effective Combat Pool; live value =
    #  Command*(1+cohesion) (2*Command at full strength -> Command at annihilation,
    #  ED-899/ED-1013); legacy OFF-path min(Size,Command)+Command at COMMAND_SIGMA_ENABLED=0]
    stam_pen = _hu._stamina_pool_penalty(army.agg_stamina())
    if _hu.POOL_QUALITY_MODEL:
        # [Jordan directive 2026-07-08, mirrors core.exchange.subunit_combat_pool's default
        # branch for the UNIT-level pool this pursuit/rout path uses -- see config.py's
        # POOL_QUALITY_MODEL comment.] No Command: troop-type quality (`power`) x numbers
        # (`effective_size`, the continuously-degrading quantity).
        raw = army.power * army.effective_size * _hu.POOL_QUALITY_SCALE + pen + stam_pen
    elif _hu.COMMAND_SIGMA_ENABLED:
        # SMOOTH POOLS (Jordan 2026-06-15): 2*command at FULL strength (size-decoupled per ED-899),
        # degrading SMOOTHLY with own casualties to command at annihilation via cohesion=hp/hp_max.
        # Cohesion is a FRACTION (not headcount) -> per-capita effectiveness size-independent -> Lanchester
        # exponent stays ~1 (ED-899 preserved). The smooth own-casualty degradation dilutes the discipline
        # term so it can no longer dominate and bias the mirror (the flat-2*command pool was the defect).
        cohesion = army.hp / army.hp_max if army.hp_max else 0.0
        raw = army.command * (1.0 + cohesion) + pen + stam_pen
    else:
        raw = min(army.effective_size, army.command) + army.command + pen + stam_pen
    # ED-MB-0022: an OVEREXTENDED pursuer (failed the PP-256 Feigned Retreat Discipline check)
    # re-engages at a bounded pool penalty. Gated by MB_FEIGNED_RETREAT (default ON). `.overextended` is set
    # only via resolve_feigned_retreat, which requires the feigning unit's `.feigned` (the 'feign_retreat'
    # order pseudo-field, C4, ED-MB-0067 Part C / ED-MB-0071) or a 'lure' instruction (`unit_lures`, MB-04)
    # -- see Army.feigned's own comment.
    # [canonical: mass_battle_v30.md §B.4 — Overextended -2D]
    if _hu.MB_FEIGNED_RETREAT and army.overextended:
        raw -= _hu.OVEREXTEND_PENALTY
    return max(1, math.floor(raw))


__all__ = ['between_turn_recovery', 'reset_morale_between_battles', 'reset_positions', 'run_multi_turn_battle',
           'unit_in_reserve', 'freed_attacker_damage', 'run_multi_unit_battle', 'base_combat_pool']
