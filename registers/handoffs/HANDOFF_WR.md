# Handoff — WR (World)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a `path` or `path:line`, or a command to run. Restate no count, status or date of state here. Narrative: `registers/handoffs/HANDOFF_WR_history.md`.

## Open
| item | where it lives | next step |
|---|---|---|
| threadwork WR-SCOPE build (`ED-WR-0010`: threadwork IS in scope) — built; three design calls remain | `systems/threadwork/sim/operations.py` (`RESILIENCE_GAIN`, `RESILIENCE_GAIN_SWEEP`, `resist_coherence_cost`, `RESTING_POINT_MEND_BY_DEGREE`, `price_mending`); `systems/threadwork/sim/coherence.py`; `tests/valoria/test_threadwork_resilience.py`; `tests/valoria/test_threadwork_mending_parity.py`; `tests/valoria/test_coherence_elastic_plastic.py` | (1) `R-14`'s arithmetic is unruled (RULINGS.md Batch 13; `06_operations.md:331-359`): `RESILIENCE_GAIN` ships at the control 0, so the term does nothing until a gain and the slot that fills `actor.resilience` are ruled; (2) own-configuration Mending (`target['configuration_of']`) rolls the ordinary `MENDING_OB` and costs nothing (ED-871), so repeated casts can walk a permanent set to 0 — a cost, a cadence or a harder Ob (`operations.py`, comment above `RESTING_POINT_MEND_BY_DEGREE`); (3) `collective.py` and `opposing.py` refuse a Mending whose `configuration_of` names a participant (only `attempt_mending` routes it), and being mended BY another (§6.8's third case) is not routed. Each reaches `engine/season/` only after IN-06 |
| Port-bridge constants-parity risk from the coherence reshape | `tools/export_game_constants.py --check`; its `MAPPING` (the retired `COHERENCE_*` pairs are gone with their Python owners) | Cannot be checked from this repo: confirm `valoria-game`'s `tools/check_constants_parity.py` (or equivalent) tolerates a smaller `MAPPING`, not a fixed constant count (v9 GO-06, `workplans/valoria_master_workplan_v9_part7.md`) |

## Standing orders — do not re-raise, do not do
| order | source |
|---|---|
| none | — |
