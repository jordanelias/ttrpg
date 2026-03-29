# THREADWEAVING v2.5 — STRESS TEST BATCH 4: COMBINATION SCENARIOS
**Date:** 2026-03-27  
**Method:** valoria-simulator Modes B/C/D  
**Focus:** Multi-mechanic intersections not yet tested in isolation — chains involving 3+ systems simultaneously  
**Model:** Sonnet 4.6  

---

## COMBINATION MATRIX — UNTESTED INTERSECTIONS

Priority intersections identified from coverage matrix gaps and dependency analysis:

| Chain | Systems | Why untested |
|---|---|---|
| C-01 | Residue + Collective + Coherence cap | Varfell resource in collective context |
| C-02 | Involuntary Leap + Threadcut presence + Mending | TS 90+ near a threadcut being during Gap work |
| C-03 | Past-Oriented Pull → Temporal Disjunction → Knot Crisis → Certainty collapse | Full temporal cascade |
| C-04 | Lock chronic → RS Fractured → spontaneous Gap → forced Mending → Coherence drain | Long-season degradation chain |
| C-05 | Devout character + Discovery Event + Dissolution witnessed → Dissonance Mark cascade | Church archetype under maximum pressure |
| C-06 | Opposing ops → Shifting Object → Brittleness shock → Relational Gap → Mending under combat | Full contested-ground collapse sequence |

---

## SIMULATION 17 — C-01: RESIDUE IN COLLECTIVE OPERATIONS (Mode B)

### Setup
Vaynard (Anchor, TS 80, Coherence 7) uses Potency 3 dissolution residue during a collective Territorial Weaving. Two helpers assist.

**Pool construction:**
- Anchor: Spirit 5 + History 3 + TPS 8 + residue 3D = 19D (residue dice explode 9–10)
- Helper 1: floor(Cog 4 ÷ 2) = +2D
- Helper 2: floor(Cog 3 ÷ 2) = +1D
- **Total: 22D** (3D exploding)

**Coherence cost:**
- Territorial scale: −1 base
- Residue use: −1 additional
- Cap (SIM3-F-04, confirmed): total −1
- Vaynard: Coherence 7→6

**Helpers' Coherence:** Each helper performed a Territorial operation. Each: Coherence −1.
- Helper 1: Coherence 8→7
- Helper 2: Coherence 6→5

**Finding: Cap applies to Anchor only, not helpers.** The cap is per-operation per-practitioner. Each helper's −1 is their own operation cost. Vaynard's residue use is Vaynard's event — helpers don't pay for his residue. ✓ Consistent.

**Residue dice interaction with lattice:**
Residue dice explode on 9–10. In a collective, these are Vaynard's dice — they explode normally. Helper dice do not explode (helpers don't use residue). No ambiguity. ✓

**Belief conflict + residue:**
If a helper has a tangential Belief conflict, their dice don't chain on 10. Vaynard's residue dice still explode on 9–10 (different trigger — explosion vs chaining). These are distinct mechanics. No interaction. ✓

**Finding: C-01 clean.** No new issues. Residue in collective is straightforward.

---

## SIMULATION 18 — C-02: INVOLUNTARY LEAP NEAR THREADCUT BEING DURING MENDING (Mode C)

### Setup

**Characters:**
- Practitioner (TS 92): Mending a Standard Gap (Ob 5). Pool: Att 5 + Focus 3 + TPS 9 = 17D.
- Threadcut Being (TS 70, present at Gap site): self-rendering, not hostile.

**State before:**
```
Practitioner — Coherence 8, Wounds 0, Focus 3
  Mending pool: 17D
  Mending Ob: 5 (Standard Gap) + §9.7 interference: TS÷20 cap +4 = but TS 70 ÷ 20 = 3.5 → +4 cap
  Wait: TS 70 ÷ 20 = 3.5, round up = 4. Cap is +4. So modifier = 4 (at cap).
  Actual Ob: 5 + 4 = 9.

RS: 48 | Threadcut Being: Rendering Strain 2, Health 6
```

**P1 FLAG (SIM4-F-01): §9.7 interaction with Mending Ob cap.**
The Ob 10 cap is stated in §9.7. Mending Ob 9 is within cap. But: Mending has its own Ob table capping at 8+ for Locked Zone borders. Standard Gap is Ob 5 baseline. With +4 interference, total = 9. This is within the absolute Ob 10 cap but above any single-operation Ob shown in the Mending table. Not mechanically broken — the cap exists — but the Mending table implies Ob 8+ is the maximum (Locked Zone borders). A Standard Gap Mending at Ob 9 due to threadcut interference is harder than Locked Zone Mending. The table expectation is violated.

P(≥9 net at 17D): ~12%

**Involuntary Leap trigger:** TS 92. Focus check TN 7 Ob 1 at start of scene (nearby Thread activity from Mending). P(fail) ≈ 16%.

**Scenario: Involuntary Leap fires before Mending attempt.**

Round 1: Involuntary Leap triggers. Rendering suspends 1 round.
- Co-movement: Coherence −1 (cap) → 8→7
- Actual d6: ambient effect
- Practitioner perceives threadcut being's self-rendering during involuntary contact — full originary exposure to a being that IS a permanent Leap. 

**New finding (SIM4-F-02, P2): Originary contact with a threadcut being during involuntary Leap is undefined.**
The practitioner's configuration encounters a threadcut being's configuration during undirected contact. The threadcut being's self-rendering is a permanent originary intentionality. The practitioner's involuntary contact is undirected originary intentionality. Two originary configurations meeting without direction.

Per §9.7: the being's interference adds Ob to Mending. But the interference applies to directed operations. During involuntary contact (no operation), the interference Ob doesn't apply — there's no operation to penalise.

What does apply: the practitioner perceives something during the involuntary contact. At TS 92, they perceive the being's self-rendering at full depth — "the continuous work that holds it in place." This is an involuntary Diagnosis of the being, essentially. Does this count as confrontation with the being (TS growth check)? The TS growth rules require "held confrontation." An involuntary 1-round contact probably doesn't qualify. P3 judgment call — no rule violation.

Round 2: Voluntary extension attempt (if pursued). Ob: Leap base 1 + no Diagnosis +2 + extension +1 = Ob 4. Pool: Att 5 + History 2 + TPS 9 = 16D. P(Ob 4) ≈ 98%. Succeeds.

Mending proceeds with +4 interference Ob: Ob 9. P(17D): ~12%.

**Most likely outcome: Failure.**
- Gap unchanged. Coherence −1 → 7→6. RS −2 → 48→46. No Wound (patched).

**Finding: Combined chain produces near-certain failure.** A TS 92 practitioner attempting to Mend a Standard Gap while a TS 70 threadcut being is present will almost certainly fail (12%). The scenario is realistic (threadcut being present at a Gap site — plausible in Southernmost expedition). The mechanical result: practitioners cannot effectively Mend in the presence of high-TS threadcut beings. Resolution per §9.6: the being must move away, or be engaged via communication/outlasting, before Mending can proceed.

**Design confirmation:** The combination correctly prices the scenario. ✓ But see SIM4-F-01 above — the Ob stack exceeds the implicit Mending table ceiling.

---

## SIMULATION 19 — C-03: FULL TEMPORAL CASCADE (Mode C)

### Setup: Past-Oriented Pull → Temporal Disjunction → Knot Crisis → Certainty collapse

**Character:** Maret Uln (Spirit 4, Coherence 7, Wounds 0)  
**Operation:** Past-Oriented Pull on a 3-season-old event (death of a close ally — also a named Knot)  
**Pool (Option B):** Spirit 4 + History 2 + TPS÷2 3 = 9D  
**Ob:** 5 (3–5 seasons) + 1 (RS Fragile) = 6  
P(≥6 net at 9D): ~15%

**Scenario A: Pull succeeds (15% chance)**

Physical fact displaced: ally death removed. Ally alive.

Per §9.10 (P-21):
- Physical-fact Knot strain (death as external event) → reverts
- Experience Knot strain (Maret witnessed death, called Knot, Composure buffer used) → persists
- Net: Knot reads not-in-Crisis but Maret has vivid Crisis memory

Certainty check: Spirit TN 7 Ob 1. P(pass at Spirit 4) ≈ 80%.
- Pass: Maret absorbs the disjunction. Coherence −1 (Pull, Relational temporal) = −1.
- Fail (20%): Certainty −1. Coherence −1.

**Scenario A cascade (if Certainty check fails):**
Maret at Certainty (Spirit 4) − 1 = 3 remaining. At Coherence 7→6.

Other witnesses: ally is alive. They have no Certainty check (no mechanic per SIM2-F-05, still open).
Social consequence: witness says "but I was at the funeral." Maret says "they're alive." Both are correct. Temporal Disjunction in a social scene.

**P2 (SIM2-F-05 confirmed again):** No witness Certainty rule. The social fracture has no mechanical grounding for non-practitioner characters.

**Scenario B: Pull fails (85% chance)**

Failure: snap-back. Wounds 0→1. RS −3 → 48→45 (still Fragile). Coherence −1 → 7→6.
Fraying Bane: temporal Gap forms.

**Now Maret has:** Wounds 1, Coherence 6, a temporal Gap forming, and the ally is still dead.

**Knot interaction with failure:** The Knot representing the dead ally is still in Crisis (or at elevated strain). Maret's failed attempt to undo the death while the Knot is in Crisis — what happens?

**P2 FLAG (SIM4-F-03): No rule for attempting Past-Oriented Pulling on a Knot-Crisis-active event.**
The attempt itself — reaching into the timeline to undo a death that has produced an active Knot Crisis — has no mechanic. The Knot Crisis is a current state caused by the past event. If the Pull had succeeded, the Crisis would partially revert (physical-fact strain). But the attempt itself: does the active Knot Crisis affect the Ob? Does a failed attempt worsen the Crisis?

Proposed: active Knot Crisis from the target event adds +1 Ob to Past-Oriented Pulling (the living relational weight of the grief makes the temporal thread harder to access — it's more firmly actualised by ongoing relational consequence). Flag as **SIM4-F-03 (P2)**.

**Full cascade on failure:**
```
State after failed Pull + Fraying Bane:
Maret — Wounds 1, Coherence 6, Knot in Crisis (unchanged)
RS: 45 | Temporal Gap: forming
Ally: still dead
```

Maret's contact window: if Focus 3, she has 1 operation remaining.

Options: Mend the Gap (Mending pool 14D vs Ob 5 standard + Ob modifiers). Or retreat.

Mending after failed Past-Oriented Pull: sequential failure +1 Ob + Wound +1 Ob = Ob 7. P(14D): ~30%. Maret's contact window likely ends with another failure or abort.

**Finding: The full temporal cascade is punishing and realistic.** A practitioner attempting to undo a deeply personal loss (active Knot Crisis, Relational+ resonance) faces near-impossible Ob stacks and probable failure cascades. The system correctly prices emotional ambition. ✓

---

## SIMULATION 20 — C-04: LOCK CHRONIC → RS FRACTURED → SPONTANEOUS GAP → MENDING DRAIN (Mode C)

### Seasonal Accounting Chain (5 seasons)

**Setup:** One Territorial Lock placed in Season 1, never removed. Campaign RS starts at 55.

```
Season 1:
Lock placed: RS −1 (immediate, patched from −2)
Winter drift: RS −1
Other ops (2 Partial): RS −2
Season end RS: 55 − 4 = 51

Season 2:
Lock chronic (S2, 1 season): no drift yet (drift begins S2→S3)
Winter: −1. Ops: −2.
RS: 51 − 3 = 48

Season 3:
Lock chronic drift begins (2 seasons old): RS −1
Winter: −1. Ops: −2. Gap persists from prior scene: −4.
RS: 48 − 8 = 40 → Fragile threshold (was 42, now 40 — within Fragile)

Season 4:
Lock chronic (3 seasons, now −1/season still):  −1
Fragile: spontaneous Shifting Object (1 per season at Accounting)
Winter: −1. Ops (harder now, +1 Ob everywhere): −2.
Mending attempt (to prevent Shifting Object deteriorating): Mending success → RS +1
Net: 40 − 1 − 1 − 2 + 1 = 37 → crosses into FRACTURED

Season 5:
Lock chronic (4 seasons, crosses to −2/season tier): RS −2
Fractured: spontaneous Gap risk (1d10: on 1-2 = Gap forms, 20% chance)
Gap if formed: RS −4 per season it persists
Winter: −1. Ops: −3 (Fractured zone, +1 Ob, more failures).
Mending the spontaneous Gap: 1 attempt. P(Standard Gap, 14D) = ~58%. 
  Success: Gap closed, RS +1. Net season: −2 −1 −3 +1 = −5. RS 37→32.
  Failure (42%): Gap persists. Net: −2 −1 −3 −4 (Gap persisting next season) = −10. RS 37→27.
```

**Finding: Without Lock removal, RS hits 27–32 by Season 5.** The Rupture (RS 0) is 5–7 more seasons away depending on Mending success rate. A campaign that doesn't actively remove Locks and Mend Gaps reaches Rupture in ~10–12 seasons. This is the designed trajectory — but it requires the table to understand the math.

**Mending drain on practitioners:**
Each Mending attempt: Coherence −1. 1–2 Mendings per season = Coherence −1 to −2 per season. A dedicated Mender hits Coherence 0 in 10 seasons without recovery. The resource required to slow RS degradation costs the practitioners responsible for slowing it.

**New finding (SIM4-F-04, P2): No rule for coordinated seasonal Mending between multiple practitioners.**
If two practitioners each Mend once per season, do their RS gains stack? (2× RS +1 per season = RS +2/season?) The rules say each Mending adds RS +1 on success. Two successful Mendings = RS +2. Appears to stack — but no explicit statement. If stacking is correct, a group of dedicated Menders could offset Lock drift and winter degradation, making the campaign sustainable. This is probably intended (Revolution's Community Mending strategy) but should be explicit.

---

## SIMULATION 21 — C-05: DEVOUT CHARACTER UNDER MAXIMUM PRESSURE (Mode C)

### Setup: Church Archetype — Himlensendt

**Character:** Himlensendt (Devout Constraint active, TC driver, zero TS awareness)  
**Scenario:** Himlensendt witnesses a Dissolution attempt that produces a Gap and Monstrous Incursion. Maximum Thread exposure for a Devout character.

**State before:**
```
Himlensendt — Spirit 4, Certainty 4 (Spirit score), Coherence N/A (not a practitioner)
  Devout Constraint: active (essentialist theological Belief)
  TS: 0 (inert — no Thread perception)
  TC: 8 (institutional expansion)
```

**Events:**

**1. Dissolution attempt nearby:**
Himlensendt perceives nothing (TS 0). The Dissolution completes. Gap forms.

**2. Monstrous Incursion (Gap failure consequence):**
Himlensendt witnesses a monstrous entity. Certainty check: Spirit TN 7 Ob 1.
Per §4.4 (character sheet): "Devout characters receive +2D on Certainty-resist checks against monstrous encounters."
At Spirit 4 + 2D bonus = 6D: P(≥1 net) ≈ 92%.

**Most likely: Certainty intact.** Devout framework absorbs the shock. ✓

**3. Devout Constraint interaction:**
The monstrous entity is a Gap incursion — a rendering failure. Himlensendt's theology frames this as divine intervention, demonic manifestation, or test of faith. The Devout Constraint forecloses TS growth (the theological framework prevents the perceptual shift that produces sensitivity). Himlensendt processes the encounter without it producing TS growth. ✓

**4. Discovery Event bypass:**
If the Dissolution were directly performed on Himlensendt (non-consensual Thread work on a sentient being), a Discovery Event would be triggered. Spirit check + Belief bonus, TN 7, Ob 1.
- Success: Himlensendt holds the confrontation. +5 TS. Immediately triggers Theological Dissonance Event.
  - Dissonance Event: Spirit TN 7 Ob 1. At Spirit 4 + Devout bonus: P(pass) ≈ 86%.
  - Pass: framework holds. Constraint re-engages. Certainty −1.
  - Fail (14%): Dissonance Mark 1.

**Dissonance cascade test:**
If Himlensendt accumulates 3 Dissonance Marks: Devout Constraint collapses.

Probability of 3 marks from 3 consecutive Discovery Events:
Each event: 14% chance of a mark (assuming Spirit 4 each time).
P(3 marks from 3 events): 0.14³ ≈ 0.3%. Near-impossible through random chance.

To accumulate 3 marks reliably: ~21+ Discovery Events needed (expected marks per event = 0.14; 3 marks ÷ 0.14 ≈ 21 events).

**Finding: Devout Constraint is extremely robust.** A committed Devout character almost never reaches Constraint collapse through normal play. This is correct design — the Church's theological framework is genuinely difficult to crack. ✓

**Finding (SIM4-F-05, P3): No escalating difficulty for repeated Discovery Events on a Devout character.** The 21st Discovery Event has the same Ob as the first. A character who has repeatedly survived confrontations with Thread reality never accumulates Dissonance faster. This may be intentional (faith is not worn down by repetition) or an oversight. Noted as P3 — not breaking.

---

## SIMULATION 22 — C-06: FULL CONTESTED-GROUND COLLAPSE (Mode C)

### Setup: Opposing Ops → Shifting Object → Brittleness Shock → Relational Gap → Combat Mending

**Characters:**
- Practitioner A (Crown, Spirit 5, TS 65, Coherence 8): Weaving a diplomatic alliance (Relational)
- Practitioner B (Revolution, Spirit 4, TS 60, Coherence 7): Pulling the same configuration

Both in contact simultaneously. Opposing intentionalities per §9.13.

**Pools:**
- A: Spirit 5 + History 3 + TPS 6 = 14D vs Ob 3 (Relational Weaving)
- B: Spirit 4 + History 2 + TPS 6 = 12D vs Ob 3 (Relational Pull, normally actualised)

P(A succeeds) ≈ 96%  
P(B succeeds) ≈ 92%  
P(Both succeed) ≈ 0.96 × 0.92 = 88% → **Relational Shifting Object**  
P(A only) ≈ 8%  
P(B only) ≈ 4%  
P(Both fail) ≈ 0.3%

**Most likely (88%): Relational Shifting Object forms.**

Both practitioners: Coherence −1 additional (§9.13) + Relational scale −1 = capped at −1 each.
- A: Coherence 8→7 (Dissonant)
- B: Coherence 7→6

RS: both operations produced contradictory direction. Per §9.13 both succeed: no explicit RS cost listed.

**P2 FLAG (SIM4-F-06): §9.13 "both succeed" outcome has no RS cost.**
Both-succeed produces a Shifting Object. The degree tables for Weaving and Pulling both list RS costs on Partial/Failure. On Success, no RS cost. But the §9.13 both-succeed outcome is a degraded result (Shifting Object, not intended by either). Should it carry an RS cost?

Proposed: both-succeed opposing outcome costs RS −1 (substrate strained by contradictory successful directions — the thread is being pulled two ways at once at full force). This is lower than a Partial (−1 to −2) but acknowledges the substrate damage. Flag as SIM4-F-06 (P2).

**Season 1: Relational Shifting Object persists. Neither faction Mends.**

Season 2: Relational Shifting Object deteriorates to Relational Gap (per §9.5: 1d3 seasons, assume 1).

**Relational Gap effect:**
Per SIM2-F-10 (still open — Relational Gap mechanics undefined). For this simulation: assume Relational Gap = diplomatic relations fully severed. No treaties possible between Crown and Revolution until Mended.

**Mending the Relational Gap under combat pressure:**

Practitioner A attempts Mending. Combat ongoing (Revolution forces in the zone).

Pool: Att 4 + Focus 3 + TPS 6 = 13D  
Ob: Standard Gap (5) + RS Fractured zone (+1) + combat pressure (+1 Ob, Wound taken) = Ob 7  
P(≥7 net at 13D): ~22%

**Sequential failure cascade:**
- Failure 1: Gap unchanged. RS −2. Coherence −1.
- A now Wounds 1, Coherence 6.
- Retry: Ob 7 + sequential +1 + Wound +1 = Ob 9. P(13D): ~2%. Effectively impossible.

**Finding: Once a contested Relational Gap forms in an active conflict zone, it is extremely difficult to Mend.** The combination of base Ob, RS degradation, and combat pressure stacks to near-impossible territory. This requires either a ceasefire (remove combat Ob), a specialist Mender (larger pool), or collective operation.

**Finding: This chain is the primary RS death spiral path in active faction conflicts.** Contested Thread operations → Shifting Objects → Gaps → RS degradation → harder Mending → more failures → more RS degradation. The cycle is self-reinforcing. ✓ Design confirmed — the system punishes Thread-as-weapon use. But players need to understand this cycle explicitly.

**SIM4-F-07 (P2): No explicit warning about the contested-operation RS spiral.** A GM sidebar noting this cycle would prevent player surprise when their faction conflict produces exponential RS damage. Add to §9.13.

---

## AGGREGATE FINDINGS — BATCH 4

| ID | Category | Description | Severity | Frequency |
|---|---|---|---|---|
| SIM4-F-01 | Incoherence | §9.7 interference can push Mending Ob above the implicit table ceiling (8+); Standard Gap becomes harder than Locked Zone Mending | P1 | Low |
| SIM4-F-02 | Ambiguity | Originary contact between involuntary Leap practitioner and threadcut being: undefined interaction | P2 | Low |
| SIM4-F-03 | Gap | No rule for active Knot Crisis affecting Past-Oriented Pull Ob on the Crisis-causing event | P2 | Medium |
| SIM4-F-04 | Gap | No explicit statement that multiple Mending successes per season stack their RS gains | P2 | Medium |
| SIM4-F-05 | Incoherence | Devout character Discovery Event Ob never escalates across repeated exposures | P3 | Low |
| SIM4-F-06 | Gap | §9.13 both-succeed opposing outcome: no RS cost specified | P2 | Medium |
| SIM4-F-07 | Gap | No GM sidebar warning about contested-operation RS death spiral | P2 | High |

**P1: 1 (SIM4-F-01)**  
**P2: 5**  
**P3: 1**

---

## CROSS-BATCH OPEN FINDINGS SUMMARY

After 4 batches, open items requiring action:

**P1 (3 total):**
- SIM4-F-01: §9.7 + Mending Ob ceiling conflict
- SIM2-F-03: ✓ Patched (recency table)
- SIM2-F-09: ✓ Patched (concealment)

**P2 (12 open):**
- SIM2-F-01 (collective Focus halving Coherence)
- SIM2-F-02 (Past-Oriented Pull TPS exclusion — ✓ patched to Option B)
- SIM2-F-05 (witness Certainty checks for temporal displacement)
- SIM2-F-08 (involuntary contact as partial Diagnosis)
- SIM2-F-10 (Relational/Territorial/Structural Gap mechanics)
- SIM2-F-11 (cross-phase opposing ops timing)
- SIM3-F-02 (Crown no TS 70+ practitioner)
- SIM3-F-03 (Hafenmark no Thread entry)
- SIM3-F-06 (political NPC involuntary Leap social consequence)
- SIM4-F-02 (threadcut + involuntary Leap contact)
- SIM4-F-03 (Knot Crisis + Past-Oriented Pull)
- SIM4-F-04 (seasonal Mending stacking)
- SIM4-F-06 (both-succeed opposing op RS cost)
- SIM4-F-07 (contested-op spiral sidebar)

**P3 (3 open):**
- SIM2-F-06 (RS success > failure cost note)
- SIM4-F-05 (Devout escalation)
- SIM3-F-05 (non-practitioner residue)
