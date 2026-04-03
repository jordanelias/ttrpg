# AUDIT-D-02 + SIM-D-05: Full Debate Audit + Three-Mode + Thread/Temporal Stress Test
## Date: 2026-04-02
## Source: debate_system_redesign_v1.md v1.5; params_threadwork.md v0.14-AUD1
## Covers: Re-audit (post gap-fill), TTRPG/Hybrid/BG all modes, Thread in Past/Present/Future axes

---

## 7-Dimension Tag
```
Test IDs: AUDIT-D-02 / SIM-D-05
Mechanics: Full debate system v1.5 + Thread operations in all temporal axes during debate
Mode: TTRPG + Hybrid + Board Game (all three) | Temporal: PAST, PRESENT, FUTURE, CROSS
Tracks: TC, Composure, Concentration, RS, Coherence, Debate Fatigue
Factions: Church, Hafenmark, Crown, Varfell, Restoration
NPCs: Himlensendt, Baralta, Klapp, Maret Uln, Generic practitioners
Archetypes: Institutional authority, legalist, practitioner-orator, BG coalition delegate
```

---

# PART 1: AUDIT-D-02 — Post-Gap-Fill Re-Audit (Modes A, D, E, G)

## AUDIT Mode A — Formula Validation (v1.5)

| ID | Formula | Status | Notes |
|----|---------|--------|-------|
| FA-01 | Presence modifier: max(0, floor((Pres−3)/2)) | ✓ PASS | PP-101 applied. Min 0 confirmed. |
| FA-02 | Concentration floor 0 | ✓ PASS | PP-102 applied. |
| FA-03/04 | Strain min 1 | ✓ PASS | PP-103 applied. |
| FA-05 | effective_margin_CLASH = floor(margin × weight × 1.0) | ✓ PASS | |
| FA-06 | TC movement = effective_margin − resistance, min 0 | ✓ PASS | |
| FA-07 | DIVERGE negative successes → treated as 0 | ✓ PASS | PP-111. |
| FA-NEW-01 | BG effective_vote = floor(net × genre_weight) | **WARN P2:** Orientation weight not applied in BG formula. TTRPG uses genre × orientation. BG drops orientation. Acceptable abstraction but undocumented. Flag for design note. | PP-119 |
| FA-NEW-02 | Hybrid TC offset cap ±2 | ✓ PASS | Clean boundary. |
| FA-NEW-03 | Pre-debate prep: Attunement + History, TN7/8/6, Ob1 | ✓ PASS | No edge case at Attunement=0 (pool min 1D per params_core). |
| FA-NEW-04 | Coalition Concentration: only Lead depletes | ✓ PASS | Non-leads unchanged per exchange. |
| FA-NEW-05 | BG vote resistance: base 0 + up to +2 from Stability≥6 Abstains | ✓ PASS | Cap explicit. |
| FA-NEW-06 | Debate Fatigue: consumed after first social roll | ✓ PASS | PP-117 clarified. |
| FA-NEW-07 | Total Victory: TC≥9 or ≤1 | **FLAG P3:** "Total Victory" is a named state but §6.8 Untested Items list still refers to old open items not updated for gap-fills. §6.8 and §6.9 are now stale — they list items as "no procedure exists" that have been resolved in §§6.11–6.15. | PP-119 cleanup |

## AUDIT Mode D — Gap Detection (v1.5)

All GAP-DS-01 through GAP-DS-20 checked against v1.5 text:

| Gap | Status |
|-----|--------|
| GAP-DS-01 (Ob tables) | ✓ Resolved — PP-112 clarifies no fixed Ob for Argue. |
| GAP-DS-02 (Thread mid-debate) | ✓ Resolved — §6.15. |
| GAP-DS-03 (Total Victory) | ✓ Resolved — §6.5 PP-114. |
| GAP-DS-04 (Reading Exchange +1D) | ✓ Resolved — §6.11 prep roll is the TTRPG mechanism; BG has Diplomacy action. |
| GAP-DS-05 (BG Parliamentary Vote) | ✓ Resolved — §6.13. |
| GAP-DS-06 (Multi-party) | ✓ Resolved — §6.12. |
| GAP-DS-07 (Genre pivot) | ✓ Resolved — PP-112 Step 3. |
| GAP-DS-08 (Doubt Marker replacement) | ✓ Resolved — PP-113. |
| GAP-DS-09 (Strain minimum) | ✓ Resolved — PP-103. |
| GAP-DS-10 (Concentration floor) | ✓ Resolved — PP-102. |
| GAP-DS-11 (Presence modifier) | ✓ Resolved — PP-101. |
| GAP-DS-12 (Corroboration in §6.4) | Partial — PP-104 stub present. Full port blocked by ED-051 (NPC stats). Remains P1 but stub in place. |
| GAP-DS-13 (Debate initiation gate) | ✓ Resolved — PP-107 §6.0. |
| GAP-DS-14 (Rattled+Spent stacking) | ✓ Resolved — PP-106. |
| GAP-DS-15 (§6.10 stale note) | ✓ Resolved — cleaned. |
| GAP-DS-16 (Post-debate strain recovery) | ✓ Resolved — PP-108/114. |
| GAP-DS-17 (Momentum in Debate) | ✓ Resolved — PP-112 Step 3. |
| GAP-DS-18 (Corroboration asymmetric) | ✓ Resolved — PP-116. |
| GAP-DS-19 (Beliefs integration) | ✓ Resolved — PP-115. |
| GAP-DS-20 (DIVERGE negative successes) | ✓ Resolved — PP-111. |

**NEW gaps found in v1.5:**

| ID | Description | Severity |
|----|-------------|---------|
| GAP-DS-21 | §6.8 and §6.9 stale — list items as unresolved that are now resolved in §§6.11–6.15. | P3 (cleanup) |
| GAP-DS-22 | BG orientation weight absent from §6.13 effective_vote formula — undocumented abstraction. | P2 |
| GAP-DS-23 | §6.11 prep roll: no definition of "most relevant History" — GM discretion assumed but unstated. | P3 |
| GAP-DS-24 | Thread temporal axis interaction: R-65 bonus uses TS÷30 but §6.15 between-exchange ops have no temporal axis restrictions — Pulling (Past-oriented) during a Future-genre debate has no rule. | P1 — see SIM-D-05 Part 3 |
| GAP-DS-25 | Coalition §6.12: no rule for what happens when only ONE coalition member remains un-Rattled and that member is also the only one who can lead. Edge case: last-man lead with no corroborator available. | P3 |
| GAP-DS-26 | BG §6.13 multi-round: no rule on whether sides may change genre declaration between vote rounds. | P2 |
| GAP-DS-27 | Hybrid §6.14: TC offset cap ±2 interacts with pre-debate lobbying (already ±2 from Diplomacy). Double-capping means lobbying is irrelevant in Hybrid context if BG vote already provides maximum offset. | P2 |

## AUDIT Mode E — Core Principles (v1.5)

| Principle | Status v1.5 |
|-----------|------------|
| 1 (Roll only when meaningful) | ✓ Gate added PP-107. |
| 2 (Let It Ride) | ✓ Implied by exchange structure. |
| 3 (Fail Forward) | ✓ Compromise zone provides output on failure. |
| 4 (Histories, not Skills) | ✓ History bonus applies. |
| 5 (Pool = Attribute + History) | ALTERED — (Presence×2)+History. Documented in PP-112. |
| 6 (Wounds) | N/A |
| 7 (Inspiration/Spirit) | ✓ Momentum integration PP-112/115. |
| 8 (Beliefs) | ✓ PP-115 Belief achievement on aligned win. |
| 9 (Social combat via Rhetoric) | ✓ |
| 13 (Circles and Resources) | ✓ Corroboration uses Bonds (Circles attribute). |

**All prior principle gaps now resolved.** P5 alteration documented.

## AUDIT Mode G — Cross-Mode Consistency (v1.5)

| Mechanic | TTRPG | Hybrid | BG | Flag |
|----------|-------|--------|----|------|
| Argue pool | (Pres×2)+History | Same | Mandate sum | Consistent — appropriate abstraction |
| Genre weights | Full table | Same | Same | ✓ |
| Orientation weights | ×1.0 / Doubt Marker | Same | **ABSENT** | GAP-DS-22 — P2 |
| Conviction Track | Active | Active (from BG offset) | Active | ✓ |
| Thread consequences | Fire | Fire (TTRPG layer) | Do NOT fire | ✓ Documented |
| Beliefs/Momentum | Active | Active | **Not applicable** | ✓ Correct — faction-level has no Beliefs |
| Preparation | Prep roll §6.11 | Same | Diplomacy domain action | ✓ Consistent abstraction |
| Debate Fatigue | Active | Active | **Absent** | GAP-DS-22 — does BG vote produce Debate Fatigue equivalent? Unstated. P3. |
| Total Victory | Full consequences | Full consequences | Mandate −1 only | ✓ Appropriate abstraction |

---

# PART 2: SIM-D-05a — All Three Modes Full Stress Test

## TTRPG Mode — Grand Debate, No Thread

Already comprehensively tested (SIM-D-01 through SIM-D-04). Confirmed findings:
- Resistance 2 → Compromise ~95% in 3-exchange Formal; ~75% in 5-exchange Grand.
- Coalition: endurance advantage confirmed.
- Rattled in exchange 3–5 typical for Composure ≤ 9 losing orators.
- Total Victory (TC≥9/≤1) achievable in ~5% of Grand Debates at resistance 2.
**Status: ✓ Verified across multiple scenario types.**

## BG Mode — Parliamentary Vote, Full Season Cycle

**Scenario: Church (Mandate 5) + Crown (Mandate 5) coalition vs Hafenmark (4) + Varfell (3). Motion: succession ratification (Future primary ×1.0, Crown audience → Present ×1.5). No abstentions. Resistance 0.**

Side A (Church+Crown): pool 10D. Genre: Present ×1.5. E[net]=3.3. effective_vote=floor(3.3×1.5)=floor(4.95)=4. Δ_A=4.
Side B (Hafenmark+Varfell): pool 7D. Genre: Future ×1.0. E[net]=2.31. effective_vote=floor(2.31)=2. Δ_B=2.
Net: 2 toward A. TC: 5→7. **Motion passes in one round.**

**Genre switch between rounds [GAP-DS-26 test]:** If Hafenmark+Varfell switch to Past genre (×0.5 for Crown audience) in round 2: effective_vote=floor(2.31×0.5)=1. Even weaker. **Switching to secondary genre never improves position for the losing coalition under Crown audience.** Genre pivot between BG rounds is unlikely to be tactically useful against a dominant audience ethical mode — the optimal genre is locked by the question and the audience. GAP-DS-26 resolution: allow genre change between rounds but add design note that it is rarely advantageous. **PP-119 design note.**

**BG Orientation absence [GAP-DS-22]:** Under TTRPG, Hafenmark might use Obscuring to place a Doubt Marker — a purely defensive play when losing. BG has no equivalent. Factions cannot "Abstain from moving the TC" in a targeted way. This is correct — BG Parliamentary Vote is a public vote, not a debate. The Obscuring mechanic belongs to personal-scale argumentation, not faction-level voting. **GAP-DS-22 resolved: BG orientation absence is correct and intentional. Add design note to §6.13. PP-119.**

**BG multi-round genre declaration [GAP-DS-26]:** Add to §6.13: sides may change genre declaration between vote rounds. **PP-119.**

## Hybrid Mode — Full Sequence

**Setup:** Prior season: Hafenmark ran 2 Diplomacy domain actions targeting this vote. Both successful. TC offset: +2 toward Hafenmark (Side B). Starting TTRPG TC: 5−2=3.

**Hmm — TC=3 is already Side B win threshold.** Does the Hybrid debate start with a win condition already met?

**[HD-F-01] P1 FINDING:** If prior lobbying (2 Diplomacy actions toward Side B) produces TC start = 3 or lower (≤3 = Side B wins), the TTRPG personal debate is irrelevant — the outcome is already decided before the named characters speak. This makes the Hybrid debate scene dramatically hollow.

**Resolution:** Add rule: Hybrid debate starting TC is clamped to 4–6 (compromise zone) regardless of BG offset. The BG offset shifts where in the compromise zone the debate starts (4 = Side B dominant compromise; 6 = Side A dominant compromise; 5 = neutral) but never pre-decides the outcome. **PP-120 provisional.**

**[HD-F-01 continued]:** With PP-120, maximum offset ±2 capped to compromise zone 4–6:
- BG Δ=+2 toward Side A → TTRPG TC starts at 6 (not 7).
- BG Δ=+2 toward Side B → TTRPG TC starts at 4 (not 3).
- BG Δ=0 → TTRPG TC starts at 5.

This preserves personal skill relevance in all Hybrid contexts. From TC=6, Side B needs to push to TC≤3 in 3–5 exchanges — very difficult but not impossible. **Design intent preserved.**

**Revised §6.14 Step 2:** "Hybrid starting TC = 5 + capped offset, then clamped to 4–6. The personal debate always begins in the compromise zone — faction-level lobbying determines the starting position within that zone, not the outcome."

---

# PART 3: SIM-D-05b — Thread in All Temporal Axes During Debate

## Temporal Axis Framework (from params_threadwork.md)

Thread operations interact with time through three genres that map directly onto debate genres:

| Thread Temporal Mode | Debate Genre | Expected Interaction |
|---------------------|-------------|---------------------|
| Past-Oriented Pulling | Past | Orator cites temporal evidence Thread amplifies |
| Present Weaving | Present | Orator claims authority Thread reinforces |
| Future actualization | Future | Orator argues consequence Thread anchors |

The question: does the temporal axis of a Thread operation interact with the debate genre in use?

**Current rule (§6.15):** Thread genre weights are fixed at setup. Thread operations affect audience Disposition (via W-42) or the practitioner's personal state (RS/Coherence). No genre-axis interaction stated.

**P-01 compliance check:** Inseparability requires that Thread operations produce co-movement in all three dimensions (temporal, epistemic, actual). A Past-Oriented Pull during a Past-genre debate should produce co-movement that overlaps with the debate's epistemic frame — both are invoking the Past simultaneously. No mechanic exists for this overlap.

---

### TEST 1 — Past-Oriented Pulling during Past-Genre Debate

**Setup:** Church Tribunal. Question: "Did the accused conduct heretical Thread operations?" (Past genre primary ×1.0, Church audience → Past ×1.5, so Past = 1.5). Maret Uln (TS 50, in the gallery) initiates Past-Oriented Pull between Exchange 2 and 3, targeting a historical Thread configuration from 3 seasons ago.

**POP requirements (params_threadwork):** TS 70+ required for most POP applications. Maret TS 50 → can only pull Same scene/session (Ob 3, TN7). Even this Ob 3 at pool (Spirit+History+TPS/2) is a moderate difficulty.

**[TT-F-01] Finding P2:** POP requires TS 70+ for any application beyond same-scene pulling (Ob 3). At TS 50, Maret's between-exchange Pull is same-scene only. The evidentiary value is limited — it can only re-invoke what happened in this scene/session. This is correct: Past genre debates invoke historical precedent (documents, prior statements), while POP invokes actual Thread configurations from the past. Same-scene POP during a Past-genre Tribunal invokes THIS session's Thread events, not the broader historical record. Temporally coherent.

**P-01 check:** POP fires automatically: (a) temporal auto-effect: audience observers with TS ≥ 10 perceive a "wrongness" as the past configuration bleeds into the present. (b) epistemic auto-effect: all observers' testimony about events in that time period becomes slightly less certain (Certainty check Ob 1 for TS-sensitive observers). (c) actual auto-effect: d6 consequence. All three fire. ✓ P-01 compliant.

**Interaction with debate Past genre:** The debate's Past genre weight (×1.5 for Church) applies to the ARGUE roll, not to Thread operations. The POP's temporal auto-effect (audience uncertainty) could shift the audience's Read result for the next exchange — GM discretion per §6.15 (±1 TN). **No new rule needed** — the existing between-exchange procedure handles this. The ±1 TN Read modifier from §6.15 is the correct and sufficient hook for Thread temporal effects on debate.

---

### TEST 2 — Weaving (Present) during Present-Genre Debate

**Setup:** Parliament, Formal Debate. Question: "Is Baralta fit to hold her Duchy?" (Present genre primary ×1.0, Crown audience → Present ×1.5). Klapp (TS 31, barely Stirring) uses R-65 Weaving bonus during Exchange 2's Argue step to support Himlensendt.

**R-65 rules:** TS 31 → floor(31÷30) = +1D bonus to Argue pool. Declare before rolling. Coherence check Ob 1 after exchange.

**Present-genre debate + Present Weaving test:**
- The Weaving adds +1D to Himlensendt's argue pool. Mechanical effect: 15D → 16D. ✓
- Present Weaving (relational scale) = Coherence −1. Klapp starts Coherence 10.  After: 9.
- RS change: Weaving at relational scale, Success → RS 0 change. ✓ No RS cost on success.
- Audience observers with TS ≥ 10: perceive the operation (detection table: TS 30–49 = "senses operation, general direction"). Church cardinal (Klapp's own colleague — this is Klapp supporting Himlensendt, risking Church's own investigation of one of its Cardinals). 

**[TT-F-02] Finding P2 — INSTITUTIONAL PARADOX:** Klapp (Cardinal of Scholarship, TS 31) using R-65 Weaving in a Parliamentary debate is observed by any present character with TS ≥ 30. This includes Himlensendt himself (TS 0 — does not observe). But Baralta has TS 0. Random Parliamentary members: TS 10–29 range for most → "vague unease" only. However, if any MP has TS 30+ (possible among educated nobility), they observe the operation type and direction.

**Church member supporting Church orator via Thread = Church auto-investigates itself?** The Heresy Investigation trigger (§6.15) says "Church may immediately file Heresy Investigation Domain Action." If the Thread operator IS a Church Cardinal, the Church faces an absurd situation: filing a Heresy Investigation against one of its own Cardinals for supporting the Confessor in debate.

**Resolution:** Add exception to §6.15 Heresy Investigation trigger: "The Church does not initiate Heresy Investigation against its own ordained members using Thread operations in support of Church interests. Investigation may still be filed by opposing factions or concerned MPs as a Domain Action." **PP-121.**

---

### TEST 3 — Future Actualization / Consequence + Future-Genre Debate

**Setup:** Grand Debate. Question: "Should Valoria establish a Southernmost Accord?" (Future genre primary ×1.0, Varfell audience → Future ×1.5). Vaynard is the orator for Side A. He has TS 14 (Dormant — cannot Leap, no Thread operations active).

**No Thread practitioner on either side.** Testing: does the debate's Future genre interact with Thread actualization passively?

**§3.8 Thread consequences from debate (carried forward):** "Consequence (Future) genre win → Actualization — Domain Echo. +1D on first Domain Action pursuing that consequence within the season. RS +1 if the consequence involves Thread-sensitive matters."

**RS change from winning a Future-genre Grand Debate:** RS +1. This is a Thread consequence that fires without any practitioner involvement. The debate itself — at sufficient social scale — produces Thread co-movement.

**[TT-F-03] Finding P2 — PASSIVE RS GAIN INTERACTION WITH RS CEILING:**
- RS +1 from Future-genre Grand Debate win.
- RS ceiling = 100 (params_threadwork).
- If RS is at 100: RS +1 is wasted. No rule states this explicitly for debate-generated RS changes.
- params_threadwork states RS ceiling 100 for operations. The same ceiling should apply to debate-generated RS changes.
- **PP-122:** Add to §3.8 (or §6.5): "Debate-generated RS changes are subject to the RS ceiling of 100 and the RS=0 lockout. If RS = 100, no RS gain occurs. If RS = 0, no debate can generate further RS loss through §3.8 consequences — the substrate is already ruptured."

---

### TEST 4 — Thread Practitioner as Orator (All Three Temporal Axes)

**Setup:** Maret Uln (TS 50, Coherence 10, Spirit 4) is the TTRPG orator for Side B in a Grand Debate (Future genre primary, Varfell audience → Future ×1.5). She uses R-65 on Exchange 1, between-exchange W-42 on Exchange 2, and attempts Past-Oriented Pull between Exchange 3 and 4.

**Exchange 1: R-65 Future Argue bonus:**
Pool: (Presence 3 × 2) + History 2 + R-65 bonus floor(50÷30)=+1D = 9D.
Coherence check after: Ob 1. At Coherence 10, trivially succeeds. Coherence: 10.
Effective pool boost from R-65 at TS 50: +1D. Marginal on 8D base. ✓ Proportionate.

**Exchange 2: W-42 between exchanges (Present Weaving):**
Maret is debating a Future question while weaving a Present-scale configuration (Crowd Coherence). This is temporally mixed — she's arguing what SHOULD happen (Future) while threading how things ARE now (Present). P-01 requires co-movement: the Weave's actual effect (audience coherence shift, +1D Read next exchange at GM discretion) is consistent with the epistemic auto-effect of a Present Weave. ✓ No contradiction.

Coherence cost: relational scale Weave = −1. Coherence: 10→9. RS: Success → 0 change. ✓

**Exchange 3–4: Past-Oriented Pulling (temporal axis conflict test):**
Maret attempts POP (same-scene/session, Ob 3, TS 50 qualifies for same-scene only) between exchanges 3 and 4. She's arguing Future genre. The POP invokes Past configurations.

**[TT-F-04] P1 FINDING — TEMPORAL AXIS CONFLICT RULE MISSING:**
No rule governs what happens when a practitioner uses a Past-axis Thread operation during a Future-axis debate exchange. The between-exchange procedure (§6.15) allows any personal Thread operation with "no debate effect." But POP at same-scene level involves temporal auto-effects that affect all observers — including the audience the orator is simultaneously trying to persuade.

Specifically: POP's temporal auto-effect makes "the audience re-experience the cited past. Observers with TS 30+ perceive a thread-shimmer." This audience effect occurs during a Future-genre debate. The temporal auto-effect of Past invocation contradicts the Future framing of the argument. Should this impose a penalty on the orator's Argue pool or TC position?

**Current rule:** §6.15 says personal Thread operations have "no debate effect." This covers the practitioner's own RS/Coherence. But the POP's automatic audience-affecting temporal effect (which fires per P-01 co-movement) is NOT a personal effect — it affects all present observers.

**Provisional resolution PP-123:** When a practitioner conducts a between-exchange Thread operation whose temporal auto-effect contradicts the current debate's primary genre (Past-axis operation during Future-genre debate, or Future-axis operation during Past-genre debate), the audience Read roll for the next exchange is at TN 8 (Desperate) instead of TN 7 for both orators. The temporal cross-contamination makes audience state harder to read. This applies only to operations with explicit temporal auto-effects (POP, Weaving with RS-affecting temporal signatures). Neutral operations (Mending, Locking) and same-axis operations do not trigger this.

---

### TEST 5 — RS=0 Lockout Interaction with Debate Consequences

**Setup:** RS = 2 (Critical state). Grand Debate concludes with Future-genre decisive win. §3.8 says: RS +1 if Thread-sensitive matters. §6.5 Domain Echo fires.

**RS +1 from debate win at RS=2:** RS = 2→3. Threshold still Critical. ✓ Clean.

**But: another Future-genre debate win that same session. RS = 3 → 4.** RS 4 is still Critical. No threshold crossing. ✓

**Now: RS deteriorates to 0 between scenes (multiple Dissolution failures). RS = 0. Grand Debate occurs. Future-genre decisive win.**

**[TT-F-05] Finding P1:** §3.8 Thread consequence says "RS +1 if Thread-sensitive matters." But params_threadwork PP-166 says "RS=0 → all Thread operations cannot be attempted." Does RS=0 lockout apply to debate-generated RS changes?

**Analysis:** RS=0 lockout in params_threadwork applies to Thread **operations** (Leap, Weave, Pull, Lock, Dissolve, Mend). Debate-generated RS changes (§3.8) are not Thread operations — they are social-scale co-movement consequences. The lockout text says "Thread operations cannot be attempted" not "RS changes from any source are blocked."

**But at RS=0, the Rupture has occurred.** The world is in campaign-ending crisis. Any debate generating RS changes is a nonsensical frame — the substrate has no integrity. PP-122 already addresses this: "If RS=0, no debate can generate further RS loss through §3.8 consequences." Extension: if RS=0, no debate-generated RS gain either — the substrate cannot respond to social co-movement when it is fully ruptured. PP-122 covers this with "RS=0 lockout applies to debate-generated changes in both directions."

---

## Thread + Temporal Findings Summary

| ID | Test | Severity | Description | Disposition |
|----|------|----------|-------------|-------------|
| TT-F-01 | 1 | P2 | POP at TS 50 is same-scene only; between-exchange use is temporally coherent but limited. No new rule needed — §6.15 ±1 TN Read modifier handles it. | None |
| TT-F-02 | 2 | P2 | Church self-investigation paradox: Church member using Thread in support of Church orator would trigger Church investigation of itself. | PP-121 — add exception |
| TT-F-03 | 3 | P2 | Debate-generated RS changes not subject to RS ceiling (100) or lockout (0) in current rules. | PP-122 — add to §6.5/§3.8 |
| TT-F-04 | 4 | **P1** | Past-axis Thread operation during Future-genre debate: temporal auto-effect contradicts argument frame; no rule governs. | PP-123 provisional — TN8 Read next exchange for both orators |
| TT-F-05 | 5 | P1 | RS=0 lockout: debate-generated RS changes not covered by lockout. At RS=0 (Rupture), debate RS changes should also be blocked. | PP-122 extension |

---

# PART 4: EDITORIAL FLAGS (New items requiring user decision)

| ID | Description | Blocks |
|----|-------------|--------|
| ED-087 | §6.14 Hybrid: TC clamped to 4–6 (PP-120 provisional) — confirm this is correct. Alternate: allow BG lobbying to pre-decide outcome (no clamp). | Hybrid scenarios where faction lobbying should be decisive |
| ED-088 | §6.15 Church self-investigation exception (PP-121) — confirm scope. Does exception apply only to ordained Church members, or to anyone acting under Church institutional authority? | Church Tribunal practitioner support scenarios |
| ED-089 | §6.15 Thread temporal axis conflict rule (PP-123) — confirm TN8 Read penalty is the right calibration. Alternative: −1D to both Argue rolls that exchange instead of Read penalty. | Thread-practitioner-as-orator scenarios |
| ED-090 | §3.8 passive RS consequences from debate: should ALL Grand Debates with Thread-sensitive subject matter generate RS change, or only those explicitly involving practitioner actions? Currently "if the consequence involves Thread-sensitive matters" — GM discretion is the gate. Confirm or tighten. | RS tracking consistency |
| ED-091 | BG orientation absent (GAP-DS-22): confirmed as intentional abstraction. Confirm no BG equivalent to Obscuring/Doubt Marker is needed (e.g., "faction Abstain as Doubt Marker analog"). | BG vote tactical depth |

---

# PART 5: PATCHES REQUIRED

## In-place patches to debate_system_redesign_v1.md:

| Patch | Location | Change |
|-------|----------|--------|
| PP-119 | §6.8, §6.9, §6.13 | (1) Update §6.8/6.9 to mark resolved items. (2) Add design note to §6.13: BG orientation absent by design; genre pivot between rounds permitted. |
| PP-120 | §6.14 Step 2 | Clamp Hybrid TC starting position to 4–6 (compromise zone). BG offset determines where within zone, not whether outcome is pre-decided. [PROVISIONAL] |
| PP-121 | §6.15 Heresy Investigation | Add exception: Church does not investigate its own ordained members using Thread in support of Church interests. Opposing factions may still file. [PROVISIONAL] |
| PP-122 | §6.5 and note in §6.10/§3.8 | Debate-generated RS changes subject to RS ceiling (100) and RS=0 lockout. At RS=0, no RS change from §3.8 fires in either direction. |
| PP-123 | §6.15 Between Exchanges | Past-axis Thread operation during Future-genre debate (or Future-axis during Past-genre): both orators' next Read roll uses TN 8. Applies only to operations with temporal auto-effects. [PROVISIONAL] |

## No in-place patches needed in other docs:
- params_threadwork: no change. Rules already handle RS ceiling and lockout.
- params_core: no change.
- state_transfer_spec: no change (Thread↔Debate cross-mode already documented).

---

# PART 6: REFERENCE CARD AUDIT

Cross-checking debate_ref_card_v1.md against v1.5 operative text:

| Card Section | Accuracy |
|-------------|---------|
| Genre/weight table | ✓ |
| Read result table | ✓ |
| Exchange flowchart | ✓ (all 7 steps) |
| CLASH formula | ✓ — includes orientation_weight=1.0 (Revealing) |
| COMPETITION | ✓ |
| DIVERGENCE | ✓ — includes negative-successes note |
| TIE | ✓ |
| OBSCURING WIN | ✓ |
| Conviction Track quick-math | ✓ |
| Proceeding types table | ✓ |
| §§6.11–6.15 scale variants | ✓ (all five summarised) |
| Probability table | ✓ |
| Presence modifier formula | ✓ — max(0,...) included |
| Derived values | ✓ |
| Domain Echo table | ✓ |
| Debate Fatigue / Total Victory | ✓ |
| **MISSING:** Thread temporal axis note | **Add one-line note to card §9: "Past-axis Thread op during Future-genre debate (or vice versa): both orators Read TN8 next exchange."** |
| **MISSING:** BG orientation absent note | Minor — card covers BG at high level only; acceptable omission |

---

# FINDINGS SUMMARY

**P1 findings: 3**
- HD-F-01: Hybrid TC can start at win threshold (pre-decided) → PP-120 clamps to 4–6
- TT-F-04: Past-axis Thread during Future-genre debate — no rule → PP-123
- TT-F-05: RS=0 lockout not covering debate-generated RS → PP-122 extension

**P2 findings: 6**
- FA-NEW-01/GAP-DS-22: BG orientation absent — confirmed intentional → PP-119 design note
- GAP-DS-26: BG genre pivot between rounds → PP-119 permits
- GAP-DS-27: Hybrid double-capping → resolved by PP-120 (clamp makes lobbying meaningful within zone)
- TT-F-02: Church self-investigation → PP-121
- TT-F-03: RS ceiling/lockout for debate → PP-122

**P3 findings: 4**
- GAP-DS-21: §6.8/6.9 stale → PP-119 cleanup
- GAP-DS-23: "Most relevant History" undefined → GM discretion, add note
- GAP-DS-25: Coalition last-member edge → GM ruling acceptable (no patch)
- FA-NEW-07: Total Victory not cross-referenced in §6.8 → PP-119 cleanup

**Editorial flags: 5 (ED-087 through ED-091)**

---
*End AUDIT-D-02 + SIM-D-05. Patches PP-119 through PP-123 to be applied in-place.*
