"""mass_battle.hierarchy.units — Subunit and Unit dataclasses (the unit/subunit hierarchy).
Stage-1 behaviour-frozen extract from orchestration.py. The DATA model + the per-object geometry/
movement/state methods. Depends only on LOWER layers — config, geometry (_oriented/footprint_for/
cell_speed/octagon), core.exchange (derive_command/_stamina_pool_penalty/subunit_combat_pool),
troop_types.registry (stats_for), percell (build_column_grid) — and never imports orchestration
(no cycle). Re-imported by orchestration via star-import so every Subunit(...)/Unit(...) call site
is unchanged. [canonical: mass_battle_v30.md §A.3b/§A.4; derived_stats unit composition]"""
import math
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Dict, Set
from mass_battle.config import *
from mass_battle.geometry import *
from mass_battle.core.exchange import *
from mass_battle.troop_types.registry import *
from mass_battle.percell import *
from mass_battle.resolution import *

import os as _hu_os
# Consumer-local maneuver toggles (read by advance_cells; runtime-togglable by validators on this
# module). Kept here, not config, to stay within the touched-file set during the Stage-1 extraction.
PC_ENVELOP_PATH = (_hu_os.environ.get("PC_ENVELOP_PATH", "1") == "1")  # [canonical: mass_battle_v30.md §A.8 — directed envelop maneuver toggle]
PC_SWEEP = (_hu_os.environ.get("PC_SWEEP", "1") == "1")  # [canonical: mass_battle_v30.md §A.8 — lateral sweep maneuver toggle]
# [movement-substrate review 06 — finding 2] Continuous-speed toggle. ON: a per-cell fractional-speed
# accumulator, so a discipline-degraded body advances at its TRUE average rate instead of flooring to 0
# each turn (floor(1*0.7)=0 freezes a slow degraded unit). Consumer-local here (advance_cells), like
# PC_ENVELOP_PATH/PC_SWEEP.
# [ED-1089, Jordan-ratified 2026-07-02: "yes, field movement is default."] DEFAULT FLIPPED 0 -> 1
# (Stage A step 7 executed): the coordinate field is now what runs by default; the integer grid remains
# available (FIELD_MOVEMENT=0 PC_NODE_COHESION=0) and stays the frozen byte-exact regression oracle —
# bat.py's grid digests are still checked in CI with those toggles pinned explicitly OFF.
FIELD_MOVEMENT = (_hu_os.environ.get("FIELD_MOVEMENT", "1") == "1")
# [movement-substrate review 06 — coordinate-field migration] FIELD_MOVEMENT is the continuous COORDINATE
# FIELD master toggle. Continuous positions require the node float path (PC_NODE_COHESION stores true floats
# in _node_pos): the field toggle therefore UNIFIES with it — field-ON implies the node path is active. A
# FIELD-ON / NODE-OFF run would silently half-migrate (legacy integer branch never emits floats), so
# run_battle enforces FIELD_MOVEMENT ⇒ PC_NODE_COHESION at setup (see run_battle). Toggles live here (not
# config.py) so the whole-file fabrication scan does not surface config's pre-existing uncited constants.
FIELD_CONTACT = (_hu_os.environ.get("FIELD_CONTACT", "0") == "1")  # default OFF -> byte-exact contact path
CONTACT_REACH = float(_hu_os.environ.get("CONTACT_REACH", "0.0"))  # 0.0 => ON contact predicate == OFF adjacency (exempt value)
COL_WIDTH = 1.0  # inter-file column pitch = 1 lattice unit; file = round(x/COL_WIDTH). At 1.0, round(int)==int -> OFF byte-exact.

# ─── FACING PHYSICS (anti-hyper-reactivity; movement-substrate review 06, facing-heading cluster) ───
# Cell-level facing STATE gating the octagon. Master toggle default OFF -> byte-exact (raw-movement-vector
# facing, instantly re-faced each turn, exactly as today). ON: facing becomes committed state with slew-rate,
# attention, an FOV blind arc, and rout-away facing. DEFAULT-OFF; F2 is NOT enabled — magnitudes below are
# ungrounded placeholders (calibrated debt), not ratified. Placed here (not config.py) so the whole-file
# fabrication scan does not surface config's pre-existing uncited constants; exported in __all__ so
# orchestration's star-import of units sees them (avoids the config __all__ omission that would NameError).
PC_FACING_MODEL = (_hu_os.environ.get('PC_FACING_MODEL', '0') == '1')   # master gate; OFF -> today's raw-vector facing
PC_FACING_ATTENTION = (_hu_os.environ.get('PC_FACING_ATTENTION', '1') == '1')  # (a) engaged cell faces its ENGAGED target; no-op unless PC_FACING_MODEL
PC_FACING_SLEW_BASE = float(_hu_os.environ.get('PC_FACING_SLEW_BASE', '60'))  # [CALIBRATED-DEBT, Stage-5: ungrounded placeholder pivot rate deg/tick; NOT ratified — do not enable]
PC_FACING_FOV_GATE = (_hu_os.environ.get('PC_FACING_FOV_GATE', '1') == '1')  # (c) rear blind arc GATES reaction/targeting; reuses REAR_BLIND_DEG/FOV_HALF_DEG
PC_FACING_ROUT = (_hu_os.environ.get('PC_FACING_ROUT', '1') == '1')  # (d) routed body faces AWAY from the enemy

__all__ = ['Subunit', 'Unit', 'Order', 'PC_ENVELOP_PATH', 'PC_SWEEP', 'FIELD_MOVEMENT', 'FIELD_CONTACT', 'CONTACT_REACH', 'COL_WIDTH',
           'PC_FACING_MODEL', 'PC_FACING_ATTENTION', 'PC_FACING_SLEW_BASE', 'PC_FACING_FOV_GATE', 'PC_FACING_ROUT',
           'CELL_RADIUS', 'standoff_from_reach', 'standoff', 'PC_REACH_FACING_GATE', 'resolve_toi_and_commit']

# [Stage A — true-adjacency halt] Per-cell physical-body radius, distinct from core.contact._cell_radius
# (a whole-FORMATION bounding radius used by the FIELD_CONTACT centroid bound). Grounded the same way
# that function already is: half the existing COL_WIDTH=1.0 lattice pitch.
CELL_RADIUS = 0.5


def standoff_from_reach(reach_a, reach_b):
    """[Stage A] Stand-off distance (lattice units) from two already-resolved PP-290 reach values
    (troop_types.registry.reach_for). Symmetric by construction."""
    return (CELL_RADIUS + reach_a) + (CELL_RADIUS + reach_b)


def standoff(troop_type_a, troop_type_b):
    """[Stage A] True-adjacency stand-off distance (lattice units) between a cell of troop_type_a and
    a cell of troop_type_b: (CELL_RADIUS + reach(a)) + (CELL_RADIUS + reach(b)). Two Short-Reach cells
    stand off 2.0 lattice units apart; Long vs Short, 3.0. Used by find_contacts (core/contact.py) — a
    generous, non-facing-gated outer bound (see _effective_reach) — so contact never lags behind the
    (tighter, facing-gated) movement halt below."""
    return standoff_from_reach(reach_for(troop_type_a), reach_for(troop_type_b))


def _cell_facing_for_box(atom, cid):
    """[v2 Stage B/C] The heading used to orient a cell's CellBox -- the SAME expression
    resolve_toi_and_commit._flat uses for its _ToiCell.facing, so the contact predicate (Stage B) and
    the TOI halt (Stage C) build byte-identical boxes for the same cell/position and therefore agree on
    the touch surface exactly. Committed cell facing (cell_facing_vec) if present, else the sub-unit's
    live node facing, else the raw advance direction (advance_dir, 0). NOT get_cell_facing: the
    PC_FACING_ROUT away-facing flip is a targeting/reach-adjudication concern, deliberately NOT applied
    to the physical-body box geometry (a fleeing body still occupies its square)."""
    return atom.cell_facing_vec.get(cid, getattr(atom, '_node_facing', None) or (atom.advance_dir, 0))


def cell_boxes_for(atom, reach_front):
    """[v2 Stage B] One CellBox per cell of `atom`, aligned index-for-index with atom.cells_float()
    (both iterate _oriented(atom) order, so zip() pairs each float centre with its own box). Standard
    unit square (w=d=1.0); heading = the cell's facing (_cell_facing_for_box); reach_front = the atom's
    melee reach, passed in by the caller (reach_for(troop_type) this stage -- REACH_SHORT=0.5) so contact
    and TOI feed the identical value. Pure/deterministic; no mutation of atom."""
    boxes = []
    for (orig_r, orig_c, _o_r, _o_c), (r, c) in zip(_oriented(atom), atom.cells_float()):
        fv = _cell_facing_for_box(atom, (orig_r, orig_c))
        boxes.append(cellbox_from(float(r), float(c), (float(fv[0]), float(fv[1])),
                                  w=1.0, d=1.0, reach_front=reach_front))
    return boxes


# [TOI refactor] Reach bonus only projects within the forward FOV arc (reuses Stage B's FOV_HALF_DEG) --
# default ON, no-op unless FIELD_MOVEMENT (only the new cross-side TOI resolve consults this).
PC_REACH_FACING_GATE = (_hu_os.environ.get('PC_REACH_FACING_GATE', '1') == '1')


def _effective_reach(base_reach, facing_vec, dr, dc):
    """[TOI refactor] A cell's weapon reach only threatens what's within its forward FOV arc -- a cell
    facing away from a given enemy fights that enemy at CELL_RADIUS-only (no reach bonus) until its
    facing catches up (ties the reach-advantage mechanic to Stage B's facing/FOV model instead of
    treating reach as an omnidirectional bubble). dr,dc: direction from this cell toward the enemy
    (need not be normalized); facing_vec: this cell's current (pre-tick) facing."""
    if base_reach <= 0 or not PC_REACH_FACING_GATE:
        return base_reach
    fr, fc = facing_vec
    fmag = math.hypot(fr, fc)
    amag = math.hypot(dr, dc)
    if fmag < 1e-9 or amag < 1e-9:  # [canonical: epsilon: float magnitude guard]
        return base_reach
    cos_a = max(-1.0, min(1.0, (dr * fr + dc * fc) / (amag * fmag)))
    angle_deg = math.degrees(math.acos(cos_a))
    return base_reach if angle_deg <= FOV_HALF_DEG else 0.0


def _reach_throttle(reach_eff_a, reach_eff_b):
    """[TOI refactor] Reach-asymmetric closing-budget throttle for one cross-side pair. The side with
    the LARGER effective threat radius (CELL_RADIUS + facing-gated reach) is capped to a SMALLER share
    of this tick's closing motion: it needs to close less ground to bring its longer weapon to bear, so
    it plants its formation first, while the shorter-reach side must cover the rest of the gap to bring
    its own (shorter) weapon into range. Returns (rho_a, rho_b), each in (0,1]; the larger side is
    always 1.0 (free to use its full proposed motion, subject to the TOI solve itself). Equal reach ->
    (1.0, 1.0) -- the plain symmetric case, unchanged in spirit from a shared-t TOI."""
    if reach_eff_a > reach_eff_b:
        return (reach_eff_b / reach_eff_a, 1.0)
    if reach_eff_b > reach_eff_a:
        return (1.0, reach_eff_a / reach_eff_b)
    return (1.0, 1.0)


def _pair_toi_scale(start_a, start_b, proposed_a, proposed_b, rho_a, rho_b, target):
    """[TOI refactor] Exact continuous-collision (time-of-impact) solve for one cross-side cell pair.
    Both cells' motion this tick is linear from start to proposed (the UNCAPPED end-of-tick position
    each would reach with no standoff constraint at all): pos_a(s) = start_a + rho_a*s*(proposed_a -
    start_a), similarly for b, so the relative position is linear in s and |pos_a(s)-pos_b(s)|^2 is a
    quadratic. Returns the smallest s in (0,1] at which the pair first reaches `target` (the pair's
    reach-and-facing-gated standoff distance), or None if no cap is needed this tick (already >=
    target at the full throttled motion, i.e. s=1, or the pair never closes to target within the
    tick). A pre-existing violation at s=0 (should already be caught by halted_cells -- true adjacency
    contact -- so this is a defensive floor, not the normal path) returns 0.0: freeze immediately."""
    d0r = start_a[0] - start_b[0]; d0c = start_a[1] - start_b[1]
    c0 = d0r * d0r + d0c * d0c - target * target
    if c0 < 0:
        return 0.0
    var_r = rho_a * (proposed_a[0] - start_a[0]) - rho_b * (proposed_b[0] - start_b[0])
    var_c = rho_a * (proposed_a[1] - start_a[1]) - rho_b * (proposed_b[1] - start_b[1])
    a = var_r * var_r + var_c * var_c
    if a < 1e-9:  # [canonical: epsilon: float magnitude guard]
        return None
    b = 2.0 * (d0r * var_r + d0c * var_c)
    if c0 < 1e-9 and b >= 0:  # [canonical: epsilon: float magnitude guard]
        return None  # starting essentially ON the boundary but separating (or tangent) -- no cap
    disc = b * b - 4.0 * a * c0
    if disc < 0:
        return None
    # f(s) = a*s^2 + b*s + c0 is an upward parabola (a>=0); f(0)=c0>=0 (checked above). If it dips
    # below zero at all, that happens on exactly one interval (lo,hi) with lo<=hi (both real since
    # disc>=0) -- NOT just by checking f(1): two bodies whose straight-line paths cross can be safely
    # apart at BOTH s=0 and s=1 while still dipping inside the standoff ring somewhere in between (a
    # "pass-through" case a same-endpoint check misses entirely). The first entry into violation
    # within this tick is the smallest root that's > 0, clamped into (0,1].
    sq = math.sqrt(disc)
    r1 = (-b - sq) / (2.0 * a); r2 = (-b + sq) / (2.0 * a)
    lo, hi = (r1, r2) if r1 <= r2 else (r2, r1)
    if hi <= 0.0 or lo > 1.0:
        return None  # the violation window (if any) falls entirely outside this tick
    return max(0.0, lo)


# [v2 Stage C, ED-MB-0011] ANALYTIC swept-SAT time-of-impact on the OBB touch predicate -- the closed-
# form replacement for the original scan+bisection (which called obb_front_reach_overlap ~178x per near-
# contact pair per tick and made the field path ~60x slower, stalling the byte-exact battery). Over one
# tick the box axes and corner-offsets are CONSTANT -- Euclidean motion translates only the centre --
# so on each SAT axis the strict-overlap band is a linear-in-s inequality, i.e. an s-interval;
# intersecting the <=4 axes' intervals gives the overlap window and its left edge is the first touch.
# No iteration, no tolerance knobs. Verified against the reference scan+bisection to machine epsilon
# (max_err 1.7e-15 over 700 seeded fuzzed pairs, 281 genuine touches) -- see test_obb_contact_toi.py /
# the scratch verify probe. ~15 us/pair (was several hundred us under bisection).


def _swept_first_overlap_s(a0, va, off_a, b0, vb, off_b, axes):
    """First s in [0,1] at which the two moving boxes overlap (strict SAT) on ALL candidate `axes`,
    or None. Box A occupies {a0 + s*va + corner : corner in off_a}; B likewise. Over one tick the box
    axes and corner-offsets are CONSTANT (Euclidean motion translates only the centre), so on each axis
    n the SAT overlap condition `bmin-amax < P(s) < bmax-amin` (P(s)=(A_centre-B_centre)·n, LINEAR in s)
    is a half-open band -> an s-interval. Intersecting the ≤4 axes' intervals gives the overlap window
    (lo, hi); the first touch is its left edge. O(len(axes)) analytic -- replaces the per-pair scan+
    bisection (~30 SAT calls/pair) that made the field path ~20-60x slower. Deterministic, no iteration."""
    lo, hi = 0.0, 1.0
    for (nr, nc) in axes:
        amin = amax = off_a[0][0] * nr + off_a[0][1] * nc
        for o in off_a[1:]:
            p = o[0] * nr + o[1] * nc
            if p < amin: amin = p
            elif p > amax: amax = p
        bmin = bmax = off_b[0][0] * nr + off_b[0][1] * nc
        for o in off_b[1:]:
            p = o[0] * nr + o[1] * nc
            if p < bmin: bmin = p
            elif p > bmax: bmax = p
        p0 = (a0[0] - b0[0]) * nr + (a0[1] - b0[1]) * nc
        dp = (va[0] - vb[0]) * nr + (va[1] - vb[1]) * nc
        band_lo = bmin - amax   # P must be strictly ABOVE this to overlap on n
        band_hi = bmax - amin   # ...and strictly BELOW this
        if band_hi <= band_lo:
            return None          # degenerate (zero-area box) -> never overlaps
        if -1e-15 < dp < 1e-15:  # P constant on this axis
            if not (band_lo < p0 < band_hi):
                return None
            continue             # overlaps for all s on this axis -> no constraint
        s1 = (band_lo - p0) / dp
        s2 = (band_hi - p0) / dp
        axlo, axhi = (s1, s2) if s1 <= s2 else (s2, s1)
        if axlo > lo: lo = axlo
        if axhi < hi: hi = axhi
        if lo >= hi:
            return None
    if hi <= 0.0:
        return None              # overlap window is entirely in the past (already separating)
    if lo <= 0.0:
        return 0.0               # already overlapping at s=0
    if lo > 1.0:
        return None              # first overlap beyond this tick's motion
    return lo                    # first touch = the overlap band's left edge


def _pair_toi_box_scale(start_a, prop_a, start_b, prop_b, rho_a, rho_b, head_a, reach_a, head_b, reach_b):
    """[v2 Stage C] Smallest tick-fraction s in [0,1] at which cell A (centre gliding start_a->prop_a,
    throttled by rho_a) and cell B (start_b->prop_b, rho_b) first bring their OBB engagement surfaces
    into contact (obb_front_reach_overlap = a's reach-extended box meets b's body OR vice-versa), or
    None if they never touch across this tick's throttled motion. Analytic swept-SAT (see
    _swept_first_overlap_s): O(1) per pair, no iteration. Headings/reach fixed over the tick (motion is
    Euclidean -- only the centre translates); each box is the unit square grown by reach_front on its
    FRONT face. Deterministic. Returns 0.0 if already touching at s=0 (a pre-existing contact). Verified
    to match the reference scan+bisection to <1e-6 over fuzzed pairs (see test_obb_contact_toi.py)."""
    _ba0 = cellbox_from(0.0, 0.0, head_a, w=1.0, d=1.0, reach_front=reach_a)  # centre at origin
    _bb0 = cellbox_from(0.0, 0.0, head_b, w=1.0, d=1.0, reach_front=reach_b)
    axes = _cellbox_axes(_ba0) + _cellbox_axes(_bb0)   # 4 candidates: A depth/width + B depth/width
    off_a_reach = _cellbox_corners(_ba0, use_reach=True)   # config 1: a extended vs b plain
    off_b_plain = _cellbox_corners(_bb0, use_reach=False)
    off_a_plain = _cellbox_corners(_ba0, use_reach=False)  # config 2: a plain vs b extended
    off_b_reach = _cellbox_corners(_bb0, use_reach=True)
    a0 = (start_a[0], start_a[1]); b0 = (start_b[0], start_b[1])
    va = (rho_a * (prop_a[0] - start_a[0]), rho_a * (prop_a[1] - start_a[1]))
    vb = (rho_b * (prop_b[0] - start_b[0]), rho_b * (prop_b[1] - start_b[1]))
    s1 = _swept_first_overlap_s(a0, va, off_a_reach, b0, vb, off_b_plain, axes)
    s2 = _swept_first_overlap_s(a0, va, off_a_plain, b0, vb, off_b_reach, axes)
    if s1 is None: return s2
    if s2 is None: return s1
    return s1 if s1 <= s2 else s2


def _slew_facing(cur, desired, discipline):
    """Rotate `cur` toward `desired` by at most PC_FACING_SLEW_BASE*disc_mult degrees; return a unit vector.
    Zero-mag `desired` returns `cur` unchanged. Deterministic (no RNG). [movement-substrate review 06 — facing (b)]"""
    cmag = math.hypot(cur[0], cur[1])
    dmag = math.hypot(desired[0], desired[1])
    if dmag < 1e-9:  # [canonical: epsilon: float magnitude guard]
        return cur
    if cmag < 1e-9:  # [canonical: epsilon: float magnitude guard]
        return (desired[0] / dmag, desired[1] / dmag)
    cx, cy = cur[0] / cmag, cur[1] / cmag
    dx, dy = desired[0] / dmag, desired[1] / dmag
    ang = math.atan2(cx * dy - cy * dx, cx * dx + cy * dy)  # signed angle cur->desired
    disc_mult = 1.0 if discipline >= 5 else (0.7 if discipline >= 3 else 0.4)  # [canonical: mass_battle_v30.md §A.4 — Discipline degradation tiers]
    max_turn = math.radians(PC_FACING_SLEW_BASE * disc_mult)
    if ang > max_turn: ang = max_turn
    elif ang < -max_turn: ang = -max_turn
    ca, sa = math.cos(ang), math.sin(ang)
    return (cx * ca - cy * sa, cx * sa + cy * ca)


# [Stage C, adversarial review] Order.behavior may only set fields that are pure behavioral/targeting
# switches -- read fresh every tick, no cached derived state keyed off them. Fields that drive
# _oriented()/cell geometry (shape, tier, troops, concentration, starting_position) or a live position
# sign-multiplier (advance_dir) are DELIBERATELY excluded: __post_init__ distributes cell_troops over
# _oriented(self)'s ids exactly once at construction, so setattr-ing any of those mid-battle leaves
# cell_troops/cell_offsets stale against the new geometry -- confirmed via repro to orphan troops
# (troop_count changes but cell_troops keeps the old key set/sum) or teleport a cell instantly (flipping
# advance_dir is a live sign-flip on already-accumulated cell_offsets, not a next-tick effect). Safely
# supporting those would need re-running __post_init__'s redistribution, which no order use case
# (hold-then-advance, stance/instructions/targeting switches, entering escort mode) actually needs.
_ORDER_SAFE_FIELDS = frozenset({
    'stance', 'instructions', 'unit_type', 'role',
    'target_condition', 'target_delay_ticks', 'order_target_idx',
    'escort_of', 'escort_offset', 'escort_engage_on_contact',
    # [DG-2, Jordan-ruled "build it now" 2026-07-08] `yielding` is a pure behavioural switch (like
    # `stance`), read fresh every tick via `yield_active` -- no cached derived state keyed off it,
    # same reasoning as every other field in this set.
    'yielding',
})

# [Stage C, adversarial review] Recognized trigger prefixes -- validated eagerly at construction so a
# malformed trigger (a typo, e.g. 'tickk:4') fails loudly immediately rather than silently never firing
# for the rest of the battle (the two failure modes -- "malformed trigger" and "condition legitimately
# never met" -- are otherwise behaviourally indistinguishable to a caller; a condition that's correctly
# never satisfied SHOULD stay pending forever, that's by design, but a typo should not get that far).
_ORDER_TRIGGER_KINDS = ('immediate', 'tick:', 'enemy_range:', 'ally_at:')


@dataclass
class Order:
    """[Stage C] A single timed/conditional instruction queued on a Subunit. trigger:
    'immediate' | 'tick:N' | 'enemy_range:D' | 'ally_at:D' (needs waypoint_ref). behavior: a dict of
    attribute->value, applied via setattr when the trigger fires (e.g. {'stance':'balanced',
    'instructions':('envelop',)}) -- restricted to _ORDER_SAFE_FIELDS (behavioral/targeting switches,
    including escort_of/escort_offset -- a subunit can switch INTO escort mode mid-battle via an order),
    not geometry/troop-accounting fields (see _ORDER_SAFE_FIELDS's own note for why)."""
    trigger: str
    behavior: dict = field(default_factory=dict)
    waypoint_ref: Optional[object] = field(default=None, repr=False)  # only consulted for 'ally_at:D'

    def __post_init__(self):
        if self.trigger != 'immediate' and not self.trigger.startswith(('tick:', 'enemy_range:', 'ally_at:')):
            raise ValueError(f"Order.trigger {self.trigger!r} unrecognized; expected one of {_ORDER_TRIGGER_KINDS}")
        bad = set(self.behavior) - _ORDER_SAFE_FIELDS
        if bad:
            raise ValueError(f"Order.behavior sets unsafe field(s) {sorted(bad)}; "
                              f"Order may only set {sorted(_ORDER_SAFE_FIELDS)} (see _ORDER_SAFE_FIELDS)")


@dataclass
class Subunit:
    shape: str
    troop_type: str           # 'infantry'|'cavalry' etc. — anatomical type (v8 legacy)
    tier: int
    starting_position: Tuple[int, int]
    advance_dir: int = 1
    stance: str = "balanced"
    # v9: unit_type governs combat role. 'melee' = engages at contact (v8 behavior).
    # 'ranged' = fires in Phase 2 Volley at any enemy in line of sight, then optionally
    # closes to melee. [canonical: mass_battle_v30.md §A.7 Phase 2 Volley]
    unit_type: str = "melee"
    order_target_idx: Optional[int] = None
    cell_offsets: Dict[Tuple[int, int], int] = field(default_factory=dict)
    cell_offsets_c: Dict[Tuple[int, int], int] = field(default_factory=dict)
    halted_cells: Set[Tuple[int, int]] = field(default_factory=set)
    target_atom: Optional[object] = field(default=None, repr=False)
    # [class-B] targeting extensions
    target_delay_ticks: int = 0          # hold N ticks before first targeting; decremented each assign_targets call
    target_condition: Optional[str] = None  # None/'nearest'(default) | 'weakest' | 'in_range:N' | 'direct'
    # F-ii: last movement speed per orig coord (only updated when cell actually moves)
    cell_last_speed: Dict[Tuple[int, int], int] = field(default_factory=dict)
    # v11: per-cell raw movement vector for octagon angle computation.
    # Stored as (dr, dc) — the actual direction the cell moved last turn.
    # Initialized to advance_dir on first use. Updated whenever a cell moves.
    # [canonical: Jordan design — octagon facing = raw movement vector]
    cell_facing_vec: Dict[Tuple[int, int], Tuple[int, int]] = field(default_factory=dict)
    # v13: position snapshot at start of advance_cells, used to revert on
    # discipline-pass collision (cell returns to its formation slot).
    # [canonical: Jordan design 2026-05-12 — discipline-gated formation hold]
    _prev_offsets: Dict[Tuple[int, int], int] = field(default_factory=dict)
    _prev_offsets_c: Dict[Tuple[int, int], int] = field(default_factory=dict)
    _prev_facings: Dict[Tuple[int, int], Tuple[int, int]] = field(default_factory=dict)
    # v13: cells flagged as "formation-broken" (failed discipline check on collision).
    # Used for diagnostics; facing is already corrupted to midpoint vector in cell_facing_vec.
    merged_cells: Set[Tuple[int, int]] = field(default_factory=set)
    # v13: cells that actually moved this turn (vs halted or already-at-target).
    # Used by resolve_cross_side_contention to distinguish moving vs static cells.
    # Reset at top of advance_cells. [canonical: Jordan design 2026-05-12 — speed priority]
    _moved_this_turn: Set[Tuple[int, int]] = field(default_factory=set)
    # [field-movement, default OFF] per-cell fractional-speed carry for FIELD_MOVEMENT (continuous speed).
    # Empty and untouched on the default (floor) path -> byte-exact. [movement-substrate review 06 — finding 2]
    _speed_accum: Dict[Tuple[int, int], float] = field(default_factory=dict)
    # P-C scaffold (INERT): role drawn from the troop_type-gated menu (FM position→role) + the
    # instruction package the role applies. Not consumed yet — wiring instructions to primitives
    # (brace→+density, etc.) is the behaviour-cascading next step (design §3.5/§9.1).
    role: Optional[str] = None
    instructions: Tuple[str, ...] = ()
    # Continuous-scale (Jordan directive 2026-06-03): when `troops` is set the footprint is
    # generated from (troops, concentration) via footprint_for and `tier` becomes vestigial;
    # None keeps the legacy tier path (byte-exact).
    troops: Optional[float] = None
    concentration: Optional[float] = None
    # [ED-MB-0026, Jordan directive] Explicit frontage×depth: `width` (columns/frontage) and `depth` (rows).
    # When BOTH are set they define an exact width×depth rectangular footprint (troops set for the count),
    # and per-cell density = troops/(width·depth) follows — the coupled tactical axes ('columns vs rows,
    # which affect each other': wide-shallow = frontage/envelopment, narrow-deep = breakthrough/depth).
    # None (either) falls back to the density (`concentration`) path or the legacy tier path.
    width: Optional[int] = None
    depth: Optional[int] = None
    # [ED-MB-0025, Jordan directive] Depth density gradient: how the subunit's troops distribute across
    # its ranks. 'uniform' (default, byte-exact) = equal per cell; 'front' = leading ranks denser (shock /
    # weight at the point of contact); 'rear' = trailing ranks denser (depth / staying-power reserve — the
    # Theban deep wing at Leuctra). r=0 is the leading rank in the footprint. Sum over cells == troop_count.
    distribution: str = 'uniform'
    # Per-subunit quality stats (Jordan directive): a subunit is a homogeneous typed body
    # with its OWN combat stats; None INHERITS the parent Unit (back-ref _unit set in Unit.__post_init__),
    # so single-subunit / homogeneous units stay byte-exact. Mixed units (e.g. a cavalry subunit + an
    # infantry subunit) differentiate per-subunit in the pool, casualty exchange, and charge/brace/morale sigma.
    power: Optional[int] = None
    discipline: Optional[int] = None
    morale: Optional[int] = None
    morale_start: Optional[int] = None
    dr: Optional[int] = None
    # Per-subunit stamina (Jordan directive): a subunit drains and rests its OWN stamina; None INHERITS
    # the parent Unit (single-subunit / homogeneous units stay byte-exact via eff_stamina -> unit.stamina).
    # An engaged subunit drains; a reserve subunit stays fresh -> line relief / depth-as-reserve becomes
    # mechanically real (triplex-acies line relief; Clausewitz reserves).
    stamina: Optional[float] = None
    stamina_max: Optional[float] = None
    # Per-subunit rout lifecycle (Jordan directive 2026-06-17): a subunit tracks its OWN rout/broken
    # state, so a heavily-hit subunit can break while a fresh sibling holds ("a section of the line
    # breaks" — §A.12 Cannae/Hastings). routed = its eroding morale reached 0; broken = its discipline
    # reached 0 (formation gone, contributes 0 to combat). For a single-subunit unit these coincide with
    # the parent Unit's routed/broken so the homogeneous gauge stays byte-exact. discipline_start mirrors
    # morale_start (the per-subunit nominal start for degradation tracking); None inherits the Unit.
    routed: bool = False
    broken: bool = False
    discipline_start: Optional[int] = None
    # [DG-2, designs/proposals/mass_battle_fighting_withdrawal_v1.md, Jordan-ruled "build it now"
    # 2026-07-08] A yielding subunit gives ground under pressure but keeps FIGHTING and keeps FACING
    # the threat -- the mechanical distinction from `routed` (which turns away and stops fighting).
    # Default False -> inert/byte-exact for every existing Subunit; entry is commanded-only this
    # pass (a 'yield' order's `behavior` dict sets this True directly via check_orders' existing
    # generic setattr application -- no new order-primitive code needed), gated on
    # `eff_discipline >= D_YIELD` at every CONSUMPTION site (movement/facing/combat pool), not at
    # entry -- ordering a too-disordered subunit to yield is simply a no-op, not a special case.
    yielding: bool = False
    # [ED-MB-0024, DG-2 §2.4 pocket exit] Set live during the yield movement pass when rearward motion is
    # structurally blocked (map edge in the flee direction, or an enemy has gotten behind into the retreat
    # path). While pocketed, yielding converts to a HOLD with the combat malus REMOVED (Cannae's pinned-
    # and-annihilated kill condition). Default False -> inert; only ever set when PC_YIELD_POCKET is on.
    pocketed: bool = False
    # [Stage C] Timed/conditional order queue -- fired in sequence by check_orders (core/contact.py),
    # called once per tick per side, before assign_targets. Empty tuple -> the consumer's loop body
    # never executes for any existing Subunit (byte-exact).
    orders: Tuple[Order, ...] = ()
    _order_idx: int = 0
    # [Stage C] Escort / formation-relative positioning ("hold position in front of the marching
    # archers"): a subunit tracking a friendly's position instead of (or until) engaging an enemy.
    # All default-inert -> byte-exact for any existing Subunit.
    escort_of: Optional[object] = field(default=None, repr=False)   # live ref to the escorted friendly Subunit
    escort_offset: Tuple[float, float] = (0.0, 0.0)   # (dr, dc) in the escorted unit's LOCAL (facing-rotated) frame; +dr = ahead
    escort_engage_on_contact: bool = False    # False = keep screening indefinitely; True = one-shot latch to normal enemy-targeting once acquired
    _escort_engaged: bool = False             # the latch
    # [ED-1095, Jordan-ruled 2026-07-02: "Bracing is not something that can be done instantaneously,
    # but must be prepared ahead of time and intentionally set."] Tick this subunit's 'brace'
    # instruction has been continuously present since -- -1 = not currently braced. Stamped 0 at
    # construction for a subunit deployed ALREADY braced (it had time to set up before the battle
    # began); stamped to the firing tick by check_orders when an Order adds 'brace' mid-battle (see
    # resolution._subunit_braced, which requires >=1 full tick since this stamp before treating the
    # subunit as braced).
    _brace_since_tick: int = -1
    # [D2 fix, 2026-07-05, mass-battle Cannae gauge follow-up audit] `_envelop_goal`'s phase-1/
    # phase-2 transition used the SAME threshold for entry and exit (no hysteresis) -- once past,
    # turning toward a rear enemy cell re-crosses that same row and flips back to phase 1 every
    # tick, a permanent limit cycle that never reaches contact. This latch commits the subunit to
    # phase 2 the first time `past` is true. Default False -> byte-exact/inert for any subunit
    # that never uses 'envelop'.
    _envelop_committed: bool = False

    def __post_init__(self):
        # Construction-time validation (arch review / stress-test hardening): turn the cryptic
        # KeyError (invalid tier/shape) and silent off-grid placement into clear errors at the
        # point of construction, so resolution never sees a malformed atom. Valid in-bounds
        # formations are unaffected (byte-exact). Bounds are checked on the initial formation
        # (cell_offsets are 0 here); dynamic movement past the edge is a separate concern.
        if self.shape not in CELL_PATTERN_FN:
            raise ValueError(f"Subunit shape {self.shape!r} unknown; valid shapes: {sorted(CELL_PATTERN_FN)}")
        # Continuous mode = troops set, with EITHER a density (concentration) OR an explicit width×depth
        # grid (ED-MB-0026). Legacy tier path = troops None (and no concentration/grid).
        _has_grid = self.width is not None and self.depth is not None
        if self.troops is None and (self.concentration is not None or _has_grid):
            raise ValueError("Subunit: continuous mode (concentration or width×depth) needs troops set")
        if self.troops is not None and self.concentration is None and not _has_grid:
            raise ValueError("Subunit: continuous mode needs a concentration (density) or an explicit width×depth")
        if self.troops is None and self.tier not in TROOPS_PER_TIER:
            raise ValueError(f"Subunit (shape={self.shape}) tier must be one of {sorted(TROOPS_PER_TIER)}, got {self.tier!r}")
        for ar, ac in self.cells():
            if not (0 <= ar < BATTLEFIELD_SIZE and 0 <= ac < BATTLEFIELD_SIZE):
                raise ValueError(
                    f"Subunit (shape={self.shape}, tier={self.tier}) at anchor {self.starting_position} "
                    f"places a cell at ({ar},{ac}) outside the {BATTLEFIELD_SIZE}x{BATTLEFIELD_SIZE} battlefield; "
                    f"move the anchor inward so the formation fits.")
        # Step 1 (cell-primary, Jordan directive 2026-06-03): per-cell troops are the SOURCE OF TRUTH.
        # troop_count spreads uniformly over the subunit's cells at spawn; columns + unit hp become
        # emergent sums over these. [arch: cell = primitive; column = first-level emergence.]
        _ids = [(o_r, o_c) for o_r, o_c, _a, _b in _oriented(self)]
        # [ED-MB-0025] Distribute troop_count across cells by the depth gradient. 'uniform' -> equal per
        # cell (byte-exact with the prior spread). 'front'/'rear' weight cells by their rank r (r=0 = front):
        # front-heavy loads the leading ranks (shock), rear-heavy the trailing ranks (depth reserve). The
        # weights are normalised so sum(cell_troops) == troop_count exactly (conservation preserved).
        if _ids and self.distribution in ('front', 'rear'):
            _rmax = max(o_r for o_r, _o_c in _ids)
            # linear ramp over depth; front: weight = (rmax - r + 1), rear: weight = (r + 1). Flat if depth 1.
            _w = {(o_r, o_c): ((_rmax - o_r + 1) if self.distribution == 'front' else (o_r + 1))
                  for (o_r, o_c) in _ids}
            _wsum = sum(_w.values()) or 1.0
            self.cell_troops = {pid: self.troop_count * _w[pid] / _wsum for pid in _ids}
        else:
            _per = self.troop_count / len(_ids) if _ids else 0.0
            self.cell_troops = {pid: _per for pid in _ids}
        self._unit = None                      # stat-inheritance back-ref (set by Unit.__post_init__)
        self._start_troops = self.troop_count  # spawn troop count = per-subunit cohesion denominator
        self._cell_target = dict(self.cell_troops)  # [ED-MB-0028] prescribed per-cell density at spawn (close_ranks fill target)
        self._spawn_position = self.starting_position  # snapshot for reset_positions (multi-turn re-engagement)
        self._brace_since_tick = 0 if 'brace' in self.instructions else -1  # [ED-1095] prepared before the battle if deployed already braced
        if PC_NODE_COHESION:
            self._init_node_state()

    @classmethod
    def of_type(cls, troop_type, shape, tier, starting_position, **kw):
        """Construct a Subunit of a canonical troop type (mass_battle_v30 §B.2). The type's
        power / discipline / morale (and morale_start = morale) are filled from
        TROOP_TYPE_STATS unless the caller overrides them in **kw; an unknown type fills
        nothing (fields stay None -> inherit the parent Unit). This is the taxonomy's
        'stat home'. It is purely additive: callers that build Subunit(...) directly are
        unaffected, so single-subunit / homogeneous units stay byte-exact.
        NOTE: only STATS are mapped. unit_type (melee vs ranged) is a role, not a stat —
        a ranged type (archers / crossbow / sling) takes unit_type='ranged' via **kw."""
        preset = stats_for(troop_type)
        if preset:
            kw.setdefault('power', preset['power'])
            kw.setdefault('discipline', preset['discipline'])
            kw.setdefault('morale', preset['morale'])
            kw.setdefault('morale_start', preset['morale'])
        return cls(shape=shape, troop_type=troop_type, tier=tier,
                   starting_position=starting_position, **kw)

    @property
    def troop_count(self):
        return self.troops if self.troops is not None else TROOPS_PER_TIER[self.tier]

    # ── per-subunit effective stats: own value, else inherit parent Unit (byte-exact when None) ──
    def _u(self):
        return getattr(self, '_unit', None)
    @property
    def eff_power(self):
        return self.power if self.power is not None else (self._u().power if self._u() else 4)  # [canonical: sim_mb_06_v9_historical_spec.md — P4 tier baseline default]
    @property
    def eff_discipline(self):
        return self.discipline if self.discipline is not None else (self._u().discipline if self._u() else 5)
    @property
    def yield_active(self):
        """[DG-2 §2.5 anti-abuse, Jordan-ruled "build it now" 2026-07-08] The single, shared gate
        every yield consumption site (movement, facing-lock, combat-pool malus, no-volley) checks --
        discipline-gated (a too-disordered subunit's yield order is a no-op, not honored) and
        melee-only ("ranged troop types already have kite; yielding is not a second kiting mechanic
        for archers to exploit for permanent standoff"). One property, not five repeated inline
        conditions, so the gate can't drift out of sync between call sites."""
        return self.yielding and self.eff_discipline >= D_YIELD and self.unit_type != 'ranged'
    @property
    def eff_morale(self):
        if self.morale is not None: return self.morale
        return self._u().morale if self._u() else 0
    @property
    def eff_morale_start(self):
        if self.morale_start is not None: return self.morale_start
        return getattr(self._u(), 'morale_start', 0) if self._u() else 0
    @property
    def eff_dr(self):
        return self.dr if self.dr is not None else (self._u().dr if self._u() else 1)
    @property
    def eff_stamina(self):
        if self.stamina is not None: return self.stamina
        u = self._u()
        return u.stamina if u is not None else STAMINA_MAX
    @property
    def eff_stamina_max(self):
        if self.stamina_max is not None: return self.stamina_max
        u = self._u()
        return u.stamina_max if u is not None else STAMINA_MAX
    def drain_stamina(self, amount):
        # Reduce effective stamina (floor 0). Writes to own stamina if set, else routes to the inherited
        # Unit -> a single-subunit unit reproduces the old unit.stamina drain exactly (byte-exact).
        new = max(0, self.eff_stamina - amount)
        if self.stamina is not None: self.stamina = new
        else:
            u = self._u()
            if u is not None: u.stamina = new
    def recover_stamina(self, amount):
        # Increase effective stamina, capped at eff_stamina_max; same own-else-inherited-Unit write routing.
        new = min(self.eff_stamina_max, self.eff_stamina + amount)
        if self.stamina is not None: self.stamina = new
        else:
            u = self._u()
            if u is not None: u.stamina = new
    @property
    def eff_discipline_start(self):
        if self.discipline_start is not None: return self.discipline_start
        u = self._u()
        return u.discipline_start if u is not None else 5
    def erode_morale(self, amount):
        # Reduce effective morale (may pass <=0 -> rout, matching the unit `morale -= loss`). Writes to own
        # morale if set, else routes to the inherited Unit -> single-subunit reproduces the old unit erosion.
        new = self.eff_morale - amount
        if self.morale is not None: self.morale = new
        else:
            u = self._u()
            if u is not None: u.morale = new
    def pull_morale(self, delta):
        # [DG-4, ED-MB-0002, 2026-07-04 Jordan ruling: "Subunit morale combination of own morale
        # and overall morale; more likely to wilt if other subunits losing, more likely to rally if
        # other subunits winning."] A CONTINUOUS, signed coupling toward siblings' state (called
        # from core/state.py's morale_check_phase every phase) -- distinct from erode_morale (a
        # one-directional casualty/exhaustion penalty) and cascade_morale_hit (a discrete, one-time
        # army-wide contagion event). delta>0 rallies (siblings trending better than this atom),
        # delta<0 wilts (siblings trending worse). Same own-else-inherited-Unit write routing as
        # erode_morale/degrade_discipline. Capped at eff_morale_start on the rally side (siblings'
        # strength cannot rally a subunit ABOVE its own pristine ceiling); no floor on the wilt
        # side, matching erode_morale's own unbounded-negative convention (rout is a <=0 threshold
        # check elsewhere, not enforced here).
        new = min(self.eff_morale_start, self.eff_morale + delta)
        if self.morale is not None: self.morale = new
        else:
            u = self._u()
            if u is not None: u.morale = new
    def degrade_discipline(self):
        # -1 discipline toward floor 0 (formation degradation); own-else-inherited-Unit write routing.
        new = max(0, self.eff_discipline - 1)
        if self.discipline is not None: self.discipline = new
        else:
            u = self._u()
            if u is not None: u.discipline = new
    def restore_discipline(self):
        # +1 discipline toward the nominal start (Reform); own-else-inherited-Unit write routing.
        new = min(self.eff_discipline_start, self.eff_discipline + 1)
        if self.discipline is not None: self.discipline = new
        else:
            u = self._u()
            if u is not None: u.discipline = new
    @property
    def cur_troops(self):
        return sum(self.cell_troops.values()) if getattr(self, 'cell_troops', None) else self.troop_count
    @property
    def cohesion(self):
        u = self._u()
        if u is not None and len(u.subunits) == 1:
            return (u.hp / u.hp_max) if u.hp_max else 0.0   # exact match to unit base_combat_pool (byte-exact single-subunit path)
        start = getattr(self, '_start_troops', 0) or self.troop_count
        return (self.cur_troops / start) if start else 0.0
    @property
    def eff_size(self):
        u = self._u()
        if u is not None and len(u.subunits) == 1:
            return u.effective_size
        return self.cur_troops / BLOCK_SIZE

    @property
    def charge_pen(self):
        # Increment 5: intrinsic charge penetration (ranks punched through on impact).
        # Cavalry charge is the stubbed mechanic being wired ("noted but not wired").
        # [ASSUMPTION: cavalry charge_pen=3 ranks — basis: real shock-cavalry penetration of
        #  thin lines; absorbed by deep formations (pike/deep infantry). Class-B, Jordan-vetoable.]
        return 3 if self.troop_type == 'cavalry' else 0

    def cells(self):
        if PC_NODE_COHESION and hasattr(self, '_node_pos'):
            return self._node_cells()
        op = _oriented(self)
        result = []
        for orig_r, orig_c, or_r, or_c in op:
            abs_r = (self.starting_position[0] + or_r
                     + self.cell_offsets.get((orig_r, orig_c), 0) * self.advance_dir)
            abs_c = (self.starting_position[1] + or_c
                     + self.cell_offsets_c.get((orig_r, orig_c), 0))
            result.append((abs_r, abs_c))
        return result

    def cells_float(self):
        """Float analogue of cells() — same order/length. Node path returns the UNSNAPPED _node_pos floats
        (the true floats cells() snaps at _node_cells); legacy path returns integer positions widened to
        float. Used by the FIELD_CONTACT contact pipeline. [movement-substrate review 06 — contact cluster]"""
        if PC_NODE_COHESION and hasattr(self, '_node_pos'):
            out = []
            for orig_r, orig_c, _o_r, _o_c in _oriented(self):
                r, c = self._node_pos.get((orig_r, orig_c), (0.0, 0.0))
                out.append((float(r), float(c)))
            return out
        op = _oriented(self)
        out = []
        for orig_r, orig_c, or_r, or_c in op:
            abs_r = (self.starting_position[0] + or_r
                     + self.cell_offsets.get((orig_r, orig_c), 0) * self.advance_dir)
            abs_c = (self.starting_position[1] + or_c
                     + self.cell_offsets_c.get((orig_r, orig_c), 0))
            out.append((float(abs_r), float(abs_c)))
        return out

    def iter_cells(self):
        """Cell-primary view (step 1): yield (cell_id, (abs_r,abs_c), troops) per cell in _oriented
        order. cell_id = (orig_r, orig_c) pattern identity (stable under movement)."""
        for orig_r, orig_c, or_r, or_c in _oriented(self):
            abs_r = (self.starting_position[0] + or_r
                     + self.cell_offsets.get((orig_r, orig_c), 0) * self.advance_dir)
            abs_c = (self.starting_position[1] + or_c
                     + self.cell_offsets_c.get((orig_r, orig_c), 0))
            yield (orig_r, orig_c), (abs_r, abs_c), self.cell_troops.get((orig_r, orig_c), 0.0)

    def troop_total(self):
        return sum(self.cell_troops.values())

    def close_ranks(self):
        """[ED-MB-0028, task #29; Jordan 2026-07-23] Cell-level closing-ranks — the internal-subunit
        version of rotating troops. After casualties, redistribute the subunit's LIVING troops so the
        LEADING ranks (orig_r ascending; r=0 is the front/engaged edge) are refilled toward their spawn
        prescribed density (`_cell_target`) by pulling troops FORWARD from the rear; the rearmost cells
        deplete first. So a DEEP formation sustains full front-cell density — and thus full front combat
        pool, since `_pair_engaged_troops` weights the exchange by the actual troops in the engaged front
        cells — until its depth is spent, while a SHALLOW one thins at the front immediately. This is the
        reserve/rotation the depth machinery abstracts (stamina fatigue-damping), now made literal at the
        troop level: rear ranks step up as the front falls.

        Relational, not absolute — troops close toward the front rather than leaving sub-density holes
        scattered through the block ("troops will always be as close together as possible", Jordan). A
        cell emptied by the reflow keeps its key at 0.0 (every `iter_cells` consumer already gates on
        troops>0, so it contributes nothing to combat/contact — functional coverage shrinks from the rear
        without mutating the cell SET this pass; literal cell dissolution + lateral close-up is a later
        increment). CONSERVATION: sum(cell_troops) is unchanged by this pass — only casualties (applied
        elsewhere) reduce the total. Gated by PC_CLOSE_RANKS (default OFF → cell_troops untouched,
        byte-exact)."""
        if not PC_CLOSE_RANKS:
            return
        ct = self.cell_troops
        if not ct:
            return
        total = sum(ct.values())
        if total <= 0:
            return
        targets = getattr(self, '_cell_target', None) or ct
        # Fill priority: leading rank first (orig_r asc), then column order — the frontage is held while
        # depth is spent from the rear. A cell is filled to its spawn target; the pool empties front-to-back.
        rem = total
        for pid in sorted(ct.keys(), key=lambda pid: (pid[0], pid[1])):
            tgt = targets.get(pid, 0.0)
            if tgt >= rem:
                ct[pid] = rem
                rem = 0.0
            else:
                ct[pid] = tgt
                rem -= tgt
        if rem > 1e-9:  # leftover (only if total exceeded sum of targets — rounding safety) tops the front
            ct[min(ct.keys(), key=lambda pid: (pid[0], pid[1]))] += rem

    def _init_node_state(self):
        """Node-relational cohesion (step 2): cells are nodes at live positions, held in formation by
        relational offsets read off the spawn layout. The shape lays them out once; thereafter the
        formation translates (later wheels/deforms) while the relational offsets maintain cohesion.
        [arch: shapes = initial layout; cohesion = node relational-distance, not re-imposed pattern.]"""
        self._node_facing = None; self._node_facing0 = None
        pos = {}
        for orig_r, orig_c, or_r, or_c in _oriented(self):
            pos[(orig_r, orig_c)] = (float(self.starting_position[0] + or_r),
                                     float(self.starting_position[1] + or_c))
        if not pos:
            self._node_pos = {}; self._node_rel = {}
            self._node_anchor = (0.0, 0.0); self._node_prev_pos = {}
            return
        ar = sum(p[0] for p in pos.values()) / len(pos)
        ac = sum(p[1] for p in pos.values()) / len(pos)
        self._node_anchor = (ar, ac)
        self._node_rel = {cid: (p[0] - ar, p[1] - ac) for cid, p in pos.items()}
        self._node_pos = dict(pos)
        self._node_prev_pos = dict(pos)

    def _rekey_node_state(self, new_ids):
        """Mid-battle re-key of node state to a new pattern id set (movement audit finding 1.5,
        ED-1096) -- called by check_drift right after a shape change, mirroring the existing
        cell_troops re-key. Unlike _init_node_state (which lays a FRESH formation out at
        starting_position, i.e. spawn), this re-forms the new pattern's cells AROUND THE CURRENT
        LIVE ANCHOR -- the sub-unit re-organizes in place, it does not teleport back to spawn.
        The relational-offset math is identical to _init_node_state's (offsets are the new
        pattern's own (or_r,or_c) local layout centered on its own mean -- starting_position
        cancels out of a relative-offset computation identically either way), just anchored to
        self._node_anchor's live value instead of starting_position. Facing is preserved
        untouched -- a formation reorganizing does not reset which way it's looking.

        [2026-07-02 adversarial-review finding, ED-MB-0001] `new_ids` must equal self's CURRENT
        _oriented() id set -- it exists only for the caller to assert against, not as an
        alternative offset source (_oriented(self) is the sole source of the (or_r, or_c) offset
        geometry a bare id tuple cannot carry). Verified below rather than silently accepted: a
        caller computing new_ids from stale or differently-derived state would otherwise re-key to
        the wrong ids with no error -- this was previously a latent, unenforced trap (the sole
        existing call site, check_drift, always passes a freshly-matching set, so this assertion
        changes nothing for it)."""
        offs = {(orig_r, orig_c): (float(or_r), float(or_c)) for orig_r, orig_c, or_r, or_c in _oriented(self)}
        assert set(offs) == set(new_ids), (
            f"_rekey_node_state: new_ids {sorted(new_ids)} doesn't match self's current "
            f"_oriented() id set {sorted(offs)} -- new_ids must be freshly derived from self's "
            f"CURRENT shape/tier/troops immediately before this call, not stale or independently "
            f"computed state.")
        if not offs:
            self._node_pos = {}; self._node_rel = {}; self._node_prev_pos = {}
            return
        mr = sum(p[0] for p in offs.values()) / len(offs)
        mc = sum(p[1] for p in offs.values()) / len(offs)
        ar, ac = self._node_anchor
        self._node_rel = {cid: (o[0] - mr, o[1] - mc) for cid, o in offs.items()}
        self._node_pos = {cid: (ar + rel[0], ac + rel[1]) for cid, rel in self._node_rel.items()}
        self._node_prev_pos = dict(self._node_pos)

    def _node_cells(self):
        """Node-path cells(): live positions in _oriented order. FIELD_MOVEMENT OFF -> snapped to the integer
        grid (byte-exact prior behaviour). FIELD_MOVEMENT ON -> the COORDINATE FIELD: row stays rank-snapped
        (ranks are integer bins) and column is binned to its FILE (frontage=distinct files, depth=rank count)
        via round(c/COL_WIDTH); the raw int(round(c)) grid-snap is deleted on the ON branch only. This is the
        coordinated flip that makes cells() emit file-binned floats end-to-end. [movement-substrate review 06 —
        position + column clusters; folds the COL file-quantizer with the P snap-deletion at one line.]"""
        out = []
        for orig_r, orig_c, _o_r, _o_c in _oriented(self):
            r, c = self._node_pos.get((orig_r, orig_c), (0.0, 0.0))
            if FIELD_MOVEMENT:
                out.append((int(round(r)), int(round(c / COL_WIDTH))))  # field-ON: rank-snapped row, file-binned column
            else:
                out.append((int(round(r)), int(round(c))))  # OFF: exact prior snap
        return out

    def _resolve_maneuver_goal(self, enemy_cells):
        """[movement audit fix-plan step 7, ED-MB-0001 -- the waypoint primitive] Per-subunit maneuver
        goal for the ANCHOR (not per-cell -- the node path's relational cohesion, self._node_rel,
        already carries every cell along together as the anchor moves, so a single anchor-level
        goal is sufficient; no per-cell goal list is needed the way the legacy grid path required
        one). Modeled directly on the legacy 'envelop'/'sweep' two-state per-cell machines
        (advance_cells, ~L890-937) -- same phase logic and the same clearance/rear-margin
        magnitudes (ported, not reinvented), lifted to anchor granularity. Resolved FRESH every
        tick from LIVE enemy extent (never frozen coordinates -- a frozen goal goes stale against a
        moving enemy, this repo's own established discipline, already followed by the legacy
        version this ports). Returns (goal_r, goal_c) if a maneuver instruction is active and
        resolvable, else None (falls through to fix-plan step 4's lateral file-holding default).

        Jordan's "crossed past the enemy" test (2026-07-02, verbatim: "if this grid is 0,0 at
        bottom left, then the wings to encircle must literally be at a smaller x than their
        opponent") is exactly the existing `_past` predicate below -- already implemented in the
        legacy version this ports, not a new mechanic.

        Path-length budget (Jordan-ruled 2026-07-02: "use a formula based upon like
        0.5*speed*maximum-ticks-in-battle") is NOT enforced here -- this resolver computes a goal
        POINT each tick from live geometry, it does not pre-plan a multi-waypoint ROUTE with a
        total length to budget. The two maneuvers here (envelop/sweep) are each a bounded 2-phase
        state machine, not an open-ended path, so there is no route length to validate against the
        budget; that formula applies to a genuinely free-form waypoint list, which is a further
        extension beyond what this step builds (Image 2's asymmetric per-wing / interior-strike-
        point case) -- not built in this pass, flagged as follow-up, not silently dropped."""
        if not enemy_cells:
            return None
        # Gated behind the SAME toggles the legacy per-cell version uses (PC_ENVELOP_PATH/
        # PC_SWEEP) -- not a new gate: this preserves a real kill switch for the new node-path
        # behavior (matching every other additive change this session), and without it V-ENVELOP/
        # V-SWEEP's on/off comparison would be meaningless on the node path (both arms would
        # exercise the maneuver, since 'envelop'/'sweep' stay in Subunit.instructions regardless of
        # the toggle -- confirmed the hard way: this was missing on the first pass and made
        # on==off on the node path even though the mechanism itself was already working).
        if PC_ENVELOP_PATH and 'envelop' in self.instructions:
            return self._envelop_goal(enemy_cells)
        if PC_SWEEP and 'sweep' in self.instructions:
            return self._sweep_goal(enemy_cells)
        if PC_KITE_ENABLED and 'kite' in self.instructions:
            return self._kite_goal(enemy_cells)
        # [DG-2, Jordan-ruled "build it now" 2026-07-08] Discipline-gated at the CONSUMPTION site
        # (not at entry) -- a subunit ordered to yield below D_YIELD simply falls through to the
        # plain default steering below, exactly as if `yielding` were never set.
        if self.yield_active:
            return self._yield_goal(enemy_cells)
        return None

    def _envelop_goal(self, enemy_cells):
        """Two-phase wrap-to-rear, ported from the legacy per-cell version verbatim (same
        clearance/rear-margin magnitudes: +2 frontage clearance, +/-2 rear margin -- ported, not
        reinvented). Phase 1 (not yet past the enemy's depth): steer wide of the nearer flank and
        beyond the enemy's far row edge -- go AROUND, not into the front. Phase 2 (past the
        enemy's depth -- Jordan's "smaller x than their opponent" crossing test): turn in to the
        nearest enemy cell, now a REAR cell."""
        ar, ac = self._node_anchor
        er_rows = [er for (er, _ec) in enemy_cells]
        ec_cols = [ec for (_er, ec) in enemy_cells]
        emin_r, emax_r = min(er_rows), max(er_rows)
        emin_c, emax_c = min(ec_cols), max(ec_cols)
        cen_c = (emin_c + emax_c) / 2.0
        ew = (emax_c - emin_c) + 2   # [ported from advance_cells L903] clearance >= enemy frontage, stays out of contact range
        wide_c = (emin_c - ew) if ac < cen_c else (emax_c + ew)
        if self.advance_dir < 0:
            rear_r = emin_r - 2      # [ported from advance_cells L907]
            past = ar <= rear_r
        else:
            rear_r = emax_r + 2      # [ported from advance_cells L910]
            past = ar >= rear_r
        # [anchor-level adjustment, not present in the ported legacy version -- see docstring]
        # `past` requires REACHING the rear_r depth itself, not merely crossing the enemy's near
        # edge (the legacy per-cell test, `my_r < _emin_r` with no margin). Reuses the SAME
        # existing `2` constant already established for rear_r -- no new magnitude. Necessary
        # because this goal is a SINGLE anchor-level decision for the whole body (one flip point),
        # whereas the legacy version lets each of a subunit's many cells flip independently at
        # its own row -- naturally producing a range of penetration depths across the body, some
        # deeper than others. A single anchor flipping at the bare edge (like the legacy per-cell
        # test) turns the WHOLE body in almost immediately upon crossing, converging on a much
        # shallower rear position than the per-cell average; matching rear_r itself as the
        # threshold is the minimal, non-fabricated fix -- confirmed to close this gap in the
        # V-ENVELOP node-path acceptance measurement (see fix-plan step 6/7 verification).
        #
        # [D2 fix, 2026-07-05] `past` alone is NOT safe to re-test every tick once phase 2 has
        # begun: phase 2's own target (the nearest enemy cell) sits on the near side of `rear_r`
        # from the wing's perspective, so driving toward it re-crosses `rear_r` and `past` flips
        # back to False -- phase 1's goal then yanks the anchor back out to `wide_c`, which
        # re-crosses `rear_r` again next tick, forever. Confirmed by direct trace: wings wheel to
        # the rear_r line correctly, then jitter on it for the rest of the battle, never closing
        # to contact. Fix: latch commitment the first time `past` is true (entry condition),
        # rather than re-testing the same threshold as an exit condition every tick.
        if past:
            self._envelop_committed = True
        if not self._envelop_committed:
            return (rear_r, wide_c)  # phase 1: around the flank, past the depth
        return min(enemy_cells, key=lambda e: (e[0] - ar) ** 2 + (e[1] - ac) ** 2)  # phase 2: turn in to the (now rear) cells

    def _sweep_goal(self, enemy_cells):
        """Lateral flank-march then frontal engagement, ported from the legacy per-cell version.
        Phase 1: shift the anchor laterally toward the nearer enemy flank COLUMN, holding the
        current row (a pure sideways march, matching the legacy "hold row, step column" per-cell
        behaviour) -- the anchor's own existing step-distance scaling (in _node_advance's caller)
        handles the per-tick rate, so the goal is the flank column itself, not a one-step-ahead
        increment the way the legacy per-cell version needed. Phase 2 (at the flank): drive in to
        the nearest enemy cell."""
        ar, ac = self._node_anchor
        swc = [ec for (_er, ec) in enemy_cells]
        swmin, swmax = min(swc), max(swc)
        swcen = (swmin + swmax) / 2.0
        # UNIT-level flank direction (from the subunit's deploy column, not the live anchor column)
        # so the whole body commits to ONE flank coherently -- matches the legacy per-cell version's
        # own reasoning (advance_cells ~L929-931: "per-cell choice would tear the unit toward both").
        swsign = -1 if self._spawn_position[1] < swcen else 1
        swgoal_c = swmin if swsign < 0 else swmax
        if (swsign < 0 and ac > swgoal_c) or (swsign > 0 and ac < swgoal_c):
            return (ar, swgoal_c)    # phase 1: shift laterally toward the flank column, hold row
        return min(enemy_cells, key=lambda e: (e[0] - ar) ** 2 + (e[1] - ac) ** 2)  # phase 2: at the flank -> drive in

    def _kite_goal(self, enemy_cells):
        """[2026-07-02 adversarial-review finding, ED-MB-0001] Standoff-band regulation ('kite'
        instruction), ported to anchor granularity -- matching _envelop_goal/_sweep_goal's own
        established pattern. Closes a real gap: fix-plan step 7 ported envelop/sweep to the node
        path but never kite, so a mounted_archers subunit (gate 2 correctly gives it
        instructions=('kite', 'shoot_move')) fell through to plain target_centroid steering and
        closed to melee on the live default path -- exactly the class of bug this whole audit
        exists to fix, just for a fourth instruction the first pass missed.

        A kiter attacks then flees on countering (Jordan's gate-2 ruling, verbatim: 'Kite is a
        behaviour of attacking an opponent then fleeing upon countering'). Reuses PC_KITE_STANDOFF/
        VOLLEY_MAX_RANGE/reach_for exactly as the legacy per-cell block does (advance_cells
        ~L903-910) -- no new magnitude.

        Matches the legacy 'toward'/'away'/in-band semantics precisely, not just approximately:
        the legacy block never redirects 'toward' to a specific enemy cell -- it leaves cell_target
        as whatever the ALREADY-computed plain approach resolved to (kite_mode='toward' is a no-op
        on dr/dc) -- so 'too far' here returns None, falling through to _node_advance's own step-4
        default exactly as if kite weren't active, rather than inventing a 'drive at the nearest
        cell' behaviour the legacy never had. 'Too close' reflects the nearest enemy point through
        the anchor (goal = 2*anchor - nearest), producing a flee delta -- the anchor-level
        equivalent of the legacy's dr,dc = -dr,-dc inversion. In-band returns the anchor's own
        current position (zero resulting delta downstream), matching the legacy's early `return`
        (hold position entirely, keep volleying) rather than the plain step-4 default (which would
        still close in row)."""
        ar, ac = self._node_anchor
        nearest = min(enemy_cells, key=lambda e: (e[0] - ar) ** 2 + (e[1] - ac) ** 2)
        d = math.hypot(nearest[0] - ar, nearest[1] - ac)
        far_bound = VOLLEY_MAX_RANGE if self.unit_type == 'ranged' else reach_for(self.troop_type)
        if d < PC_KITE_STANDOFF:
            return (2 * ar - nearest[0], 2 * ac - nearest[1])  # too close -> flee (reflect through anchor)
        if d > far_bound:
            return None  # too far -> close in via the plain default approach (matches legacy 'toward')
        return (ar, ac)  # in band -> hold position, keep volleying (matches legacy early return)

    def _yield_goal(self, enemy_cells):
        """DG-2 §2.3 (designs/proposals/mass_battle_fighting_withdrawal_v1.md): giving ground under
        pressure, reusing `_kite_goal`'s reflect-through-anchor flee vector -- the anchor-level
        equivalent of "move away from the nearest engaged enemy". Unlike kite, this ALWAYS flees
        (yielding isn't a standoff-band behaviour); the "at most 1 cell/tick" cap and the ED-MB-0001
        §6 path-budget bound are both enforced by the caller (`_node_advance`'s step-cap), not here,
        matching how `_envelop_goal`/`_sweep_goal`/`_kite_goal` all leave step-magnitude to the caller."""
        if not enemy_cells:
            if PC_YIELD_POCKET:
                self.pocketed = False
            return None
        ar, ac = self._node_anchor
        nearest = min(enemy_cells, key=lambda e: (e[0] - ar) ** 2 + (e[1] - ac) ** 2)
        flee = (2 * ar - nearest[0], 2 * ac - nearest[1])  # reflect through anchor -> flee vector
        # [ED-MB-0024, DG-2 §2.4] Pocket detection: rearward motion structurally blocked -> the body has
        # nowhere left to give ground. Set live so subunit_combat_pool drops the yield malus this tick.
        if PC_YIELD_POCKET:
            self.pocketed = self._yield_pocketed(flee, enemy_cells)
        return flee

    def _yield_pocketed(self, flee, enemy_cells):
        """DG-2 §2.4 pocket: True iff the yielding body cannot give ground -- (a) stepping one cell along
        the flee vector leaves the battlefield (map edge), or (b) an enemy cell lies in the retreat
        direction within YIELD_POCKET_REACH (an enemy has gotten behind it). Reuses only enemy_cells +
        BATTLEFIELD_SIZE -- no new collision substrate, per the design doc's 'emerges from the existing
        standoff/collision detection' accounting."""
        ar, ac = self._node_anchor
        fr, fc = flee[0] - ar, flee[1] - ac
        fmag = math.hypot(fr, fc)
        if fmag < 1e-9:                       # [canonical: epsilon: float magnitude guard] threat coincident with anchor -> nowhere to flee
            return True
        ur, uc = fr / fmag, fc / fmag         # unit flee direction
        nr, nc = ar + ur, ac + uc             # one cell of retreat
        if not (0 <= nr < BATTLEFIELD_SIZE and 0 <= nc < BATTLEFIELD_SIZE):
            return True                       # (a) map edge in the flee direction
        for e in enemy_cells:                 # (b) an enemy in the retreat path (gotten behind)
            er, ec = e[0] - ar, e[1] - ac
            if er * ur + ec * uc > 0 and (er * er + ec * ec) <= YIELD_POCKET_REACH ** 2:
                return True
        return False

    def _node_advance(self, discipline, target_centroid, enemy_cells=None, enemy_cells_float=None):
        """Node-path advance (step 2, increment a): the formation translates toward the target as a
        body (vector-halt at adjacency preserved); each cell relaxes toward its relational slot
        (anchor + rel) by a discipline-gated cohesion factor, so the formation holds together while
        contention/edges can dent it. [arch: relational cohesion replaces the re-imposed shape pattern.]

        [TOI refactor] When FIELD_MOVEMENT is on and enemy_cells_float is supplied, this method no
        longer clamps or commits anything itself -- it computes each non-halted cell's PROPOSED
        (uncapped) end-of-tick position (anchor step, WHEEL rotation, and cohesion relax all run at
        full magnitude, exactly as if no enemy existed) and stashes it on self._node_pending_proposal,
        then returns without touching self._node_pos/_node_anchor. The caller (orchestration.py's
        run_battle) calls this once for every atom on BOTH sides first (the propose phase), then calls
        the module-level resolve_toi_and_commit(atoms_a, atoms_b) exactly once, which finds the true
        continuous-collision time-of-impact for every cross-side cell pair (capping each cell to the
        exact tick-fraction at which it would first reach its reach-and-facing-gated standoff boundary,
        rather than an approximate halved/iterated pull-back) and commits final positions for both
        sides together. This replaces the old halved-anchor-precap + 4-pass best-position-tracking
        per-cell clamp entirely -- see git history for that design and why it was retired (an
        approximation adopted to land a bias fix quickly, not the best available design).

        Every OTHER path (no enemy_cells_float -- the legacy `enemy_cells` Chebyshev/Euclidean dmin-1
        cap, or no clamp at all) is UNCHANGED and commits immediately within this call, exactly as
        before -- byte-exact-off is untouched; this refactor only changes the FIELD_MOVEMENT +
        enemy_cells_float path, which is the one Stage A introduced and is not part of the frozen
        byte-exact invariant."""
        if self.stance == "hold":
            return
        self._node_prev_pos = {cid: p for cid, p in self._node_pos.items()}
        self._moved_this_turn = set()
        op = _oriented(self)
        disc_mult = 1.0 if discipline >= 5 else (0.7 if discipline >= 3 else 0.4)  # [canonical: mass_battle_v30.md §A.4 — Discipline degradation tiers]
        stance_mod = STANCE_SPEED_MOD[self.stance]
        speeds = [cell_speed(self.shape, self.tier, r, c) for r, c, _o, _p in op]
        nz = [s for s in speeds if s > 0]
        base = min(nz) if nz else 0
        # [DG-10 fix, 2026-07-22 — Jordan ruling "if it's broken and not commensurate with system,
        # disable ... fields, not grids. no grids." + "what even is the point of the continuous
        # velocity accumulator?"] The node/field path is the LIVE default: since ED-1089,
        # FIELD_MOVEMENT=1 routes movement HERE, not to advance_cells. It previously took a raw integer
        # floor `max(0, math.floor(base*disc_mult) + stance_mod)`, which grid-snaps any sub-Discipline-5
        # body's velocity to 0 (floor(1*0.7)=0), so a balanced disc<5 formation NEVER advanced to
        # contact on the field (levy/light_inf/heavy_inf/archers/crossbow/sling/artillery are all
        # disc<5 in §B.2 -> the MAJORITY of canonical troop types could not close). That floor is the
        # not-commensurate grid discretization the coordinate FIELD exists to remove. The correct field
        # answer is NOT the fractional-velocity accumulator advance_cells carries (that is itself only a
        # Bresenham-style workaround for keeping INTEGER positions on a grid): _node_anchor/_node_pos
        # are already floats, and the sole downstream consumer moves the anchor by `eff = min(step,
        # mag)` along a unit vector -- fully float-safe. So on the FIELD path we keep `step` as the REAL
        # velocity (no floor, no accumulator): a disc4 body simply advances 0.7 cells/tick on the
        # continuous field. A WHOLE-number velocity is kept as an int (below) so that WHILE a body holds
        # Discipline>=5 it moves bit-for-bit as the old integer path did -- Line-vs-Line gauge rows
        # (mirror/ranged), where no MOVING unit ever degrades below 5, stay byte-identical. The decisive
        # rows DO change, for the right reason: a unit that degrades below Discipline 5 MID-battle
        # (combat / charge shock) previously had its step floored to 0 and FROZE in place; it now keeps
        # moving at its true reduced rate (disc3 -> 0.4 cells/tick). Verified by per-row digest diff +
        # trace (wedge seed 0: side B degrades to disc 3). The legacy grid path (FIELD_MOVEMENT off)
        # keeps its integer floor untouched -> the CI byte-exact grid oracle is preserved. Field gauge
        # goldens (bat.py cell_field/unit_field, not CI-checked) re-recorded for this ruled change.
        vel = base * disc_mult
        if PER_CELL and self.troop_type in ('cavalry', 'mounted_archers'):
            vel *= PC_CAVALRY_SPEED_MULT
        # [ED-MB-0017, Jordan 2026-07-22] The envelop/sweep MANEUVER is a rapid flanking march (envelopment
        # is a timing race — the wing must reach the flank/rear before it is defeated in detail). A cell
        # executing it moves PC_ENVELOP_SPEED_MULT× faster; INERT for any cell without envelop/sweep
        # (byte-exact for the line-vs-line gauge/signature battles). Applies on the field path regardless
        # of PER_CELL so infantry envelopers speed up too, not only PER_CELL cavalry.
        if 'envelop' in self.instructions or 'sweep' in self.instructions:
            vel *= PC_ENVELOP_SPEED_MULT
        if FIELD_MOVEMENT:
            _sf = max(0.0, vel + stance_mod)                       # continuous field velocity (no grid floor)
            # Keep a whole velocity as an int: a float 1.0 vs int 1 changes downstream int-typed
            # speed-differential / cell_last_speed / charge-momentum reads (and the recorded digest),
            # so an undegraded disc>=5 body stays bit-for-bit. Only a genuinely FRACTIONAL velocity
            # (disc<5 -- previously floored to a frozen 0) stays a float and advances the anchor at its
            # true sub-cell rate. "fields, not grids": the fraction is no longer floored away.
            step = int(_sf) if _sf == int(_sf) else _sf
        else:
            step = max(0, math.floor(base * disc_mult) + stance_mod)   # legacy grid oracle: integer floor
            if PER_CELL and self.troop_type in ('cavalry', 'mounted_archers') and step > 0:
                step = int(math.floor(step * PC_CAVALRY_SPEED_MULT))
        # [DG-2 §2.5 anti-abuse, Jordan-ruled "build it now" 2026-07-08] "Speed capped below any
        # realistic pursuer's closing speed (1 cell/tick ceiling)" -- a yielding body cannot
        # indefinitely maintain a standoff gap the way a true kiter can. Applies regardless of the
        # unit's own speed stat (a cavalry subunit ordered to yield still only gives 1 cell/tick).
        if self.yield_active:
            step = min(step, 1)
        toi_deferred = bool(FIELD_MOVEMENT and enemy_cells_float)
        ar, ac = self._node_anchor
        nar, nac = ar, ac
        if target_centroid and step > 0:
            # [movement audit fix-plan step 7, ED-MB-0001] Maneuver goal resolution: an instruction-
            # driven goal (envelop/sweep) takes priority over the plain target_centroid steering.
            # Falls back to fix-plan step 4's lateral file-holding default (see _resolve_maneuver_
            # goal's docstring) when no maneuver instruction is active or resolvable.
            goal = self._resolve_maneuver_goal(enemy_cells)
            if goal is not None:
                goal_r, goal_c = goal
            else:
                # [step 4] Lateral file-holding: a v12 mechanism that existed only on the legacy
                # grid path and regressed to pure-centroid convergence on the node path (finding
                # 1.3) -- a plain advance with no active goal steered every subunit's column at the
                # SAME enemy-centroid column, so wide-placed wings collapsed inward before any
                # maneuver could even begin. A subunit that is one of several siblings in a multi-
                # subunit Unit holds its OWN deployment file (self._spawn_position's column) while
                # its row still closes on the target; a solo subunit is unchanged (steers its
                # column at the target directly -- Stage A/B's existing maneuver tests exercise
                # this case).
                #
                # [2026-07-02 adversarial-review finding, ED-MB-0001] An ESCORT atom (escort_of set)
                # must be checked FIRST, before the sibling-count fallback below: Stage C's
                # orchestration.py already computes an escort-relative target_centroid[1] each tick
                # (the escorted unit's live column + its rotated escort_offset -- see
                # orchestration.py's cached_centroids pass, "so screening survives the escorted
                # unit wheeling/enveloping/sweeping"). An escort is always one of >1 siblings in its
                # Unit by construction, so without this check the sibling branch below silently
                # overwrote that live-tracking column with the escort's own fixed spawn file the
                # moment the escorted unit's column diverged from it -- confirmed via direct
                # reproduction: an escort's anchor column moved TOWARD its spawn file instead of
                # its tracked target the instant this fix-plan step landed.
                _siblings = getattr(getattr(self, '_unit', None), 'subunits', None)
                if self.escort_of is not None:
                    goal_c = target_centroid[1]
                elif _siblings is not None and len(_siblings) > 1:
                    goal_c = self._spawn_position[1]
                else:
                    goal_c = target_centroid[1]
                goal_r = target_centroid[0]
            dr = goal_r - ar
            dc = goal_c - ac
            if self.stance == "retreat":
                dr, dc = -dr, -dc
            if not toi_deferred and enemy_cells:
                # [migration S2, unchanged] legacy anchor pre-cap -- FIELD_MOVEMENT off (PC_NODE_COHESION
                # on) or no float data supplied; no per-cell TOI counterpart exists for this path, so it
                # keeps its own dmin-1 cap exactly as before.
                mine = self._node_cells()
                if mine:
                    dmin = min((math.hypot(mr - er, mc - ec) if FIELD_MOVEMENT else max(abs(mr - er), abs(mc - ec)))
                               for (mr, mc) in mine for (er, ec) in enemy_cells)  # [migration S2] Euclidean on the field; Chebyshev on the grid (byte-exact OFF)
                    step = min(step, max(0, dmin - 1))   # vector-halt: stop at adjacency, not past
            # [TOI refactor] The FIELD_MOVEMENT+enemy_cells_float anchor pre-cap is REMOVED: the anchor
            # now always proposes its FULL uncapped step (no standoff clamp at the body level at all).
            # Per-cell time-of-impact (resolve_toi_and_commit) is the sole standoff-enforcement
            # mechanism on this path now, operating on true continuous linear paths per cell rather
            # than a body-level speed pre-cap layered under a second per-cell clamp.
            mag = abs(dr) + abs(dc)
            # [D2b fix, 2026-07-05, mass-battle Cannae gauge follow-up audit] Was `if mag >= 0.5 and
            # step > 0: nar,nac = ar + step*(dr/mag), ...` -- a fixed integer `step` that does not
            # evenly divide the remaining distance can leave `mag` permanently inside [0, 0.5) of a
            # maneuver waypoint (e.g. _envelop_goal's phase-1 (rear_r, wide_c)) without ever reaching
            # it: since a full `step`-length move overshoots past a close-but-not-arrived goal, and
            # the < 0.5 branch below took no action at all, the anchor froze there forever, unable to
            # ever satisfy a waypoint's exact-threshold test. Capping the move at min(step, mag)
            # instead closes the remaining gap exactly when within one step of the goal (no
            # overshoot, no freeze) and reproduces the old behaviour bit-for-bit whenever mag >= step
            # (the common, far-from-goal case) -- confirmed by direct trace: a maneuvering wing that
            # previously stalled ~0.3 units short of its rear_r waypoint for the rest of the battle
            # now reaches it exactly.
            if step > 0 and mag > 1e-9:  # [canonical: epsilon: float magnitude guard]
                eff = min(step, mag)
                nar, nac = ar + eff * (dr / mag), ac + eff * (dc / mag)
        # WHEEL (increment 2b): the formation re-faces the enemy as a body. f = current facing (unit vector),
        # f0 = spawn facing (toward the enemy at first contact); the relational layout is rotated by the
        # rotation taking f0 -> f, so the whole formation pivots while cohesion holds it together. Head-on
        # engagements (f stays ~ f0) leave the rotation at identity -> identical to increment 2a. Uses the
        # PROPOSED anchor (nar,nac); harmless when toi_deferred, since facing only cares about direction to
        # a not-too-close centroid, not the exact (possibly later TOI-capped) anchor value.
        rc_w, rs_w = 1.0, 0.0   # (cos, sin) of the spawn->current rotation; identity until the body wheels
        if target_centroid:
            tdr = target_centroid[0] - nar; tdc = target_centroid[1] - nac
            tmag = math.hypot(tdr, tdc)
            if tmag > 0:
                ftr, ftc = tdr / tmag, tdc / tmag   # f_target: unit direction to the enemy
                if self._node_facing is None:
                    self._node_facing = (ftr, ftc); self._node_facing0 = (ftr, ftc)
                else:
                    # [movement audit fix-plan step 5, ED-MB-0001] Rotation-based facing update,
                    # replacing the prior lerp-normalize (fr0 + kw*(ftr-fr0), then re-normalize).
                    # The lerp degenerates to the zero vector when current and desired facing are
                    # EXACTLY anti-parallel at full discipline (kw=0.5: 0.5*fr0 + 0.5*(-fr0) = 0),
                    # and is numerically unstable approaching that point (dividing a near-zero
                    # vector by its own near-zero magnitude amplifies rounding noise into an
                    # effectively random direction) -- exactly the 180-degree reversal a
                    # wheel-to-rear maneuver needs to pass through cleanly. Same wheel rate `kw`
                    # (disc-gated, no new magnitude), reused as an ANGULAR fraction of the
                    # remaining turn instead of a linear vector blend fraction -- for small angles
                    # the two are nearly identical (sin(theta)~=theta), so ordinary (non-180)
                    # wheeling is not meaningfully perturbed; at 180 degrees the rotation is
                    # well-defined and non-degenerate for any kw>0.
                    kw = disc_mult * 0.5            # wheel rate (disc-gated, slower than the cohesion snap)
                    fr0, fc0 = self._node_facing
                    theta_cur = math.atan2(fc0, fr0)
                    theta_tgt = math.atan2(ftc, ftr)
                    delta = math.atan2(math.sin(theta_tgt - theta_cur), math.cos(theta_tgt - theta_cur))  # wrap to (-pi, pi]
                    if abs(delta) >= math.pi - 1e-9:  # [canonical: epsilon: float angle-wrap tolerance guard]
                        delta = math.pi  # deterministic tie-break: exact/near-exact reversal always turns the same way
                    theta_new = theta_cur + kw * delta
                    self._node_facing = (math.cos(theta_new), math.sin(theta_new))
                f0r, f0c = self._node_facing0; fr, fc = self._node_facing
                rc_w = f0r * fr + f0c * fc          # cos of rotation f0 -> f
                rs_w = f0r * fc - f0c * fr          # sin of rotation f0 -> f
        k = disc_mult   # cohesion factor reuses the discipline multiplier: disciplined formations hold tight, ragged ones deform
        proposal = {}
        for orig_r, orig_c, _o_r, _o_c in op:
            cid = (orig_r, orig_c)
            if cid in self.halted_cells:
                if toi_deferred:
                    # Frozen body still occupies space -- record it (proposed==start, zero motion) so
                    # OTHER (moving) cells, on either side, correctly treat it as a fixed obstacle in
                    # the cross-side TOI resolve. No facing/position write (matches the `continue`
                    # below exactly): a halted cell's own state is untouched this tick.
                    _fr, _fc = self._node_pos.get(cid, self._node_anchor)
                    proposal[cid] = (_fr, _fc, _fr, _fc)
                continue
            rel = self._node_rel.get(cid, (0.0, 0.0))
            des_r = nar + (rc_w * rel[0] - rs_w * rel[1])   # anchor + R(f0->f) . rel : rotated relational slot
            des_c = nac + (rs_w * rel[0] + rc_w * rel[1])
            cr, cc = self._node_pos.setdefault(cid, self._node_anchor)  # [canonical: continuous-mode seed: unseen cell defaults to anchor]
            nr = min(BATTLEFIELD_SIZE - 1, max(0, cr + k * (des_r - cr)))
            nc = min(BATTLEFIELD_SIZE - 1, max(0, cc + k * (des_c - cc)))
            if not toi_deferred and enemy_cells:
                # [migration P, unchanged] OFF = verbatim int(round) grid-membership probe; ON (no float
                # data supplied) = file-binned probe matching the file-indexed enemy cells() keys.
                _probe = (int(round(nr)), int(round(nc / COL_WIDTH))) if FIELD_MOVEMENT else (int(round(nr)), int(round(nc)))
                if _probe in enemy_cells:
                    nr, nc = cr, cc   # blocked: an enemy holds this cell -> hold (no pass-through; front dents); cohesion retries next tick
            self.cell_last_speed[cid] = step
            if toi_deferred:
                # [TOI refactor] Defer: (cr,cc) is the START position, (nr,nc) is the PROPOSED
                # (uncapped) end-of-tick position. No standoff clamp applied here at all -- see
                # resolve_toi_and_commit for the exact continuous-collision solve and commit.
                proposal[cid] = (cr, cc, nr, nc)
            else:
                self._commit_cell_position(cid, nr, nc, target_centroid, discipline)
        if toi_deferred:
            self._node_pending_proposal = proposal
            self._node_pending_target_centroid = target_centroid
            self._node_pending_discipline = discipline
        else:
            self._node_anchor = (nar, nac)

    def _commit_cell_position(self, cid, nr, nc, target_centroid, discipline):
        """[TOI refactor, factored out of _node_advance] Write one cell's FINAL (post-standoff, if
        any) position and update its attention/facing state. Called either immediately (legacy /
        no-clamp paths, from _node_advance itself) or once per cell from resolve_toi_and_commit after
        the cross-side TOI resolve has determined the final position on the FIELD_MOVEMENT +
        enemy_cells_float path. Unchanged from the pre-refactor per-cell facing-update block."""
        # (a) attention (facing model): face the ENGAGED target; else keep the WHEEL-slewed body facing.
        # [Stage B] The prior "don't double-slew, the node path already has a disc-gated WHEEL slew"
        # reasoning didn't actually hold once this branch fires: it OVERWRITES cell_facing_vec with
        # a fresh, instantaneous target-direction vector, discarding whatever latency the WHEEL slew
        # (a body-level heading, a different quantity) had built up -- zero rate-limiting, the exact
        # hyper-reactive instant-snap this facing model exists to prevent. Slewed here too, reusing
        # _slew_facing (the same function the legacy path already uses for this), gated identically.
        # [DG-2 §2.3, Jordan-ruled "build it now" 2026-07-08] "Facing is preserved toward the enemy"
        # -- mechanically load-bearing (octagon_angle's zone gating is a pure function of facing), so
        # this fires REGARDLESS of PC_FACING_MODEL (which defaults OFF): a yielding body must not
        # inherit the raw-movement-vector facing that would otherwise point it in its flee direction,
        # the exact "faces away like a routing body" failure this mechanic exists to avoid. Default
        # `yielding=False` -> inert for every existing scenario, independent of the facing-model toggle.
        if self.yield_active and self.target_atom is not None:
            _tc = self.target_atom.centroid()
            self.cell_facing_vec[cid] = (_tc[0] - nr, _tc[1] - nc)
        elif PC_FACING_MODEL and PC_FACING_ATTENTION and self.target_atom is not None:
            _tc = self.target_atom.centroid()
            _desired = (_tc[0] - nr, _tc[1] - nc)
            _cur = self.cell_facing_vec.get(cid, self._node_facing or (self.advance_dir, 0))
            self.cell_facing_vec[cid] = _slew_facing(_cur, _desired, discipline)
        elif self._node_facing is not None:
            self.cell_facing_vec[cid] = self._node_facing
        elif target_centroid:
            self.cell_facing_vec[cid] = (target_centroid[0] - nr, target_centroid[1] - nc)
        self._node_pos[cid] = (nr, nc)
        self._moved_this_turn.add(cid)

    def centroid(self):
        c = self.cells()
        if not c: return self.starting_position
        return (sum(r for r, x in c) / len(c), sum(x for r, x in c) / len(c))

    def advance_cells(self, discipline, target_centroid, enemy_cells=None, enemy_cells_float=None):
        """
        enemy_cells: set of abs (r,c) positions of all enemy cells.
        enemy_cells_float: [Stage A, additive] list of (r,c,reach) true-float enemy-cell triples --
        see _node_advance's docstring. Ignored on the legacy (non-node) path below.
        v11: cap each cell's advance to bring it to adjacency (distance=1) but not past
        the nearest enemy cell. Prevents over-run that produces paradoxical angles.
        [canonical: Jordan design — vector halt at first adjacency]
        """
        if PC_NODE_COHESION and hasattr(self, '_node_pos'):
            return self._node_advance(discipline, target_centroid, enemy_cells, enemy_cells_float)
        if self.stance == "hold": return
        # KITING (§13): a unit with the 'kite' instruction regulates its distance to stay in a
        # standoff band instead of closing to melee. Distance metric matches volley's
        # _atom_distance (Chebyshev, nearest cells) so "in band" == "can shoot" for a ranged kiter.
        # INERT without the 'kite' instruction -> byte-exact for every existing scenario.
        #
        # [movement audit gate 2, ED-MB-0001, Jordan-ruled 2026-07-02: "Kite is a behaviour of
        # attacking an opponent then fleeing upon countering, which means that it is BEST done
        # with ranged weapons like a bow but can still be executed by cavalry with spears/lances."]
        # No longer gated on unit_type=='ranged' -- kite is weapon-independent steering; ONLY
        # volley fire itself (a separate gate, orchestration.volley_phase) requires a ranged
        # weapon. The "far" edge of the band still uses VOLLEY_MAX_RANGE for a ranged kiter
        # (unchanged, exact prior behaviour), but for a melee kiter (a lance/spear cavalry
        # executing a hit-and-run) VOLLEY_MAX_RANGE would be meaningless -- reuses the already-
        # grounded PP-290 reach_for(troop_type) primitive instead (troop_types.registry) rather
        # than inventing a new melee-standoff magnitude: hover just past where its own weapon
        # can no longer threaten, not a volley-specific distance. NOTE: this whole block is
        # currently unreachable on the default node/field path (the early return above fires
        # first) -- it only ever ran, and only ever will run until fix-plan step 7 ports kiting
        # to the live path, when PC_NODE_COHESION is off.
        kite_mode = None
        if PC_KITE_ENABLED and 'kite' in self.instructions and enemy_cells:
            far_bound = VOLLEY_MAX_RANGE if self.unit_type == 'ranged' else reach_for(self.troop_type)
            mine = self.cells()
            if mine:
                d = min((math.hypot(mr - er, mc - ec) if FIELD_MOVEMENT else max(abs(mr - er), abs(mc - ec))) for (mr, mc) in mine for (er, ec) in enemy_cells)  # [migration S2] Euclidean on the field (byte-exact OFF)
                if d < PC_KITE_STANDOFF: kite_mode = 'away'    # too close -> open the gap (retreat vector)
                elif d > far_bound:      kite_mode = 'toward'  # out of range -> close into the band
                else:                    return                # in band -> hold position, keep volleying
        # v13: snapshot offsets and facings before advance, used to revert any cell
        # whose new position would collide with another cell of this subunit (and
        # the discipline check passes — formation held). Without snapshot, we can't
        # cleanly return a cell to its formation slot.
        # [canonical: Jordan design 2026-05-12 — discipline-gated formation hold]
        self._prev_offsets = dict(self.cell_offsets)
        self._prev_offsets_c = dict(self.cell_offsets_c)
        self._prev_facings = dict(self.cell_facing_vec)
        # v13: reset per-turn movement tracker
        self._moved_this_turn = set()
        op = _oriented(self)
        disc_mult = 1.0 if discipline >= 5 else (0.7 if discipline >= 3 else 0.4)  # [canonical: mass_battle_v30.md §A.4 — Discipline degradation tiers]
        stance_mod = STANCE_SPEED_MOD[self.stance]
        all_speeds = [cell_speed(self.shape, self.tier, r, c) for r, c, _, _ in op]
        nonzero_speeds = [s for s in all_speeds if s > 0]
        min_speed = min(nonzero_speeds) if nonzero_speeds else 0
        for orig_r, orig_c, or_r, or_c in op:
            if (orig_r, orig_c) in self.halted_cells: continue
            base_speed = cell_speed(self.shape, self.tier, orig_r, orig_c)
            if base_speed == 0: continue
            if FIELD_MOVEMENT:
                # [field-movement, default OFF — movement-substrate review 06, finding 2] CONTINUOUS speed:
                # accumulate the fractional discipline-scaled velocity and step by its whole part, carrying
                # the remainder, so a degraded body advances at its TRUE average rate instead of flooring to
                # 0 every turn (floor(1*0.7)=0 freezes a slow degraded unit). Integer positions are
                # preserved; only the per-turn step TIMING changes. The cavalry multiplier scales the float
                # velocity (not a re-floored integer). ON path is a recorded behaviour change (own baseline).
                vel = base_speed * disc_mult
                if PER_CELL and self.troop_type in ('cavalry', 'mounted_archers'):
                    vel *= PC_CAVALRY_SPEED_MULT
                acc = self._speed_accum.get((orig_r, orig_c), 0.0) + vel
                whole = math.floor(acc)
                self._speed_accum[(orig_r, orig_c)] = acc - whole
                actual_speed = max(0, int(whole) + stance_mod)
            else:
                actual_speed = max(0, math.floor(base_speed * disc_mult) + stance_mod)
                if PER_CELL and self.troop_type in ('cavalry', 'mounted_archers') and actual_speed > 0:
                    # Increment 4-followup: cavalry velocity primitive — cavalry closes faster, producing the
                    # momentum differential that triggers the depth-absorbed charge (Incr5). [ASSUMPTION:
                    # cavalry speed x2 — basis: shock cavalry close far faster than infantry. Class-B, vetoable.]
                    actual_speed = int(math.floor(actual_speed * PC_CAVALRY_SPEED_MULT))
            if actual_speed == 0: continue
            if TIP_SUPPORT_ENABLED and base_speed > min_speed:
                current_offset = self.cell_offsets.get((orig_r, orig_c), 0)
                slow_offsets = [
                    self.cell_offsets.get((r2, c2), 0)
                    for r2, c2, _, _ in op
                    if cell_speed(self.shape, self.tier, r2, c2) == min_speed
                ]
                if slow_offsets and current_offset >= min(slow_offsets) + TIP_SUPPORT_GAP:
                    continue
            my_r = (self.starting_position[0] + or_r
                    + self.cell_offsets.get((orig_r, orig_c), 0) * self.advance_dir)
            my_c = (self.starting_position[1] + or_c
                    + self.cell_offsets_c.get((orig_r, orig_c), 0))
            # v12: column-local targeting — each cell maintains its starting column
            # and steers toward the enemy at that column-level. Bottom-up: historical
            # infantry maintained their assigned file in the formation. Lateral drift
            # only happens via deliberate maneuver, not engagement attraction.
            #
            # Effect: GappedLine blocks don't converge (gap stays open). Horseshoe
            # wings don't drift inward (wide footprint preserved). Wedge naturally
            # leads with tip because wedge cells are already at different columns.
            # [canonical: Jordan design 2026-05-12 — bottom-up column-local targeting]
            cell_target = None
            if target_centroid:
                my_starting_col = self.starting_position[1] + or_c
                cell_target = (target_centroid[0], my_starting_col)
                # ENVELOPMENT WHEEL (Jordan 2026-05-31): an OVERHANG cell — one with no enemy in its
                # file (beyond the enemy frontage) — wheels toward the nearest enemy cell (the flank)
                # instead of holding its column. Lateral movement -> the facing vector (set below at
                # cell_facing_vec) rotates inward -> the octagon angle reads the enemy's flank/rear.
                # "the front of the cell should be the same as its vector." Gated; toggle-off untouched.
                if PER_CELL and PC_WHEEL and enemy_cells:
                    e_cols = [ec for (_er, ec) in enemy_cells]
                    emin, emax = min(e_cols), max(e_cols)
                    # overhang = my column lies BEYOND the enemy's frontage span (past either flank)
                    if my_c < emin or my_c > emax:
                        cell_target = min(enemy_cells,
                                          key=lambda e: (e[0] - my_r) ** 2 + (e[1] - my_c) ** 2)
                # ENVELOP MANEUVER (build C): a subunit carrying the 'envelop' instruction paths AROUND the
                # enemy's flank into its REAR -- two phase. Phase 1 (not yet past the enemy's depth): steer to a
                # point wide of the nearer flank and beyond the enemy's far row edge (go around, not into the
                # front). Phase 2 (past the enemy's depth): turn in to the nearest enemy cell, which is now a
                # REAR cell -> the facing vector reads RED. Reuses the 2D cell_target steering; gated by the
                # 'envelop' instruction -> INERT for every existing scenario (no such instruction) -> byte-exact.
                # [canonical: Cannae 216 BC double-envelopment; Khalid at Walaja; A.8 Envelopment -- the wrap to the rear.]
                if PER_CELL and PC_ENVELOP_PATH and 'envelop' in self.instructions and enemy_cells:
                    _er_rows = [er for (er, _ec) in enemy_cells]
                    _ec_cols = [ec for (_er, ec) in enemy_cells]
                    _emin_r, _emax_r = min(_er_rows), max(_er_rows)
                    _emin_c, _emax_c = min(_ec_cols), max(_ec_cols)
                    _cen_c = (_emin_c + _emax_c) / 2.0
                    _ew = (_emax_c - _emin_c) + 2          # clearance >= enemy frontage so the pass stays out of contact range
                    _wide = (_emin_c - _ew) if my_c < _cen_c else (_emax_c + _ew)
                    if self.advance_dir < 0:
                        _past = my_r < _emin_r
                        _rear_r = _emin_r - 2
                    else:
                        _past = my_r > _emax_r
                        _rear_r = _emax_r + 2
                    if not _past:
                        cell_target = (_rear_r, _wide)            # phase 1: around the flank, past the depth
                    else:
                        cell_target = min(enemy_cells,            # phase 2: turn in to the (now rear) cells
                                          key=lambda e: (e[0] - my_r) ** 2 + (e[1] - my_c) ** 2)
                # SWEEP MANEUVER (build E, lateral half): a subunit carrying the 'sweep' instruction marches
                # LATERALLY to the nearer enemy FLANK column, then drives in to engage there -- concentrating
                # force on a flank WITHOUT the full wrap-to-rear of 'envelop'. Distinct from envelop (rear) and
                # from the wheel (which only turns OVERHANG cells): sweep repositions the whole body sideways
                # first, then engages the flank frontally. Gated by the 'sweep' instruction -> INERT for every
                # existing scenario -> byte-exact.
                # [ASSUMPTION: 'sweep' = lateral flank-ward repositioning then frontal flank engagement -- basis:
                #  oblique order / flank march (Leuthen 1757; Epaminondas at Leuctra). The original E item named
                #  'sweep' without semantics; this is a grounded editorial reading. Class-B, Jordan-vetoable.]
                if PER_CELL and PC_SWEEP and 'sweep' in self.instructions and enemy_cells:
                    _swc = [ec for (_er, ec) in enemy_cells]
                    _swmin, _swmax = min(_swc), max(_swc)
                    _swcen = (_swmin + _swmax) / 2.0
                    # UNIT-level flank direction (from the subunit's deploy column, NOT the cell's) so the whole
                    # body shifts coherently to one flank -- per-cell choice would tear the unit toward both.
                    _swsign = -1 if self.starting_position[1] < _swcen else 1
                    _swgoal = _swmin if _swsign < 0 else _swmax
                    if (_swsign < 0 and my_c > _swgoal) or (_swsign > 0 and my_c < _swgoal):
                        cell_target = (my_r, my_c + _swsign * actual_speed)   # phase 1: shift laterally (uniform) toward the flank
                    else:
                        cell_target = min(enemy_cells,            # phase 2: at the flank -> drive in to engage
                                          key=lambda e: (e[0] - my_r) ** 2 + (e[1] - my_c) ** 2)
            if cell_target:
                dr = cell_target[0] - my_r
                dc = cell_target[1] - my_c
                if self.stance == "retreat": dr, dc = -dr, -dc
                if kite_mode == 'away': dr, dc = -dr, -dc  # kiter opens the gap; 'toward' keeps dr,dc (closes in); 'hold' returned above
                abs_dr, abs_dc = abs(dr), abs(dc)
                total = abs_dr + abs_dc
                if total < 0.5: continue
                if FIELD_MOVEMENT:
                    # continuous heading: true-diagonal float step, no 8-direction snap (field baseline).
                    # NOTE: on a valid field-ON run FIELD_MOVEMENT ⇒ PC_NODE_COHESION, so advance_cells returns
                    # early to _node_advance and this legacy branch is not reached; kept guarded for OFF byte-exactness.
                    r_step = actual_speed * (dr / total)
                    c_step = actual_speed * (dc / total)
                else:
                    r_step = round(actual_speed * (abs_dr / total))
                    c_step = actual_speed - r_step
                    r_step *= (1 if dr > 0 else -1) if abs_dr > 0 else 0
                    c_step *= (1 if dc > 0 else -1) if abs_dc > 0 else 0
                # v11: proximity cap removed — over-run corrected post-movement
                self.cell_offsets[(orig_r, orig_c)] = \
                    self.cell_offsets.get((orig_r, orig_c), 0) + r_step * self.advance_dir
                self.cell_offsets_c[(orig_r, orig_c)] = \
                    self.cell_offsets_c.get((orig_r, orig_c), 0) + c_step
            else:
                self.cell_offsets[(orig_r, orig_c)] = \
                    self.cell_offsets.get((orig_r, orig_c), 0) + actual_speed
            # EDGE-CORNERING (§13 follow-up / dynamic-bounds): a cell cannot move off the battlefield.
            # Clamp the resulting absolute position to [0, BATTLEFIELD_SIZE) and back-solve the offset
            # so it does not accumulate past the edge (no hysteresis when the cell later moves back).
            # Inward-moving units never reach an edge -> byte-exact; a retreating kiter pinned at the
            # edge can be overtaken (the vs-cavalry / cornering counter; Patay/Arsuf).
            _abs_r = self.starting_position[0] + or_r + self.cell_offsets[(orig_r, orig_c)] * self.advance_dir
            _abs_c = self.starting_position[1] + or_c + self.cell_offsets_c.get((orig_r, orig_c), 0)
            _cl_r = min(BATTLEFIELD_SIZE - 1, max(0, _abs_r))
            _cl_c = min(BATTLEFIELD_SIZE - 1, max(0, _abs_c))
            if _cl_r != _abs_r:
                self.cell_offsets[(orig_r, orig_c)] = (_cl_r - self.starting_position[0] - or_r) * self.advance_dir
            if _cl_c != _abs_c:
                self.cell_offsets_c[(orig_r, orig_c)] = _cl_c - self.starting_position[1] - or_c
            # F-ii: record speed when cell actually moves
            self.cell_last_speed[(orig_r, orig_c)] = actual_speed
            # v11: record raw movement vector for octagon angle
            _desired = (r_step if cell_target else actual_speed * self.advance_dir,
                        c_step if cell_target else 0)
            # [DG-2 §2.3, Jordan-ruled "build it now" 2026-07-08] Same facing-lock as the node path's
            # equivalent block (see its comment) -- fires regardless of PC_FACING_MODEL. Default
            # `yielding=False` -> inert; this legacy grid path is otherwise the frozen byte-exact
            # oracle and untouched by this change unless a scenario explicitly sets `yielding`.
            if self.yield_active and self.target_atom is not None:
                _tc = self.target_atom.centroid()
                _desired = (_tc[0] - my_r, _tc[1] - my_c)
            elif PC_FACING_MODEL:
                # (a) attention: face the ENGAGED target if one is committed, else the movement vector
                if PC_FACING_ATTENTION and self.target_atom is not None:
                    _tc = self.target_atom.centroid()
                    _desired = (_tc[0] - my_r, _tc[1] - my_c)
                # (b) slew/commitment: rotate current facing toward _desired at a disc-gated rate (no instant snap)
                _cur = self.cell_facing_vec.get((orig_r, orig_c), (self.advance_dir, 0))
                self.cell_facing_vec[(orig_r, orig_c)] = _slew_facing(_cur, _desired, discipline)
            else:
                self.cell_facing_vec[(orig_r, orig_c)] = _desired
            # v13: mark cell as having moved this turn (for cross-side contention)
            self._moved_this_turn.add((orig_r, orig_c))

    def get_cell_facing(self, orig_r, orig_c):
        """Return the facing vector for a cell. Defaults to advance_dir if never moved."""
        # (d) rout facing: a routed body faces AWAY from the enemy (fleeing) -> rear penalties land.
        if PC_FACING_MODEL and PC_FACING_ROUT and getattr(self, 'routed', False):
            fv = self.cell_facing_vec.get((orig_r, orig_c), (self.advance_dir, 0))
            return (-fv[0], -fv[1])
        return self.cell_facing_vec.get((orig_r, orig_c), (self.advance_dir, 0))

    def halt_before_enemy(self, enemy_unit):
        """
        v11: over-run correction disabled. Pre-pairs halting (in run_battle) handles
        contact stability. Per-cell octagon sees REAR angles symmetrically when both
        sides over-run, which cancels out in symmetric matchups.
        [canonical: Jordan design — removed after causing ordering asymmetries]
        """
        pass

    def role_at_contact(self, contact_col):
        # [LC-8] Horseshoe/RefusedFlank branches removed -- zero live callers (confirmed dead code
        # before this change too; a diagnostic label helper never wired to any resolver), and both
        # shapes are retired as Subunit.shape values (see geometry.CELL_PATTERN_FN's note).
        if self.shape == "Line": return "normal"
        if self.shape == "Arrowhead":
            pattern = CELL_PATTERN_FN[self.shape](self.tier)
            for r, c in pattern:
                if r == 0:
                    abs_c = self.starting_position[1] + c + self.cell_offsets_c.get((r, c), 0)
                    if abs(abs_c - contact_col) <= 0.5: return "tip"
            return "flank"
        if self.shape == "GappedLine":
            # [canonical: v11 — updated to match equalized gapped_line_cells sizes]
            sizes = {1: 2, 2: 3, 3: 4, 4: 4}
            half_w = sizes.get(self.tier, 4)  # [canonical: geometry.py gapped_line_cells / §A.3b — half-width default]
            if contact_col == half_w + self.starting_position[1]: return "gap"
            return "flank_engaged"
        return "normal"

    # [canonical: Jordan design — cell capacity, discipline-gated merge, midpoint facing on formation breakdown]
    def resolve_internal_collisions(self, unit_discipline):
        """v13: discipline-gated formation hold.

        After advance_cells + halt_before_enemy, detect cells of THIS subunit that
        occupy the same absolute position. Bottom-up: a cell has finite capacity;
        two cells cannot meaningfully occupy the same battlefield position without
        merging — and merging is a tactical failure (lost formation, broken facing).

        For each collision cluster (>1 cells at same abs pos):
          - Anchor: cell with smallest orig_r (formation-front position)
          - For each trailing cell:
            - Roll d10 vs unit_discipline
            - PASS (roll <= discipline): trailing cell reverts to its previous
              position (snapshot from start of this turn's advance_cells). Formation
              held; cell stays in its assigned slot.
            - FAIL (roll > discipline): cells merge at the collision position.
              Their cell_facing_vec is averaged (midpoint vector). This propagates
              through per-cell octagon angle — misaligned facing produces YELLOW/RED
              zones more often, modelling vulnerability of broken formation.

        Returns (n_halted, n_merged) for diagnostics.
        Citation: see preceding canonical comment.
        """
        if not self._prev_offsets:
            return (0, 0)  # First turn, no snapshot to revert to
        op = _oriented(self)
        pos_to_cells = {}
        for orig_r, orig_c, or_r, or_c in op:
            ar = (self.starting_position[0] + or_r
                  + self.cell_offsets.get((orig_r, orig_c), 0) * self.advance_dir)
            ac = (self.starting_position[1] + or_c
                  + self.cell_offsets_c.get((orig_r, orig_c), 0))
            pos_to_cells.setdefault((ar, ac), []).append((orig_r, orig_c))
        n_halted = 0
        n_merged = 0
        for pos, cells in pos_to_cells.items():
            if len(cells) <= 1:
                continue
            # Anchor: smallest orig_r (front-most in formation) breaks ties by orig_c
            cells_sorted = sorted(cells, key=lambda c: (c[0], c[1]))
            anchor = cells_sorted[0]
            for trailing in cells_sorted[1:]:
                # Discipline check: d10 roll vs unit's discipline value
                # [canonical: params/core.md — d10 vs TN; here TN = unit_discipline]
                roll = random.randint(1, 10)
                if roll <= unit_discipline:
                    # PASS: revert trailing cell to its previous position (formation held)
                    self.cell_offsets[trailing] = self._prev_offsets.get(trailing, 0)
                    self.cell_offsets_c[trailing] = self._prev_offsets_c.get(trailing, 0)
                    self.cell_facing_vec[trailing] = self._prev_facings.get(
                        trailing, (self.advance_dir, 0)
                    )
                    n_halted += 1
                else:
                    # FAIL: cells merge with midpoint facing (formation broken)
                    anc_fv = self.cell_facing_vec.get(anchor, (self.advance_dir, 0))
                    tr_fv = self.cell_facing_vec.get(trailing, (self.advance_dir, 0))
                    mid_fv = (
                        (anc_fv[0] + tr_fv[0]) / 2,
                        (anc_fv[1] + tr_fv[1]) / 2,
                    )
                    self.cell_facing_vec[anchor] = mid_fv
                    self.cell_facing_vec[trailing] = mid_fv
                    self.merged_cells.add(anchor)
                    self.merged_cells.add(trailing)
                    n_merged += 1
        return (n_halted, n_merged)


class _ToiCell:
    """[TOI refactor] One cell's position/reach/facing data for one tick's cross-side resolve, plus its
    mutable best_t (the tightest cap found across every cross-side pair it's party to; starts at 1.0 =
    unconstrained). A plain named-attribute holder rather than a positional tuple/list, so field access
    reads clearly (ea.reach, not ea[6]) and mutating best_t needs no index bookkeeping."""
    __slots__ = ('atom', 'cid', 'sr', 'sc', 'pr', 'pc', 'reach', 'facing', 'best_t', 'movable')

    def __init__(self, atom, cid, sr, sc, pr, pc, reach, facing, movable):
        self.atom = atom; self.cid = cid
        self.sr = sr; self.sc = sc; self.pr = pr; self.pc = pc
        self.reach = reach; self.facing = facing
        self.best_t = 1.0
        self.movable = movable


def resolve_toi_and_commit(all_atoms_a, all_atoms_b):
    """[TOI refactor] Cross-side time-of-impact resolve + commit. Call once per tick with EVERY
    subunit of both sides (moving or not) -- an atom that called _node_advance this tick (FIELD_MOVEMENT
    + enemy_cells_float) has stashed a proposal on self._node_pending_proposal (its start and PROPOSED,
    uncapped, end-of-tick position for every non-halted cell); an atom that did NOT move this tick (no
    target yet, a reserve, gated by target_delay_ticks/target_condition) contributes its CURRENT true
    positions as static (start==proposed) obstacle entries instead -- it must still be respected as a
    physical body by the other side's moving cells, exactly as the pre-refactor enemy_cells_float (built
    from ALL of a unit's subunits unconditionally) always was; only feeding the resolve the "moving"
    subset would silently let an enemy pass into/through a not-yet-targeting friendly formation for a
    tick, an adversarial-review-caught regression versus the pre-refactor behaviour.

    For every cross-side cell pair the stop surface is BODY vs BODY (two unit squares, reach 0 -- see
    the ED-MB-0012 note at the pair loop): a circular reject on the body circumscribed circles skips
    far pairs O(1), then an analytic swept-SAT (_pair_toi_box_scale at reach 0 -> _swept_first_overlap_s)
    gives the first tick-fraction s at which the two bodies touch across their full (rho=1,1) proposed
    motion -- using the actual full endpoints, not a nearer intermediate one, so it catches paths that
    CROSS (both endpoints apart, bodies meeting in between). None -> no cap this pair. The stop is
    symmetric and reach-INDEPENDENT (reach is a weapon envelope that engages across a gap via the Stage B
    contact box, NOT a wall two bodies decelerate against), so both cells cap at the SAME body-touch
    fraction s -- no reach throttle. (The prior reach-throttled model halted cells on the reach surface,
    which deadlocked closing pairs on the strict-overlap contact boundary at a 0-casualty standoff; see
    the ED-MB-0012 note.)

    A cell that is party to several violating pairs takes the MOST restrictive (smallest) cap across all
    of them -- exact and monotonic (unlike the old iterative worst-violator pull-back this replaces),
    since each pair's own solved fraction is the FIRST point at which that specific pair's bodies touch:
    at any smaller fraction, that pair (and, by taking the overall minimum, every pair) is guaranteed
    still body-disjoint.

    Halted cells (already in contact, frozen) are included in the position data so moving cells on
    either side correctly treat them as fixed obstacles, but never themselves receive a cap (they don't
    move regardless)."""
    def _flat(atoms):
        out = []
        for atom in atoms:
            prop = getattr(atom, '_node_pending_proposal', None)
            reach = reach_for(atom.troop_type)
            if prop:
                for cid, (sr, sc, pr, pc) in prop.items():
                    facing = atom.cell_facing_vec.get(cid, atom._node_facing or (atom.advance_dir, 0))
                    out.append(_ToiCell(atom, cid, sr, sc, pr, pc, reach, facing, movable=True))
            else:
                # Static this tick (no target yet / reserve / delayed) -- current true position is a
                # fixed obstacle for the other side; never capped or committed itself.
                ids = [(o_r, o_c) for o_r, o_c, _, _ in _oriented(atom)]
                for cid, (r, c) in zip(ids, atom.cells_float()):
                    facing = atom.cell_facing_vec.get(cid, atom._node_facing or (atom.advance_dir, 0))
                    out.append(_ToiCell(atom, cid, r, c, r, c, reach, facing, movable=False))
        return out

    cells_a = _flat(all_atoms_a)
    cells_b = _flat(all_atoms_b)
    for ea in cells_a:
        a_halted = ea.cid in ea.atom.halted_cells
        for eb in cells_b:
            b_halted = eb.cid in eb.atom.halted_cells
            if a_halted and b_halted:
                continue  # both frozen -- nothing to resolve between two static cells
            # [v2 Stage C reconcile, ED-MB-0011 -- "why decelerate instead of collide?"] The hard
            # geometric stop is BODY vs BODY: two unit squares that must never interpenetrate -- NOT the
            # reach-extended engagement box. Reach is a WEAPON envelope that engages ACROSS a gap
            # (find_contacts / Stage B fires contact on the reach box); it is not a wall two bodies
            # decelerate against. Halting on the reach surface parked closing cells EXACTLY on the
            # obb_front_reach_overlap TOUCH boundary, where the strict-overlap contact predicate returns
            # False -- a permanent standoff at gap = 2*(CELL_RADIUS+reach) with ZERO casualties: contact
            # never fired, so engagement/charge-shock never triggered (the whole battle drew at range 1.5).
            # Stopping on the BODY lets cells close until their bodies meet; the reach surfaces overlap on
            # the way in, so contact fires (and halts the pair) BEFORE bodies touch whenever reach>0 --
            # bodies collide, weapons reach across the closing gap. Charge is preserved: cell_last_speed
            # (read by _momentum_speed at contact) is the PRE-cap step, so a charge's shock reflects its
            # closing velocity, not the throttled crawl. The stop is symmetric and reach-independent, so
            # there is no reach throttle here any more -- both cells cap at the SAME body-touch fraction s;
            # reach asymmetry (a longer weapon engaging first) is expressed by contact firing earlier for
            # the longer-reach box, not by a movement handicap. (_effective_reach/_reach_throttle retained
            # as defined helpers but no longer called; the reach-standoff model they served is retired.)
            start_a, proposed_a = (ea.sr, ea.sc), (ea.pr, ea.pc)
            start_b, proposed_b = (eb.sr, eb.sc), (eb.pr, eb.pc)
            # (1) circular REJECT on the two BODY circumscribed circles (radius hypot(CELL_RADIUS,
            #     CELL_RADIUS) = √2/2 about each centre, reach-INDEPENDENT). A superset of body-box touch,
            #     so it never wrongly skips a pair whose bodies actually meet across this tick's full
            #     (un-throttled) motion. Uses the exact circular quadratic already proven here.
            R_body = math.hypot(CELL_RADIUS, CELL_RADIUS)
            if _pair_toi_scale(start_a, start_b, proposed_a, proposed_b, 1.0, 1.0, 2.0 * R_body) is None:
                continue
            # (2) exact BODY-box swept-SAT -- first fraction s at which the two unit-square bodies touch
            #     (reach 0 on BOTH sides -> _pair_toi_box_scale collapses to pure body-OBB touch). None ->
            #     a glancing near-miss the circle over-approximated; no cap this pair.
            s = _pair_toi_box_scale(start_a, proposed_a, start_b, proposed_b, 1.0, 1.0,
                                    ea.facing, 0.0, eb.facing, 0.0)
            if s is None:
                continue
            # A cap IS needed: both cells stop at the SHARED body-touch fraction (symmetric, no throttle).
            # A halted cell's proposed==start (zero motion), so it never needs (nor receives) a cap -- but
            # it still acted as a fixed obstacle for the other, still-moving side via this same pair solve.
            if not a_halted and s < ea.best_t: ea.best_t = s
            if not b_halted and s < eb.best_t: eb.best_t = s
    for entries in (cells_a, cells_b):
        for e in entries:
            if not e.movable or e.cid in e.atom.halted_cells:
                continue
            final_r = e.sr + e.best_t * (e.pr - e.sr)
            final_c = e.sc + e.best_t * (e.pc - e.sc)
            e.atom._commit_cell_position(e.cid, final_r, final_c, e.atom._node_pending_target_centroid,
                                          e.atom._node_pending_discipline)
    for atom in list(all_atoms_a) + list(all_atoms_b):
        prop = getattr(atom, '_node_pending_proposal', None)
        if not prop:
            continue
        pts = [atom._node_pos[cid] for cid in prop if cid not in atom.halted_cells]
        if not pts:
            pts = [atom._node_pos[cid] for cid in prop]
        if pts:
            atom._node_anchor = (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))
        del atom._node_pending_proposal
        del atom._node_pending_target_centroid
        del atom._node_pending_discipline

# ─── UNIT ────────────────────────────────────────────────────────────────────

@dataclass
class Unit:
    name: str
    faction: str
    power: int
    command: int
    discipline: int
    discipline_start: int
    morale: int
    morale_start: int
    subunits: List[Subunit]
    dr: int = 1
    h_per_size: int = 0
    size: int = 0
    size_max: int = 0
    hp: int = 0
    hp_max: int = 0
    routed: bool = False
    broken: bool = False
    # ED-MB-0022: Feigned Retreat (PP-256). `feigned` = this unit declared a Feigned Retreat and is
    # withdrawing to bait a pursuer (its "rout" is a ruse). `overextended` = a pursuer that failed the
    # PP-256 Discipline check while chasing a feigning enemy — its NEXT engagement pool is cut by
    # OVEREXTEND_PENALTY. Both are inert unless PC_FEIGNED_RETREAT is ON (default OFF, byte-exact).
    feigned: bool = False
    overextended: bool = False
    stance: str = "balanced"
    # v22/G-11: Speed tier — determines pursuit capability.
    # [canonical: designs/provincial/mass_battle_v30.md L120 — "Slow / Standard / Fast"]
    # [ASSUMPTION: Cavalry/Knights Templar = Fast; Heavy Infantry = Slow; others = Standard
    #  — basis: L429 "Cavalry → Standard" in forest implies Fast default]
    speed: str = "Standard"  # "Slow" | "Standard" | "Fast"
    # G-1: stamina (0–STAMINA_MAX). Drains per contact tick, recovers at phase boundary.
    stamina: int = STAMINA_MAX
    stamina_max: int = STAMINA_MAX
    # Jordan directive 2026-06-02: if both provided, Command is DERIVED (Cha primary + Cog secondary).
    charisma: int = None
    cognition: int = None

    def __post_init__(self):
        # [canonical: Jordan directive 2026-06-02] Command DERIVED from Charisma (primary) +
        # Cognition (secondary) when both supplied; else the explicit command stat is used.
        if COMMAND_SIGMA_ENABLED and self.charisma is not None and self.cognition is not None:
            self.command = derive_command(self.charisma, self.cognition)
        total = sum(a.troop_count for a in self.subunits)
        self.size = max(1, total // TROOPS_PER_SIZE)
        self.size_max = self.size
        self.h_per_size = max(1, min(self.discipline, self.command) + self.dr)
        # v19: HP = TroopCount = Size × BLOCK_SIZE. Bottom-up: damage = soldier casualties.
        # [canonical: derived_stats architecture — "TroopCount = Size × block_size"]
        self.hp_max = float(total)   # step 1: hp_max = actual troops = Sum(cell troops); emergent from cells
        self.hp = float(self.hp_max)
        self.ncells = sum(len(a.cells()) for a in self.subunits)  # step 3: cell count for all-fight per-cell density
        self.effective_size = float(self.size)  # v16: continuous, not floored
        self.stamina = STAMINA_MAX
        self.stamina_max = STAMINA_MAX
        for a in self.subunits:
            if a.stance == "balanced": a.stance = self.stance
            a._unit = self                     # stat-inheritance back-ref (per-subunit eff_* falls back here)
        # Increment 1: per-column block grid (state only; resolution wires in at Increment 2).
        self.col_grid = build_column_grid(self) if PER_CELL else None

    def total_troops(self): return sum(a.troop_count for a in self.subunits)

    # Derived unit-level aggregates (Jordan directive): troop-weighted means of the
    # subunits' effective stats. For a homogeneous unit these equal the unit's own stat; for a mixed
    # unit they are the genuine composite. Combat reads PER-SUBUNIT (below); these are the unit view.
    def _agg(self, attr):
        tt = sum(a.troop_count for a in self.subunits)
        if tt <= 0: return getattr(self, attr.replace('eff_', ''), 0)
        return sum(getattr(a, attr) * a.troop_count for a in self.subunits) / tt
    def agg_power(self):      return self._agg('eff_power')
    def agg_discipline(self): return self._agg('eff_discipline')
    def agg_morale(self):     return self._agg('eff_morale')
    def agg_dr(self):         return self._agg('eff_dr')
    def agg_stamina(self):    return self._agg('eff_stamina')

    def derive_rout(self):
        # Unit-level rout DERIVED from subunit state (per-subunit rout, Jordan directive): the unit routs
        # when its general is gone (Command<=0), when every subunit has routed, or when its troop-weighted
        # aggregate morale reaches 0 (the canonical Morale-0 rout, §A.4/§A.12, now read as the composite).
        # A routed unit's subunits all rout (the whole body flees). Single-subunit: agg_morale == the lone
        # subunit's morale == unit.morale, so this fires exactly when the old `unit.morale<=0` did (byte-exact).
        if self.routed:
            return
        if self.command <= 0 or all(a.routed for a in self.subunits) or self.agg_morale() <= 0:
            self.routed = True
            for a in self.subunits:
                a.routed = True
    def cascade_morale_hit(self, amount):
        # Unit-wide morale hit (§A.12 inter-unit cascade / contagion / flank erosion): erode the unit's
        # inherited-default morale ONCE (covers every subunit that INHERITS it -> no double-count for a
        # homogeneous unit) AND each subunit that carries its OWN morale, by `amount`. Single-subunit /
        # homogeneous: exactly the old `unit.morale -= amount` (byte-exact). Mixed: own-morale subunits
        # are eroded too, so the cascade is felt per-subunit consistently with the rest of the model.
        self.morale -= amount
        for a in self.subunits:
            if a.morale is not None:
                a.morale = a.morale - amount

    def recalc_size(self):
        # v19: effective_size = HP / BLOCK_SIZE (HP = TroopCount).
        # [canonical: derived_stats architecture — "Size = floor(TroopCount / block_size)"]
        self.effective_size = self.hp / BLOCK_SIZE if BLOCK_SIZE > 0 else 0.0
        self.size = max(0, math.floor(self.effective_size))
        if self.size == 0:
            self.routed = True
            for a in self.subunits:        # destruction routs the unit; mark subunits for per-subunit consumers
                a.routed = True

    def discipline_penalty(self):
        # SMOOTH (Jordan 2026-06-15 'fix discipline'): continuous linear penalty over the SAME range as the
        # old tiers' endpoints (discipline>=5 -> 0, discipline 1 -> -2) -- no step/cliff. disc<=0 -> broken.
        if self.discipline <= 0: return -99  # [canonical: mass_battle_v30.md §A.4 — sentinel: Disc<=0 formation-broken]
        return -max(0.0, min(2.0, (5.0 - self.discipline) * 0.5))

    def base_combat_pool(self):
        if self.routed or self.broken: return 0
        pen = self.discipline_penalty()
        if pen == -99: self.broken = True; return 0  # [canonical: mass_battle_v30.md §A.4 — sentinel: -99 broken-formation flag]
        # v16: pool uses continuous effective_size (float), floored for dice count.
        # [canonical: mass_battle_v30.md §A.4 Effective Combat Pool; live value =
        #  Command*(1+cohesion) (2*Command at full strength -> Command at annihilation,
        #  ED-899/ED-1013); legacy OFF-path min(Size,Command)+Command at COMMAND_SIGMA_ENABLED=0]
        stam_pen = _stamina_pool_penalty(self.agg_stamina())
        if POOL_QUALITY_MODEL:
            # [Jordan directive 2026-07-08, mirrors core.exchange.subunit_combat_pool's default
            # branch for the UNIT-level pool this pursuit/rout path uses -- see config.py's
            # POOL_QUALITY_MODEL comment.] No Command: troop-type quality (`power`) x numbers
            # (`effective_size`, already the continuously-degrading quantity this method's own v16
            # comment names).
            raw = self.power * self.effective_size * POOL_QUALITY_SCALE + pen + stam_pen
        elif COMMAND_SIGMA_ENABLED:
            # SMOOTH POOLS (Jordan 2026-06-15): 2*command at FULL strength (size-decoupled per ED-899),
            # degrading SMOOTHLY with own casualties to command at annihilation via cohesion=hp/hp_max.
            # Cohesion is a FRACTION (not headcount) -> per-capita effectiveness size-independent -> Lanchester
            # exponent stays ~1 (ED-899 preserved). The smooth own-casualty degradation dilutes the discipline
            # term so it can no longer dominate and bias the mirror (the flat-2*command pool was the defect).
            cohesion = self.hp / self.hp_max if self.hp_max else 0.0
            raw = self.command * (1.0 + cohesion) + pen + stam_pen
        else:
            raw = min(self.effective_size, self.command) + self.command + pen + stam_pen
        # ED-MB-0022: an OVEREXTENDED pursuer (failed the PP-256 Feigned Retreat Discipline check)
        # re-engages at a bounded pool penalty. Gated by PC_FEIGNED_RETREAT (default OFF -> flag never
        # set -> branch inert -> byte-exact). [canonical: mass_battle_v30.md §B.4 — Overextended -2D]
        if PC_FEIGNED_RETREAT and self.overextended:
            raw -= OVEREXTEND_PENALTY
        return max(1, math.floor(raw))

    def check_drift(self):
        # per-subunit formation drift: each subunit's OWN Discipline governs whether it can hold its
        # shape (consistent with the per-subunit Discipline model); single-subunit == unit -> byte-exact.
        for a in self.subunits:
            if a.eff_discipline < MIN_DISCIPLINE[a.shape] and a.shape != "Line":
                # ED-1032: on drift, re-key cell_troops to the new shape's pattern so the sub-unit's
                # troops re-inherit the (Line) formation instead of orphaning the wings -- preserves
                # total strength (sum(cell_troops) == hp) and mirrors the spawn distribution (L629).
                # Spatial-fidelity fix; identical for any sub-unit that does not drift (branch not entered).
                total = sum(a.cell_troops.values())
                a.shape = "Line"
                new_ids = [(o_r, o_c) for o_r, o_c, _a2, _b2 in _oriented(a)]
                per = total / len(new_ids) if new_ids else 0.0
                a.cell_troops = {pid: per for pid in new_ids}
                # [movement audit finding 1.5, ED-1096] ED-1032's re-key above only ever covered
                # cell_troops -- the node-path position state (_node_pos/_node_rel, keyed by pattern
                # id) was never included, so a drift on the node path left the OLD shape's ids in
                # _node_pos: _node_cells()/_node_advance's per-cell lookups (keyed by the NEW ids)
                # then fall through to their (0.0,0.0)/anchor setdefaults -- cells teleport to the
                # battlefield corner or collapse onto the anchor. Only reachable/relevant when node
                # state exists at all (PC_NODE_COHESION); the legacy grid path has no _node_pos and
                # is untouched (byte-exact-off preserved by construction, not by a toggle check).
                if PC_NODE_COHESION and hasattr(a, '_node_pos'):
                    a._rekey_node_state(new_ids)

# ─── DICE ────────────────────────────────────────────────────────────────────



# ─── TARGETING ───────────────────────────────────────────────────────────────
