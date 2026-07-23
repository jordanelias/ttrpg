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
from mass_battle.core.exchange import *  # [Stage-1] pool primitives extracted to core.exchange
from mass_battle.core.state import *  # [Stage-1] morale/discipline/rout transitions extracted to core.state
from mass_battle.core.attrition import *  # [Stage-1] Lanchester attrition law extracted to core.attrition
from mass_battle.core.contact import *  # [Stage-1] targeting/contact extracted to core.contact
from mass_battle.troop_types.registry import *  # [Stage-1] troop-type stats/roles extracted
from mass_battle.hierarchy.units import *  # [Stage-1] Subunit/Unit data model extracted
from mass_battle.resolution import *  # [Stage-1] sigma head (roll/degree/morale-sigma/trace) — restored: import rode into hierarchy with the class block
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


def _subunit_depth(atom):
    # Rank count (rows) of ONE subunit's pattern = its internal reserve depth for stamina rotation.
    # For a single-subunit unit this equals _formation_depth(unit) -> byte-exact phase recovery.
    pattern = CELL_PATTERN_FN[atom.shape](atom.tier)
    return (max(r for r, c in pattern) + 1) if pattern else 1


def stamina_check(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """G-1: at phase boundary, recover stamina proportional to formation depth.
    Drain happens per-tick in run_battle; this hook handles rotation recovery.
    [canonical: audit_sim_mb_06_v14.md §G-1 — depth permits front-rank rotation]"""
    for u in [unit_a, unit_b]:
        if u.routed or u.broken:
            continue
        for atom in u.subunits:
            depth = _subunit_depth(atom)
            reserve_ranks = max(0, depth - 1)
            recovery = STAMINA_RECOVERY_PER_RESERVE_RANK * reserve_ranks
            atom.recover_stamina(recovery)


def rally_check(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """Empty hook — rally lands in a future cycle (G-7)."""
    pass

import os as _reform_os
# G-8 reform flag kept in-engine (not config.py) to avoid the sim_fabrication ledger drift on
# config's pre-existing constants; default OFF preserves the calibrated byte-exact baseline.
REFORM_CHECK_ENABLED = _reform_os.environ.get('REFORM_CHECK_ENABLED', '0') == '1'

def reform_check(unit_a, unit_b, phase_idx):  # noqa: ARG001
    # [canonical: mass_battle_v30.md §A.5; PP-241 — Reform Phase Discipline restoration:]
    #   an unengaged unit gains +1 Discipline; requires the general's Command to be at least
    #   one above the unit's current Discipline, and Command of at least two; a Command of one
    #   cannot restore (the Command-asymmetry rule).
    # [canonical: mass_battle_v30.md §A.7 Phase Reform — non-engaged units restore Discipline.]
    """G-8 Reform: an unengaged unit restores one step of Discipline toward its start,
    gated by the general's Command. Flag-gated default OFF (REFORM_CHECK_ENABLED) to
    preserve the calibrated byte-exact baseline; opt-in for re-baseline, mirroring
    PER_CELL / PC_NODE_COHESION. Canon Reform also recovers Morale and merges sub-units —
    not implemented here (separate, morale/lifecycle-touching).
    [ASSUMPTION: cadence — fires per phase-boundary, bounded by discipline_start so a unit
     only recovers what it lost. Canon Reform is once-per-turn (the Reform Phase); the sim's
     phase-boundary count varies with the turn cap, so per-boundary+cap is the conservative
     mapping pending a once-per-turn ruling.]
    """
    if not REFORM_CHECK_ENABLED:
        return
    if find_contacts(unit_a, unit_b):
        return  # any contact pair -> both units engaged (1v1) -> no reform this boundary
    for u in (unit_a, unit_b):
        if u.routed or u.broken:
            continue
        # Command-asymmetry (PP-241 on the citation line above): one cannot restore;
        # restoration needs Command at least one above the (per-subunit) current Discipline.
        if u.command < 2:
            continue
        for atom in u.subunits:
            if atom.routed or atom.broken:
                continue
            if u.command < atom.eff_discipline + 1:
                continue
            if atom.eff_discipline < atom.eff_discipline_start:
                atom.restore_discipline()   # +1 toward start, routes own-else-Unit (byte-exact single-subunit)
        u.check_drift()

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
            if PC_NODE_COHESION and hasattr(atom, '_node_pos'):
                _pr, _pc = atom._node_pos.get((orig_r, orig_c), (0.0, 0.0))
                # [migration H] file-bin the column on ON so comp matches the file-binned cells()/contact
                # cells; OFF = verbatim int(round). FIELD_MOVEMENT/COL_WIDTH via units star-import.
                comp_r, comp_c = (int(round(_pr)), int(round(_pc / COL_WIDTH))) if FIELD_MOVEMENT else (int(round(_pr)), int(round(_pc)))
            if (comp_r, comp_c) == (abs_r, abs_c):
                speeds.append(atom.cell_last_speed.get((orig_r, orig_c), 0))
                break
    return sum(speeds) / len(speeds) if speeds else 0.0

def _cascade_depth_key(pair):
    """Sub-phase ordering: foremost attacker resolves first.
    [canonical: Jordan handoff §(3) — tip arrives first]"""
    atom_a = pair["atom_a"]
    a_cells = pair["a_cells"]
    if not a_cells: return 999  # [canonical: sentinel: 999 = no-cells max distance]
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
import os
PC_FIXING_FLANK = (os.environ.get("PC_FIXING_FLANK", "1") == "1")
PC_ENVELOP_SHOCK = (os.environ.get("PC_ENVELOP_SHOCK", "1") == "1")  # B: envelopment moral-shock on a fixed unit struck flank/rear (toggle; default ON)
PC_VOLLEY_TARGETING = (os.environ.get("PC_VOLLEY_TARGETING", "1") == "1")  # E: atomized archer volley targeting -- an ordered archer fires at + concentrates casualties on its target subunit (toggle; default ON)
# [partition-invariance fix, 2026-07-08, Jordan-ruled "genuine defect -- fix it"] renormalizes a
# convergence group -- >=2 of ONE side's atoms simultaneously, independently fully engaging the
# SAME single opposing atom (e.g. a pinning body plus wings all converging on one Line defender)
# -- back down to what ONE merged atom of the group's combined troops would contribute. Toggle OFF
# reproduces the pre-fix (multiplicative-per-attacker) behaviour byte-exact, for ablation/compare.
PC_CONVERGENCE_NORM = (os.environ.get("PC_CONVERGENCE_NORM", "1") == "1")


def _convergence_scale(unit_a, unit_b, pairs):
    """[partition-invariance fix] `subunit_combat_pool` is, by Jordan's own DG-3 characterization,
    a per-atom COMBAT SCORE (Command + per-subunit discipline/cohesion/stamina) rather than a
    per-troop rate -- deliberately (ED-899: "base driven SOLELY by Command"). `pair_pool_contribution`
    correctly renormalizes when ONE atom is itself split across MULTIPLE enemies (an atom fighting on
    two fronts gets its OWN score divided between them, by troop share). It does nothing for the
    mirror case: when SEVERAL of one side's atoms each independently, fully engage the SAME single
    opposing atom, each gets its own near-full base_pool with no reduction -- so splitting a fixed
    total force into more simultaneously-converging atoms multiplies total dice against that one
    shared target, purely from the split, not from any change in troops or quality. This is exactly
    the mechanism the 2026-07-05 Cannae follow-up (`designs/proposals/mass_battle_fighting_withdrawal_v1.md`
    §7) measured and flagged as a genuinely undecided architecture question; Jordan ruled it a
    genuine defect (2026-07-08) rather than an intended encirclement bonus.

    For every group of >=2 atoms on one side sharing one target atom on the other, this computes
    the troop-weighted-mean base score across the group (`merged_base`) and the group's combined
    own-troop count (`merged_troops`) and combined engaged troops (`total_wt`), then derives what
    ONE merged atom of that combined size would contribute: `(merged_base / merged_troops) *
    total_wt`. Dividing that by the naive (uncorrected) group sum gives a single scale factor
    applied uniformly to every member's own pair contribution -- preserving each member's relative
    share while capping the group's total at the merged-atom figure. A group of size 1 (the
    overwhelming majority of pairs -- every single-subunit-vs-single-subunit gauge row has no other
    shape) is mathematically a no-op (scale 1.0, verified: merged/naive collapse to the same ratio
    algebraically) and is skipped outright below for clarity/speed. Dead atoms (routed/broken,
    base_pool==0 by `subunit_combat_pool`'s own gate) are excluded from a group's aggregate --
    they contribute 0 to `merged_base` already downstream (`a_dead`/`b_dead` zero their net outright),
    so counting their troops in `merged_troops` would only dilute their live siblings' credit for no
    reason.

    Returns (a_scale, b_scale): dicts keyed by (id(atom_a), id(atom_b)) -> float. Missing key means
    1.0 (no convergence for that pair on that side). Only meaningful for POOL_VARIANT=="C-ii" (the
    live variant) -- callers gate application accordingly; this function itself is pure dict/float
    math, safe to compute unconditionally."""
    def _dead(unit, atom):
        return unit.routed or unit.broken or atom.routed or atom.broken

    def _group_and_scale(key_of, attacker_of, attacker_unit, cells_of, out):
        """attacker_of(p)/cells_of(p) select the CONVERGING side's atom/contact-cells for pair p;
        key_of(p) selects the shared TARGET atom the group is defined by. attacker_unit is that
        side's Unit (fixed for the whole call -- unit_a for the a_scale pass, unit_b for b_scale)."""
        groups = {}
        for p in pairs:
            groups.setdefault(id(key_of(p)), []).append(p)
        for group in groups.values():
            if len(group) < 2:
                continue
            infos = []
            for p in group:
                atk = attacker_of(p)
                if _dead(attacker_unit, atk):
                    continue
                base = subunit_combat_pool(attacker_unit, atk)
                wt = _pair_engaged_troops(atk, cells_of(p))
                if base <= 0 or wt <= 0:
                    continue
                infos.append((p, atk, base, wt))
            if len(infos) < 2:
                continue
            total_wt = sum(i[3] for i in infos)
            merged_troops = sum(i[1].cur_troops for i in infos)
            if total_wt <= 0 or merged_troops <= 0:
                continue
            merged_base = sum(i[2] * i[3] for i in infos) / total_wt
            corrected_total = (merged_base / merged_troops) * total_wt
            naive_total = sum((i[2] / i[1].cur_troops) * i[3] for i in infos)
            if naive_total <= 0:
                continue
            factor = corrected_total / naive_total
            for p, atk, base, wt in infos:
                out[(id(p["atom_a"]), id(p["atom_b"]))] = factor

    a_scale, b_scale = {}, {}
    # Group by shared B-side target (>=2 atom_a's converging on one atom_b) -> corrects a_pool_raw
    _group_and_scale(key_of=lambda p: p["atom_b"], attacker_of=lambda p: p["atom_a"],
                      attacker_unit=unit_a, cells_of=lambda p: p["a_cells"], out=a_scale)
    # Group by shared A-side target (>=2 atom_b's converging on one atom_a) -> corrects b_pool_raw
    _group_and_scale(key_of=lambda p: p["atom_a"], attacker_of=lambda p: p["atom_b"],
                      attacker_unit=unit_b, cells_of=lambda p: p["b_cells"], out=b_scale)
    return a_scale, b_scale


def resolve_engagements(unit_a, unit_b, pairs, dynamic_facings=None, t=None, conv_scale=None):
    """Resolve all contact pairs.
    F-i: support_engage_frac replaces bare engage_frac.
    F-ii: puncture bonus from momentum differential.
    dynamic_facings: per-cell facing dict for F-iii (None -> default advance_dir).
    t: current battle tick (None -> old instantaneous-brace behaviour; see resolution._brace_setup_ok),
    threaded to _charge_shock_sigma and the reciprocal-recoil _subunit_braced calls. [ED-1095]"""
    dmg_a, dmg_b = 0, 0
    eng_counts = count_engagements_per_atom(pairs)
    # [ED-MB-0018 fix, balance-critic A1/A1-gap + arch-critic #1] MULTI-SIDE = the set of DISTINCT octagon
    # SIDES a subunit is actually struck from, aggregated over its contact pairs' real attacker-cell
    # BEARINGS (front / left / right / rear, relative to the subunit's own facing) -- NOT the arc-blind
    # pair COUNT (`eng_counts`) the shock used before. The pair count fired on TWO attackers both in the
    # FRONT arc (a concentric frontal pinch, not an encirclement -> false +50%) and MISSED one wide body
    # that genuinely wraps two arcs (`eng_count==1` -> no shock). Deriving the trigger from the cells'
    # bearings fixes both and makes "engaged from >=2 sides" a genuine aggregation over contacts. Only
    # computed under the octagon-damage flag (it drives the graded multi-side shock in the damage block).
    _atom_sides = {}
    if PC_OCTAGON_DMG:
        def _mean_facing(_atom):
            _fv = getattr(_atom, 'cell_facing_vec', None)
            if _fv:
                _rs = sum(v[0] for v in _fv.values()); _cs = sum(v[1] for v in _fv.values())
                if _rs or _cs:
                    return (_rs, _cs)                       # average of the atom's per-cell (wheeled) facings
            return (_atom.advance_dir, 0)                   # nominal facing (no wheel recorded)
        def _nearest_face(_dcells, _dfac, _acen):
            # [Jordan geometry ruling] A subunit's perimeter has four FACE midpoints -- front / rear / left /
            # right lines -- and an attacking body engages the face NEAREST it: a side attack targets the
            # OUTERMOST side line, a rear attack the BACKMOST line (not the centroid, which mislabels both).
            # Faces are the extremes of the footprint projected onto the facing axis (front/rear) and its
            # perpendicular (left/right) -- emergent from the cells, so this stays cell-up.
            _n = len(_dcells)
            _cr = sum(r for r, c in _dcells) / _n; _cc = sum(c for r, c in _dcells) / _n
            _fm = (_dfac[0] ** 2 + _dfac[1] ** 2) ** 0.5 or 1.0
            _fu = (_dfac[0] / _fm, _dfac[1] / _fm)          # facing (front) unit normal
            _pu = (-_fu[1], _fu[0])                          # left-perpendicular unit
            _al = [(r - _cr) * _fu[0] + (c - _cc) * _fu[1] for r, c in _dcells]
            _pp = [(r - _cr) * _pu[0] + (c - _cc) * _pu[1] for r, c in _dcells]
            _faces = {
                'F': (_cr + max(_al) * _fu[0], _cc + max(_al) * _fu[1]),
                'B': (_cr + min(_al) * _fu[0], _cc + min(_al) * _fu[1]),
                'L': (_cr + max(_pp) * _pu[0], _cc + max(_pp) * _pu[1]),
                'R': (_cr + min(_pp) * _pu[0], _cc + min(_pp) * _pu[1]),
            }
            return min(_faces, key=lambda k: (_faces[k][0] - _acen[0]) ** 2 + (_faces[k][1] - _acen[1]) ** 2)
        # MULTI-SIDE = the set of distinct FACES a subunit is struck on, ONE face per contacting enemy body
        # (its contact-cell centroid -> nearest defender face). A wide head-on line hits ONE face (front);
        # two enemy bodies front+rear hit TWO faces -> the genuine encirclement Jordan's "relief divided"
        # describes. Per-cell arc lethality is handled separately in _octagon_dmg_mod; this only gates the
        # graded multi-side shock.
        for _p in pairs:
            for _datom, _atk_cells in ((_p["atom_b"], _p["a_cells"]), (_p["atom_a"], _p["b_cells"])):
                _dcells = list(_datom.cells())
                _ac = list(set(_atk_cells))
                if not _dcells or not _ac:
                    continue
                _acen = (sum(r for r, c in _ac) / len(_ac), sum(c for r, c in _ac) / len(_ac))
                _face = _nearest_face(_dcells, _mean_facing(_datom), _acen)
                _atom_sides.setdefault(id(_datom), set()).add(_face)
    # [partition-invariance fix] conv_scale is precomputed ONCE per TICK on the FULL tick's pairs
    # by the caller (run_battle, before any CASCADING_ENABLED sub-phase split -- see
    # resolve_engagements_cascading) so a convergence group spanning multiple cascade sub-phases is
    # still corrected as one group. A direct caller that never precomputes it (tests, or the
    # non-cascading path where `pairs` already IS the full tick) gets it computed here instead --
    # identical math either way, since resolve_engagements_cascading passes the SAME `pairs` this
    # function would otherwise recompute from.
    if conv_scale is None:
        a_conv_scale, b_conv_scale = _convergence_scale(unit_a, unit_b, pairs)
    else:
        a_conv_scale, b_conv_scale = conv_scale
    # A (atomized fixing-force, subunit-scale): a subunit engaged on its FRONT by an enemy body cannot
    # wheel as a body to face a SEPARATE detachment on its flank/rear -- so that detachment's hit lands
    # with the zone penalty (the envelopment of a fixed unit). "Fixed" is emergent from frontal contact
    # and requires a DIFFERENT enemy subunit than the flanker -> impossible in any single-subunit clash
    # (byte-exact for the counters). Centroid-based, per contacting pair.
    def _su_centroid(_su):
        _cs = _su.cells()
        return (sum(r for r, c in _cs) / len(_cs), sum(c for r, c in _cs) / len(_cs)) if _cs else None
    _front_fixers = {}
    for _p in pairs:
        for _d, _e in ((_p["atom_a"], _p["atom_b"]), (_p["atom_b"], _p["atom_a"])):
            _dc = _su_centroid(_d); _ec = _su_centroid(_e)
            if _dc is None or _ec is None:
                continue
            _fz0, _ = octagon_angle(_ec, _dc, (_d.advance_dir, 0))
            if _fz0 == "GREEN":
                _front_fixers.setdefault(id(_d), set()).add(id(_e))
    for p in pairs:
        atom_a, atom_b = p["atom_a"], p["atom_b"]
        a_troops_frac = atom_a.troop_count / unit_a.total_troops()
        b_troops_frac = atom_b.troop_count / unit_b.total_troops()
        a_base = subunit_combat_pool(unit_a, atom_a)   # per-subunit pool (shared command; per-subunit discipline+cohesion)
        b_base = subunit_combat_pool(unit_b, atom_b)

        # F-i: support-stack-adjusted engage_frac -- only computed for the variants that actually
        # use it (baseline/C-i). [ED-MB-0002 perf fix] C-ii's bottom-up pair_pool_contribution()
        # does its own abs->orig cell-coordinate conversion (cells_to_orig_coords) internally;
        # unconditionally also calling support_engage_frac here duplicated that same conversion for
        # a value C-ii never reads, roughly doubling per-pair cost for no reason (measured: a
        # multi-subunit field-path battery went from ~seconds to ~3 minutes before this fix).
        if POOL_VARIANT != "C-ii":
            a_engage_frac = support_engage_frac(atom_a, p["a_cells"])
            b_engage_frac = support_engage_frac(atom_b, p["b_cells"])

        if POOL_VARIANT == "baseline":
            a_pool_raw = a_base * a_troops_frac * a_engage_frac
            b_pool_raw = b_base * b_troops_frac * b_engage_frac
        elif POOL_VARIANT == "C-i":
            a_pool_raw = a_base * a_engage_frac
            b_pool_raw = b_base * b_engage_frac
        elif POOL_VARIANT == "C-ii":
            # [DG-3, ED-MB-0002, 2026-07-04 Jordan ruling: "Combat pool for a subunit is
            # misleading. It should be based upon combat pool per cell as per troop type/quality/
            # density, and the overall combat pool for a subunit is actually just a combat score
            # for the subunit. This is bottom-up, and it solves issues with multiple engagements."]
            # `a_base`/`b_base` (subunit_combat_pool) stay exactly what Jordan calls them: the
            # subunit's aggregate COMBAT SCORE -- unchanged formula, not touched here.
            # `pair_pool_contribution` (core/exchange.py) is the bottom-up piece: it redistributes
            # that score across THIS specific pair by actual troop density in the cells engaged with
            # THIS enemy (`p["a_cells"]`/`p["b_cells"]`, already pair-scoped by find_contacts), plus
            # depth-weighted support from ranks behind — replacing a flat "divide by how many
            # simultaneous pairs" approximation (an earlier version of this fix used exactly that,
            # via eng_counts/count_engagements_per_atom; corrected same-session per Jordan's
            # feedback that it was still top-down, not bottom-up) with an exact per-pair troop-
            # weighted split.
            #
            # [2026-07-05 fix, mass-battle Cannae gauge follow-up audit, Jordan-ratified: "Intensive
            # (per-troop, partition-invariant)"] `a_troops_frac`/`b_troops_frac` was PREVIOUSLY kept
            # as an outer multiplier here on the theory that it was a separate, pre-existing concern
            # (dampening a multi-subunit army's shared-Command-driven score). A Fable-5 adversarial
            # audit found this reasoning didn't hold: `pair_pool_contribution` already normalizes
            # per-troop internally (`base_pool / atom.cur_troops`), so multiplying `a_base` by
            # `a_troops_frac` (== atom.troop_count / unit.total_troops()) BEFORE that division makes
            # the pair's effectiveness scale with the subunit's share of the WHOLE ARMY's troops, not
            # its own troop type/quality/density -- identical troops fought at 1/3 effectiveness
            # merely because their army had 3 subunits instead of 1, an army-bookkeeping denominator
            # Jordan's own DG-3 wording never asked for. Confirmed by direct trace: this was the
            # dominant reason the H3/H5/H6 gauge rows locked into 100% draws even after DG-3/DG-4
            # landed. Fixed by dropping the outer multiplier here -- a subunit's combat score is now
            # partition-invariant (splitting one army into N subunits does not change its total
            # output), matching the ratified "intensive" reading.
            a_pool_raw = pair_pool_contribution(atom_a, p["a_cells"], a_base)
            b_pool_raw = pair_pool_contribution(atom_b, p["b_cells"], b_base)
            # [partition-invariance fix, 2026-07-08] The per-pair split above is exact for ONE atom
            # split across several enemies; it does nothing when several of THIS side's atoms
            # instead converge on the SAME single opposing atom (a_conv_scale/b_conv_scale key on
            # (id(atom_a), id(atom_b)), 1.0 -- i.e. absent -- for every non-converging pair, so this
            # is a no-op for the overwhelming majority of pairs, byte-exact).
            if PC_CONVERGENCE_NORM:
                a_pool_raw *= a_conv_scale.get((id(atom_a), id(atom_b)), 1.0)
                b_pool_raw *= b_conv_scale.get((id(atom_a), id(atom_b)), 1.0)
        else:
            raise ValueError(f"Unknown POOL_VARIANT: {POOL_VARIANT}")

        # [ED-MB-0002 §2 step 2] Guard against float accumulation error dropping a whole die when
        # a pool value should land exactly on an integer boundary (e.g. a_pool_raw == 3.0 stored as
        # 2.9999999999999996). Confirmed to touch all 4 bat.py digest modes, not just field-path --
        # this variable is shared combat-resolution code, unlike every prior mass-battle fix in this
        # lane, which lived entirely inside the FIELD_MOVEMENT-gated node path.
        #
        # [D3 fix, 2026-07-05, mass-battle Cannae gauge follow-up audit] The `max(1, ...)` floor
        # below existed to guarantee a live atom always rolls AT LEAST one die -- but it applied
        # unconditionally, so a ROUTED/BROKEN atom (whose true a_pool_raw/b_pool_raw is exactly 0.0,
        # from subunit_combat_pool's own `if unit.routed or ... atom.broken: return 0` gate) got
        # resurrected to pool 1 and kept dealing real damage for many ticks after routing --
        # contradicts §A.12 ("routing: cannot fight back") and confirmed by direct trace (a routed
        # subunit dealt ~5-18 casualties/turn for 9 turns while flagged routed=True). `a_pool`/`b_pool`
        # is forced to exactly 0 here for bookkeeping (trace_event, the ranged//3 and encirclement
        # adjustments below) -- but see the SECOND part of this fix at `a_net`/`b_net` below:
        # `roll_pool`/`_sigma_net_boost` BOTH independently re-floor their own `pool` argument to a
        # minimum of 1 internally (`resolution.py`'s `range(max(1,n))` / `math.sqrt(max(1,pool))`), so
        # zeroing `a_pool` here ALONE has zero effect on the actual dice/damage outcome -- confirmed by
        # an adversarial reviewer's revert-and-diff test (byte-identical digest with vs without this
        # zeroing). The real fix forces `a_net`/`b_net` to 0 directly, downstream of those calls.
        a_dead = unit_a.routed or unit_a.broken or atom_a.routed or atom_a.broken
        b_dead = unit_b.routed or unit_b.broken or atom_b.routed or atom_b.broken
        a_pool = 0 if a_dead else max(1, math.floor(a_pool_raw + 1e-9))  # [canonical: epsilon: float magnitude guard]
        b_pool = 0 if b_dead else max(1, math.floor(b_pool_raw + 1e-9))  # [canonical: epsilon: float magnitude guard]

        # v11: Per-cell octagon angle — replace centroid-to-centroid with per-cell raw vectors
        # [canonical: Jordan design — octagon, GREEN<45°, YELLOW 45-90°, RED≥90°]
        # For each contact cell-pair, compute angle using defender's per-cell facing vector.
        # Average the modifier across all contact cell-pairs per side.
        def _per_cell_angle_mod(defender_subunit, defender_cells, attacker_cells, attacker_subunit=None, fixed_by_other=False):
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
                        # (c) FOV blind arc GATES reaction: a threat in the rear blind arc cannot be perceived,
                        # so it cannot pin. Reuses FOV_HALF_DEG; no-op unless the facing model is enabled.
                        if PC_FACING_MODEL and PC_FACING_FOV_GATE and _a > FOV_HALF_DEG:
                            continue
                        if (((a[0]-d_pos[0])**2 + (a[1]-d_pos[1])**2) ** 0.5 <= PC_PIN_REACH
                                and _a < 45.0):  # [canonical: mass_battle_v30.md §A.3b — 45deg octagon GREEN/YELLOW boundary]
                            pinned = True; break
                    worst_mod = 0; worst_ang = 0.0; worst_pos = None
                    for a in _wrappers:
                        zone, ang = octagon_angle(a, d_pos, facing)
                        if zone == "RED" and PC_ENVELOP_MOD < worst_mod:
                            worst_mod = PC_ENVELOP_MOD; worst_ang = ang; worst_pos = a
                    if worst_mod < 0 and (not pinned) and worst_ang <= FOV_HALF_DEG:
                        worst_mod = 0   # refused: free to turn AND can see the threat
                    # A (atomized detached-flank / envelopment of a fixed unit): if no wider-line wrap
                    # fired, a cell whose SUBUNIT is fixed frontally by a separate body (fixed_by_other)
                    # with the attacker bearing on its flank/rear arc takes the zone penalty -- independent
                    # of attacker frontage-width. The detachment strikes the flank/rear of a fixed unit.
                    # [canonical: Cannae 216 BC; du Picq -- the unseen attack on a pinned line.]
                    if worst_mod == 0 and fixed_by_other and PC_FIXING_FLANK:
                        _fz, _fa = octagon_angle(atk_centroid, d_pos, facing)
                        if _fz in ("YELLOW", "RED") and ANGLE_DEF_MOD[_fz] < 0:
                            worst_mod = ANGLE_DEF_MOD[_fz]; worst_ang = _fa
                            worst_pos = min(attacker_cells,
                                            key=lambda a: (a[0]-d_pos[0])**2 + (a[1]-d_pos[1])**2)
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

        # [ED-MB-0018, Jordan 2026-07-22] The OCTAGON = a DAMAGE-RECEIVED MULTIPLIER, not a dice penalty.
        # This computes the pure per-cell FACING ARC that feeds that multiplier -- SEPARATE from
        # `_per_cell_angle_mod` above (which bundles the wrapper/pocket/roll-up tactical POOL penalties of
        # the legacy paradigm Jordan is replacing). Three Jordan requirements are modelled here:
        #   (1) arc = damage multiplier: front GREEN 0, flank YELLOW -1, rear RED -2 -> mult 1.0/1.5/2.0.
        #   (2) reaction is NOT instantaneous: a cell hit outside its front arc keeps its EXPOSED facing
        #       (penalty stands) until it has had FACING_REACTION_TICKS to wheel -- and only if it can SEE
        #       the threat (within FOV) and is not pinned frontally. A REAR strike (in the blind arc) is
        #       never seen -> the cell never turns -> the 2x lands for the whole engagement (the surprise
        #       rear attack). The per-cell reaction clock persists on the subunit across ticks.
        #   (3) multi-side compounding is applied by the CALLER (eng_counts>=2 -> *(1+MULTI_SIDE_SHOCK)):
        #       orderly rank-relief collapses when hit from >=2 sides -- worse than a mere halving.
        # Uses the LOCAL attacker centroid (attacker cells within OCTAGON_LOCAL_REACH of each defender
        # cell; global fallback) so a wing cell of a WIDE line in a head-on clash stays GREEN instead of
        # reading the whole enemy line's centre as an oblique (flank) bearing -- verified front->1.00x,
        # rear->2.00x exactly. [canonical: Jordan design -- octagon damage multiplier; du Picq flank/rear
        # lethality + reaction time under surprise]
        def _octagon_dmg_mod(defender_subunit, defender_cells, attacker_cells):
            if not defender_cells or not attacker_cells:
                return 0.0
            atk = list(set(attacker_cells))
            op = _oriented(defender_subunit)
            abs_to_orig = {}
            for orig_r, orig_c, or_r, or_c in op:
                abs_r = (defender_subunit.starting_position[0] + or_r
                         + defender_subunit.cell_offsets.get((orig_r, orig_c), 0)
                         * defender_subunit.advance_dir)
                abs_c = (defender_subunit.starting_position[1] + or_c
                         + defender_subunit.cell_offsets_c.get((orig_r, orig_c), 0))
                abs_to_orig[(abs_r, abs_c)] = (orig_r, orig_c)
            _rs = getattr(defender_subunit, '_react_since', None)
            if _rs is None:
                _rs = {}; defender_subunit._react_since = _rs
            mods = []
            seen = set()
            for d_pos in defender_cells:
                if d_pos in seen:
                    continue
                seen.add(d_pos)
                orig = abs_to_orig.get(d_pos)
                facing = (defender_subunit.get_cell_facing(*orig)
                          if orig else (defender_subunit.advance_dir, 0))
                near = [a for a in atk
                        if (a[0]-d_pos[0])**2 + (a[1]-d_pos[1])**2 <= OCTAGON_LOCAL_REACH ** 2]
                if not near:
                    near = atk
                lc = (sum(r for r, c in near) / len(near), sum(c for r, c in near) / len(near))
                zone, ang = octagon_angle(lc, d_pos, facing)
                m = ANGLE_DEF_MOD[zone]
                _rk = orig if orig else d_pos
                _clear = True   # clear this cell's reaction clock unless it is actively counting toward a wheel
                if m < 0:
                    # frontally pinned? an attacker in the front arc within reach holds the cell so it
                    # cannot wheel to face the flank/rear threat (the fixing-force half of envelopment).
                    pinned = False
                    for a in atk:
                        _z2, _a2 = octagon_angle(a, d_pos, facing)
                        # [canonical: mass_battle_v30.md §A.3b — 45deg octagon GREEN/YELLOW boundary]
                        if (_a2 < 45.0
                                and (a[0]-d_pos[0])**2 + (a[1]-d_pos[1])**2 <= PC_PIN_REACH ** 2):
                            pinned = True; break
                    can_react = (ang <= FOV_HALF_DEG) and (not pinned)   # must SEE it AND be free to turn
                    if can_react:
                        if FACING_REACTION_TICKS <= 0:
                            m = 0                       # reaction delay disabled -> instant face
                        elif t is None:
                            pass                        # [ED-MB-0018 fix, arc-critic A4] no tick context -> cannot
                            #                             time the wheel -> penalty STANDS (was: instant-face footgun
                            #                             that silently zeroed every flank/side penalty on a t=None call)
                        else:
                            # [ED-MB-0018 fix, reaction-critic R1/R2] Frame-INDEPENDENT consecutive-tick counter,
                            # idempotent within a tick. Stored as (last_tick, count): survives run_battle's per-turn
                            # `t` restart (a continuous multi-turn flank keeps accumulating -- no absolute-tick
                            # arithmetic, which previously left a cell "stuck" penalized when t reset below its
                            # stamp), and a cell struck in >=2 pairs in ONE tick advances the counter ONCE (same
                            # `t` -> no double-count, which previously made a 2-sided cell's wheel order-dependent).
                            # The clock is RESET at engagement boundaries (reset_positions / reset_morale_between_
                            # battles) so it never leaks a stale stamp into a later, asymmetric re-engagement.
                            _prev = _rs.get(_rk)
                            if _prev is None or _prev[0] != t:
                                _cnt = (0 if _prev is None else _prev[1]) + 1
                                _rs[_rk] = (t, _cnt)
                            else:
                                _cnt = _prev[1]
                            _clear = False              # actively counting toward the wheel -> keep the clock
                            if _cnt >= FACING_REACTION_TICKS:
                                m = 0                   # reaction window elapsed -> wheeled to face -> penalty drops
                    # else (rear/blind or pinned): never wheels -> full penalty persists; clock cleared below
                if _clear:
                    _rs.pop(_rk, None)   # faced/green, rear/blind/pinned, or no-tick -> not counting -> reset clock
                mods.append(m)
            return sum(mods) / len(mods) if mods else 0.0

        a_fixed_other = bool(_front_fixers.get(id(atom_a), set()) - {id(atom_b)})
        b_fixed_other = bool(_front_fixers.get(id(atom_b), set()) - {id(atom_a)})
        a_angle_mod = _per_cell_angle_mod(atom_a, list(set(p["a_cells"])),
                                           list(set(p["b_cells"])), atom_b, a_fixed_other)
        b_angle_mod = _per_cell_angle_mod(atom_b, list(set(p["b_cells"])),
                                           list(set(p["a_cells"])), atom_a, b_fixed_other)
        # === SIGMA-LEVERAGE HEAD (prototype) ===
        # Advantages (octagon angle, puncture, encirclement, ranged-in-melee) enter as a
        # delta-sigma net-boost on the offensive net successes (uniform impact across pool
        # size), NOT as pool modifiers (non-uniform impact). Bare pool above = pure capacity.
        # Spine (degree -> DAMAGE_BY_DEGREE -> casualties) unchanged.
        # [canonical resolution: mass_combat.md §A.4 net-success exchange; sigma math:
        #  params/core.md continuous engine + modifier_system_spec.md §2.1/§3.1]
        ns_a = ns_b = 0.0   # legacy-path default so the mechanical trace can read these uniformly
        if SIGMA_HEAD_ENABLED:
            # [ED-MB-0018] Under PC_OCTAGON_DMG the octagon is a DAMAGE-RECEIVED MULTIPLIER (applied to
            # dmg_a/dmg_b below), NOT a net-successes penalty -- so it is REMOVED from the sigma head here
            # to avoid double-counting. The zone is still read for charge-shock / brace gating below.
            ns_a = 0.0 if PC_OCTAGON_DMG else a_angle_mod * SIGMA_PER_D     # a_angle_mod<=0 when A flanked
            ns_b = 0.0 if PC_OCTAGON_DMG else b_angle_mod * SIGMA_PER_D
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
                        _zb = "GREEN" if b_angle_mod > -0.5 else ("YELLOW" if b_angle_mod > -1.5 else "RED")  # [canonical: config.py:65 ANGLE_DEF_MOD GREEN 0/YELLOW -1/RED -2; -0.5, -1.5 are the zone-value midpoints re-binning the per-cell-averaged angle_mod to a zone: -0.5=mid(0,-1), -1.5=mid(-1,-2)]
                        ns_b += _charge_shock_sigma(unit_b, p["b_cells"], _zb, atom_b, t)
                    elif PC_ENVELOP_SHOCK and b_fixed_other and b_angle_mod <= -0.5:
                        # B (envelopment shock): a subunit FIXED frontally by a separate body and struck on
                        # its flank/rear cannot face the new threat -- the du Picq moral shock of envelopment
                        # fires even WITHOUT a momentum charge (the charge path's gap). Reuses the calibrated
                        # _charge_shock_sigma (zone/brace/depth/shaken gated: a braced+deep+disciplined line
                        # resists, a loose/shaken/shallow one shatters -- Cannae). elif -> mutually exclusive
                        # with the charge path (no double-count); b_fixed_other -> provably inert single-subunit.
                        # [canonical: Cannae 216 BC; du Picq Battle Studies -- the unfaceable attack on a pinned line.]
                        _zb = "YELLOW" if b_angle_mod > -1.5 else "RED"
                        ns_b += _charge_shock_sigma(unit_b, p["b_cells"], _zb, atom_b, t)
                    if b_pen > 0:
                        _za = "GREEN" if a_angle_mod > -0.5 else ("YELLOW" if a_angle_mod > -1.5 else "RED")  # [canonical: config.py:65 ANGLE_DEF_MOD zone midpoints — see the _zb line above]
                        ns_a += _charge_shock_sigma(unit_a, p["a_cells"], _za, atom_a, t)
                    elif PC_ENVELOP_SHOCK and a_fixed_other and a_angle_mod <= -0.5:
                        _za = "YELLOW" if a_angle_mod > -1.5 else "RED"  # [canonical: config.py:65 ANGLE_DEF_MOD zone midpoints — -1.5=mid(YELLOW -1, RED -2)]
                        ns_a += _charge_shock_sigma(unit_a, p["a_cells"], _za, atom_a, t)
                    # Reciprocal charge-recoil (the missing historical term): a charge driven home into a
                    # BRACED + deep + disciplined wall shatters the charger (Courtrai/Swiss/Waterloo squares).
                    # Charger = higher-momentum side; recoil scales with the wall's prep (discipline x depth).
                    # Gated by the 'brace' INSTRUCTION -> instruction-less scenarios stay byte-exact. Emergent:
                    # pikes break a cavalry charge, a loose/shallow line is still ridden down.
                    # [ED-1091, Jordan-approved 2026-07-02] PC_RECOIL_FRONTAL zone-gates the recoil to the
                    # wall's frontal (GREEN) octagon zone -- a brace cannot repel what it cannot face
                    # (Burkholder 2007), so a flank/rear charge into a braced wall is no longer wrongly
                    # recoiled (the latent flag mass_battle_gauge_grounding.md §4.3 carried since 2026-06-16;
                    # gauge row C7 deliberately avoided 'brace' because of it). Zone read: the defender's
                    # per-cell-averaged angle_mod, same GREEN midpoint re-binning as the charge-shock above.
                    # [canonical: config.py:65 ANGLE_DEF_MOD GREEN 0/YELLOW -1/RED -2; -0.5=mid(0,-1)]
                    # [ED-1095, Jordan-ruled 2026-07-02] PC_RECOIL_CHARGER_GATE additionally requires the
                    # CHARGING atom to actually be cavalry (mounted_archers -- who should never be closing
                    # at all, see T4 -- explicitly excluded) AND the defender's reach >= the charger's reach
                    # (a longer-reaching charger, e.g. a lance, can strike a wall whose weapons can't reach
                    # back, so the wall cannot retaliate/recoil it). reach_for is structural only today
                    # (TROOP_TYPE_REACH is deliberately empty -> everyone is REACH_SHORT -> this half of the
                    # gate is a no-op until reach assignments are separately ratified).
                    if PC_BRACE_ENABLED:
                        if (a_mom > b_mom and _subunit_braced(atom_b, t) and (not PC_RECOIL_FRONTAL or b_angle_mod > -0.5)
                                and (not PC_RECOIL_CHARGER_GATE or (atom_a.troop_type == 'cavalry'
                                                                     and reach_for(atom_b.troop_type) >= reach_for(atom_a.troop_type)))):
                            ns_a -= PC_CHARGE_RECOIL * _wall_prep(unit_b, p["b_cells"], atom_b) * SIGMA_PER_D
                        elif (b_mom > a_mom and _subunit_braced(atom_a, t) and (not PC_RECOIL_FRONTAL or a_angle_mod > -0.5)
                                and (not PC_RECOIL_CHARGER_GATE or (atom_b.troop_type == 'cavalry'
                                                                     and reach_for(atom_a.troop_type) >= reach_for(atom_b.troop_type)))):
                            ns_b -= PC_CHARGE_RECOIL * _wall_prep(unit_a, p["a_cells"], atom_a) * SIGMA_PER_D
            # [ED-MB-0018 fix, arch-critic #2] The legacy ENCIRCLEMENT_PENALTY fires on the SAME >=2 trigger
            # as the new multi-side damage shock -> under the octagon flag it would DOUBLE-COUNT encirclement
            # (once as an offence/sigma penalty here, once as a defence damage multiplier below). Gate it off
            # so the octagon multi-side shock is the single owner of the multi-engagement effect.
            if not PC_OCTAGON_DMG:
                if eng_counts.get(id(atom_a), 0) >= 2: ns_a -= ENCIRCLEMENT_PENALTY * SIGMA_PER_D
                if eng_counts.get(id(atom_b), 0) >= 2: ns_b -= ENCIRCLEMENT_PENALTY * SIGMA_PER_D
            if atom_a.unit_type == 'ranged': ns_a += RANGED_MELEE_SIGMA
            if atom_b.unit_type == 'ranged': ns_b += RANGED_MELEE_SIGMA
            ns_a += _morale_sigma(unit_a, atom_a)    # graded morale effectiveness (du Picq): per-subunit morale
            ns_b += _morale_sigma(unit_b, atom_b)
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
            # [ED-MB-0018] octagon = damage multiplier under PC_OCTAGON_DMG -> not a pool penalty here
            a_pool = max(1, a_pool + (0 if PC_OCTAGON_DMG else round(a_angle_mod)))
            b_pool = max(1, b_pool + (0 if PC_OCTAGON_DMG else round(b_angle_mod)))
            if PUNCTURE_ENABLED:
                a_mom = _momentum_speed(atom_a, p["a_cells"])
                b_mom = _momentum_speed(atom_b, p["b_cells"])
                if a_mom > b_mom:   a_pool += min(PUNCTURE_CAP, int(a_mom - b_mom))
                elif b_mom > a_mom: b_pool += min(PUNCTURE_CAP, int(b_mom - a_mom))
            if not PC_OCTAGON_DMG:   # [ED-MB-0018 fix, arch-critic #2] see the sigma-head gate above — no double-count
                if eng_counts.get(id(atom_a), 0) >= 2: a_pool = max(1, a_pool - ENCIRCLEMENT_PENALTY)
                if eng_counts.get(id(atom_b), 0) >= 2: b_pool = max(1, b_pool - ENCIRCLEMENT_PENALTY)
            if atom_a.unit_type == 'ranged': a_pool = max(1, a_pool // 3)
            if atom_b.unit_type == 'ranged': b_pool = max(1, b_pool // 3)
            a_net = roll_pool(a_pool)
            b_net = roll_pool(b_pool)
        # [D3 fix, part 2 -- 2026-07-05 adversarial-review correction] `roll_pool`/`_sigma_net_boost`
        # BOTH independently floor their own pool argument to a minimum of 1 internally, so zeroing
        # `a_pool`/`b_pool` above (for a routed/broken atom) has NO effect on `a_net`/`b_net` -- the
        # dice/sigma-boost math never sees the zero. Force the net directly here instead: a dead atom
        # always resolves to `compute_degree`'s `net<=0` -> "Failure" -> `DAMAGE_BY_DEGREE["Failure"]`
        # = 0 damage, closing the gap the first pass of this fix only appeared to close (confirmed by
        # the reviewer's revert-and-diff test: without this, the digest is byte-identical to no fix
        # at all).
        if a_dead: a_net = 0
        if b_dead: b_net = 0
        a_deg = compute_degree(a_net, max(1, b_net))
        b_deg = compute_degree(b_net, max(1, a_net))
        # [ED-MB-0018] Octagon = DAMAGE-RECEIVED MULTIPLIER (Jordan): the arc the attacker strikes from
        # multiplies the DEFENDER's casualties -- front 1.0x, flank 1.5x, rear 2.0x -- interpolated from the
        # dedicated per-cell FACING-ARC (`_octagon_dmg_mod`, 0..-2 -> mult = 1 - arc*(RED-1)/2, capped at
        # RED). This is the pure octagon arc (local-centroid, reaction-gated), NOT the legacy
        # `a_angle_mod`/`b_angle_mod` bundle (which also carries wrapper/pocket/roll-up pool penalties and
        # spuriously reads a wide line's wings as flanked head-on). Under PC_OCTAGON_DMG the legacy pool
        # angle-penalty is zeroed above, so this multiplier + MULTI-SIDE SHOCK are the single envelopment
        # model. MULTI-SIDE SHOCK: a subunit engaged from >=2 sides has its rank-relief divided AND
        # shock-compromised -> an extra COMPOUNDING factor (1+MULTI_SIDE_SHOCK), not a mere halving.
        # `a_arc`/`b_arc` are each side's own exposure, scaling that side's incoming damage (dmg_a = A's).
        _red = OCTAGON_DMG_MULT["RED"]
        if PC_OCTAGON_DMG:
            a_arc = _octagon_dmg_mod(atom_a, list(set(p["a_cells"])), list(set(p["b_cells"])))
            b_arc = _octagon_dmg_mod(atom_b, list(set(p["b_cells"])), list(set(p["a_cells"])))
            _a_dmg_mult = min(_red, 1.0 - a_arc * (_red - 1.0) / 2.0)
            _b_dmg_mult = min(_red, 1.0 - b_arc * (_red - 1.0) / 2.0)
            # MULTI-SIDE SHOCK, GRADED by the number of DISTINCT sides struck (`_atom_sides` above): the
            # rotate-in/out relief system is progressively more compromised the more directions a body is
            # engaged from -- 2 sides -> x1.5, 3 -> x2.0, 4 -> x2.5 (was a flat x1.5 on a 2-pair count that
            # both over- and under-fired). Compounds on the arc AFTER the cap, so a rear pair on a 2-sided
            # body reaches ~3.0x -- the annihilation-by-encirclement regime (du Picq / Cannae).
            _na = len(_atom_sides.get(id(atom_a), ()))
            _nb = len(_atom_sides.get(id(atom_b), ()))
            if _na >= 2: _a_dmg_mult *= (1.0 + MULTI_SIDE_SHOCK * (_na - 1))
            if _nb >= 2: _b_dmg_mult *= (1.0 + MULTI_SIDE_SHOCK * (_nb - 1))
        else:
            _a_dmg_mult = _b_dmg_mult = 1   # int 1 (not 1.0): `X * 1` preserves X's exact type -> the
            #                                 legacy PC_OCTAGON_DMG=0 path stays byte-exact (a float 1.0
            #                                 would coerce integer casualties to float and move the digest)
        if LANCHESTER_ENABLED:
            # P-L Linear Law: casualties to X scale with the ENEMY's engaged strength in
            # contact (frontage-capped); DAMAGE_BY_DEGREE retained as per-soldier exchange
            # quality. Numbers-in-contact lives ONLY here under Lanchester (the run_battle
            # opp_frac post-scaler is skipped) — one variable, one role (Lesson 1).
            # [v2 Stage D, ED-MB-0013] Pass the continuous engaged frontage width (OBB front-overlap)
            # when the FIELD_MOVEMENT contact path recorded it; p.get(...) is None on the grid/OFF path
            # (whose pairs carry no *_front key) -> _lanchester_strength falls back to the legacy integer
            # column count, keeping the byte-exact grid oracle untouched (I4).
            lin_b = _lanchester_strength(p["b_cells"], unit_b, p.get("b_front"))   # B's contacting strength -> casualties to A
            lin_a = _lanchester_strength(p["a_cells"], unit_a, p.get("a_front"))   # A's contacting strength -> casualties to B
            dmg_a += K_LINEAR * lin_b * max(0, DAMAGE_BY_DEGREE[b_deg](atom_b.eff_power) - atom_a.eff_dr) * _a_dmg_mult
            dmg_b += K_LINEAR * lin_a * max(0, DAMAGE_BY_DEGREE[a_deg](atom_a.eff_power) - atom_b.eff_dr) * _b_dmg_mult
        else:
            dmg_a += CASUALTY_SCALE * max(0, DAMAGE_BY_DEGREE[b_deg](atom_b.eff_power) - atom_a.eff_dr) * _a_dmg_mult
            dmg_b += CASUALTY_SCALE * max(0, DAMAGE_BY_DEGREE[a_deg](atom_a.eff_power) - atom_b.eff_dr) * _b_dmg_mult
        trace_event('melee', a_pool=a_pool, b_pool=b_pool,
                    ns_a=round(ns_a, 3), ns_b=round(ns_b, 3),
                    a_net=round(a_net, 2), b_net=round(b_net, 2),
                    a_deg=a_deg, b_deg=b_deg)
    return {"dmg_a": dmg_a, "dmg_b": dmg_b, "engagements": len(pairs)}

def resolve_engagements_cascading(unit_a, unit_b, pairs, t=None):
    """F-iii: cascading sub-phase resolution with facing rotation.
    [canonical: Jordan handoff §(3)]

    Contacts sorted by attacker depth (tip first). Each sub-phase resolves
    one depth group, then rotates engaged cells' facings toward their attacker.
    Later sub-phases see FLANK/REAR angles on already-rotated cells.
    Effect requires tight formation (TIP_SUPPORT_GAP=1 or 2) so multiple
    Arrowhead rows are simultaneously adjacent to Line cells.
    t: current battle tick, threaded to resolve_engagements for the brace-setup-delay gate. [ED-1095]"""
    # [partition-invariance fix] Compute the convergence scale ONCE on the FULL tick's pairs, before
    # any cascading sub-phase split below -- a convergence group (e.g. a pinning body's pair resolves
    # in an early sub-phase, a wing's pair in a later one) must be seen as a whole to be corrected
    # correctly; splitting it across sub-phase calls would under-count each sub-phase's group size.
    conv_scale = _convergence_scale(unit_a, unit_b, pairs)
    if not CASCADING_ENABLED:
        return resolve_engagements(unit_a, unit_b, pairs, t=t, conv_scale=conv_scale)

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
        result = resolve_engagements(unit_a, unit_b, active, dynamic_facings, t=t, conv_scale=conv_scale)
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
    """Nearest-cell distance between two atoms. Chebyshev (king-move) on the integer grid; EUCLIDEAN on the
    coordinate field (FIELD_MOVEMENT) so a diagonal approach is not counted 'free' — circular range rings
    (movement-substrate review 06, finding 1 / migration S2). Byte-exact OFF (the Chebyshev branch)."""
    cells_a = atom_a.cells()
    cells_b = atom_b.cells()
    if not cells_a or not cells_b:
        return float('inf')
    best = float('inf')
    for (ra, ca) in cells_a:
        for (rb, cb) in cells_b:
            d = math.hypot(ra - rb, ca - cb) if FIELD_MOVEMENT else max(abs(ra - rb), abs(ca - cb))
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
            return 0, None, False
        # [DG-2 §2.3/2.5, Jordan-ruled "build it now" 2026-07-08] "No volleying while yielding" --
        # a body actively repositioning doesn't also fire, matching the existing 'kite' precedent.
        # `yield_active` is already melee-only-gated, so this only ever fires for a ranged atom in
        # the (currently unreachable, by construction) case its unit_type somehow flips mid-battle;
        # kept for defence-in-depth, not because it's expected to trigger today.
        if shooter_atom.yield_active:
            return 0, None, False
        target_atoms = target_unit.subunits
        # E (atomized archer targeting): an archer ORDERED to a specific or weakest target fires at IT when
        # in range, else the nearest -- so archers can be directed at a flanker / priority unit. Gated by
        # PC_VOLLEY_TARGETING + an explicit order; default (no order) = nearest (the exact prior logic) ->
        # byte-exact. The ORDERED portion is concentrated on the target subunit downstream (apply_to_subunit);
        # unordered fire stays faction-spread. [canonical: longbow fire discipline, Crecy/Agincourt; §A.7.]
        _ordered = None
        if PC_VOLLEY_TARGETING:
            _oti = getattr(shooter_atom, 'order_target_idx', None)
            if _oti is not None and _oti < len(target_atoms):
                _ordered = target_atoms[_oti]
            elif getattr(shooter_atom, 'target_condition', None) == 'weakest':
                _cand = [t for t in target_atoms
                         if VOLLEY_MIN_RANGE <= _atom_distance(shooter_atom, t) <= VOLLEY_MAX_RANGE]
                if _cand:
                    _ordered = min(_cand, key=lambda t: sum(t.cell_troops.values()) if t.cell_troops else 0)
        best_target = None
        best_dist = float('inf')
        was_ordered = False
        if _ordered is not None and VOLLEY_MIN_RANGE <= _atom_distance(shooter_atom, _ordered) <= VOLLEY_MAX_RANGE:
            best_target = _ordered
            best_dist = _atom_distance(shooter_atom, _ordered)
            was_ordered = True
        else:
            for t in target_atoms:
                d = _atom_distance(shooter_atom, t)
                if VOLLEY_MIN_RANGE <= d <= VOLLEY_MAX_RANGE and d < best_dist:
                    best_dist = d
                    best_target = t
        if best_target is None:
            return 0, None, False
        # Pool = unit Power dice (PP-503). Discipline penalty applies (per §A.4).
        _vdisc = shooter_atom.eff_discipline   # per-subunit volley pool (Jordan directive): shooter subunit's power + discipline
        _vpen = 0 if _vdisc >= 5 else (1 if _vdisc >= 3 else (2 if _vdisc >= 1 else 99))  # [canonical: mass_battle_v30.md §A.4 — volley discipline penalty tiers]
        pool = max(1, shooter_atom.eff_power - _vpen)
        net = _roll_volley_pool(pool)
        # DR subtracts from net successes (Ranged DR Table)
        net_after_dr = max(0, net - RANGED_DR_DEFAULT)
        if LANCHESTER_ENABLED:
            # P-L Square Law: aimed fire lifts the frontage cap — every shooter engages the
            # target area, so volley effectiveness scales with SHOOTER COUNT (toward N²-type
            # concentration over the integral). Distinct from the frontage-capped melee linear
            # term. [spec mb_lanchester_design.md §3b; Lanchester Square Law = ranged/aimed fire.]
            net_after_dr = net_after_dr * K_SQUARE * shooter_atom.eff_size
        dens = _volley_density_mult(target_unit)
        out = net_after_dr * dens
        trace_event('volley', shooter=getattr(shooter_unit, 'name', '?'), d=best_dist,
                    pool=pool, net=net, net_dr=round(net_after_dr, 2),
                    dens=round(dens, 3), loss=round(out, 2))
        return out, best_target, was_ordered

    ordered_a = []
    ordered_b = []
    for atom in unit_a.subunits:
        dmg, tgt, was_ordered = fire(atom, unit_a, unit_b)
        if tgt is not None:
            loss_b += dmg
            shots += 1
            if was_ordered:
                ordered_b.append((tgt, dmg))
    for atom in unit_b.subunits:
        dmg, tgt, was_ordered = fire(atom, unit_b, unit_a)
        if tgt is not None:
            loss_a += dmg
            shots += 1
            if was_ordered:
                ordered_a.append((tgt, dmg))

    return {"loss_a": loss_a, "loss_b": loss_b, "shots": shots,
            "ordered_a": ordered_a, "ordered_b": ordered_b}


# ─── WORKBENCH TRACE SNAPSHOTS (read-only; gated by tracing_on(), zero cost when tracing is off) ──
# [tick-by-tick visualizer, Jordan directive 2026-07-01] Extends the existing observe-only trace seam
# (resolution.start_trace/trace_event/get_trace) with a spatial 'positions' event per tick. Uses
# atom.cells() (NOT iter_cells(), which reads legacy cell_offsets unconditionally and is NOT
# field-aware) zipped against _oriented(atom)'s stable (orig_r,orig_c) ids — both iterate in the
# SAME order (cells()/_node_cells() are themselves built by iterating _oriented(self)), so this is a
# correct pairing on BOTH the integer-grid and coordinate-field paths. Callers gate on tracing_on()
# so this construction (and its cost) is skipped entirely for every normal battle run.
def _cell_snapshot(atom):
    ids = [(o_r, o_c) for o_r, o_c, _, _ in _oriented(atom)]
    cells = []
    for cid, pos in zip(ids, atom.cells()):
        fr, fc = atom.get_cell_facing(*cid)
        cells.append({'id': list(cid), 'pos': [pos[0], pos[1]],
                       'troops': round(atom.cell_troops.get(cid, 0.0), 1),
                       'facing': [fr, fc], 'halted': cid in atom.halted_cells})
    return cells

def _subunit_snapshot(atom):
    return {'shape': atom.shape, 'troop_type': atom.troop_type, 'unit_type': atom.unit_type,
            'role': atom.role, 'instructions': list(atom.instructions),
            'routed': atom.routed, 'broken': atom.broken, 'stance': atom.stance,
            'cells': _cell_snapshot(atom)}

def _unit_snapshot(unit):
    return {'name': unit.name, 'faction': unit.faction,
            'hp': round(unit.hp, 1), 'hp_max': unit.hp_max,
            'morale': unit.morale, 'discipline': unit.discipline, 'stance': unit.stance,
            'routed': unit.routed, 'broken': unit.broken,
            'subunits': [_subunit_snapshot(a) for a in unit.subunits]}


# ─── BATTLE ──────────────────────────────────────────────────────────────────

def _draw_friction_cev(unit):
    """[ED-MB-0016, DG-6 resolution] Draw `unit`'s per-battle combat-effectiveness friction factor ONCE.
    Idempotent within a battle: a fresh unit has no `_friction_cev`; once set it is never redrawn (so a
    multi-turn battle's repeated run_battle entries keep the single per-battle draw). M ~ LogNormal(0,
    PC_FRICTION_SIGMA^2) via exp(gauss) on the seeded `random` stream. PC_FRICTION_CEV off -> 1.0
    (default-inert, byte-exact). See config.py PC_FRICTION_CEV for the full grounding."""
    if getattr(unit, '_friction_cev', None) is not None:
        return
    if PC_FRICTION_CEV and PC_FRICTION_SIGMA > 0.0:
        unit._friction_cev = math.exp(random.gauss(0.0, PC_FRICTION_SIGMA))
    else:
        unit._friction_cev = 1.0


def run_battle(unit_a, unit_b, max_turns=18):  # [canonical: mass_battle_v30.md §A.7 — 18-tick battle (3 phases x 6)]
    """Run one engagement turn (up to 3 phases = 18 ticks).
    v16: max_turns=18 = one battle turn's engagement cap (3 phases).
    Multi-turn battles call this repeatedly with persistent unit state.
    [canonical: Jordan direction — "limit of three phases per simultaneous
     engagement per turn"]

    Returns:
      {"winner": "A"|"B"|"draw", "turns": int, "phases": int, "tick_in_phase": int}
    """
    # [movement-substrate review 06 — coordinate-field migration] The continuous COORDINATE FIELD requires
    # the node float path: field-ON stores/emits true floats only via _node_pos (PC_NODE_COHESION). A
    # FIELD-ON / NODE-OFF run would silently half-migrate (legacy integer branch, no floats, but the
    # fractional-speed accumulator active) -> a degenerate integer 'field' run. Enforce the implication at
    # setup so the invalid combination fails loudly instead of producing a corrupt result. No-op when
    # FIELD_MOVEMENT is OFF (byte-exact).
    assert (not FIELD_MOVEMENT) or PC_NODE_COHESION, \
        "FIELD_MOVEMENT=1 requires PC_NODE_COHESION=1 (the coordinate field runs on the node float path)"
    # [ED-MB-0016, DG-6 resolution] Draw each side's per-BATTLE combat-effectiveness (CEV) friction factor
    # ONCE, lazily: the FIRST run_battle entry for a fresh unit draws it; subsequent turns of a multi-turn
    # battle (which re-enter run_battle with persistent unit state) see it already set and do NOT re-draw
    # -- so the shock is drawn once per battle, not per turn (per-turn re-draws would self-average away the
    # very variance this restores). A fresh unit per gauge trial gets a fresh draw. Default-inert: with
    # PC_FRICTION_CEV off, _draw_friction_cev sets 1.0 (no behaviour change; byte-exact). Uses the seeded
    # `random` stream so determinism (I2) holds; enabling it shifts the stream (field goldens re-record).
    _draw_friction_cev(unit_a)
    _draw_friction_cev(unit_b)
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
            # [migration H] recompute abs from _node_pos (file-binned) on ON so it matches find_contacts'
            # (file-binned) cells; OFF = verbatim cell_offsets build. Otherwise the == misses on the node
            # path and halted_cells stays empty -> pre-contact halt silently disabled on the field path.
            _atom_a = p["atom_a"]; _atom_b = p["atom_b"]
            _fld_a = FIELD_MOVEMENT and PC_NODE_COHESION and hasattr(_atom_a, '_node_pos')
            _fld_b = FIELD_MOVEMENT and PC_NODE_COHESION and hasattr(_atom_b, '_node_pos')
            op_a = _oriented(_atom_a)
            for cell in p["a_cells"]:
                for orig_r, orig_c, or_r, or_c in op_a:
                    if _fld_a:
                        _pr, _pc = _atom_a._node_pos.get((orig_r, orig_c), (0.0, 0.0))
                        abs_r = int(round(_pr)); abs_c = int(round(_pc / COL_WIDTH))
                    else:
                        abs_r = (_atom_a.starting_position[0] + or_r
                                 + _atom_a.cell_offsets.get((orig_r,orig_c), 0) * _atom_a.advance_dir)
                        abs_c = (_atom_a.starting_position[1] + or_c
                                 + _atom_a.cell_offsets_c.get((orig_r,orig_c), 0))
                    if (abs_r, abs_c) == cell:
                        _atom_a.halted_cells.add((orig_r, orig_c)); break
            op_b = _oriented(_atom_b)
            for cell in p["b_cells"]:
                for orig_r, orig_c, or_r, or_c in op_b:
                    if _fld_b:
                        _pr, _pc = _atom_b._node_pos.get((orig_r, orig_c), (0.0, 0.0))
                        abs_r = int(round(_pr)); abs_c = int(round(_pc / COL_WIDTH))
                    else:
                        abs_r = (_atom_b.starting_position[0] + or_r
                                 + _atom_b.cell_offsets.get((orig_r,orig_c), 0) * _atom_b.advance_dir)
                        abs_c = (_atom_b.starting_position[1] + or_c
                                 + _atom_b.cell_offsets_c.get((orig_r,orig_c), 0))
                    if (abs_r, abs_c) == cell:
                        _atom_b.halted_cells.add((orig_r, orig_c)); break
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
            if PC_NODE_COHESION and getattr(sub, '_node_facing', None) is not None:
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
        moving_a = [atom for atom in unit_a.subunits
                    if atom.target_atom or (atom.escort_of is not None and not atom._escort_engaged)]
        moving_b = [atom for atom in unit_b.subunits
                    if atom.target_atom or (atom.escort_of is not None and not atom._escort_engaged)]
        for atom in moving_a:
            # per-subunit formation-hold: each subunit advances on its OWN Discipline
            # (single-subunit inherits -> == unit.discipline -> byte-exact)
            atom.advance_cells(atom.eff_discipline, cached_centroids[id(atom)],
                               enemy_cells=b_cells_set, enemy_cells_float=b_cells_float)
        for atom in moving_b:
            atom.advance_cells(atom.eff_discipline, cached_centroids[id(atom)],
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
        # resolve_internal_collisions) is implemented but not invoked here —
        # it over-tuned battery (12/13 -> 9/13). Left available for future use
        # when paired with a proper bad-facing trigger.
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
            # E: ORDERED volley fire concentrates its portion on the target subunit (apply_to_subunit); the
            # unordered remainder spreads as before. Same totals -> sum==hp preserved; with no ordered fire
            # (the default) this is byte-exact-identical to the prior two distribute_casualties calls.
            _sa = volley_hp_scale(unit_a)
            _sb = volley_hp_scale(unit_b)
            _ord_a = vol.get("ordered_a", [])
            _ord_b = vol.get("ordered_b", [])
            _ord_a_tot = sum(_d for _su, _d in _ord_a)
            _ord_b_tot = sum(_d for _su, _d in _ord_b)
            distribute_casualties(unit_a, result["dmg_a"] + (volley_dmg_a - _ord_a_tot) * _sa, pairs)
            distribute_casualties(unit_b, result["dmg_b"] + (volley_dmg_b - _ord_b_tot) * _sb, pairs)
            for _su, _d in _ord_a:
                apply_to_subunit(unit_a, _su, _d * _sa)
            for _su, _d in _ord_b:
                apply_to_subunit(unit_b, _su, _d * _sb)
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

        # Rout check AFTER both erosions applied — per-subunit, then derive the unit rout
        for u in [unit_a, unit_b]:
            if u.routed:
                continue
            for atom in u.subunits:
                if not atom.routed and atom.eff_morale <= 0:
                    atom.routed = True
            u.derive_rout()   # single-subunit: fires iff old `u.morale<=0` did (byte-exact)
        # v15: phase boundary — stamina_check, morale_check_phase, rout_resolution
        # are now populated (G-1 + G-2). rally/reform/threadwork remain empty.
        if t % TICKS_PER_PHASE == 0:
            current_phase += 1
            phase_boundary(unit_a, unit_b, current_phase)
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
    for atom in unit.subunits:
        atom.recover_stamina(BETWEEN_TURN_STAMINA_RECOVERY)
    unit.morale = min(unit.morale_start, unit.morale + BETWEEN_TURN_MORALE_RECOVERY)
    for atom in unit.subunits:        # per-subunit Morale recovery (own-Morale subunits; inert at RECOVERY=0)
        if atom.morale is not None:
            atom.morale = min(atom.eff_morale_start, atom.morale + BETWEEN_TURN_MORALE_RECOVERY)


def reset_morale_between_battles(unit):
    """Campaign-boundary reset: Morale resets between battles; the unit reforms.
    [canonical: designs/provincial/mass_battle_v30.md §A.4; params/mass_combat.md §PP-711 (Morale resets between battles), §PP-712 (Discipline persists between battles)]
    Resets the unit's Morale and each own-Morale subunit's Morale to its nominal start, and clears the
    routed/broken flags -- rout is DERIVED from Morale reaching zero, so resetting Morale without clearing
    the flags would leave an incoherent routed-but-full-Morale unit (derive_rout only ever SETS the flag).
    Discipline is NOT reset (it persists per the citation above). Inherited-Morale subunits (own Morale is
    None) are covered by the unit-level reset via eff_morale. Called by the campaign layer at the battle
    boundary -- NOT within a single battle: between_turn_recovery handles the within-battle turn boundary,
    this handles the battle-to-battle boundary. A single-subunit unit reduces to the unit-level reset."""
    unit.morale = unit.morale_start
    unit.routed = False
    unit.broken = False
    for atom in unit.subunits:
        if atom.morale is not None:
            atom.morale = atom.eff_morale_start   # own Morale -> its nominal start
        atom.routed = False
        atom.broken = False
        # [ED-MB-0018, reaction-critic R1] A new battle is a fresh engagement -> clear the facing-reaction
        # clock (per-engagement transient state must not survive the battle boundary onto a persistent atom).
        _rs = getattr(atom, '_react_since', None)
        if _rs is not None:
            _rs.clear()


def reset_positions(unit, shape, anchor_map):
    """Reset subunit positions for re-engagement after disengagement -- LEGACY GRID PATH ONLY.
    Units return to their starting rows for fresh approach.

    [Fix, 2026-07-02] Each subunit now returns to its OWN spawn column (Subunit._spawn_position,
    snapshotted once at construction) rather than a single shape-keyed anchor shared by every
    subunit in the unit. The old behaviour was byte-exact-correct only by coincidence for a
    single-subunit unit built via build_unit (whose one subunit's spawn position IS exactly
    anchor_map[(shape,tier)] -- so this change reproduces identical results for every such case,
    confirmed via bat.py's byte-exact battery, which exercises exactly this path). It was silently
    WRONG for a multi-subunit army (build_army/build_envelopment/build_refused_flank): resetting
    EVERY subunit to one shared anchor column collapsed any wide-placed wing/escort back onto the
    center on every subsequent battle-turn, discovered while dogfooding build_envelopment/
    build_refused_flank through the multi-turn ('multi'/"resolving mode") path for the first time
    -- Stage C's own verification only ever exercised kind='single', which never calls this
    function, so the gap went unexercised until now. `shape`/`anchor_map` stay as parameters (no
    call-site signature change) and are used only as a defensive fallback for a subunit that
    somehow lacks a spawn snapshot (should not occur for anything built through __post_init__).

    [Fix, 2026-07-02, movement audit finding 1.1 / ED-1096] Node-path atoms are now explicitly
    SKIPPED, not silently corrupted. This function writes only starting_position/cell_offsets/
    cell_offsets_c -- the legacy grid fields -- which _node_cells()/cells() never reads once
    PC_NODE_COHESION is on (node position lives in _node_pos). The old code wrote these fields
    unconditionally anyway: a harmless no-op for the node path's OWN rendering, but a landmine for
    any OTHER code that reads Subunit.starting_position post-construction expecting it to track a
    node-path atom's live position (it never has) -- most immediately the forthcoming waypoint
    primitive (fix-plan step 7), which must not inherit a stale "reset to spawn" value. Per
    Jordan's ruling (2026-07-02, verbatim): "an army only has subunits reset to initial
    positions... at the start of a new battle. it is nonsensical for them to return to starting
    positions within the same battle" -- the correct node-path behaviour for a within-battle
    re-engagement turn is to do NOTHING to position at all, continuing exactly where the subunit
    currently is. (The separate question of whether/how a subunit can be mid-battle REDIRECTED to
    a new position or role once already committed -- e.g. disengaging from contact -- is gate 1's
    Command/Discipline-gated conditional-tactics system, explicitly deferred until
    envelopment/pincer/wheeling pathing is confirmed working.) Legacy-path atoms are completely
    unaffected -- this is an additive skip, not a behavior change to the branch that fires."""
    start_row = SIDE_A_START_ROW if unit.faction == 'A' else SIDE_B_START_ROW
    fallback_col = anchor_map.get((shape, unit.subunits[0].tier), 10) if unit.subunits else 10
    for atom in unit.subunits:
        if PC_NODE_COHESION and hasattr(atom, '_node_pos'):
            continue
        spawn = getattr(atom, '_spawn_position', None)
        anchor_col = spawn[1] if spawn is not None else fallback_col
        atom.starting_position = (start_row, anchor_col)
        atom.cell_offsets = {}
        atom.cell_offsets_c = {}
        # [ED-MB-0018, reaction-critic R1] A GRID re-approach is a FRESH engagement -> clear the per-cell
        # facing-reaction clock so a stamp from the prior turn cannot mis-score the opening ticks. (Field/
        # node atoms hit the `continue` above -> their continuous engagement correctly keeps the clock.)
        _rs = getattr(atom, '_react_since', None)
        if _rs is not None:
            _rs.clear()


def run_multi_turn_battle(unit_a, unit_b, shape_a, shape_b, anchor_map,
                          max_battle_turns=8):  # [canonical: mass_battle_v30.md §A.7 — battle-turn cap]
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
            'a_stamina': unit_a.agg_stamina(), 'b_stamina': unit_b.agg_stamina(),
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
                          anchor_map, max_battle_turns=8):  # [canonical: mass_battle_v30.md §A.7 — battle-turn cap]
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
                    _disc = target.agg_discipline()   # per-subunit-aware resistance (== unit.discipline if homogeneous)
                    if _disc > 0 and target.command > 0:
                        erosion = dmg / (_disc * target.command)
                        target.cascade_morale_hit(erosion)
                    for atom in target.subunits:
                        if not atom.routed and atom.eff_morale <= 0:
                            atom.routed = True
                    target.derive_rout()
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
                    friend.cascade_morale_hit(1)
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
                friend.cascade_morale_hit(ROUT_CONTAGION_MORALE_HIT)
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

__all__ = ['_formation_depth', '_subunit_depth', '_stamina_pool_penalty', 'stamina_check', 'morale_check_phase', 'rout_resolution', 'discipline_check_phase', 'rally_check', 'reform_check', 'threadwork_check', 'phase_boundary', 'Subunit', 'Unit', 'derive_command', 'command_base_pool', 'assign_targets', 'resolve_cross_side_contention', 'find_contacts', 'count_engagements_per_atom', '_momentum_speed', '_cascade_depth_key', 'PC_ROLLUP_PER_RANK', 'PC_ROLLUP_MARGIN', 'PC_ROLLUP_REACH', 'PC_ROLLUP_CAP', 'PC_ROLLUP_FLANK_REACH', 'PC_ROLLUP_MIN_DEPTH', '_lanchester_strength', 'resolve_engagements', 'resolve_engagements_cascading', '_atom_distance', '_roll_volley_pool', 'volley_phase', 'run_battle', 'BETWEEN_TURN_STAMINA_RECOVERY', 'BETWEEN_TURN_MORALE_RECOVERY', 'between_turn_recovery', 'reset_morale_between_battles', 'reset_positions', 'run_multi_turn_battle', 'REARGUARD_PENALTY', 'RECALL_OB', 'pursuit_damage', 'recall_check', 'MORALE_CASCADE_OB', 'ROUT_CONTAGION_MORALE_HIT', 'FREED_ATTACKER_FLANK_PENALTY', 'discipline_check_cascade', 'freed_attacker_damage', 'run_multi_unit_battle', 'roles_for', 'role_allowed', 'stats_for', 'TROOP_TYPE_STATS']
