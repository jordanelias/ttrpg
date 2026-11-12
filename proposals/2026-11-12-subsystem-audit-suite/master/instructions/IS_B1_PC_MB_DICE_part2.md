# Instruction suite, lane IS-B1 — part 2: mass battle (MB), the dice (DICE), the tables v12 takes, limits, evidence

## Status: PROPOSED (part 2 of `master/instructions/IS_B1_PC_MB_DICE.md`; nothing here is applied; resolves nothing at runtime)

Read part 1 first: its §0 gives the item form, the words (A-98; `unified/MB_LEXICON.md` for the army and the battle) and the four probes P-1 to P-4 this part cites. Short names used in both parts: **PB** is `proposals/03_PC_duel_round_and_approach_B.md`; **GO-B** is `proposals/11_GO_player_surface_contract_B.md`; **the manager proposal** is `proposals/04_MB_manager_battle_one_resolver.md`; **the scenario proposal** is `proposals/04_MB_playable_field_scenario.md`.

---

## P2-1. Mass battle (MB) — two armies of unit rows, resolved on cells

### P2-1.0 The standalone-playable test

| element | today (opened at this read) | what makes it pass | carried by | the proof (execution artifact, expected reading) |
|---|---|---|---|---|
| **entry** | the registered entry `modules.mass_battle.massbattle:resolve_field(inp, rng)` on a hand-built record (`massbattle.py:473`; P-2); the army's menu as an API (`engine/season/harness/military_menu.py`); a battle page outside the loop (`systems/mass_battle/sim/walkthrough.py` `[LEDGER: audits/04_MB_audit.md:906]`). No `field_scene.py` in `engine/season/harness/` (`ls`) | `python -m engine.season.harness.field_scene --seed S --policy NAME`; `python -m engine.season.harness.scene mass_battle.resolve_field --fixture field --seed S`; `python -m engine.season.harness.play_surface --seed S --person P --scenario field` | the scenario proposal §A creates `field_scene.py` with `build`, `play` and `Report` and names no command: **IS-MB-01** adds it. The other two: `01_CORE_one_scene_contract` edit 4, GO-B §8 (B34) | each command exits 0 and prints a `Report` whose last line names an ending kind; same seed twice, one `content_hash` |
| **scenario** | none that is a game (`audits/04_MB_audit.md:903`) | two factions, each with a seat that may `march` and `marshal`, an army minted and filled through the real verbs from cohorts with training Sites, a settlement each (one garrisoned), stores at both treasuries | the scenario proposal §A (B20) | `engine/season/tests/test_field_scene.py::test_two_policies_end_in_different_bands` |
| **player-facing surface** | before: the `march` target only; posture, the standing order and the army verbs are withheld or off (`fixtures.py:1157`; `rosters.yaml:1176` `values: [storm]`). During: none, one call of up to 18 field ticks. After: the band Event | before: `MilitaryMenu`, the order of battle, `field_estimate`'s shares; during: `FieldWindowView` and one `GeneralAction` at each window; after: `FieldOutcome.report` and the `account` | the manager proposal §2, §4–§6 and `27_MB_D` (B20); GO-B §6, row *field* (B34) | the manager proposal's gates 1–3; GO-B gate 1 |
| **stub contract for the neighbours** | the typed input is the declared interface: `MassBattleInput` (`engine/season/queries/inputs.py:205-267`); the module reads no `World` (`massbattle.py:473` docstring) | the table below | **IS-MB-01** | `harness.scene mass_battle.resolve_field --fixture field` with `apply=False` reaches `seam.contest` and writes nothing else |
| **ending kinds** | a battle returns four keys and one of four words; there is no drawn end state and, at the shipped scale, no result but the attacker's `Failure` (P-2) | per battle, the end state **won**, **lost** or **drawn** (with **unopposed** and **invested**), A-3. Per scenario: **win** (the played faction takes the other's settlement by its own `seize`, or the other side `surrender`s), **lose** (the reverse), **draw** (the season cap, with each army at its station and its losses written). Every end state leaves a durable write (A-81) | `04_MB_headcount_grade_and_scale` and `04_MB_typed_outcome_and_one_path` (B17); the manager proposal §1 (B20); the scenario proposal §C, gate 7 (B20); `U5d_FA_land_and_seats_pass_on_a_won_march` (B23) for the `seize` ending | **IS-MB-01**'s `test_every_ending_kind_is_reached_and_each_writes`; the scenario proposal's `test_no_field_band_without_a_durable_write` |
| **a choice that matters** | P-3: the standing order's fall-back point changed the result in 1 of 1,500 cells; seven of fifteen roles change nothing | a policy that differs from another only in one choice ends differently at some seed, for each choice the scenario offers | the manager proposal §2 (standing orders on the unit row) and its falsifier; `26_MASS_BATTLE_cell_scale_and_time` §3 (bouts and lulls, B19); `U5b_MB_residue` §1 (the roles that leave the menu, B17) | **IS-MB-01**'s `test_a_fall_back_point_changes_some_battle` |
| **one code path** | no: the workbench runs loops the season cannot reach and the season runs arms the workbench cannot (`audits/04_MB_audit.md:911-912`) | the commanded, the delegated and the replayed battle are one call | `04_MB_typed_outcome_and_one_path` §2 (B17); the manager proposal §5, gate 7 (B20) | `tests/valoria/test_army_battle.py::test_none_decider_equals_no_decider`, `::test_replay_from_interventions_is_identical` (`assert checked >= 200`) |
| **integrated check** | seed 0, one season: the adapter is entered 3 times and `resolve_field` 0 times; the army record's rows and `loop/effects_army.py` are entered by no run `[LEDGER: master/HOLISTIC_AUDIT.md §3]` | a seeded realm raises armies and fights battles by persons' own acts | the scenario proposal §E and `14_VERBS_MILITARY_A..D` (B22) | **IS-MB-05**: `aperture 2 s`, s = 0, 1, 2: `field.won + field.lost + field.drawn` above 0 and the `ENGINES` rows `mass_battle.resolve_field`, `mass_battle.army`, `mass_battle.army_order` above 0 |

**The stub contract** (a stub is a plain value on `MassBattleInput` or a row of the scenario's world; never a second code path):

| neighbour | what the battle consumes from it in the loop | the stand-in in the scenario | what the stub may not do |
|---|---|---|---|
| DICE | the one sampler, once B05 lands (`U5b_MB_rulings_in_the_field` §1); today the module's own roller (`modules/mass_battle/resolution.py:50`) | **not stubbed** | — |
| CHAR | each member's `weight`; the sides' stances; the commander's and officers' skill score in `command` and their attributes (`27_MB_A`); the decider of a commander nobody plays | two commanders and their officers authored by `field_scene.build`; an unplayed commander's window action comes from **IS-MB-03** | decide for a commander by a rule in the scenario file or the module (`27_MB_D` §4) |
| FA | the seat whose remit grants `march` and `marshal`; who holds the target; whether the two are at war | one seat a faction, the war planted at build | pass title in the battle's fold: land moves only by the winner's own `seize` (A-66; `U3_CONFLICT_LEDGER.md` C3-L12 `[LEDGER]`) |
| SE | fortification (`world_q.fortification_of`), training Sites, stores through `settlements.provision`, garrison Sites | one garrisoned settlement, training Sites of each kind, stores at both treasuries | size a side past what its stores and cohorts allow |
| WR | the geography file's terrain and rivers (`MassBattleInput.geography`, read-only) | the shipped file; two territories named | write into it |
| PC | the `duel` callable (`combat.round`, nested at cap 1; B30) | absent before B30: an officer contact is reported unresolved | call `modules/combat` by import (`04_MB_squad_grid_of_named_characters` gate 5) |
| SC, FI | nothing consumed | absent | — |

### P2-1.1 The batch sequence, and what each batch gives the test

| order | batch | what it gives mass battle | what the test can show after it |
|---|---|---|---|
| 1 | **B02-tests** (IN) | CI-11's `ENGINES` block | the before-reading for every MB row |
| 2 | **B05-one-roll** (IN) | one sampler in the battle (A-5; `U5b_MB_rulings_in_the_field` §1; `10_DICE_one_roller_one_fraction_rule` Edit C) | the battle and a debate draw from one roller |
| 3 | **B06-keyed-draw** (IN) | every draw keyed `(field, tick, unit, purpose)` | a replayed battle is identical by construction |
| 4 | **B17-mb-scale** (MB) | one survivor share, one owner of weight to troops, the **drawn** end state and the return to station (A-67 to A-70), the typed `FieldOutcome`, one path, `references/troops.yaml` and its exporter | **a battle resolves at the shipped scale with three end states** (P-2 is the before-reading) |
| 5 | **B19-mb-field-calibration** (MB) | command and the obedience draw (A-59), the stand and pursuit draws, the linear melee law (A-60), cells and the hierarchy as data, bouts and lulls, the side-wide multiplier tested out (A-77) | the result has causes the report can name; a fall-back point is reachable inside a battle |
| 6 | **B20-mb-orders** (MB) | standing orders on the unit row, the window and `GeneralAction`, the interventions list, the report, the scenario, the commander's view and odds; **IS-MB-01**, **IS-MB-03** | **MB plays alone**: choices before and during, a report after, three ending kinds (the `seize` ending waits on B23) |
| 7 | **B22-mb-armies** (MB) | what an army carries back (A-69, A-78), the military verbs, supply and muster, armies at realm build; **IS-MB-02** (the siege) | **MB is integrated**: a seeded realm fights battles in natural play; besiege is a real second option |
| 8 | **B23-land** (FA) | `seize`, occupy, withdraw; seats pass with holdings (A-57, A-58, A-66) | the scenario's **win** by taking the place |
| 9 | **B30-mb-nested** (MB) | officers' duel contacts, the squad of named characters; **IS-MB-04**, IS-PC-02 | a duel inside a battle; a squad plays alone |
| 10 | **B31-mb-loadout-economy** (MB) | the secondary weapon and its cost, movement and fatigue as data, the campaign economy, unit prowess on the row; **IS-MB-06** | a designer defines a troop type and its kit as data |
| 11 | **B34-go-surface** (GO) | the transcript and the generic scene entry | the battle as a player would see it |

**The cut, stated.** MB's standalone scenario lands in B20 and its integrated proof in B22 because the military verbs (B22) wait on a decision U1 has not taken (IS-MB-B1); holding the scenario for them would leave B17, B19 and B20 with nothing to play. The scenario does not need them: its armies are minted at build by `harness/army_presets.py::install`, which folds the army verbs directly between seasons and spends no person's budget (that file's head).

### P2-1.2 Items

**Item: IS-MB-01 · the battle scenario's command line, its policies, its ending kinds, and a choice that must bite**

- **Advances:** MB standalone (entry, end condition, instrument); the manager proposal's falsifier *"a standing order that cannot change an outcome at any of 200 seeds"*, which P-3 shows is live today.
- **INSTRUCTION** (edits to `engine/season/harness/field_scene.py`, after the scenario proposal §A creates it in the same batch):
  1. `POLICIES`, a closed mapping of name to player-proxy callback over `military_menu.menu`, `field_estimate` and `FieldWindowView`: `storm` (march at once; `none` at every window); `fall_back_early` (as `storm`, with every unit's standing order `(own_strength:F, {stance: retreat})` set at the highest `F` the closed set offers); `signal_then_hold` (the manager proposal's gate-2 script: fire a signal at window 1, order one unit to `hold` at window 2); `auto` (no callback: both commanders decided by the chooser and IS-MB-03). `besiege_then_storm` joins when IS-MB-02 lands.
  2. **Registry first (Sonnet check, 2026-11-12).** The scenario proposal's `play` is not a second season loop: `field_scene` registers `field` in `scenarios.SCENARIOS` (`IS-B2-CORE-01`, B11; B20 follows B11) with `build=field_scene.build`, `verbs=None`, `seat` the played faction's commander, `ending=field_ending`, `role="mass_battle.resolve_field"`, and `kinds` and `unreached` as `IS-B3-GO-01` defines them; `play` calls `scenarios.run("field", seed, seasons, host=...)`, and `main()` keeps its command line (the rule of `IS-B2-CORE-01` (4)). `ending_kind(report) -> 'won' | 'lost' | 'drawn' | None` (the closed `ENDING_KINDS` of `IS-B3-GO-01`) for the played faction is the `kinds` row applied to `field_ending`'s name, by the table in P2-1.0 (`win`, `lose` and `draw` there are the work order's words for `won`, `lost` and `drawn`); at the season cap the report's last block prints where each army stands, each unit row's losses (by kind once `27_MB_E` lands) and who holds each settlement, so a draw is a state a player can act on and never a blank.
  3. `main()`: `--seed`, `--policy`, `--seasons`; prints the `Report` and the `content_hash`.
  4. Split part, lands in **B34**: `harness/scene.py::FIXTURES["field"]` names `field_scene.build` and its opening `march`; `play_surface --scenario field` resolves to the same builder.
- **WHERE:** `engine/season/harness/field_scene.py`; `engine/season/harness/scenarios.py` (one registry row, B20); `engine/season/tests/test_field_scene.py`; in B34 one line each in `harness/scene.py` and `harness/play_surface.py`.
- **FALSIFIER and control:** each policy pair that differs in one choice ends identically at every seed read (then that choice is cosmetic). Control: `storm` twice at one seed is one hash; `storm` at two seeds differs (the scenario proposal's gate 1).
- **GATE:** added to `engine/season/tests/test_field_scene.py`, written first and read red: `test_every_ending_kind_is_reached_and_each_writes` (seeds 0–59 under `auto`; `assert` on the count of battles read); `test_a_fall_back_point_changes_some_battle` (`storm` against `fall_back_early`, seeds 0–199, `assert checked >= 200`: the `FieldOutcome` differs at some seed); `test_a_window_action_changes_some_battle` (`storm` against `signal_then_hold`, the same form); `test_same_seed_twice_is_one_hash`. **If the fall-back test is red at B20's close**, the fall-back point is removed from the scenario's offered choices in that commit and the close says so with the reading: a choice the player is offered must be able to matter, and P-3 is the before-reading.
- **Hash movers:** none (a harness file and its test; the scenario's `Fixtures` overrides are for its world only).
- **Depends on:** the scenario proposal §A–§D (PROPOSED, B20); the manager proposal §2, §4–§5 (PROPOSED, B20); `26_MASS_BATTLE_cell_scale_and_time` §3 (PROPOSED, B19); `04_MB_headcount_grade_and_scale` (PROPOSED, B17); `IS-B2-CORE-01` and `IS-B3-GO-01` (PROPOSED, B11); `play_surface.dispatching_chooser`, `military_menu`, `field_estimate` (`seam/wrappers/mass_battle.py:463`), `army_presets.install` (EXISTS-IN-TREE).
- **Lane:** MB. **Joins:** B20-mb-orders, after the scenario proposal's §A–§D; step 4 in B34. **Cost class and tier:** small build; `sonnet`, `high`. **Lands it:** B20's `valoria-author` producer, one `Item: IS-MB-01` commit.

**Item: IS-MB-02 · the siege: `besiege` joins the march's postures** (closes G-1 of `unified/U4_TRACEABILITY.md` §6; unblocks `17_CENSUS_C1A_02`'s `_siege` row and `U5d_STORY_owed_edits` §1)

- **Advances:** R-04 and R-05 (a chain whose first link nothing can fire); the *invested* end state; the scenario's second way to take a place. G-1's carry text stands; three things it does not carry are added (steps 1, 4, 5).
- **INSTRUCTION** (in order):
  1. **The roster's own precondition, read first.** `engine/season/rosters.yaml:1171-1173` says `besiege` joins *"in its own declared-mover commit, whose body must state that `restore` executed on a garrison Site in a natural run (seeds 0-2)"*, because until then *"besiege-then-storm dominates storm, since the wear is permanent"*. Run `python -m engine.season.harness.aperture 2 s`, s = 0, 1, 2, and read `restore`'s `executed` on a garrison Site. `restore` is landed by `14_VERBS_MATERIAL_A_mending` (B12). If it reads 0 at any seed the item stops (`STOPPED`), with the reading, and nothing below ships.
  2. `rosters.yaml: march_postures.values`: `[storm]` becomes `[storm, besiege]`, in its own commit, declared as a mover. `choice_sourced` already ranges `march`'s `posture` over this roster (`rosters.yaml:2566-2590`), so `_fanned_choices` (`decision/options.py:1343`) begins to form a `besiege` Candidate with no further edit.
  3. The `march` row and `seam/wrappers/mass_battle.py::resolve` already answer an opposed `besiege` as `Invested` (the roster's note, `:1162-1165`); `loop/effects_combat.py::_siege` (`:686`, reached from `:520`) wears each garrison Site. No edit; name both in the commit.
  4. **A siege that wears nothing still writes (A-81).** `_siege` returns `NO_CHANGE` when no Site would fall, and the act then reads `march.refused` (`effects_combat.py:686-700`, its own `[ASSUMPTION]`). Change it so the `siege.pressed` Event (`verb_table.yaml:1076`) is emitted and witnessed whether or not a wall fell, by the mechanism `03_PC_typed_outcome_one_door.md:92` gives an `undecided` fight. `[ASSUMPTION: the durable write is the witnessed claim that the place is besieged — basis: U3 C3-C11's precedent, and `14_VERBS_BINDING_E_war_seats` reads `siege.pressed` claims for its `Besieged` class]`
  5. **The wear is a draw, by its one owner.** `_siege` takes its fall from `loop/effects_economy.py::_fall`, `sabotage`'s formula; the draw on it is SE's (`U5b_MB_residue` §8). After B12, open `_fall`: if it is the drawn form, `_siege` inherits it; if it is still a fixed fraction, this item stops and reports to the SE lane. No second formula is written here. **Read at the tree, 2026-11-12 (Sonnet check):** `_fall` (`effects_economy.py:141`) is `(max(0, site.condition) * num) // den`, a fixed commons fraction with no draw, and `_siege` (`effects_combat.py:686`) reads it unchanged; so at today's tree this step stops. It passes only if B12 turns `_fall` into a draw (`16_PESSIMIST_SE_B` / `U5b_MB_residue` §8), and B22 follows B12.
  6. Delete the scenario's `march_postures: [storm, besiege]` override "for this world only" (the scenario proposal §A): the roster now ships both. Add `besiege_then_storm` to IS-MB-01's `POLICIES`.
- **WHERE:** `engine/season/rosters.yaml`; `engine/season/loop/effects_combat.py`; `engine/season/tests/test_march.py`; `engine/season/harness/field_scene.py`.
- **FALSIFIER and control:** `test_march.py::test_an_opposed_besiege_is_invested_and_wears_the_garrison` (planted garrison; control: `storm` against the same garrison fights a battle; G-1's test); `::test_an_invested_siege_that_wears_nothing_still_leaves_a_claim` (step 4; control: with the edit reverted the act reads `march.refused`); `::test_one_besiege_does_not_ruin_the_walls_at_every_seed` (a rung with one person present, seeds 0–19, `assert checked >= 20`: the garrison's condition is above 0 at some seed; the roster warns that today *"a single besiege act zeroes the walls"*, `:1173-1174`).
- **GATE:** the three tests; `aperture 2 0`: `march` with posture `besiege` formed and executed at least once, `Invested` read; and one table in the commit body, read by `opus` at the batch's close: over `field_scene` seeds 0–39, the `win` share and the seasons taken under `storm` and under `besiege_then_storm`, each with its disjoint-seed control. If besieging first wins at least as often at every seed and costs nothing the table can show, the mover commit of step 2 is not made and the close says why.
- **Hash movers:** any seeded realm in which a chooser forms `besiege`; one re-pin, in B22's last `Item:` commit, said plainly as a re-pin.
- **Depends on:** `14_VERBS_MILITARY_A_movement` edits 1–5 (PROPOSED, B22); `14_VERBS_MATERIAL_A_mending` (PROPOSED, B12); workplan v11 position CP-T04-06 (MISSING until `STAGES.md` step 5 dispositions it: this item is what retires it).
- **Lane:** MB. **Joins:** B22-mb-armies, after `14_VERBS_MILITARY_A`. **Cost class and tier:** edit; `sonnet`, with the table read by `opus`. **Lands it:** B22's producer.

**Item: IS-MB-03 · an unplayed commander acts at a window** (completes `27_MB_D` item 27D-4; `U4_DOCUMENT_STATUS.md` §3.4 code DESIGN)

- **Advances:** the NPC half of the standing requirement (the world generates battles nobody watches); R-06 and R-08 inside a battle. The proposal returns 27D-4 to CHAR as *"a design only"*. The form is decided here by the ladder's step 4 (precedent): PB §5 already specifies how a person nobody plays picks among a closed set inside a contest, and `27_MB_D` §4 asks for *"the chooser over the same closed set"*. What stays CHAR's is the content of the cells.
- **INSTRUCTION** (in order):
  1. **No second decider is written (Sonnet check, 2026-11-12).** `IS-B2-CHAR-02` (B10) builds the one function that picks among a view's legal values by choice score on a keyed stream, `engine/season/decision/decider.py::make_decider(p, fx, draw, *, key, odds=None, bias=None, watch=None)`, and says it closes the same `27_MB_D` 27D-4; this item had drafted `choose.py::general_action_of` doing the same sum and the same `_sample_order` pick. The field's commander is `make_decider` with `key="general_action"`: the view's `legal` tuple is `none` plus the kinds a matching `window_responses` row names; the choice score is `IS-B2-CHAR-02`'s (`align_choice('general_action', kind, axis)` on the person's axis weights); `bias` is this item's one addition, a callable `(view, value) -> float` returning the summed `weight` of the rows matching that value (0.0 where none), added to the choice score. One legal value (the shipped state: no row) returns `none` and draws nothing. The draw is keyed `general_action:<kind>` on a stream of its own, never the battle's. `GeneralAction.reasons` carries `watch`'s two terms for the winner. `IS-B2-CHAR-02` gains the `bias` argument (default `None`: no term the chooser does not have) and `test_a_single_legal_value_draws_nothing`.
  2. `engine/season/data/verbs.py::CHOICE_RANGES` (`:1698`): `general_action` as a pointer to the module's closed kinds (`signal`, `order`, `rally`, `withdraw`, `none`). It is **not** listed under any verb in `rosters.yaml: choice_sourced`, so nothing fans at DELIBERATE: the action is chosen in the battle, at the window.
  3. `engine/season/rosters.yaml: window_responses`, a new optional table, shipped empty: rows `{window, own: <band>, value: {kind, post, arg}, weight}`, where `post` is one of the army formation's post names (`centre`, `left`, `right`, `rear`, `reserve`; the closed set `commander_post` uses, `MB_LEXICON.md` post row: the proposed name `front` is `centre`) and names the unit an `order` or `rally` goes to. The loader (`data/rosters.py`) reads the table while empty and refuses, naming the row, a `kind` outside the closed kinds, a `post` outside the posts and an `arg` outside the standing-order behaviours. A row is content about how commanders respond to what they can see; it names no person, faction or outcome.
  4. `engine/season/seam/wrappers/mass_battle.py::resolve` (`:355`): one decider per commander: the host's when the host plays him, by the inline party test the combat adapter uses today (`seam/wrappers/combat.py:394-395`; B34's `played_by` replaces both tests later, `01_CORE_one_scene_contract` edit 2), otherwise a closure over his frozen `PersonInterior` calling `make_decider(..., key="general_action", bias=...)` (step 1); passed as `decide=`.
  5. Ships with no cell and no row. The cells (`choices: general_action:` in `tables.alignment`) are `02_CHAR_choice_alignment`'s block and Jordan's or the CHAR content pass's values (G-3).
- **WHERE:** `engine/season/data/verbs.py`; `engine/season/rosters.yaml`; `engine/season/data/rosters.py`; `engine/season/seam/wrappers/mass_battle.py`; `tests/valoria/test_army_battle.py`; `engine/season/tests/test_field_scene.py`.
- **FALSIFIER and control:** a rule for an unplayed commander found in `modules/mass_battle/` or in the adapter; a decider that changes the count of draws from the battle's stream. Control: with nothing authored, `auto` equals the delegated battle at 200 seeds.
- **GATE:** `tests/valoria/test_army_battle.py::test_a_chooser_served_commander_with_no_cell_is_the_delegated_battle` (`assert checked >= 200`); `engine/season/tests/test_field_scene.py::test_two_commanders_opposed_on_one_axis_act_differently_at_a_window` (one cell and one row authored in the test, temperature 0); `::test_the_window_decider_draws_nothing_from_the_battles_stream`; the loader's three refusals beside the other `rosters.yaml` refusals.
- **Hash movers:** none while no cell and no row is authored.
- **Depends on:** `27_MB_D` items 27D-1 to 27D-3 and the manager proposal §4–§5 (PROPOSED, B20); PB step 4, `approach_of` (PROPOSED, B16; B20 follows B16 in U3 §2.1); `U5a_CORE_owed_edits` §E, the frozen `PersonInterior` (PROPOSED, B03); `IS-B2-CHAR-02`'s `make_decider` (PROPOSED, B10); `02_CHAR_choice_alignment`, `align_choice` and the loader rule PB §5 amends (PROPOSED, B10); `CHOICE_RANGES` (EXISTS-IN-TREE).
- **Lane:** MB, with IN review of the `decision/` edit. **Joins:** B20-mb-orders, after `27_MB_D`. **Cost class and tier:** small build; `sonnet`, the function read at the batch's one `opus` critique. **Lands it:** B20's producer. `[ASSUMPTION: the duel's form transfers to the window unchanged — basis: PB §5 and `27_MB_D` §4, §5; reversible: delete the adapter's closure and the adapter passes no decider, which is today's complete behaviour]`

**Item: IS-MB-04 · the squad plays alone**

- **Advances:** MB standalone at the scale below a unit (the Ogre Battle and Unicorn Overlord referents, `AUDIT_BRIEF.md:361-368`) and PC's mode 2. `04_MB_squad_grid_of_named_characters` gates on the realm's own seed-2 battle and names no scenario.
- **INSTRUCTION:** in `engine/season/harness/field_scene.py`: `build_squad(seed) -> World`, two sides of named persons (three against two, the size of the realm's seed-2 battle the proposal's gate 1 reads), each with a squad sheet (places and standing orders) held as the proposal's §2 says; `POLICIES` gains `leader_front` and `leader_rear` (the same sheet with the leader's place changed); `main()` gains `--squad`. It registers `squad` in `scenarios.SCENARIOS` (`IS-B2-CORE-01`; `build=build_squad`, `role="mass_battle.resolve_field"`, `kinds` and `unreached` per `IS-B3-GO-01`) and calls `scenarios.run`, as `IS-MB-01` does. Split part in B34: `FIXTURES["squad"]`.
- **WHERE:** `engine/season/harness/field_scene.py`; `engine/season/harness/scenarios.py` (one registry row, B30); `engine/season/tests/test_squad_field.py`.
- **FALSIFIER and control:** the proposal's own: a squad result that does not change when a member's kit, wounds or place changes. Control: the same sheet twice at one seed is one hash.
- **GATE:** `engine/season/tests/test_squad_field.py::test_the_squad_scenario_ends_and_two_sheets_hurt_different_persons` (the proposal's gate 2 on this world, seeds 0–19, `assert checked >= 20`).
- **Hash movers:** none. **Depends on:** `04_MB_squad_grid_of_named_characters` (PROPOSED, B30); IS-MB-01. **Lane:** MB. **Joins:** B30-mb-nested, after the squad file, before IS-PC-02. **Cost and tier:** small build; `sonnet`. **Lands it:** B30's producer. `[ASSUMPTION: three against two — basis: the proposal's gate 1 names the realm's seed-2 battle as two against three]`

**Item: IS-MB-05 · the integrated reading, quoted at four closes**

- **Advances:** the integrated half of the test; H-01.
- **INSTRUCTION:** at the close of B17, B20, B22 and B23 the last commit body quotes `python -m engine.season.harness.aperture 2 s`, s = 0, 1, 2: the `ENGINES` lines for `mass_battle.resolve_field`, `mass_battle.army`, `mass_battle.army_order`; the counts of `field.won`, `field.lost`, `field.drawn`, `field.unopposed`, `siege.pressed`; `attempted` and `executed` for `march`, `marshal`, `recruit`, `form_unit`, `assign_troops`, `order_unit`. Each reading names its SHA and is taken once.
- **WHERE:** no file; the four close commits.
- **FALSIFIER and control:** after B22, `mass_battle.resolve_field` reads 0 at any of the three seeds. Control: before B17, `resolve_field` reads 0 in the first season at seed 0 (`master/HOLISTIC_AUDIT.md` §3).
- **GATE:** expected after B17: at seed 2 the battle the realm fights is `field.won`, `field.lost` or `field.drawn` and no longer the artefact of the shipped scale; after B22: fought battles above 0 at every seed and the two army rows above 0 (the scenario proposal's gate 4); after B23: at least one `seize` following a `field.won`.
- **Hash movers:** none. **Depends on:** CI-11 (PROPOSED, B02). **Lane:** MB (B17, B20, B22), FA (B23). **Joins:** those closes. **Cost and tier:** a reading; `haiku` runs it. **Lands it:** each batch's BATCH-CLOSE.

**Item: IS-MB-06 · unit prowess is one arithmetic with two callers** (settles `27_MB_B` item 27B-2 at the tree; `U4_DOCUMENT_STATUS.md` §3.4 code SITE)

- **Advances:** A-59 (2) (each unit's own prowess as data on its row). The proposal read `Unit.base_combat_pool` by grep and left a fallback; the site is opened here.
- **INSTRUCTION:** `modules/mass_battle/core/exchange.py`: add `prowess_of(power, size, pen, stam_pen) -> float`, returning `power * size * POOL_QUALITY_SCALE + pen + stam_pen`. `prowess(atom)` (27B-1) calls it with `atom.eff_power`, `atom.eff_size` and the subunit's clamped discipline penalty; `Unit.base_combat_pool`'s `POOL_QUALITY_MODEL` arm (`modules/mass_battle/hierarchy/units.py:3013`) calls it with `self.power`, `self.effective_size` and `self.discipline_penalty()`. The fallback is taken, not the direct call: the two share the arithmetic and not the penalty's source (the unit's comes from `discipline_penalty()` with its broken-unit-formation sentinel (the tree's comment says "broken-formation"), `units.py:2994-2998`; the subunit's from the clamp on `atom.eff_discipline`, `exchange.py`, in `subunit_combat_pool`), so the unit arm is not `prowess(atom)` for a lone subunit.
- **WHERE:** `modules/mass_battle/core/exchange.py`; `modules/mass_battle/hierarchy/units.py`.
- **FALSIFIER and control:** any mass-battle golden moving. Control: the three digests of `tools/ci_golden_modes_check.py` equal before and after.
- **GATE:** `python tools/ci_golden_modes_check.py`; the covering file `tests/valoria/test_army_battle.py`.
- **Hash movers:** none. **Depends on:** `27_MB_B` item 27B-1 (PROPOSED). **Lane:** MB. **Joins:** the batch that lands 27B-1, which is B31 by U3 §2.1; `27_MB_B`'s own line puts 27B-1 and 27B-2 at the head of the field calibration batch (B19). The two disagree; U3 governs until v12's author moves the pair (it is hash EQUAL and reads nothing B19 creates, so either batch is sound). **Cost and tier:** edit; `sonnet`. **Lands it:** that batch's producer.

**Pointers: decided elsewhere in the suite, nothing added**

| handle | the missing part | where it is decided | batch |
|---|---|---|---|
| IS-MB-P1 | `27_MB_A` item 27A-6 cannot be coded on today's tree (no `capabilities:` block, no `pool.py::score`) | `U5a_capability_home_and_two_inputs` Part B; B05 precedes B19 in U3 §2.1 | B05, then B19 |
| IS-MB-P2 | `27_MB_C` item 27C-2 waits on 27A-4 to 27A-6 and the two rout files | U3 §1 item 19's order inside the batch | B19 |
| IS-MB-P3 | at the shipped scale no battle resolves (P-2; F-MB-01) | `04_MB_headcount_grade_and_scale` gates 2 and 3 | B17 |
| IS-MB-P4 | roles that change nothing (P-3) | `U5b_MB_residue` §1, the one list of unit roles that leave the menu | B17 |
| IS-MB-P5 | the battle returns an untyped mapping (H-06) | `04_MB_typed_outcome_and_one_path` §1 | B17 |
| IS-MB-P6 | the module keeps its own roller | `10_DICE_one_roller_one_fraction_rule` Edit C with `U5b_MB_rulings_in_the_field` §1 | B05 |
| IS-MB-P7 | a besieged town's larder (`U5d_STORY_owed_edits` §1) and the census's `_siege` row | unblocked by IS-MB-02 | B22, then B39 |

**Blocked items**

| handle | what is missing | why it cannot be decided here | owner | what the suite assumes meanwhile |
|---|---|---|---|---|
| IS-MB-B1 | which obstacle terms of `14_VERBS_MILITARY_A..D` and the army-size source of `14_VERBS_PHYSICAL_B` are members of the obstacle roster (`U5c_SC_one_obstacle_form` §2) | a vocabulary decision the owners ledger has not taken (`U5b_VERBS_military_physical_residue` §1 rule 3 `[LEDGER: U4_DOCUMENT_STATUS.md §3.4]`) | U1 owners ledger | B22's military verbs wait; the standalone scenario (B20) does not, since its armies are minted by `army_presets.install`. The integrated check (IS-MB-05 after B22) cannot be met before the decision |
| IS-MB-B2 | the drill step (a cohort's skill score in `arms` as a step on its unit's `power`): its size, its cap, the host-side read | no proposal specifies a read, and the size is a calibration against `26_MASS_BATTLE_calibration_targets` | MB lane, design-first, B31 | no step: a cohort's skill does not reach unit prowess; that is the control arm |
| IS-MB-B3 | every share table and the return window of `27_MB_E` (items 27E-3, 27E-4) | no value exists in the tree's research; the dead-to-wounded ratio is not established (`README.md` §6) | Jordan, or a source search filed under `research/historical/` | the loader refuses a missing value, so the return ships switched off; the scenario's report prints losses without kinds until then |
| IS-MB-B4 | two unread sites: how a non-verb caller hands `ArmyCommand` to the army record's write path (`27_MB_E`), and how a unit row's name addresses its `Subunit` inside the module (`27_MB_A`) | each is one function to read at landing; this lane did not open them | the landing session of B22 and of B19 | nothing; each proposal says which function |

---

## P2-2. The dice (DICE) — the one roll every contest draws

### P2-2.0 How the test is read for a substrate, and the test

`engine/dice_engine/` holds no scenario, no state and no ending, and Layer 1 is right that it is not a module (`audits/10_DICE_audit.md:646-650`, `:667`). The standing requirement says *every* subsystem plays alone. The ladder answers at step 5 (what makes sense for the architecture): the dice play alone as **one roll taken as a decision**, in a one-act world, through the registered module that rolls (`modules/social_contest/roll.py::roll`), so the substrate gains nothing and the requirement is met by the smallest game the code can host. Reversible on Jordan's word; nothing is built for it beyond one fixture and one printed record.

| element | today (opened at this read) | what makes it pass | carried by | the proof |
|---|---|---|---|---|
| **entry** | `roll(inp, rng)` on a hand-built `SocialContestInput` (`modules/social_contest/roll.py:157`); `sigma_leverage.record_odds` (`engine/dice_engine/sigma_leverage.py:378`). *"A harness line that deals one named act and prints its record; none exists and none is proposed"* (`audits/10_DICE_audit.md:654`) | `python -m engine.season.harness.scene social_contest.roll --fixture roll --seed S [--verb V] [--effort N]` | **IS-DICE-01** | the command prints the record and the dealt band; same seed twice, the same band |
| **scenario** | the act's own generator | two persons who differ in skill score and attributes, a witness, one rolled verb whose band cells differ | **IS-DICE-01** | `test_scene_contract.py::test_the_roll_fixture_prints_terms_that_sum_to_the_obstacle` |
| **choice surface** | which verb, against whom, and `effort` 0 to 2 (`audits/10_DICE_audit.md:656`) | the same, with two inputs visible (A-6: the skill score plus a base gives the dice; A-7: the governing attribute gives named levels) | `U5a_capability_home_and_two_inputs` Parts A and B (B04, B05); `10_DICE_one_score_two_roles` (B05) | `aperture 4 0` prints *"two actors at different pools: yes"* (`U4_TRACEABILITY.md` §4.2c) |
| **legible odds** | `odds_of` exact (`seam/wrappers/sigma.py:350`); `View.odds` believed, `None` against any person; no surface shows either | the exact odds, the believed odds with a prior, the obstacle's terms on the record | `10_DICE_believed_odds_have_a_prior`, `05_SC_contest_record_on_event` (B05); GO-B §2 (B34) | IS-DICE-01's `test_printed_odds_match_realised_bands` |
| **ending kinds** | the four bands; `Failure` writes nothing on the social path and the top band cannot occur (`audits/10_DICE_audit.md:158`, `:658`) | each of the four bands is reachable and each leaves a durable write (A-81) | `U5a_DICE_owed_edits` §1 and `29_DICE` rows 2–4 (B05); `16_PESSIMIST_CORE_a_refusal_is_remembered` (B09); `23_STORY_A_what_a_roll_leaves` (B38) | IS-DICE-01's `test_each_band_is_reached_and_each_writes` |
| **stub contract** | the typed input is the interface: `SocialContestInput` (`engine/season/queries/inputs.py:45-96`) | every neighbour is a number on that record: pool, opposition, difficulty, leverage, reception, proofs | — | `apply=False` reaches `seam.contest` and writes nothing |
| **one code path** | yes for the social roll; the battle keeps a second roller (`modules/mass_battle/resolution.py:50`) and seven files build their own generator (`master/HOLISTIC_AUDIT.md` §2.1, S9) | one roller, one ladder, one draw owner | `10_DICE_one_roller_one_fraction_rule`, `U5b_MB_rulings_in_the_field` §1 (B05); `11_GO_one_draw_owner` with `16_PESSIMIST_GO_keyed_draw_no_recorder` (B06) | `grep -rn "randint(1, 10)" modules engine/dice_engine engine/season --include=*.py`, tests excluded, prints one code line (three lines today, this read) |
| **integrated check** | seed 0, one season: 48 rolls and 62 graded findings among 13,379 Events `[LEDGER: master/HOLISTIC_AUDIT.md §3]` | most consequential outcomes are drawn (R-09) | B05, B06, B07 (`18_DETERMINISM_task_draw_for_uncontested_verbs`) | the R-09 row's reading, owned by lane IS-A |

### P2-2.1 The batch sequence

| order | batch | what it gives the dice | what the test can show after it |
|---|---|---|---|
| 1 | **B02-tests** | the R-09 falsifier row (lands with B05) and CI-11 | the before-reading |
| 2 | **B03-hygiene** | CI-03: the obstacle composer reached by its own composition row; CI-04, CI-05: the season's settings in the typed export | the roll's obstacle is reached by row; the port reads the dice's settings from one artifact |
| 3 | **B04-capability-home** | a skill defined once as data; `opposed_ob` | a new skill is a row |
| 4 | **B05-one-roll** | the bell curve everywhere (A-5), the skill score plus a base (A-6), two inputs (A-7), a wound as a level (A-8), 0.4 a point (A-26), the soft ceiling, believed odds with a prior, the sources of advantage | **one roll, the same for a debate, a fight and a battle** |
| 5 | **B06-keyed-draw** | one draw per key (A-30); declared floats | a roll is recomputable from its key |
| 6 | **B07-task-draw** | uncontested verbs draw too | the integrated check moves |
| 7 | **B15-pc-calibration** | `29_DICE` rows 5–7, 9: the fight on the one curve | — |
| 8 | **B30-mb-nested** | `29_DICE` item 29-5: the nested round and the hearing carry the rate | — |
| 9 | **B34-go-surface** | the scene entry and `Offer`'s odds; **IS-DICE-01** | **the dice play alone** |
| 10 | **B41-go-port-gate** | the draw and float vectors' export round-trip | the port's roller is checked against the oracle's |

### P2-2.2 Items

**Item: IS-DICE-01 · one roll, played**

- **Advances:** DICE standalone; the audit's §8 step 7 (*a surface that prints `odds_of` for an act the player is about to choose*).
- **INSTRUCTION** (edits to `engine/season/harness/scene.py`, which `01_CORE_one_scene_contract` edit 4 creates in the same batch):
  1. `FIXTURES["roll"]`: the world of `duel_scene.build(seed)` (IS-PC-01) with one more authored skill score on each of its two fighters, in the skill the fixture's verb row names, and one authored opening act of a rolled verb. The verb is chosen at landing from the rows of `verb_table.yaml` whose band cells differ, and named in the fixture. `[ASSUMPTION: the duel's world is reused — basis: it already holds two persons who differ and a witness; one small world fewer to build and keep]`
  2. For the role `social_contest.roll`, `scene.play`'s printed record: the pool and its parts (the skill score, the base, the floor); each obstacle term by name and their sum; the levels in force (attributes, wounds, a seat's modifier); the exact band odds (`sigma_leverage.band_odds`); the actor's believed odds; the draw's key; the dealt band; and, with `apply=True`, the writes that band made.
  3. `main()` gains `--verb` and `--effort`.
- **WHERE:** `engine/season/harness/scene.py`; `engine/season/tests/test_scene_contract.py`.
- **FALSIFIER and control:** printed exact odds that disagree with the realised bands beyond the sampling band at 2,000 seeds; a band that leaves the world unchanged with `apply=True`. Control: `--effort 0` twice at one seed prints one record.
- **GATE:** added to `engine/season/tests/test_scene_contract.py`: `test_the_roll_fixture_prints_terms_that_sum_to_the_obstacle`; `test_printed_odds_match_realised_bands` (seeds 0–1,999); `test_effort_changes_the_printed_odds_and_some_dealt_band` (seeds 0–199, `assert checked >= 200`); `test_each_band_is_reached_and_each_writes` (all four bands occur within the 2,000 seeds; each has a write other than the budget debit). Expected reading of the command at seed 0: a record whose terms sum to its obstacle and one of the four bands.
- **Hash movers:** none.
- **Depends on:** `01_CORE_one_scene_contract` edit 4 (PROPOSED, B34); `05_SC_contest_record_on_event` (the `terms`; PROPOSED, B05); `10_DICE_believed_odds_have_a_prior` (PROPOSED, B05); `16_PESSIMIST_CORE_a_refusal_is_remembered` (PROPOSED, B09); IS-PC-01; `roll`, `band_odds`, `odds_of` (EXISTS-IN-TREE).
- **Lane:** GO (the batch's lane), with IN review. **Joins:** B34-go-surface, after `01_CORE_one_scene_contract`. **Cost class and tier:** edit; `sonnet`. **Lands it:** B34's producer.

**Pointers: decided elsewhere in the suite, nothing added**

| handle | the finding | where it is decided | batch |
|---|---|---|---|
| IS-DICE-P1 | a second roller in the battle (F-DICE-07) | `10_DICE_one_roller_one_fraction_rule` Edit C; `U5b_MB_rulings_in_the_field` §1 | B05 |
| IS-DICE-P2 | fourteen places build a generator (S9) | `11_GO_one_draw_owner`; CI-06 lands first so B06 edits one composition of the chooser | B03, B06 |
| IS-DICE-P3 | the typed layer omits the facts every draw depends on (F-DICE-09) | `10_DICE_exported_face_rule_and_band_edges` (A, D); the vectors' export in `16_PESSIMIST_GO_surface_pins` | B05, B41 |
| IS-DICE-P4 | the host reaches the obstacle composer by reflection (H-05) | CI-03 | B03 |
| IS-DICE-P5 | leverage reads 0 on every roll (`audits/10_DICE_audit.md:660`) | `10_DICE_advantage_sources_for_the_arcs`, whose gate is nonzero leverage on a graded roll in `aperture` | B05 |

**Blocked item**

| handle | what is missing | why | owner | what completes it |
|---|---|---|---|---|
| IS-DICE-B1 | `29_DICE` item 29-5, the hearing half: the files, lines, call sites and test of the rule on `HearingInput` and `Speaker` | neither dataclass exists until `05_SC_playable_hearing_B` lands (U3 §6.3) | the SC lane (instruction lane IS-B2) for the records; B30's producer for the edit | at B30, after B24: in `modules/social_contest/hearing.py`, `Speaker.score` is the skill score `_opposition_of` returns; the `argue` move builds a `SocialContestInput` whose `opposition` is that number and `answer` builds one with `opposition=None` (29-5's own text). Test, beside the hearing's own: a hand-built hearing in which every `argue` roll's obstacle is `even_line + difficulty + opposed_ob(the answering speaker's skill score, opposition_rate)`. `[ASSUMPTION: the file name — basis: U3 §6.3 lists `modules/social_contest/hearing.py` as created by HEAR_B]` |

---

## P2-3. The tables v12 takes

### P2-3.1 Items by batch (no batch is created; every item joins an existing handle)

| batch | lane | items this suite adds | hash |
|---|---|---|---|
| B01, B15, B16, B37 closes | IN, PC | IS-PC-03 (a reading) | EQUAL |
| B14-pc-outcome | PC | IS-PC-04 | EQUAL |
| B16-pc-round | PC | IS-PC-01 (last item) | EQUAL |
| B17, B20, B22, B23 closes | MB, FA | IS-MB-05 (a reading) | EQUAL |
| B20-mb-orders | MB | IS-MB-01 (after the scenario proposal §A–§D), IS-MB-03 (after `27_MB_D`) | EQUAL with nothing authored |
| B22-mb-armies | MB | IS-MB-02 | **mover**: realms in which `besiege` forms; one re-pin at B22's last item |
| B30-mb-nested | MB | IS-MB-04, then IS-PC-02 | EQUAL |
| B31 (or B19, see IS-MB-06) | MB | IS-MB-06 | EQUAL |
| B34-go-surface | GO | IS-DICE-01; the split registrations of IS-PC-01, IS-MB-01, IS-MB-04 | EQUAL |

### P2-3.2 File census (files this suite's items create or edit; serial order is item order in the batch)

| file | items | batch |
|---|---|---|
| `engine/season/harness/duel_scene.py` (new), `engine/season/tests/test_duel_scene.py` (new) | IS-PC-01 | B16 |
| `engine/season/harness/field_scene.py` (created by the scenario proposal) | IS-MB-01 (B20) → IS-MB-02 step 6 (B22) → IS-MB-04 (B30) | B20 → B22 → B30 |
| `engine/season/harness/scenarios.py` (created in B11 by `IS-B2-CORE-01`) | one row each: IS-PC-01 `duel` (B16), IS-MB-01 `field` (B20), IS-MB-04 `squad` (B30); appended at the end of the mapping, in merge order | B16, B20, B30 |
| `engine/season/tests/test_field_scene.py` | the scenario proposal, IS-MB-01, IS-MB-03 | B20 |
| `engine/season/tests/test_squad_field.py` (created by the squad proposal) | IS-MB-04 → IS-PC-02 | B30 |
| `engine/season/harness/scene.py`, `harness/play_surface.py` (created or edited by B34's members) | IS-DICE-01; one registration line each from IS-PC-01, IS-MB-01, IS-MB-04 | B34 |
| `engine/season/tests/test_scene_contract.py` | `01_CORE_one_scene_contract`, IS-DICE-01 | B34 |
| `engine/season/decision/choose.py` | PB step 4 `approach_of` (B16); IS-MB-03 no longer edits it (it calls `make_decider`, `decision/decider.py`, `IS-B2-CHAR-02`, B10); `_stance_arm` in the same file is a serial instrument (U3 §1.1) | B16 |
| `engine/season/data/verbs.py` (`CHOICE_RANGES`) | PB step 4 → IS-MB-03 | B16 → B20 |
| `engine/season/rosters.yaml` | IS-MB-03 (`window_responses`, a new key at the end of the choice family's block), IS-MB-02 (`march_postures.values`) | B20, B22 |
| `engine/season/seam/wrappers/mass_battle.py` | the manager proposal §4, `27_MB_D` 27D-4's forward, IS-MB-03 step 4 (one edit, the same lines) | B20 |
| `engine/season/loop/effects_combat.py` (`_siege`), `engine/season/tests/test_march.py` | IS-MB-02 | B22 |
| `modules/mass_battle/core/exchange.py`, `modules/mass_battle/hierarchy/units.py` | `27_MB_B` 27B-1, IS-MB-06 | B31 (or B19) |
| `tests/valoria/test_combat_duel_terms.py`, `test_combat_invariants.py`, `test_combat_strength_jobs.py` | IS-PC-04 | B14 |

### P2-3.3 Serial edges this suite adds (all point forward)

B16 (IS-PC-01) → B34 (the `duel` registration; IS-DICE-01 reuses the duel world) · B16 (`approach_of`) → B20 (IS-MB-03) · B12 (`restore`, the drawn fall) → B22 (IS-MB-02) · B20 (IS-MB-01) → B22 (IS-MB-02 step 6) → B30 (IS-MB-04) → IS-PC-02 · B24 → B30 (IS-DICE-B1's completion). No edge points back; no batch gains a second close.

### P2-3.4 Requirement rows these items serve (the map itself is lane IS-A's)

PC items: R-04's combat conjunct, R-05 (`fight`, `challenge`, `accept`, `capture`), R-09 inside a fight. MB items: R-04, R-05 (`march` and its postures, the army verbs), R-06 and R-08 inside a battle (IS-MB-03). DICE item: R-09 and the legibility half of R-08. None moves a row's `status:` by being written; each batch's close reads `register --requirements`.

### P2-3.5 What this lane closed, and what it left

| source | row | state after this suite |
|---|---|---|
| `U4_TRACEABILITY.md` §6 | G-1 (the siege) | **closed** by IS-MB-02, with three additions G-1 lacks |
| `U4_TRACEABILITY.md` §3 | DICE *"partial by nature"* | **answered** at ladder step 5 (P2-2.0), carried by IS-DICE-01 |
| `U4_DOCUMENT_STATUS.md` §3.4 | `03_PC_duel_round_and_approach_B` (step 5, MB's side) | **closed** by pointer IS-PC-P1; step 3d stays blocked (IS-PC-B1) |
| | `03_PC_loadout_and_carry` | **closed** by pointer IS-PC-P2 |
| | `U5b_PC_residue` §10 | **closed** by IS-PC-04, on this lane's criterion and its `[ASSUMPTION]` |
| | `16_PESSIMIST_PC_A` (the values) | blocked, IS-PC-B2 (Jordan) |
| | `27_MB_A`, `27_MB_C` | **closed** by order (IS-MB-P1, IS-MB-P2); two sites left to the landing session (IS-MB-B4) |
| | `27_MB_B` | 27B-2 **closed** at the tree (IS-MB-06); the drill step blocked (IS-MB-B2) |
| | `27_MB_D` (27D-4) | **closed** by IS-MB-03; the cells' content stays CHAR's (G-3) |
| | `27_MB_E` | blocked on content (IS-MB-B3) |
| | `29_DICE` (29-5, hearing half) | blocked on B24, with its completing step (IS-DICE-B1) |
| | `14_VERBS_MILITARY_A..D`, `14_VERBS_PHYSICAL_B`, `U5b_VERBS_military_physical_residue` | blocked on U1 (IS-MB-B1) |
| | `17_CENSUS_C1A_02` (`_siege`), `U5d_STORY_owed_edits` §1 | **unblocked** by IS-MB-02 |
| `master/HOLISTIC_AUDIT*.md` | H-01 for combat and the army record | read at the closes IS-PC-03 and IS-MB-05 name, through CI-11 |
| | H-06, H-08 | pointers (B14 and B17; B13) |

**Not this lane's:** G-2 to G-7 and G-10 to G-16 fall in other subjects (scale vocabulary, authored content, R-07 and R-08 tests, the requirement map, domain actions, skill loss, the no-null-scene reading, ages, construal, the reveal, zero coherence, the acts that count for a march); lanes IS-A, IS-B2 and IS-B3 carry them.

## P2-4. What was not checked

- **No proposal was executed and no test was run** (the order forbids pytest). Every gate above is an instruction; the four probes are the only executions.
- **Proposals opened in full:** PB, the scenario proposal, `01_CORE_one_scene_contract`. **Opened at the sections cited:** the manager proposal (§1–§8 and its gate), `27_MB_D` (§4, §5, the edits and the instructions), `29_DICE` (head, items 29-2 and 29-5), `04_MB_headcount_grade_and_scale` (resolution, gate), `04_MB_squad_grid_of_named_characters` (edits, gate), `16_PESSIMIST_PC_A` (gate, cost), `U5b_PC_residue` (§10), `27_MB_A`, `27_MB_B`, `27_MB_E` (their INCOMPLETE tails), `03_PC_typed_outcome_one_door` (`:84-92`), `03_PC_exits_withdrawal_recovery` (`:44-62`), GO-B (§6 table, §8, gate). **Not opened:** `03_PC_person_inputs_content`, `03_PC_loadout_and_carry`, `04_MB_typed_outcome_and_one_path` beyond its headings, `04_MB_cell_hierarchy_as_data`, the six `26_MASS_BATTLE_*` files, `27_MB_C`, the `10_DICE_*` files and `U5a_DICE_owed_edits` beyond what U3 and U4 say of them, `14_VERBS_MILITARY_A..D`, `U5b_MB_rulings_in_the_field`, `U5b_PC_rulings_in_the_fight`. Claims about those rest on the ledgers and carry `[LEDGER]` or name the ledger line.
- **Audits:** `03_PC_audit` §0, §1, §8–§10; `04_MB_audit` §9, §10; `10_DICE_audit` §8–§10. The addenda and audits 26, 27 and 29 were not opened.
- **Digests and the DICE and MB dossiers** were not opened; the PC dossier was read to its hole-register rows. **`engine/season/requirements.yaml`** was not opened: the nine are lane IS-A's, and this file cites requirement ids only through `U4_TRACEABILITY.md` §2.
- **Whether `_fall` becomes a draw in B12**, and **how an Event is emitted for a band that writes nothing** (IS-MB-02 steps 4 and 5): both are named as reads at landing, not asserted.
- **`02_CHAR_choice_alignment`'s `choices:` block and `align_choice`** are taken from PB §5's account of them, not from the file.
- **P-3 is one matchup at one size.** It shows that the present fall-back points do not bite in an even 18-tick bout; it is not a claim about standing orders after B19 and B20.
- **Words.** Proposals quoted here still carry words A-98 retires; this file's own prose was checked for them by search.

## P2-5. Evidence log

All at `b07fc1c`, `PYTHONHASHSEED=0`; scripts in the session scratchpad (not committed); nothing tracked was written by a probe.

| id | command or script | seed and size | outcome |
|---|---|---|---|
| P-1 | `p_pc.py`: `composition.require("combat.fight")` on `PersonalCombatInput(claimants=("a","b"), ends=(4,4), wound_quantities=("wounds","max_wounds"), terms=T)` | `random.Random(s)`, s = 0–199, three terms, two deciders | `death` 99 / 99 / 2; `blood` 103 / 97 / 0; `yield` 98 / 101 / 1 (first party wins / loses / undecided); withdraw-at-first-wound 67 / 32 / 101; always-`engage` 99 / 99 / 2, the tallies of no decider (tallies compared, not each seed). `TURN_CHOICES = ('engage', 'withdraw')`, `DUEL_TERMS = ('yield', 'blood', 'death')` |
| P-2 | `p_mb.py`: `composition.require("mass_battle.resolve_field")` on a `MassBattleInput` with no territory, no fort, stances and loyalties 0 | s = 0–99 | 40 v 40 at `troops_per_weight` 1: `Failure` 100. At 25: `Success` 37, `Failure` 63. 80 v 40: 50, 49, `Partial` 1. 40 v 80: 21, 79. Return keys: `attacker_size_pct`, `attacker_wins`, `defender_size_pct`, `degree` |
| P-3 | `p_mb2.py`: the same battle at 25 with `orders=(FieldOrder(role, r), None)`, comparing `(degree, both shares)` per seed | s = 0–99; 15 roles; `RETREAT_AT = ('none', '0.5', '0.25')` | seeds on which the fall-back point changes the result: 0 for fourteen roles, 1 for `Shock`. Seeds on which the role changes it against no order: `ShieldWall` 17, `Hold` 17, `Push` 11, `Flanker` 50, `Skirmish`, `Shock`, `Harass`, `Kite` 100 each, the other seven 0. A defender's `Hold` with each fall-back point: 0. Control: 33 distinct results over the 100 seeds with no order |
| P-4 | `scan_loops.py` over `tests/valoria/test_combat*.py` (and over `tests/valoria/test_*.py`: 20 loop nodes in all) | — | nine loop nodes in four functions, listed at IS-PC-04 |
| — | `Fixtures` read at `engine/season/data/fixtures.py` | — | `field_troops_per_weight=1` (`:789`), `field_subunits="side"` (`:797`), `field_provisioning=False` (`:809`), `contest_max_depth=2` (`:426`), `withheld_verbs` holds the army verbs, `marshal` and `surrender` (`:1157`) |
| — | symbol checks by `grep` | — | present: `choose.py` `deliberation_memo` `:130`, `score_terms` `:193`, `_sample_order` `:322`; `data/verbs.py` `CHOICE_RANGES` `:1698`; `options.py` `_fanned_choices` `:1343`; `effects_combat.py` `_eff_march` `:451`, `_siege` `:686`; `seam/wrappers/mass_battle.py` `resolve` `:355`, `field_estimate` `:463`; `seam/wrappers/combat.py` `fight_estimate` `:235`; `battle_loop.py` `phase_boundary` call `:461`; `rosters.yaml` `fight_endings` `:986`, `march_postures` `:1159`, `choice_sourced` `:2566`. Absent: `engine/season/harness/scene.py`, `duel_scene.py`, `field_scene.py` |
