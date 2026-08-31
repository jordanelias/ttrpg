# R4 — references/, registers/, canon/ : registries, vocabulary, ledgers

## 1. CURRENT.md reproduced

`CURRENT.md:1` — Generation v40. `_Last reconciled:_` stamp (`CURRENT.md:20`) = **2026-08-27** (IN+SC+PC+FA lanes, post-merge audit). Note: the file's own header (`CURRENT.md:10-16`) says `deprecated/` no longer exists (retired to `FORK:baf29d5`, S6/6a) and the status dashboard was RETIRED 2026-08-21.

| Subsystem | Current head | Status note |
|---|---|---|
| Personal combat | `systems/combat/combat_engine_v1/` (resolver package) | `CURRENT.md:23` — engine wins over prose; open items JD-2/3/5/6/7/8 |
| Mass battle | `systems/mass_battle/mass_battle_v30.md` + integration doc | `CURRENT.md:24` |
| Social contest | `systems/social_contest/social_contest_v30.md` (+index/infill); kernel `sim/contest/` | `CURRENT.md:25` — ⚠ contest_rebuild in flight, "three resolution models under one name" found by 2026-08 audit; ED-SC-0015 needs Jordan |
| Faction / political | `faction_canon_v30.md` + 4 co-docs + `faction_politics_v30.md` (PP-660, CANONICAL) | `CURRENT.md:26` |
| Settlement / territory | `settlement_layer_v30.md` + adjacency/temperament/geography | `CURRENT.md:27` — governance-play redesign PROPOSED |
| Clocks & tracks | `systems/overview/clock_registry_v30.md`, self-declared CANONICAL | `CURRENT.md:28` — Truth rename (ED-IN-0075) executed; 419-ref corpus sweep still STAGED |
| Threadwork | `systems/threadwork/threadwork_v30.md` | `CURRENT.md:29` |
| Fieldwork/Investigation | `fieldwork_v30.md` (DESIGN) + `investigation_systems_v30.md` (CANONICAL) | `CURRENT.md:30` |
| Architecture / Key substrate | `key_substrate_v30.md` + `key_type_registry_v30.md` | `CURRENT.md:31` — executable substrate `engine/substrate/keys.py` landed 2026-07-07; A17 pointer-vocab enforcement backlog 36/71 |
| Architecture / Holonic doctrine | `holonic_container_doctrine_v1.md` — CANONICAL | `CURRENT.md:32` |
| Architecture / Propagation spec | `propagation_spec_v1.md` — CANONICAL | `CURRENT.md:33` |
| Scale transitions | `scale_transitions_v30.md` — CANONICAL | `CURRENT.md:34` |
| Player agency | `player_agency_v30.md` — CANONICAL | `CURRENT.md:35` |
| Articulation | `articulation_layer_v30.md` | `CURRENT.md:36` |
| NPC behaviour | `npc_behavior_v30.md` | `CURRENT.md:37` |
| Master workplan | `workplans/valoria_master_workplan_v6.md` — CANON | `CURRENT.md:38` |
| Narrative engine | `narrative_engine_design_v2_churn.md` — RATIFIED | `CURRENT.md:39` |
| Godot conversion | `godot/godot_conversion_strategy_v1.md` — PROPOSED | `CURRENT.md:40` — GO lane ACTIVE, Gate-0 blocked on ED-1051 |
| Board game | EVACUATED → `params_tables.yaml` (fork `c451bcb`) | `CURRENT.md:41` |
| Dice / resolution | EVACUATED → `params_tables.yaml`; live resolver in code | `CURRENT.md:42` |
| Repository state armature | RETIRED 2026-08-21 | `CURRENT.md:43` |
| Decision policy | `decision_policy_v1.md` — DRAFT FOR RULING, does not ratify on merge | `CURRENT.md:44` |

**No `## Status:` row anywhere in this table names a Person/Rung/Office/Site/Tenure carrier or a mint/alter/efface state-change vocabulary — see §10.**

---

## 2. THE GLOSSARY — every defined term (`references/glossary.md`, 305 lines, last updated 2026-08-08)

The glossary is organized in 13 numbered Parts. Every "Full Term" row is a defined term. Complete inventory by Part, with a same/different-meaning check against the proposed design:

**Part One — Attributes** (`glossary.md:57-63`, ⚠ IN FLUX per `:53`): Agility, Attunement, Cognition, Endurance, Presence, Spirit, Strength (7-row roster — **conflicts with `descriptor_registry.yaml`'s 9-row roster**, see §4). None of these words appear as carrier/edge names in the design; **`Presence`** is the one overlap word — see §6.

**Derived Character Stats** (`:75-82`): Health, Stamina, Coherence, Intelligibility, Composure, Focus, Truth, Momentum. **`Coherence` here is a STORED per-character track**, not the design's `Query`. See §3.

**Thread Practitioner Stats** (`:88-91`): Thread Sensitivity (TS), Thread Pool Score (TPS), Thread Depth (TD, REMOVED PP-166), Thread Tension (TT).

**Part Two — World Clocks** (`:100-106`): Mending Stability (MS), Church Influence (CI), Institutional Pressure (IP), Public Instability (PI).

**Part Three — Debate** (`:114-120`): Piety Track (CT), Concentration, Doubt Marker, Composure, Genre, Orientation, Interaction Type.

**Part Four — Faction Stats** (`:132-138`): Mandate, Influence, Wealth, Military, Intel, Stability, Standing.

**Part Five — Combat** (`:148-155`): Combat Endurance, Command, Damage Resistance, Size, Power, Discipline, Health per Size, Total Health. **`Command`, `Discipline` are the mass-battle unit stats** — not the design's vocabulary.

**Part Six — Dice** (`:165-170`): Target Number (TN), Obstacle (Ob), Expected Value (EV), Degree of Success, Overwhelming, Partial. **`Degree`-adjacent** — see §6.

**Part Seven — World/Narrative** (`:178-197`): Gap, Shifting Object, Locked Zone, Monstrous Incursion, The Rupture, Knot, Belief, Inspiration, History, Character Point (CP), Disposition, Domain Action, Domain Echo, Grievance Marker, Co-Movement Card, Einhir, Arc, Zoom In, Zoom Out, Cardinal. **`Disposition`** appears — the design does not use it, but it is a live NPC-attitude vocabulary word a Person-carrier design would need to reconcile against (`glossary.md:188`).

**Part Eight — Thread Operations** (`:205-215`): Weaving, Pulling, Past-Oriented Pulling (POP), Locking, Dissolution, Mending, Diagnosis, Leap, Forced Resolution (FR), Dissolution Residue, Overweaving.

**Part Nine — Sim/Infra** (`:223-231`): Simulation Identifier, Patch (PP-NNN), Editorial Decision (ED-NNN), Simulation Debt, Game Master (GM), NPC, PC, Burning Wheel (BW), AI.

**Part Ten — Mode labels** (`:241-243`): TTRPG, BG, Hybrid.

**Part Eleven — Top-level systems** (`:251-259`): Turmoil, Conflict Architecture, Campaign Architecture, Victory, CI Political + 12 "registration pending" system names.

**Part Twelve — Collision/Disambiguation table** (`:267-273`, abbreviation collisions only): CI, CP, TD, COMP, RS.

**Part Thirteen — Deprecated abbreviations** (`:281-288`): CERT, TLK, DD, FSTAT, CE, INT.

None of the design's four carriers (`Person`, `Rung`, `Office`, `Site`), its edge (`Tenure`), its state-change vocabulary (`mint`/`alter`/`efface`), or its six loop-step names (CALENDAR/MATTER/DELIBERATE/RESOLVE/WITNESS/CENSUS) appear anywhere in the glossary.

---

## 3. ⭐ THE `Derived` FACT

**Verbatim, `references/glossary.md:65`:** `### Derived Character Stats`, table header at `:73`: `| Full Term | Abbr | Formula lives at | Description |`, with member rows at `:75-82`: **Health, Stamina, Coherence, Intelligibility, Composure, Focus, Truth, Momentum** — each a per-character, engine-tracked, *stored* value (e.g. `:77` "Coherence... Starts at 10", `:82` "Momentum... Gained on Overwhelming success... Spent for automatic successes").

**`engine/engine_params/params_tables.yaml`** (confirmed on disk under `engine/engine_params/`, not `references/`) ships sections literally titled *"Derived Values"* / *"Derived Scores"* per the design's own citation (`03_COMPENDIUM.md:649`) and CLAUDE.md §5 ("`params/core.md` §Derived Scores").

**`references/descriptor_registry.yaml:284`** — the `not_descriptors.derived_values:` list, a **flat array of 20 bare strings** (`[Health, Stamina, Composure, Concentration, Thread Fatigue, Resolve, Garrison Strength, Local Economy, Mandate, Wound Interval, Max Wounds, Face, TroopCount, "Legitimacy (faction, derived)", Treasury, Levies Available, Reputation, "Discipline (faction)", Intelligence Holdings, Public Order, Settlement Weight]`) — confirming "flat global namespace" is the literal on-disk shape, not a design exaggeration.

**Verdict: the design's claim is CONFIRMED TRUE.** `Derived` in this repository — today, in three independent live registries (`glossary.md`, `params_tables.yaml`, `descriptor_registry.yaml`) — means a **stored, per-character, computed-and-cached value in a flat global namespace**. The design's `Query` category means the **opposite**: "a named pure function over state, never stored" (`03_COMPENDIUM.md:649`, citing its own R-1: *"compute-on-demand, never push, never store"*). Reusing `Derived` for the opposite meaning would have been a direct, repo-verified collision. **The rename to `Query` was necessary, not cosmetic**, and the collision the design cites is real down to the exact file:line locations it names.

---

## 4. `descriptor_registry.yaml` PARSED

Parsed with `yaml.safe_load` (`references/descriptor_registry.yaml`, 322 lines, `version: v1`, `ratified: 2026-06-06`).

**Attributes** (`:45-59`): 3 domains (body/mind/social) × 3 attributes = **9 total**: `attr.body.{strength,endurance,agility}`, `attr.mind.{focus,acuity,will}`, `attr.social.{attunement,charisma,bonds}`. Each carries `aliases:` — e.g. `attr.mind.will` aliases `[Spirit]`, `attr.social.charisma` aliases `[Influence, Presence]`, `attr.social.attunement` aliases `[Perception]`.

**CLAUDE.md claims, VERIFIED:**
- "ships NINE attributes" — **VERIFIED-TRUE** (`:49-59`, counted 9 leaf entries).
- "tenth unnamed" — **VERIFIED-TRUE**, and stronger than paraphrase: the file's own header (`:39-43`) states it explicitly — *"Jordan, 2026-08-14: 'it will be 10 attributes'. NINE are defined below. The TENTH IS UNNAMED... Do not infer the tenth from the aliases: Spirit folds to Will and Perception folds to Attunement..."*
- "aggregates `agg.body/mind/social` marked `placeholder`" — **VERIFIED-TRUE** (`:64-66`, all three entries carry `status: placeholder`; note at `:67-71` confirms "NOT active until that migration").
- "attribute keys marked `warn` not `block`" — **[unclear/PARTIAL]**: the block/warn severity is not a field *in this file*; it lives in the CI checker (`tools/quantity_registry.py` / `ci_quantity_vocabulary_check.py`, cited at `CURRENT.md:31` as "report-only"). This registry itself carries no `warn`/`block` field — cannot verify from this file alone; consistent with, but not directly confirmed by, the registry's own text. **[unclear]**

**Other verified structure:**
- `faction_stats` (`:150-159`): 6 entries, all floor 0 as of 2026-08-23 Jordan rulings (`fac.influence, fac.legitimacy, fac.wealth, fac.military, fac.intel, fac.stability`) — note `:159` explicitly distinguishes `fac.legitimacy` from `Mandate` (a size-weighted derived aggregate, NOT a base stat).
- `settlement_stats` (`:164-172`): 6 entries.
- `category_b_scalars` (`:184-201`): 7 pointer-only registrations (Wounds, Poise, Initiative, Turmoil, Accord, Coup posture, Succession status, season counter) — explicitly NOT schema bindings (`:202-207`).
- `conviction_roster` (`:235-251`): 13 named Convictions, enumerated in-file since 2026-08-24 specifically to close a silent-no-op bug where two code modules (`conviction.py` 9 names, `npe.py` 8 names) had invented their own divergent rosters (`:210-234`).
- `deprecated` (`:268-269`): 1 entry (`resonance_style`), with its own retraction-of-retraction note.
- `not_descriptors` (`:283-322`): `derived_values` (20), `tracks` (7), `clocks` (4: Piety, CI, MS, IP), `pools` (8).

---

## 5. THE REGISTRATION TABLE — `module_contracts.yaml` as a name-binding surface

Parsed: `schema_version: 2`, `generated: 2026-06-10`, `status: EXTRACTED_STAGE1`, **27 modules** (`modules:` is a list, confirmed len=27).

**`doc: null` count — VERIFIED = 9** (matches CLAUDE.md's corrected count exactly): `npc_memory, scene_slate, game_director, scene_timer, audit, domain_actions, settlement_economy, engine_clock, scenario_authoring`.

**`[ASSUMPTION]`-grade resolver count — VERIFIED = 11** (grep for `resolver:.*# [ASSUMPTION]` comment pattern, lines 210, 287, 386, 419, 471, 835, 877, 1024, 1169, 1206, 1233 — exactly 11 lines). CLAUDE.md's "11/27" claim is confirmed.

**Module roster** (module -> doc -> resolver): `faction_state`->`faction_behavior_v30.md`->`deterministic_accounting`; `npc_behavior`->`political_dynamics_keys_migration_v30.md`->`deterministic_accounting`; `npc_memory`->null->`state_reader`; `piety_track`->`conviction_track_v1.md`->`deterministic_accounting`; `territorial_piety`->`conviction_track_v30.md`->`deterministic_accounting`; `threadwork`->`threadwork_v30.md`->`dice_pool`; `fieldwork_knots`->`knots_v30.md`->`dice_pool`; `scene_slate`->null->`manifest`; `game_director`->null->`manifest`; `scene_timer`->null->`state_reader`; `audit`->null->`state_reader`; `social_contest`->`social_contest_v30.md`->`dice_pool`; `mass_battle`->`mass_battle_v30.md`->`dice_pool`; `domain_actions`->null->`d_sigma`; `peninsular_strain`->`peninsular_strain_v30.md`->`deterministic_accounting`; `settlement_layer`->`settlement_layer_v30.md`->`deterministic_accounting`; `settlement_economy`->null->`deterministic_accounting`; `ci_political`->`ci_political_v30.md`->`deterministic_accounting`; `victory`->`victory_v30.md`->`state_reader`; `engine_clock`->null->`clock_advance`; `faction_politics`->`faction_politics_v30.md`->`deterministic_accounting`; `miraculous_event`->`miraculous_event_v30.md`->`state_reader`; `scenario_authoring`->null->`manifest`; `articulation_layer`->`articulation_layer_v30.md`->`deterministic_accounting`; `clock_registry`->`clock_registry_v30.md`->`manifest`; `personal_combat`->`combat_engine_v1/`->`d_sigma`; `campaign_architecture`->`campaign_architecture_v30.md`->(status `stub`, no resolver).

**Key/event-type namespace — 48 distinct types** across all `consumes`/`emits` (plus a wildcard `*`): `da.{antinomian_action,covert_betrayal,diplomatic_alliance,economic_intervention,public_governance}`, `env.{crisis,disaster,peninsular_strain_shock,population_change}`, `mechanical.{accounting,cascade_resolution,mission_shift,project_advanced,scene_entered,scene_exited,scene_skipped,season_change}`, `meta.{knot_formed,knot_ruptured,miraculous_event,thread_woven}`, `scene.{battle_concluded,combat_felled,combat_hit,combat_resolved,combat_strike,contest_resolved,dialogue,displacement,draft_da,gift,gossip,insult,interaction,investigation_resolved,thread_operation,threat,witness}`, `state.{belief_revised,concern_resolved,coup_attempted,opinion_revised,project_completed,project_failed,scar_acquired,standing_change,succession}`.

**Is this the single registration table CLAUDE.md §3 claims?** **NO — refuted, in-tree, by the repo's own newest editorial entry.** `registers/editorial_ledger_in.jsonl` ED-IN-0200 (2026-08-27, `status: open`, quoted in full in §8) states: *"Three registries exist and none of them is hierarchically related to the others: `references/module_contracts.yaml`... `engine/engine_params/key_types.json` (55 key types)... `references/descriptor_registry.yaml`... They are three FLAT namespaces that reference each other by string. There is no single surface from which a reader — or the Godot port — can descend from 'the game' to a subsystem to a module to its Keys to the fields those Keys carry."* This is a Jordan ruling, not executed. See §13.

---

## 6. THE COLLISION REGISTER, CHECKED AGAINST THE REPO

| word | meanings the design found | ADDITIONAL meanings in the repo | sufficient? |
|---|---|---|---|
| **`hold`/`HOLDS`** | Tenure kind; Proposition mood `HOLDS`; predicate `HOLDS(p,x)`; coercion quantity (4) | **5th, live CODE meaning, not in prose at all**: a mass-battle unit **tactical stance**. `systems/mass_battle/sim/config.py:269` — `STANCE_SPEED_MOD = {"aggressive": 1, "balanced": 0, "hold": -99, "retreat": 0}`; consumed at `systems/mass_battle/sim/hierarchy/units.py:1416,1701` (`if self.stance == "hold":`) and `systems/mass_battle/sim/engine.py:387`. Extensively discussed in `registers/handoffs/HANDOFF_MB.md:328-560` (ED-MB-0043/0045) as a load-bearing two-gate mechanic. **6th, process-vocabulary sense**: `HELD`/"held for Jordan" as a ruling-queue status (`tests/valoria/test_degree_ladder_single_owner.py::HELD`, `HANDOFF_IN.md:53` "Two DECLARED HOLDS... both needing Jordan") — an item awaiting a decision. | **NO — the design's table (`03_COMPENDIUM.md:683`) does not mention the mass-battle stance sense at all**, and it is the single highest-collision word in the register colliding with a live, currently-executing engine constant in a sibling subsystem the design must eventually interoperate with (mass battles are a `Site`/`Office`-adjacent domain). |
| **`subject`** | `Tenure.subject`, `Claim.subject`, `Proposition.subject`, `subject_id`, Key `Target` role (5) | No further repo meaning found beyond generic English ("subject matter", "same subject") — no registry field named bare `subject`. | Sufficient as scoped. |
| **`kind`** | `Rung.kind`, `Tenure.kind`, mark/need/stance-referent kind, `Record.kind`, `MatterKind` (7) | **Two additional repo-native taxonomy fields not cross-checked**: (a) `references/descriptor_registry.yaml:16-19` — the registry's own `KIND:` enum (`attribute_scalar | attribute_aggregate | faction_stat | settlement_stat | practitioner_stat | territory_stat | conviction_weight | ethical_axis | conviction_axis_map | orientation_scalar | contest_style | temperament_type | template | personal_track`) — a 14-value classification vocabulary for descriptors, used as a bare `kind:` YAML key at `:186-200,257-263`. (b) `references/module_contracts.yaml:171-178` — a **separate** `kind: value` field distinguishing module-constant registrations from callables (`contest_side.a: {kind: value, ...}`). | **Design's disambiguation ("always qualified by its record") does not anticipate that `kind:` is already an active YAML key in two unrelated repo registries** — a future exporter emitting `Tenure.kind`/`Rung.kind` alongside these registries risks a field-name collision at the tooling layer even if prose never confuses the senses. |
| **`condition`** | `condition(site)`, convening condition, stasis-ladder "named condition" (3) | Generic-English uses only (`ci_checks_registry.yaml:466` "pre-existing condition"); no additional load-bearing repo sense found. | Sufficient. |
| **`object`** | `Tenure.object`, `touch.target`, generic "object" (3) | No additional registry-bound sense; `canon/00_philosophical_foundations.md:135` uses "object" in ordinary philosophical-English (phenomenology of dread "that has no object") — thematically adjacent to canon vocabulary but not a mechanical collision. | Sufficient. |
| **`act`** | record `Act`, `remit.acts`, currency sense (3) | `references/name_collision_database.yaml:63` — `CB: {term: "Casus Belli"..., silo: 11}` glosses CB as "standing right to **act**" (English verb only, not a collision). No additional binding sense. | Sufficient. |
| **`matter`** | `Rung.matter` field, MATTER step/write-class, English verb (3) | No additional registry-bound sense (all repo hits are ordinary English "the matter is unsettled" / "subject matter"). | Sufficient. |
| **`root`** | graph sense `sovereign_fraction(root)`, provenance "root token", `conferral_path` reaching root (3) | Repo-native organizational sense not in the design's table: **"root" = repository root / root-level file**, used constantly (e.g. `atomization_rules.yaml:135` "root index + lane files", `id_reservations.yaml:117` "root-cause audit", `canonical_sources.yaml:471` "root PP-686 doc"). Low collision risk (obviously disjoint domains) but the design's table doesn't record this sense exists at all. | Sufficient in practice; **not recorded**. |
| **`degree`** | commitment degree 0-5, degree-of-success band, knot `depth` (3) | Consistent with, not additional to, the design's "degree band" sense: `id_reservations_history.md:96` "ED-IN-0170 — degree-vocabulary equivalence census" and `id_reservations.yaml:234` "0187 degree ladder" are the SAME degree-of-success-band collision the repo has already been actively resolving (ED-SC-0031/0032, `HANDOFF.md:20-36`) — this is corroboration, not a new sense. | Sufficient — and independently corroborated as a *live, currently-being-fixed* repo collision. |
| **`presence`** | Query `presence(prop,c)`, "deposits by presence", `enforcer_presence` (3) | **Additional, high-value repo meaning**: `references/glossary.md:61` — **`Presence`** was the original name of the Core Attribute now aliased to `Charisma` in `descriptor_registry.yaml:58` (`attr.social.charisma... aliases: [Influence, Presence]`). This is a THIRD live meaning (a per-character attribute score, 1-7 scale, appearing in dozens of formula citations across the corpus under its legacy name) that the design's table does not list. | **NO — the attribute-name sense is a real, formula-cited, still-alias-resolved collision the design's table omits entirely.** |
| **`View`/`view`** | type passed to `choose` (capital), function `view`->renamed `assemble` (2, case-distinguished) | **Additional repo meaning**: `systems/_architecture/engine_atlas_v1.md:33` — `View` names one of **four documentation-perspective lenses** on the engine ("Declared / Countable / As-built / Structural View"), a repo-process vocabulary term, capitalized, in a CANONICAL-adjacent architecture doc. | **NO — a third, capitalized, architecture-vocabulary sense of `View` exists and is not in the table.** |
| **`stake`** | `Rung.stake[]` field, "escalate the stake" manoeuvre (2) | `references/throughlines_meta_infill.md:144,263,384` use "stake"/"stakes" in ordinary narrative-design English ("stakes are visible", "no attached NPC with stake") — thematically close but not a registry-bound collision. | Sufficient. |
| **`address`** | `Person.address` field, "may address many offices" verb (2) | No additional registry sense; `canon/01_foundations_amendment_self_rendering.md:56` uses "address" in ordinary English. | Sufficient. |
| **`magnitude`** | die reading, `impact_vector` signed magnitude (2) | No additional bound sense found. | Sufficient. |
| **`standard`** | advancement-attempt sense (forbidden), `EntryStandardTerm` type (2) | No additional bound sense found. | Sufficient. |
| **`commit`** | Tenure kind, `commit(+delta)` operation, git commit (3, declared acceptable) | Confirmed: `CLAUDE.md` §2 (git commit) is the third sense the design already names and accepts. No further sense found. | Sufficient (design already resolves it explicitly). |
| **`Derived`** | design's retired query-category name | See §3 — **CONFIRMED, three independent live sources** (`glossary.md:65-82`, `params_tables.yaml`, `descriptor_registry.yaml:284`). | N/A — already resolved by rename. |
| **`Container`/`Node`** | Godot built-ins (generic warning) | **Confirmed with exact citations, not previously pinned by the design**: `godot/godot_architecture_specification.md:381` (`class_name ContainerBase extends Control`), `:402` (`class_name ConflictContainer extends Node`), `:576` (`extends Node`) — this doc is CLAUDE.md-flagged **STALE REFERENCE** (§6/CURRENT.md:41) but is still on disk and still the only Godot-side prior art using these exact class shapes. Any future `Container`/`Node` type in the new design's Godot layer collides directly with these already-authored (if stale) class names. | Design's warning is directionally right; **now has file:line grounding** it lacked. |

**Highest-value new finding: `hold` as mass-battle stance is a fifth, live, currently-executing-code collision the design's own table does not record — and it sits in the one adjacent subsystem (mass battle, closest existing analogue to `Office`/`Site` military domain-actions) most likely to actually interoperate with a `Tenure(kind=hold)` edge.**

---

## 7. CANON P-01..P-15 — compliance check

Source: `canon/02_canon_constraints.md:10-24` (the extracted constraint table with violation tests).

| # | One-line principle | Compliance verdict |
|---|---|---|
| P-01 | Inseparability: thread ops co-move temporal/epistemic/actual dimensions, no GM discretion to skip | **Silent** — the design's `resolve`/`witness` signatures don't touch Thread-operation mechanics at all; P-01 constrains a subsystem (`threadwork`) the design doesn't model. |
| P-02 | Monstrosity grounded in the Lacanian Real, structurally non-moral | **Silent** — no monster/Monstrous-Incursion carrier in the design. |
| P-03 | Rendering = consciousness-performed, not external mechanism; GM is the rendering engine | **Tension, worth flagging**: the design's `Query` category is explicitly "never stored, always recomputed" (`03_COMPENDIUM.md:649`) — structurally resonant with P-03's "rendering is what minds do, performed, not stored" framing, but P-03 is about *in-world epistemics* (what a character perceives) while `Query` is an *engine* computation category. Not a real conflict, but a term-level echo worth naming if `Query`/`View`/`Sensation` ever get read as claims about in-fiction rendering rather than engine plumbing. |
| P-04 | Monstrosity = ontological, not moral; no alignment system | **Silent** — design has no monster/alignment vocabulary. |
| P-05 | Three emergence modes mechanically distinct | **Silent**. |
| P-06 | Threadcut beings have no layer 2 | **Silent**. |
| P-07 | Calamity = rendered-side mechanism; the ground has no agency | **Silent** — but this is the principle CLAUDE.md itself cites (`02_foundations_amendment_leap_mechanism.md:40`) as "the ground does not resist actively"; the design's `World` carrier and `resolve()` signature, if ever extended to Thread mechanics, would need to respect P-07's no-agency constraint. Not currently at risk. |
| P-08 | Epistemological barrier = inaccessibility, not suppression | **Silent**. |
| P-09 | Memory pulling = messy, costly, detectable | **Silent**. |
| P-10 | Coherence indexes commensurability with human-mode being, tridimensional | **Silent** — `Coherence` (a stored `Derived`/track value, §2-3 above) is untouched by the design; no naming risk since the design doesn't use `Coherence`. |
| P-11 | Temporal Disjunction universal to thread ops | **Silent**. |
| P-12 | Drift propagation tridimensional through knots | **Silent** — no `Knot` carrier in the design (design has no relationship-bond primitive distinct from `Tenure`). |
| P-13 | Forgetting = rendering failure, Southernmost knowledge untransmittable | **Silent**. |
| P-14 | Board/VG modes must express inseparability, co-movement in every mode | **Potentially relevant, unaddressed**: the design's six-step loop (CALENDAR/MATTER/DELIBERATE/RESOLVE/WITNESS/CENSUS) is presented as the single game loop across scales. P-14 requires that co-movement (temporal/epistemic/actual) fire in **every** mode/scale. If the design's loop is meant to *replace* the TTRPG/BG/Hybrid mode distinction P-14 is written against, that is an open compliance question the design does not address — **flag, don't resolve.** |
| P-15 | Three-layer being-persistence (Ein Sof spooling / unconscious self-rendering / deliberate threadwork); Leap = layer-2 suspension | **Silent** — no `Coherence`/Leap vocabulary in the design. |

**Overall verdict: SILENT on 13 of 15, one soft terminological echo (P-03/`Query`), one structural question flagged but not resolved (P-14/loop-vs-modes).** The design operates at a level of abstraction (bureaucratic/political carriers and edges) that the canon's P-01..P-15 constraints — all about Thread metaphysics, monstrosity, and rendering — do not reach. **No conflict found.** This is itself worth stating plainly: the design is not in tension with canon because it does not yet touch the layer canon governs.

---

## 8. THE LEDGERS — schema, counts, and every relevant entry

**Schema:** two generations coexist (`CLAUDE.md` §4 confirmed in practice). Pre-cutover flat entries (`registers/editorial_ledger.jsonl`, sample `ED-107`) carry `{id, status, date_resolved, description, decision, tags, date_deprecated?, deprecation?}`. Post-cutover lane entries (`registers/editorial_ledger_<lane>.jsonl`, sample `ED-IN-0003`) carry `{id, status, date, description, source?, confidence, needs_jordan, system?, citations?, files?}`.

**Line counts** (each file is one JSON object per line):
| file | lines |
|---|---|
| `editorial_ledger.jsonl` (flat, pre-cutover) | 289 |
| `editorial_ledger_archive.jsonl` | 492 |
| `editorial_ledger_fa.jsonl` | 38 |
| `editorial_ledger_fi.jsonl` | 8 |
| `editorial_ledger_go.jsonl` | 1 |
| `editorial_ledger_in.jsonl` | 57 |
| `editorial_ledger_in_archive.jsonl` | 145 |
| `editorial_ledger_mb.jsonl` | 30 |
| `editorial_ledger_mb_archive.jsonl` | 38 |
| `editorial_ledger_pc.jsonl` | 29 |
| `editorial_ledger_pc_archive.jsonl` | 28 |
| `editorial_ledger_sc.jsonl` | 32 |
| `editorial_ledger_se.jsonl` | 50 |
| `editorial_ledger_wr.jsonl` | 9 |

`registers/archive/` (26 frozen ED-ledger fragments, per CLAUDE.md §1/§3) holds 25 `.yaml` files + 1 `editorial_ledger_index.md` (unparsed by design, per CLAUDE.md — walked, not read).

**registers/mechanics_index.yaml**: dict, 13 top-level keys. **registers/patch_register_active.yaml**: `patches:` list, **6 active patches**. **registers/supersession_register.yaml**: `entries:` list, **28 entries**.

**Every ledger entry dated 2026-08-25 or later (13 total, all lanes, parsed programmatically):**

| lane/file | id | date | status | description (truncated) |
|---|---|---|---|---|
| FA | ED-FA-0037 | 08-25 | landed | Mass seizure wrote a canonical Accord TIER into the CONTINUOUS `Territory.accord` field (`mass_seizure.py:293`) |
| FA | **ED-FA-0038** | 08-27 | landed | **"ONE FACTION WRITE MECHANISM" (Jordan ruling, logged late)** — see §13 |
| IN | ED-IN-0196 | 08-25 | landed | **"TN7 always. Never change TN anywhere ever."** (Jordan ruling) |
| IN | ED-IN-0197 | 08-25 | landed | Continuity/doctrine correction — HANDOFF.md falsely said `main` was red |
| IN | ED-IN-0198 | 08-25 | landed | Campaign-level regression gate was INERT (CI timeout 5min vs 6m15s runtime) |
| IN | ED-IN-0199 | 08-27 | landed | `engine_clock` module now exists; tick composition owned per `propagation_spec_v1.md` §O.1 |
| IN | **ED-IN-0200** | 08-27 | **open** | **Centralized hierarchical key/module contracts — RULED, NOT EXECUTED.** Full text §5/§13. |
| IN | **ED-IN-0201** | 08-28 | **open** | **Personnel precondition — RULED, NOT EXECUTED.** Full text §10/§13. |
| MB | ED-MB-0066 | 08-25 | landed | Volley TN 6->7 under ED-IN-0196 (the one live TN-sweep golden-mover) |
| PC | ED-PC-0057 | 08-27 | landed | Duplicate-ID renumber (was ED-PC-0041, already allocated 07-29) |
| SC | ED-SC-0031 | 08-27 | landed | Ninth degree ladder migrated to `dice_engine.degree_from_net` |
| SC | ED-SC-0032 | 08-27 | landed | Injection seam `dice_engine.BandExtension`; de-saturation moved out of engine |
| SE | ED-SE-0050 | 08-25 | landed | Drift-store read/write asymmetry (`temperaments.py:117` vs `:153`) |

**Every architecture/keys/vocabulary/Godot entry regardless of date** (beyond the above): ED-IN-0192 "resolver architecture" and ED-IN-0193 "§5-§7 restore" (`id_reservations.yaml:234`, dates not in the 08-25+ window but architecture-subject); ED-GO-0001 (GO lane ACTIVE, `CURRENT.md:40`); ED-1051 (module-contract gaps, `needs_jordan`, cited repeatedly as blocking Gate-0 and `engine_clock`'s `doc:` flip); ED-1083/ED-1094 (holonic doctrine + propagation spec ratification); ED-IN-0018/0026 (Key & Echo Armature). The full text of the two most load-bearing (ED-IN-0200, ED-IN-0201) is quoted in §13.

**Open `needs_jordan: true` rows, by lane file (grep counts, not exhaustive text — see individual HANDOFF files for full text):** `HANDOFF_2026-08-24_SESSION.md` 3 mentions (incl. "154 `needs_jordan` rows" repo-wide estimate, `:253`); `HANDOFF_FA.md` 7 (ED-FA-0010, 0013(c), 0018, 0021 resolved-false, others open); `HANDOFF_IN.md` 24 (incl. ED-IN-0030, ED-IN-0042, ED-1051, the armature §5 docket, D15/D16 from ED-IN-0064); `HANDOFF_MB.md` 4 (ED-MB-0039, 0044); `HANDOFF_PC.md` 8 (ED-PC-0049, 0050, 0051); `HANDOFF_SC.md` 3 (ED-SC-0002..0005 docket); `HANDOFF_SE.md` 6 (ED-SE-0002 Accord/Order stacking, ED-SE-0013/0014/0015/0017 optional mechanics). `HANDOFF_FI.md`, `HANDOFF_GO.md`, `HANDOFF_WR.md` have zero.

---

## 9. HANDOFF STATE — open items and next actions

**Root `HANDOFF.md` (531 lines), current as of 2026-08-27 (`:12`):** `main` IS GREEN (1772 passed / 23 skipped / 15 xfailed). Cross-lane items OPEN (`:83-108`):
- **[PC]** Derive Ob from the DEFENDER — "genuine new mechanism", last declared HOLD in `test_degree_ladder_single_owner.py`.
- **[IN]** `engine_clock.run_tick`'s drain topology (§4.1) is NOT implemented — blocked on R-1 (D.6 double-count) and R-4 (ORD-3 observer ordering).
- **[IN]** ~38 flow-skeleton anchors re-based; adversarial sample found 12/23 already stale; nothing in CI validates anchor *content*.
- **[FA/WR]** parliamentary-bridge shut-out set has taken 3 different values under 3 unrelated changes — only measured at n=8/seed-42; needs n>=100 arm.
- **[SC]** the `BandExtension` seam has exactly one consumer (`PoolDesaturation`) — untested against a second user.

**Next actions (`:189` onward):** the live pointer is `proposals/2026-08-21-execution-order-v1.md` §3, `state: next` = **S7** (audit/ corpus extraction, ~33 working papers). S8 Half A landed (fractional dice); **S8 Half B SUSPENDED by Jordan** ("flagged for later systems work. Do not wire it") — the `score/2` Ob-derivation reconciliation. **6c (slim the handoffs) explicitly DID NOT RUN** — measured 21% narrative-but-unswept, "12 of 17 `[DONE]`-marked sections carry open/held/`needs_jordan` items inside them."

**Lane files, dated top-of-file status:**
- `HANDOFF_FA.md`: 27 SE/FA-lane items filed 2026-07-08/09, 20 still open/needs_jordan; ED-FA-0018 (Crown Administrative flat-rank credentialing pipeline) is the top needs_jordan item.
- `HANDOFF_IN.md` (3888 lines — by far the largest): dozens of open architecture items; most load-bearing: ED-1051 (module-contract gaps blocking Gate-0/`engine_clock`), the armature §5 fork docket, D15 (`contracts_bucket`<->registry-KIND crosswalk, explicitly REJECTED/not filed per `descriptor_registry.yaml:315-317`).
- `HANDOFF_PC.md`: ED-PC-0049/0050 (blunt-composite spike parity, heft two-direction split) both `needs_jordan: true`, both explicitly named as Jordan's residual after an adversarial pass.
- `HANDOFF_SC.md`: ED-SC-0015 "JORDAN RULING NEEDED" per `CURRENT.md:25`; contest_rebuild Stage 4 pending.
- `HANDOFF_SE.md`: ED-SE-0002 (Accord/Order stacking, open since 2026-07-05); 20-item needs_jordan share of the SE docket.
- `HANDOFF_MB.md`: ED-MB-0039/0044 open (envelopment stability, R3 definitional gap — "no shared substrate to reconcile onto").
- `HANDOFF_FI.md`, `HANDOFF_GO.md`, `HANDOFF_WR.md`: short (41-53 lines), no open needs_jordan items found.

**None of the above open items name Person/Rung/Office/Site/Tenure or the design's loop steps** — confirming the design proposal is a genuinely new surface, not a response to a filed HANDOFF item, **except** ED-IN-0200 and ED-IN-0201 (§13), which are close antecedents not cited by the design (dated 08-27/08-28, four/three days before the design's 08-31 date — the design may not have had access to them, or may be answering them without saying so; either way, cross-reference is warranted).

---

## 10. RECONCILIATION

| design object | named anywhere in references/registers/canon? | where | same meaning? | what registry would have to change to admit it |
|---|---|---|---|---|
| `Person` (carrier) | **NO** — zero hits for `\bPerson\b` in references/registers/canon | — | — | **`references/module_contracts.yaml:1543` is the closest existing statement of this exact gap**: *"No Character/Actor dataclass in World; 9- vs 10-attribute rival rosters, neither wired. Every personal-scale port needs this first."* `descriptor_registry.yaml` would need a `domain: person` (it currently has `[actor, settlement, equipment, environment]` at `:33` — `actor` is the closest existing domain name, not `Person`). |
| `Rung` | **NO** | — | — | No existing registry has a rank-ladder carrier; `faction_politics_v30.md`'s "rank-ladder/Standing 0-7 progression" (`CURRENT.md:26`) is the closest game-mechanical analogue but is a per-faction track, not a first-class carrier type. |
| `Office` | **NO** (as a carrier). `CI Political`/faction rank-ladders reference offices informally in prose. | `faction_politics_v30.md` (per `CURRENT.md:26`) | not directly comparable — prose office-holding vs. a typed carrier | `module_contracts.yaml` would need a new module entry with `state:` rows for Office-held descriptors. |
| `Site` | **NO** | — | — | `descriptor_registry.yaml`'s `territory_stats`/`settlement_stats` domains are the nearest existing carriers (Fort Level, Legitimacy, Prosperity, etc., `:90-172`) — `Site` would likely need to reconcile against `territory`/`settlement` scope rather than introduce a third. |
| `Tenure` (edge, 7 kinds incl. hold/oblige/commit) | **NO** as a named edge type. `hold`, `commit` collide with live vocabulary — see §6. | `mass_battle` (`hold`), `CLAUDE.md` §2 (`commit`) | **partially different** — see §6 | `engine/engine_params/key_types.json` (55 Key types, per ED-IN-0200) is the nearest existing typed-edge registry and would need a `Tenure` type family added, with the `hold`/`commit` names checked against the mass-battle stance and git-commit senses respectively. |
| mint / alter / efface (state-change modes) | **NO** | — | — | No existing registry expresses a mode-triple on state changes; `not_descriptors` in `descriptor_registry.yaml` distinguishes tracks/clocks/pools/derived_values by *kind of thing changed*, not *kind of change* — orthogonal, not overlapping. |
| `Act` / `Event` / `Claim` / `View` / `Sensation` / `World` | `Act` — generic English only (§6). `Event` — module_contracts.yaml uses `mechanical.*`/`scene.*`/`state.*` event **type strings**, not a first-class `Event` record. `Claim` — one hit, `module_contracts.yaml:1182` "Baralta Crown Claim" (a narrative-flavor term for a succession contest, unrelated meaning). `View` — see §6, third meaning found. `Sensation` — zero hits. `World` — **`module_contracts.yaml:111`** "World composition: the eleven seams inside `engine/autoload/game_state.py`" — **this is the SAME code-level object** (`game_state.py`'s `GameState`/`World` composition) the design's `resolve(Act[], World)` would need to bind to. | `module_contracts.yaml:105-120` (World), `:1182` (Claim, false-friend) | `World` — **same referent, informal alias already in use**; `Claim` — **different, false-friend** | `engine/autoload/game_state.py`'s existing "World composition" (11 seams, S5a 2026-08-22) is the closest live analogue to bind `World` to; `Claim` needs a disambiguating note against "Baralta Crown Claim" before the design's `Claim` (from `witness`) ships into the same corpus. |
| `choose`/`resolve`/`witness` (3 signatures) | **NO** as named functions. `resolver:` field in `module_contracts.yaml` (27 values: `deterministic_accounting`, `dice_pool`, `state_reader`, `manifest`, `d_sigma`, `clock_advance`) is the closest existing "resolve"-family vocabulary. | `module_contracts.yaml` `resolver:` field | different — module_contracts' `resolver` names a *strategy*, not a typed function signature | Would need a new top-level `resolve: (Act[], World) -> Event[]` contract shape layered over or replacing the current per-module `resolver:` enum. |
| six loop steps (CALENDAR/MATTER/DELIBERATE/RESOLVE/WITNESS/CENSUS) | **NO**. Closest existing loop vocabulary: `propagation_spec_v1.md`'s tick/accounting-phase sequencing (`ACTION`/accounting phases per `HANDOFF.md:29`), and `module_contracts.yaml`'s `accounting_phase:` field (values like `DA_proposal`, `settlement_accounting`, `B_concern`..`E_offscreen`). | `module_contracts.yaml` `accounting_phase:` field, `engine/autoload/engine_clock.py` (per ED-IN-0199) | **different vocabulary, same conceptual slot** (a season/tick phase sequence) | The engine's real phase machine (`engine_clock.py`, landed 2026-08-27) is the thing a CALENDAR/MATTER/DELIBERATE/RESOLVE/WITNESS/CENSUS loop would have to be reconciled against or replace — this is the single most concrete existing artifact the design's loop-step names should be checked against, and it postdates every design doc's likely drafting window (see §13). |

**The single most important reconciliation finding: `ED-IN-0200` (2026-08-27, Jordan-ruled, unexecuted) asks for exactly the thing this design proposal's collision/registration apparatus is — "key contracts and module contracts... explicitly defined in a centralized hierarchical manner" — four days before this design's 2026-08-31 date. Neither the design nor this ledger entry appears to cite the other. They should be reconciled explicitly, not left as two independent answers to the same ruling.**

---

## 11. DUPLICATION — registries that already hold what the design proposes

- **`Query` (compute-on-demand)** duplicates nothing — it is the *correct* rename precisely because the existing `Derived`/`params_tables.yaml`/`descriptor_registry.yaml` machinery is stored-value, the opposite shape (§3).
- **`descriptor_registry.yaml`'s `domain: [actor, settlement, equipment, environment]`** partially anticipates the design's carrier split (`actor`~=`Person`, `settlement`~=`Site`) but has no `office`/`rung` domain and is attribute-scoped, not carrier-scoped.
- **`module_contracts.yaml`'s `accounting_phase:` + `engine_clock.py`** already implement a real phase/tick loop that the design's six-step loop would need to map onto rather than duplicate.
- **`key_types.json` (55 types)** is the existing typed-edge registry `Tenure`'s 7 kinds would need to extend rather than reinvent.

---

## 12. GAPS — what the design needs that no registry can currently express

1. **No carrier-level registry exists.** `descriptor_registry.yaml` registers attributes/stats *of* an actor/settlement, never the actor/settlement *as a typed entity*. There is no `carriers.yaml` or equivalent. `module_contracts.yaml:1543` names this exact gap for the Person/Character case.
2. **No edge-type registry with a `kind:` enum for relationships** — `key_types.json` types Keys (typed messages/state), not typed persistent relationships between two carriers (what `Tenure` would be).
3. **No mode-of-change vocabulary** (mint/alter/efface) anywhere — the closest is the `bucket:` field in `module_contracts.yaml`'s `state:` entries (`track`/`clock`/`derived_value`), which classifies *what* changes, not *how*.
4. **No single hierarchical registration surface** — this is ED-IN-0200's own finding, verbatim, and is the gap the design's collision/gap-register apparatus is implicitly trying to fill without (apparently) citing ED-IN-0200 as its trigger.
5. **No registered notion of "a person must exist to act"** in the descriptor/module registries — but this exact requirement was independently ruled by Jordan one day after (ED-IN-0201, §13) and is currently **unexecuted engine-side** (`Faction` has no leader field, `world.npcs` is empty in every seeded campaign). The design's `Person` carrier is the natural home for executing ED-IN-0201, whether or not that was the design's intent.

---

## 13. Claims to escalate

1. **ED-IN-0200 (2026-08-27, open, unexecuted) vs. this design proposal (2026-08-31) answer the same Jordan ruling independently.** ED-IN-0200 verbatim: *"KEY CONTRACTS AND MODULE CONTRACTS ETC NEED TO BE EXPLICITLY DEFINED IN A CENTRALIZED HIERARCHICAL MANNER... Three registries exist and none of them is hierarchically related to the others... There is no single surface from which a reader — or the Godot port — can descend from 'the game' to a subsystem to a module to its Keys to the fields those Keys carry."* If the design proposal is meant to be that centralized hierarchy (or a step toward it), it should say so and cite ED-IN-0200; if it isn't, ED-IN-0200 remains open and unaddressed by four+ days of subsequent design work. **Escalate: does this design close ED-IN-0200, or does ED-IN-0200 still need separate execution?**
2. **ED-IN-0201 (2026-08-28, open, unexecuted) — the "personnel precondition" — is nearly the design's `Person` carrier's own charter, ruled one day before the design's dated corpus, and not cited by it.** Verbatim: *"all faction actions, settlement governance, mass battles, etc are predicated upon people existing... that leader themselves is going to influence what choices are made."* Measured engine state: `Faction` has no leader field, `Settlement.governor_id` is `None` on all 37 settlements, `world.npcs` is empty in every seeded campaign, so under this ruling a campaign currently performs **zero faction actions** once the gate is implemented. **Escalate: reconcile the design's `Person`/`choose(Person, View, Sensation) -> Act` signature explicitly against ED-IN-0201's two clauses (the gate; the decider) — this may already BE the execution vehicle for ED-IN-0201, unstated.**
3. **CLAUDE.md §3's "acyclic import graph" / single-registration claim vs. ED-IN-0200's "three flat unrelated namespaces" finding.** CLAUDE.md §3 documents the import-cycle fix (`test_importing_engine_pulls_in_no_subsystem`) as settling *dependency* structure, but does not claim (and ED-IN-0200 explicitly refutes) that the *naming*/registration structure is unified. Not a contradiction once read carefully, but worth flagging because a fast reader of CLAUDE.md §3 could mistake "acyclic imports" for "single registry," which ED-IN-0200 shows is false.
4. **`hold` (§6) is a five-way collision, and the mass-battle sense is both live code and untouched by the design's disambiguation rules.** The design's rule ("edge kind always written `Tenure(kind=hold)`") does not protect `STANCE_SPEED_MOD['hold']` in `systems/mass_battle/sim/config.py:269`, which is bare, lower-case, unqualified, and load-bearing (a `-99` speed multiplier gating an entire tactical mode). If `Tenure`/mass-battle ever share a namespace (plausible, since military domain-actions are a stated design target), this needs an explicit disambiguation rule, not just the four senses already in the table.
5. **`descriptor_registry.yaml`'s own count claim is stronger than the design likely knows**: the tenth attribute is not merely "unnamed" but the file itself (`:39-43`) actively warns against inferring it from aliases — a constraint that would bind any `Person` carrier's attribute-vector shape the moment it is authored, and is worth the design citing directly rather than only via CLAUDE.md's paraphrase.
