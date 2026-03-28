# THREADWEAVING STRESS TESTS — BATCH 3
## Date: 2026-03-27
## Source: threadweaving_redesign_v2.3
## Purpose: Final edge cases — Catastrophe replay, Locked Zone Mending, Rendering Crisis forced contact, Knot recovery loops, the Rupture, involuntary Leap.

---

# TEST S-13: THE CATASTROPHE REPLAY

**Setup:** 4 practitioners in collective formation attempt Structural-scale Weaving to stabilise the Southernmost's foundational thread-configuration. This is the Einhir's final working, replayed at smaller scale. Anchor: TS 82, Coherence 5, Focus 5. Three helpers: TS 55-65, Coherence 6-7, Focus 3-4. RS 48 (Fragile). The working targets a Foundational configuration (Ob 5 base). The Southernmost Core Zone halves contact duration.

**Pre-operation checks:**
- Core Zone: Focus halved (round down per P-11). Anchor Focus 5 → 2. Two contact rounds: settling + one operation. Helpers: Focus 4 → 2 (one operation), Focus 3 → 1 (zero operations — **helper drops out before contributing**).
- **ISSUE FOUND: Core Zone Focus halving eliminates low-Focus helpers from collective operations.** A helper with Focus 3 in the Core Zone has effective Focus 1 = zero operation rounds. They Leap, settle, and their rendering reasserts before the operation fires. Their dice never contribute.
- **Is this intended?** Yes. The Core Zone is described as having Thread density that "interferes" with contact. Low-Focus practitioners literally cannot sustain suspension long enough to participate. The Einhir needed high-Focus practitioners for their Southernmost work. This is a legitimate gate.

**Revised collective:** Anchor + 2 helpers (the Focus 3 helper cannot participate). Anchor pool: Spirit (5) + History (8) = 13 dice (FR/Weaving at Structural uses Spirit + History, not Attunement + Focus). Helper contributions: floor(Cog÷2) each. Say Cognition 4 and 5: +2 and +2 = +4 dice. Total: 17 dice.

**Ob calculation:**
- Structural scale: Ob 5.
- +1 Ob (Fragile territory effect): Ob 6.
- Over-actualisation from prior Weaving in the Southernmost (accumulated over the expedition's prior seasons): +1 Ob. Total: Ob 7.
- The Einhir Catastrophe occurred when practitioners at this site pushed at maximum actualization pressure. At Ob 7, 17 dice TN 7: expected ~5.1 successes. Partial is most likely.

**Assume Failure (the Catastrophe replay):**
- Weaving collapses. RS −2. RS: 48 → 46.
- At RS ≤ 40 (approaching): Shifting Object forms. But RS is 46, still Fragile. No spontaneous Shifting Object from this alone.
- Over-actualisation from PRIOR successful Weavings: the accumulated rigid configurations in the Southernmost have been straining the substrate. A failed Structural Weaving in this environment — **does the existing over-actualisation worsen the failure?**

**ISSUE: Over-actualisation hazard stacking across sessions.** The over-actualisation rule says "+1 Ob to subsequent Thread operations targeting this same configuration." If the Southernmost expedition has been Weaving successfully for 3 seasons, the accumulated +1 Ob per season stacks to +3 Ob on the 4th attempt (same configuration targeted each time). At Ob 5 + 1 (Fragile) + 3 (accumulated over-actualisation) = Ob 9. Almost impossible.

**This IS the Einhir Catastrophe mechanism.** Each season of successful Weaving stiffened the configuration. The Ob climbed. Eventually the practitioners were attempting Ob 9-10 operations. When they failed — and at those Obs, failure was inevitable — the Structural-scale failure produced catastrophic RS loss and the over-actualised configurations shattered.

**But:** The over-actualisation rule says "Clears after one season or when the configuration is Pulled." Does this mean each season's over-actualisation clears independently? If Season 1's Weaving produces +1 Ob that clears at the end of Season 1, then Season 2's Weaving starts fresh at +0. The stacking only accumulates within a single season.

**Resolution:** Over-actualisation clears at seasonal accounting ("after one season"). Multi-season Weaving does NOT produce permanent Ob stacking. Each season starts fresh. The accumulation that destroyed the Einhir was not from over-actualisation stacking — it was from the configurations themselves becoming increasingly complex and deeply actualised over generations. The Ob rose because the configurations were genuinely harder to work (more firmly actualised from centuries of maintenance), not because over-actualisation penalties stacked.

**FINDING: Over-actualisation does not stack across seasons. It clears at seasonal accounting. The Einhir Catastrophe is modelled by the configurations' actualization level rising naturally over time (from "Normally actualised" to "Firmly actualised" to "Previously Woven" to "Foundational"), not by penalty stacking. No patch needed — but document the distinction in GM guidance.**

**What DOES happen on Structural Weaving failure in the Southernmost:**
- RS −2 (Failure degree). But Structural scale failure should be worse than −2. Checking: Weaving degree table says "Failure: RS −2." This is the same regardless of scale. **ISSUE: Should Structural-scale failure produce worse RS consequences than Object-scale failure?**

**ISSUE FOUND: RS consequences don't scale with operation scale.** Weaving Failure is RS −2 whether you failed at Object or Structural scale. Philosophically, failing a Structural operation — where the below-the-waterline portion is enormous — should produce far worse consequences than failing an Object operation. The unintelligible portion that responded to the failed interaction is proportionally larger.

**PATCH NEEDED: RS consequences scale with operation scale on Failure and Partial.**

| Scale | Partial RS Cost | Failure RS Cost |
|---|---|---|
| Object | −1 | −1 |
| Personal | −1 | −1 |
| Relational | −1 | −2 |
| Territorial | −2 | −4 |
| Structural | −3 | −6 |

This makes Structural-scale failure devastating (RS −6) while Object-scale failure is minor (RS −1). The Einhir Catastrophe at Foundational scale with multiple practitioners would produce RS −6 or worse per practitioner involved. With 4 practitioners failing simultaneously in a collective: RS −6 (collective counts as one operation) or RS −6 per participant? Collective operations count as one operation for co-movement purposes, so RS −6 once, but "co-movement scales with participant count" (§2.5). Four participants: RS −6 × scaling factor. Say ×1.5 for 4 practitioners: RS −9. From RS 48 → 39. **Crosses into Fractured.**

With the historical Einhir working involving dozens of practitioners at truly Foundational scale: RS loss would be catastrophic. This correctly models the Catastrophe.

---

# TEST S-14: MENDING A LOCKED ZONE BORDER

**Setup:** Late campaign. A practitioner (TS 78, Coherence 5, Focus 5) attempts to Mend the border of a Locked Zone — the edge of the Southernmost's permanent configurational damage from the Catastrophe.

**Ob:** Locked Zone border = 8+ (per Mending Ob table). Requires Einhir ritual framework.

**ISSUE: What is "Einhir ritual framework" mechanically?** This requirement appears in the Mending table but is never defined. What does it mean to have access to an Einhir ritual framework? What does the framework provide?

**Resolution:** The Einhir ritual framework is a prerequisite, not a modifier. It means the practitioner must have:
1. Knowledge of Einhir Mending techniques (acquired through Einhir Texts or Southernmost expedition Diagnosis).
2. At least one Einhir Text technique specifically applicable to Mending (e.g., "Settling" — +1D to Mending Shifting Objects).
3. Physical presence at an Einhir site-network node (the Southernmost has these; they are the infrastructure the Einhir used for their coordinated work).

Without all three: the Mending cannot be attempted. The Ob 8+ is impossible to achieve through raw dice alone — the ritual framework provides the structure that makes the intentionality coherent enough to interact with a Locked Zone border.

**PATCH NEEDED: Define "Einhir ritual framework" as a prerequisite set. Knowledge + technique + site-network node. Without all three, Locked Zone Mending is impossible (not just hard — impossible).**

**With the framework in place:**
- Pool: Attunement (4) + Focus (5) + TPS (7) = 16 dice.
- Einhir technique bonus: +1D (Settling or equivalent). Total: 17 dice.
- Ob 8. +1 Ob (Fragile territory): Ob 9.
- 17 dice TN 7 Ob 9: expected ~5.1 successes. Almost certainly Failure.
- **This operation requires collective Mending.** Solo practitioners cannot achieve Ob 9 at 17 dice. A collective with 3+ helpers contributing +6-8 dice: total ~23-25 dice. Expected ~7.5 successes. Ob 9 is achievable but not reliable.

**FINDING: Locked Zone Mending is a multi-practitioner, multi-season project requiring specific prerequisites. This is correct — the Einhir needed generations of practitioners at their site-network to maintain this level of work. A campaign-ending achievement, not a mid-session operation.**

---

# TEST S-15: FORCED CONTACT AT COHERENCE 0

**Setup:** A practitioner at Coherence 0 (Rendering Crisis — their rendering of reality is no longer functional). Can they Leap? What happens if a threadcut being or environmental Thread event forces contact?

**Voluntary Leap at Coherence 0:**
- The Leap prerequisites (v2.3) are: Approach Training tag, TS 30+, not in melee, not incapacitated. Coherence is not a prerequisite.
- **Can a practitioner whose rendering has collapsed Leap?** The Leap is the suspension of rendering. If rendering has already collapsed, what is being suspended? There is nothing to let go of. The practitioner is already beyond their own rendering.
- **Philosophical answer:** A practitioner at Coherence 0 IS in a permanent state of rendering failure. Their consciousness can no longer perform the constitutive function that makes them human. They are not "in contact" — they are not anything. They cannot form intentionality because intentionality requires rendering (you must render the target to set intention toward it). They cannot Diagnose because Diagnosis IS rendering. They are functionally incapable of Thread operations.

**PATCH NEEDED: Coherence 0 prevents all Thread operations. The practitioner cannot Leap because they cannot form intentionality (no Diagnosis possible — rendering has failed). This is implicit in the Rendering Crisis description ("reality as commonly rendered is no longer accessible") but should be stated explicitly: "A practitioner at Coherence 0 cannot attempt the Leap, Diagnosis, or any Thread operation. Their rendering has collapsed; they cannot form the intentionality required to direct an operation."**

**Forced contact by external event:**
- What if a threadcut being interacts with the practitioner's configuration directly? The being operates through continuous Thread work. If it targets the Coherence 0 practitioner, it is interacting with a configuration that is no longer self-rendering.
- The practitioner is not "in contact" — they haven't Leaped. Their configuration is passive. The threadcut being's Thread work operates ON them. This is non-consensual Thread work on a sentient being (Certainty −1 for the being, per existing rules).
- For the practitioner: they are already at Coherence 0. They cannot perceive the being (their rendering is non-functional). The being's work affects their configuration but the practitioner is not conscious of it in any renderable sense.
- **Can the being's Thread work restore the practitioner's rendering?** Weaving toward coherence could theoretically stabilise the practitioner's configuration — re-establishing the rendering function. This would be Mending at the Personal scale (repairing a person's rendering substrate). Ob: depends on severity of the collapse. The practitioner would need to be Woven back to a Coherence that permits function.

**ISSUE: Can Weaving restore Coherence?** The recovery rules (§3.5) say: non-practice, Knot anchoring, Einhir techniques. Weaving is not listed. But philosophically, Weaving draws configurations toward coherence — and Coherence IS the stability of the practitioner's configuration. Could a sufficiently skilled practitioner Weave another practitioner's rendering back toward stability?

**Resolution:** Yes, with strict limits. This IS the "corrective Weaving" already mentioned in §3.4 ("another practitioner may perform corrective Weaving (Ob 3) to stabilise the degraded practitioner's configuration: +1 Coherence per season"). At Coherence 0, the corrective Weaving is Ob 5 (the configuration has fully collapsed — more work required). Success: +1 Coherence (practitioner rises to 1/Severed). The practitioner is now functional but severely impaired. This requires the degraded practitioner's cooperation below Coherence 3, which at Coherence 0 means... they cannot cooperate because they cannot render. **Exception needed: corrective Weaving at Coherence 0 does NOT require the target's cooperation because the target cannot render well enough to cooperate or resist. The corrective practitioner operates unilaterally on the collapsed configuration.**

**PATCH NEEDED: Corrective Weaving at Coherence 0 — Ob 5, does not require target's cooperation (target cannot render). Success: +1 Coherence. Multiple seasons of corrective Weaving required to restore function.**

---

# TEST S-16: THE KNOT RECOVERY LOOP

**Setup:** A practitioner operates aggressively, loses Coherence, uses Knot Anchoring to recover, then operates again. Is there a ceiling on this cycle?

**The loop:**
1. Practitioner at Coherence 7 performs Relational Weaving. Coherence: 7 → 6.
2. Next session: Anchoring Scene with Close Knot. Bonds check TN 7 Ob 2. Success: +1 Coherence (6 → 7). Knot strain: +1.
3. Practitioner operates again. Coherence: 7 → 6.
4. Anchoring again. +1 Coherence. Knot strain: +1 more. Total: +2.
5. Repeat.

**Strain accumulation:** Each Anchoring costs the Knot +1 strain. Close Knot wrongness threshold: 3. After 3 Anchorings: Knot at wrongness. After 6: Crisis. At Crisis: Knot cannot be used for Anchoring.

**Recovery rate of Knot strain:** Close Knot: −1 strain per season of active positive engagement. If the practitioner is using 1 Anchoring per session (~2-3 per season) and recovering −1 strain per season, the net is +1 to +2 strain per season. The Knot hits wrongness in ~2 seasons and Crisis in ~4.

**Can the practitioner rotate Knots?** If they have multiple Close Knots (up to Bonds score), they can rotate Anchoring across Knots, spreading the strain. With 3 Close Knots and 1 Anchoring per session: each Knot receives ~1 Anchoring per 3 sessions. Strain: ~1 per 3 sessions per Knot. Recovery: −1 per season per Knot with active engagement. If a season = 3 sessions: the strain rate (~1 per 3 sessions) equals the recovery rate (−1 per season). **Equilibrium.** The practitioner can sustain ~1 Relational operation per 3 sessions indefinitely by rotating Anchoring across 3 Close Knots, provided they actively maintain all 3 relationships.

**Is this a problem?** One Relational operation per 3 sessions is modest. The practitioner is investing significant resources (3 Close Knots, active relationship maintenance each season, Bonds checks each Anchoring with failure risk) to sustain a moderate practice rate. This is exactly the intended balance — Thread practice demands relational investment.

**What if the practitioner tries to accelerate?** 2 Relational operations per session + 2 Anchorings. Strain: +2 per session across Knots. Even with 3 Knots: ~2 strain per 3 sessions per Knot. Recovery: −1 per season. Net: +1 strain per season per Knot. All Knots at wrongness in 3 seasons. Crisis in 6. The practitioner burns through their relationships by late campaign.

**FINDING: No patch needed. The Knot system naturally caps the recovery loop. Aggressive use burns Knots. Moderate use is sustainable with investment. The system rewards practitioners who maintain relationships and punishes those who treat Knots as renewable resources.**

---

# TEST S-17: THE RUPTURE — RS 0

**Setup:** RS reaches 0 during Accounting. What happens mechanically?

**Current rule (§5.3):** "The Rupture. Rendered reality fails. Campaign ends in catastrophe. No faction wins."

**Is this sufficient?** For the board game: yes. It's a shared loss condition. Game over. For the TTRPG and hybrid: a campaign-ending event needs more than one sentence. What do the characters experience? What can they do?

**The Rupture is not the world ending.** Per the Foundations: the Ein Sof is infinite positive being. RS 0 means the rendered world's capacity to integrate what the ground provides has completely failed. The ground doesn't stop. Being doesn't stop. What stops is rendering — consciousness's ability to perform the constitutive function that makes the world intelligible. The world doesn't end. It becomes unintelligible.

**What this looks like:**
- Non-practitioners: total rendering failure. Reality is no longer coherent. Memories conflict. Objects are in multiple states. Spatial relationships become unreliable. Time is non-linear. This is not madness — the world itself has become unintelligible. Every non-practitioner experiences what the Fragmented Fallout table describes, but permanently and comprehensively.
- Practitioners: their TS perception now renders a world that has no stable intelligible surface. They can perceive threads but the threads have no coherent above-the-waterline portion. Everything is below the waterline. They can perceive more than non-practitioners but what they perceive is chaotic configurational activity without stable rendering.
- Threadcut beings: unaffected in their own rendering (they sustain themselves through Thread work, not through the world's rendering). But the world around them has become unintelligible. They exist in a sea of configurational chaos, sustaining their own island of coherence.
- Gaps are everywhere. There is no distinction between Gap and non-Gap because the entire rendered surface has failed. Monstrous configurations emerge continuously — not because the ground is hostile but because the unintelligible ground's positive being floods through everywhere, unrendered.

**ISSUE: Is the Rupture reversible?** Could practitioners Mend the entire world's rendering? The scale would be beyond Structural — it would be Foundational, operating on the substrate of the entire rendered world. Ob: effectively infinite. No practitioner or collective could achieve this. The Einhir at their peak might have had the infrastructure. Post-Catastrophe practitioners cannot.

**Resolution:** The Rupture is mechanically irreversible within the campaign. It IS the campaign-ending condition. For TTRPG, the GM narrates the Rupture as the final session: characters experiencing the dissolution of intelligible reality. PCs with high TS may perceive what is happening. Devout characters may interpret it theologically. The Rupture is the campaign's tragedy ending — the rendered world failed because those responsible for maintaining it (practitioners, institutions, factions) could not or would not cooperate to preserve it.

**FINDING: The Rupture description should be expanded from one sentence to a paragraph in the RS section, covering what characters experience. No mechanical change — it's a narrative endpoint, not a recoverable state. The expansion is framing, not mechanics.**

---

# TEST S-18: INVOLUNTARY LEAP AT TS 90+

**Setup:** A TS 92 practitioner (Coherence 5, Focus 4) is walking through a market when a significant Thread operation occurs within the district. Per TS passive perception table: "TS 90-100: Thread operations across the district; significant operations → involuntary Leap risk (Focus check TN 7 Ob 1)."

**The Focus check:**
- Focus 4: 4 dice TN 7 Ob 1. Expected ~1.2 successes. Likely success (practitioner resists involuntary Leap).
- **Say Failure:** The practitioner's rendering suspends involuntarily.

**What happens during an involuntary Leap:**
- The practitioner has NOT Diagnosed. They have NOT set intentionality. They have NOT declared an operation. Their rendering has simply... stopped. Their consciousness has been pulled beyond itself by the intensity of the nearby Thread activity.
- This is not a Leap in the operational sense. It is an involuntary rendering suspension — the practitioner's sensitivity is so high that intense Thread activity in the vicinity overwhelms their rendering's capacity to hold.

**ISSUE FOUND: Involuntary Leap mechanics under the new Diagnosis-before-Leap framework.** The operational Leap requires Diagnosis and declaration before the suspension. An involuntary Leap has neither. The practitioner is in contact without intentionality. Their configuration is interacting with the ambient Thread environment without direction.

**What happens to a configuration in contact without intentionality?**
- No operation occurs. The practitioner is simply Beyond their own rendering, experiencing the thread-level process without acting on it.
- But their configuration IS interacting with the ambient threads — it can't not interact. Without intentionality to direct the interaction, the practitioner's configuration is a leaf in a current. Ambient Thread activity flows through them.
- **Co-movement fires.** Even without an operation, the practitioner's configuration is interacting with threads. The temporal auto-effect fires: Coherence −1 (this is a Relational+ scale interaction — ambient district-level Thread activity). The epistemic effect fires: the practitioner perceives things they didn't choose to perceive. The actual d6 fires: something happens to the practitioner's physical configuration.
- **Coherence loss without benefit.** The practitioner loses Coherence from the involuntary contact but gains nothing — no operation was performed, no outcome was achieved. This is pure cost.

**Duration:** How long does involuntary contact last? The practitioner didn't choose to Leap, so Focus doesn't apply (Focus is the capacity to sustain chosen suspension). The involuntary contact persists until the triggering Thread activity ends or the practitioner's rendering reasserts.

**Resolution:** Involuntary Leap duration = 1 round. The practitioner's rendering reasserts quickly because there is no intentionality holding it open. The suspension was forced by external stimulus, not sustained by internal commitment. After 1 round, the practitioner returns to rendering — disoriented, having lost 1 Coherence, having perceived something they may not understand.

**If the practitioner WANTS to stay in contact:** They may attempt a standard Leap roll in the round after the involuntary suspension, using the involuntary contact as a running start. This Leap does not require a separate Diagnosis round (the practitioner's configuration has already begun interacting — they can set intentionality "from within" the contact). However: the Ob is +1 (setting intentionality mid-contact is harder than setting it pre-Leap). And the operation fires without the full Diagnosis information — the practitioner sensed the ambient Thread environment but did not carefully render and assess a specific target.

**PATCH NEEDED: Involuntary Leap mechanics — 1 round duration, no operation, co-movement fires (Coherence −1, d6), practitioner returns to rendering disoriented. Optional: standard Leap roll next round to extend into voluntary contact at +1 Ob, without Diagnosis.**

---

# FINDINGS SUMMARY — BATCH 3

## Issues Found

| # | Issue | Severity | Source Test |
|---|---|---|---|
| 18 | RS consequences don't scale with operation scale | SIGNIFICANT | S-13 |
| 19 | "Einhir ritual framework" undefined | MODERATE | S-14 |
| 20 | Coherence 0 doesn't explicitly prevent Thread operations | MODERATE | S-15 |
| 21 | Corrective Weaving at Coherence 0 — cooperation requirement impossible | MODERATE | S-15 |
| 22 | Involuntary Leap mechanics undefined under new framework | SIGNIFICANT | S-18 |
| 23 | Rupture description insufficient for TTRPG/hybrid | LOW (framing) | S-17 |

## Proposed Patches

| # | Patch | Targets Issue |
|---|---|---|
| P-25 | RS consequences scale with operation scale on Partial/Failure. Object/Personal: −1. Relational: −2. Territorial: −4. Structural: −6. Collective operations scale with participant count (×1.5 for 3-4, ×2 for 5+). | 18 |
| P-26 | Define "Einhir ritual framework": Knowledge of Einhir Mending techniques + at least one applicable Einhir Text technique + physical presence at site-network node. All three required. Without all three, Locked Zone Mending is impossible. | 19 |
| P-27 | Coherence 0 explicitly prevents all Thread operations. Cannot Leap, Diagnose, or form intentionality. Rendering has collapsed. | 20 |
| P-28 | Corrective Weaving at Coherence 0: Ob 5, does NOT require target's cooperation (target cannot render). Success: +1 Coherence. Multiple seasons required. | 21 |
| P-29 | Involuntary Leap: 1 round duration, no operation, co-movement fires (Coherence −1 minimum, d6). Optional voluntary extension: standard Leap roll next round at +1 Ob, without Diagnosis. | 22 |
| P-30 | Rupture description expanded: what characters experience by type (non-practitioner, practitioner, threadcut being). Narrative endpoint, not recoverable. | 23 |

## Confirmed Design Decisions (no patch needed)

| Finding | Decision | Rationale |
|---|---|---|
| Over-actualisation does not stack across seasons | Clears at Accounting | The Einhir Catastrophe is modelled by configurations' actualization level rising naturally over generations, not by penalty stacking. |
| Core Zone Focus halving eliminates low-Focus helpers | Intended | The Core Zone is a legitimate gate on who can participate in Southernmost operations. |
| Knot recovery loop is self-limiting | No patch | Strain accumulation naturally caps Anchoring frequency. 3 Close Knots sustain ~1 Relational op per 3 sessions at equilibrium. |
| Rupture is mechanically irreversible | Intended | Campaign-ending condition. No in-campaign recovery possible. |

## Running Patch Count

| Batch | Patches |
|---|---|
| Initial review (P-01 through P-10) | 10 |
| Batch 1 (P-11 through P-20) | 10 |
| Batch 2 (P-21 through P-24) | 4 |
| Batch 3 (P-25 through P-30) | 6 |
| **Total** | **30** |
