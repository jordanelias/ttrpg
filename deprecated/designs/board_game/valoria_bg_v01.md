<!-- DEPRECATED: 2026-04-09 — SUPERSEDED BY designs/board_game/valoria_bg_v05_simulation_and_patches.md. Do not use as a mechanical reference. Retained for audit trail only. -->

# VALORIA: THE BOARD GAME
## Skeleton Ruleset v0.1
**Date:** 2026-04-01  
**Authority:** Audit + Consolidation (2026-04-01) is authoritative. bg_improvement_v3_amendment2.md highest-priority source. Mass Battle v3 and GT-01–GT-03 approved.  
**Scope:** System reduction analysis → pared system set → skeleton ruleset → full review

---

# PART A — SYSTEM REDUCTION ANALYSIS

## A.1 Full Proposal Register with Disposition

All 33 proposals (MP-01–MP-33) plus 3 synthesis additions (MP-34–36) evaluated against:
- Audit findings (contradictions resolved by authority)
- Canon compliance (bg_improvement_review.md independent assessment)
- Cognitive load target: ≤20 core player-facing systems
- The correction that BG is mandatory standalone AND hybrid layer

### CUT — Removed from consideration

| ID | Proposal | Reason |
|----|----------|--------|
| MP-01 | Mandate Dice | Randomness in action selection contradicts TTRPG's deterministic capability structure. Superseded by MP-31. |
| MP-13 | Order Fatigue | Superseded by MP-29 (Action Wheel). MP-29 is more transparent and correctly targeted. |
| MP-15 | Development Tracks (Nippon IC/EP) | Superseded by MP-30. |
| MP-17 | Fate Cards | Metaphysically incoherent in Valoria — "cheat fate" has no referent in the Foundations. Hard cut. |
| MP-19 | Token Commitment (Cloudspire) | Double-jeopardy without setting justification. Rendered-world failure consequences are already present. |

**Additionally cut from action economy stack:** MP-11 (Lead/Follow) deferred to Advanced Rules. The card-hand + orientation stack is already the deepest permitted layer. Adding a resolution modifier compounds cognitive load without adding emergent texture at core play level. Restore in advanced/expansion.

---

### KEPT — Core system set (20 systems)

| # | ID | System | Layer | Notes |
|---|----|--------|-------|-------|
| 1 | MP-31 | Card-Hand + Recess | Action Economy | Foundation of all player agency. Hand = capability. |
| 2 | MP-33 | Order Orientation | Action Economy | Sub-type selector on cards. Inward/Outward. Low overhead. |
| 3 | — | Senate Market | Action Economy | Hand expansion = faction development. 9 purchasable card types. |
| 4 | MP-29 | Cooldown Track | Action Economy | 3-slot wheel for Unique Powers. Transparent rationing. |
| 5 | — | Three Clocks (RS/TC/IP) | Victory/Loss | Existing. RS metaphysically primary; TC/IP politically co-equal. |
| 6 | — | Clock Environmental Effects | Ambient Modifier | All three clocks modify action Obs. New requirement (Amendment 1). |
| 7 | MP-03 | Deed Tokens | Victory | Visible sub-condition tracking. From Inis. |
| 8 | MP-36 | Hollow Victory Scoring | Victory | End-game modifier. Elevated to T1 (Amendment 1). |
| 9 | MP-34 | Institutional Mandate (Uphold/Compromise) | Political | BG equivalent of Belief. Faction identity with mechanical teeth. |
| 10 | — | Standing Tokens | Political | Merged Contempt + Leverage. Political grievance/capital economy. |
| 11 | MP-27 | Crown Policy | Political | Crown as policy actor affecting all. 6 policy instruments. |
| 12 | — | Parliament Integrity | Political | Shared institution (0–10). Hafenmark's primary lever. |
| 13 | MP-04 | Thread Resonance (TR) | Thread | Environmental sensitivity (capped at TR 3 for non-sensitives — P-08 fix). |
| 14 | MP-12 | Thread Debt | Thread | Temporal cost with residual RS degradation (P-11 fix). |
| 15 | MP-24 | Church Attention Pool | Thread | Consequence-detection, not operation-detection (P-08 fix). |
| 16 | — | Co-Movement Card Deck (20 cards + GT-02 additions) | Thread | P-14 compliance. Three-dimensional consequence per Thread operation. |
| 17 | MP-21 | Community Projects | Faction/Thread | Multi-season investments. Quiet Year mechanic. |
| 18 | MP-25 + MP-32 | Champions + Wound States | Military | Named leaders as mobile tokens. 4 states. Hybrid bridge. |
| 19 | MP-30 | Research Tracks (2 per faction) | Progression | Long-arc faction development. No randomness. |
| 20 | MP-18 | Faction Structural Asymmetry | Faction | Church TC-currency, Restoration Movement Presence, Niflhel Network Depth, Guilds Contractor |

**Faction-specific private tracks** (faction mat complexity, not board complexity — do not count against core system limit):
- VTM: Varfell Thread Mastery Track (Amendment 2)
- RDT: Hafenmark Reformed Doctrine Track (Amendment 2, replaces Ecclesiastical Claim)
- TD: Hafenmark Theological Dissatisfaction, private (Amendment 2)
- AER: Church Altonian Ecclesiastical Relationship (Amendment 2)

---

### KEPT — Advanced/Variant Rules (not in skeleton core)

| ID | System | When Active |
|----|--------|------------|
| MP-23 | Secondary Objectives | Default BG; disable in hybrid |
| MP-26 | Proxy Support | Advanced |
| MP-10 | Thread Veil Cards | Advanced (remove Baralta Einhir lineage card — P-08 fail) |
| MP-02 | Deal Tokens (sealed pledges) | Advanced negotiation variant |
| MP-20 | Winter Accounting / Leader Age | Long campaign only |
| MP-05 | Political Hand Cards | Variant (merge with Senate Market if adopted) |
| MP-06 | Solo Mode | Variant |
| MP-28 | Unit Identity / Naming | Flavour; one property per unit type |
| MP-11 | Lead/Follow Resolution | Advanced layer |

---

### MODIFIED — Applied with fixes from bg_improvement_review.md

| ID | System | Fix Applied |
|----|--------|-------------|
| MP-04 | Thread Resonance | TR 4–5 effects for non-sensitive factions removed. TR 4–5 available only to Restoration Movement, Varfell (VTM ≥ 2), or any faction with a TS-qualified agent present. |
| MP-12 | Thread Debt | Repaying debt reduces penalty rate but leaves permanent residual RS −0.5 per token ever incurred (accumulates to whole numbers at Year-End). Debt cannot be fully discharged. |
| MP-16 | Conviction/Belief | Renamed Resonant Styles to political terminology in BG context. Almud's approach: "Precedent" (not Consequence). Vaynard's: "Investigation" (not Evidence). Same mechanic, clean epistemic boundary. |
| MP-18 | Restoration Movement | Must have two distinct action types: Community Weaving (Thread, with co-movement) AND Community Organizing (rendered-world political/social, no Thread operation). Not Thread-only. |
| MP-24 | Church Attention Pool | All triggers rewritten as consequence-detection, not operation-detection. Church sees social indicators and behavioral anomalies, not Thread events directly. |

---

## A.2 The Canonical System Architecture

Arranged by player cognitive engagement (what you track simultaneously during a season):

```
BOARD STATE (public, visible)
├── Territory map: control, Prosperity, Fortification, Champions, Presence Markers
├── Three Clocks: RS (100→0), TC (0→100), IP (0→100)
├── Parliament Integrity track (0–10)
└── Church Attention Pool (0–10, resets each season)

FACTION MAT (private to player)
├── Card Hand (6 starting cards + purchased cards)
├── Cooldown Track (3 slots)
├── 2× Research Tracks (faction-specific, 0–5)
├── Deed Track (faction-specific conditions)
├── Standing Tokens (held)
└── Private tracks: VTM / RDT / TD / AER (faction-dependent)

SHARED LEDGER / REFERENCE
├── Community Project Progress Tracks
├── Coup Counter (Löwenritter NPC, 0–4)
├── Restoration Movement Presence Markers (per territory)
├── Niflhel Network Depth (per territory)
└── AER track (Church + Altonia relationship, 0–5)

REFERENCE CARDS (consult, don't track)
├── Clock Environmental Effects table
├── Co-Movement card resolution rules
├── Order resolution procedure
└── Hollow Victory modifiers
```

---

# PART B — SKELETON RULESET v0.1

---

## B1 — OVERVIEW

**Valoria: The Board Game** is a standalone political-strategic game for 2–7 players (1 in solo mode) set on the Valorian peninsula. It is also the strategic layer of hybrid TTRPG/board game play.

**Three mandatory game modes:**
- **Board Game (this ruleset):** Complete standalone game, 2–4 hours, 3–5 seasons per session.
- **Hybrid:** BG as strategic layer feeding into TTRPG personal-scale scenes. See Part B13.
- **TTRPG:** Governed by separate compiled stages.

**Core feel:** Powerful institutions trying to manage a world that is quietly dying. The Thread substrate degrades (RS). The Church consumes governance legitimacy (TC). An outside power watches for weakness (IP). No faction wins by expanding — they win by holding on long enough, coherently enough, while the three clocks count down.

**Player count:**
| Players | Mode |
|---------|------|
| 1 | Solo (see Advanced Rules) |
| 2 | Competitive asymmetric; NPC AI runs remaining factions |
| 3–5 | Competitive-cooperative; NPC AI runs remainder |
| 6 | Full faction coverage (Crown, Church, Hafenmark, Varfell, Guilds, Niflhel) |
| 7 | Full coverage + Restoration Movement (optional 7th player) |

Schoenland: always NPC-controlled.  
Löwenritter: always NPC-controlled (partial sheet until coup trigger).  
Restoration Movement: NPC-controlled by default; optional 7th player faction.

---

## B2 — THE BOARD

### Territory Map

15 territories in adjacency layout (north-south peninsula axis). Each territory has: controlling faction marker, Prosperity value (1–7), Fortification level (0–4), and may have: Project markers, Presence markers, Champion token, unit tokens.

| # | Territory | Start Control | Pros | Fort | Special |
|---|-----------|--------------|------|------|---------|
| 1 | Valorsplatz (Capital) | Crown | 6 | 2 | Royal Court: Crown Policy −1 Ob. Parliament: Hafenmark Mandate orders −1 Ob. |
| 2 | Gransol | Crown | 5 | 1 | Garrison: Muster here +1D. |
| 3 | Himmelenger | Church | 5 | 2 | Grand Cathedral: TC +1/season Church controls. Church Unique Power −1 Ob here. |
| 4 | Spartfell | Crown | 3 | 2 | Altonian Border: IP threshold events here first. Invasion entry point. |
| 5 | Arnesheld | Crown/Löwenritter | 4 | 3 | Löwenritter Fortress: Martial Law −1 Ob. Fort max 4. |
| 6 | Hafenvalor | Hafenmark | 6 | 1 | Ducal Court: Sovereign Authority Doctrine here only. Major port. |
| 7 | Lowenskyst | Hafenmark | 5 | 0 | Trade Hub: all Trade +1D. Schoenland sea route. |
| 8 | Eidursjo | Guilds | 4 | 0 | Difficult terrain: March costs 2 movement. Guilds Trade +1D. |
| 9 | Varfell | Varfell | 4 | 1 | Varfell Seat: private Research here only. Einhir ruins: Restoration Weaving −1 Ob. |
| 10 | Sigurdshelm | Niflhel | 3 | 0 | Black Market: Niflhel Covert −1 Ob. All Trade +1 Ob. |
| 11 | Halvardshelm | Guilds | 5 | 0 | Breadbasket: +1 Prosperity/season uncontested. Muster Ob −1. |
| 12 | Oastad | Uncontrolled | 3 | 0 | Thread Wound: RS thresholds trigger +10 early here. RS −1/season after 2 consecutive seasons of any occupation. |
| 13 | Stillhelm | Uncontrolled | 2 | 0 | Southernmost Access: required for Expedition. Non-Thread orders +1 Ob. RS −1/season any occupation. |
| 14 | Eisengrund | Restoration (informal) | 4 | 0 | Einhir Heartland: Restoration Influence −1 Ob. Church Influence +1 Ob. |
| 15 | Schoenland | Neutral | 5 | 1 | Altonian Trade. At IP ≥ 75: Altonian vanguard deploys. Intel orders here: visible to Altonia. |

### Clock Tracks

**RS (Thread Substrate Integrity):** Starts at 72. Counts down toward 0. RS Rupture at 0 = shared loss.  
**TC (Theocratic Clock):** Starts at 15. Counts up toward 100. TC 80 = Church Territorial Seizure event. TC 100 = Holy State endgame.  
**IP (Invasion Pressure):** Starts at 20. Counts up toward 100. IP 75 = Altonian Vanguard deployed.  
**Parliament Integrity:** Starts at 7. Counts 0–10.

### Clock Environmental Effects

All three clocks modify the action environment. These apply continuously to all territorial orders in affected conditions.

**RS Environmental Effects:**
| RS Range | Effect |
|----------|--------|
| 72–50 | No modifier |
| 49–30 | Thread operations: −1 Ob (community urgency). Non-Thread orders in T12/T13: +1 Ob |
| 29–20 | As above. Entity encounters possible in T12/T13. Muster all territories: +1 Ob |
| Below 20 | All orders all territories: +1 Ob. Community Projects advance +1/season. Entity encounters expand |

**TC Environmental Effects:**
| TC Range | Effect |
|----------|--------|
| Below 30 | No modifier |
| 30–49 | Church orders: −1 Ob in Church-held territory. Secular Diplomacy: no modifier |
| 50–69 | Church orders: −1 Ob everywhere. Non-Church Diplomacy targeting Church: +1 Ob. Mandatory Church Assert/Suppress choice each season |
| 70+ | As above. Church Territorial Seizure protocol active. AER begins modifying TC gains |

**IP Environmental Effects:**
| IP Range | Effect |
|----------|--------|
| Below 30 | Trade with Schoenland: +1D (stable relations) |
| 30–59 | Trade with Schoenland: +1 Ob (Altonian scrutiny). All factions: +1D to Intel orders (information flows freely) |
| 60–74 | Trade disrupted: Schoenland Trade +2 Ob. Schoenland NPC funds proxy operations: +1D to military at T4 (Border Pass) |
| 75+ | Altonian Vanguard deployed. Invasion countdown begins |

---

## B3 — ACTION ECONOMY

The Card-Hand system (MP-31, Concordia) is the action economy foundation. There are no Order tokens. Your hand of Action Cards is your complete list of available actions this season. Playing a card executes its action and removes it from your hand until Recess.

### Base Hand (6 cards per faction)

All factions start with 6 cards. Faction starting compositions express institutional identity:

| Card Type | Action Domain | Action (determined by Orientation) |
|-----------|--------------|--------------------------------------|
| **Legionary** | Military | Inward: Muster (raise unit in territory). Outward: March (move units to adjacent territory). |
| **Consul** | Domain | Inward: Govern (consolidate control, Prosperity). Outward: Trade (generate Wealth). |
| **Senator** | Social | Inward: Decree / Parliamentary Manoeuvre. Outward: Diplomacy (inter-faction negotiation). |
| **Tribune** | Intel/Covert | Inward: Investigate (learn own territory state). Outward: Spy (learn enemy stat or territory). |
| **Prefect** | Domain (broad) | Govern in ALL controlled territories simultaneously (each at Ob +1). Orientation does not apply. |
| **Recess** | — | Retrieve all played cards. Costs 1 Wealth. No other action this card-play. |

**Starting hands by faction:**
| Faction | Hand Composition |
|---------|-----------------|
| Crown | 2× Legionary, 1× Consul, 1× Senator, 1× Prefect, 1× Recess |
| Church | 2× Senator, 1× Pontifex (free), 1× Consul, 1× Legionary, 1× Recess |
| Hafenmark | 2× Consul, 1× Senator, 1× Legionary, 1× Diplomat (free), 1× Recess |
| Varfell | 2× Tribune, 1× Legionary, 1× Consul, 1× Colonist (free), 1× Recess |
| Guilds | 2× Consul, 1× Aedile (free), 1× Tribune Militum, 1× Diplomat, 1× Recess |
| Niflhel | 3× Tribune, 1× Legionary, 1× Consul, 1× Recess |

**Restoration Movement (NPC / optional 7th player):** 2× Organizer (Community Organizing action), 1× Weaver (Community Weaving action — Thread), 1× Presence Spread (move Presence markers), 1× Project (start/advance Community Project), 1× Recess. No Legionary. No Muster.

### Order Orientation (MP-33)

When playing a card, rotate it Inward or Outward before resolving. Inward = home-focused sub-action. Outward = external sub-action. See table above. Players who forget to declare: default Inward.

### Senate Market (Card Development)

6 cards face-up from Senate Deck. One new card added each season. Purchase during Diplomacy card resolution (or as a designated Buying phase — confirm at playtesting). Cost in Wealth.

| Card | Action | Cost |
|------|--------|------|
| Tribune | Covert/Intel action | 1 |
| Architectus | Fortify + Govern in same territory | 2 |
| Colonist | March + Govern in destination | 2 |
| Diplomat | Diplomacy at −1 Ob | 1 |
| Tribune Militum | Military at −1 Ob | 2 |
| Aedile | Trade at −1 Ob | 1 |
| Pontifex | Thread operation (Restoration Movement / Thread-qualified only) | 2 |
| Praetor | Start or advance a Community Project | 1 |
| Censor | Crown only: issue one Policy. Non-Crown: block one order this season | 3 |

Purchasing a card permanently adds it to your hand (it is available after next Recess).

### Cooldown Track (MP-29)

Each faction has a 3-slot Cooldown Track for their Unique Power card. After use, place Unique Power on Slot 3. At Seasonal Accounting, all cooldown items advance one slot. At Slot 0 (exits track): card returns to hand and is available again.

Default cooldowns:
| Faction | Unique Power | Cooldown |
|---------|-------------|---------|
| Crown | Royal Decree | 2 seasons |
| Church | Excommunication | 3 seasons |
| Hafenmark | Sovereign Authority Doctrine | Once per game (not on cooldown track) |
| Varfell | Private Collection | 1 season |
| Guilds | Economic Leverage | 1 season |
| Niflhel | Quiet Network: Assassination mode | 3 seasons; other modes 1 season |
| Löwenritter | Martial Law | 2 seasons |

Crown Policies: same policy may not repeat for 2 seasons (tracked on Cooldown Track using policy tokens, not the Unique Power slot).

---

## B4 — TURN STRUCTURE

Each game round = 1 season. A full campaign = 12–20 seasons. Standard session: 3–5 seasons.

### Phase 1 — Planning (simultaneous, ~5 min)
All players simultaneously select cards from their hand and place them face-down in the territories where they will act, with orientation chosen. Players may place up to 5 cards per season (hand may be smaller if depleted). Players may negotiate informally during planning.

NPC factions execute their AI priority trees (see B12) at the same time.

### Phase 2 — Negotiation (~3 min)
Players may make deals. Open deals: declared publicly (enforceable — breaking costs Standing −2 from the betrayed faction). Sealed deals: written privately (no enforcement). Orders remain face-down.

### Phase 3 — Reveal
All cards flipped simultaneously. Players see the board state.

### Phase 4 — Resolution (sequential, ~8 min)
Cards resolve in priority order. Within a priority tier, resolve by faction Stability (highest first within tier; ties: simultaneously).

**Resolution Priority Order:**
1. Intel/Covert (Tribune, Tribune operations) — information before action
2. Military (Legionary — March and Muster)
3. Domain (Consul, Prefect, Architectus, Colonist — Govern and Trade)
4. Social (Senator — Decree, Parliamentary Manoeuvre, Diplomacy)
5. Thread operations (Pontifex, Weaver)
6. Special/Unique Powers (Censor, Royal Decree, Excommunication, etc.)
7. Project advancement (Praetor)

**Resolution procedure per card:**
1. Declare orientation (Inward/Outward → specific action).
2. Assemble dice pool from appropriate faction stat.
3. Apply modifiers: Clock Environmental Effects, territory specials, ethical framework, Research Track bonuses, Champion presence.
4. Roll. Determine degree (Overwhelming/Success/Partial/Failure).
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

### Phase 5 — Seasonal Accounting (~5 min)

Execute in this order:
1. Apply all pending attribute changes from resolved orders.
2. Faction Stability checks for any faction that suffered attribute loss ≥ 2 this season (Ob = loss magnitude).
3. Advance Cooldown Track (all items move −1 slot; at 0: return to hand).
4. Clock advances: RS baseline drift (−1 at Winter only). TC per Church activity formula. IP per Altonian pressure table. Parliament Integrity changes.
5. Church Attention Pool: resolve threshold responses. Pool resets to 0.
6. Thread Debt: outstanding tokens older than 1 season: RS −0.5 per token (record as partial; apply as whole numbers at Year-End).
7. Check threshold events (RS/TC/IP threshold tables from Event Deck: draw one Event Card per threshold crossed this season).
8. Co-Movement secondary resolution: if RS crossed any threshold this season, all factions draw TR +1.
9. Check victory conditions (all Deed Tokens held simultaneously = declare victory).
10. Season marker advances. If Winter (every 4th season): Year-End Accounting (see B11).

---

## B5 — FACTION CARDS

### Resolution Pools

All rolls: pool = relevant faction stat (1–7 scale, same as TTRPG attribute). Dice: d6. Success = 4+ on each die. Surplus successes = Overwhelming. Each 1 rolled (when majority of dice show 1): Failure regardless of other dice.

**Ethical framework modifiers** apply before rolling:
- Crown (Virtue Ethics): public, visible, virtuous actions −1 Ob. Covert or morally ambiguous: +1 Ob.
- Church (Divine Command): doctrine-aligned −1 Ob. Thread-supporting: +2 Ob.
- Hafenmark (Categorical Imperative): procedurally grounded, precedent-following −1 Ob. Ad hoc or precedent-breaking: +1 Ob.
- Varfell (Reason): evidence-based Intel actions −1 Ob. Emotional/reactive orders: +1 Ob.
- Guilds (Contractual): agreed-contract-fulfilling actions −1 Ob. Unilateral, non-negotiated: +1 Ob.
- Niflhel (Act Consequentialism): any action with a net-positive Niflhel outcome −0 Ob (no modifier, all actions are equally valid to Niflhel by design). Self-sabotage: +1 Ob.
- Restoration Movement (Rawlsian): community-benefiting −1 Ob. Hierarchical or exclusionary: +1 Ob.

---

### FACTION: THE CROWN

**Stats:** Mandate 5 · Influence 5 · Wealth 4 · Military 4 · Stability 4  
**Ethical Framework:** Virtue Ethics  
**Leader:** King Almud Almqvist  
**Conviction:** [EDITORIAL BG-E-59 — proposed: "The state is the only legitimate vessel of order."]  
**Political Decision Style:** Precedent  

**Institutional Mandate:** "The monarchy provides the order that protects Valoria — and all other institutions serve the monarchy's order."  

**Mandate trigger events** (must Uphold or Compromise):
- Church refuses a Crown directive in Crown territory
- Varfell operates Intel without Crown awareness in Crown territory
- Hafenmark Parliamentary ruling contradicts Crown decree
- Any faction allies with Altonia without Crown approval

**Unique Power — Royal Decree:** Once per season (2-season cooldown). Roll Mandate vs Ob 2. Success: one faction attribute change (any faction, ±1) takes effect immediately rather than at accounting. Failure: Crown Mandate −1. Cannot target Intel. Effect declared before rolling.

**Crown-Exclusive — Policy Instruments:** Once per season (in addition to normal card plays), Crown may issue one Policy if Mandate ≥ 4. Same policy cannot repeat for 2 seasons.

| Policy | Effect | Downside |
|--------|--------|----------|
| Royal Taxation | All Trade this season: +1 Wealth to Crown | Non-Crown Trade Ob +1 |
| Conscription Mandate | All Muster orders: −1 Ob this season | Mustered units begin Cohesion −1 |
| Free Trade Decree | IP −1; Schoenland Trade +1D | Church TC +1 |
| Curfew | Intel/Covert in Crown territories: +2 Ob | Niflhel Leverage (Standing) +2 |
| Parliamentary Session | All factions: one additional Diplomacy this season | Crown Mandate check Ob 1 on failure |
| Emergency Powers | Crown executes one order face-down (revealed at resolution) | Hafenmark gets free Parliamentary Manoeuvre; Church TC +1; Baralta TD +1 |
| Supremacy Decree (once/game) | Named faction treats Crown Mandate as +2 higher for all opposed rolls this season | All other factions: Standing +1 vs Crown |

**Victory — Constitutional Stability (Primary):** 5 Deed Tokens + PI ≥ 3 simultaneously at accounting.

| Deed | Condition |
|------|-----------|
| 1 | Mandate ≥ 5 |
| 2 | Control Valorsplatz + Gransol + ≥ 2 other territories |
| 3 | TC < 60 and IP < 75 simultaneously |
| 4 | Parliament Integrity ≥ 5 |
| 5 | Torben Loyalty ≥ 5 |

**Victory — Dominion (Alternate):** Controls ≥ 8 territories AND achieves one Submission Condition.

| Submission Condition | How | Standing Cost |
|---------------------|-----|---------------|
| Church recognizes Crown supremacy over religious appointments in Crown territories | Deal Token (Open Pledge) accepted by Church, OR TC = 0 | +2 Standing vs Crown from Church; Baralta Mandate trigger |
| Varfell formally subordinates Intel to Crown oversight | Varfell Intel Research Track ≤ 1 OR Crown captures Vaynard + controls all Varfell territories | +1 Standing vs Crown from Varfell |
| Hafenmark surrenders Parliamentary independence | PI = 0 OR Baralta Compromise count ≥ 4 | +2 Standing vs Crown from Hafenmark; Riskbreakers Priority 2 fires against Crown |

---

### FACTION: THE CHURCH OF SOLMUND

**Stats:** Mandate 5 · Influence 6 · Wealth 5 · Military 4 · Stability 5  
**Ethical Framework:** Divine Command  
**Leader:** Confessor Arne Himlensendt  
**Conviction:** Faith  
**Political Decision Style:** Evidence  

**Institutional Mandate:** "Solmund's doctrine is the rightful framework for all governance — secular authority is derivative and conditional."

**Church-Exclusive — TC as Resource:** TC is simultaneously the Church's victory track AND their spending resource. Church may spend TC to amplify actions at a cost to their own victory condition. Spending TC: declared before rolling; −1 TC spent → +1D to any Church action. Maximum spend: 2 TC per roll.

**Church-Exclusive — Altonian Ecclesiastical Relationship (AER):** Shared ledger track, 0–5, starting at 2. See B6 for full rules. [EDITORIAL BG-E-61: confirm starting value.]

**Church-Exclusive — Mandatory Theocratic Assert/Suppress:** Each season TC > 50, Church must choose:
- **Assert:** TC +1. All secular faction Mandate triggers fire. Riskbreakers evaluate Priority 3.
- **Suppress:** TC +0. AER −1. Himlensendt Renown −1.
No neutral option. This choice is mandatory, announced at Phase 5 Accounting.

**Church-Exclusive — Inquisitors:** Unit type deployable via Inquisition card play (Senator Inward with Church unique flag). Once deployed in a territory: +2 to Attention Pool per season present. Can open Heresy Investigation without an additional card play. Moving an Inquisitor: requires Senator card.

**Unique Power — Excommunication:** Roll Mandate vs target leader's Mandate (or Ob 2 for non-leaders). 3-season cooldown. Overwhelming: target Mandate −1; target barred from Church territories 1 season; target Reputation −1 all factions. Success: Mandate −1 only. Failure: Church Mandate −1, target Mandate +1 (martyr sympathy).

**Victory — Holy State (Primary):** TC ≥ 70 + Mandate ≥ 5 + control Himmelenger + Valorsplatz + AER ≥ 3.

| Deed | Condition |
|------|-----------|
| 1 | TC ≥ 40 |
| 2 | Church Mandate ≥ 5 |
| 3 | Control Himmelenger continuously |
| 4 | Control Valorsplatz |
| (+) | AER ≥ 3 (gate condition — not a Deed, but required for victory declaration) |

**Victory — Dual Theocracy (Alternate):** TC ≥ 60 + AER = 5 + IP ≤ 30. Theological governance through diplomatic mastery, not military dominance.

---

### FACTION: HAFENMARK

**Stats:** Mandate 4 · Influence 4 · Wealth 5 · Military 3 · Stability 4  
**Ethical Framework:** Categorical Imperative  
**Leader:** Duchess Inge Baralta  
**Conviction:** [EDITORIAL BG-E-51]  
**Political Decision Style:** Investigation  

**Institutional Mandate:** "Constitutional process is the only legitimate source of authority."

**Hafenmark-Exclusive — Reformed Doctrine Track (RDT, 0–6):** Replaces Ecclesiastical Claim entirely. Measures spread and credibility of Reformed Doctrine (direct access to Solmund, without Church mediation).

**Gaining RDT:**
- Senator card (Outward/Diplomacy) in non-Church territory: theological outreach Ob 2. Success: RDT +1.
- TC rises above 50 AND Baralta has a unit in that territory: RDT +1 (Church overreach validates Reform).
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
| 3 | Church Inquisition Autonomy threshold: Attention Pool must reach 8 (not 7) |
| 4 | TC capped at current level + 5 for remainder of game |
| 5 | Reformed Settlement available (once/game) |
| 6 | All Diplomatic actions targeting Hafenmark: +1 Ob |

**Reformed Settlement (RDT 5):** Baralta declares the theological right of direct faithful access. Church must respond:
- **Resist:** TC +3; RDT +1 (martyrdom); Hafenmark +1 Standing, +1 Deed Token.
- **Accommodate:** TC −5; Church Mandate trigger; Church Stability −1 [EDITORIAL BG-E-50 Cardinal schism]; AER −2.
- **Ignore:** RDT +1 next season. [EDITORIAL BG-E-62: confirm three responses cover all canon outcomes.]

**Hafenmark-Exclusive — Theological Dissatisfaction (TD, 0–5, private):** Baralta watches Almud. Tracked privately on faction mat.

**Gaining TD:** Crown issues Emergency Powers (+1); Crown submits to Altonian pressure without resistance (+1); Crown fails to respond to Church incursion in Crown territory (+1).  
**Losing TD:** Almud issues Parliamentary Session (+TD −1); Crown collaborates with Hafenmark on policy (+TD −1).

**TD Effects (private track):**
| TD | Effect |
|----|--------|
| 0–2 | No effect |
| 3 | Hafenmark +1D Diplomatic actions targeting Crown |
| 4 | Baralta may declare Almud unworthy publicly: Crown −1 Deed Token; Hafenmark +1 Standing vs Crown |
| 5 | Rival Succession Claim: Hafenmark +1D all orders in Crown-adjacent territories; if Civil War fires, Hafenmark no Standing penalty for seizing Crown territories |

**Unique Power — Sovereign Authority Doctrine:** Once per game. Hafenvalor only. Roll Mandate vs Ob 4. Overwhelming: TC −3, Church Mandate −1, Heresy Investigation blocked this season. Success: TC −2, Church Mandate −1, Heresy Investigation opens against Baralta. Failure: TC +1, Investigation fires, Baralta Mandate −1.

**TC Passive Suppression:** While Baralta's Mandate ≥ 4: TC −1/season. Pauses if Mandate drops below 4.

**Victory — Reformed Valoria (Path A):** Reformed Settlement completed + PI ≥ 3 at game end + 3 Deed Tokens.  
**Victory — Theological Supremacy (Path B):** RDT = 6 + TD = 5 + 2 Deed Tokens.  
**Victory — Parliamentary Consolidation (Path C):** 4 Deed Tokens + PI ≥ 4.

---

### FACTION: VARFELL

**Stats:** Mandate 3 · Influence 4 · Wealth 3 · Military 4 · Intel 5 · Stability 4  
**Ethical Framework:** Epistemic Reason  
**Leader:** Vaynard  
**Conviction:** [EDITORIAL BG-E-53]  
**Political Decision Style:** Investigation  

**Institutional Mandate:** "Information is the truest form of power — and all other power is information in disguise."

**Varfell-Exclusive — Thread Mastery Track (VTM, 0–5):** Private at VTM 0–2; public (visible to all) at VTM 3+.

**Gaining VTM:**
- Tribune (Intel) card on Thread-active territory (TR ≥ 2): VTM +1.
- Southernmost Expedition season completed with Varfell unit in T13: VTM +1.
- Thread Debt incurred by any faction: VTM +1 (Vaynard perceives the substrate strain).
- Patience + Casus Belli combination in RS-affected territory: VTM +1.
- Riskbreakers expose a Vaynard Casus Belli: VTM −1.

**VTM Effects and Southernmost Access:**
| VTM | Access | Capability |
|-----|--------|-----------|
| 0–1 | None | — |
| 2 | First Layer (public at 3) | Varfell TR never capped below 3 |
| 3 | Deep Layer | Once/game: preview top 2 Co-Movement cards before an order; keep either |
| 4 | Deep Layer without Restoration guide | Patience Protocol max → 6; Casus Belli Ob −1 |
| 5 | Core zone | Once/game: choose outcome of one Co-Movement card draw. Produces Thread Debt token + RS −1. [EDITORIAL BG-E-63: P-14 compliance confirmation required] |

**Victory — Intelligence Hegemony (Path A):** Intel Research Track L5 + have revealed stats of all other factions at least once + 3 Deed Tokens + 3 territories controlled.  
**Victory — Southernmost Dominion (Path B):** Control T12–T13 + VTM ≥ 3 + Southernmost Expedition complete (any zone) + 2 Deed Tokens.  
**Victory — Thread Supremacy (Path C, hardest):** VTM = 5 + RS ≥ 50 + 3 territories including T13. RS ≥ 50 requires Vaynard has exploited the substrate without breaking it. This is the game's most difficult victory.

---

### FACTION: GUILDS

**Stats:** Mandate 3 · Influence 3 · Wealth 6 · Military 2 · Stability 4  
**Ethical Framework:** Contractual  
**Leader:** Guildmaster  
**Conviction:** Commerce  

**Institutional Mandate:** "Commerce is neutral; we serve whoever can pay."

**Guilds-Exclusive — No Standard Military:** Guilds cannot Muster or March standard units. Instead: pay 2 Wealth to immediately place one Hired Blade unit without a card play. Hired Blades: offensive only, 1-season duration, cannot garrison, cannot defend fortified positions, disappear at Accounting if Guilds Wealth < 4.

**Guilds-Exclusive — Contracts:** Once per season during Diplomacy, Guilds may issue 1 paid Contract to any faction: 1–3 Wealth sealed → that faction's chosen order this season resolves at +1D per Wealth spent. If Contract action succeeds: Guilds gain 1 Influence in territory. If faction refuses or fails: Wealth lost, relationship costs Standing −1.

**Unique Power — Economic Leverage:** 1-season cooldown. Guilds choose one faction. That faction's next Trade or Wealth gain: redirected to Guilds (equal amount). If faction has Military ≥ 4: they may retaliate without Casus Belli penalty next season.

**Victory — Commercial Dominance:** Active trade in 4+ territories + Wealth ≥ 8 + 3 Deed Tokens.

---

### FACTION: NIFLHEL

**Stats:** Mandate 2 · Influence 3 · Wealth 4 · Military 0 · Intel 6 · Stability 3  
**Ethical Framework:** Act Consequentialism  
**Leader:** None (headless structure)  
**Network Coordinator Card:** Face-down one-shot unique capability. Revealed once per game.  

**Institutional Mandate:** "Everyone serves their own interest; there is no other law."

**Niflhel-Exclusive — Network Depth:** Track per territory (0–3). Network Depth markers placed in territories represent Niflhel's operational capacity. Depth gained by: successful Intel/Covert in new territories, successful Quiet operations, Smuggle orders.

- Network Depth 1 in territory: Niflhel can execute one covert action per season there without using a card play.
- Network Depth 2: Actions in territory at −1 Ob.
- Network Depth 3: Niflhel learns all face-down orders placed in that territory before they flip.

**Niflhel-Exclusive — No Champion:** Network Coordinator card is face-down. Once per game, reveal it during Accounting to trigger its single-use capability (faction-specific powerful effect). [EDITORIAL BG-E-26 — content decision]

**RS Passive Cost:** Each territory where Niflhel operates covertly (Network Depth ≥ 1): RS −0.5 per season at Year-End accounting (accumulated; resolved as whole numbers). Niflhel's supply chain creates trace Thread disturbance.

**Victory — Network Supremacy:** Network Depth ≥ 2 in 6 territories + Intel Research Track L5 + 3 Deed Tokens.

---

### FACTION: RESTORATION MOVEMENT (NPC / Optional 7th Player)

**Stats:** Mandate 2 · Influence 3 · Wealth 2 · Military 0 · Stability 3  
**Ethical Framework:** Rawlsian  
**Leader:** Collective (no named Champion; Dahl Erikssen as informal figure)  

**Institutional Mandate:** "The community is the only legitimate political unit."

**Restoration-Exclusive — Presence Markers:** 8 total. Placed in territories; represent community organisation, not military control. One Presence Spread action (card play) moves markers into adjacent territories organically. Military force cannot remove Presence markers — only successful Heresy Investigations or Community Project disruption.

**Two Action Types (fix per bg_improvement_review.md):**
1. **Community Organizing** (Organizer card, rendered-world): Influence, advocacy, community development. Ob reduction by Presence density. No Thread operation. No co-movement.
2. **Community Weaving** (Weaver card, Thread operation): Ob 2, −1 Ob per Presence marker in territory. Always draws Co-Movement card. Always produces three-dimensional consequences.

**Community Projects:** Restoration Movement's primary engine. Projects are started with Praetor card (any faction) or Weaver card (Restoration); advanced each season by Restoration presence or Domain card from any faction. Disrupted by battle, control change, or Heresy Investigation.

**Victory (if played):** Restoration Network complete (5 Presence markers in 5 non-adjacent territories, maintained for 2 consecutive seasons) + RS ≥ 50 at game end. Alternatively: Co-Victory available with any faction that achieves Constitutional Stability while RS ≥ 50.

---

## B6 — THREAD SYSTEMS

### Thread Resonance (MP-04, fixed per bg_improvement_review.md)

TR is a per-faction track (0–5), temporary, resets to 0 at season end.

**TR accumulates when:**
- A Thread operation occurs in or adjacent to a faction's controlled territory: +1 TR
- A Co-Movement card affects the faction: +1 TR
- RS drops below a threshold this season: +1 TR all factions

**TR effects:**
| TR | Effect |
|----|--------|
| 0 | No effect |
| 1 | Thread Awareness: may look at top Co-Movement card once this season |
| 2 | Resonance: one card this season may be declared after seeing the Event Card |
| 3 | Sensitive Proximity: Intel orders gain +1D when targeting practitioners or Thread-active sites |
| 4–5 | Thread-qualified factions only (Restoration Movement, Varfell VTM ≥ 2, or faction with TS ≥ 30 agent present) |

**TR 4 (qualified factions):** Ask one yes/no question about RS (above/below threshold).  
**TR 5 (qualified factions):** Spend TR 5 to either: (a) cancel one Co-Movement card effect targeting them, or (b) contribute +1D to Restoration Community Weaving this season.

### Thread Debt (MP-12, fixed per bg_improvement_review.md)

When a Thread-qualified faction executes a Thread operation against temporal flow (or when Vaynard uses VTM 5): incur 1 Thread Debt token at −1 Ob.

**Thread Debt tokens:**
- At next Seasonal Accounting: faction may "service" the debt by executing a Mend-equivalent action (Restoration Weaver card in same territory, or spend 2 TR). Serviced token: reduces current RS penalty rate to 0 but leaves **residual RS −0.5 permanently** (recorded on faction ledger; becomes whole number at Year-End).
- Unserviced tokens: RS −1 per outstanding token per season (not residual — active drain).
- Maximum 3 Thread Debt tokens simultaneously. At 3: no further Debt incurrence until reduced to 2.
- Church may use outstanding Thread Debt as grounds for automatic Heresy Investigation: Ob −1 if target faction holds ≥ 2 tokens.

**Year-End Thread Debt resolution:** All residual RS fractions sum to whole number and apply to RS track.

### Church Attention Pool (MP-24, fixed per bg_improvement_review.md)

Tracks social indicators of Thread and heretical activity. **The Church detects consequences, not operations.**

**Pool accumulates from (consequence-detection framing):**
- Unauthorized community gathering reported in any territory: +1 Attention
- Unexplained structural/social change in territory (triggered by GM/NPC AI interpretation of Thread operation visible effects): +2 Attention
- Einhir artefact surfaces (Event Card C-13): +2 Attention
- Restoration community gathering in Church-adjacent territory: +3 Attention
- Faction behavior consistent with heretical influence in multiple territories: +1 Attention per territory showing behavioral anomaly

**Attention thresholds (pool resets each season):**
| Pool | Response |
|------|----------|
| 3 | Church opens one Heresy Investigation (free, no card play) |
| 5 | Church TC +1 |
| 7 | Inquisitor protocol: all Thread-active factions −1D to covert/Intel this season. Inquisition Autonomy threshold fires. (Modified to 8 if RDT ≥ 3) |
| 10 | Church Crusade: Templar units may deploy anywhere in Church territory without Muster card |

### Co-Movement Cards (P-14 compliance)

Every Thread operation draws one Co-Movement card. Cards produce consequences across three axes:
1. **Actualized dimension (RS):** RS change (positive or negative).
2. **Epistemic dimension:** Information revealed, concealed, or distorted.
3. **Temporal dimension:** History/continuity marker (Project disruption, Pledge complication, or NPC relationship change).

20-card base deck + GT-02 additions (approved). Cards are not optional. They cannot be cancelled except by TR 5 (Thread-qualified only).

---

## B7 — POLITICAL SYSTEMS

### Institutional Mandate — Uphold/Compromise (MP-34)

Each faction has a stated Institutional Mandate. When a trigger event occurs (faction card lists triggers), the faction must respond:

- **Uphold:** Act consistently with Mandate, even at cost. Earns 1 Renown on Champion + 1 Stability. No mechanical benefit from the triggering situation.
- **Compromise:** Act against Mandate for strategic advantage. Earns the mechanical benefit of the action. Costs: 1 Standing token (self-inflicted, visible to others) + 1 Stability.

In hybrid mode: if PC faction leader's personal Belief arc contradicts the faction's Uphold/Compromise pattern, Hollow Victory condition activates.

### Standing Tokens (merged Contempt + Leverage)

Standing tokens replace both Contempt and Leverage as a single unified economy.

**Gaining Standing against another faction:**
- That faction breaks an Open Pledge (deal in your favour)
- That faction executes Brutal disposition against Valorian civilians
- That faction seizes territory from you while you had a non-broken Pledge
- Church Excommunicates your faction leader
- That faction Compromises their Institutional Mandate publicly
- That faction's action directly targets you this season (defensive generation)

**Spending Standing:**
| Cost | Effect |
|------|--------|
| 1 Standing (yours) | +1D to any one defensive roll this season |
| 2 Standing | Execute one defensive order at Ob −1 |
| 3 Standing | Respond to an action targeting you (one out-of-priority defensive card play) |
| 4 Standing | Convert to 1 Wealth, 1 Mandate, or 1 Influence |

**Standing effects on others:**
- 3+ Standing against one faction from you: that faction's Diplomacy targeting you automatically fails
- 5+ Standing against one faction from you: that faction cannot ally with you or give you Deal Tokens

Standing against you is visible (physical tokens on your faction card). This creates political history.

### Parliament Integrity (PI, 0–10)

Shared institution tracking health of parliamentary governance. Starts at 7.

| PI | Effect |
|----|--------|
| ≥ 5 | Parliamentary Manoeuvres available to Hafenmark. Crown Policy requires Mandate ≥ 4. |
| 3–4 | Parliamentary Manoeuvres +1 Ob. Crown Policy Ob −1 (no check needed). |
| ≤ 2 | Parliament non-functional. Hafenmark loses Parliamentary Manoeuvre. Crown governs by decree. TC +2/season. |

**PI degrades:** Crown Emergency Powers (−1), Church Territorial Seizure (−1), Löwenritter Coup (−3).  
**PI recovers:** Hafenmark Parliamentary Manoeuvre success (+1), Crown Parliamentary Session policy (+1).

### Altonian Ecclesiastical Relationship (AER, 0–5)

Shared ledger track. Church's standing with Altonian power. Starts at 2. [EDITORIAL BG-E-61]

| AER | TC Effect | IP Effect |
|-----|-----------|-----------|
| 0–1 | No modification | IP escalates normally |
| 2 | Neutral | Neutral |
| 3 | TC environmental effects +1 level | IP vanguard threshold: 76 → 80 |
| 4 | TC gains > 3/season treated as +4 | Altonia will not invade |
| 5 | Once/game: any order targeting Church interests fails | IP set to 50 and held |

**AER gaining:** TC crosses 30/50/70 threshold (+1 each), successful Heresy Investigation removes Restoration Presence (+1), Church issues Interdict (+1).  
**AER losing:** TC drops below threshold (−1), Church Stability < 3 (−1), Reformed Settlement occurs at RDT 5 (−2).

---

## B8 — MILITARY

### Units

Each faction's Military stat = maximum active units simultaneously. Unit stats are Cohesion (1–5) and Martial (1–4).

| Type | Martial | Cohesion | Notes |
|------|---------|---------|-------|
| Standard | 2 | 3 | Default muster result |
| Elite | 3–4 | 4–5 | Requires specific conditions per faction |
| Hired Blade (Guilds) | 2 | 3 | Offensive only, 1-season duration |
| Knights Templar (Church) | 4 | 5 | Immune to Co-Movement Cohesion penalties; +2D vs practitioners |
| Inquisitors (Church) | 1 | 2 | Deploy via Senator Inward; +2 Attention Pool/season present |

**Mass Battle:** Per Mass Battle v3 (approved). BG resolution: Martial pool vs opposed Martial pool. Cohesion tracks unit health. Losing side: Cohesion −1 per defeat until 0 (destroyed). Winning side: Cohesion −0 unless Overwhelming failure. General (Champion or officer) modifies all rolls.

### Champions (MP-25, MP-32)

Named faction leaders as mobile tokens on the board.

**Champion States:**
| State | Condition | Effect |
|-------|-----------|--------|
| Active | Default | Full bonuses. +1D to all units in same territory. Diplomacy +1D. Stability checks −1 Ob. |
| Wounded | Lost a battle in their territory | Champion bonuses halved; Renown gain paused. Govern order in territory restores to Active. |
| Captured | Enemy takes territory while Champion is Wounded | Removed from board; no bonuses; held by enemy. Rescue: military action vs captor. Ransom: 3 Wealth. |
| Convalescing | Returned from capture | In home territory; 2 seasons to recover (no bonuses during). |

**Champion Renown (0–5):** Earned from victories, successful orders while present, Uphold events. Renown 3+ unlocks faction Unique ability. Renown 5: Conviction Intervention (once/game). [EDITORIAL BG-E-27, BG-E-33]

---

## B9 — RESEARCH TRACKS

Each faction has 2 Research Tracks (0–5). Advances via specific order types. Breakthrough bonuses at L3 and L5.

**Crown:**
| Track | Advances via | L3 | L5 |
|-------|-------------|----|----|
| Mandate Authority | Decree, Parliamentary Session | All Govern −1 Ob | Royal Decree cooldown → 1 season |
| Military Tradition | Muster + March | Unit cap +2 | Champion Renown gains at double rate |

**Church:**
| Track | Advances via | L3 | L5 |
|-------|-------------|----|----|
| Doctrinal Reach | Preach + TC-generating events | TC from Preach +0.5/season | Heresy Investigations auto-open in Church territory |
| Inquisition Network | Inquisition + Heresy Investigations | Attention Pool thresholds trigger 1 step earlier | Heresy Investigation Ob −1 |

**Hafenmark:**
| Track | Advances via | L3 | L5 |
|-------|-------------|----|----|
| Constitutional Precedent | Parliamentary Manoeuvre successes | One Parliamentary ruling irrevocable | Sovereign Authority: usable twice (second use at TC 50+) |
| Maritime Commerce | Trade in coastal territories | Hafenvalor/Lowenskyst Trade auto-Success on any non-Failure | Schoenland route: +1 Wealth regardless of IP |

**Varfell:**
| Track | Advances via | L3 | L5 |
|-------|-------------|----|----|
| Einhir Knowledge | Tribune (Intel) + Overwhelming Intel vs Thread sites | VTM gain rate +1/qualifying source | At VTM 5: one Mend-equivalent (RS +1, no Thread Debt) |
| Intelligence Network | Intel orders + revealed faction stats | Intel: Partial counts as Success | One faction's stats permanently visible |

**Guilds:**
| Track | Advances via | L3 | L5 |
|-------|-------------|----|----|
| Market Penetration | Trade + successful Contracts | Guild Favour cannot drop below 2 any territory | Economic Leverage: no Wealth cost, available every season |
| Contract Law | Successful Contracts + Diplomacy | 2 Contracts per season | Breach: breaching faction pays 2 Wealth (enforceable) |

**Niflhel:**
| Track | Advances via | L3 | L5 |
|-------|-------------|----|----|
| Network Depth | Intel + Smuggle in new territories | Network operates 2 territories from any controlled | Network Depth max → 4 per territory |
| Operational Security | Quiet ops without detection | Compromise token removes automatically after 2 seasons undetected | Cannot receive more than 2 Compromise tokens simultaneously |

---

## B10 — COMMUNITY PROJECTS

Projects are started in any territory with Presence. Progress Track of 1–5 (scope varies). Any faction with presence in the territory may advance it 1 step per season (costs Domain card for non-Restoration factions; free for Restoration Movement with Presence present).

**Disruption conditions:**
- Battle in territory: Progress −2
- Territory changes control: Progress −1
- Heresy Investigation active there: −1 per season (not stacking with battle)

**Project types (GT-01 approved — this expands the project menu):**

| Project | Scope | Completion Effect |
|---------|-------|------------------|
| Community Weave | 3 | RS +2; Restoration Influence +2 in territory; permanent Thread Resonance node (+1 TR/season here) |
| Einhir Memory Recovery | 4 | GM introduces historical fact about the Calamity; TK +1 any contributing faction; RS +1 |
| Restoration Network | 5 | Restoration gains Presence in 2 adjacent territories even if disrupted; IP −1 |
| Fortification (any faction) | 3 | Territory Fort +1 at no Wealth cost |
| Diplomatic Mission (any faction) | 2 | Faction Reputation +1 all factions; next Diplomacy −1 Ob |
| Southernmost Expedition (multi-season, faction-specific) | 4 | Per B11 |

---

## B11 — YEAR-END ACCOUNTING

Fires every 4th season.

1. **Annual Attrition (MP-07):** Each unit that fought ≥ 1 battle this year: Cohesion check Ob 1. Failure: Cohesion −1. Units at Cohesion 2 or below: may be retired; replacement at next Muster Ob −1.
2. **Sustenance:** Each military unit costs 1 Prosperity from controlling territory per year of active service. Territories below Prosperity 2: excess units disbanded.
3. **Thread Debt residuals:** Sum all residual RS fractions (0.5 per serviced Thread Debt token over game) → apply as whole-number RS loss.
4. **Niflhel RS passive drain:** −0.5 per Niflhel-operated territory (Network Depth ≥ 1) → apply as whole numbers.
5. **Thread Wound territories:** T12/T13 occupied ≥ 2 consecutive seasons by any faction: RS −1 per additional season.
6. **Stability Recovery:** Each faction that did not engage in military action this year AND has no active Heresy Investigation: Stability +1.
7. **Pledge accounting:** Any Open Pledges not honored: automatically exposed. Betrayed faction: Standing +2 vs betrayer.
8. **Research Track:** Confirm all track advances applied.
9. **AER adjustment:** Apply all end-of-year AER changes.
10. **Season Objective reveal** (at seasons 4, 8, 12): flip the face-down Season Objective token; apply its scoring bonus this season.

---

## B12 — VICTORY, DEED TOKENS, HOLLOW VICTORY

### Deed Tokens

Victory requires all Deed Tokens simultaneously at Seasonal Accounting — not just completing the last one. A Deed Token is placed when its condition is first met; removed immediately if the condition breaks. The race to hold all tokens at the same moment is the game's tension engine.

### Hollow Victory Scoring (MP-36)

At game end, after standard victory conditions are checked, apply:

**Legitimacy Modifiers (reduce final Deed count):**
- Each 2 Standing tokens held against you from other factions: −1 Deed
- Institutional Mandate publicly Compromised ≥ 3 times: −1 Deed
- RS below 20 at game end: all victories hollow regardless of Deed count (the world is dying)
- TC above 80 at game end: Church victory hollow unless Himmelenger + Valorsplatz controlled
- Any faction eliminated (Stability 0) by you: your victory −1 Deed

**Legitimacy Bonuses (increase Deed count):**
- Institutional Mandate upheld ≥ 5 times: +1 Deed
- RS above 60 at game end: all victories +1 Deed (world recovering)
- Zero Standing tokens held against you at game end: +1 Deed

**Cleanest victory:** Zero Standing tokens held, Mandate upheld throughout, RS above 60. This is the game's highest achievement. It is intended to be rare.

---

## B13 — NPC AI BLOCKS

### Löwenritter (Partial Sheet until Coup)

**Priority order (peacetime):**
1. If units in Arnesheld threatened: March to defend (Military Legionary Inward/Outward)
2. If TC > 50 and Church Mandate > Crown Mandate in any territory: issue Martial Law
3. If Crown orders in current season threaten Valorian sovereignty: declare opposition

**Coup Counter (0–4):** Advances by 1 when any coup trigger condition occurs:
1. Crown deposed
2. Foreign power controls Crown
3. TC ≥ 80 AND Church controls Crown-held territories
4. Crown formally subordinates to foreign power

At Coup Counter 4: Ehrenwall waits one season. If condition persists: Coup fires. Roll Military vs Ob 3. Success: Löwenritter gains full sheet, Mandate 3, Wealth 2 (from Crown). All factions receive Standing +1 vs Löwenritter.

### Riskbreakers (Always NPC, Always Covert)

3 tokens/year. Refresh at Year-End. Priority tree evaluated at Accounting in strict order:

| Priority | Condition | Intervention |
|----------|-----------|-------------|
| 1 | Vaynard has active manufactured Casus Belli | Expose fabrication: CB fails next season. Varfell +1 Standing from all. VTM −1. |
| 2 | Civil War active AND triggered by Vaynard CB | De-escalate: one faction's Military next season +2 Ob in most contested territory. PI +1. |
| 3 | Church seized Crown-controlled territory AND TC > 60 | Sabotage governance: territory Prosperity −1; Church Govern there +1 Ob next season. |
| 4 | Löwenritter Coup Counter = 3 AND Condition 4 approaching | Intercept: diplomatic action that would trigger Condition 4 fails. No faction absorbs Standing. |
| 5 | Any faction's Military targets civilian community with Restoration Presence | Intervene: Military +1 Ob; if fails, Restoration gains Presence in adjacent territory. |
| 6 (default) | None above | Observe. Crown player receives 1 revealed intelligence: hidden stat of faction acting most against Valoria's interests. |

**Riskbreakers vs Crown (Almud Dominion path):** If Almud Mandate ≥ 6 AND Emergency Powers issued ≥ 2 times: Priority 2 may fire against Crown's own military orders.

**Riskbreakers vs Vaynard (Riskbreaker File):** Each prior Vaynard CB that Riskbreakers exposed: next exposure costs −1 token (file deepens). Each failed exposure at VTM 4+: exposure Ob +1.

### Schoenland (Active Spoiler)

At each Accounting:
- IP 30+: fund proxy at T4 Border Pass → +1D any faction's Military orders there
- TC 50+: provide intelligence to anti-Church factions
- RS < 40: do nothing (doesn't understand Thread substrate)
- No active conflict this season: IP +1 (funding border provocations to maintain arms market)
- AER ≥ 3: active hostility to Baralta's Reformed movement

### Restoration Movement (when NPC)

**Priority order:**
1. Spread Presence to any territory with RS < 40 (urgent community organizing)
2. Advance highest-progress Community Project
3. Move Presence to territory with active Heresy Investigation (supporting the investigated)
4. Start new Community Weave in Einhir Heartland territory (T14 priority)
5. Community Organizing in any contested territory

---

## B14 — HYBRID INTERFACE

### Zoom-In Triggers

The following BG events mandate a TTRPG scene if any PC-affiliated faction is involved (GM may call at discretion):

| BG Event | Scene Type |
|----------|-----------|
| Co-Movement card draws TR ≥ 3 event in PC's home territory | Personal Thread encounter |
| Heresy Investigation opened against PC or PC-adjacent NPC | Personal/Social scene |
| Battle in territory where PC has stated presence | Combat scene |
| RS drops below 40 (first time) | Thread Awareness scene (all practitioners mandatory) |
| IP crosses 30 AND Torben is PC or PC-adjacent | Personal Decision scene |
| Löwenritter Coup Counter = 4 | Political Crisis scene |
| Named NPC's Conviction challenged by BG order outcome | Social scene |
| Any faction reaches a Hollow Victory state | Belief Crisis scene |
| Riskbreakers intercept a Vaynard CB | Hidden conflict scene (Vaynard POV or Riskbreaker POV) |
| Reformed Settlement declared (RDT 5) | Theological Crisis scene |

### Cascade Phase Card Effects (MP-35)

After personal scenes resolve in hybrid play, BG card economy effects apply:

| Personal Scene Outcome | Cascade Effect |
|-----------------------|---------------|
| PC achieves Belief this season | Add one free Senate card to faction hand (no Wealth cost) |
| PC's Belief challenged but engaged | Recess cost → 0 Wealth this season |
| PC executes successful Thread operation | Faction's Pontifex card available even if on Cooldown |
| PC fails Thread operation catastrophically | Pontifex goes on Cooldown Track (2-season cooldown) |
| PC Wounded in personal combat | Champion enters Wounded state on BG board |
| PC dies or captured | Champion token removed; faction loses all Champion bonuses 3 seasons |
| PC negotiates major alliance | Add 1 Diplomat card to faction hand this season (temporary) |
| PC uncovers evidence against another faction | That faction's one hidden stat revealed to PC's faction |

---

# PART C — FULL SYSTEM REVIEW

---

## C1 — LEGIBILITY

**Assessment: Moderate. Significant improvement over base; still requires layered information architecture to be strictly enforced.**

**What works:**
- The four-layer information architecture (public board / faction mat / shared ledger / reference cards) correctly separates what players see at a glance from what they privately manage and what they consult. This is essential given system count.
- Deed Tokens give any observer an immediate read on who is close to winning. At any moment, counting tokens = understanding the race. This is Inis's key contribution and it lands well here.
- Clock tracks are the first thing players see. Three sliders. RS going down; TC and IP going up. The visual grammar of "everything is tipping toward catastrophe" is immediately legible.
- Champion tokens on the board give named leaders physical presence. Point at the token = this is who the scene is about. Strong hybrid bridge.

**What is still difficult:**
- The Church Attention Pool resets each season. This means players must track it *within* a season and then mentally discard it. Resetting mechanics that accumulate quickly are cognitively expensive.
- VTM (private at 0–2, public at 3+) requires players to understand a visibility rule on a track. Small but real.
- AER is a shared ledger value that has no physical representation on the public board. It should. A small dial or token on the board edge near the IP track (AER affects IP) would make it visible.
- Hollow Victory fractions (resolved at Year-End) require a running ledger of half-values. Acceptable but needs explicit physical tracking mechanism on faction mat or shared ledger.

**Fix (no editorial gate):** Add AER token to public board, near IP track. Add Hollow Victory sub-score track to faction mat (tally marks).

**Legibility Score: 6/10.** The architecture is right; physical component design will determine whether this resolves to 8 or stays at 6.

---

## C2 — COHERENCY

**Assessment: Strong. The document set coheres around a clear game identity.**

The canonical synthesis identified the game's feel: "powerful institutions trying to manage a world that is quietly dying." Every major system serves this:
- Clocks count down to catastrophe (world dying).
- Deed Tokens require holding all conditions simultaneously (managing, not accumulating).
- Institutional Mandate / Hollow Victory make identity costs mechanically real (powerful institutions compromising themselves).
- Community Projects and Restoration Movement make the "doing something about it" visible (community acting against the dying).
- Thread Debt with residual RS loss makes Thread operations permanently costly (you cannot undo what you did to the substrate).

**Coherence gaps:**
- **Guilds** remain the least philosophically integrated faction. "Commerce is neutral" as a Mandate doesn't connect as deeply to "world dying" as other factions. The Contractor mechanic makes them indispensable but feels more Euro-optimization than existential. This may be intentional — the Guilds are the faction that doesn't believe in the crisis. That's valid design but should be stated explicitly in the faction card's introductory framing.
- **Secondary Objectives** (moved to Advanced) in core BG play creates a gap: a player without secondary objectives has all long-arc goals fully public (Deed Tokens). This is actually fine — legibility improves when long-arc goals are visible. Secondary Objectives add hidden-goal replayability at the cost of legibility, appropriate as Advanced.
- The **Riskbreaker Priority Tree** coherence: the tree protects Valoria from the worst outcomes. But Riskbreakers are invisible — their interventions appear as random failures to players who don't know about them. This is correct setting fiction but creates a design risk: if a player's plan fails because of Riskbreaker Priority 1, and they don't know Riskbreakers exist, the failure feels arbitrary. The rulebook must introduce Riskbreakers early and clearly — "there is an extralegal force protecting Valoria's institutional health; it works in the shadows and you will not see it coming."

**Coherence Score: 8/10.**

---

## C3 — COGNITIVE LOAD

**Assessment: At the edge of the acceptable window. Strict information layering is mandatory.**

**System count: 20 core systems** for all players. Plus 4 faction-specific private tracks for individual players. This is near the ceiling for a 2–4 hour game with 6 active factions.

**Positive factors:**
- The Card-Hand system dramatically reduces decision overhead *within* a season. Rather than evaluating all possible orders, players evaluate their current hand (3–9 cards). This is a major cognitive load reduction versus the original flat-order system.
- Orientation (Inward/Outward) adds almost zero cognitive overhead — it's a single binary choice made at card-play time, not a system to track.
- Cooldown Track is a physical object. Zero abstract tracking.
- Research Tracks are simple tally marks. No decisions until L3 or L5 bonus fires.
- Clock Environmental Effects are reference-card material. Players consult, don't memorize.

**Load spikes (high-complexity moments):**
1. **Church's Assert/Suppress mandatory choice each season (TC > 50):** Fires alongside all other accounting steps. Adds one mandatory decision to an already dense accounting phase.
2. **Thread operation chain:** Play Weaver card → determine orientation → roll → draw Co-Movement → resolve three dimensions → Church Attention Pool update → check if Mandate triggered → check Thread Debt. This is 6–7 sequential micro-steps from one card play. It needs a reference card "Thread Operation Procedure" listing exactly these steps in order.
3. **Hollow Victory Year-End:** Multiple concurrent calculations applying to all factions simultaneously. Recommend a structured scoring sheet (pre-printed) rather than mental arithmetic.
4. **Faction-specific private tracks:** VTM (Varfell), RDT (Hafenmark), TD (Hafenmark), AER (Church). These are faction mat elements but they each have gaining/losing conditions that must be tracked across multiple seasons. Individual player cognitive load is manageable; the concern is when players must reason about *other* factions' private tracks.

**The hardest single season:** A Community Weaving in Church-adjacent territory with an Inquisitor present, a Champion nearby, and Thread Debt outstanding. From the audit: 10+ sequential steps. Per the critical review's proposal (BG-E-65), cap cascade depth at 3 within-resolution effects; defer remaining to next accounting. This cap needs to be confirmed [EDITORIAL BG-E-65] but should be included in the skeleton as a provisional rule.

**Provisional cascade depth cap (pending BG-E-65):** No single card play may trigger more than 3 immediate mechanical effects in one resolution phase. Additional triggered effects are queued for Seasonal Accounting.

**Cognitive Load Score: 7/10.** The Card-Hand system does enormous work. The cascade depth cap (if confirmed) keeps it playable. Without the cap: 5/10.

---

## C4 — PROCEDURE AND FLOW

**Assessment: Turn structure is correct in architecture; several resolution-order ambiguities need codification.**

**What works:**
- The 5-phase turn structure (Planning → Negotiation → Reveal → Resolution → Accounting) is clean and follows best-in-class precedents (ASOIAF, Dune). Simultaneous planning with sequential resolution creates the right information dynamics.
- Card-play priority order (Intel → Military → Domain → Social → Thread → Special → Project) is logically defensible: information is gathered first, then military action moves pieces, then governance orders, then diplomacy negotiates the aftermath, then Thread operations respond to the altered state.
- Accounting as a structured 10-step sequence (not a free-for-all) is essential. The sequence exists; it needs to be printed on a reference card and executed strictly.

**Ambiguities to codify:**

1. **Resolution order within priority tiers:** Cards in the same tier resolve by Stability (highest first). What happens when two factions play the same card type in the same territory targeting each other? Simultaneous resolution: both rolls made; higher result (by Ob margin) applies first. Ties: player to the active faction's left goes first.

2. **Crown Policy vs Parliamentary Opposition vs Censor resolution order** (previously flagged BG-E-66): Policy (Crown plays Censor outward) → Parliamentary Manoeuvre (Hafenmark may respond with Senator Inward) → Censor (any faction's Censor card blocks one order). Sequence: Policy effect is declared → Hafenmark may respond immediately (interrupt) → Censor activates last (blocks one specific order in the sequence). [EDITORIAL BG-E-66 for confirmation]

3. **Senate Market purchase timing:** When during resolution can a faction buy a Senate card? Recommend: Senate Market purchases are a sub-action of Social (Senator) card play. Playing Senator Outward (Diplomacy) to purchase a Senate card is a valid Diplomacy action. This must be stated explicitly.

4. **Recess timing:** When can Recess be played? Recess is played as a card in the Resolution phase (Priority 5, with Social, or as a standalone). It cannot be played simultaneously with another card — it is a full card play, taking the Recess card's place in the sequence.

5. **Year-End accounting vs Seasonal accounting:** Year-End includes all Seasonal steps plus additional Year-End steps. Must be stated clearly: Year-End is a Season with extra steps, not a separate phase.

**Flow Score: 7/10.** Architecture correct; codification of ambiguities will move this to 9/10.

---

## C5 — MECHANICAL CRUNCH

**Assessment: High but structured. Crunch is concentrated and front-loaded; the mid-game is actually smoother than setup suggests.**

**Sources of crunch:**
- **Setup:** Territory control, 6 faction stat tracks, 12 Research Track positions (2 per faction × 6), 6 Champion tokens, 6 starting card hands, PI track, Attention Pool, RS/TC/IP tracks, AER value. Setup is dense but occurs once.
- **Season Start:** Planning simultaneous, so crunch is distributed across players. Not a bottleneck.
- **Resolution:** Variable per card type. Thread operations are the crunchiest (6–7 steps per operation). Non-Thread resolutions are 2–3 steps (roll, apply, check Mandate). Most seasons will not have Thread operations — crunch is event-driven, not constant.
- **Accounting:** The 10-step sequence. This is the consistent crunch point, every season.

**Crunch comparisons to claimed precedents:**
- Accounting-phase crunch is comparable to *Gaia Project* (research track advances, round bonus scoring, federation checks — all dense). GP players accept this crunch because the mid-game is smoother. Same should be true here.
- Thread operation crunch is comparable to *Anachrony* exosuit placement + temporal mechanics. Anachrony players describe these as "the interesting decisions," not "the exhausting ones." If Thread operations feel interesting (high-stakes, consequence-heavy), crunch is a feature.
- The Senate Market + Card-Hand is simpler than Concordia's province card scoring (which requires tracking 4 gods' point formulas). Valoria's Senate cards don't have complex scoring conditions — they expand action vocabulary.

**Crunch reduction opportunities (no editorial gate):**
- Thread Operation Procedure reference card (single laminated card per table): 7 steps in order. Eliminates "what comes next" hesitation.
- Accounting Reference Card: 10 steps, printed as checklist. Players check off each step. Eliminates "did we do X?" debates.
- Scoring Sheet for Hollow Victory: pre-printed columns per faction with modifier checkboxes.

**Mechanical Crunch Score: 7/10.** Acceptable for the target complexity tier (Gaia Project, Pendragon, Concordia are all in this band). Reference cards are mandatory for this to feel smooth.

---

## C6 — EMERGENT POSSIBILITIES

**Assessment: Excellent. This is the system's greatest strength.**

The audit identified three full emergent narrative chains from Amendment 2 alone. Here, the structural analysis of where emergence comes from:

**Highest-yield emergent intersections:**

1. **AER + TC + RDT triple pressure (Amendment 2):** Church loses AER (appears weak domestically) → must Assert every season → Assert fires Crown and Hafenmark Mandate triggers → Almud issues Supremacy Decree → Church TC −3 → AER −1 → RDT +1 → Church cannot reach primary victory → Church pivots to Dual Theocracy → IP drops (Altonia invested in Church) → Vaynard's VTM advances unmolested → Thread Supremacy path opens. Nobody scripted this. It emerges from three interlocked faction mechanics.

2. **Riskbreaker File vs Vaynard VTM escalation:** Each Vaynard CB that Riskbreakers expose reduces their next token cost by 1 (file deepens). Each failed exposure after VTM 4 costs Riskbreakers +1 difficulty. This creates a true multi-season adversarial escalation between an NPC and a player: Vaynard manufactures; Riskbreakers counter; Vaynard improves; Riskbreakers adapt; eventually one side wins a decisive season. The outcome is not predictable.

3. **Restoration Presence + Attention Pool + Champion geography:** Revolution starts Community Weave in T14 (Einhir Heartland) → Attention Pool rises → at threshold 7, Inquisitors deploy → Inquisitors in T14 → each Inquisitor present: +2 Attention next season → Church Crusade declared → Templars deploy into T14 → Battle → Community Project disrupted → RS −2 from Community Weave failure → RS drops below threshold → TR +1 all factions → Varfell Tribune on T14: VTM +1 → Vaynard uses TR 3 ability (preview Co-Movement cards) → Vaynard positions for Patience + CB next season. One Weaving attempt set Vaynard up for a Casus Belli.

4. **Almud Dominion path + Riskbreakers turning against Crown:** Almud issues Emergency Powers twice → Riskbreakers Priority 2 may fire against Crown's own Military → Crown's Dominion push is obstructed by its own peace-keeping apparatus → Baralta's TD rises (Emergency Powers trigger) → TD 4: Baralta declares Almud unworthy → Crown loses 1 Deed Token → Crown must choose: back down (lose Dominion momentum) or push harder (accelerate Riskbreaker opposition and Baralta's Theological Supremacy path simultaneously). The king's overreach becomes its own enemy.

**Emergent quality per landmark precedent:**
- Pax Pamir: Valoria matches its political texture — you are always embedded in a system you don't control. ✓
- The Quiet Year: Community Projects race against clock-doom in exactly the right way. ✓
- Pendragon: Conviction/Institutional Mandate mechanic creates multi-season character arcs for faction leaders. ✓
- Concordia: Card-hand as capability creates exactly the "what I've built is what I can do" feeling. ✓

**Emergent Score: 9/10.** The system density that creates cognitive load concerns also creates this emergent quality. The tradeoff is real but worth it.

---

## C7 — AGAINST ACCLAIMED PRECEDENTS

**Concordia:** The Card-Hand + Recess + Senate Market is a near-direct translation. Valoria adds: Orientation (makes one card do two things — an improvement), Unique Power cooldown (Action Wheel — absent from Concordia), faction-asymmetric starting hands (more asymmetric than Concordia — appropriate for Valoria's Hegemony-style faction differentiation). Where Concordia diverges (no dice; Valoria uses dice): this is intentional for TTRPG compatibility (Ob + roll maps to TTRPG resolution). Valoria's dice are stat-pool based — less variance than pure card-flip but more than pure determinism. Acceptable.

**Pax Pamir:** The political embed-and-leverage dynamic is well expressed through Standing Tokens, Crown Policy (everyone must adapt to Crown's policy environment), and Proxy Support (Advanced). Pax Pamir's court card mechanics (coalition loyalty shifts) are partially replaced by Institutional Mandate — you can't pivot faction identity costlessly.

**The Quiet Year:** Community Projects and the clock-doom structure (RS Rupture as the Frost Shepherds) land well. One divergence: The Quiet Year has no individual winners. Valoria has faction victory paths that coexist with shared survival. This is a creative tension, not a contradiction — the "and yet individuals still compete" of Valoria is a more complex moral statement than The Quiet Year's pure-collective model.

**Pendragon:** Conviction/Institutional Mandate/Hollow Victory creates the seasonal-passion mechanic analog. The multi-season faction narrative arc (Baralta watching Almud, TD accumulating, TD 4 firing as a decisive moment) IS Pendragon's passion-building model applied at faction scale. Strong translation.

**Nemesis:** Attention Pool as noise-mechanic translates well, with the P-08 fix (consequence-detection, not operation-detection). Nemesis uses noise to escalate tension within a session; Valoria uses Attention to escalate Church institutional response over a season. Same structure, different temporal scale.

**Gaia Project:** Research Tracks (2 per faction, 0–5, L3/L5 breakthroughs) are a clean extraction. Valoria correctly chose 2 tracks (synthesis ruling) over Gaia Project's 6 — appropriate scaling. The Season Objective tile system (variable round scoring) adds mid-game relevance for factions not in the lead — a necessary pacing tool.

**What the precedents are missing (Valoria's unique contributions):**
- None of the reference games have a substrate mechanic where all actions occur on a common ground that is simultaneously degrading (RS as Thread substrate, not just a clock). This is Valoria's most philosophically distinctive feature and it works.
- None have a BG/TTRPG hybrid interface with bidirectional consequence propagation. The Cascade Phase card effects are genuinely novel design.

**Precedent Alignment Score: 8/10.** Strong extraction from best-in-class games. Novel in its substrate-as-ground mechanic and hybrid interface.

---

## C8 — FUNCTIONALITY

**Assessment: High structural functionality; two critical functional gaps must be resolved before playtest.**

**Functional:**
- Victory conditions are specific and trackable. Deed Token system makes them publicly visible.
- Season structure has a defined sequence. No ambiguity about when things happen.
- NPC AI priority trees are deterministic. No GM judgment required for NPC resolution.
- Clock environmental effects are threshold-based, not continuous calculation.
- Co-Movement cards provide structured randomness for Thread consequences without requiring GM improvisation.
- Mass Battle (now approved) provides a complete resolution procedure separate from domain orders.

**Critical functional gaps:**

**Gap 1 — Senate Market buying procedure:** When, exactly, can a player buy from the Senate Market? The skeleton says "during Social (Senator) card play" but this creates a sequencing issue: if Senate cards are bought during resolution (Phase 4, Priority 4 Social), a player who played all their non-Social cards in Priorities 1–3 cannot buy Senate cards this season. This may be intentional (you must invest in Social capacity to develop your hand) or an unintended limitation. Needs a ruling. 

**Recommendation:** Allow Senate Market purchases as a standalone action during the Negotiation Phase (Phase 2) at standard cost, OR as part of Social card resolution. This gives players two windows and prevents full hand-depletion from blocking development.

**Gap 2 — Löwenritter during peacetime:** The Löwenritter's partial sheet gives them Legionary, Tribune, Martial Law, and Recess. During peacetime, their priority tree says: defend Arnesheld → issue Martial Law if TC > 50 → oppose sovereignty threats. But between these triggers, they do nothing. An NPC faction that takes 0 actions for 8 seasons is a board-state problem — their inaction has effects (Arnesheld unfortified, no Muster). The NPC AI needs a default action for quiet seasons: default to Govern in Arnesheld (Consult card, Inward) to accumulate Stability. Simple but necessary.

**Gap 3 — Restoration Movement political actions:** Per the bg_improvement_review.md fix, Restoration needs both Community Weaving (Thread) AND Community Organizing (rendered-world). The skeleton provides Organizer and Weaver card types but does not specify what Community Organizing *mechanically does* (what roll, what outcome, what territory effects). This needs to be defined before playtesting.

**Recommendation:** Community Organizing (Organizer card, Outward) = Influence roll vs Ob 2. Success: Restoration gains 1 Influence in territory. Overwhelming: Restoration gains 1 Influence + territory Prosperity +1 (community investment). Failure: territory controller may issue Govern without card play to offset. This is a simple but necessary completion.

**Functionality Score: 7/10.** Three gaps identified; all solvable without editorial approval. Once resolved: 9/10.

---

## C9 — SUMMARY SCORECARD

| Criterion | Score | Key Issue |
|-----------|-------|-----------|
| Legibility | 6/10 | AER needs physical board representation; Hollow Victory needs pre-printed sheet |
| Coherency | 8/10 | Guilds framing thin; Riskbreakers need early rulebook introduction |
| Cognitive Load | 7/10 | Provisional cascade depth cap needed; Thread Operation reference card mandatory |
| Procedure and Flow | 7/10 | 3 resolution-order ambiguities need codification |
| Mechanical Crunch | 7/10 | Acceptable for complexity tier; reference cards mandatory |
| Emergent Possibilities | 9/10 | The system's greatest strength; multi-faction chain interactions are genuine |
| Against Precedents | 8/10 | Strong extractions; novel in substrate mechanic and hybrid interface |
| Functionality | 7/10 | 3 functional gaps; all solvable without editorial approval |
| **Overall** | **7.4/10** | **Ready for structured playtest; not ready for final compilation** |

---

## C10 — PRE-PLAYTEST CHECKLIST

**Must complete before first playtest (no editorial gate):**

- [ ] Senate Market purchase timing: add to ruleset (Phase 2 window + Phase 4 Social window)
- [ ] Community Organizing mechanic: define roll + outcome for Organizer card
- [ ] Löwenritter default NPC action (quiet seasons: Govern Arnesheld)
- [ ] AER physical component: small dial or track on board near IP track
- [ ] Thread Operation Procedure reference card (7-step laminated card)
- [ ] Seasonal Accounting reference card (10-step checklist)
- [ ] Hollow Victory pre-printed scoring sheet
- [ ] Provisional cascade depth cap stated in rulebook as explicit rule
- [ ] Crown Policy → Parliamentary Manoeuvre → Censor resolution order codified (pending BG-E-66 editorial)

**Must resolve before first playtest (editorial gate — user approval required):**

- [ ] BG-E-51: Baralta's Conviction
- [ ] BG-E-53: Vaynard's Conviction
- [ ] BG-E-59: Almud's Conviction
- [ ] BG-E-63: VTM 5 / P-14 compliance ruling
- [ ] BG-E-64: Crown's 5 Deed Token enumeration
- [ ] BG-E-65: Cascade depth cap confirmation
- [ ] BG-E-66: Policy resolution order confirmation
- [ ] MP-34: Institutional Mandate trigger conditions per faction (currently skeleton shows implied triggers; formal trigger list must be authored)

**Can wait until after first playtest (editorial gate):**
- [ ] BG-E-60: TD visibility
- [ ] BG-E-61: AER starting value
- [ ] BG-E-62: Reformed Settlement response options
- [ ] BG-E-50: Cardinal schism mechanics
- [ ] BG-E-27/33: Champion Renown ability text
- [ ] All Advanced Rules (Secondary Objectives, Proxy Support, Thread Veil Cards)

---

*Skeleton Ruleset v0.1 complete.*  
*20 core systems. Document hierarchy applied throughout. Mass Battle v3 and GT-01–GT-03 fully integrated as approved.*  
*GitHub MCP unavailable — all outputs require user commit to jordanelias/ttrpg, branch main.*
