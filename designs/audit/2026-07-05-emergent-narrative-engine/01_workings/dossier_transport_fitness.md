# Dossier — Transport fitness for convergence detection + narrative state

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0068]
Lane: transport fitness. Sonnet. 2026-07-05.

## Sources read in full
- `designs/audit/2026-07-05-emergent-narrative-engine/00_grounding/00_engine_charter.md`
- `designs/audit/2026-07-05-emergent-narrative-engine/00_grounding/03_prior_art_and_module_homes.md`
- `designs/audit/2026-07-05-emergent-narrative-engine/00_grounding/01_arc_corpus.md`
- `designs/architecture/key_substrate_v30.md` (full)
- `designs/architecture/key_type_registry_v30.md` (full — all 44 types)
- `designs/architecture/propagation_spec_v1.md` (full)
- `designs/architecture/scale_transitions_v30.md` §5 (Domain Echo), §12 (All-Directions Key Delivery)
- `references/arcs/arc_register_events.md` §VI (Convergence Markers, COLLISION A–J) — spot-checked
  for what "convergence" means in authored form today
- grep of `sim/**/*.py` for `causes=` / `causes[` — **zero hits** (see §5 below)
- grep of `designs/audit/2026-04-30-architecture-session/*.md` for the ~15% figure's provenance

## Question framing
Charter Q3 (`00_engine_charter.md` line 87-88) requires "correlation tests (shared targets[],
causes[] overlap, temporal windows, same-direction pressure on a shared stake)". The substrate
contract (line 139-140) says the engine OWNS "convergence windows" as new state, distinct from
what it READS. This dossier asks, for each of (a)-(d): what exists today, what's missing, minimal
addition — staying inside C3 (no parallel event system), C5 (no new progression currency, no
scale-local dialect), and AU-1's discipline (no aggregate is ever a write target — derive, don't
mutate).

---

## (a) Convergence-window queries: cross-Key temporal coincidence on shared targets/stakes

**What exists:**
- Total order over the Key log: `emitted_at.season_index` + `sub_step_index`
  (`key_substrate_v30.md` §2.1, §4.7); `propagation_spec_v1.md` §1 O.4/SSI-1..4 nails down
  assignment (KEY_LOG.append-assigned, not emitter-assigned).
- `targets[]` with `actor_id` + `role` on every Key (`key_substrate_v30.md` §2.1, §2.2).
- `CAUSAL_GRAPH` (`key_substrate_v30.md` §5.1-5.3) — sparse dict-of-sets, but this indexes
  **causes[] provenance only**, not target-sharing. It answers "what led to this Key," not
  "what else touched this actor/territory/faction recently."
- `MemoryIndex` (`key_substrate_v30.md` §4.4) has a `by_target_mention: actor_id → [key_refs]`
  bucket and a `by_time_window: season → [key_refs]` bucket — **but this is per-NPC** (`NPC.memory`
  is the scope, §4.3). There is no engine-global equivalent.
- Authored convergence today (`references/arcs/arc_register_events.md` §VI, COLLISION A-J) is
  defined over **continuous faction/clock state** (Loyalty ≤3, TC ≥60, Coup Counter) — e.g.
  COLLISION C: "Torben Loyalty ≤ 3 (ARC-S07) coincides with Southernmost Ritual failure
  (ARC-T04)." These triggers are checked against state variables directly, never against a
  Key-log query. Per `01_arc_corpus.md` (e): "arc entries cite clocks/stats directly... but
  never Keys or Domain Echo by name... no runtime module consumes ARC-IDs." So the *existing*
  convergence vocabulary gives no precedent for a Key-level correlation query — it has to be
  built fresh, informed by, not copied from, the register.

**What's missing:**
1. A **global cross-actor target index** — `by_target_mention` generalized from per-NPC memory
   to an engine-owned structure: `target_id → sorted [(season_index, sub_step_index, key_ref)]`,
   where `target_id` ranges over `targets[].actor_id` (already includes territory/faction ids
   per `role: object`, per §2.2). This is a direct structural analogy to the already-speced
   per-NPC index (§4.4) — same shape, wider scope, same incremental-maintenance-on-write
   discipline. No new Key field required: it indexes the existing `targets[]` array.
2. A **"stake" concept has no Key-level representation.** Charter Q3 says "same-direction
   pressure on a shared stake" — but nothing in `key_substrate_v30.md` §2 defines what a stake
   *is* in Key terms. The minimal reading: a stake = a `targets[].actor_id` (an actor, territory,
   or faction) considered as the coincidence key for the index in (1), scoped by `role` (object
   = institutional/territorial stake; subject = personal stake). This avoids inventing a new
   `stake_id` field — reuse `targets[].actor_id` + `role`.
3. **A time-window sliding accumulator, engine-owned** — the charter's substrate contract
   explicitly names "convergence windows" as new engine-OWNED state (line 139), distinct from
   read-only derivation. This is the "new state bucket" analogous to how `faction_stat[s]` is a
   read-only aggregate but the Key log underneath it is append-only ground truth
   (`propagation_spec_v1.md` AU-1, AU-4). A convergence-window accumulator would be: for each
   `target_id`, a rolling bucket of `(key_ref, symbolic_dimensions, impact_vector sign)` aged out
   by `time_horizon`/decay, queried on demand by the correlation test.
4. **"Same-direction pressure"** is checkable with existing fields — `symbolic_dimensions` and
   `impact_vector[actor][axis]` sign comparison across Keys sharing a target (`key_substrate_v30.md`
   §2.4/§2.5) — no schema change needed there.
5. **causes[] overlap** as a correlation signal is already walkable via `walk_backward`
   (`key_substrate_v30.md` §5.3) — reusable as-is, bounded by `depth_limit`.

**Minimal addition:** one new engine-owned global index (target_id → time-ordered key_refs,
generalizing the existing per-NPC `by_target_mention`/`by_time_window` pattern to engine scope)
+ a windowed accumulator over it ("convergence windows," per the charter's own substrate-contract
language) + a correlation-test function combining (index-membership overlap) × (causes[] overlap
via existing walk_backward) × (same-direction impact_vector/symbolic_dimensions check). **No new
Key schema field is required** — everything the correlation test needs (`targets[]`,
`causes[]`, `symbolic_dimensions`, `impact_vector`, `emitted_at`) already exists on every Key.
This is discipline + one new index, the same shape as `propagation_spec_v1.md`'s own framing
("no bespoke channel is added," §12.2) — the convergence detector is a new **consumer/reader**,
not a new writer, over the existing substrate.

---

## (b) Persistent arc-vector state

**What exists:**
- Arc-vector definitions (`references/arcs/arc_register_*.md`, ~110 IDs) live entirely **outside**
  the Key substrate, as authored prose read by no runtime module (`01_arc_corpus.md` (e)). Their
  "vectors" are clock/stat thresholds (Torben Loyalty 8→0, Coup Counter, etc.), not Key-log state.
- T-23 ("NPC Arc Emergence") IS mechanized — `npc_behavior_v30 §5` state machine + Domain Echo —
  but T-24 ("Convergence as Crisis") is prose-only, no code computes it (`01_arc_corpus.md` (d)).
- No Key type family for an "arc" as a first-class object exists in `key_type_registry_v30.md`
  (checked all 44 types across 7 families — none named `arc_*`, `meta.arc_*`). The nearest
  neighbors — `mechanical.cascade_resolution`, `mechanical.mission_shift`, `meta.knot_formed` —
  are scoped to `faction_id` or a Knot pair, not a general arc-lifecycle object with
  seeded→active→escalating→converging→resolved/dormant/abandoned states (charter Q3).
- `references/module_contracts.yaml` has no `game_director`/`scenario_authoring` consumer
  entries that read or write arc state (`03_prior_art_and_module_homes.md` (c)) — both are
  `doc:null`, `status: extracted`.

**What's missing:**
1. **Arc lifecycle Key types** — `meta.arc_seeded`, `meta.arc_stage_transition` (or
   split per-stage: `meta.arc_escalated`, `meta.arc_converged`), `meta.arc_resolved` /
   `meta.arc_abandoned` / `meta.arc_dormant`. Doc 11 already named the *shape* of two of these
   (`meta.arc_detected`, `meta.arc_resolved` — `03_prior_art_and_module_homes.md` (a)) but they
   were never authored into the registry. This is precisely the missing vocabulary ED-IN-0003
   (convergence detector/applier, charter C4) needs as its **output**.
2. **Persistent accumulated arc state (weight, participating-actor set, lifecycle stage)** must
   NOT be a directly-written mutable field per AU-1's discipline (`propagation_spec_v1.md`:
   "no aggregate is ever written... every write terminates at a settlement/territory substrate
   cell, or a Key-log entry the aggregation function reads at derivation time"). The arc's
   current stage/weight should be **derived** by reading the arc's own lifecycle Keys
   (`meta.arc_*`) at query time — same discipline as `faction_stat[s]`, i.e. `arc_state(id) =
   fold(meta.arc_* Keys tagged/correlated to id)`. This keeps arc state inside "read-only
   getters, no setters" (IV.2 law 1, cited by AU-1) rather than adding a second, un-audited
   mutable aggregate.
3. **Arc-membership tagging.** How does an arbitrary Key (a `scene.dialogue`, a
   `state.standing_change`) get attributed to a given arc? Two options, ranked:
   - **Preferred, schema-conservative:** no per-Key field at all — membership is *computed*, not
     authored, by running the (a)-correlation test against the arc's own known target set
     (the arc's `targets[]`/`causes[]` neighborhood) each time the detector runs. This is
     consistent with C5's "no new progression currency" and the holonic doctrine's "no
     scale-local interface dialect" — an arc is a *view* over the existing Key log, not a
     property baked into every Key.
   - **Fallback if re-derivation cost is too high at scale** (2,700-27,000+ Keys per campaign,
     `key_substrate_v30.md` §10): an *optional* `payload.arc_refs: [arc_id]` convention (payload,
     not a universal-schema change) populated by emitters when the arc is already known at
     emission time (e.g. a slate scene explicitly tagged as arc-carrying) — same
     population-discipline pattern as `causes[]` itself (§2.2's guideline), not a new required
     field, and not a supersession event against §2.1.
4. Emitting the lifecycle lifecycle Keys is the closure ED-IN-0003 needs: the "detector" reads
   via (a)'s index/correlation test; the "applier" is exactly this — emit a `meta.arc_*` Key
   marking the transition, which then flows through the ordinary §4.1 update rule (memory,
   subscriptions, causal graph) like any other state transition. No parallel system (C3
   satisfied) — the arc engine is a consumer-then-emitter over the same substrate.

**Minimal addition:** 3-5 new `system_meta` Key types (arc lifecycle markers) + a derived
(read-only) arc-state view computed from those Keys + a membership convention (preferably
zero-schema, correlation-derived; payload-optional `arc_refs` only if performance forces it).

---

## (c) The total-accounting invariant

**What exists:**
- §4.1's single update rule guarantees every Key is validated, logged, observer-resolved, and
  routed to `TYPE_SUBSCRIPTIONS[key.type]` (`key_substrate_v30.md` §4.1 steps 1-7) — this is
  "did every declared consumer see it," a **static registration** guarantee
  (`module_contracts.yaml` consumer lists), not a **runtime per-Key disposition** record.
- §4.8 Key lifecycle states (Drafted/Emitted/Persistent/Decayed/Pruned) describe
  memory/persistence lifecycle (does this Key still surface in NPC reasoning), **not** narrative
  disposition (was this Key ever shown to the player, backgrounded with dignity, or dropped by
  the significance filter — charter's own vocabulary, "filtering ladder (trigger → significance
  → accumulate → discard)").
- Keys are immutable once logged (append-only, §2.3; the propagation spec's drain explicitly
  states "No mutation of the logged Key," §4.2) — so a disposition tag **cannot** be written onto
  the Key itself after the fact.

**What's missing:**
- A per-Key **disposition ledger**, separate from the Key log, recording for every narrative-
  eligible Key one of {RENDERED, ACCUMULATED, CONSUMED-INTO-STATE, DISCARDED+reason}. This is
  structurally identical to `NPC.memory` (§4.3: `key_ref` + `salience`, append-only, one entry
  per (npc, key)) but **engine-global and single-writer**: `NARRATIVE_DISPOSITION_LOG: key_ref →
  {disposition, reason, surface/tier, season_index}`, written exactly once per eligible Key at
  the point the filtering ladder resolves it.
- The filtering ladder itself (articulation_layer_v30, doc 12) has no requirement today that a
  "discard" step write anything — it can silently return without action. The gap is not a
  missing mechanism so much as a missing **write requirement** at the point that already exists.
- A CI-checkable invariant (per charter's "a CI-checkable rule per invariant, each living once in
  `tools/`") — new validator: for every Key in KEY_LOG whose type is in the narrative-relevant
  set (`scene_event`, `da_outcome`, `state_transition`, `scene_outcome`, `system_meta`, plus (b)'s
  new `arc_*` types), assert exactly one `NARRATIVE_DISPOSITION_LOG` entry exists. Same shape as
  the existing `ci_sim_fabrication_check.py` (CLAUDE.md §7/§8) — scans the log, asserts a
  1:1 property, lives once in `tools/`.

**Minimal addition:** one new append-only engine-owned ledger (no Key-schema change — mirrors how
Memory itself was added without altering the Key shape) + a write-on-resolve requirement at the
filtering ladder's existing discard point + one new CI validator.

---

## (d) Trail media — the causes[] walk made diegetic

**What exists:**
- `walk_backward`/`walk_forward` (`key_substrate_v30.md` §5.3) already do the graph traversal
  needed, with a `depth_limit` parameter — directly reusable.
- §5.4 "Diagnostic UI use" already specs a player-facing consumer of this walk: the Phase 5a
  "Why?" diagnostic, backward-walking from a focal Key and filtering to the player's observable
  subset (visibility-gated). **This is framed as a debug/diagnostic overlay**, which sits in
  tension with C2 (no narratological surfacing) if left as-is — Q4's "Trails" requirement wants
  this walk surfaced as **in-world discoverable media** (rumor, witness, document, Thread-Read),
  not a meta UI panel.
- `scene.witness` (`key_type_registry_v30.md` §2) already has the right shape for one trail
  medium: `required_payload_fields: observed_key_id, witness_actor` — a witness Key that *names*
  the Key it observed. This is exactly the primitive Q4 wants, already registered, just not used
  generatively.
- `scene.gossip` (§8, PP-687 Phase B Stage 1) is a working in-world propagation mechanism
  (`principals`, `cumulative_drift`, `origin_interaction_key`, `propagation_observers`) — closest
  existing precedent for a "document/rumor" medium, but scoped specifically to Procedure E's
  social-drift mechanic, not general-purpose.
- `scene.thread_operation` (Thread-Reads' likely carrier) is `[STUB]` — payload inferred, not
  canon-specified (`key_type_registry_v30.md` line 145) — a real gap for the "Thread-Reads" trail
  medium the charter names explicitly.

**What's missing:**
1. A **generic trail-artifact primitive** that, for a foregrounded Key (one dispositioned
   RENDERED per (c)), packages one hop of its `causes[]` chain as an in-world object the player
   can discover via investigation/dialogue/fieldwork — rather than only being queryable via the
   diagnostic UI. `scene.witness`'s `observed_key_id` is the exact right shape; the gap is a
   **document-class** medium (no Key type today plays the "a written record naming a prior Key"
   role the way `scene.witness` plays it for direct observation and `scene.gossip` plays it for
   social propagation).
2. **Systematic generation, not ad-hoc authoring**: today, `scene.witness`/`scene.gossip` fire
   only when the emitting system (scene_slate, npc_behavior, fieldwork) happens to construct one.
   Nothing currently says "when a Key is foregrounded (disposition=RENDERED, per (c)), also emit
   a trail-medium Key referencing it" — that pairing rule doesn't exist yet.
3. **Investigation/fieldwork consumer wiring**: `scene.investigation_resolved` currently has no
   declared read-path over trail-medium Keys by their `references_key`/`observed_key_id` field —
   the consumer side of the walk isn't wired even where the emitter primitive already exists.

**Minimal addition:** (i) reuse `scene.witness`'s `observed_key_id` pattern as the general trail
shape; (ii) add one new lightweight Key type (or an optional payload extension on
`scene.witness`) — e.g. `scene.trail_artifact { references_key: <key_id>, medium: rumor |
witness | document | thread_read }` — emitted alongside any Key that clears the (c) disposition
= RENDERED gate and passes the Q3 meaningfulness test; (iii) a declared consumer relationship:
fieldwork/investigation systems query trail-artifact Keys by `references_key` to resolve
backward through `causes[]`, reusing `walk_backward` unchanged. No new graph mechanism — the
walk already exists; what's missing is packaging its output as an in-world Key instead of only
a diagnostic-UI query result, plus the emission rule that makes it happen systematically instead
of ad hoc.

---

## (e) Raising causes[] population from ~15%

**Provenance of the 15% figure (grounding this precisely, since the audit calibration list is
context not discovery):** grep of `sim/**/*.py` for `causes=`/`causes[` returns **zero hits** —
there is no code today that populates a top-level `causes[]` field on anything, because the Key
substrate itself is still design-only / PROVISIONAL (`key_substrate_v30.md` §7.1 Phase A: "no
system migrated yet"). The ~15% figure (`key_substrate_v30.md` §5.2, §10; confirmed in
`designs/audit/2026-04-30-architecture-session/09_PP-687_simulation_evaluation.md` lines 60/161)
comes from the **Stage-10 sim's synthetic Key-emission test harness** (a randomized ~10-15%
chance of populating `causes[]` per Key, used to validate the substrate's sparse-graph handling)
— **not** from real production emitter logic. So today, literally no emitter populates it,
by construction; the number describes a test assumption, not an observed authoring failure.
`10_emergent_arcs_engagement_NERS.md` line 457 already flags the fix as a **prose
recommendation that was never landed as a spec edit**: "PP-687's spec should add §3.x guidance...
causes[] must reference prior Keys" — this recommendation sits in an audit doc, not in
`key_substrate_v30.md` itself; `key_substrate_v30.md` §2.2 already carries similar prose
("Authoring guideline... This is not optional for emergent narrative legibility") but it is
guidance, not a validated invariant — §2.3's 8 universal invariants do not check `causes[]`
non-emptiness against any condition.

**A concrete, zero-new-apparatus rule (the real finding):** the type registry already contains
**payload-level fields that duplicate what causes[] should carry**, i.e. the causal information
is already computed by the emitter, just not copied into the field the graph/walks actually
read:

| Type | Payload field that names a prior Key | causes[] populated? |
|---|---|---|
| `state.scar_acquired` | `triggering_event_key` (required) | not required to mirror |
| `env.peninsular_strain_shock` | `cause_keys` (required, plural) | not required to mirror |
| `state.belief_revised` | `triggering_keys` (optional) | not required to mirror |
| `scene.gossip` | `origin_interaction_key` (required) | not required to mirror |
| `state.opinion_revised` | `driver_memory_refs` (optional) | not required to mirror |
| `mechanical.cascade_resolution` | `triggered_by` (categorical, not key_id — weaker signal) | n/a |

**Minimal addition:** a mechanical mirroring rule at emission time — "any type whose registry
entry declares a `*_key`/`*_keys`/`*_refs` payload field pointing at prior Key IDs MUST copy
those IDs into `causes[]` at emission" — enforced as a new §2.3-style invariant (warn-level,
matching the project's existing warn-not-block precedent for in-flux schema per CLAUDE.md §5's
`descriptor_registry.yaml` attribute-key treatment). This alone raises population for at least
5 of 44 registered types **using information the emitter already has**, with no new field, no
new module, and no change to what any consuming system reads (`causes[]` is already the read
target for `walk_backward`/`walk_forward` and the CAUSAL_GRAPH). Broader authoring discipline
(requiring emitters to populate `causes[]` whenever they *know* a prior Key caused the event,
per the existing §2.2 guideline) is the second, harder-to-enforce lever — the mirroring rule
above is the concrete, immediately actionable one because it needs no new judgment calls, only
copying data the emitter already has in hand.

---

## Cross-cutting notes for the assembling agent
- None of (a)-(d)'s minimal additions require a new Key-schema field on every Key (i.e. no
  change to §2.1's required fields) — everything routes through `targets[]`, `causes[]`,
  `symbolic_dimensions`/`impact_vector`, and new **Class B** system_meta types plus new
  **engine-owned indexes/ledgers** that sit beside (not inside) the Key. This matches
  `propagation_spec_v1.md`'s own discipline ("no bespoke channel added," §12.2) and AU-1
  ("no aggregate is ever written" — derive, don't mutate).
- The engine-owned state named by the charter's substrate contract ("arc-vector states, actor
  narrative weight, convergence windows, texture budgets") maps cleanly onto: (b)'s derived
  arc-state view, (a)'s convergence-window accumulator, and (c)'s disposition ledger — three
  concrete new state buckets, not one monolithic new subsystem.
- `scenario_authoring` and `game_director` (both `doc:null`, `03_prior_art_and_module_homes.md`
  (c)) are the two candidate homes for the new indexes/emitters — neither has an authored spec
  today, which is a pre-existing gap this lane inherits rather than resolves.
- Open item for Jordan: whether arc-membership tagging should be zero-schema (correlation-
  derived, preferred) or needs the payload-optional `arc_refs` fallback is a performance question
  this dossier cannot resolve without a scale estimate at production Key-log sizes (2,700/30
  seasons per `key_substrate_v30.md` §10, scaling toward 27,000+ at 100 seasons — extrapolated,
  [UNGROUNDED] beyond §10's stated 30-season figure).
