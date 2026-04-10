<!-- DEPRECATED: 2026-04-09 — SUPERSEDED BY designs/board_game/valoria_bg_v05_simulation_and_patches.md. Do not use as a mechanical reference. Retained for audit trail only. -->

# BG REVISED PROPOSAL — CRITICAL REVIEW

**Date:** 2026-03-31
**Scope:** Review against specific setting elements, naming corrections, and 8 evaluation metrics

---

## NAMING CORRECTIONS (apply throughout all BG documents)

| Wrong | Correct | Notes |
|-------|---------|-------|
| Revolution | **Restoration Movement** | Always. Not a revolution — a restoration of what was lost. |
| Solmund | **Solmund** | Always. The name used in canon. |
| AG (Anno Solmund) | **AS (Anno Solmundi)** | Calendar system follows the correct name. |
| Church of Solmund | **Church of Solmund** | Follows from above. |

These are not optional. Every document in the designs folder uses the wrong names. All need correction before compilation.

---

## MISSING SETTING ELEMENTS

### 1. Löwenritter — Missing as Full 8th Faction

**Problem:** The proposal mentions Löwenritter only in passing (Crown garrison at Ehrenfeld, coup reference). The Löwenritter is a designed 8th faction with:
- Partial sheet (Military, Stability, Influence, Intelligence — no Mandate, no Wealth in peacetime)
- Full sheet on coup trigger (4 conditions, gains Mandate and Wealth from Crown)
- Unique Power: Martial Law
- Ethical framework: Deontological Honor Code
- Leader: Grandmaster Sigrid Ehrenwall (the most dangerous NPC — patient, competent, commanding an army)
- Institutional Mandate should be: *"The military order serves the Crown as institution, not the monarch."*
- Coup Counter interaction with TC (Church territorial seizure at TC 80 + Löwenritter coup = three-way endgame)

**The proposal needs a full Löwenritter faction card** in B3, with Card-Hand adaptation. Löwenritter's peacetime card hand: 1× Legionary, 1× Tribune (Intel), 1× Martial Law (Unique), 1× Recess. Post-coup: expanded hand. The Löwenritter should feel like a coiled spring — limited actions until the moment they act, then decisive.

### 2. Inquisitors — Missing as Church Sub-System

**Problem:** Inquisitors have their own ethical framework (duty-centred against heresy) distinct from the Church's Divine Command. They're the Church's operational heresy-hunting arm. The proposal's Attention Pool and Heresy Investigation mechanics should be explicitly tied to the Inquisitors as the Church's deployable instrument — not an abstract "Church opens investigation."

**Fix:** Inquisitor units are a Church unit type (alongside Parish Militia and Knights Templar). Inquisitors: deploy via Inquisition card play. Once deployed in a territory: +2 Attention Pool per season they are present. Can open Heresy Investigations without an additional card play. One Inquisitor can be active per territory. Moving an Inquisitor to a new territory requires a Senator card (Social action).

### 3. Riskbreakers — Missing Entirely

**Problem:** Riskbreakers (Act Consequentialism ethical framework) appear in the gap register's faction ethical framework table. They are not represented in the BG proposal. They appear to be an independent mercenary/adventurer group.

**Status:** [GAP: Riskbreakers — insufficient information to design BG representation. Need: who they are, what they do, their scale of operation, and whether they are a sub-faction, NPC force, or hire-able unit type.]

### 4. Four Cardinals under the Holy Confessor — Missing Entirely

**Problem:** The Church hierarchy below the Holy Confessor (Himlensendt) includes four Cardinals. These are not mentioned in any project knowledge document or the BG proposal. If they exist in the setting, they should be:
- The Church's officer corps for BG purposes (each Cardinal governs a doctrinal or territorial arm)
- Sources of internal Church tension (Cardinals may disagree with the Confessor)
- Potential split mechanics if Church Stability drops (a Cardinal may challenge the Confessor — internal schism)

**Status:** [GAP: Four Cardinals — no canon source found. Need: names, doctrinal portfolios, relationship to Confessor, whether they are mechanically distinct or narrative-only.]

### 5. Schoenland — Insufficiently Mechanized

**Problem:** Schoenland is described in canon as an active spoiler: pro-war (arms sales), anti-conquest (benefits from sustained feuding), actively stokes tensions without triggering resolution. The proposal treats it as a passive territory (T15) with trade modifiers.

**Fix:** Schoenland NPC AI should actively:
- At IP 30+: fund proxy operations (+1D to any faction's military actions at Border Pass — Schoenland sells arms to whoever is fighting)
- At TC 50+: provide intelligence to anti-Church factions (Schoenland profits from secular trade, not theocratic governance)
- At RS < 40: do nothing (Schoenland doesn't understand or care about Thread substrate)
- Stoke tensions: each season where no faction is in active conflict, Schoenland NPC AI: IP +1 (they fund border provocations to maintain the arms market)

Schoenland should feel like a profiteer that benefits from everyone else's misery — a constant background pressure that makes peace unprofitable.

### 6. Southernmost — Missing as Late-Game Region

**Problem:** The proposal mentions T12/T13 as Thread Wound territories but doesn't capture the Southernmost as a multi-season expedition target. The existing Southernmost Expedition procedure (batch_bc_designs.md) is a 4+ season extended action with zone-based exploration, entity encounters, and Extraordinary Weaving as the endgame Thread repair path.

**Fix:** The BG needs a Southernmost Expedition mechanic:
- Requires: RS < 40, faction unit + Thread-sensitive character in T13 (Askeheim), 3 Wealth investment
- Multi-season Project (scope 4): each completed season of expedition advances toward Thread repair
- Completion: permanent RS +5, Southernmost stabilized
- Risk: entity encounters each season of expedition (entity tier escalates with depth)

The Southernmost Council (Levinas-based Husserlian pragmatism) is a non-faction entity that can provide information and Thread support but does not pursue political goals. They are the most knowledgeable Thread practitioners alive and structurally uninterested in power.

### 7. Parliament / Royal Court / Senate — Under-Mechanized

**Problem:** The proposal mentions Parliamentary Manoeuvre (Hafenmark) and Royal Decree (Crown) but doesn't give Parliament, the Royal Court, or any senatorial body a distinct mechanical identity. Canon includes "Parliament Integrity" as a starting stat (7 at game start).

**Fix:** Parliament should be a shared institution, not just Hafenmark's tool:
- **Parliament Integrity (0–10):** Tracks institutional health of parliamentary governance. Starts at 7.
- At PI ≥ 5: Parliamentary Manoeuvres are available to Hafenmark. Crown Decree requires Mandate ≥ 4.
- At PI 3–4: Parliamentary Manoeuvres at +1 Ob. Crown Decree Ob reduced to 1 (Crown governs without parliamentary check).
- At PI ≤ 2: Parliament non-functional. Hafenmark loses Parliamentary Manoeuvre. Crown governs by decree (no Ob check). TC +2 (Church fills the governance vacuum).
- PI degrades when: Crown issues Emergency Powers (−1), Church territorial seizure occurs (−1), Löwenritter coup fires (−3, Parliament is suspended).
- PI recovers when: Hafenmark plays Parliamentary Manoeuvre successfully (+1), Crown issues Parliamentary Session policy (+1).

The Royal Court (Valorsplatz special property) should mechanically represent the physical location where Decree and Parliamentary actions gain their bonuses. It is not a separate institution — it is the *place* where Crown and Parliament interact.

---

## EVALUATION METRICS

### 1. Coherence with Canon

**Score: Moderate.** The prior review identified 4 P-code violations (MP-10 Hafenmark lineage [fixed], MP-24 triggers [fixed], MP-04 TR cap [fixed], MP-18 Restoration split [fixed]) and a P-14 co-movement extension requirement. All fixes were applied in the revised proposal. Remaining canon concern: the Church of Solmund naming is wrong throughout, and the Solmundite theological framework (Divine Command) should reference Solmund, not Solmund.

### 2. Cogency with TTRPG and Hybrid

**Score: Good structurally, thin at interfaces.** The Card-Hand system mirrors the TTRPG's "capability = what you've built" principle well. The Cascade Phase effects (MP-35) are the strongest hybrid bridge. The Zoom-In triggers are adequate but should be expanded to include Löwenritter coup, Inquisitor arrival, and Schoenland diplomatic contact as additional trigger conditions. The Parliament Integrity stat needs to be shared across modes (TTRPG Domain Echoes can affect PI; BG orders affect PI; shared seasonal cap applies).

### 3. Cognitive Load

**Score: TOO HIGH.** This is the proposal's most serious problem. Count of distinct mechanical systems a player must track:

Core: Card-Hand (6 card types + orientation + Recess timing) + Lead/Follow + Cooldown Track = **3 systems**
Political: Institutional Mandate (Uphold/Compromise) + Contempt + Deal Tokens + Crown Policy + Proxy + Leverage = **6 systems**
Thread: TR + Thread Debt + Substrate Scars + Attention Pool + Community Projects + Co-Movement cards = **6 systems**
Champions: Presence + Wound States + Renown + Conviction invocation = **4 systems**
Progression: 2 Research Tracks + Season Objectives = **2 systems**
Victory: Deed Tokens + Hollow Victory modifiers + Secondary Objectives = **3 systems**
Faction-specific: TC-as-currency (Church) + Network Depth (Niflhel) + Contractor (Guilds) + Presence (Restoration) + Policy (Crown) = **5 systems**

**Total: ~29 distinct mechanical systems.** For comparison: Gaia Project has ~10. Pax Pamir has ~8. Even Twilight Imperium 4th has ~15.

This is a crunch cascade generator. A single season could involve: play a card (check orientation, Lead/Follow), resolve against Ob (modified by RS environmental effect + TC environmental effect + territory special + ethical framework + Research Track bonus + Champion presence), check if Mandate is triggered (Uphold/Compromise), check Attention Pool accumulation, check TR accumulation, apply co-movement card, check for Heresy Investigation, apply Contempt changes, check Leverage generation, advance Project markers, update Deed Tokens.

**Recommendation — cut or merge to ≤15 systems:**
- **Merge** Leverage and Contempt into a single Reputation/Standing system
- **Cut** Proxy Support (achievable through Deal Tokens + Contracts informally)
- **Cut** Season Objectives (Research Tracks already provide mid-game scoring variation)
- **Simplify** Lead/Follow to a flat domain-expertise bonus (+1D) rather than a response/follow mechanic
- **Defer** Substrate Scars to advanced/campaign rules (Thread Debt alone is sufficient for standard play)
- **Defer** Champion Conviction invocation to hybrid mode only (BG Champions provide static bonuses only)
- **Make** Hollow Victory scoring OPTIONAL (print on a reference card; experienced players use it)

This brings the count to ~18 — still heavy but within the range of a complex strategy game.

### 4. Friction Points

| Friction | Systems Involved | Issue |
|----------|-----------------|-------|
| Card-Hand + faction asymmetry | Church TC-as-currency deploys units without Muster card; Guilds Contract requires coordinating with another player's card availability | Two asymmetric factions' actions depend on systems outside the Card-Hand, creating rules exceptions that players must remember |
| Attention Pool + Restoration Organizing | Restoration Community Organizing (non-Thread) should NOT trigger the Pool; Community Weaving (Thread) should. Players/AI must track which Restoration action is which | The Organizing/Weaving split is canon-necessary but creates a bookkeeping burden for the NPC AI |
| Crown Policy + Parliamentary Manoeuvre | Crown issues a Policy; Hafenmark may oppose. If the Censor card is also in play (blocks one order), there are three layers of order-modification happening simultaneously | Resolution order of Policy → Opposition → Censor is undefined |
| Deed Tokens + Hollow Victory | A faction may have all 4 Deed Tokens but fail Hollow Victory modifiers, producing a net Deed count of 2.5. Half-Deed scoring is unintuitive | Round Hollow Victory modifiers to whole numbers |

### 5. Contradictions

| Contradiction | Details |
|---|---|
| Restoration Movement is "always NPC-controlled" but has the most detailed player-facing mechanics (Presence markers, Community Projects, Organizing/Weaving split) | If always NPC, these mechanics must run on NPC AI — but the Organizing/Weaving distinction requires judgment calls that simple priority trees can't make well. Either make Restoration playable as an optional 7th player faction, or simplify its mechanics to NPC-executable priority logic. |
| Guilds "cannot Muster" but can place Hired Blades via Wealth | This is mechanically a Muster-by-another-name. If the point is "Guilds cannot build military capacity," then Hired Blades should have strict limitations (cannot garrison, disappear after 1 season, cannot defend — attack only) |
| Niflhel Network Depth is gained by Intel/Smuggle but the Card-Hand gives Niflhel 3× Tribune cards | Tribune is the Intel/Covert card. 3 Tribunes + 1 limited Legionary + 1 Consul + 1 Recess = 6 cards. Niflhel's hand is 50% Intel cards. This is appropriate for their identity but means Niflhel plays a fundamentally different game (information-heavy, action-light) that may not be *fun* for 12+ seasons |

### 6. Mechanical Crunch Cascades

**Worst case scenario:** A Community Weaving operation in a Church-adjacent territory with an Inquisitor present, a Champion nearby, and Thread Debt outstanding.

Chain: Community Weaving fires → co-movement card drawn → Attention Pool +2 (community gathering) → if Pool crosses threshold 3, Heresy Investigation opens automatically → Investigation targets Restoration → Restoration Stability check → if failed, Restoration loses Presence → Project progress −1 → Thread Debt still outstanding → RS −1 at Accounting → RS crosses threshold → TR +1 to all factions → TC environmental modifier may change → Church gets free Inquisition...

This chain is 10+ steps from a single action. Each step involves a different system. This is the definition of a crunch cascade.

**Fix:** Cap cascade depth. Rule: "No single action may trigger more than 3 downstream mechanical effects in a single resolution. Additional effects are deferred to next season's Accounting." This is ugly but necessary.

### 7. Emergent Qualities

**Score: Excellent — the best aspect of the proposal.** The multi-system intersection design produces emergent narrative conditions that no single system could generate:

- Crown issues Royal Taxation → Guilds' Mandate challenged → Guilds Compromise → self-Contempt → Guilds politically weakened → Church smells opportunity → Inquisition targets Guilds' trade partners → Guilds' economic engine threatened → Guilds Contract with Varfell for Intel against Church → Varfell gains information → Varfell TK advances → information reaches Restoration → Community Weaving strengthened → RS improves → everyone benefits except Church

This is a 10-step emergent political narrative generated entirely by mechanical interactions. No scenario script required. This is what the game is FOR.

- Ehrenwall watches Almud surrender to Altonian tutoring demand → Löwenritter Coup Counter advances → Church senses opportunity → TC rises → Church territorial seizure at TC 80 → Löwenritter coup trigger #3 met → three-way endgame (Crown collapse, Church theocracy, military junta) → in hybrid, this generates 4-5 TTRPG scenes spontaneously

The proposal's emergent quality justifies its complexity — but only if the cognitive load can be managed.

### 8. Legibility

**Score: Poor at current complexity.** A player looking at the board mid-game sees: 15 territories with Prosperity/Fort/control markers + Substrate Scar markers + Project markers + Presence markers + Network Depth markers + Champion tokens + unit tokens + 3 clock tracks + Attention Pool track + per-faction: card hand + Cooldown Track + 2 Research Tracks + Deed Track + Contempt/Leverage tokens + Deal Tokens.

This is more information than a player can parse at a glance. The board state is illegible.

**Fix — information layering:**
- **Public board:** territories + clocks + control markers + Champions only. This is what you see.
- **Faction mat:** card hand + Research Tracks + Deed Track + Contempt + Cooldown. This is what you hold.
- **Reference cards:** environmental effects, order procedures, co-movement rules. This is what you consult.
- **Everything else** (Network Depth, Substrate Scars, Attention Pool, Project progress): tracked on a shared ledger or companion app, not physical tokens on the board.

---

## SUMMARY

The revised proposal is mechanically ambitious and narratively rich. Its emergent qualities are excellent — the best in the project. But it is currently overloaded:

- **29 systems** is too many. Target: ≤15 core + ≤5 advanced/campaign.
- **Crunch cascades** need a depth cap.
- **Legibility** needs information layering.
- **5 setting elements** are missing or under-mechanized (Löwenritter, Inquisitors, Schoenland AI, Southernmost expedition, Parliament Integrity).
- **2 elements** need investigation (Riskbreakers, Four Cardinals).
- **Naming** is wrong throughout (Solmund, Restoration Movement, AS).

The proposal should be revised to: reduce system count, add missing factions/institutions, fix naming, and layer information for legibility. The emergent narrative engine — which is the proposal's greatest strength — should survive these cuts intact, because emergence comes from system *interaction*, not system *quantity*.
