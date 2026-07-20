# Resolution Diagnostic — Threadwork

**Date:** 2026-05-28
**Skill:** valoria-resolution-diagnostic (Stage 1)
**Scope:** threadwork per skill INITIAL HYPOTHESES — covers `designs/threadwork/threadwork_v30.md`, `params/threadwork.md`, `designs/personal/knots_v30.md`, `canon/01_foundations_amendment_self_rendering.md`, `canon/02_foundations_amendment_leap_mechanism.md`. Cross-references: derived_stats §4.1 (wound penalty + Pool Floor 5), faction_layer (RS world track interaction), threadcut beings (Part Six).
**Status:** Audit output. Commits blocked (B6) — staged inline.

## §0 Pre-flight & citations

**Files consulted this session:**

- `designs/threadwork/threadwork_v30.md` — full + sections §2.3 Leap Roll, §2.6 Opposing Operations, §3.1–3.6 Coherence (definition/reduction/thresholds/residue/recovery/fallout), §3.7 Rendering Crisis [PROVISIONAL], §4.1 Co-Movement Core, §4.3 Auto-Effect Tables head, §5.3 RS Thresholds head
- `params/threadwork.md` — full (Thread Pool formula, three-axis Ob, TN modifiers, Gap Self-Closure, RS Track, Dissonance, Substrate Saturation, WR/WC, Knots PP-632)
- `canon/02_foundations_amendment_leap_mechanism.md` — full (Leap suspension, knot formation, operation-type taxonomy)
- `canon/01_foundations_amendment_self_rendering.md` — full (three-layer being-persistence, Coherence definition, Coherence 0 outcomes TS-gated)
- `designs/personal/knots_v30.md` — full (Pass 2g synthesis; surfaces 3 contradictions TIER-DRIFT-001, COMPOSURE-DRIFT-001, TRUNC-DRIFT-001)
- `canon/02_canon_constraints.md` — full (P-01–P-15 incl. P-01 Inseparability, P-10 Coherence, P-12 propagation, P-15 three-layer)
- `references/canonical_sources.yaml`, `skills/valoria-mechanic-audit/SKILL.md` — full

**NERS source:** PI `<definitions>` block per Turn B.

**Prior-art relationship:** No threadwork-specific prior NERS audit located in tree (tree match for 'ners' did not include threadwork audits). Foundations amendments (canon/01, canon/02) ARE the prior structural reasoning. This diagnostic builds on the Foundations-grounded intent rather than displacing it.

## §1 Phase 0 — Resolution component decomposition

| Component | Mechanism | Quantity category |
|---|---|---|
| **A · Thread Pool** | `(Spirit×2) + History (cap 3D) + TPS (=TS÷10), min 5 floor (cross-system)` per params §Thread Pool | Dice (aggregated, floored) |
| **B · Three-axis Ob** | Depth (Fibonacci 1/2/3/5/8/13) + Breadth (0–4) + Distance (0–3) | Deterministic gate |
| **C · TN by op type** | Standard 7 / Binding (Lock/Diss) 8 / POP 8 / POP-Binding 9 | Discrete TN tier |
| **D · Leap roll** | Eligibility gates (Approach Training tag, TS ≥ 30, Focus capacity); roll w/ retention at end | Dice + retention check |
| **E · Operation types** | Restorative (Mending) / Manipulative (Weave/Lock/Pull non-restorative) / Destructive (Dissolution, de-actualisation) per canon/02 Amendment 3 | Discrete taxonomy |
| **F · Coherence** | 10→0 scale; reduces by operation per §3.2; thresholds at 8/5/3/2/1/0 per §3.3 | **Continuous resource** (per skill three-category table) |
| **G · Co-Movement** | P-01 mandatory tri-dimensional auto-effects (temporal CD + epistemic + actual d6 + Co-Movement Card draw) per §4.1 | Deterministic + random discrete (cards) |
| **H · Mending Stability (RS)** | World-scale 100→0; Rupture (shared loss) at 0 per §5 | **Discrete accumulator** (clock; multi-threshold) |
| **I · Knot mechanics** | (Bonds×2)+3 formation pool; max floor(Bonds/2)+1; permanent once formed; strain capacity per tier (contested — T6); rupture cascade | Dice + discrete state |
| **J · Substrate Saturation Counter** | ≥3 ops/battle turn → +1 Ob/Coherence cost (cap +2); cumulative ≥3 → +2 Ob remainder + RS −1 next Accounting (cap −1/battle) | Discrete accumulator + cap |
| **K · Rendering Crisis arc** | Coherence 0 = campaign event with arc resolution; Pool = highest Close Knot's Bonds + Anchoring Scenes successful, TN 7 Ob 3; Success → Coherence 3 (Fragmented); failure → NPC | Arc-clock + dice |
| **L · Substrate-aligned operation cost (Foundations Amendment 3)** | Restorative (Mending): ZERO Coherence; Manipulative: proportional to deviation × duration; Destructive: catastrophic | Deterministic, operation-type-keyed |
| **M · Coherence 0 TS-gated outcomes** | TS 30–49 (Stirring) → Ontological Freefall; TS 50–69 (Attuned) → Relational Persistence; TS 70+ → Deeper outcomes | Discrete branching |

**Three-category classification:**
- **Continuous resources:** Coherence (10→0), Composure (×3 per derived_stats §3 Multiplier Tiers), Thread Fatigue (×5)
- **Base parameters:** Spirit, History, TS (0–100 — quasi-continuous but used as scalar), Focus, Bonds
- **Discrete accumulators:** Mending Stability (clock 100→0 multi-threshold), Substrate Saturation Counter, Knot strain counter (per tier — contested)

## §2 Phase 1 — Stress points

### 1a · Smallest pool by design / after degradation

**By design** — Thread Pool floor = 5 (cross-system min, same as Combat Pool). At Spirit 1 + History 0 + TPS 3 (TS 30, minimum to Leap): 2 + 0 + 3 = 5 (floor active).

| Build | Spirit | Hist | TPS | Pool |
|---|---|---|---|---|
| Minimum eligible practitioner (TS 30) | 1 | 0 | 3 | 5 (floor) |
| Capable | 3 | 2 | 5 (TS 50) | 13 |
| Expert | 5 | 3 | 7 (TS 70) | 20 |
| Master | 7 | 3 | 10 (TS 100) | 27 |

**Pool floor 5 IS the Lesson 3 safeguard** — same architectural pattern as combat. Wound penalty (PP-716 universal −1D) capped by floor (derived_stats §4.1).

**After degradation:**
- Wounds: −1D universal, capped by floor 5
- Coherence Fragmented (4–3): +1 Ob all Thread ops including Leap (rendering reasserts harder)
- Coherence Severed (1): +2 Ob all Thread ops
- Substrate Saturation: +1 Ob (cap +2 per battle); +2 Ob if counter ≥3 cumulative
- Sustained Opposition: +1 Ob sequential per round
- Dissonance failure: Spirit −1D for scene/season

Multiple +Ob stacks compound. A wounded practitioner at Coherence 3 in saturated substrate facing sustained opposition could face Ob +1 (Coherence) +2 (Saturation) +1 (Sustained) = +4 Ob on the base Ob of the operation (which at Relational scale is 3 + Breadth + Distance). Pool reduction (wounds) compounded by Ob inflation. **High-stress compound case is plausible.**

### 1b · Exposure frequency

| Stress case | Path | Likelihood |
|---|---|---|
| Floor-pool practitioner (TS 30 minimum-eligible) Leaping at Foundational scale | Build-extreme; nobody actually does this | L |
| Practitioner at Coherence 3–4 Leaping (Fragmented penalties stack) | After accumulated Structural/FR work | M |
| Saturated substrate (≥3 ops in battle turn) | Mass battle with multiple practitioners | M (campaign-event-dependent) |
| Compound: wounded + Coherence-low + saturated + sustained opposition | Late-arc mass battle climax | L (but high-magnitude when it fires) |
| Cumulative Coherence reduction from sustained Structural-scale practice | Long-campaign master practitioner doing extensive manipulative ops | M (long-term build path) |

`[FREQUENCY SIGNAL: PP-194 Rendering Crisis is explicitly a "campaign event," not a routine resolution. Most threadwork takes place at Object/Personal scale (Coherence cost 0) by design — the cost ladder targets the rare deeper operations. Per Amendment 3: restorative ops are zero-cost; manipulative ops bear the deviation cost. Most practitioners doing Mending across lifetimes (Edeyja) bear zero Coherence cost. Stress paths are intended-rare.]`

## §3 Phase 2 — What the stress point decides

### 2a · Outcome type

| Action | Outcome type | Depth |
|---|---|---|
| Standard Thread op (Weave/Pull/Mend at Object/Personal) | Continuous magnitude (degree → effect scale) | shallow per op; deep across many ops |
| Structural/Foundational op | Discrete cliff (Coherence −2; FR adds −1 surcharge) | discrete-event |
| Leap retention roll | Binary | shallow per Leap; clock-deep across Leaps |
| Co-Movement (every op) | Multi-dimensional discrete (temporal CD + epistemic mod + actual d6 + card draw) | shallow per op, accumulating |
| Knot rupture | Discrete event with cascade (Composure damage, Coherence −1, Disposition →−4) | binary |
| Coherence threshold crossing | Discrete state transition (Stable → Dissonant → Fragmented → Fractured → Severed → Crisis) | clock-deep (6 thresholds) |
| Rendering Crisis arc resolution | Clock-deep (4 designed beats per ED-681) → dice resolution roll at Beat 4 | deep clock + dice |

### 2b · Stakes & reversibility

| Outcome | Reversibility |
|---|---|
| Coherence loss from individual op | Recoverable +1/season non-practice OR Knot Anchoring OR Einhir technique |
| Coherence floor 0 | **Recoverable via Rendering Crisis arc** (Pool roll; Success → Coherence 3; Failure → NPC) — bounded by design, distinct from faction Stab=0 termination |
| Knot rupture | Knot points return; Composure damage caps per PP-633; Coherence −1; permanent removal of that specific Knot |
| Rendering Crisis Failure | Practitioner becomes NPC at season end (terminal for player agency, but doesn't end the world) |
| MS Rupture at 0 | **Shared loss** — campaign-ending world event |

### 2c · Risk profile

| Scenario | Impact | Exposure | Irreversibility |
|---|---|---|---|
| Master practitioner reaching Coherence 0 → Crisis | H | M (long-arc path) | M (recoverable via arc, but with TS −1 cost) |
| MS reaches 0 → world Rupture | H | L (designed climax event) | **H (shared loss)** |
| Knot rupture cascade (multiple Knots fire same scene) | M | L (rare composition) | L (per-Knot; PP-633 caps Composure damage) |
| TS 30–31 practitioner triggers Crisis with Success → TS 29 (below Leap minimum) | M | L | H (loses Thread access permanently) |

**The highest-impact outcome is MS Rupture (shared loss).** This is bounded by the entire ecosystem of safeguards: Substrate Saturation Counter, Coherence cost on operations, Gap self-closure rates by scale, WR/WC gates on Edeyja Mending. The system is designed to **make Rupture difficult to reach by accident**, easy to reach by sustained over-use.

## §4 Phase 3 — Effect-curve checks

### 3a · Impact uniformity

**Coherence reduction by scale (§3.2):**

| Operation | Object/Personal | Relational | Territorial | Structural |
|---|---|---|---|---|
| Standard (Weave/Pull) | 0 | −1 | −1 | −2 |
| FR (Lock/Diss) surcharge | +1 (PROVISIONAL PP-196) or min total −2 (base) — contested, T2 | additional −1 | additional −1 | additional −1 |
| POP surcharge | additional −1 | additional −1 | additional −1 | additional −1 |
| **Mending** | **0 per Foundations Amendment 3** — but §3.2 lists −1 (T1 contradiction) | same contradiction | same | same |

**Cliffs by intent.** The 0 → −1 jump at Object/Personal → Relational is intentional (canon/02 Amendment 3: greater ontological depth = greater cost). The −1 → −2 jump at Relational → Structural is intentional (same principle). Phase 3b classifies these as intended-by-design cliffs (see below).

**Thread Pool scaling per Spirit:**

Pool formula `(Spirit × 2) + Hist + TPS`. Linear in Spirit. Per Spirit point above floor: +2D. Same √N non-uniform-impact pattern as combat pool (combat C1 trade-off). **Pool floor 5 is the Lesson 3 safeguard; non-uniform impact at floor is the Lesson 2 trade-off** — identical to combat C1. **T9: same finding, same resolution (trade-off, not violation).**

### 3b · Threshold cliffs

| Cliff | Location | Status |
|---|---|---|
| Coherence thresholds at 8 / 5 / 3 / 2 / 1 / 0 (6 thresholds on 10→0 scale) | threadwork §3.3 | **PASS** — intended multi-step per canon/01 Amendment 3 (observable degradation: Stable / Dissonant / Fragmented / Fractured / Severed / Crisis). Per Lesson 6 second clause: "intended, spaced thresholds — especially clock thresholds — are exempt and may be multiple." Six thresholds is at the upper end of "multiple," but each corresponds to a distinct phenomenological state explicitly justified in Foundations canon. **PASS.** |
| Coherence reduction cliffs by scale (0 / −1 / −1 / −2) | §3.2 | **PASS by intent** — Foundations Amendment 3 justifies the scale-keyed cost as substrate-tendency alignment. |
| Substrate Saturation Counter triggers at ≥3 ops | params §Substrate Saturation | **PASS** — explicit cap mechanic with hard limit (+2 max per battle, −1 RS max per battle). |
| Coherence 0 = Rendering Crisis arc | §3.7 PROVISIONAL | **PASS-with-flag** — bounded loop, but arc spec is PROVISIONAL (T3). |
| MS thresholds (100/.../0) | §5.3 | **PASS** — world-scale clock, intended thresholds. |
| TS 30/50/70/90 Leap-eligibility/scale gates | §2.3 + params §Practitioner Stats | **PASS** — discrete capability gates, intentional. |
| Knot tier strain capacity (1/2/5 OR 4/7 OR 1/2/4/7) | knots_v30 §2 (T6 TIER-DRIFT-001) | **DEFECT** — tier system contested; impact on rupture cliffs varies by which tier system is canon. Until resolved, the cliffs are undefined. |

**No accidental cliff stacking.** All cliffs identified are either (a) intended/foundational, or (b) PASS in design-intent but defective at canon level (T1, T2, T6). Cleanup is canon-coherence work, not mechanical-redesign.

### 3c · Role conflation

**Spirit carries:** Thread Pool (statistical) + Dissonance check (TN 7 vs Dissonance Factor) + Knot formation pool component. Three uses of Spirit, but all are "ontological-rendering-stability" expressions. Single coherent narrative (Spirit = depth of contact with substrate as both practitioner and as configured-being). **PASS** — not Lesson 1 conflation.

**Endurance / wounds / Coherence:** Health drains from combat damage; Coherence drains from substrate engagement. Two different resources tracking two different forms of degradation. Wound penalty applies cross-system (−1D all Pools per PP-716). **PASS** — clear conceptual separation.

**Bonds carries:** Knot Pool (formation roll) + Max Knot count + Disposition ceiling + Rendering Crisis Pool (Beat 4 resolution). Multi-use but coherent narrative ("relational depth"). PASS.

**TS:** Perceptual depth gate (scale access) + TPS contribution to Thread Pool + Coherence 0 outcome branching + Leap eligibility. Multi-use but coherent ("substrate-perception capacity"). PASS.

**No true role conflation.** Phase 3c clean.

## §5 Phase 4 — Loops

### 4a · Loop catalog

| ID | Loop | Damper | Cap |
|---|---|---|---|
| **TL1 (Coherence degradation)** | Thread op → Coherence loss → +Ob (at 4–3 / 1) → harder ops → more retention failures → more Coherence loss | §3.5 Recovery (+1/season non-practice OR Knot Anchoring OR Einhir technique) | **Coherence 0 = Rendering Crisis arc → recoverable to Coherence 3** (Success) — bounded by design |
| **TL2 (P-01 tri-dimensional co-movement)** | Every Thread op → mandatory temporal/epistemic/actual auto-effects → CD accumulation + RS drain → world Rupture | Substrate Saturation Counter caps in-battle compounding; CD/History Resonance has per-op cost not unbounded amplification | **MS 0 = shared-loss Rupture (world bound)** |
| **TL3 (P-12 knot-mediated propagation)** | Drifting practitioner → tri-dimensional propagation through Knot → connected entity altered (actuality, intelligibility, temporality) → cumulative exposure can initiate drift in connected entity → propagates further | Knot strain caps per tier (CONTESTED — T6); PP-633 simultaneous-rupture Composure cap | Max Knots = floor(Bonds/2)+1 limits propagation surface; rupture removes knots | 
| **TL4 (Substrate Saturation in battle)** | ≥3 ops/battle turn → +1 Ob/Coherence cost cap +2; cumulative ≥3 → +2 Ob remainder + RS −1 next Accounting | Explicit hard cap on Ob/Coherence accrual (+2 max); RS drain capped at −1/battle | Battle-end reset |
| **TL5 (Substrate-saturation × Coherence)** | Saturated battle → more Ob → more failures → more residue use (which has its own Coherence cost) → harder ops → ... | Same as TL4 + Coherence recovery dampers | Same |
| **TL6 (Opposing N-Way)** | 3+ practitioners with opposing intentionalities → lattice collapse → Gap formed → MS −(2×N) | **Lattice collapse IS the cap** — automatic; all operations fail | Bounded per-engagement |
| **TL7 (Engine "intent_of_game" positive feedback loop, threadwork instance)** | Player decisions about Thread ops → substrate consequences (co-movement, RS, Coherence) → world-state changes → narrative material → player decisions | Coherence + RS + Gap self-closure as multi-axis damper | Multi-axis caps (Coherence arc, RS Rupture, Gap closure) |

### 4b · Damper + Cap analysis

**TL1 (Coherence degradation):** damper exists but is **rate-asymmetric** (recovery +1/season vs degradation up to −2/op + surcharges). T4: similar shape to faction F5 asymmetry. **Key difference:** the floor (Coherence 0) is **arc-recoverable, not terminal**. Per skill Lesson 5 ("No loop both undamped and unbounded"): damped (weakly) + bounded (arc not terminal). **PASS-with-flag** — asymmetry is intentional per Amendment 3 (operation-type taxonomy); arc is the designed safeguard.

**TL2 (P-01 co-movement):** Mandatory tri-dimensional auto-effects are the **engine that drives the intent_of_game positive feedback loop**. Per skill: "Lesson 5 is doubly critical — `intent_of_game` is itself a positive feedback loop." Damper: Substrate Saturation Counter (+caps); CD accumulation is per-op not amplifying; RS drain per-op not amplifying. Cap: MS 0 = shared-loss Rupture. **PASS** — explicit dampers + system-bound cap.

**TL3 (P-12 knot-mediated propagation):** Per canon/02_canon_constraints.md P-12: tridimensional propagation explicit. Damper: Knot strain caps (per tier, contested per T6) + PP-633 simultaneous-rupture Composure cap. Cap: Max Knots = floor(Bonds/2)+1. **BUT: the "cumulative exposure can initiate drift" formula on connected NPCs is not in my read this session.** `[GAP T11: cumulative-exposure-drift mechanic — knots_v30 mentions "relational contagion (P-12) for practitioners" but the exact mechanical formula for inbound drift on connected NPCs is not located in this session's reads. Damper-quantification verification pending.]` **PASS-with-gap.**

**TL4–TL5 (Substrate Saturation):** Explicit hard cap. **PASS.**

**TL6 (Opposing N-Way):** Lattice-collapse-as-cap is elegant. **PASS.**

**TL7 (intent_of_game engine loop):** This IS the project's central design intent ("positive feedback loop between player decisions and mechanics/system/designs"). Threadwork carries the metaphysical weight (P-01 Inseparability). Multi-axis cap (Coherence arc + RS Rupture + Gap closure + Substrate Saturation). **PASS by intent**, with the deepest possible safeguard stack.

**No undamped+unbounded loops in threadwork.** Phase 4 PASS-with-T11-gap.

## §6 Phase 5 — Intent gate

| Finding | Intent evidence | Safeguard | Adequate? | Result |
|---|---|---|---|---|
| T1 (Mending cost contradiction) | Foundations Amendment 3 explicit ("Mending's Coherence cost is zero"); also explicit §31 reference | Foundations supersedes design doc per project hierarchy | n/a (canon defect) | **defect — needs propagation to §3.2** |
| T6 (Knot TIER-DRIFT) | Pre-flagged in knots_v30 §2 as PROVISIONAL; Jordan resolution required | None — open editorial | n/a | **defect** |
| T2 (FR surcharge contradiction) | PP-196 PROVISIONAL in same section as base table | None — both in canon | n/a | **defect** |
| T7 (COMPOSURE-DRIFT) | Pre-flagged in knots_v30; canon citation error | None | n/a | **defect** |
| T11 (cumulative-exposure-drift unread) | P-12 canon constraint explicit; mechanical formula location unverified this session | n/a (partial read) | n/a | **gap (partial read)** |
| T3 (Rendering Crisis PROVISIONAL) | §3.7 marked [PROVISIONAL] in canon | Arc structure designed (4 beats) but spec unfinalized | partial | **design-in-flight** |
| T4 (asymmetric recovery) | Amendment 3 explicit: cost is structural consequence of operation-type alignment; restorative is zero by design | Recovery dampers + arc cap | YES | **PASS** |
| T5 (P-01 co-movement) | canon/02_canon_constraints.md P-01; canon/00 §1.1; canon/01 Amendment 2 — explicit | Substrate Saturation Counter + system caps + MS bound | YES | **PASS (doubly critical loop, doubly safeguarded)** |
| T8 / T9 (Pool floors) | Architectural floors (Combat Pool min 5, Thread Pool floor 5) | The floors ARE the safeguard | YES | **PASS (trade-off)** |
| T10 (Substrate Saturation) | params §Substrate Saturation Counter explicit | Hard caps + battle-end reset | YES | **PASS** |
| T12 (Co-Movement Cards) | §4.3 explicit; ED-577 canonical card list | Discrete trigger; bounded variance | YES | **PASS** |
| T_thresh (Coherence thresholds) | canon/01 Amendment 3 explicit observable-degradation states | Foundations-grounded; phenomenologically justified | YES | **PASS** |
| T2.6 / N-Way (lattice collapse) | §2.6 explicit | Automatic cap | YES | **PASS** |

## §7 Phase 6 — Triage

| # | Finding | Component | Impact | Exposure | Irreversibility | Phase | Severity |
|---|---|---|---|---|---|---|---|
| T1 | Mending Coherence cost — Foundations 0 vs §3.2 −1 | F · Coherence + L · op-type | H | H | M | 0 | **P1 (canon)** |
| T6 | Knot TIER-DRIFT-001 (3 conflicting sources) | I · Knots | H | H | M | 0 | **P1 (canon)** |
| T2 | FR surcharge contradiction (base −2 vs PP-196 −1) | F · Coherence | M | M | M | 0 | **P2 (canon)** |
| T7 | COMPOSURE-DRIFT-001 | I · Knots | M | M | M | 0 | **P2 (canon)** |
| T11 | Cumulative-exposure-drift formula not in this-session reads | TL3 | M | M | M | meta | **P2 (gap)** |
| T3 | Rendering Crisis PROVISIONAL | K · arc | L | L | L | meta | **P3** |
| All PASS items below: T4/T5/T8/T9/T10/T12/T_thresh/T2.6 | | | | | | | — |

## §8 Stage 2 — Lesson mapping

| # | Finding | Lesson(s) | Remediation direction |
|---|---|---|---|
| T1 | Mending Coherence contradiction | (canon defect) | **Editorial ledger candidate:** ED-NEW threadwork §3.2 row "Mending −1" superseded by canon/02 Amendment 3 ("Mending Coherence cost is zero"). Update §3.2 to row "Mending | 0" + cite Amendment 3. The downstream effect: Edeyja's lifetime Mending without cumulative Coherence cost (canon explicit) becomes mechanically realizable. |
| T6 | Knot TIER-DRIFT-001 | (canon defect) | **Editorial ledger candidate:** ED-NEW knot tier system ratification. Per knots_v30 §2: three options — A (ED-773 supersedes PP-632, Distant/Close 4/7), B (PP-632 stands, Loose/Med/Close 1/2/5), C (4-tier hybrid). Jordan-decision. Knots_v30 §2 recommends Option A as most likely intended. |
| T2 | FR surcharge contradiction | (canon defect) | **Editorial ledger candidate:** ED-NEW FR Coherence surcharge ratification. PP-196 PROVISIONAL revises base table; either ratify PP-196 and update base table, or strike PP-196. Both currently in canon. |
| T7 | COMPOSURE-DRIFT-001 | (canon defect) | **Editorial ledger candidate (pre-flagged):** correct articulation §2.4 citation from "5 per ED-773" to "4 per ED-773." |
| T11 | Cumulative-exposure-drift formula unread | (gap) | **Action:** read knots_v30 §7+ or threadwork_v30 §3 deeper to locate the formula; alternatively, fetch threadwork_v30 sections covering cross-Knot drift propagation mechanics. Verify the L4 (TL3) loop has explicit mechanical damper-quantification. |
| T3 | Rendering Crisis PROVISIONAL | (design-in-flight) | **Note:** finalize PP-194 spec. The current 4-beat structure (ED-681) is designed but the resolution mechanic carries [PROVISIONAL] markers. Stabilization pending. |
| T4 | Recovery asymmetry | (PASS-with-flag) | **No remediation.** Asymmetry is intentional per Amendment 3 operation-type alignment philosophy. Document as deliberate where not already explicit. |
| T9 | Thread Pool floor trade-off | (trade-off, same as combat C1) | **No remediation.** Floor IS the L3 safeguard; L2 non-uniformity at floor is the trade-off price. Identical reasoning to combat C1. |
| Other PASS items | — | — | No remediation required. |

## §9 Status

Stage 1 complete. Findings carried to Stage 3 verdict in `ners_verdict_threadwork.md`.

**Confidence:**
- `[CONFIDENCE: high]` — T1 (direct text comparison Foundations vs design doc), T5/T8–T10/T12/T_thresh (audit-validated against canon + Foundations)
- `[CONFIDENCE: medium]` — T4 (rate analysis dependent on op frequency assumptions), T6/T7 (pre-flagged contradictions; my role is surfacing not resolving)
- `[CONFIDENCE: medium]` — T11 (gap — could be mechanical surface I didn't reach in 80k of available threadwork canon)

**Files NOT deep-read this pass:**
- `designs/threadwork/threadwork_v30.md` Parts Six (Threadcut Beings) and Seven (Cross-Mode) — read at index-grain only
- `designs/threadwork/thread_horizontal_integration_spec.md` — not read this turn; would affect TL3 cumulative-exposure-drift mechanic
- `designs/world/solmund_*` — provisional ontological canon; not in resolution scope

**Departures from skill INITIAL HYPOTHESES:**
- Skill: "Threadwork — likely compliant for operations; Coherence is a depleting resource (continuous, variable-cost) — validate that its depletion and threshold effects satisfy Lessons 2 and 6."
- **Validated as compliant** on operations + thresholds (T_thresh PASS Lesson 6 second clause; T4 PASS-with-flag on Lesson 5; T9 PASS Lesson 3 with L2 trade-off).
- **Skill did not predict** the Foundations-vs-design-doc contradiction (T1), which is the most consequential finding of this turn.
- **Skill did not predict** the depth of pre-flagged contradictions (T6/T7) in the Knot subsystem — but these were already flagged in knots_v30 Pass 2g as Pending-Jordan-resolution; my role is cross-system impact assessment, not original surfacing.
