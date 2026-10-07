# Handoff — WR (World)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a `path` or `path:line`, or a command to run. Restate no count, status or date of state here. Narrative: `registers/handoffs/HANDOFF_WR_history.md`.

## Open
| item | where it lives | next step |
|---|---|---|
| threadwork WR-SCOPE build (`ED-WR-0010`: threadwork IS in scope) — three items remain | `systems/threadwork/sim/coherence.py` (two-quantity elastic/plastic model, `canon/philosophy/07_drift.md` §7.1/§7.4); `systems/threadwork/sim/operations.py`'s `_resolve_operation` (`ED-WR-0008`'s P-25 scale term, a formula on `COHERENCE_COST_BY_SCALE` — no separate table); `tests/valoria/test_coherence_elastic_plastic.py` | (1) no caller applies `R-14`'s practitioner-resilience term (RULINGS.md Batch 13 retracted "no toughness term" — `06_operations.md:331-359`; the replacement's arithmetic is unruled) — v9 WR-01; (2) Mending aimed at the mender's OWN configuration is not routed to `coherence.mend_resting_point` — it has no non-test caller, and the `target` dict has no whose-configuration field to route on (`operations.py`'s `attempt_mending` docstring, "NOT ROUTED HERE") — v9 WR-02; (3) `collective.py`'s and `opposing.py`'s Mending give the mender no restorative feedback, so they disagree with `attempt_mending` (NERS S), and each prices Mending Stability its own way (`opposing.py`'s scale-cost proxy; `collective.py`'s flat 0) — v9 WR-03, one pricing owner. All in `workplans/valoria_master_workplan_v9_part7.md`; each reaches `engine/season/` only after IN-06. Not open: `attempt_mending` calls `recover()` (`coherence_delta` stays 0 per ED-871 and `06_operations.md` §6.8) — only tests call it, and `environment_in_equilibrium` defaults to False; the P-25 term's missing reader was closed by `ED-WR-0008`'s superseding row |
| Port-bridge constants-parity risk from the coherence reshape | `tools/export_game_constants.py --check`; its `MAPPING` (the retired `COHERENCE_*` pairs are gone with their Python owners) | Cannot be checked from this repo: confirm `valoria-game`'s `tools/check_constants_parity.py` (or equivalent) tolerates a smaller `MAPPING`, not a fixed constant count (v9 GO-06, `workplans/valoria_master_workplan_v9_part7.md`) |
| `ED-WR-0010` consequence 3 ("the doc follows") for the P-25 scale term | `registers/editorial_ledger_wr_archive.jsonl` (`ED-WR-0010`); `systems/threadwork/sim/operations.py`'s `_resolve_operation` (the code half) | Code half done; doc half unwritten. Author it in `proposals/` — `.designs/` is quarantined (CLAUDE.md §1: do not add to it) (v9 WR-04, `workplans/valoria_master_workplan_v9_part7.md`) |

## Standing orders — do not re-raise, do not do
| order | source |
|---|---|
| none | — |
