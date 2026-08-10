# Valoria — Key Index (55 key types)

> **GENERATED** by `tools/build_contract_index.py`. Do not hand-edit — every fact below is rendered from a source file and a hand-edit is silently discarded on the next build.
> Fix a fact at its source: keys in `systems/_architecture/key_type_registry_v30.md`, edges and owned state in `references/module_contracts.yaml`, build status in `references/wiring_manifest.yaml`.

**Sources joined:** `references/key_graph.json` (generated) ← `systems/_architecture/key_type_registry_v30.md` + `references/module_contracts.yaml`. Module-level companion: [CONTRACT_INDEX.md](CONTRACT_INDEX.md).

A blank cell means **not declared**, which is not the same claim as "none". Producer/consumer sets are the **union** of both authored views; the `agreement` column says whether that union was unanimous.

---

## Review queue — keys

Ordered by the kind of answer needed, not by severity: a chain that terminates is a **design** question, an under-declaration is a **filing** question.

### 1. Chains that terminate (design questions)

**1 key type(s) nobody produces** — a payload schema no system fills. Either something should emit it, or the type should be retired.

| key | family | declared consumers |
|---|---|---|
| [`meta.legacy_event`](#metalegacy_event) | system_meta | — |

**8 key type(s) nobody consumes** — a message no system reads. Several are terminal world-events where a consumer may genuinely never exist; that is a legitimate answer, but it should be a recorded one.

| key | family | declared producers |
|---|---|---|
| [`env.crisis`](#envcrisis) | environmental | `peninsular_strain`, `scenario_authoring` |
| [`mechanical.era_transition`](#mechanicalera_transition) | mechanical_event | `victory` |
| [`mechanical.season_change`](#mechanicalseason_change) | mechanical_event | `engine_clock` |
| [`mechanical.second_calamity`](#mechanicalsecond_calamity) | mechanical_event | `victory` |
| [`mechanical.settlement_captured`](#mechanicalsettlement_captured) | mechanical_event | `settlement_layer` |
| [`mechanical.theocracy_unification_declared`](#mechanicaltheocracy_unification_declared) | mechanical_event | `ci_political`, `territorial_piety` |
| [`meta.legacy_event`](#metalegacy_event) | system_meta | — |
| [`state.settlement_revolt`](#statesettlement_revolt) | state_transition | `settlement_layer` |

### 2. Contradictions (need a ruling)

**None.** The two authored views agree everywhere they both speak — they differ only in how much they have authored. That distinction is load-bearing: it makes the backlog below a filing task rather than a pile of design decisions.

### 3. Under-declaration (filing questions)

**42** key type(s) where the registry names systems the contracts have not declared back. No contradiction — the contract side is simply unauthored.

**Grouped by the module that is missing** — 42 undeclared edge(s) across 2 module(s). `articulation_layer` alone accounts for **41 of 42**, so most of this column is one decision applied repeatedly, not 42 separate ones.

| module missing the declaration | as producer of | as consumer of | total |
|---|---|---|---|
| [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer) | 0 | 41 | 41 |
| `player_input` _(not a contract module — unresolved reference)_ | 1 | 0 | 1 |

<details><summary>per-key detail</summary>

| key | side | named by registry | declared in contracts |
|---|---|---|---|
| [`da.antinomian_action`](#daantinomian_action) | consumers | `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` | `faction_state`, `npc_behavior`, `piety_track` |
| [`da.covert_betrayal`](#dacovert_betrayal) | consumers | `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` | `faction_state`, `npc_behavior`, `piety_track` |
| [`da.diplomatic_alliance`](#dadiplomatic_alliance) | consumers | `articulation_layer`, `faction_state` | `faction_state` |
| [`da.economic_intervention`](#daeconomic_intervention) | consumers | `articulation_layer`, `faction_state`, `settlement_economy` | `faction_state`, `settlement_economy` |
| [`da.public_governance`](#dapublic_governance) | consumers | `articulation_layer`, `faction_state`, `npc_behavior` | `faction_state`, `npc_behavior` |
| [`env.disaster`](#envdisaster) | consumers | `articulation_layer`, `faction_state`, `settlement_layer` | `faction_state`, `settlement_layer` |
| [`env.peninsular_strain_shock`](#envpeninsular_strain_shock) | consumers | `articulation_layer`, `faction_state`, `npc_behavior`, `settlement_layer` | `faction_state`, `npc_behavior`, `settlement_layer` |
| [`mechanical.accounting`](#mechanicalaccounting) | consumers | `articulation_layer`, `faction_state` | `faction_state` |
| [`mechanical.cascade_resolution`](#mechanicalcascade_resolution) | consumers | `articulation_layer`, `faction_state`, `npc_behavior` | `faction_state`, `npc_behavior` |
| [`mechanical.mission_shift`](#mechanicalmission_shift) | consumers | `articulation_layer`, `faction_state`, `npc_behavior` | `faction_state`, `npc_behavior` |
| [`mechanical.project_advanced`](#mechanicalproject_advanced) | consumers | `articulation_layer`, `npc_behavior` | `npc_behavior` |
| [`mechanical.scene_entered`](#mechanicalscene_entered) | consumers | `articulation_layer`, `audit`, `scene_timer` | `audit`, `scene_timer` |
| [`mechanical.scene_exited`](#mechanicalscene_exited) | consumers | `articulation_layer`, `audit`, `scene_timer` | `audit`, `scene_timer` |
| [`meta.knot_formed`](#metaknot_formed) | consumers | `articulation_layer`, `npc_behavior` | `npc_behavior` |
| [`meta.knot_ruptured`](#metaknot_ruptured) | consumers | `articulation_layer`, `npc_behavior`, `piety_track` | `npc_behavior`, `piety_track` |
| [`meta.miraculous_event`](#metamiraculous_event) | consumers | `articulation_layer`, `faction_state`, `npc_behavior` | `faction_state`, `npc_behavior` |
| [`meta.thread_woven`](#metathread_woven) | consumers | `articulation_layer`, `npc_behavior`, `piety_track` | `npc_behavior`, `piety_track` |
| [`scene.battle_concluded`](#scenebattle_concluded) | consumers | `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` | `faction_state`, `npc_behavior`, `piety_track` |
| [`scene.combat_felled`](#scenecombat_felled) | consumers | `articulation_layer`, `faction_state`, `npc_behavior` | `faction_state`, `npc_behavior` |
| [`scene.combat_resolved`](#scenecombat_resolved) | consumers | `articulation_layer`, `faction_state`, `npc_behavior` | `faction_state`, `npc_behavior` |
| [`scene.combat_strike`](#scenecombat_strike) | producers | `player_input`, `scene_slate` | `scene_slate` |
| [`scene.contest_resolved`](#scenecontest_resolved) | consumers | `articulation_layer`, `faction_state`, `npc_behavior` | `faction_state`, `npc_behavior` |
| [`scene.dialogue`](#scenedialogue) | consumers | `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` | `faction_state`, `npc_behavior`, `piety_track` |
| [`scene.displacement`](#scenedisplacement) | consumers | `articulation_layer`, `npc_behavior` | `npc_behavior` |
| [`scene.draft_da`](#scenedraft_da) | consumers | `articulation_layer`, `npc_behavior` | `npc_behavior` |
| [`scene.gift`](#scenegift) | consumers | `articulation_layer`, `faction_state`, `npc_behavior` | `faction_state`, `npc_behavior` |
| [`scene.gossip`](#scenegossip) | consumers | `articulation_layer`, `npc_memory` | `npc_memory` |
| [`scene.insult`](#sceneinsult) | consumers | `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` | `faction_state`, `npc_behavior`, `piety_track` |
| [`scene.interaction`](#sceneinteraction) | consumers | `articulation_layer`, `npc_memory` | `npc_memory` |
| [`scene.investigation_resolved`](#sceneinvestigation_resolved) | consumers | `articulation_layer`, `faction_state`, `npc_behavior` | `faction_state`, `npc_behavior` |
| [`scene.thread_operation`](#scenethread_operation) | consumers | `articulation_layer`, `npc_behavior` | `npc_behavior` |
| [`scene.threat`](#scenethreat) | consumers | `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` | `faction_state`, `npc_behavior`, `piety_track` |
| [`scene.witness`](#scenewitness) | consumers | `articulation_layer`, `npc_behavior`, `piety_track` | `npc_behavior`, `piety_track` |
| [`state.belief_revised`](#statebelief_revised) | consumers | `articulation_layer`, `npc_behavior` | `npc_behavior` |
| [`state.concern_resolved`](#stateconcern_resolved) | consumers | `articulation_layer`, `npc_memory` | `npc_memory` |
| [`state.coup_attempted`](#statecoup_attempted) | consumers | `articulation_layer`, `faction_state`, `npc_behavior` | `faction_state`, `npc_behavior` |
| [`state.opinion_revised`](#stateopinion_revised) | consumers | `articulation_layer`, `npc_memory`, `social_contest` | `npc_memory`, `social_contest` |
| [`state.project_completed`](#stateproject_completed) | consumers | `articulation_layer`, `npc_behavior` | `npc_behavior` |
| [`state.project_failed`](#stateproject_failed) | consumers | `articulation_layer`, `npc_behavior` | `npc_behavior` |
| [`state.scar_acquired`](#statescar_acquired) | consumers | `articulation_layer`, `faction_state`, `npc_behavior` | `faction_state`, `npc_behavior` |
| [`state.standing_change`](#statestanding_change) | consumers | `articulation_layer`, `faction_state`, `npc_behavior` | `faction_state`, `npc_behavior` |
| [`state.succession`](#statesuccession) | consumers | `articulation_layer`, `faction_state`, `npc_behavior` | `faction_state`, `npc_behavior` |

</details>

### 4. Names that resolve to no module

Registry prose naming something that is not a contract module. Left unresolved on purpose — mapping `player_input` or `all subscribing systems` to a module is a design decision, and guessing one would fabricate it.

| unresolved reference |
|---|
| `all` |
| `all subscribing systems` |
| `echo_transport` |
| `legacy-aware consumers only` |
| `player_input` |
| `substrate (auto)` |

### 5. Names that are not key types

Entries in the contracts' `emits`/`consumes` that are not `namespace.name` key types. `*` is the known and deliberate one — a **wildcard subscription** meaning "every key", not a malformed name (ED-IN-0149). Anything else here is a defect.

| name | reading | declared by |
|---|---|---|
| `*` | wildcard subscription — every key | `articulation_layer`, `fieldwork_knots` |

---

## Key types by family

Family is the registry's **physical** `## §N Family:` filing. It differs from the registry's own §9 logical count table, which the registry notes itself: some Class-B types are physically filed under §8 `system_meta`. Neither count is wrong — they count different things.

| family | types | no producer | no consumer |
|---|---|---|---|
| [da_outcome](#family-da_outcome) | 5 | 0 | 0 |
| [environmental](#family-environmental) | 4 | 0 | 1 |
| [mechanical_event](#family-mechanical_event) | 12 | 0 | 5 |
| [scene_event](#family-scene_event) | 8 | 0 | 0 |
| [scene_outcome](#family-scene_outcome) | 8 | 0 | 0 |
| [state_transition](#family-state_transition) | 7 | 0 | 1 |
| [system_meta](#family-system_meta) | 11 | 1 | 1 |

### Family: da_outcome

| key | producers | consumers | scale | permanence | horizon | agreement |
|---|---|---|---|---|---|---|
| [`da.antinomian_action`](#daantinomian_action) | `domain_actions` | `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` | `territory` | persistent | far | registry ⊃ contracts |
| [`da.covert_betrayal`](#dacovert_betrayal) | `domain_actions` | `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` | `territory` | persistent | far | registry ⊃ contracts |
| [`da.diplomatic_alliance`](#dadiplomatic_alliance) | `domain_actions` | `articulation_layer`, `faction_state` | `territory`, `peninsula` | indelible | far | registry ⊃ contracts |
| [`da.economic_intervention`](#daeconomic_intervention) | `domain_actions` | `articulation_layer`, `faction_state`, `settlement_economy` | `territory` | persistent | near | registry ⊃ contracts |
| [`da.public_governance`](#dapublic_governance) | `domain_actions` | `articulation_layer`, `faction_state`, `npc_behavior` | `territory` | persistent | near | registry ⊃ contracts |

### Family: environmental

| key | producers | consumers | scale | permanence | horizon | agreement |
|---|---|---|---|---|---|---|
| [`env.crisis`](#envcrisis) | `peninsular_strain`, `scenario_authoring` | — | `peninsula` | indelible | far | ABSENT |
| [`env.disaster`](#envdisaster) | `peninsular_strain`, `scenario_authoring` | `articulation_layer`, `faction_state`, `settlement_layer` | `territory` | persistent | near | registry ⊃ contracts |
| [`env.peninsular_strain_shock`](#envpeninsular_strain_shock) | `peninsular_strain` | `articulation_layer`, `faction_state`, `npc_behavior`, `settlement_layer` | `peninsula` | persistent | far | registry ⊃ contracts |
| [`env.population_change`](#envpopulation_change) | `peninsular_strain`, `settlement_layer` | `faction_state`, `settlement_economy` | `settlement`, `territory` | persistent | near | agreed |

### Family: mechanical_event

| key | producers | consumers | scale | permanence | horizon | agreement |
|---|---|---|---|---|---|---|
| [`mechanical.accounting`](#mechanicalaccounting) | `engine_clock` | `articulation_layer`, `faction_state` | `peninsula` | indelible | immediate | registry ⊃ contracts |
| [`mechanical.cascade_resolution`](#mechanicalcascade_resolution) | `faction_state` | `articulation_layer`, `faction_state`, `npc_behavior` | `territory` | persistent | near | registry ⊃ contracts |
| [`mechanical.era_transition`](#mechanicalera_transition) | `victory` | — | `peninsula` | indelible | far | ABSENT |
| [`mechanical.mission_shift`](#mechanicalmission_shift) | `faction_state` | `articulation_layer`, `faction_state`, `npc_behavior` | `territory`, `peninsula` | indelible | far | registry ⊃ contracts |
| [`mechanical.project_advanced`](#mechanicalproject_advanced) | `npc_behavior` | `articulation_layer`, `npc_behavior` | `personal` | persistent | near | registry ⊃ contracts |
| [`mechanical.scene_entered`](#mechanicalscene_entered) | `game_director`, `scene_slate` | `articulation_layer`, `audit`, `scene_timer` | `personal`, `territory`, `peninsula` | persistent | immediate | registry ⊃ contracts |
| [`mechanical.scene_exited`](#mechanicalscene_exited) | `game_director` | `articulation_layer`, `audit`, `scene_timer` | `personal`, `territory`, `peninsula` | persistent | immediate | registry ⊃ contracts |
| [`mechanical.scene_skipped`](#mechanicalscene_skipped) | `game_director` | `audit`, `scene_timer` | `personal`, `territory` | persistent | immediate | agreed |
| [`mechanical.season_change`](#mechanicalseason_change) | `engine_clock` | — | `peninsula` | indelible | immediate | ABSENT |
| [`mechanical.second_calamity`](#mechanicalsecond_calamity) | `victory` | — | `peninsula` | indelible | far | ABSENT |
| [`mechanical.settlement_captured`](#mechanicalsettlement_captured) | `settlement_layer` | — | `settlement`, `territory` | indelible | near | ABSENT |
| [`mechanical.theocracy_unification_declared`](#mechanicaltheocracy_unification_declared) | `ci_political`, `territorial_piety` | — | `territory`, `peninsula` | indelible | far | ABSENT |

### Family: scene_event

| key | producers | consumers | scale | permanence | horizon | agreement |
|---|---|---|---|---|---|---|
| [`scene.dialogue`](#scenedialogue) | `npc_behavior`, `scene_slate`, `social_contest` | `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` | `personal` | persistent | near | registry ⊃ contracts |
| [`scene.displacement`](#scenedisplacement) | `npc_behavior` | `articulation_layer`, `npc_behavior` | `personal` | transient | immediate | registry ⊃ contracts |
| [`scene.draft_da`](#scenedraft_da) | `domain_actions` | `articulation_layer`, `npc_behavior` | `personal` | transient | immediate | registry ⊃ contracts |
| [`scene.gift`](#scenegift) | `fieldwork_knots`, `scene_slate` | `articulation_layer`, `faction_state`, `npc_behavior` | `personal` | persistent | near | registry ⊃ contracts |
| [`scene.insult`](#sceneinsult) | `scene_slate`, `social_contest` | `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` | `personal` | persistent | near | registry ⊃ contracts |
| [`scene.thread_operation`](#scenethread_operation) | `threadwork` | `articulation_layer`, `npc_behavior` | `personal` | persistent | near | registry ⊃ contracts |
| [`scene.threat`](#scenethreat) | `scene_slate`, `social_contest` | `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` | `personal` | persistent | near | registry ⊃ contracts |
| [`scene.witness`](#scenewitness) | `npc_behavior`, `scene_slate` | `articulation_layer`, `npc_behavior`, `piety_track` | `personal` | persistent | near | registry ⊃ contracts |

### Family: scene_outcome

| key | producers | consumers | scale | permanence | horizon | agreement |
|---|---|---|---|---|---|---|
| [`scene.accord_echo`](#sceneaccord_echo) | `echo_transport` | `articulation_layer` | `settlement` | persistent | near | registry only |
| [`scene.battle_concluded`](#scenebattle_concluded) | `mass_battle` | `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` | `territory` | indelible | far | registry ⊃ contracts |
| [`scene.combat_felled`](#scenecombat_felled) | `personal_combat` | `articulation_layer`, `faction_state`, `npc_behavior` | `personal` | indelible | near | registry ⊃ contracts |
| [`scene.combat_hit`](#scenecombat_hit) | `personal_combat` | `personal_combat` | `personal` | transient | immediate | agreed |
| [`scene.combat_resolved`](#scenecombat_resolved) | `personal_combat` | `articulation_layer`, `faction_state`, `npc_behavior` | `personal` | persistent | near | registry ⊃ contracts |
| [`scene.combat_strike`](#scenecombat_strike) | `player_input`, `scene_slate` | `personal_combat` | `personal` | transient | immediate | agreed |
| [`scene.contest_resolved`](#scenecontest_resolved) | `social_contest` | `articulation_layer`, `faction_state`, `npc_behavior` | `personal` | persistent | near | registry ⊃ contracts |
| [`scene.investigation_resolved`](#sceneinvestigation_resolved) | `faction_politics`, `scene_slate` | `articulation_layer`, `faction_state`, `npc_behavior` | `territory` | indelible | far | registry ⊃ contracts |

### Family: state_transition

| key | producers | consumers | scale | permanence | horizon | agreement |
|---|---|---|---|---|---|---|
| [`state.coup_attempted`](#statecoup_attempted) | `faction_politics` | `articulation_layer`, `faction_state`, `npc_behavior` | `territory` | indelible | far | registry ⊃ contracts |
| [`state.project_completed`](#stateproject_completed) | `npc_behavior` | `articulation_layer`, `npc_behavior` | `personal` | persistent | near | registry ⊃ contracts |
| [`state.project_failed`](#stateproject_failed) | `npc_behavior` | `articulation_layer`, `npc_behavior` | `personal` | persistent | near | registry ⊃ contracts |
| [`state.scar_acquired`](#statescar_acquired) | `piety_track` | `articulation_layer`, `faction_state`, `npc_behavior` | `personal` | indelible | far | registry ⊃ contracts |
| [`state.settlement_revolt`](#statesettlement_revolt) | `settlement_layer` | — | `settlement`, `territory` | indelible | near | ABSENT |
| [`state.standing_change`](#statestanding_change) | `faction_politics`, `faction_state` | `articulation_layer`, `faction_state`, `npc_behavior` | `territory` | indelible | far | registry ⊃ contracts |
| [`state.succession`](#statesuccession) | `faction_politics` | `articulation_layer`, `faction_state`, `npc_behavior` | `territory`, `peninsula` | indelible | far | registry ⊃ contracts |

### Family: system_meta

| key | producers | consumers | scale | permanence | horizon | agreement |
|---|---|---|---|---|---|---|
| [`meta.cascade_cluster_event`](#metacascade_cluster_event) | `articulation_layer` | `articulation_layer` | `territorial` | persistent | far | registry only |
| [`meta.knot_formed`](#metaknot_formed) | `fieldwork_knots` | `articulation_layer`, `npc_behavior` | `personal` | indelible | far | registry ⊃ contracts |
| [`meta.knot_ruptured`](#metaknot_ruptured) | `fieldwork_knots` | `articulation_layer`, `npc_behavior`, `piety_track` | `personal` | indelible | far | registry ⊃ contracts |
| [`meta.legacy_event`](#metalegacy_event) | — | — | `system_meta` | transient | immediate | ABSENT |
| [`meta.miraculous_event`](#metamiraculous_event) | `miraculous_event` | `articulation_layer`, `faction_state`, `npc_behavior` | `personal`, `settlement`, `peninsula` | indelible | far | registry ⊃ contracts |
| [`meta.thread_woven`](#metathread_woven) | `threadwork` | `articulation_layer`, `npc_behavior`, `piety_track` | `personal` | persistent | near | registry ⊃ contracts |
| [`scene.gossip`](#scenegossip) | `npc_behavior` | `articulation_layer`, `npc_memory` | `personal` | structural | medium | registry ⊃ contracts |
| [`scene.interaction`](#sceneinteraction) | `npc_behavior` | `articulation_layer`, `npc_memory` | `personal` | transient | immediate | registry ⊃ contracts |
| [`state.belief_revised`](#statebelief_revised) | `fieldwork_knots`, `npc_behavior` | `articulation_layer`, `npc_behavior` | `personal` | indelible | far | registry ⊃ contracts |
| [`state.concern_resolved`](#stateconcern_resolved) | `npc_behavior` | `articulation_layer`, `npc_memory` | `personal` | structural | medium | registry ⊃ contracts |
| [`state.opinion_revised`](#stateopinion_revised) | `npc_behavior` | `articulation_layer`, `npc_memory`, `social_contest` | `personal` | structural | medium | registry ⊃ contracts |

---

## Key detail

### da.antinomian_action

Action that contradicts faction Mission or institutional role.

| field | value |
|---|---|
| family | da_outcome |
| scale | `territory` |
| permanence | persistent |
| time horizon | far |
| payload — required | `faction_id`, `description` |
| payload — optional | `mission_alignment`, `role_violation_severity`, `role_acting` |
| producers (union) | [`domain_actions`](CONTRACT_INDEX.md#domain_actions) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior), [`piety_track`](CONTRACT_INDEX.md#piety_track) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` · contracts: `faction_state`, `npc_behavior`, `piety_track`

### da.covert_betrayal

Covert action against ally or stated mission.

| field | value |
|---|---|
| family | da_outcome |
| scale | `territory` |
| permanence | persistent |
| time horizon | far |
| payload — required | `faction_id`, `target_actor`, `target_faction`, `exposed` |
| payload — optional | `exposure_witnesses`, `mission_alignment`, `role_acting` |
| producers (union) | [`domain_actions`](CONTRACT_INDEX.md#domain_actions) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior), [`piety_track`](CONTRACT_INDEX.md#piety_track) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` · contracts: `faction_state`, `npc_behavior`, `piety_track`

### da.diplomatic_alliance

Treaty, alliance formation, or formal accord.

| field | value |
|---|---|
| family | da_outcome |
| scale | `territory`, `peninsula` |
| permanence | indelible |
| time horizon | far |
| payload — required | `faction_id`, `counterparty_faction`, `terms` |
| payload — optional | `witnesses`, `mission_alignment`, `role_acting` |
| producers (union) | [`domain_actions`](CONTRACT_INDEX.md#domain_actions) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state` · contracts: `faction_state`

### da.economic_intervention

Direct economic action — taxation, market manipulation, sumptuary law, gift to populace.

| field | value |
|---|---|
| family | da_outcome |
| scale | `territory` |
| permanence | persistent |
| time horizon | near |
| payload — required | `faction_id`, `target_territories`, `intervention_type` |
| payload — optional | `mission_alignment`, `magnitude`, `role_acting` |
| producers (union) | [`domain_actions`](CONTRACT_INDEX.md#domain_actions) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`settlement_economy`](CONTRACT_INDEX.md#settlement_economy) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `settlement_economy` · contracts: `faction_state`, `settlement_economy`

### da.public_governance

Visible administrative or sovereign-role action.

| field | value |
|---|---|
| family | da_outcome |
| scale | `territory` |
| permanence | persistent |
| time horizon | near |
| payload — required | `faction_id`, `mission_alignment`, `outcome` |
| payload — optional | `target_territory_id`, `public_ceremony`, `role_acting` |
| producers (union) | [`domain_actions`](CONTRACT_INDEX.md#domain_actions) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior` · contracts: `faction_state`, `npc_behavior`

### env.crisis

Acute peninsula-scale event (war, plague, succession crisis, schism).

| field | value |
|---|---|
| family | environmental |
| scale | `peninsula` |
| permanence | indelible |
| time horizon | far |
| payload — required | `crisis_type`, `affected_territories` |
| payload — optional | `duration`, `causes` |
| producers (union) | [`peninsular_strain`](CONTRACT_INDEX.md#peninsular_strain), [`scenario_authoring`](CONTRACT_INDEX.md#scenario_authoring) |
| consumers (union) | **none — nothing reads this** |

- **Prose naming no module:** `all`

### env.disaster

Localized environmental damage (fire, flood, earthquake, blight).

| field | value |
|---|---|
| family | environmental |
| scale | `territory` |
| permanence | persistent |
| time horizon | near |
| payload — required | `disaster_type`, `affected_territories` |
| payload — optional | `severity` |
| producers (union) | [`peninsular_strain`](CONTRACT_INDEX.md#peninsular_strain), [`scenario_authoring`](CONTRACT_INDEX.md#scenario_authoring) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`settlement_layer`](CONTRACT_INDEX.md#settlement_layer) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `settlement_layer` · contracts: `faction_state`, `settlement_layer`

### env.peninsular_strain_shock

Peninsula-scale Strain delta event.

| field | value |
|---|---|
| family | environmental |
| scale | `peninsula` |
| permanence | persistent |
| time horizon | far |
| payload — required | `strain_delta`, `causes`, `affected_territories` |
| payload — optional | `symbolic_register`, `severity` |
| producers (union) | [`peninsular_strain`](CONTRACT_INDEX.md#peninsular_strain) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior), [`settlement_layer`](CONTRACT_INDEX.md#settlement_layer) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior`, `settlement_layer` · contracts: `faction_state`, `npc_behavior`, `settlement_layer`

### env.population_change

Settlement population shift (migration, mortality, birth surge).

| field | value |
|---|---|
| family | environmental |
| scale | `settlement`, `territory` |
| permanence | persistent |
| time horizon | near |
| payload — required | `territory_id`, `delta`, `cause` |
| payload — optional | `destination_or_origin` |
| producers (union) | [`peninsular_strain`](CONTRACT_INDEX.md#peninsular_strain), [`settlement_layer`](CONTRACT_INDEX.md#settlement_layer) |
| consumers (union) | [`faction_state`](CONTRACT_INDEX.md#faction_state), [`settlement_economy`](CONTRACT_INDEX.md#settlement_economy) |


### mechanical.accounting

Per-season Accounting completed; faction state recomputes.

| field | value |
|---|---|
| family | mechanical_event |
| scale | `peninsula` |
| permanence | indelible |
| time horizon | immediate |
| payload — required | `season_index`, `factions_processed` |
| payload — optional | `annual` |
| producers (union) | [`engine_clock`](CONTRACT_INDEX.md#engine_clock) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state` · contracts: `faction_state`

### mechanical.cascade_resolution

Faction Cascade re-resolved (per PP-686 §3.2).

| field | value |
|---|---|
| family | mechanical_event |
| scale | `territory` |
| permanence | persistent |
| time horizon | near |
| payload — required | `faction_id`, `prior_aggregate`, `new_aggregate`, `cascade_fidelity_change`, `triggered_by` |
| payload — optional | `leader_id_at_resolution` |
| producers (union) | [`faction_state`](CONTRACT_INDEX.md#faction_state) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior` · contracts: `faction_state`, `npc_behavior`

### mechanical.era_transition

World-state era boundary crossed — MS=0 Post-Calamity Era entry (victory_v30 §5.1), MS restored to 20 within 10 seasons Post-Calamity Recovery (§5.1), IP=100 Phased Occupation Era entry incl. the 3-phase escalation (§5.2), all factions dissolved Anarchy Era entry (§5.3). The MS<=5-sustained-10-seasons Second Calamity is registered SEPARATELY (mechanical.second_calamity, below) — victory_v30 §5.1/§5.3 both call it out by name as "the only true campaign terminal", a distinction this registry preserves rather than folding into the general transition type.

| field | value |
|---|---|
| family | mechanical_event |
| scale | `peninsula` |
| permanence | indelible |
| time horizon | far |
| payload — required | `to_era`, `trigger_stat` |
| payload — optional | `occupation_phase` |
| producers (union) | [`victory`](CONTRACT_INDEX.md#victory) |
| consumers (union) | **none — nothing reads this** |

- **producers — registry only.** Only the registry speaks. The contract side is unauthored. Registry: `victory` · contracts: —

### mechanical.mission_shift

Faction Mission redefined (per PP-686 §3.1).

| field | value |
|---|---|
| family | mechanical_event |
| scale | `territory`, `peninsula` |
| permanence | indelible |
| time horizon | far |
| payload — required | `faction_id`, `prior_mission`, `new_mission`, `trigger` |
| payload — optional | `public_announcement` |
| producers (union) | [`faction_state`](CONTRACT_INDEX.md#faction_state) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior` · contracts: `faction_state`, `npc_behavior`

### mechanical.project_advanced

NPC Project advanced one step (Procedure C). Doc-12 §4.1.

| field | value |
|---|---|
| family | mechanical_event |
| scale | `personal` |
| permanence | persistent |
| time horizon | near |
| payload — required | `project_id`, `progress_before`, `progress_after`, `project_domain` |
| payload — optional | `mood_modifier` |
| producers (union) | [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_behavior` · contracts: `npc_behavior`

### mechanical.scene_entered

Scene boundary marker — fired when GameDirector pushes a scene container onto the zoom stack. Payload-only (no state mutation). Wall-clock timestamps are NEVER added to payload — the SceneTimer sidecar records wall-clock to `user://telemetry/<campaign_id>.jsonl` and joins by scene_id at analysis time. This separation preserves PP-687 §6 V4 replay determinism.

| field | value |
|---|---|
| family | mechanical_event |
| scale | `personal`, `territory`, `peninsula` |
| permanence | persistent |
| time horizon | immediate |
| payload — required | `scene_id`, `system_id`, `scope`, `sa_cost_estimated`, `slate_priority`, `season_n`, `parent_scene_id`, `stack_depth_after` |
| payload — optional | `display_name` |
| producers (union) | [`game_director`](CONTRACT_INDEX.md#game_director), [`scene_slate`](CONTRACT_INDEX.md#scene_slate) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`audit`](CONTRACT_INDEX.md#audit), [`scene_timer`](CONTRACT_INDEX.md#scene_timer) |

- **producers — contracts ⊃ registry.** The contracts declare systems the registry does not list. Filing task, in the other direction. Registry: `game_director` · contracts: `game_director`, `scene_slate`
- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `audit`, `scene_timer` · contracts: `audit`, `scene_timer`

### mechanical.scene_exited

Scene boundary marker — fired when GameDirector pops a scene container after `scene_completed` (or on engine cancel). Pairs with scene_entered via scene_id. Wall-clock excluded from payload (see scene_entered notes); SceneTimer sidecar computes elapsed_ms by joining records.

| field | value |
|---|---|
| family | mechanical_event |
| scale | `personal`, `territory`, `peninsula` |
| permanence | persistent |
| time horizon | immediate |
| payload — required | `scene_id`, `sa_cost_actual`, `outcome_class`, `ended_by`, `sufficient_scope` |
| payload — optional | `scopes_invoked`, `coherence_cost` |
| producers (union) | [`game_director`](CONTRACT_INDEX.md#game_director) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`audit`](CONTRACT_INDEX.md#audit), [`scene_timer`](CONTRACT_INDEX.md#scene_timer) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `audit`, `scene_timer` · contracts: `audit`, `scene_timer`

### mechanical.scene_skipped

Scene-opportunity marker — fired when GameDirector resolves an opportunity abstractly (player declined to zoom in, or no container available). No scene_entered/exited pair is emitted; this is the sole record of the dispatch. Carries zero-elapsed sidecar telemetry to support opportunity-density analysis.

| field | value |
|---|---|
| family | mechanical_event |
| scale | `personal`, `territory` |
| permanence | persistent |
| time horizon | immediate |
| payload — required | `scene_id`, `system_id`, `scope`, `slate_priority`, `season_n`, `reason` |
| payload — optional | `source_action_type` |
| producers (union) | [`game_director`](CONTRACT_INDEX.md#game_director) |
| consumers (union) | [`audit`](CONTRACT_INDEX.md#audit), [`scene_timer`](CONTRACT_INDEX.md#scene_timer) |


### mechanical.season_change

Season boundary crossed.

| field | value |
|---|---|
| family | mechanical_event |
| scale | `peninsula` |
| permanence | indelible |
| time horizon | immediate |
| payload — required | `season_index`, `new_season` |
| payload — optional | `annual` |
| producers (union) | [`engine_clock`](CONTRACT_INDEX.md#engine_clock) |
| consumers (union) | **none — nothing reads this** |

- **Prose naming no module:** `all subscribing systems`

### mechanical.second_calamity

MS <= 5 sustained for 10 seasons during the Post-Calamity Era — "the only true campaign terminal" (victory_v30 §5.1, restated §5.3). Kept distinct from mechanical.era_transition because every other era boundary is recoverable (§5.1's own Recovery clause, §5.3's quorum-restoration clause) while this one is not.

| field | value |
|---|---|
| family | mechanical_event |
| scale | `peninsula` |
| permanence | indelible |
| time horizon | far |
| payload — required | `seasons_sustained_at_or_below_5` |
| payload — optional | — |
| producers (union) | [`victory`](CONTRACT_INDEX.md#victory) |
| consumers (union) | **none — nothing reads this** |

- **producers — registry only.** Only the registry speaks. The contract side is unauthored. Registry: `victory` · contracts: —

### mechanical.settlement_captured

Undefended settlement (Defense 0, no garrison) auto-captured on hostile military entry — no roll (settlement_layer_v30 §5.2).

| field | value |
|---|---|
| family | mechanical_event |
| scale | `settlement`, `territory` |
| permanence | indelible |
| time horizon | near |
| payload — required | `settlement_id`, `territory_id`, `capturing_faction_id`, `prior_controlling_faction_id` |
| payload — optional | — |
| producers (union) | [`settlement_layer`](CONTRACT_INDEX.md#settlement_layer) |
| consumers (union) | **none — nothing reads this** |

- **producers — registry only.** Only the registry speaks. The contract side is unauthored. Registry: `settlement_layer` · contracts: —

### mechanical.theocracy_unification_declared

CI reaches 100 — Church publicly declares Papal Sovereignty and triggers the one-shot Mass Seizure on every territory with Church buildings (ci_political_v30 §2.2). The SAME threshold is independently gated by territorial_piety's g_ci100 entry (module_contracts.yaml :288-292), which cites this identical section as its source — one event, registered once, closing both silent emitters named in ED-IN-0014 rather than duplicating a type per module.

| field | value |
|---|---|
| family | mechanical_event |
| scale | `territory`, `peninsula` |
| permanence | indelible |
| time horizon | far |
| payload — required | `ci_value`, `mass_seizure_targets` |
| payload — optional | `outcome` |
| producers (union) | [`ci_political`](CONTRACT_INDEX.md#ci_political), [`territorial_piety`](CONTRACT_INDEX.md#territorial_piety) |
| consumers (union) | **none — nothing reads this** |

- **producers — registry only.** Only the registry speaks. The contract side is unauthored. Registry: `ci_political`, `territorial_piety` · contracts: —

### meta.cascade_cluster_event

Cross-faction cascade cluster forms or dissolves (sustained ≥ 4 seasons of \|cosine similarity\| > 0.40 between two factions' cascade_fidelity_history). A CANONICAL articulation trigger (articulation_layer_v30 §3.1

| field | value |
|---|---|
| family | system_meta |
| scale | `territorial` |
| permanence | persistent |
| time horizon | far |
| payload — required | `cluster_pair`, `similarity`, `cluster_type`, `sustained_seasons` |
| payload — optional | `regime_transition` |
| producers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer) |

- **producers — registry only.** Only the registry speaks. The contract side is unauthored. Registry: `articulation_layer` · contracts: —
- **consumers — registry only.** Only the registry speaks. The contract side is unauthored. Registry: `articulation_layer` · contracts: —

### meta.knot_formed

Knot formed between two NPCs (per fieldwork_socializing §5.6).

| field | value |
|---|---|
| family | system_meta |
| scale | `personal` |
| permanence | indelible |
| time horizon | far |
| payload — required | `participants`, `tier` |
| payload — optional | `formation_scene_id` |
| producers (union) | [`fieldwork_knots`](CONTRACT_INDEX.md#fieldwork_knots) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_behavior` · contracts: `npc_behavior`

### meta.knot_ruptured

Knot rupture event (per ED-773 lifecycle).

| field | value |
|---|---|
| family | system_meta |
| scale | `personal` |
| permanence | indelible |
| time horizon | far |
| payload — required | `knot_id`, `participants`, `cause` |
| payload — optional | `composure_damage`, `witnessed_publicly` |
| producers (union) | [`fieldwork_knots`](CONTRACT_INDEX.md#fieldwork_knots) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior), [`piety_track`](CONTRACT_INDEX.md#piety_track) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_behavior`, `piety_track` · contracts: `npc_behavior`, `piety_track`

### meta.legacy_event

Wrapper for legacy event channels during Phase B partial migration (per substrate spec §7.2).

| field | value |
|---|---|
| family | system_meta |
| scale | `system_meta` |
| permanence | transient |
| time horizon | immediate |
| payload — required | `originating_system`, `legacy_payload` |
| payload — optional | — |
| producers (union) | **none — nothing fills this** |
| consumers (union) | **none — nothing reads this** |

- **Prose naming no module:** `legacy-aware consumers only`, `substrate (auto)`

### meta.miraculous_event

Miraculous Event activated (per miraculous_event_v30.md).

| field | value |
|---|---|
| family | system_meta |
| scale | `personal`, `settlement`, `peninsula` |
| permanence | indelible |
| time horizon | far |
| payload — required | `event_type`, `center_actor`, `witnessed_by` |
| payload — optional | `peninsula_visibility` |
| producers (union) | [`miraculous_event`](CONTRACT_INDEX.md#miraculous_event) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior` · contracts: `faction_state`, `npc_behavior`

### meta.thread_woven

Thread operation completed.

| field | value |
|---|---|
| family | system_meta |
| scale | `personal` |
| permanence | persistent |
| time horizon | near |
| payload — required | `thread_id`, `operating_npc`, `operation_type` |
| payload — optional | `subject_npcs`, `degree_of_success` |
| producers (union) | [`threadwork`](CONTRACT_INDEX.md#threadwork) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior), [`piety_track`](CONTRACT_INDEX.md#piety_track) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_behavior`, `piety_track` · contracts: `npc_behavior`, `piety_track`

### scene.accord_echo

§5.5 Accord Domain Echo — a resolved scene's downstream settlement-Order consequence (scale_transitions_v30.md §5.5, degree-keyed governance/destabilisation/territorial_transfer/violence rows), applied to Settlement.order at the settlement where the scene occurred (AUD-SET-02, :215) and queued to Accounting Step 4c per §5.5's own caption (:221). Distinct from scene.contest_resolved/scene.combat_resolved (the SAME scene resolution's §5.2 Domain Echo Key, a disjoint faction-stat consequence) — one resolved scene may emit both, and this Key's causes[] cites that Key's id when it also fired (OI-28).

| field | value |
|---|---|
| family | scene_outcome |
| scale | `settlement` |
| permanence | persistent |
| time horizon | near |
| payload — required | `scene_outcome`, `target_settlement` |
| payload — optional | `accord_delta` |
| producers (union) | `echo_transport` _(unresolved)_ |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer) |

- **producers — registry only.** Only the registry speaks. The contract side is unauthored. Registry: `echo_transport` · contracts: —
- **consumers — registry only.** Only the registry speaks. The contract side is unauthored. Registry: `articulation_layer` · contracts: —

### scene.battle_concluded

Mass battle ended.

| field | value |
|---|---|
| family | scene_outcome |
| scale | `territory` |
| permanence | indelible |
| time horizon | far |
| payload — required | `battle_id`, `victor`, `casualties_per_side`, `territorial_outcome` |
| payload — optional | `duration_seasons`, `decisive`, `officer_deaths` |
| producers (union) | [`mass_battle`](CONTRACT_INDEX.md#mass_battle) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior), [`piety_track`](CONTRACT_INDEX.md#piety_track) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` · contracts: `faction_state`, `npc_behavior`, `piety_track`

### scene.combat_felled

A combatant incapacitated by Health depletion (ED-1041 wound model). Witnessable; ripples up to factions and into NPC memory.

| field | value |
|---|---|
| family | scene_outcome |
| scale | `personal` |
| permanence | indelible |
| time horizon | near |
| payload — required | `actor_id` |
| payload — optional | `by_actor` |
| producers (union) | [`personal_combat`](CONTRACT_INDEX.md#personal_combat) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior` · contracts: `faction_state`, `npc_behavior`

### scene.combat_hit

A landed blow within a fight; carries the wound as a write-protected `health` stat_delta on the defender target (F1 — the wound rides the substrate, never a direct write). StrikeModule emits; WoundModule consumes.

| field | value |
|---|---|
| family | scene_outcome |
| scale | `personal` |
| permanence | transient |
| time horizon | immediate |
| payload — required | — |
| payload — optional | `degree`, `damage`, `net` |
| producers (union) | [`personal_combat`](CONTRACT_INDEX.md#personal_combat) |
| consumers (union) | [`personal_combat`](CONTRACT_INDEX.md#personal_combat) |


### scene.combat_resolved

Personal / skirmish combat concluded (F3 — the missing combat scene_outcome subtype; mirrors scene.contest_resolved on the combat path).

| field | value |
|---|---|
| family | scene_outcome |
| scale | `personal` |
| permanence | persistent |
| time horizon | near |
| payload — required | `scene_id`, `outcome`, `participants` |
| payload — optional | `casualties`, `wounds_inflicted` |
| producers (union) | [`personal_combat`](CONTRACT_INDEX.md#personal_combat) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior` · contracts: `faction_state`, `npc_behavior`

### scene.combat_strike

A declared combat action (a strike) entering personal-combat resolution — the action-input subtype the CombatEngine's StrikeModule consumes (F3 — combat-path action vocabulary; 2-part family.subtype per registry convention).

| field | value |
|---|---|
| family | scene_outcome |
| scale | `personal` |
| permanence | transient |
| time horizon | immediate |
| payload — required | `attacker`, `defender` |
| payload — optional | `commit`, `weapon` |
| producers (union) | `player_input` _(unresolved)_, [`scene_slate`](CONTRACT_INDEX.md#scene_slate) |
| consumers (union) | [`personal_combat`](CONTRACT_INDEX.md#personal_combat) |

- **producers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `player_input`, `scene_slate` · contracts: `scene_slate`

### scene.contest_resolved

Social contest (Wager, debate) concluded.

| field | value |
|---|---|
| family | scene_outcome |
| scale | `personal` |
| permanence | persistent |
| time horizon | near |
| payload — required | `scene_id`, `outcome`, `participants` |
| payload — optional | `persuasion_track_final`, `rhetorical_style_used` |
| producers (union) | [`social_contest`](CONTRACT_INDEX.md#social_contest) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior` · contracts: `faction_state`, `npc_behavior`

### scene.dialogue

Per-scene exchange of speech; advances persuasion or relational state.

| field | value |
|---|---|
| family | scene_event |
| scale | `personal` |
| permanence | persistent |
| time horizon | near |
| payload — required | `exchange_count`, `initiator_id`, `topic` |
| payload — optional | `rhetorical_style_used`, `persuasion_track_displacement`, `outcome`, `belief_engagement_for`, `inspirations_engaged_for`, `knot_partners_present` |
| producers (union) | [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior), [`scene_slate`](CONTRACT_INDEX.md#scene_slate), [`social_contest`](CONTRACT_INDEX.md#social_contest) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior), [`piety_track`](CONTRACT_INDEX.md#piety_track) |

- **producers — contracts ⊃ registry.** The contracts declare systems the registry does not list. Filing task, in the other direction. Registry: `scene_slate`, `social_contest` · contracts: `npc_behavior`, `scene_slate`, `social_contest`
- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` · contracts: `faction_state`, `npc_behavior`, `piety_track`

### scene.displacement

Displacement / neglect perceived (Procedure displacement_neglect_observed) — an NPC registers being displaced or neglected in a relation.

| field | value |
|---|---|
| family | scene_event |
| scale | `personal` |
| permanence | transient |
| time horizon | immediate |
| payload — required | `observer_id`, `displaced_relation` |
| payload — optional | `displaced_by`, `neglect_context` |
| producers (union) | [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_behavior` · contracts: `npc_behavior`

### scene.draft_da

Domain Action drafted / submitted (pre-resolution); resolution later emits da_outcome.*.

| field | value |
|---|---|
| family | scene_event |
| scale | `personal` |
| permanence | transient |
| time horizon | immediate |
| payload — required | `action_type`, `actor_id` |
| payload — optional | `target_id` |
| producers (union) | [`domain_actions`](CONTRACT_INDEX.md#domain_actions) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_behavior` · contracts: `npc_behavior`

### scene.gift

Material or symbolic transfer between actors.

| field | value |
|---|---|
| family | scene_event |
| scale | `personal` |
| permanence | persistent |
| time horizon | near |
| payload — required | `giver_id`, `receiver_id`, `gift_type` |
| payload — optional | `value`, `public` |
| producers (union) | [`fieldwork_knots`](CONTRACT_INDEX.md#fieldwork_knots), [`scene_slate`](CONTRACT_INDEX.md#scene_slate) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior` · contracts: `faction_state`, `npc_behavior`

### scene.gossip

Emitted by Procedure E §6.3 when cumulative interaction drift > 0.5. Generates a propagatable gossip artifact reachable by inner-circle observers and (via propagation) third-parties. (PP-687 Phase B Stage 1 §7.3)

| field | value |
|---|---|
| family | system_meta |
| scale | `personal` |
| permanence | structural |
| time horizon | medium |
| payload — required | `principals`, `cumulative_drift`, `origin_interaction_key` |
| payload — optional | `propagation_observers` |
| producers (union) | [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_memory`](CONTRACT_INDEX.md#npc_memory) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_memory` · contracts: `npc_memory`

### scene.insult

Public or private dishonor against an actor.

| field | value |
|---|---|
| family | scene_event |
| scale | `personal` |
| permanence | persistent |
| time horizon | near |
| payload — required | `source_actor`, `target_id` |
| payload — optional | `severity`, `witnessed_by` |
| producers (union) | [`scene_slate`](CONTRACT_INDEX.md#scene_slate), [`social_contest`](CONTRACT_INDEX.md#social_contest) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior), [`piety_track`](CONTRACT_INDEX.md#piety_track) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` · contracts: `faction_state`, `npc_behavior`, `piety_track`

### scene.interaction

Emitted by Procedure E (Off-Screen Interactions) for ambient inner-circle interactions and cross-faction Distant Contact. Carries pre-mutation drift values; state.opinion_revised emits separately if drift threshold crossed. (PP-687 Phase B Stage 1 §7.2)

| field | value |
|---|---|
| family | system_meta |
| scale | `personal` |
| permanence | transient |
| time horizon | immediate |
| payload — required | `interaction_type`, `drift_a_to_b`, `drift_b_to_a` |
| payload — optional | `faction`, `shared_conviction_primary`, `cumulative_drift` |
| producers (union) | [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_memory`](CONTRACT_INDEX.md#npc_memory) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_memory` · contracts: `npc_memory`

### scene.investigation_resolved

Investigation, inquiry, or trial concluded.

| field | value |
|---|---|
| family | scene_outcome |
| scale | `territory` |
| permanence | indelible |
| time horizon | far |
| payload — required | `scene_id`, `subject_id`, `finding` |
| payload — optional | `public`, `witnesses`, `sentence` |
| producers (union) | [`faction_politics`](CONTRACT_INDEX.md#faction_politics), [`scene_slate`](CONTRACT_INDEX.md#scene_slate) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior` · contracts: `faction_state`, `npc_behavior`

### scene.thread_operation

Thread operation performed (weave / cut / reinforce); per-scene threadwork act.

| field | value |
|---|---|
| family | scene_event |
| scale | `personal` |
| permanence | persistent |
| time horizon | near |
| payload — required | `operation`, `operator_id` |
| payload — optional | `target_thread`, `operation_scale` |
| producers (union) | [`threadwork`](CONTRACT_INDEX.md#threadwork) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_behavior` · contracts: `npc_behavior`

### scene.threat

Coercive demand against an actor.

| field | value |
|---|---|
| family | scene_event |
| scale | `personal` |
| permanence | persistent |
| time horizon | near |
| payload — required | `threatener`, `threatened`, `demand` |
| payload — optional | `implicit`, `severity` |
| producers (union) | [`scene_slate`](CONTRACT_INDEX.md#scene_slate), [`social_contest`](CONTRACT_INDEX.md#social_contest) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior), [`piety_track`](CONTRACT_INDEX.md#piety_track) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior`, `piety_track` · contracts: `faction_state`, `npc_behavior`, `piety_track`

### scene.witness

NPC observes an event without participating directly.

| field | value |
|---|---|
| family | scene_event |
| scale | `personal` |
| permanence | persistent |
| time horizon | near |
| payload — required | `observed_key_id`, `witness_actor` |
| payload — optional | `thread_event_subtype` |
| producers (union) | [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior), [`scene_slate`](CONTRACT_INDEX.md#scene_slate) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior), [`piety_track`](CONTRACT_INDEX.md#piety_track) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_behavior`, `piety_track` · contracts: `npc_behavior`, `piety_track`

### state.belief_revised

Player Belief revision per fieldwork_socializing §5.5 marker.

| field | value |
|---|---|
| family | system_meta |
| scale | `personal` |
| permanence | indelible |
| time horizon | far |
| payload — required | `npc_id`, `prior_belief`, `new_belief` |
| payload — optional | `triggering_keys` |
| producers (union) | [`fieldwork_knots`](CONTRACT_INDEX.md#fieldwork_knots), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **producers — contracts ⊃ registry.** The contracts declare systems the registry does not list. Filing task, in the other direction. Registry: `fieldwork_knots` · contracts: `fieldwork_knots`, `npc_behavior`
- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_behavior` · contracts: `npc_behavior`

### state.concern_resolved

Emitted by Procedure B (Concern Generation and Resolution) when Concern resolves with subject_npc_id set. Carries resolution polarity and Belief-revision flag. (Belief revision itself emits state.belief_revised separately.) (PP-687 Phase B Stage 1 §7.4)

| field | value |
|---|---|
| family | system_meta |
| scale | `personal` |
| permanence | structural |
| time horizon | medium |
| payload — required | `concern_tag`, `affect` |
| payload — optional | `belief_revision` |
| producers (union) | [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_memory`](CONTRACT_INDEX.md#npc_memory) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_memory` · contracts: `npc_memory`

### state.coup_attempted

Internal challenge to faction leadership.

| field | value |
|---|---|
| family | state_transition |
| scale | `territory` |
| permanence | indelible |
| time horizon | far |
| payload — required | `faction_id`, `challenger_id`, `incumbent_id`, `outcome` |
| payload — optional | `public`, `witnesses` |
| producers (union) | [`faction_politics`](CONTRACT_INDEX.md#faction_politics) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior` · contracts: `faction_state`, `npc_behavior`

### state.opinion_revised

Emitted by Procedure D (Opinion Drift) when an Opinion's affect_axis changes by ≥ 0.5 or confidence value changes. Drives Articulation Tier 2 trigger evaluation. (PP-687 Phase B Stage 1 / political_dynamics_keys_migration_v30 §7.1)

| field | value |
|---|---|
| family | system_meta |
| scale | `personal` |
| permanence | structural |
| time horizon | medium |
| payload — required | `opinion_subject`, `affect_axis_before`, `affect_axis_after`, `confidence_before`, `confidence_after` |
| payload — optional | `driver_memory_refs` |
| producers (union) | [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_memory`](CONTRACT_INDEX.md#npc_memory), [`social_contest`](CONTRACT_INDEX.md#social_contest) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_memory`, `social_contest` · contracts: `npc_memory`, `social_contest`

### state.project_completed

NPC Project completed (progress >= 10; Procedure C). Doc-12 §4.3.

| field | value |
|---|---|
| family | state_transition |
| scale | `personal` |
| permanence | persistent |
| time horizon | near |
| payload — required | `project_id`, `project_domain`, `completion_effect`, `supporters`, `obstructors`, `goal_short` |
| payload — optional | — |
| producers (union) | [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_behavior` · contracts: `npc_behavior`

### state.project_failed

NPC Project failed via stall (seasons_stalled >= 8; Procedure C). Doc-12 §4.2.

| field | value |
|---|---|
| family | state_transition |
| scale | `personal` |
| permanence | persistent |
| time horizon | near |
| payload — required | `project_id`, `failure_mode`, `seasons_stalled` |
| payload — optional | — |
| producers (union) | [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `npc_behavior` · contracts: `npc_behavior`

### state.scar_acquired

NPC takes a Conviction Scar.

| field | value |
|---|---|
| family | state_transition |
| scale | `personal` |
| permanence | indelible |
| time horizon | far |
| payload — required | `npc_id`, `conviction`, `scar_count_before`, `scar_count_after`, `triggering_event_key` |
| payload — optional | `thread_event_subtype` |
| producers (union) | [`piety_track`](CONTRACT_INDEX.md#piety_track) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior` · contracts: `faction_state`, `npc_behavior`

### state.settlement_revolt

Settlement Order reaches 0 — local revolt; governor expelled unless a garrison is present (settlement_layer_v30 §4.3 Settlement Events table, "Order 0" row; also §1.3 "Order 0 = local revolt").

| field | value |
|---|---|
| family | state_transition |
| scale | `settlement`, `territory` |
| permanence | indelible |
| time horizon | near |
| payload — required | `settlement_id`, `territory_id`, `governor_expelled` |
| payload — optional | `controlling_faction_id` |
| producers (union) | [`settlement_layer`](CONTRACT_INDEX.md#settlement_layer) |
| consumers (union) | **none — nothing reads this** |

- **producers — registry only.** Only the registry speaks. The contract side is unauthored. Registry: `settlement_layer` · contracts: —

### state.standing_change

NPC Standing rank shifts (promotion, demotion).

| field | value |
|---|---|
| family | state_transition |
| scale | `territory` |
| permanence | indelible |
| time horizon | far |
| payload — required | `npc_id`, `standing_before`, `standing_after`, `trigger` |
| payload — optional | `decided_by`, `magnitude` |
| producers (union) | [`faction_politics`](CONTRACT_INDEX.md#faction_politics), [`faction_state`](CONTRACT_INDEX.md#faction_state) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior` · contracts: `faction_state`, `npc_behavior`

### state.succession

Leader change in a faction.

| field | value |
|---|---|
| family | state_transition |
| scale | `territory`, `peninsula` |
| permanence | indelible |
| time horizon | far |
| payload — required | `faction_id`, `prior_leader_id`, `new_leader_id`, `succession_mode` |
| payload — optional | `public_ceremony`, `witnesses` |
| producers (union) | [`faction_politics`](CONTRACT_INDEX.md#faction_politics) |
| consumers (union) | [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer), [`faction_state`](CONTRACT_INDEX.md#faction_state), [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) |

- **consumers — registry ⊃ contracts.** The registry names systems the contracts have not declared back. Filing task — no decision needed unless the registry is wrong. Registry: `articulation_layer`, `faction_state`, `npc_behavior` · contracts: `faction_state`, `npc_behavior`
