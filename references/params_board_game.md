<!-- version: v0.9.1 | source: valoria_bg_v05_simulation_and_patches.md + victory_architecture_v1.md + calamity_radiation.md + geography_design.md (canonical per canonical_sources.yaml) | last_updated: 2026-04-06 -->
<!-- PP-249 2026-04-04: ED-142 resolved — BG Overwhelming: 2×Ob + floor 3, supersedes ED-031 -->
<!-- PATCHES APPLIED: PP-169-PP-187 | CORRECTIONS: PP-188 | PP-189 (v05 final) | PP-190–201 (BG balance, territory table, road network, map v2) | PP-219 (Southernmost access redesign) | PP-220 (Champion TS table) -->
<!-- AUTHORITATIVE SOURCE: designs/board_game/valoria_bg_v05_simulation_and_patches.md (faction stats, clocks, victory conditions); designs/board_game/stage_bg_proposal_v02.md (action economy, card-hand system PP-177) -->
<!-- NOTE: v05 is canonical for BG mechanics. v04 B-sections remain structural base. -->
<!-- STALE CHECK: v0.9.0 — RS Effects, Victory, CV/WC/WA, TC generation updated. Territory renumbering complete: all T# references use geography_design.md canonical numbering (17 territories). Old territory names (Vargstad, Eidursjo, Arcansheld, Nordhelm, Mittelmark) replaced with canonical names (Grauwald, Rendstad, Ehrenfeld, Kronmark, Feldmark). Ducal Geography (ED-107) resolved. Varfell expansion rewritten. -->

# params_board_game.md — Board Game Mode (v0.7.0)

## FACTION ASSIGNMENT (canonical, v04 B1)

### Playable Factions
| Faction | Player Count |
|---------|-------------|
| Crown | 2–5 players |
| Church of Solmund | 2–5 players |
| Hafenmark | 2–5 players |
| Varfell | 2–5 players |
| Restoration Movement | 5 players only (optional) — statless faction; operates through CV and Presence only |
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
| Torben Loyalty | **3** | 0–7 | Active from game start. No IP trigger. On Crown elimination: Torben Loyalty track transfers to Löwenritter (they inherit the succession claim). Löwenritter wins or loses Torben via Influence actions the same way Crown did. Church and Hafenmark may contest via Senator Outward Diplomacy (Ob = current Torben Loyalty ÷ 2). (ED-332, PP-498: start 3, range 0–7 per §Torben Loyalty Track canonical.) |
| Elske Loyalty | 4 | 0–7 | Off-board card near T4. |
| Löwenritter Coup Counter | 0 | 0–4 | Public. Threshold 4 = coup eligible. |
| Warden Cooperation | 0 | 0–3 | Near T6. Inactive until Warden Emergence. |

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
| Restoration Movement | — | — | — | — | — | No faction stats. Operates via Presence markers and Community Weaving only. (PP-460) |
| Löwenritter (post-coup) | 3 | 2 | 3 | 6 | 5 |
| Guilds (NPC) | 3 | 4 | 6 | 2 | 5 |
| Niflhel (NPC) | — | 5 | 4 | — | 4 |

CORRECTIONS (PP-191/PP-195): Varfell Mandate 4, Wealth 4. Varfell starts with 4 territories (T4/T11/T12/T13). Handicap is defensive: mountain range + Thread Wounds hem in expansion. Handicap is defensive: mountain range + Thread Wounds hem in expansion. Intelligence path is correct. Fortification constraint (PP-191) applies to outward expansion, not inward security. TC = 28 (P-32). TC phase transition = 75 (per victory_architecture_v1.md §7).


## Faction Elimination — Territory Status (ED-333 resolved)
When a faction is eliminated (Stability 0 and no recovery action taken):
- All territories previously held enter **Political Vacuum** for 1 season (PP-500). During Vacuum: no faction may March in; Fort level retained; tokens removed. After 1 season: Vacuum lifts, territories become Uncontrolled, normal March rules apply.
- Uncontrolled territories: any faction may March in freely (no Battle roll for entry, no defender).
- Fort level is retained on the territory card (physical fortifications don't vanish).
- Ministry AP-tokens and Guilds CP-tokens in eliminated faction territories are removed immediately.
- Löwenritter Coup Counter: if Crown is eliminated, Löwenritter Coup Counter sets to 4 (coup fires next season per existing rule — PP-194).
- TC, IP, RS effects tied to eliminated faction's territory holdings: cease immediately (e.g. T9 TC +1/season bonus stops if Church is eliminated and loses T9 control).


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
| Muster (Legionary Inward) | 2 | −1 T12 garrison |
| March (Legionary Outward) | No roll | Contested entry = Battle |
| Govern (Consul Inward) | Prosperity ÷ 2 (round up, min 1) | −1 own capital |
| Trade (Consul Outward) | Prosperity ÷ 3 (round up, min 1) | +1 IP≥30; +1 T2 |
| Diplomacy vs NPC (Senator Outward) | NPC Stability ÷ 2 (round up) | — |
| Diplomacy between players | Negotiated | Not a roll |
| Formal Crown Treaty (Senator Outward) | Target faction's Mandate | Crown only. Both factions must agree. See victory_architecture_v1.md §3.1. |
| Thread Operation (Pontifex/Weaver) | Ob 2 base | See PP-182 co-movement protocol |
| Investigate/Intel (Tribune) | 2 | +2 Ob in Church territory with Inquisitor |
| Spy (Tribune Outward) | Target Intel ÷ 2 round up | — |
| Parliamentary Manoeuvre (Hafenmark) | Opponent Influence ÷ 2 round up | — |
| Community Organising (Restoration) | 2 | Pool: 1D base + 1D per adjacent territory with RM Presence marker. Failure: no Stability cost (RM has no Stability). Try again next season. (PP-460) |
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
4b. **Church Prominence update (ED-326):** Church player marks Prominent territories on faction mat — any territory where Church global Mandate exceeds that territory's controlling faction's global Mandate. Updated every Accounting. Used for: Counter-Narrative target eligibility, Seizure Ob formula, Piety Spread.
5. Church Attention Pool: resolve threshold responses. Pool resets to 0.
6. Thread Debt: tokens >1 season old: RS −1/token. Serviced tokens: no drain; permanent residual RS −0.5 recorded.
7. Clear Thread Resonance markers (all factions reset).
8. Check threshold events: draw one Event Card per threshold crossed.
8b. Milestone Bonus check.
9. Warden Emergence check.
9b. Vaynard-Edeyja same-season rule: if Warden Emergence at Step 9 AND VTM ≥ 4 AND Varfell played Tribune Inward in T6: Warden Cooperation +1 immediately.
10. Warden Cooperation check.
10b. Torben/Elske Loyalty events: apply Loyalty changes.
11. [DISSOLVED — Hollow Victory totals no longer tracked. Step retained for numbering continuity.]
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
[Superseded — Hafenmark capital = Gransol (T8). See Territory Table.]

## Clock Environmental Effects (v04 B2)

### Rendering Stability (RS) Effects
**Canonical source: `designs/setting/calamity_radiation.md`** (Simplified BG Lookup Table).

RS effects are geographically graduated by Proximity Rating (node distance from Askeheim T15), not applied globally.
Each territory card includes a Proximity Rating (0–5). At Accounting, one lookup per territory: current RS band × Proximity Rating.

| RS Band | Proximity 0 | Proximity 1 | Proximity 2 | Proximity 3 | Proximity 4–5 |
|---|---|---|---|---|---|
| 100–80 | Wound contained; Forgetting active; no radiation | — | — | — | — |
| 79–60 | +1 Ob non-Thread; Forgetting active | Folklore (no mech) | — | — | — |
| 59–40 | +2 Ob non-Thread; Shifting Objects | +1 Ob Thread; Shifting Objects (1d10: 1–2) | Folklore (no mech) | — | — |
| 39–20 | Gaps auto; beings present | +1 Ob all; Gaps (1d10: 1–2) | +1 Ob Thread; Shifting Objects (1d10: 1) | Folklore (no mech) | — |
| 19–1 | +2 Ob Mending; beings; Gaps (1d3) | +1 Ob all; Gaps (1d10: 1–4) | +1 Ob Thread; Gaps (1d10: 1–2) | Shifting Objects (1d10: 1) | Folklore (no mech) |

Additional global RS effects at Critical (19–1): all Thread operations +1 Ob worldwide; seasonal Stability checks for all factions at Ob 1 (failure: Mandate −1).
RS 0 = Rupture (campaign ends, all factions lose).

Southernmost Surge (one-time, RS ≤ 10): all territories within Proximity 2 of Askeheim experience effects one band worse for one season. See calamity_radiation.md.




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

## Victory Conditions — Pointer
**Canonical source: `designs/board_game/victory_architecture_v1.md`** (all victory conditions, co-victory pairings, shared loss conditions).

The Deed-based victory system has been dissolved for ALL factions including Löwenritter (PP-427). Victory = Territory Consolidation Value (TCV) thresholds + faction-specific political conditions, sustained for 2 consecutive Accounting steps.

### Summary (see victory_architecture_v1.md §3 for full conditions)

| Faction | Primary Victory | Key Thresholds |
|---------|----------------|----------------|
| Crown | Peninsula Sovereignty | TCV ≥ 16 + suppress all rivals + Invasion Pressure (IP) < 60 + Parliament Integrity (PI) ≥ 3 |
| Church of Solmund | Solmundan Orthodoxy | TCV ≥ 8 + CV ≥ 3 all held territories. Graduated Seizure: Pool = Influence + floor(TC/15), Ob = 7 − CV (PP-494) |
| Hafenmark | Parliamentary Sovereignty | TCV ≥ 12 + Mandate ≥ 4 + PI ≥ 5 + Crown Mandate ≤ 3 |
| Varfell Path A | Intelligence Hegemony | TCV ≥ 10 + Vaynard Thread Mastery (VTM) ≥ 3 + 2 rival stats revealed + expansion |
| Varfell Path B | Southernmost Dominion | TCV ≥ 8 + VTM ≥ 3 + T13 control + T15 presence + Warden's Accord (WA) ≥ +1 |
| Varfell Path C | Thread Supremacy | TCV ≥ 10 + VTM = 5 + Rendering Stability (RS) ≥ 50 |
| Restoration Movement (RM) | Cultural Revolution (Hybrid only, post-Founding) | Phase 1: CV ≤ 1 in ≥ 8/15 territories. Phase 2: Cultural Uprising of T9 Himmelenger. Win: T9 held + Phase 1 × 2 Accounting. No faction stats. (PP-460, PP-478) |
| Löwenritter | Regency Establishment | TCV ≥ 10 + Thread Consciousness (TC) < 50 + IP < 60 + RS > 40 + PI ≥ 4 + successor |

### Territory Consolidation Values (TCV)
Per victory_architecture_v1.md §1. Total TCV = 30 (T16 Schoenland not in territorial play, T15 Askeheim TCV = 0).

| T# | Territory | TCV | Starting Controller |
|----|-----------|-----|---------------------|
| T1 | Valorsplatz | 5 | Crown |
| T8 | Gransol | 4 | Hafenmark |
| T9 | Himmelenger | 3 | Church of Solmund |
| T12 | Sigurdshelm | 3 | Varfell |
| T3 | Lowenskyst | 2 | Crown |
| T10 | Spartfell | 2 | Hafenmark |
| T14 | Ehrenfeld | 2 | Crown |
| T2 | Kronmark | 1 | Crown |
| T4 | Grauwald | 1 | Varfell |
| T5 | Feldmark | 1 | Crown |
| T6 | Stillhelm | 1 | Crown |
| T7 | Rendstad | 1 | Hafenmark |
| T11 | Halvardshelm | 1 | Varfell |
| T13 | Oastad | 1 | Varfell |
| T17 | Halvarshelm | 1 | Hafenmark |

Starting TCV: Crown 12, Hafenmark 8, Varfell 6, Church of Solmund 3.

### Co-Victory Pairings
Per victory_architecture_v1.md §4. All require 2 consecutive Accounting steps except Church+Hafenmark Partition (immediate on mutual agreement).

| Pair | Key Conditions |
|------|---------------|
| Crown + Hafenmark | Crown TCV ≥ 12, Hafenmark TCV ≥ 8, PI ≥ 5, TC < 50 |
| Crown + Varfell | Crown TCV ≥ 12, Varfell TCV ≥ 8, VTM ≥ 3, RS ≥ 50 |
| Varfell + RM | VTM ≥ 4, WA ≥ +2, ≥ 4 territories CV ≤ 1, RS ≥ 40 |
| Hafenmark + RM | Hafenmark TCV ≥ 10, ≥ 4 territories CV ≤ 2, PI ≥ 4, RS ≥ 40 |
| Löwenritter + Hafenmark | Löwenritter TCV ≥ 8, Hafenmark TCV ≥ 8, PI ≥ 4 |
| Church + Hafenmark (Partition) | Crown Mandate ≤ 1, TC ≥ 50, Church ≥ 2 territories, Hafenmark ≥ 3, no military conflict |

Incompatible: Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM.

### Shared Loss Conditions
Per victory_architecture_v1.md §5. RS = 0 (Rupture), IP ≥ 100 + Altonian External Relationship (AER) ≤ 1 (Altonian Conquest), or all factions Stability 0 (Total Institutional Collapse).

### Hollow Victory — DISSOLVED
The Hollow Victory modifier system (Deed-count penalties) has been dissolved with the Deed system (PP-427). In Hybrid mode, BG victory without personal arc resolution is a narrative qualifier per P-32 (see victory_architecture_v1.md §9.3).

### Public Instability (PI) Thresholds (PP-501, ED-361 resolved)
PI measures popular dissatisfaction with monarchical governance. Higher PI benefits Hafenmark (PI ≥ 5 required for their victory). PI hurts Crown.

| PI Range | Effect |
|----------|--------|
| 0–4 | Stable. No mechanical effect. |
| 5–9 | Tensions. Crown Domain Actions +1 Ob in territories with PI markers. Hafenmark Parliamentary Manoeuvre −1 Ob. |
| 10–14 | Unrest. Crown Stability check Ob +1 at Accounting. Popular demonstrations — flavour. |
| 15–19 | Revolt. Crown loses 1 territory per season (lowest TCV, becomes Uncontrolled after 1-season Political Vacuum per PP-500). Löwenritter coup check if Coup Counter ≥ 2. |
| 20+ | Collapse. Crown elimination at next Accounting unless PI reduced below 20 before then. |

PI advances per existing IP/PI interaction rules. PI markers placed in territories where relevant events fire.
[EDITORIAL: ED-361 — resolved provisionally. Thresholds designed so PI 5 (Hafenmark victory condition) is achievable without triggering Crown crisis. PI 15+ is catastrophic for Crown. Flagged for simulation.]

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

[STRUCK — Deed system dissolved PP-424. Torben Loyalty conditions now per victory_architecture_v1.md §3.6 Löwenritter.]
Altonian Tutoring Demand triggers at IP ≥ **40** (v04 B2: "Torben Tutoring Demand (IP ≥ 40 Event)") (not 30 — v04 B2: "Torben Tutoring Demand (IP ≥ 40 Event)").

## Elske Off-Board Card (v04 B2)
Princess Elske Almqvist is in Altonia (not on the board). Married to Doux Alexios Laskaris, province borders T4.
Elske Loyalty: 0–7, starts 4. Tracked on off-board card near T4.

Contact: Crown or Löwenritter Senator Outward in T4 (Ob 2 at IP < 60; Ob 3 at IP ≥ 60).
Return: Elske Loyalty ≥ 6 + IP < 60 + Crown/Löwenritter unit in T4: Military vs Ob 2. IP +5 on success.

## TC Generation — Seasonal (per victory_architecture_v1.md §7)
**Starting TC: 28. Phase transition at TC 75 (TC freezes — Church shifts to territorial seizure).**

Seasonal TC at Accounting (execute in order):
1. **Institutional Momentum:** TC +1 (passive).
2. **Conviction Yield:** for each territory where Church is prominent (Church Mandate > controlling faction's Mandate), add based on CV. CV 5 = +1, CV 4 = +0.5, others = 0. Total = floor(sum).
3. **Assert** (optional Church action): Influence vs Ob 2. Success: TC +1. Failure: Stability −1.
4. **Suppress** (optional opponent action): Mandate vs Ob = Church Mandate. Success: negate Step 1 passive. Failure: Stability −1.
5. **Hafenmark Structural Suppression:** while Baralta Mandate ≥ 4, TC −1/season.

**TC seasonal cap (PP-504):** ±3 per season from player-initiated Domain Actions. ±5 per season from all sources combined (includes Institutional Momentum, Conviction Yield, Calamity Drift, event cards).

Legacy TC sources (AER momentum, Attention Pool threshold, Emergency Powers, Free Trade Decree, Church unit presence) are subsumed into the Conviction Yield system — Church prominence in high-CV territories captures the same dynamics. AER ≥ 3 still bypasses Hafenmark structural suppression (PP-203).

## TC 75 Territorial Seizure (PP-421 — per victory_architecture_v1.md §7)
**Post-TC 75: TC freezes. Church shifts to territorial seizure campaign.**

### Seizure Ob
Ob = 2 + Fort Level + max(0, 3 − CV).
Prominence required: Church Mandate > controlling faction's Mandate in target territory.
Church Mandate ≥ 4 required to attempt seizure.

### Seizure Results
Per victory_architecture_v1.md §7. Overwhelming seizure: CV +1 in target territory (counts against ±1 CV seasonal cap).

### Seizure Constraints
One seizure attempt per season. Cannot target T15 (Askeheim) or T16 (Schoenland).

### Church Graduated Seizure (PP-494)
**Pool:** Influence + floor(TC / 15). At TC 28: 7D. At TC 75: 11D.
**Ob:** 7 − CV (target territory Conviction value). CV 5 = Ob 2. CV 0 = Ob 7.
**Prerequisites:** Church Mandate ≥ 4. Prominence (Church Mandate > controlling faction Mandate).
**Overwhelming:** CV +1 in target territory (consequence, not cap-governed).
**Failure:** Stability −1.
**Political cost:** Seizure attempt grants controlling faction Casus Belli vs Church.
[EDITORIAL: ED-355 — Fort Level interaction. See victory_architecture_v1.md §3.2.]

### Battle Ob Formula (PP-499, ED-343 resolved)
**Battle Ob = defender Military ÷ 2 (round up, min 1).**
Attacker rolls: Military pool vs Ob. Degree table per standard BG degree table (PP-249).
[EDITORIAL: ED-343 — resolved provisionally. Defender Military ÷ 2 matches other Domain Action Ob patterns. Min 1 prevents auto-success vs Military 0 factions (RM). Flagged for simulation confirmation.]



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
Crown = Legionary | Church = Senator | Hafenmark = Consul/Prefect | Varfell = Tribune | Restoration = Pontifex (Thread) only. RM hand: 2× Praetor (Community Organising/Project), 1× Pontifex (Community Weaving + Cultural Uprising), 1× Recess. No Legionary, no Senator (for stats-based actions), no Tribune. (PP-460)

## Mandate Recovery (PP-174 — provisional, no v04 basis but not contradicted)
Govern Overwhelming in own capital: Mandate +1 (max once/season, max to faction starting Mandate).

## Trade Network Investment — Hafenmark Wealth Sink (PP-178)
Consul Inward, 2 Wealth cost. Ob 2. Places Trade Route tokens for +1D Trade bonuses.
Success: Trade Route token placed (+1D Trade this territory this season). Token persists until control transfer.
Overwhelming: As above + token links adjacent territory + Guild Favour +1 in non-capital territory.
Partial: Token placed, no bonus. Persists.
Failure: No token, Stability −1.

## BG Co-Movement Resolution Protocol (PP-182, ED-086 resolved 2026-04-03 — P-14 compliant)

**Serialization (PP-503):** When multiple Thread operations fire in the same season, resolve each operation's Co-Movement card fully (draw → apply all three dimensional effects → discard) before the next operation draws. Effects from earlier cards may alter conditions for later draws (e.g., RS threshold crossings).
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
Per-territory ceiling: 10. **First Inquisitor at AP ≥ 3. Second Inquisitor at AP ≥ 6.** Max 2 Inquisitors/territory. (ED-322 confirmed 2026-04-08.)
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


## Warden Cooperation Track (WC)
**Canonical source: `designs/board_game/victory_architecture_v1.md` §6**

Range: 0–3. Starts at 0.

| WC Level | Effect |
|----------|--------|
| ≥ 1 | +1D to all Thread operations peninsula-wide |
| ≥ 2 | RS decay rate halved |
| ≥ 3 | RS +2/season at Accounting |

WC advances via successful Southernmost Expedition and Warden engagement actions. Multiple victory conditions require RS thresholds; WC is the primary tool to arrest RS decline.

## Warden's Accord (WA)
**Canonical source: `designs/board_game/victory_architecture_v1.md` §8**

Range: −3 to +3. Starts at 0.

RM Emergence triple condition: WA ≤ −2 AND ≥ 3 territories CV ≤ 1 AND RS ≤ 50. One-shot.
RM Suppression: WA ≥ 0 OR all territories CV ≥ 2 OR RM Stability 0.
Varfell Path B blocked if RM has emerged (WA ≤ −2).

See victory_architecture_v1.md §8 for WA movement rules and full RM stat block.

## Institutional Mandate Uphold/Appease (PP-189 — v05 names this "Appease" not "Compromise")
Each faction has a printed Institutional Mandate. When event challenges it:
- **Uphold** (before roll): Roll proceeds normally. No cost.
- **Appease** (before roll): Triggering action cancelled entirely — no roll made. Mandate −1.
**Trigger scope (ED-324 resolved 2026-04-08):** Fires when a Domain Action directly targets the faction's Mandate stat OR their unique clock/track — TC for Church, PI for Hafenmark, VTM for Varfell. Stability, Influence, Wealth, Military do not trigger. Deterministic — no GM discretion.
NPC rule: NPC factions Appease if Mandate ≥ 4 AND Stability ≤ 3.
Note: Prior params used "Compromise" — v05 PP-189 establishes "Appease" as the canonical term.

## Hollow Victory Mechanics — DISSOLVED (PP-427)
Deed system and Hollow Victory modifiers dissolved. See victory_architecture_v1.md §9.3 for Hybrid mode narrative qualifier (P-32).

## Intel Advancement Counter (PP-180 revised)
Intel Advancement Counter (0–3) on faction mat.
Each season with ≥1 successful Intel or Quiet Network order: Counter +1.
At Counter 4: Intel stat +1 (max 7); Counter resets to 0.
Note: Intel stat advancement is valid for NPC factions (Niflhel). Varfell victory paths do NOT require Intel stat advancement — they use VTM and territorial control.

## Accounting Phase Reference (PP-180 + v04 B4)
13-step sequence. See Phase 5 section above.


## Command Event — Captured or Killed General (ED-334 + ED-335 resolved)
When a named PC General is captured or killed during a Zoom In personal scene (Hybrid) or TTRPG mass combat:

**Immediate BG consequence (fires at Zoom Out / next Accounting):**
- Captured general's faction: Legionary card unavailable for **1 season** (no Muster or March orders — the command structure is disrupted).
- Capturing/killing faction: **Influence +1** (political leverage or military prestige).
- Captured general's faction: **Mandate −1** at next Accounting (morale blow — general lost).

**Ransom:** Capturing faction may offer ransom. Base: **2 Wealth** per named general. Both factions must agree. Ransom paid → general returns next season, Legionary card restored.

**Rescue:** Tribune Investigate (Ob 4 in secure enemy territory) to locate, then a Zoom In rescue scene. Success returns general; Failure may result in execution (Mandate −2 instead of −1).

**NPC-initiated kills only:** When an NPC kills a PC General (not captured), the Influence +1 and Mandate −1 still apply. No ransom is possible. The general is dead; the faction loses their named commander permanently (all Command bonuses from that general cease).

**Does not trigger a Domain Echo** (this is an Accounting consequence, not a Domain Echo — Domain Echoes apply to PC-initiated Domain Actions only).

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
Varfell seat T12 (Sigurdshelm) is adjacent to: T4 (Grauwald, Varfell), T11 (Halvardshelm, Varfell), T13 (Oastad, Varfell).

All four Varfell starting territories form a chain along the western fjords. Expansion paths:
- From T4 (Grauwald): adjacent to T7 (Rendstad, Hafenmark), T12 (Varfell), T14 (Ehrenfeld, Crown Fort 3). T14 is the strongest fortress on the board — Löwenritter garrison, Fort 3 (max 4).
- From T11 (Halvardshelm): adjacent to T10 (Spartfell, Hafenmark Fort 2), T12 (Varfell). Spartfell is fortified.
- From T13 (Oastad): adjacent to T6 (Stillhelm, Crown), T12 (Varfell), T15 (Askeheim, uncontrolled). T6 is the Southernmost Access point. T15 cannot be controlled.
- From T12 (Sigurdshelm): only adjacent to other Varfell territories — no outward expansion.

Every viable expansion runs into fortified or hostile positions. Varfell must either neutralise fortifications (Tribune Sabotage, Ob = Fort level) or accept unfavourable odds.

**Fortification Combat Rule:** When attacking a fortified territory, defending faction adds Fort level as bonus dice to defensive Military roll. Fort 3 (Ehrenfeld) = defender rolls Military + 3D.

**Varfell Intelligence Path:** Varfell's dominant early game is information, not territory. The Intelligence Hegemony victory path requires TCV ≥ 10 + VTM ≥ 3 + 2 rival stats revealed. Path B (Southernmost Dominion) and Path C (Thread Supremacy) both run through T13 (Oastad)/T15 (Askeheim).

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
One AP-token per territory in which Ministry has clerks active. Starts with AP-tokens in T14 (Ehrenfeld), T2 (Kronmark), T5 (Feldmark), T1 (Valorsplatz). These represent the administrative apparatus of Parliamentary governance. (PP-204 corrected.)

### Parliament Connection — Direct Mechanics
Ministry is the mechanical engine behind Parliament Integrity (PI).

**Ministry Stabilisation (fires at Accounting Step 11, before Hollow Victory totals):**
Each season Ministry has an AP-token in T1 (Valorsplatz, Parliament seat): PI degradation from Crown Emergency Powers is reduced by 1 (to a minimum of −0 — i.e. Ministry can prevent one Emergency Powers PI loss per season). This represents clerks managing the parliamentary record and maintaining continuity despite political disruption.

**Ministry Legislative Record:**
At each Year-End Accounting: Ministry produces a Legislative Record for the prior year. Any Parliamentary Manoeuvre that succeeded (Hafenmark) this year is recorded as a Parliamentary Ruling. Effect: the first time each year a Parliamentary Ruling is recorded, PI +1 (the institution acknowledges the precedent). This is in addition to the standard Hafenmark Parliamentary Manoeuvre PI recovery.

**Ministry and Crown Policy:**
Crown Policy Instruments require Ministry countersignature. If Ministry Mandate < 2 (collapsed or compromised): Crown Policy actions cost +1 Ob (the administrative apparatus is too compromised to implement the decree cleanly). If Ministry Mandate = 0: Crown Policy actions unavailable until Ministry Mandate recovers.

**Ministry and Church Seizure (TC 75):**
Church Territorial Seizure of T1 (Valorsplatz) requires removing the Ministry AP-token first. If AP-token present: seizure Ob +1 (the administrative apparatus resists institutional capture). If seizure succeeds despite the token: Ministry AP-token in T13 is removed. All Crown Policy actions are now +1 Ob until Ministry reestablishes presence in T13 (requires 1 season of Ministry NPC action in T13).

**Ministry and Hafenmark:**
Hafenmark's Parliamentary Manoeuvre benefits from Ministry presence. If Ministry has AP-token in T13: Hafenmark Parliamentary Manoeuvre Ob −1 (the clerks facilitate process). If Ministry AP-token absent from T13: Parliamentary Manoeuvre Ob +1 (no procedural infrastructure to execute the manoeuvre).

**Ministry and Löwenritter Coup:**
If Löwenritter Coup fires: Ministry AP-tokens in T13 and T12 are removed immediately. Ministry Mandate −2. PI −3 (standard coup effect) but Ministry Stabilisation does not fire next season (Ministry is recalibrating). Ministry attempts to re-establish AP-tokens in recouped territories at rate of 1/season.

### Ministry NPC AI Priority Tree (runs at Phase 4, Priority 4 — Domain Actions tier)
| Priority | Condition | Action |
|----------|-----------|--------|
| 1 | PI ≤ 3 | Ministry plays Consul Inward (Govern) in T13: roll Ministry Mandate (3D) vs Ob 1. Success: PI +1 (clerks shore up parliamentary function). |
| 2 | T13 has no Ministry AP-token | Ministry plays Consul Inward in T13: roll Mandate 3D vs Ob 1. Success: AP-token placed in T13. |
| 3 | Any territory with AP-token has PI loss pending from Church Seizure | Ministry plays Senator Outward (Diplomacy) vs Church: Mandate 3D vs Church Mandate. Success: Church seizure of that territory delayed 1 season (Ministry files formal procedural objection). |
| 4 | Crown Mandate ≥ 4 AND PI < 5 | Ministry plays Senator Inward (Decree support): PI +1 (Ministry facilitates Crown constitutional governance). Requires Crown Mandate ≥ 4 — Ministry does not support a weakened Crown. |
| 5 (default) | None of above | Ministry plays Consul Inward in highest-Prosperity uncontested territory with AP-token: Prosperity maintained. |

### Ministry Compromise and Corruption
Factions may attempt to corrupt Ministry via Diplomacy.

**Corrupt Ministry (Consul Outward, any faction, Ob = Ministry Mandate ÷ 2 round up, min 2):**
Success: Ministry NPC Priority 4 fires in favour of the corrupting faction this season (Ministry supports that faction's Crown Policy or Parliamentary action regardless of current priorities).
Overwhelming: As above + Ministry AP-token in one territory of choice acts as if that territory is the corrupting faction's capital for one season (−1 Ob on all their actions there).
Failure: Ministry notes the attempt. Corrupting faction Stability −1. Ministry sends record to Riskbreakers (Riskbreaker Priority 6 now includes the corrupting faction's territory).

**Ministry Collapse (Mandate 0):** Ministry ceases NPC actions for 2 seasons. All Ministry AP-tokens removed. During collapse: Crown Policy +1 Ob, Parliamentary Manoeuvre +1 Ob, all Hafenmark Deed 3 (Parliamentary Consolidation) checks suspended. Collapse exit: Hafenmark or Crown plays Govern Inward in T13 (Ob 2). Success: Ministry Mandate returns to 1, AP-token placed in T13, collapse ends.

### Ministry and PI Track — Summary
| Ministry State | PI Effect |
|---------------|-----------|
| AP-token in T13, Mandate ≥ 2 | Emergency Powers PI loss −1 (Ministry prevents one loss/season) |
| AP-token in T13, Mandate ≥ 2, Hafenmark Manoeuvre success this year | Additional PI +1 at Year-End (Legislative Record) |
| AP-token absent from T13 | Hafenmark Parliamentary Manoeuvre Ob +1 |
| Ministry Mandate = 0 | Crown Policy unavailable |
| Church seizes T13 with AP-token present | Seizure Ob +1; if seized: AP-token removed, Crown Policy +1 Ob |
| Löwenritter Coup | T13+T12 AP-tokens removed; Ministry Mandate −2; Ministry Stabilisation suspended 1 season |

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
- **Temperance (Scholars):** AER maintenance. While Church controls at least one university city (T9 Himmelenger has a university): AER loss events are reduced by 1/Year-End (Temperance scholars maintain Altonian ecclesiastical relationships through scholarship).


### Cardinal Death — Succession (ED-336 resolved)
When a Cardinal is killed during a Zoom In scene (Hybrid mode):

**Gap period:** The Cardinal's BG mechanic is **suspended** until Year-End Accounting.
- Fortitude: Templar deployment requires Legionary card (no free deployment).
- Justice: Heresy Investigations cannot be issued (no authorising Cardinal).
- Prudence: Tithe income halved (clerks continue but without Cardinal oversight).
- Temperance: AER maintenance suspended (one additional AER loss event may fire this year).

**Succession:** At Year-End Accounting, Holy See appoints a replacement Cardinal. The new Cardinal is anonymous (no named NPC stats — treat as standard Cardinal for mechanical purposes). Full mechanics restored immediately on appointment.

**Player knowledge:** The replacement Cardinal is public (appointment announced). Church player may designate the new Cardinal as Focused (PP-430) the season after appointment.

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
- **Lions' Helm:** Naval arm. (BG: no direct naval territory but relevant to Schoenland sea route — Löwenritter Helm can deny T10 sea access to Schoenland at IP < 75 if Crown requests.)
- **Riskbreakers:** Sub-unit of Löwenritter, NOT independent faction. Operates outside the law to infiltrate cults and criminal organizations. [CORRECTION: Prior design documents treated Riskbreakers as independent NPC. Canonical source places them inside Löwenritter. They remain NPC-controlled but their Priority Tree now links to Löwenritter's coup counter and Crown's Mandate.]
- **Civic Arm:**
  - Knights of the Peace: patrol and enforce law. BG: when Löwenritter is active (any phase), one territory per season has its March Ob −1 (pacified roads).
  - Royal Investigators: counter-espionage and investigation. BG: once per season, Löwenritter may cancel one successful Intel action targeting Crown (Royal Investigators intercept).

**Riskbreaker correction (PP-194):** Riskbreakers are Löwenritter's covert sub-unit. In BG:
- Pre-coup: Riskbreakers fire under Löwenritter NPC AI Priority Tree (not independent).
- Post-coup: Riskbreakers become a Löwenritter player resource — once per season, may execute one Priority Tree action at no card cost.
- Riskbreaker "independence" in prior design documents (acting against Crown) remains mechanically valid — Riskbreakers serve Valoria, not Almud personally, consistent with canonical source.


### Löwenritter — Reconstitution (ED-331 resolved)
**Type:** Senator Inward (Löwenritter only, post-coup). Available only when PI = 0.
Roll: Mandate vs Ob 3. Once per season.

| Degree | Effect |
|--------|--------|
| Overwhelming | PI restored to 2. Parliamentary Manoeuvre re-enabled immediately. |
| Success | PI restored to 1. Parliamentary Manoeuvre re-enabled. |
| Partial | PI = 0 (no change). Stability −1. |
| Failure | PI = 0 (no change). Stability −1. Church Mandate +1 (institutional vacuum benefits Church). |

**Rationale:** Löwenritter as successor authority has the standing to reconstitute parliamentary function. Without Reconstitution, PI = 0 is a permanent lock on Regency primary victory (PI ≥ 4 required). This action creates a credible recovery path without trivialising the coup's consequences.

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

## Ducal Geography — RESOLVED (ED-107)
Canonical geography applied. 17 territories per geography_design.md. See Territory Table below.
All faction starting positions reflect canonical geography. Old v04 map assignments fully superseded.
## Territory Table — Canonical (geography_design.md)
17 territories. Faction ownership per geography_design.md. Fort levels, Prosperity (Pros), and special properties listed.

| T# | Territory | Faction | Fort | Pros | Special |
|----|-----------|---------|------|------|---------|
| T1 | Valorsplatz | Crown ★ | 2 | 6 | Kingdom capital. Parliament seat. Ministry AP-token. Sea connection to T16 (Schoenland). |
| T2 | Kronmark | Crown | 1 | 4 | Crown heartland. Adjacent to T1, T3, T9, T14. |
| T3 | Lowenskyst | Crown | 3 | 3 | Border fortress. Fort max 4. Adjacent to T2, T9, T17. |
| T4 | Grauwald | Varfell | 0 | 3 | Highland timber. Adjacent to T7, T12, T14. Proximity 3 (Calamity Radiation). |
| T5 | Feldmark | Crown | 0 | 5 | Crown breadbasket. +1 Pros/season uncontested. Adjacent to T1, T6, T14. Proximity 2 (Calamity Radiation). |
| T6 | Stillhelm | Crown | 0 | 2 | Southern farmland. Southernmost Access point — Expedition into T15 staged from here. Non-Thread orders +1 Ob (frontier terrain). Proximity 1 (Calamity Radiation). Adjacent to T5, T13, T15. |
| T7 | Rendstad | Hafenmark | 0 | 4 | Timber valley. Adjacent to T4, T8. |
| T8 | Gransol | Hafenmark ★ | 1 | 5 | Hafenmark capital. Garrison: Muster +1D. Adjacent to T7, T9, T10, T17. |
| T9 | Himmelenger | Church ★ | 2 | 5 | Cathedral city. Church starts here. TC +1/season Church controls. Church Unique Power −1 Ob. Adjacent to T2, T3, T8, T14, T17. |
| T10 | Spartfell | Hafenmark | 2 | 3 | Border castle. NE Altonian pass. Invasion Pressure (IP) events fire here first. Adjacent to T8, T11. |
| T11 | Halvardshelm | Varfell | 0 | 5 | Central fjords. Breadbasket +1 Pros/season uncontested. Muster Ob −1. Guilds CP-token. Adjacent to T10, T12. |
| T12 | Sigurdshelm | Varfell ★ | 1 | 3 | Varfell Seat. Niflhel Black Market: Trade +1 Ob, Niflhel Covert −1 Ob. Adjacent to T4, T11, T13. Proximity 2 (Calamity Radiation). |
| T13 | Oastad | Varfell | 0 | 3 | Southern fjords. Einhir ruins: Restoration Weaving −1 Ob. Adjacent to T6, T12, T15. Proximity 1 (Calamity Radiation). |
| T14 | Ehrenfeld | Crown | 3 | 4 | Military hinge. Central fortress. Fort max 4. Löwenritter garrison. Martial Law −1 Ob. Adjacent to T1, T2, T4, T5, T9. Proximity 3 (Calamity Radiation). |
| T15 | Askeheim | Uncontrolled | 0 | 1 | The Southernmost. Epicentre. Warden domain. Not a normal territory — cannot be controlled by any faction. See §Southernmost Access System. Adjacent to T6, T13. Proximity 0 (Calamity Radiation). |
| T16 | Schoenland | Neutral NPC | 1 | 5 | Maritime island. Sea connection to T1 (Valorsplatz). Altonian Trade. IP ≥ 75: Vanguard deploys. Proximity 4 (Calamity Radiation). |
| T17 | Halvarshelm | Hafenmark | 0 | 3 | Northern mines. Adjacent to T3, T8, T9. Proximity 5 (Calamity Radiation). |

★ = faction capital.


## Starting Control — Canonical (geography_design.md)
| Faction | Territories | Count | Starting TCV |
|---------|------------|-------|-------------|
| Crown | T1 Valorsplatz★, T2 Kronmark, T3 Lowenskyst, T5 Feldmark, T6 Stillhelm, T14 Ehrenfeld | 6 | 12 |
| Hafenmark | T7 Rendstad, T8 Gransol★, T10 Spartfell, T17 Halvarshelm | 4 | 8 |
| Varfell | T4 Grauwald, T11 Halvardshelm, T12 Sigurdshelm★, T13 Oastad | 4 | 6 |
| Church of Solmund | T9 Himmelenger★ | 1 | 3 |
| Löwenritter | T14 Ehrenfeld (shared with Crown pre-coup) | shared | — |
| Uncontrolled | T15 Askeheim | — | 0 |
| NPC | T16 Schoenland | — | — |


## Adjacency — Canonical (geography_design.md)
| Territory | Adjacent To |
|-----------|------------|
| T1 Valorsplatz | T2 Kronmark, T5 Feldmark, T14 Ehrenfeld, T16 Schoenland (sea) |
| T2 Kronmark | T1 Valorsplatz, T3 Lowenskyst, T9 Himmelenger, T14 Ehrenfeld |
| T3 Lowenskyst | T2 Kronmark, T9 Himmelenger, T17 Halvarshelm |
| T4 Grauwald | T7 Rendstad, T12 Sigurdshelm, T14 Ehrenfeld |
| T5 Feldmark | T1 Valorsplatz, T6 Stillhelm, T14 Ehrenfeld |
| T6 Stillhelm | T5 Feldmark, T13 Oastad, T15 Askeheim |
| T7 Rendstad | T4 Grauwald, T8 Gransol |
| T8 Gransol | T7 Rendstad, T9 Himmelenger, T10 Spartfell, T17 Halvarshelm |
| T9 Himmelenger | T2 Kronmark, T3 Lowenskyst, T8 Gransol, T14 Ehrenfeld, T17 Halvarshelm |
| T10 Spartfell | T8 Gransol, T11 Halvardshelm |
| T11 Halvardshelm | T10 Spartfell, T12 Sigurdshelm |
| T12 Sigurdshelm | T4 Grauwald, T11 Halvardshelm, T13 Oastad |
| T13 Oastad | T6 Stillhelm, T12 Sigurdshelm, T15 Askeheim |
| T14 Ehrenfeld | T1 Valorsplatz, T2 Kronmark, T4 Grauwald, T5 Feldmark, T9 Himmelenger |
| T15 Askeheim | T6 Stillhelm, T13 Oastad |
| T16 Schoenland | T1 Valorsplatz (sea) |
| T17 Halvarshelm | T3 Lowenskyst, T8 Gransol, T9 Himmelenger |


## Road Network — Canonical (geography_design.md)

### Primary Roads
| Route | Territories |
|-------|------------|
| Crown Corridor | T1 Valorsplatz — T5 Feldmark — T14 Ehrenfeld — T2 Kronmark |
| Northern Arc | T2 Kronmark — T9 Himmelenger — T8 Gransol |
| Eastern Coast | T1 Valorsplatz — T2 Kronmark — T3 Lowenskyst |
| Western Highland | T14 Ehrenfeld — T4 Grauwald — T12 Sigurdshelm |

### Secondary Roads
| Route | Territories |
|-------|------------|
| Southern Approach | T5 Feldmark — T6 Stillhelm — T13 Oastad |
| Fjord Route | T12 Sigurdshelm — T11 Halvardshelm — T10 Spartfell |
| Hafenmark Interior | T8 Gransol — T7 Rendstad — T4 Grauwald |
| Northern Mining | T8 Gransol — T17 Halvarshelm — T3 Lowenskyst |

### Geographic Trade Notes
Sea routes: T1 (Valorsplatz) ↔ T16 (Schoenland). No land connection to Schoenland. No northern circumnavigation.
Hafenmark is fully landlocked — all maritime trade routes through Crown territory (T1 Valorsplatz or T3 Lowenskyst).

### Altonian Mountain Passes
| Pass | Connection | Notes |
|------|-----------|-------|
| NE Pass | T10 (Spartfell) ↔ off-map Altonia | Primary invasion route. IP events fire at T10. Vanguard enters here. |
| NW Pass | T3 (Lowenskyst) ↔ off-map Altonia | Event-only. Not a playable march. Fires at IP ≥ 90. |


## Proximity Ratings (supersedes Southernmost Zones — PP-199)
**Canonical source: `designs/setting/calamity_radiation.md`** (Node Distance Map + Radiation Matrix).

The Southernmost Zones system is superseded by the Proximity Rating system. Each territory's Proximity Rating is its node distance from Askeheim (T15) on the adjacency graph. Printed on each territory card.

| Proximity | Territories |
|-----------|------------|
| 0 | T15 Askeheim |
| 1 | T6 Stillhelm, T13 Oastad |
| 2 | T5 Feldmark, T12 Sigurdshelm |
| 3 | T1 Valorsplatz, T14 Ehrenfeld, T4 Grauwald, T11 Halvardshelm |
| 4 | T2 Kronmark, T16 Schoenland, T9 Himmelenger, T7 Rendstad, T10 Spartfell |
| 5 | T3 Lowenskyst, T8 Gransol, T17 Halvarshelm |

RS effects per Proximity Rating: see §Rendering Stability (RS) Effects above (Simplified BG Lookup Table from calamity_radiation.md).


## Southernmost Access System (PP-219)
### Authority: designs/ttrpg/edeyja_npc.md; Philosophical Foundations P-13

**T6 Stillhelm = normal territory.** Standard military march, territorial control,
Domain Actions all apply. Difficult frontier terrain (+1 Ob non-Thread) and RS drain
from substrate proximity, but no special access gate.

**T15 Askeheim = the Southernmost proper.** Not a normal territory. Cannot be
controlled by any faction through standard mechanics. The Warden presence and the
substrate damage itself make conventional occupation impossible — any military force
that enters encounters Thread operations at TS 75–80 scale. This has never needed
advertising. It has simply never been necessary.

### Expedition Procedure (T6 → T15)
Required sequence to access Askeheim:

1. **Stage in T6 (Stillhelm):** Faction must control T6 AND have a Champion with
   TS ≥ 30 present there for at least 1 full season. Champion must not have been
   used for military orders that season (Expedition requires full attention).

2. **Declare Expedition:** Phase 4, Praetor or Tribune Inward in T6.
   Roll: Champion pool (TS ÷ 10, rounded down, min 1D, max 3D) vs Ob 3.
   Modifiers: Restoration Weaver with Presence in T6: −1 Ob. VTM ≥ 2: −1 Ob.
   Failure: expedition does not depart this season. Try again next season.
   Success/Overwhelming: expedition departs. Move to step 3.

3. **Forgetting Check (on entry into T15):**
   Same pool vs Ob 2. Modifiers same as above.
   | Result | Effect |
   |--------|--------|
   | Failure | Champion enters T15 but retains nothing. No Warden contact. No Cooperation advance. No VTM progress. Champion returns to T6 next season. |
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
- Varfell Path B (T4+T6) refers to control of T6 — a normal territory.
  The deed measures political and strategic presence at the Southernmost threshold,
  not occupation of the epicentre itself.
- Varfell Path C Deed 2 (T4+T6+1 other): same — T6 is the territorial condition.
  T15 is never the territorial condition.
- Warden Cooperation track advances through successful Expedition seasons in T15,
  not through territorial control.

## TC 75 Seizure — Territory Values — SUPERSEDED
**See TCV table in §Victory Conditions above.** Per-territory seizure Ob = 2 + Fort Level + max(0, 3 − CV). Fort levels per geography_design.md territory table.
[TERRITORY-DEBT: RESOLVED 2026-04-08 — PP-493. All T# references verified against geography_design.md.]
## Victory Condition Territory References — SUPERSEDED
**All victory territory references now use TCV from victory_architecture_v1.md §1.**
Territory numbering follows geography_design.md (17-territory canonical map).
Old PP-199 territory references using pre-geography_design numbering are stale.
[TERRITORY-DEBT: RESOLVED 2026-04-08 — PP-493. TCV table, territory detail table, adjacencies, and all named T# references verified against geography_design.md canonical numbering.]
## Ministry AP-Token Starting Positions (PP-203)
T14 (Ehrenfeld), T2 (Kronmark), T5 (Feldmark), T1 (Valorsplatz — primary Parliament seat).

## Guilds CP-Token Starting Positions (PP-203)
T11 (Halvardshelm), T8 (Gransol), T3 (Lowenskyst), T1 (Valorsplatz), T9 (Himmelenger). [PP-199 numbering confirmed — all correct.]

## Niflhel Network Starting Depth (PP-203)
T12 (Sigurdshelm) depth 2. T1 (Valorsplatz) depth 1. T9 (Himmelenger) depth 1. [Confirmed correct numbering.]

## Balance Findings — Status Update
**BAL-04, BAL-05/06, BAL-08, BAL-09 (all P1):** Superseded by victory_architecture_v1.md redesign. Crown victory restructured (TCV ≥ 16 + political conditions, per victory_architecture_v1.md). Church primary restructured (TC 75 phase transition + seizure). Varfell Path B redesigned. TC dynamics recalibrated.
**BAL-10 (P2):** Varfell T13 (now T13 Oastad) dominant opening — still relevant for monitoring under new TCV system.
See victory_architecture_v1.md §10 for Monte Carlo win probability assessment.
[SIM-DEBT: Full faction-AI simulation needed to validate multi-faction interaction under new victory architecture.]
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
Crown territory names (provisional): T2 = **Kronmark** (NW of Arcansheim), T5 = **Sudmarken** (SE border).
[FLAGGED: confirm names before map publication.]

## ED-109 through ED-113 Resolution (PP-278) [FLAGGED FOR DESIGNER REVIEW]
**ED-109 — Crown victory front-loaded:** Remove 1 pre-met deed from Crown starting conditions. Crown starts with 2 of 5 deeds met (not 3). Rebalances opening tempo.
**ED-110 — Church primary victory inaccessible:** Add fallback: if TC reaches 70 and Church holds 2+ territories, Church may declare Ecclesiastical Mandate victory (partial win, shared with one ally). Unblocks solo Church win path.
**ED-111 — Varfell Path B under-gated:** Require VTM ≥ 4 (not 3) to seize T6 via Path B. +1 VTM threshold gate.
**ED-112 — TC lock:** Hafenmark suppression capped at −1/season total (cannot be stacked via multiple actions). Church TC gain from T9 remains +1/season. Net: Church can advance TC by investing elsewhere.
**ED-113 — Varfell T6 opening dominance:** Add Fort 1 to T6 at game start (not Fort 0). Increases seizure Ob from 0-fort to Fort 1 resistance (+1D to defender).
[FLAGGED: all balance adjustments require playtesting confirmation.]

## BG Overwhelming Threshold — Final (PP-281 / PP-299)
Supersedes PP-179 (which incorrectly stated 'matches TTRPG').
BG Overwhelming = Ob+1 surplus (margin ≥ Ob+1 after ties → attacker wins).
BG Overwhelming floor: net ≥ 3 (PP-249 canonical — matches TTRPG PP-232 floor). Supersedes prior net ≥ 2 proposal.
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
T2 = **Kronmark** (NW of Ehrenfeld, buffer territory). T5 = **Sudmarken** (SE border zone).
[FLAGGED: confirm names before map and BG board publication.]


## ED-109–113 Resolution (PP-303) — BG Balance Adjustments [FLAGGED]
**ED-109 Crown front-loaded:** Remove 1 pre-met deed. Crown starts with 2/5 (not 3). Rebalances opening.
**ED-110 Church primary inaccessible:** Fallback: if TC ≥ 70 + Church holds 2+ territories → Ecclesiastical Mandate (partial shared victory).
**ED-111 Varfell Path B under-gated:** Require VTM ≥ 4 (not 3) to seize T6 via Path B.
**ED-112 TC lock:** Hafenmark suppression capped at −1/season total (cannot stack). Church TC from T9 remains +1/season.
**ED-113 Varfell T6 dominance:** Add Fort 1 to T6 at game start (+1D to defender, raising seizure difficulty).
[FLAGGED: all balance adjustments require playtesting confirmation before publication.]


## ED-142 Resolution (PP-322) — BG Overwhelming Threshold [FLAGGED]
BG Overwhelming: net ≥ 2×Ob AND net ≥ 3 (PP-179 canonical + PP-232 floor). ED-031 superseded.
Ob 10 exception: Overwhelming unavailable; Partial requires net ≥ 5.
[FLAGGED: confirm 2×Ob canonical; confirm floor of 3 applies to BG before BG compilation.]

## BG Overwhelming — Final Ruling (PP-262)
[STRUCK — superseded by PP-249: BG Overwhelming = net ≥ 2×Ob AND net ≥ 3.]
Floor: net ≥ 2 (not 3 — TTRPG floor of 3 is personal-scale drama; BG abstraction warrants lower floor).
PP-179 ('matches TTRPG') was a documentation error. ED-031 (Ob+1) is correct.


## Faction Unique Actions — Board Game (PP-428–442, 2026-04-07)
<!-- PATCHES APPLIED: PP-428–442 + PP-431-COR + PP-441-COR -->
<!-- Status: applied -->

### Church — Piety Spread (PP-428)
**Type:** Consul Inward (Church only). **Prerequisite:** AP ≥ 1.
Roll: Mandate vs Ob = controlling faction Mandate ÷ 2 round up + Fort Level, min 1.
Doctrine-aligned territory: −1 Ob.
**Post-TC 75:** Range-limited to adjacent territories only.

| Degree | Effect |
|--------|--------|
| Overwhelming | CV +1 in territory + AP +1 |
| Success | CV +1 in territory |
| Partial | AP +1 |
| Failure | Stability −1 |

---

### Church — Active Inquisition (PP-429)
**Type:** Senator Inward (Church only).
Roll: Mandate vs Ob = territory Stability ÷ 2, min 1.
**First Inquisitor threshold:** AP ≥ 3 (ED-322 confirmed). Second: AP ≥ 6.

| Degree | Effect |
|--------|--------|
| Overwhelming | AP +3 + immediate Inquisitor deployment if at threshold |
| Success | AP +2 |
| Partial | AP +1 |
| Failure | AP −1 + Stability −1 |

**Sustained AP (≥ 8 sustained across Accounting):** Territory Stability −1 at Accounting.

---

### Church — Cardinal Focus (PP-430)
**Timing:** Phase 1 declarative. No cost. Once per season.
Designate one Cardinal as Focused:

| Cardinal | Focus Effect |
|----------|--------------|
| Fortitude | Templar deploys without Legionary card this season |
| Justice | AP threshold for first Inquisitor −1 this season |
| Prudence | Wealth +1 (integer) this season |
| Temperance | AER +1 this season |

**Schism interaction:** Schisming Cardinal ignores Focus. Focus has no effect if the designated Cardinal is in schism this season.

---

### Hafenmark — Parliamentary Challenge (PP-431 + PP-431-COR)
**Type:** Senator Inward (Hafenmark only). **Once per season.**
Roll: Mandate vs Ob 2 (−1 Ob if PI ≥ 5 → Ob 1 minimum).

**PP-431-COR:** In any season Hafenmark plays Parliamentary Challenge, structural TC suppression (Baralta's Mandate ≥ 4 automatic −1/season) does NOT fire. Challenge replaces structural — the replacement triggers on card play regardless of roll outcome.

| Degree | Effect |
|--------|--------|
| Overwhelming | TC −2 + Church must Uphold or Appease |
| Success | TC −1 |
| Partial | Stability −1 |
| Failure | Stability −1 + Church Mandate +1 |

---

### Hafenmark — Parliamentary Session (PP-432)
**Type:** Senator Outward (Hafenmark only). **Once per arc.**
All factions vote (Support / Oppose / Abstain). Ministry vote = Support if AP-token in T1.
Blocking factions generate Resentment tokens per PP-405.

| Outcome | Effect |
|---------|--------|
| Majority Support | PI +1 + Hafenmark Mandate +1 |
| Majority Oppose | Hafenmark Stability −1 |
| Tie | TC +1 (institutional paralysis) |

**Diplomatic Token interaction (PP-320-ED):** Each active Diplomatic Token on a faction mat counts that faction as Support regardless of declared vote.

---

### Hafenmark — Diplomat Card (ED-320 RESOLVED)
**Type:** Senator Outward. **Card type:** Hafenmark faction card. **Once per season.**
Roll: Influence vs Ob = target Mandate ÷ 2 round up, min 1.
**Restriction:** Cannot target Church if PI < 3.

| Degree | Effect |
|--------|--------|
| Overwhelming | Place 1 Diplomatic Token on target mat + target Stability +1 + PI +1. Target faction's actions against Hafenmark: +1 Ob this season and next. |
| Success | Place 1 Diplomatic Token on target mat + PI +1 |
| Partial | PI +1 (no Token) |
| Failure | Hafenmark Stability −1 |

**Diplomatic Token:** Permanent marker on target faction mat. Removed on military conflict with Hafenmark OR target faction elimination. Maximum 1 per faction mat. Public. Token effects: target faction counts as Support in Parliamentary Sessions.

---

### Crown — Royal Charter (PP-433)
**Type:** Consul Inward (Crown only).
Roll: Mandate vs Ob = territory Prosperity ÷ 2 round up, min 1. Virtue Ethics: −1 Ob.
**Limit:** Max (Mandate ÷ 2 round up) active Charters simultaneously.

Success: Territory becomes Crown Charter Territory:
- All factions: Govern/Trade −1 Ob
- Church Seizure: +1 Ob
- Crown own actions: −2 Ob
Charter dissolves on control transfer.

---

### Crown — Royal Decree Enhancement (PP-435)
**Type:** Special/Unique Power. Ob 2. Once per season (existing mechanic).
**Enhancement (Overwhelming only — net ≥ 2×Ob AND ≥ 3):**
Choose one:
(a) Stat ±2 to one faction
(b) Stat ±1 to two different factions
(c) Stat ±1 to one faction AND suspend one threshold effect for one season

Success (unchanged): Stat ±1 to one faction. Consecutive: +1 Ob/season.
Cannot target Intel.

---

### Crown — Thread Liaison (PP-436)
**Timing:** Phase 1 declarative. No roll.
Crown designates one allied faction. Liaison's Thread operations in Crown-held territories count toward Crown's co-victory RS threshold tracking.
**Allied definition:** Active Treaty partner OR same-side Parliamentary Session voter OR common Resentment target.
**Dissolves on:** Military conflict between Crown and Liaison.

---

### Crown — Diplomatic Outreach to Schoenland (PP-437)
**Type:** Senator Outward (Crown only). Cannot use same season as Formal Crown Treaty.
Roll: Influence vs Ob = current AER level, min 1. Virtue Ethics: −1 Ob.
**Fragmentation modifier:** +2 Ob if 3+ factions have Stability ≤ 2.

| Degree | Effect |
|--------|--------|
| Overwhelming | IP −2 + AER +1 |
| Success | IP −1 + AER +0.5 |
| Partial | AER +0.5 |
| Failure | AER −0.5 |

---

### Varfell — VTM Discretion (PP-438)
**Type:** Accounting action. **At VTM 3+.**
Spend 1 Patience Counter at Accounting to suppress VTM TC contribution for that season.
**Cooldown:** Once per 2 consecutive seasons (Discretion Cooldown marker, cleared at Year-End).
Does not suppress other TC sources.

**Cost:** 0 PC at VTM 3 (cooldown-only gate; TC contribution is low). 1 PC at VTM 4+ (TC contribution is high; cost is proportional). (ED-323 resolved 2026-04-08.)

---

### Varfell — Revelation Tokens / Path A (PP-439)
**Full reveal criteria:** Overwhelming result on Tribune Investigate OR 4 consecutive PC Spy successes.
On full reveal: place Revelation Token on target faction mat (public, permanent).
**Path A condition:** Two Revelation Tokens on two different rival faction mats = "fully revealed" condition met.
Target faction knows they've been revealed (public token).

---

### Varfell — Ethical Framework (PP-440)
**Consequentialism −1 Ob applies to:**
- Tribune Intel actions (Investigate, Spy, VTM-building, Counter-Narrative)

**+1 Ob penalty applies to:**
- Public ideological campaigns
- Open diplomatic commitments
- Relationship investments with no Intel yield

---

### Varfell — Counter-Narrative (PP-441 + PP-441-COR)
**Type:** Tribune Outward (Varfell only). Target = Church-held or Church-prominent territory.
Church-prominent = Church global Mandate > controlling faction global Mandate (assessed at action declaration).
Roll: Intel vs Ob = Church Mandate ÷ 2 round up, min 1. Consequentialism: −1 Ob.
**+2 Ob modifier:** If territory has an active Inquisitor (applies to all Tribune Intel actions).

| Degree | Effect |
|--------|--------|
| Overwhelming | TC −0.5 + AP +2 in territory |
| Success | AP +2 in territory |
| Partial | AP +1 |
| Failure | Intel network exposed: Church notified of Varfell presence, AP +1 tagged as Varfell (+2 Ob to Counter-Narrative in this territory next season) |

**TC tracking:** Fractional TC values accumulate. Track running decimal on TC track. Round to integer for threshold checks only.
**AP note (ED-325):** AP is tracked per-territory (PP-185). Counter-Narrative AP in a territory contributes to that territory's AP pool, not a global pool. Inquisitor deploys in the territory where threshold is crossed.

---

### Counter-Intelligence Postures (PP-442)
All three are passive faction abilities (no card required, no roll):

**Crown — Royal Guard** (Phase 4, Priority 1 — fires before all other Phase 4 actions):
Once per season, cancel one successful Intel action targeting Crown. No card cost.

**Hafenmark — Procedural Objection:**
On any Varfell Tribune Investigate success, Hafenmark may declare Procedural Objection. Cost: consumes Parliamentary Challenge use for this season (if Challenge already used: cannot declare Objection). Effect: if Hafenmark Mandate ≥ 4, revealed stat is replaced with a false value for all non-Varfell observers. Varfell sees true value; others see false.

**Church — Sanctuary Extension:**
Existing Sanctuary card: extended to also block Varfell 4-PC Spy action once per season (in addition to existing Sanctuary effects).

---

## Parish / Cathedral System — Church (ED-319 RESOLVED)
**Prerequisite:** Church Consul Inward action in territory.
Parish: 2 sequential successful Consul Inward actions + 1 Wealth. Effect: CV floor raised to 1 (persists unless Cathedral). 
Cathedral: 3 more successful Consul Inward (5 total from zero) + 2 additional Wealth. Effect: CV floor 2 + Church Prominence +1 in territory for seizure calculations.
**Control change:** Parish survives. Cathedral degrades to Parish on control transfer.
**Limits:** Max 1 Parish or Cathedral per territory. Max 1 upgrade attempt per territory per arc.

---

## Hafenmark — RDT/TD Tracks (ED-321 RESOLVED)

### Reformed Doctrine Track (RDT) — Range 0–6
Advances: Reformed Settlement event = +1 (max once per arc). Requires: Hafenmark controls territory where Church has Parish/Cathedral AND Hafenmark M ≥ 3 AND PI ≥ 4.

| RDT | Effect |
|-----|--------|
| 0 | Reformed Settlement blocked: Church may Appease at no cost |
| 1 | Parliamentary Manoeuvre targeting TC: −1 Ob |
| 2 | Formal Reformed Settlement. TD track activates. |
| 3 | Church Mandate −1 (institutional strain) + Diplomatic actions vs Church: −1 Ob |
| 4 | TC suppression extends: −1 TC/season while Hafenmark Mandate ≥ 3 (was ≥ 4). Reformed territory CV actions +1 Ob for Church. |
| 5 | Excommunication against Hafenmark costs +2 Mandate. Baralta: −2 Ob on TC Suppress actions. |
| 6 | All diplomatic actions targeting Hafenmark from any faction: +1 Ob |

### Theological Dissatisfaction (TD) — Range 0–5
Activates at RDT 2. Advances: +1 per arc when RDT ≥ 2 AND Church plays Assert. Church may freeze TD by playing Accommodate Reformed Settlement.
Regression: TD −1 if Church Excommunicates Hafenmark AND RDT does not advance that arc.

| TD | Effect |
|----|--------|
| 0 | No effect |
| 1 | Templar deployment costs +1 Wealth in Hafenmark-adjacent territories |
| 2 | Cardinal of Fortitude schism risk when Church Stability < 3 |
| 3 | Any season Church loses PI: Hafenmark gains PI +1 |
| 4 | Church Seizure in Hafenmark territories: Ob +2 |
| 5 | Church cannot seize T8 Gransol (Hafenmark capital) regardless of TC or CV. Permanent. |

---

## Total Domination Victory Path (ED-318 RESOLVED)
Available to all playable factions. Alternate path, no TCV requirement met via normal faction path.

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 28 (all controllable territory) |
| All rival factions | Stability 0 (eliminated) OR formally Submitted |

**Submission mechanics:** Any faction at Stability 0 that has not been eliminated may formally Submit (declared at Accounting). Submitted faction: removed from victory competition, remains on board as vassal (NPC-controlled, all stats halved rounded down, no independent actions). The Total Domination faction must hold all non-Submitted, non-eliminated rivals at Stability 0 simultaneously for 2 consecutive Accounting steps.

---

## Varfell Path B — Southernmost Dominion (ED-311 RESOLVED — Option A)
**[Replaces provisional conditions in victory_architecture_v1.md §3.4]**

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 8 |
| Control T4 (Grauwald) AND T13 (Oastad) | both held |
| VTM | ≥ 3 |
| Warden Recognition (WR) | ≥ 2 |

**WR track (0–4):**
- WR 0: Wardens unaware/indifferent
- WR 1: Wardens have observed Vaynard (≥ 1 successful Expedition)
- WR 2: Wardens recognise Vaynard as steward (prior WA ≥ +1 AND WC ≥ 1 conditions collapsed here)
- WR 3: Wardens actively cooperate (+1D Thread ops peninsula-wide)
- WR 4: Edeyja has made substantive contact (Overwhelming Forgetting Check)

WR advances: successful Expedition seasons (+1 per Overwhelming or cumulative Successes).
WR decreases: RM emergence (WR −2); T15 neglect 3+ seasons (no Expedition attempted): WR −1.
**Blocked if:** WR has ever returned to 0 after first advancing past 1.

## BG Stress Test Patches (2026-04-08)
<!-- PATCHES APPLIED: PP-470-PP-475 -->

## Total TCV Correction (PP-470)
Canonical Total TCV = **29** (corrected from stated 30).
Recount: T1(5)+T2(1)+T3(2)+T4(1)+T5(1)+T6(1)+T7(1)+T8(4)+T9(3)+T10(2)+T11(1)+T12(3)+T13(1)+T14(2)+T15(0)+T17(1) = 29.
Total Domination (TCV >= 28) leaves 1 uncaptured TCV (any single TCV-1 territory).

## Restoration Senate Market Restriction (PP-471)
Restoration Movement may not purchase Legionary cards from Senate Market.
Military 0 makes Muster invalid (PP-039). Legionary cards are unplayable in hand.

## Conviction Yield Dead Zone — Explicit Note (PP-473)
**Church-controlled territories produce zero Conviction Yield.**
Church Prominence = Church Mandate > controlling faction Mandate. When Church controls a territory, Church IS the controlling faction. Church Mandate > Church Mandate = False = not Prominent = no Conviction Yield.
Implication: Post-TC 75 seizure removes territories from Conviction Yield pool. Plan accordingly.

## AER >= 3 and Parliamentary Challenge — Independence Clarification (PP-474)
AER >= 3 (PP-203) and Parliamentary Challenge (PP-431-COR) are independent:
- AER >= 3 bypasses Hafenmark Structural Suppression (passive -1/season from Baralta Mandate >= 4).
- Parliamentary Challenge is a card action; fires when played regardless of AER.
- When AER >= 3 is active: structural is already negated; Challenge's "replaces structural" clause has no practical effect on structural. Challenge still fires and produces its degree-table TC result.

## Submission + Mandate 0 Ruling (PP-475)
If Submitting faction's halved Mandate = 0: **Submission supersedes Faction Collapse.**
Submitted faction remains as vassal with Mandate 0. Mandate-0 effects apply. Faction does not enter Faction Collapse (which requires Stability 0 at Accounting end per I-04/P-15, not Mandate 0).

## Battle Resolution — Formal Outcome Table (PP-476)
Both attacker and defender apply their own degree result independently.
For each side: margin = (own net − opponent net), if positive; 0 if own net ≤ opponent net.
Apply: margin 0 → no outcome for that side; margin 1 to Ob−1 → Discipline −2 on opponent unit;
margin = Ob → Discipline −4 on opponent unit; margin > Ob → opponent unit destroyed.
Drawn battle (equal net): no degree for either side; both Discipline −1.

Discipline floor: 0. Any result pushing Discipline to ≤ 0 destroys the unit.
Multi-unit territory: one roll per faction using Military stat pool. Player assigns Discipline loss to specific unit card of their choice.
Unit removed (by stat cap reduction): returned to reserve with Discipline reset on next Muster.

## Fortify — Pool Stat (ED-338 provisional)
[PROVISIONAL: Fortify uses Military stat pool. Confirmation pending.]

## VTM 5 — Once-Per-Game Tracking (PP-477)
Varfell faction mat: flip token 'VTM 5 Power Used'. Set to Used on ability activation. Not reset between sessions.

## Restoration Movement — Founding Mechanic (PP-478)
<!-- RM is NOT a playable faction in BG-only mode. -->
<!-- In Hybrid mode, RM emerges mid-campaign via Founding if conditions are met. -->

### RM Status by Mode
| Mode | RM Status |
|------|-----------|
| BG only | Not a playable faction. Presence markers are environmental tokens (GM/table). No player controls RM. No RM solo or co-victory. |
| Hybrid | Not present at game start. Emerges via Founding event. Once founded: playable by PC's controlling player (or GM if NPC-founded). |

### Popular Will (PW) Track
Range 0–5. Public track (placed near RS clock). Starts at 0. Belongs to no faction.

**Advances +1 when:**
- ≥ 2 territories simultaneously have CV ≤ 1 AND no Church Heresy Investigation is active in any of them (checked at Accounting).
- A PC performs a successful Community Organising or Community Weaving personal scene in a CV ≤ 1 territory (Zoom In result).

**Regresses −1 when:**
- Church executes a successful Heresy Investigation in a CV ≤ 1 territory.
- TC ≥ 60 at Accounting (while TC ≥ 60: PW regresses −1/season automatically).

Floor: 0. Ceiling: 5.

### Founding Trigger (all three at any Accounting, Hybrid mode only)
| Condition | Threshold |
|-----------|-----------|
| PW track | ≥ 3 |
| Territories with CV ≤ 1 | ≥ 3 |
| RS | ≤ 60 |

### Founding Procedure
Founding Agent declared (PC with communal Conviction, or named NPC at GM discretion).
Roll: Founding Agent's Influence vs Ob = TC ÷ 10 (round up, min 1, max 5).

| Degree | Starting Stats | Presence Markers |
|--------|---------------|-----------------|
| Overwhelming | Mandate 2, Influence 3, Wealth 1, Military 0, Stability 4 | 3 markers in CV ≤ 1 territories |
| Success | Mandate 1, Influence 2, Wealth 1, Military 0, Stability 3 | 2 markers |
| Partial | PW +1. Not founded. Retry next Accounting. | — |
| Failure | PW −1. Church gets 1 free Heresy Investigation. Cannot retry until PW resets to ≥ 3. | — |

**Post-founding card hand:** 2× Praetor, 1× Pontifex, 1× Recess.
**NPC-founded RM AI priority:** CV reduction > Presence spreading > Founding Agent protection > Weaving.

### Community Organising (Restoration, post-Founding)
Pool: 1D base + 1D per adjacent territory with RM Presence marker (PP-460). Failure: no Stability cost. Retry next season.

### BG-Only Mode Notes
- PW track not used.
- RM co-victories (Varfell+RM, Hafenmark+RM) not available.
- "5 players only" restriction struck — RM is not a player faction in any player-count BG game.

## Conflict Marker — Church + Hafenmark Partition (PP-479)
Conflict Marker: flip token on Church or Hafenmark mat. Placed when either faction plays Legionary targeting the other's territory. Removed at second Accounting after placement.
"No active military conflict" condition for Partition co-victory = no Conflict Marker active on either mat.

## Ministry Domain Action Conflict (PP-480)
If Ministry NPC would play a Domain action in a territory already acted on by any player faction this Phase 4 resolution: Ministry redirects to next-priority viable territory per AI tree. If all viable territories are already acted-on this phase: Ministry takes Priority 5 default in any uncontested AP-token territory.
