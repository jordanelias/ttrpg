# SIM-X-03: Mass Battle + Thread (W-30 Cohesion Bolster + W-33 Rally the Broken)
## Mode: C (Full Scenario) + B (Interaction Chain)
## Mechanics: §8.9 Mass Combat × W-30 × W-33
## Scale: Company (100 soldiers per Strength point)
## Question: Do W-30/W-33 produce meaningful tactical decisions in mass combat, and what is the RS cost curve?

---

## Setup

**Battle: Lowenritter Professional infantry vs Rebel Militia. Practitioner (Solmund, TS 70) attached to Lowenritter.**

**Unit A: Lowenritter Infantry (defending)**
- CP: 4 (Veteran), Size: 5, Cohesion: 4, Morale: 6
- Formation: Shield Wall (−1D Off, +2D Def)
- Weapon: Heavy Cut, Armour: Medium
- Effective Combat Pool: min(CP=4, Strength=5) = 4D, −1D Off (Shield Wall) = 3D Off, +2D Def = 6D Def
- General: CR 4. Cohesion ceiling = min(CR=4, Military=4) = 4.

**Unit B: Rebel Militia (attacking)**
- CP: 2 (Militia), Size: 6, Cohesion: 3, Morale: 4
- Formation: Wedge (+2D Off, −1D Def)
- Weapon: Light Cut, Armour: Light
- Effective Pool: min(CP=2, Strength=6) = 2D, +2D Off (Wedge) = 4D Off, −1D Def (Wedge) = 1D Def
- General: CR 2. Cohesion ceiling = min(CR=2, Military=2) = 3.

**Weapon interaction:** Unit B (LightCut) vs Unit A (Medium armour): DR=4. LightCut vs Medium is ✗ — near-zero expected damage.
Unit A (HeavyCut) vs Unit B (Light armour): DR=1. HeavyCut vs Light is ✓✓ — effective.

**Practitioner: Solmund (TS 70)**
- Pool W-30: Spirit + History + TPS = 5+3+7 = 15D, TN7
- Pool W-33: Spirit + History + TPS = 15D, TN7 (same pool, Relational scale)
- Coherence: 10/10. RS: 100.
- W-30 Ob: 4 (Territorial scale). W-33 Ob: 3 (Relational scale).
- P(Success, 15D TN7 vs Ob4): from reference, 15D expected net = 5.0, P(≥4) ≈ ~92%
- P(Success, 15D TN7 vs Ob3): P(≥3) ≈ ~98%

**Co-movement for mass battle Thread ops:** Flat ×3 multiplier (RS −3 base).
RS impact per op: W-30 Success = RS unchanged (Weaving) + RS −3 co-movement base.
W-33 Relational: −1 Coherence (Relational scale §3.2). RS −3 co-movement.

Wait — re-check: Mass combat Thread RS cost table from §8.9:
> "Replace standard co-movement TT multiplier with flat ×3 (RS −3 base). Total RS loss from a single mass combat Thread operation capped at −15."

Weaving degree table: Success = RS unchanged. So W-30 on Success: RS −3 (co-movement only).
W-33 Relational scale: Coherence −1. RS −3 (co-movement). Plus RS cost from Relational scale Weaving degree: Success = RS unchanged. Total: RS −3, Coherence −1.

---

## State: Turn 1, Phase 1–3

### Units
Unit A (Lowenritter) — CP4, Size 5/5, Cohesion 4, Morale 6
  Formation: Shield Wall. Effective: 3D Off, 6D Def.
Unit B (Rebel) — CP2, Size 6/6, Cohesion 3, Morale 4
  Formation: Wedge. Effective: 4D Off, 1D Def.

### Tracks
RS: 100 | Solmund Coherence: 10/10 | Solmund at Unit A (same zone).

**Practitioner decision Phase 1:** Solmund declares W-30 (Cohesion Bolster) targeting Unit A.
Declared Phase 1 (public). Fires Phase 5 (Support Thread — see §8.9 Phase 5 order).
Thread Diagnosis occurs at Phase 1 (public declaration = rendering the target configuration).

---

## Phase 2 — Volley
No projectile units. W-30 declared, fires at Phase 5.

## Phase 4 — Engagement

**Both sides split Off/Def simultaneously.**
Unit A: 3D Off / 6D Def (Shield Wall locks in).
Unit B: 4D Off / 1D Def (Wedge locks in; −1D Def means minimal protection).

**Resolution:**

Unit A Off (3D, TN6 HeavyCut, TN7 Ob): 3D at TN7. Expected net = 3×0.33 = 1.0
Unit B Off (4D, TN5 LightCut): 4D at TN7 from defender perspective (TN for hit is 5 but defender rolls at TN7 for defence).

Wait — clarify: in mass combat, "Roll Offence dice at TN6/7/etc." refers to the Hit TN, not the defence TN.
Per §8.9 Phase 4: "(2) Split Offence/Defence (both sides simultaneous). (3) Damage = max(0, net hits + weapon modifier − DR)."
Roll Offence at Hit TN, Defence at Def TN (from weapon table). Both sides use their own weapon's TN values.

Unit A Off: 3D at TN6 (HeavyCut hit TN). P(die≥6) = 0.5. Expected net = 3×(0.5−0.1) = 1.2.
Unit B Def: 1D at TN7 (LightCut def TN). Expected = 1×0.33 = 0.33.

Net hits to Unit B: 1.2 − 0.33 = 0.87. Weapon modifier +4 (HeavyCut). DR(Unit B Light armour, HeavyCut) = 1.
Damage to Unit B: max(0, 0.87 + 4 − 1) = 3.87 Size loss.

Unit B Off: 4D at TN5 (LightCut hit TN). P(die≥5) = 0.6. Expected net = 4×(0.6−0.1) = 2.0.
Unit A Def: 6D at TN6 (LightCut def TN). Expected = 6×(0.5−0.1) = 2.4.

Net hits to Unit A: 2.0 − 2.4 = −0.4 → 0 hits (Shield Wall effective).
Damage to Unit A: 0 (Unit B cannot penetrate Shield Wall + defender's defence pool superiority).

**Critical insight:** Unit B (LightCut vs Medium armour) DR=4. Even with hits, damage = hits + 1 − 4 = hits − 3. Expected hits = 0 → expected damage = 0. LightCut vs Medium armour is functionally useless, confirming §8.2 weapon effectiveness table.

Mass Mismatch check: Unit B (Light weapon) attacking Unit A (Heavy weapon wielder): −1 defensive success to Unit B's defence. Applied: Unit B defence goes from 0.33 to max(0, 0.33−1) = 0 defensive successes.

Damage to Unit B (revised): 0.87 + 4 − 1 = 3.87. With mass mismatch to Unit B's def: unit B cannot defend effectively.

### State Delta: Phase 4
Unit B: Size 6 − 4 (rounded) = Size 2.
Unit A: Size 5 − 0 = Size 5.

---

## Phase 5 — Cascade

**Step 1: Apply Strength damage.**
Unit B: Size 6→2. Total lost = 4.

**Step 2: Cohesion checks.**
Unit B: lost 4 Strength this turn. Cohesion = 3. Lost (4) > Cohesion (3) → Cohesion degrades by 1 → Cohesion 3→2.
CP penalty at Cohesion 3–4: −1D. At Cohesion 1–2: −2D. Unit B was at Cohesion 3 (−1D), now at Cohesion 2 (−2D). Effective pool next turn: min(CP=2, Strength=2)=2D, −2D = 0D effective combat pool.

**Step 3: Morale checks.**
Unit B triggers: Size below 50% (Size 2 of original 6 = 33%): −1 Morale.
Size below 25%? No (33%). −1 total.
Allied unit routed? No. General incapacitated? No.
Unit B Morale: 4−1 = 3. At Morale 3: no rout (rout at 0).

**Step 4: Support Thread (W-30 fires now).**
Solmund rolls W-30: 15D TN7, Ob 4. P(Success) ~92%.
Expected outcome: Success.
Effect: Unit A Cohesion +2 for remainder of battle. 4+2 = Cohesion 6 (capped at 7, fine).
RS: −3 (co-movement). Solmund Coherence: −1 (Territorial scale §3.2).

**Step 5: General action.** General rallies (no action needed — Unit A stable).

### State Delta: Phase 5
Unit A: Cohesion 4→6 (W-30). Size 5. Morale 6.
Unit B: Size 2, Cohesion 2 (→−2D penalty), Morale 3.
RS: 100→97. Solmund Coherence: 10→9.

---

## State: Turn 2, Phase 1

### Units
Unit A — CP4, Size 5/5, Cohesion 6, Morale 6. Formation: Shield Wall. Effective: 3D Off, 6D Def.
Unit B — CP2, Size 2/6, Cohesion 2, Morale 3. Formation: Wedge (Cohesion collapse may break formation — GM call).
  Effective: min(CP=2, Strength=2)=2D, Cohesion −2D penalty = 0D effective pool.

**Unit B at 0D effective combat pool: cannot attack or defend.** Formation broken.

**Cohesion 0 rule:** Formation broken; cannot attack. Per table: CP penalty at Cohesion 0 = cannot attack.
But Cohesion is 2 (not 0) — penalty is −2D. With 2D base: 2−2 = 0D. **Functionally same as broken.**

**Unit B is mechanically eliminated in Turn 2.** Even if they survive combat, 0 effective dice mean they cannot participate.

---

## W-33 Assessment: Rally the Broken (hypothetical)

**Setup:** Suppose Unit B routed at end of Turn 2 (Morale dropped to 0 through continued engagement).
Solmund attempts W-33 to rally them.

W-33: Relational scale, Ob 3. 15D TN7. P(Success) ~98%.
Effect: Unit B re-enters with Cohesion 2 (regardless of prior value).
Coherence cost: −1 (Relational).
RS: −3 (co-movement).

Rallied Unit B stats: Size 2 (unchanged), Cohesion 2 (restored to 2 by W-33), CP 2.
Effective pool: min(CP=2, Strength=2) = 2D, Cohesion−2D penalty → 0D again.

**Finding F-11 [P1]:** W-33 restores Cohesion to 2, but a unit with Strength=2 and CP=2 still has 0D effective pool (Cohesion penalty −2D eliminates both base dice). W-33 cannot rescue a unit that has taken heavy Size losses — the Cohesion restoration is mechanically irrelevant when Strength is the binding constraint on pool size. W-33's effect is only meaningful if the unit retains Strength ≥ 4 (enough that Cohesion 2 penalty doesn't eliminate the pool entirely).

**Corrected W-33 scenario:** Unit B had Size 4 when it routed (hypothetical). Rallied Cohesion 2 → effective pool: min(2,4)=2D, −2D = 0D. Still 0D.

Even Size 5: min(2,5)=2D, −2D = 0D.

W-33 restoring Cohesion 2 only helps when CP ≥ 3 AND Strength ≥ 3+2 = 5.

**For CP=2 units, W-33 never produces a functional combat pool via Cohesion 2 restoration.** The only units W-33 can effectively rally are CP ≥ 3 (Professional+).

---

## RS Cost Curve for Thread in Mass Battle

| Operation | Ob | P(Success) | RS cost | Coherence cost | Net value |
|-----------|-----|-----------|---------|---------------|-----------|
| W-30 (Cohesion+2) | 4 | ~92% | −3 | −1 | Cohesion+2 ~1 turn |
| W-33 (Rally) | 3 | ~98% | −3 | −1 | Cohesion=2 (conditional) |
| Failure (W-30) | — | ~8% | −1 Cohesion to target | −1 | Harmful |
| W-30 + W-33 same battle | — | ~90% | −6 | −2 | Coherence 10→8 |

**Budget:** Solmund (Coherence 10) can sustain ~10 Relational+ operations before hitting Coherence 0. At −1/op: 10 ops = 10 seasons in campaign frame. But at −1 per mass battle op: a single large battle with 5+ Thread ops → Coherence 5 → Dissonant.

---

## Summary

| Finding | Category | Severity |
|---------|----------|----------|
| F-11 | Design | P1 | W-33 cannot rescue CP≤2 units: Cohesion=2 restoration insufficient when Strength is binding constraint |
| F-12 | Balance | P2 | W-30 effective but expensive (−1 Coherence, −3 RS): only 9–10 uses before Dissonant |
| F-13 | Interaction | P2 | Weapon mismatch (LightCut vs Medium+) is decisive at mass scale — composition determines outcome before Thread ops are considered |
| F-14 | Balance | P3 | W-30's Failure mode (Cohesion −1 to own unit) is dangerous: ~8% chance at Ob4 → must be weighed carefully |

**P1 Summary:** W-33 is design-broken for CP≤2 units. Fix proposal: W-33 should restore Cohesion to min(3, prior Cohesion before rout) OR restore +2 Strength (headcount) in addition to Cohesion. Requires [EDITORIAL: user decision on which fix or alternative approach.]
