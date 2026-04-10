<!-- DEPRECATED: 2026-04-09 — SUPERSEDED BY designs/board_game/valoria_bg_v05_simulation_and_patches.md. Do not use as a mechanical reference. Retained for audit trail only. -->

# VALORIA: THE BOARD GAME
## Skeleton Ruleset v0.2
**Date:** 2026-04-01
**Authority:** Skeleton Ruleset v0.1 (2026-04-01) + audit corrections and integrations.
**Changes from v0.1:**
- Research Tracks removed; Milestone Bonuses replace them (B9).
- Löwenritter post-coup full faction sheet integrated (B5, B8, B13).
- Guilds, Ministry, Niflhel, Schoenland: NPC-only. Removed from B5. Full AI blocks in B13.
- Edeyja / Wardens integrated: board rule for T12/T13 military dissolution (B2); Warden Emergence trigger; Warden Cooperation track (B7); Edeyja NPC AI priority tree (B13).
- Thread Resonance simplified: 0–5 track → binary seasonal marker (B6).
- AER given explicit board representation (B2, B7).
- Playable faction list made explicit in B1.
- Cascade depth cap stated as provisional working rule (B4).
- Community Organizing mechanic defined (B5).
- Löwenritter peacetime default action added (B13).
- Ministry NPC AI block created from scratch (B13).

---

# PART A — SYSTEM REGISTER

## A.1 Core Systems (19 player-facing systems)

| # | System | Layer | Notes |
|---|--------|-------|-------|
| 1 | Card-Hand + Recess | Action Economy | Hand = capability. Foundation of all player agency. |
| 2 | Order Orientation | Action Economy | Inward/Outward sub-type selector. Zero overhead. |
| 3 | Senate Market | Action Economy | Hand expansion = faction development. |
| 4 | Cooldown Track | Action Economy | 3-slot wheel for Unique Powers. |
| 5 | Three Clocks (RS/TC/IP) | Victory/Loss | RS is metaphysically primary. TC and IP are politically co-equal. |
| 6 | Clock Environmental Effects | Ambient Modifier | All three clocks modify action Obs. |
| 7 | Deed Tokens | Victory | Simultaneous-holding tension. All must be held at once. |
| 8 | Hollow Victory Scoring | Victory | End-game legitimacy modifier. |
| 9 | Institutional Mandate | Political | Uphold/Compromise. Faction identity with mechanical teeth. |
| 10 | Standing Tokens | Political | Political history. Grievance and capital. |
| 11 | Crown Policy | Political | Crown sets the environment for all other factions. |
| 12 | Parliament Integrity (PI) | Political | Shared institution. Hafenmark's primary lever. |
| 13 | Thread Resonance | Thread | Binary seasonal marker: in resonance or not. |
| 14 | Thread Debt | Thread | Permanent cost of Thread operations. Cannot be fully discharged. |
| 15 | Church Attention Pool | Thread | Consequence-detection only. Church sees behaviour, not operations. |
| 16 | Co-Movement Card Deck | Thread | Three-dimensional consequence per Thread operation. P-14 compliance. |
| 17 | Community Projects | Faction/Thread | Multi-season investments. Quiet Year mechanic. |
| 18 | Champions + Wound States | Military | Named leaders as mobile tokens. Hybrid bridge. |
| 19 | Faction Structural Asymmetry | Faction | Distinct action profiles, private tracks, unique mechanics. |

**Faction-specific private tracks** (faction mat complexity, not board complexity):
- VTM: Varfell Thread Mastery Track
- RDT: Hafenmark Reformed Doctrine Track
- TD: Hafenmark Theological Dissatisfaction (private)
- AER: Church Altonian Ecclesiastical Relationship

## A.2 System Architecture

```
BOARD STATE (public, visible to all)
├── Territory map: control, Prosperity, Fortification, Champions, Presence markers
├── Three Clocks: RS (72→0), TC (15→100), IP (20→100)
├── Parliament Integrity track (0–10, starts 7)
├── Church Attention Pool (0–10, resets each season)
├── AER track (0–5, Church/Altonia relationship, starts 2) — near IP track
├── Löwenritter Coup Counter (0–4)
└── Warden Cooperation track (0–3) — near T13; inactive until Warden Emergence

FACTION MAT (private to player)
├── Card Hand (6 starting cards + purchased cards)
├── Cooldown Track (3 slots)
├── Deed Track (faction-specific conditions)
├── Standing Tokens (held)
├── Thread Resonance marker (in resonance / not in resonance this season)
└── Private tracks: VTM / RDT / TD / AER (faction-dependent)

SHARED LEDGER / REFERENCE
├── Community Project Progress Tracks
├── Restoration Movement Presence Markers (per territory)
├── Niflhel Network Depth Markers (per territory, NPC tracking)
└── Thread Debt tokens (max 3 in play at once)

REFERENCE CARDS (consult, don't track)
├── Clock Environmental Effects table
├── Thread Operation Procedure (7-step laminated card — mandatory)
├── Seasonal Accounting Checklist (10-step — mandatory)
└── Hollow Victory Scoring Sheet (pre-printed — mandatory)
```

## A.3 Advanced / Variant Rules (not in skeleton core)

| System | When Active |
|--------|-------------|
| Secondary Objectives | Default BG; disable in hybrid |
| Proxy Support | Advanced |
| Thread Veil Cards | Advanced (Baralta Einhir lineage card removed — P-08 violation) |
| Deal Tokens | Advanced negotiation variant |
| Winter Accounting / Leader Age | Long campaign only |
| Solo Mode | Variant |
| Lead/Follow Resolution | Advanced layer |

---

# PART B — RULESET v0.2

---

## B1 — OVERVIEW

**Valoria: The Board Game** is a standalone political-strategic game set on the Valorian peninsula. It is also the strategic layer of hybrid TTRPG/board game play.

**Core feel:** Powerful institutions attempting to consolidate power across a dying world. Rendering Stability (RS) degrades through sustained conflict and accelerates sharply under large-scale Threadwork. The Church of Solmund siphons Crown authority toward a long-term theocracy. Altonia watches for weakness. Every faction wins by expanding — but expansion itself tears the world further apart.

**Three mandatory game modes:**
- **Board Game (this ruleset):** Complete standalone game, 2–4 hours, 3–5 seasons per session.
- **Hybrid:** BG as strategic layer feeding into TTRPG personal-scale scenes.
- **TTRPG:** Governed by separate compiled stages.

### Playable Factions

| Faction | Available |
|---------|-----------|
| Crown | 2–5 players |
| Church of Solmund | 2–5 players |
| Hafenmark | 2–5 players |
| Varfell | 2–5 players |
| Restoration Movement | 5 players only (optional) |
| Löwenritter (post-coup) | Conditional: only if coup fires; replaces NPC Löwenritter |

### NPC-Driven Factions (never playable)

Löwenritter (pre-coup), Riskbreakers, Inquisitors, Guilds, Ministry, Niflhel, Altonia, Schoenland, and Edeyja / the Wardens are always NPC-controlled. They provide unique pressures and mechanics that drive emergent play. Their AI priority trees are in B13.

### Player Count

| Players | Mode |
|---------|------|
| 1 | Solo (Advanced Rules) |
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
| 3 | Himmelenger | Church | 5 | 2 | Grand Cathedral: TC +1/season Church controls. Church Unique Power −1 Ob here. |
| 4 | Spartfell | Crown | 3 | 2 | Altonian Border: IP threshold events here first. Invasion entry point. |
| 5 | Arnesheld | Crown/Löwenritter | 4 | 3 | Löwenritter Fortress: Martial Law −1 Ob. Fort max 4. |
| 6 | Hafenvalor | Hafenmark | 6 | 1 | Ducal Court: Sovereign Authority Doctrine here only. Major port. |
| 7 | Lowenskyst | Hafenmark | 5 | 0 | Trade Hub: all Trade +1D. Schoenland sea route. |
| 8 | Eidursjo | Guilds (NPC) | 4 | 0 | Difficult terrain: March costs 2 movement. Guild trade routes active. |
| 9 | Varfell | Varfell | 4 | 1 | Varfell Seat: private VTM research here only. Einhir ruins: Restoration Weaving −1 Ob. |
| 10 | Sigurdshelm | Niflhel (NPC) | 3 | 0 | Black Market: Niflhel Covert −1 Ob. All Trade +1 Ob. |
| 11 | Halvardshelm | Guilds (NPC) | 5 | 0 | Breadbasket: +1 Prosperity/season uncontested. Muster Ob −1. |
| 12 | Oastad | Uncontrolled | 3 | 0 | Thread Wound: RS thresholds trigger +10 early here. RS −1/season after 2 consecutive seasons of any occupation. **Southernmost rule applies (see below).** |
| 13 | Stillhelm | Uncontrolled | 2 | 0 | Southernmost Access: required for Expedition. Non-Thread orders +1 Ob. RS −1/season any occupation. **Southernmost rule applies (see below). Warden Cooperation track here (inactive until Warden Emergence).** |
| 14 | Eisengrund | Restoration (informal) | 4 | 0 | Einhir Heartland: Restoration Influence −1 Ob. Church Influence +1 Ob. |
| 15 | Schoenland | Neutral (NPC) | 5 | 1 | Altonian Trade. At IP ≥ 75: Altonian vanguard deploys. Intel orders here: visible to Altonia. |

### The Southernmost Rule (T12 and T13)

**Any military unit token placed in T12 (Oastad) or T13 (Stillhelm) by a faction that does not have a Thread-qualified presence in that territory is immediately removed from the board at the resolution step, before battle is resolved.** No Standing cost, no Stability check, no battle: the units simply cease to function. This is not Edeyja's power. It is the nature of the Southernmost — the substrate damage there is such that non-Thread configurations cannot sustain themselves.

A Thread-qualified presence means: a Restoration Movement Weaver card was played in that territory this season, OR Varfell has VTM ≥ 2, OR a practitioner with TS ≥ 30 is present (hybrid mode only).

This rule has always applied. It is why the Southernmost was never conquered during Altonian colonisation. Factions discover it by attempting and failing. Before Warden Emergence, no faction knows why it happens.

### Board Tracks (additional to territories)

**AER Track (0–5):** Small 5-step track printed on the board near the Invasion Pressure (IP) clock. Tokens placed here represent the Church's standing with Altonian power. Starts at 2. Church player updates this track at Accounting.

**Warden Cooperation Track (0–3):** Printed near T13. Greyed out / inactive until Warden Emergence fires. Once active, a wooden Warden Token sits on the track at the current Cooperation level. Represents the wardens' willingness to work alongside expedition practitioners.

### Clock Tracks

**RS:** Starts at 72. Counts toward 0. Rupture at 0 = shared loss.
**TC:** Starts at 15. Counts toward 100. TC 80 = Church Territorial Seizure event.
**IP:** Starts at 20. Counts toward 100. IP 75 = Altonian Vanguard deployed.
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
| 30–49 | Church orders: −1 Ob in Church-held territory. |
| 50–69 | Church orders: −1 Ob everywhere. Non-Church Diplomacy targeting Church: +1 Ob. Mandatory Assert/Suppress choice. |
| 70+ | As above. Church Territorial Seizure protocol active. AER begins modifying TC gains. |

**Invasion Pressure (IP) Effects:**

| IP Range | Effect |
|----------|--------|
| Below 30 | Trade with Schoenland: +1D |
| 30–59 | Trade with Schoenland: +1 Ob. All factions: +1D to Intel orders. |
| 60–74 | Trade disrupted: Schoenland Trade +2 Ob. Schoenland funds proxy at T4: +1D military there. |
| 75+ | Altonian Vanguard deployed. Invasion countdown begins. |

---

## B3 — ACTION ECONOMY

The Card-Hand system (MP-31, Concordia) is the action economy foundation. There are no Order tokens. Your hand of Action Cards is your complete list of available actions this season. Playing a card executes its action and removes it from your hand until Recess.

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
| Church | 2× Senator, 1× Pontifex (unique), 1× Consul, 1× Legionary, 1× Recess |
| Hafenmark | 2× Consul, 1× Senator, 1× Legionary, 1× Diplomat (unique), 1× Recess |
| Varfell | 2× Tribune, 1× Legionary, 1× Consul, 1× Colonist (unique), 1× Recess |
| Restoration Movement | 2× Organizer, 1× Weaver, 1× Presence Spread, 1× Project, 1× Recess |

### Order Orientation

When playing a card, rotate it Inward or Outward before resolving. Default if forgotten: Inward.

### Senate Market

6 cards face-up from Senate Deck. Purchase windows: (a) during Senator card play (Outward/Diplomacy), or (b) during Phase 2 Negotiation at standard cost. Purchasing adds the card permanently to your hand (available after next Recess).

| Card | Action | Cost |
|------|--------|------|
| Tribune | Covert/Intel | 1 |
| Architectus | Fortify + Govern same territory | 2 |
| Colonist | March + Govern at destination | 2 |
| Diplomat | Diplomacy at −1 Ob | 1 |
| Tribune Militum | Military at −1 Ob | 2 |
| Aedile | Trade at −1 Ob | 1 |
| Pontifex | Thread operation (Restoration / Thread-qualified only) | 2 |
| Praetor | Start or advance a Community Project | 1 |
| Censor | Crown only: issue one Policy. Non-Crown: block one order this season | 3 |

Löwenritter (post-coup) Senate Market access: Legionary, Architectus, Tribune, Tribune Militum only. Senator, Diplomat, Pontifex, and Censor are barred.

### Cooldown Track

Each faction has a 3-slot Cooldown Track for their Unique Power card. After use, place on Slot 3. Each Seasonal Accounting, all items advance one slot. At Slot 0: return to hand.

| Faction | Unique Power | Cooldown |
|---------|-------------|---------|
| Crown | Royal Decree | 2 seasons |
| Church | Excommunication | 3 seasons |
| Hafenmark | Sovereign Authority Doctrine | Once per game (not on cooldown track) |
| Varfell | Patient Observation | 1 season |
| Restoration Movement | Community Chorus | 2 seasons |
| Löwenritter (post-coup) | Iron Discipline | 2 seasons |

Crown Policies: same policy may not repeat for 2 seasons (tracked on Cooldown Track using policy tokens).

---

## B4 — TURN STRUCTURE

Each game round = 1 season. A full campaign = 12–20 seasons. Standard session: 3–5 seasons.

### Phase 1 — Planning (simultaneous, ~5 min)

All players simultaneously select cards from hand, place face-down in territories where they will act, with orientation chosen. **Maximum 5 cards per season** (hand may be smaller if depleted). NPC factions execute AI priority trees simultaneously.

### Phase 2 — Negotiation (~3 min)

Open deals: publicly declared, enforceable (breaking costs Standing −2 from betrayed faction). Sealed deals: written privately, no enforcement. Orders remain face-down. Senate Market purchases available during this phase.

### Phase 3 — Reveal

All cards flipped simultaneously.

### Phase 4 — Resolution (sequential, ~8 min)

**Priority order:**
1. Intel/Covert (Tribune)
2. Military (Legionary)
3. Domain (Consul, Prefect, Architectus, Colonist)
4. Social (Senator)
5. Thread operations (Pontifex, Weaver)
6. Special/Unique Powers (Censor, Royal Decree, Excommunication, etc.)
7. Project advancement (Praetor)

Within a priority tier: highest Stability goes first. Ties: resolve simultaneously. Two factions playing the same card type in the same territory against each other: both roll; higher result (by Ob margin) applies first; ties go to the player to the left of whoever is currently active.

**Resolution procedure per card:**
1. Declare orientation → specific action.
2. Assemble dice pool from relevant faction stat.
3. Apply modifiers: Clock Environmental Effects, territory specials, ethical framework, Milestone Bonuses, Champion presence.
4. Roll. Determine degree (Overwhelming / Success / Partial / Failure).
5. Apply result.
6. If Thread operation: draw Co-Movement card. Apply three-dimensional consequence.
7. If result triggers Institutional Mandate: resolve Uphold/Compromise.

**Roll results:**

| Successes | Degree |
|-----------|--------|
| ≥ Ob + 1 surplus | Overwhelming |
| = Ob | Success |
| Ob − 1 | Partial |
| 0 | Failure |

**Cascade Depth Cap (provisional working rule — confirm at playtesting):** No single card play may trigger more than 3 immediate mechanical effects during a single resolution step. Additional triggered effects are queued and applied at Seasonal Accounting. This applies to within-resolution chains only; effects that unfold naturally across seasons are not capped.

**Resolution order — Crown Policy / Parliamentary Manoeuvre / Censor:** Crown Policy is declared and its effect established → Hafenmark may respond immediately with Senator Inward (interrupt) → Censor card activates last (blocks one specific order in the resolution sequence, whichever is currently first).

### Phase 5 — Seasonal Accounting (~5 min)

Execute in strict order:
1. Apply all pending attribute changes from resolved orders.
2. Faction Stability checks: any faction that suffered ≥ 2 attribute loss this season rolls Ob = loss magnitude.
3. Advance Cooldown Track (all items move −1 slot; at 0: return to hand).
4. Clock advances: RS baseline drift (−1 at Winter only). TC per Church activity formula. IP per Altonian pressure table. Parliament Integrity (PI) changes.
5. Church Attention Pool: resolve threshold responses. Pool resets to 0.
6. Thread Debt: outstanding tokens older than 1 season: RS −1 per token (active drain). Serviced tokens: no active drain; permanent residual recorded.
7. Clear Thread Resonance markers (all factions reset to "not in resonance").
8. Check threshold events: draw one Event Card per threshold crossed this season.
9. Warden Emergence check (see B7): has Forgetting Check been passed this season?
10. Warden Cooperation check (see B7): have any Cooperation conditions fired this season?
11. Check victory conditions. All Deed Tokens held simultaneously = declare victory.
12. Season marker advances. If Winter (every 4th season): Year-End Accounting (B11).

---

## B5 — PLAYABLE FACTION CARDS

All rolls: pool = relevant faction stat (1–7). Dice: d6. Success = 4+. Majority 1s = Failure regardless of other dice.

**Ethical framework modifiers** apply before rolling:
- Crown (Virtue Ethics): public, visible actions −1 Ob. Covert or morally ambiguous: +1 Ob.
- Church (Divine Command): doctrine-aligned −1 Ob. Thread-supporting: +2 Ob.
- Hafenmark (Categorical Imperative): procedurally grounded, precedent-following −1 Ob. Ad hoc or precedent-breaking: +1 Ob.
- Varfell (Epistemic Reason): evidence-based Intel −1 Ob. Emotional or reactive: +1 Ob.
- Restoration Movement (Rawlsian): community-benefiting −1 Ob. Hierarchical or exclusionary: +1 Ob.
- Löwenritter (Military Honor): orders protecting Valorian civilians or sovereignty −1 Ob. Orders advancing personal or factional gain at Valoria's expense: +2 Ob.

---

### FACTION: THE CROWN

**Stats:** Mandate 5 · Influence 5 · Wealth 4 · Military 4 · Stability 4
**Ethical Framework:** Virtue Ethics
**Leader:** King Almud Almqvist
**Conviction:** [EDITORIAL BG-E-59 — proposed: "The state is the only legitimate vessel of order."]
**Political Decision Style:** Precedent

**Institutional Mandate:** "The monarchy provides the order that protects Valoria — and all other institutions serve the monarchy's order."

**Mandate trigger events:**
- Church refuses a Crown directive in Crown territory
- Varfell operates Intel without Crown awareness in Crown territory
- Hafenmark Parliamentary ruling contradicts Crown decree
- Any faction allies with Altonia without Crown approval

**Unique Power — Royal Decree** (2-season cooldown): Roll Mandate vs Ob 2. Success: one faction attribute change (any faction, ±1) takes effect immediately. Failure: Crown Mandate −1. Effect declared before rolling.

**Crown-Exclusive — Policy Instruments:** Once per season (in addition to normal card plays), Crown may issue one Policy if Mandate ≥ 4. Same policy cannot repeat for 2 seasons.

| Policy | Effect | Downside |
|--------|--------|----------|
| Royal Taxation | All Trade this season: +1 Wealth to Crown | Non-Crown Trade Ob +1 |
| Conscription Mandate | All Muster: −1 Ob this season | Mustered units begin Cohesion −1 |
| Free Trade Decree | IP −1; Schoenland Trade +1D | TC +1 |
| Curfew | Intel/Covert in Crown territories: +2 Ob | Niflhel Standing +2 |
| Parliamentary Session | All factions: one additional Diplomacy this season | Crown Mandate check Ob 1 on failure; TD −1 |
| Emergency Powers | Crown executes one order face-down (revealed at resolution) | Hafenmark gets free Parliamentary Manoeuvre; TC +1; TD +1 |
| Supremacy Decree (once/game) | Named faction treats Crown Mandate as +2 higher for all opposed rolls this season | All other factions: Standing +1 vs Crown |

**Victory — Constitutional Stability (Primary):** All 5 Deed Tokens held simultaneously + PI ≥ 3 at Accounting.

| Deed | Condition |
|------|-----------|
| 1 | Mandate ≥ 5 |
| 2 | Control Valorsplatz + Gransol + ≥ 2 other territories |
| 3 | TC < 60 and IP < 75 simultaneously |
| 4 | Parliament Integrity ≥ 5 |
| 5 | Torben Loyalty ≥ 5 |

**Victory — Dominion (Alternate):** Controls ≥ 8 territories AND one Submission Condition met simultaneously at Accounting.

| Submission Condition | How Achieved | Standing Cost |
|---------------------|-------------|---------------|
| Church recognizes Crown supremacy over religious appointments in Crown territories | Deal Token (Open Pledge) accepted, OR TC = 0 | +2 Standing vs Crown from Church; Baralta Mandate trigger |
| Varfell formally subordinates Intel to Crown oversight | Varfell VTM ≤ 1 OR Crown captures Vaynard + all Varfell territories | +1 Standing vs Crown from Varfell |
| Hafenmark surrenders Parliamentary independence | PI = 0 OR Baralta Compromise count ≥ 4 | +2 Standing vs Crown from Hafenmark; Riskbreakers Priority 2 fires against Crown |

---

### FACTION: THE CHURCH OF SOLMUND

**Stats:** Mandate 5 · Influence 6 · Wealth 5 · Military 4 · Stability 5
**Ethical Framework:** Divine Command
**Leader:** Confessor Arne Himlensendt
**Conviction:** Faith
**Political Decision Style:** Evidence

**Institutional Mandate:** "Solmund's doctrine is the rightful framework for all governance — secular authority is derivative and conditional."

**Church-Exclusive — TC as Resource:** TC is simultaneously the Church's victory track and spending resource. Declared before rolling; −1 TC spent → +1D to any Church action. Maximum: 2 TC per roll.

**Church-Exclusive — Altonian Ecclesiastical Relationship (AER):** Shared ledger track, 0–5, starts at 2. Full rules in B7.

**Church-Exclusive — Mandatory Theocratic Assert/Suppress:** Each season TC > 50, Church must choose:
- **Assert:** TC +1. All secular faction Mandate triggers fire. Riskbreakers evaluate Priority 3.
- **Suppress:** TC +0. AER −1. Himlensendt Renown −1.
No neutral option. Announced at Phase 5 Accounting.

**Church-Exclusive — Inquisitors:** Unit type deployable via Senator (Inward) with Church flag. While deployed in a territory: +2 to Attention Pool per season present. Can open Heresy Investigations without additional card play. Moving an Inquisitor requires a Senator card. Inquisitors withdraw if territory is attacked; they are not combat units.

**Unique Power — Excommunication** (3-season cooldown): Roll Mandate vs target leader's Mandate (or Ob 2 for non-leaders). Overwhelming: target Mandate −1; barred from Church territories 1 season; Reputation −1 all factions. Success: Mandate −1 only. Failure: Church Mandate −1; target Mandate +1 (martyr sympathy).

**Victory — Holy State (Primary):** TC ≥ 70 + Mandate ≥ 5 + control Himmelenger + control Valorsplatz + AER ≥ 3.

| Deed | Condition |
|------|-----------|
| 1 | TC ≥ 40 |
| 2 | Church Mandate ≥ 5 |
| 3 | Control Himmelenger continuously for 2 seasons |
| 4 | Control Valorsplatz |
| (Gate) | AER ≥ 3 (not a Deed; required to declare victory) |

**Victory — Dual Theocracy (Alternate):** TC ≥ 60 + AER = 5 + IP ≤ 30. Theological governance through diplomatic mastery rather than military conquest.

---

### FACTION: HAFENMARK

**Stats:** Mandate 4 · Influence 4 · Wealth 5 · Military 3 · Stability 4
**Ethical Framework:** Categorical Imperative
**Leader:** Duchess Inge Baralta
**Conviction:** [EDITORIAL BG-E-51 — proposed: "Faith is not mediated — it is lived. Anyone who is truly faithful can hear Solmund. Anyone who cannot should not rule."]
**Political Decision Style:** Investigation

**Institutional Mandate:** "Constitutional process is the only legitimate source of authority."

**Hafenmark-Exclusive — Reformed Doctrine Track (RDT, 0–6):** Measures spread of Reformed Doctrine (direct access to Solmund, without Church mediation). Replaces Ecclesiastical Claim entirely.

**Gaining RDT:**
- Senator card (Outward) in non-Church territory: Ob 2. Success: RDT +1.
- TC rises above 50 AND Baralta has a unit in that territory: RDT +1.
- Crown issues Emergency Powers without Parliamentary check: RDT +1.
- Any faction publicly Compromises their Institutional Mandate: RDT +1.

**Losing RDT:**
- Church Excommunicates Baralta: RDT −2.
- Baralta publicly Compromises her own Mandate: RDT −2.
- RS drops below 30: RDT −1/season.

**RDT Effects:**

| RDT | Effect |
|-----|--------|
| 0–1 | No mechanical effect |
| 2 | TC gains this season halved (rounded down) |
| 3 | Church Inquisition Autonomy threshold rises: Attention Pool must reach 8 (not 7) |
| 4 | TC capped at current level + 5 for remainder of game |
| 5 | Reformed Settlement available (once/game) |
| 6 | All Diplomatic actions targeting Hafenmark: +1 Ob |

**Reformed Settlement (RDT 5, once/game):** Baralta declares the theological right of direct faithful access. Church must respond:
- **Resist:** TC +3; RDT +1 (martyrdom); Hafenmark +1 Standing, +1 Deed Token.
- **Accommodate:** TC −5; Church Mandate trigger; Church Stability −1; AER −2. [EDITORIAL BG-E-50: Cardinal schism mechanics.]
- **Ignore:** RDT +1 next season. [EDITORIAL BG-E-62: confirm these three responses cover all canon outcomes.]

**Hafenmark-Exclusive — Theological Dissatisfaction (TD, 0–5, private):** Tracked privately on faction mat. Other players observe effects, not the score.

**Gaining TD:** Crown issues Emergency Powers (+1); Crown submits to Altonian pressure without resistance (+1); Crown fails to respond to Church incursion in Crown territory (+1).
**Losing TD:** Almud issues Parliamentary Session (−1); Crown collaborates with Hafenmark on policy (−1).

**TD Effects:**

| TD | Effect |
|----|--------|
| 0–2 | No effect |
| 3 | Hafenmark +1D Diplomatic actions targeting Crown |
| 4 | Baralta may declare Almud theologically unworthy publicly: Crown −1 Deed Token; Hafenmark +1 Standing vs Crown |
| 5 | Rival Succession Claim: Hafenmark +1D all orders in Crown-adjacent territories; no Standing penalty for seizing Crown territories if Civil War fires |

**Unique Power — Sovereign Authority Doctrine (once/game):** Hafenvalor only. Roll Mandate vs Ob 4. Overwhelming: TC −3, Church Mandate −1, Heresy Investigation blocked this season. Success: TC −2, Church Mandate −1, Investigation opens against Baralta. Failure: TC +1, Investigation fires, Baralta Mandate −1.

**TC Passive Suppression:** While Baralta's Mandate ≥ 4: TC −1/season. Pauses if Mandate drops below 4.

**Victory — Reformed Valoria (Path A):** Reformed Settlement completed + PI ≥ 3 + 3 Deed Tokens.
**Victory — Theological Supremacy (Path B):** RDT = 6 + TD = 5 + 2 Deed Tokens.
**Victory — Parliamentary Consolidation (Path C):** 4 Deed Tokens + PI ≥ 4.

---

### FACTION: VARFELL

**Stats:** Mandate 3 · Influence 4 · Wealth 3 · Military 4 · Stability 4
**Ethical Framework:** Epistemic Reason
**Leader:** Duke Magnus Vaynard
**Conviction:** [EDITORIAL BG-E-53 — proposed: "The strongest thread is the one others cannot see — and I have spent my life learning to pull it."]
**Political Decision Style:** Investigation

**Institutional Mandate:** "Information is the truest form of power — and all other power is information in disguise."

**Varfell-Exclusive — Thread Mastery Track (VTM, 0–5):** Private at VTM 0–2; publicly visible (board marker) at VTM 3+.

**Gaining VTM:**
- Tribune (Intel) card on Thread-active territory (faction in Thread Resonance this season): VTM +1.
- Southernmost Expedition season completed with Varfell unit in T13: VTM +1.
- Thread Debt incurred by any faction: VTM +1 (Vaynard perceives the substrate strain).
- Patience + Casus Belli combination in RS-affected territory: VTM +1.
- Riskbreakers expose a Vaynard Casus Belli: VTM −1.

**VTM Effects and Southernmost Access:**

| VTM | Southernmost Access | Capability |
|-----|--------------------|-----------:|
| 0–1 | None | — |
| 2 | First Layer | Varfell always in Thread Resonance in T9. Qualifies as Thread-qualified presence in T12/T13. |
| 3 | Deep Layer | Once/game: preview top 2 Co-Movement cards before an order; keep either. VTM 3 is publicly visible. |
| 4 | Deep Layer without Restoration guide | Patience Protocol max → 6. Casus Belli Ob −1. |
| 5 | Core zone | Once/game: choose outcome of one Co-Movement card draw. Always produces Thread Debt token + RS −1. [EDITORIAL BG-E-63: P-14 compliance confirmation required.] |

**Victory — Intelligence Hegemony (Path A):** VTM ≥ 3 + all other factions' stats revealed at least once + 3 Deed Tokens + control 3 territories.
**Victory — Southernmost Dominion (Path B):** Control T12–T13 + VTM ≥ 3 + Southernmost Expedition complete (any zone) + 2 Deed Tokens.
**Victory — Thread Supremacy (Path C, hardest):** VTM = 5 + RS ≥ 50 + control 3 territories including T13. The hardest victory in the game: Vaynard must exploit the substrate without breaking it.

---

### FACTION: RESTORATION MOVEMENT (Optional 5th Player / NPC default)

**Stats:** Mandate 2 · Influence 3 · Wealth 2 · Military 0 · Stability 3
**Ethical Framework:** Rawlsian
**Leader:** Collective (no named Champion; Dahl Erikssen as informal figure — TS 18)

**Institutional Mandate:** "The community is the only legitimate political unit."

**Restoration-Exclusive — Presence Markers (8 total):** Military force cannot remove Presence markers. Only successful Heresy Investigations or Community Project disruption removes them. One Presence Spread action moves markers into adjacent territories organically.

**Two Action Types (distinct — P-08 fix):**
1. **Community Organizing** (Organizer card, rendered-world): Influence roll vs Ob 2. Success: Restoration gains 1 Influence in territory. Overwhelming: 1 Influence + Prosperity +1. Failure: territory controller may Govern without card play to offset. No Thread operation. No Co-Movement.
2. **Community Weaving** (Weaver card, Thread operation): Ob 2, −1 Ob per Presence marker in territory. Always draws Co-Movement card. Always produces three-dimensional consequences.

**Unique Power — Community Chorus** (2-season cooldown): All Presence markers in the same territory or adjacent territories contribute to a shared Weaving this season. Combine all Ob reductions. One Co-Movement card drawn (not one per marker). RS +1 if Overwhelmingly successful.

**Thread Resonance and Restoration:** Restoration always gains Thread Resonance in any territory where they have a Presence marker, in addition to standard resonance triggers.

**Victory (if played):** Restoration Network complete — 5 Presence markers in 5 non-adjacent territories, maintained for 2 consecutive seasons — + RS ≥ 50 at game end. Alternatively: Co-Victory with any faction achieving Constitutional Stability while RS ≥ 50.

---

### FACTION: LÖWENRITTER (post-coup only)

**Activation:** The Löwenritter begin as NPC-controlled (partial sheet, see B13). If the Coup Counter reaches 4 and coup fires successfully (Military vs Ob 3), the Löwenritter gain this full sheet. In a 4-player game they remain NPC-controlled even post-coup. In solo play, the Löwenritter post-coup may be played as the solo faction.

**Stats (post-coup):** Mandate 3 · Influence 2 · Wealth 3 · Military 6 · Stability 5
**Ethical Framework:** Military Honor
**Leader:** Grandmaster Sigrid Ehrenwall (Late 50s)
**Conviction:** Valoria endures, whatever the cost.

**Institutional Mandate:** "The Löwenritter exist to protect Valoria when no one else will. We hold until Valoria can govern itself."

**Mandate trigger events:**
- Church seizes a Löwenritter-governed territory without military response: trigger.
- Parliament Integrity (PI) drops to 0 during Löwenritter rule: trigger.
- Emergency Powers issued more than twice in one year: trigger.
- Invasion Pressure (IP) crosses 75 without a military order that season: trigger.

**Governing State — Permanent Martial Law:** All Crown territories are under Martial Law from the moment the coup fires. This is the structural reality of military government.
- All Military orders in governed territory: −1 Ob.
- All non-Military orders by any faction in governed territory: +1 Ob.
- Parliament Integrity (PI): −3 immediately on coup. Recovers only through Löwenritter Parliamentary Sessions or installation of a legitimate successor.

**Conscription:** Once per year at Year-End Accounting, may raise one unit without a Legionary card. Territory conscripted from: Prosperity −1.

**Card Hand:** 3× Legionary, 1× Tribune, 1× Prefect, 1× Recess.
**Senate Market access:** Legionary, Architectus, Tribune, Tribune Militum only.

**Unique Power — Iron Discipline** (2-season cooldown): Any one Löwenritter unit this season is immune to Rout and Cohesion degradation. Declare before battle resolves.

**What Happens to Almud:**
- Almud in Valoria at coup: house arrest. Token in Valorsplatz; no faction card; no card plays. Factions may liberate him (Military vs Ob 3 in Valorsplatz). If liberated, he may attempt to reclaim Crown (Parliamentary Session, Ob 2, PI-modified) or enter exile.
- Soft coup (Almud yielded command authority): he remains nominally present with 1 Senator card play per season (Diplomacy Outward only).
- Elske and Torben arcs activate immediately on coup, regardless of prior state.

**Deed Tokens:**

| Deed | Condition |
|------|-----------|
| 1 | TC < 50 (suppressed theocratic overreach) |
| 2 | IP < 60 (deterred Altonian invasion) |
| 3 | RS > 40 (the world is not dying on their watch) |
| 4 | PI ≥ 4 (maintained constitutional structure despite military rule) |
| 5 | Succession candidate located: Elske free, OR Torben at Loyalty ≥ 6 |

**Victory — Regency Resolution (Primary):** All 5 Deed Tokens held simultaneously AND a legitimate successor installed (Elske confirmed by Parliamentary Session Ob 3, or Torben retrieved at Loyalty ≥ 6 and confirmed). At succession: Löwenritter hand over military command. Shared victory state — they saved Valoria and left.

**Victory — Military Consolidation (Alternate):** Only available if Regency Resolution has not fired after 8 seasons of Löwenritter rule. Requires: control ≥ 8 territories + Military ≥ 5 + RS > 35 + TC < 60. Hollow Victory modifier: −2 Deeds from accumulated Standing tokens. If PI = 0 when this fires: victory is void.

**Coalition Dynamics Post-Coup:**
- Church: primary adversary. TC rising fills the governing legitimacy vacuum that Martial Law creates. Löwenritter have no Senator cards to fight it diplomatically.
- Hafenmark: reluctant allies. Baralta despises the coup but shares TC suppression as a goal. Löwenritter need Hafenmark's political capability; Hafenmark needs Löwenritter not to destroy Parliament further.
- Guilds (NPC): natural partners. Commerce functions under security.
- Riskbreakers: the Löwenritter's own shadow apparatus may turn against them if Ehrenwall overreaches (Almud Mandate ≥ 6 with Emergency Powers ≥ 2 times: Riskbreakers evaluate Crown's own military orders).

---

## B6 — THREAD SYSTEMS

### Thread Resonance (simplified from v0.1)

Thread Resonance is a binary seasonal marker, not a track. A faction is either **in Thread Resonance** or **not in Thread Resonance** this season. The marker is held on the faction mat (a token, flipped or placed) and cleared at Accounting Step 7.

**Gaining Thread Resonance this season:**
- A Thread operation occurs in or adjacent to a faction's controlled territory.
- A Co-Movement card effect targets the faction.
- RS drops below a threshold this season (all factions gain Thread Resonance).
- Restoration Movement faction: also gains Thread Resonance in any territory with a Presence marker.
- Varfell VTM ≥ 2: always in Thread Resonance in T9. Always qualifies for Thread-active territory checks.

**While in Thread Resonance:**
- +1D to Intel orders targeting practitioners or Thread-active sites.
- Senate Market purchase of Pontifex card: −1 cost.
- Faction qualifies for Thread-qualified presence test for T12/T13 (combined with appropriate card play).

**Thread Resonance for qualified factions only** (Restoration Movement, Varfell VTM ≥ 2, or faction with TS ≥ 30 agent present in hybrid mode):
- May ask one yes/no question about RS (above or below a threshold) this season.
- May spend Thread Resonance marker to: cancel one Co-Movement card effect targeting them, OR contribute +1D to Restoration Community Weaving in their territory.

**Thread Witness Nodes:** When a Community Weave Project is completed, the territory gains a permanent Thread Witness Node marker. Any Thread operation in this territory draws an additional Co-Movement card.

### Thread Debt

When a Thread-qualified faction executes a Thread operation against temporal flow (or Vaynard uses VTM 5): incur 1 Thread Debt token at −1 Ob.

**Thread Debt tokens:**
- Active drain: RS −1 per outstanding unserviced token per season.
- Service: faction executes a Mend-equivalent action (Restoration Weaver card in same territory, or spend Thread Resonance marker while qualified). Serviced token: active drain ceases. Permanent residual RS −0.5 recorded on faction ledger.
- Maximum 3 Thread Debt tokens simultaneously. At 3: no further Debt incurrence until reduced to 2.
- Church may use outstanding Thread Debt as grounds for automatic Heresy Investigation: Ob −1 if target faction holds ≥ 2 tokens.

**Year-End Thread Debt resolution:** All residual RS fractions sum to whole number and apply to RS track.

### Church Attention Pool

Tracks social indicators of Thread and heretical activity. The Church detects consequences, not operations.

**Pool accumulates from:**
- Unauthorized community gathering reported in any territory: +1 Attention
- Unexplained structural/social change in territory (GM/NPC AI interprets Thread operation visible effects): +2 Attention
- Einhir artefact surfaces (Event Card C-13): +2 Attention
- Restoration community gathering in Church-adjacent territory: +3 Attention
- Faction behaviour consistent with heretical influence in multiple territories: +1 per territory showing anomaly

**Attention thresholds (pool resets each season):**

| Pool | Response |
|------|----------|
| 3 | Church opens one Heresy Investigation (free, no card play) |
| 5 | TC +1 |
| 7 | Inquisitor protocol: all Thread-active factions −1D to covert/Intel this season. Inquisition Autonomy fires. (Modified to 8 if RDT ≥ 3) |
| 10 | Church Crusade: Templar units may deploy anywhere in Church territory without Muster card |

**Thread Operation Procedure (reference card — print and laminate):**
1. Declare card (Weaver or Pontifex) and orientation.
2. Declare territory and Thread operation type.
3. Apply Ob modifiers: RS environmental, Presence markers, Thread Debt, Champion.
4. Roll. Determine degree.
5. Apply result.
6. Draw Co-Movement card. Apply all three dimensional effects.
7. Check Attention Pool: does this operation's visible consequences add Attention? Apply.

### Co-Movement Cards (P-14 compliance)

Every Thread operation draws one Co-Movement card. Thread Witness Node territories draw two (apply both). Cards cannot be declined. Cards produce consequences across three axes:
1. **Actualized dimension:** RS change.
2. **Epistemic dimension:** Information revealed, concealed, or distorted.
3. **Temporal dimension:** History/continuity marker — Project disruption, Pledge complication, or NPC relationship change.

20-card base deck + GT-02 additions (approved). Co-Movement cards cannot be cancelled except by a qualified faction spending its Thread Resonance marker.

---

## B7 — POLITICAL SYSTEMS

### Institutional Mandate — Uphold / Compromise

Each faction has a stated Institutional Mandate. When a trigger event occurs, the faction must respond:

- **Uphold:** Act consistently with Mandate, even at cost. Earns 1 Renown on Champion + 1 Stability. No mechanical benefit from the triggering situation.
- **Compromise:** Act against Mandate for strategic advantage. Earns the mechanical benefit. Costs: 1 Standing token (visible to others) + 1 Stability.

In hybrid mode: if PC faction leader's personal Belief arc contradicts the faction's Uphold/Compromise pattern, Hollow Victory condition activates.

### Standing Tokens

**Gaining Standing against another faction:**
- That faction breaks an Open Pledge in your favour.
- That faction executes Brutal disposition against Valorian civilians.
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

3+ Standing against one faction from you: their Diplomacy targeting you automatically fails. 5+: they cannot ally with you or give you Deal Tokens.

### Parliament Integrity (PI, 0–10)

Shared institution. Starts at 7.

| PI | Effect |
|----|--------|
| ≥ 5 | Parliamentary Manoeuvres available to Hafenmark. Crown Policy requires Mandate ≥ 4. |
| 3–4 | Parliamentary Manoeuvres +1 Ob. Crown Policy Ob −1 (no check needed). |
| ≤ 2 | Parliament non-functional. Hafenmark loses Parliamentary Manoeuvre. Crown governs by decree. TC +2/season. |

PI degrades: Crown Emergency Powers (−1), Church Territorial Seizure (−1), Löwenritter Coup (−3).
PI recovers: Hafenmark Parliamentary Manoeuvre success (+1), Crown Parliamentary Session policy (+1).

### Altonian Ecclesiastical Relationship (AER, 0–5)

Church's standing with Altonian power. Physical track on board near IP clock. Starts at 2.

| AER | TC Effect | IP Effect |
|-----|-----------|-----------|
| 0–1 | No modification | IP escalates normally |
| 2 | Neutral | Neutral |
| 3 | TC environmental effects +1 level | IP vanguard threshold rises: 76 → 80 |
| 4 | TC gains > 3/season treated as +4 | Altonia will not invade while AER ≥ 4 |
| 5 | Once/game: any order targeting Church interests fails automatically | IP fixed at 50 and held |

AER gaining: TC crosses 30/50/70 threshold (+1 each), successful Heresy Investigation removes Restoration Presence (+1), Church issues Interdict (+1).
AER losing: TC drops below threshold (−1), Church Stability < 3 (−1), Reformed Settlement occurs at RDT 5 (−2).

### Warden Cooperation Track (0–3)

**Inactive until Warden Emergence.** Printed near T13 (Stillhelm) on the board with a 3-step marker track. The Warden Token sits on this track once Edeyja's faction is visible.

**Warden Emergence Trigger:** At Seasonal Accounting Step 9, check: has any faction's Southernmost Expedition completed a Season 1 (Approach) action this season AND passed the Forgetting Check (Success or Overwhelming result on the Forgetting Check roll)? If yes: Warden Emergence fires.

- The Warden Token is placed on the track at position 0.
- The expedition faction's player is told: "The wardens see you. Someone has been here all along."
- All other factions learn only: a Warden Token has appeared on T13.
- The T13 territory entry now lists Edeyja and the Wardens as a presence (NPC, see B13).
- The Warden Token is a permanent board marker — it does not move unless Warden Cooperation changes.

**Forgetting Check:** When a faction's expedition piece enters T13 for the first time, the Forgetting Check fires. Roll Spirit + Thread Sensitivity proxy (Ob 1; Restoration Weaver presence: −1 Ob; VTM 2+: −1 Ob). Overwhelming: full knowledge retained; faction gains information about the Calamity's mechanism (GM reveals one fact from the Warden Working Libraries — see Hybrid Interface). Success: facts retained; the weight fades by morning. Partial: emotional impressions, dread without content. Failure: nothing operational; the season was spent and nothing was brought back.

**Warden Cooperation levels:**

| Level | Edeyja's Stance | Effect |
|-------|----------------|--------|
| 0 | Observes only | Wardens do not engage expedition factions. Southernmost Expedition Ob unmodified. |
| 1 | Acknowledges competent practitioners | Southernmost Expedition seasonal actions: −1 Ob. RS drain from Warden-managed mending in T12/T13 reduced by 0.5/season. |
| 2 | Works alongside | RS +1 per completed Expedition season (wardens assist directly). Deep Layer accessible to Restoration Movement without VTM gate. |
| 3 | Active collaboration | Ceiral Ritual unlocked. RS +5 on successful Ritual completion. Edeyja provides knowledge inaccessible anywhere else (Calamity mechanism, Locked Zone nature, pre-Calamity methodology — campaign-altering). |

**Advancing Warden Cooperation:**
- Practitioner with VTM ≥ 3 (or TS 40+ in hybrid) succeeds in Thread operation at T13 primary site: +1.
- Two consecutive seasons of expedition presence in T13 without any military units: +1.
- VTM 4+ practitioner reaches T13 and completes an Intel action (Vaynard's understanding recognized by Edeyja): +1.

**Reducing Warden Cooperation:**
- Military unit placed in T12 or T13 by expedition faction: −1 (disruption of the work).
- Thread Debt incurred in T12 or T13: −1 (straining the substrate she is maintaining).
- Niflhel Network Depth ≥ 1 detected in T13: −1 per season until resolved (supply chain disturbance).

---

## B8 — MILITARY

### Unit Types

Each faction's Military stat = maximum active units simultaneously. Mass Battle resolution per Mass Battle v3 (approved).

| Type | Martial | Cohesion | Notes |
|------|---------|---------|-------|
| Standard | 2 | 3 | Default Muster result. Str 2, CP = Military ÷ 2. |
| Elite | 3–4 | 4–5 | Specific faction conditions required. |
| Knights Templar (Church) | 4 | 5 | Immune to Co-Movement Cohesion penalties. +2D vs practitioners. |
| Inquisitors (Church) | 1 | 2 | Deploy via Senator Inward. +2 Attention Pool/season present. |
| Hired Blade (Guilds NPC) | 2 | 3 | Offensive only. 1-season duration. Cannot garrison. |

### Mass Battle (BG)

Per Mass Battle v3 (approved), Part B. Resolution occupies Priority 2 slot. 3–5 minutes per engagement.

**Muster output (per Muster action):** 1 unit with Strength 2, CP = faction Military ÷ 2 (round up). Deploys following season.

**Battle outcome → faction consequences:**
- Unit destroyed: faction Military −1 (subject to ±2/season cap).
- Battle lost (defending force routed): Stability check Ob 1.
- Campaign-scale defeat: Stability check Ob 2, Mandate −1.

**Tactic card hands:** Each faction receives 4 shared tactic cards + 2 faction-specific cards at game start. Refresh each season. See Mass Battle v3 Part B.4 for full tactic card list.

### Champions

Named faction leaders as mobile tokens.

| State | Condition | Effect |
|-------|-----------|--------|
| Active | Default | +1D all units in same territory. Diplomacy +1D. Stability checks −1 Ob. |
| Wounded | Lost battle in their territory | Champion bonuses halved; Renown gain paused. Govern in territory restores to Active. |
| Captured | Enemy takes territory while Champion Wounded | Removed from board. Rescue: Military action vs captor. Ransom: 3 Wealth. |
| Convalescing | Returned from capture | Home territory, 2 seasons recovery; no bonuses. |

**Champion Renown (0–5):** Earned from victories, Uphold events. Renown 3+ unlocks faction Unique ability. Renown 5: Conviction Intervention (once/game). [EDITORIAL BG-E-27, BG-E-33]

### Löwenritter Military (post-coup)

**Military stat: 6.** Maximum active units: 6. Faction may field units up to CP 6. Starting Cohesion ceiling: 7.

**Conscription (Year-End Accounting):** Once per year, raise one unit (Strength 2, CP 3) without Legionary card. Territory of conscription: Prosperity −1.

**Ehrenwall as General:** CR derived from Presence 3 + Cognition 4 → CR 4. All Löwenritter units within CR range: Morale floor 1. Wounds on Ehrenwall carry over as +1 Ob to tactic execution.

---

## B9 — MILESTONE BONUSES

Replaces Research Tracks entirely. No tracking positions. No Accounting steps. Each bonus fires automatically the first time its trigger condition is met; it is then permanent for the remainder of the game.

### Crown

| Milestone | Trigger | Bonus (permanent) |
|-----------|---------|------------------|
| Mandate Authority | Crown holds Mandate ≥ 5 for 3 consecutive seasons | All Govern orders: −1 Ob permanently |
| Military Tradition | Champion Renown reaches 4 | Royal Decree cooldown → 1 season |

### Church

| Milestone | Trigger | Bonus (permanent) |
|-----------|---------|------------------|
| Doctrinal Reach | TC crosses 50 for the first time | Preach actions generate +0.5 TC/season (accumulates; applies as whole numbers at Year-End) |
| Inquisition Network | Attention Pool has reached threshold 7 three or more times total across the game | Heresy Investigations auto-open in Church territory without card play |

### Hafenmark

| Milestone | Trigger | Bonus (permanent) |
|-----------|---------|------------------|
| Constitutional Precedent | Hafenmark's Parliamentary Manoeuvre succeeds 4 times total | One Parliamentary ruling per game is irrevocable (cannot be overridden by Crown Policy that season) |
| Maritime Commerce | Trade in coastal territories (T6, T7) succeeds 5 times total | Schoenland route: +1 Wealth regardless of Invasion Pressure (IP) |

### Varfell

| Milestone | Trigger | Bonus (permanent) |
|-----------|---------|------------------|
| Einhir Knowledge | VTM reaches 3 | VTM advance conditions fire at +1 rate (each qualifying source counts double for one advance) |
| Intelligence Network | All other factions' stats revealed at least once | One faction's full stat line permanently visible to Varfell (player chooses which) |

### Restoration Movement

| Milestone | Trigger | Bonus (permanent) |
|-----------|---------|------------------|
| Community Resilience | 3 Community Projects completed total | Community Projects cannot be disrupted by Heresy Investigation (battle and control change still apply) |
| Thread Recovery | Community Weave Project completed in T14 (Einhir Heartland) | RS +1 at every subsequent Year-End where Restoration has Presence in T14 |

### Löwenritter (post-coup)

| Milestone | Trigger | Bonus (permanent) |
|-----------|---------|------------------|
| Iron Administration | Löwenritter successfully Governs 4 territories in one season | Ministry delay mechanic does not apply to Löwenritter orders (bureaucracy neutralized) |
| Legitimate Force | TC < 50 held for 3 consecutive seasons during Löwenritter rule | Mandate rises to 4 (military government earns grudging recognition) |

---

## B10 — COMMUNITY PROJECTS

Projects are started in any territory with Presence. Progress Track of 1–5 (scope varies). Any faction with presence in the territory may advance it 1 step per season (costs Domain card for non-Restoration factions; free for Restoration with Presence present).

**Disruption conditions:**
- Battle in territory: Progress −2.
- Territory changes control: Progress −1.
- Heresy Investigation active there: −1 per season.

**Project types:**

| Project | Scope | Completion Effect |
|---------|-------|------------------|
| Community Weave | 3 | RS +2; Restoration Influence +2 in territory; permanent Thread Witness Node (additional Co-Movement card drawn per Thread operation here) |
| Einhir Memory Recovery | 4 | GM introduces one historical fact about the Calamity; VTM +1 for any contributing faction; RS +1 |
| Restoration Network | 5 | Restoration gains Presence in 2 adjacent territories even if disrupted; IP −1 |
| Fortification | 3 | Territory Fort +1 at no Wealth cost (any faction) |
| Diplomatic Mission | 2 | Faction Reputation +1 all factions; next Diplomacy −1 Ob (any faction) |
| Southernmost Expedition | 4 | Multi-season. Per season: check Forgetting Check; advance Warden Cooperation if conditions met. Completion: faction has reached Core Zone. Edeyja will speak to them if Warden Cooperation ≥ 1. |

---

## B11 — YEAR-END ACCOUNTING

Fires every 4th season (Winter).

1. **Annual Attrition:** Each unit that fought ≥ 1 battle this year: Cohesion check Ob 1. Failure: Cohesion −1.
2. **Sustenance:** Each military unit costs 1 Prosperity from controlling territory per year. Territories below Prosperity 2: excess units disbanded.
3. **Thread Debt residuals:** Sum all residual RS fractions (0.5 per serviced Thread Debt token across game) → apply as whole-number RS loss.
4. **Niflhel RS passive drain** (NPC accounting): −0.5 per Niflhel-operated territory (Network Depth ≥ 1) → apply as whole numbers.
5. **Thread Wound territories:** T12/T13 occupied ≥ 2 consecutive seasons by any faction: RS −1 per additional season (Warden Cooperation ≥ 1 reduces this: RS −0.5 instead).
6. **Doctrinal Reach accumulation:** If Church has met the Doctrinal Reach milestone, apply accumulated +0.5 TC/season to TC now (as whole number).
7. **Stability Recovery:** Each faction that did not engage in military action this year AND has no active Heresy Investigation: Stability +1.
8. **Pledge accounting:** Any Open Pledges not honored: automatically exposed. Betrayed faction: Standing +2 vs betrayer.
9. **Milestone Bonuses:** Confirm all milestone triggers. Apply any that fired this year.
10. **AER adjustment:** Apply all end-of-year AER changes.
11. **Löwenritter check (if post-coup active):** Is Martial Law still in effect? If PI = 0 and Military Consolidation is not yet eligible: Löwenritter Mandate −1 (governing without any constitutional legitimacy is unsustainable).
12. **Season Objective reveal** (at seasons 4, 8, 12): flip face-down Season Objective token; apply scoring bonus this season.

---

## B12 — VICTORY, DEED TOKENS, HOLLOW VICTORY

### Deed Tokens

Deed Tokens are placed when their condition is first met; removed immediately if the condition breaks. Victory requires all Deed Tokens held simultaneously at Seasonal Accounting.

### Hollow Victory Scoring

**Legitimacy Modifiers (reduce effective Deed count at game end):**
- Each 2 Standing tokens held against you from other factions: −1 Deed.
- Institutional Mandate publicly Compromised ≥ 3 times: −1 Deed.
- RS below 20 at game end: all victories hollow regardless of Deed count.
- TC above 80 at game end: Church victory hollow unless Himmelenger + Valorsplatz controlled.
- Any faction eliminated (Stability 0) by you: your victory −1 Deed.

**Legitimacy Bonuses:**
- Institutional Mandate upheld ≥ 5 times: +1 Deed.
- RS above 60 at game end: all victories +1 Deed.
- Zero Standing tokens held against you at game end: +1 Deed.

**Note:** No fractional Deeds. All modifiers are whole numbers. Standing modifier: −1 Deed per 2 Standing tokens held against you (not per token).

---

## B13 — NPC AI BLOCKS

### Löwenritter (Pre-Coup, Partial Sheet)

**Priority order (peacetime):**
1. Units in Arnesheld threatened: March to defend.
2. TC > 50 and Church Mandate > Crown Mandate in any territory: issue Martial Law.
3. Crown orders this season threaten Valorian sovereignty: declare opposition (spend Tribune card).
4. *(Default — quiet seasons):* Govern in Arnesheld (Consul card, Inward) to accumulate Stability.

**Coup Counter (0–4):** Advances +1 when any coup trigger condition occurs:
1. Crown deposed.
2. Foreign power controls Crown.
3. TC ≥ 80 AND Church controls Crown-held territories.
4. Crown formally subordinates to foreign power.

At Coup Counter 4: Ehrenwall waits one season. If condition persists: Coup fires. Roll Military vs Ob 3. Success: Löwenritter gains post-coup full sheet (see B5). All factions receive Standing +1 vs Löwenritter. PI −3 immediately. If Coup fails (rare): Coup Counter resets to 2; Ehrenwall is politically weakened but remains.

### Riskbreakers (Always NPC, Always Covert)

3 tokens/year. Refresh at Year-End. Priority tree evaluated at Accounting in strict order:

| Priority | Condition | Intervention |
|----------|-----------|-------------|
| 1 | Vaynard has active manufactured Casus Belli | Expose fabrication. CB fails next season. Varfell +1 Standing from all. VTM −1. |
| 2 | Civil War active AND triggered by Vaynard CB | De-escalate: one faction's Military next season +2 Ob in most contested territory. PI +1. |
| 3 | Church seized Crown-controlled territory AND TC > 60 | Sabotage governance: territory Prosperity −1; Church Govern there +1 Ob next season. |
| 4 | Löwenritter Coup Counter = 3 AND Condition 4 approaching | Intercept: diplomatic action that would trigger Condition 4 fails. No faction absorbs Standing. |
| 5 | Any faction's Military targets civilian community with Restoration Presence | Intervene: Military +1 Ob; if fails, Restoration gains Presence in adjacent territory. |
| 6 (default) | None above | Observe. Crown player receives 1 revealed intelligence: hidden stat of faction acting most against Valoria's interests. |

**Riskbreakers vs Crown (Dominion path):** If Almud Mandate ≥ 6 AND Emergency Powers issued ≥ 2 times: Priority 2 may fire against Crown's own military orders. The peace-keepers protect Valoria from its own king.
**Riskbreaker File vs Vaynard:** Each prior Vaynard CB that Riskbreakers exposed: next exposure costs −1 token. Each failed exposure at VTM 4+: exposure Ob +1.

### Ministry (NPC, Crown Administrative Apparatus)

The Ministry is the Crown's Byzantine bureaucratic apparatus. It is nominally loyal to the Crown but has become semi-autonomous through institutional inertia. It does not pursue political goals. It processes paperwork.

**Ministry AI (evaluated at Accounting):**

1. **Policy Delay:** Each season Crown issues a Policy, roll d3: (1) Policy fires immediately; (2) Policy delayed 1 season; (3) Policy delayed 2 seasons. Löwenritter Milestone "Iron Administration" negates this delay permanently.
2. **Regulatory Friction:** At PI < 5, Ministry begins applying autonomous regulations. One non-Crown faction per season receives +1 Ob to one Govern order (bureaucratic compliance required). Ministry selects the faction with the highest Prosperity territory.
3. **Bureaucratic Capture:** At PI ≤ 2, Ministry has filled the governance vacuum. Crown cannot issue Policy this season (Ministry has suspended the apparatus). Löwenritter issuing Emergency Powers to override this: Ministry SD triggers; Löwenritter Mandate −1.
4. **Coup Resistance:** If Löwenritter stage a coup, Ministry immediately begins passive resistance. All Löwenritter Govern orders: +1 Ob for the first 3 seasons post-coup (records are unhelpful, appointments are vacant). Neutralized by Löwenritter Iron Administration milestone.

### Guilds (NPC, Economic Environment)

Guilds manage economic life in T8 (Eidursjo) and T11 (Halvardshelm). They are not a faction — they are a pressure.

**Guild AI (evaluated at Accounting):**
1. At Trade < 3 successful orders this season across all factions: Guild Disruption fires. All Trade orders next season: +1 Ob (merchants are nervous).
2. At Wealth > 8 (Guild economic prosperity): Guild Dividend — one random non-Church, non-Niflhel faction receives 1 Wealth (economic spillover).
3. At TC > 60: Guilds become secular. −1 Ob to any non-Church Trade order (Guilds prefer trading with secular powers).
4. At Löwenritter coup: Guild Neutrality — Guilds trade with whoever controls territories, no loyalty. Martial Law applies to their territories normally.
5. Hired Blades: if any faction has ≥ 2 Wealth and Military orders in T8 or T11 this season, Guilds field 1 Hired Blade unit (offensive only, 1-season duration) as a protective response. This unit serves the Guilds, not the faction.

### Niflhel (NPC, Corruption Layer)

Niflhel maintains Network Depth per territory (0–3) as a covert operational presence. It is not pursuing political victory. It is extracting value.

**Niflhel AI (evaluated at Accounting):**
1. **Network Expansion:** If Niflhel has Network Depth < 3 in T10 (Sigurdshelm): expand depth by 1. In other territories: expand into the territory with the highest Prosperity that has Network Depth 0, if any faction's Intel actions did not target that territory this season.
2. **Passive RS Drain:** Each territory with Network Depth ≥ 1: RS −0.5 at Year-End (Niflhel's supply chain creates trace Thread disturbance, including through T12/T13 routes).
3. **Opportunistic Extraction:** If any faction's Stability drops below 3 this season: Niflhel executes one covert action against that faction (Tribune Outward, Ob 2) at Network Depth ≥ 1 in their territory. Success: faction loses 1 Wealth. Failure: Network Depth in that territory −1 (detected).
4. **Church-Niflhel Connection (Olafsson vulnerability):** If a faction successfully exposes the Cardinal Olafsson / Niflhel connection (Intel vs Ob 4), the Church loses Inquisitor capability for 1 season, Church Stability −1, TC −2. Niflhel's Network Depth in T3 (Himmelenger) immediately drops to 0 (cover blown).
5. **Southernmost Supply Route:** Niflhel maintains a covert supply chain through T12/T13. This creates the Thread disturbance Edeyja has noticed. If Warden Cooperation ≥ 1, Edeyja's AI Priority 2 fires to investigate. If Niflhel is exposed via this route: Network Depth in T13 → 0; Niflhel Stability −1; Warden Cooperation advances by 1 (the disturbance is resolved).

**RS Passive Cost at Year-End:** −0.5 per Niflhel-operated territory, applied as whole numbers.

### Schoenland (NPC, Active Spoiler)

**Schoenland AI (evaluated at Accounting):**
- IP 30+: fund proxy at T4 (Spartfell) → +1D any faction's Military orders there next season.
- TC 50+: provide intelligence to anti-Church factions (Schoenland profits from secular trade).
- RS < 40: do nothing. Schoenland does not understand Thread substrate and will not operate near it.
- No active faction conflict this season → IP +1 (funding border provocations to maintain arms market).
- AER ≥ 3: actively hostile to Baralta's Reformed movement. Schoenland funds counter-messaging in Hafenmark territories: RDT gaining conditions at +1 Ob next season.

### Restoration Movement (when NPC)

**Priority order:**
1. Spread Presence to any territory with RS < 40 (urgent community organizing).
2. Advance highest-progress Community Project.
3. Move Presence to territory with active Heresy Investigation (supporting the investigated).
4. Start new Community Weave in T14 (Einhir Heartland) as first priority among new projects.
5. Community Organizing in any contested territory.

### Edeyja / The Wardens (NPC — conditional on Warden Emergence)

**Inactive until Warden Emergence fires** (see B7 — Warden Cooperation Track). Before Emergence: Edeyja does not exist on the board. The Southernmost rule (military dissolution in T12/T13) applies regardless.

**After Warden Emergence, Edeyja's AI (evaluated at Accounting, in order):**

1. **Contain:** If a monstrous entity is present in T12 or T13 this season (triggered by RS threshold breach or expedition failure): Warden containment active. RS drain from that entity is halted for 1 season. No other intervention this season.

2. **Investigate:** If Niflhel Network Depth ≥ 1 is detected in T13 (trigger: Niflhel AI Priority 5 OR a faction's Intel success in T13): Warden investigation fires. Niflhel Covert actions in T13 at +2 Ob next season. Church Attention Pool +1 (the wardens' response creates visible Thread disturbance that reads as unexplained activity). If the disturbance is resolved (Niflhel depth drops to 0 in T13), Warden Cooperation may advance at next opportunity.

3. **Work alongside:** If Warden Cooperation ≥ 1 AND an expedition faction is present in T13 with no military units: apply Cooperation benefits (RS reduction; Expedition Ob reduction per Cooperation level).

4. **Emergency Mend:** If RS < 30: Edeyja's wardens perform emergency Mending. RS +1 this season (warden active intervention at reduced RS state activates emergency protocol). This fires regardless of other conditions.

5. **Maintain:** No active threats. Warden Token remains. No visible board effect. The wardens are holding. They are always holding.

**Edeyja and Vaynard:** If Vaynard's VTM reaches 4 and he reaches T13, Edeyja's AI grants him a unique interaction regardless of current Warden Cooperation level: she will speak to him. This is the first time in her life she has spoken to someone who understands what she is managing. Warden Cooperation advances +1 from this interaction automatically (overrides other conditions). Trigger: Varfell plays Tribune (Intel) Inward in T13 at VTM 4+.

**What Edeyja will not do:**
- Leave the Southernmost.
- Engage in any political conflict between peninsula factions.
- Provide information freely. She responds to demonstrated competence.
- Ask for help. It will be visible in how she responds when the work goes well.

**Edeyja's physical representation:** She has no unit token, no Champion token. The Warden Token on the Cooperation track is her faction's entire board presence. She is felt more than seen — through expedition difficulty changes, RS interventions, and the Cooperation track advancing or retreating.

---

## B14 — HYBRID INTERFACE

### Zoom-In Triggers

| BG Event | Scene Type |
|----------|-----------:|
| Co-Movement card draws resonance event in PC's home territory | Personal Thread encounter |
| Heresy Investigation opened against PC or PC-adjacent NPC | Personal/Social scene |
| Battle in territory where PC has stated presence | Combat scene |
| RS drops below 40 (first time) | Thread Awareness scene (all practitioners mandatory) |
| IP crosses 30 AND Torben is PC or PC-adjacent | Personal Decision scene |
| Löwenritter Coup Counter = 4 | Political Crisis scene |
| Named NPC's Conviction challenged by BG order outcome | Social scene |
| Any faction reaches Hollow Victory state | Belief Crisis scene |
| Riskbreakers intercept a Vaynard CB | Hidden conflict scene |
| Reformed Settlement declared (RDT 5) | Theological Crisis scene |
| Warden Emergence fires | Southernmost Encounter scene (expedition faction PC mandatory) |
| Warden Cooperation reaches 3 | Campaign-altering knowledge scene (Calamity mechanism revealed) |

### Cascade Phase Card Effects

| Personal Scene Outcome | BG Cascade Effect |
|-----------------------|-------------------|
| PC achieves Belief this season | Add one free Senate card to faction hand (no Wealth cost) |
| PC's Belief challenged but engaged | Recess cost → 0 Wealth this season |
| PC executes successful Thread operation | Faction's Pontifex card available even if on Cooldown |
| PC fails Thread operation catastrophically | Pontifex goes on Cooldown Track (2-season cooldown) |
| PC Wounded in personal combat | Champion enters Wounded state on BG board |
| PC dies or is captured | Champion token removed; faction loses Champion bonuses 3 seasons |
| PC negotiates major alliance | Add 1 Diplomat card to faction hand this season (temporary) |
| PC uncovers evidence against another faction | That faction's one hidden stat revealed to PC's faction |
| PC passes Forgetting Check in Southernmost | Warden Emergence fires immediately (does not wait for Accounting) |

### Warden Working Libraries (Hybrid only)

On Overwhelming Forgetting Check success, the GM may reveal one fact from the following list (each fact revealed once per campaign; cross off when used):

1. The Calamity was not caused by something attacking the world. The Einhir drew their substrate too tight. It tore from the inside.
2. What came through the tear is not evil. It is fullness that the rendering cannot hold. The monstrosities are being, in excess.
3. The Forgetting is not a cultural catastrophe. It is a rendering failure. The threads that constitute memory of the Calamity were themselves damaged.
4. The wardens have been here since the day after. They are fewer each generation. Edeyja does not know how many seasons remain before the work exceeds their capacity.
5. The Locked Zones are not ruins. They are places where being has failed. New threads cannot spool through regions where the substrate has been ruptured.
6. There is a working methodology from before the Calamity. Edeyja holds it. No one else does.

---

# PART C — SYSTEM REVIEW (v0.2 update)

## C1 — Changes from Skeleton Audit

**Cognitive Load:** Improved from 7/10. Research Track removal eliminates 12 tracking positions and one Accounting step. Thread Resonance simplification removes a per-faction 0–5 track that reset every season. Estimated at 8/10 with reference cards in hand; 6/10 without.

**Coherency:** Improved from 8/10. Edeyja's integration connects the metaphysical foundation to a living NPC face. The Warden Cooperation track makes the Southernmost a relationship, not just a territory. Guilds, Ministry, and Niflhel repositioned to NPC-only correctly — their presence as player factions was incoherent given the core feel. 8.5/10.

**Legibility:** Improved from 6/10. AER now has a physical board track. Warden Cooperation track is on the board near T13. Still requires Thread Operation Procedure reference card. 7/10 — component design is the remaining gap.

**Mechanical Crunch Cascade:** Unchanged from skeleton except cascade depth cap is now a stated provisional working rule (no longer a flagged editorial item). 7/10. Still requires reference cards to reach 9/10.

**Emergent Possibility:** Improved from 9/10. Edeyja adds new chains: Niflhel supply chain disturbs Warden Cooperation before any player knows Edeyja exists; Vaynard reaching VTM 4 triggers a unique conversation that advances Cooperation by 1 automatically; Löwenritter post-coup restructures all coalition dynamics. 9.5/10.

**Precedent Alignment:** Unchanged from skeleton. 8/10. Edeyja / Warden dynamic parallels the Silent Ones in Pax Pamir (third-party actor whose neutralisation changes the board dramatically).

**Functionality:** Improved from 7/10. Three functional gaps from the skeleton are resolved: Senate Market purchase timing (Phase 2 + Phase 4); Community Organizing mechanic defined; Löwenritter default peacetime action added. Ministry AI block closes the last named faction with zero mechanical presence. 8.5/10.

**Core Feel:** Confirmed. 10/10 design intent alignment. Every playable faction's victory path creates RS risk. The wardens are losing ground slowly. The Church is winning by doing exactly what it believes is right. Vaynard is the most dangerous person on the peninsula and no one can prove it. Baralta is reforming the theological foundation of the state while the state is tearing apart. The Löwenritter are trying to protect something they've already broken by protecting it. This is what the game is.

## C2 — Pre-Playtest Checklist (updated from v0.1)

**Resolved (no longer blocking):**
- ✅ Senate Market purchase timing
- ✅ Community Organizing mechanic defined
- ✅ Löwenritter default NPC peacetime action
- ✅ Thread Resonance simplified
- ✅ AER physical board representation
- ✅ Ministry NPC AI block
- ✅ Guilds/Niflhel/Schoenland correctly positioned as NPC-only
- ✅ Cascade depth cap stated as provisional working rule
- ✅ Research Tracks removed; Milestone Bonuses integrated
- ✅ Löwenritter post-coup full faction sheet
- ✅ Edeyja / Warden Emergence trigger and AI
- ✅ T12/T13 Southernmost military dissolution as board rule

**Still blocking (editorial approval required before first playtest):**
- [ ] BG-E-51: Baralta's Conviction
- [ ] BG-E-53: Vaynard's Conviction
- [ ] BG-E-59: Almud's Conviction
- [ ] BG-E-63: VTM 5 / P-14 compliance ruling (co-movement direction)
- [ ] BG-E-64: Crown 5 Deed Token enumeration — current version carries forward skeleton's enumeration; confirm
- [ ] BG-E-65: Cascade depth cap confirmation (currently stated as provisional working rule)
- [ ] BG-E-66: Policy resolution order (currently stated as provisional working rule)
- [ ] MP-34: Institutional Mandate trigger conditions per faction (skeleton shows implied triggers; formal authored text required)

**Can wait until after first playtest:**
- [ ] BG-E-60: TD visibility
- [ ] BG-E-61: AER starting value (2)
- [ ] BG-E-62: Reformed Settlement response options
- [ ] BG-E-50: Cardinal schism mechanics
- [ ] BG-E-27/33: Champion Renown ability text
- [ ] All Advanced Rules content
- [ ] Co-Movement deck expansion for new Thread mechanics
- [ ] Southernmost Working Libraries (6 facts above are placeholders)
- [ ] Forgetting Check stat derivation in BG mode (hybrid-only currently)

---

*Ruleset v0.2 complete.*
*19 core systems. Research Tracks removed. Löwenritter post-coup integrated. Guilds/Ministry/Niflhel/Schoenland repositioned as NPC-only. Edeyja / Wardens integrated with conditional emergence and Warden Cooperation track. Thread Resonance simplified. All faction cards for playable factions only. GitHub commit required: jordanelias/ttrpg, branch main.*
