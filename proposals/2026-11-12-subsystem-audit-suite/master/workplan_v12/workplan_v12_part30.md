# Workplan v12 — part 30: batches B20-mb-orders and B25-fi-questioning

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12, `V12_STRUCTURE_part3.md` §8; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `9700714` (branch `ccr-62958c70-0kjhsw`), read 2026-11-12; author lane A30 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2. Every item is written against the tree as the batches its `GATE:` lines name will leave it; where a symbol is named that does not exist at `9700714`, the item says which batch makes it.

**What this part holds.** Two batches in execution order: `B20-mb-orders` (the commander's battle: standing orders, the window, the interventions list, the report, the scenario and the commander as a chooser) and `B25-fi-questioning` (formation on what is known, a word with content, a case with a charge, a question the questioned answer, and `tie`). B20's block is in this file; B25's block is in `workplan_v12_part30_cont.md`. A part cites another part's batch or item by handle only.

**Words.** `unified/U1_GLOSSARY.md`. A person's numbers: attribute, skill, skill score, martial skill, derived score (A-98). Armies: army, unit, army formation, unit formation, no size word (A-99, the MB lexicon); a unit's *posture* (the code field `stance` keeps its name). A *lap* is one pass of the season's scene budget; a *round* is one engagement of a fight (A-101). Copied source text that says "round" for the season's pass is corrected to "lap" where it is copied, and the correction is said. The riposte's code id is `finalblow_riposte` (none is named in this part).

**Paths.** As `V12_STRUCTURE.md` states: a bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `IS-A` is `master/instructions/IS_A_NINE.md` and `_part2`; `the intake` is `master/eval/V12_INTAKE.md`. Short names of this part: **MGR** `proposals/04_MB_manager_battle_one_resolver.md`; **MNV** `proposals/26_MASS_BATTLE_maneuver_orders.md`; **SCN** `proposals/04_MB_playable_field_scenario.md`; **CHO** `proposals/27_MB_D_the_commander_as_chooser.md`; **REST_2** `proposals/17_CENSUS_REST_2_wiring.md`; **RES** `proposals/U5b_MB_residue.md`; **IS-B1** `master/instructions/IS_B1_PC_MB_DICE_part2.md`. A path under `engine/`, `modules/`, `tools/`, `references/`, `registers/`, `tests/`, `systems/` is the repository's.

**Names after earlier batches** (`V12_STRUCTURE_part2.md` §5.10): B16L `subformations` → `units`, `Subformation` → `UnitRow`, `stance` (the army row's key) → `posture`, `STANCES` → `POSTURES`; B16M `hierarchy.units.Unit` → `Army`, `Subunit` → `Unit`, `subunits` → `units`, `.broken` → `.disordered`, `max_turns` → `max_ticks`; B03c `harness/populated.py::build_realm` → `boot/realm.py`; B04 `scenes_per_round` → `scenes_per_lap`, `Claim.round` → `Claim.lap`; B04.04 deletes `rosters.yaml: verb_capability` (a verb's skill is the row's own `capability:` cell). Each item's `NAMES:` line says which it uses. Where MB source text says "subunit" for the engine's smallest body it is copied as "unit" (B16M), and "the engine's unit" as "army".

---

## Batch B20-mb-orders · lane MB · wave W16 · step S16 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B20-mb-orders
IN-FLIGHT ROW: registers/handoffs/HANDOFF_MB.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B16L-mb-words
GATE: Batch B05-one-roll
GATE: Batch B15-pc-calibration
GATE: Batch B16-pc-round
GATE: Batch B17-mb-scale
GATE: Batch B19-mb-field-calibration
  (Reached through those, not added as edges: B10 (`make_decider`, B10.57; B15 follows B10) and B11 (`harness/scenarios.py`, B11.05; B16 follows B11 by the edge part 23 states). B20.11, B20.12 and B20.19 name their items; no wave or step moves.)
REQUIREMENT: R-04.c4; R-04.c5 (ii), (iii); R-07.c — read with B19 (IS-A §12.2 row "B19, B20") → `field.won + field.lost` above 0 at seeds 0–2 with the stance receipt on the losing side; the commanded field equals the automatic one with no decider. `status:` is not edited (A-114).
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command):
  `python -m pytest tests/valoria/test_army_battle.py tests/valoria/test_conditional_orders.py tests/valoria/test_mass_battle_signals.py tests/valoria/test_mass_battle_maneuvers.py tests/valoria/test_army_verbs.py tests/valoria/test_mass_battle_officers.py tests/valoria/test_army_menu_presets.py engine/season/tests/test_field_scene.py engine/season/tests/test_march.py engine/season/tests/test_mass_battle_module.py engine/season/tests/test_scenarios_runner.py -q` → all pass;
  `python tools/export_battle_orders.py --check` → exit 0; `python tools/export_troops.py --check` → exit 0; `python tools/ci_golden_modes_check.py` → every digest equal to B19's close (`reading @<sha>`) (no item edits a `bat.py` mode at control);
  `python -m engine.season.harness.field_scene --seed 0 --policy storm`, twice → one `content_hash`, and a `Report` whose last line names an ending kind (IS-B1 P2-1.0, entry);
  `python -m engine.season.harness.aperture 1 s`, s = 0, 1, 2 → `field.won + field.lost` above 0 at each seed, printed beside `field.unopposed`, with `_eff_march`'s `Person.stance` receipt on the losing side (R-04.c4, R-07.c);
  `tests/valoria/test_army_battle.py::test_none_decider_equals_no_decider` (`assert checked >= 200`) → pass (R-04.c5 (iii));
  `git grep -n "attacker_wins\|verdict" modules/mass_battle engine/season/seam/wrappers/mass_battle.py` → prints nothing (MGR gate 5; B17 made it true, B20 keeps it);
  `git grep -n "envelop\|cannae\|refused" modules/mass_battle/massbattle.py modules/mass_battle/battle_loop.py` → prints no branch on a manoeuvre's name (MNV gate 6);
  `python -m engine.season.harness.register --check` → exit 0; `python -m engine.season.harness.register --requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (the batch edits `engine/season` core and registries: the full gates, CLAUDE.md §0.4);
  the glossary rows the items name, read against the code they landed (STAGES "The glossary always matches" rule 2): a mismatch fails the close;
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`, B19's close) and after, `IS-MB-05`'s reading (B20.21), and the batch's measured wall time; B20.99 writes the conjuncts' `reading:` records; `status:` is not edited (`IS-A-12`).
RE-PIN: once, in B20.99: the realm pins in `engine/season/tests/_realm_goldens.py` (B02's one pin file) moved by B20.05, B20.06, B20.13 and B20.14 (every seeded realm that folds a fought field, seed 2 at one season; and every world in which a `march` Candidate is scored under `odds_weighting: believed`), read against B19's close (`reading @<sha>`); the commit says "re-pin: B20.05, B20.06 (Observations on the band Event), B20.13 (the believed field estimate), B20.14 (the aftermath)".
IDS: ED-MB 0; H 0 (no item adds a hole-register row; the fixtures B20.13 and B20.14 add carry `[JUSTIFIED: …]` tags naming their items, not NUMBER rows: `[ASSUMPTION: a `Fixtures` field needs a tag, not a register row — basis: `odds_weighting`'s line in `engine/season/data/fixtures.py` carries a `[JUSTIFIED: …]` tag that names its register row H-248; if `ci_sim_fabrication_check` refuses an untagged-by-row field, the item takes one H id from B20's spare (B00's block plus five)]`)
DIALS AT CONTROL: `orders.obey.arm` = `off` (MNV §1; the 27A-2 key, B19); set by B19's own calibration if its close set it, else B98; target: MNV gate 1 ("the order is applied at tick 3 in some fields, at tick 4 in some, and later or never in some; `orders_fired` records which", n 200). `window_responses` = empty (IS-MB-03 step 5); set by no batch (content: CHAR's cells, G-3); B98 lists it `BLOCKED (content: no authored row)`. `doctrines.<name>.commander_post` = `reserve` for every doctrine (CHO "Data rows": "seed `reserve` for every doctrine, which is the control"); set by B98; target: CHO gate 3 (forward against reserve, n 400, both differences beyond two standard errors). The doctrine choice of an unplayed commander is not a setting here (B22, `create_record`).
UNDECIDED:
  (U-1) **MGR §1 and SCN §C are not items.** §1's rule (`field_degree` reads the two sides' flags; no `verdict`) landed in B17.01 step 6 and B17.03; SCN §C ("each army returns at once to its station") landed in B17.01 step 8 (cost class "C: none"). MGR's gate 5 is read in the batch gate. Other reading: re-land them as pointers; nothing would change.
  (U-2) **SCN §B is not an item** (`V12_STRUCTURE_part2.md` §5.5: superseded in whole by MGR §4; its surviving sentence, the seam forwarding `host.decide`, is B20.03's step 4).
  (U-3) **SCN §G is an item (B20.14)** though U3 §1 item 20 names "A, C, D" only: SCN's own Lands line puts "A, B, C, D and G in B20", U3 §4.1 rows 69–70 split only §E to B22, and B17.02 step 5 closes H-355 on "a routed defender is re-homed", which only §G builds. Other reading: hold §G to B23 with the land; then H-355's text is false from B17 to B23.
  (U-4) **MGR §8 is not an item.** It states a constraint with no edit ("a closed-form odds function is not proposed and should be refused if proposed"); its two conformant ways to pay are used by B20.13 (`believed_field_samples`, a cache keyed on the frozen input). Its falsifier ("a closed-form estimate anywhere in the tree") is read in B20.13's GATE.
  (U-5) **RES §5 with SCN §F (B20.13) and RES §9 R-29 (B20.07)** are carried here, not in B17: B17's part placed them here (its UNDECIDED (3), E-8: the dependency wins), and the orchestrator confirmed it (A11's receipt). They depend on files this batch creates or extends: §5 on `seam/wrappers/mass_battle.py::field_estimate`'s `believed=` (SCN §F, landed in B20.13 itself) and on `seam/wrappers/sigma.py::believed_chance`; R-29 on `FieldOutcome.report` (B20.05).
  (U-6) **SCN §D lands before MGR §6** (B20.05 before B20.06), not after MGR as U3 §1.2 lists the five members: MGR §6 reads "`FieldOutcome.report` (first lane: per phase, per part, …) gains", so §D declares the field; U3 §1.2 gives no edge between the two (its row reads "3. `04_MB_playable…`" with no "needs"). **`FieldOutcome.report` is declared here, in B20.05, and nowhere earlier**: the B19 author blocked B19.27 (`27_MB_C` 27C-1's `report.draws` and the per-bout report of `26_MASS_BATTLE_cell_scale_and_time` §3) on B20 for want of this field (the orchestrator's relay of A26's receipt); B19.27 consumes it when it lands, adding its members to the record B20.05 declares. Because three sources add named members to the report (SCN §D the phases, MGR §6 `orders_fired` and `interventions`, RES R-29 `truncated_troops`) and a fourth waits (27C-1 `draws`), B20.05 declares it as a frozen record with named fields, not SCN §D's bare `tuple`. Other reading: SCN's `tuple` of `PhaseSummary`, to which the others could not add a named member.
  (U-7) **IS-MB-01's step 2 (registry first) is applied inside B20.11 (SCN §A)**, so §A never writes a season loop that B20.12 then deletes; B20.12 keeps IS-MB-01's steps 1 and 3 and its four tests. Other reading: §A as written, then IS-MB-01 replaces `play`'s loop (two commits over one function).
  (U-8) **The `doctrines:` block of `references/troops.yaml`** is first needed here (MGR §2's doctrine bullet, MNV §3's rows, CHO's `commander_post`) though SCN §E (B22) moves `ARM_SHARES` into it: B20.10 creates the block with `balanced` and MNV §3's rows (orders, posts, `commander_post`) and no shares; §E in B22 adds the shares to the same rows. Other reading: create the block in B22 and hold MNV §3 and CHO's data row to B22.
  (U-9) **Post names**: CHO's data row lists `front`; IS-MB-03 step 3 and the MB lexicon's post row name it `centre`. The items write `centre` (the lexicon governs, `V12_STRUCTURE_part2.md` §5.11) and say so.
  (U-10) **IS-MB-03 step 1's "`IS-B2-CHAR-02` gains the `bias` argument"** is already in B10.57's signature (`make_decider(p, fx, draw, *, key, odds=None, bias=None, watch=None)`): B20.19 adds nothing to `decider.py` and calls it.
  (U-11) **MNV §1 at this tree**: `27_MB_A` 27A-4 (B19) already makes `core/contact.py::check_orders` call `obey` before applying a behaviour, at `arm: off`. B20.08 adds what B19 could not: the draw for a general's `signal` and `order` actions and for the lull actions (they need MGR §4 and MNV §2), and MNV §1's step table rows if 27A-2 did not author them (a SITE step).
C(B20-mb-orders): this batch's entries; the plan's head parts; `unified/U1_GLOSSARY.md` rows *posture*, *standing order*, *window*, *doctrine*, *end state*, *report*, *obey*;
  `modules/mass_battle/massbattle.py`, `battle_loop.py`, `armyrecord.py`, `orderofbattle.py`, `armies.py`, `orchestration.py`, `core/contact.py`, `hierarchy/units.py`, `config.py`, `troop_types/presets.py`; `references/troops.yaml`; `tools/export_battle_orders.py`; `engine/engine_params/battle_orders.json`; `engine/substrate/battle_orders.py`; `tools/export_troops.py`; `engine/engine_params/troops.json`;
  `engine/season/queries/inputs.py` (`MassBattleInput`, `FieldOutcome`, `CommandRecord`); `engine/season/seam/wrappers/mass_battle.py` (`resolve`, `field_input`, `field_estimate`); `engine/season/seam/wrappers/sigma.py` (`believed_chance`); `engine/season/seam/wrappers/combat.py` (the party test, read only); `engine/season/loop/effects_combat.py` (`_eff_march`); `engine/season/loop/effects_army.py`; `engine/season/loop/effects_migration.py` (`_relocate`, read only); `engine/season/harness/military_menu.py`, `army_presets.py`, `play_surface.py`, `scenarios.py`; NEW `engine/season/harness/field_scene.py`; `engine/season/decision/decider.py` (read only); `engine/season/data/verbs.py` (`CHOICE_RANGES`); `engine/season/data/rosters.py`; `engine/season/data/fixtures.py`; `engine/season/rosters.yaml` (`observation_terms`, `window_responses`); `engine/season/queries/world_q.py` (`governing_hold`), `person_q.py` (`held_against`) read only;
  the tests named in the items; instruments: `aperture`, `register`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`, `tools/ci_golden_modes_check.py`, `tools/ci_sim_fabrication_check.py`; `engine/season/tests/_realm_goldens.py`;
  the closing SHAs of B00, B01, B02, B16L, B05, B15, B16, B17, B19 (and B10, B11, reached through them); the permanent surface.
SERIAL EDGES (written after the position table, E-11): within the batch: B20.01 → B20.02 (the strategy key is re-read once the order rows exist) and → B20.03 (`order` applies "one behaviour from the standing-order set") → B20.04 (the list carries `GeneralAction`) → B20.05 (`report` declared) → B20.06 (gains two fields) and → B20.07 (one figure on the same field); B20.03 → B20.08 (the actions to draw for) → B20.09 (`GeneralAction.kind` gains the lull kinds; the triggers join the exported sets) → B20.10 (doctrine rows name the new triggers and behaviours); B20.06 → B20.11 (the scenario's `Report` reads `FieldOutcome.report`) → B20.12 → B20.13 (the believed estimate is shown in `Report`); B20.06 → B20.14 (`_eff_march`, after B20.05 and B20.06 in the same function); B20.08 → B20.15 (`obey_odds` shares `_obey_terms`) → B20.16 → B20.17 (B20.10's doctrine rows gain `commander_post`) → B20.19 (the window decider reads the view) ; B20.18 points at B20.19; B20.01 → B20.20 (the row form gains `ally`); B20.21 reads the batch's tree; B20.99 last. Hash-EQUAL items precede the movers wherever the sources allow (§5.9): B20.05 and B20.06 are movers placed where the report exists, because B20.07, B20.11 and B20.16 read it.
  With other batches, by file (U3 §5.1 rows, in v12's landing order): `seam/wrappers/mass_battle.py` B16M → B17 → B19 → B20 → B22 → (B23, B30) → B31; `troops.yaml` B17 → B19a → B19 → B20 → B22 → B30 → B31; `massbattle.py` B16L → B16M → B17 → B19 → B20 → B31; `armyrecord.py` B19 → B20 → B22 → B31; `battle_loop.py` B16M → B17 → B15 → B19 → B20; `orderofbattle.py` B16L → B17 → B19 → B20 → (B22, B32) → B31; `battle_orders.json`, `tools/export_battle_orders.py` B19 → B20 → B30; `hierarchy/units.py`, `orchestration.py` B16M → B17 → B19 → B20; `core/contact.py` B19 → B20 → B32; `military_menu.py` B20 → B21 (U3's row; in v12's schedule B21 closes at S12, so the menu's B21 edit lands first and B20 edits after it, by function); `effects_army.py` B21 → B20 → B22 (same reason); `effects_combat.py` B04 → B14 → B17 → (B12a–c, B16) → B19 → B20 → B22 → B23 → B31; `harness/field_scene.py` B20 → B22 (`IS-MB-02` step 6) → B30 (`IS-MB-04`) → B34; `harness/scenarios.py` B11 → B12 → B16 → B20 → B21… (appended at the end of the mapping, in merge order: IS-B1 P2-3.2); `data/verbs.py` (`CHOICE_RANGES`) B16 → B20; `rosters.yaml` (hot: `window_responses` at the end of the choice family's block, `observation_terms` appended at its end; CIP part 2 §5 note 1); `data/fixtures.py` (hot: `believed_field_samples`, `field_aftermath`, new keys at the end of their family); `seam/wrappers/sigma.py` (hot: `believed_chance` only).
PARALLEL: S16 with B11F1-flow-se (SE), B25-fi-questioning (FI), B27-sc-proceedings (SC), B37-happenings (IN). Shared files: with B25, `rosters.yaml`, `data/fixtures.py`, `data/verbs.py`, `seam/wrappers/sigma.py` (B20: `window_responses`, `observation_terms`, two fixtures, `CHOICE_RANGES`, `believed_chance`; B25: other keys and functions, its block's census); with B27 and B37 the same hot files by key (the coordinator reads the census at the step's open, `V12_STRUCTURE_part3.md` §7.3). The mover batches of the step merge in §2.1's order (B11F1, B20, B25, B27, B37 as listed there): B20 rebases on B11F1's merge and re-pins once in B20.99 (§7.4).
COST: small builds and edits; producer `valoria-author` on `sonnet`, `high`; MB review of the seam edits, IN review of B20.19's call into `decision/`; the doctrine readings `haiku` read by `opus` (MNV); the close's terminal critique `opus` (IS-MB-03's function is read there).
EST: 12 h [estimate: `V12_STRUCTURE.md` §2.4's per-commit formula over this batch's 23 positions (0.4 h × 23 + 2.5 h); §2.2's 5 h counted the five members, not the commits they order]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B20.01 | standing orders on the unit row, from closed sets | MGR §2 | BUILD | EQUAL | Batch B19 |
| B20.02 | the strategy roster leaves the choice surface | MGR §3 | BUILD | EQUAL | B20.01 |
| B20.03 | one general's action at each window of the same call | MGR §4 | BUILD | EQUAL | B20.01; Batch B16 |
| B20.04 | the interventions list: one slice at every depth | MGR §5 | BUILD | EQUAL | B20.03 |
| B20.05 | the report: what each phase cost each side | SCN §D | BUILD | MOVER(behaviour) | B20.04 |
| B20.06 | the report names the orders that fired and the actions taken | MGR §6 | BUILD | MOVER(behaviour) | B20.05 |
| B20.07 | the troops past the fifth depth group are reported | RES §9 R-29 | BUILD | EQUAL | B20.05 |
| B20.08 | a general's order is obeyed by a draw, as a standing order is | MNV §1 | BUILD | EQUAL | B20.03; Batch B19 |
| B20.09 | two triggers, three behaviours, three lull actions | MNV §2 | BUILD | EQUAL | B20.08 |
| B20.10 | the manoeuvres as doctrine rows; the bait's own draw | MNV §3, its exact-edit rows | BUILD | EQUAL | B20.09 |
| B20.11 | the battle scenario and its instrument | SCN §A with `IS-MB-01` step 2 | BUILD | EQUAL | B20.06; Batch B11 |
| B20.12 | the scenario's command line, its policies, its ending kinds | `IS-MB-01` steps 1, 3 | BUILD | EQUAL | B20.11 |
| B20.13 | a commander may weigh a field by what he believes | RES §5 with SCN §F | BUILD | MOVER(behaviour) | B20.11; Batch B05 |
| B20.14 | after a won field: the routed re-homed, a grudge eased | SCN §G | BUILD | MOVER(behaviour) | B20.06 |
| B20.15 | the odds of one order, from the dice owner | CHO 27D-1 | BUILD | EQUAL | B20.08 |
| B20.16 | what a commander is shown at a window | CHO 27D-2 | BUILD | EQUAL | B20.15, B20.13 |
| B20.17 | who commands each unit and where the commander rides | CHO 27D-3 | BUILD | EQUAL | B20.16, B20.10 |
| B20.18 | the unplayed commander's decider | CHO 27D-4 | POINTER | — | B20.19 |
| B20.19 | an unplayed commander acts at a window | `IS-MB-03` | BUILD | EQUAL | B20.17, B20.12; Batch B10 |
| B20.20 | `ally_at:D` has an ally | REST_2 W1 | BUILD | EQUAL | B20.01 |
| B20.21 | mass battle's integrated reading at this close | `IS-MB-05` | READING | — | B20.01 to B20.20 |
| B20.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | B20.01 to B20.21 |

Consumed by another batch's item: B19.27 (`27_MB_C` 27C-1's `report.draws` and the per-bout report), BLOCKED in B19 on `FieldOutcome.report`, which B20.05 declares (U-6); no `T-` row id is used in this batch (`T-11` belongs to `27_MB_E` and MBA-08). Not in this batch, and where each is: MGR §1 (B17.01, B17.03; U-1); MGR §7, the officers' duel (B30, MGR's own Lands line); MGR §8 (U-4); SCN §B (U-2); SCN §C (B17.01; U-1); SCN §E (B22, U3 §4.1 rows 69–70); RES §1, §2, §4 item 2, §6, §9 R-24 (B17); RES §3 (B22); RES §4 item 1 (after B19; B17's part); REST_2 W2 (B24, B24.36), W3 (B35), W5 (B32); `IS-MB-02` (B22; adds `besiege_then_storm` to B20.12's `POLICIES`); `IS-MB-04` (B30); `IS-MB-01` step 4 and the `FIXTURES["field"]` line (B34); CHO 27D-4's cells (CHAR's content; G-3).

### B20.01 — standing orders on the unit row, from closed sets · MGR §2 · BUILD · HASH EQUAL
- SOURCE: MGR "The resolution, decided" §2, "Gate" 3, "Tests (W3-1)" (gate 3), "Cost class"; D-U1-11f (`standing_order_cap`); rulings A-2 (`officer` and `standing_orders` are columns of the unit row); closes R-39 of `audits/04_MB_audit_addendum_B.md` §B6 (F-MB-21's lever half).
- ADVANCES: R-04.c5 (iii) (orders a commander sets reach the field); IS-B1 P2-1.0 "a choice that matters".
- INSTRUCTION (MGR §2, copied):
  ```
  standing_orders: ((trigger, behaviour), ...)     # at most `standing_order_cap` (seed 4; battle_orders.json, D-U1-11f), in priority order
  trigger   ∈ immediate | tick:N | enemy_range:D | ally_at:D | own_strength:F | signal:NAME | flanked | volleys_spent
  behaviour ⊂ { stance, target_condition, yielding, conceded, route, in_hand, fire_signal }
  ```
  1. "The two sets are exported beside the order vocabulary (`tools/export_battle_orders.py`, `engine/engine_params/battle_orders.json` gains `triggers`, `behaviours` and the scalar `standing_order_cap`, read through `engine/substrate/battle_orders.py`; `armyrecord.order` refuses a list longer than it, so no literal 4 lives in `armyrecord`), from `hierarchy/units.py::_ORDER_TRIGGER_KINDS` and a named subset of `_ORDER_SAFE_FIELDS`. `flanked` and `volleys_spent` are added by `04_MB_unit_loadout_and_weapon_in_hand_B.md`." First step (SITE): open `_ORDER_TRIGGER_KINDS` and record in the commit body whether `flanked` and `volleys_spent` are present (loadout_B stages 1–2 landed in B17.10–B17.11; its stages 3–4 are B31's); a trigger not yet in the engine's set is not exported here and is named in the commit body.
  2. "`modules/mass_battle/armyrecord.py::order` validates a row against those sets and refuses by name; `immediate` is legal only as the last row (an unconditional first row starves the rest)."
  3. "`orderofbattle._spec_for` builds one `Order` per row. `fall_back_at` leaves the record: it is the row `(own_strength:F, {stance: retreat})`." Every reader of `fall_back_at` (`git grep -n fall_back_at` at the open: `harness/military_menu.py` and `loop/effects_army.py` at `9700714`) reads the row instead.
  4. "The `order_unit` verb's payload carries the list (`engine/season/loop/effects_army.py`); the menu (`harness/military_menu.py`) offers the closed sets."
  5. MGR §2's last bullet (the doctrine row writes an unplayed commander's standing orders) lands with B20.10, which creates the doctrine rows (U-8).
  6. Glossary: row *standing order* (add if absent): "standing order: an instruction a commander gives a unit before the battle, to be carried out when its trigger holds, as an army's standing orders are"; owner `battle_orders.json: triggers, behaviours`.
- WHERE: `tools/export_battle_orders.py`; `engine/engine_params/battle_orders.json` (re-derived by the tool); `engine/substrate/battle_orders.py`; `modules/mass_battle/armyrecord.py` (`order`); `modules/mass_battle/orderofbattle.py` (`_spec_for`); `engine/season/loop/effects_army.py` (`order_unit`'s payload); `engine/season/harness/military_menu.py`; `tests/valoria/test_conditional_orders.py`; `unified/U1_GLOSSARY.md` (*standing order*).
- TESTS: in `tests/valoria/test_conditional_orders.py`, written before step 2 and read red: `test_standing_orders_fire_and_report` (MGR gate 3: "A unit with `((enemy_range:4, {stance: hold}), (own_strength:0.6, {stance: retreat}))` holds when the enemy comes within four and retreats at 60%"; the `orders_fired` half of that gate is completed at B20.06), `test_unknown_trigger_refused_by_name` ("a row with an unknown trigger is refused by name at `order_unit`"), `test_more_than_standing_order_cap_rows_refused`, and `test_immediate_only_as_the_last_row` `[ASSUMPTION: test name; the item creates it]`.
- FALSIFIER and CONTROL: "a standing order that cannot change an outcome at any of 200 seeds" (MGR Falsifier; read at B20.12's `test_a_fall_back_point_changes_some_battle`). Control: a side with no standing orders: `python tools/ci_golden_modes_check.py` digests and the seed-0 one-season realm hash equal to B19's close (`reading @<sha>`) ("Nothing for a side that has no standing orders").
- GATE: `python tools/export_battle_orders.py --check` → exit 0; `python -m pytest tests/valoria/test_conditional_orders.py tests/valoria/test_mass_battle_signals.py -q` → pass; realm hash at seed 0, one season → equal.
- HASH MOVERS: none ("none for a side with no orders").
- DEPENDS ON: EXISTS-IN-TREE `hierarchy/units.py::_ORDER_TRIGGER_KINDS`, `::_ORDER_SAFE_FIELDS`, `::Order`, `armyrecord.py::order`, `orderofbattle.py::_spec_for`, `tools/export_battle_orders.py`, `engine/substrate/battle_orders.py`, `harness/military_menu.py`; V12 Batch B19 (27A-2's `obey` key and 27A-3's `officer` column in the same files).
- GLOSSARY: *standing order* (step 6).
- NAMES: `subformation` → unit row (`UnitRow`, B16L) where MGR says "the unit row"; `Subunit` → `Unit` (B16M) in `_spec_for`'s spec.
- COST and TIER: small build; `sonnet`, `high`; MB review.
- LANDS IT: B20's `valoria-author` producer, `isolation: worktree`; `Item: B20.01`, `[skip ci]`.

### B20.02 — the strategy roster leaves the choice surface · MGR §3 · BUILD · HASH EQUAL
- SOURCE: MGR §3, "Gate" 4, "Tests (W3-1)" (gate 4); closes R-34 (F-MB-21's trap half).
- ADVANCES: none of the nine; a lever that loses to the default leaves the menu.
- INSTRUCTION (copied): "`STRATEGIES`' `advance` and `defend` are removed from `armyrecord`'s accepted values and from the menu; the record's `strategy` key carries the army's **formation** name (`04_MB_cell_hierarchy_as_data.md`), whose default `line` is today's deployment. A posture is still settable per unit by a standing order. An army-wide posture returns as a roster only when each value beats the default in some named matchup and none beats it in a mirror by more than the same-run control." First step (W3-1, test 9): "the scratch `lever_probe` is first written as `systems/mass_battle/sim/lever_probe.py`; expected output the control row of the even combined-arms field at n 200, 59 wins to 49, unchanged by the edit"; run it before and after the edit and record both in the commit body.
- WHERE: `modules/mass_battle/armyrecord.py` (`STRATEGIES`, `order`'s `strategy` check); `modules/mass_battle/orderofbattle.py` (`STRATEGIES` if read there); `engine/season/harness/military_menu.py`; NEW `systems/mass_battle/sim/lever_probe.py`; `tests/valoria/test_army_verbs.py`.
- TESTS: `tests/valoria/test_army_verbs.py::test_advance_and_defend_refused`, written first, red.
- FALSIFIER and CONTROL: the probe's control row moves (then the edit changed a default field). Control: "the addendum's `lever_probe` control row is unchanged" (59 to 49 at n 200).
- GATE: `python -m pytest tests/valoria/test_army_verbs.py -q` → pass; `python systems/mass_battle/sim/lever_probe.py` → the control row `59 / 49` (n 200), equal before and after.
- HASH MOVERS: none (`advance`/`defend` are formed by no season act: the army verbs are withheld).
- DEPENDS ON: EXISTS-IN-TREE `armyrecord.py::STRATEGIES`, `orderofbattle.py::STRATEGIES`; V12 Batch B19 (`04_MB_cell_hierarchy_as_data`'s formations, which the `strategy` key names).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B20's producer; `Item: B20.02`, `[skip ci]`.

### B20.03 — one general's action at each window of the same call · MGR §4 · BUILD · HASH EQUAL
- SOURCE: MGR §4 (copied), "Gate" 1, 7, "Tests (W3-1)" (gates 1–2); Layer 1 nodes `L1-A3`, `L1-A4` (APPLIED, A-97: the field decider is a declared adapter input); rulings A-1, A-2, A-59 (`rally` on the `command` skill, D-U1-11g); closes R-31's remainder, F-MB-24.
- ADVANCES: R-04.c5 (iii).
- INSTRUCTION (copied):
  1. "`modules/mass_battle/massbattle.py::resolve_field(inp, rng, *, troops_a=None, troops_b=None, decide=None)`; `battle_loop.run_battle(..., on_window=None)` called where `phase_boundary` is called, after it." (B17.12 already gave `resolve_field` the keywords `cfg`, `decide`, `duel` "that nothing passes yet"; this item gives `decide` its reader.)
     ```python
     @dataclass(frozen=True)
     class FieldWindowView:          # one side's own view; built by the module, never a Unit
         window: int                 # 1-based
         side: str
         units: tuple                # ((name, share, routed, in_contact, in_hand, orders_pending), ...)
         signals_fired: tuple

     @dataclass(frozen=True)
     class GeneralAction:
         kind: str                   # 'signal' | 'order' | 'rally' | 'withdraw' | 'none'
         unit: Optional[str] = None  # for 'order' and 'rally'
         arg: Any = None             # a signal name, or one behaviour from the standing-order set
     ```
     | action | what it does, by an existing primitive |
     |---|---|
     | `signal` | adds the name to `Unit.fired_signals`: every order waiting on `signal:NAME` fires, on every unit |
     | `order` | applies one behaviour dict to one unit, through the same validation an `Order` uses |
     | `rally` | the commander's hook: `rally_check` for that unit, a draw on the commander's `command` skill (carried on `CommandRecord`, `27_MB_A` §2; the old integer `MassBattleInput.command` is retired, D-U1-11g) restoring morale toward its start |
     | `withdraw` | the retreat `_retreat_orders` already sets on every unit |
     | `none` | nothing |
  2. "One action a window; the count of windows is the engine's phase boundaries (two in an 18-tick engagement). `signal` is the prepared act and `order` the improvised one."
  3. "The wrapper never hands the decider a `Unit`, and the decider is handed nothing of the other side but what is in contact with its own units."
  4. "`engine/season/seam/wrappers/mass_battle.py::resolve` forwards `host.decide` for a played claimant or defending commander, as `seam/wrappers/combat.py` does (REM-31 …). A commander nobody plays has no decider by default; CHAR may supply one through the same parameter" (B20.19). SCN §B's sentence, kept: "The `host` keyword is already in the signature."
- WHERE: `modules/mass_battle/massbattle.py` (`resolve_field`, `FieldWindowView`, `GeneralAction`); `modules/mass_battle/battle_loop.py` (`run_battle`'s `on_window`, at the `phase_boundary` call); `engine/season/seam/wrappers/mass_battle.py` (`resolve`); `tests/valoria/test_army_battle.py`.
- TESTS: in `tests/valoria/test_army_battle.py`, written first, red (no `decide` reader): `test_none_decider_equals_no_decider` (MGR gate 1: "Seeds 0 to 199 on an army field: `decide=None`, and a decider that always returns `none`, give equal outcomes and an equal count of draws from `rng`"; `assert checked >= 200`); `test_a_window_view_holds_no_unit_object` `[ASSUMPTION: test name; the item creates it]` (gate 7's spirit at the view: every element of `FieldWindowView.units` is a tuple of plain values).
- FALSIFIER and CONTROL: "A decider that changes the draw count" (MGR). Control: `decide=None` reproduces B19's close digests (`tools/ci_golden_modes_check.py`) and realm hash.
- GATE: `python -m pytest tests/valoria/test_army_battle.py -q` → pass; `python tools/ci_golden_modes_check.py` → digests equal; the reach probe of MGR gate 7 ("No function under `modules/mass_battle/` is entered by the commanded run and not by the delegated one") run on a hand-built field under the two modes and its two lists recorded in the commit body.
- HASH MOVERS: none (no host passes a decider in natural play).
- DEPENDS ON: EXISTS-IN-TREE `battle_loop.py::run_battle` (the `phase_boundary` call), `massbattle.py::_retreat_orders`, `orchestration.py::rally_check`, `hierarchy/units.py` (`fired_signals`), `seam/wrappers/combat.py` (the forwarding precedent); V12 Batch B19 (`CommandRecord`, 27A-1; `rally` on `command`); V12 Batch B17 (B17.12's keywords).
- GLOSSARY: row *window* (add if absent): "window: a pause inside one battle at which a commander may take one action, as a window of opportunity is"; owner `battle_loop.run_battle`'s `on_window`.
- NAMES: "Unit" in the view's comment is the engine's smallest body after B16M (`Unit`, formerly `Subunit`); the army is `Army`.
- COST and TIER: small build (after §2); `sonnet`, `high`; MB review of the seam.
- LANDS IT: B20's producer; `Item: B20.03`, `[skip ci]`.

### B20.04 — the interventions list: one slice at every depth · MGR §5 · BUILD · HASH EQUAL
- SOURCE: MGR §5 (copied), "Gate" 2, "Tests (W3-1)"; rulings A-1, A-30 (keyed draws); closes the addendum's §B5.4 (R-45's fidelity half).
- ADVANCES: R-04.c5 (iii) (the commanded and the delegated battle are one call).
- INSTRUCTION (copied): "`MassBattleInput.interventions: tuple = ()`, each `(side, window, GeneralAction)`. When no decider is given, the module applies the listed action at its window. `FieldOutcome.interventions` returns the actions a decider took. So: **delegated** = `resolve_field(inp, rng)`: standing orders decide; **commanded** = `resolve_field(inp, rng, decide=d)`; **the same battle, summarised or replayed** = `resolve_field(replace(inp, interventions=out.interventions), rng)`, which returns the identical outcome." "A decider draws nothing, and every draw the module makes is keyed `(field, tick, unit, purpose)` through `11_GO_one_draw_owner.md`'s owner, the same keys for a standing order, a decider's action and a replayed intervention, so the draws do not depend on who decided." `FieldOutcome.interventions` is declared here (D-U1-11e: a field of the one `FieldOutcome` declared by the proposal that lands it).
- WHERE: `engine/season/queries/inputs.py` (`MassBattleInput.interventions`, `FieldOutcome.interventions`); `modules/mass_battle/massbattle.py` (`resolve_field`: apply the listed action at its window when `decide` is `None`; collect a decider's actions); `tests/valoria/test_army_battle.py`.
- TESTS: `tests/valoria/test_army_battle.py::test_replay_from_interventions_is_identical`, written first, red (MGR gate 2: "A scripted decider (fire a signal at window 1, order one unit to `hold` at window 2): the outcome differs from the control at some seed; feeding its returned `interventions` back with no decider gives an outcome equal field by field, at every one of the 200 seeds"; `assert checked >= 200`).
- FALSIFIER and CONTROL: "a commanded battle whose replay from its interventions differs in any field" (MGR). Control: `interventions=()` with no decider reproduces B20.03's digests.
- GATE: `python -m pytest tests/valoria/test_army_battle.py -q` → pass; `python tools/ci_golden_modes_check.py` → equal.
- HASH MOVERS: none (`MassBattleInput` and `FieldOutcome` are seam records, not `World` carriers: neither is in `World.content_hash()`'s reach `[ASSUMPTION: basis — `state/world.py::_encode_into` walks `World._STATE_COLLECTIONS`; a field of an input or outcome record is not stored on the world; if the item finds either stored, it is MOVER(encoding) and re-pinned in B20.99]`).
- DEPENDS ON: V12 B20.03; V12 Batch B06 (the keyed draw owner, `11_GO_one_draw_owner`; reached through B16); V12 Batch B17 (`FieldOutcome`, B17.03).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B20's producer; `Item: B20.04`, `[skip ci]`.

### B20.05 — the report: what each phase cost each side · SCN §D · BUILD · HASH MOVER(behaviour)
- SOURCE: SCN "The resolution, decided" §D (copied), "Gate" 3, "Tests (W3-1)" (gate 3); D-U1-06 (Observations are `observation_terms` members); D-U1-11e; closes R-11 (`audits/04_MB_audit.md` §8 step 4b).
- ADVANCES: R-07.c (a field leaves a story the losing side carries); IS-B1 P2-1.0 "player-facing surface: after".
- INSTRUCTION: (U-6) this item declares `FieldOutcome.report` (D-U1-11e: "the other fields of the one `FieldOutcome` land each with its own proposal"); B19.27 (BLOCKED in B19 on this field: `27_MB_C` 27C-1's `draws` and the per-bout report) consumes it. Declared as `report: FieldReport = FieldReport()`, a frozen dataclass in `queries/inputs.py` whose first field is `phases: tuple = ()` (SCN §D's tuple), each later member added by its own item (B20.06, B20.07; 27C-1's `draws` when B19.27 lands) with a default, so a `FieldOutcome` built by any arm before them stays valid. Then, copied, as `phases`: "`FieldOutcome.report: tuple` of at most three `PhaseSummary(phase, attacker=(lost_share, parts_broken), defender=(...), flanked: (bool, bool))`, built in `massbattle.py` from the engine's own trace categories (`casualty`, `melee`) with `resolution.tracing()` opened inside the call and closed before it returns. `_eff_march` writes `broke_observed` for both sides [landed, B17.03] and one `Observation` per phase summary on the band Event (an Event has no payload field; Observations are its carrier, as CP-T04-01 established; each predicate a member of `rosters.yaml: observation_terms`, D-U1-06). A bystander's account of a battle is then something `tell` can carry." The new predicate (`phase_summary` `[ASSUMPTION: the predicate's name — basis: none in SCN; the item names it once in `observation_terms` and the glossary]`) is appended at the end of `observation_terms`.
- WHERE: `engine/season/queries/inputs.py` (`PhaseSummary`, `FieldReport`, `FieldOutcome.report`); `modules/mass_battle/massbattle.py` (`resolve_field`: the tracing block); `engine/season/loop/effects_combat.py` (`_eff_march`); `engine/season/rosters.yaml` (`observation_terms`); NEW `engine/season/tests/test_field_scene.py` (this item's test only; B20.11 adds the scenario's).
- TESTS: `engine/season/tests/test_field_scene.py::test_field_event_names_who_broke_first` (SCN gate 3: "A folded field's Event carries, for both sides, who broke first and in which phase"), written first, red (no phase Observation).
- FALSIFIER and CONTROL: a phase summary whose `lost_share` does not match the side's share drop over that phase (read off the same trace). Control: a field fought by no season act (seeds 0 and 1, one season): realm hash equal to B20.04's.
- GATE: `python -m pytest engine/season/tests/test_field_scene.py -k broke_first -q` → pass; the seed-2 one-season realm hash → moved (its fought field's band Event gains Observations), act tallies equal; recorded for B20.99.
- EXPECTED RED UNTIL: B20.99 for the seed-2 pin of `_realm_goldens.py` (under `[skip ci]`).
- HASH MOVERS: every seeded realm that folds a fought field (seed 2 at one season, B17's reading). Declared; B20.99.
- DEPENDS ON: V12 B20.04; V12 Batch B17 (B17.03: `broke_observed`, `observation_terms`); EXISTS-IN-TREE `modules/mass_battle` `resolution.tracing()` `[ASSUMPTION: the context manager's module — basis: SCN names `resolution.tracing()`; the item opens `modules/mass_battle/resolution.py` and records the symbol]`.
- GLOSSARY: row *report* (field sense) or a sentence on it: "the report: what each phase of a battle cost each side, as a commander's after-action report says".
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B20's producer; `Item: B20.05`, `[skip ci]`.

### B20.06 — the report names the orders that fired and the actions taken · MGR §6 · BUILD · HASH MOVER(behaviour)
- SOURCE: MGR §6 (copied; the struck `fortune` pair not carried, A-59, A-77), "Gate" 3 (its `orders_fired` half), "Falsifier"; D-U1-06.
- ADVANCES: R-07.c; R-04.c5 (iii) (a player can read his own orders back).
- INSTRUCTION (copied): "`FieldOutcome.report` … gains: `orders_fired: ((tick, unit, trigger), ...)`, from one `trace_event('order', …)` at the point `core/contact.check_orders` applies a behaviour (the only engine addition in this proposal); `interventions`, as above [B20.04]." "`_eff_march` writes these as Observations on the band Event (first lane, step 4b), as members of `rosters.yaml: observation_terms` on `Event.observed` (D-U1-06)." The predicates (`order_fired`, `intervention` `[ASSUMPTION: names — basis: none in MGR; appended at the end of `observation_terms`]`).
- WHERE: `modules/mass_battle/core/contact.py` (`check_orders`: one `trace_event('order', …)`); `modules/mass_battle/massbattle.py` (the report's two fields); `engine/season/loop/effects_combat.py` (`_eff_march`); `engine/season/rosters.yaml` (`observation_terms`); `tests/valoria/test_conditional_orders.py`.
- TESTS: `test_standing_orders_fire_and_report` (B20.01) gains its second half: "`orders_fired` names both with their ticks" (MGR gate 3); `test_orders_fired_is_empty_with_no_orders` `[ASSUMPTION: test name; the item creates it]`.
- FALSIFIER and CONTROL: "a report whose `orders_fired` is empty when an order visibly fired" (MGR). Control: a field with no orders reports `orders_fired == ()`; realm hash at seeds 0 and 1, one season, equal to B20.05's.
- GATE: `python -m pytest tests/valoria/test_conditional_orders.py -q` → pass; the seed-2 one-season realm hash → moved or equal, recorded (moved only if the realm's field carries an order: the record's `fall_back_at` row does, B20.01 step 3).
- HASH MOVERS: as B20.05 (Observations on a fought field's band Event). Declared; B20.99.
- DEPENDS ON: V12 B20.05, B20.04; EXISTS-IN-TREE `core/contact.py::check_orders`, `trace_event`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B20's producer; `Item: B20.06`, `[skip ci]`.

### B20.07 — the troops past the fifth depth group are reported · RES §9 R-29 · BUILD · HASH EQUAL
- SOURCE: RES §9, row R-29 (copied); carried here from B17 (U-5): it depends on `FieldOutcome.report` (B20.05); closes the first audit's R-29.
- ADVANCES: none of the nine; a battle's account does not hide men it dropped.
- INSTRUCTION (copied): "`modules/mass_battle/massbattle.py::_run_and_grade`; `FieldOutcome.report` (`04_MB_playable_field_scenario.md` §D): the count of troops in engagement groups past the fifth depth group, which `run_battle` already returns and `_run_and_grade` drops, rides the report as one figure, `truncated_troops`."
- WHERE: `modules/mass_battle/massbattle.py` (`_run_and_grade`); `engine/season/queries/inputs.py` (the report's `truncated_troops`); `engine/season/tests/test_mass_battle_module.py`.
- TESTS: `test_mass_battle_module.py::test_truncated_troops_are_reported` `[ASSUMPTION: test name; the item creates it]`, written first, red: RES's gate, "a field built to exceed five depth groups reports a non-zero figure; an ordinary field reports 0".
- FALSIFIER and CONTROL: an over-deep field that reports 0. Control: an ordinary field reports 0; realm hash equal to B20.06's ("R-29 moves nothing": `_eff_march` does not write the figure).
- GATE: `python -m pytest engine/season/tests/test_mass_battle_module.py -q` → pass; realm hash at seed 2, one season → equal to B20.06's reading.
- HASH MOVERS: none.
- DEPENDS ON: V12 B20.05 (`FieldOutcome.report`); EXISTS-IN-TREE `massbattle.py::_run_and_grade`, `battle_loop.run_battle`'s return (the depth-group count) `[ASSUMPTION: the return key — basis: RES "which `run_battle` already returns"; the item opens `run_battle` and names the key in the commit body]`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B20's producer; `Item: B20.07`, `[skip ci]`.

### B20.08 — a general's order is obeyed by a draw, as a standing order is · MNV §1 · BUILD · HASH EQUAL
- SOURCE: MNV "The resolution, decided" §1 (as W3-1 reconciled it: the pool and obstacle are `27_MB_A` §4's), "Gate" 1–2, "Tests (W3-1)", "Falsifier"; rulings A-6, A-7, A-30, A-59; closes rows B-2, B-3 of `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` for the general's actions.
- ADVANCES: R-04.c5 (iii) (a commander's order can fail, as a plan can).
- INSTRUCTION (U-11):
  1. SITE: open `modules/mass_battle/core/contact.py` and record in the commit body what B19 left: `obey`, `_obey_terms`, `_roller_for`, and whether `check_orders` calls `obey` before applying a behaviour (27A-4: "`check_orders` … calls `obey` before the `for k, v in order.behavior.items()` loop and applies on `obeyed`, sets `sub._order_due` on `late`, leaves the order pending on `not carried out`"). If it does not, this item stops (`STOPPED`: B19 did not land 27A-4) and says so.
  2. The general's `signal` and `order` actions (B20.03) are drawn through the same `obey`, "whoever issued the order (a standing order, a decider, a replayed intervention), so the draws do not depend on who decided": "the roller is each person who has to pass the order on (the unit's officer for a standing order; the commander and then the officer for an improvised one); his pool is the one pool rule on his trained `command` (A-6, A-7), his Presence and Reason enter as levels; the obstacle is the one task obstacle plus the step for the kind of order below (`orders.obey.step`); the draw is `core/contact.py::obey`, keyed `(field, tick, unit, "obey", link)` (A-30)." Bands, copied:
     ```
     degree   -> Overwhelming, Success : applied this tick
                 Partial               : applied late (one tick plus the distance steps; on a unit holding orders
                                         on two signals, the wrong one: 27_MB_A §4)
                 Failure               : not applied; the order stays pending and may fire again
                                         when its trigger next holds, once per phase
     ```
  3. The step table, copied into `references/troops.yaml: orders.obey.step` if 27A-2 did not author it (SITE: read the block first; a row present is not re-written; record which):
     | kind of order | step (`orders.obey.step`, seed) |
     |---|---|
     | keep doing what the body is doing (`hold`, `stance` unchanged) | 0: no draw |
     | a change of posture, target or route; a weapon switch | 1 |
     | stop or restrain: `hold` on `enemy_broken`; `recall`; a signalled halt | 2 (`RECALL_OB`, already 2) |
     | act together on a signal across several units | 1, +1 for each unit beyond three |
     | anything, for a body with Discipline 1 or `raw` | +1 |
     "`obey: off` is the control and is today's certainty." Re-derive `battle_orders.json` with `tools/export_battle_orders.py`.
- WHERE: `modules/mass_battle/massbattle.py` (the window's `signal`/`order` application through `obey`); `modules/mass_battle/core/contact.py` (only if a call site for an action is needed beside `check_orders`); `references/troops.yaml` (`orders.obey.step`); `engine/engine_params/battle_orders.json` (re-derived); `tests/valoria/test_conditional_orders.py`.
- TESTS: in `tests/valoria/test_conditional_orders.py`, written first: `test_obey_on_spreads_the_applied_tick` (MNV gate 1: "`obey: on`, an army with a single order `(tick:3, {stance: hold})`, n 200: the order is applied at tick 3 in some fields, at tick 4 in some, and later or never in some; `orders_fired` records which"; `assert checked >= 200`; the arm turned on inside the test); `test_three_issuers_equal_outcomes` (gate 2: "Same seeds, the order issued as a standing order, by a decider at the same tick, and from a replayed interventions list: equal outcomes and equal draw counts").
- FALSIFIER and CONTROL: "An order that takes effect at its trigger in every one of 200 fields with the draw on; a draw count that depends on who issued an order" (MNV). Control: "`obey: off`: digests equal to the manager proposal's tree" (B20.07's reading).
- GATE: `python -m pytest tests/valoria/test_conditional_orders.py -q` → pass; `python tools/export_battle_orders.py --check` → exit 0; `python tools/ci_golden_modes_check.py` → equal.
- HASH MOVERS: "none with `obey: off`; the flip moves every army field with orders" (the flip is not made here: DIALS AT CONTROL).
- DEPENDS ON: V12 B20.03, B20.04; V12 Batch B19 (27A-2 `ORDER_OBEY`, 27A-4 `obey`, `_obey_terms`, `_roller_for`; 27A-3 `officer_record`).
- GLOSSARY: row *obey* (or *obedience draw*): "the obedience draw: whether an order is carried out at once, late or not at all, as a soldier obeys or fails to"; owner `core/contact.py::obey`.
- NAMES: `sub._order_due` on the engine's `Unit` (B16M).
- COST and TIER: small build; `sonnet`, `high`; one `opus` read of the gate-1 spread.
- LANDS IT: B20's producer; `Item: B20.08`, `[skip ci]`.

### B20.09 — two triggers, three behaviours, three lull actions · MNV §2 · BUILD · HASH EQUAL
- SOURCE: MNV §2 (copied), its "Exact edits" rows for `hierarchy/units.py`, `troops.yaml`/`export_battle_orders.py`, `massbattle.py`; "Gate" 5; `26_MASS_BATTLE_cell_scale_and_time.md` §3 (B19: bouts and the lull inside `resolve_field`, Option A); closes B-9.
- ADVANCES: R-04.c5 (iii).
- INSTRUCTION (copied): "Triggers added to `_ORDER_TRIGGER_KINDS`: `enemy_broken` (the body this unit is fighting has routed) and `in_lull` (the bout has ended drawn and a lull is open). With `flanked` and `volleys_spent` … the set is ten." "Behaviours added to the standing-order set: `pursue: true | false`, `reform: {shape, ranks, files}` (`26_MASS_BATTLE_movement_and_fatigue_as_data.md` §4), `feign: true` (the existing `feign_retreat` pseudo-field, under its plain name)." "Lull actions added to `GeneralAction.kind` (legal only in a lull): `relieve` (two units of one post exchange lines), `reform`, `commit` (a `reserve` post takes a place in the line). Each is drawn as an order of the second row above. In a lull a reform costs no ticks; relief moves the fresher unit's columns to the front and that is all it does." Exact edits: "`_ORDER_TRIGGER_KINDS` gains two; `_ORDER_SAFE_FIELDS` gains `pursue`, `reform`; `feign` as the accepted spelling of the pseudo-field"; "`massbattle.py`: the three lull actions, applied between bouts"; the exported `triggers` and `behaviours` (B20.01) gain the new members (re-derive). STOPS IF: `reform`'s `{shape, ranks, files}` reader is `26_MASS_BATTLE_movement_and_fatigue_as_data` §4 (B31): if absent at the item's open, `reform` is accepted by the validator and applied as "no change of shape" until B31 `[ASSUMPTION: the reading that changes less — basis: MNV "a row that needs one [mechanism] names it"]`, and the commit body says so.
- WHERE: `modules/mass_battle/hierarchy/units.py` (`_ORDER_TRIGGER_KINDS`, `_ORDER_SAFE_FIELDS`, the `feign` spelling); `modules/mass_battle/core/contact.py` (the two triggers' tests); `modules/mass_battle/massbattle.py` (`GeneralAction.kind`'s lull values; the lull application); `tools/export_battle_orders.py`; `engine/engine_params/battle_orders.json`; NEW `tests/valoria/test_mass_battle_maneuvers.py`.
- TESTS: in the new file, written first, red: `test_relieve_brings_the_fresher_unit_forward` (MNV gate 5: "the unit that comes forward reads higher column stamina than the one it replaced, and the next bout's loss on that post differs from the unrelieved control beyond the control's spread"); `test_enemy_broken_and_in_lull_fire` `[ASSUMPTION: test name; the item creates it]`.
- FALSIFIER and CONTROL: a lull action legal outside a lull. Control: no side with orders: digests equal to B20.08's.
- GATE: `python -m pytest tests/valoria/test_mass_battle_maneuvers.py tests/valoria/test_conditional_orders.py -q` → pass; `python tools/export_battle_orders.py --check` → exit 0.
- HASH MOVERS: none (no side in natural play holds these orders).
- DEPENDS ON: V12 B20.08, B20.03; V12 Batch B19 (`26_MASS_BATTLE_cell_scale_and_time` §3: bouts and lull; the column ledger, `16_PESSIMIST_MB_one_stamina_ledger`); EXISTS-IN-TREE `hierarchy/units.py` `feign_retreat` pseudo-field.
- GLOSSARY: row *lull* (add if absent): "a lull: the pause between two bouts of one battle, as a lull in the fighting is".
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B20's producer; `Item: B20.09`, `[skip ci]`.

### B20.10 — the manoeuvres as doctrine rows; the bait's own draw · MNV §3 and its exact-edit rows · BUILD · HASH EQUAL
- SOURCE: MNV §3 (the table, copied by reference below), §4, "Exact edits" rows `references/troops.yaml: doctrines` and `modules/mass_battle/orchestration.py`, "Gate" 3, 4, 6; MGR §2's last bullet; `04` D-27a (no proper noun in a row); U-8.
- ADVANCES: R-06 inside a battle (two unplayed commanders differ in what their armies do); R-04.c5 (iii).
- INSTRUCTION:
  1. `references/troops.yaml`: a `doctrines:` block (U-8: created here if absent; B22's SCN §E adds each row's shares). Each row: "a list of `(class of unit, post, standing_orders)`; `balanced` stays today's and has none." The rows are MNV §3's twelve manoeuvres, each keyed by its plain manoeuvre name (`stand_and_receive`, `shoot_then_close`, `hold_the_horse`, `refuse_to_chase`, `feigned_flight`, `envelopment`, `refused_flank`, `line_relief`, `reserve_against_a_turn`, `fighting_withdrawal`, `pursue_to_destruction`; `storm` has "no order row" and is not a row) `[ASSUMPTION: the keys — basis: MNV §4 "Doctrine row keys name manoeuvres (`envelopment`, `refused_flank`)"; the rest are the table's names in snake case]`, with the units and orders of MNV §3's second column, copied cell by cell (posts written `centre` where MNV says centre; U-9). "No manoeuvre name is read by the resolver. A doctrine row is data that writes orders." The proper nouns of the sources stay out of `troops.yaml`. Exported by `tools/export_troops.py` to `engine/engine_params/troops.json` (re-derive; `--check` blocking) and loaded by the troop file's loader (B17.10), which refuses an order row that `armyrecord.order` would refuse (B20.01).
  2. MGR §2's bullet, copied: "An unplayed commander's standing orders are written by his doctrine row … a doctrine names, per class of unit, the orders it gives." The writer is the planner that already holds the doctrine's shares (`modules/mass_battle/troop_types/presets.py::plan`, which reads `q.doctrine` after B22's SCN §E; until B22 every army is planned on the shipped `balanced`, which writes no order): `plan` copies the matching row's `standing_orders` onto each unit row it plans.
  3. `modules/mass_battle/orchestration.py`: "the bait's own draw before `feigned_retreat_recognized` is asked": "(i) the bait's own Discipline against obstacle 1 or its flight is real (new, one call of `stand_draw` with no shock terms)".
- WHERE: `references/troops.yaml` (`doctrines`); `tools/export_troops.py`; `engine/engine_params/troops.json` (re-derived); `modules/mass_battle/troop_types/table.py` (the loader's refusal) `[ASSUMPTION: the loader's file — basis: B19a's C set names `troop_types/table.py` as the troop file's module reader]`; `modules/mass_battle/orchestration.py` (`feigned_retreat_recognized`'s caller); `tests/valoria/test_mass_battle_maneuvers.py`.
- TESTS: `test_feigned_flight_three_outcomes` (MNV gate 3: "Feigned flight against an enemy with `pursue: true`, n 200: the pursuer is overextended in some fields, recognises the feint in some, and the bait's flight turns real in some. All three counts above zero"); `test_envelopment_wings_sometimes_never_close` (gate 4: "The envelopment doctrine against the `balanced` doctrine, equal armies, n 200, against the same-run mirror: its win share and the share of fields in which the wings never closed are both reported; the second is above zero. No target"). Each `assert checked >= 200`.
- FALSIFIER and CONTROL: "a doctrine whose manoeuvre succeeds in every field; the resolver reading a doctrine's name" (MNV). Control: `balanced` (no orders): digests equal to B20.09's.
- GATE: `python -m pytest tests/valoria/test_mass_battle_maneuvers.py -q` → pass; `python tools/export_troops.py --check` → exit 0; `git grep -n "envelop\|cannae\|refused" modules/mass_battle/massbattle.py modules/mass_battle/battle_loop.py` → no branch on a manoeuvre's name (gate 6); the two gate-4 shares quoted in the commit body, read by `opus`.
- HASH MOVERS: none ("none with `obey: off`"; no season army holds a doctrine with orders until B22).
- DEPENDS ON: V12 B20.09, B20.01; V12 Batch B17 (B17.10: the troop file, its exporter and loader); EXISTS-IN-TREE `orchestration.py::feigned_retreat_recognized`, `::feigned_retreat_check`, `stand_draw` (B19's `26_MASS_BATTLE_rout_pursuit_and_giving_ground` §1).
- GLOSSARY: row *doctrine* (add if absent): "doctrine: a named way of fighting that sets which orders each kind of unit is given, as an army's doctrine does"; owner `troops.yaml: doctrines`.
- COST and TIER: small build plus data; `sonnet`; the doctrine readings `haiku` run, read by `opus` (MNV "Lands").
- LANDS IT: B20's producer; `Item: B20.10`, `[skip ci]`.

### B20.11 — the battle scenario and its instrument · SCN §A with `IS-MB-01` step 2 · BUILD · HASH EQUAL
- SOURCE: SCN §A (copied; its end condition as W3-1 rewrote it to A-57, A-58, A-66), "Gate" 1, "Tests (W3-1)"; IS-B1 P2-1.2 `IS-MB-01` step 2 ("Registry first", U-7); IS-B1 P2-1.0's stub contract; U3 §1.3 (`harness/field_scene.py` created in B20); closes F-MB-03, R-07.
- ADVANCES: R-04.c4 (`test_field_scene.py`); MB plays alone (IS-B1 P2-1.1 row 6).
- INSTRUCTION:
  1. NEW `engine/season/harness/field_scene.py` (SCN §A, copied): "`build(seed) -> World`: two factions; each with a seat whose remit grants `march` and `marshal`, an army Record minted and filled through the real verbs from cohorts with real training Sites (so the doctrine has a barracks, a range and a stable to use), a settlement each, one garrisoned; stores at both treasuries. Built with `Fixtures` overrides that un-withhold the army verbs, `marshal` and `surrender` and roster `march_postures: [storm, besiege]` **for this world only**." The armies are minted at build by `harness/army_presets.py::install` (IS-B1 P2-1.1, "The cut, stated").
  2. `play`, by `IS-MB-01` step 2 (copied): "`field_scene` registers `field` in `scenarios.SCENARIOS` (`IS-B2-CORE-01`, B11; B20 follows B11) with `build=field_scene.build`, `verbs=None`, `seat` the played faction's commander, `ending=field_ending`, `role="mass_battle.resolve_field"`, and `kinds` and `unreached` as `IS-B3-GO-01` defines them; `play` calls `scenarios.run("field", seed, seasons, host=...)`". A policy (B20.12) is the host's callback; SCN §A's "runs `SeasonDriver.season` with `play_surface.dispatching_chooser`" is what `scenarios.run` does, and no season loop is written in this file. "A policy sees `military_menu.menu`, `field_estimate` and, once a field is drawn, the last `FieldOutcome`." The registry row is appended at the end of `SCENARIOS`.
  3. "`Report`: per field, the estimate shown, the choices taken, the outcome record, each named person's `body` and posture before and after, where everyone stands." "End condition of the scenario: one faction's seat holds both settlements (by the aggressor's own `seize` after a `Won` on a march into held land, A-57, A-58, A-66; C3-L12), or a `surrender`, or the season cap." (`field_ending` returns the name; the `seize` ending is reachable only after B23, IS-B1 P2-1.1 row 8.)
- WHERE: NEW `engine/season/harness/field_scene.py` (`build`, `play`, `Report`, `field_ending`); `engine/season/harness/scenarios.py` (one `field` row); `engine/season/tests/test_field_scene.py`.
- TESTS: `engine/season/tests/test_field_scene.py::test_two_policies_end_in_different_bands` (SCN gate 1: "`field_scene.play` at one seed under two policies (storm at once; besiege then storm) ends in different bands with different persons hurt; the same policy at two seeds differs"), written first, red (no module); the two policies are written in the test until B20.12 lands `POLICIES`.
- FALSIFIER and CONTROL: "a policy that cannot change a scenario's ending" (SCN). Control: the shipped realm untouched: `build_realm(s)` hashes at s = 0, 1, 2, one season, equal to B20.07's (the overrides are this world's only).
- GATE: `python -m pytest engine/season/tests/test_field_scene.py engine/season/tests/test_scenarios_runner.py -q` → pass (the runner's `test_every_ending_name_a_reader_can_return_has_a_kind` covers the new row); realm hashes → equal.
- HASH MOVERS: none (a harness file and its test).
- DEPENDS ON: V12 B20.06 (the `Report` reads `FieldOutcome.report`); V12 B11.05 (`scenarios.py`, `SCENARIOS`, `run`, `ENDING_KINDS`); EXISTS-IN-TREE `harness/army_presets.py::install`, `harness/military_menu.py`, `seam/wrappers/mass_battle.py::field_estimate`, `harness/play_surface.py::dispatching_chooser`.
- GLOSSARY: row *scenario* is B11's; none added.
- NAMES: `build_realm` in `boot/realm.py` (B03c); the posture roster's key `march_postures` (unchanged by B16L, which renames the army row's `stance`).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B20's producer; `Item: B20.11`, `[skip ci]`.

### B20.12 — the scenario's command line, its policies, its ending kinds · `IS-MB-01` steps 1, 3 · BUILD · HASH EQUAL
- SOURCE: IS-B1 P2-1.2 `IS-MB-01` (steps 1, 3 copied; step 2 in B20.11, U-7; step 4 in B34), its GATE, FALSIFIER; MGR "Falsifier" ("a standing order that cannot change an outcome at any of 200 seeds").
- ADVANCES: R-04.c4; MB standalone (entry, end condition, instrument); "a choice that matters".
- INSTRUCTION (copied):
  1. "`POLICIES`, a closed mapping of name to player-proxy callback over `military_menu.menu`, `field_estimate` and `FieldWindowView`: `storm` (march at once; `none` at every window); `fall_back_early` (as `storm`, with every unit's standing order `(own_strength:F, {stance: retreat})` set at the highest `F` the closed set offers); `signal_then_hold` (the manager proposal's gate-2 script: fire a signal at window 1, order one unit to `hold` at window 2); `auto` (no callback: both commanders decided by the chooser and IS-MB-03). `besiege_then_storm` joins when IS-MB-02 lands" (B22).
  2. "`ending_kind(report) -> 'won' | 'lost' | 'drawn' | None` … for the played faction is the `kinds` row applied to `field_ending`'s name …; at the season cap the report's last block prints where each army stands, each unit row's losses (by kind once `27_MB_E` lands) and who holds each settlement, so a draw is a state a player can act on and never a blank."
  3. "`main()`: `--seed`, `--policy`, `--seasons`; prints the `Report` and the `content_hash`."
  4. "**If the fall-back test is red at B20's close**, the fall-back point is removed from the scenario's offered choices in that commit and the close says so with the reading: a choice the player is offered must be able to matter, and P-3 is the before-reading."
- WHERE: `engine/season/harness/field_scene.py` (`POLICIES`, `ending_kind`, `main`); `engine/season/tests/test_field_scene.py`.
- TESTS (added to `test_field_scene.py`, written first, red): `test_every_ending_kind_is_reached_and_each_writes` ("seeds 0–59 under `auto`; `assert` on the count of battles read"); `test_a_fall_back_point_changes_some_battle` ("`storm` against `fall_back_early`, seeds 0–199, `assert checked >= 200`: the `FieldOutcome` differs at some seed"); `test_a_window_action_changes_some_battle` ("`storm` against `signal_then_hold`, the same form"); `test_same_seed_twice_is_one_hash`. Expected: `won`, `lost` and `drawn` each reached under `auto` by B20's close only if an unplayed commander acts (B20.19 ships no cell): the first test reads the kinds reached and asserts `drawn` and at least one of `won`/`lost` `[ASSUMPTION: the reachable set before B23's `seize` and with no window cell — basis: IS-B1 P2-1.1 row 6, "three ending kinds (the `seize` ending waits on B23)"]`.
- FALSIFIER and CONTROL: "each policy pair that differs in one choice ends identically at every seed read (then that choice is cosmetic). Control: `storm` twice at one seed is one hash; `storm` at two seeds differs."
- GATE: `python -m pytest engine/season/tests/test_field_scene.py -q` → pass; `python -m engine.season.harness.field_scene --seed 0 --policy storm` → exit 0, a `Report` whose last line names an ending kind.
- HASH MOVERS: none ("a harness file and its test; the scenario's `Fixtures` overrides are for its world only").
- DEPENDS ON: V12 B20.11, B20.03, B20.04; V12 B20.19 for `auto`'s window decider (lands after: `auto` with no decider is the delegated battle until then, which is a complete behaviour, CHO INCOMPLETE item 1); EXISTS-IN-TREE `harness/military_menu.py`, `seam/wrappers/mass_battle.py::field_estimate`.
- GLOSSARY: none (*ending kind* is B11's row).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B20's producer; `Item: B20.12`, `[skip ci]`.

### B20.13 — a commander may weigh a field by what he believes · RES §5 with SCN §F · BUILD · HASH MOVER(behaviour)
- SOURCE: RES §5 (copied), its Gate, Falsifier, Movers; SCN §F (copied); MGR §8 (the cache and the sample count, U-4); `10_DICE_believed_odds_have_a_prior.md` Edits A–B (B05); AQ-X1; rulings A-1, A-30; closes the first audit's step 5b, F-DICE-14 Edit C. Carried here from B17 (U-5).
- ADVANCES: R-06 and R-08 inside a battle (an NPC commander is no longer blind to odds and not omniscient).
- INSTRUCTION:
  1. SCN §F, copied: "`field_estimate(w, actor, via, target, order=None, believed=None)`: when `believed` is given (a mapping the host builds from the actor's claims about the defenders' strength and walls), the input is built from it instead of from the world. A person who knows nothing gets no estimate."
  2. RES §5, copied: "`believed_chance`, for a row whose prize binds the `mass_battle` provider: `field_estimate(…, believed=…)`, the input built **from the believer's own claims** about the defenders' strength and walls; a person who holds no such claim gets `None` ("cannot say"), which `10_DICE_believed_odds_have_a_prior.md` Edits A–B … already price as a prior, not as certainty." "The estimate is samples of the one resolver on a private stream keyed `H(seed, tick, believer, "estimate.field")` (A-30); its count for this caller is the fixture `believed_field_samples` (seed 40), and a cache keyed on the frozen input is lawful. No closed form (A-1)." "AQ-X1's sentence at the wrapper is restated: no NPC reads the **world's** odds; any person may reckon on what he believes."
  3. `believed_field_samples = 40` in `engine/season/data/fixtures.py`, at the end of its family, with its `[JUSTIFIED: …]` tag naming this item.
- WHERE: `engine/season/seam/wrappers/mass_battle.py` (`field_estimate`'s `believed`; the AQ-X1 docstring sentence); `engine/season/seam/wrappers/sigma.py` (`believed_chance`'s `mass_battle` branch); `engine/season/data/fixtures.py` (`believed_field_samples`); `engine/season/tests/test_march.py`.
- TESTS: `test_march.py::test_a_commander_told_a_false_strength_marches_where_a_truthful_one_does_not` `[ASSUMPTION: test name; the item creates it]` (RES gate: "A commander told a false strength marches where one told the truth does not (the first audit's 5b gate), over seeds 0 to 29"); `test_an_unchosen_estimate_leaves_the_hash` `[ASSUMPTION: test name]` ("`content_hash` is unchanged by an estimate whose act is not chosen"); `test_no_claim_no_estimate` (a believer with no claim reads `None`). Written first, red.
- FALSIFIER and CONTROL: "An NPC's estimate built from a strength no claim of his names" (RES). Control: `odds_weighting: none` (H-248's control arm) reproduces B20.07's realm hashes; MGR §8's falsifier: `git grep -n "def .*odds.*field\|closed.form" engine/season/seam/wrappers/mass_battle.py` shows no closed-form field estimate (read, quoted in the commit body).
- GATE: `python -m pytest engine/season/tests/test_march.py -q` → pass; `python tools/ci_sim_fabrication_check.py` → exit 0; realm hashes at seeds 0–2, one season → moved where a `march` Candidate is scored (recorded for B20.99), act tallies quoted.
- HASH MOVERS: "Worlds in which a `march` Candidate is scored under `odds_weighting: believed`" (shipped `believed`, `fixtures.py` H-248). Declared; B20.99.
- DEPENDS ON: V12 B20.11 (none strictly; placed after the scenario so its `Report` shows the believed estimate); V12 Batch B05 (`10_DICE_believed_odds_have_a_prior` Edits A–B); EXISTS-IN-TREE `seam/wrappers/sigma.py::believed_chance`, `seam/wrappers/mass_battle.py::field_estimate`, `Fixtures.odds_weighting`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet` (RES "§5 `sonnet`").
- LANDS IT: B20's producer; `Item: B20.13`, `[skip ci]`.

### B20.14 — after a won field: the routed re-homed, a grudge eased · SCN §G · BUILD · HASH MOVER(behaviour)
- SOURCE: SCN §G (copied; W3-1: the title passes only by the aggressor's own `seize`, which is B23's), "Gate" 6, "Tests (W3-1)" (gate 6); U-3; closes R-22 (`audits/04_MB_audit.md` §8 step 6); makes B17.02's H-355 text true.
- ADVANCES: R-07.c; A-80 (a won field moves the world for the beaten).
- INSTRUCTION (copied): "`_eff_march` on `Won`: each routed defender who is not removed is re-homed to the nearest rung his faction holds (`world_q.governing_hold` up his own chain, else the faction's seat rung), by `_relocate` under the gate's `muster` basis; if there is none he stays. On `Won`, each winner who holds a negative row toward his own faction (`person_q.held_against`) loses one. Both are behind the existing `field_casualty_model` roster's precedent: a fixture `field_aftermath` (`off` control, `withdraw` shipped)." The fixture is added at the end of the `field_*` family with its `[JUSTIFIED: …]` tag naming this item.
- WHERE: `engine/season/loop/effects_combat.py` (`_eff_march`, the `Won` branch); `engine/season/data/fixtures.py` (`field_aftermath`); `engine/season/tests/test_march.py`.
- TESTS: `engine/season/tests/test_march.py::test_won_rehomes_a_routed_defender` (SCN gate 6: "After a folded `field.won` with a routed defender who holds another rung, `mustered(target, loser)` is empty; a faction that loses, loses, then wins starts its next field at morale 4"), written first, red.
- FALSIFIER and CONTROL: a routed defender left on the lost field when his faction holds another rung. Control: `field_aftermath: off` reproduces B20.13's realm hashes.
- GATE: `python -m pytest engine/season/tests/test_march.py -q` → pass; `python tools/ci_sim_fabrication_check.py` → exit 0; the seed-2 one-season realm hash → moved or equal, recorded (moved only where the realm's field is `Won` with a routed defender).
- HASH MOVERS: every seeded realm whose fought field folds `Won` with a routed defender or a winner holding a row against his faction. Declared; B20.99.
- DEPENDS ON: V12 B20.06 (the same function, after); EXISTS-IN-TREE `world_q.governing_hold`, `person_q.held_against`, `loop/effects_migration.py::_relocate`, the gate's `muster` basis (`state/gate.py`), `Fixtures.field_casualty_model`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B20's producer; `Item: B20.14`, `[skip ci]`.

### B20.15 — the odds of one order, from the dice owner · CHO 27D-1 · BUILD · HASH EQUAL
- SOURCE: CHO "Instructions to code it", item 27D-1 (copied), §2 (`obey_odds`), "Gate" 1, "Tests" (named); rulings A-59; closes the addendum's "every order is free" half (CHO "The problem").
- ADVANCES: R-08 inside a battle (the odds shown are the odds drawn).
- INSTRUCTION (copied): "`modules/mass_battle/core/contact.py` :: new `obey_odds(view, action, me)` — calls `_obey_terms` (27A-4's helper, the one composition of pool, levels and obstacle) for each link and `engine.dice_engine.sigma_leverage.band_odds(pool, ob, boost)` on the result; composes two links by multiplying the at-once shares and summing the rest; draws nothing." Its return: `obey_odds(view, action, me: CommandRecord) -> (p_at_once, p_late, p_not)`. "It is the closed form of the same sampler for **one draw** …, not a second rule, and it draws nothing. It is not the field closed form that `04_MB_manager_battle_one_resolver.md` §8 refuses."
- WHERE: `modules/mass_battle/core/contact.py` (`obey_odds`); `tests/valoria/test_conditional_orders.py`.
- TESTS: `test_obey_odds_agrees_with_two_thousand_draws_of_obey` (CHO gate 1: "for 20 hand-built situations, the three shares it returns lie within the sampling band of 2,000 draws of `obey` on the same inputs"; `assert checked >= 20`), `test_obey_odds_and_obey_share_one_terms_helper` ("`git grep -c "def _obey_terms" modules/mass_battle` is 1"). Written first, red.
- FALSIFIER and CONTROL: "An odds function that needs a second obstacle rule" (CHO); planted: "`obey_odds` given its own obstacle arithmetic (the helper-count test and gate 1 fail)". Control: digests equal to B20.14's (nothing calls it in a field).
- GATE: `python -m pytest tests/valoria/test_conditional_orders.py -q` → pass; `git grep -c "def _obey_terms" modules/mass_battle` → 1.
- HASH MOVERS: none.
- DEPENDS ON: V12 B20.08; V12 Batch B19 (27A-4 `_obey_terms`, `obey`); EXISTS-IN-TREE `engine/dice_engine/sigma_leverage.py::band_odds`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`.
- LANDS IT: B20's producer; `Item: B20.15`, `[skip ci]`.

### B20.16 — what a commander is shown at a window · CHO 27D-2 · BUILD · HASH EQUAL
- SOURCE: CHO 27D-2 (copied), §2 (the view block, copied), §4 (`reasons`), "Gate" 5, 6, "Added test (W3-1)"; `04` D-42 (7b-16: the officer's pool is shown as believed); closes CHO INCOMPLETE item 2 (closed by W3-1, built here).
- ADVANCES: R-08 inside a battle; R-06 (a commander's view is his, not the world's).
- INSTRUCTION (copied): "`modules/mass_battle/massbattle.py` :: `FieldWindowView.units`, `GeneralAction` (both created by `04_MB_manager_battle_one_resolver.md` §4) — the three view fields, computed where the view is built: `reach_steps` by the same function `obey` uses, `steady` from the unit's Discipline and `raw`, `officer_pool` copied from the believed value the host handed in (7b-16; never from `Subunit.officer_record`'s true score); `GeneralAction.reasons: tuple = ()`, copied untouched into `FieldOutcome.interventions`. Host side: `seam/wrappers/mass_battle.py::field_input` builds the believed pools from the commander's claims."
  ```python
  units: tuple   # ((name, share, routed, in_contact, in_hand, orders_pending,
                 #   reach_steps, steady, officer_pool), ...)
                 # reach_steps: whole distance steps from his post to the unit (27_MB_A §4; "band" is kept for a degree)
                 # steady: 'disciplined' | 'ordinary' | 'unsteady'
                 # officer_pool: the dice of the unit's officer AS THE COMMANDER BELIEVES THEM, or None ("unknown")
  ```
  "The host builds each from the commander's own claims about that officer (`person_q` over his ledger, the same believed route as `U5b_MB_residue.md` §5 [B20.13]) and hands it in on the input beside the officer's `CommandRecord`; `None` when he holds no claim, shown as "unknown". The module copies the handed value into the view and never reads the officer's true record for it." "He is shown nothing of the enemy but what is in contact with his own units."
- WHERE: `modules/mass_battle/massbattle.py` (`FieldWindowView.units`, `GeneralAction.reasons`); `engine/season/queries/inputs.py` (`MassBattleInput`'s believed officer pools, beside the `CommandRecord`s); `engine/season/seam/wrappers/mass_battle.py` (`field_input`); `tests/valoria/test_army_battle.py`.
- TESTS: in `tests/valoria/test_army_battle.py`, written first, red: `test_the_window_view_shows_no_enemy_unit_out_of_contact` (gate 5: "asserted on the view's fields over 200 fields"); `test_no_decider_and_no_orders_is_todays_field` (gate 6, the control, 200 seeds); `test_officer_pool_is_believed_or_unknown` ("a commander holding no claim about an officer sees `None`; one holding a false claim sees the false value").
- FALSIFIER and CONTROL: planted "the view built from `World` (gate 5 fails on an enemy unit out of contact)". Control: gate 6: "With no decider and no standing orders, the field equals the field without this proposal, at 200 seeds."
- GATE: `python -m pytest tests/valoria/test_army_battle.py -q` → pass; digests equal to B20.15's.
- HASH MOVERS: "None with no decider."
- DEPENDS ON: V12 B20.03, B20.15, B20.13 (the believed route); V12 Batch B19 (27A-3 `officer_record`, the reach function of 27A-4).
- GLOSSARY: none (*distance step* is the glossary's *band* row: "band" kept for a degree).
- NAMES: `Subunit.officer_record` → `Unit.officer_record` (B16M).
- COST and TIER: small build; `sonnet`.
- LANDS IT: B20's producer; `Item: B20.16`, `[skip ci]`.

### B20.17 — who commands each unit and where the commander rides · CHO 27D-3 · BUILD · HASH EQUAL
- SOURCE: CHO 27D-3 (copied), §1 (the two bold rows), "Data rows" (copied, U-9), "Gate" 3, 4, "Tests" (named); `04_MB_cell_hierarchy_as_data.md` §3 (posts, B19).
- ADVANCES: R-06 inside a battle (where he rides and whom he trusts are choices with odds).
- INSTRUCTION (copied): "`modules/mass_battle/armyrecord.py` :: `order`, `options`; `references/troops.yaml: doctrines.<name>.commander_post`; `engine/season/harness/military_menu.py` — `order` accepts `commander_post` and `officer` (27A-3 adds the keys; this adds the menu's closed sets: unit names; persons of the faction, handed in as facts); `options()` gains `unofficered` and `post_names_no_unit`; the menu lists both and prints `obey_odds` beside each window action." Data rows: "`doctrines.<name>.commander_post`: a post name of the formation (`centre`, `rear`, `left`, `right`, `reserve`), resolved to the unit holding that post; seed `reserve` for every doctrine, which is the control (the rear centre, today's implied position)." (`centre` for the source's `front`: the MB lexicon's post row, U-9.)
- WHERE: `modules/mass_battle/armyrecord.py` (`order`, `options`); `references/troops.yaml` (`doctrines.<name>.commander_post`, every row B20.10 wrote); `tools/export_troops.py` (the column; re-derive `troops.json`); `engine/season/harness/military_menu.py`; `tests/valoria/test_mass_battle_officers.py`; `tests/valoria/test_army_menu_presets.py`.
- TESTS (written first, red): `tests/valoria/test_mass_battle_officers.py::test_a_forward_post_buys_obedience_and_costs_exposure` (gate 3: "The same commander posted forward against in reserve, n 400: forward, improvised orders are obeyed at once more often; forward, the share of fields in which his unit was struck is higher. Both differences beyond two standard errors"), `::test_three_signals_can_be_misread_and_one_cannot` (gate 4: "misreadings occur in the first and never in the second; the first's share of fields in which every wing closed is lower"); `tests/valoria/test_army_menu_presets.py::test_the_menu_offers_officer_and_post_from_their_closed_sets`. The forward/reserve and signal tests turn the `obey` arm on inside the test.
- FALSIFIER and CONTROL: "A forward post that costs nothing in 400 fields" (CHO). Control: every doctrine at `reserve`: digests equal to B20.16's.
- GATE: `python -m pytest tests/valoria/test_mass_battle_officers.py tests/valoria/test_army_menu_presets.py -q` → pass; `python tools/export_troops.py --check` → exit 0.
- HASH MOVERS: "none (withheld verbs)".
- DEPENDS ON: V12 B20.16, B20.10 (the doctrine rows), B20.15 (`obey_odds`); V12 Batch B19 (27A-3: `commander_post`, `officer` keys; `04_MB_cell_hierarchy_as_data` §3 posts).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`.
- LANDS IT: B20's producer; `Item: B20.17`, `[skip ci]`.

### B20.18 — the unplayed commander's decider · CHO 27D-4 · POINTER
- What it points at: CHO 27D-4 ("forward `host.decide` for either side's commander by the one parameter; the chooser's decider over `GeneralAction`'s closed set"), INCOMPLETE (DESIGN) in `unified/U4_DOCUMENT_STATUS.md` §3.4 ("27D-4, the unplayed commander's decider, is interface only"), is completed by `IS-MB-03` (IS-B1: "completes `27_MB_D` item 27D-4"), built as B20.19: the seam forward (step 4) and the decider (`make_decider`, B10.57). The cells on payload values stay CHAR's content (G-3; DIALS AT CONTROL: `window_responses` empty).
- Target files and symbols: `engine/season/seam/wrappers/mass_battle.py::resolve`; `engine/season/decision/decider.py::make_decider` (read).
- GATE: B20.19's.

### B20.19 — an unplayed commander acts at a window · `IS-MB-03` · BUILD · HASH EQUAL
- SOURCE: IS-B1 P2-1.2 `IS-MB-03` (steps 1–5 copied, as the Sonnet check amended it), GATE, FALSIFIER; CHO §4, 27D-4; PB §5 (the precedent, ladder step 4); U-10; closes CHO INCOMPLETE item 1 and IS-B1 P2-3.5's row "`27_MB_D` (27D-4) closed by IS-MB-03".
- ADVANCES: R-06 and R-08 inside a battle; the NPC half of the standing requirement (battles nobody watches).
- INSTRUCTION (copied):
  1. "**No second decider is written.** … The field's commander is `make_decider` with `key="general_action"`: the view's `legal` tuple is `none` plus the kinds a matching `window_responses` row names; the choice score is `IS-B2-CHAR-02`'s (`align_choice('general_action', kind, axis)` on the person's axis weights); `bias` is this item's one addition, a callable `(view, value) -> float` returning the summed `weight` of the rows matching that value (0.0 where none), added to the choice score. One legal value (the shipped state: no row) returns `none` and draws nothing. The draw is keyed `general_action:<kind>` on a stream of its own, never the battle's. `GeneralAction.reasons` carries `watch`'s two terms for the winner." (`bias` and `test_a_single_legal_value_draws_nothing` already landed with B10.57, U-10.)
  2. "`engine/season/data/verbs.py::CHOICE_RANGES`: `general_action` as a pointer to the module's closed kinds (`signal`, `order`, `rally`, `withdraw`, `none`). It is **not** listed under any verb in `rosters.yaml: choice_sourced`, so nothing fans at DELIBERATE: the action is chosen in the battle, at the window." (The lull kinds of B20.09 join the closed kinds: `relieve`, `reform`, `commit`, legal only in a lull.)
  3. "`engine/season/rosters.yaml: window_responses`, a new optional table, shipped empty: rows `{window, own: <band>, value: {kind, post, arg}, weight}`, where `post` is one of the army formation's post names (`centre`, `left`, `right`, `rear`, `reserve`; the closed set `commander_post` uses …) and names the unit an `order` or `rally` goes to. The loader (`data/rosters.py`) reads the table while empty and refuses, naming the row, a `kind` outside the closed kinds, a `post` outside the posts and an `arg` outside the standing-order behaviours. A row is content about how commanders respond to what they can see; it names no person, faction or outcome." Added at the end of the choice family's block (IS-B1 P2-3.2).
  4. "`engine/season/seam/wrappers/mass_battle.py::resolve`: one decider per commander: the host's when the host plays him, by the inline party test the combat adapter uses today (`seam/wrappers/combat.py`; B34's `played_by` replaces both tests later …), otherwise a closure over his frozen `PersonInterior` calling `make_decider(..., key="general_action", bias=...)` (step 1); passed as `decide=`."
  5. "Ships with no cell and no row. The cells (`choices: general_action:` in `tables.alignment`) are `02_CHAR_choice_alignment`'s block and Jordan's or the CHAR content pass's values (G-3)."
  6. The decider is passed only for a role `npc_decider_roles` names (B10.57 step 5: "a wrapper passes this decider as `decide=` only for a role named there and a party the host does not play"); `mass_battle.resolve_field` is not added to that tuple here (its control and shipped value `()`), so the shipped realm's battles stay delegated `[ASSUMPTION: the role is not added — basis: B10.57's rule and step 5 "Ships with no cell and no row"; adding it is B98's, beside `npc_decider_roles`]`.
- WHERE: `engine/season/data/verbs.py` (`CHOICE_RANGES`); `engine/season/rosters.yaml` (`window_responses`); `engine/season/data/rosters.py` (its loader); `engine/season/seam/wrappers/mass_battle.py` (`resolve`); `tests/valoria/test_army_battle.py`; `engine/season/tests/test_field_scene.py`.
- TESTS (written first, red): `tests/valoria/test_army_battle.py::test_a_chooser_served_commander_with_no_cell_is_the_delegated_battle` (`assert checked >= 200`); `engine/season/tests/test_field_scene.py::test_two_commanders_opposed_on_one_axis_act_differently_at_a_window` ("one cell and one row authored in the test, temperature 0"), `::test_the_window_decider_draws_nothing_from_the_battles_stream`; the loader's three refusals beside the other `rosters.yaml` refusals (`test_window_responses_refuses_an_unknown_kind_post_or_arg` `[ASSUMPTION: test name; the item creates it]`).
- FALSIFIER and CONTROL: "a rule for an unplayed commander found in `modules/mass_battle/` or in the adapter; a decider that changes the count of draws from the battle's stream. Control: with nothing authored, `auto` equals the delegated battle at 200 seeds."
- GATE: the tests above → pass; realm hashes at seeds 0–2, one season → equal to B20.17's.
- HASH MOVERS: "none while no cell and no row is authored."
- DEPENDS ON: V12 B10.57 (`make_decider`, `bias`, `npc_decider_roles`); V12 Batch B16 (PB step 4, `approach_of`); V12 B03 (`U5a_CORE_owed_edits` §E, the frozen `PersonInterior`); V12 B10.56 (`02_CHAR_choice_alignment`, `align_choice`); V12 B20.16, B20.17, B20.12; EXISTS-IN-TREE `data/verbs.py::CHOICE_RANGES`, `seam/wrappers/combat.py` (the party test).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`; the function read at the batch's one `opus` critique; IN review of the `decision/` call.
- LANDS IT: B20's producer; `Item: B20.19`, `[skip ci]`. `[ASSUMPTION: the duel's form transfers to the window unchanged — basis: PB §5 and `27_MB_D` §4, §5; reversible: delete the adapter's closure and the adapter passes no decider, which is today's complete behaviour]` (IS-MB-03's own).

### B20.20 — `ally_at:D` has an ally · REST_2 W1 · BUILD · HASH EQUAL
- SOURCE: REST_2 "W1" (copied: Resolution, the code block, the three bullets, Layer 1, Gate, Falsifier); Lands line ("W1 in B20 … One commit each"); closes `audits/17_CENSUS_REST.md`'s `ally_at:` declared-with-no-reader row.
- ADVANCES: none of the nine; an accepted trigger that fires instead of damming its queue (MGR §2's grammar).
- INSTRUCTION (copied, names after B16L/B16M): "The ally is named, by the unit's name (its `units` row), on the order; the army builder resolves the name to the sibling unit; an order that needs an ally and has none is refused where it is built."
  ```
  # modules/mass_battle/hierarchy/units.py
  @dataclass
  class Order:
      trigger: str
      behavior: dict = field(default_factory=dict)
      ally: Optional[str] = None                 # NEW: a sibling unit's name; required by,
                                                 # and only lawful with, an 'ally_at:D' trigger
      waypoint_ref: Optional[object] = field(default=None, repr=False)   # resolved by build_army, never authored

      def __post_init__(self):
          ...existing checks...
          if self.trigger.startswith('ally_at:') != (self.ally is not None):
              raise ValueError("Order: 'ally_at:D' needs ally=<unit name>, and no other trigger takes one")
  ```
  - "`modules/mass_battle/armies.py::build_army`: a unit spec may carry `'name'` (popped before `Unit.of_type`; `orderofbattle._spec_for` adds `spec['name'] = row.name`, which `OrderOfBattle` already holds unique …). After the loop that builds `units`, one pass: for each unit's orders with `ally`, set `order.waypoint_ref = units[index_of[order.ally]]`; refuse (`ValueError`, naming the unit and the name) an `ally` that is no sibling's name or is the unit's own."
  - "`modules/mass_battle/core/contact.py`: the `if order.waypoint_ref is not None:` guard becomes an unconditional read. A `None` there is now a build defect and raises `AttributeError` at the first check rather than waiting forever."
  - "`04_MB_manager_battle_one_resolver.md` §2's row form: `(trigger, behaviour)` becomes `(trigger, behaviour[, ally])`, and `armyrecord.py::order`'s validation (that proposal's edit) refuses the third element on any other trigger." (B20.01's validator gains the clause here.)
  - Layer 1, at the site: "`holonic_ARCHITECTURE.md` §45 …: the name is data on the module's own input record (`OrderOfBattle`), resolved inside one `resolve_field` call; no state survives it."
- WHERE: `modules/mass_battle/hierarchy/units.py` (`Order`); `modules/mass_battle/armies.py` (`build_army`); `modules/mass_battle/orderofbattle.py` (`_spec_for`); `modules/mass_battle/core/contact.py` (the `ally_at` read in `check_orders`); `modules/mass_battle/armyrecord.py` (`order`); `tests/valoria/test_mass_battle_signals.py`.
- TESTS: "A new case in `tests/valoria/test_mass_battle_signals.py` …: two units `a`, `b` built 10 cells apart, `a` holding `Order('ally_at:3', {'stance': 'aggressive'}, ally='b')`; `check_orders` leaves `a._order_idx == 0` while the centroids are farther than 3, and advances it to 1 on the first check after `b` is moved within 3. Three refusals: `Order('ally_at:3')` (no ally); `Order('tick:2', ally='b')`; `build_army` with `ally='nobody'`." Written first, red.
- FALSIFIER and CONTROL: "Delete the resolution pass in `build_army`: the order never fires and the test's `_order_idx == 1` fails … Control: the same pair with `enemy_range:3` in place of `ally_at:3` does not fire on `b`'s approach."
- GATE: `python -m pytest tests/valoria/test_mass_battle_signals.py tests/valoria/test_conditional_orders.py -q` → pass; `python tools/ci_golden_modes_check.py` → equal (no shipped order uses `ally_at`).
- HASH MOVERS: none (module-internal; "no host builds an `ally_at` order").
- DEPENDS ON: V12 B20.01; EXISTS-IN-TREE `hierarchy/units.py::Order` (`waypoint_ref`), `armies.py::build_army`, `orderofbattle.py::_spec_for`, `core/contact.py::check_orders`.
- GLOSSARY: none.
- NAMES: `subformations` → `units`, `sf.name` → `row.name` (B16L: `UnitRow`); `Subunit.of_type` → `Unit.of_type`, `subs` → `units`, "subunit" → unit (B16M). The copied code is corrected to these names, and the correction is said here.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B20's producer; `Item: B20.20`, `[skip ci]`.

### B20.21 — mass battle's integrated reading at this close · `IS-MB-05` · READING
- In the position table only; its text is Reading R1 below. Lands in B20.99's commit body. Cost: a reading; `haiku` runs it.

## Readings (B20)

R1 (`IS-MB-05`, IS-B1 P2-1.2, copied byte for byte): "at the close of B17, B20, B22 and B23 the last commit body quotes `python -m engine.season.harness.aperture 2 s`, s = 0, 1, 2: the `ENGINES` lines for `mass_battle.resolve_field`, `mass_battle.army`, `mass_battle.army_order`; the counts of `field.won`, `field.lost`, `field.drawn`, `field.unopposed`, `siege.pressed`; `attempted` and `executed` for `march`, `marshal`, `recruit`, `form_unit`, `assign_troops`, `order_unit`. Each reading names its SHA and is taken once." Expected at B20 (IS-MB-05's GATE names B17, B22 and B23 only): unchanged in kind from B19's close for the army verbs (still withheld until B22); `mass_battle.resolve_field` above 0 at seed 2 at least (B17's reading). A fall to 0 at seed 2 is a finding about B20's movers, reported in the close.

### B20.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12; `IS-A-12`.
- ADVANCES: the requirement readings of this batch (REQUIREMENT line).
- INSTRUCTION: (1) re-record the realm pins in `engine/season/tests/_realm_goldens.py` moved by B20.05, B20.06, B20.13, B20.14, once, read against B19's close (`reading @<sha>`), with act and Event tallies quoted beside each moved pin; the commit says "re-pin" and names the four movers; (2) run the batch gate's seeded commands at seeds 0–2 (two seasons at most) and the one full-suite run (CLAUDE.md §0.4); (3) write the `reading:` records of R-04.c4, R-04.c5 (ii), (iii) and R-07.c in `engine/season/requirements.yaml` (no `status:` edit); (4) the commit body carries Reading R1 and the close's record (§5.12).
- WHERE: `engine/season/tests/_realm_goldens.py`; `engine/season/requirements.yaml` (`reading:` records only).
- TESTS: none new; every test file named in the batch gate.
- FALSIFIER and CONTROL: a pin re-recorded whose tallies moved with no declared mover in the batch; the commanded field with no decider differing from the automatic one (`test_none_decider_equals_no_decider` red). Control: `python tools/ci_golden_modes_check.py` digests equal to B19's close.
- GATE: the BATCH GATE above.
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: V12 B20.01 to B20.21.
- GLOSSARY: none.
- COST and TIER: edit and instrument time; `sonnet`; the close's terminal critique `opus`.
- LANDS IT: B20's producer; `Item: B20.99`, the batch's last `Item:` commit (no `[skip ci]`).

| STOP. Batch B20-mb-orders closes here |

---

Batch B25-fi-questioning follows in `workplan_v12_part30_cont.md`. The last item this file wrote: B20.99.
