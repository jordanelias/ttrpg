<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: board_game_v30_infill.md -->

<!-- v30 baseline — renamed from designs/board_game/valoria_bg_v05_simulation_and_patches.md on 2026-04-13 -->
# VALORIA: THE BOARD GAME
## Institutional Mandate — Uphold / Appease (PP-189)

**Trigger:** Domain Action directly challenges a faction's core institutional authority AND targeted faction Mandate ≥ 4.

| Choice | Timing | Effect | Cost |
|--------|--------|--------|------|
| **Uphold** | Before roll | Roll proceeds normally | None |
| **Appease** | Before roll | Triggering action cancelled entirely — no roll made | Mandate −1 |

**NPC rule:** Non-Player Character factions Appease if Mandate ≥ 4 AND Stability ≤ 3.

*PP-189, 2026-04-02*

## Version: v0.6 (ST-BG/INT + P-12–P-32 applied in-place; PART THIRTEEN and PART TEN/ELEVEN eliminated; pure mechanical spec)
## Status: WORKING DESIGN — read straight through. No appendix sections.
## v0.4 → v0.5 → v0.6 Transition Document
**Date:** 2026-04-01
**Critical corrections applied:** d10 dice system (7-10 = success; 10 = bonus success; 1 = remove one success). Ob minimum = 1 (Ob0 impossible).

---

# PART ONE: CRITICAL SYSTEM CORRECTIONS

## CORRECTION 1 — Dice System (d10, supersedes all d6 language)

**Current state (B3):** "All rolls: pool = relevant faction stat (1–7). Dice: d6. Success = 4+. Majority 1s = Failure regardless of other dice."

**Correct state:**
All rolls use **d10**. Results per die:
- **7, 8, 9:** 1 success.
- **10:** 2 successes (1 standard + 1 bonus).
- **1:** −1 success (subtract one from total net).
- **2–6:** 0.



> **P-15: standing cap:** Standing: Cannot exceed 5. Cannot fall below 0. Changes of +2 or −2 cap at the boundary — surplus is lost.


**Probability summary (d10):**

| Pool | E(net successes) | P(≥1 net) | P(≥2 net) | P(≥3 net) |
|------|-----------------|-----------|-----------|-----------|
| 2    | 0.80            | ~58%      | ~22%      | ~5%       |
| 3    | 1.20            | ~74%      | ~40%      | ~15%      |
| 4    | 1.60            | ~85%      | ~56%      | ~27%      |
| 5    | 2.00            | ~91%      | ~69%      | ~42%      |
| 6    | 2.40            | ~95%      | ~80%      | ~57%      |
| 7    | 2.80            | ~97%      | ~88%      | ~69%      |

*These probabilities are approximated using binomial and trinomial expansion with P(success-or-bonus)=0.40, P(subtraction)=0.10, P(neutral)=0.50. Exact computation available; approximations sufficient for balance assessment.*

**Impact on existing content:**
- Faction pools of 4-5 (most common) at Ob 2 succeed roughly 56-69% of the time. Previously (d6 at 4+) success was ~60-74%. The d10 system is slightly harder, producing more Partials. This is correct for the setting's contested political tone.
- Ob 1 checks for pools of 3+ are effectively reliable (74-97%), preserving the feel that basic competence succeeds. Ob 3 checks are genuinely threatening (15-42% for pools 3-5), preserving the weight of difficult rolls.
- The bonus success on 10 (10%) adds upside tension on small pools: a pool of 2 can still get Overwhelming if both dice show 10.

> **P-24:** **Faction elimination:** Stability 0 at Accounting end = faction eliminated. Units remain on board until Muster order removes them (holding ground, now Masterless). Other factions may Claim (Domain Action) Masterless units.

> **P-14: rep cap:** Reputation: Cannot exceed 5. Cannot fall below 0. Cap applies before any modifier is applied — excess is discarded.

---

## CORRECTION 2 — Ob Minimum = 1 (Ob0 is impossible)

**Current state (B3):** "Ob 0: Any roll with ≥ 1 success = Overwhelming. Ob cannot go below 0. Rolling is still required."

**Correct state (REMOVE the Ob0 paragraph entirely. REPLACE with):**

> **Ob minimum = 1.** No Ob may ever be reduced below 1 regardless of bonuses, modifiers, or stacking effects. Modifiers that would push Ob below 1 are wasted — they do not carry over, grant additional dice, or create other effects. If multiple modifiers stack and would produce Ob 0 or lower, the result is Ob 1.

**Impact on gameplay:**

> **P-29: Rendering Stability gain:** Revolution Rendering Stability gain from Thread operations: +1 Rendering Stability per successful Weave against Church-held territory (max +2/season from this source). Requires Thread Sensitivity ≥ 20 practitioner.

> **P-23:** **Theocracy Counter Seizure threshold:** Church Theocracy Counter 80+ triggers seizure at next Accounting. Territory roll: Church Military vs Defender Military, Ob 2. Each success: one contested territory flips. Hard cap: maximum 2 territory transfers per seizure event per faction (prevents single-season consolidation).


> **P-18:** **Unit cap at Military:** Number of units deployed cannot exceed current Military stat. Excess units over Military are immediately removed — they cannot be held as reinforcements beyond the cap.

**Specific affected rules:**
- Hafenmark Diplomat in T6: Influence 4, Diplomat −1 Ob, base Ob 1 = floor 1. Cannot be reduced further. ✓
- Church in T3 with doctrine-aligned −1 Ob AND territory −1 Ob on a base Ob 2 action = Ob 1 floor. Correct.
- Restoration Community Weaving: Ob = ceil((100−RS)/20) min 1, −1 per Presence marker in territory (floor 1). At RS 72 (start): Ob 2. Formula per params_board_game.md is canonical; bg_v05 simplified "Ob 2" is stale. [PP-491, ED-330 resolved]

> **Policy Instrument definition (PP-036):** **Policy Instrument (Crown only):** When Crown's Mandate ≥ 4, Crown may take one additional Standard Action per season designated as the Policy Instrument. This action may be any action Crown could normally take; it is not limited by card-hand constraints. It activates once per season and cannot be interrupted by Parliamentary Manoeuvre (see P-19). Activation condition: Mandate ≥ 4 at the start of the season.

> **P-19: PM scope:** The Hafenmark free Parliamentary Manoeuvre interrupt is triggered only by Crown's Policy Instrument (once-per-season bonus action, available when Mandate ≥ 4). It does NOT apply to Crown Senator card plays, Decrees, Diplomacy, or any other Crown action.

> **P-21:** | Action | Default Ob | Typical Modifiers |
|--------|-----------|------------------|
| Muster (Legionary Inward) | 2 | −1 in T2 (Garrison), −1 in T11 (Breadbasket) |
| March (Legionary Outward) | 2 | +1 in T8 (Difficult terrain) |
| Govern (Consul Inward / Prefect) | 2 | −1 in own capital; −1 with 

---

## CORRECTION 3 — Degree Table Update (incorporating d10 and negative net successes)

**Remove current degree table. Replace with:**

| Net Successes       | Degree               |
|---------------------|----------------------|
| Ob + 1 or more     | **Overwhelming**     |
| = Ob               | **Success**          |
| Ob − 1             | **Partial**          |
| 0                  | **Failure**          |
| Negative (after subtraction) | **Failure** (treat as 0 for degree purposes; Critical Failure if A majority-1s result (more 1s than 7-10 results) produces a standard Failure with no additional consequence. The degree table applies normally (net ≤ 0 = Failure). Apply Critical Failure consequences.

> **P-16:** **Victory determination:** Both sides roll simultaneously. Compare net successes.
- If attacker's net > defender's net: **Attacker wins.** Apply outcome from attacker's degree (Overwhelming/Success/Partial/Failure) using the DIFFERENCE as the effective surplus: (attacker net − defender net) vs Ob.
-


---



> **DESIGN DECISION (2026-04-02):** Catastrophic Failure / majority-1s override has been struck from the system. All rolls resolve through the standard degree table only. Low-pool results produce Failure; they do not produce an additional consequence category. The majority-1s rule is removed.

# PART TWO: INCONSISTENCIES AND CONTRADICTIONS

## I-01 — Majority 1s Rule uses d6 language

**Location:** B3, Core Mechanic.
**Error:** "Majority 1s override: If more dice show 1 than show 4+, result is Failure." References "4+" (d6 threshold).
**Correction (PATCH P-12):** Update to "If more dice show 1 than show 7-10."

> **P-12: CF rule:** If more dice show 1 than show 7–10 in the same roll, result is **Critical Failure**: apply normal Failure consequences plus one additional immediate consequence (Game Master discretion: −1 Standing, −1 Stability, or one stat degradation).

---

## I-02 — Patience Protocol body vs P-07 Patch (Cap contradiction)

**Location:** B5 Varfell (Patience Protocol), and Part E PATCH P-07.
**Error:** B5 body reads: "Only **one** of the two inaction conditions (Tribune held back, OR Senate Market purchase passed) generates +1 Player Character per season. Both conditions may be met simultaneously, but Player Character gain from inaction is capped at +1 per season. The maximum of +2/season previously stated was an error, corrected in P-07 and now reflected here." PATCH P-07 corrects this to "+1 Player Character maximum per season from inaction." The body text was never updated to reflect P-07.
**Correction (PATCH P-13):** B5 body text must be updated. See Section Two, P-13.

---

## I-03 — Casus Belli Expiration vs "Permanent Until Used"

**Location:** B7 Treaty Betrayal Consequences table vs B7 Casus Belli rules.

---

## I-04 — Faction Collapse: "Attributes Freeze" Contradicted by "Mandate Drops to 0"

**Location:** B4 Accounting, Stability Check at 0.
**Error:** "All that faction's attributes **freeze at current values.**" followed immediately by "That faction's **Mandate immediately drops to 0.**" Mandate is an attribute. An attribute cannot simultaneously freeze and change.
**Correction (PATCH P-15):** "On Faction Collapse, Mandate drops to 0 immediately (the institution has lost all political legitimacy). All OTHER attributes freeze at their pre-collapse values. The Mandate-0 drop occurs before the freeze snapshot is taken."

> **P-20:** **Accounting — Mandate cap:** Faction Mandate cannot exceed 7 (hard ceiling). All modifiers that would push above 7 are discarded. Mandate floor is 0.

> **Military loss timing by mode (PP-041):** Military loss from unit destruction applies differently by mode: — TTRPG mode: Military −1 is an immediate world-state consequence. It affects faction capabilities from the moment the unit is destroyed (within the same battle if relevant). — BG mode: Military −1 from unit destruction queues to the season's Accounting phase (Domain Echo timing). The faction's Military stat does not change during the season; it updates at Accounting. — Hybrid mode: TTRPG timing applies during the battle (immediate). BG timing applies to any units that are destroyed outside of a Player Character-triggered TTRPG engagement.

---

## I-05 — Battle Resolution: Both Sides Roll, No Clear Victory Determination

**Location:** B8, Battle Resolution.
**Error:** "Each side rolls their Military stat + Commander Coordination modifier + Disposition modifier." Outcomes are then listed only from the attacker's perspective: "Overwhelming win: losing side's unit destroyed... Success win: losing side Discipline −2... Partial (attacker)... Failure (attacker)." But both sides roll. The outcome table only resolves the attacker's roll. What happens if the attacker rolls Success and the defender also rolls Success? Is victory assigned by net margin? By who rolled higher net successes?
**Correction (PATCH P-16):** See below. The resolution needs a "compare net successes" rule.

> **Clarification (PP-034):** Drawn battle: "On exactly tied net successes: the battle is drawn. Both sides take Discipline −1 and hold position. Neither side claims or loses territory from this engagement. On the subsequent turn, the initiating attacker may re-engage or withdraw; the territory is contested."

---

## I-06 — Restoration Victory Rendering Stability ≥ 50 vs Rendering Stability Starting at 72

**Location:** B5 Restoration Victory.
**Framing inconsistency:** "5 Presence markers in 5 non-adjacent territories, held 2 consecutive seasons + Rendering Stability ≥ 50." Rendering Stability starts at 72, so this condition is met at game start. The condition only becomes challenging once Rendering Stability degrades below 50, which means in early-game there's no Rendering Stability gate. This is almost certainly intentional design (Restoration must maintain Rendering Stability above 50 to win — it's a preservation condition, not an acquisition condition) but requires explicit framing.
**Correction (PATCH P-17):** Add: "Rendering Stability ≥ 50 must be met at the moment of victory declaration. Restoration's network victory goal inherently requires preventing world degradation — their win is impossible if the world has decayed past the threshold."

---

## I-07 — Phase 4 Tiebreaking Contradiction (Simultaneous vs Sequential for 3+)

**Location:** B4 Phase 4.
**Error:** "Within tier: descending Stability first. **Ties: resolve simultaneously.** Three or more factions same card type same territory: **descending Stability each applying fully before the next.**" For two factions tied on Stability: simultaneous. For three+: sequential. What applies when three factions tie on Stability?
**Correction (PATCH P-18):** "Within tier: resolve in descending Stability order. Tied Stability (exactly equal): resolve simultaneously *only* if there are exactly two factions tied. Three or more factions tied on Stability: resolve in alphabetical faction order (consistent, arbitrary, no player advantage). Ties between two factions in adversarial military actions always resolve simultaneously (both attacks land before consequences are assessed)."

---

## I-08 — Parliamentary Manoeuvre Free Interrupt Scope

**Location:** B4 Phase 4, Resolution order — Policy/Parliament/Censor.
**Ambiguity:** "Crown Policy declared → Hafenmark may immediately respond with Senator Inward (interrupt, no card play cost)." Does this interrupt apply to: (a) Crown's Policy Instrument only (the extra free action from Crown's exclusive tool), or (b) any Crown Senator Inward card play?
**Correction (PATCH P-19):** The interrupt applies to **Crown's Policy Instrument only** — the once-per-season bonus action if Mandate ≥ 4. A Crown Senator Inward played as a normal card play (Decree or Diplomacy) is NOT subject to the free interrupt. This preserves the constitutional balance mechanic (Parliament checks the executive's bonus authority) without making every Crown Senator play costlessly contested.


---

## I-09 — Information Asymmetry Boundary Roll uses d6 while Main System is d10

**Location:** B14 Hybrid Interface, Fog of War.

---

# PART THREE: GAPS AND AMBIGUITIES

## G-01 — Standard Action Obs Not Stated in B3

**Location:** B3 Core Mechanic; action outcome tables.
**Gap:** The stat-to-action mapping lists which stat each card uses, but never states the **default Ob** for each action type. Obs are implied by territory specials ("Muster Ob −1" implies a base), but a new player cannot determine what to roll against without reading all territory descriptions.
**Correction (PATCH P-21):** Add a Standard Ob Reference table to B3.

> **Clarification (PP-039):** "At Military 0, Muster actions produce no units and may not be taken. A Muster action at Military 0 is invalid and does not count as the faction's action for that season. Factions at Military 0 remain politically active but cannot field new military units until Military is raised above 0."

> **Clarification (PP-039):** "At Military 0, Muster actions produce no units and may not be taken. A Muster action at Military 0 is invalid and does not count as the faction's action for that season. Factions at Military 0 remain politically active but cannot field new military units until Military is raised above 0."

---

## G-02 — Prosperity: Undefined Track

> **P-22:** **Prosperity** is a territory-level track, not a faction stat. Each territory has a Prosperity value (0–5); starting values shown in B2. Govern success (Consul Inward / Prefect) increases Prosperity by 1 in that territory. Govern failure decreases it by 1.
**Prosperity effects at Accounting (Year-En

**Gap:** Govern outcome says "Prosperity +1" on Success. T11 grants "+1 Prosperity/season." Community Projects mention "Prosperity +1." But Prosperity is never defined as a stat or track — it is referenced as if self-evident. Is Prosperity a territory-level track that feeds into faction Wealth at accounting? Is it Wealth itself under a different name?
**Correction (PATCH P-22):** Prosperity is a **territory-level modifier** (not a faction stat). Each territory has a Prosperity value (0–5). Uncontested Govern success: Prosperity +1 in that territory. At Year-End Accounting: each territory with Prosperity ≥ 3 generates +1 Wealth for the controlling faction. Prosperity can never exceed 5 or fall below 0. Uncontested T11 Breadbasket: Prosperity +1/season automatically without Govern requirement.

---

## G-03 — VTM "Thread-active territory" Undefined

**Location:** B5 Varfell, Gaining VTM.

---

## G-04 — Thread Operation Step 3 "−1 Ob to THIS operation" Ambiguity

**Location:** B6 Thread Operation Procedure, Step 3.
**Correction (PATCH P-24):** Replace "−1 Ob to THIS operation as substrate resistance" with: "+1 Ob to the NEXT Thread operation in this territory (applied at that future operation's Step 4). The Thread Debt token signals that the substrate has been stressed — future operations in this territory are harder, not this one." This preserves the debt as a forward-looking cost rather than an immediate reward.

---

## G-05 — Heresy Investigation with No Valid Target

**Location:** B6 Church Attention Pool; PATCH P-10 Church Non-Player Character artificial intelligence.

---

## G-06 — Forgetting Check "Spirit Proxy" in Board Game Mode

**Location:** B7 Warden Cooperation Track, Forgetting Check.
**Gap:** "**In board game mode, the Forgetting Check pool is:**
- Restoration faction: Influence + 1D per Presence marker in T13.
- Ob 1 (floor). Thread-qualified presence (Restoration Weaver active in T13 this season, or VTM 2+) does not reduce Ob below the floor; instead, the qualified party may reroll one die once.
In hybrid mode: use the Player Character's Spirit + Thread Sensitivity (Thread Sensitivity ÷ 10, rounded down) as the pool, as specified in TTRPG compiled stages." Spirit is a TTRPG attribute with no defined board game equivalent. What does a faction roll for this check?
**Correction (PATCH P-26):** "In board game mode, the Forgetting Check pool is: Influence + 1D per Presence marker in T13 (Restoration) OR VTM level (Varfell) OR Wealth ÷ 2 rounded up (other factions, representing the resources they brought to sustain cognitive continuity). Ob 1 (floor applies). Thread-qualified presence (Restoration Weaver this season, VTM 2+) grants −1 Ob, already at floor. A practitioner Player Character present reduces the applicable Ob by 1 in hybrid mode using their actual Thread Sensitivity."

---

## G-07 — VTM Bootstrapping Success Rate on d10

**Location:** B5 Varfell, VTM Bootstrapping.
**Gap:** Bootstrapping: "Roll Influence vs. **Ob 1**. 
- Success or Overwhelming: VTM +1 immediately.
- Failure: Bootstrapping fails. No retry this campaign. Varfell must gain VTM through standard methods only." On d10 with Influence 4 at Ob 2: P(≥2 net successes) ≈ 56%. A once-per-campaign action fails 44% of the time. This is too harsh for a foundational faction mechanic.
**Correction (PATCH P-27):** Reduce Bootstrapping to Ob 1. P(≥1 net success from pool of 4) ≈ 85% — a confident but not guaranteed start. **Add:** "Partial on Bootstrapping: the attempt partially takes hold. Varfell gains a 'Latent VTM' marker. On any subsequent successful Tribune Inward in T9 within 2 seasons, this converts to VTM +1. Failure: attempt fails; Bootstrapping cannot be retried." This preserves Season 1 stakes without making the faction's entire arc hinge on a coin-flip.

---

## G-08 — Restoration Community Weaving with Multiple Presence Markers and Ob1 Floor

**Location:** B5 Restoration, Two Action Types.
**Gap:** Community Weaving: "Ob 2, −1 Ob per Presence marker in territory." With the Ob1 minimum correction, 2+ Presence markers cap Weaving at Ob 1. Previously, 3 markers could theoretically reach Ob −1 (impossible, but the rule wasn't explicit about the floor). The Ob1 floor is now explicit, but this makes mid-to-late Restoration Weaving very reliable (pool of 4 at Ob 1 = ~85% success). This is probably intended — Restoration's power comes from patient Presence building.

---

## G-09 — Standard Muster Ob Not Stated

**Implications for G-01 above.** From simulation context, standard Muster = Ob 2. T11 Breadbasket says "Muster Ob −1" implying base Ob 2 → becomes Ob 1 there. Confirmed by the simulation code ("Crown Legionary Inward T2 (Muster): Military 4 vs Ob 2 (standard muster)"). Resolved in PATCH P-21.

---

## G-10 — Varfell Starting Stats: Mandate and Wealth Discrepancy

**Location:** B5 Varfell (Mandate 3, Wealth 3) vs canonical_timeline.md (Mandate 4, Wealth 4).
**Recommendation:** Keep Varfell at Mandate 3, Wealth 3 for the board game. The lower values create a distinct underdog profile — information-rich, militarily capable, but politically marginalised — that drives Varfell's gameplay identity. Add a design note to B5: "Varfell's starting Mandate 3 reflects their current political isolation, not their full institutional depth. This is intentional. The game rewards building influence through intelligence rather than from a position of legitimacy."

---

## G-11 — Incomplete Institutional Pressure Pressure Advancement Table

| Condition | Institutional Pressure Change |
|-----------|-----------|
| Base: each season | 0 (Institutional Pressure does not advance automatically) |
| Altonian Trade Mission refused (Institutional Pressure 30 event) | +1 |
| Torben complied (sent to Altonia) | −3/season while

**Location:** B4 Accounting Step 4, B2 Clock Environmental Effects.
**Gap:** The Institutional Pressure section in B2 shows threshold EFFECTS but not the ongoing Institutional Pressure ADVANCEMENT formula. "Institutional Pressure per Altonian pressure table" is referenced in B4 but no table appears in the document. From scattered references: Theocracy Counter > 60 → Institutional Pressure +1/season. No base Institutional Pressure advancement is stated.
**Correction (PATCH P-28):** See below.

---

## G-12 — Battle Resolution: No Comparison Mechanic When Both Sides Roll

See I-05 above. PATCH P-16 resolves this.

---

# PART FOUR: COGNITIVE LOAD ANALYSIS

## Load Assessment by System

**Systems at acceptable load (clear, low overhead):**
- Institutional Mandate Uphold/Appease: binary choice, mechanically immediate. Load ≈ 2/10.
- Standing Tokens: simple accumulation/spending. Load ≈ 2/10.
- Casus Belli: well-defined acquisition and effect. Load ≈ 3/10.

**Systems at moderate load (manageable with reference cards):**
- Faction-specific private tracks (VTM, Player Character, RDT, Thread Depth, AER): five concurrent private tracks across factions. Per-player this is one or two tracks. Load ≈ 4/10 per player.


**Systems at elevated load (require careful design attention):**
- Year-End Accounting (10+ steps): fires every 4th season. Adds ~10 minutes per occurrence.

**Cognitive Load Reduction Recommendations:**

**Hybrid addition:** +1.5/10. Total hybrid: 8.0/10 with reference cards.

---

# PART FIVE: MECHANICAL CASCADE CRUNCH

## Cascade Test 1: Church Overwhelming Decree Chain (Season 7, Theocracy Counter 36)

**Setup:** Theocracy Counter 36 (above 30; Church in territory −1 Ob bracket active). Church plays Senator Inward T3 (Decree). Mandate 5, doctrine-aligned −1 Ob, Church-held territory −1 Ob (Theocracy Counter 30–49 bracket). Base Ob 2 − 1 − 1 = Ob 1 (floor applies — already at 1; no further reduction).

**Roll (d10):** 5d10: 10, 8, 3, 7, 1 → 10(×2), 8(×1), 7(×1), 1(-1) = 4 − 1 = 3 net successes. Ob 1, surplus 2 = **Overwhelming.**

**Cascade from Overwhelming Decree:**
1. Decree issued: Legally binding. Non-compliance = Standing −1 per non-complying faction.
2. Mandate check waived (Overwhelming).
4. Attention Pool: "Unexplained structural change" — the Decree itself isn't a Thread operation, no +2. But the HI opening: does the opening of a HI add Attention? No — the HI IS a response to Attention, not a source of it. ✓

**Total immediate effects from this card play:** 3 (Overwhelming Decree binding + free HI + Standing consequence). Within the Cascade Depth Cap of 3. ✓ No queue to Accounting needed.

**But**: The HI itself, when resolved at Accounting Step 5, could trigger:
- If successful (Attention Pool ≥ 3): Theocracy Counter +0.5; AER +1; Restoration potentially loses Presence marker.
- If target is Restoration faction, Restoration may Appease their Mandate (Investigation closes, Mandate −1).
- If Restoration Compromises: their Stability −1 (Appease cost: 1 Standing + 1 Stability).

**Season end cascade from T3 Decree + HI:**
- Theocracy Counter +1 (T3 control) at Accounting.
- +0.5 Theocracy Counter if HI confirmed at Step 5.
- AER +1 if HI confirmed (AER 2 → 3, which triggers: "Institutional Pressure vanguard threshold: 76→80").

**Verdict:** This chain is manageable. Three immediate effects, then deferred accounting effects. The Cascade Depth Cap is doing its job. The queued HI resolution creates appropriate drama but doesn't chain into uncontrolled spirals.

---

## Cascade Test 2: Reformed Settlement Chain (Hafenmark, RDT 5, Season 12)


Church Non-Player Character must respond at Accounting Step 5: Resist, Accommodate, or Ignore.



Effects from Reformed Settlement — Resist:
1. Theocracy Counter +3. Current Theocracy Counter 52 + 1 (Assert) + 3 (Resist) = 56.
2. RDT +1 → RDT 6.
3. Hafenmark +1 Standing vs Church.
4. Hafenmark +1 Deed Token.

**Theocracy Counter 56 triggers:**
5. Assert/Suppress mandatory this season — already fired (Priority 1). But Theocracy Counter 56 is still in the 50–69 bracket (mandatory Assert each season going forward). No new threshold crossed this season unless Theocracy Counter hits 60.

Actually wait: Theocracy Counter 52 + Assert (+1) + Resist (+3) = 56. Theocracy Counter 60 threshold NOT crossed this season. No new environmental effects. ✓

But at RDT 6:
6. "All Diplomatic actions targeting Hafenmark: +1 Ob." This is now permanent for the remainder of the game.

8. **VICTORY CHECK:** Hafenmark declares victory at Accounting Step 12.
9. **Hollow Victory check:** Hafenmark Appease count: assume 2 (−1 Deed effective). Effective Deeds: 3 − 1 = 2. Path A requires 3. Hafenmark CANNOT declare victory — Hollow Victory modifier reduces effective Deed count below threshold.

> **Clarification (PP-035):** "Hollow Victory applies only to Deed-counting factions (Hafenmark, Guilds, and any faction whose victory condition uses a Deed or similar countable token). Restoration's presence-based victory condition (Rendering Stability ≥ 50) and Löwenritter/Crown's mandate-based conditions are not Deed systems. Hollow Victory does not apply to these factions."

**Verdict:** The Reformed Settlement chain fires 6-7 effects in one resolution window. The Cascade Depth Cap of 3 immediate effects prevents some of these from applying instantly — specifically: the Theocracy Counter gain, RDT gain, and Deed confirmation must queue to Accounting rather than applying mid-Phase. This is correct behavior per the cap rule. The cap prevents a single card play from immediately triggering a victory declaration within Phase 4.

**Gap identified:** The Cascade Depth Cap says "more than 3 immediate mechanical effects in one resolution step." Are clock changes (Theocracy Counter +3 from Resist) "immediate mechanical effects"? If yes, the Reformed Settlement Resist triggers ONLY 3 immediate effects (Theocracy Counter +3, RDT +1, Standing +1) with the Deed Token queuing to Accounting. If the Deed Token queues, Hafenmark cannot win this season unless accounting resolves and confirms. This is correct. **The Cascade Depth Cap is a genuine pacing tool.** Confirm that clock changes count against the 3-effect cap. Add this to PATCH P-29.

---

## Cascade Test 3: Varfell VTM 5 + Co-Movement + Rendering Stability Trigger

**Setup:** Rendering Stability 38 (below 40; Thread operations Ob −1 globally active; but Ob1 floor applies). Varfell VTM 5. Varfell plays Pontifex (Senate Market, Thread operation) in T12. Declares Actualized dimension outcome before drawing (VTM 5 ability): chooses Rendering Stability +1 (stabilize).

**Thread Operation Procedure:**
1. Declare: Pontifex, T12, Weaving (stabilization).
2. Against temporal flow check: Rendering Stability is below 30? No (Rendering Stability 38). Prior Thread Debt in T12? Assume yes — 1 token present. → Thread Debt incurred. +1 Ob to NEXT operation here (per PATCH P-24 correction).
3. Ob modifiers: base Ob 2, Thread Witness Node in T12? Assume yes (+1 additional Co-Movement draw later). Rendering Stability environment (49–30): Thread operations −1 Ob. Ob 2 − 1 = Ob 1 (floor). Thread Debt existing: this doesn't increase THIS operation's Ob (per PATCH P-24 — the debt affects the NEXT operation, not this one). Ob 1.
4. Roll: VTM 5 ability — Varfell doesn't roll VTM as a stat directly. Thread operations use Influence. Influence 4 + VTM modifier? VTM 5 benefits: "choose the Actualized dimension outcome of one Co-Movement card draw." The roll itself uses Influence vs Ob.
   Roll 4d10: 9, 7, 2, 10 → 9(1), 7(1), 10(2) = 4 net. Ob 1, surplus 3 = **Overwhelming.**

5. Apply result: Weaving Overwhelming in T12 — the stabilization works. Additional effect at Overwhelming: Rendering Stability +1 (from the declared VTM 5 Actualized dimension choice).
6. Co-Movement draw: Thread Witness Node → draw 2 cards. Cards drawn: CM-12 (Ground Stability) and CM-19 (Substrate Assertion).
   - VTM 5 ability: Actualized dimension already declared as Rendering Stability +1. CM-12 Actualized = Rendering Stability +1. CM-19 Actualized = Rendering Stability −3.
   - Per VTM 5: "choose the Actualized dimension outcome of one Co-Movement card draw." Only ONE card's Rendering Stability can be chosen. The other applies normally.
   - Varfell chooses CM-12 as the card for VTM 5 intervention: Rendering Stability +1 applies. CM-19's Rendering Stability −3 applies normally.
   - Net Rendering Stability from this operation: +1 (Overwhelming) + +1 (CM-12 chosen) − 3 (CM-19) = Rendering Stability −1 net. Rendering Stability 38 → 37.

8. Attention Pool: CM-12 = no epistemic. CM-19: Varfell reveals operation type → Church Attention Pool +2.

**Total cascade: Rendering Stability −1, Attention +2, Varfell operation type revealed to all, +1 Ob to next T12 Thread operation (Thread Debt).**

**Verdict:** VTM 5's power is real but bounded. Two Co-Movement draws with Thread Witness Node creates meaningful variance — Varfell chose to stabilize but one of the two cards undercut them. The Rendering Stability outcome (−1 net after trying to stabilize) is appropriately dramatic. Reveal of operation type adds political heat. This is a well-designed climactic moment. **No crunch failure.** The VTM 5 ability is correctly scoped.

---

## Cascade Test 4: Church Theocracy Counter 80 Territorial Seizure



Per-territory roll for Church at Theocracy Counter 80: Church Mandate vs Ob 3 (contested territory) or Ob 2 (allied/neutral).
Territories Church can seize: any non-Church controlled territory.

5 territories to roll on (T1, T2, T6, T9, T14 — example distribution):
- T1 (Crown capital): Church Mandate 5 vs Ob 3. Roll 5d10: 8, 7, 3, 2, 9 → 3 net. Ob 3 = Success. T1 contested (Crown and Church now both present — BATTLE required).
- T2 (Crown): Roll 5d10: 5, 4, 6, 2, 8 → 1 net. Ob 3 = Failure. No seizure of T2.
- T6 (Hafenmark): Roll 5d10: 9, 7, 7, 1, 4 → 3−1 = 2 net. Ob 3 = Partial. "Territory status contested but not seized" — what does Partial mean for Theocracy Counter 80 seizure? **Gap identified below.**
- T9 (Varfell): Roll 5d10: 3, 1, 5, 6, 7 → 1−1 = 0 net. Failure.
- T14 (Restoration): Roll 5d10: 8, 8, 9, 7, 2 → 4 net. Overwhelming. Immediate seizure + no Standing cost for Church.


**Further cascade:** T1 seizure success → Battle between Crown and Church in T1. This:
- Fires a Zoom-In trigger in hybrid mode (Battle in Player Character home territory).
- Triggers Crown Institutional Mandate event (Church in Crown territory without consent).
- Public Instability −1 (Church Territorial Seizure).
- Theocracy Counter +2 (Seizure successful per Theocracy Counter formula).
- AER: if AER ≥ 3, AER adjusts Theocracy Counter formula.

> **P-25: wound conversion:** Wound conversion on Zoom In: 1 personal Wound = Coherence Rating −1 for that character (minimum Coherence Rating 1). Wounds do not convert to unit Strength loss.

**Total effects from one Theocracy Counter 80 seizure roll on T1:** 5+ cascading effects. Only 3 can be immediate per the Cascade Depth Cap — the rest queue. **The Theocracy Counter 80 event is the largest cascade event in the game. This warrants a dedicated resolution checklist card.**

---

# PART SIX: EMERGENT SCENARIOS (Branching Dice Rolls)

## SCENARIO A: The Klapp Awakening — Church-Varfell-Wardens Triangle
*(Season 9, 4-player game. Theocracy Counter 38, Rendering Stability 48, Varfell VTM 3)*


**Klapp Event draws from Named Character Events deck. Card drawn.**

Church player now holds Klapp Active State: +1D all Investigate, Heresy Investigations cost 0 Wealth.

**Following Season (Season 10): Klapp Trajectory Choice fires.**
Varfell VTM 3 is in T9 (adjacent to T3). Trajectory Choice condition met.

**BRANCH A: Church chooses Trajectory A (Suppress)**
- Theocracy Counter +1 (Theocracy Counter 39). Klapp card removed.
- Church player: "We knew. We always know. Klapp's archive will remain sealed."
- Downstream: Varfell player correctly deduces Church suppressed something. Tribune Investigate in T3 (Ob 2, d10 roll): 4d10: 9, 7, 3, 1 → 2-1 = 1 net. Ob 2. Partial: "above or below threshold" for one stat. Varfell learns Church Mandate is "Good" (4-5). No further information. The suppression is opaque.

**BRANCH B: Church chooses Trajectory B (Investigate Further)**
- Theocracy Counter −1 (Theocracy Counter 37). Klapp Active continues.
- Next season (11): **Klapp Discovery Event Roll.** Church: Mandate 5 vs Ob 2.
  - Roll A (5d10): 8, 8, 7, 3, 9 → 4 net. Success. Klapp suspects. Church player notes privately.
    - Church player: Klapp has developed awareness. Trajectory B continues.
    - Himmensendt must Prosecute or Protect Klapp.
      - **Prosecute:** Church Stability −1. AER −1. Theocracy Counter −2. Klapp removed.
      - **Protect:** Himmensendt Renown −1. Klapp Active 1 more season.

*Assume Varfell VTM 4 in this branch.*
- Warden Cooperation +1 (now 2). Theocracy Counter −2 (Theocracy Counter 36). Church Stability −1.
- Church gains limited Thread access: one Senate Market Pontifex/season.
- Varfell: Tribune Outward in T3 (Spy): Influence 4 + VTM 4 (Casus Belli Ob −1 not applicable here) vs Ob 2. Roll 4d10: 10, 8, 2, 5 → 2+1 = 3 net. Overwhelming. Varfell learns of Trajectory C. Klapp's Awakening Milestone fires: **Restoration + Varfell may now collaborate on [NAME-PENDING: ED-048] Ritual research at Warden Cooperation 2 instead of 3.**


---

## SCENARIO B: Varfell Patience Protocol Climax — Season 14, VTM 4+
*(Single-player scenario, Varfell player)*

**State:** Player Character 6 (maximum, VTM 4+). Varfell has not played their Tribune in 6 consecutive seasons except once for Senate Market restraint. Mandate 3, Military 4, VTM 4.

**Spending 6 Player Character for VTM +1 (VTM 4 → 5):**


**Tribune Inward T14 (Thread-active, Restoration Weaving this season):**


> **Clarification (PP-037):** "Co-Movement cards with VTM effects that cannot be applied due to the once-per-season cap or the VTM maximum (7): convert to +1D on the following season's Tribune action in any territory. The converted bonus cannot exceed +2D regardless of how many VTM effects were blocked."

**Roll for Tribune Inward T14 (Investigate the Restoration Weaving):**
Influence 4 (standard Intel) vs Ob 2. Thread Resonance: +1D. Epistemic Reason (Varfell): evidence-based Intel −1 Ob = Ob 1.
Roll 5d10 (Influence 4 + Thread Resonance 1D): 9, 7, 10, 3, 8 → 1+1+2+1 = 5 net. Ob 1, surplus 4 = **Overwhelming.**

Overwhelming Investigate: Restoration's complete stat line revealed + one hidden private track. **Restoration has no private tracks other than their public Presence markers.** The Overwhelming reveals their complete stats (Mandate 2, Influence 4, Wealth 2, Stability 3) plus their active Presence marker locations.


**Downstream intelligence use:** Varfell negotiates with Crown in Phase 2 next season (Open Pledge: share Restoration intelligence in exchange for Crown's Institutional Pressure management commitments). Crown gains 2 seasons' worth of Restoration movement patterns. Varfell gains +1D to all Military actions in Crown-adjacent territories for 2 seasons.


---

## SCENARIO C: Institutional Pressure Crisis Triple Response — Season 11, Institutional Pressure 68
*(4-player game: Crown, Church, Hafenmark, Löwenritter post-coup)*

**State:** Institutional Pressure 68 (Altonian Vanguard imminent — threshold 75; AER 3 raises threshold to 80). Elske Loyalty 4, Contact Established. Torben Tutoring Demand fired (Season 8, Crown complied — Torben in Altonia, Loyalty 1). Löwenritter active post-coup, Public Instability 4.

**Phase 1 Planning:**
- Crown (soft coup, 1 Senator only): Senator Outward T4 (contact Elske, Diplomacy Ob 2).
- Hafenmark: Consul Outward T7 (Trade — Institutional Pressure disruption; T7 Trade at Institutional Pressure 30-59 = +1 Ob). Consul: Wealth 5 vs Ob 2 (standard Trade) + 1 Ob (Institutional Pressure disruption) = Ob 3.
- Church: AER 3 active. Church Non-Player Character Priority 4: "Diplomacy toward Altonia (AER maintenance) if AER < 3." AER 3 ≥ 3, so Priority 4 doesn't fire. Priority 3: Govern T3.

**Phase 4 Resolution:**

**Priority 2 — Military:**
Löwenritter March T5→T4: Military 6 vs Ob 2. Roll 6d10: 8, 9, 7, 3, 7, 2 → 4 net. Ob 2, surplus 2 = Overwhelming. Unit moves to T4; may immediately initiate Battle if enemy present. T4: no enemy units (Vanguard hasn't deployed yet, Institutional Pressure 68 < 75). Territory captured — Löwenritter now controls T4.

**Priority 3 — Domain:**
Hafenmark Trade T7: Wealth 5 vs Ob 3 (Institutional Pressure friction). Roll 5d10: 9, 3, 7, 1, 6 → 2-1 = 1 net. Ob 3. Partial: Wealth +1, but Schoenland demands 1 Wealth at Year-End OR blocks next Trade. Hafenmark chooses to accept the demand (Wealth +1 now, -1 at Year-End = net 0). Why trade? Senate Market purchase opportunity — Hafenmark uses Overwhelming counter-deal from last season to purchase Architect at −1 cost.

**Priority 4 — Social:**
Crown Senator Outward T4 (Elske contact, Diplomacy): Mandate 5 vs Ob 2 (Institutional Pressure 60–74: "Trade disrupted; proxy at T4 +1D military — but this is Diplomacy, not Trade or Military). Ob 2 unchanged for Diplomacy. Roll 5d10: 8, 7, 5, 9, 2 → 3 net. Ob 2, surplus 1 = Overwhelming.
Overwhelming Diplomacy: Elske Loyalty +1 (now 5) AND block one declared Löwenritter order next season at no cost.

**Elske Loyalty 5 at Institutional Pressure < 60? No — Institutional Pressure is 68. The return condition requires Institutional Pressure < 60.** Elske CANNOT return this season despite Loyalty 5. But she is now at the threshold.

**Accounting:**

Institutional Pressure 70: AER 3 holds Vanguard threshold at 80. So Vanguard deploys at Institutional Pressure 80, not 75. The factions have bought 5 more seasons (10 points of buffer at +2/season). **But only if AER stays at 3 or above.**

Crown player correctly identifies: AER 3 is the firewall. If Church Stability drops below 3 (AER −1: AER → 2), or Reformed Settlement occurs (AER −2: AER → 1), the invasion threshold reverts to 75 and Vanguard deploys immediately at current Institutional Pressure 70.

**Threat tree:**
- Hafenmark pursues Reformed Settlement (RDT 5, possible at Season 13): AER −2.
- If AER → 1: Institutional Pressure threshold → 75. Current Institutional Pressure 70 → Vanguard deploys in 3 seasons.

**BRANCH A: Hafenmark proceeds with Reformed Settlement. Church resists. AER −2.**
Institutional Pressure 70, AER 1, threshold reverts to 75. Next season: Institutional Pressure +2 → 72. Season following: Institutional Pressure 74. Season after: Institutional Pressure 76 → Vanguard deploys.

**Löwenritter in T4 with Military 6 vs Vanguard Military 5, Discipline 5:**
Battle: Löwenritter Offensive (+2D, Ob 2) vs Vanguard Balanced (Ob 2).
Löwenritter: Military 6 +2D (Offensive) = 8 dice vs Ob 2. Roll 8d10: 9, 7, 8, 3, 10, 2, 7, 5 → 1+1+1+2+1 = 6 net. Ob 2, surplus 4 = Overwhelming. Vanguard unit destroyed. Löwenritter territory controlled.
Vanguard (defender, Balanced vs Offensive): Discipline 5 +fort? T4 has Fort 2: +2D. Military 5 +2D = 7 dice vs Ob 2. Roll 7d10: 8, 4, 9, 1, 3, 7, 6 → 1+1+1-1 = 2 net. Ob 2 = Success. Löwenritter unit Discipline −2 (from defender's Success — see PATCH P-16 resolution rules).

**Resolution (per PATCH P-16, compare net successes):** Löwenritter 6 net vs Vanguard 2 net. Löwenritter wins by 4 (overwhelming margin). Vanguard unit destroyed; Institutional Pressure does not advance to Season 2 invasion. Institutional Pressure −5 (military rebuff). Institutional Pressure: 76 → 71. Below threshold again. AER consequence: Vanguard repelled → AER −1 (optional, reflect Altonian embarrassment).

**EMERGENT CONCLUSION:** A seemingly inevitable invasion is repelled by a military that sacrificed political legitimacy to get there. The Löwenritter won the battle. But Public Instability = 4, AER = 1 (after Reformed Settlement), and Theocracy Counter = 55. The Church is consolidating. Hafenmark won the Reformed Settlement Deed but may have brought the invasion closer by degrading AER. **This is the exact political-military tension the game is designed to produce.** The system works.

---

# PART SEVEN: COMPARISON TO PRECEDENT GAMES

## Terra Mystica / Gaia Project

**Valoria advantage:** The Institutional Mandate Uphold/Appease system creates emotional investment in faction identity that Terra Mystica never achieves. Players care about their faction's soul, not just their engine.

## Root


## A Feast for Odin / Feast Games
**Comparison:** Complex action selection with cascading production chains. Valoria's Phase 5 Accounting is the most Feast-like element — many simultaneous calculations. The risk is that accounting feels like bookkeeping rather than drama. **Recommendation:** Any accounting step that changes the board state in a visible, narratively interesting way (a clock crossing a threshold, a faction collapsing) should be **announced dramatically** before the numbers are updated. The drama of "Theocracy Counter crosses 50 — Assert/Suppress now mandatory every season" should be a table moment, not a quiet bookkeeping entry.

## Here I Stand / Virgin Queen
- HIS has explicit rules for when the game ends in a shared loss (Ottoman conquest). Valoria's Rendering Stability Rupture = shared loss is correct but the Rendering Stability decline rate (−1/year baseline) is slow. In a 20-season game, Rendering Stability loses ~5 points from baseline alone. Thread operations accelerate this. The shared loss threat needs to feel more immediate in the mid-game.

## Twilight Imperium 4th Edition

---

# PART EIGHT: EQUITY AND BALANCE ANALYSIS

## Church Holy State Victory — Pace Analysis

**Starting Theocracy Counter 22. Target Theocracy Counter 70. Gap: 48 points.**

**Typical gain rate:**
- T3 control (guaranteed start): +1/season
- Assert (Theocracy Counter > 50, mandatory): +1/season from Season ~14+
- Minor sources (Heresy confirmations, Templar deployments): +0.5–1.5/season


**With Hafenmark Baralta suppression (Mandate ≥ 4 passive: −1/season):** Net gain ~1/season before Theocracy Counter 50, ~2/season after. Estimated victory: Season 35–45.



Alternatively, add an additional Theocracy Counter gain source: "Church wins any contested Institutional Mandate dispute (another faction Compromises their Mandate in response to a Church action): Theocracy Counter +0.5." This rewards active Church engagement in political disputes.

---

## Löwenritter Post-Coup Victory — Structural Assessment





---

## Restoration Movement at 5 Players Only


---

## Starting Stat Assessment (all factions)

| Faction | Total Points | Peak Stat | Weakness |
|---------|-------------|-----------|---------|
| Crown | 22 | Mandate 5, Influence 5 | Wealth only 4 |
| Church | 25 | Influence 6 | No Intel; Thread-suppressed |
| Hafenmark | 20 | Wealth 5 | Military 3 |
| Varfell | 18 | Influence 4, Military 4 | Mandate 3, Wealth 3 |
| Restoration | 11 | Influence 4 | Military 0, Mandate 2 |
| Löwenritter | 19 | Military 6 | Influence 2, Mandate 3 |



---

# PART NINE: HYBRID MODE INTERSECTION
<!-- PP-644: hybrid_gaps_v30 decisions propagated 2026-04-13 -->
<!-- Source: designs/hybrid/hybrid_gaps_v30.md (all 17 gaps resolved) -->

All 17 hybrid design gaps resolved and propagated from hybrid_gaps_v30.md.

---

## §9.1 Session Structure (G-075, G-091)

Phase sequence: Personal → Strategic → Cascade.
Personal phase duration: 90–150 minutes (dependent on scene volume).
Strategic and Cascade phases: accounting-driven, no fixed time target.
Session minimum: 1 real-world session per in-game season. No maximum — a season may span multiple sessions if scene volume warrants.
Seasonal accounting fires at end of the session in which the season closes, not mid-session.

---

## §9.2 Information Asymmetry — Fog of War (G-079)

All faction stats (Mandate, Influence, Wealth, Military, Intelligence, Stability) displayed to non-owning players in four qualitative states:

| Display | Underlying value |
|---------|-----------------|
| In ruins | 1 |
| Poor | 2–3 |
| Good | 4–5 |
| Excellent | 6–7 |

Own faction: exact values visible. Intel stat: always hidden from all players regardless of ownership.

---

## §9.3 Cross-System Handoff Rules (G-080)

All consequences batch to the Cascade phase via the Game Master ledger. Exception: if the Game Master judges a consequence is simple enough to track inline (single stat change, no threshold risk), they may apply it immediately. This is a Game Master call, not a player option.

| Handoff type | Resolution |
|---|---|
| Personal action → faction stat change | Batch to Cascade |
| Thread op → clock change | Batch to Cascade (applied in Cascade step 2) |
| Domain Echo from personal scene | Batch to Cascade (applied in Cascade step 1) |
| Board order → TTRPG scene trigger | Fires at start of next Personal phase (see §9.4) |
| Faction stat change → personal consequence | Game Master narrates in next Personal phase scene |
| Non-Player Character action → personal character impact | Game Master narrates; fires in correct scene sequence (§9.4) |
| Clock threshold → institutional response | Fires in Cascade step 3; Game Master queues response for next Personal phase |
| Player Character death → faction state | Fires in Cascade (§9.9) |
| Faction collapse → personal state | Fires in Cascade (§9.10) |
| Flashback → board state | Not permitted (§9.6) |
| Resources spent → Wealth impact | Evaluated in Cascade (§9.7) |
| Expedition absence → faction orders | Handled per §9.11 |

---

## §9.4 Board Game Order → TTRPG Scene Triggers (G-081)

Zoom In trigger: player-initiated only. Non-Player Character actions against players: narrated at board scale unless the Game Master judges it dramatically necessary to Zoom In (rare).
Scene sequencing: when multiple triggers fire simultaneously, the Game Master sequences them by dramatic logic (most consequential first). No strict mechanical priority.

---

## §9.5 Thread Operations in Hybrid (G-083)

Personal Thread operations: batch to Cascade. Thread Debt incurred by personal Thread operations applies to the board only if the TTRPG-scale operation would qualify as "against temporal flow" by TTRPG criteria. The Game Master determines this at the Cascade phase ledger, not the player mid-scene.

Faction Thread orders: resolve as board game Thread orders. Co-Movement Cards drawn at Cascade step 2.

---

## §9.6 Zoom In Criteria (G-085, G-092)

Zoom In occurs when:
- A player initiates it during the Strategic phase (player-triggered)
- A board consequence directly affects a named Player Character or their home territory (mechanical trigger)

Zoom In is restricted to the Personal phase. No Zoom In may be initiated during the Strategic phase itself. Consequences mid-Strategic phase are held and fire at the next Personal phase.

Flashback rule (G-092): No player may initiate a Personal phase flashback scene to alter a Strategic phase outcome already resolved. What has been rolled stands.

---

## §9.7 Resource Spending → Wealth (G-093)

Resource expenditure threshold: 2× rolled net successes. Below threshold = "stressed" — faction takes Wealth −1 at Cascade. Above threshold = sustainable — no Wealth change.

Note: the 2×−1 variant (threshold at 2× Ob minus 1) was tested but produced excessive stress results. 2×rolled is canonical.

---

## §9.8 Cascade Sequence — 5 Steps (G-094)

The Cascade phase resolves all batched consequences in fixed order. Game Master-run; not skippable.

1. Domain Echoes from Personal phase scenes
2. Thread operation clock changes (RS, TT)
3. Clock threshold events (TC, IP, RS band transitions)
4. Board order consequences (Non-Player Character actions, coalition penalties, etc.)
5. Accounting: attribute changes, seasonal caps applied, victory checks

---

## §9.9 Player Character Death in Hybrid (G-086)

On Player Character death:
- Crisis penalty fires immediately: faction loses 1 Stability, 1 Mandate at next Accounting
- Player takes over the highest-loyalty Non-Player Character officer within that faction
- If no valid Non-Player Character officer: player takes over a new Personal Character from a different faction (or the same, with Game Master approval)
- No new Player Characters introduced mid-season — succession resolves at next season boundary

---

## §9.10 Faction Collapse in Hybrid (G-087)

On faction reaching Stability 0:
- Player Character continues playing as a personal character, unaffiliated
- Faction dice bonuses (from board game faction stats) no longer apply to personal rolls
- Player may attempt to reconstitute the faction via Influence Domain Actions (Ob 4, multi-season)

---

## §9.11 Downtime (G-088)

Downtime actions run concurrently with the Strategic phase. A Player Character who declares Downtime cannot Zoom In during that Strategic phase. Downtime results batch to Cascade.

---

## §9.12 CP Awards from Board Game Successes (G-089)

Board game successes generate Character Points (CP) when the successful action is tied to the Player Character's TTRPG Belief arc by the Game Master at Cascade. The Institutional Mandate Uphold/Appease decision is the canonical bridge: Upholding a Mandate in a way that reflects the Player Character's Conviction earns CP even when resolved at board scale.
Criteria: same as TTRPG (Belief engagement, significant Domain Action, Maxim expression).

---

## §9.13 BG Information Gating → TTRPG Scenes (G-090)

Board game discoveries (factional intelligence, revealed stats) may generate TTRPG scenes only if the Player Character has in-scene awareness of the information. Exception: if a board discovery is immediately relevant to the next Personal phase scene (same session), the Game Master may grant limited access without prior in-scene discovery.

---

## §9.14 Player Character Proxy During Expedition Absence (G-095)

A Player Character on an extended expedition (Southernmost, Einhir research) is absent from Strategic phase faction orders. Options:
- Designate a Non-Player Character proxy officer: proxy receives 1 directive per season from the Player Character
- No proxy: faction reverts to Non-Player Character artificial intelligence for that Player Character's orders

---

## §9.15 Thread Debt in Hybrid — Design Note

Thread Debt incurred in personal Thread operations applies on the board only when the Game Master determines the operation was "against temporal flow" by TTRPG criteria (Past-Oriented Pulling, contested operations at RS < 30). Standard Weaving, Mending, and Locking do not generate Thread Debt on the board regardless of RS level.

---

## Summary — 17 Hybrid Gaps Resolved

| Gap | Key decision |
|-----|-------------|
| G-075 | Personal phase 90–150 min; 1 session min/season |
| G-079 | Four qualitative states; Intel always hidden |
| G-080 | Batch to Cascade; Game Master ledger; inline exception at Game Master discretion |
| G-081 | Zoom In player-only; Non-Player Character actions narrated; sequencing by drama |
| G-083 | Thread ops batch to Cascade; Thread Debt gated by TTRPG criteria |
| G-085 | Player-initiated or mechanical trigger; Personal phase only |
| G-086 | Crisis penalty; take over Non-Player Character officer or succession at season end |
| G-087 | Continue as personal character; lose faction dice bonuses |
| G-088 | Downtime concurrent with Strategic phase; no Zoom In during Downtime season |
| G-089 | Board successes → CP when tied to Belief arc by Game Master at Cascade |
| G-090 | Gated by in-scene discovery; exception for immediate-next-scene |
| G-091 | 1 session minimum per season; seasonal accounting at session end |
| G-092 | No flashback to alter resolved Strategic phase outcomes |
| G-093 | Threshold = 2× rolled; below = stressed (Wealth −1) |
| G-094 | 5-step Cascade sequence; Game Master-only; not skippable |
| G-095 | Non-Player Character proxy gets 1 directive/season; else Non-Player Character artificial intelligence |
| Thread Debt | Personal ops: board debt only if against temporal flow (TTRPG criteria) |

