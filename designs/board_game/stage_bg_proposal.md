# VALORIA: BOARD GAME MODE — REVISED PROPOSAL

## Date: 2026-03-31
## Status: Proposal — requires editorial review before compilation
## Supersedes: stage_bg_board_game_mode.md (current compilation)
## Sources: bg_improvement_v1–v4.md, bg_synthesis.md, bg_consolidated_synthesis.md, bg_synthesis_amendment_1.md

---

## DESIGN PRINCIPLES

The board game is one of three mandatory game modes (TTRPG, Hybrid, Board Game). It is a complete standalone game that also functions as the strategic layer in hybrid play. It must satisfy four simultaneous requirements:

1. **Standalone completeness.** A 2–4 hour game with full arc, emergent narrative, and moral weight.
2. **Hybrid integration.** Clean handoffs to/from TTRPG personal-scale play at any point. Scale interweaving, not bolted-on zoom-in.
3. **Political weight.** The faction landscape, its boiling points, its institutional tensions — these give the game purpose. TC and IP generate decisions as compelling as RS.
4. **Metaphysical coherence.** Thread is the constitutive ground, not a subsystem. Every action occurs on a substrate that is degrading. P-01–P-14 compliance without exception.

**The feel:** Powerful institutions trying to manage a world that is quietly dying. Every strategic decision carries identity consequences that outlast the season. Victory is possible but never clean.

---

## B1: OVERVIEW AND SETUP

### Player Count

| Players | Mode |
|---|---|
| 1 | Solo (see B14) |
| 2 | Competitive asymmetric; NPC AI runs remaining factions |
| 3–4 | Competitive-cooperative; NPC AI runs remainder |
| 5 | Full coverage (Crown, Church, Hafenmark, Varfell, Guilds, Niflhel) — one player takes two factions or Crown+Löwenritter |
| 6 | Full faction coverage |

Revolution is always NPC-controlled. Schoenland is always NPC-controlled.

### Components

**Boards and Tracks**
- 1× Main board: territory map (15 territories), 3 clock tracks (RS 100→0, TC 0→100, IP 0→100), Church Attention Pool track (0–10), round tracker
- 15× Territory tiles with Prosperity/Fortification values + Substrate Scar slots
- 1× Senate Market board (6 card slots)

**Per Faction**
- 1× Faction card (stats, Institutional Mandate, Conviction, ethical framework, Deed Track)
- 1× Champion token (named leader)
- 1× Champion state card (Active/Wounded/Captured/Convalescing)
- 6× Starting Action Cards (faction-specific hand — see B4)
- 1× Recess card
- 1× Cooldown Track (3 slots for Unique Power cooldown)
- 2× Research Track markers
- Stat dials: Mandate / Influence / Wealth / Military / Intel / Stability (where applicable)
- 4× Unit tokens (faction-named types — see B6)
- 3× Deal Tokens (wooden discs in faction colour)
- Contempt token slots on faction card

**Shared Components**
- 1× Co-Movement card deck (20 cards — carries forward from current B7)
- 1× Event deck (30 cards — carries forward from current B9; integrate C-11–C-20 per GT-01)
- 1× Senate Deck (18 purchasable Action Cards)
- 1× Disposition table card
- 12× Secondary Objective cards (2 per faction, shuffled; each player draws 1 at game start)
- Thread Debt tokens (6 total)
- Substrate Scar markers (12 total)
- Contempt tokens (30 total, generic)
- Leverage tokens (30 total, generic)
- Community Project markers + Progress tracks (6 markers)
- Revolution Presence markers (8)
- Niflhel Network Depth markers (15, 1 per territory)
- Faction control markers, Fortification tokens, Prosperity cubes — carry forward from current B1

### Starting State

Clocks: RS 72. TC 15. IP 20. Church Attention Pool: 0.

Territory control, starting Prosperity, Fortification: per current B2 territory table (unchanged).

Each player-controlled faction: place Champion token in home territory. Place 1 unit in home territory. Crown receives 1 additional unit in Arnesheld.

Each faction: draw starting Action Card hand (6 cards, faction-specific — see B4). Place Unique Power card on Cooldown Track slot 0 (available immediately).

All Research Track markers at starting values (see B9).

---

## B2: TERRITORY MAP

Carries forward from current B2. No changes to layout, adjacency, territory table, or territory rules.

**Addition — Clock Environmental Effects:**

The three clocks modify the action environment globally. These modifiers are always active:

**RS Environmental Effects:**
| RS Range | Effect |
|---|---|
| 72–50 | No modifier |
| 49–30 | All Thread operations: −1 Ob (community urgency). All non-Thread orders in T12/T13: +1 Ob (substrate strain bleeds into rendered-world activity) |
| 29–20 | As above. Entity encounters possible in T12/T13 (see B11). Muster in all territories: +1 Ob (population unsettled by ambient wrongness) |
| Below 20 | All orders in all territories: +1 Ob (the world is failing). Community Projects advance +1 per season (urgency). Entity encounters expand to territories adjacent to T12/T13 |

**TC Environmental Effects:**
| TC Range | Effect |
|---|---|
| 0–30 | No modifier |
| 31–50 | Church Preach/Inquisition: −1 Ob everywhere. Non-Church Diplomacy: +1 Ob in Church-controlled territories |
| 51–70 | As above. All factions: Govern in non-home territories +1 Ob (theocratic bureaucratic pressure) |
| 71–80 | Church orders everywhere: −1 Ob. All other factions: Social orders +1 Ob (theocratic dominance suppresses secular discourse) |

**IP Environmental Effects:**
| IP Range | Effect |
|---|---|
| 0–40 | No modifier |
| 41–60 | Trade with Schoenland: +1D (Altonian interest brings opportunity). Intel orders by all factions: +1D (Altonian intelligence flows both directions) |
| 61–75 | Trade with Schoenland: disrupted (+1 Ob). Military orders in T4 (Spartfell) and T15 (Schoenland): +1 Ob (border militarization) |
| 76+ | Altonian vanguard deploys in T15. March into T4: automatic battle. All external Trade: +2 Ob |

---

## B3: FACTION CARDS

Each faction card contains: starting stats, Institutional Mandate, Conviction, ethical framework, unique power, action system, Deed Track, and two Research Track axes.

### Structural Asymmetry

Four factions use structurally distinct action systems. Crown and Hafenmark use the standard Card-Hand system. Varfell uses the standard system with intelligence extensions.

| Faction | Action System | Core Distinction |
|---|---|---|
| Crown | Standard Card-Hand + Policy Instruments | Sets the conditions for all other factions |
| Church | Standard Card-Hand + TC-as-Currency | Consumes its own victory resource to act |
| Hafenmark | Standard Card-Hand | Parliamentary proceduralism as strategic tool |
| Varfell | Standard Card-Hand + TK Intelligence | Information as power |
| Guilds | Contractor Card-Hand (no Military cards) | Rents capability from other factions |
| Niflhel | Standard Card-Hand (no Govern) + Network Depth | Territorial influence without territorial control |
| Revolution (NPC) | Presence Markers + Community Projects | Distributed community infrastructure without institutional orders |

### FACTION: THE CROWN

**Stats:** Mandate 5 · Influence 5 · Wealth 4 · Military 4 · Stability 4

**Ethical Framework: Virtue Ethics** — Public, visible actions: −1 Ob. Covert or morally ambiguous: +1 Ob.

**Leader/Champion: King Almud Almqvist** — Conviction: Order. Deviation cost: Stability check Ob 2.

**Institutional Mandate:** *"The monarchy provides the order that protects Valoria."*
Mandate triggers: Church Excommunication targets Crown-affiliated character; IP crosses 60; another faction controls Valorsplatz; Löwenritter Coup Counter reaches 3.

**Unique Power — Royal Decree** (Cooldown: 2 seasons after use)
Roll Mandate vs Ob 2. Success: one faction attribute change (any faction, ±1) takes effect immediately. Failure: Crown Mandate −1.

**Policy Instruments** (Crown exclusive — see B5)
Each season, Crown may issue one Policy affecting the entire board, in addition to normal card play. Requires Mandate ≥ 4. Same Policy cannot repeat within 2 seasons (tracked on Cooldown Track).

**Starting Card Hand:** 2× Legionary, 1× Consul, 1× Senator, 1× Prefect, 1× Recess

**Research Tracks:** Mandate Authority (starts 2) / Military Tradition (starts 1)

**Victory — Constitutional Stability:** Deed Tokens as currently defined (B3 current). No changes.

---

### FACTION: THE CHURCH OF GALBADOS

**Stats:** Mandate 5 · Influence 6 · Wealth 5 · Military 4 · Stability 5

**Ethical Framework: Divine Command** — Doctrine-aligned: −1 Ob. Thread-supporting: +2 Ob.

**Leader/Champion: Confessor Arne Himlensendt** — Conviction: Faith. Deviation cost: Stability check Ob 3.

**Institutional Mandate:** *"Solmund's doctrine is the rightful framework for all governance."*
Mandate triggers: TC drops below previous season's value; a parliamentary ruling contradicts Church authority; a Thread operation occurs in Church-controlled territory and Church fails to respond.

**TC-as-Currency:** Church may voluntarily spend TC to pay for enhanced actions:
| Cost | Effect |
|---|---|
| 2 TC | Deploy 1 Templar unit anywhere Church controls (no Muster card required) |
| 1 TC | Preach action costs no card play this season (free action) |
| 3 TC | Declare Interdict on one territory — no faction may Trade there for 1 season; Church gains 1 TC back at accounting |

This creates the Church's central dilemma: TC is both victory resource AND action currency. Spending TC to win faster reduces the margin for error.

**Unique Power — Excommunication** (Cooldown: 3 seasons)
Roll: Mandate vs target leader's Mandate. Outcomes as currently defined (B3 current).

**Starting Card Hand:** 2× Senator, 1× Pontifex (free at game start), 1× Consul, 1× Legionary, 1× Recess

**Research Tracks:** Doctrinal Reach (starts 2) / Inquisition Network (starts 2)

**Victory — The Holy State:** Deed Tokens as currently defined. No changes.

---

### FACTION: HAFENMARK

Carries forward from current B3 with the following additions:

**Institutional Mandate:** *"Constitutional process is the only legitimate source of authority."*
Mandate triggers: Crown issues Emergency Powers policy; Church Excommunicates without Grand Debate; any faction seizes territory by force without prior Diplomacy attempt.

**Starting Card Hand:** 2× Consul, 1× Senator, 1× Legionary, 1× Diplomat (free at game start), 1× Recess

**Research Tracks:** Constitutional Precedent (starts 1) / Maritime Commerce (starts 3)

All other stats, powers, victory conditions: unchanged.

---

### FACTION: VARFELL

Carries forward from current B3 with the following additions:

**Institutional Mandate:** *"Information is the truest form of power."*
Mandate triggers: a faction conceals information Varfell has requested; Church destroys or seals a document/archive; Varfell is forced to act on incomplete intelligence.

**Starting Card Hand:** 2× Tribune (Intel), 1× Legionary, 1× Consul, 1× Colonist (free at game start), 1× Recess

**Research Tracks:** Einhir Knowledge (starts 1) / Intelligence Network (starts 2)

All other stats, powers, TK track, victory conditions: unchanged.

---

### FACTION: THE GUILDS

**Stats:** Mandate 3 · Influence 4 · Wealth 6 · Military 2 · Stability 5

**Ethical Framework: Moral Relativism** — Trade/guild autonomy actions: −1 Ob. Moral consistency across contexts: +1 Ob.

**Leader/Champion: Guildmaster Council** — No single Conviction. Deviation from prior decision: no Stability check (consensus may legitimately reverse).

**Institutional Mandate:** *"Commerce is neutral; we serve whoever can pay."*
Mandate triggers: Crown issues Royal Taxation; Church declares Interdict in Guild territory; any faction demands the Guilds take sides in a conflict.

**Contractor System:** Guilds have no Legionary (Military) cards in their hand. Zero standard military capacity. Instead:
- Each season, Guilds may issue 1 **Contract** to any other faction: pay 1–3 Wealth for that faction to execute one specific order on Guilds' behalf in a named territory.
- The contracted faction uses their own stats; the Guilds' Wealth investment gives +1D per Wealth spent.
- If the contracted faction fails or refuses: Guilds retain Wealth; relationship costs 1 Contempt.
- **Hired Blades exception:** Guilds may pay 2 Wealth at any time to place 1 Hired Blade unit (see B6) without a Muster card. Maximum 2 Hired Blades in play simultaneously.

**Starting Card Hand:** 2× Consul, 1× Aedile (Trade, free at game start), 1× Tribune (limited — Intel at +1 Ob), 1× Diplomat, 1× Recess

**Research Tracks:** Market Penetration (starts 2) / Contract Law (starts 1)

**Victory — Economic Dominance:** Deed Tokens as currently defined. No changes.

---

### FACTION: NIFLHEL

**Stats:** Influence 5 · Wealth 4 · Intel 4 · Stability 4. No Mandate, no Military.

**Ethical Framework: Amoral Consequentialism** — Covert: −1 Ob. Public: +2 Ob.

**No Champion token.** Niflhel has a **Network Coordinator card** (face-down): reveals a single-use capability once per game — the moment one arm's leadership makes a decisive move.

**Institutional Mandate:** *"Everyone serves their own interest; there is no other law."*
Mandate triggers: a faction demands Niflhel loyalty; Niflhel is forced to act publicly; an arm is compromised and Niflhel must choose between cutting it loose or exposing the network.

**Network Depth System:** Niflhel does not place territorial control markers. Instead, Niflhel tracks Network Depth (0–3) per territory.
- Network Depth gained by successful Intel or Smuggle orders in a territory (not Govern).
- Network Depth gives Niflhel: income (Wealth at depth 2+), information access, Sabotage capability.
- Niflhel "controls" Sigurdshelm for victory purposes at Network Depth ≥ 3.
- Military orders against Niflhel target Network Depth: each battle in a territory reduces Niflhel's Depth by 1 there.

**Starting Card Hand:** 3× Tribune (Intel), 1× Legionary (limited — Sabotage/Assassination only), 1× Consul (Trade/Smuggle), 1× Recess

**Research Tracks:** Network Depth (starts 2) / Operational Security (starts 2)

**Unique Power, RS passive degradation, victory conditions:** carry forward from current B3.

---

### REVOLUTION (NPC ONLY)

**No Card Hand. No Order tokens.** Revolution uses a Presence-based system.

**Institutional Mandate:** *"The community is the only legitimate political unit."*

**Presence Markers (8 total):** Placed in territories. Represent community organization, not military control.
- Each season, Revolution NPC AI moves Presence markers into adjacent territories (no order required — organic community spread).
- Revolution has two action types:
  - **Community Organizing** (rendered-world): Build non-Thread Projects, recruit, spread Presence. No Thread operation. No co-movement. No Attention Pool trigger.
  - **Community Weaving** (Thread operation): RS restoration. Requires practitioner Presence. Produces full co-movement (draw Co-Movement card). Triggers Church Attention Pool.

**Community Projects:** Revolution may start Projects in territories with Presence (see B7).

**Victory:** Revolution does not "win" in the standard sense. Revolution's success state: RS > 60 at game end AND Revolution Presence in ≥ 4 territories. This modifies other factions' hollow victory scoring.

---

## B4: ACTION ECONOMY — THE CARD-HAND SYSTEM

The Order token system is replaced by a Concordia-derived Card-Hand action economy.

### Core Concept

Each faction has a **hand** of Action Cards. Playing a card executes its action and removes it from your hand. Your hand IS your institutional capability this season. The only way to recover played cards is the **Recess** card — which costs 1 Wealth AND your entire season (no other action).

### Card Types

| Card | Action Domain | Inward Orientation | Outward Orientation |
|---|---|---|---|
| Legionary | Military | Muster (raise unit at home) | March (move unit to adjacent) |
| Consul | Domain | Govern (consolidate control) | Trade (generate Wealth) |
| Senator | Social | Decree/Parliamentary (internal policy) | Diplomacy (inter-faction negotiation) |
| Tribune | Covert | Investigate (learn own territory state) | Spy (learn enemy territory/stat) |
| Prefect | Domain (wide) | Govern ALL controlled territories at +1 Ob | Trade ALL controlled territories at +1 Ob |
| Recess | Recovery | Retrieve all played cards. No other action. Cost: 1 Wealth. |

**Orientation:** When playing a card, rotate it inward (toward home territory) or outward (toward other territories) to select sub-type. Default: Inward.

### Faction-Specific Cards

| Card | Available to | Action |
|---|---|---|
| Pontifex | Church, Revolution-affiliated | Thread operation (Community Weaving / Mend) |
| Diplomat | Hafenmark (free start) | Diplomacy at −1 Ob |
| Aedile | Guilds (free start) | Trade at −1 Ob |
| Colonist | Varfell (free start) | March + Govern in destination (combined) |
| Tribune Militum | Purchasable | Military at −1 Ob |
| Architectus | Purchasable | Fortify + Govern in same territory |
| Praetor | Purchasable | Place a Community Project marker |
| Censor | Purchasable | Crown: issue Policy. Non-Crown: block one order |

### Senate Market

6 cards face-up from the Senate Deck. At each season's Accounting, add 1 new card from the deck.

Purchase cost: 1–3 Wealth (printed on card). Purchased cards join your hand permanently.

The Senate Market is how factions develop: buying cards expands institutional capability. Other players can see what you've purchased — partial information asymmetry.

### Season Flow

Each season, a faction plays cards from hand sequentially (one per priority tier). Unplayed cards remain in hand for next season. A faction is never forced to play all cards — holding cards in reserve is strategic.

**Maximum cards played per season: 5.** Even if hand exceeds 5 cards, only 5 may be played in one season.

### Lead/Follow (Resolution Modifier)

When orders resolve, the faction with domain expertise in that card type is the **Lead** faction:
- Crown leads Military. Church leads Social. Hafenmark leads Domain. Varfell leads Intel. Guilds leads Trade. Revolution leads Thread.

Factions playing the same card type as the Lead: resolve at −1 Ob (following established institutional patterns). Factions with no card in that tier may **Opportunistically Follow** by spending 1 Mandate (reactive, unplanned action at +1 Ob).

Niflhel's actions cannot be followed (covert; no public signal).

### Cooldown Track

Each faction has a 3-slot Cooldown Track for Unique Powers and powerful abilities. After use, place the ability on slot 3. Each Accounting: all items advance 1 slot. Item exits slot 0: returns to available.

| Ability | Cooldown |
|---|---|
| Royal Decree (Crown) | 2 seasons |
| Excommunication (Church) | 3 seasons |
| Sovereign Authority (Hafenmark) | Once per game (unchanged) |
| Private Collection (Varfell) | 1 season |
| Economic Leverage (Guilds) | 1 season |
| Quiet Network: Assassination (Niflhel) | 3 seasons |
| Quiet Network: other modes (Niflhel) | 1 season |
| Champion Renown 5 abilities | 3 seasons |

---

## B5: POLITICAL SYSTEM

### Institutional Mandate (MP-34)

Each faction's Institutional Mandate is printed on the faction card. When a game event triggers a Mandate challenge (specific conditions listed per faction on the card), the controlling player must choose:

- **Uphold:** Act consistently with the Mandate, even at cost. Gain: +1 Champion Renown, +1 Stability.
- **Compromise:** Act against the Mandate for strategic advantage. Gain: the mechanical benefit of the action. Cost: +1 self-inflicted Contempt token (visible to all), −1 Stability.

In hybrid mode: the Uphold/Compromise pattern is tracked. If the PC faction leader's personal Belief arc contradicts the faction's pattern, the hollow victory condition activates.

NPC factions always Uphold unless their NPC AI tree specifies otherwise.

### Contempt Tokens (MP-22)

Contempt tokens represent accumulated political grievances between factions.

**Gaining Contempt:**
- Breaking a Deal Pledge: +1 Contempt from the betrayed faction
- Executing Brutal disposition against Valorian civilians: +1 Contempt from all factions
- Seizing territory from a faction you were previously allied with: +1 Contempt from that faction
- Church Excommunicates a faction leader: +1 Contempt from the excommunicated faction
- Niflhel operation traced to them: +1 Contempt from the targeted faction
- Self-inflicted via Mandate Compromise: +1 Contempt (no specific issuer — visible to all)

**Contempt effects:**
- Each Contempt token: −1 Reputation with the issuing faction (permanent until cleared)
- 3+ Contempt from one faction: that faction's Diplomacy orders targeting you automatically fail
- 5+ total Contempt from all sources: faction cannot form alliances or receive Deal Tokens this season

**Clearing:** 1 Contempt per season: spend 1 Wealth + 1 Influence order as public gesture.

### Deal Tokens and Pledges (MP-02)

Each faction has 3 Deal Tokens per game (refresh each year — every 4 seasons).

During Diplomacy resolution, a faction may spend a Deal Token to place a Pledge on another faction:
- **Open Pledge:** Declared publicly. Breaking costs Reputation −2 with all factions + Contempt +1. Token returns immediately.
- **Sealed Pledge:** Private commitment. Revealed at game end during scoring. If broken: costs the breaker Reputation −3 and Contempt +2.

### Crown Policy Instruments (MP-27)

Each season, Crown may issue one Policy (in addition to normal card play). Requires Mandate ≥ 4. Same Policy cannot repeat for 2 seasons.

| Policy | Effect | Downside |
|---|---|---|
| Royal Taxation | All Trade: +1 Wealth to Crown | Non-Crown Trade: +1 Ob |
| Conscription Mandate | All Muster: −1 Ob | Mustered units begin at Cohesion −1 |
| Free Trade Decree | IP −1; Schoenland Trade: +1D | TC +1 |
| Curfew | Intel/Covert in Crown territories: +2 Ob | Niflhel gains Leverage +2 |
| Parliamentary Session | All factions: 1 additional Diplomacy action | Crown Mandate check Ob 1; failure: Mandate −1 |
| Emergency Powers | Crown places 1 order face-down (revealed at resolution) | Hafenmark gains free Parliamentary Manoeuvre; TC +1 |

Any faction may oppose a Policy via Diplomacy Ob 3. Success: effect halved. Overwhelming: blocked.

### Proxy Support (MP-26)

During Diplomacy resolution, a faction may secretly designate another faction as a Proxy (pay 1–3 Wealth, sealed). The Proxy executes one order with +1D per Wealth spent. If successful, supporting faction gains 1 Influence in the target territory. Attribution: Intel vs Ob 3 reveals the support relationship. If revealed: supporting faction takes +1 Contempt from the targeted faction.

### Leverage Tokens (MP-14, defensive only)

Gained when another faction's order directly targets your faction or territory. Cap: 5 per faction. Used defensively only:

| Cost | Effect |
|---|---|
| 1 | +1D to any defensive roll this season |
| 2 | One incoming order: resolve at +1 Ob for the attacker |
| 3 | Immediate defensive order out of priority sequence |
| 5 | Nullify one order targeting your faction this season |

---

## B6: MILITARY

### Unit Types

Faction-specific naming. One unique property per unit type per faction:

| Faction | Tier 1 | Property | Tier 2 | Property |
|---|---|---|---|---|
| Crown | Royal Levy | +1D when Champion present | Royal Guard | Cannot be Routed while Almud in territory |
| Church | Parish Militia | +1 Contempt to Church per Militia lost | Knights Templar | +2D vs practitioners; immune to Co-Movement Cohesion penalties |
| Hafenmark | Ducal Marines | +1D in coastal territories | Baralta's Household | Defensive disposition always at base Ob |
| Varfell | Highland Scouts | +1D Intel in occupied territory | Mountain Infantry | Cohesion 5; −1 Ob defending in highlands |
| Guilds | Hired Blades | Deployed via Wealth (no Muster card) | — | — |
| Niflhel | Street Enforcers | Network Depth +1 after winning battle | Shadow Operators | Intel: Partial counts as Success |
| Revolution | — | (No standard units) | Community Wardens | Emerge at RS < 40; Cohesion 3; return via Community Weaving |
| Löwenritter | Iron Knights | Immune to Rout at Coup Counter < 4 | — | — |

Combat procedures, disposition table, siege clock, supply lines, annual attrition: carry forward from current B6. Formation Break health reset changed from "full" to "Resilience+3" (half health) to prevent cycling.

---

## B7: THREAD SYSTEM

### Thread Operations

All Thread operations draw a Co-Movement card (mandatory, P-01). All Thread operations in BG mode produce three-dimensional consequences via the Co-Movement deck.

Thread operations available to:
- Revolution: Community Weaving (via Presence + practitioner), Community Projects
- Any faction with TS 50+ affiliated character: Mend order
- Varfell: Private Collection (indirect)
- Niflhel: Southernmost Harvest (passive, unattributed)

Thread operation resolution tables: carry forward from current B7.

### Thread Debt (MP-12)

When a faction executes a Thread operation that works against temporal flow (Past-Pull equivalents, Foundational operations), they may reduce the Ob by 1 by incurring 1 Thread Debt token.

- Maximum 3 Thread Debt tokens in play per faction.
- At each Seasonal Accounting, unpaid Thread Debt: RS −1 per outstanding token.
- **Repayment:** Execute a Mend-equivalent action (Community Weaving at Success, or spend 2 TR). Removes the token and stops the RS bleed.
- **Substrate Scar (residual):** When Thread Debt is repaid, place a Substrate Scar marker in the territory where the debt was incurred. Scars are permanent: +1 Ob to all Thread operations in that territory; +1 baseline TR for all factions with presence there. Scars accumulate. A territory with 3+ Scars is mechanically approaching Thread Wound status.

### Church Attention Pool (MP-24)

Track: 0–10, resets at Seasonal Accounting.

**Accumulation triggers** (consequence-detection — the Church monitors rendered-world indicators, not Thread operations directly):
- Unauthorized community gathering reported in territory (triggered when Community Weaving occurs): +2
- Unexplained structural/social change in territory (triggered when any Thread operation produces a visible co-movement actual effect): +1
- Covert operations disturb Church networks (any Niflhel operation): +1
- Behavioral pattern consistent with heretical influence (any faction at TR ≥ 3): +1 per qualifying faction
- RS crosses a threshold: +1

**Threshold responses:**
| Pool | Response |
|---|---|
| 3 | Church opens 1 Heresy Investigation anywhere (free, no card required) |
| 5 | TC +1 |
| 7 | All Thread-active factions: −1D to covert/Intel orders this season |
| 10 | Church Crusade: deploy Templars anywhere without Muster |

Player-controlled Church may suppress a threshold response: Stability check Ob 1.

### Community Projects (MP-21)

A faction may start a Project in any territory with Presence or control. Projects have a Progress Track (scope-dependent).

| Project | Scope (seasons) | Effect on Completion |
|---|---|---|
| Community Weave | 3 | RS +2; creates permanent TR +1 node in territory |
| Einhir Memory Recovery | 4 | Reveals narrative hook; TK +1 to contributors; RS +1 |
| Restoration Network | 5 | Revolution gains permanent Presence in 2 adjacent territories; IP −1 |
| Fortification (any) | 3 | Fort +1 at no Wealth cost |
| Diplomatic Mission (any) | 2 | Target faction: Reputation +1; Diplomacy −1 Ob next season |

Projects advance +1 per season while faction has presence. Disruption: battle in territory = Progress −2; territory changes control = −1; Heresy Investigation opened = −1/season.

Projects near Thread Wound territories (T12, T13): advance +1 faster. At RS < 40: all Progress checks +1.

### Thread Resonance (TR)

Carries forward from current B7 with one modification:

**TR cap for non-Thread factions:** Factions without a Thread-sensitive agent in the affected territory: TR caps at 3. TR 4–5 effects available only when a Thread-sensitive character is present.

### Co-Movement Cards, RS Passive Degradation, TK Track

Carry forward from current B7.

---

## B8: CHAMPIONS (MP-25)

Each faction has a named Champion token (their faction leader as a mobile unit on the board).

**Champion Rules:**
- One Champion per faction. Occupies a territory.
- Cannot be killed (retreats when routed) but can be captured.
- Moves via March at no additional card cost (travels with units or alone).

**Champion Bonuses (base):**
- Units in Champion's territory: +1D to all rolls
- Stability checks in Champion's territory: −1 Ob
- Diplomacy by Champion: +1D

**Champion States:**
| State | Condition | Effect |
|---|---|---|
| Active | Default | Full bonuses |
| Wounded | Loses a battle in territory with units | Bonuses halved; Renown gain paused |
| Captured | Enemy takes territory while Champion is Wounded | No bonuses; held by enemy |
| Convalescing | Returned from capture | Returns to home territory; 2 seasons to recover |

**Recovery:** Govern order in Champion's territory while no enemy military present → Champion returns to Active.

**Renown (0–5):** Champions gain Renown from victories, successful rolls while present, and Mandate Upholds. Renown unlocks faction-specific abilities at levels 1, 3, and 5.

[EDITORIAL: Champion Renown ability text per faction — carries forward from bg_improvement_v3.md MP-25 table, with Niflhel using Network Coordinator card instead.]

**Conviction Invocation (MP-16):** Once per season, a Champion may invoke their Conviction for +1D to one order (stacking with Resonant Style for +3D if both aligned). Critical failure on the invocation (all dice fail, ≥ 2 showing 1): Conviction Crisis — GM/NPC AI controls one faction order next season.

**Hybrid integration:** When a Zoom-In fires in a territory with the Champion, the Champion's NPC stats are used directly in the TTRPG scene. Champion wound state persists across scales.

---

## B9: RESEARCH TRACKS (MP-30)

Each faction has 2 Research Tracks (0–5). Tracks advance via specific successful orders (1 step per qualifying Success). Breakthroughs at levels 3 and 5.

Starting values and track definitions per faction: carry forward from bg_improvement_v4.md MP-30 tables (reduced to 2 tracks per faction as specified in consolidated synthesis).

**Scale interweaving note:** Research Track advances at L3 and L5 require a specific event (not just accumulated orders). L3 Military Tradition requires winning a battle with Champion present. L3 Doctrinal Reach requires a successful Preach in a non-Church territory. This ties progression to narrative moments, not bookkeeping.

**Season Objective Tokens:** At game start, deal 3 Season Objective tokens face-down on rounds 4, 8, 12. At those rounds, flip: scoring bonus for that season. Carry forward from MP-30 token table.

---

## B10: TURN STRUCTURE

### Round Structure (Revised)

| Phase | Name | What Happens |
|---|---|---|
| 1 | Season Card | Flip top Event card. Season modifier is public. Check Mandate triggers — any faction whose Mandate is challenged must Uphold or Compromise before planning. |
| 2 | Planning | All players simultaneously select cards from hand to play this season (face-down in territory slots). Crown announces Policy (if issuing). Contracts announced (Guilds). |
| 3 | Resolution | Cards flipped. Resolve by priority: Thread → Military → Intel → Domain → Unique Powers → Policy/Parliamentary. Lead/Follow bonuses applied. |
| 4 | Attention & Response | Update Church Attention Pool. Apply threshold responses. Any faction may initiate Crisis Response. |
| 5 | Accounting | Clock movements. Stability checks. Contempt/Leverage updates. Project progress. Research Track advances. Deed Token checks. Victory/game-end checks. Senate Market refresh (+1 card). |
| 6 | Cleanup | TR resets to 0. Attention Pool resets. Cooldown Track advances. Thread Debt bleed applies. Advance round tracker. |

---

## B11: VICTORY AND ENDGAME

### Per-Faction Victory Conditions

Carry forward from current B10. No changes to faction Deed Track conditions.

### Shared Survival Condition

RS > 20, TC < 80, IP < 80 simultaneously at game-end trigger. Carries forward unchanged.

### Hollow Victory Scoring (MP-36, BG-only rule)

After standard victory checks, apply Legitimacy Modifiers:

**Reductions:**
- Each Contempt token held: −0.5 Deeds
- Institutional Mandate Compromised ≥ 3 times: −1 Deed
- RS below 20 at game end: all victories are hollow regardless of Deed count
- TC above 80: Church victory is hollow unless controlling Himmelenger + Valorsplatz
- Any faction eliminated (Stability 0): the eliminating faction: −1 Deed

**Bonuses:**
- Institutional Mandate Upheld ≥ 5 times: +1 Deed
- RS above 60 at game end: all factions +1 Deed
- Zero Contempt at game end: +0.5 Deed

The cleanest victory: zero Contempt, Mandate upheld throughout, RS above 60. This is the game's highest achievement.

### Hidden Secondary Objectives (MP-23, BG-only)

Each faction draws 1 Secondary Objective card at game start (from a shuffled pool of 12 — 2 per faction). Checked at game end. Score additional Deeds if conditions met. If shared survival fails: Secondary Objectives score 0.

Secondary Objective card text: carry forward from bg_improvement_v3.md MP-23.

**Disabled in hybrid mode** — in hybrid, PC Beliefs serve this function.

### Game-End Triggers, Endgame Events, Scoring Tiebreak

Carry forward from current B10. No changes.

---

## B12: NPC AI

Architecture carries forward from current B8. NPC AI trees require updating for the Card-Hand system (NPC factions draw from a simplified AI card deck that specifies which Action Card type to play and in which territory, replacing Order token placement).

Revolution NPC AI: revised per Presence Marker system (B3). Priority trees carry forward from current B8 with terminology updated.

[EDITORIAL: NPC AI trees need mechanical update for Card-Hand system. Architecture unchanged; card-selection logic replaces order-placement logic.]

---

## B13: HYBRID MODE INTERFACE

### Zoom-In Triggers

Carry forward from current B12. 8 trigger conditions for BG→TTRPG scene generation.

### Cascade Phase Card Effects (MP-35)

In hybrid mode, after Personal Phase scenes resolve, the following card economy effects apply:

| Personal Scene Outcome | Cascade Effect |
|---|---|
| PC achieves their Belief this season | Add 1 free card from Senate Market (no Wealth cost) |
| PC's Belief is challenged and engaged | Recess cost: 0 Wealth this season |
| PC executes successful Thread operation | Faction's Pontifex card available even if on Cooldown |
| PC fails Thread operation catastrophically | Pontifex goes on Cooldown (2 seasons) |
| PC Wounded in personal combat | Champion enters Wounded state on BG board |
| PC dies or is captured | Champion removed; no bonuses for 3 seasons |
| PC negotiates major alliance | +1 temporary Diplomat card this season |
| PC uncovers evidence against another faction | That faction's 1 hidden stat revealed this season |

### Domain Echo

Carries forward from stage11 §11.5. Personal rolls that cross scales produce automatic faction-attribute changes. Seasonal cap: ±2 per attribute per season, shared across both phases.

### Scale Interweaving

The BG generates emergent TTRPG scenes through mechanical intersection. When multiple systems converge on the same territory — a Community Project under construction, Church Attention Pool approaching threshold, a Champion present, Thread Debt ticking — the GM (or in standalone BG, the players) should recognize the narrative conditions being produced.

In hybrid mode: these intersections ARE the scene prompts. The BG doesn't need a scripted scenario engine — its mechanics produce scenarios by operating on the same board.

---

## B14: SOLO MODE (MP-06)

The player controls one faction using the standard Card-Hand system. All other factions run on NPC AI (3 cards per season per NPC faction).

**Clock Escalation:** At season 8 (Normal difficulty), all clocks gain +1 passive movement per season. Easy: no escalation. Hard: escalation at season 5. Expert: escalation at season 3 + one NPC faction targets player by priority.

**Solo Victory:** Player meets standard victory condition while shared survival holds.

**Solo Loss:** Any clock reaches game-end threshold, or player faction reaches Stability 0.

**Recommended solo factions:** Hafenmark (TC brake; defensive), Varfell (information advantage), Guilds (economic engine). Not recommended: Crown (relationship-dependent), Niflhel (passive RS degradation creates moral discomfort in solo).

---

## EDITORIAL FLAGS

| ID | Item | Blocking? |
|---|---|---|
| BG-E-30 | Confirm Card-Hand system adoption (replaces Order tokens) | Yes — structural precondition for all other changes |
| BG-E-31 | Champion Renown ability text per faction | Yes |
| BG-E-33 | Belief Intervention content per Champion (MP-32) | Yes |
| BG-E-34 | Institutional Mandate trigger conditions per faction — review proposed conditions | Yes |
| BG-E-35 | NPC AI tree update for Card-Hand system | Yes — blocks NPC faction play |
| BG-E-36 | Secondary Objective card text (12 cards) | Low |
| BG-E-37 | Co-Movement deck expansion for Thread Debt and Community Project co-movement coverage | Yes — P-14 compliance |
| BG-E-38 | Senate Market card balance and pricing | Low |
| BG-E-39 | Research Track L3/L5 event triggers per faction | Low |
| BG-E-25 | Thread Veil card content (revised — Baralta lineage card replaced) | Low |
| BG-E-26 | Niflhel Network Coordinator card content | Low |

---

## CARRY-FORWARD REGISTER

The following sections carry forward from the current stage_bg_board_game_mode.md without structural changes:

| Section | Status |
|---|---|
| B2 Territory Map (layout, adjacency, territory table) | Unchanged + clock environmental effects added |
| B6 Military (combat, disposition, siege, supply) | Unchanged except Formation Break fix and unit renaming |
| B7 Co-Movement Cards (existing 20-card deck structure) | Carry forward + expand for new Thread mechanics |
| B9 Event Deck (30-card structure, C-01–C-20, S-01–S-15) | Carry forward; integrate GT-01 cards |
| B10 Endgame Events (Rupture, Holy State, Invasion) | Unchanged |
| B11 Entity Encounters | Unchanged |

---

*Proposal complete. This document integrates 27 approved mechanics from V1–V4 synthesis into a unified BG design. All carry-forward content retains current compilation state. All new systems are canon-compliant per P-01–P-14 review (bg_improvement_review.md) with fixes applied per consolidated synthesis.*

*The next step is BG-E-30: confirm Card-Hand adoption. All other editorial flags depend on this structural decision.*
