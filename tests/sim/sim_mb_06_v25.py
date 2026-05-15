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
#   - SHAPE_OFF_MOD and SHAPE_DEF_MOD zeroed (flat per-shape bonuses removed)
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

# v25: BATTLEFIELD GEOMETRY [canonical: designs/provincial/mass_battle_v30.md §A.3b — 2026-05-15]
# 1v1 battle uses a connected 41 cols × 42 rows map. Each unit gets a
# 41×21 personal grid. Formation area within unit grid is 19 wide × 11 deep
# (a player can shape their formation within this area; each cell holds
# a player-assignable troop count between min/max).
# Buffers:
#   - 11 cells lateral buffer each side (cols 0-10 and 30-40)
#   - 5 cells front buffer (between formation area and enemy)
#   - 5 cells back buffer (between formation area and map edge)
# Wide side buffers give formations real room to gap, spread wings, and
# maneuver without immediately running into the map edge.
# A occupies rows 21-41 (lower half), advance_dir=-1 toward B at rows 0-20.
# Formation centered at grid center: A at row 31, B at row 10, both at col 20.
BATTLEFIELD_HEIGHT = 42
BATTLEFIELD_WIDTH = 41
BATTLEFIELD_SIZE = max(BATTLEFIELD_HEIGHT, BATTLEFIELD_WIDTH)  # legacy alias
UNIT_GRID_HEIGHT = 21       # per-unit row extent
UNIT_GRID_WIDTH = 41        # per-unit col extent (= battlefield width)
FORMATION_AREA_WIDTH = 19   # max formation width within unit grid
FORMATION_AREA_DEPTH = 11   # max formation depth within unit grid
FRONT_BACK_BUFFER = 5       # rows between formation area and unit grid edge
SIDE_BUFFER = 11            # cols between formation area and unit grid edge
UNIT_GRID_SIZE = max(FORMATION_AREA_WIDTH, FORMATION_AREA_DEPTH)  # legacy alias

# Horseshoe wing pathing buffer: how many cols outside enemy's lateral edge
# the wing's INNERMOST cell targets. Matches SIDE_BUFFER so wings can spread
# deep into the side buffer zone before turning inward.
WING_LATERAL_BUFFER = 3

# Sightline geometry [canonical: Jordan 2026-05-15]
# Cells can only perceive enemies within a 135° arc from their facing
# AND within 15 cells distance. Cells cannot rotate to face attackers
# outside this sightline — they don't know those attackers are there.
# This is the mechanical justification for why a Line cell doesn't simply
# turn around when Horseshoe wings wrap behind it.
SIGHTLINE_ARC_HALF = 67.5   # [canonical: designs/provincial/mass_battle_v30.md §A.3b] half-angle of 135° sightline (degrees)
SIGHTLINE_DISTANCE = 15     # [canonical: designs/provincial/mass_battle_v30.md §A.3b] max distance a cell perceives

# Formation CENTERS (one row of each 5-cell-tall Line, etc, placed here at
# the center). A's grid center row 31, B's grid center row 10.
SIDE_A_START_ROW = 31       # A formation center row (lower half center)
SIDE_B_START_ROW = 10       # B formation center row (upper half center)
BATTLEFIELD_CENTER_COL = 20 # lateral center of 41-wide map (col 0-40)

POOL_VARIANT = "C-ii"

TIP_SUPPORT_ENABLED = True
TIP_SUPPORT_GAP = 4  # v25: increased from 2 — tip must be able to penetrate deeply
# [canonical: Jordan design — Arrowhead tip pierces line and creates displacement ripple;
#  gap=2 arrested tip at Line's front; gap=4 allows penetration 2 rows into formation]

# [canonical: mass_battle_v30.md §Scale — T1=100(1 size), T2=200(2), T3=400(4), T4=800(8), base 100]
TROOPS_PER_TIER = {1: 100, 2: 200, 3: 400, 4: 800}
TROOPS_PER_SIZE = 100
ENCIRCLEMENT_PENALTY = 1

# F-i: Cell support stacking [canonical: Jordan handoff §(1)]
SUPPORT_STACK_ENABLED = True
# [canonical: Jordan handoff §(1) — depth-1: full, depth-2: 0.7, depth-3: 0.5, floor 0.3]
SUPPORT_WEIGHTS = {1: 1.0, 2: 0.7, 3: 0.5}
SUPPORT_WEIGHT_FLOOR = 0.3

# F-ii: Puncture mechanism [canonical: Jordan handoff §(2)]
PUNCTURE_ENABLED = True
PUNCTURE_CAP = 3

# F-iii: Cascading resolution [canonical: Jordan handoff §(3)]
CASCADING_ENABLED = True
MAX_SUB_PHASES = 5

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
TICKS_PER_PHASE = 6

# ─── TROOP COUNT / BLOCK SIZE (bottom-up lethality) ─────────────────────────
# [canonical: designs/provincial/mass_battle_v30.md §A.3 — "1 Size = block_size soldiers"]
# [canonical: derived_stats architecture (2026-04-19) — "TroopCount = Size × block_size"]
# HP = TroopCount = Size × BLOCK_SIZE. Damage from combat = soldier casualties.
# No LETHALITY_SCALE — casualty rates emerge from pool/TN/DR mechanics directly.
# At Company scale: Size 4 unit = 400 soldiers = 400 HP. Pool=8, ~3 successes/tick
# = ~3 soldiers killed/tick = 0.75%/tick = ~13% per 3-phase turn. Emergent.
BLOCK_SIZE = 100  # [canonical: designs/provincial/mass_battle_v30.md §A.3 — Company scale]

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
STAMINA_MAX = 100
STAMINA_DRAIN_PER_CONTACT_CELL = 1   # drain per cell in contact per tick
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
STAMINA_RECOVERY_PER_RESERVE_RANK = 8
# Pool penalty: only at exhaustion. The differentiation comes from WHEN each
# formation exhausts, not how much worse they get. -1 die when exhausted =
# small but persistent disadvantage that compounds across many ticks.
# Deeper formations recover more → exhaust later → fight at full pool longer.
STAMINA_POOL_THRESHOLDS = [(1, 0)]  # no penalty while stamina > 0
STAMINA_EXHAUSTED_POOL_PENALTY = -1  # stamina == 0: -1 die
# G-2 rout-at-threshold constants (phase-boundary morale check for exhausted units)
# [canonical: mass_battle_v30.md §A.4 — morale floor = 1 while general present;
#  G-2 overrides this for exhausted+damaged units at phase boundary]
ROUT_FLOOR_LOSS_PCT = 0.20          # casualty% at which exhausted unit loses morale floor
ROUT_EXHAUSTION_MORALE_HIT = 1      # morale loss per phase boundary when exhausted
# [canonical: mass_battle_v30.md §A.4 — cap −3 per Cascade Phase for non-general morale loss]
MORALE_PHASE_CAP = 3

# ─── DISCIPLINE DEGRADATION WITH CONTINUOUS EFFECTIVE_SIZE (D-6) ─────────
# [canonical: params/mass_combat.md §Discipline Degradation —
#  "Discipline degrades when Size lost > Discipline AND asymmetric"]
# Reinterpreted for continuous: check cumulative HP loss as fraction of
# h_per_size at each phase boundary. Fires when cumulative_loss in eff_size
# terms exceeds 1.0 AND loss is asymmetric. Each time it fires, threshold
# resets (so it can fire again after another 1.0 eff_size loss).
# [ASSUMPTION: threshold 1.0 eff_size maps to "Size lost > 1" in original]
DISCIPLINE_LOSS_THRESHOLD = 1.0  # [canonical: params/mass_combat.md §Discipline Degradation]

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
        if u.routed or u.broken:
            continue
        if u.stamina > 0:
            continue  # only exhausted units feel phase-boundary pressure
        # v20: exhaustion accelerates morale erosion at phase boundary.
        # Additional erosion = 1.0 / (discipline * command). Small but compounds.
        if u.discipline > 0 and u.command > 0:
            exhaustion_erosion = 1.0 / (u.discipline * u.command)
            u.morale -= exhaustion_erosion


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
VOLLEY_ENABLED = True
# TN for Volley success rolls. Standard d10: TN 6 success rate ≈ 0.5/die.
# [canonical: mass_battle_v30.md §A.7 PP-503 — "TN 6 [PROVISIONAL]"]
VOLLEY_TN = 6
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
RANGED_DR_DEFAULT = 2
# Minimum cell-distance for Volley targeting. Distance ≤ 1 = adjacent/melee contact;
# ranged units historically stop firing once enemy closes to hand-to-hand range.
# [canonical: mass_battle_v30.md §A.7 Phase 2 vs Phase 5 — Volley is pre-Engagement;
#  once contact made, units fight in melee not volley]
VOLLEY_MIN_RANGE = 2
# v12: VOLLEY_MAX_RANGE reduced from BATTLEFIELD_SIZE (25) to 8.
# Initial deployment is row 5 vs row 15 = 10 cells apart. Range 8 means ranged
# units must close 1-2 cells (or wait for enemy to approach) before volley begins.
# Historical longbow at Crécy/Agincourt: effective fire began ~100 paces (~5 cells)
# but harassment fire extended further. Range 8 captures both regimes.
# Reduces R1 (Ranged vs Line) by ~25% by removing 4-5 turns of free volley.
# [canonical: references/historical/precedents_warfare.md — effective volleys at
#  100-200 paces; killing zone was the final approach to contact]
VOLLEY_MAX_RANGE = 8

# [canonical: mass_battle_v30.md §ED-816 shape mods; -99 = structural sentinel (−∞ pool)]
# [canonical: v11 — gap=-99 removed for GappedLine. Gap effect is geometric:
#  no cells at the gap column means no engagement there. Per-cell angles handle
#  the flanking naturally. Structural sentinel only retained where cell is absent.]
SHAPE_OFF_MOD = {
    "Line":        lambda role: 0,
    "Arrowhead":   lambda role: 0,
    "Horseshoe":   lambda role: 0,
    "GappedLine":  lambda role: 0,
    "RefusedFlank":lambda role: 0,
}
SHAPE_DEF_MOD = {"Line": lambda r: 0, "Arrowhead": lambda r: 0,
                  "Horseshoe": lambda r: 0,
                  "GappedLine": lambda r: 0, "RefusedFlank": lambda r: 0}
MIN_DISCIPLINE = {
    # [canonical: mass_battle_v30.md §ED-815 shape discipline — min disc required by shape]
    "Line": 1, "Arrowhead": 4, "Horseshoe": 5, "GappedLine": 5, "RefusedFlank": 3
}

# ─── CELL PATTERNS ───────────────────────────────────────────────────────────
# [canonical: mass_battle_v30.md §Shapes — per-tier cell grid dimensions, Jordan design]

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


def in_sightline(observer_pos, observer_facing, target_pos,
                 arc_half=SIGHTLINE_ARC_HALF, max_dist=SIGHTLINE_DISTANCE):
    """Check if target_pos is within observer's sightline.

    A target is in sightline if it is BOTH within max_dist cells AND
    within arc_half degrees of the observer's facing direction.

    During flanking maneuvers, a moving cell's facing rotates to its
    movement vector — so a wing sweeping diagonally outward looks in
    that diagonal direction. The enemy it's flanking continues facing
    forward and CANNOT see the wing (wing is beyond enemy's sightline arc).
    This is the mechanical justification for why flanked units don't
    simply rotate to face the new threat.

    [canonical: designs/provincial/mass_battle_v30.md §A.3b — 2026-05-15 — 135° sightline from facing
     octagon front; 15 cell range; sightline rotates with movement vector]
    """
    dr = target_pos[0] - observer_pos[0]
    dc = target_pos[1] - observer_pos[1]
    dist_sq = dr*dr + dc*dc
    if dist_sq > max_dist * max_dist:
        return False
    if dist_sq < 1e-9:
        return True  # co-located
    fr, fc = observer_facing
    fmag_sq = fr*fr + fc*fc
    if fmag_sq < 1e-9:
        return True  # no facing → can see everything
    dist = dist_sq ** 0.5
    fmag = fmag_sq ** 0.5
    cos_a = (dr * fr + dc * fc) / (dist * fmag)
    cos_a = max(-1.0, min(1.0, cos_a))
    angle_deg = math.degrees(math.acos(cos_a))
    return angle_deg <= arc_half

ANGLE_DEF_MOD = {
    # v11: per-cell octagon. GREEN < 45° = 0D; YELLOW 45-90° = -1D; RED ≥ 90° = -2D.
    # [canonical: Jordan design]
    "GREEN": 0, "YELLOW": -1, "RED": -2,
    "FRONT": 0, "FLANK": -1, "REAR": -2,  # legacy aliases
}

# v25: angle-dependent damage multipliers — bottom-up cell-level mechanics.
# [canonical: Jordan design — "side attacks to do more damage, back attacks even more"]
# GREEN (frontal):  1.0× — equal engagement, shield and facing give full protection
# YELLOW (flank):   1.5× — partial shield coverage, soldier partially turned
# RED (rear):       2.0× — no shield, no awareness, double casualties
ANGLE_DMG_MULT = {"GREEN": 1.0, "YELLOW": 1.5, "RED": 2.0}  # [canonical: Jordan design]

# v25: flanked-while-engaged multiplier.
# [canonical: Jordan design — "being flanked while front is occupied is devastating"]
# Applied when a cell has ≥1 GREEN attacker AND is simultaneously attacked from non-GREEN.
# The non-GREEN attack gets this additional multiplier on top of ANGLE_DMG_MULT.
FLANKED_BONUS = 1.5  # [canonical: Jordan design — flanked while engaged]

# v25: attention split — max pool fraction when facing multiple attackers simultaneously.
# [canonical: Jordan design — "cannot commit full pool against each cell it's facing"]
# A cell facing N opponents has its effective pool divided by N when any attack is non-GREEN.
# No split if all attacks are GREEN (frontal — unit can hold its line against multiple front attackers).
ATTENTION_SPLIT_MIN_POOL = 1  # [canonical: structural — minimum pool floor]

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
            comp_r, comp_c = atom.cell_pos.get((orig_r, orig_c), (0, 0))
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
    """Rotate engaged defender cells toward their VISIBLE attackers.

    v25 sightline: a cell only rotates toward attackers it can see
    (within 135° forward arc AND 15-cell range from its current facing).
    Attackers outside the cell's sightline are invisible — the cell
    doesn't know they're there, so it can't turn to face them.

    This is the mechanical justification for flanking: when Horseshoe
    wings wrap behind a Line cell that's facing forward, the wing cells
    are in the Line cell's REAR (outside its sightline arc). The Line
    cell can't perceive them, doesn't rotate, and takes ongoing RED-zone
    attacks from the wings.

    Wing cells DO see the enemy from their flank-sweep position because
    their own facing rotated to match their movement vector (looking in
    the direction they're moving). Asymmetric sightline = asymmetric
    awareness = flanking works.

    [canonical: designs/provincial/mass_battle_v30.md §A.3b — 2026-05-15 — 135° sightline, 15-cell range,
     rotates with movement vector during maneuvers]
    """
    if not attacker_abs_cells or not defender_abs_cells:
        return
    op = oriented_pattern(defender_atom.shape, defender_atom.tier, defender_atom.advance_dir)
    for abs_r, abs_c in defender_abs_cells:
        for orig_r, orig_c, or_r, or_c in op:
            comp_r, comp_c = defender_atom.cell_pos.get((orig_r, orig_c), (0, 0))
            if (comp_r, comp_c) != (abs_r, abs_c):
                continue
            # Get this defender cell's CURRENT facing for sightline check
            current_facing = defender_atom.get_cell_facing(orig_r, orig_c)
            # Filter attackers by sightline — only visible attackers count
            visible = [(ar, ac) for ar, ac in attacker_abs_cells
                       if in_sightline((abs_r, abs_c), current_facing, (ar, ac))]
            if not visible:
                break  # no visible attackers — no rotation, sightline blocks awareness
            # Rotate toward mean of VISIBLE attackers only
            att_r = sum(c[0] for c in visible) / len(visible)
            att_c = sum(c[1] for c in visible) / len(visible)
            dr = att_r - abs_r
            dc = att_c - abs_c
            mag = max(1e-9, (dr*dr + dc*dc)**0.5)
            facing = (round(dr / mag), round(dc / mag))
            dynamic_facings[_cell_facing_key(defender_atom, orig_r, orig_c)] = facing
            # Persistent write-back so subsequent octagon reads use rotated facing
            defender_atom.cell_facing_vec[(orig_r, orig_c)] = facing
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
            comp_r, comp_c = atom.cell_pos.get((orig_r, orig_c), (0, 0))
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

STANCE_SPEED_MOD = {"aggressive": 1, "balanced": 0, "hold": -99, "retreat": 0}

# ─── ATOM ────────────────────────────────────────────────────────────────────

@dataclass
class Subunit:
    """
    v24: RELATIVE-ORIGIN CELL MODEL.

    Each cell carries its own reference position (cell_ref) and current
    position (cell_pos), making both sides symmetric by construction. No
    global starting_position offset arithmetic; no advance_dir in position
    computation.

    cell_ref  — fixed battlefield position set at init. Never changes.
    cell_pos  — current battlefield position. Updated by advance_cells.
    cell_vec  — current movement vector per cell (dr, dc). Allows per-cell
                formation-role targeting (Horseshoe wings, Arrowhead tip).

    cells()   — list(cell_pos.values())
    centroid  — mean of cell_pos positions

    Contention revert: cell_pos[oc] = _prev_pos[oc]  (clean, no arithmetic)
    Displacement ripple: shift cell_pos along loser's vector, propagate
        to cells behind along same axis.

    [canonical: Jordan design — relative origins, per-cell vectors]
    """
    shape: str
    troop_type: str
    tier: int
    starting_position: Tuple[int, int]
    advance_dir: int = 1
    stance: str = "balanced"
    unit_type: str = "melee"
    order_target_idx: Optional[int] = None
    # v24: relative-origin model — per-cell positions
    cell_ref: Dict[Tuple[int, int], Tuple[int, int]] = field(default_factory=dict)
    cell_pos: Dict[Tuple[int, int], Tuple[int, int]] = field(default_factory=dict)
    cell_vec: Dict[Tuple[int, int], Tuple[int, int]] = field(default_factory=dict)
    _prev_pos: Dict[Tuple[int, int], Tuple[int, int]] = field(default_factory=dict)
    halted_cells: Set[Tuple[int, int]] = field(default_factory=set)
    target_atom: Optional[object] = field(default=None, repr=False)
    cell_last_speed: Dict[Tuple[int, int], int] = field(default_factory=dict)
    cell_facing_vec: Dict[Tuple[int, int], Tuple[int, int]] = field(default_factory=dict)
    merged_cells: Set[Tuple[int, int]] = field(default_factory=set)
    _moved_this_turn: Set[Tuple[int, int]] = field(default_factory=set)
    # v25: per-cell sticky Phase 2 flag for Horseshoe wings. Once a wing cell
    # has reached its wide-spread position and entered Phase 2 (closing inward
    # toward enemy edge), it stays in Phase 2. Prevents oscillation between
    # spread and engage targets at the boundary.
    wing_phase_2_cells: Set[Tuple[int, int]] = field(default_factory=set)

    def __post_init__(self):
        """Initialise per-cell reference positions and default vectors."""
        if self.cell_ref:
            return  # already initialised (e.g. copy)
        op = oriented_pattern(self.shape, self.tier, self.advance_dir)
        for orig_r, orig_c, or_r, or_c in op:
            ref = (self.starting_position[0] + or_r,
                   self.starting_position[1] + or_c)
            self.cell_ref[(orig_r, orig_c)] = ref
            self.cell_pos[(orig_r, orig_c)] = ref
            # Default vector: straight forward along advance_dir, no lateral
            # [canonical: Jordan design — cells maintain assigned file]
            self.cell_vec[(orig_r, orig_c)] = (self.advance_dir, 0)

    @property
    def troop_count(self): return TROOPS_PER_TIER[self.tier]

    def cells(self):
        return list(self.cell_pos.values())

    def centroid(self):
        c = self.cells()
        if not c: return self.starting_position
        return (sum(r for r, _ in c) / len(c), sum(x for _, x in c) / len(c))

    def advance_cells(self, discipline, target_centroid, enemy_cells=None):
        """
        v24: relative-origin advance. Each cell moves along its vector toward
        a per-cell target derived from its formation role and the enemy position.

        Formation-role targets (computed from enemy_cells span):
          - ALL cells:           target_col = cell_ref_col (column-local, preserves file)
                                 target_row = enemy_centroid_row
          - Horseshoe wings:     target_row past enemy (wrap-around envelopment)
            Wing = any cell whose ref_col is OUTSIDE the enemy's column span.
            They advance straight along their column, which is already outside the
            enemy's span, so they pass the enemy's front without collision and arrive
            at the flank/rear. No lateral steering needed.
            [canonical: §A.6 — Horseshoe = Envelopment; Jordan design — wings are
             wider than enemy, so column-local advance naturally produces wrap-around]
          - Arrowhead tip:       target_row 2 rows past enemy centroid (penetration).
            Tip cell (orig_r==0) at speed 2 pierces through the enemy front row.
            [canonical: §A.6 — Wedge breaks line; Jordan design — speed+penetration]

        Displacement ripple happens in resolve_cross_side_contention (not here).
        [canonical: Jordan design — relative origins, per-cell vectors]
        """
        if self.stance == "hold": return

        # Snapshot positions before advance (for contention revert)
        self._prev_pos = dict(self.cell_pos)
        self._moved_this_turn = set()

        op = oriented_pattern(self.shape, self.tier, self.advance_dir)
        disc_mult = 1.0 if discipline >= 5 else (0.7 if discipline >= 3 else 0.4)
        stance_mod = STANCE_SPEED_MOD[self.stance]

        all_speeds = [cell_speed(self.shape, self.tier, r, c) for r, c, _, _ in op]
        nonzero_speeds = [s for s in all_speeds if s > 0]
        min_speed = min(nonzero_speeds) if nonzero_speeds else 0

        # Pre-compute enemy column span for formation-role targeting
        enemy_min_col = enemy_max_col = None
        if enemy_cells:
            enemy_col_list = [c for _, c in enemy_cells]
            if enemy_col_list:
                enemy_min_col = min(enemy_col_list)
                enemy_max_col = max(enemy_col_list)

        for orig_r, orig_c, or_r, or_c in op:
            if (orig_r, orig_c) in self.halted_cells: continue
            base_speed = cell_speed(self.shape, self.tier, orig_r, orig_c)
            if base_speed == 0: continue
            actual_speed = max(0, math.floor(base_speed * disc_mult) + stance_mod)
            if actual_speed == 0: continue

            # Tip support: fast cells can't outrun slow cells by more than TIP_SUPPORT_GAP
            if TIP_SUPPORT_ENABLED and base_speed > min_speed:
                # Measure how far this cell has advanced relative to slowest cells
                cur_r, cur_c = self.cell_pos[(orig_r, orig_c)]
                ref_r, ref_c = self.cell_ref[(orig_r, orig_c)]
                my_adv = abs(cur_r - ref_r)
                slow_advs = [
                    abs(self.cell_pos[(r2, c2)][0] - self.cell_ref[(r2, c2)][0])
                    for r2, c2, _, _ in op
                    if cell_speed(self.shape, self.tier, r2, c2) == min_speed
                ]
                if slow_advs and my_adv >= min(slow_advs) + TIP_SUPPORT_GAP:
                    continue

            cur_r, cur_c = self.cell_pos[(orig_r, orig_c)]
            ref_col = self.cell_ref[(orig_r, orig_c)][1]

            if not target_centroid:
                # No target — advance straight forward
                new_r = cur_r + actual_speed * self.advance_dir
                new_c = cur_c
                r_step, c_step = actual_speed * self.advance_dir, 0
            else:
                # Per-cell target computation
                tgt_row = target_centroid[0]
                tgt_col = ref_col  # column-local: each cell keeps its starting column

                if self.shape == "Horseshoe" and enemy_min_col is not None and enemy_cells:
                    # v25 DYNAMIC WIDE WING PATHING [canonical: Jordan 2026-05-15]
                    # Wings position relative to the ENEMY'S WIDEST OCCUPIED COLUMN
                    # (enemy_min_col for left wing, enemy_max_col for right wing),
                    # NOT the enemy centroid. Each wing is a contiguous block of
                    # cells that targets a position OUTSIDE the enemy's lateral
                    # extent by a tactical buffer (~6 cols). Extreme cases hit
                    # the battlefield margins.
                    #
                    # Per Jordan: if enemy's widest cell is at col 9, a 3-wide
                    # left horseshoe wing would target cols 1-3 — wing's
                    # innermost cell ~6 cols clear of enemy's edge.
                    #
                    # Each wing cell within the wing keeps its relative position:
                    # outermost cells go furthest out, innermost cells closest
                    # to where the wing turns inward.
                    #
                    # Phase 1 (Spread): cell hasn't reached its wide target col.
                    #                   Move toward (enemy_centroid_row, wide_col).
                    # Phase 2 (Engage): cell has reached its wide flank position.
                    #                   Move toward enemy's flank edge cells.
                    hs_sizes = {1: 2, 2: 2, 3: 3, 4: 3}
                    hs_wing_w = hs_sizes.get(self.tier, 3)  # center pattern col
                    hs_depth_sizes = {1: 2, 2: 3, 3: 3, 4: 4}
                    hs_depth = hs_depth_sizes.get(self.tier, 4)
                    is_back_row = (orig_r == hs_depth)
                    is_center_col = (orig_c == hs_wing_w)
                    is_wing = (not is_back_row) and (not is_center_col)
                    if is_wing:
                        # Wing extremity: 1 = innermost, hs_wing_w = outermost
                        extremity = abs(orig_c - hs_wing_w)
                        wing_dir = -1 if orig_c < hs_wing_w else +1
                        LATERAL_BUFFER = WING_LATERAL_BUFFER  # module constant

                        if wing_dir < 0:
                            # Left wing: target cols LEFT of enemy_min_col
                            # Innermost (extremity=1) at enemy_min_col - LATERAL_BUFFER
                            # Outermost (extremity=hs_wing_w) at innermost - (hs_wing_w - 1)
                            innermost_target_col = enemy_min_col - LATERAL_BUFFER
                            target_col = innermost_target_col - (extremity - 1)
                            # Clamp to left margin (col 1 minimum)
                            target_col = max(1, target_col)
                        else:
                            # Right wing: target cols RIGHT of enemy_max_col
                            innermost_target_col = enemy_max_col + LATERAL_BUFFER
                            target_col = innermost_target_col + (extremity - 1)
                            target_col = min(BATTLEFIELD_WIDTH - 2, target_col)

                        # Per-cell target row maintains wing's row structure.
                        # Wing's middle row (orig_r = (hs_depth-1)/2 ≈ 1) at enemy
                        # centroid. Front cells advanced past centroid (in advance_dir),
                        # back cells slightly behind centroid.
                        middle_pat_r = (hs_depth - 1) // 2  # ≈ 1 for tier 3 (depth 3)
                        # For A (advance_dir=-1): orig_r=0 is FRONT (lower row),
                        # should target LOWER row than middle.
                        # For B (advance_dir=+1): orig_r=0 is FRONT, oriented to HIGHER row.
                        # The offset is (orig_r - middle_pat_r) * (-advance_dir).
                        target_row = (target_centroid[0]
                                       + (orig_r - middle_pat_r) * (-self.advance_dir))

                        # Phase 2 check: have we reached our wide flank position?
                        # Once a cell has reached its wide target col, transition
                        # to Phase 2 PERMANENTLY (sticky). This prevents oscillation
                        # between Phase 1 (spread) and Phase 2 (close) at the boundary.
                        cell_key = (orig_r, orig_c)
                        if cell_key not in self.wing_phase_2_cells:
                            # Check if cell has reached wide position
                            if wing_dir < 0:
                                reached_wide = (cur_c <= target_col + 1)
                            else:
                                reached_wide = (cur_c >= target_col - 1)
                            if reached_wide:
                                self.wing_phase_2_cells.add(cell_key)

                        if cell_key in self.wing_phase_2_cells:
                            # Phase 2: close inward toward enemy's near edge
                            if wing_dir < 0:
                                target_col = enemy_min_col  # close to left edge
                            else:
                                target_col = enemy_max_col  # close to right edge
                            target_row = target_centroid[0]

                        tgt_row, tgt_col = target_row, target_col

                elif self.shape == "Arrowhead" and orig_r == 0:
                    # Tip cell: pierce 2 rows past enemy centroid along advance_dir
                    # [canonical: §A.6 — Wedge breaks line; Jordan design]
                    tgt_row = target_centroid[0] + 2 * self.advance_dir

                if self.stance == "retreat":
                    tgt_row = 2 * cur_r - tgt_row
                    tgt_col = 2 * cur_c - tgt_col

                dr = tgt_row - cur_r
                dc = tgt_col - cur_c
                abs_dr, abs_dc = abs(dr), abs(dc)
                total = abs_dr + abs_dc
                if total < 0.5: continue

                r_step = round(actual_speed * (abs_dr / total))
                c_step = actual_speed - r_step
                r_step = r_step * (1 if dr > 0 else -1) if abs_dr > 0 else 0
                c_step = c_step * (1 if dc > 0 else -1) if abs_dc > 0 else 0
                new_r = cur_r + r_step
                new_c = cur_c + c_step

            self.cell_pos[(orig_r, orig_c)] = (new_r, new_c)
            self.cell_vec[(orig_r, orig_c)] = (r_step if target_centroid else actual_speed * self.advance_dir,
                                               c_step if target_centroid else 0)
            self.cell_last_speed[(orig_r, orig_c)] = actual_speed
            self.cell_facing_vec[(orig_r, orig_c)] = self.cell_vec[(orig_r, orig_c)]
            self._moved_this_turn.add((orig_r, orig_c))

    def get_cell_facing(self, orig_r, orig_c):
        """Return the facing vector for a cell. Default: advance_dir if never moved."""
        return self.cell_facing_vec.get((orig_r, orig_c),
                                        self.cell_vec.get((orig_r, orig_c), (self.advance_dir, 0)))

    def halt_before_enemy(self, enemy_unit):
        """v25: no-op. Line stability is handled by pre-turn pre_pairs halting
        (cells found adjacent in the prior tick are marked halted_cells and
        skipped in advance_cells), plus resolve_cross_side_contention for
        overlap resolution.

        halt_before_enemy was causing a B-side ordering bias: A halted first
        (reverted positions), then B's halt was computed against A's REVERTED
        positions, giving B a consistent positional advantage (30/70 in mirror
        tests). Removing it restores 50/50 mirror symmetry.

        Speed-2 tip penetration is handled by contention: tip wins against
        speed-1 infantry and advances past them naturally.
        [canonical: Jordan design — contact line stability via pre_pairs + contention]
        """
        pass

    def role_at_contact(self, contact_col):
        if self.shape == "Line": return "normal"
        if self.shape == "Arrowhead":
            for oc, (pos_r, pos_c) in self.cell_pos.items():
                if oc[0] == 0 and abs(pos_c - contact_col) <= 0.5: return "tip"
            return "flank"
        if self.shape == "Horseshoe":
            sizes = {1: 2, 2: 2, 3: 3, 4: 3}
            wing_w = sizes.get(self.tier, 3)
            # Center gap column in starting position space
            center_ref_col = self.starting_position[1] + wing_w
            if abs(contact_col - center_ref_col) <= 0.5: return "center"
            return "flank_engaged"
        if self.shape == "GappedLine":
            sizes = {1: 2, 2: 3, 3: 4, 4: 4}
            half_w = sizes.get(self.tier, 4)
            gap_ref_col = self.starting_position[1] + half_w
            if abs(contact_col - gap_ref_col) <= 0.5: return "gap"
            return "flank_engaged"
        if self.shape == "RefusedFlank":
            sizes = {1: 3, 2: 4, 3: 5, 4: 6}
            width = sizes.get(self.tier, 6)
            refused_ref_col = self.starting_position[1] + (width - 1)
            if abs(contact_col - refused_ref_col) <= 0.5: return "refused"
            return "engaged"
        return "normal"

    def resolve_internal_collisions(self, unit_discipline):
        """v24: discipline-gated formation hold — adapted to cell_pos model.
        [canonical: Jordan design — discipline-gated cell hold]
        """
        if not self._prev_pos:
            return (0, 0)
        pos_to_cells = {}
        for oc, pos in self.cell_pos.items():
            pos_to_cells.setdefault(pos, []).append(oc)
        n_halted = 0
        n_merged = 0
        for pos, cells in pos_to_cells.items():
            if len(cells) <= 1: continue
            cells_sorted = sorted(cells, key=lambda c: (c[0], c[1]))
            anchor = cells_sorted[0]
            for trailing in cells_sorted[1:]:
                roll = random.randint(1, 10)
                if roll <= unit_discipline:
                    self.cell_pos[trailing] = self._prev_pos.get(trailing, self.cell_ref.get(trailing, pos))
                    self.cell_facing_vec[trailing] = self.cell_facing_vec.get(trailing, (self.advance_dir, 0))
                    n_halted += 1
                else:
                    anc_fv = self.cell_facing_vec.get(anchor, (self.advance_dir, 0))
                    tr_fv = self.cell_facing_vec.get(trailing, (self.advance_dir, 0))
                    mid_fv = ((anc_fv[0] + tr_fv[0]) / 2, (anc_fv[1] + tr_fv[1]) / 2)
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

    def __post_init__(self):
        total = sum(a.troop_count for a in self.subunits)
        self.size = max(1, total // TROOPS_PER_SIZE)
        self.size_max = self.size
        self.h_per_size = max(1, min(self.discipline, self.command) + self.dr)
        # v19: HP = TroopCount = Size × BLOCK_SIZE. Bottom-up: damage = soldier casualties.
        # [canonical: derived_stats architecture — "TroopCount = Size × block_size"]
        self.hp_max = self.size_max * BLOCK_SIZE
        self.hp = float(self.hp_max)
        self.effective_size = float(self.size)  # v16: continuous, not floored
        self.stamina = STAMINA_MAX
        self.stamina_max = STAMINA_MAX
        for a in self.subunits:
            if a.stance == "balanced": a.stance = self.stance

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
        raw = min(self.effective_size, self.command) + self.command + pen + stam_pen
        return max(1, math.floor(raw))

    def check_drift(self):
        for a in self.subunits:
            if self.discipline < MIN_DISCIPLINE[a.shape] and a.shape != "Line":
                a.shape = "Line"

# ─── DICE ────────────────────────────────────────────────────────────────────

def roll_pool(n, tn=7):
    net = 0
    for _ in range(max(1, n)):
        f = random.randint(1, 10)
        if f == 1:         net -= 1
        elif tn <= f <= 9: net += 1
        elif f == 10:      net += 2
    return net

def compute_degree(net, ob):
    if net <= 0:                    return "Failure"
    if net >= 2 * ob and net >= 3:  return "Overwhelming"
    if net >= ob:                   return "Success"
    return "Partial"

DAMAGE_BY_DEGREE = {"Overwhelming": lambda p: 1+p, "Success": lambda p: p,
                     "Partial": lambda p: 1,        "Failure": lambda p: 0}

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
    """v24: cross-side cell contention with displacement ripple.

    Speed-priority resolution (v13 model preserved):
      - faster cell keeps the position; slower cell reverts to _prev_pos
      - equal speed: both cells co-locate; combat (find_contacts) resolves

    Displacement ripple (NEW v24):
      When a faster cell forces a slower cell back, any cells of the SAME
      subunit that are immediately behind the loser (along the loser's
      advance vector) are also pushed back one step. This models the
      historical reality that a penetrating cavalry cell or wedge tip
      forces the cells behind the contact to shuffle backward — the
      "ripple" Jordan described.

      Ripple cap: 3 cells deep (prevents runaway cascade in tight formations).
      Only fires when the loser's displacement is non-zero (it actually moved).

    Size/random tiebreakers deferred (see v13 manifest reasoning).
    [canonical: Jordan design — relative origins + displacement ripple]
    """
    def collect(unit):
        """abs_pos → [(subunit, orig_coord, speed)]"""
        result = {}
        for su in unit.subunits:
            for oc, pos in su.cell_pos.items():
                speed = su.cell_last_speed.get(oc, 0) if oc in su._moved_this_turn else 0
                result.setdefault(pos, []).append((su, oc, speed))
        return result

    def ripple(su, oc, depth=0, visited=None):
        """Push back cells behind oc along oc's vector. Max depth 3."""
        if depth >= 3: return
        if visited is None: visited = set()
        if oc in visited: return
        visited.add(oc)
        vec = su.cell_vec.get(oc, (su.advance_dir, 0))
        if vec == (0, 0): return
        cur_r, cur_c = su.cell_pos[oc]
        # Cell directly BEHIND oc (opposite of its vector direction)
        behind_pos = (cur_r - vec[0], cur_c - vec[1])
        for oc2, pos2 in su.cell_pos.items():
            if oc2 == oc: continue
            if pos2 == behind_pos:
                # Push this cell back one step in oc's direction (i.e. backward for it too)
                su.cell_pos[oc2] = (pos2[0] - vec[0], pos2[1] - vec[1])
                ripple(su, oc2, depth + 1, visited)

    a_pos = collect(unit_a)
    b_pos = collect(unit_b)
    contested = set(a_pos.keys()) & set(b_pos.keys())
    n_resolved = 0

    for pos in contested:
        a_cells_here = a_pos[pos]
        b_cells_here = b_pos[pos]
        a_speed = max(sp for _, _, sp in a_cells_here)
        b_speed = max(sp for _, _, sp in b_cells_here)
        if a_speed == 0 and b_speed == 0:
            continue  # stale — neither moved here this turn

        if a_speed > b_speed:
            losers = b_cells_here
            winners = a_cells_here
        elif b_speed > a_speed:
            losers = a_cells_here
            winners = b_cells_here
        else:
            # Equal speed — random tiebreaker (50/50 who keeps the cell).
            # [canonical: Jordan design 2026-05-12 — "if same size, then randomised
            #  who gets that space"; size tiebreaker deferred, random applied now]
            if random.random() < 0.5:
                losers, winners = b_cells_here, a_cells_here
            else:
                losers, winners = a_cells_here, b_cells_here

        for su, oc, cell_speed_val in losers:
            if oc in su._moved_this_turn:
                # Loser moved this turn → revert to previous position
                prev = su._prev_pos.get(oc)
                if prev is not None:
                    su.cell_pos[oc] = prev
                    ripple(su, oc)
                    n_resolved += 1
            else:
                # Loser is STATIONARY — winner displaces it ONLY if winner is
                # clearly faster (speed ≥ 2). Equal-speed contact (infantry vs
                # infantry) should halt the winner, not push the loser back.
                # [canonical: Jordan design — cavalry displaces infantry;
                #  infantry stops at contact line against equal-speed enemy]
                winner_speed = max(sp for _, _, sp in winners) if winners else 0
                if winner_speed >= 2 and winners:
                    w_su, w_oc, _ = winners[0]
                    w_pos = w_su.cell_pos.get(w_oc, pos)
                    dr = pos[0] - w_pos[0]
                    dc = pos[1] - w_pos[1]
                    mag = max(1, abs(dr) + abs(dc))
                    push_r = round(dr / mag)
                    push_c = round(dc / mag)
                    new_pos = (su.cell_pos[oc][0] + push_r, su.cell_pos[oc][1] + push_c)
                    su.cell_pos[oc] = new_pos
                    su.cell_vec[oc] = (push_r, push_c)
                    ripple(su, oc)
                    n_resolved += 1
                elif winners:
                    # Equal-speed: winner should also halt (can't push stationary equal)
                    # Revert winner to its previous position
                    for w_su, w_oc, _ in winners:
                        if w_oc in w_su._moved_this_turn:
                            w_prev = w_su._prev_pos.get(w_oc)
                            if w_prev is not None:
                                w_su.cell_pos[w_oc] = w_prev
                                n_resolved += 1

    return n_resolved




def update_cell_facings(unit_a, unit_b):
    """v25: cells in contact rotate to face the primary enemy.

    Every combatant faces the threat most aligned with their advance direction
    (the direction they're fighting toward). If multiple enemies are at the same
    advance_dir distance, prefer the one in the same column — this gives formation-
    level coherence (cells face straight ahead, not diagonally).

    This preserves flank/rear angles: a cell facing its primary frontal threat
    shows its side/back to any attacker coming from a different direction.

    [canonical: Jordan design — cells rotate to face enemy if they can;
     primary threat = most advance_dir-aligned, same-column preference]
    """
    for unit, enemy_unit in [(unit_a, unit_b), (unit_b, unit_a)]:
        enemy_positions = set(pos for su in enemy_unit.subunits
                              for pos in su.cell_pos.values())
        for su in unit.subunits:
            for oc, pos in su.cell_pos.items():
                adjacent_enemies = [
                    (er, ec) for er, ec in enemy_positions
                    if max(abs(pos[0] - er), abs(pos[1] - ec)) <= 1
                ]
                if not adjacent_enemies:
                    continue  # not in contact — keep current facing

                # Find the enemy most aligned with advance_dir
                # (the primary threat: the one the cell is fighting toward)
                max_align = max(
                    (ep[0] - pos[0]) * su.advance_dir for ep in adjacent_enemies
                )
                candidates = [
                    ep for ep in adjacent_enemies
                    if (ep[0] - pos[0]) * su.advance_dir == max_align
                ]
                # Prefer same column (straight ahead) to keep formation facing coherent
                same_col = [ep for ep in candidates if ep[1] == pos[1]]
                target = same_col[0] if same_col else min(
                    candidates, key=lambda ep: abs(ep[1] - pos[1])
                )
                su.cell_facing_vec[oc] = (target[0] - pos[0], target[1] - pos[1])


def find_contacts(unit_a, unit_b):
    pairs = []
    a_cells = {id(a): set(a.cells()) for a in unit_a.subunits}
    b_cells = {id(b): set(b.cells()) for b in unit_b.subunits}
    for atom_a in unit_a.subunits:
        for atom_b in unit_b.subunits:
            ca = a_cells[id(atom_a)]
            cb = b_cells[id(atom_b)]
            # v24: deduplicate — each cell appears at most once in contact list.
            # Previous code appended one A cell per adjacent B cell, inflating
            # contact counts N× for cells adjacent to multiple enemies.
            seen_a, seen_b = set(), set()
            contact_cells_a, contact_cells_b, contact_cols = [], [], set()
            for (ra, c) in ca:
                for (rb, cb_) in cb:
                    if abs(ra-rb) <= 1 and abs(c-cb_) <= 1:
                        if (ra, c) not in seen_a:
                            contact_cells_a.append((ra, c))
                            seen_a.add((ra, c))
                        if (rb, cb_) not in seen_b:
                            contact_cells_b.append((rb, cb_))
                            seen_b.add((rb, cb_))
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
    op = oriented_pattern(atom.shape, atom.tier, atom.advance_dir)
    for abs_r, abs_c in contact_abs_cells:
        for orig_r, orig_c, or_r, or_c in op:
            comp_r, comp_c = atom.cell_pos.get((orig_r, orig_c), (0, 0))
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

def resolve_engagements(unit_a, unit_b, pairs, dynamic_facings=None):
    """Resolve all contact pairs.
    F-i: support_engage_frac replaces bare engage_frac.
    F-ii: puncture bonus from momentum differential.
    dynamic_facings: per-cell facing dict for F-iii (None -> default advance_dir)."""
    dmg_a, dmg_b = 0, 0
    eng_counts = count_engagements_per_atom(pairs)
    for p in pairs:
        atom_a, atom_b = p["atom_a"], p["atom_b"]
        cols = p["cols"]
        primary_col = sorted(cols)[len(cols)//2]
        role_a = atom_a.role_at_contact(primary_col)
        role_b = atom_b.role_at_contact(primary_col)
        off_a = SHAPE_OFF_MOD[atom_a.shape](role_a)
        off_b = SHAPE_OFF_MOD[atom_b.shape](role_b)
        if off_a == -99 or off_b == -99: continue

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

        a_pool = max(1, math.floor(a_pool_raw) + off_a)
        b_pool = max(1, math.floor(b_pool_raw) + off_b)

        # v25: Per-cell angle pool modifier with correct facing from update_cell_facings.
        # Pool reduction (ANGLE_DEF_MOD) not damage multiplication — angle advantage is a
        # probability shift (harder to defend from side/rear), not a damage amplifier.
        # v14 achieved 12/13 in-band with this approach at the right pool scale.
        # [canonical: Jordan design — GREEN/YELLOW/RED pool modifier per cell]
        a_set = set(p["a_cells"])
        b_set = set(p["b_cells"])

        abs_to_orig_a = {pos: oc for oc, pos in atom_a.cell_pos.items()}
        abs_to_orig_b = {pos: oc for oc, pos in atom_b.cell_pos.items()}

        def get_zone(atk_pos, def_pos, def_atom, abs_to_orig_def):
            oc = abs_to_orig_def.get(def_pos)
            fac = def_atom.get_cell_facing(*oc) if oc else (def_atom.advance_dir, 0)
            zone, _ = octagon_angle(atk_pos, def_pos, fac)
            return zone

        # Per-defender-cell angle mods; one entry per unique defender cell in contact
        b_mods, b_seen = [], set()  # B defends vs A attacks
        a_mods, a_seen = [], set()  # A defends vs B attacks
        cell_pair_count = 0
        for ar, ac in a_set:
            for dr_o, dc_o in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                bp = (ar + dr_o, ac + dc_o)
                if bp in b_set:
                    cell_pair_count += 1
                    if bp not in b_seen:
                        b_seen.add(bp)
                        z = get_zone((ar, ac), bp, atom_b, abs_to_orig_b)
                        b_mods.append(ANGLE_DEF_MOD[z])
        for br, bc in b_set:
            for dr_o, dc_o in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                ap = (br + dr_o, bc + dc_o)
                if ap in a_set and ap not in a_seen:
                    a_seen.add(ap)
                    z = get_zone((br, bc), ap, atom_a, abs_to_orig_a)
                    a_mods.append(ANGLE_DEF_MOD[z])

        # Average angle modifier → applied to DEFENDER pool
        # a attacks b → b_pool reduced; b attacks a → a_pool reduced
        b_angle_mod = round(sum(b_mods) / len(b_mods)) if b_mods else 0
        a_angle_mod = round(sum(a_mods) / len(a_mods)) if a_mods else 0
        a_pool = max(1, a_pool + a_angle_mod)
        b_pool = max(1, b_pool + b_angle_mod)

        # Frontage pool bonus: wider coordinated contact = higher success probability
        frontage_bonus = min(PUNCTURE_CAP, cell_pair_count // 2)
        a_pool_eff = max(1, a_pool + frontage_bonus)
        b_pool_eff = max(1, b_pool + frontage_bonus)

        # Attention split: if a cell is attacked from non-GREEN while frontally engaged,
        # its effective pool is reduced. Applied to the most-attacked cell as representative.
        # [canonical: Jordan design — cannot commit full pool against each cell it's facing]
        def attention_mod(def_zones_list):
            """Return pool modifier for a cell attacked from multiple directions.

            v25 cap: max penalty is -2 (representing up to 2 simultaneous
            non-frontal threats that a unit must split attention to cover).
            Beyond that, soldiers adapt formation; further attackers don't
            multiply the penalty indefinitely.
            [canonical: Jordan design — attention split penalises flanked cells
             but should not collapse the entire unit's pool from one bad cell]
            """
            if not def_zones_list: return 0
            if all(z == "GREEN" for z in def_zones_list): return 0
            non_green = sum(1 for z in def_zones_list if z != "GREEN")
            return -min(2, non_green)  # cap: max -2 pool penalty

        # Build per-cell zone lists for attention split
        b_cell_atk_zones = {}
        a_cell_atk_zones = {}
        for ar, ac in a_set:
            for dr_o, dc_o in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                bp = (ar + dr_o, ac + dc_o)
                if bp in b_set:
                    z = get_zone((ar, ac), bp, atom_b, abs_to_orig_b)
                    b_cell_atk_zones.setdefault(bp, []).append(z)
        for br, bc in b_set:
            for dr_o, dc_o in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                ap = (br + dr_o, bc + dc_o)
                if ap in a_set:
                    z = get_zone((br, bc), ap, atom_a, abs_to_orig_a)
                    a_cell_atk_zones.setdefault(ap, []).append(z)

        if b_cell_atk_zones:
            worst_b = max(b_cell_atk_zones.values(), key=len)
            b_pool_eff = max(ATTENTION_SPLIT_MIN_POOL, b_pool_eff + attention_mod(worst_b))
        if a_cell_atk_zones:
            worst_a = max(a_cell_atk_zones.values(), key=len)
            a_pool_eff = max(ATTENTION_SPLIT_MIN_POOL, a_pool_eff + attention_mod(worst_a))

        a_net = roll_pool(a_pool_eff)
        b_net = roll_pool(b_pool_eff)
        a_deg = compute_degree(a_net, max(1, b_net))
        b_deg = compute_degree(b_net, max(1, a_net))
        dmg_a += max(0, DAMAGE_BY_DEGREE[b_deg](unit_b.power) - unit_a.dr)
        dmg_b += max(0, DAMAGE_BY_DEGREE[a_deg](unit_a.power) - unit_b.dr)

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

    def fire(shooter_atom, shooter_unit, target_atoms):
        """Pick nearest in-range target atom, roll Power vs TN, return Size loss inflicted."""
        if shooter_atom.unit_type != "ranged":
            return 0, None
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
        return net_after_dr, best_target

    for atom in unit_a.subunits:
        dmg, tgt = fire(atom, unit_a, unit_b.subunits)
        if tgt is not None:
            loss_b += dmg
            shots += 1
    for atom in unit_b.subunits:
        dmg, tgt = fire(atom, unit_b, unit_a.subunits)
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
            # v24: use cell_pos (pos→orig_coord inverse map) for halted_cells assignment
            pos_to_orig_a = {pos: oc for oc, pos in p["atom_a"].cell_pos.items()}
            for cell in p["a_cells"]:
                oc = pos_to_orig_a.get(cell)
                if oc: p["atom_a"].halted_cells.add(oc)
            pos_to_orig_b = {pos: oc for oc, pos in p["atom_b"].cell_pos.items()}
            for cell in p["b_cells"]:
                oc = pos_to_orig_b.get(cell)
                if oc: p["atom_b"].halted_cells.add(oc)
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
        # v25: cells in contact rotate to face primary enemy (most advance_dir-aligned,
        # same-column preference). Must run after positions settle, before engagement.
        # [canonical: Jordan design — cells rotate to face enemy if they can]
        update_cell_facings(unit_a, unit_b)
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
        # v25: opp_frac scaling REMOVED.
        # Previously scaled damage by opponent contact fraction (5/25 = 0.2 for a
        # fresh Line contact). The cell-level weight system (weight_b_takes /
        # FRONTAGE_REF) already captures engagement quality bottom-up; applying
        # opp_frac on top created a 5× suppression that cancelled the angle mechanics.
        # [REMOVED: v20 opp_frac block — superseded by cell-level weights]
        # v21: SIMULTANEOUS HP — apply damage to both units, THEN recalc_size
        # for both. Prevents size recalc of unit_a from affecting anything
        # before unit_b's damage is applied.
        # [canonical: params/mass_combat.md PP-233 — "Damage is simultaneous.
        #  Both sides deal and receive damage before Size is recalculated."]
        unit_a.hp = max(0, unit_a.hp - result["dmg_a"] - volley_dmg_a * volley_hp_scale(unit_a))
        unit_b.hp = max(0, unit_b.hp - result["dmg_b"] - volley_dmg_b * volley_hp_scale(unit_b))
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
        total_dmg_a_morale = result.get("dmg_a", 0) + volley_dmg_a * volley_hp_scale(unit_a)
        total_dmg_b_morale = result.get("dmg_b", 0) + volley_dmg_b * volley_hp_scale(unit_b)
        for u, total_dmg in [(unit_a, total_dmg_a_morale), (unit_b, total_dmg_b_morale)]:
            if u.routed: continue
            # General death: Command=0 → instant rout (M1: general IS the army)
            # [canonical: designs/provincial/mass_battle_v30.md §A.4 — "General killed: Morale −2 (uncapped)"]
            if u.command <= 0:
                u.morale = 0.0
                continue  # rout check below
            if total_dmg > 0 and u.discipline > 0:
                erosion = total_dmg / (u.discipline * u.command)
                u.morale -= erosion
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
        # v24: re-initialise cell_ref and cell_pos from new starting_position
        atom.cell_ref.clear()
        atom.cell_pos.clear()
        atom.cell_vec.clear()
        atom._prev_pos.clear()
        atom.halted_cells.clear()
        atom._moved_this_turn.clear()
        op = oriented_pattern(atom.shape, atom.tier, atom.advance_dir)
        for orig_r, orig_c, or_r, or_c in op:
            ref = (start_row + or_r, anchor_col + or_c)
            atom.cell_ref[(orig_r, orig_c)] = ref
            atom.cell_pos[(orig_r, orig_c)] = ref
            atom.cell_vec[(orig_r, orig_c)] = (atom.advance_dir, 0)


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
    raw_dmg = a_net * (1 + pursuer.power)
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
    dmg = max(0, DAMAGE_BY_DEGREE[a_deg](freed_unit.power) - target_unit.dr)
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
