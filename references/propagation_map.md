# VALORIA PROPAGATION MAP
## Last updated: 2026-04-03
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

### Step C — Stale detection (executable)
Run `tools/broken_dependency_checker.py` before closing any commit.

```bash
export GITHUB_PAT=<pat>
python3 tools/broken_dependency_checker.py
```

The script:
1. Fetches the full repository file tree from GitHub
2. Scans propagation_map.md, canonical_sources.yaml, skill_registry.md, and editorial_ledger.yaml
3. Reports every file reference that does not exist in the repo
4. Exits 1 if any broken dependency found; 0 if clean

If broken dependencies are found:
- Do NOT close the commit until resolved
- Either fix the reference (update the path) or add `[BROKEN-DEP: path — reason]` to the commit message with an explanation
- Update the BROKEN DEPENDENCIES section of this file

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

### DEBATE

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `designs/debate/debate_system_redesign_v1.md` | `references/params_debate.md` | Values extracted; patches must sync |
| `designs/debate/debate_system_redesign_v1.md` | `compilation/v0.14/stage9_social.md` | STALE — stage9 is empty; compile when stable |
| `references/params_debate.md` | `skills/valoria-simulator-SKILL.md` (Mode G2) | Sim loads params |
| `tests/sim_d_01_debate_stress_test.md` | `tests/coverage_matrix.md` | Findings logged |
| `tests/sim_d_02_debate_scenario_c.md` | `tests/coverage_matrix.md` | Findings logged |
| `tests/sim_d_02_debate_scenario_c.md` | `canon/editorial_ledger.yaml` | ED-051, ED-052 harvested |
| `tests/audit_debate_a_g.md` | `tests/coverage_matrix.md` | Audit findings logged |
| `tests/audit_debate_a_g.md` | `canon/editorial_ledger.yaml` | ED-053–059 harvested |
| `tests/sim_d_03_subsystem_k.md` | `tests/coverage_matrix.md` | G2+K findings logged |
| `tests/sim_d_03_subsystem_k.md` | `skills/valoria-orchestrator/references/state_transfer_spec.md` | K2-F-02: debate Zoom In gap |
| `tests/sim_d_04_gap_fill_stress.md` | `tests/coverage_matrix.md` | Gap-fill verification logged |
| `designs/debate/debate_system_redesign_v1.md` | `references/params_debate.md` | v1.6 — params_debate needs §§6.11-6.15 values extracted |
| `tests/audit_d02_sim_d05.md` | `tests/coverage_matrix.md` | Audit + stress test findings logged |
| `tests/audit_d02_sim_d05.md` | `canon/editorial_ledger.yaml` | ED-087-091 harvested |
| `gm_ref/debate_ref_card_v1.md` | `designs/debate/debate_system_redesign_v1.md` | Reference card must track v1.x |
| `compilation/v0.14/stage13_npcs.md` | `designs/debate/debate_system_redesign_v1.md` | NPC Composure/attributes feed debate sim |

### SCALE TRANSITIONS / HYBRID

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `compilation/v0.14/stage11_scale_transitions.md` | `references/params_scale_transitions.md` | Extracted values |
| `compilation/v0.14/stage11_scale_transitions.md` | `skills/valoria-orchestrator/references/state_transfer_spec.md` | Phase structure drives transfer rules |
| `skills/valoria-orchestrator/references/state_transfer_spec.md` | `skills/valoria-simulator-SKILL.md` (Mode K2) | Transition tests load spec |
| `designs/hybrid/hybrid_gaps_resolved.md` | `compilation/v0.14/stage11_scale_transitions.md` | Pending integration |
| `designs/hybrid/hybrid_gaps_resolved.md` | `designs/board_game/valoria_bg_v05_simulation_and_patches.md` §B.5 | Pending integration |

### GM REFERENCE / FLOWCHARTS

| `designs/gm_ref_cp14/zoom_in_out_reference_card.md` (NEW) | `skills/valoria-orchestrator/references/state_transfer_spec.md` | Summarises spec §1 for table use |
| `designs/gm_ref_cp14/zoom_in_out_reference_card.md` (NEW) | `designs/mass_combat/mass_battle_v3.md` §B.2/B.5 | Pulls unit conversion table |
| `designs/mass_combat/mass_battle_v3.md` | `designs/gm_ref_cp14/zoom_in_out_reference_card.md` | B.5 references this card |

| `tests/sim_hyb_01_templar_crossing.md` (NEW) | `tests/coverage_matrix.md` | Simulation run — log row added |
| `tests/sim_hyb_01_templar_crossing.md` (NEW) | `canon/patch_register.yaml` | PP-101 sourced from this sim |
| `tests/sim_hyb_01_templar_crossing.md` (NEW) | `canon/editorial_ledger.yaml` | ED-054 flagged from this sim |
| `designs/mass_combat/mass_battle_v3.md` | `skills/valoria-orchestrator/references/state_transfer_spec.md` | B.5 BG→TTRPG conversion now cross-refs B.2 |
| `designs/mass_combat/mass_battle_v3.md` | `references/params_mass_combat.md` | PP-101 applied; params_mass_combat notes open gaps PARAMS-GAP-04/05 |


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



### BOARD GAME AUDIT 2026-04-02

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `references/params_board_game.md` | `designs/board_game/valoria_bg_v05_simulation_and_patches.md` | PP-115-122 gap fills |
| `references/params_board_game.md` | `canon/editorial_ledger.yaml` | ED-053-058 added |
| `references/params_board_game.md` | `canon/patch_register.yaml` | PP-112-122 added |
| `canon/editorial_ledger.yaml` | `session_log_current.md` | New editorial decisions pending |

## BROKEN DEPENDENCIES (auto-detected, log here)

| File | Broken Reference | Detected | Status |
|------|-----------------|----------|--------|
| `compilation/v0.14/stage3_thread_operations.md` | References threadwork operations — empty/stale | 2026-04-02 | KNOWN — awaiting rewrite from threadwork_v25 |
| `compilation/v0.14/stage9_social.md` | References debate system — empty/stale | 2026-04-02 | KNOWN — awaiting rewrite from debate_system_redesign_v1 Part 6 |
| `compilation/v0.14/stage_bg_board_game_mode.md` | References BG rules — stale | 2026-04-02 | KNOWN — ED-001 blocker |

---

*This map is updated in every commit that touches any file listed here. It is never updated manually in isolation — always part of an atomic commit containing the files being linked.*

*`tools/broken_dependency_checker.py` scans this map and others for broken refs. Run it as part of Step C before every commit closes.*

## tests/sim_bg_01.md
- system: BG
- type: TEST
- depends_on: [references/params_board_game.md, designs/board_game/valoria_bg_v05_simulation_and_patches.md, references/params_factions.md]
- referenced_by: [tests/coverage_matrix.md, canon/editorial_ledger.yaml]

## tests/sim_bg_balance_01.md
- system: BG
- type: TEST
- depends_on: [references/params_board_game.md, compilation/v0.14/stage_bg_board_game_mode.md]
- referenced_by: [tests/coverage_matrix.md, canon/patch_register.yaml]

## designs/board_game/stage_bg_proposal_v02.md (action economy canonical)
- system: BG
- type: DESIGN
- depends_on: [canon/00_philosophical_foundations.md, canon/02_canon_constraints.md]
- referenced_by: [references/params_board_game.md, references/canonical_sources.yaml]
- note: Canonical for BG action economy (PP-177). Mechanics/stats/VCs still from bg_v05.

## DOCREVIEW-BG-01 synthesis
- system: BG
- type: TEST
- depends_on: [designs/board_game/*.md, designs/gm_ref_cp14/arcs/*.md, references/params_board_game.md]
- referenced_by: [tests/coverage_matrix.md, canon/editorial_ledger.yaml, canon/patch_register.yaml]

### PP-172 — Ranged Subtypes (2026-04-02)
Source: designs/combat/combat_design_v1.md §5, §6
Propagation targets:
- references/params_combat.md → DONE (this commit)
- designs/mass_combat/mass_battle_v3.md → DONE (PP-173, this commit)
- references/params_mass_combat.md → DONE (PP-173, this commit)
- designs/board_game/ → NOT REQUIRED (BG abstracts above weapon-type level — confirmed SIM-003)

### PP-173 — Mass Combat Ranged DR (2026-04-02)
Source: designs/mass_combat/mass_battle_v3.md §A.4 (DR table)
Propagation targets:
- references/params_mass_combat.md → DONE (this commit)
- designs/board_game/ → NOT REQUIRED (BG abstracts above weapon type)
- references/propagation_map.md: PP-172 entry updated: mass_battle → DONE

### PP-175 — Mass Combat Ranged DR Scaling (2026-04-02)
Source: designs/mass_combat/mass_battle_v3.md §A.4 (Ranged DR table)
Finding: SIM-005-F1
Propagation targets:
- references/params_mass_combat.md → DONE (this commit)
- Pending ED-096 user confirmation — values marked PROVISIONAL

### ED-098 — Cover declaration ruling (2026-04-02)
Pending propagation:
- designs/combat/combat_design_v1.md §5 Environmental Factors → add: "Cover must be declared in Phase 1. Game Master determines physical availability. No declaration = no DR benefit that round."

### PP-188 — Ranged Redesign (2026-04-02)
Source: designs/combat/combat_design_v1.md §5 (weapon table, reach rules, armour DR)
Resolved: ED-061
Propagation targets:
- references/params_combat.md → DONE (this commit)
- designs/mass_combat/mass_battle_v3.md → DONE (this commit)
- references/params_mass_combat.md → DONE (this commit)
- session_log_current.md → DONE (this commit)

### PP-232 — Docx Review Batch (2026-04-03)
Propagation complete. All affected params updated in same commit (22ee783).
- references/params_core.md → DONE
- references/params_combat.md → DONE
- references/params_debate.md → DONE
- references/params_threadwork.md → DONE
- references/params_mass_combat.md → DONE
- references/params_scale_transitions.md → DONE (this commit)
- references/glossary.md → DONE (this commit)
- canon/editorial_ledger.yaml → DONE (ED-127–135 added)
- canon/patch_register.yaml → DONE
- tests/coverage_matrix.md → DONE (this commit)
- session_log_current.md → DONE (this commit)
- references/params_board_game.md → NOT REQUIRED (BG battle abstracts above unit-stat level; BG uses faction Military stat for battle resolution, not Size/Power/Discipline)
- references/params_factions.md → NOT REQUIRED (no mass combat stat references in factions params)

### PP-233 — Mass Combat Unit Formula (2026-04-03)
Source: design conversation 2026-04-03. Commit: 6db033d.
Propagation targets:
- references/params_mass_combat.md → DONE (6db033d)
- references/glossary.md → DONE (this commit — new terms: Size, Power, Discipline, Command, H, Total Health)
- tests/coverage_matrix.md → DONE (SIM-DEBT-03 added)
- session_log_current.md → DONE (this commit)
- designs/mass_combat/mass_battle_v3.md → STALE — unit formula in design doc predates PP-233. Needs rewrite on next design pass. [PROP-STALE: mass_battle_v3.md §B.1 unit stats]
- compilation/v0.14/stage8_combat.md → STALE — mass combat compilation predates PP-232/233. [PROP-STALE: stage8_combat.md]

## Propagation Pass — 2026-04-03 (ED batch from review session)
**EDs resolved and propagated:** ED-005, 006, 009, 014, 019, 022, 024, 029, 030, 034, 036, 056, 072, 080, 081, 083, 085, 086, 087, 094, 098, 109, 110, 121, 124, 130, 134
**Files updated:**
- references/params_debate.md — ED-009 (proceeding types), ED-014 (corroboration), ED-022 (violence/Unmask), ED-029 (Southernmost purpose rolls)
- references/params_combat.md — ED-098 (cover Phase 1), ED-130 (Stage 1/2 struck)
- references/params_threadwork.md — ED-030 (Mode 3 Thread combat), ED-034 (Ceiral Ritual RS), ED-086 (co-movement simultaneous), ED-121 (paradox window scene), ED-124 (Diagnosis struck mass battle), ED-134 (Diagnosis struck)
- references/params_mass_combat.md — ED-019 (tactic cards), ED-036 (Altonian stats confirmed), ED-094 (HP reload abstracted)
- references/params_factions.md — ED-005 (Maret Vossen, Aldric Hann), ED-006 (Riskbreakers identity)
- references/params_board_game.md — ED-056 (TC/Zoom In), ED-072 (concurrent Zoom In), ED-080/081 (Conviction texts), ED-083 (VTM5 P-14), ED-085 (Ignore penalised), ED-086 (co-movement), ED-087 (ranged modifier), ED-109 (Crown victory), ED-110 (Church TC)
**Status:** Complete for params layer. Design docs (designs/) not updated — skeleton debt flagged separately.

## PP-234 Propagation (2026-04-04)
- Attribute renames: Presence→Charisma, Memory→Recall propagated to: stage1, stage2, mass_battle_v3, params_core, params_mass_combat, params_factions.
- params_debate.md superseded by params_contest.md.
- debate_system_redesign_v1.md Part 6 superseded by social_contest_system_v2.md.
- Genre rename: Past→Memory, Present→(turfed), Future→Projection.
- Files NOT yet propagated: params_debate_history.md (historical, keep as-is), test outputs (flagged stale).
| references/sim_decision_protocols.md | sim_decision_protocols | skills/valoria-simulator-SKILL.md, tests/coverage_matrix.md | Protocol changes propagate to simulator skill and any test using actor protocol assignments |
| references/sim_decision_protocols.md | sim_decision_protocols | skills/valoria-simulator-SKILL.md, tests/coverage_matrix.md | Protocol library; changes propagate to all simulation test files using actor assignments |
| designs/combat/combat_design_v1.md (Feint §PP-291/293/294) | feint-partial-commit | references/params_combat.md | Feint versus roll + pool reduction; params must reflect current formula |
| designs/combat/combat_design_v1.md (Rescue §PP-290/292/295) | rescue-contested | references/params_combat.md, references/sim_decision_protocols.md | Rescue eligibility, contest, Momentum wound trigger |
| references/params_board_game.md (PP-296) | mandate-suppression | designs/board_game/valoria_bg_v05_simulation_and_patches.md | Mandate Ob cap 4 + coalition bonus; must propagate to BG design doc on next compile |
| designs/contest/social_contest_system_v2.md | contest-movement | references/params_contest.md | ED-295/296 open — CLASH/REINFORCE formula fixes pending; do not compile until resolved |
| references/params_combat.md (ED-200/201/202/203 rulings) | combat-rulings-2026-04-04 | designs/combat/combat_design_v1.md | Wound cap, carry-over, recovery, pool floor — resolved by design doc silence. Propagate to compilation on next pass. |
| references/params_contest.md (PP-401 REINFORCE floor) | reinforce-floor | designs/contest/social_contest_system_v2.md | REINFORCE max(0,...) floor. Propagate to design doc on next compilation. |

## ED-300 Propagation (2026-04-05)
| Source | Dependency key | Targets | Notes |
|--------|---------------|---------|-------|
| canon/editorial_ledger.yaml (ED-300) | domain-echo-scene-availability | designs/board_game/valoria_bg_v05_simulation_and_patches.md, references/params_board_game.md | Domain Echo reframe: availability declaration + escalation clock + primary/secondary yield. All-modes applicability. Propagate to BG design doc when ED-300 resolved. |

## ED-301 Propagation (2026-04-05)
| Source | Dependency key | Targets | Notes |
|--------|---------------|---------|-------|
| canon/editorial_ledger.yaml (ED-301) | ts-coherence-orthogonal | designs/ttrpg/threadwork_redesign_v25.md, references/params_threadwork.md, references/params_core.md | TS and Coherence are orthogonal axes. Coherence loss = expansion beyond human rendering frame, not degradation. Knots = relational bindings. Coherence 0 = rendering frame incompatibility, not incapacitation. Propagate to threadwork design doc and params when resolved. |
