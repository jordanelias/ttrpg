# World-Schema Gap Register — part 2 of 4 (G-15–G-29)

## Status: REFERENCE — observations against the tree. **Ratifies nothing.**

**Date:** 2026-08-11 · **Lane:** IN · **ED:** ED-IN-0153 · **Base:** `63d4d0c`

Method: [`00_orchestration_plan.md`](00_orchestration_plan.md) · Verdict, held decisions and what this run did NOT cover: [`02_verdict_and_residuals.md`](02_verdict_and_residuals.md)

_Continues [part 1](01_gap_register.md)._ 
> **Read `02_verdict_and_residuals.md` before acting on any row.** Three producer claims were
> **overturned** and are absent here; two proposals **would have caused damage if executed** and
> are flagged there rather than silently dropped. Every row survived a read-only `valoria-critic`
> pass that never saw the producer's reasoning.

## Rows (continued)

<a id="g-15"></a>

### G-15 · SCRIPTING DRIFT

**rung** `territory` · **kind** `missing_individuation_descriptor` · **disposition** `propose_authoring_field` · **independent lanes** 1

**Lenses.** `hardcoded singleton`, `individuation`, `religion`

**Claim.** SCRIPTING DRIFT. Territory.templar — a real, writable, persisted, consequential field seeding infrastructure.py's Axis-2 templar_station — is set for exactly one territory by a hardcoded named branch, templar=(tid == 'T9'), in create_world(). No other territory could ever start with the trait without a code change. The same function individuates two more per-territory values the same way: prosperity from an inline set literal {'T1','T2','T3','T8','T9','T14'} and fort_level from a module-level STARTING_GARRISON dict — while the geography YAML already authors per-province fort_level and starting_pros that create_world does not read.

**Proposal.** propose_authoring_field — add one narrow per-province boolean column to valoria_geography_v30.yaml's provinces block and read it in create_world, replacing the tid == 'T9' literal; and route prosperity/fort_level through the already-authored starting_pros/fort_level fields in the same file rather than inline literals. THE PRODUCER'S PROPOSAL IS REJECTED AND MUST NOT BE ACTED ON: it proposed deriving the templar seed from a threshold on spiritual_weight on the stated basis that T9's value of 4 is 'the highest of all 17 provinces'. That is false — I ran the full 17-province census and T15 Askeheim is 5 (valoria_geography_v30.yaml:209; T9's 4 is at :131, not :27 as cited). A threshold would site the templar station in Askeheim, which the same file describes as faction: Uncontrolled, settlements: [], 'Calamity epicenter. Forgetting zone.' A related range defect goes with it (G-48): settlement_generator_v1.md:45 declares spiritual_weight 0-2 and gates a Cathedral on >= 2, while the geography file authors 4 and 5 for two provinces.

**Evidence.** engine/autoload/game_state.py:150 (templar field), :229-231 (the three hardcoded individuation lines verified verbatim: prosperity set literal, fort_level from STARTING_GARRISON, templar=(tid == 'T9')), :288 and :359 (serialize/restore — real persisted state, not dead code), :212 (create_world takes only a seed); systems/settlements/sim/infrastructure.py:128-131,:166,:194-200,:210,:225,:247 (templar read repeatedly as the seed for a real Axis-2 mechanical effect); full spiritual_weight census of all 17 provinces run directly against the YAML (values 0-5; max 5 at :209).

**Existing tracking.** Partially: systems/settlements/settlements_flow_skeleton_v1.md:146 records the whole geography provinces block — naming spiritual_weight explicitly — as 'read by no production code anywhere'. settlements_flow_skeleton_v1.md:48 documents templar as a legitimate backward-compat seed without flagging the singleton branch. Four ledger hits on 'templar' across main/archive/mb/pc files; none discusses hardcoded-seed-vs-authored-data.

---

<a id="g-16"></a>

### G-16 · SCRIPTING DRIFT

**rung** `national_faction` · **kind** `missing_individuation_descriptor` · **disposition** `propose_contract` · **independent lanes** 1

**Lenses.** `hardcoded singleton`, `individuation`

**Claim.** SCRIPTING DRIFT. Every faction-unique mechanic in code is dispatched by hardcoded Python string comparison on the faction or territory-owner name — faction.name == 'Crown', faction.name == 'Church', t.owner == 'Church', initiator == 'Crown' — and three Church/Crown-specific booleans (excommunicated, council_used_this_arc, parl_transfer_used_this_arc) sit on EVERY Faction instance. Varfell and Hafenmark fall through to nothing because no branch names them.

**Proposal.** propose_contract — a ROUTING fix against a primitive that already exists, not a new field. THE PRODUCER'S CLAIM THAT NO SUCH FIELD EXISTS ANYWHERE IS OVERTURNED: registers/mechanics_index.yaml:939-966 declares 'categories: faction_unique_actions:' as exactly the faction → capability-id map the proposal asked to invent (Crown: [royal_progress, great_work, coronation_renewal, crown_treaty]; Church: [excommunication_action, absolution, council_solmund, mass_seizure, infrastructure_reclamation, home_sanctuary_t9]; Hafenmark: [charter_of_liberties, altonian_reinforcements, hafenmark_equipment]; Varfell: [varfell_mandate_action, varfell_territorial_acquisition]; plus universal: and emergent: buckets — verified verbatim), with per-mechanic 'faction:' bindings at :596/:610/:620. The lane grepped only module_contracts.yaml and descriptor_registry.yaml. WHAT SURVIVES AND IS FILED: route _faction_specific_unique's dispatch through that binding (a lookup keyed by capability id) instead of an if/elif chain on .name, and move the three per-faction booleans off the shared dataclass. The 'Varfell/Hafenmark have no unique action' sub-claim is also false — their resolvers exist (varfell_mandate_action.py, varfell_territorial_acquisition.py, charter_liberties.py, hafenmark_equipment.py) and are blocked on a tracked canon-authoring hold, not a missing id.

**Evidence.** systems/factions/sim/faction_action.py:277 (if faction.name == 'Crown':) and :293 (if faction.name == 'Church':) — both read directly and verified; :251,:313-316 (Varfell/Hafenmark fallthrough); systems/overview/sim/ci_track.py:91 and systems/factions/sim/mass_seizure.py:131 (if t.owner == 'Church':); systems/factions/sim/parliamentary_transfer.py:107 (initiator == "Crown" CB source); engine/autoload/game_state.py:116-122 (the three faction-specific booleans on every instance, read verbatim); registers/mechanics_index.yaml:939-966, :599,:606,:622 ('Pass 2d canon authoring pending faction contamination audit', Jordan 2026-05-17).

**Existing tracking.** TRACKED, contrary to the lane's 'none found': systems/factions/factions_flow_skeleton_v1.md:177 states it verbatim — '6 of 16 systems/factions/sim/ modules... are pure stubwire.stub_resolve armature stubs... Two whole faction identities (Varfell, Hafenmark) have zero faction-unique action in the live dispatch'. registers/placeholder_names.yaml:91 carries the authoring hold. ED-FA-0014 is an unrelated Regency fork and does not cover this.

---

<a id="g-17"></a>

### G-17 · BLOCKING PRECONDITION FOR EVERY propose_key ROW IN THIS REGISTER

**rung** `cross_rung` · **kind** `missing_authoring_schema` · **disposition** `needs_jordan_ruling` · **independent lanes** 1

**Lenses.** `governance`, `process`

**Claim.** BLOCKING PRECONDITION FOR EVERY propose_key ROW IN THIS REGISTER. key_type_registry_v30.md §10 carries a RATIFIED (Jordan, 2026-07-07, ED-IN-0026) precondition on the type-extension process: no new Key type may be appended without a corresponding row in references/rendering_dispositions.yaml recording a RENDERED-RICH / GENERIC / UNRENDERED / DELIBERATE-SILENT verdict. That file does not exist — references/ holds 19 yaml files and it is not among them. Not one of the thirteen-plus proposals that needed it mentioned the constraint.

**Proposal.** needs_jordan_ruling — who authors references/rendering_dispositions.yaml, and whether the existing 55-type backlog is dispositioned before or alongside new appends. PRECISION THE AUDIT'S OWN INSTRUMENT ENTRY GETS WRONG and this row corrects: ED-IN-0153 states the audit 'structurally cannot append them', which is stronger than the doc says — §10 :1287-1291 has A15 enforce the rule REPORT-ONLY against the existing roster first, and it 'flips to blocking new entries once rendering_dispositions.yaml exists and the backlog is at zero' (standard warn→block discipline). So appends are governed and unrecorded today, not mechanically refused. Every propose_key row here (G-01, G-04, G-08, G-26, G-27, G-28, G-29, G-40) must ship its rendering-disposition row as a co-artifact. A SECOND UNSTATED OBLIGATION rides along: engine/engine_params/key_types.json is GENERATED from this registry by tools/export_key_types.py, declares 'NEVER hand-edit', and pins 'Key order is REGISTRY order (ORD-1) and is significant — do not sort'; no proposal mentioned the export or the godot/skeleton/data/key_types/ mirror.

**Evidence.** systems/_architecture/key_type_registry_v30.md:1280-1291 read verbatim, including the report-only→blocking clause; directory listing of references/*.yaml (19 files; ls references/rendering_dispositions.yaml returns 'No such file or directory'); key_type_registry_v30.md:1273-1278 (the separate Class A supersession cost on payload edits, which governs G-07/G-08/G-19/G-31); engine/engine_params/key_types.json:2 (GENERATED banner, ORD-1 ordering constraint); references/module_contracts.yaml:1055 (the godot mirror).

**Existing tracking.** registers/editorial_ledger_in.jsonl:57 (ED-IN-0153, open) records it as measured fact 3 of this audit's own instrument entry — but no individual finding cited it, which is why it is elevated to its own register row. systems/_architecture/key_echo_armature_v1.md §3 (:173-191, RATIFIED) is the corpus's canonical route for proposing registry deltas and its 12-row candidate table contains no faction-lifecycle, caste, culture or ladder candidate; every propose_key row here additionally needs a §3-shaped row plus a PP-674 Class-B vetting block that none of the producers drafted.

---

<a id="g-18"></a>

### G-18 · EXECUTABLE DEFECT, PATTERN NOT ONE-OFF

**rung** `cross_rung` · **kind** `vocabulary_conflict` · **disposition** `propose_contract` · **independent lanes** 1

**Lenses.** `substrate integrity`, `runtime cross-check`

**Claim.** EXECUTABLE DEFECT, PATTERN NOT ONE-OFF. The registry parser recognises a flow list only when the raw value both starts with '[' and ends with ']'. Any entry whose flow list carries a trailing inline comment therefore fails that test and is stored as one raw string; apply_defaults() then does list(<that string>), producing a list of individual characters, every one of which fails invariant 7 and raises KeyValidationError. At least two type entries are broken this way, plus two more fields on a third — and the corrupted fields include emitting_systems/consuming_systems, which module_contracts.yaml's own header says its from: lists are auto-wired from. No guard exists anywhere.

**Proposal.** propose_contract — one owner, every site routed through it, and a guard that fails on recurrence (§0.1 point 5). Fix at engine/substrate/keys.py:294 by stripping a trailing '#' comment before the startswith/endswith test, NOT by editing individual registry prose lines: the producer's option (a) fixes one of at least three sites and leaves the recurrence path open. Ship the guard with it — a test that parses every registry entry and asserts each default_scale_signature is a list whose members are all in SCALES. Underneath the parse bug, meta.cascade_cluster_event's declared intent (a similarity-dependent scale) is something the static default_scale_signature field cannot express even when parsed cleanly, and 'territorial' is not a SCALES member regardless; that half is a separate design question, not a parser fix.

**Evidence.** engine/substrate/keys.py:294 read verbatim (elif value.startswith('[') and value.endswith(']')), :326 (key.scale_signature = list(entry['default_scale_signature'])), :414-418 (invariant 7), :65 (SCALES = personal/settlement/territory/peninsula — no 'territorial', no 'provincial'); key_type_registry_v30.md:1084 (meta.cascade_cluster_event: 'default_scale_signature: [territorial]  # peninsular when abs(similarity) > 0.95'), :383 read verbatim (mechanical.scene_entered: 'default_scale_signature: [personal, territory, peninsula]   # mirrors scope' — a Class B key with a real declared emitter 'emitting_systems: [game_director]' at :386, whose three scale values are ALL legal, so the trailing comment is the only thing breaking it), :1087-1088 (same defect on emitting_systems/consuming_systems); references/module_contracts.yaml:11-12 (from: lists auto-wired from those very fields); grep of tests/ for default_scale_signature/apply_defaults returns only the sidestep comment at tests/valoria/test_articulation_subscriber.py:85.

**Existing tracking.** Known only as a sidestepped test comment (test_articulation_subscriber.py:83-86, 'a pre-existing registry-prose defect this test sidesteps rather than silently depends on; out of OI-08's scope to fix'); ED-IN-0095 landed the surrounding subscriber wiring and explicitly did not fix it. Not a tracked ED item. The second and third instances were found adversarially, not by the producer.

---

<a id="g-19"></a>

### G-19 · meta

**rung** `character` · **kind** `vocabulary_conflict` · **disposition** `needs_jordan_ruling` · **independent lanes** 1

**Lenses.** `individuation`, `personal history`, `relation`

**Claim.** meta.knot_formed's authored payload carries a STRUCK enum. Its required tier field is declared 'Loose | Medium | Close' — the PP-632 3-tier point-cost model that knots_v30.md records as struck in favour of the Distant/Close strain model, with the supersession logged and ED-912 canonizing Distant/Close only. The defect has propagated into the generated code-facing export. Separately and additionally, the payload carries no relation_kind, so two Knots at the same tier are mechanically identical whether the partner is a mother or a criminal handler, and the 'secret' framing of a handler-Knot has no distinct treatment from an openly-known parent-Knot.

**Proposal.** needs_jordan_ruling — correcting the tier enum changes an existing type's required_payload_fields, which key_type_registry_v30.md:1273-1278 makes a CLASS A supersession event (supersession_register entry + migration rule for existing Keys + Class A patch entry). That is a heavier item than the optional relation_kind field the lane proposed, and it should be ruled before the additive field lands so both ship in one supersession rather than two. The additive half, when it lands, is optional_payload_field relation_kind (kin | mentor | patron | handler | rival | dependent | professional) on the existing type — no new family, no per-character special case. Recorded rather than proposed because the lane that read this entry silently substituted the correct canon vocabulary for the file's actual text, and the file's text is what the exporter reads.

**Evidence.** systems/_architecture/key_type_registry_v30.md:1014-1031 read verbatim: required_payload_fields are participants and 'tier                      # Loose | Medium | Close'; optional is formation_scene_id only; systems/fieldwork/knots_v30.md:58 read verbatim ('the PP-632 Loose/Medium/Close 3-tier point-cost model (1/2/5) is struck in favour of the Distant/Close strain model. Supersession logged in canon/supersession_register.yaml'), reaffirmed at :39,:51-52,:85,:91 (ED-912 canonizes Distant/Close only); engine/engine_params/key_types.json (GENERATED, type_count 55, inherits the struck enum); systems/characters/character_histories_v30.md:71,:136,:275,:362 (starting Knots where relation-kind is the load-bearing fact, incl. 'a handler within the Order... This Knot is itself a secret'); systems/fieldwork/knots_v30.md §2-§8 (every use-site branches on tier/strain/Disposition, never relation-kind).

**Existing tracking.** none — the struck-enum half is filed by no claim in this audit and was surfaced only by adversarial re-reading of the cited lines. The relation_kind half: ED-391 (cited in character_histories_v30_infill.md:121) is adjacent but distinct (whether the GM-side 'ghost sheet' of a lost Knot partner is a design-layer requirement).


⚠ **[CORRECTED 2026-08-11, second adversarial pass — ED-IN-0157]** The "none found" verdict is **OVERTURNED**: `registers/supersession_register.yaml:227-230` registers PP-632's Knot tier-cost model as superseded by **ED-912** (2026-06-28). This row's own Evidence field quotes `knots_v30.md:58` pointing at that register. **The sharpening is worth more than the overturn:** `supersession_register.yaml:238-240`'s `files_to_recheck` omits `key_type_registry_v30.md`, which is the nameable mechanism by which the struck enum survived and reached the generated `key_types.json`.
---

<a id="g-20"></a>

### G-20 · The canonical named-character roster EXISTS and is orphaned from both schema surfaces

**rung** `character` · **kind** `missing_authoring_schema` · **disposition** `propose_contract` · **independent lanes** 1

**Lenses.** `identity/actor substrate`, `individuation`

**Claim.** The canonical named-character roster EXISTS and is orphaned from both schema surfaces. references/npc_registry.yaml declares itself 'Canonical source of truth for ALL named characters' with an enforcement rule ('No character name may appear in design docs without an entry here') and an explicit schema block, and it is referenced ZERO times by references/module_contracts.yaml and ZERO times by key_type_registry_v30.md. No contract module owns character identity; all 27 treat npc_id/actor_id as an opaque foreign key into someone else's state.

**Proposal.** propose_contract — the actionable finding is the INVERSE of the producer's: do not author a new roster, bind the existing one. Add a character_identity module row whose state block declares the roster and the core fields every other module's payload already assumes (name/kind, current territory_id/settlement_id, current affiliation_faction), sourced to references/npc_registry.yaml, following the pattern every other rung already has (faction_state owns faction stats, settlement_layer owns settlement stats). The producer's 'there is no roster' is withdrawn: the roster is enforced, schema'd, and unreferenced — an orphaned authored surface, not a missing one. This is also where G-09's caste field and G-13's authored conviction vector belong, which is why binding it first is cheaper than three separate allocations.

**Evidence.** references/npc_registry.yaml:1-13 verified verbatim (canonical-source-of-truth header at :2, ENFORCEMENT line at :5, schema block at :11-13: required [id, first_name, last_name, faction, role, status]; optional [age, birthplace, territory, ts, coherence, stats, convictions, goals, arc_trajectory, notes]); grep -c 'npc_registry' against references/module_contracts.yaml and systems/_architecture/key_type_registry_v30.md returns 0 and 0 (run directly); references/module_contracts.yaml — 27 '- module:' rows, none named character/actor/identity/roster; systems/world/sim/npe.py:115-134 (NPC dataclass fields exist only in code, never mirrored as contract state).

**Existing tracking.** TRACKED — the producer's 'none found' is false and the tracking is this audit's own instrument entry: registers/editorial_ledger_in.jsonl:57 (ED-IN-0153, open) states as pre-measured fact (1) that 'no module_contracts.yaml row and no key_type_registry family OWNS character identity -- all 27 modules treat npc_id/actor_id as an opaque foreign key'. The orphaned-roster sharpening is new.

---

<a id="g-21"></a>

### G-21 · The Jordan-ratified B12 Territory tier (Settlement < Territory < Province < Duchy < Country) has no key type, no contrac

**rung** `territory` · **kind** `missing_scale_or_transition` · **disposition** `needs_jordan_ruling` · **independent lanes** 1

**Lenses.** `entity-ladder coherence`, `geography`

**Claim.** The Jordan-ratified B12 Territory tier (Settlement < Territory < Province < Duchy < Country) has no key type, no contract scale value, and no code distinguishing it from the pre-B12 flat unit. Every live schema and code surface uses 'territory' or 'province' for the SAME 17-unit T1-T17 entity that B12 itself now identifies as Province, with settlements as direct children and no intermediate tier. The measurement that pins it: 'provincial' appears 0 times in the entire key type registry, across all 55 entries.

**Proposal.** needs_jordan_ruling — the MEASUREMENT is upheld and independently reproduced; the PROPOSAL is rejected twice over. (1) It is barred: module_contracts.yaml:16-21 (OI-40a) states 'No vocabulary unification lands here or anywhere else until that fork resolves' (ED-IN-0103 §6 fork 1), and reassigning a scale token IS that unification. (2) It composes on the wrong surface: 'provincial' is not a substrate token at all — key_substrate_v30.md:57 and engine/substrate/keys.py:65 declare the authoritative enum as personal|settlement|territory|peninsula, and promoting a module_contracts-local word into substrate semantics is shape divergence, not composition. Keep the measurement; drop the proposal.

**Evidence.** systems/settlements/scale_hierarchy_v1.md:3 (RATIFIED), :9-24 (the B12 hierarchy), :156-167 (§6 item 1, PP-726 rewrite unexecuted); engine/autoload/game_state.py:35-40,:142-151 (T1..T17 keys, flat Territory class, no intermediate class); systems/settlements/valoria_geography_v30.yaml:18-30 ('provinces:' block with settlements listed directly under each T-code); systems/world/geography_v30.md:7-8,:58 (same 17 units called 'Territories', CANONICAL, approved 2026-04-05, pre-B12, never re-bannered); systems/factions/franchise_v30.md:32-49 (same T-codes, flat naming); grep of 'provincial' across the whole key type registry: ZERO hits of any kind (independently re-run); engine/substrate/keys.py:65.

**Existing tracking.** scale_hierarchy_v1.md's own §6 (RATIFIED but unexecuted; its header states 'No ED allocated yet for the propagation work this doc tracks'); ED-IN-0103 §6 fork 1 HELD per module_contracts.yaml:16-21; ED-IN-0062 (open, needs_jordan) as a broad docket citing the pre-rename path. This finding sharpens the held fork with the 0-of-55 measurement; it does not duplicate the fork's own enum-size/spelling triple.

---

<a id="g-22"></a>

### G-22 · scale_hierarchy_v1 §5

**rung** `cross_rung` · **kind** `missing_payload_field` · **disposition** `needs_jordan_ruling` · **independent lanes** 1

**Lenses.** `geopolitics`, `politics`, `entity-ladder coherence`

**Claim.** scale_hierarchy_v1 §5.1 ratifies local/provincial/national faction tiers as INDEPENDENT (not containment-nested; 'factions do not necessarily need to hold territory — they need to hold PEOPLE'), but faction_state declares scales: [provincial] as its only scale, and neither the Faction dataclass nor faction_state's state/consumes/emits blocks carry a tier field anywhere. A settlement-scale guild or a national-scale Löwenritter-style faction — both named as canon examples in the same section — cannot be expressed as an instance of the schema's one faction-behavior contract. Relatedly, the only faction-power state is Faction.territories; no field carries 'population held'.

**Proposal.** needs_jordan_ruling on the shape (field vs module), with a strong recommendation on the record: tier-as-field on the existing contract, NOT a module per tier — §5.1's own point is that tiers are the same kind of entity differing only in population held, so a per-tier module would be the special-casing the task warns against. Add tier (enum local | provincial | national) to faction_state's state block and to the Faction dataclass, plus a population_held derived_value per §5.1's people-not-territory primitive. SPLIT REQUIRED: the second half of the lane proposal widens the scales: enum itself, which is frozen behind ED-IN-0103 fork 1 (G-21, G-43) — the tier field can and should land independently rather than be blocked behind a held ruling.

**Evidence.** systems/settlements/scale_hierarchy_v1.md:79-93 (§5.1 verbatim, with local examples 'guilds, independence protests, militia' and national examples 'the Restoration Movement, Löwenritter'), :156-165 (§6 propagation, 'tracked, not yet executed'), :175-178 (§6 item 3, the F-series tier-field follow-on); references/module_contracts.yaml:71 (scales: [provincial], sole value), :101-110 (tier-free state block); engine/autoload/game_state.py:94-122 (class Faction — name, parliamentary, L/Sta/W/I/Mil, intel, territories, standing at :114, five seasonal/arc flags; no tier), :35-40,:51-56 (four static instances, no mechanism to instantiate a provincial or local faction); grep of 'tier' across faction_behavior_v30.md and descriptor_registry.yaml: zero faction-tier hits.

**Existing tracking.** scale_hierarchy_v1.md's own §6 item 3 is the precise pointer ('generation_sourcebook_v1.md's F-series... needs an explicit local/provincial/national tier field per generated faction... plus a people-held-not-territory-held power computation') — tracked as unauthored follow-on with no ED of its own. ED-IN-0062 names the area generally. ED-IN-0153 measured fact 2 names the ladder the schema cannot express.

---

<a id="g-23"></a>

### G-23 · The NPC-NPC Relational Graph (PP-724) is a Class A canonical substrate defining six typed edges — sworn-bond, liege-vass

**rung** `character` · **kind** `missing_owned_state` · **disposition** `propose_contract` · **independent lanes** 1

**Lenses.** `politics`, `relation`, `personal history`

**Claim.** The NPC-NPC Relational Graph (PP-724) is a Class A canonical substrate defining six typed edges — sworn-bond, liege-vassal, kinship, patronage, rivalry, feud — with per-edge {type, direction, strength}, formation conditions, strain accumulation, capacity, break/rupture rules and cross-generational transmission, explicitly authored because 'existing canon assumed but did not define' this state. It carries a direct character-to-faction effect (a liege takes Mandate damage proportional to a vassal's faction position; armed defection generates Casus Belli). Neither schema surface has any trace of it, its own declared edge-storage file was never created, and grep finds zero implementations.

**Proposal.** propose_contract — compose on the doc's OWN declared data home before adding anything: author canon/relational_edges_v30.yaml, which §5 declares and the doc's own open items list as not-yet-created, then add an npc_relational_graph module row (scales: [personal]) pointing at it with a relational-edges state row. Key types (state.relational_edge_formed / _broken) are deferred behind G-17. THIS ROW IS LOAD-BEARING FOR FOUR OTHERS: it is the corpus's existing answer to 'where do per-counterparty relations live', and G-24, G-06, G-07 and the organizational_hierarchy half of G-02 should all compose on it rather than each inventing a shape. One lane's claim that NPC.supervisor_id is 'the sole NPC-NPC relational field anywhere in canon' is withdrawn — kinship, patronage and rivalry are canonized here. One lane's 'the built defection-cascade mechanic (ED-1000/1001)' is also qualified: §7's 'BUILT' means design-written, not implemented.

**Evidence.** systems/npcs/npc_relational_graph_v30.md:1-2 (Class A, PROVISIONAL, PP-724), :12, :24 (affects npc_behavior, faction_politics, settlement_layer §6.2, mass_battle), :46-64 (§2, six edge types with per-edge record {type, direction, strength: 1..3}), :121-160 (§3 strain/capacity/break lifecycle, modelled on the F2 Knot template, ED-773), :233 (liege Mandate damage), :246 (Casus Belli on armed defection), :535 and :661 ('canon/relational_edges_v30.yaml not yet created; will be authored at B2 instantiation'); references/module_contracts.yaml — no relational_graph row among 27; grep of key_type_registry_v30.md for sworn_bond/relational_edge/liege/kinship/patronage: zero.

**Existing tracking.** ED-SC-0030 (2026-08-08, open, needs_jordan) names PP-724 as 'PROVISIONAL with ZERO code' among nine forks held for Jordan, from the social-contest lane's angle (minimum edge subset for panel churn) rather than the schema-row angle. audit/2026-08-08-world-churn-audit/00_findings.md:205-208 (ED-IN-0149) already records the doc-only status and the missing yaml with the same grep.

---

<a id="g-24"></a>

### G-24 · The state[] bucket taxonomy (pool / derived_value / track / clock) is defined only for single-owner scalar quantities an

**rung** `cross_rung` · **kind** `missing_authoring_schema` · **disposition** `needs_jordan_ruling` · **independent lanes** 1

**Lenses.** `substrate design`, `diplomacy`, `relation`

**Claim.** The state[] bucket taxonomy (pool / derived_value / track / clock) is defined only for single-owner scalar quantities and has no shape for a per-counterparty relation or for a continuously-updated meter. Every relational primitive this audit found — treaty, Casus Belli, NPC relational edges, settlement subnational footholds — is real state stored as a dict or list precisely because no bucket can hold it; and separately, six of this register's findings are VECTOR-shaped quantities that a Key is explicitly 'not built to be'.

**Proposal.** needs_jordan_ruling — and the lane's proposal is rejected on three counts. (1) Wrong owner: it proposed editing skills/valoria-module-adjudicator/SKILL.md:57, but that line's own grounding column cites derived_stats §1/§11/§14 — the taxonomy belongs to systems/_architecture/derived_stats_v30.md, and editing the skill instead of the owner is the §8 'never re-implement a rule' violation. (2) The 'abuse' is already the standing convention, so it is not a blocker: module_contracts.yaml:197-198 files npc_behavior's per-subject keyed collections as bucket: track. (3) A canonical relational record already exists (G-23) and a general Field/Gauge primitive is already sketched — minting a 'ledger' bucket beside them is dialect growth, and it collides with the settlement Ledger-of-Consequence. The real call for Jordan is whether governance_type_registry_v1 §4.2's Field/Gauge primitive lands: filing six per-quantity state rows before that fork resolves risks six divergent shapes for one primitive.

**Evidence.** skills/valoria-module-adjudicator/SKILL.md:57 (the four-value taxonomy and its derived_stats grounding); bucket census run over all of references/module_contracts.yaml returns exactly {clock:14, derived_value:7, pool:2, track:17} — no fifth value anywhere; systems/_architecture/key_substrate_v30.md contains no relation/dyad/counterparty/ledger concept; engine/autoload/game_state.py:187 (World.treaties dict), systems/factions/sim/parliamentary_transfer.py:22-23 (duck-typed casus_belli), systems/settlements/sim/registry.py:85 (subnational dict) — three real relational stores with no contract home; systems/_architecture/governance_type_registry_v1.md:43-50 ('a Key is not built to *be* a continuously-updated meter') and :248-271 (§4.2 field_id schema sketch); systems/settlements/sim/ledger.py + governance_type_registry_v1.md:115 (the colliding Ledger concept).

**Existing tracking.** governance_type_registry_v1.md §4.1/§4.2 (PROPOSED, no ED allocated, referenced in CURRENT.md:94 and :157) is the general tracking and is the shared root cause of G-03, G-05, G-13, G-23, G-25 and the derived half of G-02. No ledger entry names the bucket taxonomy itself (grep for 'bucket taxonomy' and 'ledger bucket': zero hits).

---

<a id="g-25"></a>

### G-25 · Church Attention Pool (0-10 per-territory accumulator gating Inquisitor spawn and Heresy Investigation Ob) is written by

**rung** `territory` · **kind** `missing_owned_state` · **disposition** `propose_contract` · **independent lanes** 1

**Lenses.** `religion`, `society`

**Claim.** Church Attention Pool (0-10 per-territory accumulator gating Inquisitor spawn and Heresy Investigation Ob) is written by at least 10 distinct canon triggers across 7+ subsystem docs and read by two gating mechanisms, with no owned-state row anywhere. SHARPENED: it is not the one orphan on its table. Its actual table-siblings in the per-territory tracks block — Guild Favour (0-7) and legacy territory Prosperity (1-7) — also have zero contract rows. The finding is that the per-territory track table is largely unowned, not that AP is uniquely so.

**Proposal.** propose_contract — one state row per unowned per-territory track on the territory-scale owner (ci_political or territorial_piety, both of which already own Church-clock state), filed as one table-wide sweep rather than three separate items. A state.church_attention_change key type (territory_id, delta, cause) reused across all 10 emitting sites — one key family, not one per emitting subsystem — is deferred behind G-17 and behind G-24, since AP is a VECTOR ('No decay — pure accumulator') and is exactly the class the Field/Gauge fork governs. TWO CORRECTIONS: AP is not listed alongside CI/IP/Turmoil/MS — those are the 'Shared Clocks (All Modes)' table at :12-19; AP is in the separate per-territory block at :55-64. SEAM recorded, not resolved: conviction_track_v30.md:511 claims AP is 'now tracked per settlement... not per province', contradicting the per-territory framing in three other registries — an unreconciled scale conflict distinct from the held ED-IN-0103 fork.

**Evidence.** systems/overview/clock_registry_v30.md:12-19 (Shared Clocks), :62 (legacy Prosperity 1-7), :63 (Guild Favour 0-7), :64 (AP); systems/_architecture/governance_type_registry_v1.md:151 ('Church Attention Pool | Territory | VECTOR (0-10)... No decay'), :113/:162 (the legacy-Prosperity same-name/different-range collision); systems/_architecture/canonical_registry.md:101-104; ten trigger sites incl. systems/fieldwork/fieldwork_v30.md:615-655, systems/threadwork/threadwork_v30.md:769,:771, systems/npcs/npc_behavior_v30.md:297, systems/factions/faction_politics_v30.md:329,:852,:1096, systems/combat/combat_reference_v1.md:671; zero hits for 'attention' or 'Guild Favour' in module_contracts.yaml or key_type_registry_v30.md; systems/settlements/goldenfurt_slice/verification_findings.md:16 (sim-F3, 'load-bearing... but modeled nowhere', patched only inside one narrative fixture).

**Existing tracking.** Partially: governance_type_registry_v1.md:151 already inventories AP as an unowned VECTOR in the §2.7 cross-cutting-clock gap table the claim itself cites. Zero ledger hits for 'Church Attention' across all lane + archive files. ED-IN-0062 names 'heresy/cultural-suppression threads' plausibly covering the area without naming AP or this absence.


⚠ **[SOFTENED 2026-08-11, ED-IN-0157]** `tools/observability/INCOMPLETENESS.md:336` carries *"Church Attention Pool — in 19 docs, unregistered (IN)"* — same file and format as the `Casus Belli` entry at `:334` that this audit **did** harvest into G-06. The file was read and one entry taken, not the other.
---

<a id="g-26"></a>

### G-26 · Canon requires a territory-scale state transition — a territory at Accord 0 becomes Uncontrolled at Accounting, with Tur

**rung** `territory` · **kind** `missing_key_type` · **disposition** `propose_key` · **independent lanes** 1

**Lenses.** `churn`, `events`, `governance`

**Claim.** Canon requires a territory-scale state transition — a territory at Accord 0 becomes Uncontrolled at Accounting, with Turmoil +1 — that no key type can carry. Only the settlement-scale analogue (state.settlement_revolt, fired on Order reaching 0) was ever declared.

**Proposal.** propose_key — type_id state.territory_revolt, family state_transition; required_payload_fields: territory_id, prior_controlling_faction_id, turmoil_delta; default_scale_signature: [territory]; emitting_systems: [peninsular_strain]; consuming_systems: [] held DECLARE-ONLY pending the emitting module's build, which is the same disposition already used for its settlement-scale sibling under ED-IN-0096. This adds only the missing announcement channel and deliberately does not touch the separate code-level question of whether Territory.owner is ever set to None — that is ED-IN-0149's D1, a code fix, correctly refused by the producer. BLOCKED on G-17. Minor citation correction: the step is 4c, not 4d (4d begins at :486).

**Evidence.** systems/overview/peninsular_strain_v30.md:60 (Accord table, Revolt row: 'Territory becomes Uncontrolled at Accounting'), :483 (Step 4c: 'Each territory at Accord 0: Revolt fires... Territory becomes Uncontrolled. Turmoil +1'); exhaustive grep of key_type_registry_v30.md for revolt/Uncontrolled across all 1295 lines finds only state.settlement_revolt at :726-757 (settlement-scale, 'Order reaches 0'); engine/autoload/game_state.py:144 (Territory.owner single-value field); key_type_registry_v30.md:751-756 (the ED-IN-0096 declare-only precedent).

**Existing tracking.** audit/2026-08-08-world-churn-audit/00_findings.md D1 (ED-IN-0149) tracks the CODE consequence — no path anywhere sets Territory.owner = None. The schema-level absence of a key type for the transition is separately untracked; grep of all ledger files for 'territory revolt' and 'uncontrolled' with 'accord 0' finds nothing.

---

<a id="g-27"></a>

### G-27 · A province's conditional/emergent existence — formed only while its constituent territories share a common faction holde

**rung** `territory` · **kind** `missing_edge` · **disposition** `propose_key` · **independent lanes** 1

**Lenses.** `governance`, `entity-ladder coherence`, `churn`

**Claim.** A province's conditional/emergent existence — formed only while its constituent territories share a common faction holder, dissolving the instant that stops holding and re-forming when it resumes — has no key type at all, so victory's PV scoring, franchise recalculation, articulation and faction_state silently re-derive it every Accounting with no record that a province came into or went out of existence.

**Proposal.** propose_key — type_id mechanical.province_coherence_changed, family mechanical_event (composing on mechanical.era_transition / mechanical.theocracy_unification_declared, the nearest one-shot world-boundary precedents); required_payload_fields: territory_ids, faction_id, transition (formed | dissolved); default_scale_signature: [territory, peninsula]. MUST be filed DECLARE-ONLY with consuming_systems: [] and that disposition stated explicitly — unlike the sibling proposals, this one has to reckon with the fact that references/KEY_INDEX.md:24-35 already lists 8 consumer-less types including BOTH precedents it composes on, so a ninth belongs under the same ED-IN-0096 discipline rather than naming speculative consumers. BLOCKED on G-17.

**Evidence.** systems/settlements/scale_hierarchy_v1.md:26-39 (§2: 'When that condition stops holding, the province simply stops existing as a unit... when it starts holding again... the province re-forms'); exhaustive grep of key_type_registry_v30.md across all ~55 type_id entries for province form/dissolv/emerg/conditional aggregation: zero matches; references/module_contracts.yaml:832-852 (victory's gates read MS/IP/CI/Turmoil/Mandate/faction-dissolution, no province-coherence signal); references/KEY_INDEX.md:24-35 (the 8 consumer-less types); systems/factions/franchise_v30.md §4.2 (National Influence recalculation fires 'at Accounting, after territory control changes' — the silent re-derivation).

**Existing tracking.** The defect CLASS is filed on the same module the finding inspects: module_contracts.yaml:854 records 'world-state era transitions... are UNKEYED — no mechanical_event/state_transition type exists; articulation is blind to era changes via the Key stream [registry §10 candidate]'. Grep of all lanes + archives for 'province' with 'conditional'/'emergent'/'dissolv': zero hits. ED-IN-0062 is broadly adjacent but does not name province-formation events.

---

<a id="g-28"></a>

### G-28 · Conviction resolution (Fulfilled/Failed/Transformed/Unresolved) is the game's central player-progression mechanic, expli

**rung** `character` · **kind** `missing_key_type` · **disposition** `propose_key` · **independent lanes** 1

**Lenses.** `goals and ambitions`, `individuation`, `provenance integrity`

**Claim.** Conviction resolution (Fulfilled/Failed/Transformed/Unresolved) is the game's central player-progression mechanic, explicitly triggering a Truth shift, an NPC arc trigger, Domain Echo eligibility and Portrait recording — and no key type carries it. SHARPENED: the canon doc self-cites ED-686 for this exact mechanic, and ED-686 is a resolved archive entry about unrelated Co-Movement card calibration, flagged ID-CONFLICT, with the conviction-resolution description surviving only in a _migration_alt field. So a CANONICAL doc carries a citation that the anti-fabrication gate passes (the ID exists) while it resolves to unrelated closed content — a live instance of the leak CLAUDE.md §0 names.

**Proposal.** propose_key — type_id state.conviction_resolved, family state_transition (§5, alongside state.belief_revised which already exists for the adjacent Belief mechanic); required_payload_fields: npc_id, conviction_id, resolution_state (fulfilled | failed | transformed | unresolved), sufficient_scope (bool, per the doc's own >=2-scene-action gate); default_scale_signature: [personal]; emitting_systems: [piety_track]; consuming_systems: [] DECLARE-ONLY. BLOCKED on G-17. The ED-686 citation defect should be filed SEPARATELY as an IN-lane provenance item — it is not a schema gap and should not be bundled into the schema fix, but it is the more generalizable finding of the two.

**Evidence.** systems/_architecture/player_agency_v30.md:89 (Fulfillment triggers 'Truth shift, NPC arc trigger, or Domain Echo'), :95-98 (the 4-row resolution-state table with distinct Momentum/Truth/Portrait consequences), :100-106 (Sufficient Scope gate + Portrait Retirement + Draft Portrait), :106 (the [EDITORIAL: ED-686] tag); grep for conviction_resolved / conviction.*resolv across key_type_registry_v30.md and module_contracts.yaml: zero in both; registers/editorial_ledger_archive.jsonl:403 (ED-686 status resolved, description 'ED-577-01/02/03/04: Co-Movement card calibration', _migration_flag 'ID-CONFLICT: multiple distinct descriptions — Jordan resolve', conviction-resolution text only in _migration_alt).

**Existing tracking.** The doc's own ED-686 self-citation is unresolvable as tracking, per the evidence above — it is a broken pointer, not a closed item. No other ledger entry covers the schema gap.

---

<a id="g-29"></a>

### G-29 · The canonical Key-sequencing spec for npc_behavior specifies that Procedure C's completion and failure branches each cal

**rung** `character` · **kind** `missing_key_type` · **disposition** `propose_key` · **independent lanes** 1

**Lenses.** `goals and ambitions`, `events`

**Claim.** The canonical Key-sequencing spec for npc_behavior specifies that Procedure C's completion and failure branches each call generate_new_project / generate_replacement_project to give the NPC a new forward-looking commitment, but no key type exists for project or ambition FORMATION. Only the three downstream states are registered (project_advanced, project_completed, project_failed), so the moment an NPC forms a new goal is generated in-process and announced to nothing.

**Proposal.** propose_key — type_id state.project_formed, family state_transition (§5, parallel to state.project_completed/state.project_failed); required_payload_fields: npc_id, project_id, project_domain, goal_short; optional_payload_fields: prior_project_id, formation_cause; default_scale_signature: [personal]; emitting_systems: [npc_behavior]; consuming_systems: [npc_memory, articulation] — filed DECLARE-ONLY unless those subscriptions are live, per ED-IN-0096. BLOCKED on G-17. ADJACENT STALE-MARKER DEFECT found while verifying and worth filing with it: module_contracts.yaml's canonical accounting_sequence at :1092-1096 still annotates all three existing project types plus scene.displacement as '[unreg]', while npc_behavior's own gap_notes at :218/:220 record that ED-935 registered them on 2026-06-14 — the 2026-07-29 sweep fixed the module rows and missed the accounting block, leaving the file contradicting itself about ED-935.

**Evidence.** systems/factions/political_dynamics_keys_migration_v30.md:216 (generate_replacement_project on stall-failure, no emission shown), :256 (generate_new_project on completion, no emission shown), :175-235 (§4 Procedure C full pseudocode); key_type_registry_v30.md:446 (mechanical.project_advanced), :691 (state.project_completed), :710 (state.project_failed) — no formation type among the 55; references/module_contracts.yaml:172-176,:189-191 (the three self-loop edges, no formation counterpart); tree-wide grep for the two generator function names returns only the doc lines plus generated echoes (systems/factions/_identifier_census.yaml:1497-1510, glossary) — no implementation anywhere.

**Existing tracking.** ED-1006 (2026-06-10) flagged 'npc Procedure C projects' among 4 unkeyed CANONICAL/DESIGN systems needing registry SS10 extensions; ED-1007 (struck, superseded by ED-935) enumerated the four types by name and project FORMATION was never among them, so ED-935's 2026-06-14 registration closed advance/complete/fail and never covered formation. The residual is real, not unclosed paperwork on an already-tracked item.

---

_Continues in [part 3](01_gap_register_part3.md)._
