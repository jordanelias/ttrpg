# VALORIA STRESS TEST REPORT
## BG v0.5 Simulation & Patches + Mass Battle v3 — Comprehensive Audit
## Cross-system, within-system, and intersection tests

**Status markers:**
- **[CRITICAL]** — Rules produce wrong or undefined outcomes; blocks play
- **[SIGNIFICANT]** — Ambiguity or conflict that stalls tables; fix before playtest
- **[MINOR]** — Cosmetic inconsistency; no functional impact
- **[QUESTION]** — Design decision required; no error, but author must choose
- **[CONFIRMED]** — Tested; functions correctly

---

# PART ONE: WITHIN-SYSTEM — BG v0.5

## ST-BG-01 — Degree Table Boundary: Net Successes = Ob + 1 vs Ob + 0
**[SIGNIFICANT]**

The v0.5 degree table reads:

| Net Successes | Degree |
|---|---|
| Ob + 1 or more surplus | Overwhelming |
| = Ob | Success |
| Ob − 1 | Partial |
| 0 | Failure |

"Ob + 1 or more surplus" means net successes = Ob + 1. But "= Ob" means net successes = Ob exactly. This is internally consistent on its face. The stress case: **Ob 1, net successes = 2.** Is this Overwhelming (surplus = 1) or Success (surplus = 0, net = Ob × 2 not required)? By the table as written, net 2 at Ob 1 = Overwhelming (net ≥ Ob + 1 = 2). Correct.

But the parent TTRPG ruleset (CP13) defines Overwhelming as "net ≥ 2× Ob." At Ob 1 that is net ≥ 2, which matches. At Ob 2 that is net ≥ 4. The BG formulation "Ob + 1 surplus" at Ob 2 gives Overwhelming at net ≥ 3 — **one success lower than the TTRPG parent**.

**These are different thresholds.** The BG Overwhelming triggers more easily than the TTRPG Overwhelming.

**Decision required:** Which threshold is correct for the BG? "Ob + 1" (BG-as-written) or "2× Ob" (TTRPG parent)? At high Obs this matters significantly: Ob 3, pool of 5 — BG Overwhelming requires net ≥ 4 (~27%); TTRPG Overwhelming requires net ≥ 6 (~11%). The BG version is much more achievable.

---

## ST-BG-02 — Catastrophic Failure Majority-1s: Probability at Pool 2
**[SIGNIFICANT]**

The majority-1s rule: "If dice showing 1 outnumber dice showing 7-10, result is Catastrophic Failure."

At pool of 2: P(2 ones) ≈ 1%. P(1 one, 0 hits) = P(1) × P(2-6) × 2 arrangements = 0.10 × 0.50 × 2 = 10%. So majority-1s fires at pools of 2 roughly 11% of the time (1% + 10%). That is not "uncommon" — it is every ninth roll at pool 2.

The document claims "catastrophic outcomes should be uncommon, not endemic." Eleven percent is too high for "uncommon." For comparison: at pool 4, majority-1s requires ≥ 3 ones against ≤ 2 hits, which drops to roughly 2–3%.

**Implication:** Factions at low stats (Restoration Mandate 2, Revolution Military 2) hit Catastrophic Failure at a meaningful rate on foundational actions. Bootstrapping Varfell at VTM pool 1 (pre-Ob correction: pool 1, Ob 2) would fire Catastrophic ~10% per attempt. This may be intended as a fragility signal for weak factions but should be explicit.

**No patch required if intentional; design note required.**

---

## ST-BG-03 — Catastrophic Failure and the Degree Table: Which Applies?
**[CRITICAL]**

The degree table says net ≤ 0 = Failure. The majority-1s override says if 1s outnumber 7-10, result is Catastrophic Failure "regardless of net success count." 

Edge case: pool of 4, roll 10, 10, 1, 1. Net = 2+2−1−1 = 2. Majority: two 1s vs two 10s — exactly tied, not majority. No Catastrophic. Net 2 = result depends on Ob. ✓ No issue here.

Second edge case: pool of 5, roll 10, 1, 1, 1, 3. Net = 2−3 = −1 (negative). Majority: three 1s vs one 10 = majority. Catastrophic Failure fires. Net is also negative. The document says "treat negative net as 0 for degree purposes." So: do we apply (a) Catastrophic Failure from the override, or (b) Failure from the degree table, or (c) both? 

The document says Catastrophic fires "plus one additional consequence at Game Master discretion." So the Catastrophic override supersedes the degree table in this case. **Confirmed working logic, but only if Catastrophic is explicitly described as a fifth degree that replaces Failure-degree outcomes in that roll.** The current text implies both can apply to the same roll. That needs one sentence of clarification: "Catastrophic Failure replaces, and is not added to, the Failure degree result."

---

## ST-BG-04 — Battle Resolution P-16 (Compare Net Successes): Drawn Battles
**[SIGNIFICANT]**

P-16 adds "compare net successes" to determine victor in B8 battles. The document acknowledges both sides roll. If attacker net = defender net, the outcome table currently covers:

- Attacker Overwhelming: loses one unit destroyed
- Attacker Success: defender Cohesion −2
- Attacker Partial: attacker Cohesion −2
- Attacker Failure: attacker retreats

But P-16 doesn't specify what happens on a dead tie (equal net successes). Does neither side suffer? Does the higher-pool side win? This is the same issue as the Versus Roll tiebreaking from the TTRPG, but it was never imported to B8.

**Patch needed:** "On exactly tied net successes, the battle is drawn — both sides Cohesion −1 and both hold position. Neither side claims territory from this engagement. On subsequent turn, initiating attacker may re-engage or withdraw."

---

## ST-BG-05 — Theocracy Counter 80 Seizure: How Many Territories Simultaneously?
**[QUESTION]**

P-30 addresses Theocracy Counter 80 Partial seizure. Cascade Test 4 shows Church rolling on 5 territories. But the text does not state whether Theocracy Counter 80 triggers rolls on ALL territories or only territories Church declares. If all non-Church territories: with 15 territories and Church in some, this could be 10+ simultaneous rolls, each potentially cascading. The Cascade Depth Cap (3 effects/step) would be overwhelmed.

**Decision required:** Is the Theocracy Counter 80 seizure a declared target or an all-territory sweep? If all-territory, the Cascade Depth Cap must explicitly state how batched Theocracy Counter 80 rolls are handled (treated as a single "Theocracy Counter 80 sweep" event counting as one effect, with individual rolls queuing under that umbrella).

---

## ST-BG-06 — Restoration Rendering Stability ≥ 50 Victory + Hollow Victory Interaction
**[SIGNIFICANT]**

P-17 clarifies "Rendering Stability ≥ 50 must be met at the moment of victory declaration." But the Hollow Victory modifier reduces effective Deed count. If Restoration's Rendering Stability is 52 and they have 5 Presence markers in 5 non-adjacent territories held 2 seasons, but Compromise count reduces effective Deeds to 4 — do they still win? Their Rendering Stability condition is met (52 ≥ 50). Their Deed condition: 5 territories = technically not a Deed system (that's Hafenmark). Restoration's victory condition is presence-based. Rendering Stability is the gate.

The Hollow Victory system appears to apply to Deed-counting factions (Hafenmark). Does it apply to Restoration's presence-based victory? If yes, how? What does "−1 effective Deed" mean for a presence-based win? If no, the Hollow Victory system has asymmetric coverage.

**Clarification needed:** State explicitly whether Hollow Victory applies to Restoration and Löwenritter/Crown (non-Deed factions), and if so, what it reduces.

---

## ST-BG-07 — Ob1 Floor + Restoration Weaving: Late-Game Reliability
**[CONFIRMED — with design note]**

G-08 flags this and says no patch required. The test confirms: at 2+ Presence markers, Community Weaving hits Ob 1. Pool of Influence 4 at Ob 1 = P(≥1 net) ≈ 85%. Confirmed functional and apparently intentional.

However: what if Restoration has 4 Presence markers in one territory (an edge case)? The rule says "−1 Ob per Presence marker." At 4 markers, Ob 2 − 4 = Ob −2, floored at 1. Still Ob 1. The fourth marker does nothing additional. Players will notice this ceiling quickly.

**Design note only:** "Each Presence marker after the second provides no Ob benefit to Weaving in that territory. Markers beyond 2 per territory serve presence-stability purposes only."

---

## ST-BG-08 — Parliamentary Manoeuvre (P-19): "Policy Instrument" Undefined in B3
**[SIGNIFICANT]**

P-19 says the Hafenmark free interrupt applies to "Crown's Policy Instrument only — the once-per-season bonus action if Mandate ≥ 4." But "Policy Instrument" is not defined as a named mechanic anywhere in the provided B3 text. The B3 Action Economy section references "Parliamentary Manoeuvre" and "Senator Inward" but not "Policy Instrument" as a distinct card or mechanic.

If "Policy Instrument" is Crown's exclusive card (implied by the rule), it needs a B3 entry alongside the stat-to-action mapping — both its activation condition (Mandate ≥ 4) and what action it permits. Without this, P-19's patch has no mechanical anchor.

---

## ST-BG-09 — VTM Once-Per-Season Cap (P-31): Interaction with Player Character Spend
**[CONFIRMED with note]**

P-31: "VTM can only advance once per season regardless of source. Player Character spend takes priority." Stress case: what if the Player Character spend fires and VTM advances to 5, but a Co-Movement card that season has an effect reading "VTM +1"? VTM is already at 5. The cap fires from P-31 (already advanced). Is the Co-Movement effect simply lost, or does it convert to another effect?

**Gap:** Co-Movement cards with VTM effects do not state what happens when VTM is already at maximum (7) or when the once-per-season cap has been reached. Add: "Co-Movement VTM effects that cannot be applied due to the once-per-season cap or maximum ceiling: convert to +1D on the following season's Tribune action in any territory."

---

## ST-BG-10 — Standing Token Mechanics: Not Defined in Provided Text
**[QUESTION]**

The cognitive load analysis mentions Standing Tokens with load 2/10. The majority-1s Catastrophic Failure lists "a Standing loss" as a possible additional consequence. But Standing Tokens are never defined in the B3 Core Mechanic text provided. What is their range (0–N)? What do they do? When are they spent vs lost?

This is likely defined in B-sections not included in the provided document. Flagging as a definitional dependency.

---

# PART TWO: WITHIN-SYSTEM — MASS BATTLE v3

## ST-MB-01 — TN 6 for Volley (Phase 2) vs Universal TN 7
**[CRITICAL]**

Mass Battle v3 §A.7 Phase 2 states: "Roll Effective CP vs **TN 6**."

The BG v0.5 document (Part One, Correction 1) establishes: "All rolls use d10. Results per die: 7, 8, 9: 1 success. 10: 2 successes." The TTRPG ruleset (CP13) uses a single TN of 7+ for all rolls, explicitly eliminating TN variation.

Mass Battle v3 retains TN 6 for Volley rolls. This means Volley has P(success per die) = 50% (TN 6 = 6, 7, 8, 9, 10 succeed, counting 10 as 2 successes → 40% standard + 10% bonus), while all other rolls have P(success per die) = 40% (TN 7). **Volley is 25% more accurate per die than melee on the same table.**

This may be intentional (representing the structural advantage of massed ranged fire vs the chaos of melee), but it is not flagged as an intentional exception anywhere in the document. The EDGE references and patch notations do not address this TN discrepancy. TN 5 is used in the BG B.3 ("TN 7" is cited but the disposition table uses TN 5 for mass combat per earlier CP checkpoint documents — and now mass_battle_v3 introduces TN 6 for Volley independently).

**Requires design confirmation:** Is TN 6 for Volley intentional differentiation? If yes, document it as such. If no, update to TN 7.

---

## ST-MB-02 — Coherence: Undefined Concept in BG Context
**[CRITICAL]**

§A.10 references "Coherence" extensively: "Coherence auto-cost −1/op," "Severed (Coherence 1) general," "Coherence depletion warning." The BG unit stats (§B.2) have no Coherence field. The TTRPG character stat "Coherence" does not appear in CP13 (which uses Composure, not Coherence). 

"Coherence" appears to be a practitioner-specific stat — separate from Composure and from unit Cohesion — introduced in a document not provided (likely stage5_clocks.md or a practitioner character sheet supplement). It is referenced in mass_battle_v3 as if self-evident.

**Blocking gap:** §A.10 is unplayable until Coherence is defined. What is its starting value? How is it calculated? What happens when it reaches 0 beyond the noted "Severed (Coherence 1): +2 Ob" state?

---

## ST-MB-03 — Effective CP Calculation: Simultaneous Damage Application
**[SIGNIFICANT]**

Effective CP = min(CP, current Strength). Phase 4 has simultaneous damage: "Both sides take Strength damage simultaneously." But the Effective CP calculation uses "current Strength." If damage is simultaneous, do both sides calculate Effective CP using their Strength *before* this turn's damage? Or *after*? 

The answer matters for multi-unit engagements where a unit is taking Strength damage from multiple sources in Phase 4. A unit at Str 4 hit by two simultaneous engagements totaling 5 damage ends at Str 0. When the second engagement calculates its opponent's Effective CP, does it use Str 4 (pre-damage) or Str 0 (post first-engagement damage)?

**Proposed clarification:** "Effective CP is calculated at the start of Phase 4 using Strength as of Phase 3 end. All damage within Phase 4 is applied simultaneously at Phase 5 Step 1. CP cannot change within a single Phase 4."

---

## ST-MB-04 — Morale Cap −3 per Cascade Phase: General Kill Interaction
**[SIGNIFICANT]**

§A.4: "Morale cap: −3 per Cascade Phase. General killed (Stage 2) deals −2 separately, not subject to the cap."

Stress case: In one Phase 5 Cascade, the following all occur:
1. Str drops below 50%: −1 Morale
2. Cohesion broken: −1 Morale  
3. Allied unit routed: −1 Morale (cap reached — this is the −3 maximum)
4. General killed Stage 2: −2 Morale (separate, outside cap)

Total: −5 Morale. A unit at Morale 5 becomes Morale 0 and routs.

This seems extreme but is actually a plausible design feature — when your general dies during an already-collapsing battle, catastrophic rout is realistic. However, "general killed (Stage 2) deals −2 separately, not subject to the cap" creates ambiguity: is the −3 cap applied first and then −2 added? Or does the cap not even begin to accumulate until all non-general sources are counted?

**Proposed clarification:** "Apply all non-general Morale changes first, capping at −3. Then apply Stage 2 general death −2 additionally. Total Morale loss in one Cascade Phase: maximum −5."

---

## ST-MB-05 — Coherence Rating = 0 After General Stage 2 Death: Uncommanded Units
**[SIGNIFICANT]**

§A.5: "Stage 2 (killed): Coherence Rating = 0, all units uncommanded." §A.4: "Units beyond Coherence Rating limit fight at Line formation, Cohesion = 1 floor, no tactics available." With Coherence Rating = 0, the sub-unit limit is 0. Does the "units beyond Coherence Rating limit" rule apply when Coherence Rating = 0 (meaning ALL units are beyond the Coherence Rating limit)?

Stress case: A Coherence Rating = 0 state means every unit fights at Line, Cohesion floor 1, no tactics. This is severe but survivable for strong units. A unit at Cohesion 3, CP 5, Str 6 retains significant combat effectiveness under these conditions. However, with Morale floor suspended (Stage 2 also suspends the floor), the same unit might rout on any Morale trigger.

**Confirmed as working — Coherence Rating = 0 triggering "all units uncommanded" + Line formation + Cohesion floor 1 is coherent but brutal.** Add explicit example to the rules to prevent table disputes.

---

## ST-MB-06 — Reserve Units: Timing vs Phase 3 Manoeuvre
**[SIGNIFICANT]**

§A.6: "Reserve: Cannot engage. Commits at Phase 3 start of NEXT turn." §A.7 Phase 3: "Reserve commitment declared here (takes effect next turn's Phase 3)."

This creates a two-turn lag: declare Reserve in Phase 3 of Turn N → commits in Phase 3 of Turn N+1. But at Phase 3 of Turn N+1, the unit "commits" — does it immediately become available for Phase 4 engagement in Turn N+1, or does commitment mean it transitions out of Reserve status and is available from Phase 4 of Turn N+1?

Stress case: a general in Turn N declares a unit to Reserve. Turn N+1, Phase 3, they commit. Turn N+1, Phase 4 — can this unit engage? The phrasing "commits at Phase 3 start of NEXT turn" suggests yes, it's available for the Phase 4 of that same turn. This seems correct but should be explicit: "Reserve commitment at Phase 3 makes the unit available for Phase 4 engagement that same turn."

---

## ST-MB-07 — Shield Wall vs Two-Front Flanking
**[CONFIRMED with edge case]**

§A.6: "Shield Wall: Negates flanking from one declared side per turn. Second flank from opposite side applies normally." Stress case: three-sided encirclement (front + both flanks). Shield Wall negates ONE declared flank. The front and the other flank both apply normally.

Front: Shield Wall has −1D Off, +2D Def. The defender faces front attack at full +2D Def advantage. Left flank: negated (declared). Right flank: full flanking bonus applies to attacker. 

This is the intended "Shield Wall can't negate everything" design. The question is whether the "second flank applies normally" language covers a THIRD engagement (front + right + left simultaneously). With Coherence Rating = 3 max, attacker could have front, left, right simultaneous. Shield Wall handles left and front but the right applies normally. Three-way Coherence Rating = 3 vs Shield Wall is functionally two unmitigated engagements plus one defended — working as designed.

---

## ST-MB-08 — Feigned Retreat Counter: "Coherence Rating Ob 2 to recognise"
**[SIGNIFICANT]**

§A.8 Tactics: "Feigned Retreat | Disengage; pursuer Cohesion check; re-engage next turn with flank | 3 | Coherence Rating Ob 2 to recognise."

"Coherence Rating Ob 2 to recognise" means the opposing general makes a Coherence Rating check against Ob 2 to identify the Feigned Retreat as a feint (not a genuine retreat). What is the pool for this check? The Coherence Rating rating itself? "Coherence Rating dice" would mean — rolling Coherence Rating in d10s? Coherence Rating is a derived stat (⌈(Presence + Cognition) ÷ 2⌉), not a stat with defined pool dice.

**Gap:** The recognition check needs a pool defined. Proposed: "Roll a number of d10s equal to the general's Coherence Rating score, against Ob 2." This is consistent with the Rally check pattern (Coherence Rating dice vs Ob). But this is not stated.

---

## ST-MB-09 — Southernmost Thread Sensitivity < 30 Rule: Faction with Mixed Forces
**[SIGNIFICANT]**

§A.11: "Non-Thread-sensitive units (Thread Sensitivity < 30) cannot operate in Southernmost. They dissolve without awareness on entry — no casualties, no Morale trigger, no Cohesion check. Remove from battle map."

Stress case: A force enters the Southernmost with 3 units. Unit A: Thread-sensitive soldiers (Thread Sensitivity 30+). Unit B: mixed Thread Sensitivity. Unit C: no Thread sensitivity. Unit C dissolves. But what counts as "the unit"? In TTRPG, units are abstract formations. Does the unit dissolve if ANY soldier has Thread Sensitivity < 30 (i.e., the majority of the formation)?

The rule "All individuals in a military force operating in Southernmost must personally have Thread Sensitivity ≥ 30" resolves this for strict reading: if even one individual lacks Thread Sensitivity 30, they dissolve. But a "unit" as a block: does the whole unit dissolve when some individuals dissolve, or do the non-sensitive individuals simply vanish while sensitive ones remain?

**For the TTRPG:** "Dissolve without awareness" means the unit's Strength reduces proportionally to the non-sensitive fraction, and the formation's effective CP drops. But this interpretation is not in the text. The text says "remove from battle map" — which implies the whole unit vanishes if it contains ANY non-sensitive individual, since "all individuals must have Thread Sensitivity ≥ 30."

**Practical gap:** How does a faction form a Southernmost-capable force at game start? Only Restoration communities and Varfell VTM 2+ can plausibly field Thread-sensitive units. This means the Southernmost is militarily inaccessible to Crown, Church, Hafenmark, and Niflhel regardless of military strength.

---

## ST-MB-10 — Woven Unit Brittleness: Shifting Object Formation
**[QUESTION]**

§A.14: "Taking Str loss > Cohesion in a single turn qualifies as a non-Thread event of sufficient severity — Game Master may rule the Woven configuration shatters into a Shifting Object."

A Woven unit that takes a Str loss of 5 with Cohesion 4 would shatter. But the Shifting Object rule (TTRPG §14) says Shifting Objects have variable stats per scene — "a weapon's damage bonus changes; a document changes between readings." A unit-sized Shifting Object would be a monstrous formation that changes its attack stats each turn.

**Design question:** Is a unit-scale Shifting Object something that should occur during battle? The implications are significant — the Game Master has to track and apply shifting stats turn-by-turn for what was formerly a regular unit. This is a very high cognitive load mid-battle. **Recommend:** "Unit Woven configurations that shatter into Shifting Objects do so at battle resolution, not within battle. A shattered Woven unit fights at Line formation, Cohesion 1 for the remainder of the battle, and the Shifting Object status is registered for post-battle Thread consequences."

---

# PART THREE: INTERSECTION STRESS TESTS

## ST-INT-01 — BG Battle Resolution (P-16) vs TTRPG Mass Battle (A.7): Same Roll or Different?
**[CRITICAL]**

BG B.3 battle resolution: "Pool = sum of all engaged unit Martial values + commander bonus. TN 7. Net successes = damage dealt."

TTRPG A.4/A.7: "Effective Combat Pool = min(CP, current Strength). Phase 4: Per engagement: Effective Pool → apply Formation modifier → split into Offence/Defence → roll → net hits = Offence succs − Defence succs → Damage = max(0, net hits + weapon modifier − DR)."

These are **fundamentally different resolution systems:**
- BG: single pool (sum of Martial stats), single roll, net successes = damage directly
- TTRPG: per-unit pools, split Offence/Defence, subtracted from each other, then weapon modifier and DR applied

The BG hybrid handoff (§B.5) says: "Player Character faction leader present in contested territory: BG resolution defers to TTRPG mass battle rules." But the stat translation table maps BG Martial to TTRPG CP. These are not the same: BG pools aggregate (sum all Martial values), TTRPG pools cap at individual unit CP. A 4-unit BG force with Martial 3+3+3+3 = pool 12D. TTRPG equivalent: 4 units at CP 3 each, max 3 sub-unit engagements simultaneously, each with pool 3D.

**The two systems produce dramatically different dice pool sizes for the same force.** A BG-to-TTRPG handoff mid-battle could see a force that was rolling 12D suddenly rolling at most 9D across 3 engagements. This is not trivial and could swing outcomes dramatically.

**Patch needed:** Define a conversion formula that produces comparable expected outcomes across both systems, or explicitly state that the two systems will produce different expected results and that TTRPG mode is more tactically granular but not statistically equivalent to BG mode.

---

## ST-INT-02 — Commander Bonus Formula: BG (Military ÷ 3) vs TTRPG (Coherence Rating = ⌈(Pres+Cog)÷2⌉)
**[SIGNIFICANT]**

BG §B.3 EDITORIAL: "Commander bonus = faction Military ÷ 3, round down."
TTRPG §A.5: "Coherence Rating = ⌈(Presence + Cognition) ÷ 2⌉."

In BG mode, the commander bonus is a function of the *faction's Military stat*, not the individual commander's personal attributes. In TTRPG mode, Coherence Rating is an individual attribute calculation. The hybrid handoff says "TTRPG general Coherence Rating → BG commander bonus (Coherence Rating ÷ 2, round down)." But BG mode normally doesn't use Coherence Rating at all.

These three formulas (Military ÷ 3, Coherence Rating from Pres+Cog, Coherence Rating ÷ 2 for handoff) produce different values for the same general:

Example: Serena (Presence 4, Coordination 4, faction Military 4).
- BG mode: 4 ÷ 3 = +1D commander bonus
- TTRPG mode: Coherence Rating = ⌈(4+4)÷2⌉ = ⌈4⌉ = 4. Coherence Rating = 4
- Hybrid handoff: 4 ÷ 2 = +2D bonus (higher than the BG formula!)

The hybrid handoff gives Serena a HIGHER commander bonus than pure BG mode. This inconsistency means transitioning from BG to TTRPG mid-battle (when a Player Character arrives) actually improves the force's effectiveness at the command level.

**This should be an explicit design decision, not an accident.** State whether this is intentional (PCs are better generals than Non-Player Character faction leaders, reflecting their attribute investment) or whether the formulas need alignment.

---

## ST-INT-03 — Thread Operation TN: BG (PATCH P-21 references B6, TN 7) vs TTRPG (§A.10 Volley TN 6)
**[SIGNIFICANT]**

The BG Standard Action Ob table (PATCH P-21) includes "Thread operation (base): Ob 2." This uses TN 7 (the standard d10 system). 

TTRPG mass battle §A.10 (Thread in mass battle) doesn't specify TN separately — it inherits from the TTRPG core (TN 7).

But §A.7 Phase 2 Volley uses TN 6.

The inconsistency exists within mass_battle_v3 itself (Volley TN 6 vs all-else TN 7), but it propagates to the BG-TTRPG hybrid because Ranged/Artillery units in BG (§B.2) have the Volley keyword. When those units are in a hybrid battle (BG Ranged unit converted to TTRPG Projectile unit), do their Volley attacks use TN 6 (TTRPG mass battle) or TN 7 (BG standard)?

**The answer is whichever system's mass battle rules apply.** But this is not stated. If TTRPG battle rules apply in hybrid mode (§B.5), then hybrid Volley uses TN 6. If BG rules continue to apply to unit stats even in hybrid mode, TN 7. **State explicitly which TN applies to Volley in hybrid mode.**

---

## ST-INT-04 — Military Stat Change on Unit Destruction: Seasonal Cap Interaction
**[SIGNIFICANT]**

§A.13 FACTION-P2-02 (proposed, EDITORIAL): "Unit destroyed: faction Military −1 (subject to ±2/season cap)."

BG v0.5 §B4 Accounting (Correction I-04 vicinity): Domain Actions are also capped at ±2 per season for faction attributes. If a faction loses 3 units in one season of battles, their Military would drop −3. But the ±2 cap means it drops only −2 through Domain Actions. Does the military loss from battle count against the same ±2 cap as Domain Actions?

If yes: a faction that loses 2 units in battle (−2 Military, hitting the cap) cannot be further weakened through Domain Actions targeting Military the same season. This creates a perverse protection: suffering catastrophic military losses immunises you from political military-weakening actions for that season.

If no: the two systems stack, meaning a faction can lose up to −4 Military in one season (−2 from battles + −2 from Domain Actions).

**Decision required:** State whether the seasonal cap applies separately to battle outcomes and Domain Actions, or pooled.

---

## ST-INT-05 — Faction Collapse at Military 0: BG vs TTRPG Outcomes
**[SIGNIFICANT]**

BG v0.5 Faction Collapse (P-15): "All OTHER attributes freeze at their pre-collapse values." This applies when Stability hits 0. But what if Military hits 0 via unit destructions (§A.13)? The collapse rule is triggered only by Stability = 0 (per B4 Accounting). Military = 0 is not mentioned as a collapse trigger.

A faction could theoretically have Military 0, Stability 3 — all units destroyed, no ability to field new ones, but still politically active. In BG terms, they can't play Legionary cards but can continue with Senator, Consul, Tribune. This may be correct (political vs military collapse are distinct), but it needs an explicit statement.

**Specifically:** Can Muster (Legionary Inward) still be played at Military 0? If Muster produces a unit with CP = Military ÷ 2 = 0, the resulting unit cannot roll any dice. Is this intended? **Propose:** "At Military 0, Muster actions produce no units and may not be taken."

---

## ST-INT-06 — BG Unit Tokens vs TTRPG Thread Sensitivity Requirement
**[CRITICAL]**

§A.11: "All individuals in a military force operating in Southernmost must personally have Thread Sensitivity ≥ 30."

BG unit tokens (§B.2) have no Thread Sensitivity stat. Knights Templar, Cavalry, Heavy Infantry — none carry Thread Sensitivity tracking. There is no mechanism in BG mode for a unit to "have" Thread Sensitivity.

Hybrid handoff (§B.5) says BG territory consequences apply even in TTRPG battle mode. If a battle occurs in the Southernmost:
- TTRPG rules apply (Player Character present)
- TTRPG Southernmost rule fires: units dissolve unless Thread Sensitivity ≥ 30
- But the BG units transitioning into TTRPG mode have no Thread Sensitivity value

**What Thread Sensitivity do BG units get when translated to TTRPG?** No rule exists. The BG-to-TTRPG stat translation (§B.5) maps Martial → CP, Cohesion → Cohesion, Morale → Cohesion check, but is silent on Thread Sensitivity.

**Proposed bridge rule:** "BG units translating to TTRPG mode in Southernmost: Thread Sensitivity = 0 unless the deploying faction has a designated Thread-capable asset (Restoration Weaver marker, Varfell VTM 2+) in that territory. Church Templar units have Thread Sensitivity 0 by default (doctrinally prohibited Thread sensitivity) and dissolve in Southernmost. Restoration and Varfell units with Thread designations have Thread Sensitivity 30 for Southernmost purposes."

---

## ST-INT-07 — BG Thread Operations via Co-Movement vs TTRPG Thread Operations: Same Thread Tension/Rendering Stability Effect?
**[SIGNIFICANT]**

BG Co-Movement cards produce Rendering Stability effects (the BG equivalent of Thread Tension/Rendering Stability). TTRPG Thread operations produce Rendering Stability changes via the TTRPG formulas (BG document uses Rendering Stability; TTRPG uses Thread Tension; EDGE-06 notes these must be reconciled with inversion). 

If a practitioner Player Character performs a Weaving (Overwhelming) in TTRPG mass battle mode, the TTRPG result is Thread Tension −1. Per EDGE-06, "Thread Tension +N → Rendering Stability −N." So Overwhelming Weaving = Rendering Stability +1 in BG terms. But in BG mode, the equivalent Thread action via Co-Movement might produce Rendering Stability +1 from the "Ground Stability" card. These should be equivalent, and for a single Weaving they appear to be.

**But the scales diverge on major operations.** Ceiral Ritual (TTRPG): Rendering Stability +6 to +10. No BG Co-Movement card produces Rendering Stability +6 in a single draw. If the Ceiral Ritual is performed in hybrid mode (Player Character practitioners present), the Rendering Stability gain from TTRPG rules would dwarf anything achievable in BG mode. This creates a strong mechanical incentive for players to always perform major Thread operations in TTRPG mode rather than through Co-Movement cards.

**Decision required:** Is this asymmetry intentional (PCs and TTRPG mode produce larger Thread consequences than board game abstractions)? If yes, confirm. If no, the Ceiral Ritual's Rendering Stability effect needs a BG Co-Movement cap or the Co-Movement effects need scaling.

---

## ST-INT-08 — Muster Output (FACTION-P2-03): Str=2 vs BG Existing Unit Health
**[SIGNIFICANT]**

§A.13 FACTION-P2-03: "Muster action produces 1 unit with Strength = 2, CP = faction Military ÷ 2 (round up)."

BG §B.2 unit tokens have Health values of 8–11 (Light Infantry Health 9, Heavy Infantry Health 10, etc.). Hybrid translation §B.5: "TTRPG unit Strength → BG unit Health (Str × 1.5, round up — Str 4 ≈ Health 9)."

A Mustered unit (Str = 2) translates to BG Health = 2 × 1.5 = 3. But the lowest Health on a standard BG unit token is 8 (Artillery). A Mustered unit has Health 3 — far below the minimum on any pre-printed token.

**This means Muster creates units that are mechanically off the token scale.** They cannot use pre-printed tokens without confusion. Either:
(a) Mustered units use custom tokens showing Str and Health, not matching pre-printed values — this adds component complexity.
(b) Muster output needs to be scaled to match BG Health ranges (e.g., Str = 5, CP = Military for a fresh unit starting at baseline BG Health).
(c) Muster is a TTRPG-only mechanic that doesn't translate to BG unit tokens.

**Design decision required.** Recommend (c) with explicit statement.

---

## ST-INT-09 — Battle Outcome → Faction Stat Consequences: Domain Echo Timing
**[SIGNIFICANT]**

§A.13 FACTION-P2-02: "Unit destroyed: faction Military −1 (subject to ±2/season cap)."

BG v0.5 Domain Echoes apply at Accounting (not immediately). But military losses in battle are immediate tactical facts. Does the Military −1 from unit destruction:
(a) Apply immediately when the unit reaches Str 0 (within the battle)?
(b) Queue to the season's Accounting like Domain Echoes?

If (a): a faction that loses its only unit in a battle immediately cannot use Military-dependent abilities for the rest of that season's Phase 4. This has dramatic tactical implications.

If (b): the faction's Military stat doesn't change during the season, only at Accounting. This feels disconnected — you just lost an army and your Military 4 is unchanged until year-end.

**The answer is almost certainly (b) for BG purposes (Domain Echo timing) and (a) for TTRPG purposes (immediate world-state consequence).** This creates a discrepancy in hybrid mode: in TTRPG battle, military losses may immediately downgrade future unit quality; in BG, they queue to Accounting. **State the distinction explicitly.**

---

## ST-INT-10 — Church Military Victory → Theocracy Counter Change: CLOCK-EDIT-02
**[QUESTION]**

CLOCK-EDIT-02 (open editorial): "Church military victory → Theocracy Counter change. No Theocracy Counter change from military victory alone (confirm)."

This has significant gameplay implications. If Church captures T3 (their capital) militarily, Mandate +1 and Theocracy Counter +1 (control of a holy site), but not a dedicated military-Theocracy Counter modifier. But in TTRPG mass battle, a Church army Weaving its soldiers (boosting Cohesion) generates Rendering Stability consequences from Thread operations. Does the Thread work involved in fielding a Church military force produce Rendering Stability changes independent of the military outcome?

The question isn't just "does winning a battle change Theocracy Counter" but "does the means of fighting (Thread-Woven Church forces) change Theocracy Counter regardless of outcome." §A.10 says all Thread operations in mass battle generate Rendering Stability drift via standard operation rules. So a Church army using Woven soldiers would produce Rendering Stability consequences from the Weaving, not from the victory.

**Confirm and state:** "Military victory itself produces no Theocracy Counter/Rendering Stability change. Thread operations performed during the battle produce standard Rendering Stability changes per §A.10."

---

## ST-INT-11 — Anti-Armour Keyword (BG) vs DR Table (TTRPG): Equivalence
**[CONFIRMED with note]**

§B.2 Anti-Armour keyword: "+2D when targeting Heavy Infantry, Cavalry, or Knights Templar." This approximates the TTRPG DR table outcome where HeavyBlunt vs Heavy armour has DR 1 (lowest of any weapon against Heavy), meaning HeavyBlunt is the only weapon that can reliably damage heavily armoured units.

Test: TTRPG HeavyBlunt vs Heavy armour DR table: DR = 1. In TTRPG, net hits after DR yields damage. In BG, +2D replaces the DR calculation. At pool 5 at Ob 2, +2D raises the pool to 7D, going from ~42% to ~69% of hitting Ob 3 net. This is a meaningful bonus that roughly captures "HeavyBlunt bypasses Heavy armour" without requiring per-die DR subtraction.

The approximation works but is not mathematically exact. For a playtest this is acceptable. **Confirmed functional.**

---

## ST-INT-12 — Altonian Invasion Unit Stats (CLOCK-EDIT-01): Blocking Gap in Hybrid Mode
**[CRITICAL — blocking]**

v0.4-NEW-02 and CLOCK-EDIT-01 are both marked Blocking: "Battle Tactic Card deck" and "Altonian invasion unit stats."

In hybrid mode (§B.5), if the Altonian Vanguard deploys at Institutional Pressure 75+ and the Player Character faction is defending, "BG resolution defers to TTRPG mass battle rules." The TTRPG mass battle rules require unit stat blocks (Strength, CP, Cohesion, Morale, Weapon, Armour) for the Altonian units. Without CLOCK-EDIT-01 resolution, a hybrid battle against Altonia is impossible — the Game Master has no unit stats to work with.

**This is the highest-priority blocking item in the entire stack.** All scenario simulations involving Altonia (Scenario C in Part Six of the BG document) are provisional. The Institutional Pressure 68 scenario is playable to the threshold but not through invasion resolution.

---

## ST-INT-13 — TTRPG Wound Penalty +1 Ob vs BG Stat Abstraction
**[MINOR]**

TTRPG mass battle §A.5: "Wounds carry over: Wounds from personal combat add +1 Ob to Coherence Rating tactic execution rolls."

BG mode has no wound tracking — faction leaders don't have Health/Wound mechanics in the board game. But in hybrid mode, a Player Character general who took wounds in a prior personal combat scene would have +1 Ob to their Coherence Rating checks.

This is a minor hybrid-mode consistency issue. When a Player Character transitions from TTRPG personal combat (where they took wounds) to BG mode (where wounds are not tracked), do the wound Ob penalties carry into their BG-mode commander bonus?

**Proposed:** "In hybrid mode, wound Ob penalties from TTRPG personal combat apply to the Player Character's Coherence Rating checks in TTRPG mass battle. They do not reduce the commander bonus calculation in BG mass battle (which uses Military ÷ 3, not Coherence Rating). This is the intended distinction between the two modes."

---

# PART FOUR: CONSOLIDATED PRIORITY LIST

## Critical — Fix Before Playtest

| ID | Issue | System |
|----|-------|--------|
| ST-MB-01 | TN 6 for Volley vs universal TN 7 | Mass Battle v3 |
| ST-MB-02 | Coherence undefined as a stat | Mass Battle v3 |
| ST-INT-01 | BG vs TTRPG battle pool sizes incompatible | Intersection |
| ST-INT-06 | BG unit tokens have no Thread Sensitivity; Southernmost rule breaks | Intersection |
| ST-INT-12 | Altonian invasion unit stats missing (blocking) | Intersection |
| ST-BG-03 | Catastrophic Failure and Failure degree: which applies? | BG v0.5 |
| ST-BG-01 | Overwhelming threshold: Ob+1 (BG) vs 2×Ob (TTRPG) | BG v0.5 |

## Significant — Fix Before Distribution

| ID | Issue | System |
|----|-------|--------|
| ST-BG-02 | Catastrophic Failure rate at pool 2: ~11% | BG v0.5 |
| ST-BG-04 | Drawn battles undefined | BG v0.5 |
| ST-BG-05 | Theocracy Counter 80 seizure scope not stated | BG v0.5 |
| ST-BG-06 | Hollow Victory + non-Deed faction interactions | BG v0.5 |
| ST-BG-08 | Policy Instrument not defined in B3 | BG v0.5 |
| ST-BG-09 | Co-Movement VTM effects at cap: no conversion rule | BG v0.5 |
| ST-MB-03 | Simultaneous damage and Effective CP timing | Mass Battle v3 |
| ST-MB-04 | Morale cap and general kill application order | Mass Battle v3 |
| ST-MB-05 | Coherence Rating = 0 uncommanded units + suspended Morale floor | Mass Battle v3 |
| ST-MB-06 | Reserve commitment timing within same turn | Mass Battle v3 |
| ST-MB-08 | Feigned Retreat recognition pool undefined | Mass Battle v3 |
| ST-MB-09 | Mixed Thread Sensitivity forces in Southernmost | Mass Battle v3 |
| ST-MB-10 | Woven unit Shifting Object: mid-battle vs post-battle | Mass Battle v3 |
| ST-INT-02 | Three conflicting commander bonus formulas | Intersection |
| ST-INT-03 | Volley TN in hybrid mode | Intersection |
| ST-INT-04 | Military loss cap: shared or separate from Domain Actions | Intersection |
| ST-INT-05 | Military 0: Muster and collapse implications | Intersection |
| ST-INT-07 | Ceiral Ritual Rendering Stability gain vs Co-Movement scale | Intersection |
| ST-INT-08 | Muster Str=2 → BG Health 3: off token scale | Intersection |
| ST-INT-09 | Military loss timing: immediate vs Accounting | Intersection |
| ST-INT-11 | Theocracy Counter change from military victory (CLOCK-EDIT-02) | Intersection |

## Minor / Design Notes

| ID | Issue | System |
|----|-------|--------|
| ST-BG-07 | Presence marker ceiling at 2 for Weaving Ob | BG v0.5 |
| ST-BG-10 | Standing Tokens undefined in provided B3 text | BG v0.5 |
| ST-MB-07 | Three-way flanking vs Shield Wall | Mass Battle v3 |
| ST-INT-10 | Church military victory Theocracy Counter confirmation | Intersection |
| ST-INT-13 | Wound penalties in BG vs TTRPG mode | Intersection |

---

# PART FIVE: SUMMARY ASSESSMENT

## BG v0.5

The d10 correction and Ob minimum = 1 are applied consistently within the document. The Standard Ob table (P-21) is the most useful single addition. The Cascade Depth Cap is well-designed and functioning. The Klapp Awakening scenario is the most complete and narratively coherent emergent scenario — all three branches produce distinct, playable game states.

The primary remaining fragility is the degree table definition of Overwhelming (Ob+1 vs 2×Ob divergence from TTRPG parent), the undefined Policy Instrument mechanic, and the Theocracy Counter 80 seizure scope. None of these block core play but all will produce table disputes on first encounter.

## Mass Battle v3

The deterministic Cohesion check system is an excellent simplification from probabilistic variants. The Coherence Rating asymmetry (Coherence Rating=7 vs Coherence Rating=1 "produces near-certain outcome before a die is rolled") is well-justified design. The TTRPG Phase structure is coherent and the patches are internally consistent.

The critical gaps are Coherence (undefined stat blocking §A.10 entirely) and TN 6 for Volley (contradicts the universal TN 7 correction). Both are resolvable with one sentence each.

## Intersection

The hybrid handoff logic is sound in principle. The gap is in the conversion formulas: pool size incompatibility between aggregated BG pools and per-unit TTRPG pools will produce outcomes that feel miscalibrated when transitioning mid-battle. The Altonian invasion unit stats (CLOCK-EDIT-01) are the blocking item for any scenario involving the campaign's primary external threat.

The most elegant intersection design is the tactic card system: faction-specific cards translate doctrinal flavour (Varfell's information advantage, Löwenritter's Iron Discipline) without requiring rule lookups. Once the commander bonus formula is unified, this layer is playtest-ready.

**Estimated fixes before playtest: 7 critical (patches or explicit design decisions), 19 significant (most requiring 1–3 sentences), 5 minor. Estimated revision time for author with design authority: 3–4 focused hours.**
