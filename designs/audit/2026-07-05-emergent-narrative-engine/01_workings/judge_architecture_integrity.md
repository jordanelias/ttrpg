# Judge — Architecture Integrity lens

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0069]
## Date: 2026-07-05 · Lane: IN

Lens: score primarily on **the substrate contract** (total accounting; determinism/replay;
holonic containment C3/C5; edge hygiene vs the F-4/S-1 failure class; conformance
checkability) + **Q1/Q3 mechanism quality**. Charter acceptance tests, not taste.

## Verifications run against the working tree (not memory)

1. **scene_entered double-emitter is a live defect.** `references/module_contracts.yaml`:
   `scene_slate` L349 emits `mechanical.scene_entered` (flagged, terminal:false) AND
   `game_director` L375 emits it — `[OPEN — Jordan]` attribution conflict. Crucially,
   `scene_timer` L393 already `consumes: {type: mechanical.scene_entered, from: [game_director]}`
   — so the **consumer edge already treats game_director as the emitter**. Resolving the conflict
   in game_director's favour (B and C do; A leaves it open) is the edge-hygiene-correct call.
2. **arc-state field is NPC-scoped only.** L150 `{name: "arc state", bucket: clock}` is
   npc_behavior §5's one-way FSM to a terminal phase. No general per-arc lifecycle field exists —
   the concrete form of ED-IN-0003. Register-formalizability dossier confirmed.
3. **articulation is a wildcard reader.** L768 `consumes: {type: "*", from: engine}` — B/C's
   plan for game_director to mirror this subscription is grounded.
4. **Determinism (V4) is CONDITIONAL.** `propagation_spec_v1.md` §1: replay V4 (same seed →
   identical KEY_LOG hash) holds only under the full precondition set (O.1 + ORD-1/2 + SSI-1..4 +
   RNG-1..3 + ORD-3). **ORD-4** (`scene_slate._queue` is MODULE-scope, L114-118): until it lands,
   "determinism holds only under SEQUENTIAL execution; parallel batch runs share module-global
   queue state." This directly threatens the arc_test_batch 5-seed narrative-regression method
   (anti-oatmeal #3) if seeds run in parallel. **Also a live RNG-MODEL-COLLISION** (§1 O.5): three
   unreconciled RNG contracts — an inherited hazard for all three architectures.
5. **C's detector primitive is real and sim-validated.** `articulation_layer_v30.md` L99-100:
   `cosine_similarity(faction_a.cascade_fidelity_history[-4:], faction_b...[-4:])` already exists.
   C's generalization from faction-pairs to arc-pairs rides a tested mechanism, not fresh authoring.
6. **A's F-4 close is surgical and real.** L294-298: `scene.combat_resolved` is declared to render
   "by default" in prose §6.4 under the ED-936 `[ASSUMPTION]` grant, but the §3.1 TABLE never got
   the trigger — that gap IS F-4/ED-IN-0004. Adding it to the table (A's move) is the literal close.
7. **Transport-fitness dossier is a stub** ("test", key_points ["a","b"]) — S-1 seam claims rest
   on architecture self-assertion + my module_contracts/propagation_spec spot-checks, which do
   substantiate the shared transport. Doesn't differentially harm any architecture (all ride the
   same substrate) but the S-1 lane produced no independent evidence.

## Substrate-contract scorecard (the explicit charter checklist, §"substrate contract")

| Contract line item | A | B | C |
|---|---|---|---|
| Total accounting (RENDERED/ACC/CONSUMED/DISCARDED, ≥1 consumer) | clean, **+1** new Key | **best — ZERO new Keys** | clean, **+2** new Keys |
| Resolve `mechanical.scene_entered` ownership | **MISSED (left OPEN)** | resolved (game_director) | resolved + single-emitter lint |
| Home docs for game_director / scenario_authoring | **MISSED (claims no module)** | both + scene_slate | both, subordinates scene_slate |
| All six directions w/ ordering notes | **MISSED (up/down/diag UNUSED)** | all six | all six + ORD conditionality cited |
| Replay determinism | fine (minimal new state, boundary-only) | asserts V4, **does not fix ORD-4** | **UNIQUELY fixes ORD-4** (queue→World) |
| Holonic containment (owns vs reads) | **cleanest** (owns only fired-set) | clean (owns general store, reads NPC specialization) | heaviest (extends L150 global; salience+curve state) |
| Conformance (each once in tools/) | 4 lints | 6 rules **mapped to corpus defects** | 6 rules (adds booking + watch/participate invariants) |
| Edge hygiene vs F-4 render gap | **CLEANEST close** (§3.1 table + C6 beats) | close "by construction" — **§3.1/C6 not explicit** | rationing addressed, §3.1/C6 beats not explicit |
| C2 attack surface (absolute constraint) | smallest | small (Key-neutral) | **largest** (entire state is narratological; lint-dependent) |

## Q1 mechanism quality (primary)

- **A — materially short.** Participation rides existing edges (marker→slate→ordinary engine→
  outcome Key into causes[]) and genuinely works, but with NO per-arc lifecycle it cannot
  represent "the arc advanced BECAUSE you participated" as a first-class transition — capstone #3
  is demonstrable only as a stat-flip inside a static conjunction. The load-bearing Q1 shortfall.
- **B — strongest.** Participation IS arc I/O: the vector subscribes to Keys whose causes[]/
  targets[] intersect participating_actors; `pressure_effects.condition` guards + the lifecycle
  transition fire on the participated outcome. ARC-S07's "Covert Contact fails → Loyalty −1" and
  "3 successes → floor 6" are participated-outcome-conditioned FSM transitions — capstone #3 direct.
- **C — strong via the window guarantee.** The engagement-window as a *booking invariant* (≥1
  injection slot per N seasons while state ∈ {seeded,active,escalating}) directly serves C7 +
  Q4's "keep ≥1 open intervention point until converging" — exactly what A cannot guarantee.
  Relies on the lifecycle field C owns.

## Q3 mechanism quality (primary)

- **A — a whitelist, not a discriminator.** The 8 authored COLLISION conjunctions, evaluated over
  SETTLED state at ACCOUNTING_BOUNDARY. Because it reads settled state (not the Key stream) it
  structurally CANNOT do causes[]-overlap or temporal-window correlation — the charter's named Q3
  test dimensions. No meaningfulness test. Cleanest CLOSE of ED-IN-0003 for 8 cases; not a general
  legibility engine.
- **B — strongest general discriminator.** COLLISION rows become first-class convergence vectors
  whose predicates read OTHER vectors' arc_state; detection = correlation tests (shared targets[],
  causes[] overlap, temporal_window, same-direction pressure) — the charter mechanism literally.
  Meaningfulness test generalizes §3.2 significance (identity-touch/tie-proximity/durability).
  Taxonomy + lifecycle measurable off the data.
- **C — best-grounded primitive, but SUBORDINATED.** Rides the sim-validated trigger-9 cosine
  primitive (corr +0.937) — the only detector grounded in a tested mechanism. But detection is a
  service the scheduler CALLS, and the meaningfulness gate is a *budget filter*: "legibility is a
  budgeted decision." This risks the budget starving genuine convergences (false negatives) — a
  mechanism-integrity concern for the core emergence deliverable. C flags it; mitigates via the
  §3.3 re-promotable accumulator.

## Determinism sub-criterion — the sharpest differentiator my lens surfaces

Only **C structurally closes ORD-4** by relocating the season scene-queue onto World scope as
director-owned state. B asserts V4 inheritance but leaves `scene_slate._queue` at module scope —
the parallel-replay non-determinism hazard persists (a real threat to the 5-seed regression gate).
A doesn't touch the queue either. This is a **mandatory graft from C into any winner.**

## Scores

- **A — 64.** Cleanest containment and the single most surgical, ratifiable close of F-4/ED-IN-0004
  + C6. But misses THREE explicit substrate-contract line items (scene_entered, home docs, six
  directions), is the weakest on both primary mechanism criteria (whitelist Q3, lifecycle-less Q1),
  and the detector reading settled state cannot do the charter's correlation tests. Low cost,
  low ambition.
- **B — 84. WINNER.** Maximizes the substrate contract (fullest coverage; ZERO new Key types =
  best total accounting and capstone #9 by design; cleanest arc-state containment; conformance
  mapped to the actual corpus defects) AND both primary mechanisms (first-class participation→FSM
  transition; general correlation-test discriminator with meaningfulness). Its costs — authoring
  becomes engineering, ~15% GM-judgment arcs need decision functions, scripting-drift hazard,
  temporal_window unspecified — are content/calibration costs, NOT architecture-integrity defects.
  On my lens they barely move the needle; the scripting-drift hazard is the only C5 concern and it
  is a discipline rule, not a structural flaw. Gap: does not explicitly discharge the §3.1
  table/C6 render (graft from A) and inherits ORD-4 (graft from C).
- **C — 78.** Strong substrate (uniquely fixes ORD-4; scene_entered single-emitter; sim-grounded
  detector primitive; owns the rationing/texture/watch-vs-participate layer B lacks) and genuinely
  wins Q4. But: heaviest new-state footprint, largest C2 attack surface (its ENTIRE state is the
  narratological state the doc-12 veto forbids — correctness rests on a lint holding), largest
  ratification blast radius, and — decisively for my lens — it SUBORDINATES detection to
  scheduling, risking false-negatives on the emergence the whole engine exists to surface. Great
  Q4 layer wrapped around a slightly demoted Q3 core.

## Winner: Architecture B (the Arc-Vector Engine)

It is the architecture the substrate contract and the Q1/Q3 mechanism tests reward. The
lifecycle field it builds IS the concrete form of ED-IN-0003; its Key-neutrality is the cleanest
total-accounting story in the set; its detector is the charter's correlation-test mechanism made
real. B is not complete — it needs the grafts below, three of which are load-bearing (A's §3.1/C6
close, C's ORD-4 fix, C's rationing layer).

## Grafts the synthesis MUST keep

1. **[A, mandatory] §3.1 trigger-table completion — the literal F-4/ED-IN-0004 + C6 close.**
   Add `scene.combat_resolved` + `scene.investigation_resolved` (discharging the §6.4/ED-936
   `[ASSUMPTION]`, L294-298) AND the four ED-681 Rendering-Crisis thread beats (C6). B closes
   ED-IN-0004 "by construction" via the realizer but never discharges the table gap or guarantees
   the thread beats render — without this graft the synthesis leaves the literal render defect open.
2. **[A, mandatory] Total-accounting discipline: every non-firing marker EXPLICITLY DISCARDED with
   reason (predicate_false, logged), and evaluate convergence over SETTLED state at
   ACCOUNTING_BOUNDARY** (not mid-drain) to avoid the ORD-3-conditional mid-cascade non-determinism.
3. **[C, mandatory] The ORD-4 fix — relocate the season scene-queue onto World scope as
   engine-owned state.** The ONLY proposal that closes the parallel-replay determinism hazard B
   inherits; load-bearing for V4 replay and the 5-seed narrative-regression gate.
4. **[C, mandatory] The sim-validated trigger-9 cosine-similarity primitive** (articulation_layer
   L99-100, corr +0.937) as the GENERAL correlation-test backbone, generalized faction-pairs →
   arc-vector pairs — so the detector rides a tested mechanism, not only the 8 hand-authored
   COLLISION conjunctions.
5. **[C, mandatory] The pacing/rationing layer as a SUBORDINATE service over B's detector**
   (invert C's subordination: detect-THEN-schedule, so scheduling never starves detection).
   Keep: cut-scene rationing inside player_agency §4.3's 3-5 envelope; texture-between-scenes as
   the demotion destination (immersion gap); the **watching/participating ratio as a CI-checkable
   booking invariant** ("every major arc keeps ≥1 open intervention point until converging") —
   this is how capstones #4 and Q4 pacing become demonstrable. B has no rationing governor.
6. **[C, keep] scene_entered single-emitter resolution + its conformance lint** (both B and C
   resolve to game_director; keep C's explicit single-emitter CI rule).
7. **[A, keep] Staging as independently-mergeable stages riding existing homes** — B's Stage-0
   compiler gate is heavier; borrow A's ratifiability discipline so early stages land without the
   whole engine.
8. **[C, keep] The C2 literal-string bake-audit lint** (A and C both propose) — mandatory given C2
   is absolute; the winner's arc-state/lifecycle labels must never surface.
