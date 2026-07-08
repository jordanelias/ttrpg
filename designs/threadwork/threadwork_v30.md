<!-- SKELETON — mechanical spec only — atomized 2026-04-13 from designs/ttrpg/threadwork_v30.md -->
<!-- Infill: designs/ttrpg/threadwork_v30_infill.md -->
<!-- DO NOT add prose. Rationale/examples live in the infill file. -->

<!-- v30 baseline — renamed from designs/ttrpg/threadwork_redesign_v25.md on 2026-04-13 -->
# THREADWORK MECHANICS — v2.6
## Status: CANONICAL
## Date: 2026-03-27 (revised 2026-04-02)
## Authority: Philosophical Foundations (immutable) → this document (design proposal, requires editorial approval)
## Version: v3.2 — Part Nine (S-01–S-06 / P-11–P-26) applied in-place. All appendix sections eliminated. PP-632: §2.6 Opposing Operations added.
## Revision: Incorporates Leap-as-rendering-suspension. Supersedes v1.

---

---

## CANONICAL POOL NOTICE (PP-616, PP-618, PP-619, PP-624, PP-625)
> **All Thread operation pool formulas in this document have been updated to the canonical
> post-PP-619 form: (Spirit × 2) + relevant History bonus + Thread Pool Score.**
> Ob tables in this document predate the three-axis Ob system (PP-622/PP-623).
> **Canonical Ob values: params_threadwork.md §Three-Axis Ob System.**

## SETTLEMENT-LEVEL THREAD CONSEQUENCES (Throughline T1)

Thread operations at Relational scale or above produce settlement-level stat consequences alongside province-level MS effects. Full table: settlement_layer_v30 §4.4. Key effects: Weaving → Order +1. Dissolution Failure → Defense −1, Order −1. Mending → Prosperity +1. Community Organizing → Order +1, Prosperity +1. Lock → Defense +1 (permanent). Cap: ±1 per settlement stat per season from Thread.

Thread perception is settlement-modulated: +1 Ob in Cathedral settlements (rendering thick with doctrine). −1 Ob in Outposts near Askeheim (rendering thin). Einhir heritage settlements reveal historical Thread layers on Success.

## MODE APPLICABILITY INDEX
*Added 2026-04-02 — applied per user session instruction*

### ALL MODES (TTRPG, Board Game, Hybrid)
- Part 1: Philosophical Framing — foundational for all modes
- Part 5: Mending Stability (World Track) — world-level track applies in all modes
  - §5.4: Mending Stability in Board Game (BG only)
  - §5.5: Mending Stability in Hybrid (Hybrid only)
- Part 8: Interdependency Map — implementation sequence for all modes
- Part 9: Stress Test Patches (S-01/P-11 through S-??/P-30) — all mode patches compiled here

> **Scale-based Mending Stability (P-25):** Mending Stability consequences on Partial and Failure results scale with operation scale. The below-the-waterline portion of a Structural thread is enormously larger than an Object thread's; when the interaction fails, the unintelligible portion's response is proportionally more severe. **Override degree table Mending Stability values with the following:** | Scale | Partial Mending Stability Cost | Failure Mending Stability Cost | |---|---|---| | Object | 


> **Mass battle Mending Stability cost note (ST-TW-03):** **Finding from sim_x_03_massbattle_thread.md**
**[DESIGN NOTE]**
**[STRUCK — campaign_architecture_v1 §3.1]** The ×3 MS multiplier is replaced by a flat additive model:

- **Standard Mass Battle:** −1 MS per battle, regardless of scale or outcome.
- **Cataclysmic Mass Battle** (player-tagged at scene setup, extraordinary circumstances): −2 MS.
- **Mass Battle in destabilized substrate** (MS ≤ 10): −1 MS base, plus Stability Check (Ob 3) — failure adds −1 MS (maximum −2/battle in destabilized conditions).

The flat model makes warfare cost predictable and cumulative. Three battles per season = −3 MS. No spikes. The player can see degradation coming and choose to stop fighting. The Stability Check at MS ≤ 10 preserves the sense that warfare near the tipping point is especially dangerous — chance-based, not multiplicative.

A practitioner performing Thread operations in mass battle pays the standard per-operation Coherence cost (−1/op at Relational+, 0 for Mending per asymmetry) but MS drain from battle is the flat −1 regardless of operation count. This makes Thread in battle a meaningful choice rather than strategically suicidal.

### TTRPG ONLY
- Part 3: Coherence (10→0) — personal practitioner track; no BG equivalent
- Part 6: Threadcut Beings — TTRPG encounter mechanics


> **Paradox window resolution (PP-193):** [PROVISIONAL] The P-22 paradox window resolves as follows. **Auto-resolution:** At window end (1d3 scenes), physical facts update; thread snaps to displaced state. Observers Thread Sensitivity 30+ perceive sudden realignment. **Early closure:** A practitioner may Mend the paradox window site (treat as Micro-Gap, Ob 3). Success: window closes immediately. Partial: duration halved. Failure: window persists full duration; MS −2. **Exploitation during window:** Another practitioner may target the paradoxed thread at +2 Ob (two simultaneous configurations resist). On Failure: window collapses immediately and operation's Failure consequences also apply. **After window:** Temporal Disjunction persists (memories intact; physical facts now match displaced state). No further mechanics unless new operation targets displaced thread.

> **Sequential POPs on paradoxed thread (PP-203):** [PROVISIONAL] If a practitioner attempts a Past-Oriented Pull targeting a thread that is currently in a paradox window (P-22 delayed manifestation active on that thread), the attempt **automatically fails**. The thread exists in two simultaneous states; intentionality cannot lock onto a thread with indeterminate configuration. The Leap still fires (Coherence cost applies, Focus window consumed), but the operation resolves as Failure without a roll (no MS cost from the operation itself — the substrate did not engage). The paradox window is unaffected. This ruling applies only to the paradoxed thread itself; other threads in the same scene are unaffected.



> **Threadcut/Mending (P-17):** A threadcut being present at a Gap site draws on the same substrate the practitioner is trying to Mend. Its continuous self-rendering competes with the Mending operation's intentionality. **Mechanical effect:** +Ob = being's Thread Sensitivity ÷ 20 (round up), maximum +4, to Mending operations targeting that Gap while the being is present. This Ob modifier stacks with other modifiers (territory effects, Fraying B

> **Opposing beliefs (P-12):** *Already patched into §2.5.* Directly opposing Beliefs require a pre-Leap Belief check. Tangential conflicts: non-chaining dice.

> **Pool floor correction (R-57):** Minimum 5 dice before rolling any Pull. Below 5D (from wounds, degradation, low stats):
Apply to §2.4 Pulling, eligibility section.

> **Ob correction (R-55):** For Dissolution targeting a living being at Personal scale:
> Ob = target's Endurance + target's Spirit + armour modifier (Light+1, Medium+2, Heavy+3)
> Standard success = Partial (Shifting Object, ~50% HP damage).
> Overwhelming required for immediate incapacitation.
Replaces: "same as Lock" for Pe


### BOARD GAME ONLY
- §5.4: Mending Stability in Board Game
- §7.1: Board Game — New Order: Mend, Co-Movement Card Deck (18 cards), Lock Chronic Drift, Mending Stability Track

### HYBRID ONLY
- §5.5: Mending Stability in Hybrid
- §7.2: Hybrid Mode
- §7.3: Updated Mode Branching

### CROSS-MODE (applies in both TTRPG and Hybrid)
- §A.10 of mass_battle_v3.md: Thread operations in mass battle (Hybrid / TTRPG mass combat)

> **Cross-reference (ST-TW-05):** Coherence referenced in mass_battle_v3 §A.10 = this document's personal Coherence track (10→0). Not a unit stat. auto-cost −1/op depletes personal track by 1 per mass battle operation.

---

## PHILOSOPHICAL FOUNDATION

# PART TWO: OPERATIONS

## 2.1 Approach Training

Approach Training is a binary tag: a practitioner either has it or does not. It is the prerequisite for performing any Thread operation through the Leap (§2.3). Without Approach Training, even a Thread Sensitive character (TS ≥ 30) cannot Leap — they perceive the substrate but cannot suspend rendering enough to act on it.

**Acquisition pathways:**

- **Character creation (Formation 2F: Practitioner Mentorship):** Per character_histories §Formation, characters whose 2F slot is "Practitioner Mentorship" begin with Approach Training as a starting skill. This is the canonical entry route for player characters wanting Thread agency from session 1.
- **In-campaign training (full-season commitment):** A character without Approach Training may acquire it through a single full-season training arc with a willing practitioner-mentor at TS ≥ 50. Requirements:
  - Mentor at Disposition ≥ +2 with the trainee.
  - Mentor's TS ≥ 50 (cannot self-train; cannot be trained by a TS 30-49 practitioner — the mentor must have substrate-control sufficient to demonstrate suspension safely).
  - One full season committed: trainee cannot pursue other Domain Actions or Faction-track advancement during the training season.
  - Resolution scene at season end: Spirit pool, TN 7, Ob 2.
  - Success: Approach Training tag granted. Trainee gains 1 Thread Sensitivity (the formal Leap exposure registers as substrate engagement per §3.2).
  - Partial: tag granted at next Accounting (one additional season of mentor-led practice required, no further roll).
  - Failure: tag not granted. The trainee may attempt again next season with a different mentor (cannot retry with the same mentor in the same campaign year — the training relationship is exhausted).
- **Spontaneous acquisition (rare, narrative-driven):** The Catalyst event "First Leap" (per character_histories §Catalyst 4E) may grant Approach Training implicitly if the character survives an unguided first Leap. This is an engine adjudication moment — typical resolution is +Approach Training tag + 1 Conviction Scar + Coherence −1 (the unguided Leap leaves perceptual residue per A1/C1 inseparability).

**Effects of holding the tag:**

- Eligible to attempt §2.3 Leap operations (suspending rendering).
- +1D on Leap rolls (per character_histories §270 Approach Training trait listing — Scene Battle Thread context: trained specifically for the surrender of rendering).
- Partial Leap result no longer imposes +1 Ob on the subsequent operation (advanced training benefit per character_histories §498 ladder).
- Eligible for collective operations (§2.5) at scales requiring Approach Training (Relational and above).

**Effects of NOT holding the tag (TS ≥ 30 without training):**

- Character perceives Thread phenomena per §2.6 visibility rules and may participate in Thread-related social actions (Argue, Read with Thread context).
- Cannot Leap. Cannot perform any Thread operation (Weaving, Pulling, Locking, Dissolution, Mending). The substrate is legible to them but their rendering does not have the trained capacity to suspend.
- Eligible to undergo training as described above.

**Loss of tag:**

- Approach Training is generally permanent once acquired. The trained capacity is a structural change to the practitioner's rendering, not a learned skill that decays.
- One exception: a character who suffers Coherence reduction to 0 with no Reconstitution (per canon/01_foundations §4 Coherence 0 outcomes) loses the tag along with their identity. Reconstituted characters at TS 90+ regain it as part of Full Reconstitution.

[EDITORIAL: ED-774 — Approach Training §2.1 propagated from threadwork_v25_historical + character_histories §Formation 2F + character_histories §270 (Approach Training trait) + character_histories §498 (skill ladder). Closes propagation defect: §2.1 was empty header in canonical threadwork_v30 with infill comment 'No changes from current §5.1' but §5.1 in v25_historical is actually 'What Mending Stability Measures', not Approach Training. Canonical content was scattered across 3 different files; consolidated here. Source: 2026-04-25 stress-test 30 propagation defect.]


## 2.2 Diagnosis — STRUCK (ED-134/ED-124, 2026-04-03)



## 2.3 The Leap — Suspending Rendering

> **Foundational reference (canon/02).** The Leap's suspension target (layer 2 reflexive facing), the mechanics of involuntary knot formation, and the operation-type taxonomy (restorative / manipulative / destructive) governing knot-propagation weight are specified in `canon/02_foundations_amendment_leap_mechanism.md` Amendments 1–3. This section's mechanical parameters (eligibility, Contact Duration, retention roll) implement those foundations.

### Eligibility (verify before rolling)

- Approach Training tag ✓
- Thread Sensitivity 30+ ✓
- Not incapacitated (Health > 0) (PP-232 — prior ceiling(Health÷2) threshold removed; incapacitation is binary under current wound system)


### The Leap Roll

**Pool:** (Spirit × 2) + relevant History bonus (points + 3 constant; up to +3D from History level) + Thread Pool Score (TPS = TS ÷ 10, round down) (PP-619, PP-624 — Attunement struck; all Leaps are Spirit-primary)
**TN:** 7
**Ob:** Thread Sensitivity 30–49 = 2 · Thread Sensitivity 50+ = 1

**Wound penalty (universal):** each Wound adds **+0.15 Ob** (cumulative per wound) to the Leap roll — **never a −1D pool cut** (Jordan ruling 2026-07-08, ED-PC-0005; reverses PP-716's −1D). Value calibrated ED-PC-0006: reuses ED-1041's combat "attacking" magnitude (the active-roller case — a Leap has no bilateral attacker/defender split, so the passive-defence +0.25 term does not apply); per `designs/scene/derived_stats_v30.md` §4.1.

> **Einhir framework (P-26):** "Einhir framework" appears as a prerequisite for Locked Zone border Mending (Ob 8+). It requires all three of: 1. **Knowledge:** The practitioner has Diagnosed the Locked Zone's structure (requires a prior Southernmost expedition Diagnosis scene or equivalent scholarly research via Einhir Texts). 2. **Technique:** The practitioner possesses at least one Einhir Text technique applicable to Mending 

Pre-calculate the Leap pool on the character sheet as a named entry separate from History pools.

| Degree | Outcome |
|---|---|
| Overwhelming | Clean suspension. Next Operation's Ob reduced by 1 (minimum 1). Practitioner gains 1 Thread Sensitivity. |
| Success | Rendering suspended. Contact established. Proceed to operation. |
| Partial | Unstable suspension — rendering keeps reasserting. Operation Ob +1. Take 2 Composure strain. |
| Failure | Thread contact fails. −1D to Thread Pool Score for remainder of scene. (PP-232) |


**Failure framing:** The practitioner could not surrender rendering. Their consciousness held on. This is not weakness — it is the fundamental difficulty of doing something that your being resists constitutively. The aftereffect (−1D Thread Pool Score) represents the psychic friction of the failed attempt — the practitioner's engagement with Thread is degraded for the remainder of the scene, not from injury but from the failed surrender itself. (PP-232)

**Thread-Read as fieldwork (cross-reference):** Thread-Read — using a perceptive Leap to gather investigative evidence from Thread configurations — is also defined as a fieldwork investigation action. It is the only fieldwork action that constitutes a Thread operation and fires co-movement. TS ≥ 30 required. Pool: (Spirit × 2) + History + TPS (same as all Leaps — PP-619). See fieldwork_investigation.md §4.5 for the fieldwork Evidence Track context and scope of Thread-derived evidence.

**Fieldwork integration (TW-05, fieldwork_v30 §2.3, §4.5):** Thread-Read fired during fieldwork follows the standard Leap procedure with co-movement firing on all three axes (temporal, epistemic, actualized) per threadwork §3.2. Evidence Track advances when the operation's consequences reveal investigation-relevant information. Per-op cap ruling (TW-05): POP Coherence −1 additional IS subject to per-op cap (total POP Coherence cost = −1 max regardless of scale), unlike FR/Binding Operations which are cap-exempt per PP-196. Thread-Read and FR operations are mutually exclusive within a single fieldwork action (TW-10). Thread-Read Evidence advances are gated to Depth ≥ 4 investigation questions only (P1-16 ruling: prevents Thread-Read from trivializing mundane investigation).

### The First Leap (Event Scene)





### Contact Duration (ED-694: Thread Fatigue replaces Contact Rounds)

**Thread Fatigue** counts up from 0 toward threshold = Spirit × 5 (range 5–35). At threshold: contact breaks involuntarily, cannot re-establish until rested.

**Per-operation fatigue costs:** Leap (entry, one-time) 3. Passive sensing 2/round. Mending 4/round. Pulling 5/round. Locking 7/round. Dissolution 10/round.

**Focus role:** Focus no longer sets contact duration. Focus sets max operations per contact session (Focus − 1). A Spirit 6/Focus 2 practitioner has high endurance but only 1 operation per session. A Spirit 2/Focus 6 practitioner exhausts quickly but can perform up to 5 operations if endurance allows.

**Equipment:** Thread-conductive artifact −1 fatigue/round. Einhir proximity +3/round. Stimulant herbs: threshold +5 temporarily.

**Recovery:** Full rest resets to 0. Meditation reduces by Spirit score.

### Contact Duration (legacy reference)


> **Focus Halving (P-11):** When an environmental effect halves contact duration, round down. Focus 1 after halving = zero operations (experience only). Focus 3 halved = 1 = zero operations. Focus 5 halved = 2 = one operation. Environmental Focus reduction affects contact duration only, not pool calculation — the attribute itself is unchanged.


**Revised standard sequence (Diagnosis precedes Leap):**
- **Round 2+:** Operations proceed as declared.
- **Round (Focus + 1):** Contact drops. Rendering reasserts. Practitioner returns to themselves.

**Operations per Focus:**

| Focus | Contact Rounds (legacy) | Operation Rounds (legacy) | Max Operations (ED-694: this column is the active rule; duration governed by Thread Fatigue) |
|---|---|---|---|
| 1 | 1 | 0 | None. Contact is too brief. Configuration orients and rendering reasserts. The practitioner experiences the suspension but cannot act within it. |
| 2 | 2 | 1 | One operation. |
| 3 | 3 | 2 | Two operations. |
| 4+ | 4+ | 3+ | Three or more. Rare — Focus 4+ requires significant investment. |


**Wound during the Leap round (before contact is established):** If the practitioner takes a Wound in the same round as the Leap roll, before the roll is resolved, the normal wound penalty falls on the Leap roll — +0.15 Ob per Wound (ED-PC-0005/ED-PC-0006), not a −1D pool cut. The Attunement disruption check does not apply — it only triggers once contact is established. If the Leap succeeds despite the Wound penalty, contact proceeds normally.

**Incapacitation during contact:** If a Wound incapacitates the practitioner during contact (Wounds reach or exceed the incapacitation threshold: ceiling(Health ÷ 2)), contact terminates immediately regardless of the Attunement disruption check result. The operation in progress is treated as a Failure. The practitioner returns to rendering incapacitated.

**Wound disruption during contact:** When the practitioner takes a Wound while contact is established, make a Spirit check immediately: Spirit score in d10s, TN 7, Ob 1. Failure: rendering reasserts violently — the body's damage overrides the suspension. Contact drops. (PP-624: corrected from Attunement. Maintaining Thread-state suspension against physical disruption is Spirit's function — metaphysical grounding while engaged — not Attunement's social/perceptual calibration.)

### Thread Operation Visibility


| Observer Thread Sensitivity | Perception |
|---|---|
| 0–9 | Nothing perceived |
| 10–29 | Vague unease; cannot locate source |
| 30–49 | Senses an operation in the scene; general direction identifiable |
| 50–69 | Identifies operation type and approximate target |
| 70+ | Perceives the full configuration being worked |

Physical effects (a wound closing, an object moving) are visible to all.

**Concealing from Thread Sensitivity 30+ observers:** Roll Cognition only (no History), TN 7, Ob = observer's Thread Sensitivity ÷ 30 (round up). This is a pre-Leap action — concealment is set before rendering suspends. The practitioner shapes how their configuration presents during contact, but cannot adjust concealment during contact itself.

**Wound penalties:** each Wound adds **+0.15 Ob** (cumulative) to all Thread operation rolls — Leap, Weaving, Pulling, Mending, FR — **never a −1D pool cut** (Jordan ruling 2026-07-08, ED-PC-0005; reverses PP-716; value calibrated ED-PC-0006 from ED-1041's combat "attacking" magnitude; per `designs/scene/derived_stats_v30.md` §4.1). The body's damage impedes the suspension.

### Rendered-Level Thread Event Visibility (ED-677)

Extension of the above table to rendered-level events — not practitioner operations but the thread events that combat, death, and substrate instability constitute:

| Observer TS | Combat Wound | Death | Mass Casualty | Gap Manifestation | Rendering Crisis |
|---|---|---|---|---|---|
| 0–9 | Normal perception | Normal grief | Normal horror | Nothing | Vague wrongness |
| 10–29 | Vague unease | Loss beyond grief | Deep wrongness; nightmares | Unease near site | Overwhelming wrongness |
| 30–49 | Thread disruption at wound | Configuration ceasing to cohere | Mass disruption; direction identifiable | Absence; Gap partly readable | Full crisis visible |
| 50–69 | Wound depth (surface vs structural) | Full thread-state dissolution | Scope/casualties through substrate | Full Gap: original config reconstructible | Crisis cause identifiable |
| 70+ | Complete structural perception | Dying configuration's complete state | Every individual disruption perceivable | Full forensic + temporal trace | Can intervene (Anchoring assistance) |

No mechanical changes. Provides narrative and investigative information. Supplements fieldwork_v30 §4.5 Thread-Read evidence quality.

## 2.4 Operations During Contact





### Weaving — Things Cohere

> **Design note (ST-TW-01):** W-24 (Coherent Strike) at Object scale: Mending Stability unchanged, Coherence −0 on Success. If Leap round is protected (opponent at wrong range), operation is free in Thread terms. Design question: is this intended? See ED-046.



**Pool:** (Spirit × 2) + relevant History bonus + Thread Pool Score (PP-616, PP-625)
**TN:** 7

**Ob by scale (Thread Sensitivity minimum required):** *(Pre-PP-622 single-axis scale — canonical: params_threadwork.md §Three-Axis Ob System.)*

| Scale | Example | Ob | Min Thread Sensitivity |
|---|---|---|---|
| Object | Close a wound; reinforce a cracking blade | 1 | 30+ |
| Personal | Stabilise a dying character; accelerate injury healing | 2 | 30+ |
| Relational | Bind a diplomatic agreement; reinforce trust | 3 | 50+ |
| Territorial | Raise a faction's Stability by 1; stabilise a region | 4 | 50+ |
| Structural | Permanent reinforcement of a fortification or institution | 5 | 70+ |

| Degree | Outcome |
|---|---|
| Overwhelming | Full effect. Mending Stability +1 (Relational scale or above only). Practitioner gains 1 Thread Sensitivity. The effect exceeds the stated intention — the wound closes without scarring; the agreement develops genuine trust beyond its terms. |
| Success | Full effect. Mending Stability unchanged. |
| Partial | Partial effect (engine sets scope). Mending Stability −1. Coherence −1. |
| Failure | Interaction collapses. Mending Stability −2. Coherence −1. At Mending Stability ≤ 40: Shifting Object forms. At Mending Stability ≤ 20: Gap opens. |

**Over-Actualisation Hazard (Relational+ scale):**


| Scale | Over-Actualisation Consequence on Success |
|---|---|
| Object / Personal | None. |
| Relational | Subsequent Thread operations targeting this same configuration: +1 Ob. Clears after one season or when the configuration is Pulled. |
| Territorial | As Relational, plus: Diagnosis on this configuration +1 Ob. |
| Structural | As Territorial, plus: +1 Mending Stability degradation per season it persists (the rigid configuration obstructs substrate traffic). |

On Overwhelming at Relational+: over-actualisation effects halved in duration.

**Over-Actualisation through State Transitions (PP-208):** OA modifier does NOT carry through brittleness collapse to Shifting Object. A Shifting Object is a new configuration — OA accumulated on the prior stable configuration is lost. Exception: if a Mending operation targets a thread that is still in its original Woven state (i.e., has not collapsed), OA modifiers from prior Weavings of that thread still apply.







**Overweaving:** Each operation after the first in the same contact window: +1 Ob (cumulative). A collapsed overweave: Mending Stability −3 and local Shifting Object risk.

### Pulling — Things Open


> **Fortification Ob addition (R-67):** When Pulling a structural/territorial configuration that includes a fortified site (Fortification ≥ 1):
add the Fortification level to the Ob. Physical reinforcement increases actualization.
Apply to §2.4 Pulling, Foundational/Structural scale section.



**Pool:** (Spirit × 2) + relevant History bonus + Thread Pool Score (PP-616, PP-625)
**TN:** 7

**Ob by actualization level:** *(Pre-PP-622 single-axis scale — canonical: params_threadwork.md §Three-Axis Ob System.)*

| Actualization | Example | Ob | Min Thread Sensitivity |
|---|---|---|---|
| Loosely actualised | Thread already drifting | 1 | 30+ |
| Normally actualised | Standard state | 2 | 30+ |
| Firmly actualised | Strong configuration, deliberate or old | 3 | 50+ |
| Previously Woven | Another practitioner's work resists | 4 | 50+ |
| Foundational | Deep structural thread | 5 | 70+ |

**Duration by surplus successes:** 0 = end of scene. 1 = end of session. 2+ = until next seasonal accounting.

> **Correction (R-54):** Duration ladder shifted (Pull requires re-application at scene scale):
- 0 surplus successes = 3 rounds (was: end of scene)
- 1 surplus success = end of scene (was: end of session)
- 2+ surplus = end of session (was: until next seasonal accounting)
- 3+ surplus = until next seasonal accounting
Apply to §2.4 Pulling — Past-Oriented Pulling duration table.

| Degree | Outcome |
|---|---|
| Overwhelming | Full effect. Extended duration. Mending Stability unchanged. |
| Success | Full effect. Standard duration. Mending Stability unchanged. |
| Partial | Partial effect or reduced duration. Mending Stability −1. Coherence −1. |
| Failure | Snap-back. 1 Wound (armour does not apply). Mending Stability −2. Coherence −1. |

### Past-Oriented Pulling

**[ED-WR-0007, 2026-07-08 — pessimist-action audit DISTILL (design-merit call, Jordan's to ratify).** Past-Oriented Pulling is a **temporal-target variant of Pulling**, not a structurally separate operation. Its "Ob by recency" table is a standalone recency axis un-integrated with the canonical Three-Axis Ob System (Depth/Breadth/Distance) every other operation uses, with no stated interaction rule (does a POP target also carry Depth/Breadth Ob?) — a Q-smooth "methodology matches governing subsystem" fail. The DISTILL folds POP into Pulling as a temporal target governed by an explicit fourth axis (or a Distance-axis reinterpretation for temporal targets) *inside* the Three-Axis system, rather than a separately-TN'd operation with a parallel recency table. The capability — reaching into the past; grief/legacy as political weight — is **not cut**, only simplified into the one Ob system every operation already shares. Physical fold lands with the per-op cost-table work (resolution_plan C-TW-3/4/10/11, Stratum B); the recency table below is retained as the parameter reference until then.]

**Pool:** (Spirit × 2) + relevant History bonus + Thread Pool Score (PP-619, PP-625 — TPS÷2 struck; full TPS always; TN+1 already encodes temporal-depth difficulty)
**TN:** 8 (Binding temporal depth — POP targets past configurations)

**Ob by recency:**

| Recency | Ob |
|---|---|
| Same scene/session | 3 |
| 1–2 seasons | 4 |
| 3–5 seasons | 5 |
| 6–10 seasons | 6 |
| 10+ seasons / generational | 7 |

*All existing mechanics (Ob by recency, degree table, Thread Tension/Mending Stability consequences, Fraying Bane) retained with Mending Stability replacing Thread Tension throughout. Mending Stability costs inverted: where Thread Tension was +3 minimum, Mending Stability is −3 minimum.*

**Additional Ob modifier — active Knot Crisis:** If the target event has caused an active Knot Crisis in any character (the death is still being grieved, the loss is still raw), add +1 Ob. The ongoing relational weight of the grief makes the temporal thread more firmly actualised — living sorrow has woven itself into the thread's current configuration and resists displacement.

### Locking — Unable to Become

> **Mending Stability drain cap (R-58):** Regardless of concurrent active Locks: Mending Stability drain from Locks cannot exceed −1/round in combat
Apply to §3.2 Coherence Reduction / Loc


**Requirements:** Thread Sensitivity 50+
**Pool:** (Spirit × 2) + relevant History bonus + Thread Pool Score (PP-618, PP-625)
**TN:** 8 (PP-619 — Binding Operations)
**Minimum Ob:** Struck (PP-623). Three-axis Ob: see params_threadwork.md §Three-Axis Ob System.

*(Pre-PP-622/PP-623 Ob table — struck; retained for patch history only:)*

| Scale (STRUCK) | Old Ob |
|---|---|
| Object | ~~4~~ |
| Personal | ~~5~~ |
| Relational / Process | ~~6~~ |
| Territorial | ~~7~~ |
| Structural / Foundational | ~~8+~~ |

**Thread Sensitivity 70+ Tier Reduction:** −1 to all FR Mending Stability costs (minimum 1).

| Degree | Outcome |
|---|---|
| Overwhelming | Target permanently locked. Mending Stability −1. Practitioner gains 1 Thread Sensitivity. |
| Success | Target locked. Mending Stability −1. |
| Partial | Partial lock (engine sets scope). Mending Stability −2. Coherence −1 (cap). |
| Failure | Collapse onto practitioner. Take 2 Wounds (no armour). Mending Stability −3. Coherence −1 (cap). Adjacent configurations become partially rigid: +1 Ob to all Thread operations targeting configurations adjacent to the failure site, remainder of season. |

**Chronic consequences:**

| Duration | Effect |
|---|---|
| 1 season | No additional effect. |
| 2–3 seasons | Mending Stability −1/season (substrate strain from blocked configurational traffic). +1 Ob to operations targeting Lock or adjacent configurations. |
| 4+ seasons | Mending Stability −2/season. Operations targeting any configuration in the same zone: +1 Ob (the frozen thread occludes Diagnosis, degrading intentionality for subsequent operations). |
| Permanent (never reversed) | Substrate adapts. Mending Stability drift ceases. Permanent +1 Ob to adjacent operations. This is how Locked Zones form. |

> **Variable Mending Stability drift (R-63):** Replaces uniform −1 Mending Stability/season for locked institutions:
- Slow-change domain (seasonal/yearly evolution): −1 Mending Stability/season
Engine determines domain type when Lock is applied.

**Reversing a Lock:** Pulling at Ob = (original practitioner's Thread Sensitivity ÷ 10, round up) − 2, minimum Ob 1. Successful release: Mending Stability +1 per season the Lock persisted (max +5), as the substrate decompresses.

**Dissolution of a Lock:** Tears the locked configuration rather than unwinding it. No Mending Stability release bonus (unlike Pulling — the configuration was torn, not cleanly unwound). Dissolution of a Permanent Lock (4+ seasons, substrate adapted) automatically fails — the configuration no longer exists as a discrete target; it has become part of the substrate's structure. Permanent Locks can only be addressed via the Einhir framework. A novice Lock (Thread Sensitivity 30) is trivially reversible (Ob 1); an expert Lock (Thread Sensitivity 100) requires a specialist (Ob 8). Long-standing Lock release: Mending Stability +1 per season the Lock persisted (max +5). If 4+ seasons: Shifting Object risk from sudden configurational release.

### Dissolution — Unable to Be



**Requirements:** Thread Sensitivity 50+
**Pool:** (Spirit × 2) + relevant History bonus + Thread Pool Score (PP-618, PP-625)
**TN:** 8 (PP-619 — Binding Operations)
**Minimum Ob:** Struck (PP-623). Ob: see params_threadwork.md §Three-Axis Ob System.

*(Pre-PP-622/PP-623 Ob table: same as Lock above — also struck.)*

| Degree | Outcome |
|---|---|
| Overwhelming | Target dissolves cleanly. Mending Stability −3. Micro-Gap forms and closes within the scene. |
| Success | Target dissolves. Mending Stability −5. Gap forms, lasts one scene, closes. |
| Partial | Target becomes a Shifting Object. Mending Stability −6. Gap does not close without Mending. Coherence −1 (cap). |
| Failure | Full Gap tears open. Mending Stability −8. Monstrous Incursion immediately. Practitioner Incapacitated. Coherence −1 (cap). |

**Lock vs. Dissolution summary:**

| Dimension | Lock | Dissolution |
|---|---|---|
| What it does | Freezes the intelligible face | Tears the intelligible face away |
| Temporal character | Chronic (damage accumulates) | Acute (damage immediate) |
| Mending Stability consequence | Lower immediate (−2 to −4), chronic drift (−1 to −2/season) | Higher immediate (−3 to −8), no drift |
| Gap risk | None on success; stiffening on failure | Always |
| Core violation | Unable to become | Unable to be |

> **Chronic perception (P-13):** *Already patched into §2.7 chronic table.* The frozen thread's perceptual occlusion manifests as +1 Ob to the operation (degraded intentionality from impaired Diagnosis), not to Diagnosis itself (which has no Ob).

### Mending — Repairing the Substrate

> **[ED-WR-0007, 2026-07-08 — pessimist-action audit REFINE (design-iteration flag, Jordan's call; the zero-cost ruling is explicitly NOT touched).** Mending is the *only* legal repair tool for its target class (Gap / Shifting-Object / Locked-Zone border — Weaving/Pulling/Locking/Dissolution cannot target these), it is Coherence-free and unopposeable (Mending Immunity), and collective/Einhir "approaches" are the *same operation at scale*, not distinct tools. So the single most world-track-consequential decision in the lane — whether/when/how hard to repair the substrate — has no real branching: it is one tool plus a strictly-dominated "leave it, pay the Gap Self-Closure RS-drain" fallback, which fails Q-robust's "three viable approaches" bar. The REFINE does **not** change the zero-Coherence-cost value (canon/02 Amendment 3 + ED-871 — a load-bearing restorative/manipulative/destructive asymmetry): it flags, for Jordan, that Gap-repair needs a genuine second branch or scarcity/opposition dimension (e.g. an opposeable variant in contested/Church-adjacent territory, or RS-drain tuning that makes "let it self-close" a real choice). Design-merit call, not a mechanical fix this audit resolves.]

> **Foundational reference (canon/02).** Mending's zero Coherence cost is a structural consequence of its alignment with substrate tendency (restorative operation type); it is not a mechanical exception. See `canon/02_foundations_amendment_leap_mechanism.md` Amendment 3. Warden Coherence erosion is environmental (proximity to Gaps, dissolution residue, third-mode presences) and is not a function of Mending operations themselves.

> **Correction (R-56):** Healing operations (W-08 and variants) use accelerated Overweave: each healing operation in the same contact window adds +2 Ob (not +1). Sequence: 1st heal Ob 1, 2nd Ob 3, 3rd Ob 5, 4th Ob 7.

> **W-33 note (P-31):** W-33 is effective only for units with CP ≥ 3. A rallied unit with CP ≤ 2 will have an effective combat pool of 0 despite Discipline restoration — the Discipline penalty from Discipline 2 eliminates the entire pool at low CP values. W-33's primary use case is Professional or Elite infantry (CP 3+) that has broken under morale pressure while retaining Strength.



**Requirements:** Thread Sensitivity 50+ · Target must be a Gap, Shifting Object, or Locked Zone border
**Pool:** (Spirit × 2) + relevant History bonus + Thread Pool Score (PP-616, PP-625 — Attunement and Focus struck from pool dice; Focus still governs Contact Rounds)
**TN:** 7

**Design note (PP-616, PP-625):** Mending uses the same pool as all other Thread operations: (Spirit × 2) + History + TPS. The prior Attunement + Focus construction is struck. Spirit is the metaphysical attribute for all Thread contact — this applies whether the operation targets a thread (Weaving, Pulling, Locking) or the substrate's absence (Mending). Focus continues to govern Contact Rounds (duration), not pool dice. Ob table below predates PP-622; canonical Mending Ob: params_threadwork.md §Three-Axis Ob System (Mending Ob = Depth Ob − 1 + age modifier + Breadth + Distance).


**Ob by Gap severity:**

| Gap Type | Ob | Min Thread Sensitivity |
|---|---|---|
| Shifting Object (pre-Gap) | 2 | 50+ |
| Micro-Gap (same scene) | 3 | 50+ |
| Standard Gap (1 session – 1 season) | 5 | 50+ |
| Entrenched Gap (1+ seasons) | 6 | 70+ |
| Catastrophic Gap (3+ seasons) | 7 | 70+; requires Einhir framework or collective operation |
| Locked Zone border | 8+ | 70+; requires Einhir framework |

**Design note — Catastrophic Gaps and Locked Zones:** These are Calamity-tier damage. Solo Mending at Ob 7–8 is intentionally near-impossible (~40–58% even at maximum pool). These sites require collective operations, the Einhir framework, or multi-season Mending arcs. This is the Einhir Catastrophe's legacy made mechanical: the damage they caused cannot be reversed by a single practitioner acting alone.

| Degree | Outcome |
|---|---|
| Overwhelming | Substrate restored. Gap closes cleanly. Mending Stability +2 (strain released). Coherence: 0 (Mending is aligned work — no rendering damage). Mended area +1 Ob to future Gap formation in this zone for 1 season. |
| Success | Substrate restored. Gap closes. Mending Stability +1. Coherence: 0. |
| Partial | Gap reduced one severity category. Mending Stability unchanged. Coherence: 0. Second Mending required. |
| Failure | Mending fails. Gap unchanged. Coherence: 0. Mending Stability −2. |

**Mending Coherence Asymmetry:** Mending never costs Coherence. A practitioner who Mends is restoring the substrate's intelligible face — working with the rendering, not against it. This is the philosophical distinction between Mending and all other Thread operations: Pull, Weave, Lock, and Dissolution all suspend the practitioner's own rendering (layer 2) to act on another thread's rendering. Mending does not suspend — it supports. The practitioner's rendering is continuous throughout. This is why the Edeyja can Mend indefinitely without personal degradation, and why Mending is the only Thread operation that is unconditionally good for the world.

**Seasonal Mending Fatigue:** Each consecutive Mending in the same season (not scene — season) adds +1 Ob cumulative. A practitioner who Mends 4 times in one season rolls the fourth at +3 Ob. Resets each season. The work is tiring, not corrosive — a surgeon can operate all day without moral injury, but their hands get tired.

**Mending co-movement profile:**


*Epistemic auto-effect (by degree):*

| Degree | Epistemic Effect |
|---|---|
| Overwhelming | Strong settling. Thread Sensitivity 10+ observers perceive the area as markedly calmer. Non-sensitives notice a distinct easing of tension. |
| Success | Settling. Thread Sensitivity 10+ observers perceive calming. Non-sensitives may notice subtle easing. |
| Partial | Ambiguous. Observers perceive both settling and tension — something shifted but didn't fully resolve. |
| Failure | Increased tension. Observers perceive things worsening. Non-sensitives feel heightened unease. The substrate was disturbed without being repaired. |

No investigation Ob modifiers on Success or Overwhelming — Mending resolves epistemic instability rather than producing it. On Partial or Failure: +1 Ob to social rolls in the immediate area for the remainder of the scene.

*Actual (d6):*

| d6 | Effect |
|---|---|
| 1 | Dissolution residue at the Mending site |
| 2 | Nearby threads settle into slightly different configurations (minor Shifting Object risk in adjacent zone; self-corrects in 1d3 days) |
| 3 | Temperature/light/sound shift at site (Thread Sensitivity 10+ detectable) |
| 4 | Mended area retains a trace — Thread Sensitivity 30+ perceive a scar in the substrate for 1 season |
| 5 | Adjacent thread realigns, producing an unexpected minor benefit (engine surfaces) |
| 6 | Full closure delayed 1d3 scenes |

## 2.5 Collective Operations




**Collective Leap procedure:** All practitioners roll their own Leap in the same round (Priority 5). If the Anchor fails: the collective lattice does not form. Helpers who succeeded are in individual contact (their own Focus windows) but pool their dice to no one — each may perform individual operations at their own Ob, without collective bonuses. If the Anchor succeeds but helpers fail: subtract their contributed dice; if remaining pool drops below half the Anchor's solo pool, apply +1 Ob (lattice fracture). If all fail: all take individual Leap failure consequences.

**Anchor:** Highest Thread Sensitivity practitioner. Sets the primary intentionality. Rolls their full operation pool.

**Helper contribution:** Each assisting practitioner contributes **floor(Cognition ÷ 2)** bonus dice to the Anchor's pool. Each helper must have their own active contact window.

**Constraints:**
- Helpers cannot Fork; Anchor cannot Fork when acting as Anchor.
- If a helper's contact drops (rendering reasserts) before the roll: remove their contributed dice. If total pool drops below half the Anchor's solo pool: +1 Ob (the lattice fractures — one configuration reasserted its rendering and disrupted the interaction).
- Conflicting Beliefs: if a helper's Belief is tangentially conflicting (relevant tension but not direct opposition), their dice cannot chain on 10 — their intentionality is misaligned, limiting coherence. If a helper's Belief **directly opposes** the operation's declared goal, the helper must pass a pre-Leap Belief check (Spirit TN 7 Ob 1) to suppress their opposing intentionality enough to align with the Anchor. Failure: the helper cannot align and drops out before the Leap. Success: participates with non-chaining dice.


---

## 2.6 Opposing Operations — Contested Intentionality




### Opposing Engagement Modifier

Each practitioner's Ob is increased by +floor(opponent's Thread Pool Score ÷ 2), minimum +1.

| Opponent Thread Pool Score | Modifier |
|---|---|
| 3 (Thread Sensitivity 30–39) | +1 |
| 4–5 (Thread Sensitivity 40–59) | +2 |
| 6–7 (Thread Sensitivity 60–79) | +3 |
| 8–9 (Thread Sensitivity 80–99) | +4 |
| 10 (Thread Sensitivity 100) | +5 |

The opponent's configuration drives the thread in the opposite direction during contact. Their perceptual depth (Thread Pool Score) determines the resistance they create. This is rendered-side resistance (P-07). Stacks with all other Ob modifiers.

### Resolution Table

Both roll their operation pools against modified Obs.

| A's Result | B's Result | Thread Outcome | Mending Stability | A's Consequences | B's Consequences |
|---|---|---|---|---|---|
| Meets Ob | Meets Ob | **Shifting Object** at target's scale | Worst single degree-table Mending Stability cost + 1 | Coherence per §3.2. Knot strain: +1 Ob next Thread op this scene, 2 Composure. | Same. |
| Meets Ob | Partial | **A's operation resolves.** Overwhelming degrades to Success; Success unchanged. | A's degree-table Mending Stability cost + 1 | Coherence per §3.2. 1 Composure. | Coherence per §3.2. Knot strain: +1 Ob, 2 Composure. No degree-table consequences. |
| Meets Ob | Failure | **A's operation resolves at achieved degree.** No contest. | A's degree-table Mending Stability cost | Normal. | Standard Failure per degree table. |
| Partial | Partial | **Weak oscillation.** d6: 1–2 = Shifting Object one scale below. 3–6 = none. | −1 | Coherence per §3.2. Knot strain: +1 Ob, 2 Composure. | Same. |
| Partial | Failure | **A's Partial resolves.** | A's Partial Mending Stability cost | Normal Partial. | Standard Failure. |
| Failure | Failure | **Nothing resolves.** | −1 | Coherence per §3.2. 1 Composure. | Same. |


### Knot Strain

| Scenario | Losing/Tied Practitioner | Winning Practitioner |
|---|---|---|
| Standard (Weave/Pull) | +1 Ob next Thread op this scene. 2 Composure. | 1 Composure. |
| FR (Lock/Dissolution) | +2 Ob. 4 Composure. If winner Dissolved: +1 Wound (tear through knot; no armour). | 2 Composure. |
| Both meet Ob (tie) | Both: +1 Ob, 2 Composure. (FR: +2 Ob, 4 Composure.) | N/A |
| Both fail | Both: 1 Composure. | N/A |

Composure restores at scene change. Ob penalty expires after next Thread operation or at scene end.

### Co-Movement

Coherence fires per-practitioner per §3.2 (each suspended their own layer 2). Epistemic and actual effects fire ONCE for the compound event — one disturbance on one thread. If one operation won: use that operation's co-movement profile. If Shifting Object formed: epistemic = observers perceive oscillation (+1 Ob social rolls at site, remainder of scene); actual = roll once on the Weaving actual table.

### FR vs FR Both-Fail Scaling

| Scale | Mending Stability Cost | Shifting Object Risk (d6) |
|---|---|---|
| Object | −1 | 1 = 17% |
| Personal | −2 | 1–2 = 33% |
| Relational | −3 | 1–3 = 50% |
| Territorial | −4 | 1–4 = 67% |
| Structural | −5 | 1–5 = 83% |

Both practitioners: +2 Ob, 4 Composure.

### Sustained Opposition

Pre-declared operations in subsequent rounds: +1 Ob sequential failure penalty if target state changed. Knot strain Ob stacks with sequential penalty. A Shifting Object receiving a second Shifting Object from opposing operations advances one deterioration tier (1d3 seasons → 1d3 sessions → end of scene).

### N-Way Opposing Operations (3+ Practitioners)

Three or more practitioners with at least two genuinely opposing intentionalities on the same configuration: automatic lattice collapse. All operations fail. Gap forms at target's scale. Mending Stability −(2 × number of opposing practitioners). All: Coherence per §3.2; knot strain +2 Ob, 4 Composure.

### Combat Timing




# PART THREE: COHERENCE (10→0)

## 3.1 What Coherence Measures




**Range:** 10 (fully coherent) → 0 (rendering crisis).
**Starting value:** 10 (all practitioners). Non-practitioners do not track Coherence.

## 3.2 Coherence Reduction



| Source | Coherence Loss |
|---|---|
| Object or Personal scale operation | 0 (co-movement fires but practitioner's rendering absorbs negligibly) |
| Relational scale operation | −1 |
| Territorial scale operation | −1 |
| Structural scale operation | −2 |
| FR Lock or Dissolution (any scale) | −1 additional (Lock minimum total: −2; Dissolution minimum total: −2) |
| Past-Oriented Pulling | −1 additional on top of standard Pulling cost |
| Mending | 0 (restorative operation type — ED-871 / canon/02_foundations_amendment_leap_mechanism.md Amendment 3; operation-type, not scale, determines Coherence risk. Matches this doc's own §2.4 Mending degree table. Sim `sim/thread/operations.py` still charges −1/−2 — SIM-CODE fix deferred to Stratum B, entangled with the C-TW-3 blanket-penalty bug and lacking test coverage) |
| Dissolution residue use (per use) | −1 additional (on top of operation cost) |
| History Resonance risk die (shows 1) | −1 |
| Practitioner Flashback anchoring (engine trigger) | −1 |
| Extended proximity to Structural-scale Gap | −1 per season |


> **FR surcharge cap exemption (PP-196):** [PROVISIONAL — canon: §1.1 Inseparability, P-01] The Forced Resolution (FR) surcharge (−1 Coherence additional for Lock or Dissolution) is **exempt from the §3.2 per-operation cap.** FR operations are deeper ontological violations than Pull or Weave: Lock drives actuality to total actualization (preventing becoming); Dissolution tears the intelligible face (preventing being). The inseparability principle requires that this greater ontological depth register differently at the personal track, not be flattened by a general cap. Consistent with: Dissolution residue use is already cap-exempt (§3.4). **Revised Coherence costs for FR:**
- FR Lock or Dissolution at Object/Personal scale: −1 total (FR surcharge only; scale cost = 0, but FR surcharge applies and is not capped).
- FR Lock or Dissolution at Relational scale: −2 total (−1 scale + −1 FR; cap does not suppress the FR surcharge).
- FR Lock or Dissolution at Territorial scale: −2 total (same as Relational).
- FR Lock or Dissolution at Structural scale: −3 total (−2 scale + −1 FR).
The §3.2 per-operation cap still governs non-FR operations.


## 3.3 Coherence Thresholds

| Coherence | State | Effects |
|---|---|---|
| 10–8 | Stable | No penalty. Rendering solid. The world is legible. |
| 7–5 | Dissonant | Narrative flickers: wrongness, déjà vu, events slightly out of sequence. Close Knots sense wrongness (+1 strain per 3 sessions). |
| 4–3 | Fragmented | −1D to all social rolls. −1D to Recall-based rolls. (PP-234) Engine may present the character's recollection differently from what others remember. All Knots at wrongness pace (+1 strain per 2 sessions). +1 Ob on all Thread operations including the Leap roll (rendering reasserts more aggressively, making suspension harder). Roll Fragmented Fallout on entering this band. |
| 2 | Fractured | −2D to all social rolls. −2D to Recall-based rolls. (PP-234) All Knots at accelerated wrongness (+1 strain per session). Once per scene with Thread operation: Spirit TN 7 Ob 1 or lose 1 round to a dissociative episode. Certainty maximum reduced by 1 per Coherence level below 3. **Belief Co-Authorship begins:** Engine presents the practitioner's shifting perceptual framework as the character's internal voice. Player must rewrite each Belief to reflect the framework in which the categories that structure consciousness are loosening. Roll Fractured Fallout on entering this band. |
| 1 | Severed | −2D social, −2D Recall. (PP-234) Dissociative episodes once per scene regardless of operations (fire at scene start, not mid-operation). Involuntary perceptual events. All Knots +2 strain per session. +2 Ob on all Thread operations including the Leap (rendering barely holds; suspension is constitutively dangerous). The practitioner's rendering is barely functional. The distinction between self and world, between human and monstrous, between actual and potential, is dissolving. Not because something evil is happening to them. Because they have been outside rendering so many times that rendering no longer holds. |
| 0 | Rendering Crisis | Campaign event. Reality as commonly rendered is no longer accessible. The practitioner's spooling is destabilised — their organic drawing-from-ground is compromised. They must resolve the crisis narratively: sustained engagement with the world's rendered state, relational anchoring, or withdrawal from practice. If unresolved by season end: Non-Player Character. |


## 3.4 Dissolution Residue

*Replaces §5.10 (Taint track) and §5.11 (Dissolution Residue). No separate Taint track.*

Dissolution residue is compressed potential oriented toward the unintelligible ground. A practitioner may draw on it during an operation: add bonus dice equal to Potency rating (1–5) to the operation pool. These dice explode on 9–10 (volatile).

**Cost:** −1 Coherence per use (additional, on top of the operation's normal Coherence cost). Maximum one use per contact window. Same source: +1 Ob per prior use (depletion).

**Coherence cap interaction:** Residue use is a distinct Coherence event from the operation itself and is not subject to the §3.2 cap. At Object or Personal scale (base operation cost = 0): residue use costs −1 Coherence — the only cost of the operation. At Relational+ scale (base operation cost = −1, already capped): the cap absorbs the residue cost — total remains −1. In practice: residue use has a real Coherence cost when the operation would otherwise be free (Object/Personal), and no additional cost when the operation already costs −1 (Relational+). This preserves the philosophical weight — engaging with residue at shallow scale still pushes the practitioner deeper into beyond-rendering states — without stacking costs at the scales where the cap already governs.




## 3.5 Recovery


- **Full season of non-practice (no Thread operations):** +1 Coherence. Spooling reasserts when the practitioner stops suspending it.
- **A Close Knot voluntarily anchoring through a dedicated Anchoring Scene (Bonds check TN 7, Ob 2):** +1 Coherence. The shared thread of being — the relational spooling — helps stabilise rendering. Costs the Knot +1 strain.
- **Certain Einhir techniques (engine permits late-campaign):** +1 Coherence.
- **Cannot exceed 10. Cannot be purchased with CP.**

## 3.6 Fallout Tables

*Retained from current system.*

**Fragmented Fallout (d6):**
1. You vividly remember a conversation others recall differently
2. A specific skill-memory requires Memory check Ob 2 to access correctly
4. Someone you have not seen recently feels as though you just spoke to them
5. Something you said this session feels like it was said last session
6. A Knot's emotional valence briefly reverses

**Fractured Fallout (d6):**
2. Your most recent History advancement feels uncertain — borrowed, not learned
3. A named Knot briefly does not recognise you, or vice versa. Lasts one scene.
4. You perform an action you do not remember. Engine describes the gap.
5. Your Inspiration refresh this scene feels already spent
6. A Belief reads, briefly, as belonging to someone else

---

## 3.7 Rendering Crisis Resolution (PP-194) [PROVISIONAL]


**Minimum conditions:**
1. Full season withdrawal from Thread practice (no Leap, no Thread operations).
2. Three Anchoring Scenes with Close Knots (each: Bonds check TN 7, Ob 2; failed scene costs the scene without progress).

**Resolution attempt** (at Accounting after conditions met):
Pool: highest Close Knot's Bonds score + number of successful Anchoring Scenes, TN 7, Ob 3.

| Degree | Outcome |
|--------|----------|
| Overwhelming | Coherence → 4. Functional. Permanent −1 Thread Sensitivity. |
| Success | Coherence → 3 (Fragmented). Minimally functional. −1 Thread Sensitivity. |
| Partial | Coherence → 1 (Severed). Another full-season arc required for further recovery. |
| Failure | No recovery. Practitioner becomes Non-Player Character at season end. |




> **GM guidance — TS 30-31 Rendering Crisis risk (PP-206):** [PROVISIONAL] Before a practitioner with Thread Sensitivity 30 or 31 begins the Rendering Crisis arc (PP-194), the GM must inform the player: Success or Overwhelming results permanently reduce Thread Sensitivity by 1. At TS 30, this reduction yields TS 29 — below the Leap minimum. The practitioner survives the crisis but loses Thread ops permanently. This is intended. Surface this before the arc begins so the player makes an informed choice: attempt resolution (risk losing Thread access) or accept NPC status directly.


### Rendering Crisis — Narrative Structure (ED-681)

For videogame implementation, the mechanical checklist above unfolds as four designed beats:

**Beat 1 — Withdrawal:** The practitioner cannot sustain normal rendering. Colors desaturate. Sounds echo. NPCs' words arrive with delay. The practitioner perceives the thread-substrate without the rendering filter. No rolls — pure narrative. Companion Commentary fires if companion present (bridge_part1_revisions B.3.3).

**Beat 2 — Knot Anchoring:** A Close Knot NPC arrives. The practitioner perceives them simultaneously as rendered person and thread-configuration. Mechanical: Spirit check TN 7 Ob 1. Success: Coherence +1. Failure: NPC receives Knot Strain +1.

**Beat 3 — Place Anchoring:** The practitioner visits a location with personal significance (from character_histories_v30 lifepath). The place's familiar configuration provides rendering reference. Mechanical: Spirit check TN 7 Ob 2. Success: Coherence +1. Failure: involuntary Thread-Read fires (co-movement applies).

**Beat 4 — The Choice:** The practitioner confronts epistemic seduction (A11): do I want to return to rendering? Full substrate perception — the world as it is, not as rendering presents it. This IS the resolution roll. Pool: Spirit + Focus, TN 7, Ob 2. Overwhelming: +2 Coherence, −1 TS. Success: +1 Coherence. Partial: no change. Failure: no recovery; Coherence floor at current value for 1 additional season.

The crisis is not punishment. It is the practitioner's existential season.

> **TS 90+ Coherence 0 — Reality Strain MS cost (PP-197):** [PROVISIONAL — canon: Amendment 01 §Resonant] A practitioner who reaches Coherence 0 with Thread Sensitivity 90+ is undergoing Structural-scale self-maintenance threadwork at every moment (per Amendment 01: they substitute layer 3 for failed layer 2). This continuous Structural-scale threadwork strains the substrate exactly as the Einhir site-network did, localized to their presence. **MS cost:** −1 MS per scene in which the practitioner is actively maintaining their existence (any scene in which they are conscious and present). This cost fires at scene end, not at Accounting — it is immediate and continuous. The practitioner need not perform any deliberate Thread operations for this cost to apply; their existence is the operation. This cost is separate from and stacks with all other MS degradation sources. For TS 30–69 practitioners at Coherence 0: no reality strain MS cost (insufficient Thread Sensitivity for layer 3 self-maintenance at the required depth — they are in ontological freefall, not self-maintenance). For TS 70–89: −1 MS per session (not per scene — Structural-scale self-maintenance is possible but less continuous than Resonant). Apply during Rendering Crisis arc and after, if the practitioner remains at Coherence 0.



---

# PART FOUR: CO-MOVEMENT (VERSION C)

## 4.1 Core Principle

Co-Movement is constitutive, not incidental. When a practitioner operates on Thread, they intervene in the substrate from which all being is rendered (A1). The substrate is not a mechanism with predictable outputs — it is constitutive ground, the condition of possibility for things to appear as they do. An operation that alters one configuration necessarily disturbs adjacent configurations because configurations are not discrete objects stored in separate locations; they are aspects of a continuous substrate that extends through all three dimensions simultaneously (A2).

The practitioner intends a specific outcome — to weave a configuration toward a particular actualisation, or to pull a temporal thread toward a prior state. But the substrate responds as a whole. The epistemic, temporal, and actualised dimensions co-move because they are not independent axes of a coordinate system; they are distinguishable aspects of a single constitutive ground. Co-Movement is what happens when the ground responds to being touched. The practitioner controls where they touch. They do not control how the ground moves.

## 4.2 Why the Actual Effect Is Random

The game models Co-Movement through random card draws rather than deterministic tables because the practitioner cannot predict how the substrate will respond to intentional intervention. This is not a limitation of the practitioner's skill or knowledge — it is a metaphysical fact about the substrate itself (A1, A4). The unintelligible ground (Ein Sof) from which threads are continuously spooled exceeds all categories and attributes (A5). A practitioner who could predict Co-Movement with certainty would possess complete knowledge of how the constitutive ground relates to every rendered configuration in the affected region. This knowledge is, by definition, impossible for a rendering-bound consciousness.

The card deck represents the bounded unpredictability of substrate response. The deck is finite (18 cards) and known (the practitioner understands what kinds of effects are possible), but the specific card drawn on any given operation is not foreseeable. Over a full deck cycle, all effects will occur — the substrate's response is exhaustive, not arbitrary. But the ordering is beyond the practitioner's control. Card counting across peninsula-wide operations is possible but requires tracking information the practitioner does not naturally possess, modeling the strategic value of Thread-monitoring intelligence networks.

## 4.3 Auto-Effect Tables

### Co-Movement Cards 1–15 (ED-577 — canonical card list)

All Thread Tension references from the original deck are converted to Mending Stability (inverted polarity: original +TT becomes −MS, original −TT becomes +MS).

| Card | Name | Actualized Effect | Unactualized Effect |
|------|------|-------------------|---------------------|
| CM-01 | Temporal Drift | Mending Stability −1. One clock in the territory advances 1 tick. | No MS change. Clock advance still applies. |
| CM-02 | Substrate Ripple | Mending Stability −2. All Thread operations in territory +1 Ob next season. | Mending Stability −1. No Ob change. |
| CM-03 | Echo Cascade | Mending Stability −1. One resolved Thread operation re-manifests a minor version of its effect. | No effect. |
| CM-04 | Coherence Bleed | Mending Stability −1. Lowest-Coherence Thread entity in territory: Coherence −1. | No MS change. Coherence loss still applies. |
| CM-05 | Anchor Settling | Mending Stability +1. One Thread Witness Node in territory stabilises (cannot be disrupted this season). | Mending Stability +1. No Node effect. |
| CM-06 | Resonance Bloom | Mending Stability −2. Each Practitioner in territory: +1D to their next Thread operation this season (one use per practitioner, expires unused at season end). (ED-577-04 resolved) | Mending Stability −1. No bonus. |
| CM-07 | Scar Memory | No MS change. One Dissolution residue site in territory becomes visible to non-Sensitives for 1 scene. | No effect. |
| CM-08 | Temporal Fold | Mending Stability −1. One past-oriented Pulling operation in territory may target one additional season into the past (free depth extension). | No MS change. No depth extension. |
| CM-09 | Rendering Surge | Mending Stability −3. All Thread entities in territory: forced Coherence check Ob 1. | Mending Stability −2. No Coherence check. |
| CM-10 | Ground Harmony | Mending Stability +2. Mending operations in territory: −1 Ob this season. | Mending Stability +1. No Ob change. |
| CM-11 | Witness Flare | No MS change. All Thread Witness Nodes in territory activate: Church Attention Pool +1. | Church Attention Pool +1. No Node activation. |
| CM-12 | Ground Stability | Mending Stability +1. Territory Thread Debt cleared (all accumulated +Ob tokens removed). | Mending Stability +1. Debt not cleared. |
| CM-13 | Epistemic Breach | Mending Stability −1. One non-Sensitive NPC in territory gains temporary TS = 15 for 1 scene (passive perception only — anomalous awareness per visibility table, cannot Thread-Read or Leap). Certainty pressure point. Church Attention Pool +1. (ED-577-01 resolved) | Church Attention Pool +1. No perception grant. |
| CM-14 | Substrate Assertion | Mending Stability −3. One Locked Thread entity in territory: Lock strength +1. | Mending Stability −1. No Lock change. |
| CM-15 | Dissolution Wake | Mending Stability −2. One territory gains a Dissolution residue site if none exists. If one exists: residue intensity +1. | Mending Stability −1. Residue intensity +1 if site exists; otherwise no effect. |

**Deck composition:** 18 cards total (CM-01 through CM-18). Cards 16–18 are Mending-specific additions (see §7.1). Shuffle all 18 into a single deck. Draw 1 per Thread operation (2 if Thread Witness Node present in territory). Reshuffle when all 18 cards drawn (global deck, not per-territory). Deck cycles every ~3-4 seasons at typical operation rates. (ED-577-02 resolved)


## 4.4 History Resonance and Flashback Anchoring

*Unchanged from current R37, R38. ThS → Coherence.*

---

# PART FIVE: RENDERING STABILITY (WORLD TRACK)

## 5.1 What Mending Stability Measures


**Range:** 100 (fully stable) → 0 (the Rupture).

## 5.2 Mending Stability Degradation Sources

| Source | Mending Stability Change |
|---|---|
| Thread operation (Weaving, Pulling — partial or failure) | −1 to −2 per degree table |
| Thread operation (Weaving — overwhelming at Relational+) | +1 (restoration) |
| FR Lock | −1 to −3 (immediate) + chronic drift |
| FR Dissolution | −3 to −8 |
| Past-Oriented Pulling | −3 minimum |
| Micro-Gap persisting to Accounting (normally closes same scene) | −1 |
| Gap persisting (per season) | −4 |
| Siege (per season) | −1 (concentrated suffering) |
| Einhir site under stress during siege | −1 additional |
| Mending (success/overwhelming) | +1 to +2 (restoration); multiple successful Mendings in a season stack independently at Accounting |
| Community Organizing (Revolution success) | +1 to +2 |
| Southernmost expedition Mending | +2 permanent per successful season |
| Board game Weave order (success) | +1 |
| Board game Mend order (success) | +1 |
| Board game Weave order (failure) | −1 |
| Winter annual drift | −1 |

## 5.3 Mending Stability Thresholds

> **Mending Stability threshold cumulation (P-14):** Mending Stability threshold effects are cumulative. Each lower band includes all effects from higher bands: - **Fractured (39–20)** includes all Fragile effects (spontaneous Shifting Objects, +1 Ob in affected territories) PLUS Fractured-specific effects (spontaneous Gaps, Monstrous Incursion risk, rendering failures for non-practitioners). - **Critical (19–1)** includes all Fragile + Fractured effects PLUS Crit



| Mending Stability | State | World Effects |
|---|---|---|
| 100–80 | Stable | No unusual phenomena. Substrate sound. |
| 79–60 | Strained | Occasional wrongness in territories with Thread history. Non-practitioners with Thread Sensitivity 10+ may sense unease near old operation sites. |
| 59–40 | Fragile | Shifting Objects form spontaneously in high-traffic Thread territories. One random Shifting Object per season at Accounting. Thread operations +1 Ob in affected territories. |
| 39–20 | Fractured | Gaps may open spontaneously (1d10 per season at Accounting; on 1–2: Gap in territory with lowest Prosperity). Monstrous Incursion risk in all territories with existing Gaps. Non-practitioners experience rendering failures — inconsistent memories, déjà vu, objects in wrong places. |
| 19–1 | Critical | As Fractured, plus: spontaneous Gaps on 1–4 (doubled risk). All Thread operations +1 Ob worldwide (the substrate resists manipulation). Seasonal Stability checks for all factions at Ob 1 (institutional rendering begins failing) — failure produces Mandate −1 for that faction (minimum 0). At Mandate 0, failure instead produces Faction Fracture: one sub-faction splinters off as a new minor faction (engine determines composition and goals). Mandate cannot go below 0. Discovery Events become common — Thread Sensitivity growth checks for any non-practitioner who witnesses a rendering failure. NPCs with coup or succession trigger conditions (flagged in design files) treat Mending Stability ≤ 10 as +1 to their trigger check pool (institutional rendering failure accelerates political instability). |
| 0 | The Rupture | Rendered reality fails. Campaign ends in catastrophe. No faction wins. The Ein Sof's fullness overwhelms the rendered world's capacity. What emerges is not destruction but excess — too much being for consciousness to render. The world does not end. It becomes unintelligible. |

**Design note — Mending Stability Critical as endgame:** Once Mending Stability enters the Critical band (19–1), the campaign is in a 2–4 season endgame without dramatic intervention. At Mending Stability 1, the endgame trap is complete: almost every Thread operation carries Rupture risk on Failure, but not operating also reaches Rupture within 1–3 seasons from Lock drift and winter. The only structural exit requires: remove all active Locks (eliminates drift), Mend all active Gaps (eliminates per-season Mending Stability loss), then operate exclusively at Object/Personal scale until Mending Stability recovers via successful Mending. Each Mending attempt at Mending Stability 1 risks Rupture on Failure (~17–34% success at best). This is the Einhir Catastrophe replicated mechanically — they reached this point, and there was no escape. The game does not provide a clean rescue from Mending Stability 1. It provides a narrow, difficult path that requires practitioner cooperation across faction lines and accepts that Rupture is a legitimate campaign ending. The convergence of Lock drift, Gap persistence, spontaneous Gap formation, and seasonal operation failures produces net Mending Stability losses of 8–15 per season even with active Mending. The seasonal cap (±10) prevents single-Accounting Rupture but cannot arrest multi-season terminal decline. Mending Stability Critical is the point of no return: the table must coordinate across faction lines to stabilise the world, or accept that the campaign ends in the Rupture. This is designed. The Einhir reached the same point.

## 5.4 Mending Stability in Board Game


**Mending Stability is hidden from players by default.** The Investigate Thread order (Intelligence vs Ob 3) reveals the current Mending Stability value. Overwhelming: also reveals which territories have Gaps. Players know the world is degrading (they see the threshold effects) but do not know the exact number without investigation.

## 5.5 Mending Stability in Hybrid

Mending Stability advances at Accounting (Cascade Phase). Both TTRPG-sourced changes (from Personal Phase Thread operations) and board-game-sourced changes (from Strategic Phase orders) are applied at the same Accounting. No double-counting; seasonal cap on Mending Stability change is ±10 per season.

## 5.6 Thread Revelation Curve (campaign_architecture_v1 §4)

As MS drops, Thread becomes progressively visible to non-practitioners. This is the game's master narrative driver — every NPC arc, faction identity, and political alliance is downstream of the revelation curve.

**Starting state (MS ~72):** Threadwork is folklore. Common people consider it old stories. The Church frames Thread phenomena through Solmundic theology. Crown considers it irrelevant. Hafenmark ignores it. Varfell KNOWS (Vaynard's private collection, VTM track). Wardens live it but are marginal.

**The Forgetting (critical context):** The Forgetting radiates from the Southernmost. It is possible to READ about threadwork from surviving books and documents, but it is NOT possible to truly EXPERIENCE or understand threadwork through rational/linguistic means. Thread Sensitivity is experiential, not intellectual. This means RM's cultural revival can reconstruct governance structures but cannot access the metaphysical foundation. People who believe threadwork was real are treated like flat-earth contrarians — correct, but considered insane.

| MS Band | Non-Practitioner Perception | Political Impact |
|---------|----------------------------|-----------------|
| 100–80 (Stable) | Nothing. Folklore. | None. Thread is politically irrelevant. |
| 79–60 (Strained) | Subtle anomalies near T15/T6/T13. Animals behaving strangely. Crop patterns. "The Southernmost is always strange." | Mild unease in border territories. Church explains as "God's testing ground." No political action. |
| 59–40 (Fragile) | Observable phenomena in Proximity ≤ 2 territories. Gaps visible as physical distortions. People disappear near Gap sites. | Growing fear. Church scrambles to maintain theological framework. Crown must address public safety. Varfell's Thread knowledge becomes politically valuable. RM denial becomes harder to sustain. |
| 39–20 (Fractured) | Peninsula-wide phenomena. Brief moments where reality looks "thin." Memories feel uncertain. Familiar places seem unfamiliar. Threadcut beings encountered by ordinary people. | **Crisis of understanding.** "The stories were true." Every faction must respond. Church: theological challenge. Crown: governance inadequacy. RM: ideological foundation shakes. Varfell + Wardens gain enormous political relevance. |
| 19–1 (Critical) | Thread undeniable. Non-practitioners perceive substrate directly in extreme cases. World visibly frays. | **Existential reorientation.** The faction integrating Thread reality into governance fastest gains decisive advantage. |

**Revelation Triggers (accelerate public awareness regardless of MS):** A renowned character performs threadwork publicly. A Threadcut being appears in a populated settlement. Edeyja's Mending produces visible results. Mass battle involving Thread operations. Each trigger produces a mandatory Revelation Event scene — player and relevant NPCs react to Thread becoming more public. NPC Conviction and Certainty determine reaction.

**Faction responses:** Church → theological crisis (Himlensendt's arc). Crown → governance inadequacy (no framework for metaphysical crisis). Hafenmark → legitimacy challenge. Varfell → vindication and opportunity. RM → identity crisis (Embrace/Denial/Schism, see campaign_architecture_v1 §2.4). Wardens → political relevance.

**Hidden Thread-site bonus (historical_precedents_analysis §4.3):** RM governance cells at settlements containing Thread-active sites (former Threadweaving locations, Proximity ≤ 2) receive +0.5 Accord/season, unlabeled in UI. The player observes RM governance working better in certain locations without knowing why. At Thread revelation (MS enters Fragile band or Revelation Trigger fires), the bonus becomes visible and the player understands: the governance model was partly metaphysical.

Branch on RM choice:
- **Embrace:** Bonus revealed, doubles to +1 Accord/season. RM consciously engages Thread properties.
- **Denial:** Bonus continues but stays hidden. Governance works but RM refuses to acknowledge why.
- **Schism:** Embrace faction gets doubled bonus in their settlements. Denial faction loses bonus entirely.

**Thread-active settlement mapping:** A settlement is Thread-active if: (a) it is in a territory with Proximity ≤ 2 to T15 Askeheim, OR (b) it contains a POI tagged as a former Threadweaving site in geography_v30. Current Thread-active settlements: S-010 Stillhelm, S-011 Stillhelm Watch, S-031 Oastad, S-032 Oastad Shrine, S-033 Askeheim Ruins, S-034 Askeheim Gate, S-028 Grauwald (Einhir heritage site), S-029 Grauwald Lodge.

[EDITORIAL: ED-693 — Thread Revelation Curve propagated. Source: campaign_architecture_v1 §4, historical_precedents_analysis §4.3.]

---

# PART SIX: THREADCUT BEINGS

## 6.1 Ontological Status




## 6.2 Observer-Dependent Rendering

Each observer perceives a threadcut being at their own rendering ceiling.

| Observer Thread Sensitivity | Perception |
|---|---|
| 0–9 | Nothing, or vague unease. |
| 10–29 | A presence. Unstable image. Details shift. |
| 30–49 | Coherent figure, but features approximate. Real but wrong in inarticulable ways. |
| 50–69 | Stable perception. The being is fully rendered. Its continuous self-sustaining Thread work visible as a hum of operation. |
| 70+ | Full perception. The observer perceives the being's self-rendering effort — the continuous work that holds it in place. The being is something that holds itself up rather than something held up. |

### Rendering Beyond Observer Capacity


**Cost:** Each scene of beyond-ceiling rendering: +1 **Rendering Strain** (cumulative). When Rendering Strain equals Health: De-actualisation begins.

The more intensely the being renders itself, the sooner it ceases to be.

## 6.3 Mechanical Distinctions

- **Wounds:** Each costs 1 additional point of sustained Thread work rather than conventional Ob penalty.
- **Coherence track:** Does not apply. Threadcut beings do not render — they have no rendering to destabilise.
- **External Thread operations:** A threadcut being may direct their originary intentionality toward external threads rather than self-maintenance. No Leap is required — they are already in the originary state that organic practitioners must Leap to reach. Declare operation type and target; roll standard operation pool (Spirit + History + Thread Pool Score) against standard Ob. Cost: each external Thread operation adds +1 Rendering Strain (directing intentionality outward strains the continuous self-maintenance that constitutes the being's existence). A threadcut being performing external operations accelerates their own De-Actualisation. This is the Solmund dilemma: the being capable of Structural intervention faces the choice between acting (and beginning to cease) and withholding (and preserving existence at the cost of inaction).

## 6.4 De-Actualisation

When Rendering Strain equals Health, or Wounds reach **Rendering Threshold** (Health ÷ 2), the being can no longer sustain self-rendering.


**Sequence:**
- **Round 1:** Intelligible face dissolving. Thread Sensitivity 30+ observers perceive loss of coherence. All operations +2 Ob. May attempt stabilisation: Weaving on itself (standard pool vs Ob = Wounds + Rendering Strain).
- **Round 2:** Perceivable only by Thread Sensitivity 50+. Operations +4 Ob. Second stabilisation attempt possible.
- **Round 3+:** Configuration returns to the unintelligible ground. Not death — cessation of self-rendering. Micro-Gap forms, closes within scene. Dissolution residue remains.


---

# PART SEVEN: CROSS-MODE IMPLICATIONS

## 7.1 Board Game

### New Order: Mend

Available to any faction with an affiliated Thread Sensitivity 50+ character, or Revolution (via Community Mending).


| Order | Roll | Effect |
|---|---|---|
| **Mend** | Intelligence (or faction-specific) vs Ob by Gap category (see below) | Success: Gap closed. Mending Stability +1. Failure: Mending Stability −1. Draw Co-Movement Card. |

**Board game Mend Ob** (lower than TTRPG — faction-level effort abstracts collective resources):

| Gap Category | Board Game Ob |
|---|---|
| Shifting Object | 1 |
| Standard Gap | 2 |
| Entrenched Gap | 3 |
| Catastrophic Gap | 4 |

### Revised Co-Movement Card Deck (18 cards)

Cards 1–15: retained (all Thread Tension references become Mending Stability, inverted).
Cards 16–18 added:

16. **Substrate Settling** — Mended territory: all Thread operations −1 Ob next season.
17. **Scar Trace** — Mended territory retains visible Thread scar. Church Church Influence +1. No Mending Stability change.
18. **Residue Condensation** — dissolution residue forms at Mending site. Niflhel may harvest.

### Lock Chronic Drift


### Mending Stability Track

Replaces Thread Tension track on board. Runs 100→0. Hidden by default (Investigate Thread reveals). Shared loss at 0.

## 7.2 Hybrid Mode




> **Hybrid Coherence declaration rule (PP-198):** [PROVISIONAL — canon: Amendment 01 §2, §3] Coherence cost in Hybrid Strategic Phase is paid by the Player Character who **declares leadership at Phase 1 of the Cascade Phase** (committing to have performed the Leap for that order). This declaration is binary and mechanical — it is not a narrative judgment. The declaring PC's layer 2 was suspended for that order; therefore their Coherence decrements. If no PC declares leadership at Phase 1: no Coherence cost applies to any PC for that order (the order was executed by Non-Player Character practitioners). Multiple PCs cannot co-declare leadership for a single order; only the declared PC pays. Replace all instances of "narratively leads" in Hybrid Coherence rules with "declared leadership at Phase 1 of Cascade Phase."
- **Mending Stability changes:** Both Personal and Strategic Phase changes applied at Accounting. Seasonal cap: ±10 net (the cap applies to the net Mending Stability change after all sources — positive and negative — are resolved at Accounting).

> **Hybrid co-declaration tie-break (PP-205):** [PROVISIONAL] If two or more Player Characters simultaneously declare leadership for the same Strategic Phase Thread order at Phase 1 of the Cascade Phase, the declaration resolves as follows: (1) The PC with the highest Thread Sensitivity declares. (2) If Thread Sensitivity is tied: the PC who declared first at the table (in real-world turn order, not game priority order) declares. (3) The non-declaring PC's declaration is void; they pay no Coherence cost for that order. This ruling applies only to simultaneous declarations. If PCs choose to negotiate among themselves before Phase 1 closes, that negotiation determines the declarer with no tie-break needed.


## 7.3 Updated Mode Branching

| Rule | TTRPG | Board Game | Hybrid |
|---|---|---|---|
| Thread operations | Weaving, Pulling, Mending, Lock, Dissolution — personal-scale | Weave, Mend, Investigate, Harvest — faction-scale | Personal Phase: TTRPG. Strategic Phase: board game. |
| Gap closure | Mending (Att + Focus + Thread Pool Score) | Mend order | TTRPG Mending or Mend order |
| Co-movement | Version C (temporal + epistemic auto, actual d6) | Co-Movement Cards (18) | Personal: Version C. Strategic: Cards. |
| Practitioner degradation | Coherence 10→0 | Not tracked | Coherence during Personal Phase |
| World stability | Mending Stability 100→0 at seasonal accounting | Mending Stability 100→0 at Accounting | Mending Stability at Cascade Phase Accounting |
| Lock chronic | Engine tracks; Mending Stability drift at accounting | Territory card: Mending Stability −1/season | Personal-scale → territory card at Cascade |

---

# PART EIGHT: INTERDEPENDENCY MAP

## 8.1 Systems Replaced

| Old System | Replaced By | Scope |
|---|---|---|
| Intelligibility (§4.5, 10→0) | Coherence (10→0) | All character sheets, all Thread operation tables |
| ThS / CD (§5.9, 20→0) | Coherence (10→0) | Campaign tracking eliminated as separate system |
| Taint (§5.10, 0→10) | Coherence (low-end effects) | No separate track. Dissolution residue = accelerated Coherence loss. |
| Thread Tension (Thread Tension, 0→100) | Mending Stability (Mending Stability, 100→0) | Board game track, all threshold tables, all operation consequence tables |
| Gap closure via FR Dissolution | Mending (new operation) | §5.13, board game orders, Southernmost expedition |
| "Solmund" (all references) | "Solmund" | All files (logged for Haiku batch) |
| AG calendar | AS calendar | All files (logged for Haiku batch) |
| "Epistemic seduction" | Cut — Coherence degradation | All references |
| "Taint" | Cut — Coherence degradation | All references |

## 8.2 Systems Unchanged

- Core engine (dice, TN, Ob, degrees)
- Combat engine (pool split, Wounds, Health)
- Social system (Composure, Debates, Appeals)
- Faction system (Domain Actions, attributes, accounting)
- Political axes, mass combat, siege
- Histories, Beliefs, Inspirations
- Circles, Resources

## 8.3 Implementation Sequence

| Step | Task | Model |
|---|---|---|
| 1 | Simulate Coherence 10→0 degradation rates across archetype campaigns | Sonnet |
| 2 | Simulate FR Lock chronic Mending Stability drift across 10-season campaigns | Sonnet |
| 3 | Simulate Mending pool (Att + Focus + Thread Pool Score) probability curves | Sonnet |
| 4 | Simulate over-actualisation impact on practitioner gameplay | Sonnet |
| 5 | Stress test Diagnosis-before-Leap sequence (timing in combat) | Sonnet |
| 6 | Stress test threadcut de-actualisation | Sonnet |
| 7 | Compile into Thread Operations chapter (new Stage 3) | Sonnet |
| 8 | Update board game Thread orders, Co-Movement deck, Mending Stability track | Haiku |
| 9 | Update hybrid mode branching catalogue | Haiku |
| 10 | Solmund rename + AG→AS + Church rename (all files) | Haiku |
| 11 | Canon guard pass on complete redesign | Sonnet |

