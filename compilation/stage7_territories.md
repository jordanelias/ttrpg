# PART SEVEN: TERRITORIES

Valoria comprises fifteen territories arranged in a roughly north-south layout, connected by an adjacency graph (not a hex map). Territories are the primary unit of control in board game and hybrid modes, and the geographic backdrop for TTRPG scenes. Each territory has a Prosperity score, a Fortification level, a starting controller, and at least one special property.

---

## 7.1 Territory Properties

Each territory tracks four attributes:

| Attribute | Scale | Meaning |
|---|---|---|
| Prosperity | 1–7 | Economic output; affects mustering Ob, Wealth generation, and population mood |
| Fortification | 0–3 (0–4 at Ehrenfeld) | Defense bonus; Fortification 2+ required for a siege to be declared |
| Control | Faction or Neutral | Which faction controls this territory and receives its benefits |
| Special Property | Fixed | Unique mechanical effect; does not change unless specifically altered |

**Control** transfers when one faction has the only military units present, or wins the most recent battle. Contested (multiple factions with units): no control benefits for anyone until resolved.

---

## 7.2 Territory Map

| # | Territory | Starting Control | Prosperity | Fort | Special Property | Adjacent |
|---|---|---|---|---|---|---|
| 1 | Valorsplatz (Capital) | Crown | 6 | 2 | Royal Court: Crown Decree −1 Ob here. Parliament: Hafenmark Influence −1 Ob here. | 2, 3, 5, 6 |
| 2 | Kronmark (Crown heartland) | Crown | 5 | 1 | Garrison: +1D Muster here. | 1, 3, 4 |
| 3 | Himmelstift (Cathedral city) | Church | 5 | 2 | Grand Cathedral: TC +1 per season Church controls this. Church Excommunicate −1 Ob here. | 1, 2, 6, 7 |
| 4 | Border Pass | Crown | 3 | 2 | Altonian Border: IP threshold events trigger here first. Invasion entry point. | 2, 5, 15 |
| 5 | Ehrenfeld (Military heartland) | Crown / Lowenritter garrison | 4 | 3 | Lowenritter Fortress: Lowenritter Martial Law −1 Ob here. Fortification maximum 4 (not 3). | 1, 4, 9 |
| 6 | Hafenstadt (Hafenmark capital) | Hafenmark | 6 | 1 | Ducal Court: Hafenmark Sovereign Authority may be invoked here. Major port. | 1, 3, 7, 8 |
| 7 | Sternhaven (Northern port) | Hafenmark | 5 | 0 | Trade Hub: all Trade orders +1D here. Schoenland sea route terminus. | 3, 6, 8 |
| 8 | Grauwald (Forest region) | Guilds | 4 | 0 | Timber and Mining: Guilds Trade +1D here. Difficult terrain: March costs 2 movement (not 1). | 6, 7, 10, 11 |
| 9 | Eisengrund (Southern highlands) | Varfell | 4 | 1 | Varfell Seat: Private Collection usable here only. Einhir ruins: Revolution Community Weaving −1 Ob. | 5, 10, 12, 13 |
| 10 | Schwarzmarkt (Underground trade) | Niflhel | 3 | 0 | Black Market: Niflhel Quiet Network −1 Ob here. All factions Trade here at +1 Ob (illicit goods). | 8, 9, 11 |
| 11 | Feldmark (Farming plains) | Guilds | 5 | 0 | Breadbasket: +1 Prosperity recovery per season if uncontested. Muster Ob −1 (willing recruits). | 8, 10, 14 |
| 12 | Sudwald (Southern forest) | Uncontrolled | 3 | 0 | Thread Wound: TT threshold events trigger here at TT −10 (earlier than elsewhere). Revolution informal presence. | 9, 13, 14 |
| 13 | Askeheim (Southernmost border) | Uncontrolled | 2 | 0 | Southernmost Access: required for Southernmost Expedition. Thread proximity: all non-Thread orders +1 Ob. TS 30+ characters: automatic Discovery Event per season present. | 9, 12 |
| 14 | Korntal (Southern farmland) | Revolution (informal) | 4 | 0 | Einhir Heartland: Revolution Influence −1 Ob here. Church Influence +1 Ob here (cultural resistance). | 11, 12 |
| 15 | Schoenland (Altonian trade port) | Neutral (Altonian trade) | 5 | 1 | Altonian Trade: +1 Wealth per season to any faction with Trade order here while route is open. Altonian spies: Intelligence orders here reveal results to Altonia. At IP 75+: Altonian vanguard deploys here. | 4, 7 |

---

## 7.3 Adjacency Notes

- **Valorsplatz (1)** is the most connected territory (4 adjacencies). Political hub; changes hands are maximum-consequence.
- **Schoenland (15)** connects to Border Pass by land and Sternhaven by sea. The sea route is severed when Schoenland trade suspends (IP 75+).
- **Askeheim (13)** is a dead end — only two connections. It is expedition territory, not strategic chokepoint.
- **Ehrenfeld (5)** is the Lowenritter's primary position. Its anomalous Fortification cap (4 instead of 3) reflects the order's entrenched presence.

---

## 7.4 Territory Control Mechanics

### Control Benefits (TTRPG/Hybrid)

A controlling faction treats the territory's Prosperity as a Domain Action resource. Controlled territories contribute to seasonal Wealth accounting and allow Muster actions.

A territory changes control when:
- A faction moves units in and no enemy units are present.
- A battle resolves with the defending faction's units destroyed or routed.
- A Govern order succeeds in an uncontrolled territory (first Govern = claim).

### Prosperity Dynamics

Prosperity changes through:
- Muster: −1 per muster action (labor and resources diverted).
- Conquest: −1 immediately (war damage).
- Govern Overwhelming success in own territory: +1.
- Breadbasket property (Feldmark): +1 per season if uncontested.
- Mine Collapse event: −1 permanent until Govern restores.
- Extended siege: −1 Endurance per season for garrisoned units; territory Stability affected.

Prosperity recovery rate (no active effects): +1 per season of peace if territory is controlled and not at Prosperity cap (7).

### Fortification

Built with Fortify orders. Maximum 3 for standard territories; 4 for Ehrenfeld only. Fortification level determines siege Ob and attack bonus for defenders (+1D per level to relevant defense rolls).

Fortification 2+ is required for a siege to be declared. Territories at 0–1 are assaulted directly.

---

## 7.5 Thread-Significant Territories

Three territories have Thread significance beyond their political properties:

**Sudwald (12):** A Thread Wound in the southern forest. TT threshold events fire here 10 TT points earlier than elsewhere. The Revolution's informal presence here is not coincidental — Einhir practitioners recognized the site's significance.

**Askeheim (13):** Proximity to the Southernmost creates ambient Thread pressure. All non-Thread orders suffer +1 Ob. This is the only territory from which the Southernmost Expedition can be launched (see §4.7, Southernmost).

**Eisengrund (9):** Einhir ruins beneath the Varfell highlands. The Revolution's Community Weaving is easier here (−1 Ob) because the configurational substrate retains resonance. Varfell's Private Collection access is tied to this site.

---

## 7.6 TTRPG Zone-Based Movement

In TTRPG mode, territories are not tracked with unit tokens. They function as named locations with associated properties. Movement between territories is narrative, not mechanical — the GM determines journey time based on terrain and circumstance.

For overland journeys of consequence (expeditions, supply runs, military marches), use the territory adjacency graph as a rough distance guide. Standard overland travel: one territory per day under normal conditions; Grauwald costs two days (difficult terrain).

Thread-significant territories require awareness: entering Askeheim or the Sudwald Thread Wound zone triggers the relevant passive effects on practitioners (automatic Discovery Events, TS growth checks) when applicable.
