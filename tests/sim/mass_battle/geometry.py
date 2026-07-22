"""mass_battle.geometry — cell layout, facing/octagon, support vectors, cell speed.
Behaviour-frozen P-A extract. Depends only on config + stdlib.
NB: explicit __all__ so underscore-prefixed helpers cross `import *`."""
import math
from dataclasses import dataclass
from mass_battle.config import *

__all__ = ['arrowhead_cells', 'line_cells', 'gapped_line_cells', 'column_cells', 'CELL_PATTERN_FN', 'footprint_for', 'oriented_pattern', 'cell_facing', 'octagon_angle', '_support_along_vector', 'atom_max_width', 'cells_to_orig_coords', 'support_engage_frac', '_cell_facing_key', '_rotate_defender_facing', '_init_dynamic_facings', '_atom_avg_facing', 'cell_speed', '_oriented', 'CellBox', 'cellbox_from', 'obb_overlap', 'obb_front_reach_overlap', '_normalize_heading', '_rotate90', '_cellbox_axes', '_cellbox_corners', '_sat_separated']

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
    sizes = {1: (3, 3), 2: (5, 3), 3: (5, 5), 4: (7, 5)}  # [canonical: geometry line_cells tier table (F2 derive-target); §A.3b deployment]
    width, depth = sizes.get(tier, (7, 5))  # [canonical: line_cells default (F2 derive-target)]
    return [(r, c) for r in range(depth) for c in range(width)]


def column_cells(tier):
    # Deep-narrow column = the Line block transposed (its wide rectangle stood on end):
    # narrow frontage, deep files. The depth primitive for depth-vs-width tactics
    # (phalanx / assault column; Leuctra's deep wing).
    # [canonical: Jordan directive 2026-06-03 — depth wins by staying-power/breakthrough;
    #  width's edge is envelopment. A deployable deep-narrow form lets that choice exist.]
    return [(c, r) for (r, c) in line_cells(tier)]

def gapped_line_cells(tier):
    # [canonical: v10 — sized to match Line cell count at each tier so advantage
    #  emerges from arrangement (the gap), not extra troops. Was 56 cells T3, now 24.]
    sizes = {1: (2, 2), 2: (3, 3), 3: (4, 3), 4: (4, 4)}  # [canonical: geometry gapped_line_cells tier table (F2 derive-target); §A.3b]
    half_w, depth = sizes.get(tier, (4, 4))  # [canonical: gapped_line_cells default (F2 derive-target)]
    cells = []
    for r in range(depth):
        for c in range(half_w):
            cells.append((r, c))
        for c in range(half_w + 1, 2 * half_w + 1):
            cells.append((r, c))
    return cells

CELL_PATTERN_FN = {
    # [LC-8, ED-909, Jordan-approved 2026-07-02: "correct, retire them. those are emergent outcomes."]
    # Horseshoe/RefusedFlank are RETIRED here as Subunit-level shapes -- envelopment and refused-flank
    # are now Unit-level, multi-body, emergent compositions (engine.build_envelopment/
    # build_refused_flank), not a single subunit's cell pattern. Only Line/Arrowhead/GappedLine/Column
    # remain valid Subunit.shape values, per ED-909's taxonomy.
    "Line": line_cells, "Arrowhead": arrowhead_cells, "GappedLine": gapped_line_cells,
    "Column": column_cells,
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
def _cells_gapped_line(half_w, depth):
    cells = []
    for r in range(depth):
        cells += [(r, c) for c in range(half_w)]
        cells += [(r, c) for c in range(half_w + 1, 2 * half_w + 1)]
    return cells

# [LC-8] Horseshoe/RefusedFlank retired here too -- see CELL_PATTERN_FN's note.
_SHAPE_BUILD = {
    "Line":         (lambda s: dict(width=max(1, round(LINE_ASPECT * s)), depth=s), _cells_line),
    "Arrowhead":    (lambda s: dict(depth=s),                                       _cells_arrowhead),
    "GappedLine":   (lambda s: dict(half_w=s, depth=s),                             _cells_gapped_line),
    "Column":       (lambda s: dict(width=max(1, round(s)), depth=max(1, round(LINE_ASPECT * LINE_ASPECT * s))), _cells_line),
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
    fmag = max(1e-9, (fr*fr + fc*fc) ** 0.5)  # [canonical: epsilon: float magnitude guard]
    # Vector from defender to attacker
    dr = attacker_pos[0] - defender_pos[0]
    dc = attacker_pos[1] - defender_pos[1]
    amag = max(1e-9, (dr*dr + dc*dc) ** 0.5)  # [canonical: epsilon: float magnitude guard]
    # Cosine of angle between defender facing and direction-to-attacker
    cos_a = (dr * fr + dc * fc) / (amag * fmag)
    cos_a = max(-1.0, min(1.0, cos_a))
    angle_deg = math.degrees(math.acos(cos_a))
    # [canonical: Jordan design — octagon: GREEN<45deg, YELLOW 45-90deg, RED>=90deg]
    # 45.0 = half of GREEN 90deg face; 90.0 = boundary of rear hemisphere
    if angle_deg < 45.0:   return "GREEN",  angle_deg  # [canonical: mass_battle_v30.md §A.3b — 45deg octagon GREEN boundary]
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
    if mag < 1e-9:  # [canonical: epsilon: float magnitude guard]
        return 1.0
    dr /= mag; dc /= mag
    tot = 0.0
    for (fr, fc) in friendly_cells:
        rr = fr - cell[0]; rc = fc - cell[1]
        t = rr * dr + rc * dc            # parallel distance along away-from-attacker dir
        if t < -1e-9:                    # [canonical: epsilon: float projection tolerance] in front of cell (toward attacker): not depth
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

def _oriented_abs_map(atom):
    """{ (abs_r,abs_c): (orig_r,orig_c) } for an atom's live cells — the abs->orig (pattern-identity)
    recovery, built ONCE, FIRST-wins in oriented_pattern order (exactly matching the historical
    break-on-first reverse-lookup). Centralizes the identity round-trip that cells_to_orig_coords /
    _rotate_defender_facing / _atom_avg_facing each open-coded as an O(n^2) scan. Byte-exact (same
    first-match). [movement-substrate review 06 — findings 4/8: this abs->orig reverse-lookup is the hard
    grid dependency; centralizing it is the step toward threading the cell identity from the source.]"""
    # [movement-substrate review 06 — findings 4/8: G] On the coordinate field the atom's live cells come
    # from _node_pos (floats), file-binned as cells()/_node_cells does: (int(round(r)), int(round(c/COL_WIDTH))).
    # The legacy cell_offsets lattice diverges from _node_pos under node cohesion, so amap MUST be keyed from
    # _node_pos on ON or every consumer (cells_to_orig_coords / support_engage_frac / _rotate_defender_facing /
    # _atom_avg_facing / octagon) would look up float cells against integer keys and silently drop them.
    # Toggles read at call time from hierarchy.units (units imports geometry -> no top-level cycle). OFF branch
    # is the verbatim prior cell_offsets build.
    import mass_battle.hierarchy.units as _u
    amap = {}
    if _u.FIELD_MOVEMENT and _u.PC_NODE_COHESION and hasattr(atom, '_node_pos'):
        for orig_r, orig_c, or_r, or_c in oriented_pattern(atom.shape, atom.tier, atom.advance_dir):
            _pr, _pc = atom._node_pos.get((orig_r, orig_c), (0.0, 0.0))
            abs_r = int(round(_pr))
            abs_c = int(round(_pc / _u.COL_WIDTH))
            amap.setdefault((abs_r, abs_c), (orig_r, orig_c))   # FIRST-wins: matches the file-binned cells() keys
        return amap
    for orig_r, orig_c, or_r, or_c in oriented_pattern(atom.shape, atom.tier, atom.advance_dir):
        abs_r = (atom.starting_position[0] + or_r
                 + atom.cell_offsets.get((orig_r, orig_c), 0) * atom.advance_dir)
        abs_c = (atom.starting_position[1] + or_c
                 + atom.cell_offsets_c.get((orig_r, orig_c), 0))
        amap.setdefault((abs_r, abs_c), (orig_r, orig_c))   # FIRST-wins: matches the old break-on-first
    return amap


def cells_to_orig_coords(atom, abs_cells):
    """orig (pattern-identity) coords for each of abs_cells that belongs to this atom, in abs_cells
    order. Byte-exact refactor of the old per-cell reverse scan via the centralized abs->orig map."""
    amap = _oriented_abs_map(atom)
    return [amap[(r, c)] for (r, c) in abs_cells if (r, c) in amap]

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
    amap = _oriented_abs_map(defender_atom)
    for abs_r, abs_c in defender_abs_cells:
        oc = amap.get((abs_r, abs_c))
        if oc is None:
            continue
        orig_r, orig_c = oc
        dr = att_r - abs_r
        dc = att_c - abs_c
        mag = max(1e-9, (dr*dr + dc*dc)**0.5)  # [canonical: epsilon: float magnitude guard]
        dynamic_facings[_cell_facing_key(defender_atom, orig_r, orig_c)] = \
            (round(dr / mag), round(dc / mag))

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
    amap = _oriented_abs_map(atom)
    facings = []
    for abs_r, abs_c in contact_abs_cells:
        oc = amap.get((abs_r, abs_c))
        if oc is None:
            continue
        key = _cell_facing_key(atom, oc[0], oc[1])
        facings.append(dynamic_facings.get(key, cell_facing(atom.advance_dir)))
    if not facings:
        return cell_facing(atom.advance_dir)
    return (sum(f[0] for f in facings) / len(facings),
            sum(f[1] for f in facings) / len(facings))

# ─── PER-CELL SPEED ──────────────────────────────────────────────────────────

def cell_speed(shape, tier, local_r, local_c):
    # [LC-8] Horseshoe/RefusedFlank per-cell speed tables retired along with the shapes themselves
    # (see CELL_PATTERN_FN's note) -- their differential-speed behaviour (wing tips faster than the
    # center; an engaged front rank faster than a refused column) now emerges from the Unit-level
    # build_envelopment/build_refused_flank presets' own timed-order release + per-subunit stance,
    # not a per-cell lookup table keyed to a retired shape name.
    if shape == "Line":    return 1
    if shape == "Column":  return 1
    if shape == "Arrowhead": return 2 if local_r == 0 else 1
    if shape == "GappedLine": return 1
    return 1


def _oriented(su):
    """Oriented base pattern for a subunit, as a list of (orig_r, orig_c, or_r, or_c) tuples.
    Continuous path (su.troops set): footprint_for(shape, troops, concentration). Legacy path
    (troops None): oriented_pattern(shape, tier) — byte-exact. Orientation matches
    oriented_pattern exactly. [Jordan directive — continuous footprint]"""
    troops = getattr(su, 'troops', None)
    if troops is not None:
        pat = footprint_for(su.shape, troops, su.concentration)
        if su.advance_dir == -1:
            return [(r, c, r, c) for r, c in pat]
        max_r = max(r for r, c in pat)
        return [(r, c, max_r - r, c) for r, c in pat]
    return oriented_pattern(su.shape, su.tier, su.advance_dir)


# ─── OBB (ORIENTED BOUNDING BOX) CELL PRIMITIVE ──────────────────────────────
# [spatial-model upgrade, circle->box foundation] Pure, deterministic geometry.
# NOTHING calls this yet -- zero behaviour change to any existing code path.
# Lattice conventions this matches (see hierarchy/units.py): COL_WIDTH = 1.0
# (pitch), CELL_RADIUS = 0.5 (half pitch) -> a body-only CellBox (w=d=1.0,
# reach_front=0) has the same footprint diameter as the legacy circle model.
# Facing is the raw movement vector (dr, dc), not snapped -- see cell_facing/
# octagon_angle above. Positions and extents are floats throughout.

def _normalize_heading(heading):
    """Unit-length (dr, dc). Zero (or near-zero) vector guards to the default
    up-field heading (-1.0, 0.0) -- matches advance_dir=-1 ("up-field")."""
    dr, dc = heading
    mag = math.hypot(dr, dc)
    # [antagonist reconcile, ED-MB-0011 v2 Stage A] Guard non-finite as well as near-zero: a NaN/inf
    # heading would otherwise propagate NaN axes into SAT and silently return garbage overlaps. Out of
    # the intended domain (headings are finite movement vectors) but cheap defense-in-depth on the
    # foundation everything else builds on.
    if not math.isfinite(mag) or mag < 1e-9:  # [canonical: epsilon: float magnitude guard]
        return (-1.0, 0.0)
    return (dr / mag, dc / mag)


def _rotate90(v):
    """Rotate a 2-vector 90 degrees: (x, y) -> (-y, x). Applied to a unit
    heading this yields the box's width axis (perpendicular to depth/facing),
    itself unit-length since rotation preserves magnitude."""
    return (-v[1], v[0])


@dataclass(frozen=True)
class CellBox:
    """Oriented bounding box for one cell. cr,cc = centre (row, col). w = full
    width across the frontage axis (perpendicular to facing); d = full depth
    along the facing axis (front-to-back); standard w=d=1.0 (matches the
    legacy CELL_RADIUS=0.5 circle's footprint). heading = raw (dr, dc) facing
    vector, normalized to unit length in __post_init__ (zero vector -> the
    default (-1.0, 0.0) "up-field" heading -- see _normalize_heading).
    reach_front >= 0 extends the FRONT face only (weapon reach); the back and
    side faces are unaffected, so a box with reach_front > 0 is asymmetric
    front-to-back. Half-extents: d/2 back, d/2 + reach_front front, w/2 each
    side. Local axes: depth axis = heading; width axis = heading rotated 90
    degrees (_rotate90)."""
    cr: float
    cc: float
    w: float = 1.0
    d: float = 1.0
    heading: tuple = (-1.0, 0.0)
    reach_front: float = 0.0

    def __post_init__(self):
        object.__setattr__(self, 'heading', _normalize_heading(self.heading))


def cellbox_from(cr, cc, heading, w=1.0, d=1.0, reach_front=0.0):
    """Convenience constructor mirroring CellBox's fields in a call-site-friendly
    positional order (heading before the sizing kwargs)."""
    return CellBox(cr=cr, cc=cc, w=w, d=d, heading=heading, reach_front=reach_front)


def _cellbox_axes(box):
    """The box's 2 local unit axes (depth, width) as (dr, dc) tuples -- the
    SAT candidate separating axes contributed by this box."""
    dr, dc = box.heading
    return [(dr, dc), _rotate90((dr, dc))]


def _cellbox_corners(box, use_reach):
    """World-space (r, c) corners of the box's rectangle. use_reach=False is
    the pure body (front half-extent = d/2, symmetric with the back); use_reach
    =True extends the front half-extent by reach_front (back/sides unchanged)
    -- this is what makes reach directional: it only pushes the FRONT corners
    forward along heading, never the back corners."""
    dr, dc = box.heading
    wr, wc = _rotate90((dr, dc))
    half_back = box.d / 2.0
    half_front = box.d / 2.0 + (box.reach_front if use_reach else 0.0)
    half_w = box.w / 2.0
    return [
        (box.cr - half_back * dr + half_w * wr, box.cc - half_back * dc + half_w * wc),
        (box.cr - half_back * dr - half_w * wr, box.cc - half_back * dc - half_w * wc),
        (box.cr + half_front * dr + half_w * wr, box.cc + half_front * dc + half_w * wc),
        (box.cr + half_front * dr - half_w * wr, box.cc + half_front * dc - half_w * wc),
    ]


def _sat_separated(corners_a, corners_b, axis):
    """True iff `axis` is a separating axis for the two corner sets (SAT):
    their projections onto `axis` touch-or-don't-overlap. Strict overlap only
    -- touching exactly (interval boundaries equal) counts as separated, so
    two unit boxes at centre-distance exactly 1.0 do NOT overlap (documented
    boundary; matches the legacy circle test's strict `<`)."""
    ar, ac = axis
    proj_a = [p[0] * ar + p[1] * ac for p in corners_a]
    proj_b = [p[0] * ar + p[1] * ac for p in corners_b]
    min_a, max_a = min(proj_a), max(proj_a)
    min_b, max_b = min(proj_b), max(proj_b)
    return max_a <= min_b or max_b <= min_a


def _sat_overlap(corners_a, axes_a, corners_b, axes_b):
    """Core SAT test over two corner sets and their combined candidate axes
    (2 per box == 4 total for two rectangles -- sufficient since each box is
    a rectangle, even the front-reach-extended asymmetric one: it is still a
    quadrilateral with two pairs of parallel faces, so its face normals are
    still exactly its depth/width axes). Overlap iff NO candidate axis
    separates the two corner sets."""
    for axis in axes_a:
        if _sat_separated(corners_a, corners_b, axis):
            return False
    for axis in axes_b:
        if _sat_separated(corners_a, corners_b, axis):
            return False
    return True


def obb_overlap(a, b):
    """Pure body-vs-body OBB overlap (Separating Axis Theorem, 2D): project
    both boxes onto each box's 2 local axes (depth, width) -- 4 candidate
    separating axes total -- and overlap iff none of them separates the
    boxes. `reach_front` is ignored on both sides (ADR: use
    obb_front_reach_overlap for the reach-aware engagement test). Symmetric
    (obb_overlap(a,b) == obb_overlap(b,a)), translation-invariant, and
    rotation-consistent by construction (SAT is a geometric fact about the
    two shapes, independent of which box's axes are listed first)."""
    corners_a = _cellbox_corners(a, use_reach=False)
    corners_b = _cellbox_corners(b, use_reach=False)
    return _sat_overlap(corners_a, _cellbox_axes(a), corners_b, _cellbox_axes(b))


def obb_front_reach_overlap(a, b):
    """Reach-aware engagement test: True iff EITHER box's reach-extended body
    meets the OTHER box's plain body -- a's reach reaching b's body, OR b's
    reach reaching a's body (a longer weapon reaches first; contact fires if
    either side can reach the other). Reach is directional: `reach_front`
    only extends a box's FRONT face along ITS OWN heading (see
    _cellbox_corners), so a target directly ahead of a reaching box can be
    engaged within reach_front even with no body overlap, while the identical
    target placed directly BEHIND that box at the same distance is not
    (reach never extends the back face). reach_front=0 on both sides makes
    both extended corner sets identical to the plain-body corner sets, so
    this collapses exactly to obb_overlap(a, b). Symmetric by construction
    (both directions are checked explicitly)."""
    a_ext = _cellbox_corners(a, use_reach=True)
    b_body = _cellbox_corners(b, use_reach=False)
    if _sat_overlap(a_ext, _cellbox_axes(a), b_body, _cellbox_axes(b)):
        return True
    b_ext = _cellbox_corners(b, use_reach=True)
    a_body = _cellbox_corners(a, use_reach=False)
    return _sat_overlap(b_ext, _cellbox_axes(b), a_body, _cellbox_axes(a))
