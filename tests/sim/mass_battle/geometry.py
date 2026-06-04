"""mass_battle.geometry — cell layout, facing/octagon, support vectors, cell speed.
Behaviour-frozen P-A extract. Depends only on config + stdlib.
NB: explicit __all__ so underscore-prefixed helpers cross `import *`."""
import math
from mass_battle.config import *

__all__ = ['arrowhead_cells', 'line_cells', 'horseshoe_cells', 'gapped_line_cells', 'refused_flank_cells', 'CELL_PATTERN_FN', 'footprint_for', 'oriented_pattern', 'cell_facing', 'octagon_angle', '_support_along_vector', 'atom_max_width', 'cells_to_orig_coords', 'support_engage_frac', '_cell_facing_key', '_rotate_defender_facing', '_init_dynamic_facings', '_atom_avg_facing', 'cell_speed']

def arrowhead_cells(tier):
    cells = []
    for r in range(tier + 2):
        width = 2 * r + 1
        center_col = tier + 1
        start = center_col - r
        for c in range(start, start + width):
            cells.append((r, c))
    return cells

def line_cells(tier):
    sizes = {1: (3, 3), 2: (5, 3), 3: (5, 5), 4: (7, 5)}
    width, depth = sizes.get(tier, (7, 5))
    return [(r, c) for r in range(depth) for c in range(width)]

def horseshoe_cells(tier):
    sizes = {1: (2, 2), 2: (2, 3), 3: (3, 3), 4: (3, 4)}
    wing_w, depth = sizes.get(tier, (3, 4))
    full_width = wing_w * 2 + 1
    cells = []
    for r in range(depth):
        for c in range(wing_w):
            cells.append((r, c))
        for c in range(wing_w + 1, full_width):
            cells.append((r, c))
    for c in range(full_width):
        cells.append((depth, c))
    return cells

def gapped_line_cells(tier):
    # [canonical: v10 — sized to match Line cell count at each tier so advantage
    #  emerges from arrangement (the gap), not extra troops. Was 56 cells T3, now 24.]
    sizes = {1: (2, 2), 2: (3, 3), 3: (4, 3), 4: (4, 4)}
    half_w, depth = sizes.get(tier, (4, 4))
    cells = []
    for r in range(depth):
        for c in range(half_w):
            cells.append((r, c))
        for c in range(half_w + 1, 2 * half_w + 1):
            cells.append((r, c))
    return cells

def refused_flank_cells(tier):
    # [canonical: v10 — sized to match Line cell count at each tier. Engaging-side
    #  block is (width-1) × depth, plus 1 cell at front of refused column.
    #  The refused side withdraws troops from contact (geometric concentration on engaging side),
    #  not from total. Was 21 cells T3, now 25.]
    sizes = {1: (3, 4), 2: (4, 5), 3: (5, 6), 4: (6, 7)}
    width, depth = sizes.get(tier, (6, 7))
    cells = []
    for r in range(depth):
        for c in range(width - 1):
            cells.append((r, c))
    # One forward cell in the refused column at the front row
    cells.append((depth, width - 1))
    return cells

CELL_PATTERN_FN = {
    "Line": line_cells, "Arrowhead": arrowhead_cells,
    "Horseshoe": horseshoe_cells, "GappedLine": gapped_line_cells,
    "RefusedFlank": refused_flank_cells,
}

# ─── CONTINUOUS-SCALE FOOTPRINT GENERATOR (Jordan directive 2026-06-03) ───
# Dimension-parametric cell builders (the tier *_cells fns above stay for the legacy path).
# footprint_for lays a continuous troop count into a shape at a user-set concentration,
# bounded so per-cell troops stay in [CELL_FLOOR, CELL_CAP]; achievable density is the closest
# the shape's discrete geometry allows within that bound.
def _cells_line(width, depth):
    return [(r, c) for r in range(depth) for c in range(width)]
def _cells_arrowhead(depth):
    cells = []
    for r in range(depth):
        w = 2 * r + 1; start = (depth - 1) - r
        cells += [(r, c) for c in range(start, start + w)]
    return cells
def _cells_horseshoe(wing_w, depth):
    full = wing_w * 2 + 1; cells = []
    for r in range(depth):
        cells += [(r, c) for c in range(wing_w)]
        cells += [(r, c) for c in range(wing_w + 1, full)]
    cells += [(depth, c) for c in range(full)]
    return cells
def _cells_gapped_line(half_w, depth):
    cells = []
    for r in range(depth):
        cells += [(r, c) for c in range(half_w)]
        cells += [(r, c) for c in range(half_w + 1, 2 * half_w + 1)]
    return cells
def _cells_refused_flank(width, depth):
    cells = [(r, c) for r in range(depth) for c in range(width - 1)]
    cells.append((depth, width - 1))
    return cells

_SHAPE_BUILD = {
    "Line":         (lambda s: dict(width=max(1, round(LINE_ASPECT * s)), depth=s), _cells_line),
    "Arrowhead":    (lambda s: dict(depth=s),                                       _cells_arrowhead),
    "Horseshoe":    (lambda s: dict(wing_w=s, depth=s),                             _cells_horseshoe),
    "GappedLine":   (lambda s: dict(half_w=s, depth=s),                             _cells_gapped_line),
    "RefusedFlank": (lambda s: dict(width=s, depth=s),                              _cells_refused_flank),
}

def footprint_for(shape, troops, concentration):
    """Lay `troops` into `shape` at ~`concentration` troops/cell, bounded so per-cell stays
    in [CELL_FLOOR, CELL_CAP]; returns the cell-set [(r,c), ...]. Achievable density is the
    closest the shape's discrete geometry allows within the bound."""
    troops = max(1, int(troops))
    lo = math.ceil(troops / CELL_CAP)
    hi = max(lo, troops // CELL_FLOOR)
    target = min(hi, max(lo, round(troops / max(1.0, float(concentration)))))
    mk, build = _SHAPE_BUILD[shape]
    max_s = max(2, math.isqrt(hi) + 2)
    best = None
    for s in range(1, max_s + 1):
        n = len(build(**mk(s)))
        if lo <= n <= hi and (best is None or abs(n - target) < abs(best[1] - target)):
            best = (s, n)
    if best is None:                                  # granularity skipped [lo,hi]; nearest overall
        for s in range(1, max_s + 1):
            n = len(build(**mk(s)))
            if best is None or abs(n - target) < abs(best[1] - target): best = (s, n)
    s, n = best
    return build(**mk(s))

def oriented_pattern(shape, tier, advance_dir):
    pattern = CELL_PATTERN_FN[shape](tier)
    if advance_dir == -1:
        return [(r, c, r, c) for r, c in pattern]
    max_r = max(r for r, c in pattern)
    return [(r, c, max_r - r, c) for r, c in pattern]

def cell_facing(advance_dir):
    # [canonical: v11 — legacy centroid facing, kept for fallback only]
    return (advance_dir, 0)

# v11: Per-cell octagon angle model
# [canonical: Jordan design — octagon, 2 GREEN faces = 90°, 2 YELLOW = 45°+45°, 4 RED = 180°]
# Facing = raw movement vector per cell (not snapped). Octagon rotates to facing direction.
# Angle between attack vector and defender facing:
#   GREEN  |diff| < 45°  → 0 modifier   (attacker in defender's front arc)
#   YELLOW 45° ≤ |diff| < 90° → -1D     (attacker at defender's flank)
#   RED    |diff| ≥ 90° → -2D           (attacker in defender's rear 180°)

def octagon_angle(attacker_pos, defender_pos, defender_facing_vec):
    """
    Compute octagon zone (GREEN/YELLOW/RED) for an attack on defender.
    defender_facing_vec: raw (dr, dc) movement vector of the defender cell.
    Returns zone string and angle in degrees.
    """
    fr, fc = defender_facing_vec
    fmag = max(1e-9, (fr*fr + fc*fc) ** 0.5)
    # Vector from defender to attacker
    dr = attacker_pos[0] - defender_pos[0]
    dc = attacker_pos[1] - defender_pos[1]
    amag = max(1e-9, (dr*dr + dc*dc) ** 0.5)
    # Cosine of angle between defender facing and direction-to-attacker
    cos_a = (dr * fr + dc * fc) / (amag * fmag)
    cos_a = max(-1.0, min(1.0, cos_a))
    angle_deg = math.degrees(math.acos(cos_a))
    # [canonical: Jordan design — octagon: GREEN<45deg, YELLOW 45-90deg, RED>=90deg]
    # 45.0 = half of GREEN 90deg face; 90.0 = boundary of rear hemisphere
    if angle_deg < 45.0:   return "GREEN",  angle_deg
    if angle_deg < 90.0:   return "YELLOW", angle_deg  # [canonical: designs/provincial/mass_battle_v30.md §octagon]
    return "RED", angle_deg


def _support_along_vector(cell, attacker_pos, friendly_cells):
    """Supporting depth behind `cell` measured PARALLEL to the attacker's approach
    vector, with partial-cell weighting.

    Two geometric corrections over the old Y-column depth (`_depth_by_col`):
      (1) Depth is counted along the push direction d = normalize(cell - attacker_pos),
          NOT the formation's Y-column. A frontal hit therefore counts the file (Y),
          a flank hit counts the row (X), a diagonal hit counts along the diagonal.
          A cell hit along X no longer gets backed up by the cell behind it in Y.
      (2) Each friendly cell counts by how much the 1-wide attack lane cuts through it:
          weight = max(0, 1 - perp), where perp is the cell's perpendicular distance
          from the lane axis. A cardinal lane counts only the exact line (perp 0 -> 1,
          perp 1 -> 0); a diagonal lane counts on-lane cells fully and clipped cells
          partially -- so we don't over-count cells barely in the path.

    Only cells at or behind `cell` along d (t >= 0, i.e. away from the attacker) count
    as supporting depth. Returns >= 1.0 (the cell itself, perp 0, contributes 1).
    """
    dr = cell[0] - attacker_pos[0]
    dc = cell[1] - attacker_pos[1]
    mag = (dr * dr + dc * dc) ** 0.5
    if mag < 1e-9:
        return 1.0
    dr /= mag; dc /= mag
    tot = 0.0
    for (fr, fc) in friendly_cells:
        rr = fr - cell[0]; rc = fc - cell[1]
        t = rr * dr + rc * dc            # parallel distance along away-from-attacker dir
        if t < -1e-9:                    # in front of cell (toward attacker): not depth
            continue
        pr = rr - t * dr; pc = rc - t * dc
        perp = (pr * pr + pc * pc) ** 0.5
        w = 1.0 - perp
        if w > 0.0:
            tot += w
    return tot if tot > 0.0 else 1.0


def atom_max_width(shape, tier):
    pattern = CELL_PATTERN_FN[shape](tier)
    by_row = {}
    for r, c in pattern:
        by_row.setdefault(r, []).append(c)
    return max(len(v) for v in by_row.values())

# ─── F-i: CELL SUPPORT STACKING ──────────────────────────────────────────────

def cells_to_orig_coords(atom, abs_cells):
    op = oriented_pattern(atom.shape, atom.tier, atom.advance_dir)
    orig_coords = []
    for abs_r, abs_c in abs_cells:
        for orig_r, orig_c, or_r, or_c in op:
            comp_r = (atom.starting_position[0] + or_r
                      + atom.cell_offsets.get((orig_r, orig_c), 0) * atom.advance_dir)
            comp_c = (atom.starting_position[1] + or_c
                      + atom.cell_offsets_c.get((orig_r, orig_c), 0))
            if (comp_r, comp_c) == (abs_r, abs_c):
                orig_coords.append((orig_r, orig_c))
                break
    return orig_coords

def support_engage_frac(atom, contact_abs_cells):
    """F-i: support-stack-adjusted engage_frac.
    Cells behind the contact zone contribute weighted support.
    [canonical: Jordan handoff §(1)]"""
    max_w = atom_max_width(atom.shape, atom.tier)
    if not SUPPORT_STACK_ENABLED:
        return len(set(contact_abs_cells)) / max_w

    pattern = CELL_PATTERN_FN[atom.shape](atom.tier)
    contact_orig = cells_to_orig_coords(atom, set(contact_abs_cells))

    if not contact_orig:
        return len(set(contact_abs_cells)) / max_w

    contact_orig_set = set(contact_orig)
    front_r = min(r for r, c in contact_orig)

    supporter_total = 0.0
    for orig_r, orig_c in pattern:
        if (orig_r, orig_c) in contact_orig_set:
            continue
        if orig_r <= front_r:
            continue
        depth = orig_r - front_r
        w = SUPPORT_WEIGHTS.get(depth, SUPPORT_WEIGHT_FLOOR)
        supporter_total += w

    effective_engaged = len(contact_orig) + supporter_total
    return min(1.0, effective_engaged / max_w)

# ─── F-iii: FACING HELPERS ───────────────────────────────────────────────────

def _cell_facing_key(atom, orig_r, orig_c):
    return (id(atom), orig_r, orig_c)

def _rotate_defender_facing(defender_atom, defender_abs_cells, attacker_abs_cells,
                             dynamic_facings):
    """Rotate engaged defender cells toward attacker (Rule A: full pivot).
    [canonical: Jordan handoff §(3a)]"""
    if not attacker_abs_cells or not defender_abs_cells:
        return
    att_r = sum(c[0] for c in attacker_abs_cells) / len(attacker_abs_cells)
    att_c = sum(c[1] for c in attacker_abs_cells) / len(attacker_abs_cells)
    op = oriented_pattern(defender_atom.shape, defender_atom.tier, defender_atom.advance_dir)
    for abs_r, abs_c in defender_abs_cells:
        for orig_r, orig_c, or_r, or_c in op:
            comp_r = (defender_atom.starting_position[0] + or_r
                      + defender_atom.cell_offsets.get((orig_r, orig_c), 0) * defender_atom.advance_dir)
            comp_c = (defender_atom.starting_position[1] + or_c
                      + defender_atom.cell_offsets_c.get((orig_r, orig_c), 0))
            if (comp_r, comp_c) == (abs_r, abs_c):
                dr = att_r - abs_r
                dc = att_c - abs_c
                mag = max(1e-9, (dr*dr + dc*dc)**0.5)
                dynamic_facings[_cell_facing_key(defender_atom, orig_r, orig_c)] = \
                    (round(dr / mag), round(dc / mag))
                break

def _init_dynamic_facings(unit_a, unit_b):
    df = {}
    for u in [unit_a, unit_b]:
        for atom in u.subunits:
            op = oriented_pattern(atom.shape, atom.tier, atom.advance_dir)
            for orig_r, orig_c, _, _ in op:
                df[_cell_facing_key(atom, orig_r, orig_c)] = cell_facing(atom.advance_dir)
    return df

def _atom_avg_facing(atom, contact_abs_cells, dynamic_facings):
    """Compute average facing for an atom's contact cells from dynamic_facings."""
    op = oriented_pattern(atom.shape, atom.tier, atom.advance_dir)
    facings = []
    for abs_r, abs_c in contact_abs_cells:
        for orig_r, orig_c, or_r, or_c in op:
            comp_r = (atom.starting_position[0] + or_r
                      + atom.cell_offsets.get((orig_r, orig_c), 0) * atom.advance_dir)
            comp_c = (atom.starting_position[1] + or_c
                      + atom.cell_offsets_c.get((orig_r, orig_c), 0))
            if (comp_r, comp_c) == (abs_r, abs_c):
                key = _cell_facing_key(atom, orig_r, orig_c)
                facings.append(dynamic_facings.get(key, cell_facing(atom.advance_dir)))
                break
    if not facings:
        return cell_facing(atom.advance_dir)
    return (sum(f[0] for f in facings) / len(facings),
            sum(f[1] for f in facings) / len(facings))

# ─── PER-CELL SPEED ──────────────────────────────────────────────────────────

def cell_speed(shape, tier, local_r, local_c):
    if shape == "Line":    return 1
    if shape == "Arrowhead": return 2 if local_r == 0 else 1
    if shape == "Horseshoe":
        sizes = {1: 2, 2: 2, 3: 3, 4: 3}
        wing_w = sizes.get(tier, 3)
        depth_sizes = {1: 2, 2: 3, 3: 3, 4: 4}
        depth = depth_sizes.get(tier, 4)
        if local_r == depth:    return 0
        elif local_c != wing_w: return 2
        return 1
    if shape == "GappedLine": return 1
    if shape == "RefusedFlank":
        sizes = {1: 3, 2: 4, 3: 5, 4: 6}
        width = sizes.get(tier, 6)
        # v12: front row of engaged side at speed 2 (oblique-order charge).
        # The "phalanx push" was led by the front rank at battle pace, with
        # deeper ranks following at marching pace. Whole-column speed 2 over-tunes
        # vs Line (H6); front-2-rows still over-tunes; front-row-only is the
        # partial momentum bonus that helps against wide formations (HS) without
        # dominating same-width opposition (Line).
        # Refused cell at width-1 holds at speed 0.
        # [canonical: references/historical/precedents_warfare.md — Leuctra 371 BC,
        #  Theban front rank advanced at battle pace; depth followed]
        if local_c == width - 1: return 0
        if local_r == 0: return 2
        return 1
    return 1

