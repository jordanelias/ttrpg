# CENSUS (REST) — C2..C6 and the extended census, verified at the call site

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 4995824 (working tree)

Lane: Fable census, PART=REST. Rows: all of `census/C2`, `C3`, `C4`, `C5`, `C6`, plus the extended
census of `CENSUS_BRIEF.md` (verbs without predicate/effect or that never execute; records written and
never read; closed rosters with no loader refusal; tests over uncalled code; documents describing code
that does not exist). C1 is another lane's.

**IN PROGRESS — sections are appended as they are verified. A section that is absent below has not been
done; a row marked `[UNVERIFIED]` was not opened at the call site.**

## 0. Verdict and counts

(written last; see the end of the file until this placeholder is replaced)

## 1. C2 — record fields (72 rows, all opened at the write site and the read site)

**Reading of the census itself.** The script counted `.field =` as the only store. It cannot see a
positional constructor argument, a keyword it attributed to the declaration, `+=`, item assignment into a
dict field, or `getattr(self, f"{a}_{b}")`. 25 of the 72 rows are that and nothing else (20 more are the
same misreading inside the social-contest kernel, which dies anyway). 28 rows sit in
`systems/social_contest/sim/contest/`, which `05_SC_sc05_kernel_disposition_B.md` retires whole; 13 sit in
`systems/threadwork/sim/`, which `09_WR_threadwork_module.md` moves to `modules/threadwork/`; the other 31
are decided here on their own.

Decision codes: **FP** false positive · **DEAD** delete · **WIRE** broken, wire · **LABEL** correct text.
"T-read" = read by a test only.

### 1a. Engine and modules (27 rows)

| row | reading at the call site | decision | evidence |
|---|---|---|---|
| `RollResult.pool_size` `dice_engine.py:143` | written by keyword at `:215`; read by one test (`tests/valoria/test_dice_engine_properties.py:57`), which asserts `len(result.rolls)` for the same number at `:61`. `pool_size == len(rolls)` by construction (`:211-215`) | **DEAD** (batch D1) | no `.pool_size` load in `engine/`, `modules/`, `systems/`, `tools/` |
| `GoalStages.for_goals` `goals.py:83` | written positionally `goals.py:461`; read `:462` | **FP** | `GoalStages(rid, tuple(for_ids), ...)` |
| `Goal.org_kind` `goals.py:95` | written by keyword `goals.py:513`; 15 reads | **FP** | `org_kind=org_kind` |
| `VerbRow.refusals_by_clause` `verbs.py:217` | written by keyword `verbs.py:665`; read `verbs.py:350-358`, `resolve.py:755`, `aperture.py:253` | **FP** | — |
| `DevelopmentSheet.person_id` `sheet.py:122` | written positionally `sheet.py:155` (`DevelopmentSheet(p.id, ...)`); its reader is the `pick` callback handed in, i.e. the player surface | **FP** (record for the surface; `11_GO_player_surface_contract_B.md` §1 splits this record and keeps the id) | `sheet.py:152-157` |
| `Chronicle.person_id`, `.scar_pursuits`, `.scar_affiliations_held`, `.scar_affiliations_history` `sheet.py:187-193` | all four written positionally `sheet.py:203-209`; the three scar fields T-read (`test_rem30_character_sheet.py:174-176`) | **FP** ×4 as fields. The function is the finding: see X-T1 (`chronicle()` has no caller outside tests) | `sheet.py:196-209` |
| `MilitaryMenu.raise_` `military_menu.py:63` | written by keyword `:109`; read `:167-169` | **FP** | — |
| `ObligeeReading.tells_by_obligees`, `.tells_all`, `.attempted_by`, `.edges_since` `obligee_report.py:79-84` | written by `+=` (`:132`, `:137`) and item assignment (`:111`, `:142`) | **FP** ×4 | — |
| `MassBattleInput.loyalty_gain` `inputs.py:261` | written by keyword `seam/wrappers/mass_battle.py:273`; read `massbattle.py:560-561` | **FP** as a field. As a mechanism it is inert twice: see X-R4 | — |
| `BodyFall.body_after` `inputs.py:395` | written positionally `modules/settlements/subsist.py:76`; read `matter.py:702,709` | **FP** | — |
| `SubsistOutcome.short_by_person` `inputs.py:409` | written positionally `subsist.py:86`; read `matter.py:601` | **FP** | — |
| `FabricInput.live_works` `inputs.py:503` | written `world_q.py:619` (keyword) and `:639` (positional); read `modules/settlements/fabric.py:32-33` | **FP** | — |
| `Office.body_function` `carriers.py:1061` | written in `__post_init__` (`:1091-1092`) from `BODY_FUNCTION` (`data/rosters.py:1324`, `rosters.yaml: office_bodies.function`); **no reader of the field anywhere**, tests included. The comment eleven lines above states the criterion that deletes it ("an artifact nothing reads"). The roster map is a different object: Jordan asked for the type-of-office axis (`rosters.yaml:2188-2190`) and a test reads it (`test_season_shape.py:10017-10020`) | **DEAD** (batch D1): the stored field and its write only. `BODY_FUNCTION` and the `function:` map stay; a surface that shows what a body does reads `BODY_FUNCTION[office.body]` at the read, which is one owner instead of a copy per Office | `grep -rn "\.body_function"` → the write at `carriers.py:1092` and nothing else |
| `StubResult.io_contract` `stubwire.py:49` | written by keyword `:77`; T-read (`tests/valoria/test_stubwire.py:55`). The only caller of `stub_resolve` is the SC kernel (`wrapper.py:227`, `dictionaries.py:48`) | **DEAD with its caller**: when the kernel goes (SC disposition B), `engine/substrate/stubwire.py` has no caller and goes in the same batch with `tests/valoria/test_stubwire.py` (batch D3). Until then FP | `grep -rn stub_resolve` |
| `Order.waypoint_ref` `units.py:333` | **never written by anything**. `ally_at:D` is an accepted trigger kind (`units.py:309,336`), its payload is range-checked (`:349`), and `contact.py:106-110` evaluates it only `if order.waypoint_ref is not None`; so an `ally_at:` order is accepted, queued, never fires, and dams every order queued behind it (`contact.py:89-90`, the loop stops at the first unfired order) | **WIRE** (W1). `04_MB_manager_battle_one_resolver.md` §2 lists `ally_at:D` in the standing-order grammar it exports and validates, so the trigger is needed | probe P-1 |
| `Subunit.merged_cells` `units.py:434` | reset at `:1121` and `:1149`; nothing ever adds a cell to it and nothing reads it | **DEAD** (batch D1) | `grep -rn merged_cells modules` → declaration, a docstring word, two resets |
| `Subunit._order_idx` `units.py:516` | written by `+=` `contact.py:198` | **FP** | — |
| `Unit.officers` `units.py:2849` | written by keyword `armies.py:353`; T-read only; the declaration says "nothing at resolution time reads it" | **WIRE**, carried by `04_MB_manager_battle_one_resolver.md` §7 (the duel contact reads the unit's officer). No separate edit here; if §7 lands on the unit row's `officer` id instead, this tuple is then dead and leaves in that commit | `units.py:2845-2849` |
| `Unit.terrain_off_d`, `.terrain_def_d` `units.py:2856-2857` | written by `+=` `massbattle.py:419-422` | **FP** ×2 | — |
| `OrderOfBattle.drawn_from` `orderofbattle.py:104` | written positionally `armyrecord.py:271`; read `seam/wrappers/mass_battle.py:328` | **FP** | — |

### 1b. Retained oracles outside the loop (4 rows)

`systems/characters/sim/conviction.py` is retained by ED-IN-0283 and unreached by the loop
(`02_CHAR_audit.md` §6 row 27: keep); `systems/fieldwork/sim/knots.py` is an oracle the loop does not call
(`08_FI_audit.md` F-FI-07; `08_FI_08_knots-season-form.md` carries its season form).

| row | reading | decision | evidence |
|---|---|---|---|
| `ConvictionThresholdState.scar_counts` `conviction.py:164` | written `:260`; T-read `engine/tests/test_knots_ed912.py:146,148` | **FP** | — |
| `ConvictionThresholdState.destabilised`, `.any_crisis` `conviction.py:165,168` | written `:261,264`; read by nothing, tests included | **DEAD** ×2 (batch D1): two summary fields of a retained oracle; the retention covers the scar model, not a summary nobody takes | `grep -rn "\.destabilised\|\.any_crisis"` → 0 |
| `KnotState.ruptured` `knots.py:150` | written at eight constructor sites; T-read `engine/tests/test_knots_ed912.py:89-93` | **FP** | — |

### 1c. The social-contest kernel (28 rows): dead with the directory

`05_SC_sc05_kernel_disposition_B.md` retires `systems/social_contest/sim/contest/` whole and carries its
exchange game as the specification of `modules/social_contest/hearing.py`, whose outward record is
`HearingTurnView` (`05_SC_playable_hearing_B.md`:75), not `ContestView`. The row-level question is
therefore "does the carried design need this field", and the answer is recorded so the hearing does not
re-import a field no chooser ever read.

| rows | reading in the kernel | carried? |
|---|---|---|
| `ContestView.live_ground`, `.can_hard`, `.reserve_frac`, `.evidence_available` | written by keyword `resolver.py:275-281` (census FP); read by `policy.py` and `agon_harness.py` | the facts are carried, as `HearingTurnView.rung` / `.board`; the field names are not |
| `ContestView.appeal_axis`, `.my_standing`, `.opp_standing`, `.audience_learned`, `.audience_hostile` | written `resolver.py:275-280`; **read by no policy and not shown by the play harness** | **not carried.** A view field enters `HearingTurnView` only with a reader (a policy or the surface) |
| `HarnessState.consult_count` | `+=` at `agon_harness.py:153` (census FP) | not carried (a prompt counter of the retired harness) |
| `Style.canonical_flavor` | four literals, no reader | not carried: display text belongs to the surface's string table, not the resolver |
| `AdjudicatorType.mechanical_key`, `Proceeding.mechanical_key` | written, never read: the "binding" to `modes.CANONICAL_ADJUDICATORS` / `modes.PROCEEDINGS` is a comment | not carried |
| `Faction.fixed_lean` | never written; `faction.py:42` is a dead branch | not carried |
| `Chronicle.lead_changes`, `.turning_point`, `.decisive_appeal`, `.decisive_ground`, `.room_leader` (`narrative.py`) | written positionally `narrative.py:154` (census FP); read by `Chronicle.line()` | carried as derivations over `HearingOutcome.exchanges` (`05_SC_contest_record_on_event.md`), not as stored fields |
| `RhetoricalWeights` × 9 | read by `weight()` through `getattr(self, f"{appeal}_{tense}", 1.0)` (`primitives.py:206`) (census FP) | the 3×3 table is tuning; `13_SC_tuning_tables.md` is its home if the hearing keeps tense |

Decision for all 28: **DEAD**, deleted by SC disposition B's directory retirement (no separate batch; its
`FORK:` row covers them). Of the 28, 20 are census false readings inside a dead module and 8 are true
dead fields (the five unread view fields, the two `mechanical_key`s, `canonical_flavor`); `fixed_lean` is a
true never-written.

### 1d. Threadwork (13 rows): the consumer is the module host that does not exist yet

`09_WR_threadwork_module.md` moves `systems/threadwork/sim/` to `modules/threadwork/` behind typed
records; the season loop reaches none of it today (`09_WR_audit.md`:48, :281). Every "never read" here is a
result-record field whose only reader is a test, because the host adapter that would read it is unbuilt.

| row | reading | decision |
|---|---|---|
| `CoMovementCard.card_id` `co_movement.py:65` | written `:128,132`; read by nothing, tests included; `name` identifies the card | **DEAD** (batch D1) |
| `CoherenceFailureResult.present_displacement` `coherence.py:287` | written by keyword `:431` | **FP** |
| `MendingPrice.coherence_cost` `operations.py:458` | written by keyword `:490`; read `opposing.py:248-249`, `collective.py:193` | **FP** |
| `CoherenceFailureResult.just_transitioned` `coherence.py:284` | written `:428`; T-read. It is the edge ("first check to observe the failure") a host needs to emit one event rather than one per check | **WIRE**, carried by `09_WR_threadwork_module.md` (the host adapter reads it) |
| `OperationResult.net_successes` `operations.py:206` | written `:342`, `collective.py:216`; T-read. The host's degree owner grades `net` against `ob` (`dice_engine.degree_label`), the same methodology as `Margin` | **WIRE**, same carrier |
| `CollectiveResult.leap_results`, `.lattice_formed`, `.lattice_fractured`, `.operation_result` `collective.py:52-55` | written at three return sites; T-read through `test_threadwork_mending_parity.py:91-94` | **WIRE** ×4, same carrier (per-actor consequences are written by the host from `leap_results`) |
| `OpposingResult.a_degree`, `.b_degree`, `.a_consequences`, `.b_consequences` `opposing.py:71-76` | written `:266-268`; T-read | **WIRE** ×4, same carrier. Rule for the landing commit: an outcome field the adapter does not read at landing is cut in that commit, not carried inert |

**C2 totals (72):** FP 25 · DEAD 35 (28 with the kernel; 6 in batch D1: `pool_size`, `body_function`,
`merged_cells`, `destabilised`, `any_crisis`, `card_id`; 1 in batch D3: `io_contract`) · WIRE 12 (1 new
edit, W1; 11 carried by named proposals) · LABEL 0. Census misreadings inside the dead kernel are counted
DEAD, not FP.

## 2. C3 — registry keys no code names (14 rows)

| rows | reading at the loader | decision | evidence |
|---|---|---|---|
| `venues.yaml` `quarters.{City, Cathedral-City, Fortress-City, Fortress, Town, Village}` and `buildings.{same six}` (12 rows) | read by subscript on the geography file's `type:` value: `ven["quarters"][kind]`, `ven["buildings"][kind]` (`harness/populated.py:1197,1201`), with a refusal for a type that has no row (`:1191-1195`) | **FP** ×12 | the key is a data value, never a literal in code |
| `venues.yaml` `seats.Parliament` | iterated: `ven["seats"]` (`populated.py:1283`), and cross-checked against `seat_precedence` with a refusal (`:239-250`) | **FP** | — |
| `rosters.yaml` `knowledge_kinds` | **true: nothing reads it**, and the roster says so itself (`rosters.yaml:1763-1777`: "no code reads this roster, so `thread_substrate` gates nothing yet", H-85). No claim, record or subject carries a kind for it to gate over. `12_ARCS_adjudication.md` row 19 relies on it as "the owner; the gate applies to the kinds it names" with an `[UNVERIFIED: roster not opened at the row]` mark; opened here, it gates nothing | **WIRE** (W3): the cases that need the distinction are NPC-086 N3, NPC-087 N2, NPC-088 N6 (ARCS row 19) | `grep -rn knowledge_kinds engine modules tools tests references` → the roster and the H-85 row only |

**C3 totals (14):** FP 13 · WIRE 1.

## 3. C5 — hole-register pointers (16 rows as given; 837 pointers re-derived)

**The census read the wrong tree.** `census.py` resolved a pointer by `ROOT / p`, and when that failed (the
register writes paths relative to `engine/season/`: `loop/effects.py`, `queries/person_q.py`), fell back to
the first file of that basename anywhere under the repository (`ROOT.rglob(basename)[:1]`). That landed on
a locked, stale worktree (`.claude/worktrees/agent-a737f996de1fa4752`, at `1424aa7`) or on an unrelated
file of the same name (`proposals/2026-08-31-shape-tracer/tracer/probes.py`). Eleven of the 16 rows were
therefore checked against a file that is not the game, and pointers that resolve in the stale copy but not
in the working tree were not flagged at all. **C1 is exposed to the same defect only if it walks the same
roots; it walks `engine`, `modules`, `systems`, `tools`, `references` (`census.py:17-29`), not `.claude/`,
so it is not.** Re-derived here against the working tree, resolving relative to `engine/season/` first
(`scratchpad/census_rest/c5.py`; 837 `site:`/`owner:` pointers).

`site:` and `owner:` are read by code for non-emptiness only (`harness/register.py:215`); every correction
below is text.

### 3a. The 16 rows as given

| row | reading in the working tree | decision |
|---|---|---|
| H-72 `site` `queries/readers.py` | no such file; `LedgerReader` is `queries/person_q.py:994` | **LABEL** |
| H-138 `owner` `tests/test_season_shape.py:8103-8112` | the `norm` helper is at `:11363` and `:11445`; the same field's `loop/effects.py -- _eff_transfer` is `loop/effects_economy.py:215` | **LABEL** (both) |
| H-148 `site`, H-152 `owner` `loop/effects.py::_eff_march` | `loop/effects_combat.py:451`; `effects.py` neither defines nor re-exports it | **LABEL** ×2 |
| H-155 `site` `witness.py:189` | the `isinstance(held.value, (int, float))` branch is `witness.py:220` | **LABEL** (cite the function, drop the line) |
| H-207 `owner` `decision/options.py::aggregate_questions` | `decision/questions.py:54` | **LABEL** |
| H-210 `owner` `workplans/valoria_master_workplan_v9_part6.md` | retired, `FORK:c1374059` (`restructure_ledger.md:3015`) | **LABEL** |
| H-230 `owner` `workplans/valoria_master_workplan_v9_part5.md` | retired, `FORK:c1374059` (`:3014`) | **LABEL** |
| H-238 `owner` `workplans/valoria_master_workplan_v9.md` §0.5 | retired (`:3010`); the rule it cites is carried at `workplans/valoria_master_workplan_v11.md:40` (P9) | **LABEL** |
| H-220 `owner` `harness/probes.py::Ev` | exists: `engine/season/harness/probes.py:326`. The census opened another `probes.py` | **FP** |
| H-224 `owner` `decision/choose.py::unrest_pull` | absent on purpose: the row records that it "was built and REVERTED at B-U's close" | **FP** (the pointer names a reverted symbol and says so) |
| H-357 `owner` `queries/person_q.py::lie_said_of` | exists: `:1236` | **FP** (stale worktree) |
| H-358 `owner` `queries/person_q.py::heritage_regard` | exists: `:468` | **FP** (stale worktree) |
| H-361 `site` ×3 `_eff_marshal`, `standing_order`, `_fanned_choices` | exist: `effects_information.py:340`, `world_q.py:2300`, `options.py:1343` | **FP** ×3 (stale worktree) |

### 3b. What the corrected resolution adds (rows the census missed)

One cause covers most of them: `loop/effects.py` was split into `effects_{army,combat,economy,founding,governance,information,migration,shared}.py`,
and the register still names the old file. `effects.py` re-exports three names (`_renewals`,
`_oblige_term`, `_eff_kill`; `effects.py:85,101-102`), so those pointers still import; the rest do not.

| row · field | pointer | defined at | decision |
|---|---|---|---|
| H-152 `site` | `loop/effects.py::_eff_march` | `loop/effects_combat.py:451` | **LABEL** |
| H-140 `owner` | `effects.py` `_eff_move` | `loop/effects_migration.py` | **LABEL** |
| H-156 `owner` | `effects.py` `_eff_commit` | `loop/effects_information.py` | **LABEL** |
| H-43 `default` | `effects.py` `_eff_petition` | `loop/effects_information.py` | **LABEL** |
| H-105 `hole`, H-164 `hole` and `owner` | `effects.py` `_rise` | `loop/effects_economy.py` | **LABEL** ×3 |
| H-158 `site`, H-174 `owner` | `loop/effects.py::_renewals` | `loop/effects_economy.py:321` (re-exported) | **LABEL** ×2 (name the owner, not the re-export) |
| H-159 `site` | `loop/effects.py::_oblige_term` | `loop/effects_shared.py:93` (re-exported) | **LABEL** |
| H-126, H-245, H-246, H-247 `site` | `seam/wrappers/sigma.py::faculty` | `seam/wrappers/pool.py:78` | **LABEL** ×4 |
| H-245 `owner` | `seam/wrappers/sigma.py::register_pool_addend` | `seam/wrappers/pool.py:41` | **LABEL** |
| H-172 `owner` | `decision/options.py::belief_contradicts` | `epistemic.py:72` | **LABEL** |
| H-174 `owner` | `queries/world_q.py::home_of` | `state/containment.py:73` (imported by `world_q`) | **LABEL** |
| H-79 `site` | `loop/driver.py::SeasonDriver.witness` | `loop/witness.py:339`, bound onto the class at the foot of `driver.py` (`:574-585`) | **FP** (bound, as the file says) |
| H-213 `owner` | `seam/wrappers/sigma.py::_obstacle_of` | deleted; the row says "was deleted at this step" | **FP** |
| H-127, H-150, H-175, H-240, H-312, H-358 | a bare filename after its full path was given once in the same field | resolve | **FP** ×6 |
| H-153 `site`, H-222 `owner` | `19_PLAN.md` | `proposals/2026-09-05-proceedings-subsystem/19_PLAN.md` (unique by basename) | **FP** ×2 |

**C5 totals:** as given 16 → LABEL 9 · FP 7. Added by the corrected resolution 28 → LABEL 17 · FP 11.
Exact replacement text: `proposals/17_CENSUS_REST_3_corrections.md` §A.

## 4. C6 — composition and contract targets (0 rows as given; verified, then extended)

**The empty table is correct for what it measured.** Every `target:` in
`references/module_contracts.yaml` was imported and its symbol taken with `getattr`: 16 targets, 0
failures; `python tools/export_composition.py --check` → `OK — 16 role(s), every target resolved; wiring
valid for 26 module(s)` (probe P-2). The census checked `target:` keys only. The same file's `modules:`
block (26 rows) is where the pointers that do not resolve are:

| row | reading | decision | carried by |
|---|---|---|---|
| `combat` `wiring.build: unwired`, and its note | false. `combat.fight` is a registered `verb_call` entry (`module_contracts.yaml:58-62`) and `fight` executed 13 times in the corpus run (seed 0). The note describes a campaign driver, `DISPATCH_COMBAT_BRIDGE`, `scene_slate.queue_scene`, `combat_bridge.py:37` and `scene_dispatch.py:37`, none of which exists | **LABEL** | correction C-1 |
| `mass_battle` `sim_module:` absent ("until the MB lane adds it"), note names `systems/mass_battle/sim/massbattle.py` as LIVE | the code is `modules/mass_battle/` (`composition_roles: mass_battle.resolve_field`); the note carries two `[SUPERSEDED]` bracketed corrections after a body that is false | **LABEL** | correction C-2 |
| `social_contest` `sim_module: systems/social_contest/sim/contest/`, note "reached live only via emergency_council" | the registered module is `modules/social_contest/roll.py`; `emergency_council` does not exist | **LABEL** | `05_SC_sc05_kernel_disposition_B.md` edit 1 (its row edit); no second edit here |
| `threadwork` `sim_module`, `fieldwork` row, the retired-faction rows, 20 `parity: key-log` values | stale | **LABEL** | `09_WR_B_pointer_text_for_the_orchestrator.md`; `08_FI_04_small-edits.md`; `06_FA_hygiene.md` §5; `11_GO_pointer_and_stale_text_resolutions.md` row 8 |
| 18 rows with `sim_module: none` (`faction_state`, `npc_behavior`, `npc_memory`, `territorial_piety`, `scene_slate`, `game_director`, `scene_timer`, `audit`, `domain_actions`, `settlement_layer`, `settlement_economy`, `ci_political`, `victory`, `faction_politics`, `miraculous_event`, `scenario_authoring`, `clock_registry`, `campaign_architecture`) | each is a contract (`state:`, `transitions:`, `loops:`, `resolver:`) for a module with no code, and each says so in its own fields (`sim_module: none`; `wiring.build: design` or `deferred`). Six notes narrate code "deleted at `28-iii`/`29b`/`29c`/`29d`". Nothing the game or the port reads opens these rows: the port gate reads `composition_roles:` (`11_GO_port_gate_order_and_coverage.md`:73) | 16 rows **FP** (a document that describes absent code and declares it absent is not mislabelled; the stale narration in their notes is accepted and nothing is written, CLAUDE.md §0.1 pt 5). 2 rows **DEAD**: `settlement_economy` and `campaign_architecture` carry `godot: retire`, `port_rank: 9`, and their own notes call them "phantom" and "a consolidation doc, not a runtime module"; nothing joins either by `with:` | deletion batch D4 |
| 19 path strings in `notes:`/`sources:` that name files which do not exist (`engine/autoload/game_state.py`, `engine/cross_scale/echo_transport.py`, `engine/params/core.md`, `systems/combat/sim/combat.py`, `systems/factions/sim/mass_seizure.py`, `systems/overview/sim/accounting.py`, `tests/valoria/test_faction_l_reconstruction.py`, `tests/valoria/test_public_governance_transfer_key.py`, 11 others) | history written into a registry's notes; none sits in a field a tool resolves (`doc:`, `sim_module:`, `target:` all resolve or are `none`) | accepted, nothing written, except the two inside the `combat` and `mass_battle` rows (C-1, C-2), which a port decision would read | — |

**C6 totals:** as given 0, confirmed 0 by import. Added in the `modules:` block: LABEL 2 new (C-1, C-2)
plus 4 groups already carried by named proposals · DEAD 2 contract rows (D4) · FP 16.

## 5. C4 — event kinds (0 rows as given; the table is empty because the script matched nothing)

**Why the table is empty.** `census.py:136` looks for `emits = "kind"` in Python and
`census.py:142` for `emits: kind` in YAML. Effects do not name a kind that way (the fold emits the verb
row's kinds), and `verb_table.yaml` writes `emits: ["petition.carried"]`, a list, which
`emits:\s*["']?([\w.]+)` does not enter. The script printed `C4 0 of N` over a near-empty `emitted` map.
Re-derived here from the code's own roster, `data/verbs.py::EVENT_KINDS` (178 kinds: every emission
column of the verb table, the write matrix's `emits:`, `fold_kinds`, `logged_kinds`), against (a) the
Event log of a realm run and (b) every kind-specific consumer (`scratchpad/census_rest/c4.py`).

**Instrument.** `python -m engine.season.harness.aperture 3 0` (realm, seed 0, 3 seasons, 83 persons;
its control line reads `content_hash EQUAL`), `PYTHONHASHSEED=0`. One seed, three seasons: every "never
emitted" below is a count in that run, not a claim that the kind cannot fire.

**What counts as a consumer.** Four layers, and the census must not confuse them:
1. *generic*: WITNESS deposits every Event as claims in the ledgers of those who perceive it; every kind
   has this consumer unless `undeposited_kinds` names it;
2. *by derived class*: `REFUSAL_KINDS`, `DEED_KINDS`, `PAIRED_KINDS`, `_KIND_STRATA`, `DOCKETING_KINDS`
   (`data/verbs.py:1489-1492`, `queries/person_q.py:226-232`, `queries/world_q.py:350`) read a kind
   through its verb row, without naming it;
3. *by roster*: `strife_kinds` (opens / joins / never / concludes), `standing_routes.kinds.dominance`,
   `covert_kinds`, goal-stage rows in `goals.yaml`;
4. *by name*: a string literal in `queries/`, `loop/`, `decision/`, `state/`, `epistemic.py`.

| class | kinds | reading | decision |
|---|---|---|---|
| emitted in the run and named by a layer 3–4 consumer | 35 | live both ends | — |
| **A.** emitted, no layer 3–4 consumer | 43 | 34 are refusal kinds (`*.refused`, `*.unauthorized`, `*.impossible`, `travel.blocked`, `speech.unheard`): consumed at layer 2 as `REFUSAL_KINDS` and by the instruments (`aperture`, `obligee_report`, `scarce`). 9 are not: `body.tended`, `case.opened`, `cover.assumed`, `faction.surveyed`, `matter.held`, `matter.turned`, `news.untold`, `proposition.uttered`, `pursuit.moved`; `case.opened` is in `DOCKETING_KINDS` (layer 2), the rest reach the game only as claims (layer 1) | **FP** ×43 as "no consumer": layer 1–2 is a consumer. Whether a *refusal* should be seen by anyone but the refused is `01_CORE_reason_trail_in_the_act_store.md`'s question, not a census row |
| **B.** named by a layer 3–4 consumer, never emitted in the run | 39 | the consumer waits on an Event that did not occur. 23 of the 39 sit in `strife_kinds`; of that roster's nine `opens` kinds, eight did not occur (`field.won`, `rung.seized`, `rung.razed`, `record.seized`, `arrest.made`, `compliance.withheld`, `requisition.taken`, `site.damaged`), so in this run a strife could open on `field.lost` and nothing else. Each traces to a verb in §6's never-executes set (`seize`, `raze`, `arrest`, `comply`/`evade / defy`, `requisition`, `sabotage`) or to a march that was not won | **WIRE**, carried by the verb build-outs (§6); no edit to the consumers. Evidence that the consumers are correct and starved: `09_WR_story_instruments_that_can_fail.md` |
| **C.** never emitted, no layer 3–4 consumer | 61 | 27 are refusal kinds of verbs never attempted; 21 are deed kinds of verbs that never execute (`accept.declared`, `bond.formed`, `capability.raised`, `challenge.issued`, `compliance.given`, `confession.*` ×4, `fight.declared`, `capture.declared`, `place.surrendered`, `order.marshaled`, `siege.pressed`, `site.worked`, `site.restored`, `matter.*` ×3, `contest.undecided`, `arrest.resisted`); 4 are the fold's and the log's own kinds (`act.ineligible`, `act.refused`, `attempt.refused`, `standing.band_crossed`); **9 are declared by the write matrix and have no emitter anywhere** (below) | per kind, below |

### 5a. Nine kinds the write matrix declares that nothing can emit

The gate requires a MATTER-class write to name one of its row's declared kinds
(`state/world.py:1344-1356`, D22 / H-12). It does not require that of an ACTS-class write: the fold
passes `emits=None` and the act's own Event carries the verb row's kind. So for a cell written only at
RES/ENC the matrix's `emits:` is a list of *permitted* kinds, and a kind no verb row lists and no writer
passes is vocabulary that cannot occur. Measured by wrapping `World.write` over the same run
(`scratchpad/census_rest/writes_probe.py`; hash `52ff67bc45c5b956cd99215f6ba3097f`, 30 of 42 matrix
rows written, 0 unrowed writes):

| matrix row | declared kind | gate writes in the run | Events of that kind | emitter in code | decision |
|---|---|---|---|---|---|
| `(Person, scar)` | `scar.taken` | 883 | 0 | none (`resolve.py::_scar_witnesses` passes no `emits`) | **WIRE**, carried by `11_GO_player_surface_contract.md` §4 and `02_CHAR_scar_is_a_wound.md`. Correction to §4's wording: the row already declares `scar.taken`; the edit is `emits=` at the writer, not a new row entry (correction C-5). 883 writes in three seasons is the volume `02_CHAR_scar_cap_and_regard_unit.md` measures; the Event must land after that proposal's cap, or it publishes 883 Events |
| `(Person, conviction)` | `conviction.moved` | 2 | 0 | none (`_conviction_crisis`) | **WIRE**, same carrier |
| `(Person, weight)` | `weight.changed` | 0 | 0 | none; CENSUS writes no weight | **WIRE**, carried by `07_SE_population_census.md` |
| `(Person, coherence)` | `coherence.changed` | 0 | 0 | none; `Person` has no `coherence` field; the gate admits only the driver `Seam` (`world.py:1305`) | **WIRE**, carried by `09_WR_threadwork_module.md` |
| `(Record, ttl)` | `record.expired` | 0 | 0 | none; `Record.ttl` has no writer and no reader (`world_q.py:2304`) | **DEAD**, with `08_FI_04_small-edits.md`'s deletion of the field and row; its dependants are batch D2 |
| `(Record, stages)` | `record.staged` | 370 | 0 | none | **FP** as a defect: the write rides the act's own Event (`record.created`, `petition.carried`); under the gate's reading (permitted kinds) nothing is wrong, and no consumer names the kind. H-86 already registers the column's ambiguity |
| `(ConveningCondition, attached)` | `condition.attached` | 17 | 0 | none | see X-R1: the value written has no reader either |
| `(Rung, envelope)` | `envelope.changed` | 0 | 0 | none; "the ratified-but-unwritten field" (`world_q.py:1803-1807`) | accepted, nothing written: `04` §A.2's `loop/census` row names `envelope`, so the row stays; no proposal in the suite gives it a writer `[UNVERIFIED: 07_SE proposals searched by name only]` |
| `(Tenure, degree)` | `tenure.graded` | 0 | 0 | none; `degree` is set at the edge's construction (`effects_information.py:700-702`) and never re-graded | accepted: `05_SC_arrangement_rows_that_bind.md` decides what the band does |

**The trap this leaves, and its resolution.** `EVENT_KINDS` is what the import-time checks hold a
consumer roster to (`_check_strife_kinds`: "a kind in any list absent from `EVENT_KINDS`"). A roster may
therefore name a kind that cannot be emitted and import cleanly. None does today (the nine have no layer
3–4 consumer). Two near-cases do exist and are narrower than they look: `strife_kinds.joins` and
`.concludes` name `tenure.opened`, which only `confer` emits (0 Events) while `Tenure.since` was written
178 times; `strife_kinds.never` names `stance.moved`, which only `forgive` emits while `(Person, stance)`
was written once without it. Decision: no new check (CLAUDE.md §0.1 pt 5: a roster of an instrument is
process); the two rows are reported to the WR lane as readings (correction C-6).

**C4 totals:** as given 0. Extended over 178 kinds: FP 43 (class A) + 2 · WIRE 39 (class B, carried) + 4
(5a, carried) · DEAD 1 (`record.expired`) · accepted without edit 2 · class C's other 52 (27 refusal
kinds, 21 deed kinds, 4 fold and log kinds) follow their verbs (§6).

## 6. Extended — verbs with no predicate/effect, or that never execute

**Instruments.** `python -m engine.season.harness.corpus_run 0` (143 cases, seed 0, seasons from
`temporal.span_seasons`; exit 0) and the realm run of §5. `register --requirements`: R-05 `not_met`
(met 3 · partial 5 · not_met 1).

| | corpus (143 worlds) | realm (1 world, 3 seasons) |
|---|---|---|
| executed at least once | 23 | 30 |
| attempted, always refused | 13 | 18 |
| formed or foldable, never attempted | 30 | 7 formed-never-attempted + 12 never formed |
| no predicate/effect | 1 (`tie / knot`) | 1 (`tie / knot`: formed for 83, offered to 0) |

Union: **33 of 67 verbs execute in at least one of the two instruments; 34 execute in neither.**

| group | verbs | deciding read (realm, per refused act) | owner |
|---|---|---|---|
| no effect | `tie / knot` | `resolvable_verbs()` excludes it | `08_FI_08_knots-season-form.md` |
| never formed for anyone in the realm, never attempted in the corpus (11) | `assign_troops`, `disband_unit`, `discharge_troops`, `form_unit`, `order_unit`, `recruit`, `marshal`, `surrender`, `succeed`, `interrogate`, `destroy_record` | no candidate: nobody holds an army record, a detainee, a vacancy claim or a record to destroy | `14_VERBS_MILITARY.md`; `14_VERBS_BINDING.md`; `06_FA_seat_terms_and_turnover.md` (`succeed`) |
| formed, never attempted (6) | `arrest` (2 formed), `confer` (6), `examine` (1), `forgive` (2), `restore` (1), `work` (1) | ranked below the budget line every time | `14_VERBS_BINDING.md`, `14_VERBS_PHYSICAL.md`, `14_VERBS_MATERIAL.md`, `14_VERBS_SOCIAL1.md` |
| attempted, always refused (16) | `accept` (45 refused: `exists:challenge=0`), `build` (4: `exists:works=0`), `comply` (47), `construe` (10), `evade / defy` (8) (all three: `exists:dispensation=0`), `covenant` (18: `exists:Proposition=0`), `determine` (3: clause `docket` 2, `party` 1), `exchange` (79: 37 post-admission), `found` (7: `exists:works=0`), `pardon` (3, all post-admission: `bench=True`), `raze` (22; 21 post-admission), `requisition` (5: clause `authority`), `revoke` (6: no read recorded), `sabotage` (47: `exists:Site=0`), `seize` (14, all post-admission: clause `write`), `train` (119; 24 post-admission) | as listed | the `14_VERBS_*` lane for the verb's stratum |

Two things the table shows that a per-verb reading hides:

1. **Wrong-referent formation is the largest single cause.** `exists:<K>=0` decided 402 of 1,440 refused
   acts: the chooser formed `accept` on something that is not a challenge 45 times and `comply` /
   `construe` / `evade / defy` on something that is not a dispensation 65 times. The verb is built; its
   candidate is not. Carried by `14_VERBS_SOCIAL1_A_formation.md` and
   `14_VERBS_SOCIAL2_A_formation_on_what_is_known.md`.
2. **Post-admission refusal with no reason on the Event.** 304 refused acts cleared every recorded read
   and were refused in the effect; for `seize` (14 of 14), `pardon` (3 of 3) and `raze` (21 of 22) that
   is every refusal. A verb that always clears its `requires` and always fails in its effect is a broken
   wire, not a hard precondition. Carried by `01_CORE_predicates_name_their_clause.md` (the reason) and
   the verb's lane (the effect).

Decision for the 34: **WIRE**, all carried; this census adds no verb edit. It adds the measurement that
ties them to §5 class B (the 39 consumers waiting on kinds these verbs emit).

## 7. Extended — records written and never read (write matrix, writers followed to readers)

`write_matrix.yaml` has 42 rows and no readers column. Writers were counted at the gate (§5a's probe);
readers by attribute and key reads in `queries/`, `decision/`, `loop/`, `state/`, `seam/`, `epistemic.py`
and `modules/` (harness excluded, since an instrument is not the game).

| id | row | written (run) | read by | decision |
|---|---|---|---|---|
| X-R1 | `(ConveningCondition, attached)`: `date["convening_attached"] = True` (`loop/effects_governance.py:457`) | 17 | **nothing, tests included.** The "condition" is the constant `True`; CALENDAR fires the Date without consulting it | **WIRE**, carried by the Papacy lane's `quorum_share:` arrangement key (`audits/15_INSTITUTIONS_PAPACY.md` proposal B): the value CALENDAR tests before `date.fired` is what this cell holds. Until that lands the write is inert; if B is not adopted, delete the key, keep the Layer 1 row (W5 states both) |
| X-R2 | `(Record, ttl)` | 0 | nothing | **DEAD** (`08_FI_04`; dependants D2) |
| X-R3 | `(Rung, envelope)` | 0 | one query that explicitly declines to count it | accepted (§5a) |
| X-R4 | `MassBattleInput.loyalties` × `loyalty_gain` (C2 row; not a matrix cell) | every field | read (`massbattle.py:560-561`) and **0 by construction twice**: the `field_morale_loyalty_gain` fixture ships `0` (`data/fixtures.py:771`, H-148's control), and since CR-87 (5) no built realm holds a loyalty row toward a creed's utterer, so `loyalties` is `(0.0, 0.0)` whatever the gain (`inputs.py:228-229`, H-256) | **WIRE**, carried by `04_MB_typed_outcome_and_one_path.md` and CR-88's betrayal reading (H-256 `unblocks:`); sweeping the gain while the stance term is identically 0 is a fake control (CLAUDE.md §7) and is recorded as such |
| X-R5 | `(DocketItem, arrangement)`, `(DocketItem, petition)` | 11 each | `effects_information.py:421`, `predicates.py:558`, `matter.py:452` | **FP** (dict keys `DOCKET_ARRANGEMENT` / `DOCKET_PETITION`, not attributes) |
| X-R6 | twelve rows not written in the run: `Act[].returned`, `Person.body_ceiling`, `Person.coherence`, `Person.exists`, `Person.weight`, `Record.subject_matter`, `Record.ttl`, `Rung.dates`, `Rung.envelope`, `Site.exists`, `Tenure.degree` and `Proposition.*` | 0 | — | `body_ceiling`, `Person.exists`, `subject_matter`, `Site.exists` have writers that this run did not reach (no fight, no death, no army, no `build`); `Rung.dates` `[UNVERIFIED: writer not located; `convene` writes `(Date, due_at)`]`; `Act[].returned` and `Proposition.*` are declared write-less. The other five are §5a's. **FP** ×6, 1 unverified; no row here is new |

Every other row has both a writer that ran and a reader in game code.

## 8. Extended — closed rosters with no loader refusal

`rosters.yaml` holds 127 named rosters and tables (`scratchpad/census_rest/rosters_probe.py`). 125 are
loaded by name in game code. The textual probe flagged 26 as "loaded, never used for membership"; the 22
opened at their use sites are, with one exception, uses or refusals the regex could not see (a multi-line
`require_member(`, a `_check_*` at import, a destructuring assignment); four were not opened
(`order_roles`, `modules`, and the tables `pursuit_projection`, `alignment`: each has 8 or more uses).
What is left:

| roster | reading | decision |
|---|---|---|
| `knowledge_kinds` | no loader, no reader (§2) | **WIRE** (W3) |
| `ladder_rungs` | loaded into `LADDER_RUNGS` (`data/rosters.py:868`), which no game code uses. `arrangements.yaml: speech_kinds` "reuses" its six ids (`arrangements.yaml:62`), and the only thing holding the two equal is a test (`tests/test_arrangements.py:89`); `data/arrangements.py` refuses an unknown genre, band, proof and interposed kind (`:140-194`) and not an unknown or missing speech-kind id | **WIRE** (W2): the equality moves from the test into the loader, the one licensed place (CLAUDE.md §0.05: "the loader's refusal per data family"). `05_SC_playable_hearing_B.md` renames what this roster is for (`audits/05_SC_audit_addendum_B.md` G-46: "the issue ladder is absent and its name is on the charge ladder"); the refusal is written against whichever name that edit leaves |
| `witness_channel_predicates` | holds a `predicates:` map of prose meanings for the five channels; the predicates themselves are functions (`epistemic.py::_ch_*`), keyed by `witness_channels`. Read by one test (`test_season_shape.py:4818`) for set equality with the channel names | **FP**: reference text beside H-33's row; nothing claims it is a mechanism |
| `venues.yaml` rows | a building row is read by subscript (`b['slug']`, `b['quarter']`); a missing key raises `KeyError`, an unknown key is ignored | accepted: authored-for-play data with one consumer (the realm builder); no proposal in the suite authors venues by hand |

## 9. Extended — tests that exercise code nothing calls

Module-level only; the symbol-level sweep is C1's. A cluster is listed when its only importers are
tests (sibling lane's import graph, `scratchpad/modlive.json`, re-checked here by grep at each row).

| id | code | tests | reading | decision |
|---|---|---|---|---|
| X-T1 | `engine/season/decision/sheet.py` (`creation_sheet`, `seat`, `development_space`, `take_ranked`, `chronicle`) | `test_rem30_character_sheet.py`, `test_g2_token.py`, `test_cr20_attributes.py` | the player's seat ships switched off (`person_id=None`); no harness or loop code calls any of the five. The tests are real (they run the season with the arm on and compare hashes) | **WIRE**, carried by `11_GO_player_surface_contract_B.md` and `01_CORE_one_scene_contract.md`; `chronicle()` in particular has no caller that is not a test |
| X-T2 | `systems/threadwork/sim/{coherence,operations,collective,opposing}.py` | 6 files under `tests/valoria/`, 1 under `engine/tests/` | an oracle with tests and no host | **WIRE**, `09_WR_threadwork_module.md`. `co_movement.py` and `threadcut.py` have neither test nor caller; they move or die in that proposal's commit, and `CoMovementCard.card_id` dies either way (D1) |
| X-T3 | `systems/social_contest/sim/contest/` (16 files) | `_kernel_tests.py` and the test importers that proposal lists | retired by ruling (ED-SC-0033 cl. 2) | **DEAD**, `05_SC_sc05_kernel_disposition_B.md` |
| X-T4 | `engine/substrate/stubwire.py` | `tests/valoria/test_stubwire.py` | its only callers are in X-T3 | **DEAD** with X-T3 (batch D3) |
| X-T5 | `systems/characters/sim/conviction.py`, `systems/fieldwork/sim/knots.py` | `engine/tests/test_knots_ed912.py`, `tests/valoria/test_knot_pool_formula.py`, `test_conviction_roster_single_owner.py` | retained oracles (ED-IN-0283; `02_CHAR_audit.md` §6 row 27; `08_FI_audit.md` R-14) | **FP**: kept on purpose, and each audit says so |
| X-T6 | mass-battle order features: `signal:NAME` triggers and `Unit.fired_signals`; `build_army(officers=…)`; `ally_at:D` | `test_mass_battle_signals.py`, `test_mass_battle_officers.py`; `ally_at` has no test at all | production constructs none of the three (`units.py:2843`: "no … production code constructs a 'signal:' trigger"; `armies.py:115` default `officers=()`) | **WIRE**: `04_MB_manager_battle_one_resolver.md` §2 (the standing-order grammar and `fire_signal`) and §7 (officers); `ally_at` is W1 |
| X-T7 | `modules/combat/*` shown as tests-only by the import graph | — | reached by path, not import: `engine/substrate/pc_engine.py` is the one `PATH_SEAM_ALLOWED` seam, and `combat.fight` is a registered entry | **FP** of the graph |

## 10. Extended — documents that describe code that does not exist

A scan of 916 tracked live files (everything but `.designs/`, `.audit/`, `proposals/`, `registers/`,
`research/`, `workplans/`, the restructure ledger and `_history` files) for path strings under
`engine/`, `modules/`, `systems/`, `tools/`, `tests/` that do not resolve found 530 in 140 files. That
number is a ceiling, not a count of defects: the register and the verb table write `tests/test_x.py`
relative to `engine/season/` (those two files hold 116 of the 530), tests name fabricated paths on purpose, and tools and
indexes name a retired file in order to say it is retired (`CURRENT.md:37-40`, the workflow's comments).
Opened at the line:

| id | document | claim | reading | decision |
|---|---|---|---|---|
| X-D1 | `engine/season/write_matrix.yaml:4`, `:28-31` | "`engine/season/shape.py`'s `write()` gate reads it"; "`python engine/season/register.py --verify-write-matrix` re-extracts and fails on drift" | `shape.py` does not exist (the gate is `state/world.py::World.write`); `harness/register.py` has five flags (`--check`, `--counts`, `--verify-citations`, `--rule`, `--requirements`) and no `--verify-write-matrix`; the string occurs nowhere else in the tree. The header of a file the gate reads at runtime asserts a drift check that does not exist | **LABEL** (C-3) |
| X-D2 | `references/module_contracts.yaml` `combat`, `mass_battle` rows | §4 | **LABEL** (C-1, C-2) |
| X-D3 | `engine/season/hole_register.yaml` `site:`/`owner:` | §3 | **LABEL** (26 pointers) |
| X-D4 | `architecture/PLAN.md:564-717`, `00_ADOPTION_README.md:27`, `ARCHITECTURE_V2.md` | `engine/season/register.py`, `engine/season/shape.py` | Layer 1 names files that were split into `harness/register.py` and `state/`. Layer 1 is not edited to match code (CLAUDE.md §0.05); these are plan-history paths inside ratified documents | accepted, nothing written; `11_GO_pointer_and_stale_text_resolutions.md` is the suite's home for pointer text and already lists what the orchestrator may touch |
| X-D5 | `references/what_valoria_is_and_what_runs.md` (11 dead paths: `systems/factions/sim/faction_action.py`, `crown_initiative.py`, …) | describes the retired campaign driver | `[UNVERIFIED: not opened past the path list]` | reported to the orchestrator: a document titled "what runs" naming eleven files that do not exist is a currency hazard; its disposition is not a census edit |
| X-D6 | `engine/season/harness/arms.py`, `tests/valoria/test_balance_oracle_arms.py` (18 mentions of `tools/balance_oracle.py`) | name the retired instrument | they name it as retired (CLAUDE.md §7) | **FP** |

<!-- APPEND -->

