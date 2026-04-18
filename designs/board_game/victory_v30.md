<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: victory_v30_infill.md -->

<!-- v30 baseline — renamed from designs/board_game/victory_architecture_v1.md on 2026-04-13 -->
# VALORIA BG — Victory Architecture
## ED-306 Resolution (v3 — geography_design.md territory numbering, TC 75 canonical, PT cap clarified)
## PP-540–546 (2026-04-10): Balance patches — solo + co-victory timeline normalisation
## Date: 2026-04-06 | Status: DESIGN — pending Varfell Path B user decision (ED-311)
## Supersedes: v2 (same path), params_board_game.md §Victory Conditions, all Deed-based victory systems
## Dependencies: ED-302 (PT confirmed), ED-303 (TC freeze at 75), ED-304 (Partition Victory), ED-305 (WA=0), ED-307 (Baralta cadet branch), BALANCE-001 (equal win probability), BALANCE-004 (Askeheim purpose)
## Territory numbering: geography_design.md canonical (all T-numbers match geography_design.md)
## See also: designs/board_game/peninsular_strain_v1.md (Accord, Peninsular Strain, universal victory condition, faction acquisition toolkits)

---

## Core Frame


Two simultaneous contests: who governs the peninsula AND whether it survives. Church and Hafenmark are structurally blind to the Rendering Stability (RS) crisis. Church compensates with Graduated Seizure — available early but strongest at high TC. Crown and Varfell can address RS via Thread path but at cost of political resources.

**Equal win probability** for Crown, Varfell, Hafenmark, Church. Restoration Movement (RM) is hardest mode (Hybrid only). (BALANCE-001, revised PP-494)

---

## 0. Universal Victory Condition — Peninsular Sovereignty

**All factions share this victory condition.** Faction-specific conditions in §3 below are retained as alternate (easier) paths.

All conditions simultaneous at Accounting, held for 2 consecutive Accountings:

| Condition | Threshold |
|-----------|-----------|
| Territory control | All 15 playable territories (T1–T14, T17) — directly or via effective hegemony |
| Accord | ≥ 2 in all directly-controlled territories |
| Peninsular Strain | ≤ 6 |

**Effective hegemony** counts rival-held territories if the rival is: Treaty-bound (Crown Treaty or equivalent), Submitted (Stability 0, formal submission), or institutionally dominated (rival Mandate ≤ 1 AND hegemon Mandate ≥ 5).

**Full rules:** See designs/board_game/peninsular_strain_v1.md §6.

### 0.1 Peninsular Partition (Co-Victory, multiplayer)

All conditions simultaneous at Accounting, held for 2 consecutive Accountings:

| Condition | Threshold |
|-----------|-----------|
| Collective territory control | Both factions collectively control all 15 playable territories (directly or via hegemony) |
| Individual minimum | Each faction TCV ≥ 10 |
| Accord | ≥ 2 in all territories controlled by each faction |
| Non-aggression | No Battle between the two factions in preceding 4 seasons |
| Peninsular Strain | ≤ 6 |
| Institutional standing | Both factions Mandate ≥ 3 |

**Incompatible pairings:** Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM.

Existing co-victory pairings in §4 below are retained as alternate co-victories with their existing thresholds.

### 0.2 Accord System

Per-territory attribute (0–3). Modifies effective Prosperity. See peninsular_strain_v1.md §2 for full rules.
- Accord 3 (Aligned): full Prosperity, defender +1D.
- Accord 2 (Compliant): full Prosperity, normal.
- Accord 1 (Resistant): no Prosperity contribution, Govern Ob +1, garrison required.
- Accord 0 (Revolt): territory becomes Uncontrolled.
- **TCV counts only at Accord ≥ 2.**
- Military conquest → Accord 1. Faction-specific non-military acquisition → Accord 2+.

### 0.3 Peninsular Strain Counter

Global track (0–10). Advances from inter-faction battles, faction eliminations, revolts. See peninsular_strain_v1.md §4.

### 0.4 Battle Consequences

Each Battle on Valorian soil: RS −1 (Campaign/War scale: RS −2). Each season with inter-faction battle: IP +2, Strain +1. See peninsular_strain_v1.md §3.

### 0.5 Faction Acquisition Toolkits

| Faction | Non-Military Acquisition | Card Type | Accord on Success |
|---------|------------------------|-----------|-------------------|
| Crown | Formal Crown Treaty | Senator | 2 (diplomatic transfer) |
| Church | Graduated Seizure | Special/Unique | max(floor(PT/2)+1, 2) |
| Hafenmark | Dynastic Proclamation | Diplomat | 2 |
| Varfell | Cultural Reformation | Colonist | 2 |
| Löwenritter | Martial Governance | Legionary (Govern variant) | +1 per success (cap 2) |

Full specifications: peninsular_strain_v1.md §5.

---

## 1. Territory Consolidation Values (TCV)

All territory numbers match geography_design.md canonical table.

| T# | Territory | TCV | Controller |
|----|-----------|-----|------------|
| T1 | Valorsplatz | 5 | Crown★ |
| T9 | Himmelenger | 5 | Church★ |
| T8 | Gransol | 3 | Hafenmark★ |
| T12 | Sigurdshelm | 3 | Varfell★ |
| T3 | Lowenskyst | 2 | Crown |
| T14 | Ehrenfeld | 2 | Crown |
| T10 | Spartfell | 1 | Hafenmark |
| T7 | Rendstad | 1 | Hafenmark |
| T17 | Halvarshelm | 1 | Hafenmark |
| T2 | Kronmark | 1 | Crown |
| T5 | Feldmark | 1 | Crown |
| T6 | Stillhelm | 1 | Crown |
| T13 | Oastad | 1 | Varfell |
| T11 | Halvardshelm | 1 | Varfell |
| T4 | Grauwald | 1 | Varfell |
| T15 | Askeheim | 0 | Uncontrolled |
| T16 | Schoenland | — | Not in territorial play |
| | **Total** | **31** | |

**Starting TCV by faction:** Crown 12, Hafenmark 6, Varfell 6, Church 5.

---

## 2. Piety Track (PT)

Per-territory track. Range 0–5 per territory. 0 = Restoration pole, 5 = Piety pole.


Key rules:
- T15 (Askeheim) PT hard-fixed at 0. Cannot increase. (P-03 + Foundations §8)
- T9 (Himmelenger) starts at 5, soft cap — can drop under pressure, does not auto-recover.
- **PT action cap:** Each faction may initiate at most one deliberate PT-moving action per territory per season (±1 max). Calamity Drift, Church Seizure Overwhelming PT bonus, and Domain Echoes from Zoom In are consequences — they are not faction actions and are not cap-governed.
- Calamity Drift (RS-linked PT erosion) ignores the action cap. RS ≤ 50: T6/T13 PT −1. RS ≤ 35: territories within 2 steps of T15 PT −1. RS ≤ 20: all territories PT −1.

---

## 3. Faction Strategies — Asymmetric Approaches to Peninsular Sovereignty

**These are NOT victory conditions.** They describe each faction's unique toolkit for territorial acquisition. The ONLY faction victory is Peninsular Sovereignty (§0): control all 15 territories, Accord ≥ 2, Strain ≤ 6, held 2 consecutive Accountings. Every faction pursues the same goal through different means.


### 3.1 Crown — Peninsula Sovereignty

**All conditions simultaneous at Accounting:**

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 14 | *(PP-540: was 16)* |
| Rival suppression | At least 2 of the 3 other playable factions: Mandate ≤ 2 OR eliminated OR formal Crown Treaty in effect | *(PP-540: was all 3)* |
| IP | < 60 |
| PI | ≥ 3 |

**Formal Crown Treaty (PP-512/513/514/523):** Senator Outward, Crown only. Cannot combine with Diplomatic Outreach to Schoenland same season. Ob = ceil(target Mandate / 2), min 1. Mandate ≤ 1 target: invalid (insufficient institutional standing).

**Consent (PP-513):** Target declares consent/refusal at Phase 1 of following season. Refusal: Crown gains Casus Belli (standard, 3 seasons); no retry vs same faction for 2 seasons. NPC AI consent: Mandate ≥ 3 AND Stability ≤ 3.

**Degree effects:** Overwhelming: Treaty formed + target Mandate −1 + Stability +1 + Crown Mandate +1. Success: Treaty formed + target Mandate −1 + Stability +1. Partial: Treaty offered — target accepts (formed, no stat changes) or declines (Crown gains CB). Failure: Crown Stability −1.

**Treaty period:** 4 seasons. Either party may extend (action, no roll) or let lapse. Lapse is not betrayal. **Lapse timing (PP-528):** Treaty lapse occurs at Phase 1 of the season after the period ends. Treaty formed Season N lapses at Phase 1 of Season N+5. Accounting of Season N+4 sees the Treaty as active. Extension must be declared at Phase 1 of Season N+5. **Hybrid Diplomacy bridge (ED-370):** Personal Diplomacy success in TTRPG/Hybrid scene queues −1 Ob Domain Echo on BG Treaty roll at next Accounting. Cap: −1 Ob, once per Treaty target per arc.

**Crown-break (PP-511):** Crown Stability −2, Mandate −1 (end of Phase 4). Betrayed faction gains permanent CB. CB usable next season.

**Target-break (PP-514):** Treaty partner initiates Domain Action directly targeting Crown's held territory → Treaty dissolves immediately. Crown gains permanent CB. Partner Stability −1.

**Token interaction (PP-509):** Hafenmark Diplomatic Token on Treaty partner removed at Treaty formation.

#### Alternate — Dominion
TCV ≥ 22 AND every other playable faction eliminated (Stability 0). No treaties.

---

### 3.2 Church of Solmund — Solmundan Orthodoxy

**Graduated Seizure (PP-494):** Church may attempt Territorial Seizure at any TC value. TC determines the size of Church's Seizure pool — the higher the TC, the more institutional authority Church projects.

**Church Seizure Pool:** Influence + floor(TC / 15)
**Church Seizure Ob:** 7 − PT (where PT is the target territory's Piety value, 0 = Restoration pole, 5 = Piety pole)
**Seizure Accord:** Success → max(floor(PT/2)+1, 2). Overwhelming → floor(PT/2)+2, max 3. Partial → 1. See peninsular_strain_v1.md §5.2.

| TC | Pool Bonus | Total Pool (Inf 6) |
|----|-----------|-------------------|
| 15 | +1 | 7 |
| 30 | +2 | 8 |
| 45 | +3 | 9 |
| 60 | +4 | 10 |
| 75 | +5 | 11 |

| PT | Seizure Ob | Notes |
|----|-----------|-------|
| 5 (Piety) | 2 | Pious territory — Church authority unquestioned |
| 4 | 3 | |
| 3 | 4 | |
| 2 | 5 | Contested ground |
| 1 | 6 | Restoration-leaning — Church is an invader |
| 0 (Restoration) | 7 | Hostile population — Seizure is an act of war |

TC freezes at 75. At TC 75 (pool 11D) vs PT 5 (Ob 2): Seizure is essentially guaranteed. Against PT 0 (Ob 7): Church succeeds ~40% — formidable but not certain.

Early Seizure (TC < 50) is possible but carries political consequences: Casus Belli from the controlling faction, and every other faction sees Church territorial ambition. The lower the TC, the more it looks like institutional aggression rather than a natural extension of authority. The civil war scenario is a real cost.

**Fort interaction (PP-500, ED-355 resolved):** Fort Level does not modify Seizure Ob. Seizure is a political act — Church institutional authority overriding local governance. If the territory has a garrison (Fort ≥ 1 AND military units present), Church must win a Battle (attacker Military vs Battle Ob, modified by Fort per standard Battle rules) before Seizure can be attempted. An ungarrisoned fortified territory (Fort ≥ 1, no units) can be Seized without Battle.

**Victory conditions (all simultaneous at Accounting):**

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 8 |
| PT in all held territories | ≥ 3 |
| Accord in non-capital territories | ≥ 3 in at least 3 non-capital Church territories (not T9) |

*(ED-585/590 resolved 2026-04-16: Accord ≥ 3 condition added. TCV + PT alone was insufficient — Church met TCV ≤ Season 4 in simulation, making it no constraint on TC timing. Accord ≥ 3 requires Govern OW or Seizure OW in 3 non-capital territories, creating a sustained governance burden that competes with Assert and Seizure for Church's Consul card each season.)*

**Prominence prerequisite:** Church may only seize a territory where Church is Prominent — defined as Church Mandate exceeding the controlling faction's Mandate in that territory. Church Mandate is the Church faction's global Mandate stat. Controlling faction Mandate is their global Mandate stat. Prominence is assessed at seizure declaration.

Church Mandate ≥ 4 required to initiate any seizure. Overwhelming seizure: PT +1 in target territory (this is a consequence, not a cap-governed action).

#### Alternate — Altonian Theocracy Path
Altonian Ecclesiastical Accord (AEA) track 0–5. Victory: AEA = 5 + TC ≥ 60 + Church controls T9 (Himmelenger). Requires less territory but more diplomatic conditions.

#### Partition — Church + Hafenmark (ED-304)
**Trigger (all simultaneous at Accounting):**
- Crown Mandate ≤ 1
- TC ≥ 50
- Church controls ≥ 2 territories
- Hafenmark controls ≥ 3 territories
- No active military conflict between Church and Hafenmark

**Partition Pressure marker (ED-338, PP-566):** At Accounting, if all conditions EXCEPT TC ≥ 50 are simultaneously met, place a public Partition Pressure marker. Other factions have 1 season to disrupt conditions before TC threshold check fires. Remove marker if any condition breaks before TC ≥ 50.



---

### 3.3 Hafenmark — Dynastic Assertion (Primary)

**[Parliamentary Sovereignty STRUCK — replaced by Dynastic Assertion as primary per peninsular_strain_v1.md. Baralta's identity is divine-right claimant, not constitutional reformer.]**

**All conditions simultaneous at Accounting:**

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 13 | *(PP-541: was 12)* |
| Hafenmark Mandate | ≥ 4 |
| Hafenmark Stability | ≥ 3 | *(PP-571, ED-388: prevents Parliamentary Sovereignty while faction is destabilised)* |
| PI | ≥ 5 |
| Crown Mandate | ≤ 3 |

#### Alternate — Dynastic Assertion (ED-307)

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 12 |
| Crown Mandate | ≤ 1 |
| Control T1 (Valorsplatz) | held |
| Hafenmark Mandate | ≥ 5 |
| Torben Loyalty | ≤ 3 OR Torben removed |

---

### 3.4 Varfell — Vaynard's Three Paths

#### Path A — Intelligence Hegemony

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 10 |
| VTM | ≥ 3 |
| At least 2 rival factions' stats fully revealed | fixed count |
| Varfell controls ≥ 1 territory outside starting 4 | — |

#### Path B — Southernmost Dominion
[ED-311 RESOLVED — Option A (4 conditions + WR track), 2026-04-07]

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 8 |
| Control T4 (Grauwald) AND T13 (Oastad) | both held |
| VTM | ≥ 3 |
| Warden Recognition (WR) | ≥ 2 |

**WR track (0–4):** See params_board_game.md §Varfell Path B for full WR track rules.
**Blocked if:** WR has ever returned to 0 after first advancing past 1.

#### Path C — Thread Supremacy

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 10 |
| VTM | ≥ 4 | *(PP-542: was = 5)* |
| RS | ≥ 50 |

---

### 3.5 Restoration Movement — Cultural Revolution (5 players only, hardest mode)


**Two-phase win condition:**

#### Phase 1 — Cultural Majority (threshold to unlock Phase 2)
PT ≤ 1 in ≥ 4 of the 15 playable territories (T1–T14, T17) *(PP-543: was ≥ 8; PP-478 had ≥ 5 — PP-543 supersedes both)*. Checked at each Accounting. Once met and held, Phase 2 becomes available. If the majority drops below 8, Phase 2 is locked again until it recovers.

#### Phase 2 — Cultural Uprising of T9 Himmelenger
Available only while Phase 1 condition is met. Declared once per game at any Accounting where Phase 1 holds. RM plays their Pontifex card and rolls: **Weaver Thread pool vs Ob = TC ÷ 10 (round up, min 1, max 5).**

Prerequisites: RS ≥ 25 (substrate must be stable enough for a coherent popular movement — below 25, physical destabilisation overwhelms cultural organisation). If RS < 25, Cultural Uprising is unavailable regardless of Phase 1 status.

Modifiers:
- T9 PT ≤ 1: Ob −1 (Cathedral already culturally shifted)
- WC ≥ 2: +1D (Wardens support the Uprising)
- TC ≥ 50 at declaration: Ob +1 (Church institutional authority is strong enough to resist)
- Church Mandate ≥ 5: Ob +1 (Church actively suppresses)

| Degree | Effect |
|--------|--------|
| Overwhelming | T9 transfers to RM administration. Church Mandate −2. TC −3 (institutional rupture). T9 PT −2 (population has decisively shifted — makes PT ≤ 3 holding condition immediately achievable from a PT 5 starting position). |
| Success | T9 transfers to RM administration. Church Mandate −1. |
| Partial | T9 does not transfer. PT in T9 −1 (popular sentiment shifted). Uprising attempt used up for this arc. |
| Failure | Uprising crushed. TC +2 (Church authority strengthened by resistance). T9 PT +1. Uprising attempt used up for this arc. |

#### RM Territory Control — Cultural Displacement
**Presence markers vs Phase 1 (important distinction):** Presence markers are the *holding mechanic* for post-Uprising T9 (≥ 3 required in T9). They are NOT the Phase 1 mechanic. Phase 1 (PT ≤ 1 in ≥ 4 territories) tracks Piety Track values, not Presence marker counts. Community Organizing places Presence markers; it does not directly reduce PT. PT reduction comes from: Cultural Reformation OW (Varfell, −1 PT), successful Uprising OW (T9, −2 PT), Calamity Drift (RS ≤ 50 in low-PT territories), and natural secular drift (−1 PT per 5 seasons without Church cultivation). RM players should prioritise PT reduction for Phase 1 and Presence markers for post-Uprising T9 holding — these are parallel but distinct goals.

**Overwhelming Uprising bonus:** An Overwhelming Cultural Uprising result automatically places +2 Presence markers in T9 (population mobilisation from the Uprising itself). These markers are placed before the holding condition is checked, ensuring OW Uprising immediately provides the foundation for holding T9.

RM holds T9 through cultural presence, not military garrison. Control is maintained while:
- RM has ≥ 3 Presence markers in T9
- PT in T9 ≤ 3 *(ED-588 resolved 2026-04-16: revised from PT ≤ 1. T9 starts PT 5 under Church management; ≤ 1 was unreachable post-Uprising without 4+ seasons of RM governance. PT ≤ 3 is achievable immediately after Uprising OW: PT 5 − 2 = PT 3. RM must then prevent Church Govern actions from rebuilding PT above 3.)*

If either condition fails at Accounting, T9 reverts to the prior controller (or becomes Uncontrolled if the prior controller has been eliminated). RM cannot March, garrison, or build Fort in any territory. (PP-578)



**Win condition:** T9 under RM administration AND Phase 1 held, for 2 consecutive Accounting steps. Church cannot perform Territorial Seizure on T14 while RM holds it (the population actively resists institutional reconquest — Seizure Ob +3 vs RM-held T9).

---

### 3.6 Löwenritter — Military Regency (conditional faction, post-coup)

**[Design note: Löwenritter is a transitional faction, not a conventional winning faction. Post-coup, Löwenritter holds government until a legitimate successor is installed and their own faction takes over — that new ruler leads Crown (or whichever faction claimed the capital), not Löwenritter. Regency Establishment marks a successful handoff, not a Löwenritter victory in the traditional sense. Military Consolidation represents the edge case where no legitimate successor emerges within 8 seasons — a contested end state, not a stable governance resolution.]**

#### Primary — Regency Establishment

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 10 |
| TC | < 50 |
| IP | < 60 |
| RS | > 40 |
| PI | ≥ 4 |
| Successor confirmed | Elske confirmed OR Torben Loyalty ≥ 6 |

### Elske Loyalty Track (ED-624 — approved 2026-04-17)

| Loyalty | Status | IP effect |
|---------|--------|-----------|
| 0–1 | Hostile | IP +1/season |
| 2–3 | Hostage (start) | None |
| 4–5 | Aligned | IP −1/season |
| 6–7 | Devoted | IP −2/season; Diplomatic Exchange eligible |

**Advancement:** Senator Outward (Diplomacy Ob 2) Success +1, OW +2. Personal scene Disposition ≥ +2 (Solidarity RS) +1. Fair trade treatment of Schoenland routes: +1/year. Conviction violation: −1. War on Schoenland: −3.

**Diplomatic Exchange (Loyalty ≥ 6, IP < 60):** Senator Outward, Ob 2. Success: IP −10, threshold +5, AER +1, Elske status changes to willing resident. OW: All above + Schoenland Treaty.

**"Elske confirmed"** = Diplomatic Exchange success. Satisfies Regency Establishment condition above. *Conviction: Order. RS: Solidarity. Certainty: 4.*

#### Alternate — Military Consolidation
Only available if Regency Establishment not achieved after 8 Löwenritter seasons (track with counter on Löwenritter mat).

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 16 |
| Löwenritter Military | ≥ 5 |
| RS | > 35 |
| TC | < 60 |

---

## 4. Co-Victory Pairings


| Pair | Conditions (all simultaneous at Accounting) |
|------|---------------------------------------------|
| **Crown + Hafenmark** | Crown TCV ≥ 12 AND Hafenmark TCV ≥ 12 AND PI ≥ 7 AND TC < 50 AND Crown Mandate ≥ 4 AND Hafenmark Mandate ≥ 4 AND neither faction has played Legionary targeting the other in preceding 4 seasons | *(PP-561 + PP-572, ED-391: 4-season no-active-conflict reinforces cooperative design)* |
| **Crown + Varfell** | Crown TCV ≥ 12 AND Varfell TCV ≥ 8 AND VTM ≥ 3 AND RS ≥ 50 |
| **Varfell + RM** | VTM ≥ 3 AND WR ≥ 2 AND ≥ 3 territories PT ≤ 1 AND RS ≥ 40 AND Varfell controls T13 | *(PP-545: VTM was ≥ 4; territories was ≥ 4)* |
| **Hafenmark + RM** | Hafenmark TCV ≥ 10 AND ≥ 3 territories PT ≤ 2 AND PI ≥ 4 AND RS ≥ 40 | *(PP-546: territories was ≥ 4)* |
| **Löwenritter + Hafenmark** | Löwenritter TCV ≥ 8 AND Hafenmark TCV ≥ 8 AND PI ≥ 4 |
| **Church + Hafenmark (Partition)** | See §3.2. Crown Mandate ≤ 1, TC ≥ 50, Church ≥ 2 territories, Hafenmark ≥ 3, no active military conflict. Requires Phase 1 Declaration (see below). |

**Partition Phase 1 Declaration (ED-629):** Church+Hafenmark Partition cannot fire silently at Accounting. At Phase 1 of the season in which all Partition conditions are simultaneously met, either the Church player (or NPC Church AI) OR the Hafenmark player (or NPC Hafenmark AI) must publicly declare: "We assert Peninsular Partition this season." This declaration is visible to all players at Phase 1. Other factions then have the full Phase 4 Domain Action window to disrupt any single Partition condition: restore Crown Mandate from ≤ 1 to ≥ 2 (Crown Govern OW), initiate Battle between Church and Hafenmark (breaking non-aggression), reduce Church or Hafenmark territory count below the required minimum, or suppress TC below 50 (Hafenmark OW Suppress + Varfell VTM Discretion). If all conditions survive Phase 4 and hold at Accounting: Partition fires. **NPC AI Partition Declaration:** NPC Hafenmark and NPC Church both declare when all 5 conditions are met at Phase 1 evaluation. NPC AI never suppresses a Partition declaration.

**Incompatible:** Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM.

Co-victories are distinct from operational coalitions (PP-404/405). A faction may pursue a coalition without pursuing a co-victory.

---

## 5. World-State Transitions

**No shared loss. No fade to black.** Every crisis becomes a new chapter. The campaign continues.

| Condition | Trigger | Transition |
|-----------|---------|------------|
| Post-Calamity Era | RS = 0 at Accounting | Substrate tears. Faction acquisition suspended 3 seasons. Mending Domain Echo doubled. Dissolution/Lock +2 Ob. Recovery: MS restored to 20 within 10 seasons. |
| Occupation Era | IP ≥ 100 AND AER ≤ 1 | Altonian Governorate activates (Mandate 3, Military 5, Stability 4). All faction Domain Actions in occupied territories +2 Ob. Underground Network and Resistance Work activate. Recovery: IP reduced below 60 through sustained resistance. |

**Occupation Era — Expanded (historical_precedents_analysis §2, campaign_architecture_v1 Part 5):**

**Critical design note:** During Occupation, the game world continues ticking. RS continues to decline. Thread phenomena continue to intensify. The Southernmost calamity clock does not pause. Faction internal politics continue. The Occupation is a new constraint layered on top of existing systems, not a replacement for them. A player dealing with Occupation must simultaneously manage: Altonian resistance, internal faction politics, RS/Thread crisis, and their personal character arc. This is historically accurate — occupied nations face the full weight of their pre-existing problems plus the occupation itself.

**IP Visibility Milestones (NEW — historical_precedents_analysis §2.3):**
- **IP 60:** All factions receive Intelligence Report: "Altonian forces massing at border." Mandatory notification in Scene Slate (Priority 2). Factions currently in inter-faction conflict make Mandate check (Ob 2) to divert resources to border defense. Failure: faction is too consumed by internal politics to respond (no defensive Domain Actions targeting Altonia permitted this season).
- **IP 80:** Second Intelligence Report: "Altonian advance forces in Schoenland corridor." Mandatory Priority 1 scene: faction leaders convene emergency session. Player may attempt coalition-building via Social Contest.
- **IP 90:** Final warning: "Invasion imminent." All factions aware. Any faction still engaged in inter-faction Battle takes Cohesion −20 (population perceives leadership failure, derived_stats_v1).

**Altonian Alignment (NEW — historical_precedents_analysis §2.4):** NPC faction AI behavior — when an NPC faction reaches Mandate ≤ 2 (desperate), there is a chance it secretly contacts the Altonian Vanguard Commander, offering strategic intelligence in exchange for favorable treatment during Occupation. This is NOT a player action — it is a world event the player discovers through investigation. Effect: IP +5 immediate. Aligning faction gets −2 Ob on Domain Actions during Occupation Era (collaborator status). **Discoverable:** Niflhel intelligence or Riskbreaker investigation (Evidence Track threshold 4). Discovery produces a Revelation Event scene — the player learns that a faction they may have trusted has betrayed the peninsula. If exposed publicly: aligning faction's Accord drops to 0 in all territories, Peninsular Strain +3, all other factions gain Casus Belli. Historical precedent: Byzantine Kantakouzenos inviting Ottomans (1354), French collaboration during WWII. This generates emergent narrative — the betrayal is a story the player discovers and responds to as a character, not a button they press.

[EDITORIAL: ED-684 — IP milestones and Altonian Alignment. Source: historical_precedents_analysis.md §2.]

**RM Presence → Underground Network (NEW — historical_precedents_analysis §2.3):** When Occupation Era begins, RM Presence markers in occupied territories convert 1:1 to Underground Network points. RM's political organizing infrastructure — consensus-governance cells, mutual-aid networks, community contacts — functions as resistance infrastructure. Historical precedent: French Resistance built on pre-war communist and socialist party cell structures; Polish Solidarity's workplace networks became underground resistance during martial law. This gives RM a meaningful advantage in resistance scenarios without making Occupation trivially easy (RM caps at ~5-6 Presence per territory; Occupation likely lasts 10+ seasons).

[EDITORIAL: ED-685 — RM Underground Network conversion. Source: historical_precedents_analysis.md §2.]
| Anarchy Era | All playable factions at Stability 0 simultaneously | Parliament dissolved. Direct governance via personal Charisma. Founded Organizations claim ungoverned territories. New faction formation available (Mandate 3 + 2 territories + Founding Declaration). Recovery: two formal factions establish Parliament quorum. |

**The only true campaign terminal:** Second Calamity. Fires after 10 seasons sustained at MS ≤ 5 during Post-Calamity Era. Requires a decade of complete failure to reach.

### The Rupture Scene (ED-630)

When RS reaches 0 at Accounting, the Rupture Scene fires as a narrative transition into the Post-Calamity Era.

**Step 1 — World state narration:** The engine describes what RS 0 feels like in the territory the player currently occupies. Sensory, immediate, not abstract.

**Step 2 — The Last Declaration:**

The player states: (1) their primary Belief as currently written; (2) one specific action over the campaign that most clearly expressed that Belief; (3) whether, given everything, they would do that action again.

**Step 3 — Post-Calamity Era begins.** Faction acquisition suspended. Mending becomes the most consequential action in the game.
---

## 6. Askeheim and RS (BALANCE-004)

If no faction engages with Askeheim (T15), RS trends toward 0 and a second Calamity occurs.

**See also:** references/rs_budget.md (centralized RS drain/recovery budget), references/wc_survival_spine.md (WC as the mechanism of the survival contest).

**The Two Contests:** The campaign presents two simultaneous contests: (1) political sovereignty — which faction governs, and (2) world survival — does the world survive. WC is the mechanism of Contest 2. RS 0 = Rupture = all factions lose. See wc_survival_spine.md for the full strategic architecture, including the IP/expedition resource tension that makes the contests compete.

**Warden Cooperation track (0–3):**
- WC ≥ 1: +1D to all Thread operations peninsula-wide.
- WC ≥ 2: All RS drain from Gaps and Locks halved.
- WC ≥ 3: RS +2/season at Accounting (Edeyja active Mending). **This is the singular endgame survival path** — see rs_budget.md Scenario C.

Multiple victory conditions require RS thresholds. A faction that ignores RS risks losing to Rupture regardless of territorial control.

**Warden Recognition (WR) track (0–4) — Varfell Path B:**
- WR 0: Wardens unaware or indifferent.
- WR 1: Wardens have observed Vaynard (≥ 1 successful Expedition).
- WR 2: Wardens recognise Vaynard as steward.
- WR 3: Active cooperation (+1D Thread ops, as WC ≥ 1 equivalent).
- WR 4: Edeyja makes substantive contact.


---

## 7. TC Generation and Church Seizure

Starting TC: 28. Phase transition at TC 75 (TC freezes, Church shifts to seizure mode).

**CI=100 Mass Seizure Declaration (campaign_architecture_v1 §1.3, settlement_layer_v30 §1.5):** When CI reaches 100, every territory where at least one settlement has a Church building (Chapel or higher) becomes a simultaneous Seizure target. Individual Seizure Ob calculated per-territory based on PT and infrastructure modifiers. The Mass Seizure is a mandatory Zoom In event — the Archbishop declares, other factions get 1 season of Emergency Session to respond, then each territory resolves independently. CI=100 does NOT mean the Church wins — it means the Church makes its bid for theocracy. See campaign_architecture_v1.md §1.3 for full specification.

**Seasonal TC at Accounting:**
1. Institutional Momentum: TC +1 (passive).
2. Piety Yield: per territory where Church is Prominent (Church Mandate > controlling faction Mandate), add by PT. PT 5 = +1, PT 4 = +0.5, others = 0. Total = floor(sum).
3. Assert (optional Church action): Influence vs Ob 2. Success: TC +1. Failure: Cohesion −15 (derived_stats_v1).
4. Suppress (optional opponent action): Mandate vs Ob = floor(Church Mandate / 2) + 1. Success: negate Step 1 passive. Failure: Cohesion −15 (derived_stats_v1).
5. Hafenmark Structural Suppression: while Baralta Mandate ≥ 4, TC −1/season.

**Church Seizure (Graduated, PP-494):** Pool = Influence + floor(TC/15). Ob = 7 − PT. Prominence required. Church Mandate ≥ 4. Overwhelming seizure: PT +1 (consequence, not cap-governed). See §3.2 for full table.

---

## 8. RM Founding Mechanic (ED-620 — approved 2026-04-17)

WA-based spontaneous emergence struck (PP-478). RM emergence in Hybrid mode is exclusively via the Founding Mechanic.

**Prerequisites (all required):**
- Player PC Disposition ≥ +3 with Maret Vossen
- ≥ 2 territories have PT ≤ 2
- RS ≥ 40
- Player has completed ≥ 1 Community Organizing (Relational-scale Thread operation protecting or supporting a non-practitioner community)

**Founding Scene (mandatory Priority 0 Zoom In when prerequisites met):**
1. Player proposes: a named territory (first cell location), a Commitment, a Belief declaration.
2. Vossen evaluates via Solidarity RS. Argue roll: Attunement primary, No Adjudicator, Ob 2. Success → Founding. Partial → 1 additional Community Organizing required next season. Failure → retry after 1 season.
3. On Founding, RM is created with: Mandate 2, Influence 4, Wealth 1, Military 0, Stability 4.

**Post-Founding:** Praetor card activates (Community Projects). Mandate cap 4. PC Embedding: +1D on RM Domain Actions in Founding territory. Phase 1 objective: PT ≤ 1 in ≥ 4 territories.

*Validated Season 8 with deliberate investment (ST-34). Full arc: Founding S8 → Uprising OW S14 → Victory S15 (ST-48).*

---

## 9. Hybrid Mode Integration

### 9.1 PT State Transfer

| Transition | PT Rule |
|-----------|---------|
| BG → TTRPG (Zoom In) | PT is read-only context. GM uses PT to inform NPC attitudes and faith-related framing. |
| TTRPG → BG (Zoom Out) | PT changes from personal scenes queue as Domain Echoes. Cap: ±1 PT in one territory per Zoom In, firing at next Accounting. |
| Calamity Drift during Zoom In | Queues and fires when Accounting resumes. Cannot be skipped. |

**Variables that TRANSFER (BG → TTRPG):**

| BG Variable | TTRPG Equivalent | Transformation |
|-------------|-----------------|----------------|
| Territory PT (0–5) | Scene context (NPC attitudes, crowd faith level) | Read-only. Changes queue as Domain Echo (±1 max per Zoom In). |

**Zoom Out (TTRPG → BG):**

| TTRPG Outcome | BG State Update |
|---------------|----------------|
| Faith-affecting personal scene (sermon, debate, Community Organizing) | PT ±1 in that territory, queued to Accounting. Cap: 1 PT Domain Echo per Zoom In. |

### 9.2 Victory Condition Check — Hybrid


### 9.3 Hybrid Victory and P-32

P-32 ("Hybrid victory = BG victory PLUS personal arc resolution") is retained. A BG victory is mechanically valid. If the winning faction's PC has unresolved Beliefs or Inspirations, the victory is narratively qualified — no mechanical penalty. "Hollow Victory" in the P-32 sense is distinct from the Church + Hafenmark Partition Victory. These are different concepts.

### 9.4 Domain Echo Autonomous Resolution (ED-300)


---

## 10. Win Probability Assessment

| Faction | Start TCV | Target TCV | Gap | Key Difficulty | Est. Timeline |
|---------|-----------|------------|-----|----------------|---------------|
| Crown | 12 | 14 | +2 | Suppress 2 of 3 rivals (×2 political) | 12–16 seasons | *(PP-540)* |
| Church | 5 | 8 | +3 | Graduated Seizure from TC 30+; PT management | 14–18 seasons |
| Hafenmark | 6 | 12 | +6 | Dynastic Proclamation + Mil 3 handicap + Crown Mandate suppression | 12–16 seasons | *(PP-541)* |
| Varfell A | 6 | 10 | +4 | Geographic isolation + VTM 3 + intel reveals | 12–14 seasons |
| Varfell B | 6 | 8 | +2 | VTM 3 + Warden Recognition + T13 control | 12–16 seasons |
| Varfell C | 6 | 10 | +4 | VTM 5 (~S14+) + RS maintenance | 14–18 seasons |
| RM | — | — | — | 4 territories PT ≤ 1 (Phase 1) + Phase 2 roll | 14–18 seasons | *(PP-543)* |
| **Universal** | any | 31 (all) | varies | All 15 territories, Accord ≥ 2, Strain ≤ 6 | 20–30 seasons | Prestige win |


---

## 11. Open Editorial Items

| ED | Description | Status |
|----|-------------|--------|
| ED-311 | Varfell Path B redesign — see varfell_path_b_redesign_ed311.md | AWAITING USER DECISION |

---

## 12. Patch Register

| PP | Scope | Description |
|----|-------|-------------|
| PP-408 | TCV | Territory Consolidation Values — remapped to PP-199 numbering |
| PP-409 | Victory | Crown Peninsula Sovereignty — TCV ≥ 16 (gap restored to +6 after remapping) |
| PP-410 | Victory | Crown Dominion alternate — TCV ≥ 22 |
| PP-411 | Victory | Hafenmark Parliamentary Sovereignty — TCV ≥ 12 |
| PP-412 | Victory | Hafenmark Dynastic Assertion — T1 Valorsplatz (corrected from old T-number) |
| PP-413 | Victory | Church Altonian Theocracy — T9 Himmelenger (corrected from old T-number) |
| PP-414 | Victory | Varfell Path B provisional (ED-311 pending) |
| PP-415 | Victory | RM Cultural Revolution — RS ≥ 40 confirmed canonical |
| PP-416 | PT | PT action cap clarified — consequences not cap-governed |
| PP-417 | Church | Prominence mechanic defined (Church Mandate > controlling faction Mandate per territory) |
| PP-418 | Löwenritter | Military Consolidation — 8-season timer requires counter on Löwenritter mat |
| PP-419 | Hybrid | PT state transfer rules (replaces §9.1 directives-to-author format) |
| PP-420 | Hybrid | Victory condition check — replaces TC Win-Delay Rule |
| PP-421 | TC | TC 75 canonical freeze + seizure threshold. TC 80 in params_board_game struck. |
| PP-422 | Co-Victory | WA/WC references replaced with WR in Varfell+RM co-victory |
| PP-423 | Crown | Formal Crown Treaty mechanic |
| PP-424 | System | Deed system dissolved — all factions |
| PP-425 | WR | Warden Recognition track defined (0–4) |
| PP-493 | Territory | All T-numbers remapped to geography_design.md canonical. Old names (Arcansheld, Vargstad, Eidursjo, Nordhelm, Mittelmark) replaced. TCV total = 30. Starting TCV: Crown 12, Hafenmark 8, Varfell 6, Church 3. |
| PP-494 | Church | Graduated Seizure: Pool = Influence + floor(TC/15), Ob = 7 − PT. Replaces TC 75 hard gate. Church TCV threshold reduced to ≥ 8. BALANCE-001 revised to include Church in equal win probability. |


---

## 5. Total Domination (ED-318 RESOLVED, 2026-04-07)

Available to all playable factions as alternate victory path.

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 28 |
| All rival factions | Stability 0 (eliminated) OR Submitted |

Both conditions must hold simultaneously for 2 consecutive Accounting steps.

**Submission:** Any faction at Stability 0 that has not been eliminated may formally Submit at Accounting. Submitted faction: removed from victory competition, remains on board as NPC vassal (stats halved rounded down, no independent actions). The Total Domination faction must hold all non-Submitted, non-eliminated rivals at Stability 0 simultaneously.

---

## 6. Notes on Spoiler Dynamics (SIM-SPOILER-BG-01 + SIM-SPOILER-HY-01, 2026-04-07)

Simulation confirms that spoiler strategies are functional. Key findings:
- Church spoiling Crown: viable 5–8 season delay via Mandate maintenance + Inquisitor deployment. Crown counter: Royal Decree chain.
- Varfell spoiling Church: TC suppression via Counter-Narrative is minor (−0.135 TC/use expected); primary effect is AP pressure. Hybrid mode allows invisible spoiling via personal-scale Zoom In actions.
- Institutional Mandate trigger scope: [EDITORIAL: ED-324 — confirm trigger fires on Mandate-targeting actions only.]

## PP-478 Override — §3.5 Restoration Movement

**[PP-478 SUPERSEDES §3.5 above for mode applicability.]**

### RM Mode Applicability
- **BG-only mode:** RM solo victory and co-victories are UNAVAILABLE. RM is not a player faction.

### RM Solo Victory (Hybrid mode, post-Founding)
Phase 1: ≥ 4 territories PT ≤ 1, held 2 consecutive Accounting steps. *(PP-543: was ≥ 5)*
Phase 2: Cultural Uprising of T9 Himmelenger. RS ≥ 25 required (PP-467).
Roll: Weaver Thread pool vs Ob = TC ÷ 10. Win: T9 under RM administration + Phase 1 held × 2 Accounting steps.

### §4 Co-Victory Override (PP-478)
Varfell+RM and Hafenmark+RM co-victories: **Hybrid mode only, post-Founding.** BG-only: struck.

### §8 RM Emergence Override (PP-478)
The WA-based spontaneous RM Emergence mechanic (§8) is REPLACED by the Founding mechanic.
WA track remains (it governs Warden's Accord, not RM emergence). The triple-condition RM emergence
(WA ≤ −2 AND ≥ 3 territories PT ≤ 1 AND RS ≤ 50) is struck. RM emergence is now exclusively
via the Founding Mechanic in Hybrid mode.