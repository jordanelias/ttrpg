# THREADWEAVING v2.5 — STRESS TEST SIMULATION
**Date:** 2026-03-27  
**Method:** valoria-simulator protocol (Modes A/B/C/D)  
**Source:** designs/threadweaving_redesign_v25.md  
**Model:** Sonnet 4.6  

---

## SIMULATION 1 — COHERENCE DEGRADATION CURVES (Mode A + C)

### 1.1 Input Space

| Variable | Range | Typical | Edge |
|---|---|---|---|
| Scale per operation | Object(0) / Personal(0) / Relational(−1) / Territorial(−1) / Structural(−2) | Relational (most campaign pressure) | Structural (max cost) |
| FR Lock/Dissolution bonus | −1 additional | Applied sometimes | Every operation |
| Past-Oriented Pulling bonus | −1 additional | Rare | Every operation |
| Mending cost | −1 (fixed) | Occasional | Every operation |
| Dissolution residue use | −1 per use | Rare | Every operation |
| Degree table Partial/Failure costs | +1 to +2 (Relational+) | ~25% of operations | All operations fail |
| Recovery: season off | +1 per season | Once per 3 seasons | Every season |
| Recovery: Knot Anchoring | +1 per scene | Twice per campaign | Unavailable |

### 1.2 Archetype Campaign Curves

**Assumptions per curve:**
- Campaign: 30 sessions, 10 seasons
- ~3 operations per session (1 per operative scene; many sessions have 0–1 Thread scenes)
- Total operations over campaign: ~45–60
- Starting Coherence: 10

---

**Archetype A: Restrained Practitioner (Object/Personal focus)**
- Scale mix: 80% Object/Personal (0 Coherence), 15% Relational (−1), 5% Territorial (−1)
- FR ops: 1 total campaign
- Past-Oriented Pulling: 0
- Dissolution residue: never
- Partial/Failure rate: 20%
- Recovery: 1 season off (mid-campaign)

| Season | Ops | Coherence Loss | Recovery | Running Coherence |
|---|---|---|---|---|
| 1 | 4 | −1 (1 Relational) | 0 | 9 |
| 2 | 5 | −1 (1 Relational) | 0 | 8 |
| 3 | 4 | 0 | +1 (season off) | 9 |
| 4 | 5 | −1 | 0 | 8 |
| 5 | 5 | −1 | 0 | 7 |
| 6 | 6 | −1 | 0 | 6 |
| 7 | 5 | −1 | 0 | 5 |
| 8 | 6 | −1 | 0 | 4 |
| 9 | 6 | −1 | 0 | 3 |
| 10 | 6 | −1 | 0 | 2 |

**Final Coherence: 2 (Fractured)**  
**Assessment:** A restrained practitioner who takes one recovery season still enters Fractured state by late campaign. The Einhir trajectory in miniature — restraint delays but does not prevent crisis. ✓ Design intent confirmed.

---

**Archetype B: Ambitious Practitioner (Relational/Territorial scale)**
- Scale mix: 30% Object/Personal, 50% Relational, 15% Territorial, 5% Structural
- FR ops: 3 total campaign
- Past-Oriented Pulling: 2 total
- Dissolution residue: 4 uses
- Partial/Failure rate: 30% (higher — harder Obs)
- Recovery: 1 Knot Anchoring (+1) mid-campaign

| Season | Ops | Coherence Loss | Recovery | Running Coherence |
|---|---|---|---|---|
| 1 | 5 | −3 (3 Relational) | 0 | 7 |
| 2 | 6 | −4 (3 Relational + 1 FR Lock −1 extra) | 0 | 3 |
| 3 | 5 | −3 (2 Relational + 1 Partial @ Relational) | +1 Knot | 1 |
| 4 | 4 | −2 (1 Territorial + 1 Relational) | 0 | 0 → **Rendering Crisis** |

**Final Coherence: 0 at Season 4**  
**Assessment:** An ambitious practitioner hits Rendering Crisis within the first third of the campaign without deliberate recovery strategy. P1 FLAG: Season 2's −4 is plausible in a single crisis scene (Leap + FR Lock + one failed Relational op = −3 minimum, plus Partial outcome = −4). A practitioner can hit Fractured in a single bad session. See §1.4.

---

**Archetype C: Crisis Practitioner (minimal use, forced escalation)**
- Scale mix: 60% Object/Personal, 20% Relational, 10% Territorial, 10% Structural
- FR ops: 2
- Past-Oriented Pulling: 1
- Dissolution residue: 2 uses
- Partial/Failure rate: 25%
- Recovery: 2 seasons off, 1 Knot Anchoring

| Season | Ops | Coherence Loss | Recovery | Running Coherence |
|---|---|---|---|---|
| 1 | 3 | −1 | 0 | 9 |
| 2 | 4 | −2 | 0 | 7 |
| 3 | 2 | 0 | +1 (off) | 8 |
| 4 | 5 | −3 (Territorial + FR + residue) | 0 | 5 |
| 5 | 3 | −2 | +1 Knot | 4 |
| 6 | 4 | −2 | 0 | 2 |
| 7 | 3 | −1 | +1 (off) | 2 |
| 8 | 5 | −2 | 0 | 0 → **Rendering Crisis** |

**Final Coherence: 0 at Season 8**  
**Assessment:** Even a crisis practitioner with disciplined recovery (2 seasons off, 1 Anchoring) hits Rendering Crisis before end-campaign. Recovery of +1/season is outpaced by accumulated scale pressure once faction demands escalate.

### 1.3 Coherence Recovery Adequacy Assessment

| Recovery Type | Rate | Equivalent Operations Offset | Adequate? |
|---|---|---|---|
| Season off | +1 | Offsets 1 Relational op | Marginal |
| Knot Anchoring | +1 | Offsets 1 Relational op | Limited — max ~2/campaign |
| Einhir technique | +1 (GM discretion) | As above | Unavailable until late campaign |
| Community Weaving (Coherence 4–3) | +1/season | Requires another practitioner | Conditional |

**Finding:** Recovery ceiling is +3 over a 10-season campaign for a well-supported practitioner (+2 seasons off + 1 Anchoring). Operations at Relational+ scale cost −1 per op minimum. Campaign arc naturally generates 15–20 Relational+ ops. Net Coherence loss: ~12–17 minus 3 recovery = 9–14. Starting value is 10. Every PC practitioner who engages at scale WILL hit Rendering Crisis before campaign end without extraordinary recovery planning. This is design-confirmed, not a flaw — but players need to understand it from session 1.

### 1.4 FINDING: Single-Session Coherence Cliff

**Setup:** Practitioner with Coherence 7 faces a crisis scene requiring: Diagnosis + Leap + FR Lock (large-scale) + one Relational Weaving after  
**Mechanism:**
- FR Lock (Territorial, Partial): −1 (Territorial scale) −1 (Lock bonus) −2 (Partial degree) = −4
- Relational Weaving (Success): −1
- **Total this scene: −5 → Coherence 7 → 2**

**Severity: P1** — A practitioner can plunge from Stable (8+) to Fractured (2) in a single extended scene. No warning, no intermediate threshold crossed. At Coherence 7 (Dissonant), the player may not realize the danger until it's too late.

**Frequency:** Medium. Any scene involving a large-scale FR op with a sub-optimal outcome.

**Proposed fix:** Add a mid-scene Coherence warning at Dissonant threshold. When a practitioner enters Dissonant (≤7), GM should explicitly name their Coherence to the player. Consider adding a pre-Leap "Coherence cost estimate" — player can see the expected cost before committing to the operation.

---

## SIMULATION 2 — FR LOCK CHRONIC RS DRIFT (Mode B)

### 2.1 Interaction Chain

FR Lock (success) → RS −2 immediate → Chronic drift begins → RS −1 or −2/season → potential Locked Zone formation

### 2.2 10-Season Campaign Projection

**Scenario:** Campaign starts RS 60. One Lock placed per faction in Territory level (8 factions × 1 Lock typical = up to 8 Locks in play at any time). Realistically: 3–5 active Locks at mid-campaign.

**Conservative (3 Locks, mixed durations):**

| Season | New Locks | Lock Immediate RS | Chronic Drift | Other RS (Gaps, Winter, Ops) | Season-End RS |
|---|---|---|---|---|---|
| 1 | 1 | −2 | 0 | −2 (1 Gap, winter −1) | 56 |
| 2 | 1 | −2 | −1 (L1: S2) | −2 | 51 |
| 3 | 1 | −2 | −2 (L1: S3, L2: S2) | −3 | 44 |
| 4 | 0 | 0 | −4 (L1: S4 at −2/season, L2 at −1, L3) | −4 | 36 |
| 5 | 0 | 0 | −5 | −3 | 28 |
| 6 | 1 | −2 | −6 (3 Locks all at 4+ season tier = −2/season each) | −3 | 17 |
| 7 | 0 | 0 | −6 | −3 | 8 |
| 8 | 0 | 0 | −5 (one Lock permanent = drift ceases) | −3 | 0 → **Rupture** |

**Finding: P1 — CRITICAL.** FR Locks alone, without any removal, drive RS to 0 in 7–8 seasons. Three Locks at 4+ season duration produce −6/season in chronic drift alone. This is on top of all other RS costs. **The game cannot sustain 3+ unremoved Locks past mid-campaign.**

### 2.3 Lock Accumulation Rate Assessment

| Condition | Lock Rate | Sustainable? |
|---|---|---|
| No Locks ever placed | N/A | RS reaches ~20 by S10 (winter drift + gaps alone) |
| 1 Lock, removed after 2 seasons | −3 total | Sustainable |
| 1 Lock, never removed | −6 to −8 over 10 seasons | Marginal |
| 3 Locks, none removed | −18 to −30 over 10 seasons | Fatal |
| 5 Locks (moderate faction conflict) | −30 to −50 over 10 seasons | Rupture before midgame |

**Finding: P2 — Lock removal mechanics must be visible and accessible.** The Pulling to reverse a Lock (Ob = original TS ÷ 10, round up) is well-designed but players may not realize the RS implications of leaving Locks in place. GMs should explicitly track Lock ages and communicate chronic RS drift to the table.

### 2.4 Seasonal Cap Interaction

The ±10 seasonal RS cap (hybrid mode §7.2) interacts awkwardly with this:
- 3 active old Locks produce −6 chronic drift
- Add 2 Gap formations (−8), winter (−1), and 2 Thread op partials (−2)
- Gross RS change: −17, capped at −10
- Cap provides meaningful protection in hybrid — but only if it's actually enforced. **P3 FLAG:** The cap definition says "±10 per season" but doesn't specify whether it applies before or after Mending offsets. Clarification needed.

---

## SIMULATION 3 — MENDING POOL PROBABILITY (Mode A)

### 3.1 Pool Composition

**Mending pool:** Attunement + Focus + TPS (TS ÷ 10, round down)

Distinct from Weaving/Pulling (Spirit + History + TPS). This is intentional — different faculty engaged.

| Character Type | Typical Attunement | Typical Focus | TS | TPS | Pool Size |
|---|---|---|---|---|---|
| Minimum-viable practitioner | 3 | 2 | 50 | 5 | 10D |
| Experienced practitioner | 4 | 3 | 70 | 7 | 14D |
| Dedicated Mender (TS 90, Focus 4) | 5 | 4 | 90 | 9 | 18D |
| Expert (TS 100) | 6 | 4 | 100 | 10 | 20D |

### 3.2 Ob Reference

| Gap Type | Ob | Min pool for 80% success |
|---|---|---|
| Shifting Object | 2 | 6D (P(≥2 net at TN7) ≈ 70%; 8D ≈ 82%) |
| Micro-Gap | 3 | 8D (P(≥3) ≈ 60%; 10D ≈ 73%) |
| Standard Gap | 5 | 15D (P(≥5) ≈ 84% at 15D) |
| Entrenched Gap | 6 | 18D (P(≥6) ≈ ~70% at 18D; see below) |
| Catastrophic Gap | 7 | 20D+ |
| Locked Zone border | 8+ | Likely impossible for most practitioners |

### 3.3 Probability Table (TN7, expected net ≈ 0.33/die)

| Pool | Ob 2 | Ob 3 | Ob 5 | Ob 6 | Ob 7 | Ob 8 |
|---|---|---|---|---|---|---|
| 10D | ~82% | ~73% | ~35% | ~22% | ~12% | ~6% |
| 14D | ~95% | ~90% | ~58% | ~42% | ~28% | ~17% |
| 18D | ~99% | ~97% | ~76% | ~62% | ~47% | ~34% |
| 20D | ~99% | ~99% | ~84% | ~72% | ~58% | ~44% |

*Computed from binomial with p=0.33, chaining adjustments ≈ +0.03/die.*

### 3.4 Findings

**Finding 1 — P2: Standard Gap requires specialist.**  
Ob 5 at a 10D pool (minimum viable) = 35% success. A character who barely meets the TS threshold (50+) will fail Standard Gap Mending 65% of the time. This feels correct for an emergency Mending — it SHOULD be hard — but players may attempt it without realizing the near-certain failure.

**Finding 2 — P2: Entrenched Gap is effectively capped at ~62%.**  
Even a dedicated 18D Mender has a 38% failure rate on Entrenched Gaps. Failure causes: Gap unchanged + 1 Wound + Coherence −2 + RS −2. A Mender who fails an Entrenched Gap in bad health can cascade to incapacitation and Coherence damage simultaneously.

**Finding 3 — P1: Catastrophic Gap is nearly impossible.**  
Ob 7 at 20D = 58%. Even the most powerful practitioner fails more than 40% of the time. And failure at Catastrophic is: Gap unchanged + RS −2 + Coherence −2 + Wound. Multiple failure attempts on the same Gap without recovery will deplete the Mender. After 3 failures: Wound count makes the next Leap harder (+1 Ob per Wound), further reducing pool efficacy. Catastrophic Gaps likely require multi-session Mending arcs or the Einhir ritual framework.

**Finding 4 — P3: Attunement vs Spirit asymmetry.**  
Weaving pool uses Spirit. Mending uses Attunement. A practitioner specialized in Spirit (social archetype) is better at standard operations but worse at Mending. A practitioner specialized in Attunement (Einhir scholar archetype) is better at Mending. This creates a meaningful specialization split. However: **there is no character advancement pathway explicitly labeled "Mending specialist."** GMs should note that Attunement investment is the path to Mending competence.

---

## SIMULATION 4 — OVER-ACTUALISATION IMPACT (Mode B)

### 4.1 Interaction Chain

Relational+ Weaving (Success) → Over-actualisation → +1 Ob to subsequent ops targeting same configuration → potential brittleness under stress → Shifting Object on shock → Scale-up to Territorial/Structural → RS drift

### 4.2 Scenario: Diplomatic Agreement Woven at Relational Scale

**Setup:** A practitioner Weaves a diplomatic agreement between Crown and Hafenmark (Relational scale, Ob 3). Success. Over-actualisation penalty: subsequent Thread ops targeting this agreement +1 Ob. Season 1 after Weaving, a second practitioner attempts to Diagnose and Pull the agreement (opponent faction trying to dissolve it). 

**Expected vs actual experience:**

*Without over-actualisation:* Pull at Ob 3 (firmly actualised — it was Woven). P(Success at 8D) = ~70%.  
*With over-actualisation:* Pull at Ob 4 (firmly actualised +1 over-actulisation). P(Success at 8D) = ~55%.

**Finding:** Over-actualisation provides a modest defensive bonus (~15% increase in opponent's failure rate). Not game-breaking but meaningful — a Woven agreement is harder to tear down.

**BUT: Brittleness (P-18) introduces asymmetry.** If a non-Thread event (territorial seizure, institutional collapse) threatens the agreement, the GM may rule it shatters into a Relational Shifting Object rather than bending. This creates a counterintuitive outcome:

- **Without Weaving:** The agreement might just... end. Treaty broken, consequences follow, but world state is coherent.
- **With Weaving:** Agreement shatters into a Shifting Object. Now you have a Relational Shifting Object (§9.5) — a relationship that oscillates between binding and void, with 1d3 season deterioration to a Relational Gap.

**Finding: P2 — Weaving at Relational+ scale can produce WORSE outcomes than not Weaving** when the thing you Wove is later stressed. A practitioner who Weaves a fragile political agreement may turn a "broken treaty" into a "Relational Gap requiring Mending." GMs must communicate P-18 clearly when players consider Relational+ Weaving in politically volatile contexts.

### 4.3 Territorial Scale: Stability Increase

**Setup:** Faction raises Stability by 1 via Territorial Weaving. Success. Over-actualisation:
- Subsequent Thread ops targeting this stability: +1 Ob
- Diagnosis on this configuration: +1 Ob

**Season 2 consequence:** A Dissolution practitioner (opponent) tries to destabilize the territory. Their base Ob is now Ob 5 (Territorial) + 1 (over-actualised) = Ob 6. P(Success at 12D) ≈ 50% vs 60% base.

**But:** If a siege hits the territory (non-Thread event), the stabilized configuration becomes brittle. GM rules it shatters. Now: Territorial Shifting Object → 1d3 seasons → Territorial Gap → RS −4/season it persists. The faction spent a Thread operation to raise Stability and may end up with a Territorial Gap.

**Finding: P2 — confirmed amplification of P2 from §4.2.** Territorial Weaving in active conflict zones is a trap without explicit player understanding of P-18.

---

## SIMULATION 5 — DIAGNOSIS-BEFORE-LEAP COMBAT TIMING (Mode D)

### 5.1 Timing Sequence

Per §2.3 and §2.2:
- Diagnosis: Priority 4 standard action
- Leap: Priority 5 full-round action (no movement, no attack)
- Standard operation: following round(s)

**Minimum combat commitment for one Thread op:** 3 rounds (Diagnosis round + Leap round + Operation round)

At Focus 1: 3 rounds minimum, 0 operations completed (Contact too brief — §2.3).  
At Focus 2: 3 rounds minimum, 1 operation.  
At Focus 3: 3 rounds minimum, 2 operations.

### 5.2 Combat Pressure Tests

**Test A: Enemy attacks during Diagnosis round**  
Diagnosis (Priority 4). Enemy (Priority 3) acts before Diagnosis? No — Priority 3 is LOWER number = earlier action. Check priority structure.

**P1 FLAG: Priority numbering ambiguity.** The ruleset uses Priority numbers but the convention (lower = earlier? higher = earlier?) is not defined in this document. Leap is "Priority 5." Diagnosis is "Priority 4." If lower number = earlier action, then Priority 4 Diagnosis fires before Priority 5 Leap (correct). But if Priority 5 is "highest priority = first action," the Leap would fire before Diagnosis — which is the wrong sequence. **This must be clarified in the core engine.** Assuming lower = earlier for this simulation.

**Test B: Enemy attacks during Leap round**  
The practitioner is eligible for reactive defence only (Parry or Dodge Backwards). Parry uses combat pool — does this affect the Leap roll? The document says "these are pre-conscious physical responses that do not require rendering." Therefore: Parry or Dodge Backwards do not penalize the Leap roll. ✓ Consistent.

BUT: If the practitioner takes a Wound during the Leap round, before the roll is resolved — the Leap immediately requires an Attunement check (§2.3: Wound disruption during contact). **When does this check fire relative to the Leap roll itself?**

**P2 FLAG: Leap roll vs. Wound disruption timing unclear.** If a Wound is taken during the Leap round (before the Leap roll), should:  
(a) The Wound penalty (+1 Ob) apply to the Leap roll, then proceed normally if successful?  
(b) The Attunement disruption check fire immediately on the Wound, preventing the Leap entirely?

The disruption check text says "while contact is established" — implying it applies after a successful Leap, not during the attempt. So (a) is correct — Wound adds +1 Ob to the Leap roll. The disruption check only applies if contact is already established. ✓ Consistent, but needs explicit clarification in the text.

**Test C: Diagnosis → Gap appears before Leap**  
Scenario: Practitioner Diagnoses a thread. The Diagnosis reveals a Gap forming (correctly noted as "critical safety information"). Next round, before the Leap, the Gap opens fully. The practitioner's declared intentionality is now directed at a thread that has been partially dissolved.

**P2 FLAG: No rule for mid-sequence configuration change.** The practitioner has Diagnosed. They have not yet Leaped. The target changed. Can they revise their declared intentionality? The text does not address this case.

**Proposed resolution:** Practitioner may revise declared operation before the Leap roll (they have not yet suspended rendering). If they proceed with the original intentionality against an altered configuration: +2 Ob (malformed intentionality, as per skipping Diagnosis rule).

**Test D: Multiple practitioners, staggered Diagnosis**  
Collective operation. Anchor Diagnoses (Priority 4). Helpers Diagnose (Priority 4, same round). How are simultaneous Priority 4 actions resolved? No rule provided for same-priority simultaneous actions.

**P3 FLAG: Simultaneous-priority resolution not defined.** For collective Diagnosis: functionally no problem — all practitioners need to Diagnose but can do so in the same round sharing the same GM exchange. The gap is in the rules text, not the actual play experience.

**Test E: Diagnosis in stealth context**  
Practitioner attempts Diagnosis while hiding. Diagnosis is a rendered act — it is the last act of rendering before the Leap. Is Diagnosis visible to TS 30+ observers?

Per §2.3, visibility rules apply to operations (Weaving, Pulling, etc.). Diagnosis is not an operation — it is perception. 

**P3 FLAG: No rule for Diagnosis detectability.** An Inquisitor with TS 50 is in the same scene. Can they detect that a practitioner is Diagnosing a configuration? The text specifies operation visibility tiers but not Diagnosis detectability. Suggested rule: Diagnosis is not detectable at TS below 50. At TS 50+: Perception check TN 7 Ob 1 to notice that someone is rendering the thread more carefully than passive perception would require.

---

## SIMULATION 6 — THREADCUT DE-ACTUALISATION (Mode C)

### 6.1 State Setup

**Character: Solmund (Threadcut Being)**

| Attribute | Value |
|---|---|
| Health | 6 |
| Rendering Strain | 0 (initial) |
| Rendering Threshold | Health ÷ 2 = 3 (Wounds) |
| TS | 100 (assumed: Solmund renders himself at maximum) |
| Wounds | 0 |

**Scenario:** Solmund renders beyond observer capacity for 4 scenes, sustaining a large group of Low-TS observers. Then confronted by antagonist practitioners attempting Dissolution.

### 6.2 Phase 1: Beyond-Ceiling Rendering

**Scene 1:** Beyond-ceiling rendering. Rendering Strain +1 → RS 1  
**Scene 2:** Beyond-ceiling rendering. Rendering Strain +1 → RS 2  
**Scene 3:** Beyond-ceiling rendering. Rendering Strain +1 → RS 3  
**Scene 4:** Beyond-ceiling rendering. Rendering Strain +1 → RS 4  

**State at Scene 4:** Rendering Strain 4 = Health 6. Not yet at threshold. But: RS (4) does not equal Health (6), so De-actualisation has NOT begun.

**P3 FLAG: Rendering Strain threshold is confusingly worded.** §6.2 says: "When Rendering Strain equals Health" — De-actualisation begins. But it also says "or Wounds reach Rendering Threshold (Health ÷ 2)." These are independent triggers. At Health 6: Rendering Strain threshold = 6, Wound threshold = 3. The two triggers have very different rates of approach. Under normal beyond-ceiling rendering, Rendering Strain hits 6 after 6 scenes. Under combat Wounds, Rendering Threshold hits 3 Wounds potentially in 1–2 rounds. The relationship between these two triggers is not stated.

**Proposed clarification:** Both triggers independently initiate De-actualisation. Whichever is reached first activates the sequence.

### 6.3 Phase 2: Antagonist Dissolution Attempt

**Practitioners:** Two practitioners, one attempting Dissolution.  
**Pool:** Spirit 5 + History 2 + TPS 7 = 14D at TN7  
**Ob:** Territorial Dissolution = Ob 6 (threadcut being of significant scale)  
**But:** Threadcut being interference from §9.7: +Ob = TS ÷ 20 = 100 ÷ 20 = 5. Total Ob: 11.

**P1 FLAG: Ob 11 is effectively impossible.** P(Success at 14D, Ob 11) ≈ 0.5%. This is functionally an auto-failure. A Solmund-equivalent threadcut being cannot be Dissolved by any credible practitioner team. This may be intentional (Solmund is effectively indestructible unless he chooses to De-actualise), but it needs explicit statement in the rules rather than emerging from mechanical arithmetic.

**Resolution options per §9.6:**
- **Pulling to weaken:** Ob = being's TS ÷ 10 = 10. Similarly extreme. P(Success at 14D, Ob 10) ≈ 3%. Also near-impossible.
- **Outlasting De-actualisation:** Viable — but requires 6 scenes of patience against a being that can be actively hostile.
- **Communication:** Only viable path if the being is cooperative.

**Finding: P1 — High-TS threadcut beings are mechanically immune to direct Thread operations.** The §9.7 interference formula needs recalibration. Suggested: cap the interference Ob modifier at +3 regardless of TS. This keeps high-TS beings hard to target without making them impossible.

### 6.4 Phase 3: De-Actualisation Sequence (Voluntary)

**State:** Solmund chooses voluntary De-actualisation. No Ob penalties.

**Round 1 state:**
```
Solmund — Rendering Strain 6 = Health 6 → De-actualisation triggered
Intelligible face dissolving.
- TS 30+ observers: perceive loss of coherence
- All operations +2 Ob
- Stabilisation option: Weaving on self (pool vs Ob = Wounds + Rendering Strain = 0 + 6 = 6)
  - Voluntary: Solmund does not attempt stabilisation (choosing cessation)
```

**Round 2 state:**
```
Solmund — perceivable only by TS 50+
- Operations +4 Ob
- Second stabilisation attempt: not taken
```

**Round 3+ state:**
```
Configuration returns to unintelligible ground.
Micro-Gap forms (closes within scene).
Dissolution residue remains.
```

**Finding:** Voluntary De-actualisation is clean and well-defined. The three-round sequence provides narrative space. ✓

**P2 FLAG: Stabilisation Ob at voluntary cessation.** If a dying/De-actualising being chooses NOT to stabilise (voluntary cessation), but a friendly practitioner attempts Weaving on it to force stabilisation — the Ob is Wounds + Rendering Strain. At full De-actualisation, this is Ob 6+ (§6.4 Weaving vs Ob = Wounds + RS: 0 Wounds + 6 RS = Ob 6). P(Success at 14D) ≈ 42%. A practitioner *can* attempt to save Solmund against his will. Whether they can is a separate question from whether they should. The rules allow it; the philosophy strongly discourages it (P-04: monstrosity ≠ moral). Good design. ✓

---

## SIMULATION 7 — INVOLUNTARY LEAP EDGE CASE (Mode D)

### 7.1 Setup

**Character:** TS 90 practitioner (triggering involuntary Leap risk at TS 90–100)  
**Scenario:** In a scene with a nearby major Thread operation

**Per §9.18:**
- Focus check TN 7 Ob 1 to avoid involuntary Leap
- Failure: rendering suspends for 1 round, no operation occurs
- Co-movement fires: Coherence −1, actual d6

**P2 FLAG: Involuntary Leap during combat.**  
If the practitioner is in melee and an involuntary Leap triggers, they lose rendering for 1 round. They cannot Parry (Parry requires rendering — it's a combat response). But the text says reactive defence uses "pre-conscious physical responses." Does an involuntary Leap suppress even pre-conscious physical responses?

Per the framing: an involuntary Leap is a forced rendering suspension. The text says the practitioner's "rendering suspends involuntarily." If this is true rendering suspension, the same rules as voluntary Leap should apply — Parry and Dodge Backwards remain available as pre-conscious responses.

**Proposed rule:** Involuntary Leap allows Parry and Dodge Backwards as defensive responses (same as voluntary Leap). Attacks cannot be made. The practitioner is available to physical harm but has no conscious defence response other than reflexes.

### 7.2 Voluntary Extension from Involuntary Leap

Per §9.18: Practitioner may attempt Leap roll at +1 Ob in the round after involuntary contact to extend into voluntary contact.

**Problem:** This requires the practitioner to have not been disrupted by a Wound during the involuntary contact. If they took a Wound during the involuntary round, the disruption check fires (Attunement TN 7 Ob 1). If they fail the disruption check, rendering reasserts — and they're in the round AFTER, attempting voluntary extension from a baseline of reasserted rendering. Can they still extend?

**P3 FLAG: Voluntary extension eligibility after Wound during involuntary contact is undefined.** Suggested resolution: If rendering reasserted due to Wound disruption, voluntary extension is not possible — the rendering has already reasserted. Standard Leap procedure required if they want to re-enter contact.

---

## AGGREGATE FINDINGS TABLE

| ID | Category | Description | Severity | Frequency | Resolution |
|---|---|---|---|---|---|
| F-01 | Cascade | Single-session Coherence cliff: −5 possible in one scene | P1 | Medium | Add pre-operation Coherence cost estimate; GM warning at Dissonant entry |
| F-02 | Cascade | FR Lock chronic drift fatal within 7–8 seasons (3 unremoved Locks) | P1 | High | Explicit Lock age tracking; GM communication of RS implications |
| F-03 | Degenerate | Catastrophic Gap Mending: ~58% max success rate with exhausting failure consequences | P1 | Low | Expected — should require multi-session arc or Einhir framework |
| F-04 | Degenerate | TS 100 threadcut being: effectively immune to Dissolution and Pulling (Ob 11/10) | P1 | Low | Cap §9.7 interference modifier at +3 |
| F-05 | Ambiguity | Priority numbering convention not defined in this document | P1 | Systematic | Define in core engine: lower number = earlier action |
| F-06 | Incoherence | Over-Actualisation Brittleness (P-18) can make Weaving worse than not Weaving | P2 | Medium | Already intended — requires explicit player communication; add GM sidebar |
| F-07 | Ambiguity | Leap roll vs Wound disruption timing during Leap round unclear | P2 | Medium | Clarify: Wound during Leap round adds +1 Ob to Leap roll; disruption check only after successful Leap |
| F-08 | Ambiguity | Mid-sequence configuration change (target altered between Diagnosis and Leap) | P2 | Low | Add rule: revise intentionality before Leap at no cost; proceed without revision at +2 Ob |
| F-09 | Ambiguity | Mending epistemic co-movement by degree table needed (P-19) vs §2.4 framing | P2 | Low | Already patched — confirm P-19 is integrated into main §2.4 text, not just the patch log |
| F-10 | Crunch Cascade | Standard Gap Mending (Ob 5) at minimum pool = 35% success; failure loops dangerous | P2 | Medium | Add explicit "do not attempt Standard+ Gaps without 14D+ pool" guidance |
| F-11 | Ambiguity | Rendering Strain vs Wound De-actualisation trigger relationship unclear | P3 | Low | Clarify: both triggers independent; whichever reached first activates De-actualisation |
| F-12 | Ambiguity | Diagnosis detectability by TS observers not defined | P3 | Medium | Add rule: Diagnosis undetectable below TS 50; Perception Ob 1 at TS 50+ |
| F-13 | Ambiguity | Simultaneous-priority Diagnosis in collective operations | P3 | Low | Same-round collective Diagnosis is a shared GM exchange; no mechanical conflict |
| F-14 | Ambiguity | Voluntary extension eligibility after Wound disruption during involuntary Leap | P3 | Low | Clarify: Wound disruption ends contact; no voluntary extension possible |
| F-15 | Ambiguity | RS seasonal cap (±10, hybrid mode): applies before or after Mending offsets? | P3 | Low | Define: cap applies to net RS change after all sources resolved |

---

## COVERAGE MATRIX UPDATE

| Mechanic | Test Type | Mode | Status | Key Findings |
|---|---|---|---|---|
| Coherence degradation | Mode A (isolation) | TTRPG | Complete | F-01 |
| FR Lock chronic drift | Mode B (interaction) | TTRPG/HYB | Complete | F-02 |
| Mending pool | Mode A (isolation) | TTRPG/BG | Complete | F-03, F-10 |
| Over-actualisation | Mode B (interaction) | TTRPG | Complete | F-06 |
| Diagnosis-Leap timing | Mode D (edge cases) | TTRPG | Complete | F-05, F-07, F-08, F-12 |
| Threadcut De-actualisation | Mode C (scenario) | TTRPG | Complete | F-04, F-11 |
| Involuntary Leap | Mode D (edge cases) | TTRPG | Complete | F-14 |

---

## SESSION-CLOSE ACTIONS REQUIRED

1. **P1 patches needed (4):** F-01, F-02, F-04, F-05 — route to mechanic-audit for patch specification
2. **Confirmation needed:** P-19 (Mending epistemic co-movement by degree) integrated into §2.4 main text — verify in Haiku batch
3. **Lock removal visibility:** Add explicit GM guidance (not a mechanical change)
4. **§9.7 interference cap:** Proposed fix is "cap at +3" — requires editorial confirmation before patching
5. **Update gap register:** F-01 through F-15 — 4 P1, 5 P2, 6 P3
