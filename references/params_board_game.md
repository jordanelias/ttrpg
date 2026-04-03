<!-- version: v0.7.0+CORRECTED | source: valoria_bg_v04.md (canonical) + v05 corrections | last_updated: 2026-04-02 -->
<!-- PATCHES APPLIED: PP-169-PP-187 | CORRECTIONS: PP-188 (revert PP-171/172/173/176/186 errors; fix starting values; correct faction list) -->
<!-- AUTHORITATIVE SOURCE: designs/board_game/valoria_bg_v04.md for all faction cards, victory conditions, turn structure, starting values -->
<!-- NOTE: v05 is a correction document only (dice system, Ob minimum, inconsistency patches). v04 B-sections are the ruleset. -->
<!-- STALE CHECK: All known BG editorial blockers resolved as of PP-188. -->

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

## Degree Table (PP-179 — matches TTRPG)
| Net Successes | Degree |
|--------------|--------|
| ≥ 2× Ob | Overwhelming |
| = Ob | Success |
| 0 < net < Ob | Partial |
| ≤ 0 | Failure |
Ob 10 exception: Overwhelming unavailable. Partial requires net ≥ 5.

## Starting Values (v04 B2, PP-188 correction)
| Track | Start | Range | Notes |
|-------|-------|-------|-------|
| Rendering Stability (RS) | 72 | 0–100 | Rupture = shared loss |
| Theocracy Clock (TC) | **22** | 0–100 | TC 80 = Territorial Seizure. CORRECTED from 28 (P-32 was wrong). |
| Invasion Pressure (IP) | 20 | 0–100 | IP 75 = Altonian Vanguard |
| Parliament Integrity (PI) | **7** | 0–10 | CORRECTED from 5. |
| AER | 2 | 0–5 | Near IP clock. |
| Torben Loyalty | **3** | 0–7 | CORRECTED from 8. Active from game start. No IP trigger needed. |
| Elske Loyalty | 4 | 0–7 | Off-board card near T4. |
| Löwenritter Coup Counter | 0 | 0–4 | Public. Threshold 4 = coup eligible. |
| Warden Cooperation | 0 | 0–3 | Near T13. Inactive until Warden Emergence. |

## Faction Starting Stats (v04 B5)
| Faction | Mandate | Influence | Wealth | Military | Stability |
|---------|---------|-----------|--------|----------|-----------|
| Crown | 5 | 5 | 4 | 4 | 4 |
| Church | 5 | 6 | 5 | 4 | 5 |
| Hafenmark | 4 | 4 | 5 | 3 | 4 |
| Varfell | **3** | 4 | **3** | 4 | 4 |
| Restoration | 2 | 4 | 2 | 0 | 3 |
| Löwenritter (post-coup) | 3 | 2 | 3 | 6 | 5 |
| Guilds (NPC) | 3 | 4 | 6 | 2 | 5 |
| Niflhel (NPC) | — | 5 | 4 | — | 4 |

CORRECTIONS (PP-188): Varfell Mandate 4→3, Varfell Wealth 4→3. These match v04 B5.

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
12. Victory condition check. All Deed Tokens simultaneously = declare victory.
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

Unit starting Cohesion: Light Infantry 3, Heavy Infantry 4, Cavalry 4, Ranged 3, Artillery 3.

## Faction Capital Territories (v04 B2)
| Faction | Capital | Territory |
|---------|---------|-----------|
| Crown | Valorsplatz | T1 |
| Church | Himmelenger | T3 |
| Hafenmark | Hafenvalor | T6 |
| Varfell | Varfell | T9 |
| Guilds (NPC) | Halvardshelm | T11 |
| Niflhel (NPC) | Sigurdshalm | T10 |
| Restoration | No capital | — |
| Löwenritter | Arnesheld | T5 |

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
| 70+ | As above. Territorial Seizure protocol active. AER begins modifying TC gains |

### Invasion Pressure (IP) Effects
| IP Range | Effect |
|----------|--------|
| Below 30 | Trade with Schoenland: +1D |
| 30–59 | Trade with Schoenland: +1 Ob. All factions: +1D to Intel orders |
| 60–74 | Trade disrupted: +2 Ob. Proxy at T4: +1D military |
| 75+ | Altonian Vanguard deployed. AER ≥ 4: threshold rises to 80. AER 5: IP held at 50 |

## Victory Conditions (v04 B5 — PP-188 corrections)

### CROWN — Constitutional Stability (Primary, 5 Deeds + PI ≥ 3 gate)
| Deed | Condition |
|------|-----------|
| 1 | Mandate ≥ 5 |
| 2 | Control T1 + T2 + ≥ 2 other territories (total ≥ 4) |
| 3 | TC < 60 and IP < 75 simultaneously |
| 4 | PI ≥ 5 |
| 5 | Torben Loyalty ≥ 5 |
Gate: PI ≥ 3 to declare victory (not a Deed).

CORRECTIONS (PP-188): Added Deed 4 (PI ≥ 5) and Deed 5 (Torben Loyalty ≥ 5) which were missing. Removed IP escape clause from PP-172 (not in v04). Deed 2 territory count reverted to ≥4 (PP-186 was wrong — v04 says T1+T2+≥2 others = 4 total, not 5).

### CROWN — Dominion (Alternate)
Controls ≥ 8 territories AND one Submission Condition simultaneously (see AER/faction section).

### CHURCH — Holy State (Primary, 4 Deeds + AER ≥ 3 gate)
| Deed | Condition |
|------|-----------|
| 1 | TC ≥ 40 |
| 2 | Mandate ≥ 5 |
| 3 | Control T3 continuously ≥ 2 seasons |
| 4 | Control T1 |
Gate: AER ≥ 3 required to declare victory. Primary victory threshold: TC ≥ 70.

CORRECTIONS (PP-188): Reverted PP-171. Deed 4 is Control T1 (not "Crown Mandate ≤ 2"). Primary victory threshold is TC ≥ 70 per v04 — meeting all 4 Deeds plus AER ≥ 3 declares victory, but TC must be ≥ 70. Deed 1 (TC ≥ 40) is a milestone deed, not the victory threshold.

### CHURCH — Dual Theocracy (Alternate)
TC ≥ 60 + AER = 5 + IP ≤ 30.

### HAFENMARK — Three Paths (v04 B5)
Path A — Reformed Valoria (3 Deeds): RDT ≥ 4, PI ≥ 3, Reformed Settlement completed.
Path B — Theological Supremacy (2 Deeds): RDT = 6, TD = 5.
Path C — Parliamentary Consolidation (4 Deeds): PI ≥ 4, Mandate ≥ 4, control T6, no active Heresy Investigation ≥ 2 seasons.

### VARFELL — Three Paths (v04 B5)
Path A — Intelligence Hegemony (3 Deeds): VTM ≥ 3, control ≥ 3 territories, all other faction stats revealed at least once.
Path B — Southernmost Dominion (2 Deeds): control T12 + T13 simultaneously, VTM ≥ 3.
Path C — Thread Supremacy (3 Deeds): VTM = 5, control T12 + T13 + ≥ 1 other, RS ≥ 50 at Accounting.

CORRECTIONS (PP-188): Removed Intel-stat-based deeds (PP-173, PP-176 — no basis in v04). Reverted to v04 path structure.

### RESTORATION MOVEMENT — Network Victory
5 Presence markers in 5 non-adjacent territories, held 2 consecutive seasons + RS ≥ 50.
Or co-victory with compatible faction (see Co-Victory section).

### LÖWENRITTER — Regency Resolution (Primary, 5 Deeds)
| Deed | Condition |
|------|-----------|
| 1 | TC < 50 |
| 2 | IP < 60 |
| 3 | RS > 40 |
| 4 | PI ≥ 4 |
| 5 | Succession candidate: Elske confirmed OR Torben Loyalty ≥ 6 |
All 5 Deeds + legitimate successor installed = shared victory.

Alternate: Military Consolidation (≥8 territories + Military≥5 + RS>35 + TC<60) — only if Regency Resolution not fired after 8 Löwenritter seasons.

## Hollow Victory (v04 B12)
Running modifier per faction. Tracked publicly at each Year-End.
| Event | Modifier |
|-------|---------|
| Compromised Institutional Mandate | −0.5 Deeds per Compromise |
| Löwenritter Coup while player faction supported coup | −1 Deed |
| RS < 30 at victory declaration | −1 Deed |
| IP > 60 at victory declaration | −1 Deed |
| Allied faction holds Standing ≥ 3 vs your faction at victory | −0.5 Deed per faction |
| Faction holds ≥ 4 Casus Belli Standing | −1 Deed |
| PC Belief arc contradicted Uphold/Compromise pattern (hybrid) | −1 Deed per season |
| Torben Loyalty ≤ 1 at victory | −1 Deed |
If effective Deeds below required threshold: victory cannot be declared.

## Co-Victory Pairings (v04 B15)
| Pair | Path |
|------|------|
| Crown + Hafenmark | Crown holds Constitutional Stability AND Hafenmark holds Reformed Valoria (Path A) |
| Crown + Varfell | Crown holds Constitutional Stability AND Varfell holds Intelligence Hegemony |
| Varfell + Restoration | Varfell holds Thread Supremacy AND Restoration holds Network Victory (both require RS ≥ 50) |
| Hafenmark + Restoration | Hafenmark holds Reformed Valoria AND Restoration holds Network Victory |
| Löwenritter + Hafenmark | Löwenritter holds Regency Resolution AND Hafenmark holds Parliamentary Consolidation |
Incompatible: Church + Hafenmark, Crown + Church, Crown + Löwenritter.

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

Crown Deed 5 condition: Torben Loyalty ≥ 5.
Altonian Tutoring Demand triggers at IP ≥ **40** (not 30 — v04 B2: "Torben Tutoring Demand (IP ≥ 40 Event)").

## Elske Off-Board Card (v04 B2)
Princess Elske Almqvist is in Altonia (not on the board). Married to Duke Hardar Veldensohn, duchy borders T4.
Elske Loyalty: 0–7, starts 4. Tracked on off-board card near T4.

Contact: Crown or Löwenritter Senator Outward in T4 (Ob 2 at IP < 60; Ob 3 at IP ≥ 60).
Return: Elske Loyalty ≥ 6 + IP < 60 + Crown/Löwenritter unit in T4: Military vs Ob 2. IP +5 on success.

## TC Advancement (v04 B5 Church)
| Source | TC Gain |
|--------|---------| 
| Church controls T3 (Himmelenger) | +1/season |
| Assert choice (TC > 50, mandatory) | +1 |
| Attention Pool reaches threshold 5 | +1 |
| Emergency Powers (Crown or Löwenritter) | +1 |
| Free Trade Decree (Crown) | +1 |
| Church unit in non-Church territory at season end | +0.5/unit (max +1/season) |
| Church Territorial Seizure success | +2/territory seized |
| Reformed Settlement — Church Resists | +3 |
| Heresy Investigation confirmed success | +0.5 |
| Doctrinal Reach Milestone | +0.5/season |

**TC Decreases:**
Reformed Settlement Accommodate: −5. Sovereign Authority Doctrine (Hafenmark): −2 to −3. Baralta passive (Mandate ≥ 4): −1/season. Löwenritter Requisition Order success: −1. Royal Decree targeting TC: −1.

## TC 80 Territorial Seizure (PP-181 revised by PP-188 — reconciled with v05 P-23)
At TC ≥ 80: Church Territorial Seizure active. Per season:
Church may target territories. v04/v05 P-23: "Hard cap: maximum 2 territory transfers per seizure event per faction."
Roll: Church Military vs Defender Military, Ob 2.
| Degree | Effect |
|--------|--------|
| Overwhelming | Immediate seizure, no Standing cost. |
| Success | Seizure; TC +2. |
| Partial | Not seized; Templar Staging Token placed. |
| Failure | No seizure. |
Cap: 2 territory transfers per seizure event (v04/v05). PP-183's cap of 4 was too generous — corrected to 2.

## Theocracy Counter Starting Value — Canonical
TC starts at **22** (v04 B2: "TC starts at 22, not 15, per canonical timeline: 45 years of post-independence accumulation").
Prior params value of 28 (P-32) and 15 (early compilation) are both wrong.

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

## Faction Conviction Texts (PP-181, v04 confirmed)
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

## BG Co-Movement Resolution Protocol (PP-182 — P-14 compliance)
[Full protocol in PP-182 section — three-dimensional auto-effects for all Thread operations]
History Resonance markers (temporal), Attention Pool (epistemic), Primary result (actualized).
Thread Tension (TT) = sum of all History Resonance markers across board.
| TT | Effect |
|----|--------|
| 0–9 | Normal |
| ≥ 10 | All Thread operation Obs +1 globally |
| ≥ 15 | Thread Wound formation triggers automatically in any territory with ≥ 2 markers |

## TC 80 Seizure — Territorial Seizure (PP-188 corrects PP-183)
Cap: 2 territory transfers per seizure event (v04/v05 P-23). Previously set to 4 by PP-183 — reverted.

## Church Excommunication Ob Cap (PP-180)
Ob = min(target Mandate, 4). Maximum Ob 4 regardless of target Mandate.

## Drawn Battle Rule (PP-180)
Equal net successes: Stalemate. Both Cohesion −1. No territorial change.
Both at Cohesion 0: both units destroyed simultaneously. Territory uncontrolled.

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

## Warden Emergence (v04 B2/B13)
Condition: any faction's Southernmost Expedition passes Forgetting Check (Phase 5 Step 9).
On Emergence: Warden Token placed at position 0. Warden Cooperation Track activates.
Edeyja/Wardens NPC AI activates (B13: contain entity; investigate Niflhel; work alongside; emergency Mend).

## Institutional Mandate Uphold/Compromise (PP-180, v04 B7)
Each faction has a printed Institutional Mandate. When event challenges it:
- Uphold: act consistently. +1 Renown + 1 Stability.
- Compromise: strategic benefit. Hollow Victory −0.5 Deeds. Stability −1.

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
