# World-Schema Gap Register — part 4 of 4 (G-46–G-50)

## Status: REFERENCE — observations against the tree. **Ratifies nothing.**

**Date:** 2026-08-11 · **Lane:** IN · **ED:** ED-IN-0153 · **Base:** `63d4d0c`

Method: [`00_orchestration_plan.md`](00_orchestration_plan.md) · Verdict, held decisions and what this run did NOT cover: [`02_verdict_and_residuals.md`](02_verdict_and_residuals.md)

_Continues [part 3](01_gap_register_part3.md)._ 
> **Read `02_verdict_and_residuals.md` before acting on any row.** Three producer claims were
> **overturned** and are absent here; two proposals **would have caused damage if executed** and
> are flagged there rather than silently dropped. Every row survived a read-only `valoria-critic`
> pass that never saw the producer's reasoning.

## Rows (continued)

<a id="g-46"></a>

### G-46 · settlement_layer §1

**rung** `cross_rung` · **kind** `missing_scale_or_transition` · **disposition** `propose_contract` · **independent lanes** 1

**Lenses.** `governance`, `politics`

**Claim.** settlement_layer §1.8b cites state.succession by name and specifies its effect at settlement granularity (succession_mode determining L unchanged / +1 / -1 in ALL held settlements), but the key's schema has no settlement_id and its default_scale_signature is [territory, peninsula], omitting settlement — so no settlement-scale consumer has a declared right to subscribe.

**Proposal.** propose_contract, re-filed against the RATIFICATION rather than the registry — 'Canon requires' overstates by exactly one status line: settlement_layer_v30.md:234 reads '(PROPOSED — ED-SE-0012, 2026-07-08)' and :236 '**Status: PROPOSED, not yet ratified.**', and an unratified subsection cannot make the registry wrong today. Per CLAUDE.md §2's ratification rule, whoever ratifies ED-SE-0012 must carry the scale_signature widening (adding 'settlement' to state.succession's default) in the same merge, or ratify a §1.8b no consumer can subscribe to. Adding a scale value to an existing default is not a payload change and so is not Class A; the optional affected_settlement_ids field the lane offered as an alternative WOULD be, and is the more expensive fallback. File against ED-SE-0012, not against the registry.

**Evidence.** systems/settlements/settlement_layer_v30.md:234-236 (the PROPOSED banner, read directly), :255-259 (the fan-out table naming the Key and its succession_mode field); systems/_architecture/key_type_registry_v30.md:670-689 (required faction_id/prior_leader_id/new_leader_id/succession_mode; default_scale_signature [territory, peninsula]); references/module_contracts.yaml:900-908 (faction_politics emits it at scales: [provincial] only, so the emitting side never touches settlement scale either).

**Existing tracking.** ED-SE-0012 authored §1.8b and states the RULE the key must satisfy without flagging that the key's own schema cannot carry it. The ratification-time obligation is the tracking hook; no separate ledger row found.

---

<a id="g-47"></a>

### G-47 · Of the 9 A6-violating module pairs in CONTRACT_INDEX, 8 are covered by scale_transitions §12

**rung** `cross_rung` · **kind** `missing_edge` · **disposition** `needs_jordan_ruling` · **independent lanes** 1

**Lenses.** `cross-scale spine`

**Claim.** Of the 9 A6-violating module pairs in CONTRACT_INDEX, 8 are covered by scale_transitions §12.4's own enumerated down-seam list. The 9th — piety_track receiving scene.dialogue/insult/threat/witness from scene_slate — is in neither that list nor among the eight named handoffs in §3, whose only Personal/Scene entry runs the other direction.

**Proposal.** needs_jordan_ruling, low priority — and the producer's own hedge is the likely resolution: scene_slate is scales:[scene] and piety_track is scales:[personal], and 'scene' is no more a member of the runtime SCALES than 'provincial' is, so this pair may dissolve entirely under ED-IN-0103 fork 1 rather than needing a new handoff. Recorded, not resolved, per the instruction on the held vocabulary fork. The arithmetic independently corroborates the classification: the 8 §12.4 pairs cover 16 of the 20 A6 rows, and §12.4's own count is 'fifteen type-edges' — exactly 16 minus scene.draft_da, which module_contracts.yaml:613 marks 'NOT in registry (F2 class)' and which is therefore not registry-canonical.

**Evidence.** references/CONTRACT_INDEX.md:23 (9 pairs), :27-46 (the 20 A6 rows, incl. the 4 piety_track←scene_slate rows at :38-41); systems/_architecture/scale_transitions_v30.md:341 (§12.4's enumerated list, verified to exclude this pair), :40-81 (§3's eight handoff headings — §3.3 is 'Personal → Scene' only, no reverse entry), :28-36 (§1 Three-Mode/scale table, the basis for treating personal/scene as possibly same-tier); references/module_contracts.yaml:439 (scene_slate scales:[scene]), :262 (piety_track scales:[personal]), :613.

**Existing tracking.** ED-1038 / §12 covers the other 8 pairs explicitly and adequately. None found for this 9th pair.

---

<a id="g-48"></a>

### G-48 · The per-territory 'P1 Location' authoring inputs the settlement generator names as the intended individuation source for

**rung** `territory` · **kind** `missing_individuation_descriptor` · **disposition** `propose_authoring_field` · **independent lanes** 1

**Lenses.** `individuation`, `flavour with no hook`, `geography`

**Claim.** The per-territory 'P1 Location' authoring inputs the settlement generator names as the intended individuation source for a settlement's religious character, wealth and calamity exposure — spiritual_weight, proximity_calamity, starting_pros, plus province-level fort_level, region and sub — are authored for all 17 provinces and have zero descriptor KIND, zero contract state row and zero code reader anywhere. Provinces differ in the authored data (proximity_calamity 0 vs 1 vs 5) and are identical in play.

**Proposal.** propose_authoring_field — do not invent a parallel mechanism: these are exactly the fields the settlement generator's own P1/P5/P8 paradigm table designates as generation inputs, so the fix is landing that spec, or at minimum registering them as territory_stats descriptors (the terr.fort_level precedent already exists as that section's only entry) plus a state row wherever they land. Do not special-case any one field. A RANGE DEFECT must be fixed in the same pass and is the same one that breaks G-15's rejected proposal: settlement_generator_v1.md:45 declares spiritual_weight 0-2 and :66 gates a Cathedral on >= 2, while the geography file authors 4 for T9 (:131) and 5 for T15 (:209) — 2 of 17 provinces outside the spec's declared range, uncaught by any surface.

**Evidence.** systems/settlements/valoria_geography_v30.yaml — per-province spiritual_weight/proximity_calamity/starting_pros for all 17 (full spiritual_weight census run: values 0-5, max 5 at :209, T9's 4 at :131); T15 proximity_calamity 0 at :210, T6 1 at :93, T3 5 at :54; comprehensive grep across systems/, engine/, tools/ for the three field names returns zero non-YAML, non-prose hits; references/descriptor_registry.yaml:84-87 (territory_stats has exactly one entry, terr.fort_level); systems/settlements/settlement_generator_v1.md:45 (the P1 row and its 0-2 range), :66 (Cathedral gate).

**Existing tracking.** TRACKED, contrary to the lane's 'none found', on the settlements subsystem's own §7 traced-gap list: systems/settlements/settlements_flow_skeleton_v1.md:146 states 'The geography YAML's top-level provinces: block (per-province fort_level, starting_pros, spiritual_weight, proximity_calamity, polygon, anchor, settlements: list, description) is read by no production code anywhere', with the same evidence anchors. VSG itself (settlement_generator_v1.md) is PROPOSED with no ED allocated. The range defect is new.

---

<a id="g-49"></a>

### G-49 · institutional_culture is authored as the one scalar meant to individuate a faction's Cascade behaviour via the α_institu

**rung** `national_faction` · **kind** `missing_individuation_descriptor` · **disposition** `propose_descriptor` · **independent lanes** 2

**Lenses.** `individuation`, `hook with no variation`, `society`

**Claim.** institutional_culture is authored as the one scalar meant to individuate a faction's Cascade behaviour via the α_institution term, and it is read by zero lines of Python anywhere in the tree. On paper the spread is thinner than one lane reported: six canonical factions collapse to four distinct values with -0.1 authored THREE times, so half the roster is behaviourally identical on the axis meant to distinguish them.

**Proposal.** propose_descriptor — the state-row half is G-02; what this row adds is that when the Cascade α formula is implemented, α_institution must be sourced from that row rather than the doc's inline per-faction comment table, so the value is data a resolver reads rather than a docstring humans keep in sync. SEVERITY REDUCED for a reason worth stating: 'no system reads it' is not a property of this scalar — nothing in the cascade subsystem is implemented at all (module_contracts.yaml:66-70; factions_flow_skeleton_v1.md:175 measures cascade_resolution as having zero implementation hits in systems/ or engine/, its only tree occurrence being its own declaration in the key-types export). The FLAVOUR-WITH-NO-HOOK label therefore applies to the whole resolver, not to this field. The framing is also narrower than 'no authoring home exists': systems/factions/faction_state_authoring_v30.md IS that home and is 'STATUS: PROVISIONAL — Class A authoring document', so the accurate gap is 'a PROVISIONAL Class A authoring doc has no ratified contract row' — a ratification action, not a schema-invention action.

**Evidence.** systems/factions/faction_behavior_v30.md:56 (the '# Authored' declaration), :152-160 (α formula + per-faction table: Hafenmark -0.2, Crown 0, Restoration +0.1, Löwenritter -0.1); systems/factions/faction_state_authoring_v30.md:2 (STATUS: PROVISIONAL — Class A authoring document), :18, and the six per-faction instantiations at :59 (0.0), :112 (-0.1), :158 (-0.2), :209 (-0.1), :258 (+0.1), :316 (-0.1) — three instances of -0.1, spanning 4 of the 5 quantised steps in [-0.2, +0.2]; grep -rn institutional_culture --include=*.py across the tree returns zero hits; references/module_contracts.yaml:66-70, :107-110.

**Existing tracking.** TRACKED, contrary to 'none found': audit/2026-07-13-multi-agent-audit/_workings_joined.md:978 lists institutional_culture under 'Defined-but-never-referenced (orphaned) mechanics' and :1015 records it as a single-consumer narrow chain. The lane grepped only registers/editorial_ledger*.jsonl; this corpus also files findings in surviving audit units. references/glossary/GLOSSARY_factions.md:256 flags the term as UNRESOLVED — a glossary-definition gap, a different claim.


⚠ **[CORRECTED 2026-08-11, ED-IN-0157]** The citation to `audit/2026-07-13-multi-agent-audit/_workings_joined.md:978` is **reversed**: read in full, that line says `institutional_culture` *"is narrow (single-consumer: feeds only α_institution) **but is consumed, not orphaned**"* — it sits under the orphaned-mechanics heading in order to EXCLUDE the field. ⚠ The disagreement **sharpens this row**: that audit's "consumed" is design-level (it feeds α_institution in the formula) while this session measured **zero Python readers**. Design-consumed and code-unread is precisely this row's subject.
---

<a id="g-50"></a>

### G-50 · NPC residence is recorded at two different grains — NPC

**rung** `cross_rung` · **kind** `missing_edge` · **disposition** `not_a_gap` · **independent lanes** 1

**Lenses.** `demographics`, `geography`

**Claim.** NPC residence is recorded at two different grains — NPC.territory_id (province) and Settlement.npc_ids (settlement) — with no bridge, and generate_npc never writes to any Settlement's npc_ids.

**Proposal.** not_a_gap as stated; the asymmetry the claim rests on does not exist, and the correct residual is already filed elsewhere. 'production-populated by generate_npc' is false: systems/world/world_flow_skeleton_v1.md:179 records that generate_npc 'is fully implemented but has no call site anywhere in production code (world-gen or season-tick)', that engine/mc_v18.py:186-194 records the absence via a named stubwire.stub_resolve call rather than invoking it, and that the acceptance test is xfail(strict=True) confirming npc_counter stays at 0 for a full seeded campaign. Neither residence field is populated, so there is no live sibling to be out of sync with. The lane checked characters_ and settlements_flow_skeleton but npe.py lives under systems/world/, and world_flow_skeleton §7 is where this whole area is tracked. Of the lane's own two branches, (b) — retire Settlement.npc_ids as dead schema — is the better and cheaper one, and it is the same dead-field class as G-36.

**Evidence.** systems/world/sim/npe.py:118 (NPC.territory_id), :313 and :320-321 (the sole store write, keyed by territory_id); systems/settlements/sim/registry.py:86 (Settlement.npc_ids, no production write); systems/world/world_flow_skeleton_v1.md:179; grep of 'world.settlements' against npe.py: zero hits; the only production-shaped npc_ids write is tools/sim_harness/adapters/pr119_governance/goldenfurt_fixture.py:89, a prototype fixture not wired to CI.

**Existing tracking.** systems/world/world_flow_skeleton_v1.md:173-186 §7 — gap 3 at :179 (generate_npc unreached in production, xfail-pinned), :182 (npe.py's three-way homing split), :183 (module_contracts registers only miraculous_event of this subsystem's four sim modules), :185 (the coverage/execution inversion). An entire pre-filed §7 gap list no lane in this audit cited.

---

