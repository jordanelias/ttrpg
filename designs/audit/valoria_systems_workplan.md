# VALORIA — Comprehensive Systems Workplan
## File Index, Skeleton/Infill Strategy, Audit Structure, Interdependency Matrix
## Date: 2026-04-15
## Scope: All 18 systems across both repos (jordanelias/ttrpg, jordanelias/valoria-game)

---

# SYSTEM TAXONOMY

18 systems organized by scale. Each system entry contains: (A) skeleton/infill strategy, (B) file index, (C) audit structure, (D) interdependencies.

| ID | System | Scale | Primary Doc |
|----|--------|-------|------------|
| S01 | Metaphysics & Canon | Foundation | canon/00_philosophical_foundations.md |
| S02 | Core Engine | Foundation | references/params_core.md |
| S03 | Geography & Territory | Peninsula | designs/setting/geography_v30.md |
| S04 | Clocks & Tracks | Peninsula | designs/systems/clock_registry_v30.md |
| S05 | Calamity Radiation | Peninsula | designs/setting/calamity_radiation_v30.md |
| S06 | Faction Layer | Faction | designs/board_game/faction_layer_v30.md |
| S07 | Victory & Peninsular Strain | Faction | designs/board_game/victory_v30.md + peninsular_strain_v1.md |
| S08 | TC Political Redesign | Faction | designs/board_game/tc_political_redesign_v30.md |
| S09 | Military Layer | Faction | designs/board_game/military_layer_v30.md |
| S10 | NPC Behavior | Individual/Faction | designs/systems/npc_behavior_v30.md |
| S11 | Combat (Personal) | Individual | designs/combat/combat_v30.md |
| S12 | Social Contests | Individual | designs/contest/social_contest_v30.md |
| S13 | Thread Operations | Individual | designs/ttrpg/threadwork_v30.md |
| S14 | Fieldwork | Individual | designs/fieldwork/fieldwork_v30.md |
| S15 | Mass Combat | Territory/Faction | designs/mass_combat/mass_battle_v30.md |
| S16 | Emergent Arcs | Cross-scale | references/arc_register.md |
| S17 | Scale Transitions & Hybrid | Cross-scale | designs/hybrid/scale_transitions_v30.md |
| S18 | Character & Histories | Individual | designs/characters/character_histories_v30.md |

---

# S01 — METAPHYSICS & CANON

## A. Skeleton/Infill Strategy

**Skeleton:** canon/00_philosophical_foundations_rules.md (7,772 chars — enforcement rules). Load for every canon check, mechanic proposal, and audit.

**Infill:** canon/00_philosophical_foundations.md (full prose, ~17,554 tokens). Load only for deep editorial work, philosophical derivations, or metaphysical disputes.

**Amendment:** canon/01_foundations_amendment_self_rendering.md — three-layer being-persistence (personal memory, cultural practice, Thread substrate). Load when working on Coherence, Knots, Community Weaving, or RM.

**Constraints:** canon/02_canon_constraints.md (P-01 through P-15). Load for any mechanic audit.

**When to hold in context:** Always load rules + constraints for any design session. Load full prose only when the question is "does this mechanic violate the metaphysics?"

## B. File Index

| File | Repo | Role | Tokens (est.) |
|------|------|------|---------------|
| canon/00_philosophical_foundations.md | ttrpg | Full prose foundations | ~17,500 |
| canon/00_philosophical_foundations_rules.md | ttrpg | Enforcement rules (condensed) | ~2,000 |
| canon/01_foundations_amendment_self_rendering.md | ttrpg | Amendment: three-layer being | ~3,000 |
| canon/02_canon_constraints.md | ttrpg | P-01 through P-15 constraint table | ~1,800 |
| canon/03_canonical_timeline.md | ttrpg | Historical timeline | ~2,000 |
| designs/ttrpg/threadwork_philosophical_reference_v30.md | ttrpg | Philosophical underpinnings of threadwork | ~5,000 |
| designs/ttrpg/threadwork_philosophical_reference_v30_infill.md | ttrpg | Extended philosophical discussion | ~8,000 |

## C. Audit Structure

**Working well:** P-01 (inseparability) is load-bearing and correctly constrains all Thread mechanics. Three emergence modes (un-rendering, over-rendering, displacement) are mechanically distinguished. Ein Sof as positive being (not void) consistently prevents "corruption/evil" framing.

**Not working well:** P-03 (consciousness-performed rendering) has no videogame computational analogue. The philosophical document is ~17K tokens — too large for routine loading.

**Outstanding:** Videogame rendering model. "Metaphysical Stability" naming (ED-303 flagged but unresolved — Jordan considered "World Coherence" but no decision).

**Recommendations:** (1) Write a 500-word videogame rendering model deriving from P-03. (2) Resolve MS naming.

## D. Interdependencies

| Paired With | Interaction | Type |
|-------------|------------|------|
| S13 Thread Ops | P-01 constrains all Thread mechanics | Constraint |
| S05 Calamity | P-02/P-04 constrains monster/entity framing | Constraint |
| S14 Fieldwork | P-05 constrains emergence mode classification | Constraint |
| S10 NPC Behavior | P-08 constrains epistemological barrier (Church) | Constraint |
| S18 Characters | P-15 constrains Coherence/Knot/identity mechanics | Constraint |

---

# S02 — CORE ENGINE

## A. Skeleton/Infill Strategy

**Skeleton:** references/params_core.md (12,303 chars). Contains all formulas, dice rules, attribute definitions, derived values. Load for any mechanic work.

**Infill:** None — params_core is already the densest reference. The compilation stage1 is deprecated.

**When to hold:** Always load params_core for any session touching mechanics.

## B. File Index

| File | Repo | Role |
|------|------|------|
| references/params_core.md | ttrpg | Canonical: dice, attributes, pools, Ob, derived values |
| references/params_core_history.md | ttrpg | Change log |
| compilation/v0.14/stage1_core_engine_deprecated.md | ttrpg | Historical (deprecated) |
| systems/engine/CoreEngine.gd | valoria-game | Godot dice engine |
| systems/engine/CoreResolver.gd | valoria-game | Roll resolution |
| systems/engine/RollContext.gd | valoria-game | Roll context data |
| systems/engine/RollResult.gd | valoria-game | Roll result data |
| references/d10_success_probabilities.json | ttrpg | Probability tables |
| references/D10_INTEGRATION_GUIDE.md | ttrpg | d10 system guide |
| skills/valoria-dice-model/valoria_dice.py | ttrpg | Python dice simulator |

## C. Audit Structure

**Working well:** Universal pool formula (Attr×2)+H+3 is rigorously consistent. Universal Ob formula floor(stat/2)+1 applied everywhere. d10 system with TN 7 is well-calibrated (0.4 expected net per die).

**Not working well:** Nothing — this is the most stable system.

**Outstanding:** None.

**Recommendations:** Consider writing a one-page "Core Engine Quick Reference" for new sessions.

## D. Interdependencies

Every system depends on S02. Key interactions:

| Paired With | Interaction |
|-------------|------------|
| S11 Combat | Pool = (Agi×2)+H+3; Wound Threshold = End+6 |
| S12 Contest | Pool = (Attr×2)+H+3; Composure = Cha+6 |
| S13 Thread | Pool = (Spi×2)+H+TPS (exception to +3) |
| S14 Fieldwork | All actions use universal pool |
| S15 Mass Combat | Unit pool = min(S,C)+C (structural exception) |
| S18 Characters | 10 attributes, 31-point creation |

---

# S03 — GEOGRAPHY & TERRITORY

## A. Skeleton/Infill Strategy

**Skeleton:** designs/setting/geography_v30.md (5,388 chars). Territory map, adjacency graph, terrain, starting control. Always load for any territory-referencing work.

**Infill:** designs/setting/geography_v30_infill.md. Extended geographic descriptions, cultural details.

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/setting/geography_v30.md | ttrpg | Canonical: 17 territories, adjacency, starting control |
| designs/setting/geography_v30_infill.md | ttrpg | Extended descriptions |
| designs/setting/adjacency_map.jsx | ttrpg | Interactive map component |
| designs/board_game/valoria_map_v2.svg | ttrpg | Visual map |
| scenes/containers/board/BoardContainer.gd | valoria-game | Godot territory map |
| scenes/containers/board/BoardContainer.tscn | valoria-game | Godot board scene |

## C. Audit Structure

**Working well:** 17-territory map is canonical and stable. Two invasion corridors (Lowenskyst, Spartfell). Two Southernmost gates. Schoenland as naval gatekeeper.

**Not working well:** Some documents reference 15 territories (excluding Schoenland and Askeheim from playable count). Inconsistent.

**Outstanding:** J-7 (0–4 territory scale). Territory starting values for Accord, Prosperity.

**Recommendations:** Resolve J-7 and propagate. Create a single canonical starting-values table.

## D. Interdependencies

| Paired With | Interaction |
|-------------|------------|
| S05 Calamity | Node distance from T15 determines radiation reach |
| S04 Clocks | Territory-level tracks (Accord, Piety, Prosperity, Fort) |
| S07 Victory | Territory Value, Accord ≥ 2 for count, universal sovereignty |
| S08 TC Reform | Spiritual Weight per territory gates CI flow |
| S09 Military | Fort Level modifies battle Ob |

---

# S04 — CLOCKS & TRACKS

## A. Skeleton/Infill Strategy

**Skeleton:** designs/systems/clock_registry_v30.md (5,346 chars — **STALE, needs update**). Single registry of all clocks, tracks, counters.

**Infill:** clock_registry_v30_infill.md. Extended descriptions.

**Critical:** This file is the authority for "what tracks exist." Currently stale (see staleness report). Must be updated before use.

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/systems/clock_registry_v30.md | ttrpg | Canonical registry (STALE) |
| designs/systems/clock_registry_v30_infill.md | ttrpg | Extended descriptions |
| systems/trackers/Tracker.gd | valoria-game | Godot tracker base |
| systems/trackers/TrackerRegistry.gd | valoria-game | Godot tracker registry |
| systems/trackers/TrackerThreshold.gd | valoria-game | Threshold events |
| systems/engine/TrackerBinding.gd | valoria-game | Tracker-to-consequence binding |

## C. Audit Structure

**Working well:** Registry concept is correct — single source of truth for all tracks.

**Not working well:** **23 stale items** (see clock_registry_staleness_report.md). PI struck but still listed. TC ceiling wrong. Disposition range wrong. Multiple stale source references.

**Outstanding:** Full update from peninsular_strain_v1, tc_political_redesign_v30, PP-632, PP-611.

**Recommendations:** Priority 1 update. Block all other work until clock_registry is current.

## D. Interdependencies

All systems feed into or read from clocks. This is the central nervous system.

| Paired With | Interaction |
|-------------|------------|
| S07 Victory | MS, CI, IP, Political Stability determine victory/loss |
| S05 Calamity | MS thresholds trigger radiation expansion |
| S13 Thread | Thread ops modify MS; Coherence tracked here |
| S15 Mass Combat | Battles modify MS, IP, Political Stability |
| S06 Faction | Faction stats (Mandate etc.) tracked here |

---

# S05 — CALAMITY RADIATION

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/setting/calamity_radiation_v30.md | ttrpg | Canonical: MS band × distance radiation |
| designs/setting/calamity_radiation_v30_infill.md | ttrpg | Extended effects |
| designs/setting/southernmost_v30.md | ttrpg | Southernmost/Askeheim design |
| designs/setting/southernmost_v30_infill.md | ttrpg | Extended Southernmost |
| references/params_southernmost.md | ttrpg | Southernmost params |

## C. Audit Structure

**Working well:** Dynamic radiation expanding with MS drop is narratively powerful and mechanically simple. Fixed node-distance values provide geographic susceptibility.

**Not working well:** The Southernmost itself lacks detailed gameplay content (POIs, encounters, progression).

**Outstanding:** ED-507 (POI catalog — deferred). Threadcut being encounter tables.

---

# S06 — FACTION LAYER

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/board_game/faction_layer_v30.md | ttrpg | Stability, occupation, treaties, Accounting |
| designs/board_game/faction_layer_v30_infill.md | ttrpg | Extended faction mechanics |
| designs/board_game/board_game_v30.md | ttrpg | Full BG spec (54K chars) |
| designs/board_game/board_game_v30_infill.md | ttrpg | BG extended |
| references/params_board_game.md | ttrpg | BG params (122K chars — largest file) |
| references/params_factions.md | ttrpg | Faction params |
| references/params_factions_ttrpg.md | ttrpg | TTRPG faction params |
| systems/faction/FactionTurnSystem.gd | valoria-game | Godot faction turn |
| systems/faction/ValoriaFactionAI.gd | valoria-game | Godot faction AI |
| systems/registries/FactionRegistry.gd | valoria-game | Godot faction data |
| resources/data_types/FactionData.gd | valoria-game | Faction data type |
| resources/data_types/ActionCardData.gd | valoria-game | Card system data |

## C. Audit Structure

**Working well:** PP-403 repeal is clean. Stability triggers are well-defined. Card system with cooldowns adds tactical depth.

**Not working well:** params_board_game.md at 122K chars is unwieldy. RM has no mechanical actor.

**Outstanding:** RM Domain Action capability. Starting faction stat values need confirmation.

---

# S07 — VICTORY & PENINSULAR STRAIN

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/board_game/victory_v30.md | ttrpg | Victory architecture |
| designs/board_game/victory_v30_infill.md | ttrpg | Extended victory |
| designs/board_game/peninsular_strain_v1.md | ttrpg | Accord, Political Stability, universal victory, acquisition toolkits |
| designs/board_game/varfell_path_b_v30.md | ttrpg | Varfell victory paths |

## C. Audit Structure

**Working well:** Universal victory condition (all 15, Accord ≥ 2, Political Stability ≤ 6, 2 consecutive) is elegant. 5 acquisition toolkits give strategic asymmetry.

**Not working well:** peninsular_strain_v1 is PROPOSAL status but effectively canonical — should be merged into victory_v30. Hafenmark Parliamentary alternate struck but replacement not fully specified.

**Outstanding:** ED-538 (compound simulation). ED-539 (TC reform compound). J-6 (Seizure Ob). Starting PT values (provisional).

---

# S08 — TC POLITICAL REDESIGN

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/board_game/tc_political_redesign_v30.md | ttrpg | CI milestones, political legitimacy, conditional passive |
| designs/systems/tc_political_redesign_v30.md | ttrpg | Duplicate path — check which is canonical |

## C. Audit Structure

**Working well:** CI milestones at 40/55/65/80/100 create meaningful political costs. Political legitimacy bonus (floor(CI/20)) integrates Church power into all institutional contexts.

**Not working well:** Status still PROPOSAL. Needs formal acceptance and merge into parent documents.

**Outstanding:** J-8 (confirm milestones). J-9 (confirm Spiritual Weight). Simulation of compound effects.

---

# S09 — MILITARY LAYER

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/board_game/military_layer_v30.md | ttrpg | Unit bridge, TC revision |
| references/params_mass_combat.md | ttrpg | Mass combat params |

---

# S10 — NPC BEHAVIOR

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/systems/npc_behavior_v30.md | ttrpg | Canonical: conviction taxonomy, ethical frameworks, AI priority stacks |
| designs/systems/npc_behavior_v30_infill.md | ttrpg | Extended NPC behavior |
| designs/npcs/npc_roster_v30.md | ttrpg | NPC roster |
| designs/npcs/npc_character_analyses_v30.md | ttrpg | Character analyses |
| designs/npcs/npc_foils_v30.md | ttrpg | Foil relationships |
| designs/ttrpg/edeyja_npc.md | ttrpg | Edeyja specification |
| tests/sim_npc_01.py | ttrpg | NPC simulation code |
| tests/sim_npc_01_results.md | ttrpg | NPC sim results |
| tests/audit_npc_behavior_system.md | ttrpg | NPC audit |
| systems/npc/* | valoria-game | Godot NPC systems (6 files) |
| resources/instances/characters/* | valoria-game | NPC instances (22 files) |

## C. Audit Structure

**Working well:** PP-NPC-01 through NPC-04 fix real simulation failures. Haelgrund (39/40) is the best-specified NPC. Ethical framework Ob modifiers create genuine faction differentiation.

**Not working well:** Lenneth (28/40) has zero mechanical expression. Elske (24/40) has zero characterization. Almud has no BG mode expression.

**Outstanding:** J-4 (stance triangles for Lenneth, Elske, Haelgrund). Post-coup Löwenritter AI. Baralta succession.

---

# S11 — COMBAT (PERSONAL)

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/combat/combat_v30.md | ttrpg | Canonical combat spec |
| designs/combat/combat_v30_infill.md | ttrpg | Extended combat |
| references/params_combat.md | ttrpg | Combat params |
| skills/valoria-combat-simulator/* | ttrpg | Combat sim skill |
| tests/sim_combat_*.py | ttrpg | Combat simulation scripts |
| systems/engine/CombatInitiativeSystem.gd | valoria-game | Godot initiative |
| scenes/containers/combat/* | valoria-game | Godot combat scene |

## C. Audit Structure

**Working well:** Most stable subsystem. PP-285 (Rescue), PP-294 (Feint) confirmed via simulation. Weapon three-axis system is elegant.

**Not working well:** Nothing significant.

**Outstanding:** None. This system is complete.

---

# S12 — SOCIAL CONTESTS

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/contest/social_contest_v30.md | ttrpg | Canonical contest spec |
| designs/contest/social_contest_v30_infill.md | ttrpg | Extended contest |
| references/params_contest.md | ttrpg | Contest params |
| scenes/containers/debate/* | valoria-game | Godot contest scene |

## C. Audit Structure

**Working well:** Calibration confirmed (±1 Cha = 25-30%, ±4 = Total Victory). Adjudicator type matters. Coalition mechanic works.

**Not working well:** 16-cell decision space (2 genres × 2 orientations × 4 styles) is steep learning curve. Needs strong UI.

---

# S13 — THREAD OPERATIONS

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/ttrpg/threadwork_v30.md | ttrpg | Canonical threadwork (57K chars) |
| designs/ttrpg/threadwork_v30_infill.md | ttrpg | Extended threadwork |
| references/params_threadwork.md | ttrpg | Thread params (51K chars) |
| designs/ttrpg/threadwork_philosophical_reference_v30.md | ttrpg | Philosophical underpinnings |
| tests/sim_opposing_threadwork_final.md | ttrpg | Opposing ops sim |
| tests/sim_thread_*.md | ttrpg | Thread simulations (many) |
| systems/engine/ThreadworkSystem.gd | valoria-game | Godot threadwork |

## C. Audit Structure

**Working well:** Post-PP-619 system is clean. Three-axis Ob is elegant. Mending immunity is philosophically derived. N-way collapse is well-specified.

**Not working well:** threadwork_v30 at 57K chars is the second-largest doc. Params at 51K chars.

**Outstanding:** None — most thoroughly patched system (PP-600 through PP-632).

---

# S14 — FIELDWORK

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/fieldwork/fieldwork_v30.md | ttrpg | Canonical fieldwork (63K chars — largest design doc) |
| designs/fieldwork/fieldwork_v30_infill.md | ttrpg | Extended fieldwork |
| designs/fieldwork/fieldwork_*.md | ttrpg | 8 atomized sub-files (investigation, socializing, exploration, exposure, etc.) |
| references/params_fieldwork.md | ttrpg | Fieldwork params |
| systems/engine/InvestigationSystem.gd | valoria-game | Godot investigation |

## C. Audit Structure

**Working well:** PP-632 Disposition/Knot unification. Sincerity Gate (37% failure). Cover calibration. Evidence Track pacing.

**Not working well:** fieldwork_v30 at 63K chars is unwieldy. Already atomized into 8 sub-files which helps.

**Outstanding:** Fieldwork has no explicit resource cost for extended investigation (no "health" parallel).

---

# S15 — MASS COMBAT

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/mass_combat/mass_battle_v30.md | ttrpg | Canonical mass combat (38K chars) |
| designs/mass_combat/mass_battle_v30_infill.md | ttrpg | Extended mass combat |
| references/params_mass_combat.md | ttrpg | Mass combat params |
| scenes/containers/battle/* | valoria-game | Godot battle scene |

## C. Audit Structure

**Working well:** Seven-phase structure is comprehensive. Splitting doctrine (+9-45%) validated. Battle consequences (MS −1, IP +2, Political Stability +1) create meaningful costs.

**Not working well:** Unit Health = Type Health × Size is unvalidated. Cognitive load at table is high.

**Outstanding:** J-1 (pool formula). Unit Health validation.

---

# S16 — EMERGENT ARCS

## B. File Index

| File | Repo | Role |
|------|------|------|
| references/arc_register.md | ttrpg | Canonical arc register |
| references/arc_register_infill.md | ttrpg | Extended arc descriptions |
| gm_ref/arcs_*.md | ttrpg | GM reference arc batches (8 files) |
| designs/gm_ref_cp14/arcs/*.md | ttrpg | Arc design files (6 files) |
| designs/ttrpg/valoria_emergent_scenarios.md | ttrpg | Emergent scenarios |
| designs/ttrpg/valoria_narrative_scenario_chains.md | ttrpg | Narrative chains |
| tests/sim_arc_*.md | ttrpg | Arc simulations (many) |
| systems/data/ArcEvaluatorRegistry.gd | valoria-game | Godot arc evaluator |
| resources/instances/triggers/*.tres | valoria-game | Trigger instances (15 files) |

## C. Audit Structure

**Working well:** Vector-based architecture (pressures, not triggers). 120+ arcs covering all factions and scales.

**Not working well:** Overtriggered Church, undertriggered Crown/Hafenmark/Varfell. Missing territory-based triggers. Only 5 Zoom In triggers for 120+ arcs.

**Outstanding:** 20–30 Zoom In triggers needed. Territory-based arc triggers. RM arc coverage.

---

# S17 — SCALE TRANSITIONS & HYBRID

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/hybrid/scale_transitions_v30.md | ttrpg | Canonical scale transitions |
| designs/hybrid/scale_transitions_v30_infill.md | ttrpg | Extended transitions |
| designs/hybrid/hybrid_gaps_v30.md | ttrpg | Identified gaps |
| references/params_scale_transitions.md | ttrpg | Transition params |
| systems/transition/TransitionManager.gd | valoria-game | Godot transitions |

## C. Audit Structure

**Working well:** Domain Echo (Sufficient Scope → ±1/±2 faction stat) is clean.

**Not working well:** Only 5 Zoom In triggers. Hybrid mode's promise is unkept without more triggers.

**Outstanding:** 20–30 Zoom In triggers. Mid-execution zoom conversion protocol.

---

# S18 — CHARACTER & HISTORIES

## B. File Index

| File | Repo | Role |
|------|------|------|
| designs/characters/character_histories_v30.md | ttrpg | Canonical histories |
| designs/characters/character_histories_v30_infill.md | ttrpg | Extended histories |
| designs/conviction_track/conviction_track_v30.md | ttrpg | Certainty track |
| scenes/character_creation/CharacterCreationManager.gd | valoria-game | Godot character creation |
| resources/data_types/CharacterData.gd | valoria-game | Character data type |
| resources/data_types/HistoryData.gd | valoria-game | History data type |
| resources/data_types/KnotData.gd | valoria-game | Knot data type |
| resources/data_types/SkillData.gd | valoria-game | Skill data type |
| systems/engine/SkillSparkingSystem.gd | valoria-game | Skill sparking |
| systems/engine/SkillEffectResolver.gd | valoria-game | Skill effects |

## C. Audit Structure

**Working well:** 10 attributes with clear domain separation. 31-point creation with min/max constraints. Certainty redesign (0–5 oscillating) is philosophically superior.

**Not working well:** CharacterCreationManager.gd references attributes but doesn't implement allocation constraints.

**Outstanding:** Confirm certainty redesign propagated to params_core.

---

# INFRASTRUCTURE FILES (not a system, but required context)

| File | Role |
|------|------|
| references/canonical_sources.yaml | Which file governs each system |
| references/file_index.md / file_index_summary.md | File discovery |
| references/propagation_map.md | Cross-file change tracking |
| references/design_registry.yaml | Skeleton/infill tracking |
| canon/patch_register_active.yaml | Open/recent patches |
| canon/patch_register_archive.yaml | Applied patches |
| canon/patch_register_index.md | Patch index |
| canon/editorial_ledger.yaml | Active editorial decisions |
| canon/editorial_ledger_archive.yaml | Resolved editorials |
| session_log_current.md | Session state |
| skills/valoria-orchestrator/scripts/github_ops.py | Git operations |
| skills/valoria-orchestrator/scripts/valoria_hooks.py | Enforcement hooks |
| tools/*.py | CI/CD tooling (7 files) |
| .github/workflows/valoria-ci.yml | CI workflow |

---

# SYSTEM INTERDEPENDENCY MATRIX

## Reading the Matrix

Each cell describes the interaction between the row system and the column system. Interactions are typed:

- **C** = Constraint (row constrains column's design space)
- **F** = Feeds (row's output is column's input)
- **M** = Modifies (row's actions change column's state)
- **R** = Reads (row reads column's state for decisions)
- **T** = Transitions (row triggers scale change into column)
- **—** = No direct interaction

## Pairwise Matrix

|  | S01 Meta | S02 Core | S03 Geo | S04 Clock | S05 Calam | S06 Fact | S07 Victory | S08 TC | S09 Mil | S10 NPC | S11 Combat | S12 Contest | S13 Thread | S14 Field | S15 Mass | S16 Arcs | S17 Scale | S18 Char |
|--|---------|---------|---------|-----------|-----------|---------|-------------|--------|---------|---------|------------|-------------|------------|-----------|----------|----------|-----------|----------|
| **S01 Meta** | — | C | — | — | C | — | — | — | — | C | — | — | C | C | — | C | — | C |
| **S02 Core** | — | — | — | — | — | F | — | — | — | F | F | F | F | F | F | — | — | F |
| **S03 Geo** | — | — | — | F | F | — | F | F | F | — | — | — | — | — | F | F | — | — |
| **S04 Clock** | — | — | R | — | F | R | F | F | — | R | — | — | R | R | — | F | — | — |
| **S05 Calam** | — | — | R | R | — | — | M | — | — | — | — | — | R | — | — | F | — | — |
| **S06 Fact** | — | R | R | M | — | — | F | F | F | R | — | — | — | — | — | F | F | — |
| **S07 Victory** | — | — | R | R | R | R | — | R | — | — | — | — | R | — | — | F | — | — |
| **S08 TC** | — | — | R | M | — | M | M | — | R | R | — | M | — | — | — | F | — | — |
| **S09 Mil** | — | R | R | — | — | R | — | R | — | — | — | — | — | — | F | — | — | — |
| **S10 NPC** | R | R | — | R | — | R | R | R | — | — | — | R | R | R | — | F | — | R |
| **S11 Combat** | — | R | — | — | — | — | — | — | — | — | — | — | — | — | T | F | T | R |
| **S12 Contest** | — | R | — | — | — | M | — | M | — | R | — | — | — | — | — | F | T | R |
| **S13 Thread** | R | R | — | M | M | — | M | — | — | — | — | — | — | R | M | F | T | R |
| **S14 Field** | R | R | R | M | — | — | — | M | — | M | T | T | R | — | — | F | T | R |
| **S15 Mass** | — | R | R | M | — | M | — | — | R | — | T | — | R | — | — | F | T | — |
| **S16 Arcs** | R | — | R | R | R | R | R | R | R | R | R | R | R | R | R | — | R | R |
| **S17 Scale** | — | — | — | — | — | M | — | — | — | — | T | T | T | T | T | F | — | — |
| **S18 Char** | R | R | — | — | — | — | — | — | — | R | F | F | F | F | — | — | — | — |

## Key Interaction Chains (compound effects requiring joint simulation)

### Chain 1: Battle → Peninsula Clocks → Victory
`S15 Mass Combat` → M → `S04 Clocks` (MS −1, IP +2, Pol.Stab +1) → F → `S07 Victory` (shared loss check, universal victory gate)

**Simulation status:** ED-538 (P1, unvalidated). Must simulate: does repeated battle cascade into shared loss before any faction achieves victory?

### Chain 2: Thread Ops → MS → Calamity Radiation → Territory State
`S13 Thread` → M → `S04 Clocks` (MS change) → F → `S05 Calamity` (radiation zone expansion) → M → `S03 Geo` (territory effects)

**Simulation status:** Validated individually. Compound chain not simulated end-to-end.

### Chain 3: Church Mechanics → TC → Seizure → Accord → Victory
`S08 TC Reform` (CI advancement) → M → `S04 Clocks` (CI milestones) → F → `S07 Victory` (Graduated Seizure) → M → `S03 Geo` (Accord 1 on conquest) → R → `S07 Victory` (Accord ≥ 2 gate)

**Simulation status:** ED-539 (P1, unvalidated). The Accord ≥ 2 gate may make Church conquest self-defeating.

### Chain 4: Fieldwork → NPC → Contest → Faction → Domain Echo
`S14 Fieldwork` (Disposition change) → M → `S10 NPC` (arc trigger) → R → `S12 Contest` (Conviction-modified argument) → M → `S06 Faction` (Mandate/Influence change) → F → `S17 Scale` (Domain Echo)

**Simulation status:** Partially validated. Full chain not simulated.

### Chain 5: Personal Combat → Wounds → Thread Contact → Coherence → Knot
`S11 Combat` (wound during Thread contact) → Spirit check → `S13 Thread` (contact broken, Coherence −1) → impact on `S14 Fieldwork` (Knot strain) → M → `S18 Character` (Disposition change on rupture)

**Simulation status:** Validated (SIM-STRESS-06, SIM-DEBT-FW-10).

### Chain 6: NPC AI → Domain Action → Territory → All Clocks
`S10 NPC` (priority stack selection) → `S06 Faction` (Domain Action execution) → M → `S03 Geo` (territory Accord/Piety/Prosperity) → M → `S04 Clocks` (CI, Political Stability) → F → `S07 Victory` + `S16 Arcs`

**Simulation status:** valoria_sim v4 validates basic chain. Accord-aware NPC AI not yet re-simulated.

---

# UPLOADED DOCUMENTS NOT YET COMMITTED

These files from this conversation should be committed or stored:

| File | Recommended Action |
|------|-------------------|
| valoria_holistic_audit.md | Commit to designs/ or reference as session artifact |
| clock_registry_staleness_report.md | Use to update clock_registry_v30.md, then discard |
| valoria_character_arc_web.html | Evaluate for tools/ |
| valoria_unified_videogame_spec_r2.md | Commit to designs/ if not already |
| stability_occupation_treaty_parliament_v1.md | Subsumed by faction_layer_v30 — do not commit separately |
| certainty_redesign_and_audit.md | Check if propagated to conviction_track_v30; commit if not |
| emergent_arc_system_v8.md | Check against arc_register.md; merge any missing vectors |
| character_histories_v2.md | Check against character_histories_v30; merge any missing |
| simulation_strategy_v8.md | Commit to tests/ as sim planning reference |

---

# HOW TO USE THIS WORKPLAN

**For any future session:**

1. Identify which system(s) the task touches.
2. Look up the system's **File Index** (section B) to know what to fetch.
3. Check the **Interdependency Matrix** to identify which other systems are affected.
4. Fetch the skeleton docs for all affected systems (load infill only when needed).
5. Check the **Audit Structure** (section C) for known issues before starting work.
6. After completing work, check the **Interaction Chains** to see if compound effects need simulation.

**For audits:**
1. Pick a row in the matrix.
2. For each non-empty cell in that row, verify the interaction is correctly implemented in both systems' docs.
3. Flag any interaction that lacks simulation validation.
4. Cross-reference against the Audit Structure's "Outstanding" items.

**For simulation planning:**
1. Pick an Interaction Chain.
2. Identify which systems are involved.
3. Fetch all relevant params files.
4. Run valoria_sim or a targeted Python simulation covering the chain.
5. Update the chain's "Simulation status" field.
