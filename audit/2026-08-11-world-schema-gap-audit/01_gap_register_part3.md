# World-Schema Gap Register — part 3 of 4 (G-30–G-45)

## Status: REFERENCE — observations against the tree. **Ratifies nothing.**

**Date:** 2026-08-11 · **Lane:** IN · **ED:** ED-IN-0153 · **Base:** `63d4d0c`

Method: [`00_orchestration_plan.md`](00_orchestration_plan.md) · Verdict, held decisions and what this run did NOT cover: [`02_verdict_and_residuals.md`](02_verdict_and_residuals.md)

_Continues [part 2](01_gap_register_part2.md)._ 
> **Read `02_verdict_and_residuals.md` before acting on any row.** Three producer claims were
> **overturned** and are absent here; two proposals **would have caused damage if executed** and
> are flagged there rather than silently dropped. Every row survived a read-only `valoria-critic`
> pass that never saw the producer's reasoning.

## Rows (continued)

<a id="g-30"></a>

### G-30 · env

**rung** `settlement` · **kind** `missing_owned_state` · **disposition** `propose_contract` · **independent lanes** 1

**Lenses.** `demographics`, `economics`

**Claim.** env.population_change is a real emitted key with a well-formed payload (delta, cause) that settlement_layer declares in its emits, but settlement_layer's state has no Population field to apply the delta to, and settlement_economy — the module its own gap_notes name as the natural owner — is a phantom stub (doc: null, state: []) explicitly recommended for retirement, leaving the decision deferred to a register whose host file is not in the tree.

**Proposal.** propose_contract — matches the module's own gap_note recommendation: retire settlement_economy, add Population to settlement_layer's state, and re-point env.population_change's consumer edge. THREE SOFTENERS. (1) The producer mis-cited the key spec at key_type_registry_v30.md:386-400, which is inside mechanical.scene_entered/scene_exited; the real entry is :816-831. (2) Population is not conceptually homeless — settlement_layer_v30.md:158 states Settlement Weight 'Operationalizes the Population dimension named in §1.2 but left unscaled', W_s is already a contract derivation at :750-751, and §1.8c 'Weight loss as Exit' at :273 is the population-leaving mechanic; the fix should compose on Weight, not introduce a parallel scalar. (3) 'cites a nonexistent file' overstates — open_decisions is a real register name used elsewhere in the corpus whose host was in the audit corpus evacuated by ED-IN-0145; it is a stale pointer, not a fabricated one. The numeric formula and starting values remain Jordan's design call, correctly not invented by the producer.

**Evidence.** systems/_architecture/key_type_registry_v30.md:816-831 (env.population_change: cause in {migration, mortality, birth_surge, conscription}); references/module_contracts.yaml:704-711 (settlement_layer emits it; four state rows, no Population), :770-793 (settlement_economy doc: null, state: [], gap_note at :787 'RECOMMEND RETIRE... Adding a Population stat is a DESIGN decision (deferred — open_decisions §2)'); systems/settlements/settlement_layer_v30.md:158,:273; module_contracts.yaml:750-751 (W_s derivation).

**Existing tracking.** gap_note only (module_contracts.yaml:787, mirrored at references/CONTRACT_INDEX.md:123 and :1194) — no ED filed for this item despite it being named in the audit brief. This finding confirms the module's self-diagnosis is accurate and adds that its resolution pointer no longer resolves.

---

<a id="g-31"></a>

### G-31 · Canon routes settlement-scale governance actions — Bishop-Governor installation transferring settlement governance to Ch

**rung** `settlement_faction` · **kind** `missing_payload_field` · **disposition** `already_tracked` · **independent lanes** 1

**Lenses.** `governance`, `events`, `politics`

**Claim.** Canon routes settlement-scale governance actions — Bishop-Governor installation transferring settlement governance to Church, and Grant/Revoke Subnational Management of a named settlement — through da.public_governance by settlement_layer's own ratified routing note, but that key's payload has no field naming which settlement the action targets.

**Proposal.** propose_contract via an optional target_settlement_id on da.public_governance, mirroring the field shape scene.accord_echo already uses (target_settlement, key_type_registry_v30.md:975) — no new naming convention, and critically no second carrier for an action canon already routes through an existing key (this is the composing answer that G-36's rejected key-half must defer to; the two cannot both ship). THREE CORRECTIONS. (1) 'every da_outcome key's default_scale_signature is territory-only' is false — da.diplomatic_alliance is [territory, peninsula] at :245. (2) Adding an OPTIONAL field is Class B; adding a REQUIRED one would be Class A supersession (:1273-1278), the reverse of the cost model two lanes assumed. (3) A separate seam held for Jordan: the substrate already provides an enumerable per-target channel (targets[] with per-target impact_vector/stat_deltas, key_substrate_v30.md:45-53), and whether a settlement id is a legal actor_id there is unresolved — it decides whether this field is needed at all.

**Evidence.** systems/_architecture/key_type_registry_v30.md:191-208 (da.public_governance payload verified: required faction_id/mission_alignment/outcome; optional target_territory_id/public_ceremony/role_acting — no settlement field), :245, :975; systems/settlements/settlement_layer_v30.md:561 (Bishop-Governor), :581 ('a da.public_governance Domain Action that happens to target a settlement'), :583 (granting management); grep of the whole da_outcome family for 'settlement' returns only the consuming-system name settlement_economy; systems/_architecture/key_substrate_v30.md:45-53 (targets[] read verbatim).

**Existing tracking.** TRACKED at the very line the finding cites: settlement_layer_v30.md:581 names ED-FA-0002 as pending, and registers/editorial_ledger_fa.jsonl:2 shows it OPEN, RATIFIED-AS-ACCEPTED 2026-07-05, with an ACTION to 'author one home doc unifying card-hand + faction actions + resolver + da.* tagging (what a player does on their strategic turn, costs, degrees, feedback per verb)' — i.e. exactly where this payload field is due. The lane reported 'none found'.

---

<a id="g-32"></a>

### G-32 · Canon requires settlement-to-settlement and province-to-province economic flow (grain routes tracing the adjacency graph

**rung** `settlement` · **kind** `missing_edge` · **disposition** `needs_jordan_ruling` · **independent lanes** 1

**Lenses.** `economics`, `geography`

**Claim.** Canon requires settlement-to-settlement and province-to-province economic flow (grain routes tracing the adjacency graph to a breadbasket/Port source; the Requisition verb explicitly stripping a neighbour and displacing Dearth to it), but the only economic key type is a one-to-many top-down faction action with no settlement-to-settlement edge, and the nominally responsible module is a phantom stub. SHARPENED: the underlying design ruling has been reversed without reconciliation and the reversal has propagated into live continuity — a resolved archive ruling is being worked as an open item on two live surfaces.

**Proposal.** needs_jordan_ruling — the BALANCE-005 contradiction must be ruled before any schema work: registers/editorial_ledger_archive.jsonl:477 is status resolved, date_resolved 2026-04-13, resolution 'The dependency is narrative pressure, not mechanical. Monitor in playtesting', while ED-SE-0009 reopens it as a mechanical rule (§4.3b PROPOSED) and registers/handoffs/HANDOFF_SE.md:61 describes it as 'the open geography_v30 ED-054/BALANCE-005'. Once ruled, the schema shape is settled and uncontroversial: do NOT resurrect settlement_economy (its RECOMMEND RETIRE verdict is sound — no doc, no state, no logic); the consuming module is settlement_layer, which already owns Prosperity/Order, plus a state.grain_route_cut key (family state_transition; required_payload_fields settlement_id, source_or_neighbor_id, cause; default_scale_signature [settlement]) and the granary: int 0-3 registry field the doc itself already names as a follow-on. Blocked additionally on G-17.

**Evidence.** systems/settlements/settlement_layer_v30.md:771 (Requisition verb: 'a neighbor with grain/granary on the adjacency graph... displaces the Dearth to that neighbor'), :795-834 (§4.3b PROPOSED under ED-SE-0009, 'its sole output is a Dearth trigger consumed by §4.3a'); systems/world/geography_v30.md:162 (BALANCE-005 open item in a CANONICAL doc: 'Hafenmark food dependency has no mechanical teeth'); references/module_contracts.yaml:770-792 (settlement_economy phantom); systems/_architecture/key_type_registry_v30.md:274-291 (da.economic_intervention, faction_id → target_territories); whole-file grep for trade/route/grain/supply/market key types: zero.

**Existing tracking.** ED-SE-0009 (registers/editorial_ledger_se.jsonl, open, 2026-07-08) tracks authoring the RULE and its own text notes 'No sim code yet' without mentioning Keys or contracts at all. BALANCE-005 (registers/editorial_ledger_archive.jsonl:477, resolved 2026-04-13) ruled the opposite. Both are live on two surfaces; neither reconciles with the other.

---

<a id="g-33"></a>

### G-33 · Canon requires a persistent individuated military-unit entity (a named formation stationed in a territory, with Size/Dis

**rung** `cross_rung` · **kind** `missing_key_type` · **disposition** `needs_jordan_ruling` · **independent lanes** 2

**Lenses.** `military`, `invasion`

**Claim.** Canon requires a persistent individuated military-unit entity (a named formation stationed in a territory, with Size/Discipline/Experience tracked across seasons of Reinforcement) and a settlement-owns-garrison relation whose Discipline is read cross-module to compute effective Defense — but mass_battle's contract state is empty, settlement_layer has no garrison row, and no key type represents a unit.

**Proposal.** needs_jordan_ruling — this cannot be filed by this audit, for a stated reason. FOUR corrections make it a lane-boundary question rather than a schema proposal. (1) The entity is not absent from the tree: systems/mass_battle/sim/units.py:325-336 defines a typed Unit dataclass (size, discipline, discipline_start, command, subunit cells), battle-scoped and unregistered — materially narrower than 'no unit at all'. (2) The garrison side is not blank either: registry.py:67 declares garrison: bool, serialized at :118/:143, and Garrison Strength is already a contract derived_value with a formula at module_contracts.yaml:709,:741-744; the defensible finding is the producer's own proposal, that a bool undersells a unit reference. (3) The proposed default_scale_signature [territory, provincial] would raise at keys.py:414-418 the first time apply_defaults ran, since 'provincial' is not in SCALES. (4) DECISIVE: module_contracts.yaml:566-572 reserves mass_battle's rows to the MB lane as single-writer, stating 'the join lane does not touch MB's rows even to add a field' (OI-54, ED-IN-0097 W4). I report that boundary and do not rule on the MB lane's disposition.

**Evidence.** systems/mass_battle/military_layer_v30.md:39 ('A unit token on the board is a named military formation stationed in a specific territory... Size, Discipline, Experience'); systems/mass_battle/sim/units.py:325-336 (the Unit dataclass); references/module_contracts.yaml:578 (mass_battle state: []), :110 (faction stats 1-7, the sole military-adjacent slot), :566-572 (the MB single-writer boundary), :709,:741-744 (Garrison Strength derivation); systems/settlements/settlement_layer_v30.md:957 ('effective Defense = settlement Defense + garrison Discipline'); systems/settlements/sim/registry.py:67; references/canonical_sources.yaml:160-162 (military_layer_v30 SHA-pinned as canonical while absent from module_contracts).

**Existing tracking.** none found for the schema absence (ledger hits on military_layer are PP renumbering / Hafenmark-modifier entries ED-770/776/782/868; ED-440 is an archived Fort-Level ruling; ED-SE-0015's governor_emergence is unrelated). The MB lane boundary at module_contracts.yaml:566-572 is the governing tracked constraint.

---

<a id="g-34"></a>

### G-34 · Five ongoing Parliamentary Sanction statuses (Censure/Embargo/Blockade/Combined/Outlawry) and two durable constructive-m

**rung** `provincial_faction` · **kind** `missing_owned_state` · **disposition** `propose_contract` · **independent lanes** 1

**Lenses.** `diplomacy`, `politics`, `governance`

**Claim.** Five ongoing Parliamentary Sanction statuses (Censure/Embargo/Blockade/Combined/Outlawry) and two durable constructive-motion outcomes (Recognition Challenge's '-1 TCV from victory calculation, until rescinded'; Succession Endorsement's permanent recognised heir) are long-duration per-target political conditions with explicit renewal/lapse/rescission rules, and none has a state field anywhere — including victory's own state block, which is a single reader-only row with nowhere for a TCV modifier to land.

**Proposal.** propose_contract — add an Active Sanctions row (target_faction, tier, imposed_season, renewal_status) to faction_state and a Recognition status row carrying the per-faction TCV modifier that victory's derivations block can read alongside its existing clock reads. Compose on bucket: track or pool — the lane's 'ledger-bucket row' invents an enum value absent from all 40 state rows and collides with the settlement Ledger-of-Consequence, so it is rejected for the same reason as in G-06 and G-24.

**Evidence.** systems/factions/faction_layer_v30.md:445 (veto-eligible list naming Censure/Embargo/Outlawry/Recognition Challenge/Succession Endorsement), :451-465 (§5.4 table: Embargo 'Until lifted', Outlawry 'Permanent until petitioned', Recognition Challenge '-1 TCV from victory calculation | Until rescinded', Succession Endorsement 'Permanent'); references/module_contracts.yaml:107-110 (faction_state — no sanction or recognition row), :828-829 (victory state: one reader-only row 'MS / IP / CI / Turmoil / Accord / Mandate / PV / PT reads', writable: false).

**Existing tracking.** none found — grep of ledgers for 'Recognition Challenge' and 'Parliamentary Sanction' returns only ED-FA-0006 itself, the parameterization decision collapsing five mechanics into one action, which is about action design rather than state ownership.

---

<a id="g-35"></a>

### G-35 · Shadow Renown (0-10) and Deniability Debt (0-7) are ratified canon state closed as CANON at ED-632/ED-633, driving a 7-s

**rung** `national_faction` · **kind** `vocabulary_conflict` · **disposition** `needs_jordan_ruling` · **independent lanes** 1

**Lenses.** `politics`, `social_status`

**Claim.** Shadow Renown (0-10) and Deniability Debt (0-7) are ratified canon state closed as CANON at ED-632/ED-633, driving a 7-step threshold ladder that reaches mandatory Commander demotion, with no key type and no state field on either faction_state or faction_politics. BUT the schema absence is not the first thing to resolve: three registries carry a DEPRECATED disposition on Deniability Debt, directly contradicting the doc that specifies it and the ED that closed it as CANON.

**Proposal.** needs_jordan_ruling — currency must be ruled before any schema row is added, or the row canonises a struck mechanic. references/definitions/vocab_source.yaml:593-601, references/deprecated_terms_registry.yaml:74-77 and references/glossary.md:285 all mark Deniability Debt DEPRECATED with 'mechanic functions redistributed to settlement-broker (settlement_layer §4.7-4.9)' and 'Niflhel-as-faction struck per ED-764', while faction_politics_v30.md:424 says 'stage13 mechanic, retained' and ED-633 closes it CANON. The producer's grep claim that the only non-source hits were one classification row and unrelated prose is withdrawn — the term hits 23 files including three registries it did not open. ALSO WITHDRAWN: the stated consequence 'Deniability Debt=3 triggers an NPC investigation review per npc_roster_v30.md:76,272-273' is not what those lines say (:76 is 'Deniability Debt +1 when aborted operations leave evidence'; :272-273 are Torsvald prose); the Debt-3 effect is a Riskbreaker Exposure card at faction_politics_v30.md:492. The real consequence set is larger than claimed but is not the thing cited.

**Evidence.** systems/factions/faction_politics_v30.md:340-500 (§2.2b specs), :424, :490-496 (the 7-step ladder to mandatory Commander demotion at 7); registers/editorial_ledger_archive.jsonl:360-361 (ED-632/ED-633 both resolved/CANON); references/definitions/vocab_source.yaml:593-601, references/deprecated_terms_registry.yaml:74-77, references/glossary.md:285 (the three DEPRECATED dispositions); zero hits for either term in key_type_registry_v30.md or module_contracts.yaml; systems/_architecture/governance_type_registry_v1.md:89 (a PROPOSED classification-only survey row, no schema proposal).

**Existing tracking.** ED-IN-0030 (registers/editorial_ledger_in.jsonl:10) mentions the pair only in passing, to rule it OUT as the referent of an unrelated 'debt scene' phantom-mechanic investigation. The currency contradiction itself is untracked.

---

<a id="g-36"></a>

### G-36 · Six of the seven canon subnational-faction archetypes (Guilds, Ministry, Löwenritter, RM, Wardens, Niflhel — Church exce

**rung** `settlement_faction` · **kind** `missing_owned_state` · **disposition** `propose_contract` · **independent lanes** 2

**Lenses.** `politics`, `governance`, `individuation`

**Claim.** Six of the seven canon subnational-faction archetypes (Guilds, Ministry, Löwenritter, RM, Wardens, Niflhel — Church excepted, since it maps onto the existing national Faction object) have no contract module, no owned-state row and no key type; each exists only as a free-text key in Settlement.subnational: dict, which is a DEAD field — it appears exactly three times in registry.py (declaration, to_dict, from_dict) with no write site anywhere, so it round-trips through serialization while nothing populates it.

**Proposal.** propose_contract — add one generic state row to settlement_layer: {name: "subnational faction management (archetype -> foothold level)", bucket: track, writable: true}, sourced from the existing dict shape, with 'archetype' staying a free string exactly as the canon table's left column already is — do NOT special-case the seven. THE KEY HALF IS DROPPED AND THE REASON IS THE POINT: one lane proposed a new settlement_layer-emitted state.subnational_management_changed, but settlement_layer_v30.md:581 (ED-SE-0005, ratified under the ED-IN-0027 pessimist-action audit) already rules that Grant/Revoke Subnational Management is 'mechanically a da.public_governance Domain Action that happens to target a settlement', single-homed in the FA lane's inventory under ED-FA-0002. Minting a second carrier for an action canon already routes through an existing key is exactly the shape-divergence guardrail; G-31's optional target_settlement_id is the composing answer and the two cannot both ship. A sibling lane's premise that this is a 'real, built mechanism' for §5.2 cross-scale claiming is OVERTURNED by the three-occurrence census.

**Evidence.** systems/settlements/settlement_layer_v30.md:563-575 (the 7-row archetype table), :581 (the ratified da.public_governance routing), :583-587 (grant/revoke/contest vocabulary); systems/settlements/sim/registry.py — grep of 'subnational' returns exactly :85 (dataclass default, comment 'foothold -> level'), :126 (to_dict), :151 (from_dict), run directly and verified; populate_from_geography (:215-266) and succeed_governor (:198-207) never touch it; engine/autoload/game_state.py:51-56 (Guilds/Ministry/Löwenritter/RM/Wardens/Niflhel never instantiated as anything); references/module_contracts.yaml:707-711 (no subnational row); grep of key_type_registry_v30.md for subnational/foothold: zero; systems/_architecture/governance_type_registry_v1.md:117 (the 'already-built implementation' overclaim, disproved by the census).

**Existing tracking.** none found — grep of all ledger files and both index files for 'subnational' and 'foothold' returns zero hits outside the prose doc and the dead dict. The same defect class IS filed for sibling fields at systems/settlements/settlements_flow_skeleton_v1.md:147,:149 (Settlement.legitimacy/.popular_support/.religious_building), which no lane cited.

---

<a id="g-37"></a>

### G-37 · The geography file authors a per-settlement second faction role (controller_subordinate: Löwenritter on S-014 Ehrenfeld,

**rung** `settlement` · **kind** `missing_individuation_descriptor` · **disposition** `propose_authoring_field` · **independent lanes** 1

**Lenses.** `individuation`, `governance`

**Claim.** The geography file authors a per-settlement second faction role (controller_subordinate: Löwenritter on S-014 Ehrenfeld, whose controller is Crown) that the loader has nowhere to put and silently drops — canon's §3.3 subnational-management mechanic requires two independently-varying faction roles per settlement, and the Settlement dataclass carries only owner_faction. SHARPENED: the loader's provenance docstring is false in two ways, one of which no lane caught — it asserts 'controller -> Settlement.owner_faction (one entry, S-037/Schoenland)', but all 37 settlements carry a controller key and all 37 get owner_faction set. A docstring written specifically to certify no-fabrication states a count its own data contradicts.

**Proposal.** propose_authoring_field — add managing_faction: str | None to Settlement (registry.py), distinct from owner_faction and from the dead subnational dict (wrong grain: §3.3 grant/revoke is a discrete flag, not a graduated level, per governance_type_registry_v1.md's own classification), wire populate_from_geography to read controller_subordinate into it, and register a set.managing_faction descriptor in descriptor_registry.yaml's settlement_stats. Correct BOTH docstring assertions in the same change. The lane's disproof of governance_type_registry_v1.md:117's 'this is the literal, already-built implementation' claim is upheld and independently reconfirmed by the three-occurrence census in G-36. Any paired key composes on mechanical.settlement_captured's existing pattern, not a new family.

**Evidence.** systems/settlements/valoria_geography_v30.yaml:356 (controller_subordinate: Löwenritter — the only occurrence of this key in the 37-settlement file, grep-verified unique; S-014's controller is Crown); systems/settlements/sim/registry.py:215-266 (populate_from_geography reads only type/stats/territory/controller), :232-239 (the false-count and false-completeness docstring), :253-263 and :261 (owner_faction set for every settlement); valoria_geography_v30.yaml:251-540 (all 37 settlements carry controller: — 15 Crown, 10 Hafenmark, 10 Varfell, 1 Church, 1 Schoenland); systems/settlements/settlement_layer_v30.md:565-618 (§3.3 with concrete Ob formulas); systems/_architecture/governance_type_registry_v1.md:117.

**Existing tracking.** governance_type_registry_v1.md §2.3/§3.3 (PROPOSED, no ED allocated per CURRENT.md:94) names the general mechanic while overclaiming its build status; it does not note the loader-level field gap or the specific dropped S-014 datum. Grep of registers/editorial_ledger*.jsonl for controller_subordinate / subnational / management grant: none found.

---

<a id="g-38"></a>

### G-38 · Nothing in the schema can express which starting world a campaign uses

**rung** `cross_rung` · **kind** `missing_authoring_schema` · **disposition** `needs_jordan_ruling` · **independent lanes** 1

**Lenses.** `world configurability`, `individuation`

**Claim.** Nothing in the schema can express which starting world a campaign uses. scenario_authoring — the only module with any conceptual claim to authoring a variant starting world — declares an emit vocabulary of env.crisis/env.disaster whose payloads are runtime event descriptors, not a starting configuration; and create_world() takes only an RNG seed. No key type or contract state anywhere carries era, faction roster, calamity state, starting clocks or invasion posture as an authorable value.

**Proposal.** needs_jordan_ruling — whether a singleton starting world is an intentional design ruling. TWO SOFTENERS mean the proposal must be re-cut before it is acted on. (1) The module's own gap_note already names this: module_contracts.yaml:958 records fork 11 RATIFIED (ED-IN-0011), 'compile is authoring-time, its output packs seed runtime', and lists the unbuilt pieces as 'no Stage-1 compile tooling / template-pack format / settlement_layer injection wiring — C-INJ-5'; the template-pack format IS the starting-configuration schema the lane said nothing tracks, so 'neither addresses the distinct claim made here' does not hold. (2) The corpus already HAS an authored world-data locus the lane missed — valoria_geography_v30.yaml is loaded at world-gen by populate_from_geography, mapping its own territory/type/stats/controller keys onto Settlement fields — so 'every faction/territory/garrison value hardcoded in module-level dicts' is true of create_world() but false of world-gen as a whole. Any variant-selection design should compose on that YAML plus the ED-IN-0011 template-pack, not a new world_config.* key family. WHAT REMAINS SQUARELY TRUE: env.crisis/env.disaster cannot be widened to carry compile-time configuration without becoming incoherent with their own scale_signature.

**Evidence.** references/module_contracts.yaml:941-958 (scenario_authoring: doc null, sim_module none, consumes [], state [], emits only env.crisis/env.disaster terminal:false; the fork-11 gap_note at :958); engine/autoload/game_state.py:44-91 (STARTING_OWNER/STATS/ACCORD/PT/GARRISON hardcoded dicts), :212 ('def create_world(seed: int | None = None)' — no config parameter), :229-231 (the inline individuation literals of G-15); systems/_architecture/key_type_registry_v30.md:783-814 (both payloads are crisis_type/disaster_type + affected_territories only); systems/settlements/sim/registry.py:215-266 (the geography loader, PP-726, 37 settlements).

**Existing tracking.** references/CONTRACT_INDEX.md:139-140 and :43 track scenario_authoring as UNBUILT (A4 non-terminal emission with no declared consumer; A6 cross-scale edge with no transitions entry) citing ED-IN-0011/ED-IN-0023. Contrary to the lane's read, module_contracts.yaml:958's 'template-pack format' item does address the authoring-schema half.

---

<a id="g-39"></a>

### G-39 · The canonical Key-migration spec gives npc_memory's storage a fully-typed schema (MemoryReference: key_uuid, salience [0

**rung** `character` · **kind** `missing_owned_state` · **disposition** `propose_contract` · **independent lanes** 1

**Lenses.** `personal history`, `beliefs and convictions`

**Claim.** The canonical Key-migration spec gives npc_memory's storage a fully-typed schema (MemoryReference: key_uuid, salience [0,7] with decay, salience_floor, and a 10-per-NPC cap) as the explicit bridge from the legacy Memory record to the Key substrate, and states that four Procedures emit Keys specifically so per-NPC salience can be set on emission — yet the npc_memory contract declares state: [] and emits: [], so there is nowhere to write a single MemoryReference.

**Proposal.** propose_contract — add {name: "MemoryReferences", bucket: track, writable: true} to npc_memory (the 10-per-NPC cap makes it a bounded track, not an unbounded log; the Key log itself stays the unbounded source per §2.3). TWO SOFTENERS. (1) Mis-attribution: the 'tree-wide grep for npc_memory* returns nothing' text is in the sim_module comment at :233-234, not gap_notes; the actual gap_note at :247 reads 'home doc unlocated — Memory schema lives in doc-12 §2.3 schema bridge; standalone spec [GAP]', i.e. the module already self-flags most of this finding. (2) With ED-WR-0003 covering the adjacent visibility/revelation half and the gap_note covering the home-doc half, the residual is a filing item on an already-flagged module rather than an unnoticed absence — entered at reduced severity for that reason. The producer's core point stands: neither of ED-WR-0003's action items would add this row, so the gap survives their execution.

**Evidence.** systems/factions/political_dynamics_keys_migration_v30.md:44,:55-64 (class MemoryReference: key_uuid/salience/salience_floor), :73 (the 10-MemoryReference cap), :117,:136,:240 (each Procedure creates one on Key emission); references/module_contracts.yaml:230-247 (npc_memory: the four declared consumes at :238-241; emits: [] and state: [] at :242-243; gap_note at :247).

**Existing tracking.** ED-WR-0003 (registers/editorial_ledger_wr.jsonl:3, RATIFIED-AS-ACCEPTED by Jordan 2026-07-05) targets (a) a visibility/'overheard' fix for scene.interaction/scene.gossip's hardcoded private_observers and (b) writing npc_behavior_v30 §6.1/§6.1b's revelation procedures; neither action item adds the state row or the MemoryReference schema to the contract. The module's own gap_note at :247 is the closer tracking.

---

<a id="g-40"></a>

### G-40 · Canon requires faction affiliation to be changeable (dismissal to Standing -1 with a persistent Dishonored flag, volunta

**rung** `character` · **kind** `missing_payload_field` · **disposition** `propose_key` · **independent lanes** 1

**Lenses.** `politics`, `social_status`

**Claim.** Canon requires faction affiliation to be changeable (dismissal to Standing -1 with a persistent Dishonored flag, voluntary declaration for a different faction, defection as a named demotion trigger) but NPC.affiliation_faction is a bare Optional[str] set once at construction with zero mutator anywhere in the tree, and no key type carries an affiliation transition.

**Proposal.** propose_key — type_id state.affiliation_changed, family state_transition (§5, alongside state.standing_change/state.succession, not a new family and not a new emitting subsystem beyond faction_politics which already emits the siblings); required_payload_fields: npc_id, faction_before, faction_after, trigger (dismissal | defection | voluntary_declaration | patron_death, matching faction_politics §1.0's own vocabulary); default_scale_signature: [personal, territory]. BLOCKED on G-17. SOFTENED: 'neither payload names a faction transition' overstates by a hair — state.standing_change's required trigger enum already includes exile and death (key_type_registry_v30.md:638), so departure and removal are expressible causes on an npc-keyed event; what is genuinely missing is faction_before/faction_after. The authoring surface also carries affiliation (npc_registry.yaml's schema requires a per-character faction field), so the gap is the mutation-and-announce path, not the concept. NOTE the interaction with G-08: if standing_change gains a sibling, affiliation may belong on it rather than as a separate type — the two proposals should be reconciled before either lands.

**Evidence.** systems/world/sim/npe.py:124 (affiliation_faction: Optional[str] = None); grep of 'affiliation_faction\s*=' finds only the dataclass default and generate_npc's one-time constructor assignment at :313 — no mutator; systems/factions/faction_politics_v30.md:76-88 (Dismissal/Dishonored-flag table, 'Faction Membership: Retained/Forfeited'); systems/_architecture/player_agency_v30.md:157 ('...or declare for a different faction'); grep of key_type_registry_v30.md for affiliation/membership: zero matches; :638 (the existing trigger enum); references/npc_registry.yaml:12.

**Existing tracking.** ED-652/ED-776 (registers/editorial_ledger_archive.jsonl:371) close the PROSE spec of dismissal mechanics as 'fully spec'd' — design-doc closure, not schema. No open ED for the schema side. The Dishonored half is partly homed: module_contracts.yaml:908's Standing row comment already cites '§1.0a, ED-776' demotion, so the owning module and section are declared and only the flag field is missing.

---

<a id="g-41"></a>

### G-41 · The world model implies individual character mortality (env

**rung** `character` · **kind** `missing_owned_state` · **disposition** `propose_contract` · **independent lanes** 1

**Lenses.** `churn`, `events`, `demographics`

**Claim.** The world model implies individual character mortality (env.crisis names war/plague; env.population_change names mortality as a cause) but the NPC dataclass carries no status or alive field, and no event whose SUBJECT is a character's death, incapacitation or removal exists — only an aggregate settlement-level population delta with no per-NPC attribution.

**Proposal.** propose_contract at reduced scope, and the producer's disciplined handling is upheld and worth preserving: ED-898 rules that named-character combat death is deliberately excluded ('no mass-battle mechanic kills a player or named character' — incapacitation/capture instead), so this is NOT a request for a death key, and any lifecycle primitive must carry status in {active, incapacitated, captured, removed} per that ruling rather than a binary alive/dead. SOFTENED: 'no key type announces death or removal' is too strong — state.standing_change's trigger enum includes death and exile on an npc-keyed payload (:638) and meta.knot_ruptured's required cause enum includes death (:1040), so two existing per-NPC carriers already announce a character's removal as a CAUSE, and a lifecycle primitive should compose there rather than starting from nothing. npe.NPC also carries an untyped persistent_state dict (:134) — not a status field, but not 'nowhere to put it' either. The real residual is narrower: no TYPED lifecycle status, and no event whose subject rather than side-effect is the removal.

**Evidence.** systems/world/sim/npe.py:114-134 (NPC dataclass: npc_id, territory_id, stance, worldview, affiliation_faction, affiliation_loyalty, hidden_allegiance, compromise_category, volatility, deviation_roll, is_arc_vector, persistent_state — no status/alive field); systems/_architecture/key_type_registry_v30.md:816-831 (env.population_change, settlement/territory-scale only, no npc_id), :638, :1040; registers/editorial_ledger_archive.jsonl ED-898 ('The engine emits an incapacitated/captured state... the post-capture consequence... is a world-layer event rendered OUTSIDE the mass-battle container (not designed here)').

**Existing tracking.** audit/2026-08-08-world-churn-audit/00_findings.md D5 (ED-IN-0149) tracks that world.npcs stays empty in live campaigns — a build/wiring gap, distinct from this one, which holds even for a populated store since the field does not exist on the dataclass. Grep of ledgers for 'npc status'/'npc lifecycle'/'alive' near 'NPC': none found.

---

<a id="g-42"></a>

### G-42 · env

**rung** `cross_rung` · **kind** `missing_edge` · **disposition** `needs_jordan_ruling` · **independent lanes** 2

**Lenses.** `events`, `churn`

**Claim.** env.crisis and mechanical.season_change declare their consumers as unresolvable wildcards — 'consuming_systems: [all]' and '[all subscribing systems]' — while their direct siblings env.disaster and mechanical.accounting name concrete consumer sets. The asymmetry is evidence a consumer edge is missing rather than the types being legitimately terminal by nature.

**Proposal.** needs_jordan_ruling — HELD at ED-IN-0151 item c ('which of the 8 consumerless keys are legitimately terminal'), and the producer correctly declined to rule. BOTH LANES' FRAMING IS CORRECTED: 'zero declared consumers, not even a registry-only one' is self-contradicted by the registry text — the accurate statement is 'declared as an unresolvable wildcard', which is a JOIN defect rather than an absent declaration, and both lanes quoted KEY_INDEX.md's generated module-name translation as if it were the registry's own text. The temporal spine is also declared, just not as consumer edges: module_contracts.yaml:1082-1087 makes season_tick and accounting_boundary the first two phases of the canonical accounting_sequence, enforced by check A12. Fold both into the ED-IN-0151 fork as one line rather than carrying two findings.

**Evidence.** systems/_architecture/key_type_registry_v30.md:797 (env.crisis consuming_systems: [all], permanence indelible, horizon far) vs :813 (env.disaster: [faction_layer, settlement_layer, articulation], persistent/near); :312 (mechanical.season_change: [all subscribing systems]) vs :328 (mechanical.accounting: [faction_layer, articulation]); references/KEY_INDEX.md:171,:179 (the translated rows the lanes quoted); references/module_contracts.yaml:1082-1087 (accounting_sequence phases) and engine_clock's gap_note citing ED-1051, open.

**Existing tracking.** ED-IN-0151 (open, needs_jordan: true) names exactly this class of decision as HELD. ED-1051 (open) is the closest item for the season_change half but is scoped to engine_clock's doc: null field rather than the consumer edge. No entry rules on either key directly.

---

<a id="g-43"></a>

### G-43 · At least four parallel scale vocabularies coexist with no reconciliation: the Key registry's default_scale_signature val

**rung** `cross_rung` · **kind** `vocabulary_conflict` · **disposition** `already_tracked` · **independent lanes** 2

**Lenses.** `entity-ladder coherence`, `substrate integrity`

**Claim.** At least four parallel scale vocabularies coexist with no reconciliation: the Key registry's default_scale_signature values, module_contracts.yaml's implicit 7-value scales enum, engine/substrate/keys.py's runtime 4-member SCALES, scale_hierarchy_v1's ratified Country>Duchy>Province>Territory>Settlement ladder, and a fifth in scale_transitions_v30 (Object/Personal/Relational/Territorial/Structural, in which 'Structural — a kingdom, an institution' is the national tier under another name). 'provincial' appears in module_contracts rows and in no substrate enum; 'national' appears in canon prose and in no enum at all. The registry's own signature vocabulary is not internally closed either — one entry declares 'territorial', a singleton token no other entry uses.

**Proposal.** needs_jordan_ruling — HELD at ED-IN-0103 §6 fork 1 per module_contracts.yaml:16-21 ('No vocabulary unification lands here or anywhere else until that fork resolves'). RECORD ONLY, and three lane proposals are barred by it: G-21's token promotion, one lane's 'add national to the enum' (additive to one of five parallel vocabularies is still dialect growth while the fork holds — the disclaimer 'this is additive, not a reconciliation' names the hazard without avoiding it), and G-33's [territory, provincial] signature. The genuinely new data this audit contributes, which the held note does not contain, are the 0-of-55 'provincial' measurement and the 'territorial' singleton at :1084 — the latter is upstream of any request to add a value, and I found no ED recording it.

**Evidence.** engine/substrate/keys.py:65 (SCALES, 4 members, read verbatim) and systems/_architecture/key_substrate_v30.md:57 (the authoritative enum); references/module_contracts.yaml:16-21 (OI-40a, the held fork, whose own text compares 'this field's 7-value enum vs keys.py's runtime 4-enum vs mechanics_index_gen's 9-value peninsular spelling'), :71,:308,:700 (territory/provincial used interchangeably per-module); systems/_architecture/key_type_registry_v30.md — 'provincial' 0 hits across the whole file (re-run), :1084 ('territorial' singleton); systems/settlements/scale_hierarchy_v1.md:9-24; systems/_architecture/scale_transitions_v30.md:26-36 (the fifth vocabulary); skills/valoria-module-adjudicator/SKILL.md:53 (the 7-value enum's owner, already carrying an '[ASSUMPTION: ... unknown values are warnings, not violations]' marker).

**Existing tracking.** ED-IN-0103 §6 fork 1, HELD, recorded at module_contracts.yaml:16-21 (OI-40a). ED-IN-0153 measured fact 2 restates it from the ladder side. This row adds evidence to the held fork; it is not a separate item.

---

<a id="g-44"></a>

### G-44 · The settlement-to-province membership relation — canon's own foundational grouping ('Each province contains 1-3 settleme

**rung** `cross_rung` · **kind** `missing_edge` · **disposition** `propose_contract` · **independent lanes** 1

**Lenses.** `geography`, `entity-ladder coherence`

**Claim.** The settlement-to-province membership relation — canon's own foundational grouping ('Each province contains 1-3 settlements'), load-bearing for the province-Accord derivation and the accounting drift probe — has no contract locus: it is not a state row, not a key-type payload field, not a declared input to the derivation that depends on it, and Settlement.province_id is an unvalidated free string with nothing checking it names a live territory.

**Proposal.** propose_contract at reduced scope. 'No schema locus anywhere' is withdrawn: valoria_geography_v30.yaml is the canonical authored source of the mapping (PP-726) and populate_from_geography loads it at world-gen, documenting the field mapping per field at :230-231 ('territory -> Settlement.province_id — the geography file's own key name for the same referent'). The residual is real and narrower, and is what the lane's own proposal already got right: (a) add the membership key to the province-Accord derivation's inputs list at module_contracts.yaml:715-720, which currently lists only 'Order' and silently assumes the grouping; (b) add a referential-integrity check that territory names a live World.territories entry — the idiom already exists and was simply not applied here, since registry.py:254-257 DOES raise on an illegal settlement type. The lane correctly refuses to touch the ED-IN-0103 vocabulary fork while doing it, which is the right discipline.

**Evidence.** systems/settlements/settlement_layer_v30.md:15 ('Each province contains 1-3 settlements'); systems/settlements/sim/registry.py:180-190 (province_members/province_accord — a raw s.province_id == province_id filter, no schema declaration), :215-266 with :230-231 and :261 (the geography loader and its documented mapping), :254-257 (the illegal-type refusal idiom); systems/overview/sim/accounting.py:53-92 (_probe_province_accord_drift — measures a VALUE divergence built on top of this grouping, never validates the grouping); references/module_contracts.yaml:715-720 (province Accord derivation, inputs: ['Order'] only).

**Existing tracking.** OI-37 (cited at systems/overview/sim/accounting.py:34-38; registers/handoffs/HANDOFF_SE.md:127-134, 'single highest-priority open item') tracks the VALUE reconciliation between registry.province_accord and Territory.accord — adjacent and distinct from the membership edge's missing declaration. No dedicated tracking found for the edge itself.

---

<a id="g-45"></a>

### G-45 · Two CANONICAL-doc-backed, mechanics_index-registered province-scale territory-transfer resolvers have no row at all in m

**rung** `territory` · **kind** `missing_contract_module` · **disposition** `propose_contract` · **independent lanes** 1

**Lenses.** `governance`, `geopolitics`

**Claim.** Two CANONICAL-doc-backed, mechanics_index-registered province-scale territory-transfer resolvers have no row at all in module_contracts.yaml, and propagation_spec's own eight-down-seam closure worklist has no faction→settlement_layer seam, so a province-scale transfer has no declared channel for its per-settlement Order effects.

**Proposal.** propose_contract, at HALF the claimed scope — the payload-arity leg is withdrawn as factually wrong and is the most instructive error in this audit. Every Key already carries a substrate-level targets[] array with per-target impact_vector and stat_deltas (key_substrate_v30.md:45-53, :86-95); that IS the 'one Key, N targets' distribute-down channel propagation_spec §D.1 defines and which the claim itself cites, and parliamentary_transfer.py:167-168 already populates scale_signature=['territory'], targets=[Target(...)] on the very key the lane said cannot fan out. Reading optional_payload_fields and concluding a key cannot distribute is pattern-matching on the payload table instead of the substrate concept. ALSO WITHDRAWN: 'both live' is false for mass_seizure, re-measured 2026-08-03 as 'UNREACHABLE. Zero production callers... and no owner write in 40 seeded campaigns'. WHAT SURVIVES: add a module_contracts.yaml row for parliamentary_transfer (or fold into faction_politics, whose sim_module is 'none' despite these files existing), and add the §D.4 down-seam entry. The doc's own resolver already flags the deeper question for Jordan.

**Evidence.** references/module_contracts.yaml — 27-row enumeration, neither name present; :889-921 (faction_politics sim_module: none, 'no dedicated code found'); systems/_architecture/propagation_spec_v1.md:239-250 (§D.4's eight rows, no faction→settlement_layer seam), :217-226 (§D.1 the distribute-down rule); systems/_architecture/key_substrate_v30.md:45-53 (targets[] read verbatim: actor_id, role, impact_vector, stat_deltas); systems/factions/sim/parliamentary_transfer.py:167-168, :130-135 (the mass_seizure unreachability record), :142-147 ('the alternative is a dedicated da.territorial_transfer type, which is a canon addition. Flagged for Jordan rather than settled here'), :278 and mass_seizure.py:295 (the direct accord writes); systems/factions/factions_flow_skeleton_v1.md:178.

**Existing tracking.** ED-IN-0096 (landed) measures and routes the CODE-level write-model divergence (Territory.accord vs Settlement.order) to the SE lane's OI-37/E5 per HANDOFF_SE.md:135-136, and accounting.py:33-35's docstring states reconciling the two write models 'is NOT this program's to resolve.' Neither it nor HANDOFF_SE's E5 names the missing contract row or §D.4 entry. The missing-replay-semantic half is self-flagged in the resolver's own docstring at :142-147, which the lane did not cite.

---

_Continues in [part 4](01_gap_register_part4.md)._
