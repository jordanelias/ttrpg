<!-- DEPRECATED -->
> **DEPRECATED — 2026-04-11**
> Phase 1 design briefs (Batch E). Absorbed into params files. Superseded.
> Do not use as a canonical source.

---

# Phase 1 — Batch E: Board Game Design
## Date: 2026-03-25 (Session 5)
## Status: Design briefs
## Covers: G-025, G-026, G-027 (resolved S3), G-028, G-029, G-030, G-031, G-049, G-050, G-051, G-057, G-058 (resolved S3), G-059, G-060

---

# DESIGN PRINCIPLES

1. **The board game is a standalone game.** It must be playable without the TTRPG rulebook. It must be learnable in one session.
2. **Faction asymmetry is the core experience.** Each faction plays differently — different Order Sets, different victory conditions, different strengths. (Root model, not Risk model.)
3. **The board game uses the same 6 faction attributes as the TTRPG** (1-7 scale). Faction sheets are shared across modes.
4. **Three clocks drive the campaign arc:** Thread Tension, Theocracy Counter, Institutional Pressure. These advance automatically and through player action. The game ends when a victory condition or a shared loss condition fires.
5. **Simultaneous order placement** with sequential resolution. (ASOIAF/Dune model.)
6. **2-5 players + solo mode.** Uncontrolled factions run on Non-Player Character artificial intelligence.
7. **8 factions.** Crown, Church, Hafenmark, Varfell, Guilds, Niflhel, Revolution, Lowenritter. Partial-sheet factions (Revolution, Niflhel, Lowenritter) have fewer available orders but unique capabilities.
8. **Session length target:** 2-4 hours for a full campaign arc (10 seasons). Individual seasons: ~15-20 minutes.

---

# CLUSTER 1: TURN STRUCTURE + ORDERS

## G-026: Turn Structure (Complete Round Procedure)

Each game round = 1 season. A full campaign = 10 seasons (2.5 years of game time).

### Season Structure

**Phase 1 — Planning (simultaneous, ~5 min)**
All players simultaneously select and place orders face-down on territories. See G-059.

**Phase 2 — Negotiation (open, ~3 min)**
Players may negotiate deals, alliances, and threats. Formal deals use the Negotiation mechanic (G-049). Informal deals are non-binding (players may lie). Orders remain face-down — players may claim anything about their orders.

**Phase 3 — Reveal**
All orders flipped simultaneously. Players see the board state.

**Phase 4 — Resolution (sequential, ~5-8 min)**
Orders resolve in priority order. See G-060.

**Phase 5 — Accounting (~2-3 min)**
1. Apply all pending attribute changes from resolved orders.
2. Faction Stability checks for any faction that suffered attribute loss this season.
3. Clock advances: Thread Tension baseline drift (+1 at Winter only). Theocracy Counter advances per Church activity. Institutional Pressure advances per Altonian pressure table.
4. Check threshold events (Thread Tension/Theocracy Counter/Institutional Pressure threshold tables from existing rules).
5. Draw Event Card if applicable (see G-050).
6. Co-Movement resolution: any faction that performed a Thread operation or crossed a Thread Tension threshold draws a Co-Movement Card.
7. Check victory conditions.
8. Season marker advances. If Winter: year-end accounting (Thread Tension drift, annual events).
9. If season 10: final scoring.

---

## G-025: Order Set (Menu of Available Actions)

Each faction has a base set of available orders. Full-sheet factions get 3 orders per season. Partial-sheet factions get 2.

Orders are placed on territories. Each territory can receive at most 1 order from each faction per season (you cannot stack two of your own orders on the same territory).

### Universal Orders (available to all factions)

| Order | Roll | Effect on Success | Effect on Failure |
|-------|------|-------------------|-------------------|
| **Govern** | Mandate vs Ob 2 | +1 Stability in that territory's controlling faction. If you control: +1 Prosperity to territory. | No effect. |
| **Influence** | Influence vs Ob 2 | +1 Mandate in that territory OR -1 Mandate to one rival present in territory. | -1 Influence for 1 season (overreach). |
| **Trade** | Wealth vs Ob 2 | +1 Wealth (if trade route open to target territory). | No effect. Wealth tied up. |
| **Muster** | Military vs Ob = territory condition (1-4) | Raise 1 unit in territory. See unit table. | Territory Prosperity -1. |
| **March** | No roll | Move up to 2 units to adjacent territory. If enemy units present: triggers Battle. | N/A (automatic). |
| **Spy** | Intelligence vs Ob 3 | Reveal one hidden attribute of one faction in that territory. | Your Intelligence revealed to target for 1 season. |
| **Fortify** | Military vs Ob 2 | Territory gains +1 Fortification (max 3). Defenders +1D in battles here. | No effect. |

### Restricted Orders (require specific conditions)

| Order | Requirement | Roll | Effect |
|-------|-------------|------|--------|
| **Siege** | Your units adjacent to fortified enemy territory | Military vs Fortification level | Success: Fortification -1. Overwhelming: Fortification -1 AND battle initiated. Failure: besieging units -1 Cohesion. |
| **Treaty** | Negotiation phase deal made | Both parties Influence vs Ob 2 | Formal alliance: +1D to all orders in shared territories for 2 seasons. Betrayal triggers Grievance Marker per existing rules. |
| **Excommunicate** | Church only, Mandate >= 4 | Church Mandate vs target Mandate | Per Church Unique Action. |
| **Royal Decree** | Crown only, 1/season | Mandate vs Ob 2 | Per Crown Unique Action. |
| **Martial Law** | Lowenritter only, military presence | Military vs Ob 3 | Per Lowenritter Unique Action. |

### Faction-Specific Order Replacements

Each faction's Unique Action replaces one Universal Order in their Order Set. They still get 3 (or 2) orders — but one slot is their unique.

| Faction | Unique Action Replaces | Notes |
|---------|----------------------|-------|
| Crown | Royal Decree replaces 1 Govern | Crown gets 2 universals + Decree |
| Church | Excommunicate replaces 1 Spy | Church gets 2 universals + Excommunicate |
| Hafenmark | Sovereign Authority replaces 1 Influence | Hafenmark gets 2 universals + Sovereign Authority |
| Varfell | Private Collection replaces 1 Spy | Varfell gets 2 universals + Private Collection |
| Guilds | Economic Leverage replaces 1 Trade | Guilds gets 2 universals + Economic Leverage |
| Niflhel | Quiet Network replaces 1 Spy | Niflhel gets 1 universal + Quiet Network (2 orders total) |
| Revolution | Community Weaving replaces 1 Influence | Revolution gets 1 universal + Community Weaving (2 orders total) |
| Lowenritter | Martial Law replaces 1 March | Lowenritter gets 1 universal + Martial Law (2 orders total, peacetime) |

**Post-coup Lowenritter:** Gains full sheet = 3 orders. Martial Law + 2 universals.

---

## G-059: Simultaneous Order Placement Procedure

1. Each player takes their faction's order tokens (physical tokens, face-down).
2. Players simultaneously place tokens on the board, one at a time in clockwise rotation (prevents last-mover advantage). Each placement is face-down.
3. A player may place orders only on territories where they have presence (units, control, or adjacency for March/Siege).
4. Spy and Influence orders can be placed on any territory (long-range operations).
5. Once all orders are placed, no changes. Proceed to Negotiation phase.
6. **Bluffing:** Players may place dummy tokens (each faction gets 1 dummy token per game). Dummies are revealed as blanks during resolution — no effect, but they obscure your real plan.

---

## G-060: Resolution Phase Ordering

Orders resolve in this priority:

| Priority | Order Type | Rationale |
|----------|-----------|-----------|
| 1 | Spy | Intelligence gathered before action taken. |
| 2 | Excommunicate / Royal Decree / Sovereign Authority | Political acts set the context for military/economic action. |
| 3 | Influence | Political maneuvering before physical action. |
| 4 | Trade / Economic Leverage | Economic actions before military. |
| 5 | Muster | Troops raised before movement. |
| 6 | Fortify | Defenses built before attack. |
| 7 | March (no battle) | Movement without contact. |
| 8 | March (triggers battle) | Combat resolution. Uses disposition table. |
| 9 | Siege | Siege resolution after open-field battle. |
| 10 | Govern | Administrative action after dust settles. |
| 11 | Treaty | Formalized after the season's events are known. |
| 12 | Unique Actions (Thread-related) | Thread operations resolve last — their co-movement effects apply at accounting. |

**Ties within priority:** Resolve in Influence order (highest Influence first). Equal Influence: roll off.

---

# CLUSTER 2: MAP

## G-029: Territory Differentiation (15 Territories)

15 territories arranged in a roughly north-south layout with adjacency connections (not hexes — territory-adjacency graph).

Each territory has:
- **Name**
- **Starting controller** (which faction controls it at game start)
- **Prosperity** (1-7, affects mustering Ob and economic output)
- **Fortification** (0-3, defense bonus)
- **Special property** (unique mechanical effect)
- **Adjacencies** (which territories connect)

### Territory Map

| # | Territory | Start Control | Prosperity | Fort | Special Property | Adjacent To |
|---|-----------|--------------|------------|------|-----------------|-------------|
| 1 | Valorsplatz (Capital) | Crown | 6 | 2 | Royal Court: Crown Decree -1 Ob here. Parliament: Hafenmark Influence -1 Ob here. | 2, 3, 5, 6 |
| 2 | Kronmark (Crown heartland) | Crown | 5 | 1 | Garrison: +1 Muster die here. | 1, 3, 4 |
| 3 | Himmelstift (Cathedral city) | Church | 5 | 2 | Grand Cathedral: Theocracy Counter +1 per season Church controls this. Church Excommunicate -1 Ob here. | 1, 2, 6, 7 |
| 4 | Border Pass | Crown | 3 | 2 | Altonian Border: Institutional Pressure threshold events trigger here first. Invasion entry point. | 2, 5, 15 |
| 5 | Ehrenfeld (Military heartland) | Crown (Lowenritter garrison) | 4 | 3 | Lowenritter Fortress: Lowenritter Martial Law -1 Ob here. +1 Fortification max (4 here). | 1, 4, 9 |
| 6 | Hafenstadt (Hafenmark capital) | Hafenmark | 6 | 1 | Ducal Court: Hafenmark Sovereign Authority can be invoked here. Major port. | 1, 3, 7, 8 |
| 7 | Sternhaven (Northern port) | Hafenmark | 5 | 0 | Trade Hub: all Trade orders +1D here. Schoenland route terminus. | 3, 6, 8 |
| 8 | Grauwald (Forest region) | Guilds | 4 | 0 | Timber/Mining: Guilds Trade +1D here. Difficult terrain: March costs 2 movement (not 1). | 6, 7, 10, 11 |
| 9 | Eisengrund (Southern highlands) | Varfell | 4 | 1 | Varfell Seat: Private Collection usable here only. Einhir ruins: Revolution Community Weaving -1 Ob. | 5, 10, 12, 13 |
| 10 | Schwarzmarkt (Underground trade) | Niflhel | 3 | 0 | Black Market: Niflhel Quiet Network -1 Ob here. All factions can Trade here at +1 Ob (illicit goods). | 8, 9, 11 |
| 11 | Feldmark (Farming plains) | Guilds | 5 | 0 | Breadbasket: +1 Prosperity recovery per season (if not contested). Muster Ob -1 (willing recruits). | 8, 10, 14 |
| 12 | Sudwald (Southern forest) | Uncontrolled | 3 | 0 | Thread Wound: Thread Tension threshold events hit here at -10 Thread Tension (earlier than elsewhere). Revolution presence (not control). | 9, 13, 14 |
| 13 | Askeheim (Southernmost border) | Uncontrolled | 2 | 0 | Southernmost Access: required for Southernmost Expedition. Thread proximity: all non-Thread orders +1 Ob. Thread Sensitivity 30+ characters: automatic Discovery Event per season here. | 9, 12 |
| 14 | Korntal (Southern farmland) | Revolution (informal) | 4 | 0 | Einhir Heartland: Revolution Influence -1 Ob here. Restoration Movement stronghold. Church Influence +1 Ob here (cultural resistance). | 11, 12 |
| 15 | Schoenland (Altonian trade port) | Neutral (Altonian trade) | 5 | 1 | Altonian Trade: generates +1 Wealth for any faction with Trade order here (while trade route open). Altonian spies: Intelligence orders here reveal results to Altonia. At Institutional Pressure 75+: Altonian vanguard deploys here. | 4, 7 |

### Territory Control
- A faction controls a territory if it has the only military units present OR won the most recent battle there.
- Uncontrolled territories: no faction benefits from control bonuses. First faction to station units claims control.
- Contested: multiple factions have units. No one gets control bonuses until resolved.

### Adjacency Notes
- Schoenland connects to Border Pass (land route) and Sternhaven (sea route). Sea route severed if Schoenland trade suspended.
- Askeheim is a dead end — only connects to Sudwald and Eisengrund. Expedition territory, not strategic.
- Valorsplatz is the most connected territory (4 adjacencies) — the political hub.

---

# CLUSTER 3: VICTORY

## G-028: Victory Conditions Per Faction

### Shared Loss Condition (all players lose)
**Thread Tension reaches 100.** The Rupture occurs. Rendered reality fails. No faction survives in recognizable form. This is the cooperative pressure underlying the competitive game — all players must manage Thread Tension even while competing.

### Per-Faction Victory Conditions

Each faction has a **primary** victory condition (wins the game outright) and a **secondary** (wins on points if no outright winner by season 10).

| Faction | Primary Victory | Secondary (Points) |
|---------|----------------|-------------------|
| **Crown** | Control Valorsplatz + 4 other territories at end of any season. Mandate >= 5. | 1 pt per controlled territory + 1 pt per Mandate above 3 + 2 pts if heir secure (Torben Loyalty >= 5). |
| **Church** | Theocracy Counter reaches 80. Church controls Himmelstift + Valorsplatz. | 1 pt per 10 Theocracy Counter + 1 pt per territory where Church Mandate > Crown Mandate + 2 pts if Excommunication active. |
| **Hafenmark** | Parliamentary Supremacy: Hafenmark Mandate + Influence both >= 6. Crown Mandate <= 3. | 1 pt per Influence above 3 + 1 pt per Wealth above 3 + 2 pts if Sovereign Authority successfully invoked. |
| **Varfell** | Possess 3+ Thread-locked artifacts (via Private Collection or expedition). Thread Sensitivity of any affiliated character >= 50. | 1 pt per artifact + 1 pt per Intelligence above 3 + 2 pts if Einhir Research completed. |
| **Guilds** | Wealth >= 7 AND Economic Leverage active in 3+ territories simultaneously. | 1 pt per Wealth above 3 + 1 pt per territory with Guild Favour 5+ + 2 pts if trade routes all open. |
| **Niflhel** | Control (covertly) 3+ territories' Intelligence networks (Intelligence >= 5 in 3 territories via Quiet Network). No faction knows Niflhel's true Stability. | 1 pt per Intelligence above 3 + 1 pt per successful assassination + 1 pt per covert territory control. |
| **Revolution** | Thread Tension reduced to <= 20 via Community Weaving. Revolution Influence >= 5. Einhir cultural practices publicly restored. | 1 pt per Influence above 2 + 1 pt per 10 Thread Tension reduced below starting value + 2 pts if Restoration publicly active. |
| **Lowenritter** | Successful military coup + control of Valorsplatz + Border Pass + Ehrenfeld. All foreign influence expelled (Institutional Pressure <= 20, no Altonian units on map). | 1 pt per Military above 3 + 1 pt per controlled territory + 2 pts if coup triggered + 2 pts if Altonia repelled. |

### Victory Timing
- Primary victory checked at end of each season (Phase 5, step 7).
- If multiple factions achieve primary victory simultaneously: the faction with higher total points wins.
- If no primary victory by season 10: highest point total wins. Ties broken by Stability (most stable faction endures).

### Design Notes
- Crown's victory is the "default" — maintain the status quo. It's the hardest to disrupt but the easiest to erode.
- Church's victory is clock-driven — Theocracy Counter advances naturally. Other factions must actively suppress it.
- Revolution's victory is cooperative with the shared survival goal — reducing Thread Tension helps everyone. But it requires the Revolution to become publicly powerful, which other factions resist.
- Lowenritter's victory is conditional — they can't even attempt it without a coup trigger. They're a latent threat that activates under crisis.
- Niflhel's victory is information-based — they win by knowing everything while being known by no one.

---

# CLUSTER 4: SYSTEMS

## G-050: Event Deck / World Event System

### Event Card Types

**Clock Events (triggered automatically):**
When Thread Tension, Theocracy Counter, or Institutional Pressure crosses a threshold (every 20 points), draw from the corresponding clock event table. These are pre-scripted — not random.

| Clock | Threshold | Event |
|-------|-----------|-------|
| Thread Tension 20 | Shifting Objects appear in 1d3 territories. Cosmetic but unsettling. |
| Thread Tension 40 | Southernmost expedition becomes possible. Thread Wounds visible in Sudwald/Askeheim. |
| Thread Tension 60 | Gaps appear. One random territory: all orders +1 Ob this season (reality unstable). Practitioners gain +1D to Thread ops. |
| Thread Tension 80 | Monstrous entities emerge in Sudwald and Askeheim. Military units there: Cohesion check Ob 2 or -1 Cohesion. |
| Theocracy Counter 20 | Church begins Heresy Investigation in 1 territory (Game Master/artificial intelligence choice). |
| Theocracy Counter 40 | Templar units deploy. Church gains 1 free military unit in Himmelstift. |
| Theocracy Counter 60 | Church demands civil authority in 1 territory. Crown must Refuse (Theocracy Counter +2) or Comply (Crown Mandate -1 in that territory). |
| Theocracy Counter 80 | Church claims territories of influence. Church begins controlling territories where Church Mandate > Crown Mandate. These territories' control shifts to Church. |
| Institutional Pressure 30 | Altonian demands begin. Tutoring Demand activates (see succession mechanic). |
| Institutional Pressure 45 | Altonian proxy units appear at Border Pass. |
| Institutional Pressure 60 | Altonian army visible. Diplomatic Resolution possible. |
| Institutional Pressure 75 | Altonian vanguard at Schoenland. Trade suspended. |
| Institutional Pressure 100 | Full invasion. Altonian army enters via Border Pass + Schoenland. |

**Seasonal Events (1 per season, drawn randomly):**
A deck of 20 cards, shuffled at game start. Draw 1 per season at Accounting. These inject variety and force adaptation.

Example events (10 of 20):
1. **Plague** — one territory (lowest Prosperity): Prosperity -1, Muster Ob +2 this territory for 2 seasons.
2. **Bumper Harvest** — Feldmark and Korntal: Prosperity +1 this season.
3. **Heretic Scholar** — a practitioner surfaces publicly. Church Theocracy Counter +2. Revolution Influence +1. Random territory.
4. **Bandit Uprising** — Grauwald or Schwarzmarkt: 1 bandit unit appears (Martial 2, Cohesion 3). Attacks any faction present.
5. **Diplomatic Envoy** — Altonia sends a trade delegation. Any faction may attempt Trade with +1D in Schoenland this season.
6. **Mine Collapse** — Grauwald or Eisengrund: Prosperity -1 permanently until Govern order restores it.
7. **Einhir Festival** — Korntal: Revolution Influence +1. Church Mandate -1 in Korntal (pagan celebration offends).
8. **Assassination Attempt** — target faction leader (highest Mandate). Roll target Stability vs Ob 2. Failure: leader incapacitated 1 season (no Unique Action).
9. **Trade Dispute** — two adjacent territories: Trade orders fail in both this season unless Treaty in place.
10. **Thread Tremor** — Thread Tension +2. One random territory: all orders +1 Ob (configurational instability).

---

## G-051: Season Wheel / Seasonal Differentiation

Four seasons rotate: Spring → Summer → Autumn → Winter. Each has a modifier.

| Season | Modifier |
|--------|----------|
| **Spring** | Muster +1D (recruitment season). March into mountain/forest territories: no terrain penalty. |
| **Summer** | Trade +1D (peak commerce). Military Cohesion checks: +1D (morale high). |
| **Autumn** | Harvest: all controlled territories with Prosperity 4+: +1 Wealth to controlling faction. Siege -1D (approaching winter). |
| **Winter** | All March orders: -1D (weather). Siege: besieged faction Stability check Ob 2 (starvation pressure). Thread Tension annual drift +1. Year-end accounting. |

A full campaign = 10 seasons. Default start: Spring Year 1. Seasons 1-4 = Year 1, 5-8 = Year 2, 9-10 = first half of Year 3 (Spring + Summer).

The season wheel is a physical component (rotating dial or track on the board).

---

## G-057: Thread Operations (Simplified Faction-Card Procedure)

In the board game, Thread operations are abstracted to faction-level actions. No personal-scale Thread scenes.

### Thread Orders (available to factions with Thread capability)

**Thread-capable factions:** Varfell (via Private Collection), Revolution (via Community Weaving), any faction with an affiliated Thread Sensitivity 30+ character.

| Thread Order | Roll | Effect |
|--------------|------|--------|
| **Weave** | Intelligence (or faction-specific attribute) vs Ob = Thread Tension / 20 (round up) | Success: Thread Tension -1. Overwhelming: Thread Tension -2. Failure: Thread Tension +1. |
| **Investigate Thread** | Intelligence vs Ob 3 | Success: learn current Thread Tension value (normally hidden from players). Overwhelming: also learn which territories have Thread Wounds. |
| **Thread Harvest** (Niflhel only) | Intelligence vs Ob 2 | Success: +1 Wealth (dissolution residue trade). Thread Tension +0.5 (tracked as half-points, round up at accounting). |

All Thread operations draw a Co-Movement Card at Accounting (per P-01).

### Co-Movement Cards
Deck of 15 cards. Draw 1 whenever a Thread operation occurs or Thread Tension crosses a threshold.

Effects are unpredictable and can be positive, negative, or lateral:
1. Stability -1 (acting faction) — Thread backlash.
2. Thread Tension +1 — operation disturbed more than it healed.
3. One territory: Prosperity +1 — configurational alignment benefits the land.
4. Random faction: Intelligence -1 for 1 season — Thread noise disrupts information networks.
5. Acting faction: Influence +1 — the population senses something has changed for the better.
6. Thread Tension -1 — resonance cascade (beneficial).
7. One unit in acting faction's territory: Cohesion -1 — soldiers sense wrongness.
8. No effect — the Thread absorbs the operation without visible consequence.
9. Acting faction: Mandate -1 — the operation was subtly visible. Someone noticed.
10. Church Theocracy Counter +1 — the Church's theological sensors detect heterodoxy.
11. One practitioner Non-Player Character surfaces in a random territory — a Thread event drew them out.
12. Acting faction: +1D to next Thread operation — resonance established.
13. Two territories: swap Prosperity values — configurational drift reshapes the land.
14. Institutional Pressure -1 — Altonia's intelligence network suffers Thread interference.
15. All factions: Stability check Ob 1 — a tremor in the configurational substrate.

---

## G-049: Negotiation / Deal Mechanics

### Informal Deals
Players may make any promise during the Negotiation phase. These are non-binding. Players may lie. Broken promises have no mechanical consequence (but other players will remember).

### Formal Treaties
Require both parties to spend a Treaty order (uses one of their 3 orders for the season).

**Treaty procedure:**
1. Both parties declare terms (specific, verifiable conditions: "I will not March into your territory for 2 seasons" / "You will Trade with me in Sternhaven").
2. Both roll Influence vs Ob 2.
3. Both succeed: Treaty is binding. Place Treaty token between the two factions. Duration: 2 seasons (or as negotiated, max 4).
4. One fails: Treaty fails to formalize. The willing party gains +1 Influence (seen as trustworthy). The failing party: no penalty.
5. Both fail: negotiation collapses publicly. Both factions -1 Mandate in the territory where negotiation occurred.

**Treaty betrayal:** Per existing rules from Batch C — betrayed gets Stability -1 (2 seasons) + casus belli + Grievance Marker; betrayer gets Influence -1 (2 seasons) + Mandate +1 (1 season) + individual Reputation damage.

**Constraint:** A faction may have at most 2 active Treaties simultaneously. (Prevents alliance-lock where one player allies with everyone.)

---

# CLUSTER 5: META

## G-030: Component Specification

### Physical Components

| Component | Quantity | Purpose |
|-----------|----------|---------|
| Territory board | 1 | 15-territory adjacency map with art |
| Faction sheets | 8 | 6-attribute tracker (sliding markers) |
| Order tokens | 8 sets of 8 | 7 order types + 1 dummy per faction |
| Unit tokens | ~40 total | Military units (5 per faction) with Martial/Cohesion tracks |
| Clock tracks | 3 | Thread Tension (0-100), Theocracy Counter (0-100), Institutional Pressure (0-100) — printed on board |
| Season wheel | 1 | Rotating dial: Spring/Summer/Autumn/Winter |
| Co-Movement deck | 15 cards | Thread consequence cards |
| Event deck | 20 cards | Seasonal event cards |
| Treaty tokens | 8 | Placed between allied faction sheets |
| Grievance markers | 16 | Placed on faction sheets |
| Control markers | 15 | 1 per territory — faction color |
| Fortification markers | 15 | Stackable (0-3 per territory) |
| Prosperity markers | 15 | Sliding (1-7 per territory) |
| Dice | 10d10 | Shared pool |
| Reference cards | 8 | Per-faction: order summary, victory condition, unique action |
| Torben Loyalty track | 1 | 8-0 countdown (on Crown faction sheet or separate) |
| Rulebook | 1 | ~20 pages |
| Quick-start guide | 1 | 2-page setup + first season walkthrough |

### Faction Colors
| Faction | Color |
|---------|-------|
| Crown | Gold |
| Church | White |
| Hafenmark | Blue |
| Varfell | Purple |
| Guilds | Green |
| Niflhel | Black |
| Revolution | Red |
| Lowenritter | Silver |

---

## G-031: Non-Player Character artificial intelligence Expansion

When fewer than 8 players, uncontrolled factions run on Non-Player Character artificial intelligence. The artificial intelligence follows a simple decision tree per faction, evaluated each season.

### artificial intelligence Decision Framework

Each Non-Player Character faction has 3 priorities (ordered). The artificial intelligence selects orders to serve the highest unfulfilled priority.

| Faction | Priority 1 | Priority 2 | Priority 3 |
|---------|-----------|-----------|-----------|
| Crown | Maintain control of Valorsplatz | Defend Border Pass | Govern (increase Stability) |
| Church | Increase Theocracy Counter (place orders that advance Theocracy Counter) | Expand to new territory via Influence | Suppress heresy (Spy on Thread-active factions) |
| Hafenmark | Protect Hafenstadt + Sternhaven | Trade (increase Wealth) | Influence in Valorsplatz (political power) |
| Varfell | Use Private Collection if available | Spy (increase Intelligence advantage) | Defend Eisengrund |
| Guilds | Trade in highest-Prosperity territory | Economic Leverage against weakest rival in Guild territory | Govern (maintain Prosperity) |
| Niflhel | Quiet Network (intelligence gathering) | Trade in Schwarzmarkt | Avoid exposure (never March openly) |
| Revolution | Community Weaving (reduce Thread Tension) | Influence in Korntal/Sudwald | Avoid military confrontation |
| Lowenritter | Fortify Ehrenfeld/Border Pass | Monitor coup trigger conditions | Follow Crown orders (support Crown's highest-priority unfulfilled order) |

### artificial intelligence Order Selection Procedure
1. Check Priority 1. If the condition is unmet, select the order that best addresses it.
2. If Priority 1 is met, check Priority 2. Select accordingly.
3. If both met, Priority 3.
4. Remaining orders (if 3-order faction): default to Govern in controlled territory.
5. Non-Player Character factions never negotiate Treaties. They respond to player-initiated Treaties with a coin flip (50% accept).

### artificial intelligence Escalation
- If an Non-Player Character faction's Stability drops to 2 or below: all orders become defensive (Fortify, Govern, no offensive actions).
- If an Non-Player Character faction is attacked: it retaliates against the attacker next season (Priority 1 override).
- Church artificial intelligence: if Theocracy Counter >= 60, artificial intelligence shifts to aggressive expansion (Priority 1 becomes "claim territory where Church Mandate > Crown Mandate").
- Lowenritter artificial intelligence: if any coup trigger condition is met, artificial intelligence initiates coup next season.

---

# BATCH E SUMMARY

| Gap | Status | Editorial Needed |
|-----|--------|-----------------|
| G-025 | Designed | None |
| G-026 | Designed | None |
| G-027 | Resolved S3 | N/A |
| G-028 | Designed | Varfell victory condition may need tuning (artifact count) |
| G-029 | Designed | Territory names are placeholder-quality — may want editorial pass |
| G-030 | Designed | None |
| G-031 | Designed | None |
| G-049 | Designed | None |
| G-050 | Designed | None — event cards C-11–C-20 completed (GT-01) |
| G-051 | Designed | None |
| G-057 | Designed | None |
| G-058 | Resolved S3 | N/A |
| G-059 | Designed | None |
| G-060 | Designed | None |

**13 gaps designed. 2 previously resolved. Batch E complete pending editorial review.**

---

## Canon Compliance (Batch-level)

- **P-01 (inseparability):** Co-Movement Cards enforce Thread consequences for every Thread operation. No faction can manipulate the Thread without rendered-side feedback.
- **P-05 (three modes distinct):** Board game has its own Order Set, turn structure, and victory conditions — mechanically distinct from TTRPG Domain Actions and hybrid phase structure.
- **P-07 (Calamity = rendered-side):** All victory conditions are rendered-side (political, military, economic, informational). Thread operations produce consequences but Thread mastery alone doesn't win (except Revolution, whose victory IS Thread healing).
- **P-11 (Thread Depth universal):** Every Thread operation in board game has Thread Depth cost via Co-Movement Cards — no free Thread work.
- **P-14 (all modes express inseparability):** The shared Thread Tension loss condition forces all factions to acknowledge Thread reality even while pursuing political goals. The board game mechanically prevents pure political play from being sufficient — someone must manage Thread Tension or everyone loses.

---

# Generation Tasks: GT-01, GT-02, GT-03
## Date: 2026-03-30
## Status: Draft — requires user review before committing to canonical files

---

# GT-01: Seasonal Event Cards C-11 through C-20

Cards C-01 through C-10 established in batch_e_designs.md. These are C-11–C-20 to complete the 20-card deck.

Design constraints applied:
- Each card should be resolvable in ~1 minute
- Effects should interact with at least one of the three clocks or faction stats
- Variety: political, military, economic, Thread-related, and personal-scale cards distributed across the deck
- No card should duplicate C-01–C-10 effect types exactly

---

**C-11 — SUCCESSION RUMOUR**
*A whisper circulates that Almud's health is failing. The succession question sharpens.*
- Torben Loyalty track: −1 (Altonian interest intensifies around a potential heir).
- Crown Mandate −1 (uncertainty around Crown stability).
- Church Theocracy Counter +1 (theological interest in who controls the next monarch).
- *Trigger condition:* If Torben Loyalty is already ≤ 3 when this card fires: Institutional Pressure +2 instead (Altonia acts on the rumour).

---

**C-12 — GUILD PRICE FIXING**
*The Merchant Guilds coordinate to suppress competition in a key trade territory.*
- Guilds Wealth +1.
- One non-Guild faction with Trade orders in any Guild-controlled territory this season: those Trade orders fail automatically (prices locked out).
- If the affected faction has Military ≥ 4: they may retaliate with March next season without casus belli penalty (economic coercion = justified response).

---

**C-13 — EINHIR ARTEFACT SURFACES**
*A construction crew in [Game Master-chosen territory] uncovers a pre-Calamity Einhir object. Its nature is unclear.*
- Varfell: if they have Intelligence ≥ 4, they learn of it automatically and may claim it via a Spy order (opposed by territory controller).
- Church Theocracy Counter +1 (heretical object; suppression demanded).
- Revolution Influence +1 (cultural heritage moment; community organises around it).
- Thread Tension +1 (the object is Thread-active — its exposure disturbs the local configuration).
- *If Varfell claims it:* +1 toward Varfell Einhir Research track (if applicable). The artefact contributes to Private Collection.

---

**C-14 — CONSCRIPTION CRISIS**
*A local lord attempts to raise troops beyond his legal authority. A territorial dispute follows.*
- One territory (Game Master choice — most militarised): Muster orders by all factions +1 Ob this season (population resistant).
- Territory Prosperity −1 (conscription disrupts harvest/trade).
- Löwenritter: if they have presence in this territory, they may issue Martial Law immediately without using their order for the season (enforcing order is within their mandate).

---

**C-15 — THREAD PRACTITIONER SURFACED**
*A practitioner operating covertly is exposed — rumour, incident, or deliberate reveal.*
- Church: immediately targets the practitioner with Heresy Investigation (Ob 2, using no order slot — reflex institutional action).
- Theocracy Counter +2 if investigation succeeds. Theocracy Counter +0 if it fails (practitioner escapes or is defended).
- Revolution: may attempt to shelter the practitioner (Influence vs Church Mandate, Ob = Church Mandate ÷ 2). Success: Theocracy Counter +0, practitioner joins Revolution. Failure: practitioner captured, Theocracy Counter +2.
- Varfell: may attempt to recruit the practitioner instead (Intelligence vs Ob 3). Cannot contest Church and Varfell simultaneously — if both try, Church acts first.
- *Personal-scale trigger in hybrid:* if a Player Character is the practitioner or has a Knot with them, a mandatory TTRPG scene fires.

---

**C-16 — ALTONIAN DIPLOMATIC MISSION**
*An Altonian delegation arrives, nominally for trade. Actual agenda: assess Valorian political stability.*
- Institutional Pressure +1 (Altonian intelligence gathering advances the clock).
- Any faction that refuses to receive the delegation: Reputation −1 with all factions (perceived as hostile to peace).
- Crown may attempt formal Negotiation with the mission (Influence vs Ob 3): success = Institutional Pressure −1 (diplomatic reassurance). Failure = Institutional Pressure +1 (mission reports instability).
- Hafenmark may invoke constitutional precedent to limit the mission's access (Unique Action counts as used this season if they do so): Institutional Pressure −2 but Church Theocracy Counter +1 (Hafenmark seen as obstructing Altonian church-trade links).

---

**C-17 — FAMINE SEASON**
*Harvest shortfalls affect the southern territories.*
- Feldmark and Korntal: Prosperity −1 each.
- All factions in those territories: Military Cohesion checks Ob 1 (hungry troops).
- Revolution: Community Weaving in either territory this season generates +1D (shared suffering strengthens communal response).
- Guilds: may Trade at +1D in affected territories (emergency supplies = price gouging opportunity). This triggers a Grievance Marker from Revolution if Guilds exploits it.

---

**C-18 — JUDICIAL CONFRONTATION**
*A landmark legal case in Valorsplatz forces a public ruling on Church vs ducal authority.*
- Choose: the ruling goes to Church (Theocracy Counter +1, Crown Mandate −1, Hafenmark Influence −1) or Crown/Parliament (Theocracy Counter −1, Church Mandate −1 in Valorsplatz).
- If no faction controls Valorsplatz: Game Master determines the ruling based on current balance of Mandate scores.
- If a Player Character is involved in the case (TTRPG scene in hybrid): the Player Character's side of the argument shifts the outcome one tier regardless of Mandate scores.

---

**C-19 — LÖWENRITTER PATROL**
*A Löwenritter patrol reports something they cannot explain near the Sudwald or Askeheim border.*
- Thread Tension +1 (Thread activity near the wound sites).
- Löwenritter Intelligence: if ≥ 3, the patrol report reaches Grandmaster Ehrenwall (or successor). She files it without acting — but the Coup Counter may advance if this is the third such report (Game Master discretion).
- Varfell: if they have Intelligence ≥ 4, they intercept the report. Discovery Event: learn Thread Tension current value.
- *Narrative consequence:* the patrol soldiers are disturbed. One deserts. Military −1 in the territory where the patrol was stationed.

---

**C-20 — RESTORATION RALLY**
*The Restoration Movement holds a public gathering in an Einhir-heritage territory. It is larger than expected.*
- Revolution Influence +2 in Korntal or Sudwald (Game Master choice, whichever is more Revolution-favourable).
- Church Theocracy Counter +1 (public Einhir practice = institutional threat).
- Crown Mandate −1 in the rally territory (the crowd is implicitly challenging the post-war settlement).
- Löwenritter: if they have military presence, must choose: Disperse (Revolution Influence −1, Löwenritter Stability −1 from internal dissent) or Allow (Revolution Influence +2 stands, Löwenritter gains Grievance Marker from Crown).
- *Personal-scale trigger in hybrid:* a Player Character with any Restoration-affiliated Knot or Belief that engages this event receives +1 CP.

---

# GT-02: Co-Movement Cards CM-11 through CM-20

CM-01 through CM-15 established in batch_e_designs.md. The deck was specified as 15 cards — but GT-02 calls for CM-11 through CM-20, implying expansion to 20. Proceeding with 10 new cards (CM-11–20), expanding deck to 25 total.

[EDITORIAL: Confirm whether deck should expand to 25 or stay at 15 and replace CM-11–15 with these.]

Design constraints:
- Mix of positive, negative, and lateral consequences
- All consequences rendered-side (political, military, economic, personal) — not direct Thread changes (those are the deterministic auto-effects)
- Scale should feel proportionate but unpredictable — the point is that Thread contact produces consequences beyond intention

---

**CM-11 — MEMORY SURFACING**
*Something in the Thread interaction triggered a fragment of Einhir cultural memory in a nearby person.*
- One Non-Player Character in the territory where the operation occurred gains a partial memory of pre-Calamity Thread practice. They will seek out a practitioner within 1 season.
- *If no practitioner is accessible:* the Non-Player Character becomes a minor Restoration sympathiser. Revolution Influence +1 in that territory.
- *If a practitioner is accessible:* potential Thread Sensitivity 0 recruit (Game Master introduces as narrative hook, not guaranteed recruitment).

---

**CM-12 — INSTITUTIONAL TREMOR**
*A faction's administrative apparatus experiences a disruption — records lost, personnel unsettled, routines broken.*
- One faction (highest current Stability): Stability check Ob 1. Failure: Stability −1. Success: no effect.
- Rationale: high-Stability institutions are more brittle when the unexpected occurs — their stability is partially a function of assuming the world behaves predictably.

---

**CM-13 — BOUNDARY COLLAPSE**
*A territorial boundary becomes unclear — disputed land claims, survey errors, a fortification that appears to shift.*
- Two adjacent territories: their control markers are both removed. Control is contested until a faction sends a Govern or March order.
- Prosperity of both territories: −1 until control is re-established (uncertainty disrupts local economy).

---

**CM-14 — PRACTITIONER RESONANCE**
*The operation's Thread signature was distinctive. Another practitioner perceived it.*
- One Non-Player Character practitioner within 3 territories of the operation knows someone performed Thread work here. They do not know who. They will investigate.
- *If Edeyja or a Southernmost warden is within range (Askeheim or Sudwald):* she notes it. This is factored into her assessment of whether northern practitioners are worth engaging.
- *If the Church has an active Inquisitor:* investigation begins immediately (Heresy Investigation Ob 2 this season).

---

**CM-15 — WEALTH DISRUPTION**
*Trade flows shift around the Thread-active site. Merchants avoid the area, or flock to it.*
- Roll 1d10: 1–5 = disruption (Wealth −1 for controlling faction), 6–10 = attraction (Wealth +1 for controlling faction — curiosity tourism, unusual goods).
- Effect lasts 1 season.

---

**CM-16 — SOLDIER SUPERSTITION**
*Military units in or adjacent to the operation territory become unsettled.*
- All military units in the territory: Cohesion −1 this season.
- Löwenritter units: immune (they have seen enough to be steady, not superstitious).
- Templar units: immune (faith framework interprets the experience as divine proximity rather than wrongness).

---

**CM-17 — POLITICAL OPPORTUNISM**
*A faction immediately capitalises on the visible Thread disturbance for political advantage.*
- The faction with the highest current Mandate (not acting faction): Mandate +1 (they publicly interpret the event as validating their authority/theology/cause).
- If that faction is the Church: Theocracy Counter +1 additionally (theological claim on the event).

---

**CM-18 — TEMPORAL ECHO**
*People in the territory experience brief déjà vu, dreams of events that haven't happened, or recall events that don't match recorded history.*
- No immediate mechanical effect.
- Game Master note: this territory is Thread-active and should be treated as having elevated perceptual strangeness for the remainder of the season. Thread Sensitivity 15+ characters passing through automatically notice something is different. This is a narrative consequence, not a stat change — but it is canon that Thread work at this site has disturbed the local temporal rendering.
- One Non-Player Character in the territory gains an anomalous memory — Game Master uses this as a future scene hook.

---

**CM-19 — FACTIONAL INTELLIGENCE LEAK**
*The Thread operation's side effects were detectable in ways that revealed strategic information.*
- Acting faction: one of their hidden stats is revealed to all players (Game Master chooses which). The revelation lasts until end of next season.
- If the acting faction is Niflhel: this effect is doubled — two stats revealed. Niflhel's operations are the most Thread-disturbing and thus the most visible to those watching the right things.

---

**CM-20 — GROUND STABILITY**
*The operation worked cleanly with the substrate. The rendered world is, briefly, more coherent here.*
- Thread Tension −1 (net positive consequence of the operation interacting well with the existing configuration).
- Territory where operation occurred: all orders −1 Ob next season (clarity of configuration assists all action).
- This is the rarest co-movement outcome — the one that suggests the Einhir were right that small-scale, precise work is genuinely beneficial.

---

# GT-03: Monstrous Entity Compound Thread Operation Tables

Per R-77: entities passively perform compound Thread operations (random combination of two ops simultaneously, scale by Gap size).

## Framework

Monstrous entities are Mode 2 or Mode 3 configurations that exist in radical excess of normal rendering. Their "operations" are not intentional Thread work — they are their existence producing Thread-side effects. When an entity acts, it does so simultaneously across multiple operational axes because its very presence destabilises the rendered fabric.

**Three entity tiers** (per R-77):
- **Tier 1** (small, recent Gap): 2 compound operations, Object–Personal scale
- **Tier 2** (significant Gap, sustained presence): 2 compound operations, Personal–Relational scale
- **Tier 3** (major Gap, or Southernmost interior): 3 compound operations, Relational–Structural scale

---

## Compound Operation Combination Table

Roll 1d10 twice (or use the table to select a combination). Each result names two simultaneous operations.

| Roll | Operation A | Operation B | Combined effect |
|------|------------|------------|----------------|
| 1 | Loose (actuality axis) | Pull (temporality axis) | Entity destabilises the actuality of everything in the zone while drawing temporal weight out of beings. Targets age rapidly in perceived terms. Ob to resist = entity's Gap scale (1–3). |
| 2 | Lock (actuality axis) | Dissolve (intelligibility axis) | Entity freezes configurations while dissolving their intelligibility. Targets become physically immobile AND cease to be legible to each other — practitioners cannot Diagnose in this zone. |
| 3 | Pull (actuality axis) | Loose (intelligibility axis) | Entity draws things toward itself while loosening their intelligibility. Objects and people drift toward the entity; their Thread configurations become harder to read (+2 Ob to Diagnose). |
| 4 | Dissolve (actuality axis) | Lock (temporality axis) | Entity unmakes actuality while freezing temporal flow. Area around entity: things do not move in time — they are caught between moments. Practitioners attempting Leap in this zone: +2 Ob (temporal axis locked interferes with intentionality). |
| 5 | Loose (temporality axis) | Lock (actuality axis) | Temporal loosening + actuality freezing. Targets experience temporal distortion (past bleeding into present) while physically unable to act. Spirit check Ob = entity tier or Certainty −1. |
| 6 | Pull (intelligibility axis) | Dissolve (temporality axis) | Entity draws intelligibility out of beings (they become hard to perceive, even by themselves) while dissolving temporal depth. Targets lose 1d3 History access for the scene (cannot recall relevant experience). |
| 7 | Lock (intelligibility axis) | Loose (actuality axis) | Intelligibility locked (nothing can be known about anything near the entity — perception blocked) + actuality loosening (things stop being fully present). Effectively: the zone around the entity becomes an un-rendered bubble. Practitioners: Coherence check Ob = entity tier or Coherence −1. |
| 8 | Dissolve (intelligibility axis) | Pull (actuality axis) | Intelligibility dissolving + actuality drawing. Everything in the zone loses legibility while the entity draws physical mass toward itself. Structural damage to fortifications and terrain: Fortification −1 per season of sustained presence. |
| 9 | Loose (actuality axis) | Dissolve (actuality axis) | Double actuality disruption. Severe localised rendering failure. Everything in the zone is partially un-rendered — the Game Master describes visual distortion, spatial incoherence. Thread Tension +2 if this zone is near a Thread Wound territory. Practitioners: Coherence −1 immediately on entering zone. |
| 10 | Pull (temporality axis) | Lock (intelligibility axis) | Temporal pull + intelligibility lock. The entity draws the past forward while making the present unreadable. Every character in the zone experiences a forced Memory check — they re-experience a past scene from their History (Game Master chooses). This is not voluntary. Certainty check Ob 1 or lose 1 Certainty. |

---

## Scale Modifiers by Entity Tier

| Tier | Gap context | Compound ops | Ob to resist | Area of effect |
|------|-------------|-------------|--------------|---------------|
| 1 | Small, recent Gap | 2 | 1 | Single zone |
| 2 | Significant Gap | 2 | 2 | Zone + adjacent zone |
| 3 | Major Gap or Southernmost interior | 3 | 3 | All zones in territory |

For Tier 3: roll three compound operations. All three apply simultaneously. This is the Einhir principle in reverse — at large scale, the consequences exceed any practitioner's ability to manage.

---

## Game Master Usage Notes

- Entities do not "choose" their compound operations. Roll at the start of each round of contact. The operations change round to round because the entity's excess is not stable.
- Practitioners inside the entity's effect zone add the entity tier to all Thread operation Obs (the entity's Thread noise interferes with intentional work).
- A practitioner who successfully Dissolves a Tier 2+ entity: Thread Tension −1d3 (the entity was contributing to Thread instability). This is the primary mechanical incentive for engaging entities rather than retreating.
- The Southernmost wardens' primary activity is containing Tier 2–3 entities and preventing them from reaching territories where their zone of effect would overlap with settled populations. Edeyja has fought Tier 3 entities multiple times. This is the injury context.

---

## Compound Operation — Abbreviated Reference Card (for play use)

| Code | Axes | Shorthand |
|------|------|-----------|
| L+P | Act + Temp | Destabilise + drain time |
| K+D | Act + Intel | Freeze + blind |
| P+L | Act + Intel | Draw + blur |
| D+K | Act + Temp | Unmake + freeze |
| L+K | Temp + Act | Time-distort + immobilise |
| P+D | Intel + Temp | Drain legibility + erase past |
| K+L | Intel + Act | Blind + dissolve presence |
| D+P | Intel + Act | Blur + pull mass |
| L+D | Act + Act | Double actuality failure |
| P+K | Temp + Intel | Past-surge + blind |