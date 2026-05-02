<!-- [CANONICAL: 2026-05-01 — PP-687 Key type registry; promoted from PROVISIONAL after Stage 10 sim PASS (12/14 battery; commits bb5e293 lateral + 3cb5207 articulation)] -->
<!-- STATUS: PROVISIONAL — Class A canonical document. Companion to key_substrate_v30.md. -->
<!-- AUTHORITY: PP-687 -->

# Key Type Registry (PP-687)

**Class:** A — substrate-defining canonical document.
**Companion:** `designs/architecture/key_substrate_v30.md`.
**Extension policy:** Adding new types is Class B. Modifying existing types' required-payload fields is a supersession event.

---

## §1 Type Format

Each entry:

```yaml
type_id: <family.subtype>
description: <one-line purpose>
required_payload_fields: [...]
optional_payload_fields: [...]
default_scale_signature: [...]
default_permanence: <transient | persistent | indelible>
default_time_horizon: <immediate | near | far>
emitting_systems: [...]
consuming_systems: [...]
```

Universal Key fields (§2.1 of substrate spec) are required for every type — not repeated here.

---

## §2 Family: scene_event

Personal/scene-scale interactions; observable by scene members.

### scene.dialogue

```yaml
description: Per-scene exchange of speech; advances persuasion or relational state.
required_payload_fields:
  - exchange_count            # int
  - initiator_id              # actor_id
  - topic                     # short string
optional_payload_fields:
  - rhetorical_style_used     # style_id (for Resonant Style)
  - persuasion_track_displacement  # int -5..+5 (PP-683)
  - outcome                   # decisive | compromise | stalemate
  - belief_engagement_for     # {actor_id: aligned/challenging/betraying} (PP-688)
  - inspirations_engaged_for  # {actor_id: [inspiration_names]} (PP-688)
  - knot_partners_present     # [actor_ids] (PP-688)
default_scale_signature: [personal]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [scene_slate, social_contest]
consuming_systems: [npc_behavior, conviction_track, faction_layer, articulation]
```

### scene.witness

```yaml
description: NPC observes an event without participating directly.
required_payload_fields:
  - observed_key_id           # key_id of the observed event
  - witness_actor             # actor_id
optional_payload_fields:
  - thread_event_subtype      # for Conviction Scar triggers
default_scale_signature: [personal]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [scene_slate, npc_behavior]
consuming_systems: [conviction_track, npc_behavior, articulation]
```

### scene.gift

```yaml
description: Material or symbolic transfer between actors.
required_payload_fields:
  - giver_id
  - receiver_id
  - gift_type                 # material | symbolic | obligation
optional_payload_fields:
  - value                     # numeric
  - public                    # bool — performed publicly
default_scale_signature: [personal]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [scene_slate, fieldwork]
consuming_systems: [npc_behavior, faction_layer, articulation]
```

### scene.insult

```yaml
description: Public or private dishonor against an actor.
required_payload_fields:
  - source_actor              # the insulter
  - target_id
optional_payload_fields:
  - severity                  # 1-3
  - witnessed_by              # [actor_ids]
default_scale_signature: [personal]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [scene_slate, social_contest]
consuming_systems: [npc_behavior, conviction_track, faction_layer, articulation]
```

### scene.threat

```yaml
description: Coercive demand against an actor.
required_payload_fields:
  - threatener
  - threatened
  - demand                    # short string
optional_payload_fields:
  - implicit                  # bool
  - severity                  # 1-3
default_scale_signature: [personal]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [scene_slate, social_contest]
consuming_systems: [npc_behavior, conviction_track, faction_layer, articulation]
```

---

## §3 Family: da_outcome

Strategic-layer Domain Action results. These subtypes provide the **Mission alignment categories** that PP-686 references.

### da.public_governance

```yaml
description: Visible administrative or sovereign-role action.
required_payload_fields:
  - faction_id
  - mission_alignment         # bonus | penalty | none
  - outcome                   # success | partial | failure
optional_payload_fields:
  - target_territory_id
  - public_ceremony           # bool
  - role_acting               # true if performed in faction-role context (PP-686 §3.9)
default_scale_signature: [territory]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [da_framework]
consuming_systems: [faction_layer, npc_behavior, articulation]
```

### da.covert_betrayal

```yaml
description: Covert action against ally or stated mission.
required_payload_fields:
  - faction_id
  - target_actor              # actor_id
  - target_faction            # faction_id (or null)
  - exposed                   # bool
optional_payload_fields:
  - exposure_witnesses        # [actor_ids]
  - mission_alignment         # bonus | penalty | none
  - role_acting               # bool
default_scale_signature: [territory]
default_permanence: persistent
default_time_horizon: far
emitting_systems: [da_framework]
consuming_systems: [faction_layer, npc_behavior, articulation, conviction_track]
notes:
  - Visibility flips dramatically based on `exposed`. If false, only source_actor and target_actor know.
  - If exposed=true, exposure_witnesses are added to semi_public_observers and Legitimacy violation event fires.
```

### da.diplomatic_alliance

```yaml
description: Treaty, alliance formation, or formal accord.
required_payload_fields:
  - faction_id
  - counterparty_faction
  - terms                     # short string
optional_payload_fields:
  - witnesses                 # [actor_ids]
  - mission_alignment
  - role_acting               # bool
default_scale_signature: [territory, peninsula]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [da_framework]
consuming_systems: [faction_layer, articulation]
notes:
  - Indelible per Renaissance convention; treaties carry permanent weight even on later abrogation.
```

### da.antinomian_action

```yaml
description: Action that contradicts faction Mission or institutional role.
required_payload_fields:
  - faction_id
  - description
optional_payload_fields:
  - mission_alignment         # always penalty for this subtype
  - role_violation_severity   # 1-3
  - role_acting               # bool
default_scale_signature: [territory]
default_permanence: persistent
default_time_horizon: far
emitting_systems: [da_framework]
consuming_systems: [faction_layer, npc_behavior, articulation, conviction_track]
notes:
  - High Cascade Fidelity divergence; major expectation_weight contribution to PP-688 significance.
```

### da.economic_intervention

```yaml
description: Direct economic action — taxation, market manipulation, sumptuary law, gift to populace.
required_payload_fields:
  - faction_id
  - target_territories        # [territory_ids]
  - intervention_type         # tax | grant | regulation | dispossession
optional_payload_fields:
  - mission_alignment
  - magnitude                 # numeric
  - role_acting               # bool
default_scale_signature: [territory]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [da_framework]
consuming_systems: [faction_layer, settlement_economy, articulation]
```

---

## §4 Family: mechanical_event

Engine-driven state changes; not actor-initiated.

### mechanical.season_change

```yaml
description: Season boundary crossed.
required_payload_fields:
  - season_index
  - new_season                # spring | summer | autumn | winter
optional_payload_fields:
  - annual                    # true if also year boundary (triggers Tier 3 chronicle)
default_scale_signature: [peninsula]
default_permanence: indelible
default_time_horizon: immediate
emitting_systems: [engine_clock]
consuming_systems: [all subscribing systems]
```

### mechanical.accounting

```yaml
description: Per-season Accounting completed; faction state recomputes.
required_payload_fields:
  - season_index
  - factions_processed        # [faction_ids]
optional_payload_fields:
  - annual                    # true at year end (triggers Tier 3 chronicle)
default_scale_signature: [peninsula]
default_permanence: indelible
default_time_horizon: immediate
emitting_systems: [engine_clock]
consuming_systems: [faction_layer, articulation]
```

### mechanical.cascade_resolution

```yaml
description: Faction Cascade re-resolved (per PP-686 §3.2).
required_payload_fields:
  - faction_id
  - prior_aggregate           # vector
  - new_aggregate             # vector
  - cascade_fidelity_change   # delta
  - triggered_by              # succession | drift | crisis
optional_payload_fields:
  - leader_id_at_resolution
default_scale_signature: [territory]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [faction_layer]
consuming_systems: [faction_layer, npc_behavior, articulation]
```

### mechanical.mission_shift

```yaml
description: Faction Mission redefined (per PP-686 §3.1).
required_payload_fields:
  - faction_id
  - prior_mission             # mission spec
  - new_mission               # mission spec
  - trigger                   # victory_milestone | leader_replacement | mission_failure | authored
optional_payload_fields:
  - public_announcement       # bool (otherwise covert)
default_scale_signature: [territory, peninsula]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [faction_layer]
consuming_systems: [faction_layer, npc_behavior, articulation]
```

### mechanical.scene_entered

```yaml
description: Scene boundary marker — fired when GameDirector pushes a scene container onto the zoom stack. Payload-only (no state mutation). Wall-clock timestamps are NEVER added to payload — the SceneTimer sidecar records wall-clock to `user://telemetry/<campaign_id>.jsonl` and joins by scene_id at analysis time. This separation preserves PP-687 §6 V4 replay determinism.
required_payload_fields:
  - scene_id                  # 12-hex deterministic hash of (season, year, key_count, seed)
  - system_id                 # combat | social_contest | fieldwork | mass_battle | strategic
  - scope                     # personal | relational | territorial | peninsular
  - sa_cost_estimated         # int — predicted Scene-Action cost (per_system_lookup)
  - slate_priority            # 0=mandatory, 1=crisis, 2=elective_high, 3=elective, 4=ambient, -1=nested
  - season_n                  # int
  - parent_scene_id           # scene_id of parent zoom frame, or "" if top-level
  - stack_depth_after         # int — zoom-stack depth after push (1=top-level, 2=nested)
optional_payload_fields:
  - display_name              # human-readable label (audit only)
default_scale_signature: [personal, territory, peninsula]   # mirrors scope
default_permanence: persistent
default_time_horizon: immediate
emitting_systems: [game_director]
consuming_systems: [scene_timer, articulation, audit]
class: B
declared_by: Phase 5a session 3.5 telemetry substrate (valoria-game commit b8b9a4a)
notes:
  - First member of the scene-lifecycle pair (entered/exited).
  - parent_scene_id encodes the nesting structure for the zoom stack (max depth 2 per ZM-05).
  - Articulation may consume for Tier 3 chronicle pacing analysis.
```

### mechanical.scene_exited

```yaml
description: Scene boundary marker — fired when GameDirector pops a scene container after `scene_completed` (or on engine cancel). Pairs with scene_entered via scene_id. Wall-clock excluded from payload (see scene_entered notes); SceneTimer sidecar computes elapsed_ms by joining records.
required_payload_fields:
  - scene_id                  # same as paired scene_entered
  - sa_cost_actual            # int — actual SA consumed (may differ from estimated)
  - outcome_class             # overwhelming | success | partial | failure | unknown
  - ended_by                  # player | engine_timeout | zoom_in | interrupt | auto_resolve
  - sufficient_scope          # bool — Domain Echo eligibility per scale_transitions §7
optional_payload_fields:
  - scopes_invoked            # [scope_ids] — additional scopes touched mid-scene
  - coherence_cost            # int — Coherence loss (if any)
default_scale_signature: [personal, territory, peninsula]
default_permanence: persistent
default_time_horizon: immediate
emitting_systems: [game_director]
consuming_systems: [scene_timer, articulation, audit]
class: B
declared_by: Phase 5a session 3.5 telemetry substrate (valoria-game commit b8b9a4a)
notes:
  - Always emitted; on engine cancellation, ended_by="interrupt" with sa_cost_actual=0.
  - SceneTimer treats arrival without prior scene_entered as a warning (`unknown scene_id`).
```

### mechanical.scene_skipped

```yaml
description: Scene-opportunity marker — fired when GameDirector resolves an opportunity abstractly (player declined to zoom in, or no container available). No scene_entered/exited pair is emitted; this is the sole record of the dispatch. Carries zero-elapsed sidecar telemetry to support opportunity-density analysis.
required_payload_fields:
  - scene_id                  # 12-hex hash; unique to this skip event
  - system_id                 # which system the opportunity belonged to
  - scope                     # ditto
  - slate_priority            # 0=mandatory (rare; mandatory normally cannot skip), 3=elective
  - season_n
  - reason                    # abstract_resolve | unbuilt_container | depth_exceeded
optional_payload_fields:
  - source_action_type        # the originating DA type
default_scale_signature: [personal, territory]
default_permanence: persistent
default_time_horizon: immediate
emitting_systems: [game_director]
consuming_systems: [scene_timer, audit]
class: B
declared_by: Phase 5a session 3.5 telemetry substrate (valoria-game commit b8b9a4a)
notes:
  - SceneTimer writes a zero-elapsed sidecar record on receipt.
  - mandatory skips (slate_priority=0) should be rare and indicate a missing container or depth-exceeded path; surface in audit.
```

---

## §5 Family: state_transition

Narrative-significant state changes on actors or factions.

### state.scar_acquired

```yaml
description: NPC takes a Conviction Scar.
required_payload_fields:
  - npc_id
  - conviction                # which Conviction
  - scar_count_before
  - scar_count_after
  - triggering_event_key      # key_id of the Key that caused this
optional_payload_fields:
  - thread_event_subtype      # e.g., dissolution_of_living_being
default_scale_signature: [personal]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [conviction_track]
consuming_systems: [npc_behavior, faction_layer, articulation]
notes:
  - Scars are indelible; do not decay.
```

### state.standing_change

```yaml
description: NPC Standing rank shifts (promotion, demotion).
required_payload_fields:
  - npc_id
  - standing_before
  - standing_after
  - trigger                   # promotion | demotion | succession | exile | death
optional_payload_fields:
  - decided_by                # actor_id of authority
  - magnitude                 # 1-3 per faction_politics §1.0a
default_scale_signature: [territory]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [faction_layer, faction_politics]
consuming_systems: [npc_behavior, faction_layer, articulation]
```

### state.coup_attempted

```yaml
description: Internal challenge to faction leadership.
required_payload_fields:
  - faction_id
  - challenger_id
  - incumbent_id
  - outcome                   # success | failure | inconclusive
optional_payload_fields:
  - public                    # bool
  - witnesses                 # [actor_ids]
default_scale_signature: [territory]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [faction_politics]
consuming_systems: [faction_layer, npc_behavior, articulation]
notes:
  - High expectation_weight contribution to PP-688 significance regardless of outcome.
```

### state.succession

```yaml
description: Leader change in a faction.
required_payload_fields:
  - faction_id
  - prior_leader_id
  - new_leader_id
  - succession_mode           # normal | contested | emergency | imposed
optional_payload_fields:
  - public_ceremony           # bool
  - witnesses                 # [actor_ids]
default_scale_signature: [territory, peninsula]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [faction_politics]
consuming_systems: [faction_layer, npc_behavior, articulation]
notes:
  - Triggers immediate cascade_resolution event with triggered_by=succession.
```

---

## §6 Family: environmental

Non-actor-initiated events. `source_actor` is null.

### env.peninsular_strain_shock

```yaml
description: Peninsula-scale Strain delta event.
required_payload_fields:
  - strain_delta              # signed int
  - cause_keys                # [key_ids] of prior Keys contributing to shock
  - affected_territories      # [territory_ids]
optional_payload_fields:
  - symbolic_register         # which Convictions feel the impact
  - severity                  # mild | severe | crisis
default_scale_signature: [peninsula]
default_permanence: persistent
default_time_horizon: far
emitting_systems: [peninsular_strain]
consuming_systems: [faction_layer, npc_behavior, articulation, settlement_layer]
```

### env.crisis

```yaml
description: Acute peninsula-scale event (war, plague, succession crisis, schism).
required_payload_fields:
  - crisis_type               # war | plague | famine | schism | invasion
  - affected_territories      # [territory_ids]
optional_payload_fields:
  - duration                  # seasons (estimate)
  - origin_keys               # [key_ids]
default_scale_signature: [peninsula]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [peninsular_strain, scenario_authoring]
consuming_systems: [all]
```

### env.disaster

```yaml
description: Localized environmental damage (fire, flood, earthquake, blight).
required_payload_fields:
  - disaster_type
  - affected_territories      # [territory_ids]
optional_payload_fields:
  - severity                  # mild | severe | catastrophic
default_scale_signature: [territory]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [scenario_authoring, peninsular_strain]
consuming_systems: [faction_layer, settlement_layer, articulation]
```

### env.population_change

```yaml
description: Settlement population shift (migration, mortality, birth surge).
required_payload_fields:
  - territory_id
  - delta                     # signed int
  - cause                     # migration | mortality | birth_surge | conscription
optional_payload_fields:
  - destination_or_origin     # for migration
default_scale_signature: [settlement, territory]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [settlement_layer, peninsular_strain]
consuming_systems: [faction_layer, settlement_economy]
```

---

## §7 Family: scene_outcome

End-of-scene resolutions; emit when a scene type concludes.

### scene.contest_resolved

```yaml
description: Social contest (Wager, debate) concluded.
required_payload_fields:
  - scene_id
  - outcome                   # initiator_win | target_win | compromise | stalemate
  - participants              # [actor_ids]
optional_payload_fields:
  - persuasion_track_final    # int -5..+5
  - rhetorical_style_used
default_scale_signature: [personal]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [social_contest]
consuming_systems: [npc_behavior, faction_layer, articulation]
```

### scene.battle_concluded

```yaml
description: Mass battle ended.
required_payload_fields:
  - battle_id
  - victor                    # faction_id or null (indecisive)
  - casualties_per_side       # {faction_id: int}
  - territorial_outcome       # {territory_id: control_change}
optional_payload_fields:
  - duration_seasons
  - decisive                  # bool
  - officer_deaths            # [actor_ids]
default_scale_signature: [territory]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [mass_battle]
consuming_systems: [faction_layer, npc_behavior, articulation, conviction_track]
notes:
  - Decisive battles contribute high stakes to PP-688 significance.
  - Officer deaths emit child state.standing_change Keys (cause = this Key).
```

### scene.investigation_resolved

```yaml
description: Investigation, inquiry, or trial concluded.
required_payload_fields:
  - scene_id
  - subject_id                # who was investigated
  - finding                   # exonerated | guilty | inconclusive
optional_payload_fields:
  - public                    # bool
  - witnesses
  - sentence                  # if guilty
default_scale_signature: [territory]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [scene_slate, faction_politics]
consuming_systems: [faction_layer, npc_behavior, articulation]
```

---

## §8 Family: system_meta

Engine-level events the player observes as significant moments.

### meta.knot_formed

```yaml
description: Knot formed between two NPCs (per fieldwork_socializing §5.6).
required_payload_fields:
  - participants              # [actor_id_a, actor_id_b]
  - tier                      # Loose | Medium | Close
optional_payload_fields:
  - formation_scene_id
default_scale_signature: [personal]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [fieldwork]
consuming_systems: [npc_behavior, articulation]
notes:
  - Class B extension added per PP-688 §6.
  - Triggers Tier 2 cut scene per PP-688 §3 trigger ruleset.
```

### meta.knot_ruptured

```yaml
description: Knot rupture event (per ED-773 lifecycle).
required_payload_fields:
  - knot_id
  - participants              # [actor_id_a, actor_id_b]
  - cause                     # betrayal | death | dissolution
optional_payload_fields:
  - composure_damage          # 5 per ED-773 default
  - witnessed_publicly        # bool
default_scale_signature: [personal]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [fieldwork]
consuming_systems: [npc_behavior, articulation, conviction_track]
notes:
  - Class B extension added per PP-688 §6.
  - Triggers Tier 2 cut scene with high significance bonus.
  - 5-Composure-damage is gameplay-load-bearing (per fieldwork_editorial.md SIM-DEBT-SOC-03).
```

### meta.thread_woven

```yaml
description: Thread operation completed.
required_payload_fields:
  - thread_id
  - operating_npc
  - operation_type            # weaving | severing | reinforcing
optional_payload_fields:
  - subject_npcs
  - degree_of_success
default_scale_signature: [personal]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [threadwork]
consuming_systems: [conviction_track, npc_behavior, articulation]
```

### meta.miraculous_event

```yaml
description: Miraculous Event activated (per miraculous_event_v30.md).
required_payload_fields:
  - event_type
  - center_actor              # actor at the center
  - witnessed_by              # [actor_ids]
optional_payload_fields:
  - peninsula_visibility      # bool — visible across peninsula
default_scale_signature: [personal, settlement, peninsula]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [miraculous_event]
consuming_systems: [faction_layer, npc_behavior, articulation]
notes:
  - Always indelible. Always public-visible regardless of original scene scope.
  - High significance contribution.
```

### state.belief_revised

```yaml
description: Player Belief revision per fieldwork_socializing §5.5 marker.
required_payload_fields:
  - npc_id                    # the Belief-holder (player or NPC)
  - prior_belief              # short string
  - new_belief                # short string
optional_payload_fields:
  - triggering_keys           # [key_ids] that led to revision
default_scale_signature: [personal]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [fieldwork]
consuming_systems: [npc_behavior, articulation]
notes:
  - Class B extension added per PP-688 §6.
  - Belief revision is canonical character-development beat — high significance.
  - Triggers Tier 2 cut scene; chronicle named-event by default.
```

### meta.legacy_event

```yaml
description: Wrapper for legacy event channels during Phase B partial migration (per substrate spec §7.2).
required_payload_fields:
  - originating_system
  - legacy_payload            # opaque
optional_payload_fields: []
default_scale_signature: [system_meta]
default_permanence: transient
default_time_horizon: immediate
emitting_systems: [substrate (auto)]
consuming_systems: [legacy-aware consumers only]
notes:
  - Pruned once originating system completes Phase B migration.
```

---

### state.opinion_revised

```yaml
description: Emitted by Procedure D (Opinion Drift) when an Opinion's affect_axis changes by ≥ 0.5 or confidence value changes. Drives Articulation Tier 2 trigger evaluation. (PP-687 Phase B Stage 1 / political_dynamics_keys_migration_v30 §7.1)
required_payload_fields:
  - opinion_subject       # npc_id
  - affect_axis_before    # float
  - affect_axis_after     # float
  - confidence_before     # int [1, 5]
  - confidence_after      # int [1, 5]
optional_payload_fields:
  - driver_memory_refs    # [key_uuid]
default_scale_signature: [personal]
default_permanence: structural
default_time_horizon: medium
default_visibility: private_observers=[emitter, opinion_subject]
emitting_systems: [npc_behavior / Procedure D]
consuming_systems: [articulation, npc_memory, social_contest]
class: B
declared_by: PP-687 Phase B Stage 1
articulation_significance: stakes_weight 1-3 per affect delta + confidence change
```

### scene.interaction

```yaml
description: Emitted by Procedure E (Off-Screen Interactions) for ambient inner-circle interactions and cross-faction Distant Contact. Carries pre-mutation drift values; state.opinion_revised emits separately if drift threshold crossed. (PP-687 Phase B Stage 1 §7.2)
required_payload_fields:
  - interaction_type      # enum: ambient_inner_circle | cross_faction_distant_contact | knot_partner
  - drift_a_to_b          # float
  - drift_b_to_a          # float
optional_payload_fields:
  - faction               # faction_id
  - shared_conviction_primary   # bool
  - cumulative_drift      # float
default_scale_signature: [personal]
default_permanence: transient
default_time_horizon: immediate
default_visibility: private_observers=[participants]
emitting_systems: [npc_behavior / Procedure E]
consuming_systems: [npc_memory, articulation (low priority)]
class: B
declared_by: PP-687 Phase B Stage 1
articulation_significance: stakes_weight 0-1 (low; cumulative_drift > 1.0 escalates)
```

### scene.gossip

```yaml
description: Emitted by Procedure E §6.3 when cumulative interaction drift > 0.5. Generates a propagatable gossip artifact reachable by inner-circle observers and (via propagation) third-parties. (PP-687 Phase B Stage 1 §7.3)
required_payload_fields:
  - principals            # [npc_id]
  - cumulative_drift      # float
  - origin_interaction_key   # key_uuid
optional_payload_fields:
  - propagation_observers # [npc_id] — populated by propagation logic
default_scale_signature: [personal]
default_permanence: structural
default_time_horizon: medium
default_visibility: semi_public_observers=propagation_observers (initial: principals only)
emitting_systems: [npc_behavior / Procedure E]
consuming_systems: [npc_memory, articulation]
class: B
declared_by: PP-687 Phase B Stage 1
articulation_significance: stakes_weight 1; multi-hop propagation escalates significance
```

### state.concern_resolved

```yaml
description: Emitted by Procedure B (Concern Generation and Resolution) when Concern resolves with subject_npc_id set. Carries resolution polarity and Belief-revision flag. (Belief revision itself emits state.belief_revised separately.) (PP-687 Phase B Stage 1 §7.4)
required_payload_fields:
  - concern_tag           # string
  - affect                # float [-3, +3] — resolution polarity (implied_affect)
optional_payload_fields:
  - belief_revision       # bool — true if state.belief_revised also emitted
default_scale_signature: [personal]
default_permanence: structural
default_time_horizon: medium
default_visibility: private_observers=[emitter, subject_npc_id]
emitting_systems: [npc_behavior / Procedure B]
consuming_systems: [npc_memory, articulation]
class: B
declared_by: PP-687 Phase B Stage 1
articulation_significance: stakes_weight 1-2 per affect magnitude
```

---

## §9 Type Count Summary

| Family | Subtypes | Notes |
|---|---|---|
| scene_event | 7 | Adds Class B scene.interaction, scene.gossip per PP-687 Phase B Stage 1 |
| da_outcome | 5 |  |
| mechanical_event | 7 | Adds Class B mechanical.scene_entered/exited/skipped per Phase 5a session 3.5 telemetry substrate |
| state_transition | 6 | Adds Class B state.opinion_revised, state.concern_resolved per PP-687 Phase B Stage 1 |
| environmental | 4 |  |
| scene_outcome | 3 |  |
| system_meta | 5 (incl. PP-688 Class B additions: meta.knot_ruptured, state.belief_revised, plus meta.legacy_event) |  |
| **Total** | **37** |  |

Original integration-plan target was 25-30 per §3.2 commit 1 D6; Class B extensions in PP-687 Phase B Stage 1 (+4 types) and Phase 5a session 3.5 telemetry substrate (+3 types) expand the registry by 7 types (11 of total are Class B post-Stage-1+telemetry). Class A type count remains within the 25-30 bound.

---

## §10 Extension Process

Adding a new Key type:

1. Class B vetting block (PP-674 framework).
2. Append entry to this registry following format (§1).
3. Define emitting and consuming systems.
4. Update consuming systems' subscription tables.
5. Test against universal invariants (§2.3 of substrate).
6. Patch register entry referencing this registry.

Modifying required_payload_fields of an existing type:

1. Class A supersession event.
2. Entry to `canon/supersession_register.yaml`.
3. Migration path for existing Keys of that type (transformation rule or Phase-B-style wrapping).
4. Patch register Class A entry.

---

**End registry. PROVISIONAL pending ratification.**
