"""`run_battle` -- one engagement turn (up to 3 phases = 18 ticks) -- moved out of `orchestration.py` VERBATIM.

ED-1043 (the mass-battle god-file split): CP-T04-03 edits this function's stop test, so its first change was this
extraction, hash EQUAL -- the body below was `orchestration.run_battle` byte for byte except the one call-time import
that stands for the globals it read there; CP-T04-03's one stop-test line (`unit_conceded`) is the only edit since.
`orchestration` re-exports it (`from modules.mass_battle.battle_loop import
run_battle`), so every caller and every `orchestration.run_battle` name resolves as before. Nothing imports this module
directly: it needs `orchestration` loaded, which loads it."""
import math  # noqa: F401  (read by the nested helpers below, as `orchestration`'s own `math` was)
from modules.mass_battle.hierarchy.units import unit_conceded


def run_battle(unit_a, unit_b, max_turns=18):  # [canonical: mass_battle_v30.md §A.7 — 18-tick battle (3 phases x 6)]
    """Run one engagement turn (up to 3 phases = 18 ticks).
    v16: max_turns=18 = one battle turn's engagement cap (3 phases).
    Multi-turn battles call this repeatedly with persistent unit state.
    [canonical: Jordan direction — "limit of three phases per simultaneous
     engagement per turn"]

    Returns:
      {"winner": "A"|"B"|"draw", "turns": int, "phases": int, "tick_in_phase": int}
    """
    # ED-1043: the names this function reads are resolved from `orchestration` AT CALL TIME, as the globals they were
    # while it lived there (a patch on `orchestration.<name>` is still seen), and so that this module need not
    # import `orchestration` at load (it imports this one).
    from modules.mass_battle.orchestration import (
        CASCADING_ENABLED, COL_WIDTH, FIELD_MOVEMENT, LANCHESTER_ENABLED, MB_CELL_DAMAGE, MB_CLOSE_RANKS,
        MB_ENVELOP_SHOCK, MB_FRONTAGE_BLEND, MB_FRONTAGE_REF, MB_NODE_COHESION, PER_CELL,
        STAMINA_DRAIN_PER_CONTACT_CELL, SUBUNIT_ROUT_FLOOR, TICKS_PER_PHASE, VOLLEY_LETHALITY_SCALE, _draw_friction,
        _engaged_cols, _is_moving_atom, _oriented, _unit_snapshot, apply_to_subunit, assign_targets,
        attribute_hp_loss, check_orders, discipline_check_cascade, distribute_casualties,
        distribute_casualties_cellwise, find_contacts, phase_boundary, reach_for, resolve_cross_side_contention,
        resolve_engagements, resolve_engagements_cascading, resolve_toi_and_commit, separate_all_bodies,
        sync_col_grid, trace_event, tracing_on, turn_to_face_aggressors, update_stamina, volley_phase,
    )
    # [movement-substrate review 06 — coordinate-field migration] The continuous COORDINATE FIELD requires
    # the node float path: field-ON stores/emits true floats only via _node_pos (MB_NODE_COHESION). A
    # FIELD-ON / NODE-OFF run would silently half-migrate (legacy integer branch, no floats, but the
    # fractional-speed accumulator active) -> a degenerate integer 'field' run. Enforce the implication at
    # setup so the invalid combination fails loudly instead of producing a corrupt result. No-op when
    # FIELD_MOVEMENT is OFF (byte-exact).
    assert (not FIELD_MOVEMENT) or MB_NODE_COHESION, \
        "FIELD_MOVEMENT=1 requires MB_NODE_COHESION=1 (the coordinate field runs on the node float path)"
    # [ED-MB-0016, DG-6 resolution] Draw each side's per-BATTLE combat-effectiveness friction factor
    # ONCE, lazily: the FIRST run_battle entry for a fresh unit draws it; subsequent turns of a multi-turn
    # battle (which re-enter run_battle with persistent unit state) see it already set and do NOT re-draw
    # -- so the shock is drawn once per battle, not per turn (per-turn re-draws would self-average away the
    # very variance this restores). A fresh unit per gauge trial gets a fresh draw. Default-inert: with
    # MB_FRICTION off, _draw_friction sets 1.0 (no behaviour change; byte-exact). Uses the seeded
    # `random` stream so determinism (I2) holds; enabling it shifts the stream (field goldens re-record).
    _draw_friction(unit_a)
    _draw_friction(unit_b)
    turns = 0
    current_phase = 0
    separate_all_bodies(unit_a, unit_b)   # an army is deployed clear of itself and of the enemy
    # [ED-MB-0048 / A3] battle-scoped totals for the sub-phase truncation counter; see
    # resolve_engagements_cascading. Zero on every shipped workload measured so far — the
    # value of carrying them is that a non-zero is now READABLE rather than needing a probe.
    trunc_groups = trunc_pairs = 0
    trunc_troops = 0.0
    max_groups = 0
    for t in range(1, max_turns + 1):
        turns = t
        trace_event('tick', t=t)
        if unit_a.routed or unit_b.routed: break
        # CP-T04-03: a side every subunit of which has retreated or routed has conceded the field; the battle stops for
        # it as a rout stops it, and `unit.routed` is not set, so it takes no rout facing flip. `massbattle._grade`
        # reads the same predicate, so a conceded side is never graded the winner.
        if unit_conceded(unit_a) or unit_conceded(unit_b): break
        # Phase 2 — Volley. Ranged atoms fire at range BEFORE movement.
        # Damage accumulated here, applied with Phase 5 damage at end of turn.
        # [canonical: mass_battle_v30.md §A.7 Phase 2; PP-503]
        vol = volley_phase(unit_a, unit_b)
        volley_dmg_a = vol["loss_a"]
        volley_dmg_b = vol["loss_b"]
        # Pre-movement contacts -> halt
        pre_pairs = find_contacts(unit_a, unit_b)
        for atom in unit_a.subunits + unit_b.subunits:
            atom.halted_cells = set()
        for p in pre_pairs:
            # [migration H] recompute abs from _node_pos (file-binned) on ON so it matches find_contacts'
            # (file-binned) cells; OFF = verbatim cell_offsets build. Otherwise the == misses on the node
            # path and halted_cells stays empty -> pre-contact halt silently disabled on the field path.
            for _atom, _cells in ((p["atom_a"], p["a_cells"]), (p["atom_b"], p["b_cells"])):
                _fld = FIELD_MOVEMENT and MB_NODE_COHESION and hasattr(_atom, '_node_pos')
                op = _oriented(_atom)
                for cell in _cells:
                    for orig_r, orig_c, or_r, or_c in op:
                        if _fld:
                            _pr, _pc = _atom._node_pos.get((orig_r, orig_c), (0.0, 0.0))
                            abs_r = int(round(_pr)); abs_c = int(round(_pc / COL_WIDTH))
                        else:
                            abs_r = (_atom.starting_position[0] + or_r
                                     + _atom.cell_offsets.get((orig_r,orig_c), 0) * _atom.advance_dir)
                            abs_c = (_atom.starting_position[1] + or_c
                                     + _atom.cell_offsets_c.get((orig_r,orig_c), 0))
                        if (abs_r, abs_c) == cell:
                            _atom.halted_cells.add((orig_r, orig_c)); break
        # [Stage C] check_orders BEFORE assign_targets -- a fired order's behavior dict may itself set
        # target_condition/target_delay_ticks/stance/instructions, so orders must land first. Hoisting
        # a_cells_set/b_cells_set up here (they were computed just after assign_targets) is a pure,
        # behavior-preserving reorder: both are recomputed fresh from current cell positions with no
        # side effects, so moving the computation 3 lines earlier changes nothing else.
        b_cells_set = set(c for sub in unit_b.subunits for c in sub.cells())
        a_cells_set = set(c for sub in unit_a.subunits for c in sub.cells())
        check_orders(unit_a, t, b_cells_set)
        check_orders(unit_b, t, a_cells_set)
        assign_targets(unit_a, unit_b)
        # v21: SIMULTANEOUS RESOLUTION — cache all target centroids BEFORE any
        # atom moves. Without this, unit_a advances toward unit_b's pre-move
        # centroid, but unit_b advances toward unit_a's POST-move centroid,
        # creating ~10% first-arg bias. With caching, both sides see each
        # other's pre-move positions symmetrically.
        # [canonical: params/mass_combat.md PP-233 — "Damage is simultaneous"]
        cached_centroids = {}
        for atom in unit_a.subunits + unit_b.subunits:
            if atom.target_atom:
                cached_centroids[id(atom)] = atom.target_atom.centroid()

        # [Stage C] Escort / formation-relative positioning ("hold position in front of the marching
        # archers"). A screening subunit (escort_of set) has no enemy target yet, so it was never in
        # cached_centroids above and the movement gate below (`if atom.target_atom:`) never fired for
        # it — confirmed dead code in an earlier draft. Two additive fixes, computed here (same
        # synchronized pre-move point as cached_centroids, preserving the v21 simultaneity discipline):
        # latch the one-shot engage-on-contact switch now that assign_targets has run (a just-acquired
        # real target_atom takes over targeting immediately, not one tick late), then give any
        # still-escorting atom a centroid to advance toward -- the escorted subunit's live centroid
        # plus escort_offset ROTATED into its current facing frame (not the static spawn-time
        # advance_dir), so screening survives the escorted unit wheeling/enveloping/sweeping.
        def _escort_facing(sub):
            if MB_NODE_COHESION and getattr(sub, '_node_facing', None) is not None:
                fr, fc = sub._node_facing
            elif sub.cell_facing_vec:
                _vecs = list(sub.cell_facing_vec.values())
                fr = sum(v[0] for v in _vecs) / len(_vecs)
                fc = sum(v[1] for v in _vecs) / len(_vecs)
            else:
                fr, fc = sub.advance_dir, 0
            mag = math.hypot(fr, fc)
            return (fr / mag, fc / mag) if mag > 1e-9 else (float(sub.advance_dir), 0.0)  # [canonical: epsilon: float magnitude guard]

        for atom in unit_a.subunits + unit_b.subunits:
            if (atom.escort_of is not None and atom.escort_engage_on_contact
                    and not atom._escort_engaged and atom.target_atom is not None):
                atom._escort_engaged = True
            # NOTE: the escort centroid overrides cached_centroids whenever escorting-and-not-yet-
            # engaged, regardless of target_atom -- assign_targets' default 'nearest' condition sets
            # target_atom to SOME enemy unconditionally the instant one exists (it is not gated on
            # range), so gating this override on "target_atom is None" (an earlier version of this
            # fix did) left it dead in every ordinary scenario: target_atom becomes non-None almost
            # immediately, long before real contact, and the escort would silently start chasing the
            # enemy directly instead of holding its screening position -- confirmed empirically (a
            # screen with escort_engage_on_contact=False still switched to chasing the enemy on tick
            # 1). "Screen IS the front line" (the False default) means movement is governed by the
            # escort relationship until the one-shot latch above actually fires; a caller wanting
            # real range-gated engagement should set target_condition='in_range:D' on the escorting
            # subunit (an existing primitive) rather than relying on target_atom's mere presence.
            if atom.escort_of is not None and not atom._escort_engaged:
                _esc = atom.escort_of
                _fr, _fc = _escort_facing(_esc)
                _ex, _ey = _esc.centroid()
                _dr, _dc = atom.escort_offset
                cached_centroids[id(atom)] = (_ex + _dr * _fr - _dc * _fc, _ey + _dr * _fc + _dc * _fr)

        def _cells_float_of(unit):
            return [(r, c, reach_for(sub.troop_type)) for sub in unit.subunits for (r, c) in sub.cells_float()]

        # [TOI refactor] b_cells_float/a_cells_float are now consulted by _node_advance ONLY for
        # truthiness -- a non-empty list signals "defer to the cross-side TOI resolve rather than
        # commit immediately" (see _node_advance's toi_deferred). The actual cross-side standoff
        # computation (reach- and facing-asymmetric, exact time-of-impact) now runs once, after both
        # sides have proposed, in resolve_toi_and_commit below -- replacing the old sequential,
        # halved-closing-budget anchor pre-cap this comment used to describe (see git history: that
        # design fixed a real first-mover bias but only approximately, and was retired once the bias's
        # true fix -- exact per-pair TOI -- was designed properly instead of adopted under time
        # pressure). None when FIELD_MOVEMENT is off -> zero cost, byte-exact.
        b_cells_float = _cells_float_of(unit_b) if FIELD_MOVEMENT else None
        a_cells_float = _cells_float_of(unit_a) if FIELD_MOVEMENT else None
        # [Stage C] additive `or` clause: a screening escort (escort_of set, not yet engaged) moves
        # even with target_atom=None, using the escort centroid computed above. Every existing
        # scenario's `if atom.target_atom:` case is untouched (escort_of defaults to None).
        # [A1, ED-MB-0067 Part A] second additive `or` clause: a sub-unit marching an unfinished
        # route moves even with no target_atom/escort at all (no enemy in sight yet) -- there is no
        # cached_centroids entry for such an atom (the loops above only populate one for a
        # target_atom or an escort), so the advance_cells calls below use .get(id(atom)) instead of
        # a bare [id(atom)] indexing and pass target_centroid=None for it; _node_advance's own gate
        # (see its comment) is what makes a None target_centroid safe here, and its _resolve_route_
        # goal/_resolve_maneuver_goal chain is what actually supplies the route as the goal.
        # [F5, adversarial-pass round 2] The route clause is gated on the node path actually being
        # active -- see _is_moving_atom's own docstring for why inclusion without that guard was
        # not the harmless no-op it looked like on the legacy-lattice arm.
        moving_a = [atom for atom in unit_a.subunits if _is_moving_atom(atom)]
        moving_b = [atom for atom in unit_b.subunits if _is_moving_atom(atom)]
        for atom in moving_a:
            # per-subunit formation-hold: each subunit advances on its OWN Discipline
            # (single-subunit inherits -> == unit.discipline -> byte-exact)
            atom.advance_cells(atom.eff_discipline, cached_centroids.get(id(atom)),
                               enemy_cells=b_cells_set, enemy_cells_float=b_cells_float)
        for atom in moving_b:
            atom.advance_cells(atom.eff_discipline, cached_centroids.get(id(atom)),
                               enemy_cells=a_cells_set, enemy_cells_float=a_cells_float)
        # [TOI refactor] On the FIELD_MOVEMENT path, the advance_cells calls above only PROPOSED
        # (uncapped) end-of-tick positions for every atom on BOTH sides -- enemy_cells_float being
        # non-empty (b_cells_float/a_cells_float, built above) signals _node_advance to defer rather
        # than commit. Resolve the cross-side continuous-collision time-of-impact ONCE, across both
        # sides together (not per-atom, not sequential), and commit final positions now. Replaces the
        # old per-atom halved-anchor-precap + iterated per-cell pull-back entirely.
        #
        # Pass ALL subunits (unit_a.subunits/unit_b.subunits), not just moving_a/moving_b: a subunit
        # with no target yet (a reserve, or gated by target_delay_ticks/target_condition) never called
        # advance_cells and so has no pending proposal, but its cells are real, occupied positions that
        # the OTHER side's moving cells must still treat as obstacles -- resolve_toi_and_commit reads
        # such atoms' current true positions directly (adversarial-review-caught: an earlier version
        # passed only moving_a/moving_b, silently dropping idle/reserve subunits as obstacles for a
        # tick, a regression versus the pre-refactor enemy_cells_float, which was always built from
        # ALL of a unit's subunits unconditionally).
        if FIELD_MOVEMENT:
            resolve_toi_and_commit(unit_a.subunits, unit_b.subunits)
        # v11: vector halt-at-contact — prevent over-run that creates paradoxical angles
        for atom in unit_a.subunits: atom.halt_before_enemy(unit_b)
        for atom in unit_b.subunits: atom.halt_before_enemy(unit_a)
        # v13: cross-side cell contention (speed → size → random priority).
        # After both sides have advanced, cells from opposing sides may occupy the
        # same abs position. Resolve per Jordan design 2026-05-12: higher-speed
        # cell wins; tie → greater size; tie → random. Losers that moved this turn
        # revert; static losers shift back 1 step ("end-of-phase displacement").
        # [canonical: Jordan design 2026-05-12 — same-cell contention rules]
        resolve_cross_side_contention(unit_a, unit_b)
        # v13: within-side discipline-gated formation hold (Subunit method
        # resolve_internal_collisions, DELETED per ED-MB-0057's re-adjudicated disposition —
        # zero call sites since 2026-05-29; it over-tuned battery 12/13 -> 9/13 and its
        # co-location case is closed by ED-MB-0059's same-side field exclusion below instead).
        # No replacement call site: nothing here invokes it, before or after.
        pairs = find_contacts(unit_a, unit_b)
        # v20: stamina drain proportional to cells in contact (bottom-up).
        # More front-line cells fighting = more exhaustion. Emergent from formation.
        if pairs:
            # Per-subunit stamina drain (Jordan directive): each ENGAGED subunit drains by ITS OWN cells in
            # contact; a subunit not in this tick's contact set (a reserve) does not drain -> rotation. For a
            # single-subunit unit the one subunit's contact-cells == the unit's, so unit.stamina drains
            # identically to the old unit-level drain (byte-exact).
            for u in [unit_a, unit_b]:
                if u.routed:
                    continue
                for atom in u.subunits:
                    if atom.routed or atom.broken:
                        continue
                    cic = 0
                    for p in pairs:
                        if p.get('atom_a') is atom:
                            cic += len(p.get('a_cells', []))
                        elif p.get('atom_b') is atom:
                            cic += len(p.get('b_cells', []))
                    if cic > 0:
                        atom.drain_stamina(cic * STAMINA_DRAIN_PER_CONTACT_CELL)
        result = (resolve_engagements_cascading(unit_a, unit_b, pairs, t=t)
                  if CASCADING_ENABLED
                  else resolve_engagements(unit_a, unit_b, pairs, t=t))
        # [ED-MB-0048 / A3] Accumulate the truncation counters. `.get` because the keys exist
        # only on the cascading path — truncation is a property of sub-phase grouping and cannot
        # occur when CASCADING_ENABLED is off, so their absence there is correct, not a gap.
        trunc_groups += result.get("truncated_groups", 0)
        trunc_pairs += result.get("truncated_pairs", 0)
        trunc_troops += result.get("truncated_troops", 0.0)
        max_groups = max(max_groups, result.get("n_groups", 0))
        # Apply Phase 2 Volley + Phase 5 Engagement damage simultaneously at Phase 6 Step 1
        # [canonical: mass_battle_v30.md §A.7 — Volley/Thread/Engagement damage applied together]
        # v12: Volley size-loss → hp uses ceil(h_per_size / 2), not full h_per_size.
        # Bottom-up rationale: a ranged "size loss" represents arrows finding targets in
        # the formation; many hits glance off shields/armor. Melee size loss represents
        # men killed in close combat, where wounds are decisive. Halving the conversion
        # captures that volley size loss is less lethal per unit than melee size loss.
        # Reduces R1 (Ranged vs Line) without breaking R3 (mirror — same scaling on both sides).
        # [canonical: Jordan design 2026-05-12 — volley hp scaling tuned for historical match]
        # [ED-MB-0041 FIX] Volley loss -> troop conversion must NOT depend on the target's own quality.
        # This previously read `max(1, (u.h_per_size + 1) // 2)` where
        # `h_per_size = max(1, min(discipline, command) + dr)`, so BETTER ARMOUR, DISCIPLINE OR COMMAND
        # STRICTLY INCREASED the missile casualties that unit took (dr 1 -> x3, dr 3 -> x4). Historically
        # backwards without qualification. It is a fossil of the retired `hp = size x h_per_size` model;
        # `hp_max` is now the raw troop count (hierarchy/units.py:1924), so the factor is a pure
        # Size->troops lethality scale and has no business reading the target's stats.
        # Held at 3 = the value the gauge baseline (disc 5, cmd 4, dr 1) produced, so this removes the
        # inversion WITHOUT silently re-tuning ranged lethality; armour's real effect now lives where it
        # belongs, in the DR subtraction above.
        # [JUSTIFIED: magnitude preserved from the prior baseline to isolate the inversion fix; the
        #  underlying scale is admitted band-fitting (file header v12 note #4) and is Tier-3 debt.]
        # v20: scale engagement damage by contact fraction.
        # More cells in contact = more soldiers fighting = more damage dealt.
        # Bottom-up: the envelopment advantage EMERGES from having more cells engaged.
        # contact_fraction = cells_in_contact / total_cells. Capped at 1.0.
        # P-L: SKIPPED under LANCHESTER_ENABLED — numbers-in-contact is carried by the
        # linear term in resolve_engagements (one role, one place). Skipping here also
        # makes LANCHESTER_ENABLED=0 byte-exact to the pre-P-L engine.
        if pairs and not LANCHESTER_ENABLED:
            for u, dmg_key in [(unit_a, "dmg_a"), (unit_b, "dmg_b")]:
                # The OPPONENT's contact fraction scales their damage against us
                # More of the opponent's troops fighting = more damage TO us
                opp = unit_b if u is unit_a else unit_a
                opp_cells_contact = set()
                opp_total = 0
                for sub in opp.subunits:
                    opp_total += len(list(sub.cells()))
                    for p in pairs:
                        if p.get('atom_a') is sub:
                            opp_cells_contact.update(p.get('a_cells', []))
                        elif p.get('atom_b') is sub:
                            opp_cells_contact.update(p.get('b_cells', []))
                # Scale damage: opponent's contact fraction → damage to us
                if PER_CELL and getattr(opp, 'col_grid', None):
                    # Increment 4: depth-aware BLEND. Frontage term (engaged cols / total cols) removes the
                    # reserve-depth penalty; width term (engaged cols / reference frontage) keeps the legitimate
                    # "a wider front brings more men to bear" effect. MB_FRONTAGE_BLEND in [0,1] trades between them.
                    grid = opp.col_grid
                    eng_cols = _engaged_cols(opp, pairs)
                    alive_cols = [b for b in grid if b.alive()]
                    n_alive = len(alive_cols)
                    n_eng = sum(1 for b in alive_cols if b.col in eng_cols)
                    frontage_term = (n_eng / n_alive) if n_alive else 0.0          # depth-neutral
                    width_term = min(1.0, n_eng / MB_FRONTAGE_REF)                  # more engaged columns = more men
                    opp_frac = MB_FRONTAGE_BLEND * frontage_term + (1.0 - MB_FRONTAGE_BLEND) * width_term
                else:
                    opp_frac = len(opp_cells_contact) / max(1, opp_total)
                result[dmg_key] = result[dmg_key] * max(0.2, opp_frac)
        # v21: SIMULTANEOUS HP — apply damage to both units, THEN recalc_size
        # for both. Prevents size recalc of unit_a from affecting anything
        # before unit_b's damage is applied.
        # [canonical: params/mass_combat.md PP-233 — "Damage is simultaneous.
        #  Both sides deal and receive damage before Size is recalculated."]
        # [ED-MB-0052 / C1] Attribution brackets the EXISTING assignment; the arithmetic below is
        # byte-identical to what it replaced. Melee and volley are separated by computing each
        # side's split from the same terms the assignment uses — no second derivation of either.
        _a_before, _b_before = unit_a.hp, unit_b.hp
        _vol_a = volley_dmg_a * VOLLEY_LETHALITY_SCALE
        _vol_b = volley_dmg_b * VOLLEY_LETHALITY_SCALE
        unit_a.hp = max(0, unit_a.hp - result["dmg_a"] - volley_dmg_a * VOLLEY_LETHALITY_SCALE)
        unit_b.hp = max(0, unit_b.hp - result["dmg_b"] - volley_dmg_b * VOLLEY_LETHALITY_SCALE)
        if tracing_on():
            # Split the clamped total across its two sources in proportion to their nominal share,
            # so the parts always sum to the whole even on a killing blow (where the clamp bites).
            for _u, _before, _after, _melee, _vol in (
                    (unit_a, _a_before, unit_a.hp, result["dmg_a"], _vol_a),
                    (unit_b, _b_before, unit_b.hp, result["dmg_b"], _vol_b)):
                _nominal = _melee + _vol
                _actual = _before - _after
                _share = (_actual / _nominal) if _nominal > 0 else 0.0
                attribute_hp_loss(_u, _before, _before - _melee * _share, 'melee', t=t,
                                  phase=current_phase)
                attribute_hp_loss(_u, _before, _before - _vol * _share, 'volley', t=t,
                                  phase=current_phase)
        if PER_CELL:
            # Increment 2: mirror the same total casualties onto the per-column grid (keeps sum==hp).
            # E: ORDERED volley fire concentrates its portion on the target subunit (apply_to_subunit); the
            # unordered remainder spreads as before. Same totals -> sum==hp preserved; with no ordered fire
            # (the default) this is byte-exact-identical to the prior two distribute_casualties calls.
            _ord_a = vol.get("ordered_a", [])
            _ord_b = vol.get("ordered_b", [])
            _ord_a_tot = sum(_d for _su, _d in _ord_a)
            _ord_b_tot = sum(_d for _su, _d in _ord_b)
            # [ED-MB-0040] MELEE casualties land CELLWISE (per-cell facing weights from the resolver) when
            # MB_CELL_DAMAGE is on; the VOLLEY remainder keeps the aggregate density spread (area fire is not
            # a contact-facing exchange, so it has no per-cell arc). Flag OFF -> one combined aggregate call,
            # byte-exact as before.
            _cda = result.get("cell_dmg_a") if MB_CELL_DAMAGE else None
            _cdb = result.get("cell_dmg_b") if MB_CELL_DAMAGE else None
            if _cda:
                distribute_casualties_cellwise(unit_a, result["dmg_a"], _cda)
                distribute_casualties(unit_a, (volley_dmg_a - _ord_a_tot) * VOLLEY_LETHALITY_SCALE, pairs)
            else:
                distribute_casualties(unit_a, result["dmg_a"] + (volley_dmg_a - _ord_a_tot) * VOLLEY_LETHALITY_SCALE, pairs)
            if _cdb:
                distribute_casualties_cellwise(unit_b, result["dmg_b"], _cdb)
                distribute_casualties(unit_b, (volley_dmg_b - _ord_b_tot) * VOLLEY_LETHALITY_SCALE, pairs)
            else:
                distribute_casualties(unit_b, result["dmg_b"] + (volley_dmg_b - _ord_b_tot) * VOLLEY_LETHALITY_SCALE, pairs)
            for _su, _d in _ord_a:
                apply_to_subunit(unit_a, _su, _d * VOLLEY_LETHALITY_SCALE)
            for _su, _d in _ord_b:
                apply_to_subunit(unit_b, _su, _d * VOLLEY_LETHALITY_SCALE)
            if MB_CLOSE_RANKS:
                # [ED-MB-0028] Cell-level closing-ranks: AFTER both units' casualties are applied (so it
                # stays simultaneous — neither side's reflow sees the other mid-tick), rear cells step up
                # to refill the leading ranks toward spawn density, depleting from the back. Re-sync the
                # emergent column grid from the moved cell state. Gated OFF -> byte-exact (skipped entirely).
                for _a in unit_a.subunits:
                    _a.close_ranks()
                for _a in unit_b.subunits:
                    _a.close_ranks()
                sync_col_grid(unit_a)
                sync_col_grid(unit_b)
            update_stamina(unit_a, pairs)   # Increment 3: drain engaged (depth-damped), rest others
            update_stamina(unit_b, pairs)
        unit_a.recalc_size()
        unit_b.recalc_size()
        # v18: discipline degradation moved to phase_boundary (D-6).
        # Per-tick integer Size changes are rare at TroopCount HP scale.
        # check_drift still runs per-tick for formation coherence.
        for u in [unit_a, unit_b]:
            if not u.routed and not u.broken:
                u.check_drift()
        # v21: SIMULTANEOUS MORALE — compute erosion for both units, then
        # check rout for both. Prevents ordering from affecting which unit
        # routs first within a single tick.
        # [canonical: designs/provincial/mass_battle_v30.md §A.4 — generalship]
        # step 3 (Jordan directive 2026-06-03): per-tick ABSOLUTE-damage morale erosion REMOVED.
        # Morale degrades by canonical Size-fraction triggers at the phase boundary (morale_check_phase, §A.4).
        for u in [unit_a, unit_b]:
            if u.routed: continue
            # General incapacitated/captured (ED-898): Command=0 → instant rout (M1: general IS the army).
            # Command=0 models a general removed from command (incapacitated, captured if field lost) — never killed.
            # [canonical: designs/provincial/mass_battle_v30.md §A.4/§A.5 — "General incapacitated/captured (Stage 2): Morale −2 (uncapped), Command=0"; ED-898 death→capture reframe]
            if u.command <= 0:
                u.set_morale(0.0)   # [ED-MB-0042 sweep] must reach the cells, else the rout never lands
                continue  # rout check below

        # [ED-MB-0075 option (2), superseding row 2026-09-28 — C2/C3, ED-MB-0067 Part C] Envelopment-shock
        # damage-to-morale coupling. C2 ruled the rear/flank damage multiplier (ED-MB-0018) a CONTRIBUTING
        # CAUSE of morale collapse; C3 ruled it "checked against Discipline". This is that check, at the
        # scale run_battle already commits damage at (above, dmg_a/dmg_b — NOT run_multi_unit_battle's
        # cross-pair post-processing, a different scale of the simulation). A unit flagged shocked this
        # tick (result["shocked_a"/"shocked_b"], OR-accumulated over every engaged pair/sub-phase) rolls
        # discipline_check_cascade (Ob 1); on FAIL (does not resist), the damage it received this tick
        # erodes morale by the SAME formula run_multi_unit_battle's freed_attacker path uses (erosion =
        # dmg / (agg_discipline x command), via cascade_morale_hit) rather than the erosion formula-only
        # (no-roll) or roll-scaled-by-margin alternatives Part D also specified and did not recommend.
        # REPLACES the prior pre-combat delta-sigma penalty on the shocked unit's own net successes
        # (resolve_engagements's old `ns_a/ns_b += _charge_shock_sigma(...)` in this same elif) — the
        # sibling CHARGE-shock branches (the `if a_pen/b_pen > 0` arms immediately above them in
        # resolve_engagements) are untouched: a different, already-ratified mechanism (engine.py:58,
        # status WIRED), out of scope here. MB_ENVELOP_SHOCK-gated defensively even though shocked_a/b can
        # only be True when it is already on (resolve_engagements only sets them inside its own
        # MB_ENVELOP_SHOCK-gated elif) — byte-exact OFF, same convention as every other MB_ flag here.
        if MB_ENVELOP_SHOCK:
            for u, _shocked, _dmg in ((unit_a, result.get("shocked_a", False), result["dmg_a"]),
                                       (unit_b, result.get("shocked_b", False), result["dmg_b"])):
                if not _shocked or u.routed or u.broken:
                    continue
                _sdisc = u.agg_discipline()
                if _sdisc > 0 and u.command > 0 and not discipline_check_cascade(u):
                    u.cascade_morale_hit(_dmg / (_sdisc * u.command))

        # Rout check AFTER both erosions applied — per-subunit, then derive the unit rout
        # [ED-MB-0041 Tier-2] The two rout triggers are now aligned. Morale collapse was checked here,
        # per TICK; the annihilation trigger (troop_total below SUBUNIT_ROUT_FLOOR) was checked only in
        # rout_resolution, which runs at a PHASE boundary — every TICKS_PER_PHASE (=6) ticks. So a
        # subunit ground below the floor kept fighting, at full effectiveness, for up to 5 more ticks
        # before it was allowed to break. Both are "this body has stopped being a body"; both belong on
        # the same clock. rout_resolution still runs the same check at the boundary (harmless: setting
        # an already-set flag), so its canonical §A.12 sequencing is untouched.
        for u in [unit_a, unit_b]:
            if u.routed:
                continue
            for atom in u.subunits:
                if not atom.routed and (atom.eff_morale <= 0
                                        or atom.troop_total() < SUBUNIT_ROUT_FLOOR):
                    atom.routed = True
            u.derive_rout()   # single-subunit: fires iff old `u.morale<=0` did (byte-exact)
        # v15: phase boundary — stamina_check, morale_check_phase, rout_resolution
        # are now populated (G-1 + G-2). rally/reform/threadwork remain empty.
        if t % TICKS_PER_PHASE == 0:
            current_phase += 1
            phase_boundary(unit_a, unit_b, current_phase)
        # A cell with enemies on it turns toward them (per cell, rate-limited); then no two bodies interpenetrate at the
        # end of any tick, whatever step last wrote a position.
        turn_to_face_aggressors(unit_a, unit_b)
        separate_all_bodies(unit_a, unit_b)
        if tracing_on():
            trace_event('positions', t=t, a=_unit_snapshot(unit_a), b=_unit_snapshot(unit_b))
    winner = ("A" if not unit_a.routed and unit_b.routed else
              "B" if not unit_b.routed and unit_a.routed else "draw")
    tick_in_phase = turns % TICKS_PER_PHASE if turns else 0
    return {"winner": winner, "turns": turns,
            "phases": current_phase, "tick_in_phase": tick_in_phase,
            "a_stamina": unit_a.agg_stamina(), "b_stamina": unit_b.agg_stamina(),
            "a_hp_pct": round(unit_a.hp / unit_a.hp_max * 100, 1) if unit_a.hp_max else 0,
            "b_hp_pct": round(unit_b.hp / unit_b.hp_max * 100, 1) if unit_b.hp_max else 0,
            "a_morale": unit_a.morale, "b_morale": unit_b.morale,
            # [ED-MB-0048 / A3] sub-phase truncation, battle-scoped. Not in trial_vector, so it
            # cannot move a golden; readable by any harness that wants to know whether the
            # MAX_SUB_PHASES bound bit during a run.
            "truncated_groups": trunc_groups, "truncated_pairs": trunc_pairs,
            "truncated_troops": trunc_troops, "max_groups": max_groups}

