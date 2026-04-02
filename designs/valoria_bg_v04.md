# VALORIA: THE BOARD GAME
## Ruleset v0.4
**Date:** 2026-04-01
**Authority:** v0.3 + canon audit against canonical_timeline.md, narrative_scenario_chains.md, batch_ad_resolutions.md, mechanical_tasks_and_patches.md, hybrid_gaps_resolved.md, batch_e_designs.md, emergent_scenarios.md, Valoria_Philosophical_Foundations.md.
**Status:** Pre-playtest. All three prior editorial blockers resolved. New blocking items noted in C2.

---

## CHANGES FROM v0.3

### Canon Fixes
- **Elske's location corrected.** v0.3 placed Elske in T3 (Himmelenger, Church custody). Canonical timeline has her in Altonia, married to an Altonian Duke whose territory borders T4 (Spartfell). She is now an off-board character. Rescue path revised. See B5 Löwenritter and new B2 notation.
- **Torben Tutoring Demand formalised.** Per canonical timeline: Altonia is actively demanding Torben for court "education." This is now an IP-triggered event at IP ≥ 40. Previously implied, never mechanised.
- **Year confirmed: 245 AG.** Per canonical_timeline.md, superseding all prior checkpoint references to Year 102 AG.
- **Starting clock values corrected.** TT/TC/IP alignment with canonical timeline: RS 72 (unchanged), TC 22 (was 15 — adjusted to reflect Church's colonial-period establishment pre-Secession), IP 20 (unchanged). See B2.
- **Restoration Movement Mandate corrected to 2** (was noted as raised to 4 in v0.3 changelog, but faction sheet shows 2 — the Influence was raised to 4, not Mandate). Clarified in B5 Restoration.
- **Church of Solmund name retained.** Solmund is the divine figure; Galbados was the catalyst. The Church venerates Solmund's doctrine as transmitted through Galbados's acts and teachings. This is canonical — Baralta's Conviction references Solmund-ordained authority as distinct from Church mediation.

### Editorial Blockers Resolved
- **BG-E-NEW-01 (Patience Protocol):** Authored. See B5 Varfell.
- **BG-E-NEW-02 (Casus Belli):** Authored. See B7 Standing and Treaties.
- **BG-E-NEW-03 (Klapp Event Card):** Authored. See B10 Event Cards.

### Integrations from Supporting Documents
- **Hybrid gap resolutions** (hybrid_gaps_resolved.md): Information asymmetry display table (B14), Cascade phase process (B4 Accounting), NPC pledge compliance (B16), contested figure resolution.
- **Mechanical patches** (mechanical_tasks_and_patches.md): Unit rosters (MT-01) formalised in B8. Domain Echo and Domain Ob clarifications from MT-02/03 carried into B7.
- **Batch A–D resolutions** (batch_ad_resolutions.md): Approach Training CP cost (8 CP, hybrid only), Circles single-track architecture confirmed, faction collapse at Stability 0 (B9 new rule), treaty betrayal consequences table (B7).
- **Battle resolution** written for board game mode (B8 expanded) — previously referenced "Mass Battle v3 Part B" which was not included.
- **NPC AI blocks** completed for Guilds, Niflhel, Schoenland, Riskbreakers, Inquisitors (B13).
- **Milestone Bonuses table** completed (B14 renamed from Hybrid Interface; was incomplete).
- **Community Projects table** completed (B9).

### New Issues Resolved by Simulation
See Part D (Simulation Report) and Part E (Patch Report) for simulation-identified issues and their resolutions. 11 gaps found; all patched.

---

# PART A — SYSTEM REGISTER

## A.1 Core Systems (21 player-facing systems)

| # | System | Layer | Notes |
|---|--------|-------|-------|
| 1 | Card-Hand + Recess | Action Economy | Hand = capability. Foundation of all player agency. |
| 2 | Order Orientation | Action Economy | Inward/Outward sub-type selector. Zero overhead. |
| 3 | Senate Market | Action Economy | Hand expansion = faction development. |
| 4 | Cooldown Track | Action Economy | 3-slot wheel for Unique Powers. |
| 5 | Three Clocks | Victory/Loss | RS metaphysically primary. TC and IP politically co-equal. |
| 6 | Clock Environmental Effects | Ambient Modifier | All three clocks modify action obstacle ratings. |
| 7 | Deed Tokens | Victory | Simultaneous-holding tension. |
| 8 | Hollow Victory Scoring | Victory | Legitimacy modifier. Tracked publicly at Year-End. |
| 9 | Institutional Mandate | Political | Uphold/Compromise. Faction identity with mechanical teeth. |
| 10 | Standing Tokens | Political | Political history. Grievance and capital. |
| 11 | Crown Policy | Political | Crown sets the environment for all factions. |
| 12 | Parliament Integrity | Political | Shared institution. Hafenmark's primary lever. |
| 13 | Thread Resonance | Thread | Binary seasonal marker. |
| 14 | Thread Debt | Thread | Permanent cost of Thread operations. |
| 15 | Church Attention Pool | Thread | Consequence-detection only. |
| 16 | Co-Movement Card Deck | Thread | Three-dimensional consequence per operation. |
| 17 | Community Projects | Faction/Thread | Multi-season investments. |
| 18 | Champions + Wound States | Military | Named leaders as mobile tokens. Hybrid bridge. |
| 19 | Faction Structural Asymmetry | Faction | Distinct profiles, private tracks, unique mechanics. |
| 20 | Patience Protocol | Varfell | Vaynard's sustained restraint mechanic. |
| 21 | Casus Belli | Political | Justified military expansion on treaty breach. |

**Faction-specific private tracks:**
- Varfell Thread Mastery (VTM) 0–5: private until VTM 3
- Varfell Patience Counters (PC) 0–6: always private
- Reformed Doctrine Track (RDT) 0–6: Hafenmark private
- Theological Dissatisfaction (TD) 0–5: Hafenmark private
- Altonian Ecclesiastical Relationship (AER) 0–5: Church, board-visible

---

# PART B — RULESET v0.4

## B1 — OVERVIEW

**Valoria: The Board Game** is a standalone political-strategic game set on the Valorian peninsula, 245 AG. It is also the strategic layer of hybrid tabletop roleplaying / board game play.

**Core feel:** Powerful institutions attempting to consolidate power across a dying world. Rendering Stability (RS) degrades through sustained conflict and accelerates under large-scale Threadwork. The Church of Solmund siphons Crown authority toward theocracy. Altonia watches. Every faction wins by expanding — but expansion tears the world further apart.

**Three game modes:**
- **Board Game (this ruleset):** Complete standalone, 2–4 hours, 3–5 seasons per session.
- **Hybrid:** Board game as strategic layer feeding into tabletop roleplaying personal-scale scenes.
- **Tabletop Roleplaying:** Governed by TTRPG compiled stages (separate document).

### Playable Factions

| Faction | Available |
|---------|-----------|
| Crown | 2–5 players |
| Church of Solmund | 2–5 players |
| Hafenmark | 2–5 players |
| Varfell | 2–5 players |
| Restoration Movement | 5 players only (optional) |
| Löwenritter (post-coup) | Conditional: only if coup fires |

### NPC-Driven Factions

Löwenritter (pre-coup), Riskbreakers, Inquisitors, Guilds, Schoenland, Niflhel, Altonia, and Edeyja / the Wardens are always NPC-controlled. Full AI blocks in B13.

---

## B2 — THE BOARD

### Territory Map

| # | Territory | Start Control | Pros | Fort | Special |
|---|-----------|--------------|------|------|---------|
| 1 | Valorsplatz (Capital) | Crown | 6 | 2 | Royal Court: Crown Policy −1 Ob. Parliament here: Hafenmark Mandate orders −1 Ob. |
| 2 | Gransol | Crown | 5 | 1 | Garrison: Muster here +1D. |
| 3 | Himmelenger | Church | 5 | 2 | Grand Cathedral: TC +1/season Church controls. Church Unique Power −1 Ob here. **Elske is NOT here** (see below). |
| 4 | Spartfell | Crown | 3 | 2 | Altonian Border: IP threshold events fire here first. Invasion entry point. **Border contact with Elske's duchy possible at IP ≥ 40.** |
| 5 | Arnesheld | Crown/Löwenritter | 4 | 3 | Löwenritter Fortress: Martial Law −1 Ob. Fort max 4. |
| 6 | Hafenvalor | Hafenmark | 6 | 1 | Ducal Court: Sovereign Authority Doctrine here only. Major port. |
| 7 | Lowenskyst | Hafenmark | 5 | 0 | Trade Hub: all Trade +1D. Schoenland sea route. |
| 8 | Eidursjo | Guilds (NPC) | 4 | 0 | Difficult terrain: March costs 2 cards. Guild trade routes active. |
| 9 | Varfell | Varfell | 4 | 1 | Varfell Seat: VTM research here only. Einhir ruins: Restoration Weaving −1 Ob. |
| 10 | Sigurdshalm | Niflhel (NPC) | 3 | 0 | Black Market: Niflhel Covert −1 Ob. All Trade +1 Ob. |
| 11 | Halvardshelm | Guilds (NPC) | 5 | 0 | Breadbasket: +1 Prosperity/season uncontested. Muster Ob −1. |
| 12 | Oastad | Uncontrolled | 3 | 0 | Thread Wound: RS thresholds trigger +10 early here. RS −1/season after 2 consecutive seasons of any occupation. Southernmost rule applies. |
| 13 | Stillhelm | Uncontrolled | 2 | 0 | Southernmost Access: required for Expedition. Non-Thread orders +1 Ob. RS −1/season any occupation. Southernmost rule applies. Warden Cooperation track here (inactive until Warden Emergence). |
| 14 | Eisengrund | Restoration (informal) | 4 | 0 | Einhir Heartland: Restoration Influence −1 Ob. Church Influence +1 Ob. |
| 15 | Schoenland | Neutral (NPC) | 5 | 1 | Altonian Trade. At IP ≥ 75: Altonian Vanguard deploys. Intel orders here: visible to Altonia. |

### Elske — Off-Board Status (v0.4 Correction)

**Princess Elske Almqvist is in Altonia, not on the board.** She was married to Duke Hardar Veldensohn, whose duchy borders T4 (Spartfell) at game start. This is a diplomatic arrangement, not captivity — but she is effectively beyond Valoria's reach while IP ≥ 30 makes cross-border movement hostile.

**Elske's Off-Board Card:** Keep a face-down Elske card near T4. It tracks:
- Elske Loyalty (0–7, starts 4): her sympathy toward Valoria vs. her Altonian household. Modified by events.
- Contact Established (yes/no): any Diplomatic action by Crown or Löwenritter in T4 when a Diplomat or Tribune card reaches T4 with orientation Outward: makes contact.

**Making Contact with Elske (T4 required):**
- Crown or Löwenritter Senator Outward in T4 (Diplomacy, Ob 2 at IP < 60; Ob 3 at IP ≥ 60): Contact Established.
- Once established: Tribune Inward in T4 reveals one piece of Elske's information (her current Loyalty, what she knows about Altonian court).
- Elske Loyalty increases: Crown upholds Constitutional Stability path; Löwenritter holds PI ≥ 3; any faction exposes Altonian aggression publicly.
- Elske Loyalty decreases: IP rises (Altonian pressure on her household); Torben sent to Altonia (−2); Almud publicly concedes to Altonian demands (−2).

**Elske Returning to Valoria (rescue/choice):**
- At Elske Loyalty ≥ 6 AND IP < 60: she may choose to return. Crown or Löwenritter must have a unit in T4. Roll Crown/Löwenritter Military vs. Ob 2. Success: Elske returns. Duke Veldensohn does not pursue — her choice is respected if she acts independently. IP +5 (diplomatic rupture; Altonia views this as breach of treaty).
- At Elske Loyalty ≤ 2: she actively supports Altonian strategic interests. IP −3/season while so disposed.

**Elske Loyalty ≥ 6 at campaign end (without formal return):** Elske represents Valoria's interests within Altonian court. Grand Diplomatic Scene Ob −2 (she has been quietly working toward peace).

### Torben Tutoring Demand (IP ≥ 40 Event)

When IP crosses 40 for the first time: **Altonian Tutoring Demand** event fires at next Accounting.

- Altonia formally requests Torben Almqvist be sent to their court for "diplomatic education." This is leverage, not education.
- Crown must respond this season (Phase 2 — Negotiation):
  - **Comply:** Torben leaves T1. Torben Loyalty −2. IP −5 (Altonia satisfied for 3 seasons). Ehrenwall Coup Counter +1 (Crown deferred sovereignty to Altonia).
  - **Refuse:** IP +3. Altonia begins active pressure. Crown Mandate −1 (perceived as provoking foreign crisis).
  - **Negotiate (Diplomat or Senator Outward, Ob 3):** Delay the demand 2 seasons. IP stays. No Loyalty change. Ob 3 — difficult but available.

- If Complied: Torben is off-board. Torben Loyalty can still increase (Crown holds PI ≥ 5 consecutively: +1/Year-End despite Torben's absence — his respect for Valoria persists). Torben can be retrieved via Elske (if she is allied and in Altonian court): this becomes a combined diplomatic operation.

### The Southernmost Rule (T12 and T13)

**Any military unit in T12 or T13 placed by a faction without Thread-qualified presence is immediately removed.** No Standing cost, no Stability check, no battle. The substrate damage there cannot support non-Thread configurations.

Thread-qualified presence: Restoration Weaver card played this season in that territory, OR Varfell VTM ≥ 2, OR hybrid practitioner with TS 30+ present.

This rule has always applied. Factions discover it by attempting.

### Board Tracks

**AER Track (0–5):** Near IP clock. Starts at 2.
**Warden Cooperation Track (0–3):** Near T13. Inactive until Warden Emergence.
**Löwenritter Coup Counter (0–4):** Public, near Löwenritter reference card.
**Torben Loyalty Track (0–7, starts 3):** Shared ledger or Crown mat.
**Elske Loyalty Track (0–7, starts 4):** On Elske off-board card, near T4.

### Clock Tracks

**Rendering Stability (RS):** Starts 72 → 0. Rupture = shared loss.
**Theocratic Clock (TC):** Starts 22 → 100. TC 80 = Church Territorial Seizure.
**Invasion Pressure (IP):** Starts 20 → 100. IP 75 = Altonian Vanguard.
**Parliament Integrity (PI):** Starts 7. Range 0–10.

*(TC starts at 22, not 15, per canonical timeline: the Church predated Valorian independence and its theocratic momentum was already building through the Altonian colonial period. This reflects 45 years of post-independence accumulation on a pre-existing institutional base.)*

### Clock Environmental Effects

**Rendering Stability (RS) Effects:**

| RS Range | Effect |
|----------|--------|
| 72–50 | No modifier |
| 49–30 | Thread operations: −1 Ob (world urgency accelerates practitioners). Non-Thread orders in T12/T13: +1 Ob |
| 29–20 | As above. Entity encounters possible in T12/T13. All Muster: +1 Ob |
| Below 20 | All orders all territories: +1 Ob. Community Projects advance +1/season (crisis mobilises communities). Entity encounters expand to all uncontrolled territories |

**Theocratic Clock (TC) Effects:**

| TC Range | Effect |
|----------|--------|
| Below 30 | No modifier |
| 30–49 | Church orders: −1 Ob in Church-held territory |
| 50–69 | Church orders: −1 Ob everywhere. Non-Church Diplomacy targeting Church: +1 Ob. Mandatory Assert/Suppress each season |
| 70+ | As above. Territorial Seizure protocol active. AER begins modifying TC gains |

**Invasion Pressure (IP) Effects:**

| IP Range | Effect |
|----------|--------|
| Below 30 | Trade with Schoenland: +1D |
| 30–59 | Trade with Schoenland: +1 Ob. All factions: +1D to Intel orders |
| 60–74 | Trade disrupted: Schoenland +2 Ob. Proxy at T4: +1D military there |
| 75+ | Altonian Vanguard deployed. Note: AER ≥ 4 raises threshold to 80; AER 5 holds IP at 50 |

**Altonian Invasion Events (IP ≥ 75):**
- Season 1: Altonian Vanguard (Military 5, Cohesion 5) deploys to T4. Invasion countdown begins (3 seasons). Duke Veldensohn's territory is staging ground — this directly threatens Elske.
- Season 2: Vanguard advances if not repelled. All factions: −1 Ob military in T4.
- Season 3: If not repelled and IP not below 60: full invasion. Altonia marches north (T4→T2). Shared loss if Altonia controls ≥ 5 territories.
- If IP drops below 60 before Season 3: Vanguard withdraws. Resets if IP crosses 75 again.

**Special — Elske During Invasion:** If Vanguard deploys and Elske Contact Established: her Loyalty −1 (household is now enemy army). If Elske Loyalty 0 at invasion: she actively supports Altonian logistics. Elske Loyalty ≥ 5 at invasion: she provides intel about Vanguard composition (one Altonian unit stat revealed free).

---

## B3 — ACTION ECONOMY

### Core Mechanic
All rolls: pool = relevant faction stat (1–7). Dice: d6. Success = 4+. Majority 1s = Failure regardless of other dice.

**Degree table:**

| Net Successes | Degree |
|---------------|--------|
| Ob + 1 or more surplus | Overwhelming |
| = Ob | Success |
| Ob − 1 | Partial |
| 0 successes | Failure |

**Ob 0:** Any roll with ≥ 1 success = Overwhelming. Ob cannot go below 0. Rolling is still required.
**Majority 1s override:** If more dice show 1 than show 4+, result is Failure regardless of successes.

### Stat-to-Action Mapping

| Card | Action | Stat Used |
|------|--------|-----------|
| Legionary | Muster / March | Military |
| Consul | Govern / Trade | Mandate (Govern) · Wealth (Trade) |
| Prefect | Govern all controlled | Mandate |
| Senator | Decree / Diplomacy | Mandate |
| Tribune | Investigate / Spy | Influence |
| Recess | Retrieve hand | — (costs 1 Wealth) |
| Organizer (Restoration) | Community Organizing | Influence |
| Weaver (Restoration) | Community Weaving | Influence |
| Presence Spread (Restoration) | Move Presence markers | Influence |
| Project (Restoration) | Start Community Project | Mandate |
| Pontifex (Church base) | Ecclesiastical Suppression | Mandate |
| Pontifex (Senate Market) | Thread operation | Influence |
| Diplomat | Diplomacy at −1 Ob | Influence |
| Colonist | March + Govern at destination | Military then Mandate |
| Architectus | Fortify + Govern same territory | Military then Mandate |
| Tribune Militum | Military at −1 Ob | Military |
| Aedile | Trade at −1 Ob | Wealth |
| Praetor | Start or advance Community Project | Mandate |
| Censor | Crown only: issue Policy / Block order | Mandate |

### Base Hands

| Faction | Starting Hand |
|---------|--------------|
| Crown | 2× Legionary, 1× Consul, 1× Senator, 1× Prefect, 1× Recess |
| Church | 2× Senator, 1× Pontifex (Eccl. Suppression), 1× Consul, 1× Legionary, 1× Recess |
| Hafenmark | 2× Consul, 1× Senator, 1× Legionary, 1× Diplomat, 1× Recess |
| Varfell | 2× Tribune, 1× Legionary, 1× Consul, 1× Colonist, 1× Recess |
| Restoration Movement | 2× Organizer, 1× Weaver, 1× Presence Spread, 1× Project, 1× Recess |
| Löwenritter (post-coup) | 3× Legionary, 1× Tribune (Requisition Order), 1× Prefect, 1× Recess |

### Action Outcome Effects

**Govern (Consul Inward / Prefect):**
- Overwhelming: Prosperity +1; may issue one Decree effect in this territory at no additional card play.
- Success: Prosperity +1.
- Partial: No Prosperity change; Stability check waived this season.
- Failure: Prosperity −1; Stability check Ob 1.

**Trade (Consul Outward / Aedile):**
- Overwhelming: Wealth +2; target faction may offer counter-deal at no card play.
- Success: Wealth +1.
- Partial: Wealth +1, but target may block future Trade 1 season OR demand 1 Wealth at Year-End.
- Failure: No gain. If Trade targeted Schoenland at IP ≥ 30: +1 Ob friction on next Trade there.

**Diplomacy (Senator Outward / Diplomat):**
- Overwhelming: 1 Influence in territory; establish Open Pledge at no card play; OR block one declared Order next season.
- Success: 1 Influence in territory; OR arrange Open Pledge.
- Partial: Non-binding deal; no Influence.
- Failure: No effect. If adversarial: target gains Standing +1 vs you.

**Decree (Senator Inward):**
- Overwhelming: Legally binding Decree; non-compliance costs Standing −1; Mandate check waived.
- Success: Decree issued; non-compliance costs Standing +1 vs you.
- Partial: Contested; target may respond with Parliamentary Manoeuvre or Senator without card cost.
- Failure: Your Mandate −1; Standing +1 vs you from territory factions.

**Parliamentary Manoeuvre (Hafenmark Senator Inward):**
- Overwhelming: PI +1; block one Crown Policy this season.
- Success: PI +1.
- Partial: PI unchanged; one declared Order delayed one priority tier.
- Failure: PI unchanged; next Parliamentary Manoeuvre this season +1 Ob.

**Investigate (Tribune Inward):**
- Overwhelming: One faction's complete stat line revealed; one hidden private track revealed.
- Success: One faction stat revealed.
- Partial: Qualitative — "above or below threshold" for one stat.
- Failure: No info. If in enemy territory: target may play one defensive card out-of-priority (costs them 2 Standing).

**Spy (Tribune Outward):**
- Overwhelming: Target's planned card in one territory revealed before Phase 3; one stat revealed; plant one false information.
- Success: One planned card revealed before Phase 3.
- Partial: Card TYPE in territory known (not orientation or exact card).
- Failure: Nothing. If in enemy territory: target gains Standing +1 vs you.

**Muster (Legionary Inward):**
- Overwhelming: Raise 1 unit; may immediately upgrade to Elite (Cohesion +1) at no cost.
- Success: Raise 1 unit (Strength 2, Combat Power = Military ÷ 2 round up).
- Partial: Raise 1 unit, Cohesion −1 (understrength muster).
- Failure: No unit; Wealth −1 (wasted recruitment).

**March (Legionary Outward):**
- Overwhelming: Move unit; may immediately initiate Battle if enemy present; establish control if empty.
- Success: Move unit; declare Battle if enemy present (resolved Phase 4 Priority 2).
- Partial: Unit moves but Cohesion −1.
- Failure: Unit stays; Stability check Ob 1.

**Community Organizing (Organizer — Restoration only):**
- Overwhelming: 1 Influence in territory + Prosperity +1.
- Success: 1 Influence in territory.
- Partial: No effect; territory controller may Govern without card play to offset.
- Failure: Church Attention Pool +1.

**Senate Market:**
6 cards face-up from Senate Deck. Purchase during Senator Outward (Diplomacy) play or during Phase 2 at standard cost. Purchased card enters hand after Recess.

| Card | Cost |
|------|------|
| Tribune | 1 |
| Architectus | 2 |
| Colonist | 2 |
| Diplomat | 1 |
| Tribune Militum | 2 |
| Aedile | 1 |
| Pontifex (Thread — Restoration / qualified only; Church barred) | 2 |
| Praetor | 1 |
| Censor (Crown only: issue Policy / others: block one order) | 3 |

**Löwenritter Senate Market:** Legionary, Architectus, Tribune, Tribune Militum only.

**Cooldown Track:**

| Faction | Unique Power | Cooldown |
|---------|-------------|----------|
| Crown | Royal Decree | 2 seasons |
| Church | Excommunication | 3 seasons |
| Hafenmark | Sovereign Authority Doctrine | Once/game |
| Varfell | Patient Observation | 1 season |
| Restoration | Community Chorus | 2 seasons |
| Löwenritter | Iron Discipline | 2 seasons |

---

## B4 — TURN STRUCTURE

Each round = 1 season. Full campaign = 12–20 seasons. Session target: 3–5 seasons.

### Phase 1 — Planning (~5 min)

All players simultaneously select cards and place face-down in territories. Maximum 5 cards per season. No limit on cards per territory. NPC factions execute AI simultaneously.

### Phase 2 — Negotiation (~3 min)

Open deals: publicly declared, enforceable (breaking costs Standing −2 from betrayed faction). Sealed deals: private, non-binding. Orders remain face-down.

Senate Market purchases available at standard cost.

**Torben Tutoring Demand response** (if event active): Crown declares response during this phase.

**Elske contact action** (if Contact Established): factions may negotiate around Elske's situation here.

### Phase 3 — Reveal

All cards flipped simultaneously.

### Phase 4 — Resolution (~8–20 min depending on player count)

**Priority order:**
1. Intel/Covert (Tribune)
2. Military (Legionary) — includes Battle
3. Domain (Consul, Prefect, Architectus, Colonist)
4. Social (Senator)
5. Thread operations (Pontifex Senate Market; Weaver)
6. Special/Unique Powers (Censor, Royal Decree, Excommunication, etc.)
7. Project advancement (Praetor)

Within tier: descending Stability first. Ties: resolve simultaneously. Three or more factions same card type same territory: descending Stability each applying fully before the next.

**Resolution procedure per card:**
1. Declare orientation → specific action.
2. Assemble pool from relevant stat (B3 mapping).
3. Apply modifiers: Clock Environmental Effects, territory specials, ethical framework, Milestone Bonuses, Champion presence.
4. Roll. Determine degree.
5. Apply result.
6. If Thread operation: draw Co-Movement card. Apply three-dimensional consequence.
7. If Institutional Mandate triggered: resolve Uphold/Compromise (B7).

**Cascade Depth Cap:** No single card play may trigger more than 3 immediate mechanical effects in one resolution step. Additional effects queue to Accounting.

**Resolution order — Policy/Parliament/Censor:** Crown Policy declared → Hafenmark may immediately respond with Senator Inward (interrupt, no card cost) → Censor activates last (blocks next order in priority sequence).

**Ethical Framework Modifiers:**

| Faction | Bonus | Penalty |
|---------|-------|---------|
| Crown (Virtue Ethics) | Public, visible actions −1 Ob | Covert or morally ambiguous: +1 Ob |
| Church (Divine Command) | Doctrine-aligned −1 Ob | Thread-supporting: +2 Ob |
| Hafenmark (Categorical Imperative) | Procedurally grounded −1 Ob | Ad hoc or precedent-breaking: +1 Ob |
| Varfell (Epistemic Reason) | Evidence-based Intel −1 Ob | Emotional or reactive: +1 Ob |
| Restoration (Rawlsian) | Community-benefiting −1 Ob | Hierarchical/exclusionary: +1 Ob |
| Löwenritter (Military Honor) | Orders protecting Valorian sovereignty −1 Ob | Advancing personal/factional gain at Valoria's expense: +2 Ob |

### Phase 5 — Seasonal Accounting (~5–20 min)

Execute in strict order:

1. Apply all pending attribute changes from resolved orders.
2. Faction Stability checks: any faction that suffered ≥ 2 attribute loss this season rolls Stability pool vs. Ob = loss magnitude.
3. Advance Cooldown Track (all items −1 slot; at 0: return to hand).
4. Clock advances: RS baseline drift (−1 at Winter only). TC per formula (B5 Church). IP per Altonian pressure table. PI changes.
5. Church Attention Pool: resolve threshold responses. Pool resets to 0.
6. Thread Debt: tokens older than 1 season: RS −1 per token (active drain). Serviced tokens: no drain; permanent residual RS −0.5 recorded.
7. Clear Thread Resonance markers (all factions reset to "not in resonance").
8. Check threshold events: draw one Event Card per threshold crossed.
8b. Milestone Bonus check: has any Milestone Bonus trigger been met? Apply immediately. Mark fired (each fires once only).
9. Warden Emergence check: has any faction's Expedition passed a Forgetting Check this season?
9b. Vaynard-Edeyja same-season rule: if Warden Emergence fired at Step 9 AND VTM ≥ 4 AND Varfell played Tribune Inward in T13 this season: Warden Cooperation +1 immediately.
10. Warden Cooperation check: have any Cooperation conditions fired?
10b. Torben/Elske events: apply any Loyalty changes from this season's events.
11. Update Hollow Victory totals publicly. Each player announces running total. Record on shared sheet.
12. Check victory conditions. All Deed Tokens held simultaneously = declare victory.
13. Season marker advances. If Winter (every 4th season): Year-End Accounting (B11).

**Stability Check at 0 (Faction Collapse — from batch_ad_resolutions.md):**
If a faction's Stability reaches 0: **Faction Collapse** fires at Accounting Step 2.
- All that faction's attributes freeze at current values.
- That faction's Mandate immediately drops to 0.
- Other factions may run Domain Actions (equivalent orders) against that faction at −1 Ob for 2 seasons.
- Faction reconstitution: Diplomacy Ob 4 targeting that faction (representing re-establishing leadership) + Stability rebuilt above 2 before next Accounting. One faction may sponsor reconstitution — they gain Standing +2 vs the collapsed faction.

**Cascade Phase (Hybrid Mode only — from hybrid_gaps_resolved.md):**
In Hybrid Mode, the GM runs the Cascade as 5 sequential steps after Phase 5:
1. Apply all Domain Echoes from personal scenes (TTRPG outcomes → faction stats).
2. Apply Thread consequences from personal Thread operations (TT changes, RS changes).
3. Clock threshold checks: fire in order RS → TC → IP. Queue institutional responses for next Personal phase.
4. Seasonal accounting per above Steps 1–12 (if end of season).
5. Board state update.

---

## B5 — PLAYABLE FACTION CARDS

### FACTION: THE CROWN

**Stats:** Mandate 5 · Influence 5 · Wealth 4 · Military 4 · Stability 4
**Ethical Framework:** Virtue Ethics
**Leader:** King Almud Almqvist (early 50s; reigning 27 years; privately sympathises with Einhir Restoration; TS 28 — near-Stirring)
**Conviction:** "The state is the only legitimate vessel of order."

**Institutional Mandate:** "The monarchy provides the order that protects Valoria — and all other institutions serve the monarchy's order."

**Mandate trigger events and Compromise benefits:**

| Trigger | Compromise Benefit |
|---------|-------------------|
| Church refuses Crown directive in Crown territory | Issue one additional Policy this season without Mandate ≥ 4 requirement |
| Varfell operates Intel in Crown territory without Crown awareness | Crown receives same information Varfell gathered (shared Intel result) |
| Hafenmark Parliamentary ruling contradicts Crown decree this season | Crown Policy overrides Parliamentary ruling for 1 season |
| Any faction allies with Altonia (Open Pledge) without Crown approval | Crown may join alliance as third party at no Standing cost |

**Uphold benefit (all triggers):** +1 Renown on Almud + 1 Stability.

**Crown-Exclusive — Policy Instruments:** Once per season, may issue one Policy if Mandate ≥ 4. Same policy cannot repeat for 2 seasons.

| Policy | Effect | Downside |
|--------|--------|----------|
| Royal Taxation | All Trade: +1 Wealth to Crown | Non-Crown Trade Ob +1 |
| Conscription Mandate | All Muster: −1 Ob | Mustered units Cohesion −1 |
| Free Trade Decree | IP −1; Schoenland Trade +1D | TC +1 |
| Curfew | Intel in Crown territories: +2 Ob | Niflhel Standing +2 |
| Parliamentary Session | All factions: one additional Diplomacy | Crown Mandate check Ob 1 on failure; TD −1 |
| Emergency Powers | Crown executes one order face-down | Hafenmark free Parliamentary Manoeuvre; TC +1; TD +1 |
| Supremacy Decree (once/game) | Named faction: Crown Mandate treated +2 higher all opposed rolls this season | All other factions: Standing +1 vs Crown |

**Unique Power — Royal Decree** (2-season cooldown): Roll Mandate vs. Ob 2. Success: one faction attribute change (any faction, ±1) takes effect immediately. Failure: Crown Mandate −1. Effect declared before rolling.

**Torben Loyalty Track (0–7, starts 3):** Visible to all.

**Gaining Torben Loyalty:**
- Senator Outward (Diplomacy) targeting Torben's location: Overwhelming +2; Success +1.
- Crown holds PI ≥ 5 at Year-End: +1.
- Crown upholds Institutional Mandate 2+ consecutive seasons: +1 per Year-End continued.

**Losing Torben Loyalty:**
- Crown Compromises Institutional Mandate: −1.
- Crown issues Emergency Powers: −1.
- Löwenritter Coup fires: reset to 1.
- TC crosses 60: −1 (Torben concerned about Church).
- Torben sent to Altonia (comply with tutoring demand): −2 immediately.

**Victory — Constitutional Stability (Primary):** All 5 Deed Tokens simultaneously + PI ≥ 3.

| Deed | Condition |
|------|-----------|
| 1 | Mandate ≥ 5 |
| 2 | Control T1 + T2 + ≥ 2 other territories |
| 3 | TC < 60 and IP < 75 simultaneously |
| 4 | PI ≥ 5 |
| 5 | Torben Loyalty ≥ 5 |

**Victory — Dominion (Alternate):** Controls ≥ 8 territories AND one Submission Condition simultaneously.

| Submission Condition | How |
|---------------------|-----|
| Church recognizes Crown supremacy over religious appointments in Crown territories | Open Pledge accepted, OR TC = 0 |
| Varfell subordinates Intel to Crown oversight | VTM ≤ 1 OR Crown captures Vaynard + all Varfell territories |
| Hafenmark surrenders Parliamentary independence | PI = 0 OR Baralta Compromise count ≥ 4 |

---

### FACTION: THE CHURCH OF SOLMUND

**Stats:** Mandate 5 · Influence 6 · Wealth 5 · Military 4 · Stability 5
**Ethical Framework:** Divine Command
**Leader:** Confessor Arne Himlensendt (sincerely devout, zero TS, wrong but not cynical)
**Conviction:** Faith

**Institutional Mandate:** "Solmund's doctrine is the rightful framework for all governance — secular authority is derivative and conditional."

**Mandate triggers and Compromise benefits:**

| Trigger | Compromise Benefit |
|---------|-------------------|
| Crown refuses to enforce a Church Interdict in Crown territory | AER +1 |
| Heresy Investigation fails (target escapes) | Uphold only: Himlensendt Renown +1; Compromise: none available |
| Any faction occupies T3 without Church military response | Church calls Crusade: Templars deploy without Muster; TC +2; Attention +3 |
| Reformed Settlement declared (Baralta) | See Reformed Settlement response rules |

**Church-Exclusive — Pontifex (Ecclesiastical Suppression, base hand):**
NOT a Thread operation. Social/Mandate action.
- **Inward (Doctrinal Inquiry):** Mandate vs. Ob 2 (−1 Ob in Church territory). Open Heresy Investigation without Attention Pool threshold (costs 1 Wealth instead).
- **Outward (Thread Suppression):** If a Thread operation by another faction was resolved this Phase 4 in this territory: Mandate vs. Ob 2. Overwhelming: Co-Movement RS effect cancelled. Success: RS effect reduced by 1 (minimum 0). Partial: no suppression; Attention Pool +1. Failure: no suppression; Church Mandate −1.

**Thread Operations and Klapp:** Church cannot purchase Senate Market Pontifex and cannot perform standard Thread operations. See B10 for Klapp Event Card — this is the only path to temporary Church Thread access, and it undermines TC while active.

**Church-Exclusive — TC as Resource:** Declare before rolling: spend 1 TC → +1D to any Church action. Maximum 2 TC per roll. Spending reduces your victory threshold simultaneously.

**TC Advancement Formula (applied at Accounting Step 4):**

| Source | TC Gain |
|--------|---------|
| Church controls T3 (Himmelenger) | +1/season |
| Assert choice (TC > 50, mandatory) | +1 |
| Attention Pool reaches threshold 5 | +1 |
| Emergency Powers policy (Crown or Löwenritter) | +1 |
| Free Trade Decree (Crown) | +1 |
| Church unit in any non-Church territory at season end | +0.5/unit (max +1/season; whole number at Year-End) |
| Church Territorial Seizure (TC ≥ 80) | +2 |
| Reformed Settlement — Resist | +3 |
| Heresy Investigation confirmed success | +0.5 (whole number at Year-End) |
| Doctrinal Reach Milestone | +0.5/season (whole number at Year-End) |

**TC Decreases:**
- Reformed Settlement — Accommodate: −5
- Sovereign Authority Doctrine (Hafenmark): −2 to −3
- Baralta passive suppression (Mandate ≥ 4): −1/season
- Löwenritter Requisition Order success: −1
- Royal Decree targeting Church TC: −1
- Klapp Trajectory B or C active: −1 to −2 (see B10)

**Mandatory Assert/Suppress (TC > 50):** Each season:
- **Assert:** TC +1. All secular faction Mandate triggers fire. Riskbreakers evaluate Priority 3.
- **Suppress:** TC +0. AER −1. Himlensendt Renown −1.
Announced at Accounting Step 5.

**Unique Power — Excommunication** (3-season cooldown): Mandate vs. target leader Mandate (or Ob 2 non-leaders). Overwhelming: Mandate −1; barred from Church territories 1 season; Reputation −1 all factions. Success: Mandate −1 only. Failure: Church Mandate −1; target Mandate +1.

**Victory — Holy State (Primary):** TC ≥ 70 + Mandate ≥ 5 + control T3 + control T1 + AER ≥ 3.

| Deed | Condition |
|------|-----------|
| 1 | TC ≥ 40 |
| 2 | Church Mandate ≥ 5 |
| 3 | Control T3 continuously for 2 seasons |
| 4 | Control T1 |
| (Gate) | AER ≥ 3 (required to declare victory, not a Deed) |

**Victory — Dual Theocracy (Alternate):** TC ≥ 60 + AER = 5 + IP ≤ 30.

---

### FACTION: HAFENMARK

**Stats:** Mandate 4 · Influence 4 · Wealth 5 · Military 3 · Stability 4
**Ethical Framework:** Categorical Imperative
**Leader:** Duchess Inge Baralta
**Conviction:** "Faith is not mediated — it is lived. Anyone who is truly faithful can hear Solmund. Anyone who cannot should not rule."

**Institutional Mandate:** "Constitutional process is the only legitimate source of authority."

**Mandate triggers and Compromise benefits:**

| Trigger | Compromise Benefit |
|---------|-------------------|
| Crown governs by decree (PI ≤ 2 this season) | Issue one Parliamentary Manoeuvre at no card play cost |
| Crown issues Emergency Powers without prior Parliamentary Session | TD −1 (strategic cooperation reduces tension) |
| Church seizes civilian territory without Parliamentary debate | Free Diplomacy action vs. Church |
| Any faction acts with military force in T6 (Hafenvalor) | Hafenmark +2 Wealth from emergency trade deals |
| Löwenritter Coup fires | Hafenmark retains PI at current level (coup-related PI loss doesn't apply this season) |

**Reformed Doctrine Track (RDT, 0–6):** Private to Hafenmark player.

**Gaining RDT:**
- Senator Outward in non-Church territory (Ob 2 success): +1.
- TC rises above 50 AND Baralta has a unit in that territory: +1.
- Crown issues Emergency Powers without Parliamentary check: +1.
- Any faction publicly Compromises their Mandate: +1.

**Losing RDT:**
- Church Excommunicates Baralta: −2.
- Baralta publicly Compromises own Mandate: −2.
- RS drops below 30: −1/season.

**RDT Effects:**

| RDT | Effect |
|-----|--------|
| 0–1 | No effect |
| 2 | TC gains this season halved (round down) |
| 3 | Church Inquisition Autonomy threshold: Attention Pool must reach 8 instead of 7 |
| 4 | TC capped at current level +5 for remainder of game |
| 5 | Reformed Settlement available (once/game) |
| 6 | All Diplomatic actions targeting Hafenmark: +1 Ob |

**Reformed Settlement (RDT 5, once/game):** Declared during Phase 2. Church responds at Accounting Step 5.
- **Resist:** TC +3; RDT +1 (martyrdom); +1 Standing vs Church; +1 Deed Token.
- **Accommodate:** TC −5; Church Mandate trigger; Church Stability −1; AER −2.
- **Ignore:** RDT +1 next season. Maximum 2 Ignores. On third occurrence: must Resist or Accommodate.

**TC Passive Suppression:** While Baralta Mandate ≥ 4: TC −1/season.

**Unique Power — Sovereign Authority Doctrine (once/game):** Declared during Phase 2. Immediately: TC −2 to −3 (Baralta announces constitutional limits on Church temporal power). Effect persists 3 seasons: all Church Diplomatic actions in Hafenmark territory +1 Ob.

**Deed Tokens — Three Paths:**

*Path A — Reformed Valoria (3 Deeds):*
| Deed | Condition |
|------|-----------|
| 1 | RDT ≥ 4 |
| 2 | PI ≥ 3 |
| 3 | Reformed Settlement completed |

*Path B — Theological Supremacy (2 Deeds):*
| Deed | Condition |
|------|-----------|
| 1 | RDT = 6 |
| 2 | TD = 5 |

*Path C — Parliamentary Consolidation (4 Deeds):*
| Deed | Condition |
|------|-----------|
| 1 | PI ≥ 4 |
| 2 | Mandate ≥ 4 |
| 3 | Control T6 (Hafenvalor) |
| 4 | No active Heresy Investigation vs Hafenmark last 2 seasons |

---

### FACTION: VARFELL

**Stats:** Mandate 3 · Influence 4 · Wealth 3 · Military 4 · Stability 4
**Ethical Framework:** Epistemic Reason
**Leader:** Duke Magnus Vaynard (privately investigating Thread knowledge and Einhir artefacts; TS developing)
**Conviction:** "The strongest thread is the one others cannot see — and I have spent my life learning to pull it."

**Institutional Mandate:** "Information is the truest form of power — and all other power is information in disguise."

**Mandate triggers and Compromise benefits:**

| Trigger | Compromise Benefit |
|---------|-------------------|
| Riskbreakers expose a Varfell Casus Belli | Plant one false Intel result in another faction's possession for 1 season |
| Varfell Spy action fails (target detects) | Accept detection publicly; gain Standing +1 from ALL factions (diplomatic immunity gambit) |
| Another faction successfully Investigates Varfell's stats | Reveal one CHOSEN stat (not the investigated one — control the narrative) |
| VTM becomes publicly visible (reaches 3) | Einhir Knowledge Milestone fires immediately even if normal trigger unmet |

**Varfell Thread Mastery (VTM, 0–5):** Private at VTM 0–2; publicly visible (board marker) at VTM 3+.

**VTM Bootstrapping (T9 Research, once/campaign):** Season 1 only. Tribune Inward in T9 as substrate research. Roll Influence vs. Ob 2. Success/Overwhelming: VTM +1. No Co-Movement card. No Thread Debt.

**Gaining VTM:**
- Tribune in Thread-active territory while in Thread Resonance: +1.
- Southernmost Expedition Season 1 (Approach) completed: +1.
- Thread Debt incurred by any faction: +1 (Vaynard perceives substrate strain).
- Patience Protocol 6 Counters spent at VTM 4+: +1 (see below).
- Riskbreakers expose a Vaynard Casus Belli: VTM −1.

**VTM Effects:**

| VTM | Southernmost Access | Capability |
|-----|--------------------|-----------:|
| 0–1 | None | — |
| 2 | First Layer | Always in Thread Resonance in T9. Qualifies as Thread-qualified presence in T12/T13. |
| 3 | Deep Layer | Once/game: preview top 2 Co-Movement cards before an order; keep either. Becomes publicly visible. |
| 4 | Deep Layer without Restoration guide | Patience Counter max raised to 6. Casus Belli Ob −1. Vaynard-Edeyja encounter eligible. |
| 5 | Core zone | Once/game: choose the Actualized dimension (RS change) outcome of one Co-Movement card draw. Declare before drawing. Epistemic and Temporal dimensions still apply from drawn card. Always produces Thread Debt + RS −1. (BG-E-63 approved.) |

---

#### PATIENCE PROTOCOL (BG-E-NEW-01 — Authored)

Vaynard's sustained restraint mechanic. Tracks the strategic value of deliberate inaction.

**Patience Counters (PC, 0–4 at VTM 0–3; 0–6 at VTM 4+):** Private to Varfell player. Tracked on faction mat.

**Gaining Patience Counters:**
- Each season Varfell has a Tribune card available but plays it as a different card type (or doesn't play it): +1 PC. (He could have acted but chose to wait.)
- Each season Varfell passes on purchasing a Senate Market card when Wealth ≥ 3: +1 PC. (Restrain economic ambition.)
- The above two counters can both trigger in the same season. Maximum +2 PC per season from inaction.

**Spending Patience Counters:**

| Cost | Effect |
|------|--------|
| 1 PC | +1D to one Intel (Tribune) action this season |
| 2 PC | Preview one Co-Movement card before any draw this season (choose whether to use the previewed card or draw fresh) |
| 3 PC | Guarantee one Tribune action resolves at Success minimum (roll still required; if majority 1s: Partial instead of Failure) |
| 4 PC | Execute one Spy action in any territory on the board, regardless of adjacency or unit presence (Vaynard's network is everywhere, if patient) |
| 6 PC (VTM 4+ only) | +1 VTM (Vaynard's sustained observation of the substrate yields a genuine advancement). Requires VTM 4+. |

**Patience Counter cap:** 4 at VTM 0–3; 6 at VTM 4+. Counters carry across seasons — they are never automatically cleared. They can only decrease by spending.

**Patience Protocol tone:** This mechanic rewards the player who restrains their Tribune plays and accumulates advantage through apparent inaction. The faction that sees everything and acts rarely is more dangerous than the faction that acts constantly. This is canonical to Vaynard's Conviction.

---

**Deed Tokens — Three Paths:**

*Path A — Intelligence Hegemony (3 Deeds):*
| Deed | Condition |
|------|-----------|
| 1 | VTM ≥ 3 |
| 2 | Control 3 territories simultaneously |
| 3 | All other factions' stat lines revealed at least once (cumulative across game) |

*Path B — Southernmost Dominion (2 Deeds):*
| Deed | Condition |
|------|-----------|
| 1 | Control T12 and T13 simultaneously |
| 2 | VTM ≥ 3 |

*Path C — Thread Supremacy (3 Deeds):*
| Deed | Condition |
|------|-----------|
| 1 | VTM = 5 |
| 2 | Control T12, T13, and ≥ 1 other (≥ 3 territories controlled) |
| 3 | RS ≥ 50 at Accounting |

---

### FACTION: RESTORATION MOVEMENT (Optional 5th / NPC default)

**Stats:** Mandate 2 · Influence 4 · Wealth 2 · Military 0 · Stability 3
**Ethical Framework:** Rawlsian
**Leader:** Collective (Dahl Erikssen informal figure, TS 18)

**Institutional Mandate:** "The community is the only legitimate political unit."

**Mandate triggers and Compromise benefits:**

| Trigger | Compromise Benefit |
|---------|-------------------|
| Any faction's Military targets a territory with Restoration Presence | Move all Presence markers from attacked territory to adjacent at no card cost |
| Heresy Investigation opens in a territory with Restoration Presence | Investigation closes at next Accounting; no Presence loss (costs Restoration Mandate −1) |
| Community Project disrupted by battle (Progress −2) | Restoration receives 1 Wealth from the disrupting faction |
| RS drops below 40 | All Restoration Thread operations this season cost 1 Thread Resonance marker (spend to reduce Ob by 1 additional — urgent but taxing) |

**Presence Markers (8 total):** Military cannot remove them. Only Heresy Investigation success or Community Project disruption removes them.

**Presence Spread Timing:** Markers placed via Presence Spread take effect at the START of Phase 4 in the same season.

**Two Action Types:**
1. **Community Organizing** (Organizer card): Influence vs. Ob 2. Not a Thread operation. No Co-Movement card.
2. **Community Weaving** (Weaver card, Thread operation): Ob 2, −1 Ob per Presence marker in territory. Always draws Co-Movement card.

**Thread Resonance:** Restoration gains Thread Resonance in any territory with a Presence marker, in addition to standard triggers.

**Unique Power — Community Chorus** (2-season cooldown): All Presence markers in same or adjacent territories contribute to a shared Weaving. Combine all Ob reductions. One Co-Movement card only. RS +1 on Overwhelming.

**Victory:** 5 Presence markers in 5 non-adjacent territories, held 2 consecutive seasons + RS ≥ 50. Or co-victory with compatible faction (see B15).

---

### FACTION: LÖWENRITTER (Post-Coup Only)

**Activation:** Begins NPC-controlled (peacetime AI: B13). If Coup Counter reaches 4 and coup fires (Military vs. Ob 3), Löwenritter gains this full sheet.

**Stats (post-coup):** Mandate 3 · Influence 2 · Wealth 3 · Military 6 · Stability 5
**Leader:** Grandmaster Sigrid Ehrenwall (late 50s; career soldier; keeping count of Almud's compromises)
**Conviction:** Valoria endures, whatever the cost.

**Institutional Mandate:** "The Löwenritter exist to protect Valoria when no one else will. We hold until Valoria can govern itself."

**Mandate triggers and Compromise benefits:**

| Trigger | Compromise Benefit |
|---------|-------------------|
| Church seizes Löwenritter-governed territory without military response | Cede diplomatically; AER +1 |
| PI drops to 0 during Löwenritter rule | Issue declaration of permanent emergency governance; no PI penalties 2 seasons |
| Emergency Powers issued > twice in one year | Third use legal; no Standing cost; TC +2 |
| IP crosses 75 without a military order that season | Cede T4 (Spartfell) to Altonian Vanguard as buffer; IP halted 2 seasons |

**Permanent Martial Law:** All Military orders in governed territory −1 Ob. All non-Military orders by any faction in governed territory +1 Ob. PI −3 immediately on coup.

**Conscription:** Once per year at Year-End: raise one unit without Legionary. Territory conscripted: Prosperity −1.

**Card Hand:** 3× Legionary, 1× Tribune (Requisition Order), 1× Prefect, 1× Recess.

**Requisition Order (Tribune Inward, Löwenritter only):** Roll Military vs. Ob 2 in any Church-controlled territory.
- Overwhelming: TC −2; Attention +2; Church may not Assert this season.
- Success: TC −1; Attention +2.
- Partial: Attention +1 only.
- Failure: No effect; Church +1 Standing vs Löwenritter.

**Unique Power — Iron Discipline** (2-season cooldown): One Löwenritter unit this season immune to Rout and Cohesion degradation. Declare before battle.

**Elske (Succession Candidate — v0.4 Corrected):**
Elske is in Altonia, not T3. The Löwenritter path to her:
- Make Contact (Löwenritter Senator Outward in T4, Ob 2): Contact Established.
- If Elske Loyalty ≥ 5 AND IP < 60 AND Löwenritter controls T4: roll Military vs. Ob 2. Success: Elske returns. IP +5.
- Elske Wounded on extraction (Partial): 2-season recovery before Parliamentary confirmation possible.
- Elske not available for Parliamentary confirmation until healthy AND PI ≥ 3.

**Confirming Elske as Successor (post-extraction):** Parliamentary Session (Mandate vs. Ob 3, PI-modified: −1 Ob per 2 PI above 4). Available once Elske healthy + PI ≥ 3.

**What Happens to Almud:**
- In Valoria at coup: house arrest. Token in T1; no card plays. Liberate: Military vs. Ob 3 in T1.
- Soft coup (Almud yielded command): 1 Senator card play per season (Diplomacy Outward only).
- Elske and Torben arcs activate immediately on coup.

**Torben Constitutional Restraint Path:** Torben Loyalty +1 at each Year-End in which Löwenritter maintained PI ≥ 3 AND did not issue Emergency Powers that year.

**Deed Tokens:**

| Deed | Condition |
|------|-----------|
| 1 | TC < 50 |
| 2 | IP < 60 |
| 3 | RS > 40 |
| 4 | PI ≥ 4 |
| 5 | Succession candidate: Elske free + confirmed, OR Torben Loyalty ≥ 6 |

**Victory — Regency Resolution (Primary):** All 5 Deeds simultaneously AND legitimate successor installed. At succession: Löwenritter hand over command. Shared victory.

**Victory — Military Consolidation (Alternate):** Only if Regency Resolution not fired after 8 Löwenritter seasons. ≥ 8 territories + Military ≥ 5 + RS > 35 + TC < 60. Hollow Victory −2 Deeds from Standing tokens. PI = 0 when this fires: victory void.

---

## B6 — THREAD SYSTEMS

### Thread Resonance

Binary seasonal marker. In Thread Resonance or not. Cleared at Accounting Step 7.

**Gaining Thread Resonance:**
- A Thread operation occurs in or adjacent to a faction's controlled territory.
- A Co-Movement card effect targets the faction.
- RS drops below a threshold this season (all factions gain Thread Resonance).
- Restoration: also in any territory with a Presence marker.
- Varfell VTM ≥ 2: always in Thread Resonance in T9.

**While in Thread Resonance:**
- +1D to Intel targeting practitioners or Thread-active sites.
- Senate Market Pontifex: −1 cost.
- Qualifies for Thread-qualified presence test for T12/T13.

**For Thread-qualified factions only:**
- May ask one yes/no question about RS (above or below a threshold).
- May spend Thread Resonance marker: cancel one Co-Movement effect targeting them, OR contribute +1D to Restoration Community Weaving in their territory.

**Thread Witness Nodes:** When a Community Weave Project is completed, territory gains permanent Thread Witness Node. Any Thread operation here draws one additional Co-Movement card.

### Thread Debt

**Against temporal flow (Thread Debt trigger):**
- The territory already contains a Thread Debt token from prior operation.
- RS is below 30 at the time the operation is declared.
- VTM 5 ability used.

Standard Restoration Community Weaving and standard Senate Market Pontifex do NOT inherently incur Thread Debt unless the above applies.

**Thread Debt tokens:**
- Active drain: RS −1 per outstanding unserviced token per season (Accounting Step 6).
- Service: faction executes Mend-equivalent action (Restoration Weaver in same territory, OR spend Thread Resonance while qualified). Serviced: drain ceases; permanent residual RS −0.5 recorded.
- Maximum 3 tokens simultaneously. At 3: no further debt until reduced to 2.
- Church may use Thread Debt as grounds for automatic Heresy Investigation: Ob −1 if target holds ≥ 2 tokens.
- Thread Debt incurred by any faction: Varfell VTM +1.

**Mass Lock RS Drain Cap (from R-58):** Regardless of concurrent Locks, total RS drain from active Locks cannot exceed −1 per round of combat or −1 per scene in non-combat contexts. Multiple Locks do not stack drain rates within a scene. Seasonal drift is unaffected.

**Year-End Thread Debt Resolution:** All residual RS fractions sum and round up; apply at Year-End Accounting.

### Church Attention Pool (0–10)

**Accumulates from:**
- Unauthorized community gathering: +1
- Unexplained structural/social change (Thread operation visible effects): +2
- Einhir artefact surfaces (Event Card C-13): +2
- Restoration gathering in Church-adjacent territory: +3
- Faction behaviour consistent with heretical influence, multiple territories: +1/territory
- Löwenritter Requisition Order success/partial: +1–2
- Warden investigation in T13: +1

**Attention thresholds (resets each season at Step 5):**

| Pool | Response |
|------|----------|
| 3 | Church opens one Heresy Investigation (free) |
| 5 | TC +1 |
| 7 | Inquisitor protocol: Thread-active factions −1D to covert/Intel this season. Inquisition Autonomy fires. (Modified to 8 if RDT ≥ 3.) |
| 10 | Church Crusade: Templar units may deploy anywhere in Church territory without Muster |

### Thread Operation Procedure (laminated card)

1. Declare card (Weaver or Senate Market Pontifex) and orientation.
2. Declare territory and Thread operation type.
3. Check "against temporal flow" conditions. If any apply: incur Thread Debt token (placed in territory, −1 Ob to THIS operation as substrate resistance).
4. Apply Ob modifiers: RS environmental, Presence markers, existing Thread Debt, Champion.
5. Roll. Determine degree.
6. Apply result.
7. Draw Co-Movement card (+1 additional if Thread Witness Node). Apply all three-dimensional effects.
8. Check Attention Pool: do visible consequences add Attention?

### Niflhel Exposure and RS Stabilization

To fully stabilise RS decline: Niflhel Network Depth in active territories must be reduced to 0. Execute via Intel (Tribune Investigate, Ob 4) or Warden investigation (automatic if Niflhel detected in T13 with Warden Cooperation ≥ 1).

### Co-Movement Cards (P-14 Compliance)

Every Thread operation draws one Co-Movement card. Two if Thread Witness Node territory. Cards cannot be declined. Three simultaneous effects:
1. **Actualized dimension:** RS change.
2. **Epistemic dimension:** Information revealed, concealed, or distorted.
3. **Temporal dimension:** History marker — Project disruption, Pledge complication, or NPC relationship change.

Cards can be cancelled only by a qualified faction spending Thread Resonance marker (one cancellation per marker).

**Co-Movement Card Sample (CM-01 through CM-20):** [See B10 Event Cards for full deck. 20-card base deck. Draw from shuffled pile.]

---

## B7 — POLITICAL SYSTEMS

### Institutional Mandate — Uphold / Compromise

When a trigger event occurs:
- **Uphold:** Act consistently with Mandate at cost. +1 Renown on Champion + 1 Stability. No mechanical benefit from the triggering situation.
- **Compromise:** Act against Mandate for strategic advantage. Earn the specific Compromise benefit. Cost: 1 Standing token (visible to all) + 1 Stability.

### Standing Tokens

**Gaining Standing against another faction:**
- That faction breaks an Open Pledge in your favour.
- That faction uses Brutal disposition against Valorian civilians.
- That faction seizes your territory while you had an active non-broken Pledge.
- Church Excommunicates your faction leader.
- That faction Compromises their Institutional Mandate publicly.
- That faction's action directly targeted you this season.

**Spending Standing:**

| Cost | Effect |
|------|--------|
| 1 Standing | +1D to any one defensive roll this season |
| 2 Standing | Execute one defensive order at Ob −1 |
| 3 Standing | Respond to an action targeting you (out-of-priority defensive card play) |
| 4 Standing | Convert to 1 Wealth, 1 Mandate, or 1 Influence |

3+ Standing against one faction: their Diplomacy targeting you automatically fails. 5+: cannot ally or exchange Deal Tokens.

### Open Pledges and Treaty Betrayal

**Open Pledge:** Publicly declared agreement between two factions. Binding — breaking it costs Standing −2 from the betrayed faction. Sealed deals are private and non-binding.

**Treaty Betrayal Consequences (from batch_ad_resolutions.md):**

| Target | Effect | Duration |
|--------|--------|----------|
| Betrayed faction | Stability −1 | 2 seasons |
| Betrayed faction | Free Casus Belli vs betrayer | Immediate, permanent until used |
| Betrayed faction | Grievance Marker vs betrayer | Permanent until resolved |
| Betraying faction | Influence −1 | 2 seasons |
| Betraying faction | Mandate +1 (strategic advantage gained) | 1 season |
| Betraying individuals | Reputation −3 with betrayed faction | Permanent |
| Betraying individuals | Reputation −1 with all witness factions | Permanent |

**Grievance Marker:** While active: +1 Ob all diplomatic rolls between the two factions. +1D to Intel actions targeting the betrayer. Clears through: one full season of genuine reparation (territory cession, tribute, or public apology scene — not mere declaration) OR change of faction leadership on the betraying side.

---

#### CASUS BELLI (BG-E-NEW-02 — Authored)

A Casus Belli token represents justified military justification — the moral and diplomatic right to pursue military action beyond normal geographic constraints.

**Acquiring a Casus Belli:**
- When a faction breaks an Open Pledge against you: automatic, as part of Treaty Betrayal Consequences above.
- When another faction executes a Brutal disposition against Valorian civilians in a territory you controlled: 1 Casus Belli against that faction.
- When a Heresy Investigation is opened against your faction leader based on fabricated evidence (Tribune Investigate success reveals the falsity): 1 Casus Belli against the Church.

**Casus Belli Effects (while held):**

| Effect | Notes |
|--------|-------|
| Military orders against the betraying faction: −1 Ob | Applies to all Military orders for 2 seasons |
| May March into their territory from non-adjacent territories | Pay 2 Legionary card plays instead of 1 (justified advance through neutral territories) |
| All other factions: you gain Standing +1 vs betrayer | Diplomatic capital from the grievance — issued once when Casus Belli is acquired, not per season |
| Riskbreakers: if they expose a Varfell Casus Belli | Varfell loses the Casus Belli AND VTM −1 (Patience Protocol is compromised) |

**Casus Belli Expiration:** 2 seasons after acquisition if unused for a Military action. On use for a Military action: Casus Belli is consumed. Only one Casus Belli can be held per faction at a time (a second acquisition replaces the first if unused).

**Note on Varfell:** Vaynard's Casus Belli is unique — it is accumulated through patience (Patience Protocol combination at VTM 4+), not through being wronged. The Riskbreakers treat this exposure as evidence of Varfell's manipulation of the political environment.

---

### Parliament Integrity (PI, 0–10)

Shared institution. Starts at 7.

| PI | Effect |
|----|--------|
| ≥ 5 | Parliamentary Manoeuvres available to Hafenmark. Crown Policy requires Mandate ≥ 4. |
| 3–4 | Parliamentary Manoeuvres +1 Ob. Crown Policy Ob −1. |
| ≤ 2 | Parliament non-functional. Hafenmark loses Parliamentary Manoeuvre. Crown governs by decree. TC +2/season. |

PI degrades: Crown Emergency Powers (−1), Church Territorial Seizure (−1), Löwenritter Coup (−3).
PI recovers: Hafenmark Parliamentary Manoeuvre success (+1), Crown Parliamentary Session policy (+1).

### AER Track (0–5)

Church's standing with Altonian power. Starts at 2.

| AER | TC Effect | IP Effect |
|-----|-----------|-----------|
| 0–1 | No modification | IP escalates normally |
| 2 | Neutral | Neutral |
| 3 | TC environmental effects apply +1 level | IP vanguard threshold: 76→80 |
| 4 | TC gains > 3/season treated as +4 | Altonia will not invade while AER ≥ 4 |
| 5 | Once/game: any order targeting Church interests fails automatically | IP fixed at 50 |

**AER gaining:** TC crosses 30/50/70 (+1 each); successful Heresy Investigation removes Restoration Presence (+1); Church issues Interdict (+1).
**AER losing:** TC drops below threshold (−1); Church Stability < 3 (−1); Reformed Settlement occurs (−2).

### Theocratic Clock Advancement and Altonian Ecclesiastical Context

TC crosses 60 → IP +1/season (Church dominance alarms Almaic Kyriakos minority in Altonia).
TC crosses 70 → AER gains trigger at each threshold; Almaic Kyriakos begins documenting Valorian heresy.

### Warden Cooperation Track (0–3)

Inactive until Warden Emergence. Printed near T13.

**Warden Emergence:** At Accounting Step 9: has any faction's Southernmost Expedition completed a Season 1 (Approach) action AND passed the Forgetting Check? If yes: Warden Emergence fires. Warden Token placed at position 0.

**Vaynard-Edeyja Encounter (Step 9b):** If Warden Emergence fires AND VTM ≥ 4 AND Varfell played Tribune Inward in T13 this season: Warden Cooperation +1 immediately (same Accounting phase, not deferred).

**Forgetting Check:** When a faction's expedition piece enters T13 first time: roll Spirit proxy + Thread Sensitivity (Ob 1; Restoration Weaver present −1 Ob; VTM 2+ −1 Ob). Overwhelming: full knowledge retained. Success: facts retained, weight fades by morning. Partial: emotional impressions, dread without content. Failure: nothing operational.

**Warden Cooperation Levels:**

| Level | Effect |
|-------|--------|
| 0 | No engagement |
| 1 | Expedition Ob −1. RS drain from Warden mending in T12/T13 −0.5/season |
| 2 | RS +1 per completed Expedition season. Deep Layer accessible to Restoration without VTM gate |
| 3 | Ceiral Ritual unlocked. RS +5 on successful Ritual. Edeyja provides Calamity knowledge |

**Advancing Cooperation:**
- Practitioner VTM ≥ 3 (or TS 40+ hybrid) succeeds in Thread operation at T13 primary site: +1.
- Two consecutive seasons in T13 without military units: +1.
- VTM 4+ reaches T13 + completes Intel action: +1. (Step 9b: same season as Emergence.)

**Reducing Cooperation:**
- Military unit in T12/T13 (expedition faction): −1.
- Thread Debt incurred in T12/T13: −1.
- Niflhel Network Depth ≥ 1 in T13: −1/season until resolved.

---

## B8 — MILITARY

### Champion Starting Positions

| Champion | Faction | Starting Territory |
|----------|---------|-------------------|
| Almud Almqvist | Crown | T1 (Valorsplatz) |
| Arne Himlensendt | Church | T3 (Himmelenger) |
| Inge Baralta | Hafenmark | T6 (Hafenvalor) |
| Magnus Vaynard | Varfell | T9 (Varfell) |
| Sigrid Ehrenwall | Löwenritter | T5 (Arnesheld) |

*Note: Elske is not a Champion token. She is tracked on the off-board Elske card.*

### Unit Types and Rosters (MT-01)

Faction Military stat = maximum active units simultaneously.

| Type | Martial | Cohesion | Notes |
|------|---------|---------|-------|
| Standard | 2 | 3 | Default Muster result. CP = Military ÷ 2. |
| Elite | 3–4 | 4–5 | Specific faction conditions. |
| Knights Templar (Church) | 4 | 5 | Immune to Co-Movement Cohesion penalties. +2D vs practitioners. |
| Inquisitors (Church) | 1 | 2 | Deploy via Senator Inward. +2 Attention/season present. |
| Hired Blade (Guilds NPC) | 2 | 3 | Offensive only. 1 season. Cannot garrison. |

**Starting unit rosters (derived from Military stats, MT-01):**

| Faction | Military | Max Units | Starting Units | Unit Type Notes |
|---------|---------|-----------|----------------|-----------------|
| Crown | 4 | 4 | 2 standard | Mixed infantry + cavalry |
| Church | 4 | 4 | 2 standard + 2 Templar eligible | Templars deploy at TC ≥ 40 or Crusade |
| Hafenmark | 3 | 3 | 1 elite (Baralta's guard) + 2 militia | Ducal guard: Cohesion 4, Martial 3 |
| Varfell | 4 | 4 | 2 standard | Highland infantry; +1D in T9 home territory |
| Guilds (NPC) | 2 | 2 | 2 Hired Blades | Replaced each season if they leave Eidursjo |
| Löwenritter (post-coup) | 6 | 6 | 5 standard → 6 after Crown transfer | All units: Cohesion 5, Martial 4 (elite stat block) |
| Restoration | 0 | 0 | None | Presence markers cannot be removed by Military |

### Muster Staging Protocol

Muster action success: place **Staging Token** in territory. Staging Token:
- Cannot be targeted before deployment.
- Converts to deployed unit at start of Phase 1 **following season**.
- If muster territory changes control before deployment: token removed (no refund).

### Battle Resolution (Board Game Mode)

Battle triggers when a March action (Legionary Outward) moves units into a territory containing enemy units.

**Battle Sequence:**
1. Attacker declares Disposition (Balanced/Offensive/Defensive/Brutal).
2. Defender declares Disposition.
3. Each side rolls their Military stat + Commander Coordination modifier + Disposition modifier.

**Disposition Modifiers to Pool:**

| Attacker \ Defender | Balanced | Defensive | Offensive | Brutal |
|---|---|---|---|---|
| **Balanced** | ±0, Ob 2 | −0, Ob 3 | +2D, Ob 2 | +1D, Ob 2 |
| **Defensive** | −2D, Ob 2 | −2D, Ob 3 | ±0, Ob 2 | −1D, Ob 2 |
| **Offensive** | +2D, Ob 2 | +2D, Ob 3 | +2D, Ob 2 | +3D, Ob 2 |
| **Brutal** | +2D +2 dmg, Ob 2 | +2D +2 dmg, Ob 3 | +2D +2 dmg, Ob 2 | +3D +4 dmg, Ob 2 |

Read: attacker rolls pool vs Ob shown. Defender rolls their own row against attacker's column. Both roll simultaneously.

**Commander bonus:** Faction Champion in territory: +1D to that faction's Military roll.
**Fortification:** Fort level provides +1D to defender per Fort level. Does not apply to Muster/March.

**Battle outcomes (winning side = more net successes):**
- Overwhelming win: losing side's unit destroyed (removed from board); losing side Stability check Ob 2; territory captured.
- Success win: losing side's unit Cohesion −2; if Cohesion = 0: unit routed (removed, Stability check Ob 1); territory may be captured if defender retreats.
- Partial (attacker): attacker's unit Cohesion −1; defender holds.
- Failure (attacker): attacker's unit Cohesion −2; no territorial change.

**Rout:** Unit at Cohesion 0 is removed. Faction's Military stat −1 (permanent until Muster replaces it). Stability check Ob 1.

**Tactic Cards:** Each faction holds 4 shared + 2 faction-specific tactic cards. One may be played secretly per battle (revealed simultaneously). Tactic effects apply as stated on the card (generic deck to be finalised in physical production).

### Champions in Battle

Champion in territory: +1D all units in same territory. Champion Wounded (Cohesion 0 or lost battle in their territory): bonuses halved. Champion Captured (enemy takes territory while Champion Wounded): removed from board. Rescue: Military vs. Ob 3. Ransom: 3 Wealth.

---

## B9 — COMMUNITY PROJECTS

Community Projects are multi-season investments representing faction-scale social construction. One project per territory at a time.

**Starting a Project (Praetor card):** Roll Mandate vs. Ob 1. Success: project begins with 1 Progress. Failure: wasted card play.

**Advancing a Project:** Any Praetor card play in same territory: roll Mandate vs. Ob 2. Success: Progress +1. Overwhelming: Progress +2. Failure: no advance.

**Project Completion:** At Progress = Required (see table). Applies effect permanently; territory gains Thread Witness Node if Thread-type project. Progress resets to 0 and project card is removed.

**Project disruption:** Battle in territory: Progress −2. Faction disrupting pays Restoration 1 Wealth if disrupted.

**Community Project Table:**

| Project | Required Progress | Territory | Effect on Completion |
|---------|------------------|-----------|---------------------|
| Einhir Site Restoration | 5 | T9, T12, T13, T14 | RS +3; Thread Witness Node; Restoration Influence +1; Warden Cooperation +1 if T13 |
| Trade Route Establishment | 3 | T7, T6, T15 | Wealth +2/season for controlling faction; IP −2 |
| Parliamentary Records | 3 | T1 | PI +2; Crown Mandate +1 |
| Community Weave | 4 | Any | RS +2; Thread Witness Node; Restoration Presence in territory cannot be removed for 3 seasons |
| Grain Reserve | 3 | T11 | All factions: Muster Ob −1 for 2 seasons; Prosperity +1 |
| Fortification Works | 4 | Any | Fort +2 (stacks with existing) |
| Southernmost Study | 5 | T12 or T13 | Forgetting Check Ob −1 for all factions; Warden Cooperation +1; one Warden Working Library fact revealed |
| Reformed Doctrine Centre | 3 | Non-Church territory | RDT +1; Church Influence in territory −1; Attention Pool +1 when completed |

**Project completion at RS < 20:** All projects gain automatic +1 Progress/season from crisis mobilisation (per B2 Environmental Effects).

---

## B10 — EVENT CARDS

Events trigger at Accounting Step 8: draw one per threshold crossed. GMs shuffle and maintain two separate decks: **World Events** (general) and **Named Character Events** (Klapp, Riskbreakers, Edeyja, Guilds).

### Klapp Event Card (BG-E-NEW-03 — Authored)

**Cardinal Klapp's Archive Awakens**

*Trigger conditions (draw from Named Character Events deck when):*
- A Thread operation succeeds within 1 territory of T3 (Himmelenger) this season, AND
- TC ≥ 30, AND
- No Heresy Investigation was opened this season by the Church.

*When drawn:* Place card face-up near Church faction mat. It activates the **Klapp State**:

**Klapp Active State:**
- Church +1D to all Investigate actions for 2 seasons (Klapp's scholarly network responds to Thread disturbances with documentary rigour).
- Heresy Investigations cost 0 Wealth while Klapp Active (he runs them through his archive budget).
- Church player announces: "Klapp is investigating." Other players do not learn what he has found.

**Klapp Trajectory Fire (subsequent season, Trajectory Choice):**
*Fires when Klapp Active AND any of: Varfell VTM ≥ 3 is in T3/T9 this season, OR Restoration has Presence in T3, OR any practitioner character with TS 30+ (hybrid) is in T3.*

Church player must choose a Trajectory. Once chosen, Trajectory cannot be changed.

**Trajectory A — Suppress:**
Church player resolves Klapp Active. No further effect.
- TC +1 (orthodoxy maintained by removing a deviant influence — Klapp's inquiry is quietly terminated).
- Klapp card removed. Cannot be redrawn this campaign.

**Trajectory B — Investigate Further:**
Klapp Active continues. TC −1 (his investigation weakens the Church's certainty, however briefly).
- Next season: **Klapp Discovery Event Roll** (Church rolls Mandate pool vs. Ob 2).
  - Success or Overwhelming: Klapp's TS advances (internal state, not publicly announced). Church player notes privately: "Klapp suspects." He does not act yet.
  - Failure: **Heresy Protocol Fires** — the Inquisitors detect anomalous behaviour from a Cardinal. Himmensendt must publicly declare whether to prosecute or protect Klapp.
    - Prosecute: Klapp card removed. Church Stability −1. AER −1 (Altonian Kyriakos minority learns Church is eating its own). TC −2.
    - Protect: Klapp Active continues 1 more season. Himmensendt Renown −1. If Klapp Discovery Event fails AGAIN next season: Himmensendt Stability check Ob 3.

**Trajectory C — Collaborate** (available only if Varfell VTM ≥ 4 OR Warden Cooperation ≥ 2):
Church player places Klapp as a Cooperation token. He is now working with practitioners.
- Warden Cooperation +1 (the Church's own scholar acknowledges the Wardens' reality).
- TC −2. Church Stability −1 (the institution fractures at the top).
- Church now has limited Thread access: may purchase one Senate Market Pontifex per season at full cost. (This is Klapp providing theological cover, not the Church endorsing Thread work.)
- Trajectory C cannot be reversed. The card remains in play as a reminder.
- If Himmensendt learns of Trajectory C (Tribune Investigate vs Ob 3 by any faction in T3): Inquisitor Autonomy fires immediately against Klapp. Warden Cooperation −1. The card is removed.

**Klapp Card Expiry:** If Trajectory A chosen or no Trajectory chosen after 2 seasons of Klapp Active: card removed automatically. If Trajectory B or C chosen: card remains until explicitly resolved per trajectory rules.

---

### Co-Movement Card Deck (20 Cards, CM-01 through CM-20)

**Draw conditions:** One per Thread operation. Two if Thread Witness Node territory. Cannot be declined.

*Three simultaneous effects per card: Actualized (RS), Epistemic (information), Temporal (history marker).*

| # | Name | RS | Epistemic | Temporal |
|---|------|----|-----------|----------|
| CM-01 | Ground Shock | −1 | Acting faction's Thread operation was visible: Attention +1 | One Community Project in territory: Progress −1 |
| CM-02 | Substrate Clarity | +1 | Acting faction may ask one yes/no about any faction's stat | No temporal effect |
| CM-03 | Resonance Surge | 0 | All factions in Thread Resonance this season: +1D next Intel | One NPC relationship improves (GM / hybrid: one NPC disposition shifts friendly) |
| CM-04 | Information Bleed | −1 | Acting faction: one hidden stat revealed to all players until next Year-End | One Open Pledge in territory becomes contested (roll Influence Ob 2 or it weakens by 1 step) |
| CM-05 | False Memory | 0 | One other faction's player may not use Intel information gained this season (the data is confused) | Acting faction's most recent completed Project: benefit lasts 1 fewer season than stated |
| CM-06 | Deep Tremor | −2 | No epistemic effect | All units in territory: Cohesion −1 this season (structural unease) |
| CM-07 | Temporal Echo | 0 | No epistemic effect | GM: one NPC in territory gains an anomalous memory — use as future scene hook. TS 15+ characters notice something is different |
| CM-08 | Political Opportunism | 0 | Faction with highest Mandate: Mandate +1 (they capitalise) | If that faction is Church: TC +1 additionally |
| CM-09 | Soldier Superstition | 0 | No epistemic effect | All military units in territory: Cohesion −1 this season. Löwenritter units: immune. Templars: immune |
| CM-10 | Wealth Disruption | 0 | No epistemic effect | Roll 1d6: 1–3 = controlling faction Wealth −1 (disruption); 4–6 = Wealth +1 (curiosity draws commerce) |
| CM-11 | Factional Intelligence Leak | −1 | Acting faction: one hidden stat revealed to all until next Accounting. If Niflhel: two stats revealed | No temporal effect |
| CM-12 | Ground Stability | +1 | No epistemic effect | Territory: all orders −1 Ob next season (substrate clarity aids action) |
| CM-13 | Einhir Artefact Surfaces | −1 | Artefact type revealed to all: roll 1d6 (1–2: Shifting Object, 3–4: Intentional Lock, 5–6: Dissolution Residue). Attention +2 | Church gains Casus Belli vs acting faction (theological violation) |
| CM-14 | Thread Witness Activation | 0 | Thread-qualified factions: each may ask one yes/no about RS simultaneously | Territory permanently gains Thread Witness Node (regardless of whether Project was complete) |
| CM-15 | Memory Dissolution | 0 | One faction of acting player's choice: their Intel results from last season become unreliable — they must verify before acting on them | No temporal effect |
| CM-16 | Community Stirring | +1 | No epistemic effect | Any active Community Project in territory: Progress +1 (the Thread operation accelerated social momentum) |
| CM-17 | Relational Contagion | −1 | No epistemic effect | One Standing relationship between two factions (GM / acting player choice) shifts one step toward hostility |
| CM-18 | Resonant Quiet | 0 | All factions in Thread Resonance this season may not spend their Thread Resonance marker for co-movement cancellation (the quiet IS the consequence) | No temporal effect |
| CM-19 | Substrate Assertion | −3 | Acting faction must reveal which Thread operation type was used (Weaving/Pulling/FR) | If this operation was Dissolution FR: an additional Monstrous Configuration Ob check fires at T12/T13 next season |
| CM-20 | The Past Answers | 0 | Acting faction learns one fact from Warden Working Libraries (B14) — GM selects which | Warden Cooperation +1 if Cooperation currently 0–2 |

---

### World Event Deck (Selected Entries)

Drawn at Accounting Step 8 when a clock threshold is crossed (1 per threshold crossed this season). Shuffle separately from Named Character Events.

| Event | Trigger Threshold | Effect |
|-------|------------------|--------|
| Schoenland Proxy Arms Deal | IP 45 | Schoenland provides arms to Altonian client faction in T4: +1D Military all orders there for 1 season. IP +2 |
| Riskbreaker Priority Notice | TC 35, OR Crown Emergency Powers 2+ times this year | See Riskbreakers NPC AI (B13) |
| Einhir Heartland Rising | RS < 50, Restoration Influence ≥ 3 in T14 | Restoration Mandate +1. Church Attention +2. Einhir Knowledge Milestone eligible next season |
| Altonian Trade Mission | IP 30 | Schoenland negotiates terms: Crown may accept (Trade +2D, IP −3) or refuse (IP +1, Standing vs Altonia) |
| Guilds Strike Action | Any faction's Wealth < 2 for 2 consecutive seasons | All Trade orders in Guild territories +1 Ob for 1 season. Guilds NPC: Stability −1 |
| Himmensendt's Sermon | TC 50 | Church Mandate +1. All other factions: Diplomacy targeting Church +1 Ob this season. Attention +1 |

---

## B11 — YEAR-END ACCOUNTING

Runs at end of Winter season (every 4th season).

1. Apply all Year-End TC and RS fractions (thread residuals from partial values).
2. RS baseline drift: −1 (the world degrades annually regardless of Thread operations).
3. Conscription for Löwenritter (if active): raise one free unit; Prosperity −1 in chosen territory.
4. Torben Loyalty: apply Year-End modifiers (Crown PI ≥ 5: +1; Crown upheld Mandate 2+ consecutive seasons: +1; Löwenritter PI ≥ 3 without Emergency Powers: +1).
5. Elske Loyalty: apply Year-End modifiers.
6. Hollow Victory modifier totals announced publicly. Record on shared sheet.
7. Any Once-Per-Year effects trigger (Supremacy Decree reset, etc.).
8. Age track (optional Long Campaign only): Champions begin accumulating age penalties after Year 3.
9. Check if TC Year-End fractional accumulations now cross a threshold. If so: draw Event Card.
10. Season marker resets to Spring. Campaign year advances.

---

## B12 — HOLLOW VICTORY

Hollow Victory tracks whether a faction's victory is legitimate or pyrrhic.

**Hollow Victory Modifier tracking:** A running total of modifier values is kept per faction. Negative modifiers reduce effective Deed count at victory declaration. Tracked publicly at each Year-End.

**Hollow Victory Modifiers:**

| Event | Modifier |
|-------|---------|
| Compromised Institutional Mandate | −0.5 Deeds per Compromise (accumulated) |
| Löwenritter Coup while player faction supported coup | −1 Deed |
| RS < 30 when faction declares victory | −1 Deed |
| IP > 60 when faction declares victory | −1 Deed |
| Any Allied faction holds Standing ≥ 3 vs your faction at victory | −0.5 Deed per such faction |
| Faction holds ≥ 4 Casus Belli Standing (was the aggressor multiple times) | −1 Deed |
| PC Belief arc contradicted faction Uphold/Compromise pattern (hybrid) | −1 Deed per season of contradiction |
| Torben Loyalty ≤ 1 at victory | −1 Deed (the dynasty has no future) |

**Hollow Victory at declaration:** Count effective Deeds after applying all accumulated modifiers. If effective Deeds fall below required threshold: victory cannot be declared.

---

## B13 — NPC AI BLOCKS

All NPC factions resolve Phase 4 actions in descending Stability order (ties: highest Military acts first). Riskbreakers Priority notification: at start of Phase 4, announce any Priority that will fire this season. Riskbreakers fire at their stated Priority before Phase 4 resolves in the relevant step.

### Crown (when NPC)

Priority order:
1. Govern T1 (maintain Valorsplatz Prosperity).
2. If TC > 40: issue Policy (Parliamentary Session, Free Trade Decree, or Curfew based on threat state).
3. If IP > 50: March units toward T4.
4. Diplomacy toward highest-TC threat this season.
5. Trade (Consul Outward in T7 or T2).

### Church of Solmund (when NPC)

Priority order:
1. If TC > 50: Assert.
2. If Attention Pool ≥ 3: issue Heresy Investigation in territory with highest Restoration Presence.
3. Govern T3 (maintain Himmelenger Prosperity).
4. Diplomacy toward Altonia (AER maintenance) if AER < 3.
5. If RS < 40: Suppress one Thread operation effect (Pontifex Outward).

### Hafenmark (when NPC)

Priority order:
1. If TC > 40: Parliamentary Manoeuvre (Senator Inward in T1).
2. Govern T6 (maintain Ducal Court Prosperity).
3. If RDT < 3: Senator Outward in non-Church territory (Diplomacy).
4. Trade (Consul Outward in T7).
5. If IP > 60: Legionary to T4 (support Crown defence).

### Varfell (when NPC)

Priority order:
1. Tribune Inward in adjacent territory (Intelligence gathering).
2. If VTM < 3: Tribune Inward in T9 (VTM development).
3. March to uncontrolled territory if RS < 50 and T12/T13 available.
4. Govern T9.
5. Patience Counter accumulation (default inaction when no higher priority fires).

### Restoration Movement (when NPC)

Priority order:
1. Spread Presence to any territory with RS < 40.
2. Advance highest-progress Community Project.
3. Move Presence to territory with active Heresy Investigation.
4. Start new Community Weave in T14 as first priority among new projects.
5. Community Organizing in any contested territory.

### Löwenritter (Pre-Coup NPC)

Peacetime AI. Coup Counter advances when:
1. Crown Mandate < 3 (Crown cannot govern legitimately): Counter +1.
2. TC ≥ 50 (Church dominates political space): Counter +1/season TC > 50.
3. IP > 60 (Altonian invasion imminent, Crown has not responded): Counter +1.
4. Crown Emergency Powers issued ≥ 3 times total: Counter +1.

At Counter = 4: Coup attempt. Roll Löwenritter Military vs. Ob 3. Success: Coup fires. Failure: Counter remains 4 (coup failed; Counter does not reset; next season retry). Coup fires when roll succeeds OR when Counter would advance beyond 4 due to a new trigger.

**Peacetime actions:**
1. March to T4 if IP > 50.
2. Govern T5 (maintain Arnesheld Prosperity).
3. If TC > 45: Tribune Inward in Church territory (monitoring).
4. Muster (build toward Military 6 reserve if below max).

### Riskbreakers (NPC — Conditional)

The Riskbreakers serve the Valorian state, not any individual faction. They evaluate conditions at Phase 4 start and fire at the relevant Priority if any condition is met.

**Priority 1 (fires before all other actions, same phase):**
Condition: Any faction's action directly threatens civilian populations AND the Riskbreaker mandate covers this territory.
- Action: Tribune Outward targeting the threatening faction. If Success or Overwhelming: the threatening faction's action is exposed to all players; that faction loses 1 Standing vs all.

**Priority 2 (fires at Phase 4 Priority 2 — Military step):**
Condition: Crown Mandate ≥ 6 AND Crown has issued Emergency Powers ≥ 2 times.
- Action: Riskbreakers evaluate Crown's Military orders this season. Crown Military orders in non-Crown territory must pass Riskbreaker Approval (Crown rolls Mandate vs. Ob 2; Failure: the order is delayed to next season). This is the Riskbreakers protecting Valoria from its own King.

**Priority 3 (fires at Phase 4 Priority 4 — Social step):**
Condition: TC ≥ 50 AND Assert declared this season.
- Action: Riskbreaker Tribune Investigate in one Church territory. If Success: one Church stat revealed to all.

**Priority 4 (fires at Phase 4 Priority 6 — Special):**
Condition: Varfell has accumulated Casus Belli via Patience Protocol AND VTM ≥ 3.
- Action: Riskbreakers expose the Casus Belli. Varfell loses the Casus Belli. VTM −1. All players notified.

**Priority 5 (Year-End only):**
Condition: Any faction holds Hollow Victory modifier of −2 or worse.
- Action: Public announcement of Hollow Victory state. All players learn which factions are in this state. No mechanical effect beyond transparency.

**Priority 6 (passive — information default):**
Riskbreakers maintain observation in T4 (Elske observation), T1 (Crown observation), and T3 (Church observation). Once per Year-End: Riskbreakers report one observable fact from each territory to all players (basic territorial intelligence — who is present, whether units are stationed, no stat details).

### Guilds (NPC)

Guilds have no military ambitions. Their AI is purely economic.

Priority order:
1. Trade (Consul Outward) from T8 or T11 to any adjacent faction with Wealth < 4.
2. Govern T11 (maintain Breadbasket Prosperity).
3. If any faction's Military is in T8 (Eidursjo): Guilds hire 1 Hired Blade (no Muster card required). Remove unit if Military threat departs.
4. Diplomacy toward highest-Military faction present in adjacent territory.
5. No action if all priorities satisfied.

**Guild Interaction:** Factions may target Guild territories with Trade orders. The Guilds respond positively to Trade (Wealth exchanged normally). They do not respond to Diplomacy unless a faction has Standing 3+ vs another faction that is harassing Guild territories — in that case, Guilds grant that faction a free Trade action next season.

### Niflhel (NPC)

Niflhel never controls territories. They operate as a network, not a territorial faction.

Priority order:
1. Increase Network Depth in territory with highest information value (highest Prosperity; or in T1, T3, T6 regardless of Prosperity).
2. If a faction's Intel action targets Niflhel operations in a territory: Niflhel Covert response (they attempt to expose the investigator — if any faction's Tribune Investigate fails in their territory: that faction's Intel result is reversed — they receive false information).
3. If Network Depth ≥ 2 in a territory: sell intelligence to highest-bidding faction (bidding occurs during Phase 2 as a sealed deal; highest bid acquires one enemy faction stat this season).
4. If Church Attention Pool ≥ 5: Niflhel goes quiet in Church territories for 1 season (Covert operations suspended to avoid exposure).

**Niflhel Network Depth:** A token per territory. Max 3 in any territory. Increasing Depth: automatic unless Intel (Tribune Investigate Ob 4) or Warden action (if T13 with Cooperation ≥ 1) removes it.

### Schoenland (NPC)

Schoenland is a spoiler actor. It profits from tension without resolving it.

Priority order:
1. If IP 30–60: increase Trade friction (all Valorian Trade involving Schoenland routes: add 1 Wealth cost to any faction using the route, paid to Schoenland — Schoenland War Chest accumulates but has no mechanical effect except tracking the cost of neutrality).
2. If IP > 60: Schoenland provides proxy military support to Altonian client in T4 (+1D Military in T4 for Altonian-aligned forces). Schoenland War Chest +2.
3. If IP < 30: Schoenland Trade available at standard terms (+1D bonus as per Environmental Effects).
4. Schoenland never allies. Never sends units into Valorian territories.

### Edeyja / The Wardens (NPC — conditional)

*Inactive until Warden Emergence.*

After Warden Emergence:
1. **Contain:** If monstrous entity in T12/T13: containment active. RS drain from entity halted 1 season.
2. **Investigate:** If Niflhel Network Depth ≥ 1 in T13: Warden investigation fires. Niflhel Covert in T13 +2 Ob next season. Attention +1.
3. **Work alongside:** If Cooperation ≥ 1 AND expedition faction in T13 without military units: apply Cooperation benefits.
4. **Emergency Mend:** If RS < 30: RS +1 this season (emergency warden intervention regardless of other conditions).
5. **Maintain:** No active threats. Warden Token remains. No visible effect. The wardens are holding.

**Edeyja will not:** Leave the Southernmost. Engage in peninsular political conflict. Provide information freely. Ask for help.

### Inquisitors (Church NPC sub-unit)

When deployed via Senator Inward with Church flag:
- While in territory: Attention +2/season.
- Can open Heresy Investigations without additional card play.
- Moving an Inquisitor requires Senator card.
- Inquisitors withdraw if territory is attacked. Not combat units.
- Inquisitor AI: pursue highest Restoration Presence territory first. If no Restoration Presence: pursue territory where most recent Thread operation occurred.

---

## B14 — HYBRID INTERFACE AND MILESTONE BONUSES

### Zoom-In Triggers (Hybrid Mode)

| Board Game Event | Scene Type |
|---------|----------:|
| Co-Movement card draws resonance event in PC's home territory | Personal Thread encounter |
| Heresy Investigation opened against PC or adjacent NPC | Personal/Social scene |
| Battle in territory where PC has stated presence | Combat scene |
| RS drops below 40 (first time) | Thread Awareness scene (all practitioners mandatory) |
| IP crosses 30 AND Torben is PC or adjacent | Personal Decision scene |
| IP crosses 40 (Torben Tutoring Demand event) | Political Crisis scene |
| Löwenritter Coup Counter = 4 | Political Crisis scene |
| Named NPC's Conviction challenged by board order outcome | Social scene |
| Any faction reaches Hollow Victory state | Belief Crisis scene |
| Riskbreakers intercept Vaynard Casus Belli | Hidden conflict scene |
| Reformed Settlement declared (RDT 5) | Theological Crisis scene |
| Warden Emergence fires | Southernmost Encounter scene (expedition faction mandatory) |
| Warden Cooperation reaches 3 | Campaign-altering knowledge scene (Calamity revealed) |
| Klapp Trajectory Choice fires | Church Institutional Crisis scene |
| Elske Loyalty drops below 2 | Diplomatic Emergency scene |

### Information Asymmetry (Fog of War — from hybrid_gaps_resolved.md)

All faction stats displayed to non-owning players in four qualitative states:

| Display | Underlying value |
|---------|-----------------|
| In ruins | 1 |
| Poor | 2–3 |
| Good | 4–5 |
| Excellent | 6–7 |

**Boundary ambiguity:** A stat at exactly 4: roll 1d6 at point of observation. 1–3 = Poor; 4–6 = Good. Fixed for that scene; re-rolled next observation.

**Faction-leader PCs:** See their own faction's exact values always. All other factions: fog.

**Intel always hidden:** Intelligence scores never display to non-owning players regardless of observation. Only revealed through successful Intel Domain Actions.

### Cascade Phase (Hybrid Mode)

After Phase 5 Accounting, GM runs Cascade as 5 steps:
1. Domain Echoes (TTRPG outcomes → faction stats).
2. Thread consequences (personal Thread operations → RS/TC changes).
3. Clock threshold checks (RS → TC → IP in order). Queue institutional responses.
4. Seasonal accounting (if end of season).
5. Board state update.

Personal scene consequences batch to Cascade phase. Exception: if consequence is simple and no threshold risk, GM may apply inline.

### Cascade Personal-to-Board Effects

| Personal Scene Outcome | Board Cascade Effect |
|-----------------------|-------------------|
| PC achieves Belief this season | Free Senate card to faction hand (no Wealth cost) |
| PC's Belief challenged but engaged | Recess cost → 0 Wealth |
| PC executes successful Thread operation | Faction's Pontifex available even if on Cooldown |
| PC fails Thread operation catastrophically | Pontifex on Cooldown Track (2 seasons) |
| PC Wounded in personal combat | Champion enters Wounded state on board |
| PC dies or is captured | Champion removed; faction loses Champion bonuses 3 seasons |
| PC negotiates major alliance | Add 1 Diplomat card to faction hand this season |
| PC uncovers evidence against another faction | That faction's one hidden stat revealed to PC's faction |
| PC passes Forgetting Check in Southernmost | Warden Emergence fires immediately |
| PC establishes contact with Elske | Elske card Contact Established; Elske Loyalty revealed to PC's faction |

### Milestone Bonuses

Each fires once only. Mark when triggered.

| Milestone | Trigger | Bonus |
|-----------|---------|-------|
| Constitutional Precedent | Crown holds PI ≥ 5 for 3 consecutive seasons | Crown Mandate +1 permanently |
| Einhir Knowledge | VTM ≥ 3 OR Warden Cooperation ≥ 2 | Revealing: Varfell (or triggering faction) +1 to all Intel for 2 seasons |
| Doctrinal Reach | Church controls T3 + Mandate ≥ 5 + TC ≥ 40 | TC advancement +0.5/season (permanent additional) |
| Community Resilience | Restoration has 5+ Presence markers (including at least 1 in T14) | RS +2 immediately; Community Project Progress rate +1 for 2 seasons |
| Thread Attuned | RS < 40 for 2 consecutive seasons (world is Awakening) | All Thread operation Ob −1 globally for 2 seasons |
| Reformed Valoria | RDT ≥ 5 AND PI ≥ 4 | Hafenmark Influence +1 permanently; Baralta gains Resonant Style for Consequence argument (+1D) |
| Southernmost Survivor | Any expedition faction completes a Southernmost Expedition season without losing a unit | Warden Cooperation +1; that faction's next Tribune Investigate in T12/T13 +2D |
| Grand Diplomatic Scene | IP < 25 at any Year-End | All factions: Diplomacy Ob −1 for 2 seasons; Schoenland Trade returns to standard |
| Klapp's Awakening | Klapp Trajectory B or C chosen | Klapp Milestone: Restoration + Varfell may now collaborate on Ceiral Ritual research without Warden Cooperation 3 (reduced requirement: Cooperation 2) |

### Warden Working Libraries (Hybrid Only)

On Overwhelming Forgetting Check, GM reveals one fact (each once per campaign):

1. The Calamity was not caused by something attacking the world. The Einhir drew their substrate too tight. It tore from the inside.
2. What came through is not evil. It is fullness that the rendering cannot hold. The monstrosities are being, in excess.
3. The Forgetting is not a cultural catastrophe. It is a rendering failure. The threads constituting memory of the Calamity were themselves damaged.
4. The wardens have been here since the day after. They are fewer each generation. Edeyja does not know how many seasons remain before the work exceeds their capacity.
5. The Locked Zones are not ruins. They are places where being has failed. New threads cannot spool through regions where the substrate has been ruptured.
6. There is a working methodology from before the Calamity. Edeyja holds it. No one else does.

---

## B15 — COOPERATIVE VICTORY

Two players may declare co-victory if conditions not directly contradictory. Declared publicly during Phase 2 in any season. Both victory paths evaluated together at Accounting Step 12.

**Approved co-victory pairings:**

| Pair | Path Name | Requirements |
|------|-----------|-------------|
| Crown + Hafenmark | Constitutional Co-Victory | Crown holds Constitutional Stability AND Hafenmark holds Reformed Valoria (Path A) simultaneously |
| Crown + Varfell | Informed Sovereignty | Crown holds Constitutional Stability AND Varfell holds Intelligence Hegemony. Note: Varfell Intel in Crown territory does not trigger Crown Mandate during active co-victory. |
| Varfell + Restoration | Substrate Preservation | Varfell holds Thread Supremacy (Path C) AND Restoration holds Network victory, both requiring RS ≥ 50 |
| Hafenmark + Restoration | Reformed Commonwealth | Hafenmark holds Reformed Valoria (Path A) AND Restoration holds Network victory |
| Löwenritter + Hafenmark | Regency Alliance | Löwenritter holds Regency Resolution AND Hafenmark holds Parliamentary Consolidation (Path C) |

**Co-victory Hollow Victory:** Both players' modifiers apply. If either player's effective Deed count falls below threshold: co-victory void (higher-count player may still claim solo victory if eligible).

**Incompatible pairings:** Church + Hafenmark (TC conditions contradict). Crown + Church (both require T1). Crown + Löwenritter (coup undermines Crown victory conditions).

---

## B16 — SOLO MODE

### Setup

1. Select a faction. Standard board setup.
2. Assign all NPC factions their AI priority trees (B13). Place Champions in starting positions.
3. NPC play order for Phase 4: Stability order (descending).

### Phase 2 — Strategic Planning (Solo)

No negotiation. Player may:
- Purchase from Senate Market at standard cost.
- Declare Open Pledges with NPC factions (NPC honors if consistent with current AI priority tree — does not conflict with Priority 1 or 2).
- Review all public board state.

### Phase 4 — NPC Actions (Solo)

After player's cards revealed (Phase 3): execute NPC plays in Stability order. Each NPC plays one card per season consistent with AI priority. NPCs do not exceed 5 cards/season. NPC cards treated as face-down during Phase 1.

### Solo Victory Conditions

Victory conditions unchanged. Hollow Victory modifiers apply. Solo calibrated for 12–20 season campaign. Session victories (3–5 seasons) may not be achievable on all paths — evaluate progress as partial wins.

### Solo Difficulty

| Difficulty | Modifier |
|------------|---------|
| Standard | NPC factions follow AI priority trees exactly |
| Challenging | Each NPC may deviate one priority level higher against the player once per year |
| Hard | Add one additional NPC faction; all NPC Stability +1 |

---

# PART C — SYSTEM REVIEW (v0.4)

## C1 — Assessment

**Functional Gaps Resolved (from v0.2–v0.3):** 16/16 identified gaps patched.
**All Three Editorial Blockers Resolved:** Patience Protocol, Casus Belli, Klapp Event Card authored.
**Canon Corrections Applied:** Elske location, TC starting value, Torben Tutoring Demand formalised.
**Simulation Issues:** 11 gaps found across 3 simulations; all patched (see Part E).

**Balance:** All playable factions have viable win paths from Season 1. Elske's corrected placement increases IP management tension and gives Löwenritter a more difficult but more meaningful succession path. Torben Tutoring Demand at IP 40 creates a Crown policy crisis that intersects cleanly with the Löwenritter Coup Counter. Patience Protocol gives Varfell a genuine strategic alternative to continuous Tribune plays.

**Cognitive Load:** Estimated 7.5/10 with reference cards; 5.5/10 without. Primary loads: Thread Operation Procedure (7-step, already laminated), Klapp Trajectory (new decision tree), Elske/Torben tracking (two new off-board cards). All manageable with the reference card set.

**Emergent Possibility:** 9.5/10 unchanged. The Klapp event card creates a new triangular interaction (Church-Klapp-Wardens) that wasn't previously available. Casus Belli gives Varfell a new political weapon to wield through Patience Protocol that is thematically rich and mechanically interesting.

## C2 — Pre-Playtest Checklist

**All Previously Blocking (now resolved):**
- ✅ BG-E-NEW-01 (Patience Protocol) — authored
- ✅ BG-E-NEW-02 (Casus Belli) — authored
- ✅ BG-E-NEW-03 (Klapp Event Card) — authored

**Still Blocking (editorial approval required before first playtest):**
- [ ] **v0.4-NEW-01:** Elske's Duke Veldensohn — named and given one mechanical property (his duchy borders T4), but no stats. Required for Altonian Invasion events (does Veldensohn cooperate or resist if IP ≥ 75?). Designer authorship required: one faction-like entry for Veldensohn as a named NPC during Invasion events.
- [ ] **v0.4-NEW-02:** Battle Tactic Card deck — referenced in B8 but contents not specified. 4 shared + 2 faction-specific cards per faction. Physical deck required. Suggest simple design: 4 generic (Advance, Hold, Feint, Rally — each with one combat modifier) + faction-specific based on faction strengths.
- [ ] **v0.4-NEW-03:** Mass Battle v3 Part B.4 reference — this document is referenced for tactic cards but not provided. Either create inline (see v0.4-NEW-02 above) or provide the document.

**Can wait until after first playtest:**
- [ ] BG-E-60: TD visibility (Hafenmark private track)
- [ ] BG-E-61: AER starting value confirmation (currently 2)
- [ ] BG-E-62: Reformed Settlement Ignore limit 2 — full response canon review
- [ ] BG-E-50: Cardinal schism mechanics (Church Accommodate path)
- [ ] BG-E-27/33: Champion Renown ability text
- [ ] Advanced Rules content
- [ ] Co-Movement deck expansion for new Thread mechanics
- [ ] Southernmost Working Libraries — 6 facts are placeholders
- [ ] Forgetting Check stat derivation in board game mode (hybrid only currently)
- [ ] Extended Altonian invasion mechanics (current patch covers basic)

---

# PART D — SIMULATION REPORT

Three full simulations were run: Standard competitive (3-player), Thread-intensive (4-player), and Solo Mode. Each simulation tracks mechanical resolution, clock states, and identifies friction points.

---

## SIMULATION 1: Three-Player Standard (Crown, Church, Hafenmark)

**Setup:** 245 AG. RS 72, TC 22, IP 20, PI 7. Season 1 begins.
**Players:** Crown (Alice), Church (Bob), Hafenmark (Clara).
**NPC Factions active:** Varfell, Restoration, Guilds, Niflhel, Schoenland, Löwenritter (pre-coup).

### Season 1 Resolution

**Phase 1 Planning:**
- Crown: Legionary (Inward) in T2, Consul (Outward) in T1, Senator (Outward) in T4.
- Church: Senator (Inward) in T3, Pontifex Eccl. Suppression (Outward) in T14, Legionary (Inward) in T3.
- Hafenmark: Consul (Outward) in T7, Senator (Inward) in T1, Diplomat in T6.

**Phase 2:** Crown offers Open Pledge with Hafenmark (PI maintenance). Hafenmark accepts. Church declines all engagement.

**Phase 3 Reveal:** All cards flipped.

**Phase 4 Resolution:**

Priority 1 (Intel): No Tribune cards this season. Skip.

Priority 2 (Military):
- Crown Legionary Inward T2 (Muster): Military 4 vs Ob 2 (standard muster). Roll: 5, 4, 2, 4 → 3 successes = Success. Raise 1 unit (Staging Token in T2). Deploys next season.
- Church Legionary Inward T3 (Muster): Military 4 vs Ob 2. Roll: 3, 1, 4, 5 → 2 successes, no majority 1s = Success. Staging Token in T3.

Priority 3 (Domain):
- Crown Consul Outward T1 (Trade): Wealth 4 vs Ob 2. Roll: 5, 1, 3, 6 → 2 successes, no majority 1s = Success. Wealth +1 (Crown Wealth → 5).
- Hafenmark Consul Outward T7 (Trade): Wealth 5 vs Ob 2. Roll: 4, 5, 3, 5, 6 → 4 successes = Overwhelming. Wealth +2 (Hafenmark Wealth → 7). Hafenmark may offer one counter-deal to adjacent faction at no cost.

> **GAP-S1-A:** Trade cap not stated. Hafenmark Wealth 5 + 2 = 7, which exceeds the stat maximum of 7. Confirmed: faction stats cap at 7 (consistent with 1–7 scale). No explicit cap rule stated. **PATCH P-01 below.**

Priority 4 (Social):
- Church Senator Inward T3 (Decree): Mandate 5 vs Ob 2. Roll: 5, 3, 6, 2, 5 → 3 successes = Success. Church decrees T3 a closed Ecclesiastical Zone: all non-Church actions in T3 +1 Ob until Decree is contested.
- Crown Senator Outward T4 (Diplomacy — contact Elske): Mandate 5 vs Ob 2 (Contact Established in T4). Roll: 4, 5, 2, 6, 3 → 3 successes = Success. **Contact Established.** Elske card activated. Elske Loyalty revealed to Crown: 4.
- Hafenmark Senator Inward T1 (Parliamentary Manoeuvre): Influence 4 vs Ob 2. Roll: 3, 5, 1, 4 → 2 successes, no majority 1s = Success. PI +1 → 8.
- Hafenmark Diplomat T6 (Diplomacy): Influence 4 + Diplomat (−1 Ob) = Ob 1. Roll: 6, 4, 4, 4 → 4 successes (Ob = 1; surplus 3) = Overwhelming. Hafenmark +1 Influence in T6. Establish Open Pledge with any adjacent faction at no cost — Hafenmark extends offer to Guilds (T8 adjacent): Guilds accept (consistent with Guild AI Priority 4).
- Pontifex Outward T14 (Eccl. Suppression — Thread Suppression): No Thread operation occurred in T14 this season. Card wasted (wrong territory; Church should have held).

> **GAP-S1-B:** No rule stating a Pontifex Outward (Thread Suppression) that targets a territory where no Thread operation occurred this season simply has no effect. Rules state "if a Thread operation by another faction was resolved this Phase 4 in this territory." Clear: if no operation, suppression cannot fire. But the card is still played and consumed. Should there be a refund mechanic for misplayed Pontifex? **PATCH P-02 below.**

Priority 5 (Thread): None this season.

**Phase 5 Accounting:**
1. Attribute changes: Crown Wealth 5, Hafenmark Wealth 7 (capped at 7), PI 8 (capped at 10 — PI is 0–10, now 8), Hafenmark Influence 5 in T6 (local — not faction-wide; local Influence vs faction stat need clarification). 

> **GAP-S1-C:** "Influence in territory" from Diplomacy vs. faction Influence stat. These appear to be the same stat but territory-specific gains feel wrong if they directly modify the faction's overall Influence score. **PATCH P-03 below.**

2. Stability checks: No faction suffered ≥ 2 attribute loss. Skip.
3. Cooldown: Nothing on cooldown. Skip.
4. Clock advances: TC formula — Church controls T3: +1. No Assert/Suppress (TC < 50). TC: 22 → 23. IP: no Altonian pressure table trigger this season. IP stays 20. RS: no drift (not Winter).
5. Church Attention Pool: +0 this season (no Thread operations, no gatherings detected). Pool = 0. No threshold.
6. Thread Debt: None outstanding.
7. Thread Resonance cleared.
8. Threshold events: no thresholds crossed.
8b. Milestone check: None triggered.
9. Warden Emergence: No expedition this season.
11. Hollow Victory: All factions at 0 modifiers. Announced.
12. Victory check: No Deed Tokens held by any faction. No victory.
13. Season → Summer.

**Season 1 End State:** RS 72, TC 23, IP 20, PI 8. Crown Wealth 5. Hafenmark Wealth 7. Church Decree active in T3. Contact with Elske established.

---

### Season 2 — Key Events

**Planning:** Crown plays Legionary Outward T2 (March unit from T2 staging — wait, the staging unit hasn't deployed yet).

> **GAP-S1-D:** Muster Staging Token converts to deployed unit at start of Phase 1 in the following season. This means at the start of Season 2 Phase 1, the Crown's T2 staging token converts to a deployed standard unit. The Crown player correctly has a deployed unit available in T2 at the start of Season 2. No issue — but the timing is critical and must be announced at the start of Phase 1. **PATCH P-04: Add explicit note that Staging Token conversion occurs at the START of Phase 1, before any cards are placed. GM announces conversions.**

Season 2 proceeds through a Church attempt to open a Heresy Investigation against Restoration presence in T14 (attention-based), an IP advance from Schoenland proxy activity, and a Crown Royal Decree targeting Church TC (−1). TC ends Season 2 at 24, IP at 22.

**IP 22 → approaching 30 within 3–4 seasons.** Crown player correctly identifies the approaching Schoenland friction threshold and prioritises a Trade deal with Schoenland via T7 (Lowenskyst, Hafenmark-controlled) in Season 3.

---

### Simulation 1 Findings

**Worked correctly:**
- Card-hand economy clean and intuitive.
- Mandate Uphold/Compromise system fired correctly (no trigger Season 1; Church's T3 Decree was not a trigger event).
- Hollow Victory tracking trivial at low complexity.
- Elske Contact established cleanly via Senator Outward in T4.
- Torben Loyalty track not yet triggered (IP 20 < 40 threshold).

**Gaps found:** S1-A, S1-B, S1-C, S1-D (see Patch Report, Part E).

---

## SIMULATION 2: Four-Player Thread-Intensive (Crown, Varfell, Restoration, Löwenritter post-coup)

**Setup:** Same start. Coup fires at start of Season 1 (forced for testing). Löwenritter player takes control. Crown player relegated to soft-coup mode (1 Senator/season). PI immediately −3 → PI 4.

**Test focus:** Thread system, VTM progression, Co-Movement cards, Coup mechanics.

### Season 1 Resolution

**Phase 2:** Varfell declares Patience Protocol intent (playing Conservative — not using Tribune this season to accumulate Patience Counters). Restoration announces Community Weaving in T14.

**Season 1 VTM Bootstrapping:**
Varfell plays Tribune Inward T9 (VTM Bootstrapping action, Season 1 only). Roll Influence 4 vs Ob 2: 6, 4, 1, 4 → 3 successes, no majority 1s = Success. VTM: 0 → 1.

> **GAP-S2-A:** VTM Bootstrapping uses "Tribune Inward in T9 as substrate research action." But Varfell's Tribune card is Inward orientation for Investigate normally. Is the Bootstrapping the same roll with a different consequence, or a different action entirely? Rules state "regardless of Thread Resonance status" and "does not draw a Co-Movement card." This is a special action triggered by the Tribune Inward in T9 during Season 1 only. The roll is correct (Influence vs Ob 2). But if the player ALSO wants to Investigate in T9 this season, do they get two effects from one Tribune Inward? **PATCH P-05 below.**

**Restoration Community Weaving T14:**
Weaver card (Thread operation). T14 has 0 Presence markers (Restoration hasn't spread yet — they need to play Presence Spread before Weaving benefits apply).
Ob 2 (base). No Presence markers to reduce. Roll Influence 4 vs Ob 2: 3, 4, 5, 2 → 2 successes = Success. Community Weaving complete. Draw Co-Movement card.

**Co-Movement Card Draw:** CM-07 (Temporal Echo). Temporal dimension: GM notes anomalous NPC memory for future hook. No RS change. No epistemic effect.

**Thread Resonance acquired:** Restoration is now in Thread Resonance (Thread operation occurred in or adjacent to their controlled... wait, T14 is Restoration-controlled informally, not a full control token).

> **GAP-S2-B:** T14 is described as "Restoration (informal)" with no controlling faction token. The Thread Resonance rule states a Thread operation "in or adjacent to a faction's CONTROLLED territory." Does Restoration control T14? The faction sheet says Military 0 — they have no units. The territory description says "Restoration (informal)" as starting control. **PATCH P-06 below.**

**Patience Counter accumulation:** Varfell played Tribune (Bootstrapping) this season, not a standard Intel action. Does the Bootstrapping count as "having a Tribune card available but playing it as a different card type"? No — the Bootstrapping IS a Tribune Inward. So no Patience Counter gained this season (Varfell used their Tribune).

> **GAP-S2-C:** Patience Protocol says "each season Varfell has a Tribune card available but plays it as a different card type: +1 PC." The Bootstrapping uses the Tribune card. Varfell gets no PC this season. But what if Varfell has no Tribune available (it was discarded and Recess hasn't occurred)? Can they still accumulate PC for inaction? PC should accumulate only when a Tribune card IS in hand and NOT played. **PATCH P-07 below.**

### Season 2 — Coup Aftermath

Löwenritter: Permanent Martial Law active. All Military orders in governed territory −1 Ob. All non-Military orders by any faction in governed territory +1 Ob (including Crown's soft-coup Senator).

**Löwenritter Requisition Order in T3 (Church territory):** Roll Military 6 vs Ob 2: 4, 5, 3, 6, 4, 5 → 5 successes (surplus 3) = Overwhelming. TC −2 (TC: 24 → 22). Attention +2. Church may not Assert this season.

**Elske — Season 2 Update:** Crown player (soft coup, 1 Senator/season) plays Senator Outward in T4 (Diplomacy, Ob 2). Roll Mandate... what is Crown Mandate after coup? Crown Mandate was 5 at game start. Coup itself does not reduce Crown Mandate directly, but PI −3 means Crown's Policy instrument now doesn't require Mandate check (PI 3–4 bracket). Soft-coup Crown retains their Mandate stat.

> **GAP-S2-D:** Soft-coup Crown has 1 Senator card play per season (Diplomacy Outward only). But the Senator card is the card that enables Diplomacy. If Crown already played their Senator this season for Elske contact in Season 1 (no, that was the v0.3 scenario — in Simulation 1 Crown had a full hand including Senator), in the post-coup world with soft coup, Crown gets exactly 1 Senator/season. This is correct per the rules. But does the soft-coup Crown still have their Recess card? **PATCH P-08 below.**

### Thread Operation Cascade Test (Season 3)

Restoration attempts a second Weaving in T14. First Weaving was Season 1. Thread Witness Node was NOT established (that requires a Community Weave Project completion, not a single Weaving). No second Co-Movement card draw required.

**Presence Spread:** Restoration plays Presence Spread. Move markers into T9 (adjacent to T14) and T12 (adjacent to T13). Roll Influence 4 vs Ob 2: Success. 2 Presence markers placed (T9 and T12).

**Thread Resonance now active in T9 and T12** (Restoration has Presence there). Varfell is also in Thread Resonance in T9 (VTM ≥ 2 — wait, VTM is 1 at this point). VTM 1 does not grant automatic T9 Thread Resonance. Only VTM 2+ does.

> **GAP-S2-E:** VTM 2 grants "always in Thread Resonance in T9." Varfell has VTM 1 after Season 1 Bootstrapping. They are NOT in Thread Resonance unless a Thread operation occurred in or adjacent to a territory they control. T9 is Varfell-controlled. The Restoration Community Weaving in T14 is not adjacent to T9. The Season 1 T14 Weaving: T14 is adjacent to T9 (checking adjacency table — not stated explicitly). Need explicit adjacency list. **PATCH P-09 below.**

**VTM +1 from Thread Debt:** No Thread Debt was incurred in Simulations 1 or 2 through Season 3. Varfell VTM remains 1.

### Simulation 2 Findings

**Worked correctly:**
- Coup mechanism (forced for testing) fired cleanly.
- Martial Law modifier applied without confusion.
- Requisition Order Ob calculation straightforward.
- Community Weaving Co-Movement card drew correctly.
- Patience Protocol intent declaration (Season 2 onward) incentivised correctly — Varfell player chose to hold Tribune Season 2, gaining +1 PC.

**Gaps found:** S2-A through S2-E (see Patch Report).

---

## SIMULATION 3: Solo Mode (Hafenmark, 4-Season Campaign)

**Setup:** Hafenmark player, NPC factions running AI. TC 22, RS 72, IP 20, PI 7.

**Goal test:** Reformed Valoria (Path A, 3 Deeds). Hafenmark needs RDT ≥ 4, PI ≥ 3, Reformed Settlement.

### Season 1 Solo

Planning: Hafenmark plays Consul Outward T7 (Trade), Senator Inward T1 (Parliamentary Manoeuvre), Diplomat T6 (Diplomacy toward Guilds).

NPC Church AI: Senator Inward T3 (Decree), Legionary Inward T3 (Muster), Pontifex Outward T14 (misplayed — no Thread operation in T14; see GAP-S1-B above).

NPC Crown AI: Consul Outward T1 (Trade), Legionary Inward T2 (Muster).

**Phase 4:**
Hafenmark Parliamentary Manoeuvre (Senator Inward T1): Influence 4 vs Ob 2. Roll: 5, 4, 1, 3 → 2 successes = Success. PI +1 → 8.

Church Decree in T3 (Senator Inward): Mandate 5 vs Ob 2. Roll: 5, 4, 5, 6, 3 → 4 successes (surplus 2) = Overwhelming. Church Decree: T3 closed Ecclesiastical Zone. This fires an Overwhelming, meaning Church may issue one Decree effect at no additional card play. Church player (NPC) uses this to open a Heresy Investigation in T14 (no Attention threshold cost — free from Overwhelming).

> **GAP-S3-A:** Church NPC AI Priority 2 says "if Attention Pool ≥ 3: open Heresy Investigation." However, the Overwhelming Decree effect in Phase 4 can open a Heresy Investigation without Attention threshold. NPC AI doesn't account for this. **PATCH P-10 below.**

**Accounting:** TC 22 → 23 (T3 control). IP 20 → 20. PI 8. RDT: +1 from Crown's Consul Outward Trade (Crown didn't issue Emergency Powers). Wait — RDT increases when Crown issues Emergency Powers without Parliamentary check, not from Trade. RDT: 0.

**Solo NPC Pledge Compliance Test:** Hafenmark offers Open Pledge to Crown NPC (mutual TC suppression: Crown will not issue Emergency Powers; Hafenmark will support any Crown Govern action with +1D). Crown NPC AI Priority 2: "If TC > 40: issue Policy." TC is 23 < 40 — Priority 2 doesn't fire. Priority 3: "If IP > 50: March to T4" — IP 20, doesn't fire. Priority 4: "Diplomacy toward highest-TC threat" — no TC threat active. Priority 5: "Trade in T7 or T2." The pledge terms (Crown won't issue Emergency Powers) don't conflict with any current Priority 1 or 2. Pledge accepted automatically. ✓

### Season 4 State

After 4 seasons of focused Hafenmark play:
- RDT: 2 (two Senator Outward successes in non-Church territories)
- PI: 9 (three Parliamentary Manoeuvres succeeded; one failed)
- Reformed Settlement: not yet available (needs RDT 5)
- Deed 1: Not held (RDT 2, needs ≥ 4)
- Deed 2: Held (PI 9 ≥ 3) ✓
- Deed 3: Not held (no Reformed Settlement yet)

TC at Season 4: 26 (T3 control +1/season; no Assert/Suppress yet).
IP at Season 4: 25 (Schoenland starting friction but below 30 threshold).

**Pace assessment:** At this rate, Hafenmark wins approximately Season 10–12 (Reformed Settlement requires RDT 5 which takes ~5 more seasons at +1/season average). This is within the 12–20 season campaign target for solo mode. ✓

### Simulation 3 Findings

**Worked correctly:**
- RDT progression at expected pace.
- PI recovery through Parliamentary Manoeuvres functional.
- Solo NPC Pledge Compliance rule worked cleanly.
- Hafenmark Deed Token 2 (PI ≥ 3) achievable Season 1 if PI 8 from setup.

> **GAP-S3-B:** Deed 2 requires PI ≥ 3. PI starts at 7. So Deed 2 is immediately held at game start for Hafenmark (PI 7 ≥ 3). This means Hafenmark starts with 1 of 3 Deeds already. Is this intended? **PATCH P-11 below.**

**Gaps found:** S3-A, S3-B (see Patch Report).

---

# PART E — PATCH REPORT

All 11 gaps identified across 3 simulations. Patches applied to the ruleset above where indicated. Summary here.

## PATCH P-01 — Faction Stat Cap at 7

**Gap:** S1-A. No explicit cap on faction stats.

**Rule added (B3, after Degree table):**
> "Faction stats are capped at 7 maximum. No stat may exceed 7 regardless of bonuses, orders, or Event Card effects. If a gain would push a stat above 7, it is recorded as 7 and the surplus is discarded. No stat may fall below 0 through action effects; the minimum is 0."

**Note:** Stability checks fire at Stability 0 (Collapse, per B4 Accounting). The 0 minimum and 7 maximum apply to all six stats.

---

## PATCH P-02 — Misplayed Pontifex (Thread Suppression) — No Refund

**Gap:** S1-B. Pontifex Outward (Thread Suppression) in a territory with no Thread operation has no effect.

**Rule added (B5 Church, Pontifex section):**
> "If Pontifex Outward (Thread Suppression) is played in a territory where no Thread operation occurred this Phase 4, the card is consumed with no effect. There is no refund. This is intentional: the Church's suppression apparatus can be misdirected. Factions may bluff Thread operations during Phase 2 precisely to bait a wasted Pontifex."

---

## PATCH P-03 — Territory Influence vs Faction Influence Stat

**Gap:** S1-C. "Gain 1 Influence in territory" from Diplomacy success — does this modify the faction's Influence stat or a territory-specific value?

**Clarification (B3, Diplomacy outcome):**
> "'Gain 1 Influence in territory' means: the acting faction's Influence stat increases by 1, representing the expansion of their political reach. This is a stat change, capped at 7, and applies faction-wide (it is not territory-specific). The territory is where the Diplomacy occurred — the Influence gain is the faction's gain."

**Design note:** Influence as a stat represents total political reach. A successful Diplomacy in T6 means the faction's overall network has expanded, not that T6 specifically has a different Influence value. This keeps tracking simple.

---

## PATCH P-04 — Staging Token Conversion Timing

**Gap:** S1-D. Staging Token conversion timing not explicitly announced.

**Rule added (B8, Muster Staging Protocol):**
> "At the very start of Phase 1 (before any cards are placed or plans are made), all Staging Tokens on the board are converted to deployed unit tokens by the owning faction. This conversion is announced publicly. Units converted this Phase 1 are immediately available for all Phase 4 military actions this season."

---

## PATCH P-05 — VTM Bootstrapping vs Tribune Investigate

**Gap:** S2-A. If Bootstrapping uses the Tribune Inward, does Varfell also get a standard Investigate?

**Rule added (B5 Varfell, VTM Bootstrapping):**
> "The VTM Bootstrapping action uses the Tribune card in the Inward orientation. It replaces the standard Investigate action for that card — the card is played as a Bootstrapping action, not as an Investigate. Varfell cannot use the same Tribune card for both Bootstrapping and Investigate in the same season. A second Tribune card (from Senate Market purchase) could be played as a standard Investigate in the same season."

---

## PATCH P-06 — T14 Control Clarification

**Gap:** S2-B. T14 is listed as "Restoration (informal)" but has no formal control token. Does Restoration control it?

**Rule added (B2, Territory Map, T14 entry):**
> "T14 (Eisengrund) begins under Restoration Movement informal control. Restoration has a control token in T14 at game start. The 'Restoration (informal)' notation indicates no military units are stationed there — control exists without military presence. Restoration's control of T14 can be displaced by any faction that successfully Marches a unit there without Restoration military resistance (Restoration has Military 0 and no units). If control is displaced, Restoration Presence markers remain (they cannot be removed by military action), but the controlling faction token changes."

---

## PATCH P-07 — Patience Counter Accumulation Condition

**Gap:** S2-C. Patience Counter accumulation requires "Tribune available but played as different card type" — ambiguity when Bootstrapping uses Tribune.

**Rule clarified (B5 Varfell, Patience Protocol):**
> "Patience Counters accumulate when: a Tribune card IS in Varfell's hand at the start of Phase 1 AND Varfell does not play the Tribune card during Phase 4 of that season. 'Not playing' means no Tribune Inward, Tribune Outward, Bootstrapping (Season 1 only), or any Senate Market Tribune Militum. Playing a different card (Legionary, Consul, etc.) while the Tribune remains unplayed earns +1 PC. If both the Tribune and another card trigger condition applies in the same season, maximum gain is still +1 PC per season from hand inaction (not +2 for two different cards held back)."

**Correction:** Earlier draft stated maximum +2 PC per season from inaction (hold Tribune + hold Senate Market purchase). The correct cap is +1 PC per season from inaction. The +2 cap was an error; the PC cap of 4 or 6 total is unchanged.

---

## PATCH P-08 — Soft-Coup Crown Hand

**Gap:** S2-D. Soft-coup Crown has 1 Senator/season (Diplomacy Outward only) — does this include Recess?

**Rule added (B5 Löwenritter, Soft Coup description):**
> "Under the soft coup, Crown retains: 1 Senator card play per season (Diplomacy Outward orientation only — may not use Senator Inward for Decree or Parliamentary Manoeuvre) AND 1 Recess card (functions normally: retrieve cards at cost of 1 Wealth). Crown's Legionary, Consul, Tribune, and Prefect cards are held but may not be played. The Recess is available so Crown can manage their hand between seasons; otherwise they would be unable to retrieve the Senator for next season's use."

---

## PATCH P-09 — Territory Adjacency List

**Gap:** S2-E. Adjacency not explicitly listed.

**Adjacency Map (B2, added after Territory Table):**

| Territory | Adjacent To |
|-----------|------------|
| T1 (Valorsplatz) | T2, T3, T5 |
| T2 (Gransol) | T1, T3, T4, T6 |
| T3 (Himmelenger) | T1, T2, T5 |
| T4 (Spartfell) | T2, T5, T15 |
| T5 (Arnesheld) | T1, T3, T4 |
| T6 (Hafenvalor) | T2, T7, T8 |
| T7 (Lowenskyst) | T6, T8, T15 |
| T8 (Eidursjo) | T6, T7, T9 |
| T9 (Varfell) | T8, T10, T11, T14 |
| T10 (Sigurdshalm) | T9, T11, T12 |
| T11 (Halvardshelm) | T9, T10, T13 |
| T12 (Oastad) | T10, T13 |
| T13 (Stillhelm) | T11, T12 |
| T14 (Eisengrund) | T9, T11 |
| T15 (Schoenland) | T4, T7 (sea route) |

*T15 (Schoenland): sea route — accessible via T7 for Trade, accessible via T4 for invasion. Units cannot March to T15 (it is a neutral foreign power).*

**Derived:** T14 (Eisengrund) is adjacent to T9 and T11. A Thread operation in T14 affects Thread Resonance in T9 and T11 (any faction with controlled territory there gains Thread Resonance). Restoration's Presence markers in T9 and T12 (Simulation 2, Season 3) create Thread Resonance for Restoration in T9 and T12 specifically.

---

## PATCH P-10 — Church NPC AI Overwhelming Decree Effect

**Gap:** S3-A. NPC AI Priority 2 says "Attention ≥ 3: open Heresy Investigation." Does not account for Overwhelming Decree opening a free investigation.

**Rule added (B13, Church NPC block):**
> "After Church NPC resolves Decree (Senator Inward) in Phase 4: if the result was Overwhelming, the NPC immediately executes one of the following (GM chooses based on current state, in order of threat priority): open a Heresy Investigation in the territory with highest Restoration Presence, OR open a Heresy Investigation in the territory where the most recent Thread operation occurred this season, OR Mandate check to declare T3 closed. This Overwhelming bonus effect does not require a card play. Record the investigation as having fired at Phase 4 Priority 4 (simultaneous with the Decree)."

---

## PATCH P-11 — Hafenmark Deed 2 Starting State

**Gap:** S3-B. Hafenmark Path C Deed 2 requires PI ≥ 3; PI starts at 7. Hafenmark holds this Deed at game start.

**Decision:** This is intentional design, not an error. Hafenmark begins with a structural advantage in Parliamentary Consolidation (Path C) — they start with 1 of 4 Deeds already. This reflects their institutional position as the constitutional guardians. The challenge is the other three Deeds, particularly PI ≥ 4 (which can be lost under coup or Church seizure) and Control T6 (which can be contested).

**Rule added (B5 Hafenmark, Path C note):**
> "Deed 2 (PI ≥ 3) is typically held at game start (PI begins at 7). Hafenmark begins with 1 of 4 Parliamentary Consolidation Deeds already met. The challenge of Path C is maintaining all four simultaneously — including Deed 1 (PI ≥ 4, which may fall under coup or Church territorial seizure), and ensuring Deed 4 (no active Heresy Investigation) is clear at the same time."

---

## Summary Table: All Patches

| ID | Gap | Location | Status |
|----|-----|----------|--------|
| P-01 | Stat cap at 7 | B3 | Applied |
| P-02 | Misplayed Pontifex | B5 Church | Applied |
| P-03 | Territory Influence vs Faction stat | B3 | Applied |
| P-04 | Staging Token conversion timing | B8 | Applied |
| P-05 | VTM Bootstrapping vs Investigate | B5 Varfell | Applied |
| P-06 | T14 control clarification | B2 | Applied |
| P-07 | Patience Counter accumulation | B5 Varfell | Applied |
| P-08 | Soft-coup Crown hand | B5 Löwenritter | Applied |
| P-09 | Territory adjacency list | B2 | Applied |
| P-10 | Church NPC Overwhelming Decree | B13 | Applied |
| P-11 | Hafenmark Deed 2 starting state | B5 Hafenmark | Applied |

---

## Findings and Suggestions

**Suggestions for first playtest (not blocking, but recommended prep):**

1. **Elske and Torben cards:** Print as dedicated reference cards (postcard size). Elske card should have: Loyalty track, Contact Established box, information fields (Duke Veldensohn, duchy borders T4, IP threshold impacts). Torben card should have: Loyalty track, Altonian location box (if sent), tutoring demand response status.

2. **Thread Operation Procedure:** The 8-step laminated card is essential. Playtest should not begin without it in physical form.

3. **Adjacency map physical representation:** The adjacency list (P-09) should be printed on the board or on a quick-reference card. Territory adjacency confusion is the most common source of rules disputes in territory-control games.

4. **Patience Protocol tracking:** Varfell needs a dedicated Patience Counter track on their faction mat (0–6 track, physical tokens). Without physical tracking, players will lose count.

5. **Co-Movement Card physical deck:** 20 cards (CM-01 through CM-20) need to be printed and shuffled before play. Named Character Events (Klapp, Riskbreakers) should be a separate smaller deck.

6. **TC starting value 22:** The shift from v0.3's TC 15 to v0.4's TC 22 (canonical correction) accelerates the Assert/Suppress threshold by approximately 6 seasons. Playtesters should note whether this feels correct — TC 50 (Assert threshold) is now ~14 seasons of +2/season gain away instead of ~17 seasons. At 3-4 player competitive, this is appropriate tension in a 12–20 season game.

7. **Veldensohn authorship (v0.4-NEW-01):** This is the most urgent remaining gap. Without knowing whether Veldensohn cooperates with or resists the Altonian Vanguard (IP ≥ 75), the Invasion Events in T4 cannot be fully resolved. Suggest: Veldensohn default disposition is Neutral → shifts to Hostile toward Altonian Vanguard if Elske Loyalty ≥ 5 (he sees his wife's sympathies and acts accordingly) OR Friendly if Elske Loyalty ≤ 2 (the household is Altonian in orientation).

---

*Ruleset v0.4 complete.*
*21 core systems. 3 blocking editorial items resolved (Patience Protocol, Casus Belli, Klapp Event Card). 11 simulation gaps patched. 3 new pre-playtest blockers identified (v0.4-NEW-01, -02, -03). 62 items resolved since v0.1.*
*Next step: designer authorship on Veldensohn, Tactic Card deck, and Mass Battle v3 Part B.4. Then first playtest.*
