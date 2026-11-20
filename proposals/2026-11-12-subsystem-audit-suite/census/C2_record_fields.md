# C2 · dataclass fields the game code declares but never reads and/or never writes (leads)

Counts are textual: `.field` loads; `.field =` stores; `field=` keyword uses (one of which is the declaration default); quoted `"field"` strings (covers `write("kind", "field", ...)` and `getattr`); the name in YAML. A field set only through a string-keyed `write` shows as a string hit and is not flagged.

| file:line | class.field | loads | stores | kw | strings | reading |
|---|---|---|---|---|---|---|
| `engine/dice_engine/dice_engine.py:143` | `RollResult.pool_size` | 0 | 0 | 2 | 0 | NEVER READ |
| `engine/season/data/goals.py:83` | `GoalStages.for_goals` | 1 | 0 | 0 | 0 | NEVER WRITTEN (beyond its default) |
| `engine/season/data/goals.py:95` | `Goal.org_kind` | 15 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `engine/season/data/verbs.py:217` | `VerbRow.refusals_by_clause` | 8 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `engine/season/decision/sheet.py:122` | `DevelopmentSheet.person_id` | 0 | 0 | 1 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `engine/season/decision/sheet.py:187` | `Chronicle.person_id` | 0 | 0 | 1 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `engine/season/decision/sheet.py:191` | `Chronicle.scar_pursuits` | 0 | 0 | 0 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `engine/season/decision/sheet.py:192` | `Chronicle.scar_affiliations_held` | 0 | 0 | 0 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `engine/season/decision/sheet.py:193` | `Chronicle.scar_affiliations_history` | 0 | 0 | 0 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `engine/season/harness/military_menu.py:63` | `MilitaryMenu.raise_` | 4 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `engine/season/harness/obligee_report.py:79` | `ObligeeReading.tells_by_obligees` | 2 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `engine/season/harness/obligee_report.py:80` | `ObligeeReading.tells_all` | 2 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `engine/season/harness/obligee_report.py:83` | `ObligeeReading.attempted_by` | 4 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `engine/season/harness/obligee_report.py:84` | `ObligeeReading.edges_since` | 3 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `engine/season/queries/inputs.py:261` | `MassBattleInput.loyalty_gain` | 2 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `engine/season/queries/inputs.py:395` | `BodyFall.body_after` | 2 | 0 | 0 | 0 | NEVER WRITTEN (beyond its default) |
| `engine/season/queries/inputs.py:409` | `SubsistOutcome.short_by_person` | 1 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `engine/season/queries/inputs.py:503` | `FabricInput.live_works` | 2 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `engine/season/state/carriers.py:1061` | `Office.body_function` | 0 | 1 | 1 | 0 | NEVER READ |
| `engine/substrate/stubwire.py:49` | `StubResult.io_contract` | 0 | 0 | 1 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `modules/mass_battle/hierarchy/units.py:333` | `Order.waypoint_ref` | 3 | 0 | 0 | 0 | NEVER WRITTEN (beyond its default) |
| `modules/mass_battle/hierarchy/units.py:434` | `Subunit.merged_cells` | 0 | 2 | 2 | 0 | NEVER READ |
| `modules/mass_battle/hierarchy/units.py:516` | `Subunit._order_idx` | 3 | 0 | 0 | 0 | NEVER WRITTEN (beyond its default) |
| `modules/mass_battle/hierarchy/units.py:2849` | `Unit.officers` | 0 | 0 | 4 | 0 | NEVER READ |
| `modules/mass_battle/hierarchy/units.py:2856` | `Unit.terrain_off_d` | 9 | 0 | 0 | 0 | NEVER WRITTEN (beyond its default) |
| `modules/mass_battle/hierarchy/units.py:2857` | `Unit.terrain_def_d` | 5 | 0 | 0 | 0 | NEVER WRITTEN (beyond its default) |
| `modules/mass_battle/orderofbattle.py:104` | `OrderOfBattle.drawn_from` | 1 | 0 | 0 | 0 | NEVER WRITTEN (beyond its default) |
| `systems/characters/sim/conviction.py:164` | `ConvictionThresholdState.scar_counts` | 0 | 0 | 1 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/characters/sim/conviction.py:165` | `ConvictionThresholdState.destabilised` | 0 | 0 | 2 | 0 | NEVER READ |
| `systems/characters/sim/conviction.py:168` | `ConvictionThresholdState.any_crisis` | 0 | 0 | 1 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/fieldwork/sim/knots.py:150` | `KnotState.ruptured` | 0 | 0 | 8 | 0 | NEVER READ |
| `systems/social_contest/sim/contest/agon_harness.py:145` | `HarnessState.consult_count` | 3 | 0 | 0 | 0 | NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/contract.py:55` | `ContestView.live_ground` | 22 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/contract.py:56` | `ContestView.appeal_axis` | 0 | 0 | 1 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/contract.py:57` | `ContestView.my_standing` | 0 | 0 | 13 | 0 | NEVER READ |
| `systems/social_contest/sim/contest/contract.py:58` | `ContestView.opp_standing` | 0 | 0 | 1 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/contract.py:59` | `ContestView.can_hard` | 1 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/contract.py:60` | `ContestView.reserve_frac` | 1 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/contract.py:64` | `ContestView.audience_learned` | 0 | 0 | 1 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/contract.py:65` | `ContestView.audience_hostile` | 0 | 0 | 1 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/contract.py:66` | `ContestView.evidence_available` | 6 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/dictionaries.py:84` | `Style.canonical_flavor` | 0 | 0 | 4 | 0 | NEVER READ |
| `systems/social_contest/sim/contest/dictionaries.py:347` | `AdjudicatorType.mechanical_key` | 0 | 0 | 5 | 0 | NEVER READ |
| `systems/social_contest/sim/contest/dictionaries.py:516` | `Proceeding.mechanical_key` | 0 | 0 | 5 | 0 | NEVER READ |
| `systems/social_contest/sim/contest/faction.py:20` | `Faction.fixed_lean` | 2 | 0 | 0 | 0 | NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/narrative.py:45` | `Chronicle.lead_changes` | 3 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/narrative.py:46` | `Chronicle.turning_point` | 4 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/narrative.py:48` | `Chronicle.decisive_appeal` | 5 | 0 | 0 | 0 | NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/narrative.py:49` | `Chronicle.decisive_ground` | 2 | 0 | 0 | 0 | NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/narrative.py:51` | `Chronicle.room_leader` | 2 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/primitives.py:192` | `RhetoricalWeights.logos_past` | 0 | 0 | 0 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/primitives.py:193` | `RhetoricalWeights.logos_present` | 0 | 0 | 0 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/primitives.py:194` | `RhetoricalWeights.logos_future` | 0 | 0 | 0 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/primitives.py:196` | `RhetoricalWeights.ethos_past` | 0 | 0 | 0 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/primitives.py:197` | `RhetoricalWeights.ethos_present` | 0 | 0 | 2 | 0 | NEVER READ |
| `systems/social_contest/sim/contest/primitives.py:198` | `RhetoricalWeights.ethos_future` | 0 | 0 | 0 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/primitives.py:200` | `RhetoricalWeights.pathos_past` | 0 | 0 | 0 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/primitives.py:201` | `RhetoricalWeights.pathos_present` | 0 | 0 | 0 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/social_contest/sim/contest/primitives.py:202` | `RhetoricalWeights.pathos_future` | 0 | 0 | 0 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/threadwork/sim/co_movement.py:65` | `CoMovementCard.card_id` | 0 | 0 | 2 | 0 | NEVER READ |
| `systems/threadwork/sim/coherence.py:284` | `CoherenceFailureResult.just_transitioned` | 0 | 0 | 2 | 0 | NEVER READ |
| `systems/threadwork/sim/coherence.py:287` | `CoherenceFailureResult.present_displacement` | 2 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `systems/threadwork/sim/collective.py:52` | `CollectiveResult.leap_results` | 0 | 0 | 4 | 0 | NEVER READ |
| `systems/threadwork/sim/collective.py:53` | `CollectiveResult.lattice_formed` | 0 | 0 | 3 | 0 | NEVER READ |
| `systems/threadwork/sim/collective.py:54` | `CollectiveResult.lattice_fractured` | 0 | 0 | 5 | 0 | NEVER READ |
| `systems/threadwork/sim/collective.py:55` | `CollectiveResult.operation_result` | 0 | 0 | 3 | 0 | NEVER READ |
| `systems/threadwork/sim/operations.py:206` | `OperationResult.net_successes` | 0 | 0 | 4 | 0 | NEVER READ |
| `systems/threadwork/sim/operations.py:458` | `MendingPrice.coherence_cost` | 3 | 0 | 1 | 0 | NEVER WRITTEN (beyond its default) |
| `systems/threadwork/sim/opposing.py:71` | `OpposingResult.a_degree` | 0 | 0 | 1 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/threadwork/sim/opposing.py:72` | `OpposingResult.b_degree` | 0 | 0 | 1 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/threadwork/sim/opposing.py:75` | `OpposingResult.a_consequences` | 0 | 0 | 1 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
| `systems/threadwork/sim/opposing.py:76` | `OpposingResult.b_consequences` | 0 | 0 | 1 | 0 | NEVER READ + NEVER WRITTEN (beyond its default) |
