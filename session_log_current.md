session_id: 2026-03-30T_CROSS_MECHANIC_SIM_BATCH
phase: closed
status: CLOSED

## SESSION SUMMARY
Cross-mechanic simulation batch. 12 new sim files produced (SIM-X-05 through X-16).
Two mechanical patches applied and propagated.

## PATCHES COMMITTED THIS SESSION
- PP-WND-01: Wound penalty changed from +1 Ob per Wound → −1D per Wound
  Files: stage1_core_engine, stage3_thread_operations, stage8_combat, stage15_spell_catalog, valoria_ruleset_checkpoint_14
- PP-COH-01: Coherence reduction changed from per-operation scale-based loss → retention roll at end of Leap (pool vs sum of Obs)
  Files: stage3_thread_operations, stage15_spell_catalog, valoria_ruleset_checkpoint_14
- Terminology fix: Strength → Size in mass battle sim files X-03, X-04, X-07

## SIMULATION FILES COMMITTED
tests/sim_x_05 through sim_x_16 (12 files)
tests/coverage_matrix.md (updated to v3)

## EDITORIAL DECISIONS PENDING (user must decide before patching)
- F-11: W-33 broken for CP≤2 units — fix options: Cohesion min(3,prior) or add Size component
- F-27: Mass battle stalemate resolution — no rule for zero-damage indefinite stalemates
- F-30: Coup Counter successor on Grandmaster Ehrenwall death
- F-43: No seasonal cap on TC clock movement — two Domain Actions dropped TC by 4 in one season
- F-45: Church Stability brake scope — suppresses all TC or only Mandate-based TC?
- F-52: Faction Stability recovery rate — no rule defined for externally damaged Stability
- F-70: Klapp Rendering Crisis — Belief revision content requires user input

## CRITICAL FINDINGS (no patch needed, campaign awareness)
- F-58: RS 22 is 2 points from Dormant threshold — any failed Weaving disables all Leaps globally
- F-62: Certainty (Spirit=3) depletes in 2 Leaps for Klapp — Rendering Crisis imminent
- F-51: Olafsson Evidence Chain is dominant TC suppression (6–7 TC over 3 seasons at low cost)
- F-53: Territorial Weave success (−1 Ob territory-wide) disproportionately powerful at low RS

## NEXT ACTIONS
1. User resolves 7 editorial decisions above
2. Apply resulting patches
3. Propagate PP-WND-01 + PP-COH-01 into stage2_characters if wound/coherence references exist
4. Update valoria_gap_register_consolidated.md with new gaps from sim batch
5. Continue simulation or move to compilation

## WORLD STATE AT SESSION CLOSE (canonical starting values + sim deltas)
RS: 20 (from canonical 28, multiple Thread ops)
TC: 20 (from canonical 22, Doctrine + Evidence chain net)
IP: 22 (passive drift)
Vaynard TS: 30. TK: 3.
Klapp TS: ~50. CE: 8. Coherence: 9. Certainty: 0 (Rendering Crisis pending resolution).
Ehrenwall: Dead. Coup Counter: Terminated.
Olafsson: Partially reinstated (Church Stability 4).
Maret Uln: Active. TS 50. Coherence: 10.
Inquisitor Vald: CE 3. Investigation Stage 1 complete.
