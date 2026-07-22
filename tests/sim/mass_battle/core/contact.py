"""mass_battle.core.contact — targeting + contact detection (the contact-event layer).
Stage-1 behaviour-frozen extract from orchestration.py (assign_targets, resolve_cross_side_contention,
find_contacts, count_engagements_per_atom). Depends on geometry (_oriented/octagon/facing) + config +
math + duck-typed unit/atom methods; no up-DAG import (no cycle). Re-imported by orchestration via
star-import so resolve_engagements/run_battle and every caller are unchanged.
[canonical: mass_battle_v30.md §A.7 manoeuvre/contact]"""
import math
from mass_battle.config import *
from mass_battle.geometry import *

__all__ = ['check_orders', 'assign_targets', 'resolve_cross_side_contention', 'find_contacts', 'count_engagements_per_atom']


def check_orders(unit, t, enemy_cells):
    """[Stage C] Fire each subunit's pending orders (Subunit.orders, a Tuple[Order,...]) whose trigger
    condition is met this tick. Called once per tick per side, BEFORE assign_targets (an order's
    behavior dict may itself set target_condition/target_delay_ticks/etc., so orders must land first).
    Orders fire in sequence -- a later order cannot fire before an earlier one's trigger is satisfied.
    Reuses the exact 'kind:value' trigger-parsing idiom already in production for target_condition's
    'in_range:N' (see assign_targets, immediately below) -- no new parsing pattern.

    Triggers: 'immediate' | 'tick:N' (t >= N) | 'enemy_range:D' (within D of the nearest enemy cell) |
    'ally_at:D' (within D of order.waypoint_ref's centroid -- the allied Subunit to watch).

    Byte-exact: Subunit.orders defaults to () -- the while loop body never executes for any existing
    Subunit, the identical safe-default pattern as the already-shipped target_delay_ticks: int = 0."""
    for sub in unit.subunits:
        while sub._order_idx < len(sub.orders):
            order = sub.orders[sub._order_idx]
            fired = False
            if order.trigger == 'immediate':
                fired = True
            elif order.trigger.startswith('tick:'):
                fired = t >= int(order.trigger.split(':', 1)[1])
            elif order.trigger.startswith('enemy_range:'):
                D = float(order.trigger.split(':', 1)[1])
                if enemy_cells:
                    my = sub.centroid()
                    fired = min(math.hypot(my[0] - er, my[1] - ec) for (er, ec) in enemy_cells) <= D
            elif order.trigger.startswith('ally_at:'):
                D = float(order.trigger.split(':', 1)[1])
                if order.waypoint_ref is not None:
                    my = sub.centroid(); wp = order.waypoint_ref.centroid()
                    fired = math.hypot(my[0] - wp[0], my[1] - wp[1]) <= D
            if not fired:
                break
            for k, v in order.behavior.items():
                setattr(sub, k, v)
            # [ED-1095] Track when 'brace' most recently BECAME present via an order (vs. having been
            # present since construction, stamped 0 in __post_init__) -- resolution._subunit_braced
            # requires a full tick since this stamp before treating the subunit as braced. Reset to -1
            # on removal so a later re-brace gets its own fresh delay rather than reusing a stale stamp.
            if 'brace' in sub.instructions:
                if sub._brace_since_tick < 0:
                    sub._brace_since_tick = t
            else:
                sub._brace_since_tick = -1
            sub._order_idx += 1


def assign_targets(unit_a, unit_b):
    """Assign target_atom per subunit every tick.
    Priority: delay countdown > order_target_idx (direct by index) > target_condition.
    Conditions: 'nearest'(default) | 'weakest'(fewest remaining troops) | 'in_range:N'(hold until within N).
    Delay: target_delay_ticks=N holds the subunit N ticks before first activation (one-shot countdown)."""
    def _pick(atom, enemies):
        if not enemies: return None
        if atom.target_delay_ticks > 0:
            atom.target_delay_ticks -= 1
            return None                                          # subunit holds this tick
        if atom.order_target_idx is not None and atom.order_target_idx < len(enemies):
            return enemies[atom.order_target_idx]               # direct: fixed index
        cond = atom.target_condition or 'nearest'
        if cond == 'nearest':
            my = atom.centroid()
            return min(enemies, key=lambda e: math.hypot(my[0]-e.centroid()[0], my[1]-e.centroid()[1]))
        elif cond == 'weakest':
            return min(enemies, key=lambda e: sum(e.cell_troops.values()) if e.cell_troops else 0)
        elif cond.startswith('in_range:'):
            R = float(cond.split(':', 1)[1])
            my = atom.centroid()
            nearest = min(enemies, key=lambda e: math.hypot(my[0]-e.centroid()[0], my[1]-e.centroid()[1]))
            d = math.hypot(my[0]-nearest.centroid()[0], my[1]-nearest.centroid()[1])
            return nearest if d <= R else None                   # hold until in range
        else:
            my = atom.centroid()
            return min(enemies, key=lambda e: math.hypot(my[0]-e.centroid()[0], my[1]-e.centroid()[1]))
    for atom in unit_a.subunits: atom.target_atom = _pick(atom, unit_b.subunits)
    for atom in unit_b.subunits: atom.target_atom = _pick(atom, unit_a.subunits)

# ─── CONTACTS ────────────────────────────────────────────────────────────────

# [canonical: Jordan design — speed-priority cell contention; historical: Crécy/Agincourt timing, Leuctra oblique order, hoplite equal-speed combat resolution]
def resolve_cross_side_contention(unit_a, unit_b):
    """v13: cross-side cell contention — strict speed-differential resolution.

    Historical model (per Jordan design this session, confirmed against precedent):

    The default v11/v12 sim allowed cells from opposing sides to magically
    co-locate at the same abs position (a contact zone where both sides exist
    on the same square). Per Jordan: "if they were to occupy the same cell,
    then the troop with higher speed gets priority for taking up that adjacent
    cell while the other remains in place."

    Historical precedents for the resolution model:

      Crécy and Agincourt (Hundred Years' War): English archers reached their
      defensive positions BEFORE French cavalry could close. The speed
      advantage (defenders pre-positioned, attackers slowed by terrain) meant
      the English took the ground; French had to halt and assault from
      disadvantaged position. Loser of the timing race stays in place.

      Leuctra (Epaminondas's oblique order, classical Greek): the strong left
      wing advanced FASTER than the weakened right. Strong wing reached enemy
      first, hit Spartan elite before Spartan right could engage the
      weakened Theban right. Speed advantage = first-engagement priority.

      Phalanx-meets-phalanx (Greek hoplite era, Roman vs Roman): two
      equally-fast disciplined formations meeting at the contact line.
      Neither side gains ground via movement alone — the push (othismos)
      decides via combat. Resolution-by-movement only fires on CLEAR speed
      differential; equal-speed meetings stay at the magical-co-location
      contact zone where combat resolves the outcome.

    Implementation:

      For each contested abs position (cells from BOTH sides):
        - Skip if both sides have only static cells (stale contention)
        - If a_speed > b_speed: A wins, B loser-cells that moved this turn
          revert to their pre-move snapshot (didn't advance into A's space)
        - If b_speed > a_speed: symmetric
        - Tied speed: NO MOVEMENT-BASED RESOLUTION. Cells stay at contested
          position; combat resolves via find_contacts + engagement damage.
          This is the historically-correct behavior for equal-speed meetings.

      Size and random tiebreakers from Jordan's spec are NOT applied. Per
      historical precedent, equal-speed equal-size meetings don't resolve
      by movement priority — they resolve by combat. Applying random
      tiebreakers per contested position per turn introduces battery noise
      that doesn't model anything historical. Reserved for cavalry charge-
      through cases (where size and morale do matter for penetration depth).

    Charge-through (cavalry past static infantry) and end-of-phase
    displacement: deferred — no cavalry in current battery, and the
    framework is in place to add it via speed/power/facing inputs when
    cavalry units enter the test suite.

    Citation: see preceding canonical comment.
    """
    import mass_battle.hierarchy.units as _u
    if _u.FIELD_MOVEMENT:
        # [Stage A] Co-location is now geometrically impossible on the field path: _node_advance halts
        # every cell at standoff() before it can ever reach an enemy cell's true position, so there is
        # nothing left for this function to resolve. Kept (not deleted) as a documented no-op; the OFF/
        # grid path below is untouched and still does the full speed-priority resolution.
        return 0

    def collect(unit):
        """abs_pos -> [(subunit, orig_coord, contention_speed)]"""
        result = {}
        for su in unit.subunits:
            op = _oriented(su)
            for orig_r, orig_c, or_r, or_c in op:
                ar = (su.starting_position[0] + or_r
                      + su.cell_offsets.get((orig_r, orig_c), 0) * su.advance_dir)
                ac = (su.starting_position[1] + or_c
                      + su.cell_offsets_c.get((orig_r, orig_c), 0))
                if PC_NODE_COHESION and hasattr(su, '_node_pos'):
                    _pr, _pc = su._node_pos.get((orig_r, orig_c), (0.0, 0.0))
                    # [migration H] file-bin the column on ON so the contested-set intersection tests
                    # co-location on the SAME file-cell grid as cells()/find_contacts (the ratified
                    # 'contested grid cell = unit of contested ground' model), not raw-float equality
                    # (which almost never coincides). OFF = verbatim int(round). Toggles at call time.
                    import mass_battle.hierarchy.units as _u
                    ar, ac = (int(round(_pr)), int(round(_pc / _u.COL_WIDTH))) if _u.FIELD_MOVEMENT else (int(round(_pr)), int(round(_pc)))
                # Contention speed: only counts if cell moved this turn
                speed = (su.cell_last_speed.get((orig_r, orig_c), 0)
                         if (orig_r, orig_c) in su._moved_this_turn
                         else 0)
                result.setdefault((ar, ac), []).append((su, (orig_r, orig_c), speed))
        return result

    a_pos = collect(unit_a)
    b_pos = collect(unit_b)
    contested = set(a_pos.keys()) & set(b_pos.keys())
    n_resolved = 0
    for pos in contested:
        a_cells = a_pos[pos]
        b_cells = b_pos[pos]
        # Each side's representative speed is its highest at this position
        a_speed = max(sp for _, _, sp in a_cells)
        b_speed = max(sp for _, _, sp in b_cells)
        # Skip stale contention — neither moved into this position this turn
        if a_speed == 0 and b_speed == 0:
            continue
        # Strict speed differential only. Equal-speed meetings stay co-located
        # (combat resolves via engagement, not movement priority).
        if a_speed > b_speed:
            winner = 'A'
        elif b_speed > a_speed:
            winner = 'B'
        else:
            continue  # tied speed → combat resolves, no movement adjustment
        losers = b_cells if winner == 'A' else a_cells
        for su, oc, _ in losers:
            if oc in su._moved_this_turn:
                # Loser moved this turn → revert to pre-move snapshot.
                # Historical: "the other remains in place" — slower cell
                # didn't actually advance to the contested cell; it stays at
                # the position it held at the start of the turn.
                su.cell_offsets[oc] = su._prev_offsets.get(oc, 0)
                su.cell_offsets_c[oc] = su._prev_offsets_c.get(oc, 0)
                su.cell_facing_vec[oc] = su._prev_facings.get(oc, (su.advance_dir, 0))
                if PC_NODE_COHESION and hasattr(su, '_node_pos'):
                    su._node_pos[oc] = su._node_prev_pos.get(oc, su._node_pos.get(oc, (0.0, 0.0)))
                n_resolved += 1
            # Loser that didn't move: nothing to revert. The mover (winner) is
            # already at this position; both cells now occupy it. This is the
            # cavalry-charge-through case (handled separately when implemented).
    return n_resolved


def find_contacts(unit_a, unit_b):
    # Toggles read at CALL TIME (not import-bound) so a runtime flag flip stays consistent across modules
    # and to avoid a units->contact import cycle. [movement-substrate review 06 — contact cluster]
    import mass_battle.hierarchy.units as _u
    if _u.FIELD_MOVEMENT:
        # [Stage A] The continuous-field halt (_node_advance) now stops cells at standoff() -- not at
        # Chebyshev<=1 -- so contact must fire at the SAME radius, or cells halt at 2-3 lattice units
        # while contact still only fires at <=1 (out of sync). Takes priority over FIELD_CONTACT (a
        # narrower, separate int-round-snap refinement that predates this fix and is untouched here).
        return _find_contacts_standoff(unit_a, unit_b)
    if not _u.FIELD_CONTACT:
        pairs = []
        a_cells = {id(a): set(a.cells()) for a in unit_a.subunits}
        b_cells = {id(b): set(b.cells()) for b in unit_b.subunits}
        for atom_a in unit_a.subunits:
            for atom_b in unit_b.subunits:
                ca = a_cells[id(atom_a)]
                cb = b_cells[id(atom_b)]
                contact_cells_a, contact_cells_b, contact_cols = [], [], set()
                for (ra, c) in ca:
                    for (rb, cb_) in cb:
                        if abs(ra-rb) <= 1 and abs(c-cb_) <= 1:
                            contact_cells_a.append((ra, c))
                            contact_cells_b.append((rb, cb_))
                            contact_cols.add((c + cb_) // 2)
                if contact_cols:
                    pairs.append({"atom_a": atom_a, "atom_b": atom_b,
                                   "a_cells": contact_cells_a, "b_cells": contact_cells_b,
                                   "cols": list(contact_cols)})
        return pairs
    return _find_contacts_field(unit_a, unit_b)


def _cell_radius(atom):
    """Half the max lattice extent of an atom's footprint (min 0.5) — a per-atom contact radius for the
    FIELD_CONTACT centroid bound. [movement-substrate review 06 — contact cluster]"""
    op = _oriented(atom)
    rows = [r for r, c, _o, _p in op]
    cols = [c for r, c, _o, _p in op]
    if not rows:
        return 0.5
    ext = max(max(rows) - min(rows), max(cols) - min(cols)) + 1
    return max(0.5, ext / 2.0)


def _find_contacts_standoff(unit_a, unit_b):
    """[Stage A] FIELD_MOVEMENT ON: contact fires at the same standoff() radius the halt uses, on true
    floats (cells_float(), no snapping) -- so contact and halt never drift out of sync. Returned
    a_cells/b_cells are snapped to the same (rank, file) convention _node_advance/orchestration.py
    already use for halted_cells matching (int(round(r)), int(round(c/COL_WIDTH))) -- only the contact
    PREDICATE is continuous; the reported cell identities stay on the existing snap convention."""
    import mass_battle.hierarchy.units as _u
    pairs = []
    # [v2 Stage B] Each cell is now an oriented unit box (CellBox) grown by its melee reach on the FRONT
    # face; contact fires on obb_front_reach_overlap (the boxed engagement surface) instead of the
    # isotropic circle math.hypot(Δ) <= standoff_from_reach. reach unchanged this stage (reach_for ->
    # REACH_SHORT=0.5); this is a pure CIRCLE->BOX shape swap at unchanged reach. The boxes are built by
    # _u.cell_boxes_for, index-aligned with cells_float() and orientation/reach-identical to the boxes
    # resolve_toi_and_commit halts on (Stage C), so contact and halt share one touch surface exactly.
    af = {id(a): (a.cells_float(), _u.cell_boxes_for(a, _u.reach_for(a.troop_type))) for a in unit_a.subunits}
    bf = {id(b): (b.cells_float(), _u.cell_boxes_for(b, _u.reach_for(b.troop_type))) for b in unit_b.subunits}
    for atom_a in unit_a.subunits:
        fa, boxes_a = af[id(atom_a)]
        for atom_b in unit_b.subunits:
            fb, boxes_b = bf[id(atom_b)]
            # Sets, not lists: the engagement envelope is wide enough that one cell can meet several
            # enemy cells at once, which would otherwise append the SAME snapped identity multiple times
            # -- confirmed by adversarial review to silently over-count stamina drain downstream
            # (orchestration.py sums len(a_cells) directly, uncounted duplicates inflate it). Converted
            # to sorted lists at the end for deterministic output.
            contact_cells_a, contact_cells_b, contact_cols = set(), set(), set()
            for (ar, ac), box_a in zip(fa, boxes_a):
                for (br, bc), box_b in zip(fb, boxes_b):
                    # [v2 Stage B perf reconcile, ED-MB-0011] Cheap bounding-circle reject before the
                    # full SAT: two unit boxes (half-diagonal √2/2 ≈ 0.707) each grown by ≤ reach on the
                    # front face can only engage if their centres are within 2·(0.707 + reach). With the
                    # widest melee reach in play (REACH_SHORT=0.5 this stage) that bound is ≤ ~2.42; 2.6
                    # is a safe, conservative cap. Far pairs (the vast majority) skip the SAT in O(1).
                    # [canonical: geometry — derived bounding-circle reject bound 2·(CELL_RADIUS·√2 + REACH_SHORT) ≈ 2.42; 2.6 = conservative superset, never wrongly skips (perf-only, not a game value)]
                    if (ar - br) * (ar - br) + (ac - bc) * (ac - bc) > 2.6 * 2.6:
                        continue
                    if obb_front_reach_overlap(box_a, box_b):
                        contact_cells_a.add((int(round(ar)), int(round(ac / _u.COL_WIDTH))))
                        contact_cells_b.add((int(round(br)), int(round(bc / _u.COL_WIDTH))))
                        contact_cols.add(round(((ac + bc) / 2.0) / _u.COL_WIDTH))
            if contact_cols:
                pairs.append({"atom_a": atom_a, "atom_b": atom_b,
                               "a_cells": sorted(contact_cells_a), "b_cells": sorted(contact_cells_b),
                               "cols": sorted(contact_cols)})
    return pairs


def _find_contacts_field(unit_a, unit_b):
    """FIELD_CONTACT ON: contact on the promoted floats. Each atom's cells_float() is snapped to int(round())
    here (NOT pre-snapped at cells()), then the SAME append-per-adjacent-pair Chebyshev<=1 loop runs on the
    snapped cells — so the contacting SET reconstruction is identical IN KIND to the OFF path. ca_snap/cb_snap
    are SETS (matching OFF's set(a.cells()) dedup) so round-colliding float cells do not multiply-count.
    At CONTACT_REACH=0.0 this reduces exactly to OFF adjacency. [movement-substrate review 06 — contact cluster]
    NOTE: reach>0 widening of the SET predicate is UNSPECIFIED and pending Jordan; ships reach=0.0 only."""
    import mass_battle.hierarchy.units as _u
    _reach = _u.CONTACT_REACH  # exercised only when a ratified non-zero reach lands; 0.0 => OFF adjacency
    pairs = []
    af = {id(a): a.cells_float() for a in unit_a.subunits}
    bf = {id(b): b.cells_float() for b in unit_b.subunits}
    for atom_a in unit_a.subunits:
        fa = af[id(atom_a)]
        ca_snap = set((int(round(r)), int(round(c))) for (r, c) in fa)
        for atom_b in unit_b.subunits:
            fb = bf[id(atom_b)]
            cb_snap = set((int(round(r)), int(round(c))) for (r, c) in fb)
            contact_cells_a, contact_cells_b, contact_cols = [], [], set()
            for (ra, c) in ca_snap:
                for (rb, cb_) in cb_snap:
                    if abs(ra-rb) <= 1 and abs(c-cb_) <= 1:
                        contact_cells_a.append((ra, c))
                        contact_cells_b.append((rb, cb_))
                        if _u.FIELD_MOVEMENT:
                            contact_cols.add(round(((c + cb_) / 2.0) / _u.COL_WIDTH))  # file index of the meeting column
                        else:
                            contact_cols.add((c + cb_) // 2)
            if contact_cols:
                pairs.append({"atom_a": atom_a, "atom_b": atom_b,
                               "a_cells": contact_cells_a, "b_cells": contact_cells_b,
                               "cols": list(contact_cols)})
    return pairs

def count_engagements_per_atom(pairs):
    counts = {}
    for p in pairs:
        counts[id(p["atom_a"])] = counts.get(id(p["atom_a"]), 0) + 1
        counts[id(p["atom_b"])] = counts.get(id(p["atom_b"]), 0) + 1
    return counts
