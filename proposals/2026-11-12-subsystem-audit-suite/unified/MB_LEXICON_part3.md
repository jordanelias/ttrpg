# The mass-battle lexicon, part 3: the ladder decisions, the rename batches, and the sweep

## Status: PROPOSED (continues `MB_LEXICON.md` and `MB_LEXICON_part2.md`)

## §3 · Where two good words competed: what is settled, and by which step

Ladder steps (CLAUDE.md §0): 1 superseded by a ruling, 2 irrelevant, 3 a design document, 4 precedent in the
tree, 5 what makes sense for the architecture. Each decision is reversible on Jordan's word.

| id | the competition | settled | step and basis |
|---|---|---|---|
| D-1 | **subformation**: A-59's grouping of units; the code's single unit (`armyrecord` key `subformations`, `orderofbattle.Subformation`); D-U1-11o's "formation post group" | **A group of units at one post of the army formation, fighting by one set of tactics, led by the officer its units name when one man leads them all.** Carried by two proposed columns already in the suite (the unit row's `post`, `04_MB_cell_hierarchy_as_data.md` §3; its `officer`, `27_MB_A` §3), so no new entity: a subformation is **read** over unit rows (A-2: a unit is a row; nothing new is stored). Its tactics are the doctrine row for its (troop class, post) (`26_MASS_BATTLE_maneuver_orders.md` §3) and any orders its units carry. [ASSUMPTION, reversible: where the units at one post name different officers it is still one subformation; each officer's span counts his own units] | 1 (A-59's words; A-94: Jordan's word stands and is settled here) and 4 (the engine's `Officer` already leads "one or more Subunits" under C5's ruled span, "max commanded = Command at every echelon", ED-MB-0067 row 2, built as ED-MB-0073; the doctrine rows are keyed by post). D-U1-11o and "formation post group" are retired |
| D-2 | **unit** vs subformation / subunit / body / block / company | **unit** for the row, everywhere | 1 (A-2: "a unit is a row"); 4 (the season verbs already say it: `form_unit`, `order_unit`, `disband_unit`); 5 (*body* is `Person.body`; *block* is `config.BLOCK_SIZE`, a hundred men) |
| D-3 | **formation** at two scales | **army formation** (Jordan's "grand formation") and **unit formation**, always qualified; bare "formation" refused where both could be meant | 1 (A-59 uses "grand formation" of the army); 5 (ordinary English uses "formation" at both scales, so the qualifier is the cheapest fix; the glossary's precedent: "capability role", "composition role", "unit role") |
| D-4 | the formation posts `front, rear, left, right, reserve` | **`centre`, `left`, `right`, `rear`, `reserve`**; the units on `left`/`right` are the **wings** | 5: `front` collides with the glossary's *front* (the width in contact) and with every unit's own front, and the post sits at the centre of the first line (`across: centre`); the period word is *centre* (CR D7, SQ §7). The posts are proposed data (P*): free to rename |
| D-5 | **commander** vs general / captain / marshal | **commander** (the holder of the army Record); **officer** (a unit's leader) | 4 (the tree: "an army is where its commander is", `seam/wrappers/mass_battle.py::_order_of_battle`; the verbs' "the commander's standing"); 5 (*Marshal* is a canon seat title, A-91, and the verb `marshal`) |
| D-6 | **recruit** vs levy vs muster vs raise | **recruit** is the act; **levy** is the troop type; **muster** is the men of a faction gathered at a place to march (`world_q.mustered`, `state/gate.py::may_muster`) | 4 (the verb `recruit`, the troop type `levy`, the query `mustered`, each a tree name that passes); `14_VERBS_MILITARY_C_the_muster.md` used "muster" and "levy" for recruiting: suite coinages, renamed (§5) |
| D-7 | **clocks**: field tick, engine phase, bout / turn / engagement / round, battle, season | one word per quantity: **field tick** (about four seconds) < **engine phase** (six ticks) < **bout** (18 ticks) < **battle** (one or more bouts) < **season** | 5. *Turn* is A-9's word for a person's short sequence and the duel's twelve turns; *round* is the season's scene slot and the duel round; *engagement* has three tree senses. The engine's 18-tick "turn" quotes a Jordan direction (`config.py:425`, "limit of three phases per simultaneous engagement per turn"), but that is not a term in `DECISIONS_ANSWERED.md`, and A-9 (a later ruling) gives "turn" another meaning, so by STAGES.md's own scope it is not a ruled term and the ladder may settle it; the quotation keeps its words |
| D-8 | the end state **drawn** vs the noun **a draw** | **"a drawn battle"**, "the battle was drawn"; the noun "a draw" never stands for the end state in MB prose | 5: the glossary's *draw* row already refuses the end-state sense in a sentence that also samples; MB prose samples in nearly every paragraph (the stand, obedience, rally, pursuit and return draws), so the stricter rule is the only one a reader can apply. Jordan's quoted words ("Draw on land taking march ...", A-58) stand as quoted |
| D-9 | **posture** vs the code field `stance` | prose **posture**; the army Record's row key and payload key `stance` → `posture` (L1-4); the engine attribute `Subunit.stance` keeps its name | 4 (`march_postures`, glossary *posture*); 5 on cost: `core/contact.py::check_orders` applies an order's behaviour by attribute name (`_ORDER_SAFE_FIELDS`), and the behaviours are exported data (`battle_orders.json`), so renaming the engine attribute is a change of the order format, not a rename; the Record-facing key is cheap |
| D-10 | **give ground** vs the engine attribute `yielding` | prose **give ground**; `yielding` keeps its name | 5, as D-9: `yielding` is an order behaviour key. The glossary's *yield* (a fighter gives up) is why the prose word differs |
| D-11 | **station** vs base vs origin vs home | **station**; *base* is Jordan's synonym (A-70) and stays in quotation; `march_origin` stays the code's | 1 (A-67, A-68, A-70 name the same place: where the march began, where the army returns on a drawn battle); 5 (*home* is a person's building) |
| D-12 | **strength** vs fighting power vs headcount | **strength** = men present and fit; nothing names a fighting value | 1 (A-59: a static side-wide fighting value is misleading; A-60: numbers act through frontage, depth and endurance); 4 (`armyrecord.to_order_of_battle`'s "strength"; Lanchester's) |
| D-13 | **kit** vs loadout | **kit** | 4 (`world_q.kit_of`, T); 5 (one word for one primitive; "kit" is the plainer). Supersedes the glossary's two-word row *loadout / kit* |
| D-14 | **order of battle** (the army as fielded) vs the Record kind `order_of_battle` (a side's standing order) | the army as fielded is the **order of battle** (`OrderOfBattle`); the Record kind is a **standing order** → `standing_order` (L1-3) | 4 (the reader is already `world_q.standing_order`, its docstrings say "standing order"); ordinary "order of battle" is an army's arrangement, not one role and a fall-back point |
| D-15 | the unit formation's columns `ranks`/`files` (P) vs `depth`/`width` | **`depth`, `width`**, counted in cells; prose gives men in parentheses ("two cells deep, eight men") | 4 (the engine's own `Subunit.depth`, `width`, `hierarchy/units.py:449-462`); 5 (*rank* already has two glossary senses, and `ranks: 2` reads as two men deep) |
| D-16 | the engine's `broken` (Discipline at nothing) vs **break** (to run) | **break** means to run; the engine's state is **disordered** (L2-2) | 5: the stand draw's `breaks` and the research (MV R3–R5) use *break* for the onset of a rout; a reader given "the unit is broken but still on the field" lands on the wrong thing |
| D-17 | **casualty** vs **loss**; **injured** vs wounded; **captured** vs taken | **casualty** = the engine's count of men put out of the fight; **loss** = every man missing after it, of four kinds **dead, captured, injured, fled**; fled men **regroup** or become **deserters** | 1 (A-69's "losses", "injury", "fleeing"; A-78's "died or got captured or deserted", "injured or who fled and regrouped"); 5 (*wounded* is a person's end state in a fight) |
| D-18 | **battle** vs field | prose **battle**; "field" for the ground and in tree identifiers | 4 (the tree's `a field`, `field.won`, `resolve_field` stay: ordinary English allows "won the field"); 5 (the player reads "battle") |
| D-19 | **prowess** of a person | **unit only**; a person's skill at arms is his **martial skill** | 1 (A-98 (3), 2026-11-12) |
| D-20 | **host** as the period word for an army | refused | 5: the tree's *host* is the season side that hosts a module ("host input builder", `seam/wrappers/`), in hundreds of docstrings |

**What survives for Jordan: nothing.** Every competition above is answered by a ruling or by the ladder; the one
open MB word (prowess of a person, J-U4d-03) was ruled by A-98 while this lane ran. No
`MB_LEXICON_FOR_JORDAN.md` is written (the brief: "only for what survives").

## §4 · The rename batches (tree names that fail the word test)

**Shape.** Two code batches, both hash-EQUAL by intent and therefore placed **ahead of the MB movers**
(STAGES.md, pinning rule 1: "hash-EQUAL refactors (owners, renames, loaders) are batched ahead of movers"), plus
the suite-side renames of §5 that the MB rewrite lanes apply to their own proposals before their batches land.
Every later MB proposal's instructions name the old identifiers; the batch close of each later MB batch reads
them through this table (old → new) rather than editing every proposal now.

**Slot in `unified/U3_DEPENDENCY_ORDER.md` §2.1.** A new row **`B16L-mb-words`** (lane MB, wave W3, after B00,
B01, B02; before B17) carrying L1; and **`B16M-mb-engine-words`** (lane MB, wave W4, after B16L; before B17)
carrying L2. B17, B19, B20, B22, B30, B31 each gain `B16L` (and B17 onward `B16M`) in their "after" column.
Why before B17: B17's members (`04_MB_typed_outcome_and_one_path`, `04_MB_unit_loadout_and_weapon_in_hand_B`)
edit `orderofbattle.py` and `armyrecord.py`; a rename after them is a second edit of the same symbols
(file-census rule 2). Both are MB-lane batches, so they run one at a time (one open batch per lane).
[ASSUMPTION: U3's §2.1 table is edited by the U3/v12 author, not by this lane; this lane writes no row there.]

### L1 · `B16L-mb-words`: the season-facing names (small)

| id | rename | files (measured with `git grep -l`, 2026-11-12) |
|---|---|---|
| L1-1 | army Record key `subformations` → `units`; the advisory kind `subformation_routs` → `unit_routs`; error and docstring text "subformation" → "unit" | `modules/mass_battle/armyrecord.py`, `engine/season/rosters.yaml` (`record_kinds.values.army` and the `army_verbs` note), `engine/season/loop/effects_information.py`, `engine/season/harness/military_menu.py`, `tests/valoria/test_army_verbs.py`, `test_army_battle.py`, `test_mass_battle_army_record.py`, `test_mass_battle_order_of_battle.py`, `test_army_menu_presets.py`, `test_army_phase5.py`, `systems/mass_battle/sim/stress.py`, `stress_scenarios.json`, `walkthrough.py`, `walkthrough_example.json` (15 files hold the string `subformations`) |
| L1-2 | `orderofbattle.Subformation` → `UnitRow`; `OrderOfBattle.subformations` → `units`; `__all__` | `modules/mass_battle/orderofbattle.py`, `armyrecord.py`, `massbattle.py`, `tests/valoria/test_mass_battle_order_of_battle.py`, `systems/mass_battle/sim/stress.py`, `walkthrough.py` (6 files hold `Subformation`) |
| L1-3 | Record kind `order_of_battle` → `standing_order` | `engine/season/data/rosters.py:588` (`ORDER_KIND`, the one owner of the string), `engine/season/rosters.yaml:266` and its note, `engine/season/verb_table.yaml` (`marshal` notes), `loop/effects_information.py:341`, `queries/inputs.py:196,242`, `queries/world_q.py:2302`, `engine/substrate/battle_orders.py:6`, `tools/export_battle_orders.py:4`, `engine/season/tests/test_cp_t04_02_marshal.py` (literals at :218, :225, :234, :306), `engine/season/hole_register.yaml` (prose only: leave the frozen text, add nothing) — 10 files |
| L1-4 | the army Record's unit-row key and the `order` payload key `stance` → `posture`; `orderofbattle.STANCES` → `POSTURES`; `UnitRow.stance` → `posture`; `armyrecord.options()['stances']` → `['postures']` | `armyrecord.py` (`form`, `order`, `_apply`, `options`), `orderofbattle.py` (`UnitRow`, `validate`, `_spec_for`, which still writes the **engine** spec key `stance`, D-9), `engine/season/loop/effects_army.py`, `harness/military_menu.py`, `verb_table.yaml` (`order_unit` notes), the six test files of L1-1 [ASSUMPTION: file list from the L1-1 set; not separately measured] |
| L1-5 | none (reserved: `retreat_at` was weighed against `fall_back_at` and **not** renamed; both pass and they belong to two holders with two value forms) | — |
| L1-6 | add the read **`orderofbattle.subformations(oob) -> tuple[(post, tuple[unit name, ...]), ...]`** — **only after `04_MB_cell_hierarchy_as_data.md` §3 lands the `post` column** (B19); until then nothing in code names a subformation | `orderofbattle.py` (the function and `__all__`), `tests/valoria/test_mass_battle_order_of_battle.py` |

**Ordered edits (L1-1 to L1-4, one commit each, in this order).**
1. L1-3 first (no other rename touches its files except `effects_information.py`): change `ORDER_KIND` in
   `data/rosters.py`; change the key in `rosters.yaml: record_kinds`; replace the string in the test literals;
   update the docstrings that say "order of battle" for the kind to "standing order". Do not edit
   `hole_register.yaml`'s historical text.
2. L1-2: rename the class and the field in `orderofbattle.py`; update `armyrecord.to_order_of_battle`
   (`Subformation(...)` → `UnitRow(...)`, `OrderOfBattle(tuple(parts), ...)` unchanged positionally) and
   `massbattle.py`'s readers of `oob.subformations`; then the test and the two sim scripts. Keep local
   variable names (`sf`) unless they read wrongly.
3. L1-1: rename the key in `armyrecord.KEYS`, `new`, every `record['subformations']` read, the messages; the
   `rosters.yaml` key list in the same commit (`test_mass_battle_army_record.py:189-190` pins the two equal);
   `effects_information.py`, `military_menu.py`, the tests and the JSON fixtures. Rename `subformation_routs`.
   Replace "trooper" with "man" in the docstrings touched.
4. L1-4: rename the row key and payload key; `STANCES` → `POSTURES`; `_spec_for` maps `posture` onto the
   engine spec's `stance` key (one line, commented with D-9).
- **Tests.** The covering files: `tests/valoria/test_mass_battle_army_record.py`,
  `test_mass_battle_order_of_battle.py`, `test_army_verbs.py`, `test_army_battle.py`, `test_army_menu_presets.py`,
  `test_army_phase5.py`, `engine/season/tests/test_cp_t04_02_marshal.py` (CLAUDE.md §0.4: the files covering the
  edit, mid-batch; the full suite once at the close).
- **Gate (expected reading).** (a) `git grep -n -E "\bsubformations\b|\bSubformation\b|order_of_battle\b" --
  modules engine tests tools systems` prints only `to_order_of_battle`, `_order_of_battle` and frozen
  `hole_register.yaml` text; (b) `python -m pytest engine/season/tests/test_go07_canonical_digest.py -q` green
  with **no pin re-recorded** (the realm hash pins at seeds 0–2 equal); (c) `python tools/ci_golden_modes_check.py`
  digests equal.
- **Falsifier.** A shipped seeded season whose content hash moves: it would show an `army` or a standing-order
  Record minted in a natural run, which the [ASSUMPTION] below denies.
- **Hash movers.** None declared. [ASSUMPTION: no shipped seeded world mints an `army` or `order_of_battle`
  Record, because the six army verbs and `marshal` are in `Fixtures.withheld_verbs`
  (`engine/season/data/fixtures.py:1157`) and the army mint is reached by the menu harness; a Record's kind and
  `subject_matter` keys are folded into `World.content_hash()` (`state/world.py:1667-1707`), so a world that does
  hold one moves. Not measured: gate (b) measures it. If (b) moves, the batch is a declared mover and is
  re-placed after B22 with the army batch's re-pin.]
- **Dependencies.** None in code; L1-6 waits on B19.
- **Glossary.** The same commit edits `U1_GLOSSARY.md` §J rows *unit*, *subformation*, *standing order*,
  *posture* to point at the new identifiers (STAGES.md, "every v12 batch").
- **Cost class.** Small; `sonnet` producer, effort `high`; no `opus` node (no judgment left).

### L2 · `B16M-mb-engine-words`: the engine's names (large; may be cut)

| id | rename | files |
|---|---|---|
| L2-1 | engine `hierarchy.units.Unit` (one side's army in a battle) → `Army`; then `Subunit` → `Unit`; `Unit.subunits` → `units`; `SUBUNIT_CAP` → `UNIT_CAP`; `SUBUNIT_ROUT_FLOOR` → `UNIT_ROUT_FLOOR`; `core/exchange.py::subunit_combat_pool` → `unit_combat_pool`; `MassBattleInput.subunits` and the fixture `field_subunits` → `units`, `field_units` | `Subunit` in 46 files, `subunits` in 71, `SUBUNIT_` in 26, `Unit(` in 16 (overlapping), across `modules/mass_battle/` (14), `systems/mass_battle/sim/` (6), `tests/valoria/` (17+), `tests/sim/`, `engine/season/queries/inputs.py`, `engine/season/data/fixtures.py`, `engine/season/seam/wrappers/mass_battle.py`; `.audit/` copies are not edited |
| L2-2 | `Subunit.broken`, `Unit.broken` (Discipline at nothing) → `disordered`; `cell_broken` keeps its name (a cell's morale at nothing: the break sense) | 16 files hold `.broken`/`'broken'` |
| L2-3 | `battle_loop.run_battle(max_turns=18)` → `max_ticks`; its local `turns` → `ticks` | 22 files hold `max_turns` or a `["turns"]` read (49 sites) |

**Ordered edits.**
1. L2-3 first, identifiers only: the parameter and local names. **The returned dict keeps the key `"turns"`**
   in this batch (its readers include traces and goldens); `"turns"` → `"ticks"` is a separate declared mover if
   wanted, and `FieldOutcome` (proposed) is born with `ticks` (S-3).
2. L2-2: rename the attribute on both classes and every reader; keep any emitted string (trace event fields)
   unchanged in this batch.
3. L2-1 in two steps in one commit: (a) `Unit` → `Army` with a word-boundary match that excludes `Subunit`,
   `UnitRow`, `unit_` and `_unit` (and `build_unit`, `_weighted_unit`, `_person_unit`, which keep their names
   or become `build_army`-style names only where they build an `Army`); (b) `Subunit` → `Unit`, `subunits` →
   `units`, the constants and the pool function. Python identifiers only: **no dict key or emitted string
   changes** (e.g. `massbattle.py:346`'s `{'subunits': ...}` result key stays), so nothing serialised moves.
- **Tests.** `tests/valoria/test_field_golden_pins.py`, `test_mass_battle_order_of_battle.py`,
  `test_frontage_conservation.py`, `test_mass_battle_routes.py`, `test_mass_battle_yield.py`, `test_reach_weapon_class.py`,
  `test_body_contact_toi.py`, `test_body_no_interpenetration.py`, `test_friction.py`,
  `engine/season/tests/test_cp_t04_01_person_subunits.py`; `python tools/tests_for_diff.py` names the rest; the
  full suite once at the close with `-m mass_battle` first.
- **Gate (expected reading).** `python tools/ci_golden_modes_check.py`: every mode's digest equal;
  `python -m systems.mass_battle.sim.lanchester_signature` reads as before the batch (same verdict lines);
  `engine/season/tests/test_go07_canonical_digest.py` green, no pin re-recorded; `git grep -n -w Subunit --
  modules systems tests engine` prints nothing.
- **Falsifier.** Any golden digest moving: it would show a class or attribute name reaching serialised state
  (a `repr` in a trace, a key built from `type(x).__name__`). The batch then stops; the moved digest names the
  site.
- **Hash movers.** None declared. [ASSUMPTION: no MB golden digest hashes a Python identifier; the canonical
  encoder hashes values, not class names (`state/world.py:1688-1696`, "not `repr()`"), but the engine's own
  `bat.py` digests were not read. Not measured.]
- **Why it may be cut.** It is the largest rename in the suite (about 80 files) and buys a correct code
  vocabulary for the port (`godot/`), not a game change. If the critical path cannot carry it, cut it: the
  suite's prose already says **army**, **unit**, **disordered**, **tick**, and gives the identifiers in
  backticks once. Cut or not, it must not be split across batches (half-renamed classes are worse than either).
- **Cost class.** Mechanical but wide: `sonnet` producer, effort `high`; the gate readings by `haiku`
  (`valoria-measure`).

### Not renamed (weighed and kept)

`stance` and `yielding` on the engine's unit (D-9, D-10: order-format changes); the engine's `tick`, `phase`
(hundreds of sites; prose qualifies); the army Record key `strategy` (passes); `trained` (passes: recruited men
are trained, the act needs a training place); `mustered` and the `muster` basis (pass in the march sense);
`levy` (passes as a troop type); `field` in identifiers (D-18); the `garrison Sites` wording (tree prose only);
`retreat_at` / `fall_back_at` (L1-5).

## §5 · The sweep: what was edited now, and what is owed

### 5.1 Edited by this lane (each file's `Reconciled:` line names the change)

| file | change |
|---|---|
| `unified/U1_GLOSSARY.md` | new §J "Mass battle lexicon" (a pointer row per term); rows corrected: *unit*, *formation*, *body*, *post*, *loadout / kit*, *rout / break*, *bout*, *cell*; §H rows `subformations`/`Subformation`, MB `stance` updated with this file's costs |
| `unified/U1_OWNERS_AND_VOCABULARY.md` | D-U1-11o: superseded-by pointer (A-94, this file D-1) |
| `proposals/27_MB_B_unit_prowess_on_the_row.md` | §1 table row 4, §2 two bullets and gate 5: A-59's "subformation" is no longer read as the unit's cell arrangement |
| `proposals/04_MB_cell_hierarchy_as_data.md` | §1 Words: the levels are army, subformation, unit, unit formation, troops; the second Folded line's item (1) |
| `proposals/04_MB_typed_outcome_and_one_path.md` | `FieldOutcome.turns` → `ticks` (S-3) at its declaration and the base-field list |
| `proposals/26_MASS_BATTLE_aggression_and_land.md` | "on a draw" (the end state) → "after a drawn battle" in the rule and the NERS lines |

### 5.2 Owed: suite renames the MB rewrite lanes apply before their batches land

Not swept now because each is a many-site rename across files whose batches have their own authors; a partial
sweep would leave two words in one batch. Each is a word change only.

| id | rename | where (counts by `grep -c`, lines not all read) | applied by |
|---|---|---|---|
| S-1 | "general" (the commander) → **commander**; `GeneralAction` → `CommanderAction` | `26_MASS_BATTLE_rout_pursuit_and_giving_ground` (11), `16_PESSIMIST_MB_rout_has_two_exits` (8), `26_MASS_BATTLE_maneuver_orders` (6), `04_MB_manager_battle_one_resolver` (3 + title + §4 class), `27_MB_A` (4), `04_MB_playable_field_scenario` (2 + `GeneralAction` at :80, :198), `26_MASS_BATTLE_cell_scale_and_time` §3 (`GeneralAction` at :107, :116) | B19 and B20 authors |
| S-2 | field share `taken` → **`captured`** | `26_…rout…` §4, `27_MB_E` §1–§2, `16_PESSIMIST_MB_rout_has_two_exits` step 5, `U1_OWNERS_AND_VOCABULARY.md` D-U1-11e | B19 author (D-U1-11e by the v12 author) |
| S-3 | `FieldOutcome.turns` → **`ticks`** | done in `04_MB_typed_outcome` (5.1); `U1_OWNERS_AND_VOCABULARY.md` D-U1-11e's base-field list still says `turns` | v12 author |
| S-4 | `muster_room` → **`recruit_room`**, `muster_difficulty` → **`recruit_difficulty`**, `levy.shirked` → **`recruit.shirked`**, "muster seat" → "recruiting seat", the title's "the muster" → "recruiting" (the file name stays) | `14_VERBS_MILITARY_C_the_muster.md` (12 "muster", 22 "levy"; the troop-type uses of "levy" stay) | B22 author |
| S-6 | post `front` → **`centre`** | `04_MB_cell_hierarchy_as_data.md` §3 YAML and `default_post`, `26_MASS_BATTLE_maneuver_orders.md` §3, `27_MB_D_the_commander_as_chooser.md` data rows (:200), `27_MB_A` §2 ("the army's rear centre" stays) | B19 author (`04_MB_cell`), B20 author |
| S-7 | unit-row and troop-row columns `ranks`, `files` → **`depth`, `width`** (cells; prose gives men) | `04_MB_cell_hierarchy_as_data.md` §2 (28 "rank" hits), `27_MB_B` §1, `26_MASS_BATTLE_movement_and_fatigue_as_data` §4, `27_MB_D` §1 table, `14_VERBS_MILITARY_D` (Folded line 3), `16_PESSIMIST_MB_partition_and_the_pair_rule` | B19 author |
| S-8 | "body" (a unit) → **unit** | 22 MB files; largest: `26_…rout…` (26), `14_VERBS_MILITARY_D` (19), `26_…movement…` (15), `04_MB_unit_loadout_and_weapon_in_hand_B` (13) | each MB batch author for his own files (STAGES.md rule 3) |
| S-9 | "loadout" (prose) → **kit**; "troop kind" → **troop type**; "subunit" (prose) → **unit** | `04_MB_unit_loadout_and_weapon_in_hand_B`, `16_PESSIMIST_MB_one_stamina_ledger`, `04_MB_cell_hierarchy`, `27_MB_B` (14 "subunit"), `27_MB_A` (5) | each MB batch author |
| S-10 | "engagement" for a bout or a battle → **bout** / **battle** | `16_PESSIMIST_MB_rout_has_two_exits` (title, :48), `26_MASS_BATTLE_cell_scale_and_time` (:49–50), `04_MB_playable_field_scenario` (5), `U5b_MB_residue` (CP-T04-04, R-29) | B19, B20 authors |
| S-11 | "a draw" (end state) → **a drawn battle** | `04_MB_headcount_grade_and_scale.md` :21, :46 (and its 18 "drawn" hits, mostly correct, not read one by one) | B17 author |
| S-12 | strength meaning fighting power → **fighting power**, or rewrite as "where it stands decides" | `27_MB_C_dynamic_strength_and_the_residual_chance.md` title line and §1 (file name stays) | B19 author |

### 5.3 What this lane could not check

- Every hit of a common word (body, general, rank, turn, draw) was counted, not read; the owed list gives counts.
- The engine's `bat.py` golden digests (L2's hash claim) and whether any natural run mints an army Record (L1's)
  were not measured; each batch's gate measures them.
- The `.audit/` and `.designs/` copies were not searched (quarantined; not live).
- `14_VERBS_MILITARY_A_movement.md`, `14_VERBS_MILITARY_B_train.md`, `04_MB_cr12_linear_law.md`,
  `26_MASS_BATTLE_calibration_targets.md` were read only at grep hits.
