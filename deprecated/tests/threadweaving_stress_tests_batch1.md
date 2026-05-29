# THREADWEAVING STRESS TESTS — EXTREME CHAIN SCENARIOS
## Date: 2026-03-27
## Source: threadweaving_redesign_v2.1
## Purpose: Break the system. Find every interaction failure, cascade loop, undefined state, and philosophical contradiction.

---

# TEST S-01: THE SOUTHERNMOST CATASTROPHE REPLAY

**Setup:** Late campaign. RS 35 (Fractured world state). A 3-practitioner collective attempts Mending on a Catastrophic Gap in the Southernmost Core Zone. The Anchor (TS 72, Coherence 5/Dissonant, Focus 4) uses dissolution residue. Helper 1 (TS 55, Coherence 7) has a conflicting Belief ("The Southernmost should remain sealed"). Helper 2 (TS 51, Coherence 6) has 2 Wounds. A Löwenritter military escort (Cohesion 6) is present. A Devout Knight Templar officer observes.

**Pre-operation state check:**
- RS 35 = Fractured. Spontaneous Gap risk (1d10 at Accounting, 1–2 = new Gap). All Thread operations +1 Ob worldwide (Critical threshold not yet reached, but Fractured state has territory-specific effects).
- Core Zone special rule: all non-practitioners Spirit check Ob 2 or Certainty −1 per round. Practitioners: contact duration halved.
- Contact duration halved: Anchor's Focus 4 → effective Focus 2 in Core Zone. Only 1 operation round after settling.

**ISSUE FOUND: Contact duration halving + settling round.** Old system: Focus halved meant Focus 4 → 2, giving Leap + Diagnosis + ... nothing (old Focus 2 = re-Leap needed). New system: Focus 4 → 2 after halving. Settling round consumes Round 1. One operation round remains (Round 2). The Anchor gets exactly one shot. Helpers at Focus 2 (halved from 4) = same. Helpers at Focus 3 (halved = 1, round down) = zero operation rounds. **Focus halving at odd numbers needs a rounding rule.** Assume round down: Focus 3 halved = 1 = zero operations. Focus 5 halved = 2 = one operation.

**PATCH NEEDED: Explicit rounding rule for Focus halving. Round down. Focus 1 after halving = zero operations (experience only, as per the settling round rule).**

**Diagnosis round (pre-Leap):**
- Anchor Diagnoses the Catastrophic Gap. GM describes: substrate torn open for 3+ seasons, unintelligible ground showing through, dissolution residue at edges, no trajectory perceivable (Structural-scale trajectory is below the waterline).
- Anchor declares: Mending. Target: Catastrophic Gap.
- Helpers declare alignment with Anchor's intentionality.
- Helper 1's conflicting Belief: "The Southernmost should remain sealed." This directly opposes the Mending intentionality. **Does this prevent Helper 1 from participating, or does it apply the conflicting-Belief penalty (dice cannot chain on 10)?**
- Per §2.5: "Conflicting Beliefs: dissenting participant's dice cannot chain on 10." Helper 1 can participate but their contributed dice are degraded.

**ISSUE FOUND: Can a helper with a directly opposing Belief participate at all?** The current rule says their dice can't chain. But philosophically, their intentionality is directed AGAINST the Anchor's goal. In the beyond-rendering state, their configuration is pulling in the opposite direction. This isn't just "reduced contribution" — it's active interference. **Consider: conflicting Belief that directly opposes the operation's goal should SUBTRACT dice rather than add non-chaining dice. Or: force a pre-Leap Belief check (Spirit TN 7 Ob 1) — failure means the helper cannot align their intentionality and drops out before the Leap.**

**Leap rolls:**
- Anchor pool: Attunement (let's say 4) + History "Einhir Scholar" (5+3=8) + TPS (72÷10=7) = 19 dice. TN 7, Ob 1. Very likely to succeed.
- Wait — Anchor has 2 Wounds? No, Helper 2 has 2 Wounds. Anchor is unwounded. Anchor Ob = 1 (TS 50+).
- Helper 2 pool: Attunement (3) + History (4+3=7) + TPS (51÷10=5) = 15 dice. TN 7, Ob 1 + 2 Wounds = Ob 3. Harder.
- Helper 2 fails the Leap. Rendering snaps back. Composure strain 4. Rattled.

**Helper 2 failure cascade:**
- Helper 2 is now a rendering consciousness in the zone while the other two are in contact. Per §2.5: "If a helper's contact drops before the roll: remove their contributed dice."
- Helper 2's contributed dice: floor(Cognition÷2). Say Cognition 4 → 2 dice removed from Anchor's pool.
- Total pool drops. Is it below half the Anchor's solo pool? Anchor solo = Attunement + Focus + TPS (Mending pool) = let's recalculate. Mending uses Attunement + Focus + TPS. Anchor: Attunement 4 + Focus 4 (but halved to 2 in Core Zone — **ISSUE: does Focus halving affect the Mending pool, or only contact duration?**)

**ISSUE FOUND: Focus halving — does it affect the pool or only duration?** The Core Zone rule says "contact duration halved." Focus determines contact duration (§2.3). If Focus is halved for duration purposes only, the Mending pool still uses full Focus. If Focus is globally halved, the pool is reduced too.

**Resolution:** The Core Zone rule targets contact duration specifically. Focus as an attribute is unchanged — the Thread density interferes with sustaining the suspension, not with the practitioner's capacity. Mending pool uses full Focus. Duration uses halved Focus. **This should be explicitly stated in the Core Zone rules.**

**Continuing with corrected pools:**
- Anchor Mending pool: Attunement (4) + Focus (4, full) + TPS (7) = 15 dice.
- Helper 1 contributes: floor(Cognition÷2) = floor(4÷2) = 2 dice. But conflicting Belief: cannot chain on 10.
- Helper 2 failed Leap: 0 dice.
- Total pool: 15 + 2 (non-chaining) = 17 dice.
- Half of Anchor's solo pool: 15÷2 = 7.5. Pool is 17. Above half. No lattice fracture penalty.

**Dissolution residue declaration:**
- Anchor declared residue use before Leap. +Potency dice (say Potency 3) = +3 dice, explode on 9–10.
- Coherence cost: −1 additional (residue) on top of Mending base cost (−1) = −2 total for this operation minimum.
- Anchor Coherence: 5 → 3 (minimum, before degree-table costs). Enters Fragmented on return. Fragmented Fallout roll required.

**Mending roll:**
- Total pool: 15 + 2 (non-chaining) + 3 (residue, explode 9–10) = 20 dice.
- Mending Ob for Catastrophic Gap: 7. + 1 Ob (Fragmented world state, territory-specific). Total Ob: 8.
- Wait — is the +1 Ob from Fractured world state (RS 35) already in effect? RS 39–20 = Fractured, but the threshold table says "Thread operations +1 Ob in affected territories" at RS 59–40 (Fragile), not at Fractured. At Fractured (39–20): "all factions Stability check" and spontaneous Gaps, but no +1 Ob to Thread operations. The +1 Ob to Thread operations worldwide is at Critical (19–1). **Checking: does Fragile's "+1 Ob in affected territories" apply here?** RS 35 is Fractured. The Fragile penalties persist as the world degrades further (Fractured is worse than Fragile). So yes, the +1 Ob from Fragile persists at Fractured. **This should be stated explicitly: threshold effects are cumulative as RS degrades.**

**PATCH NEEDED: RS threshold effects are cumulative. Fractured includes all Fragile effects plus Fractured-specific effects. Critical includes all of the above.**

- Corrected Ob: 7 (Catastrophic Gap) + 1 (Fragile/Fractured cumulative territory effect) = 8.
- 20 dice at TN 7: expected successes ~6 (30% per die). Ob 8 is a stretch. Likely Partial or Failure.

**Assume Partial result:**
- Gap reduced from Catastrophic to Entrenched. RS unchanged. Coherence: −2 (base −1 + additional −1 from Partial).
- Anchor total Coherence loss this operation: −1 (Mending base) + −1 (residue) + −1 (Partial additional) = −3. Anchor Coherence: 5 → 2. **Fractured.**
- Fractured Fallout roll required. Belief Co-Authorship triggers.
- Anchor enters the scene at Coherence 2 with Belief Co-Authorship active. GM presents shifted perspective. Player must rewrite Beliefs.

**Co-movement fires (three descriptions of one event):**
- Temporal: Coherence −1 (already counted in base). The substrate's damaged temporal state partially absorbed by the Anchor.
- Epistemic: Observers with TS 10+ perceive settling. The Devout Templar officer senses easing. Non-practitioners (Löwenritter escort) may notice reduced tension.
- Actual (d6): Roll. Say 1 — dissolution residue forms at the Mending site. The old Gap's content condensed.

**Devout Templar officer cascade:**
- The officer witnessed a Thread operation. This is a qualifying event for a Discovery Event.
- Officer is Devout (essentialist theological Belief). Devout characters' Discovery Events bypass the constraint for the initial check (involuntary).
- Spirit check TN 7 Ob 1 for TS growth. Say the officer has Spirit 5, rolls 5 dice. ~1.5 successes expected. Likely success.
- Success: +5 TS. Officer now has TS 5 (from 0). Inert range, but growth has begun.
- Immediate Theological Dissonance Event: Spirit TN 7 Ob 1. Say success: framework holds. Devout Constraint re-engages. Certainty −1.
- Officer's Certainty was Spirit (5). Now 4.

**Löwenritter escort cascade:**
- Non-practitioners in Core Zone: Spirit check Ob 2 or Certainty −1 per round of exposure.
- Escort Cohesion 6. Spirit check for individual soldiers is abstracted to Cohesion check for the unit.
- Cohesion check Ob 2 (per Core Zone rules). Roll 6 dice TN 7. ~1.8 successes. Likely fails.
- Failure: Certainty −1 for the unit (abstracted as Cohesion −1). Escort Cohesion: 6 → 5.

**Knot cascades from Anchor's Coherence drop:**
- Anchor dropped from Coherence 5 to 2 in one operation. Crosses from Dissonant through Fragmented to Fractured.
- Fragmented entry: Roll Fragmented Fallout. Say 3 — "Your sense of timing this scene is wrong."
- Fractured entry: Roll Fractured Fallout. Say 4 — "You perform an action you do not remember."
- Knot strain: At Coherence 2 (Fractured), all Knots +1 strain per session. If Anchor has a Close Knot at 2/3 strain (wrongness threshold), this pushes to 3/3. Knot enters Wrongness. The connected entity perceives something wrong about the Anchor.
- If the Close Knot is the military escort commander: the commander now perceives the Anchor as uncanny. This affects the escort's willingness to continue the expedition.

**Rendering Stability check at Accounting:**
- Mending Partial: RS unchanged.
- Gap reduced to Entrenched: still persists. RS −4/season (Gap persistence).
- Dissolution residue formed at site: no RS effect.
- Siege/suffering: not applicable.
- Net RS change this season: −4 (Gap persistence). RS: 35 → 31.
- Still Fractured. Spontaneous Gap risk at Accounting: 1d10, 1–2 = new Gap. Say 3 — no new Gap.

**Test result: System holds but reveals 4 issues.**

---

# TEST S-02: THE RECURSIVE LOCK CASCADE

**Setup:** A TS 80 practitioner (Coherence 6/Dissonant, Focus 5) attempts FR Lock on a Structural-scale configuration — a political institution (the Crown's legitimacy) — in a territory that already contains a 3-season-old Lock (from a prior FR Lock on a fortification gate). RS 45 (Fragile). The practitioner has History "Crown Loyalist" (6 points) and a Close Knot with Queen Almud. TC is at 78 (2 points from Church territorial seizure threshold).

**Pre-operation state:**
- Existing Lock (3 seasons old): +1 TT... wait, +RS drift. The Lock's chronic consequence: RS −2/season (4+ season Lock = −2). So this territory has been losing RS −2/season for 3 seasons. RS impact already absorbed into current RS 45.
- New Lock in same territory: RS −2 immediate + future chronic drift.
- Fragile world state (RS 59–40): Shifting Objects form spontaneously. Thread operations +1 Ob in affected territories.

**Diagnosis (pre-Leap):**
- Practitioner renders the Crown's legitimacy as a Structural-scale configuration. Trajectory: near-opaque at Structural scale. "Something large is shifting but the trajectory is too complex to render." The practitioner cannot see where this is heading.
- Existing Lock in the same territory: Diagnosis +1 Ob (4+ season Lock effect). But Diagnosis has no roll — it's a GM exchange. **ISSUE: Does the +1 Ob from long-standing Locks affect Diagnosis, which has no Ob?** The Lock rule says "Diagnosis on anything within the same zone: +1 Ob." But Diagnosis is a no-roll GM exchange. The +1 Ob has no mechanical target.

**ISSUE FOUND: Lock chronic effects reference Diagnosis Ob, but Diagnosis has no Ob.** The intent is that Diagnosis is impaired — the locked configuration occludes Thread perception. Without an Ob to modify, this needs a different expression. Options: (a) Diagnosis in a Lock-affected zone is incomplete — the GM withholds one piece of information that would normally be revealed. (b) The +1 Ob applies to the OPERATION, not Diagnosis — the occluded perception carries into the operation as degraded intentionality. Option (b) is cleaner mechanically.

**PATCH NEEDED: Lock chronic Diagnosis penalty reframed as +1 Ob to the subsequent operation (degraded intentionality from impaired Diagnosis), not to Diagnosis itself.**

**Leap roll:**
- Pool: Attunement (5) + History "Crown Loyalist" (6+3=9) + TPS (8) = 22 dice. TN 7, Ob 1. Trivial.
- Success. Contact established. Focus 5 = 4 operation rounds after settling.

**FR Lock roll:**
- Pool: Spirit (5) + History bonus (9). No TPS for FR (per current rules — FR uses Spirit + History only). = 14 dice.
- Wait — checking v2.1. FR Lock says "Pool: Spirit + relevant History bonus." No TPS. Correct.
- Ob: Structural = 8+ (say 8). + 1 (Fragile territory effect). + 1 (existing Lock chronic effect, reframed as operation Ob). Total Ob: 10.
- **Ob 10 is the maximum.** Ob cap rule from §1.3. So Ob stays at 10.
- 14 dice at TN 7 Ob 10. Expected successes: ~4.2. Essentially impossible.
- **Even the most powerful practitioner in the game cannot Lock a Structural configuration in a degraded, Lock-affected territory.** Is this intended?

**Analysis:** Ob 10 at 14 dice is a ~0.01% success rate. The system is saying: you cannot Lock a political institution's legitimacy while standing in a territory that's already been configurally damaged by a prior Lock. The existing Lock has made the substrate too rigid. Your intentionality cannot reach deep enough through the occluded configuration.

This is philosophically correct. The prior Lock has stiffened the substrate. You're trying to freeze something in a territory where the configurational traffic is already blocked. The substrate cannot absorb another Lock. The operation should fail.

But what if the practitioner attempts anyway?

**Assume Failure (overwhelmingly likely):**
- Collapse onto practitioner. 2 Wounds (no armour). RS −4. Coherence: −1 (Territorial scale) + −1 (FR additional) + −2 (Failure degree) = −4. Coherence: 6 → 2. **Fractured.**
- Adjacent configurations become partially rigid: +1 Ob to all Thread operations adjacent to failure site, remainder of season.
- Stiffening effect STACKS with existing Lock's chronic +1 Ob. Territory now has +2 Ob to all Thread operations.

**RS cascade:**
- RS: 45 → 41 (from −4). Still Fragile, but barely.
- Existing Lock chronic drift: −2/season. New failed Lock stiffening: temporary (season-end). At Accounting: RS 41 − 2 (old Lock drift) = RS 39. **Crosses into Fractured (39–20).**
- Fractured entry effects: Gaps may open spontaneously (1d10, 1–2). Monstrous Incursion risk in all territories with existing Gaps. Non-practitioners experience rendering failures.

**TC cascade:**
- The FR Lock attempt on the Crown's legitimacy — even failed — was a visible Thread operation at Structural scale. An operation this large is detectable by TS 30+ practitioners across the district (per Visibility table). The Church has practitioners (even if unacknowledged).
- **ISSUE: Does a failed FR Lock that produces no Lock still produce the Structural-scale visibility signature?** Yes — the practitioner attempted a Structural operation. The attempt is visible regardless of outcome. The interaction with the configurational substrate occurred; it just didn't produce the intended result.
- If Church intelligence detects this: TC +1 or +2 (GM discretion for Structural-scale heterodox activity).
- TC was 78. +2 = 80. **Church territorial seizure threshold crossed.**
- Per Church territorial seizure rules: per-territory roll at TC 80. The Church begins seizing territories.

**Knot cascade:**
- Practitioner has Close Knot with Queen Almud. Coherence dropped to 2 (Fractured). +1 strain per session to all Knots.
- If the practitioner's Knot with Almud is at crisis threshold: Almud confronts the practitioner. The Crown's chief Thread operator is now Fractured, socially impaired (−2D), and the Church is seizing territories.
- The practitioner's Belief Co-Authorship triggers: GM presents the shifted perspective. The practitioner at Coherence 2 may no longer perceive the Crown's legitimacy as worth preserving — the categories that made "legitimacy" meaningful are dissolving.

**Co-movement:**
- Temporal: Coherence −1 (counted). History "Crown Loyalist" resonates — the practitioner has a History relevant to the operation's context. Next use of Crown Loyalist: 1 bonus die. If the bonus die shows 1: Coherence −1 (to 1 = Severed).
- Epistemic: FR Lock failure — the target configuration did NOT Lock. But the attempt destabilised perception around it. Investigation rolls involving the Crown's legitimacy: +1 Ob until seasonal accounting.
- Actual (d6): Roll. Say 4 — "Target's physical configuration overshoots intended scope." The Crown's legitimacy was not Locked but the failed attempt has distorted it. The configuration is now in a state it wasn't in before — neither Locked nor natural. **Is this a Shifting Object?** At RS 41 (just entered Fractured): Shifting Objects form at RS 59–40 (Fragile, cumulative). A distorted Structural configuration that's been subjected to a failed Lock... this should produce a Shifting Object at the Structural scale. The Crown's legitimacy itself becomes a Shifting Object — oscillating between presence and absence. What does that look like narratively? The Crown's authority flickers. Some territories respond to Crown edicts. Others don't. The legitimacy is no longer stable.

**ISSUE FOUND: Shifting Objects at Structural scale.** Current rules describe Shifting Objects as Object-scale phenomena (oscillating objects). A Structural-scale Shifting Object — a political institution's legitimacy oscillating — is not covered. The mechanic needs to scale or the Shifting Object rules need explicit scale limitations.

**PATCH NEEDED: Shifting Objects scale. Object-scale: physical objects oscillate. Personal-scale: a person's rendering flickers (others perceive inconsistency). Relational-scale: an agreement or bond becomes unreliable. Territorial-scale: a region's configurational state fluctuates. Structural-scale: an institution or law oscillates between presence and absence — its authority is intermittent and unreliable.**

**Test result: System holds but reveals 3 issues. The cascade from failed FR Lock → RS threshold crossing → TC threshold crossing → Church territorial seizure is a legitimate emergent narrative event that the mechanics generate correctly. The Lock-on-Lock stacking produces the correct impossibility result.**

---

# TEST S-03: THREADCUT BEING ENCOUNTER DURING COLLECTIVE MENDING

**Setup:** Mid-campaign. RS 50 (Fragile). A 2-practitioner team attempts Mending on an Entrenched Gap in Eisengrund (Varfell territory). During Round 2 of contact (the Anchor's operation round), a Mode 3 threadcut being emerges through the Gap.

**The problem:** The practitioners are in contact — rendering suspended. They cannot perceive the threadcut being through rendering because rendering is suspended. Their configurations are interacting with the substrate in originary intentionality. The threadcut being is also operating beyond rendering (it exists through continuous Thread work, which is permanent Leap-state per §6.1). 

**ISSUE FOUND: Configuration interaction during contact.** Two configurations (the practitioners') are interacting with the substrate to Mend. A third configuration (the threadcut being's) is present and actively self-rendering through Thread work. What happens when configurations interact in the beyond-rendering state?

Options:
(a) The practitioners' configurations are directed by specific intentionality (Mending). The threadcut being's configuration is directed by different intentionality (self-maintenance + whatever brings it here). The interactions are independent — they don't interfere unless they target the same thread/substrate.
(b) The threadcut being's continuous Thread work at the Gap site directly interferes with the Mending — its self-rendering draws on the same substrate the practitioners are trying to repair. +Ob to the Mending operation.
(c) The practitioners' configurations perceive the threadcut being in originary terms — not as a visual/spatial entity but as a configurational presence. Their intentionality must accommodate its presence. The Mending continues but is complicated.

**Resolution:** Option (b) is the most mechanically clean and philosophically coherent. The threadcut being sustains itself through continuous Thread work. At a Gap site, it is drawing on the substrate — the same substrate the practitioners are Mending. This is direct configurational competition. The Mending Ob increases by the threadcut being's self-rendering intensity (proxy: its TS ÷ 20, round up). A TS 80 threadcut being adds +4 Ob. The practitioners cannot know this during contact — they experience it as increased resistance, not as a being.

**When contact drops (Focus expires):**
- The practitioners' rendering reasserts. They now perceive the threadcut being through their TS.
- Anchor (TS 72): perceives the being stably. Sees the continuous Thread work. Perceives it as something that holds itself up.
- Helper (TS 55): stable perception. Sees the being as fully rendered.
- The being is there. The Mending may or may not have succeeded (probably partial or failed given the +Ob).

**Observer-dependent rendering in action:**
- Varfell agents in the territory (TS 0–9): perceive nothing. Or vague unease.
- If the being renders itself beyond observer ceiling: Rendering Strain +1 per scene.

**Assume the Mending failed. Gap remains. Threadcut being present.**

**Now what? The practitioners must decide:**
1. Re-Leap and attempt Mending again (with the threadcut being still drawing on the substrate).
2. Attempt to communicate with the being (threadcut beings may have comprehensible goals — Mode 3 rule).
3. Attempt FR Dissolution on the being (destroys being but creates second Gap on failure).
4. Attempt Weaving to dissolve the being's configuration (TS 60+, Ob 4 — but this is Weaving, not Dissolution).
5. Retreat.

**If they attempt Weaving to dissolve the being (option 4):**
- This is resolving a monstrous entity via Weaving. Current rule: "Weaving (TS 60+, Ob 4): destroys entity AND partially closes Gap (RS +2)."
- But the being is Mode 3 (threadcut). Mode 3 beings have special rules: "Wounds cost additional sustained Thread work rather than conventional incapacitation."
- **ISSUE: Can you Weave a threadcut being to "destroy" it?** Weaving draws threads toward coherence. A threadcut being sustains itself through Thread work. Weaving it toward coherence would... reinforce its self-rendering? Make it MORE stable? That's the opposite of destroying it.

**ISSUE FOUND: Weaving-based monstrous entity resolution doesn't work on Mode 3 beings.** The current rule ("Weaving destroys entity AND partially closes Gap") was written for Mode 1/2 entities — configurations from the unintelligible ground that the rendered world cannot integrate. Weaving them toward coherence resolves their configuration into something the world can absorb. But a Mode 3 being is already coherent — it's self-coherent through continuous Thread work. Weaving it reinforces it. You cannot Weave a threadcut being to death.

**Resolution options for Mode 3:**
- **Pulling:** Drawing the being toward potential, loosening its self-rendering. But Pulling effects are temporary — the being's continuous Thread work would resist. Ob = being's TS ÷ 10 (round up), as with Locked objects (the being's self-rendering functions like a continuous Lock).
- **Dissolution:** Tearing the being's intelligible face away. This destroys the being but opens a second Gap (on Partial/Failure). Extreme risk.
- **Mending the Gap while the being is present:** If the Gap closes, the being loses its emergence point. But it's already emerged — closing the Gap doesn't un-emerge it. The being persists as long as its Thread work continues.
- **Outlasting:** The being's Rendering Strain accumulates. If it's rendering beyond observer capacity, it will eventually De-actualise. But if it's not pushing beyond capacity, it can persist indefinitely.
- **Communication:** The being may have goals. It may not be hostile. Mode 3 beings are not by nature antagonistic (P-04: monstrosity ≠ moral).

**PATCH NEEDED: Weaving-based monstrous entity resolution explicitly excludes Mode 3 (threadcut) beings. Mode 3 resolution requires: Dissolution (risky), Pulling to weaken self-rendering then conventional damage, or communication/negotiation. Add to §5.13 under Monstrous Entities.**

---

# TEST S-04: THE FIVE-WAY SIMULTANEOUS MESS

**Setup:** Hybrid mode. Cascade Phase. RS 42 (Fragile). TC 79. IP 58.

**Events this season (all resolve at Cascade Phase):**
1. **Personal Phase:** PC practitioner (Coherence 4/Fragmented, TS 65) performed Relational Weaving to bind a diplomatic agreement between Crown and Hafenmark. Success. Over-actualisation: +1 Ob to subsequent ops on this configuration.
2. **Personal Phase:** Same practitioner then performed Object-scale Pulling to unlock a cell (rescuing Torben). Success. No Coherence cost (Object scale).
3. **Strategic Phase:** Revolution player used Community Weaving order. Success: RS +1.
4. **Strategic Phase:** Church player used Excommunicate order against the Crown PC. Single roll: Church Mandate (6) vs target. Succeeded.
5. **Strategic Phase:** Varfell player used Private Collection (Thread Harvest equivalent). Success: +1 Wealth. RS −0.5 (tracked as half-point).
6. **Event Card drawn:** "Heretic Scholar" — a practitioner surfaces publicly. TC +2. Revolution Influence +1.

**Cascade Phase resolution (sequential):**

**Step 1: Apply Personal Phase Thread consequences.**
- Relational Weaving success: RS unchanged. Coherence: −1 (Relational scale). Practitioner Coherence: 4 → 3. Still Fragmented.
- Co-movement from Weaving (Version C):
  - Temporal: Coherence −1 (already counted). History Resonance check: practitioner has History "Diplomatic Courier." Relevant to binding a diplomatic agreement. History resonates. Bonus die stored for next use.
  - Epistemic: Target becomes more intelligible. Observers perceive the agreement as clearer.
  - Actual (d6): Roll. Say 5 — environmental texture shift. The negotiation chamber feels warmer.
- Over-actualisation: +1 Ob to subsequent Thread ops targeting Crown-Hafenmark agreement.
- Object Pulling (Torben's cell): RS unchanged. Coherence: 0 (Object scale). Co-movement fires but minor.
  - d6: Roll. Say 2 — nearby object enters partial potentiality. The cell door's hinges become slightly unstable. Self-corrects in 1d3 days.

**Step 2: Apply Strategic Phase consequences.**
- Community Weaving success: RS +1. RS: 42 → 43.
- Co-Movement Card drawn (Revolution). Say card 5: "Acting faction: Influence +1." Revolution Influence +1 (on top of the Event Card's +1). Revolution Influence total: +2 this season.
- Excommunication succeeded. Crown PC is excommunicated. Per social system: Mandate consequences, faction interaction effects.
- TC impact of excommunication: per existing rules, successful excommunication = TC +1 (Church authority demonstrated).
- TC: 79 + 1 = 80. **Church territorial seizure threshold crossed.**
- Thread Harvest (Varfell): RS −0.5. RS: 43 → 42.5 (tracked as half-point, rounds up at Accounting).
- Co-Movement Card drawn (Varfell). Say card 10: "Church TC +1." TC: 80 → 81. Already past threshold.

**Step 3: Apply Event Card.**
- "Heretic Scholar" — TC +2. TC: 81 → 83. Revolution Influence +1 (already counted).

**Step 4: Accounting.**
- RS: 42.5 → rounds to 42 at Accounting (half-points round against the acting faction).
- Wait — Thread Harvest says "TT +0.5 (tracked as half-points, round up at accounting)." Inverted for RS: RS −0.5, round down at accounting. RS: 43 − 0.5 = 42.5 → round down → 42. Hmm, "round up" in TT terms = "round down" in RS terms (both are against the acting faction). RS: 42.
- RS 42 = Fragile. Spontaneous Shifting Object: one random per season. GM places it.
- TC 83: Church territorial seizure active. Per-territory rolls begin.
- IP 58: Altonian army visible. Diplomatic Resolution possible.

**Step 5: Check practitioner Coherence at session end.**
- Practitioner at Coherence 3 (Fragmented). −1D to social rolls. −1D to Memory rolls. +1 Ob on all Thread operations.
- Practitioner was just excommunicated. The excommunication + Coherence 3 social penalties stack: −1D from Fragmented + whatever social consequences excommunication imposes.
- Practitioner's History Resonance (Diplomatic Courier) is loaded. Next use: bonus die. If it shows 1: Coherence −1 → Coherence 2 (Fractured). Belief Co-Authorship triggers.

**ISSUE FOUND: Excommunication + Coherence penalties stacking.** No explicit interaction rule. Excommunication imposes social/political consequences (loss of Church protection, Mandate effects). Fragmented imposes mechanical social penalties (−1D). These should stack independently — they're from different sources. But the combined effect may be too severe. A practitioner at Coherence 3 who is excommunicated is mechanically crippled in social scenes: −1D from Coherence + any excommunication modifiers + over-actualisation +1 Ob if they try to use Thread work to address it. **This is correct and intended — the system punishes a practitioner who is both degraded and politically exposed. It's the consequence spiral that the game's dramatic engine runs on.**

**Step 6: Check faction consequences.**
- TC 83: Church begins territorial seizure. This is a MAJOR campaign event occurring as a cascade consequence of Strategic Phase actions.
- The practitioner's Relational Weaving to bind Crown-Hafenmark agreement is now under threat: if the Church seizes territories, the agreement's configurational basis is destabilised. The over-actualised agreement (+1 Ob to subsequent ops) is rigid — it cannot adapt to the Church's territorial seizure. This rigidity may cause it to shatter rather than bend, producing a Shifting Object at the Relational scale (the agreement oscillating between binding and void).

**ISSUE FOUND: Over-actualised configurations under external stress.** The over-actualisation hazard says "+1 Ob to subsequent Thread operations targeting this configuration." But what happens when a non-Thread event (Church territorial seizure, which is a political action, not a Thread operation) stresses an over-actualised configuration? The rules don't address this. Options:
(a) Non-Thread events cannot interact with over-actualised configurations mechanically — the rigidity only affects Thread operations.
(b) Over-actualised configurations are brittle under all stress: if a non-Thread event would naturally strain the configuration (e.g., territorial seizure threatening an inter-faction agreement), the configuration has a chance of shattering. Roll a Stability-equivalent check (GM sets Ob based on severity of the external stress). Failure: the configuration becomes a Shifting Object at its scale.

**Resolution:** Option (a) is simpler but philosophically incomplete. The Foundations say the three dimensions co-move — a political event (actuality) affects Thread-level configurations (all dimensions). Option (b) is correct: over-actualised configurations are brittle because they've been driven beyond what the substrate naturally supports. External stress that would naturally strain the configuration can shatter it. **But this is GM judgment, not a mechanical check.** The GM determines whether a political event is severe enough to threaten an over-actualised configuration. If yes: the GM narrates the configuration becoming a Shifting Object. No roll — this is a rendering consequence, handled by the rendering engine (the GM).

**FINDING: Over-actualised configuration brittleness under external stress should be documented as a GM guidance note, not a mechanical check. The GM determines when political/social/military events threaten over-actualised Thread configurations.**

---

# TEST S-05: THE DEATH SPIRAL ESCAPE

**Setup:** PC practitioner at Coherence 1 (Severed). TS 85. Focus 5. Has a Close Knot with a non-practitioner spouse at 5/6 strain (one point from Crisis). The practitioner wants to perform an Anchoring Scene to recover Coherence — but the Anchoring Scene itself risks pushing the Knot to Crisis.

**The dilemma:**
- Anchoring Scene: Bonds check TN 7, Ob 2. Success: +1 Coherence (1 → 2). Costs Knot +1 strain.
- Knot at 5/6 strain. +1 strain = 6/6 = Crisis. The Knot enters Crisis regardless of Anchoring success.
- Crisis Knot: cannot be Called or used as Composure buffer. The connected entity takes action — confrontation, departure, or betrayal.

**So the practitioner can recover +1 Coherence but loses the Knot to Crisis.** At Coherence 2 they're still Fractured (Belief Co-Authorship, dissociative episodes, −2D social). And their closest relationship has just shattered.

**Can they recover without the Knot?**
- Full season of non-practice: +1 Coherence. Coherence 1 → 2. Still Fractured.
- Another season: 2 → 3. Still Fragmented.
- Another: 3 → 4. Still Fragmented.
- Another: 4 → 5. Enters Dissonant. Functional again.
- **Four seasons of non-practice to become functional.** A season is ~2–3 sessions. That's 8–12 sessions of the practitioner doing no Thread work. Essentially sitting out the Thread dimension of the game for a quarter to a third of the campaign.

**ISSUE: Is this too harsh, or is this the intended dramatic cost?**

**Analysis:** The system is saying: if you practice Thread operations aggressively enough to reach Coherence 1, the recovery cost is enormous. Four seasons of non-practice. Your closest relationship shatters if you try to recover through it. This IS the Einhir arc at personal scale — the cost of ambition. The system produces a genuine dramatic crisis: the practitioner must choose between continuing to operate (risking Rendering Crisis and NPC status) or withdrawing for a significant portion of the campaign.

**But is it escapable at all?** If the practitioner continues operating at Coherence 1 (Severed), every Relational+ operation costs −1 Coherence. One more operation → Coherence 0 → Rendering Crisis → NPC. They cannot operate. They cannot recover quickly. They are trapped.

**Escape routes:**
1. Einhir techniques (GM discretion): +1–2 Coherence. Requires access to Einhir knowledge (late campaign, Southernmost expedition).
2. Another practitioner's corrective Weaving (Ob 3): +1 per season. But below Coherence 3, requires the degraded practitioner's active cooperation, which is unlikely at Coherence 1.
3. Use a different Knot for Anchoring (if one exists that isn't near Crisis). Costs that Knot +1 strain but doesn't shatter.
4. Establish a new Knot (2 CP) and immediately use it for Anchoring. Fresh Knot at 0/3 strain (Close). Anchoring costs +1 strain → 1/3. Not at Crisis. +1 Coherence. Repeat next season with same Knot (1/3 → 2/3, still below Crisis). This works but costs CP and narrative investment.

**Route 4 is the escape.** A practitioner at Coherence 1 can establish a new Close Knot (2 CP, narrative investment) and use it for Anchoring each season. Recovery rate: +1 Coherence per season (with Anchoring) or +2 per season (Anchoring + non-practice). The Knot accumulates 1 strain per Anchoring. It hits Wrongness (3/3) after 3 seasons and Crisis (6) after 6 — enough time to recover from Coherence 1 to Coherence 5 or 6 before the Knot shatters.

**But at Coherence 1 (Severed): −2D to social rolls.** Establishing a new Knot requires genuine relationship building. At −2D social, this is mechanically difficult. The system makes recovery possible but hard in proportion to how deep the degradation goes.

**Finding: The death spiral is escapable but narrow. Route 4 (new Knot) works if the player invests CP and narrative effort. Route 1 (Einhir techniques) works as a late-campaign escape hatch. The recovery arc IS the dramatic content — a practitioner clawing back from the edge of rendering collapse through new relationships and deliberate withdrawal. This is correct.**

---

# TEST S-06: SIMULTANEOUS THREADCUT AND MENDING AT RENDERING CRISIS

**Setup:** RS 22 (Fractured, approaching Critical). A threadcut being has been present for 3 seasons in a territory with an Entrenched Gap. The being is at Rendering Strain 4 / Health 10. A practitioner (TS 75, Coherence 6, Focus 4) attempts Mending on the Gap while the threadcut being is present and actively self-rendering.

**Complications layered:**
- RS 22: Fragile + Fractured cumulative effects. All Thread operations in affected territories +1 Ob. Gaps may open spontaneously. Monstrous Incursion risk in territories with existing Gaps.
- Threadcut being present at Gap: per S-03 finding, its self-rendering adds Ob = TS ÷ 20 (round up). Say the being's TS equivalent is 60: +3 Ob.
- Practitioner is not in Core Zone so no Focus halving.
- The practitioner also has the Fraying Bane (performed 3+ FR Dissolutions this season): +1 Ob to all Thread operations. Contact duration −1 round (Focus 4 → effective 3 for duration).

**Mending roll setup:**
- Base Ob for Entrenched Gap: 6.
- +1 (Fragile/Fractured territory effect): 7.
- +3 (threadcut being self-rendering): 10.
- +1 (Fraying Bane): would be 11, but **Ob cap is 10.**
- Final Ob: 10.
- Pool: Attunement (4) + Focus (4) + TPS (7) = 15 dice. TN 7.
- At Ob 10: Overwhelming unavailable. Partial requires net ≥ 5.
- Expected successes at 15 dice TN 7: ~4.5. Partial is the best realistic outcome (net 5+ is possible but unlikely).

**Assume Failure (net < 5 at Ob 10 = Failure):**
- Mending fails. Gap unchanged. 1 Wound (no armour). Coherence: −1 (Mending base) + −1 (Failure additional) = −2. Coherence: 6 → 4. Enters Fragmented. RS −2. RS: 22 → 20.
- **RS 20: the last point before Critical (19–1).** One more RS loss and everything gets worse.
- Fraying Bane: Partial results on any Thread op produce involuntary micro-Gaps. But this was a Failure, not Partial. No micro-Gap from Fraying.

**Threadcut being response:**
- The Mending attempt disturbed the substrate without repairing it. The threadcut being felt this as interference with its self-rendering substrate.
- Does the being react? Per §6.3: Mode 3 beings "may have comprehensible goals." The being may perceive the Mending attempt as helpful (repairing the Gap benefits the substrate it relies on) or as threatening (the disturbance without repair destabilised its footing).
- GM determines: the being's response is based on its configuration's intentionality, which is unknowable to the practitioner.

**Monstrous Incursion risk:**
- RS 22 (Fractured): start of each scene near a Gap, roll 1d10. On 1–2: Mode 1 incursion.
- Say 2: Mode 1 incursion manifests through the Entrenched Gap.
- Mode 1 entity: Health 6, Martial 3, Cohesion 1. Certainty −1 to all in scene. −1 Health per round (rendering refuses to sustain). Dissolves in 1d6 rounds.
- The practitioner is now facing a Mode 1 incursion, a Mode 3 threadcut being, an Entrenched Gap, Coherence 4 (Fragmented), the Fraying Bane, and 1 Wound.
- Practitioner's options: retreat (safe), attempt Weaving to dissolve Mode 1 entity (TS 60+, Ob 4 + 1 Fragile + 1 Fraying = Ob 6), or wait for Mode 1 to self-dissolve (1d6 rounds).
- Mode 3 being: may or may not intervene against the Mode 1 entity.

**Co-movement from failed Mending:**
- Temporal: Coherence −1 (counted).
- Epistemic: per Mending profile, observers perceive settling. But this was a Failure — the epistemic effect should be different. **ISSUE: Mending co-movement profile doesn't differentiate by degree.** The profile says "observers perceive settling." On Failure, there was no settling — there was disturbance. The epistemic effect should be inverted on Failure: observers perceive increased tension rather than settling.

**PATCH NEEDED: Mending epistemic co-movement differentiates by degree. Success/Overwhelming: settling. Partial: slight settling, slight tension. Failure: increased tension (observers sense things getting worse, not better).**

**Test result: System holds under extreme pressure. The Ob cap at 10 prevents impossible numbers. The threadcut being's interference makes Mending nearly impossible at high RS degradation — which is correct (the world is too damaged, and the being's presence complicates everything). The system produces a legitimate "no good options" scenario that drives narrative.**

---

# FINDINGS SUMMARY

## Issues Found

| # | Issue | Severity | Source Test |
|---|---|---|---|
| 1 | Focus halving rounding rule unspecified | MODERATE | S-01 |
| 2 | Conflicting Belief that directly opposes operation goal — should it subtract dice or block participation? | SIGNIFICANT | S-01 |
| 3 | Lock chronic Diagnosis penalty targets a no-roll action | MODERATE | S-02 |
| 4 | RS threshold effects not explicitly cumulative | MODERATE | S-01, S-02 |
| 5 | Shifting Objects at non-Object scales undefined | SIGNIFICANT | S-02 |
| 6 | Weaving-based monstrous entity resolution doesn't work on Mode 3 | SIGNIFICANT | S-03 |
| 7 | Threadcut being interference with Mending — Ob modifier unspecified | MODERATE | S-03, S-06 |
| 8 | Over-actualised configuration brittleness under non-Thread stress | LOW (GM guidance) | S-04 |
| 9 | Mending epistemic co-movement doesn't differentiate by degree | LOW | S-06 |
| 10 | Contact duration halving vs. pool attribute distinction needed | LOW | S-01 |

## Proposed Patches

| # | Patch | Targets Issue |
|---|---|---|
| P-11 | Focus halving: round down. Focus 1 after halving = zero operations. | 1 |
| P-12 | Directly opposing Belief: helper must pass pre-Leap Belief check (Spirit TN 7 Ob 1). Failure: cannot align intentionality, drops out before Leap. Success: participates with non-chaining dice. | 2 |
| P-13 | Lock chronic Diagnosis penalty reframed: +1 Ob to the operation following Diagnosis in a Lock-affected zone (degraded intentionality from occluded perception). | 3 |
| P-14 | RS threshold effects are cumulative. Each lower band includes all effects from higher bands. State this explicitly. | 4 |
| P-15 | Shifting Objects scale: Object (physical oscillation), Personal (rendering flicker), Relational (bond unreliability), Territorial (regional fluctuation), Structural (institutional intermittence). | 5 |
| P-16 | Weaving-based entity resolution explicitly excludes Mode 3. Mode 3 resolution requires: Dissolution, Pulling to weaken then damage, communication, or outlasting De-actualisation. | 6 |
| P-17 | Threadcut being at Gap site: +Ob = being's TS ÷ 20 (round up) to Mending operations targeting that Gap. Self-rendering draws on the same substrate. | 7 |
| P-18 | Over-actualised configuration brittleness: GM guidance note. Non-Thread events of sufficient severity can shatter rigid configurations into Shifting Objects (GM judgment, not mechanical check). | 8 |
| P-19 | Mending epistemic co-movement by degree: Overwhelming/Success = settling. Partial = ambiguous (slight settling, slight tension). Failure = increased tension. | 9 |
| P-20 | Core Zone / environment Focus reduction: affects contact duration only, not pool calculation. State explicitly. | 10 |
