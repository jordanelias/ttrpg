# VALORIA: BOARD GAME MODE
## Compilation Stages B1–B10

*Board Game Mode is a standalone competitive-cooperative game for 2–6 players. It shares the Valoria setting, faction mechanics, clocks, and territory map with TTRPG mode but replaces narrative resolution with card-driven orders, simplified unit management, and structured turn sequences. The three game-end conditions — Rendering Stability Rupture, Theocracy Counter Holy State, Institutional Pressure Invasion — are shared with TTRPG mode. Victory is per-faction unless the shared Rendering Stability survival condition is met.*

---

## B1: OVERVIEW AND SETUP

### Player Count and Mode

| Players | Mode | Notes |
|---|---|---|
| 2 | Competitive (asymmetric) | Each controls one major faction; remaining factions run on Non-Player Character artificial intelligence |
| 3–4 | Competitive-cooperative | Each controls one faction; Non-Player Character artificial intelligence runs remainder |
| 5 | Competitive-cooperative | One player controls Crown + Löwenritter as allied bloc |
| 6 | Full faction coverage | Crown, Church, Hafenmark, Varfell, Guilds, Niflhel each played by one player |

**Revolution is always Non-Player Character-controlled** regardless of player count. Its Rawlsian framework and movement structure make it more useful as a reactive force than as a direct player instrument.

**Schoenland is always Non-Player Character-controlled.** See B8 (Non-Player Character artificial intelligence).

### Faction Assignment

At 3–5 players, assign factions by draft. First-pick order: random roll. Each player blindly draws a faction card and may swap once with any willing player before the game begins.

At 2 players: recommended pairing is Crown vs. Church. All other match-ups are supported but see notes in B10 on 2-player victory tuning.

### Components

**Boards and Tracks**
- 1× Main board: territory map (15 territories in adjacency layout), 3 clock tracks (Rendering Stability 100→0, Theocracy Counter 0–100, Institutional Pressure 0–100), seasonal accounting track, round structure reference
- 3× Clock sliders or tokens: one per track (Rendering Stability starts at 72, Theocracy Counter at 15, Institutional Pressure at 20)
- 15× Territory tiles: double-sided (controlled/uncontrolled), showing Prosperity and Fortification values
- 1× Seasonal accounting board: faction stat grid, pending Domain Action queue, stability check record

**Faction Components (per faction)**
- 1× Faction card (stats, unique power, order set, victory condition, Thread capability)
- 1× Leader card (Non-Player Character leader stats, conviction, deviation cost)
- 6× Stat dials or track markers: Mandate / Influence / Wealth / Military / Intel / Stability (where applicable)
- 4× Unit tokens (light infantry base type; additional types unlocked by muster)
- 1× Order Set reference card
- 5× Order tokens (placed face-down during planning phase)
- 1× Ethical Framework reminder card

**Shared Components**
- 1× Co-Movement card deck (18 cards)
- 1× Event deck (30 cards: clock-triggered events + random seasonal events)
- 1× Disposition table card (shared reference for mass combat)
- Faction control markers (10 per faction, in faction colour)
- Unit type tokens: Light Infantry, Heavy Infantry, Cavalry, Ranged, Artillery, Knights Templar (Church only)
- Fortification tokens (0–4 per territory)
- Prosperity cubes (1–7 per territory)
- Parliamentary Vote tokens (2 per faction)
- 1× Round tracker (seasons 1–20; year markers at 4, 8, 12, 16, 20)

**Cards**
- 30× Event cards (structured in B9)
- 20× Co-Movement cards (drawn on Thread operations; structured in B7)
- 7× Seasonal Event cards per faction (special seasonal trigger cards)
- 10× Non-Player Character artificial intelligence cards per Non-Player Character faction (Crown, Church, Hafenmark, Varfell, Guilds, Niflhel, Revolution, Schoenland)

### Starting State

Before play begins, apply starting setup from territorial and faction records:

**Territory control:** Place control markers per territory starting control (§7.2). Starting Prosperity and Fortification values from territory table.

**Faction stats:** Set all faction stat dials to starting values per faction sheet.

**Clocks:** Place Rendering Stability at 72. Theocracy Counter at 15. Institutional Pressure at 20.

**Units:** Each player-controlled faction places 1 Light Infantry unit in their home territory at game start. Crown receives 1 additional unit in Arnesheld (Löwenritter garrison).

**Event deck:** Shuffle. Place face-down beside board.

---

## B2: TERRITORY MAP

### Layout

The 15 territories are arranged in a north-south axis. The board represents the Valorian peninsula. Connections are adjacency-based (not hex grid); movement costs are abstracted via the march order procedure.

```
                    [15: Schoenland] ─── [4: Spartfell]
                          |                     |
[7: Lowenskyst] ──── [6: Hafenvalor] ──── [1: Valorsplatz] ──── [2: Gransol]
       |                  |                     |                      |
       └──────── [3: Himmelenger] ─────── [5: Arnesheld] ────── (to 4)
                          |
[8: Eidursjo] ──── [10: Sigurdshelm]
       |                  |
[11: Halvardshelm]      [9: Varfell] ──── [12: Oastad]
       |                  |                    |
       └──────────── [14: Varfell]      [13: Stillhelm]
```

*Abbreviated layout for reference. Full adjacency from territory table below.*

### Territory Table

| # | Territory | Starting Control | Prosperity | Fort | Special Property | Adjacent |
|---|---|---|---|---|---|---|
| 1 | Valorsplatz (Capital) | Crown | 6 | 2 | Royal Court: Crown Decree −1 Ob. Parliament: Hafenmark Influence −1 Ob. | 2, 3, 5, 6 |
| 2 | Gransol (Crown heartland) | Crown | 5 | 1 | Garrison: +1D Muster here. | 1, 3, 4 |
| 3 | Himmelenger (Cathedral city) | Church | 5 | 2 | Grand Cathedral: Theocracy Counter +1/season Church controls. Church Excommunicate −1 Ob here. | 1, 2, 6, 7 |
| 4 | Spartfell | Crown | 3 | 2 | Altonian Border: Institutional Pressure threshold events trigger here first. Invasion entry point. | 2, 5, 15 |
| 5 | Arnesheld (Military heartland) | Crown / Löwenritter | 4 | 3 | Löwenritter Fortress: Martial Law −1 Ob. Fort max 4. | 1, 4, 9 |
| 6 | Hafenvalor (Hafenmark capital) | Hafenmark | 6 | 1 | Ducal Court: Sovereign Authority may be invoked here. Major port. | 1, 3, 7, 8 |
| 7 | Lowenskyst (Northern port) | Hafenmark | 5 | 0 | Trade Hub: all Trade orders +1D. Schoenland sea route terminus. | 3, 6, 8 |
| 8 | Eidursjo (Forest region) | Guilds | 4 | 0 | Timber/Mining: Guilds Trade +1D. Difficult terrain: March costs 2 movement. | 6, 7, 10, 11 |
| 9 | Varfell (Southern highlands) | Varfell | 4 | 1 | Varfell Seat: Private Collection usable here only. Einhir ruins: Revolution Weaving −1 Ob. | 5, 10, 12, 13 |
| 10 | Sigurdshelm (Underground) | Niflhel | 3 | 0 | Black Market: Niflhel Quiet −1 Ob. All Trade +1 Ob (illicit). | 8, 9, 11 |
| 11 | Halvardshelm (Farming plains) | Guilds | 5 | 0 | Breadbasket: +1 Prosperity/season if uncontested. Muster Ob −1. | 8, 10, 14 |
| 12 | Oastad (Southern forest) | Uncontrolled | 3 | 0 | Thread Wound: Rendering Stability threshold events trigger at Rendering Stability +10 here (substrate more sensitive). Revolution informal. | 9, 13, 14 |
| 13 | Stillhelm (Southernmost border) | Uncontrolled | 2 | 0 | Southernmost Access: required for Expedition. All non-Thread orders +1 Ob. | 9, 12 |
| 14 | Eisengrund (Southern farmland) | Revolution (informal) | 4 | 0 | Einhir Heartland: Revolution Influence −1 Ob. Church Influence +1 Ob. | 11, 12 |
| 15 | Schoenland (Altonian port) | Neutral | 5 | 1 | Altonian Trade: +1 Wealth/season to faction with active Trade order here. Intel orders reveal to Altonia. At Institutional Pressure 75+: Altonian vanguard deploys. | 4, 7 |

### Territory Rules

**Control transfer:** A faction gains control when its units are the only military units present. If multiple factions have units: territory is Contested — no control benefits for any party until resolved by battle or withdrawal.

**Contested territories:** No Prosperity benefit, no Muster action permitted.

**Fortification cap:** Standard maximum is 3. Arnesheld only: maximum 4.

**Uncontrolled territories (12, 13):** First Govern action claims them (no battle required if no enemy units present).

**Thread Wound Territories (T12 Oastad, T13 Stillhelm):** These territories sit over active Thread Wounds. Any faction controlling T12 or T13 for 2 or more consecutive seasons: Rendering Stability −1 per additional season of control (beginning season 3 of occupancy). This applies regardless of faction or intent — the occupation disrupts the local substrate by adding rendered-world activity to an already stressed site. This cost is disclosed to the controlling faction; it is not hidden. Factions that choose to occupy Thread Wound territories knowingly accept this tradeoff.

**Schoenland:** Neutral throughout unless Institutional Pressure ≥ 75 (Altonian vanguard) or a diplomatic alliance is secured (see B10).

---

## B3: FACTION CARDS

Each faction card contains: starting stats, unique power, order set, Thread capability, and victory condition.

---

### FACTION: THE CROWN

**Stats (1–7 scale):** Mandate 5 · Influence 5 · Wealth 4 · Military 4 · Stability 4
*(Intel not tracked — Crown does not operate covert networks institutionally)*

**Ethical Framework: Virtue Ethics**
- Actions that are public, visible, and virtuous: **−1 Ob**
- Covert or morally ambiguous actions: **+1 Ob**

**Leader: King Almud Almqvist**
- Conviction: Order · Resonant Style: Consequence
- Deviation cost: Stability check Ob 2

**Unique Power — Royal Decree**
Once per season. Roll Mandate vs Ob 2.
- Success: One faction attribute change (any faction, ±1) takes effect immediately rather than at seasonal accounting.
- Failure: Crown Mandate −1.
- Constraint: Cannot target Intel. Consecutive season use: +1 Ob per season (decree fatigue).
- BG use: Announce target attribute before rolling. Decree is public — all players see the effect.

**Order Set:** Govern · Muster · March · Trade · Decree (Unique) · Diplomacy

**Thread Capability:** None (institutional). Almud has Thread Sensitivity 28 (Dormant) — this is a narrative property, not a BG mechanic.

**Löwenritter Integration:** Crown controls Arnesheld garrison. If coup threshold fires (see B8 Non-Player Character artificial intelligence), the Löwenritter acts as a separate BG faction under Non-Player Character artificial intelligence for the remainder of the game.

**Victory Condition:** *Constitutional Stability.*

**Standard path:** Crown controls Valorsplatz + Gransol + at least 2 other territories; Mandate ≥ 5; Theocracy Counter < 60; Institutional Pressure < 75; Torben's Loyalty Clock ≥ 5. All conditions must be met simultaneously.

**Alternative path (active consolidation):** Crown controls 4+ territories including Valorsplatz; Mandate ≥ 6; Stability ≥ 6; at least 1 formal alliance with another faction (active Treaty token). Represents genuine consolidated rule independent of Church/Altonian failure.

**Deed Tokens (Crown):** Place a Deed Token when each sub-condition is achieved. Victory requires all 4 tokens simultaneously at Seasonal Accounting.
| Deed | Condition |
|------|-----------|
| 1 | Mandate ≥ 5 |
| 2 | Control Valorsplatz + Gransol + ≥2 other territories |
| 3 | Theocracy Counter < 60 and Institutional Pressure < 75 simultaneously |
| 4 | Torben Loyalty ≥ 5 |

---

### FACTION: THE CHURCH OF GALBADOS

**Stats:** Mandate 5 · Influence 6 · Wealth 5 · Military 4 · Stability 5

**Ethical Framework: Divine Command**
- Doctrine-aligned actions: **−1 Ob**
- Thread-supporting actions: **+2 Ob**

**Leader: Confessor Arne Himlensendt**
- Conviction: Faith · Resonant Style: Evidence
- Deviation cost: Stability check Ob 3

**Unique Power — Excommunication**
Roll: Mandate vs target leader's Mandate (or Ob 2 for non-leaders).
- Overwhelming: Target Mandate −1; target faction barred from Church-controlled territories for 1 season; target personal Reputation −1 with all factions.
- Success: As Overwhelming minus Reputation penalty.
- Failure: Church Mandate −1; target Mandate +1 (martyr sympathy).
- Constraint: Requires Church Mandate ≥ 3. Reversal: Grand Debate (5 exchanges) or new Confessor appointed.

**Theocracy Counter Driver:** Church Mandate 5+ at accounting: Theocracy Counter +1/season. Stability ≤ 4: Theocracy Counter generation pauses.

**Territory Theocracy Counter Scores (flat, non-accruing — Church-controlled territories only):**
- Himmelenger (Cathedral City): 0 Theocracy Counter value. Church starts controlling it. Losing Himmelenger: Theocracy Counter −5 immediately.
- All other Church-controlled territories: +1 Theocracy Counter flat on gaining control; −1 Theocracy Counter on losing control.
- Valorsplatz: +5 Theocracy Counter flat on gaining control; −5 Theocracy Counter on losing control.
- **Expansion lock:** Church may not control more than 1 territory (Himmelenger) until Theocracy Counter ≥ 40. Territorial seizure unlocks at Theocracy Counter 40 (adjusted: Church needs room to expand and reach Valorsplatz before hitting the Theocracy Counter 60 victory threshold).
- **Theocracy Counter 40–70 expansion window:** Between Theocracy Counter 40 and Theocracy Counter 70, Church may claim one uncontrolled territory per season via Govern order (Mandate vs Ob 2). Church may not use military force to seize territories until Theocracy Counter ≥ 70 (C-03 threshold card activates Territorial Seizure with military option).
- **Theocracy Counter ceiling:** Cannot reach 100 without controlling Valorsplatz (the +5 flat score is required for the final push).

**Order Set:** Preach · Govern · Inquisition · Military (Templar deploy) · Excommunication (Unique) · Diplomacy

**Thread Capability:** None. Knights Templar units are immune to Co-Movement card effects that would reduce their Cohesion.

**Victory Condition:** *The Holy State.* Theocracy Counter reaches 60 with Church Mandate ≥ 5 and Church controlling Himmelenger + Valorsplatz. This condition can be met under shared survival (Theocracy Counter 60 < 80 threshold). Theocracy Counter reaching 100 triggers THE HOLY STATE endgame event regardless (see B10) — that is a separate, escalated resolution path.

**Deed Tokens (Church):**
| Deed | Condition |
|------|-----------|
| 1 | Theocracy Counter ≥ 40 |
| 2 | Church Mandate ≥ 5 |
| 3 | Control Himmelenger (continuously since game start or recaptured) |
| 4 | Control Valorsplatz |

---

### FACTION: HAFENMARK

**Stats:** Mandate 4 · Influence 4 · Wealth 5 · Military 3 · Stability 4

**Ethical Framework: Categorical Imperative**
- Procedurally grounded, legal-precedent actions: **−1 Ob**
- Ad hoc or precedent-breaking actions: **+1 Ob**

**Leader: Duchess Inge Baralta**
- Conviction: Order · Resonant Style: Evidence
- Deviation cost: Stability check Ob 1

**Theocracy Counter Suppression:** While Baralta's Mandate ≥ 4: Theocracy Counter −1/season (passive suppression). Lost if Mandate drops below 4 or Baralta is excommunicated (Theocracy Counter +4 immediately on excommunication).

**Unique Power — Sovereign Authority Doctrine**
Once per game (not per season). Roll Mandate vs Ob 4. At Hafenvalor only.
- Overwhelming: Theocracy Counter −3. Church Mandate −1. Heresy Investigation blocked this season. +1D social vs Church for the arc.
- Success: Theocracy Counter −2. Church Mandate −1. Heresy Investigation opens against Baralta (Ob 4).
- Partial: Theocracy Counter −1. Heresy Investigation opens immediately. Church Influence +1.
- Failure: Theocracy Counter +1. Heresy Investigation fires. Baralta Mandate −1.

**Order Set:** Govern · Trade · March · Parliamentary Manoeuvre · Sovereign Authority (Unique) · Diplomacy

**Thread Capability:** None.

**Victory Condition:** *Constitutional Order.* At game end: Hafenmark controls Hafenvalor + Lowenskyst; Mandate ≥ 4; Theocracy Counter < 50; no outstanding Heresy Investigation against Baralta; at least one Parliamentary ruling in Hafenmark's favour.

**Deed Tokens (Hafenmark):**
| Deed | Condition |
|------|-----------|
| 1 | Mandate ≥ 4 and no active Heresy Investigation |
| 2 | Control Hafenvalor + Lowenskyst |
| 3 | Theocracy Counter < 50 |
| 4 | At least 1 Parliamentary ruling in Hafenmark's favour (this season or prior) |

---

### FACTION: VARFELL

**Stats:** Mandate 4 · Influence 4 · Wealth 4 · Military 4 · Stability 4

**Ethical Framework: Consequentialist Pragmatism**
- Short-term, measurable-outcome actions: **−1 Ob**
- Long-term, uncertain-payoff actions: **+1 Ob**

**Leader: Duke Magnus Vaynard**
- Conviction: Reason · Resonant Style: Consequence
- Deviation cost: Stability check Ob 2

**Unique Power — The Private Collection**
Available in Varfell only. Once per season. Roll Intel vs Ob 2.
- Success (choose one): +2D to one Thread-related Domain Action this season; OR reveal one hidden faction stat; OR −1 Ob to one Einhir Research action.
- Failure: Artefact Thread signature detected. Church Intel +1D vs Varfell for 1 season. Rendering Stability −1.
- Thread Knowledge Track (TK 0–5): Advances through the Collection. See B7 for TK effects.

**Order Set:** Govern · Intel · Trade · Military · Private Collection (Unique) · Diplomacy

**Thread Capability:** Indirect. The Collection provides Thread-adjacent effects without direct Thread operations. At TK 5, Vaynard understands Thread structure — but this is a narrative development, not a BG roll.

**Victory Condition:** *Information Supremacy.* At game end: Varfell Intel ≥ 6; TK ≥ 3; control of Varfell; Vaynard has revealed at least 2 hidden faction stats. Alternatively: deliver Thread-knowledge intelligence to the Revolution enabling their Community Weaving success at Rendering Stability > 60. *TK (Thread Knowledge) tokens: gained via successful Private Collection order (+1 TK), Overwhelming Intel order targeting a practitioner or Einhir site (+1 TK), or delivering Thread intel to Revolution enabling Community Weaving (+1 TK, once). Max 1 TK/season. Max 5 TK.*

**Deed Tokens (Varfell):**
| Deed | Condition |
|------|-----------|
| 1 | Intel ≥ 6 |
| 2 | TK ≥ 3 |
| 3 | Control Varfell (T9) |
| 4 | 2 or more hidden faction stats revealed (accumulated total, any faction) |

---

### FACTION: THE GUILDS

**Stats:** Mandate 3 · Influence 4 · Wealth 6 · Military 2 · Stability 5

**Ethical Framework: Moral Relativism**
- Actions benefiting trade or guild autonomy: **−1 Ob**
- Actions requiring moral consistency across contexts: **+1 Ob**

**Leader: Guildmaster Council (Non-Player Character collective)**
- No single conviction. Redirecting policy: Influence vs Ob 3.
- Deviation from prior decision costs no Stability check — the Council's decisions are by consensus and may legitimately reverse.

**Unique Power — Economic Leverage**
Available in territories where Guild Favour ≥ 5 (tracked per territory; starts at 3 in Guild-controlled territories).
Roll Wealth vs target faction Wealth.
- Overwhelming: Target −1 Wealth + −1 Prosperity in one territory.
- Success: Target −1 Wealth for 1 season.
- Failure: Guild Favour −1 in that territory.

**Order Set:** Trade · Govern · Economic Leverage (Unique) · Muster (limited) · Diplomacy

**Thread Capability:** None.

**Victory Condition:** *Economic Dominance.* At game end: Guilds Wealth ≥ 6; control of Halvardshelm + Eidursjo; Guild Favour ≥ 5 in at least 3 territories; Schoenland trade route active (Institutional Pressure < 75). *Note: Trade order in Schoenland (Success) reduces Institutional Pressure by 1 that season — the Guilds' primary Institutional Pressure suppression tool.*

**Deed Tokens (Guilds):**
| Deed | Condition |
|------|-----------|
| 1 | Wealth ≥ 6 |
| 2 | Control Halvardshelm + Eidursjo |
| 3 | Guild Favour ≥ 5 in ≥ 3 territories |
| 4 | Institutional Pressure < 75 (Schoenland route open) |

---

### FACTION: NIFLHEL

**Stats:** Influence 5 · Wealth 4 · Intel 4 · Stability 4
*(No Mandate, no Military)*

**Ethical Framework: Amoral Consequentialism**
- Covert actions: **−1 Ob**
- Public or open-credit actions: **+2 Ob**

**Structure:** Four competing criminal networks (Sollvik, Hafenbund, Bernweg, Stiltsift). No unified leader. Each network acts as an independent officer. Redirecting any network: Intel vs Ob 3 within Niflhel. See CP14 §8.7 for full network details.

**Unique Power — The Quiet Network**
Choose mode before rolling.

*Intelligence mode:* Roll Intel vs target Intel. Success: learn one hidden faction stat or one Non-Player Character active Belief. Overwhelming: learn two.

*Sabotage mode:* Roll Intel vs target Stability. Success: target Stability −1. Failure: Niflhel Intel −1 for 1 season; target gains Grievance Marker.

*Assassination mode:* Roll Intel vs target Intel +2. Overwhelming: named Non-Player Character eliminated; no evidence. Success: eliminated; evidence trail. Partial: target wounded; evidence. Failure: operative captured; Niflhel Stability −2.

*Rendering Stability cost:* Each Quiet deployment: Rendering Stability −0.5 (cumulative). Niflhel's Southernmost harvesting supply chain disturbs Thread substrate. They do not know this mechanically — the Rendering Stability degradation is applied by the game without player attribution.

**Order Set:** Intel · Sabotage · Assassination · Trade (covert) · Quiet Network (Unique) · Smuggle

**Thread Capability:** Indirect and unintentional. Rendering Stability degrades from Niflhel operations without faction knowledge.

**Victory Condition:** *Shadow Supremacy.* At game end: Niflhel Intel ≥ 5; control of Sigurdshelm; at least 3 pieces of hidden faction information held; no arm of Niflhel publicly compromised; Stability ≥ 4. *Publicly compromised: any Intel order targeting Niflhel achieves Overwhelming success → Compromise token placed. Resets via Disappear tactic card or successful counter-Intel order (Ob 2).*

**Deed Tokens (Niflhel):**
| Deed | Condition |
|------|-----------|
| 1 | Intel ≥ 5 |
| 2 | Control Sigurdshelm (T10) |
| 3 | ≥ 3 pieces of hidden faction information held |
| 4 | No Compromise token on any arm AND Stability ≥ 4 |

---

## B4: TURN STRUCTURE

One game round = one season. A campaign year is 4 rounds. Standard game length: 12–16 rounds (3–4 years). Extended game: 20 rounds.

### Round Structure

| Phase | Name | What Happens |
|---|---|---|
| 1 | Season Card | Flip top Event deck card. This season's modifier is public for all. |
| 2 | Planning | All players simultaneously place Order tokens face-down in their designated territory slots. |
| 3 | Intel Reveal | Niflhel (and any faction with Intel operations) reveals any information-gathering result from last season. |
| 4 | Order Resolution | Flip all orders simultaneously. Resolve in priority sequence (see below). |
| 5 | Seasonal Accounting | Apply clock movements. Stability checks. Faction stat changes. CP awards. Check victory and game-end conditions. |
| 6 | Cleanup | Remove temporary effects. Advance round tracker. Draw replacement cards if any. |

### Crisis Response (Optional — Phase 5 Only)

Any faction may initiate a Crisis Response during Seasonal Accounting to collectively push back one clock. Crisis Response requires at least 2 participating factions.

**Procedure:**
1. Initiating faction announces target clock (Rendering Stability, Theocracy Counter, or Institutional Pressure) and contributes ≥ 1 Wealth.
2. Any other faction may join by contributing ≥ 1 Wealth.
3. Roll:
   - *For Theocracy Counter or Institutional Pressure:* Contributing faction with highest Influence rolls Influence vs Ob = (clock value ÷ 20, round up, minimum 1).
   - *For Rendering Stability:* Sum all participating factions' Thread Resonance (TR — see B7). Roll this pool vs same Ob. TR is expended on this roll (faction TR resets to 0 after Crisis Response regardless of result).
4. Results:
   - **Overwhelming:** Clock −(number of contributing factions).
   - **Success:** Clock −(contributing factions ÷ 2, round up).
   - **Partial:** Clock unchanged. Wealth contributed: returned.
   - **Failure:** Wealth lost. Clock +1 (response backfired — overeager intervention destabilised the situation).
5. Wealth contributed is consumed on any result other than Partial.

### Order Resolution Priority

Orders resolve in this sequence. Within same priority: simultaneous (declare before resolving).

| Priority | Order Type | Notes |
|---|---|---|
| 1 | Thread Operations | Rendering Stability change applies first; co-movement fires before any other resolution. |
| 2 | Military orders (March, Assault, Siege action) | Battles resolve simultaneously per territory. |
| 3 | Intel and Sabotage orders | Outcomes apply before economic and governance. |
| 4 | Domain Actions (Govern, Trade, Muster, Diplomacy) | All standard Domain Actions. |
| 5 | Unique Powers | Each faction's Unique Power resolves last. |
| 6 | Decree / Parliamentary Manoeuvre | Crown Decree and Hafenmark Parliamentary Manoeuvre resolve after all others (these affect attribute changes applied to other resolutions; they take effect at next accounting if timing is ambiguous). |

**Mid-phase game-end check:** If a clock reaches 100 during Phase 4, complete the current priority tier, then apply the endgame event before continuing.

**Contested resolution:** If two orders interact in the same territory or target the same faction attribute, both roll simultaneously. Apply results simultaneously. No order gets to react to another order resolving unless a specific card or rule says otherwise.

### Planning Phase Rules

- Orders are placed face-down before any are revealed.
- Each faction has 5 Order tokens per season. Up to 3 may be placed in a single territory; remaining in other territories.
- One Order token = one Domain Action. Faction-specific orders (Unique Powers) use a designated token.
- Orders may not be changed after placement begins. Once first token is placed, all must be placed before any are revealed.
- Faction with lowest Stability places orders first; highest Stability places last. Ties: roll.

---

## B5: ORDERS

### Standard Orders (Available to Most Factions)

---

**GOVERN**
*Purpose:* Control, stability, and infrastructure.

| Roll | Effect |
|---|---|
| Overwhelming | +1 Prosperity in territory (max 7). Territory Stability +1 for 1 season. If uncontrolled: faction gains control. |
| Success | Faction gains/retains control of territory. |
| Partial | Control gained but Prosperity −1 (instability during governance transition). |
| Failure | Territory resistance. Prosperity −1. Faction cannot Govern this territory next season. |

*Roll:* Mandate vs Ob = territory Prosperity ÷ 2 (round up), minimum Ob 1.
*Special:* First Govern in an uncontrolled territory is Ob 1 regardless of Prosperity. No battle required if no enemy units present.

---

**MUSTER**
*Purpose:* Raise military units.

| Roll | Effect |
|---|---|
| Overwhelming | Raise unit type of choice (within eligibility). Territory Prosperity unchanged. |
| Success | Raise Light Infantry. Territory Prosperity −1. |
| Partial | Raise Light Infantry. Territory Prosperity −1. New unit begins next season at Formation Break (−1 Martial for first battle). |
| Failure | Muster fails. Territory Prosperity −1 (labor diverted). |

*Roll:* Military vs Ob = unit type Ob (see unit table in B6).
*Special:* Maximum units per faction = Military stat. Mustering beyond this: +1 Ob per unit over cap.

---

**MARCH**
*Purpose:* Move military units between territories.

No roll required for standard movement. One unit moves one territory per March order. Eidursjo costs 2 movement.

*Contested entry:* Moving into a territory with enemy units triggers immediate battle resolution (see B6). Both sides declare disposition before rolling.

*Supply check:* After March, check supply status for moved units (see B6 Supply).

*Limits:* One March order moves all units in one territory or one unit across multiple territories (not both). Players choose before placing token.

---

**TRADE**
*Purpose:* Generate Wealth.

| Roll | Effect |
|---|---|
| Overwhelming | +2 Wealth. Trade relationship established (−1 Ob to Trade in same territory next season). |
| Success | +1 Wealth. |
| Partial | +0 Wealth. Nothing. |
| Failure | −1 Wealth. Goods lost or taxed. |

*Roll:* Wealth vs Ob = territory Prosperity ÷ 3 (round up), minimum Ob 1.
*Special:* Trade Hub (Lowenskyst) and Altonian Trade (Schoenland while active): +1D to Trade rolls in those territories.
*Sigurdshelm:* All factions Trade at +1 Ob in Sigurdshelm.

---

**DIPLOMACY**
*Purpose:* Inter-faction negotiation and relationship changes.

*Not a roll.* Diplomacy orders are declared openly and resolved as negotiation between players. In the same resolution window (Priority 4), player factions may:
- Offer or accept non-aggression pacts (1 season)
- Offer trade agreements (specified Wealth transfer at seasonal accounting)
- Offer military alliances (units defend jointly in one named territory for 1 season)
- Demand tribute (Influence vs target Mandate — contested roll; success = 1 Wealth transfer)

*Against Non-Player Character factions:* Roll Influence vs Ob = Non-Player Character faction Stability ÷ 2 (round up). Success: Non-Player Character faction takes one action aligned with your interest at next accounting. Overwhelming: two actions.

---

**INTEL**
*(Varfell, Niflhel; other factions at +1 Ob)*

| Roll | Effect |
|---|---|
| Overwhelming | Learn 2 hidden faction stats OR learn 1 stat and 1 pending Order. |
| Success | Learn 1 hidden faction stat. |
| Partial | Learn nothing. Your Intel operation is detected (target faction notified). |
| Failure | Operative captured. Intel −1 for 1 season. Target gains Grievance Marker against you. |

*Roll:* Intel vs target Intel (or Ob 2 if target has no Intel stat).
*Hidden stats:* Varfell and Niflhel may keep one faction stat hidden from public view at any time. Hidden stats must be revealed honestly when targeted by a successful Intel order.

---

**FORTIFY**
*(Controlling faction only; cannot be used while under active siege)*

Roll: Wealth vs Ob = current Fortification level + 1 (min Ob 1). Max Fortification: 5.

| Degree | Effect |
|---|---|
| Overwhelming | Fort +1. Prosperity unchanged. |
| Success | Fort +1. Prosperity −1. |
| Partial | No gain. Prosperity −1. |
| Failure | No gain. Prosperity −1. Cannot Fortify this territory next season. |

---

### Faction-Specific Orders

**ROYAL DECREE (Crown only)** — See B3 Unique Power.

**INQUISITION (Church only)**
Roll: Church Intel vs target territory Stability.
- Success: Open a Heresy Investigation against one character or faction present. Investigation marker placed.
- Ongoing: Each season the Investigation is open: target Mandate −1 (cumulative). Theocracy Counter +2.
- Closing: Grand Debate (Priority 4, 5 exchanges). Win: Investigation closed. Lose: Mandate −2, Theocracy Counter +2 additional.

**PARLIAMENTARY MANOEUVRE (Hafenmark only)**
Roll: Mandate vs Ob = opponent's Influence ÷ 2 (round up).
- Success: One pending Domain Action outcome delayed by 1 season (cannot delay Unique Powers or Decrees).
- Overwhelming: As Success + opponent's Stability −1 for 1 season (procedural obstruction drain).

**PREACH (Church only)**
Roll: Mandate vs Ob = territory population resistance (proxy: Game Master assigns 1–3 based on Revolution Influence in territory).
- Success: Church Favour +1 in territory (tracked like Guild Favour). Theocracy Counter +0.5 (institutional momentum).
- Overwhelming: Church Favour +2. Theocracy Counter +1.
- In Revolution territories (Varfell, Oastad): +1 Ob.

**SMUGGLE (Niflhel only)**
Roll: Intel vs Ob = territory Fortification level + 1.
- Success: Smuggle goods through territory. Target faction −1 Wealth. Niflhel +1 Wealth.
- Failure: Goods seized. Niflhel Wealth −1. Exposure risk: if Partial, Niflhel identity known to territory controller.

---

## B6: MILITARY

### Unit Types

| Type | Martial | Resilience | Cohesion | Health | Muster Ob | TTRPG CP equiv | TTRPG Weapon | TTRPG Armour |
|---|---|---|---|---|---|---|---|---|
| Light Infantry | 3 | 3 | 3 | 9 | 1 | 3 | LightCut | Light |
| Heavy Infantry | 4 | 4 | 4 | 10 | 2 | 4 | HeavyCut | Medium |
| Cavalry | 4 | 3 | 5 | 9 | 3 | 5 | HeavyCut | Heavy |
| Ranged | 3 | 2 | 3 | 8 | 2 | 3 | Projectile | Light |
| Artillery | 2 | 2 | 2 | 8 | 4 | 2 | HeavyBlunt | None |
| Knights Templar | 5 | 5 | 6 | 11 | — | 5 | HeavyBlunt | Heavy |

*BG 'Resilience' = TTRPG unit Endurance proxy (renamed to avoid confusion with character attribute Endurance). Health = Resilience + 6.*

*Anti-Armour keyword (Artillery, Knights Templar): +2D when targeting Heavy Infantry, Cavalry, or Knights Templar.*

*Muster Ob requirements unchanged: Light Infantry None; Heavy Infantry Prosperity 5+ + Wealth Ob 2; Cavalry Prosperity 6+ or officer History + Wealth Ob 3; Ranged officer with Ranged proficiency; Artillery Wealth Ob 4 + 1 season construction.*

**Health = Endurance + 6.** Damage reduces Health. When Health reaches 0: Formation Break.

**Unit cap:** Faction's Military stat = maximum units in play simultaneously. Additional units cost +1 Ob per unit over cap.

### Mustering

Muster actions occur in controlled territories (Priority 4). Roll Military vs Ob = unit type Muster Ob. Territory Prosperity −1 on Success or Partial. New units deploy the following season (placed face-down this season, flipped at start of next season's Phase 1).

### Movement

Each March order moves units as follows:
- Standard territory: 1 movement point
- Eidursjo (T8): 2 movement points
- Stillhelm (T13): 1 movement point but all non-Thread orders receive +1 Ob after arriving

One March order = 2 movement points total for the ordered unit(s) in that territory.

### Combat

Combat resolves when units from opposing factions occupy the same territory at Order Resolution Priority 2.

**Step 1 — Declaration.** Both sides simultaneously reveal disposition (Balanced / Defensive / Offensive / Brutal) and manoeuvre (Advance / Hold / Withdraw / Flank / Bombard).

**Step 2 — Disposition Table.** Read attacker's row, defender's column:

| Attacker \ Defender | Balanced | Defensive | Offensive | Brutal |
|---|---|---|---|---|
| **Balanced** | Ob 1, ±0 | Ob 2, ±0 | Ob 1, +2D | Ob 1, +1D |
| **Defensive** | Ob 1, −2D | Ob 2, −2D | Ob 1, ±0 | Ob 1, −1D |
| **Offensive** | Ob 1, +2D | Ob 2, +2D | Ob 1, +2D | Ob 1, +3D |
| **Brutal** | Ob 1, +3D −1D def | Ob 2, +3D −1D def | Ob 1, +3D −1D def | Ob 1, +3D −1D def |

*Brutal: +3D Offence, −1D Defence. No flat damage bonus. Cohesion 4+ required.*

*Both sides attack simultaneously using own row/column result.*

**Step 3 — Roll.** Pool = unit Martial + commander bonus (if applicable). TN 7. Ob from table. Net successes = damage dealt to opponent.

**Step 4 — Apply damage.** Reduce opposing unit's Health by damage dealt. When Health = 0: Formation Break (see below).

**Step 5 — Morale.** After damage application: if any unit is at Formation Break, that side rolls Cohesion vs Ob 2. Failure: unit Routes (cannot take ordered actions; remove from board for this season; returns to controlling faction next season at Martial −1, recoverable by one Govern action).

**Formation Break:** Unit Health reaches 0. Reset Health to Resilience + 3 (half maximum). All actions at +1 Ob for remainder of battle. Cohesion check required. A unit that reaches Formation Break a second time in the same battle without recovering: auto-Rout (no Cohesion check).

### Disposition Constraints (BG)

- **Defensive:** Requires Cohesion 3+.
- **Offensive:** Requires Martial 3+.
- **Brutal:** Requires Cohesion 4+. If used against a civilian population (Govern order interrupted by Brutal attack): Theocracy Counter +1 if Church present.


### Tactic Cards

Each faction receives a hand of 6 tactic cards at game start (4 shared + 2 faction-specific). Cards refresh each season. One tactic card may be played per battle, placed face-down before the Disposition declaration.

**Simultaneous reveal:** Both sides place tactic cards face-down. Reveal simultaneously. The tactic card sets the Disposition row and provides additional effects. *Shadow Intel exception: see Varfell card.*

**Shared tactic cards (all factions):**

| Card | Disposition | Effect |
|---|---|---|
| Standard Advance | Offensive | No additional effect |
| Disciplined Defence | Defensive | If opponent plays Offensive or Brutal: +1D Defence this engagement |
| Feigned Retreat | Balanced | On loss: opponent's winning units are Overextended (−2D Martial in that territory next season) |
| Concentrated Strike | Offensive | One unit of your choice rolls +2D this engagement |

**Faction-specific tactic cards (2 per faction):**

| Faction | Card | Effect |
|---|---|---|
| Crown | Royal Guard | Elite unit of your choice: +3D this engagement |
| Crown | Ducal Call | Summon 1 unit from adjacent territory this engagement |
| Church | Crusade Fervour | Brutal disposition; Cohesion check exempt this engagement |
| Church | Inquisitor's Mark | Target opposing unit: −2D this engagement |
| Hafenmark | Mercenary Surge | Pay 1 Wealth: +2 Martial pool dice this engagement |
| Hafenmark | Sovereign Authority | Immune to Disposition table Ob penalties this engagement |
| Varfell | Shadow Intel | After both cards placed face-down: reveal opponent's card. You may swap your card for a different one from your hand. |
| Varfell | Calculated Retreat | Withdraw all units; opponent cannot pursue this season |
| Guilds | Paid Off | Target opposing unit: −1D this engagement (costs 1 Wealth) |
| Guilds | Logistics Mastery | Strained units fight at full Martial this engagement |
| Niflhel | Assassination | Target opposing commander: all opponent units −1D this engagement |
| Niflhel | Disappear | Withdraw all units; no Overextended penalty; clears Compromise token if held |
| Löwenritter | Iron Discipline | Immune to Route this engagement regardless of Cohesion check |
| Löwenritter | Martial Law | After winning: territory gains Martial Law next season |
| Revolution | People's Courage | All units: Cohesion +1 this engagement |
| Revolution | Ambush | In Oastad or Stillhelm only: opponent has no Defence allocation first exchange |

### Siege Clock

Siege may be declared against any territory with Fortification 2+. Fortification 0–1 territories are assaulted directly (immediate combat, no siege).

**Siege Clock** starts at the territory's Fortification level.

**Each siege season:**
- **Attacker:** rolls Military vs Ob = defender's current Stability. Success: Clock −1.
- **Defender (choose one):** Relief (Influence Ob 2 → Clock +1); Sortie (Military vs Ob = attacker Military ÷ 2 → Clock +1); Negotiate (Influence vs attacker Stability → resolve diplomatically).

Clock cannot drop below 0 mid-season. **At Clock = 0 (Accounting):** walls breached — immediate mass combat resolves, then territory control transfers.

**Siege end:** Clock = 0 (breach), attacker withdraws, or negotiated settlement.

**Hybrid:** Player Character Personal Phase sabotage success applies as Domain Echo (Clock −1 at Cascade Phase), stacking with the attacker's seasonal roll. Maximum Clock movement per season: −2.

**Siege Rendering Stability cost:** Rendering Stability −1 per season of active siege. Einhir site in fortification: Rendering Stability −1 additional per season.

### Supply Lines

Checked at seasonal accounting for each unit.

| Status | Condition | Effect |
|---|---|---|
| Supplied | Within 2 territories of friendly-controlled Prosperity 3+ | None |
| Strained | 3 territories from supply, or supply territory Prosperity 1–2 | −1D all rolls next season |
| Cut Off | No connected friendly territory with Prosperity 1+, or route blocked | −1 Endurance/season; Cohesion check Ob 1 or −1 Cohesion |

---

### Annual Attrition (Year-End Accounting — Round 4, 8, 12, 16, 20)

At the end of each game year (every 4th round), apply annual attrition to all military units:

- **Units that fought in at least one battle this year:** Cohesion check Ob 1. Failure: Cohesion −1.
- **Units that did not fight:** No Cohesion check. Veteran idleness is not attrition.
- **Units at Cohesion 1:** Automatically retire at year-end unless the controlling faction spends 1 Wealth to maintain them through hardship.
- **Retirement and replacement:** Retired units may be replaced via Muster at −1 Ob the following season (fresh recruits replace battle-worn veterans with institutional momentum).
- **Elite units (Cohesion 5+):** On a failed Cohesion check, may spend 1 Wealth to ignore the result (elite units have support structures).

*Design note: Annual attrition creates a strategic pulse — build-fight-rebuild — and prevents permanent stationary armies from dominating the late game.*

---

## B7: THREAD OPERATIONS AND CO-MOVEMENT

### Board Game Thread Framework

In Board Game Mode, Thread operations are faction-level actions triggered by Unique Powers and specific order types. Full practitioner mechanics (Thread Sensitivity, CD, personal Leap) are not used. Thread operations are abstracted to faction-card procedures with co-movement consequences preserved.

**Rendering Stability Track:** Rendering Stability runs 100→0. Starting value: Rendering Stability 72. Rendering Stability is hidden from players by default — use the Investigate Thread order to reveal it. Shared loss condition: Rendering Stability reaches 0 (The Rupture). See §5.4.3 for full threshold effects.

**Factions with Thread capability:**

| Faction | Thread Access | How |
|---|---|---|
| Revolution | Community Weaving (Unique Power) | Collective operation; reduces Rendering Stability (raises Rendering Stability value) |
| Varfell | Private Collection (Unique Power, indirect) | Thread-adjacent; triggers Rendering Stability degradation on failure |
| Niflhel | Southernmost harvesting (passive) | Rendering Stability −0.5/season from operations; unattributed |
| Any faction with Thread Sensitivity 50+ affiliated character | Mend order | Gap closure; Rendering Stability restoration |
| Any with Thread Sensitivity 30+ affiliated character | Thread order (optional rule) | Advanced play; Game Master adjudicates |

### Revolution: Community Weaving Procedure

Available in: Varfell (T14), Oastad (T12), Varfell (T9, −1 Ob).

Requirements: Revolution Influence in territory. At least 1 practitioner affiliated (narrative; confirmed at campaign start or through play).

Roll: Influence vs Ob = (100 − Rendering Stability) ÷ 20 (round up, minimum Ob 1). As Rendering Stability degrades, this operation becomes easier — the community's need grows.

| Result | Effect |
|---|---|
| Overwhelming | Rendering Stability +2. Draw 1 Co-Movement card. |
| Success | Rendering Stability +1. Draw 1 Co-Movement card. |
| Partial | Rendering Stability unchanged. Revolution Stability −1. Draw 1 Co-Movement card. |
| Failure | Revolution Stability −1. Rendering Stability −1. Draw 1 Co-Movement card. |

**Co-Movement is mandatory on every Thread operation.** This is P-01 (Inseparability). Even beneficial Thread work produces consequences.

### Mend Order Procedure

Available to: any faction with an affiliated Thread Sensitivity 50+ character, or Revolution (via Community Mending).

**Full thread order table (Weave/Mend/Investigate/Harvest) and degree outcomes:** See §5.6.1 of Part Five (Thread Operations). Summary:

| Order | Roll | Overwhelming | Success | Partial | Failure |
|---|---|---|---|---|---|
| **Weave** | Intelligence vs Ob = (100−Rendering Stability)÷20 | Rendering Stability +2 | Rendering Stability +1 | Rendering Stability unchanged; draw Co-Movement Card | Rendering Stability −1; draw Co-Movement Card |
| **Mend** | Intelligence vs Ob by Gap category (SO:1, Standard:2, Entrenched:3, Catastrophic:4) | Gap closed; Rendering Stability +2 | Gap closed; Rendering Stability +1 | Gap reduced one category | Gap unchanged; Rendering Stability −1 |
| **Investigate** | Intelligence vs Ob 3 (+1 Ob at Rendering Stability <40 or <20) | Learn Rendering Stability + Gap locations | Learn Rendering Stability value | Learn approximate Rendering Stability | Learn nothing |
| **Harvest** (Niflhel only) | Intelligence vs Ob 2 | +1 Wealth; Rendering Stability −0.5 | +1 Wealth; Rendering Stability −0.5 | +0.5 Wealth; Rendering Stability −0.5 | No Wealth; Rendering Stability −1 |

All Thread orders draw a Co-Movement Card at Accounting. Rendering Stability threshold +1 Ob (from §5.4.3) applies to all Thread orders.

### Co-Movement Cards (Board Game Version)

The Co-Movement deck contains 20 cards. Each card specifies:
- One **Temporal effect** (affects clock values or territory Prosperity)
- One **Epistemic effect** (affects faction information, orders, or revealed stats)
- One **Actual effect** (affects territory properties, unit stats, or faction relations)

Draw one card per Thread operation regardless of result. Apply all three effects.

**Sample Co-Movement Cards:**

| Card | Temporal | Epistemic | Actual |
|---|---|---|---|
| CM-01 | Rendering Stability +1 (past coherence) | One hidden faction stat is revealed to all players | Object in target territory becomes a Shifting Object marker (+1 Ob to Govern there next season) |
| CM-02 | Theocracy Counter +1 (Church perceives Thread event as divine sign) | Target faction's pending Order is revealed before resolution | Thread residue: all Intel orders in target territory +1 Ob for 1 season |
| CM-03 | Institutional Pressure +1 (Altonian agents observe Thread disturbance) | Nothing | Einhir ruins in territory activate: Revolution gains Influence +1 in territory |
| CM-04 | Rendering Stability −1 (operation disturbed local substrate) | Performing faction's Intel reduced −1D for 1 season | Physical residue: Fortification −1 in territory (Thread pressure on structures) |
| CM-05 | Rendering Stability +1 | Target territory Prosperity +1 (Thread stabilisation has material effect) | Nothing |
| CM-06 | Theocracy Counter −1 (Thread event reveals Church framework as incomplete) | Nothing | Thread sensitivity: all Leap-eligible characters in territory gain Thread Sensitivity +2 (TTRPG crossover marker; track for Hybrid mode) |
| CM-07 | Nothing | Witnesses disagree: 1 random Order token this season is shuffled (that player replaces it before reveal) | Environmental shift: Eidursjo movement cost reduced to 1 this season (Thread energy smooths terrain) |
| CM-08 | Institutional Pressure −1 (Thread event reveals Altonian intervention as spiritually illegitimate to Schoenland) | Nothing | Löwenritter coup tracker advances by 1 (Thread disturbance counts as Crown compromise) |
| CM-09 | Rendering Stability −2 (operation backfired) | All players must reveal one pending Order before placing remaining tokens this planning phase | Nothing |
| CM-10 | Rendering Stability +3 (exceptional repair) | Nothing | Revolution Stability +1 (community strengthened by successful operation) |

*Note: The confirmed 18-card deck includes CM-01 through CM-18. CM-16: Substrate Settling (Mended territory: Thread ops −1 Ob next season). CM-17: Scar Trace (Mended territory retains visible scar; Church Theocracy Counter +1). CM-18: Residue Condensation (dissolution residue forms at Mending site; Niflhel may harvest). [EDITORIAL: 10 remaining Co-Movement cards — expand from framework above, maintaining P-01 inseparability in each card.]*

### Thread Resonance (TR)

**Thread Resonance (TR 0–5)** is a per-faction track that measures how much a faction's season has been touched by Thread events. TR is temporary — it resets to 0 at Seasonal Accounting (after any Crisis Response that uses it).

**TR accumulates when (during Order Resolution or Accounting):**
- A Thread operation occurs in or adjacent to the faction's controlled territory: +1 TR
- A Co-Movement card effect directly affects this faction: +1 TR
- Rendering Stability drops below a clock threshold this season: +1 TR (all factions)
- Faction units occupy T12 or T13 (Thread Wound territories): +1 TR per season of occupancy

**TR cap: 5.** Faction-specific modifiers may raise the cap (see Thread Veil cards when implemented).

**TR effects:**
| TR | Effect |
|----|--------|
| 0 | No effect |
| 1 | *Thread Awareness:* Once this season, look at the top card of the Co-Movement deck (do not reveal or reorder). |
| 2 | *Resonance:* One of this faction's orders may be placed *after* the Season Event card is revealed (not before). The order must be placed before any orders are flipped. |
| 3 | *Sensitive Proximity:* All Intel orders this season targeting practitioners, Einhir sites, or Thread operations: +1D. |
| 4 | *Threshold Feeling:* Once this season, ask any yes/no question about the current Rendering Stability value (e.g., "Is Rendering Stability above 40?"). Answer is accurate. |
| 5 | *Full Resonance:* Spend all TR (reset to 0): either (a) cancel one Co-Movement card effect targeting this faction this season, OR (b) contribute this faction's TR as a bonus die to Revolution's Community Weaving roll this season (+5D). |

*Thread Resonance is the board game expression of P-01 (inseparability): factions that are proximate to Thread events are unavoidably affected by them. TR does not grant Thread capability — it represents environmental sensitivity, not operational access. The epistemological barrier (P-08) remains intact.*

---

### Rendering Stability Passive Degradation from Niflhel

At every seasonal accounting: Rendering Stability −0.5 if Niflhel is in play and has conducted at least one order this season. This is applied automatically, without attribution, and without Niflhel's knowledge mechanically. Players controlling Niflhel are not told this is the source. The effect is described as "substrate disturbance from southern trade routes."

### Thread Knowledge Track — Varfell (TK 0–5)

Tracked on Varfell's faction card. Advances via:
- Successful Private Collection use: TK +1 (cap 2 per campaign)
- Sustained practitioner relationship (narrative; 1 season commitment): TK +1 (cap ×2 total)
- Church archive access via Niflhel: TK +1 per archive accessed (requires Niflhel cooperation)
- Player-to-player knowledge transfer (any faction sharing Thread-level information): TK +1–2 by depth

| TK | Campaign Effect |
|---|---|
| 1–2 | Acute awareness, no mechanical effect. |
| 3 | Theocracy Counter +1 (Vaynard's structural theory destabilises institutions). Succession leverage formalized: +1D Diplomacy with Crown. |
| 4 | Varfell will offer Collection access for Thread education. Declare to Revolution or any practitioner faction. |
| 5 | Theocracy Counter +3. Vaynard understands Galbados's structural nature. Seeks capability. Game-level event: TK 5 triggers [EDITORIAL: Varfell TK 5 consequence to be determined — capability-seeking resolution path]. |

---

## B8: Non-Player Character artificial intelligence

Non-Player Character-controlled factions follow deterministic priority trees. At the start of each Planning Phase, the active player to the left of the Non-Player Character's assigned seat (or rotate if no assigned seat) draws the top Non-Player Character artificial intelligence card for that faction and executes it.

Each Non-Player Character artificial intelligence card specifies:
- Current priority conditions (check in order; execute first that applies)
- Default order if no condition matches
- Clock-threshold overrides

---

### Crown Non-Player Character artificial intelligence

*Used when Crown is not player-controlled.*

**Priority 1 — Almud constraint check:** If Theocracy Counter > 45, Crown executes one Diplomacy order attempting to secure Church non-aggression pact. Do not execute military orders this season.

**Priority 2 — Succession:** If Institutional Pressure > 29 and Torben has not been sent (Loyalty Clock not started), Crown executes Diplomacy vs Altonia (Ob 4). Failure: Torben departs next season.

**Priority 3 — Defend capital:** If Valorsplatz is Contested, Crown deploys March order moving nearest units to Valorsplatz.

**Priority 4 — Treaty maintenance:** Crown executes Trade order in highest-Prosperity controlled territory.

**Default:** Govern in Gransol.

**Clock override:** At Institutional Pressure > 59, Crown executes Grand Diplomatic Scene preparation (Diplomacy + Influence both deployed toward Altonian engagement).

---

### Church Non-Player Character artificial intelligence

*Used when Church is not player-controlled.*

**Priority 1 — Theocracy Counter expansion:** Church executes Preach in territory with lowest Church Favour.

**Priority 2 — Heresy response:** If any faction has openly performed Thread operations or if Rendering Stability < 60: Church opens Inquisition in the territory where the event occurred.

**Priority 3 — Excommunication trigger:** If Crown Mandate < 4 and Theocracy Counter > 30: Church executes Excommunication against Crown leader.

**Priority 4 — Military deployment:** If Church Mandate ≥ 5 and Theocracy Counter > 50: deploy Templar unit to Valorsplatz or Hafenvalor (whichever is not Church-controlled).

**Default:** Govern in Himmelenger.

**Clock override:** At Theocracy Counter > 70, Church executes territorial seizure attempt (Mandate vs Ob 3 for each uncontrolled territory adjacent to Church-held territory; one attempt per season).

---

### Hafenmark Non-Player Character artificial intelligence

*Used when Hafenmark is not player-controlled.*

**Priority 1 — Theocracy Counter brake:** If Theocracy Counter > 30 and Baralta Mandate ≥ 4: Hafenmark executes Parliamentary Manoeuvre targeting Church's most recent Domain Action.

**Priority 2 — Economic consolidation:** Hafenmark executes Trade in Hafenvalor or Lowenskyst (whichever has higher Prosperity).

**Priority 3 — Sovereign Authority trigger:** If Theocracy Counter > 40 and Baralta Mandate ≥ 4 and Sovereign Authority not yet used: trigger Sovereign Authority this season (in Hafenvalor).

**Priority 4 — Defend ports:** If Lowenskyst or Hafenvalor is Contested: March units to contested port.

**Default:** Govern in Hafenvalor.

---

### Varfell Non-Player Character artificial intelligence

*Used when Varfell is not player-controlled.*

**Priority 1 — Intelligence gathering:** Varfell executes Intel order against faction with highest Mandate (knowledge of the powerful).

**Priority 2 — Private Collection:** If in Varfell and Collection available: execute Private Collection. Prioritise revealing hidden stats.

**Priority 3 — TK advancement:** If practitioner faction available for contact and TK < 3: Varfell executes Diplomacy toward that faction.

**Priority 4 — Maintain Varfell:** If Varfell is threatened: March units to Varfell.

**Default:** Trade in highest-Prosperity controlled territory.

---

### Guilds Non-Player Character artificial intelligence

*Used when Guilds are not player-controlled.*

**Priority 1 — Economic leverage:** If any faction's Military is in Halvardshelm or Eidursjo: Guilds executes Economic Leverage against that faction.

**Priority 2 — Trade:** Guilds executes Trade in Halvardshelm (highest Guild Favour territory).

**Priority 3 — Favour building:** If Guild Favour < 5 in a controlled territory: Govern to build Favour.

**Priority 4 — Resist military threats:** If Guilds Military ≤ 1 and any faction has Military ≥ 4: Guilds executes Diplomacy toward non-threatening faction to seek alliance.

**Default:** Trade in Eidursjo.

---

### Niflhel Non-Player Character artificial intelligence

*Used when Niflhel is not player-controlled.*

**Priority 1 — Exposure avoidance:** If any Niflhel operative was detected last season: Quiet Network (Intelligence mode) against detecting faction to suppress evidence.

**Priority 2 — Wealth generation:** Niflhel executes Smuggle in highest-Fortification adjacent territory.

**Priority 3 — Sabotage highest-stability faction:** Identify faction with highest Stability. Quiet Network (Sabotage mode) against that faction.

**Priority 4 — Control Sigurdshelm:** If Sigurdshelm is threatened: any available response to maintain control.

**Default:** Intel order against the currently leading faction (highest combined stats).

---

### Revolution Non-Player Character artificial intelligence

**Key Named Figures:**

*Eidur Sjostrom* — Southernmost elder, Thread Sensitivity 70+. Survived a Thread gap excess event. Engages with Revolution selectively when it serves Thread repair. Not politically motivated. Chest occasionally falls out of configurational coherence — detectable by Thread Sensitivity 30+.

*Hakan Reusfoldt* — Revolution organiser, Thread Sensitivity 0. Culturally Einhir-connected. Relentless and politically sharp. Once per season: redirect Revolution Influence between territories without an order (Influence vs Ob 2).

### Revolution Non-Player Character artificial intelligence (Priority Trees)

*Always Non-Player Character-controlled.*

**Priority 1 — Rendering Stability response:** If Rendering Stability < 60 and practitioner available: Community Weaving in Varfell or nearest eligible territory.

**Priority 2 — Influence expansion:** Revolution executes Govern (informal presence claim) in Oastad if uncontrolled.

**Priority 3 — Counter-Church:** If Church Favour > 4 in Varfell: Revolution executes counter-Preach (Influence vs Ob = Church Favour ÷ 2, success reduces Church Favour by 1).

**Priority 4 — Support practitioners:** If any faction publicly supports Thread operations: Revolution executes Diplomacy toward that faction (affinity-building).

**Default:** Govern in Varfell.

**Non-Player Character only rule:** Revolution never executes military orders. It has no Military stat. All Resolution-phase cards that would trigger military action for Revolution instead trigger Community Weaving or Influence action.

---

### Schoenland Non-Player Character artificial intelligence

*Always Non-Player Character-controlled.*

**Priority 1 — Profit from tension:** If two or more factions are actively at war (Contested territories with battles resolved this season): Schoenland executes Trade in Lowenskyst (sea route active; +1 Wealth).

**Priority 2 — Hedge toward Altonia:** If Institutional Pressure > 45: Schoenland closes trade route to one Valorian faction (declare publicly; that faction loses Schoenland Trade bonus for 1 season).

**Priority 3 — Alliance response:** If all major factions are at Stability ≥ 5 simultaneously: Schoenland opens naval alliance discussions with Valoria (Institutional Pressure −2 if accepted by Crown + any other faction by Diplomacy).

**Default:** Trade order (Schoenland profits every season regardless of Valorian internal politics).

---

### Löwenritter Coup Trigger and Non-Player Character artificial intelligence

The Löwenritter are a Crown sub-faction at game start. They have no independent orders. If the coup threshold fires, they become an independent Non-Player Character faction.

**Coup Tracker:** Private Game Master/designated-player counter. Starts at 0. Threshold: 5.

**Coup trigger conditions (each adds to tracker):**
- Crown breaks a formal treaty: +1
- Almud supports Thread operations openly: +1
- Torben Loyalty Clock drops to 3 or below: +1
- Crown Mandate drops below 3: +1
- Crown executes Brutal disposition against Valorian citizens: +2
- Co-Movement card CM-08 drawn: +1

**At tracker 5+:** Löwenritter splits from Crown. Arnesheld transfers to Löwenritter control. Löwenritter Non-Player Character artificial intelligence activates.

**Löwenritter Non-Player Character artificial intelligence (post-coup):**
- Priority 1: Hold Arnesheld (defend; never initiate March unless Valorsplatz is under direct threat).
- Priority 2: Martial Law declaration (Govern in Valorsplatz if Crown Mandate < 3).
- Priority 3: Assess Crown compliance (if Crown Mandate recovers to 4+, Löwenritter resumes Crown alliance — tracker reduced by 1 per season of restored Mandate; at 2 or below: reintegration possible via Diplomacy Ob 3).
- Default: Hold position.

---

## B9: EVENT DECK

The Event Deck contains 30 cards. Cards are divided into two pools:
- **15 Clock-Threshold Cards:** Drawn automatically when a clock crosses a threshold marker.
- **15 Seasonal Random Events:** Drawn at Phase 1 (Season Card phase) each round.

Shuffle each pool separately. Threshold cards are drawn from their pile when triggered; seasonal cards are drawn each round regardless.

### Clock-Threshold Events

**Rendering Stability Thresholds (T-01 through T-05):**

| Card | Trigger | Event |
|---|---|---|
| T-01 | Rendering Stability drops below 60 | Monstrous Configuration in Oastad (T12). Oastad Prosperity −1. All March orders to Oastad: +1 Ob this season. Church Inquisition automatically opens in Oastad (Church artificial intelligence acts; player Church may redirect if in play). |
| T-02 | Rendering Stability drops below 40 | Thread operations in all territories: +1 Ob for remainder of game. Practitioner-affiliated factions gain Awareness marker (narrative: they understand what this means). Non-practitioner factions gain Alarm marker (narrative: they don't). |
| T-03 | Rendering Stability drops below 20 | Thread enters battlefields. All mass combat this season: both sides roll 1 Co-Movement card in addition to standard battle resolution. |
| T-04 | Rendering Stability reaches 0 | THE RUPTURE (game-end event). See B10. |
| T-05 | Rendering Stability rises above 60 after being below it | Recovery marker placed. Rendering Stability +1 additional next seasonal accounting (momentum). |

**Theocracy Counter Thresholds (C-01 through C-05):**

| Card | Trigger | Event |
|---|---|---|
| C-01 | Theocracy Counter crosses 40 | The Ultimatum. Church publicly demands Crown recognition of Church supremacy over spiritual governance. Parliament must convene next season: Parliamentary Vote (Crown Mandate vs Church Mandate, 3 exchanges). Loss: Theocracy Counter +3. |
| C-02 | Theocracy Counter crosses 60 | Schism Politics. Church declares Crown spiritually compromised. Excommunication threat issued against all non-Church-aligned ducal leaders simultaneously. Hafenmark Theocracy Counter Suppression checked immediately (if Baralta Mandate ≥ 4: suppression holds; otherwise Theocracy Counter +2). |
| C-03 | Theocracy Counter crosses 70 | Church Territorial Seizure active. Each season: Church may roll Mandate vs Ob 3 to claim one uncontrolled or low-Mandate territory without military action. |
| C-04 | Theocracy Counter reaches 100 | HOLY STATE (game-end event). See B10. |
| C-05 | Theocracy Counter drops below 40 after being above it | Church Momentum broken. Theocracy Counter +1 threshold pauses for 2 seasons. Church Stability check Ob 2. |

**Institutional Pressure Thresholds (I-01 through I-05):**

| Card | Trigger | Event |
|---|---|---|
| I-01 | Institutional Pressure crosses 30 | Tutoring Demand. Altonian diplomatic message arrives: Torben must be sent for education within 2 seasons or Institutional Pressure +5. Torben Loyalty Clock activates at value 8. |
| I-02 | Institutional Pressure crosses 45 | Hostile. Border skirmishes: Spartfell (T4) becomes Contested (Altonian probe units placed; no combat yet). Vassalage demands issued through Schoenland. |
| I-03 | Institutional Pressure crosses 60 | Warlike. Invasion preparations: Altonian military units placed on Spartfell. Institutional Pressure now drifts +2/season instead of +1. |
| I-04 | Institutional Pressure crosses 75 | Invasion Imminent. Altonian vanguard deploys to Schoenland (T15). Schoenland trade route suspended (no Trade orders in T15). Naval route to Lowenskyst (T7) threatened (March from T15 to T7 possible). |
| I-05 | Institutional Pressure reaches 100 | INVASION (game-end event). See B10. |

### Seasonal Random Events (S-01 through S-15)

| Card | Event |
|---|---|
| S-01 | **Harvest Failure.** Roll d6. Territory with that number (re-roll for 13–15 or uncontrolled) loses 1 Prosperity this season. |
| S-02 | **Diplomatic Rumour.** One random hidden faction stat is revealed publicly this season. |
| S-03 | **Assassination Attempt.** Niflhel artificial intelligence executes Assassination order against the current leading faction's leader (highest combined stats) regardless of normal artificial intelligence priority. |
| S-04 | **Trade Boom.** All Trade orders this season: +1D. |
| S-05 | **Military Desertion.** Faction with lowest Stability: −1 unit (remove weakest unit, player's choice). If two factions tied at lowest: both. |
| S-06 | **Church Favour Surge.** Church Preach in one random territory is automatic Success this season (no roll required). Theocracy Counter +1. |
| S-07 | **Schoenland Shift.** Draw Schoenland artificial intelligence card and execute immediately (in addition to its normal turn). |
| S-08 | **Einhir Ruins Discovered.** One random uncontrolled territory (reroll if T13): Revolution Influence +1 there. Rendering Stability +1 (stabilising discovery). [EDITORIAL: Name the Einhir site.] |
| S-09 | **Plague.** One territory (Game Master/designated player draws from territory stack): Prosperity −1 for 2 seasons. Any units there: Endurance check Ob 1 or −1 Endurance. |
| S-10 | **Flood Season.** All March orders in territories 11–14: +1 movement cost. Halvardshelm Breadbasket does not trigger this season. |
| S-11 | **Parliamentary Crisis.** Parliament convenes emergency session. Any pending Parliamentary Manoeuvre resolves this season regardless of timing. Crown Mandate check Ob 1 or −1 Mandate. |
| S-12 | **Altonian Envoy.** Institutional Pressure −1 (gesture of diplomatic goodwill). Any faction may Diplomacy vs Altonia this season at −1 Ob. |
| S-13 | **Löwenritter Audit.** Advance Coup Tracker by 1. Reveal to all players. (Ehrenwall is reassessing.) |
| S-14 | **Thread Disturbance.** Rendering Stability −2 (unexplained). No co-movement card drawn (substrate disturbance, not an operation). All practitioner-affiliated factions: Awareness marker. |
| S-15 | **Restoration Memory.** [EDITORIAL: S-08 Einhir site name deferred.] Revolution Stability +1. Rendering Stability +1. |
| S-16 | **Niflhel Network Exposure.** One Niflhel network (Game Master chooses) has an operation surface publicly. That network's Intel −1 for 2 seasons. Any faction with an active Intel order this season may immediately learn one piece of information that network holds. |
| S-17 | **Einhir Practitioner Surfaces.** A practitioner with Thread Sensitivity 40+ is reported operating openly in one random territory. Church automatically opens Inquisition there. Revolution Influence +1 in that territory. Rendering Stability −1. |
| S-18 | **Border Skirmish.** Two adjacent factions (Game Master or random draw) have a minor military incident. Neither loses units but both take −1 Stability. Institutional Pressure +1 if Crown is involved. |
| S-19 | **Debt Called.** Guilds call a debt from the faction with highest Wealth. That faction: Wealth −1 this season OR Guilds gain Influence +1 in one territory of their choice. |
| S-20 | **Thread Quiet.** Unusually stable substrate this season. All Thread operations: −1 Ob. Rendering Stability +1 at seasonal accounting. Practitioners with Thread Sensitivity 50+ sense it as uncanny — the quiet is wrong, not peaceful. |

---

## B10: VICTORY AND ENDGAME

### Per-Faction Victory Conditions (Summary)

| Faction | Victory Condition |
|---|---|
| Crown | Constitutional Stability (see B3) |
| Church | Theocracy Counter ≥ 60 + controls Himmelenger + Valorsplatz at game-end (see B3) |
| Hafenmark | Constitutional Order (see B3) |
| Varfell | Information Supremacy (see B3) |
| Guilds | Economic Dominance (see B3) |
| Niflhel | Shadow Supremacy (see B3) |

### Shared Survival Condition (P-01 Compliance)

Before checking any per-faction victory, check the shared survival condition:

**Rendering Stability > 20, Theocracy Counter < 80, Institutional Pressure < 80 simultaneously at the moment the game-end trigger fires.**

If this condition is met: all players whose faction victories are also met share a co-victory. The inseparability of the three dimensions is expressed in the shared stakes — no faction achieves its individual victory at the expense of the world remaining inhabitable.

If only one player meets their faction victory condition while shared survival is met: that player wins outright.

If multiple players meet faction victories while shared survival is met: tiebreak by scoring (below).

If shared survival is not met: no per-faction victory counts. The game ends in collective loss unless one of the transcendent endgame paths is achieved.

### Game-End Triggers

Any of the following ends the game immediately:

| Trigger | Game-End Event |
|---|---|
| Rendering Stability = 0 | THE RUPTURE — see below |
| Theocracy Counter = 100 | THE HOLY STATE — see below |
| Institutional Pressure = 100 | THE INVASION — see below |
| Round 20 completed | Standard game-end. Check victory conditions. |

### Endgame Events

**THE RUPTURE (Rendering Stability = 0)**
The relationship between rendered world and thread-substrate changes permanently. This is not automatically a loss. Its meaning is determined by the current state of the world:

- If Revolution Community Weaving was successful at least 3 times and Rendering Stability was below 40 before reaching 0: *Rupture as Healing* — the Thread substrate returns to its pre-Calamity coherence across the entire peninsula simultaneously:
- Stillhelm and the Southernmost become habitable. The Forgetting dissolves.
- Every Lock releases — objects, relationships, and personal threads return to their natural state. Living things that were Locked age at extraordinary speed on release and turn to dust within moments.
- Shifting Objects stabilise. Thread Wounds and Gaps close.
- Galbados relics become ordinary objects — no longer holding configurational charge.
- Dissolution residue reintegrates into the substrate.
- Memory, political structures, deaths, and human consequences remain unchanged.
All factions still in play at Stability ≥ 3: co-survival.
- If Niflhel Southernmost harvesting was uninterrupted for ≥ 8 seasons and no Co-Movement mitigation was applied: *Rupture as Extraction Consequence* — collective loss.
- Default (neither condition): *Rupture Unresolved* — collective loss. Shared survival condition fails automatically.

**THE HOLY STATE (Theocracy Counter = 100)**
The Church has structurally absorbed Valorian governance. Note: the Church's standard victory condition is Theocracy Counter ≥ 60 (see B10 Per-Faction Victory Conditions). THE HOLY STATE fires at Theocracy Counter = 100 as a game-end event regardless of whether the Church has already achieved its standard victory. This is a Church faction victory only if Church also controls Himmelenger + Valorsplatz at the moment Theocracy Counter = 100. Otherwise: it is a collective loss (the Church won an institutional conquest but not the game's victory condition).

If Crown Mandate was ≥ 4 at Theocracy Counter = 100: *Constitutional Resistance Ongoing* — the Crown survives as a contested institution. Crown player may contest the Holy State by triggering a Grand Debate (5 exchanges, final resolution scene). Win: Theocracy Counter −20, Church restructured; game continues to Round 20. Lose: collective loss.

**THE INVASION (Institutional Pressure = 100)**
Altonian forces enter Valoria. This is a collective loss unless:
- A Grand Diplomatic Scene was completed this season (Diplomacy + Influence both deployed, all player factions agree): Institutional Pressure frozen, peace treaty possible, game continues.
- Schoenland naval alliance was secured before Institutional Pressure = 75 and remains active: Altonian naval capacity limited; Institutional Pressure −10 immediately; invasion becomes border conflict. Game continues.

Default: collective loss.

### Scoring (Tiebreak)

Used only when multiple players meet faction victory conditions simultaneously.

| Criterion | Points |
|---|---|
| Clock control: each clock kept below 50 at game end | +2 per clock |
| Territories controlled at game end | +1 per territory |
| Faction stats ≥ 5 at game end | +1 per stat |
| Named Non-Player Character alive and affiliated with your faction | +2 per Non-Player Character |
| Parliamentary rulings in your favour | +1 per ruling |
| Opponent faction eliminated (Stability = 0) | +3 per faction |
| Shared survival condition met | +5 to all scoring factions |

### 2-Player Victory Tuning

At 2 players, each player controls one major faction. The remaining five player factions run on Non-Player Character artificial intelligence. This creates significant clock-driving pressure (5 Non-Player Character factions act, many driving Rendering Stability/Theocracy Counter/Institutional Pressure automatically). 

**2-player adjustment:** Non-Player Character factions execute only 2 orders per season instead of 3. Clock threshold triggers for Non-Player Character factions require 1 additional season of condition persistence before firing (except game-end triggers — those fire immediately).

**Recommended pairings by tension:**
- Crown vs. Church: classic axis tension on Theocracy Counter (highest drama).
- Hafenmark vs. Church: procedural vs. divine authority (Theocracy Counter-focused with Sovereign Authority counterplay).
- Varfell vs. Niflhel: intelligence warfare (low clock drama, high information game).
- Crown vs. Varfell: succession + information asymmetry (balanced; Institutional Pressure becomes primary pressure).

### Extended Game (20 Rounds)

Use when players want a full campaign arc rather than a decisive victory contest. At Round 20:
- Any faction meeting their victory condition wins.
- Shared survival condition still applies.
- If no faction has met victory: last-faction-standing wins (highest scoring faction by tiebreak criteria).

---

---

## B11: ENTITY ENCOUNTER RULES

*(Sourced from GT-03, approved 2026-03-30. Full tables in `designs/generation_tasks_gt01_gt02_gt03.md`.)*

When Rendering Stability drops below 60, monstrous entities may be present in Thread Wound territories (T12, T13) or in territories adjacent to active Rendering Stability threshold events. Entity encounters are called by the Game Master (or in solo mode, triggered automatically on an Rendering Stability threshold card draw).

**Entity Tiers:**
| Tier | Context | Compound Ops | Ob to Resist | Area |
|------|---------|-------------|-------------|------|
| 1 | Small, recent Gap | 2 | 1 | Single zone |
| 2 | Significant Gap | 2 | 2 | Zone + adjacent |
| 3 | Major Gap / Southernmost interior | 3 | 3 | All zones in territory |

**Board Game Effect of Entity Presence:**
- Units in entity territory: Cohesion check Ob = entity Tier each season of presence. Failure: Cohesion −1.
- Governing faction: Govern orders in entity territory: +1 Ob per entity Tier.
- Entity dissolved: Rendering Stability +1d3 (the entity's configuration was contributing to substrate stress; its dissolution releases it).
- **Practitioners present (hybrid/TTRPG zoom-in):** Entity encounter always triggers a Zoom-In condition (see B12).

Roll compound operations from GT-03 table to determine entity effects this season. Roll at start of each season the entity is active.

---

## B12: HYBRID MODE — ZOOM-IN INTERFACE

The following board game events **mandate** a TTRPG personal scene if any Player Character-affiliated faction is involved. GMs may also call a Zoom-In for any of these at their discretion.

| BG Trigger | TTRPG Scene Type | Mandatory? |
|------------|-----------------|-----------|
| Co-Movement card with Thread Resonance ≥ 3 event in a Player Character's home territory | Personal Thread encounter | Recommended |
| Heresy Investigation opened against a Player Character character | Personal/Social Scene | Yes |
| Battle in a territory where a Player Character has stated presence | Combat Scene | Yes |
| Rendering Stability drops below 40 for the first time | Thread Awareness Scene (all practitioners) | Yes |
| Institutional Pressure crosses 30 and Torben is a Player Character or Player Character-adjacent | Personal Decision Scene | Recommended |
| Löwenritter Coup Tracker reaches 4 | Political Crisis Scene | Recommended |
| Named Non-Player Character's Belief is directly challenged by a BG order outcome | Social Scene | Game Master discretion |
| Rendering Stability < 10 (approaching Rupture) | Thread Emergency Scene | Yes |
| Entity encounter in territory with Player Character presence | Entity Encounter Scene | Yes |

**Domain Echo (Zoom-Out):** After a TTRPG personal scene, the Player Character may execute one **Domain Echo** order (Priority 5, after all BG resolution) representing their personal-level action within the strategic phase. One Domain Echo per Player Character per season; the order must be coherent with what happened in the personal scene.

**Zoom-In / Zoom-Out Timing:**
- Zoom-In occurs between BG Phase 4 (Order Resolution) and Phase 5 (Seasonal Accounting).
- Domain Echo resolves before Accounting (applies to Accounting calculations).
- TTRPG scenes that produce attribute changes for an Non-Player Character: apply at Accounting.

---

## EDITORIAL FLAGS

| ID | Item | Status |
|---|---|---|
| BG-E-01 | Co-Movement cards CM-11 through CM-20 | RESOLVED — GT-02 approved 2026-03-30 (designs/generation_tasks_gt01_gt02_gt03.md). Pending BG-E-12: deck size decision before integration. |
| BG-E-02 | Varfell TK 5 consequence / capability-seeking resolution path | Requires editorial decision |
| BG-E-03 | THE RUPTURE narrative determination | Requires editorial design |
| BG-E-04 | Seasonal Event S-08 Einhir site name | Requires territory name editorial decision |
| BG-E-05 | Seasonal Event S-15 Restoration Memory | Requires Restoration Non-Player Character design (already in TTRPG editorial pending) |
| BG-E-06 | Victory condition for Revolution (if ever made player-controllable) | Future design item |
| BG-E-07 | Mandate Dice adoption vs flat orders (MP-01 — structural change) | Requires editorial decision |
| BG-E-08 | Secret Agreement card content per faction (MP-02) | Requires editorial content decisions |
| BG-E-09 | Political Hand card text review — 18 cards across 6 factions (MP-05) | Requires editorial review |
| BG-E-10 | Thread Veil card content — particularly Baralta Einhir lineage, 218 AG card (MP-10) | Requires lore decisions |
| BG-E-11 | GT-01 event deck expansion: add 10 seasonal cards (30→40) or replace 10 existing | Requires editorial decision |
| BG-E-12 | GT-02 co-movement deck: expand to 25 (CM-01–25) or replace CM-11–15 | Requires editorial decision |
| BG-E-13 | GT-03 B11 entity encounter rules: confirm addition (already added) | Low — confirm or revert |
| BG-E-14 | Solo mode recommended faction list | Low |

---

*Board Game Mode compilation complete. Stages B1–B10.*
*Source documents: stage6_factions.md, stage7_territories.md, stage5_clocks.md, stage8_combat.md, stage3_thread_operations.md.*
*Thread Operations cross-reference: Full Thread operation rules for all modes are in §5.6.1 (Part Five). This section provides board game procedure; §5.6.1 governs in cases of conflict.*

*Canon compliance: P-01 (co-movement mandatory on all Thread ops) observed throughout B7. P-05 (three modes distinct) maintained — BG mechanics are board-resolution procedures, not TTRPG narrative systems.*


---

## MT-01: Faction Unit Rosters

Starting unit counts derived from Military scores (Military = max active units).

| Faction | Military | Starting Units | Type |
|---------|---------|---------------|------|
| Crown | 4 | 4 | Mixed infantry + cavalry (standard) |
| Church | 4 | 4 | 2 Templar (elite: Cohesion 5, Martial 4) + 2 garrison (Cohesion 3, Martial 2) |
| Hafenmark | 3 | 3 | 1 ducal guard (elite: Cohesion 4, Martial 3) + 2 militia |
| Varfell | 4 | 4 | Highland infantry (Cohesion 4). +1D in Eisengrund. |
| Guilds | 2 | 2 | Hired mercenaries (Cohesion 3, Martial 2). Rapid replacement via Wealth. |
| Niflhel | — | 0 | No standing units. Relies on Quiet Network. |
| Revolution | — | 0 | No standing units. Community defence via Community Weaving. |
| Löwenritter | 5 (→6 post-coup) | 5 (→6) | All elite (Cohesion 5, Martial 4). Post-coup +1 from Crown transfer. |

**Unit stat defaults:** Standard = Martial 2, Cohesion 3. Elite = Martial 3–4, Cohesion 4–5.
**Cohesion:** −1 per defeat. At 0: unit destroyed.
**Mustering:** 1 new unit per Muster success, up to Military cap.
**Upgrade to elite:** 2 consecutive successful Govern orders in territory + Wealth ≥ 4.
**Church Templars:** Deploy at Theocracy Counter ≥ 40 as free unit in Himmelstift. Elite stat block. Separate from regular garrison cap.