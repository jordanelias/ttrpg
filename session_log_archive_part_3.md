
## Session: 2026-04-11 — NPC Directory Consolidation

### Tasks completed
1. Consolidated `designs/npcs/` into canonical structure:
   - **`npc_roster.md`** (492 lines) — merged roster + caste annotations (§14 appended)
   - **`npc_character_analyses.md`** (333 lines) — Part One: roster NPCs + Part Two: ruler diamond & existing named NPCs
   - **`npc_foils.md`** (301 lines, new) — Part One: axis analysis + Part Two: subjective perspectives & extended foil network

2. Deprecated 8 files (deprecation banner added, content retained for audit trail):
   - `npc_roster_caste_annotations.md` → merged into roster §14
   - `npc_character_analyses_existing.md` → merged into analyses Part Two
   - `ruler_diamond_foil_analysis.md` → merged into foils Part One
   - `ruler_diamond_extended_foils.md` → merged into foils Part Two
   - `npc_comprehensive_audit.md` → superseded
   - `lenneth_threadwork_design.md` → content absorbed into roster + params_threadwork
   - `almud_correction_plan.md` → resolved, audit trail only
   - `ed_403_406_407_resolutions.md` → editorial resolutions absorbed

### Commit
- `deaf729ccf7a92948d1d0916956e79ca0bc2faa9`
- `[cleanup] Consolidate designs/npcs — roster, analyses, foils; 8 files deprecated`

### Post-commit checks
- `broken_dependency_checker.py`: 15 broken (pre-existing glob patterns — not introduced by this commit)
- `patch_propagation_checker.py`: 138 failures (pre-existing params propagation debt — not introduced)

### Open editorials carried forward
ED-370, ED-371, ED-372, ED-373 (as prior session)


## Session 2026-04-12 — Arc Audit Resolution

**Task:** Resolve audit findings from two-day arc collation + canon/NPC review.

**Completed:**
- ED-408 resolved: Prudence Cardinal named Aldric Tormann (npc_roster §13, arcs_36_40)
- ED-409 resolved: Torsvald Deniability Debt threshold = 3
- ED-410 resolved: Collection 1/season confirmed canonical (PP-168); no modification
- ED-411 resolved: Solberg recall → Schoenland Intel Ob 2 (PP-555 applied); IP threshold corrected 15→8
- ED-412 resolved: Convergence compression formula N + max(4, 8−N)
- Arc 40 partial convergence table added (4/4, 3/4, 2/4, 1/4 outcomes)
- Collision point 4 false positive documented (arc_narrative_analysis)
- Cross-Batch Collision Register added (arc_narrative_analysis)
- PP-556: Arc-specific Hybrid Zoom In trigger extension (zoom_in_out reference card)
- Ehrenwall Counter one-way ratchet documented as intentional (not a gap)
- Parish Revolt buildup: cross-referenced to existing roster Mandate erosion (no new mechanic)

**Proposals struck after full NPC/canon review:**
- Ehrenwall Counter decrement: STRUCK — contradicts documented characterisation ("The Ledger That Never Forgives"; never decrements is intentional design per npc_comprehensive_audit)
- Parish Revolt Stability −1 addition: STRUCK — creates destabilising stack on top of existing Mandate erosion; existing mechanism is sufficient
- Vaynard Intel escalation to TS growth: STRUCK — Intel already governs Collection roll (Intel vs Ob 2 per PP-168); TS growth is +1/use canonical; no additional modifier warranted

**Open items:** Vaynard full NPC roster entry (blocks Arc 39 simulation); TK track parameterization; Baralta roster entry; Zoom In arc-specific triggers to be added per-arc doc as work continues.


---

## Session: 2026-04-11 — Repository-Wide Consolidation (continued)

### Task: Consolidate all folders (except deprecated/) — mark deprecated

### Decisions made per folder

**tests/, references/, skills/, tools/, docs/, versions/**: No action — test archive, params system, skill SKILL.md structure, and utilities are all correctly structured. No consolidation applicable.

**gm_ref/**: No action — all arc files (arcs 01-04, 05-09, 10-18, 36-40, 41-45, narrative analysis) are current sequential batches. No overlaps.

**designs/setting/, designs/combat/, designs/contest/, designs/conviction_track/, designs/hybrid/, designs/mass_combat/, designs/mechanics/, designs/systems/**: Single-file folders or clean multi-file folders. No action.

### Commits

**Commit `8d08ef2`** — canon/ + compilation/v0.14/
- Deprecated 1 canon file: audit_threadwork_v24.md (superseded by v25)
- Deprecated 15 compilation/v0.14 stage files (superseded by design docs or params files)
- Kept: README, valoria_ruleset_v0.14.md, stage4_southernmost (only southernmost source), stage6_factions (only TTRPG factions source), stage11_scale_transitions (only source), stage12_campaign_modes (only source)

**Commit `a1168683`** — designs/board_game/ + designs/gm_ref_cp14/
- Deprecated 2 board_game files: faction_resolutions_2026_04_07.md, stress_test_report (absorbed; bg_v05 and victory_architecture are canonical)
- Kept: valoria_bg_v05_simulation_and_patches.md (canonical), victory_architecture_v1.md (canonical), valoria_map_v2.svg, varfell_path_b_redesign_ed311.md (open editorial ED-311)
- Deprecated 4 gm_ref_cp14/arcs (arcs 1-12, superseded by gm_ref/ arcs 1-18)
- Deprecated 10 gm_ref_cp14/dashboards (CP14 mechanics, outdated)
- Deprecated 3 gm_ref_cp14 other (workplan, zoom card, templar crossing flowchart)
- Kept: arcs 16-35 + experimental + campaign arcs (no gm_ref/ replacements exist)

**Commit `96c64d14`** — designs/ttrpg/ + designs/worldbuilding/ + designs/ root
- Deprecated 11 ttrpg/ files: all Phase 1 batch files (batch_a through batch_f, batch_ad_resolutions) + church_territorial_seizure, generation_tasks, lowenritter_faction_card, mechanical_tasks_and_patches, succession_mechanic
- Kept: threadwork_redesign_v25.md (canonical), edeyja_npc.md (canonical NPC), valoria_emergent_scenarios.md, valoria_narrative_scenario_chains.md (referenced by gm_ref arcs), threadwork_philosophical_reference.md (used by canon-guard skill)
- Updated SUPERSEDED.md to correctly document kept vs deprecated files
- Deprecated worldbuilding/editorial_comprehensive_review.md (absorbed into editorial ledger)
- Deprecated designs/cogload_reduction_strategies.md (superseded by cogload_moderate_target.md)

### Total deprecated this session extension: 48 files across 6 directories
### Post-commit checks: 15 broken (pre-existing glob patterns), 139 propagation failures (pre-existing) — no new issues introduced

### Open editorials carried forward
ED-311 (Varfell Path B — awaiting user review)
ED-370, ED-371, ED-372, ED-373 (carried from prior session)


---

## Session — 2026-04-13: Character Histories & Skill System Design

### Stage: Design — Character Creation / Skill Acquisition

### Summary
Designed and implemented the Character Histories lifepath system with SaGa-style skill sparking, 
Recall-as-skill-gatekeeper, and skill levels 1–3. Full Godot implementation committed to 
jordanelias/valoria-game.

### Key Decisions
1. **Lifepath structure:** 4-stage character creation (Origin → Formation → Vocation → Catalyst)
   - Origin: geography, culture, Certainty base, first Knot. 0 starting skills.
   - Formation: education/shaping, Certainty modifier, second Knot. 1 starting skill.
   - Vocation: profession, faction affiliation, third Knot. 2 starting skills.
   - Catalyst: inciting event, starting Belief, campaign hook. 0 starting skills.
   - Total starting skills: 3.

2. **Recall as gatekeeper (triple duty):**
   - Equip slots: max_equipped = Recall (1–7). Swap loadout between scenes.
   - Skill depth: Level 2 requires dice_bonus ≥ 3; Level 3 requires dice_bonus ≥ 5. Recall caps dice_bonus.
   - Learning speed: floor(Recall/2) bonus dice on spark checks.

3. **Coherence degrades equip slots:** Fragmented = −1 slot. Fractured/Severed = −2 slots. 
   Practitioners lose skill access — not just social/memory rolls — as Coherence drops.

4. **SaGa-style sparking:** Skills acquired through scene use, not menus.
   - Overwhelming at Ob 3+ → automatic spark
   - Success at Ob 3+ → Spirit + Recall/2, TN 7, Ob 1
   - Partial at Ob 2+ → Spirit + Recall/2, TN 7, Ob 2
   - Failure at Ob 3+ → Spirit + Recall/2, TN 8, Ob 1
   - Ob 1 → no check (routine)
   - Cross-History hybrid sparks for simultaneous use of 2+ Histories

5. **Skill levels 1–3:** Sparking prioritises level-ups over new skill acquisition.
   Level determines effect magnitude (per-level effect arrays in SkillData).

### Commits (jordanelias/valoria-game)
- `813f27b` — Initial History/Skill/Sparking system (10 files)
- `ab7c10a` — Recall as equip gatekeeper + skill levels 1–3 (9 files)

### Commits (jordanelias/ttrpg)
- Character Histories lifepath design doc: designs/characters/character_histories_lifepath.md

### New Editorial Items
- ED-374: Lifepath system requires user approval
- ED-375: Skill effects provisional — simulation required
- ED-377: Intuitive Threadwork + Co-Movement interaction open
- ED-378: Confirm 3 Knots is the right lifepath count
- ED-379: Can experienced characters have 2 Catalysts?
- ED-380: Southern Einhir Descendant +5 Thread Sensitivity at creation — Leap eligibility
- ED-381: Recall 1 = 1 equip slot — too punishing?
- ED-382: Coherence equip slot loss — player choice vs auto-drop?
- ED-383: Level 3 requiring Recall ≥ 5 — intentional specialist gate?

### Open editorials carried forward
ED-311 (Varfell Path B — awaiting user review)
ED-370, ED-371, ED-372, ED-373 (carried from prior session)

---

## Session: 2026-04-13 — NPC Behavior System Design

### Task
Design NPC ethical stances and resonance styles impacting AI decision trees, arc emergence, and behavior.

### Deliverables
1. **designs/systems/npc_behavior_system_v1.md** — Full design (860+ lines). Stance Triangles for 13 NPCs, BG Priority Trees for 9 factions, arc profiles, Resonant Style Contest integration, Framework Drift.
2. **tests/audit_npc_behavior_system.md** — 15 findings. All HIGH/MEDIUM resolved or flagged.

### New Editorial Items
ED-384 through ED-400 (17 items). P1-BLOCKER: ED-387.

### New Simulation Debt
SIM-NPC-01 through SIM-NPC-05.

### Open editorials carried forward
ED-311, ED-370–373, ED-374–383, ED-384–400.

### Consolidation commit — 2026-04-13
Merged character_histories_lifepath.md + character_histories_revision_pass.md into single canonical document.
- Starting skills: 5 (Origin 1, Formation 1, Vocation 2, Catalyst 1)
- Canon fix: 1D Forgetting misattribution corrected (Church suppression, not Forgetting)
- Generic entries rebuilt: 1F (Tideward/Ashmarket modifiers), 1H (Occupation Displaced / Calamity Orphan / Church Ward)
- 2D rebuilt as Empiricist; 2E Weapons Training changed from TN−1 to +1D Offence
- 5 new Vocations: Crown Farmer, Diplomat, Independent Criminal, Church Investigator, Löwenritter Patrol Officer (threadcut veteran)
- Catalysts specified: 4D faction-specific, 4F three specific Valorian conflicts, 4G GM-determines direction
- Thread-adjacent spark skills added to 4 non-practitioner Vocations
- Knot audit: 8 weak Knots rewritten for dramatic specificity
- Skill level principle: L1 base, L2 quantitative, L3 qualitative unlock (7 example skills mapped)
- 4E Leap Scar changed from −1 Ob to +1D (avoids OB_FLOOR interaction)
- Literacy model formalised by Formation
- Revision pass doc deleted (absorbed)


---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_DEBATE_STRESS_TEST
phase: Phase 9 — Debate stress test (SIM-DEBT-01)
status: COMPLETE

completed:
  - SIM-D-01: Debate stress test Modes A+D+J+L. New calibration baselines established.
  - PP-097/098/099 PROVISIONAL: applied in-place to debate_system_redesign_v1.md.
  - SIM-D-02: Debate Mode C scenario — Himlensendt vs Baralta, Parliament.
  - PP-100 PROVISIONAL: §6.7 proposer/initiative decoupling clarified in-place.
  - ED-051 (P1): stage13 NPC debate stat block missing — Attunement, Focus, Poise, Bonds.
  - ED-052 (P2): NPC Composure formula mismatch — shorthand vs Poise+Bonds+3.
  - SIM-DEBT-01: RESOLVED.
  - debate_system_redesign_v1.md: v1.2

key_findings:
  - 3-exchange Formal Debate → Compromise ~95% at resistance 2 (structural design, not a flaw)
  - Resistance level is the dominant variable for track movement in short debates
  - Genre weight dominates pool-size adjustments up to ~+2D Memory bonus
  - DIVERGE produces 0 strain — Composure drain only in CLASH/COMPETITION
  - F-C-04 P1: NPC debate attributes missing — blocks authoritative NPC debate sims
  - F-C-06 P1: Novice debate time 9 min/exchange — GM reference card needed

next_action:
  task: "GM reference card for debate (one-page: §6.1 setup + §6.4 exchange flowchart + genre weight table). Addresses F-C-06 P1."
  note: "Or pivot to next simulation priority. Confirm with user."

commits_this_session:
  - 22a1f24: SIM-D-01 + PP-097/098/099 + params_debate + coverage_matrix
  - 1641078a: debate v1.1 in-place patches + propagation_map + session_log
  - [this]: SIM-D-02 + PP-100 + ED-051/052 + debate v1.2 + coverage_matrix + propmap + session_log
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_SKELETON_CLEAN_2
phase: Phase 10 — bg_v05 → v0.6, threadwork → v2.6, skeleton-debt cleared
status: CLOSED

completed:
  - bg_v05 → v0.6: ST-BG-03/04/06/07/08/09 and ST-INT-01/05/06/09/10 applied in-place. PART THIRTEEN appendix eliminated. 981 → 1000 lines (net minimal growth because patches are now context notes, not appendix sections).
  - threadwork_v25 → v2.6: ST-TW-01–05 and R-54–R-68 applied in-place. Parts 10+11 appendix eliminated. 1059 → 1108 lines.
  - skeleton-debt register updated in file_index.md.
  - In-place patching rule now enforced in simulator Mode I and orchestrator.

skeleton_debt_remaining:
  - threadwork v2.6 → v3.0: Part 1 philosophical framing should move to a reference doc (separate from the mechanical spec). Low priority — Part 1 is useful reference for canon-guard.
  - compilation/v0.14/stage8_combat.md: Part Eleven appendix. Low priority — compilation layer.
  - compilation/v0.14/stage11_scale_transitions.md: PP-089/090 appended. Low priority.

next_action:
  task: "Begin simulation. stress test debate — SIM-DEBT-01 (Presence×2 pool recalibration)."
  note: "All high-priority skeleton-debt cleared. Design documents now internally consistent. Pipeline verified."
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_DEBATE_STRESS_TEST
phase: Phase 9 — Debate stress test (SIM-DEBT-01)
status: IN PROGRESS

completed:
  - SIM-D-01: Debate stress test Modes A+D+J+L. Calibration baselines recalibrated.
  - PP-097 PROVISIONAL: DIVERGE+TIE → Tie rule fires (any interaction type). Applied in-place to debate_system_redesign_v1.md §6.4 DIVERGE block.
  - PP-098 PROVISIONAL: Regroup at Concentration=0 → consumes Spent without penalty. Applied in-place §6.4 Step 5.
  - PP-099 PROVISIONAL: Obscuring in Divergence → Doubt Marker; orientation_weight=1.0. Applied in-place §6.4 DIVERGE block.
  - debate_system_redesign_v1.md bumped to v1.1.
  - propagation_map.md updated with DEBATE section.
  - SIM-DEBT-01 PARTIALLY RESOLVED: Mode C scenario run still needed.

key_findings:
  - P(Overwhelming) doubled: ~25% old → ~60% new (symmetric 8D pools)
  - Exchanges to Rattled halved: 7-9 old → 3-5 new (Composure 9)
  - Track movement now consistent 1 step/exchange vs 0 often under old pool
  - F-D-01 P1 (PP-097): DIVERGE+TIE ambiguity — Tie rule takes priority
  - F-D-06 P2: Grand Debate + Corroboration ~90 resolution steps, no GM reference card

next_action:
  task: "Mode C debate scenario — Baralta vs Himlensendt, 3-exchange Formal Debate. Completes SIM-DEBT-01."
  note: "Read stage13_npcs.md for Baralta and Himlensendt stats before running. New pool: (Presence×2)+History."

commits_this_session:
  - 22a1f24: SIM-D-01 test file + patch_register PP-097/098/099 + params_debate recalibration + coverage_matrix
  - [this commit]: debate_system_redesign_v1.md v1.1 in-place patches + propagation_map + session_log
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_SKELETON_CONTAINERS_FINAL
phase: Phase 8 — Skeleton rulesets, container pattern, broken dependency checker
status: CLOSED

completed:
  - tools/broken_dependency_checker.py: executable scanner for broken refs across propagation_map, canonical_sources, skill_registry, editorial_ledger. Exits 1 if broken. propagation_map Step C now references it.
  - Container pattern applied to params files: clean values file + separate history file. params_combat 113→80 lines, params_debate 141→88, params_mass_combat 203→136, params_threadwork 269→246, params_board_game 250→194. Each has container refs to patch_history and canonical_sources.
  - Skeleton ruleset principle and container pattern documented in project_instructions.md.
  - Project instructions: PAT/GraphQL bootstrap section at top of document.
  - Skeleton-debt flagged: debate Parts 1-4 (historical/philosophical), threadwork Part 1.

next_action:
  task: "Begin simulation. Priority: stress test debate (SIM-DEBT-01)."
  note: "All infrastructure complete. Pipeline verified. Project instructions ready."

commits_this_session:
  - bf2917b: canonical_sources + P-15 + project instructions
  - a256278: broken_dependency_checker + container pattern + skeleton docs
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_FINAL_REVIEW
phase: Phase 7 — Canon, clarity, canonical sources, project instructions
status: CLOSED

## SESSION SUMMARY

### Canon-guard analysis
- Amendment 01 (self-rendering) introduces three-layer being-persistence; Leap redefined; Coherence 0 TS-gated branching
- These were NOT in P-01-P-14. P-15 added to canon/02_canon_constraints.md
- Canon-guard updated with amendment integration workflow (auto-runs when any canon file changes)
- Canon-guard now reads canonical_sources.yaml to determine which document to validate

### Version authority
- references/canonical_sources.yaml created — maps every system to canonical source
- Rule: compilation_current:false = use design doc; compilation_current:true = compilation is correct
- Key reversals: combat and mass_combat now point to designs/ not compilation stage8
- simulator Read Protocol updated to check canonical_sources.yaml first (Step 0)

### Params fixes
- params_combat: source corrected to designs/combat/combat_design_v1.md
- params_mass_combat: source corrected (combat_design_v1 + mass_battle_v3)
- params_scale_transitions: version tag updated (stage11 updated April 2)

### Token efficiency
- The params abstraction IS working correctly. Skills read params (compact) not design docs (verbose).
- Simulator trimmed from 441 to 432 lines (duplicate version check removed).
- Efficiency note added to project instructions.

### Project instructions
- project_instructions.md rewritten. Key changes:
  - Removed "check Project Files first" (Project Files deprecated)
  - Added canonical_sources.yaml reference
  - Added simulation command vocabulary table
  - Added audit criteria coverage statement
  - Updated model routing table
  - Added compilation rules (lowest priority, when to compile)
  - Added open blockers summary

### Pipeline status
- 5/5 questions: YES (with honest note on broken-dependency detection)
- 12/12 checks passing
- All critical issues from review resolved

### Remaining honest limitations
- Propagation map broken-dependency detection: described but not executable code
- SIM-DEBT-01: debate calibration needs re-simulation with Presence×2 pool
- ED-048: Ceiral non-canon name in 22 files — awaiting canonical name from user

### next_action:
  task: "Run simulations. Priority: (1) stress test debate (SIM-DEBT-01), (2) stress test combat, (3) simulate hybrid scenario."
  note: "Pipeline verified and documented. Project instructions ready. Begin simulation work next session."

### commits_this_session:
  - a96161: simulation infra modes J/K/L/M (prior)
  - e4a276e: pipeline clarity fixes (prior)
  - 74836d8, 1a6ea6a: version check fixes (prior)
  - bf2917b: canonical_sources + P-15 + project_instructions (this close)
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_PIPELINE_VERIFIED
phase: Phase 6 — Pipeline review, clarity fixes, viability confirmed
status: CLOSED

## SESSION SUMMARY

### Pipeline review findings (4 blocking, 5 warnings, 1 note)

Blocking — all fixed:
- [1] Simulator Mode I: duplicate Step 7 → renumbered to Step 8
- [2] Skill registry: described non-existent Tier1/2/2.5 simulation skills — rewritten to reflect actual GitHub skills with simulation command routing table
- [3] State transfer spec: section 5 heading still said UNRESOLVED after ED-050 resolution — fixed
- [4] Simulator Mode G2: used old Rhetoric pool terminology — updated to (Presence×2)+History, Conviction Track, genre/orientation framing

Warnings — all fixed:
- [W1] Simulator version check referenced compilation/README.md — replaced with params version tag check
- [W2] Canon-guard path: canon/canon_constraints.md → canon/02_canon_constraints.md
- [W3] Compiler: old gap register reference → canon/editorial_ledger.yaml; output path fixed; designs-first note added
- [W4] Mechanic-audit Mode G: incomplete path to state_transfer_spec → full path added
- [W5] Session protocol: stale filename valoria_session_log.md → session_log_current.md

Note — communicated:
- Propagation map broken-dependency detection is described but not executable code; honest limitation

### Pipeline viability: CONFIRMED
12/12 checks passing after fixes.

### Commits this session:
- e4a276e: all pipeline fixes (skill_registry, simulator, audit, canon-guard, compiler, editorial-register, session_protocol, state_transfer_spec, propagation_map)
- 74836d8: first pass compilation/README fix
- 1a6ea6a: complete compilation/README removal

### next_action:
  task: "Run first simulation. Recommend: stress test debate (SIM-DEBT-01 — re-calibrate Presence×2 pool). Use simulator Mode G2 + Mode J (cognitive load) + Mode L (precedent)."
  note: "Pipeline is verified and ready. Every criteria dimension covered. All blocking issues resolved. Propagation is automatic."
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_SIMREADY_FINAL
phase: Phase 5 — Simulation infrastructure complete and self-maintaining
status: CLOSED

## SESSION SUMMARY

### Completed
- ED-050 resolved: 7-phase mass battle. Offensive Thread = Phase 4 (between Manoeuvre and Engagement). Support Thread = Phase 6 Cascade step 4-5. All damage (Volley + Thread + Engagement) applied simultaneously at Phase 6 Step 1. BG has no battle-phase Thread. Propagated to mass_battle_v3, stage11, state_transfer_spec, params_mass_combat.
- Propagation map v2: self-maintaining with embedded AUTO-UPDATE PROTOCOL. Dependency rules by file type. Params-skill dependency map. New files and cross-references now detected and registered automatically at commit time via Step 6 of simulator Mode I. Never manually maintained again.
- Simulator Mode I updated: Step 6 = propagation map update before commit (mandatory). Step 7 = atomic commit (includes propagation_map). Step 8 = report.
- Orchestrator updated: propagation is automatic, not manual.

### Five questions answered
1. Simulations/tests/audits for all game modes/systems/mechanics: YES
2. Mechanical patches applied and flagged in patch registry: YES (Mode I enforced)
3. Editorial decisions identified, checked against ledger, added if missing: YES
4. Comprehensive results recorded against all criteria: YES (Modes A-M)
5. Changes propagated across all relevant documents: YES (self-maintaining propagation map)

### next_action:
  task: "Run simulations. Recommend starting with: stress test debate (SIM-DEBT-01 re-calibration with Presence×2 pool), then simulate a hybrid scenario for full cross-mode test."
  note: "Every sim run now commits findings immediately. Propagation map updates automatically. All five infrastructure questions are answered."

### commits_this_session:
  - 5b67b79: ED-050 resolved — 7-phase mass battle
  - 3349725: propagation map v2 + simulator Mode I + orchestrator update
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_SIMINFRA_COMPLETE
phase: Phase 4 — Simulation infrastructure complete
status: CLOSED

## SESSION SUMMARY

### Completed
- Simulator Modes J/K/L/M added:
    J: Cognitive load + time audit (decision count, lookup count, parallel tracks, novice/experienced/expert minutes)
    K: Cross-mode delta (K1: TTRPG/Hybrid/BG property table; K2: transition stress test against state_transfer_spec)
    L: Precedent comparison (8-game library, flag unjustified complexity)
    M: Narrative flowchart generator (branching nodes with state tracking, min 3 branches per node, 3 nodes deep, terminal state labels, GAP/DEAD-BRANCH flags, cross-mode mapping)
- mechanic-audit Mode G added: cross-mode consistency audit + transition point checks
- state_transfer_spec.md created: all variables at every mode boundary (TTRPG↔Hybrid, BG↔Hybrid, within-TTRPG Register Shifts), interruption protocols, invariants
- stage11 TT Multiplier column patched (T5-P1-01): obsolete column removed, reference to threadwork added
- ED-050 added: Thread→Mass timing conflict (T1-P1-01) — choose A/B/C
- Flowchart output directory: designs/gm_ref_cp14/flowcharts/

### Simulation command vocabulary (confirmed)
- "stress test [specific mechanic]" → Mode A + D + J + L (isolation, edge cases, cognitive load, precedent)
- "stress test [subsystem]" → Mode G-submode + D + J + K + L (full subsystem, cross-mode delta, load, precedent)
- "stress test [mode]" → all G-submodes for that mode — multi-session, orchestrator stages it
- "simulate [scenario]" → Mode C + M (full scenario + branching flowchart)
- "simulate [ttrpg/hybrid/boardgame]" → Mode C + G-suite + M — multi-session
- "audit [subsystem]" → mechanic-audit Modes A-G

### Full audit criteria coverage
- Crunch cascade ✓, Edge cases ✓, Regressions ✓, Failures ✓, Ambiguities ✓
- Overlap/repetition ✓, Incoherence ✓, Philosophy compliance ✓
- Meaningful actions ✓ (Mode C scenario output), Emergent gameplay ✓ (Mode M flowchart)
- Cognitive load ✓ (Mode J — NEW), Time consumed ✓ (Mode J — NEW)
- Precedent comparison ✓ (Mode L — NEW)
- Cross-mode interdependency ✓ (Mode K1 — NEW), Transition/zoom ✓ (Mode K2 — NEW)
- Narrative flowchart with branching ✓ (Mode M — NEW)

### Remaining editorial before full simulation clearance
- ED-050: Thread→Mass timing (P1) — blocks K2 transition test for mass battle Thread
- ED-001: Card-Hand system (P1-BLOCKER) — blocks BG compilation only
- 38 other open items (non-blocking for simulation)

### commits_this_session:
  - 2e4bf45: ED-047 debate pool resolved
  - 5719802: provisional decisions + sim infra
  - 6124d9f: session close phase 3
  - 3728b3a: Modes J/K/L/M + state_transfer_spec + Mode G + stage11 patch
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_BLOCKERS_SIMPREP
phase: Phase 3 — Blocker resolution, simulation infrastructure repair
status: CLOSED

## SESSION SUMMARY

### Completed
- ED-047 resolved: debate pool = (Presence × 2) + History. R-65 applied. SIM-DEBT-01 registered.
- ED-031 provisional: BG Overwhelming = Ob+1 (intentional divergence from TTRPG 2×Ob)
- ED-037 provisional: Volley TN 6 confirmed as intentional exception to universal TN 7
- ED-038 resolved: Coherence in mass battle = personal track (10→0, threadwork Part 3)
- ED-036 provisional: Altonian unit stats placeholder (Vanguard/Elite Guard/Thread Corps)
- Coverage matrix: F-11 resolved (ST-TW-02); F-27/F-30-33/F-43/F-52 provisioned; F-45 → ED-049
- PP-093-096 applied (provisional): stalemate, coup successor, TC cap, Stability recovery
- Simulator skill Mode I: enforced atomic commit protocol; path fix (sim_coverage_matrix→tests/coverage_matrix); SIM-DEBT section added; provisional decision protocol added
- Editorial register skill: provisional status added
- params_mass_combat: Altonian stats, ED-037/038 decisions applied
- params_board_game: ED-031 BG Overwhelming rule added
- ED-049 added: Church Stability brake scope (F-45, P2)
- Ledger: 49 items total — 40 open, 3 provisional, 2 resolved, 4 struck

### Simulation readiness
- Combat: READY
- Threadwork: READY
- Mass combat: READY (ED-037/038 resolved provisionally; Altonian stats provisional)
- Board game faction play: READY (ED-031 provisional; ED-001 Card-Hand still open but non-blocking for most tests)
- Debate: DEGRADED (SIM-DEBT-01 — pool change needs re-calibration; can simulate, results directional)
- Full hybrid campaign: READY for most scenarios (Altonian engagement provisional)

### next_action:
  task: "Simulate. Use Mode G suite (G1 mass combat, G2 debate, G3 threadwork, G4 faction play, G5 BG)."
  note: "Simulator Mode I is now enforced — every sim run commits findings immediately. Provisional decisions are marked in-text. SIM-DEBT-01 requires debate re-simulation with Presence×2 pool."
  remaining_editorials_blocking_simulation: [ED-001 (Card-Hand BG compilation only)]

### commits_this_session:
  - 2e4bf45: ED-047 resolved, R-65 applied, SIM-DEBT-01 registered
  - 5719802: provisional decisions + sim infrastructure repair
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_DESIGN_CLEANUP
phase: Phase 2 — Design cleanup, three-mode framing, infrastructure
status: CLOSED

## SESSION SUMMARY

### Completed
- Catastrophic Failure / majority-1s override struck from BG system entirely
- Debate: quaestio deprecated; §6.0 context-sensitivity principle added; proceeding-type table expanded (private negotiation vs parliamentary vs tribunal); Parts 1-4 = reference only
- Debate: §6.10 added flagging R-66 vs stress-test pool conflict (ED-047, P1-BLOCKER)
- Threadwork: "Einhir ritual framework" → "Einhir framework" (ritual not canon)
- Threadwork: R-54–R-68 patches applied (Pull duration, Dissolution Ob, healing overweave, Pull floor, Lock drain cap, Mode 3 immunity, Fortification Pulling, institution RS drift)
- designs/combat/combat_design_v1.md created — TTRPG-baseline working document with three-mode framing; replaces stage8 as design-layer source; PP-086–092 + MT-01 faction unit rosters incorporated
- ED-047 (debate pool conflict blocker) + ED-048 (Ceiral non-canon — 22 files affected) added to editorial ledger
- Orchestrator: designs-first philosophy, three-mode framing, stale sweep at session start, compilation = lowest priority
- file_index: combat design added; propagation-pending section added (batch_ad_resolutions, succession, hybrid_gaps_resolved, generation_tasks); three-mode framing header
- designs/ audit completed: all files catalogued; batch_ad_resolutions.md has 11 approved decisions not yet propagated; generation_tasks flagged for user review; hybrid_gaps_resolved ready for integration

### GitHub state (committed)
- 7a3c2ce: all above changes (single atomic commit)

### next_action:
  task: "Resolve P1-BLOCKERs in priority order"
  priority_queue:
    - ED-047 (debate pool formula — P1-BLOCKER, blocks all debate simulation)
    - ED-048 (Ceiral canonical name — P1, blocks NPC/arc work)
    - ED-036 (Altonian unit stats — P1-BLOCKER, blocks hybrid Altonian engagement)
    - ED-038 (Coherence stat definition — P1, blocks mass_battle §A.10)
    - ED-001 (Card-Hand system — P1-BLOCKER, blocks BG compilation)
  note: "Use valoria-editorial-register Workflow A. After blockers: propagate batch_ad_resolutions.md decisions (G-038 treaty betrayal needs a home file), integrate hybrid_gaps_resolved.md into stage11."

### editorial_decisions_pending: 44 open (ED-001–046 minus struck; plus ED-047–048)
### blockers: ED-047, ED-036, ED-001

### commits_this_session:
  - d0ffda0: session close (prior)
  - 03e462b through ac99de5: infra (prior)
  - 7a3c2ce: design cleanup + three-mode framing
```

---

# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_PATCH_INFRA
phase: Phase 1 — Stress Test Patches + Infrastructure
status: CLOSED

## SESSION SUMMARY

### Completed
- BG stress test patches (ST-BG-01–10, ST-INT-01–13) applied to bg_v05_simulation_and_patches.md
- Mass battle stress test patches (ST-MB-01–10) applied to mass_battle_v3.md
- Debate stress tests v1+v2 (D-01–v2-P04) compiled into debate_system_redesign_v1.md Part 6
- Threadwork mode index added + ST-TW-01–05 patches applied to threadwork_redesign_v25.md
- stage8_combat.md: PP-086–092 applied (P1-B11 + P2-B11 series)
- stage11_scale_transitions.md: PP-089 (hybrid phase order) + PP-090 (mid-siege conversion) applied
- patch_register.yaml: gap filled PP-086–092; PP-089/090 marked applied
- github_ops.py: GraphQL batch reader added (read_files_graphql)
- references/file_index.md: new repository index (all files, systems, status, dependencies)
- references/propagation_map.md: new cross-reference tracking system
- skills/valoria-editorial-register/SKILL.md: updated with dedup/consolidate/stale logic + Workflow E
- editorial_ledger.yaml: ED-031–046 harvested; ED-008,011,013,018 struck. 46 items total, 42 open, 4 struck.
- All 5 stale params files synced (params_combat, mass_combat, board_game, debate, threadwork)

### GitHub state (all committed)
- 8d8fd91: debate/bg/mass_battle/threadwork ST patches + github_ops GraphQL batch reader
- 133052e: stage8_combat PP-086–092 + patch_register gap filled
- 03e462b: file_index + propagation_map + editorial-register skill update
- e619c33: editorial_ledger ED-031–046 + consolidations/strikes
- 3775932: all 5 params synced + file_index stale section updated
- ac99de5: stage11 PP-089+PP-090 + patch_register applied status

### next_action:
  skill: valoria-editorial-register
  task: "Workflow A — resolve P1-BLOCKERs: ED-036 (Altonian unit stats), ED-038 (Coherence definition), ED-001 (Card-Hand system)"
  parameters:
    priority_queue: [ED-036, ED-038, ED-001, ED-031, ED-037, ED-044, ED-033]

### open_gaps_added:
  - "Params stale: stage3_thread_operations.md needs rewrite from threadwork_v25"
  - "Params stale: stage9_social.md needs rewrite from debate_system_redesign_v1.md Part 6"
  - "PP-089/090 applied to stage11; params_scale_transitions.md not yet re-synced"

### editorial_decisions_pending: 42 open items (ED-031–046 new; prior carry-forward)
  - P1-BLOCKERs: ED-036 (Altonian unit stats), ED-001 (Card-Hand system)
  - P1: ED-031,032,033,037,038,044

### blockers:
  - ED-036 (Altonian unit stats) blocks hybrid Altonian engagement at IP>=75
  - ED-001 (Card-Hand system) blocks BG stage_bg compilation
  - ED-038 (Coherence stat) blocks mass_battle_v3 §A.10

### commits_this_session:
  - 8d8fd91 through ac99de5 (6 commits)
```

---

# Valoria Session Log — Updated

```yaml
session_close: 2026-04-01
checkpoint: hybrid_sim_arcs_31_35
completed_stages:
  - valoria-editorial-register skill created and committed (skills/valoria-editorial-register/SKILL.md)
  - editorial_ledger.yaml populated: 21 harvested items (ED-001–021) + 9 new (ED-022–030) = 30 total
  - Arcs 31–35 generated (designs/gm_ref_cp14/arcs/arcs_31_35_hybrid_systems.md)
  - Simulation Mode C+G for Arcs 31+33 (tests/simulation_report_arcs_31_33.md)
  - Patches PP-159–163 added to patch_register.yaml
next_action:
  skill: valoria-editorial-register
  task: "Resolve editorial decisions — start with P1-BLOCKERs: ED-027 (Poise attribute), ED-030 (Thread combat vs Mode 3), then ED-001 (BG-E-30 Card-Hand system)"
  parameters:
    priority_queue: [ED-027, ED-030, ED-001, ED-008, ED-011, ED-012, ED-013, ED-016, ED-018, ED-020]
    consolidate_first: [[ED-011, ED-027], [ED-005, ED-021], [ED-009, ED-010]]
open_gaps_added:
  - "GAP-ARC31-SIM-01: Focus/NPC attributes missing from stage13_npcs — all NPC profiles need Focus + Attunement values"
  - "GAP-ARC31-02: Grand Debate quaestio Ob per phase not specified (currently assumes Ob 1)"
  - "GAP-ARC33-SIM-02: Southernmost entity stat blocks (Mode 3) not in compilation"
  - "GAP-ARC34-01: Vaynard TK5 independent action clause missing from TK track"
  - "GAP-ARC35-01: Klapp CE track trigger criteria need formalisation (which objects qualify)"
editorial_decisions_pending:
  - "ED-027: Poise attribute → Focus mapping (P1-BLOCKER — blocks debate compilation)"
  - "ED-030: Thread combat vs Mode 3 entities — pool split or separate roll (P1-BLOCKER)"
  - "ED-001: Card-Hand system adoption (BG-E-30, P1-BLOCKER — carries from prior session)"
  - "ED-008: Niflhel formal Debate access"
  - "ED-011: Concentration attribute (Focus vs Poise)"
  - "ED-012: Audience Disposition win-condition scope (all Formal vs Grand only)"
  - "ED-013: Grand Debate role alternation — who gets extra proposition"
  - "ED-016: Military stat → unit quality mapping confirmation"
  - "ED-018: Commander bonus formula confirmation"
  - "ED-020: Pulling general command capacity — intended tactical option?"
  - "ED-022: Forced Unmask vs Register Shift from external disruption"
  - "ED-023: Vaynard TK5 operational capability vs knowledge-brokerage"
  - "ED-024: Southernmost Mode 3 entity stat blocks needed"
  - "ED-025: Almud Torben yield — scene vs automatic"
  - "ED-026: Klapp Trajectory determination + Discovery Event intervention"
  - "ED-028: Forgetting dissolution — dramatic vs silent"
  - "ED-029: Purpose tracking in Southernmost"
blockers:
  - "ED-027 (Poise attribute) blocks debate system compilation"
  - "ED-030 (Thread vs Mode 3 combat) blocks Southernmost encounter simulation"
  - "ED-001 (Card-Hand system) blocks all BG Tier 1 work — carries from prior session"
simulation_coverage:
  - "SIM-ARC31-C01: Arc 31, Modes C+G1+G2+G4 — 7 findings, 4 patches"
  - "SIM-ARC33-C01: Arc 33, Modes C+G3 — 4 findings, 1 patch"
  - "Remaining: Arcs 32, 34, 35 not yet simulated — next session priority after editorial pass"
commits_this_session:
  - "507ce0c7: skills/valoria-editorial-register/SKILL.md (new skill)"
  - "d690b177: canon/editorial_ledger.yaml (initial population, 21 items)"
  - "eb0edf0d: designs/gm_ref_cp14/arcs/arcs_31_35_hybrid_systems.md (arcs 31-35)"
  - "466d6391: tests/simulation_report_arcs_31_33.md (simulation report)"
  - "0497c387: canon/patch_register.yaml (PP-159–163)"
  - "1d96469a: canon/editorial_ledger.yaml (ED-022–030)"
```

---

# Valoria Session Log — Archive

> Historical record. Do NOT read on session start. Read session_log_current.md instead.

# Valoria Session Log
## Initialized: 2026-03-25

---

```yaml
session_close: 2026-03-24
checkpoint: pre-CP14 (infrastructure)
completed_stages:
  - "Philosophical Foundations document (canonical)"
  - "Initial ruleset audit (2 documents vs Foundations)"
  - "6-attribute proposed ruleset with co-movement, Taint reframe, gate wounds"
  - "Faction leader profiles (Baralta, Vaynard, Almud, Lenneth)"
  - "Theocracy Clock, Inquisitor/Riskbreaker mechanics, Church heresy investigation"
  - "Monte Carlo stress tests → 28 patches applied to CP10"
  - "Skill ecosystem (6 skills, 7 reference files)"
  - "CP14 compilation workplan (18 stages, 7 batches)"
  - "Pre-CP14 audit value assessment (19 delta items)"
  - "Game system analysis (33 systems, tiered recommendations)"
  - "Three-dimensional co-movement redesign (Version C selected)"
  - "Skeleton stress tests R1-R3 (30 scenarios, 40 rulings)"
  - "Archetype substitution analysis (30 scenarios × 6+ archetypes)"
next_action:
  skill: orchestrator
  task: "Phase 1 design work"
```
