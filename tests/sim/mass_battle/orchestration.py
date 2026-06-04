# SIM-MB-06 v20 — Continuous TroopCount + G-3 lethality recalibration
# Session: 2026-05-13 | Iteration v19 -> v20
# [canonical: mass_battle_v30.md §A.3 TroopCount/block_size, §A.4 morale triggers,
#  §A.7 battle turn structure, §A.12 rout/pursuit; params/mass_combat.md;
#  derived_stats architecture — TroopCount as granular health pool]
#
# v16 changes (two architectural shifts):
#
#   G-3 CONTINUOUS EFFECTIVE SIZE — HP represents TroopCount at Company scale.
#   effective_size = hp / h_per_size (FLOAT, not floored to integer).
#   Pool formula uses continuous effective_size: a unit at 280/400 troops
#   fights at effective_size 2.8, not Size 2. Pool degrades continuously
#   as casualties mount, producing proportional combat degradation instead
#   of step-function drops at Size boundaries.
#   [canonical: mass_battle_v30.md §A.3/§A.4 — "TroopCount = Size × block_size",
#    "Size = floor(TroopCount / block_size)"; derived_stats architecture
#    from 2026-04-19 session — continuous TroopCount as granular health pool]
#
#   G-3 LETHALITY RECALIBRATION — damage scaled so 3-phase battles (18 ticks)
#   produce ~30% casualties on the losing side. Historical battles ended by
#   rout at 10-30% casualties; 30% chosen as gameplay-appropriate threshold
#   (enough fighting to feel consequential, army survives to fight again).
#   HP = TroopCount; damage = soldier casualties (no scaling).
#   Morale triggers now fire on loss_pct (HP percentage) at 30%/50%, replacing
#   integer-Size-based triggers that were too coarse at Size 4.
#   [canonical: Jordan direction — "3-phase battles should be damaging, not
#    eliminating"; "30% rout threshold, not 10-15%"]
#
#   v15 stamina (G-1) and rout hooks (G-2) retained, now operating in the
#   extended battle timescale where stamina differentiation actually manifests.
#
# v15 (base): stamina drain/recovery, -1 exhaustion pool penalty, phase-boundary
#   morale check, rout resolution. Battery 11/13.
#
# v13 (committed c33aa93aee095df634f6c74f2d116bf6dc7dae6b):
#
#
#   Cross-side cell contention (resolve_cross_side_contention). After both
#   sides advance, cells from opposing sides may end the phase at the same
#   absolute position (over-run). Prior to v13: silent magical co-location.
#   v13: strict speed-differential resolution.
#
#   Rule (per Jordan design 2026-05-12, full spec):
#     "if they were to occupy the same cell, then the troop with higher speed
#      gets priority for taking up that adjacent cell while the other remains
#      in place. if they have the same speed, then the troop with the greater
#      size gets that space. if they are the same size, then it's randomized."
#
#   v13 implementation (conservative subset):
#     - STRICT speed differential only: faster cell wins, loser cells that
#       moved this turn revert to pre-move snapshot.
#     - Tied speed → NO movement resolution (combat decides via engagement).
#     - Size and random tiebreakers DEFERRED until cavalry units exist:
#       applying them per contested position per turn produces battery noise
#       in symmetric matchups without modelling anything historical (equal
#       infantry formations don't resolve by random; they resolve by combat).
#
#   Historical grounding:
#     - Crécy 1346 / Agincourt 1415: English defenders pre-positioned via
#       speed (terrain choice + faster deployment) → French attackers halt
#       at disadvantage. Speed-priority = first to the ground.
#     - Leuctra 371 BC: Epaminondas's oblique order — strong wing advances
#       faster, reaches enemy first, hits before slower wing engages.
#     - Hoplite phalanx mirror (Greek city-state warfare): equal-speed
#       formations meet at adjacency; the push (othismos) decides via
#       combat, not movement priority. → equal-speed → no movement adjust.
#
#   Charge-through (cavalry past static infantry) and end-of-phase
#   displacement (opponent shifts back when overlapping with cavalry) are
#   noted in code but NOT WIRED — no cavalry in current battery.
#   Framework supports: _moved_this_turn tracking, _prev_offsets snapshot,
#   pre-existing cell_last_speed. Wiring requires power × facing inputs.
#
#   Within-side discipline-gated formation hold (Subunit.resolve_internal_
#   collisions) is implemented but NOT INVOKED. Earlier attempt broke battery
#   (12/13 → 9/13) because midpoint-of-two-forward-vectors is still forward
#   in the FAIL case (no effective penalty), and the PASS revert helped only
#   shapes with deep column stacking. Available for v14+ when paired with a
#   proper bad-facing trigger (e.g., wrap-around forcing different facings).
#
# Battery at n=500:
#   12/13 in-band (same as v12; H5 RF vs HS still out at 47.4%, target 50-65%)
#
#   The mechanism fires substantially in asymmetric-speed matchups:
#     H3 HS vs Line: 14 firings/battle (HS wings speed-2 vs Line speed-1)
#     H10 Line vs HS: 8 firings/battle (symmetric to H3)
#     H6 RF vs Line:  4 firings/battle (RF front speed-2 vs Line speed-1)
#   Fires 0 times in equal-speed matchups (H1 Line-Line, H5 RF-HS, H7 GL-Line),
#   per the historical model — equal speeds resolve via combat.
#
# H5 remains the open tension. Speed-priority doesn't address it because
# both sides have speed-2 components (RF front and HS wings). HS's wrap-
# around past RF's footprint isn't a co-location (different columns); it's
# geometry. Deferred to v14: anti-wrap defensive, refused-stub repositioning,
# or depth-ratio pool bonus when enemy extends past own footprint.
#
# v12 changes (5 bottom-up mechanisms, each with historical precedent):
#
#   1. Column-local targeting: each cell maintains its starting column, steers toward
#      target row at that column. Replaces centroid-attractor convergence. Historical:
#      infantry held their assigned file in formation; lateral drift was a sign of
#      breakdown, not engagement. Effect: GappedLine blocks no longer converge (gap
#      stays open). Horseshoe wings don't drift inward. Arrowhead wedge tip leads
#      because wedge cells deploy at different columns already.
#
#   2. VOLLEY_MAX_RANGE 25 → 8: ranged units need to be within 8 cells before firing.
#      Initial deployment is 10 cells apart, so 1-2 turns of approach before volleys
#      begin. Historical: Crécy/Agincourt killing zones were the final 100 paces.
#
#   3. Ranged melee penalty pool//2 → pool//3: archers in close combat were marginal.
#      Historical: Agincourt 1415, Crécy 1346 — archers contributed little to melee
#      after the ranged phase decided.
#
#   4. Volley HP scaling: 1 size loss = ceil(h_per_size/2) hp, not full h_per_size.
#      Ranged "size loss" represents arrows finding targets in formation, many
#      glancing off shields/armor. Melee size loss represents decisive wounds. This
#      single change moved R1 (Ranged vs Line) from 69% to 35%, into 30-50% band.
#
#   5. RefusedFlank front-row speed 2: the engaged side's front rank advances at
#      battle-charge pace, ahead of the deeper rows. Historical: Theban left at
#      Leuctra 371 BC charged in oblique order, front rank striking first. Whole-
#      column speed 2 over-tunes vs Line; front-row-only is the partial momentum
#      bonus that helps vs wide formations (HS) without dominating same-width (Line).
#
# v12 battery at n=500: 12/13 in-band (up from v11's 10/13)
#   In-band: H1, H2, H3, H4, H6, H7, H8, H9, H10, H11, R1, R3
#   Borderline: H5 RefusedFlank vs Horseshoe at 47.4% (target 50-65%, 2.6% below floor)
#
# Tensions carried forward to v13:
#   - H5: RF vs HS wraparound. Mechanism candidates: speed-asymmetric anti-wrap,
#     refused-stub repositioning to flank the engaged column, depth-ratio pool bonus
#     when enemy extends past own footprint. None tried cleanly fix H5 without
#     breaking H6 (vs Line). Likely needs geometry-aware mechanism that distinguishes
#     wider-than-me vs same-width-as-me opponents.
#
# v11 changes (carried, see v11 header for full details):
#   - Atom → Subunit rename, per-cell octagon angle, vector halt-at-contact,
#     GappedLine -99 sentinel removed, ranged melee penalty pool//2.
#
# v10 changes (bottom-up geometric advantages):
#   - Cell counts equalized across shapes at each tier (no shape gets free troops)
#     Was at T3: Line=25, Arrow=25, Horse=25, Gap=56(!), Refused=21
#     Now at T3: all ≈ 25 cells; advantages come from arrangement, not extra cells
#   - SHAPE_OFF_MOD and SHAPE_DEF_MOD RETIRED (flat per-shape bonuses removed entirely; formation effects emerge from geometry)
#   - Shape advantages must emerge from existing geometric mechanisms:
#       support_engage_frac    — wedge concentration via depth-stack support
#       engagement_angle       — flank/rear bonus from facing geometry
#       _momentum_speed        — puncture from speed differential
#       count_engagements      — encirclement penalty from atom-pair count
#   - MIN_DISCIPLINE retained (deployment-validity, not combat modifier)
#   - If a shape's historical advantage doesn't emerge from geometry alone,
#     that's a REAL missing mechanism to add (not a band-aid to re-introduce).

import random, math, statistics, time
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Dict, Set

# [canonical: designs/provincial/mass_battle_v30.md §map — 25×25 grid, 5-cell buffer per side]
from mass_battle.config import *  # P-A: constants extracted to mass_battle/config.py
# [canonical: designs/provincial/mass_battle_v30.md §units — 15×15 cell unit grid fits T4 pattern]
# v20 fix: symmetric deployment. Both sides 7 rows from center (row 12).
# [canonical: designs/provincial/mass_battle_v30.md §deployment]



# [canonical: mass_battle_v30.md §Scale — T1=100(1 size), T2=200(2), T3=400(4), T4=800(8), base 100]

# F-i: Cell support stacking [canonical: Jordan handoff §(1)]
# [canonical: Jordan handoff §(1) — depth-1: full, depth-2: 0.7, depth-3: 0.5, floor 0.3]

# F-ii: Puncture mechanism [canonical: Jordan handoff §(2)]

# F-iii: Cascading resolution [canonical: Jordan handoff §(3)]

# ─── v14: PHASE / TICK STRUCTURE ────────────────────────────────────────────
# A "tick" is one resolution cycle (volley + advance + engagement). A "phase"
# is a block of TICKS_PER_PHASE ticks corresponding to one cavalry charge-and-
# return cycle (approach + gallop + impact + contact + disengage/reform).
# A pre-modern battle is then ~3-6 phases, matching the 30-90 minutes of
# active fighting found in hoplite, medieval, and early-modern accounts.
# [canonical: Jordan design — phase = gallop and charge cycle, ~5-6 ticks per
#  Operational Studies Group's "three-hex charge would take about 5 minutes",
#  with reform-to-position adding 1-2 ticks; hoplite phalanx fighting bounded
#  ~10-15 minutes by exhaustion before rotation/withdrawal]

# ─── TROOP COUNT / BLOCK SIZE (bottom-up lethality) ─────────────────────────
# [canonical: designs/provincial/mass_battle_v30.md §A.3 — "1 Size = block_size soldiers"]
# [canonical: derived_stats architecture (2026-04-19) — "TroopCount = Size × block_size"]
# HP = TroopCount = Size × BLOCK_SIZE. Damage from combat = soldier casualties.
# No LETHALITY_SCALE — casualty rates emerge from pool/TN/DR mechanics directly.
# At Company scale: Size 4 unit = 400 soldiers = 400 HP. Pool=8, ~3 successes/tick
# = ~3 soldiers killed/tick = 0.75%/tick = ~13% per 3-phase turn. Emergent.
import os as _os

# ─── MORALE EROSION (v20 — fully emergent) ───────────────────────────────────
# [canonical: designs/provincial/mass_battle_v30.md §A.4 morale triggers]
# v20: morale eroded by damage_taken / (discipline × command) each tick.
# NO thresholds. Rout point emerges from unit stats:
#   morale 6, damage ~3/tick, disc=5, cmd=4: erosion 3/20 = 0.15/tick
#   morale 6 → 0 in 40 ticks × 0.75%/tick = ~30% casualties to rout.
#   cmd=6: 45% to rout. cmd=2: 15%. Generalship dominance (T1) is structural.
# Morale is now float (accumulates fractional erosion). Rout at morale ≤ 0.
# No morale floor — general's contribution is in the denominator.
# [canonical: designs/provincial/mass_battle_v30.md §A.4 — "Generalship dominates"]

# ─── STAMINA CONSTANTS (G-1) ────────────────────────────────────────────────
# [ASSUMPTION: stamina constants are tuning parameters — basis: no canonical
#  source specifies stamina values; audit G-1 identifies the mechanism gap
#  without prescribing numbers. Validated against battery.]
# v20: stamina drain proportional to cells in contact — emergent from formation.
# v20 fix: 1/cell gives ~8 drain/tick at 8 contact cells → 12.5 ticks to exhaust.
# Historical: front-rank rotation every 2-3 phases (12-18 ticks).
# [ASSUMPTION: drain per contact cell is a tuning parameter]
# Recovery at phase boundary: per reserve rank (rows behind front row).
# Net drain/phase (6 contact ticks × 16 = 96):
#   RF (6 reserve × 8 = 48): net −48/phase. Exhausts mid-phase 3.
#   Line (4 reserve × 8 = 32): net −64/phase. Exhausts early phase 2.
#   HS (3 reserve × 8 = 24): net −72/phase. Exhausts late phase 1.
#   GL (2 reserve × 8 = 16): net −80/phase. Exhausts mid phase 1.
# Pool penalty: only at exhaustion. The differentiation comes from WHEN each
# formation exhausts, not how much worse they get. -1 die when exhausted =
# small but persistent disadvantage that compounds across many ticks.
# Deeper formations recover more → exhaust later → fight at full pool longer.
# G-2 rout-at-threshold constants (phase-boundary morale check for exhausted units)
# [canonical: mass_battle_v30.md §A.4 — morale floor = 1 while general present;
#  G-2 overrides this for exhausted+damaged units at phase boundary]
# [canonical: mass_battle_v30.md §A.4 — cap −3 per Cascade Phase for non-general morale loss]

# ─── DISCIPLINE DEGRADATION WITH CONTINUOUS EFFECTIVE_SIZE (D-6) ─────────
# [canonical: params/mass_combat.md §Discipline Degradation —
#  "Discipline degrades when Size lost > Discipline AND asymmetric"]
# Reinterpreted for continuous: check cumulative HP loss as fraction of
# h_per_size at each phase boundary. Fires when cumulative_loss in eff_size
# terms exceeds 1.0 AND loss is asymmetric. Each time it fires, threshold
# resets (so it can fire again after another 1.0 eff_size loss).
# [ASSUMPTION: threshold 1.0 eff_size maps to "Size lost > 1" in original]

# ─── PHASE-BOUNDARY HOOKS ───────────────────────────────────────────────────
# Called once per phase boundary. Order is canonical:
# stamina → morale → rout → rally → reform → threadwork.
# v15 populates stamina_check, morale_check_phase, rout_resolution.
# rally_check, reform_check, threadwork_check remain empty (future cycles).


def _formation_depth(unit):
    """Max row count across all subunits = number of distinct ranks.
    Deeper formations have more reserve ranks for stamina rotation.
    [canonical: audit_sim_mb_06_v14.md §G-1 — depth permits rotation]"""
    max_depth = 1
    for sub in unit.subunits:
        pattern = CELL_PATTERN_FN[sub.shape](sub.tier)
        if pattern:
            rows = max(r for r, c in pattern) + 1
            if rows > max_depth:
                max_depth = rows
    return max_depth


def _stamina_pool_penalty(stamina):
    """Return pool penalty (negative int) based on current stamina level."""
    if stamina <= 0:
        return STAMINA_EXHAUSTED_POOL_PENALTY
    for threshold, penalty in STAMINA_POOL_THRESHOLDS:
        if stamina >= threshold:
            return penalty
    return STAMINA_EXHAUSTED_POOL_PENALTY


def stamina_check(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """G-1: at phase boundary, recover stamina proportional to formation depth.
    Drain happens per-tick in run_battle; this hook handles rotation recovery.
    [canonical: audit_sim_mb_06_v14.md §G-1 — depth permits front-rank rotation]"""
    for u in [unit_a, unit_b]:
        if u.routed or u.broken:
            continue
        depth = _formation_depth(u)
        reserve_ranks = max(0, depth - 1)
        recovery = STAMINA_RECOVERY_PER_RESERVE_RANK * reserve_ranks
        u.stamina = min(u.stamina_max, u.stamina + recovery)


def morale_check_phase(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """v17: phase-boundary morale = exhaustion pressure ONLY (D-7 fix).
    Per-tick morale handles casualty-based triggers separately.
    Exhausted units lose -1 morale at phase boundary (within cap).
    Floor is NOT overridden here — that's the per-tick trigger's job.
    [canonical: designs/provincial/mass_battle_v30.md §A.4 — morale floor 1 while general present;
     §A.4 — cap −3 non-general morale loss per Cascade Phase]"""
    for u in [unit_a, unit_b]:
        if u.routed:
            continue
        # step 3 (Jordan directive 2026-06-03): canonical Size-fraction morale triggers (§A.4),
        # replacing the per-tick absolute-damage erosion. Routs occur at meaningful casualty levels,
        # not ~98% intact. No general-floor in the unit duel (units rout from their own casualties).
        frac = (u.hp / u.hp_max) if u.hp_max else 1.0
        loss = 0.0
        if frac < 0.50: loss += 1.0    # Size < 50% max -> -1
        if frac < 0.25: loss += 1.0    # Size < 25% max -> -1 additional
        if u.broken: loss += 1.0       # discipline broken (formation gone) -> -1 (canon A.4); broken units rout, not freeze
        if u.stamina <= 0 and u.discipline > 0 and u.command > 0:
            loss += 1.0 / (u.discipline * u.command)   # exhaustion pressure (kept)
        if loss:
            u.morale -= min(loss, 3.0)   # cap -3 per Cascade Phase (§A.4)


def rout_resolution(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """Units with morale ≤ 0 rout.
    [canonical: designs/provincial/mass_battle_v30.md §A.12 —
     "Routing: Slow/Standard cannot fight back."
     "Pursuit: Fast units only. Routing unit loses Size equal to pursuer net
      Offence successes (no Defence) each turn. Recall: Command Ob 2."]
    v19: Standard infantry cannot pursue. Pursuit is a level-2 mechanic
    that fires at the battle-map level when a Fast unit is adjacent.
    Morale Cascade (§A.12): friendly units in same engagement make
    Discipline check Ob 1 on rout — modeled when multi-unit engagements exist."""
    for u, opponent in [(unit_a, unit_b), (unit_b, unit_a)]:
        if u.routed or u.broken:
            continue
        if u.morale <= 0:
            u.routed = True
            # No pursuit damage from Standard infantry (canonical: Fast only).
            # Pursuit damage will be handled at the battle-map level (level 2)
            # when cavalry (G-11) and multi-unit engagements (D-3) are implemented.


def discipline_check_phase(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """v18 (D-6): discipline degradation at phase boundary using cumulative loss.
    [canonical: params/mass_combat.md §Discipline Degradation —
     deterministic, fires when effective_size loss > threshold AND asymmetric]"""
    a_loss = (unit_a.hp_max - unit_a.hp) / BLOCK_SIZE if BLOCK_SIZE else 0
    b_loss = (unit_b.hp_max - unit_b.hp) / BLOCK_SIZE if BLOCK_SIZE else 0
    for u, my_loss, their_loss in [(unit_a, a_loss, b_loss), (unit_b, b_loss, a_loss)]:
        if u.routed or u.broken:
            continue
        # How many full thresholds of loss have we crossed?
        disc_hits = int(my_loss / DISCIPLINE_LOSS_THRESHOLD)
        # How many have we already applied? Track via discipline_start - discipline
        already_applied = u.discipline_start - u.discipline
        if disc_hits > already_applied and my_loss > their_loss:
            u.discipline = max(0, u.discipline - 1)
            u.check_drift()


def rally_check(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """Empty hook — rally lands in a future cycle (G-7)."""
    pass

def reform_check(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """Empty hook — reform lands in a future cycle (G-8)."""
    pass

def threadwork_check(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """Empty hook — threadwork lands in a future cycle (G-9)."""
    pass

def phase_boundary(unit_a, unit_b, phase_idx):
    """Run the phase-boundary hook sequence in canonical order.
    Called every TICKS_PER_PHASE ticks within run_battle."""
    stamina_check(unit_a, unit_b, phase_idx)
    discipline_check_phase(unit_a, unit_b, phase_idx)
    morale_check_phase(unit_a, unit_b, phase_idx)
    rout_resolution(unit_a, unit_b, phase_idx)
    rally_check(unit_a, unit_b, phase_idx)
    reform_check(unit_a, unit_b, phase_idx)
    threadwork_check(unit_a, unit_b, phase_idx)

# v9 Volley (Phase 2 ranged fire) [canonical: mass_battle_v30.md §A.7 Phase 2; PP-503]
# TN for Volley success rolls. Standard d10: TN 6 success rate ≈ 0.5/die.
# [canonical: mass_battle_v30.md §A.7 PP-503 — "TN 6 [PROVISIONAL]"]
# [canonical: mass_battle_v30.md §A.7 PP-503 — "Roll [Power stat] dice"]
# Volley pool = Power dice; not the engagement pool formula.
# Ranged DR table [canonical: params/mass_combat.md §Ranged DR Table — Volley Phase, PP-188]
# Keys: (armour_class) → DR vs Piercing. Sim default: Light armour (DR 1).
# Ranged_DR_None=0, Light=1, Medium=2, Heavy=3 (Piercing column).
# Default DR vs Piercing (ranged) applied to ALL volley targets. Medium-armoured
# infantry (typical Veteran/Professional tier) = DR 2 vs Piercing. Configurable via
# Atom.armour_class in future iterations.
# [canonical: params/mass_combat.md §Ranged DR Table — Medium vs Piercing = 2]
# [canonical: params/mass_combat.md §Ranged DR Table — default DR vs piercing 2]
# Minimum cell-distance for Volley targeting. Distance ≤ 1 = adjacent/melee contact;
# ranged units historically stop firing once enemy closes to hand-to-hand range.
# [canonical: mass_battle_v30.md §A.7 Phase 2 vs Phase 5 — Volley is pre-Engagement;
#  once contact made, units fight in melee not volley]
# v12: VOLLEY_MAX_RANGE reduced from BATTLEFIELD_SIZE (25) to 8.
# Initial deployment is row 5 vs row 15 = 10 cells apart. Range 8 means ranged
# units must close 1-2 cells (or wait for enemy to approach) before volley begins.
# Historical longbow at Crécy/Agincourt: effective fire began ~100 paces (~5 cells)
# but harassment fire extended further. Range 8 captures both regimes.
# Reduces R1 (Ranged vs Line) by ~25% by removing 4-5 turns of free volley.
# [canonical: references/historical/precedents_warfare.md — effective volleys at
#  100-200 paces; killing zone was the final approach to contact]

# [canonical: mass_battle_v30.md §ED-816 shape mods; -99 = structural sentinel (−∞ pool)]
# [canonical: v11 — gap=-99 removed for GappedLine. Gap effect is geometric:
#  no cells at the gap column means no engagement there. Per-cell angles handle
#  the flanking naturally. Structural sentinel only retained where cell is absent.]

# ─── CELL PATTERNS ───────────────────────────────────────────────────────────
# [canonical: mass_battle_v30.md §Shapes — per-tier cell grid dimensions, Jordan design]

from mass_battle.geometry import *  # P-A stage 2: geometry extracted

# ─── ATOM ────────────────────────────────────────────────────────────────────

# P-C scaffold: troop_type→role gating (the FM position→role model). Pure accessors over
# TROOP_TYPE_ROLES; INERT until the instruction→primitive modulation lands. See design §3.5.
def roles_for(troop_type):
    """Roles a troop type may be assigned (its gated menu); falls back to the 'any' menu."""
    return TROOP_TYPE_ROLES.get(troop_type, TROOP_TYPE_ROLES.get("any", []))

def role_allowed(troop_type, role):
    """True iff `role` is in `troop_type`'s gated menu."""
    return role in roles_for(troop_type)


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

    @property
    def troop_count(self):
        return self.troops if self.troops is not None else TROOPS_PER_TIER[self.tier]

    @property
    def charge_pen(self):
        # Increment 5: intrinsic charge penetration (ranks punched through on impact).
        # Cavalry charge is the stubbed mechanic being wired ("noted but not wired").
        # [ASSUMPTION: cavalry charge_pen=3 ranks — basis: real shock-cavalry penetration of
        #  thin lines; absorbed by deep formations (pike/deep infantry). Class-B, Jordan-vetoable.]
        return 3 if self.troop_type == 'cavalry' else 0

    def cells(self):
        op = _oriented(self)
        result = []
        for orig_r, orig_c, or_r, or_c in op:
            abs_r = (self.starting_position[0] + or_r
                     + self.cell_offsets.get((orig_r, orig_c), 0) * self.advance_dir)
            abs_c = (self.starting_position[1] + or_c
                     + self.cell_offsets_c.get((orig_r, orig_c), 0))
            result.append((abs_r, abs_c))
        return result

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
        # KITING (§13): a ranged unit with the 'kite' instruction regulates its distance to stay in
        # the volley band [VOLLEY_MIN_RANGE, VOLLEY_MAX_RANGE] instead of closing to melee. Distance
        # metric matches volley's _atom_distance (Chebyshev, nearest cells) so "in band" == "can shoot".
        # INERT without the 'kite' instruction -> byte-exact for every existing scenario.
        kite_mode = None
        if PC_KITE_ENABLED and self.unit_type == 'ranged' and 'kite' in self.instructions and enemy_cells:
            mine = self.cells()
            if mine:
                d = min(max(abs(mr - er), abs(mc - ec)) for (mr, mc) in mine for (er, ec) in enemy_cells)
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
        disc_mult = 1.0 if discipline >= 5 else (0.7 if discipline >= 3 else 0.4)
        stance_mod = STANCE_SPEED_MOD[self.stance]
        all_speeds = [cell_speed(self.shape, self.tier, r, c) for r, c, _, _ in op]
        nonzero_speeds = [s for s in all_speeds if s > 0]
        min_speed = min(nonzero_speeds) if nonzero_speeds else 0
        for orig_r, orig_c, or_r, or_c in op:
            if (orig_r, orig_c) in self.halted_cells: continue
            base_speed = cell_speed(self.shape, self.tier, orig_r, orig_c)
            if base_speed == 0: continue
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
            if cell_target:
                dr = cell_target[0] - my_r
                dc = cell_target[1] - my_c
                if self.stance == "retreat": dr, dc = -dr, -dc
                if kite_mode == 'away': dr, dc = -dr, -dc  # kiter opens the gap; 'toward' keeps dr,dc (closes in); 'hold' returned above
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

def derive_command(charisma, cognition):
    """Command DERIVED from Charisma (primary weight) + Cognition (secondary weight).
    [canonical: Jordan canon-structure directive] Command = leadership leverage:
    Charisma primary (inspire/hold the line), Cognition secondary (tactical read).
    Weighted mean on the 1-7 scale, rounded and clamped to 1-7 (derived_stats weighting convention).
    """
    w = CMD_CHA_WEIGHT + CMD_COG_WEIGHT
    val = round((CMD_CHA_WEIGHT * charisma + CMD_COG_WEIGHT * cognition) / w)
    # [canonical: params/factions/stats_1_7_scale.md — attributes on the 1-7 scale; Command clamped to it]
    return max(1, min(7, int(val)))


def command_base_pool(command, pen, stam_pen):
    """Command-only base exchange pool (the COMMAND_SIGMA branch): MULT×Command + pool advantages.
    Module-level so the MECHANICS 'command_sigma_base' entry resolves to a real callable rather than
    a bare constant. [canonical: Jordan canon-structure directive — base driven SOLELY by
    Command; Size enters outcomes only via the Lanchester frontage term; MULT=2 matches
    min(Size,Cmd)+Cmd at Size≥Cmd.]"""
    return COMMAND_POOL_MULT * command + pen + stam_pen


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
        # Increment 1: per-column block grid (state only; resolution wires in at Increment 2).
        self.col_grid = build_column_grid(self) if PER_CELL else None

    def total_troops(self): return sum(a.troop_count for a in self.subunits)

    def recalc_size(self):
        # v19: effective_size = HP / BLOCK_SIZE (HP = TroopCount).
        # [canonical: derived_stats architecture — "Size = floor(TroopCount / block_size)"]
        self.effective_size = self.hp / BLOCK_SIZE if BLOCK_SIZE > 0 else 0.0
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
        stam_pen = _stamina_pool_penalty(self.stamina)
        if COMMAND_SIGMA_ENABLED:
            # [canonical: Jordan canon-structure directive 2026-06-02 — base exchange driven
            #  SOLELY by Command (sigma-leverage quality); Size enters outcomes ONLY via the
            #  Lanchester frontage term. Replaces min(Size,Command)+Command (size-dependent →
            #  super-linear melee). pen/stam_pen remain pool-side advantages (sigma head unchanged).]
            raw = command_base_pool(self.command, pen, stam_pen)
        else:
            raw = min(self.effective_size, self.command) + self.command + pen + stam_pen
        return max(1, math.floor(raw))

    def check_drift(self):
        for a in self.subunits:
            if self.discipline < MIN_DISCIPLINE[a.shape] and a.shape != "Line":
                a.shape = "Line"

# ─── DICE ────────────────────────────────────────────────────────────────────

from mass_battle.resolution import *  # P-A stage 4: resolution (sigma head) extracted


# ─── TARGETING ───────────────────────────────────────────────────────────────

def assign_targets(unit_a, unit_b):
    for atom in unit_a.subunits:
        if not unit_b.subunits: atom.target_atom = None; continue
        if atom.order_target_idx is not None and atom.order_target_idx < len(unit_b.subunits):
            atom.target_atom = unit_b.subunits[atom.order_target_idx]
        else:
            my = atom.centroid()
            atom.target_atom = min(unit_b.subunits,
                key=lambda e: math.hypot(my[0]-e.centroid()[0], my[1]-e.centroid()[1]))
    for atom in unit_b.subunits:
        if not unit_a.subunits: atom.target_atom = None; continue
        if atom.order_target_idx is not None and atom.order_target_idx < len(unit_a.subunits):
            atom.target_atom = unit_a.subunits[atom.order_target_idx]
        else:
            my = atom.centroid()
            atom.target_atom = min(unit_a.subunits,
                key=lambda e: math.hypot(my[0]-e.centroid()[0], my[1]-e.centroid()[1]))

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
                n_resolved += 1
            # Loser that didn't move: nothing to revert. The mover (winner) is
            # already at this position; both cells now occupy it. This is the
            # cavalry-charge-through case (handled separately when implemented).
    return n_resolved


def find_contacts(unit_a, unit_b):
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

def count_engagements_per_atom(pairs):
    counts = {}
    for p in pairs:
        counts[id(p["atom_a"])] = counts.get(id(p["atom_a"]), 0) + 1
        counts[id(p["atom_b"])] = counts.get(id(p["atom_b"]), 0) + 1
    return counts

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
            if (comp_r, comp_c) == (abs_r, abs_c):
                speeds.append(atom.cell_last_speed.get((orig_r, orig_c), 0))
                break
    return sum(speeds) / len(speeds) if speeds else 0.0

def _cascade_depth_key(pair):
    """Sub-phase ordering: foremost attacker resolves first.
    [canonical: Jordan handoff §(3) — tip arrives first]"""
    atom_a = pair["atom_a"]
    a_cells = pair["a_cells"]
    if not a_cells: return 999
    if atom_a.advance_dir == -1:
        return min(r for r, c in a_cells)
    return -max(r for r, c in a_cells)

# === SIGMA-LEVERAGE HEAD constants + helpers (prototype, sim-tunable) ===
import os as _sigma_os
# === GRADED MORALE / DAMPED ROUT (Jordan directive 2026-05-31: damp rout, more attrition; morale = inspiration not fact) ===

# === PER-CELL (per-column) COMBAT MODEL — Increment 1: state only (Jordan 2026-05-31) ===
# Diagnostic-settled (ners_verdict_percell_resolution.md, corrected by the 2026-05-31 double-check):
# T3 units carry only ~400 troops, so >=100-troop multi-rank blocks are infeasible. The grid is
# COLUMN-level (frontage columns; each column = density + stamina + depth=rank count), and combat
# (later increments) resolves per column-pair via the CONTINUOUS sigma path (mu-shift, stable at small N).
# PER_CELL OFF reproduces the committed engine (0dea67d1) EXACTLY: the grid is built but unused.
# class-B tunables ported from per_cell_combat.py (validated prototype 75908b9e); Jordan-vetoable
                            # advantage; a separate envelopment delta-sigma double-counts and breaks H4 Cannae.
                            # (NERS-N/E: do not add unneeded apparatus.) _envelopment_sigma retained, dormant at 0.
                            # vs a rear-charged / already-shaken defender; the prepared-defence gate below
                            # scales it toward ~0 for a braced+disciplined+deep defender (Waterloo squares:
                            # "virtually impossible for cavalry to break a well-disciplined square"). Applied
                            # to the DEFENDER's morale channel (not the charger's offence — that is the
                            # puncture path, L1733; a charger-offence wiring would double-count it, the
                            # NERS-N/E defect that disabled _envelopment_sigma). [class-B; Jordan-vetoable]
# PC_CHARGE_TICKS RETIRED 2026-06-01: the shock fires only while a momentum differential exists
# (a_mom>b_mom, L1724); once both bodies lock into stationary melee the differential vanishes and the shock
# stops EMERGENTLY (du Picq: the moral impulse is spent once the charge stalls). A separate tick counter was
# redundant apparatus (NERS-E). Window is now emergent from the speed dynamics.
# --- prepared-defence gate (Phase 3; calibrated in Stage-4 vs the C1-C7 historical bands) ---
# Perception model (Jordan 2026-05-31; grounded in visual physiology + military scholarship):
#   human horizontal visual field ~190-210deg -> REAR BLIND ARC ~150deg, visible +/-105deg.
#   Pinning models the attentional lock of an engaged cell separately (fixing-force doctrine).
# Pocket / gap-trap (Polybius: maniple gaps "lured hoplites in... surrounded"; also the concave Cannae pocket):
# an enemy cell that penetrates LEVEL between two of our cells (attackers on both lateral sides, same rank) is
# surrounded -> not refusable. Mirror-safe: parallel lines put attackers AHEAD (a different rank), never beside
# on both flanks; only a penetration into a gap/concavity produces it.
# Oblique-offense ROLL-UP (Leuthen/Leuctra: a concentrated DEEP wing crushes a thinner enemy wing at the point of
# contact). At an in-contact pair, depth is measured PARALLEL to the contact vector for BOTH sides (Jordan's
# vectorized depth). If the attacker's local push-depth exceeds our supporting depth by more than a margin, that
# local superiority rolls the cell up. Fires ONLY where neither wrap nor pocket fired (no double-count) and only
# in contact (a recessed/refused cell that no one is yet in contact with is not rolled up -- this protects a
# deliberately thin Cannae centre). Mirror-safe: equal formations have equal depth, so excess <= 0 everywhere.
PC_ROLLUP_PER_RANK = float(_sigma_os.environ.get('PC_ROLLUP_PER_RANK', '0.4'))  # penalty per rank of depth excess past the margin
PC_ROLLUP_MARGIN   = float(_sigma_os.environ.get('PC_ROLLUP_MARGIN', '1.0'))    # local depth superiority needed before roll-up bites
PC_ROLLUP_REACH    = float(_sigma_os.environ.get('PC_ROLLUP_REACH', '1.6'))     # contact distance (~adjacent incl. diagonal) to be rollable
PC_ROLLUP_CAP      = float(_sigma_os.environ.get('PC_ROLLUP_CAP', '-1.0'))      # floor on the roll-up penalty (octagon RED scale)
# A roll-up is a FLANK phenomenon: you concentrate a wing and roll the enemy line up FROM ITS END (Leuthen,
# Leuctra). The interior of a line is not directly rolled up -- its collapse is a downstream morale consequence.
# So the roll-up penalty bites only on cells at the defender's lateral extreme; a recessed/penetrated centre
# (e.g. a Cannae concave) is handled by the pocket, not the roll-up.
PC_ROLLUP_FLANK_REACH = float(_sigma_os.environ.get('PC_ROLLUP_FLANK_REACH', '1.0'))  # cols from a lateral edge to count as a wing
# A roll-up breaks a still-FORMED but out-massed wing (a deep wing rolling a thinner one by design); it must not
# mop up a cell already attrited to a single rank -- that cell is already losing on troop count, and penalising it
# again double-counts attrition. So the defender cell must retain real depth (>= floor) to be rollable.
PC_ROLLUP_MIN_DEPTH = float(_sigma_os.environ.get('PC_ROLLUP_MIN_DEPTH', '2.0'))  # defender must still have this depth

from mass_battle.percell import *  # P-A stage 3: percell extracted

def _lanchester_strength(contact_cells, unit=None):
    """P-L Linear Law: enemy effective strength IN CONTACT, expressed as engaged
    contact-frontage (distinct contact columns) normalized to ~1 at LANCHESTER_STRENGTH_REF
    so K_LINEAR composes with the canonical exchange scale (PP-233 successes×(1+Power)).
    Frontage-capped BY CONSTRUCTION: contact columns can never exceed the meeting frontage,
    so numerical superiority is a LINEAR edge (via overlap/envelopment), never square.
    Mode-agnostic: contact cells exist under PER_CELL 0 and 1; depletion enters via the
    pool (effective_size→degree) and, under PER_CELL=1, via dead columns leaving contact.
    [spec mb_lanchester_design.md §3a; Lanchester Linear Law = frontage-capped ancient melee.]
    """
    if not contact_cells:
        return 0.0
    n_eng_cols = len(set(c for r, c in contact_cells))
    if unit is not None and getattr(unit, 'ncells', 0):
        tpc = unit.hp / unit.ncells   # all-fight: current per-cell troops (thins as casualties mount)
        return n_eng_cols * (min(tpc, CELL_CAP) / LANCHESTER_DENSITY_REF) / LANCHESTER_STRENGTH_REF
    return n_eng_cols / LANCHESTER_STRENGTH_REF

def resolve_engagements(unit_a, unit_b, pairs, dynamic_facings=None):
    """Resolve all contact pairs.
    F-i: support_engage_frac replaces bare engage_frac.
    F-ii: puncture bonus from momentum differential.
    dynamic_facings: per-cell facing dict for F-iii (None -> default advance_dir)."""
    dmg_a, dmg_b = 0, 0
    eng_counts = count_engagements_per_atom(pairs)
    for p in pairs:
        atom_a, atom_b = p["atom_a"], p["atom_b"]
        a_troops_frac = atom_a.troop_count / unit_a.total_troops()
        b_troops_frac = atom_b.troop_count / unit_b.total_troops()
        a_base = unit_a.base_combat_pool()
        b_base = unit_b.base_combat_pool()

        # F-i: support-stack-adjusted engage_frac
        a_engage_frac = support_engage_frac(atom_a, p["a_cells"])
        b_engage_frac = support_engage_frac(atom_b, p["b_cells"])

        if POOL_VARIANT == "baseline":
            a_pool_raw = a_base * a_troops_frac * a_engage_frac
            b_pool_raw = b_base * b_troops_frac * b_engage_frac
        elif POOL_VARIANT == "C-i":
            a_pool_raw = a_base * a_engage_frac
            b_pool_raw = b_base * b_engage_frac
        elif POOL_VARIANT == "C-ii":
            a_pool_raw = max(a_base * a_engage_frac * 0.5,
                             a_base * a_troops_frac * a_engage_frac)
            b_pool_raw = max(b_base * b_engage_frac * 0.5,
                             b_base * b_troops_frac * b_engage_frac)
        else:
            raise ValueError(f"Unknown POOL_VARIANT: {POOL_VARIANT}")

        a_pool = max(1, math.floor(a_pool_raw))
        b_pool = max(1, math.floor(b_pool_raw))

        # v11: Per-cell octagon angle — replace centroid-to-centroid with per-cell raw vectors
        # [canonical: Jordan design — octagon, GREEN<45°, YELLOW 45-90°, RED≥90°]
        # For each contact cell-pair, compute angle using defender's per-cell facing vector.
        # Average the modifier across all contact cell-pairs per side.
        def _per_cell_angle_mod(defender_subunit, defender_cells, attacker_cells, attacker_subunit=None):
            if not defender_cells or not attacker_cells: return 0
            # Use attacker CENTROID rather than nearest-cell to avoid non-determinism
            # when a defender cell is equidistant between attacker cells (e.g. Arrowhead tip
            # embedded between two Line rows). [canonical: Jordan design]
            atk_cr = sum(r for r,c in attacker_cells) / len(attacker_cells)
            atk_cc = sum(c for r,c in attacker_cells) / len(attacker_cells)
            atk_centroid = (atk_cr, atk_cc)
            mods = []
            op = _oriented(defender_subunit)
            abs_to_orig = {}
            for orig_r, orig_c, or_r, or_c in op:
                abs_r = (defender_subunit.starting_position[0] + or_r
                         + defender_subunit.cell_offsets.get((orig_r, orig_c), 0)
                         * defender_subunit.advance_dir)
                abs_c = (defender_subunit.starting_position[1] + or_c
                         + defender_subunit.cell_offsets_c.get((orig_r, orig_c), 0))
                abs_to_orig[(abs_r, abs_c)] = (orig_r, orig_c)
            seen = set()
            _pc_refuse = PER_CELL and PC_REFUSE
            atk_sorted = sorted(set(attacker_cells)) if _pc_refuse else None
            if _pc_refuse:
                _dcols = [c for (_r, c) in defender_cells]
                _dmin, _dmax = min(_dcols), max(_dcols)
                # F1 structural: envelopers = attacker cells wrapped BEYOND the defender's frontage span
                # (past either flank). Mirror-stable BY CONSTRUCTION — equal-width formations produce NO
                # wrappers, so a frontal/mirror clash incurs no envelopment penalty regardless of integer-
                # movement stagger. Also fixes the enveloper self-flank (F2): the wider side's narrower
                # enemy cannot wrap it, so an enveloper is never penalised for its own inward-rotated facing.
                # F3 (mirror fix): only a NOMINALLY WIDER attacker can wrap. Width = column SPAN (extent)
                # of the static oriented pattern, symmetric under A<->B — a true mirror has equal span ->
                # NO wrappers regardless of dynamic drift (mirror == refuse-off). SPAN not distinct-count, so
                # a gapped formation (GappedLine) is correctly "wide" by its reach.
                _dc = [t[3] for t in op]; _def_front = max(_dc) - min(_dc) + 1
                if attacker_subunit is not None:
                    _op_atk = _oriented(attacker_subunit)
                    _ac = [t[3] for t in _op_atk]; _atk_front = max(_ac) - min(_ac) + 1
                else:
                    _atk_front = _def_front + 1
                if _atk_front > _def_front:
                    _wrappers = [a for a in atk_sorted if a[1] < _dmin or a[1] > _dmax]
                else:
                    _wrappers = []
                # full defender footprint, for vectorized depth resistance: reserves resist the wrap
                # measured along the WRAPPER'S approach vector, not the Y-column (Clausewitz reserves;
                # Jordan's geometric correction). Captured once per call.
                _def_cells = list(defender_subunit.cells())
                _atk_full = list(attacker_subunit.cells())   # full attacker footprint, for roll-up push-depth
            for d_pos in defender_cells:
                if d_pos in seen: continue
                seen.add(d_pos)
                orig = abs_to_orig.get(d_pos)
                facing = (defender_subunit.get_cell_facing(*orig)
                          if orig else (defender_subunit.advance_dir, 0))
                if _pc_refuse:
                    # Envelopment + refusal (fixing-force doctrine). A cell PINNED in front (attacker
                    # engaged adjacent in the front arc) cannot reorient; a flanker outside the cell's
                    # FOV cannot be seen. The cell REFUSES (turns to face -> no penalty) only if NOT
                    # pinned AND it can see the threat; otherwise the rear penalty lands. The threat is a
                    # STRUCTURAL wrapper (attacker beyond the defender frontage) in this cell's REAR.
                    pinned = False
                    for a in atk_sorted:
                        _z, _a = octagon_angle(a, d_pos, facing)
                        if (((a[0]-d_pos[0])**2 + (a[1]-d_pos[1])**2) ** 0.5 <= PC_PIN_REACH
                                and _a < 45.0):
                            pinned = True; break
                    worst_mod = 0; worst_ang = 0.0; worst_pos = None
                    for a in _wrappers:
                        zone, ang = octagon_angle(a, d_pos, facing)
                        if zone == "RED" and PC_ENVELOP_MOD < worst_mod:
                            worst_mod = PC_ENVELOP_MOD; worst_ang = ang; worst_pos = a
                    if worst_mod < 0 and (not pinned) and worst_ang <= FOV_HALF_DEG:
                        worst_mod = 0   # refused: free to turn AND can see the threat
                    if worst_mod < 0:
                        # depth resists the wrap, measured PARALLEL to the wrapper's approach (Jordan):
                        # a flank wrap is blunted by ROW depth, a rear wrap by FILE depth -- not the
                        # Y-column. A cell hit along X no longer draws spurious support from y-1.
                        _cd = _support_along_vector(d_pos, worst_pos, _def_cells)
                        worst_mod *= 1.0 / (1.0 + PC_ENVELOP_DEPTH_RESIST * max(0.0, _cd - 1.0))
                    # pocket / gap-trap: only where the WRAP did not already fire (worst_mod==0). The gap-
                    # flanking maniples sit WITHIN the defender's span (not wrappers), so a cell trapped level
                    # between them gets the pocket; a Horseshoe's concave wings are BEYOND the span (wrappers),
                    # so those cells take the depth-scaled wrap instead — no double-count. Enemy level on BOTH
                    # lateral sides; not refusable. Mirror-safe (parallel lines never put enemies beside on both).
                    if worst_mod == 0:
                        _hl = _hr = False
                        for a in atk_sorted:
                            if abs(a[0] - d_pos[0]) <= 0.5:
                                _dcol = a[1] - d_pos[1]
                                if -PC_POCKET_REACH <= _dcol < 0: _hl = True
                                elif 0 < _dcol <= PC_POCKET_REACH: _hr = True
                        if _hl and _hr:
                            worst_mod = PC_POCKET_MOD
                    # oblique-offense roll-up: fires only where neither wrap nor pocket fired, and the
                    # cell is actually in contact. Depth is measured PARALLEL to the contact vector for
                    # both sides (Jordan); if the nearest attacker's local push-depth out-masses our
                    # supporting depth past the margin, the local concentration rolls the cell up
                    # (Leuthen deep wing vs thin wing). A recessed/refused cell with no attacker in
                    # contact is NOT rolled up -- protects a deliberately thin Cannae centre.
                    if worst_mod == 0:
                        _cols = [c for (_r, c) in _def_cells]
                        _cmn = min(_cols); _cmx = max(_cols)
                        _is_wing = ((d_pos[1] - _cmn) <= PC_ROLLUP_FLANK_REACH
                                    or (_cmx - d_pos[1]) <= PC_ROLLUP_FLANK_REACH)
                        _na = None; _nd = 1e9
                        if _is_wing:
                            for a in atk_sorted:
                                _dd = ((a[0] - d_pos[0]) ** 2 + (a[1] - d_pos[1]) ** 2) ** 0.5
                                if _dd < _nd:
                                    _nd = _dd; _na = a
                        if _na is not None and _nd <= PC_ROLLUP_REACH:
                            _ds = _support_along_vector(d_pos, _na, _def_cells)
                            _ap = _support_along_vector(_na, d_pos, _atk_full)
                            _excess = _ap - _ds
                            if _excess > PC_ROLLUP_MARGIN and _ds >= PC_ROLLUP_MIN_DEPTH:
                                worst_mod = max(PC_ROLLUP_CAP,
                                                -PC_ROLLUP_PER_RANK * (_excess - PC_ROLLUP_MARGIN))
                    mods.append(worst_mod)
                else:
                    zone, _ = octagon_angle(atk_centroid, d_pos, facing)
                    mods.append(ANGLE_DEF_MOD[zone])
            return sum(mods) / len(mods) if mods else 0

        a_angle_mod = _per_cell_angle_mod(atom_a, list(set(p["a_cells"])),
                                           list(set(p["b_cells"])), atom_b)
        b_angle_mod = _per_cell_angle_mod(atom_b, list(set(p["b_cells"])),
                                           list(set(p["a_cells"])), atom_a)
        # === SIGMA-LEVERAGE HEAD (prototype) ===
        # Advantages (octagon angle, puncture, encirclement, ranged-in-melee) enter as a
        # delta-sigma net-boost on the offensive net successes (uniform impact across pool
        # size), NOT as pool modifiers (non-uniform impact). Bare pool above = pure capacity.
        # Spine (degree -> DAMAGE_BY_DEGREE -> casualties) unchanged.
        # [canonical resolution: mass_combat.md §A.4 net-success exchange; sigma math:
        #  params/core.md continuous engine + modifier_system_spec.md §2.1/§3.1]
        ns_a = ns_b = 0.0   # legacy-path default so the mechanical trace can read these uniformly
        if SIGMA_HEAD_ENABLED:
            ns_a = a_angle_mod * SIGMA_PER_D     # a_angle_mod<=0 when A flanked -> A disadvantaged
            ns_b = b_angle_mod * SIGMA_PER_D
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
                        _zb = "GREEN" if b_angle_mod > -0.5 else ("YELLOW" if b_angle_mod > -1.5 else "RED")
                        ns_b += _charge_shock_sigma(unit_b, p["b_cells"], _zb)
                    if b_pen > 0:
                        _za = "GREEN" if a_angle_mod > -0.5 else ("YELLOW" if a_angle_mod > -1.5 else "RED")
                        ns_a += _charge_shock_sigma(unit_a, p["a_cells"], _za)
                    # Reciprocal charge-recoil (the missing historical term): a charge driven home into a
                    # BRACED + deep + disciplined wall shatters the charger (Courtrai/Swiss/Waterloo squares).
                    # Charger = higher-momentum side; recoil scales with the wall's prep (discipline x depth).
                    # Gated by the 'brace' INSTRUCTION -> instruction-less scenarios stay byte-exact. Emergent:
                    # pikes break a cavalry charge, a loose/shallow line is still ridden down.
                    if PC_BRACE_ENABLED:
                        if a_mom > b_mom and _unit_braced(unit_b):
                            ns_a -= PC_CHARGE_RECOIL * _wall_prep(unit_b, p["b_cells"]) * SIGMA_PER_D
                        elif b_mom > a_mom and _unit_braced(unit_a):
                            ns_b -= PC_CHARGE_RECOIL * _wall_prep(unit_a, p["a_cells"]) * SIGMA_PER_D
            if eng_counts.get(id(atom_a), 0) >= 2: ns_a -= ENCIRCLEMENT_PENALTY * SIGMA_PER_D
            if eng_counts.get(id(atom_b), 0) >= 2: ns_b -= ENCIRCLEMENT_PENALTY * SIGMA_PER_D
            if atom_a.unit_type == 'ranged': ns_a += RANGED_MELEE_SIGMA
            if atom_b.unit_type == 'ranged': ns_b += RANGED_MELEE_SIGMA
            ns_a += _morale_sigma(unit_a)    # graded morale effectiveness (du Picq): low morale -> worse exchange
            ns_b += _morale_sigma(unit_b)
            if PER_CELL:    # Increment 3: fatigue of the engaged front (depth-damped) as delta-sigma
                ns_a += _fatigue_sigma(unit_a, set(c for r, c in p["a_cells"]))
                ns_b += _fatigue_sigma(unit_b, set(c for r, c in p["b_cells"]))
            if PER_CELL:    # Increment 6: envelopment — wider side pressures flanks, refused by enemy depth
                env_a = _envelopment_sigma(unit_a, unit_b)   # A wider -> A gets the envelopment bonus
                env_b = _envelopment_sigma(unit_b, unit_a)   # B wider -> B gets it
                ns_a += env_a
                ns_b += env_b
            a_net = roll_pool(a_pool) + _sigma_net_boost(ns_a, a_pool)
            b_net = roll_pool(b_pool) + _sigma_net_boost(ns_b, b_pool)
        else:
            # === LEGACY POOL-MODIFIER PATH (baseline; advantages modify the pool) ===
            a_pool = max(1, a_pool + round(a_angle_mod))
            b_pool = max(1, b_pool + round(b_angle_mod))
            if PUNCTURE_ENABLED:
                a_mom = _momentum_speed(atom_a, p["a_cells"])
                b_mom = _momentum_speed(atom_b, p["b_cells"])
                if a_mom > b_mom:   a_pool += min(PUNCTURE_CAP, int(a_mom - b_mom))
                elif b_mom > a_mom: b_pool += min(PUNCTURE_CAP, int(b_mom - a_mom))
            if eng_counts.get(id(atom_a), 0) >= 2: a_pool = max(1, a_pool - ENCIRCLEMENT_PENALTY)
            if eng_counts.get(id(atom_b), 0) >= 2: b_pool = max(1, b_pool - ENCIRCLEMENT_PENALTY)
            if atom_a.unit_type == 'ranged': a_pool = max(1, a_pool // 3)
            if atom_b.unit_type == 'ranged': b_pool = max(1, b_pool // 3)
            a_net = roll_pool(a_pool)
            b_net = roll_pool(b_pool)
        a_deg = compute_degree(a_net, max(1, b_net))
        b_deg = compute_degree(b_net, max(1, a_net))
        if LANCHESTER_ENABLED:
            # P-L Linear Law: casualties to X scale with the ENEMY's engaged strength in
            # contact (frontage-capped); DAMAGE_BY_DEGREE retained as per-soldier exchange
            # quality. Numbers-in-contact lives ONLY here under Lanchester (the run_battle
            # opp_frac post-scaler is skipped) — one variable, one role (Lesson 1).
            lin_b = _lanchester_strength(p["b_cells"], unit_b)   # B's contacting strength -> casualties to A
            lin_a = _lanchester_strength(p["a_cells"], unit_a)   # A's contacting strength -> casualties to B
            dmg_a += K_LINEAR * lin_b * max(0, DAMAGE_BY_DEGREE[b_deg](unit_b.power) - unit_a.dr)
            dmg_b += K_LINEAR * lin_a * max(0, DAMAGE_BY_DEGREE[a_deg](unit_a.power) - unit_b.dr)
        else:
            dmg_a += CASUALTY_SCALE * max(0, DAMAGE_BY_DEGREE[b_deg](unit_b.power) - unit_a.dr)
            dmg_b += CASUALTY_SCALE * max(0, DAMAGE_BY_DEGREE[a_deg](unit_a.power) - unit_b.dr)
        trace_event('melee', a_pool=a_pool, b_pool=b_pool,
                    ns_a=round(ns_a, 3), ns_b=round(ns_b, 3),
                    a_net=round(a_net, 2), b_net=round(b_net, 2),
                    a_deg=a_deg, b_deg=b_deg)
    return {"dmg_a": dmg_a, "dmg_b": dmg_b, "engagements": len(pairs)}

def resolve_engagements_cascading(unit_a, unit_b, pairs):
    """F-iii: cascading sub-phase resolution with facing rotation.
    [canonical: Jordan handoff §(3)]

    Contacts sorted by attacker depth (tip first). Each sub-phase resolves
    one depth group, then rotates engaged cells' facings toward their attacker.
    Later sub-phases see FLANK/REAR angles on already-rotated cells.
    Effect requires tight formation (TIP_SUPPORT_GAP=1 or 2) so multiple
    Arrowhead rows are simultaneously adjacent to Line cells."""
    if not CASCADING_ENABLED:
        return resolve_engagements(unit_a, unit_b, pairs)

    dynamic_facings = _init_dynamic_facings(unit_a, unit_b)
    total_dmg_a = total_dmg_b = 0
    resolved_keys = set()

    # Sort by attacker depth; group into sub-phases by proximity (1-row buckets)
    sorted_pairs = sorted(pairs, key=_cascade_depth_key)
    if not sorted_pairs:
        return {"dmg_a": 0, "dmg_b": 0, "engagements": 0}

    groups = []
    cur_group = [sorted_pairs[0]]
    cur_depth = _cascade_depth_key(sorted_pairs[0])
    for p in sorted_pairs[1:]:
        d = _cascade_depth_key(p)
        if abs(d - cur_depth) <= 1:
            cur_group.append(p)
        else:
            groups.append(cur_group)
            cur_group = [p]
            cur_depth = d
    groups.append(cur_group)

    total_engagements = 0
    for sub_idx, group in enumerate(groups):
        if sub_idx >= MAX_SUB_PHASES:
            break
        active = [p for p in group
                  if (id(p["atom_a"]), id(p["atom_b"])) not in resolved_keys]
        if not active:
            continue
        result = resolve_engagements(unit_a, unit_b, active, dynamic_facings)
        total_dmg_a += result["dmg_a"]
        total_dmg_b += result["dmg_b"]
        total_engagements += result["engagements"]
        for p in active:
            resolved_keys.add((id(p["atom_a"]), id(p["atom_b"])))
            # Rotate engaged cells toward their opponents
            _rotate_defender_facing(p["atom_b"], p["b_cells"], p["a_cells"], dynamic_facings)
            _rotate_defender_facing(p["atom_a"], p["a_cells"], p["b_cells"], dynamic_facings)

    return {"dmg_a": total_dmg_a, "dmg_b": total_dmg_b, "engagements": total_engagements}

# ─── VOLLEY (Phase 2 — ranged fire at distance) ──────────────────────────────
# [canonical: mass_battle_v30.md §A.7 Phase 2 — Volley fires before Manoeuvre.
#  PP-503: Volley pool = Power dice vs TN 6. Net successes − ranged DR = Size loss.
#  Damage recorded in Phase 2 but APPLIED at Phase 6 Step 1 (simultaneous with engagement).]

def _atom_distance(atom_a, atom_b):
    """Chebyshev (king-move) distance between nearest cells of two atoms."""
    cells_a = atom_a.cells()
    cells_b = atom_b.cells()
    if not cells_a or not cells_b:
        return float('inf')
    best = float('inf')
    for (ra, ca) in cells_a:
        for (rb, cb) in cells_b:
            d = max(abs(ra - rb), abs(ca - cb))
            if d < best:
                best = d
                if best == 0:
                    return 0
    return best


def _roll_volley_pool(power_dice):
    """Roll power_dice d10s vs TN=VOLLEY_TN. Returns net successes (count of d>=TN)
    with the standard fumble/crit: 1 = -1 net, 10 = +2 net.
    [canonical: mass_battle_v30.md §A.1 dice engine — TN-based successes, 1=-1, 10=+2]
    """
    if power_dice <= 0:
        return 0
    net = 0
    for _ in range(power_dice):
        roll = random.randint(1, 10)
        if roll == 1:
            net -= 1
        elif roll == 10:
            net += 2
        elif roll >= VOLLEY_TN:
            net += 1
    return max(0, net)  # floor at 0; PP-273 minimum pool is for engagement, not volley result


def _volley_density_mult(target_unit):
    """Missile-vulnerability of the TARGET formation: packed/deep columns catch overshoot and
    cannot disperse, so they bleed more under volley (Carrhae/Agincourt/Crecy); a dispersed or
    shallow line takes far fewer hits. 1.0 at the reference line density. Ranged-only path ->
    the melee gauge never reaches it (byte-exact).
    [bottom-up: col_grid density = troops/cell x ranks. historical anchor: massed-formation missile losses.]"""
    if not PC_VOLLEY_DENSITY_ENABLED:
        return 1.0
    grid = getattr(target_unit, 'col_grid', None)
    if not grid:
        return 1.0
    mean_density = sum(b.density for b in grid) / len(grid)
    return max(PC_VOLLEY_DENSITY_FLOOR, min(PC_VOLLEY_DENSITY_CAP, mean_density / PC_VOLLEY_DENSITY_REF))

def volley_phase(unit_a, unit_b):
    """Phase 2 Volley. Each ranged atom selects nearest in-range enemy atom and fires.
    Returns dict of total Size-loss to each side (applied simultaneously at end of turn).
    Pool = Power; TN = VOLLEY_TN; ranged DR subtracts from net successes.
    [canonical: mass_battle_v30.md §A.7 Phase 2 Volley; params/mass_combat.md §Ranged DR Table]
    """
    if not VOLLEY_ENABLED:
        return {"loss_a": 0, "loss_b": 0, "shots": 0}

    loss_a = loss_b = 0
    shots = 0

    def fire(shooter_atom, shooter_unit, target_unit):
        """Pick nearest in-range target atom, roll Power vs TN, return Size loss inflicted.
        Volley loss scales with the TARGET formation's density (_volley_density_mult)."""
        if shooter_atom.unit_type != "ranged":
            return 0, None
        target_atoms = target_unit.subunits
        best_target = None
        best_dist = float('inf')
        for t in target_atoms:
            d = _atom_distance(shooter_atom, t)
            if VOLLEY_MIN_RANGE <= d <= VOLLEY_MAX_RANGE and d < best_dist:
                best_dist = d
                best_target = t
        if best_target is None:
            return 0, None
        # Pool = unit Power dice (PP-503). Discipline penalty applies (per §A.4).
        pool = max(1, shooter_unit.power - shooter_unit.discipline_penalty_volley())
        net = _roll_volley_pool(pool)
        # DR subtracts from net successes (Ranged DR Table)
        net_after_dr = max(0, net - RANGED_DR_DEFAULT)
        if LANCHESTER_ENABLED:
            # P-L Square Law: aimed fire lifts the frontage cap — every shooter engages the
            # target area, so volley effectiveness scales with SHOOTER COUNT (toward N²-type
            # concentration over the integral). Distinct from the frontage-capped melee linear
            # term. [spec mb_lanchester_design.md §3b; Lanchester Square Law = ranged/aimed fire.]
            net_after_dr = net_after_dr * K_SQUARE * shooter_unit.effective_size
        dens = _volley_density_mult(target_unit)
        out = net_after_dr * dens
        trace_event('volley', shooter=getattr(shooter_unit, 'name', '?'), d=best_dist,
                    pool=pool, net=net, net_dr=round(net_after_dr, 2),
                    dens=round(dens, 3), loss=round(out, 2))
        return out, best_target

    for atom in unit_a.subunits:
        dmg, tgt = fire(atom, unit_a, unit_b)
        if tgt is not None:
            loss_b += dmg
            shots += 1
    for atom in unit_b.subunits:
        dmg, tgt = fire(atom, unit_b, unit_a)
        if tgt is not None:
            loss_a += dmg
            shots += 1

    return {"loss_a": loss_a, "loss_b": loss_b, "shots": shots}


# ─── BATTLE ──────────────────────────────────────────────────────────────────

def run_battle(unit_a, unit_b, max_turns=18):
    """Run one engagement turn (up to 3 phases = 18 ticks).
    v16: max_turns=18 = one battle turn's engagement cap (3 phases).
    Multi-turn battles call this repeatedly with persistent unit state.
    [canonical: Jordan direction — "limit of three phases per simultaneous
     engagement per turn"]

    Returns:
      {"winner": "A"|"B"|"draw", "turns": int, "phases": int, "tick_in_phase": int}
    """
    turns = 0
    current_phase = 0
    for t in range(1, max_turns + 1):
        turns = t
        trace_event('tick', t=t)
        if unit_a.routed or unit_b.routed: break
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
            op_a = _oriented(p["atom_a"])
            for cell in p["a_cells"]:
                for orig_r, orig_c, or_r, or_c in op_a:
                    abs_r = (p["atom_a"].starting_position[0] + or_r
                             + p["atom_a"].cell_offsets.get((orig_r,orig_c), 0) * p["atom_a"].advance_dir)
                    abs_c = (p["atom_a"].starting_position[1] + or_c
                             + p["atom_a"].cell_offsets_c.get((orig_r,orig_c), 0))
                    if (abs_r, abs_c) == cell:
                        p["atom_a"].halted_cells.add((orig_r, orig_c)); break
            op_b = _oriented(p["atom_b"])
            for cell in p["b_cells"]:
                for orig_r, orig_c, or_r, or_c in op_b:
                    abs_r = (p["atom_b"].starting_position[0] + or_r
                             + p["atom_b"].cell_offsets.get((orig_r,orig_c), 0) * p["atom_b"].advance_dir)
                    abs_c = (p["atom_b"].starting_position[1] + or_c
                             + p["atom_b"].cell_offsets_c.get((orig_r,orig_c), 0))
                    if (abs_r, abs_c) == cell:
                        p["atom_b"].halted_cells.add((orig_r, orig_c)); break
        assign_targets(unit_a, unit_b)
        b_cells_set = set(c for sub in unit_b.subunits for c in sub.cells())
        a_cells_set = set(c for sub in unit_a.subunits for c in sub.cells())
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
        for atom in unit_a.subunits:
            if atom.target_atom:
                atom.advance_cells(unit_a.discipline, cached_centroids[id(atom)],
                                   enemy_cells=b_cells_set)
        for atom in unit_b.subunits:
            if atom.target_atom:
                atom.advance_cells(unit_b.discipline, cached_centroids[id(atom)],
                                   enemy_cells=a_cells_set)
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
        # resolve_internal_collisions) is implemented but not invoked here —
        # it over-tuned battery (12/13 -> 9/13). Left available for future use
        # when paired with a proper bad-facing trigger.
        pairs = find_contacts(unit_a, unit_b)
        # v20: stamina drain proportional to cells in contact (bottom-up).
        # More front-line cells fighting = more exhaustion. Emergent from formation.
        if pairs:
            for u in [unit_a, unit_b]:
                if u.routed:
                    continue
                cells_in_contact = 0
                for p in pairs:
                    if p.get('atom_a') in u.subunits:
                        cells_in_contact += len(p.get('a_cells', []))
                    elif p.get('atom_b') in u.subunits:
                        cells_in_contact += len(p.get('b_cells', []))
                drain = max(1, cells_in_contact) * STAMINA_DRAIN_PER_CONTACT_CELL
                u.stamina = max(0, u.stamina - drain)
        result = (resolve_engagements_cascading(unit_a, unit_b, pairs)
                  if CASCADING_ENABLED
                  else resolve_engagements(unit_a, unit_b, pairs))
        sz_a, sz_b = unit_a.size, unit_b.size
        # Apply Phase 2 Volley + Phase 5 Engagement damage simultaneously at Phase 6 Step 1
        # [canonical: mass_battle_v30.md §A.7 — Volley/Thread/Engagement damage applied together]
        total_dmg_a_turn = result["dmg_a"] + volley_dmg_a
        total_dmg_b_turn = result["dmg_b"] + volley_dmg_b
        # v12: Volley size-loss → hp uses ceil(h_per_size / 2), not full h_per_size.
        # Bottom-up rationale: a ranged "size loss" represents arrows finding targets in
        # the formation; many hits glance off shields/armor. Melee size loss represents
        # men killed in close combat, where wounds are decisive. Halving the conversion
        # captures that volley size loss is less lethal per unit than melee size loss.
        # Reduces R1 (Ranged vs Line) without breaking R3 (mirror — same scaling on both sides).
        # [canonical: Jordan design 2026-05-12 — volley hp scaling tuned for historical match]
        volley_hp_scale = lambda u: max(1, (u.h_per_size + 1) // 2)
        # v20: scale engagement damage by contact fraction.
        # More cells in contact = more soldiers fighting = more damage dealt.
        # Bottom-up: the envelopment advantage EMERGES from having more cells engaged.
        # contact_fraction = cells_in_contact / total_cells. Capped at 1.0.
        # P-L: SKIPPED under LANCHESTER_ENABLED — numbers-in-contact is carried by the
        # linear term in resolve_engagements (one role, one place). Skipping here also
        # makes LANCHESTER_ENABLED=0 byte-exact to the pre-P-L engine.
        if pairs and not LANCHESTER_ENABLED:
            for u, dmg_key in [(unit_a, "dmg_a"), (unit_b, "dmg_b")]:
                cells_in_contact = set()
                total_cells = 0
                for sub in u.subunits:
                    total_cells += len(list(sub.cells()))
                    for p in pairs:
                        if p.get('atom_a') is sub:
                            cells_in_contact.update(p.get('a_cells', []))
                        elif p.get('atom_b') is sub:
                            cells_in_contact.update(p.get('b_cells', []))
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
                    # "a wider front brings more men to bear" effect. PC_FRONTAGE_BLEND in [0,1] trades between them.
                    grid = opp.col_grid
                    eng_cols = _engaged_cols(opp, pairs)
                    alive_cols = [b for b in grid if b.alive()]
                    n_alive = len(alive_cols)
                    n_eng = sum(1 for b in alive_cols if b.col in eng_cols)
                    frontage_term = (n_eng / n_alive) if n_alive else 0.0          # depth-neutral
                    width_term = min(1.0, n_eng / PC_FRONTAGE_REF)                  # more engaged columns = more men
                    opp_frac = PC_FRONTAGE_BLEND * frontage_term + (1.0 - PC_FRONTAGE_BLEND) * width_term
                else:
                    opp_frac = len(opp_cells_contact) / max(1, opp_total)
                result[dmg_key] = result[dmg_key] * max(0.2, opp_frac)
        # v21: SIMULTANEOUS HP — apply damage to both units, THEN recalc_size
        # for both. Prevents size recalc of unit_a from affecting anything
        # before unit_b's damage is applied.
        # [canonical: params/mass_combat.md PP-233 — "Damage is simultaneous.
        #  Both sides deal and receive damage before Size is recalculated."]
        unit_a.hp = max(0, unit_a.hp - result["dmg_a"] - volley_dmg_a * volley_hp_scale(unit_a))
        unit_b.hp = max(0, unit_b.hp - result["dmg_b"] - volley_dmg_b * volley_hp_scale(unit_b))
        if PER_CELL:
            # Increment 2: mirror the same total casualties onto the per-column grid (keeps sum==hp).
            distribute_casualties(unit_a, result["dmg_a"] + volley_dmg_a * volley_hp_scale(unit_a), pairs)
            distribute_casualties(unit_b, result["dmg_b"] + volley_dmg_b * volley_hp_scale(unit_b), pairs)
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
                u.morale = 0.0
                continue  # rout check below

        # Rout check AFTER both erosions applied
        for u in [unit_a, unit_b]:
            if not u.routed and u.morale <= 0:
                u.routed = True
        # v15: phase boundary — stamina_check, morale_check_phase, rout_resolution
        # are now populated (G-1 + G-2). rally/reform/threadwork remain empty.
        if t % TICKS_PER_PHASE == 0:
            current_phase += 1
            phase_boundary(unit_a, unit_b, current_phase)
    winner = ("A" if not unit_a.routed and unit_b.routed else
              "B" if not unit_b.routed and unit_a.routed else "draw")
    tick_in_phase = turns % TICKS_PER_PHASE if turns else 0
    return {"winner": winner, "turns": turns,
            "phases": current_phase, "tick_in_phase": tick_in_phase,
            "a_stamina": unit_a.stamina, "b_stamina": unit_b.stamina,
            "a_hp_pct": round(unit_a.hp / unit_a.hp_max * 100, 1) if unit_a.hp_max else 0,
            "b_hp_pct": round(unit_b.hp / unit_b.hp_max * 100, 1) if unit_b.hp_max else 0,
            "a_morale": unit_a.morale, "b_morale": unit_b.morale}

# ─── MULTI-TURN BATTLE ORCHESTRATOR (D-1, D-9) ─────────────────────────────
# Models a multi-turn battle: each turn = one 3-phase engagement (run_battle).
# Between turns: units disengage, partial stamina recovery, state persists.
# [canonical: Jordan direction — "we have a bunch of turns throughout the mass
#  battle system. 5 turns in a row attacking. limit of 3 phases per engagement"]

# Between-turn recovery rules (D-9):
# [ASSUMPTION: between-turn recovery constants are tuning parameters —
#  basis: no canonical source specifies inter-turn recovery rates]
# [canonical: params/mass_combat.md §PP-712 — "Discipline persists between battles"]
BETWEEN_TURN_STAMINA_RECOVERY = 30  # partial rest during disengagement
BETWEEN_TURN_MORALE_RECOVERY = 0    # morale does NOT recover between turns
# HP does NOT recover between turns (casualties are permanent within a battle)
# Discipline persists (canonical PP-712)
# [canonical: designs/provincial/mass_battle_v30.md §A.4 — "Morale reset between battles"]


def between_turn_recovery(unit):
    """Apply between-turn state changes. Called after each engagement turn.
    [canonical: params/mass_combat.md §PP-712 — discipline persists]"""
    if unit.routed or unit.broken:
        return
    unit.stamina = min(unit.stamina_max, unit.stamina + BETWEEN_TURN_STAMINA_RECOVERY)
    unit.morale = min(unit.morale_start, unit.morale + BETWEEN_TURN_MORALE_RECOVERY)


def reset_positions(unit, shape, anchor_map):
    """Reset subunit positions for re-engagement after disengagement.
    Units return to their starting rows for fresh approach."""
    start_row = SIDE_A_START_ROW if unit.faction == 'A' else SIDE_B_START_ROW
    anchor_col = anchor_map.get((shape, unit.subunits[0].tier), 10)
    for atom in unit.subunits:
        atom.starting_position = (start_row, anchor_col)
        atom.cell_offsets = {}
        atom.cell_offsets_c = {}


def run_multi_turn_battle(unit_a, unit_b, shape_a, shape_b, anchor_map,
                          max_battle_turns=8):
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
        # v21: alternating swap removed — simultaneous resolution makes
        # run_battle symmetric regardless of argument order.
        r = run_battle(unit_a, unit_b)

        a_loss_turn = (hp_a_before - unit_a.hp) / unit_a.hp_max if unit_a.hp_max else 0
        b_loss_turn = (hp_b_before - unit_b.hp) / unit_b.hp_max if unit_b.hp_max else 0
        a_loss_cum = 1.0 - (unit_a.hp / unit_a.hp_max) if unit_a.hp_max else 1.0
        b_loss_cum = 1.0 - (unit_b.hp / unit_b.hp_max) if unit_b.hp_max else 1.0

        log.append({
            'turn': battle_turn,
            'a_loss_turn': a_loss_turn, 'b_loss_turn': b_loss_turn,
            'a_loss_cum': a_loss_cum, 'b_loss_cum': b_loss_cum,
            'a_pool': unit_a.base_combat_pool(), 'b_pool': unit_b.base_combat_pool(),
            'a_eff_size': unit_a.effective_size, 'b_eff_size': unit_b.effective_size,
            'a_morale': unit_a.morale, 'b_morale': unit_b.morale,
            'a_stamina': unit_a.stamina, 'b_stamina': unit_b.stamina,
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


# ─── PURSUIT (G-11, v22) ─────────────────────────────────────────────────────
# [canonical: designs/provincial/mass_battle_v30.md §A.12-514]
# "Pursuit: Fast units only. Routing unit loses Size equal to pursuer net
#  Offence successes (no Defence) each turn. Recall: Command Ob 2."
# "Routing: Slow/Standard cannot fight back. Fast may rearguard at −2D Off."
REARGUARD_PENALTY = 2  # [canonical: §A.12 — "Fast may rearguard at −2D Off"]
RECALL_OB = 2  # [canonical: §A.12 — "Recall: Command Ob 2"]


def pursuit_damage(pursuer, routing_unit):
    """Fast pursuer attacks routing unit. Routing unit has no defence
    unless it is also Fast (rearguard at -2D Off).
    Returns HP damage dealt.
    [canonical: designs/provincial/mass_battle_v30.md §A.12]"""
    if pursuer.speed != "Fast":
        return 0  # Only Fast units can pursue
    if pursuer.routed or pursuer.broken:
        return 0
    if not routing_unit.routed:
        return 0

    # [canonical: params/mass_combat.md PP-233 — Pool = min(Size,Cmd)+Cmd]
    a_pool = pursuer.base_combat_pool()
    a_net = roll_pool(a_pool)

    # Fast routing unit may rearguard at -2D Off
    # [canonical: §A.12 — "Fast may rearguard at −2D Off"]
    if routing_unit.speed == "Fast":
        rg_pool = max(1, routing_unit.base_combat_pool() - REARGUARD_PENALTY)
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


def recall_check(pursuer):
    """General attempts to recall pursuing unit. Command Ob 2.
    Returns True if recalled (pursuit stops).
    [canonical: designs/provincial/mass_battle_v30.md §A.12]"""
    net = roll_pool(pursuer.command)
    return net >= RECALL_OB


# ─── MULTI-UNIT BATTLE ORCHESTRATOR (D-3, D-5, v22) ──────────────────────────
# Models battles with multiple units per side. Each engagement pair runs through
# run_battle (1v1). After all pairs resolve: morale cascade, rout contagion,
# freed-attacker flanking. Between turns: recovery.
# [canonical: designs/provincial/mass_battle_v30.md §A.12 — Morale Cascade,
#  Rout contagion brake, pursuit rules]

# v22: Morale cascade discipline check — Ob 1, fires at Phase 6 Step 3
# [canonical: §A.12 — "all friendly units in the same engagement make a
#  Discipline check (Ob 1). Failure: Morale −1"]
MORALE_CASCADE_OB = 1  # [canonical: designs/provincial/mass_battle_v30.md §A.12]
ROUT_CONTAGION_MORALE_HIT = 1  # [canonical: designs/provincial/mass_battle_v30.md L167]
FREED_ATTACKER_FLANK_PENALTY = 1  # [canonical: §A.4 octagon YELLOW = -1D]


def discipline_check_cascade(unit):
    """Discipline check Ob 1 for morale cascade.
    Returns True if unit PASSES (resists cascade).
    [canonical: designs/provincial/mass_battle_v30.md §A.12 — Ob 1 check]"""
    # [canonical: params/mass_combat.md — roll_pool uses TN 7 default]
    net = roll_pool(unit.discipline)
    return net >= MORALE_CASCADE_OB


def freed_attacker_damage(freed_unit, target_unit):
    """Freed unit attacks target from the flank.
    The freed unit rolls its full pool. Target defends at -1D (flank).
    Returns damage dealt to target.
    [canonical: designs/provincial/mass_battle_v30.md §A.12 — implied by
     rout freeing the victor to attack adjacent enemies]"""
    if freed_unit.routed or freed_unit.broken:
        return 0
    if target_unit.routed or target_unit.broken:
        return 0
    # [canonical: params/mass_combat.md PP-233 — Pool = min(Size,Cmd)+Cmd]
    a_pool = freed_unit.base_combat_pool()
    # [canonical: designs/provincial/mass_battle_v30.md §A.4 — YELLOW zone -1D]
    b_pool = max(1, target_unit.base_combat_pool() - FREED_ATTACKER_FLANK_PENALTY)
    a_net = roll_pool(a_pool)
    b_net = roll_pool(b_pool)
    a_deg = compute_degree(a_net, max(1, b_net))
    # [canonical: params/mass_combat.md PP-233 — Damage = successes × (1+Power)]
    dmg = CASUALTY_SCALE * max(0, DAMAGE_BY_DEGREE[a_deg](freed_unit.power) - target_unit.dr)
    return dmg


def run_multi_unit_battle(side_a, side_b, pairings, shapes_a, shapes_b,
                          anchor_map, max_battle_turns=8):
    """Run a multi-unit battle with morale cascade and freed-attacker.

    Args:
        side_a: list of Unit objects for side A
        side_b: list of Unit objects for side B
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

    for battle_turn in range(1, max_battle_turns + 1):
        turn_log = {
            'turn': battle_turn,
            'engagements': [],
            'cascades': [],
            'freed_attacks': [],
            'pursuits': [],
            'routs_this_turn': [],
        }

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
            if recall_check(pursuer):
                pursuing_units.remove((pursuer, routing, p_side, p_pair))
                freed_units.append((pursuer, p_side, p_pair))
                turn_log['pursuits'].append({
                    'pursuer': pursuer.name, 'target': routing.name,
                    'damage': 0, 'recalled': True,
                })
                continue
            # Pursuit damage
            dmg = pursuit_damage(pursuer, routing)
            if dmg > 0:
                routing.hp = max(0, routing.hp - dmg)
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
            r = run_battle(ua, ub)
            turn_log['engagements'].append({
                'pair': pair_idx, 'a_idx': a_idx, 'b_idx': b_idx,
                'result': r['winner'], 'ticks': r['turns'],
            })

        # ── Freed-attacker bonus damage (from PREVIOUS turn's freed units) ──
        # [canonical: §A.12 — freed unit attacks adjacent enemy from flank]
        for freed_unit, owner_side, source_pair in list(freed_units):
            if freed_unit.routed or freed_unit.broken:
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
                if not enemy.routed and not enemy.broken:
                    target = enemy
                    break

            if target:
                dmg = freed_attacker_damage(freed_unit, target)
                if dmg > 0:
                    # [canonical: params/mass_combat.md PP-233 — simultaneous damage]
                    target.hp = max(0, target.hp - dmg)
                    target.recalc_size()
                    # Morale erosion from flanking damage
                    # [canonical: designs/provincial/mass_battle_v30.md §A.4]
                    if target.discipline > 0 and target.command > 0:
                        erosion = dmg / (target.discipline * target.command)
                        target.morale -= erosion
                    if target.morale <= 0:
                        target.routed = True
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
                if not discipline_check_cascade(friend):
                    friend.morale -= 1
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
                friend.morale -= ROUT_CONTAGION_MORALE_HIT
                # Brake: this morale loss cannot cause rout this turn
                # (rout check deferred to next turn's engagement resolution)

        # ── Freed-attacker: victor from resolved pair becomes free ──
        # v22/G-11: Fast victors PURSUE routing unit (§A.12). Non-Fast join adjacent.
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
        if not active_pairs and not pursuing_units:
            # No engagements and no pursuit — freed attackers can't do anything
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

__all__ = ['_formation_depth', '_stamina_pool_penalty', 'stamina_check', 'morale_check_phase', 'rout_resolution', 'discipline_check_phase', 'rally_check', 'reform_check', 'threadwork_check', 'phase_boundary', 'Subunit', 'Unit', 'derive_command', 'command_base_pool', 'assign_targets', 'resolve_cross_side_contention', 'find_contacts', 'count_engagements_per_atom', '_momentum_speed', '_cascade_depth_key', 'PC_ROLLUP_PER_RANK', 'PC_ROLLUP_MARGIN', 'PC_ROLLUP_REACH', 'PC_ROLLUP_CAP', 'PC_ROLLUP_FLANK_REACH', 'PC_ROLLUP_MIN_DEPTH', '_lanchester_strength', 'resolve_engagements', 'resolve_engagements_cascading', '_atom_distance', '_roll_volley_pool', 'volley_phase', 'run_battle', 'BETWEEN_TURN_STAMINA_RECOVERY', 'BETWEEN_TURN_MORALE_RECOVERY', 'between_turn_recovery', 'reset_positions', 'run_multi_turn_battle', 'REARGUARD_PENALTY', 'RECALL_OB', 'pursuit_damage', 'recall_check', 'MORALE_CASCADE_OB', 'ROUT_CONTAGION_MORALE_HIT', 'FREED_ATTACKER_FLANK_PENALTY', 'discipline_check_cascade', 'freed_attacker_damage', 'run_multi_unit_battle', 'roles_for', 'role_allowed']
