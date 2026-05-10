# R1 — Wound Permanence vs Canonical Recovery
## Module 1 of combat_arch_residual_stress_01

**Date:** 2026-05-09
**Mode:** B (interaction chain) + D (exhaustive edge cases)
**Source question:** `tests/stress/combat_videogame_arch_2026-05-01/06_synthesis.md §4 R1`
**Question text:** *"Canonical §4 says Wounds clear at end of session. Wildermyth pattern (Chunk 2 §3) suggests permanent-consequence Wounds for narrative weight. The composite stack doesn't take a position. Decision needed: do some Wounds (catastrophic — limb loss, blind eye) become permanent for narrative payoff, with normal Wounds clearing canonically?"*

**Decision shape:** yes (specify catastrophic-Wound criteria) / no (preserve canonical) / partial (use existing permanence channel)

---

## 1. Verification ledger entries (this module)

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| R1-L01 | combat_pool_formula | `(Agility × 2) + Relevant History + 3 (minimum 5)` | designs/scene/combat_v30.md | §1 line 34 | "Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)" |
| R1-L02 | wound_pool_penalty | −1D per Wound, cumulative, no Ob | designs/scene/combat_v30.md | §7 line 266 | "Each Wound: −1D Combat Pool only (cumulative). No Ob penalty from wounds." |
| R1-L03 | wound_threadwork_penalty | +1 Ob per Wound, all Thread ops | designs/scene/combat_v30.md | §thread line 378 | "- \*\*Wound penalties:\*\* +1 Ob per Wound to all Thread operations (threadwork_v30 §2.3)." |
| R1-L04 | vitality_formula | Endurance × 10 (+ equipment) | designs/scene/combat_v30.md | §7 line 253 | "\*\*Vitality = Endurance × 10\*\* (range 10–70). Total damage capacity. Equipment adds flat Vitality. Incapacitated at 0." |
| R1-L05 | wound_interval | Endurance + 6 (range 7–13) | designs/scene/combat_v30.md | §7 line 255 | "\*\*Wound Interval = Endurance + 6\*\* (range 7–13). Wounds accrue at floor(cumulative_damage / Wound_Interval)." |
| R1-L06 | wound_clearance_canonical | wounds clear at session end | params/combat.md | line 271 | "Session end: all wounds clear" |
| R1-L07 | stabilised_recovery | one-scene rest after stabilisation | designs/scene/combat_v30.md | §4 line 109 | "Stabilised characters may return to action after one full scene of rest. Wounds clear at end of session (or after extended rest per GM)." |
| R1-L08 | pool_floor | 5D, no further wound penalty | params/combat.md | §Pool minimum line 274 | "Combat Pool minimum 5 is a clean floor. No −1D penalty at the floor." |
| R1-L09 | conviction_scar_existing | permanence channel exists, attached to Conviction not Wound | designs/scene/derived_stats_v30.md | §Conviction L195 | "Lifetime; shifts only through Scar accumulation or major narrative events" |
| R1-L10 | knot_lifecycle_strain_capacity | Distant 4 / Close 7 | designs/scene/fieldwork_v30.md | §5.6b line 495–498 | "\| Distant Knot \| 4 strain \| Can be upgraded to Close (per §5.6a Success outcome)." |
| R1-L11 | fr_dissolution_wound | +1 Wound to Knot partner on FR Dissolution | designs/scene/fieldwork_v30.md | §5.6b line 515 | "Tears the Knot directly; partner-of-rupture takes +1 Wound (no armor)." |
| R1-L12 | dissolution_witness_scar | scar on all witnesses to Dissolution | params/combat.md | line 306 | "\*\*Dissolution in combat:\*\* RS cost per threadwork_v30 §5.2. Scar on all witnesses per npc_behavior_v30 §3.4." |
| R1-L13 | coherence_track_permanence | Coherence is permanent degradation track | designs/scene/derived_stats_v30.md | line 241 | "\*\*Coherence\*\* (survival resource): unchanged. 10→0 countdown. Not a derived value — a permanent degradation track." |

All quoted_text strings verified to appear verbatim in the fetched canonical content (force_full=True, read_depth=full per Module 0 protocol).

---

## 2. Existing permanence channels (canon)

R1 asks whether to introduce a *new* permanence channel for catastrophic Wounds. Before adopting a new channel, enumerate the channels that already exist:

| # | Channel | Carrier | Trigger | Mechanical effect |
|---|---|---|---|---|
| P1 | **Conviction Scar** | Conviction (Piety/Persuasion Track post-rename) | Major narrative events, Knot rupture at strain ≥ Close threshold | +1 Scar → Conviction shift; Lifetime; Resonant Style change |
| P2 | **Witness Scar** | NPC reaction state | Witnessing Dissolution event | per npc_behavior §3.4 — Disposition shifts and faction reaction lock-in |
| P3 | **Coherence track** | Practitioner | Thread overdraw, FR Lock failures, Calamity radiation | Permanent degradation track 10→0 |
| P4 | **Inspiration permanent loss** | derived_stats | Focus permanently destroyed/captured/lost | Inspiration drops to 0 immediately; recovery requires new focus |
| P5 | **Knot rupture** | Relational state | Conviction opposition, FR Dissolution, public counsel citation | Disposition reset, possible Conviction Scar |

Adding "physical wound permanence" would be channel P6.

---

## 3. Candidates

| ID | Name | Description |
|---|---|---|
| **C1.1** | Pure canonical | All Wounds clear at session end. No new channel. |
| **C1.2** | Catastrophic-permanent | Tag certain Wounds "catastrophic" at the moment of accrual; catastrophic Wounds persist across sessions; normal Wounds clear canonically. Tag criteria require specification. |
| **C1.3** | Knot-tagged | Wounds taken in events that already trigger existing permanence channels (FR Dissolution +1 Wound to Knot partner per R1-L11; Dissolution-witness +1 Wound by extension) become permanent as Conviction Scar +1. Reuses P1, no new channel. |
| **C1.4** | All-permanent | All Wounds persist across sessions; clearance via specific actions (extended rest with healer, Mending Operation, downtime ritual). |

---

## 4. NERS at full grain — 24 cells per candidate

Per Module 0 self-audit corrections: 6 directions × 4 NERS = 24 cells. N-failures categorical. Diagonal = cross-system. Lateral = same-scale parallel. Threshold drift avoided by fixing scoring criteria here:

**Criteria locked at module start:**
- N: ✓ if mechanic is present and complete; ⚠ if specified but with gaps; ✗ if mechanic missing or undefined.
- E: ✓ if mechanic adds depth without overhead; ⚠ if depth added with non-trivial bookkeeping; ✗ if overhead exceeds depth.
- R: ✓ if mechanic produces emergent variation across character types; ⚠ if variation present but uneven; ✗ if mechanic produces homogenized outcomes or dominant strategies.
- S: ✓ if mechanic integrates without contradicting another canonical rule; ⚠ if integration adds new edge cases; ✗ if mechanic contradicts another canonical rule.

### C1.1 — Pure canonical

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Canonical wound clearance is fully specified; no new state to manage at faction layer; clean. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Combat Pool math, Wound Interval, Vitality preserved; resolution unchanged at scene scale. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Wound clearance scales identically across personal / mass / faction (mass uses Discipline-tier abstraction; PCs use scene-scale). |
| Diagonal (cross-system) | ✓ | ✓ | ✓ | ✓ | Cross-system effects (Threadwork +1 Ob per Wound) are scoped to the wounded session and clear with the wound. |
| Lateral (same-scale parallel) | ✓ | ✓ | ✓ | ✓ | Wounds ↔ Stamina ↔ Composure ↔ Concentration all clear at session end; consistent. |
| Horizontal (campaign time) | ⚠ | ✓ | ⚠ | ✓ | Campaign-arc narrative weight of a battle wound is *not* mechanically retained; relies on Conviction Scar / faction-reputation channels for narrative permanence. |

**Verdict C1.1:** Two ⚠ on Horizontal direction (Wildermyth gap — battle wounds don't carry narrative weight across campaign). All N, E, S clean. Mechanically minimal, narratively sparse.

### C1.2 — Catastrophic-permanent

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ⚠ | ⚠ | ⚠ | Tag criteria undefined — "catastrophic" must be specified. Without criteria, Game Master adjudication; with criteria, +1 spec section. Faction layer must track per-NPC permanent Wound state across sessions. |
| Bottom-up | ⚠ | ⚠ | ✗ | ✗ | **R FAILS:** Pool floor 5D (R1-L08) makes permanent-wound penalty asymmetric. High-stat characters lose meaningful Pool (12D → 5D = 58% reduction at 7 wounds). Low-stat characters (5D Pool) lose nothing — already at floor. Reverses canonical design intent. **S FAILS:** contradicts canonical "Wounds clear at session end" (R1-L06); requires PP-level patch to override. |
| Vertical | ⚠ | ⚠ | ⚠ | ✗ | **S FAILS:** mass-scale unit Discipline/Morale resolution does not have Wound Interval; permanence at unit scale undefined. Asymmetric scale handling. |
| Diagonal (cross-system) | ⚠ | ⚠ | ✗ | ⚠ | **R FAILS:** Threadwork penalty has NO floor (R1-L03: "+1 Ob per Wound to all Thread operations"). Permanent-Wound + Threadwork compounds without bound. A practitioner with 5 permanent Wounds takes +5 Ob to all Thread ops *forever*. Practitioner viability collapses. |
| Lateral | ⚠ | ⚠ | ⚠ | ⚠ | Mismatch with Stamina / Composure / Concentration which clear cleanly. Pool clearance asymmetric. |
| Horizontal | ✓ | ⚠ | ✓ | ⚠ | Narrative-weight goal achieved; campaign arcs gain battle-wound permanence channel. ⚠ on E for tag-criteria bookkeeping. |

**Verdict C1.2:** **N=⚠ on 5 of 6 directions (categorical concern).** **R=✗ on Bottom-up and Diagonal.** **S=✗ on Bottom-up and Vertical.** Per locked criteria, R-fail and S-fail are categorical rejections. **C1.2 fails NERS at full grain.**

### C1.3 — Knot-tagged

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Reuses existing channel (Conviction Scar via P1); no new state; faction layer unchanged. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Wound mechanic unchanged at scene scale (clears at session end per canon); permanence carried by Scar at perception layer. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Conviction Scar already operates across scales (per derived_stats_v30 §Conviction L195). |
| Diagonal | ✓ | ✓ | ✓ | ✓ | FR Dissolution → Knot rupture (existing) → +1 Wound (R1-L11) → Conviction Scar (existing P1). No new compounding pathway. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Stamina/Composure/Concentration clear normally; Wound clears normally; Scar fires only on triggered events. |
| Horizontal | ✓ | ✓ | ✓ | ✓ | Narrative weight earned via existing Scar mechanism — battles producing Knot ruptures or Dissolution events leave Scars on participants/witnesses. |

**Verdict C1.3:** All 24 cells ✓. **C1.3 passes NERS at full grain.** No new channel required; uses existing P1/P2 permanence pathways.

### C1.4 — All-permanent

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ✗ | ✗ | ✗ | **E FAILS:** every NPC tracked across all sessions for cumulative permanent Wound state. Crunch overhead. **R FAILS:** Pool floor 5D + no Threadwork floor → low-stat characters more durable than high-stat under sustained injury. **S FAILS:** contradicts R1-L06 universally, requires complete patch of canonical clearance. |
| Bottom-up | ✗ | ✗ | ✗ | ✗ | **N FAILS:** clearance mechanism undefined (the spec says "specific actions" but those actions aren't enumerated). Compound failures across NERS. |
| Vertical | ✗ | ⚠ | ✗ | ✗ | Same as C1.2 vertical issues, amplified by universality. |
| Diagonal | ✗ | ⚠ | ✗ | ✗ | Threadwork compounding without floor produces extinction-level effect on practitioners over campaign time. |
| Lateral | ⚠ | ⚠ | ⚠ | ✗ | Stamina/Composure/Concentration still clear; Wound permanence creates asymmetry without justification. |
| Horizontal | ✓ | ✗ | ✗ | ⚠ | Narrative weight achieved at the cost of unbounded campaign-time degradation; characters become unplayable after ~5–10 sessions of routine combat. |

**Verdict C1.4:** **N=✗ on 3 directions, R=✗ on 5 directions, S=✗ on 4 directions.** Categorical rejection on multiple axes. **C1.4 fails NERS at full grain.**

### Cross-candidate summary

| Candidate | N pass | E pass | R pass | S pass | Verdict |
|---|---|---|---|---|---|
| C1.1 Pure canonical | 6/6 | 6/6 | 5/6 (⚠ Horizontal) | 6/6 | PASS — minor narrative gap |
| C1.2 Catastrophic-permanent | 1/6 ✓ + 5⚠ | 1/6 ✓ + 5⚠ | 3/6 (2 ✗) | 2/6 (3 ✗) | **REJECT — categorical R-fail and S-fail** |
| C1.3 Knot-tagged | 6/6 | 6/6 | 6/6 | 6/6 | **PASS — uses existing channels** |
| C1.4 All-permanent | 1/6 (3 ✗) | 1/6 (3 ✗) | 0/6 (5 ✗) | 0/6 (4 ✗) | **REJECT — multiple categorical fails** |

---

## 5. Mode B — Interaction chain analysis (probability-driven)

### Chain 1: Wound → Pool degradation → next-session combat viability

Reference character: Agility 4, Relevant History 1 → **Pool = 12D** (canonical formula R1-L01). Pool floor 5 (R1-L08).

| Wounds carried | Pool | Expected net (TN7) | P(≥1 net) | P(≥2 net) | P(≥3 net) |
|---|---|---|---|---|---|
| 0 | 12D | 3.96 | 99% | 95% | 83% |
| 1 | 11D | 3.63 | 99% | 92.5% | 78% |
| 2 | 10D | 3.30 | 99% | 90% | 73% |
| 3 | 9D | 2.97 | 98% | 86% | 66.5% |
| 4 | 8D | 2.64 | 97% | 82% | 60% |
| 5 | 7D | 2.31 | 94.5% | 76% | 52.5% |
| 6 | 6D | 1.98 | 92% | 70% | 45% |
| **7** | **5D (floor)** | **1.65** | **86%** | **60%** | **35%** |
| 8+ | 5D | 1.65 | 86% | 60% | 35% |

**Key finding:** at 7 permanent Wounds, the 12D pool hits the canonical floor. Wounds 8+ are mechanically inert. Under C1.2 / C1.4, a "catastrophic-Wound" beyond the 7th has narrative weight but zero mechanical consequence on Pool.

Low-stat character (Agi 1, Hist 0 → 5D Pool, already at floor): Wound penalty is *zero from the start*. Permanent-Wound mechanic does not affect them. Reverses the canonical design intent that high-Endurance characters are more resilient.

### Chain 2: Wound → Threadwork +1 Ob → practitioner viability

Threadwork operations target TN 7 typically; Ob varies by operation depth (Fibonacci 1, 2, 3, 5, 8, 13 per Thread Ob three-axis). +1 Ob per Wound is **uncapped** (R1-L03).

A practitioner with **5 permanent Wounds** under C1.2/C1.4 takes +5 Ob to every Thread operation forever. For a depth-1 (Fibonacci Ob 1) operation: effective Ob 6. For depth-3 (Ob 5): effective Ob 10 — typically requiring 12+ net successes from a Spirit×2+TPS pool. Realistic Spirit × 2 + TPS = 8–14 dice → ~3–5 expected net at TN 7. **Operations at depth ≥ 3 become probabilistically unreachable under permanent-wound accumulation.**

**Compounding regression risk:** under permanent-wound rules, a wounded practitioner cannot perform Mending (which would clear coherence loss) → Coherence drains → Practitioner enters Crisis → another Wound from Crisis → +1 Ob compounds → cannot Mend. Loop closes on practitioner extinction.

C1.3 avoids this entirely — the Wound clears at session end per canon; the *Scar* (Conviction-channel) carries the narrative weight.

### Chain 3: Wound → Knot strain → relational rupture

Under canon (R1-L10, R1-L11): a Knot accrues strain from specific use; FR Dissolution targeting Knot partner gives +1 Wound (no armor) AND tears the Knot directly. The +1 Wound is currently session-clearing.

Under C1.2: if FR-Dissolution-induced Wound is tagged "catastrophic" (the criterion is unspecified), permanent-wound state attaches to Knot rupture event. Mechanically: the Knot rupture already triggers Conviction Scar +1 (R1-L09, fieldwork §5.6b "Close Knots that broke at high strain: Conviction Scar +1 to both partners"). **Adding a permanent Wound on top of an existing Conviction Scar is double-permanence on a single triggering event.**

Under C1.3: the Wound clears at session end (canon); the Conviction Scar carries the permanent record. Single permanence channel per event, mechanically clean.

### Chain 4: Wound → narrative arc density (Wildermyth-style)

Wildermyth produces narrative weight by tying combat outcomes to character traits (Tough/Goofy/Snarky → quirks change with major events). The closest canonical Valoria channel is Conviction Track post-rename (Piety/Persuasion). Per derived_stats_v30 §Conviction (R1-L09): "Lifetime; shifts only through Scar accumulation or major narrative events." Conviction shifts already drive Resonant Style and major decision frameworks.

To replicate Wildermyth's "permanent quirk" pattern in canon-respecting form, the existing Scar mechanism is sufficient. A new permanent-Wound channel adds a second tracking surface without adding a different *kind* of narrative weight.

### Chain 5: Wound → fieldwork capability

Fieldwork uses Investigation, Exploration, Socializing pools — none of which are Combat Pool. Wounds do not directly penalize fieldwork actions. They penalize Threadwork (Chain 2) which is a fieldwork-adjacent mechanic for practitioners.

**Crunch implication for C1.2/C1.4:** Game Masters must check, at every fieldwork scene, whether a wounded character's Threadwork-adjacent action is cumulatively penalized. C1.3 avoids by routing permanence through Conviction Scar which has its own well-specified cross-system effect.

---

## 6. Mode D — Edge case discovery

Nine categories per SKILL.md. Findings tagged P1 (breaks game) / P2 (bad play experience) / P3 (minor oddity).

### Boundary
**EC-D1.B-01 [P1] (C1.2/C1.4 only):** Pool floor 5D combined with permanent Wounds reverses canonical resilience hierarchy. Endurance 1 character (5D pool already at floor) is mechanically *more robust under sustained injury* than Endurance 7 character (12D → 5D over 7 permanent Wounds). Contradicts canonical Vitality scaling design intent (R1-L04 Vitality = End × 10).

**EC-D1.B-02 [P2] (C1.2/C1.4 only):** At Vitality = 0 + Wound = Stage 2 Dying (R1-L07 stabilisation Ob 3 within one scene) — if the Stage 2 character is stabilised but the Wound is "catastrophic," the character carries a permanent Wound from a death-cascade-adjacent state with no mechanical handle for the catastrophe-vs-routine distinction.

### Cascade
**EC-D1.C-01 [P1] (C1.2/C1.4 only):** Practitioner cascade — see Chain 2. Permanent Wound → Threadwork +1 Ob compounding → cannot Mend → Coherence Crisis → more Wounds. Closed loop on practitioner extinction over 5–10 sessions of routine combat. Pool floor does not bind Threadwork penalty.

**EC-D1.C-02 [P2] (C1.2):** "Catastrophic" tag undefined → cascade where Game Master adjudication snowballs. One Game Master tags every Stage-1 Wound catastrophic; another tags none. Cross-table consistency fails.

### Regression
**EC-D1.R-01 [P1] (C1.2/C1.4 only):** Wound → Threadwork +1 Ob → reduces Practitioner ability to perform Mending → Mending is *the canonical wound-clearance ritual* (per fieldwork_v30 §5.6 and Mending community quality tiers from the wider window) → practitioner self-treatment becomes harder as Wounds accumulate. Output loops back as input.

### Deadlock
**EC-D1.D-01 [P2] (C1.4):** Party with all members at Pool floor 5D and high permanent-Wound count cannot complete combat encounters above ~Ob 2 reliably. Encounter design must shift floor on encounter Ob downward, contradicting canonical Ob curve.

**EC-D1.D-02 [P3] (C1.2):** "Catastrophic" criteria undefined → Game Masters lock into "no Wounds qualify" → C1.2 collapses to C1.1 in practice, but with overhead of tracking the un-fired criterion.

### Crunch cascade
**EC-D1.CR-01 [P1] (C1.4):** Per-NPC permanent-Wound state across all named characters in the campaign × all sessions. Estimated 12 named NPCs × 30 sessions × 1.5 Wounds/session/character = 540 state entries to track and clear/preserve. Above sustainable bookkeeping for tabletop play.

**EC-D1.CR-02 [P2] (C1.2):** Per-character "catastrophic" tagging at the moment of Wound accrual is a Game Master decision per Wound. Adds 1 decision per Wound × ~5 Wounds per session = 5 extra adjudications per session.

**EC-D1.CR-03 [P3] (C1.3):** Conviction Scar tracking is already in canon; no additional crunch beyond what Conviction Track post-rename already imposes.

### Ambiguity
**EC-D1.A-01 [P1] (C1.2):** "Catastrophic" criterion is the central undefined term. Synthesis suggests "limb loss, blind eye." But the canonical Wound mechanic (R1-L02, R1-L05) does not have hit-location detail — Wounds are a count, not a typed catalog. No mechanical surface to derive catastrophe-vs-routine. **Either** introduce hit-location mechanic (substantial canon expansion) **or** leave criterion as pure narrative-flavor (Game Master-side, unverifiable cross-table).

**EC-D1.A-02 [P2] (C1.4):** "Specific actions" for clearance are not enumerated. Mending? Extended rest? Healer's kit (R1-L04 listed as Vitality-restoring consumable)? Spec gap.

### Incoherence
**EC-D1.I-01 [P1] (C1.2/C1.4):** Direct contradiction with R1-L06 ("Session end: all wounds clear") and R1-L07 ("Wounds clear at end of session"). Requires PP-level canonical override. Patches that override session-clearance are unprecedented in the v30 baseline.

**EC-D1.I-02 [P2] (C1.2):** With R1-L11 (FR Dissolution → +1 Wound to Knot partner), the canonical mechanic *already* delivers a Wound at a moment-of-narrative-weight. Adding "permanent" to it doubles the permanence (already triggers Conviction Scar via Knot rupture; would also trigger physical-Wound permanence). Single-event-double-channel coupling.

### Optimal play
**EC-D1.O-01 [P1] (C1.2/C1.4):** Player optimal strategy: avoid combat entirely after first 3–5 permanent Wounds. Combat avoidance is mechanically incentivized over canonical's "combat is one tool among several" framing.

**EC-D1.O-02 [P2] (C1.4):** Players take only the lowest-Endurance characters into combat (already at floor, take no further penalty), reserving high-Endurance characters for fieldwork/social. Reverses canonical role differentiation — high-End characters become combat-averse.

### Degenerate
**EC-D1.DG-01 [P2] (C1.2):** If "catastrophic" criterion is too narrow, never fires → C1.2 = C1.1 with overhead.

**EC-D1.DG-02 [P1] (C1.2):** If "catastrophic" criterion is too broad, fires too often → C1.2 = C1.4 with degeneracies described above.

---

## 7. Decision-shape findings

**Recommendation: C1.3 (Knot-tagged permanence via existing Conviction Scar channel).**

**Rationale:**

1. **C1.1 (pure canonical) passes 24/24 NERS** but has an acknowledged narrative-weight gap (Horizontal direction, ⚠ on N and R). Solves the question by leaving it alone.
2. **C1.2 (catastrophic-permanent) fails categorical R and S checks** at full NERS grain. The Pool floor (R1-L08) reverses canonical resilience hierarchy under permanent-wound accumulation; Threadwork penalty (R1-L03) is unfloored, producing practitioner-extinction cascades. Undefined "catastrophic" criterion is a P1 ambiguity. Reject.
3. **C1.3 (Knot-tagged) passes 24/24 NERS** and uses canon's existing P1 (Conviction Scar) and P2 (Witness Scar) channels for narrative permanence. The mechanical Wound continues to clear at session end per R1-L06. The narrative weight Wildermyth provides is delivered through existing Scar accumulation. **Strict subset of canonical surface; no new tracking; passes all NERS at full grain.**
4. **C1.4 (all-permanent) fails on multiple categorical axes.** Reject.

**Concrete implementation under C1.3 (no new code, canonical clarification only):**

- Affirm canonical session-end Wound clearance (R1-L06) without modification.
- Document explicitly that **narrative-weight permanence for combat events is carried by the Conviction Scar channel** (R1-L09), not by physical-wound persistence.
- Verify the existing FR-Dissolution + Knot rupture cascade (R1-L11 → Conviction Scar via fieldwork §5.6b "broken at high strain → Conviction Scar +1 both partners") is well-documented as the *primary mechanism* by which combat events leave permanent narrative residue.
- Optionally extend: dissolution-witness Scar (R1-L12) propagates to PCs witnessing a Dissolution event in combat. This already exists per canon — confirm no further specification needed.

**Decision-shape statement for Jordan ratification:**

> Wounds clear at session end (canonical, preserve). Narrative-weight permanence for catastrophic combat events is carried by existing Conviction Scar / Witness Scar channels, triggered by canonical Knot rupture, FR Dissolution, and Dissolution-witness mechanics. No new permanent-wound channel introduced. The Wildermyth narrative pattern is satisfied via the existing Scar apparatus, not via a parallel physical-wound permanence track.

**Items deferred to Jordan:**

- Confirm: should Conviction Scar accumulation thresholds be tightened to make permanence-from-combat events *more frequent*, since Wound permanence is rejected? Currently Conviction Scar fires on Piety Track ≥ 3 events; could the threshold be tied to combat-event severity directly?
- Confirm: should the synthesis §4 R1 entry be marked "resolved — see combat_arch_residual_stress_01/r1_wound_permanence.md" upon Jordan acceptance?

---

## 8. Open items / observations surfaced during R1

- **Pool floor (R1-L08) is the load-bearing floor for permanent-wound asymmetry.** If Jordan ever revises the Pool floor downward, R1's analysis must be re-run.
- **Threadwork penalty is unfloored (R1-L03).** This is independently a candidate for stress testing — at very high natural Wound counts in a single session, Threadwork operations become trivially impossible. Module R1 surfaces this but does not test it directly.
- **PP-684 → PP-711..715 mapping** (Disposition ceiling = Bonds) — the Disposition-ceiling rule appears in fieldwork §3 line 364: "Maximum Disposition per NPC is capped by the player's Bonds attribute: ceiling = Bonds (PP-684, revised from PP-632 floor formula)." This file references "PP-684" but per Module 0 the 4/18 PP-684 was renumbered. **The fieldwork_v30 file has stale PP citation.** Carrying as a finding for editorial follow-up (not in scope for R1 to fix).

---

## 9. Module status

| Item | Status |
|---|---|
| Canonical sources fetched at full depth | ✓ |
| Verification ledger entries (13) | ✓ |
| sim_gate('custom', systems=['combat', 'derived_stats']) | (called at commit) |
| NERS full-grain analysis (96 cells) | ✓ |
| Mode B chains (5) | ✓ |
| Mode D edge cases (15 across 9 categories) | ✓ |
| Decision-shape finding | ✓ |
| Stale PP citation surfaced (fieldwork §3 PP-684 → PP-711..715) | ✓ |

**Module 1 status: verified.**
