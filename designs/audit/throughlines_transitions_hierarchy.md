# Valoria — Throughlines, Transitions, Echoes & Scale Hierarchy
## Comprehensive Map — 2026-04-18

---

# PART 1: THROUGHLINES

Throughlines are named cross-system integration questions that cut across multiple design docs. Two categories exist: **Numbered Throughlines (TL-1 through TL-10)** from the faction politics audit, and **Tagged Throughlines (T1 through T8)** from the settlement bridge unification and player agency system.

## A. Numbered Throughlines (from throughline_resolutions_v1)

| # | Name | Problem | Resolution | Status |
|---|------|---------|------------|--------|
| TL-1 | Caste Starting-State Onboarding | No signal for which caste × faction combinations are viable at character creation | Viability Matrix displayed at creation (player_agency §7.1) | Resolved (PP-661) |
| TL-2 | Standing 0 Initiation Duty | Duty system auto-generates duties at Standing 0, contradicting the Initiation Duty gate | Standing 0 carve-out: only Initiation Duty available until Standing 1 | Resolved (PP-661) |
| TL-3 | TC × Warden Asymmetry | Warden rank ladder not covered by TC pressure; RM-when-active has no rank ladder | Warden × TC Pressure Scale added; RM stub marked for future design | Resolved (PP-661), RM stub open |
| TL-4 | Generational × Coup × IP Convergence | Torben maturation interacts with Coup Counter, IP, and Baralta Crown Claim without defined sequencing | Three-Clock Interaction Table added to baralta_crown_claim §7 | Resolved (PP-661) |
| TL-5 | NPC Roster Capacity | ~35 load-bearing NPCs; companion app limits unverified | npc_behavior §11: 3-tier roster (Active/Tracked/Background), 30-NPC cap | Resolved (PP-661) |
| TL-6 | Hall Tier Settlement Integration | Hall Tier was flavor text with no settlement_layer mechanical hook | Institutional Facility Tiers (settlement_layer §1.4): Wing/Suite/Chamber/Billet slots per settlement type | Resolved (PP-661) |
| TL-7 | Warden × Thread Stress Test | ED-629 P0 integration: Warden Thread operations under MS pressure | Cross-reference note only; full stress test remains open | Open (P0) |
| TL-8 | ED-NEW-06 Lineage | Lineage tracking for ED numbering | Confirmed archived as ED-475 | Closed |
| TL-9 | SIM-POL Discoverability | Simulation debt items invisible outside register files | SIM-POL-R01 through R05 appended to coverage_matrix | Resolved |
| TL-10 | Register Split | faction_politics_expanded_v1 is too large (947 lines) for single-doc maintenance | Future-split marker placed in §0 | Deferred |

## B. Tagged Throughlines (T1–T8, from settlement bridge and player agency)

| Tag | Name | What It Connects | Where Implemented |
|-----|------|-----------------|-------------------|
| **T1** | Settlement-Level Thread | Thread operations producing settlement-level consequences (Order/Prosperity/Defense shifts) alongside province-level MS effects | settlement_layer §4.4. Cap: ±1 per settlement stat per season from Thread ops. Dissolution → Order −1; Mending → Order +1; Gap → Defense −1. |
| **T2** | Personal Resources / Economics | Player personal economic capacity (Resources 0–5) interacting with settlement and faction economies | player_agency §9 (Resources track), combat §13.1b (Economic Actions in Settlements: loot, equipment, military upgrades, Trade action). Resources interact with Treasury via personal purchases. |
| **T3** | Settlement POI Templates | Points of Interest assigned per settlement (not per province), with depth-gated content | settlement_layer §4.6, fieldwork §3.1. Each settlement has 2–4 POIs. 7 narrative-critical named POIs (Sealed Codex, Foundation Stones, Wound Core, etc.) in throughline_specifications §T3.3. |
| **T4** | Registrar Haelgrund | Ministry as investigative throughline — Haelgrund's arc connects archives, Thread artifacts, institutional neutrality | npc_behavior §2.14. Three arcs: Neutral / Whistleblower / Archivist. Home settlement S-013 Ehrenfeld Market. |
| **T5** | Martial Law at Settlement Level | Löwenritter governance producing settlement-level Order effects during military occupation | peninsular_strain §2.6b. Martial Law: Order +2 (immediate stability), Accord −1 per season (population resents military governance). Settlement-specific, not province-wide. |
| **T6** | *(not explicitly tagged in any doc — gap between TL-6 and T7)* | — | — |
| **T7** | Local Actors | Settlement-generated lightweight NPCs representing the population, providing social texture and investigation targets | settlement_layer §4.5. 1–2 Local Actors per settlement, generated from NPE territory ecology. Persist across seasons. Feed into fieldwork socializing and investigation. |
| **T8** | Conviction Legacy | When a PC retires/dies, one Conviction carries forward to the next character (transformed) | player_agency §10. Legacy Conviction inherits as a transformed version. Mechanical: the new character starts with one Conviction pre-authored by prior play. |

## C. Implicit Throughlines (not formally tagged but function as cross-system threads)

| Name | What It Connects | Systems Involved |
|------|-----------------|-----------------|
| **Church Creep** | Church infrastructure growth through institutional helpfulness → Theocracy Counter advancement → territorial seizure | settlement_layer §1.5–1.7 (4-axis infrastructure), conviction_track §1–2 (PT movement), victory §3.2 (Graduated Seizure), peninsular_strain §5.2 (Seizure Accord formula) |
| **Mending Stability Pressure** | MS decline from Thread operations → Calamity Drift → PT erosion → faction strategic recalculation | threadwork §5.1–5.5 (MS track), conviction_track §1.3 (Calamity Drift), mass_battle §A.14 (battle MS cost), peninsular_strain §3.1 (Substrate Fracture) |
| **Reputation Cascade** | Player combat/social actions → Combat Reputation / Renown → NPC Disposition shifts → Scene Slate generation | combat §13.2, player_agency §5.4, npc_behavior §8.11 (Outreach driven by Disposition), fieldwork §5.1 (Disposition Track) |
| **Epistemic Progression** | Character Certainty shifts from Thread exposure → NPC interactions change → new dialogue options unlock → new investigation paths open | character_histories (starting Certainty), threadwork §3.4 (Rendering Strain → Certainty forced shifts), investigation_systems (Ontological Ledger gates dialogue), npc_behavior §3.4 (Thread Event × Conviction Scar Matrix) |
| **Institutional Capture** | Player Standing progression → governance authority → settlement control → faction stat influence → victory contribution | player_agency §5.1 (Standing ladder), settlement_layer §3.2 (Governor eligibility), derived_stats §3 (settlement → faction), victory §0 (Peninsular Sovereignty) |

---

# PART 2: SCALES OF PLAY

Five nested scales, each with distinct mechanical resolution but shared engine grammar (d10 pool, TN 7, Ob-based).

## Scale Hierarchy

```
PENINSULA (global)
  └── TERRITORY / PROVINCE (15 playable)
        └── SETTLEMENT (36 total)
              └── SCENE (personal action space)
                    └── ROUND (combat/Thread operation granularity)
```

| Scale | Resolution Unit | Tracking Scope | Mechanical Layer |
|-------|----------------|----------------|------------------|
| **Peninsula** | Season / Arc | Global clocks: MS, TC, IP, PI, Peninsular Strain | Victory conditions, faction elimination, Altonian invasion |
| **Territory** | Season (Accounting) | Faction stats (1–7), derived values, Accord, PT, Fort Level, Prosperity | Domain Actions, military operations, faction priority trees |
| **Settlement** | Season (sub-Accounting) | Settlement stats (P/D/O, 0–5), settlement derived values, Governor | Governance actions, POI discovery, NPC roster, institutional facilities |
| **Scene** | Scene action (3–5/season) | Evidence Track, Disposition, Exposure, Conviction Track, Composure, Concentration | Fieldwork, social contests, combat initiation, Thread operations |
| **Round** | Round (~6–10 seconds) | Combat Pool, Wound progress, Stamina, Coherence, Contact Duration | Personal combat, Thread Leap/operations, mass battle phases |

## Thread Scale (parallel to geographic scale)

| Thread Scale | Scope | Min TS | Coherence Cost | Ob Range |
|-------------|-------|--------|----------------|----------|
| Object | One item/wound | 30+ | 0 | 1 |
| Personal | One person | 30+ | 0 | 2 |
| Relational | Small group | 50+ | −1 | 3 |
| Territorial | District/duchy | 50+ | −1 | 4 |
| Structural | Kingdom/institution | 70+ | −2 | 5+ |

## Mass Battle Scale (parallel to unit size)

| Battle Scale | 1 Size = | Thread Scale | Example |
|-------------|---------|-------------|---------|
| Skirmish | ~10 soldiers | Personal | Patrol encounter |
| Company | ~100 soldiers | Object | Guard action |
| Battle | ~500 soldiers | Territorial | Provincial battle |
| Campaign | ~1,000 soldiers | Territorial | Multi-territory operation |
| War | ~5,000 soldiers | Structural | Peninsula-wide conflict |

---

# PART 3: TRANSITION POINTS

Every named transition between scales, systems, or modes. Organized by direction.

## A. Upward Transitions (personal → faction/world)

| ID | From | To | Trigger | Mechanism | Cap |
|----|------|----|---------|-----------|-----|
| **DE-1** | Personal combat | Faction stats | Kill/defeat named faction officer | Combat Domain Echo (combat §13.1): defeat → acting faction stat +1, target Stability −1; kill → additionally Mandate −1 | 1 Echo/scene/faction (PP-329) |
| **DE-2** | Social contest | Faction stats | Decisive win (Conviction Track ≥7 or ≤3) | Debate Domain Echo (scale_transitions §5.4): Winner Mandate +1, Loser Mandate −1 | 1 Echo/scene/faction |
| **DE-3** | Fieldwork investigation | Faction stats | Evidence Track reaches threshold (Complex+ scope) | Investigation Domain Echo (fieldwork §2.5): Finding with faction-level scope → ±1 to relevant stat | 1 Echo/scene/faction |
| **DE-4** | Thread operation | Faction stats | MS change ≥1, or Conviction Scar fires, or Gap/Lock/Knot at Territorial+ | Thread Domain Echo (scale_transitions §5.6): Dissolution → Stability −1, Mending → Mandate +1, etc. | 1 Thread Echo/scene/faction |
| **DE-5** | Personal scene (any) | Territory Accord | Public governance, destabilization, negotiated transfer, or violence at territorial scale | Accord Domain Echo (scale_transitions §5.5): ±1 Accord in one territory per Zoom In | ±1 Accord/territory/Zoom In |
| **DE-6** | Thread operation | Settlement stats | Relational+ scale Thread op within a settlement | Settlement Thread Echo (settlement_layer §4.4 / T1): Dissolution → Order −1, Mending → Order +1, Gap → Defense −1 | ±1 per settlement stat/season from Thread |
| **DE-7** | Combat | Settlement stats | Public combat, combat against governor, killing resident NPC | Settlement Combat Consequences (combat §13.2b): public combat → Order −1, governor combat → Order −2 | Stacks with DE-1 |
| **DE-8** | Personal combat | Garrison Strength | Player defends settlement | Garrison Strength feedback (combat §13.2b / derived_stats §8.4): victory +10, OW victory +20 + PO +5, defeat −10 | Per-battle |
| **DE-9** | Combat kill | NPC network | Kill named NPC | Death Cascade (combat §13.3): Knot rupture, Disposition shifts, Scene Slate entries, faction Stability, Exposure | No cap — full cascade fires |
| **DE-10** | Conviction resolution | Renown | Conviction fulfilled, failed, or transformed | Renown +1 per resolution (player_agency §5.4) | |
| **DE-11** | Battle | Peninsula | Any inter-faction battle on Valorian soil | MS −1 (Campaign/War: MS −2), IP +2, Peninsular Strain +1 (mass_battle §A.14) | Per season |

## B. Downward Transitions (faction/world → personal)

| ID | From | To | Trigger | Mechanism |
|----|------|----|---------|-----------|
| **ZI-1** | BG battle | TTRPG personal combat | Player faction leader in contested territory | mass_battle §B.5: BG resolution defers to TTRPG mass battle |
| **ZI-2** | BG domain action | TTRPG scene | Zoom In trigger fires | scale_transitions §4.1: legal entry at 3 phase-lock points; scene Ob modified by BG degree |
| **ZI-3** | Faction crisis | Mandatory personal scene | Stability ≤2, leader removal, Heresy Investigation target, etc. | scale_transitions §4.3.2: 7 mandatory triggers generate Priority 0 Scene Slate entries |
| **ZI-4** | World-state shift | Optional personal scene | Clock band transition, NPC crisis, treaty change, territory control change, Warden emergency | scale_transitions §4.3.3: 5 world-state triggers generate Priority 1 Scene Slate entries |
| **ZI-5** | NPC priority tree | Scene generation | NPC Outreach/Demand conditions met | npc_behavior §8.11 → player_agency §4.2 Step 5: Scene Slate entries |
| **ZI-6** | Clock threshold | Scene Slate | MS, TC, IP cross band threshold | player_agency §4.2 Step 2b: Thread-State scenes (Priority 1–3) |
| **ZI-7** | Missed world event | Retrospective scene | Player absent from major event | scale_transitions §4.4: "Where Were You?" — free narrative moment filtered through social environment |
| **ZI-8** | Faction duty | Scene generation | Faction priority stack assigns duty | player_agency §3.2 → §4.2 Step 3: Duty-aligned scenes (Priority 2) |
| **ZI-9** | Conviction | Scene generation | Player Conviction text intersects with NPCs/locations/systems | player_agency §4.2 Step 4: Conviction-aligned scenes (Priority 3) |

## C. Lateral Transitions (system ↔ system at same scale)

| ID | From | To | Trigger | Rules Reference |
|----|------|----|---------|----------------|
| **LT-1** | Fieldwork → Combat | Exposure threshold, ambush, hostile contact | fieldwork §2.3 / scale_transitions §3.9 (F-TRANS-01): Exposure → Initiative advantage |
| **LT-2** | Fieldwork → Contest | Negotiation exceeds §5.7 boundary, investigation Finding cited | fieldwork §2.3 / scale_transitions §3.9 (F-TRANS-10/11): Evidence → +1D per Finding, max +2D |
| **LT-3** | Fieldwork → Thread | Thread-Read declared during investigation | fieldwork §2.3 / §4.5: Leap procedure, co-movement fires, +1 time unit |
| **LT-4** | Fieldwork → Mass Battle | Mass battle declared while fieldwork active | scale_transitions §3.9 (F-TRANS-06): suspends fieldwork, freezes Evidence Track |
| **LT-5** | Combat → Fieldwork (post-combat) | Combat ends | scale_transitions §3.9 (F-TRANS-09/12): 1 fieldwork scene, Exposure codified |
| **LT-6** | Combat → Fieldwork (fled) | Player fled/retreated | combat §11.5 (ED-576): no scene; site becomes POI; evidence degrades +1 Ob/season |
| **LT-7** | Contest → Fieldwork | Contest resolved | scale_transitions §3.9 (F-TRANS-05/10): Appraise → +1 Evidence Track; Disposition ±1 |
| **LT-8** | Personal combat ↔ Mass battle | General Duel | scale_transitions §3.7: 1 personal exchange per battle turn, max 5 exchanges, Command suspended |
| **LT-9** | Scene → Mass | Social/investigation win modifiers | scale_transitions §3.8: +1D Command / +1D Volley / free Reform; 1 turn duration |
| **LT-10** | Thread → Faction | Thread op targets faction-level config | scale_transitions §3.5: Thread pool used, faction Ob applied, no extra roll |

---

# PART 4: ECHO TYPES

All named echo and propagation mechanisms.

| Echo Type | Trigger | Effect | Timing | Cap | Source |
|-----------|---------|--------|--------|-----|--------|
| **Domain Echo** | Personal scene meets Sufficient Scope (§7) | ±1 or ±2 to most relevant faction stat by degree | TTRPG: immediate. Hybrid: Accounting. | 1/scene/faction (PP-329); ±2 per stat per echo | scale_transitions §5 |
| **Combat Domain Echo** | Kill/defeat named faction officer | Acting faction stat +1, target Stability −1 (kill: additionally Mandate −1) | Scene end | 1/scene/faction | combat §13.1 |
| **Debate Domain Echo** | Decisive contest win (Track ≥7 or ≤3) | Winner faction Mandate +1, Loser Mandate −1 | Scene end | Per contest | scale_transitions §5.4 |
| **Accord Domain Echo** | Personal scene in Hybrid produces governance/destabilization | ±1 Accord in one territory | Accounting Step 4c | ±1/territory/Zoom In | scale_transitions §5.5 |
| **Thread Domain Echo** | Thread event with Thread Significance | Dissolution → Stability −1, Mending → Mandate +1, Gap → Stability −1, Public op in Church territory → Church Mandate −1 | Accounting | 1 Thread Echo/scene/faction | scale_transitions §5.6 |
| **Settlement Echo** | Combat or Thread at settlement level | Order/Defense/Prosperity shifts per event tables | Immediate | ±1 per stat/season (Thread); immediate stacking (combat) | combat §13.2b, settlement_layer §4.4 |
| **Death Cascade** | Named NPC killed in combat | 5-step cascade: Knot rupture → Scene Slate entries → faction Stability → Exposure → player Conviction strain | Immediate (cascading) | No cap — full sequence fires | combat §13.3 |
| **Conviction Scar** | Contest decisive win via correct Resonant Style | Scar count +1 on target NPC → behavior/conviction changes per accumulation table | At contest resolution | 1 Scar per decisive win | npc_behavior §3.2–3.3 |
| **Thread Co-Movement** | Any Thread operation | 3-axis auto-effects: temporal (clock), epistemic (perception), actualized (d6 table) + Co-Movement card draw | During operation | Per operation | threadwork §4, Co-Movement cards §4.3 |
| **Coherence Degradation** | Thread operation at Relational+ scale, FR operations, residue use | Coherence −1 per qualifying operation → threshold effects at 7/4/2/1/0 | Per operation | Per-op cap (FR exempt PP-196) | threadwork §3.2 |
| **Calamity Drift** | MS crosses threshold (≤50, ≤35, ≤20) | PT −1 in affected territories at Accounting | Accounting | Ignores ±1/season PT cap; stacks with Thread Op CV Drift | conviction_track §1.3 |
| **Thread Operation CV Drift** | Public Thread event witnessed by non-practitioners | CV/PT shift per event type (Dissolution −1, Rendering Crisis +1, etc.) | Accounting | Cap ±2/territory/season from Thread sources (Calamity + Op combined) | conviction_track §1.3b |
| **Morale Cascade** | Unit routs in mass battle | Adjacent units Discipline check Ob 1; failure → Morale −1; compounds per simultaneous rout | Cascade Phase | Secondary loss cannot cause further rout until next turn | mass_battle §A.12 |
| **Knot Strain Propagation** | NPC arc involves TS threshold crossing or epistemic seduction | Knotted partners receive strain per TS band (TS 30–49: +1/season close, TS 70+: +3/season close, +2/season distant) | Per season | Per NPC per Knot | npc_behavior §5.0b |
| **Obligation** | Decisive contest win in Formal/Grand Contest | Binding commitment on loser lasting 2–4 seasons; violation → Mandate −1/−2, Stability −1 | At contest resolution | GM advisory cap: 3 active simultaneously | social_contest §6.1 |
| **Framework Drift** | Faction ethical framework produces passive stat changes | Per-framework table: Church → TC +1/season, Crown → Certainty +1/year, Hafenmark → Influence +1/season (conditional) | Per season/year | Stat ceiling 7, floor 1 | npc_behavior §7.1 |

---

# PART 5: SUFFICIENT SCOPE CONDITIONS

A personal scene qualifies for Domain Echo when it involves ANY of these (scale_transitions §7):

1. A named faction leader or their designated representative
2. A direct challenge to a faction's institutional authority
3. A completed Complex/Structural investigation (Evidence Track ≥5) concerning a faction's institutional acts
4. A Thread operation targeting a faction-level configuration (Relational+ scale)
5. Combat victory against a named NPC who holds faction office
6. Reaching Disposition +4 (Devoted) or +5 (Bonded) with a named NPC holding faction office
7. Settlement governance action that changes Order by ±1 or more

**Companion modifier:** +1 to net successes for Sufficient Scope evaluation when companion present.

---

# PART 6: MODE TRANSITIONS

Three playable modes with defined transition procedures.

```
     TTRPG ←──────────────────→ HYBRID ←──────────────────→ BG
  (scene-by-scene)          (BG + Zoom In/Out)         (turn-based)
       │                         │                          │
       │    §6.1 Session      §6.2 Mid-Game             §6.1 Session
       │    Boundary            Zoom In                   Boundary
       │         │                │                          │
       └─────────┘                └──────────────────────────┘
```

| Transition | Trigger | State Transfer | Reference |
|-----------|---------|----------------|-----------|
| TTRPG → BG | Session boundary | Domain Echoes queue; clocks batch to Accounting | scale_transitions §6.1 |
| BG → Hybrid | Zoom In trigger fires | Character sheet reactivates; scene Ob modified by BG degree (Failure +1, Success −1, OW −2) | scale_transitions §6.2, §4.1 |
| Hybrid → TTRPG | Zoom Out | Personal outcomes → Domain Echo; Phase 6 continues with updated state | scale_transitions §6.3, §4.2 |
| Coherence initialization | First Hybrid activation | Coherence = 10; subsequent = carry forward | scale_transitions §6.4 |

**Zoom In legal entry points (PP-103):** After Phase 1, After Phase 3, After Phase 6 Step 1. Mid-phase triggers defer to next legal point.

---

# PART 7: PROPAGATION PATHWAYS

Complete map of how a single player action propagates through the system hierarchy.

## Example: Player kills a Church Cardinal in combat

```
ROUND SCALE
  Player Strike → net hits → damage → Cardinal Wounds → Incapacitation → Stage 2 (Death)
    │
SCENE SCALE
  ├── Death Cascade fires (combat §13.3):
  │     ├── Step 1: Knot rupture — all Knotted NPCs: Disposition −3, Conviction Scar if central
  │     ├── Step 2: Scene Slate — all NPCs Disposition ≥+2: Priority 1 entries next season
  │     ├── Step 3: Faction — Church Stability trigger (npc_behavior §5.2)
  │     ├── Step 4: Exposure — public +3, +2 per territory where Cardinal had Disposition ≥+2
  │     └── Step 5: Player Conviction test (if Cardinal was relevant to active Conviction)
  │
  ├── Combat Domain Echo (combat §13.1):
  │     └── Acting faction stat +1, Church Stability −1, Church Mandate −1 (officer killed)
  │
  ├── Combat Reputation +1 (named NPC kill) + +1 (public victory) = +2 (combat §13.2)
  │
  └── Settlement Echo (combat §13.2b):
        └── Order −2 (combat against governor equivalent), all Dispositions in settlement −2
    │
SETTLEMENT SCALE
  ├── Order change → Province Accord recalculation (floor of mean settlement Order)
  └── Garrison Strength modifier if settlement defense relevant
    │
TERRITORY SCALE
  ├── Accord change propagates: if Accord drops below threshold → victory condition affected
  ├── Church Stability −1 may trigger priority tree shift → Constrained sub-arc if Mandate <3
  └── Church Cardinal vacancy → Succession per arc profiles
    │
PENINSULA SCALE
  ├── If Church Stability ≤2: Church enters crisis → Zoom In trigger (mandatory)
  ├── Church priority tree modified: remaining Cardinals' behavior shifts
  ├── Coup Counter evaluation (if Crown stability perceived as weak)
  └── TC generation may slow (Cardinal-driven TC actions suspended)
```

## Example: Player Mends a Gap in Stillhelm (T6)

```
ROUND SCALE
  Leap → Spirit pool → Mending roll vs Ob (Gap severity) → Success
    │
  Co-Movement fires: draw 1 card (2 if Thread Witness Node)
    │
  Coherence −1 (Mending base cost)
    │
SCENE SCALE
  ├── MS +1 (Mending Success, threadwork §2.4)
  ├── Evidence Track: +1 if investigation-relevant (fieldwork §2.4)
  └── Epistemic auto-effect: observers perceive settling; social Ob normalized
    │
SETTLEMENT SCALE (T1 — settlement_layer §4.4)
  └── Mending → Order +1 in Stillhelm
    │
TERRITORY SCALE
  ├── Thread Domain Echo: Mending at Territorial+ → controlling faction Mandate +1
  │   (scale_transitions §5.6)
  ├── Settlement Order +1 → Province Accord recalculation
  └── Co-Movement card effect applies (MS ±N per card)
    │
PENINSULA SCALE
  ├── MS +1 may shift MS band → Calamity Drift threshold changes at next Accounting
  ├── If MS crosses 40/60/80 band: Thread Revelation Curve triggers (threadwork §5.6)
  └── If MS recovers above threshold: PT erosion from Calamity Drift ceases
```

---

# PART 8: COMPLETE HIERARCHY MAP

## Tracked State by Scale

### Peninsula (Global)
| Track | Range | Mechanical Role |
|-------|-------|----------------|
| Mending Stability (MS) | 0–100 | Thread world-health; drives Calamity Drift, Revelation Curve, faction strategy |
| Theocracy Counter (TC) | 0–100 | Church institutional authority; drives Seizure capability |
| Invasion Pressure (IP) | 0–100 | External threat; drives Altonian Vanguard emergence |
| Parliament Integrity (PI) | 0–20 | Hafenmark institutional strength |
| Peninsular Strain | 0–10 | Aggregate inter-faction damage; victory condition gate |

### Territory (15 playable)
| Track | Range | Mechanical Role |
|-------|-------|----------------|
| Faction Stats (×5) | 1–7 | Dice pools for Domain Actions |
| Derived Values (×5) | 0–max | Granular resource state (Treasury, Legitimacy, Reputation, Cohesion, Levies) |
| Accord | 0–3 | Population alignment with controlling faction; derived from settlement Order |
| Piety Track (PT) | 0–5 | Church vs Restoration axis; drives Seizure Ob and Calamity Drift |
| Fort Level | 0–4 | Military defensibility |
| Prosperity | 1–7 | Economic output (contributes to Treasury income) |
| Church Attention Pool | 0–10 | Inquisitor deployment; Thread surveillance |

### Settlement (36)
| Track | Range | Mechanical Role |
|-------|-------|----------------|
| Prosperity | 0–5 | Local Economy derived value → faction Treasury |
| Defense | 0–5 | Garrison Strength derived value → military targeting |
| Order | 0–5 | Public Order derived value → province Accord derivation |
| Institutional Facility Slots | by type | Wing/Suite/Chamber/Billet availability → rank advancement gate |
| Church Infrastructure | 4 axes | Religious Building / Templar / Inquisitor / Governor → TC, PT, Seizure Ob |
| Governor | NPC/player | Governance actions, local NPC relationships |

### Scene (Personal)
| Track | Range | Mechanical Role |
|-------|-------|----------------|
| Evidence Track | 0–threshold | Investigation progress per active question |
| Disposition | −3 to +5 | Per-NPC relationship state → information gates, companion eligibility |
| Exposure | 0–10+ | Detection risk per territory per season |
| Conviction Track | 0–10 | Contest progress → Decisive/Compromise |
| Composure | 7–13 | Social damage buffer → Rattled threshold |
| Concentration | 2–14 | Contest endurance → Spent state |
| Momentum | 0–4 | Bonus successes / Stunt invocation |

### Round (Combat/Thread)
| Track | Range | Mechanical Role |
|-------|-------|----------------|
| Combat Pool | min 5 | Per-round dice available for offense/defense split |
| Wound Progress | 0–Wound Interval | Damage within current wound threshold |
| Wounds | 0–max | −1D per wound cumulative |
| Stamina | min 2 | Fatigue; 0 → Out of Breath (−2D) |
| Coherence | 0–10 | Thread practitioner rendering stability |
| Contact Duration | 0–Focus+1 | Rounds available for Thread operations per Leap |

---

# PART 9: GAPS AND MISSING CONNECTIONS

| Gap | Description | Priority |
|-----|-------------|----------|
| **T6 tag unassigned** | Throughline tags jump from T5 (Martial Law) to T7 (Local Actors). No T6 designation exists. May be an oversight or may correspond to TL-6 (Hall Tier) — but TL-6 and T6 are different numbering schemes. | P3 |
| **Knot formation during play** | AUD-NPC-01: the entire Solidarity Resonant Style pathway depends on Knots, but Knot formation after character creation has no mechanical procedure. Knots are acquired through lifepath or "GM-granted" — the latter doesn't exist in a videogame. | P1 |
| **Accord propagation** | AUD-SET-02: all existing docs that reference "Accord ±N" haven't been updated to route through settlement Order changes. The settlement layer changed the Accord derivation but downstream consumers still use the old direct-modification model. | P1 |
| **Co-Movement card deck management** | ED-577-02: reshuffle timing unspecified. This affects card-counting strategy and long-campaign MS variance. | P2 |
| **Settlement → Derived Stats display** | AUD-UI-01/02: the UI spec doesn't integrate derived stats or settlement map view. | P2 |
| **Independent player throughline** | The independent path (player_agency §5.3) generates fewer Scene Slate entries, has no Duty-aligned scenes, and reaches Renown 7+ as its faction-equivalent authority. The full throughline from independent character to peninsula-scale influence hasn't been mapped end-to-end. | P3 |
| **Generational transition throughline** | When a PC dies/retires and a new character enters (Conviction Legacy T8), the transition's effect on all tracked state (Disposition with NPCs, Standing, Exposure, Evidence Tracks, Knots) is only partially specified. Evidence Tracks persist (fieldwork §4.1). Disposition resets (new character). Standing resets to 0. Knots break. Coherence resets. But some of these aren't explicitly stated. | P2 |
