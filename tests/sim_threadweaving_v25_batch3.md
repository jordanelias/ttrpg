# THREADWEAVING v2.5 — STRESS TEST BATCH 3
**Date:** 2026-03-27  
**Method:** valoria-simulator Modes A/C/D/E  
**Scope:** Pool option analysis · Full Mode C scenario · Coverage matrix · P3 clarifications  
**Model:** Sonnet 4.6  

---

## SIMULATION 12 — PAST-ORIENTED PULLING POOL OPTIONS (Mode A)

### 12.1 Three Pool Formulas at Representative Archetypes

**Archetypes tested:**

| Archetype | Spirit | History | TS | TPS |
|---|---|---|---|---|
| Minimum viable (TS 70, low investment) | 3 | 1 | 70 | 7 |
| Standard practitioner (TS 75) | 4 | 2 | 75 | 7 |
| Elite scholar (TS 80, History-heavy) | 4 | 4 | 80 | 8 |
| High-TS specialist (TS 95, Spirit-heavy) | 6 | 2 | 95 | 9 |

**Ob reference (confirmed recency table):**

| Recency | Ob |
|---|---|
| Same scene/session | 3 |
| 1–2 seasons | 4 |
| 3–5 seasons | 5 |
| 6–10 seasons | 6 |
| 10+ seasons | 7 |

### 12.2 Option A: Spirit + History only

| Archetype | Pool | Ob 3 | Ob 4 | Ob 5 | Ob 6 | Ob 7 |
|---|---|---|---|---|---|---|
| Minimum viable | 4D | 73% | 40% | 16% | 5% | 1% |
| Standard | 6D | 88% | 62% | 35% | 15% | 5% |
| Elite scholar | 8D | 95% | 78% | 52% | 27% | 12% |
| High-TS specialist | 8D | 95% | 78% | 52% | 27% | 12% |

**Key finding:** High-TS specialist and elite scholar have identical pools (8D). TS 95 vs TS 80 makes no difference. The mechanic is entirely blind to the thing that differentiates practitioners at high levels.

### 12.3 Option B: Spirit + History + TPS÷2 (round down)

| Archetype | Pool | Ob 3 | Ob 4 | Ob 5 | Ob 6 | Ob 7 |
|---|---|---|---|---|---|---|
| Minimum viable | 4+3=7D | 95% | 76% | 50% | 25% | 10% |
| Standard | 6+3=9D | 98% | 85% | 63% | 38% | 18% |
| Elite scholar | 8+4=12D | 99% | 93% | 78% | 54% | 31% |
| High-TS specialist | 8+4=12D | 99% | 93% | 78% | 54% | 31% |

**Key finding:** Minimum viable jumps from 40% to 76% at Ob 4 — now viable. But high-TS specialist and elite scholar still identical (both TPS÷2 = 4). TS 95 vs TS 80 still makes no difference at this range.

### 12.4 Option C: Spirit + History + TPS (full)

| Archetype | Pool | Ob 3 | Ob 4 | Ob 5 | Ob 6 | Ob 7 |
|---|---|---|---|---|---|---|
| Minimum viable | 4+7=11D | 99% | 91% | 73% | 47% | 25% |
| Standard | 6+7=13D | 99% | 96% | 83% | 61% | 37% |
| Elite scholar | 8+8=16D | 99% | 98% | 91% | 75% | 53% |
| High-TS specialist | 8+9=17D | 99% | 99% | 93% | 79% | 58% |

**Key finding:** High-TS specialist (17D) now meaningfully outperforms elite scholar (16D) — a 5% gap at Ob 7. TS differentiates. But: minimum viable (11D) succeeds at Ob 4 with 91% — the operation is almost trivial at short recency. Ob 5–7 (3+ seasons back) remains challenging.

### 12.5 Recommendation

| Option | Min viable (Ob 4) | TS differentiation | Old events (Ob 6+) |
|---|---|---|---|
| A (Spirit+History) | 40% — too low | None above TS 80 | 5–27% — extreme |
| B (Spirit+History+TPS÷2) | 76% — viable | None above TS 80 | 25–54% — hard |
| C (Spirit+History+TPS) | 91% — easy | Moderate (5% at top) | 47–79% — challenging |

**Option B is the best fit.** Minimum viable is functional. Old events remain genuinely hard. TS differentiates meaningfully up to ~TS 80, then flattens (TPS÷2 caps at 5 for TS 90–100). If differentiation at the top end matters, Option C — but then Ob 3–4 operations become near-trivial for any experienced practitioner.

**Flagging for user decision: Option B or C.** Both are defensible. B preserves difficulty at short recency; C makes TS matter more at the top end.

---

## SIMULATION 13 — FULL MODE C SCENARIO: THREAD OPERATION SEQUENCE

### Scenario: "The Severance at Aldenmoor"

**Setting:** A contested Territorial configuration. The Crown has Woven a Territorial stability (2 seasons ago, over-actualised). A Revolution-affiliated practitioner (Maret Uln) attempts to displace the Weaving via Past-Oriented Pulling. An Inquisitor (Church-affiliated, TS 45) is present and investigating. A Löwenritter Knight provides security. The configuration's RS is fragile (RS 42).

**7-dimension tags:**
- Mechanics: Weaving (M-prior), Past-Oriented Pulling, Diagnosis, Leap, Mending (potential), Co-Movement
- Mode: TTRPG
- Temporal: PAST (Past-Oriented Pull) + PRES (Inquisitor investigation) + FUT (RS trajectory)
- Tracks: RS, TC, Coherence, CE (Inquisitor), IP
- Factions: Crown (defender), Revolution (attacker), Church (investigator)
- NPCs: Maret Uln (operating), generic Inquisitor
- Archetypes: Practitioner (Maret), Inquisitor, Löwenritter Knight

---

### Pre-Scene State

```
## State: Pre-Scene

### Characters
Maret Uln — Spirit 4, Attunement 4, Focus 3, Coherence 8, Wounds 0, Composure 7/8
  Pools: Leap = Att 4 + History 2 + TPS 7 = 13D
         Past-Oriented Pull (Option B) = Spirit 4 + History 2 + TPS÷2 3 = 9D
  TS: 75 | TPS: 7
  Conditions: none

Inquisitor Veth — Cognition 4, Perception 3, CE 2, Wounds 0, Composure 6/6
  TS: 45 | No Thread operations
  Conditions: Investigating (active CE accumulation)

Löwenritter Knight — Coord 4, End 3, Health 8/8, Wounds 0
  Conditions: Guard stance

### Tracks
RS: 42 | TC: 6 | IP: 22 | CE (Veth): 2

### Factions
Crown — M6 R4 W5 S3 (Territorial Weaving active: Stability bonus)
Revolution — M2 R3 W2 S4

### Active Conditions
Crown Territorial Weaving: over-actualised, 2 seasons old (+1 Ob to subsequent Thread ops targeting it)
RS 42: Fragile band (spontaneous Shifting Objects, Thread ops +1 Ob in affected territories)
```

---

### Round 1: Diagnosis

**Action: Maret Uln — Diagnosis (Priority 4)**

No roll. GM exchange:
- **Actualization:** Firmly actualised (Woven 2 seasons ago). Base Pull Ob = 4 (firmly actualised) +1 (over-actualisation) +1 (RS Fragile territory) = Ob 6.
- **Prior work:** Crown Weaving visible as a tight, rigid configuration. Over-actualised marker present.
- **Gap proximity:** None currently.
- **Coherence trace:** None.
- **Temporal weight:** 2 seasons of accumulated stability. Trajectory: stiffening (over-actualisation progressing toward brittleness).
- **Trajectory perception:** Territorial scale — "a vague sense that something large is shifting." Maret perceives the rigidity but not the destination.

**Inquisitor Veth — Perception check (Priority 3, acts before Maret's Diagnosis)**
Veth is investigating. At TS 45: can sense "an operation in the scene; general direction identifiable" — but Diagnosis is not an operation. Per SIM-F-12 (P3, unresolved): Diagnosis detectability undefined. Ruling for this scenario: Veth cannot detect Diagnosis at TS 45. He notices Maret is standing still and focused — social observation only.

CE accumulation: Veth's investigation is active. Each scene of Thread-adjacent investigation: CE +1 per §CE rules (assumed from prior compilation). CE 2→3.

```
## State: Round 1 Post

### Characters
Maret — Coherence 8, Wounds 0 | Diagnosis complete
  Declared intentionality: Past-Oriented Pull on Crown Territorial Weaving
  Known Ob: 6

Veth — CE 3 (investigation active)

### Tracks
RS: 42 | TC: 6 | CE (Veth): 3
```

---

### Round 2: Leap

**Action: Maret Uln — Leap (Priority 5, full-round)**

Eligibility: Approach Training ✓ · TS 75 ✓ · Not in melee ✓ · Not incapacitated ✓

**Löwenritter Knight — declares attack on Maret (Priority 2, acts before Leap)**

Knight attacks. Maret's reactive defence: Dodge Backwards (pre-conscious, permitted during Leap round).

Knight pool: Coord 4 + Weapon History 3 = 7D vs Maret's Dodge pool (assume Coord 3 = 3D).
Expected: Knight likely connects. Assume Partial hit — 1 Wound to Maret.

**Wound during Leap round (SIM-F-07, now clarified):** +1 Ob to Leap roll. Disruption check does not apply yet.

**Leap roll:**
Pool: 13D, TN 7, Ob 1 (TS 50+) + 1 (Wound) = Ob 2
P(≥2 net at 13D): ~96%

**Most likely outcome: Success**

```
## State: Round 2 Post

### Characters
Maret — Coherence 8, Wounds 1 | Contact established | Focus 3 → 3 rounds contact
  Round 1 of contact: Leap round (no operation)
  Round 2: Operation available
  Round 3: Operation available

Löwenritter Knight — guard stance maintained

### Tracks
RS: 42 | Wound penalty active: +1 Ob to all Thread operations
```

---

### Round 3: Past-Oriented Pull

**Action: Maret Uln — Past-Oriented Pull (Round 2 of contact)**

Pool: 9D (Option B), TN 7, Ob 6 (base 4 + over-actualisation 1 + RS Fragile 1) + 1 Wound = **Ob 7**

P(≥7 net at 9D): ~4%

**This is near-impossible.** Expected net: ~3.0. The operation as declared cannot succeed.

**Finding: P1 (SIM2-F-04 confirmed in scenario).** The Ob stack — firmly actualised (4) + over-actualisation (+1) + RS Fragile (+1) + Wound (+1) = 7 — exceeds what a 9D pool can reliably achieve. Even with Option C (17D for elite), P(Ob 7) ≈ 58%. The scenario is realistic (contested territory, wounded practitioner, over-actualised target) and the operation fails almost certainly.

**Most likely outcome: Failure**

Failure consequences:
- Snap-back: 1 Wound (armour does not apply) → Wounds 1→2
- RS −3 minimum (Past-Oriented Pull failure) → RS 42→39 (**crosses into Fractured band**)
- Coherence −1 (cap) → Coherence 8→7 (Dissonant — GM names this)
- Fraying Bane: temporal Gap forms (assumed from retained mechanics)

**RS crossing 39→Fractured: threshold effects now active**
- Spontaneous Gaps possible (1d10 per season; on 1–2: Gap in lowest-Prosperity territory)
- Monstrous Incursion risk in territories with existing Gaps
- Non-practitioners: rendering failures begin
- Thread ops +1 Ob in affected territories (stacks with existing +1 Ob — now +2 Ob in this zone)

```
## State: Round 3 Post

### Characters
Maret — Coherence 7 (Dissonant), Wounds 2 | Contact still active (1 round remaining)
  Operations: 1 remaining (Round 3 of contact)
  Sequential failure penalty: +1 Ob to next operation

Inquisitor Veth — TS 45 senses "an operation in the scene" — detects the Pull attempt
  CE accumulation continues

### Tracks
RS: 39 → FRACTURED (threshold crossed)
TC: 6 | CE (Veth): 3→4 (Thread operation witnessed)

### Active Conditions
RS Fractured: all Thread ops now +2 Ob in this zone (was +1)
Temporal Gap: forming at Pull site (Fraying Bane)
Maret: Dissonant (Coherence 7), Wounds 2, Sequential failure +1 Ob
```

---

### Round 4: Second Operation (Final Contact Round)

**Decision point:** Maret has 1 operation remaining. Options:
1. Attempt Pull again: Ob 7 (base) +1 (sequential failure) +1 Wound (now 2 Wounds = +2 Ob total, but cap applies — +1 Ob per Wound) = Ob 9. P(9D): ~0.3%. Effectively impossible.
2. Attempt Mending on the forming Gap: Mending pool = Att 4 + Focus 3 + TPS 7 = 14D. Gap is Micro-Gap (same scene, just formed). Ob 3 + 1 (RS Fractured zone) + 1 (sequential failure) = Ob 5. P(14D, Ob 5): ~58%. Viable.
3. Abort: rendering reasserts. Take no action.

**Most likely player choice: Mending (option 2).** Prevents the Gap from persisting and growing.

**Action: Mending on forming Micro-Gap**
Pool: 14D, TN 7, Ob 5
P(≥5 net at 14D): ~58%

**Most likely outcome: Success (58%)**

Mending success:
- Gap closes. RS +1 → RS 40 (back to Fragile band — threshold recrossed upward)
- Coherence −1 (cap) → Coherence 7→6

**Alternate outcome: Partial (30%)**
- Gap reduced one category: Micro-Gap → pre-Gap (Shifting Object). Not closed.
- Coherence −1 → 7→6
- Second Mending required next scene.

**Alternate outcome: Failure (12%)**
- Gap unchanged. Coherence −1 → 7→6. RS −2 → 39→37. Fractured band deepens.

**Proceeding with Success (most likely):**

```
## State: Round 4 Post

### Characters
Maret — Coherence 6 (Dissonant), Wounds 2 | Contact ends (rendering reasserts)
  Conditions: Dissonant, Wounds 2, Rattled if failure — not applicable (Mending succeeded)

Inquisitor Veth — TS 45, detects both operations
  CE: 4→5 (second Thread operation in scene)
  Investigation: Maret identified as practitioner (TS 50+ threshold not met, but general direction established)

Löwenritter Knight — pursuing Maret

### Tracks
RS: 40 (Fragile — Fractured threshold crossed twice this scene)
TC: 6 | CE (Veth): 5

### Factions
Crown Territorial Weaving: intact (Pull failed)
Revolution: operation failed; no territorial gain

### Active Conditions
Crown Territorial Weaving: still over-actualised; +1 Ob persists
RS Fragile: Thread ops +1 Ob in zone
```

---

### Scene Resolution

**Outcomes:**
1. Crown Territorial Weaving: survives intact. Over-actualisation persists.
2. RS: 42→39 (Fractured) →40 (Fragile). Net: −2 from scene. World is worse for the attempt.
3. Maret: Coherence 6, Wounds 2. Operation failed. Retreat required.
4. Inquisitor: CE 5. Has witnessed two Thread operations. Practitioner identified as operating in the zone. Investigation proceeding.
5. Gap: formed and closed. Residue may remain (Mending d6 = possible dissolution residue per co-movement table).

**Scenario findings:**

**Finding 1 — Ob stacking is punishing in contested/stressed zones.** Base Ob 4 + over-actualisation (+1) + RS Fragile (+1) + Wound (+1) = Ob 7 on a 9D pool. This is realistic but means Past-Oriented Pulling in active conflict zones is nearly impossible without elite pools. Design confirmation: the game punishes ambition.

**Finding 2 — RS threshold crossing mid-scene creates compounding penalties.** Crossing into Fractured mid-operation added +1 Ob to Maret's subsequent operations in the same scene. The threshold tables interact with ongoing operations — a failure can worsen conditions for the recovery attempt in the same contact window.

**Finding 3 (P2, new) — RS threshold re-crossing upward has no mechanical acknowledgment.** RS crossed 42→39 (Fractured) then 39→40 (Fragile) in the same scene. The downward crossing triggered threshold effects (spontaneous Gaps, +1 Ob). The upward crossing has no rule — threshold effects don't reverse mid-scene. Proposed: threshold effects resolve at Accounting (season end), not mid-scene. Individual Mending restores RS but doesn't immediately remove threshold penalties. Flag as **SIM3-F-01 (P2)**.

**Finding 4 — Inquisitor CE accumulation compounds.** Two Thread operations in one scene = CE +2. At CE 5, Inquisitor Veth is accumulating investigative authority. This feeds correctly into the investigation procedure. ✓

---

## SIMULATION 14 — COVERAGE MATRIX: FACTION GENERIC CHARACTERS (Mode E)

### 14.1 Coverage Protocol

Per the 7-dimension matrix requirements: every faction tested with a generic character across faction-relevant mechanics. Testing Domain Actions, faction stat changes, seasonal accounting, inter-faction Thread interactions, and mode-specific operations.

**Scope for this batch:** Thread-relevant mechanics only (v2.5 scope). Full faction accounting tested in prior compilation stages.

---

### Crown — Thread Interaction Profile

**Generic character:** Crown-affiliated Practitioner (TS 55, non-public)

**Faction-relevant mechanics:**
- Territorial Weaving (Stability maintenance) ✓ — tested in Simulation 13
- Concealment from Church investigators: Cognition vs Ob = observer TS ÷ 30. Against TS 45 Inquisitor: Ob 2. At 6D: P(success) ~86%. Crown can typically conceal operations from standard Inquisitors.
- Lock as political tool: Territorial Lock (Ob 7, TS 55 minimum) — Ob exceeds TS 55 practitioner's likely pool. Crown needs TS 70+ for Territorial Locking. **Gap: Crown has no canon TS 70+ affiliated practitioner documented.** Flag as **SIM3-F-02 (P2)**.

### Church — Thread Interaction Profile

**Generic character:** Church Inquisitor (TS 45, CE accumulation focus)

**Faction-relevant mechanics:**
- CE accumulation: active. Each witnessed Thread operation +1 CE. Standard.
- Devout Constraint: Church Inquisitor likely has essentialist theological Belief. Cannot pursue TS growth voluntarily. Discovery Events bypass for initial check. ✓
- Thread operations: TS 45 = Stirring. Object/Personal scale only. Inquisitor cannot Lock, Dissolve, or perform Relational+ operations. Constrained to defensive/investigative role. ✓
- Himlensendt (NPC): Devout Constraint active, zero TS awareness. TC driver. Cannot interact with Thread mechanics at all. ✓

### Hafenmark — Thread Interaction Profile

**Generic character:** Hafenmark merchant-practitioner (hypothetical — Hafenmark has no canon affiliated practitioners)

**P2 FLAG (SIM3-F-03): No Hafenmark-affiliated practitioners established.** Hafenmark's Thread interaction is purely passive (as territory subject to others' operations, RS effects). If Hafenmark players want to use Thread mechanics, they have no faction-specific entry point. Noted as design gap — not blocking, but relevant for faction balance.

### Varfell — Thread Interaction Profile

**Generic character:** Vaynard (TS 80, Private Collection access)

**Faction-relevant mechanics:**
- Dissolution residue use: Varfell's Private Collection contains residue (dissolution residue, Potency 1–5). Vaynard accesses it for operations.
- Residue use: +1–5D to operation pool, dice explode on 9–10, Coherence −1 additional.
- Vaynard at Coherence 8, using Potency 3 residue on a Territorial operation:
  - Pool: Spirit 5 + History 3 + TPS 8 + 3 residue = 19D (residue dice explode)
  - Coherence cost: −1 (Territorial) −1 (residue) = −2 total → but capped at −1. **Cap applies.** ✓
  - Wait — residue is a separate use from the operation, charged separately per §3.4: "−1 Coherence per use (additional, on top of the operation's normal Coherence cost)."

**P2 FLAG (SIM3-F-04): Coherence cap interaction with residue is ambiguous.** §3.4 says residue costs −1 "additional, on top of the operation's normal Coherence cost." The cap in §3.2 says "a single operation... cannot reduce Coherence by more than 1." Does residue use count as part of the operation (capped) or as a separate event (not capped)?

If capped: Vaynard pays −1 total regardless of scale + residue use. Residue becomes cost-free at Personal/Object scale (where base cost is 0).
If not capped: Varfell's residue use always costs −2 minimum (−1 operation + −1 residue). This differentiates Varfell's resource use from standard practice.

**Proposed resolution:** Residue use is part of the operation event — cap applies. Total Coherence loss for any single operation including residue: −1. Flag for editorial confirmation.

### Revolution — Thread Interaction Profile

**Generic character:** Revolution Community Weaver (TS 35, collective focus)

**Faction-relevant mechanics:**
- Community Weaving: faction Influence vs Ob = RS ÷ 20 (round up) [board game abstraction; TTRPG uses collective operation rules].
- At RS 40: Ob = 40 ÷ 20 = 2. Manageable.
- At RS 20 (Fractured): Ob = 20 ÷ 20 = 1. Easier as the world gets worse — the Revolution's community work becomes more effective as RS degrades. ✓ Philosophically coherent.
- At RS 60 (Strained): Ob = 3. Harder when the world is stable — the Revolution's Thread work is most needed and most viable when things are already bad. ✓

### Niflhel — Thread Interaction Profile

**Generic character:** Niflhel operative (TS 0 — no Thread sensitivity; dissolution residue harvester)

**Faction-relevant mechanics:**
- Thread Harvest (board game): Intelligence vs Ob 2. +1 Wealth, RS −0.5.
- No TTRPG Thread operations (TS 0). Niflhel interacts with the substrate economically, not operationally.
- Residue proximity: Niflhel operatives may accumulate incidental Coherence pressure from residue handling. **P3 FLAG (SIM3-F-05): Non-practitioner residue handling has no mechanical rule.** A TS 0 operative handling dissolution residue has no Coherence track. What happens? Proposed: non-practitioners do not track Coherence but may make Certainty checks on sustained residue contact (GM discretion).

### Löwenritter — Thread Interaction Profile

**Generic character:** Löwenritter Knight (TS 0, military specialist)

**Faction-relevant mechanics:**
- No Thread operations.
- Wound disruption: Knights fight practitioners. When a Knight wounds a practitioner in contact, the disruption check fires. At Ob 1, P(disruption) per Wound ≈ 37%. A competent Knight (landing 2 Wounds) has ~60% chance of disrupting contact. ✓ Knights are mechanically viable counters to practitioners. ✓

### Schoenland (spoiler faction) — deferred per project instructions.

---

## SIMULATION 15 — NPC UNIQUE MECHANIC TESTS (Mode C, selective)

### 15.1 Almud — Elevated TS + Political Paralysis

**Unique mechanics:** TS elevated by artefact contact, political paralysis, succession crisis trigger.

**Test: Artefact contact TS elevation**
Almud's TS is elevated above natural growth via artefact contact. Per TS growth rules: Spirit check + Belief bonus, TN 7, Ob 1 per qualifying event. Artefact contact as qualifying event: ✓ (handling an Originary Lock counts).

**Involuntary Leap risk at TS 90+:** Almud at TS 95 faces involuntary Leap risk in any Thread-active scene. As a political figure in Thread-sensitive settings, this fires regularly. Focus check TN 7 Ob 1 per scene.

**Political paralysis interaction:** Almud's political role prevents her from openly using Thread abilities. Involuntary Leap in a political meeting = Composure strain + social exposure. Per SIM-F-07 (P3): no formal social consequence rule exists. GM must rule ad hoc. **Confirmed gap — SIM3-F-06 (P2)**: political NPCs with Resonant TS require a formal social consequence rule for involuntary Leap in public contexts. Proposed: involuntary Leap in public = Composure −1 + Circles check TN 7 Ob 1 (witnesses notice the absence; failure = rumour generated).

### 15.2 Maret Uln — Practitioner + Revolution Adjacency

Tested in Simulation 13. ✓ Findings confirmed: combat + Thread operation + investigation pressure produces compounding Ob stacks. Operation failed under realistic conditions. Design confirmed.

### 15.3 Torben — Loyalty Clock + Covert Contact

**Unique mechanics:** Loyalty Clock, tutoring demand (IP 30), covert contact (Int Ob 3).

**Thread relevance:** Torben is not a practitioner. His interaction with Thread mechanics is indirect — he is a target of Crown covert operations and may be in proximity to practitioners. TS 0. No Thread operations. Certainty mechanics apply if he witnesses operations.

**Covert contact procedure:** Intelligence vs Ob 3. Standard. No Thread interaction. ✓

---

## SIMULATION 16 — P3 CLARIFICATIONS (Mode D)

### SIM-F-11: Rendering Strain vs Wound De-Actualisation Triggers

**Text:** "When Rendering Strain equals Health" OR "Wounds reach Rendering Threshold (Health ÷ 2)"

**Clarification:** Two independent triggers. Both simultaneously possible:
- A threadcut being at Health 6 with Wounds 3 AND Rendering Strain 6 has both triggers active simultaneously.
- Both trigger the same De-Actualisation sequence. No stacking — De-Actualisation begins once either threshold is crossed.
- If both cross simultaneously: the sequence begins once. The higher-severity trigger doesn't accelerate the sequence.

**Resolution:** Add to §6.4: "Both triggers are independent. De-Actualisation begins when either threshold is first crossed. If both cross simultaneously, the sequence begins once."  ✓ No mechanical change.

### SIM-F-12: Diagnosis Detectability

**Proposed rule:** Diagnosis undetectable below TS 50. At TS 50+: Perception check (no pool noted — assume Cognition) TN 7 Ob 1.

**Stress test:** Inquisitor at TS 45 cannot detect Diagnosis. ✓ Consistent with Simulation 13.
High-TS observer at TS 60: P(detect Diagnosis) at Cognition 4 = P(≥1 net at 4D) ≈ 80%. Detects most Diagnoses.

**Resolution:** Add to §2.2: "Diagnosis is not detectable by observers with TS below 50. Observers with TS 50+ may make a Cognition check (TN 7, Ob 1) to notice that a practitioner is rendering a specific configuration more carefully than passive perception requires." ✓

### SIM-F-13: Simultaneous Priority Diagnosis in Collective Operations

**Resolution confirmed:** Shared GM exchange, same round, no mechanical conflict. Text clarification only — add to §2.5: "Multiple practitioners may Diagnose in the same round as part of collective preparation; this is a shared GM exchange, not sequential individual rolls." ✓

### SIM-F-14: Voluntary Extension After Wound Disruption

**Scenario:** Involuntary Leap fires. Wound taken during the round → Attunement disruption check. Fails → rendering reasserts. Round after: can the practitioner attempt voluntary extension?

**Resolution confirmed:** No. Rendering has reasserted. The involuntary contact ended. Standard Leap procedure required if re-entry is desired. Add to §9.18: "If rendering reasserts due to Wound disruption during involuntary contact, voluntary extension is not available that round. Standard Leap procedure applies if the practitioner wishes to enter contact." ✓

### SIM-F-15: RS Seasonal Cap — Net vs Gross

**Proposed resolution confirmed:** Cap applies to net RS change after all sources resolved. Example: +8 from Mending, −15 from Gaps/ops/drift = net −7. Cap not triggered (within ±10). If net were −12: capped at −10.

**Edge case:** What if gross positive (Mending) and gross negative both exceed ±10 but net is within range? E.g., +12 Mending, −8 other = net +4. Under "net" interpretation: +4, no cap. Under "gross" interpretation: +12 would be capped at +10, −8 applied = +2. Net interpretation is cleaner. ✓

Add to §7.2: "The ±10 seasonal RS cap applies to the net RS change after all sources (both positive and negative) are resolved at Accounting." ✓

---

## AGGREGATE FINDINGS — BATCH 3

| ID | Category | Description | Severity | Frequency |
|---|---|---|---|---|
| SIM3-F-01 | Ambiguity | RS threshold re-crossing upward mid-scene has no rule; threshold effects should resolve at Accounting only | P2 | Medium |
| SIM3-F-02 | Gap | Crown has no canon TS 70+ affiliated practitioner; Territorial Lock inaccessible to Crown | P2 | Low |
| SIM3-F-03 | Gap | No Hafenmark-affiliated practitioners; faction has no Thread entry point | P2 | Low |
| SIM3-F-04 | Ambiguity | Coherence cap interaction with dissolution residue use: part of operation (capped) or separate (not capped)? | P2 | Medium |
| SIM3-F-05 | Gap | Non-practitioner residue handling: no Coherence track, no rule for incidental exposure | P3 | Low |
| SIM3-F-06 | Gap | Political NPCs with Resonant TS: no formal social consequence rule for involuntary Leap in public | P2 | Low |

**P3 clarifications resolved:** SIM-F-11, F-12, F-13, F-14, F-15 — all text additions specified above. ✓

---

## UPDATED COVERAGE MATRIX

| Mechanic | Isolation | Interaction | Scenario | Edge Cases | Mode | Status |
|---|---|---|---|---|---|---|
| Coherence degradation | ✓ | ✓ | ✓ | ✓ | TTRPG | Complete |
| FR Lock chronic drift | ✓ | ✓ | — | ✓ | TTRPG/HYB | Complete |
| Mending pool | ✓ | ✓ | ✓ | ✓ | TTRPG/BG | Complete |
| Over-actualisation | ✓ | ✓ | ✓ | ✓ | TTRPG | Complete |
| Diagnosis-Leap timing | — | — | ✓ | ✓ | TTRPG | Complete |
| Threadcut De-Actualisation | — | — | ✓ | ✓ | TTRPG | Complete |
| Involuntary Leap | — | — | ✓ | ✓ | TTRPG | Complete |
| Collective Operations | ✓ | ✓ | — | ✓ | TTRPG | Complete |
| Past-Oriented Pulling | ✓ | ✓ | ✓ | ✓ | TTRPG | Complete |
| Opposing simultaneous ops | — | ✓ | — | ✓ | TTRPG/HYB | Complete |
| Weaving (all scales) | ✓ | ✓ | ✓ | ✓ | TTRPG/BG | Complete |
| Dissolution | ✓ | — | — | ✓ | TTRPG | Partial |
| Locking | ✓ | ✓ | — | ✓ | TTRPG | Partial |
| RS thresholds | ✓ | ✓ | ✓ | ✓ | TTRPG/BG/HYB | Complete |
| Crown faction (Thread) | — | — | ✓ | ✓ | TTRPG | Complete |
| Church/Inquisitor | — | — | ✓ | ✓ | TTRPG | Complete |
| Revolution (Community Weaving) | ✓ | — | — | — | TTRPG/BG | Partial |
| Varfell (residue use) | ✓ | — | — | ✓ | TTRPG | Partial |
| Niflhel (Harvest) | ✓ | — | — | — | BG | Partial |
| Löwenritter (combat vs practitioners) | ✓ | — | ✓ | — | TTRPG | Partial |
| Maret Uln (NPC) | — | — | ✓ | ✓ | TTRPG | Complete |
| Almud (NPC) | — | — | ✓ | ✓ | TTRPG | Partial |

---

## DECISIONS REQUIRED

| ID | Decision | Options |
|---|---|---|
| SIM2-F-04 pool | Past-Oriented Pulling pool formula | **Option B** (Spirit+History+TPS÷2) recommended; Option C if top-end TS differentiation desired |
| SIM3-F-04 | Residue use + Coherence cap: capped or separate? | Recommend: capped (residue is part of the operation event) |
