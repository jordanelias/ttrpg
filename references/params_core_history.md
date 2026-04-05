## PP-247 — Combat Pool formula correction
- **Date:** 2026-04-04
- **Source:** SIM-C-01 pre-simulation audit (AUD-F01)
- **Change:** params_core Combat Pool row corrected from `(Agility × 2) + History + 3` to `Agility + History (points + 3)` to match stage1 §2.3 and §3.4.
- **Impact:** At Agi=5, hist=2: old formula gave 15D; correct value is 10D. 50% overcounting. Affects all combat pool calculations in params_core.

## PP-248 — Stamina and Health row corrections
- **Date:** 2026-04-04
- **Source:** SIM-C-01 pre-simulation audit (AUD-F02, AUD-F03)
- **Change (Stamina):** params_core Stamina row corrected from `End + Relevant History + 1` to `End + 1` per stage1 §3.9. History does not contribute to Stamina.
- **Change (Health):** params_core Health row clarified: `End + 6` is the base buffer score. Wound-interval reset mechanics moved to Notes column.
- **Impact:** Stamina calculations were inflated by History bonus. Health formula was misleadingly presented as a multiplier.

## PP-249 — Ob cap propagation: stage1 §1.3 updated to Ob 20
- **Date:** 2026-04-04
- **Source:** SIM-C-01 pre-simulation audit (AUD-F06); PP-232 raised cap to 20 in params_core but stage1 was not updated.
- **Change:** stage1 §1.3 Ob cap updated from 10 to 20. Ob stacking cap updated. Degrees table Ob 20 exception updated.
- **Impact:** Removes ambiguity about which cap governs. PP-232 is now consistently applied across both canonical sources.