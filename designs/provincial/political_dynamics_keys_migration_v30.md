<!-- [PROVISIONAL: 2026-05-01 — PP-687 Phase B Stage 1: doc 12 procedures consume Keys] -->
<!-- STATUS: PROVISIONAL — Class A migration spec. Wraps designs/audit/2026-04-28-political-dynamics-session/12_development_specification.md (the canonical "doc 12") and specifies the deltas required to consume PP-687 Keys. Does not rewrite the 109k-character source spec; instead enumerates per-procedure input/output changes anchored to source line numbers. -->
<!-- AUTHORITY: PP-687 §8.3 / faction_behavior_v30 §6.2 Stage 1 -->

# Doc 12 Procedures — Key-Migration Spec (PP-687 Phase B Stage 1)
## Status: CANONICAL

**Source spec:** `designs/audit/2026-04-28-political-dynamics-session/12_development_specification.md` (v1.2.2; 1875 lines; Procedures B/C/D/E + DA Proposal Phase + Real-Time Mood).

**Companion:** `designs/architecture/key_substrate_v30.md` §4 (update rule), §8.3 (this migration), §10 (Class B extensions); `designs/architecture/key_type_registry_v30.md`.

---

## §1 Procedure-Naming Reconciliation

The substrate spec PP-687 §8.3 refers to "Procedures A–E"; the canonical doc 12 has Procedures B–E (Procedure A was eliminated in session 09 — see `09_integration_test_streamlined.md`). This migration spec uses the canonical doc 12 naming. The mapping:

| Substrate §8.3 reference | Canonical doc 12 procedure | Section |
|---|---|---|
| "Procedure A — Concern generation" | **Procedure B — Concern Generation and Resolution** | doc 12 L1127 |
| (no equivalent; intermediate phase) | **DA Proposal Phase** (between B and C) | doc 12 L1228 |
| "Procedure B — Project advancement" | **Procedure C — Project Advancement** | doc 12 L1310 |
| "Procedure C — Project completion" | (handled within Procedure C, L1340) | doc 12 L1340 |
| "Procedure D — Disposition update" | **Procedure D — Opinion Drift** | doc 12 L1411 |
| "Procedure E — Knowledge sharing" | **Procedure E — Off-Screen Interactions** | doc 12 L1463 |

This document refers to procedures by the canonical doc 12 names below.

---

## §2 Migration Architecture

### §2.1 What stays

- Per-NPC data structures (Concerns, Projects, Opinions, Memories, Knowledge) per doc 12 §2.
- Armature computation (doc 12 §3) — NPC-level interpretive substrate.
- Real-Time Mood (doc 12 §6.1).
- Procedural logic flow within each procedure.
- All PATCH revisions (v1.2.1 NERS cleanup, v1.2.2 INT-3.1) carry forward unchanged.

### §2.2 What changes

1. **Event-source replacement.** `last_season.events` (doc 12 L1165) is replaced with a Memory Query API call (`key_substrate_v30.md` §4.4) that returns Keys filtered by axis-relevance to the NPC's `armature_position_personal`.

2. **Memory record schema.** Per-NPC Memories (doc 12 §2.6) become per-NPC references to Keys with salience overlay, per substrate §4.3. The bespoke Memory schema (timestamp, event_type, participants, affect, salience, detail) survives in semantic content but is wrapped as a Key reference + per-NPC salience field.

3. **Outcome emissions.** Procedures that previously created bespoke Memory records (B-Resolution, C-Completion, D-Drift, E-Interaction) now also emit Keys to the universal log; per-NPC Memory salience is set on Key emission per substrate §4.4.

4. **Class B extensions.** Three new Key subtypes are required to faithfully encode procedure-specific outputs (§5).

### §2.3 Schema bridge

```python
# Bridge from doc 12 Memory schema to PP-687 Key reference
class MemoryReference:
    key_uuid: str                # references Key.uuid in universal log
    salience: float              # per-NPC salience [0, 7], decays per doc 12 §2.6
    salience_floor: float        # PATCH v1.2-25, evidence_memory_refs guard
    
    # Backward-compat read-through accessors:
    @property
    def timestamp(self): return Key.lookup(self.key_uuid).emitted_at
    @property
    def event_type(self): return Key.lookup(self.key_uuid).type
    @property
    def participants(self): return Key.lookup(self.key_uuid).targets
    @property
    def affect(self): return Key.lookup(self.key_uuid).payload.get('affect', 0)
    @property
    def detail(self): return Key.lookup(self.key_uuid).payload.get('detail', '')
```

Existing doc 12 code that reads `memory.affect` / `memory.event_type` / etc. continues to function via accessors. The 10-Memory cap (doc 12 §2.6 + L1218) becomes a 10-MemoryReference cap; the Key log itself is unbounded.

---

## §3 Procedure B — Concern Generation and Resolution

**Source:** doc 12 L1127–1226.

### §3.1 Input change (Generation phase, L1163–1185)

```diff
- For each event in last_season.events:
-     For each NPC in event.affected_npcs:
-         if not npc_observes_event(npc, event):
+ For each NPC in active_npcs:
+     # PP-687 Memory Query: axis-relevant Keys this season
+     candidate_keys = memory_query(
+         npc_id=npc.id,
+         time_window=(current_season - 1, current_season),
+         axis_relevance_threshold=0.3,                   # tunable; default 0.3
+         armature_position=npc.armature_position_personal,
+         include_knowledge_keys=False,                   # Knowledge handled separately L1182
+     )
+     # Visibility gate per Key payload (PP-687 §3 visibility model)
+     candidate_keys = [k for k in candidate_keys if key_visible_to(k, npc)]
+     for key in candidate_keys:
          # Concern regeneration cooldown (PATCH 3.1 / N-BOT-C)
-         potential_tag = derive_concern_tag(event, npc.armature)
-         if potential_tag in npc.concern_history and event.salience < 4:
+         potential_tag = derive_concern_tag(key, npc.armature)
+         if potential_tag in npc.concern_history and key.salience < 4:
              continue
-         concern = generate_concern(npc, event, event_impact_matrix)
+         concern = generate_concern(npc, key, event_impact_matrix_for(key))
          npc.concerns.append(concern)
```

`memory_query()` is the substrate Memory Query API (substrate §4.4). It filters by:
- Time window (current_season − 1 to current_season): catches all this-season Keys.
- Axis-relevance: `cosine_similarity(key.symbolic_dimensions, npc.armature_position_personal) >= 0.3`. Tunable.
- Visibility per substrate §3 (default-from-scene-presence; explicit override via Key.visibility field).

### §3.2 Output change (Resolution phase, L1187–1226)

When Concern resolves with `subject_npc_id` set (L1209), Procedure B currently creates a bespoke Memory record. Migration: emit a Class B Key first, then create the MemoryReference.

```python
# After: resolution = resolve_concern(npc, concern)
if resolution.subject_npc_id:
    # PP-687: emit state.concern_resolved Key
    key = emit_key(
        type='state.concern_resolved',                  # Class B (§5.1)
        emitted_by=npc.id,
        targets=[npc.id, resolution.subject_npc_id],
        payload={
            'concern_tag': resolution.tag,
            'affect': resolution.implied_affect,
            'belief_revision': resolution.causes_belief_revision,
        },
        scale_signature='personal',
        symbolic_dimensions=project_to_axes(npc, resolution),
        visibility={'private_observers': [npc.id, resolution.subject_npc_id]},
    )
    # Then: create per-NPC MemoryReference pointing to that Key
    add_memory_reference(npc, key.uuid, salience=resolution.salience)
```

**Belief revision emission (L1196–1206).** Belief revision currently mutates `npc.beliefs` and increments scar counts. Migration: also emit `state.belief_revised` Key (already declared as Class B in PP-688 §6 / substrate §10).

```python
if resolution.contradiction_strength == "strong":
    emit_key(
        type='state.belief_revised',                    # Class B (PP-688 §6.3)
        emitted_by=npc.id,
        targets=[npc.id],
        payload={
            'belief_id': resolution.target_belief.id,
            'prior_belief': resolution.target_belief.value_before,
            'revised_belief': resolution.target_belief.value_after,
            'contradiction_strength': 'strong',
            'scar_generated': True,
        },
        scale_signature='personal',
    )
```

### §3.3 Knowledge-triggered Concerns (L1181–1185)

```diff
  For each Active NPC:
-     For each Knowledge in npc.knowledge with salience >= 4:
+     # Knowledge stays in npc.knowledge per doc 12 §2.7;
+     # not migrated to Keys at Stage 1 (Knowledge is a separate ontology).
+     For each Knowledge in npc.knowledge with salience >= 4:
          if knowledge contradicts any active Belief domain:
              generate Concern("Is [Belief] accurate given Knowledge X?")
```

Knowledge is preserved as a doc-12-internal data structure; not migrated to Keys at Stage 1. Stage 1 explicitly does NOT touch Knowledge. (Future stage may unify Knowledge with the Key log; out of Stage 1 scope.)

---

## §4 Procedure C — Project Advancement

**Source:** doc 12 L1310–1410.

### §4.1 Stall + advancement emission (L1316–1337)

Procedure C currently advances Projects without emitting external state. Migration: emit `mechanical_event.project_advanced` Keys per substrate type registry §4.

```python
# After: advance_project(project, mood_modifier)
emit_key(
    type='mechanical.project_advanced',                 # registry §4 (existing)
    emitted_by=npc.id,
    targets=[npc.id],
    payload={
        'project_id': project.id,
        'progress_before': project.progress - delta,
        'progress_after': project.progress,
        'project_domain': project.project_domain,
        'mood_modifier': mood_modifier,
    },
    scale_signature='personal',
)
```

### §4.2 Stall failure (L1319–1322)

```python
if project.seasons_stalled >= 8:
    execute_failure(project, npc)
    emit_key(
        type='state.project_failed',                    # registry §4 (existing)
        emitted_by=npc.id,
        targets=[npc.id],
        payload={
            'project_id': project.id,
            'failure_mode': 'stalled',
            'seasons_stalled': project.seasons_stalled,
        },
        scale_signature='personal',
    )
    generate_replacement_project(npc)
```

### §4.3 Project completion (L1340–1364)

Currently emits two bespoke Memory records per supporter / obstructor. Migration: emit one `state.project_completed` Key first, then per-supporter/obstructor `meta.relational_consequence` Keys (or store as MemoryReferences to the completion Key with relationship-tagged salience).

```python
if project.progress >= 10:
    completion_key = emit_key(
        type='state.project_completed',                 # registry §4 (existing)
        emitted_by=npc.id,
        targets=[npc.id],
        payload={
            'project_id': project.id,
            'project_domain': project.project_domain,
            'completion_effect': project.completion_effect.serialize(),
            'supporters': project.supporters,
            'obstructors': project.obstructors,
            'goal_short': project.goal_short,
        },
        scale_signature='personal',
    )
    
    # Per-supporter/obstructor MemoryReferences to the completion Key:
    for supporter_id in project.supporters:
        add_memory_reference(
            npc, completion_key.uuid,
            salience=4,
            relationship_tag='project_legacy_support',
            affect=+0.5,
        )
    for obstructor_id in project.obstructors:
        add_memory_reference(
            npc, completion_key.uuid,
            salience=4,
            relationship_tag='project_legacy_obstruction',
            affect=-0.5,
        )
    
    generate_new_project(npc)
```

The doc 12 Memory schema's `event_type='project_legacy_support'` / `'project_legacy_obstruction'` becomes a per-NPC `relationship_tag` field on the MemoryReference, since the underlying Key (state.project_completed) is shared but interpretive framing differs per NPC.

---

## §5 Procedure D — Opinion Drift

**Source:** doc 12 L1411–1461.

### §5.1 Input filter unchanged in semantics (L1421–1424)

```diff
- new_memories = filter_memories(npc.memories, 
+ # MemoryReferences point to Keys; filter by Key.targets including subject
+ new_memory_refs = filter_memory_refs(npc.memory_refs,
                                  subject=opinion.subject,
                                  this_season=True)
```

`filter_memories` continues to function via the MemoryReference accessor layer (§2.3). Semantics preserved.

### §5.2 Opinion mutation emission (L1418–1455)

Procedure D currently mutates `opinion.affect_axis` and `opinion.confidence` without emitting. Migration: emit `state.opinion_revised` Class B Key per accounted opinion that crossed a meaningful threshold.

```python
# After all drift application for this opinion:
if abs(opinion.affect_axis_before - opinion.affect_axis_after) >= 0.5 or \
   opinion.confidence_before != opinion.confidence_after:
    emit_key(
        type='state.opinion_revised',                   # Class B (§7.1 below)
        emitted_by=npc.id,
        targets=[npc.id, opinion.subject_npc_id],
        payload={
            'opinion_subject': opinion.subject_npc_id,
            'affect_axis_before': opinion.affect_axis_before,
            'affect_axis_after': opinion.affect_axis_after,
            'confidence_before': opinion.confidence_before,
            'confidence_after': opinion.confidence_after,
            'driver_memory_refs': [m.key_uuid for m in new_memory_refs],
        },
        scale_signature='personal',
        causes=[m.key_uuid for m in new_memory_refs],   # CAUSAL_GRAPH wiring
    )
```

The `causes[]` field wires the opinion revision to the source Keys — supports substrate §5.4 backward causal walk for "why does this NPC now distrust X?" diagnostics.

### §5.3 Cognitive dissonance Concern generation (L1444)

```python
if opinion.confidence >= 3 and contradiction_acute:
    generate_concern_about_subject(npc, opinion.subject)
    if opinion.confidence in [4, 5] and contradiction_acute:
        npc.mood = Distracted
```

Concern generation here continues to use doc 12 Concern schema. The Concern itself is per-NPC state (not a Key); no emission required at this hook.

---

## §6 Procedure E — Off-Screen Interactions

**Source:** doc 12 L1463–1513.

### §6.1 Interaction emission (L1486–1489)

Procedure E currently calls `apply_drift(...)` without emitting external state. Migration: emit `scene.interaction` Class B Key per ambient interaction.

```python
if random() < base_prob:
    interaction = generate_interaction(npc_a, npc_b)
    
    # PP-687 emission
    interaction_key = emit_key(
        type='scene.interaction',                        # Class B (§7.2 below)
        emitted_by='system_mood',                        # off-screen system actor
        targets=[npc_a.id, npc_b.id],
        payload={
            'interaction_type': 'ambient_inner_circle',
            'faction': npc_a.faction.id,
            'shared_conviction_primary': bool(npc_a.conviction_primary == npc_b.conviction_primary),
            'drift_a_to_b': interaction.drift_a,
            'drift_b_to_a': interaction.drift_b,
            'cumulative_drift': abs(interaction.drift_a) + abs(interaction.drift_b),
        },
        scale_signature='personal',
        visibility={'private_observers': [npc_a.id, npc_b.id]},
    )
    
    apply_drift(npc_a.opinion_of(npc_b), interaction)
    apply_drift(npc_b.opinion_of(npc_a), interaction)
```

### §6.2 Knowledge sharing emission (L1491–1499)

Knowledge sharing (`share_knowledge(npc, other, knowledge)`) currently produces a bespoke Memory ("Heard from [npc] that [knowledge.fact]"). Migration: emit `scene.dialogue` Key per substrate registry §3 (existing) with `payload.knowledge_shared = True`.

```python
for npc, other in [(npc_a, npc_b), (npc_b, npc_a)]:
    for knowledge in npc.knowledge:
        if knowledge.salience >= 3 and knowledge.valid:
            if any(other.concern.seeking matches knowledge.fact_tag for concern in other.concerns):
                share_knowledge(npc, other, knowledge)
                
                dialogue_key = emit_key(
                    type='scene.dialogue',               # registry §3 (existing)
                    emitted_by=npc.id,
                    targets=[npc.id, other.id],
                    payload={
                        'dialogue_subtype': 'knowledge_sharing',
                        'knowledge_fact': knowledge.fact_tag,
                        'knowledge_salience_at_share': knowledge.salience,
                        'recipient_concern_match': True,
                    },
                    scale_signature='personal',
                    visibility={'private_observers': [npc.id, other.id]},
                )
                # Recipient gets MemoryReference to the dialogue Key
                add_memory_reference(other, dialogue_key.uuid, salience=knowledge.salience - 1)
```

### §6.3 Gossip propagation (L1502–1504)

```python
if cumulative_drift > 0.5:
    gossip_key = emit_key(
        type='scene.gossip',                             # Class B (§7.3 below)
        emitted_by='system_gossip',
        targets=[npc_a.id, npc_b.id],                   # principals; observer set expands per propagation
        payload={
            'principals': [npc_a.id, npc_b.id],
            'cumulative_drift': cumulative_drift,
            'origin_interaction_key': interaction_key.uuid,
        },
        scale_signature='personal',
        causes=[interaction_key.uuid],
    )
```

### §6.4 Cross-faction Distant Contact (L1507–1510)

```diff
  For each cross-faction pair (npc_a, npc_b) with prior Memory and mutual Opinion |≥1|:
      if random() < 0.10:
          interaction = generate_distant_contact(npc_a, npc_b)
+         emit_key(
+             type='scene.interaction',
+             ...
+             payload={'interaction_type': 'cross_faction_distant_contact', ...}
+         )
          apply_drift_with_decay(...)
```

Same emission pattern as §6.1 with `interaction_type='cross_faction_distant_contact'`.

---

## §7 New Class B Key Type Declarations

Per substrate §10 Class B extension protocol. Three new Class B Key types declared by this Stage 1 migration:

### §7.1 state.opinion_revised

```yaml
type: state.opinion_revised
class: B
declared_by: PP-687 Phase B Stage 1 / political_dynamics_keys_migration_v30
purpose: |
  Emitted by Procedure D when an Opinion's affect_axis changes by ≥ 0.5 or
  confidence value changes. Drives Articulation Tier 2 trigger evaluation.
payload:
  required:
    - opinion_subject: npc_id
    - affect_axis_before: float
    - affect_axis_after: float
    - confidence_before: int [1, 5]
    - confidence_after: int [1, 5]
  optional:
    - driver_memory_refs: [key_uuid]
visibility_default: private_observers=[emitter, opinion_subject]
scale_signatures: [personal]
articulation_significance: stakes_weight 1-3 (per affect delta + confidence change)
```

### §7.2 scene.interaction

```yaml
type: scene.interaction
class: B
declared_by: PP-687 Phase B Stage 1 / political_dynamics_keys_migration_v30
purpose: |
  Emitted by Procedure E for ambient inner-circle interactions and
  cross-faction Distant Contact. Procedure E payload carries drift values
  computed before Opinion mutation (state.opinion_revised emits separately
  if drift threshold crossed).
payload:
  required:
    - interaction_type: enum [ambient_inner_circle, cross_faction_distant_contact, knot_partner]
    - drift_a_to_b: float
    - drift_b_to_a: float
  optional:
    - faction: faction_id
    - shared_conviction_primary: bool
    - cumulative_drift: float
visibility_default: private_observers=[participants]
scale_signatures: [personal]
articulation_significance: stakes_weight 0-1 (low; rarely triggers cut scene unless cumulative_drift > 1.0)
```

### §7.3 scene.gossip

```yaml
type: scene.gossip
class: B
declared_by: PP-687 Phase B Stage 1 / political_dynamics_keys_migration_v30
purpose: |
  Emitted by Procedure E §6.3 when cumulative_drift > 0.5. Generates a
  gossip artifact that may propagate across the inner-circle and reach
  third-party observers.
payload:
  required:
    - principals: [npc_id]                        # interaction principals
    - cumulative_drift: float
    - origin_interaction_key: key_uuid
  optional:
    - propagation_observers: [npc_id]             # filled by gossip propagation logic
visibility_default: semi_public_observers=propagation_observers (initial: principals only)
scale_signatures: [personal]
articulation_significance: stakes_weight 1 (low; multi-hop propagation to articulation only at high cumulative)
```

### §7.4 state.concern_resolved

```yaml
type: state.concern_resolved
class: B
declared_by: PP-687 Phase B Stage 1 / political_dynamics_keys_migration_v30
purpose: |
  Emitted by Procedure B at Concern resolution when subject_npc_id is set.
  Carries the resolution polarity (implied_affect) and whether Belief revision
  followed. (Belief revision itself emits state.belief_revised separately.)
payload:
  required:
    - concern_tag: string
    - affect: float [-3, +3]                      # resolution polarity
  optional:
    - belief_revision: bool                       # true if also emitted state.belief_revised
visibility_default: private_observers=[emitter, subject_npc_id]
scale_signatures: [personal]
articulation_significance: stakes_weight 1-2 (moderate; high-affect concerns approach trigger threshold)
```

These four new Class B types are added to the type registry in a follow-up commit (Stage 1b).

---

## §8 Sequencing within Accounting

Per doc 12 §6.2 ("Accounting Sequence"), procedures fire in order: B → DA Proposal Phase → C → D → E. Migration preserves this sequencing. Within each procedure, all Key emissions occur during procedure execution; the substrate's single update rule (§4.1) processes emissions inline (per substrate determinism guarantee).

```
Accounting boundary (mechanical.accounting Key emitted)
  ├── Procedure B
  │     ├── B.0 Knowledge Decay (no Key emission)
  │     ├── Generation
  │     │     └── memory_query() reads Keys; generates Concerns
  │     └── Resolution
  │           ├── state.concern_resolved Keys emitted
  │           ├── state.belief_revised Keys emitted (if applicable)
  │           └── MemoryReferences created
  ├── DA Proposal Phase
  │     ├── select_proposal() reads Faction Meta-Armature
  │     ├── execute_proposed_domain_actions() emits da_outcome.* Keys (existing)
  │     └── displacement_neglect_observed events emitted as scene.displacement Keys
  ├── Procedure C
  │     ├── mechanical.project_advanced Keys emitted
  │     ├── state.project_failed Keys emitted (if stall ≥ 8)
  │     └── state.project_completed Keys emitted
  ├── Procedure D
  │     └── state.opinion_revised Keys emitted (per drift threshold)
  └── Procedure E
        ├── scene.interaction Keys emitted (per ambient pair)
        ├── scene.dialogue Keys emitted (per knowledge sharing)
        └── scene.gossip Keys emitted (per cumulative_drift > 0.5)
```

---

## §9 Determinism

All Key emissions inherit substrate determinism guarantees (substrate §6):

- Per-emission RNG seed (substrate §4.1 step 4) for any procedure-internal stochastic outcomes (e.g., Procedure E's `random() < base_prob`).
- Stable sort order: when multiple NPCs emit Keys at the same procedure step, ordered by NPC.id ascending (matches doc 12 PATCH v1.2-8 four-level tiebreak determinism precedent).
- All emissions happen synchronously within the Accounting tick; no inter-tick reordering.

Replay determinism: same Key log + same RNG seed → same procedure output → same Key emissions, verified at Stage 8 (Stage 10 sim battery).

---

## §10 Stage 1 Acceptance Criteria

| Criterion | Met by |
|---|---|
| Procedure B reads Memory Keys via Memory Query API | §3.1 |
| Procedure B emits state.concern_resolved on resolution | §3.2 |
| Procedure B emits state.belief_revised on strong contradiction | §3.2 |
| Procedure C emits mechanical.project_advanced on advance | §4.1 |
| Procedure C emits state.project_completed on completion | §4.3 |
| Procedure C emits state.project_failed on stall ≥ 8 | §4.2 |
| Procedure D emits state.opinion_revised on threshold-crossing drift | §5.2 |
| Procedure D wires causes[] for backward causal walk | §5.2 |
| Procedure E emits scene.interaction per ambient pair | §6.1 |
| Procedure E emits scene.dialogue on knowledge sharing | §6.2 |
| Procedure E emits scene.gossip on cumulative_drift > 0.5 | §6.3 |
| 4 new Class B Key types declared | §7 |
| Substrate determinism guarantees preserved | §9 |
| MemoryReference accessor layer preserves doc 12 read-side semantics | §2.3 |

---

## §11 What Stage 1 Does NOT Do

- **Knowledge ontology unification.** Knowledge stays in `npc.knowledge` per doc 12 §2.7; not migrated to Keys at this stage. Future stage may unify.
- **Faction Meta-Armature recomputation.** doc 12 §5.3 + PATCH 2.1 stay unchanged; aggregate is computed over inner-circle as today.
- **Promotion of doc 12 to canonical path.** doc 12 remains in `designs/audit/2026-04-28-political-dynamics-session/` as PROVISIONAL until Stage 10 sim verification. Phase B Stage 1 augments rather than promotes.
- **Mood subsystem changes.** Real-Time Mood (doc 12 §6.1) is unchanged.
- **Articulation Tier 2 calibration.** PP-688 §3.2 significance scoring of new Class B Keys is calibrated at Stage 8 (Stage 10 sim).

---

## §12 Migration Implementation Order

For Phase 5a Godot implementation:

1. Implement substrate Memory Query API (substrate §4.4) — prerequisite.
2. Implement MemoryReference accessor layer (§2.3) — preserves doc 12 read-side.
3. Add 4 new Class B Key types to registry (§7).
4. Modify Procedure B input (§3.1) — first migration step; verify with single-NPC unit test.
5. Modify Procedure B output (§3.2) — verify with `state.concern_resolved` Key in log.
6. Modify Procedure C output (§4) — verify with `state.project_*` Keys.
7. Modify Procedure D output (§5) — verify with `state.opinion_revised` and causes[] wiring.
8. Modify Procedure E output (§6) — verify with `scene.interaction` / `scene.dialogue` / `scene.gossip`.
9. Run Stage 8 (Stage 10) sim battery to validate determinism and behavioral parity.

Estimated Phase 5a scope add: 1.5–2 sessions for full doc 12 migration implementation + verification.

---

## §13 Sign-off

| Item | Status |
|---|---|
| Per-procedure migration delta authored | YES — PROVISIONAL |
| Procedure-naming reconciled with canonical doc 12 (B/C/D/E, no A) | YES — §1 |
| 4 new Class B Key types declared (state.opinion_revised, scene.interaction, scene.gossip, state.concern_resolved) | YES — §7 |
| MemoryReference accessor layer specified | YES — §2.3 |
| Determinism guarantees inherited from substrate | YES — §9 |
| Stage 1 acceptance criteria enumerated | YES — §10 |
| Out-of-scope clearly marked | YES — §11 |

**Stage 1 closed:** PROVISIONAL pending Stage 10 sim verification + Phase 5a Godot implementation.

**Type registry update:** A follow-up Stage 1b commit adds the 4 new Class B types to `designs/architecture/key_type_registry_v30.md` §8 (Class B Extensions section).

---

**End Stage 1 migration spec. PROVISIONAL pending Stage 10 calibration.**
