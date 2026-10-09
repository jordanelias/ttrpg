# Handoff — PC (Personal Combat)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a `path` or
`path:line`, or a command to run. Restate no count, status or date of state here. Narrative:
`registers/handoffs/HANDOFF_PC_history.md`; finished work: `HANDOFF_PC_closed.md`.

## Open

| item | where it lives | next step |
|---|---|---|
| ED-PC-0007 — pessimist-audit PC action-menu consolidation | `registers/editorial_ledger_pc_archive.jsonl` (id `ED-PC-0007`, status deferred) | Reopen only if `combat_engine_v1` grows a discrete player-action menu |
| ED-PC-0013 — audit bundle, item 1: the `.gd` RESIST re-export is held with the port | `registers/editorial_ledger_pc_archive.jsonl` (id `ED-PC-0013`, last row); v9 PC-05 and GO-05 (`workplans/valoria_master_workplan_v9_part7.md`) | PC-05: item 1 after GO-05, which follows GO-01 (J-9) |
| Channel-leverage residual (§C remainder, Phase 4c) — affinity budget fixed total competence, not per-channel leverage | `.designs/systems/combat/combat_engine_v1/reference/phase4_5_plan_v1.md` §4c | Design-laden (Jordan sets per-paradigm strength); re-measure with `python systems/combat/combat_engine_v1/workbench/balance.py context` once scoped (v9 PC-08, `workplans/valoria_master_workplan_v9_part7.md`: LEAVE until named) |
| Abilities-as-access depth (Phase 4b) + game-theoretic layer (Phase 4a) + contact axis (Phase 5) + WS-7 multi-combatant | `.designs/systems/combat/combat_engine_v1/reference/phase4_5_plan_v1.md` §Phase 4 / §Phase 5 | Design-gated, no immediate action; WS-7 additionally gated on ED-911 ratification (v9 PC-08, `workplans/valoria_master_workplan_v9_part7.md`) |
| R2 capstone finding — reach-class weapons run above the contested-balance target vs arming | `HANDOFF_PC_history.md`, heading "R2 (closing-distance/facing/grip/contact redesign)" | If a Phase-C engine-scale recalibration starts, read that finding first |

## Standing orders — do not re-raise, do not do

| order | source |
|---|---|
| Do not "restore" E2a's prescribed `strike_point_lever(w, elem_mass, elem_x)` signature — it double-counts mass, pinned by `test_element_lever_does_not_double_count_mass` | `HANDOFF_PC_history.md`, heading "E0–E3 ARE COMPLETE" |
| Do not implement the A7d curvature fix sketch as originally written (`min(1,eff/0.70)` is a no-op against the live population) | `HANDOFF_PC_history.md`, heading "2026-07-26 COMBAT ARC" |
| Never hand-edit `combat_config.gd` to correct the Python oracle — fix canon, then re-export | `CLAUDE.md` §6, `ED-1050` |
