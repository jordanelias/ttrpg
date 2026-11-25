# Handoff — PC (Personal Combat)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a `path` or
`path:line`, or a command to run. Restate no count, status or date of state here. Narrative:
`HANDOFF_PC_history.md`; finished work: `HANDOFF_PC_closed.md`.

## Open

| item | where it lives | next step |
|---|---|---|
| Batch B16-pc-round — IN FLIGHT | `workplans/valoria_master_workplan_v12_part23.md`, "Batch B16-pc-round"; open 8142371d0 | built B16.01 B16.02 B16.03 B16.04 · close none · B16.05 to B16.11 build, then B16.99 (rebases on B08's and B12a's merges, plan §7.4; neither is on `main`) |
| B15's held residue: the fight-length window against the yield roll, cell (7,5), the riposte's certain matchups and its counter, the mortal draw's middle band | `registers/editorial_ledger_pc.jsonl` (id `ED-PC-0064`, `needs_jordan`); `engine/season/hole_register.yaml` H-575 (the slope bound's knob), H-576 (left for dead writes as lives), H-577 (the record omits the spared outcome and shaken/rallied), H-578 (the helper is any non-fighter at the place), H-579 (the riposte, the bare-zone draw's mean) | Jordan's ruling on ED-PC-0064; `python -m pytest tests/valoria/test_combat_opposed_rule_shape.py -q` reads the (7,5) red until then |
| CP-T03-06, the survivor's grudge: measured and designed, the BUILD held | `proposals/2026-11-24-b15-14-survivors-grudge.md` (`PROPOSED`; Stage 1 mint and read, Stage 2 the deposit rule only if Stage 1 leaves non-actor patients) | a later batch builds Stage 1 on the design's merge; the reading is in the commit body of B15.14's `Item:` commit |
| PC-10a — duel terms in the module (commit `daae7401`, batch B-Y) | `modules/combat/wrapper.py` (`DUEL_TERMS`, `fight(terms=)`); `modules/combat/config.py` `CFG['YIELD_HEALTH_FRAC']`; `tests/valoria/test_combat_duel_terms.py` | PC-10b is built (`d2847e7b`, B10-11 close two); the season side reads it through `engine/season/hole_register.yaml` H-240, H-255 |
| I1 — the season reaches almost none of the personal-combat engine | PC-10b (duel terms and yield) is built, `d2847e7b` (B10-11 close two); `FORK:1b7c2f87:workplans/valoria_master_workplan_v11_part5.md` PC-06 (a combatant from the person: K-1/K-5, K-5 HELD) | No scheduled closer beyond those; B10-10b is closed (`FORK:1b7c2f87:workplans/valoria_master_workplan_v11_part3.md`, its close-six paragraph) |
| ED-PC-0007 — pessimist-audit PC action-menu consolidation | `registers/editorial_ledger_pc_archive.jsonl` (id `ED-PC-0007`, status deferred) | Reopen only if `combat_engine_v1` grows a discrete player-action menu |
| Channel-leverage residual (§C remainder, Phase 4c) — affinity budget fixed total competence, not per-channel leverage | `phase4_5_plan_v1.md` §4c | Design-laden (Jordan sets per-paradigm strength); re-measure with `python systems/combat/combat_engine_v1/workbench/balance.py context` once scoped (PC-08, `FORK:1b7c2f87:workplans/valoria_master_workplan_v11_part5.md`: LEAVE until named) |
| Abilities-as-access depth (Phase 4b) + game-theoretic layer (Phase 4a) + contact axis (Phase 5) + WS-7 multi-combatant | `phase4_5_plan_v1.md` §Phase 4 / §Phase 5 | Design-gated, no immediate action; WS-7 additionally gated on ED-911 ratification (PC-08, `FORK:1b7c2f87:workplans/valoria_master_workplan_v11_part5.md`) |
| R2 capstone finding — reach-class weapons run above the contested-balance target vs arming | `HANDOFF_PC_history.md`, heading "R2 (closing-distance/facing/grip/contact redesign)" | If a Phase-C engine-scale recalibration starts, read that finding first |

## Standing orders — do not re-raise, do not do

| order | source |
|---|---|
| Do not "restore" E2a's prescribed `strike_point_lever(w, elem_mass, elem_x)` signature — it double-counts mass, pinned by `test_element_lever_does_not_double_count_mass` | `HANDOFF_PC_history.md`, heading "E0–E3 ARE COMPLETE" |
| Do not implement the A7d curvature fix sketch as originally written (`min(1,eff/0.70)` is a no-op against the live population) | `HANDOFF_PC_history.md`, heading "2026-07-26 COMBAT ARC" |
| Never hand-edit a value into the `.gd` side to correct the Python oracle — fix canon, then re-export | `CLAUDE.md` §6, `ED-1050` |
