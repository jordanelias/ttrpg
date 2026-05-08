<!-- [PROVISIONAL: 2026-04-30 — PP-687 draft, universal Key substrate] -->
<!-- STATUS: PROVISIONAL — design proposal, not canonical mechanic -->
<!-- TITLE: PP-687 — Universal Key Substrate: typed event records as engine substrate -->
<!-- AUTHORITY: drafted under PP-674 vetting framework. Class A new subsystem. -->

# PP-687 — Universal Key Substrate

**Status:** PROVISIONAL — proposal pending Jordan review.
**Class:** A (new engine substrate; foundational architecture).
**Supersedes:** doc 08 §1 EventImpact (becomes prototype Key); ad-hoc event-passing in doc 12 procedures; bespoke memory record schema; bespoke Conviction Scar trigger schema; bespoke event records in scene/social_contest/mass_battle systems.
**Sequencing dependency:** PP-687 ratifies before PP-686 implementation. PP-686 is rewritten to consume Keys.
**Co-files:** `designs/architecture/key_substrate_v30.md` (new); `designs/architecture/key_type_registry_v30.md` (new); updates to `designs/audit/2026-04-28-political-dynamics-session/12_development_specification.md`, `designs/audit/2026-04-28-political-dynamics-session/08_event_matrix_meta_armatures.md`, `designs/personal/conviction_track_v1.md`, `designs/scene/scene_slate_v30.md`, `designs/scene/social_contest_v30.md`, `designs/scene/mass_battle_v30.md`, `designs/npcs/npc_behavior_v30.md`, `references/glossary.md`, `references/canonical_sources.yaml`.

---

## §0 Abstract

The Valoria engine currently has many event channels — Domain Action outcomes, scene events, Conviction Scar triggers, treaty signatures, mass battle results, Mission shifts, witnessing actions, gifts, insults — each with its own record schema, its own update rule, its own propagation path. This proposal introduces a **universal Key substrate**: a single typed event format consumed by a single update rule, used by every system at every scale.

Each event in the engine emits a **Key** — a structured record with source actor, targets, impact vectors, scale signature, symbolic dimensions, visibility, causal provenance, time horizon, and permanence. NPCs interpret Keys through their armature (per the Conviction-vector framework). Memory becomes a list of Key references with salience. Faction state (Mission, Cascade, Legitimacy, Popular Support) updates from Keys. Diagonal chains become walkable provenance graphs.

The substrate makes lateral cross-system coupling *the default* rather than a per-pair specification problem. It composes naturally with the Conviction taxonomy (PP-684), the Persuasion Track (PP-683), the faction architecture (PP-686), and Phase 5a Godot implementation. It also gives the engine save/restore, replay, and modding interfaces as automatic byproducts.

This is the largest single architectural proposal in the project to date. Its impact crosses every existing system. Its cost is real and front-loaded. Its benefit is structural — once the substrate is in place, subsequent design work composes through it rather than requiring per-system event schemas.

---

## §1 Motivation

### §1.1 Cross-system coupling is currently undefined

The week's NERS audit found lateral peer-system integration to be the project's weakest direction. Specific gaps:

- mass_battle outcomes affect social_contest standings — by what mechanism?
- scene_slate events affect Conviction Scars and faction Cascade — through what channel?
- peninsular_strain events propagate to faction Public Expectation — via what route?

Each pair currently requires either bespoke wiring or implicit inheritance. Adding a new peer system (e.g., a future trade subsystem) means defining N new pair-couplings.

A universal substrate replaces N×N pair-couplings with N system-to-substrate couplings. New systems plug into the substrate; existing systems read from it.

### §1.2 Memory has no canonical schema

The current canon describes Memory as a record with fields *event_type*, *salience*, *implied_affect*, *seeking_tags*, *timestamps* — but the schema varies across consumers. NPC autonomous behavior reads Memory differently from Conviction Scar triggers; both differ from social_contest's reference to "memory of the last debate." This is a documentation gap that a universal Key schema closes.

### §1.3 doc 08 EventImpact is the prototype

The EventImpact Matrix introduced in `designs/audit/2026-04-28-political-dynamics-session/08_event_matrix_meta_armatures.md` is a partial Key — it defines `event_type`, `source_actor`, `material_effects`, `symbolic_effects`, `relational_effects`, `scale_signature`, `time_horizon`, `visibility`. The proposal here generalizes EventImpact to cover *all* event categories, not just political-dynamics-internal events.

### §1.4 PP-686 audit findings

Several PP-686 findings (per `2026-04-30_PP-686_audit_NERS.md`) resolve through Keys rather than through per-finding work:

| Audit finding | Resolution via Keys |
|---|---|
| P1-3 DA category schema | DA categories become Key subtypes (`da_outcome.public_governance`, `da_outcome.covert_betrayal`, etc.) |
| P2-1 NPC behavior coupling | NPCs read Keys via armature; *which* armature (effective vs personal) is a function of context, not of separate event channels |
| P2-3 Strain interaction | Strain emits Keys with peninsula-scale signature; factions/NPCs read them via standard rule |
| Diagonal opacity (E-DIAG-A) | Keys carry `causes[]`; UI surfaces the chain naturally |
| Lateral peer-system gaps | All peer systems emit/consume Keys; coupling is uniform |

### §1.5 Player-facing benefits

Three player-visible features become natural with Keys:

- **"Why" diagnostic.** Player asks why a faction's Public Expectation strictness rose. Engine walks back through recent Keys affecting that faction's L and PS; surfaces the chain. With current architecture this requires bespoke logging.
- **Replay and save-state.** Game state = Key log + initial conditions. Save and restore are file I/O on the log.
- **Audit trail for unexpected dynamics.** A faction collapses unexpectedly; the player traces the cascade of Keys that brought it there.

### §1.6 Modding and authoring

A Key emitter is the engine's plug-in point. A scenario is a Key sequence. A mod is a Key emitter. New event types extend the Key registry without touching engine internals.

---

## §2 Design Goals

| Goal | Means |
|---|---|
| Single substrate for all events | Universal Key schema |
| Type-safe specialization | Key type registry; per-type field constraints |
| Cross-system coupling by default | All systems emit/consume Keys |
| Diagonal provenance visible | `causes[]` chain in every Key |
| Memory derives from Keys | Memory records are typed Key references with salience |
| Save/restore by Key log | Game state = initial state + ordered Key sequence |
| Compose with Conviction taxonomy + faction architecture | Symbolic dimensions and impact vectors live in Conviction-axis space |
| Player-facing diagnostic via Key chain walks | Engine exposes Key history and causal graph |
| Authoring economy | Scenarios author Key sequences; modding is Key emission |
| Compatible with Godot Resources | Key is a Godot Resource subclass; types map to Resource type registry |

---

## §3 Key Schema

### §3.1 Universal Key fields

Every Key, regardless of type, carries these fields:

```yaml
Key:
  # Identity
  id: <uuid>
  type: <key_type_string>                      # see §4 type registry
  
  # Causation
  source_actor: <actor_id | null>              # who or what caused the event
  emitted_at: <season_index, sub_step_index>   # ordered position in time
  causes: [<key_id>, ...]                      # provenance — Keys that led to this
  
  # Targets and impact
  targets:
    - actor_id: <id>
      role: <subject | object | witness | beneficiary | bystander>
      impact_vector:                           # vectorized in Conviction-axis space
        <axis_name>: <signed_magnitude>
      stat_deltas:                             # raw stat changes (if any)
        <stat_name>: <delta>
  
  # Scale and symbolic content
  scale_signature: [<personal | settlement | territory | peninsula>, ...]
  symbolic_dimensions:                         # for armature interpretation
    <axis_name>: <position>                    # uses PP-684 Conviction axes
  
  # Visibility
  visibility:
    public: <bool>                             # observable by all
    semi_public_observers: [<actor_id>, ...]   # restricted but multi-witness
    private_observers: [<actor_id>, ...]       # specific only
  
  # Temporal properties
  time_horizon: <immediate | near | far>       # immediate=this season; near=1-3; far=4+
  permanence: <transient | persistent | indelible>
  
  # Type-specific payload
  payload: <type-specific>                     # see §4 per-type schemas
```

### §3.2 Field semantics

**`source_actor`** is the proximate cause. May be `null` for environmental events (peninsular_strain shocks, season changes). For an event with multi-actor cause (e.g., a battle), the source is the actor who initiated; participating actors appear in `targets` as `subject` role.

**`emitted_at`** orders Keys deterministically within a season. Sub-step index allows multiple Keys per step (e.g., DA resolution emits a sequence of Keys: outcome, observer Memory writes, stat updates).

**`causes`** is the provenance graph. A typical Key has 0-3 `causes`; a downstream Key can have many. Walking this graph backward produces the diagonal chain. Walking forward from a chosen Key produces "consequences of this event."

**`targets[]`** is the canonical list of affected actors. The `role` field disambiguates: a battle has subjects (the combatants), objects (the territory), witnesses (the surrounding population), beneficiaries (the victor's faction). Each role implies different downstream interpretation.

**`impact_vector`** is the Conviction-axis projection of how the event affects the actor. A heretical event has high contradicted-resonance for Faith-Conviction NPCs. The vector replaces the doc 08 `aligned/neutral/contradicted` categorical with a continuous projection.

**`stat_deltas`** is for raw mechanical state changes (Treasury −5, Discipline +1). Decoupled from the symbolic interpretation; both can coexist.

**`scale_signature`** is the list of scales the event runs at. Most events are single-scale; some (a peninsular treaty signed in a settlement scene) are multi-scale.

**`symbolic_dimensions`** is the event's position in named axis space (per PP-684 vectorization decision). Used by armature dot-products to produce interpretation.

**`visibility`** determines who can observe and therefore form Memory. Public events are observed by all in the relevant scale; semi-public by a witness list; private by a specific list. Visibility is a property of the Key, not of consumers — the event itself is public or not.

**`time_horizon`** is the event's expected effect duration. Used to scale Memory salience decay.

**`permanence`** distinguishes:
- `transient`: present this season only (a passing rumor)
- `persistent`: state that decays over seasons (a Conviction Scar)
- `indelible`: state that does not decay (a treaty signed, a death witnessed)

**`payload`** is type-specific. Examples in §4.

### §3.3 Impact vector and symbolic dimensions: relationship to PP-684

PP-684 introduces named axes for Convictions and events:

- *hierarchical ↔ egalitarian*
- *sacred ↔ secular*
- *instrumental ↔ principled*
- *traditional ↔ progressive*

A Key's `symbolic_dimensions` lives in this space. An event's projection onto each axis is authored or computed.

A Key's `impact_vector[actor].axis_name` is the *signed magnitude* of the event's effect on that actor along that axis. For example, a heretical-but-popular event impacts a Faith-aligned NPC negatively on the *sacred* axis (their frame is contradicted) but maybe neutrally on the *instrumental* axis.

The armature's interpretation of a Key for a given NPC is approximately:

```
interpretation(npc, key) = 
    sum over axes:
      npc.armature_position[axis] × key.symbolic_dimensions[axis] × key.impact_vector[npc.id][axis]
```

The result is a scalar that drives Concern salience, Disposition shift, Memory write, etc. — depending on the consumer.

### §3.4 Compatibility with structured-concentration NPCs (sim v2)

NPCs have personal_convictions as a 12-Conviction vector with structured concentration. Translating to axis-space requires a **Conviction → axis matrix** authored once (12 × 4 = 48 entries):

```yaml
CONVICTION_AXIS_MATRIX:
  Faith:      {hierarchical: +0.3, sacred: +0.9, instrumental: -0.5, traditional: +0.7}
  Authority:  {hierarchical: +0.9, sacred: +0.1, instrumental: +0.2, traditional: +0.4}
  Order:      {hierarchical: +0.6, sacred: +0.0, instrumental: +0.0, traditional: +0.5}
  Scholastic: {hierarchical: +0.2, sacred: +0.4, instrumental: -0.3, traditional: +0.6}
  Utility:    {hierarchical: +0.0, sacred: -0.5, instrumental: +0.9, traditional: -0.2}
  Equity:     {hierarchical: -0.7, sacred: +0.0, instrumental: -0.1, traditional: +0.0}
  Liberty:    {hierarchical: -0.6, sacred: -0.3, instrumental: +0.0, traditional: -0.3}
  Precedent:  {hierarchical: +0.4, sacred: +0.2, instrumental: -0.4, traditional: +0.9}
  Community:  {hierarchical: -0.2, sacred: +0.2, instrumental: -0.2, traditional: +0.5}
  Identity:   {hierarchical: +0.1, sacred: +0.3, instrumental: +0.0, traditional: +0.4}
  Warden:     {hierarchical: +0.0, sacred: +0.6, instrumental: +0.1, traditional: +0.6}
  Virtue:     {hierarchical: +0.1, sacred: +0.4, instrumental: -0.4, traditional: +0.5}
```

(Values illustrative; calibration during Stage 10.)

An NPC's armature position in axis-space is computed once from their personal_convictions:

```
npc.armature_position[axis] = sum over Convictions:
    npc.personal_convictions[c] × CONVICTION_AXIS_MATRIX[c][axis]
```

This yields a 4-element vector per NPC. Cosine similarity / dot product on this is the substrate for armature interpretation.

The Conviction-vector representation (12-dim) and axis representation (4-dim) coexist: 12-dim for player legibility (NPC sheets show Conviction labels), 4-dim for engine math (faster, smoother).

---

## §4 Key Type Registry

### §4.1 Type taxonomy

Keys are organized into 7 top-level type families, each with subtypes. The registry is extensible — adding a new type extends the registry without modifying the core schema.

| Family | Purpose | Example subtypes |
|---|---|---|
| **scene_event** | Per-scene actions, observations, exchanges | scene.dialogue, scene.witness, scene.gift, scene.insult, scene.threat |
| **da_outcome** | Strategic-layer Domain Action results | da.public_governance, da.covert_betrayal, da.diplomatic_alliance, da.antinomian_action, da.economic_intervention |
| **mechanical_event** | Engine-driven state changes | mechanical.season_change, mechanical.accounting, mechanical.cascade_resolution, mechanical.mission_shift |
| **state_transition** | Narrative-significant state changes | state.scar_acquired, state.standing_change, state.coup_attempted, state.succession |
| **environmental** | Non-actor-driven events | env.peninsular_strain_shock, env.crisis, env.disaster, env.population_change |
| **scene_outcome** | End-of-scene resolutions | scene.contest_resolved, scene.battle_concluded, scene.investigation_resolved |
| **system_meta** | Engine-level events the player observes | meta.knot_formed, meta.thread_woven, meta.miraculous_event |

### §4.2 Per-type schemas

Each type extends the universal Key with type-specific `payload` content. Examples:

#### scene.dialogue

```yaml
type: scene.dialogue
payload:
  exchange_count: <int>
  initiator_id: <actor_id>
  topic: <topic_string>
  rhetorical_style_used: <style_id>     # for Resonant Style activation
  persuasion_track_displacement: <int>  # ±5..+5 signed (per PP-683)
  outcome: <decisive | compromise | stalemate>
```

Emits Memory references for participants, witnesses, and any audience. Visibility = `public` if scene is in public space; otherwise list-based.

#### da.covert_betrayal

```yaml
type: da.covert_betrayal
payload:
  faction_id: <id>
  target_actor: <id>
  target_faction: <id | null>
  exposed: <bool>                       # was the covert action discovered
  exposure_witnesses: [<actor_id>, ...]
  mission_alignment: <bonus | penalty | none>
```

Visibility flips dramatically based on `exposed`. If false, only the source_actor and target_actor know; if true, exposure_witnesses are added to semi_public_observers, and Legitimacy violation event fires.

#### state.scar_acquired

```yaml
type: state.scar_acquired
payload:
  npc_id: <id>
  conviction: <conviction_name>          # which Conviction took the Scar
  scar_count_before: <int>
  scar_count_after: <int>
  triggering_event_key: <key_id>         # the Key that triggered this
  thread_event_subtype: <string | null>  # e.g., "dissolution_of_living_being"
```

Permanence: `indelible` (Scars don't decay).

#### env.peninsular_strain_shock

```yaml
type: env.peninsular_strain_shock
payload:
  strain_delta: <int>
  cause_keys: [<key_id>, ...]            # which prior Keys caused the shock
  affected_territories: [<territory_id>, ...]
  symbolic_register: <which Convictions feel impact>
```

Source: null (environmental). Scale signature: `[peninsula]`. Visibility: public.

#### mechanical.cascade_resolution

```yaml
type: mechanical.cascade_resolution
payload:
  faction_id: <id>
  prior_aggregate: <conviction_vector>
  new_aggregate: <conviction_vector>
  cascade_fidelity_change: <delta>
  triggered_by: <succession | drift | crisis>
```

Visibility: public (faction state is observable).

### §4.3 Type registry as authored canon

The full registry lives at `designs/architecture/key_type_registry_v30.md`. Each entry includes:

- type_id (e.g., `da.covert_betrayal`)
- description
- required_payload_fields
- optional_payload_fields
- default_scale_signature
- default_permanence
- default_time_horizon
- emitting_systems (which subsystem produces this Key type)
- consuming_systems (which systems consume it)

The registry is Class A canon. Adding a new Key type is a Class B extension. Modifying an existing type's required_payload is a supersession event.

---

## §5 Update Rule and Lifecycle

### §5.1 Single update rule

When a Key is emitted:

```
on_key_emitted(key):
    # 1. Validate against registry
    validate_against_type_registry(key)
    
    # 2. Append to Key log
    KEY_LOG.append(key)
    
    # 3. Resolve observer set
    observers = compute_observers(key)
    # observers includes:
    #   - source_actor
    #   - all targets
    #   - all visibility witnesses (public, semi_public, private)
    
    # 4. Each observer interprets and applies
    for observer in observers:
        interpretation = observer.armature.interpret(key)
        memory_record = observer.memory.record(key, salience=salience(interpretation))
        observer.apply_state_changes(interpretation, key.stat_deltas)
    
    # 5. Cross-system propagation
    for subscribing_system in TYPE_SUBSCRIPTIONS[key.type]:
        subscribing_system.consume(key)
    
    # 6. Causal graph update (for diagnostic UI)
    CAUSAL_GRAPH.add_edge(key.id, key.causes)
```

This rule is the *only* update path for engine state. All systems emit Keys; all systems read Keys. No bespoke event channels remain.

### §5.2 Observer resolution

`compute_observers(key)` resolves the visibility list:

```
observers = set()
observers.add(key.source_actor) if not null
for target in key.targets:
    observers.add(target.actor_id)
if key.visibility.public:
    observers.update(actors_in_scale(key.scale_signature))
observers.update(key.visibility.semi_public_observers)
observers.update(key.visibility.private_observers)
return observers
```

`actors_in_scale()` returns all actors whose state intersects the relevant scale (e.g., for a peninsula-scale Key, all faction-aware actors).

### §5.3 Memory as Key reference

NPCs maintain a Memory log of Key references with per-NPC salience:

```yaml
NPC.memory:
  - key_ref: <key_id>
    salience: <0..3>
    seasons_held: <int>
    decay_rate: <float>                  # per time_horizon
```

Memory queries (used by armature, Concern generation, etc.) walk this log filtering by:
- Time window
- Salience threshold
- Conviction-axis relevance (to current armature query)
- Targeting (which Keys mention this NPC)

This replaces the bespoke Memory schema currently scattered across systems.

### §5.4 Salience computation

```
salience(interpretation) = clamp(
    abs(interpretation.dot(observer.armature_position)) * key.time_horizon_factor,
    0, 3
)
```

Where `time_horizon_factor` is:
- `immediate`: 1.5
- `near`: 1.0  
- `far`: 0.5

The dot product captures "how much does this event matter to me given my frame." High alignment (positive or negative) → high salience.

### §5.5 Causal graph and provenance

`CAUSAL_GRAPH` is a directed acyclic graph (in practice — cycles are bugs). Edges go from cause to consequence. Walking backward from any Key produces the causal chain. Walking forward produces the cascade of consequences.

For the player diagnostic UI, this graph powers "why did X happen?" queries. The engine returns the chain of Keys leading to X, with visibility filtered to what the player's character could observe.

For the simulation harness (Stage 10 verification), this graph powers property-test assertions: *"in 8 seasons, did any Key-chain produce a cycle?"*, *"which Key types most frequently lead to Conviction crises?"*, etc.

### §5.6 Replay and save-state

A complete game state is `(initial_state, KEY_LOG)`. Replay:

```
state = initial_state
for key in KEY_LOG:
    state = on_key_emitted(state, key)
```

Determinism requires the rule and validators to be pure functions of `(state, key)`. Random elements (DA dice rolls, etc.) are recorded in the Key payload itself, not regenerated at replay.

Save = serialize KEY_LOG. Restore = deserialize and replay (or skip to checkpoint and forward).

### §5.7 Lifecycle states

A Key's lifecycle:

1. **Drafted** — type set, payload populated, but not emitted (e.g., a DA in player consideration; not yet committed)
2. **Emitted** — committed to log; observer set computed; interpretations applied
3. **Persistent** — past events with `permanence > transient`; remain in observer Memory and CAUSAL_GRAPH
4. **Decayed** — Memory salience reached 0; Key remains in log but no longer surfaces in NPC reasoning
5. **Pruned** — only for `transient` events past their time_horizon; removed from log

Pruning is for performance; persistent and indelible Keys are never pruned.

---


## §6 Integration with Existing Systems

### §6.1 PP-686 faction architecture

PP-686 (Faction Behavior Architecture) becomes a Key consumer. The four-piece architecture maps to Key consumption:

| PP-686 component | Key types consumed | Effect |
|---|---|---|
| Mission outcome scoring | `da_outcome.*` | Each DA Key with mission_alignment payload contributes to Mission delivery score |
| Cascade resolution | `state.succession`, `state.scar_acquired` (leader), `mechanical.cascade_resolution` (self-emit) | Triggers re-resolution; emits update Keys |
| Public Expectation | `da_outcome.*`, `state.coup_attempted`, `env.*` | Updates strictness based on observed faction behavior |
| Legitimacy / Popular Support | `da_outcome.*` (success/failure), `state.scar_acquired` (leader), `env.peninsular_strain_shock` | Standard ΔL/ΔPS update rule per PP-686 §3.4-3.5 |

**Resolution of PP-686 audit findings:**

- **P1-3 DA category schema**: `da_outcome` subtypes (per §4.1) provide the canonical category enumeration. PP-686's mission_aligned_categories sets reference these subtypes.
- **P2-1 NPC behavior coupling**: NPC autonomous behavior reads its own Memory (Key references) through its armature. The armature *can* be either personal_convictions-based or effective_convictions-based depending on context — both are stored on the NPC, both can interpret the same Keys. Context flag (e.g., "this is a faction-role action vs a personal-time action") chooses which armature is consulted.
- **P2-3 Strain interaction**: `env.peninsular_strain_shock` Keys are emitted by the strain subsystem; PP-686's public temperament reads these to adjust Popular Support.
- **Lateral peer-system gaps**: peer systems all become Key emitters/consumers; coupling is uniform.

### §6.2 PP-684 Conviction taxonomy

The 12-Conviction taxonomy (with 4-axis vectorization) is the substrate Keys use for symbolic_dimensions. Conviction → axis matrix (§3.4) is canonical authoring. Keys emit symbolic projections; armatures interpret via matrix-mediated dot product.

**No conflict.** PP-684 ratifies independently; PP-687 reads from it.

### §6.3 Doc 12 Political Dynamics

Doc 12's procedures rewrite to consume Keys:

- Procedure A (Concern generation): reads memory Keys filtered by salience and Conviction-relevance.
- Procedure B (Project advancement): emits scene_event Keys for actions taken; reads outcome Keys.
- Procedure C (Project completion): emits state_transition Keys.
- Procedure D (Disposition update): consumes scene_event and da_outcome Keys.
- Procedure E (Knowledge sharing): emits scene.dialogue Keys with knowledge payload.

The current procedures' bespoke event records are renamed to Key references. No mechanical changes.

### §6.4 Personal-scale systems

- **Conviction Track** (`conviction_track_v1.md`): Scar triggers consume `scene.witness` Keys with thread-event subtype payload; emit `state.scar_acquired` Keys.
- **Threadwork**: thread operations emit `scene.thread_operation` Keys; consumers (NPCs, Memory, Conviction triggers) read them.
- **Fieldwork / Knot system**: knot formation emits `meta.knot_formed`; rupture emits `meta.knot_ruptured`. Bonds-≥-5 prerequisite checked against accumulated Keys.

### §6.5 Scene-scale systems

- **scene_slate**: scene activation emits `mechanical.scene_activated`; events within scenes emit `scene.*` Keys.
- **social_contest** (with PP-683 Persuasion Track signed −5..+5): each exchange emits `scene.dialogue` Key with persuasion_track_displacement payload.
- **mass_battle**: battle resolution emits `scene_outcome.battle_concluded` with casualty and territorial_outcome payload; phase events emit `scene.*` Keys.

### §6.6 Strategic-scale systems

- **Domain Actions**: DA submission emits `scene.draft_da` Key; resolution emits `da_outcome.*` Key; consequences propagate via standard rule.
- **Faction state**: PP-686 components emit Keys when state changes (Mission shift, Cascade re-resolution, Legitimacy/PS thresholds crossed).
- **Turmoil**: Strain accumulation emits `env.peninsular_strain_*` Keys.

### §6.7 Cross-scale infrastructure

- **scale_transitions**: scale-bridge events emit Keys with multi-scale `scale_signature` lists.
- **The 16-Accounting trace** (per PP-666 / SIM-F): the trace becomes a forward walk of the CAUSAL_GRAPH from a Key in scene-scale to whatever peninsula-scale consequences arose.

### §6.8 Godot implementation

Keys map cleanly to Godot Resources:

- `Key` is a base Resource subclass.
- Per-type subclasses extend with type-specific payload schemas.
- The Key registry is a `KeyTypeRegistry` autoload.
- The Key log is a `Resource` with a typed array of Keys.
- The CAUSAL_GRAPH is built from Key references; can use Godot's built-in graph utilities or a custom AStar2D.
- Save/restore = serialize the Key log Resource.

This is the cleanest mapping any Valoria mechanic has to Godot's type system — Keys are *built* for Resource representation.

### §6.9 Phase 5a (early implementation, per workplan v3 addendum)

PP-687 substantially **simplifies** Phase 5a. The first Godot scene (Wager arc per addendum §C, Track 3) becomes:

- Scene initialization emits a `scene.contest_initiated` Key with Wager-relevant payload.
- Each exchange emits a `scene.dialogue` Key.
- Resolution emits `scene_outcome.contest_resolved`.
- Outcome propagates to Disposition / Standing via standard rule.
- Sim-vs-engine parity test (addendum C3.5) = run same Key sequence in TTRPG sim and Godot scene; verify state changes match.

Phase 5a effort estimate may *drop* from 5 sessions to 3-4 because Keys give the engine its event-handling layer for free.

---

## §7 Migration Plan

### §7.1 Sequence

| Stage | Task | Effort |
|---|---|---|
| 1 | Author `designs/architecture/key_substrate_v30.md` codifying §3 + §5 | 1 session |
| 2 | Author `designs/architecture/key_type_registry_v30.md` enumerating all initial Key types | 1 session |
| 3 | Author Conviction → axis matrix (§3.4) — 12 × 4 = 48 entries | 0.5 session |
| 4 | Update doc 12, doc 08 to reference Keys instead of bespoke events | 1 session |
| 5 | Update conviction_track_v1, threadwork, fieldwork to use Keys | 0.5 session |
| 6 | Update scene_slate, social_contest, mass_battle to emit/consume Keys | 1 session |
| 7 | Update PP-686 spec (faction architecture) to read Keys per §6.1 | 0.5 session |
| 8 | Update glossary, canonical_sources.yaml, supersession_register.yaml | 0.3 session |
| 9 | Run integration sim: emit a multi-scale Key sequence, verify all consumers respond correctly | 1 session |
| 10 | Stage 10 verification: full property-test battery on Key chains | 1-2 sessions |
| **Total** | | **7-9 sessions** |

### §7.2 Backward compatibility

Existing canon documents reference event channels by current name (e.g., "the EventImpact Matrix"). Rather than rewrite all references, introduce alias notes:

```yaml
# references/alias_registry.yaml
- canonical_term: Key
  legacy_terms:
    - EventImpact (doc 08)
    - "event record" (doc 12 procedures)
    - Memory record (NPC schema)
    - Conviction Scar trigger event
  notes: "Universal event substrate per PP-687; legacy terms refer to specific Key types"
```

Existing `EventImpact` references in doc 08 read forward to the Key prototype.

### §7.3 Phased rollout

- **Phase A (immediate, 2-3 sessions):** Stages 1-3. Substrate authored; type registry populated; matrix authored. No system migration yet.
- **Phase B (per existing system, 4-5 sessions):** Stages 4-7. Each consumer system migrated to Keys, one at a time. Existing tests verify no regression.
- **Phase C (verification, 2 sessions):** Stages 9-10. Integration sim + property-test battery.

Phase A delivers the substrate even if migration stalls. Phase B can be paused between consumers without breaking the engine.

### §7.4 Risk mitigation

- **Schema design risk:** §3.1 schema review by Jordan before Stage 1 commit. If schema is wrong, fix is cheaper now than after Phase B.
- **Performance risk:** ~35 NPCs × multiple Keys per season = manageable for Godot. High-frequency scene Keys may need batching. Address in Phase C if surfaced.
- **Migration risk:** Each Phase B stage is independent; rollback per-stage is possible.
- **Authoring overhead risk:** initial Key registry has ~25-30 types. New Key types are Class B extensions, not Class A — low ratification cost.

### §7.5 Deprecation

```yaml
# canon/supersession_register.yaml
- id: SUPERSESSION-PP687-001
  superseded: "doc 08 §1 EventImpact"
  superseder: "designs/architecture/key_substrate_v30.md (Key universal schema)"
  reason: "EventImpact generalized to universal Key substrate"
  
- id: SUPERSESSION-PP687-002
  superseded: "Bespoke event records in doc 12 procedures A-E"
  superseder: "Key references"
  reason: "Procedures rewrite to consume Keys"
  
- id: SUPERSESSION-PP687-003
  superseded: "NPC Memory record schema (per npc_behavior_v30)"
  superseder: "Memory as Key references with per-NPC salience"
  reason: "Memory becomes derived from Key log"
```

---

## §8 Vetting Block (per PP-674 framework)

```yaml
vetting:
  class: A
  necessity: pass
  omega: pass
  mu: [Μ-α, Μ-β, Μ-γ, Μ-δ]      # all 4 modes served
  m_ratings:
    M-1: "+"     # extends — universal event substrate is new continuous-pressure substrate
    M-2: "○"     # neutral
    M-3: "+"     # extends — Keys carry symbolic dimensions in shared axis space
    M-4: "+"     # extends — institutional postures expressed via Key emission patterns
    M-5: "+"     # extends — Keys with multi-scale signatures are scale-bridges
    M-6: "+"     # extends — every cross-scale strategic action emits Keys
    M-7: "+"     # extends — Keys give canonical structure for autonomous-agent composition
    M-8: "+"     # extends — Keys are the public-substrate channel for institutional signaling
    M-9: "+"     # extends — Key log IS the state-evolution record
    M-10: "✓"    # consistent
    M-11: "+"    # extends — provenance chains are external modulators on every interpretation
  q: pass
```

### N — Necessity (full justification)

Renaissance political and intellectual systems all wrestle with the *transmission of event significance* — how an event becomes news, becomes interpretation, becomes consequence, becomes precedent. The Florentine *cronache* tradition (Compagni, Villani) recorded events as causal chains; the chronicle form is itself a Key log with provenance. The Council of Constance's resolution of the Schism turned on legitimacy claims that traced through specific Key-chains: Urban VI's election conditions → Council legitimacy → conciliar authority. This is exactly the diagonal-chain causality Keys encode.

Subject-matter grounding (load-bearing in source material):

- **Florentine cronache and ricordanze:** these family chronicles maintained year-by-year event records with explicit causal annotations. Buonaccorso Pitti, Gregorio Dati, Giovanni Morelli all wrote in this form. The records were used for legal claims, marriage negotiations, political positioning — the chronicle was *active substrate*, not passive history. Keys map directly to this practice.
- **Italian merchant correspondence:** Datini's archive (~150,000 letters) demonstrates that long-distance trade required exactly the structured event-record format Keys propose. Each letter encoded source, recipients, transaction, observers, and (often) causes. The economic substrate of Renaissance Italy ran on Key-equivalents.
- **Papal curia event registries:** the Vatican Apostolic Library's *registra* preserved structured records of every consequential papal action with witnesses, scope, and provenance. Used for canon law adjudication centuries later. Indelible-permanence Keys with public visibility.
- **Tudor State Papers:** Cecil's archive at Hatfield maintained structured records of intelligence reports, diplomatic correspondence, and policy decisions. Each document carried metadata equivalent to Key fields — source, observers, scope, time horizon.

The Renaissance *invented* structured event records as the substrate for political and economic consequence. Keys are not a fantasy imposition; they are how the period actually operated.

Existing-mechanic coverage check: doc 08's EventImpact, doc 12's bespoke event handling, NPC Memory records, Conviction Scar triggers, scene event flows, mass_battle events — all are partial instances of the universal Key pattern. Each is currently authored separately; consolidation is overdue.

Failure-mode check:
- *Fantasy imposition:* No. Directly grounded in Renaissance documentary practice.
- *Duplicate coverage:* No. Replaces multiple partial implementations with single substrate.
- *Edge case:* No. Universal substrate is the central engine architecture.
- *Abstractable:* No — this *is* the abstraction. The thing being abstracted is the event-substrate itself.

**N PASSES.**

### Ω — Intent (full)

| Clause | Assessment |
|---|---|
| **Ω-a** Strategic actions produce cross-scale traceable-but-unanticipatable consequences | **Defining.** The CAUSAL_GRAPH is exactly this property. Trace is queryable; full prediction is impossible because Keys cascade through autonomous armature interpretations. |
| **Ω-b** Personal-layer confrontation transforms character through substrate | **Strong.** Conviction Scar Keys are personal-layer transformation events; Threadwork Keys propagate through personal substrate. |
| **Ω-c** Autonomous agents generate consequential events independent of player | **Defining.** NPCs autonomously emit scene_event and state_transition Keys based on their own Procedures. Player observes; player does not control. |
| **Ω-d** No strategy produces dominance — every action pays what it buys | **Strong.** Each Key emission consumes resources (action economy, exposure, attention). No free Keys. |

**Ω PASSES.**

### Μ — Modes served

All four primary modes:

- **Μ-α (pressure as engagement driver):** Keys arrive continuously; the engine is always processing the log.
- **Μ-β (autonomous agent composition):** NPCs emit Keys autonomously per their Procedures.
- **Μ-γ (substrate ontology):** Keys ARE the substrate channel. Not metaphorically; literally.
- **Μ-δ (cross-scale consequence):** multi-scale `scale_signature` is core schema.

No Μ undermined. **All four modes served.**

### М — Meta-throughlines

10 of 11 patterns extended; 1 neutral. No contradictions. See vetting block above.

### Τ — Throughlines

Load-bearing:
- T-04 institutional decay → Keys carry the chain of institutional events
- T-08 information asymmetry → visibility field encodes who knows what
- T-09 legitimate vs effective authority → Key chains distinguish *what happened* from *what was said*
- T-15 the persuasive populace → audience Keys aggregate
- T-23 succession cascade → succession events emit Keys consumed by Cascade
- T-27 effects real, explanation wrong → the same Key produces different interpretations across NPCs with different armatures
- T-31 institutional posture shifts under leadership → Cascade re-resolution emits Keys
- All others composable; no breaks.

### Q — Quality

**Q-robust.** Authoring inputs are bounded: ~25-30 Key types initially; per-type schemas; Conviction → axis matrix (48 entries). Subsequent type additions are Class B (low ratification cost). Player customization: scenarios are Key sequences; modding is Key emission. Variety: every player choice composes through Keys, producing distinguishable consequence chains.

**Q-smooth.** Single substrate replaces N×N pair-couplings. Memory schema is unified. Save/restore is Key log serialization. Godot Resource mapping is direct. Scale-zoom: Keys carry scale_signature explicitly; no per-pair zoom rules needed. Calculation methodology consistent: dot products, observer set computation, log append — same primitives across all systems.

**Q-elegant.** One substrate. One update rule. The schema *is* the abstraction; nothing is hidden. Player intuits "what's happening" by walking the Key log; "why it happened" by walking the CAUSAL_GRAPH. Authors write scenarios as Key sequences. The architecture's primary virtue is that *nothing else needs to be built* — derived features (replay, mod, diagnostic) emerge.

**Q PASSES.** This is the most elegant single architectural decision the project has made.

---


## §9 Open Questions for Decision

Items requiring Jordan call before this proposal can be ratified:

1. **Schema sign-off.** §3.1 universal Key fields. The proposal lists 11 top-level fields; any field deemed superfluous, missing, or mis-shaped must be flagged before implementation begins. Schema is the load-bearing piece.

2. **Type registry initial scope.** §4.1 lists 7 type families. Any missing? (Candidates not in initial registry: economy events? religious observances at sub-DA scale? rumor propagation as separate from scene.dialogue?)

3. **Conviction → axis matrix authoring.** §3.4 provides illustrative values for the 48-entry matrix. Are 4 axes the right number? More? Different axes? Calibration timing?

4. **Visibility list authoring burden.** Each Key must specify visibility. For autonomous events (NPC actions in private), the engine computes default visibility; for authored events (scenarios), authors specify. Acceptable? Or should visibility be derived purely from scene-presence and scale?

5. **Memory salience formula (§5.4).** The dot-product formula is provisional. Calibrate at Stage 10, or prefer different functional form now?

6. **Causal graph storage cost.** A multi-season game accumulates many Keys. Pruning rules (§5.7) prune transient; persistent and indelible accumulate. After 30 seasons, ~20-50 Keys per faction × 6 factions × 30 seasons = 3,600-9,000 Keys. Manageable. But: should there be a memory-management policy beyond `transient` pruning? (E.g., compress old Keys to summary records after 10 seasons?)

7. **Phased rollout vs hard cutover.** §7.3 proposes 3-phase rollout. Alternative: hard cutover where all systems migrate simultaneously. Higher risk, possibly faster. Which?

8. **Naming.** "Key" is the proposed term. Alternatives: Event, Record, Atom, Signal, Trace. Each has tradeoffs. Stay with Key, or pick another?

9. **Relationship to PP-686 ratification.** Sequencing: PP-687 ratifies first, PP-686 references it, both implement. Alternative: parallel development with explicit interface contract. Which?

10. **Stage 10 verification scope.** §7 lists property-test battery. Specific properties to test: cycle-freeness in CAUSAL_GRAPH; salience monotonic decay; visibility correctness; replay determinism. Comprehensive list?

---

## §10 Anticipated Audit Concerns

(Self-anticipating audit findings; the proposal is intentionally drafted to address these inline.)

| Likely audit finding | Pre-resolution |
|---|---|
| Schema design risk | §9 #1 explicit Jordan sign-off; Stage 1 review checkpoint |
| Performance / scale | §7.4 risk mitigation; expected ~3,600-9,000 Keys per game; Phase C verification |
| Migration scope | §7.3 phased rollout; per-system independence; rollback per stage |
| NPC behavior coupling (P2-1 from PP-686) | §6.1 explicit resolution; both armatures coexist |
| Lateral peer-system gaps (PP-686 audit) | §6 explicit per-system integration |
| Diagonal opacity (E-DIAG-A) | CAUSAL_GRAPH walks provide diagonal trace |
| Player legibility of Key sequences | UI-level concern; Phase 5a Godot scope; not in this proposal |
| Modding interface (out of scope) | Documented as automatic byproduct; explicit modding spec deferred |
| Authoring overhead for Key registry | §7.4: ~25-30 initial types; new types are Class B |
| Backward compatibility | §7.2 alias_registry handles transition |

---

**End proposal.** PP-687 ready for review.

---

## Document outline (for navigation)

- §0 Abstract
- §1 Motivation (cross-system gaps; Memory schema; doc 08 prototype; PP-686 audit findings; player benefits; modding)
- §2 Design Goals
- §3 Key Schema (universal fields, semantics, axis-space integration, structured-NPC compatibility)
- §4 Key Type Registry (taxonomy, per-type schemas, registry as canon)
- §5 Update Rule and Lifecycle (single rule, observer resolution, Memory as Key reference, salience, causal graph, replay, lifecycle states)
- §6 Integration with Existing Systems (PP-686, PP-684, doc 12, personal-scale, scene-scale, strategic-scale, cross-scale, Godot, Phase 5a)
- §7 Migration Plan (sequence, backward compat, phased rollout, risks, deprecation)
- §8 Vetting Block (per PP-674 framework with full N/Ω/Μ/М/Τ/Q justification)
- §9 Open Questions
- §10 Anticipated Audit Concerns

