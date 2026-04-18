# Valoria — Complete System Audit & Architecture Reference
## 2026-04-18 | Compiled from 4 audit passes

**Contents:**
1. System Audit Part 1 — Six Core Systems (Combat, Fieldwork, Social Contest, Threadwork, Player Agency, NPC Behavior)
2. System Audit Part 2 — Remaining 12 Systems
3. Throughlines, Transitions, Echoes & Scale Hierarchy
4. **Interdependency Matrix** (NEW)
5. **Resolution Engine & Statistical Matrix** (NEW)

---
---

# ═══════════════════════════════════════════════════════
# SECTION 1: SYSTEM AUDIT — SIX CORE SYSTEMS
# ═══════════════════════════════════════════════════════

# 1. COMBAT (combat_v30.md)

## Quality: 8/10

The combat system is mechanically complete and internally consistent. Pool construction (Agility × 2 + History + 3), TN 7, simultaneous declaration with initiative-based information advantage — the core loop is tight. The weapon TN matrix (three binary axes producing 8 weapon profiles) is the standout design: it replaces equipment lists with a combinatorial system that players can intuit. Short Light Blade = TN 5 (fast, precise), Long Heavy Blunt = TN 8 (slow, devastating). STR minimums create build constraints without hard-gating.

**Deficiencies:**
- §4 action priority table has a note "THIS DOESN'T MAKE SENSE RE PRIORITY. IT'S ALL SIMULTANEOUS" — an unresolved internal flag in a canonical doc. The priority table conflicts with the Phase 2 simultaneous declaration structure.
- Rescue (§4, §8) is the most complex single action in the game: 280+ words of rules, 5 patches, 3 sub-conditions.
- Ranged weapons (§5) are flagged ED-129 as "pending integration" into the TN matrix.

## Historical Precedent: Strong (Burning Wheel + KOEI)

Pool-split offense/defense from BW's Fight! system. Wound interval from BW's mortal wound threshold. Fibonacci group bonus is original. Initiative-as-information-advantage from BW's scripted combat simplified. Weapon system's binary-axis construction is closer to roguelike weapon generation (Caves of Qud) than to traditional RPG weapon lists.

## Smoothness: 7/10

Integrates cleanly with fieldwork (§11.5 transitions), Thread (§10), and the faction layer (§13 World Bridge). Death Cascade (§13.3) is well-integrated — one kill fires consequences across Knot networks, Scene Slate, faction Stability, Exposure, and Conviction. Friction: §9 mass combat uses pre-PP-232 stat names; references deprecated doc for PP-089/090; two different damage formulas for personal-scale vs full mass battle.

## Robustness: 9/10

Extensively simulated (sim_combat_batch_11, sim_x_06). Wound degradation smooth curve, no single-wound cliffs. Range control more fight-determining than pool size — confirmed intentional. Weapon TN matrix produces meaningful differentiation across armor types. Unsimulated: Rescue interaction with Fibonacci in 4v3+ engagements.

## Elegance: 7/10

Core loop elegant. Action list long (10+ actions). Three resource tracks in combat (pool dice, wound progress, Stamina) — Stamina could be folded into pool depletion.

## Necessity: Essential
## Contribution: Emergence High, Agency Very High, Strategic Depth High

### Flags
- **AUD-COM-01:** §4 action priority contradicts §2 simultaneous declaration. [P2]
- **AUD-COM-02:** §9 pre-PP-232 stat names. [P3]
- **AUD-COM-03:** §9 PP-089/090 references deprecated doc. [P3]
- **AUD-COM-04:** ED-129 ranged TN matrix integration pending. [P2]
- **AUD-COM-05:** Stamina merge with pool depletion. [P3, design proposal]

---

# 2. FIELDWORK (fieldwork_v30.md)

## Quality: 9/10

Strongest individual system. Intelligibility Gradient (Depth 0–5) unifies exploration, investigation, and socializing. Evidence Track is a simple progress clock with reliability tags. Disposition Track (−3 to +5) parallels Depth axis for social access. Exposure system (Cover-derived thresholds) creates clean risk/reward.

Deficiency: §5.9 Demand deflection Ob (floor(NPC highest stat ÷ 2) + 2) may be prohibitively high for mid-game characters. Thread-Read investigation superiority at Depth ≥ 4 not offset by sufficient cost.

## Historical Precedent: Exceptional

Obra Dinn (Evidence Track), Persona 5 (Disposition/Confidant), Disco Elysium (skill-gated perception), Hitman (Exposure/threat meter), BW (Circles/Sincerity Gate). The unified system under one pool formula is original.

## Smoothness: 9/10
## Robustness: 8/10 (SIM-DEBT-FW-01 through FW-06 all resolved)
## Elegance: 8/10 (Depth/Disposition parallel is elegant; total system is large)
## Necessity: Essential
## Contribution: Emergence Very High, Agency Very High, Strategic Depth Very High

### Flags
- **AUD-FW-01:** Demand deflection Ob may be prohibitive. [P3]
- **AUD-FW-02:** Thread-Read superiority at Depth ≥ 4 insufficiently offset. [P3, design proposal]

---

# 3. SOCIAL CONTEST (social_contest_v30.md)

## Quality: 9/10

Four interaction types (CLASH, REINFORCE, CROSS, TIE) create genuine tactical decisions. Conviction Track (0–10) with audience resistance parallels armor DR. Genre system (Memory/Projection × Revealing/Obscuring) with faction-specific audience boosts. Obligation system creates multi-season consequences. Chain Contests generate follow-up scenes.

Deficiencies: §1 Core Principle section empty. CROSS interaction floor(÷2) may be non-viable against Resistance 2+.

## Historical Precedent: Strong (BW Duel of Wits + Persona)
## Smoothness: 9/10
## Robustness: 7/10 (SIM-DEBT-03/04 outstanding since PP-234)
## Elegance: 9/10
## Necessity: Essential
## Contribution: Emergence High, Agency Very High, Strategic Depth Very High

### Flags
- **AUD-SC-01:** §1 Core Principle empty. [P3]
- **AUD-SC-02:** CROSS floor(÷2) may be non-viable at Resistance 2+. [P2]
- **AUD-SC-03:** SIM-DEBT-03/04 outstanding. [P2]

---

# 4. THREADWORK (threadwork_v30.md)

## Quality: 8/10

Most conceptually ambitious system. Five operation types (Weaving, Pulling, Locking, Dissolution, Mending) with Coherence degradation (10→0) as emotional engine. Leap-as-rendering-suspension creates combat vulnerability. Rendering Crisis at Coherence 0 produces the game's most powerful narrative arc.

Deficiencies: §4.1/4.2 empty stubs (Co-Movement foundation text). Three-axis Ob system canonical in params_threadwork but struck from design doc without clear cross-reference. N-Way Opposing Operations (3+ practitioners = auto-collapse) is a blunt ceiling.

## Historical Precedent: Unique

No game makes supernatural power self-destructive at the identity level. Closest: Unknown Armies' madness meters, but Coherence erodes ontological stability, not psychological.

## Smoothness: 8/10 (FR cap exemption PP-196 adds complexity; residue cap interaction varies by scale)
## Robustness: 6/10 (Co-Movement cards unsimulated; RS campaign variance unknown)
## Elegance: 7/10 (Core elegant; exceptions accumulate)
## Necessity: Essential
## Contribution: Emergence Exceptional, Agency High, Strategic Depth Very High

### Flags
- **AUD-TW-01:** §4.1/4.2 empty. [P2]
- **AUD-TW-02:** params_threadwork Ob alignment unverified. [P2]
- **AUD-TW-03:** N-Way auto-collapse — consider graduated. [P3, design proposal]

---

# 5. PLAYER AGENCY (player_agency_v30.md)

## Quality: 9/10

Solves "what should I do?" with three interlocking layers: Convictions (player-authored goals), Duties (faction-assigned objectives), Scene Slate (procedurally generated opportunities). Precedent analysis cites ROTK, CK3, Disco Elysium, Mount & Blade, Pathologic 2, Pentiment — each with named mechanical contribution. Conviction resolution states (Fulfilled/Failed/Transformed/Unresolved) with Sufficient Scope gate. Portrait Retirement as player-controlled character conclusion.

Deficiencies: Scene Slate variety over 30+ stable seasons needs simulation. Independent path generates fewer opportunities.

## Historical Precedent: Exceptional
## Smoothness: 10/10 (pure meta-system with no new resolution mechanics)
## Robustness: 7/10 (Slate generation algorithm untested across full campaign arc)
## Elegance: 9/10
## Necessity: Essential
## Contribution: Emergence Exceptional, Agency Maximum, Strategic Depth High

### Flags
- **AUD-PA-01:** Slate variety over 30+ seasons needs sim. [P2]
- **AUD-PA-02:** Independent path fewer opportunities. [P3]

---

# 6. NPC BEHAVIOR (npc_behavior_v30.md)

## Quality: 9/10

Most sophisticated AI architecture. Stance Triangle (Conviction × Resonant Style × Ethical Framework), 7-type Conviction Taxonomy, Belief revision via Conviction Scars, Arc State Machines (A/B/C branches). Decision Derivation (§4): Institutional Filter → Conviction Filter → Decision Fork, with Scar count determining fork resolution. 14 named NPC profiles.

Deficiencies: 7 NPCs missing TS/Certainty values. Knot formation during play unspecified (blocks Solidarity targeting). Conviction crisis d6 table may produce faction-incoherent actions.

## Historical Precedent: Strong (CK3 + Nemesis System)
## Smoothness: 9/10 (connective tissue between all systems)
## Robustness: 6/10 (least-simulated major system; priority trees untested cross-faction)
## Elegance: 7/10 (architecture elegant; total surface area enormous)
## Necessity: Essential
## Contribution: Emergence Maximum, Agency High (indirect), Strategic Depth Very High

### Flags
- **AUD-NPC-01:** Knot formation during play unspecified. [P1]
- **AUD-NPC-02:** 7 NPC stat gaps. [P2]
- **AUD-NPC-03:** Priority tree cross-faction interactions unsimulated. [P2]
- **AUD-NPC-04:** Conviction crisis d6 — consider weighted table. [P3, design proposal]

---
---

# ═══════════════════════════════════════════════════════
# SECTION 2: SYSTEM AUDIT — REMAINING 12 SYSTEMS
# ═══════════════════════════════════════════════════════

# 7. MASS BATTLE (mass_battle_v30.md) — Quality 9/10

Core formula: Effective Pool = min(Size, Command) + Command. Generalship dominates. 7-phase turn structure with simultaneous damage application. Formation counter logic (rock-paper-scissors). Campaign Supply and Levy Restriction model historical military economics. BG abstraction resolves in 3–5 minutes. Hybrid handoff via phase-lock points.

Robustness 8/10 (extensively simulated; splitting doctrine quantified). Elegance 7/10 (core clean; implementation dense). Contribution: Emergence High, Agency High, Strategic Depth Very High.

**Flags:** AUD-MB-01 (duplicated PP-249 paragraph, P3), AUD-MB-02 (Part C editorial items pending, P2).

---

# 8. SCALE TRANSITIONS (scale_transitions_v30.md) — Quality 9/10

Architectural backbone. Eight handoff rules covering every scale crossing. Zoom In/Out with phase-lock points. Domain Echo with Sufficient Scope gating (7 conditions). "Where Were You?" retrospective scene is a standout innovation.

Smoothness 10/10 (IS the smoothness system). Robustness 7/10 (simultaneous Echo stacking untested). Elegance 9/10. Contribution: Emergence High, Agency Moderate, Strategic Depth High.

**Flags:** AUD-ST-01 (simultaneous Domain Echo cap interaction, P3).

---

# 9. VICTORY (victory_v30 + peninsular_strain_v1) — Quality 9/10

Universal victory (Peninsular Sovereignty) unifies all factions; asymmetric toolkits differentiate paths. Accord system incentivizes diplomacy over military conquest (conquered territories don't produce). Church Graduated Seizure scales with TC.

Robustness 7/10 (5-faction race unsimulated end-to-end). Elegance 8/10 (Accord rules split across two docs). Contribution: Emergence High, Agency High, Strategic Depth Very High.

**Flags:** AUD-VIC-01 (Accord rules split, P3), AUD-VIC-02 (RM win probability unsimulated, P2).

---

# 10. SETTLEMENT LAYER (settlement_layer_v30.md) — Quality 8/10

Two-Tier Map (provinces for factions, settlements for players). 36 settlements. Dual-Authority governance. Church infrastructure (4 independent axes) with Parish Social Services ("Geneva trap"). RM Cell Resilience. Institutional Facility Tiers gate rank advancement to physical settlement capacity.

Robustness 5/10 (entirely unsimulated). Elegance 7/10 (architecture clean; system large). Contribution: Emergence Very High, Agency Very High, Strategic Depth Very High.

**Flags:** AUD-SET-01 (Order averaging caps Accord, P2), AUD-SET-02 (Accord propagation not done, P1), AUD-SET-03 (36-settlement economy unsimulated, P2).

---

# 11. DERIVED STATS (derived_stats_v1.md) — Quality 9/10

Separates structural capability (1–7 stats) from current state (granular derived values). Cascade rule: derived → 0, stays through Accounting → stat −1. Player-facing display conceived (stat bars + resource numbers).

Robustness 6/10 (all multipliers PROVISIONAL). Necessity: Essential for videogame.

**Flags:** AUD-DS-01 (all values provisional, no faction economic simulation, P1).

---

# 12. FACTION POLITICS (faction_politics_expanded_v1.md) — Quality 8/10

Five rank ladders, branch specialization, Ministry/Committee/Dicastery Competence tracks.

Robustness 5/10 (947 lines unsimulated, 5 SIM-POL deferred).

**Flags:** AUD-FP-01 (unsimulated, P1).

---

# 13. CONVICTION TRACK (conviction_track_v30.md) — Quality 8/10

Per-territory stat (0–5), movement rules, Calamity Drift, Thread Operation CV Drift. Consecrated Status creates Church snowball.

Smoothness 7/10 (CV/PT terminology inconsistency).

**Flags:** AUD-CT-01 (CV→PT rename deferred, P3).

---

# 14. CHARACTER HISTORIES (character_histories_v30.md) — Quality 8/10

Four-stage lifepath with SaGa-style sparking. Literacy model gates archival investigation. Lifepath outputs feed all systems.

**Flags:** AUD-CH-01 (Coherence erosion → Recall → skill access, P3).

---

# 15. INVESTIGATION SYSTEMS (investigation_systems_proposal) — Quality 9/10

Four interlocking systems (NPE, Investigation Interface, Dialogue Lattice, Response Matrix) sharing the Ontological Ledger. NPE generates procedural NPCs with 5-axis Genome from territory ecology. Dialogue Lattice gates utterances by character state.

Robustness 6/10 (Volatility-driven convergence may flatten diversity over long campaigns).

**Flags:** AUD-INV-01 (NPE convergence risk, P3).

---

# 16. COMPANION SPECIFICATION (companion_specification_v30.md) — Quality 9/10

Clean, compact (221 lines). Companion vs recruited NPC distinction. 5-rule combat AI. Max 2 active.

No flags.

---

# 17. CLOCK REGISTRY (clock_registry_v30.md) — Quality 9/10

Single source of truth for all clocks/tracks/counters. 123 lines. Pure reference.

**Flags:** AUD-CK-01 (settlement derived value tracks not yet listed, P3).

---

# 18. UI/UX (valoria_ui_ux_v4_1.md) — Quality 9/10

1431 lines, 14 parts + 5 appendices. Three Design Oaths with violation tests. 14-state FSM. Capability-gated chrome ("the player earns their HUD").

**Flags:** AUD-UI-01 (derived stats display not integrated, P2), AUD-UI-02 (settlement map view not specified, P2).

---

## System Quality Rankings (All 18)

| Tier | Systems |
|------|---------|
| 9/10 | Fieldwork, Social Contest, Player Agency, NPC Behavior, Mass Battle, Scale Transitions, Victory, Derived Stats, Investigation, Companion, Clock Registry, UI/UX |
| 8/10 | Combat, Threadwork, Settlement, Faction Politics, Conviction Track, Character Histories |

---
---

# ═══════════════════════════════════════════════════════
# SECTION 3: THROUGHLINES, TRANSITIONS, ECHOES & HIERARCHY
# ═══════════════════════════════════════════════════════

## 3.1 Throughlines

### Numbered Throughlines (TL-1 through TL-10)

| # | Name | Status |
|---|------|--------|
| TL-1 | Caste Starting-State Onboarding | Resolved (PP-661) |
| TL-2 | Standing 0 Initiation Duty | Resolved (PP-661) |
| TL-3 | TC × Warden Asymmetry + RM Ladder | Resolved (PP-661), RM stub open |
| TL-4 | Generational × Coup × IP Convergence | Resolved (PP-661) |
| TL-5 | NPC Roster Capacity | Resolved (PP-661) |
| TL-6 | Hall Tier Settlement Integration | Resolved (PP-661) |
| TL-7 | Warden × Thread Stress Test | Open (P0) |
| TL-8 | ED-NEW-06 Lineage | Closed |
| TL-9 | SIM-POL Discoverability | Resolved |
| TL-10 | Register Split | Deferred |

### Tagged Throughlines (T1–T8)

| Tag | Name | What It Connects |
|-----|------|-----------------|
| T1 | Settlement-Level Thread | Thread ops → settlement Order/Defense changes |
| T2 | Personal Resources/Economics | Player Resources (0–5) ↔ settlement/faction Treasury |
| T3 | Settlement POI Templates | POIs per settlement (not province); 7 narrative-critical named POIs |
| T4 | Registrar Haelgrund | Ministry ↔ archives ↔ Thread artifacts ↔ institutional neutrality |
| T5 | Martial Law at Settlement Level | Löwenritter governance → Order +2, Accord −1/season |
| T6 | *(unassigned — gap)* | — |
| T7 | Local Actors | Settlement-generated lightweight NPCs |
| T8 | Conviction Legacy | PC death/retirement → transformed Conviction carries forward |

### Implicit Throughlines

| Name | Systems Involved |
|------|-----------------|
| Church Creep | settlement_layer §1.5–1.7, conviction_track, victory §3.2, peninsular_strain §5.2 |
| RS Pressure | threadwork §5, conviction_track §1.3, mass_battle §A.14, peninsular_strain §3.1 |
| Reputation Cascade | combat §13.2, player_agency §5.4, npc_behavior §8.11, fieldwork §5.1 |
| Epistemic Progression | character_histories, threadwork §3.4, investigation_systems, npc_behavior §3.4 |
| Institutional Capture | player_agency §5.1, settlement_layer §3.2, derived_stats §3, victory §0 |

---

## 3.2 Scales of Play

```
PENINSULA (global clocks: RS, TC, IP, PI, Strain)
  └── TERRITORY (15 provinces: faction stats, derived values, Accord, PT)
        └── SETTLEMENT (36: Prosperity/Defense/Order, facilities, governor)
              └── SCENE (Evidence Track, Disposition, Exposure, Conviction Track)
                    └── ROUND (Combat Pool, Wounds, Stamina, Coherence, Contact)
```

---

## 3.3 Transition Points

### Upward (personal → faction/world): 11 pathways (DE-1 through DE-11)

| ID | From → To | Trigger | Mechanism |
|----|-----------|---------|-----------|
| DE-1 | Combat → Faction | Kill/defeat faction officer | Combat Domain Echo |
| DE-2 | Contest → Faction | Decisive win | Debate Domain Echo |
| DE-3 | Investigation → Faction | Evidence Track threshold (Complex+) | Investigation Domain Echo |
| DE-4 | Thread → Faction | RS change ≥1 or Scar fires or Territorial+ Gap/Lock/Knot | Thread Domain Echo |
| DE-5 | Personal scene → Accord | Public governance/destabilization/transfer/violence | Accord Domain Echo |
| DE-6 | Thread → Settlement | Relational+ Thread op in settlement | Settlement Thread Echo |
| DE-7 | Combat → Settlement | Public combat / governor combat / resident NPC kill | Settlement Combat Consequences |
| DE-8 | Combat → Garrison Strength | Player defends settlement | Garrison Strength feedback |
| DE-9 | Combat kill → NPC network | Named NPC killed | Death Cascade (5-step, no cap) |
| DE-10 | Conviction resolution → Renown | Any non-Unresolved resolution | Renown +1 |
| DE-11 | Battle → Peninsula | Inter-faction battle on Valorian soil | RS −1/−2, IP +2, Strain +1 |

### Downward (faction/world → personal): 9 pathways (ZI-1 through ZI-9)

| ID | From → To | Trigger | Mechanism |
|----|-----------|---------|-----------|
| ZI-1 | BG battle → TTRPG | PC faction leader in contested territory | BG defers to TTRPG mass battle |
| ZI-2 | BG action → TTRPG scene | Zoom In trigger | Phase-lock entry; scene Ob modified by BG degree |
| ZI-3 | Faction crisis → Mandatory scene | 7 mandatory triggers | Priority 0 Scene Slate |
| ZI-4 | World-state → Optional scene | 5 world-state triggers | Priority 1 Scene Slate |
| ZI-5 | NPC tree → Scene | Outreach/Demand conditions | npc_behavior §8.11 → Scene Slate Step 5 |
| ZI-6 | Clock threshold → Scene | RS/TC/IP band crossing | Scene Slate Step 2b |
| ZI-7 | Missed event → Retrospective | Player absent from major event | "Where Were You?" free scene |
| ZI-8 | Faction duty → Scene | Priority stack assigns duty | Duty-aligned scenes (Priority 2) |
| ZI-9 | Conviction → Scene | Conviction text intersects game state | Conviction-aligned scenes (Priority 3) |

### Lateral (system ↔ system): 10 pathways (LT-1 through LT-10)

| ID | Transition | State Transfer |
|----|-----------|----------------|
| LT-1 | Fieldwork → Combat | Exposure → Initiative advantage |
| LT-2 | Fieldwork → Contest | Evidence → +1D/Finding (max +2D) |
| LT-3 | Fieldwork → Thread | Thread-Read = Leap; co-movement fires |
| LT-4 | Fieldwork → Mass Battle | Suspends fieldwork; freezes Evidence |
| LT-5 | Combat → Fieldwork (post-combat) | 1 scene; Exposure codified |
| LT-6 | Combat → Fieldwork (fled) | No scene; site = POI; evidence degrades |
| LT-7 | Contest → Fieldwork | Appraise → +1 Evidence; Disposition ±1 |
| LT-8 | Personal combat ↔ Mass battle | General Duel: 1 exchange/turn, max 5 |
| LT-9 | Scene → Mass | Social/investigation win → +1D/free Reform (1 turn) |
| LT-10 | Thread → Faction | Thread op IS faction action (no extra roll) |

---

## 3.4 Echo Types (16 named)

| Echo | Trigger | Effect | Cap |
|------|---------|--------|-----|
| Domain Echo | Sufficient Scope (7 conditions) | ±1/±2 faction stat by degree | 1/scene/faction |
| Combat Domain Echo | Kill/defeat faction officer | Faction stat shifts | 1/scene/faction |
| Debate Domain Echo | Decisive contest win | Winner/Loser Mandate ±1 | Per contest |
| Accord Domain Echo | Personal governance/destabilization | ±1 Accord | ±1/territory/Zoom In |
| Thread Domain Echo | Thread Significance | Stat shift by event type | 1 Thread Echo/scene/faction |
| Settlement Echo | Combat/Thread at settlement | Order/Defense/Prosperity shifts | ±1/stat/season (Thread) |
| Death Cascade | Named NPC killed | 5-step cascade (no cap) | Full sequence fires |
| Conviction Scar | Decisive contest via Resonant Style | Scar +1 → behavior changes | 1/decisive win |
| Thread Co-Movement | Any Thread operation | 3-axis auto-effects + card draw | Per operation |
| Coherence Degradation | Relational+ ops, FR, residue | Coherence −1 per qualifying op | Per-op cap (FR exempt) |
| Calamity Drift | RS ≤50/35/20 | PT −1 in affected territories | Ignores ±1/season PT cap |
| Thread Op CV Drift | Public Thread event | CV/PT shift per type | ±2/territory/season combined |
| Morale Cascade | Unit routs | Adjacent units Discipline Ob 1 | Secondary can't cascade same turn |
| Knot Strain Propagation | NPC TS threshold crossing | Strain per TS band to Knotted | Per season |
| Obligation | Decisive Formal/Grand Contest | Binding commitment 2–4 seasons | Advisory 3 active |
| Framework Drift | Faction ethical framework | Passive stat changes per faction | Stat ceiling/floor |

---

## 3.5 Sufficient Scope Conditions

A personal scene qualifies for Domain Echo when it involves ANY of:
1. Named faction leader or representative
2. Direct challenge to faction institutional authority
3. Completed Complex/Structural investigation (Evidence Track ≥5) concerning faction institutional acts
4. Thread operation at Relational+ scale targeting faction configuration
5. Combat victory against named NPC holding faction office
6. Disposition +4/+5 with named NPC holding faction office
7. Settlement governance action changing Order by ±1+

Companion modifier: +1 net successes for Scope evaluation.

---

## 3.6 Gaps

| Gap | Priority |
|-----|----------|
| Knot formation during play unspecified (blocks Solidarity Resonant Style) | P1 |
| Accord propagation to settlement Order not done in downstream docs | P1 |
| T6 tag unassigned | P3 |
| Co-Movement deck reshuffle timing unspecified | P2 |
| UI spec missing derived stats display and settlement map | P2 |
| Independent player throughline unmapped end-to-end | P3 |
| Generational transition state transfer partially specified | P2 |

---
---

# ═══════════════════════════════════════════════════════
# SECTION 4: INTERDEPENDENCY MATRIX
# ═══════════════════════════════════════════════════════

How each system reads from and writes to every other system. **R** = reads from (depends on). **W** = writes to (modifies). **—** = no direct dependency.

|  | Combat | Fieldwork | Contest | Threadwork | MassBattle | ScaleTrans | Victory | PlayerAgency | NPCBehavior | Settlement | DerivedStats | FactionPol | ConvTrack | CharHist | InvestSys | Companion | ClockReg | UI/UX |
|--|--------|-----------|---------|------------|------------|------------|---------|-------------|-------------|------------|-------------|------------|-----------|----------|-----------|-----------|----------|-------|
| **Combat** | — | W | — | R | W | W | — | W | W | W | W | — | — | R | — | R | W | R |
| **Fieldwork** | W | — | W | R,W | W | W | — | W | R,W | R | — | — | — | R | R | R | W | R |
| **Contest** | — | R | — | R | — | W | — | W | R,W | W | — | — | — | R | — | R | W | R |
| **Threadwork** | R | R,W | R | — | R,W | W | — | W | W | W | — | — | W | R | — | R | W | R |
| **MassBattle** | R | — | — | R | — | W | W | — | — | W | W | — | — | R | — | R | W | R |
| **ScaleTrans** | R | R | R | R | R | — | W | R,W | R | R | R | — | — | — | — | R | R | R |
| **Victory** | — | — | — | — | R | R | — | — | — | R | R | — | R | — | — | — | R | R |
| **PlayerAgency** | — | R | R | — | — | R | — | — | R,W | R | — | R | — | R | — | R | R | R |
| **NPCBehavior** | R | R,W | R,W | R,W | R | R,W | R | R,W | — | R | — | R | R | R | R | R | R | R |
| **Settlement** | R | R | R | R | R | R | R | R | R | — | R,W | R | R | — | R | — | R | R |
| **DerivedStats** | — | — | — | — | R | — | R | — | — | R,W | — | R | — | — | — | — | W | R |
| **FactionPol** | — | — | R | — | — | — | R | R,W | R,W | R | R | — | — | R | — | — | R | R |
| **ConvTrack** | — | — | — | R | R | — | R | — | — | R | — | — | — | — | — | — | R | R |
| **CharHist** | W | W | W | W | — | — | — | W | W | — | — | W | W | — | — | — | — | — |
| **InvestSys** | — | R,W | R | — | — | — | — | R | R,W | R | — | — | — | R | — | — | — | R |
| **Companion** | R,W | R | R | R | R | R | — | R | R | — | — | — | — | — | — | — | — | R |
| **ClockReg** | R | R | R | R | R | R | R | R | R | R | R | R | R | R | — | — | — | R |
| **UI/UX** | R | R | R | R | R | R | R | R | R | R | R | R | R | R | R | R | R | — |

### Reading the Matrix

**Rows** = the system being examined. **Columns** = the system it interacts with.

**Most depended-upon systems (column density):**
- **NPC Behavior** — 14 systems read from it (everything except ClockReg, UI/UX, DerivedStats, and itself)
- **Scale Transitions** — 12 systems read from it
- **Clock Registry** — 16 systems read from it (universal reference)
- **Character Histories** — 10 systems write to it (it seeds all starting state)

**Most dependent systems (row density):**
- **NPC Behavior** — reads from 14 other systems
- **Settlement Layer** — reads from 13 other systems
- **Scale Transitions** — reads from 10 other systems
- **UI/UX** — reads from all 17 other systems (it renders everything)

**Highest bidirectional coupling:**
- NPC Behavior ↔ Fieldwork (R,W both directions)
- NPC Behavior ↔ Contest (R,W both directions)
- NPC Behavior ↔ Threadwork (R,W both directions)
- NPC Behavior ↔ Player Agency (R,W both directions)
- Settlement ↔ Derived Stats (R,W both directions)

**Isolated systems (low coupling):**
- Companion Specification — reads from many, writes to few (Combat only)
- Clock Registry — read-only reference; writes nothing back
- Conviction Track — reads Thread/Battle/Settlement; writes only to Victory (via PT)

### Dependency Risk

NPC Behavior is the system with the highest dependency fan-in AND fan-out. A bug or design error in NPC Behavior propagates to 14 other systems. This is architecturally appropriate (NPCs are the connective tissue) but means NPC Behavior requires the highest test coverage and the most conservative change management.

---
---

# ═══════════════════════════════════════════════════════
# SECTION 5: RESOLUTION ENGINE & STATISTICAL MATRIX
# ═══════════════════════════════════════════════════════

## 5.1 Core Engine

All systems share one resolution engine. Every meaningful roll in the game uses this grammar:

```
Pool: (Primary Attribute × 2) + History bonus + system-specific modifiers
TN:   7 (Standard) | 6 (Controlled) | 8 (Desperate/Binding)
Ob:   1–8 (difficulty gate)
Die:  d10, success on ≥ TN, chain on 10 (reroll, keep)
```

**Degree table (universal):**

| Net Successes vs Ob | Degree |
|---------------------|--------|
| 0 (fail to meet Ob) | Failure |
| Meets Ob, < 2×Ob or < 3 | Partial |
| Meets Ob | Success |
| ≥ 2×Ob AND ≥ 3 | Overwhelming |

---

## 5.2 Pool Construction by System

| System | Primary Attribute | Pool Formula | TN | Ob Source |
|--------|------------------|-------------|-----|-----------|
| **Combat** | Agility | (Agility × 2) + History + 3 | 7 | Opposed (net hits) |
| **Combat — Ranged** | Agility | Same | 6–8 per weapon | Opposed |
| **Fieldwork — Exploration** | Cognition/Attunement/Endurance | (Attr × 2) + History + 3 | 7 (6 Controlled, 8 Desperate) | Depth table (1–8) |
| **Fieldwork — Investigation** | Cognition/Attunement/Recall/Spirit | (Attr × 2) + History + 3 | 7 | Depth table + modifiers |
| **Fieldwork — Socializing** | Charisma/Bonds/Attunement | (Attr × 2) + History + 3 | 7 | Action-specific (1–5) |
| **Social Contest — Argue** | Cognition/Charisma/Attunement (by adjudicator) | (Attr × 2) + History + genre/audience bonus (max +2D) + Recall (+2D) | 7 | Opposed (margin vs resistance) |
| **Social Contest — Appraise** | Attunement | Attunement alone (no History) | 7 | 1 |
| **Social Contest — Initiative** | Attunement | Attunement pool | 7 | 1 (opposed) |
| **Thread — Leap** | Spirit | (Spirit × 2) + History + TPS | 7 | TS-indexed (1–2) |
| **Thread — Weaving** | Spirit | (Spirit × 2) + History + TPS | 7 | Scale table (1–5) |
| **Thread — Pulling** | Spirit | (Spirit × 2) + History + TPS | 7 | Actualization (1–5) |
| **Thread — POP** | Spirit | (Spirit × 2) + History + TPS | 8 | Recency (3–7) |
| **Thread — Lock/Dissolution** | Spirit | (Spirit × 2) + History + TPS | 8 | Three-axis (params_threadwork) |
| **Thread — Mending** | Spirit | (Spirit × 2) + History + TPS | 7 | Gap severity (2–8) |
| **Thread — Opposing** | Spirit | Same as operation | 7/8 | Base Ob + floor(opponent TPS ÷ 2) |
| **Mass Battle — Engagement** | N/A (unit-level) | min(Size, Command) + Command − Discipline penalty | 7 | Opposed (net hits + weapon mod − DR) |
| **Mass Battle — Volley** | N/A (unit-level) | Power stat | 6 | Net successes − DR = Size loss |
| **Mass Battle — Tactic** | Command | Command pool | 7 | Tactic-specific (1–4) |
| **Governance** | Cognition/Charisma/Attunement | (Attr × 2) + History | 7 | Stat-derived (1–3) |
| **Conviction check** | Spirit | Spirit pool | 7 | 1 |

---

## 5.3 Damage/Effect Formulas

| Context | Formula | Variables |
|---------|---------|-----------|
| **Personal combat damage** | net hits + STR + weapon modifier − DR | net hits = Off successes − Def successes; weapon mod per TN matrix vs armor table |
| **Personal combat critical** | net hits ≥ 3 → weapon modifier doubled | Before DR subtraction |
| **Mass battle damage** | max(0, net hits + weapon modifier − DR) | Per unit engagement; simultaneous application Phase 6 |
| **Mass battle critical** | net hits ≥ 3 → weapon modifier doubled | Same as personal |
| **Contest strain (CLASH)** | margin + Charisma modifier − Focus defence (min 0) | Cha mod: max(0, floor((Cha−3)÷2)); Foc def: floor(Foc÷2) |
| **Contest strain (REINFORCE)** | (margin − 1, min 0) + Cha mod − Foc def (min 0) | Reduced by 1 vs CLASH |
| **Contest track movement** | margin − resistance (if positive) | Resistance = avg Stability of factions, round up, −1, min 0 |
| **Wound Interval** | Endurance + 6 | Range 7–13 |
| **Max Wounds** | floor(Endurance ÷ 2) + 1 | Range 1–4 |
| **Composure** | Charisma + 6 | Range 7–13 |
| **Concentration** | Focus + Recall | Range 2–14 |
| **Health (total capacity)** | Wound Interval × (Max Wounds + 1) | Range 14–65 |
| **Stamina** | Endurance + History + 1 − armor mod | Min 2 |
| **Cover** | Cognition + most relevant History | Determines Exposure thresholds |
| **Command** | ⌈(Charisma + Cognition) ÷ 2⌉ | Range 1–7 |
| **Thread Pool Score (TPS)** | TS ÷ 10 (floor) | Range 0–10 |
| **Effective Combat Pool (mass)** | min(Size, Command) + Command | Discipline penalty subtracted |

---

## 5.4 Derived Value Formulas

| Derived Value | Formula | Seasonal Income | Stat Damage Trigger |
|--------------|---------|-----------------|---------------------|
| **Treasury** (from Wealth) | Wealth × 100 | Σ(settlement Prosperity) × 10 + Trade results + Haushalt bonus | Treasury = 0 through Accounting → Wealth −1 |
| **Legitimacy** (from Mandate) | Mandate × 20 | +5 per territory at Accord ≥ 2 + Govern results | Legitimacy = 0 → Mandate check Ob 2; fail → Mandate −1 |
| **Reputation** (from Influence) | Influence × 15 | +5 per diplomatic relationship at Disp ≥ +2 + Intel/Diplomacy results | Reputation = 0 → Diplomatic +1 Ob, Intel +1 Ob; next Accounting → Influence −1 |
| **Cohesion** (from Stability) | Stability × 10 | +10 per peaceful season + Govern +5 | Cohesion = 0 → Stability check Ob 1; fail → Stability −1 |
| **Levies Available** (from Military) | Military × 2 | N/A (ceiling, not resource) | Over ceiling → disband |
| **Local Economy** (settlement) | Prosperity × 50 | Contributes to faction Treasury | Local Economy = 0 through Accounting → Prosperity −1 |
| **Garrison Strength** (settlement) | Defense × 20 + Fort × 30 | N/A | N/A (derived indicator) |
| **Public Order** (settlement) | Order × 20 | N/A | Public Order < 0 → riot events |

---

## 5.5 Probability Reference

All rolls: Nd10, success on ≥ TN. Chain on 10 (reroll, additional success on ≥ TN).

**Expected successes per die (without chaining):**

| TN | P(success) per die | Expected net per die |
|-----|-------------------|---------------------|
| 6 | 0.50 | 0.556 (with chain) |
| 7 | 0.40 | 0.444 |
| 8 | 0.30 | 0.333 |

**P(meeting Ob) by pool size at TN 7:**

| Pool | Ob 1 | Ob 2 | Ob 3 | Ob 4 | Ob 5 |
|------|------|------|------|------|------|
| 3D | 78% | 35% | 10% | 2% | <1% |
| 5D | 92% | 63% | 32% | 12% | 4% |
| 7D | 97% | 80% | 52% | 27% | 11% |
| 9D | 99% | 90% | 69% | 43% | 22% |
| 11D | ~100% | 95% | 81% | 58% | 35% |
| 13D | ~100% | 98% | 89% | 72% | 49% |

**Key calibration points:**
- Ob 1 at 3D = 78%: basic competence succeeds ~4/5 times
- Ob 3 at 5D = 32%: difficult tasks genuinely threaten average characters
- Ob 3 at 9D = 69%: specialists handle difficult tasks ~2/3 of the time
- Ob 5 at 13D = 49%: maximum pool, maximum difficulty = coin flip

**Design implication:** The engine produces a natural difficulty curve where Ob 1–2 tasks are routine for competent characters, Ob 3 tasks are genuinely uncertain, and Ob 5+ tasks are specialist-only. This holds across combat, fieldwork, contests, and Thread operations because the pool formula and TN are shared.

---

## 5.6 Attribute Role Map

| Attribute | Primary Pool For | Secondary/Derived Use |
|-----------|-----------------|----------------------|
| **Agility** | Combat | — |
| **Endurance** | Fieldwork (terrain) | Wound Interval, Max Wounds, Stamina |
| **Strength** | — | Combat damage addition, weapon minimums |
| **Cognition** | Fieldwork (investigation), Contest (Expert Judge), Governance | Cover (with History), Command (with Charisma) |
| **Charisma** | Fieldwork (socializing), Contest (Crowd) | Composure, Contest strain modifier, Command (with Cognition) |
| **Attunement** | Fieldwork (Read, Negotiate), Contest (No Adjudicator), Appraise | Social initiative |
| **Recall** | Fieldwork (Research, Reconstruct) | Concentration (with Focus), skill gatekeeper, Recall bonus in Contest |
| **Bonds** | Fieldwork (Connect) | Disposition ceiling, Knot capacity |
| **Focus** | — | Contact Duration (Thread), Concentration (with Recall), Focus defence (Contest strain) |
| **Spirit** | All Thread operations (Leap, Weave, Pull, Lock, Dissolve, Mend) | Conviction check, wound disruption during Thread contact |

**Build archetypes from attribute investment:**
- **Warrior:** Agility + Endurance + STR → combat pool, survivability, damage
- **Investigator:** Cognition + Recall + Attunement → fieldwork pool, Cover, evidence quality
- **Diplomat:** Charisma + Attunement + Bonds → contest pool, Disposition ceiling, social actions
- **Practitioner:** Spirit + Focus + Attunement → Thread pool, Contact Duration, social perception
- **Governor:** Cognition + Charisma → Command, governance pools, Contest (Expert Judge)
- **Generalist:** Balanced → competent everywhere, exceptional nowhere

---
---

# ═══════════════════════════════════════════════════════
# CONSOLIDATED FLAGS
# ═══════════════════════════════════════════════════════

## P1 (4 flags)

| Flag | System | Issue |
|------|--------|-------|
| AUD-NPC-01 | NPC Behavior | Knot formation during play unspecified — blocks Solidarity targeting |
| AUD-SET-02 | Settlement | Accord change rules not propagated to settlement Order |
| AUD-DS-01 | Derived Stats | All numerical values PROVISIONAL — no faction economic simulation |
| AUD-FP-01 | Faction Politics | 947 lines unsimulated; 5 SIM-POL items deferred |

## P2 (13 flags)

| Flag | System | Issue |
|------|--------|-------|
| AUD-COM-01 | Combat | §4 action priority contradicts §2 simultaneous declaration |
| AUD-COM-04 | Combat | ED-129 ranged TN matrix integration pending |
| AUD-SC-02 | Social Contest | CROSS floor(÷2) may be non-viable at Resistance 2+ |
| AUD-SC-03 | Social Contest | SIM-DEBT-03/04 outstanding since PP-234 |
| AUD-TW-01 | Threadwork | §4.1/4.2 empty (Co-Movement foundation) |
| AUD-TW-02 | Threadwork | params_threadwork Ob alignment unverified |
| AUD-MB-02 | Mass Battle | Part C editorial items pending approval |
| AUD-VIC-02 | Victory | RM win probability unsimulated |
| AUD-SET-01 | Settlement | Order averaging → one revolt caps Accord |
| AUD-SET-03 | Settlement | 36-settlement economy unsimulated |
| AUD-NPC-02 | NPC Behavior | 7 NPC stat gaps (TS/Certainty) |
| AUD-NPC-03 | NPC Behavior | Priority tree cross-faction interactions unsimulated |
| AUD-UI-01/02 | UI/UX | Derived stats display + settlement map not integrated |

## P3 (10 flags)

| Flag | System | Issue |
|------|--------|-------|
| AUD-COM-02 | Combat | §9 pre-PP-232 stat names |
| AUD-COM-03 | Combat | §9 references deprecated doc |
| AUD-COM-05 | Combat | Stamina merge proposal |
| AUD-SC-01 | Social Contest | §1 Core Principle empty |
| AUD-TW-03 | Threadwork | N-Way auto-collapse — consider graduated |
| AUD-PA-02 | Player Agency | Independent path fewer opportunities |
| AUD-NPC-04 | NPC Behavior | Conviction crisis d6 — consider weighted |
| AUD-CT-01 | Conviction Track | CV→PT rename deferred |
| AUD-CH-01 | Character Histories | Coherence → Recall → skill access |
| AUD-CK-01 | Clock Registry | Settlement derived tracks not listed |

## Highest-Priority Work

**Integrated multi-system simulation across a 30-season campaign.** Individual systems are calibrated. The coupled feedback loop (derived stats → NPC behavior → Scene Slate → player actions → Domain Echo → derived stats) has never been stress-tested end-to-end. This is the single biggest remaining risk before Godot implementation.
