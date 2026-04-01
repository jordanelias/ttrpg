# VALORIA: BOARD GAME MODE — REVISED PROPOSAL v2

## Date: 2026-03-31
## Status: Proposal — requires editorial review before compilation
## Supersedes: stage_bg_revised_proposal.md
## Sources: bg_synthesis.md, bg_proposal_critical_review.md, bg_synthesis_amendment_1.md, lowenritter_faction_card.md, Economy/Guilds/Trade wiki

---

## DESIGN PRINCIPLES

The board game is one of three mandatory game modes (TTRPG, Hybrid, Board Game). It is a complete standalone game that also functions as the strategic layer in hybrid play.

1. **Standalone completeness.** A 2–4 hour game with full arc, emergent narrative, and moral weight.
2. **Hybrid integration.** Clean handoffs to/from TTRPG personal-scale play. Scale interweaving, not bolted-on zoom-in.
3. **Political weight.** TC and IP generate decisions as compelling as RS. Institutional tensions drive the game.
4. **Metaphysical coherence.** Thread is the constitutive ground, not a subsystem. P-01–P-14 compliance without exception.
5. **Cognitive discipline.** Target: ≤20 core systems. Emergence comes from system *interaction*, not system *quantity*.

**The feel:** Powerful institutions trying to manage a world that is quietly dying. Every strategic decision carries identity consequences that outlast the season. Victory is possible but never clean.

**Information Layering Principle:** The board state must be legible at a glance. All information exists in one of four layers:
- **Public board:** Territories, clocks (RS/TC/IP), control markers, Champions, Parliament Integrity, Löwenritter Coup Counter, Crown Deniability Debt. What everyone sees.
- **Faction mat:** Card hand, Research Tracks, Deed Track, Standing tokens, Cooldown Track. What you hold.
- **Reference cards:** Environmental effects, resolution procedures, co-movement rules, faction-specific summaries (Church: TC-as-Currency + Inquisitors + Attention Pool thresholds). What you consult.
- **Shared ledger / companion app:** Network Depth, Attention Pool, Project progress, Thread Debt residual territory modifiers. What you track off-board.

---

## B1: OVERVIEW AND SETUP

### Player Count

| Players | Mode |
|---|---|
| 1 | Solo (see B14) |
| 2 | Competitive asymmetric; NPC AI runs remaining factions |
| 3–5 | Competitive-cooperative; NPC AI runs remainder |
| 6 | Full faction coverage (Crown, Church, Hafenmark, Varfell, Guilds, Niflhel) |
| 7 | Full coverage + Restoration Movement (optional 7th player faction) |

Schoenland is always NPC-controlled. Löwenritter is always NPC-controlled (partial sheet until coup trigger — see B3).

### Components

**Public Board**
- 1× Main board: territory map (15 territories), 3 clock tracks (RS 100→0, TC 0→100, IP 0→100), Parliament Integrity track (0–10), Löwenritter Coup Counter track (0–4), Crown Deniability Debt track (0–5), round tracker
- 15× Territory tiles with Prosperity/Fortification values
- Faction control markers, Fortification tokens, Prosperity cubes — carry forward from current B1

**Per Faction**
- 1× Faction card (stats, Institutional Mandate, ethical framework, Deed Track)
- 1× Champion token (named leader) — except Niflhel (Network Coordinator card)
- 1× Champion state card (Active/Wounded/Captured/Convalescing)
- 6× Starting Action Cards (faction-specific hand — see B4)
- 1× Recess card
- 1× Cooldown Track (3 slots)
- 2× Research Track markers
- Stat dials (faction-dependent)
- Unit tokens (faction-named types — see B6)
- 3× Deal Tokens (wooden discs in faction colour)

**Shared Components**
- 1× Co-Movement card deck (20 cards — carry forward from current B7)
- 1× Event deck (30 cards — carry forward; integrate C-11–C-20 per GT-01)
- 1× Senate Deck (18 purchasable Action Cards)
- 1× Disposition table card
- 12× Secondary Objective cards (2 per faction, shuffled; each player draws 1 at game start — BG-only)
- Thread Debt tokens (6 total)
- Standing tokens (30 total, generic — replaces Contempt + Leverage)
- Community Project markers + Progress tracks (6 markers)
- Restoration Movement Presence markers (8)
- Niflhel Network Depth markers (15, 1 per territory)

### Starting State

Clocks: RS 72. TC 15. IP 20. Parliament Integrity: 7. Church Attention Pool: 0. Löwenritter Coup Counter: 0.

Territory control, starting Prosperity, Fortification: per current B2 territory table (unchanged).

Each player-controlled faction: place Champion token in home territory. Place 1 unit in home territory. Crown receives 1 additional unit in Arnesheld.

Each faction: draw starting Action Card hand (faction-specific — see B4). Place Unique Power card on Cooldown Track slot 0 (available immediately).

---

## B2: TERRITORY MAP

Carries forward from current B2. No changes to layout, adjacency, territory table, or territory rules.

**Clock Environmental Effects:**

**RS Environmental Effects:**
| RS Range | Effect |
|---|---|
| 72–50 | No modifier |
| 49–30 | All Thread operations: −1 Ob (community urgency). All non-Thread orders in T12/T13: +1 Ob (substrate strain) |
| 29–20 | As above. Entity encounters possible in T12/T13. Muster in all territories: +1 Ob (population unsettled) |
| Below 20 | All orders in all territories: +1 Ob (the world is failing). Community Projects advance +1 per season. Entity encounters expand to territories adjacent to T12/T13 |

**TC Environmental Effects:**
| TC Range | Effect |
|---|---|
| 0–30 | No modifier |
| 31–50 | Church Preach/Inquisition: −1 Ob everywhere. Non-Church Diplomacy: +1 Ob in Church-controlled territories |
| 51–70 | As above. All factions: Govern in non-home territories +1 Ob (theocratic bureaucratic pressure) |
| 71–80 | Church orders everywhere: −1 Ob. All other factions: Social orders +1 Ob (theocratic dominance) |

**IP Environmental Effects:**
| IP Range | Effect |
|---|---|
| 0–40 | No modifier |
| 41–60 | Trade with Schoenland: +1D. Intel orders by all factions: +1D (Altonian intelligence flows both directions) |
| 61–75 | Trade with Schoenland: disrupted (+1 Ob). Military orders in T4 (Spartfell) and T15 (Schoenland): +1 Ob |
| 76+ | Altonian vanguard deploys in T15. March into T4: automatic battle. All external Trade: +2 Ob |

---

## B3: FACTION CARDS

Each faction card contains: starting stats, Institutional Mandate, ethical framework, unique power, and Deed Track.

### Structural Asymmetry

| Faction | Action System | Core Distinction |
|---|---|---|
| Crown | Standard Card-Hand + Policy Instruments | Sets conditions for all other factions |
| Church of Solmund | Standard Card-Hand + TC-as-Currency | Consumes its own victory resource to act |
| Hafenmark | Standard Card-Hand + Parliamentary Manoeuvre | Proceduralism as strategic tool |
| Varfell | Standard Card-Hand + TK Intelligence | Information as power |
| Guilds | Contractor Card-Hand (no Military cards) | Rents capability from other factions |
| Niflhel | Standard Card-Hand (no Govern) + Network Depth | Influence without territorial control |
| Restoration Movement | Community Card-Hand (no Military, no Trade) | Distributed community infrastructure |
| Löwenritter (NPC) | Partial sheet → full sheet on coup | Military coiled spring |
| Schoenland (NPC) | NPC AI — active spoiler | Profiteer of conflict |

---

### FACTION: THE CROWN

**Stats:** Mandate 5 · Influence 5 · Wealth 4 · Military 4 · Stability 4

**Ethical Framework: Virtue Ethics** — Public, visible actions: −1 Ob. Covert or morally ambiguous: +1 Ob.

**Leader/Champion: King Almud Almqvist** — Conviction: Order. Deviation cost: Stability check Ob 2.

**Institutional Mandate:** *"The monarchy provides the order that protects Valoria."*
Mandate triggers: Church Excommunication targets Crown-affiliated character; IP crosses 60; another faction controls Valorsplatz; Löwenritter Coup Counter reaches 3.

**Unique Power — Royal Decree** (Cooldown: 2 seasons)
Roll Mandate vs Ob 2. Success: one faction attribute change (any faction, ±1) takes effect immediately. Failure: Crown Mandate −1. Requires Parliament Integrity ≥ 5 for full effect; at PI 3–4: Ob reduced to 1 (Crown governs without check). At PI ≤ 2: no Ob check required (decree by fiat).

**Policy Instruments** (Crown exclusive — see B5)

**Riskbreakers** (Crown/Löwenritter covert capability — Act Consequentialism):
The extralegal arm of the Löwenritter, operated as Crown's deniable instrument. Deploy via Tribune card (Intel). Riskbreaker operations use Act Consequentialism (not Crown's Virtue Ethics — they are Löwenritter assets operating outside Crown's institutional identity): resolve at −1 Ob but incur **Deniability Debt** (0–5, tracked on shared ledger):
- Each Riskbreaker operation: Debt +1
- Debt 3: Crown Domain actions against non-Crown factions +1 Ob (parliamentary trust erodes). PI −1.
- Debt 5: Parliamentary inquiry opens. PI −2. Crown must spend 1 season on Diplomacy to resolve or accept permanent PI reduction.
- Key capability: can expose Church-Niflhel connection (counter-play against Church territorial seizure). Each successful exposure removes one seized territory and prevents re-seizure for one season.

**Starting Card Hand:** 2× Legionary, 1× Consul, 1× Senator, 1× Prefect, 1× Recess

**Research Tracks:** Mandate Authority (starts 2) / Military Tradition (starts 1)

**Victory — Constitutional Stability:** Deed Tokens as currently defined.

---

### FACTION: THE CHURCH OF SOLMUND

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

**Inquisitors:** Church deploys Inquisitors via Inquisition card play (Senator card, Outward orientation). One Inquisitor may be active per territory. While deployed: +2 Attention Pool per season in that territory. Inquisitors may open Heresy Investigations without additional card play. Moving an Inquisitor to a new territory requires a Senator card. Inquisitors are not combat units — they withdraw if the territory is attacked. Inquisitors are the instrument of the Cardinal of Justice.

**The Four Cardinals** (Church officer corps — each oversees a doctrinal/operational arm):
| Cardinal | Virtue | Portfolio | BG Relevance |
|---|---|---|---|
| Osten Jarnstal | Fortitude | Knights Templar | Templar deployment goes through Jarnstal. Drifting toward independence — at Church Stability ≤ 3, Jarnstal may refuse Confessor's Templar orders (Stability check Ob 2; failure: Templars unavailable this season). |
| Arnlod Olafsson | Justice | Inquisitors, Grand Adjudicator | Active Niflhel connection (vulnerability). If exposed via Riskbreaker or Intel operation: Church loses Inquisitor capability for 1 season; Church Stability −1; TC −2. |
| Magnus Klapp | Temperance | Scholarly institutions, monasteries, universities | TS 31 (approaching Stirring). If triggered by Thread-significant event: Church gains unexpected Thread intelligence (+1 TK) BUT Church Stability −1 (institutional crisis). Hybrid zoom-in trigger. |
| [EDITORIAL: BG-E-46] | Prudence | Tithes, charities | Church Wealth generation (Consul/Trade card). Charities provide +1D to Church Diplomacy in territories with Church Presence. |

**Internal Church tension:** At Church Stability ≤ 4, TC generation pauses (Cardinals competing — canon per stage6_factions.md). At Stability ≤ 3: one Cardinal may challenge the Confessor's authority (NPC AI selects based on highest-pressure conditions). This can produce internal schism — a Cardinal acting independently of the Confessor for one season.

**Unique Power — Excommunication** (Cooldown: 3 seasons)
Roll: Mandate vs target leader's Mandate. Outcomes as currently defined.

**Starting Card Hand:** 2× Senator, 1× Pontifex (free at game start), 1× Consul, 1× Legionary, 1× Recess

**Research Tracks:** Doctrinal Reach (starts 2) / Inquisition Network (starts 2)

**Victory — The Holy State:** Deed Tokens as currently defined.

---

### FACTION: HAFENMARK

Carries forward from current B3 with the following additions:

**Institutional Mandate:** *"Constitutional process is the only legitimate source of authority."*
Mandate triggers: Crown issues Emergency Powers policy; Church Excommunicates without Grand Debate; any faction seizes territory by force without prior Diplomacy attempt.

**Parliamentary Manoeuvre:** Available when Parliament Integrity ≥ 5. At PI 3–4: +1 Ob. At PI ≤ 2: unavailable (Parliament non-functional).

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

**Leader/Champion: Guildmaster Council** — No single Conviction. Deviation from prior decision: no Stability check.

**Institutional Mandate:** *"Commerce is neutral; we serve whoever can pay."*
Mandate triggers: Crown issues Royal Taxation; Church declares Interdict in Guild territory; any faction demands the Guilds take sides in a conflict.

**Contractor System:** Guilds have no Legionary (Military) cards. Instead:
- Each season, Guilds may issue 1 **Contract** to any other faction: pay 1–3 Wealth for that faction to execute one specific order on Guilds' behalf in a named territory. +1D per Wealth spent. If contracted faction fails or refuses: Guilds retain Wealth; +1 Standing against that faction.
- **Hired Blades exception:** Guilds may pay 2 Wealth at any time to place 1 Hired Blade unit. Maximum 2 simultaneously. Hired Blades: attack-only (cannot defend or garrison), removed at end of season regardless of combat status, cannot hold territory.

**Guild Forum Integration:** The Guilds' economic operations are monitored by the Ministry of Guilds (setting canon). Mechanically: Guilds' Trade orders in a territory generate +1 Wealth if that territory has Prosperity ≥ 3 (guild infrastructure adds value). Guilds may spend 1 Wealth to invoke a Guild Forum resolution: modifies a target faction's Trade order in the same territory at +1 Ob (non-competition enforcement). Declared during Negotiation window (Phase 2); applied when the targeted Trade order resolves (Phase 3, Domain tier).

**Starting Card Hand:** 2× Consul, 1× Aedile (Trade, free at game start), 1× Tribune (limited — Intel at +1 Ob), 1× Diplomat, 1× Recess

**Research Tracks:** Market Penetration (starts 2) / Contract Law (starts 1)

**Victory — Economic Dominance:** Deed Tokens as currently defined.

---

### FACTION: NIFLHEL

**Stats:** Influence 5 · Wealth 4 · Intel 4 · Stability 4. No Mandate, no Military.

**Ethical Framework: Amoral Consequentialism** — Covert: −1 Ob. Public: +2 Ob.

**No Champion token.** Niflhel has a **Network Coordinator card** (face-down): reveals a single-use capability once per game.

**Institutional Mandate:** *"Everyone serves their own interest; there is no other law."*
Mandate triggers: a faction demands Niflhel loyalty; Niflhel is forced to act publicly; an arm is compromised and Niflhel must choose between cutting it loose or exposing the network.

**Network Depth System:** Niflhel tracks Network Depth (0–3) per territory on the shared ledger (not the public board).
- Gained by successful Intel or Smuggle orders (not Govern).
- Depth 2+: income (Wealth). Depth 3: Sabotage capability. Depth 3 in Sigurdshelm: controls for victory.
- Military orders against Niflhel reduce Depth by 1 per battle.

**Design note (Niflhel play experience):** Niflhel's hand is 50% Intel cards (3× Tribune). This is appropriate for identity but means Niflhel plays a fundamentally different, information-heavy game. Over 12+ seasons, ensure Niflhel has meaningful decisions each season — Network Depth placement is the strategic layer; Intel results are the tactical payoff.

**Starting Card Hand:** 3× Tribune (Intel), 1× Legionary (limited — Sabotage/Assassination only), 1× Consul (Trade/Smuggle), 1× Recess

**Research Tracks:** Network Depth (starts 2) / Operational Security (starts 2)

**Unique Power, RS passive degradation, victory conditions:** carry forward from current B3.

---

### FACTION: RESTORATION MOVEMENT (Optionally Playable)

**When NPC-controlled:** operates on NPC AI priority trees (see B12). Uses simplified card draws from AI deck.

**When player-controlled (7th player):**

**Stats:** No Mandate. Influence 3 · Wealth 2 · Military 1 · Stability 5

**Ethical Framework: Rawlsian Social Justice** — Community-building actions: −1 Ob. Power-concentrating actions: +2 Ob.

**Leader/Champion:** [EDITORIAL: BG-E-45 — Name and characterize Restoration Movement leader. Must be a community organizer figure, not a military commander or political leader.]

**Institutional Mandate:** *"The community is the only legitimate political unit."*
Mandate triggers: a faction offers the Restoration institutional power (seat on council, territory governorship); Church Inquisition targets Restoration Presence; Crown or Hafenmark attempt to co-opt the movement into formal politics.

**Presence Markers (8 total):** Placed in territories. Represent community organization, not military control.
- Each season, Restoration may spread Presence to 1 adjacent territory via Senator card (Social organizing).
- Two distinct action modes:
  - **Community Organizing** (Praetor card): Build non-Thread Projects, recruit, spread Presence. No Thread operation. No co-movement. No Attention Pool trigger.
  - **Community Weaving** (Pontifex card): RS restoration. Requires practitioner Presence. Produces full co-movement (draw Co-Movement card). Triggers Church Attention Pool.

**Community Projects:** Restoration may start Projects in territories with Presence (see B7).

**Starting Card Hand:** 1× Pontifex, 2× Praetor (Community Projects), 1× Senator, 1× Tribune (Intel — staying hidden from Church), 1× Recess

**No Legionary, no Consul.** Restoration cannot wage institutional war or trade at institutional scale. Community Wardens (defensive only, Cohesion 3) emerge at RS < 40 — 1 per Presence marker.

**Wealth income:** Restoration has no Trade actions. Wealth is generated from: completed Community Projects (+1 Wealth per project completed); Presence in territories with Prosperity ≥ 3 (+1 Wealth per such territory at Accounting, representing community economic support).

**Research Tracks:** Community Resilience (starts 1) / Thread Practice (starts 1)

**Victory:** RS > 60 at game end AND Presence in ≥ 4 territories AND ≥ 2 Community Projects completed.

---

### FACTION: THE LÖWENRITTER (NPC — Partial Sheet)

**Ethical Framework: Deontological Honor Code** — Defense of Valorian sovereignty: −1 Ob. Serving foreign interests: +2 Ob.

**Leader: Grandmaster Sigrid Ehrenwall** — Conviction: Duty. The most dangerous NPC: patient, competent, commanding an army.

**Institutional Mandate:** *"The military order serves the Crown as institution, not the monarch."*

**Partial Sheet (Peacetime):** Military 5 · Stability 5 · Influence 3 · Intel 3. No Mandate, no Wealth (funded by Crown).

**Peacetime Card Hand (NPC AI):** 1× Legionary (garrison), 1× Tribune (Intel), 1× Martial Law (Unique), 1× Recess. The Löwenritter should feel like a coiled spring — limited actions until the moment they act, then decisive.

**Coup Counter (0–4):** Tracked on shared ledger. Advances +1 when any of these conditions are met:
1. Crown is deposed or no legitimate successor installed
2. Foreign power controls or captures the heir (Torben sent to Altonia)
3. TC reaches 80 (Church controls Crown-held territories)
4. Crown formally subordinates to a foreign power

**Full Sheet Trigger — Military Coup:** When Coup Counter reaches 4, Löwenritter declares institutional independence.
- Roll Military vs Ob 3.
- Success: Löwenritter gains full 6-attribute sheet (Mandate 3, Wealth 2 — seized from Crown). Crown: Wealth −2, Stability −2. All factions: +1 Standing against Löwenritter (coup is destabilizing). Parliament Integrity −3.
- Failure: Löwenritter Stability −2. Grandmaster removed — officer succession. Crown may purge (Military −1).
- Post-coup card hand expands: 2× Legionary, 1× Consul, 1× Tribune, 1× Martial Law, 1× Recess.

**Unique Power — Martial Law** (Cooldown: 2 seasons)
Roll Military vs Ob 3 in a territory with Löwenritter military presence. Success: all other factions' Domain Actions +1 Ob in that territory for 1 season. Crown Mandate +1 (order restored). Cannot be used where Church Mandate exceeds Crown Mandate.

**Three-way endgame interaction:** Church territorial seizure at TC 80 + Löwenritter coup = three-way endgame (Crown collapse, Church theocracy, military junta).

---

### SCHOENLAND (NPC — Active Spoiler)

Schoenland occupies T15. Not playable. Schoenland's NPC AI actively destabilizes to profit from conflict (canon: major merchant republic, benefits from sustained feuding, pro-war via arms sales, anti-conquest).

**Schoenland NPC AI Behavior:**
| Condition | Action |
|---|---|
| IP ≥ 30 | Fund proxy operations: +1D to any faction's military actions at Border Pass (Schoenland sells arms to whoever is fighting) |
| TC ≥ 50 | Provide intelligence to anti-Church factions: +1D to Intel orders targeting Church (Schoenland profits from secular trade) |
| RS < 40 | No action (Schoenland doesn't understand Thread substrate) |
| No faction in active conflict for 1+ seasons | IP +1 (Schoenland funds border provocations to maintain the arms market) |

**Trade:** Schoenland's east-west trade position (canon: cottons, linens, silks from the west; art, carpets, jewelry, spices from Altonia via reopened trade line in 97 AS). Guilds' Trade orders involving Schoenland generate +1 Wealth (Schoenland's processing monopoly on silks and cloths). At IP ≥ 75: Schoenland trade suspended (Altonian military presence disrupts maritime routes).

Schoenland should feel like a profiteer that benefits from everyone else's misery — a constant background pressure that makes peace unprofitable.

---

## B4: ACTION ECONOMY — THE CARD-HAND SYSTEM

The Order token system is replaced by a Concordia-derived Card-Hand action economy.

### Core Concept

Each faction has a **hand** of Action Cards. Playing a card executes its action and removes it from hand. Your hand IS your institutional capability. The only way to recover played cards: **Recess** — costs 1 Wealth AND your entire season.

### Card Types

| Card | Action Domain | Inward Orientation | Outward Orientation |
|---|---|---|---|
| Legionary | Military | Muster (raise unit at home) | March (move unit to adjacent) |
| Consul | Domain | Govern (consolidate control) | Trade (generate Wealth) |
| Senator | Social | Decree/Parliamentary (internal policy) | Diplomacy (inter-faction negotiation) |
| Tribune | Covert | Investigate (learn own territory state) | Spy (learn enemy territory/stat) |
| Prefect | Domain (wide) | Govern ALL controlled territories at +1 Ob | Trade ALL controlled territories at +1 Ob |
| Recess | Recovery | Retrieve all played cards. No other action. Cost: 1 Wealth. |

**Orientation:** When playing a card, rotate inward or outward to select sub-type.

### Faction-Specific Cards

| Card | Available to | Action |
|---|---|---|
| Pontifex | Church, Restoration Movement | Thread operation (Community Weaving / Mend) |
| Diplomat | Hafenmark (free start) | Diplomacy at −1 Ob |
| Aedile | Guilds (free start) | Trade at −1 Ob |
| Colonist | Varfell (free start) | March + Govern in destination (combined) |
| Praetor | Restoration (free start), Purchasable | Place/advance a Community Project marker |
| Tribune Militum | Purchasable | Military at −1 Ob |
| Architectus | Purchasable | Fortify + Govern in same territory |
| Censor | Purchasable | Crown: issue Policy. Non-Crown: block one order |

### Senate Market

6 cards face-up from the Senate Deck. At each season's Accounting: +1 new card from deck.

Purchase cost: 1–3 Wealth (printed on card). Purchased cards join hand permanently. Other players see what you've purchased.

### Domain Expertise Bonus

Each faction has domain expertise in one card type. When playing that card type: +1D to resolution. This is a flat bonus, not a response mechanic.

| Faction | Expertise |
|---|---|
| Crown | Military (Legionary) |
| Church | Social (Senator) |
| Hafenmark | Domain (Consul/Prefect) |
| Varfell | Covert (Tribune) |
| Guilds | Trade (Consul, Outward) |
| Restoration Movement | Thread (Pontifex) |
| Niflhel | Covert (Tribune) — Niflhel's actions cannot be observed by other factions |

### Season Flow

Each season, a faction plays cards from hand sequentially (one per priority tier). Unplayed cards remain for next season. **Maximum cards played per season: 5.**

### Cooldown Track

3-slot track for Unique Powers. After use: place on slot 3. Each Accounting: advance 1 slot. Exits slot 0: returns to available.

| Ability | Cooldown |
|---|---|
| Royal Decree (Crown) | 2 seasons |
| Excommunication (Church) | 3 seasons |
| Sovereign Authority (Hafenmark) | Once per game |
| Private Collection (Varfell) | 1 season |
| Economic Leverage (Guilds) | 1 season |
| Quiet Network: Assassination (Niflhel) | 3 seasons |
| Quiet Network: other modes (Niflhel) | 1 season |
| Martial Law (Löwenritter) | 2 seasons |
| Champion Renown 5 abilities | 3 seasons |

---

## B5: POLITICAL SYSTEM

### Institutional Mandate (MP-34)

Each faction's Institutional Mandate is printed on the faction card. When a game event triggers a Mandate challenge, the controlling player must choose:

- **Uphold:** Act consistently with the Mandate, even at cost. Gain: +1 Champion Renown, +1 Stability.
- **Compromise:** Act against the Mandate for strategic advantage. Gain: the mechanical benefit. Cost: +1 Standing against self (visible to all — counts toward Standing thresholds for victory scoring and alliance restrictions, but does not give other factions defensive bonuses), −1 Stability.

NPC factions always Uphold unless NPC AI specifies otherwise.

### Standing Tokens (replaces Contempt + Leverage)

Standing tokens represent accumulated political grievances between factions. Directional: placed by the aggrieved faction against the offending faction.

**Gaining Standing (against another faction):**
- Breaking a Deal Pledge: +2 Standing from the betrayed faction
- Brutal disposition against Valorian civilians: +1 Standing from all factions
- Seizing territory from an allied faction: +1 Standing from that faction
- Church Excommunicates a faction leader: +1 Standing from the excommunicated faction
- Niflhel operation traced: +1 Standing from the targeted faction
- Mandate Compromise: +1 Standing against self (no specific issuer)
- Contract refusal (Guilds): +1 Standing from Guilds

**Standing effects:**
- Each Standing token against a faction: that faction gains +1D to defensive rolls against the holder (moral high ground — replaces Leverage)
- 3+ Standing from one faction: that faction's Diplomacy targeting you automatically fails
- 5+ total Standing from all sources: faction cannot form alliances or receive Deal Tokens this season

**Clearing:** 1 Standing per season: spend 1 Wealth + 1 Influence order as public gesture.

**Victory scoring:** Standing tokens against you at game end: 3+ tokens = −1 Deed; 6+ tokens = −2 Deeds. Zero Standing against you at game end: +1 Deed.

### Deal Tokens and Pledges (MP-02)

Each faction has 3 Deal Tokens per game (refresh each year — every 4 seasons).

- **Open Pledge:** Declared publicly. Breaking: −2 Standing with all factions + Reputation cost. Token returns immediately.
- **Sealed Pledge:** Private. Revealed at game end during scoring. If broken: −3 Standing, +2 Standing from betrayed faction.

### Crown Policy Instruments (MP-27)

Each season, Crown may issue one Policy (in addition to normal card play). Requires Mandate ≥ 4. Same Policy cannot repeat for 2 seasons.

| Policy | Effect | Downside |
|---|---|---|
| Royal Taxation | All Trade: +1 Wealth to Crown | Non-Crown Trade: +1 Ob |
| Conscription Mandate | All Muster: −1 Ob | Mustered units begin at Cohesion −1 |
| Free Trade Decree | IP −1; Schoenland Trade: +1D | TC +1 |
| Curfew | Intel/Covert in Crown territories: +2 Ob | Niflhel gains +2D to next Intel |
| Parliamentary Session | All factions: 1 additional Diplomacy action. PI +1. | Crown Mandate check Ob 1; failure: Mandate −1 |
| Emergency Powers | Crown places 1 order face-down (revealed at resolution) | Hafenmark gains free Parliamentary Manoeuvre; TC +1; PI −1 |

Any faction may oppose a Policy via Diplomacy Ob 3. Success: effect halved. Overwhelming: blocked.

**Resolution order:** Policy → Opposition → Censor (if in play). This order is fixed and printed on the reference card.

### Parliament Integrity (0–10)

Shared institution track. Starts at 7. Printed on public board.

**Effects by level:**
| PI | State |
|---|---|
| ≥ 5 | Parliamentary Manoeuvres available to Hafenmark. Royal Decree requires Mandate ≥ 4. |
| 3–4 | Parliamentary Manoeuvres at +1 Ob. Royal Decree Ob reduced to 1. |
| ≤ 2 | Parliament non-functional. Hafenmark loses Parliamentary Manoeuvre. Crown governs by decree (no Ob). TC +2 (Church fills governance vacuum). |

**PI degrades when:** Crown issues Emergency Powers (−1); Church territorial seizure occurs (−1); Löwenritter coup fires (−3).

**PI recovers when:** Hafenmark plays Parliamentary Manoeuvre successfully (+1); Crown issues Parliamentary Session policy (+1).

The Royal Court (Valorsplatz special property) is the physical location where Decree and Parliamentary actions gain their bonuses — not a separate institution.

### Cascade Depth Cap

**Rule: No single action may trigger more than 3 downstream mechanical effects in a single resolution.** Additional triggered effects are deferred to next season's Accounting (Phase 6). **State-based modifiers** (RS/TC/IP environmental effects, PI threshold effects, and similar always-on conditions) apply immediately when their track value changes and do not count against the cascade cap — they are properties of the game state, not triggered chains. Print on reference card.

---

## B6: MILITARY

### Unit Types

Faction-specific naming. One unique property per unit type per faction:

| Faction | Tier 1 | Property | Tier 2 | Property |
|---|---|---|---|---|
| Crown | Royal Levy | +1D when Champion present | Royal Guard | Cannot be Routed while Almud in territory |
| Church | Parish Militia | +1 Standing against Church per Militia lost | Knights Templar | +2D vs practitioners; immune to Co-Movement Cohesion penalties |
| Church | Inquisitor | Non-combat; +2 Attention Pool/season; opens Heresy Investigations | — | — |
| Hafenmark | Ducal Marines | +1D in coastal territories | Baralta's Household | Defensive disposition always at base Ob |
| Varfell | Highland Scouts | +1D Intel in occupied territory | Mountain Infantry | Cohesion 5; −1 Ob defending in highlands |
| Guilds | Hired Blades | Via Wealth (no Muster); attack-only; removed at end of season | — | — |
| Niflhel | Street Enforcers | Network Depth +1 after winning battle | Shadow Operators | Intel: Partial counts as Success |
| Restoration | Community Wardens | Emerge at RS < 40; Cohesion 3; defensive only | — | — |
| Löwenritter | Iron Knights | Immune to Rout at Coup Counter < 4; Cohesion 5 | — | — |
| Crown (covert) | Riskbreakers | Deploy via Tribune; Intel at −1 Ob; +1 Deniability Debt per operation | — | — |

Combat procedures, disposition table, siege clock, supply lines, annual attrition: carry forward from current B6. Formation Break health reset: Resilience+3 (half health) to prevent cycling.

---

## B7: THREAD SYSTEM

### Thread Operations

All Thread operations draw a Co-Movement card (mandatory, P-01). All Thread operations produce three-dimensional consequences via the Co-Movement deck.

Thread operations available to:
- Restoration Movement: Community Weaving (via Presence + practitioner), Community Projects
- Any faction with TS 50+ affiliated character: Mend order
- Varfell: Private Collection (indirect)
- Niflhel: Southernmost Harvest (passive, unattributed)

Thread operation resolution tables: carry forward from current B7.

### Thread Debt (MP-12)

When a faction executes a Thread operation that works against temporal flow, they may reduce Ob by 1 by incurring 1 Thread Debt token.

- Maximum 3 Thread Debt tokens per faction.
- Each Seasonal Accounting: RS −1 per outstanding token.
- **Repayment:** Community Weaving at Success, or spend 2 TR. Removes the token.
- **Residual:** When Thread Debt is repaid, the territory where debt was incurred gains a permanent +1 Ob to Thread operations (tracked on shared ledger). This accumulates.

*Substrate Scar markers (the full visual marker system) are deferred to advanced/campaign rules.*

### Church Attention Pool (MP-24)

Track: 0–10 on shared ledger. Resets at Seasonal Accounting.

**Accumulation triggers:**
- Community Weaving occurs: +2
- Any Thread operation produces visible co-movement effect: +1
- Any Niflhel operation: +1
- Any faction at TR ≥ 3: +1 per qualifying faction
- RS crosses a threshold: +1
- Inquisitor present in territory where Thread activity occurs: +2 (additional)

**Threshold responses:**
| Pool | Response |
|---|---|
| 3 | Church opens 1 Heresy Investigation anywhere (free, no card) |
| 5 | TC +1 |
| 7 | All Thread-active factions: −1D to covert/Intel this season |
| 10 | Church Crusade: deploy Templars anywhere without Muster |

Player-controlled Church may suppress a threshold response: Stability check Ob 1.

### Community Projects (MP-21)

A faction may start a Project in any territory with Presence or control.

| Project | Scope (seasons) | Effect on Completion |
|---|---|---|
| Community Weave | 3 | RS +2; permanent +1 TR node in territory |
| Einhir Memory Recovery | 4 | Reveals narrative hook; TK +1; RS +1 |
| Restoration Network | 5 | Restoration gains permanent Presence in 2 adjacent territories; IP −1 |
| Fortification | 3 | Fort +1 at no Wealth cost |
| Diplomatic Mission | 2 | Target faction: +1 Standing cleared; Diplomacy −1 Ob next season |

Projects advance +1/season while faction has presence. Disruption: battle = Progress −2; territory changes control = −1; Heresy Investigation = −1/season.

### Southernmost Expedition

The Southernmost (beyond T12/T13) is a multi-season expedition target — the locus of the original Einhir catastrophe and the endgame Thread repair path.

**The Forgetting (P-13):** The Southernmost is protected by a rendering failure. Non-Thread-sensitive beings who approach forget their purpose and turn back. This is not a magical barrier — it is a property of the damaged substrate. Memory of intent does not persist in the affected zone.

**BG Prerequisites:**
- RS < 40 (the Southernmost is significant only when the substrate is visibly degrading)
- Faction unit + Thread-sensitive character in T13 (Askeheim). Without Thread sensitivity (TS 30+ in TTRPG terms; in BG: faction must have a practitioner-affiliated unit or the Restoration Movement must have Presence in T13), the expedition automatically fails — The Forgetting turns them back.
- 3 Wealth investment

**Expedition as Project (scope 4):** Each completed season advances toward Thread repair. Entity encounters each season (tier escalates with depth — tracked on shared ledger).

**Completion:** Permanent RS +5. Southernmost stabilized. In hybrid mode: generates 4–5 TTRPG scenes spontaneously.

**Southernmost Council:** Non-faction entity. Levinas-based Husserlian pragmatism. Provides Thread information and support but does not pursue political goals. The most knowledgeable Thread practitioners alive and structurally uninterested in power. Contact requires reaching the Core zone (Season 3+ of expedition).

### Thread Resonance (TR)

Carries forward from current B7. TR cap for non-Thread factions: TR caps at 3 without Thread-sensitive character present. TR 4–5 requires Thread-sensitive presence.

### Co-Movement Cards, RS Passive Degradation, TK Track

Carry forward from current B7.

---

## B8: CHAMPIONS (MP-25)

Each faction has a named Champion token (faction leader as mobile unit).

**Champion Rules:**
- One per faction. Occupies a territory. Cannot be killed (retreats when routed) but can be captured.
- Moves via March at no additional card cost.

**Champion Bonuses (static in BG):**
- Units in Champion's territory: +1D to all rolls
- Stability checks in Champion's territory: −1 Ob
- Diplomacy by Champion: +1D

**Champion States:**
| State | Condition | Effect |
|---|---|---|
| Active | Default | Full bonuses |
| Wounded | Loses a battle in territory with units | Bonuses halved; Renown gain paused |
| Captured | Enemy takes territory while Wounded | No bonuses; held by enemy |
| Convalescing | Returned from capture | Returns home; 2 seasons to recover |

**Recovery:** Govern order in Champion's territory, no enemy present → returns to Active.

**Renown (0–5):** Gained from victories, successful rolls while present, Mandate Upholds. Unlocks faction-specific abilities at 1, 3, 5.

*Conviction Invocation (MP-16) is available in hybrid mode only. In standalone BG, Champions provide static bonuses. This reduces cognitive load without sacrificing hybrid depth.*

[EDITORIAL: BG-E-31 — Champion Renown ability text per faction. Carries forward.]

**Hybrid integration:** Champion NPC stats persist across scales. Wound state carries into TTRPG zoom-in. Conviction Invocation available in hybrid: once per season, +1D to one order (stacking with ethical framework for +3D if aligned). Critical failure (all dice fail, ≥2 showing 1): Conviction Crisis.

---

## B9: RESEARCH TRACKS (MP-30)

Each faction has 2 Research Tracks (0–5). Advance via specific successful orders (1 step per qualifying Success). Breakthroughs at levels 3 and 5.

Starting values and track definitions per faction: carry forward from bg_improvement_v4.md (reduced to 2 tracks per faction).

**Scale interweaving note:** L3 and L5 advances require a specific event, not accumulated orders. L3 Military Tradition requires winning a battle with Champion present. L3 Doctrinal Reach requires successful Preach in a non-Church territory.

*Season Objective Tokens are cut. Research Tracks already provide mid-game scoring variation.*

---

## B10: TURN STRUCTURE

### Round Structure

| Phase | Name | What Happens |
|---|---|---|
| 1 | Season Card | Flip Event card. Check Mandate triggers — challenged factions must Uphold or Compromise before planning. |
| 2 | Negotiation & Planning | **Negotiation window:** Guilds may propose Contracts; any faction may discuss Deal Tokens. Then all players simultaneously select cards from hand (face-down). Crown announces Policy. |
| 3 | Resolution | Cards flipped. Resolve by priority: Thread (Pontifex) → Military (Legionary) → Intel (Tribune) → Domain (Consul/Prefect) → Social (Senator) → Unique Powers → Policy/Parliamentary. Domain expertise +1D applied. Schoenland modifiers (arms sales, intel support) are ongoing conditions applied during this phase when relevant. |
| 4 | Attention & Response | Update Attention Pool. Apply threshold responses. Crisis Response available. Check Coup Counter advancement. |
| 5 | Accounting | Resolve in order: (1) Clock movements + Schoenland NPC AI IP manipulation, (2) PI changes, (3) Stability checks, (4) Standing changes, (5) Project progress, (6) Research Track advances, (7) Restoration Wealth income, (8) Thread Debt bleed (RS −1 per token), (9) Deed Token checks, (10) Victory/game-end check, (11) Senate Market refresh (+1 card). |
| 6 | Cleanup | TR resets to 0. Attention Pool resets. Cooldown Track advances. Deferred cascade effects resolve. Advance round tracker. |

---

## B11: VICTORY AND ENDGAME

### Per-Faction Victory Conditions

Carry forward from current B10. No changes to faction Deed Track conditions.

### Shared Survival Condition

RS > 20, TC < 80, IP < 80 simultaneously at game-end trigger.

### Hollow Victory Scoring (OPTIONAL — experienced players; print on reference card)

After standard victory checks, apply Legitimacy Modifiers:

**Reductions:**
- Standing tokens against you ≥ 3: −1 Deed
- Standing tokens against you ≥ 6: −2 Deeds
- Institutional Mandate Compromised ≥ 3 times: −1 Deed
- RS below 20 at game end: all victories are hollow regardless of Deed count
- TC above 80: Church victory is hollow unless controlling Himmelenger + Valorsplatz
- Any faction eliminated (Stability 0): the eliminating faction −1 Deed

**Bonuses:**
- Institutional Mandate Upheld ≥ 5 times: +1 Deed
- RS above 60 at game end: all factions +1 Deed
- Zero Standing against you at game end: +1 Deed

### Hidden Secondary Objectives (MP-23, BG-only)

Each faction draws 1 Secondary Objective card at game start (from pool of 12). Checked at game end. If shared survival fails: objectives score 0.

**Disabled in hybrid mode** — PC Beliefs serve this function.

### Game-End Triggers, Endgame Events, Scoring Tiebreak

Carry forward from current B10.

---

## B12: NPC AI

### Architecture

NPC AI trees carry forward from current B8. Updated for Card-Hand: NPC factions draw from simplified AI card deck specifying card type and target territory.

[EDITORIAL: BG-E-35 — NPC AI trees need mechanical update for Card-Hand system.]

### Restoration Movement NPC AI

When NPC-controlled (no 7th player), Restoration draws 3 cards per season from AI deck. Priority:
1. If RS < 40: Community Weaving in territory with highest Presence (Pontifex)
2. If Attention Pool ≥ 5: spread Presence to territory without Church control (Senator)
3. If Community Project in progress: advance Project (Praetor)
4. Default: Community Organizing in territory with lowest Presence (Praetor)

**Organizing/Weaving distinction for NPC:** NPC Restoration uses Community Weaving only when RS < 40 (clear environmental signal). Above RS 40: always Community Organizing (no Attention Pool trigger, no co-movement). This simplifies the judgment call to a single threshold check.

### Löwenritter NPC AI

Peacetime: Löwenritter follows Crown orders. 2 cards per season from AI deck.
1. If Crown issues Military order in border territory: Löwenritter Legionary follows (garrison support)
2. If IP ≥ 60: Löwenritter deploys Intel (Tribune) toward Altonian border
3. Default: Recess (the coiled spring waits)

Coup Counter checked at Phase 4. On reaching 4: Löwenritter AI immediately attempts coup (see B3).

Post-coup: Löwenritter AI becomes aggressive — 4 cards per season, prioritizes Martial Law and territorial control.

### Schoenland NPC AI

Schoenland acts at Accounting (Phase 5). No card hand — behavior is automatic:
- If IP ≥ 30: +1D to any faction's military actions at Border Pass (arms sales)
- If TC ≥ 50: +1D to anti-Church factions' Intel orders (secular trade interest)
- If no faction in active conflict for 1+ seasons: IP +1 (border provocations)
- If IP ≥ 75: Schoenland trade suspended (Altonian disruption)
- RS < 40: no Schoenland action (doesn't understand Thread)

---

## B13: HYBRID MODE INTERFACE

### Zoom-In Triggers

Carry forward from current B12 (8 trigger conditions) + 5 additional:
- Löwenritter coup fires
- Inquisitor arrives in a territory with PC presence
- Schoenland diplomatic contact (IP ≥ 30, any faction attempts negotiation)
- Cardinal Klapp's TS triggers (Thread-significant event in territory with Church scholarly presence)
- Riskbreaker operation exposes Cardinal Olafsson's Niflhel connection

### Cascade Phase Card Effects (MP-35)

In hybrid mode, after Personal Phase scenes resolve:

| Personal Scene Outcome | Cascade Effect |
|---|---|
| PC achieves their Belief this season | Add 1 free card from Senate Market (no Wealth cost) |
| PC's Belief is challenged and engaged | Recess cost: 0 Wealth this season |
| PC executes successful Thread operation | Faction's Pontifex available even if on Cooldown |
| PC fails Thread operation catastrophically | Pontifex goes on Cooldown (2 seasons) |
| PC Wounded in personal combat | Champion enters Wounded state on BG board |
| PC dies or is captured | Champion removed; no bonuses for 3 seasons |
| PC negotiates major alliance | +1 temporary Diplomat card this season |
| PC uncovers evidence against another faction | That faction's 1 hidden stat revealed this season |
| PC conducts Riskbreaker operation | Crown Deniability Debt +1 on BG board |
| PC advances Southernmost Expedition zone | Expedition Project advances +1 on BG board |

### Conviction Invocation (Hybrid Only)

In hybrid mode, Champions gain Conviction Invocation: once per season, +1D to one order (stacking with ethical framework alignment for +3D). Critical failure (all dice fail, ≥2 showing 1): Conviction Crisis — GM/NPC AI controls one faction order next season.

### Domain Echo, Scale Interweaving

Carry forward from stage11 §11.5. Seasonal cap: ±2 per attribute per season, shared across phases.

Parliament Integrity is shared across modes: TTRPG Domain Echoes affect PI; BG orders affect PI.

---

## B14: SOLO MODE (MP-06)

Player controls one faction using standard Card-Hand system. All others on NPC AI (3 cards/season).

**Clock Escalation:** Season 8 (Normal): all clocks +1 passive/season. Easy: no escalation. Hard: season 5. Expert: season 3 + one NPC targets player.

**Solo Victory:** Standard victory condition + shared survival holds.
**Solo Loss:** Any clock reaches threshold, or player Stability 0.

**Recommended:** Hafenmark (TC brake, defensive), Varfell (information advantage), Guilds (economic engine). Not recommended: Crown (relationship-dependent), Niflhel (passive RS degradation = moral discomfort in solo).

---

## SYSTEM COUNT (Post-Revision)

| Category | Systems | Count |
|---|---|---|
| Core | Card-Hand (6 types + orientation + Recess) · Cooldown Track | 2 |
| Political | Institutional Mandate · Standing · Deal Tokens · Crown Policy · Parliament Integrity | 5 |
| Thread | TR · Thread Debt · Attention Pool · Community Projects · Co-Movement · Southernmost Expedition | 6 |
| Champions | Presence · Wound States · Renown | 3 |
| Progression | 2 Research Tracks per faction | 1 |
| Victory | Deed Tokens · Secondary Objectives | 2 |
| Faction-specific | TC-as-currency · Network Depth · Contractor · Presence Markers · Policy · Coup Counter | 6 |

**Player-facing total: ~20 core systems** (Southernmost is late-game optional; Coup Counter is NPC-tracked; Hollow Victory is optional). A first-game player interacts with ~15 systems. Within range of complex strategy games (Twilight Imperium ~15, Gaia Project ~10).

**Deferred to advanced/campaign rules:** Substrate Scar visual markers, Conviction Invocation (BG standalone), Season Objectives.

---

## EDITORIAL FLAGS

| ID | Item | Blocking? |
|---|---|---|
| BG-E-30 | Confirm Card-Hand system adoption (replaces Order tokens) | Yes — structural precondition |
| BG-E-31 | Champion Renown ability text per faction | Yes |
| BG-E-33 | Belief Intervention content per Champion (MP-32) | Yes |
| BG-E-34 | Institutional Mandate trigger conditions per faction — review proposed conditions | Yes |
| BG-E-35 | NPC AI tree update for Card-Hand system | Yes — blocks NPC play |
| BG-E-36 | Secondary Objective card text (12 cards) | Low |
| BG-E-37 | Co-Movement deck expansion for Thread Debt and Community Project coverage | Yes — P-14 |
| BG-E-38 | Senate Market card balance and pricing | Low |
| BG-E-39 | Research Track L3/L5 event triggers per faction | Low |
| BG-E-25 | Thread Veil card content (revised — Baralta lineage card replaced) | Low |
| BG-E-26 | Niflhel Network Coordinator card content | Low |
| BG-E-45 | Restoration Movement leader — name and characterize | Yes (if playable) |
| BG-E-46 | Cardinal of Prudence — name and characterize (tithes, charities) | Low |

---

## CARRY-FORWARD REGISTER

| Section | Status |
|---|---|
| B2 Territory Map (layout, adjacency, territory table) | Unchanged + clock environmental effects |
| B6 Military (combat, disposition, siege, supply) | Unchanged except Formation Break fix, unit renaming, Inquisitor/Hired Blade/Riskbreaker additions |
| B7 Co-Movement Cards (20-card deck) | Carry forward + expand for Thread Debt/Project coverage |
| B9 Event Deck (30-card structure) | Carry forward; integrate GT-01 |
| B10 Endgame Events (Rupture, Holy State, Invasion) | Unchanged |
| B11 Entity Encounters | Unchanged |
| canon/valoria_canonical_timeline.md | Needs Solmund naming correction (currently says Galbados) |

---

## OPEN GAPS

| Gap | Status |
|---|---|
| Riskbreakers | RESOLVED — integrated as Crown/Löwenritter covert unit with Deniability Debt track |
| Four Cardinals | RESOLVED — three named (Jarnstal, Olafsson, Klapp); fourth (Prudence) needs naming (BG-E-46) |

---

*Revision complete. Changes from v1: naming corrected (Solmund, Restoration Movement, AS throughout); Löwenritter full 8th faction; Inquisitors as Church unit; Schoenland active NPC AI; Southernmost Expedition with Forgetting barrier; Parliament Integrity shared track; Standing replaces Contempt+Leverage; Proxy Support cut; Season Objectives cut; Lead/Follow simplified to Domain Expertise +1D; Substrate Scars deferred; Conviction Invocation deferred to hybrid-only; Hollow Victory made optional; Restoration Movement optionally playable; cascade depth cap added; information layering principle applied; half-Deed scoring fixed to whole numbers; Policy resolution order defined; Hired Blades limitations enforced; Guild Forum integration added.*

*System count reduced from ~29 to ~20 core (first-game ~15). All cuts preserve the emergent narrative engine — emergence comes from system interaction, not system quantity.*
