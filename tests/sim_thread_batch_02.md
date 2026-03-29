# THREADWEAVING v2.5 — STRESS TEST BATCH 2
**Date:** 2026-03-27  
**Method:** valoria-simulator Modes B/C/D  
**Mechanics under test:** Collective Operations · Past-Oriented Pulling · Involuntary Leap (full scenario) · Opposing Simultaneous Operations  
**Model:** Sonnet 4.6  

---

## SIMULATION 8 — COLLECTIVE OPERATIONS (Mode B + C)

### 8.1 Pool Construction

**Anchor:** Highest TS practitioner. Full operation pool (Spirit + History + TPS).  
**Helper contribution:** floor(Cognition ÷ 2) bonus dice each.  
**Constraints:** No Forking. Belief conflicts affect chaining. Lattice fracture at <50% pool.

**Representative collective: 3 practitioners**

| Role | Spirit | Cognition | History | TS | TPS | Individual Pool | Contribution |
|---|---|---|---|---|---|---|---|
| Anchor (Vaynard) | 5 | 4 | 3 | 80 | 8 | 16D | — |
| Helper 1 (TS 60) | 4 | 4 | 2 | 60 | 6 | 12D | +2D |
| Helper 2 (TS 50) | 3 | 3 | 1 | 50 | 5 | 9D | +1D |

**Collective pool: 16 + 2 + 1 = 19D**

### 8.2 Scenario: Collective Weaving on Territorial Configuration

**Setup:** Three practitioners attempt to stabilise a Territorial configuration (Weaving, Ob 4) — raising a faction's Stability by 1. Vaynard anchors; two helpers assist.

**State before:**
```
Practitioners
Vaynard — Spirit 5, Cognition 4, Coherence 8, Wounds 0
  Pool: 16D base + 3D helper contributions = 19D
Helper 1 — Coherence 7, Wounds 0
Helper 2 — Coherence 9, Wounds 1

Tracks
RS: 55 | TC: 3 | IP: 12

Active Conditions: none
```

**Action: Collective Territorial Weaving**
Pool: 19D, TN 7, Ob 4  
P(≥4 net at TN7): ~88% at 19D (expected net ≈ 6.3)  
Expected net successes: 6.3  
Most likely outcome: **Success** (surplus ~2.3 → standard duration Pull equivalent, but this is Weaving so: full effect)

**Most likely outcome: Success**

Co-movement: Territorial scale  
- Temporal auto-effect: Coherence −1 each (Vaynard, Helper 1, Helper 2) — all at Territorial scale  
- Epistemic auto-effect: Settling perceived by TS 10+ observers  
- Actual d6: roll required (narrative)

**State delta:**
```
Vaynard: Coherence 8→7 (Dissonant — GM names this per §3.3 protocol)
Helper 1: Coherence 7→6
Helper 2: Coherence 9→8
RS: unchanged (Weaving Success at Territorial — no RS change on success)
Over-actualisation: +1 Ob to subsequent Thread ops targeting this Stability config
Target faction: Stability +1
```

**Finding: Design confirmed.** Collective Territorial Weaving is viable and reliable (88% success). The Coherence cost distributes across all practitioners — each pays −1, not just the Anchor. This is correct per §3.2 (each practitioner performed an operation at Territorial scale).

### 8.3 Lattice Fracture Test

**Setup:** Same collective. Helper 2 takes a Wound mid-contact (before the roll), rendering reasserts. Pool drops from 19D to 17D.

**Threshold check:** Half of Anchor's solo pool = 16D ÷ 2 = 8D. Remaining pool (17D) is above 8D. No lattice fracture penalty. ✓

**Test: Helper 1 also drops (Wound).** Pool: 16D. Still above 8D. No penalty.

**Test: Both helpers drop.** Pool: 16D. Equals 8D threshold exactly.  
**P3 FLAG: Threshold is "drops below half" — at exactly half, no penalty fires.** This is correct per the text ("below half"), but worth confirming: a solo Anchor with zero helpers is fine; only sub-50% triggers the +1 Ob.

**Extreme test: Anchor pool halved by environmental effect (Focus Halving, P-11).** Focus 3 → halved → Focus 1 = zero operations. The collective achieves Leap but cannot perform any operation. Each practitioner still pays the Coherence cost for the Leap (scale of the intended operation). 

**P2 FLAG: Coherence cost when collective achieves contact but performs zero operations.** The §3.2 scale-based cost fires on operations, not on the Leap itself. If Focus halving prevents all operations, does Coherence still cost?  
**Ruling from text:** Coherence costs are listed as "operation" costs. A Leap without operations = no operation = no scale-based Coherence cost. However: the Leap itself is at minimum a Relational-scale commitment (collective Leap). Ambiguous.  
**Proposed resolution:** If contact is established but zero operations occur (Focus 1 after halving), Coherence loss = 0. The practitioner experienced suspension but performed no Thread interaction at scale. Flag as **SIM2-F-01 (P2)**.

### 8.4 Belief Conflict in Collective

**Setup:** Anchor (Vaynard) intends to Weave a diplomatic agreement (Relational scale). Helper has Belief: "The Church's authority must be preserved." The operation would undermine Church interests — tangential conflict.

**Per §2.5:** Tangential conflict = helper's dice cannot chain on 10.

**Effect on pool:**  
- Helper contributes floor(Cognition ÷ 2) = 2D, but these dice cannot chain.  
- Expected contribution from non-chaining dice: 2 × 0.37 (success but no chain) ≈ 0.74 net vs standard 2 × 0.40 ≈ 0.80 net.  
- Practical difference: negligible (~0.06 expected net successes). The penalty is flavourful but mechanically minor.

**Direct opposition test:** Helper's Belief directly opposes the operation. Pre-Leap Belief check: Spirit TN 7 Ob 1.  
At Spirit 3: P(≥1 net) ≈ ~66%. Helper fails ~34% of the time → drops out before Leap.  
Pool if dropped: 17D instead of 19D. P(Success at Ob 4): ~86% vs ~88%. Also negligible.

**Finding: P3 — Belief conflict mechanics are flavourful but mechanically minimal.** The system correctly prioritises narrative over mechanical weight here. ✓

---

## SIMULATION 9 — PAST-ORIENTED PULLING (Mode C — Full Scenario)

### 9.1 Scenario Setup

**Character:** Maret Uln (Practitioner, TS 75)  
**Operation:** Past-Oriented Pull on a territorial event — specifically, displacing the physical facts of a recent battle (2 seasons ago) that killed a key NPC.

**Eligibility check:**
- TS 75 ✓ (requires 70+)
- RS current: 52 ✓ (requires ≤60)
- Diagnosis: mandatory — performed prior round ✓

**State before:**
```
Maret Uln — Spirit 4, Coherence 7, Wounds 0, TPS 7
  Pool: Spirit 4 + History 2 + TPS 7 = 13D (Note: Past-Oriented Pulling uses Spirit + History only, no TPS)
  Corrected pool: Spirit 4 + History 2 = 6D

RS: 52 | TC: 4 | IP: 18
Knots: 3 active
Target thread: battle-event, 2 seasons recency
```

**P2 FLAG: TPS exclusion from Past-Oriented Pulling pool.**  
Per §2.4: "Pool: Spirit + relevant History bonus" — no TPS listed. Every other operation includes TPS. The exclusion is presumably intentional (Past-Oriented Pulling engages temporal depth, not Thread sensitivity) but is never explained. A TS 100 practitioner and a TS 30 practitioner have the same pool for this operation if their Spirit and Histories are equal. This seems wrong. Flag as **SIM2-F-02 (P2)** — add design rationale note or include TPS at reduced weight (÷2?).

**Proceeding with text as written: pool = 6D.**

### 9.2 Operation Resolution

**Ob by recency (2 seasons):** Per §2.4 reference to existing mechanics — "Ob by recency" retained. Assuming: recent (within season) = Ob 3; 1–2 seasons = Ob 4; 3–5 seasons = Ob 5; older = Ob 6. (Standard recency table — not fully reproduced in v2.5; flagging below.)

**P2 FLAG: Recency Ob table not reproduced in v2.5.** §2.4 says "All existing mechanics (Ob by recency, degree table, TT/RS consequences, Fraying Bane) retained with RS replacing TT throughout." But the actual Ob table is not in this document. A GM running only v2.5 cannot find the recency Ob values. Flag as **SIM2-F-03 (P1)** — must be reproduced or explicitly cross-referenced to a specific document location.

**Using assumed Ob 4 (2 seasons):**  
Pool: 6D, TN 7, Ob 4  
P(≥4 net at 6D): ~10%  
Expected net: ~2.0  
Most likely outcome: **Failure** (~70% of the time)

**This is a near-impossible operation at minimum viable TS.** A TS 70 practitioner with Spirit 4 and 2 History dice has a ~10% success rate on a 2-season-old event. 

**P1 FLAG (SIM2-F-04): Past-Oriented Pulling is effectively inaccessible without heavy Spirit + History investment.** The pool formula (Spirit + History only, no TPS) means TS matters only for eligibility, not for execution. A TS 90 practitioner with Spirit 3 and no relevant History has a smaller pool than a TS 30 practitioner with Spirit 5 and 3 History dice — but the TS 30 practitioner can't even attempt it. The operation is gated by TS but powered by Spirit/History, creating a disconnect where TS does not improve your ability at the operation it unlocks.

**At Spirit 6, History 4 (elite practitioner):** Pool = 10D. P(Ob 4) ≈ 55%. Viable but risky.  
**At Spirit 5, History 3:** Pool = 8D. P(Ob 4) ≈ 40%. Marginal.

### 9.3 Failure Consequences

**Failure:** Snap-back. 1 Wound (armour does not apply). RS −2. Coherence −1 (cap). Fraying Bane (from retained mechanics — assume: additional temporal consequence, GM determines).

**State delta on failure:**
```
Maret Uln: Wounds 0→1, Coherence 7→6
RS: 52→50
TD: increases (Temporal Disjunction — amount from retained mechanics)
```

**Cascading failure test:** Maret Uln (now Wounds 1) attempts again same contact window.  
- Sequential failure penalty: +1 Ob (cumulative) → Ob now 5
- Wound penalty: +1 Ob → Ob 6
- Pool: 6D vs Ob 6. P(Success): ~2%
- This is auto-failure territory. A failed Past-Oriented Pull cannot be meaningfully retried within the same contact window.

**Finding: Design confirmed.** Past-Oriented Pulling should not be attempted without a large Spirit/History pool. The sequential failure penalty makes retry functionally impossible. ✓

### 9.4 P-21 State Reversion Test (Mode B)

**Setup:** Past-Oriented Pull succeeds. Battle is displaced — the NPC death is a physical fact removed. Per §9.10:
- Physical-fact-triggered Knot strain reverts (the death didn't happen)
- Experience-triggered Knot strain persists (Maret remembers the death)

**State after successful pull:**
```
NPC: alive (physical fact restored)
Maret's Knot to NPC: strain from "external event" (death) → reverts
Maret's Knot to NPC: strain from "witnessing death" (experience) → persists
Net: Knot reads as not-in-Crisis but character vividly remembers the Crisis
```

**Certainty check triggered:** Spirit TN 7 Ob 1.  
At Spirit 4: P(pass) ≈ 80%. On failure: Certainty −1.

**Temporal Disjunction chain:**  
Other characters who witnessed the battle also remember it. They have no mechanical Knot strain reverting (they're not the operating practitioner). But the NPC is alive.

**P2 FLAG (SIM2-F-05): Social consequences of witnessed temporal displacement not addressed.**  
Other characters know the NPC died. Now they're alive. This should produce Certainty checks or equivalent for any witness — but no rule specifies this. The mechanical gap: who rolls the Certainty check? Only the operating practitioner per §9.10. All other witnesses experience a rendering failure (the world doesn't match their memory) with no mechanical consequence. Proposed: witnesses with TS 0–29 may make a Spirit check or ignore it (they'll rationalise); TS 30+ witnesses perceive the temporal displacement and make a Certainty check.

### 9.5 RS Consequences

**RS −3 minimum** on any Past-Oriented Pulling (per §5.2).  
On Success with surplus 2+: RS −3 still (minimum floor, not variable).

**P3 FLAG (SIM2-F-06): RS cost asymmetry.** Successful Past-Oriented Pulling costs RS −3 regardless of outcome quality. Failed Pulling costs RS −2 (snap-back). Success is more expensive to the substrate than failure. This is philosophically coherent (a successful displacement damages the world more than a failed attempt) but counterintuitive to players. Worth a design note.

---

## SIMULATION 10 — INVOLUNTARY LEAP FULL SCENARIO (Mode C)

### 10.1 Setup

**Character:** Almud (TS 95, Resonant range)  
**Situation:** Political meeting. A second practitioner (TS 60) performs a Relational Weaving in the same room — binding a diplomatic agreement.

**Involuntary Leap trigger:** TS 90–100. Focus check TN 7 Ob 1.  
Almud's Focus: 3.  
P(fail Focus check): ~1 − P(≥1 net at 3D) ≈ 1 − 0.84 = ~16%.

**State before:**
```
Almud — TS 95, Focus 3, Spirit 4, Coherence 8, Wounds 0
  Active: political meeting, no combat
  Composure: 7/8

RS: 55 | TC: 5 | IP: 20
```

### 10.2 Involuntary Leap Fires (Focus check failed)

**Duration:** 1 round. No operation (no intentionality set).  
**Co-movement:**
- Coherence −1 (minimum — undirected interaction, Relational ambient scale)
- Actual d6 fires
- Epistemic: Almud perceives things she didn't choose to perceive

**State delta:**
```
Almud: Coherence 8→7 (Dissonant — GM names per protocol)
Actual d6: narrative (ambient thread environment, no directed operation)
```

**What Almud perceives during involuntary contact:**  
She experiences the diplomatic agreement's thread configuration directly — not as rendered perception but as originary contact. She is not consciously present to interpret it. When she returns to rendering, she has a residue-perception: she knows something about the agreement's thread state that she cannot fully articulate (she wasn't rendering during contact). This is the epistemic auto-effect: not investigation advantage but unsettling partial knowledge.

**Composure check:** The involuntary loss of rendering in a political context is socially disruptive. Almud may appear momentarily absent or strange. GM may call Composure strain (1 point) — social context, unexpected rendering loss.

**P3 FLAG (SIM2-F-07): No rule for social consequences of involuntary Leap in non-combat contexts.** The Wound disruption and combat rules are covered. A high-TS practitioner in a political meeting who regularly loses rendering involuntarily should have some social-cost rule. Proposed: Composure −1 per involuntary Leap in a social scene (others notice the momentary absence).

### 10.3 Voluntary Extension Attempt

**Round after involuntary contact:** Almud attempts voluntary extension at +1 Ob.  
Standard Leap: Attunement + History + TPS. Assume Attunement 4, History 2, TPS 9 = 15D, Ob 1 base (TS 50+) + 1 (no Diagnosis) + 1 (extension penalty) = Ob 3.  
P(Success at 15D, Ob 3): ~97%.

**Operation declared (mid-contact, no Diagnosis):** Almud sets intentionality from within the contact — she already knows the agreement's thread state from involuntary exposure. She intends to Pull it (loosen, weaken the agreement).

**Ob for Pulling without Diagnosis:** Base Ob (normally actualised = 2) + skip Diagnosis +2 Ob = Ob 4. But: she had involuntary contact, giving her partial thread knowledge. GM may reduce the skip penalty to +1 Ob (she has some information, just not rendered Diagnosis). Flag as GM judgment call — no rule.

**P2 FLAG (SIM2-F-08): Involuntary contact as partial Diagnosis substitute — no rule.** A practitioner who experienced involuntary contact with a thread has information about its state. Whether this counts as partial Diagnosis (reducing the skip penalty) is undefined. Proposed: involuntary contact reduces the skip-Diagnosis Ob penalty by 1 (from +2 to +1) — the practitioner has some intentionality basis, just not a fully rendered one.

**Most likely outcome (15D, Ob 4 with reduced penalty):**  
P(≥4 net at 15D): ~84%. Probable success.

**State delta:**
```
Almud: Coherence 7→6 (Relational Pull, −1)
Agreement: Pulled — loosened, duration end-of-scene
RS: unchanged (Pull success)
```

**Scenario finding:** A Resonant practitioner can exploit an involuntary Leap to perform an undetected operation. She never declared a Thread operation — she appeared to merely zone out for a moment. No concealment roll was made because no operation was declared before the Leap. 

**P1 FLAG (SIM2-F-09): Involuntary-Leap-to-voluntary-extension bypasses concealment.** Concealment is set before the Leap as a pre-Leap action (§2.3). In voluntary-extension-from-involuntary-contact, there is no pre-Leap phase — the Leap already happened. The practitioner performs an operation with no opportunity for concealment to have been set. To TS 50+ observers: the operation is visible (they detect the Pull). But the practitioner had no chance to set concealment. This creates an exploit: high-TS practitioners in the presence of ongoing Thread activity can perform covert operations with structural undetectability. Proposed: voluntary extension requires a concealment roll at +1 Ob (setting concealment mid-contact is harder but possible) or the operation is always visible to TS 50+ observers.

---

## SIMULATION 11 — OPPOSING SIMULTANEOUS OPERATIONS (Mode B + D)

### 11.1 Scenario: Weave vs Pull on Same Configuration

**Setup:** Practitioner A (Vaynard, Weaving Relational config, Ob 3) and Practitioner B (opponent, Pulling same config, Ob 3). Both in contact simultaneously, opposing intentionalities.

Per §9.13:

| Both succeed | Shifting Object at Relational scale. Both Coherence −1 additional. |
| A succeeds, B fails | A's Weaving resolves normally. B takes failure consequences + Coherence −1. |
| Both fail | Shifting Object. Both failure consequences. RS −2. |

**Probability analysis:**

Assume both have 8D pools at Ob 3.  
P(Success) per practitioner ≈ 73%.  
P(Both succeed) ≈ 0.73 × 0.73 = 53%  
P(One succeeds) ≈ 2 × 0.73 × 0.27 = 39%  
P(Both fail) ≈ 0.27 × 0.27 = 7%

**Most likely outcome (53%): Shifting Object.**  
A Relational Shifting Object (§9.5): a bond/agreement that oscillates between binding and void. Deteriorates to Relational Gap in 1d3 seasons without Mending.

**Finding:** In most contested operations, opposing practitioners produce a Shifting Object rather than either succeeding. The contest mechanic systemically damages the substrate — neither faction wins, both pay Coherence, and a Shifting Object persists. This is philosophically coherent (Thread operations on contested ground are more destructive than uncontested ones) but strategically significant: if factions regularly oppose each other's Thread operations, they will collectively drive RS down faster than either could alone.

### 11.2 Cascade: Shifting Object to Gap

**Timeline:** Relational Shifting Object forms. Neither faction Mends it. 1d3 seasons → Relational Gap.

**Relational Gap:** What does a Relational Gap look like? §9.5 defines it as "a bond, agreement, or alliance [that] becomes unreliable" at Shifting Object stage. A Relational Gap would be: a bond that is simply absent — a relationship with no ground, where the parties cannot form meaningful agreements and may not reliably recognise each other's relational existence.

**P2 FLAG (SIM2-F-10): Relational Gap mechanical consequences undefined.** §9.5 defines Shifting Objects at each scale but does not define what a Gap at Relational, Territorial, or Structural scale means mechanically (only Object-scale Gaps and their RS costs are discussed). A Relational Gap should have distinct mechanical effects (e.g., faction treaties automatically void, social rolls in the affected relationship at +Ob) but none are specified. Flag as gap in the gap mechanics.

### 11.3 Cross-Mode Opposing Operations (Hybrid)

**Setup:** TTRPG practitioner in Personal Phase Weaves a Territorial configuration. In Strategic Phase, an opposing faction plays a Pull order on the same territory.

Per §9.13: "The board game roll substitutes for the opposing practitioner's individual roll."

**Timing issue:** Personal Phase happens before Strategic Phase in the Hybrid sequence. The TTRPG operation resolves in Personal Phase. The board game Pull order resolves at Cascade Phase. These are different moments in the season.

**P2 FLAG (SIM2-F-11): Cross-phase opposing operations have temporal ambiguity.** If the TTRPG Weaving resolves in Personal Phase and the board game Pull resolves at Cascade Phase, do they oppose each other per §9.13, or does the Weaving simply resolve first and then the Pull targets the (now-Woven) result? The text says they "resolve at Cascade Phase using this procedure" — implying both are held until Cascade. But the TTRPG practitioner resolved their roll in Personal Phase. Proposed: TTRPG Thread operations targeting configurations also targeted by Strategic Phase orders are flagged at Personal Phase and re-resolved at Cascade Phase using the opposing procedure. The original Personal Phase roll stands as the TTRPG practitioner's input.

---

## AGGREGATE FINDINGS — BATCH 2

| ID | Category | Description | Severity | Frequency |
|---|---|---|---|---|
| SIM2-F-01 | Ambiguity | Coherence cost when collective achieves contact but Focus halving prevents all operations | P2 | Low |
| SIM2-F-02 | Ambiguity | Past-Oriented Pulling excludes TPS from pool — no design rationale; TS doesn't improve execution | P2 | Medium |
| SIM2-F-03 | Gap | Past-Oriented Pulling recency Ob table not reproduced in v2.5 — referenced but absent | P1 | Systematic |
| SIM2-F-04 | Degenerate | Past-Oriented Pulling near-inaccessible without Spirit 5+ and History 3+ | P1 | Systematic |
| SIM2-F-05 | Ambiguity | Certainty checks for non-practitioner witnesses of temporal displacement undefined | P2 | Medium |
| SIM2-F-06 | Incoherence | Successful Past-Oriented Pull costs more RS than failure — counterintuitive, needs design note | P3 | Low |
| SIM2-F-07 | Gap | No social consequence rule for involuntary Leap in non-combat scenes | P3 | Medium |
| SIM2-F-08 | Ambiguity | Involuntary contact as partial Diagnosis substitute — undefined | P2 | Low |
| SIM2-F-09 | Optimal Play | Involuntary-to-voluntary-extension bypasses concealment — undetectable operation exploit | P1 | Low |
| SIM2-F-10 | Gap | Relational/Territorial/Structural Gap mechanical consequences undefined | P2 | Medium |
| SIM2-F-11 | Ambiguity | Cross-phase opposing operations: temporal ambiguity in hybrid mode | P2 | Medium |

**P1 findings: 3 (SIM2-F-03, SIM2-F-04, SIM2-F-09)**  
**P2 findings: 6**  
**P3 findings: 2**

---

## COVERAGE MATRIX UPDATE

| Mechanic | Test Type | Mode | Status | Key Findings |
|---|---|---|---|---|
| Collective Operations | Mode B + C | TTRPG | Complete | SIM2-F-01 |
| Belief conflict (collective) | Mode B | TTRPG | Complete | Minor — flavour > mechanics |
| Past-Oriented Pulling | Mode C | TTRPG | Complete | SIM2-F-02, F-03, F-04, F-05, F-06 |
| Involuntary Leap | Mode C | TTRPG | Complete | SIM2-F-07, F-08, F-09 |
| Opposing simultaneous ops | Mode B | TTRPG/HYB | Complete | SIM2-F-10, F-11 |
| Lattice fracture | Mode D | TTRPG | Complete | P3 threshold clarification |

---

## PRIORITY ACTIONS

**SIM2-F-03 (P1):** Reproduce recency Ob table in §2.4 Past-Oriented Pulling. Non-negotiable — the operation cannot be run without it.  
**SIM2-F-04 (P1):** Design decision needed — add TPS (or TPS÷2) to Past-Oriented Pulling pool, or add design rationale note explaining why TS doesn't improve execution.  
**SIM2-F-09 (P1):** Concealment rule needed for voluntary-extension-from-involuntary-contact. Proposed: operation is always visible to TS 50+ unless concealment roll made at +2 Ob during the extension Leap.
