<!-- [CANONICAL: 2026-05-01 — PP-687 v1 universal Key substrate; promoted from PROVISIONAL after Stage 10 sim PASS (12/14 battery; commits bb5e293 lateral + 3cb5207 articulation); V7/V8 perf items UNVERIFIED pending Phase 5a, not blocking] -->
<!-- STATUS: PROVISIONAL — Class A canonical document; ratification by Jordan or designated authority required for promotion. -->
<!-- AUTHORITY: PP-687 (this doc); supersedes doc 08 §1 EventImpact, bespoke event records in doc 12 procedures, NPC Memory bespoke schema, Conviction Scar trigger schema. -->
<!-- SUPERSESSIONS: SUPERSESSION-PP687-001, SUPERSESSION-PP687-002, SUPERSESSION-PP687-003 -->

# Universal Key Substrate (PP-687)
## Status: CANONICAL

**Class:** A — foundational engine substrate.
**Status:** PROVISIONAL.
**Sequencing:** ratifies before PP-686 implementation; consumed by PP-688.
**Companion docs:** `designs/architecture/key_type_registry_v30.md` (Key type registry); `designs/personal/conviction_axis_matrix_v30.md` (axis vectorization).
**Co-files updated:** doc 08, doc 12 (procedures rewritten to consume Keys), `designs/personal/conviction_track_v1.md`, scene/social_contest/mass_battle docs (per Phase B migration), `references/glossary.md`, `references/alias_registry.yaml`, `canon/supersession_register.yaml`, `references/canonical_sources.yaml`.

---

## §1 Substrate Statement

Every consequential event in the Valoria engine is represented as a **Key** — a typed, validated, append-only record. A single update rule consumes Keys and propagates effects to observers, subsystems, and the causal-graph. Save state = initial conditions + Key log. Replay = deterministic re-execution of the log.

Keys are the engine's only event substrate. No system maintains a private event channel; every system emits Keys and consumes Keys.

The chronicle metaphor is exact: Keys are the *cronaca* entry; observers are the witnesses; the causal graph is the *concatenated narrative*; replay is the chronicler's re-reading.

---

## §2 Universal Key Schema

### §2.1 Required fields

```yaml
Key:
  # Identity
  id: <uuid>                                    # globally unique
  type: <key_type_string>                       # registered type per registry

  # Causation
  source_actor: <actor_id | null>               # proximate cause; null for environmental
  emitted_at:
    season_index: <int>                         # ordered season position
    sub_step_index: <int>                       # ordered position within season
  causes: [<key_id>, ...]                       # provenance — Keys that led to this

  # Targets and impact
  targets:
    - actor_id: <id>
      role: <subject | object | witness | beneficiary | bystander>
      impact_vector:                            # Conviction-axis projection of effect on this actor
        hierarchical: <signed_magnitude>
        sacred: <signed_magnitude>
        instrumental: <signed_magnitude>
        traditional: <signed_magnitude>
      stat_deltas:                              # raw mechanical deltas (system-specific bounds)
        <stat_name>: <delta>

  # Scale and symbolic content
  scale_signature: [<personal | settlement | territory | peninsula>, ...]
  symbolic_dimensions:                          # event's position in axis space
    hierarchical: <position>
    sacred: <position>
    instrumental: <position>
    traditional: <position>

  # Visibility
  visibility:
    public: <bool>                              # observable by all in scale
    semi_public_observers: [<actor_id>, ...]    # restricted multi-witness list
    private_observers: [<actor_id>, ...]        # specific only

  # Temporal properties
  time_horizon: <immediate | near | far>        # immediate=this season; near=1-3; far=4+
  permanence: <transient | persistent | indelible>

  # Type-specific payload
  payload: <type-specific dict>                 # see §3 type-specific schemas
```

### §2.2 Field semantics

`source_actor` — the proximate cause. May be null for environmental events (peninsular_strain, season changes, harvest events). Multi-actor causes name the initiator; participants appear in `targets[]` with role=subject.

`emitted_at` — ordered position. `season_index` is monotonic across the campaign. `sub_step_index` orders Keys within a season; tiebreak by emission order (stable sort).

`causes[]` — provenance graph. 0–3 entries typical. Walking backward yields the diagonal chain; walking forward yields the cascade of consequences. **Authoring guideline:** when an emitter knows that prior Keys caused this event, populate `causes[]`. This is not optional for emergent narrative legibility; sparse `causes[]` produces shallow chains.

`targets[]` — affected actors. Role disambiguates downstream interpretation:
- `subject`: actor being acted upon directly (DA target, scene-action recipient)
- `object`: territorial or institutional target (territory, faction, building)
- `witness`: present and observing but not directly affected
- `beneficiary`: outcome accrues to (faction whose Mission is served)
- `bystander`: present but not centrally involved

`impact_vector` — signed projection of the event's effect on a target along each Conviction axis. Replaces doc 08 categorical (aligned/neutral/contradicted) with continuous projection.

`stat_deltas` — raw mechanical state changes (Treasury −5, Discipline +1). Decoupled from symbolic interpretation; both can coexist in the same Key.

`scale_signature` — list of scales the event runs at. Multi-element when an event operates at multiple scales (a peninsula-relevant treaty signed in a settlement scene).

`symbolic_dimensions` — the event's position in axis space (hierarchical/sacred/instrumental/traditional). Used by armature dot-products to produce per-observer interpretation.

`visibility` — determines who can form Memory. Public events observed by all in `scale_signature` extent; semi-public by witness list; private by specific list. **Default visibility:** computed from scene presence (see §6.2). Authors may override.

`time_horizon` — expected effect duration. `immediate` = this season only; `near` = 1–3 seasons; `far` = 4+ seasons.

`permanence`:
- `transient`: present this season only (a passing rumor; pruned after time_horizon)
- `persistent`: state that decays over seasons (a Conviction Scar entering Memory; remains until salience reaches 0)
- `indelible`: never decays (a treaty signed, a death witnessed, a Knot formed)

`payload` — type-specific. Per-type schema in registry.

### §2.3 Validation invariants

Every Key is validated at emission against the type registry. Required-field constraints are per-type; universal invariants always hold:

1. `id` unique across the log.
2. `type` registered in current type registry.
3. `causes[]` contains only Keys already in the log.
4. `causes[]` does not introduce a cycle (BFS-checked at emission time; see §4.6).
5. `emitted_at` strictly orders Keys: each new Key has `(season_index, sub_step_index)` ≥ all prior Keys' values.
6. `impact_vector` and `symbolic_dimensions` axis names match the canonical 4-axis set (per §2.5).
7. `scale_signature` non-empty.
8. `visibility` exactly one of: `public=true`, `public=false` with non-empty `semi_public_observers`, or `public=false` with non-empty `private_observers`.

A Key failing any invariant is rejected; emitter receives `ValueError` and the Key does not enter the log.

### §2.4 Conviction axis-space (4-axis)

The substrate uses four named axes for symbolic dimensions and impact vectors:

| Axis | Positive pole | Negative pole |
|---|---|---|
| **hierarchical** | rank-bearing, status-asserting, deferential to position | egalitarian, status-effacing, peer-leveling |
| **sacred** | numinous, ritually charged, oath-binding | secular, instrumental, contractually bounded |
| **instrumental** | end-justifies-means, calculative, transactional | principled, deontological, intrinsically motivated |
| **traditional** | precedent-respecting, conservative, ancestral | progressive, reformist, generative |

The 4-axis simplification is acknowledged: some Renaissance distinctions (Community vs Identity convictions; communal-vs-categorical belonging) collapse onto similar axis-positions. **A 5th axis is permitted as a Class B extension if Stage 10 calibration finds the simplification load-bearing**; treat as deferred unless required.

### §2.5 Conviction → axis mapping

Per `designs/personal/conviction_axis_matrix_v30.md`, each Conviction projects onto the 4 axes via a 13-entry × 4-column matrix. NPCs read the matrix to derive armature_position from their personal_convictions vector:

```
npc.armature_position[axis] = Σ over c in Convictions:
    npc.personal_convictions[c] × CONVICTION_AXIS_MATRIX[c][axis]
```

A Key's `impact_vector[actor].axis_name` is the *signed magnitude* of the event's effect on that actor along that axis. The armature's interpretation of a Key for a given NPC is:

```
interpretation(npc, key) = Σ over axes:
    npc.armature_position[axis] × key.symbolic_dimensions[axis] × key.impact_vector[npc.id][axis]
```

The result is a scalar driving Concern salience, Disposition shift, Memory salience, etc.

---

## §3 Key Type Registry

Full registry in `designs/architecture/key_type_registry_v30.md`. Summary structure:

7 type families × 25–30 subtypes (total). Initial registry:

| Family | Subtypes (initial) |
|---|---|
| **scene_event** | scene.dialogue, scene.witness, scene.gift, scene.insult, scene.threat |
| **da_outcome** | da.public_governance, da.covert_betrayal, da.diplomatic_alliance, da.antinomian_action, da.economic_intervention |
| **mechanical_event** | mechanical.season_change, mechanical.accounting, mechanical.cascade_resolution, mechanical.mission_shift |
| **state_transition** | state.scar_acquired, state.standing_change, state.coup_attempted, state.succession |
| **environmental** | env.peninsular_strain_shock, env.crisis, env.disaster, env.population_change |
| **scene_outcome** | scene.contest_resolved, scene.battle_concluded, scene.investigation_resolved |
| **system_meta** | meta.knot_formed, meta.thread_woven, meta.miraculous_event |

(PP-688 extends with `meta.knot_ruptured` and `state.belief_revised` as Class B additions.)

Adding a new Key type is a Class B extension. Modifying an existing type's required-payload fields is a supersession event (entry to `canon/supersession_register.yaml` required).

---

## §4 Update Rule and Lifecycle

### §4.1 The single update rule

```
on_key_emitted(key):
    # 1. Validate against registry and universal invariants (§2.3)
    validate(key)

    # 2. Append to Key log (immutable)
    KEY_LOG.append(key)

    # 3. Resolve observer set (§4.2)
    observers = compute_observers(key)

    # 4. Each observer interprets and applies
    for observer in observers:
        interpretation = observer.armature.interpret(key)
        memory_salience = compute_salience(interpretation, key.time_horizon)
        observer.memory.record(key.id, salience=memory_salience)
        observer.apply_state_changes(interpretation, key.stat_deltas)

    # 5. Cross-system propagation
    for subscribing_system in TYPE_SUBSCRIPTIONS[key.type]:
        subscribing_system.consume(key)
        # Subscription callbacks must be O(1) or async — long-running consumers
        # subscribe to async queue, not synchronous emit path.

    # 6. Causal graph update (sparse representation; see §5.2)
    for cause_id in key.causes:
        CAUSAL_GRAPH.add_edge(cause_id, key.id)

    # 7. Awareness update for caused Keys (PP-688 §6 extension)
    for cause_id in key.causes:
        cause_key = KEY_LOG.lookup(cause_id)
        cause_key.awareness = clamp(cause_key.awareness + 0.1, 0, 1)
```

This rule is the *only* update path for engine state. All systems emit Keys; all systems read Keys.

### §4.2 Observer resolution

```
compute_observers(key):
    observers = set()
    if key.source_actor is not None:
        observers.add(key.source_actor)
    for target in key.targets:
        observers.add(target.actor_id)
    if key.visibility.public:
        observers.update(actors_in_scale(key.scale_signature))
    observers.update(key.visibility.semi_public_observers)
    observers.update(key.visibility.private_observers)
    return observers
```

`actors_in_scale(scales)` returns all actors whose state intersects the scales in `scales`. For peninsula-scale Keys this includes all faction-aware actors; for personal-scale this is the immediate scene members.

**Default visibility computation** when not explicitly authored:

```
default_visibility(scene_id, scale_signature):
    scene_members = get_scene_members(scene_id)
    if scene is in public space (per scene_slate spec):
        return {public: true}
    elif len(scene_members) >= 2:
        return {public: false, semi_public_observers: scene_members}
    else:
        return {public: false, private_observers: scene_members}
```

Authors may override default visibility per-Key. Override is recorded in payload metadata.

### §4.3 Memory as Key reference

NPCs maintain a Memory log of Key references with per-NPC salience:

```yaml
NPC.memory:
  - key_ref: <key_id>
    salience: <0..3>
    seasons_held: <int>
    decay_rate: <float>                  # per time_horizon
```

Memory queries (used by armature, Concern generation, Disposition update, etc.) walk this log filtering by:
- Time window: `seasons_held ≤ N`
- Salience threshold: `salience ≥ S`
- Conviction-axis relevance: `dot(query_axis, key.symbolic_dimensions) ≥ R`
- Targeting: `npc.id in [t.actor_id for t in key.targets]`

### §4.4 Memory Query API

Memory queries must scale to ~1000–3300 entries per NPC across 30–100 season campaigns. Required indexing:

```
MemoryIndex:
  by_axis_relevance:        # axis → sorted list of (salience × axis_alignment, key_ref)
    hierarchical: [...]
    sacred: [...]
    instrumental: [...]
    traditional: [...]
  by_time_window:           # season_index bucket → list of key_refs
    <season>: [...]
  by_target_mention:        # actor_id → list of key_refs where actor mentioned
    <actor_id>: [...]
```

All three indexes are maintained incrementally on Memory write. Queries combine indexes by intersection. Query API:

```
memory_query(npc, axis_filter=None, time_window=None,
             target_filter=None, salience_threshold=0,
             limit=None) → list[(key_ref, salience)]
```

Indexed lookup is O(log n) for any single filter; combined filters intersect indexed sets. No regex / full-scan queries at engine level.

### §4.5 Salience computation

```
compute_salience(interpretation, time_horizon):
    horizon_factor = {immediate: 1.5, near: 1.0, far: 0.5}[time_horizon]
    return clamp(abs(interpretation) × horizon_factor, 0, 3)
```

The dot-product magnitude captures "how much does this event matter to me given my frame." High alignment (positive or negative) → high salience. The form is provisional pending Stage 10 calibration.

### §4.6 Cycle detection

`causes[]` must form a DAG. Cycle detection runs in the validator (§4.1 step 1):

```
detect_cycle(key):
    queue = list(key.causes)
    visited = set()
    while queue:
        cid = queue.pop(0)
        if cid == key.id:
            raise ValueError("Key {key.id} introduces cycle in causes graph")
        if cid in visited:
            continue
        visited.add(cid)
        cause_key = KEY_LOG.lookup(cid)
        queue.extend(cause_key.causes)
```

Performance: O(depth × log size) per emission; sub-millisecond at projected scale (sim §1.6).

### §4.7 Sub-step ordering tiebreak

Keys with identical `(season_index, sub_step_index)` are ordered by emission timestamp via stable sort. Within a single sub-step, the emission order is preserved deterministically. This is the rule that gives replay determinism in multi-emit scenarios.

### §4.8 Lifecycle states

A Key's lifecycle:

1. **Drafted** — type set, payload populated, but not yet emitted (e.g., a DA in player consideration).
2. **Emitted** — committed to log; observer set computed; interpretations applied; CAUSAL_GRAPH updated.
3. **Persistent** — past events with `permanence > transient`; remain in observer Memory and CAUSAL_GRAPH.
4. **Decayed** — Memory salience reached 0; Key remains in log but no longer surfaces in NPC reasoning.
5. **Pruned** — `transient` events past their time_horizon; removed from log.

Pruning policy (current): prune `transient` only. Persistent and indelible Keys are never pruned. Compression of old persistent Keys to summary records is an optional optimization deferred to post-ratification calibration.

---

## §5 Causal Graph and Provenance

### §5.1 Graph structure

`CAUSAL_GRAPH` is a directed acyclic graph. Edges go cause → consequence. Walking backward from any Key produces the causal chain leading to it. Walking forward produces the cascade of consequences emerging from it.

### §5.2 Sparse representation

Production observation (sim §1.1, artifact 09 §2.3): only ~15% of Keys have `causes[]` populated. The graph is **sparse**. Implementation must use sparse representation (dict-of-sets, not adjacency matrix). Most Keys are independent emissions; the graph is dense only where deliberate authoring or systematic chains create chains.

### §5.3 Walks

```
walk_backward(key, depth_limit):
    visited, queue = set(), [(key.id, 0)]
    while queue:
        cid, d = queue.pop(0)
        if cid in visited or d > depth_limit:
            continue
        visited.add(cid)
        for parent in CAUSAL_GRAPH.parents(cid):
            queue.append((parent, d + 1))
    return visited

walk_forward(key, depth_limit):
    # mirror; uses CAUSAL_GRAPH.children
```

Performance: sub-millisecond for 10-depth walks at projected scale (sim §1.1).

### §5.4 Diagnostic UI use

The Phase 5a Godot diagnostic UI exposes walk results to the player as the "Why?" diagnostic (per artifact 09 §1.5, artifact 10 §9.1). Player query → backward walk from focal Key → engine returns chain filtered to player's observable subset (Keys whose visibility includes the player as observer).

---

## §6 Determinism Guarantees

`save = (initial_state, KEY_LOG)`. Replay re-executes the rule against the same KEY_LOG yielding identical state.

Three determinism guarantees the engine must enforce:

### §6.1 RNG seeding per Key emission

Every random draw is seeded per Key emission, not engine-globally. Each emitter records its RNG seed in payload metadata; replay uses the recorded seed. No engine-wide global RNG state contributes to Key payload.

### §6.2 Deterministic ordering

All sub-step tiebreaks via stable sort by emission order (§4.7). No multi-threaded emission paths that cannot be deterministically reproduced; if multi-threading is used, an explicit ordering invariant must be enforced at the substrate boundary.

### §6.3 Floating-point reproducibility

Specified at architecture level: x86_64 with IEEE-754 default rounding (round-to-nearest-even). Cross-architecture FP reproducibility is not guaranteed; save files specify the originating architecture in metadata.

These three together suffice for replay determinism within a single architecture. Sim §1.2 confirmed the architecture supports determinism; production engine implements the three rules at engine init.

---

## §7 Migration and Rollout

### §7.1 Phased rollout

Three phases:

- **Phase A (substrate authoring, this commit + commit 5):** key_substrate_v30.md + key_type_registry_v30.md + axis_matrix_v30.md authored. Substrate exists; no system migrated yet.
- **Phase B (per-system migration, post-ratification):** each consumer system migrated to Keys, one at a time. Existing tests verify no regression. Stages:
  1. doc 12 Political Dynamics procedures rewrite to consume Keys (~1 session).
  2. PP-686 spec consumes Keys (commit 3 of integration plan).
  3. conviction_track + threadwork + fieldwork emit Keys (~0.5 session).
  4. scene_slate + social_contest + mass_battle emit/consume Keys (~1 session).
  5. PP-688 Articulation Layer integrates Keys (commit 4 of integration plan).
- **Phase C (verification, post-Phase-B):** Stage 10 sims (lateral cross-system + articulation) run against full migrated state.

### §7.2 Bootstrap rule for partial-migration state

During Phase B, some systems emit Keys while others use legacy event channels. Substrate handles partial migration via:

```
legacy_event_wrapper(legacy_event, originating_system):
    return Key(
        type='meta.legacy_event',
        source_actor=legacy_event.source,
        targets=[],
        payload={
            'originating_system': originating_system,
            'legacy_payload': legacy_event,
        },
        scale_signature=['system_meta'],
        visibility={public: false, private_observers: [originating_system]},
        permanence='transient',
        time_horizon='immediate',
    )
```

Legacy events arriving during Phase B are wrapped; downstream Key consumers skip `meta.legacy_event` Keys unless they have explicit legacy-handling code. Wrappers are pruned once originating system completes Phase B migration.

### §7.3 Backward compatibility

References in existing canon to "EventImpact," "event record," "Memory record," "Conviction Scar trigger event" map forward to Key types via `references/alias_registry.yaml`. Existing doc 08 EventImpact is the prototype Key family — semantically equivalent to `da_outcome.*` and `state_transition.*` subtypes.

Alias entries:

```yaml
event_impact:
  canonical: "Key"
  abbreviations: []
  aliases: ["EventImpact"]
  legacy: ["EventImpact Matrix"]
  patch: "PP-687"
  note: "Doc 08 EventImpact is the Key prototype; specific subtypes are da_outcome.* and state_transition.*"

memory_record:
  canonical: "Memory entry (Key reference + salience)"
  aliases: ["Memory record", "Memory schema"]
  patch: "PP-687"
  note: "Memory entries are Key references with per-NPC salience. See key_substrate_v30.md §4.3."
```

### §7.4 Supersession

Three supersession entries to `canon/supersession_register.yaml`:

- SUPERSESSION-PP687-001: doc 08 §1 EventImpact → key_substrate_v30.md
- SUPERSESSION-PP687-002: bespoke event records in doc 12 procedures A–E → Key references
- SUPERSESSION-PP687-003: NPC Memory record schema (per npc_behavior_v30) → Memory as Key references with per-NPC salience

---

## §8 Integration with Existing Systems

### §8.1 PP-686 faction architecture

Faction state machinery consumes Keys per `designs/provincial/faction_behavior_v30.md` §4. Mission outcome scoring reads `da_outcome.*`; Cascade resolution triggers on `state.succession` and `state.scar_acquired` (leader); Public Expectation strictness reads from observed faction behavior (full Key stream); L/PS update via standard rule.

PP-686 audit findings resolved via Keys:
- P1-3 DA category schema: provided by `da_outcome.*` subtypes.
- P2-1 NPC behavior coupling: NPCs read effective_convictions in role-acting context (per Key.payload.role_acting flag), personal_convictions in personal-time context.
- P2-3 Strain interaction: `env.peninsular_strain_shock` Keys consumed by faction's public-temperament dynamics.

### §8.2 PP-684 Conviction taxonomy

PP-684 13-Conviction taxonomy + axis matrix (`designs/personal/conviction_axis_matrix_v30.md`) is the substrate for `symbolic_dimensions` and `armature_position`. Keys carry projections; armatures interpret via matrix-mediated dot product.

### §8.3 Doc 12 Political Dynamics

Doc 12's procedures rewrite to consume Keys (Phase B Stage 1):
- Procedure A (Concern generation) reads memory Keys filtered by salience and Conviction-relevance.
- Procedure B (Project advancement) emits scene_event Keys for actions; reads outcome Keys.
- Procedure C (Project completion) emits state_transition Keys.
- Procedure D (Disposition update) consumes scene_event and da_outcome Keys.
- Procedure E (Knowledge sharing) emits scene.dialogue Keys with knowledge payload.

### §8.4 Personal-scale systems

- Piety Track: Scar triggers consume scene.witness Keys; emit state.scar_acquired.
- Threadwork: thread operations emit scene.thread_operation Keys.
- Fieldwork / Knot system: knot formation emits meta.knot_formed; rupture emits meta.knot_ruptured (PP-688 Class B).
- Bonds-≥-5 prerequisite checked via Memory query against accumulated Keys.

### §8.5 Scene-scale systems

- scene_slate: scene activation emits mechanical.scene_entered; events within emit scene.* Keys.
- social_contest (with PP-683 signed −5..+5): each exchange emits scene.dialogue with persuasion_track_displacement payload.
- mass_battle: resolution emits scene_outcome.battle_concluded; phase events emit scene.* Keys.

### §8.6 Strategic-scale systems

- Domain Actions: submission emits scene.draft_da; resolution emits da_outcome.*; consequences propagate via standard rule.
- Faction state: PP-686 components emit Keys when state changes (Mission shift, Cascade re-resolution, L/PS thresholds crossed).
- Turmoil: accumulation emits env.peninsular_strain_shock with delta payload.

### §8.7 PP-688 Articulation Layer

PP-688 extends the Key registry with `meta.knot_formed`, `meta.knot_ruptured`, `state.belief_revised` (Class B). Scene-event Keys gain three optional payload fields: `belief_engagement_for`, `inspirations_engaged_for`, `knot_partners_present`. Significance function reads from Key fields directly. See `designs/articulation/articulation_layer_v30.md`.

### §8.8 Godot implementation (Phase 5a)

Keys map cleanly to Godot Resources:
- `Key` is a Resource subclass (per-type subclasses extend with payload).
- Type registry is a `KeyTypeRegistry` autoload.
- Key log is a `Resource` with typed array.
- CAUSAL_GRAPH is built from Key references; sparse dict-of-sets.
- Save = serialize Key log Resource.

---

## §9 Stage 10 Verification Battery

Property-tests required before promotion to canonical (post-PROVISIONAL):

| # | Property | Test |
|---|---|---|
| V1 | Cycle-freeness | Random 30-season Key emission with 10% causes[]-rate; no cycles introduced |
| V2 | Salience monotonicity | Memory salience strictly non-increasing without re-write triggers |
| V3 | Visibility correctness | Observer set always contains source + targets + visibility witnesses; no leakage |
| V4 | Replay determinism | Same seed + same player choices → identical Key log hash |
| V5 | Cross-system propagation | Key emitted by system A reaches all subscribing systems exactly once |
| V6 | PP-686 integration | da_outcome Keys correctly drive L/PS updates per PP-686 §3.4–3.5 |
| V7 | Memory query performance | 1000-entry queries return in <10ms across all index types |
| V8 | Walk performance | 10-hop CAUSAL_GRAPH walks return in <1ms |

V1–V6 confirmed in sim. V7–V8 require production-engine measurement.

---

## §10 Performance Characteristics (sim-validated)

From `designs/audit/2026-04-30-architecture-session/sims/pp687_sim_output.txt`:

- 30 seasons × 35 NPCs × 6 factions × ~90 events/season = 2,703 Keys.
- Wall time: 144ms. Throughput: 18,724 keys/sec.
- Avg observers per Key: 13.4.
- Memory accumulation: ~1,000 entries/NPC at 30 seasons; ~3,300 at 100 seasons (require Memory Query API §4.4 indexing).
- Causal graph parents: 372; edges: 400 (~15% of Keys have causes — sparse).
- Forward 10-hop walk: 0.07ms; backward: 0.04ms.

Performance is not a constraint at projected game scale.

---

## §11 Vetting Block (per PP-674 framework)

```yaml
vetting:
  class: A
  necessity: pass
  omega: pass
  mu: [Μ-α, Μ-β, Μ-γ, Μ-δ]
  m_ratings:
    M-1: "+"
    M-2: "○"
    M-3: "+"
    M-4: "+"
    M-5: "+"
    M-6: "+"
    M-7: "+"
    M-8: "+"
    M-9: "+"
    M-10: "✓"
    M-11: "+"
  q: pass
```

Full N/Ω/Μ/М/Τ/Q justification documented in `designs/audit/2026-04-30-architecture-session/07_PP-687_proposal.md` §8.

---

## §12 Open Items Carried Forward

Items decided per integration plan §3.4 (D5–D10):

| Decision | Resolution |
|---|---|
| D5 schema sign-off | Approved as drafted |
| D6 type registry initial scope | 7 families × 25–30 subtypes per §3 + key_type_registry_v30.md |
| D7 visibility default | Default-from-scene-presence with explicit override |
| D8 phased rollout | Phased per §7.1 |
| D9 naming | "Key" retained |
| D10 Stage 10 verification scope | Per §9 V1–V8 |

Additional items for Stage 10 calibration:
- Memory salience formula form (§4.5) — calibrate vs sim.
- Pruning compression policy beyond `transient` — defer.
- Cross-architecture FP reproducibility — defer (single-architecture sufficient).

---

**End spec. PROVISIONAL pending ratification.**
