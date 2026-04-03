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

CORRECTIONS (PP-191): Varfell Mandate 4, Wealth 4 (user decision — G-10 was wrong to confirm 3/3). Varfell's mechanical handicap is territorial positioning: all territories adjacent to Varfell's starting position are fortified, making early expansion costly. TC = 28 (P-32). TC victory = 65 (P-32).

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
| Hafenvalor (T6, duchy capital) | +3 |
| Lowenskyst (T7) | +1 |
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
- T10 (Sigurdshalm): Niflhel NPC territory. Trade +1 Ob. No military presence but diplomatically hostile.
- T12/T13: Uncontrolled Thread Wound sites. RS −1/season if occupied. Accessible only with VTM ≥ 2.

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
