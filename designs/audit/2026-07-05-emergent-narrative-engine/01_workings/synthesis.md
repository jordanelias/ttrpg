# Synthesis — The Unified Emergent Narrative Engine

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0068]
_Unifies Architectures A/B/C per the three judge verdicts (B wins 82/84/85, all three lenses)
into ONE layered design. Working tree only. Cites charter + grounding + dossiers; [UNGROUNDED]
tags mark my own extrapolations._

---

## 0. The verdict I am building from

All three judges (player-experience, architecture-integrity, buildability) picked **Architecture
B — the Arc-Vector Engine** as the spine, each with the SAME set of mandatory grafts from A and
C. The convergence is not a tie broken by tally; it is three lenses agreeing that B's typed
arc-vector store is the substrate the other two architectures either decline to build (A) or
merely read on top of (C). My job is to seat B as the spine and bolt on the grafts as
subordinate services, not co-spines.

**One-line architecture:** compile the arc register into a frozen typed-vector corpus (offline,
`scenario_authoring`); at runtime `game_director` owns a live arc-vector store whose lifecycle
FSMs step on the Key stream, a convergence **detector** runs at the Accounting boundary, a
subordinate **director** rations detector output into the existing 7-priority slate, and a
graduated NLG **realizer** renders the booked beats — **detect-THEN-schedule-THEN-render**, so
scheduling never starves detection (the inversion of C's subordination, per architecture-integrity
graft #5).

---

## 1. The six layers (bottom → top)

| # | Layer | Home | What it does | Closes / satisfies |
|---|---|---|---|---|
| L0 | **Compile** | `scenario_authoring` (offline) | register (~110 IDs) → frozen typed `arc_vector` corpus + PP-690 seed Keys | C1 bake; resolves authoring-vs-runtime seam |
| L1 | **Store + tick** | `game_director` | owns arc-vector store; steps lifecycle FSMs on Key stream + clocks each season | Q1 non-participation, Q2 world-acts, C5 one-ledger |
| L2 | **Detect** | `game_director` service | 8 COLLISION predicates (edge-once at Accounting) + cosine-similarity general correlation backbone + meaningfulness test | **ED-IN-0003**, Q3 |
| L3 | **Schedule/ration** | `game_director` (director, graduates articulation §7 D11) | beat budget over player_agency §4.3's 3-5 envelope; salience economy; watching/participating invariant; texture scheduling | Q4 pacing, C7 window guarantee |
| L4 | **Cast + inject** | casting resolver → `scene_slate` (demoted to candidate gen) | tie-graph over `participating_actors`; inject arc-tagged candidates into player_agency §4's 7 priorities | **ED-IN-0004** (structural), Q2 casting, Q1 participation |
| L5 | **Render** | NLG realizer (graduated PROPOSED) + articulation §3.1 table completion | fragment schema, offline bake, deterministic splice; fills articulation §5 socket | **ED-IN-0004** (render), C6 thread beats, Q4 present |

Holonic containment (C5, substrate contract): **OWNS** = arc-vector lifecycle state, actor
narrative weight, convergence windows, texture budgets, salience/tension ledger, the season
scene-queue on World scope (ORD-4). **READS** = clocks (`clock_registry_v30`), faction stats,
NPC state (incl. the NPC-scoped arc-state bucket `module_contracts.yaml:150`, which becomes a
**specialization the store reads**, not a rival owner).

---

## 2. The `arc_vector` data structure (L0 output — the load-bearing type)

From `dossier_register_formalizability` schema_proposal (register anatomy already has this shape,
`01_arc_corpus §a`: trigger → mechanical effects → Direction:):

```
arc_vector:
  id            # ARC-S07 etc.
  tier          # enum S|T|P|TE|BG-CV|COLLISION|NPC-ARC
  scope         # {faction, territories, mode}
  activity_mode # enum level_triggered | edge_triggered_once |
                #      edge_triggered_retryable | clock_escalation | convergence
  trigger:
    predicate:  # [{field: <clock|stat|npc_track|arc_state>.<path>, op, value}]
    resolves_via # dice_pool | deterministic_accounting | state_reader | manifest | null
    temporal_window   # [OPEN — Jordan]; default 4-season cosine (see fork 3)
  pressure_effects: # [{target, delta, cadence, condition}]  ±2/season cap
  payload:
    direction            # the causal sentence — the realizer's slot source
    participating_actors # the casting set (tie-graph intersection)
    stakes_tags          # gating | pricing | foreclosure | pattern_response
    ledger_cause         # every gate cites its cause (CI-checkable, Q2)
  lifecycle:
    state    # seeded → active → escalating → converging → resolved/dormant/abandoned
    terminal # bool
  cross_refs: [id]
  gaps: [{type, note, cites}]  # missing_clock | struck_mechanic | gm_judgment |
                               # dangling_id | stale_citation | open_number ...
```

Compile reality (dossier): **~45%** compile now (post trivial TC→CI / RS→MS rename), **~40%**
need one buildable field (chiefly the generalized `lifecycle.state` — the concrete form of
ED-IN-0003), **~15%** are GM-judgment-irreducible (ARC-P05, ARC-S29) and either get an authored
decision function or are declared non-firing in `gaps[]` (honesty ledger, buildability graft #4).

The compiled corpus IS the typed engine-params asset §5 of CLAUDE.md demands — it exports
directly to Godot (buildability judge: B's best property). It is a frozen asset, C1-clean.

---

## 3. The detector (L2 — closes ED-IN-0003)

Two-tier, both mandatory grafts:

1. **The 8 hand-authored COLLISION conjunctions** (from A / buildability graft #3): transcribe
   `arc_register_events.md §VI` COLLISION A–J to typed `convergence` arc_vectors whose
   `trigger.predicate` references OTHER vectors' `lifecycle.state` and shared `targets[]`.
   Evaluated **edge-triggered-once** over SETTLED state at the ACCOUNTING_BOUNDARY (architecture
   -integrity graft #2 — sidesteps ORD-3 mid-cascade non-determinism), deduped by a
   `convergence_fired_set`. Every non-firing marker EXPLICITLY DISCARDED with reason
   (`predicate_false`, logged) — total accounting.
2. **The general cosine-similarity backbone** (from C / all three judges): generalize
   `articulation_layer_v30 §3.1 trigger-9` (cosine similarity of `cascade_fidelity_history[-4:]`,
   4-season window, threshold ±0.40, sim-validated corr +0.937 at the Crown/Hafenmark pair) from
   faction-pairs to **arc-vector pairs**. This is the buildable path to the charter-Q3
   correlation-test generality the 8-marker whitelist lacks, and it SUPPLIES the temporal_window
   the COLLISION conjunctions never specify register-wide (dossier open-Q6).

**Meaningfulness test** (Q3, orthogonal to §3.2 stakes-loudness): generalize
`articulation_layer_v30 §3.2` significance — durability (moves a slow variable) × tie-proximity
(tie-graph distance to a `participating_actor`) × identity-touch (targets Belief/Conviction/Scar
/Coherence). This is the budget filter L3 applies; noise is backgrounded (re-promotable via the
§3.3 accumulator generalized to arcs), never silently dropped. Satisfies capstone #8.

---

## 4. The director as a SUBORDINATE service (L3 — the C-graft, contained)

C's Director Layer scored 76–78 but was the riskiest on C2 (its whole state IS the forbidden
narratological state) and C7 (over-orchestration → railroad). The synthesis keeps its Q4
strengths and drops its spine claim: the director is a **budget filter over the detector's
output**, not the thing that decides what a story is.

- **Beat budget / cut-scene rationing** (player-experience + buildability grafts): articulation
  today fires cut scenes "whenever triggers match" (§7, no rationing). The director allocates the
  3-5 scene-action envelope (`player_agency §4.3`) across Tier-2 cut scenes / slate scenes /
  texture. Bounded, a CEILING not a floor (C7 mitigation).
- **Watching-vs-participating invariant** (CI-checkable): per-arc `participated` vs `watched`
  counters; **a major arc cannot be all-watched before converging** (charter Q4 headline test).
  Stronger than B's structural-only lifecycle invariant.
- **Texture-between-scenes** = the demotion destination (immersion-audit gap neither A nor B
  touch): a demoted arc's beats become rumor/overheard/documents → Tier-1 ambient, **not
  nothing** (total accounting). Trails = the `causes[]` walk as in-world media (Q4).
- **Impulsion cadence** (Q2): director owns the diegetic-clock / forced-choice M-6 scheduling
  (`scale_transitions §4.3.2`).

C2 containment (absolute): the tension curve, salience ledger, and lifecycle labels NEVER
surface. Hard internal/external boundary + a **C2 literal-string lint applied to ALL
arc-lifecycle/salience state** (not just baked fragments) — demotion manifests only diegetically
(a summons becomes a rumor).

---

## 5. Casting + slate injection (L4 — closes ED-IN-0004 structurally + resolves scene_entered)

ONE tie-graph casting rule (Q2): when a live vector needs a scene, the resolver reads its
`payload.participating_actors` + tie-graph edges (Duty/Conviction alignment, Bonds/Knots,
lifepath/location, Standing, position). PC is cast if in `participating_actors` OR tie-adjacent;
"why-you" = the matched edge, surfaced diegetically. Rides `player_agency_v30 §4`'s 7 priorities
(scope+actors decide the step: 1 Crisis, 3 Duty, 4 Conviction, 5 NPC Outreach, 6 Territorial).
Same rule casts NPCs (co-protagonists, one ledger). The **factionless on-ramp** — the ONLY
architecture that structurally builds it (player-experience judge): a vector ladder
Conviction/Duty → TE-tier settlement arcs → Standing/Obligation proto-currency → recruitment-as
-arc. Acceptance test (a factionless PC gets playable seasons) met by construction.

**Position determines native story** (Q2): leaders — the `npc_behavior_v30 §5` concern/project
engine emits concern/project Keys; a vector with `scope.faction = leader's` subscribes (filter
`target = leader`) and injects reports-as-scenes / requests-for-ruling as NAMED actors with
wants (anti-spreadsheet). Members: `stakes_tags:[pricing]` duties with refusal costs under T-30
asymmetry.

**scene_entered ownership — RESOLVED (this lane's job, not a fork):** `game_director`
single-sources `mechanical.scene_entered/exited/skipped` (consistent with `scene_timer` already
consuming it `from:[game_director]`, `module_contracts.yaml:392-395`). `scene_slate` is **demoted
to a candidate/manifest generator**: it runs the 7-priority slate and emits `scene.*` CONTENT
Keys ONLY (`scene.dialogue/gift/insult/investigation_resolved/threat/witness`) — it loses
`mechanical.scene_entered`. A single-emitter conformance lint enforces it. (This subordination
touches three doc:null modules; the lane PROPOSES it, Jordan ratifies on merge per CLAUDE.md
ED-1094.)

---

## 6. Render (L5 — the render gap, ships FIRST as an independent stage)

Two edits, both architecture-neutral, both shippable WITHOUT the compiler (buildability graft #1
— the single best ships-first move):

1. **articulation §3.1 trigger-table completion** (the literal F-4 / ED-IN-0004 root at
   `articulation_layer_v30 L294-298`, the §6.4/ED-936 [ASSUMPTION]): add `scene.combat_resolved`
   + `scene.investigation_resolved` + the **four ED-681 Rendering-Crisis thread beats**
   (`threadwork_v30 §3.7` — C6 hard constraint) + the two new meta Keys. The §5 socket
   (`matches_trigger_ruleset` → `emit_cut_scene`) is untouched.
2. **NLG realizer graduation to PROPOSED** (`03_articulation_nlg_architecture.md` → PP-688 §11):
   fragment schema riding existing Key metadata only (`causes[]`, `targets[].role`,
   `symbolic_dimensions`, `significance`, `awareness` — no new Key fields), the coherence-tiers +
   solmund_voice §18 Certainty tables converted to runtime lookups, the **ARC-S07 worked
   example** (capstone #10), a C2 literal-string bake-audit lint, and explicit total-accounting
   DISCARD-with-reason logging. Bake key per `dossier_nlg_graduation`: `{key_type, significance
   _band, coherence_band, ts_band, spirit, certainty_register, focalizer}`. Content-economics
   dossier: ~350-450 authored units under orthogonal composition (feasible); the Certainty axis
   is a fork (§7 fork 6).

Anti-oatmeal #1 is STRUCTURAL here: because arc_vectors are DATA, two seeds diverge in named
actors / stakes / outcomes (capstone #11), verifiable because vectors are data not prose. ERA +
5-seed arc_test_batch are bake gates fed by arc-vector variety.

---

## 7. Staging — what ships first, what each stage unblocks

- **Stage 0 — Render-gap close (INDEPENDENT, ships first).** §6 above: articulation §3.1
  completion + NLG graduation + C2 lint. **Closes ED-IN-0004 + C6 at near-zero cost, rides
  existing homes, NOT gated behind the compiler.** Unblocks capstone #10, the whole Q4 render
  path. _Independently mergeable._
- **Stage 1 — Compile gate (`scenario_authoring`).** register → typed corpus; resolve the 3
  corpus defects (forks 1, 2 + TC→CI/RS→MS aliases). Ships the ~45% that compile now. **Unblocks
  everything downstream.**
- **Stage 2 — Store + tick (`game_director`).** arc-vector store + lifecycle stepper, read-only
  over clocks. Unblocks autonomous progression (Q1 non-participation, Q2).
- **Stage 3 — Detect (closes ED-IN-0003 fully).** 8 COLLISION predicates + cosine backbone +
  meaningfulness test; needs the generalized `lifecycle.state` field + the ratified
  temporal_window (fork 3). Unblocks Q3 emergence-vs-noise.
- **Stage 4 — Schedule + cast + inject (structural ED-IN-0004 + scene_entered resolution + ORD-4
  fix).** Director rations into player_agency §4; casting resolver; scene-queue relocated to
  World scope. Unblocks Q1 participation, Q2 casting, Q4 presence, C7 window guarantee.
- **Stage 5 — Texture + conformance + capstone.** Texture-between-scenes; the CI conformance
  suite (6 rules, each once in `tools/`); ARC-S07 end-to-end worked-season trace (all 12
  capstones).

Each stage is independently mergeable and rides an existing home (A's ratifiability discipline,
architecture-integrity graft #7). Stage 0 deliberately precedes the compile gate so value lands
before the biggest cost.

---

## 8. New Key types (total accounting — the one place I depart from B's "zero new types")

B's cleanest property was zero new Key types (capstone #9 "by design"). But the grafted detector
must render convergence AND feed the `causes[]` walk, which needs a carried event. I resolve this
in favor of **total accounting (every emitted Key has ≥1 declared consumer), not type-count
minimalism** — the actual substrate-contract invariant. Two new **Class B** types, both
consumer-closed, both C2-internal (labels never surface):

- **`meta.convergence_detected`** (Class B) — emitted by `game_director` L2. Consumers:
  `game_director` (booking / L3), `articulation` (Tier-2/3 render), chronicle (`causes[]` walk /
  Q3 queryable event). Registered in `key_type_registry_v30` with named consumers.
- **`meta.arc_state_changed`** (Class B) — emitted by `game_director` L1 on lifecycle transition.
  Consumers: `game_director` (CONSUMED-INTO-STATE), chronicle (retrospect), articulation
  (significance input). C2-internal.

All EXISTING touched Keys stay RENDERED / ACCUMULATED / CONSUMED-INTO-STATE / DISCARDED-with
-reason. `mechanical.scene_entered/exited/skipped` remain existing types (no new). This is fork 4
(default = add the 2).

---

## 9. Six transport directions (substrate contract)

- **up** — member→faction via Domain Echo (`sim/cross_scale/domain_echo.py`, ORD-3)
- **down** — faction pressure → member injection (§12.4 down-seam)
- **lateral** — NPC-ARC ↔ NPC-ARC COLLISION (the detector's primary read)
- **diagonal** — TE recruits NPC into a faction vector (`causes[]`-chain, §5.6)
- **forwards** — FSM lifecycle transitions (experienced as pressure/choices, C2-internal)
- **backwards** — chronicle `causes[]` walk (recognized as story)

Determinism: pure function of Key log + seed (PP-687 §6 V4), CONDITIONAL on ORD-3/ORD-4. The
ORD-4 fix (relocate the season scene-queue to World scope, `propagation_spec_v1 L114-118`) is
MANDATORY (architecture-integrity graft #3) — the only proposal closing the parallel-replay
hazard B inherits; load-bearing for the 5-seed narrative-regression gate.

---

## 10. Conformance suite (6 CI rules, each once in `tools/`)

1. **predicate-field-resolves** — catches ARC-T04 dangling ID + STRUCK Coup Counter.
2. **consumer-closure** — every emitted Key (incl. the 2 new) names ≥1 declaring consumer.
3. **total-accounting linter** — every touched Key rendered/accumulated/consumed/discarded-with
   -reason; no silent drop.
4. **C2 literal-string lint** — on ALL arc-lifecycle/salience state + baked fragments; no
   narratological label surfaces.
5. **scene_entered single-emitter** — only `game_director` emits it.
6. **watching/participating invariant** — no major arc all-watched before converging.
   (+ gate-cites-ledger_cause, replay-determinism as the same rules extend.)

---

## 11. Genuine Jordan forks (stated fork + default — never silently resolved)

1. **Coup Counter migration.** Remap numeric thresholds (2,3,40) 1:1 onto the Löwenritter
   Autonomy 4-stage track, OR re-author arc text against stage semantics. **Default: 1:1
   threshold remap** (cheaper; unblocks ARC-P03/S20/S56, NPC-ARC-BRA, ARC-T26, COLLISION-F).
   Blocks Stage 1. `[OPEN — Jordan]`
2. **ARC-T04 / Southernmost Ritual.** Author fresh, OR strike the two dangling cross-refs
   (`arc_register_territory.md:33`, `arc_register_events.md:38`). **Default: strike the stale
   cross-refs** (COLLISION-C becomes 7-of-8), defer authoring to a WR-lane arc. Needs a fresh
   lane-tagged ED (ED-WR-#### or ED-IN-####). `[OPEN — Jordan]`
3. **Convergence temporal_window.** same-season / same-Accounting / N-season lookback.
   **Default: 4-season cosine window (±0.40) for the general backbone; same-Accounting-boundary
   for the 8 hand-authored conjunctions.** Blocks Stage 3. `[OPEN — Jordan]`
4. **Two new Class B Key types vs zero-new-types purity.** Add `meta.convergence_detected` +
   `meta.arc_state_changed` (consumer-closed), OR keep detection fully internal and render via
   direct socket call. **Default: add the 2** (total-accounting, not type-count, is the
   invariant). `[OPEN — Jordan]`
5. **Lifecycle-state field ownership.** Class B extension of the npc_behavior arc-state bucket
   (`module_contracts.yaml:150`), OR a new `game_director`-owned store. **Default:
   game_director-owned store** (engine OWNS arc-vector state; NPC arc-state stays the
   specialization it reads). `[OPEN — Jordan]`
6. **Bake key includes Certainty?** NLG §8 omits Certainty from the frozen-pool key; charter Q4
   lists it. **Default: include it (charter authority)** — swings the bake ~5-6×
   (dossier_content_economics); fallback if bake cost prohibitive = Certainty as a runtime
   lexicon-swap, not a frozen-pool axis. `[OPEN — Jordan tuning-adjacent]`
7. **GM-judgment-irreducible ~15% (ARC-P05, ARC-S29).** Author a general decision function per
   judgment-arc (scripting-drift hazard, C5), OR declare them non-firing in `gaps[]` until
   authored. **Default: declare non-firing (honesty ledger)**; author case-by-case later. `[OPEN
   — Jordan]`

---

## 12. Grafts explicitly REJECTED / re-scoped

- **C's spine claim (director owns the loop).** REJECTED as spine; re-scoped to a subordinate
  budget filter (§4). Reason: C2/C7 risk + the detector must not be starved by scheduling
  (detect-THEN-schedule).
- **A as a standalone architecture.** REJECTED (fails factionless + intervention-window tests
  outright, player-experience judge). Its three edits (§3.1 completion, NLG graduation, marker
  predicates) are ABSORBED as Stage 0 + the detector's inner whitelist — kept, not discarded.
- **B's zero-new-types purity.** RE-SCOPED to total-accounting (§8, fork 4). Two consumer-closed
  types added.
