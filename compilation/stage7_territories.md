# PART NINE: TERRITORIES

The Valn Peninsula is divided into fifteen territories on a territory-adjacency graph (not a hex grid at the strategic level). Each territory has a name, starting controller, six properties, and adjacency connections.

---

## 9.1 Territory Properties

| Property | Scale | Description |
|---|---|---|
| Prosperity | 1–7 | Economic output and population wellbeing. Affects muster Ob and Wealth income. |
| Fortification | 0–3 (max 4 at Ehrenfeld) | Defensive bonus. Attacker Ob +1 per Fortification level when assaulting. |
| Special property | — | Unique mechanical effect for that territory |
| Controller | Faction | Which faction holds the territory |
| Stability | 1–7 (territory-level) | Local population cohesion |
| Guild Favour | 1–7 | Guild presence and economic integration |

**Territory control:** A faction controls a territory if it has the only military units present or won the most recent battle there. Uncontrolled territories yield no control bonuses — the first faction to station units claims control. Contested territories (multiple factions with units present) grant no control bonuses to anyone until resolved.

**Einhir Sites:** Each site has a visible state — Intact, Damaged, or Destroyed.
- Intact: +1 Stability to the territory, −1 TT per season
- Damaged: neither bonus
- Destroyed: TT +3 at moment of destruction (permanent); practitioners present sense it viscerally and immediately

The Church can destroy Einhir sites as a deliberate Domain Action. Niflhel inadvertently damages them through harvesting operations. Einhir sites on contested battlefields can be destroyed as a tactical action.

---

## 9.2 Territory Map (15 Territories)

| # | Territory | Start Control | Prosperity | Fort | Special Property | Adjacent To |
|---|---|---|---|---|---|---|
| 1 | Valorsplatz *(Capital)* | Crown | 6 | 2 | **Royal Court:** Crown Decree −1 Ob here. **Parliament:** Hafenmark Influence −1 Ob here. | 2, 3, 5, 6 |
| 2 | Kronmark *(Crown heartland)* | Crown | 5 | 1 | **Garrison:** +1 Muster die here. | 1, 3, 4 |
| 3 | Himmelstift *(Cathedral city)* | Church | 5 | 2 | **Grand Cathedral:** TC +1/season while Church controls this. Church Excommunicate −1 Ob here. | 1, 2, 6, 7 |
| 4 | Border Pass | Crown | 3 | 2 | **Altonian Border:** IP threshold events trigger here first. Primary invasion entry point. | 2, 5, 15 |
| 5 | Ehrenfeld *(Military heartland)* | Crown *(Löwenritter garrison)* | 4 | 3 | **Löwenritter Fortress:** Löwenritter Martial Law −1 Ob here. Fortification max 4 (not 3). | 1, 4, 9 |
| 6 | Hafenstadt *(Hafenmark capital)* | Hafenmark | 6 | 1 | **Ducal Court:** Sovereign Authority Doctrine can be invoked here. Major port. | 1, 3, 7, 8 |
| 7 | Sternhaven *(Northern port)* | Hafenmark | 5 | 0 | **Trade Hub:** All Trade orders +1D here. Schoenland route terminus. | 3, 6, 8 |
| 8 | Grauwald *(Forest region)* | Guilds | 4 | 0 | **Timber/Mining:** Guilds Trade +1D here. Difficult terrain: March costs 2 movement (not 1). | 6, 7, 10, 11 |
| 9 | Eisengrund *(Southern highlands)* | Varfell | 4 | 1 | **Varfell Seat:** Private Collection usable here only. Einhir ruins: Revolution Community Weaving −1 Ob. | 5, 10, 12, 13 |
| 10 | Schwarzmarkt *(Underground trade)* | Niflhel | 3 | 0 | **Black Market:** Niflhel Quiet Network −1 Ob here. All factions can Trade here at +1 Ob (illicit goods). | 8, 9, 11 |
| 11 | Feldmark *(Farming plains)* | Guilds | 5 | 0 | **Breadbasket:** +1 Prosperity recovery per season if not contested. Muster Ob −1 (willing recruits). | 8, 10, 14 |
| 12 | Sudwald *(Southern forest)* | Uncontrolled | 3 | 0 | **Thread Wound:** TT threshold events manifest here 10 TT earlier than elsewhere. Revolution presence (not control). | 9, 13, 14 |
| 13 | Askeheim *(Southernmost border)* | Uncontrolled | 2 | 0 | **Southernmost Access:** Required for Southernmost Expedition (§6.3). Thread proximity: all non-Thread orders +1 Ob. TS 30+ characters: automatic Discovery Event per season present. | 9, 12 |
| 14 | Korntal *(Southern farmland)* | Revolution *(informal)* | 4 | 0 | **Einhir Heartland:** Revolution Influence −1 Ob here. Restoration Movement stronghold. Church Influence +1 Ob here (cultural resistance). | 11, 12 |
| 15 | Schoenland *(Altonian trade port)* | Neutral *(Altonian trade)* | 5 | 1 | **Altonian Trade:** +1 Wealth to any faction with Trade order here (while trade route open). Altonian spies: Intelligence orders here reveal results to Altonia. At IP 75+: Altonian vanguard deploys here. | 4, 7 |

[EDITORIAL: Territory names (1–14) are functional placeholders. Editorial naming pass pending.]

---

## 9.3 Adjacency Notes

- **Schoenland** (15) connects to Border Pass (4) by land and Sternhaven (7) by sea. The sea route is severed if Schoenland trade is suspended.
- **Askeheim** (13) is a dead end — connects only to Sudwald (12) and Eisengrund (9). Expedition territory, not strategic.
- **Valorsplatz** (1) is the most connected territory (4 adjacencies) — the political and strategic hub.
- **Grauwald** (8) difficult terrain applies to military movement only, not to Domain Actions.

---

## 9.4 Strategic Movement

- Standard movement: 1 territory per season by road
- Mountain pass: 2 seasons through designated passes
- Naval: coastal territories accessible to Hafenmark or any faction with active Schoenland trade agreement

**Supply lines:** Armies more than 2 territories from a friendly-controlled territory with Wealth 3+ begin attrition: −1 Endurance to all units per season. Winter campaigns in mountain terrain: −1 Endurance automatically.

---

## 9.5 TTRPG Zone-Based Play

In TTRPG mode, territories function as scene-setting zones rather than strategic counters. The GM uses territory properties to generate scene modifiers and encounter context.

**Zone modifiers in TTRPG mode:**
- Fortification level → ambient difficulty for infiltration, assault, or sabotage operations
- Prosperity → available contacts and resources (Circles Ob modifier: high Prosperity −1 Ob, low Prosperity +1 Ob)
- Special properties → GM applies the property's mechanical effect when characters act in that territory
- Einhir site state → practitioner perception layer (Intact sites are perceptible to TS 30+ as a distinct warmth in the configurational environment)

**Thread environment by territory:**
- Askeheim (13): permanent Thread proximity bonus/hazard regardless of TT level — treat as if TT is always +10 for practitioner purposes
- Sudwald (12): Thread Wound territory — TT threshold events fire here at (actual TT − 10)
- Eisengrund (9): Einhir ruins — Community Weaving −1 Ob regardless of who performs it
- Any territory with Intact Einhir site: practitioners within the territory gain +1D on Weaving and Pulling

---

## 9.6 Victory Conditions (Per Faction)

**Shared loss condition:** TT reaches 100. The Rupture occurs. No faction survives in recognisable form. This is the cooperative pressure underlying the competitive game — all players must manage TT even while competing.

**Per-faction victory conditions:**

| Faction | Primary Victory | Secondary (Points if no primary by Season 10) |
|---|---|---|
| Crown | Control Valorsplatz + 4 other territories. Mandate ≥ 5. | 1 pt/controlled territory + 1 pt/Mandate above 3 + 2 pts if heir secure (Torben Loyalty ≥ 5) |
| Church | TC reaches 80. Church controls Himmelstift + Valorsplatz. | 1 pt per 10 TC + 1 pt/territory where Church Mandate > Crown Mandate + 2 pts if Excommunication active |
| Hafenmark | Parliamentary Supremacy: Mandate + Influence both ≥ 6. Crown Mandate ≤ 3. | 1 pt/Influence above 3 + 1 pt/Wealth above 3 + 2 pts if Sovereign Authority successfully invoked |
| Varfell | Possess 3+ Thread-locked artefacts. TS of any affiliated character ≥ 50. | 1 pt/artefact + 1 pt/Intel above 3 + 2 pts if Einhir Research completed |
| Guilds | Wealth ≥ 7 AND Economic Leverage active in 3+ territories simultaneously. | 1 pt/Wealth above 3 + 1 pt/territory with Guild Favour ≥ 5 + 2 pts if all trade routes open |
| Niflhel | Intel ≥ 5 in 3+ territories via Quiet Network. No faction knows Niflhel's true Stability. | 1 pt/Intel above 3 + 1 pt/successful assassination + 1 pt/covert territory control |
| Revolution | TT ≤ 20 via Community Weaving. Revolution Influence ≥ 5. Einhir cultural practices publicly restored. | 1 pt/Influence above 2 + 1 pt per 10 TT reduced below starting value + 2 pts if Restoration publicly active |
| Löwenritter | Successful coup + control Valorsplatz + Border Pass + Ehrenfeld. IP ≤ 20, no Altonian units on map. | 1 pt/Military above 3 + 1 pt/controlled territory + 2 pts if coup triggered + 2 pts if Altonia repelled |

[EDITORIAL: Varfell victory condition — possession of 3 artefacts is the current threshold. Confirm or tune.]

**Victory timing:** Primary victory checked at end of each season. If multiple factions achieve primary simultaneously: highest point total wins. Ties broken by Stability. Season 10 endpoint: highest points wins.

---

*End of Stage 7 compilation. Stage 8 (Combat: pool split, priority, reach, manoeuvres, mass combat, siege) follows.*
