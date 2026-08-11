# World-Schema Gap Register — part 1 of 4 (G-01–G-14)

## Status: REFERENCE — observations against the tree. **Ratifies nothing.**

**Date:** 2026-08-11 · **Lane:** IN · **ED:** ED-IN-0153 · **Base:** `63d4d0c`

Method: [`00_orchestration_plan.md`](00_orchestration_plan.md) · Verdict, held decisions and what this run did NOT cover: [`02_verdict_and_residuals.md`](02_verdict_and_residuals.md)


> **Read `02_verdict_and_residuals.md` before acting on any row.** Three producer claims were
> **overturned** and are absent here; two proposals **would have caused damage if executed** and
> are flagged there rather than silently dropped. Every row survived a read-only `valoria-critic`
> pass that never saw the producer's reasoning.

**Run:** 17 agents · 0 errors · 0 empty returns · `stop_reason: completed` · not degraded · 61 disputes recorded, 0 left unadjudicated.
**Input:** 75 raw findings from 12 producer lanes across three method-disjoint passes → 50 register rows after critic verdicts and merge.

| disposition | n | | gap kind | n |
|---|---|---|---|---|
| `propose_contract` | 20 | | `missing_owned_state` | 16 |
| `needs_jordan_ruling` | 13 | | `missing_key_type` | 6 |
| `propose_key` | 8 | | `missing_edge` | 6 |
| `already_tracked` | 4 | | `missing_individuation_descriptor` | 5 |
| `propose_authoring_field` | 3 | | `missing_payload_field` | 4 |
| `propose_descriptor` | 1 | | `missing_authoring_schema` | 4 |
| `not_a_gap` | 1 | | `vocabulary_conflict` | 4 |
|  |  | | `missing_contract_module` | 3 |
|  |  | | `missing_scale_or_transition` | 2 |

### Index — all 50 rows

The `×` column is **independent lanes that reached the row**. See `02_verdict_and_residuals.md` §3
for why those counts are a synthesis reconstruction rather than a recorded measurement.

| id | × | rung | kind | disposition | part |
|---|---|---|---|---|---|
| [G-01](01_gap_register.md#g-01) | 4 | national_faction | `missing_key_type` | `propose_key` | 1 |
| [G-02](01_gap_register.md#g-02) | 3 | national_faction | `missing_owned_state` | `propose_contract` | 1 |
| [G-03](01_gap_register.md#g-03) | 3 | territory | `missing_contract_module` | `propose_contract` | 1 |
| [G-04](01_gap_register.md#g-04) | 3 | settlement | `missing_key_type` | `propose_key` | 1 |
| [G-05](01_gap_register.md#g-05) | 3 | character | `missing_owned_state` | `needs_jordan_ruling` | 1 |
| [G-06](01_gap_register.md#g-06) | 2 | cross_rung | `missing_owned_state` | `already_tracked` | 1 |
| [G-07](01_gap_register.md#g-07) | 2 | provincial_faction | `missing_owned_state` | `propose_contract` | 1 |
| [G-08](01_gap_register.md#g-08) | 2 | national_faction | `missing_payload_field` | `propose_key` | 1 |
| [G-09](01_gap_register.md#g-09) | 2 | character | `missing_owned_state` | `already_tracked` | 1 |
| [G-10](01_gap_register.md#g-10) | 2 | province | `missing_owned_state` | `propose_contract` | 1 |
| [G-11](01_gap_register.md#g-11) | 2 | province | `missing_owned_state` | `needs_jordan_ruling` | 1 |
| [G-12](01_gap_register.md#g-12) | 2 | territory | `missing_contract_module` | `propose_contract` | 1 |
| [G-13](01_gap_register.md#g-13) | 2 | character | `missing_owned_state` | `propose_contract` | 1 |
| [G-14](01_gap_register.md#g-14) | 2 | national_faction | `missing_owned_state` | `propose_contract` | 1 |
| [G-15](01_gap_register_part2.md#g-15) | 1 | territory | `missing_individuation_descriptor` | `propose_authoring_field` | 2 |
| [G-16](01_gap_register_part2.md#g-16) | 1 | national_faction | `missing_individuation_descriptor` | `propose_contract` | 2 |
| [G-17](01_gap_register_part2.md#g-17) | 1 | cross_rung | `missing_authoring_schema` | `needs_jordan_ruling` | 2 |
| [G-18](01_gap_register_part2.md#g-18) | 1 | cross_rung | `vocabulary_conflict` | `propose_contract` | 2 |
| [G-19](01_gap_register_part2.md#g-19) | 1 | character | `vocabulary_conflict` | `needs_jordan_ruling` | 2 |
| [G-20](01_gap_register_part2.md#g-20) | 1 | character | `missing_authoring_schema` | `propose_contract` | 2 |
| [G-21](01_gap_register_part2.md#g-21) | 1 | territory | `missing_scale_or_transition` | `needs_jordan_ruling` | 2 |
| [G-22](01_gap_register_part2.md#g-22) | 1 | cross_rung | `missing_payload_field` | `needs_jordan_ruling` | 2 |
| [G-23](01_gap_register_part2.md#g-23) | 1 | character | `missing_owned_state` | `propose_contract` | 2 |
| [G-24](01_gap_register_part2.md#g-24) | 1 | cross_rung | `missing_authoring_schema` | `needs_jordan_ruling` | 2 |
| [G-25](01_gap_register_part2.md#g-25) | 1 | territory | `missing_owned_state` | `propose_contract` | 2 |
| [G-26](01_gap_register_part2.md#g-26) | 1 | territory | `missing_key_type` | `propose_key` | 2 |
| [G-27](01_gap_register_part2.md#g-27) | 1 | territory | `missing_edge` | `propose_key` | 2 |
| [G-28](01_gap_register_part2.md#g-28) | 1 | character | `missing_key_type` | `propose_key` | 2 |
| [G-29](01_gap_register_part2.md#g-29) | 1 | character | `missing_key_type` | `propose_key` | 2 |
| [G-30](01_gap_register_part3.md#g-30) | 1 | settlement | `missing_owned_state` | `propose_contract` | 3 |
| [G-31](01_gap_register_part3.md#g-31) | 1 | settlement_faction | `missing_payload_field` | `already_tracked` | 3 |
| [G-32](01_gap_register_part3.md#g-32) | 1 | settlement | `missing_edge` | `needs_jordan_ruling` | 3 |
| [G-33](01_gap_register_part3.md#g-33) | 2 | cross_rung | `missing_key_type` | `needs_jordan_ruling` | 3 |
| [G-34](01_gap_register_part3.md#g-34) | 1 | provincial_faction | `missing_owned_state` | `propose_contract` | 3 |
| [G-35](01_gap_register_part3.md#g-35) | 1 | national_faction | `vocabulary_conflict` | `needs_jordan_ruling` | 3 |
| [G-36](01_gap_register_part3.md#g-36) | 2 | settlement_faction | `missing_owned_state` | `propose_contract` | 3 |
| [G-37](01_gap_register_part3.md#g-37) | 1 | settlement | `missing_individuation_descriptor` | `propose_authoring_field` | 3 |
| [G-38](01_gap_register_part3.md#g-38) | 1 | cross_rung | `missing_authoring_schema` | `needs_jordan_ruling` | 3 |
| [G-39](01_gap_register_part3.md#g-39) | 1 | character | `missing_owned_state` | `propose_contract` | 3 |
| [G-40](01_gap_register_part3.md#g-40) | 1 | character | `missing_payload_field` | `propose_key` | 3 |
| [G-41](01_gap_register_part3.md#g-41) | 1 | character | `missing_owned_state` | `propose_contract` | 3 |
| [G-42](01_gap_register_part3.md#g-42) | 2 | cross_rung | `missing_edge` | `needs_jordan_ruling` | 3 |
| [G-43](01_gap_register_part3.md#g-43) | 2 | cross_rung | `vocabulary_conflict` | `already_tracked` | 3 |
| [G-44](01_gap_register_part3.md#g-44) | 1 | cross_rung | `missing_edge` | `propose_contract` | 3 |
| [G-45](01_gap_register_part3.md#g-45) | 1 | territory | `missing_contract_module` | `propose_contract` | 3 |
| [G-46](01_gap_register_part4.md#g-46) | 1 | cross_rung | `missing_scale_or_transition` | `propose_contract` | 4 |
| [G-47](01_gap_register_part4.md#g-47) | 1 | cross_rung | `missing_edge` | `needs_jordan_ruling` | 4 |
| [G-48](01_gap_register_part4.md#g-48) | 1 | territory | `missing_individuation_descriptor` | `propose_authoring_field` | 4 |
| [G-49](01_gap_register_part4.md#g-49) | 2 | national_faction | `missing_individuation_descriptor` | `propose_descriptor` | 4 |
| [G-50](01_gap_register_part4.md#g-50) | 1 | cross_rung | `missing_edge` | `not_a_gap` | 4 |

---

## Rows

<a id="g-01"></a>

### G-01 · No key type at any family announces a faction coming into or going out of existence, at any tier canon describes: Stage-

**rung** `national_faction` · **kind** `missing_key_type` · **disposition** `propose_key` · **independent lanes** 4

**Lenses.** `entity lifecycle`, `churn`, `politics`, `individuation`

**Claim.** No key type at any family announces a faction coming into or going out of existence, at any tier canon describes: Stage-4 Faction Declaration (settlement_layer §6.2, with a ratified ED-790 starting stat sheet), Collapse-to-city-state and full Dissolution (§6.3), Succession Split (faction_succession_split_v30 §2.4, which must mint a NEW faction identity), Löwenritter Autonomy Stage 4 (conflict_architecture_proposal, CANONICAL), and insurgency promotion. The one production path that claims to implement emergence, check_insurgency_promotion(), sets two fields on an InsurgencyRecord and returns; it never constructs a Faction, never touches world.factions, and emits nothing. 'Which factions exist' is a 4-entry Python literal, not schema.

**Proposal.** propose_key — type_id state.faction_lifecycle_event, family state_transition (§5, alongside state.succession which already models a within-faction leadership change); required_payload_fields: faction_id, event_type (declared | collapsed_to_city_state | dissolved | split | promoted_from_subnational), origin_entity_type, origin_entity_id; optional: parent_faction_id, new_faction_id, founding_stats (the ED-790 table supplies this shape verbatim); default_scale_signature: [settlement, territory, peninsula]. NOTE the producers' proposals used 'provincial' — engine/substrate/keys.py:65 SCALES has no such member and invariant 7 would raise on it; stripped. Explicitly generic: Crown/Church/Varfell/Hafenmark/Löwenritter are NOT special-cased, and Löwenritter's Split composes on the same primitive as insurgency promotion rather than hanging state off Crown. Paired propose_contract: a roster-membership state row on faction_state, {name: "faction roster membership", bucket: track, writable: true}. BLOCKED on G-17.

**Evidence.** systems/settlements/settlement_layer_v30.md:1027-1063 (§6.2 + ED-790 stats table), :1065-1096 (§6.3 contraction/dissolution); systems/factions/faction_succession_split_v30.md §2.4 (~:70-90, 60/40 splinter; :132 a new faction identity 'Eastern Varfell'); systems/_architecture/conflict_architecture_proposal.md:2 (CANONICAL), :68-79 (Split → separate faction M3/I2/W3/Mil6/Stab5); systems/world/sim/insurgency_pipeline.py:199-253 (success path is rec.promoted=True; rec.parliamentary_status=... at :247-248, then return — no Faction construction, no emit); engine/autoload/game_state.py:51-56 + 215-220 (STARTING_STATS is the sole Faction construction site, 4 entries); exhaustive grep of all 55 '### ' type headers in key_type_registry_v30.md — no faction_founded/declared/emerged/collapsed/dissolved/split type. Nearest neighbours are wrong-entity or wrong-grain: state.succession (:670-689) and mechanical.era_transition, whose trigger_stat comment at :503 reads '# MS | IP | faction_dissolution' — dissolution carried only as an aggregate world-era trigger, never per-faction. module_contracts.yaml:848-852 gate g_diss POLLS 'faction Mandate (faction_state, all factions)' in place of consuming an announcement.

**Existing tracking.** ED-FA-0001 / ED-IN-0047 RULE that 4 starting factions plus emergent ones is intentional and assert the pathway needs 'no new resolver', but neither addresses that the cited mechanism stops at a boolean with no key or roster schema. ED-790 ratifies starting-stat VALUES only. ED-767/ED-810 track the Löwenritter DESIGN, not the schema. SHARPENED by an uncited surface: systems/world/world_flow_skeleton_v1.md:183,:185 records that module_contracts.yaml registers only miraculous_event among this subsystem's four sim modules — insurgency_pipeline, the would-be emitter, has no contract row at all, and :185 calls the coverage 'inverted from the execution'. So the missing key sits on an undeclared module.

---

<a id="g-02"></a>

### G-02 · faction_state's owned-state block is exactly three rows (Mandate, Treasury, 'faction stats 1-7') against its own canon d

**rung** `national_faction` · **kind** `missing_owned_state` · **disposition** `propose_contract` · **independent lanes** 3

**Lenses.** `beliefs and convictions`, `goals and ambitions`, `values and ethics`, `society`, `individuation`

**Claim.** faction_state's owned-state block is exactly three rows (Mandate, Treasury, 'faction stats 1-7') against its own canon doc's authored + derived Faction State Schema of roughly nine to twelve fields: role, mission (incl. prior_mission, which mechanical.mission_shift's payload presupposes), leader, organizational_hierarchy (nodes/edges/cascade_roots), institutional_culture, aggregate_effective_convictions, cascade_fidelity, expected_convictions, strictness, Public Expectation — plus treaties and active sanctions, which the contract's own SCOPE note already claims are in scope. Three of the faction's four canonical components are absent from the block that is supposed to own them.

**Proposal.** propose_contract — one row-set change to references/module_contracts.yaml:107-110 (NOT five separate findings, and NOT a new module: the file's own A6 scope ruling at :119 already assigns faction_layer_v30's treaties/parliament and faction_behavior_v30's mission/cascade/expectation/Mandate to faction_state, so registering a separate 'treaty' or 'cascade' module contradicts a recorded decision). Add: {name: "Mission", bucket: track, writable: true}; {name: "role", bucket: track, writable: false}; {name: "institutional_culture", bucket: track, writable: false}; {name: "organizational_hierarchy", bucket: track, writable: true}; {name: "aggregate_effective_convictions", bucket: derived_value, writable: false}; {name: "cascade_fidelity", bucket: derived_value, writable: false}; {name: "expected_convictions", bucket: derived_value, writable: false}; {name: "Public Expectation", bucket: derived_value, writable: false}. TWO PRODUCER PROPOSAL DEFECTS CORRECTED: (a) three lanes proposed 'bucket: track, writable: true' for quantities the source doc files under '# Derived (recomputed each Accounting)' — that is exactly the read/write asymmetry CLAUDE.md §0.1 point 1 names, and it contradicts the F1-guard convention already applied to Mandate/Treasury at :108-109; (b) 'ledger bucket' is not a bucket — the enum across all 40 state rows is exactly {clock:14, derived_value:7, pool:2, track:17}, and 'Ledger' already names the settlement-scoped Ledger-of-Consequence (systems/settlements/sim/ledger.py). The organizational_hierarchy row must compose on G-23's canonical edge record, not invent a second relational shape.

**Evidence.** systems/factions/faction_behavior_v30.md:18-24 (four components), :39-59 (§2 '# Authored' block: role/mission/leader/organizational_hierarchy/institutional_culture), :63-69 ('# Derived (recomputed each Accounting)': aggregate_effective_convictions/cascade_fidelity/expected_convictions/strictness), :77-99 (§3.1 mission_alignment_modifier), :107-128 (NPC.supervisor_id, orphan handling, cascade_roots), :189-236 (§3.3 Public Expectation), :320 (§3.6 Strictness); references/module_contracts.yaml:107-110 verified verbatim as the complete three-row block; bucket census run over the whole file returns only the four values above; grep of module_contracts.yaml for supervisor|cascade_fidelity|organizational_hierarchy|expected_convictions|strictness returns ZERO.

**Existing tracking.** Partially named, never allocated: module_contracts.yaml:119 and references/CONTRACT_INDEX.md:97 record the A6 SCOPE ruling 'faction_state = {faction_layer_v30 (stability/occupation/treaties/parliament) + faction_behavior_v30 (mission/cascade/expectation/Mandate)}' — i.e. the file knows these belong here and the rows were never written. ED-FA-0035 covers the adjacent computability half (cascade_alignment_modifier has no formula), not state ownership. MATERIAL CAVEAT: the resolver half does not exist either — module_contracts.yaml:66-70 and systems/factions/factions_flow_skeleton_v1.md:175 both record that cascade_resolution/mission_shift accounting logic has zero implementation anywhere in the tree, so these are undeclared fields feeding an unbuilt resolver, not live reads. One producer's word 'live' is withdrawn.

---

<a id="g-03"></a>

### G-03 · Territory temperament — the 5-typology α/β ethical axis that canon authors per territory, drifts under env

**rung** `territory` · **kind** `missing_contract_module` · **disposition** `propose_contract` · **independent lanes** 3

**Lenses.** `values and ethics`, `society`, `individuation`

**Claim.** Territory temperament — the 5-typology α/β ethical axis that canon authors per territory, drifts under env.peninsular_strain_shock, and aggregates population-weighted into faction effective temperament feeding the political-support formula — has no owning module_contracts.yaml row, no key type announcing a drift, and its only implementation is a verified zero-importer orphan. A mechanism that computes correctly in isolation is structurally unable to inform any other system.

**Proposal.** propose_contract — do NOT bespoke-wire it. Add a territory_temperaments row (scales: [territory], doc: systems/settlements/territory_temperaments_v30.md, sim_module: systems/settlements/sim/temperaments.py) with a TWO-ROW state block, which is the correct decomposition and the one two of three lanes got wrong: {name: "temperament", bucket: track, writable: false} (authored per-territory) and {name: "temperament_drift", bucket: track, writable: true} (the only mutated half); consumes: [{type: env.peninsular_strain_shock, from: [peninsular_strain]}]; and add territory_temperaments to that key's consuming_systems at key_type_registry_v30.md:780. A drift-band-crossing key type should wait on the general Field/Gauge primitive (G-24), not be minted per-quantity.

**Evidence.** systems/settlements/territory_temperaments_v30.md:6 (Status: CANONICAL), :11-19 (5-typology), :32+ (17-territory instantiation), §4 (:64-65 drift pseudocode keyed on env.peninsular_strain_shock); systems/factions/faction_behavior_v30.md:235-236,:250,:254-283 (§3.4.1 typology + §3.4.2 pseudocode + population-weighted faction aggregate); systems/settlements/sim/temperaments.py:12-15 (its own ASSUMPTION comment: 'drift state would belong on World per schema migration pattern... deferred until first consumer lands'), :86-95 (module-level _drift_state dict); key_type_registry_v30.md:765-782 (env.peninsular_strain_shock consuming_systems: [faction_layer, npc_behavior, articulation, settlement_layer] — no temperament owner, and no such module exists to be listed); grep of module_contracts.yaml for 'temperament': ZERO rows; references/descriptor_registry.yaml:164 (temp.* KIND exists, scope 'territory/faction (pop-weighted avg)' — vocabulary without ownership); registers/mechanics_index.yaml:779-785 (indexed as a live mechanic).

**Existing tracking.** TRACKED — two of three lanes wrongly reported 'none found'. systems/_architecture/governance_type_registry_v1.md:138 (§2.6 temperament VECTOR row, 'directly actionable now that Territory is a real tier') and :248-271 (§4.1/§4.2 general VECTOR-vs-Key gap + Field/Gauge schema sketch, PROPOSED, no ED); registers/handoffs/HANDOFF_IN.md:540 (ED-IN-0149 T0-3 'temperaments.py read/write-asymmetry guard'); systems/settlements/settlements_flow_skeleton_v1.md:29-32,:140 pins all four temperaments.py entry points as no-importer; tests/valoria/test_oi12_orphan_census.py:51 allowlists it as a confirmed orphan.

---

<a id="g-04"></a>

### G-04 · Settlement

**rung** `settlement` · **kind** `missing_key_type` · **disposition** `propose_key` · **independent lanes** 3

**Lenses.** `governance`, `politics`, `churn`

**Claim.** Settlement.governor_id — a canon-load-bearing identity (§3.2 assignment, §3.3 subnational-governor replacement, and the Bishop-Governor case whose appointment is stated to trigger province fractionalization) — has no row in settlement_layer's contract state block, and no key type expresses a governor change. state.settlement_revolt carries only a bare governor_expelled bool with no incoming-governor identity; mechanical.settlement_captured omits governor entirely. The sole writer, succeed_governor(), has zero production callers.

**Proposal.** propose_key — type_id state.governor_changed, family state_transition (§5, composing on state.succession/state.coup_attempted, which already model 'who holds an office changed'); required_payload_fields: settlement_id, territory_id, prior_governor_id, new_governor_id, mode (assigned | expelled | bishop_appointed | rotated); default_scale_signature: [settlement, territory] (territory included so the Bishop-Governor fractionalization check has a scale to fire at); emitting_systems: [settlement_layer]; consuming_systems: [] filed DECLARE-ONLY per the ED-IN-0096 precedent at key_type_registry_v30.md:751-756 rather than naming consumers with no live subscription. Paired propose_contract: add governor_id to settlement_layer's state block via the contract's own disclosed cross-file-pull methodology (module_contracts.yaml:693-699, already used for Legitimacy/Popular Support). BLOCKED on G-17. ADJUDICATION between two lanes: 'zero production callers' is correct; the sibling claim's 'actively-mutated / production-adjacent' is withdrawn — the only callers are tools/sim_harness/adapters/pr119_governance/*, a prototype not imported by engine/, systems/*/sim/, or any CI test.

**Evidence.** systems/settlements/sim/registry.py:61 (governor_id field), :198-207 (succeed_governor, sole writer, mutating at :205), :236 (its own docstring names governor_id as awaiting 'a later system'); key_type_registry_v30.md:726-757 (state.settlement_revolt — governor_expelled bool at :733, no new-governor field) and :464-471 (mechanical.settlement_captured — capturing/prior_controlling_faction_id only); systems/settlements/settlement_layer_v30.md:561 (Bishop-Governor: 'Settlement governance transfers to Church on appointment. Province fractionalizes if...'); references/module_contracts.yaml:707-711 (no governor row).

**Existing tracking.** ALREADY FILED on a surface no lane opened: systems/settlements/settlements_flow_skeleton_v1.md:22,:116,:144 — :144 states 'succeed_governor, the one production entry point that would trigger ledger_sweep, itself has no production caller', and :116 marks governor_id W '(no production caller)'. ED-SE-0013/0029/0030/0031/0033 stage future governance mechanics (residencia, podestà, rotation, corregidor) that would need exactly this element but none names the schema gap. The sim_module pointer defect at :150 is separate and does not resolve this.

---

<a id="g-05"></a>

### G-05 · Renown (0-10, persistent, cross-faction, explicitly independent of Standing and surviving faction collapse) is written b

**rung** `character` · **kind** `missing_owned_state` · **disposition** `needs_jordan_ruling` · **independent lanes** 3

**Lenses.** `social_status`, `politics`, `individuation`

**Claim.** Renown (0-10, persistent, cross-faction, explicitly independent of Standing and surviving faction collapse) is written by 8 named canon triggers and read by Domain Action pool sizing, NPC Disposition floors, governance-scope gating, Legacy inheritance, and the entire Stature Ladder that gates faction emergence — yet it has no key type, no owned-state row on any module, and its home doc player_agency_v30 has no module row among the 27 at all. Its only registration anywhere is as a bare NAME inside descriptor_registry.yaml's not_descriptors.tracks block.

**Proposal.** needs_jordan_ruling — the gap is certain, the owner is not, and the two lanes that proposed fixes contradicted each other (a new character/player_agency contract module vs folding into npc_behavior). Folding a cross-faction CHARACTER track into npc_behavior, whose rows are beliefs/opinions, concerns, projects, arc state, is scale-local shape divergence and is rejected. A third lane's 'promote Renown out of not_descriptors' is also rejected as scripting drift: descriptor_registry.yaml:174-187 files SEVEN tracks identically (Piety, Disposition, Renown, Standing, Persuasion, Coherence, Warden Recognition) under a block-level ruling; promoting one member special-cases it. Two calls are needed — (1) does player_agency get a contract module row, and (2) is not_descriptors.tracks swept as a block — before any row is written.

**Evidence.** systems/_architecture/player_agency_v30.md:404-436 (§5.4: 8-row Renown Sources table, thresholds 3/5/7/9 at :431-434, +2/season cap at :421, Standing/Renown independence at :436), :566 (Legacy inheritance floor(predecessor÷2)); systems/settlements/settlement_layer_v30.md:1015-1025 (Stature Ladder — Renown is one of TWO columns with Standing, not the sole determinant as one lane claimed), :1046 (Stage 3→4 gate is four conditions: 4+ settlements, 2+ provinces, Renown 7+, 1 province Seat); case-insensitive grep for renown across key_type_registry_v30.md, module_contracts.yaml AND the generated engine/engine_params/key_types.json: zero in all three; no player_agency module row among the 27; references/descriptor_registry.yaml:187 (name-only registration inside not_descriptors).

**Existing tracking.** none for the schema absence. Ledger hits across all lane + archive files are numeric-value rulings only (ED-790 starting-stat formula, ED-793 which Conviction outcomes grant it) or the OPT-AV-13/18 Renown-cap fork left open in ED-IN-0029.

---

<a id="g-06"></a>

### G-06 · Casus Belli — a formal standing right to act against a named faction, granted by treaty breach / Outlawry / Excommunicat

**rung** `cross_rung` · **kind** `missing_owned_state` · **disposition** `already_tracked` · **independent lanes** 2

**Lenses.** `geopolitics`, `diplomacy`, `relation`

**Claim.** Casus Belli — a formal standing right to act against a named faction, granted by treaty breach / Outlawry / Excommunication / Diplomatic Token, consumed on use, expiring after one season, stacking-capped per source per target (PP-510/519) — is cited across faction_layer, march_layer, settlement_adjacency, victory, npc_relational_graph and derived_stats, and has no key type, no owned-state row, and no field on World. Its only access path is a duck-typed getattr(world, 'casus_belli', None) with zero production writers anywhere in the tree, making every CB-gated branch unreachable in a fresh campaign.

**Proposal.** propose_contract — add a Casus Belli state row to faction_state (whose declared A6 scope at module_contracts.yaml:119 already covers faction_layer_v30's treaties/parliament), plus a first-class World field. Both lanes proposed a 'ledger bucket'; rejected — the bucket enum is {clock, derived_value, pool, track} and 'Ledger' collides with the settlement Ledger-of-Consequence. Use bucket: track with a keyed-collection value, which is the standing convention (npc_behavior's 'beliefs/opinions' and 'concerns' at :197-198 are already per-subject keyed collections filed as track). A paired state.casus_belli_granted key is deferred behind G-24 and G-17. REJECT the sibling proposal's Crown carve-out: parliamentary_transfer.py:107's initiator == "Crown" auto-CB must become data on the faction, not a literal (G-16).

**Evidence.** systems/factions/faction_layer_v30.md:376-390 (§3.5 definition + effect table); engine/engine_params/params_tables.yaml:6774-6778 (PP-519 stacking cap/consumption); systems/factions/sim/parliamentary_transfer.py:22-26 ('[ASSUMPTION: game_state models NO Casus Belli ledger (verified — no casus_belli field)]'), :107-112 and :263 (two duck-typed call sites); engine/autoload/game_state.py:163-209 (World dataclass body — no casus_belli field); systems/factions/factions_flow_skeleton_v1.md:183 (zero production writers; every _MODE_CB entry unreachable in a fresh campaign).

**Existing tracking.** TRACKED — both lanes reported 'none found' after grepping only registers/editorial_ledger*.jsonl. tools/observability/INCOMPLETENESS.md:334 already carries it, lane-tagged and generated: "'Casus Belli' — in 21 docs, unregistered (IN) — appears in 21 design docs (57 mentions) but the central ontology (tokens/modules/descriptors/graph nodes) has no match — a candidate missing registration; register it or confirm it is not canonical" (verified verbatim). systems/overview/clock_registry_v30.md:112 also registers '| Casus Belli | per-faction |'. ED-FA-0017 is a historical-precedent annotation only.

---

<a id="g-07"></a>

### G-07 · World

**rung** `provincial_faction` · **kind** `missing_owned_state` · **disposition** `propose_contract` · **independent lanes** 2

**Lenses.** `diplomacy`, `geopolitics`, `churn`

**Claim.** World.treaties is real, serialized and restored per campaign (a dict of TreatyRecord with parties, terms, bound_arc, bound_season, active) with six canon treaty types, but no module owns it and no key type represents an ongoing treaty as queryable state — da.diplomatic_alliance is a one-shot formation event only. Its lifecycle transition sets treaty.active = False with no emit anywhere in the function, so nothing can learn a treaty ended. Separately, that formation key's payload (faction_id, counterparty_faction, terms-as-short-string) can express only a bilateral pair, while canon defines Alliance obligations among signatories generally plus a third-party Guarantor role, and the code's own register_treaty accepts an arbitrary-arity party set with structured dict terms.

**Proposal.** propose_contract — add a Treaties state row to faction_state's block (bucket: track, writable: true), NOT a new 'treaty' module: module_contracts.yaml:119's recorded A6 scope ruling already assigns faction_layer_v30's treaties to faction_state, so minting a separate module contradicts a decision on the record. The arity half is a genuine payload gap but note the cost model: widening da.diplomatic_alliance's REQUIRED fields is Class A supersession (:1273-1278), and the Guarantor is not a signatory — the substrate already supplies the primitive for a non-signatory participant via targets[].role (key_substrate_v30.md:86-92), so no new vocabulary is needed. THREE CORRECTIONS: (a) the runtime key is tuple(sorted(parties)) at treaty.py:150, NOT the frozenset the game_state.py:187 comment claims — a lane propagated the stale comment into a finding about doc/code divergence; (b) 'real, per-campaign' overstates — process_treaty_expirations and register_treaty have zero production callers and propose_treaty is a stubwired no-op, so nothing learns a treaty ended partly because nothing ends one; (c) treaty.py:64 already types terms as a dict, so the registry's 'short string' is a live code↔schema divergence, not merely a design shortfall.

**Evidence.** engine/autoload/game_state.py:187 (treaties dict + the stale frozenset comment), serialized :303-306, restored :380-383; systems/factions/sim/treaty.py:61-77 (TreatyRecord; parties: tuple at :63, terms: dict at :64), :121-146 (process_treaty_expirations — treaty.active=False at :140, no emit in the file), :150 (tuple(sorted(parties)) keying); systems/factions/faction_layer_v30.md:316-329 (§3.1 six treaty types), :326 (Alliance 'Mutual military obligation; casus foederis defined'), :366 (Guarantor option), :350-354 (concession rows); systems/_architecture/key_type_registry_v30.md:233-252 (the bilateral payload); references/module_contracts.yaml:107-110 and the full 27-module enumeration (no treaty row).

**Existing tracking.** module_contracts.yaml:119 + references/CONTRACT_INDEX.md:97 name treaties as in faction_state's scope — a filed W-GAP, not a resolution. audit/2026-08-08-world-churn-audit/00_findings.md:183-185 (ED-IN-0149) measures the dead call graph. systems/factions/factions_flow_skeleton_v1.md:178-179 records the zero-caller fact under OI-19/ED-IN-0091. Ledger hits (ED-791, ED-FA-0015) concern treaty terms and magnitudes, not ownership or arity.

---

<a id="g-08"></a>

### G-08 · state

**rung** `national_faction` · **kind** `missing_payload_field` · **disposition** `propose_key` · **independent lanes** 2

**Lenses.** `politics`, `social_status`, `governance`

**Claim.** state.standing_change's payload is (npc_id, standing_before, standing_after, trigger) with no faction_id and no ladder identifier, while the design's key is at minimum (npc × ladder) — 4 independent 8-rank main-faction ladders plus 7 parallel sub-office ladders an NPC holds simultaneously — and in fact (npc × ladder × arm), since Niflhel's four arms are explicitly independent reputations a character holds at once. Its two same-family siblings, state.coup_attempted and state.succession, both already require faction_id; standing_change is the outlier.

**Proposal.** propose_key — a sibling type rather than a payload edit, because the cost is inverted from what two lanes assumed: key_type_registry_v30.md:1273-1278 makes modifying required_payload_fields a CLASS A supersession event (supersession_register entry + migration rule for existing Keys + Class A patch entry), strictly MORE expensive than the ordinary §10 Class-B path for a new type. type_id state.standing_change_v2, family state_transition; required_payload_fields: npc_id, faction_id, ladder_id, standing_before, standing_after, trigger; default_scale_signature: [territory, peninsula] (matching its siblings). ladder_id must RESOLVE against a ladder registry, not be a frozen enum of proper nouns — the producers' 8-value enum both undercounts (Niflhel alone needs 4 arms) and hardcodes 'niflhel', which registers/editorial_ledger.jsonl:35 records Jordan striking as a faction on 2026-05-09. That is the scripting-drift shape. BLOCKED on G-17.

**Evidence.** key_type_registry_v30.md:630-647 (payload verbatim; trigger enum at :638 is promotion|demotion|succession|exile|death) against :649-668 (state.coup_attempted) and :670-690 (state.succession), both requiring faction_id; systems/factions/faction_politics_v30.md §1.0-§1.4 (4 main ladders), §2.1-§2.7 (7 parallel sub-office ladders, 'parallel not subordinate'), :589 (§2.6 Niflhel: 'It has standing within the four arms, and each arm operates independently. A character can hold Reckoner Standing 4 and be a Dockworker Standing 1 simultaneously... This is not a ladder; it is four parallel informal reputations'); references/module_contracts.yaml:908 (a single opaque 'Standing' row whose own inline comment documents the multiplicity it then collapses — note :903 is state.succession in emits[], the row the producer mis-cited).

**Existing tracking.** none for payload arity. references/KEY_INDEX.md:114 lists only an articulation_layer producer/consumer filing mismatch on this key. module_contracts.yaml:914's '[OPEN — Jordan]' is about module boundary, not key arity.

---

<a id="g-09"></a>

### G-09 · The caste system (Northern/Central/Southern Einhir) is canon-declared 'load-bearing for the entire NPC ecosystem', chose

**rung** `character` · **kind** `missing_owned_state` · **disposition** `already_tracked` · **independent lanes** 2

**Lenses.** `society`, `politics`, `individuation`

**Claim.** The caste system (Northern/Central/Southern Einhir) is canon-declared 'load-bearing for the entire NPC ecosystem', chosen once at character creation, and gates rank advancement across all 12 ladders, Renown, Initiation-Duty Ob, inner-circle Disposition floors, and Conviction-Scar risk — including a §3.6 cross-scale trigger where a caste transgression produces a personal-scale Conviction Scar. It has zero representation in either schema surface, and — sharper than either lane found — it is also absent from the AUTHORING surface: references/npc_registry.yaml, the enforced canonical roster of all named characters, has no caste or background field in its declared schema.

**Proposal.** propose_authoring_field first, propose_key second. The authoring half is unblocked and should land first: add caste_background to references/npc_registry.yaml's schema block (currently required [id, first_name, last_name, faction, role, status], optional [age, birthplace, territory, ts, coherence, stats, convictions, goals, arc_trajectory, notes]) so a fact canon calls load-bearing can at least be recorded. The key half (state.caste_assigned, family state_transition, required_payload_fields character_id + caste, default_scale_signature [personal], emitted once at chargen, consumed by faction_politics/npc_behavior/piety_track resolvers) is blocked on G-17. Per-faction gating tables stay resolver logic, not new key families. Second consumer neither lane named: systems/settlements/governance_play_redesign_v1.md:107 already builds a settlement-scale Hold Court sub-case on the §2.5 caste note.

**Evidence.** systems/factions/faction_politics_v30.md:640-653 (§3.1, 'The player character selects a caste background at character creation'), :655-668 (§3.2 12-row Caste × Rank Advancement table), :670-677 (§3.3 Renown modifier), :679-690 (§3.4 Initiation Duty), :692-711 (§3.5 Disposition floor, 21 named NPCs), :723-753 (§3.6/§3.6.1/§3.6.2 Conviction Scar risk); case-insensitive grep for 'caste' across key_type_registry_v30.md and module_contracts.yaml: ZERO in both (independently re-run); references/npc_registry.yaml:11-13 (schema block, no caste/background field — 'caste' appears in that file only inside free-text conviction_notes/goals/source strings); systems/settlements/settlement_generator_v1.md:53 (P9 requires a per-settlement caste-composition mapping, not merely a scalar).

**Existing tracking.** ED-IN-0062 (registers/editorial_ledger_in.jsonl:17, open, needs_jordan: true) names caste explicitly — 'the political spine (factions/governance-type/franchise/caste/standing/social-contests/parliament)' — and carries a classified ~24-item gap register plus a pressure-key registry. One lane cited it, the other reported 'none found'. Its artifact was evacuated to fork ref c451bcb and is unreadable in the working tree, so I cannot confirm or rule out that it already lists this specific gap, and say so rather than claiming either way. ED-777 is an ID-COLLISION archive entry whose live description is unrelated.

---

<a id="g-10"></a>

### G-10 · Fractional province ownership (ratified ED-711, PP-666: per-settlement PV share, Greater/Lesser renaming, a 75%-threshol

**rung** `province` · **kind** `missing_owned_state` · **disposition** `propose_contract` · **independent lanes** 2

**Lenses.** `churn`, `governance`, `geopolitics`

**Claim.** Fractional province ownership (ratified ED-711, PP-666: per-settlement PV share, Greater/Lesser renaming, a 75%-threshold Consolidation Domain Action, Fragmentation Check, Secession) requires a province held in simultaneous partial control by multiple factions, but Territory.owner is a single str|None, no contract module among the 27 owns the mechanic, and no key type announces fractionalization or consolidation.

**Proposal.** propose_contract — compose the per-settlement share on the already-populated settlement-rung field rather than adding a parallel province-level ownership map: Settlement.owner_faction is set at world-gen for all 37 settlements from the geography YAML's controller key, so province fractional status and PV share become a derivation over that fan-out, in exactly the shape of the existing 'province Accord' derived_value at module_contracts.yaml:711/:732-736. This is a FILING decision (which module owns it — none of the 27 currently do), not a fresh design decision, since ED-711 already ratified the mechanic. Fractionalization/Consolidation key types are deferred behind G-17 and must be filed DECLARE-ONLY per ED-IN-0096.

**Evidence.** systems/factions/fractional_province_ownership_v30.md:22-30 (trigger), :34-40 (PV re-derivation per settlement), :46-58 (Greater/Lesser naming), :63-75 (Consolidation, 75% threshold); engine/autoload/game_state.py:144 (Territory.owner: str | None); systems/settlements/sim/registry.py:60 (Settlement.owner_faction) and :261 (populated at world-gen from the geography controller key — all 37 settlements carry it); references/module_contracts.yaml — 27-row enumeration contains no fractional-ownership row. NOTE the doc's status banner is internally contradictory three ways at :1 (comment PROVISIONAL), :3 ('## Status: CANONICAL'), :5 ('**Status:** PROVISIONAL') — recorded, not resolved.

**Existing tracking.** ED-711 (registers/editorial_ledger_archive.jsonl:422, closed 2026-05-10) ratifies the DESIGN and its closure never touched module_contracts.yaml or key_type_registry_v30.md. ED-IN-0062 is a broad umbrella naming the area but not a schema allocation. No schema-tracking entry found across all lane + archive files.

---

<a id="g-11"></a>

### G-11 · Franchise (per-territory 0-5 parliamentary weight, designed as the deliberate territorial mechanization of caste and fee

**rung** `province` · **kind** `missing_owned_state` · **disposition** `needs_jordan_ruling` · **independent lanes** 2

**Lenses.** `society`, `politics`, `governance`

**Claim.** Franchise (per-territory 0-5 parliamentary weight, designed as the deliberate territorial mechanization of caste and feeding National Influence → Domain Action pools) has no key type and no owned-state row on any module, so the shift triggers its own §5.1 table names — settlement revolt, Church seizure at CI 60+, coup — cannot express their canon-mandated Franchise effect.

**Proposal.** needs_jordan_ruling — franchise_v30.md is Status: DRAFT and nothing should be allocated against an unratified mechanic. ALSO REJECTING the lane proposal outright: it asks to add Franchise to the consuming_systems of state.settlement_revolt, mechanical.theocracy_unification_declared and state.coup_attempted, which is the exact move ED-IN-0096 already reversed — key_type_registry_v30.md:751-756 records 'consuming_systems intentionally EMPTY (corrected 2026-07-29, adj DEFECT 1, ED-IN-0096): articulation was named here, but has no live subscription... declaring it created a false consumer for a type nothing ever fires.' Wiring a DRAFT mechanic into those lists would re-open a closed defect. Ratify or strike franchise_v30 first; the state row follows the ruling.

**Evidence.** systems/factions/franchise_v30.md:3 (Status: DRAFT), :18-20 (§2 definition), :22-49 (§2.1 per-territory table), :104-124 (§4 National Influence formula), :121-131 (§5.1 Shift Triggers), :142-152 (§6 Caste Expression); zero hits for franchise in module_contracts.yaml and key_type_registry_v30.md; registers/mechanics_index.yaml:696 corroborates DRAFT status; key_type_registry_v30.md:726-753, :560-575, :649-666 (the three cited keys and their consumer lists); references/KEY_INDEX.md:24-35 (state.settlement_revolt and theocracy_unification_declared among 8 deliberately consumer-less types).

**Existing tracking.** ED-IN-0062 (open) names 'franchise' explicitly. ED-IN-0097/OI-57 (registers/editorial_ledger_in_archive.jsonl:67) indexes the doc as-is 'without ratifying it', confirming the currency question is tracked while the schema absence is not separately filed. ED-711 is the fractional-ownership sibling, not this.

---

<a id="g-12"></a>

### G-12 · The whole geography/movement layer — 49 settlement adjacency edges, 26 territory edges, terrain_cost_matrix, vision_rang

**rung** `territory` · **kind** `missing_contract_module` · **disposition** `propose_contract` · **independent lanes** 2

**Lenses.** `geography`, `military`, `invasion`

**Claim.** The whole geography/movement layer — 49 settlement adjacency edges, 26 territory edges, terrain_cost_matrix, vision_range with its explicit effective_vision formula, march_budget, radiation_bands, altonian_passes, poi_catalog, forgetting_zone — is authored with real numeric formulas and referenced by every consumer subsystem (invasion routes, grain routes, Campaign Supply, bypass/siege math), yet owns no module_contracts.yaml row and is implemented by zero gameplay code: the only tree-wide readers of these keys are audit and build-decision meta-tooling. An army's mid-march position, accumulated march-budget spend, or a route's terrain-cost total has nowhere to live between scenes.

**Proposal.** propose_contract — add a geography/march module row (scales: [settlement, territory]) mirroring the honest doc:null / sim_module:none declaration pattern the file already uses twice (settlement_economy at :770-792, scenario_authoring at :941-958), so the gap becomes an auditable 'declared but unbuilt' row that KEY_INDEX/CONTRACT_INDEX surface instead of being invisible to the schema entirely. Its one genuinely missing state row is a per-unit position / march-budget-remaining track; the adjacency edges, terrain costs and coordinates are static config, not owned runtime state, and need no key. CORRECTION to one lane: 'all CANONICAL-headed' is false — march_layer_v30.md carries '## Status: CANONICAL' at :5 AND '**Status:** PROVISIONAL' at :7 with an unmet §11 promotion gate at :191-195, so its missing row is a materially weaker finding than the other two pillars'.

**Evidence.** systems/settlements/valoria_geography_v30.yaml:760 (terrain_cost_matrix), :775 (vision_range + formula), :800 (march_budget), :835 (forgetting_zone), :842 (radiation_bands), :875 (altonian_passes), :893 (poi_catalog) — all seven anchors independently reproduced; systems/settlements/settlement_adjacency_v30.md:1-6 (49 edges, ED-710/PP-666/PP-723); systems/settlements/march_layer_v30.md:4-20 plus the contradictory banner above; references/module_contracts.yaml 27-row enumeration — no geography/adjacency/march/movement/vision module; exhaustive grep of systems/ + engine/ for the seven key names matches only skills/valoria-vector-audit/scripts/*.py and tools/observability/build_decisions.py; references/canonical_sources.yaml:160-162 (military_layer_v30 IS SHA-pinned as canonical while absent from contracts).

**Existing tracking.** none found. ners_vsg_reconciliation_v1.md §B9 (RESOLVED 2026-07-13) concerns internal ID-scheme consistency of the adjacency data, not the absence of a contract-owning module. Ledger grep for 'march_layer' and 'geography module': zero hits.

---

<a id="g-13"></a>

### G-13 · The 13-Conviction weighted vector is THE authored character-individuation primitive — Cascade math, npc_behavior reactio

**rung** `character` · **kind** `missing_owned_state` · **disposition** `propose_contract` · **independent lanes** 2

**Lenses.** `beliefs and convictions`, `individuation`

**Claim.** The 13-Conviction weighted vector is THE authored character-individuation primitive — Cascade math, npc_behavior reaction gating, faction Mission alignment and Public Expectation all read it, and conviction_track §2 mutates it at Scar-2 ('Conviction X weight may shift downward... other primaries gain proportionally') — but no module contract owns it. piety_track's only state row is 'conviction scars' (a counter of Scar events, not the vector); npc_behavior's rows are beliefs/opinions, concerns, projects, arc state.

**Proposal.** propose_contract — add {name: "personal_convictions", bucket: track, writable: true} to piety_track (references/module_contracts.yaml:253-297), the module that already owns the Scar mechanic which mutates it. SCOPE CORRECTED: the AUTHORED half already has a home neither lane opened — references/npc_registry.yaml:37-43,:62-68 carries per-character 'convictions: primary [{conviction, weight}] + cultural_label + self_other_initial' — so what is unowned is the RUNTIME-MUTABLE half, and the claim is filed at that reduced scope. descriptor_registry.yaml:159's conv.* registration does not substitute: the file states at :148-153 that registrations 'are not schema bindings'. A LARGER SEAM is recorded, not resolved: FOUR incompatible shapes for 'a character's convictions' coexist — the taxonomy's weighted 13-vector, npc_registry's primary+cultural_label, npe.py:121-122's unweighted 'worldview: list[str]' in the live generator, and ConvictionState, which stores scars/resonant_active/in_crisis/log and no weights at all. The unweighted worldview list is the divergence with teeth, since effective_convictions(npc) is specified against the weighted vector.

**Evidence.** systems/characters/conviction_taxonomy_v30.md:117-131 (§4 personal_convictions YAML schema), :253; systems/characters/conviction_track_v1.md:42 (Scar-2 weight-shift rule); systems/factions/faction_behavior_v30.md:140,:144 (effective_convictions reads it); references/module_contracts.yaml:277 (piety_track's single state row, bucket clock) and :197-200 (npc_behavior's four rows); grep of all 55 key types for 'conviction' returns only :615 (a scar-target string) and :1189 (shared_conviction_primary bool) — no vector-valued payload field; systems/world/sim/npe.py:121-122; systems/characters/characters_flow_skeleton_v1.md:116-121 (ConvictionState fields).

**Existing tracking.** none found for the state-ownership claim across main + archive + all lane ledger files (grep for 'personal_convictions': zero hits). Distinct from ED-IN-0149's J-C (conviction VOCABULARY reconciliation — which taxonomy's names are used) and from ED-IN-0153 (entity-identity ownership generally). ED-FA-0035 is the adjacent cascade-formula gap.

---

<a id="g-14"></a>

### G-14 · Canon's faction taxonomy names a roster of never-playable NPC factions (Altonia, Schoenland, Riskbreakers, Inquisitors,

**rung** `national_faction` · **kind** `missing_owned_state` · **disposition** `propose_contract` · **independent lanes** 2

**Lenses.** `geopolitics`, `invasion`, `world history`

**Claim.** Canon's faction taxonomy names a roster of never-playable NPC factions (Altonia, Schoenland, Riskbreakers, Inquisitors, Guilds, Edeyja/Wardens) that act with faction-shaped attributes — victory_v30 stands up an 'Altonian Governorate NPC faction: Mandate 2, Military 4, Stability 3' mid-campaign, and the Occupation escalation seeds Underground Network points 1:1 from RM Presence. The Faction dataclass admits exactly four static instances; neither schema surface names Altonia or Schoenland, and they are registered only as proper nouns.

**Proposal.** propose_contract — allow Faction instances with parliamentary: false (the field already exists at game_state.py:97) to be constructed for NPC-only actors at the point their canon-specified stat block activates, composing on the existing Faction primitive rather than special-casing Altonia; this depends on G-01's roster-membership row. Underground Network points need a track row on peninsular_strain. TWO PRODUCER CITATIONS WITHDRAWN as fabricated or misfiled: (a) 'victory_v30.md:468 gates an era transition on Altonian diplomacy ≤ 1' — the string does not occur anywhere in victory_v30.md (grep verified); the gate is at systems/overview/peninsular_strain_v30.md:468 (right line number, wrong file); (b) 'Altonian diplomacy' is not an undefined bare term awaiting a faction instance — it is an existing Church-side Cardinal-of-Temperance advancement track, so instantiating an Altonia Faction to host it would create a second competing home. Also FALSIFIED: one lane's claim that the 3-phase Occupation escalation has no contract module — module_contracts.yaml:659-679 declares four IP gates (g_ip100/g_ip85/g_ip80/g_ipfall) sourced to victory_v30 §5.2; what those gates lack is a payload naming the territory set, which is the sharper and still-true form. CURRENCY SEAM recorded, not resolved: systems/_architecture/canonical_registry.md:132 lists 'Altonian diplomacy' under '**Struck:**' while five other docs still gate on it.

**Evidence.** systems/victory/victory_v30.md:585 (Governorate stat block), :610 (Underground Network conversion); systems/overview/peninsular_strain_v30.md:468 (the actual Occupation Era gate); engine/engine_params/params_tables.yaml:6261-6262 ('NPC-Only Factions (never playable): ...Schoenland, Altonia, Edeyja/Wardens'); engine/autoload/game_state.py:51-56,:94-122 (4 static instances, zero 'Altonia' hits); zero hits for Altonia in key_type_registry_v30.md and module_contracts.yaml; references/proper_noun_registry.yaml:293,:396; systems/factions/faction_canon_v30.md:545,:662 and faction_state_authoring_v30.md:105 (the Cardinal-of-Temperance track); systems/_architecture/canonical_registry.md:132; references/module_contracts.yaml:659-679, :854 (standing gap_note: world-state era transitions are UNKEYED).

**Existing tracking.** ED-FA-0001 / ED-IN-0047 (2026-07-13) ruled the PLAYABLE roster count at 4 and noted an 'Altonia-usurper archetype' among intended emergent factions — adjacent, not dispositive on whether already-canonical NPC-only actors get schema homes. systems/victory/victory_flow_skeleton_v1.md:122 independently tracks the era/Occupation gap with a repo-wide grep showing zero .py matches for 'Phased Occupation'.

---

_Continues in [part 2](01_gap_register_part2.md)._
