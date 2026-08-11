# Valoria — Module Contract Index (27 modules)

> **GENERATED** by `tools/build_contract_index.py`. Do not hand-edit — every fact below is rendered from a source file and a hand-edit is silently discarded on the next build.
> Fix a fact at its source: keys in `systems/_architecture/key_type_registry_v30.md`, edges and owned state in `references/module_contracts.yaml`, build status in `references/wiring_manifest.yaml`.

**Sources joined:** `references/module_contracts.yaml` (authored contracts) + `references/key_graph.json` (generated homes/authority) + `references/wiring_manifest.yaml` (build + port status). Key-level companion: [KEY_INDEX.md](KEY_INDEX.md).

`authority` is derived, not stored (Jordan's 2026-08-02 precedence rule): **code** if a declared `sim_module` resolves on disk **or the module is on `build_key_graph.py`'s CODE_EXISTS_UNDECLARED list** (code demonstrably present while its row deliberately declares no `sim_module` — `mass_battle`'s row is MB-lane-owned and IN must not fill it), **prose** if only a design doc exists, **none** if neither. It expires on someone else's commit, which is why nothing hand-annotates it.

---

## Review queue — modules

### 1. Contract violations (22)

From `skills/valoria-module-adjudicator/scripts/contract_adjudicator.py` (checks A1–A12), imported rather than re-implemented.

| check | violations | distinct module pairs | first instance |
|---|---|---|---|
| `A6` | 20 | 9 | edge 'da.antinomian_action' crosses scales ['provincial']→['personal', 'scene'] with no transitions entry on either side (scale_transitions §3/§5) |
| `A8` | 2 | 2 | doc 'systems/characters/conviction_track_v1.md' not declared in canonical_sources |

`A6` spans: `npc_behavior←domain_actions`, `npc_behavior←faction_politics`, `npc_behavior←peninsular_strain`, `piety_track←domain_actions`, `piety_track←scene_slate`, `settlement_economy←domain_actions`, `settlement_economy←peninsular_strain`, `settlement_layer←peninsular_strain`, `settlement_layer←scenario_authoring`

<details><summary><b>A6</b> — 20 violation(s)</summary>

- A6 [npc_behavior←domain_actions]: edge 'da.antinomian_action' crosses scales ['provincial']→['personal', 'scene'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [npc_behavior←domain_actions]: edge 'da.covert_betrayal' crosses scales ['provincial']→['personal', 'scene'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [npc_behavior←domain_actions]: edge 'da.public_governance' crosses scales ['provincial']→['personal', 'scene'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [npc_behavior←peninsular_strain]: edge 'env.peninsular_strain_shock' crosses scales ['peninsula']→['personal', 'scene'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [npc_behavior←faction_politics]: edge 'scene.investigation_resolved' crosses scales ['provincial']→['personal', 'scene'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [npc_behavior←faction_politics]: edge 'state.coup_attempted' crosses scales ['provincial']→['personal', 'scene'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [npc_behavior←faction_politics]: edge 'state.standing_change' crosses scales ['provincial']→['personal', 'scene'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [npc_behavior←faction_politics]: edge 'state.succession' crosses scales ['provincial']→['personal', 'scene'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [npc_behavior←domain_actions]: edge 'scene.draft_da' crosses scales ['provincial']→['personal', 'scene'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [piety_track←domain_actions]: edge 'da.antinomian_action' crosses scales ['provincial']→['personal'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [piety_track←domain_actions]: edge 'da.covert_betrayal' crosses scales ['provincial']→['personal'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [piety_track←scene_slate]: edge 'scene.dialogue' crosses scales ['scene']→['personal'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [piety_track←scene_slate]: edge 'scene.insult' crosses scales ['scene']→['personal'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [piety_track←scene_slate]: edge 'scene.threat' crosses scales ['scene']→['personal'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [piety_track←scene_slate]: edge 'scene.witness' crosses scales ['scene']→['personal'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [settlement_layer←peninsular_strain]: edge 'env.disaster' crosses scales ['peninsula']→['settlement', 'territory'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [settlement_layer←scenario_authoring]: edge 'env.disaster' crosses scales ['peninsula']→['settlement', 'territory'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [settlement_layer←peninsular_strain]: edge 'env.peninsular_strain_shock' crosses scales ['peninsula']→['settlement', 'territory'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [settlement_economy←domain_actions]: edge 'da.economic_intervention' crosses scales ['provincial']→['settlement'] with no transitions entry on either side (scale_transitions §3/§5)
- A6 [settlement_economy←peninsular_strain]: edge 'env.population_change' crosses scales ['peninsula']→['settlement'] with no transitions entry on either side (scale_transitions §3/§5)

</details>

`A8` spans: `piety_track`, `social_contest`

<details><summary><b>A8</b> — 2 violation(s)</summary>

- A8 [piety_track]: doc 'systems/characters/conviction_track_v1.md' not declared in canonical_sources
- A8 [social_contest]: doc 'systems/social_contest/social_contest_v30.md' not declared in canonical_sources

</details>

### 2. Modules with no home

**14** of 27 modules declare no subsystem home, **9** have no design doc, and **8** have neither doc nor code — a declared module that is currently nothing citable.

| module | subsystem | design doc | sim module | authority | status |
|---|---|---|---|---|---|
| [`audit`](CONTRACT_INDEX.md#audit) | **—** | **—** | **—** | **none** | extracted |
| [`campaign_architecture`](CONTRACT_INDEX.md#campaign_architecture) | **—** | `systems/_architecture/campaign_architecture_v30.md` | **—** | prose | stub |
| [`ci_political`](CONTRACT_INDEX.md#ci_political) | **—** | `systems/factions/ci_political_v30.md` | **—** | prose | extracted |
| [`clock_registry`](CONTRACT_INDEX.md#clock_registry) | **—** | `systems/overview/clock_registry_v30.md` | **—** | prose | extracted |
| [`domain_actions`](CONTRACT_INDEX.md#domain_actions) | **—** | **—** | **—** | **none** | extracted |
| [`engine_clock`](CONTRACT_INDEX.md#engine_clock) | **—** | **—** | **—** | **none** | extracted |
| [`faction_politics`](CONTRACT_INDEX.md#faction_politics) | **—** | `systems/factions/faction_politics_v30.md` | **—** | prose | extracted |
| [`game_director`](CONTRACT_INDEX.md#game_director) | **—** | **—** | **—** | **none** | extracted |
| [`mass_battle`](CONTRACT_INDEX.md#mass_battle) | **—** | `systems/mass_battle/mass_battle_v30.md` | **—** | code | extracted |
| [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) | **—** | `systems/factions/political_dynamics_keys_migration_v30.md` | **—** | prose | extracted |
| [`npc_memory`](CONTRACT_INDEX.md#npc_memory) | **—** | **—** | **—** | **none** | extracted |
| [`scenario_authoring`](CONTRACT_INDEX.md#scenario_authoring) | **—** | **—** | **—** | **none** | extracted |
| [`scene_slate`](CONTRACT_INDEX.md#scene_slate) | engine | **—** | `engine/autoload/scene_slate.py` | code | extracted |
| [`scene_timer`](CONTRACT_INDEX.md#scene_timer) | **—** | **—** | **—** | **none** | extracted |
| [`settlement_economy`](CONTRACT_INDEX.md#settlement_economy) | **—** | **—** | **—** | **none** | extracted |

### 3. Stubs

Pointer-only rows carrying zero edges.

| module | note |
|---|---|
| [`campaign_architecture`](CONTRACT_INDEX.md#campaign_architecture) | RECLASSIFIED 2026-06-10: doc is the 2026-04-17 victory-revision CONSOLIDATION (Church infra, RM identity, MS/Coherence reform, Thread revelation, IP escalation, Warden, Portrait/Lineage) — a cross-cutting design doc, not a runtime module; its contents distribute across victory/threadwork/settlement_layer/peninsular_strain. Recommend stub retirement [OPEN — Jordan] |

### 4. Warnings (67)

Not blocking. `W-GAP` entries are the contract authors' own recorded gap notes — read them before treating a blank field as an oversight.

<details><summary>show all</summary>

- W-GAP [faction_state]: V1 gap RESOLVED by registry matrix: faction_layer emits mechanical.cascade_resolution, mechanical.mission_shift, state.standing_change (was: "type ids unnamed" in substrate §8.6)
- W-GAP [faction_state]: registry system name faction_layer vs module faction_state — vocabulary unification [OPEN — Jordan]
- W-GAP [faction_state]: SCOPE [verification A6]: faction_state = {faction_layer_v30 (stability/occupation/treaties/parliament) + faction_behavior_v30 (PP-686 mission/cascade/expectation/Mandate)}; the doc field names only faction_behavior_v30. Boundary vs faction_politics (rank ladder) is the registry dual-emit on state.standing_change/coup_attempted/succession.
- W-GAP [npc_behavior]: CONSOLIDATED 2026-06-10: absorbs former political_dynamics module — political_dynamics_keys_migration_v30 is "Doc 12 Procedures — Key-Migration Spec (PP-687)" i.e. THIS system's Keys migration, not a separate political-dynamics system. The v1 political_dynamics record (incl. its scene.dialogue emit, unsupported by registry) is superseded by this entry. Mechanical-tier consolidation, Jordan-vetoable.
- W-GAP [npc_behavior]: SUPERSEDED 2026-07-07 (ED-IN-0023 / C-KEY-6): the four types this note flagged as registry-absent (scene.displacement, mechanical.project_advanced, state.project_failed, state.project_completed) were registered by ED-935 (2026-06-14, key_type_registry_v30 §9). The residual gap was that npc_behavior's own consumes[] never added the corresponding edges (plus scene.thread_operation / scene.draft_da, also registry-declared to it) despite being both self-loop consumer and emitter for four — closed by this same commit's consumes[] additions above.
- W-GAP [npc_behavior]: Accounting sequence (doc-12 §8, canonical): mechanical.accounting boundary -> Procedure B (Knowledge Decay -> Generation -> Resolution) -> DA Proposal Phase -> C -> D -> E; substrate §4.1 single-update rule processes emissions inline
- W-GAP [npc_behavior]: OI-24 residue CLOSED 2026-07-29 (W3 item 3 contract-truth sweep): the emits:[] inline comments on the same four types (scene.displacement, mechanical.project_advanced, state.project_failed, state.project_completed) still asserted 'NOT in registry' after the SUPERSEDED note above had already recorded ED-935's registration — a stale comment/gap_note contradiction, not a live gap. Verified in-tree against key_type_registry_v30.md (§4/§5 entries, emitting_systems: [npc_behavior]) that the SUPERSEDED note is the true state; the four emits:[] comments corrected to match.
- W-GAP [npc_behavior]: C-KEY-2 CLOSED 2026-07-29 (W3 item 3): doc: repointed from the Key-silent systems/npcs/npc_behavior_v30.md to political_dynamics_keys_migration_v30.md, the module's actual Key-sequencing spec (was cited only under sources:, per audit/2026-07-07-unaddressed-areas-audit/01_workings/cluster_C-KEY.md C-KEY-2). npc_behavior_v30.md remains reachable in sources: above — not superseded, just no longer the doc: pointer.
- W-GAP [npc_memory]: home doc unlocated — Memory schema lives in doc-12 §2.3 schema bridge; standalone spec [GAP]
- W-GAP [piety_track]: NAME COLLISION (3-way) [OPEN — Jordan]: substrate §8.4 "Piety Track" (this personal scar system, registry system conviction_track, home systems/characters/conviction_track_v1.md) vs systems/characters/conviction_track_v30.md which is the TERRITORIAL "Piety Track & Church Victory Redesign" (PP-406-418, CV per territory) — two different systems share both names
- W-GAP [territorial_piety]: CANONICAL BG-era doc with ZERO Key integration — no emitting/consuming_systems entry in the registry names it; CV drift consumes thread-op effects (§1.3b ED-676) and Calamity drift (§1.3) with no Key types [registry §10 candidate / Keys-migration pending]
- W-GAP [territorial_piety]: name collision with personal piety_track — see piety_track gap_note [OPEN — Jordan]
- W-GAP [territorial_piety]: Key types registered (W3, ED-IN-0096): mechanical.theocracy_unification_declared — emits: declaration lands with the module's build so the census never carries a declared-emit-no-consumer row; see key_type_registry entries for held consumer dispositions.
- W-GAP [threadwork]: threadwork_v30 header: "design proposal, requires editorial approval" yet carries CANONICAL POOL NOTICE — doc status ambiguity [OPEN — Jordan]
- W-GAP [fieldwork_knots]: registry attributes scene.gift emission to fieldwork (gift-giving as fieldwork social action) — cross-check vs scene_slate emitting same type
- W-GAP [fieldwork_knots]: knots_v30 §6.1/§6.2/§11 carried the pre-ED-912 tier-capacity model + −4 betrayal-rupture value after TIER-DRIFT-001/COMPOSURE-DRIFT-001 were RESOLVED by Jordan (ED-912, 2026-06-28); propagation gap closed 2026-07-07 (ED-FI-0003) — §11 now records the resolution instead of forward-flagging it. Residual: §6.2 Coherence-loss rule [UNVERIFIED post-ED-912]; systems/fieldwork/sim/knots.py rebuild = Stratum B (C-TW-12)
- W-GAP [scene_slate]: home doc unlocated — scene slate spec referenced from settlement_layer §4.1 and substrate §8.5; standalone doc [GAP]
- W-GAP [game_director]: registry-derived; home doc unlocated [GAP]; see scene_slate attribution conflict on mechanical.scene_entered
- W-GAP [scene_timer]: registry-derived; home doc unlocated [GAP]
- W-GAP [audit]: registry-derived; runtime-system vs QA-tooling classification [OPEN — Jordan]; home doc unlocated [GAP]
- W-GAP [domain_actions]: home doc unlocated [GAP] — DA resolver spec at designs/audit/2026-05-28-resolution-diagnostic/domain_action_resolver_spec.md is audit output, not a designs/ home
- W-GAP [domain_actions]: ED-FA-0006 (2026-07-08, pessimist-action audit REFINE — resolves the C-FA-12 triple-vocabulary defect): the da.* five-bucket set is an OUTCOME-TAG taxonomy (it classifies a resolved Domain Action's *consequence* for generic consumers like faction_state/npc_behavior), realized as a per-verb tag on the EXISTING Domain-Action catalogs -- engine/params/bg/core.md Standard Action Ob Reference, faction_layer_v30 §5.4 Parliamentary, engine/params/bg/faction_actions.md unique cards -- NOT a standalone module needing its own design doc. The doc:null closure therefore shrinks from 'author a new system' to 'add the per-verb da.* tag + a short crosswalk note' (a REFINE, not a new-doc GAP).
- W-GAP [domain_actions]: ED-FA-0006 residual authoring task (per-verb bucket assignment — the audit deliberately did NOT fabricate this; intent gate UNDETERMINED, boundaries are Jordan's ruling): DIRECTIONAL first pass only -- Treaty/Diplomacy/Recognition-Challenge/Succession-Endorsement/War-Authorisation -> da.diplomatic_alliance; Spy/Investigate/Counter-Intelligence + covert unique cards -> da.covert_betrayal; Govern/Trade/Subsidy/Piety-Spread/Community-Organising/Martial-Governance -> da.public_governance or da.economic_intervention; Censure/Embargo/Outlawry/Excommunication/Active-Inquisition/Church-Seizure -> da.antinomian_action (coercive) or da.public_governance. Genuinely ambiguous boundaries flagged for Jordan, NOT ruled here: (a) economic_intervention vs public_governance for fiscal-administrative verbs; (b) antinomian_action vs public_governance for punitive-institutional verbs; (c) covert_betrayal scope for lawful intelligence (Spy/Investigate) vs treachery proper. Direct-effect military verbs (Muster/March/Fortify/Blockade-Naval) are not consequence-classified and take no da.* tag.
- A4 [peninsular_strain]: non-terminal emission 'env.crisis' has no declared consumer (universal readers ['articulation_layer', 'fieldwork_knots'] see it but do not count)
- W-GAP [peninsular_strain]: GAP-F1 residual (2026-07-29, W3 item 3 / OI-32a): MS ownership declared above (mechanically determinable per audit/2026-07-14-gameplay-subsystem-observatory/remediation_plan_v1.md's 'MS contract owner' item). That remediation item also proposed adding a drafted substrate_state/peninsular entry emitting env.ms_delta pointing at the PP-255 decay — deliberately NOT done here: no consumer for env.ms_delta is declared anywhere in the corpus, so adding the emit would create a NEW dangling emit rather than close one (this wave's header corrections bar that). Recorded as an open residual, not fabricated as a closed item.
- W-GAP [settlement_layer]: settlement_layer_v30_index.md is STALE — predates LPS-2e §1.8 (no §1.8 row); index pipeline regeneration needed [tooling defect]
- W-GAP [settlement_layer]: Key types registered (W3, ED-IN-0096): state.settlement_revolt, mechanical.settlement_captured — emits: declaration lands with the module's build so the census never carries a declared-emit-no-consumer row; see key_type_registry entries for held consumer dispositions.
- W-GAP [settlement_economy]: registry-derived; relationship to settlement_layer §1.3 Local Economy derived value unestablished — possibly the same system [OPEN — Jordan]; home doc [GAP]
- W-GAP [settlement_economy]: RECOMMEND RETIRE [verification Lens-2/LD-2]: phantom module (no doc/state/logic). Fold da.economic_intervention -> settlement_layer Prosperity delta; re-point env.population_change consumer to settlement_layer. Adding a Population stat is a DESIGN decision (deferred — open_decisions §2). Self-edge hazard: settlement_layer both emits and would consume env.population_change — route peninsular_strain -> settlement_layer.
- W-GAP [settlement_economy]: ED-SE-0005 (2026-07-08): the SETTLEMENT-ACTION side of this retirement is CONFIRMED by the ratified pessimist-action audit (ED-IN-0027). The player_agency_v30 §9 Trade action -- this phantom module's likely intended settlement-economy player verb -- is PRUNED and folded into the existing income sources; no dedicated settlement-economy player action survives. The da.economic_intervention -> settlement_layer Prosperity fold and the deferred Population-stat design decision (above) remain the open structural half.
- W-GAP [ci_political]: ZERO Key integration in a CANONICAL doc — no registry entry names ci_political; CI=100 Theocracy Unification Attempt (§2.2) is unkeyed [registry §10 candidate]
- W-GAP [ci_political]: Key types registered (W3, ED-IN-0096): mechanical.theocracy_unification_declared — emits: declaration lands with the module's build so the census never carries a declared-emit-no-consumer row; see key_type_registry entries for held consumer dispositions.
- W-GAP [victory]: world-state era transitions (§5: MS=0 Post-Calamity, IP=100 Phased Occupation, all-dissolved Anarchy) are UNKEYED — no mechanical_event/state_transition type exists; articulation is blind to era changes via the Key stream [registry §10 candidate]
- W-GAP [victory]: doc status: "DESIGN — pending Varfell Path B user decision (ED-311)" — not CANONICAL
- W-GAP [victory]: victory_v30_index.md STALE: §5.1 indexed as "RS=0" but doc reads "MS=0" [index pipeline defect, same class as settlement]
- W-GAP [victory]: g_ms0/g_ms5/g_msrec 'MS (unowned clock)' annotations CORRECTED 2026-07-29 (OI-32a, W3 item 3): MS is now declared owned by peninsular_strain's state: block (GAP-F1 ownership declaration) — these three gates' reads: now point at the new owner instead of asserting no module owns it.
- W-GAP [victory]: Key types registered (W3, ED-IN-0096): mechanical.era_transition, mechanical.second_calamity — emits: declaration lands with the module's build so the census never carries a declared-emit-no-consumer row; see key_type_registry entries for held consumer dispositions.
- A4 [engine_clock]: non-terminal emission 'mechanical.season_change' has no declared consumer (universal readers ['articulation_layer', 'fieldwork_knots'] see it but do not count)
- W-GAP [engine_clock]: registry-derived; home doc unlocated [GAP] — campaign_architecture_v30 examined and is NOT it (victory-revision consolidation, no clock-spine sections)
- W-GAP [engine_clock]: 2026-07-02: systems/_architecture/propagation_spec_v1.md (ED-1093, CANONICAL per ED-1094 merge-ratifies-by-default) supplies the candidate home doc. ED-1051, open — awaiting Jordan: doc: null stays unflipped until then (a separate editorial item this doc's ratification does not by itself close).
- W-GAP [faction_politics]: registry-derived; distinct system from faction_layer per registry vocabulary (emits succession/coup/standing/investigation) — boundary vs faction_state unestablished [OPEN — Jordan]; home doc [GAP]
- W-GAP [faction_politics]: home doc [GAP] closed 2026-07-08 (ED-IN-0016): the 'home doc [GAP]' clause above is now stale — doc: field flipped to systems/factions/faction_politics_v30.md. The faction_politics-vs-faction_state boundary question remains genuinely open.
- W-GAP [faction_politics]: state: [] CLOSED 2026-07-29 (W3 item 3, OI-24/OI-20 contract half): declared the 3 top-level state items (Standing, Coup posture, Succession status) directly off faction_politics_v30.md §1.0/§1.0a/§1.1-1.4/§6/§10.1. This is a contract-truth declaration, not a sim build — OI-20's sim half stays DEFERRED to the FA lane (§3.5 of the orchestration plan).
- W-GAP [miraculous_event]: registry-derived; system-vs-event-source classification [OPEN — Jordan] (godot_conversion_strategy_v1.md register item #23, unresolved). Home doc RESOLVED (verification P6): systems/world/miraculous_event_v30.md, ## Status: CANONICAL — the prior 'home doc [GAP]' clause was stale and contradicted this entry's own doc: field/comment (L738). [ED-IN-0023, C-INJ-2]
- A4 [scenario_authoring]: non-terminal emission 'env.crisis' has no declared consumer (universal readers ['articulation_layer', 'fieldwork_knots'] see it but do not count)
- W-GAP [scenario_authoring]: registry-derived; authoring-time (compile-time) confirmed — fork 11 RATIFIED 2026-07-05 (ED-IN-0011): compile is authoring-time, its output packs seed runtime. Execution unbuilt (no Stage-1 compile tooling / template-pack format / settlement_layer injection wiring — C-INJ-5). Home doc still [GAP]: no dedicated scenario_authoring design doc exists (C-INJ-3). [ED-IN-0023]
- W-GAP [articulation_layer]: significance function and any belief_revised emission path not extracted; §8.7 names registry extensions, not articulation's own emit set
- W-GAP [clock_registry]: pure manifest — every listed clock is owned by its source system; carries PROVISIONAL flags ED-793/794/795 (staleness verifications pending)
- W-GAP [personal_combat]: EXTRACTED 2026-06-23: the v2 deferral ('canonical-candidate, extraction deferred until ratification') is RESOLVED — combat_engine_v1 was ratified CANONICAL by ED-900/904 and docket ED-1029; the only thing keeping the trigger from firing was the stale README 'canonical-candidate' line (audit F6), corrected this pass.
- W-GAP [personal_combat]: MODEL CORRECTION: resolver is d_sigma (sigma-leverage), NOT the v30 dice_pool model (pool=Agi×2, TN-7, damage=net_hits+STR) that the Godot skeleton placeholder, systems/combat/sim/combat.py, mechanics_index.yaml, and data_serialization_spec.md WeaponData all still carried. Canonical: pool=max(5,History+6); additive-coupled damage (Str+heft)*coupling*1.55; bilateral-Ob wounds (ED-1041, supersedes the -1D aggressor-only pool penalty).
- W-GAP [personal_combat]: F3 RESOLVED: the scene_outcome family now carries personal-combat outcome Key types — scene.combat_hit / scene.combat_resolved / scene.combat_felled registered in godot/skeleton/data/key_types/ (was: registry §7 had contest/battle/investigation only).
- W-GAP [personal_combat]: SLICE: combat.strike + combat.wound are PORTED + validated to the Godot shape; the remaining 9 action/substrate modules are PENDING the full port (implementation_sequence Phase G3).
- W-GAP [personal_combat]: CONSUMER WIRING (A4, surfaced): scene.combat_resolved / scene.combat_felled are declared with consuming_systems [npc_behavior, faction_layer, articulation] in the registry, but those modules' contract `consumes` lists do not yet name them — the KeyBus delivers to observers/subscribers regardless; the contract declaration follows when npc_behavior/faction_state are next touched (the README's combat→faction/NPC ripple). CLOSED 2026-07-29 (W3 item 5): npc_behavior + faction_state consumes:[] now declare both types (declared intent; runtime gated on those modules being built — npc_behavior has zero .py files). articulation's consumer edge is Wave 3 item 1's territory (L-consumers lane), not this file.
- W-GAP [campaign_architecture]: RECLASSIFIED 2026-06-10: doc is the 2026-04-17 victory-revision CONSOLIDATION (Church infra, RM identity, MS/Coherence reform, Thread revelation, IP escalation, Warden, Portrait/Lineage) — a cross-cutting design doc, not a runtime module; its contents distribute across victory/threadwork/settlement_layer/peninsular_strain. Recommend stub retirement [OPEN — Jordan]
- W-GAP [campaign_architecture]: clock-spine hypothesis WITHDRAWN — engine_clock is the registry system for season/accounting; its home doc remains unlocated
- W-DOC [npc_memory]: extracted module with no located home doc (edges grounded in sources[]: political_dynamics_keys_migration_v30 §2.3 [READ: 2026-06-10]; key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10])
- W-DOC [scene_slate]: extracted module with no located home doc (edges grounded in sources[]: key_substrate_v30 §8.5 [READ: 2026-06-10]; settlement_layer_v30 §4.1 [READ: 2026-06-10]; key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10])
- W-DOC [game_director]: extracted module with no located home doc (edges grounded in sources[]: key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10])
- W-DOC [scene_timer]: extracted module with no located home doc (edges grounded in sources[]: key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10])
- W-DOC [audit]: extracted module with no located home doc (edges grounded in sources[]: key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10])
- W-DOC [domain_actions]: extracted module with no located home doc (edges grounded in sources[]: key_substrate_v30 §8.6 [READ: 2026-06-10]; key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]; designs/audit/2026-07-08-pessimist-action-audit/ (ED-FA-0006 da.* crosswalk decision) [READ: 2026-07-08])
- W-DOC [settlement_economy]: extracted module with no located home doc (edges grounded in sources[]: key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10])
- W-DOC [engine_clock]: extracted module with no located home doc (edges grounded in sources[]: key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10])
- W-DOC [scenario_authoring]: extracted module with no located home doc (edges grounded in sources[]: key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10])
- A9-info: parsed prefix tally {'da': 5, 'env': 4, 'mechanical': 12, 'meta': 6, 'scene': 18, 'state': 10} (scene.* spans scene_event + scene_outcome by design)
- A11-info [faction_state]: derived_value 'Mandate' is computed cross-module (derivation recorded under ['settlement_layer'])
- A11-info [faction_state]: derived_value 'Treasury' is computed cross-module (derivation recorded under ['settlement_layer'])

</details>

---

## Modules at a glance

| module | scales | resolver | authority | build | godot | IN | OUT | state | gates | derivations |
|---|---|---|---|---|---|---|---|---|---|---|
| [`articulation_layer`](CONTRACT_INDEX.md#articulation_layer) | `personal`, `scene`, `provincial` | deterministic_accounting | code | stub | no-oracle | 1 | 0 | 0 | 0 | 0 |
| [`audit`](CONTRACT_INDEX.md#audit) | `scene` | state_reader | none | deferred | no-oracle | 3 | 0 | 0 | 0 | 0 |
| [`campaign_architecture`](CONTRACT_INDEX.md#campaign_architecture) | `provincial` |  | prose | design | retire | 0 | 0 | 0 | 0 | 0 |
| [`ci_political`](CONTRACT_INDEX.md#ci_political) | `provincial` | deterministic_accounting | prose | deferred | no-oracle | 0 | 0 | 3 | 0 | 0 |
| [`clock_registry`](CONTRACT_INDEX.md#clock_registry) | `provincial` | manifest | prose | design | python-oracle | 0 | 0 | 0 | 0 | 0 |
| [`domain_actions`](CONTRACT_INDEX.md#domain_actions) | `provincial` | d_sigma | none | design | no-oracle | 0 | 6 | 0 | 0 | 0 |
| [`engine_clock`](CONTRACT_INDEX.md#engine_clock) | `provincial` | clock_advance | none | design | no-oracle | 0 | 2 | 1 | 0 | 0 |
| [`faction_politics`](CONTRACT_INDEX.md#faction_politics) | `provincial` | deterministic_accounting | prose | deferred | python-oracle | 0 | 4 | 3 | 0 | 0 |
| [`faction_state`](CONTRACT_INDEX.md#faction_state) | `provincial` | deterministic_accounting | code | deferred | python-oracle | 25 | 3 | 3 | 0 | 0 |
| [`fieldwork_knots`](CONTRACT_INDEX.md#fieldwork_knots) | `personal`, `scene` | dice_pool | code | stub | no-oracle | 1 | 4 | 4 | 3 | 0 |
| [`game_director`](CONTRACT_INDEX.md#game_director) | `scene` | manifest | none | deferred | no-oracle | 0 | 3 | 0 | 0 | 0 |
| [`mass_battle`](CONTRACT_INDEX.md#mass_battle) | `scene` | dice_pool | code | live | python-oracle | 0 | 1 | 0 | 0 | 0 |
| [`miraculous_event`](CONTRACT_INDEX.md#miraculous_event) | `personal`, `settlement`, `peninsula` | state_reader | code | stub | no-oracle | 0 | 1 | 0 | 0 | 0 |
| [`npc_behavior`](CONTRACT_INDEX.md#npc_behavior) | `personal`, `scene` | deterministic_accounting | prose | design | no-oracle | 31 | 11 | 4 | 2 | 0 |
| [`npc_memory`](CONTRACT_INDEX.md#npc_memory) | `personal` | state_reader | none | design | no-oracle | 4 | 0 | 0 | 0 | 0 |
| [`peninsular_strain`](CONTRACT_INDEX.md#peninsular_strain) | `peninsula` | deterministic_accounting | code | deferred | no-oracle | 0 | 4 | 3 | 4 | 0 |
| [`personal_combat`](CONTRACT_INDEX.md#personal_combat) | `personal` | d_sigma | code | unwired | gd-ported | 2 | 3 | 6 | 0 | 1 |
| [`piety_track`](CONTRACT_INDEX.md#piety_track) | `personal` | deterministic_accounting | code | deferred | python-oracle | 9 | 1 | 1 | 2 | 0 |
| [`scenario_authoring`](CONTRACT_INDEX.md#scenario_authoring) | `peninsula` | manifest | none | design | no-oracle | 0 | 2 | 0 | 0 | 0 |
| [`scene_slate`](CONTRACT_INDEX.md#scene_slate) | `scene` | manifest | code | deferred | no-oracle | 0 | 8 | 0 | 0 | 0 |
| [`scene_timer`](CONTRACT_INDEX.md#scene_timer) | `scene` | state_reader | none | deferred | no-oracle | 3 | 0 | 0 | 0 | 0 |
| [`settlement_economy`](CONTRACT_INDEX.md#settlement_economy) | `settlement` | deterministic_accounting | none | design | retire | 2 | 0 | 0 | 0 | 0 |
| [`settlement_layer`](CONTRACT_INDEX.md#settlement_layer) | `settlement`, `territory` | deterministic_accounting | code | design | python-oracle | 2 | 1 | 4 | 3 | 7 |
| [`social_contest`](CONTRACT_INDEX.md#social_contest) | `scene` | dice_pool | code | gated | python-oracle | 1 | 4 | 1 | 0 | 0 |
| [`territorial_piety`](CONTRACT_INDEX.md#territorial_piety) | `territory`, `provincial` | deterministic_accounting | code | deferred | python-oracle | 0 | 0 | 2 | 2 | 0 |
| [`threadwork`](CONTRACT_INDEX.md#threadwork) | `personal`, `thread` | dice_pool | code | unwired | python-oracle | 0 | 2 | 2 | 0 | 0 |
| [`victory`](CONTRACT_INDEX.md#victory) | `provincial`, `peninsula` | state_reader | code | live | python-oracle | 0 | 0 | 1 | 4 | 0 |

`build` / `godot` columns are from `wiring_manifest.yaml` (as_of 2026-07-29); a blank means the module has no row there.

---

## Module detail

### articulation_layer

| field | value |
|---|---|
| registry system | `articulation` |
| scales | `personal`, `scene`, `provincial` |
| resolver | `deterministic_accounting` |
| design doc | `systems/articulation/articulation_layer_v30.md` |
| sim module | `engine/cross_scale/articulation.py` |
| authority | code |
| build / godot | stub / no-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

| key | declared producers |
|---|---|
| `*` _(wildcard subscription — every key, not a key type)_ | `engine` |

**OUT** — keys emitted

_none_

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- significance function and any belief_revised emission path not extracted; §8.7 names registry extensions, not articulation's own emit set

**Sources**

`key_substrate_v30 §8.7 [READ: 2026-06-10]`, `key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### audit

| field | value |
|---|---|
| registry system | `audit` |
| scales | `scene` |
| resolver | `state_reader` |
| design doc | **— none** |
| sim module | **— none** |
| authority | none |
| build / godot | deferred / no-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

| key | declared producers |
|---|---|
| [`mechanical.scene_entered`](KEY_INDEX.md#mechanicalscene_entered) | `game_director` |
| [`mechanical.scene_exited`](KEY_INDEX.md#mechanicalscene_exited) | `game_director` |
| [`mechanical.scene_skipped`](KEY_INDEX.md#mechanicalscene_skipped) | `game_director` |

**OUT** — keys emitted

_none_

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- registry-derived; runtime-system vs QA-tooling classification [OPEN — Jordan]; home doc unlocated [GAP]

**Sources**

`key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### campaign_architecture

| field | value |
|---|---|
| registry system |  |
| scales | `provincial` |
| resolver |  |
| design doc | `systems/_architecture/campaign_architecture_v30.md` |
| sim module | **— none** |
| authority | prose |
| build / godot | design / retire |
| status | stub |
| accounting phase |  |

**IN** — keys consumed

_none_

**OUT** — keys emitted

_none_

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- RECLASSIFIED 2026-06-10: doc is the 2026-04-17 victory-revision CONSOLIDATION (Church infra, RM identity, MS/Coherence reform, Thread revelation, IP escalation, Warden, Portrait/Lineage) — a cross-cutting design doc, not a runtime module; its contents distribute across victory/threadwork/settlement_layer/peninsular_strain. Recommend stub retirement [OPEN — Jordan]
- clock-spine hypothesis WITHDRAWN — engine_clock is the registry system for season/accounting; its home doc remains unlocated

### ci_political

| field | value |
|---|---|
| registry system |  |
| scales | `provincial` |
| resolver | `deterministic_accounting` |
| design doc | `systems/factions/ci_political_v30.md` |
| sim module | **— none** |
| authority | prose |
| build / godot | deferred / no-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

_none_

**OUT** — keys emitted

_none_

**Owned state**

| quantity | bucket | writable | note |
|---|---|---|---|
| CI (Church Influence) | `clock` | **no (derived)** |  |
| faction political pool | `pool` | yes |  |
| card hands / cooldown | `track` | yes |  |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- ZERO Key integration in a CANONICAL doc — no registry entry names ci_political; CI=100 Theocracy Unification Attempt (§2.2) is unkeyed [registry §10 candidate]
- Key types registered (W3, ED-IN-0096): mechanical.theocracy_unification_declared — emits: declaration lands with the module's build so the census never carries a declared-emit-no-consumer row; see key_type_registry entries for held consumer dispositions.

**Sources**

`ci_political_v30 full [READ: 2026-06-10]`, `clock_registry_v30 Shared Clocks [READ: 2026-06-10]`

### clock_registry

| field | value |
|---|---|
| registry system |  |
| scales | `provincial` |
| resolver | `manifest` |
| design doc | `systems/overview/clock_registry_v30.md` |
| sim module | **— none** |
| authority | prose |
| build / godot | design / python-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

_none_

**OUT** — keys emitted

_none_

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- pure manifest — every listed clock is owned by its source system; carries PROVISIONAL flags ED-793/794/795 (staleness verifications pending)

**Sources**

`clock_registry_v30 full [READ: 2026-06-10]`

### domain_actions

_Also written as `Domain Echo` in prose._

| field | value |
|---|---|
| registry system | `da_framework` |
| scales | `provincial` |
| resolver | `d_sigma` |
| design doc | **— none** |
| sim module | **— none** |
| authority | none |
| build / godot | design / no-oracle |
| status | extracted |
| accounting phase | ['DA_proposal'] |

**IN** — keys consumed

_none_

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`scene.draft_da`](KEY_INDEX.md#scenedraft_da) | no |  |
| [`da.antinomian_action`](KEY_INDEX.md#daantinomian_action) | no |  |
| [`da.covert_betrayal`](KEY_INDEX.md#dacovert_betrayal) | no |  |
| [`da.diplomatic_alliance`](KEY_INDEX.md#dadiplomatic_alliance) | no |  |
| [`da.economic_intervention`](KEY_INDEX.md#daeconomic_intervention) | no |  |
| [`da.public_governance`](KEY_INDEX.md#dapublic_governance) | no |  |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- home doc unlocated [GAP] — DA resolver spec at designs/audit/2026-05-28-resolution-diagnostic/domain_action_resolver_spec.md is audit output, not a designs/ home
- ED-FA-0006 (2026-07-08, pessimist-action audit REFINE — resolves the C-FA-12 triple-vocabulary defect): the da.* five-bucket set is an OUTCOME-TAG taxonomy (it classifies a resolved Domain Action's *consequence* for generic consumers like faction_state/npc_behavior), realized as a per-verb tag on the EXISTING Domain-Action catalogs -- engine/params/bg/core.md Standard Action Ob Reference, faction_layer_v30 §5.4 Parliamentary, engine/params/bg/faction_actions.md unique cards -- NOT a standalone module needing its own design doc. The doc:null closure therefore shrinks from 'author a new system' to 'add the per-verb da.* tag + a short crosswalk note' (a REFINE, not a new-doc GAP).
- ED-FA-0006 residual authoring task (per-verb bucket assignment — the audit deliberately did NOT fabricate this; intent gate UNDETERMINED, boundaries are Jordan's ruling): DIRECTIONAL first pass only -- Treaty/Diplomacy/Recognition-Challenge/Succession-Endorsement/War-Authorisation -> da.diplomatic_alliance; Spy/Investigate/Counter-Intelligence + covert unique cards -> da.covert_betrayal; Govern/Trade/Subsidy/Piety-Spread/Community-Organising/Martial-Governance -> da.public_governance or da.economic_intervention; Censure/Embargo/Outlawry/Excommunication/Active-Inquisition/Church-Seizure -> da.antinomian_action (coercive) or da.public_governance. Genuinely ambiguous boundaries flagged for Jordan, NOT ruled here: (a) economic_intervention vs public_governance for fiscal-administrative verbs; (b) antinomian_action vs public_governance for punitive-institutional verbs; (c) covert_betrayal scope for lawful intelligence (Spy/Investigate) vs treachery proper. Direct-effect military verbs (Muster/March/Fortify/Blockade-Naval) are not consequence-classified and take no da.* tag.

**Sources**

`key_substrate_v30 §8.6 [READ: 2026-06-10]`, `key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`, `designs/audit/2026-07-08-pessimist-action-audit/ (ED-FA-0006 da.* crosswalk decision) [READ: 2026-07-08]`

### engine_clock

| field | value |
|---|---|
| registry system | `engine_clock` |
| scales | `provincial` |
| resolver | `clock_advance` |
| design doc | **— none** |
| sim module | **— none** |
| authority | none |
| build / godot | design / no-oracle |
| status | extracted |
| accounting phase | ['season_tick', 'accounting_boundary'] |

**IN** — keys consumed

_none_

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`mechanical.accounting`](KEY_INDEX.md#mechanicalaccounting) | no |  |
| [`mechanical.season_change`](KEY_INDEX.md#mechanicalseason_change) | no |  |

**Owned state**

| quantity | bucket | writable | note |
|---|---|---|---|
| season counter | `clock` | yes |  |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- registry-derived; home doc unlocated [GAP] — campaign_architecture_v30 examined and is NOT it (victory-revision consolidation, no clock-spine sections)
- 2026-07-02: systems/_architecture/propagation_spec_v1.md (ED-1093, CANONICAL per ED-1094 merge-ratifies-by-default) supplies the candidate home doc. ED-1051, open — awaiting Jordan: doc: null stays unflipped until then (a separate editorial item this doc's ratification does not by itself close).

**Sources**

`key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### faction_politics

| field | value |
|---|---|
| registry system | `faction_politics` |
| scales | `provincial` |
| resolver | `deterministic_accounting` |
| design doc | `systems/factions/faction_politics_v30.md` |
| sim module | **— none** |
| authority | prose |
| build / godot | deferred / python-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

_none_

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`scene.investigation_resolved`](KEY_INDEX.md#sceneinvestigation_resolved) | no |  |
| [`state.coup_attempted`](KEY_INDEX.md#statecoup_attempted) | no |  |
| [`state.standing_change`](KEY_INDEX.md#statestanding_change) | no |  |
| [`state.succession`](KEY_INDEX.md#statesuccession) | no |  |

**Owned state**

| quantity | bucket | writable | note |
|---|---|---|---|
| Standing | `track` | yes |  |
| Coup posture | `track` | yes |  |
| Succession status | `track` | yes |  |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- registry-derived; distinct system from faction_layer per registry vocabulary (emits succession/coup/standing/investigation) — boundary vs faction_state unestablished [OPEN — Jordan]; home doc [GAP]
- home doc [GAP] closed 2026-07-08 (ED-IN-0016): the 'home doc [GAP]' clause above is now stale — doc: field flipped to systems/factions/faction_politics_v30.md. The faction_politics-vs-faction_state boundary question remains genuinely open.
- state: [] CLOSED 2026-07-29 (W3 item 3, OI-24/OI-20 contract half): declared the 3 top-level state items (Standing, Coup posture, Succession status) directly off faction_politics_v30.md §1.0/§1.0a/§1.1-1.4/§6/§10.1. This is a contract-truth declaration, not a sim build — OI-20's sim half stays DEFERRED to the FA lane (§3.5 of the orchestration plan).

**Sources**

`key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`, `systems/factions/faction_politics_v30.md §1.0, §1.0a, §1.1-§1.4, §6, §10.1 [READ: 2026-07-29]`

### faction_state

_Also written as `Faction Layer` in prose._

| field | value |
|---|---|
| registry system | `faction_layer` |
| scales | `provincial` |
| resolver | `deterministic_accounting` |
| design doc | `systems/factions/faction_behavior_v30.md` |
| sim module | `engine/autoload/game_state.py` |
| authority | code |
| build / godot | deferred / python-oracle |
| status | extracted |
| accounting phase | ['DA_proposal', 'settlement_accounting'] |

**IN** — keys consumed

| key | declared producers |
|---|---|
| [`da.antinomian_action`](KEY_INDEX.md#daantinomian_action) | `domain_actions` |
| [`da.covert_betrayal`](KEY_INDEX.md#dacovert_betrayal) | `domain_actions` |
| [`da.diplomatic_alliance`](KEY_INDEX.md#dadiplomatic_alliance) | `domain_actions` |
| [`da.economic_intervention`](KEY_INDEX.md#daeconomic_intervention) | `domain_actions` |
| [`da.public_governance`](KEY_INDEX.md#dapublic_governance) | `domain_actions` |
| [`env.disaster`](KEY_INDEX.md#envdisaster) | `peninsular_strain`, `scenario_authoring` |
| [`env.peninsular_strain_shock`](KEY_INDEX.md#envpeninsular_strain_shock) | `peninsular_strain` |
| [`env.population_change`](KEY_INDEX.md#envpopulation_change) | `peninsular_strain`, `settlement_layer` |
| [`mechanical.accounting`](KEY_INDEX.md#mechanicalaccounting) | `engine_clock` |
| [`mechanical.cascade_resolution`](KEY_INDEX.md#mechanicalcascade_resolution) | `faction_state` |
| [`mechanical.mission_shift`](KEY_INDEX.md#mechanicalmission_shift) | `faction_state` |
| [`meta.miraculous_event`](KEY_INDEX.md#metamiraculous_event) | `miraculous_event` |
| [`scene.battle_concluded`](KEY_INDEX.md#scenebattle_concluded) | `mass_battle` |
| [`scene.contest_resolved`](KEY_INDEX.md#scenecontest_resolved) | `social_contest` |
| [`scene.dialogue`](KEY_INDEX.md#scenedialogue) | `scene_slate`, `social_contest` |
| [`scene.gift`](KEY_INDEX.md#scenegift) | `fieldwork_knots`, `scene_slate` |
| [`scene.insult`](KEY_INDEX.md#sceneinsult) | `scene_slate`, `social_contest` |
| [`scene.investigation_resolved`](KEY_INDEX.md#sceneinvestigation_resolved) | `faction_politics`, `scene_slate` |
| [`scene.threat`](KEY_INDEX.md#scenethreat) | `scene_slate`, `social_contest` |
| [`state.coup_attempted`](KEY_INDEX.md#statecoup_attempted) | `faction_politics` |
| [`state.scar_acquired`](KEY_INDEX.md#statescar_acquired) | `piety_track` |
| [`state.standing_change`](KEY_INDEX.md#statestanding_change) | `faction_politics`, `faction_state` |
| [`state.succession`](KEY_INDEX.md#statesuccession) | `faction_politics` |
| [`scene.combat_resolved`](KEY_INDEX.md#scenecombat_resolved) | `personal_combat` |
| [`scene.combat_felled`](KEY_INDEX.md#scenecombat_felled) | `personal_combat` |

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`mechanical.cascade_resolution`](KEY_INDEX.md#mechanicalcascade_resolution) | no |  |
| [`mechanical.mission_shift`](KEY_INDEX.md#mechanicalmission_shift) | no |  |
| [`state.standing_change`](KEY_INDEX.md#statestanding_change) | no |  |

**Owned state**

| quantity | bucket | writable | note |
|---|---|---|---|
| Mandate | `derived_value` | **no (derived)** |  |
| Treasury | `derived_value` | **no (derived)** |  |
| faction stats 1-7 | `track` | yes |  |

**Scale transitions**

| field | value |
|---|---|
| via | scale_transitions §3.2 Personal → Faction / §5 Domain Echo |

**Feedback loops**

| with | damper |
|---|---|
| `` |  |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- V1 gap RESOLVED by registry matrix: faction_layer emits mechanical.cascade_resolution, mechanical.mission_shift, state.standing_change (was: "type ids unnamed" in substrate §8.6)
- registry system name faction_layer vs module faction_state — vocabulary unification [OPEN — Jordan]
- SCOPE [verification A6]: faction_state = {faction_layer_v30 (stability/occupation/treaties/parliament) + faction_behavior_v30 (PP-686 mission/cascade/expectation/Mandate)}; the doc field names only faction_behavior_v30. Boundary vs faction_politics (rank ladder) is the registry dual-emit on state.standing_change/coup_attempted/succession.

**Sources**

`key_substrate_v30 §8.1, §8.6 [READ: 2026-06-10]`, `key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`, `settlement_layer_v30 §1.8 LPS-2e [READ: 2026-06-10]`

### fieldwork_knots

_Also written as `Knots` in prose._

| field | value |
|---|---|
| registry system | `fieldwork` |
| scales | `personal`, `scene` |
| resolver | `dice_pool` |
| design doc | `systems/fieldwork/knots_v30.md` |
| sim module | `systems/fieldwork/sim/knots.py` |
| authority | code |
| build / godot | stub / no-oracle |
| status | extracted |
| accounting phase | ['settlement_accounting'] |

**IN** — keys consumed

| key | declared producers |
|---|---|
| `*` _(wildcard subscription — every key, not a key type)_ | `engine` |

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`meta.knot_formed`](KEY_INDEX.md#metaknot_formed) | no |  |
| [`meta.knot_ruptured`](KEY_INDEX.md#metaknot_ruptured) | no |  |
| [`scene.gift`](KEY_INDEX.md#scenegift) | no |  |
| [`state.belief_revised`](KEY_INDEX.md#statebelief_revised) | no |  |

**Owned state**

| quantity | bucket | writable | note |
|---|---|---|---|
| knot strain | `clock` | yes |  |
| Bonds | `track` | yes |  |
| Evidence Track | `clock` | yes |  |
| Disposition Track | `track` | yes |  |

**Gates**

| id | when | then | on | source |
|---|---|---|---|---|
| `g_strain` | Knot strain > capacity | Knot Break | knot strain | knots_v30 §6.1 |
| `g_decay` | no new strain that season AND Disposition >= +3 | Knot strain -1 at Accounting | knot strain | knots_v30 §5 |
| `g_bond5` | Bonds >= 5 | knot operations eligible (Memory-Query-checked prerequisite) | Bonds | key_substrate_v30 §8.4 |

**Scale transitions**

| field | value |
|---|---|
| via | scale_transitions §3.9 Fieldwork ↔ All Systems |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- registry attributes scene.gift emission to fieldwork (gift-giving as fieldwork social action) — cross-check vs scene_slate emitting same type
- knots_v30 §6.1/§6.2/§11 carried the pre-ED-912 tier-capacity model + −4 betrayal-rupture value after TIER-DRIFT-001/COMPOSURE-DRIFT-001 were RESOLVED by Jordan (ED-912, 2026-06-28); propagation gap closed 2026-07-07 (ED-FI-0003) — §11 now records the resolution instead of forward-flagging it. Residual: §6.2 Coherence-loss rule [UNVERIFIED post-ED-912]; systems/fieldwork/sim/knots.py rebuild = Stratum B (C-TW-12)

**Sources**

`knots_v30 full [READ: 2026-06-10]`, `fieldwork_v30 index [READ: 2026-06-10]`, `key_substrate_v30 §8.4, §8.7 [READ: 2026-06-10]`, `key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### game_director

| field | value |
|---|---|
| registry system | `game_director` |
| scales | `scene` |
| resolver | `manifest` |
| design doc | **— none** |
| sim module | **— none** |
| authority | none |
| build / godot | deferred / no-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

_none_

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`mechanical.scene_entered`](KEY_INDEX.md#mechanicalscene_entered) | no |  |
| [`mechanical.scene_exited`](KEY_INDEX.md#mechanicalscene_exited) | no |  |
| [`mechanical.scene_skipped`](KEY_INDEX.md#mechanicalscene_skipped) | no |  |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- registry-derived; home doc unlocated [GAP]; see scene_slate attribution conflict on mechanical.scene_entered

**Sources**

`key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### mass_battle

_Also written as `Mass Combat` in prose._

| field | value |
|---|---|
| registry system | `mass_battle` |
| scales | `scene` |
| resolver | `dice_pool` |
| design doc | `systems/mass_battle/mass_battle_v30.md` |
| sim module | **— none** |
| authority | code |
| build / godot | live / python-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

_none_

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`scene.battle_concluded`](KEY_INDEX.md#scenebattle_concluded) | no |  |

**Scale transitions**

| field | value |
|---|---|
| via | scale_transitions §3.6 Thread → Mass |
| via | scale_transitions §3.7 Mass → Personal (General Duel) |
| via | scale_transitions §3.8 Scene → Mass |

**Sources**

`key_substrate_v30 §8.5 [READ: 2026-06-10]`, `scale_transitions_v30 §3.6-§3.8 [READ: 2026-06-10]`, `key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### miraculous_event

| field | value |
|---|---|
| registry system | `miraculous_event` |
| scales | `personal`, `settlement`, `peninsula` |
| resolver | `state_reader` |
| design doc | `systems/world/miraculous_event_v30.md` |
| sim module | `systems/world/sim/miraculous_event.py` |
| authority | code |
| build / godot | stub / no-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

_none_

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`meta.miraculous_event`](KEY_INDEX.md#metamiraculous_event) | no |  |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- registry-derived; system-vs-event-source classification [OPEN — Jordan] (godot_conversion_strategy_v1.md register item #23, unresolved). Home doc RESOLVED (verification P6): systems/world/miraculous_event_v30.md, ## Status: CANONICAL — the prior 'home doc [GAP]' clause was stale and contradicted this entry's own doc: field/comment (L738). [ED-IN-0023, C-INJ-2]

**Sources**

`key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### npc_behavior

_Also written as `NPC Behaviour` in prose._

| field | value |
|---|---|
| registry system | `npc_behavior (+ Procedures B/D/E)` |
| scales | `personal`, `scene` |
| resolver | `deterministic_accounting` |
| design doc | `systems/factions/political_dynamics_keys_migration_v30.md` |
| sim module | **— none** |
| authority | prose |
| build / godot | design / no-oracle |
| status | extracted |
| accounting phase | ['B_concern', 'C_project', 'D_opinion', 'E_offscreen'] |

**IN** — keys consumed

| key | declared producers |
|---|---|
| [`da.antinomian_action`](KEY_INDEX.md#daantinomian_action) | `domain_actions` |
| [`da.covert_betrayal`](KEY_INDEX.md#dacovert_betrayal) | `domain_actions` |
| [`da.public_governance`](KEY_INDEX.md#dapublic_governance) | `domain_actions` |
| [`env.peninsular_strain_shock`](KEY_INDEX.md#envpeninsular_strain_shock) | `peninsular_strain` |
| [`mechanical.cascade_resolution`](KEY_INDEX.md#mechanicalcascade_resolution) | `faction_state` |
| [`mechanical.mission_shift`](KEY_INDEX.md#mechanicalmission_shift) | `faction_state` |
| [`meta.knot_formed`](KEY_INDEX.md#metaknot_formed) | `fieldwork_knots` |
| [`meta.knot_ruptured`](KEY_INDEX.md#metaknot_ruptured) | `fieldwork_knots` |
| [`meta.miraculous_event`](KEY_INDEX.md#metamiraculous_event) | `miraculous_event` |
| [`meta.thread_woven`](KEY_INDEX.md#metathread_woven) | `threadwork` |
| [`scene.battle_concluded`](KEY_INDEX.md#scenebattle_concluded) | `mass_battle` |
| [`scene.contest_resolved`](KEY_INDEX.md#scenecontest_resolved) | `social_contest` |
| [`scene.dialogue`](KEY_INDEX.md#scenedialogue) | `scene_slate`, `social_contest` |
| [`scene.gift`](KEY_INDEX.md#scenegift) | `fieldwork_knots`, `scene_slate` |
| [`scene.insult`](KEY_INDEX.md#sceneinsult) | `scene_slate`, `social_contest` |
| [`scene.investigation_resolved`](KEY_INDEX.md#sceneinvestigation_resolved) | `faction_politics`, `scene_slate` |
| [`scene.threat`](KEY_INDEX.md#scenethreat) | `scene_slate`, `social_contest` |
| [`scene.witness`](KEY_INDEX.md#scenewitness) | `npc_behavior`, `scene_slate` |
| [`state.belief_revised`](KEY_INDEX.md#statebelief_revised) | `fieldwork_knots` |
| [`state.coup_attempted`](KEY_INDEX.md#statecoup_attempted) | `faction_politics` |
| [`state.scar_acquired`](KEY_INDEX.md#statescar_acquired) | `piety_track` |
| [`state.standing_change`](KEY_INDEX.md#statestanding_change) | `faction_politics`, `faction_state` |
| [`state.succession`](KEY_INDEX.md#statesuccession) | `faction_politics` |
| [`scene.thread_operation`](KEY_INDEX.md#scenethread_operation) | `threadwork` |
| [`scene.draft_da`](KEY_INDEX.md#scenedraft_da) | `domain_actions` |
| [`scene.displacement`](KEY_INDEX.md#scenedisplacement) | `npc_behavior` |
| [`mechanical.project_advanced`](KEY_INDEX.md#mechanicalproject_advanced) | `npc_behavior` |
| [`state.project_completed`](KEY_INDEX.md#stateproject_completed) | `npc_behavior` |
| [`state.project_failed`](KEY_INDEX.md#stateproject_failed) | `npc_behavior` |
| [`scene.combat_resolved`](KEY_INDEX.md#scenecombat_resolved) | `personal_combat` |
| [`scene.combat_felled`](KEY_INDEX.md#scenecombat_felled) | `personal_combat` |

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`scene.witness`](KEY_INDEX.md#scenewitness) | no |  |
| [`state.concern_resolved`](KEY_INDEX.md#stateconcern_resolved) | no |  |
| [`state.belief_revised`](KEY_INDEX.md#statebelief_revised) | no |  |
| [`scene.displacement`](KEY_INDEX.md#scenedisplacement) | no |  |
| [`mechanical.project_advanced`](KEY_INDEX.md#mechanicalproject_advanced) | no |  |
| [`state.project_failed`](KEY_INDEX.md#stateproject_failed) | no |  |
| [`state.project_completed`](KEY_INDEX.md#stateproject_completed) | no |  |
| [`state.opinion_revised`](KEY_INDEX.md#stateopinion_revised) | no |  |
| [`scene.interaction`](KEY_INDEX.md#sceneinteraction) | no |  |
| [`scene.dialogue`](KEY_INDEX.md#scenedialogue) | no |  |
| [`scene.gossip`](KEY_INDEX.md#scenegossip) | no |  |

**Owned state**

| quantity | bucket | writable | note |
|---|---|---|---|
| beliefs/opinions | `track` | yes |  |
| concerns | `track` | yes |  |
| projects | `clock` | yes |  |
| arc state | `clock` | yes |  |

**Gates**

| id | when | then | on | source |
|---|---|---|---|---|
| `g_stall8` | project stall >= 8 | state.project_failed emitted | projects | doc-12 §8 / §4.2 |
| `g_drift` | cumulative_drift > 0.5 | scene.gossip emitted | beliefs/opinions | doc-12 §8 / §6.3 |

**Feedback loops**

| with | damper |
|---|---|
| `` |  |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- CONSOLIDATED 2026-06-10: absorbs former political_dynamics module — political_dynamics_keys_migration_v30 is "Doc 12 Procedures — Key-Migration Spec (PP-687)" i.e. THIS system's Keys migration, not a separate political-dynamics system. The v1 political_dynamics record (incl. its scene.dialogue emit, unsupported by registry) is superseded by this entry. Mechanical-tier consolidation, Jordan-vetoable.
- SUPERSEDED 2026-07-07 (ED-IN-0023 / C-KEY-6): the four types this note flagged as registry-absent (scene.displacement, mechanical.project_advanced, state.project_failed, state.project_completed) were registered by ED-935 (2026-06-14, key_type_registry_v30 §9). The residual gap was that npc_behavior's own consumes[] never added the corresponding edges (plus scene.thread_operation / scene.draft_da, also registry-declared to it) despite being both self-loop consumer and emitter for four — closed by this same commit's consumes[] additions above.
- Accounting sequence (doc-12 §8, canonical): mechanical.accounting boundary -> Procedure B (Knowledge Decay -> Generation -> Resolution) -> DA Proposal Phase -> C -> D -> E; substrate §4.1 single-update rule processes emissions inline
- OI-24 residue CLOSED 2026-07-29 (W3 item 3 contract-truth sweep): the emits:[] inline comments on the same four types (scene.displacement, mechanical.project_advanced, state.project_failed, state.project_completed) still asserted 'NOT in registry' after the SUPERSEDED note above had already recorded ED-935's registration — a stale comment/gap_note contradiction, not a live gap. Verified in-tree against key_type_registry_v30.md (§4/§5 entries, emitting_systems: [npc_behavior]) that the SUPERSEDED note is the true state; the four emits:[] comments corrected to match.
- C-KEY-2 CLOSED 2026-07-29 (W3 item 3): doc: repointed from the Key-silent systems/npcs/npc_behavior_v30.md to political_dynamics_keys_migration_v30.md, the module's actual Key-sequencing spec (was cited only under sources:, per audit/2026-07-07-unaddressed-areas-audit/01_workings/cluster_C-KEY.md C-KEY-2). npc_behavior_v30.md remains reachable in sources: above — not superseded, just no longer the doc: pointer.

**Sources**

`systems/npcs/npc_behavior_v30.md (behavioral spec — kept reachable here per C-KEY-2 repoint 2026-07-29; see doc: above) [READ: 2026-07-29]`, `systems/npcs/npc_behavior_v30_index.md [READ: 2026-06-10]`, `political_dynamics_keys_migration_v30 full incl. §8 sequencing [READ: 2026-06-10]`, `key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`, `key_substrate_v30 §8.2, §8.3 [READ: 2026-06-10]`

### npc_memory

| field | value |
|---|---|
| registry system | `npc_memory` |
| scales | `personal` |
| resolver | `state_reader` |
| design doc | **— none** |
| sim module | **— none** |
| authority | none |
| build / godot | design / no-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

| key | declared producers |
|---|---|
| [`scene.gossip`](KEY_INDEX.md#scenegossip) | `npc_behavior` |
| [`scene.interaction`](KEY_INDEX.md#sceneinteraction) | `npc_behavior` |
| [`state.concern_resolved`](KEY_INDEX.md#stateconcern_resolved) | `npc_behavior` |
| [`state.opinion_revised`](KEY_INDEX.md#stateopinion_revised) | `npc_behavior` |

**OUT** — keys emitted

_none_

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- home doc unlocated — Memory schema lives in doc-12 §2.3 schema bridge; standalone spec [GAP]

**Sources**

`political_dynamics_keys_migration_v30 §2.3 [READ: 2026-06-10]`, `key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### peninsular_strain

| field | value |
|---|---|
| registry system | `peninsular_strain` |
| scales | `peninsula` |
| resolver | `deterministic_accounting` |
| design doc | `systems/overview/peninsular_strain_v30.md` |
| sim module | `systems/overview/sim/` |
| authority | code |
| build / godot | deferred / no-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

_none_

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`env.crisis`](KEY_INDEX.md#envcrisis) | no |  |
| [`env.disaster`](KEY_INDEX.md#envdisaster) | no |  |
| [`env.peninsular_strain_shock`](KEY_INDEX.md#envpeninsular_strain_shock) | no |  |
| [`env.population_change`](KEY_INDEX.md#envpopulation_change) | no |  |

**Owned state**

| quantity | bucket | writable | note |
|---|---|---|---|
| Turmoil | `clock` | yes |  |
| IP (Institutional Pressure) | `clock` | yes |  |
| MS (Mending Stability) | `clock` | yes |  |

**Gates**

| id | when | then | on | source |
|---|---|---|---|---|
| `g_ip100` | IP = 100 | Occupation Phase 1 (first pass) | IP (Institutional Pressure) | victory_v30 §5.2 |
| `g_ip85` | IP >= 85 for 3 seasons | Occupation Phase 2 (Schoenland) | IP (Institutional Pressure) | victory_v30 §5.2 |
| `g_ip80` | IP >= 80 for 3 more seasons | Occupation Phase 3 (NW pass) | IP (Institutional Pressure) | victory_v30 §5.2 |
| `g_ipfall` | IP < 85 (P1) / < 75 (P2) | invasion stalls / corridor abandoned | IP (Institutional Pressure) | victory_v30 §5.2 |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- GAP-F1 residual (2026-07-29, W3 item 3 / OI-32a): MS ownership declared above (mechanically determinable per audit/2026-07-14-gameplay-subsystem-observatory/remediation_plan_v1.md's 'MS contract owner' item). That remediation item also proposed adding a drafted substrate_state/peninsular entry emitting env.ms_delta pointing at the PP-255 decay — deliberately NOT done here: no consumer for env.ms_delta is declared anywhere in the corpus, so adding the emit would create a NEW dangling emit rather than close one (this wave's header corrections bar that). Recorded as an open residual, not fabricated as a closed item.

**Sources**

`key_substrate_v30 §8.6 [READ: 2026-06-10]`, `clock_registry_v30 Shared Clocks [READ: 2026-06-10]`, `key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`, `systems/overview/sim/ms_track.py, systems/overview/sim/accounting.py [READ: 2026-07-29]`, `engine/params/core.md §MS Baseline Decay (PP-255) [READ: 2026-07-29]`

### personal_combat

| field | value |
|---|---|
| registry system | `personal_combat` |
| scales | `personal` |
| resolver | `d_sigma` |
| design doc | `systems/combat/combat_engine_v1/` |
| sim module | `systems/combat/combat_engine_v1/` |
| authority | code |
| build / godot | unwired / gd-ported |
| status | extracted |
| accounting phase | ['emission_processing'] |

**IN** — keys consumed

| key | declared producers |
|---|---|
| [`scene.combat_strike`](KEY_INDEX.md#scenecombat_strike) | `scene_slate`, `player_input` |
| [`scene.combat_hit`](KEY_INDEX.md#scenecombat_hit) | `personal_combat` |

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`scene.combat_hit`](KEY_INDEX.md#scenecombat_hit) | no |  |
| [`scene.combat_felled`](KEY_INDEX.md#scenecombat_felled) | no |  |
| [`scene.combat_resolved`](KEY_INDEX.md#scenecombat_resolved) | no |  |

**Owned state**

| quantity | bucket | writable | note |
|---|---|---|---|
| Health | `derived_value` | **no (derived)** |  |
| cumulative_damage | `track` | yes |  |
| Wounds | `track` | yes |  |
| Stamina | `pool` | yes |  |
| Initiative | `track` | yes |  |
| Poise | `track` | yes |  |

**Derivations**

| output | inputs | formula | source |
|---|---|---|---|
| Health | `Endurance`, `Spirit`, `Strength`, `cumulative_damage` | round(round(End+4+0.4*Spirit) * (min(floor(End/2)+1,3)+1) + 0.25*Strength*Endurance) - cumulative_damage | r2_consequence_wounds.health_full = WI*(MaxWounds+1)+0.25*Str*End, minus accrued damage (ED-1041 / derived_stats_v30 §4.1) |

**Scale transitions**

| field | value |
|---|---|
| via | scale_transitions §3.4 Domain Echo (scene.combat_resolved -> faction/NPC) / §12.3 down-up targeting |

**Feedback loops**

| with | damper |
|---|---|
| `` |  |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- EXTRACTED 2026-06-23: the v2 deferral ('canonical-candidate, extraction deferred until ratification') is RESOLVED — combat_engine_v1 was ratified CANONICAL by ED-900/904 and docket ED-1029; the only thing keeping the trigger from firing was the stale README 'canonical-candidate' line (audit F6), corrected this pass.
- MODEL CORRECTION: resolver is d_sigma (sigma-leverage), NOT the v30 dice_pool model (pool=Agi×2, TN-7, damage=net_hits+STR) that the Godot skeleton placeholder, systems/combat/sim/combat.py, mechanics_index.yaml, and data_serialization_spec.md WeaponData all still carried. Canonical: pool=max(5,History+6); additive-coupled damage (Str+heft)*coupling*1.55; bilateral-Ob wounds (ED-1041, supersedes the -1D aggressor-only pool penalty).
- F3 RESOLVED: the scene_outcome family now carries personal-combat outcome Key types — scene.combat_hit / scene.combat_resolved / scene.combat_felled registered in godot/skeleton/data/key_types/ (was: registry §7 had contest/battle/investigation only).
- SLICE: combat.strike + combat.wound are PORTED + validated to the Godot shape; the remaining 9 action/substrate modules are PENDING the full port (implementation_sequence Phase G3).
- CONSUMER WIRING (A4, surfaced): scene.combat_resolved / scene.combat_felled are declared with consuming_systems [npc_behavior, faction_layer, articulation] in the registry, but those modules' contract `consumes` lists do not yet name them — the KeyBus delivers to observers/subscribers regardless; the contract declaration follows when npc_behavior/faction_state are next touched (the README's combat→faction/NPC ripple). CLOSED 2026-07-29 (W3 item 5): npc_behavior + faction_state consumes:[] now declare both types (declared intent; runtime gated on those modules being built — npc_behavior has zero .py files). articulation's consumer edge is Wave 3 item 1's territory (L-consumers lane), not this file.

**Sources**

`systems/combat/combat_engine_v1/{core,systems,wrapper,combatant,config,tradition}.py [READ: 2026-06-22/23]`, `tests/sim/v32-combat-balance/{m1_dice_sigma_core,r1_sigma_resolution,r2_consequence_wounds}.py [READ: 2026-06-23]`, `registers/editorial_ledger.jsonl ED-900/904/1029/1040/1041 [READ: 2026-06-22]`, `personal-combat audit 2026-06-22 (this session) — model-correctness + drift findings folded in`

### piety_track

_Also written as `Conviction Track` in prose._

| field | value |
|---|---|
| registry system | `conviction_track` |
| scales | `personal` |
| resolver | `deterministic_accounting` |
| design doc | `systems/characters/conviction_track_v1.md` |
| sim module | `systems/characters/sim/conviction.py` |
| authority | code |
| build / godot | deferred / python-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

| key | declared producers |
|---|---|
| [`da.antinomian_action`](KEY_INDEX.md#daantinomian_action) | `domain_actions` |
| [`da.covert_betrayal`](KEY_INDEX.md#dacovert_betrayal) | `domain_actions` |
| [`meta.knot_ruptured`](KEY_INDEX.md#metaknot_ruptured) | `fieldwork_knots` |
| [`meta.thread_woven`](KEY_INDEX.md#metathread_woven) | `threadwork` |
| [`scene.battle_concluded`](KEY_INDEX.md#scenebattle_concluded) | `mass_battle` |
| [`scene.dialogue`](KEY_INDEX.md#scenedialogue) | `scene_slate`, `social_contest` |
| [`scene.insult`](KEY_INDEX.md#sceneinsult) | `scene_slate`, `social_contest` |
| [`scene.threat`](KEY_INDEX.md#scenethreat) | `scene_slate`, `social_contest` |
| [`scene.witness`](KEY_INDEX.md#scenewitness) | `npc_behavior`, `scene_slate` |

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`state.scar_acquired`](KEY_INDEX.md#statescar_acquired) | no |  |

**Owned state**

| quantity | bucket | writable | note |
|---|---|---|---|
| conviction scars | `clock` | yes |  |

**Gates**

| id | when | then | on | source |
|---|---|---|---|---|
| `g_scar2` | Scars on Conviction X = 2 | Resonant Style X exposed; arc transition if X was top primary | conviction scars | conviction_track_v1 §2 |
| `g_scar3` | Scars on Conviction X >= 3 | Conviction crisis on X (d6 crisis table, 1 season) | conviction scars | conviction_track_v1 §2 (PP-718 per-Conviction) |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- NAME COLLISION (3-way) [OPEN — Jordan]: substrate §8.4 "Piety Track" (this personal scar system, registry system conviction_track, home systems/characters/conviction_track_v1.md) vs systems/characters/conviction_track_v30.md which is the TERRITORIAL "Piety Track & Church Victory Redesign" (PP-406-418, CV per territory) — two different systems share both names

**Sources**

`key_substrate_v30 §8.4 [READ: 2026-06-10]`, `conviction_track_v1.md header + §1-§4 index [READ: 2026-06-10]`, `key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### scenario_authoring

| field | value |
|---|---|
| registry system | `scenario_authoring` |
| scales | `peninsula` |
| resolver | `manifest` |
| design doc | **— none** |
| sim module | **— none** |
| authority | none |
| build / godot | design / no-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

_none_

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`env.crisis`](KEY_INDEX.md#envcrisis) | no |  |
| [`env.disaster`](KEY_INDEX.md#envdisaster) | no |  |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- registry-derived; authoring-time (compile-time) confirmed — fork 11 RATIFIED 2026-07-05 (ED-IN-0011): compile is authoring-time, its output packs seed runtime. Execution unbuilt (no Stage-1 compile tooling / template-pack format / settlement_layer injection wiring — C-INJ-5). Home doc still [GAP]: no dedicated scenario_authoring design doc exists (C-INJ-3). [ED-IN-0023]

**Sources**

`key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### scene_slate

| field | value |
|---|---|
| registry system | `scene_slate` |
| scales | `scene` |
| resolver | `manifest` |
| design doc | **— none** |
| sim module | `engine/autoload/scene_slate.py` |
| authority | code |
| build / godot | deferred / no-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

_none_

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`mechanical.scene_entered`](KEY_INDEX.md#mechanicalscene_entered) | no |  |
| [`scene.combat_strike`](KEY_INDEX.md#scenecombat_strike) | no |  |
| [`scene.dialogue`](KEY_INDEX.md#scenedialogue) | no |  |
| [`scene.gift`](KEY_INDEX.md#scenegift) | no |  |
| [`scene.insult`](KEY_INDEX.md#sceneinsult) | no |  |
| [`scene.investigation_resolved`](KEY_INDEX.md#sceneinvestigation_resolved) | no |  |
| [`scene.threat`](KEY_INDEX.md#scenethreat) | no |  |
| [`scene.witness`](KEY_INDEX.md#scenewitness) | no |  |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- home doc unlocated — scene slate spec referenced from settlement_layer §4.1 and substrate §8.5; standalone doc [GAP]

**Sources**

`key_substrate_v30 §8.5 [READ: 2026-06-10]`, `settlement_layer_v30 §4.1 [READ: 2026-06-10]`, `key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### scene_timer

| field | value |
|---|---|
| registry system | `scene_timer` |
| scales | `scene` |
| resolver | `state_reader` |
| design doc | **— none** |
| sim module | **— none** |
| authority | none |
| build / godot | deferred / no-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

| key | declared producers |
|---|---|
| [`mechanical.scene_entered`](KEY_INDEX.md#mechanicalscene_entered) | `game_director` |
| [`mechanical.scene_exited`](KEY_INDEX.md#mechanicalscene_exited) | `game_director` |
| [`mechanical.scene_skipped`](KEY_INDEX.md#mechanicalscene_skipped) | `game_director` |

**OUT** — keys emitted

_none_

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- registry-derived; home doc unlocated [GAP]

**Sources**

`key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### settlement_economy

| field | value |
|---|---|
| registry system | `settlement_economy` |
| scales | `settlement` |
| resolver | `deterministic_accounting` |
| design doc | **— none** |
| sim module | **— none** |
| authority | none |
| build / godot | design / retire |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

| key | declared producers |
|---|---|
| [`da.economic_intervention`](KEY_INDEX.md#daeconomic_intervention) | `domain_actions` |
| [`env.population_change`](KEY_INDEX.md#envpopulation_change) | `peninsular_strain`, `settlement_layer` |

**OUT** — keys emitted

_none_

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- registry-derived; relationship to settlement_layer §1.3 Local Economy derived value unestablished — possibly the same system [OPEN — Jordan]; home doc [GAP]
- RECOMMEND RETIRE [verification Lens-2/LD-2]: phantom module (no doc/state/logic). Fold da.economic_intervention -> settlement_layer Prosperity delta; re-point env.population_change consumer to settlement_layer. Adding a Population stat is a DESIGN decision (deferred — open_decisions §2). Self-edge hazard: settlement_layer both emits and would consume env.population_change — route peninsular_strain -> settlement_layer.
- ED-SE-0005 (2026-07-08): the SETTLEMENT-ACTION side of this retirement is CONFIRMED by the ratified pessimist-action audit (ED-IN-0027). The player_agency_v30 §9 Trade action -- this phantom module's likely intended settlement-economy player verb -- is PRUNED and folded into the existing income sources; no dedicated settlement-economy player action survives. The da.economic_intervention -> settlement_layer Prosperity fold and the deferred Population-stat design decision (above) remain the open structural half.

**Sources**

`key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### settlement_layer

| field | value |
|---|---|
| registry system | `settlement_layer` |
| scales | `settlement`, `territory` |
| resolver | `deterministic_accounting` |
| design doc | `systems/settlements/settlement_layer_v30.md` |
| sim module | `systems/settlements/sim/settlement.py` |
| authority | code |
| build / godot | design / python-oracle |
| status | extracted |
| accounting phase | ['settlement_accounting'] |

**IN** — keys consumed

| key | declared producers |
|---|---|
| [`env.disaster`](KEY_INDEX.md#envdisaster) | `peninsular_strain`, `scenario_authoring` |
| [`env.peninsular_strain_shock`](KEY_INDEX.md#envpeninsular_strain_shock) | `peninsular_strain` |

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`env.population_change`](KEY_INDEX.md#envpopulation_change) | no |  |

**Owned state**

| quantity | bucket | writable | note |
|---|---|---|---|
| Prosperity / Defense / Order | `track` | yes |  |
| Local Economy / Garrison Strength / Public Order | `derived_value` | **no (derived)** |  |
| Legitimacy (L) / Popular Support (PS) | `track` | yes |  |
| province Accord | `derived_value` | **no (derived)** |  |

**Gates**

| id | when | then | on | source |
|---|---|---|---|---|
| `g_ord0` | Order = 0 | local revolt | Prosperity / Defense / Order | settlement_layer_v30 §1.3 |
| `g_def0` | settlement Defense = 0 | undefended — auto-capture | Prosperity / Defense / Order | settlement_layer_v30 §1.3 |
| `g_dv0` | derived value = 0 held through Accounting | owning stat -1 (same rule as faction stats) | Local Economy / Garrison Strength / Public Order | settlement_layer_v30 §1.3 |

**Derivations**

| output | inputs | formula | source |
|---|---|---|---|
| province Accord | `Order` | floor(mean Order across settlements) | settlement_layer_v30 §1.3 |
| Local Economy | `Prosperity` | Prosperity × 50 | settlement_layer_v30 §1.3 |
| Garrison Strength | `Defense`, `Fort Level` | Defense × 20 + Fort × 30 | settlement_layer_v30 §1.3 |
| Public Order | `Order` | Order × 20 (riot events below 0) | settlement_layer_v30 §1.3 |
| faction Mandate (cross-module → faction_state) | `Legitimacy`, `Popular Support`, `W_s` | q_s = 0.5L+0.5PS; W_s = base(Type)+Prosperity+FacilityTier; T = Σ W_s·(q_s/7); Mandate = clamp(round(7T/(T+6)),0,7) — saturating (Lesson-5 bound) | settlement_layer_v30 §1.8 LPS-2e |
| Legitimacy / Popular Support | `faction Mandate` | drift ±1/settlement/season toward Mandate (damped, mean-reverting; Stage-4 sim bounded 30 seasons) | settlement_layer_v30 §1.8 |
| faction Treasury income (cross-module → faction_state) | `Prosperity` | Σ Prosperity across settlements × 10 | derived_stats §8.1 (quoted in settlement_layer §1.8) |

**Feedback loops**

| with | damper |
|---|---|
| `faction_state` | Mandate↔L/PS: saturating Mandate = 7T/(T+6) (∂Mandate/∂q shrinks as T grows) + mean-reverting feedback drift ±1; Stage-4 sim bounded 0-7 over 30 seasons under mission shocks (settlement_layer_v30 §1.8, Lesson-5 bound) |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- settlement_layer_v30_index.md is STALE — predates LPS-2e §1.8 (no §1.8 row); index pipeline regeneration needed [tooling defect]
- Key types registered (W3, ED-IN-0096): state.settlement_revolt, mechanical.settlement_captured — emits: declaration lands with the module's build so the census never carries a declared-emit-no-consumer row; see key_type_registry entries for held consumer dispositions.

**Sources**

`settlement_layer_v30 §1.3/§1.8/§4.1 full [READ: 2026-06-10]`, `key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### social_contest

| field | value |
|---|---|
| registry system | `social_contest` |
| scales | `scene` |
| resolver | `dice_pool` |
| design doc | `systems/social_contest/social_contest_v30.md` |
| sim module | `systems/social_contest/sim/contest/` |
| authority | code |
| build / godot | gated / python-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

| key | declared producers |
|---|---|
| [`state.opinion_revised`](KEY_INDEX.md#stateopinion_revised) | `npc_behavior` |

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`scene.contest_resolved`](KEY_INDEX.md#scenecontest_resolved) | no |  |
| [`scene.dialogue`](KEY_INDEX.md#scenedialogue) | no |  |
| [`scene.insult`](KEY_INDEX.md#sceneinsult) | no |  |
| [`scene.threat`](KEY_INDEX.md#scenethreat) | no |  |

**Owned state**

| quantity | bucket | writable | note |
|---|---|---|---|
| persuasion_track | `clock` | yes |  |

**Scale transitions**

| field | value |
|---|---|
| via | scale_transitions §3.4 Scene → Faction (Domain Echo) |

**Feedback loops**

| with | damper |
|---|---|
| `npc_behavior` | 2-cycle: emits scene.contest_resolved/scene.dialogue, consumes state.opinion_revised. BOUNDED [verification LD-1]: Procedure-D batch cadence (1/Accounting) + \|delta-affect\|>=0.5 emission threshold + Chain-Contest cap 3 then 4-season cold equilibrium. NOTE: the affect_axis clamp is NOT in canon; convergence rests on these bounds + the saturating §5.4 drift curve. |

**Sources**

`key_substrate_v30 §8.5 (PP-683) [READ: 2026-06-10]`, `scale_transitions_v30 §3.4 [READ: 2026-06-10]`, `key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### territorial_piety

| field | value |
|---|---|
| registry system |  |
| scales | `territory`, `provincial` |
| resolver | `deterministic_accounting` |
| design doc | `systems/characters/conviction_track_v30.md` |
| sim module | `systems/overview/sim/ci_track.py` |
| authority | code |
| build / godot | deferred / python-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

_none_

**OUT** — keys emitted

_none_

**Owned state**

| quantity | bucket | writable | note |
|---|---|---|---|
| CV (per-territory Piety) | `track` | yes |  |
| CI (Church Influence) | `clock` | yes |  |

**Gates**

| id | when | then | on | source |
|---|---|---|---|---|
| `g_ci100` | CI = 100 | Theocracy Unification attempt | CI (Church Influence) | ci_political_v30 §2.2 |
| `g_cicap` | seasonal CI cap | CI gain bounded per season | CI (Church Influence) | ci_political_v30 §2.4 |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- CANONICAL BG-era doc with ZERO Key integration — no emitting/consuming_systems entry in the registry names it; CV drift consumes thread-op effects (§1.3b ED-676) and Calamity drift (§1.3) with no Key types [registry §10 candidate / Keys-migration pending]
- name collision with personal piety_track — see piety_track gap_note [OPEN — Jordan]
- Key types registered (W3, ED-IN-0096): mechanical.theocracy_unification_declared — emits: declaration lands with the module's build so the census never carries a declared-emit-no-consumer row; see key_type_registry entries for held consumer dispositions.

**Sources**

`conviction_track_v30 index §1-§11 [READ: 2026-06-10]`, `clock_registry_v30 Shared Clocks table [READ: 2026-06-10]`

### threadwork

| field | value |
|---|---|
| registry system | `threadwork` |
| scales | `personal`, `thread` |
| resolver | `dice_pool` |
| design doc | `systems/threadwork/threadwork_v30.md` |
| sim module | `systems/threadwork/sim/operations.py` |
| authority | code |
| build / godot | unwired / python-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

_none_

**OUT** — keys emitted

| key | terminal | note |
|---|---|---|
| [`scene.thread_operation`](KEY_INDEX.md#scenethread_operation) | no |  |
| [`meta.thread_woven`](KEY_INDEX.md#metathread_woven) | no |  |

**Owned state**

| quantity | bucket | writable | note |
|---|---|---|---|
| Coherence | `track` | yes |  |
| Thread Fatigue | `clock` | yes |  |

**Scale transitions**

| field | value |
|---|---|
| via | scale_transitions §3.1 Personal → Thread |
| via | scale_transitions §3.5 Thread → Faction |
| via | scale_transitions §3.6 Thread → Mass |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- threadwork_v30 header: "design proposal, requires editorial approval" yet carries CANONICAL POOL NOTICE — doc status ambiguity [OPEN — Jordan]

**Sources**

`key_substrate_v30 §8.4 [READ: 2026-06-10]`, `threadwork_v30 index Parts One-Two [READ: 2026-06-10]`, `scale_transitions_v30 §3.1/§3.5/§3.6 [READ: 2026-06-10]`, `key_type_registry_v30 emitting/consuming_systems matrix [READ: 2026-06-10]`

### victory

| field | value |
|---|---|
| registry system |  |
| scales | `provincial`, `peninsula` |
| resolver | `state_reader` |
| design doc | `systems/victory/victory_v30.md` |
| sim module | `engine/autoload/victory.py` |
| authority | code |
| build / godot | live / python-oracle |
| status | extracted |
| accounting phase |  |

**IN** — keys consumed

_none_

**OUT** — keys emitted

_none_

**Owned state**

| quantity | bucket | writable | note |
|---|---|---|---|
| MS / IP / CI / Turmoil / Accord / Mandate / PV / PT reads | `clock` | **no (derived)** |  |

**Gates**

| id | when | then | on | source |
|---|---|---|---|---|
| `g_ms0` | MS = 0 | Post-Calamity Era |  | victory_v30 §5.1 |
| `g_ms5` | MS <= 5 sustained 10 seasons | Second Calamity (true terminal) |  | victory_v30 §5.1 |
| `g_msrec` | MS restored to 20 within 10 seasons | Post-Calamity recovery |  | victory_v30 §5.1 |
| `g_diss` | all factions dissolved | Anarchy Era (Ministry continues) |  | victory_v30 §5.3 |

**Gap notes** (the authors' own recorded uncertainty — read before assuming a blank field is an oversight)

- world-state era transitions (§5: MS=0 Post-Calamity, IP=100 Phased Occupation, all-dissolved Anarchy) are UNKEYED — no mechanical_event/state_transition type exists; articulation is blind to era changes via the Key stream [registry §10 candidate]
- doc status: "DESIGN — pending Varfell Path B user decision (ED-311)" — not CANONICAL
- victory_v30_index.md STALE: §5.1 indexed as "RS=0" but doc reads "MS=0" [index pipeline defect, same class as settlement]
- g_ms0/g_ms5/g_msrec 'MS (unowned clock)' annotations CORRECTED 2026-07-29 (OI-32a, W3 item 3): MS is now declared owned by peninsular_strain's state: block (GAP-F1 ownership declaration) — these three gates' reads: now point at the new owner instead of asserting no module owns it.
- Key types registered (W3, ED-IN-0096): mechanical.era_transition, mechanical.second_calamity — emits: declaration lands with the module's build so the census never carries a declared-emit-no-consumer row; see key_type_registry entries for held consumer dispositions.

**Sources**

`victory_v30 §5 full + header [READ: 2026-06-10]`
