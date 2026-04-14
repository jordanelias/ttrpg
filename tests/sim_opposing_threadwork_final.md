# STRESS TEST: Opposing Threadwork — Final Consolidated Audit
## Date: 2026-04-13
## Status: FINAL — ready for editorial review and commit
## Method: Philosophy-first derivation → scenario testing → audit → fix → consolidate
## Supersedes: sim_opposing_threadwork.md (v1), sim_opposing_threadwork_v2_philosophy_audit.md (v2)

---

## FETCH LOG
canonical_sources.yaml: ✓ (184 lines)
designs/ttrpg/threadwork_redesign_v25.md: ✓ (877 lines)
designs/ttrpg/threadwork_philosophical_reference.md: ✓ (70 lines)
references/params_threadwork.md: ✓ (811 lines)
references/params_core.md: ✓ (188 lines)
references/params_combat.md: ✓ (286 lines)
references/params_contest.md: ✓ (255 lines)
canon/00_philosophical_foundations.md: ✓ (1349 lines)
canon/01_foundations_amendment_self_rendering.md: ✓ (138 lines)
canon/02_canon_constraints.md: ✓ (26 lines)
references/propagation_map.md: ✓ (469 lines)
tests/coverage_matrix.md: ✓ (698 lines)

---

# SECTION A: FIXES FROM V2 AUDIT

## Fix 1: "Winner Degrades One Degree" Row — Minimum Success

**V2 proposal:** "One meets Ob, one Partial → winner resolves at one degree worse (minimum Success)."

**Problem:** If winner achieved Success, degrading one degree = Partial. But Partial means net successes < Ob. The winner met Ob. Resolving at a degree below the threshold they exceeded is a mechanical contradiction — the degree system is defined by net successes vs Ob, not by a floating modifier.

**Philosophical re-examination:** The Partial opponent's configuration was in the originary space but INEFFECTIVE (below Ob). Their presence is a weak source of resistance — their knot to the shared thread absorbs some energy flowing through the thread. This can attenuate EXCESS effects (Overwhelming → Success) but cannot negate effects the winner's engagement earned against the modified Ob. The winner met or exceeded their Ob; that threshold already includes the opposing engagement modifier (+TPS/2), which is the primary mechanical expression of the opponent's resistance.

**Fix:** Winner resolves at achieved degree. If Overwhelming, degrade to Success (the Partial opponent's weak presence absorbed the excess). If Success, no degradation. The degree system is not overridden by a floating modifier — the Ob modifier already accounts for the opposition.

**Consequence for the Partial practitioner:** Unchanged — knot strain (+1 Ob next op, 2 Composure). The partial engagement was insufficient to redirect the thread but the practitioner was knotted to a thread that moved against them.

## Fix 2: "Both Meet Ob" RS Cost — Shifting Object Source

**V2 proposal:** "Do not apply both degree-table RS costs. Apply only RS cost from Shifting Object formation."

**Problem on re-examination:** The degree tables' RS costs represent substrate strain from the operation's engagement. When both operations engage deeply enough to redirect (both meet Ob), BOTH engagements strained the substrate. The strain didn't produce the intended effect (the thread oscillated instead of moving in either direction), but the substrate WAS strained by both engagements. Dismissing the degree-table RS costs entirely under-prices the compound disturbance.

**Philosophical re-derivation:** The substrate registered two deep engagements driving it in opposite directions. Neither resolved. The thread oscillated. The RS cost should reflect:
- The compound substrate disturbance from two simultaneous deep engagements (worse than one engagement alone).
- NOT the sum of two independent operations' costs (they are one compound event, not two independent events).

**Fix:** When a Shifting Object forms from opposing operations, RS cost = **worst single degree-table RS cost + 1** (the +1 represents the compounding from the second engagement). Not the sum of both. Not zero.

Example: Weaving Success (RS unchanged) vs Pulling Success (RS unchanged). Worst = 0. RS cost = 0 + 1 = −1. With the Shifting Object persisting to Accounting: additional −4 RS/season from Gap deterioration pathway.

Example: Weaving Partial (RS −1) vs Pulling Overwhelming (RS unchanged). Worst = −1. RS cost = −1 + 1 = −2.

## Fix 3: Composure as Knot Strain Track — Cross-System Audit

**V2 proposal:** Knot strain costs Composure (2 for standard, 4 for FR vs FR).

**Audit:** Composure = Charisma + 6, range 7–13. Restores at scene change. Rattled at depletion (Composure resets, +1 Ob cumulative). 2 Rattled marks = socially incapacitated.

Knot strain of 2 Composure on a Charisma 3 character (Composure 9): 9 → 7. No Rattled. Manageable.
Knot strain of 4 Composure on Charisma 2 character (Composure 8): 8 → 4. No Rattled. But significant — leaves the practitioner vulnerable to social pressure for the remainder of the scene.

The Leap Partial result already costs 2 Composure (params_threadwork: "Unstable. Op Ob +1. −2 Composure"). So Composure is an established thread-disruption cost track. Knot strain at 2 Composure is consistent with the existing precedent.

**Cross-system interaction:** A practitioner who takes knot strain and then enters a social contest in the same scene has reduced Composure. Is this appropriate?

**Philosophical audit:** Yes. The practitioner's configuration was stressed by the contested interaction. Upon returning to rendering, their self-presentation is disrupted — their layer 2 self-rendering reasserted with residual thread-level stress. This manifests as reduced social resilience (Composure) because the practitioner's rendering of themselves to others is less stable. This cross-system consequence follows directly from the three-layer model (Amendment 01) and is the kind of interconnection the system rewards.

Composure restores at scene change, so knot strain is a within-scene penalty. This is proportional — knot strain is a momentary disruption from the contested interaction, not a permanent injury.

**Verdict:** Composure confirmed as the correct track. No fix needed.

## Fix 4: Co-Movement Firing — Per-Practitioner vs Per-Event Clarification

**V2 proposal:** "Co-movement fires ONCE for the compound event, not per-operation."

**Re-examination by axis:**

- **Temporal auto-effect (Coherence):** This is a per-PRACTITIONER cost from suspending layer 2 (§3.2). Each practitioner suspended their own rendering. Each practitioner's layer 2 integrity degrades from the suspension. This fires per-practitioner regardless of what happened during contact. Two practitioners = two Coherence decrements. This is NOT co-movement — it is the Leap cost.

- **Epistemic auto-effect (investigation Ob, perception):** This is a consequence of the THREAD's disturbance on the rendered world's intelligibility at that site. The thread experienced one compound disturbance (two opposing configurations). The epistemic effect is how OBSERVERS render the aftermath. Observers perceive one event (the site where two configurations contested the same thread), not two independent events. Fires once.

- **Actual auto-effect (d6):** This represents consequences of the originary interaction that don't resolve into intelligible patterns. One compound interaction → one d6 roll. The interaction was a single event in the originary space (two configurations engaged the same thread simultaneously). The unintelligible consequences are from the compound event, not from two separate interactions.

**Fix:** Coherence fires per-practitioner (2 decrements for 2 practitioners — this is the Leap/contact cost, not co-movement). Epistemic and actual effects fire once for the compound event. This is the correct decomposition — Coherence is a personal-track cost from layer 2 suspension, and co-movement is a world-level consequence of the thread's disturbance.

---

# SECTION B: ADDITIONAL SCENARIO TESTING

## Scenario B-1: Multi-Round Contact — Sequential Opposing Operations

**Setup:** Expert A (Focus 4, Weave pool 19D) and Competent B (Focus 3, Pull pool 15D) oppose at Relational scale. Round 1 = Leap. Round 2 = opposing operations (Weave vs Pull). Round 3 = ?

**Round 2 resolution (assuming both meet Ob → Shifting Object forms):**
Treaty becomes a Relational Shifting Object. Both take knot strain (+1 Ob next op, 2 Composure).

**Round 3 — What can they do?**
Expert A has Focus 4 → Contact Rounds = 4 → still in contact (Round 3 of 4).
Competent B has Focus 3 → Contact Rounds = 3 → still in contact (Round 3 of 3, last operation round).

Both can declare operations for Round 3 — but these were pre-declared before the Leap (§2.4: "each was declared before the Leap as part of the overall intentionality").

**Philosophical audit:** Can a practitioner pre-declare an operation targeting a state that might not exist? They declared during Diagnosis: "Round 2: Weave the treaty. Round 3: Weave the treaty again (reinforcement)." But if the treaty became a Shifting Object in Round 2, the Round 3 intentionality is directed at a configuration that no longer exists in its declared form. The practitioner is not consciously present to adapt (rendering is suspended).

This is the **sequential failure penalty** mechanic applied to a new context. §2.4: "If an operation fails, all subsequent operations in the same contact window are at +1 Ob (cumulative). The practitioner's intentionality was set assuming each step would succeed. When one fails, the remaining intentions are directed at a state that no longer matches."

The opposing operation didn't "fail" in the traditional sense — it produced a Shifting Object. But the target configuration no longer matches the declared intentionality. The practitioner intended to Weave a treaty — the treaty is now a Shifting Object. The +1 Ob sequential penalty applies (the intentionality is misaligned with the current state).

Additionally, the knot strain from Round 2 gives +1 Ob. Total penalty for Round 3: +2 Ob.

**What operation does Round 3 become?** The practitioner declared "Weave the treaty." The treaty is now a Shifting Object. Weaving a Shifting Object would drive it toward coherence — stabilizing the oscillation, resolving it toward the state the practitioner originally intended. This is a valid operation (Weaving doesn't require a stable target — it drives whatever configuration it engages toward coherence).

**If both practitioners declare Round 3 operations on the same target:** They are again opposing each other. The opposing operations procedure fires again. Modified Ob for each: base Ob + opposing engagement modifier + sequential penalty (+1) + knot strain (+1).

Expert A: Weave Relational Ob 3 + opposing +2 + sequential +1 + knot strain +1 = Ob 7. At 19D: P(≥7) ≈ 40%.
Competent B: Pull (Shifting Object = loosely actualised) Ob 1 + opposing +3 + sequential +1 + knot strain +1 = Ob 6. At 15D: P(≥6) ≈ 50%.

**Finding B-1a:** Multi-round opposing operations produce escalating difficulty through legitimate stacking (sequential penalty + knot strain + opposing modifier). By Round 3, the operations are significantly harder (Ob 6–7 vs original Ob 2–3). This naturally limits the number of rounds practitioners can sustain opposition — which is the Focus mechanic working as designed. Focus represents how long you can hold rendering at bay; in contested operations, it also represents how long you can sustain opposing engagement before penalties make further operations untenable.

**Finding B-1b:** If the Round 3 opposing operations also produce a Shifting Object, the thread has now been driven into oscillation twice. Does this compound the Shifting Object? The current rules don't address "Shifting Object on a Shifting Object." Philosophically: the oscillation is being intensified — driven further from any stable configuration. The Shifting Object should advance one severity tier (toward Gap formation) — equivalent to 1 season of deterioration compressed into one scene. This is a natural consequence of sustained opposing engagement: the thread is being torn between configurations repeatedly, accelerating its collapse.

**Proposed:** Opposing operations producing a Shifting Object on an existing Shifting Object advance the Shifting Object one deterioration tier. A standard Shifting Object deteriorates to a Gap within 1d3 seasons; a twice-contested Shifting Object deteriorates in 1d3 sessions instead.

## Scenario B-2: Novice vs Master — Asymmetric Opposition

**Setup:** Novice (TS 32, TPS 3, Weave pool 10D) opposes Master (TS 95, TPS 9, Pull pool 23D) at Personal scale.

**Opposing engagement modifiers:**
- Novice: +floor(9 ÷ 2) = +4 to Weave Ob.
- Master: +floor(3 ÷ 2) = +1 to Pull Ob.
- Novice effective Ob: 2 (Personal Weave) + 4 = 6.
- Master effective Ob: 2 (Normally Actualised) + 1 = 3.

Novice at 10D, Ob 6: P(≥6) ≈ 15%. Mostly Partial or Failure.
Master at 23D, Ob 3: P(≥3) ≈ 99%. Virtually certain Success. P(Overwhelming, ≥6) ≈ 85%.

**Joint outcome:**
- Master overwhelms, Novice fails to meet Ob: ~85% × 85% ≈ 72%.
- Master overwhelms, Novice meets Ob: ~85% × 15% ≈ 13%.
- Master succeeds, Novice fails: ~14% × 85% ≈ 12%.
- Novice meets Ob, Master fails: ~15% × 1% ≈ 0.2%.

**Dominant outcome (72%):** Master's Pull resolves at Overwhelming (Novice didn't meet Ob → no degradation of Overwhelming). Novice takes Failure consequences (they genuinely failed to engage the thread against the Master's overwhelming resistance).

**Philosophical audit:** The Novice faces Ob 6 on 10D — their configuration is crushed by the Master's depth of engagement. The +4 modifier from the Master's TPS reflects the Master's configuration occupying so much of the originary space that the Novice's shallow intentionality can barely reach the thread. This maps to the scale principle: the Master's TS 95 means their configuration extends almost to the unintelligible ground. The Novice's TS 32 gives them a thin sliver of engagement. The Master's depth doesn't just oppose the Novice — it overwhelms the space the Novice needs to operate in.

**Finding B-2:** The asymmetric Ob modifier correctly prices the power differential. A Novice opposing a Master is mechanically futile without allies — which is canon-appropriate (the Einhir were defeated by the Calamity's scale, not by individual practitioners of greater power).

## Scenario B-3: Cascade — Opposing Ops Through Accounting

**Setup:** Season 3. RS 52 (Strained). Competent vs Competent at Relational scale produce a Shifting Object. No one Mends it. Track through Accounting.

**Round of opposition:** Both succeed → Shifting Object (Relational). RS: 52 − 1 (contest stress) = 51.

**Accounting (Season 3):**
- Shifting Object persists → deteriorates toward Gap. d3 roll for deterioration timeline: say 2 seasons.
- Lock in adjacent territory (3 seasons old): RS drift −1.
- Winter drift: −1 (per §5.2? Let me check — PP-239 says "RS does not decay naturally. All RS changes are event-driven." Winter drift IS listed in §5.2: "Winter annual drift: −1." But PP-239 says no natural decay. Contradiction? No — winter drift is listed in §5.2 as a source. PP-239 clarifies no NATURAL decay beyond listed sources. Winter drift is a listed source.)
- No other RS changes.
- Net RS at Accounting: 51 − 1 (Lock drift) − 1 (winter) = 49.

**Accounting (Season 4):**
- Shifting Object still present (1 season into 2-season deterioration).
- Spontaneous Shifting Object check (RS 49 < 60 = Fragile threshold at Accounting): 1 random Shifting Object in high-traffic Thread territory.
- Lock drift: −2 (4+ seasons → increased drift per §2.4 Lock chronic: −2/season at 4+ seasons).
- Winter: −1.
- Net RS: 49 − 2 − 1 = 46.

**Accounting (Season 5):**
- Original Shifting Object deteriorates into Relational Gap (2-season timeline hit).
- Gap persists: −4 RS/season from this point.
- Spontaneous Shifting Object check: 1 random.
- Lock drift: −2.
- Winter: −1.
- Net RS: 46 − 4 − 2 − 1 = 39. **Crossed into Fractured band at next Accounting.**

**Finding B-3a:** A single opposed operation at Relational scale, left unaddressed, drives RS from 52 to 39 in 3 seasons. The cascade is steep and accelerating. This is the designed behavior — the game punishes neglect of thread instability. The opposing operation itself contributed RS −1; the cascading consequences contributed RS −12.

**Finding B-3b:** The +1 RS "contest stress" from the initial opposing operation is a trivial share of the total cascade cost. The real damage comes from the Shifting Object → Gap → RS drain pathway. This confirms that the initial RS cost should be modest (the contest itself is a minor substrate disturbance; the persistent instability it creates is the real threat).

## Scenario B-4: Combat Timing — Two Leaps at Priority 5

**Setup:** Combat round. Crown practitioner and Niflhel practitioner both declare Leap (Priority 5, full-round action) targeting the same configuration.

**Priority resolution:** Both at Priority 5. Per params_combat PP-247: Priority 5 = Leap (Thread — full-round). Both Leaps are at the same Priority — they resolve simultaneously.

**Declaration:** Both practitioners declare operation type and target before the Leap roll (§2.4). Declarations happen at the start of the round (when Priority 5 actions are announced). Both hear each other's declarations — they know they are about to enter opposing contact.

**Philosophical audit:** Knowing the opponent is about to Leap changes the Diagnosis. The practitioner diagnosed the target configuration AND now knows another practitioner will be engaging it from the opposite direction. Does this affect their intentionality?

Yes — but the Diagnosis is already complete and the declaration is already made. The practitioner cannot change their operation type or target (§2.4: "Once the Leap succeeds, the operation proceeds as declared"). The awareness of opposition might cause the practitioner to withdraw (choose not to Leap) — but if they proceed, their intentionality is as declared.

**Can a practitioner choose not to Leap after hearing the opposing declaration?**
The declaration is the commitment. Withdrawing after declaration but before rolling would forfeit the full-round action (Priority 5 = full round, no attack, no movement). But the practitioner could choose to "hold" — decline to roll the Leap — and forfeit the round without entering contact. This is a meaningful choice: accept the lost round rather than enter contested contact.

**Finding B-4:** No mechanical fix needed. The combat priority system handles simultaneous Leaps correctly. The only addition: explicitly note that a practitioner who has declared Leap may withdraw before rolling (forfeiting the round) if they learn of opposing engagement. This is a TACTICAL choice, not a mechanical gap.

## Scenario B-5: Ob Modifier Stacking — Degenerate Case Check

**Worst realistic case:** Competent (15D, Weave pool) targets Relational Over-Actualised configuration. Opposing Expert (TPS 7). Competent has 1 Wound. Coherence 4 (Fragmented, +1 Ob). OA on target (+1 Ob).

Total Ob: 3 (Relational) + 3 (opposing, TPS 7/2) + 1 (OA) + 1 (Wound) + 1 (Fragmented) = 9.

At 15D, Ob 9: P(≥9) ≈ 3%. Nearly impossible.

**Is this correct?** A Wounded, Fragmented Competent practitioner opposing an Expert on an over-actualized Relational thread SHOULD find this nearly impossible. Each modifier represents a real physical or metaphysical obstacle:
- Opposing engagement (+3): the Expert's deep configuration resists.
- OA (+1): the thread is already too rigid.
- Wound (+1): the body's damage impedes suspension (§2.3).
- Fragmented (+1): rendering reasserts more aggressively (§3.3).

All modifiers are sourced from different mechanical systems. No double-counting. The stacking is legitimate.

**Finding B-5:** No degenerate stacking found. The Ob modifier does not create novel degeneracies beyond what the existing modifier stack already produces. The additional +1 to +5 from opposing engagement is proportional to the opponent's Thread capacity.

---

# SECTION C: FINAL CONSOLIDATED PROCEDURE

## C.1 Opposing Operations — Contested Intentionality

**Scope:** Two practitioners in contact (both Leaps succeeded) targeting the SAME configuration with opposing intentionalities.

**What qualifies as "opposing intentionalities":**
- Weave vs Pull (coherence vs potential): Yes — spectrum opposition.
- Lock vs Dissolution (frozen actualization vs tearing): Yes — extreme FR opposition.
- Lock vs Pull (frozen vs loosened): Yes — one drives toward maximum actualization, the other toward potential.
- Weave vs Dissolution (coherence vs tearing): Yes — one stabilizes, the other destroys.
- Weave vs Lock: NO — both drive toward actualization (Lock is an extreme of what Weave does). These compound, not oppose.
- Pull vs Dissolution: NO — both reduce the thread's actualization/intelligibility. These compound.
- Any operation vs Mending: NO — Mending targets substrate absence, not threads. Categorically different targets. (Foundations §2.4: Mending targets "the space between threads.")

**What qualifies as "the same configuration":**
- Same specific thread at the same scale: Yes.
- Same entity at different scales (Object vs Relational): No — different configurations (the Object-scale thread is a part of the Relational-scale configuration, not the same entity).
- Same location but different targets (e.g., one targets a thread, one targets a Gap): No — different target categories.

### Step 1 — Opposing Engagement Modifier

Each practitioner's Ob is increased by the opponent's Thread depth:

**Opposing Engagement Modifier = +floor(opponent's Thread Pool Score ÷ 2), minimum +1.**

| Opponent TPS (= TS ÷ 10) | Modifier |
|---|---|
| 3 (TS 30–39) | +1 |
| 4–5 (TS 40–59) | +2 |
| 6–7 (TS 60–79) | +3 |
| 8–9 (TS 80–99) | +4 |
| 10 (TS 100) | +5 |

This modifier stacks with all other applicable Ob modifiers (Wounds, Coherence threshold penalties, Over-Actualisation, territory effects, sequential failure penalty, knot strain from prior contested operations).

**Canon basis:** The opponent's configuration is in the originary space, driving the thread in the opposite direction. Their depth of engagement (TPS = perceptual depth that shaped the pre-Leap intentionality) determines how much resistance they create for the opposing configuration. This is rendered-side resistance (P-07 compliant — not the ground responding).

### Step 2 — Both Roll

Both practitioners roll their operation pools against their modified Obs. Standard d10, TN 7 resolution. Degree determination per standard four-degree system:
- Overwhelming: net successes ≥ 2 × Ob.
- Success: net successes ≥ Ob but < 2 × Ob.
- Partial: net successes ≥ 1 but < Ob.
- Failure: net successes ≤ 0.

### Step 3 — Resolution

| A's Result | B's Result | Thread Outcome | RS Cost | A's Consequences | B's Consequences |
|---|---|---|---|---|---|
| **Meets Ob** | **Meets Ob** | **Shifting Object** at target's scale. Thread oscillates between the two intended states. | Worst single degree-table RS cost + 1 (compound disturbance). | Coherence per §3.2 scale. Knot strain: +1 Ob next Thread op this scene, 2 Composure. | Same as A. |
| **Meets Ob** | **Partial** | **A's operation resolves.** If A achieved Overwhelming: degrade to Success (B's weak presence absorbed the excess). If A achieved Success: no degradation. | A's degree-table RS cost + 1 (contest stress). | Coherence per §3.2. 1 Composure (minor knot strain — contested but victorious). | Coherence per §3.2. Knot strain: +1 Ob, 2 Composure. Operation does NOT resolve. Does NOT take degree-table consequences. |
| **Meets Ob** | **Failure** | **A's operation resolves at achieved degree.** B's configuration failed to engage — no contest occurred. | A's degree-table RS cost only. No contest stress (no contest). | Normal degree-table consequences. | Standard Failure consequences per B's operation type degree table (genuine engagement failure). |
| **Partial** | **Partial** | **Weak oscillation.** d6: 1–2 = Shifting Object at one scale below target. 3–6 = no Shifting Object; thread stressed but stable. | −1 (contest stress). | Coherence per §3.2. Knot strain: +1 Ob, 2 Composure. | Same as A. |
| **Partial** | **Failure** | **A's Partial resolves as normal Partial.** B never engaged. | A's Partial degree-table RS cost. | Normal Partial consequences. | Standard Failure consequences. |
| **Failure** | **Failure** | **No operation resolves.** Thread stressed by dual failed engagement. | −1 (minor stress). | Coherence per §3.2. 1 Composure (minor — engagement was shallow). | Same as A. |

**FR vs FR modifier (Lock vs Dissolution, or Lock vs Pull at Structural+ scale):**
- All knot strain Composure costs doubled (extreme opposition): standard knot strain = 4 Composure; minor = 2 Composure.
- If winner's operation was Dissolution and loser achieved Partial: the tear propagates through the knot to the loser's configuration — loser takes 1 Wound (thread-level damage through knot propagation, not snap-back; armour does not apply).
- "Both Fail" at FR vs FR: RS cost scales with operation scale: Object −1, Personal −2, Relational −3, Territorial −4, Structural −5. d6 Shifting Object risk: 1–(scale tier number) = Shifting Object. (Object: 1 on d6 = 17%. Territorial: 1–4 on d6 = 67%.)

### Co-Movement (All Cases)

- **Coherence (temporal):** Per-practitioner per §3.2 scale table. This is the Leap/contact cost — each practitioner suspended their own layer 2. Two practitioners = two Coherence decrements. This is NOT co-movement — it is the personal cost of contact.
- **Epistemic (investigation Ob, perception):** Fires ONCE for the compound event. Use the winning operation's epistemic profile if one wins; use the Shifting Object's epistemic profile if both met Ob (observers perceive oscillation — instability, contradiction, wrongness).
- **Actual (d6):** Fires ONCE. Roll once on the relevant operation's actual-effect table (use the winning operation's table if one wins; use the Weaving table if Shifting Object formed, since Shifting Objects are actualization instabilities).

**Canon basis:** Coherence is personal-track (Amendment 01: layer 2 integrity degrades per Leap). Epistemic and actual effects are world-level consequences of the thread's disturbance — one compound disturbance, one set of world consequences.

### Step 4 — Knot Strain Details

| Scenario | Knot Strain on Losing/Tied Practitioner | Knot Strain on Winning Practitioner |
|---|---|---|
| Standard opposition (Weave/Pull) | +1 Ob next Thread op this scene. 2 Composure strain. | 1 Composure strain. No Ob penalty. |
| FR opposition (Lock/Dissolution) | +2 Ob next Thread op this scene. 4 Composure strain. (If winner Dissolved: +1 Wound from tear propagation.) | 2 Composure strain. No Ob penalty. |
| Both meet Ob (tie — Shifting Object) | Both: +1 Ob next Thread op, 2 Composure. (FR tie: +2 Ob, 4 Composure.) | N/A — both are "tied," both take the tie strain. |
| Both fail (no contest) | Both: 1 Composure only. No Ob penalty. | N/A — both failed, both take minor strain. |

**Composure recovery:** Per params_contest: Composure restores at scene change. Knot strain Composure cost persists for the remainder of the current scene only.

**Ob penalty duration:** "+1 Ob next Thread op this scene" expires after the next Thread operation attempt or at scene end, whichever comes first. It does NOT persist into the next scene.

## C.2 Sustained Opposition (Multi-Round Contact)

If both practitioners have remaining contact rounds after an opposing operation:

1. Pre-declared Round N+1 operations fire. If the target configuration changed (e.g., became a Shifting Object), the sequential failure penalty (+1 Ob) applies (intentionality is misaligned with the new state).
2. Knot strain Ob penalty from Round N stacks with the sequential failure penalty.
3. If both practitioners target the Shifting Object with opposing operations: the opposing operations procedure fires again at the new Obs.
4. A Shifting Object that receives another opposing-operations Shifting Object result **advances one deterioration tier** (the oscillation is intensified by repeated contradictory engagement). Standard Shifting Object: deteriorates in 1d3 seasons. Twice-contested: 1d3 sessions. Thrice-contested: end of current scene (the thread is being torn apart).

## C.3 N-Way Opposing Operations (3+ Practitioners)

**Prerequisite:** Three or more practitioners in contact target the same configuration with at least two genuinely opposing intentionalities.

**Resolution:** Automatic lattice collapse (Foundations §12.2: contradictory knotting topology has no stable force distribution).
- All operations fail. No degree-table consequences.
- Gap forms at the target's scale.
- RS: −(2 × number of practitioners with opposing intentionalities).
- All practitioners: Coherence per §3.2 scale table. Knot strain: +2 Ob next op, 4 Composure.

**Canon basis:** A two-way opposition produces a standing wave (Shifting Object). A three-way opposition produces chaotic interference with no stable oscillation mode. The thread cannot oscillate between three contradictory configurations — it collapses. The lattice topology (§12.2) cannot route force coherently when the knots transmit contradictory directions simultaneously. This is the Einhir Catastrophe's mechanism replicated at micro-scale.

## C.4 Mass Battle Simplification

In mass battle Phase 4, opposing Thread operations use a simplified contest (reducing resolution from ~15 steps to ~6):
- Both roll against their individual Obs (opposing engagement modifier still applies).
- Highest net successes wins. Winner resolves at achieved degree. Loser takes Partial consequences (the mass battle abstraction compresses the contest — it's representing an abstract faction-level effort, not a personal-scale interaction).
- Tie: Shifting Object. Both take Partial consequences.
- RS ×3 multiplier (PP-192/PP-225) applies to all RS costs from opposing operations, including contest stress.
- Temporal auto-effects (Coherence) NOT subject to ×3 (PP-226).

## C.5 Mending Immunity

Mending cannot be directly opposed under this procedure. Mending targets substrate absence — a categorically different target from any thread operation.

**Indirect obstruction sources (all stack up to Mending Ob ceiling of 8):**
- Thread operations at the same site (co-movement disturbance): +1 Ob.
- Threadcut being interference (P-17): +TS ÷ 20 (round up), max +4.
- Territory effects, Fraying Bane: per existing rules.
- Rendering Stability threshold penalties (Fragile+): per §5.3.

## C.6 Scale Mismatch

Operations at different scales on the same entity are NOT opposing operations. They target different configurations (the Object-scale thread is a component of the Relational-scale configuration, not the same entity). They resolve independently. Co-movement from both operations fires at the shared site — the epistemic and actual effects compound (observers perceive heightened disturbance; two d6 rolls for actual effects).

## C.7 Board Game Opposing Thread Orders

When two factions issue opposing Thread orders on the same territory:
- Both roll against their Obs.
- If both succeed: Shifting Object in that territory (tracked on territory status card). Draw 1 Co-Movement Card.
- If one succeeds: that faction's order resolves. Draw 1 Co-Movement Card.
- If both fail: no effect. No Co-Movement Card.
- No knot strain, Composure, or Coherence tracking (BG abstracts personal-scale consequences).

## C.8 Hybrid Cross-Phase Opposition

If a Personal Phase Thread operation and a Strategic Phase Thread order target the same configuration with opposing intentionalities:
- Both are held until Cascade Phase (per §7.2).
- At Cascade Phase: resolve using the full opposing operations procedure (§C.1). The TTRPG practitioner's roll from Personal Phase stands. The BG order roll is made at Cascade Phase.
- Opposing Engagement Modifier for the TTRPG practitioner: use the BG faction's Thread-capable NPC's TPS (if specified). If unspecified: use faction Intelligence ÷ 2 (round down, minimum 1).
- Opposing Engagement Modifier for the BG order: use the TTRPG practitioner's TPS.

---

# SECTION D: CANON COMPLIANCE MATRIX

| Constraint | Rule/Patch Element | Compliance |
|---|---|---|
| P-01 Inseparability | Co-movement fires for compound event (all three axes). Coherence per practitioner (personal track). | ✓ |
| P-02 Ein Sof = fullness | Gap from N-way lattice collapse is substrate failure, not void/evil. | ✓ |
| P-03 Rendering = consciousness-performed | Knot strain manifests when practitioner returns to rendering (Composure). Thread-level events ≠ experiential events until rendering reasserts. | ✓ |
| P-07 Calamity = rendered-side mechanism | Opposing engagement modifier comes from opponent's configuration (rendered-side), not from ground. | ✓ |
| P-08 Epistemological barrier | No operation gives non-sensitives Thread-level knowledge. Epistemic co-movement produces perceptual unease, not Thread comprehension. | ✓ |
| P-11 Temporal Disjunction universal | Coherence fires for every practitioner in contact, regardless of outcome. | ✓ |
| P-14 Board/VG inseparability | BG opposing orders produce Shifting Objects + Co-Movement Cards. Hybrid uses full procedure at Cascade Phase. | ✓ |
| P-15 Three-layer being-persistence | Coherence cost = layer 2 suspension cost (per-practitioner). Knot strain = layer 2 disruption on return. Distinct tracks for distinct events. | ✓ |
| Foundations §12.2 Lattice topology | Opposing knotting produces knot strain on both practitioners. N-way lattice collapse from contradictory topology. "Potentially damaging both the target configuration and the practitioners themselves." | ✓ |
| Scale Principle | Ob modifier (+TPS/2) scales with opponent's perceptual depth. FR vs FR consequences scale with operation scale. | ✓ |
| Amendment 01 Three Layers | Coherence = layer 2 cost (Leap). Composure = rendered experience of thread-level disruption on return. No double-charging the same layer. | ✓ |

---

# SECTION E: FINDINGS REGISTER

| ID | Category | Finding | Severity | Resolution |
|---|---|---|---|---|
| ST-OPP-01 | Philosophical | Mending categorically immune to direct opposition | P1 | Derived; confirmed through scenario testing |
| ST-OPP-02 | Mechanical | Opposing engagement modifier (+TPS/2) philosophically necessary | P1 | Proposed in §C.1 Step 1 |
| ST-OPP-03 | Mechanical | Overwhelmed practitioners take knot strain, not degree-table consequences | P1 | Proposed in §C.1 Step 3 |
| ST-OPP-04 | Mechanical | Co-movement: Coherence per-practitioner; epistemic+actual once per compound event | P1 | Proposed in §C.1 Co-Movement |
| ST-OPP-05 | Mechanical | Shifting Object RS cost = worst single + 1, not sum of both | P1 | Proposed in §C.1 Step 3 |
| ST-OPP-06 | Mechanical | Winner degraded only if Overwhelming → Success; Success not degraded | P2 | Fix 1 |
| ST-OPP-07 | Mechanical | N-way ops: automatic Gap via lattice collapse | P1 | Proposed in §C.3 |
| ST-OPP-08 | Mechanical | FR vs FR "both fail" RS scales with operation scale | P2 | Proposed in §C.1 Step 3 |
| ST-OPP-09 | Mechanical | Repeated opposing ops on Shifting Object: advance deterioration tier | P2 | Proposed in §C.2 |
| ST-OPP-10 | Mechanical | Mass battle uses simplified contest | P2 | Proposed in §C.4 |
| ST-OPP-11 | Mechanical | Hybrid needs TPS-equivalent for BG factions | P2 | Proposed in §C.8 |
| ST-OPP-12 | Design | Pull/Weave Ob asymmetry is correct — do not equalize | P3 | Confirmed |
| ST-OPP-13 | Design | Cascade from single opposing op: RS −13 over 3 seasons if unaddressed | P3 | Confirmed — designed behavior |
| ST-OPP-14 | Combat | Practitioner may withdraw after hearing opposing declaration (forfeit round) | P3 | Note — not a gap, just a clarification |

---

# SECTION F: EDITORIAL ITEMS

| ID | Item | Priority | Blocked By |
|---|---|---|---|
| ED-OPP-01 | Approve Contested Intentionality procedure (§C.1 full procedure) | P1-BLOCKER | — |
| ED-OPP-02 | Confirm Mending immunity from direct opposition (§C.5) | P1-BLOCKER | — |
| ED-OPP-03 | Approve knot strain as consequence category (§C.1 Step 4) | P1-BLOCKER | ED-OPP-01 |
| ED-OPP-04 | Approve compound co-movement rule (§C.1 Co-Movement) | P1-BLOCKER | ED-OPP-01 |
| ED-OPP-05 | Approve N-way lattice collapse (§C.3) | P2 | ED-OPP-01 |
| ED-OPP-06 | Approve FR vs FR scaled consequences (§C.1 FR modifier) | P2 | ED-OPP-01 |
| ED-OPP-07 | Approve sustained opposition deterioration rule (§C.2 point 4) | P2 | ED-OPP-01 |
| ED-OPP-08 | Define Hybrid TPS-equivalent for BG factions (§C.8) | P2 | ED-OPP-01 |
| ED-OPP-09 | Approve BG opposing order resolution (§C.7) | P2 | ED-OPP-01 |
| ED-OPP-10 | Approve mass battle simplified contest (§C.4) | P2 | ED-OPP-01 |
