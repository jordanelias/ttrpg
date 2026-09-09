<!-- [CANONICAL: 2026-05-01 — PP-687 Key type registry; promoted from PROVISIONAL after Stage 10 sim PASS (12/14 battery; commits bb5e293 lateral + 3cb5207 articulation)] -->
<!-- STATUS: CANONICAL — Class A canonical document. Companion to key_substrate_v30.md. (Corrected
     2026-07-07, ED-IN-0026 ruling pass / OPT-7 header-split item: this comment lagged the
     2026-05-01 promotion above and the live `## Status: CANONICAL` line below — never a live
     PROVISIONAL state, just an unpropagated header.) -->
<!-- AUTHORITY: PP-687 -->

# Key Type Registry (PP-687)
## Status: CANONICAL

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

### scene.thread_operation

```yaml
description: Thread operation performed (weave / cut / reinforce); per-scene threadwork act.
required_payload_fields:
  - operation                 # weave | cut | reinforce | <threadwork op>
  - operator_id               # actor_id
optional_payload_fields:
  - target_thread             # thread_id
  - operation_scale           # personal | settlement | territory
default_scale_signature: [personal]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [threadwork]
consuming_systems: [npc_behavior, articulation]
```
<!-- [STUB: payload inferred, not canon-specified — provisional per J-2 register-all; pending Jordan ratification; tracked workplan #29 / ED-935] -->

### scene.draft_da

```yaml
description: Domain Action drafted / submitted (pre-resolution); resolution later emits da_outcome.*.
required_payload_fields:
  - action_type               # intended da subtype
  - actor_id                  # submitting actor
optional_payload_fields:
  - target_id                 # intended target faction / territory
default_scale_signature: [personal]
default_permanence: transient
default_time_horizon: immediate
emitting_systems: [domain_actions]
consuming_systems: [npc_behavior, articulation]
```
<!-- [STUB: payload inferred, not canon-specified — provisional per J-2 register-all; pending Jordan ratification; tracked workplan #29 / ED-935] -->

### scene.displacement

```yaml
description: Displacement / neglect perceived (Procedure displacement_neglect_observed) — an NPC registers being displaced or neglected in a relation.
required_payload_fields:
  - observer_id               # actor who perceives displacement
  - displaced_relation        # relation / edge affected
optional_payload_fields:
  - displaced_by              # actor_id who displaced
  - neglect_context           # short string
default_scale_signature: [personal]
default_permanence: transient
default_time_horizon: immediate
emitting_systems: [npc_behavior]
consuming_systems: [npc_behavior, articulation]
```
<!-- [STUB: payload inferred, not canon-specified — provisional per J-2 register-all; pending Jordan ratification; tracked workplan #29 / ED-935] -->

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

### mechanical.project_advanced

```yaml
description: NPC Project advanced one step (Procedure C). Doc-12 §4.1.
required_payload_fields:
  - project_id
  - progress_before           # int
  - progress_after            # int
  - project_domain
optional_payload_fields:
  - mood_modifier
default_scale_signature: [personal]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [npc_behavior]
consuming_systems: [npc_behavior, articulation]
```

### mechanical.settlement_captured

```yaml
description: Undefended settlement (Defense 0, no garrison) auto-captured on hostile military entry — no roll (settlement_layer_v30 §5.2).
required_payload_fields:
  - settlement_id
  - territory_id
  - capturing_faction_id
  - prior_controlling_faction_id
optional_payload_fields: []
default_scale_signature: [settlement, territory]
default_permanence: indelible
default_time_horizon: near
emitting_systems: [settlement_layer]
consuming_systems: []
notes:
  - "ED-IN-0014 (OI-25, 2026-07-29 W3 item 7): settlement_layer had zero Key integration. Name/family
     match the PROPOSED candidate already filed at key_echo_armature_v1.md §3 (EP-4, C-MBSE-9) — reused
     rather than reinvented."
  - "DECLARE-ONLY this wave: the g_def0 gate (module_contracts.yaml settlement_layer) has no evaluator
     in the live loop — settlement.py derives Order/Prosperity/Defense but never checks Defense==0 with
     a hostile-entry condition, and no other module calls it. No sched.emit wired; the emit fires when
     that evaluation is built (per this wave's own scoping instruction: runtime-less/unreached gates get
     registration only, not a live emit call)."
  - "consuming_systems intentionally EMPTY (corrected 2026-07-29, adj DEFECT 1, ED-IN-0096):
     articulation (the live chronicle subscriber) was named here, but the type_id was never actually in
     engine/cross_scale/articulation.py's _TRIGGER_TYPE_IDS and never will be absent a real emit site to
     subscribe to — declaring it created a false consumer with no corresponding subscription anywhere.
     The real consumer is decided at settlement_layer's g_def0 evaluator build (the DECLARE-ONLY note
     above); held with that docket, not guessed at here. See module_contracts.yaml's settlement_layer
     gap_notes for the pointer (W3 item 3, ED-IN-0096)."
```

### mechanical.era_transition

```yaml
description: World-state era boundary crossed — MS=0 Post-Calamity Era entry (victory_v30 §5.1), MS restored to 20 within 10 seasons Post-Calamity Recovery (§5.1), IP=100 Phased Occupation Era entry incl. the 3-phase escalation (§5.2), all factions dissolved Anarchy Era entry (§5.3). The MS<=5-sustained-10-seasons Second Calamity is registered SEPARATELY (mechanical.second_calamity, below) — victory_v30 §5.1/§5.3 both call it out by name as "the only true campaign terminal", a distinction this registry preserves rather than folding into the general transition type.
required_payload_fields:
  - to_era                    # post_calamity | post_calamity_recovery | phased_occupation | anarchy
  - trigger_stat               # MS | IP | faction_dissolution
optional_payload_fields:
  - occupation_phase           # int 1-3, phased_occupation only (§5.2 corridors)
default_scale_signature: [peninsula]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [victory]
consuming_systems: []
notes:
  - "ED-IN-0014 (OI-25, 2026-07-29 W3 item 7): victory's era/occupation transitions had zero Key
     integration (module_contracts.yaml gap_note, victory :727). Family/naming follow the PROPOSED
     candidate at key_echo_armature_v1.md §3 (EP-5, C-MBSE-13) for the g_ms0/g_msrec/g_diss + IP=100
     cluster; that candidate table notes IP=100 is itself gateless in module_contracts (C-MBSE-13) —
     recorded here, not gated by this wave."
  - "DECLARE-ONLY: systems/victory/ has no sim/ subfolder — zero runtime of any kind (doc-only home,
     resolver: state_reader per its own contract entry). Registration + this contract declaration
     (routed via oracle_requests) is the full deliverable per this wave's scoping instruction for
     runtime-less emitters; the emit fires when victory's module is built."
  - "G12 note (not acted on, contracts-lane territory): module_contracts.yaml :728 gap_note reads
     'doc status: DESIGN — pending Varfell Path B user decision (ED-311) — not CANONICAL', but
     victory_v30.md itself lists ED-311 CLOSED (PP-667, :761) and its own header Status is CANONICAL for
     every section outside the explicitly-superseded §0.1/§3.1-3.6/§4/§8 list — §5 is not in that list.
     Logged per CLAUDE.md §0.1 point 5 (log, don't chase); not corrected here — module_contracts.yaml is
     the contracts lane's file this wave."
  - "consuming_systems intentionally EMPTY (corrected 2026-07-29, adj DEFECT 1, ED-IN-0096):
     articulation was named here, but has no live subscription for this type and no live emit site
     exists to subscribe to — declaring it created a false consumer for a type nothing ever fires.
     The real consumer is decided when victory's module is built (the DECLARE-ONLY note above); held
     with that docket, not guessed at here. See module_contracts.yaml's victory gap_notes for the
     pointer (W3 item 3, ED-IN-0096)."
```

### mechanical.second_calamity

```yaml
description: MS <= 5 sustained for 10 seasons during the Post-Calamity Era — "the only true campaign terminal" (victory_v30 §5.1, restated §5.3). Kept distinct from mechanical.era_transition because every other era boundary is recoverable (§5.1's own Recovery clause, §5.3's quorum-restoration clause) while this one is not.
required_payload_fields:
  - seasons_sustained_at_or_below_5   # int, >= 10 at fire time
optional_payload_fields: []
default_scale_signature: [peninsula]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [victory]
consuming_systems: []
notes:
  - "ED-IN-0014 (OI-25, 2026-07-29 W3 item 7). Matches key_echo_armature_v1.md §3's separately-listed
     candidate 'mechanical.second_calamity' (EP-5) — 'the game's only true terminal deserves its own
     type', per that table's own rationale."
  - "DECLARE-ONLY — same zero-runtime disposition as mechanical.era_transition above."
  - "consuming_systems intentionally EMPTY (corrected 2026-07-29, adj DEFECT 1, ED-IN-0096):
     articulation was named here, but has no live subscription for this type and no live emit site
     exists to subscribe to — declaring it created a false consumer for a type nothing ever fires.
     The real consumer is decided when victory's module is built (the DECLARE-ONLY note above); held
     with that docket, not guessed at here. See module_contracts.yaml's victory gap_notes for the
     pointer (W3 item 3, ED-IN-0096)."
```

### mechanical.theocracy_unification_declared

```yaml
description: CI reaches 100 — Church publicly declares Papal Sovereignty and triggers the one-shot Mass Seizure on every territory with Church buildings (ci_political_v30 §2.2). The SAME threshold is independently gated by territorial_piety's g_ci100 entry (module_contracts.yaml :288-292), which cites this identical section as its source — one event, registered once, closing both silent emitters named in ED-IN-0014 rather than duplicating a type per module.
required_payload_fields:
  - ci_value                   # int, = 100 at fire time
  - mass_seizure_targets       # [territory_ids] with Church buildings
optional_payload_fields:
  - outcome                    # active | failed_counterattack | failed_mandate_floor (§2.2: fails if
                                #   Church loses 3 territories to counterattack in one Year-End, or
                                #   Church Mandate <= 3 — "No second attempt")
default_scale_signature: [territory, peninsula]
default_permanence: indelible
default_time_horizon: far
emitting_systems: [ci_political, territorial_piety]
consuming_systems: []
notes:
  - "ED-IN-0014 (OI-25, 2026-07-29 W3 item 7): ci_political has ZERO Key integration in a CANONICAL doc
     (its own contract gap-note, :689); territorial_piety's g_ci100 gate is the same GAP-E1/GAP-E2
     zero-Key-INERT finding from the 2026-07-14 gameplay-subsystem-observatory audit
     (subsystem_nexus_artifact.html: 'GAP-E1 zero-Key INERT — key the Church card-game' /
     'GAP-E2 zero-Key INERT'). Name/family follow the PROPOSED candidate at key_echo_armature_v1.md §3
     ('mechanical.theocracy_unification_declared', EP-5)."
  - "DECLARE-ONLY: neither ci_political nor territorial_piety has any Python runtime (both doc-only
     homes; the retired tests/sim/v17-integration/m2_ci_political_revision*.py pair predates the
     current sim tree and is not a live module) — registration + contract declaration is the full
     deliverable per this wave's scoping instruction for runtime-less emitters."
  - "DUAL-EMITTER SINGLE-OWNER NOTE (2026-07-29, ED-IN-0096): ci_political §2.2 and territorial_piety's
     g_ci100 gate both cite the identical CI=100 threshold as their own trigger for this SAME event —
     one type covering both (per this entry's own header), not one per module. Which module's build
     actually calls sched.emit() for it — ci_political's Theocracy Unification Attempt resolver, or
     territorial_piety's g_ci100 gate handler, or a shared helper both call — is UNDECIDED and
     deliberately NOT guessed at here (both are doc-only, zero runtime, per the DECLARE-ONLY note
     above); the residual is named, not fabricated. Whichever module builds first inherits the emit
     site; the other becomes its caller or is superseded, decided at that build."
  - "consuming_systems intentionally EMPTY (corrected 2026-07-29, adj DEFECT 1, ED-IN-0096):
     articulation was named here, but has no live subscription for this type and no live emit site
     exists to subscribe to — declaring it created a false consumer for a type nothing ever fires.
     The real consumer is decided at whichever module's build resolves the dual-emitter question above;
     held with that docket, not guessed at here. See module_contracts.yaml's ci_political AND
     territorial_piety gap_notes for the pointer (W3 item 3, ED-IN-0096)."
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

### state.project_completed

```yaml
description: NPC Project completed (progress >= 10; Procedure C). Doc-12 §4.3.
required_payload_fields:
  - project_id
  - project_domain
  - completion_effect
  - supporters                # [actor_ids]
  - obstructors               # [actor_ids]
  - goal_short
optional_payload_fields: []
default_scale_signature: [personal]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [npc_behavior]
consuming_systems: [npc_behavior, articulation]
```

### state.project_failed

```yaml
description: NPC Project failed via stall (seasons_stalled >= 8; Procedure C). Doc-12 §4.2.
required_payload_fields:
  - project_id
  - failure_mode              # 'stalled'
  - seasons_stalled           # int
optional_payload_fields: []
default_scale_signature: [personal]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [npc_behavior]
consuming_systems: [npc_behavior, articulation]
```

### state.settlement_revolt

```yaml
description: Settlement Order reaches 0 — local revolt; governor expelled unless a garrison is present (settlement_layer_v30 §4.3 Settlement Events table, "Order 0" row; also §1.3 "Order 0 = local revolt").
required_payload_fields:
  - settlement_id
  - territory_id
  - governor_expelled          # bool — false only if a garrison is present (§4.3)
optional_payload_fields:
  - controlling_faction_id
default_scale_signature: [settlement, territory]
default_permanence: indelible
default_time_horizon: near
emitting_systems: [settlement_layer]
consuming_systems: []
notes:
  - "ED-IN-0014 (OI-25, 2026-07-29 W3 item 7). Name/family match the PROPOSED candidate already filed
     at key_echo_armature_v1.md §3 (EP-4, C-MBSE-9) — reused rather than reinvented."
  - "DECLARE-ONLY this wave: the g_ord0 gate's only live trace is
     engine/cross_scale/zoom_in_out.py::check_mandatory_triggers, which returns the 'Settlement Revolt'
     trigger SCHEMA (name/priority/condition text) but explicitly defers the world-state evaluation
     ('Order 0' condition check) to an unbuilt consumer — its own docstring: 'Actual world-state
     evaluation ... is consumer-side'. No module evaluates Order==0 anywhere in the live tree. Per this
     wave's own scoping instruction (wire the actual sched.emit only if the gate is reachable in the
     live loop), this is declare-only: registration now, emit call when the evaluator is built."
  - "consuming_systems intentionally EMPTY (corrected 2026-07-29, adj DEFECT 1, ED-IN-0096):
     articulation was named here, but has no live subscription for this type and no live emit site
     exists to subscribe to — declaring it created a false consumer for a type nothing ever fires.
     The real consumer is decided at settlement_layer's g_ord0 evaluator build (the DECLARE-ONLY note
     above); held with that docket, not guessed at here. See module_contracts.yaml's settlement_layer
     gap_notes for the pointer (W3 item 3, ED-IN-0096)."
```

---

## §6 Family: environmental

Non-actor-initiated events. `source_actor` is null.

### env.peninsular_strain_shock

```yaml
description: Peninsula-scale Strain delta event.
required_payload_fields:
  - strain_delta              # signed int
  - causes                    # [key_ids] of prior Keys contributing to shock (unified provenance naming — was cause_keys; C-INJ-12/ED-IN-0022, converges on the universal key_substrate_v30 `causes[]`)
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
  - causes                    # [key_ids] (unified provenance naming — was origin_keys; C-INJ-12/ED-IN-0022, converges on the universal key_substrate_v30 `causes[]`)
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

### scene.combat_resolved

```yaml
description: Personal / skirmish combat concluded (F3 — the missing combat scene_outcome subtype; mirrors scene.contest_resolved on the combat path).
required_payload_fields:
  - scene_id
  - outcome                   # attacker_win | defender_win | draw | rout | withdrawal
  - participants              # [actor_ids]
optional_payload_fields:
  - casualties                # [actor_ids]
  - wounds_inflicted          # {actor_id: int}
default_scale_signature: [personal]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [personal_combat]
consuming_systems: [npc_behavior, faction_layer, articulation]
```
<!-- [STUB: payload inferred, not canon-specified — provisional per J-2 register-all; pending Jordan ratification; tracked workplan #29 / ED-935] -->

### scene.combat_strike

```yaml
description: A declared combat action (a strike) entering personal-combat resolution — the action-input subtype the CombatEngine's StrikeModule consumes (F3 — combat-path action vocabulary; 2-part family.subtype per registry convention).
required_payload_fields:
  - attacker                  # actor_id
  - defender                  # actor_id
optional_payload_fields:
  - commit                    # int 2-5 (commitment depth; disposition-skewed)
  - weapon                    # weapon_id override
default_scale_signature: [personal]
default_permanence: transient
default_time_horizon: immediate
emitting_systems: [scene_slate, player_input]
consuming_systems: [personal_combat]
```
<!-- [STUB: combat-path action vocabulary; provisional per J-2 register-all; extracted 2026-06-23 with personal_combat] -->

### scene.combat_hit

```yaml
description: A landed blow within a fight; carries the wound as a write-protected `health` stat_delta on the defender target (F1 — the wound rides the substrate, never a direct write). StrikeModule emits; WoundModule consumes.
required_payload_fields: []
optional_payload_fields:
  - degree                    # graze | partial | success | overwhelming
  - damage                    # int (health-delta magnitude)
  - net                       # float (sigma-leverage net)
default_scale_signature: [personal]
default_permanence: transient
default_time_horizon: immediate
emitting_systems: [personal_combat]
consuming_systems: [personal_combat]
```
<!-- [STUB: provisional per J-2 register-all; extracted 2026-06-23 with personal_combat] -->

### scene.combat_felled

```yaml
description: A combatant incapacitated by Health depletion (ED-1041 wound model). Witnessable; ripples up to factions and into NPC memory.
required_payload_fields:
  - actor_id                  # the felled combatant
optional_payload_fields:
  - by_actor                  # actor_id of the feller
default_scale_signature: [personal]
default_permanence: indelible
default_time_horizon: near
emitting_systems: [personal_combat]
consuming_systems: [npc_behavior, faction_layer, articulation]
```
<!-- [STUB: provisional per J-2 register-all; extracted 2026-06-23 with personal_combat] -->

### scene.accord_echo

```yaml
description: §5.5 Accord Domain Echo — a resolved scene's downstream settlement-Order consequence (scale_transitions_v30.md §5.5, degree-keyed governance/destabilisation/territorial_transfer/violence rows), applied to Settlement.order at the settlement where the scene occurred (AUD-SET-02, :215) and queued to Accounting Step 4c per §5.5's own caption (:221). Distinct from scene.contest_resolved/scene.combat_resolved (the SAME scene resolution's §5.2 Domain Echo Key, a disjoint faction-stat consequence) — one resolved scene may emit both, and this Key's causes[] cites that Key's id when it also fired (OI-28).
required_payload_fields:
  - scene_outcome              # governance | destabilisation | territorial_transfer | violence (§5.5 vocabulary)
  - target_settlement          # settlement_id the write applies to
optional_payload_fields:
  - accord_delta                # int, canonical-index Settlement.order delta (§5.5 table; 0 for territorial_transfer, which sets rather than deltas)
default_scale_signature: [settlement]
default_permanence: persistent
default_time_horizon: near
emitting_systems: [echo_transport]
consuming_systems: [articulation]
notes:
  - "ED-IN-0091 plan §3 Wave 3 Handoff item 1 (W2 handoff, closing OI-03 fix 4's timing/contract
     collision, 2026-07-29): echo_transport._apply_accord_echo's own docstring named this exact
     registration as the missing piece for genuine OF-7 queue-parity with the sibling §5.2
     domain-echo leg. Family/placement: filed alongside scene.combat_resolved/scene.contest_resolved
     (§7 scene_outcome) rather than a new family, since it is the same scene resolution's second,
     disjoint-state consequence (Settlement.order/RS vs. Faction stat), not a new event class."
  - "LIVE this wave, not declare-only: echo_transport._apply_accord_echo now builds this Key and
     routes the settlement-Order write through sched.emit(key, apply=...) — the write lands at
     accounting_boundary(), exactly like the §5.2 leg. The leg itself stays DORMANT in any seeded
     campaign (no live producer declares echo['scene_outcome'] — re-verified 2026-07-29), so no
     pinned golden can move; the wiring is real, only unreached."
  - "rs_delta (§5.5's violence-row RS component) is deliberately NOT a payload field here: canon
     (scale_transitions_v30.md:219, contrasted with :221) keeps RS immediate, not queued to
     Accounting like the Accord component — it stays a direct rs_track.apply_rs_delta call outside
     this Key, unaffected by this registration."
  - "consuming_systems names articulation per the same declared-consumer rule as the OI-25 entries
     above; subscription wiring is CLOSED same wave (2026-07-29, fix round 1): articulation.py's
     _TRIGGER_TYPE_IDS gained this type as its 13th entry, articulation_layer_v30.md §3.1 gained
     row #13 (OI-03/W3), and tests/valoria/test_articulation_subscriber.py exercises it end-to-end
     through a real TickScheduler. Not a dangling emit and not merely declared-not-yet-subscribed —
     the leg stays organically DORMANT in any seeded campaign (see the note above), which is a
     reachability fact about the emit side, not a gap on the subscription side."
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

### meta.cascade_cluster_event

```yaml
description: Cross-faction cascade cluster forms or dissolves (sustained ≥ 4 seasons of |cosine similarity| > 0.40 between two factions' cascade_fidelity_history). A CANONICAL articulation trigger (articulation_layer_v30 §3.1 #9) cited this type before it was ever registered per §10 — registered 2026-07-07 (ED-IN-0022, C-KEY-8).
required_payload_fields:
  - cluster_pair              # [faction_id_a, faction_id_b]
  - similarity                # float cosine similarity of the two 4-season cascade_fidelity windows
  - cluster_type              # aligned (sim > 0) | anti_aligned (sim < 0)
  - sustained_seasons         # int regime-entry streak
optional_payload_fields:
  - regime_transition         # bool (refire on regime transition)
default_scale_signature: [territorial]   # peninsular when abs(similarity) > 0.95 per the trigger-9 spec
default_permanence: persistent
default_time_horizon: far
emitting_systems: [articulation]         # [PROVISIONAL] the trigger-9 evaluator lives in the articulation layer; confirm against the implementation section
consuming_systems: [articulation]        # [PROVISIONAL] articulation renderer (cut-scene); confirm at implementation
notes:
  - RETROACTIVE registration (C-KEY-8 / ED-IN-0022, 2026-07-07) of a type a CANONICAL trigger (articulation §3.1 #9, "Trigger 9 specification") already cites — closes the dangling-type defect.
  - Payload + scale rule per articulation_layer_v30 §3.1 (threshold ±0.40, Stage 10 A6 calibration).
  - A15 rendering-disposition row (references/rendering_dispositions.yaml) is DEFERRED to the Stratum-C rendering wave — that datafile does not exist yet, so §10's A15 precondition is recorded here as pending rather than fabricated.
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
<!-- [STUB: emitting_systems=[fieldwork] may under-attribute — npc_behavior §3 belief revision may also emit this; verify; tracked workplan #32 / ED-937] -->

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
default_visibility: "semi_public_observers=propagation_observers (initial: principals only)"
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
| scene_event | 10 | Adds Class B scene.interaction, scene.gossip per PP-687 Phase B Stage 1 |
| da_outcome | 5 |  |
| mechanical_event | 12 | Adds Class B mechanical.scene_entered/exited/skipped per Phase 5a session 3.5 telemetry substrate; +4 ED-IN-0014 (OI-25, 2026-07-29 W3): mechanical.settlement_captured, mechanical.era_transition, mechanical.second_calamity, mechanical.theocracy_unification_declared — all DECLARE-ONLY, zero live emit calls |
| state_transition | 9 | Adds Class B state.opinion_revised, state.concern_resolved per PP-687 Phase B Stage 1; +1 ED-IN-0014 (OI-25, 2026-07-29 W3): state.settlement_revolt — DECLARE-ONLY |
| environmental | 4 |  |
| scene_outcome | 8 | +3 F3 combat subtypes physically present under §7 but previously uncounted: scene.combat_strike, scene.combat_hit, scene.combat_felled. Reconciled 2026-07-07 (ED-IN-0022); +1 ED-IN-0091 plan §3 Wave 3 Handoff item 1 (2026-07-29): scene.accord_echo — LIVE (queued via sched.emit, not declare-only), leg stays dormant pending a caller-declared scene_outcome |
| system_meta | 7 (incl. PP-688 Class B additions: meta.knot_ruptured, state.belief_revised, meta.legacy_event, + the retroactively-registered meta.cascade_cluster_event) | meta.legacy_event counted + meta.cascade_cluster_event added (C-KEY-8). ED-IN-0022 |
| **Total** | **55** | reconciled to the physical `###` type-headers (was 49 per ED-IN-0022, 2026-07-07); +5 ED-IN-0014 (OI-25, 2026-07-29 W3 item 7 — the code-shape open-items program's silent-emitter registration: settlement_layer's revolt/auto-capture gates, victory's era/occupation/terminal transitions, and the shared ci_political/territorial_piety CI=100 Theocracy Unification event, one type covering both). All 5 are DECLARE-ONLY (registered here; zero live `sched.emit` call sites this wave — see each entry's notes). +1 more, same day (ED-IN-0091 plan §3 Wave 3 Handoff item 1): scene.accord_echo, LIVE (a real sched.emit call site exists, in echo_transport._apply_accord_echo) but organically dormant |

Original integration-plan target was 25-30 per §3.2 commit 1 D6; Class B extensions in PP-687 Phase B Stage 1 (+4 types) and Phase 5a session 3.5 telemetry substrate (+3 types) expand the registry by 7 types (11 of total are Class B post-Stage-1+telemetry). Class A type count remains within the 25-30 bound. ED-935 (J-2 register-all) adds 7 further types — scene.thread_operation, scene.draft_da, scene.displacement, mechanical.project_advanced, state.project_completed, state.project_failed, scene.combat_resolved — Total -> 44. (§9 family counts are logical groupings; some Class-B types are physically filed under §8 system_meta. The pre-existing declared-vs-parsed header drift, master item 11 / A9, is RECONCILED 2026-07-07 (ED-IN-0022): scene_outcome +3 (combat subtypes scene.combat_strike/hit/felled) and system_meta +1 (meta.legacy_event) bring the logical subtotals to 48; registering meta.cascade_cluster_event (below, C-KEY-8) then adds the 49th type, so both the declared total and the physical `###` count are 49. ED-IN-0014/OI-25 (2026-07-29) then adds the 5 declare-only types above, bringing both counts to 54; the same day, ED-IN-0091 plan §3 Wave 3 Handoff item 1 registers scene.accord_echo, bringing both counts to 55.)

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

**Process extension (2026-07-07, RATIFIED — Jordan's consolidated "ratify all" ruling pass,
ED-IN-0026, `key_echo_armature_v1.md` §5.16):** step 2 above gains a mandatory precondition —
**no new Key type may be appended to this registry without a corresponding row in
`references/rendering_dispositions.yaml`** (the A15 rendering-disposition datafile: RENDERED-RICH
/ GENERIC / UNRENDERED / DELIBERATE-SILENT verdict, citing the deciding armature/audit finding).
This closes the gap the armature's C-KEY sweep found — types entering the registry with no
recorded answer to "how does the player ever see this?" A15 (`skills/valoria-module-adjudicator`)
enforces it report-only against the existing 55-type roster (§9's current total, re-verified
2026-07-29 — was 48 at the time this section was written, since grown by ED-IN-0022/ED-IN-0014/
ED-IN-0091 registrations) first; it flips to blocking new entries once
`rendering_dispositions.yaml` exists and the backlog is at zero (§4 of the armature, standard
warn→block discipline).

---

**End registry. CANONICAL — see the header-split correction above (2026-07-07).**
