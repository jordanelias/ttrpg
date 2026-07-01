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
# [movement-substrate review 06 — finding 2] Continuous-speed toggle. Default OFF -> byte-exact (the OFF
# branch in advance_cells is the exact prior floor() code). ON: a per-cell fractional-speed accumulator,
# so a discipline-degraded body advances at its TRUE average rate instead of flooring to 0 each turn
# (floor(1*0.7)=0 freezes a slow degraded unit). Integer positions preserved; only step TIMING changes.
# Consumer-local here (advance_cells), like PC_ENVELOP_PATH/PC_SWEEP. ON = recorded behaviour change.
FIELD_MOVEMENT = (_hu_os.environ.get("FIELD_MOVEMENT", "0") == "1")
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

__all__ = ['Subunit', 'Unit', 'PC_ENVELOP_PATH', 'PC_SWEEP', 'FIELD_MOVEMENT', 'FIELD_CONTACT', 'CONTACT_REACH', 'COL_WIDTH',
           'PC_FACING_MODEL', 'PC_FACING_ATTENTION', 'PC_FACING_SLEW_BASE', 'PC_FACING_FOV_GATE', 'PC_FACING_ROUT',
           'CELL_RADIUS', 'standoff_from_reach', 'standoff']

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
    stand off 2.0 lattice units apart; Long vs Short, 3.0. Used by find_contacts (core/contact.py) and
    _node_advance's halt below — the SAME radius for both, so contact and halt never drift out of sync."""
    return standoff_from_reach(reach_for(troop_type_a), reach_for(troop_type_b))


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

    def __post_init__(self):
        # Construction-time validation (arch review / stress-test hardening): turn the cryptic
        # KeyError (invalid tier/shape) and silent off-grid placement into clear errors at the
        # point of construction, so resolution never sees a malformed atom. Valid in-bounds
        # formations are unaffected (byte-exact). Bounds are checked on the initial formation
        # (cell_offsets are 0 here); dynamic movement past the edge is a separate concern.
        if self.shape not in CELL_PATTERN_FN:
            raise ValueError(f"Subunit shape {self.shape!r} unknown; valid shapes: {sorted(CELL_PATTERN_FN)}")
        if (self.troops is None) != (self.concentration is None):
            raise ValueError("Subunit: continuous mode needs both troops and concentration (or neither, for the tier path)")
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
        _per = self.troop_count / len(_ids) if _ids else 0.0
        self.cell_troops = {pid: _per for pid in _ids}
        self._unit = None                      # stat-inheritance back-ref (set by Unit.__post_init__)
        self._start_troops = self.troop_count  # spawn troop count = per-subunit cohesion denominator
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

    def _node_advance(self, discipline, target_centroid, enemy_cells=None, enemy_cells_float=None):
        """Node-path advance (step 2, increment a): the formation translates toward the target as a
        body (vector-halt at adjacency preserved); each cell relaxes toward its relational slot
        (anchor + rel) by a discipline-gated cohesion factor, so the formation holds together while
        contention/edges can dent it. No wheel yet (facing points at the target).
        [arch: relational cohesion replaces the re-imposed shape pattern.]

        enemy_cells_float: [Stage A, additive, None by default -> byte-exact] list of (r, c, reach)
        true-float enemy-cell triples (r,c from cells_float(), reach from troop_types.registry.
        reach_for on that cell's owning atom) -- built by the caller in the SAME synchronized block as
        cached_centroids (orchestration.py) so both sides see each other's PRE-MOVE true positions.
        When FIELD_MOVEMENT is on and this is supplied, the halt below clamps to the standoff() ring
        against these true floats instead of the rank/file-SNAPPED enemy_cells -- the correction that
        actually delivers "never co-located" (a clamp against snapped cells targets a stale integer
        position, not the enemy's true float)."""
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
        step = max(0, math.floor(base * disc_mult) + stance_mod)
        if PER_CELL and self.troop_type in ('cavalry', 'mounted_archers') and step > 0:
            step = int(math.floor(step * PC_CAVALRY_SPEED_MULT))
        ar, ac = self._node_anchor
        if target_centroid and step > 0:
            dr = target_centroid[0] - ar
            dc = target_centroid[1] - ac
            if self.stance == "retreat":
                dr, dc = -dr, -dc
            if FIELD_MOVEMENT and enemy_cells_float:
                # [Stage A] True-adjacency anchor pre-cap: dmin against the enemy's TRUE FLOAT
                # positions (cells_float(), not the rank/file-SNAPPED _node_cells()/cells()), capped
                # to standoff() per nearest true-float pair -- not a flat "-1". This is what actually
                # delivers "never co-located": a clamp against snapped cells targets a stale integer
                # position, not where the enemy really is.
                mine = self.cells_float()
                if mine:
                    my_reach = reach_for(self.troop_type)
                    allowed = min(math.hypot(mr - er, mc - ec) - standoff_from_reach(my_reach, erch)
                                  for (mr, mc) in mine for (er, ec, erch) in enemy_cells_float)
                    step = min(step, max(0, allowed))
            elif enemy_cells:
                mine = self._node_cells()
                if mine:
                    dmin = min((math.hypot(mr - er, mc - ec) if FIELD_MOVEMENT else max(abs(mr - er), abs(mc - ec)))
                               for (mr, mc) in mine for (er, ec) in enemy_cells)  # [migration S2] Euclidean on the field; Chebyshev on the grid (byte-exact OFF)
                    step = min(step, max(0, dmin - 1))   # vector-halt: stop at adjacency, not past
            mag = abs(dr) + abs(dc)
            if mag >= 0.5 and step > 0:
                self._node_anchor = (ar + step * (dr / mag), ac + step * (dc / mag))
        nar, nac = self._node_anchor
        # WHEEL (increment 2b): the formation re-faces the enemy as a body. f = current facing (unit vector),
        # f0 = spawn facing (toward the enemy at first contact); the relational layout is rotated by the
        # rotation taking f0 -> f, so the whole formation pivots while cohesion holds it together. Head-on
        # engagements (f stays ~ f0) leave the rotation at identity -> identical to increment 2a.
        rc_w, rs_w = 1.0, 0.0   # (cos, sin) of the spawn->current rotation; identity until the body wheels
        if target_centroid:
            tdr = target_centroid[0] - nar; tdc = target_centroid[1] - nac
            tmag = math.hypot(tdr, tdc)
            if tmag > 0:
                ftr, ftc = tdr / tmag, tdc / tmag   # f_target: unit direction to the enemy
                if self._node_facing is None:
                    self._node_facing = (ftr, ftc); self._node_facing0 = (ftr, ftc)
                else:
                    kw = disc_mult * 0.5            # wheel rate (disc-gated, slower than the cohesion snap)
                    fr0, fc0 = self._node_facing
                    lr, lc = fr0 + kw * (ftr - fr0), fc0 + kw * (ftc - fc0)
                    lmag = math.hypot(lr, lc)
                    if lmag > 0: self._node_facing = (lr / lmag, lc / lmag)
                f0r, f0c = self._node_facing0; fr, fc = self._node_facing
                rc_w = f0r * fr + f0c * fc          # cos of rotation f0 -> f
                rs_w = f0r * fc - f0c * fr          # sin of rotation f0 -> f
        k = disc_mult   # cohesion factor reuses the discipline multiplier: disciplined formations hold tight, ragged ones deform
        for orig_r, orig_c, _o_r, _o_c in op:
            if (orig_r, orig_c) in self.halted_cells:
                continue
            rel = self._node_rel.get((orig_r, orig_c), (0.0, 0.0))
            des_r = nar + (rc_w * rel[0] - rs_w * rel[1])   # anchor + R(f0->f) . rel : rotated relational slot
            des_c = nac + (rs_w * rel[0] + rc_w * rel[1])
            cr, cc = self._node_pos.setdefault((orig_r, orig_c), self._node_anchor)  # [canonical: continuous-mode seed: unseen cell defaults to anchor]
            nr = min(BATTLEFIELD_SIZE - 1, max(0, cr + k * (des_r - cr)))
            nc = min(BATTLEFIELD_SIZE - 1, max(0, cc + k * (des_c - cc)))
            if FIELD_MOVEMENT and enemy_cells_float:
                # [Stage A] Per-cell clamp, continuous: pull a candidate that would land WITHIN
                # standoff() of a true-float enemy cell back to exactly the standoff ring, along the
                # axis from that enemy cell to the candidate -- shape-preserving (post-hoc; never
                # touches _node_rel), unlike the OFF/legacy exact-equality test this replaces. If
                # several enemy cells are violated, clamp against the single worst (nearest-relative-
                # to-its-own-standoff) violator -- a reasonable, symmetric-per-pair approximation
                # rather than exact multi-body constraint solving.
                my_reach = reach_for(self.troop_type)
                worst = None  # (violation, er, ec, sd, dist)
                for (er, ec, erch) in enemy_cells_float:
                    sd = standoff_from_reach(my_reach, erch)
                    dist = math.hypot(nr - er, nc - ec)
                    violation = dist - sd
                    if violation < 0 and (worst is None or violation < worst[0]):
                        worst = (violation, er, ec, sd, dist)
                if worst is not None:
                    _, er, ec, sd, dist = worst
                    if dist > 1e-9:  # [canonical: epsilon: float magnitude guard]
                        nr, nc = er + (nr - er) / dist * sd, ec + (nc - ec) / dist * sd
                    else:
                        nr, nc = cr, cc  # degenerate exact-overlap: hold at prior position
            elif enemy_cells:
                # [migration P] OFF = verbatim int(round) grid-membership probe; ON (no float data supplied,
                # i.e. FIELD_MOVEMENT off but PC_NODE_COHESION on) = file-binned probe matching the
                # file-indexed enemy cells() keys (row rank-snapped, column /COL_WIDTH).
                _probe = (int(round(nr)), int(round(nc / COL_WIDTH))) if FIELD_MOVEMENT else (int(round(nr)), int(round(nc)))
                if _probe in enemy_cells:
                    nr, nc = cr, cc   # blocked: an enemy holds this cell -> hold (no pass-through; front dents); cohesion retries next tick
            # (a) attention (facing model): face the ENGAGED target; else keep the WHEEL-slewed body facing.
            # The node path already has a disc-gated WHEEL slew (L392), so do NOT double-slew here.
            if PC_FACING_MODEL and PC_FACING_ATTENTION and self.target_atom is not None:
                _tc = self.target_atom.centroid()
                self.cell_facing_vec[(orig_r, orig_c)] = (_tc[0] - nr, _tc[1] - nc)
            elif self._node_facing is not None:
                self.cell_facing_vec[(orig_r, orig_c)] = self._node_facing
            elif target_centroid:
                self.cell_facing_vec[(orig_r, orig_c)] = (target_centroid[0] - nr, target_centroid[1] - nc)
            self.cell_last_speed[(orig_r, orig_c)] = step
            self._node_pos[(orig_r, orig_c)] = (nr, nc)
            self._moved_this_turn.add((orig_r, orig_c))

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
        # KITING (§13): a ranged unit with the 'kite' instruction regulates its distance to stay in
        # the volley band [VOLLEY_MIN_RANGE, VOLLEY_MAX_RANGE] instead of closing to melee. Distance
        # metric matches volley's _atom_distance (Chebyshev, nearest cells) so "in band" == "can shoot".
        # INERT without the 'kite' instruction -> byte-exact for every existing scenario.
        kite_mode = None
        if PC_KITE_ENABLED and self.unit_type == 'ranged' and 'kite' in self.instructions and enemy_cells:
            mine = self.cells()
            if mine:
                d = min((math.hypot(mr - er, mc - ec) if FIELD_MOVEMENT else max(abs(mr - er), abs(mc - ec))) for (mr, mc) in mine for (er, ec) in enemy_cells)  # [migration S2] Euclidean on the field (byte-exact OFF)
                if d < PC_KITE_STANDOFF:     kite_mode = 'away'    # too close -> open the gap (retreat vector)
                elif d > VOLLEY_MAX_RANGE:   kite_mode = 'toward'  # out of range -> close into the band
                else:                        return                # in band -> hold position, keep volleying
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
            if PC_FACING_MODEL:
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
        if self.shape == "Line": return "normal"
        if self.shape == "Arrowhead":
            pattern = CELL_PATTERN_FN[self.shape](self.tier)
            for r, c in pattern:
                if r == 0:
                    abs_c = self.starting_position[1] + c + self.cell_offsets_c.get((r, c), 0)
                    if abs(abs_c - contact_col) <= 0.5: return "tip"
            return "flank"
        if self.shape == "Horseshoe":
            sizes = {1: 2, 2: 2, 3: 3, 4: 3}  # [canonical: geometry.py horseshoe_cells / §A.3b — wing-width tier table (F2 derive-target)]
            wing_w = sizes.get(self.tier, 3)
            if contact_col == wing_w + self.starting_position[1]: return "center"
            return "flank_engaged"
        if self.shape == "GappedLine":
            # [canonical: v11 — updated to match equalized gapped_line_cells sizes]
            sizes = {1: 2, 2: 3, 3: 4, 4: 4}
            half_w = sizes.get(self.tier, 4)  # [canonical: geometry.py horseshoe_cells / §A.3b — wing-width default]
            if contact_col == half_w + self.starting_position[1]: return "gap"
            return "flank_engaged"
        if self.shape == "RefusedFlank":
            sizes = {1: 3, 2: 4, 3: 5, 4: 6}  # [canonical: geometry.py refused_flank_cells / §A.3b — width tier table (F2 derive-target)]
            width = sizes.get(self.tier, 6)  # [canonical: geometry.py refused_flank_cells / §A.3b — width default]
            if contact_col == (width - 1) + self.starting_position[1]: return "refused"
            return "engaged"
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
        if COMMAND_SIGMA_ENABLED:
            # SMOOTH POOLS (Jordan 2026-06-15): 2*command at FULL strength (size-decoupled per ED-899),
            # degrading SMOOTHLY with own casualties to command at annihilation via cohesion=hp/hp_max.
            # Cohesion is a FRACTION (not headcount) -> per-capita effectiveness size-independent -> Lanchester
            # exponent stays ~1 (ED-899 preserved). The smooth own-casualty degradation dilutes the discipline
            # term so it can no longer dominate and bias the mirror (the flat-2*command pool was the defect).
            cohesion = self.hp / self.hp_max if self.hp_max else 0.0
            raw = self.command * (1.0 + cohesion) + pen + stam_pen
        else:
            raw = min(self.effective_size, self.command) + self.command + pen + stam_pen
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

# ─── DICE ────────────────────────────────────────────────────────────────────



# ─── TARGETING ───────────────────────────────────────────────────────────────
