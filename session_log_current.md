session_id: 2026-03-30T_PROPAGATION_WND_COH
phase: closed
status: CLOSED

## SESSION SUMMARY
PP-WND-01 and PP-COH-01 propagation into stage2_characters audit complete.

## PROPAGATION RESULTS

### PP-WND-01 (Wound penalty: +1 Ob → −1D)
- stage1_core_engine: already correct (§3.8 states −1D per Wound)
- stage2_characters: no wound penalty formula present — CP menu only; no change needed
- stage3_thread_operations: **PATCHED** — Leap round wound penalty corrected from +1 Ob to −1D
- stage8_combat: already correct (patched prior session)
- stage15_spell_catalog: already correct (−1D per Wound stated at line 384)
- valoria_ruleset_checkpoint_14: no stale instances found

### PP-COH-01 (Coherence: per-operation → retention roll per Leap)
- stage3_thread_operations: already correct (§5.2.2 retention roll system in place)
- stage2_characters: Coherence not tracked here (non-practitioner document); no change needed
- Degree table −1 Coherence (cap) entries: correctly mean +1 Ob to retention roll, not direct loss — no change needed

## COMMITS THIS SESSION
- stage3_thread_operations.md: 6bbfdf17fb

## NEXT ACTIONS
1. Update valoria_ruleset_checkpoint_14 with editorial batch PP-154–160 + propagation fix
2. Continue simulation or move to full compilation

## WORLD STATE (unchanged)
RS: 20 | TC: 20 | IP: 22
Vaynard TS: 30. TK: 3.
Klapp TS: ~50. CE: 8. Coherence: 9. Certainty: 3.
Ehrenwall: Dead. Coup Counter: Terminated — successor rule now defined (PP-156).
Olafsson: Partially reinstated (Church Stability 4).
Maret Uln: Active. TS 50. Coherence: 10.
Inquisitor Vald: CE 3. Investigation Stage 1 complete.
