<!-- STATUS: ANALYSIS — review of existing canon (PP-687/686/688). Cites canon; edits none. -->
# 00 — Key I/O & World-State Propagation (Review)

How a Key receives input and generates output — i.e. how a consequential change propagates through Valoria's world state. Source of truth: `designs/architecture/key_substrate_v30.md` (PP-687), `key_type_registry_v30.md`, `scale_transitions_v30.md`, `references/module_contracts.yaml`.

## 1. The Key, in one line

A **Key** is a typed, validated, append-only event record — the *single* event substrate for the engine. Every consequential change is a Key; every system both emits and consumes Keys. Universal fields (substrate §2): `id`, `type`, `source_actor`, `emitted_at {season_index, sub_step_index}`, `causes[]`, `targets[] {actor_id, role, impact_vector, stat_deltas}`, `scale_signature[]`, `symbolic_dimensions`, `visibility`, `time_horizon`, `permanence`, `payload`. Registry: 7 families, 44 registered types (`key_type_registry_v30.md` §9).

## 2. IN → resolver → OUT

```
                 ┌─────────── module contract (module_contracts.yaml) ───────────┐
   prior Keys ──▶│  consumes[]  ──▶  resolver  ──▶  emits[]  (+ state writes)     │──▶ new Keys
                 └───────────────────────────────────────────────────────────────┘
```

**IN (the "Key IN" side).** Each system is wrapped as a module declaring `consumes: [{type, from}]`. When a Key of a subscribed type is appended, the consuming module's callback fires (substrate §4.1 step 5). Modules are matched to one of seven **resolver archetypes** (`module_contracts.yaml`, 37 resolver declarations):

| Resolver | Role |
|---|---|
| `dice_pool` | d10 sigma-leverage pool roll (combat, social_contest, mass_battle) |
| `d_sigma` | continuous sigma-leverage engine |
| `deterministic_accounting` | ledger procedures + sequencing (faction_state, npc_behavior) |
| `clock_advance` | threshold/segment clocks (MS, CI, victory) |
| `armature_dot_product` | NPC interpretation via Conviction-axis projection |
| `state_reader` | read-only inspection (npc_memory) |
| `manifest` | degenerate/no-roll (terminal clocks) |

**The single update rule (substrate §4.1).** This is the *only* path that mutates engine state:

```
on_key_emitted(key):
  validate(key)                      # registry + universal invariants (§2.3)
  KEY_LOG.append(key)                # immutable
  observers = source_actor ∪ targets[].actor_id
            ∪ actors_in_scale(scale_signature) if visibility.public
            ∪ semi_public_observers ∪ private_observers
  for o in observers:                # OUT, per observer
    interp   = o.armature · key.symbolic_dimensions · key.impact_vector[o]
    salience = clamp(|interp| · horizon_factor, 0, 3)
    o.memory.record(key.id, salience)
    o.apply_state_changes(interp, key.stat_deltas)
  for sys in TYPE_SUBSCRIPTIONS[key.type]:  # cross-system propagation
    sys.consume(key)                 # O(1) or async
  for c in key.causes:               # causal graph + awareness
    CAUSAL_GRAPH.add_edge(c, key.id)
    KEY_LOG[c].awareness = clamp(+0.1, 0, 1)
```

**OUT (the "OUT" side).** A Key emits state change two ways:
1. **Direct `stat_deltas`** applied to each target, under strict **bucket discipline** (`derived_stats_v30.md` §1): `pool` (only changed by resolution), `derived_value` (computed; *A5 violation to write directly* — route the delta through the substrate), `track` (linear accumulators: beliefs, concerns, Piety/Persuasion tracks), `clock` (threshold trackers: MS, CI, IP).
2. **Cross-scale propagation** via **Domain Echo** (`scale_transitions_v30.md` §3): a personal-scale Key meeting "Sufficient Scope" emits a faction-scale child Key (degree → ±stat), chained by `causes[]`. §12 specifies all-directions delivery (bottom-up, lateral, top-down, diagonal) via observer resolution + explicit `targets[]` + `scale_signature` inclusion.

## 3. Closure guarantees

The contract surface is machine-checked by `valoria-module-adjudicator` (checks A1–A12): emit-closure (A2: every emitted type registered), consume-closure (A3: every consumed type produced by some module or engine), orphan detection (A4), derived-write guard (A5), cross-scale-edge → transition handoff (A6), undamped/unbounded loop ban (A7), gate/derivation/accounting-phase validity (A10–A12). This is what makes the substrate *closed*: no Key type is consumed that nothing produces, and no derived value is written off-substrate.

## 4. Worked trace (prose)

A PC wins a social contest. `social_contest` (resolver `dice_pool`) consumes `state.opinion_revised`, resolves a sigma-leverage roll, and emits `scene.contest_resolved` (+ `scene.dialogue`) with `targets[]` = the NPC (role `subject`), `stat_deltas: {persuasion_track: +3}`, and an `impact_vector` across the Conviction axes. Propagation: the NPC (observer) interprets via its armature, records the moment in memory at a salience set by `time_horizon`, and applies the track delta. Subscribers fire: `npc_behavior` runs its disposition procedure; if disposition crosses a Sufficient-Scope threshold with a faction officer, a **Domain Echo** child Key `state.standing_change` (`stat_deltas: {Mandate: +1}`, `causes: [contest_key]`, `scale_signature: [territory, personal]`) is emitted and consumed by `faction_state`. One personal beat has propagated to faction state, with the full causal chain recorded.

## 5. The reframe that the rest of the bundle uses

The Key log is a normalized **narrative graph**: nodes = actors / factions / territories / artifacts; edges = Keys, foreign-keyed by `targets[]` and `causes[]`. This is structurally identical to Dwarf Fortress's `history_event` model (see `02_…`), where "the narrative is the traversal path through the graph." It is the substrate on which the legibility layer (`01_…`) and the realizer (`03_…`) operate: the engine already records *what happened* with full provenance — the open problem is rendering it.
