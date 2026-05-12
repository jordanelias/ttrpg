# SIM-MB-06 v8 Module Manifest
# Iteration: v7 → v8 (tension F: cell support + puncture)
# Date: 2026-05-12

## ADDED IN v8

### F-i: Cell support stack (Jordan-directed, handoff §(1))
`support_stack_frac()` replaces raw `a_engaged/a_width` engage_frac calculation.

For each contact pair:
- Map absolute contact cells → original pattern coords via `abs_cells_to_orig()`
- Find the minimum oriented_r among contact cells (front contact row)
- Sum weighted supporters behind: depth 1→×1.0, depth 2→×0.7, depth 3→×0.5, depth 4→×0.3
- total_effective = |contact_cells| + supporter_weighted_sum
- engage_frac = min(1.0, total_effective / atom_max_width)

Controlled by: `F_SUPPORT_ENABLED = True` (global flag)
Weights: `SUPPORT_WEIGHTS = {1: 1.0, 2: 0.7, 3: 0.5, 4: 0.3}`
[canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md §(1) Cell support]

### F-ii: Puncture / momentum (Jordan-directed, handoff §(2))
`puncture_bonus()` awards attacker pool dice based on speed differential at contact.

- `last_turn_speed: Dict[Tuple,int]` added to `Atom` dataclass
- `advance_cells()` records actual speed moved per cell into `last_turn_speed`
  (0 for halted cells, 0 for tip-support-gated cells)
- At engagement: average speed of attacker's contact cells vs 0 (defender halted)
- Bonus = min(PUNCTURE_CAP, floor(speed_diff × PUNCTURE_BONUS_PER_SPEED_UNIT))
- Applied additively to attacker pool (both sides compute independently)

Controlled by: `F_PUNCTURE_ENABLED = True`
Cap: `PUNCTURE_CAP = 3`
Rate: `PUNCTURE_BONUS_PER_SPEED_UNIT = 1`
[canonical: tests/sim/sim_mb_06_handoff_2026-05-12.md §(2) Puncture mechanism]

## RESULTS (n=200, seed 0-199)

| Matchup | v7 | v8 | Target | Status |
|---|---|---|---|---|
| Arrowhead T2 vs Line T2 | 4% | **59%** | 40-60% | ✓ |
| Arrowhead T3 vs Line T3 | 0% | **48.5%** | 40-60% | ✓ TENSION F RESOLVED |
| Arrowhead T4 vs Line T4 | 0% | 33.5% A / 3.5% B / **63% draw** | 40-60% | ⚠ draws = lethality |
| Line T3 mirror bias | 51.5/48.5 | 49.0/50.0 | ~50/50 | ✓ |
| Line T3 lethality | 9.7 turns | 9.5 turns | 3-6 | ✗ open |
| Cannae (Horseshoe vs Arrow T3) | 62% | **55%** | 40-60% | ✓ |
| Horseshoe vs Line T3 | 0% | 29.5% | 40-60% | ⚠ improved, open |
| Arrowhead vs Horseshoe T3 | — | 46.5% | — | OK |

## TENSIONS AFTER v8

### Resolved by v8
- **Tension F: wedge piercing.** Arrowhead vs Line climbs from 0% → 48.5% at T3.
  Root cause was engage_frac penalizing narrow attackers. Cell support stack
  correctly represents mass-behind-tip concentration of force.
  F-iii (cascading sub-phases) not needed to resolve the core problem.

### Remaining open (carry to v9 or later)

- **T4 lethality.** Line T4 mirror hits max_turns (15) in 63% of battles. T3 lethality
  = 9.5 turns vs 3-6 target. Both symptoms of under-damage at scale. F-i improved
  engage_frac (capped at 1.0), reducing the "too few dice" problem, but HP pools at
  higher tiers still exceed 15-turn budget. Next: investigate damage formula or increase
  TROOPS_PER_SIZE scaling, or raise max_turns for diagnostic purposes.

- **Horseshoe vs Line.** 29.5% (was 0%; target 40-60%). F-i helped (thin center now
  gets support from rows behind), but not enough. Horseshoe's center has 0-speed cells
  that don't contribute to puncture, and its support stack behind the center is thin.
  May need a dedicated Horseshoe-center mechanic or reassess wing-wrap timing.

- **GappedLine vs Line: 72.7%.** Higher than expected. Gap mechanic (+2 off at
  "flank_engaged") may be over-tuned relative to revised engage_frac. Noted; not
  blocking ratification.

- **F-iii (cascading sub-phases).** Jordan-directed design captured in handoff §(3).
  Not implemented — unnecessary for T3 tension F. Available as v9 enhancement if
  additional differentiation between wedge grades is wanted.

## STATUS

EXPLORATORY. ED-814 remains canonical mechanic.
Atom architecture promotion requires:
- Horseshoe vs Line resolved
- Lethality fixed (3-6 turns at T3)
- All matchups in 30-70% range (at minimum) / 40-60% (ideal)
- Then: write ED-826 (or next ID) superseding ED-814
