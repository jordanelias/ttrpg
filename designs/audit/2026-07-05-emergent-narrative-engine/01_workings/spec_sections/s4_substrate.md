# S4 — The Substrate Contract

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0069]
_Drafts the cross-cutting substrate contract for the Arc-Vector Engine (synthesis §§1–12).
Working tree only. Every mechanism cites a canon file §section or is tagged [UNGROUNDED].
Numbers tagged `[OPEN — Jordan tuning]` are calibration, not structure. C1 (no runtime LLM)
and C2 (no narratological surfacing) are absolute (`00_engine_charter.md:26-30`)._

This section discharges the charter's substrate-contract requirement
(`00_engine_charter.md:137-151`): states owned/read per scale; Keys-in (subscription, cadence,
filtering ladder, replay); Keys-out total accounting; the `module_contracts.yaml` candidate
entries; the new Key-type registry entries; the declared-vs-implemented edge table; the six
transport directions; and the CI conformance rules. It is the connective spec the six layers
(L0–L5, synthesis §1) share.

---

## S4.1 States owned / read, per scale (holonic containment)

C5 holonic guardrails (`holonic_container_doctrine_v1`, `00_engine_charter.md:36-37`) demand a
clean OWNS/READS boundary: the engine may not duplicate state another module owns, nor
genericize away an existing owner. The Arc-Vector Engine introduces exactly one owned store and
reads everything else.

| Scale (`scale_transitions_v30`) | Engine OWNS (writable) | Engine READS (never writes) |
|---|---|---|
| **scene** | `mechanical.scene_entered/exited/skipped` emission (single-sourced — S4.3, S4.7 R5); the season scene-queue relocated to World scope (ORD-4, `propagation_spec_v1.md` O.7) | `scene.*` content Keys from `scene_slate`; venue resolvers (contest/combat/thread/fieldwork/mass-battle/settlement) — C3: books venues, never resolves (`00_engine_charter.md:32-33`) |
| **personal** | arc-vector `lifecycle.state`, actor narrative weight, per-arc `participated`/`watched` counters, salience/tension ledger (C2-internal — never surfaces) | Convictions/Beliefs/Scars/Coherence ledger (P-04 no hidden meter, `00_engine_charter.md:52-53`); `npc_memory` store (`state_reader`); Bonds/Knots |
| **territory / settlement** | texture budgets; convergence windows | `clock_registry_v30` clocks; faction stats; settlement Mandate |
| **peninsula / world** | the compiled `arc_vector` corpus (frozen asset, L0); convergence dedup ledger | Domain Echo aggregates (`sim/cross_scale/domain_echo.py`, ORD-3); `national_event_modifier` Key-ledger query (`propagation_spec_v1.md:178`) |

**The one specialization the store READS, not owns:** the NPC-scoped `arc state` bucket
(`module_contracts.yaml:150`, `bucket: clock`, scoped only to `npc_behavior` T-23 NPC arcs). The
generalized per-arc `lifecycle.state` field (the concrete form of ED-IN-0003,
`dossier_register_formalizability` finding 4.1) is a NEW `game_director`-owned store; the existing
NPC bucket becomes a specialization the store reads for NPC-tier arcs. This is **fork 5** (synthesis
§11.5): default = `game_director`-owned store. `[OPEN — Jordan]`

---

## S4.2 Keys-in

### S4.2.1 Subscription model

`game_director` is a **universal reader of the full Key stream**, mirroring `articulation_layer`'s
declared subscription (`{type: "*", from: engine}`, `module_contracts.yaml:768`, sourced from
`key_substrate_v30 §8.7`). It does not subscribe per-type: the arc-vector store's lifecycle FSMs
step on whatever Keys settle, and per-arc relevance is decided by each vector's `trigger.predicate`
matching against settled Key `targets[]`/`causes[]`, not by a subscription filter. This is the only
subscription shape that satisfies Q1's "non-participation is also an input" — an FSM must be able to
step on the *absence* of a player Key, which a per-type subscription cannot express
(`00_engine_charter.md:49-50`).

Two narrow, filtered subscriptions ride on top for the casting layer (L4):
- **Leader beats:** a vector with `scope.faction = leader's` subscribes to `npc_behavior_v30 §5`
  concern/project Keys filtered to `target = leader` — named actors with wants, not report rows
  (anti-spreadsheet, `00_engine_charter.md:64`).
- **Member duties:** `stakes_tags:[pricing]` vectors read `npc_memory` (`state_reader`) for the
  refusal-cost ledger.

### S4.2.2 Cadence vs `propagation_spec_v1` ordering

The engine has exactly two cadences, both pinned to the tick structure of `propagation_spec_v1.md`:

1. **Per-Key (L1 lifecycle step).** Arc-vector FSMs advance as Keys settle into the log. Ordering
   inherits the substrate's `(season_index, sub_step_index)` total order (SSI-1..4,
   `propagation_spec_v1.md` O.4). The engine assigns nothing — `sub_step_index` is assigned by
   `KEY_LOG.append`, never by the emitter (SSI-1). The engine MUST NOT read `cascade_depth` (runtime
   scheduler state, not a Key field, `propagation_spec_v1.md:301`).
2. **Per-season (L2 detect / L3 ration).** The convergence detector and the director budget run
   **once, at the ACCOUNTING boundary**, over SETTLED state — after all scene resolution and
   Domain-Echo up-consequences (`propagation_spec_v1.md` Theorem A, `:297`). Running at ACCOUNTING
   (not mid-ACTION) is what sidesteps ORD-3 mid-cascade nondeterminism on the READ side (synthesis
   §3, architecture-integrity graft #2).

**Determinism preconditions carried from `propagation_spec_v1`.** Replay (V4) is a pure function of
the Key log + seed **CONDITIONAL on** ORD-3 (`compute_observers` order-preserving, O.6) and ORD-4
(scene-queue on World scope, O.7). The ORD-4 fix — relocate the season scene-queue from
`scene_slate._queue` module-global to World scope (`propagation_spec_v1.md:114-118`) — is MANDATORY
here: parallel batch runs of the 5-seed narrative-regression gate (Q4 anti-oatmeal item 3) share the
module-global queue otherwise, and the whole regression is a parallel batch. Until ORD-4 lands the
determinism guarantee holds only under sequential execution (`propagation_spec_v1.md:118`).

**Gate-0 / engine_clock precondition (corrects synthesis §7's "every stage rides an existing home").**
The per-season cadence rides the temporal spine, and the temporal spine is **not authored**:
`engine_clock` is `doc:null` pending ED-1051, candidate home `propagation_spec_v1.md §O.2`
(`strategic_judgments.md:24-28`, `02_interdependency_map.md:43`). Stage 2 (clock-stepping the FSMs
"each season") and Stage 3 (Accounting-boundary detection) are therefore **gated behind Gate-0 /
ED-1051** — J-2 froze the critical path here ("stop deepening… until Gate-0… engine_clock authoring
is executed", `strategic_judgments.md:28`). Stages 0 and 1 (render-gap close, offline compile) have
NO clock dependency and may precede it. This is an explicit ordering constraint on the staging plan,
not a soft note.

### S4.2.3 Filtering ladder (trigger → significance → accumulate → discard)

Per `00_engine_charter.md:143` the Keys-in path is a four-rung ladder; every rung has a total
accounting fate (S4.3):

1. **Trigger** — does any live vector's `trigger.predicate` match this settled Key's
   `targets[]`/`causes[]`? No match → the Key is still ACCUMULATED by the salience economy (rung 3)
   or DISCARDED-with-reason; never silently dropped.
2. **Significance / meaningfulness** — the meaningfulness test (Q3, orthogonal to §3.2
   stakes-loudness, `00_engine_charter.md:83-86`): `durability × tie-proximity × identity-touch`,
   generalizing `articulation_layer_v30 §3.2` significance from Keys to arcs. A matched Key below the
   meaningfulness floor is backgrounded (rung 3), re-promotable — never dropped.
3. **Accumulate** — the `articulation_layer_v30 §3.3` accumulator generalized to arcs: sub-threshold
   Keys build per-arc narrative weight; a later routine Key can cross the threshold (background's
   dignity, `00_engine_charter.md:96`).
4. **Discard** — explicit, with a logged reason string (`predicate_false`, `below_meaningfulness`,
   `noise_backgrounded`). This IS the total-accounting DISCARD fate; false positives cost player
   trust (`00_engine_charter.md:89`), so the reason is auditable.

**Arithmetic-determinism rules for rungs 1–2 (structure, not tuning — ruled regardless of the
`[OPEN — Jordan]` threshold values).** Two float comparisons cross the replay boundary and, left
naïve, break V4 and Python↔GDScript key-log parity (the ED-1050 `adef_threshold` class,
`CLAUDE.md §6`):

- **Cosine convergence backbone** (L2b, generalizing `articulation_layer_v30:99-101`
  `if abs(sim) > 0.40`). Generalizing from ~5 faction-pairs to ~110 arc-vectors is O(N²) boundary
  comparisons; the +0.937 validation was ONE faction pair over 30 seasons
  (`articulation_layer_v30:112`), not the arc-pair regime. Float summation is non-associative, so a
  marginal pair flips fired/not-fired on term order. **Rule:** quantize the cosine numerator/
  denominator to a fixed integer grid and compare integers, OR canonicalize a single summation order
  (sort contributing terms by `actor_id`) with a published epsilon-band and a conservative-tie rule
  (ties resolve to *not fired*). Pin identical fixed-point arithmetic in the GDScript port and add it
  to the key-log parity harness. The value `0.40` is `[OPEN — Jordan tuning]`; the determinism of the
  comparison is not. _(Applies adversarial MAJOR: ±0.40 boundary/cross-oracle nondeterminism.)_
- **Meaningfulness product** (`durability × tie-proximity × identity-touch`). A float product with a
  threshold plus an order-dependent graph-distance term. **Rule:** quantize each factor to a fixed
  grid, take the integer product, compare integers; make tie-graph distance deterministic (BFS over
  an `actor_id`-sorted adjacency, ties by `actor_id`).

### S4.2.4 Replay determinism (V4)

`save = (initial_state, KEY_LOG)`; replay re-executes `on_key_emitted()` over the log; V4 = same
seed + choices → identical KEY_LOG hash (`propagation_spec_v1.md` O.8, `00_engine_charter.md:143`).
The engine adds three replay-critical containers; all three MUST be order-preserving:

- **Convergence dedup — order-preserving, NOT a `set()`.** L2a dedups fired convergences. A bare
  `set()` here is a **second live ORD-2 violation** (`propagation_spec_v1.md` O.3 ORD-2 forbids any
  `set()` gating emission/mutation order; O.6 exists solely because `compute_observers`' bare `set()`
  was one). "Conditional on ORD-3" covers only the READ side; the detector's own EMIT order is
  separate. **Rule:** dedup via a dict keyed by a total order —
  `(conjunction_id, sorted(participating_actor_ids), season_index)` — and sort detected convergences
  by that key before the emit loop. Conformance rule R7 (S4.7) asserts no `set()` gates convergence
  emission order. _(Applies adversarial MAJOR: `convergence_fired_set` is a second ORD-2 violation.)_
- **Rationing / Top-N tiebreak — mandatory total order.** L3 rations into the 3–5 scene-action
  envelope (`player_agency_v30 §4.3`) via a Top-N selection generalizing `articulation_layer_v30
  §3.3`/`§4.3`. Integer salience over ~110 arcs makes marginal-slot **ties the common case**; no
  cited source specifies a tiebreak, so an unstable sort or dict/set-seeded selection emits a
  different scene set → V4 fails, precisely on the CEILING selection where C7 demands determinism.
  **Rule:** every rationing/Top-N selection sorts by `(salience DESC, tier_rank ASC, arc_vector.id
  ASC)` — `id` is unique so the order is total; unstable sort and set/dict-seeded selection are
  forbidden. Applies equally to the `§4.3` chronicle Top-N and the `§3.3` notable-individuals Top-N.
  _(Applies adversarial MAJOR: Top-N tiebreak absent.)_
- **Realizer fragment selection — pure or dedicated sub-stream.** Q4 + `propagation_spec_v1.md` O.8
  require "same rendered text"; capstone #11 wants two-seed divergence — both need fragment selection
  to be a pure function of seeded state. RNG-MODEL-COLLISION (`propagation_spec_v1.md` O.5, three
  unreconciled RNG models) leaves "which stream does the realizer draw from" unanswered. **Rule:**
  realizer fragment selection is EITHER zero-randomness (a pure function of Key metadata + focalizer
  + register band — the preferred form, since `dossier_nlg_graduation` specifies deterministic
  exact-match lookup) OR draws from a dedicated render sub-stream seeded from
  `(campaign_seed, key.id)` so render never perturbs simulation draws. String-hash / dict-iteration /
  wall-clock selection is forbidden. Disposing RNG-MODEL-COLLISION is a **Stage-0 render-lane
  precondition** (the chronicle renders at the annual boundary; if it drew from `World.rng` it would
  perturb downstream draws, RNG-3 isolation being unspecified, `propagation_spec_v1.md:103`).
  _(Applies adversarial MAJOR: realizer fragment-selection source undefined.)_

---

## S4.3 Keys-out — the TOTAL ACCOUNTING invariant

`00_engine_charter.md:143-146`: every Key the engine touches has exactly one of four fates, nothing
silent; every emitted Key is registered in `key_type_registry_v30` with ≥1 declared consumer whose
`consumes:` names it; `targets[]`/`causes[]` populated.

| Fate | Meaning | Where logged |
|---|---|---|
| **RENDERED** | surfaced as Tier-2 cut scene / Tier-3 chronicle / Tier-1 texture (diegetic only, C2) | realizer output (L5) |
| **ACCUMULATED** | added to per-arc narrative weight (`§3.3` accumulator, re-promotable) | salience ledger (C2-internal) |
| **CONSUMED-INTO-STATE** | stepped an FSM / crossed a convergence predicate; no external surface | `lifecycle.state` transition |
| **DISCARDED-with-reason** | matched no live vector and below meaningfulness | logged reason string (S4.2.3 rung 4) |

Two accounting rules are load-bearing and are NOT satisfied by the four-fate ledger alone:

**Foreclosure is mandatory-render, not merely accounted (C7).** `activity_mode` includes
`clock_escalation`/`level_triggered` with ±2/season deltas (synthesis §2); a passive clock (ARC-S07
`Loyalty ≤ 2 → Mandate −2`, `01_arc_corpus.md:41-42`) can cross a foreclosure threshold with no arc
event. But C7 requires foreclosure "via arc events only… surfaced afterward in chronicle, never
silent" (`00_engine_charter.md:41,77-78`), and a foreclosure CONSUMED-INTO-STATE is accounted yet
never rendered. **Two rules:** (a) a `stakes_tags:[foreclosure]` transition may fire ONLY from
`edge_triggered_once`/`edge_triggered_retryable`/`convergence` — never `clock_escalation`/
`level_triggered`; a foreclosing clock crossing must first raise an edge-triggered arc event. (b)
Every foreclosure transition MUST emit a Tier-3 chronicle beat — a **positive surfacing check**,
distinct from discard-with-reason logging. Conformance rule R8 (S4.7). _(Applies adversarial MAJOR:
foreclosure can fire silently via passive threshold-crossing.)_

**Convergence combined-effect provenance (anti-fabrication).** `arc_register_events.md §VI` defines a
Convergence Marker's combined pressure as "not predictable from the constituent vectors" (e.g.
COLLISION-C `RS +8, IP +2, TC +2`, `:39`) — an **authored** quantity. The general cosine backbone
(L2b) detects convergences OUTSIDE the 8 hand-authored conjunctions; wiring those to synthesize a
combined effect fabricates unauthored deltas (`CLAUDE.md §5/§7`, leaky gate). **Rule:** a
cosine-detected convergence outside the register-authored set is **RENDER/CHRONICLE-ONLY** — zero
`pressure_effects[]`, it feeds `meta.convergence_detected` for the `causes[]` walk and realizer, but
mutates no clock/stat. Mechanical combined-pressure exists ONLY for register-authored `convergence`
vectors. Conformance rule R9: any `convergence` vector with non-empty `pressure_effects[]` must trace
each delta to a register line. This keeps the mechanically-real convergences from being either a
fabrication surface or a hardcoded whitelist of 8 (holonic doctrine §2 scripting drift). _(Applies
adversarial MAJOR: convergence-EFFECT seam.)_

---

## S4.4 `module_contracts.yaml` candidate entries (verbatim-ready)

These replace the five `status: extracted`, `doc: null` stubs in the scene-orchestration cluster
(`03_prior_art_and_module_homes.md (c)`). Field shape follows the existing file convention. All are
PROPOSED; Jordan's review-and-merge ratifies (ED-1094) — **except** the two held-back hard calls
called out in S4.8, which the PR body must flag as loud, not bundled.

### game_director (RUNTIME spine — L1/L2/L3/L4 hookpoint)

```yaml
  - module: game_director
    registry_system: "game_director"
    doc: designs/audit/2026-07-05-emergent-narrative-engine/spec_sections/...  # NEW arc-vector engine spec (this effort); flips doc:null (module_contracts.yaml:368-385)
    scales: [scene, personal, territory, peninsula]   # was [scene]; owns arc state across scales
    resolver: manifest   # books venues, never owns resolution (C3); orchestrator, not state_reader
    consumes:
      - {type: "*", from: engine}   # universal reader of the full Key stream (mirrors articulation_layer, module_contracts.yaml:768); reads clocks/faction-stats/NPC-tracks/territory at the ACCOUNTING boundary
    emits:
      - {type: "mechanical.scene_entered", terminal: false}   # RE-OWNED single-source (was conflict with scene_slate); see substrate §8.5 edit in S4.8
      - {type: "mechanical.scene_exited", terminal: false}
      - {type: "mechanical.scene_skipped", terminal: false}
      - {type: "meta.convergence_detected", terminal: false}   # NEW Class B (L2 detector); see S4.5 registry entry
      - {type: "meta.arc_state_changed", terminal: false}   # NEW Class B (L1 FSM transition); see S4.5 registry entry
    state:
      - {name: "arc lifecycle state", bucket: clock, writable: true}   # generalized per-arc lifecycle.state (ED-IN-0003 concrete form); reads npc_behavior "arc state" (module_contracts.yaml:150) as a specialization
      - {name: "actor narrative weight", bucket: track, writable: true}
      - {name: "salience/tension ledger", bucket: track, writable: true}   # C2-INTERNAL — never surfaces (S4.7 R4)
      - {name: "texture budgets", bucket: track, writable: true}
      - {name: "convergence dedup", bucket: track, writable: true}   # order-preserving, NOT set() (S4.2.4, S4.7 R7)
      - {name: "season scene-queue", bucket: track, writable: true}   # ORD-4: on World scope, not module-global (propagation_spec_v1 O.7)
    transitions: []   # per-arc FSMs are data (compiled corpus), not a fixed module FSM
    loops:
      - {open: true}   # detect->ration->cast->scene->outcome-Key re-enters causes[]; bounded per-tick by Theorem A (propagation_spec_v1:297) + EMISSIONS_PER_TICK_MAX
    status: proposed
    sources:
      - "designs/audit/2026-07-05-emergent-narrative-engine/ (this effort)"
      - "key_substrate_v30 §8.5 [edit required — S4.8]"
```

### scenario_authoring (OFFLINE compile home — L0)

```yaml
  - module: scenario_authoring
    registry_system: "scenario_authoring"
    doc: designs/audit/2026-07-05-emergent-narrative-engine/spec_sections/...  # NEW compile spec + references/arcs compiled corpus; flips doc:null (module_contracts.yaml:744-760)
    scales: [peninsula]
    resolver: manifest   # authoring-time compiler; seeds runtime, owns no runtime resolution
    consumes: []   # references/arcs/*.md are an authoring-time SOURCE, not a Key (resolves the "authoring-time vs runtime" [OPEN] seam: compile is authoring-time, seeds runtime, the arc_vector schema IS the seam)
    emits:
      - {type: "env.crisis", terminal: false}   # EXISTING seed Keys (PP-690), frozen at bake
      - {type: "env.disaster", terminal: false}
    state:
      - {name: "compiled arc_vector corpus", bucket: track, writable: false}   # FROZEN data asset — the typed engine-params analogue CLAUDE.md §5 wants; C1-clean
    transitions: []
    loops: []
    status: proposed
    sources:
      - "designs/audit/2026-07-05-emergent-narrative-engine/ (this effort)"
      - "dossier_register_formalizability schema_proposal"
```

### scene_slate (DEMOTED to candidate/manifest generator — L4)

```yaml
  - module: scene_slate
    registry_system: "scene_slate"
    doc: designs/audit/2026-07-05-emergent-narrative-engine/spec_sections/...  # NEW standalone spec + player_agency_v30 §4.2 as generation spec; flips doc:null (module_contracts.yaml:342-366)
    scales: [scene]
    resolver: manifest   # deterministic 7-priority slate generation (settlement_layer §4.1; player_agency §4.2)
    consumes:
      - {type: "meta.arc_state_changed", from: [game_director]}   # director injection requests ride this + convergence_detected
      - {type: "meta.convergence_detected", from: [game_director]}
    emits:
      # mechanical.scene_entered REMOVED — re-owned to game_director (conflict resolution, S4.8)
      - {type: "scene.combat_strike", terminal: false}
      - {type: "scene.dialogue", terminal: false}
      - {type: "scene.gift", terminal: false}
      - {type: "scene.insult", terminal: false}
      - {type: "scene.investigation_resolved", terminal: false}
      - {type: "scene.threat", terminal: false}
      - {type: "scene.witness", terminal: false}
    state: []
    transitions: []
    loops: []
    status: proposed
    sources:
      - "player_agency_v30 §4.2 [READ: 2026-07-05]"
      - "settlement_layer_v30 §4.1"
      - "key_substrate_v30 §8.5 [edit required — S4.8: emission re-attributed to game_director]"
```

### articulation_layer (EXTENDED) + NLG realizer (GRADUATED) — L5

```yaml
  - module: articulation_layer
    registry_system: "articulation"
    doc: designs/articulation/articulation_layer_v30.md   # §3.1 trigger-table EDIT + graduate 03_articulation_nlg_architecture.md realizer to PROPOSED (PP-688 §11)
    scales: [personal, scene, provincial]
    resolver: deterministic_accounting   # significance accounting + deterministic template splice (C1 — no runtime LLM)
    consumes:
      - {type: "*", from: engine}   # universal reader (unchanged, module_contracts.yaml:768)
      - {type: "meta.convergence_detected", from: [game_director]}   # NEW render trigger
      - {type: "meta.arc_state_changed", from: [game_director]}   # NEW significance input
      - {type: "scene.combat_resolved", from: [personal_combat]}   # §3.1 completion (was untriggered — ED-IN-0004)
      - {type: "scene.investigation_resolved", from: [scene_slate, faction_politics]}
      # + the 4 ED-681 Rendering-Crisis thread beats (threadwork_v30 §3.7 — C6)
    emits: []   # Tier-2/3 render is output, not a Key emission (fired-Key metadata only: causes[], targets[].role, symbolic_dimensions, significance, awareness)
    state: []
    transitions: []
    loops: []
    status: proposed   # was extracted; §3.1 edit + realizer graduation
    sources:
      - "articulation_layer_v30 §3.1/§3.2/§6 [READ: 2026-07-05]"
      - "03_articulation_nlg_architecture.md (graduated)"
      - "dossier_nlg_graduation"
```

### npc_memory / scene_timer — UNCHANGED (retain `doc: null`)

`npc_memory` (`module_contracts.yaml:177-196`) stays a `state_reader` feeding the concern queue for
Q2 leader beats. `scene_timer` (`module_contracts.yaml:387-404`) stays an observability sidecar
OUTSIDE the Key log; its `consumes: [{type: mechanical.scene_entered, from: [game_director]}, …]` is
**already** attributed to `game_director` — which is the alignment evidence for the scene_entered
resolution, but is NOT by itself sufficient (S4.8). No edit to either.

**ED-1009 (open — multi-emitter attribution of `scene.dialogue` / `state.belief_revised`): DEFERRED
with a pointer, not touched.** ED-1009 flags the exact pair this section's contracts brush against —
`scene_slate` here `emits: scene.dialogue` (S4.4), and `articulation` here consumes `belief_revised`
as a significance input (the render trigger cluster, Q4.6.4/Q4.8). S4.8 resolves the **sibling**
`mechanical.scene_entered` multi-emitter conflict with a loud fork; the `scene.dialogue` /
`belief_revised` attribution is **structurally analogous** but is a distinct open item. **This
design does NOT re-attribute `scene.dialogue` or `belief_revised`** — it leaves their existing
emitter/consumer edges untouched and adds no new emitter for either. **Recommended disposition:
defer-with-pointer** — flag ED-1009 as the governing open item for that pair, apply the *same
single-emitter discipline* the scene_entered resolution establishes (S4.8, R5) if/when ED-1009 is
taken up, but do not fold ED-1009 into this PR. Carried in S4.11.

---

## S4.5 New Key-type registry entries (verbatim-ready)

Two NEW **Class B** types (extension policy: adding types is Class B,
`key_type_registry_v30.md:10`), both consumer-closed, both C2-internal (the label never surfaces —
S4.7 R4). This is the one departure from Architecture B's zero-new-types purity, resolved toward
**total accounting is the invariant, not type-count** (synthesis §8; fork 4, default = add the two).
Format follows `key_type_registry_v30.md §1`.

```yaml
### meta.convergence_detected  (add to §8 Family: system_meta)

description: Internal marker that two or more arc-vectors converged into a story at the Accounting boundary — an authored COLLISION conjunction (register-backed pressure) OR a cosine-detected correlation (RENDER/CHRONICLE-ONLY, zero pressure — S4.3). Label NEVER surfaces to the player (C2). Payload-only; no state mutation on emission.
required_payload_fields:
  - convergence_id            # conjunction_id for register-authored; deterministic hash(sorted actor_ids, season_index) for cosine-detected
  - constituent_vectors       # [arc_vector.id] — the converging arcs
  - participating_actors      # [actor_id] — the casting set (tie-graph source, L4)
  - provenance                # register_authored | cosine_detected  (gates whether pressure_effects apply — S4.3, R9)
  - season_n                  # int
optional_payload_fields:
  - similarity                # cosine value (cosine_detected only; quantized per S4.2.3)
  - temporal_window           # seasons spanned (default 4-season backbone; fork 3)
default_scale_signature: [territory, peninsula]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [game_director]
consuming_systems: [game_director, articulation (Tier-2 render), scene_slate, articulation (Tier-3 chronicle)]
class: B
declared_by: designs/audit/2026-07-05-emergent-narrative-engine (this effort; closes ED-IN-0003 render side)
notes:
  - game_director consumes for L3 booking; articulation for Tier-2 render AND the Tier-3 chronicle causes[] walk (Q3 queryable event). "chronicle" is NOT a module — Tier-3 chronicle is an articulation function (articulation_layer_v30 §4); consumer is articulation, not a separate `chronicle` module.
  - Emission order is deterministic — deduped via an order-preserving container keyed by (convergence_id), sorted before emit (S4.2.4, R7). No set() gates emission order (ORD-2).
  - cosine_detected members carry NO pressure_effects (S4.3 provenance rule, R9).
```

```yaml
### meta.arc_state_changed  (add to §8 Family: system_meta)

description: Emitted on an arc-vector lifecycle FSM transition (seeded -> active -> escalating -> converging -> resolved/dormant/abandoned). CONSUMED-INTO-STATE by game_director; retrospect input for the articulation Tier-3 chronicle; significance input for articulation Tier-2. Label NEVER surfaces (C2). Foreclosure transitions additionally trigger a mandatory Tier-3 chronicle beat (S4.3, R8).
required_payload_fields:
  - arc_vector_id             # ARC-S07 etc.
  - from_state                # prior lifecycle.state
  - to_state                  # new lifecycle.state
  - stakes_tags               # [gating | pricing | foreclosure | pattern_response]  — drives R8/R10 checks
  - ledger_cause              # the cited PP/ED or clock/stat crossing (Q2: every gate cites its cause)
  - season_n                  # int
optional_payload_fields:
  - participating_actors      # [actor_id]
  - terminal                  # bool — true on resolved/dormant/abandoned
default_scale_signature: [personal, territory, peninsula]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [game_director]
consuming_systems: [game_director, articulation (Tier-2 render), scene_slate, articulation (Tier-3 chronicle)]
class: B
declared_by: designs/audit/2026-07-05-emergent-narrative-engine (this effort)
notes:
  - "chronicle" is NOT a module — Tier-3 chronicle is an articulation function (articulation_layer_v30 §4); the retrospect consumer is articulation, not a separate `chronicle` module.
  - CONSUMED-INTO-STATE fate for game_director's own store; the emitted Key is the retrospect/render record, not the store itself.
  - A stakes_tags:[foreclosure] transition MUST also produce a Tier-3 chronicle beat (positive surfacing, R8) and may originate ONLY from edge_triggered_once/retryable/convergence (R8a).
```

**No other new types.** `mechanical.scene_entered/exited/skipped` stay EXISTING (re-owned, not new,
S4.4). `scene.combat_resolved`/`scene.investigation_resolved` and the 4 ED-681 thread beats are
EXISTING Keys given render triggers (S4.4 articulation), not new types.

---

## S4.6 Declared-vs-implemented edge table (the new engine)

Every declared consumer/producer edge, with implementation status. "declared" = named in a
`consumes:`/`emits:`; "implemented" = a resolver/handler actually processes it. This IS the total-
accounting cross-check the charter requires for the engine itself (`00_engine_charter.md:146`).

| # | Edge (producer → Key → consumer) | Declared | Implemented | Note / ordering |
|---|---|---|---|---|
| E1 | `game_director` → `meta.convergence_detected` → `articulation` | ✓ (S4.4/S4.5) | Stage 3 (detect) + Stage 5 (render) | Emit order order-preserving (R7); ACCOUNTING cadence |
| E2 | `game_director` → `meta.convergence_detected` → `articulation` (Tier-3 chronicle) | ✓ | Stage 5 | `causes[]` walk (backwards direction); Tier-3 chronicle is an articulation function, not a separate `chronicle` module |
| E3 | `game_director` → `meta.arc_state_changed` → `game_director` | ✓ | Stage 2 | CONSUMED-INTO-STATE self-edge; not a loop hazard (no re-emit) |
| E4 | `game_director` → `meta.arc_state_changed` → `articulation` | ✓ | Stage 5 | significance input |
| E5 | `game_director` → `mechanical.scene_entered` → `scene_timer` | ✓ (already, `module_contracts.yaml:392-395`) | EXISTS | single-emitter (R5); §8.5 edit pending (S4.8) |
| E6 | `game_director` → `mechanical.scene_entered` → `articulation` | ✓ | EXISTS | Tier-3 pacing analysis |
| E7 | `scene_slate` → `scene.*` content → ordinary engines | ✓ (`module_contracts.yaml:349-357`) | EXISTS | C3: venues resolve, engine only books |
| E8 | `game_director` → `meta.arc_state_changed` → `scene_slate` | ✓ (injection request) | Stage 4 | director→slate down-injection (L4) |
| E9 | `personal_combat` → `scene.combat_resolved` → `articulation` | ✓ (`key_type_registry_v30.md:724-741`) | **DECLARED-NOT-TRIGGERED** | the ED-IN-0004 gap; Stage 0 adds the §3.1 trigger |
| E10 | `scene_slate`/`faction_politics` → `scene.investigation_resolved` → `articulation` | ✓ (`key_type_registry_v30.md:705-723`) | **DECLARED-NOT-TRIGGERED** | Stage 0 §3.1 completion |
| E11 | thread system → 4 ED-681 Rendering-Crisis beats → `articulation` | partial (`threadwork_v30 §3.7`) | **DECLARED-NOT-TRIGGERED** | C6 hard constraint; Stage 0 |
| E12 | `npc_behavior §5` → concern/project → `game_director` (filtered `target=leader`) | ✓ (S4.2.1) | Stage 4 | leader beats; anti-spreadsheet |
| E13 | `env.crisis`/`env.disaster` (scenario_authoring seed) → arc store | ✓ (`module_contracts.yaml:757-758`) | Stage 1 | offline-baked seed Keys |

E9–E11 are the live ED-IN-0004 render gap: the Keys exist and declare `articulation` as consumer,
but no §3.1 trigger fires the render. Stage 0 closes all three at near-zero cost (synthesis §6),
independent of the compiler.

---

## S4.7 Six transport directions (with ordering / determinism notes)

All six directions are used (synthesis §9); each carries an ordering note pinned to
`propagation_spec_v1`.

| Direction | Carrier | Ordering / determinism note |
|---|---|---|
| **up** | member → faction via Domain Echo (`sim/cross_scale/domain_echo.py`) | ORD-3 observer order; echo `sub_step_index` assigned at append (`propagation_spec_v1.md:188`); table lookup, zero RNG |
| **down** | faction pressure → member injection (integration `§12.4` down-seam) | ONE Key with N `targets[]`, not N Keys (`propagation_spec_v1.md:245`) — one emission at one `cascade_depth` |
| **lateral** | NPC-ARC ↔ NPC-ARC COLLISION (detector's primary read) | evaluated at ACCOUNTING over settled state; dedup order-preserving (R7) |
| **diagonal** | TE recruits NPC into a faction vector (`causes[]`-chain) | authored-provenance `causes[]` edge (distinct from runtime re-entrancy edge, `propagation_spec_v1.md:358`) |
| **forwards** | FSM lifecycle transitions (experienced as pressure/choices) | C2-internal; emits `meta.arc_state_changed`; deterministic FSM step |
| **backwards** | chronicle `causes[]` walk (recognized as story) | read-only; renders at annual boundary from a dedicated render sub-stream (S4.2.4) so it perturbs no simulation draw |

Determinism overall: pure function of Key log + seed (V4), CONDITIONAL on ORD-3/ORD-4 landing and on
the three engine-added containers being order-preserving (S4.2.4). The ORD-4 fix is MANDATORY (S4.2.2).

---

## S4.8 The scene_entered resolution — restored as an explicit fork (NOT silently resolved)

The charter lists `mechanical.scene_entered` ownership as `[OPEN — Jordan]`
(`00_engine_charter.md:147-148`). Relabelling it "RESOLVED — not a fork" (synthesis §5) would be
exactly the hard-call-bundled-into-routine-work failure `CLAUDE.md §2` (ED-1094) exists to prevent.
This section therefore **restores it as a fork with a recommended default**, and the PR body must
flag it as a held-back hard call:

- **Recommended default:** `game_director` single-sources `mechanical.scene_entered/exited/skipped`;
  `scene_slate` is demoted to a content-Key generator. Evidence: `scene_timer` **already** consumes
  scene_entered `from: [game_director]` (`module_contracts.yaml:392-395`), and the registry entry
  already lists `emitting_systems: [game_director]` (`key_type_registry_v30.md:383`).
- **The contradiction the default must resolve in the SAME PR:** `key_substrate_v30 §8.5` L510 says
  verbatim "scene_slate: scene activation emits mechanical.scene_entered" — the SAME source
  `scene_slate`'s registry emit cites. The resolution is consistent with the registry but
  **inconsistent with canonical substrate §8.5**. Therefore the deliverable MUST include an explicit
  edit to `key_substrate_v30 §8.5` L510 (re-attribute emission to `game_director`, OR split
  manifest-vs-lifecycle Key), shipped in the same PR. **Until §8.5 is edited it remains a fork, not a
  resolution.** _(Applies adversarial MAJOR: scene_entered inconsistent with substrate §8.5; and the
  MAJOR that the charter's `[OPEN — Jordan]` was silently overridden.)_

`[OPEN — Jordan]` — default = `game_director` single-source + the §8.5 edit above.

---

## S4.9 CI conformance rules (each ONE rule, `tools/` home named)

Per `00_engine_charter.md:150-151`: a CI-checkable rule per invariant, each living once in `tools/`
(the "every rule lives once" invariant, `CLAUDE.md §8`). Ten rules; the first six are the synthesis
§10 suite, R7–R10 are the adversarial-hardening additions.

> **Numbering authority:** the **R1–R10 scheme in this section is the CANONICAL conformance-rule
> numbering for the whole spec** — the other sections (S3's named rules `beat-has-venue`,
> `render-is-pure`, `total-order-selection`, `director-subtract-only`, etc.) **harmonize to it** by
> name→R-number mapping, they do not introduce a parallel numbering. The scheme is internally
> complete: R1–R10 each name a single `tools/` home (new or an explicit `extend …`), and the two
> "same-rule-extended" items (gate-cites-ledger_cause → R2/R3; replay-determinism → key-log parity
> harness) are called out as folds, not new numbers — so no invariant is left without exactly one
> home.

| # | Rule | Checks | `tools/` home |
|---|---|---|---|
| R1 | **predicate-field-resolves** | every `trigger.predicate.field` resolves to a live clock/stat/track (catches ARC-T04 dangling ID + STRUCK Coup Counter) | `tools/ci_arc_predicate_check.py` (new) |
| R2 | **consumer-closure** | every emitted Key (incl. the 2 new) names ≥1 declaring consumer in some `consumes:` | extend `tools/ci_module_contract_check.py` |
| R3 | **total-accounting linter** | every touched Key is RENDERED/ACCUMULATED/CONSUMED/DISCARDED-with-reason; no silent drop | `tools/ci_total_accounting_check.py` (new) |
| R4 | **C2 literal-string lint** | no narratological label ("Rising Action", arc/lifecycle/salience-state names) surfaces — applied to ALL lifecycle/salience state AND baked fragments | extend `tools/ci_naming_check.py` |
| R5 | **scene_entered single-emitter** | only `game_director` emits `mechanical.scene_entered/exited/skipped` (enforces S4.8 once ratified) | `tools/ci_single_emitter_check.py` (new) |
| R6 | **watching/participating = OFFER not outcome** | every major arc has ≥1 OFFERED intervention window before converging; counts windows OFFERED (fired summons/slate candidate), NEVER windows TAKEN — an all-ignored major arc still converges on time and passes | `tools/ci_engagement_window_check.py` (new) |
| R7 | **no-set()-gates-convergence-order** | convergence dedup/emit uses an order-preserving container keyed by a total order; no `set()` gates emission order (second ORD-2 guard) | extend `tools/ci_ordering_check.py` |
| R8 | **foreclosure-mandatory-render** | (a) `stakes_tags:[foreclosure]` transitions originate only from `edge_triggered_once/retryable/convergence`; (b) each emits a Tier-3 chronicle beat (positive surfacing) | `tools/ci_foreclosure_check.py` (new) |
| R9 | **convergence-effect-provenance** | any `convergence` vector with non-empty `pressure_effects[]` traces each delta to a register line; `cosine_detected` convergences carry zero `pressure_effects` | `tools/ci_convergence_provenance_check.py` (new) |
| R10 | **engagement-window-divergence** | every `edge_triggered_retryable`/`convergence` vector with the player in `participating_actors` exposes ≥2 participated-outcome classes mapping to ≥2 distinct next `lifecycle.state` (or distinct `pressure_effects`); windows collapsing to one successor flagged illusory-choice at compile | `tools/ci_window_divergence_check.py` (new) |

Two further rules are the SAME rules extended, not new homes: **gate-cites-ledger_cause** (every
`stakes_tags:[gating]` transition names a `ledger_cause`) folds into R2/R3; **replay-determinism**
(quantized cosine + meaningfulness + order-preserving containers, S4.2) is validated by the existing
key-log parity harness (`CLAUDE.md §6`), extended with the fixed-point arithmetic pins.

**Two conformance gates deferred to the render lane but NAMED here so they are not dropped:**
- **pricing-over-gating audit (C7).** `stakes_tags` is a bare enum carried through compile untouched
  (synthesis §2); nothing prefers pricing. Add a compile-time `gating:pricing` ratio report + a rule
  that every `stakes_tags:[gating]` vector carries a `gaps[]`/justification note stating why pricing
  is infeasible — making gating the audited exception the charter's "pricing preferred" intends
  (`00_engine_charter.md:40,76`). `[OPEN — Jordan]` (default: add the audit). _(Applies adversarial
  MAJOR: pricing-over-gating unenforced.)_
- **salience demotion player-protection (C7).** Nothing protects a player-pursued arc from demotion
  to Tier-1 texture, so a player-chased arc can be soft-railroaded to rumor. Add a rule: any arc with
  a player participated-outcome in `causes[]` within the last K seasons is demotion-exempt (floored
  at foreground) until it resolves/converges; demotion may only touch player-untouched arcs. `K` is
  `[OPEN — Jordan tuning]`. _(Applies adversarial MAJOR: salience demotion can railroad attention
  away from player-pursued arcs.)_

---

## S4.10 The director is a SUBTRACTIVE budget ceiling — NOT a tension-curve owner (C7 reconciliation)

Synthesis §4 and `00_engine_charter.md:128-129` say the director "owns the tension curve" and
"graduates articulation D11". Two problems make this a substrate-contract concern, not just a Q4
styling choice:

1. **D11 is contentless.** `articulation_layer_v30 §7` explicitly DEFERS pacing ("does not enforce
   pacing; cut scenes fire whenever triggers match"), and `§10` marks D11 "Deferred". There is no
   mechanism to graduate — "graduate D11" would be authoring pacing from nothing under a routine-work
   banner.
2. **Curve-shaping is the over-orchestration C7 forbids, and doc-10 §8.5's NOT-list stands
   (`00_engine_charter.md:104-105`, including "no designed dramatic timing").** C2 is met only
   *lexically* by the literal-string lint (R4); doc-12 §0's veto targeted the engine *knowing/imposing
   dramatic structure in real time*, which a tension-curve scheduler does internally regardless of
   surfacing.

**Reconciliation (structure, binding on the substrate contract):** the director may only **RATION
which already-emerged beats surface** — a subtractive surfacing ceiling. It caps N cut scenes/season
(the `player_agency_v30 §4.3` 3–5 envelope) and demotes overflow to texture. It may NEVER manufacture,
insert, promote, reorder, delay, or time-compress an underlying event to shape a curve. **Event
timing stays fully emergent**, preserving doc-10 §8.5. Conformance corollary (folds into R3/R4): the
director may only SUBTRACT (ration/demote), never INSERT or advance timing. Tension-curve *ownership*
is DROPPED from the engine's owned-state list (S4.1 lists a "salience/tension ledger" only as a
C2-internal *rationing* input, never a *shaping* target). _(Applies adversarial MAJORs: real-time
tension curve vs NOT-list; director graduates a deferred/contentless spec + curve-shaping is
over-orchestration.)_

---

## S4.11 Open flags this section introduces or carries (with defaults)

Genuine Jordan forks and the two blocker-derived corrections that touch the substrate contract. All
carry a default; none are silently resolved.

1. **scene_entered ownership** (S4.8) — default `game_director` single-source **+ mandatory
   `key_substrate_v30 §8.5` L510 edit in the same PR**; held-back hard call, flag in PR body.
   `[OPEN — Jordan]`
2. **Lifecycle-state field ownership** (S4.1, synthesis fork 5) — default new `game_director`-owned
   store; NPC `arc state` bucket stays the specialization it reads. `[OPEN — Jordan]`
3. **Two new Class B Key types** (S4.5, synthesis fork 4) — default add
   `meta.convergence_detected` + `meta.arc_state_changed` (total-accounting > type-count).
   `[OPEN — Jordan]`
4. **Convergence temporal_window** (S4.5, synthesis fork 3) — default 4-season cosine window (±0.40)
   for the general backbone, same-Accounting-boundary for the 8 hand-authored conjunctions; the
   ±0.40 value is `[OPEN — Jordan tuning]`, the comparison's fixed-point determinism is structure
   (S4.2.3). `[OPEN — Jordan]`
5. **Stages 2–3 gated on Gate-0 / ED-1051 (engine_clock)** (S4.2.2) — not a fork so much as a hard
   ordering precondition surfaced here: the per-season cadence rides the unauthored temporal spine;
   `engine_clock` authoring (candidate home `propagation_spec_v1 §O.2`) precedes clock-stepping and
   Accounting-boundary detection. Stages 0–1 are unblocked.
6. **Bake-volume headline correction (BLOCKER, fork 6).** The "~350–450 authored units (feasible)"
   figure (synthesis §6 / `dossier_content_economics §2.2`) is computed **without Certainty as a
   frozen-pool axis**. Synthesis fork 6's DEFAULT is *include Certainty (charter authority,
   `00_engine_charter.md:126`)*, which `dossier_content_economics §3 item 3 / §5 item 2` say
   multiplies the pool ~5–6× → **low-thousands, not 350–450**; dossier §5's verdict is
   CONDITIONAL-feasible, not "feasible". **Corrected statement:** ~350–450 holds ONLY if Certainty is
   a runtime lexicon-swap (fork-6 fallback); under the DEFAULT (Certainty in the frozen pool) the
   honest bake is **low-thousands**. Do not label 350–450 "feasible" while defaulting to the 5–6×
   choice. Additionally, per-NPC voice must be a distinct bake line item whose top end reflects
   `35 × triggers-per-NPC × variants` (~1,050 units, `dossier_content_economics §3 item 1`), NOT the
   `3–5 × 35` name-swap floor — Q3 "recognizable-yet-dynamic" forbids the name-swap level
   (`00_engine_charter.md:96-98`). `[OPEN — Jordan]` (default: carry low-thousands as the headline OR
   flip fork 6 to lexicon-swap).
7. **Anti-oatmeal is NOT structural (BLOCKER).** Synthesis §6 claims anti-oatmeal is "STRUCTURAL…
   because vectors are data". Vector-as-data guarantees only **slot-filler divergence** (proper-noun/
   stakes/outcome slots differ), NOT **prose distinctiveness** — same cell + name swap reads as
   oatmeal (`dossier_content_economics §3 item 2`). Charter Q4 anti-oatmeal item 3
   (`00_engine_charter.md:133-135`) requires a 5-seed (fixed seeds 42/77/99/137/201, `01_arc_corpus
   §a`) prose-distinctiveness regression; its instrument, **Expressive Range Analysis, is UNBUILT**
   (`dossier_nlg_graduation §4 step 5 / §6 item 7`). **Corrected statement:** vector-as-data
   guarantees slot-filler divergence; prose distinctiveness is NOT structural and MUST be certified
   by an ERA bake gate over the 5 fixed seeds; **building ERA is a Stage-5 blocker**, and arc-specific
   authored color beyond name-substitution is a distinct bake line item. The "by construction"
   capstone-satisfaction claim is removed. Conformance: the ERA gate is a Stage-5 CI gate feeding R4's
   fragment lint; capstone #11 is proven by the 5-seed regression, not by construction.
   `[OPEN — Jordan]`
8. **pricing-over-gating audit + salience demotion player-protection** (S4.9 deferred gates) —
   defaults: add both. `K` (demotion-exempt window) `[OPEN — Jordan tuning]`.
9. **Director tension-curve ownership — DROPPED to subtract-only** (S4.10) — S4.10 presents the
   subtract-only reconciliation as "structure, binding on the substrate contract," but it
   **REVERSES** the charter's explicit directive that the director "**owns the tension curve**"
   (`00_engine_charter.md:128`), and the reversal is unanimous across all five sections. Per
   CLAUDE.md §2 (ED-1094) an explicit-charter reversal must be forked, not asserted — so it is
   carried here as an open fork. **Recommended default = subtract-only** (doc-10 §8.5 "no designed
   dramatic timing" stands, `00_engine_charter.md:104-105`; a curve-shaping scheduler is the
   over-orchestration C7 forbids and the doc-12 §0 veto targeted — S4.10). **Held-back hard call:
   flag in the PR body**; the merge review must ratify the reversal deliberately (ED-1094), not
   bundle it silently. Mirrors S3 Q4.11. `[OPEN — Jordan]`

---

_End S4. Companion sections: S1 arc-vector compile (register formalizability), S2 detector, S3
render/NLG graduation, S5 staging & capstone trace. This section is the connective contract they all
bind to._
