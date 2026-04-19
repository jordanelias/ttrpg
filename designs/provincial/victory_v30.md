<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: victory_v30_infill.md -->

<!-- v30 baseline — renamed from designs/board_game/victory_architecture_v1.md on 2026-04-13 -->
# VALORIA BG — Victory Architecture
## ED-306 Resolution (v3 — geography_design.md territory numbering, CI 100 canonical, PT cap clarified)
## PP-540–546 (2026-04-10): Balance patches — solo + co-victory timeline normalisation
## Date: 2026-04-06 | Status: DESIGN — pending Varfell Path B user decision (ED-311)
## Supersedes: v2 (same path), params_board_game.md §Victory Conditions, all Deed-based victory systems
## Dependencies: ED-302 (PT confirmed), ED-303 (CI cap at 100), ED-304 (Partition Victory), ED-305 (WA=0), ED-307 (Baralta cadet branch), BALANCE-001 (equal win probability), BALANCE-004 (Askeheim purpose)
## Territory numbering: geography_design.md canonical (all T-numbers match geography_design.md)
## See also: designs/board_game/peninsular_strain_v1.md (Accord, Peninsular Strain, universal victory condition, faction acquisition toolkits)

---

## Core Frame


Two simultaneous contests: who governs the peninsula AND whether it survives. Church and Hafenmark are structurally blind to the Rendering Stability (RS) crisis. Church compensates with Mass Seizure — a one-shot bid available at CI ≥ 60, strongest at CI 100. Crown and Varfell can address RS via Thread path but at cost of political resources.

**Equal win probability** for Crown, Varfell, Hafenmark, Church. Restoration Movement (RM) is hardest mode (Hybrid only). (BALANCE-001, revised PP-494)

---

## 0. Universal Victory Condition — Peninsular Sovereignty

**All factions share this victory condition.** Faction-specific entries in §3 below describe each faction's asymmetric approach to achieving this goal — their toolkit, not an alternate endpoint.

All conditions simultaneous at Accounting, held for 2 consecutive Accountings:

| Condition | Threshold |
|-----------|-----------|
| Territory control | All 15 playable territories (T1–T14, T17) — directly or via effective hegemony |
| Accord | ≥ 2 in all directly-controlled territories |
| Peninsular Strain | ≤ 6 |

**Effective hegemony** counts rival-held territories if the rival is: Treaty-bound (Crown Treaty or equivalent), Submitted (Stability 0, formal submission), or institutionally dominated (rival Mandate ≤ 1 AND hegemon Mandate ≥ 5).

**Full rules:** See designs/board_game/peninsular_strain_v1.md §6.

### 0.1 Peninsular Partition (Co-Victory — Alliance-Stalemate Negotiation)

When exactly two factions remain AND those factions have a formal alliance or treaty on record (Formal Crown Treaty, Partition Agreement, or any Diplomatic Card that established mutual non-aggression) AND the stalemate conditions below are met — the game surfaces a negotiation prompt.

**Stalemate conditions** (all simultaneous at Accounting, held 2 consecutive Accountings):

| Condition | Threshold |
|-----------|-----------|
| Collective territory control | Both factions collectively control all 15 playable territories (directly or via hegemony) |
| Individual minimum | Each faction PV ≥ 10 |
| Accord | ≥ 2 in all territories controlled by each faction |
| Non-aggression | No Battle between the two factions in preceding 4 seasons |
| Peninsular Strain | ≤ 6 |
| Institutional standing | Both factions Mandate ≥ 3 |

**The prompt:** "[NPC Faction] honors the alliance. The peninsula rests between you. End here, as partners, or pursue everything alone?"

**Accept:** Campaign concludes. Portrait fires. The partition is the ending — two factions who fought together chose not to fight each other. The game recognizes this as an honorable conclusion.

**Reject:** NPC faction Disposition drops significantly (likely Hostile). Alliance dissolved. Player must fight former ally for remaining territories. This path can produce the game's most emotionally complex ending: victory by betrayal.

**No formal alliance or treaty between the last two factions:** No prompt fires. They fight to completion.

**Incompatible pairings:** Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM.

### 0.2 Accord System

Per-territory attribute (0–3). Modifies effective Prosperity. See peninsular_strain_v1.md §2 for full rules.
- Accord 3 (Aligned): full Prosperity, defender +1D.
- Accord 2 (Compliant): full Prosperity, normal.
- Accord 1 (Resistant): no Prosperity contribution, Govern Ob +1, garrison required.
- Accord 0 (Revolt): territory becomes Uncontrolled.
- **PV counts only at Accord ≥ 2.**
- Military conquest → Accord 1. Faction-specific non-military acquisition → Accord 2+.

### 0.3 Peninsular Strain Counter

Global track (0–10). Advances from inter-faction battles, faction eliminations, revolts. See peninsular_strain_v1.md §4.

### 0.4 Battle Consequences

Each Battle on Valorian soil: RS −1 (Campaign/War scale: RS −2). Each season with inter-faction battle: IP +2, Strain +1. See peninsular_strain_v1.md §3.

### 0.5 Faction Acquisition Toolkits

| Faction | Non-Military Acquisition | Card Type | Accord on Success |
|---------|------------------------|-----------|-------------------|
| Crown | Formal Crown Treaty | Senator | 2 (diplomatic transfer) |
| Church | Mass Seizure (one-shot) | Special/Unique | max(floor(PT/2)+1, 2) |
| Hafenmark | Dynastic Proclamation | Diplomat | 2 |
| Varfell | Cultural Reformation | Colonist | 2 |
| Löwenritter | Martial Governance | Legionary (Govern variant) | +1 per success (cap 2) |

Full specifications: peninsular_strain_v1.md §5.

---


### 0.4 Starting Piety Track Values by Territory (ED-677, PP-652)

| T# | Territory | Starting PT | Rationale |
|----|-----------|-------------|-----------|
| T1 | Valorsplatz | 3 | Capital — moderate Church presence, Crown-dominated |
| T2 | Falkenberg | 3 | Standard |
| T3 | Steinfeld | 3 | Standard |
| T4 | Mittelmark | 2 | Varfell-adjacent; lower Church integration |
| T5 | Weissburg | 3 | Standard |
| T6 | Sonnental | 1 | Remote southern; minimal Church infrastructure |
| T7 | Grauheim | 3 | Standard |
| T8 | Gransol | 3 | Hafenmark capital; Church present but constitutionally constrained |
| T9 | Himmelenger | 5 | Church capital; maximum theological saturation |
| T10 | Nordmark | 3 | Standard |
| T11 | Eisengrund | 2 | Varfell-adjacent; traditional religion blends with doctrine |
| T12 | Sigurdshelm | 2 | Varfell capital; oral tradition dominant, Church institutional presence weaker |
| T13 | Southernmost | 1 | Warden territory; Thread-adjacent; Church has minimal reach |
| T14 | Hafenfeld | 3 | Standard |
| T15 | Kronheim | 3 | Standard |
| T16 | Bergstadt | 3 | Standard |
| T17 | Drakensholm | 3 | Standard |

**Design note:** PT 5 at T9 means the Church starts with its theological heartland at full doctrinal saturation — CI generation from T9 is guaranteed from Season 1. PT 1 at T6/T13 represents frontier territories where the Church must invest to gain traction. PT 2 at Varfell territories reflects cultural resistance to institutional theology. These values are calibrated against the CI generation formula (params_board_game) where PT ≥ 3 contributes positively to CI.


## 1. Provincial Value (PV)

All territory numbers match geography_design.md canonical table.

| T# | Territory | PV | Controller |
|----|-----------|-----|------------|
| T1 | Valorsplatz | 5 | Crown★ |
| T9 | Himmelenger | 5 | Church★ |
| T8 | Gransol | 4 | Hafenmark★ |
| T12 | Sigurdshelm | 4 | Varfell★ |
| T3 | Lowenskyst | 3 | Crown |
| T14 | Ehrenfeld | 3 | Crown |
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
| | **Total** | **33** | |

**Starting PV by faction:** Crown 14, Hafenmark 7, Varfell 7, Church 5.

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

**These are NOT victory conditions.** They describe each faction's asymmetric approach to territorial acquisition — the toolkit, not the endpoint. The ONLY victory is Peninsular Sovereignty (§0): control all 15 territories, Accord ≥ 2, Strain ≤ 6, held 2 consecutive Accountings. Every faction pursues the same goal through different means. The conditions listed under each faction below describe strategic thresholds that indicate when a faction's approach is working — NOT alternate endpoints.

**Emergent player-founded factions:** The settlement layer's Faction Emergence pathway (Local Actor → Regional Power → National Actor) means a player can build their own faction from nothing. Founded Organization at Mandate 3, controlling 2+ territories with Accord ≥ 2, declares itself a formal faction. That faction then pursues peninsular sovereignty like any other.


### 3.1 Crown — Peninsula Sovereignty

**All conditions simultaneous at Accounting:**

| Condition | Threshold |
|-----------|-----------|
| PV held | ≥ 14 | *(PP-540: was 16)* |
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

#### Strategic Milestone — Dominion
PV ≥ 22 AND every other playable faction eliminated (Stability 0). No treaties. This is not a separate victory — it indicates the Crown has achieved total military dominance and need only maintain Accord ≥ 2 across all territories to satisfy Peninsular Sovereignty (§0).

---

### 3.2 Church of Solmund — Solmundan Orthodoxy

**Church Seizure (one-time event):** The Church may declare a Mass Seizure when CI ≥ 60. This is a one-shot bid — the Church gets exactly one attempt. CI determines the Seizure pool; the higher the CI, the stronger the bid.

**Declaration is not automatic.** Mass Seizure is functionally a declaration of civil war against the Crown and secular factions. Even when mechanically available (CI ≥ 60), the Church institutional apparatus resists pulling the trigger. Probability of declaration per season scales with CI:

| CI | P(declare this season) |
|----|------------------------|
| < 60 | 0% (unavailable) |
| 60 | 5% |
| 70 | 29% |
| 80 | 52% |
| 90 | 76% |
| 100 | 100% (forced) |

**Formula:** P(declare) = max(0, min(1.0, (CI − 58) / 42)). Applied at Accounting. On success, Mass Seizure fires immediately. On failure, Church passes the season — another roll next Accounting. Player Church may override (declare voluntarily at any CI ≥ 60) or defer (suppress declaration even at CI 100 for 1 season only, then forced).

**Church Seizure Pool:** Influence + floor(CI / 15)
**Church Seizure Ob:** 10 − PT − infrastructure modifiers (floor 1). PT = target territory Piety value (0 = Restoration pole, 5 = Piety pole). Infrastructure modifiers per settlement (see below).
**Seizure Accord:** Success → max(floor(PT/2)+1, 2). Overwhelming → floor(PT/2)+2, max 3. Partial → 1. See peninsular_strain_v1.md §5.2.

| CI | Pool Bonus | Total Pool (Inf 6) |
|----|-----------|-------------------|
| 60 | +4 | 10 |
| 75 | +5 | 11 |
| 90 | +6 | 12 |
| 100 | +6 | 12 |

| PT | Base Ob (no infra) | Notes |
|----|-----------|-------|
| 5 (Piety) | 5 | Pious territory — Church has deep roots |
| 4 | 6 | |
| 3 | 7 | |
| 2 | 8 | Contested ground |
| 1 | 9 | Restoration-leaning — Church is an invader |
| 0 (Restoration) | 10 | Hostile population — Seizure is an act of war |

CI caps at 100. At CI 100 (pool 12D) vs PT 5 with Cathedral+Templar+Governor (Ob 5−5=1→floor 1): guaranteed. Against PT 0 with no infrastructure (Ob 10): Church needs extraordinary rolls. The one-shot nature means timing is everything — declare too early and waste the bid, wait too long and opponents prepare.

**This is a one-time event.** If the Church declares Mass Seizure and fails to achieve Peninsular Sovereignty within the resulting Theocratic Bid phase, the Church does not get a second attempt. The institutional authority spent in the declaration cannot be reconstituted. CI continues to accumulate but no further Mass Seizure is possible.

**Fort interaction (PP-500, ED-355 resolved):** Fort Level does not modify Seizure Ob directly — it is already captured in the infrastructure modifier system. If the territory has a garrison (Fort ≥ 1 AND military units present), Church must win a Battle (attacker Military vs Battle Ob, modified by Fort per standard Battle rules) before Seizure can be attempted. An ungarrisoned fortified territory (Fort ≥ 1, no units) can be Seized without Battle.

**Strategic milestones (indicators that the Church approach is working — NOT alternate endpoints):**

| Milestone | Threshold | Significance |
|-----------|-----------|--------------|
| PV held | ≥ 8 | Church has established territorial base through Seizure |
| PT in all held territories | ≥ 3 | Church governance has cultivated piety |
| Accord in non-capital territories | ≥ 3 in at least 3 non-capital Church territories (not T9) | Church governs well, not merely occupies |

*(ED-585/590 resolved 2026-04-16: Accord ≥ 3 condition added. PV + PT alone was insufficient — Church met PV ≤ Season 4 in simulation, making it no constraint on CI timing. Accord ≥ 3 requires Govern OW or Seizure OW in 3 non-capital territories, creating a sustained governance burden that competes with Assert and Seizure for Church's Consul card each season.)*

**Prominence prerequisite:** Church may only seize a territory where Church is Prominent — defined as Church Mandate exceeding the controlling faction's Mandate in that territory. Church Mandate is the Church faction's global Mandate stat. Controlling faction Mandate is their global Mandate stat. Prominence is assessed at seizure declaration.

Church Mandate ≥ 4 required to initiate any seizure. Overwhelming seizure: PT +1 in target territory (this is a consequence, not a cap-governed action).


**Prominence Self-Control Rule (PP-534):** The Church is automatically Prominent in all territories it controls, regardless of Mandate comparison. The Mandate comparison mechanic (Church Mandate > controlling faction's Mandate → Church is Prominent in that territory) applies only to territories controlled by rival factions. This prevents the absurdity of the Church failing its own Prominence check in territories it already governs.

#### CI=100 — Mass Seizure Declaration

When CI reaches 100, the Church's one-shot Mass Seizure (see above) fires at maximum strength. Every territory with a Church building (Chapel or higher) in at least one settlement becomes a simultaneous Seizure target. If the Church has not yet declared Seizure (CI ≥ 60 threshold), CI=100 is the optimal moment. If the Church already declared and spent its one-shot at CI 60–99, CI=100 has no additional Seizure effect.

**Settlement Church Infrastructure (4-axis model — see settlement_layer_v30.md §Church Infrastructure):**

Settlements track Church presence on four independent axes:
- **Religious Building** (mutually exclusive): None / Chapel (+0.5 PT) / Church (+1 PT) / Cathedral (+2 PT, +0.5 PT adjacent)
- **Templar Station** (binary): +1 CI/season, interrupt rival Domain Actions (+1 Ob, costs 1 CI)
- **Inquisitor Base** (binary): Surveillance Zone, suppresses RM organizing (+1 Ob)
- **Church Governor** (binary): de facto Church territory, bypasses civilian governance

**Per-settlement Seizure Ob modifiers (stacking, subtracted from base 10 − PT):**

| Axis | Modifier |
|------|----------|
| Chapel | −0 |
| Church | −1 |
| Cathedral | −2 |
| Templar Station | −1 |
| Inquisitor Base | −1 |
| Church Governor | −2 |

Maximum per settlement: −4 (cap per settlement_layer_v30.md §1.5). Territory Seizure Ob aggregates modifiers across all settlements in the territory. Ob floor: 1.

**Mass Seizure Mechanics:**

1. **Mass Seizure Declaration fires as a Zoom In event.** The Archbishop formally declares. Every faction receives an Emergency Session — 1 season to respond before seizures resolve.
2. **Seizure targets all territories with Church building (Chapel+).** Individual Seizure Ob = 10 − PT − (sum of infrastructure modifiers), floor 1.
3. **Succeeded seizures still require Accord ≥ 2.** Mass-seized territories start at Accord 1 (military-equivalent) or Accord 2 (if PT ≥ 3). The Church must govern what it seized.
4. **Failed seizures generate 2 Church Attention events** the following season.
5. **The game does not end at Mass Seizure.** It enters the Theocratic Bid phase — a high-stakes sequence where the Church consolidates while every other faction responds. If the Church achieves all 15 territories with Accord ≥ 2, it wins via Peninsular Sovereignty (§0). If it overextends, governance crisis.
6. **No second attempt.** The Mass Seizure is the Church's one shot. If the bid fails, the Church must pursue Peninsular Sovereignty through conventional territorial acquisition (Govern, military, diplomacy) like any other faction.

#### Strategic Milestone — Altonian Theocracy Path
Altonian Ecclesiastical Accord (AEA) track 0–5. Milestone: AEA = 5 + CI ≥ 60 + Church controls T9 (Himmelenger). Indicates diplomatic route to Church dominance is viable — still requires full peninsular sovereignty to win.

#### Partition — Church + Hafenmark (ED-304)
**Trigger (all simultaneous at Accounting):**
- Crown Mandate ≤ 1
- CI ≥ 50
- Church controls ≥ 2 territories
- Hafenmark controls ≥ 3 territories
- No active military conflict between Church and Hafenmark

**Partition Pressure marker (ED-338, PP-566):** At Accounting, if all conditions EXCEPT CI ≥ 50 are simultaneously met, place a public Partition Pressure marker. Other factions have 1 season to disrupt conditions before CI threshold check fires. Remove marker if any condition breaks before CI ≥ 50.



---

### 3.3 Hafenmark — Dynastic Assertion (Primary)

**[Parliamentary Sovereignty STRUCK — replaced by Dynastic Assertion as primary per peninsular_strain_v1.md. Baralta's identity is divine-right claimant, not constitutional reformer.]**

**All conditions simultaneous at Accounting:**

| Condition | Threshold |
|-----------|-----------|
| PV held | ≥ 13 | *(PP-541: was 12)* |
| Hafenmark Mandate | ≥ 4 |
| Hafenmark Stability | ≥ 3 | *(PP-571, ED-388: prevents Parliamentary Sovereignty while faction is destabilised)* |
| PI | ≥ 5 |
| Crown Mandate | ≤ 3 |

#### Alternate — Dynastic Assertion (ED-307)

| Condition | Threshold |
|-----------|-----------|
| PV held | ≥ 12 |
| Crown Mandate | ≤ 1 |
| Control T1 (Valorsplatz) | held |
| Hafenmark Mandate | ≥ 5 |
| Torben Loyalty | ≤ 3 OR Torben removed |

---

### 3.4 Varfell — Vaynard's Three Paths

#### Path A — Intelligence Hegemony

| Condition | Threshold |
|-----------|-----------|
| PV held | ≥ 10 |
| VTM | ≥ 3 |
| At least 2 rival factions' stats fully revealed | fixed count |
| Varfell controls ≥ 1 territory outside starting 4 | — |

#### Path B — Southernmost Dominion
[ED-311 RESOLVED — Option A (4 conditions + WR track), 2026-04-07]

| Condition | Threshold |
|-----------|-----------|
| PV held | ≥ 8 |
| Control T4 (Grauwald) AND T13 (Oastad) | both held |
| VTM | ≥ 3 |
| Warden Recognition (WR) | ≥ 2 |
| Season | ≥ 12 (Year 3) |

**WR track (0–4):** See params_board_game.md §Varfell Path B for full WR track rules.
**Blocked if:** WR has ever returned to 0 after first advancing past 1.
**Season gate (ED-666):** Path B represents demonstrated stewardship over time, not just accumulated territorial control. Season 12 is the earliest at which WR ≥ 2 through legitimate expedition work is plausible. Prevents S9 speed-run wins before other factions have reached meaningful development.

#### Path C — Thread Supremacy

| Condition | Threshold |
|-----------|-----------|
| PV held | ≥ 10 |
| VTM | ≥ 4 | *(PP-542: was = 5)* |
| RS | ≥ 50 |

---

### 3.5 Restoration Movement — Cultural Revolution (5 players only, hardest mode)


**Two-phase win condition:**

#### Phase 1 — Cultural Majority (threshold to unlock Phase 2)
PT ≤ 1 in ≥ 4 of the 15 playable territories (T1–T14, T17) *(PP-543: was ≥ 8; PP-478 had ≥ 5 — PP-543 supersedes both)*. Checked at each Accounting. Once met and held, Phase 2 becomes available. If the majority drops below 8, Phase 2 is locked again until it recovers.

#### Phase 2 — Cultural Uprising of T9 Himmelenger
Available only while Phase 1 condition is met. Declared once per game at any Accounting where Phase 1 holds. RM plays their Pontifex card and rolls: **Weaver Thread pool vs Ob = CI ÷ 10 (round up, min 1, max 5).**

Prerequisites: RS ≥ 25 (substrate must be stable enough for a coherent popular movement — below 25, physical destabilisation overwhelms cultural organisation). If RS < 25, Cultural Uprising is unavailable regardless of Phase 1 status.

Modifiers:
- T9 PT ≤ 1: Ob −1 (Cathedral already culturally shifted)
- WC ≥ 2: +1D (Wardens support the Uprising)
- CI ≥ 50 at declaration: Ob +1 (Church institutional authority is strong enough to resist)
- Church Mandate ≥ 5: Ob +1 (Church actively suppresses)

| Degree | Effect |
|--------|--------|
| Overwhelming | T9 transfers to RM administration. Church Mandate −2. CI −3 (institutional rupture). T9 PT −2 (population has decisively shifted — makes PT ≤ 3 holding condition immediately achievable from a PT 5 starting position). |
| Success | T9 transfers to RM administration. Church Mandate −1. |
| Partial | T9 does not transfer. PT in T9 −1 (popular sentiment shifted). Uprising attempt used up for this arc. |
| Failure | Uprising crushed. CI +2 (Church authority strengthened by resistance). T9 PT +1. Uprising attempt used up for this arc. |

#### RM Territory Control — Cultural Displacement
**Presence markers vs Phase 1 (important distinction):** Presence markers are the *holding mechanic* for post-Uprising T9 (≥ 3 required in T9). They are NOT the Phase 1 mechanic. Phase 1 (PT ≤ 1 in ≥ 4 territories) tracks Piety Track values, not Presence marker counts. Community Organizing places Presence markers; it does not directly reduce PT. PT reduction comes from: Cultural Reformation OW (Varfell, −1 PT), successful Uprising OW (T9, −2 PT), Calamity Drift (RS ≤ 50 in low-PT territories), and natural secular drift (−1 PT per 5 seasons without Church cultivation). RM players should prioritise PT reduction for Phase 1 and Presence markers for post-Uprising T9 holding — these are parallel but distinct goals.

**Overwhelming Uprising bonus:** An Overwhelming Cultural Uprising result automatically places +2 Presence markers in T9 (population mobilisation from the Uprising itself). These markers are placed before the holding condition is checked, ensuring OW Uprising immediately provides the foundation for holding T9.

RM holds T9 through cultural presence, not military garrison. Control is maintained while:
- RM has ≥ 3 Presence markers in T9
- PT in T9 ≤ 3 *(ED-588 resolved 2026-04-16: revised from PT ≤ 1. T9 starts PT 5 under Church management; ≤ 1 was unreachable post-Uprising without 4+ seasons of RM governance. PT ≤ 3 is achievable immediately after Uprising OW: PT 5 − 2 = PT 3. RM must then prevent Church Govern actions from rebuilding PT above 3.)*


#### Presence Marker Mechanics (ED-589 resolution)

**Community Organizing (RM Domain Action — political organizing, NOT Thread work):**
Pool = Mandate + Influence. TN 7. Ob 2 (base), +1 if territory has Church Governor, +1 if territory has Crown military garrison (≥ 1 professional unit).

| Degree | Effect |
|---|---|
| Overwhelming (3+ net) | +2 Presence markers in target territory. PT −1 (community rejects institutional piety). |
| Success (2 net) | +1 Presence marker in target territory. |
| Partial (1 net) | +1 Presence marker. RM Exposure +1 in territory. |
| Failure (0 net) | No marker. RM Exposure +2. Church Attention Pool +1 in territory. |

**Presence marker cap:** 5 per territory.
**Passive spread:** Per §7.1 Framework Drift — +1 adjacent territory/season when RM Stability ≥ 3.

**Suppression — Church (Preach variant):** Pool = Influence. TN 7. Ob = Presence markers in territory. Success: −1 marker, PT +1. Overwhelming: −2 markers, PT +1. Failure: no effect, RM Exposure −1 (attention diverted).

**Suppression — Crown (Enforce variant):** Pool = Military. TN 7. Ob 2. Success: −1 marker, Order −1 in target settlement. Failure: no marker removed, Order −1 (crackdown visible).

**Cell Resilience:** +1 Ob to all suppression when RM has Presence in ≥ 3 settlements in province (per settlement_layer_v30).

If either condition fails at Accounting, T9 reverts to the prior controller (or becomes Uncontrolled if the prior controller has been eliminated). RM cannot March, garrison, or build Fort in any territory. (PP-578)



**Win condition:** T9 under RM administration AND Phase 1 held, for 2 consecutive Accounting steps. Church cannot perform Territorial Seizure on T14 while RM holds it (the population actively resists institutional reconquest — Seizure Ob +3 vs RM-held T9).

---

### 3.6 Löwenritter — Military Regency (conditional faction, post-coup)

**[Design note: Löwenritter is a transitional faction, not a conventional winning faction. Post-coup, Löwenritter holds government until a legitimate successor is installed and their own faction takes over — that new ruler leads Crown (or whichever faction claimed the capital), not Löwenritter. Regency Establishment marks a successful handoff, not a Löwenritter victory in the traditional sense. Military Consolidation represents the edge case where no legitimate successor emerges within 8 seasons — a contested end state, not a stable governance resolution.]**

#### Primary — Regency Establishment

| Condition | Threshold |
|-----------|-----------|
| PV held | ≥ 10 |
| CI | < 50 |
| IP | < 60 |
| RS | > 40 |
| PI | ≥ 4 |
| Successor confirmed | Elske confirmed OR Torben Loyalty ≥ 6 |
| Season | ≥ 20 (Year 5) |

**Season gate (ED-667):** Elske confirmation requires minimum 4 successful Senator Outward actions from Loyalty 2 start — not achievable before Season 10–12 even optimally. Season 20 is the realistic floor for successor infrastructure to exist. Prevents premature Coup Counter cascade enabling Regency before the succession path is mechanically possible.

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
| PV held | ≥ 16 |
| Löwenritter Military | ≥ 5 |
| RS | > 35 |
| CI | < 60 |


#### §3.6a Post-Coup Succession Rule (ED-674)

When Coup Counter reaches 4 and Löwenritter activates:

**Immediate effects (Season of Coup):**

1. **Crown leadership vacated.** Almud is removed (imprisoned, exiled, or killed — determined by Ehrenwall's Conviction state at coup trigger). Crown faction does not dissolve but enters Interregnum: no Leadership actions, no treaty ratification, no Royal Decrees. Crown officers retain their Standing but cannot advance.
2. **Löwenritter chain of command governs.** Ehrenwall (Grand Master) is acting head of government. Knight-Commanders govern Crown-held territories at Accord −1 (military occupation). Kreutz's prior role (Royal Guard Captain) is vacated — his replacement is the senior Knight-Commander by Standing.
3. **Crown Ministries freeze.** All Ministry actions are suspended for 1 season (administrative disruption). After the freeze, Ministries resume under Löwenritter authority — Ministry NPCs serve whoever governs (per Haelgrund's Belief 1). Ministry Stability −1 from the disruption.
4. **Coup Counter resets to 0.** The counter tracks pre-coup instability; post-coup, the counter is irrelevant. It does not re-accumulate unless a second coup scenario emerges (requires Ehrenwall's removal + a successor Grand Master, which is outside standard campaign scope).

**Succession candidates (tracked from coup season onward):**

| Candidate | Path | Confirmation condition |
|---|---|---|
| Torben Almqvist | Dynastic heir | Torben Loyalty ≥ 6 + Parliamentary Succession Endorsement (faction_layer §5.4) |
| Elske (Schoenland) | Diplomatic marriage | Diplomatic Exchange success (per Elske Loyalty Track above) + Parliamentary Succession Endorsement |
| Player character | Deed-Claim | Standing ≥ 6 in Crown + 3 Legitimizing Authority tokens (per LIN-01) + inner-circle 3-of-5 supermajority |
| No candidate | Military Consolidation | 8 Löwenritter seasons elapse without confirmation → Alternate victory path activates |

**Succession confirmation:** When any candidate meets their condition, Löwenritter fires a Succession Scene (mandatory Zoom In). Ehrenwall formally transfers governance. The confirmed successor becomes Crown Leader. Löwenritter reverts to NPC faction status. All Crown officers' Standing is preserved. Accord in military-occupied territories recovers +1 per season under the new leader (maximum Accord 2 without faction-specific non-military action).

**Faction stat inheritance:** The new Crown leader inherits current Crown Mandate, Stability, and Wealth. Löwenritter Military score transfers as a one-time +1D bonus to the new leader's first Military Domain Action (the institutional military apparatus carries over, then dissolves into Crown structure). IP and CI are unchanged — these are peninsular, not faction-specific.

---

## 4. Co-Victory Pairings


| Pair | Conditions (all simultaneous at Accounting) |
|------|---------------------------------------------|
| **Crown + Hafenmark** | Crown PV ≥ 12 AND Hafenmark PV ≥ 12 AND PI ≥ 7 AND CI < 50 AND Crown Mandate ≥ 4 AND Hafenmark Mandate ≥ 4 AND neither faction has played Legionary targeting the other in preceding 4 seasons | *(PP-561 + PP-572, ED-391: 4-season no-active-conflict reinforces cooperative design)* |
| **Crown + Varfell** | Crown PV ≥ 12 AND Varfell PV ≥ 8 AND VTM ≥ 3 AND RS ≥ 50 |
| **Varfell + RM** | VTM ≥ 3 AND WR ≥ 2 AND ≥ 3 territories PT ≤ 1 AND RS ≥ 40 AND Varfell controls T13 | *(PP-545: VTM was ≥ 4; territories was ≥ 4)* |
| **Hafenmark + RM** | Hafenmark PV ≥ 10 AND ≥ 3 territories PT ≤ 2 AND PI ≥ 4 AND RS ≥ 40 | *(PP-546: territories was ≥ 4)* |
| **Löwenritter + Hafenmark** | Löwenritter PV ≥ 8 AND Hafenmark PV ≥ 8 AND PI ≥ 4 |
| **Church + Hafenmark (Partition)** | See §3.2. Crown Mandate ≤ 1, CI ≥ 50, Church ≥ 2 territories, Hafenmark ≥ 3, no active military conflict. Requires Phase 1 Declaration (see below). |

**Partition Phase 1 Declaration (ED-629):** Church+Hafenmark Partition cannot fire silently at Accounting. At Phase 1 of the season in which all Partition conditions are simultaneously met, either the Church player (or NPC Church AI) OR the Hafenmark player (or NPC Hafenmark AI) must publicly declare: "We assert Peninsular Partition this season." This declaration is visible to all players at Phase 1. Other factions then have the full Phase 4 Domain Action window to disrupt any single Partition condition: restore Crown Mandate from ≤ 1 to ≥ 2 (Crown Govern OW), initiate Battle between Church and Hafenmark (breaking non-aggression), reduce Church or Hafenmark territory count below the required minimum, or suppress CI below 50 (Hafenmark OW Suppress + Varfell VTM Discretion). If all conditions survive Phase 4 and hold at Accounting: Partition fires. **NPC AI Partition Declaration:** NPC Hafenmark and NPC Church both declare when all 5 conditions are met at Phase 1 evaluation. NPC AI never suppresses a Partition declaration.

**Incompatible:** Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM.

Co-victories are distinct from operational coalitions (PP-404/405). A faction may pursue a coalition without pursuing a co-victory.

---

## 5. World-State Transitions

**No shared loss. No fade to black.** Every crisis becomes a new chapter. The campaign continues.

### 5.1 RS=0 → Post-Calamity Era

The substrate tears. The world changes. Campaign continues.

- Faction acquisition suspended for 3 seasons (the world cannot be governed while it is coming apart)
- Mending Domain Echo doubled (MS +2/Success, +4/OW)
- Dissolution/Lock +2 Ob (destabilizing an already unstable substrate is harder)
- Mending Ob unchanged (recovery must be achievable)
- Founded Organizations gain +1 Domain Action for Community Organizing/Mending only
- Recovery: MS restored to 20 within 10 seasons
- True terminal: Second Calamity fires only after 10 seasons sustained at MS ≤ 5 — requires a decade of complete failure

**On the 3-season suspension:** The faction player's acquisition is suspended but the game is not idle. During suspension: defend existing territories' Accord from Post-Calamity degradation, contribute to Mending to end the era faster, position politically against rivals whose territories are also degrading. Scene Slate surfaces this clearly.

**"A Life in Valoria" significance:** The Post-Calamity Era is where personal-scale play is most consequential. Faction machinery is broken. Relationships, Thread competence, community organization, and the player's Founded Organization are the only functional currencies. A player who has been building Knots and Mending for 20 seasons is now the most powerful actor — not from a power boost, but because the institutions that dwarfed them have collapsed.

### 5.2 IP=100 → Phased Occupation Era

IP=100 does NOT trigger immediate Governorate imposition. It triggers a phased military invasion escalating as IP remains elevated. Three phases correspond to three geographic corridors into the peninsula.

**Phase 1 — First Mountain Pass (IP reaches 100):**
Altonian forces cross the first mountain pass. One border territory (lowest Accord, highest Military Ob for defender — T3 Lowenskyst or T10 Spartfell) comes under Active Invasion — contested, not occupied. Faction Domain Actions in contested territory +1 Ob. Personal-scale Ambush and Supply Interdiction events available. IP decay: Vanguard Commander Social Contest (Success: IP −3); passive decay if no battle for 3 seasons (IP −1/season).

If IP drops below 85 during Phase 1: invasion stalls, forward garrison withdrawn. Campaign continues without Occupation.

**Phase 2 — Additionally Through Schoenland (IP sustained at 85+ for 3 seasons after Phase 1):**
Second invasion corridor through Schoenland. Two additional territories under Active Invasion simultaneously (T1 Valorsplatz sea connection or T17 Halvarshelm). Altonian Governorate NPC faction formally established: Mandate 2, Military 4, Stability 3. Underground Network mechanics available to all non-Altonian factions. Resistance Work personal-scale actions activate. Two-front problem requiring coordinated faction response.

If IP drops below 75 during Phase 2: second corridor abandoned, Phase 1 conditions apply.

**Phase 3 — Additionally Through the Northwest Pass (IP sustained at 80+ for 3 more seasons):**
Third corridor from northwest (T4 Grauwald / T7 Rendstad). Governorate holds contiguous territory chain. Mandate rises to 3, Military 5, Stability 4. All faction Domain Actions in occupied territories +2 Ob. Governorate begins replacing local governance at Seat settlements — the existential crisis.

Recovery from Phase 3: IP reduced below 60 through sustained resistance. This is the game's hardest non-terminal challenge. Designed to be winnable but to feel like a war.

**IP Visibility Milestones:**
- **IP 60:** Intelligence Report — "Altonian forces massing at border." Scene Slate Priority 2. Factions in inter-faction conflict: Mandate check (Ob 2) to divert resources.
- **IP 80:** "Altonian advance forces in Schoenland corridor." Priority 1 scene: emergency session. Coalition-building via Social Contest available.
- **IP 90:** "Invasion imminent." All factions aware. Factions still in inter-faction Battle: Cohesion −20.

[EDITORIAL: ED-684 — IP milestones and Altonian Alignment. Source: historical_precedents_analysis.md §2.]

**Altonian Alignment:** NPC faction AI — when NPC faction reaches Mandate ≤ 2, chance it secretly contacts Altonian Vanguard Commander. Not a player action — a world event discovered through investigation. Effect: IP +5 immediate, aligning faction −2 Ob on Domain Actions during Occupation (collaborator). Discoverable via Niflhel intelligence or Riskbreaker investigation (Evidence Track threshold 4). If exposed publicly: aligning faction Accord drops to 0 all territories, Strain +3, all factions gain Casus Belli.

**Altonian Repulsion:** It is possible to REPEL the invasion entirely.

- **Military repulsion:** Defending faction(s) win Mass Battle vs Altonian forces with Overwhelming result → Altonian forces retreat one phase. Two consecutive Overwhelming defeats → full withdrawal. IP resets to 60, cannot rise above 80 for 10 seasons (Altonia rebuilding).
- **Diplomatic repulsion:** Schoenland diplomatic channel (Elske Loyalty ≥ 6, Social Contest vs Vanguard Commander Ob 4, IP < 80). Success: IP → 40. Overwhelming: IP → 20 + Non-Aggression Pact for 20 seasons.
- **Resistance repulsion (during Occupation):** Underground Network Mandate ≥ 3 AND Governorate Accord = 0 in all occupied territories AND Mass Battle vs Governorate Success+ → full withdrawal. IP → 30.
- **Permanently defeated:** If repelled by military Overwhelming ×2, or diplomatic Non-Aggression, or resistance uprising — Altonia is no longer a threat. IP freezes, cannot rise. Invasion storyline resolved.

**RM Presence → Underground Network:** When Occupation begins, RM Presence markers in occupied territories convert 1:1 to Underground Network points. RM's political organizing infrastructure functions as resistance infrastructure.

[EDITORIAL: ED-685 — RM Underground Network conversion. Source: historical_precedents_analysis.md §2.]

**Critical design note:** During Occupation, the game world continues ticking. RS declines. Thread phenomena intensify. The Southernmost calamity clock does not pause. Faction internal politics continue. The Occupation is a new constraint layered on existing systems, not a replacement.

### 5.3 All Factions Dissolved → Anarchy Era

No faction has standing Mandate. Parliament has no quorum. The Ministry continues.

- Any character with Standing 2+ retains personal network but loses institutional support
- Territory governance becomes direct: Charisma pool, not faction card
- Founded Organizations can claim Presence in ungoverned territories without Domain Action cost
- New faction formation: Founded Organization at Mandate 3 + 2 territories + Accord ≥ 2 for 2 seasons → Founding Declaration scene → formal faction
- Recovery: two or more formal factions establish Parliament quorum

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

## 7. CI Generation and Church Seizure

Starting CI: 28. CI caps at 100. Church may declare Mass Seizure at CI ≥ 60 (one-shot — see §3.2).

**Mass Seizure (see §3.2):** One-time event. Declaration gated: CI ≥ 60 available, probability (CI − 58)/42 per season, 100% at CI 100. Every territory with a Church building becomes a simultaneous Seizure target on declaration. Ob = 10 − PT − infrastructure (floor 1). No second attempt.

**Seasonal CI at Accounting:**
1. Institutional Momentum: CI +1 (passive).
2. Piety Yield: per territory where Church is Prominent (Church Mandate > controlling faction Mandate), add by PT. PT 5 = +1, PT 4 = +0.5, others = 0. Total = floor(sum).
3. Assert (optional Church action): Influence vs Ob 2. Success: CI +1. Failure: Cohesion −15 (derived_stats_v1).
4. Suppress (optional opponent action): Mandate vs Ob = floor(Church Mandate / 2) + 1. Success: negate Step 1 passive. Failure: Cohesion −15 (derived_stats_v1).
5. Hafenmark Structural Suppression: while Baralta Mandate ≥ 4, CI −1/season.

**Church Seizure (one-shot, replaces PP-494):** Pool = Influence + floor(CI/15). Ob = 10 − PT − infrastructure (floor 1). CI ≥ 60 required. One attempt only. Prominence required. Church Mandate ≥ 4. Overwhelming seizure: PT +1 (consequence, not cap-governed). See §3.2 for full specification.

---

## 8. RM Founding Mechanic (ED-620 — approved 2026-04-17)

WA-based spontaneous emergence struck (PP-478). RM emergence in Hybrid mode is exclusively via the Founding Mechanic.

**Prerequisites (all required):**
- Player PC Disposition ≥ +3 with Maret Vossen
- ≥ 2 territories have PT ≤ 2
- RS ≥ 40
- Player has completed ≥ 1 Community Organizing (political organizing — building consensus-governance cells, mutual-aid networks, community contacts)

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

| Faction | Start PV | Target PV | Gap | Key Difficulty | Est. Timeline |
|---------|-----------|------------|-----|----------------|---------------|
| Crown | 12 | 14 | +2 | Suppress 2 of 3 rivals (×2 political) | 12–16 seasons | *(PP-540)* |
| Church | 5 | 8 | +3 | Mass Seizure (one-shot) at CI ≥ 60; PT management | 14–18 seasons |
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
| PP-408 | PV | Territory Consolidation Values — remapped to PP-199 numbering |
| PP-409 | Victory | Crown Peninsula Sovereignty — PV ≥ 16 (gap restored to +6 after remapping) |
| PP-410 | Victory | Crown Dominion alternate — PV ≥ 22 |
| PP-411 | Victory | Hafenmark Parliamentary Sovereignty — PV ≥ 12 |
| PP-412 | Victory | Hafenmark Dynastic Assertion — T1 Valorsplatz (corrected from old T-number) |
| PP-413 | Victory | Church Altonian Theocracy — T9 Himmelenger (corrected from old T-number) |
| PP-414 | Victory | Varfell Path B provisional (ED-311 pending) |
| PP-415 | Victory | RM Cultural Revolution — RS ≥ 40 confirmed canonical |
| PP-416 | PT | PT action cap clarified — consequences not cap-governed |
| PP-417 | Church | Prominence mechanic defined (Church Mandate > controlling faction Mandate per territory) |
| PP-418 | Löwenritter | Military Consolidation — 8-season timer requires counter on Löwenritter mat |
| PP-419 | Hybrid | PT state transfer rules (replaces §9.1 directives-to-author format) |
| PP-420 | Hybrid | Victory condition check — replaces CI Win-Delay Rule |
| PP-421 | CI | CI 100 canonical cap + seizure threshold. CI 80 in params_board_game struck. |
| PP-422 | Co-Victory | WA/WC references replaced with WR in Varfell+RM co-victory |
| PP-423 | Crown | Formal Crown Treaty mechanic |
| PP-424 | System | Deed system dissolved — all factions |
| PP-425 | WR | Warden Recognition track defined (0–4) |
| PP-493 | Territory | All T-numbers remapped to geography_design.md canonical. Old names (Arcansheld, Vargstad, Eidursjo, Nordhelm, Mittelmark) replaced. PV total = 30. Starting PV: Crown 12, Hafenmark 8, Varfell 6, Church 3. |
| PP-494 | Church | Mass Seizure (one-shot): Pool = Influence + floor(CI/15), Ob = 10 − PT − infrastructure (floor 1). CI ≥ 60 required. Replaces Graduated Seizure. Church PV threshold reduced to ≥ 8. BALANCE-001 revised to include Church in equal win probability. |


---

## 5. Total Domination (ED-318 RESOLVED, 2026-04-07)

Available to all playable factions as alternate victory path.

| Condition | Threshold |
|-----------|-----------|
| PV held | ≥ 28 |
| All rival factions | Stability 0 (eliminated) OR Submitted |

Both conditions must hold simultaneously for 2 consecutive Accounting steps.

**Submission:** Any faction at Stability 0 that has not been eliminated may formally Submit at Accounting. Submitted faction: removed from victory competition, remains on board as NPC vassal (stats halved rounded down, no independent actions). The Total Domination faction must hold all non-Submitted, non-eliminated rivals at Stability 0 simultaneously.

---

## 6. Notes on Spoiler Dynamics (SIM-SPOILER-BG-01 + SIM-SPOILER-HY-01, 2026-04-07)

Simulation confirms that spoiler strategies are functional. Key findings:
- Church spoiling Crown: viable 5–8 season delay via Mandate maintenance + Inquisitor deployment. Crown counter: Royal Decree chain.
- Varfell spoiling Church: CI suppression via Counter-Narrative is minor (−0.135 CI/use expected); primary effect is AP pressure. Hybrid mode allows invisible spoiling via personal-scale Zoom In actions.
- Institutional Mandate trigger scope: [EDITORIAL: ED-324 — confirm trigger fires on Mandate-targeting actions only.]

## PP-478 Override — §3.5 Restoration Movement

**[PP-478 SUPERSEDES §3.5 above for mode applicability.]**

### RM Mode Applicability
- **BG-only mode:** RM solo victory and co-victories are UNAVAILABLE. RM is not a player faction.

### RM Solo Victory (Hybrid mode, post-Founding)
Phase 1: ≥ 4 territories PT ≤ 1, held 2 consecutive Accounting steps. *(PP-543: was ≥ 5)*
Phase 2: Cultural Uprising of T9 Himmelenger. RS ≥ 25 required (PP-467).
Roll: Weaver Thread pool vs Ob = CI ÷ 10. Win: T9 under RM administration + Phase 1 held × 2 Accounting steps.

### §4 Co-Victory Override (PP-478)
Varfell+RM and Hafenmark+RM co-victories: **Hybrid mode only, post-Founding.** BG-only: struck.

### §8 RM Emergence Override (PP-478)
The WA-based spontaneous RM Emergence mechanic (§8) is REPLACED by the Founding mechanic.
WA track remains (it governs Warden's Accord, not RM emergence). The triple-condition RM emergence
(WA ≤ −2 AND ≥ 3 territories PT ≤ 1 AND RS ≤ 50) is struck. RM emergence is now exclusively
via the Founding Mechanic in Hybrid mode.