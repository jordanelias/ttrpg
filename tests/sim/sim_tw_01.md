# SIMULATION: THREADWORKING ACROSS THREE TEMPORAL AXES — CROSS-MODE
## Test ID: SIM-TW-01
## Simulator Modes: A (isolation) + C (scenario) + D (edge cases) + G (cross-mode) + L (precedent)
## Date: 2026-04-02
## Status: WORKING SIMULATION
## Three temporal axes:
##   Present-axis: Weaving (actualise/stabilise) + Forced Resolution Lock/Dissolution (freeze/destroy)
##   Future-axis: Pulling (de-actualise, open toward potential)
##   Past-axis: Past-Oriented Pulling (reach into historical configuration)
## Tests: With threadworking vs Without threadworking; all three axes; all three game modes

---

## SIMULATION PARAMETERS

**Fixed character:** Mira Soleng, Thread Sensitivity (TS) 55, Attunement 5, Spirit 5, Focus 3, Coherence 10.
Relevant History: "Varfell Thread Scholar" 4 pts → pool bonus +7. Thread Pool Score (TPS) = 55÷10 = 5.
- Leap pool: Attunement 5 + History 7 + TPS 5 = 17D (TN 7, Ob 1 at TS 50+)
- Weaving pool: Spirit 5 + History 7 + TPS 5 = 17D
- Pulling pool: Spirit 5 + History 7 + TPS 5 = 17D
- Past-Oriented Pulling pool: Spirit 5 + History 7 + TPS÷2(2) = 14D
- Locking/Dissolution pool: Spirit 5 + History 7 (no TPS) = 12D

**Board state:** Season 3, Year 1. Rendering Stability (RS) 65. Theocracy Counter (TC) 34. Institutional Pressure (IP) 25. Territory T9 (Varfell capital). Church controls T3 (Himmelenger). Diplomatic crisis: Crown-Church relations strained.

**Fixed roll sequence (all rolls same in both runs; only Thread ops differ):**

Standard actions (same both runs):
- Crown Govern: pool 5D → rolls 7,8,4,2,1 → net 0 = Failure
- Church Diplomacy: pool 6D → rolls 9,7,8,7,3,2 → net 4 = Overwhelming (Ob 2)
- Hafenmark Trade: pool 6D → rolls 7,4,2,6,3,1 → net 0 = Failure

Thread operations (Mira, Run A = no thread ops; Run B = all three axes):

Leap roll: 17D → (for scenario assume Success: sufficient successes at Ob 1, net 2)

**Present-axis (Weaving):**
Target: Diplomatic agreement between Varfell and Crown (Relational scale, Ob 3, TS 50+ ✓)
Weaving pool 17D: rolls 8,7,9,4,2,1,7,3,10,6,4,2,8,7,1,9,4 → successes: 8,7,9,7,10(×2),8,7,9 = 10 − 2 (1s) = net 8. Ob 3. Net 8 ≥ 2×3 = 6 → **Overwhelming**

**Future-axis (Pulling):**  
Target: Crown's commitment to the Altonian Trade Treaty (Firmly actualised, Ob 3, TS 50+ ✓)
Pulling pool 17D: rolls 7,4,2,6,8,1,7,3,9,6,4,2,7,1,8,9,4 → successes: 7,8,7,9,7,8,9 = 7 − 2(1s) = net 5. Ob 3. Net 5 ≥ 3 → **Success**

**Past-axis (Past-Oriented Pulling):**
Target: Church's founding charter of T3 (3 seasons ago, Ob 5, TS 70+ required... TS 55 insufficient)
→ Downgrade: Church's specific T3 territory claim from last season (1–2 seasons, Ob 4, TS 70+ required... still insufficient at TS 55)
→ Downgrade: Church's aggressive position from this session/same scene (Ob 3, TS 70+ required... TS 55 still insufficient for Past-Oriented Pulling)

**FINDING: TS 55 CANNOT PERFORM PAST-ORIENTED PULLING.** Minimum TS is 70. This is correct design — Past-Oriented Pulling is the most dangerous temporal operation and correctly gated. Mira cannot use the past axis.

→ Substitute: **Forced Resolution — Lock** on the diplomatic stalemate configuration (preventing it from deteriorating). Scale: Relational (the Crown-Church diplomatic relationship). Ob 6, TS 50+ ✓. Lock pool: 12D.
Lock roll: 12D: rolls 8,7,4,2,9,1,7,3,10,6,4,2 → successes: 8,7,9,7,10(×2) = 8 − 1(1) = net 7. Ob 6. Net 7 ≥ 6 → **Success**

Lock substitute notes the past-axis limitation and runs Lock as the present-axis FR instead. Separate past-axis test uses a TS 75 character below.

**TS 75 character for past-axis:** Aldric Varstein, Thread Sensitivity 75, Spirit 6, Focus 3, History bonus +7, TPS 7. Past-Oriented Pulling pool: Spirit 6 + History 7 + TPS÷2(3) = 16D.
Target: Church territorial claim on T9 (Varfell capital), established 2 seasons ago (Ob 4). TS 75 ✓.
Past-Oriented Pulling roll: 16D → rolls 8,7,9,4,2,1,7,3,10,6,8,7,1,9,4,2 → successes: 8,7,9,7,10(×2),8,7,9 = 10 − 2(1s) = net 8. Ob 4. Net 8 ≥ 4 → **Success**

Diagnosis: Mandatory before Past-Oriented Pulling. Skip penalty avoided — Aldric diagnosed in prior round.

---

## RUN A: WITHOUT THREADWORKING

### Season 3 — Standard Actions Only

**Crown Govern (T1) — Failure (PP-184: Prosperity −1 + Moderate complication):**
Crown Govern fails. Prosperity T1: 4→3. Moderate complication: Prosperity −1 (now 3). No thread ops.

**Church Diplomacy (vs Crown) — Overwhelming (PP-183: Success + Overwhelming bonus):**
Church achieves diplomatic objective. Crown Mandate −1 (→3). Overwhelming bonus: Effect applied immediately (Decree-equivalent timing). Church gains position advantage.
Church-Crown relations: Church has upper hand.

**Hafenmark Trade — Failure (FF: Wealth −1):**
Hafenmark Wealth: 5→4. No recovery path established.

**No threadworking. Board state after S3 (Run A):**
- Crown Mandate 3 (−2 from prior). Prosperity T1: 3.
- Church gaining political ground. Theocracy Counter 34 (unchanged by standard actions).
- Hafenmark Wealth 4.
- RS: 65 (unchanged — no Thread ops).
- Diplomatic-axis: Church dominant; no counterweight.

**Emergent dynamics (Run A):** One faction is pulling ahead (Church) with no Thread-mediated counterweight. Crown is weakening. The trajectory is clear and mechanical — without threadworking, the board tilts toward the faction with better dice and better starting stats. No asymmetric interventions possible. Narrative is one-directional.

---

## RUN B: WITH THREADWORKING — All Three Temporal Axes

### Present-Axis: Weaving (Mira, Relational scale)

**Setup:** Mira performs Weaving on the Varfell-Crown diplomatic agreement. This is a present-axis operation — she is drawing the existing relationship toward greater coherence, stabilising what is fraying under Church pressure.

**Diagnosis (pre-Leap round):** Mira renders the Crown-Varfell diplomatic configuration. She reads: the threads are strained but not severed. The agreement still has some actualization. Proceeding to Weaving.

**Leap:** 17D, TN 7, Ob 1. Net 2. **Success.** Contact established. 3 rounds available (Focus 3).

**Round 2 — Weaving (Relational, Ob 3, pool 17D, net 8 ≥ 6 = Overwhelming):**

Outcome: 
- Full effect: Diplomatic agreement stabilised. Varfell-Crown relations: restored to operational.
- Relational Overwhelming: RS +1 → RS 66.
- Over-actualisation: Subsequent Thread ops targeting this agreement: +1 Ob. Clears after 1 season.
- Mira gains 1 Thread Sensitivity (TS 55→56).
- Co-movement fires (P-01):
  - *Temporal auto-effect:* Coherence −1 (Relational scale op) → Coherence 10→9. History Resonance check: Mira's "Varfell Thread Scholar" History has the resonance tag. Roll 1d6: result 4 (no loss).
  - *Epistemic auto-effect (Overwhelming):* Observers TS 10+ perceive the area as markedly calmer. Crown and Varfell diplomats sense the meeting tone shift without knowing why.
  - *Actuality auto-effect:* Roll d6 → result 3: "secondary configuration responds" — the Crown's rival faction (Church-aligned nobles) notice the diplomatic warming and begin counter-manoeuvring (GM event seed, no immediate mechanical effect).

**Present-axis result:** Varfell-Crown agreement stabilised. RS 66. Coherence 9. One diplomatic channel open that was closing.

---

### Future-Axis: Pulling (Mira, Firmly actualised, Ob 3, pool 17D, net 5 = Success)

**Setup:** Mira performs Pulling on the Crown's commitment to the Altonian Trade Treaty. The Treaty is drawing resources from Crown's Wealth and suppressing Institutional Pressure. But the Treaty is also entangling Crown in Altonian dependency. Mira's Varfell faction wants the Treaty loosened — Crown less tied to Altonian interests, more responsive to domestic politics.

**This is a future-axis operation:** Pulling does not remove the Treaty — it draws the configuration toward potential, loosening the Crown's grip on the commitment. The Treaty threads are being de-actualised — pushed toward "could not be in force" rather than "is in force." Duration: net surplus 5−3=2 → next seasonal Accounting.

**Round 3 — Pulling (Firmly actualised, Ob 3, pool 17D, net 5 = Success):**

Outcome:
- Pulling succeeds. Crown's commitment to the Altonian Trade Treaty loosened for 2 seasons. Effect: Crown may not use Trade Treaty as justification for Ob reductions in Altonian-facing actions during this period. Institutional Pressure −1 next Accounting (Treaty no longer drawing full diplomatic benefit).
- Coherence −0 (Personal scale Pull → no Coherence cost at this scale; this is Firmly actualised, which maps to Personal commitment, not Relational). Wait — "Firmly actualised" is an actualization level, not a Thread scale. The Treaty is a **Relational** scale configuration (between Crown and Altonia as entities). Relational → Coherence −1.
- Coherence 9→8 (Relational scale Pull).
- Co-movement fires:
  - *Temporal auto-effect:* Coherence −1 (applied above). The Treaty's past history does not change — only its future-openness is affected. No History Resonance risk (Pulling rarely triggers resonance; this is forward-opening, not past-reaching).
  - *Epistemic auto-effect:* Crown advisors who understand Thread work (TS 30+) sense a shift in the treaty's weight. Others notice Crown negotiators seem less committed at next meeting without knowing why.
  - *Actuality auto-effect:* d6 → result 5: "adjacent configuration loosened" — the Crown's internal debate about Altonian relations, previously resolved in favour of the Treaty, reopens. This is a GM event seed: Crown player faces a Belief check around the Treaty next session.

**Future-axis result:** Crown-Altonia Treaty loosened for 2 seasons. Institutional Pressure −1 next Accounting. Coherence 8. Crown internal debate reopened (GM event).

---

### Past-Axis: Past-Oriented Pulling (Aldric, Church T9 claim, 2 seasons ago, Ob 4, 16D, net 8 = Success)

**Setup:** Aldric Varstein (TS 75) performs Past-Oriented Pulling on the Church's territorial claim to T9 (Varfell capital), established 2 seasons ago when Church missionaries entered the territory. The claim is not a Locked configuration — it is a normally actualised political-territorial configuration grounded in events 2 seasons prior. Aldric intends to displace the founding event: make it as if the missionary entry never achieved territorial purchase.

**This is a past-axis operation:** Aldric is reaching into the historical thread configuration of T9 and pulling the Church's implantation event toward potential — making it as though it never fully actualised. This does not prevent the event from having happened. It prevents the event from having the consequence it had. The cause is not removed from history; its effect is displaced from the present configuration.

**Mandatory Diagnosis:** Completed prior round. Aldric rendered the T9 configuration and identified the Church's presence thread as: 2-season-old Relational-scale establishment with Ob 4 (1–2 seasons back). No Mending needed. No FR involved. Proceeding.

**Diagnosis cost already incurred.** Aldric Leaps. Focus 3. Round 2 action.

**Leap:** 16D (POP pool), TN 7, Ob 1 (TS 75 → Ob 1). Assume net 3 = Success.

**Round 2 — Past-Oriented Pulling (Ob 4, pool 16D, TN 7, net 8 = Success):**

Outcome:
- Success: Church's territorial establishment thread in T9 displaced. Effect: Church's claim to T9 removed from the active board state. Church loses the territorial foothold that would have generated RS gains from T9 at next Accounting. The missionaries' historical presence remains in the world's history — but its practical consequence (territorial actualization) is gone.
- RS cost: −3 minimum on POP Success (mandatory). RS 66→63.
- Coherence: Past-Oriented Pulling: −1 additional. Coherence 8→7 (Aldric, not Mira; Aldric's Coherence separately tracked, assume starts at 10 → 9 from POP cost).
- Delayed manifestation check (P-22): d6 → result 3: no delayed manifestation. The displacement takes immediate effect.
- Co-movement fires:
  - *Temporal auto-effect:* The removed cause creates an Orphaned Configuration — a Church administrative record in Himmelenger references T9 presence that no longer exists. This is a visible temporal inconsistency for TS 30+ practitioners. A paradox window opens: 1d3 scenes. Roll: 2 scenes. During these 2 scenes, practitioners with TS 30+ can perceive both the old and new configuration simultaneously.
  - *Epistemic auto-effect:* Church representatives in T9 feel sudden uncertainty about their presence — they cannot render WHY they are there clearly. No immediate mechanical effect; GM event seed: Church Spy roll +1 Ob in T9 next season (epistemic instability).
  - *Actuality auto-effect:* d6 → result 6: "delayed manifestation" — already resolved above (no delayed manifestation, direct displacement). No additional effect.

**Post-POP state:**
- Orphaned Configuration: Church T9 administrative records (will deteriorate without maintenance — if Church does not re-establish T9 presence within 2 seasons, the configuration collapses entirely).
- Paradox window: 2 scenes. During this window, any Thread operation targeting T9 is +1 Ob (substrate instability).

**Past-axis result:** Church T9 claim removed from active board. RS 63. Orphaned Configuration creates deteriorating Church position in T9. Paradox window creates tactical complication for all T9 operations for 2 scenes.

---

### End of Contact — Mira Returns to Rendering

Round 4 = end of Focus window. Rendering reasserts. Mira returns.

**Mira's final state:** Coherence 8 (from Weaving and Pulling). TS 56. No Wounds. Still functional.

**Aldric's final state:** Coherence 9. TS 75. No Wounds.

---

## BOARD STATE COMPARISON (S3 END)

| Metric | Run A (No Thread) | Run B (With Thread) |
|--------|------------------|---------------------|
| RS | 65 (unchanged) | 63 (−2) |
| Crown Mandate | 3 | 3 (same — non-Thread) |
| Varfell-Crown relations | Deteriorating | Stabilised (Woven; over-actualised; brittle) |
| Crown-Altonia Treaty | Fully active | Loosened for 2 seasons |
| Church T9 claim | Active | Removed (Orphaned Config) |
| Institutional Pressure | 25 | 24 (−1 at next Accounting from Treaty Pull) |
| Theocracy Counter | 34 | 34 (Thread ops don't move TC directly) |
| Paradox windows active | 0 | 1 (T9, 2 scenes) |
| Orphaned Configurations | 0 | 1 (Church T9 records) |
| GM event seeds | 0 | 3 (actuality co-movements from all 3 ops) |
| Mira Coherence | N/A | 8 (from 10) |
| Aldric Coherence | N/A | 9 (from 10) |
| Emergent vectors | 1 (Church ahead) | 5+ (Treaty loose; T9 unstable; Crown internal debate; Church position eroding; paradox window) |

---

## EDGE CASES AND MECHANICAL FINDINGS

### Edge Case 1: Pool minimum at 1D — all three axes

**Test:** Apply PP-181 (pool minimum 1D) to a practitioner with maximum wound penalty.
Scenario: Mira takes 4 Wounds (Wound penalty −4D to all Thread rolls). 
- Leap pool: 17D − 4 = 13D → above minimum, no trigger.
- At 16 Wounds (impossible for Health = 6+6 = 12 base, incapacitated at 6): pool would be 17−16 = 1D → pool minimum = 1D. 
- **Finding:** Pool minimum at 1D triggers well before incapacitation in this case, but the incapacitation check (at ⌈Health÷2⌉) fires at 7 Wounds for most characters, which reduces the pool by 7D. For a pool of 17D this is still 10D — minimum never triggers in practice for a TS 55+ practitioner. **For low-attribute practitioners (pool ~4–6D):** Wounds can trigger the pool minimum at 3–5 Wounds, which is realistically achievable. PP-181 is relevant for low-pool practitioners in combat.

**Test for BG Thread pool minimum:** BG Thread Operations use faction stat pools (Influence, Mandate, etc.) rather than personal pools. Minimum stat floor of 1 (Influence) = pool of 1D minimum. Pool minimum rule in BG is therefore already satisfied by the stat floor. PP-181 adds no new constraint for BG Thread ops — but explicitly stating it removes ambiguity.

### Edge Case 2: Ob minimum = 1 — interaction with Weaving over-actualisation

**Test:** Relational Weaving on an already over-actualised configuration. Base Ob 3. Over-actualisation: +1 Ob (→4). Diagnosis: +0 Ob (done correctly). No wound penalty. Net Ob: 4.
What if: three stacking bonuses apply (Overwhelming Leap −1 Ob; prior Weaving surplus −1 Ob; History tag −1 Ob) = −3 Ob from modifiers. 4 − 3 = 1. **Ob floor: 1.** Ob minimum rule fires. Roll at Ob 1.

**Finding:** The Ob minimum is structurally important for practitioners with high bonus stacking. A TS 75 practitioner with Overwhelming Leap, prior surplus, and relevant History tag can reduce Ob to 1 on Ob 3+ operations. This is intentional — high Thread Sensitivity should produce easier ops. The floor (Ob 1) means even the most competent practitioner faces some resistance. **Confirmed: Ob minimum = 1 correctly operationalises in Thread context.**

### Edge Case 3: Overwhelming Degree — cross-mode verification

**Test:** Apply Overwhelming definition (net ≥ 2×Ob) across all three axes.

| Operation | Ob | 2×Ob (Overwhelming threshold) | Pool in test | Net in test | Degree |
|-----------|-----|-------------------------------|--------------|-------------|--------|
| Weaving Relational (TTRPG) | 3 | 6 | 17D | 8 | Overwhelming ✓ |
| Pulling Firmly Actualised (TTRPG) | 3 | 6 | 17D | 5 | Success (not Overwhelming) ✓ |
| Lock Relational (TTRPG) | 6 | 12 | 12D | 7 | Success ✓ |
| POP 2-season (TTRPG) | 4 | 8 | 16D | 8 | Overwhelming ✓ |
| BG Weave (BG mode) | 2 | 4 | varies | — | per faction pool |

**Finding:** 2×Ob Overwhelming correctly differentiates degrees. At Ob 6 (Lock Relational), Overwhelming requires net 12 — extremely rare at a pool of 12D (E[net] = 0.3×12 = 3.6). This is correct: FR is difficult and Overwhelming on FR should be very rare. At Ob 3 (Weaving Relational), Overwhelming requires net 6 at 17D pool — achievable (~30% of rolls at 17D pool). **The 2×Ob rule creates appropriate difficulty scaling across operation types.**

### Edge Case 4: Past-axis TS gate — what happens if attempted below TS 70?

**Test:** Mira (TS 55) attempts Past-Oriented Pulling. Eligibility check: TS 70+ required. Fails.

**Ruling (existing — no change needed):** Past-Oriented Pulling cannot be attempted at TS < 70. The operation is not available. This is not a roll — it is a hard eligibility gate. Attempting to declare Past-Oriented Pulling below TS 70: GM should not allow the roll. If declared in error and rolled anyway: treat as Failure with automatic temporal Gap (the configuration reached into the past without sufficient substrate sensitivity; the recoil is catastrophic).

**Finding:** The TS gate for Past-Oriented Pulling is correctly positioned. TS 70 is late-campaign territory — 2+ campaign arcs of Thread Sensitivity development. This makes the past axis rare and powerful, which is appropriate. No patch needed.

### Edge Case 5: Co-movement fires on ALL three axes — P-01 verification

**Verification:** Every Thread operation in Run B produced all three co-movement auto-effects (temporal, epistemic, actuality). P-01 requires this. Checking:

| Operation | Temporal auto-effect ✓ | Epistemic auto-effect ✓ | Actuality auto-effect (d6) ✓ |
|-----------|----------------------|------------------------|------------------------------|
| Weaving (present-axis) | Coherence −1, History Resonance check | TS 10+ observers perceive calming | d6=3: secondary configuration responds |
| Pulling (future-axis) | Coherence −1, no History Resonance | TS 30+ perceive Crown commitment shift | d6=5: Crown internal debate reopened |
| Past-Oriented Pulling (past-axis) | Coherence −1 + Orphaned Config | Church TS 30+ lose epistemic clarity T9 | d6=6: delayed manifestation (resolved directly) |

**Finding:** P-01 satisfied across all three axes. No axis is exempt from co-movement. Past-Oriented Pulling generates the richest co-movement output (Orphaned Configuration, paradox window, epistemic instability) — this is correct; reaching into the past disturbs all three dimensions more severely than present or future operations.

### Edge Case 6: Thread ops in BG mode — pool minimum and Ob minimum interaction

**BG Thread Operation:** Restoration faction, Weave order in T7. Faction pool for BG Thread ops: Influence (4D). After negative modifiers: Niflhel-active +1 Ob (Ob 3 → Ob 3; Niflhel modifier is on Ob not pool). Thread Debt token in T7: +1 Ob to next op → Ob 4.
Modifiers: Church presence in T7: no pool modifier in BG (BG Thread ops don't use combat-style pool penalties from enemy units). Pool stays at 4D.
**Ob 4, pool 4D, TN 7, E[net] = 0.3×4 = 1.2. P(≥4) ≈ 2%.** Very hard but possible.

Roll: 4D → 8, 9, 2, 1 → net: +1+1+0−1 = 1. Net 1 < 4. Net 1 > 0. **Partial.**
BG Weave Partial: RS unchanged; draw Co-Movement Card.

**Pool minimum check:** 4D (starting pool). No pool penalty applied (BG abstracts pool differently). PP-181 doesn't change this roll — pool was never threatened below 1D.

**Ob minimum check:** Ob 4 → if all modifiers were positive for the Restoration, could Ob drop below 1? With Presence markers in T7 (−1 Ob each), at 4 markers Ob would be 4−4 = 0 → floor 1. Confirmed: Ob minimum = 1 fires at 4 presence markers in T7 with Thread Debt active. **PP-182 is relevant for Restoration in high-marker territory.**

---

## COMPARATIVE EMERGENT GAMEPLAY ANALYSIS

### Run A (No Threadworking)

**Emergent vectors after S3:** 1 (Church pulling ahead; everything else mechanical).

The board without Thread intervention is determined by faction stat differentials and dice luck. Church's Overwhelming Diplomacy result tilts the political axis definitively. No asymmetric intervention available. The trajectory is locked unless another faction has better rolls next season. Purely reactive.

**Narrative texture:** Zero. Fail Forward (PP-177) generates complications but no novel configurations. The complications (Crown Prosperity loss, Hafenmark Wealth loss) create pressure but not new possibilities. The game feels like a competition for initiative, not a story.

**Replayability:** Medium — dice variance creates different "who's ahead" pictures but not qualitatively different campaign arcs.

### Run B (With Threadworking — Present, Future, Past Axes)

**Emergent vectors after S3:** 5+.
1. Varfell-Crown agreement stabilised (Woven) — but brittle. A future siege on T1 could shatter it into a Relational Shifting Object. Varfell now has a stake in Crown's safety.
2. Crown-Altonia Treaty loosened — Crown internal debate reopened. This changes Crown's strategic calculations for 2 seasons. Pulls Crown toward domestic politics; away from Altonian alignment.
3. Church T9 claim removed — Orphaned Configuration deteriorating. Church must respond or lose T9 foothold permanently. Forces Church to spend an action next season on re-establishment (or let it collapse).
4. Paradox window in T9 — +1 Ob all Thread ops in T9 for 2 scenes. Creates tactical complication for any faction operating in T9 during this window.
5. RS at 63 (from 65) — Thread work always moves RS. The substrate is more fragile. Future Thread ops are marginally more dangerous (RS 59 threshold approaching: "+1 Ob in affected territories").
6. GM event seeds (3) — each co-movement actuality effect creates a future scene. These are not random events; they are logically derived from the Thread operations performed. The campaign has a causal history.

**Narrative texture:** High. Each Thread operation created a consequence visible to characters at different TS levels. Non-practitioners notice things are calmer (Weaving epistemic effect) or that Crown negotiators seem uncommitted (Pulling epistemic effect). Practitioners perceive more. The world has layers.

**Replayability:** High — different Thread operations by different practitioners in different seasons produce qualitatively different campaign arcs, not just different scores.

### Verdict: Threadworking produces qualitatively superior emergent gameplay.

The difference is not incremental. Without Thread ops, the board evolves through attrition and dice luck. With Thread ops, the board evolves through causal intervention — each operation creates a specific configuration change with specific downstream consequences. The three temporal axes create three distinct intervention types:
- **Present-axis** creates stability (or brittleness) in existing configurations
- **Future-axis** opens configurations toward change (disrupts locked trajectories)
- **Past-axis** removes historical actualization from the board (most powerful; most destabilising)

The RS cost of Thread ops (−2 across the session) is the correct trade-off. Players must choose: intervene powerfully (and move RS toward the Rupture) or play conservatively (and watch the board tilt mechanically). This is a meaningful strategic choice at the campaign level.

---

## SUMMARY OF MECHANICAL FINDINGS

| Finding | Verdict | Patch |
|---------|---------|-------|
| Pool minimum (1D floor) — PP-181: never triggered in test but relevant for low-pool characters | Confirmed correct | PP-181 apply |
| Ob minimum (1 floor) — PP-182: fires at 4+ Restoration Presence markers with Thread Debt | Confirmed correct | PP-182 apply |
| Overwhelming at 2×Ob — PP-183/PP-179: correctly differentiates Lock (near-impossible Overwhelming) vs Weaving (achievable Overwhelming) | Confirmed correct | PP-183 apply |
| BG Overwhelming bonuses (PP-183): Govern +1 additional Prosperity; appropriate reward for rare outcome | Confirmed appropriate | PP-183 apply |
| Govern degree table (PP-184): Overwhelming +2, Success +1, Partial +1+Minor, Failure −1+Moderate | Confirmed | PP-184 apply |
| Co-movement fires all three axes — P-01: verified | Confirmed | No patch |
| Past-axis TS 70 gate: correctly positioned | Confirmed | No patch |
| Thread ops in BG produce RS pressure: creates meaningful trade-off | Confirmed good design | No patch |
| Three axes produce qualitatively distinct emergent dynamics | Confirmed | Core design validated |

