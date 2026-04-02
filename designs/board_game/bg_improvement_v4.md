# VALORIA BOARD GAME — IMPROVEMENT ANALYSIS V4
## Date: 2026-03-31
## Builds on: bg_improvement_v1.md, v2.md, v3.md
## Games: Barrage, Gaia Project, Concordia, Andromeda's Edge, Mythic Battles, Inventors of the South Tigris, Uprising: Blessings, Flooruler, Iocus Arcanus, BORD

---

## KNOWLEDGE CONFIDENCE DECLARATION

| Game | Confidence | Notes |
|------|-----------|-------|
| Barrage | High | Aporta Games heavy euro; construction wheel, water-flow cascade, executive officers |
| Gaia Project | High | Z-Man; space/terraforming; research tracks, federation networks, round scoring tiles |
| Concordia | High | PD-Verlag; card-hand action economy; no dice; Mercur reset; card-market development |
| Andromeda's Edge | Medium | Cardboard Alchemy 2023/24; asymmetric factions, card-driven; limited mechanic detail |
| Mythic Battles: Pantheon | Medium | Monolith; Greek mythology; tile arena; Olympus track; wound states |
| Inventors of the South Tigris | Medium | Osprey Games; South Tigris series; rotational worker placement; pattern invention |
| Uprising: Blessings | Low | Cannot verify specific title reliably — flagged below |
| Flooruler | Low | Cannot verify — flagged below |
| Iocus Arcanus | Low | Cannot verify — flagged below |
| BORD | Low | Cannot verify — flagged below |

---

## KNOWLEDGE GAP DECLARATION

**Uprising: Blessings, Flooruler, Iocus Arcanus, BORD:** I cannot produce reliable mechanic descriptions for these titles. Producing analysis from unverified descriptions would be confabulation. If these are:
- Published games I'm not trained on: provide the core mechanic and I'll apply it immediately.
- Games you're developing or prototyping: even more reason to describe them directly — I'll map them to Valoria with full context.
- A test of whether I'll fabricate: I won't.

Describe any of the four and I'll fold them into this document or a follow-up patch.

---

## LANDMARK GAME ANALYSIS — FOURTH WAVE

| Game | Core Mechanic | Valoria Application |
|------|--------------|---------------------|
| **Barrage** | Construction wheel: used actions unavailable for N turns; water-flow cascade; executive officer specials | Action Wheel cooldowns for powerful abilities; upstream/downstream territory chains |
| **Gaia Project** | Research tracks (6 axes) with breakthrough bonuses; round scoring tiles change each round; federation network bonuses; terraforming cost asymmetry per faction | Faction Research Tracks; variable round objectives; territory network scoring |
| **Concordia** | Cards ARE actions; hand = action menu; market purchases expand hand; Mercur card = full reset; no randomness | Card-Hand Action System replacing Order tokens; market-driven faction development |
| **Andromeda's Edge** | [Partial] Asymmetric faction cards; edge territory pressure; card-driven action selection | Noted; applying general asymmetric card-driven framing |
| **Mythic Battles** | [Medium] Olympus divine intervention track; wound states (down vs destroyed); figure drafting | Active threshold invocation; Champion wound states (extends MP-25) |
| **Inventors of South Tigris** | [Medium] Rotational worker placement (orientation = action type); pattern-matching for inventions; guild tracks | Order Orientation system; invention-style tech unlock patterns |

---

## MECHANIC PROPOSALS — FOURTH WAVE

### MP-29: ACTION WHEEL — Barrage Construction Wheel
**Addresses:** G-BG-01 (action economy flat), spammable abilities
**Inspired by:** Barrage (construction wheel — used actions rotate off, unavailable for N turns)

Barrage's construction wheel is one of the most elegant action-rationing mechanics in heavy euros. When you take a major action, the tile representing that action advances on a rotation wheel. It won't be available again until enough wheel-steps pass. You're always choosing between the action you *want* and the action that's currently *available*.

**Valoria Action Wheel:**

Each faction has a **Cooldown Track** (3 slots, labeled 1–3) for their Unique Power. After using their Unique Power, a faction places it on slot 3. At each Seasonal Accounting, all items on the Cooldown Track advance by 1. When an item reaches slot 0 (exits the track), it returns to available.

Standard orders (Govern, March, Trade, etc.) do NOT go on the Cooldown Track. Only Unique Powers and exceptionally powerful actions do.

**Default cooldowns per faction:**

| Faction | Unique Power | Cooldown |
|---------|-------------|---------|
| Crown | Royal Decree | 2 seasons |
| Church | Excommunication | 3 seasons (severe; Church must be deliberate) |
| Hafenmark | Sovereign Authority | Game-once (already, per B3) — no change |
| Varfell | Private Collection | 1 season (already per-season; cooldown = same) |
| Guilds | Economic Leverage | 1 season |
| Niflhel | Quiet Network (Assassination mode) | 3 seasons; other modes: 1 season |

**Extended cooldowns for proposed mechanics:**
- MP-27 Crown Policies: same Policy cannot repeat for 2 seasons (wheel replaces the text rule)
- MP-25 Champion Renown abilities: Renown 5 abilities go on 3-season cooldown after use
- MP-24 Attention threshold responses (Church player only): Crusade declared → 4-season cooldown

**Why this is better than Order Fatigue (MP-13):**
- More transparent: the wheel is a physical object showing exactly when abilities return
- Targets the right thing: Unique Powers (the actual spam-risk), not standard orders
- Simpler to apply: one wheel per faction, not 6 fatigue markers per order type

**Recommendation:** Adopt MP-29 as the action-rationing mechanic; set aside MP-13 (Order Fatigue) unless playtesting reveals standard order spam is also a problem.

**Canon compliance:** PASS.

---

### MP-30: RESEARCH TRACKS — Gaia Project
**Addresses:** G-BG-05 (faction asymmetry), long-term faction development
**Inspired by:** Gaia Project (6 research tracks, breakthrough bonuses at specific levels)

Gaia Project gives every faction 6 research axes they can advance (Terraforming, Navigation, AI, Gaiaforming, Economy, Science). Advancing costs resources; breakthroughs at levels 3 and 5 give significant bonuses. Critically: different factions have *different starting positions* on different tracks, and different costs to advance. The research tracks ARE faction asymmetry expressed as ongoing development.

This supersedes or refines MP-15 (Nippon Development Tracks). MP-15 proposed two tracks (IC/EP). Gaia Project suggests three is the optimal number — enough variation without tracking overhead.

**Valoria Research Tracks (3 per faction, faction-specific axes):**

Each track runs 0–5. Starts at position given. Advances via specific order types (1 step per successful order of that type). Breakthrough bonuses at levels 3 and 5.

---

**CROWN Research Tracks:**

| Track | Advances via | L3 Bonus | L5 Bonus |
|-------|-------------|---------|---------|
| *Mandate Authority* | Decree orders, Parliamentary sessions | All Govern orders: Ob −1 | Royal Decree cooldown reduced to 1 season |
| *Military Tradition* | Muster + March orders | Unit cap +2 | Champion gains Renown at double rate |
| *Diplomatic Legacy* | Diplomacy Overwhelming successes | Reputation loss events: −1 severity | Crown may invoke one alliance without a Deal Token |

Starting: Mandate Authority 2, Military Tradition 1, Diplomatic Legacy 1.

---

**CHURCH Research Tracks:**

| Track | Advances via | L3 Bonus | L5 Bonus |
|-------|-------------|---------|---------|
| *Doctrinal Reach* | Preach orders + TC-generating events | TC generated by Preach: +0.5/season | Heresy Investigations auto-open on any Thread op in Church territory |
| *Militant Order* | Templar deployment + battle victories | Templar Cohesion cap raised to 7 | Excommunication cooldown reduced to 2 seasons |
| *Inquisition Network* | Inquisition orders + Heresy Investigations opened | Attention Pool thresholds trigger 1 step earlier | Heresy Investigation Ob reduced by 1 across all investigations |

Starting: Doctrinal Reach 2, Militant Order 1, Inquisition Network 2.

---

**HAFENMARK Research Tracks:**

| Track | Advances via | L3 Bonus | L5 Bonus |
|-------|-------------|---------|---------|
| *Constitutional Precedent* | Parliamentary Manoeuvre successes | One Parliamentary ruling per game: cannot be overturned | Sovereign Authority: may be used once per game AND once more at TC 50+ |
| *Maritime Commerce* | Trade in coastal territories | Trade in Hafenvalor/Lowenskyst: auto-Success on any non-Failure | Schoenland trade route: Hafenmark earns +1 Wealth regardless of IP status |
| *Civic Stability* | Govern orders at Overwhelming | TC Suppression: active even at Mandate 3 | Baralta: Heresy Investigation requires Church Mandate 5+ to open |

Starting: Constitutional Precedent 1, Maritime Commerce 3, Civic Stability 1.

---

**VARFELL Research Tracks:**

| Track | Advances via | L3 Bonus | L5 Bonus |
|-------|-------------|---------|---------|
| *Einhir Knowledge* | Private Collection + Overwhelming Intel vs Thread sites | TK gain rate: +1 additional per qualifying source | At TK 5: Varfell may execute one Mend-equivalent operation (RS +1, no Thread Debt) |
| *Intelligence Network* | Intel orders + revealed faction stats | All Intel: Partial counts as Success | One faction's stats permanently visible to Varfell at all times (choose at L5) |
| *Analytical Method* | Diplomacy + observing faction decisions | Varfell may see one other faction's face-down orders before they flip | Varfell Secondary Objective revealed to them at game start AND they see one other faction's Secondary Objective |

Starting: Einhir Knowledge 1, Intelligence Network 2, Analytical Method 2.

---

**GUILDS Research Tracks:**

| Track | Advances via | L3 Bonus | L5 Bonus |
|-------|-------------|---------|---------|
| *Market Penetration* | Trade orders + Guild Favour accumulation | Guild Favour cannot drop below 2 in any territory | Economic Leverage: no Wealth cost; available every season |
| *Contract Law* | Successful Contracts (MP-26) + Diplomacy | Contracts: 2 issued per season instead of 1 | Contracts: breach costs the breaching faction 2 Wealth (enforceable) |
| *Supply Chain* | Trade in 3+ territories same season | Supply line range +2 for all Guild units | Guilds Wealth floor: cannot drop below 3 regardless of events |

Starting: Market Penetration 2, Contract Law 1, Supply Chain 2.

---

**NIFLHEL Research Tracks:**

| Track | Advances via | L3 Bonus | L5 Bonus |
|-------|-------------|---------|---------|
| *Network Depth* (or MP-18 equivalent) | Intel + Smuggle orders in new territories | Network may operate 2 territories from any controlled territory | Network Depth max raised to 4 per territory |
| *Operational Security* | Successful Quiet operations without detection | Compromise token removal: automatic after 2 seasons without detection | Niflhel cannot receive more than 2 Compromise tokens simultaneously |
| *Shadow Economy* | Wealth generated from covert sources | RS passive cost from operations: 0 in seasons where Wealth ≥ 6 | Stiltsift arm: operates completely independently of Compromise on other arms |

Starting: Network Depth 2, Operational Security 2, Shadow Economy 1.

---

**Round Scoring Tiles (Gaia Project variable objectives):**

At game start, deal 3 **Season Objective tokens** face-down, placed on rounds 4, 8, and 12. At the start of those rounds, flip the token — it reveals a scoring bonus for that season:

| Token | Bonus (apply at Accounting this round) |
|-------|----------------------------------------|
| *Martial Prestige* | +1 VP per territory held with Fortification ≥ 2 |
| *Commercial Dominance* | +1 VP per 2 Wealth held above your starting Wealth value |
| *Thread Stability* | +2 VP if RS is higher this round than it was at last Season Objective |
| *Political Influence* | +1 VP per faction you have a non-broken Pledge with |
| *Scholarly Progress* | +2 VP per Research Track at level 3+ |
| *Military Reach* | +1 VP per territory containing your units that is NOT your home territory |

Season Objectives create emergent mid-game goals that shift play. A player trailing on their primary victory path may focus on Season Objectives to stay relevant.

**Canon compliance:** Research tracks represent faction institutional development. Season Objectives are rendered-world political/economic assessments. PASS.

---

### MP-31: CARD-HAND ACTION SYSTEM — Concordia
**Addresses:** G-BG-01 (action economy), G-BG-05 (asymmetry), information asymmetry
**Inspired by:** Concordia (cards ARE actions; hand = available moves; no randomness)

Concordia is the most elegant action economy design in the genre. There are no dice. Your hand of cards is your complete list of available actions. Playing a card executes its action AND removes it from your hand. The only way to get your cards back is the Mercur card — which is itself a turn. The market sells additional card types that expand your action vocabulary permanently.

This is the cleanest solution to the "flat action economy" problem and directly competes with MP-01 (Mandate Dice) and MP-11 (Lead/Follow). Unlike those, it requires no randomness and offers perfect information about your own future capability.

**Valoria Card-Hand System:**

Each faction starts with a base hand of **6 Action Cards** (faction-specific mix). Additional cards are purchased from a shared **Senate Market** (6 cards face-up; 1 new card added each season from the Senate Deck).

**Base hand per faction (6 cards):**

| Card Type | Action |
|-----------|--------|
| *Legionary* (×2) | Military action (March or Muster) |
| *Consul* (×1) | Domain action (Govern or Trade) |
| *Senator* (×1) | Social action (Diplomacy or Preach/Decree) |
| *Prefect* (×1) | Domain in ALL territories you control simultaneously (weaker version: each territory rolls at Ob +1, but one roll covers all) |
| *Mercur* (×1) | Retrieve all played cards. No other action. |

**The Mercur equivalent is critical.** In Concordia, playing Mercur is a full turn sacrifice to reset your hand. In Valoria: playing the Mercur-equivalent (called **Recess**) costs the faction 1 Wealth AND 1 season — but returns all played cards. Without Recess, your hand depletes. With Recess, you sacrifice tempo.

**Senate Market cards (purchasable — cost 1–3 Wealth depending on card):**

| Card | Action | Cost |
|------|--------|------|
| *Tribune* | Covert/Intel action | 1 |
| *Architectus* | Fortify + Govern in same territory | 2 |
| *Colonist* | March + Govern in destination territory | 2 |
| *Diplomat* | Diplomacy at −1 Ob | 1 |
| *Tribune Militum* | Military at −1 Ob | 2 |
| *Aedile* | Trade at −1 Ob | 1 |
| *Pontifex* | Thread operation (Revolution/affiliated only) | 2 |
| *Praetor* | Place a Project marker (MP-21) | 1 |
| *Censor* | Issue a Crown Policy (Crown only) or block one order (non-Crown) | 3 |

**Faction starting hands express character:**
- Crown: 2 Legionary, 1 Consul, 1 Senator, 1 Prefect (all territories), 1 Recess — standard governance toolkit
- Church: 2 Senator, 1 Pontifex (free), 1 Consul, 1 Legionary, 1 Recess — social/doctrine heavy
- Hafenmark: 2 Consul, 1 Senator, 1 Legionary, 1 Diplomat (free), 1 Recess — commerce/law heavy
- Varfell: 2 Tribune (Intel), 1 Legionary, 1 Consul, 1 Colonist (free), 1 Recess — information focus
- Guilds: 2 Consul, 1 Aedile (free), 1 Tribune Militum, 1 Diplomat, 1 Recess — commercial
- Niflhel: 3 Tribune, 1 Legionary, 1 Consul, 1 Recess — covert heavy

**Key design properties inherited from Concordia:**
- No randomness in action availability — your hand is known to you.
- Expanding your hand by buying Senate cards IS your development path.
- Other players can see which Senate cards you've purchased — partial information asymmetry.
- The Recess decision (when to reset) is the central tension of every faction's turn.

**Relationship to other proposals:**
- MP-31 replaces MP-01 (Mandate Dice) and MP-11 (Lead/Follow) as the action economy solution.
- MP-29 (Action Wheel) for Unique Powers is compatible with MP-31 — the Unique Power is a card in your hand that goes on cooldown after use.
- Research Tracks (MP-30) could unlock additional Senate cards or reduce their purchase cost.

**Recommendation:** MP-31 is the highest-quality action economy proposal across all four waves. If one structural change is made to the board game, this should be it. The elegance of "your hand is your capability" maps perfectly to the setting — a faction's political options are exactly what their institutional capacity allows, no more.

**[EDITORIAL: MP-31 is the most significant structural change proposed. It replaces the entire Order token system. Recommend confirming as the action economy direction before any other action economy proposals (MP-01, MP-11, MP-13) are developed further.]**

**Canon compliance:** PASS.

---

### MP-32: WOUND STATES FOR CHAMPIONS — Mythic Battles
**Addresses:** G-BG-05 (asymmetry), Champion system depth (extends MP-25)
**Inspired by:** Mythic Battles: Pantheon (figures have wound states: standing, knocked down, destroyed)

In Mythic Battles, figures are not simply alive-or-dead. They have intermediate states: standing (full capacity), knocked down (reduced capacity, can be recovered), or destroyed (removed). The knocked-down state creates tactical decisions about when to press an advantage vs consolidate.

For Valoria Champions (MP-25), extend the Champion token states:

**Champion States:**
| State | Condition | Effect |
|-------|-----------|--------|
| *Active* | Default | Full Champion bonuses apply |
| *Wounded* | Loses a battle in their territory with their units | Champion bonuses halved (round up); Renown gain paused |
| *Captured* | Enemy takes the territory while Champion is Wounded | Champion removed from board; no bonuses; held by enemy |
| *Convalescing* | Returned from capture or rescued | Champion returns to home territory; 2 seasons to recover to Active (no bonuses during recovery) |

**Recovery from Wounded:** One Govern order in Champion's territory while no active enemy military presence → Champion returns to Active.

**Olympus Track equivalent (Mythic Battles divine intervention):**

Mythic Battles has an Olympus track where divine cards can be played to intervene in battles. In Valoria, the **Belief Intervention** mechanic maps this:

Each Champion has stated Conviction (already on faction cards). Once per game, a Champion's Conviction may be invoked at Renown 3+ to trigger a **Belief Intervention** — a narrative-mechanical moment where the Champion's deepest belief causes an extraordinary action:

- Almud (Order): When Valorsplatz is threatened, invoke for free Reinforcement: 1 unit teleports from any controlled territory to Valorsplatz.
- Himlensendt (Faith): When TC is about to drop below 40, invoke: Church may immediately Preach in any 2 territories without order slots.
- Baralta (Order): When Heresy Investigation is opened against her, invoke: Investigation requires 2 consecutive seasons of Church Mandate 5+ to proceed (one season's Mandate drop resets it).
- Vaynard (Reason): When Varfell is threatened militarily, invoke: All Intel orders this season reveal their result to Varfell regardless of success level.

**[EDITORIAL: Belief Intervention content — narrative/setting decisions per Champion.]**

**Canon compliance:** Champion wound states are rendered-world physical consequences. Belief Intervention expresses Conviction as mechanical force — consistent with how the setting treats personal ethical frameworks as having real-world effects. PASS.

---

### MP-33: ORDER ORIENTATION — Inventors of the South Tigris
**Addresses:** G-BG-01 (action economy), sub-action variety
**Inspired by:** Inventors of the South Tigris (worker rotation — orientation of placement = action type)

In the South Tigris games, your workers can be placed in different orientations (which direction they face), and the orientation determines what sub-type of action they execute. One worker slot accessed four different ways gives you four distinct actions from one component.

For Valoria, **Order Token Orientation** gives each Order token two modes based on placement:

When placing an Order token, the player rotates it to face **inward** (toward home territory) or **outward** (toward other territories). The orientation changes the sub-type:

| Order | Inward Orientation | Outward Orientation |
|-------|--------------------|---------------------|
| Military | Muster (raise unit at home) | March (move unit to adjacent territory) |
| Domain | Govern (consolidate control) | Trade (generate Wealth) |
| Intel | Investigate (learn own territory state) | Spy (learn enemy territory or stat) |
| Social | Decree/Parliamentary (internal policy) | Diplomacy (inter-faction negotiation) |
| Thread | Mend (restore RS at current site) | Weave (affect distant territory) |

**Effect:** Each faction has the same 5 Order tokens but 10 functional actions. No additional complexity — just a rotation decision at placement. Players who forget to orient: default to Inward.

**Interaction with MP-31 (Concordia card system):** If MP-31 is adopted, Order Orientation becomes the sub-type selector within a card's action. Playing a *Legionary* card + Outward orientation = March; Inward = Muster. The Concordia system handles *which* action domain; orientation handles *which sub-type*.

**Canon compliance:** PASS.

---

## SYNTHESIS AND RECOMMENDATION UPDATE

After four analysis waves, the action economy landscape has three competing proposals:

| Proposal | Complexity | Randomness | Setting Fit | Recommendation |
|----------|-----------|-----------|-------------|----------------|
| MP-01: Mandate Dice | Medium | Yes | Good (Mandate = capacity) | Set aside — randomness adds variance without depth |
| MP-11: Lead/Follow | Medium | No | Excellent (political reaction) | Keep as a modifier layer, not replacement |
| MP-31: Concordia Cards | High (setup) | No | Excellent (capability = what you've built) | **Primary recommendation** |
| MP-33: Orientation | Low | No | Good | Compatible with MP-31 as sub-type selector |

**Recommended action economy stack:**
1. **MP-31** (Card-Hand) as the core action system
2. **MP-33** (Orientation) as the sub-type selector within cards
3. **MP-11** (Lead/Follow) as a resolution modifier when factions play the same card type in the same tier
4. **MP-29** (Action Wheel) for Unique Powers / Cooldowns

This stack gives the game a deep, no-randomness action economy where a faction's capability is literally what they've built (their card hand), expressed at two levels of specificity (card type → orientation), with political reaction dynamics during resolution (Lead/Follow).

---

## EDITORIAL FLAGS ADDITIONS (V4)

| ID | Item | Blocking? |
|----|------|-----------|
| BG-E-30 | MP-31: Concordia Card-Hand adoption — replaces entire Order token system | Yes — highest-priority structural decision |
| BG-E-31 | MP-30: Research Track advancement values and starting positions | Yes |
| BG-E-32 | MP-30: Season Objective tile distribution and content | Low |
| BG-E-33 | MP-32: Belief Intervention content per Champion | Yes |
| BG-E-34 | Uprising: Blessings, Flooruler, Iocus Arcanus, BORD — describe mechanics for application | Pending user input |

---

## TOTAL PROPOSAL REGISTER (all waves)

**V1 (Dune, ASOIAF, Inis, Bretwalda, WotR, Root, Arydia, Pax Pamir):** MP-01 through MP-10
**V2 (Arcs, Anachrony, Ark Nova, Nippon, Pendragon, Malifaux, Hegemony, Cloudspire, Terra Mystica):** MP-11 through MP-20
**V3 (Quiet Year, Nemesis, HoMM, New Cold War, Crisis, Kingdoms Forlorn, Eldfall):** MP-21 through MP-28
**V4 (Barrage, Gaia Project, Concordia, Mythic Battles, Inventors):** MP-29 through MP-33

**Total: 33 proposals.**

**Already integrated into stage_bg (no editorial needed):**
MP-03 (Deed Tokens), MP-04 (Thread Resonance), MP-07 (Annual Attrition), MP-08 (Crisis Response), MP-09 (Zoom-In Triggers), B11 (Entity Encounters), B12 (Hybrid Interface), fixes G-BG-12/13/14

**Ready to integrate (no editorial needed, awaiting go-ahead):**
MP-12, MP-14, MP-16, MP-22, MP-24, MP-26, MP-27, MP-29, MP-30 (tracks without starting value decisions), MP-33

**Require editorial decisions before integration:**
MP-01/11/31 (action economy — choose one stack), MP-02, MP-05, MP-06, MP-10, MP-15, MP-17, MP-18, MP-19, MP-20, MP-21 (project content), MP-23, MP-25 (Niflhel champion), MP-28, MP-30 (starting values), MP-31 (adoption), MP-32 (belief interventions)
