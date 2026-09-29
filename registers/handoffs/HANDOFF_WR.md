# Handoff — WR (World)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a `path` or `path:line`, or a command to run. This file restates no count, status or date of state: open or run the pointer. The narrative this file used to carry is verbatim in `registers/handoffs/HANDOFF_WR_history.md`.

## Open
| item | where it lives | next step |
|---|---|---|
| threadwork WR-SCOPE build (`ED-WR-0010` ruled: threadwork IS in scope) — `27`'s board row (`the-plan...md` position 27) stays OPEN: `27` also names the `rendering.py` stubs and `ED-WR-0003` below, neither built by this pass | `systems/threadwork/sim/coherence.py` (two-quantity elastic/plastic model, `canon/philosophy/07_drift.md` §7.1/§7.4); `systems/threadwork/sim/operations.py`'s `_resolve_operation` (`ED-WR-0008`'s P-25 scale term, a formula on `COHERENCE_COST_BY_SCALE` — no separate table); `tests/valoria/test_coherence_elastic_plastic.py` | Four things this position did NOT build, each outside its own scope (CLAUDE.md §4): `attempt_mending` still costs 0 and doesn't call `recover()` (C-1 says restorative work should move the mender toward equilibrium); `operations.py`'s own new P-25 term has no reader (`mending_stability_delta` is set, nothing consumes it outside the test file — `ED-WR-0008`'s own superseding row already closed on this); `opposing.py` and `collective.py` each compute Weaving/Pulling Mending Stability a third and fourth way (opposing.py's own scale-cost proxy; collective.py's flat 0) — three inconsistent methodologies for one quantity (NERS S); no caller applies `R-14`'s practitioner-resilience term (RULINGS.md Batch 13 retracted "no toughness term" — `06_operations.md:331-359` — and nothing in the tree implements the replacement yet, since its arithmetic is unruled) |
| Port-bridge constants-parity risk from the coherence reshape | `tools/export_game_constants.py --check`; its `MAPPING` (the retired `COHERENCE_*` pairs are gone — their Python owners no longer exist after the reshape) | Cannot be checked from this repo: confirm `valoria-game`'s `tools/check_constants_parity.py` (or equivalent) tolerates a smaller `MAPPING`, not a fixed constant count |
| `ED-WR-0010` consequence 3 ("the doc follows") for the P-25 scale term | `registers/editorial_ledger_wr_archive.jsonl` (`ED-WR-0010`); `systems/threadwork/sim/operations.py`'s `_resolve_operation` (the code half) | Code half done; doc half unwritten. Author it in `proposals/` — `.designs/` is quarantined (CLAUDE.md §1: do not add to it) |
| `rendering.py` wired stubs — personal/strategic-scale seam (threadwork → substrate tension → incursions → Accord) — part of `27`'s own scope (`the-plan...md` position 27), not independent backlog | `systems/threadwork/sim/rendering.py` (`apply_rs_strain`, `check_calamity_threshold`) | Wire the two stubs; Turmoil and MS (`systems/overview/sim/ms_track.py`) are already live underneath them |
| ambient-fabric window + Appraise Revelation — part of `27`'s own scope (`the-plan...md` position 27), not independent backlog | `registers/editorial_ledger_wr.jsonl` (`ED-WR-0003`) | Write the "overheard" conditional-observer rule plus the revelation procedures |

## Standing orders — do not re-raise, do not do
| order | source |
|---|---|
| none | — |
