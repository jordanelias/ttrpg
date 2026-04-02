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

---

```yaml
session_close: 2026-03-25
checkpoint: comprehensive workplan (replaces CP14 workplan)
completed_stages:
  - "Systematic review of all work (2-day audit)"
  - "Gap register reconciliation (17 → 40 items)"
  - "Patch log population (83 tracked changes)"
  - "Canon constraints updated for Version C"
  - "Workplan revision memo"
  - "Session log initialized"
  - "4 blocking editorial decisions resolved (G-003, G-004, G-010, G-017)"
  - "Design intent established: ethical frameworks, endgame, political axes, mode-specific branching"
  - "Circles/Resources editorial: tied to Histories + factions, degradable"
  - "Board game foundational review: identified all missing systems"
  - "Gap register expanded (40 → 82 items, 38 need design from scratch)"
  - "Comprehensive workplan produced (5 phases, 24-40 sessions estimated)"
next_action:
  skill: valoria-orchestrator (update needed)
  task: "Phase 1 Batch A — TTRPG core gap design"
  input: valoria_comprehensive_workplan.md
gaps_resolved:
  - "G-003 (round duration)"
  - "G-004 (pool split)"
  - "G-010 (10 attributes)"
  - "G-017 (action economy)"
gaps_opened:
  - "G-025 through G-065 (40 new gaps from systematic review)"
editorial_pending:
  - "G-027: board game player count"
  - "G-024: Lenneth TS path"
  - "G-012: Virtues/Vices merge"
  - "Batch D: all faction ethical framework mappings"
blockers:
  - "Phase 1E blocked on Phase 1D"
  - "Phase 2 blocked on Phase 1"
```

---

```yaml
session_close: 2026-03-25T02
checkpoint: S3 (gap register consolidated, editorial decisions)
completed_stages:
  - "Gap register consolidated (82 → 108 items)"
  - "22 new hybrid gaps (G-074–G-095)"
  - "5 consolidation candidates pre-resolved (Push cut, Maxims cut, etc.)"
  - "Reach system editorial (Short/Long/Projectile)"
  - "Zone-based combat editorial (TTRPG zones, board game territory-adjacency)"
  - "Board game player count resolved (2-5 + solo)"
  - "Lenneth TS path resolved (scholarly research)"
  - "Virtues & Vices cut"
  - "Hybrid architecture resolved (phase-separated, GM scenario engine)"
  - "Intelligibility system editorial (Taint → 10→0 countdown)"
  - "Faction ethical frameworks assigned (all 7 + sub-groups)"
  - "Fibonacci group bonus confirmed"
next_action:
  skill: orchestrator
  task: "Phase 1 Batch A design — begin comprehensive workplan execution"
  input: valoria_gap_register_consolidated.md + valoria_comprehensive_workplan.md
```

---

```yaml
session_close: 2026-03-25T03
phase: 1
batch: A+B+C+D
completed_stages:
  - "Batch A designed (7 gaps: G-053, G-040, G-054, G-048, G-034, G-047, G-052)"
  - "Batch A editorial resolved: Approach Training 8CP, half-CP refund on Grief failure, single Circles track"
  - "Batch B designed (6 gaps: G-033, G-035, G-036, G-046, G-056, G-045)"
  - "Batch C designed (8 gaps: G-041, G-042, G-043, G-038, G-039, G-037, G-044, G-055)"
  - "Batch C editorial resolved: faction creation = narrative prereqs only, Altonian vassalage valid"
  - "Treaty betrayal mechanic designed: betrayed gets Stability -1 (2 seasons) + casus belli + Grievance Marker; betrayer gets Influence -1 (2 seasons) + Mandate +1 (1 season) + individual Reputation damage"
  - "Batch D designed (4 gaps: G-019, G-020, G-032, G-022 — integrated faction identity packages for all 7 factions)"
  - "Batch D editorial resolved: Private Collection transfers as institutional asset (shocking); Niflhel permanently decentralized"
  - "Nine political axes designed as GM narrative tool (not tracked numerically)"
gaps_resolved_this_session:
  - "G-053 (CP spending menu)"
  - "G-040 (Inspiration acquisition/recovery)"
  - "G-054 (Circles/Resources redesign)"
  - "G-048 (Resources degradation — subsumed into G-054)"
  - "G-034 (Fortification/base building)"
  - "G-047 (Siege mechanic)"
  - "G-052 (Player/GM transition guide)"
  - "G-033 (Army levy/mustering)"
  - "G-035 (Officer recruitment/caps/maintenance)"
  - "G-036 (Defection/cross-faction recruitment)"
  - "G-046 (Unit composition/formation)"
  - "G-056 (Supply lines/logistics)"
  - "G-045 (Knights Templar organization)"
  - "G-041 (Non-leader faction membership)"
  - "G-042 (Faction creation by players)"
  - "G-043 (NPC faction elevation)"
  - "G-038 (Alliance/treaty/betrayal)"
  - "G-039 (Casus belli/war justification)"
  - "G-037 (Territory governance after conquest)"
  - "G-044 (Altonian presence pre-invasion)"
  - "G-055 (Southernmost expedition)"
  - "G-019 (Ethical framework expression — integrated into faction cards)"
  - "G-020 (Leader vs institution — integrated into faction cards)"
  - "G-032 (Asymmetric faction powers — Unique Actions)"
  - "G-022 (Nine political axes)"
gaps_opened:
  - "Löwenritter faction identity (not currently a faction — needs package or sub-faction status)"
  - "Axis 10: Succession (Almud → compromised heir — nature of compromise TBD)"
  - "Named Revolution elder NPC (optional, flagged)"
next_action:
  skill: orchestrator
  task: "Phase 1 Batch E — Board game design (14 gaps). Requires Löwenritter and Succession editorial first."
  input: batch_d_designs.md (faction identity packages as foundation for board game faction cards)
editorial_pending:
  - "Löwenritter: full faction, Crown sub-faction, or officer pool?"
  - "Succession axis: nature of heir's compromise (Niflhel? Thread-sensitive? Church-captured? Other?)"
  - "Named Revolution elder NPC (optional)"
blockers:
  - "Batch E (board game) ready to start — depends on Löwenritter decision"
  - "Batch F (hybrid+endgame) blocked on Batch E"
  - "Phase 2 (compilation) blocked on Phase 1"
output_files:
  - "batch_a_designs.md"
  - "batch_bc_designs.md"
  - "batch_d_designs.md"
```

---

```yaml
session_close: 2026-03-25T05
phase: 1
batch: D (supplement — 8th faction)
completed_stages:
  - "Löwenritter designed as full 8th faction with partial sheet (Military, Stability, Influence, Intelligence)"
  - "Coup trigger mechanic designed (4 conditions, Domain Action roll, attribute transfer from Crown)"
  - "Ethical framework assigned: Deontological Honor Code"
  - "Unique Action designed: Martial Law (with post-coup variant)"
  - "Grandmaster Sigrid Ehrenwall NPC created"
  - "Canon compliance verified (P-01, P-05, P-07, P-14)"
  - "System update requirements documented (faction count, board game, political axes, clock interactions)"
editorial_resolved:
  - "Löwenritter: full 8th faction, partial sheet in peacetime, full sheet on coup"
  - "Löwenritter loyalty: Crown as institution, not monarch"
  - "Church territory: begins holding territories at TC ~80"
  - "Almud's children: daughter married to Altonian Duke (border territory); son in Royal Court with Altonian tutoring pressure (1.5x invasion clock if refused)"
  - "Restoration Movement: non-TS leaders (scholars, guild members) as loose coalition"
  - "Southernmost Council: not publicly active in Restoration — occupied with Thread Wounds"
editorial_pending:
  - "Succession mechanic (Almud's son/Altonian pressure clock) — designed but not yet formalized"
  - "Named Restoration Movement NPCs — to be generated"
  - "Axis 10 (Succession) — to be formalized with heir mechanic"
  - "Niflhel primus inter pares (carried from S4)"
  - "Varfell Private Collection transfer (carried from S4)"
gaps_resolved_this_session:
  - "Löwenritter faction identity (opened S4, resolved S5)"
next_action:
  skill: orchestrator
  task: "Remaining pre-Batch-E work: succession mechanic, Restoration NPCs, then Batch E (board game, 14 gaps)"
  input: lowenritter_faction_card.md + batch_d_designs.md
output_files:
  - "lowenritter_faction_card.md"
```

---


```yaml
session_update: 2026-03-25T05b
completed_stages_addendum:
  - "Succession mechanic designed (Torben Loyalty Clock, 8->0 countdown)"
  - "Tutoring Demand trigger: IP 30"
  - "Covert contact mechanic: Intelligence Ob 3 to freeze loyalty decay 1 season"
  - "Retrieval options tiered by loyalty range (diplomatic/covert/military)"
  - "Elske backup heir pathway designed (four-way endgame)"
  - "Axis 10 formalized"
  - "Faction interaction map for succession (all 8 factions)"
  - "IP acceleration math verified (+10 IP delta over 10 seasons)"
  - "Canon compliance checked (P-01, P-07, P-09, P-12)"
editorial_resolved_addendum:
  - "Tutoring demand begins at IP 30"
  - "Covert contact can slow loyalty decay (Intelligence Ob 3/season)"
gaps_resolved_addendum:
  - "Axis 10 (Succession) — formalized with full mechanic"
output_files_addendum:
  - "succession_mechanic.md"
```

---


```yaml
session_update: 2026-03-25T05c
phase: 1
batch: E (board game — complete)
completed_stages:
  - "G-026: Turn structure (5-phase season: Planning/Negotiation/Reveal/Resolution/Accounting)"
  - "G-025: Order Set (7 universal + restricted + faction-specific replacements; 3 orders full-sheet, 2 partial)"
  - "G-059: Simultaneous order placement (clockwise rotation, dummy tokens)"
  - "G-060: Resolution priority (12-tier priority table, Influence tiebreak)"
  - "G-029: 15 territories designed (names, start control, Prosperity, Fortification, special properties, adjacencies)"
  - "G-028: Victory conditions per faction (8 primary + secondary scoring + shared TT loss)"
  - "G-050: Event deck (13 clock events + 10/20 seasonal events designed)"
  - "G-051: Season wheel (Spring/Summer/Autumn/Winter modifiers)"
  - "G-057: Thread operations (Weave/Investigate/Harvest + 15 Co-Movement Cards)"
  - "G-049: Negotiation (informal non-binding + formal Treaty procedure + max 2 treaties)"
  - "G-030: Component specification (full list: board, 8 faction sheets, tokens, decks, dice, reference cards)"
  - "G-031: NPC AI expansion (3-priority decision tree per faction + escalation rules)"
  - "Lowenritter integrated into all board game systems (partial sheet, post-coup full sheet)"
  - "Succession mechanic integrated (Torben Loyalty track as component)"
gaps_resolved_this_session:
  - "G-025 (Order Set)"
  - "G-026 (turn structure)"
  - "G-028 (victory conditions)"
  - "G-029 (territory differentiation)"
  - "G-030 (components)"
  - "G-031 (NPC AI)"
  - "G-049 (negotiation)"
  - "G-050 (event deck)"
  - "G-051 (season wheel)"
  - "G-057 (Thread operations)"
  - "G-059 (simultaneous placement)"
  - "G-060 (resolution ordering)"
editorial_minor:
  - "Territory names may need editorial pass (functional but placeholder-quality)"
  - "Varfell victory condition (3 artifacts) may need tuning"
  - "10 remaining seasonal event cards to write"
next_action:
  skill: orchestrator
  task: "Phase 1 Batch F (hybrid + endgame, 3 gaps) — then Phase 1 complete"
  input: batch_e_designs.md + batch_d_designs.md + succession_mechanic.md + lowenritter_faction_card.md
output_files:
  - "batch_e_designs.md"
  - "lowenritter_faction_card.md"
  - "succession_mechanic.md"
```

---


```yaml
session_close: 2026-03-25T05-final
phase: 1
status: PHASE 1 COMPLETE — all 38 design gaps resolved
completed_stages:
  - "Lowenritter faction card: 8th faction, partial sheet (Mil/Stab/Inf/Int), coup trigger, Martial Law, Deontological Honor Code"
  - "Grandmaster Sigrid Ehrenwall NPC created"
  - "Succession mechanic v2: Torben Loyalty Clock (floors at 1), Tutoring Demand at IP 30, covert contact"
  - "Elske Almqvist: full NPC with Conviction (Family vs Self-Determination), Resonant Style (Evidence), three independence paths, seven succession scenarios"
  - "Church territorial seizure mechanic: TC 80 threshold, per-territory roll vs variable Ob, counter-play options"
  - "Batch E complete: 13 board game gaps (turn structure, Order Set, 15 territories, victory conditions, event deck, season wheel, Thread ops, negotiation, components, NPC AI, simultaneous placement, resolution ordering)"
  - "Batch F complete: 3 hybrid+endgame gaps (timing table, endgame conditions all modes, mode branching catalogue)"
  - "Phase 1 Design: ALL 38 gaps resolved across Batches A-F"
editorial_resolved:
  - "Lowenritter: full 8th faction, partial sheet peacetime, full sheet on coup"
  - "Lowenritter partial sheet: Military, Stability, Influence, Intelligence"
  - "Church territory seizure: per-territory roll at TC 80, not blanket takeover"
  - "Cognatic succession, male-heir priority"
  - "Torben Loyalty floors at 1 (Altonia never lets him renounce)"
  - "Elske: torn, recruitable by multiple factions, can seize independence with support"
  - "Tutoring Demand triggers at IP 30"
  - "Covert contact slows Torben loyalty decay (Intelligence Ob 3/season)"
  - "Almud has two children: Elske (married to Altonian Duke), Torben (Royal Court)"
  - "Church does not hold territories until TC 80"
  - "Restoration Movement: non-TS leaders, loose coalition (NPCs deferred)"
  - "Southernmost Council: not publicly active in Restoration"
editorial_pending:
  - "Territory names editorial pass (functional but placeholder)"
  - "Varfell victory condition tuning (3 artifacts)"
  - "10 remaining seasonal event cards"
  - "Named Restoration Movement NPCs"
  - "Niflhel primus inter pares (carried from S4)"
  - "Varfell Private Collection transfer (carried from S4)"
gaps_resolved_this_session:
  - "Lowenritter faction identity"
  - "Axis 10 (Succession)"
  - "G-025 (Order Set)"
  - "G-026 (turn structure)"
  - "G-028 (victory conditions)"
  - "G-029 (territory differentiation)"
  - "G-030 (components)"
  - "G-031 (NPC AI)"
  - "G-049 (negotiation)"
  - "G-050 (event deck)"
  - "G-051 (season wheel)"
  - "G-057 (Thread operations)"
  - "G-059 (simultaneous placement)"
  - "G-060 (resolution ordering)"
  - "G-018 (hybrid timing table)"
  - "G-021 (endgame conditions)"
  - "G-023 (mode branching catalogue)"
  - "Church territorial seizure (TC 80)"
next_action:
  skill: orchestrator
  task: "Phase 2 — Compilation. Assemble all designs into two documents (TTRPG ruleset + board game ruleset). 28 compilation stages estimated."
  input: >
    All design files: batch_a_designs.md, batch_bc_designs.md, batch_d_designs.md,
    batch_e_designs.md, batch_f_designs.md, lowenritter_faction_card.md,
    succession_mechanic.md, church_territorial_seizure.md.
    Plus existing ruleset checkpoint (valoria_ruleset_checkpoint_13.docx),
    Philosophical Foundations, Mechanics.docx.
  prerequisites:
    - "Resolve remaining editorial items (territory names, Varfell victory, event cards, Restoration NPCs, Niflhel/Varfell carried items)"
    - "Or defer them to Phase 2 in-line"
blockers:
  - "None — Phase 2 can begin"
output_files:
  - "lowenritter_faction_card.md"
  - "succession_mechanic.md (v2)"
  - "church_territorial_seizure.md"
  - "batch_e_designs.md"
  - "batch_f_designs.md"
```

---


```yaml
session_update: 2026-03-25T05d-final
completed_stages_addendum:
  - "Canonical timeline committed: 45 AG game start, TC 22, all chronological conflicts resolved"
  - "Church territorial seizure mechanic committed (TC 80, per-territory roll vs variable Ob)"
  - "Batch F committed (hybrid timing, endgame, mode branching)"
  - "6 document-level conflicts resolved (year, TC, children, rank, TT rationale, heir name)"
  - "Lowenritter starting values added to faction table (Mil 5, Int 3, Stab 5, Inf 3)"
  - "Schoenland documented as spoiler actor (not a faction)"
  - "Edvar retired as heir name — Torben canonical"
editorial_resolved_addendum:
  - "Game start: 45 AG (not 102 AG)"
  - "TC starting value: 22 (Church predates secession, consolidated post-war)"
  - "Timeline is canonical for setting chronology, supersedes checkpoint references"
output_files_addendum:
  - "valoria_canonical_timeline.md"
  - "church_territorial_seizure.md"
  - "batch_f_designs.md"
standing_editorial:
  - "E-01: Perpetrator of ~18 AG assassination — TBD"
  - "E-03: In-world name for AG calendar — TBD"
```

---




---

# Valoria Session Log - Current

> Resuming instance: read ONLY this file. Archive is in session_log_archive.md.

---

session_close: 2026-03-26-full-compile
phase: 2
status: Phase 2 COMPLETE — all 16 TTRPG stages compiled; full document assembled
completed_stages:
  - Stage 1: Core Engine
  - Stage 2: Characters
  - Stage 3: Thread Operations
  - Stage 4: Southernmost
  - Stage 5: Clocks (TT/TC/IP)
  - Stage 6: Factions
  - Stage 7: Territories
  - Stage 8: Combat
  - Stage 9: Social Systems
  - Stage 10: Advancement
  - Stage 11: Scale Transitions
  - Stage 12: Campaign Modes
  - Stage 13: NPCs + Institutional Actors
  - Stage 14: GM Tools
  - Stage 15: Thread Spell Catalog
  - Stage 16: Reference Materials
compilation_progress: 16/16 TTRPG stages complete
assembly_output: compilation/valoria_ttrpg_complete.md (244KB, ~4,100 lines, commit a45b6525)
notes:
  - Stage 15 contains Thread Spell Catalog only (not equipment — weapons in stage 8, dissolution residue in stage 3)
  - CP13 Corruption track excluded (not canon per user)
  - Taint track references flagged for canon-guard pass — stage 3 §5.10 uses "Taint Track" header; canonical mechanic is CD (Coherence Degradation)
  - Heart/Poise attribute references in stages 3, 9 use old 9-attribute names; stage 1 uses canonical 10-attribute set — cross-stage inconsistency requires canon-guard pass
  - 4 EDITORIAL flags remain in assembled document (see below)
canon_guard_issues_flagged:
  - §5.10 header reads "Taint Track" — should read "Transformation and Epistemic Seduction — Coherence Degradation"
  - Stage 3 Leap pool uses "Heart" — should use canonical attribute (Focus or Spirit per 10-attr set)
  - Stage 9 Composure formula uses "Poise + Heart" — neither in 10-attr set; needs resolution
  - Stage 2 Inspiration cap references "Heart score" — needs attribute substitution
editorial_pending:
  - Renown permission table (Renown 1-10 tiers) — only data point is Renown 6
  - Varfell Private Collection transfer (PC takeover scenario)
  - Niflhel primus inter pares decision
  - Revolution named elder NPC contact (optional)
  - Territory names (batch_e placeholder vs design doc names)
  - Varfell victory condition tuning
  - 10 remaining seasonal event cards (of 20 total)
  - Named Restoration NPCs
  - E-01 assassination perpetrator
  - E-03 AG calendar name
  - Niflhel named NPC stat blocks (Rolf Dunmark, Solvind Brak)
  - Revolution named NPC stat blocks (Edith Varn)
next_action:
  stage: Stage 17 (Canon Guard Pass)
  task: Systematic canon-guard review of assembled document — resolve attribute name inconsistencies, remove Taint references, verify all 14 canon constraints
  model: Sonnet 4.6
  input_file: compilation/valoria_ttrpg_complete.md
  priority_issues:
    - Heart/Poise → canonical 10-attr equivalents (Focus, Spirit, Presence, Bonds)
    - §5.10 Taint Track header → CD
    - Composure formula in stage 9
    - Inspiration cap attribute in stage 2
output_files:
  - compilation/stage15_spell_catalog.md committed (d29b845f)
  - compilation/stage16_reference.md committed (bb85580e)
  - compilation/valoria_ttrpg_complete.md committed (a45b6525)

---

# Valoria Session Log - Current

> Resuming instance: read ONLY this file. Archive is in session_log_archive.md.

---

session_close: 2026-03-26-checkpoint14
phase: 2
status: Checkpoint 14 compiled and committed

completed_this_session:
  - Stage 17 canon guard pass (all P1-P14 constraints verified)
  - 6 mechanical patches applied to valoria_ttrpg_complete.md
  - 17 hybrid gaps resolved (G-075, G-079–G-095)
  - §12.3 Hybrid Mode rewritten with all resolved gap content
  - §12.9 Hybrid Consequence Rules added (new section)
  - Checkpoint 14 exported: compilation/valoria_ruleset_checkpoint_14.md

commits:
  - stage17_canon_guard.md: 8526e934
  - valoria_ttrpg_complete.md (stage 17 patches): f318f7ee
  - designs/hybrid_gaps_resolved.md: 6e543b5c
  - valoria_ttrpg_complete.md (hybrid additions): 38a0fe31
  - compilation/valoria_ruleset_checkpoint_14.md: 2115df16

canonical_decisions_locked:
  thread_op_pools:
    Leap: Attunement + History bonus
    Contact_Duration: Focus score (rounds)
    Wound_disruption: Focus check TN 7 Ob 1
    All_ops_Weave_Pull_FR: Spirit + History bonus
  composure: Presence + 6 (range 7-13)
  debate_pool: Cognition + History bonus
  battle_engine: Officer Cognition (attack) + Presence (cohesion/rally); initiative Cognition
  personal_combat_manoeuvres: Agility
  inspiration_cap: Spirit score (no derived name)
  coherence_track: individual 10-0 (10=fully coherent, 0=monstrous NPC)
  thread_stability: campaign-arc 20-0 (20=stable, 0=crisis)
  hybrid_session_structure: Personal (90-150min) → Strategic → Cascade
  hybrid_pacing: 1 session minimum per season
  hybrid_fog_of_war: 4 qualitative states; exact for own faction; Intel always hidden
  hybrid_handoffs: batch to Cascade; GM ledger
  hybrid_zoom_in: player-involved only
  hybrid_cascade: 5-step sequence, GM-only
  hybrid_resources_wealth: threshold = 2x rolled; below = stressed
  hybrid_flashback: Personal phase only
  hybrid_pc_death: Crisis penalty; take over loyal NPC or succession; no new characters
  hybrid_faction_collapse: continue as personal character; lose faction dice bonuses
  hybrid_downtime: concurrent with Strategic phase
  hybrid_advancement: board game successes generate CP
  hybrid_knot_gating: gated by in-scene discovery

editorial_pending:
  - Renown permission table (tiers 1-10)
  - Varfell Private Collection transfer
  - Niflhel primus inter pares
  - Revolution named elder NPC
  - Territory names (batch_e placeholders)
  - Varfell victory condition tuning
  - 10 remaining seasonal event cards
  - Named Restoration NPCs
  - E-01 assassination perpetrator
  - E-03 AG calendar name
  - Niflhel named NPC stat blocks (Rolf Dunmark, Solvind Brak)
  - Revolution named NPC stat blocks (Edith Varn)

next_action:
  recommended: Board game mode compilation (Phase 2 remaining deliverable) OR Phase 3 simulation
  model: Sonnet 4.6
  note: G-093 Resources/Wealth formula (2x vs 2x-1) flagged for Phase 3 stress testing

model_routing_notes: Sonnet 4.6 throughout — canon guard, hybrid gap resolution, compilation
---
session_close: 2026-03-26
checkpoint: 14-editorial
model: claude-sonnet-4-6
completed_stages:
  - Cross-reference audit CP14 TTRPG vs BG (10 passes, 62 findings)
  - P1 editorial resolution (7 items)
  - P2/P3 editorial round (16 items A-P)
  - Full correction push to both CP14 and BG

commits:
  cp14: 2325655348e0
  bg: c49141521803

corrections_applied:
  cp14:
    - Territory names: all 15 canonical
    - Forced Resolution -> Locking and Snapping throughout
    - Rattled: wound-equivalent track (-1D per accumulation)
    - Coherence: full spec with Coherence 2 consult, Coherence 0 monstrous, saving attempt rule
    - Monstrous entities: excess undifferentiated Thread via gaps
    - Knots: +1 Strain for +2D -> +2 strain for +3D; presence/narration required; closer bonds = higher capacity
    - Domain Ob: direct (1-7), pool adds faction stat if leadership position held
    - Co-movement: d10 replacing d6, no supplements, TPS added to all Thread pools
    - TPS = TS / 10 (round down)
    - Renown: full 0-10 table
    - Vaynard: Ambition Track (0-100), TK 4-5 redesigned, TS via collection
    - Vaynard victory: Path A (all 15) or Path B (10+ territories + Stillhelm + TK5 + TS75+)
    - Niflhel: four competing networks with supremacy mechanic
    - Eidur Sjostrom and Hakan Reusfoldt NPCs added
    - TC pause threshold: Stability <= 4
    - Attribute pool: 31 points
    - S-16 through S-20 seasonal events added

editorial_still_pending:
  - S-08 Einhir site name
  - E-01 assassination perpetrator
  - Vaynard Private Collection transfer procedure
  - Niflhel Supremacy seasonal resolution procedure
  - Coherence 0 saving attempt procedure

next_action:
  recommended: Phase 3 simulation or CP15 compilation
  model: Sonnet 4.6



---

session_close: 2026-03-27
checkpoint: 14-sim-prep
model: claude-sonnet-4-6
completed_stages:
  - Identified all mechanics directly impacted by editorial decisions committed 2026-03-26
  - Mapped 12 mechanic groups requiring re-simulation
  - Discovered P1 attribute pool inconsistency (§2.2 vs §14.1/§12)
  - Prepared full simulation routing table and handoff

p1_finding:
  issue: Attribute pool contradiction
  location_1: "§2.2 — 31 points distributed across 10 attributes"
  location_2: "§14.1 (Session Zero checklist) — 18 attribute points"
  location_3: "§3772 (GM checklist) — 18 attribute points"
  location_4: "§12 (hybrid) — 18 attribute points"
  action_required: Propagate 31 to all checklist references before next push

mechanics_flagged_for_simulation:
  - id: M-11/M-12/M-13/M-14/M-15
    change: TPS (=TS÷10 round down) added to all Thread operation pools
    test_modes: [A_isolation, B_interaction]
  - id: M-16/M-17/M-18
    change: Co-movement d10 replacing d6; History Resonance and Flashback removed from co-movement
    test_modes: [A_isolation, D_edge_cases]
  - id: M-26
    change: Coherence renamed Intelligibility (10->0); effects table revised; separate Coherence track retained
    test_modes: [A_isolation, B_interaction_with_Knots, D_edge_cases]
  - id: M-32
    change: Knot Call = +2 strain for +3D; closer bonds = higher strain capacity
    test_modes: [B_interaction, D_edge_cases]
  - id: M-03_Composure
    change: Rattled = wound-equivalent track (-1D per mark, cumulative); Composure resets after each Rattled
    test_modes: [A_isolation, D_edge_cases]
  - id: M-42
    change: Domain Ob = direct target stat (1-7, no division); pool adds faction stat if leadership held
    test_modes: [A_isolation, B_interaction, C_scenario]
  - id: M-36
    change: Renown 0-10 full permission table; Debate bonuses at tier 5/6/7/8
    test_modes: [A_isolation, B_interaction_with_Debate]
  - id: M-47_Vaynard
    change: Ambition Track (0-100, 5 thresholds); TK system redesigned; TS via originary lock collection
    test_modes: [A_isolation_full_range, C_scenario]
  - id: M-44_Niflhel
    change: Four-network Supremacy Mechanic at seasonal accounting
    test_modes: [A_isolation, C_endgame_scenario]
  - id: M-46_TC
    change: TC pause threshold changed from Stability <= 5 to Stability <= 4
    test_modes: [A_boundary, C_scenario]
  - id: M-43_seasonal
    change: S-16 through S-20 added (five new event triggers)
    test_modes: [C_scenario, D_interaction_with_existing_events]

commits: {}

editorial_still_pending:
  - S-08 Einhir site name (deferred)
  - Co-movement d10 table in BG (uses card system; d10 is TTRPG only)
  - E-01 assassination perpetrator (intentionally unresolved)
  - Vaynard Private Collection transfer procedure (design pending)
  - Niflhel Supremacy seasonal resolution full procedure (design pending)
  - Coherence 0 saving attempt procedure (design pending)

next_action:
  task: Run full simulation suite on all 12 mechanic groups above
  skill: valoria-simulator
  modes: [A_isolation, B_interaction, C_scenario, D_edge_cases]
  priority_order:
    1: TPS across all Thread ops (Mode A)
    2: Co-movement d10 (Mode A + D)
    3: Intelligibility x Knot strain interaction (Mode B)
    4: Rattled stacking (Mode A + D)
    5: Domain Ob + leadership pool (Mode B with faction stats)
    6: Renown x Debate (Mode B)
    7: Vaynard Ambition Track full range (Mode A)
    8: Niflhel Supremacy endgame (Mode A + C)
    9: TC pause at Stability <= 4 (Mode C)
    10: Seasonal events S-16-S-20 (Mode C)
  output_file: tests/valoria_stress_tests_batch3.md
  also_repair: Propagate attribute pool = 31 to §14.1 and §12 checklist references in CP14
  model: Sonnet 4.6

---

session_close: 2026-03-27
checkpoint: 14-sim-prep
model: claude-sonnet-4-6
completed_stages:
  - Identified all mechanics directly impacted by editorial decisions committed 2026-03-26
  - Mapped 12 mechanic groups requiring re-simulation
  - Discovered P1 attribute pool inconsistency (§2.2 vs §14.1/§12)
  - Prepared full simulation routing table and handoff

p1_finding:
  issue: Attribute pool contradiction
  location_1: §2.2 — 31 points distributed across 10 attributes
  location_2: §14.1 (Session Zero checklist) — 18 attribute points
  location_3: §3772 (GM checklist) — 18 attribute points
  location_4: §12 (hybrid) — 18 attribute points
  action_required: Propagate 31 to all checklist references before next push

---

session_close: 2026-03-27
checkpoint: 14-editorial-complete
model: claude-sonnet-4-6
completed_stages:
  - BUG-004 verified complete (stage13 clean)
  - stage3 full Stage17-P3 propagation: pool formulas, CD->ThS, FR->Locking/Snapping, §5.6 degree table
  - stage2 GAP-UC-03-A Devout targeting ruling; Locking/Snapping name fix
  - F-32 coup counter (Option A): stage6, stage13, CP14
  - F-33 Martial Law (Option A): stage6, CP14
  - F-34 TC80 seizure procedure (user ruling): stage6, CP14
  - GAP-UC-03-A Devout targeting (Option A): stage2, CP14
  - F-33B simulation: Option B rejected (2x P1, 1x P2 vs no advantages)

commits:
  stage3: 27f9335a484e
  stage6: 94695c70e70e
  stage13: 13ffa7265870
  stage2: 68fed70656e5
  cp14: a83904a1a1d3
  f33b_sim: 765fb5e24512

editorial_decisions_resolved:
  F-32: Coup Counter 0-3, three named triggers, never decrements
  F-33: Martial Law Option A (secondary Military Ob 2 check; Covert Ob 3 for others; exit Ob = Military/2)
  F-34: Church Mandate vs owner Mandate/2; flat TC +1/+3/+5 on seizure; no per-season accrual; counter-play options
  GAP-UC-03-A: Devout provides no protection from being targeted; experiences result without understanding cause

editorial_still_pending:
  - S-08 Einhir site name
  - E-01 assassination perpetrator
  - Vaynard Private Collection transfer procedure
  - Niflhel Supremacy seasonal resolution procedure
  - Coherence 0 saving attempt procedure
  - F-31: Devout bypass at TS 0-9 (fix note — Haiku-tier, mechanical)

f33b_verdict: Option A correct. Option B introduces P1 exit-condition gap and P1 coup-as-weapon dominant strategy.

next_action:
  task: Batch 5 — core combat engine M-01 through M-09
  skill: valoria-simulator
  mode: A_isolation then B_interaction
  note: 30 mechanics still untested; combat engine is foundational; start here
  model: Sonnet 4.6

---
session_close: 2026-03-27
checkpoint: post-batch6-simulation
model: claude-sonnet-4-6
completed_stages:
  - Batch 6 simulation complete: History Resonance, Push/Certainty blast radius, Diagnosis standalone, Co-Movement Cards BG, Impression Track, Reading Exchange, Defection (gap status confirmed), Fortification, BG Turn Structure, Victory Conditions, Hollow Victory
  - P1 fix applied: Reading Exchange Ob=1 + degree mapping (stage9 §9.4)
  - Impression Track + Knot Crisis priority rule added (stage2 §4.7)
  - Fortification construction Domain Action added (stage8 §8.4)
  - BG FORTIFY order added (stage_bg B5)
  - BG mid-phase clock game-end check added (stage_bg B4)
  - G-111 through G-114 closed same session
  - G-115 closed: Church VC = TC≥60 + Himmelenger + Valorsplatz; expansion lock TC≥40

editorial_pending:
  - G-115: Church victory condition — is Church intentionally unwinnable in standard play, or should TC≥80 be changed to TC≥60?
  - B6-VC-03: 2-player NPC order reduction (2 instead of 3) may undermine clock tension
  - Co-Movement cards CM-11 through CM-20 (BG-E-01)
  - Varfell TK 5 consequence (BG-E-02)
  - S-08 Einhir site name; E-01 perpetrator; Niflhel primus inter pares; territory names; Restoration NPCs

gap_register_delta:
  closed: G-111 (RE Ob), G-112 (IT+Knot), G-113 (Fortification build), G-114 (BG mid-phase)
  open: G-115 (Church VC editorial)

commits:
  - tests/valoria_stress_tests_batch6.md: Batch 6 sim results
  - compilation/stage9_social.md: Reading Exchange Ob fix
  - compilation/stage2_characters.md: IT+Knot Crisis priority
  - compilation/stage8_combat.md: Fortification construction
  - compilation/stage_bg_board_game_mode.md: FORTIFY order + mid-phase check

simulation_coverage_summary:
  batches_complete: [B5-ModeA, B5-ModeB, B6]
  mechanics_tested: M-001 through M-009 (M-005 eliminated), History Resonance, Push, Diagnosis, Co-Movement BG, Impression Track, Reading Exchange, Fortification, BG Turn Structure, Victory Conditions
  mechanics_pending: M-010 through M-056 (Thread ops, faction, combat specifics), Defection (design pending G-036)
  p1s_total_found: 5 (M002-01 fixed, M009-01 fixed, B03-01 fixed, B07-01 fixed, B6-RE-01 fixed)
  all_p1s_closed: true

next_action:
  task: Continue simulation — M-010+ (Thread ops, faction mechanics, combat specifics)
  all_editorial_blockers_cleared: true
session_close: 2026-03-27
checkpoint: post-infrastructure-overhaul
model: claude-sonnet-4-6
completed_stages:
  - Rewrote project_instructions.md — lean protocol, inline router, item-by-item GitHub reads
  - Created tools/model_router.html — auto-routing artifact for Haiku/Sonnet/Opus inline
  - Session start now reads only 3 files: session_log_current, gap_register (P1 count), workplan (phase/stage)
  - All Haiku/Opus tasks route through artifact inline; no session branching required

commits:
  - project_instructions.md: full rewrite
  - tools/model_router.html: new file

next_action:
  task: Phase 3 simulation — BG-specific mechanics M-62–64, M-67–70, M-72, M-74–75; full-scenario Mode C; then S-10/S-11/S-12
  all_reconciliation_tasks_complete: true
  p1_open_design: 40 items

---

```yaml
session_id: 2026-03-27T13
phase: Phase 3 (Simulation) — Batch 11 complete + replay
status: PP-086–091 committed; mass combat replay validates PP-086/087/091

completed_this_session:
  - PP-086–091 drafted and pushed (6 P1 fixes)
  - Mass combat replay (The Field at Harskeld): 5-round engagement, Crown vs. Varfell
  - PP-086 (base damage): validated
  - PP-087 (Formation Break stacking): validated
  - PP-091 (Artillery Bombard): validated

patch_count: 91 total (33 P1, 47 P2, 10 P3, 1 design)
next_action: M-036 (Parliamentary Vote) and M-037 (Grand Debate isolation)
```

---

session_id: 2026-03-27T14
phase: Thread Operations Redesign (philosophical + mechanical)
status: v2.5 FINAL DRAFT — canon-compliant, stress-tested, ready for Sonnet-tier simulation

completed_this_session:
  - Critical philosophical evaluation of threadweaving mechanics against Foundations
  - 6 editorial decisions resolved (ThS/Intelligibility merge, Gap proximity, FR asymmetry, Spooling level, Gap closure reclassification, Threadcut rendering)
  - Foundational reframe: Leap as rendering suspension, not rendering expansion
  - Foundational reframe: threads as oscillation of three axes, not objects with properties
  - Foundational reframe: beings ARE drawings-from-ground (spooling IS what beings are)
  - Einhir principle stated as design principle (game rewards restraint, punishes ambition)
  - Full threadweaving redesign document produced (v2.5, ~930 lines)
  - 4 systems replaced: Intelligibility + ThS + Taint → Coherence (10→0); TT → Rendering Stability (100→0)
  - 1 new operation type: Mending (substrate repair, Attunement + Focus + TPS pool)
  - Diagnosis repositioned before Leap (last act of rendering)
  - Diagnosis gains trajectory perception (scale-gated)
  - Threadcut beings: observer-dependent rendering, Rendering Strain, De-actualisation
  - Over-actualisation hazard added to Weaving at Relational+ scale
  - FR Lock gains chronic consequences (RS drift, adjacent Ob penalties)
  - 18 extreme chain stress tests across 3 batches
  - 30 patches applied (numbered P-01 through P-30)
  - 2 canon audits: 14/14 PASS + 3/3 philosophical claims INTEGRATED
  - Board game: Mend order added, Co-Movement deck expanded 15→18, degree table for all Thread orders
  - Hybrid: Coherence tracking, Lock chronic registration, Mending cross-mode rules

editorial_decisions:
  - ThS + Intelligibility merged into Coherence (10→0)
  - Gap proximity: no benefit (excess being is catastrophe, not resource)
  - FR Lock vs Dissolution: asymmetric (chronic vs acute), not equal
  - Spooling: Level 1 (framing only)
  - Gap closure: new operation type Mending (not Weaving, not FR Dissolution)
  - Threadcut rendering: observer-dependent at baseline, can render beyond ceiling at cost of accelerated exhaustion
  - Taint track: eliminated. Dissolution residue = accelerated Coherence loss.
  - TT renamed Rendering Stability, inverted (100→0)
  - Galbados → Solmund (logged for Haiku batch, not yet applied)
  - AG → AS calendar (logged for Haiku batch)
  - Church of Galbados → Church of Solmund (logged for Haiku batch)

output_files:
  - designs/threadweaving_redesign_v25.md (main design document)
  - tests/threadweaving_stress_tests_batch1.md
  - tests/threadweaving_stress_tests_batch2.md
  - tests/threadweaving_stress_tests_batch3.md
  - canon/canon_review_threadweaving_v24.md
  - canon/canon_reaudit_threadweaving_v25.md

deferred_tasks:
  - "Solmund rename (all files) — Haiku-tier"
  - "AG → AS calendar rename — Haiku-tier"
  - "Sonnet-tier simulation: Coherence degradation curves, FR Lock chronic drift, Mending pool probability, over-actualisation impact, Diagnosis-before-Leap combat timing, threadcut De-actualisation"
  - "Mode 2 stat block vs D-18 ruling verification"
  - "Board game RS track integration (Co-Movement deck rewrite)"
  - "Hybrid mode branching catalogue update"
  - "Compilation: new Stage 3 Thread Operations chapter"

blockers: []

next_action:
  task: Sonnet-tier simulation of v2.5 mechanics (Coherence curves, Mending pools, combat timing)
  model: Sonnet
  input: designs/threadweaving_redesign_v25.md

---

session_id: 2026-03-27T18
phase: Thread Operations Redesign — Simulation Batch 2
status: Batch 2 complete. 3 P1, 6 P2, 2 P3. Editorial decisions needed on F-03 and F-04.

completed_this_session:
  - Stress test batch 2: Collective Operations, Past-Oriented Pulling, Involuntary Leap, Opposing Ops
  - 11 new findings (SIM2-F-01 through SIM2-F-11)
  - Gap register updated: +11 items
  - Output: tests/sim_threadweaving_v25_batch2.md

critical_findings:
  - SIM2-F-03 (P1): Past-Oriented Pulling recency Ob table absent from v2.5 — blocks play
  - SIM2-F-04 (P1): Past-Oriented Pulling pool (Spirit+History only) makes TS irrelevant to execution
  - SIM2-F-09 (P1): Involuntary-to-voluntary-extension bypasses concealment — exploit

editorial_decisions_needed:
  - SIM2-F-04: Add TPS (or TPS/2) to Past-Oriented Pulling pool? Or add rationale note?
  - SIM2-F-03: Reproduce recency Ob table in §2.4 (from prior ruleset — needs source)

deferred_tasks:
  - Resolve editorial decisions on SIM2-F-03 and SIM2-F-04
  - Mechanic-audit patches for SIM2-F-03, F-04, F-09 (P1s)
  - P2 patches: SIM2-F-01, F-02, F-05, F-08, F-10, F-11
  - Haiku batch: Solmund rename, AG→AS, Church rename
  - Stage 3 compilation (pending all patches)

blockers:
  - SIM2-F-03: recency Ob table source unknown — need prior ruleset or user input
  - SIM2-F-04: design decision required before patching

next_action:
  task: Editorial decisions on SIM2-F-03 and SIM2-F-04
  model: Current (user decision)

---

session_id: 2026-03-27T25
phase: Phase 2 Compilation — Stage 3 Thread Operations COMPLETE
status: Stage 3 compiled, canon-guard passed, report written. No open P1 findings.

completed_this_session:
  - Applied final SIM7 patches (9 patches including Foundational Pull, threadcut external ops)
  - Assembled Stage 3 Thread Operations from threadweaving_redesign_v25.md
  - Reformatted to compilation structure (§5.0–§5.8, Part Five numbering)
  - Stripped design-doc framing; cleaned migration notes; fixed cross-references
  - Canon-guard pass: 14/14 PASS, 0 violations, 0 PARTIAL
  - Compilation report written: stage3_compilation_report.md
  - Stage 3 pushed: 78,201 chars, 826 lines (was 38,597 chars pre-v2.5)

stage3_stats:
  old_size: 38597 chars
  new_size: 78201 chars
  patches_applied: 52
  canon_guard: PASS 14/14
  open_p1: 0
  open_p2: 12 (non-blocking, logged in §5.8)
  open_p3: 10

compilation_progress:
  stages_complete: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, BG]
  stage3_was_outdated: true (pre-v2.5)
  stage3_now: current (v2.5, fully patched)
  note: Infrastructure audit (valoria_infrastructure_audit.md) indicates all 17 TTRPG stages + BG already compiled. Stage 3 was the only outdated one. Phase 2 compilation may be complete.

deferred_tasks:
  - Haiku batch: Solmund rename (all files), AG→AS calendar rename, Church of Galbados→Church of Solmund
  - Stage 4 cross-reference: SIM5-F-08 (RS threshold at Southernmost)
  - P2 items in §5.8 — assign to relevant downstream stages for polish pass
  - Verify other stages don't reference old Stage 3 terminology (TT, ThS, CD, Intelligibility)

next_action:
  task: Haiku rename batch OR verify compilation completeness across all stages
  model: Haiku (renames) / Sonnet (verification)

---

session_id: 2026-03-27T_THREADWEAVING_FINAL
phase: Phase 2 Compilation — Stage 3 Thread Operations complete
status: CLOSED — all work committed to GitHub

## SESSION SUMMARY

### What was accomplished
- Full philosophical and mechanical redesign of Thread Operations (v2.5) stress-tested and compiled
- 8 simulation batches run (64 total findings)
- 52 findings patched into designs/threadweaving_redesign_v25.md
- Stage 3 Thread Operations recompiled from 38,597 → 78,201 chars
- Canon guard: 14/14 PASS, 0 violations

### Key design decisions made this session
1. ThS/Intelligibility/CD/Taint → Coherence (10→0, unified track)
2. Thread Tension (TT) → Rendering Stability (RS, 100→0, inverted)
3. Diagnosis repositioned before Leap (last act of rendering)
4. Mending added as new operation type (substrate repair, not thread operation)
5. Coherence cap: −1 per operation maximum (all degree table costs absorbed)
6. Past-Oriented Pulling pool: Spirit + History + TPS÷2
7. Lock removal Ob: (original TS ÷ 10) − 2, minimum 1
8. §9.7 threadcut interference: capped at +4 (not uncapped)
9. Mending Ob ceiling: 8 (regardless of stacked modifiers)
10. Residue Coherence: Option C (−1 at Object/Personal; absorbed at Relational+)
11. FR Lock immediate RS cost: −1/−2/−3 (was −2/−3/−4)
12. Foundational Past-Oriented Pulling: Einhir framework required, +2 Ob, RS ×3
13. Threadcut beings: can perform external Thread operations at cost of +1 Rendering Strain each
14. Collective Leap: all practitioners roll own Leap; Anchor failure = lattice never forms
15. RS Critical: 2–4 season endgame; Mandate 0 = Faction Fracture

### GitHub state (all committed)
- designs/threadweaving_redesign_v25.md — fully patched (100,790 chars)
- compilation/stage3_thread_operations.md — recompiled v2.5 (78,201 chars)
- compilation/stage2_characters.md — SIM8-F-07/08 patches applied
- compilation/stage3_compilation_report.md — canon guard report
- tests/sim_threadweaving_v25.md — batch 1
- tests/sim_threadweaving_v25_batch2.md
- tests/sim_threadweaving_v25_batch3.md
- tests/sim_threadweaving_v25_batch4.md
- tests/sim_threadweaving_v25_batch5.md
- tests/sim_threadweaving_v25_batch6.md
- tests/sim_threadweaving_v25_batch7.md
- tests/sim_threadweaving_v25_batch8.md
- tests/mechanic_audit_sim_patches.md
- valoria_gap_register_consolidated.md — updated (~226 items)
- session_log_current.md — this close
- session_log_archive.md — prior session appended

### Open items (non-blocking)
P2 (12): SIM2-F-01, SIM3-F-02/03, SIM4-F-02, SIM5-F-08, SIM6-F-02/04, SIM7-F-04, SIM8-F-02/03/09/10
P3 (10): SIM2-F-06, SIM3-F-05, SIM4-F-05, SIM5-F-09, SIM6-F-01/07/08, SIM7-F-02/05, SIM8-F-01
All logged in §5.8 of compiled Stage 3.

### Editorial pending (unchanged from prior session)
- Territory names
- Varfell victory tuning
- 10 seasonal event cards
- Restoration NPCs
- Niflhel primus inter pares
- Varfell Private Collection transfer
- E-01 (assassination perpetrator)
- E-03 (AG calendar name — now blocked on AG→AS rename batch)

### Deferred tasks (next session)
1. Haiku batch: Solmund rename (all files), AG→AS calendar, Church of Galbados→Church of Solmund
2. Cross-stage terminology check: Stages 4–17 may reference old TT/ThS/CD terms
3. Stage 4 cross-reference: SIM5-F-08 (RS threshold +1 Ob at Southernmost)
4. Phase 3 gate: simulation coverage matrix now runnable against compiled Stage 3

### Resume instruction for next session
Read session_log_current.md. Phase 2 compilation is complete (all 17 TTRPG stages + BG compiled; Stage 3 now current). Priority 1: Haiku batch renames (Solmund, AG→AS, Church). Priority 2: Cross-stage terminology audit for TT/ThS references in Stages 4–17.

---

session_id: 2026-03-28T_BATCH_RESOLUTIONS
phase: Phase 2 Compilation — combat testing in progress (TTRPG); BG/Hybrid Thread commits pending
status: OPEN — batch resolutions committed; combat testing ongoing

## SESSION SUMMARY

### What was accomplished
- 37 gap register items resolved via PP-094–PP-130
- All derived from canon constraints + compiled stages — no editorial approval required
- valoria_patch_proposals.md updated (PP-094–PP-130 appended)
- valoria_gap_register_consolidated.md updated (status log appended)

### Resolutions by category
- Social system: G-099 (mid-Debate incapacitation), G-100 (Renown scope)
- Faction/political: G-101–G-104, G-111–G-114, G-131, G-132 (Stability floor), G-136 (TC brake fix)
- Faction stats: G-133 (Niflhel Intel=6), G-115 (archetype stat blocks)
- Thread operations: G-116–G-118, G-125, G-127–G-130, SIM2-F-03/04/09, SIM5-F-02/07, SIM6-F-03/05/10, SIM7-F-03/07/08/09/10, SIM8-F-09/10
- Mass combat: G-135 (damage formula)
- NPC: G-129 (Torben TLK drain rate)
- Documentation/asymmetry: SIM3-F-02/03 (Crown/Hafenmark Thread asymmetry — intentional, now documented)

### Key design decisions
- PP-109: Dissolution Residue drains Certainty (not Coherence) — resolves SIM5-F-07 by proxy
- PP-114: Stability floor removed; Faction Fracture at Stability 0 for 2+ seasons; Crown/Church exception defined
- PP-118: Church Stability TC brake standardised to ≤3 (was ≤4/≤5 conflict between stages)
- PP-107: Past-Oriented Pulling complete — recency table, degree table, accessibility note, Foundational scale protocol
- PP-100: Devout Discovery Event bypass rewritten to theological confrontation (not TS-gated witnessing)
- PP-104: GEN-03/06/07 stat blocks written (Inquisitor, Riskbreaker, Knight Templar)

### GitHub state (all committed)
- valoria_patch_proposals.md — PP-094–PP-130 appended
- valoria_gap_register_consolidated.md — batch resolution log appended, ~37 items marked Resolved/Closed

### Still open (not resolved this session)
- P1 remaining design: G-025–G-033 (board game architecture — requires more design context)
- Sim-derived P2 open: ~51 items (SIM-F series, various)
- Hybrid design: 14 items (G-078–G-095 series)
- Rename batch (Solmund/AG→AS/Church): still deferred
- Cross-stage terminology audit (TT/ThS/CD refs Stages 4–17): still deferred
- Editorial pending: unchanged (8 items)

### Combat testing status (user-reported)
- TTRPG combat system under active test
- Thread changes committed
- BG/Hybrid mode commits pending (user handling)

### Resume instruction for next session
Read session_log_current.md. Phase 2 complete; Phase 3 simulation underway. 37 gaps resolved this session (PP-094–PP-130). Next priorities: (1) compile resolved patches into relevant stages (Stage 3, 5, 6, 8, 9, 13); (2) deferred Haiku rename batch; (3) cross-stage terminology audit. P1 board game design gaps (G-025–G-033) remain unstarted and block BG compilation stages.

---

session_id: 2026-03-28T_BATCH_RESOLUTIONS
phase: Phase 2 Compilation — combat testing in progress (TTRPG); BG/Hybrid Thread commits pending
status: OPEN — batch resolutions committed; combat testing ongoing

## SESSION SUMMARY

### What was accomplished
- 37 gap register items resolved via PP-094–PP-130
- All derived from canon constraints + compiled stages — no editorial approval required
- valoria_patch_proposals.md updated (PP-094–PP-130 appended)
- valoria_gap_register_consolidated.md updated (status log appended)

### Resolutions by category
- Social system: G-099 (mid-Debate incapacitation), G-100 (Renown scope)
- Faction/political: G-101–G-104, G-111–G-114, G-131, G-132 (Stability floor), G-136 (TC brake fix)
- Faction stats: G-133 (Niflhel Intel=6), G-115 (archetype stat blocks)
- Thread operations: G-116–G-118, G-125, G-127–G-130, SIM2-F-03/04/09, SIM5-F-02/07, SIM6-F-03/05/10, SIM7-F-03/07/08/09/10, SIM8-F-09/10
- Mass combat: G-135 (damage formula)
- NPC: G-129 (Torben TLK drain rate)
- Documentation/asymmetry: SIM3-F-02/03 (Crown/Hafenmark Thread asymmetry — intentional, now documented)

### Key design decisions
- PP-109: Dissolution Residue drains Certainty (not Coherence) — resolves SIM5-F-07 by proxy
- PP-114: Stability floor removed; Faction Fracture at Stability 0 for 2+ seasons; Crown/Church exception defined
- PP-118: Church Stability TC brake standardised to ≤3 (was ≤4/≤5 conflict between stages)
- PP-107: Past-Oriented Pulling complete — recency table, degree table, accessibility note, Foundational scale protocol
- PP-100: Devout Discovery Event bypass rewritten to theological confrontation (not TS-gated witnessing)
- PP-104: GEN-03/06/07 stat blocks written (Inquisitor, Riskbreaker, Knight Templar)

### GitHub state (all committed)
- valoria_patch_proposals.md — PP-094–PP-130 appended
- valoria_gap_register_consolidated.md — batch resolution log appended, ~37 items marked Resolved/Closed

### Still open (not resolved this session)
- P1 remaining design: G-025–G-033 (board game architecture — requires more design context)
- Sim-derived P2 open: ~51 items (SIM-F series, various)
- Hybrid design: 14 items (G-078–G-095 series)
- Rename batch (Solmund/AG→AS/Church): still deferred
- Cross-stage terminology audit (TT/ThS/CD refs Stages 4–17): still deferred
- Editorial pending: unchanged (8 items)

### Combat testing status (user-reported)
- TTRPG combat system under active test
- Thread changes committed
- BG/Hybrid mode commits pending (user handling)

### Resume instruction for next session
Read session_log_current.md. Phase 2 complete; Phase 3 simulation underway. 37 gaps resolved this session (PP-094–PP-130). Next priorities: (1) compile resolved patches into relevant stages (Stage 3, 5, 6, 8, 9, 13); (2) deferred Haiku rename batch; (3) cross-stage terminology audit. P1 board game design gaps (G-025–G-033) remain unstarted and block BG compilation stages.


---

session_id: 2026-03-29T_PHASE0_INFRASTRUCTURE
phase: Phase 0 (Infrastructure) — steps 0.1–0.18 complete
status: CLOSED — user actions 0.19–0.22 pending
---

session_id: 2026-03-29T_COMBAT_SIMULATION
phase: Combat System Design — complete
status: CLOSED

## SESSION SUMMARY

### Completed
- Full combat system redesigned and simulated from scratch
- Binary weapon system confirmed: Light/Heavy × Cut/Blunt × Short/Long
- TN gradient: LightCut 5/6, HeavyCut+LightBlunt 6/7, HeavyBlunt 7/8
- Versatile weapon category removed
- Establish Distance: TN7 vs opponent offence successes; auto-succeeds if opponent not attacking
- Feint vs Establish Distance: direct contest (feint TN-1 vs TN7), tie goes to feint
- Initiative: structural (correct range) > hit-and-not-hit > Agi Ob2 roll
- Disarm: offence vs defence; retrieve on TN7 vs opponent offence successes
- Stamina system: OOB + Full Guard both give opponent +2D
- Critical hits: excess >= 3, weapon modifier doubled
- Mass mismatch penalty: -1 defensive success when Light splits vs Heavy (not Full Guard, not Long-at-Close)
- Wound system: Variant B selected — HP=End (flat), armour=DR per weapon type
- DR table: varies by weapon type vs armour tier (LightCut/HeavyCut/LightBlunt/HeavyBlunt)
- Long weapons at Close zone: -1D offence, half damage, type unchanged
- Group combat: zone collapse (first closer opens zone for allies) + Fibonacci bonus
- Historical manual analysis: Fiore, Silver, Liechtenauer, Talhoffer, Meyer
- Simulation: 400+ matchups, 2000 fights each, randomised character parameters
- Key finding: offence% has near-zero correlation with winning (r≈0.01)
- Heavy weapons confirmed as situationally powerful — correct in armoured and group contexts

### Files pushed
- compilation/valoria_combat.docx — complete combat system write-up

### Simulation files (local /home/claude/)
- combat_v6.py through combat_v11.py — progressive rule iterations
- combat_v8_matrix.py — full weapon×armour matrix

### Key decisions
- No versatile weapons
- No medium weapon category
- Cut/Blunt as primary damage type axis (not weight alone)
- STR stays in damage formula
- No bind mechanic (too granular)
- No cutting/blunt TN split beyond weight
- Puncture not a separate axis
- Heavy weapons situationally powerful, not generally dominant

### Resume instruction
Combat system complete and compiled. Next: group combat simulation (Fibonacci + zone
collapse together), then push combat mechanics into main compilation checkpoint.
Pending user actions 0.19-0.22 from Phase 0 still outstanding.

---

session_id: 2026-03-29T_COMBAT_GROUP_SIM
phase: Combat Group Simulation — complete
status: CLOSED

## SESSION SUMMARY

### Completed
- Group combat simulation: Fibonacci + zone collapse (sim_combat_group.py)
- Rescue / multi-engagement simulation (sim_combat_rescue.py)
- Tie Up / bind exhaustive proposition testing (sim_combat_tieup.py)
- Exhaustive group combat matrix (sim_combat_exhaustive.py)
- v11 single combat sim with mass mismatch penalty (sim_combat_v11.py)

### Key findings
- 3v1 universally decisive (99-100%) regardless of weapon/armour
- 2v1 is the tactically interesting zone — weapon type and armour matter
- LightCut vs Heavy armour at 2v1: only 56% attacker win (contested)
- HeavyBlunt is correct weapon for armoured targets at any numerical parity
- 3v2 produces 40-87% draw rate — parallel engagements resolve simultaneously
- Survival/rescue window: 2-3 rounds (after round 3, 75-80% of losers have fallen)
- HeavyCut dominates 1v1 (75% vs LightCut); HeavyBlunt is armoured specialist
- Tie Up mechanic not needed — Option A accepted (system correct without it)
- Mass battle abstraction confirmed: Fibonacci → flanking modifier,
  zone collapse → formation break, rescue → reserve timing,
  weapon type → unit specialisation, DR → unit armour rating

### Files pushed
- tests/sim_combat_group.py
- tests/sim_combat_rescue.py
- tests/sim_combat_tieup.py
- tests/sim_combat_exhaustive.py
- tests/sim_combat_v11.py
- compilation/valoria_combat.docx (previous session)

### Design notes logged
- Mass battle abstraction: 5 unit stats + 2 rolls per engagement
- Heavy armoured elite unit holds 2v1 vs wrong weapon type (56%)
- Requires 3v1 or correct weapon (HeavyBlunt) to break reliably
- Reserve timing critical: 2 battle turns = rescue window

### Resume instruction
Combat system fully simulated and validated. Next:
- Integrate group combat mechanics into valoria_combat.docx
- Design mass battle unit stat block (weapon type, armour tier,
  pool/cohesion, DR, Fibonacci modifier)
- Phase 0 user actions 0.19-0.22 still pending

---

session_id: pending
phase: pending
status: OPEN

## RESUME FROM
See session_log_archive.md — last block: 2026-03-29T_COMBAT_GROUP_SIM

## NEXT ACTIONS
1. Integrate group combat into valoria_combat.docx
2. Design mass battle unit stat block (5 stats + 2 rolls)
3. Phase 0 user actions 0.19-0.22 still pending


---

```yaml
session_close: 2026-03-29
checkpoint: Thread Operation Catalog expanded
completed:
  - "stage15_spell_catalog.md expanded (24 → ~95 operations, 72 → 464 lines)"
  - "Coverage added: combat, mass combat, debate, faction actions, siege, collective ops, board game orders, Southernmost, monstrous entities"
  - "Mending operations: 0 → 8 entries"
  - "Past-Oriented Pulling: 1 → 6 entries"
  - "TS Mastery Bonus rule: +1 per 20 TS above min, cap +3, TS 100 uncapped (+2 additional = +5 at Object/Personal)"
  - "TS minimums corrected to Stage 3 authoritative values (30/50/70)"
  - "Canon compliance verified P-01 through P-14"
  - "Pushed to GitHub: commit 78d5597dcc48"
new_rules:
  - "TS Mastery Bonus (universal rule, catalog header)"
editorial_pending:
  - "PO-06: The Great Unwinding (campaign-endpoint Past-Oriented Pulling)"
  - "CO-04: The Great Working (campaign-endpoint collective operation)"
  - "W-42: Crowd Coherence in Debates (Thread manipulation of audience)"
  - "W-51: Mandate Reinforcement via Weaving (political power balance)"
  - "FR-L-05: Locked Institution chronic severity (-2/season)"
  - "W-06c: Mode 3 conventional Dissolution immunity"
next_action:
  - "Integrate TS Mastery Bonus into stage3_thread_operations.md"
  - "Stress test Mastery Bonus at TS 100 across operation types"
  - "Resolve 6 editorial flags"
```
---
session_id: pending
phase: pending
status: OPEN

## RESUME FROM
See session_log_archive.md — last block: 2026-03-29T_COMBAT_GROUP_SIM

## NEXT ACTIONS
1. Mass combat unit stat block — specific values (pool sizes, cohesion thresholds,
   morale mechanics) flagged [EDITORIAL] in stage8_combat.md §8.9
2. Phase 0 user actions 0.19-0.22 still pending
3. Integrate remaining gap register items per workplan


---

session_id: 2026-03-29T_THREADWEAVING_COMBAT_SIM
phase: Threadweaving × Combat Simulation
status: CLOSED

## SESSION SUMMARY

### Completed
- Stress test matrix v2 reconstructed: 35 cells, 6 clusters (A–F)
- Comprehensive simulation: 31 cells tested, 13 P1, 13 P2, 5 P3 findings
- Extreme stress tests: 18 break attempts, 12 P1, dominant strategies identified
- Narrative stress tests: 4 multi-system scenarios (debate→combat→thread→faction)
- 23 patches drafted (PP-131–153), reviewed for conflicts (zero found), committed
- 6 gap resolutions (GP-01–06) resolving all threadweaving×combat blocking gaps
- 5 edge case rulings formalized
- Wound system redesigned (PP-131): continuous HP track, -1D/wound, carryover damage
- E-06 editorial ruling (Personal Lock in combat) fully integrated

### Key design findings
- Personal Pull is dominant combat Thread operation (0 Coherence, -2D, scene duration)
- Personal Dissolution is 70% assassination at optimized stats (no resistance roll)
- Practitioners dominate every system they touch; cost is world-state degradation (RS, TC, Coherence)
- Rock-paper-scissors confirmed: practitioners beat structures, fighters beat unprotected practitioners, Church politics beat practitioners' long-term interests
- Thread operations during Debates are powerful and nearly undetectable
- Contact windows carry across system transitions (Debate→Combat) seamlessly

### Files pushed
- valoria_patch_proposals.md (PP-131–153 + GP-01–06 appended)
- tests/sim_thread_combat_matrix_v2.md
- tests/sim_thread_combat_comprehensive.md
- tests/sim_thread_combat_extreme.md
- tests/sim_thread_combat_narrative.md

### Editorial pending (8 items)
1. Personal Pull balance (0 Coherence, -2D, scene duration)
2. Personal Dissolution lethality (resistance roll?)
3. Heal loop mitigation (Overweave acceleration)
4. Pull stacking floor (half base pool?)
5. Mass Lock RS drain cap
6. Weaving effect on Debates (+2D or +1D)
7. Structural Pulling vs Fortification resistance
8. Catastrophic TC surge Accounting bypass

### Resume instruction
Read session_log_current.md. 8 editorial decisions block further simulation. PP-131 invalidates all prior combat sim data — re-simulation needed after editorial resolution. Opus-tier work (E-05, E-06 downstream, F-06) deferred until editorial on items 1-2.

---

session_id: 2026-03-30T_GM_REF_P1
phase: open
status: PHASE_1_COMPLETE

## SESSION SUMMARY
GM Reference Suite Phase 1 complete. 10 mechanical deliverables committed to gm_ref/.

## FILES COMMITTED
- gm_ref/gm_reference_workplan.md — full workplan
- gm_ref/d01_cascade_consequence_reference.md — clock thresholds + cross-effects
- gm_ref/d02_seasonal_accounting_form.md — offline accounting worksheet
- gm_ref/d03_gm_dashboard.md — live state reference
- gm_ref/d04_gap_escalation_table.md — Gap age → Mend Ob + severity tables
- gm_ref/d05_coherence_band_track.md — band penalties + fallout tables
- gm_ref/d06_thread_operation_resolution_card.md — operation procedure + co-movement mechanical layer
- gm_ref/d07_npc_state_cards.md — 9 principal NPCs with clocks, Beliefs, triggers
- gm_ref/d08_knot_registry_template.md — per-practitioner Knot tracking form
- gm_ref/d09_comovement_matrix_skeleton.md — 18-cell matrix skeleton (Opus fill pending)
- gm_ref/d10_framing_process_skeleton.md — 4-step improvisation process (Opus fill pending)

## NEXT ACTION
Phase 2 — Opus tasks (4 artifacts, sequential):
1. D-11: Fill co-movement matrix narrative cells (d09 skeleton → complete)
2. D-12: Fill framing process philosophical content (d10 skeleton → complete)
3. D-13: Write 8–12 annotated examples (split-register format)
4. D-14: Write 4–6 counter-examples

Phase 2 requires user to initiate each Opus artifact. Tasks 1+2 can run in parallel.
Phase 3: assemble complete suite after all Phase 2 outputs approved.

## OPEN ITEMS
- D-07 NPC state cards: faction stat values left as blanks (fill from live Dashboard)
- D-09/D-10: all [OPUS] sections are explicit placeholders, clearly marked
- Solmund rename (Galbados→Solmund) not yet applied to new gm_ref files — apply at Phase 3 assembly
