# Refutation lane — DETERMINISM / REPLAY

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0068]
_Skeptic lane, 2026-07-05, working tree only. Cites file §section or tags [UNGROUNDED]._

## Target claim under attack

Synthesis: "Determinism PP-687 §6 V4 conditional on ORD-3/ORD-4." V4 =
"same seed+choices → identical KEY_LOG hash" (`propagation_spec_v1.md` O.8), and the charter's
replay clause = "same Key log → same narrative state, PP-687 §6 V4" plus Q4's "same rendered text."
The synthesis imports the propagation-spec determinism story by reference and adds ONE named
condition (ORD-3/ORD-4). My thesis: **the imported condition set is necessary but not sufficient —
the four NEW computation layers the synthesis adds (L2 detect, L3 ration, L4 cast, L5 render) each
introduce a nondeterminism surface that O.8's precondition enumeration never contemplated.** None is
fatal; each has a concrete fix. Verdict SOUND-WITH-FIXES.

## What the imported precondition set actually covers

`propagation_spec_v1.md` O.8 enumerates the COMPLETE determinism precondition set as: O.1 fixed
phase order + O.3 ORD-1/ORD-2 + O.4 SSI-1..4 + O.5 RNG-1..3 + O.6 ORD-3. Every one of these is about
**Key emission ORDERING, RNG threading, and phase sequencing** of the EXISTING emission machinery.
The set was derived (O.8, §4.2 Theorem B) for a world where the only things that emit are faction
actions, scene resolution, echoes, and accounting. It says nothing about **derived-score float
comparisons, candidate-selection tiebreaks, dedup-set iteration, or render-time fragment selection**,
because none of those existed in the machinery O.8 audited. The synthesis bolts four such layers on
and re-uses O.8's conclusion verbatim. That is the load-bearing gap.

---

## FINDING 1 (MAJOR) — `convergence_fired_set` is a second live ORD-2 violation the synthesis *introduces*

Synthesis L2(a): "8 COLLISION conjunctions ... edge-triggered-once ... (`convergence_fired_set`
dedup; sidesteps ORD-3 mid-cascade nondeterminism ...)."

`propagation_spec_v1.md` O.3 ORD-2 is absolute: "no `set()` may gate emission/mutation order
anywhere in the tick (generalizes the game_state.py hash-seed fix)." O.6 ORD-3 exists SOLELY because
`compute_observers` returns a bare `set()` and that was found to be "a live ORD-2 violation in the
substrate's own reference pseudocode."

The synthesis names `convergence_fired_set` as a Python **set** used for dedup at the detector. Two
distinct failure paths:
1. If detection iterates candidate conjunctions and emits `meta.convergence_detected` in the order it
   walks a set (or filters against a set whose iteration seeds the emit loop), the EMISSION ORDER of
   the convergence Keys is set-iteration-order-dependent → hash-seed-dependent → different
   `sub_step_index` assignment (SSI-1) → different KEY_LOG hash → **V4 fails.**
2. Multiple convergences firing at one ACCOUNTING_BOUNDARY get their `causes[]` and `sub_step_index`
   in whatever order the set yields. Downstream L3 rationing then selects over them, so the
   nondeterminism propagates into WHICH arcs get scenes.

The synthesis's own mitigation — "detect at ACCOUNTING_BOUNDARY over SETTLED state ... sidesteps
ORD-3 mid-cascade nondeterminism" — only addresses the READ side (observer order while reading state
mid-cascade). It does NOT address the detector's OWN emission ordering over its candidate set. The
"sidesteps ORD-3" claim is therefore partial and reads as more reassuring than it is: it fixes reads,
not the detector's emit order. This is a NEW ORD-2 violation, distinct from the compute_observers one
that ORD-3 covers, so "conditional on ORD-3" does not absolve it.

**REQUIRED_FIX:** Specify `convergence_fired_set` (and any dedup structure at L2/L3) as an
order-preserving container keyed by a total order — e.g. a dict keyed by
`(conjunction_id, participating_actor_ids sorted, season_index)` with insertion-order iteration, or
an explicit sort of detected convergences by `(conjunction_id, min(participating_actor_id))` before
the emit loop. Add a conformance rule (extend arch_B C-6) asserting no `set()` gates convergence
emission order, mirroring ORD-2.

---

## FINDING 2 (MAJOR) — L3 rationing Top-N selection has no specified tiebreak; ties are common → nondeterministic scene set

Synthesis L3: "rations detector output into player_agency §4.3's 3-5 scene envelope; salience economy
(§3.3 accumulator generalized to arcs ...)." This generalizes `articulation_layer_v30.md` §3.3
(`unarticulated_weight += stakes_weight(key)`) and §4.3 ("Top-N Keys per year by significance get
chronicle paragraphs").

The accumulator is **integer-valued**: §3.2 `stakes_weight` is 1-5, `significance` range 0–13
(`articulation_layer_v30.md:131,137`). With ~110 arc-vectors competing for a 3-5 slot ceiling,
**equal-salience ties at the marginal slot (5th vs 6th) are not a corner case — they are the common
case** for small integer scores over many candidates. Neither §3.2, §3.3, §4.3, nor the synthesis
specifies a tiebreak. "Top-N by significance" with an unstable sort or a dict/set-seeded iteration
picks a nondeterministic subset of tied arcs → different arcs injected → different `scene.*` content
Keys emitted → different KEY_LOG → **V4 fails.**

This is the single biggest replay hole because it sits on the CEILING selection (C7): the rationing
layer is explicitly a chooser among competitors, and choosing is exactly where a stable total order
is mandatory and absent. O.8's precondition set never mentions selection tiebreaks because the legacy
articulation layer's Top-N was never on the replay-critical path the way an arc-rationing ceiling is.

**REQUIRED_FIX:** Mandate a total-order tiebreak on every Top-N / rationing selection: sort by
`(salience DESC, tier_rank, arc_vector.id ASC)` (id is unique per `arch_B_arc_vector_engine.md`
schema, giving a guaranteed total order). Forbid unstable sort and set/dict-iteration-seeded
selection. Add as a conformance rule alongside arch_B C-6. Same fix applies to §4.3 chronicle Top-N
and §3.3's "notable individuals top-N named NPCs by accumulated weight" (`articulation:226`).

---

## FINDING 3 (MAJOR) — float threshold `±0.40` on cosine + float product in the meaningfulness test → boundary/accumulation-order nondeterminism, and cross-oracle (Python↔GDScript) divergence

Synthesis L2(b): "general cosine-similarity backbone ... (cascade_fidelity 4-season window ±0.40,
sim-validated +0.937) from faction-pairs to arc-vector pairs." This lifts
`articulation_layer_v30.md` §3.1 trigger-9 verbatim: `if abs(sim) > 0.40` over
`cosine_similarity(a.cascade_fidelity_history[-4:], b.cascade_fidelity_history[-4:])`
(`articulation:99-101`).

Two determinism hazards O.8 never covers:
1. **Boundary sensitivity + accumulation order.** `cosine_similarity` is a sum of products divided by
   norms. Floating-point summation is not associative; the value near the `0.40` boundary can land on
   either side depending on the order terms are accumulated. If the pair-iteration or the
   per-pair term order is set/dict-seeded, a marginal pair flips fired/not-fired → a
   `meta.convergence_detected` Key appears or not → different KEY_LOG. Generalizing from ~5-faction
   pairs (§3.1) to ~110 arc-vectors is O(N²) ≈ thousands of pairs, each a boundary coin-flip risk;
   the synthesis's `+0.937` validation was for ONE canonical faction pair over 30 seasons
   (`articulation:112`), NOT for the arc-vector-pair regime it is being generalized to.
2. **Cross-oracle divergence (§6/§7 port↔oracle discipline).** V4 must hold for the GDScript port,
   whose oracle is the Python `sim/`. Python `float` and GDScript `float` can disagree in the last
   ULP; a `> 0.40` comparison at the boundary can resolve differently on the two platforms → the port
   emits a convergence Key the oracle does not (or vice versa) → key-log parity red. CLAUDE.md §6
   (ED-1050) already records one instance of a port silently diverging from its oracle at a threshold
   (`adef_threshold`); this is the same class of bug pre-loaded into the detector.

The meaningfulness test (L2, Q3) — "durability × tie-proximity × identity-touch" — is a **float
PRODUCT with a pass/fail threshold**, inheriting the same boundary hazard, plus tie-proximity =
"tie-graph distance to a participating_actor" is a graph traversal whose nearest-actor result can be
order-dependent if the adjacency is stored as dict-of-sets with distance ties.

**REQUIRED_FIX:** Either (a) move all replay-critical thresholds to integer / fixed-point arithmetic
(quantize cosine and the meaningfulness product to a fixed decimal grid, compare integers), or (b)
canonicalize a single summation order (sort terms by actor_id before summing) AND publish an explicit
epsilon-band + a documented tie-to-the-conservative-side rule, then pin the SAME arithmetic in the
GDScript port and add it to the key-log parity harness. Make tie-graph distance deterministic
(order-preserving adjacency + total-order tiebreak on equal-distance actors). Note this is a
[OPEN — Jordan tuning] number ONLY as to the *value* 0.40; the *arithmetic determinism* is structure,
not calibration, and must be ruled regardless of where 0.40 lands.

---

## FINDING 4 (MAJOR) — L5 realizer's fragment-selection RNG source is undefined; V4's "same rendered text" is unbacked while RNG-MODEL-COLLISION is open

Charter Q4 + O.8 require "same rendered text" on replay. Synthesis L5: realizer = "fragment schema on
existing Key metadata only, coherence-tiers+solmund §18 → runtime lookups ... deterministic spliced
prose, no runtime LLM — C1" and capstone #11 wants "two-seed divergence" (different seeds → different
chronicles).

The problem: two-seed DIVERGENCE and single-seed REPLAY are the same requirement stated twice — both
demand that fragment selection be a **pure function of seeded state**. But the synthesis never names
the selection source. If the realizer picks among synonymous fragments/templates using anything other
than the seeded stream — a hash of an actor-name string, dict iteration over template variants, or
(worse) wall-clock — then same Key log → DIFFERENT text → V4 fails on the render clause even when
narrative STATE replays perfectly. "Deterministic splice" is asserted, not constructed.

This is aggravated by the still-open **RNG-MODEL-COLLISION** (`propagation_spec_v1.md` O.5, decision
queue item 5): three unreconciled RNG models coexist (single `World.rng` stream; §6.1 per-emission
seed; conversion-strategy named-draw service). Until that is disposed, "which stream does the realizer
draw from" has no canonical answer. Worse, the chronicle renders at the ANNUAL accounting boundary
walking the whole `causes[]` chain (`articulation:201,209`); if it draws from the shared `World.rng`
stream at render time, it consumes stream position and perturbs every downstream draw → replay
divergence unless render uses a dedicated, separately-seeded sub-stream. RNG-3 (per-Key
`rng_draw_index`, Open Flag O-3) — the mechanism that would isolate this — is unspecified.

**REQUIRED_FIX:** Rule that the realizer selects fragments either (a) with ZERO randomness (pure
deterministic function of Key metadata + focalizer + register band — the cleanest, and consistent
with "existing Key metadata only"), or (b) from a DEDICATED render RNG sub-stream seeded as a pure
function of `(campaign_seed, key.id)` so render draws never perturb simulation draws and replay is
exact. Forbid string-hash / dict-iteration / wall-clock selection explicitly (C2/C1 bake lint should
also catch wall-clock). This fix is gated on disposing RNG-MODEL-COLLISION first — flag as a Stage-0
render-lane precondition, since Stage 0 ships the realizer.

---

## FINDING 5 (MINOR) — arch_B C-6 is a test asserting the property, not a construction guaranteeing it; no CI can actually run it deterministically until 1-4 are fixed

`arch_B_arc_vector_engine.md` conformance C-6: "replay: same Key log → same store (PP-687 §6 V4)."
This is stated as a CI rule, but a replay-equality test can only PASS reliably if the machinery is
already deterministic; run against the current synthesis it would be FLAKY (pass/fail depending on
hash seed), which is worse than a hard failure because it hides Findings 1-4 intermittently. CLAUDE.md
§7 already warns the sim "has no regression oracle beyond the §8 smoke test" and that a degenerate
seeded batch "nothing flags." A flaky C-6 inherits exactly that failure mode.

**REQUIRED_FIX:** Split C-6 into (i) CONSTRUCTION conformance rules — no `set()` gates emission/
selection order (Finding 1), every Top-N carries a total-order tiebreak (Finding 2), all
replay-critical thresholds are integer/fixed-point or canonical-summation-order (Finding 3), render
selection is zero-RNG or dedicated-substream (Finding 4) — checkable by static lint on the source, and
(ii) a replay-equality smoke test run under ≥2 distinct `PYTHONHASHSEED` values (forcing set-order
variation) so a residual ORD-2 leak fails LOUDLY rather than flakily. The static rules are the real
guarantee; the smoke test is the backstop.

---

## Things I tried to break and could NOT (defensive credit)

- **Phase order / SLATE-FREEZE / ECHO-DEFERRAL.** The detect-THEN-schedule-THEN-render inversion runs
  detection at ACCOUNTING_BOUNDARY over SETTLED state; the propagation-spec's A1/A2 (Theorem A) give a
  clean per-tick fixpoint, so the detector reads a stable snapshot, not a mid-cascade one. This is
  genuinely the right place to detect and removes a whole class of ordering bugs. No finding.
- **Wall-clock in §3.4 "Local environmental state (scene location, time...)"** — "time" resolves to
  in-game season/clock, not wall-clock (`articulation:161`), so no leakage there. (Wall-clock risk
  survives only at render-fragment selection — Finding 4.)
- **FSM stepping on non-converging oscillating stats.** The C1 macro loop can oscillate at bounded
  amplitude forever (`propagation_spec_v1.md` §4.3, cross-tick convergence NOT proven; D.6 double-count
  open). But an oscillation is still DETERMINISTIC — same log replays the same oscillation — so it is a
  convergence/stability problem, not a replay problem. Out of my lens; belongs to the convergence
  refutation lane. Flagged only where it feeds edge-triggered detection (dedup-scope of
  `convergence_fired_set` — tick vs campaign scope unspecified), which is a sub-case of Finding 1.
- **Fan-out width tripping the cascade cap.** Correctly handled: D.1/D.5/B2 make a single N-target Key
  one emission at one `cascade_depth`; wide casting/injection fan-out does not perturb termination
  determinism. No finding.

## Bottom line

The spine's determinism story is sound and honestly scoped — but the synthesis's single-clause import
("conditional on ORD-3/ORD-4") launders four new nondeterminism surfaces past an audit that never saw
them. All four have concrete, non-architectural fixes (order-preserving dedup, total-order Top-N
tiebreaks, integer/fixed-point or canonical-order thresholds, zero-RNG-or-dedicated-substream render).
Fix them and add construction-level conformance rules (Finding 5) and V4 holds for the synthesized
engine, not just the legacy substrate. Verdict: **SOUND-WITH-FIXES.**
