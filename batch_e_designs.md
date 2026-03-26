# Phase 1 — Batch E: Board Game Design
## Date: 2026-03-25 (Session 5)
## Status: Design briefs
## Covers: G-025, G-026, G-027 (resolved S3), G-028, G-029, G-030, G-031, G-049, G-050, G-051, G-057, G-058 (resolved S3), G-059, G-060

---

# DESIGN PRINCIPLES

1. **The board game is a standalone game.** It must be playable without the TTRPG rulebook. It must be learnable in one session.
2. **Faction asymmetry is the core experience.** Each faction plays differently — different Order Sets, different victory conditions, different strengths. (Root model, not Risk model.)
3. **The board game uses the same 6 faction attributes as the TTRPG** (1-7 scale). Faction sheets are shared across modes.
4. **Three clocks drive the campaign arc:** TT, TC, IP. These advance automatically and through player action. The game ends when a victory condition or a shared loss condition fires.
5. **Simultaneous order placement** with sequential resolution. (ASOIAF/Dune model.)
6. **2-5 players + solo mode.** Uncontrolled factions run on NPC AI.
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
3. Clock advances: TT baseline drift (+1 at Winter only). TC advances per Church activity. IP advances per Altonian pressure table.
4. Check threshold events (TT/TC/IP threshold tables from existing rules).
5. Draw Event Card if applicable (see G-050).
6. Co-Movement resolution: any faction that performed a Thread operation or crossed a TT threshold draws a Co-Movement Card.
7. Check victory conditions.
8. Season marker advances. If Winter: year-end accounting (TT drift, annual events).
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
| 3 | Himmelstift (Cathedral city) | Church | 5 | 2 | Grand Cathedral: TC +1 per season Church controls this. Church Excommunicate -1 Ob here. | 1, 2, 6, 7 |
| 4 | Border Pass | Crown | 3 | 2 | Altonian Border: IP threshold events trigger here first. Invasion entry point. | 2, 5, 15 |
| 5 | Ehrenfeld (Military heartland) | Crown (Lowenritter garrison) | 4 | 3 | Lowenritter Fortress: Lowenritter Martial Law -1 Ob here. +1 Fortification max (4 here). | 1, 4, 9 |
| 6 | Hafenstadt (Hafenmark capital) | Hafenmark | 6 | 1 | Ducal Court: Hafenmark Sovereign Authority can be invoked here. Major port. | 1, 3, 7, 8 |
| 7 | Sternhaven (Northern port) | Hafenmark | 5 | 0 | Trade Hub: all Trade orders +1D here. Schoenland route terminus. | 3, 6, 8 |
| 8 | Grauwald (Forest region) | Guilds | 4 | 0 | Timber/Mining: Guilds Trade +1D here. Difficult terrain: March costs 2 movement (not 1). | 6, 7, 10, 11 |
| 9 | Eisengrund (Southern highlands) | Varfell | 4 | 1 | Varfell Seat: Private Collection usable here only. Einhir ruins: Revolution Community Weaving -1 Ob. | 5, 10, 12, 13 |
| 10 | Schwarzmarkt (Underground trade) | Niflhel | 3 | 0 | Black Market: Niflhel Quiet Network -1 Ob here. All factions can Trade here at +1 Ob (illicit goods). | 8, 9, 11 |
| 11 | Feldmark (Farming plains) | Guilds | 5 | 0 | Breadbasket: +1 Prosperity recovery per season (if not contested). Muster Ob -1 (willing recruits). | 8, 10, 14 |
| 12 | Sudwald (Southern forest) | Uncontrolled | 3 | 0 | Thread Wound: TT threshold events hit here at -10 TT (earlier than elsewhere). Revolution presence (not control). | 9, 13, 14 |
| 13 | Askeheim (Southernmost border) | Uncontrolled | 2 | 0 | Southernmost Access: required for Southernmost Expedition. Thread proximity: all non-Thread orders +1 Ob. TS 30+ characters: automatic Discovery Event per season here. | 9, 12 |
| 14 | Korntal (Southern farmland) | Revolution (informal) | 4 | 0 | Einhir Heartland: Revolution Influence -1 Ob here. Restoration Movement stronghold. Church Influence +1 Ob here (cultural resistance). | 11, 12 |
| 15 | Schoenland (Altonian trade port) | Neutral (Altonian trade) | 5 | 1 | Altonian Trade: generates +1 Wealth for any faction with Trade order here (while trade route open). Altonian spies: Intelligence orders here reveal results to Altonia. At IP 75+: Altonian vanguard deploys here. | 4, 7 |

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
**TT reaches 100.** The Rupture occurs. Rendered reality fails. No faction survives in recognizable form. This is the cooperative pressure underlying the competitive game — all players must manage TT even while competing.

### Per-Faction Victory Conditions

Each faction has a **primary** victory condition (wins the game outright) and a **secondary** (wins on points if no outright winner by season 10).

| Faction | Primary Victory | Secondary (Points) |
|---------|----------------|-------------------|
| **Crown** | Control Valorsplatz + 4 other territories at end of any season. Mandate >= 5. | 1 pt per controlled territory + 1 pt per Mandate above 3 + 2 pts if heir secure (Torben Loyalty >= 5). |
| **Church** | TC reaches 80. Church controls Himmelstift + Valorsplatz. | 1 pt per 10 TC + 1 pt per territory where Church Mandate > Crown Mandate + 2 pts if Excommunication active. |
| **Hafenmark** | Parliamentary Supremacy: Hafenmark Mandate + Influence both >= 6. Crown Mandate <= 3. | 1 pt per Influence above 3 + 1 pt per Wealth above 3 + 2 pts if Sovereign Authority successfully invoked. |
| **Varfell** | Possess 3+ Thread-locked artifacts (via Private Collection or expedition). TS of any affiliated character >= 50. | 1 pt per artifact + 1 pt per Intelligence above 3 + 2 pts if Einhir Research completed. |
| **Guilds** | Wealth >= 7 AND Economic Leverage active in 3+ territories simultaneously. | 1 pt per Wealth above 3 + 1 pt per territory with Guild Favour 5+ + 2 pts if trade routes all open. |
| **Niflhel** | Control (covertly) 3+ territories' Intelligence networks (Intelligence >= 5 in 3 territories via Quiet Network). No faction knows Niflhel's true Stability. | 1 pt per Intelligence above 3 + 1 pt per successful assassination + 1 pt per covert territory control. |
| **Revolution** | TT reduced to <= 20 via Community Weaving. Revolution Influence >= 5. Einhir cultural practices publicly restored. | 1 pt per Influence above 2 + 1 pt per 10 TT reduced below starting value + 2 pts if Restoration publicly active. |
| **Lowenritter** | Successful military coup + control of Valorsplatz + Border Pass + Ehrenfeld. All foreign influence expelled (IP <= 20, no Altonian units on map). | 1 pt per Military above 3 + 1 pt per controlled territory + 2 pts if coup triggered + 2 pts if Altonia repelled. |

### Victory Timing
- Primary victory checked at end of each season (Phase 5, step 7).
- If multiple factions achieve primary victory simultaneously: the faction with higher total points wins.
- If no primary victory by season 10: highest point total wins. Ties broken by Stability (most stable faction endures).

### Design Notes
- Crown's victory is the "default" — maintain the status quo. It's the hardest to disrupt but the easiest to erode.
- Church's victory is clock-driven — TC advances naturally. Other factions must actively suppress it.
- Revolution's victory is cooperative with the shared survival goal — reducing TT helps everyone. But it requires the Revolution to become publicly powerful, which other factions resist.
- Lowenritter's victory is conditional — they can't even attempt it without a coup trigger. They're a latent threat that activates under crisis.
- Niflhel's victory is information-based — they win by knowing everything while being known by no one.

---

# CLUSTER 4: SYSTEMS

## G-050: Event Deck / World Event System

### Event Card Types

**Clock Events (triggered automatically):**
When TT, TC, or IP crosses a threshold (every 20 points), draw from the corresponding clock event table. These are pre-scripted — not random.

| Clock | Threshold | Event |
|-------|-----------|-------|
| TT 20 | Shifting Objects appear in 1d3 territories. Cosmetic but unsettling. |
| TT 40 | Southernmost expedition becomes possible. Thread Wounds visible in Sudwald/Askeheim. |
| TT 60 | Gaps appear. One random territory: all orders +1 Ob this season (reality unstable). Practitioners gain +1D to Thread ops. |
| TT 80 | Monstrous entities emerge in Sudwald and Askeheim. Military units there: Cohesion check Ob 2 or -1 Cohesion. |
| TC 20 | Church begins Heresy Investigation in 1 territory (GM/AI choice). |
| TC 40 | Templar units deploy. Church gains 1 free military unit in Himmelstift. |
| TC 60 | Church demands civil authority in 1 territory. Crown must Refuse (TC +2) or Comply (Crown Mandate -1 in that territory). |
| TC 80 | Church claims territories of influence. Church begins controlling territories where Church Mandate > Crown Mandate. These territories' control shifts to Church. |
| IP 30 | Altonian demands begin. Tutoring Demand activates (see succession mechanic). |
| IP 45 | Altonian proxy units appear at Border Pass. |
| IP 60 | Altonian army visible. Diplomatic Resolution possible. |
| IP 75 | Altonian vanguard at Schoenland. Trade suspended. |
| IP 100 | Full invasion. Altonian army enters via Border Pass + Schoenland. |

**Seasonal Events (1 per season, drawn randomly):**
A deck of 20 cards, shuffled at game start. Draw 1 per season at Accounting. These inject variety and force adaptation.

Example events (10 of 20):
1. **Plague** — one territory (lowest Prosperity): Prosperity -1, Muster Ob +2 this territory for 2 seasons.
2. **Bumper Harvest** — Feldmark and Korntal: Prosperity +1 this season.
3. **Heretic Scholar** — a practitioner surfaces publicly. Church TC +2. Revolution Influence +1. Random territory.
4. **Bandit Uprising** — Grauwald or Schwarzmarkt: 1 bandit unit appears (Martial 2, Cohesion 3). Attacks any faction present.
5. **Diplomatic Envoy** — Altonia sends a trade delegation. Any faction may attempt Trade with +1D in Schoenland this season.
6. **Mine Collapse** — Grauwald or Eisengrund: Prosperity -1 permanently until Govern order restores it.
7. **Einhir Festival** — Korntal: Revolution Influence +1. Church Mandate -1 in Korntal (pagan celebration offends).
8. **Assassination Attempt** — target faction leader (highest Mandate). Roll target Stability vs Ob 2. Failure: leader incapacitated 1 season (no Unique Action).
9. **Trade Dispute** — two adjacent territories: Trade orders fail in both this season unless Treaty in place.
10. **Thread Tremor** — TT +2. One random territory: all orders +1 Ob (configurational instability).

---

## G-051: Season Wheel / Seasonal Differentiation

Four seasons rotate: Spring → Summer → Autumn → Winter. Each has a modifier.

| Season | Modifier |
|--------|----------|
| **Spring** | Muster +1D (recruitment season). March into mountain/forest territories: no terrain penalty. |
| **Summer** | Trade +1D (peak commerce). Military Cohesion checks: +1D (morale high). |
| **Autumn** | Harvest: all controlled territories with Prosperity 4+: +1 Wealth to controlling faction. Siege -1D (approaching winter). |
| **Winter** | All March orders: -1D (weather). Siege: besieged faction Stability check Ob 2 (starvation pressure). TT annual drift +1. Year-end accounting. |

A full campaign = 10 seasons. Default start: Spring Year 1. Seasons 1-4 = Year 1, 5-8 = Year 2, 9-10 = first half of Year 3 (Spring + Summer).

The season wheel is a physical component (rotating dial or track on the board).

---

## G-057: Thread Operations (Simplified Faction-Card Procedure)

In the board game, Thread operations are abstracted to faction-level actions. No personal-scale Thread scenes.

### Thread Orders (available to factions with Thread capability)

**Thread-capable factions:** Varfell (via Private Collection), Revolution (via Community Weaving), any faction with an affiliated TS 30+ character.

| Thread Order | Roll | Effect |
|--------------|------|--------|
| **Weave** | Intelligence (or faction-specific attribute) vs Ob = TT / 20 (round up) | Success: TT -1. Overwhelming: TT -2. Failure: TT +1. |
| **Investigate Thread** | Intelligence vs Ob 3 | Success: learn current TT value (normally hidden from players). Overwhelming: also learn which territories have Thread Wounds. |
| **Thread Harvest** (Niflhel only) | Intelligence vs Ob 2 | Success: +1 Wealth (dissolution residue trade). TT +0.5 (tracked as half-points, round up at accounting). |

All Thread operations draw a Co-Movement Card at Accounting (per P-01).

### Co-Movement Cards
Deck of 15 cards. Draw 1 whenever a Thread operation occurs or TT crosses a threshold.

Effects are unpredictable and can be positive, negative, or lateral:
1. Stability -1 (acting faction) — Thread backlash.
2. TT +1 — operation disturbed more than it healed.
3. One territory: Prosperity +1 — configurational alignment benefits the land.
4. Random faction: Intelligence -1 for 1 season — Thread noise disrupts information networks.
5. Acting faction: Influence +1 — the population senses something has changed for the better.
6. TT -1 — resonance cascade (beneficial).
7. One unit in acting faction's territory: Cohesion -1 — soldiers sense wrongness.
8. No effect — the Thread absorbs the operation without visible consequence.
9. Acting faction: Mandate -1 — the operation was subtly visible. Someone noticed.
10. Church TC +1 — the Church's theological sensors detect heterodoxy.
11. One practitioner NPC surfaces in a random territory — a Thread event drew them out.
12. Acting faction: +1D to next Thread operation — resonance established.
13. Two territories: swap Prosperity values — configurational drift reshapes the land.
14. IP -1 — Altonia's intelligence network suffers Thread interference.
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
| Clock tracks | 3 | TT (0-100), TC (0-100), IP (0-100) — printed on board |
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

## G-031: NPC AI Expansion

When fewer than 8 players, uncontrolled factions run on NPC AI. The AI follows a simple decision tree per faction, evaluated each season.

### AI Decision Framework

Each NPC faction has 3 priorities (ordered). The AI selects orders to serve the highest unfulfilled priority.

| Faction | Priority 1 | Priority 2 | Priority 3 |
|---------|-----------|-----------|-----------|
| Crown | Maintain control of Valorsplatz | Defend Border Pass | Govern (increase Stability) |
| Church | Increase TC (place orders that advance TC) | Expand to new territory via Influence | Suppress heresy (Spy on Thread-active factions) |
| Hafenmark | Protect Hafenstadt + Sternhaven | Trade (increase Wealth) | Influence in Valorsplatz (political power) |
| Varfell | Use Private Collection if available | Spy (increase Intelligence advantage) | Defend Eisengrund |
| Guilds | Trade in highest-Prosperity territory | Economic Leverage against weakest rival in Guild territory | Govern (maintain Prosperity) |
| Niflhel | Quiet Network (intelligence gathering) | Trade in Schwarzmarkt | Avoid exposure (never March openly) |
| Revolution | Community Weaving (reduce TT) | Influence in Korntal/Sudwald | Avoid military confrontation |
| Lowenritter | Fortify Ehrenfeld/Border Pass | Monitor coup trigger conditions | Follow Crown orders (support Crown's highest-priority unfulfilled order) |

### AI Order Selection Procedure
1. Check Priority 1. If the condition is unmet, select the order that best addresses it.
2. If Priority 1 is met, check Priority 2. Select accordingly.
3. If both met, Priority 3.
4. Remaining orders (if 3-order faction): default to Govern in controlled territory.
5. NPC factions never negotiate Treaties. They respond to player-initiated Treaties with a coin flip (50% accept).

### AI Escalation
- If an NPC faction's Stability drops to 2 or below: all orders become defensive (Fortify, Govern, no offensive actions).
- If an NPC faction is attacked: it retaliates against the attacker next season (Priority 1 override).
- Church AI: if TC >= 60, AI shifts to aggressive expansion (Priority 1 becomes "claim territory where Church Mandate > Crown Mandate").
- Lowenritter AI: if any coup trigger condition is met, AI initiates coup next season.

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
| G-050 | Designed | Remaining 10 seasonal event cards to be written |
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
- **P-11 (TD universal):** Every Thread operation in board game has TD cost via Co-Movement Cards — no free Thread work.
- **P-14 (all modes express inseparability):** The shared TT loss condition forces all factions to acknowledge Thread reality even while pursuing political goals. The board game mechanically prevents pure political play from being sufficient — someone must manage TT or everyone loses.
