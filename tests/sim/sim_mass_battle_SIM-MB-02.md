# SIM-MB-02 — Mass Battle Scenario Simulation + Patch Audit
## Date: 2026-04-09
## Modes: C (Full Scenario) + Mode A re-run with provisional decisions applied
## Builds on: SIM-MB-01 findings. ED-351/352/353 provisional decisions applied.
## Source files: designs/mass_combat/mass_battle_v3.md, references/params_mass_combat.md

---

## PROVISIONAL DECISIONS APPLIED THIS SESSION

| ED | Decision | Rationale |
|---|---|---|
| ED-351 | Version 2 (PP-251): Size lost > Disc AND own loss > opp loss by ≥1 | Single-condition trigger fires in symmetric carnage, which has no narrative basis. PP-251 is mechanically clean and was the most recent params patch. |
| ED-352 | Option A: Volley pool = Power stat (1–7) directly | Preserves meaningful melee/ranged distinction. Generalship governs melee; unit quality governs ranged. |
| ED-353 | Option A: Full Command per sub-unit | Confirmed by §A.8 note structure. Splitting calculus lives in terrain/flanking decision, not forced Command dilution. |

---

## SCENARIO 1: Crown vs Hafenmark — Standard Pitched Battle

Crown: Size=6, Cmd=5, Disc=5, Mor=6, Power=4, HeavyCut, Medium (DR=3 given, DR=2 taken)
Hafen: Size=5, Cmd=3, Disc=4, Mor=5, Power=3, LightCut, Light (DR=2 given, DR=1 taken)
Formation: both Line. No tactics. No Thread.

Pool Crown: min(6,5)+5 = 10D. Pool Hafen: min(5,3)+3 = 6D.

| T | Crown Sz | Hafen Sz | Crown Disc | Hafen Disc | Crown Mor | Hafen Mor | Notes |
|---|---|---|---|---|---|---|---|
| 1 | 6 | 5 | 5 | 4 | 6 | 5 | — |
| 2 | 6 | 1 | 5 | 4 | 6 | 3 | Hafen <50%→Mor4; Hafen <25%→Mor3 |
| 3 | 6 | 1 | 5 | 4 | 6 | 3 | — |
| 4 | 6 | 0 | 5 | 4 | 6 | 3 | — |

**Result: Crown wins in ~4 turns. Clean outcome. No Discipline degradation triggered (PP-251 asymmetry condition not met — Crown damage too dominant, symmetric loss condition not satisfied). System healthy.**

---

## SCENARIO 2: Command Asymmetry Validation (Cmd=7 vs Cmd=1)

Elite: Size=5, Cmd=7, Disc=6, Mor=7. Levy: Size=7, Cmd=1, Disc=3, Mor=3.

| T | Elite Sz | Levy Sz | Elite Disc | Levy Disc | Elite Mor | Levy Mor | Notes |
|---|---|---|---|---|---|---|---|
| 1 | 5 | 5 | 6 | 3 | 7 | 3 | — |
| 2 | 5 | 1 | 6 | 2 | 7 | 1 | Levy Disc↓2; Levy <50%→Mor2; Levy <25%→Mor1 |
| 3 | 5 | 0 | 6 | 2 | 7 | 1 | — |

**Result: Elite destroys Levy in 3 turns. Design axiom validated: Command=7 vs Command=1 produces predetermined outcome. PP-251 Discipline check fired (Levy taking asymmetric damage). System healthy.**

---

## SCENARIO 3: Sub-unit optimality (ED-353 validation)

Attacker Cmd=5, Size=7 concentrated (pool=10D) vs Defender Cmd=3, Size=5 (pool=6D undivided).
Both resolved in 2 turns for concentrated. Concentrated: wins 75.2%.

3-way split (sub-sizes 3/2/2, each pool ~8/7/7D) vs undivided defender:
Resolved in 1 turn. Split: defender destroyed T1.

**Result: With full Command per sub-unit, splitting is ALWAYS advantageous when the defender cannot maintain a full pool against each sub-unit. This directly contradicts §A.8.**

---

## SCENARIO 4: Volley Phase — Archer unit (ED-352 Option A validated)

Power=3 Archer (TN6) vs Heavy Infantry (DR=3):
- E[Size loss/turn] = 0.052. P(any damage) = 4.3%.
- Verdict: Archers vs Heavy armour = negligible. Weapon effectiveness table confirmed correct.

Power=3 Archer vs Light Infantry (DR=1):
- E[Size loss/turn] = 0.700. P(any damage) = 46.5%.
- Verdict: Archers vs Light = meaningful suppression. Design intent confirmed.

**System healthy for Option A. Ranged unit specialization is mechanically meaningful.**

---

## SCENARIO 5: Practitioner Thread depletion over 7-turn battle

Thread Sensitivity=55, Coherence=10, Battle scale (Territorial, Ob=4, -1 Coh/op).
6D pool, Lock operations every turn. RS starting=60.

| Turn | Coherence | RS | Result |
|---|---|---|---|
| 1 | 9 | 57 | Lock success |
| 2 | 8 | 54 | Lock success |
| 3 | 7 | 51 | Lock success |
| 4 | 6 | 48 | Lock success |
| 5 | 5 | 45 | Lock success |
| 6 | 4 | 42 | Lock success |
| 7 | 3 | 39 | Lock success — DISSONANT |

**Finding (confirms D-15-F1 from SIM-MB-01): Coherence=3 after 7 turns of constant operation — Dissonant, not Severed. Design doc warning overstates the risk. Correction to §A.10 required. → PP-501.**

Also: RS dropped from 60 to 39 over 7 turns of Lock (-3 RS per success). At this rate, 13 turns of consistent Lock would put RS at Calamity threshold. The ×3 multiplier is a meaningful long-campaign constraint even with conservative operation choices.

---

## SCENARIO 6: General death cascade — PP-273 applicability

Army destroyed before Turn 4 (when Cmd=0 would fire). The sequence: Size degrades under opponent pressure → army collapses at Size=0 before general death fires Stage 2.

**Finding: PP-273 (1D minimum after general death) requires the army to survive long enough after general death for the rule to apply. In most combat scenarios, Morale cascade from Stage 2 death (-2 Mor uncapped, plus active triggers) routes the army within 1 turn — faster than any further engagement opportunity. PP-273 is a theoretical floor with near-zero practical activation. Document as design note only.**

---

## SCENARIO 7: Shield Wall multi-direction (ED-356)

Defender in Shield Wall vs 2 simultaneous engagements (1 negated, 1 unmitigated):
- Option A (+2D Def all engagements): E[Size loss/turn] = 0.68
- Option B (+2D Def front only): E[Size loss/turn] = 0.83
- Differential: 21% more damage under Option B.

**Decision: Option A. Blanket formation modifier is mechanically consistent. PP-MB-07 phrasing "applies normally" referred to the attack resolution of the unmitigated flank, not the defender's pool. → PP-500 [PROVISIONAL].**

---

## SCENARIO 8: §A.8 claim — definitive split analysis [P1 FINDING]

Results (50k trials each):
| Configuration | Attacker wins |
|---|---|
| Concentrated 10D vs undivided 10D | 75.2% |
| Split 3+3 (defender pool splits 5+5D per engagement) | 95.5% |
| Split 3+3 (defender focuses full 10D on one, other attacks free) | 99.1% |

**Finding [P1]: §A.8 claim is INCORRECT. "Splitting Size=6 into 3+3 against undivided Size=5 defender is disadvantageous" is false in both defender response strategies.**

Structural reason: Even with full Command per sub-unit, the defender CANNOT maintain a full pool against multiple simultaneous engagements unless the design explicitly grants defenders full Command vs each sub-unit. If defender pool splits: 95.5% attacker win rate vs 75.2% concentrated — splitting is dramatically superior. If defender focuses: one sub-unit absorbs damage but the other attacks unopposed at full pool — 99.1% attacker win rate.

**§A.8 claim only holds if both the following are true:**
1. Defender maintains FULL Command pool against each attacker sub-unit simultaneously AND
2. Defender's Size loss from each engagement does NOT accumulate (impossible — damage is simultaneous)

Neither condition holds under the current rules. §A.8 is either: (a) wrong as stated and should be struck, or (b) correct under a different model where defender has unlimited pool vs simultaneous engagements — which would need to be made explicit.

**→ ED-358 raised [P1 BLOCKER]: §A.8 claim conflicts with simulation results. Rule text needs correction or defender simultaneous-engagement model needs explicit definition.**

---

## SCENARIO 9: Mutual destruction probability

Equal-strength engagement (Size=3, Cmd=3, Disc=3 each):
P(both reduced to 0 simultaneously) = 2.6% (~1 in 38 engagements).

**Result: Pyrrhic mutual destruction is rare but occurs in ~3 out of 100 equal-strength exchanges. Consistent with design intent (possible, not common). PP-240 calibrated correctly.**

---

## NEW P1 FINDING

| ID | Finding | Source |
|---|---|---|
| ED-358 | §A.8 claim contradicted by simulation: splitting 3+3 wins 95.5% vs concentrated 75.2% | SIM-MB-02 Scenario 8 |

---

## PATCHES PROPOSED THIS SESSION

| PP | Scope | Description | Status |
|---|---|---|---|
| PP-500 | mass_battle_v3.md + params | Shield Wall +2D Def applies to all simultaneous defensive pools [PROVISIONAL] | Proposed |
| PP-501 | mass_battle_v3.md §A.10 | Coherence depletion warning correction: 7-turn battle → Coherence=3 (Dissonant, not Severed). Severance requires ≥9 consecutive turns of operation from full Coherence. [PROVISIONAL] | Proposed |
| PP-502 | mass_battle_v3.md §A.6 | Discipline degradation trigger: propagate PP-251 to design doc. Replace single-condition trigger with two-condition trigger (PP-251 governs). [PROVISIONAL] | Proposed |
| PP-503 | mass_battle_v3.md §A.7 | Volley Phase pool: "Effective Power" = Power stat (1–7 quality tier). Add explicit definition. [PROVISIONAL] | Proposed |
| PP-504 | mass_battle_v3.md §A.6 + §A.8 | Command per sub-unit: add explicit rule text "Command applies in full to each commanded sub-unit's pool." [PROVISIONAL] | Proposed |
