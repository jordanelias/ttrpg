# Armature Compliance — All Systems

**Date:** 2026-05-28
**Task:** Apply the seven-principle Combat-Derived Mechanical Armature (A1–A7) to every Valoria resolution system. This is the deferred cross-system adjudication the armature document explicitly reserved ("swinging it across the project is not [in scope here]") — now requested.
**Method:** Walk A1–A7 as tests per system. A1/A6/A7 **computed** (Monte Carlo 200k + closed-form σ-leverage), not asserted — per this session's standing lesson that quantitative claims must be empirical. A2–A5 are structural judgments grounded in the 2026-05-28 resolution diagnostic + canonical reads.
**Bias:** `[SELF-AUTHORED — bias risk]` on BOTH inputs — the armature and its referenced standards (`attribute_weight_standard.md`, `derived_stats_audit.md`) are Claude-authored, as is the resolution diagnostic being reconciled. §6 turns the critique on the armature itself rather than only grading other systems against my own yardstick.
**Grading target:** **canonical, as-shipped** systems (`*_v30`), NOT proposals. Combat is graded as canonical `combat_v30` (v31-era, flat modifiers); `combat_v32_proposal` is noted as combat's *proposed remediation*, since the armature is derived from it and would otherwise grade combat against itself.

---

## §1 — Headline: A6 and A1 are orthogonal (the test that proves the armature isn't redundant)

The single most useful result of running all seven principles: **σ-leverage parity (A6) and modifier-impact uniformity (A1) catch different failures, and a system can pass one while failing the other.**

- **Faction at typical stat 3** → bare 3D pool → σ-leverage **0.289σ/pt** → **A6 PASS** (inside 0.24–0.36). Attribute weight is *fine*.
- **The same faction** → a flat −1 Ob modifier swings **31.0pp at 2D** but only **11.1pp at 18D** → **A1 FAIL** (non-uniform). The small pool is pathological for *modifiers* even though it's fine for *attribute leverage*.

This means the armature's principles are not a single idea in seven coats. A1 is about how *modifiers* scale with pool; A6 is about how *attributes* scale with pool; they diverge because faction's `mult×1` low-baseline construction happens to land A6 in-band while leaving the pool small enough that flat modifiers (A1) and stacks (A2) misbehave. **Diagnosing "faction is broken" requires naming which axis** — and the armature does, where the NERS verdict only said "non-compliant."

---

## §2 — The comprehensive matrix (canonical systems × A1–A7)

Legend: ✓ pass · ◐ partial · ✗ fail · N/A not applicable (no probabilistic-resolution-with-modifiers at this layer) · ⟂ deferred-to-proposal

| System | A1 σ-impact | A2 no-foreclose | A3 state-gate | A4 two-tier | A5 min-apparatus | A6 σ-leverage | A7 1/k resource |
|---|---|---|---|---|---|---|---|
| **Combat** (canonical v30) | ✗ flat mods (F1) → ⟂ v32 fixes | ◐ floor-bounded → ⟂ v32 tanh | ◐ phase, not mod-gated → ⟂ v32 | ✓ weapon/stance setup | ⟂ (Hodge is v32) | ✓ **0.302** (ref) | ✗ **Health** mult+stepped |
| **Social contest** | ◐ mult-margin, clock-routed | ◐ Spent=exit; genre-0.5 near-inert | ◐ interaction-types | ✓ adjudicator+format setup | ✓ (matrix irreducible) | ✓ **0.354** (+17%) | ✓ Composure/Concentration ×N |
| **Faction** | ✗ **flat −1 on 2–7D** (31pp@2D) | ✗ **Stab-0 terminal; 1% punch-up** | ◐ card/cooldown, not mod | ✗ **bare roll, no setup tier** | ◐ CI accounting good; dice overlay reducible | ◐ **0.289 typ but 0.189@stat7** | N/A (ledgers, not ×N) |
| **Mass battle** | ◐ flat Disc-penalty, mostly healthy pools | ◐ rout-brake; **no Pool Floor (MB5)** | ✓ 7-phase gated | ✓ Battle-Plan + override setup | ◐ 2-attr pool (ER-9) | ◐ **0.408@Cmd3 HIGH → in-band@Cmd4-7** | ◐ army-Health mult (by-design parallel) |
| **Threadwork** | ◐ flat Ob-mods, **floored at 5D** | ✓ Crisis-arc recoverable; Sat-cap; N-Way auto-cap | ✓ Coherence-threshold + op-type gated | ✓ Leap+op-type setup | ◐ co-move tables; Knot TIER-DRIFT (ED-841) | ✓ **0.302** (exact) | ✓ Thread-Fat ×5; Coherence=clock |
| **Investigation/fieldwork** | N/A (deterministic resolution) | ✓ five-filter can't stack-foreclose | ✓ **five-filter IS state-gating** | ✓ **exemplar** (det. filter + dice→clock) | ✓ principled, not lookup | ✓ **0.302** (newly verified) | N/A (few ×N buffers) |
| **Peninsula/victory** | N/A (no dice) | N/A (deterministic clocks) | N/A | ✓ (fully deterministic) | ✓ minimal | N/A (threshold, no roll) | N/A (accumulators) |

---

## §3 — Per-system armature-compliance lines

**Combat (canonical v30) — A1 ✗ / A2 ◐ / A3 ◐ / A4 ✓ / A5 ⟂ / A6 ✓ / A7 ✗(Health).** As-shipped combat uses *flat* modifiers — it is the v31 F1 defect the armature was built to name; `combat_v32_proposal` (σ-space + tanh + Hodge + FoV-facing) is the remediation and passes A1–A5 by construction. The one finding independent of v32: **Health fails A7** — `(End+6)×(MW+1)` is multiplicative+stepped (End 1→2 = +71%, 3→4 = +48%, then ~8%), a survival-axis non-uniformity (derived_stats D1). A6 0.302 is the project reference. *NERS reconcile: combat's NERS-COMPLIANT verdict held the resolution sound; the armature adds that its modifier system (A1) and Health resource (A7) are the live mechanism-level gaps, the former addressed by v32.*

**Social contest — A1 ◐ / A2 ◐ / A3 ◐ / A4 ✓ / A5 ✓ / A6 ✓ / A7 ✓.** Strong on the general principles, partial on the modifier-specific ones. Genre/orientation weights are *multiplicative on margin* (×0.5–1.25), not flat-Ob — closer to uniform than faction's flat mods, and the Persuasion Track clock (A4) absorbs single-exchange variance, so A1 is mitigated structurally rather than via σ-space. A2 partial: Spent is a recoverable *exit* (not foreclosure), but the genre-0.5-at-R=1 case (diagnostic D-01) is a near-inert multiplier with foreclosure flavor. A6 +17% (0.354, in band; the missing +3 floor). *NERS reconcile: COMPLIANT verdict confirmed; armature locates the two soft edges (multiplicative-margin A1, genre-0.5 A2).*

**Faction — A1 ✗ / A2 ✗ / A3 ◐ / A4 ✗ / A5 ◐ / A6 ◐ / A7 N/A.** The worst armature performer, consistent with its NERS **NON-COMPLIANT** verdict — and the armature pinpoints *which mechanisms*: **A1** (flat −1 on a 2–7D bare pool, 31pp swing at 2D), **A2** (Stab-0 = terminal foreclosure; punch-up wall at 1%), **A4** (bare-stat roll has no setup tier weighting the resolution — the card/cooldown economy is only a partial setup). **A6 is the subtle one: PASS at typical (0.289) but non-uniform across the faction's own range** — 0.354 at stat 2 (+17%) decaying to **0.189 at stat 7 (−37%, out of band LOW)**, because bare-stat baseline = stat and σ-leverage ∝ 1/√baseline. **All three fixes converge on one move: aggregate the pool** (raise N → fixes A1 by reducing flat-mod swing, fixes A2 by lifting the floor off ~0%, fixes A4 by giving setup something to weight, flattens A6 across the range) — exactly the ER-9 / engine-reconciliation recommendation. *NERS reconcile: the armature decomposes the single "non-compliant" into A1+A2+A4+A6 mechanisms and shows they share one remediation.*

**Mass battle — A1 ◐ / A2 ◐ / A3 ✓ / A4 ✓ / A5 ◐ / A6 ◐ / A7 ◐.** Decent performer with small-pool edges. A3/A4 strong (7-phase state-gating; Battle-Plan-templates-as-setup weighting phase-resolution; zoom/auto-resolve). A1 partial — Discipline degradation is a flat −1D/−2D Power penalty, non-uniform at small pools but mostly applied to healthier summed pools. A2 partial — rout cascade is braked (ROUT_CONTAGION_MORALE_HIT=1) but there is **no Pool Floor** (diagnostic MB5; unit-deletion substitutes). **A6 newly quantified: HIGH at low Command (0.500@Cmd2, 0.408@Cmd3) → in-band at Cmd4–7** — closes the `attribute_weight_standard` GAP #2 ("magnitude unverified"); the answer is non-uniform-across-range, oversized leverage for low-Command early-game generals. A7: army Total Health is multiplicative like personal Health (deliberate cross-scale parallel, derived_stats §3). *NERS reconcile: COMPLIANT-with-backlog verdict held; armature adds the Command-leverage non-uniformity (new) and re-frames MB5 as an A2 edge.*

**Threadwork — A1 ◐ / A2 ✓ / A3 ✓ / A4 ✓ / A5 ◐ / A6 ✓ / A7 ✓.** A strong armature performer, and the best **A2** example in the project: Coherence-0 routes to a *recoverable* Rendering-Crisis arc (not foreclosure), Substrate Saturation has explicit +2 caps, N-Way opposition auto-caps via lattice collapse — three independent soft bounds. A3 strong (Coherence thresholds + restorative/manipulative/destructive op-type partition gate which costs are live). A1 partial — Coherence/Saturation/Opposition are flat Ob modifiers, but the Pool Floor 5 keeps them past the worst small-pool regime (flat −1 Ob at 5D swings ~16pp, not 31pp). A6 0.302 exact match to combat. A5 partial — co-movement tables + the Knot TIER-DRIFT contradiction (already ED-841) are authored apparatus, some reducible. *NERS reconcile: COMPLIANT verdict confirmed; armature shows threadwork already implements the A2 discipline combat's v32 had to add.*

**Investigation/fieldwork — A1 N/A / A2 ✓ / A3 ✓ / A4 ✓ / A5 ✓ / A6 ✓ / A7 N/A.** The armature **poster child.** A4 is exemplary — a deterministic Five-Filter Response Matrix (Information→Conviction→Disposition→Compromise→Ethical) *is* the setup/structure tier, and dice feed only the Evidence clock (probabilistic accumulation), exactly the two-tier ideal. A3 is the same five-filter read as state-gating (only the relevant filter fires per NPC state). A1/A2 are favorably **N/A** — there is no probabilistic *resolution* to make non-uniform or to foreclose; the dice are a feeder. **A6 0.302 newly verified** (Fieldwork Pool `(Primary×2)+History`), closing the standard's GAP #3 ("not yet checked"). *NERS reconcile: COMPLIANT + "exemplar Lesson-4 routing" — the armature confirms it as the A3/A4/A5 reference the way combat is the A1/A6 reference.*

**Peninsula/victory — almost entirely N/A.** Deterministic clocks, no dice, no modifier stacks, threshold victory. A1/A2/A3/A6/A7 are **N/A** (the armature is a *resolution*-system yardstick and this layer has no probabilistic resolution); A4/A5 trivially pass (fully deterministic = all setup, minimal apparatus). *NERS reconcile: "deterministic, correctly absent" — the armature agrees by returning N/A, which is the correct result, not a gap.*

---

## §4 — New findings the armature surfaces (beyond the NERS diagnostic)

1. **Faction σ-leverage is non-uniform across its own stat range (NEW).** 0.354 (stat 2) → 0.189 (stat 7); strong factions fall **below** the 0.24 band (−37%). The bare-stat construction means a point of stat buys *decaying* leverage as the faction strengthens. This compounds the post-F2-ruling "punching-up wall": strong rivals are hard to act on (high Ob) *and* a strong faction's own stat investment is leverage-poor. **A6-axis finding the F-series diagnostic missed.** → augments ED-865.

2. **Mass-battle Command σ-leverage is HIGH at low Command (NEW; closes a GAP).** 0.500 (Cmd 2) → 0.267 (Cmd 7); low-Command early-game generals get oversized per-point leverage. Verifies and resolves `attribute_weight_standard` GAP #2 (previously "magnitude unverified"). → new minor ledger candidate.

3. **Fieldwork σ-leverage = 0.302, PASS (NEW; closes a GAP).** Resolves `attribute_weight_standard` GAP #3 ("fieldwork not yet checked"). Fieldwork Pool sits exactly at the combat reference. (Caveat: it measures leverage on *Evidence accumulation*, which is then deterministically resolved — the leverage is real but one step removed from outcome.)

4. **A1 quantified per pool-regime (NEW precision).** Flat −1 Ob: 31pp@2D, 24pp@4D, 16pp@6D, 14pp@12D, 11pp@18D — the non-uniformity is now numeric, not asserted. σ-space holds ~19–24pp across the same range.

5. **The A6⊥A1 orthogonality (NEW conceptual).** §1 — passing attribute-parity does not imply modifier-uniformity; faction proves it. Sharpens what "fix faction" means.

---

## §5 — N3 answered (σ-space scope), per the armature's own procedure

The armature says a system's A1 result *is* the N3 answer: pass A1 → no σ-space needed; fail A1 → the remediation is σ-space (or its equivalent). Walking it:

- **Faction A1 ✗ → σ-space warranted — but aggregation is the better fix**, because raising N fixes A1, A2, A4, and the A6 across-range non-uniformity *simultaneously* (σ-space alone fixes only A1). This matches the engine-reconciliation conclusion (aggregate the faction pool per ER-9 / GD-2).
- **Mass battle A1 ◐ → σ-space optional**; pools are mostly healthy (summed); the small-Command edge is better addressed by the same aggregation logic already present.
- **Combat A1 ✗ (canonical) → σ-space is exactly the v32 fix** (already proposed).
- **Threadwork / social A1 ◐ but floored/clock-routed → σ-space NOT needed**; the Pool Floor 5 (thread) and Persuasion Track (social) already bound the non-uniformity. Adding σ-space would be apparatus (A5 violation).
- **Investigation / peninsula A1 N/A → σ-space irrelevant** (deterministic resolution).

**N3 verdict: σ-space is warranted only where pools are both small and probabilistically-resolved with flat modifiers — faction (via aggregation) and canonical combat (via v32). Everywhere else it is unnecessary or actively harmful (apparatus). "Propagate vs combat-only" resolves to "neither" — it is scale-local to the unhealthy-pool systems, and even there aggregation often dominates pure σ-space.**

---

## §6 — Critical caveats on the armature itself (unbiased)

`[SELF-AUTHORED — bias risk]` applies; an independent reviewer would press these:

1. **The armature is ~40% combat-shaped.** A1/A2/A3 are *modifier-system* principles and only bite where there is probabilistic-resolution-with-modifiers. Across seven systems they returned **N/A for two** (investigation, peninsula) and **◐ for several**, while A4/A5/A6/A7 (the general principles) graded cleanly everywhere. "Comprehensive" is honest for A4–A7; for A1–A3 the comprehensive result is partly "this principle doesn't apply here," which is a statement about the armature's reach, not just about the systems. The armature is a strong *dice-modifier* yardstick and a decent *general-design* yardstick, not uniformly both.

2. **A6's single-number test is incomplete — the across-range check is the real test.** σ-leverage is profile-dependent (∝ 1/√baseline). Faction and mass battle both **pass at the typical profile and fail at a tail** (faction LOW at stat 7; mass HIGH at Cmd 2). The armature's A6 as written ("compute at the typical profile, require ±20%") would have **passed both** — only computing across the range exposed the non-uniformity. This is a refinement the armature should absorb: *A6 must be checked across the operating range, not just at the reference profile.*

3. **Circularity risk, managed.** The armature is derived from combat_v32, so combat-v32 passes A1–A5 tautologically. I graded *canonical* combat (which fails A1) and noted v32 as the fix, rather than scoring the armature's source against itself. But the deeper circularity remains: the armature encodes combat's *answers*, so systems that resemble combat (thread — identical pool construction) score well partly by similarity. Investigation scores well by genuinely different means (A4/A3), which is the stronger evidence the armature captures something general.

4. **A7 "by-design exceptions" are doing real work.** Health (combat) and army Total Health (mass) both fail the 1/k template — and both are waved through as "deliberate multiplicative" (PP-716). If the exception covers the two most consequential survival resources in the game, A7 is less a *test* than a *description of which resources were chosen to be non-uniform*. That is defensible (toughness breakpoints as game-feel) but should be named as a near-universal exception, not a passed test.

---

## §7 — Confidence & limits

`[CONFIDENCE: high]` — A1 (MC 200k, die rule sanity-checked μ=0.40), A6 (closed-form, formula from the standard), A7 1/k (closed-form). The three computed principles are robust.
`[CONFIDENCE: medium]` — A2–A5 structural grades (judgment over canonical reads + the diagnostic; another reviewer might shift a ◐↔✓ on social A3 or mass A5).
`[CONFIDENCE: medium]` — Fieldwork A6 (verified the pool formula structure; the deterministic-resolution caveat means leverage is one step from outcome).

**Did not re-read:** the 153KB `combat_v32_proposal` in full (grounded against the compact standards docs it spawned + the armature); each system's full `_v30` doc (relied on the 2026-05-28 diagnostic's reads + targeted formula confirmation). A deeper read could shift a partial grade but is unlikely to overturn a ✓ or ✗.

**Ledger candidates (staged, not filed — consolidation handoff active):** (1) faction σ-leverage across-range non-uniformity → augment ED-865; (2) mass-battle Command leverage HIGH at low Cmd → new P3; (3) Fieldwork A6 PASS → close standard GAP #3 (no defect); (4) A6-procedure refinement (check across range, not just typical) → amend `attribute_weight_standard`. None is P1; the faction items reinforce existing ED-865.

**Bottom line:** Run comprehensively, the armature confirms the NERS diagnostic's verdicts *and* adds mechanism-level precision the NERS labels lacked — most usefully, it decomposes faction's "non-compliant" into A1+A2+A4+A6 with a single shared fix (aggregate the pool), and it certifies investigation as the A3/A4 reference the way combat is the A1/A6 reference. Its limits: it is sharpest as a dice-modifier yardstick (A1–A3 N/A on deterministic systems), and its A6 needs the across-range check this run added.
