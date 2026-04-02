# VALORIA: THE BOARD GAME
## Ruleset v0.3
**Date:** 2026-04-01  
**Authority:** Skeleton Ruleset v0.2 (2026-04-01) + Simulation Round 1 and Round 2 patches + editorial approvals.  
**Status:** Pre-playtest. Two editorial items remain open (see C2).

**Changes from v0.2:**
- All standalone acronyms expanded to full name with acronym in parentheses.
- Editorial decisions BG-E-51, -53, -59, -63, -64, -65, -66, MP-34 tentatively approved and implemented.
- Church Pontifex (base hand) redefined as Ecclesiastical Suppression. Church has no access to Thread Operations unless a Klapp event occurs (B5 Church, B13 note).
- Theocratic Clock (TC) advancement formula defined (B7).
- Core action outcome effects defined for all actions (B3).
- Stat-to-action mapping table added (B3).
- Champion starting positions defined (B8).
- Ob 0 resolution defined (B4).
- Invasion terminal mechanics added, basic (B2, B7).
- Muster staging token protocol added (B8).
- Three-way (or more) Social conflict rule defined (B4).
- Presence Spread action timing clarified (B5 Restoration).
- Reformed Settlement declaration timing patched (B5 Hafenmark).
- Church Ignore cap: 2 uses maximum (B5 Hafenmark).
- Hollow Victory tracking made explicitly public (B12).
- Vaynard-Edeyja same-season rule: Accounting Step 9b added (B4, B7).
- NPC AI evaluation order defined (B13).
- Altonian Ecclesiastical Relationship (AER) effects cross-referenced in Invasion Pressure (IP) Environmental Effects table (B2).
- Milestone Bonus check added to Seasonal Accounting as Step 8b (B4).
- Community Resilience Milestone scope confirmed: includes Presence markers (B9).
- Löwenritter Requisition Order added to post-coup Tribune card (B5 Löwenritter).
- Torben constitutional restraint Loyalty path added (B5 Löwenritter).
- Restoration Movement Influence raised from 3 to 4 (B5 Restoration).
- Cooperative Victory rules added (B15).
- Solo Mode framework added (B16).
- Mandate trigger formal text and Compromise benefits per faction added (B7).
- Torben Loyalty track defined (B5 Crown, B5 Löwenritter).
- Elske location and rescue procedure defined (B5 Löwenritter).
- Varfell and Hafenmark Deed Token condition tables added (B5).
- "Against temporal flow" defined (B6).
- Varfell Thread Mastery (VTM) bootstrapping action added (B5 Varfell).
- Riskbreaker Priority notification rule added (B13).
- BG-E-NEW-01 (Patience Protocol) and BG-E-NEW-02 (Casus Belli) flagged as still blocking.

---

# PART A — SYSTEM REGISTER

## A.1 Core Systems (19 player-facing systems)

| # | System | Layer | Notes |
|---|--------|-------|-------|
| 1 | Card-Hand + Recess | Action Economy | Hand = capability. Foundation of all player agency. |
| 2 | Order Orientation | Action Economy | Inward/Outward sub-type selector. Zero overhead. |
| 3 | Senate Market | Action Economy | Hand expansion = faction development. |
| 4 | Cooldown Track | Action Economy | 3-slot wheel for Unique Powers. |
| 5 | Three Clocks | Victory/Loss | Rendering Stability (RS) is metaphysically primary. Theocratic Clock (TC) and Invasion Pressure (IP) are politically co-equal. |
| 6 | Clock Environmental Effects | Ambient Modifier | All three clocks modify action obstacle ratings. |
| 7 | Deed Tokens | Victory | Simultaneous-holding tension. All must be held at once. |
| 8 | Hollow Victory Scoring | Victory | End-game legitimacy modifier. Tracked publicly throughout the game. |
| 9 | Institutional Mandate | Political | Uphold/Compromise. Faction identity with mechanical teeth. |
| 10 | Standing Tokens | Political | Political history. Grievance and capital. |
| 11 | Crown Policy | Political | Crown sets the environment for all other factions. |
| 12 | Parliament Integrity | Political | Shared institution. Hafenmark's primary lever. |
| 13 | Thread Resonance | Thread | Binary seasonal marker: in resonance or not. |
| 14 | Thread Debt | Thread | Permanent cost of Thread operations. Cannot be fully discharged. |
| 15 | Church Attention Pool | Thread | Consequence-detection only. Church sees behaviour, not operations. |
| 16 | Co-Movement Card Deck | Thread | Three-dimensional consequence per Thread operation. P-14 compliance. |
| 17 | Community Projects | Faction/Thread | Multi-season investments. Quiet Year mechanic. |
| 18 | Champions + Wound States | Military | Named leaders as mobile tokens. Hybrid bridge. |
| 19 | Faction Structural Asymmetry | Faction | Distinct action profiles, private tracks, unique mechanics. |

**Faction-specific private tracks** (faction mat complexity, not board complexity):
- Varfell Thread Mastery (VTM): Varfell track, private until VTM 3
- Reformed Doctrine Track (RDT): Hafenmark track
- Theological Dissatisfaction (TD): Hafenmark track, private
- Altonian Ecclesiastical Relationship (AER): Church track, board-visible

## A.2 System Architecture

```
BOARD STATE (public, visible to all)
├── Territory map: control, Prosperity, Fortification, Champions, Presence markers
├── Three Clocks: Rendering Stability (RS) 72→0, Theocratic Clock (TC) 15→100, Invasion Pressure (IP) 20→100
├── Parliament Integrity (PI) track (0–10, starts 7)
├── Church Attention Pool (0–10, resets each season)
├── Altonian Ecclesiastical Relationship (AER) track (0–5, starts 2) — near Invasion Pressure (IP) track
├── Löwenritter Coup Counter (0–4)
└── Warden Cooperation track (0–3) — near T13; inactive until Warden Emergence

FACTION MAT (private to player)
├── Card Hand (6 starting cards + purchased cards)
├── Cooldown Track (3 slots)
├── Deed Track (faction-specific conditions — see B5 per faction)
├── Standing Tokens (held)
├── Thread Resonance marker (in resonance / not in resonance this season)
├── Hollow Victory modifier running total (updated publicly at Year-End)
└── Private tracks: Varfell Thread Mastery (VTM) / Reformed Doctrine Track (RDT) / Theological Dissatisfaction (TD) / Altonian Ecclesiastical Relationship (AER) (faction-dependent)

SHARED LEDGER / REFERENCE
├── Community Project Progress Tracks
├── Restoration Movement Presence Markers (per territory)
├── Niflhel Network Depth Markers (per territory, NPC tracking)
├── Torben Loyalty Track (0–7, on Crown/Löwenritter faction mat or shared ledger)
└── Thread Debt tokens (max 3 in play at once)

REFERENCE CARDS (consult, don't track)
├── Clock Environmental Effects table
├── Thread Operation Procedure (7-step laminated card — mandatory)
├── Seasonal Accounting Checklist (12-step — mandatory)
├── Hollow Victory Scoring Sheet (pre-printed — mandatory, update publicly at Year-End)
└── Southernmost Expedition Summary Card (mandatory for T12/T13 actions)
```

## A.3 Advanced / Variant Rules (not in skeleton core)

| System | When Active |
|--------|-------------|
| Secondary Objectives | Default board game; disable in hybrid |
| Proxy Support | Advanced |
| Thread Veil Cards | Advanced (Baralta Einhir lineage card removed — P-08 violation) |
| Deal Tokens | Advanced negotiation variant |
| Winter Accounting / Leader Age | Long campaign only |
| Solo Mode | See B16 |
| Lead/Follow Resolution | Advanced layer |

---

# PART B — RULESET v0.3

---

## B1 — OVERVIEW

**Valoria: The Board Game** is a standalone political-strategic game set on the Valorian peninsula. It is also the strategic layer of hybrid tabletop roleplaying / board game play.

**Core feel:** Powerful institutions attempting to consolidate power across a dying world. Rendering Stability (RS) degrades through sustained conflict and accelerates sharply under large-scale Threadwork. The Church of Solmund siphons Crown authority toward a long-term theocracy. Altonia watches for weakness. Every faction wins by expanding — but expansion itself tears the world further apart.

**Three mandatory game modes:**
- **Board Game (this ruleset):** Complete standalone game, 2–4 hours, 3–5 seasons per session.
- **Hybrid:** Board game as strategic layer feeding into tabletop roleplaying personal-scale scenes.
- **Tabletop Roleplaying:** Governed by separate compiled stages.

### Playable Factions

| Faction | Available |
|---------|-----------|
| Crown | 2–5 players |
| Church of Solmund | 2–5 players |
| Hafenmark | 2–5 players |
| Varfell | 2–5 players |
| Restoration Movement | 5 players only (optional) |
| Löwenritter (post-coup) | Conditional: only if coup fires; replaces NPC Löwenritter |

**Win probability at game start:** All playable faction combinations are designed for similar opening win probability. No faction has a structural advantage at Season 1. Faction difficulty scales with game-state complexity, not starting stats.

**Cooperative Victory:** Two players whose victory conditions are not directly contradictory may declare a co-victory (see B15). Co-victories are available from Season 1; they must be declared publicly during Phase 2 (Negotiation) when both factions commit.

### NPC-Driven Factions (never playable in standard mode)

Löwenritter (pre-coup), Riskbreakers, Inquisitors, Guilds, Ministry, Niflhel, Altonia, Schoenland, and Edeyja / the Wardens are always NPC-controlled. Their AI priority trees are in B13.

### Player Count

| Players | Mode |
|---------|------|
| 1 | Solo (see B16) |
| 2 | Competitive asymmetric; NPC AI runs remaining factions |
| 3–4 | Competitive; NPC AI runs remainder |
| 5 | Full playable coverage: Crown, Church, Hafenmark, Varfell, Restoration Movement |

---

## B2 — THE BOARD

### Territory Map

15 territories in adjacency layout (north-south peninsula axis). Each territory has a controlling faction marker, Prosperity value (1–7), Fortification level (0–4). May contain: Project markers, Presence markers, Champion token, unit tokens.

| # | Territory | Start Control | Pros | Fort | Special |
|---|-----------|--------------|------|------|---------|
| 1 | Valorsplatz (Capital) | Crown | 6 | 2 | Royal Court: Crown Policy −1 Ob. Parliament: Hafenmark Mandate orders −1 Ob. |
| 2 | Gransol | Crown | 5 | 1 | Garrison: Muster here +1D. |
| 3 | Himmelenger | Church | 5 | 2 | Grand Cathedral: Theocratic Clock (TC) +1/season Church controls. Church Unique Power −1 Ob here. |
| 4 | Spartfell | Crown | 3 | 2 | Altonian Border: Invasion Pressure (IP) threshold events here first. Invasion entry point. |
| 5 | Arnesheld | Crown/Löwenritter | 4 | 3 | Löwenritter Fortress: Martial Law −1 Ob. Fort max 4. |
| 6 | Hafenvalor | Hafenmark | 6 | 1 | Ducal Court: Sovereign Authority Doctrine here only. Major port. |
| 7 | Lowenskyst | Hafenmark | 5 | 0 | Trade Hub: all Trade +1D. Schoenland sea route. |
| 8 | Eidursjo | Guilds (NPC) | 4 | 0 | Difficult terrain: March costs 2 movement. Guild trade routes active. |
| 9 | Varfell | Varfell | 4 | 1 | Varfell Seat: Varfell Thread Mastery (VTM) research here only. Einhir ruins: Restoration Weaving −1 Ob. |
| 10 | Sigurdshelm | Niflhel (NPC) | 3 | 0 | Black Market: Niflhel Covert −1 Ob. All Trade +1 Ob. |
| 11 | Halvardshelm | Guilds (NPC) | 5 | 0 | Breadbasket: +1 Prosperity/season uncontested. Muster Ob −1. |
| 12 | Oastad | Uncontrolled | 3 | 0 | Thread Wound: Rendering Stability (RS) thresholds trigger +10 early here. RS −1/season after 2 consecutive seasons of any occupation. **Southernmost rule applies.** |
| 13 | Stillhelm | Uncontrolled | 2 | 0 | Southernmost Access: required for Expedition. Non-Thread orders +1 Ob. RS −1/season any occupation. **Southernmost rule applies. Warden Cooperation track here (inactive until Warden Emergence).** |
| 14 | Eisengrund | Restoration (informal) | 4 | 0 | Einhir Heartland: Restoration Influence −1 Ob. Church Influence +1 Ob. |
| 15 | Schoenland | Neutral (NPC) | 5 | 1 | Altonian Trade. At Invasion Pressure (IP) ≥ 75: Altonian vanguard deploys. Intel orders here: visible to Altonia. |

### The Southernmost Rule (T12 and T13)

**Any military unit token placed in T12 (Oastad) or T13 (Stillhelm) by a faction that does not have a Thread-qualified presence in that territory is immediately removed from the board at the resolution step, before battle is resolved.** No Standing cost, no Stability check, no battle: the units simply cease to function. This is not Edeyja's power. It is the nature of the Southernmost — the substrate damage there is such that non-Thread configurations cannot sustain themselves.

A Thread-qualified presence means: a Restoration Movement Weaver card was played in that territory this season, OR Varfell has Varfell Thread Mastery (VTM) ≥ 2, OR a practitioner with Thread Sensitivity 30+ is present (hybrid mode only).

This rule has always applied. Factions discover it by attempting and failing. Before Warden Emergence, no faction knows why it happens.

### Board Tracks

**Altonian Ecclesiastical Relationship (AER) Track (0–5):** Small 5-step track on board near Invasion Pressure (IP) clock. Starts at 2. Church player updates this track at Accounting.

**Warden Cooperation Track (0–3):** Printed near T13. Inactive until Warden Emergence fires. Once active, wooden Warden Token sits on track at current Cooperation level.

### Clock Tracks

**Rendering Stability (RS):** Starts at 72. Counts toward 0. Rupture at 0 = shared loss.  
**Theocratic Clock (TC):** Starts at 15. Counts toward 100. Theocratic Clock (TC) 80 = Church Territorial Seizure event.  
**Invasion Pressure (IP):** Starts at 20. Counts toward 100. Invasion Pressure (IP) 75 = Altonian Vanguard deployed.  
**Parliament Integrity (PI):** Starts at 7. Counts 0–10.

### Clock Environmental Effects

**Rendering Stability (RS) Effects:**

| RS Range | Effect |
|----------|--------|
| 72–50 | No modifier |
| 49–30 | Thread operations: −1 Ob (community urgency). Non-Thread orders in T12/T13: +1 Ob |
| 29–20 | As above. Entity encounters possible in T12/T13. All Muster: +1 Ob |
| Below 20 | All orders all territories: +1 Ob. Community Projects advance +1/season. Entity encounters expand |

**Theocratic Clock (TC) Effects:**

| TC Range | Effect |
|----------|--------|
| Below 30 | No modifier |
| 30–49 | Church orders: −1 Ob in Church-held territory |
| 50–69 | Church orders: −1 Ob everywhere. Non-Church Diplomacy targeting Church: +1 Ob. Mandatory Assert/Suppress choice each season |
| 70+ | As above. Church Territorial Seizure protocol active. Altonian Ecclesiastical Relationship (AER) begins modifying Theocratic Clock (TC) gains |

**Invasion Pressure (IP) Effects:**

| IP Range | Effect |
|----------|--------|
| Below 30 | Trade with Schoenland: +1D |
| 30–59 | Trade with Schoenland: +1 Ob. All factions: +1D to Intel orders |
| 60–74 | Trade disrupted: Schoenland Trade +2 Ob. Schoenland funds proxy at T4: +1D military there |
| 75+ | Altonian Vanguard deployed (see Invasion Events below). *Note: Altonian Ecclesiastical Relationship (AER) ≥ 4 raises the vanguard threshold to 80; AER 5 prevents Invasion Pressure (IP) from exceeding 50.* |

**Invasion Events (Invasion Pressure (IP) ≥ 75):**
- Season 1 of deployment: Altonian Vanguard (Military 5, Cohesion 5) deploys to T4 (Spartfell). Invasion countdown begins (3 seasons).
- Season 2: Vanguard advances if not repelled. All factions: military orders in T4 at −1 Ob (defending home soil).
- Season 3: If Vanguard not repelled and Invasion Pressure (IP) not reduced below 60: full Altonian invasion. Altonian forces march north (T4 → T2 pattern). Shared loss condition if Altonia controls ≥ 5 territories.
- Invasion Pressure (IP) reduced below 60 before countdown expires: Vanguard withdraws. Countdown resets if Invasion Pressure (IP) crosses 75 again.

---

## B3 — ACTION ECONOMY

The Card-Hand system is the action economy foundation. There are no Order tokens. Your hand of Action Cards is your complete list of available actions this season. Playing a card executes its action and removes it from your hand until Recess.

### Stat-to-Action Mapping

All rolls: pool = relevant faction stat (1–7). Dice: d6. Success = 4+. Majority 1s = Failure regardless of other dice.

| Card | Action (Inward / Outward) | Stat Used |
|------|--------------------------|-----------|
| Legionary | Muster / March | Military |
| Consul | Govern / Trade | Mandate (Govern) · Wealth (Trade) |
| Prefect | Govern All territories (no orientation) | Mandate |
| Senator | Decree / Diplomacy | Mandate |
| Tribune | Investigate / Spy | Influence |
| Recess | Retrieve hand | — |
| Organizer (Restoration) | Community Organizing | Influence |
| Weaver (Restoration) | Community Weaving | Influence |
| Presence Spread (Restoration) | Move Presence markers | Influence |
| Project (Restoration) | Start Community Project | Mandate |
| Pontifex (Church base hand) | Ecclesiastical Suppression (Inward: Investigate heresy / Outward: Suppress Thread consequence) | Mandate |
| Pontifex (Senate Market) | Thread operation — Restoration / Thread-qualified only | Influence |
| Diplomat | Diplomacy at −1 Ob | Influence |
| Colonist | March + Govern at destination | Military then Mandate |
| Architectus | Fortify + Govern same territory | Military then Mandate |
| Tribune Militum | Military at −1 Ob | Military |
| Aedile | Trade at −1 Ob | Wealth |
| Praetor | Start or advance Community Project | Mandate |
| Censor | Crown only: issue one Policy. Non-Crown: block one order this season | Mandate |

### Base Hand (6 cards per faction)

| Card Type | Action Domain | Action (by Orientation) |
|-----------|--------------|------------------------|
| **Legionary** | Military | Inward: Muster. Outward: March. |
| **Consul** | Domain | Inward: Govern. Outward: Trade. |
| **Senator** | Social | Inward: Decree / Parliamentary Manoeuvre. Outward: Diplomacy. |
| **Tribune** | Intel/Covert | Inward: Investigate. Outward: Spy. |
| **Prefect** | Domain (broad) | Govern ALL controlled territories simultaneously (each at Ob +1). Orientation does not apply. |
| **Recess** | — | Retrieve all played cards. Costs 1 Wealth. No other action this card-play. |

**Starting hands by faction:**

| Faction | Hand Composition |
|---------|-----------------|
| Crown | 2× Legionary, 1× Consul, 1× Senator, 1× Prefect, 1× Recess |
| Church | 2× Senator, 1× Pontifex (Ecclesiastical Suppression — see B5 Church), 1× Consul, 1× Legionary, 1× Recess |
| Hafenmark | 2× Consul, 1× Senator, 1× Legionary, 1× Diplomat (unique), 1× Recess |
| Varfell | 2× Tribune, 1× Legionary, 1× Consul, 1× Colonist (unique), 1× Recess |
| Restoration Movement | 2× Organizer, 1× Weaver, 1× Presence Spread, 1× Project, 1× Recess |
| Löwenritter (post-coup) | 3× Legionary, 1× Tribune (Requisition Order available — see B5 Löwenritter), 1× Prefect, 1× Recess |

### Action Outcome Effects

All outcomes assume relevant dice pool vs. stated Ob. Success = 4+ on each die.

| Outcome | Degree |
|---------|--------|
| ≥ Ob + 1 surplus | Overwhelming |
| = Ob | Success |
| Ob − 1 | Partial |
| 0 successes | Failure |

**Ob 0 Resolution:** If modifiers reduce Ob to 0, any roll with at least 1 success counts as Overwhelming. Failure still requires 0 successes. Partial (Ob − 1 = −1) is impossible at Ob 0. Ob cannot go below 0; there is no automatic success without rolling.

**Govern (Consul Inward / Prefect):**
- Overwhelming: Prosperity +1; may also issue one Decree effect in this territory at no additional card play.
- Success: Prosperity +1.
- Partial: No Prosperity change; Stability check waived this season.
- Failure: Prosperity −1; Stability check Ob 1.

**Trade (Consul Outward / Aedile):**
- Overwhelming: Wealth +2; target faction (if Trade is directed) may offer one counter-deal at no card play cost.
- Success: Wealth +1.
- Partial: Wealth +1, but target faction may impose one condition (block future Trade for 1 season OR demand 1 Wealth at Year-End).
- Failure: No Wealth gain. If Trade targeted Schoenland route at Invasion Pressure (IP) ≥ 30: −1 Ob to next Trade in that territory (diplomatic friction).

**Diplomacy (Senator Outward / Diplomat):**
- Overwhelming: Gain 1 Influence in target territory; establish one Open Pledge with target faction at no additional card play; OR block one declared Order from another faction in this territory next season.
- Success: Gain 1 Influence in target territory; OR arrange one Open Pledge.
- Partial: Arrange one non-binding deal (no enforcement); no Influence gain.
- Failure: No effect. If Diplomacy was adversarial: target faction gains Standing +1 vs you.

**Decree (Senator Inward):**
- Overwhelming: Issue one legally binding Decree effect (use Crown Policy list for types); all factions in territory must comply or gain Standing −1 vs you; Mandate check waived.
- Success: Issue one Decree; compliance is voluntary but non-compliance costs Standing +1 vs you.
- Partial: Decree issued but contested; target faction may respond with Parliamentary Manoeuvre or own Senator card without card play cost.
- Failure: Issuing faction's Mandate −1; Standing +1 vs you from territory factions.

**Parliamentary Manoeuvre (Hafenmark Senator Inward):**
- Overwhelming: Parliament Integrity (PI) +1; block one Crown Policy this season (queued to next season); counts toward Constitutional Precedent Milestone.
- Success: Parliament Integrity (PI) +1.
- Partial: Parliament Integrity (PI) unchanged; one specific declared Order is delayed to the next resolution priority tier (not blocked, delayed).
- Failure: Parliament Integrity (PI) unchanged; Hafenmark's next Parliamentary Manoeuvre this season costs +1 Ob.

**Investigate (Tribune Inward):**
- Overwhelming: One faction's complete stat line revealed (all 5 stats); one hidden private track revealed (your choice).
- Success: One faction stat revealed (you choose which: Mandate / Influence / Wealth / Military / Stability).
- Partial: Qualitative hint — "above or below a threshold" for one stat of your choice.
- Failure: No information gained. If Investigating in another faction's territory: target faction may play one defensive card out-of-priority this season (costs target 2 Standing).

**Spy (Tribune Outward):**
- Overwhelming: Target faction's planned card in one territory is revealed to you before Phase 3 Reveal; one stat revealed; option to plant false information (target receives −1D on one roll next season if they act on the false information).
- Success: One planned card in target territory revealed to you (you see it before Phase 3 simultaneous reveal).
- Partial: Territory-level intelligence — you learn the card TYPE in target territory, not orientation or exact card.
- Failure: Nothing gained. If in enemy territory: detected. Target faction gains Standing +1 vs you.

**Muster (Legionary Inward):**
- Overwhelming: Raise 1 unit (Strength 2, Combat Power (CP) = Military ÷ 2 round up, Cohesion standard) and may immediately upgrade to Elite (Cohesion +1) at no additional card play.
- Success: Raise 1 unit (Strength 2, Combat Power (CP) = Military ÷ 2 round up).
- Partial: Raise 1 unit (Strength 2, Combat Power (CP) = Military ÷ 2 round up, Cohesion −1 from understrength muster).
- Failure: No unit raised; Wealth −1 (wasted recruitment cost).

**March (Legionary Outward):**
- Overwhelming: Move unit to adjacent territory; may immediately initiate Battle resolution if enemy present; establish control if territory is empty.
- Success: Move unit to adjacent territory; if enemy present, declare Battle (resolved Phase 4, Priority 2).
- Partial: Unit moves but Cohesion −1 from difficult march.
- Failure: Unit does not move; Stability check Ob 1.

**Ecclesiastical Suppression — Church Pontifex (base hand only):**
See B5 — Church faction card.

**Community Organizing (Organizer — Restoration only):**
Influence roll vs. Ob 2. Overwhelming: Restoration gains 1 Influence in territory + Prosperity +1. Success: Restoration gains 1 Influence in territory. Partial: no effect; territory controller may Govern without card play to offset. Failure: Church Attention Pool +1 (gathering noticed). No Thread operation. No Co-Movement card drawn.

### Order Orientation

When playing a card, rotate it Inward or Outward before resolving. Default if forgotten: Inward.

### Senate Market

6 cards face-up from Senate Deck. Purchase windows: (a) during Senator card play (Outward/Diplomacy), or (b) during Phase 2 (Negotiation) at standard cost. Purchasing adds the card permanently to your hand (available after next Recess).

| Card | Action | Cost |
|------|--------|------|
| Tribune | Covert/Intel | 1 |
| Architectus | Fortify + Govern same territory | 2 |
| Colonist | March + Govern at destination | 2 |
| Diplomat | Diplomacy at −1 Ob | 1 |
| Tribune Militum | Military at −1 Ob | 2 |
| Aedile | Trade at −1 Ob | 1 |
| Pontifex | Thread operation (Restoration / Thread-qualified factions only; Church may not purchase) | 2 |
| Praetor | Start or advance a Community Project | 1 |
| Censor | Crown only: issue one Policy. Non-Crown: block one order this season | 3 |

**Löwenritter (post-coup) Senate Market access:** Legionary, Architectus, Tribune, Tribune Militum only. Senator, Diplomat, Pontifex, and Censor are barred.

### Cooldown Track

Each faction has a 3-slot Cooldown Track for their Unique Power card. After use, place on Slot 3. Each Seasonal Accounting, all items advance one slot. At Slot 0: return to hand.

| Faction | Unique Power | Cooldown |
|---------|-------------|---------|
| Crown | Royal Decree | 2 seasons |
| Church | Excommunication | 3 seasons |
| Hafenmark | Sovereign Authority Doctrine | Once per game (not on Cooldown Track) |
| Varfell | Patient Observation | 1 season |
| Restoration Movement | Community Chorus | 2 seasons |
| Löwenritter (post-coup) | Iron Discipline | 2 seasons |

Crown Policies: same policy may not repeat for 2 seasons (tracked on Cooldown Track using policy tokens).

---

## B4 — TURN STRUCTURE

Each game round = 1 season. A full campaign = 12–20 seasons. Standard session: 3–5 seasons.

### Phase 1 — Planning (simultaneous, ~5 min)

All players simultaneously select cards from hand, place face-down in territories where they will act, with orientation chosen. **Maximum 5 cards per season** (hand may be smaller if depleted). There is no limit on the number of cards placed in a single territory beyond the 5-card-per-season maximum. NPC factions execute AI priority trees simultaneously.

### Phase 2 — Negotiation (~3 min)

Open deals: publicly declared, enforceable (breaking costs Standing −2 from betrayed faction). Sealed deals: written privately, no enforcement. Orders remain face-down.

Senate Market purchases available during this phase at standard cost.

**Solo mode:** Phase 2 is Strategic Planning. No negotiation occurs. The player may purchase from the Senate Market normally. NPC factions do not negotiate.

### Phase 3 — Reveal

All cards flipped simultaneously.

### Phase 4 — Resolution (sequential, ~8 min standard; ~20–30 min at full 5-player with all systems active)

**Priority order:**
1. Intel/Covert (Tribune)
2. Military (Legionary)
3. Domain (Consul, Prefect, Architectus, Colonist)
4. Social (Senator)
5. Thread operations (Pontifex — Senate Market version only; Weaver)
6. Special/Unique Powers (Censor, Royal Decree, Excommunication, etc.)
7. Project advancement (Praetor)

Within a priority tier: highest Stability goes first. Ties: resolve simultaneously. **Three or more factions with the same card type in the same territory:** resolve in descending Stability order, each effect applying before the next faction rolls. Ties in Stability within multi-faction conflicts: resolve left of the currently-active player in Stability order. Each resolution applies fully before the next player's card is resolved.

**Resolution procedure per card:**
1. Declare orientation → specific action.
2. Assemble dice pool from relevant faction stat (see Stat-to-Action Mapping table, B3).
3. Apply modifiers: Clock Environmental Effects, territory specials, ethical framework, Milestone Bonuses, Champion presence.
4. Roll. Determine degree (Overwhelming / Success / Partial / Failure).
5. Apply result per action outcome effects (B3).
6. If Thread operation: draw Co-Movement card. Apply three-dimensional consequence.
7. If result triggers Institutional Mandate: resolve Uphold/Compromise (see B7).

**Cascade Depth Cap (confirmed rule — BG-E-65 approved):** No single card play may trigger more than 3 immediate mechanical effects during a single resolution step. Additional triggered effects are queued and applied at Seasonal Accounting. This applies within Phase 4 only. Coup Counter events, Assert/Suppress choices, and Accounting-phase effects are not subject to this cap.

**Resolution order — Crown Policy / Parliamentary Manoeuvre / Censor (confirmed — BG-E-66 approved):**  
Crown Policy declared and effect established → Hafenmark may respond immediately with Senator Inward (interrupt, no additional card play cost) → Censor card activates last (blocks one specific order in the current resolution sequence, whichever is next in priority).

### Phase 5 — Seasonal Accounting (~5 min standard; ~15–20 min at full complexity)

Execute in strict order:
1. Apply all pending attribute changes from resolved orders.
2. Faction Stability checks: any faction that suffered ≥ 2 attribute loss this season rolls Ob = loss magnitude.
3. Advance Cooldown Track (all items move −1 slot; at 0: return to hand).
4. Clock advances: Rendering Stability (RS) baseline drift (−1 at Winter only). Theocratic Clock (TC) per formula (see B7). Invasion Pressure (IP) per Altonian pressure table. Parliament Integrity (PI) changes.
5. Church Attention Pool: resolve threshold responses. Pool resets to 0.
6. Thread Debt: outstanding tokens older than 1 season: Rendering Stability (RS) −1 per token (active drain). Serviced tokens: no active drain; permanent residual recorded.
7. Clear Thread Resonance markers (all factions reset to "not in resonance").
8. Check threshold events: draw one Event Card per threshold crossed this season.
8b. **Milestone Bonus check:** has any Milestone Bonus trigger condition been met this season? Apply immediately if so. Mark as fired (each fires once only).
9. Warden Emergence check (see B7): has a Forgetting Check been passed this season?
9b. **Vaynard-Edeyja encounter check (same-season rule):** if Warden Emergence fired at Step 9 AND Varfell has Varfell Thread Mastery (VTM) 4+ AND played Tribune (Intel) Inward in T13 this season: Edeyja speaks to Vaynard. Warden Cooperation +1 immediately. This fires in the same Accounting phase as Warden Emergence — not deferred.
10. Warden Cooperation check (see B7): have any Cooperation conditions fired this season?
11. **Update Hollow Victory modifier totals publicly.** Every player announces their current Hollow modifier running total. Record on shared Hollow Victory Scoring sheet.
12. Check victory conditions. All Deed Tokens held simultaneously = declare victory.
13. Season marker advances. If Winter (every 4th season): Year-End Accounting (B11).
