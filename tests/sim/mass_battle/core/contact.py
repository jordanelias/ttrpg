"""mass_battle.core.contact — targeting + contact detection (the contact-event layer).
Stage-1 behaviour-frozen extract from orchestration.py (assign_targets, resolve_cross_side_contention,
find_contacts, count_engagements_per_atom). Depends on geometry (_oriented/octagon/facing) + config +
math + duck-typed unit/atom methods; no up-DAG import (no cycle). Re-imported by orchestration via
star-import so resolve_engagements/run_battle and every caller are unchanged.
[canonical: mass_battle_v30.md §A.7 manoeuvre/contact]"""
import math
from mass_battle.config import *
from mass_battle.geometry import *

__all__ = ['assign_targets', 'resolve_cross_side_contention', 'find_contacts', 'count_engagements_per_atom']


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
