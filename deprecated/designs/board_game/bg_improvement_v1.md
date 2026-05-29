<!-- DEPRECATED: 2026-04-09 — SUPERSEDED BY designs/board_game/valoria_bg_v05_simulation_and_patches.md. Do not use as a mechanical reference. Retained for audit trail only. -->

# VALORIA BOARD GAME — IMPROVEMENT ANALYSIS V1
## Date: 2026-03-31
## Status: Proposals — requires editorial gate review before compilation
## Scope: Gap analysis, mechanic proposals, landmark game synthesis, Thread integration, GT-01/02/03 integration

---

## LANDMARK GAME ANALYSIS

Reference games and the specific mechanic lessons applicable to Valoria BG:

| Game | Core Mechanic | Valoria Application |
|------|--------------|---------------------|
| **Dune (2019)** | Last-moment alliance scoring; prescience prediction; faction treachery | Endgame alliance scoring; secret prediction tokens; Niflhel treachery cards |
| **ASOIAF BG** | Westeros event deck punishes leader; simultaneous orders; Wildling threat | RS Cascade events target leading faction; order tightening |
| **Inis** | Multiple overlapping victory conditions publicly visible; Season cards | Deed tokens for visible victory progress; seasonal political hands |
| **Bretwalda** | Armies rebuild each season; temporal rhythm | Seasonal unit attrition + replenishment cycle |
| **War of the Ring** | Dice-driven action economy; asymmetric capability scarcity | Thread Dice pool replacing flat 5 orders |
| **Root** | Radical structural faction asymmetry (not just stat differences) | Factions use fundamentally different subsystems, not variants of same one |
| **Arydia** | Semi-cooperative: shared threat + private goals; resource pressure | Crisis Response mechanic for clock management |
| **Pax Pamir** | Court cards, coalition loyalty, no map ownership | Political Hand cards; Reputation as loyalty tracker |

---

## GAP ANALYSIS — CURRENT BG WEAKNESSES

### G-BG-01 — ACTION ECONOMY IS FLAT
**Problem:** All factions get 5 orders/season regardless of state. There is no scarcity, no decision tension from resource-limited action selection. The game plays like a Euro worker-placement where all players have equal capability every turn. Root, WotR, and Pax Pamir all use constrained action economies to force decisions.
**Severity:** High — affects fundamental play feel.

### G-BG-02 — NEGOTIATION IS UNSTRUCTURED
**Problem:** Diplomacy is "not a roll, just negotiation between players" — no deal tokens, no enforcement mechanism, no betrayal tracking beyond Reputation. Dune's alliance and treachery structure, and ASOIAF's power-backed promise mechanics, make negotiation feel consequential.
**Severity:** High — affects inter-player dynamics.

### G-BG-03 — VICTORY PROGRESS IS OPAQUE
**Problem:** Players cannot easily track how close others are to their victory conditions. Inis solves this brilliantly with Deed tokens: when a player achieves a condition, they take a token visibly. The tension comes from everyone seeing who is one condition away from winning.
**Severity:** High — affects game arc tension.

### G-BG-04 — THREAD IS PASSIVE
**Problem:** Thread (RS track) is primarily a slow-degrading background pressure. Only Revolution actively restores RS. Niflhel degrades it passively without knowing. The Thread system is Valoria's philosophical core and its most distinctive mechanic — it should generate active decisions, not just exist as a loss condition.
**Severity:** High — affects setting coherence and thematic identity.

### G-BG-05 — FACTION ASYMMETRY IS SHALLOW
**Problem:** All factions use the same order system (Govern/Muster/March/Trade/Diplomacy) plus one Unique Power. Root's genius is that each faction uses a *different* action system — Marquise builds infrastructure, Eyrie has decree cards, Alliance mobilises sympathy. Valoria's factions are stat-different but system-identical.
**Severity:** Medium — affects replayability.

### G-BG-06 — NO SOLO MODE
**Problem:** Confirmed in editorial decisions (2–5 + solo) but completely absent from B1. Solo mode is a significant accessibility and marketing consideration.
**Severity:** Medium.

### G-BG-07 — SEASONAL RHYTHM IS WEAK
**Problem:** Units persist indefinitely. The game has no natural planning horizon or reset rhythm. Bretwalda's army dissolution creates a seasonal pulse. Even ASOIAF's Westeros events force a periodic reset of expectations.
**Severity:** Medium.

### G-BG-08 — COLLECTIVE CRISIS RESPONSE ABSENT
**Problem:** When clocks approach thresholds, there is no formal mechanism for factions to collectively push back. Arydia's shared threat management creates moments where competitive players must cooperate. Currently factions must each individually manage clocks via their own orders, which is inefficient and un-fun.
**Severity:** Medium.

### G-BG-09 — HYBRID INTERFACE THIN
**Problem:** How the BG supports TTRPG zoom-in is mechanically thin. The Domain Echo mechanic exists but the *triggers* for zoom-in are vague. A clear set of "Zoom-In Conditions" (specific BG events that mandate or enable a TTRPG scene) would make the hybrid mode feel designed, not bolted on.
**Severity:** Medium — primarily affects hybrid mode.

### G-BG-10 — NO INFORMATION ASYMMETRY MECHANICS (beyond Niflhel/Varfell stat hiding)
**Problem:** Dune is largely an information game. Players make predictions, hold secret treachery cards, have private capabilities others don't know about. Valoria BG is largely transparent. The intel system (Niflhel/Varfell hiding one stat) is thin.
**Severity:** Medium.

### G-BG-11 — GT-01/02/03 NOT INTEGRATED INTO STAGE_BG
**Problem:** C-11–C-20 and CM-11–CM-20 were designed (GT-01/GT-02, approved 2026-03-30) and live in batch_e_designs.md, but stage_bg_board_game_mode.md still shows only C-01–C-10 and CM-01–CM-10, and retains BG-E-01 as an open editorial flag.
**Severity:** Immediate — state inconsistency.

### G-BG-12 — CHURCH TC EXPANSION LOCK INCONSISTENCY
**Problem:** B3 states Church "may not control more than 1 territory (Himmelenger) until TC ≥ 40" with a note that this was "adjusted." But B9 C-03 (TC crosses 70) states Church Territorial Seizure activates. There's a window from TC 40–70 where the expansion lock lifts but no explicit rule governs how Church expands in that range. The NPC AI says "roll Mandate vs Ob 3 to claim one uncontrolled territory per season" — but only at TC > 70.
**Severity:** Medium — mechanical gap in Church progression.

### G-BG-13 — UNIT HEALTH RESETS ON FORMATION BREAK
**Problem:** B6 states "Reset Health to full" on Formation Break. This means a unit can take a full health bar of damage repeatedly in one battle with no lasting consequence until it fails a Cohesion check. A unit with Cohesion 5 could theoretically cycle through multiple Formation Breaks without routing. This is the "healing loop" problem identified in TTRPG simulations.
**Severity:** Medium — combat distortion.

### G-BG-14 — TERRITORIAL CONTROL VS THREAD WOUND INTERACTION UNDEFINED
**Problem:** Territories 12 (Oastad/Sudwald) and 13 (Stillhelm/Askeheim) are Thread Wound sites. The board game mentions RS threshold events trigger at +10 in territory 12, but there are no rules for what happens when a faction controls a Thread Wound territory over multiple seasons. Do they accumulate RS cost? Does the Church gain TC from suppression there? Does the Revolution gain mechanical advantage?
**Severity:** Medium.

---

## MECHANIC PROPOSALS

### MP-01: MANDATE DICE — Action Economy Overhaul
**Addresses:** G-BG-01
**Inspired by:** War of the Ring (dice-driven action economy)

Each faction rolls a number of **Mandate Dice** at the start of the Planning Phase equal to their current Mandate stat (minimum 2, maximum 7). Each die face corresponds to an order type:

| Face | Order Type |
|------|-----------|
| ⚔ | Military (March, Muster, or Assault) |
| ⚙ | Domain (Govern, Trade, or Fortify) |
| 🕵 | Intel/Covert (Intel, Sabotage, or Smuggle) |
| 👥 | Social (Diplomacy, Preach, Parliamentary Manoeuvre, or Decree) |
| 🌀 | Thread (Thread operation — Revolution/affiliated only; other factions: treat as Wild) |
| ★ | Wild (any order type) |

**Rules:**
- Players may place one Order token of the matching type per die showing that face.
- Two dice of the same type may be combined to upgrade to that order's Unique variant (e.g., two ⚔ → Unique Military action for that faction).
- Unused dice are discarded; they provide no action.
- Maximum orders per season = 5 (not all Mandate Dice, up to 5 placements).
- Faction abilities that "cost no order slot" still function normally.

**Effect:** High-Mandate factions get more dice but still cap at 5 orders. Low-Mandate factions may not get the die faces they need this season, forcing improvisation. A Crown at Mandate 3 rolls only 3 dice — they might get all ⚔ and have no Domain actions available.

**Canon compliance:** P-07 (Calamity = rendered side). Mandate represents institutional coherence — its variance as a dice pool expresses that unstable institutions lose consistent capacity. PASS.

**[EDITORIAL: Confirm Mandate Dice adoption vs flat 5 orders — this is a structural change to the planning phase. Alternatively propose as optional advanced mode.]**

---

### MP-02: DEAL TOKENS AND SECRET AGREEMENTS
**Addresses:** G-BG-02
**Inspired by:** Dune (alliance mechanics), Pax Pamir (court cards)

**Deal Tokens (3 per faction, wooden discs in faction colour):**
- During Diplomacy order resolution, a faction may "spend" a Deal Token by placing it on another faction's faction card as a Pledge.
- A Pledge signifies a specific deal: declared openly (e.g., "I pledge not to march into Hafenvalor this season") or sealed (written on a slip; revealed at end of season).
- **Open Pledges:** publicly binding. Breaking an open Pledge costs Reputation −2 with all factions + Stability check Ob 2. Deal Token returns immediately.
- **Sealed Pledges:** private commitment. Betrayal carries no mechanical penalty unless revealed. Revealing a broken Sealed Pledge: costs the revealer Reputation −1 (tattling) but costs the breaker Reputation −3 and Stability −1.
- Deal Tokens refresh each year (every 4 seasons), not each season.

**Secret Agreement Cards (shuffle 5 into each faction's tactic hand at game start):**
Each Secret Agreement card specifies a condition for a hidden alliance:
- e.g., "If at game end both this faction and a named faction have met their victory condition: +3 VP each."
- Factions may reveal a Secret Agreement during the Cleanup Phase to trigger its effect.
- Each faction has one Secret Agreement card; unused ones stay secret but score 0.

**[EDITORIAL: Secret Agreement card text — content decisions for each faction's hidden win-path.]**

---

### MP-03: DEED TOKENS — Victory Progress Visibility
**Addresses:** G-BG-03
**Inspired by:** Inis (Deed cards / visible victory progress)

Each faction has a **Victory Track** (3–4 conditions, publicly visible on their faction card). When a faction achieves one of its victory sub-conditions, they place a **Deed Token** on that condition. When all tokens are placed *simultaneously* at the start of a Seasonal Accounting phase, the faction may declare victory.

**Rules:**
- Sub-conditions are specific, trackable, and visible. (e.g., Crown: "Deed 1: Mandate ≥ 5"; "Deed 2: Control Valorsplatz + Gransol"; "Deed 3: TC < 60"; "Deed 4: IP < 75 and Torben Loyalty ≥ 5")
- A Deed Token is placed when the condition is met at *any* accounting. It stays unless the condition is broken (removed immediately if condition no longer holds).
- Victory requires all tokens simultaneously at accounting — not just completing the last one.
- This means a faction can be "one Deed away" for multiple seasons, visible to all, creating pressure to disrupt them.

**Effect:** All players can see who is 1, 2, 3, 4 conditions away from winning. The race is visible and players can collectively respond. 

**Canon compliance:** Deed tracking is a player-aid mechanism, not a metaphysical claim. PASS.

---

### MP-04: THREAD RESONANCE TRACK — Making Thread Active
**Addresses:** G-BG-04
**Inspired by:** Setting coherence (P-01, P-14)

**Thread Resonance (TR)** is a per-faction track (0–5) representing how much the faction's season has been touched by Thread events. Unlike TK (Varfell-specific), TR is universal and temporary.

**TR accumulates when:**
- A Thread operation occurs in or adjacent to the faction's controlled territory (+1 TR)
- Co-Movement card affects the faction (+1 TR)
- RS drops below a threshold this season (+1 TR for all factions)
- Faction agent is present at a Thread event (hybrid only)

**TR resets to 0 each season end.**

**TR effects (by level):**
| TR | Effect |
|----|--------|
| 0 | No effect |
| 1 | Thread Awareness: faction may look at the top card of the Co-Movement deck once this season |
| 2 | Resonance: one faction order this season may be declared *after* seeing the Season Event card (not before) |
| 3 | Sensitive Proximity: faction's Intel orders gain +1D when targeting practitioners or Thread-active sites |
| 4 | Threshold Feeling: faction may ask one yes/no question about RS (is it above or below X?) |
| 5 | Full Resonance: faction may spend TR 5 to either (a) cancel one Co-Movement card effect targeting them, or (b) contribute +1 to Revolution's Community Weaving roll this season |

**Canon compliance:** P-01 (inseparability — Thread events touching factions is mechanically expressed). P-14 (all modes express inseparability). PASS.

**Note:** TR does not grant Thread capability. It represents environmental sensitivity, not practitioner skill. P-08 (epistemological barrier) is not violated because TR yields information and timing advantages, not Thread operations.

---

### MP-05: FACTION POLITICAL HANDS — Shallow Asymmetry Fix
**Addresses:** G-BG-05
**Inspired by:** Pax Pamir (court cards), Inis (season cards)

Each faction has a **Political Hand** of 3 cards (drawn from a faction-specific deck at game start; refreshed to 3 at each season change).

Political cards are played face-up once per season during Order Resolution (Priority 4), before Domain Actions resolve. They provide one-time effects specific to the faction's character.

**Sample faction political cards (3 cards per faction = 18 total):**

**CROWN (3 cards):**
- *Ancestral Legitimacy:* This season, Crown Govern orders are Ob −1. Any faction that challenged Crown authority this season: Reputation −1 with neutral factions.
- *Royal Commission:* Assign one NPC to act as Crown agent. That NPC executes one Crown order this season without using an Order token.
- *Succession Settled:* Torben Loyalty +1 immediately. IP −1 this season. Discard after use (1 copy).

**CHURCH (3 cards):**
- *Doctrinal Proclamation:* All factions with Thread Resonance ≥ 2 this season: Church may open a Heresy Investigation against them (no order required). TC +1.
- *Crusade Authority:* Templar units deployed this season: Cohesion check immune for 1 battle.
- *Papal Dispensation:* Cancel one Secular Authority card or Parliamentary Manoeuvre effect this season. TC +1.

**HAFENMARK (3 cards):**
- *Precedent Citation:* One opposing faction's Domain Action this season: delayed to next season's accounting (as Parliamentary Manoeuvre, but no roll required). Discard after use.
- *Merchant Navy:* Hafenmark may place Trade orders in sea-adjacent territories without a March order to reach them. Valid this season only.
- *Constitutional Standing:* One Heresy Investigation targeting Baralta: closed without resolution. Church Mandate −1.

**VARFELL (3 cards):**
- *Comovement Reading:* Reveal the top 3 Co-Movement cards. Return them in any order. Do not draw from deck this season — instead, choose one of those 3 when a Thread operation occurs.
- *Einhir Archive Access:* +1 TK immediately. If TK ≥ 3: may ask the GM (or read the top Seasonal Event card) before committing orders this season.
- *Calculated Withdrawal:* Varfell units that withdraw from any battle this season: no Supply or Overextended penalty. Varfell Stability +1.

**GUILDS (3 cards):**
- *Price Cartel:* All Trade orders in Guild-controlled territories this season: only Guilds may achieve Overwhelming (all others cap at Success).
- *Chartered Protection:* One territory: Guilds units cannot be targeted by Sabotage or Assassination orders this season.
- *Debt Leverage:* Name one faction. That faction: Wealth −1 immediately or they cannot Trade this season. Guilds Wealth +1.

**NIFLHEL (4 cards — one per network arm):**
- *Sollvik Move:* Sollvik network executes one order outside Niflhel's assigned territory this season (no adjacency requirement, Intel vs Ob 2).
- *Hafenbund Slip:* One Compromise token on any Niflhel arm: removed immediately. Discard after use.
- *Bernweg Contract:* One faction pays 1 Wealth to Niflhel or takes Grievance Marker. Niflhel does not need to use an order.
- *Stiltsift Discovery:* Learn all pending Orders of one faction before they are revealed this planning phase.

**[EDITORIAL: Confirm political card approach and review card text for balance/setting fit. The 4-arm Niflhel card approach may need simplification.]**

---

### MP-06: SOLO MODE — Valoria Against the Clocks
**Addresses:** G-BG-06

**Solo Mode premise:** The player controls one faction and attempts to meet their victory condition before the clocks overwhelm. All other factions run on enhanced NPC AI. The solo player's challenge is managing three simultaneous pressures: their own victory path, the clock trajectories, and opposing NPC faction interference.

**Solo modifications:**
- Player controls one faction using standard rules.
- NPC factions execute 3 orders per season per existing NPC AI trees.
- **Clock Escalation:** At season 8, all clocks gain +1 passive movement per season on top of normal triggers. Represents the world accelerating toward crisis without PC-level intervention.
- **Solo Victory:** Player meets their standard victory condition while shared survival condition holds (RS > 20, TC < 80, IP < 80).
- **Solo Loss:** Any clock reaches game-end threshold, OR player's faction reaches Stability 0.
- **Difficulty:** Easy = no Clock Escalation; Normal = Clock Escalation at Season 8; Hard = Clock Escalation at Season 5; Expert = Clock Escalation at Season 3 + one NPC faction targets player faction by priority.

**Recommended factions for solo:**
- **Hafenmark** (TC brake; defensive mechanics; highest solo viability)
- **Varfell** (intelligence advantage; information asymmetry is strongest in solo)
- **Guilds** (economic engine; clock management through Trade)

**Not recommended solo:**
- **Crown** (too dependent on inter-faction relationships)
- **Niflhel** (passive RS degradation makes solo morally uncomfortable; mechanically feasible but thematically incoherent — Niflhel alone cannot win)

---

### MP-07: SEASONAL ATTRITION CYCLE — Rhythm
**Addresses:** G-BG-07
**Inspired by:** Bretwalda

**Annual Attrition (at Round 4 / Year End accounting):**
- Each unit that fought in at least one battle this year: Cohesion check Ob 1. Failure: Cohesion −1.
- Units at Cohesion 2 or below: may be retired (removed) and replaced by a fresh unit at Muster cost −1 Ob next season.
- Units that did not fight: no Cohesion check.

**Effect:** Veteran units slowly wear down. Keeping a large army at peak costs constant muster investment. Idle armies stay intact but eventually need refreshing. Creates a strategic rhythm: build, fight, rebuild.

**Canon compliance:** Unit attrition is a rendered-world military consequence. PASS.

---

### MP-08: CRISIS RESPONSE — Collective Clock Management
**Addresses:** G-BG-08
**Inspired by:** Arydia

**Crisis Response** is a shared action available during Seasonal Accounting only. It requires at least 2 participating factions.

**Procedure:**
1. Any faction may propose a Crisis Response during Accounting by announcing the clock (RS, TC, or IP) and contributing at least 1 Wealth.
2. Other factions may join by contributing Wealth (minimum 1 each).
3. Total Wealth contributed: roll Influence vs Ob = threshold distance ÷ 10 (round up, minimum Ob 1).
4. Result:
   - **Overwhelming:** Clock moved back by total contributing factions (e.g., 3 factions contribute = clock moves −3).
   - **Success:** Clock moved back by contributing factions ÷ 2 (round up).
   - **Partial:** Clock unchanged; Wealth returned.
   - **Failure:** Wealth lost; clock moves forward by 1 (the response backfired).

**RS Crisis Response:** Use collective Thread Resonance (sum of all participating factions' TR) instead of Influence vs Ob. RS is not a political problem — it requires proximity to Thread events.

**Canon compliance:** Collective political action (TC/IP) via Influence roll: PASS. Collective Thread response (RS) via TR pool: consistent with P-01 (inseparability — collective rendered-side attention to Thread conditions is meaningful). PASS.

---

### MP-09: HYBRID ZOOM-IN TRIGGERS — Defined Conditions
**Addresses:** G-BG-09

The following BG events **mandate** a TTRPG scene if any PC-affiliated faction is involved. GM may also call a Zoom-In for any of these at their discretion.

| Trigger | TTRPG Scene Type |
|---------|-----------------|
| A Co-Movement card draws a Thread Resonance ≥ 3 event in a PC's home territory | Personal Thread encounter |
| A Heresy Investigation is opened against a PC's character | Personal/Social Scene |
| A Battle occurs in a territory where a PC has stated presence | Combat Scene |
| RS drops below 40 for the first time | Thread Awareness Scene (mandatory for all practitioners) |
| IP crosses 30 (Torben Demand) and Torben is a PC or PC-adjacent | Personal Decision Scene |
| Löwenritter Coup Tracker reaches 4 | Political Crisis Scene |
| Any named NPC's Belief is challenged by a BG order outcome | Social Scene |
| Rupture Condition approached (RS < 10) | Thread Emergency Scene |

**Domain Echo (existing mechanic — reinforce):** A PC in a BG-phase Personal Scene may execute one Domain Echo order (Priority 5, after all BG resolution) representing their personal agency within the strategic phase. This is the mechanical bridge from TTRPG to BG.

---

### MP-10: INFORMATION ASYMMETRY — Thread Veil Cards
**Addresses:** G-BG-10
**Inspired by:** Dune (treachery cards), Inis (hidden information)

**Thread Veil cards** (one per faction, sealed face-down at game start) contain one hidden capability or fact about the faction:

- Crown: *"The Crown holds a sealed Altonian peace offer: once per game, IP −3 immediately if revealed."*
- Church: *"The Church's Reliquary contains a Threadweaved artefact. Church may spend this card: +3 TC immediately but RS −2."*
- Hafenmark: *"Baralta's lineage includes Einhir ancestry (TS potential). TR cap raised to 6 for Hafenmark this game."*
- Varfell: *"Vaynard's Collection contains an entity configuration fragment. Once revealed: Varfell may declare a Thread operation (Investigate-level) in any territory."*
- Guilds: *"The Guilds fund a spy in every faction. Once per game: reveal any one faction's complete stat block to all players."*
- Niflhel: *"The Stiltsift arm has a Threadweaved smuggling route through the Southernmost. Reveal: Niflhel RS cost on operations reduced to 0 for 2 seasons (but RS −2 immediately for the revelation)."*
- Revolution: *"Edeyja has agreed to attend one community Weaving. Once per game: Revolution Community Weaving auto-Success (no roll required)."*
- Löwenritter (if independent): *"Ehrenwall's investigation files contain evidence of the 218 AG assassination. Reveal: one named faction takes Mandate −2 and Coup Counter +2."*

**Rules:**
- Cards are kept face-down throughout the game.
- A faction may reveal their Thread Veil card at any time during Seasonal Accounting.
- Once revealed, the effect fires immediately.
- Unrevealed cards score 0 VP but are visible to all as "this faction has not revealed their secret."
- **Niflhel exception:** Niflhel's Thread Veil is known to them at game start. All other factions only know their own card.

**Canon compliance:**
- Hafenmark Einhir ancestry: P-08 (epistemological barrier — having TS potential is not the same as having Thread capability). The TR cap raise is a sensitivity marker, not operational Thread access. PASS.
- Niflhel reduced RS cost: this is a mechanical representation of supply chain efficiency, not Thread capability. PASS.
- Church Reliquary: Thread-weaved artefact used by non-practitioners is consistent with the setting (Church suppresses but also exploits). PASS.

**[EDITORIAL: Thread Veil card content for all factions — setting decisions involved (particularly Baralta's Einhir lineage as a new lore element, and the 218 AG assassination card content).]**

---

## GT-01/02/03 INTEGRATION STATUS

### GT-01: Seasonal Event Cards C-11–C-20
Approved 2026-03-30. Content in `designs/generation_tasks_gt01_gt02_gt03.md`.
**Action required:** Append C-11–C-20 to B9 in stage_bg. Update Event Deck description from "30 cards" to "40 cards" (20 seasonal + 5 RS + 5 TC + 5 IP threshold cards → but confirm: are threshold cards separate from the 30 described?).

**[GAP: Event deck math needs reconciliation. B9 says "30 cards: clock-triggered events + random seasonal events." Current: 5 RS + 5 TC + 5 IP = 15 threshold; 15 random seasonal = 30 total. GT-01 adds 10 more seasonal cards → deck becomes 40 total, or replace 10 of the 15 seasonal with new ones. User decision needed.]**

**[EDITORIAL: Confirm event deck size expansion (30→40) or replacement of 10 existing seasonal cards.]**

### GT-02: Co-Movement Cards CM-11–CM-20
Approved 2026-03-30. Content in `designs/generation_tasks_gt01_gt02_gt03.md` and `designs/batch_e_designs.md`.
**Action required:** Add CM-11–CM-20 to B7 in stage_bg. Update deck description from "20 cards" to either 25 (add) or 20 (replace CM-11–15). 

**[EDITORIAL: Confirm 25-card deck (CM-01–CM-25) vs replace CM-11–15 with CM-11–CM-20.]**

### GT-03: Monstrous Entity Compound Thread Operation Tables
Approved 2026-03-30. Content in `designs/generation_tasks_gt01_gt02_gt03.md`.
**Action required:** Add as B11 (Entity Encounter Rules) in stage_bg — currently BG mode has no entity encounter procedures, which is a gap since RS degradation can trigger monstrous incursions.

---

## CANON COMPLIANCE SUMMARY

| Proposal | P-01 | P-07 | P-08 | P-11 | P-14 | Verdict |
|----------|------|------|------|------|------|---------|
| MP-01 Mandate Dice | n/a | PASS | n/a | n/a | n/a | PASS |
| MP-02 Deal Tokens | n/a | n/a | n/a | n/a | n/a | PASS |
| MP-03 Deed Tokens | n/a | n/a | n/a | n/a | n/a | PASS |
| MP-04 Thread Resonance | PASS | PASS | PASS | PASS | PASS | PASS |
| MP-05 Political Hands | n/a | n/a | n/a | n/a | n/a | PASS |
| MP-06 Solo Mode | n/a | n/a | n/a | n/a | PASS | PASS |
| MP-07 Seasonal Attrition | n/a | PASS | n/a | n/a | n/a | PASS |
| MP-08 Crisis Response | PASS | n/a | PASS | n/a | PASS | PASS |
| MP-09 Zoom-In Triggers | n/a | n/a | n/a | n/a | n/a | PASS |
| MP-10 Thread Veil Cards | PASS | n/a | PASS | n/a | PASS | PASS (with flags) |

---

## EDITORIAL FLAGS (new, surfaced this session)

| ID | Item | Blocking? |
|----|------|-----------|
| BG-E-07 | MP-01: Confirm Mandate Dice vs flat orders (structural change) | Yes — before implementation |
| BG-E-08 | MP-02: Secret Agreement card content per faction | Yes — before implementation |
| BG-E-09 | MP-05: Political Hand card text review (18 cards) | Yes — before implementation |
| BG-E-10 | MP-10: Thread Veil card content — particularly Baralta Einhir lineage and 218 AG card | Yes — lore decisions |
| BG-E-11 | GT-01 event deck size: expand to 40 or replace 10 cards | Yes — before integration |
| BG-E-12 | GT-02 co-movement deck: 25 cards or replace CM-11–15 | Yes — before integration |
| BG-E-13 | GT-03 entity encounters: confirm B11 addition to stage_bg | Low — additive |
| BG-E-14 | Solo mode: confirm recommended/not-recommended faction list | Low |

---

## IMMEDIATE NON-EDITORIAL ACTIONS (can proceed without approval)

1. **Fix G-BG-12** (Church TC expansion gap): Add explicit rule for Church territorial expansion between TC 40–70 into stage_bg B3/B8.
2. **Fix G-BG-13** (Formation Break reset): Replace "Reset Health to full" with "Reset Health to Resilience+3 (half Health)" to prevent infinite Formation Break cycling.
3. **Fix G-BG-14** (Thread Wound territory): Add rule to B2 specifying RS passive cost for extended occupation of T12/T13.
4. **Integrate MP-09** (Zoom-In Triggers): Add B12 section to stage_bg with Hybrid Interface rules.
5. **Integrate MP-07** (Seasonal Attrition): Add to B6 as Year-End procedure.
6. **Integrate MP-08** (Crisis Response): Add to B4 Phase 5 (Seasonal Accounting) as optional collective action.
7. **Integrate MP-03** (Deed Tokens): Add victory sub-conditions to each faction card in B3; specify Deed Token procedure in B10.

---

## PRIORITY ORDER FOR NEXT WORK

| Priority | Item | Type | Editorial? |
|----------|------|------|-----------|
| 1 | Fix G-BG-11 (integrate GT-01/02/03) | Integration | Needs BG-E-11/12 resolved |
| 2 | Fix G-BG-12/13/14 (Church gap, Formation Break, Thread Wound) | Mechanical fix | No |
| 3 | Integrate MP-03 (Deed Tokens) | Mechanic addition | No |
| 4 | Integrate MP-07/08/09 (Attrition, Crisis Response, Zoom-In) | Mechanic addition | No |
| 5 | BG-E-07 (Mandate Dice decision) | Editorial | Yes |
| 6 | BG-E-09/10 (Political Hands, Thread Veil) | Editorial | Yes |
| 7 | BG-E-06 (Revolution player victory) | Editorial | Yes |
| 8 | BG-E-02/03 (TK5, Rupture narrative) | Editorial | Yes |

---

*Analysis complete. Non-editorial fixes and mechanic additions can proceed to stage_bg on user confirmation.*
*All proposals are canon-compliant or flagged for canon review before implementation.*
