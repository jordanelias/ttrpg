# VALORIA PROPAGATION MAP
## Last updated: 2026-04-02
## Purpose: When file X changes, which other files must be checked/updated?
## Used by: valoria-orchestrator, valoria-compiler, valoria-editorial-register
## Rule: Any commit touching a file in the LEFT column must verify and update files in the RIGHT column.

---

## HOW TO USE

Before committing a change to any file, look it up in the left column.
Every file in the right column is a **propagation target** — it may need a corresponding update.
If it does not need updating, add a comment in the commit message: `[no-prop: reason]`.

---

## CORE ENGINE → PROPAGATES TO EVERYTHING

| Changed File | Must Check / Update |
|-------------|---------------------|
| canon/00_philosophical_foundations.md | ALL DESIGN FILES — canon guard pass required before any downstream update |
| canon/01_foundations_amendment_self_rendering.md | All threadwork files, stage3, stage17_canon_guard |
| canon/02_canon_constraints.md | stage1_core_engine, all stage files |
| compilation/v0.14/stage1_core_engine.md | references/params_core.md; all other stage files |
| compilation/v0.14/stage2_characters.md | references/params_core.md; stage8, stage10 |

---

## THREADWORK

| Changed File | Must Check / Update |
|-------------|---------------------|
| designs/ttrpg/threadwork_redesign_v25.md | references/params_threadwork.md; compilation/v0.14/stage3_thread_operations.md; compilation/v0.14/stage15_spell_catalog.md; designs/mass_combat/mass_battle_v3.md (§A.10); designs/gm_ref_cp14/dashboards/d06_thread_operation_resolution_card.md |
| compilation/v0.14/stage3_thread_operations.md | references/params_threadwork.md |
| references/params_threadwork.md | Any skill or sim that loads threadwork params |

---

## COMBAT

| Changed File | Must Check / Update |
|-------------|---------------------|
| compilation/v0.14/stage8_combat.md | references/params_combat.md; references/params_mass_combat.md; designs/mass_combat/mass_battle_v3.md (cross-references); skills/valoria-combat-simulator/references/combat_params.md |
| designs/mass_combat/mass_battle_v3.md | references/params_mass_combat.md; designs/board_game/valoria_bg_v05_simulation_and_patches.md (§B.3, B.5 intersection); compilation/v0.14/stage8_combat.md (§8.9 must stay consistent with mass_battle_v3) |
| references/params_combat.md | skills/valoria-combat-simulator uses this — verify sim still valid |
| references/params_mass_combat.md | Any sim using mass combat params |

---

## BOARD GAME

| Changed File | Must Check / Update |
|-------------|---------------------|
| designs/board_game/valoria_bg_v05_simulation_and_patches.md | references/params_board_game.md; references/params_factions.md (BG column); compilation/v0.14/stage_bg_board_game_mode.md; compilation/v0.14/stage6_factions.md (BG faction rules — note: stage6 is STALE for BG) |
| compilation/v0.14/stage_bg_board_game_mode.md | references/params_board_game.md; bg_v05_simulation_and_patches.md |
| references/params_board_game.md | Any sim loading BG params |

---

## DEBATE

| Changed File | Must Check / Update |
|-------------|---------------------|
| designs/debate/debate_system_redesign_v1.md | references/params_debate.md; compilation/v0.14/stage9_social.md (STALE — needs rewrite); designs/gm_ref_cp14/dashboards (any debate-relevant dashboard) |
| references/params_debate.md | Any sim loading debate params |
| compilation/v0.14/stage9_social.md | references/params_debate.md |

---

## FACTIONS

| Changed File | Must Check / Update |
|-------------|---------------------|
| compilation/v0.14/stage6_factions.md | references/params_factions.md (TTRPG column); designs/ttrpg/* (faction-specific mechanics); NOTE: does NOT propagate to BG faction rules (those come from bg_v05) |
| references/params_factions.md | Any sim loading faction params |

---

## SCALE TRANSITIONS / HYBRID

| Changed File | Must Check / Update |
|-------------|---------------------|
| compilation/v0.14/stage11_scale_transitions.md | references/params_scale_transitions.md; designs/hybrid/hybrid_gaps_resolved.md; designs/board_game/valoria_bg_v05 (§B.5 hybrid handoff) |
| designs/hybrid/hybrid_gaps_resolved.md | stage11_scale_transitions.md; bg_v05 (§B.5) |
| references/params_scale_transitions.md | Any sim loading scale transition params |

---

## PATCH REGISTER

| Changed File | Must Check / Update |
|-------------|---------------------|
| canon/patch_register.yaml | references/file_index.md (KNOWN STALE SYNC GAPS section); session_log_current.md (commits_this_session) |

---

## SESSION LOGS

| Changed File | Must Check / Update |
|-------------|---------------------|
| session_log_current.md | session_log_archive.md (append old current on session close) |

---

## GM REFERENCE (arcs / dashboards)

| Changed File | Must Check / Update |
|-------------|---------------------|
| Any arc file (arcs_NN_NN_*.md) | tests/simulation_report_arcs_*.md (if simulation was run); canon/editorial_ledger.yaml (harvest any EDITORIAL flags in the arc) |
| Any dashboard file | Source stage file (verify dashboard reflects compiled state) |

---

## CANON AUDIT FILES

| Changed File | Must Check / Update |
|-------------|---------------------|
| canon/audit_threadwork_v25.md | Trigger canon-guard pass on threadwork_redesign_v25.md to verify audit is still valid |

---

## PROPAGATION PROTOCOL (for valoria-orchestrator)

When committing any file:

1. Look up the file in this map.
2. For each propagation target listed:
   a. If target needs update: include it in the same atomic commit.
   b. If target does NOT need update (e.g., the change is additive and doesn't affect extracted values): add note `[no-prop: reason]` to commit message.
3. After commit: check `references/file_index.md` KNOWN STALE SYNC GAPS section and update if the commit resolved a stale gap.

**Params sync rule:** After any patch is applied to a source document, the corresponding params file is considered STALE until explicitly re-synced. Add to KNOWN STALE SYNC GAPS in file_index.md. Resolve in the following session's params update pass.

---

## PARAMS SYNC PASS (periodic task)

Run at the start of any session where simulations are planned.
For each params file listed in KNOWN STALE SYNC GAPS:
1. Read source document (via GraphQL batch read).
2. Extract updated mechanical values.
3. Update params file.
4. Remove from KNOWN STALE SYNC GAPS.
5. Atomic commit.

---

*Propagation map is maintained by valoria-orchestrator. Add new entries whenever a new design file is created or a new dependency relationship is identified.*
