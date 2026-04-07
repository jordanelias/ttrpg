<!-- version: v0.8.5+PP220 | source: valoria_bg_v05_simulation_and_patches.md (canonical per canonical_sources.yaml); action economy from stage_bg_proposal_v02.md | last_updated: 2026-04-03 -->
<!-- PP-249 2026-04-04: ED-142 resolved — BG Overwhelming: 2×Ob + floor 3, supersedes ED-031 -->
<!-- PATCHES APPLIED: PP-169-PP-187 | CORRECTIONS: PP-188 | PP-189 (v05 final) | PP-190–201 (BG balance, territory table, road network, map v2) | PP-219 (Southernmost access redesign) | PP-220 (Champion TS table) -->
<!-- AUTHORITATIVE SOURCE: designs/board_game/valoria_bg_v05_simulation_and_patches.md (faction stats, clocks, victory conditions); designs/board_game/stage_bg_proposal_v02.md (action economy, card-hand system PP-177) -->
<!-- NOTE: v05 is canonical for BG mechanics. v04 B-sections remain structural base. -->
<!-- STALE CHECK: PP-219/220 propagated. Next: ED-109–113 balance editorials open. -->

# params_board_game.md — Board Game Mode (v0.7.0)

## FACTION ASSIGNMENT (canonical, v04 B1)

### Playable Factions
| Faction | Player Count |
|---------|-------------|
| Crown | 2–5 players |
| Church of Solmund | 2–5 players |
| Hafenmark | 2–5 players |
| Varfell | 2–5 players |
| Restoration Movement | 5 players only (optional) |
| Löwenritter | Conditional: post-coup only |

### NPC-Only Factions (never playable)
Löwenritter (pre-coup), Riskbreakers, Inquisitors, Guilds, Schoenland, Niflhel, Altonia, Edeyja/Wardens.
Ministry: NPC faction (source document not yet identified — [GAP: Ministry NPC design doc not found in any read document. User confirmed it exists. Design blocked until source located.])

Note: Guilds and Niflhel do NOT have player victory conditions. All Guilds/Niflhel victory condition text from prior params versions is struck.

## Dice System (v05 correction)
d10 pool. TN 7 (standard).
| Face | Effect |
|------|--------|
| 1 | −1 success |
| 2–6 | 0 |
| 7–9 | +1 success |
| 10 | +2 successes |

Net successes = sum of contributions. May be negative (treated as 0 for degree purposes = Failure).
Ob minimum: 1. No modifier may push Ob below 1.
**Majority-1s (Catastrophic Failure) override: STRUCK** (v05 DESIGN DECISION 2026-04-02). All rolls resolve through standard degree table only. Low-pool results produce Failure; no additional consequence category exists.

## Degree Table (PP-179 + PP-249 — matches TTRPG)
| Net Successes | Degree |
|--------------|--------|
| ≥ 2× Ob AND ≥ 3 | Overwhelming |
| ≥ Ob | Success |
| 0 < net < Ob | Partial |
| ≤ 0 | Failure |
Overwhelming floor: net must be ≥ 3 regardless of Ob (matches PP-232 TTRPG rule). (PP-249)
ED-031 (Ob+1 surplus) is SUPERSEDED by PP-179 (2×Ob). PP-179 is canonical.
Ob 10 exception: Overwhelming unavailable. Partial requires net ≥ 5.
[FLAGGED FOR REVIEW: ED-142-R — confirm 2×Ob canonical; confirm floor of 3 applies to BG; confirm Ob 10 exception carries.]

## Starting Values (v04 B2, PP-188 correction)
| Track | Start | Range | Notes |
|-------|-------|-------|-------|
| Rendering Stability (RS) | 72 | 0–100 | Rupture = shared loss |
| Theocracy Clock (TC) | **28** | 0–100 | TC 75 = Territorial Seizure phase transition (TC freezes). P-32 sets starting value at 28. |
| Invasion Pressure (IP) | 20 | 0–100 | IP 75 = Altonian Vanguard |
| Parliament Integrity (PI) | **7** | 0–10 | CORRECTED from 5. |
| AER | 2 | 0–5 | Near IP clock. |
| Torben Loyalty | **10** | 0–10 | Active from game start. No IP trigger. Range extended to 10. |
| Elske Loyalty | 4 | 0–7 | Off-board card near T4. |
| Löwenritter Coup Counter | 0 | 0–4 | Public. Threshold 4 = coup eligible. |
| Warden Cooperation | 0 | 0–3 | Near T13. Inactive until Warden Emergence. |

**Warden Cooperation (WC) Effects:**
| WC | Effect |
|----|--------|
| 0 | No effect. |
| ≥ 1 | +1D to all Thread operations peninsula-wide. |
| ≥ 2 | RS decay rate halved (seasonal baseline −1 becomes −0.5, rounded down). |
| 3 | RS +2/season at Accounting. |

## Faction Starting Stats (v04 B5)
| Faction | Mandate | Influence | Wealth | Military | Stability |
|---------|---------|-----------|--------|----------|-----------|
| Crown | 5 | 5 | 4 | 4 | 4 |
| Church | 5 | 6 | 5 | 4 | 5 |
| Hafenmark | 4 | 4 | 5 | 3 | 4 |
| Varfell | **4** | 4 | **4** | 4 | 4 |
| Restoration | 2 | 4 | 2 | 0 | 3 |
| Löwenritter (post-coup) | 3 | 2 | 3 | 6 | 5 |
| Guilds (NPC) | 3 | 4 | 6 | 2 | 5 |
| Niflhel (NPC) | — | 5 | 4 | — | 4 |

CORRECTIONS (PP-191/PP-195): Varfell Mandate 4, Wealth 4. Varfell starts with 4 territories (T9/T10/T11/T12) — the most of any faction. Handicap is defensive: mountain range + Thread Wounds hem in expansion. Intelligence path is correct. Fortification constraint (PP-191) applies to outward expansion, not inward security. TC = 28 (P-32). TC victory = 65 (P-32).

## Stat Ceilings and Floors
| Stat | Floor | Ceiling |
|------|-------|---------|
| Mandate | 0 | 7 |
| Influence | 1 | 7 |
| Wealth | 0 | 7 |
| Military | 0 | 7 |
| Stability | 0 | 7 |

## Standard Action Ob Reference (P-21, v04 B3)
| Action | Default Ob | Key Modifiers |
|--------|-----------|---------------|
| Muster (Legionary Inward) | 2 | −1 T2 garrison |
| March (Legionary Outward) | No roll | Contested entry = Battle |
| Govern (Consul Inward) | Prosperity ÷ 2 (round up, min 1) | −1 own capital |
| Trade (Consul Outward) | Prosperity ÷ 3 (round up, min 1) | +1 IP≥30; +1 T10 |
| Diplomacy vs NPC (Senator Outward) | NPC Stability ÷ 2 (round up) | — |
| Diplomacy between players | Negotiated | Not a roll |
| Formal Crown Treaty (Senator Outward) | Target faction's Mandate | Crown only. Both factions must agree. See victory_architecture_v1.md §3.1. |
| Thread Operation (Pontifex/Weaver) | Ob 2 base | See PP-182 co-movement protocol |
| Investigate/Intel (Tribune) | 2 | +2 Ob in Church territory with Inquisitor |
| Spy (Tribune Outward) | Target Intel ÷ 2 round up | — |
| Parliamentary Manoeuvre (Hafenmark) | Opponent Influence ÷ 2 round up | — |
| Community Organising (Restoration) | 2 | — |
| Community Weaving (Restoration) | (100−RS)÷20 round up min 1 | −1 per Presence marker in territory |
| Fortify | Fort level + 1 | — |

All Obs: floor 1.

## Phase 4 Resolution Priority Order (v04 B4 — CORRECTED from stage_bg_proposal_v02 order)
| Priority | Order Type | Notes |
|----------|-----------|-------|
| 1 | Intel/Covert (Tribune) | Executes first; shapes information before other actions |
| 2 | Military (Legionary) — Battle | Battles resolve simultaneously per territory |
| 3 | Domain (Consul, Prefect, Architectus, Colonist) | Govern, Trade, Muster, March |
| 4 | Social (Senator) | Decree, Parliamentary Manoeuvre, Diplomacy |
| 5 | Thread operations (Pontifex, Weaver) | See PP-182 for three-dimensional auto-effects |
| 6 | Special/Unique Powers | Royal Decree, Excommunication, VTM ops, Sovereign Authority |
| 7 | Project advancement (Praetor) | Community Projects advance |

Within tier: descending Stability order. Ties: simultaneous.
NOTE: This corrects the stage_bg_proposal_v02 order (which put Thread Ops first). v04 is authoritative.

## Phase 5 Seasonal Accounting (v04 B4 — CORRECTED)
Execute in strict order:
1. Apply all pending attribute changes from resolved orders.
2. Faction Stability checks: any faction with ≥2 attribute loss this season: Stability pool vs Ob = loss magnitude.
3. Advance Cooldown Track (all items −1 slot; at 0: return to hand).
4. Clock advances: RS baseline drift (−1 at Year-End/Winter only). TC per formula. IP per Altonian pressure table. PI changes.
5. Church Attention Pool: resolve threshold responses. Pool resets to 0.
6. Thread Debt: tokens >1 season old: RS −1/token. Serviced tokens: no drain; permanent residual RS −0.5 recorded.
7. Clear Thread Resonance markers (all factions reset).
8. Check threshold events: draw one Event Card per threshold crossed.
8b. Milestone Bonus check.
9. Warden Emergence check.
9b. Vaynard-Edeyja same-season rule: if Warden Emergence at Step 9 AND VTM ≥ 4 AND Varfell played Tribune Inward in T13: Warden Cooperation +1 immediately.
10. Warden Cooperation check.
10b. Torben/Elske Loyalty events: apply Loyalty changes.
11. Hollow Victory totals: announced publicly, recorded.
12. Victory condition check. Any faction meeting all its victory conditions for 2 consecutive Accounting steps declares victory. See designs/board_game/victory_architecture_v1.md §3 for all faction conditions. Co-victory pairings checked simultaneously (§4). Shared loss conditions checked first (§5).
13. Season marker advances. If Winter (every 4th season): Year-End Accounting (B11).

## Year-End Accounting (every 4th season = Winter, v04 B11)
1. Apply Year-End TC and RS fractions.
2. RS baseline drift −1 (annual world degradation).
3. Löwenritter (if active): raise one free unit; Prosperity −1.
4. Torben Loyalty Year-End modifiers: Crown PI ≥ 5 →+1; Crown upheld Mandate 2+ consecutive seasons →+1; Löwenritter PI ≥ 3 without Emergency Powers →+1.
5. Elske Loyalty Year-End modifiers.
6. Hollow Victory totals announced publicly.
7. Once-Per-Year effects trigger.
8. Age track (optional Long Campaign only).
9. Check TC Year-End fractions for threshold crossings.
10. Season resets to Spring. Campaign year advances.

## Unit Muster Ob Table (from v04 B8 + compilation B6)
| Unit Type | Muster Ob | Prerequisites |
|-----------|----------|---------------|
| Light Infantry | 1 | None |
| Heavy Infantry | 2 | Prosperity ≥ 5 + Wealth Ob 2 |
| Cavalry | 3 | Prosperity ≥ 6 or officer History |
| Ranged | 2 | Officer with Ranged proficiency |
| Artillery | 4 | Wealth Ob 4 + 1 season construction |
| Knights Templar | Church only | Not standard Muster |

Unit starting Discipline: Light Infantry 3, Heavy Infantry 4, Cavalry 4, Ranged 3, Artillery 3.

## Faction Capital Territories — see Territory Table Reconciled (PP-195)
[Replaced by PP-195 territory table above — Hafenmark capital = Gransol T2, not Hafenvalor T6.]

## Clock Environmental Effects (v04 B2)

### Rendering Stability (RS) Effects
| RS Range | Effect |
|----------|--------|
| 72–50 | No modifier |
| 49–30 | Thread operations: −1 Ob. Non-Thread orders in T12/T13: +1 Ob |
| 29–20 | As above. Entity encounters possible in T12/T13. All Muster: +1 Ob |
| Below 20 | All orders all territories: +1 Ob. Community Projects +1/season. Entity encounters all uncontrolled territories |

### Theocracy Clock (TC) Effects
| TC Range | Effect |
|----------|--------|
| Below 30 | No modifier |
| 30–49 | Church orders: −1 Ob in Church-held territory |
| 50–69 | Church orders: −1 Ob everywhere. Non-Church Diplomacy targeting Church: +1 Ob. Mandatory Assert/Suppress each season |
| 70–74 | As above. Territorial Seizure protocol pending — Church prioritises seizure actions. |
| 75+ | TC frozen. Territorial Seizure protocol active. AER no longer modifies TC gains (TC frozen). |

### Invasion Pressure (IP) Effects
| IP Range | Effect |
|----------|--------|
| Below 30 | Trade with Schoenland: +1D |
| 30–59 | Trade with Schoenland: +1 Ob. All factions: +1D to Intel orders |
| 60–74 | Trade disrupted: +2 Ob. Proxy at T4: +1D military |
| 75+ | Altonian Vanguard deployed. AER ≥ 4: threshold rises to 80. AER 5: IP held at 50 |

## Victory Conditions
<!-- PP-424: Deed system dissolved. PP-408–PP-425: Conditions-based victory architecture. -->
**Canonical source:** designs/board_game/victory_architecture_v1.md

All faction victory conditions, co-victory pairings, and shared loss conditions are defined in the victory architecture document. The Deed-based system (v04 B5) is struck in its entirety.

**Summary (thresholds only — full conditions in victory_architecture_v1.md):**
| Faction | Primary TCV Target | Key Non-TCV Gate |
|---------|-------------------|-----------------|
| Crown | ≥ 16 | All rivals Mandate ≤ 2 or treated |
| Church | ≥ 10 (post-TC 75) | CV ≥ 3 in all held territories |
| Hafenmark | ≥ 12 | PI ≥ 5, Crown Mandate ≤ 3 |
| Varfell A | ≥ 10 | VTM ≥ 3, intel reveals |
| Varfell B | ≥ 8 | Warden Recognition ≥ 2 (ED-311 pending) |
| Varfell C | ≥ 10 | VTM = 5, RS ≥ 50 |
| RM | n/a | 5 territories CV ≤ 1, RS ≥ 40 |
| Löwenritter | ≥ 10 | TC < 50, IP < 60, RS > 40, PI ≥ 4, successor |

## Hollow Victory
<!-- PP-424: Deed-based Hollow Victory modifier table struck. -->
The Deed-based Hollow Victory modifier table (v04 B12) is struck. No mechanical penalty applies.

In Hybrid mode, a BG victory without personal arc resolution is a **narratively qualified victory** (P-32). The faction won; the character's arc is incomplete. This is a narrative marker only — it does not prevent victory declaration or impose a Deed modifier. See victory_architecture_v1.md §9.3.

## Co-Victory Pairings
<!-- PP-425: Updated from Deed-based path names to conditions-based. Full conditions in victory_architecture_v1.md §4. -->

| Pair | Minimum Conditions |
|------|-------------------|
| **Crown + Hafenmark** | Crown TCV ≥ 12 AND Hafenmark TCV ≥ 9 AND PI ≥ 5 AND TC < 50 |
| **Crown + Varfell** | Crown TCV ≥ 12 AND Varfell TCV ≥ 8 AND VTM ≥ 3 AND RS ≥ 50 |
| **Varfell + RM** | VTM ≥ 4 AND Warden Recognition ≥ 2 AND ≥ 4 territories CV ≤ 1 AND RS ≥ 40 AND Varfell controls T13 |
| **Hafenmark + RM** | Hafenmark TCV ≥ 10 AND ≥ 4 territories CV ≤ 2 AND PI ≥ 4 AND RS ≥ 40 |
| **Löwenritter + Hafenmark** | Löwenritter TCV ≥ 8 AND Hafenmark TCV ≥ 8 AND PI ≥ 4 |
| **Church + Hafenmark (Partition)** | Crown Mandate ≤ 1, TC ≥ 50, Church ≥ 2 territories, Hafenmark ≥ 3, no active military conflict |

**Incompatible:** Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM.

Co-victories require 2 consecutive Accounting steps except Partition (immediate on mutual declaration).

## Torben Loyalty Track (v04 B2 + B5 — PP-188 correction)
Range 0–7. Starts at **3**. Visible to all. Active from game start (no trigger needed).

**Gaining:**
- Senator Outward targeting Torben: Overwhelming +2; Success +1.
- Crown holds PI ≥ 5 at Year-End: +1.
- Crown upholds Institutional Mandate 2+ consecutive seasons: +1/Year-End.

**Losing:**
- Crown Compromises Institutional Mandate: −1.
- Crown issues Emergency Powers: −1.
- Löwenritter Coup fires: reset to 1.
- TC crosses 60: −1.
- Torben sent to Altonia (comply with tutoring demand): −2 immediately.

Crown Deed 5 condition: Torben Loyalty ≥ 5 (i.e. must not have degraded more than 5 points from start).
Altonian Tutoring Demand triggers at IP ≥ **40** (v04 B2: "Torben Tutoring Demand (IP ≥ 40 Event)") (not 30 — v04 B2: "Torben Tutoring Demand (IP ≥ 40 Event)").

## Elske Off-Board Card (v04 B2)
Princess Elske Almqvist is in Altonia (not on the board). Married to Duke Hardar Veldensohn, duchy borders T4.
Elske Loyalty: 0–7, starts 4. Tracked on off-board card near T4.

Contact: Crown or Löwenritter Senator Outward in T4 (Ob 2 at IP < 60; Ob 3 at IP ≥ 60).
Return: Elske Loyalty ≥ 6 + IP < 60 + Crown/Löwenritter unit in T4: Military vs Ob 2. IP +5 on success.

## TC Advancement (v04 B5 Church)
| Source | TC Gain |
|--------|---------| 
| Church controls T14 (Himmelenger) | +1/season |
| Assert choice (TC > 50, mandatory) | +1 |
| AER ≥ 3 (Altonian ecclesiastical momentum) | +1/season (PP-203 — bypasses Hafenmark domestic suppression) |
| Attention Pool reaches threshold 5 | +1 |
| Emergency Powers (Crown or Löwenritter) | +1 |
| Free Trade Decree (Crown) | +1 |
| Church unit in non-Church territory at season end | +0.5/unit (max +1/season) |
| Church Territorial Seizure success | +2/territory seized |
| Reformed Settlement — Church Resists | +3 |
| Heresy Investigation confirmed success | +0.5 |
| Doctrinal Reach Milestone | +0.5/season |

**TC Decreases:**
Reformed Settlement Accommodate: −5. Reformed Settlement Ignore: Church Stability −1, Influence −1 (penalised for non-response — ED-085 resolved 2026-04-03). Sovereign Authority Doctrine (Hafenmark): −2 to −3. Baralta passive (Mandate ≥ 4): −1/season. Löwenritter Requisition Order success: −1. Royal Decree targeting TC: −1.

## TC 75 Territorial Seizure (PP-192/PP-421 — TC 75 canonical)
At TC = 75: Church enters seizure phase. TC freezes at 75. Church shifts mode to territorial seizure. on **all Crown and Hafenmark territories** simultaneously.
This is not a Military action — it is an ecclesiastical consolidation of temporal power backed by Templar force.

### Seizure Roll (per territory)
Church Mandate vs Ob = territory Fort level + 1 (min Ob 1).
Roll for each Crown/Hafenmark territory separately. All rolls resolved simultaneously.

### TC Gain per Successful Seizure
| Territory | TC Gain on Success |
|-----------|-------------------|
| Standard Crown/Hafenmark territory | +1 |
| Gransol (T5, Hafenmark duchy capital) | +3 |
| Lowenskyst (T8, Hafenmark) | +1 |
| Eidursjo (T6, Hafenmark) | +1 |
| Spartfell (T7, Hafenmark) | +1 |
| Hafenvalor (T6, Crown port) | +1 |
| Lowenskyst (T7, Crown port) | +1 |
| Valorsplatz (T12, royal capital) | +5 |
| Himmelenger (T14, Grand Cathedral) | Already Church-held — excluded from seizure |

### Seizure Results
| Degree | Effect |
|--------|--------|
| Overwhelming | Territory seized immediately. No Standing cost. TC +territory value. PI −1. |
| Success | Territory contested (Church and prior faction both present). Battle required next season. TC +territory value queues to Accounting after battle resolves. |
| Partial | Templar Staging Token placed (P-30). Territory not seized. Prior faction may remove token with Military card play next season. |
| Failure | No effect. Church Mandate −1 (failed seizure weakens the Confessor's authority). |

### Seizure Constraints
- Seizure fires once when TC first crosses 75. TC freezes at 75 — no further TC advancement. Does not repeat unless TC drops and re-crosses 80.
- Church must have Mandate ≥ 4 to initiate (faction must be institutionally coherent to press the claim).

**Prominence (PP-417):** Church may only seize a territory where it is Prominent. Prominent = Church's global Mandate stat exceeds the controlling faction's global Mandate stat. Assessed at seizure declaration. Tie: not Prominent (tie goes to defender).
- Restoration Territory (T14, Eisengrund): not targeted — Church does not press claims against communities, only against political authorities.
- Varfell Territory (T9): not targeted — Varfell is not a Crown or Hafenmark territory.
- AER ≥ 3: +1D on all seizure rolls (Altonian ecclesiastical backing).
- PI at seizure: −1 per territory successfully seized (constitutional rupture cascades).

## Theocracy Counter Starting Value — Canonical
TC starts at **28**. (P-32, PP-189 correction. The 22 value from v04 B2 was superseded by P-32 in v05.)

## Parliament Integrity (PI) Scale
0–10. Starts at **7**. (Corrected from 5.)
| PI | State |
|----|-------|
| 8–10 | Full Parliament. Crown Policy requires Mandate ≥ 4. |
| 5–7 | Standard. Parliamentary Manoeuvre available. |
| 3–4 | Degraded. Parliamentary Manoeuvre +1 Ob. Crown Decree Ob reduced to 1. |
| ≤ 2 | Non-functional. Hafenmark loses Parliamentary Manoeuvre. Crown governs by decree. TC +2. |

PI degrades: Crown Emergency Powers (−1), Church territorial seizure (−1), Löwenritter coup (−3).
PI recovers: Hafenmark Parliamentary Manoeuvre success (+1), Crown Parliamentary Session policy (+1).

## Ethical Framework Modifiers (v04 B4)
| Faction | Bonus | Penalty |
|---------|-------|---------| 
| Crown (Virtue Ethics) | Public, visible actions −1 Ob | Covert/morally ambiguous +1 Ob |
| Church (Divine Command) | Doctrine-aligned −1 Ob | Thread-supporting +2 Ob |
| Hafenmark (Categorical Imperative) | Procedurally grounded −1 Ob | Ad hoc/precedent-breaking +1 Ob |
| Varfell (Epistemic Reason) | Evidence-based Intel −1 Ob | Emotional/reactive +1 Ob |
| Restoration (Rawlsian) | Community-benefiting −1 Ob | Hierarchical/exclusionary +1 Ob |
| Löwenritter (Military Honor) | Orders protecting Valorian sovereignty −1 Ob | Advancing personal/factional gain at Valoria's expense +2 Ob |

## Faction Conviction Texts (PP-181, ED-080/081 resolved 2026-04-03)
| Faction | Conviction |
|---------|-----------|
| Crown (Almud) | "The state is the only legitimate vessel of order." |
| Church (Himlensendt) | Faith |
| Hafenmark (Baralta) | "Faith is not mediated — it is lived. Anyone who is truly faithful can hear Solmund. Anyone who cannot should not rule." |
| Varfell (Vaynard) | "The strongest thread is the one others cannot see — and I have spent my life learning to pull it." |
| Restoration (Erikssen collective) | "The community is the only legitimate political unit." |
| Löwenritter (Ehrenwall) | "Valoria endures, whatever the cost." |

## Cascade Depth Cap (v04 B4)
Maximum 3 immediate mechanical effects per card play resolution step. Additional effects queue to next Accounting.
State-based modifiers (RS/TC/IP/PI environmental effects) do NOT count against this cap.

## Batch Card Hand (v04 B3 confirmed — Card-Hand system PP-177)
| Faction | Starting Hand |
|---------|--------------|
| Crown | 2× Legionary, 1× Consul, 1× Senator, 1× Prefect, 1× Recess |
| Church | 2× Senator, 1× Pontifex, 1× Consul, 1× Legionary, 1× Recess |
| Hafenmark | 2× Consul, 1× Senator, 1× Legionary, 1× Diplomat, 1× Recess |
| Varfell | 2× Tribune, 1× Legionary, 1× Consul, 1× Colonist, 1× Recess |
| Restoration | 1× Pontifex, 2× Praetor, 1× Senator, 1× Tribune, 1× Recess |

Domain Expertise (+1D when playing this card type):
Crown = Legionary | Church = Senator | Hafenmark = Consul/Prefect | Varfell = Tribune | Restoration = Pontifex

## Mandate Recovery (PP-174 — provisional, no v04 basis but not contradicted)
Govern Overwhelming in own capital: Mandate +1 (max once/season, max to faction starting Mandate).

## Trade Network Investment — Hafenmark Wealth Sink (PP-178)
Consul Inward, 2 Wealth cost. Ob 2. Places Trade Route tokens for +1D Trade bonuses.
Success: Trade Route token placed (+1D Trade this territory this season). Token persists until control transfer.
Overwhelming: As above + token links adjacent territory + Guild Favour +1 in non-capital territory.
Partial: Token placed, no bonus. Persists.
Failure: No token, Stability −1.

## BG Co-Movement Resolution Protocol (PP-182, ED-086 resolved 2026-04-03 — P-14 compliant)
[Full protocol in PP-182 section — three-dimensional auto-effects for all Thread operations]
History Resonance markers (temporal), Attention Pool (epistemic), Primary result (actualized).
Thread Tension (TT) = sum of all History Resonance markers across board.
| TT | Effect |
|----|--------|
| 0–9 | Normal |
| ≥ 10 | All Thread operation Obs +1 globally |
| ≥ 15 | Thread Wound formation triggers automatically in any territory with ≥ 2 markers |

## TC 75 Seizure — Territorial Seizure (PP-421)
Cap: 2 territory transfers per seizure event (v04/v05 P-23). Previously set to 4 by PP-183 — reverted.

## Church Excommunication Ob Cap (PP-180)
Ob = min(target Mandate, 4). Maximum Ob 4 regardless of target Mandate.

## Mandate Suppression — General Cap and Coalition Bonus (PP-296)
All Domain Actions targeting another faction's Mandate stat use Ob = min(target Mandate, 4). Maximum Ob 4 regardless of target Mandate. Consistent with Excommunication precedent (PP-180).

**Coalition suppression bonus (PP-296):** When 2+ factions play Domain Actions targeting the same faction's Mandate in the same Phase 4 resolution, each additional faction beyond the first adds +2D to the suppression pool (automatic — no formal pact declaration required).

| Factions suppressing | Pool bonus |
|---|---|
| 1 | +0D |
| 2 | +2D |
| 3 | +4D |
| 4+ | +6D (cap) |

Coalition bonus applies to the primary suppressing faction's pool. Secondary factions must each have a valid suppression action played this phase. Pool floor: 1D.

## Drawn Battle Rule (PP-180)
Equal net successes: Stalemate. Both Discipline −1. No territorial change.
Both at Discipline 0: both units destroyed simultaneously. Territory uncontrolled.

## Crown Policy Instrument (PP-180, v04 confirmed)
Once per season, Crown may issue one Policy if Mandate ≥ 4. Same Policy cannot repeat 2 seasons.
Resolution order: Policy → Hafenmark Opposition → Censor.
[Full Policy table in faction card section]

## Partial Mend — Thread Wound Risk (PP-184)
Partial or Failed Mend still places History Resonance marker (temporal auto-effect fires regardless of degree).
2 existing markers + Partial Mend = Thread Wound. Warning token required at 2 markers.

## Church Attention Pool — Per-Territory Rules (PP-185)
Per-territory ceiling: 10. Second Inquisitor at AP ≥ 6. Max 2 Inquisitors/territory.
Community Organizing success: AP −2 + expels one Inquisitor if AP drops below deployment threshold.

## Ranged Faction Military Modifier (ED-087 resolved 2026-04-03)
No BG Military modifier for ranged-specialist factions. BG correctly abstracts above weapon-type level. Intentional design decision — revisit only if faction asymmetry design requires it.

## Co-Movement Card Effects — BG Reference (PP-187)
20-card deck. Draw on: Partial Community Weaving, Niflhel Harvest, VTM preview.
| Category | Count | Effect |
|----------|-------|--------|
| TC effect | 4 | TC +1 immediately |
| RS stabilisation | 3 | RS +1 at next Accounting |
| Faction intel leak | 3 | One random faction learns Thread operation occurred here |
| Thread Debt adjacent | 3 | Thread Debt token in adjacent territory |
| History Resonance adjacent | 3 | History Resonance marker in adjacent territory |
| Benign | 4 | No mechanical effect |

## AER (Altonian Ecclesiastical Relationship) (PP-181, v04 confirmed)
Track 0–5. Starts 2.
[Full table in PP-181 section — confirmed by v04 B2]

## RDT (Reformed Doctrine Track) (PP-181, v04 B5 confirmed)
Hafenmark private track 0–6.
[Full mechanics in PP-181 section — confirmed by v04 B5]

## TD (Theological Dissatisfaction) (PP-181, v04 B5 confirmed)
Hafenmark private track 0–5.

## VTM (Vaynard Thread Mastery) (PP-181, v04 B5 confirmed)
Private 0–2; public 3+.
[Full table in PP-181 section — confirmed by v04 B5]

## Patience Protocol (Varfell, v04 B5)
Patience Counters (PC): 0–4 at VTM 0–3; 0–6 at VTM 4+. Private to Varfell player.
Gaining: +1 PC per season Tribune available but played differently; +1 PC per season pass on Senate purchase when Wealth ≥ 3. Max +2/season.
[Full spend table in v04 B5 — key: 4 PC = Spy anywhere on board; 6 PC at VTM 4+ = VTM +1]

## Riskbreakers (NPC, v04 B13 — reconciled with amendment2)
3 tokens per year. Priority tree evaluated at Phase 4 start.
[v04 B13 priority tree is authoritative — differs from amendment2 which was a proposal. v04 applies.]

## Warden Recognition Track (PP-425 — Varfell Path B)
Range 0–4. Varfell-only private track. Advances through successful Expeditions into T15 (Askeheim).

| WR | State |
|----|-------|
| 0 | Wardens unaware or indifferent. |
| 1 | Wardens have observed Vaynard (≥ 1 successful Expedition). |
| 2 | Wardens recognise Vaynard as steward. Varfell Path B unlocked. |
| 3 | Active cooperation (+1D Thread ops, equivalent to WC ≥ 1). |
| 4 | Edeyja has made substantive contact (Overwhelming Forgetting Check). |

**Advancing:** Overwhelming Forgetting Check → WR +1. Two consecutive Successes → WR +1. **Decreasing:** RM emergence (WA ≤ −2) → WR −2. No Expedition attempted for 3+ consecutive seasons → WR −1. If WR returns to 0 after advancing past 1: Varfell Path B permanently blocked this game.

## Warden Emergence (v04 B2/B13)
Condition: any faction's Southernmost Expedition passes Forgetting Check (Phase 5 Step 9).
On Emergence: Warden Token placed at position 0. Warden Cooperation Track activates.
Edeyja/Wardens NPC AI activates (B13: contain entity; investigate Niflhel; work alongside; emergency Mend).

## Institutional Mandate Uphold/Appease (PP-189 — v05 names this "Appease" not "Compromise")
Each faction has a printed Institutional Mandate. When event challenges it:
- **Uphold** (before roll): Roll proceeds normally. No cost.
- **Appease** (before roll): Triggering action cancelled entirely — no roll made. Mandate −1.
NPC rule: NPC factions Appease if Mandate ≥ 4 AND Stability ≤ 3.
Note: Prior params used "Compromise" — v05 PP-189 establishes "Appease" as the canonical term.

## Hollow Victory Mechanics (v04 B12)
[See full table above in Hollow Victory section]

## Intel Advancement Counter (PP-180 revised)
Intel Advancement Counter (0–3) on faction mat.
Each season with ≥1 successful Intel or Quiet Network order: Counter +1.
At Counter 4: Intel stat +1 (max 7); Counter resets to 0.
Note: Intel stat advancement is valid for NPC factions (Niflhel). Varfell victory paths do NOT require Intel stat advancement — they use VTM and territorial control.

## Accounting Phase Reference (PP-180 + v04 B4)
13-step sequence. See Phase 5 section above.

<!-- patch_history: references/params_board_game_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->

## PP-189 Final Corrections (v05 authoritative)
Corrections applied over PP-188:
- TC starting value: 28 (PP-188 had set it to 22 — wrong; P-32 in v05 explicitly raises it from 22 to 28)
- Church primary victory threshold: TC ≥ 65 (P-32 reduced from 70)
- TC 75 seizure: Church Mandate vs Ob = Fort + 1 (PP-192/PP-421); PP-183 had wrong formula
- Majority-1s override: STRUCK in v05 (DESIGN DECISION 2026-04-02)
- Institutional Mandate: Uphold/Appease (PP-189); prior params used "Compromise"
- canonical source: v05 is authoritative (v04 is the structural base; v05 is most recent)

## Varfell Territorial Expansion Constraint (PP-191)
Varfell's starting handicap is **positional**, not statistical.
Varfell (T9) is adjacent to: T5 (Arnesheld, Fort 3), T10 (Sigurdshalm, NPC/Niflhel), T12 (Oastad, uncontrolled/Thread Wound), T13 (Stillhelm, uncontrolled/Thread Wound).

Every viable expansion path from T9 runs into a fortified or hostile position:
- T5 (Arnesheld): Fort 3 — the strongest fortress on the board. Löwenritter garrison.
- T10 (Sigurdshelm): Varfell starting territory (Niflhel has network presence here, Trade +1 Ob from Black Market, but Varfell controls it). Expansion from T10 goes to T9 (already Varfell) or T11 (already Varfell) — no outward expansion available from this direction.
- T12 (Oastad): Varfell starting territory but Thread Wound — occupation costs RS. Not a liability but a constraint on holding it long-term.
- T13 (Stillhelm): Crown nominal territory, Thread Wound, Southernmost Access. Varfell must pass through T12 to reach T13.

**Fortification Combat Rule (clarification for Varfell):** When attacking a fortified territory, defending faction adds Fort level as bonus dice to defensive Military roll. Fort 3 (Arnesheld) = defender rolls Military + 3D. This is the primary mechanical reason Varfell's expansion is delayed — they must either neutralise fortifications first (Fortify-equivalent action in reverse: Tribune Sabotage to reduce Fort by 1, Ob = Fort level) or accept heavily unfavourable odds.

**Varfell Intelligence Path:** Varfell's dominant early game is information, not territory. The Intelligence Hegemony victory path (3 territories + VTM ≥ 3 + all stats revealed) doesn't require Crown or Hafenmark territory — it requires T9 + 2 others. T12 and T13 are reachable at VTM ≥ 2 (Thread-qualified presence bypasses normal March constraints into Thread Wound sites). Path B (Southernmost Dominion) and Path C (Thread Supremacy) both run through T12/T13.

Starting stat total revised: Varfell 4+4+4+4+4 = 20 points (vs Crown 22, Church 25, Hafenmark 20). Equal to Hafenmark on raw points; differentiated by asymmetric mechanics (Patience Protocol, VTM, positional constraint).


## Ministry — NPC Faction (PP-193)
### Ethical Framework: Procedural Consequentialism
The Ministry evaluates actions by whether they preserve the procedural conditions for governance. It is not loyal to Crown, Church, or Hafenmark — it is loyal to the functioning of the state itself. It is the civil service: clerks, administrators, record-keepers, tax collectors, enforcement officers.

**Ministry is always NPC-controlled.** It has no player victory condition and cannot be captured by any faction's card play.

### Ministry Stats
| Stat | Value | Notes |
|------|-------|-------|
| Mandate | 3 | Institutional legitimacy of the administrative apparatus |
| Influence | 4 | Reach into all territories via clerks and administrators |
| Wealth | 2 | State treasury access (limited — Crown controls the purse) |
| Military | 0 | Ministry has no military capacity |
| Stability | 5 | The civil service is hard to destroy |

### Ministry Tokens
Ministry maintains **Administrative Presence** tokens (AP-tokens, not to be confused with Attention Pool).
One AP-token per territory in which Ministry has clerks active. Starts with AP-tokens in T9 (Arcansheld), T10 (Nordhelm), T11 (Mittelmark), T12 (Valorsplatz). These represent the administrative apparatus of Parliamentary governance. (PP-204 corrected.)

### Parliament Connection — Direct Mechanics
Ministry is the mechanical engine behind Parliament Integrity (PI).

**Ministry Stabilisation (fires at Accounting Step 11, before Hollow Victory totals):**
Each season Ministry has an AP-token in T12 (Valorsplatz, Parliament seat): PI degradation from Crown Emergency Powers is reduced by 1 (to a minimum of −0 — i.e. Ministry can prevent one Emergency Powers PI loss per season). This represents clerks managing the parliamentary record and maintaining continuity despite political disruption.

**Ministry Legislative Record:**
At each Year-End Accounting: Ministry produces a Legislative Record for the prior year. Any Parliamentary Manoeuvre that succeeded (Hafenmark) this year is recorded as a Parliamentary Ruling. Effect: the first time each year a Parliamentary Ruling is recorded, PI +1 (the institution acknowledges the precedent). This is in addition to the standard Hafenmark Parliamentary Manoeuvre PI recovery.

**Ministry and Crown Policy:**
Crown Policy Instruments require Ministry countersignature. If Ministry Mandate < 2 (collapsed or compromised): Crown Policy actions cost +1 Ob (the administrative apparatus is too compromised to implement the decree cleanly). If Ministry Mandate = 0: Crown Policy actions unavailable until Ministry Mandate recovers.

**Ministry and Church Seizure (TC 75):**
Church Territorial Seizure of T12 (Valorsplatz) requires removing the Ministry AP-token first. If AP-token present: seizure Ob +1 (the administrative apparatus resists institutional capture). If seizure succeeds despite the token: Ministry AP-token in T1 is removed. All Crown Policy actions are now +1 Ob until Ministry reestablishes presence in T1 (requires 1 season of Ministry NPC action in T1).

**Ministry and Hafenmark:**
Hafenmark's Parliamentary Manoeuvre benefits from Ministry presence. If Ministry has AP-token in T1: Hafenmark Parliamentary Manoeuvre Ob −1 (the clerks facilitate process). If Ministry AP-token absent from T1: Parliamentary Manoeuvre Ob +1 (no procedural infrastructure to execute the manoeuvre).

**Ministry and Löwenritter Coup:**
If Löwenritter Coup fires: Ministry AP-tokens in T1 and T2 are removed immediately. Ministry Mandate −2. PI −3 (standard coup effect) but Ministry Stabilisation does not fire next season (Ministry is recalibrating). Ministry attempts to re-establish AP-tokens in recouped territories at rate of 1/season.

### Ministry NPC AI Priority Tree (runs at Phase 4, Priority 4 — Domain Actions tier)
| Priority | Condition | Action |
|----------|-----------|--------|
| 1 | PI ≤ 3 | Ministry plays Consul Inward (Govern) in T1: roll Ministry Mandate (3D) vs Ob 1. Success: PI +1 (clerks shore up parliamentary function). |
| 2 | T1 has no Ministry AP-token | Ministry plays Consul Inward in T1: roll Mandate 3D vs Ob 1. Success: AP-token placed in T1. |
| 3 | Any territory with AP-token has PI loss pending from Church Seizure | Ministry plays Senator Outward (Diplomacy) vs Church: Mandate 3D vs Church Mandate. Success: Church seizure of that territory delayed 1 season (Ministry files formal procedural objection). |
| 4 | Crown Mandate ≥ 4 AND PI < 5 | Ministry plays Senator Inward (Decree support): PI +1 (Ministry facilitates Crown constitutional governance). Requires Crown Mandate ≥ 4 — Ministry does not support a weakened Crown. |
| 5 (default) | None of above | Ministry plays Consul Inward in highest-Prosperity uncontested territory with AP-token: Prosperity maintained. |

### Ministry Compromise and Corruption
Factions may attempt to corrupt Ministry via Diplomacy.

**Corrupt Ministry (Consul Outward, any faction, Ob = Ministry Mandate ÷ 2 round up, min 2):**
Success: Ministry NPC Priority 4 fires in favour of the corrupting faction this season (Ministry supports that faction's Crown Policy or Parliamentary action regardless of current priorities).
Overwhelming: As above + Ministry AP-token in one territory of choice acts as if that territory is the corrupting faction's capital for one season (−1 Ob on all their actions there).
Failure: Ministry notes the attempt. Corrupting faction Stability −1. Ministry sends record to Riskbreakers (Riskbreaker Priority 6 now includes the corrupting faction's territory).

**Ministry Collapse (Mandate 0):** Ministry ceases NPC actions for 2 seasons. All Ministry AP-tokens removed. During collapse: Crown Policy +1 Ob, Parliamentary Manoeuvre +1 Ob, all Hafenmark Deed 3 (Parliamentary Consolidation) checks suspended. Collapse exit: Hafenmark or Crown plays Govern Inward in T1 (Ob 2). Success: Ministry Mandate returns to 1, AP-token placed in T1, collapse ends.

### Ministry and PI Track — Summary
| Ministry State | PI Effect |
|---------------|-----------|
| AP-token in T1, Mandate ≥ 2 | Emergency Powers PI loss −1 (Ministry prevents one loss/season) |
| AP-token in T1, Mandate ≥ 2, Hafenmark Manoeuvre success this year | Additional PI +1 at Year-End (Legislative Record) |
| AP-token absent from T1 | Hafenmark Parliamentary Manoeuvre Ob +1 |
| Ministry Mandate = 0 | Crown Policy unavailable |
| Church seizes T1 with AP-token present | Seizure Ob +1; if seized: AP-token removed, Crown Policy +1 Ob |
| Löwenritter Coup | T1+T2 AP-tokens removed; Ministry Mandate −2; Ministry Stabilisation suspended 1 season |

## Church of Solmund — Canonical Structure (PP-194, from original source documents)
Naming: "Church of Solmund" in source = **Church of Solmund** in all current docs (Galbados → Solmund).
Holy See = elected from among the Bishopry. Second only to the Monarch.

### Four Cardinals (appointed by Holy See)
| Cardinal | Domain | BG Mechanical Role |
|----------|--------|-------------------|
| Cardinal of Fortitude | Commands Knights Templar | Templar deployment; military arm of Church |
| Cardinal of Justice | Grand Adjudication + Inquisitors | Heresy Investigations; excommunication recommendations |
| Cardinal of Prudence | Tithes collection + Charities | Wealth generation; Church's economic arm |
| Cardinal of Temperance | Universities + Monasteries + Observatories | Scholarly institutions; AER maintenance |

**In BG, Cardinals are Church's internal officers.** When Church Stability drops below 3, one Cardinal may challenge the Confessor (per v04 B3 "internal schism" note). The challenging Cardinal acts on their own priority for one season.

**Cardinal-specific BG mechanics:**
- **Fortitude (Templar):** Templar deployment requires Cardinal of Fortitude to be active (Church Stability ≥ 2). At Stability ≤ 1: Templars do not deploy regardless of card play.
- **Justice (Inquisitors):** Heresy Investigations are issued under Cardinal of Justice. If Cardinal of Justice is compromised (via Niflhel or Varfell Intel action on Church): one Heresy Investigation this season is false (all factions notified that one Investigation this season was procedurally invalid).
- **Prudence (Tithes):** Church Wealth generation: +0.5 Wealth/season from tithed territories (rounds down at Year-End). Territories where Church has Favour ≥ 3 contribute to tithe income.
- **Temperance (Scholars):** AER maintenance. While Church controls at least one university city (T14 Himmelenger has a university): AER loss events are reduced by 1/Year-End (Temperance scholars maintain Altonian ecclesiastical relationships through scholarship).

**Cardinal schism trigger:** If Church Stability = 2 AND any faction played a Senator action targeting Church this season: one Cardinal (random or GM discretion) challenges the Confessor. That Cardinal's faction sub-action fires as an NPC Priority regardless of the Church player's card plays.

### Church Levies
Per canonical source: "Church has its own levies stationed in cathedrals across every major city. Two-thirds can be raised by the King at any given moment."
**BG mechanic:** Crown may, once per Year-End, raise Church levies: Crown gains Military +1 for one season (levies mobilised). Church loses equivalent Military capacity: Church Military −1 for that season. Church cannot refuse if Crown Mandate ≥ 4.

### Excommunication — Canonical Procedure
Excommunication recommended by Cardinal of Justice for heresy conviction. Excommunicated factions/leaders:
- Must pay penance: Wealth −1 per season until penance complete (3 seasons).
- Must perform public service: one action per season must be Senator Outward (Diplomacy) toward Church.
- Banishment (severe cases): faction permanently barred from Church-controlled territories.
**BG trigger:** Excommunication is available to Church as Unique Power (existing). The penance/public service mechanic is new — applies only after a successful Excommunication, tracking on the targeted faction's mat.

## Löwenritter — Canonical Structure (PP-194)
Per canonical source: Löwenritter serves the Monarch through military and civic arms via Lions' Council.

### Structure
- **Lions' Table:** Military arm. Coordinates military levies. Appoints Royal Guard.
- **Lions' Helm:** Naval arm. (BG: no direct naval territory but relevant to Schoenland sea route — Löwenritter Helm can deny T7 sea access to Schoenland at IP < 75 if Crown requests.)
- **Riskbreakers:** Sub-unit of Löwenritter, NOT independent faction. Operates outside the law to infiltrate cults and criminal organizations. [CORRECTION: Prior design documents treated Riskbreakers as independent NPC. Canonical source places them inside Löwenritter. They remain NPC-controlled but their Priority Tree now links to Löwenritter's coup counter and Crown's Mandate.]
- **Civic Arm:**
  - Knights of the Peace: patrol and enforce law. BG: when Löwenritter is active (any phase), one territory per season has its March Ob −1 (pacified roads).
  - Royal Investigators: counter-espionage and investigation. BG: once per season, Löwenritter may cancel one successful Intel action targeting Crown (Royal Investigators intercept).

**Riskbreaker correction (PP-194):** Riskbreakers are Löwenritter's covert sub-unit. In BG:
- Pre-coup: Riskbreakers fire under Löwenritter NPC AI Priority Tree (not independent).
- Post-coup: Riskbreakers become a Löwenritter player resource — once per season, may execute one Priority Tree action at no card cost.
- Riskbreaker "independence" in prior design documents (acting against Crown) remains mechanically valid — Riskbreakers serve Valoria, not Almud personally, consistent with canonical source.

## Ministry — Canonical Identity (PP-194)
Per canonical source: Valoria uses a system of ministries to provide services. Ministers nominated by Parliament, confirmed by Monarch.

Named ministries in source: Ministry of Law, Ministry of Guilds, Ministry of Logothetes, Ministry of Granaries, Ministry of Pure Water.

**BG Ministry faction** = the collective ministerial apparatus. Its Influence (4) represents reach across all ministries. Its Mandate (3) represents institutional legitimacy — it has authority but is subordinate to Parliament's nominations.

### Ministry of Guilds — Specific BG Role
The Ministry of Guilds monitors the guild system, arranges contracts between guilds and Imperial Court, sets taxation. In BG: Ministry of Guilds is the direct connection between Ministry (NPC) and Guilds (NPC).
- If Ministry Mandate ≥ 2 AND Guilds NPC is active: Guilds may not be targeted by Economic Leverage from other factions without a free Ministry counter (Ministry files procedural objection: +1 Ob to the Economic Leverage roll).
- If Ministry Mandate = 0: Guilds lose their trade contract protections — all Trade Ob in Guilds-controlled territories +1 (no Ministry to enforce non-competition).

### Parliament Nomination Mechanic (PP-194)
Per canonical source: Parliament nominates Ministers (confirmed by Monarch) and Rectorates.
**BG mechanic — Ministry Nomination:**
Once per Year-End: Parliament (= Hafenmark Parliamentary Manoeuvre success this year + Crown not in Emergency Powers) may nominate a Ministerial agenda. Choose one:
- **Ministry of Law agenda:** Ministry Mandate +1. All Heresy Investigation Obs +1 (legal proceduralism slows Church).
- **Ministry of Guilds agenda:** Guilds NPC Wealth +1. Ministry receives 1 Wealth (tithe/tax income).
- **Ministry of Logothetes agenda:** All faction Intel orders next season: −1 Ob (administrative records are accessible). Ministry Influence +1 for 1 season.
Crown must confirm: if Crown Mandate ≥ 3, confirmation is automatic. If Crown Mandate < 3: roll Mandate vs Ob 2. Failure: nomination blocked (Crown too weak to confirm).

### Parliament Deposition Mechanic (PP-194 — from canonical source)
Per canonical source: "Court Parliament has constitutional right to depose Monarch if deemed unfit for duties by the Holy See AND Imperial Court."
**BG mechanic — Royal Deposition:**
Fires if ALL of: PI ≥ 5 (Parliament functional), Church Mandate ≥ 5 (Holy See has standing), Crown Mandate ≤ 1 (Monarch deemed unfit), AND at least 2 other player factions have active Standing tokens against Crown.
Effect: Crown player must pass the Crown to Löwenritter (succession triggers) OR call an emergency Parliamentary Session (Senator Inward, Ob 3) to restore legitimacy. If neither: Crown faction is eliminated; Löwenritter Coup Counter immediately set to 4 (coup fires next season).

## Ducal Geography — EDITORIAL FLAG (ED-107)
Canonical source establishes different duchy boundaries than current v04 territory map.
[EDITORIAL: ED-107 — Territory assignment conflict. See stale_scan_bg_01.md. Requires user decision before territorial reassignment.]

Canonical duchy breakdown (for reference — not yet applied to map):
- **Valorsmark (Crown):** Valorsplatz (T1), Lowenskyst (T7), Himmelenger (T3), Arnesheld/Arcansheld (T5), Stillhelm (T13)
- **Hafenmark:** Gransol (T2, duchy capital), Eidursjo (T8), Spartfell (T4)
- **Varfell:** Varfell (T9, duchy capital), Sigurdshalm (T10), Halvardshelm (T11), Oastad (T12)

Current v04 map assignments differ significantly. Applying canonical geography would:
- Give Crown T7 (Lowenskyst) — currently Hafenmark
- Give Hafenmark T2 (Gransol) and T4 (Spartfell) — currently Crown and Crown
- Give Hafenmark T8 (Eidursjo) — currently Guilds NPC
- Give Varfell T10 (Sigurdshalm), T11 (Halvardshelm), T12 (Oastad) — currently Niflhel NPC, Guilds NPC, Uncontrolled
- Remove Guilds NPC and Niflhel NPC from territorial starting positions

This changes faction starting positions fundamentally and may destabilise balance. User decision required.


## Territory Table — Definitive (PP-199)
Faction counts per user: Varfell 4, Hafenmark 4, Crown 5, Church 1, Southernmost 1 = 15 land territories.
T16 Schoenland = maritime island NPC (off-peninsula extension).

| # | Territory | Faction | Fort | Pros | Special |
|---|-----------|---------|------|------|---------|
| 1 | Varfell | Varfell | 1 | 4 | NW lake city. VTM bootstrapping only. Einhir ruins: Restoration Weaving −1 Ob. |
| 2 | Sigurdshelm | Varfell | 0 | 3 | Far west. NW Altonian pass nearby. Niflhel Black Market: Trade +1 Ob, Niflhel Covert −1 Ob. |
| 3 | Halvardshelm | Varfell | 0 | 5 | W-central. Breadbasket +1 Pros/season uncontested. Muster Ob −1. Guilds CP-token. |
| 4 | Vargstad | Varfell ★ | 1 | 3 | SW duchy capital. Thread Wound. RS −1/season after 2 seasons occupation. Southernmost Zone 2. |
| 5 | Gransol | Hafenmark ★ | 1 | 5 | Center-north duchy capital. Garrison: Muster +1D. |
| 6 | Eidursjo | Hafenmark | 0 | 4 | Center-lake. March costs 2 cards. |
| 7 | Spartfell | Hafenmark | 2 | 3 | NE. NE Altonian pass. IP events fire here first. Elske's duchy borders here. |
| 8 | Lowenskyst | Hafenmark | 0 | 4 | East coast. Trade +1D. Schoenland sea route. |
| 9 | Arcansheld | Crown/Löwenritter | 3 | 4 | Central fortress. Martial Law −1 Ob. Fort max 4. |
| 10 | Nordhelm | Crown | 1 | 4 | NW of Arcansheld. Buffer between Crown heartland and Hafenmark/Varfell. [EDITORIAL: ED-108 name provisional] |
| 11 | Mittelmark | Crown | 0 | 4 | Central, between Arcansheld and Valorsplatz. [EDITORIAL: ED-108 name provisional] |
| 12 | Valorsplatz | Crown ★ | 2 | 6 | East coast. Kingdom capital. Parliament seat. Ministry AP-token. Hafenvalor = port sub-district. |
| 13 | Stillhelm | Crown | 0 | 2 | South coast. Southernmost Access point — last normal territory before the Southernmost. Non-Thread orders +1 Ob (difficult frontier terrain). RS −1/season any occupation. Normal military march and territorial control apply. Warden Cooperation track inactive here until Emergence. Expedition into T15 (Askeheim) requires Champion with TS ≥ 30 staging from T13 with at least 1 season of presence. |
| 14 | Himmelenger | Church ★ | 2 | 5 | Cathedral city. Church starts here. TC +1/season Church controls. Church Unique Power −1 Ob. |
| 15 | Askeheim | Uncontrolled | 0 | 1 | The Southernmost. Epicentre. Warden domain. **Not a normal territory — cannot be controlled by any faction under any standard military or domain action.** Access requires: (1) Champion with TS ≥ 30 present in T13 for ≥ 1 season. (2) Expedition declared (card play, Praetor or Tribune Inward, Ob 3). (3) Forgetting Check on entry (pool = Champion TS ÷ 10 round down, Ob 2; Restoration Weaver present: Ob −1; VTM 2+: Ob −1). Failure: Champion present but retains nothing — no Warden contact, no Cooperation advance, no VTM progress. Must wait 1 season and retry. Success: Warden Emergence fires if not already active. No faction control token placed. RS −2/season any non-Warden presence. Cannot be seized by TC 75 Church Territorial Seizure. |
| 16 | Schoenland | Neutral NPC | 1 | 5 | Maritime island, east of Valorsplatz. Altonian Trade. IP ≥ 75: Vanguard deploys. Intel orders visible to Altonia. |

★ = duchy/faction capital. T15 Askeheim = Southernmost territory (uncontrolled). T16 Schoenland = off-peninsula island.

## Starting Control — Definitive (PP-199)
| Faction | Territories | Count |
|---------|------------|-------|
| Varfell | T1 Varfell, T2 Sigurdshelm, T3 Halvardshelm, T4 Vargstad★ | 4 |
| Hafenmark | T5 Gransol★, T6 Eidursjo, T7 Spartfell, T8 Lowenskyst | 4 |
| Crown | T9 Arcansheld (shared), T10 Nordhelm, T11 Mittelmark, T12 Valorsplatz★, T13 Stillhelm | 5 |
| Church | T14 Himmelenger | 1 |
| Löwenritter | T9 (shared with Crown pre-coup) | shared |
| Uncontrolled | T15 Askeheim | — |
| NPC | T16 Schoenland | — |

## Adjacency — Definitive (PP-199)
Mountains impassable except at purple passes. Eidursjo lake: T6 march = 2 cards regardless.

T1 (Varfell) ↔ T2, T3, T6
T2 (Sigurdshelm) ↔ T1, T3
T3 (Halvardshelm) ↔ T1, T2, T4, T6, T10
T4 (Vargstad) ↔ T3, T13, T15
T5 (Gransol) ↔ T6, T7, T10, T14
T6 (Eidursjo) ↔ T1, T3, T5, T9, T10
T7 (Spartfell) ↔ T5, T8
T8 (Lowenskyst) ↔ T7, T12, T14, T16 (sea trade only)
T9 (Arcansheld) ↔ T6, T10, T12, T13
T10 (Nordhelm) ↔ T3, T5, T6, T9, T14
T11 (Mittelmark) ↔ T9, T12, T13
T12 (Valorsplatz) ↔ T8, T9, T11, T13, T14, T16 (sea trade only)
T13 (Stillhelm) ↔ T4, T9, T11, T12, T15
T14 (Himmelenger) ↔ T5, T8, T10, T12
T15 (Askeheim) ↔ T4, T13 (expedition access only)
T16 (Schoenland) ↔ T8 (sea trade), T12 (sea trade) [merchant NPC only — no military access, cannot be conquered]

## Road Network — Definitive (PP-199)

### Primary Roads
| Road | Route | Notes |
|------|-------|-------|
| King's Road | T12 (Valorsplatz) → T14 (Himmelenger) → T13 (Stillhelm) | Coastal arterial south. Natural route following the settled east coast. Church Inquisitor movement. Pilgrims. |
| Northern Coast Road | T12 → T8 (Lowenskyst) → T7 (Spartfell) | Coastal north. Main trade spine. Flat settled land all the way. Hafenmark primary export route. |
| Military Road | T12 → T11 (Mittelmark) → T9 (Arcansheld) | Inland strategic road. Löwenritter patrol route. Connects capital to the fortress. |
| Midland Road | T9 (Arcansheld) → T10 (Nordhelm) → T5 (Gransol) | Crown into Hafenmark. Most contested road. Crosses duchy boundary. |
| Lake Road | T5 (Gransol) → T6 (Eidursjo) → T1 (Varfell) | East shore of lake north-to-south. Hafenmark-Varfell trade route. Slow in winter (lakeside flooding). |

### Secondary Roads
| Road | Route | Notes |
|------|-------|-------|
| Western Valley Road | T1 (Varfell) → T3 (Halvardshelm) → T2 (Sigurdshelm) | Follows valley descending from lake to west coast. Remote. Niflhel network uses. |
| Southern Duchy Road | T1 (Varfell) → T3 (Halvardshelm) → T4 (Vargstad) | Varfell internal. Through Thread-active terrain in south. Only route to the capital from the north. |
| Fortress Extension | T9 (Arcansheld) → T13 (Stillhelm) | Interior route south through peninsula uplands. Löwenritter patrol. Slower than coastal King's Road but avoids Church territory. |
| Hill Track | T10 (Nordhelm) → T11 (Mittelmark) | Crown administrative road between buffer territories. |
| Pilgrims' Road | T11 (Mittelmark) → T14 (Himmelenger) | Inland connection to cathedral. Secondary — most pilgrims use King's Road coastal approach. |
| Warden Track | T13 (Stillhelm) → T15 (Askeheim) | Barely a track. Expedition access only. Non-Thread +1 Ob throughout. |

### Geographic Trade Notes
**East coast trade axis** (T7→T8→T12→T14): The commercial spine of Valoria. Flat coastal terrain, settled, maintained roads. Hafenmark controls the northern half (T7-T8), Crown the southern half (T12-T14 area). Guilds operate throughout.
**Varfell trade isolation**: All Varfell exports must cross Hafenmark territory (via Lake Road through T6, into T5 Gransol) to reach the east coast market. Varfell has no direct sea access — Sigurdshelm (T2) is on the west coast facing Altonian waters, not the trade sea. This is geographically correct and mechanically intentional (Wealth 4 despite isolation = internal resource wealth from the Halvardshelm breadbasket and Varfell mineral deposits).
**Schoenland** (T16): Maritime island. Trade connections = T8 (Lowenskyst) and T12 (Valorsplatz) by sea. T7 (Spartfell) connection = Altonian invasion staging route ONLY — IP event mechanic, not a normal trade connection. Schoenland merchants use Lowenskyst as their primary mainland port.

### Altonian Mountain Passes
| Pass | Connection | Notes |
|------|-----------|-------|
| NE Pass | T7 (Spartfell) ↔ T16 (Schoenland/Altonia) | Primary invasion route. IP events fire at T7. Vanguard enters here. |
| NW Pass | T2 (Sigurdshelm) ↔ off-map Altonia | Event-only. Not a playable march. Fires at IP ≥ 90. |

## Southernmost Zones (PP-199)
| Zone | Territory | Effect |
|------|-----------|--------|
| 3 (Outer) | T1 (Varfell), T9 (Arcansheld) | Thread Resonance +1 all factions when RS < 40. |
| 2 (Middle) | T4 (Vargstad), T3 (Halvardshelm) | Thread Wound. RS thresholds +10 early. |
| 1 (Inner) | T13 (Stillhelm) | Normal territory. RS −1/season any occupation (substrate proximity). Southernmost Access point — Expedition into T15 staged from here. |
| Epicentre | T15 (Askeheim) | RS −2/season non-Warden. Expedition required. |


## Southernmost Access System (PP-219)
### Authority: designs/ttrpg/edeyja_npc.md; Philosophical Foundations P-13

**T13 Stillhelm = normal territory.** Standard military march, territorial control,
Domain Actions all apply. Difficult frontier terrain (+1 Ob non-Thread) and RS drain
from substrate proximity, but no special access gate.

**T15 Askeheim = the Southernmost proper.** Not a normal territory. Cannot be
controlled by any faction through standard mechanics. The Warden presence and the
substrate damage itself make conventional occupation impossible — any military force
that enters encounters Thread operations at TS 75–80 scale. This has never needed
advertising. It has simply never been necessary.

### Expedition Procedure (T13 → T15)
Required sequence to access Askeheim:

1. **Stage in T13 (Stillhelm):** Faction must control T13 AND have a Champion with
   TS ≥ 30 present there for at least 1 full season. Champion must not have been
   used for military orders that season (Expedition requires full attention).

2. **Declare Expedition:** Phase 4, Praetor or Tribune Inward in T13.
   Roll: Champion pool (TS ÷ 10, rounded down, min 1D, max 3D) vs Ob 3.
   Modifiers: Restoration Weaver with Presence in T13: −1 Ob. VTM ≥ 2: −1 Ob.
   Failure: expedition does not depart this season. Try again next season.
   Success/Overwhelming: expedition departs. Move to step 3.

3. **Forgetting Check (on entry into T15):**
   Same pool vs Ob 2. Modifiers same as above.
   | Result | Effect |
   |--------|--------|
   | Failure | Champion enters T15 but retains nothing. No Warden contact. No Cooperation advance. No VTM progress. Champion returns to T13 next season. |
   | Partial | Emotional impressions retained. Warden Emergence fires (if not active). Cooperation +0 (Wardens observe but do not approach). |
   | Success | Facts retained. Warden Emergence fires. Cooperation +1. VTM +1 (Varfell only, if VTM ≥ 2). |
   | Overwhelming | Full retention. Warden Emergence fires. Cooperation +1. VTM +1 (Varfell). Edeyja makes contact. |

4. **Meeting Edeyja:**
   Requires Overwhelming on Forgetting Check, OR Success + 1 prior successful season
   in T15. She assesses the Champion. TS < 30: she will not engage. TS 30–39: brief,
   wary contact. TS 40+: substantive contact. She never leaves T15.

### Champion TS Values (BG)
| Champion | Faction | Starting TS | Qualifies at Start | Path to TS 30 |
|----------|---------|-------------|-------------------|---------------|
| Vaynard (VTM 3+) | Varfell | 30 (at VTM 3) | Yes — conditional on VTM development | VTM 3 achieved ~S7–9. Marginal: Forgetting pool = 3D. |
| Vaynard (VTM 4+) | Varfell | 40 | Yes | VTM 4 ~S10–12. Edeyja will engage substantively. |
| Almud Almqvist | Crown | 28 | **No** | Discovery Event: any Thread-significant event with Almud present, Spirit Ob 1. On success: TS 30, Certainty −1 (permanent). Politically costly: TC +1; Church learning triggers TC +2 + Heresy Investigation. |
| Lenneth Almqvist (Queen) | Crown | Unknown (not yet documented) | **Unknown** | Arc-dependent. Holds pre-Altonian sea-republic archive with first-person Thread-perception accounts (~180 AG). Potential TS development through intellectual confrontation with archive content + Thread exposure. [EDITORIAL: ED-119 — Lenneth full design required: starting TS, development path, stat block.] |
| Restoration Weaver (TS 18) | Restoration | 18 | No | Does not qualify as expedition leader. Provides Ob −1 support when accompanying a qualifying Champion. |
| Any other faction Champion | Any | < 30 | No | No standard development path. |

**Crown's Southernmost access is conditional on in-game development.**
Neither Almud nor Lenneth qualifies at game start. Crown must trigger
specific arc events (Almud Discovery Event; Lenneth archive arc) to
develop an eligible Champion. This is slower than Varfell's VTM path
but represents Crown's unique royal household angle on the Southernmost.

**Three factions have Southernmost access paths:**
- Varfell: fastest (VTM development, S7–12)
- Crown: conditional (Discovery Event / archive arc, unpredictable timing)
- Restoration: support role only (Weaver provides Ob −1, cannot lead)

### What "No Faction Control" Means in BG
- No control token can be placed in T15.
- No Govern, Trade, Muster, Fortify, or Decree orders execute in T15.
- TC 75 Church Territorial Seizure does not target T15.
- Varfell Path B (T4+T13) refers to control of T13 — a normal territory.
  The deed measures political and strategic presence at the Southernmost threshold,
  not occupation of the epicentre itself.
- Varfell Path C Deed 2 (T4+T13+1 other): same — T13 is the territorial condition.
  T15 is never the territorial condition.
- Warden Cooperation track advances through successful Expedition seasons in T15,
  not through territorial control.

## TC 75 Seizure — Territory Values (PP-421)
Targets all Crown and Hafenmark territories. Roll: Church Mandate vs Ob = Fort + 1.

| Territory | Fort | Ob | TC on Success |
|-----------|------|----|---------------|
| T12 Valorsplatz | 2 | 3 | +5 |
| T5 Gransol | 1 | 2 | +3 |
| T9 Arcansheld | 3 | 4 | +1 |
| T10 Nordhelm | 1 | 2 | +1 |
| T11 Mittelmark | 0 | 1 | +1 |
| T13 Stillhelm | 0 | 1 | +1 |
| T6 Eidursjo | 0 | 1 | +1 |
| T7 Spartfell | 2 | 3 | +1 |
| T8 Lowenskyst | 0 | 1 | +1 |
T14 Himmelenger = Church starting territory. Excluded from seizure (already consolidated).
AER ≥ 3: +1D all rolls. Ministry AP-token in T12: seizure Ob +1.

## Victory Condition Territory References (PP-199)
Crown Deed 2: control T12 (Valorsplatz) + T9 (Arcansheld) + ≥ 2 others (total ≥ 4).
Hafenmark Path C Deed 3: control T5 (Gransol, duchy capital).
Varfell Path B Deed 1: control T4 (Vargstad) + T13 (Stillhelm) simultaneously for 2 consecutive seasons. (PP-203 duration gate)
Varfell Path C Deed 2: control T4 (Vargstad) + T13 (Stillhelm) + ≥ 1 other. (PP-203 — corrected T-numbers)
Elske contact: via T7 (Spartfell, Hafenmark). Hafenmark may facilitate (+1D) or obstruct (+1 Ob). (T7 confirmed current numbering.)

## Ministry AP-Token Starting Positions (PP-203)
T9 (Arcansheld), T10 (Nordhelm), T11 (Mittelmark), T12 (Valorsplatz — primary Parliament seat).

## Guilds CP-Token Starting Positions (PP-203)
T3 (Halvardshelm), T5 (Gransol), T8 (Lowenskyst), T12 (Valorsplatz), T14 (Himmelenger). [PP-199 numbering confirmed — all correct.]

## Niflhel Network Starting Depth (PP-203)
T2 (Sigurdshelm) depth 2. T12 (Valorsplatz) depth 1. T14 (Himmelenger) depth 1. [Confirmed correct numbering.]

## Balance Findings and Proposals — BAL-BG-02 (PP-202)

### BAL-04 (P1): Crown Victory Front-Loaded
3 of 5 deeds pre-met at game start (Deed 1: Mandate≥5, Deed 3: TC<60∧IP<75, Deed 4: PI≥5).
Crown victory reduces to: hold T12+T9+2 others (Deed 2) and maintain Torben ≥ 5 (Deed 5).
[EDITORIAL: ED-109 — Crown balance. Options: (A) Raise Deed 1 to Mandate ≥ 6 (requires active maintenance). (B) Deed 3 becomes TC < 50 (tighter threshold — must actively suppress Church). (C) Add a 6th deed. (D) Accept as intended — Crown's difficulty is that maintaining passive deeds under pressure is the challenge, not achieving them.]

### BAL-05/06 (P1): Church Primary Victory Inaccessible
TC at net 0 per season (T14 control +1, Hafenmark suppression −1). TC ≥ 65 requires 37 seasons.
Church Deed 4 (seize T12) requires Military action at +2 Ob (doctrine penalty) against Fort 2.
[EDITORIAL: ED-110 — Church balance. Options: (A) Add TC generation source independent of Hafenmark suppression: "AER ≥ 3: TC +1/season additional" (Altonian ecclesiastical momentum bypasses domestic suppression). (B) Replace Deed 4 (seize T12) with "Crown formally acknowledges Church authority over religious appointments" — achievable via Diplomacy/Compromise, not Military. (C) Reduce TC victory threshold from 65 to 55. (D) Combination: (A) + (B).]

### BAL-08 (P1): Varfell Path B Under-Gated
T4 Vargstad (Varfell start) + T13 Stillhelm (Fort 0, adjacent, Crown cannot effectively hold) = fastest win path on board. VTM ≥ 3 reachable S7–9. Victory by S9–10 in favourable conditions.
[EDITORIAL: ED-111 — Varfell Path B balance. Options: (A) Add a third deed: "VTM ≥ 3, control T4+T13, AND RS ≥ 55" (RS preservation requirement slows Thread-heavy play). (B) Raise VTM requirement to 4 (adds 3–4 seasons). (C) Replace T13 with T12 Valorsplatz — far harder to seize and hold. (D) Add duration requirement: T4+T13 held simultaneously for 2 consecutive seasons (not just at Accounting).]

### BAL-09 (P1): TC Lock (Church/Hafenmark)
With Hafenmark Mandate ≥ 4: TC net = 0. Church cannot build TC toward victory.
Forcing Church to first neutralise Hafenmark before TC can build creates mandatory aggression sequence.
[EDITORIAL: ED-112 — TC lock resolution. This is likely partially intentional (Church must confront Protestant Reform). But if TC is permanently locked at 28, the Church faction is non-functional as a winner. Options: (A) AER ≥ 3 generates TC +1/season regardless of Hafenmark suppression (Altonian ecclesiastical leverage bypasses domestic politics). (B) Hafenmark suppression capped at −1/season maximum, but Church Assert (TC > 50) generates +2 not +1. (C) Church gets one TC gain per successful Heresy Investigation that Hafenmark cannot suppress. Recommended: (A) — the AER track is underused as a TC accelerant.]

### BAL-10 (P2): Varfell T13 Dominant Opening
T13 Stillhelm directly adjacent to T4 Vargstad. Fort 0. Crown nominal hold only (+1 Ob all actions).
Varfell can March T4→T13 in S1 at almost no cost.
[EDITORIAL: ED-113 — T13 opening. Options: (A) Give T13 Fort 1 (small warden garrison — the Wardens maintain some presence before Emergence). (B) Varfell march into T13 triggers immediate Warden Cooperation check (expedition trigger fires early, forcing Varfell to commit to the Southernmost path). (C) Accept — Crown holding T13 "nominally" is flavour; losing it S1 is correct fiction. Crown should simply not count T13 as a real starting territory for deed purposes.]

## TC Threshold Check — Zoom In Interaction (ED-056 resolved 2026-04-03)
TC threshold check fires at turn-end regardless of Zoom In suspension.
Zoom In cannot delay TC threshold check. Clocks continue during Zoom In personal phase.

## Concurrent Zoom In — Ordering (ED-072 resolved 2026-04-03)
If multiple factions trigger Zoom In simultaneously: faction-turn Accounting sequence order applies.
First battle completes before second begins.

## Crown Victory Condition — Redesign (ED-109 resolved 2026-04-03)
Crown must make Varfell AND Hafenmark submit OR own their territories outright.
3 pre-met deeds stand unchanged. 2 remaining deeds require active play against other major factions.
[Propagation: update Deed table when design doc revised.]

## Church TC Gain — Redesign Required (ED-110 resolved 2026-04-03)
Church must have more TC gain routes than Baralta has suppression capacity.
Baralta is one person, not a nation. Church spans multiple territories and actors.
Expand TC gain table before next BG simulation. Options under consideration: AER-linked gain, territory-hold bonuses, non-Hafenmark suppression routes.

## ED-019 Resolution (PP-261) [FLAGGED FOR DESIGNER REVIEW]
Faction unique tactic cards (2 per faction, provisional):
| Faction | Tactic A | Tactic B |
|---------|----------|----------|
| Crown | Royal Prerogative: +2D one Mandate roll | Iron Decree: cancel one opposing Domain Action (1/campaign) |
| Church | Sanctuary: protect one NPC from targeting for 1 season | Inquisition: force one faction to reveal one hidden stat |
| Hafenmark | Trade Leverage: +1D all Wealth rolls for 1 season | Constitutional Check: reduce one Crown action Ob by 2 |
| Varfell | Intelligence Supremacy: learn one faction's full stat block | Patience Protocol: pass; bank +2D for any future roll |
[FLAGGED: these are placeholder designs. Full design required before BG compilation.]

## ED-056 Resolution (PP-268)
Zoom In TC win-delay exploit: if a player triggers Zoom In specifically to suspend Accounting when TC ≥ 75 (Church phase transition), the Accounting still checks victory conditions at suspension point before Zoom In resolves.
Rule: **Victory condition check fires at the moment the threshold is crossed, not at Accounting completion.**
Zoom In cannot retroactively prevent a threshold that was crossed before the interrupt was declared.

## ED-072 Resolution (PP-269)
Confirmed from params_board_game: concurrent Zoom In ordering resolved by PP-112 (faction-turn Accounting sequence). Faction that triggered the Zoom In resolves first; others queue in Mandate order (descending). ED-072 resolved — already in params.

## ED-080 Resolution (PP-270)
Baralta Conviction text (Amendment2): "Faith is not mediated — it is immediate, or it is nothing."
Mechanical effect: Baralta gains +1D on any roll made in defence of direct Church authority (unmediated from doctrine). Loses −1D on rolls requiring institutional compromise.
[FLAGGED: confirm wording and mechanical expression.]

## ED-081 Resolution (PP-271)
Vaynard Conviction text (Amendment2): "The strongest thread is the one that does not know it is being pulled."
Mechanical effect: Vaynard gains +1D on any Intel-based action where his involvement is not publicly known. −1D if his faction affiliation is openly declared before rolling.
[FLAGGED: confirm wording.]

## ED-083 Resolution (PP-272)
VTM 5 ability (choose Actualized dimension of one Co-Movement card): P-14 compliance confirmed. Amendment2 "allows pre-draw selection" = choosing which of the two card dimensions becomes the outcome. This is not card manipulation — it is outcome selection from the existing draw. P-14 (Co-Movement must be genuine) is satisfied because the card was drawn legitimately; VTM 5 only selects the dimension, not the card. ED-083 resolved.

## ED-085 Resolution (PP-273)
Reformed Settlement Church responses confirmed (three options):
1. **Resist:** Church contests the settlement. Mandate −1 but TC gain continues; Hafenmark gains Deed.
2. **Accommodate:** Church accepts. TC gain suspended for 1 season. Parliament Integrity +1.
3. **Ignore:** Church neither contests nor accepts. No mechanical effect; sets up future escalation. TC gain halved for 1 season.
[FLAGGED: confirm Mandate −1 for Resist and PI +1 for Accommodate.]

## ED-086 Resolution (PP-274)
BG Co-Movement Resolution Protocol (P-14 compliance):
1. Declare Thread order type.
2. Roll faction stat pool (TN 7, Ob per order type).
3. Apply degree result (Overwhelm/Success/Partial/Failure from BG degree table PP-249).
4. Draw Co-Movement card.
5. Apply Actualized dimension first, then Temporal dimension.
6. Apply any VTM/ability modifications to outcome selection (not card draw).
7. Record RS change and attention pool change.
All BG Thread operations follow this sequence. No shortcuts.

## ED-108 Resolution (PP-277) [FLAGGED FOR DESIGNER REVIEW]
Crown territory names (provisional): T10 = **Nordhelm** (NW of Arcansheim), T11 = **Sudmarken** (SE border).
[FLAGGED: confirm names before map publication.]

## ED-109 through ED-113 Resolution (PP-278) [FLAGGED FOR DESIGNER REVIEW]
**ED-109 — Crown victory front-loaded:** Remove 1 pre-met deed from Crown starting conditions. Crown starts with 2 of 5 deeds met (not 3). Rebalances opening tempo.
**ED-110 — Church primary victory inaccessible:** Add fallback: if TC reaches 70 and Church holds 2+ territories, Church may declare Ecclesiastical Mandate victory (partial win, shared with one ally). Unblocks solo Church win path.
**ED-111 — Varfell Path B under-gated:** Require VTM ≥ 4 (not 3) to seize T13 via Path B. +1 VTM threshold gate.
**ED-112 — TC lock:** Hafenmark suppression capped at −1/season total (cannot be stacked via multiple actions). Church TC gain from T14 remains +1/season. Net: Church can advance TC by investing elsewhere.
**ED-113 — Varfell T13 opening dominance:** Add Fort 1 to T13 at game start (not Fort 0). Increases seizure Ob from 0-fort to Fort 1 resistance (+1D to defender).
[FLAGGED: all balance adjustments require playtesting confirmation.]

## BG Overwhelming Threshold — Final (PP-281 / PP-299)
Supersedes PP-179 (which incorrectly stated 'matches TTRPG').
BG Overwhelming = Ob+1 surplus (margin ≥ Ob+1 after ties → attacker wins).
BG Overwhelming floor: net ≥ 2 (not 3 — TTRPG floor of 3 is personal-scale drama; BG abstraction warrants lower floor).
ED-031 correct. PP-179 was documentation error. ED-142 resolved.

## ED-056 Resolution (PP-293) — Zoom In TC Win-Delay Exploit
Victory condition check fires at the moment a threshold is crossed, not at Accounting completion.
Zoom In cannot retroactively prevent a threshold crossed before the interrupt was declared.
[FLAGGED: confirm implementation in BG rules before compilation.]


## ED-072 Resolution (PP-294) — Concurrent Zoom In Ordering
Concurrent Zoom In order: faction that triggered the Zoom In resolves first; others queue
in Mandate order (descending). PP-112 confirmed. Already in params_board_game.
ED-072 resolved — no change needed.


## ED-080 Resolution (PP-295) — Baralta Conviction Text [FLAGGED]
"Faith is not mediated — it is lived. Anyone who tells you otherwise is selling something."
Mechanical effect: +1D when defending direct Church authority (unmediated from doctrine). −1D on institutional compromise rolls.
[FLAGGED: confirm wording and mechanical expression before NPC compilation.]


## ED-081 Resolution (PP-296) — Vaynard Conviction Text [FLAGGED]
"The strongest thread is the one others cannot see being pulled."
Mechanical effect: +1D on Intel actions where Varfell involvement is not publicly known. −1D if faction affiliation declared before rolling.
[FLAGGED: confirm wording before NPC compilation.]


## ED-083 Resolution (PP-297) — VTM 5 P-14 Compliance
VTM 5 ability (choose Actualized dimension of one Co-Movement card): P-14 compliant.
Amendment2 "pre-draw selection" = choosing which dimension becomes the outcome, not which card is drawn.
Card is drawn legitimately; VTM 5 selects the dimension only. P-14 satisfied. ED-083 resolved.


## ED-085 Resolution (PP-298) — Reformed Settlement Church Responses [FLAGGED]
Three Church responses confirmed:
1. Resist: Mandate −1; TC gain continues; Hafenmark gains Deed.
2. Accommodate: TC gain suspended 1 season; PI +1.
3. Ignore: TC gain halved 1 season; no other effect.
[FLAGGED: confirm Mandate −1 and PI +1 values before compilation.]


## ED-086 Resolution (PP-299) — BG Co-Movement Resolution Protocol
Protocol (P-14 compliance): 1) Declare order type. 2) Roll faction pool TN7. 3) Apply degree result.
4) Draw Co-Movement card. 5) Apply Actualized then Temporal dimension. 6) Apply VTM/ability to outcome selection.
7) Record RS and Attention changes. All BG Thread operations follow this sequence.


## ED-108 Resolution (PP-302) — Crown Territory Names [FLAGGED]
T10 = **Nordhelm** (NW of Arcansheld, buffer territory). T11 = **Sudmarken** (SE border zone).
[FLAGGED: confirm names before map and BG board publication.]


## ED-109–113 Resolution (PP-303) — BG Balance Adjustments [FLAGGED]
**ED-109 Crown front-loaded:** Remove 1 pre-met deed. Crown starts with 2/5 (not 3). Rebalances opening.
**ED-110 Church primary inaccessible:** Fallback: if TC ≥ 70 + Church holds 2+ territories → Ecclesiastical Mandate (partial shared victory).
**ED-111 Varfell Path B under-gated:** Require VTM ≥ 4 (not 3) to seize T13 via Path B.
**ED-112 TC lock:** Hafenmark suppression capped at −1/season total (cannot stack). Church TC from T14 remains +1/season.
**ED-113 Varfell T13 dominance:** Add Fort 1 to T13 at game start (+1D to defender, raising seizure difficulty).
[FLAGGED: all balance adjustments require playtesting confirmation before publication.]


## ED-142 Resolution (PP-322) — BG Overwhelming Threshold [FLAGGED]
BG Overwhelming: net ≥ 2×Ob AND net ≥ 3 (PP-179 canonical + PP-232 floor). ED-031 superseded.
Ob 10 exception: Overwhelming unavailable; Partial requires net ≥ 5.
[FLAGGED: confirm 2×Ob canonical; confirm floor of 3 applies to BG before BG compilation.]

## BG Overwhelming — Final Ruling (PP-262)
BG Overwhelming = Ob+1 surplus (attacker's net margin ≥ Ob+1).
Floor: net ≥ 2 (not 3 — TTRPG floor of 3 is personal-scale drama; BG abstraction warrants lower floor).
PP-179 ('matches TTRPG') was a documentation error. ED-031 (Ob+1) is correct.
