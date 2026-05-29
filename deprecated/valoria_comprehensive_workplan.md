<!-- DEPRECATED: 2026-04-09 — SUPERSEDED BY session_log + orchestrator skill. Do not use as a mechanical reference. Retained for audit trail only. -->

# VALORIA — COMPREHENSIVE WORKPLAN
## Replaces: valoria_cp14_compilation_workplan.md
## Date: 2026-03-25
## Output: Complete TTRPG ruleset + Complete board game ruleset

---

# SCOPE

Design, test, consolidate, and compile two complete rulesets from a shared mechanical foundation:
1. **TTRPG ruleset** — character-driven political drama with tactical combat and Thread metaphysics
2. **Board game ruleset** — faction-strategy game with mass combat, hex map, and political negotiation

Both share: faction stats, three clocks, Thread consequences, co-movement principles, setting, philosophical foundations.

Each has mode-specific mechanics that do not cross over.

---

# PROJECT STATUS

**Canonical status document:** `valoria_scope_map.md` (root level)

Tracks: all systems inventory, simulation coverage per system, open gaps and pending patches per system, critical blockers, and prioritized audit plan. Updated at every session close and after any simulation, gap register change, or patch propagation. Consult this file first when asking "where do we stand."

---

# AUTHORITY HIERARCHY (unchanged)

1. Valoria_Philosophical_Foundations.docx — governs everything
2. Mechanics.docx — original design intent
3. Editorial decisions (this workplan + session logs)
4. Simulation-tested patches and rulings (R1–R40, A–S, D-01–D-19)
5. Source documents — draw content in this priority order:
   1. In-session editorial decisions
   2. Batch A–F designs
   3. Documents newer than CP13:
      - valoria_comprehensive_workplan.md
      - valoria_cp14_compilation_workplan.md
      - valoria_stress_tests_round2.md / valoria_stress_tests_round3_hybrid.md
      - hybrid_register.md
      - valoria_archetype_substitution_analysis.md
      - valoria_three_dimensional_comovement.md
      - valoria_audit_value_and_systems_analysis.md
   4. CP13
   5. CP12, CP08–CP10, v3, COMPLETE (supplementary content only)

---

# CONFIRMED EDITORIAL DECISIONS

| Decision | Resolution | Date |
|----------|-----------|------|
| Attribute count | 10 (Agi, End, Str, Cog, Mem, Focus, Att, Bonds, Pres, Spirit) | 2026-03-25 |
| Combat architecture | Pool split offence/defence (SoS-inspired) | 2026-03-25 |
| Action economy | Pool split IS the action economy | 2026-03-25 |
| Round structure | Phase-based, priority list, 6-10s segments | 2026-03-25 |
| Movement + attack | Permitted; pure movement faster | 2026-03-25 |
| Reach resolution | Correct-range before wrong-range; same-reach simultaneous | 2026-03-25 |
| Weapon TN mapping | Light 5/6, Medium 6/7, Heavy 7/8 (attack/parry) | 2026-03-25 |
| Co-movement system | Version C (automatic deterministic + actual d6) | 2026-03-24 |
| Circles/Resources | Tied to Histories + factions; improvable and degradable | 2026-03-25 |
| Board game map | Hexes | 2026-03-25 |
| TTRPG map | Zones (theater of mind) | 2026-03-25 |
| Mode-specific rules | Permitted where dual-mode would be incoherent | 2026-03-25 |
| Endgame | Board: explicit victory conditions. TTRPG: emergent. Hybrid: both. | 2026-03-25 |
| Ethical frameworks | Gravitational tendency per faction + messy deviation; not labeled | 2026-03-25 |
| Faction leader ≠ faction | Two mechanical layers: institutional tendency + leadership friction | 2026-03-25 |

---

# PHASE STRUCTURE

## Phase 1: DESIGN (fill gaps)
## Phase 2: COMPILE (assemble into single documents)
## Phase 3: TEST (rigorous stress testing of compiled systems)
## Phase 4: CONSOLIDATE (cut, merge, simplify based on test evidence)
## Phase 5: FINAL COMPILE (clean ruleset production)

---

# PHASE 1: DESIGN

Goal: resolve all 38 "Design needed" gaps. Produce design briefs for each, organized into design batches.

## Design Batch A — TTRPG Core Gaps (prerequisite for compilation)

| Gap | Design Task | Estimated Tokens |
|-----|-----------|-----------------|
| G-053 | CP spending menu: what CP buys beyond current list (new Inspirations, Knots, Histories) | 500 |
| G-040 | Inspiration acquisition + recovery mid-campaign | 500 |
| G-054 | Circles/Resources redesign: History-based, faction-linkable, degradable | 800 |
| G-048 | Resources degradation on failed rolls (BW tax model) | 300 |
| G-034 | Fortification / base building | 500 |
| G-047 | Siege mechanic (port + adapt from VG doc) | 600 |
| G-052 | Player/GM transition reference guide | 800 |

**Batch A total: ~4,000 tokens. Dependencies: none. Can start immediately.**

## Design Batch B — TTRPG Military Gaps

| Gap | Design Task | Estimated Tokens |
|-----|-----------|-----------------|
| G-033 | Army levy / mustering from territories | 600 |
| G-035 | Officer recruitment + caps + maintenance costs | 500 |
| G-036 | Defection / cross-faction recruitment procedure | 400 |
| G-046 | Unit composition / formation mechanics | 800 |
| G-056 | Supply lines / logistics | 400 |
| G-045 | Knights Templar organizational mechanics | 500 |

**Batch B total: ~3,200 tokens. Dependencies: G-029 (territory differentiation). Can parallel with Batch A.**

## Design Batch C — TTRPG Political Gaps

| Gap | Design Task | Estimated Tokens |
|-----|-----------|-----------------|
| G-041 | Non-leader faction membership mechanics | 500 |
| G-042 | Faction creation by players | 600 |
| G-043 | NPC faction elevation to PC status | 400 |
| G-038 | Alliance / treaty / betrayal mechanics | 600 |
| G-039 | Casus belli / war justification | 500 |
| G-037 | Territory governance after conquest | 500 |
| G-044 | Altonian presence pre-invasion | 600 |
| G-055 | Southernmost expedition procedures | 500 |

**Batch C total: ~4,200 tokens. Dependencies: none. Can parallel with A and B.**

## Design Batch D — Faction Identity (shared across modes)

| Gap | Design Task | Estimated Tokens |
|-----|-----------|-----------------|
| G-019 | Ethical framework tendencies per faction (7 factions × 7 frameworks) | 1,500 |
| G-020 | Faction leader vs institution mechanical separation (7 factions) | 1,000 |
| G-032 | Asymmetric faction powers (unique mechanics per faction) | 1,500 |
| G-022 | Nine political axes as gameplay generators | 800 |

**Batch D total: ~4,800 tokens. Dependencies: none but requires heaviest editorial involvement. [EDITORIAL throughout.]**

## Design Batch E — Board Game (design from scratch)

| Gap | Design Task | Estimated Tokens |
|-----|-----------|-----------------|
| G-027 | Player count + faction assignment | 300 |
| G-025 | Order Set (menu of available actions) | 1,000 |
| G-026 | Turn structure (complete round procedure) | 800 |
| G-059 | Simultaneous order placement procedure | 400 |
| G-060 | Resolution phase ordering | 400 |
| G-029 | Territory differentiation (15 territories with properties) | 1,200 |
| G-028 | Victory conditions per faction | 800 |
| G-030 | Component specification | 600 |
| G-031 | NPC AI expansion | 600 |
| G-050 | Event deck / world event system | 800 |
| G-049 | Negotiation / deal mechanics | 500 |
| G-051 | Season wheel / seasonal differentiation | 300 |
| G-057 | Thread operations (simplified faction-card procedure) | 500 |
| G-058 | Reach as board game stat | 300 |

**Batch E total: ~8,500 tokens. Dependencies: Batch D (faction identity must be designed before board game faction cards). This is the largest batch.**

## Design Batch F — Hybrid + Endgame

| Gap | Design Task | Estimated Tokens |
|-----|-----------|-----------------|
| G-018 | Hybrid timing reference table | 600 |
| G-021 | Endgame conditions (all three modes) | 800 |
| G-023 | Mode-specific rule branching catalogue | 400 |

**Batch F total: ~1,800 tokens. Dependencies: Batches A–E complete.**

### Phase 1 Summary

| Batch | Gaps | Tokens | Dependencies | Editorial |
|-------|------|--------|-------------|-----------|
| A (TTRPG core) | 7 | 4,000 | None | Low |
| B (TTRPG military) | 6 | 3,200 | G-029 | Low |
| C (TTRPG political) | 8 | 4,200 | None | Moderate |
| D (Faction identity) | 4 | 4,800 | None | **High** |
| E (Board game) | 14 | 8,500 | Batch D | Moderate |
| F (Hybrid + endgame) | 3 | 1,800 | A–E | Low |
| **Total** | **42** | **~26,500** | | |

**Estimated sessions for Phase 1: 4–6 (depending on editorial decision batching)**

---

# PHASE 2: COMPILE

Goal: assemble all approved designs + existing resolved mechanics + 40 rulings + 19 delta patches + Version C co-movement into two documents.

## TTRPG Compilation (18 stages from original workplan, revised)

Stages 1–16 from original CP14 workplan, updated per revision memo:
- Stage 1: Core engine (10 attributes, pool split combat, variable TN)
- Stage 2: Characters (Histories, Beliefs, Inspirations, TS, CD, Knots, Circles/Resources redesign)
- Stage 3: Thread operations (Version C co-movement, History Resonance, Flashback anchoring)
- Stage 4: Southernmost (Forgetting, Extraordinary Weaving, expedition procedures)
- Stage 5: Clocks (TT/TC/IP, threshold events, interaction rules)
- Stage 6: Factions (7 factions with asymmetric powers, ethical tendencies, leader separation)
- Stage 7: Territories (zone-based for TTRPG, territory properties shared with board game)
- Stage 8: Combat (pool split, priority, reach, movement, formations, siege, maneuvers)
- Stage 9: Social (Debate, Appeal, rhetoric styles, Composure, Reading Exchange)
- Stage 10: Advancement (CP menu, test track, Inspiration acquisition, Renown)
- Stage 11: Scale transitions (8 handoff rules, transition reference guide)
- Stage 12: Campaign modes (TTRPG session structure, hybrid timing table)
- Stage 13: NPCs + institutional actors (stat blocks, Inquisitors, Riskbreakers, Templars)
- Stage 14: GM tools (Session Zero, rendering engine, co-movement reference, Ob guide)
- Stage 15: Equipment (weapons, armor, Thread-locked items, dissolution residue objects)
- Stage 16: Reference materials (cards, glossary, examples, character sheet)

Plus:
- Stage 17: Canon guard pass
- Stage 18: Compilation report

**Estimated TTRPG compilation tokens: ~50,000 (up from 45K due to new content)**

## Board Game Compilation (new, 10 stages)

- Stage B1: Overview + setup (player count, faction assignment, component list, board description)
- Stage B2: Territory map (15 territories with hex layout, properties, connections, starting control)
- Stage B3: Faction cards (7 factions: stats, unique power, Order Set, Thread capability, victory condition)
- Stage B4: Turn structure (complete round from planning → resolution → accounting)
- Stage B5: Orders (full Order Set with resolution procedures per order type)
- Stage B6: Military (unit types, mustering, movement, combat using disposition table, siege, supply)
- Stage B7: Thread operations + co-movement (simplified faction-card procedure, TT management)
- Stage B8: NPC AI (expanded decision trees per NPC faction)
- Stage B9: Event deck (world events triggered by clock thresholds + random events)
- Stage B10: Victory + endgame (per-faction victory conditions, shared TT survival condition, scoring)

**Estimated board game compilation tokens: ~20,000**

### Phase 2 Summary

| Document | Stages | Estimated Tokens | Sessions |
|----------|--------|-----------------|----------|
| TTRPG ruleset | 18 | ~50,000 | 5–7 |
| Board game ruleset | 10 | ~20,000 | 2–3 |
| **Total** | **28** | **~70,000** | **7–10** |

---

# PHASE 3: TEST

Goal: rigorous stress testing of BOTH compiled rulesets. Every mechanic tested for crunch cascade, edge cases, regressions, failures, ambiguities, overlap, time consumed, incoherence, cognitive load, meaningful actions, and emergent gameplay.

## Test Protocol

Every test evaluates ALL of the following dimensions:

| Dimension | Question |
|-----------|----------|
| **Crunch cascade** | Does this mechanic create infinite regressions, undefined states, or exponential formula interactions? |
| **Edge cases** | What happens at boundary values (0, max, simultaneous triggers)? |
| **Regressions** | Does this mechanic break something that previously worked? |
| **Failures** | What happens when the mechanic fails? Is failure interesting or just punitive? |
| **Ambiguities** | Can two reasonable readers interpret this rule differently? |
| **Overlap / repetition** | Does this mechanic duplicate the function of another mechanic? |
| **Time consumed** | How many minutes does this mechanic add to a round/scene/session/season? |
| **Incoherence** | Does this mechanic contradict another mechanic, the Foundations, or design intent? |
| **Cognitive load** | How many things must a player/GM hold in working memory to use this? |
| **Meaningful actions** | Does this mechanic produce decisions that matter, or is it busywork? |
| **Emergent gameplay** | Does this mechanic create unexpected but interesting situations when combined with others? |
| **Philosophy compliance** | Does this mechanic satisfy all 14 canon constraints? |

## TTRPG Test Suite

### Round 1: Isolation Tests
Test each major mechanic in isolation (no interactions). Covers the full 56-mechanic coverage matrix, 4 test modes each = 224 cells.

### Round 2: Interaction Tests
Test mechanic pairs and triples that share resources, triggers, or timing. Priority: combinations identified in skeleton stress tests R1–R3 that were tested against the OLD system and need re-validation against the compiled system.

### Round 3: Scenario Tests
Full multi-round, multi-scale scenarios with complete character and faction state. Minimum 10 scenarios covering:
- Pure personal (investigation, social, combat)
- Pure faction (seasonal accounting, Domain Actions, clock thresholds)
- Cross-scale (personal → faction cascade, faction → personal imposition)
- Hybrid (personal + faction simultaneous)
- Endgame (high TT, faction consolidation, alliance formation)

### Round 4: Archetype Substitution
Re-run all Round 3 scenarios with character-type swaps (practitioner, faction leader, inquisitor, riskbreaker, templar, non-affiliated). Minimum 6 archetypes × 10 scenarios = 60 evaluations.

### Round 5: Campaign Simulation
Simulate a 20-season campaign at compressed resolution. Track all clock movements, faction stat changes, character advancement, and identify:
- When do clocks converge or diverge?
- When does the game become unmanageable?
- What's the cognitive load at season 1 vs season 10 vs season 20?
- Where do players run out of meaningful decisions?

## Board Game Test Suite

### Round B1: Solo Faction Playthrough
Play one faction through 5 seasons against NPC AI. Test: order selection, resolution, accounting, clock behavior.

### Round B2: Multi-Faction Interaction
Simulate 3-player, 4-player, 5-player configurations. Test: simultaneous order conflicts, negotiation, military engagement, Thread operations.

### Round B3: Edge Case Scenarios
- All three clocks cross thresholds simultaneously
- Faction collapse + reconstitution
- TT reaches 100 (Rupture)
- Single faction controls all territories
- Two factions ally against one

### Round B4: Endgame Scenarios
Test all per-faction victory conditions for: achievability, timing, counter-play, interaction with shared TT survival condition.

### Round B5: Time/Complexity Calibration
Time a full 20-season game at each player count. Target: 180–300 minutes for a full campaign. If longer: identify what to cut. If shorter: identify what's too shallow.

## Cross-Mode Tests

### Round X1: TTRPG ↔ Board Game State Transfer
Verify that faction stats, clock positions, and territory control can transfer between modes without information loss. Test hybrid session where first half is TTRPG and second half is board game.

### Round X2: Board Game → TTRPG Zoom
Simulate a board game session that triggers a TTRPG zoom-in (personal combat during mass battle, social scene during political crisis). Test the transition procedure.

### Phase 3 Summary

| Test Suite | Tests | Coverage |
|------------|-------|----------|
| TTRPG R1 (isolation) | 224 cells | All 56 mechanics × 4 modes |
| TTRPG R2 (interaction) | ~60 pairs | Priority combinations |
| TTRPG R3 (scenarios) | 10 | Full-state multi-scale |
| TTRPG R4 (archetypes) | 60 | Substitution across R3 |
| TTRPG R5 (campaign) | 1 | 20-season compressed |
| Board game R-B1–B5 | ~20 | Solo, multi, edge, endgame, timing |
| Cross-mode X1–X2 | 5 | Transfer and zoom |
| **Total** | **~380** | |

**Estimated sessions for Phase 3: 6–10**

---

# PHASE 4: CONSOLIDATE

Goal: review all test findings. Cut, merge, or simplify mechanics that failed testing. Resolve all consolidation candidates (G-061 through G-065).

## Consolidation Criteria

A mechanic is CUT if:
- It produced crunch cascades in ≥2 test scenarios
- Players/GM never used it across ≥3 scenario tests
- It duplicates another mechanic's function with no added value
- Its cognitive load exceeds its gameplay contribution

A mechanic is MERGED if:
- Two mechanics track the same thing with different numbers
- Two mechanics occupy the same decision space but trigger differently

A mechanic is SIMPLIFIED if:
- Its resolution takes >2 minutes in testing
- It requires >3 pieces of information held in working memory
- Its edge cases outnumber its standard cases

## Consolidation Candidates (pre-flagged)

| ID | Candidate | Test to resolve |
|----|-----------|----------------|
| G-061 | Momentum vs Push | Which do players use more? Does cutting one reduce tactical depth? |
| G-062 | Maxims vs Beliefs | Do Maxims generate different play than Beliefs? |
| G-063 | Impression Track vs Knots | Are both needed for NPC relationships? |
| G-064 | Renown vs CP | Does Renown produce decisions CP doesn't? |
| G-065 | Taint + CD + Certainty | Can a practitioner track all three without confusion? |

**Estimated sessions for Phase 4: 1–2**

---

# PHASE 5: FINAL COMPILE

Goal: produce clean, complete, final rulesets incorporating all Phase 4 decisions.

## Deliverables

1. **Valoria TTRPG Ruleset** — single markdown document, fully playable, canon-guard passed
2. **Valoria Board Game Ruleset** — single markdown document, fully playable, component-specified
3. **Hybrid Mode Supplement** — timing table, transition guide, state transfer procedure
4. **GM Quick Reference** — 2-page transition guide, Ob reference, co-movement reference
5. **Player Quick Reference** — 1-page core rules, character sheet template
6. **Gap Register — Final** — all items closed or explicitly deferred with rationale
7. **Patch Log — Final** — all changes tracked with approval status
8. **Canon Guard Report** — all 14 constraints verified against final rulesets

**Estimated sessions for Phase 5: 3–5**

---

# SKILL REQUIREMENTS

## Existing Skills (update needed)

| Skill | Update Required |
|-------|----------------|
| valoria-orchestrator | Add Phase 1–5 workflow routing; add board game mode; add consolidation protocol |
| valoria-chunker | No update needed |
| valoria-canon-guard | Update P-01/P-05/P-11/P-14 violation tests for Version C + Mode 2 |
| valoria-mechanic-audit | Add board game audit mode; add consolidation candidate detection |
| valoria-simulator | Add board game simulation mode; add 11-dimension test protocol; add campaign simulation mode |
| valoria-compiler | Add board game compilation mode; add cross-mode state transfer verification |

## New Skills Needed

| Skill | Purpose | Model |
|-------|---------|-------|
| valoria-board-designer | Board game-specific design: order sets, turn structure, victory conditions, component spec, NPC AI, event deck | Sonnet |
| valoria-consolidator | Post-test consolidation: identify cuts, merges, simplifications based on test evidence against criteria | Sonnet |

**Total skills: 8 (6 updated + 2 new)**

---

# EXECUTION ORDER

| Phase | Sessions | Blockers |
|-------|----------|----------|
| 1A–C (TTRPG gaps) | 2–3 | None — can start now |
| 1D (Faction identity) | 1–2 | Editorial involvement throughout |
| 1E (Board game) | 2–3 | Batch D must be complete |
| 1F (Hybrid + endgame) | 1 | A–E must be complete |
| 2 (Compile TTRPG) | 5–7 | Phase 1 complete |
| 2 (Compile board game) | 2–3 | Phase 1 complete |
| 3 (Test TTRPG) | 4–6 | TTRPG compiled |
| 3 (Test board game) | 2–4 | Board game compiled |
| 3 (Cross-mode) | 1 | Both compiled |
| 4 (Consolidate) | 1–2 | Phase 3 complete |
| 5 (Final compile) | 3–5 | Phase 4 complete |
| **Total** | **~24–40 sessions** | |

---

# CONTEXT MANAGEMENT

Each session:
1. Read session log → confirm task → execute
2. Checkpoint after each completed stage
3. If context limit approaching: complete current stage → session-close YAML → instruct new chat
4. All intermediate work as tables, not prose
5. All final outputs as .md files
6. Chunk all inputs >500 lines before analysis

Session handoff format:
```yaml
session_close: YYYY-MM-DD
phase: [1-5]
batch: [A-F or compile stage or test round]
completed: []
next_action:
  skill: name
  task: description
  input: filename
gaps_resolved: []
gaps_opened: []
editorial_pending: []
```

---

# PENDING EDITORIAL DECISIONS

| ID | Decision Needed | Blocks |
|----|----------------|--------|
| G-027 | Board game player count (3? 3–5? 2–7?) | Phase 1E |
| G-024 | Can Lenneth gain TS through archival research? | Phase 2 Stage 13 |
| G-012 | Are Virtues/Vices a separate mechanic or merged into Beliefs? | Phase 2 Stage 2 |
| D-batch | All faction ethical framework mappings | Phase 1D |
| D-batch | All faction asymmetric power designs | Phase 1D |
| D-batch | Faction leader personality/friction designs | Phase 1D |

---

*End of Comprehensive Workplan*
