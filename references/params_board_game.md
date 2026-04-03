<!-- version: v0.7.1+PP189-V05FINAL | source: valoria_bg_v04.md (canonical) + v05 corrections | last_updated: 2026-04-02 -->
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
**Majority-1s (Catastrophic Failure) override: STRUCK** (v05 DESIGN DECISION 2026-04-02). All rolls resolve through standard degree table only. Low-pool results produce Failure; no additional consequence category exists.

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
| Theocracy Clock (TC) | **28** | 0–100 | TC 80 = Territorial Seizure. P-32 sets starting value at 28. |
| Invasion Pressure (IP) | 20 | 0–100 | IP 75 = Altonian Vanguard |
| Parliament Integrity (PI) | **7** | 0–10 | CORRECTED from 5. |
| AER | 2 | 0–5 | Near IP clock. |
| Torben Loyalty | **10** | 0–10 | Active from game start. No IP trigger. Range extended to 10. |
| Elske Loyalty | 4 | 0–7 | Off-board card near T4. |
| Löwenritter Coup Counter | 0 | 0–4 | Public. Threshold 4 = coup eligible. |
| Warden Cooperation | 0 | 0–3 | Near T13. Inactive until Warden Emergence. |

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
| 2 | Control T1 (Valorsplatz) + T6 (Hafenvalor) + ≥ 2 other territories (total ≥ 4) (PP-196) |
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
Gate: AER ≥ 3 required to declare victory. Primary victory threshold: **TC ≥ 65** (P-32).

CORRECTIONS (PP-188): Reverted PP-171. Deed 4 is Control T1 (not "Crown Mandate ≤ 2"). Primary victory threshold is TC ≥ 65 (P-32 in v05 reduced from 70). Meeting all 4 Deeds plus AER ≥ 3 plus TC ≥ 65 declares victory. Deed 1 (TC ≥ 40) is a milestone deed, not the victory threshold.

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

## TC 80 Territorial Seizure (PP-192 — user design decision)
At TC = 80: Church declares seizure attempt on **all Crown and Hafenmark territories** simultaneously.
This is not a Military action — it is an ecclesiastical consolidation of temporal power backed by Templar force.

### Seizure Roll (per territory)
Church Mandate vs Ob = territory Fort level + 1 (min Ob 1).
Roll for each Crown/Hafenmark territory separately. All rolls resolved simultaneously.

### TC Gain per Successful Seizure
| Territory | TC Gain on Success |
|-----------|-------------------|
| Standard Crown/Hafenmark territory | +1 |
| Gransol (T2, Hafenmark duchy capital) | +3 |
| Halvardshelm (T11, Hafenmark) | +1 |
| Eidursjo (T8, Hafenmark) | +1 |
| Hafenvalor (T6, Crown port) | +1 |
| Lowenskyst (T7, Crown port) | +1 |
| Valorsplatz (T1, royal capital) | +5 |
| Himmelenger (T3, Grand Cathedral) | Already Church-held — does not trigger seizure roll and generates no additional TC |

### Seizure Results
| Degree | Effect |
|--------|--------|
| Overwhelming | Territory seized immediately. No Standing cost. TC +territory value. PI −1. |
| Success | Territory contested (Church and prior faction both present). Battle required next season. TC +territory value queues to Accounting after battle resolves. |
| Partial | Templar Staging Token placed (P-30). Territory not seized. Prior faction may remove token with Military card play next season. |
| Failure | No effect. Church Mandate −1 (failed seizure weakens the Confessor's authority). |

### Seizure Constraints
- Seizure fires once when TC first crosses 80. Does not repeat unless TC drops and re-crosses 80.
- Church must have Mandate ≥ 4 to initiate (faction must be institutionally coherent to press the claim).
- Restoration Territory (T14, Eisengrund): not targeted — Church does not press claims against communities, only against political authorities.
- Varfell Territory (T9): not targeted — Varfell is not a Crown or Hafenmark territory.
- AER ≥ 3: +1D on all seizure rolls (Altonian ecclesiastical backing).
- PI at seizure: −1 per territory successfully seized (constitutional rupture cascades).

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
- TC 80 seizure: Church Military vs Defender Military Ob 2 (P-23); PP-183 had wrong formula
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
One AP-token per territory in which Ministry has clerks active. Starts with AP-tokens in T1 (Valorsplatz), T2 (Gransol), T6 (Hafenvalor), T7 (Lowenskyst). These represent the administrative apparatus of Parliamentary governance.

### Parliament Connection — Direct Mechanics
Ministry is the mechanical engine behind Parliament Integrity (PI).

**Ministry Stabilisation (fires at Accounting Step 11, before Hollow Victory totals):**
Each season Ministry has an AP-token in T1 (Valorsplatz, Parliament seat): PI degradation from Crown Emergency Powers is reduced by 1 (to a minimum of −0 — i.e. Ministry can prevent one Emergency Powers PI loss per season). This represents clerks managing the parliamentary record and maintaining continuity despite political disruption.

**Ministry Legislative Record:**
At each Year-End Accounting: Ministry produces a Legislative Record for the prior year. Any Parliamentary Manoeuvre that succeeded (Hafenmark) this year is recorded as a Parliamentary Ruling. Effect: the first time each year a Parliamentary Ruling is recorded, PI +1 (the institution acknowledges the precedent). This is in addition to the standard Hafenmark Parliamentary Manoeuvre PI recovery.

**Ministry and Crown Policy:**
Crown Policy Instruments require Ministry countersignature. If Ministry Mandate < 2 (collapsed or compromised): Crown Policy actions cost +1 Ob (the administrative apparatus is too compromised to implement the decree cleanly). If Ministry Mandate = 0: Crown Policy actions unavailable until Ministry Mandate recovers.

**Ministry and Church Seizure (TC 80):**
Church Territorial Seizure of T1 (Valorsplatz) requires removing the Ministry AP-token first. If AP-token present: seizure Ob +1 (the administrative apparatus resists institutional capture). If seizure succeeds despite the token: Ministry AP-token in T1 is removed. All Crown Policy actions are now +1 Ob until Ministry reestablishes presence in T1 (requires 1 season of Ministry NPC action in T1).

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
Naming: "Church of Galbados" in source = **Church of Solmund** in all current docs (Galbados → Solmund).
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
- **Temperance (Scholars):** AER maintenance. While Church controls at least one university city (T3 Himmelenger has a university): AER loss events are reduced by 1/Year-End (Temperance scholars maintain Altonian ecclesiastical relationships through scholarship).

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


## Territory Table — Final (PP-197, from annotated map)
Map annotations override all prior assignments. White dots = Hafenmark, Yellow = Crown, Green = Varfell.
Stars = faction capitals. Purple = Altonian mountain routes. Red = Southernmost epicentre + radiation zones.

| # | Territory | Faction | Fort | Pros | Special |
|---|-----------|---------|------|------|---------|
| 1 | Valorsplatz | Crown | 2 | 6 | Kingdom capital. Royal Court: Crown Policy −1 Ob. Parliament seat: Hafenmark Mandate orders −1 Ob. Ministry AP-token at start. Hafenvalor is the port district of this city (sub-location, not separate territory). |
| 2 | Gransol | Hafenmark ★ | 1 | 5 | Hafenmark duchy capital (white star). Garrison: Muster +1D. |
| 3 | Himmelenger | Crown | 2 | 5 | Crown territory. Church Grand Cathedral here — ecclesiastical presence, not political control. TC +1/season if Church Favour ≥ 3. Church Unique Power −1 Ob here. Yellow star cluster = Crown major settlement. |
| 4 | Spartfell | Hafenmark | 2 | 3 | White blob, northeast. Altonian mountain pass (purple route) nearby. IP threshold events fire here first. Elske's duchy borders here. |
| 5 | Arcansheld | Crown/Löwenritter | 3 | 4 | Yellow dot, central. Löwenritter Fortress. Martial Law −1 Ob. Fort max 4. |
| 6 | Hafenvalor | Crown | 1 | 5 | Crown port city, adjacent to Valorsplatz. Major harbour. Trade +1D (port). Hafenmark is named after this city's hinterland — the name predates the duchy's political independence. |
| 7 | Lowenskyst | Crown | 0 | 4 | Yellow blob, east coast. Northern port. Schoenland sea route terminus. |
| 8 | Eidursjo | Hafenmark | 0 | 4 | White blob near lake. Difficult terrain: March costs 2 cards. Lake/forest region. |
| 9 | Varfell | Varfell | 1 | 4 | Green blob (city labeled, northwest). VTM research here only. Einhir ruins: Restoration Weaving −1 Ob. Note: Varfell duchy capital star (green star) is shown SW on map — see Oastad note. |
| 10 | Sigurdshelm | Varfell | 0 | 3 | Western city. Niflhel Black Market presence: Trade +1 Ob (Niflhel network depresses legitimate commerce), Niflhel Covert −1 Ob. Northwest Altonian mountain pass (purple route) passes near here. |
| 11 | Halvardshelm | Hafenmark | 0 | 5 | White blob (MAP OVERRIDES canonical source — Halvardshelm = Hafenmark, not Varfell). Breadbasket: +1 Prosperity/season uncontested. Muster Ob −1. Guilds operate commercially here (CP-token at start). |
| 12 | Oastad | Varfell | 0 | 3 | Green star on map = Varfell capital marker in this region — Varfell duchy capital may be understood as Oastad as the administrative seat of southern Varfell, OR the green star marks the Varfell duchy's southern stronghold. Thread Wound: RS −1/season after 2 seasons any occupation. Southernmost access zone begins here. |
| 13 | Stillhelm | Crown | 0 | 2 | Yellow dot, south coast. Crown nominal control. Southernmost Access: Non-Thread orders +1 Ob. RS −1/season any occupation. Warden Cooperation track here. |
| 14 | Eisengrund | Restoration (informal) | 0 | 4 | Unlabeled south territory. Einhir Heartland. Restoration Influence −1 Ob. Church Influence +1 Ob. |
| 15 | Schoenland | Neutral NPC | 1 | 5 | Off-map. User: "east of Valorsplatz" — Altonian port, sea-accessible. Altonian Trade. At IP ≥ 75: Altonian Vanguard deploys. Intel orders visible to Altonia. |

★ = duchy/faction capital

## Adjacency — Final (PP-197, from annotated map yellow dotted lines + geography)
T1 (Valorsplatz) ↔ T3 (Himmelenger), T5 (Arcansheld), T6 (Hafenvalor), T7 (Lowenskyst)
T2 (Gransol) ↔ T4 (Spartfell), T8 (Eidursjo), T11 (Halvardshelm)
T3 (Himmelenger) ↔ T1, T6, T13 (south coast), T14 (Eisengrund)
T4 (Spartfell) ↔ T2, T15 (Schoenland — Altonian mountain pass, northeast purple route)
T5 (Arcansheld) ↔ T1, T8 (Eidursjo valley), T9 (Varfell — mountain pass), T12 (Oastad — southern route)
T6 (Hafenvalor) ↔ T1, T3, T7
T7 (Lowenskyst) ↔ T1, T6, T15 (sea route)
T8 (Eidursjo) ↔ T2, T5, T9, T11
T9 (Varfell) ↔ T5, T8, T10, T12
T10 (Sigurdshelm) ↔ T9, T11 [western Altonian mountain pass nearby — purple route; Altonia cannot enter here without IP ≥ 75 event]
T11 (Halvardshelm) ↔ T2, T8, T10, T12
T12 (Oastad) ↔ T5, T9, T11, T13, T14
T13 (Stillhelm) ↔ T3, T12, T14
T14 (Eisengrund) ↔ T3, T12, T13
T15 (Schoenland) ↔ T4 (mountain pass), T7 (sea)

## Starting Control Summary — Final (PP-197)
| Faction | Territories | Count |
|---------|------------|-------|
| Crown | T1, T3, T5 (shared), T6, T7, T13 (nominal) | 6 |
| Hafenmark | T2 (capital), T4, T8, T11 | 4 |
| Varfell | T9, T10, T12 | 3 |
| Church | None (cathedral presence in T3, city Favour elsewhere) | 0 |
| Restoration | T14 (informal) | 1 |
| Löwenritter | T5 (shared with Crown pre-coup) | shared |

## Altonian Mountain Routes (PP-197)
Two passes through mountains (purple lines on map):
- **Northeast pass** (near Spartfell): T4 (Spartfell) ↔ T15 (Schoenland/Altonia). Primary invasion route. IP threshold events fire at T4 first.
- **Northwest pass** (near Sigurdshelm): T10 (Sigurdshelm) ↔ off-map Altonian territory. Secondary. Only relevant at AER 5 or IP ≥ 90 (extreme escalation). Riskbreakers monitor this pass.

## Southernmost — Radiating Zone (PP-197)
Red concentric arcs on map, epicentre at far south tip of peninsula.
- **Epicentre** (beyond T13/T14): Site of the Calamity. The Thread substrate is most damaged here. Edeyja and the Wardens work at the epicentre. Not a territory — it is a location within T13/T14 territory. Warden Emergence fires when expedition reaches this area.
- **Zone 1** (T13, T14 — inner ring): Active Thread Wound sites. RS −1/season any occupation. Warden Cooperation track active after Emergence.
- **Zone 2** (T12, Oastad — middle ring): Thread Wound active. RS thresholds trigger +10 early.
- **Zone 3** (T9, T5 — outer ring): Substrate sensitivity. Thread Resonance +1 in these territories for all factions when RS < 40.
The rings are not hard mechanical zones but inform which territories are affected by RS threshold events first.

## Faction Starting Positions — Revised Balance Note (PP-197)
Hafenmark starts with 4 territories (T2 Gransol capital, T4 Spartfell, T8 Eidursjo, T11 Halvardshelm).
This improves Hafenmark's opening position significantly vs prior PP-195 (3 territories).
Hafenmark now has the Breadbasket (T11 +1 Prosperity/season) and Eidursjo forest access.
Hafenmark military handicap (Military 3) is offset by strong economic starting position (T11 Breadbasket, T8 trade access, T2 Garrison).

Varfell starts with 3 territories (T9, T10, T12).
T12 is a Thread Wound — net cost to hold. Effective starting position: T9 + T10 = 2 productive territories.
This confirms Varfell's position as strategically constrained but intelligence-rich.
VTM path through T12 → T13 (Southernmost) is the correct Varfell expansion path — through Thread-active territory that other factions avoid.


## Adjacency (from physical map)
T1 (Valorsplatz) ↔ T3 (Himmelenger), T5 (Arcansheld), T6 (Hafenvalor), T7 (Lowenskyst)
T2 (Gransol) ↔ T4 (Spartfell), T8 (Eidursjo), T9 (Varfell — via Eidursjo valley)
T3 (Himmelenger) ↔ T1, T6, T14 (Eisengrund — southern border)
T4 (Spartfell) ↔ T2, T15 (Schoenland — Altonian border)
T5 (Arcansheld) ↔ T1, T9 (Varfell — mountain pass)
T6 (Hafenvalor) ↔ T1, T3, T7
T7 (Lowenskyst) ↔ T1, T6, T15 (sea route)
T8 (Eidursjo) ↔ T2, T9, T11 (Halvardshelm — lake crossing)
T9 (Varfell) ↔ T2, T5, T8, T10, T12
T10 (Sigurdshelm) ↔ T9, T11
T11 (Halvardshelm) ↔ T8, T10, T12
T12 (Oastad) ↔ T9, T11, T13, T14
T13 (Stillhelm) ↔ T12, T14
T14 (Eisengrund) ↔ T3, T12, T13
T15 (Schoenland) ↔ T4, T7 (sea)

## Faction Starting Control — Reconciled (PP-195)
| Faction | Starting Territories |
|---------|---------------------|
| Crown | T1 (Valorsplatz), T3 (Himmelenger), T5 (Arcansheld, shared Löwenritter), T6 (Hafenvalor), T7 (Lowenskyst), T13 (Stillhelm, nominal) |
| Hafenmark | T2 (Gransol, capital), T4 (Spartfell), T8 (Eidursjo) |
| Varfell | T9 (Varfell, capital), T10 (Sigurdshelm), T11 (Halvardshelm), T12 (Oastad) |
| Restoration | T14 (Eisengrund, informal) |
| Church | No starting territorial control. Church has cathedral presence in T3 (Himmelenger) and Favour in all major cities. |
| Guilds (NPC) | No territorial control. Commercial presence in T11 (Halvardshelm), T8 (Eidursjo), T6 (Hafenvalor port). |
| Niflhel (NPC) | No territorial control. Network presence in T10 (Sigurdshelm), T1 (Valorsplatz), T6 (Hafenvalor). |
| Löwenritter | T5 (Arcansheld, shared with Crown pre-coup). |

## Faction Capital Territories — Corrected (PP-195)
| Faction | Capital | Territory | Notes |
|---------|---------|-----------|-------|
| Crown | Valorsplatz | T1 | Kingdom capital |
| Church | Himmelenger | T3 | Grand Cathedral — institutional HQ, Crown territory |
| Hafenmark | Gransol | T2 | CORRECTED from T6 (Hafenvalor). Hafenvalor is Crown territory. |
| Varfell | Varfell | T9 | Duchy capital |
| Löwenritter | Arcansheld | T5 | Fortress |
| Restoration | None | — | Network faction |

## Guilds — Canonical Identity (PP-195)
Guilds = commercial network, NOT a territorial faction. They operate in all cities per canonical source.
Ministry of Guilds monitors their membership lists, arranges contracts, sets taxation.
**In BG:** Guilds maintain Commercial Presence (CP-tokens, distinct from Ministry AP-tokens) in trade cities.
Starting CP-tokens: T1 (Valorsplatz), T2 (Gransol), T6 (Hafenvalor), T9 (Varfell), T11 (Halvardshelm).
CP-tokens generate economic effects without territorial control:
- Territory with CP-token: Trade orders by any faction: +0.5 Wealth at Year-End (round down; Guilds take the remainder as trade tax — Guilds Wealth +0.5/Year-End per CP-token territory).
- CP-token persists until Church Interdict or Ministry of Guilds collapse (Ministry Mandate = 0).

## Niflhel — Canonical Identity (PP-195)
Niflhel = criminal/shadow network. Never territorial. Operates in all cities.
**In BG:** Network Depth tokens (existing mechanic confirmed). No CP-tokens, no territorial control.
Starting Network Depth: T1 (depth 1), T10 (depth 2), T6 (depth 1).
Niflhel's Black Market presence in T10 (Sigurdshelm) generates the Trade +1 Ob special property for that territory — Niflhel's influence depresses legitimate trade even without control.

## Varfell Opening Position — Revised (PP-195)
Varfell starts with 4 territories (T9, T10, T11, T12). Strong starting position territorially.
Mechanical handicap is NOT positional scarcity — Varfell has the most starting territories.
Handicap is defensive: Varfell's territories are surrounded by mountains and Thread Wounds.
- T9 → T5 (Arcansheld): Fort 3 mountain pass. Löwenritter garrison.
- T9 → T2 (Gransol): Hafenmark territory; direct border conflict risk.
- T12/T13/T14: Thread Wound sites; RS cost for occupation.
The fortification constraint (PP-191) is accurate but the framing changes: Varfell has territory but is hemmed in by the mountain range and cannot easily expand outward. Intelligence, not conquest, is the correct path — confirmed by canonical geography.

## Hafenmark Opening Position — Revised (PP-195)
Hafenmark starts with 3 territories (T2, T4, T8). Duchy capital = T2 Gransol.
T4 (Spartfell) = Altonian border — exposed to IP events.
T8 (Eidursjo) = forest/lake terrain, adjacent to Varfell (T9) — eastern exposure.
Hafenmark is flanked: Altonia to the east (T4), Varfell to the west (T8→T9), Crown to the south (T2→T1 corridor).
Parliamentary strategy is correct — Hafenmark cannot win through military expansion; it wins through institutional influence.

## Crown Opening Position — Revised (PP-195)
Crown starts with 6 territories (T1, T3, T5, T6, T7, T13 nominal).
Most territories, but dispersed along the coast and south.
T3 (Himmelenger) is Crown territory but Church has deep institutional presence — Crown cannot use T3 for standard military purposes without Church backlash (Institutional Mandate trigger).
T13 (Stillhelm) is nominal — Crown claims it but exercises no governance (non-Thread orders +1 Ob).
Effective starting territories: T1, T5, T6, T7 = 4 territories with real governance. T3 = contested presence. T13 = unclaimed frontier.

## Territory Cascade Corrections (PP-196)
Following PP-195 territory reassignment, corrections applied:
- Crown Deed 2: T1+T2 → T1+T6 (T2 is now Hafenmark)
- Hafenmark Deed (Path C, Deed 3): T6 → T2 (Gransol is Hafenmark capital)
- TC 80 seizure TC values: Gransol T2 = +3 (duchy capital), Hafenvalor T6 = +1 (Crown port)
- Ministry AP-tokens: removed T2 from starting positions (Crown Ministry only)
- Varfell expansion constraint: T10 corrected (Varfell starting territory, not NPC hostile)
- T12 (Oastad): Varfell starting territory — Thread Wound cost applies but it's already theirs
- Elske contact via T4 (Spartfell): T4 is now Hafenmark. Crown or Löwenritter must operate
  in Hafenmark territory to contact Elske. Ob +1 if Hafenmark has active Standing against Crown.
  Hafenmark player may facilitate or obstruct contact (Senator Outward, Ob 2 to grant access).


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
| 13 | Stillhelm | Crown | 0 | 2 | South coast. Southernmost Access. Non-Thread orders +1 Ob. RS −1/season occupation. Warden Cooperation track. |
| 14 | Himmelenger | Church ★ | 2 | 5 | Cathedral city. Church starts here. TC +1/season Church controls. Church Unique Power −1 Ob. |
| 15 | Askeheim | Uncontrolled | 0 | 1 | The Southernmost. Epicentre. Warden domain. No faction control possible. Expedition required. RS −2/season non-Warden occupation. Forgetting Check mandatory on entry. |
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
T3 (Halvardshelm) ↔ T1, T2, T4, T6
T4 (Vargstad) ↔ T3, T9, T13, T15
T5 (Gransol) ↔ T6, T7, T10
T6 (Eidursjo) ↔ T1, T3, T5, T9, T10
T7 (Spartfell) ↔ T5, T8, T16 (NE mountain pass)
T8 (Lowenskyst) ↔ T7, T12, T16 (sea)
T9 (Arcansheld) ↔ T4, T6, T10, T11, T13
T10 (Nordhelm) ↔ T5, T6, T9, T11
T11 (Mittelmark) ↔ T9, T10, T12, T14
T12 (Valorsplatz) ↔ T8, T11, T13, T14, T16 (sea)
T13 (Stillhelm) ↔ T4, T9, T12, T15
T14 (Himmelenger) ↔ T11, T12, T13
T15 (Askeheim) ↔ T4, T13 (expedition access only)
T16 (Schoenland) ↔ T7 (NE pass), T8 (sea), T12 (sea)

## Road Network — Definitive (PP-199)

### Primary Roads
| Road | Route | Notes |
|------|-------|-------|
| King's Road | T12 → T11 → T9 → T13 | Crown central arterial. Löwenritter patrol. |
| Coastal Road North | T12 → T8 → T7 | East coast. Northern trade route. |
| Coastal Road South | T12 → T14 → T13 | South coast. Church Inquisitor route. |
| Midland Road | T9 → T10 → T5 | Crown into Hafenmark. Most contested road. |
| Lake Road | T5 → T6 → T1 | Circles lake. Hafenmark-Varfell trade. |

### Secondary Roads
| Road | Route | Notes |
|------|-------|-------|
| Western Valley | T1 → T3 → T2 | Varfell internal. Remote. |
| Southern Duchy | T1 → T3 → T4 | Varfell capital connection. Thread zone. |
| Fortress Road | T9 → T4 | Löwenritter direct south. Crown can threaten Vargstad. |
| Hill Track | T10 → T11 | Crown administrative. |
| Pilgrims' Road | T11 → T14 | Crown to Cathedral. Church Inquisitor route. Ministry records movement. |
| Warden Track | T13 → T15 | Expedition only. Non-Thread +1 Ob throughout. |

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
| 1 (Inner) | T13 (Stillhelm) | RS −1/season any occupation. Warden Cooperation track. |
| Epicentre | T15 (Askeheim) | RS −2/season non-Warden. Expedition required. |

## TC 80 Seizure — Territory Values (PP-199)
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
Varfell Path B Deed 1: control T4 (Vargstad) + T13 (Stillhelm) simultaneously.
Varfell Path C Deed 2: control T4 + T13 + ≥ 1 other.
Elske contact: via T7 (Spartfell, Hafenmark). Hafenmark may facilitate or obstruct.

## Ministry AP-Token Starting Positions (PP-199)
T9 (Arcansheld), T10 (Nordhelm), T11 (Mittelmark), T12 (Valorsplatz — primary Parliament seat).

## Guilds CP-Token Starting Positions (PP-199)
T3 (Halvardshelm), T5 (Gransol), T8 (Lowenskyst), T12 (Valorsplatz), T14 (Himmelenger).

## Niflhel Network Starting Depth (PP-199)
T2 (Sigurdshelm) depth 2. T12 (Valorsplatz) depth 1. T14 (Himmelenger) depth 1.
