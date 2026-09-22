# Handoff — PC (Personal Combat)

**Pointer index.** Every row names where its fact lives — a ledger id (its LAST row governs), a `path` or
`path:line`, or a command to run. This file restates no count, status or date of state: open or run the
pointer. The narrative this file used to carry is verbatim in `registers/handoffs/HANDOFF_PC_history.md`
(and finished work in `HANDOFF_PC_closed.md` where that exists).

## Open

| item | where it lives | next step |
|---|---|---|
| Delete the `partisan` polearm (Jordan ruled) | `ED-IN-0261` (`registers/editorial_ledger_in_archive.jsonl`); weapon still present at `systems/combat/combat_engine_v1/weapons.py:322,852` and `workbench/balance.py:37` | Delete the weapon, re-point its citing comments to `spetum`/`ranseur`, re-record the affected goldens, verify only `partisan` rows moved |
| PC-lane `ED-PC-` id block exhausted | `references/id_reservations.yaml:124` | Get a block release or a new reservation before filing another `ED-PC-NNNN` |
| ED-PC-0001 — post-R3 player-input surface not yet scheduled | `registers/editorial_ledger_pc.jsonl` (id `ED-PC-0001`) | Confirm R3's status, then add named sequence increments |
| ED-PC-0003 — OPT-10 sigma band-discipline unification | `registers/editorial_ledger_pc.jsonl` (id `ED-PC-0003`) | Land as its own verified PR with a regression pass (touches live resolver math) |
| ED-PC-0007 — pessimist-audit PC action-menu consolidation | `registers/editorial_ledger_pc.jsonl` (id `ED-PC-0007`, status deferred) | Reopen only if `combat_engine_v1` grows a discrete player-action menu |
| ED-PC-0013 — 3-item audit bundle (RESIST re-export, exporter scope fence, wound-penalty sweep) | `registers/editorial_ledger_pc.jsonl` (id `ED-PC-0013`) | Execute the three ratified sub-items |
| ED-PC-0016 — half-sword auto-switch activation held | `registers/editorial_ledger_pc_archive.jsonl` (id `ED-PC-0016`, `needs_jordan: true`) | Jordan decides the per-form conditional-switch design call |
| E-series/channel-batch calibration residues (poleaxe-vs-plate parity, thrust two-direction split, `CUT_REF_NATIVE` katana anchor, contact-moment gain parity, `CLOSE_ENGAGE_M` value, staff/mace `PERC_SCALE`/`PERC_EXP` re-fit) | `grep -h '"needs_jordan": true' registers/editorial_ledger_pc.jsonl` (ids `ED-PC-0047`, `0049`–`0055`) | Jordan rules each; none superseded yet — run the §0 five-step closure test first |
| ED-PC-0056 — §11.4 Surrender/Disengage is live spec with no implementation | `.designs/systems/combat/reference/combat_reference_v1.md` (quarantined reference) + `registers/editorial_ledger_pc.jsonl` (id `ED-PC-0056`) | Decide: a resolver in `combat_engine_v1/`, or strike the spec |
| Channel-leverage residual (§C remainder, Phase 4c) — affinity budget fixed total competence, not per-channel leverage | `.designs/systems/combat/combat_engine_v1/reference/phase4_5_plan_v1.md` §4c | Design-laden (Jordan sets per-paradigm strength); re-measure with `python systems/combat/combat_engine_v1/workbench/balance.py context` once scoped |
| Abilities-as-access depth (Phase 4b) + game-theoretic layer (Phase 4a) + contact axis (Phase 5) + WS-7 multi-combatant | `.designs/systems/combat/combat_engine_v1/reference/phase4_5_plan_v1.md` §Phase 4 / §Phase 5 | Design-gated, no immediate action; WS-7 additionally gated on ED-911 ratification |
| R2 capstone finding — reach-class weapons run above the contested-balance target vs arming | `HANDOFF_PC_history.md`, heading "R2 (closing-distance/facing/grip/contact redesign)" | If a Phase-C engine-scale recalibration starts, read that finding first |

## Standing orders — do not re-raise, do not do

| order | source |
|---|---|
| Do not "restore" E2a's prescribed `strike_point_lever(w, elem_mass, elem_x)` signature — it double-counts mass, pinned by `test_element_lever_does_not_double_count_mass` | `HANDOFF_PC_history.md`, heading "E0–E3 ARE COMPLETE" |
| Do not implement the A7d curvature fix sketch as originally written (`min(1,eff/0.70)` is a no-op against the live population) | `HANDOFF_PC_history.md`, heading "2026-07-26 COMBAT ARC" |
| Never hand-edit `combat_config.gd` to correct the Python oracle — fix canon, then re-export | `CLAUDE.md` §6, `ED-1050` |

