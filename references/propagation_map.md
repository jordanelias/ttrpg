# VALORIA PROPAGATION MAP
## Last updated: 2026-04-02
## Version: 2.0 — self-maintaining
## Format: machine-readable YAML blocks + human-readable tables

---

## AUTO-UPDATE PROTOCOL (runs on EVERY commit — not optional)

Before any commit closes, the orchestrator executes this protocol:

### Step A — New file detection
For every file being added in this commit:
1. Determine its system(s): which of TTRPG/Hybrid/BG/ALL does it cover?
2. Determine its type: DESIGN / TEST / COMPILED / SKILL / REF / TOOL / LOG
3. Determine its dependencies: which existing files does it draw mechanical values from?
4. Determine who depends on it: which existing files reference or will need to reference it?
5. Add a row to the appropriate section of this map.
6. Add a row to `references/file_index.md` CURRENT FILES section.
7. If the file is a design doc: add it to `references/propagation_map.md` under its system heading.

If you cannot determine dependencies at commit time, add the file with `depends_on: [UNKNOWN — audit required]` and flag it in the commit message as `[PROP-UNKNOWN: filename]`.

### Step B — New cross-reference detection
A new cross-reference exists whenever a simulation finding, patch, or editorial item links:
- a finding in file X to a rule in file Y (that was not previously linked)
- a patch applied to file X that affects values extracted in params file Y
- an editorial decision in file X that changes rules referenced in file Y

For each new cross-reference:
1. Add the relationship to the propagation map under the relevant system heading.
2. If the relationship is bidirectional, add it in both directions.
3. Update `references/file_index.md` `referenced_by` column for both files.

### Step C — Stale detection
After adding new entries, scan all existing entries:
- If a file listed in `depends_on` no longer exists: mark `[BROKEN DEPENDENCY]`
- If a file in `propagation_targets` no longer exists: mark `[BROKEN TARGET]`
- Report broken entries in commit message as `[PROP-BROKEN: entry]`

### Step D — Commit
Include the updated propagation_map.md in the same atomic commit as all other changed files.
Never commit a design file, params file, or test file without also committing the updated propagation map.

---

## DEPENDENCY RULES BY FILE TYPE

These rules determine propagation targets automatically based on file type and system.
The orchestrator applies these rules to any new file before asking for manual input.

| If you create or modify... | Always check/update... |
|---------------------------|------------------------|
| Any `designs/` file | Its params file (`references/params_*.md` for its system) |
| Any `designs/` file | `references/file_index.md` |
| Any `designs/` file | `references/propagation_map.md` (this file) |
| Any `designs/` file with `[EDITORIAL: ...]` flags | `canon/editorial_ledger.yaml` |
| Any `designs/` file with patches | `canon/patch_register.yaml` |
| Any `references/params_*.md` | Any skill that loads that params file (see params-skill map below) |
| Any `tests/sim_*.md` | `tests/coverage_matrix.md` |
| Any `tests/sim_*.md` | Patched design files (via Mode I) |
| Any `canon/patch_register.yaml` | `references/file_index.md` KNOWN STALE SYNC GAPS |
| Any `canon/editorial_ledger.yaml` | `session_log_current.md` editorial_decisions_pending |
| Any `compilation/v0.14/*.md` | Its corresponding `references/params_*.md` |
| Any `skills/*.md` | `skills/valoria-orchestrator/references/skill_registry.md` |
| Any new `designs/gm_ref_cp14/flowcharts/*.md` | `designs/ttrpg/valoria_emergent_scenarios.md` cross-reference section |

## PARAMS-SKILL DEPENDENCY MAP (auto-enforced)

| Params file | Skills that load it | Design docs that source it |
|-------------|--------------------|-----------------------------|
| `params_core.md` | ALL skills | `stage1_core_engine.md` |
| `params_combat.md` | simulator G1, combat-simulator | `designs/combat/combat_design_v1.md`, `stage8_combat.md` |
| `params_mass_combat.md` | simulator G1 | `designs/mass_combat/mass_battle_v3.md`, `stage8_combat.md` |
| `params_debate.md` | simulator G2 | `designs/debate/debate_system_redesign_v1.md` |
| `params_threadwork.md` | simulator G3 | `designs/ttrpg/threadwork_redesign_v25.md` |
| `params_factions.md` | simulator G4, mechanic-audit | `stage6_factions.md`, `designs/board_game/valoria_bg_v05_simulation_and_patches.md` |
| `params_board_game.md` | simulator G5 | `designs/board_game/valoria_bg_v05_simulation_and_patches.md` |
| `params_scale_transitions.md` | simulator K2 | `compilation/v0.14/stage11_scale_transitions.md` |

When any source doc changes: its params file is stale. Add to `file_index.md` KNOWN STALE SYNC GAPS immediately. Do not wait until the next session.

---

## SYSTEM PROPAGATION TABLES

### CORE ENGINE

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `canon/00_philosophical_foundations.md` | ALL design files | Canon authority — triggers full canon-guard pass |
| `compilation/v0.14/stage1_core_engine.md` | `references/params_core.md` | Extracted values |
| `references/params_core.md` | All skills (dice engine baseline) | All simulations depend on core |

### THREADWORK

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `designs/ttrpg/threadwork_redesign_v25.md` | `references/params_threadwork.md` | Extracted values |
| `designs/ttrpg/threadwork_redesign_v25.md` | `designs/mass_combat/mass_battle_v3.md` §A.10 | Thread in mass battle depends on operation definitions |
| `designs/ttrpg/threadwork_redesign_v25.md` | `compilation/v0.14/stage15_spell_catalog.md` | W-series operations |
| `designs/ttrpg/threadwork_redesign_v25.md` | `designs/gm_ref_cp14/dashboards/d06_thread_operation_resolution_card.md` | Dashboard sync |
| `references/params_threadwork.md` | `skills/valoria-simulator-SKILL.md` (Mode G3) | Sim loads params |

### COMBAT

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `designs/combat/combat_design_v1.md` | `references/params_combat.md` | Extracted values |
| `designs/combat/combat_design_v1.md` | `references/params_mass_combat.md` | Mass combat unit table sourced here |
| `designs/combat/combat_design_v1.md` | `designs/mass_combat/mass_battle_v3.md` | Unit stats, reach rules, weapon table shared |
| `designs/mass_combat/mass_battle_v3.md` | `references/params_mass_combat.md` | Extracted values |
| `designs/mass_combat/mass_battle_v3.md` | `designs/board_game/valoria_bg_v05_simulation_and_patches.md` §B.3/B.5 | BG battle resolution references mass battle |
| `designs/mass_combat/mass_battle_v3.md` | `compilation/v0.14/stage11_scale_transitions.md` | Phase structure referenced in scale transitions |
| `designs/mass_combat/mass_battle_v3.md` | `skills/valoria-orchestrator/references/state_transfer_spec.md` | Phase timing drives state transfer rules |
| `references/params_combat.md` | `skills/valoria-combat-simulator/SKILL.md` | Sim loads params |
| `references/params_mass_combat.md` | `skills/valoria-simulator-SKILL.md` (Mode G1) | Sim loads params |

### DEBATE

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `designs/debate/debate_system_redesign_v1.md` | `references/params_debate.md` | Extracted values |
| `designs/debate/debate_system_redesign_v1.md` | `compilation/v0.14/stage9_social.md` | Stale — needs rewrite |
| `references/params_debate.md` | `skills/valoria-simulator-SKILL.md` (Mode G2) | Sim loads params |

### BOARD GAME

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `designs/board_game/valoria_bg_v05_simulation_and_patches.md` | `references/params_board_game.md` | Extracted values |
| `designs/board_game/valoria_bg_v05_simulation_and_patches.md` | `references/params_factions.md` (BG column) | BG faction mechanics |
| `designs/board_game/valoria_bg_v05_simulation_and_patches.md` | `compilation/v0.14/stage_bg_board_game_mode.md` | Stale — needs sync (ED-001 blocker) |
| `references/params_board_game.md` | `skills/valoria-simulator-SKILL.md` (Mode G5) | Sim loads params |

### FACTIONS

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `compilation/v0.14/stage6_factions.md` | `references/params_factions.md` (TTRPG column) | Extracted values |
| `references/params_factions.md` | `skills/valoria-simulator-SKILL.md` (Mode G4) | Sim loads params |
| `references/params_factions.md` | `skills/valoria-mechanic-audit-SKILL.md` | Audit loads params |

### SCALE TRANSITIONS / HYBRID

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `compilation/v0.14/stage11_scale_transitions.md` | `references/params_scale_transitions.md` | Extracted values |
| `compilation/v0.14/stage11_scale_transitions.md` | `skills/valoria-orchestrator/references/state_transfer_spec.md` | Phase structure drives transfer rules |
| `skills/valoria-orchestrator/references/state_transfer_spec.md` | `skills/valoria-simulator-SKILL.md` (Mode K2) | Transition tests load spec |
| `designs/hybrid/hybrid_gaps_resolved.md` | `compilation/v0.14/stage11_scale_transitions.md` | Pending integration |
| `designs/hybrid/hybrid_gaps_resolved.md` | `designs/board_game/valoria_bg_v05_simulation_and_patches.md` §B.5 | Pending integration |

### GM REFERENCE / FLOWCHARTS

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| Any `designs/gm_ref_cp14/arcs/*.md` | `tests/coverage_matrix.md` | If simulated, log it |
| Any `designs/gm_ref_cp14/arcs/*.md` | `canon/editorial_ledger.yaml` | Harvest EDITORIAL flags |
| Any `designs/gm_ref_cp14/flowcharts/*.md` (NEW) | `designs/ttrpg/valoria_emergent_scenarios.md` | Cross-reference section |
| `designs/ttrpg/valoria_emergent_scenarios.md` | `designs/ttrpg/valoria_narrative_scenario_chains.md` | Sibling document — check for contradictions |

### SESSION / REGISTRY FILES

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `canon/patch_register.yaml` | `references/file_index.md` | Stale gap tracking |
| `canon/editorial_ledger.yaml` | `session_log_current.md` | editorial_decisions_pending |
| `session_log_current.md` | `session_log_archive.md` | On session close |

---

## BROKEN DEPENDENCIES (auto-detected, log here)

| File | Broken Reference | Detected | Status |
|------|-----------------|----------|--------|
| `compilation/v0.14/stage3_thread_operations.md` | References threadwork operations — empty/stale | 2026-04-02 | KNOWN — awaiting rewrite from threadwork_v25 |
| `compilation/v0.14/stage9_social.md` | References debate system — empty/stale | 2026-04-02 | KNOWN — awaiting rewrite from debate_system_redesign_v1 Part 6 |
| `compilation/v0.14/stage_bg_board_game_mode.md` | References BG rules — stale | 2026-04-02 | KNOWN — ED-001 blocker |

---

*This map is updated in every commit that touches any file listed here. It is never updated manually in isolation — always part of an atomic commit containing the files being linked.*
