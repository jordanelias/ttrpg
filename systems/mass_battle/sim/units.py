"""
systems/mass_battle/sim/units.py — Unit / Subunit dataclasses for mass-battle resolution

Canon source: systems/mass_battle/mass_battle_v30.md §A.3 (Company scale + block_size),
              §A.4 (Discipline, Combat Pool, Stamina); designs/scene/derived_stats_v30.md
              (TroopCount / block_size); tests/sim/sim_mb_06_v22.py (lines 697–1035)
Params source: params/mass_combat.md
Game Design constraints applicable: GD-1
Status: [CANONICAL — Phase 7 bare port from sim_mb_06_v22 2026-05-18]

Bare-port of v22 dataclasses per `mass_battle_integration_v30.md §4.1 Step 1`:
  copy v22 → massbattle.py + extract Unit / Subunit → units.py.

Module-level constants (TROOPS_PER_TIER, STAMINA_MAX, etc.) and helper functions
(oriented_pattern, cell_speed, _stamina_pool_penalty) live in `massbattle.py`.
This module late-binds to them via `_mb` to avoid circular import — Python's
import machinery resolves these names at method-call time, not import time.

Dependencies:
  - systems/mass_battle/sim/massbattle — constants + cell-pattern/speed/stamina helpers (late-bound)

Entry points:
  - Subunit  — atomic combat unit (shape + tier + cells)
  - Unit     — multi-subunit combat formation (power/command/discipline/morale)
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

# Late-bound import — Subunit/Unit methods access massbattle module-level
# names via _mb.NAME. At import time _mb may be a partially-loaded module
# (massbattle imports units from its tail); at method-call time massbattle
# is fully loaded. See module docstring.
from systems.mass_battle.sim import massbattle as _mb


@dataclass(eq=False)
class Subunit:
    # eq=False: fall back to object identity __eq__/__hash__. Required because
    # target_atom holds a direct Subunit reference (assign_targets, massbattle.py
    # L619/622/627/630), and after both sides are populated A.target_atom→B and
    # B.target_atom→A form a cycle; default field-walking __eq__ recurses.
    # target_atom is set-by-reference and never compared by value throughout
    # the engine (verified: no `subunit == subunit` call sites; sets/dicts
    # already use id() — massbattle.py L749-750).
    # [canonical: systems/mass_battle/mass_battle_integration_v30.md §4.1
    #  PROVISIONAL flex — call-signature flex licensed where statistical
    #  equivalence holds; identity-eq does not change observable outcomes]
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

    @property
    def troop_count(self): return _mb.TROOPS_PER_TIER[self.tier]

    def cells(self):
        op = _mb.oriented_pattern(self.shape, self.tier, self.advance_dir)
        result = []
        for orig_r, orig_c, or_r, or_c in op:
            abs_r = (self.starting_position[0] + or_r
                     + self.cell_offsets.get((orig_r, orig_c), 0) * self.advance_dir)
            abs_c = (self.starting_position[1] + or_c
                     + self.cell_offsets_c.get((orig_r, orig_c), 0))
            result.append((abs_r, abs_c))
        return result

    def centroid(self):
        c = self.cells()
        if not c: return self.starting_position
        return (sum(r for r, x in c) / len(c), sum(x for r, x in c) / len(c))

    def advance_cells(self, discipline, target_centroid, enemy_cells=None):
        """
        enemy_cells: set of abs (r,c) positions of all enemy cells.
        v11: cap each cell's advance to bring it to adjacency (distance=1) but not past
        the nearest enemy cell. Prevents over-run that produces paradoxical angles.
        [canonical: Jordan design — vector halt at first adjacency]
        """
        if self.stance == "hold": return
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
        op = _mb.oriented_pattern(self.shape, self.tier, self.advance_dir)
        disc_mult = 1.0 if discipline >= 5 else (0.7 if discipline >= 3 else 0.4)
        stance_mod = _mb.STANCE_SPEED_MOD[self.stance]
        all_speeds = [_mb.cell_speed(self.shape, self.tier, r, c) for r, c, _, _ in op]
        nonzero_speeds = [s for s in all_speeds if s > 0]
        min_speed = min(nonzero_speeds) if nonzero_speeds else 0
        for orig_r, orig_c, or_r, or_c in op:
            if (orig_r, orig_c) in self.halted_cells: continue
            base_speed = _mb.cell_speed(self.shape, self.tier, orig_r, orig_c)
            if base_speed == 0: continue
            # [DG-10 fix, 2026-07-22, ED-MB-0011 — "subunits aren't moving when they have previously" /
            #  "if it's broken and not commensurate with system, disable" / "fields, not grids. no grids."]
            # The old `math.floor(base_speed * disc_mult)` grid-snapped any sub-Discipline-5 body's
            # velocity to 0 (floor(1*0.7)=0) and the `== 0: continue` then FROZE it in place, so
            # levy/light_inf/heavy_inf/archers/crossbow/sling/artillery (all disc<5 in §B.2) never
            # advanced to contact. This is the wired engine's copy of the coordinate-field engine's
            # DG-10 freeze (fixed there the same day). This engine holds INTEGER cell positions —
            # contact detection is set-membership on integer coords — so it CANNOT carry a true sub-cell
            # field velocity (0.4/0.7 cells/tick) the way the coordinate-field engine can; representing
            # that on the grid would need either the fractional-velocity accumulator (Jordan rejected:
            # "what even is the point of the continuous velocity accumulator?") or float positions (which
            # break integer contact). So the honest non-breaking unfreeze here is a CLAMP to the grid's
            # minimum quantum: an advancing body takes at least one whole cell instead of a frozen zero.
            # DISCLOSED COST (verified by an adversarial pass): this FLATTENS the sub-Discipline-5 speed
            # gradient — disc 1/2/3/4 all advance at 1 cell/tick here, where the field engine keeps
            # 0.4/0.4/0.7/0.7. A faithful sub-cell gradient on this engine is out of scope until the
            # field↔grid reconciliation (ED-IN-0074 D5) — the field engine is the faithful one; this is
            # a stopgap that trades the sub-disc-5 speed curve for un-freezing the wired engine at all.
            # Discipline>=5 (incl. the wired resolve_mass_battle default of 5) is UNCHANGED bit-for-bit
            # (round(1.0)=1 == floor(1.0)); an adversarial A/B (incl. mid-battle degradation and volley-
            # under-approach) found no disc>=5 outcome that differs, since degradation lags contact when
            # movement is already moot. NOT an accumulator.
            vel = base_speed * disc_mult + stance_mod
            if vel <= 0: continue                      # 'hold' (stance_mod -99) / non-advancing → no move
            actual_speed = max(1, round(vel))          # clamp to >=1 cell: unfreeze, not faithful sub-cell velocity
            if _mb.TIP_SUPPORT_ENABLED and base_speed > min_speed:
                current_offset = self.cell_offsets.get((orig_r, orig_c), 0)
                slow_offsets = [
                    self.cell_offsets.get((r2, c2), 0)
                    for r2, c2, _, _ in op
                    if _mb.cell_speed(self.shape, self.tier, r2, c2) == min_speed
                ]
                if slow_offsets and current_offset >= min(slow_offsets) + _mb.TIP_SUPPORT_GAP:
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
            if cell_target:
                dr = cell_target[0] - my_r
                dc = cell_target[1] - my_c
                if self.stance == "retreat": dr, dc = -dr, -dc
                abs_dr, abs_dc = abs(dr), abs(dc)
                total = abs_dr + abs_dc
                if total < 0.5: continue
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
            # F-ii: record speed when cell actually moves
            self.cell_last_speed[(orig_r, orig_c)] = actual_speed
            # v11: record raw movement vector for octagon angle
            self.cell_facing_vec[(orig_r, orig_c)] = (
                r_step if cell_target else actual_speed * self.advance_dir,
                c_step if cell_target else 0,
            )
            # v13: mark cell as having moved this turn (for cross-side contention)
            self._moved_this_turn.add((orig_r, orig_c))

    def get_cell_facing(self, orig_r, orig_c):
        """Return the facing vector for a cell. Defaults to advance_dir if never moved."""
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
            sizes = {1: 2, 2: 2, 3: 3, 4: 3}
            wing_w = sizes.get(self.tier, 3)
            if contact_col == wing_w + self.starting_position[1]: return "center"
            return "flank_engaged"
        if self.shape == "GappedLine":
            # [canonical: v11 — updated to match equalized gapped_line_cells sizes]
            sizes = {1: 2, 2: 3, 3: 4, 4: 4}
            half_w = sizes.get(self.tier, 4)
            if contact_col == half_w + self.starting_position[1]: return "gap"
            return "flank_engaged"
        if self.shape == "RefusedFlank":
            sizes = {1: 3, 2: 4, 3: 5, 4: 6}
            width = sizes.get(self.tier, 6)
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
        op = _mb.oriented_pattern(self.shape, self.tier, self.advance_dir)
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

@dataclass(eq=False)
class Unit:
    # eq=False: see Subunit decorator above. Unit.subunits is List[Subunit]
    # and would walk into the Subunit cycle if Unit.__eq__ were generated.
    # Identity semantics are correct for both classes — Units are mutable
    # state containers, not value objects.
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
    # [canonical: systems/mass_battle/mass_battle_v30.md L120 — "Slow / Standard / Fast"]
    # [ASSUMPTION: Cavalry/Knights Templar = Fast; Heavy Infantry = Slow; others = Standard
    #  — basis: L429 "Cavalry → Standard" in forest implies Fast default]
    speed: str = "Standard"  # "Slow" | "Standard" | "Fast"
    # G-1: stamina (0–_mb.STAMINA_MAX). Drains per contact tick, recovers at phase boundary.
    stamina: int = _mb.STAMINA_MAX
    stamina_max: int = _mb.STAMINA_MAX

    def __post_init__(self):
        total = sum(a.troop_count for a in self.subunits)
        self.size = max(1, total // _mb.TROOPS_PER_SIZE)
        self.size_max = self.size
        self.h_per_size = max(1, min(self.discipline, self.command) + self.dr)
        # v19: HP = TroopCount = Size × _mb.BLOCK_SIZE. Bottom-up: damage = soldier casualties.
        # [canonical: derived_stats architecture — "TroopCount = Size × block_size"]
        self.hp_max = self.size_max * _mb.BLOCK_SIZE
        self.hp = float(self.hp_max)
        self.effective_size = float(self.size)  # v16: continuous, not floored
        self.stamina = _mb.STAMINA_MAX
        self.stamina_max = _mb.STAMINA_MAX
        for a in self.subunits:
            if a.stance == "balanced": a.stance = self.stance

    def total_troops(self): return sum(a.troop_count for a in self.subunits)

    def recalc_size(self):
        # v19: effective_size = HP / _mb.BLOCK_SIZE (HP = TroopCount).
        # [canonical: derived_stats architecture — "Size = floor(TroopCount / block_size)"]
        self.effective_size = self.hp / _mb.BLOCK_SIZE if _mb.BLOCK_SIZE > 0 else 0.0
        self.size = max(0, math.floor(self.effective_size))
        if self.size == 0: self.routed = True

    def discipline_penalty(self):
        if self.discipline >= 5: return 0
        if self.discipline >= 3: return -1
        if self.discipline >= 1: return -2
        return -99

    def discipline_penalty_volley(self):
        """Volley discipline penalty: returns POSITIVE pool reduction.
        [canonical: mass_battle_v30.md §A.4 Discipline table — Power penalty same for ranged]
        Discipline 5-7: 0; Discipline 3-4: 1; Discipline 1-2: 2; Discipline 0: broken (large).
        """
        if self.discipline >= 5: return 0
        if self.discipline >= 3: return 1
        if self.discipline >= 1: return 2
        return 99

    def base_combat_pool(self):
        if self.routed or self.broken: return 0
        pen = self.discipline_penalty()
        if pen == -99: self.broken = True; return 0
        # v16: pool uses continuous effective_size (float), floored for dice count.
        # [canonical: mass_battle_v30.md §A.4 — "Effective Combat Pool =
        #  min(Size, Command) + Command"; Size here is continuous from TroopCount]
        stam_pen = _mb._stamina_pool_penalty(self.stamina)
        raw = min(self.effective_size, self.command) + self.command + pen + stam_pen
        return max(1, math.floor(raw))

    def check_drift(self):
        for a in self.subunits:
            if self.discipline < _mb.MIN_DISCIPLINE[a.shape] and a.shape != "Line":
                a.shape = "Line"

# ─── DICE ────────────────────────────────────────────────────────────────────

