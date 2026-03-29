# VALORIA STRESS TESTS — BATCH 4
*Model: Sonnet 4.6 · Intensive simulation with NPC substitution and archetype gauntlet*
*Source: CP14 (canonical) · Modes: A=Isolation, B=Interaction, C=Full Scenario, D=Edge Case*
*Naming note: "Intelligibility" (§4.5) and "Coherence" (§5.10/§2.3) refer to the same 10→0 track. "ThS" (§5.9) is the separate 20→0 track. Inconsistency flagged as BUG-004.*

---

## PREFLIGHT: NAMING INCONSISTENCY (P1)

### BUG-004 · Dual naming of the 10→0 degradation track

| Location | Name used | Definition |
|---|---|---|
| §2.3 Derived Scores | Coherence | "10 (starting value); countdown to 0; measures how legible reality remains" |
| §4.5 | Intelligibility | "replaces the Coherence track. Measures how legible reality remains. Range 10→0" |
| §5.10 | Coherence track | "individual, 10→0, monstrous configuration at 0" |
| Glossary | ThS = "Coherence Degradation" | Confusingly assigns "Coherence" label to the 20→0 ThS track |

**Finding:** Two distinct tracks (10→0 and 20→0) share terminology. §4.5 establishes "Intelligibility" as the canonical rename of "Coherence" for the 10→0 track, but §5.10 and §2.3 did not update to this name. The glossary then uses "Coherence Degradation" for ThS (20→0), compounding the confusion.
**Fix required:** Standardize throughout: 10→0 track = **Intelligibility** (as §4.5 establishes). 20→0 track = **ThS (Thread Stability)** or **Thread Stability** throughout. Remove all uses of "Coherence" for either track.

---

## COVERAGE MATRIX — BATCH 4

| Test ID | Mechanic(s) | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status |
|---|---|---|---|---|---|---|---|---|
| BT4-01 | FR: Locking/Snapping | A+D | PRES | TT, ThS, CERT | Church/Varfell | Klapp (witness), Vaynard (target) | Practitioner, Inquisitor | Complete |
| BT4-02 | Past-Oriented Pulling + Fraying | A+D | PAST/CROSS | TT, ThS, TD | Revolution | Maret Uln | Practitioner |Complete |
| BT4-03 | Collective Thread lattice | B | PRES | TT, ThS | Revolution/Crown | Maret Uln (anchor), Lenneth (helper) | Practitioner |Complete |
| BT4-04 | ThS campaign velocity | A | CROSS | ThS | Any | GEN-04 | Practitioner | Complete |
| BT4-05 | Intelligibility countdown + dissolution residue | C | CROSS | INT, ThS, CERT | Church | Klapp | Practitioner (transforming) | Complete |
| BT4-06 | ThS + Certainty simultaneous crisis | D | CROSS | ThS, CERT | Any | GEN-05 | Practitioner | Complete |
| BT4-07 | Discovery Events (3× NPC substitution) | A+B | PRES | TS, CERT | Crown/Church/Hafenmark | Almud, Baralta, Lenneth | Multiple | Complete |
| BT4-08 | Torben Loyalty Clock + Tutoring Demand | C | FUT | TLK, IP, PI | Crown/Altonia | Torben, Elske, Ehrenwall | Faction Leader | Complete |
| BT4-09 | Ehrenwall Coup Trigger + Martial Law | C | PRES/FUT | FSTAT, PI | Löwenritter/Crown | Ehrenwall, Almud | Faction Leader, Knight | Complete |
| BT4-10 | Church TC 80 Territorial Seizure | C | PRES | TC, FSTAT | Church/Hafenmark/Crown | Himlensendt, Baralta | Faction Leader | Complete |
| BT4-11 | Archetype substitution gauntlet | B | PRES/CROSS | Multiple | All | All NPCs | All 9 archetypes | Complete |
| BT4-12 | Dissolution residue + Niflhel operative | D | PRES | INT, CERT, CE | Niflhel/Church | Olafsson | Inquisitor, Operative | Complete |

---

## BT4-01 · LOCKING AND SNAPPING (FORCED RESOLUTION)

**Mode A — Isolation + Mode D — Edge Cases**
**Archetypes:** GEN-04 (Attuned Practitioner, TS 55), Klapp as observer (CE 4, TS 31), Vaynard as target

### Input Space

| Variable | Range | Typical | Edge |
|---|---|---|---|
| FR pool (Spirit + History) | 3 + 5 = 8D base | 8D | 6D (low Spirit) / 14D (maxed) |
| TPS added | TS 55 → TPS 5 | +5D → 13D total | — |
| Ob (minimum 4) | 4–8+ | 5 (Personal) | 8 (Structural) |
| TT modifier | +0 (TT < 60), +1 (TT 60–79), +2 (TT 80+) | 0 | +2 |
| Wounds penalty | +0 to +4 | 0 | +4 (incapacitated) |

### Probability Table — FR by Scale

| Scale | Ob | Pool 13D | P(Overwhelming) | P(Success) | P(Partial) | P(Failure) |
|---|---|---|---|---|---|---|
| Object | 4 | 13D | ~66% (net≥8) | ~93% | ~5% | ~2% |
| Personal | 5 | 13D | ~50% (net≥10) | ~83% | ~12% | ~5% |
| Relational | 6 | 13D | ~35% (net≥12) | ~68% | ~20% | ~12% |
| Territorial | 7 | 13D | ~22% | ~50% | ~27% | ~23% |
| Structural | 8 | 13D | ~12% | ~34% | ~30% | ~36% |
| Personal + TT Rupturing (+2 Ob) | 7 | 13D | ~22% | ~50% | ~27% | ~23% |

### TT Consequence by Degree — Lock vs Dissolution

| Operation | Degree | TT Change | ThS Change | Other |
|---|---|---|---|---|
| Lock | Overwhelming | +2 | 0 | TS +1 |
| Lock | Success | +2 | 0 | — |
| Lock | Partial | +3 | −2 | Partial lock, GM sets scope |
| Lock | Failure | +4 | −2 | 2 Wounds to practitioner (no armour) |
| Dissolution | Overwhelming | +3 | 0 | Micro-Gap opens/closes in scene |
| Dissolution | Success | +5 | 0 | Gap forms, lasts 1 scene |
| Dissolution | Partial | +6 | −2 | Shifting Object; Gap stays open |
| Dissolution | Failure | +8 | −2 | Full Gap + Monstrous Incursion + Practitioner Incapacitated |

### Mode D — Edge Cases

**Edge-11 · Dissolution Failure cascade (P1)**
Setup: TT 72 (Fracturing band, +1 Ob to all Thread ops). Practitioner attempts Dissolution at Personal scale. Ob = 5 + 1 (TT) = 6. Pool 13D.
P(Failure) at 13D Ob 6: ~12%.
On Failure: TT +8 → TT 80. Gap tears. Monstrous Incursion immediately.
State after failure: TT 80 (now Rupturing — +2 Ob to all Thread ops permanently until reduced). Incapacitation. Active monstrous entity. TT entering Rupturing band triggers additional cross-clock effects: TC +2/season; IP +2/season.
**One failed FR Dissolution at TT 72 can push TT into Rupturing in a single action.**
Severity: P1. The chain is mechanically valid but produces a runaway cascade: failure generates the monstrous entity the practitioner was trying to destroy, creates a persistent Gap, and sends TT into the highest penalty band. The player had an 88% success chance — but the 12% failure path is campaign-ending for this encounter.
Proposed fix: No mechanical fix needed — this is correct and appropriately terrifying for Dissolution at high TT. Document explicitly in GM tools: "Dissolution attempts at TT > 60 carry existential risk. Always state the cascading consequence at session start."

**Edge-12 · FR on a Threadcut Being (P1)**
Setup: Practitioner attempts FR against a Mode 3 entity (Threadcut Being). Per §5.15: "Wounds cost additional sustained Thread work rather than conventional incapacitation Ob penalty. Coherence track does not apply."
But §5.7 says FR requires Diagnosis immediately preceding. And Diagnosis on monstrous entities reveals "mode, approximate Health, configuration type."
Finding: For Threadcut beings, the Wound penalty to Thread operations works differently — it is "sustained Thread work" rather than a flat Ob penalty. No mechanics are given for what "additional sustained Thread work" means in terms of Ob or dice.
Additionally: "Coherence track does not apply" to Threadcut beings — but FR uses Spirit + History for the pool. Spirit is unchanged. The Coherence bonus dice (up to +3D at low Coherence) would not apply to a Threadcut target's own pool if it were rolling — but what if the *practitioner* is at low Coherence? Do the practitioner's Coherence-track bonus dice apply?
Severity: P1 × 2:
(a) Wound-to-sustained-Thread-work conversion undefined.
(b) Coherence bonus dice applicability vs Threadcut targets ambiguous.
Proposed fix: (a) Each Wound on a Threadcut being: contact window shortened by 1 round (minimum 1 round) rather than +Ob. (b) Practitioner's own Coherence-track bonus dice always apply to the practitioner's pool — they are not contingent on the target's nature.

**Edge-13 · Klapp as involuntary observer (CE 4, TS 31)**
Setup: FR Dissolution fires in the same scene as Cardinal Klapp (CE 4, TS 31). Per §4.4, TS 30–49 perceives "active Thread operations in the scene."
Klapp perceives the FR. CE is at 4. CE 3+ triggers a TS growth check (per glossary). At CE 4, Klapp is already past the TS growth trigger.
Finding: CE 4 exceeds the CE 3 threshold. Has Klapp's TS growth check already fired? If CE 3 fires the check and CE 4 means it already happened, Klapp may already have TS 31+. But the GM reference table (§14.8) shows "Klapp | 31 | 4 | — | Trajectory B → C" — suggesting TS 31 is current with CE 4 still active.
Question: Does CE persist after firing the growth check, or is it consumed? And if CE 4 is shown as "trajectory B→C" — does that mean the check fired and succeeded (Trajectory B), and CE is now building toward 5?
Severity: P2. The CE lifecycle (does it reset after firing? does it accumulate indefinitely?) is not defined.
Proposed fix: CE is a cumulative track up to 5, not reset after firing. CE 3+ = first growth check fires. CE 4 = second check fires at a different threshold event. CE 5 = maximum — transformation arc begins.

---

## BT4-02 · PAST-ORIENTED PULLING + FRAYING BANE

**Mode A — Isolation + Mode D — Edge Cases**
**Archetype:** GEN-05 (TS 75, High-TS practitioner). NPC substitution: Maret Uln (Revolution, TS 50+)

### Input Space

| Variable | Range | Notes |
|---|---|---|
| TS requirement | 70+ | Hard floor — cannot attempt below |
| TT requirement | ≥ 40 | Second hard prerequisite |
| Pool (Spirit + History) | 8D+TPS | Spirit 4, History "Temporal Scholar" 3pts, TPS 7 = 4+6+7=17D |
| Ob by recency | 3–7+ | Same scene: 3, prior seasons: 7+ |
| TT cost | +3 minimum (any degree) | Non-negotiable |
| ThS cost | +3 additional (any degree) | On top of Pulling auto-effect |

### Probability Table — Past-Oriented Pulling

| Recency | Ob | Pool 17D | P(Overwhelming) | P(Success) | P(Partial) | P(Failure) |
|---|---|---|---|---|---|---|
| Same scene | 3 | 17D | ~93% (net≥6) | ~99% | ~0.5% | ~0.5% |
| Same session | 4 | 17D | ~85% | ~97% | ~2% | ~1% |
| Same week | 5 | 17D | ~73% | ~92% | ~6% | ~2% |
| Same season | 6 | 17D | ~56% | ~83% | ~13% | ~4% |
| Prior seasons | 7 | 17D | ~40% | ~70% | ~20% | ~10% |
| Prior seasons + TT 80 (+2 Ob) | 9 | 17D | ~16% | ~47% | ~30% | ~23% |

### ThS Accumulation per Past-Oriented Pull

**Base ThS per Pull = Pulling auto-effect (temporal: +1) + Past-Oriented additional (+3) = +4 ThS minimum per pull.**

At Partial degree: +4 ThS + degree penalty.
At Success: +4 ThS (auto-effect only, no additional degree cost for standard success).
At Overwhelming: +4 ThS.

*In 5 Past-Oriented Pulls (any degree): ThS loses 20 points — total current ThS.*

### Fraying Bane Threshold

**3+ Past-Oriented Pulls in one season → Fraying bane.**

| Season Ops Count | Fraying? | Net ThS loss | 
|---|---|---|
| 1 Past-Oriented Pull | No | −4 |
| 2 Past-Oriented Pulls | No | −8 |
| 3 Past-Oriented Pulls | **Yes** | −12+ |
| 4+ | Yes (active) | −16+ |

**Fraying effects:** All Thread ops +1 Ob, contact duration −1 round, Partial results produce micro-Gaps (TT +1 each).

**Combined effect of 3 POP in one season:**
- ThS: −12 (from 20: now ThS 8 → Fragmented band, −1D Memory-based)
- TT: +9 minimum (3 × TT +3)
- Fraying bane active: all subsequent ops +1 Ob

A practitioner who uses Past-Oriented Pulling aggressively enters Fragmented ThS and Fraying in the same season they begin.

### Mode D — Edge Cases

**Edge-14 · Orphaned Configuration deterioration (P2)**
When Past-Oriented Pulling succeeds, it creates an Orphaned Configuration — a present state whose causal history has been removed. Per §14.7 checklist: "Orphaned configuration deterioration: each orphaned configuration makes an Endurance check (TN 7, Ob 1) at accounting. Failure: configuration fragments (TT +1; perceptible wrongness at TS 30+)."
Finding: The "Endurance check" for an orphaned configuration is mechanically undefined. Configurations do not have Endurance scores. This appears to mean the GM rolls 1D, Ob 1 — but which die? What is the pool? It cannot be a character's Endurance (the character is not the configuration).
Severity: P1. Proposed fix: Orphaned configuration deterioration roll = 1d10, TN 7, Ob 1. Auto-roll by GM at accounting. Success: stable for one more season. Failure: TT +1 and TS 30+ perceive wrongness.

**Edge-15 · Past-Oriented Pulling against a Threadcut being (P1)**
Per §5.15: "Past-Oriented Pulling against a threadcut being: auto-produces a Gap (no temporal thread to pull against)."
Finding: This fires regardless of degree — even an Overwhelming success on a POP targeting a Threadcut being produces a Gap. Does the Overwhelming benefit (full effect, extended duration) still apply before the Gap forms? Or does the Gap formation replace the outcome?
Also: TT cost for a POP that auto-Gaps: is it TT +3 (POP minimum) + Gap escalation, or is the Gap itself the TT consequence?
Severity: P1. Two separate interactions undefined. Proposed fix:
(a) Overwhelming POP on Threadcut still produces Overwhelming effect (temporal pull succeeds) AND a Gap forms. The effect and Gap are simultaneous — you achieved what you intended AND broke the substrate.
(b) TT from the auto-Gap is additional to the POP cost: TT +3 (POP) + TT from Gap formation per TT level table.

**Edge-16 · Fraying bane + Prior Dissolution = compounding micro-Gaps (P2)**
Setup: Practitioner has Fraying bane active (from 3× POP in Season 1). In Season 2, they perform a Pulling operation that results in Partial success.
Fraying: "Partial results on any Thread operation produce involuntary micro-Gaps (TT +1 each)."
Standard Partial Pulling: TT +1. Fraying adds: TT +1 (micro-Gap). Total: TT +2 per Partial instead of TT +1.
If TT is at 59 and two Partial operations fire in the same scene: TT 59 → +2 → 61 → Fracturing band (was 60), crossing from Wakening into Fracturing. Operations are now +1 Ob for the rest of the session.
Finding: Fraying creates a threshold-crossing risk for practitioners already near TT band boundaries. The +1 per Partial is additive with standard Partial costs — confirmed, but the threshold-crossing consequence is not flagged in the Fraying description.
Severity: P2. Document: "Fraying practitioners near TT threshold boundaries risk pushing TT into the next band mid-scene."

---

## BT4-03 · COLLECTIVE THREAD LATTICE

**Mode B — Interaction Chain**
**Mechanics:** Collective Thread ops (§5.14), lattice construction, Belief conflict, co-movement scaling
**Scenario:** 4-practitioner lattice — Maret Uln (Anchor, TS 65), + 3 helpers
- Helper A: Cognition 4 (contributes +2D)
- Helper B: Cognition 3 (contributes +1D)  
- Helper C: Cognition 3, Conflicting Belief (contributes +1D, no chain on 10)

### Pool Construction

| Role | Contribution | Notes |
|---|---|---|
| Anchor (Maret Uln) | Spirit 4 + History 6 + TPS 6 = 16D | Full pool |
| Helper A | +floor(4÷2) = +2D | — |
| Helper B | +floor(3÷2) = +1D | — |
| Helper C | +floor(3÷2) = +1D | No chain on 10 (conflicting Belief) |
| **Total lattice pool** | **20D (18D chainable + 2D non-chainable)** | |

### Probability Table — Collective Territorial Weaving (Ob 4)

| Pool config | Ob | P(Success) | P(Partial) | P(Failure) | Expected Net |
|---|---|---|---|---|---|
| Anchor solo (16D) | 4 | ~87% | ~9% | ~4% | 5.3 |
| Full lattice (20D) | 4 | ~97% | ~2% | ~1% | 6.6 |
| Lattice – Helper A drops (17D) | 4 | ~91% | ~7% | ~2% | 5.6 |
| Lattice fracture (pool < 8D after drops, +1 Ob) | 5 | ~74% | ~18% | ~8% | — |

### Conflicting Belief Interaction

Helper C's dice "cannot chain on 10." They contribute to pool but prevent bonus cascades from their dice. Expected net reduction: a die that would chain on 10 produces approximately +0.03 net successes (the chain bonus). With 1D of non-chainable dice: negligible penalty in expectation (~0.03 net). Effectively zero.

**Finding F-22 (P3):** The Conflicting Belief mechanic has negligible expected value impact. With 1 conflicting Helper contributing 1D: −0.03 expected net. The narrative consequence is real but the mechanical consequence is nearly invisible. At 3 conflicting Helpers contributing 3D: −0.09 expected net — still negligible.
Severity: P3. The mechanic exists to narratively represent dissent but does not mechanically constrain the lattice. If the intent was to create meaningful decision around conflicting Beliefs in collective ops, a stronger mechanic may be needed (e.g., conflicting dice subtract rather than merely don't chain). Flag as design note.

### Co-Movement Scaling in Collective Operations

§5.14: "A 4-practitioner lattice produces correspondingly significant co-movement effects across all three dimensions."
**Finding F-23 (P1):** No scaling formula is provided. "Correspondingly significant" is GM narrative, not a mechanic. The co-movement d10 table and the automatic temporal/epistemic effects make no reference to participant count multipliers.
Does the d10 roll 4 times (once per practitioner)? Does each automatic effect fire once with increased severity? Is TT change multiplied?
Severity: P1. This is a gap in a core mechanic. Proposed fix: Define scaling explicitly:
- d10 co-movement: roll once but automatic effects (temporal/epistemic) fire once per participant beyond the Anchor (so in a 4-practitioner lattice: 3 additional auto-effects). Each fires from its own trigger table independently.
- TT cost: the operation's standard TT cost applies once, not multiplied. The additional co-movement effects are the scaling, not the TT.

### Mode D — Edge Case: Lattice Dissolution Under Fire

**Setup:** Combat scene. Anchor takes 1 Wound while maintaining lattice contact. Focus check fires (TN 7 Ob 1, Focus score in d10s).
Anchor Focus 3: P(Failure) = ~37%.
On failure: contact drops. Anchor's pool = 0. Lattice dissolves. Helpers' contact windows remain open — they are still in contact individually but have no Anchor.
**Finding F-24 (P1):** When the Anchor drops contact mid-lattice, what happens to the operation? Helpers cannot complete an operation solo (they contribute bonus dice, not lead operations). Does the operation fail automatically? Does a Helper with the next-highest TS become the new Anchor?
Severity: P1. Proposed fix: When Anchor drops contact, operation immediately fails (Failure degree). No Helper promotion to Anchor mid-operation. Each Helper's contact window expires naturally. No TT penalty beyond the auto-failure TT costs.

---

## BT4-04 · ThS CAMPAIGN VELOCITY

**Mode A — Isolation**
**Mechanic:** ThS 20→0 degradation rate across a 10-season campaign
**Profile:** GEN-04 (Attuned Practitioner, TS 55, uses Thread ops regularly — 2 per session average)

### ThS Loss Rate by Operation Type

From §5.9 ThS loss table:

| Operation | ThS Loss |
|---|---|
| Object scale | −1 (temporal auto-effect) |
| Personal scale Success/OW | −1 |
| Personal scale Partial/Fail | −1 + degree table |
| Relational scale (any) | −1 + degree table |
| Territorial scale (any) | −1 + degree table |
| Locking/Snapping | −2 + degree table |
| Past-Oriented Pull | −3 additional (stacks) |
| History Resonance risk die =1 | −1 |

### 10-Season Campaign Velocity (Standard Practitioner Profile)

**Assumption:** 2 Thread operations per session, 4 sessions per season = 8 ops/season.
Distribution: 50% Personal, 30% Relational, 20% Object. No FR or POP.

| Scale | Ops/season | ThS per op (avg) | Seasonal ThS loss |
|---|---|---|---|
| Object | 1.6 | −1 | −1.6 |
| Personal | 4 | −1 (Success avg; Partial ~20%) | ~−1.2/op → −4.8 |
| Relational | 2.4 | −1 + degree table. Relational Partial: +1 additional. Expected avg −1.3 | −3.1 |
| **Total seasonal loss** | 8 ops | — | **−9.5/season** |

Recovery: +2 ThS any season with no Thread ops in final session.
If practitioner takes one "rest session" per season: net −7.5/season.

| Season | ThS (start) | ThS (end) | Band |
|---|---|---|---|
| 1 | 20 | 12.5 | Fragmented (entering) |
| 2 | 12.5 | 5 | Fractured (entering) |
| 3 | 5 | 0 | **Crisis** |

**Finding F-25 (P1):** A standard attuned practitioner using Thread operations at a moderate pace (2/session) will hit ThS Crisis by Season 3. This is the equivalent of 12 campaign sessions — well within a single campaign arc.
The ThS track as designed means sustained practitioners cannot operate for more than 2–3 seasons without hitting Crisis. Either:
(a) This is intended (practitioners burn bright and burn out — the cost of power), OR
(b) The recovery rate (+2 ThS/rest season) is insufficient to sustain active practice past Season 3.

At 2 ops/session with 1 rest session/season: hits Crisis Season 3.
At 1 op/session with 1 rest session/season: ThS loss ≈ −4.75/season net. Hits Crisis Season 4.
At 1 op/session with 2 rest sessions/season: ThS loss ≈ −3.5/season. Hits Crisis Season 5–6.

**Only by severely rationing Thread use (1 op/session, 2 rest sessions) does a practitioner survive past Season 5.** This represents an extremely conservative play pattern.
Severity: P1. This requires design confirmation: is the ThS track intended as a campaign-arc countdown that reaches Crisis by Season 3 for active practitioners? If so, document this explicitly and design the Crisis resolution procedure for mid-campaign play. If not, either reduce ThS loss rates or increase recovery rates.
Proposed approach: Add mid-campaign ThS recovery option beyond the "no ops in final session" rule. Example: seasonal extended rest (full season of no Thread operations: +5 ThS instead of +2). This allows practitioners to sustain practice by cycling rest seasons.

---

## BT4-05 · INTELLIGIBILITY COUNTDOWN + DISSOLUTION RESIDUE

**Mode C — Full Scenario**
**Mechanic:** Intelligibility (10→0), dissolution residue as power source (−1 Int per use), Coherence loss path
**NPC:** Klapp (Cardinal, TS 31, CE 4) — "Trajectory B→C" per §14.8 GM reference

### Character Profile: Klapp at Campaign Start

```
## State: Season 1, Start
Klapp — TS 31, CE 4, Intelligibility 10
Spirit 3, Presence 5, Cognition 4
Composure: 11 (Presence 5 + 6)
Belief: [EDITORIAL — unspecified; presumed Church doctrinal]
Thread pool: Spirit 3 + History 5 + TPS 3 = 11D
Fraying: Not active
```

**"Trajectory B→C"** — interpretation: Klapp is tracking from trajectory B (expanding institutional role, using CE accumulation to justify covert authority) toward trajectory C (discovery event — his CE 4 status means the next significant Thread exposure will trigger a TS growth check, potentially moving him to TS 30–49 effective operation range). But he's already at TS 31, so he IS in the Stirring range. Trajectory C may mean something else: full recognition that he has Thread sensitivity, or first Leap attempt.

### Scenario: Klapp uses dissolution residue to enhance an operation

Klapp has obtained dissolution residue from a Niflhel shipment (via Olafsson's connection). Residue Potency: 3.

**Operation:** Klapp attempts to use the residue to enhance a Pulling operation against a target (exposing a heretic's inner convictions). Standard pool: 11D.
With residue: +3D → 14D. Bonus dice explode on 9–10.

```
## Action: Residue-enhanced Pulling (Personal Firm, Ob 3)
Pool: 14D (11 standard + 3 residue), TN 7
Residue dice: explode on 9–10 (vs standard 10-only)
Cost: −1 Intelligibility immediately (declared before rolling)

P(Success): 14D vs Ob 3 → ~97%
P(Overwhelming): ~86%
Expected net: ~4.6

Intelligibility: 10 → 9

### Most likely outcome: Overwhelming
Target's conviction loosened; open to revision for scene.
```

```
## Action: Klapp uses residue again (same contact window — disallowed unless new window)
Per §5.11: "Maximum one use per contact window."

Klapp must re-Leap for a new contact window.
Second Leap: 11D vs Ob 2 (TS 30–49) → P(Success) ~97%
Second residue use: same source → +1 Ob per prior use → Ob for this operation +1.
−1 Intelligibility: 9 → 8

## Running total after 3 separate operations with residue use each:
Intelligibility: 10 → 9 → 8 → 7
```

### Intelligibility Cascade: When Does It Matter?

| Intelligibility | Threshold | Effect |
|---|---|---|
| 10–8 | Coherent | No penalty. Per §4.5 (CP14 gap): no effects at 10–8 in the Intelligibility table |
| 7–5 | Strained | Knot strain +1 per 3 sessions. "Occasional perceptual slippage." |
| 4–3 | Fragmented | −1D social. Close Knots at wrongness threshold. |
| 2–1 | Fractured | −2D social. All Knots at wrongness. Involuntary perceptual events. |
| 0 | Illegible | Permanent condition unless reversed. Character becomes NPC. |

```
## State: End of Season 3 (continued residue use)
Klapp — Intelligibility 5 (Strained)
Knot strain: +1 per 3 sessions (across all Knots)
Composure: 11 (unaffected by Intelligibility)
Social D penalty: none yet (threshold 4)
Thread pool: unchanged (Intelligibility doesn't penalize Thread ops per §4.5)
```

**Finding F-26 (P1):** Intelligibility track does not penalize Thread operations. Only social rolls are penalized at 4–3. This means a practitioner can have near-zero Intelligibility while performing Thread operations at full dice — the degradation track penalizes social functioning, not Thread functioning. Coherence bonus dice at low Intelligibility (per §5.10) go in the *opposite* direction: +1D to +3D Thread ops at Intelligibility 7–9 through 2–3.

Wait — the §5.10 Coherence track states:
- "7–9: +1D to Thread operations"
- "4–6: +2D to Thread operations"
- "2–3: +3D to Thread operations"

But §4.5 (Intelligibility) has the *same range* (10→0) and *no* Thread bonus.

**This is the dual-track naming problem (BUG-004) producing a mechanical conflict.** Either:
(a) §5.10's bonuses apply to practitioners on the Intelligibility track (i.e., they are the same track) → at Int 7–9, practitioners get +1D to Thread ops (canon confirmation in §5.10), OR
(b) §4.5 governs the Intelligibility track with no Thread bonuses, and §5.10 describes a *separate* Coherence transformation path → two different tracks

The Klapp scenario changes radically depending on interpretation:
- If §5.10 applies: at Int 7, Klapp gains +1D Thread ops (becomes more effective as degraded)
- If §4.5 alone applies: Klapp gets no Thread bonus, only social penalties

**Severity: P1 (compounding BUG-004).** This must be resolved before CP15. The mechanics diverge significantly. Recommendation: §5.10 describes the *transformation path* (practitioners actively choosing monstrous development), §4.5 describes the *passive degradation path* (practitioners inadvertently losing coherence). They are separate tracks, both at 10→0, but with different triggers and effects.

---

## BT4-06 · ThS + CERTAINTY SIMULTANEOUS CRISIS

**Mode D — Edge Case Discovery**
**Profile:** GEN-05 (TS 82, Sensitive practitioner, Spirit 3). Season 3.

```
## State: Season 3, Session 8
ThS: 3 (Severed — entered this session from Fractured)
Certainty: 1 (one point from Rendering Crisis at 0)
```

### ThS Severed (3–1) + Certainty Near-Zero

**ThS Severed effects:** −3D Memory-based rolls. Dissociative episodes once per scene regardless of ops.

**Certainty loss triggers (§4.6):** Successful Leap −1. Witnessing monstrous entity −1 (Spirit check TN7 Ob1). Non-consensual Thread work on sentient −1.

This practitioner performs a Leap (Certainty −1 → 0 → Rendering Crisis), while simultaneously in ThS Severed (dissociative episodes, −3D Memory).

### Rendering Crisis at Certainty 0

Per §4.6: "A scene event. The character's rendering of reality has become unstable. They must resolve the dissonance narratively: revise a Belief, withdraw from Thread-active situations, or find a new framework."

**ThS Crisis at 0:** "Campaign event. The character must resolve the disjunction narratively — sustained engagement with the world's rendered state — or withdraw from practice until ThS rises above 5."

Both Crises are "campaign events" requiring narrative resolution. Both fire simultaneously.

**Finding F-27 (P1):** No rule exists for resolving simultaneous ThS Crisis and Certainty Rendering Crisis. These are both "campaign events" that require narrative resolution, but they have *different resolution conditions*:
- Certainty Rendering Crisis: "revise a Belief, withdraw, or find new framework"
- ThS Crisis: "sustained engagement with rendered state OR withdraw until ThS > 5"

These are not the same resolution. "Sustained engagement" (ThS) and "withdraw" (Certainty) are *contradictory* — one requires remaining in the world, the other recommends withdrawal.

**Severity: P1.** Proposed resolution: When both Crises fire simultaneously, the character enters a **Combined Crisis** where:
1. The player must first address Certainty Rendering Crisis (Belief revision — this is a single-scene declaration)
2. Then address ThS Crisis (sustained engagement — this is a multi-season commitment)
The Certainty resolution does not clear the ThS requirement. Both must resolve independently.

### Additional Edge: Certainty Maximum Reduction at Low Intelligibility

Per §4.6: "Intelligibility reaching 4 or below: −1 to Certainty maximum per Intelligibility level below 5."
At Intelligibility 3: Certainty maximum = Spirit − 2. At Spirit 3: maximum Certainty = 1. Character cannot restore Certainty above 1 while Int remains ≤ 3.

**Finding F-28 (P2):** The Certainty maximum reduction from low Intelligibility creates a soft ceiling. A practitioner at Int 3 with Spirit 3 has maximum Certainty 1 — one Leap or one monstrous entity encounter immediately triggers Rendering Crisis (Certainty → 0), regardless of any other actions.

Combined with the simultaneous crisis finding: these characters are in perpetual Rendering Crisis. They cannot escape it while Intelligibility remains low.
Severity: P2. This may be intentional (heavily degraded practitioners face permanent crisis) but it needs documentation: "A practitioner with Intelligibility ≤ 3 and Spirit 3 is in permanent Rendering Crisis risk. Recovery requires Int restoration above 4 before Certainty maximum increases."

---

## BT4-07 · DISCOVERY EVENTS — NPC SUBSTITUTION × 3

**Mode A + Mode B**
**Protocol:** Identical scenario. Three NPC substitutions. Outcome comparison.

### Scenario Setup (Constant)

**Event:** A practitioner (GEN-04, TS 55) performs a Relational-scale Weaving in a scene. Per §14.6: "Weaving or Pulling at Relational scale or above: always triggers [Discovery Event] for observers with TS 10–39."

Three NPCs are present as observers. Each tested independently in the same scenario.

### NPC-A: Almud (TS 28, Near Stirring)

```
Almud — Spirit 3, TS 28, no Devout foreclosure
Discovery Event trigger: TS 10–29 → qualifies
Roll: Spirit check TN 7 Ob 1 → 3D vs Ob 1 → P(Success) ≈ 73%

### Case 1: Success (73% likely)
Almud holds the confrontation. TS +5 → TS 33.
TS now 33: Stirring range (30–49).
TS 33 from TS 28 = crossed the 30 threshold.
Spontaneous Breakthrough check fires: additional Spirit check TN 7 Ob 2 → 3D vs Ob 2 → P(Success) ≈ 32%
  - If Breakthrough succeeds: Approach Training acquired. Almud can now Leap.
  - If Breakthrough fails: TS 33, no Approach Training. Standard path required.

### Case 2: Failure (27%)
Almud represses. No growth. Next equal/lesser event fires automatically (no check required).
GM notes: next monstrous entity encounter, Originary Lock, or Relational+ Weaving auto-advances.
```

**Key finding:** Almud's near-Stirring status means one Discovery Event has a 23% chance of granting him the ability to Leap (the 73% × 32% path). This is the "politically compromised monarch accidentally becoming a practitioner" arc — a major campaign event with no advance warning from any GM-facing threshold.

### NPC-B: Baralta (TS 0, Devout)

```
Baralta — Spirit 4, TS 0, active Devout Constraint (Categorical Imperative theology)
Discovery Event: TS 0–9 → does NOT qualify for standard trigger
Per §14.6: triggers only for "TS 10–39." Baralta is at TS 0.

### Outcome: No Discovery Event fires for Baralta.
She perceives nothing (TS 0 → invisible to Thread operations, §5.2).
No Devout Dissonance Event (that requires a successful Discovery Event first).
```

**Finding F-29 (P2):** Non-sensitive observers (TS 0–9) never trigger Discovery Events. The threshold for Discovery Event qualification is TS 10–39 — explicitly excluding TS 0–9 characters. Baralta is permanently immune to Discovery Events unless her TS first rises to 10, which requires a qualifying confrontation check. But TS growth checks are blocked by the Devout Constraint.

This creates a deadlock: Devout characters cannot gain TS through confrontation (Constraint blocks), and cannot trigger Discovery Events (TS too low). The only break path is §4.4: "Discovery Events bypass this for the initial check (the experience is involuntary)." But §14.6 says Discovery Events only trigger for TS 10–39 — so Baralta doesn't reach Discovery Event territory at all.

Severity: P2 — deadlock seems to contradict the Devout "involuntary bypass" provision. Either Devout bypass should work at TS 0–9 too (i.e., any involuntary confrontation can fire a TS check for a TS 0 character), or the TS 10–39 trigger range in §14.6 needs a specific Devout exception.

### NPC-C: Lenneth (TS 0, No foreclosure, Scholarly Path)

```
Lenneth — Spirit 4, TS 0, not Devout (no theological foreclosure)
Discovery Event: TS 0–9 → does NOT qualify (same as Baralta)

### Same outcome as Baralta: no Discovery Event fires.
```

However, Lenneth's scholarly path allows TS growth through intellectual engagement. §4.4: "Qualifying events: deep study of Thread-operation records, analysis of temporal anomalies, decoding Originary inscriptions." These are *different* qualifying events from the standard confrontation path — not the same as witnessing a live operation.

**Finding F-30 (P2):** Lenneth cannot gain TS from witnessing Thread operations (TS 0–9 exclusion from Discovery Events). She gains TS through scholarly activity (different qualifying event type). So the scenario where Lenneth watches a Weaving and gains TS is explicitly not the system — she needs to study the written record of it afterward, not witness it directly.

This is philosophically correct (her path is intellectual, not experiential) but may surprise tables who expect all characters to potentially gain TS from powerful Thread events.

### Comparative Results

| NPC | TS | Devout | Discovery Event fires? | Outcome |
|---|---|---|---|---|
| Almud | 28 | No | Yes (23% → Approach Training possible) | Major arc risk |
| Baralta | 0 | Yes | No | Completely immune |
| Lenneth | 0 | No | No | Immune by TS range (not Devout) |

**P1 FINDING — F-31: Devout bypass rule is unreachable (P1)**
The Devout Constraint says "Discovery Events bypass this for the initial check." But Discovery Events only fire for TS 10–39. A TS 0 Devout character never reaches the bypass because they never trigger a Discovery Event. The bypass provision is mechanically unreachable unless it applies differently from standard Discovery Events.
**Fix:** Add explicit note: "For Devout characters at TS 0–9, an involuntary direct Thread exposure (being targeted by a Thread operation, physical contact with an Originary Lock, surviving a monstrous entity encounter) triggers a TS growth check even without the TS 10+ qualifier. This is the Devout bypass."

---

## BT4-08 · TORBEN LOYALTY CLOCK + TUTORING DEMAND

**Mode C — Full Scenario**
**NPC substitution:** Torben (primary), Elske (alternative path), Ehrenwall (coup threshold assessor)

### Starting State

```
## State: Season 1, Campaign Start
### Clocks
TT 28 | TC 22 | IP 20

### Tracks
Torben Loyalty Clock (TLK): 8 (loyal to Valoria)

### Characters
Torben — in Altonia, in Altonian court. Not yet under formal demand.
Elske — married to Altonian Duke, embedded in Altonian society.
Crown (Almud) — M5 I5 W4 Mil4 Stab4
```

### IP 30 Trigger: Tutoring Demand

**IP crosses 30 in Season 4** (passive drift +2/season from starting 20 + cross-clock contributions).

```
## State: Season 4
IP: 32 (crossed 30)

Tutoring Demand triggers: Altonian court formally requests Torben receive "Altonian education" (supervised 2-year residency under Almaic Kyriakos).

### Crown Response Options:
A. Comply → TLK begins decreasing immediately. Torben enters Altonian sphere.
B. Refuse → IP +2 (additional direct trigger: "succession ratification delayed" is proximate). 
   Crown Mandate check Ob 2 at accounting (diplomatic pressure). IP now 34.
C. Negotiate delay → Circles Ob 3 to find diplomatic lever. Success: buys 1 season.
   Failure: IP +1 (weakness shown). Demand repeats at Season 5.
```

### TLK Deterioration Path if Crown Complies

| Season | TLK | State | Effects |
|---|---|---|---|
| 4 | 8 | Homesick | No mechanical effect |
| 5 | 7 | Homesick | No mechanical effect |
| 6 | 6 | Homesick (floor) | No effect until threshold |
| 7 | 5 | Adapting | Crown Mandate −1. Retrieval requires Altonian consent or covert extraction. |
| 8 | 4 | Adapting | Crown Mandate −1 (cumulative −1, same band) |
| 9 | 3 | Altonia-aligned | Crown Mandate −1 again (cumulative −2). Coup trigger #2 arguably met. |
| 10 | 2 | Altonia-aligned | — |

**If TLK reaches 1:** Torben is an Altonian puppet. Coup trigger #2 definitively met → Ehrenwall activation.

### Elske Path (Alternative Succession)

If Torben is alienated (TLK ≤ 3), Elske becomes the viable succession alternative. Players must recruit her via:
- Circles Ob 3 (Altonian territory)
- Social scene: Appeal or Debate (3 exchanges) targeting Family or Self-Determination conviction
- Her Resonant Style: Evidence → show concrete proof, not appeals

**Recruitment probability (Appeal vs Elske, Evidence Style, Ob 3):**
Pool: Presence 4 + History "Diplomacy" 5 = 9D. P(Success) ≈ 73%. On Partial: she requires something additional before acting.

### Ehrenwall Coup Threshold Assessment

```
## Finding F-32 (P1): Coup trigger #2 has no defined activation point

§8.9 (Löwenritter): "Grandmaster Ehrenwall is keeping count of Almud's compromises. When the Löwenritter's internal assessment of the Crown's institutional integrity drops to a threshold (tracked as a private GM counter), a coup trigger is possible."

TLK 3–2: "Coup trigger #2 arguably met." (§13.1 NPC — Torben Loyalty Clock table)
TLK 1: "Coup trigger #2 definitively met." (Same table)

But: the Coup Threshold is a "private GM counter." What is its value? What constitutes a "compromise" that decrements it? How many compromises trigger the coup?
```

**Severity: P1.** The coup trigger is a central campaign mechanic (Martial Law, Crown suspension) with no mechanical definition. "Arguably met" vs "definitively met" vs "counter drops to threshold" are three different framings that don't connect to a single procedure.

**Proposed fix:**
Define the counter explicitly:
- Starting value: 5 (Ehrenwall's assessment of the Crown's institutional health)
- Decrements by 1 for each qualifying compromise:
  - Crown fails to respond to Altonian demand (−1)
  - TLK reaches 5 or below (−1)
  - Crown acts against Constitutional procedure without Parliament approval (−1)
  - Crown publicly supports practitioners (−1)
  - Church excommunicates a Crown official and Crown accepts (−1)
- At 0: Coup trigger fires. Ehrenwall presents demands; if refused within one season, Martial Law is imposed.

---

## BT4-09 · EHRENWALL COUP TRIGGER + MARTIAL LAW

**Mode C — Full Scenario with Archetype Substitution**
**NPC substitution:** Ehrenwall (Löwenritter Knight archetype), Almud (Faction Leader archetype)

### Coup Trigger Point

Using the proposed counter from BT4-08: Crown has accumulated 5 compromise points. Counter at 0.

```
## State: Season 8
### Clocks
TT 45 | TC 52 | IP 38

### Factions
Crown — M4 I5 W4 Mil4 Stab4 (weakened by sustained pressure)
Löwenritter — Mil5 Intel3 Influence3 Stab5

### Coup Counter: 0 (threshold reached)
```

**Ehrenwall presents formal demands:**
1. Almud must publicly reaffirm Crown constitutional obligations
2. Almud must act against one named compromise (revoke a Church concession, or recall Torben if TLK ≤ 3)
3. Almud has 1 season to comply

```
## Crown response paths:

### Path A: Comply
Coup counter resets to 2 (trust partially restored).
Almud takes one of the two actions. The other remains unresolved.
IP: may change if Altonian demand is countermanded (−1 to +2 depending on action).

### Path B: Refuse
After 1 season: Martial Law imposed on Crown territories.
Martial Law: "suspending normal Domain Action resolution and replacing it with Military-based Stability enforcement."

### Martial Law Mechanics (P1 Finding F-33)
"Replacing with Military-based Stability enforcement" — no further specification.
What does Military-based resolution look like? Which Domain Actions are suspended? 
Are social actions (Debates, Appeals) still available? Can Church operate in Martial Law territory?
```

**Severity: P1.** Martial Law is referenced as a campaign-level event but has no mechanical procedure. **Proposed procedure:**
During Martial Law seasons in Crown territories:
- All Domain Actions by other factions targeting those territories: Ob = Crown Military ÷ 2 (round up) additional
- Church cannot open Inquisitions in Martial Law territories (Military supersedes ecclesiastical authority)
- All Circles checks in Martial Law territories: +1 Ob (movement restricted)
- Löwenritter acts as sovereign power: their Military substitutes for Crown Military in all calculations
- Martial Law ends when Coup Counter reaches 3+ (restored trust) OR when Löwenritter Military drops to 0 (military defeat)

---

## BT4-10 · CHURCH TERRITORIAL SEIZURE AT TC 80

**Mode C — Full Scenario**
**Mechanic:** TC 80 threshold event — Church attempts territorial seizure through institutional claim

```
## State: Season 9
### Clocks
TT 42 | TC 81 (just crossed 80) | IP 32

### Active Conditions
Baralta's TC suppressor active (Mandate 4+)
But TC already crossed 80 — suppressor applies to generation rate, not threshold event
```

**Finding F-34 (P1): TC 80 seizure procedure is not fully specified**

§7.2: "At TC 80, the Church may attempt to seize territories through institutional claim rather than military force. Per-territory roll vs variable Ob. Counter-play options available. (See Faction section for full procedure.)"

**The Faction section does not contain this procedure.** The Stage 6 compilation and CP14 Faction section for the Church (§8.3) do not include a territorial seizure procedure. The reference "See Faction section" points to content that was not written.

Severity: P1. This is a major endgame mechanic with no implementation. The seizure is referenced in two places (§7.2 and §8.3) with identical "full procedure elsewhere" references, but the procedure doesn't exist.

**Proposed procedure (design draft for editorial review):**
- Church may declare seizure on one territory per season at TC 80+
- Roll: Church Mandate vs Ob = that territory's controlling faction's Mandate ÷ 2 (round up) + Stability ÷ 2 (round up)
- Counter-play: controlling faction may resist via Domain Action (matching roll) within the same season
- Outcome on uncontested Church success: territory adds +1 to Church's TC-driven Mandate and loses 1 faction Influence for the controlling faction. Not military occupation — institutional authority transfer.
- Church may not seize: Hafenmark (Baralta's constitutional claim creates Ob +3), territories with active military defence (Military 4+), Schoenland

---

## BT4-11 · ARCHETYPE SUBSTITUTION GAUNTLET

**Protocol:** 9 archetypes × 3 scenario types. Each archetype tested in a defining scenario using NPC substitution where applicable.

### S-01 COMBAT: Inquisitor (GEN-01) vs Riskbreaker (GEN-02)

```
## Profiles
GEN-01 Inquisitor: Agility 3, Endurance 4, Strength 2, Combat History "Inquisitor Training" 1pt = pool 3+4=7D
GEN-02 Riskbreaker: Agility 4, Combat History "Irregular Warfare" 3pts = pool 4+6=10D

## Action: Combat, Round 1
Initiative: both roll Agility TN7 Ob1
GEN-01: 3D vs Ob1 → P(Success) 73% → likely wins/ties
GEN-02: 4D vs Ob1 → P(Success) 87%

Most likely: GEN-02 wins initiative (declares last).
```

```
## Pool Split Analysis:
GEN-01 (7D): Optimal split vs superior opponent:
  - Pure Defence (7D): Inquisitor survives longer, waits for opening.
  - 3D Offence / 4D Defence: P(1+ offence net success) ≈ 53% vs GEN-02's 6D defence
GEN-02 (10D): Optimal split:
  - 7D Offence / 3D Defence: P(Overwhelming offence) ≈ 55% vs GEN-01's 4D

## Probability of GEN-02 incapacitating GEN-01 in Round 1:
GEN-02 7D Offence vs GEN-01 4D Defence:
  GEN-02 expected net offence: 7×0.33 = 2.3
  GEN-01 expected net defence: 4×0.33 = 1.3
  Expected excess: 1.0 hit. Power 3 + weapon +1 + 1 excess − armour 2 = 3 damage.
  GEN-01 Health ≈ 10 (End 4 + 6). 3 damage in Round 1 does not incapacitate.

## Expected: 3 rounds to incapacitate GEN-01 under sustained 7/3 split.
```

**Finding F-35 (P2):** The Inquisitor archetype (GEN-01) is outmatched in direct combat against an active combat archetype (GEN-02) at approximately 2:1 combat pool ratio. Inquisitors' mechanical value is in investigation and social mechanics (Devout Constraint, heresy procedures) — not combat. This is correct design, but tables running combat-heavy campaigns will find Inquisitor PCs mechanically weak. Document in character archetype guidance.

### S-02 SOCIAL: Faction Leader (NPC-06 Baralta) vs Faction Leader (NPC-02 Himlensendt)

**Grand Debate (5 exchanges). Baralta challenges Church authority claim.**

```
## Profiles
Baralta: Presence 5, History "Constitutional Legalist" 3pts = social pool 5+6=11D
Resonant Style: Evidence. Conviction: Order.
Himlensendt: Presence 6, History "Theology" 3pts + "Political Negotiation" 2pts = 6+6=12D primary
Resonant Style: Consequence. Conviction: Faith.
```

**Renown interaction:** Both at institutional-peer tier (Baralta Renown ~6, Himlensendt Renown ~7). Per BT3-06 finding, Renown initial advantage is Exchange 1 only (P1 proposed fix). Himlensendt +2D Exchange 1 only: 14D vs 11D for that exchange.

```
## Exchange 1 (Himlensendt has Renown advantage):
Himlensendt: 14D (12 base + 2 Renown) vs Ob = Baralta's pool ÷ Ob structure
Baralta: 11D

Style selection critical:
  Baralta uses Evidence (her resonant style): Himlensendt does NOT gain resonant bonus
  Himlensendt uses Consequence (his resonant style): gains +1D from Baralta's engagement
  
If both play to their own resonant styles:
  Exchange 1 likely outcome: Himlensendt wins (12+2 vs 11D baseline → P(H wins) ~65%)
  
## Exchanges 2–5 (Renown advantage gone):
  Equal pools: 12D vs 11D → P(Himlensendt wins each) ~55%
  Expected wins in 5 exchanges: Himlensendt ~3, Baralta ~2.
  Himlensendt wins 3–2.
```

**Finding F-36 (P2):** In a straight Grand Debate between Baralta and Himlensendt with no style exploitation or character-level modifiers, Himlensendt wins approximately 3–2. Baralta's mechanical advantage (TC suppressor, Sovereign Authority Doctrine) is not a Debate mechanic — it is a separate faction action. Within pure Debate mechanics, the Church leader's higher Presence wins.

To beat Himlensendt, Baralta needs:
- Resonant style exploitation: Baralta targets Himlensendt's Consequence style for 5 exchanges (+1D each) → 12D vs 12D → effectively equal
- Evidence manipulation: presenting physical proof Himlensendt cannot dismiss (Ob reduction on his roll)
- Inspiration stunt: a stunt using her Conviction (Order) in Exchange 3 at Ob 3 → adds Spirit auto-successes + bonus dice

### S-03 THREAD OPERATION: GEN-04 (Attuned) → Observer: GEN-09 (Non-sensitive civilian)

**Scenario:** GEN-04 performs Weaving (Personal scale, Ob 2). GEN-09 is present.

```
## GEN-09 profile: TS 0. Non-sensitive civilian.
## Thread perception: nothing (TS 0–9 perceives nothing).
## Effect on GEN-09: The wound closes. Physical effect visible to all.

Co-movement d10 roll: 7
Effect: Epistemic bleed — witnesses disagree on one factual detail of what just happened.
GEN-09 and other non-sensitive witnesses: +1 Ob to investigation or Circles about this scene.
```

**Finding F-37 (P2):** Non-sensitive characters can be affected by co-movement epistemic effects (d10 result 7) even when they perceive nothing of the Thread operation. The physical healing is visible; the epistemic bleed distorts their memory of *how* it happened. This correctly models P-08 (epistemological barrier) — they experienced the effect without access to the cause.

### Archetype Summary Table

| Archetype | Defining Scenario | Key Finding | Severity |
|---|---|---|---|
| GEN-01 Inquisitor | S-01 Combat | Combat pool ~7D — mechanically weak vs combat archetypes | P2 |
| GEN-02 Riskbreaker | S-01 Combat | Combat pool ~10D — dominant in combat, effective; correct | OK |
| GEN-03 Knight Templar | S-01 Combat (group) | Immunity to Brutal morale, +1D Cohesion vs Thread events — but no personal stats defined | P2 (gap) |
| GEN-04 Attuned Practitioner | S-03 Thread | Full Thread capability; ThS burn rate severe (BT4-04) | P1 |
| GEN-05 High-TS | S-03 Thread + FR | Fraying bane trigger fast; simultaneous crisis risk (BT4-06) | P1 |
| GEN-06 Restoration Seeker | S-02 Social | No unique mechanics defined beyond standard social — no dedicated rules for black market Thread goods | P2 (gap) |
| GEN-07 Niflhel Operative | S-01 Combat | Combat pool undefined — Niflhel uses Intel Domain Actions, not personal combat | P2 (gap) |
| GEN-08 Political Operative | S-02 Social | Well-specified; social pool 11D; Debate-optimized | OK |
| GEN-09 Non-sensitive civilian | S-03 Thread witness | Co-movement effects land even without perception (correct) | OK |

**Finding F-38 (P1):** Three archetypes (GEN-03 Knight Templar, GEN-06 Restoration Seeker, GEN-07 Niflhel Operative) have no personal-scale mechanics defined. The auditing matrix lists them as archetypes requiring testing, but the ruleset provides no personal attribute ranges, combat pool baselines, or unique mechanic specifications for these character types. They exist as faction archetypes but not as playable character mechanical templates.
Severity: P1. These archetypes must be defined before CP15 if players are expected to play them. Minimum specification needed: attribute range, typical History, unique mechanical tag.

---

## BT4-12 · DISSOLUTION RESIDUE + NIFLHEL OPERATIVE INTERACTION

**Mode D — Edge Case Discovery**
**NPC substitution:** Olafsson (Cardinal of Justice, Church, Niflhel connection active)
**Archetype:** GEN-07 Niflhel operative + GEN-01 Inquisitor

### Residue Supply Chain

Niflhel harvests Thread-touched goods from the Southernmost. These include dissolution residue. Per §5.11: "Niflhel Southernmost operations" are a source of residue. CE +1 per extended handling session for non-practitioners.

```
## Olafsson profile: TS 0, CE 1 (starting per GM reference: "Niflhel connection active")
## CE mechanics: non-practitioner track, 0–5. At CE 3: TS growth check triggers.

Extended handling of residue shipment:
CE +1 per extended handling session. Three shipments in Season 2:
CE: 1 → 2 → 3 → TS growth check fires.

## TS growth check (CE 3): Spirit TN7 Ob1
Olafsson Spirit (assumed ~3): 3D vs Ob1 → P(Success) 73%

On Success: TS +5. Olafsson: TS 0 → 5 (Inert range — no perceptual change yet).
On Failure: Character represses. Next equal/lesser intensity: auto-fires.
```

**Finding F-39 (P2):** Olafsson's TS growth through residue handling CE accumulation means a senior Church official who oversees Niflhel operations will inadvertently develop Thread sensitivity. By Season 2, he has a 73% chance of reaching TS 5. By Season 4–5, continued handling could bring him to TS 10 (Dormant — passive perception begins). This is not a player-directed arc — it is an NPC trajectory driven by institutional behavior.

**Finding F-40 (P1):** The CE track mechanics are incompletely specified:
- CE accumulates from: "handling residue (per session)" and "Thread operation performed on observer (+2 CE)." 
- At CE 3: TS growth check fires.
- No rule for what happens at CE 4 or CE 5 (Klapp's starting CE is 4 — above the trigger threshold).
- No rule for CE accumulation rate from different exposure types (handling vs witnessing vs direct Thread work on character).
Severity: P1. The CE track for NPCs is referenced in the GM reference sheet (§14.8) with starting values but no accumulation procedure past CE 3.

**Proposed procedure:**
- CE 1: First handling or witnessing session
- CE 2: Repeated exposure (one per 2 sessions of regular contact)
- CE 3: Significant exposure (TS growth check fires)
- CE 4: Direct Thread work on this character by a practitioner, or 5+ sessions of residue handling
- CE 5: Transformation threshold — character is in persistent Thread contact. Spirit check TN7 Ob2 or permanent perceptual shift.

---

## MASTER FINDINGS REGISTER — BATCH 4

| ID | Test | Severity | Description | Action |
|---|---|---|---|---|
| BUG-004 | Preflight | P1 | Dual naming: "Intelligibility" (§4.5) and "Coherence" (§5.10/§2.3) are the same 10→0 track. ThS Glossary uses "Coherence Degradation" for the 20→0 track. Needs standardization. | Fix naming throughout |
| Edge-11 | BT4-01 | P1 | Dissolution Failure at TT 72 → TT +8 → TT 80 in one action; Rupturing band enters; TC/IP cross-clock cascade. Design correct but must be documented. | GM tools note |
| Edge-12a | BT4-01 | P1 | Threadcut Being: Wound-to-sustained-Thread-work conversion undefined | Define: −1 contact round per Wound |
| Edge-12b | BT4-01 | P1 | Practitioner Coherence bonus dice vs Threadcut target: ambiguous | Clarify: practitioner's own track always applies to their pool |
| Edge-13 | BT4-01 | P2 | CE lifecycle post-threshold: does it reset, persist, or accumulate? | Define: CE persists and accumulates to 5 |
| Edge-14 | BT4-02 | P1 | Orphaned configuration "Endurance check": configurations have no Endurance score. Roll undefined. | Fix: 1d10 TN7 Ob1 GM roll at accounting |
| Edge-15 | BT4-02 | P1 | POP on Threadcut: auto-Gap + POP effect simultaneous? TT stacking unclear. | Fix: both fire simultaneously; TT stacks |
| Edge-16 | BT4-02 | P2 | Fraying bane + Partial = double TT near thresholds — undocumented | Add to Fraying description |
| F-22 | BT4-03 | P3 | Conflicting Belief in lattice: ~−0.03 expected net — mechanically negligible | Design note |
| F-23 | BT4-03 | P1 | Collective co-movement scaling: "correspondingly significant" undefined | Fix: auto-effects fire once per helper beyond Anchor |
| F-24 | BT4-03 | P1 | Anchor drops contact mid-lattice: no rule for operation outcome | Fix: auto-Failure; no Helper promotion mid-op |
| F-25 | BT4-04 | P1 | ThS Crisis by Season 3 for active practitioners at standard play rate | Design confirmation needed; add seasonal extended rest |
| F-26 | BT4-05 | P1 | Intelligibility track has no Thread operation penalty; §5.10 grants Thread BONUSES at low Coherence. Contradicts §4.5. Compounding BUG-004. | Resolve naming + define which track grants bonuses |
| F-27 | BT4-06 | P1 | ThS Crisis + Certainty Rendering Crisis fire simultaneously: contradictory resolution conditions | Fix: Combined Crisis; Certainty resolves first (scene); ThS resolves second (campaign arc) |
| F-28 | BT4-06 | P2 | Low Int + low Spirit = permanent Rendering Crisis trap | Document: requires Int restoration above 4 first |
| F-29 | BT4-07 | P2 | Baralta: Devout bypass provision unreachable (TS 0–9 excluded from Discovery Events) | Fix: Devout bypass applies at TS 0–9 for involuntary direct exposure |
| F-30 | BT4-07 | P2 | Lenneth: cannot gain TS from witnessing Thread ops (TS 0–9 exclusion correct, scholarly path different) | Document explicitly |
| F-31 | BT4-07 | P1 | Devout bypass rule is mechanically unreachable in current Discovery Event trigger range | Fix: add explicit TS 0–9 Devout exception |
| F-32 | BT4-08 | P1 | Coup counter: "private GM counter" with no defined value, no decrement triggers, no threshold | Define counter from 5 with explicit decrement triggers |
| F-33 | BT4-09 | P1 | Martial Law: "Military-based Stability enforcement" undefined | Define full procedure |
| F-34 | BT4-10 | P1 | Church TC 80 territorial seizure procedure referenced but does not exist in faction section | Write procedure |
| F-35 | BT4-11 | P2 | Inquisitor archetype: combat pool ~7D — mechanically weak in combat (correct design, needs documentation) | Character guidance note |
| F-36 | BT4-11 | P2 | Baralta loses straight Debate vs Himlensendt; must exploit style or use Inspiration to win | Document: social mechanics reward preparation and style reading |
| F-37 | BT4-11 | P2 | Non-sensitives affected by epistemic co-movement even without Thread perception (correct per P-08) | Document as design note |
| F-38 | BT4-11 | P1 | Three archetypes (GEN-03, GEN-06, GEN-07) have no personal-scale mechanics defined | Define min spec before CP15 |
| F-39 | BT4-12 | P2 | Olafsson: inadvertent TS development through residue handling — NPC trajectory emerges from institutional behavior | Document as campaign-arc NPC development path |
| F-40 | BT4-12 | P1 | CE track past CE 3: no accumulation procedure defined for CE 4–5 | Define CE procedure through CE 5 |

---

## P1 FINDINGS SUMMARY — BATCH 4 (17 items)

| # | Finding | Source | Fix Type |
|---|---|---|---|
| 1 | BUG-004: naming inconsistency Intelligibility/Coherence/ThS | Preflight | Text fix throughout |
| 2 | Edge-12a: Threadcut Wound-to-Thread-work undefined | BT4-01 | Rule addition |
| 3 | Edge-12b: Coherence bonus vs Threadcut target | BT4-01 | Clarification |
| 4 | Edge-14: Orphaned config Endurance check undefined | BT4-02 | Rule addition |
| 5 | Edge-15: POP on Threadcut simultaneous effects | BT4-02 | Clarification |
| 6 | F-23: Collective co-movement scaling formula missing | BT4-03 | Rule addition |
| 7 | F-24: Anchor drops mid-lattice: no outcome rule | BT4-03 | Rule addition |
| 8 | F-25: ThS Crisis by Season 3 at standard play | BT4-04 | Design confirmation + recovery option |
| 9 | F-26: Intelligibility track vs §5.10 Coherence bonus dice conflict | BT4-05 | Requires BUG-004 resolution |
| 10 | F-27: ThS Crisis + Certainty Rendering Crisis simultaneous | BT4-06 | Rule addition |
| 11 | F-31: Devout bypass unreachable at TS 0–9 | BT4-07 | Rule clarification |
| 12 | F-32: Coup counter mechanics undefined | BT4-08 | Rule addition |
| 13 | F-33: Martial Law procedure undefined | BT4-09 | Rule addition |
| 14 | F-34: Church TC 80 territorial seizure procedure missing | BT4-10 | Write procedure |
| 15 | F-38: GEN-03/06/07 archetypes have no personal-scale mechanics | BT4-11 | Spec addition before CP15 |
| 16 | F-40: CE track past CE 3 undefined | BT4-12 | Rule addition |
| 17 | Edge-12b (combined with F-26) | BT4-01/05 | Linked to BUG-004 |

---

*End Batch 4. 12 mechanics tested. 17 P1 findings. 10 P2 findings. 3 P3 findings.*
*Combined Batch 3+4: 22 mechanics tested. 27 P1 findings. 28 P2 findings. 10 P3 findings.*
*Critical cluster for CP15 gate: BUG-004, F-25 (ThS velocity), F-26 (Intelligibility/Coherence conflict), F-34 (TC80 seizure), F-38 (undefined archetypes), F-32 (Coup counter).*
