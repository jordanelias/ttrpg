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
dict field, or `getattr(self, f"{a}_{b}")`. 22 of the 72 rows are that and nothing else. Of the other 50,
28 sit in `systems/social_contest/sim/contest/`, which `05_SC_sc05_kernel_disposition_B.md` retires whole;
13 sit in `systems/threadwork/sim/`, which `09_WR_threadwork_module.md` moves to `modules/threadwork/`;
and 9 are decided here on their own.

Decision codes: **FP** false positive · **DEAD** delete · **WIRE** broken, wire · **LABEL** correct text.
"T-read" = read by a test only.

### 1a. Engine and modules (25 rows)

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
| `Office.body_function` `carriers.py:1061` | written in `__post_init__` (`:1092`) from `BODY_FUNCTION` (`data/rosters.py:1324`, `rosters.yaml: office_bodies.function`); **no reader anywhere**, tests included. The comment eleven lines above states the criterion that deletes it ("an artifact nothing reads") | **DEAD** (batch D1): the field, the `:1091-1092` write, `BODY_FUNCTION`. The `function:` map in `rosters.yaml` goes with it unless `06_FA_seat_terms_by_body_B.md` lands a reader first; the quoted cells are in `.designs/` and in the roster's `source:` line | `grep -rn "body_function\|BODY_FUNCTION"` → 4 lines, all owner or writer |
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

**C2 totals (72):** FP 22 · DEAD 34 (28 with the kernel, 6 in batch D1 incl. `io_contract` in D3) ·
WIRE 12 (1 new edit W1; 11 carried by named proposals) · residual census FPs inside the dead kernel are
counted DEAD, not FP.

<!-- APPEND -->

