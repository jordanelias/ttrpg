<!-- v30 path update applied 2026-04-13 -->
# VALORIA PROPAGATION MAP
## Last updated: 2026-04-14
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
| Any `designs/` file with patches | `canon/patch_register_active.yaml` |
| Any `references/params_*.md` | Any skill that loads that params file (see params-skill map below) |
| Any `tests/sim_*.md` | `tests/coverage_matrix.md` |
| Any `tests/sim_*.md` | Patched design files (via Mode I) |
| Any `canon/patch_register_active.yaml` | `references/file_index.md` KNOWN STALE SYNC GAPS |
| Any `canon/editorial_ledger.yaml` | `session_log_current.md` editorial_decisions_pending |
| Any `compilation/v0.14/*.md` | Its corresponding `references/params_*.md` |
| Any `skills/*.md` | `skills/valoria-orchestrator/references/skill_registry.md` |
| Any new `designs/gm_ref_cp14/flowcharts/*.md` | `designs/ttrpg/valoria_emergent_scenarios.md` cross-reference section |

## PARAMS-SKILL DEPENDENCY MAP (auto-enforced)

| Params file | Skills that load it | Design docs that source it |
|-------------|--------------------|-----------------------------|
| `params_core.md` | ALL skills | `stage1_core_engine.md` |
| `params_combat.md` | simulator G1, combat-simulator | `designs/combat/combat_v30.md`, `stage8_combat.md` |
| `params_mass_combat.md` | simulator G1 | `designs/mass_combat/mass_battle_v30.md`, `stage8_combat.md` |
| `params_debate.md` | simulator G2 | `designs/contest/social_contest_v30.md` |
| `params_threadwork.md` | simulator G3 | `designs/ttrpg/threadwork_v30.md` |
| `params_factions.md` | simulator G4, mechanic-audit | `stage6_factions.md`, `designs/board_game/board_game_v30.md` |
| `params_board_game.md` | simulator G5 | `designs/board_game/board_game_v30.md` |
| `params_scale_transitions.md` | simulator K2 | `compilation/v0.14/stage11_scale_transitions_deprecated.md` |

When any source doc changes: its params file is stale. Add to `file_index.md` KNOWN STALE SYNC GAPS immediately. Do not wait until the next session.

---

## SYSTEM PROPAGATION TABLES

### CORE ENGINE

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `canon/00_philosophical_foundations.md` | ALL design files | Canon authority — triggers full canon-guard pass |
| `compilation/v0.14/stage1_core_engine_deprecated.md` | `references/params_core.md` | Extracted values |
| `references/params_core.md` | All skills (dice engine baseline) | All simulations depend on core |

### THREADWORK

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `designs/ttrpg/threadwork_v30.md` | `references/params_threadwork.md` | Extracted values |
| `designs/ttrpg/threadwork_v30.md` | `designs/mass_combat/mass_battle_v30.md` §A.10 | Thread in mass battle depends on operation definitions |
| `designs/ttrpg/threadwork_v30.md` | `compilation/v0.14/stage15_spell_catalog_deprecated.md` | W-series operations |
| `designs/ttrpg/threadwork_v30.md` | `deprecated/designs/gm_ref_cp14/dashboards/d06_thread_operation_resolution_card_deprecated.md` | Dashboard sync |
| `references/params_threadwork.md` | `skills/valoria-simulator/SKILL.md` (Mode G3) | Sim loads params |

### COMBAT

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `designs/combat/combat_v30.md` | `references/params_combat.md` | Extracted values |
| `designs/combat/combat_v30.md` | `references/params_mass_combat.md` | Mass combat unit table sourced here |
| `designs/combat/combat_v30.md` | `designs/mass_combat/mass_battle_v30.md` | Unit stats, reach rules, weapon table shared |
| `designs/mass_combat/mass_battle_v30.md` | `references/params_mass_combat.md` | Extracted values |
| `designs/mass_combat/mass_battle_v30.md` | `designs/board_game/board_game_v30.md` §B.3/B.5 | BG battle resolution references mass battle |
| `designs/mass_combat/mass_battle_v30.md` | `compilation/v0.14/stage11_scale_transitions_deprecated.md` | Phase structure referenced in scale transitions |
| `designs/mass_combat/mass_battle_v30.md` | `skills/valoria-orchestrator/references/state_transfer_spec.md` | Phase timing drives state transfer rules |
| `references/params_combat.md` | `skills/valoria-combat-simulator/SKILL.md` | Sim loads params |
| `references/params_mass_combat.md` | `skills/valoria-simulator/SKILL.md` (Mode G1) | Sim loads params |

### DEBATE

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `designs/contest/social_contest_v30.md` | `references/params_contest.md` | Extracted values |
| `designs/contest/social_contest_v30.md` | `compilation/v0.14/stage9_social_deprecated.md` | Stale — needs rewrite |
| `references/params_contest.md` | `skills/valoria-simulator/SKILL.md` (Mode G2) | Sim loads params |

### BOARD GAME

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `designs/board_game/board_game_v30.md` | `references/params_board_game.md` | Extracted values |
| `designs/board_game/board_game_v30.md` | `references/params_factions.md` (BG column) | BG faction mechanics |
| `designs/board_game/board_game_v30.md` | `compilation/v0.14/stage_bg_board_game_mode_deprecated.md` | Stale — needs sync (ED-001 blocker) |
| `references/params_board_game.md` | `skills/valoria-simulator/SKILL.md` (Mode G5) | Sim loads params |

### FACTIONS

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `compilation/v0.14/stage6_factions_deprecated.md` | `references/params_factions.md` (TTRPG column) | Extracted values |
| `references/params_factions.md` | `skills/valoria-simulator/SKILL.md` (Mode G4) | Sim loads params |
| `references/params_factions.md` | `skills/valoria-mechanic-audit/SKILL.md` | Audit loads params |

### SOCIAL CONTEST

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `designs/contest/social_contest_v30.md` | `references/params_contest.md` | Values extracted; patches must sync |
| `designs/contest/social_contest_v30.md` | `compilation/v0.14/stage9_social_deprecated.md` | STALE — stage9 is empty; compile when stable |
| `references/params_contest.md` | `skills/valoria-simulator/SKILL.md` (Mode G2) | Sim loads params |
| `tests/sim_d_01_debate_stress_test.md` | `tests/coverage_matrix.md` | Findings logged |
| `tests/sim_d_02_debate_scenario_c.md` | `tests/coverage_matrix.md` | Findings logged |
| `tests/sim_d_02_debate_scenario_c.md` | `canon/editorial_ledger.yaml` | ED-051, ED-052 harvested |
| `tests/audit_debate_a_g.md` | `tests/coverage_matrix.md` | Audit findings logged |
| `tests/audit_debate_a_g.md` | `canon/editorial_ledger.yaml` | ED-053–059 harvested |
| `tests/sim_d_03_subsystem_k.md` | `tests/coverage_matrix.md` | G2+K findings logged |
| `tests/sim_d_03_subsystem_k.md` | `skills/valoria-orchestrator/references/state_transfer_spec.md` | K2-F-02: debate Zoom In gap |
| `tests/sim_d_04_gap_fill_stress.md` | `tests/coverage_matrix.md` | Gap-fill verification logged |
| `designs/contest/social_contest_v30.md` | `references/params_contest.md` | v1.6 — params_debate needs §§6.11-6.15 values extracted |
| `tests/audit_d02_sim_d05.md` | `tests/coverage_matrix.md` | Audit + stress test findings logged |
| `tests/audit_d02_sim_d05.md` | `canon/editorial_ledger.yaml` | ED-087-091 harvested |
| `gm_ref/debate_ref_card_v1.md` | `designs/contest/social_contest_v30.md` | Reference card must track v1.x |
| `compilation/v0.14/stage13_npcs_deprecated.md` | `designs/contest/social_contest_v30.md` | NPC Composure/attributes feed debate sim |

### SCALE TRANSITIONS / HYBRID

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `compilation/v0.14/stage11_scale_transitions_deprecated.md` | `references/params_scale_transitions.md` | Extracted values |
| `compilation/v0.14/stage11_scale_transitions_deprecated.md` | `skills/valoria-orchestrator/references/state_transfer_spec.md` | Phase structure drives transfer rules |
| `skills/valoria-orchestrator/references/state_transfer_spec.md` | `skills/valoria-simulator/SKILL.md` (Mode K2) | Transition tests load spec |
| `designs/hybrid/hybrid_gaps_v30.md` | `compilation/v0.14/stage11_scale_transitions_deprecated.md` | RESOLVED — gaps propagated to board_game_v30 Part Nine (PP-644) |ntegration |
| `designs/hybrid/hybrid_gaps_v30.md` | `designs/board_game/board_game_v30.md` §B.5 | Pending integration |

### GM REFERENCE / FLOWCHARTS

| `deprecated/designs/gm_ref_cp14/zoom_in_out_reference_card_deprecated.md` (NEW) | `skills/valoria-orchestrator/references/state_transfer_spec.md` | Summarises spec §1 for table use |
| `deprecated/designs/gm_ref_cp14/zoom_in_out_reference_card_deprecated.md` (NEW) | `designs/mass_combat/mass_battle_v30.md` §B.2/B.5 | Pulls unit conversion table |
| `designs/mass_combat/mass_battle_v30.md` | `deprecated/designs/gm_ref_cp14/zoom_in_out_reference_card_deprecated.md` | B.5 references this card |

| `tests/sim_hyb_01_templar_crossing.md` (NEW) | `tests/coverage_matrix.md` | Simulation run — log row added |
| `tests/sim_hyb_01_templar_crossing.md` (NEW) | `canon/patch_register_active.yaml` | PP-101 sourced from this sim |
| `tests/sim_hyb_01_templar_crossing.md` (NEW) | `canon/editorial_ledger.yaml` | ED-054 flagged from this sim |
| `designs/mass_combat/mass_battle_v30.md` | `skills/valoria-orchestrator/references/state_transfer_spec.md` | B.5 BG→TTRPG conversion now cross-refs B.2 |
| `designs/mass_combat/mass_battle_v30.md` | `references/params_mass_combat.md` | PP-101 applied; params_mass_combat notes open gaps PARAMS-GAP-04/05 |


| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| Any `designs/gm_ref_cp14/arcs/*.md` | `tests/coverage_matrix.md` | If simulated, log it |
| Any `designs/gm_ref_cp14/arcs/*.md` | `canon/editorial_ledger.yaml` | Harvest EDITORIAL flags |
| Any `designs/gm_ref_cp14/flowcharts/*.md` (NEW) | `designs/ttrpg/valoria_emergent_scenarios.md` | Cross-reference section |
| `designs/ttrpg/valoria_emergent_scenarios.md` | `designs/ttrpg/valoria_narrative_scenario_chains.md` | Sibling document — check for contradictions |

### SESSION / REGISTRY FILES

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `canon/patch_register_active.yaml` | `references/file_index.md` | Stale gap tracking |
| `canon/editorial_ledger.yaml` | `session_log_current.md` | editorial_decisions_pending |
| `session_log_current.md` | `session_log_archive.md` | On session close |

---



### BOARD GAME AUDIT 2026-04-02

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `references/params_board_game.md` | `designs/board_game/board_game_v30.md` | PP-115-122 gap fills |
| `references/params_board_game.md` | `canon/editorial_ledger.yaml` | ED-053-058 added |
| `references/params_board_game.md` | `canon/patch_register_active.yaml` | PP-112-122 added |
| `canon/editorial_ledger.yaml` | `session_log_current.md` | New editorial decisions pending |

## BROKEN DEPENDENCIES (auto-detected, log here)

| File | Broken Reference | Detected | Status |
|------|-----------------|----------|--------|
| `compilation/v0.14/stage3_thread_operations_deprecated.md` | References threadwork operations — empty/stale | 2026-04-02 | KNOWN — awaiting rewrite from threadwork_v25 |
| `compilation/v0.14/stage9_social_deprecated.md` | References debate system — empty/stale | 2026-04-02 | KNOWN — awaiting rewrite from debate_system_redesign_v1 Part 6 |
| `compilation/v0.14/stage_bg_board_game_mode_deprecated.md` | References BG rules — stale | 2026-04-02 | KNOWN — ED-001 blocker |

---

*This map is updated in every commit that touches any file listed here. It is never updated manually in isolation — always part of an atomic commit containing the files being linked.*

*`tools/broken_dependency_checker.py` scans this map and others for broken refs. Run it as part of Step C before every commit closes.*

## tests/sim_bg_01.md
- system: BG
- type: TEST
- depends_on: [references/params_board_game.md, designs/board_game/board_game_v30.md, references/params_factions.md]
- referenced_by: [tests/coverage_matrix.md, canon/editorial_ledger.yaml]

## tests/sim_bg_balance_01.md
- system: BG
- type: TEST
- depends_on: [references/params_board_game.md, compilation/v0.14/stage_bg_board_game_mode_deprecated.md]
- referenced_by: [tests/coverage_matrix.md, canon/patch_register_active.yaml]

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
- referenced_by: [tests/coverage_matrix.md, canon/editorial_ledger.yaml, canon/patch_register_active.yaml]

### PP-172 — Ranged Subtypes (2026-04-02)
Source: designs/combat/combat_v30.md §5, §6
Propagation targets:
- references/params_combat.md → DONE (this commit)
- designs/mass_combat/mass_battle_v30.md → DONE (PP-173, this commit)
- references/params_mass_combat.md → DONE (PP-173, this commit)
- designs/board_game/ → NOT REQUIRED (BG abstracts above weapon-type level — confirmed SIM-003)

### PP-173 — Mass Combat Ranged DR (2026-04-02)
Source: designs/mass_combat/mass_battle_v30.md §A.4 (DR table)
Propagation targets:
- references/params_mass_combat.md → DONE (this commit)
- designs/board_game/ → NOT REQUIRED (BG abstracts above weapon type)
- references/propagation_map.md: PP-172 entry updated: mass_battle → DONE

### PP-175 — Mass Combat Ranged DR Scaling (2026-04-02)
Source: designs/mass_combat/mass_battle_v30.md §A.4 (Ranged DR table)
Finding: SIM-005-F1
Propagation targets:
- references/params_mass_combat.md → DONE (this commit)
- Pending ED-096 user confirmation — values marked PROVISIONAL

### ED-098 — Cover declaration ruling (2026-04-02)
Pending propagation:
- designs/combat/combat_v30.md §5 Environmental Factors → add: "Cover must be declared in Phase 1. Game Master determines physical availability. No declaration = no DR benefit that round."

### PP-188 — Ranged Redesign (2026-04-02)
Source: designs/combat/combat_v30.md §5 (weapon table, reach rules, armour DR)
Resolved: ED-061
Propagation targets:
- references/params_combat.md → DONE (this commit)
- designs/mass_combat/mass_battle_v30.md → DONE (this commit)
- references/params_mass_combat.md → DONE (this commit)
- session_log_current.md → DONE (this commit)

### PP-232 — Docx Review Batch (2026-04-03)
Propagation complete. All affected params updated in same commit (22ee783).
- references/params_core.md → DONE
- references/params_combat.md → DONE
- references/params_contest.md → DONE
- references/params_threadwork.md → DONE
- references/params_mass_combat.md → DONE
- references/params_scale_transitions.md → DONE (this commit)
- references/glossary.md → DONE (this commit)
- canon/editorial_ledger.yaml → DONE (ED-127–135 added)
- canon/patch_register_active.yaml → DONE
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
- designs/mass_combat/mass_battle_v30.md → RESOLVED — PP-233 applied (unit formula: Pool = min(Size,Command)+Command). Confirmed in params_mass_combat.md header.
- compilation/v0.14/stage8_combat_deprecated.md → STALE — mass combat compilation predates PP-232/233. [PROP-STALE: stage8_combat.md]

## Propagation Pass — 2026-04-03 (ED batch from review session)
**EDs resolved and propagated:** ED-005, 006, 009, 014, 019, 022, 024, 029, 030, 034, 036, 056, 072, 080, 081, 083, 085, 086, 087, 094, 098, 109, 110, 121, 124, 130, 134
**Files updated:**
- references/params_contest.md — ED-009 (proceeding types), ED-014 (corroboration), ED-022 (violence/Unmask), ED-029 (Southernmost purpose rolls)
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
| references/sim_decision_protocols.md | sim_decision_protocols | skills/valoria-simulator/SKILL.md, tests/coverage_matrix.md | Protocol changes propagate to simulator skill and any test using actor protocol assignments |
| references/sim_decision_protocols.md | sim_decision_protocols | skills/valoria-simulator/SKILL.md, tests/coverage_matrix.md | Protocol library; changes propagate to all simulation test files using actor assignments |
| designs/combat/combat_v30.md (Feint §PP-291/293/294) | feint-partial-commit | references/params_combat.md | Feint versus roll + pool reduction; params must reflect current formula |
| designs/combat/combat_v30.md (Rescue §PP-290/292/295) | rescue-contested | references/params_combat.md, references/sim_decision_protocols.md | Rescue eligibility, contest, Momentum wound trigger |
| references/params_board_game.md (PP-296) | mandate-suppression | designs/board_game/board_game_v30.md | Mandate Ob cap 4 + coalition bonus; must propagate to BG design doc on next compile |
| designs/contest/social_contest_v30.md | contest-movement | references/params_contest.md | ED-295/296 open — CLASH/REINFORCE formula fixes pending; do not compile until resolved |
| references/params_combat.md (ED-200/201/202/203 rulings) | combat-rulings-2026-04-04 | designs/combat/combat_v30.md | Wound cap, carry-over, recovery, pool floor — resolved by design doc silence. Propagate to compilation on next pass. |
| references/params_contest.md (PP-401 REINFORCE floor) | reinforce-floor | designs/contest/social_contest_v30.md | REINFORCE max(0,...) floor. Propagate to design doc on next compilation. |

## ED-300 Propagation (2026-04-05)
| Source | Dependency key | Targets | Notes |
|--------|---------------|---------|-------|
| canon/editorial_ledger.yaml (ED-300) | domain-echo-scene-availability | designs/board_game/board_game_v30.md, references/params_board_game.md | Domain Echo reframe: availability declaration + escalation clock + primary/secondary yield. All-modes applicability. Propagate to BG design doc when ED-300 resolved. |

## ED-301 Propagation (2026-04-05)
| Source | Dependency key | Targets | Notes |
|--------|---------------|---------|-------|
| canon/editorial_ledger.yaml (ED-301) | ts-coherence-orthogonal | designs/ttrpg/threadwork_v30.md, references/params_threadwork.md, references/params_core.md | TS and Coherence are orthogonal axes. Coherence loss = expansion beyond human rendering frame, not degradation. Knots = relational bindings. Coherence 0 = rendering frame incompatibility, not incapacitation. Propagate to threadwork design doc and params when resolved. |


---

## Calamity Radiation System (added 2026-04-06)

| Source | Target | Relationship |
|--------|--------|-------------|
| designs/setting/calamity_radiation_v30.md | designs/ttrpg/threadwork_v30.md §5.3 | Geographic graduation of RS thresholds — DONE 2026-04-06 |
| designs/setting/calamity_radiation_v30.md | designs/ttrpg/threadwork_v30.md §6 | Gap-severity classification cross-ref — DONE 2026-04-06 |
| designs/setting/calamity_radiation_v30.md | designs/setting/geography_v30.md | Supersedes Calamity Bleed Gradient section — DONE |
| designs/setting/geography_v30.md | designs/setting/calamity_radiation_v30.md | Node distance map derived from territory adjacency — DONE |

## PP-478 — RM Founding Mechanic Propagation
| Source | Depends On | Change Required |
|--------|-----------|-----------------|
| params_board_game.md §RM Founding | PW track definition | params_board_game.md ✓ applied |
| victory_architecture_v1.md §3.5 | RM mode availability | victory_architecture_v1.md ✓ override appended |
| victory_architecture_v1.md §4 | RM co-victory availability | ✓ override appended |
| victory_architecture_v1.md §8 | RM Emergence → replaced | ✓ override appended |
| params_factions.md | RM faction status | ✓ applied |
| valoria_bg_v05_simulation_and_patches.md | "5 players only" note, §Balance | STALE NOTE — see PP-478 |
| tests/coverage_matrix.md | RM simulation entries | updated |


## 2026-04-08 Propagation Status

### PP-493–504 (Territory + Church + Editorial batch)
- victory_architecture_v1.md: T-numbers remapped ✓
- params_board_game.md: Crown TCV, Church Seizure, Torben, PI thresholds, TC cap, Co-Movement serial, Political Vacuum ✓
- params_factions.md: RM TTRPG Founding Gate ✓
- params_threadwork.md: Inert Knowledge, Dissonant rates ✓
- canonical_sources.yaml: social_debate→v2, clocks→registry ✓
- designs/systems/clock_registry_v30.md: created ✓
- designs/npcs/npc_roster.md: created ✓
- worldbuilding_integration_v3.md: old territory names fixed ✓
- valoria_bg_v04.md: SUPERSEDED — not updated (stale Hardar ref acceptable in deprecated file)

### NPC Naming Propagation
- Hardar Veldensohn → Doux Alexios Laskaris: params_board_game ✓, npc_roster ✓, session_log ✓
- bg_v04 retains old name (SUPERSEDED file — no action)
- Severin Almud → Gerik Strand: npc_roster ✓ (Severin did not appear in any other active file)

## 2026-04-11 Session — New Propagation Entries

### canon/03_canonical_timeline.md
- -> designs/npcs/npc_character_analyses_existing.md (Almud TS 0, Baralta Crown ambition, Vaynard southern heritage, Lenneth revivalist)
- -> designs/npcs/ruler_diamond_foil_analysis.md (all pairings)
- -> designs/npcs/ruler_diamond_extended_foils.md (all perspectives)
- -> gm_ref/arcs_01_04_nongreedy.md (Arc 1 Almud reframing)
- -> designs/gm_ref_cp14/arcs/arcs_09_11_elske_baralta.md (Arc 9 consecration crisis)
- -> designs/mechanics/baralta_crown_claim_mechanic.md (deed-monarchy -> Crown Succession Contest)
- -> designs/npcs/lenneth_threadwork_design.md (Lenneth characterisation -> TS development)

### designs/npcs/lenneth_threadwork_design.md
- -> references/params_threadwork.md (Lenneth TS 8 supersedes TS 72)
- -> designs/mechanics/baralta_crown_claim_mechanic.md (Cultural Revival Track interacts with consecration crisis timing)
- -> designs/npcs/npc_character_analyses_existing.md (Lenneth section)
- -> designs/npcs/ruler_diamond_foil_analysis.md (Lenneth-Baralta confrontation)
- -> gm_ref/arcs_01_04_nongreedy.md (Arc 1 RM ambient track affected by Cultural Revival Track)
- -> compilation/v0.14/stage4_southernmost_deprecated.md (Southernmost Awareness — Crown gains access via Lenneth at TS 30)

### designs/mechanics/baralta_crown_claim_mechanic.md
- -> references/params_board_game.md (Crown Succession Contest, Stake Claim DA — NOT YET INTEGRATED into params)
- -> designs/npcs/ed_403_406_407_resolutions.md (Ehrenwall assessment, consecration conditional)
- -> designs/npcs/npc_character_analyses_existing.md (Baralta Crown ambition)
- -> designs/worldbuilding/worldbuilding_integration_v3.md (Motion of No Confidence — deed-monarchy context)

### designs/npcs/npc_roster_caste_annotations.md
- -> designs/npcs/npc_roster.md (companion document — all 13 NPCs annotated)
- -> canon/03_canonical_timeline.md (caste system definition)
- -> designs/setting/geography_v30.md (TS gradient by territory)

### Stale Propagation Note
- references/params_board_game.md does NOT yet contain the Crown Succession Contest, Stake Claim DA, or Consecration Crisis mechanics. Integration needed next session.
- references/params_threadwork.md updated (Lenneth TS 72 -> 8) but does NOT yet contain Cultural Revival Track or Lenneth breakthrough condition. These are in the design doc only.

## NPC Behavior System (designs/systems/npc_behavior_v30.md) — added 2026-04-13

| This file references | Direction | What |
|---|---|---|
| stage6_factions.md | reads | Ethical Frameworks, Institutional Tendency, named NPC stubs |
| social_contest_system_v2.md | extends | Resonant Style targeting, Appraise revelation |
| params_factions.md | reads + future write | Faction stats, Ob modifiers; will receive Stance Triangles |
| params_board_game.md | reads + future write | BG mechanics, NPC priority trees |
| params_core.md | reads | Certainty, Coherence, attributes |
| params_contest.md | extends | Resonant Style targeting to be extracted |
| threadwork_redesign_v25.md | reads | Knots, TS thresholds, epistemic seduction |
| edeyja_npc.md | reads | Edeyja Stance Triangle, Arc profiles |
| character_histories_lifepath.md | reads | Knot generation, starting Beliefs |
| canon/00_philosophical_foundations.md | governed by | P-04, P-08, P-10, P-12 |
| victory_architecture_v1.md | reads | Victory conditions, NPC AI consent |

## Arc Register v8 — Critical Cross-References (2026-04-13, PP-575)

| From | To | Nature |
|---|---|---|
| TE-15 | ARC-S34 | Edeyja Coherence <= 5 at TE-15: Dissolution -> Rendering Crisis regardless of outcome |
| TE-12 | ARC-S15, ARC-T04 | Varfell gate control during S15 cracking phase blocks Ceiral Ritual expedition |
| ARC-S44 | ARC-T17 | Both target AER via Schoenland; highest-roll success takes priority same season |
| ARC-S56 | ARC-T26 | T26 resolves first (Leadership Deviation check); S56 resolves under result |
| TE-09 | NPC-ARC-JAR | Jarnstal threat-assessment governs autonomous deployment trigger |
| ARC-S40 | ARC-P04 | Documentary Axis 2 before Axis 9: direction of interaction to specify (ED-402) |
| ARC-S47 | ARC-T16 | Simultaneous in same RM-presence/missionary territories: cultural contest primary |
| ARC-P09 | ARC-S52 | Crown fiscal distress weakens Charter offer; shifts Feldhaus alignment calculation |

## FIELDWORK (designs/fieldwork/fieldwork_v30.md + subsystem files) — added 2026-04-13

| Changed File | Propagates To | Reason | Status |
|-------------|--------------|--------|--------|
| `designs/fieldwork/fieldwork_v30.md` | `designs/fieldwork/fieldwork_v30.md` | `designs/fieldwork/fieldwork_v30.md` | `designs/fieldwork/fieldwork_v30.md` | `designs/fieldwork/fieldwork_v30.md` | `designs/fieldwork/fieldwork_v30.md` | `designs/fieldwork/fieldwork_v30.md` | `designs/fieldwork/fieldwork_v30.md` | `designs/ttrpg/threadwork_v30.md` | Thread-Read as perceptive Leap (§4.5); co-movement protocol; per-op cap ruling (TW-05) | PENDING — threadwork params notes open per ED-NEW-15 |
| `designs/fieldwork/fieldwork_v30.md` | `designs/contest/social_contest_v30.md` | Contest Escalation boundary (§5.7); Combined Findings (+1D per Finding in Contest, max +2D) (§2.3 / F-TRANS-11) | PENDING |
| `designs/fieldwork/fieldwork_v30.md` | `designs/combat/combat_v30.md` | Fieldwork → Combat handoff: Exposure → ambusher advantage (§2.3 / F-TRANS-01); Combat Exposure codified (quiet +1, conspicuous +2, public +3) (F-TRANS-09) | PENDING |
| `designs/fieldwork/fieldwork_v30.md` | `designs/setting/geography_v30.md` | POI catalog per territory (ED-NEW-01); conditional POI gates by RS band | PENDING (blocked: ED-NEW-01 P2) |
| `designs/fieldwork/fieldwork_v30.md` | `designs/setting/calamity_radiation_v30.md` | Proximity Rating governs Survey Ob (§8.1); Calamity zone Exposure thresholds | PENDING |
| `designs/fieldwork/fieldwork_v30.md` | `designs/mass_combat/mass_battle_v30.md` | Mass battle suspends fieldwork (§2.3 / F-TRANS-06); Post-battle investigation = 1 fieldwork scene (F-TRANS-12) | PENDING |
| `designs/fieldwork/fieldwork_v30.md` | `references/params_threadwork.md` | POP Coherence −1 additional subject to per-op cap (TW-05 / ED-NEW-15) — currently ambiguous in params | PENDING (ED-NEW-15 P2) |
| `references/params_fieldwork.md` | `skills/valoria-simulator/SKILL.md` | Sim loads params (Mode G-FW — to be created) | PENDING |
| `designs/fieldwork/fieldwork_godot.md` | `jordanelias/valoria-game` repo | §10 Validation Findings G10-F01 through G10-F07 — implementation gaps logged | REFERENCE ONLY |

### Fieldwork subsystem file cross-references

| File | Reads From | Notes |
|------|-----------|-------|
| `designs/fieldwork/fieldwork_exploration.md` | `designs/fieldwork/fieldwork_v30.md` §1, §2 | POI depth axis; pool construction |
| `designs/fieldwork/fieldwork_investigation.md` | `designs/ttrpg/threadwork_v30.md` §3.2 | Thread-Read co-movement table |
| `designs/fieldwork/fieldwork_investigation.md` | `designs/contest/social_contest_v30.md` | Contested Investigation escalation |
| `designs/fieldwork/fieldwork_socializing.md` | `designs/contest/social_contest_v30.md` | Contest escalation boundary (§5.7) |
| `designs/fieldwork/fieldwork_socializing.md` | `designs/ttrpg/threadwork_v30.md` | Threadcut being social fieldwork (§2.8) |
| `designs/fieldwork/fieldwork_exposure.md` | `designs/systems/clock_registry_v30.md` | Cover, Exposure Track, Church Attention Pool |
| `designs/fieldwork/fieldwork_bg_v30.md` | `references/params_board_game.md` | Survey Ob table; existing BG action Obs |
| `designs/fieldwork/fieldwork_hybrid_v30.md` | `designs/hybrid/scale_transitions_v30.md` | Fieldwork Offset procedure; §3.9 handoff rule |
| `designs/fieldwork/fieldwork_godot.md` | `jordanelias/valoria-game` | Validated 2026-04-13; G10-F01–F07 |

## Comparative Audit Patches — 2026-04-13 (PP-630–634)

| Changed File | Propagates To | Reason |
|-------------|--------------|--------|
| `designs/combat/combat_v30.md` | `designs/fieldwork/fieldwork_investigation.md` | §11.5 fieldwork handoff cross-reference (F-TRANS-01/09) added |
| `designs/contest/social_contest_v30.md` | `designs/fieldwork/fieldwork_investigation.md` | §9.1 Combined Findings citation cross-reference added |
| `designs/ttrpg/threadwork_v30.md` | `designs/fieldwork/fieldwork_investigation.md` | §2.3 Thread-Read-as-fieldwork cross-reference added |
| `references/params_core.md` | `designs/combat/combat_v30.md`, `designs/contest/social_contest_v30.md`, `designs/fieldwork/fieldwork_v30.md` | Pool floor 1D named rule — all pool-using systems now have canonical anchor |
| `canon/editorial_ledger.yaml` | `designs/systems/npc_behavior_v30.md` | ED-510 (NPC Recruitment PROVISIONAL), ED-511 (Hooks), ED-512 (surrender), ED-513 (fail-forward), ED-514 (social initiative) |

## PP-641–642 Propagation (2026-04-13)

### PP-641 — Opposing Operations → threadwork design doc
| Source | Target | Status |
|---|---|---|

### PP-642 — NPC Recruitment
| Source | Target | Notes |
|---|---|---|
| `designs/systems/npc_behavior_v30.md` §9.5 | `references/params_contest.md` | Findings citation extracted ✓ |
| `designs/systems/npc_behavior_v30.md` §9.5 | `references/params_combat.md` | Surrender/disengage extracted ✓ |
| `designs/systems/npc_behavior_v30.md` §9.5 | `designs/fieldwork/fieldwork_socializing.md` | Hook acquisition §5.5b — DONE (PP-643) |
| `designs/systems/npc_behavior_v30.md` §9.5 | `designs/systems/clock_registry_v30.md` | Hook tracking: roster-level tag, not a separate clock — no clock_registry change |
| `designs/systems/npc_behavior_v30.md` §9.5 | `references/params_factions.md` | Mandate −1 on successful recruitment — DONE (PP-643) |


## GM Reference Arcs — Batches 07–08 Consolidated (arcs_46_55_consolidated.md) — 2026-04-13

| Changed File | Propagates To | Reason | Status |
|-------------|--------------|--------|--------|
| `gm_ref/arcs_46_55_consolidated.md` | `gm_ref/arcs_46_55_consolidated.md` | `gm_ref/arcs_46_55_consolidated.md` | `references/params_factions.md` | Cites PP-402, PP-403, Domain Action Ob formula, ethical framework modifiers | REFERENCE |
| `gm_ref/arcs_46_55_consolidated.md` | `references/params_threadwork.md` | Cites PP-255, Leap table, Contact Duration, Coherence | REFERENCE |
| `gm_ref/arcs_46_55_consolidated.md` | `references/params_board_game.md` | Cites PI track, Coup Counter, Torben/Elske Loyalty, PP-563 VTM-TC | REFERENCE |
| `gm_ref/arcs_46_55_consolidated.md` | `canon/02_canon_constraints.md` | Critique applied P-01/P-03/P-07/P-08/P-15; arc 51 P-15 correction | REFERENCE |
| `gm_ref/arcs_46_55_consolidated.md` | `designs/systems/clock_registry_v30.md` | Cites PI, Coup Counter, WC, VTM, Torben/Elske tracks | REFERENCE |

### Unverified items — U-01 through U-11 flagged inline in consolidated doc
Require reads of: params_board_game.md §Coup Counter, threadwork_redesign_v25.md, victory_architecture_v1.md §6, stage6_factions.md §Guilds/Varfell/faction leadership.


## GM Reference Arcs — Fully Resolved (arcs_46_55_resolved.md) — 2026-04-13

| Changed File | Propagates To | Reason | Status |
|-------------|--------------|--------|--------|
| `gm_ref/arcs_46_55_resolved.md` | `gm_ref/arcs_46_55_resolved.md` | `references/params_factions.md` | Cites PP-402, PP-403, Domain Action Ob, ethical framework, Guild Leverage | REFERENCE |
| `gm_ref/arcs_46_55_resolved.md` | `references/params_threadwork.md` | Cites PP-255, RS thresholds, Coherence §3.2, Contact Duration, TS perception table | REFERENCE |
| `gm_ref/arcs_46_55_resolved.md` | `references/params_board_game.md` | Cites PI track, Coup Counter, Torben/Elske Loyalty, PP-563 VTM-TC, WC effects | REFERENCE |
| `gm_ref/arcs_46_55_resolved.md` | `canon/02_canon_constraints.md` | P-01/P-03/P-07/P-08/P-15 applied; all canon-compliant | REFERENCE |
| `gm_ref/arcs_46_55_resolved.md` | `compilation/v0.14/stage6_factions_deprecated.md` | Domain Action pool formula, Guild Favour trigger, Coup Counter triggers, Varfell Private Collection | REFERENCE |

### Design gaps surfaced (require Jordan decision)
DESIGN GAP 1: PI per-action contribution amounts — not specified in any source. Needs table in params_board_game.md.
DESIGN GAP 2: Guild Favour restoration mechanic — no upward movement source documented. Needs design decision.

## PP-643–657 Peninsular Strain System (2026-04-14)
| PP | Source | Target | Status |
|---|---|---|---|
| PP-643 | peninsular_strain_v1.md §1 | victory_v30.md §1 TCV table | DONE |
| PP-643 | peninsular_strain_v1.md §1 | params_board_game.md Starting TCV | DONE |
| PP-644 | peninsular_strain_v1.md §6 | victory_v30.md §0 | DONE |
| PP-644 | peninsular_strain_v1.md §6 | params_board_game.md Victory summary | DONE |
| PP-645 | peninsular_strain_v1.md §2 | params_board_game.md Accord table | DONE |
| PP-646 | peninsular_strain_v1.md §4 | params_board_game.md Strain thresholds | DONE |
| PP-647 | peninsular_strain_v1.md §3 | params_board_game.md battle consequences | DONE |
| PP-647 | peninsular_strain_v1.md §3 | mass_battle_v30.md faction consequences | DONE |
| PP-648 | peninsular_strain_v1.md §5.2 | victory_v30.md §3.2 Church Seizure | DONE |
| PP-649 | peninsular_strain_v1.md §5.3 | params_board_game.md Ob reference | DONE |
| PP-650 | peninsular_strain_v1.md §5.4 | params_board_game.md Ob reference | DONE |
| PP-651 | peninsular_strain_v1.md | victory_v30.md §3.3 | DONE |
| PP-652 | peninsular_strain_v1.md §2.2 | params_board_game.md Starting PT | DONE (provisional) |
| PP-653 | peninsular_strain_v1.md §2.6 | params_board_game.md Ob reference | DONE |
| PP-654 | peninsular_strain_v1.md §6.3 | victory_v30.md §0.1 | DONE |
| PP-654 | peninsular_strain_v1.md §6.3 | params_board_game.md co-victory | DONE |
| PP-655 | peninsular_strain_v1.md §5 | npc_behavior_v30.md §8 | DONE |
| PP-656 | peninsular_strain_v1.md | scale_transitions_v30.md §5.5 | DONE |
| PP-657 | peninsular_strain_v1.md §7 | params_board_game.md Accounting 4c-4e | DONE |

## Military Layer & TC Redesign (2026-04-14)
| Source | Target | Status |
|---|---|---|
| military_layer_v30.md §1 | mass_battle_v30.md §B.2 unit types | Cross-ref (consistent) |
| military_layer_v30.md §3 | params_board_game.md §TC Generation | PENDING |
| tc_political_redesign_v30.md §1 | territory cards (SW attribute) | PENDING |
| tc_political_redesign_v30.md §2 | victory_v30.md TC freeze refs | PENDING |
| tc_political_redesign_v30.md §3 | params_board_game.md political pool | PENDING |
| peninsular_strain_v1.md §7b | faction_layer_v30.md §2 Occupation | Harmonization added |
| peninsular_strain_v1.md §7c | tc_political_redesign_v30.md §2 TC 0-100 | Harmonization added |
## PP-658 Faction Layer ↔ Peninsular Strain Integration (2026-04-14)
| PP | Source | Target | Status |
|---|---|---|---|
| PP-658 | peninsular_strain_v1.md §2 | faction_layer_v30.md §2.3 (Occupation Accord) | DONE |
| PP-658 | peninsular_strain_v1.md §6.1 | faction_layer_v30.md §3.4 (Treaty hegemony types) | DONE |
| PP-658 | peninsular_strain_v1.md §4 | faction_layer_v30.md §5.6b (Parliament Strain) | DONE |
| PP-658 | peninsular_strain_v1.md §7 | faction_layer_v30.md §7 (Accounting sequence) | DONE |
| PP-658 | peninsular_strain_v1.md §2.3 | faction_layer_v30.md §1.3 (Consolidation Accord) | DONE |
## PP-659 Military Layer Integration + Register Split (2026-04-15)
| PP | Source | Target | Status |
|---|---|---|---|
| PP-659 | peninsular_strain_v1.md §3 | military_layer_v30.md §2.2b | DONE |
| PP-659 | patch_register_active.yaml | patch_register_archive.yaml (split) | DONE |
