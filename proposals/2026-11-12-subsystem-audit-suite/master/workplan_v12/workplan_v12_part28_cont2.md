# Workplan v12 — part 28, continued (2): B18-pc-content

## Status: PROPOSED (second continuation of part 28 of workplan v12, author lane A28; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

Words and paths are the part's own. `PCR-3` (B16) renamed the fight's words in code (`max_bouts` → `max_rounds`, `turn_start` → `round_start`, `engagement_end` → `round_end`); `IS-PC-05` (B15) dropped the combat attribute `faculty` (A-112); B04 deleted `rosters.yaml: verb_capability` (CAP A3). Copied text that uses an old name carries `NAMES:`.

---

## Batch B18-pc-content · lane PC · wave W14 · step S15 (D-20) · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B18-pc-content
IN-FLIGHT ROW: registers/handoffs/HANDOFF_PC.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B14-pc-outcome
GATE: Batch B15-pc-calibration
GATE: Batch B16-pc-round
GATE: Batch B17-mb-scale
REQUIREMENT: none — content for the standalone duel (§2.2's B18 row; M5): persons stop being identical fighters, a loadout is a choice. The close re-reads R-09's by-person reading for combat (`03_PC_person_inputs_content` Gate 2) and R-04.c5 (i) (`aperture 2 s`: `challenge` executed above 0, s = 0–2) and records them; no `status:` is edited (A-114).
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command):
  `python tools/export_engine_params.py --check` → exit 0 (the slot tuples and the `unarmed` record in the export);
  `python -m pytest tests/valoria/test_combat_invariants.py tests/valoria/test_combat_units_refactor.py engine/season/tests/test_cp_t03_03_kit.py engine/season/tests/test_cp_t03_04_arms.py -q` → pass; `python -m pytest tests/valoria -m combat -q -n auto` → pass (a batch inside `modules/combat`, `systems/combat` and the season's combat seam: `tools/tests_for_diff.py` names the rest);
  the realm reading (`03_PC_person_inputs_content` Gate 1): "the count of distinct `(kit, faculty, end, attributes)` tuples over persons is above 1, reported per seed 0 to 2" (`faculty` read as the skill score in `arms`, `NAMES`);
  Gate 2: "two persons with different inputs, the same opponent and the same seed set, show different felled shares outside the disjoint-seed control band (46.1 to 49.3 in the mirror)", run through `systems/combat/combat_engine_v1/workbench/balance.py::winrate` at 1,000 fights per cell, the band re-read on this tree first (the quoted band predates B15's calibration);
  Gate 4: "With `arms_kinds` emptied and the templates reverted, the pre-change season hashes return" (planted in process, not committed);
  `03_PC_loadout_and_carry` Gate 1: "Hash EQUAL with every secondary absent (the harness term relocated, same value): season pins and the combat goldens unchanged" (read at B18.07);
  `python -m engine.season.harness.aperture 2 --seeds 0 1 2` → `challenge` executed per seed and the `BUILT OUT` line, quoted (before `reading @<B17 close sha>` — the last close that ran this instrument on the PC lane's base is named in the commit);
  `python -m engine.season.harness.register --check` → exit 0; `--requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line quoted; `python tools/ci_golden_modes_check.py` → the mass-battle digests equal to B17's (`reading @<sha>`): nothing here reads a troop row (B18.06's `carry_demand_of` is not called by the MB host until B31);
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the two re-read conjuncts with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before and after, and the batch's measured wall time; no `reading:` record is written (no conjunct is this batch's) and `status:` is not edited (`IS-A-12`).
RE-PIN: once, at B18.99: the realm pins in `engine/season/tests/_realm_goldens.py` and every seeded result B18.04, .05, .08, .09 moved, against B17's close rebased on B12c's merge (§7.4; `reading @<sha>`). B18.03's `tests/valoria/r3_identity_golden.json` and the armour reference (`workbench/data/combat_armour_reference.json`) are re-recorded in B18.03's own commit by their generators (a pin only that item moves, E-1).
IDS: ED-PC 0; H 0
DIALS AT CONTROL: `CARRY_CLOSE_K` = 0 (`CFG`, `[SIM-CALIBRATE]`, "0 as the control"); set by B98; target: `03_PC_loadout_and_carry` Gate 2, "a Strength-4 spearman carrying an arming sword against the same spearman without one shows more stamina spent and a slower close; at Strength 7 the two are inside the control band" (1,000 fights per cell, disjoint-seed control).
C(B18-pc-content): this batch's entries; the plan's head parts; `unified/U1_GLOSSARY.md` rows *skill*, *skill score*, *round*, *riposte*, *kit*, *loadout*;
  `modules/combat/attributes.py`, `weapons.py`, `combat_systems.py` (`act_cost`, `close_rate`, `close_unwieldiness`), `config.py` (`CFG`), `combatant.py`, `fight.py`, `wrapper.py` (read: the consult and `ACT_THRESHOLD`), `contact.py` (read); `engine/substrate/combat_kit.py`; `engine/season/queries/inputs.py` (`PersonalCombatInput`); `engine/season/seam/wrappers/combat.py` (`combat_input`); `engine/season/queries/world_q.py` (`kit_of`); `engine/season/rosters.yaml` (`matter_kinds`, `arms_kinds`, `arms_at_build`, `lifepath_templates`); `engine/season/data/rosters.py` (`_check_arms_at_build`, `_load_lifepath_templates`); `tools/export_engine_params.py`; `engine/engine_params/combat_engine_v1.json`; `systems/combat/combat_engine_v1/workbench/balance.py`, `build_levers.py`, `data/combat_armour_reference.json`; `tests/valoria/r3_identity_golden.json`;
  `proposals/U5b_PC_residue.md` §3, `proposals/03_PC_person_inputs_content.md`, `proposals/03_PC_loadout_and_carry.md` (each item copies what executes; Part B's table is read from the item);
  the tests named in the items; instruments: `winrate`, the census (B18.01), `aperture`, `register`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`, `tools/ci_golden_modes_check.py`; `engine/season/tests/_realm_goldens.py`;
  the closing SHAs of B14, B15, B16, B17; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_PC.md`, the skill and `methodology-close`).
UNDECIDED: (1) **Part A's "two more tuples"**: the source extends `attributes.py` "with two more tuples in the same form" and lists six slot families, three already read from an existing spec or field (`attr` from `SPEC`, `pool` from `core.py`, `kit` from `Combatant`). Taken: the two are `axis` and `lever` (the families whose members the source lists as module constants with read sites), `temper` (one member, `disp`) carried as a third only if `attributes.py` holds no `disp` row at the item's open `[ASSUMPTION — basis: the table's "read at" column]`. Other reading: `axis` and `temper`. (2) **B14.11 already added** `PersonalCombatInput.axes`, `traditions`, `techniques`, `dispositions` (`03_PC_typed_outcome_one_door` Part B, "The season fills none of them until a carrier exists (`03_PC_person_inputs_content.md`)"); Part A here adds no second field for a family B14.11 carries; it adds the slot tuples, the export, and the host's filling. (3) **Part D's `verb_capability`**: B04 deleted the roster; the templates' second key names `capabilities:` rows after B04 (`NAMES`), and `arms` is one (B04.02's block). (4) **`03_PC_loadout_and_carry` items 2 and 3** are one item (E-13: one gate, "the harness term relocated, same value", needs both). (5) **D-20** puts B18 at S15 after B29; it shares no file with B29 (`14_VERBS_PHYSICAL_A` A1–A2) by the census rows read.
SERIAL EDGES (written after the position table, E-11): B18.01 → B18.04 ("`03_PC_person_inputs_content.md` Part B admits a kind to `arms_kinds` only with its census row named in the commit body"); B18.02 → B18.03 → B18.04 → B18.05 (the source's "Order of edits": Part A → Part C → Part B → Part D); B18.05 → B18.06 (`03_PC_loadout_and_carry` "after `03_PC_person_inputs_content.md` Parts B–D") → B18.07 → B18.08 → B18.09 (its own order (1) to (5)); B18.99 last.
  With other batches, by file (U3 §5.1): `engine/substrate/combat_kit.py` B14 → B18 (`03_PC_weapon_records_in_the_export`); `modules/combat/combat_systems.py`, `config.py` B14 → B15 → B16 → B18; `seam/wrappers/combat.py` B04 → B06 → B14 → B15 → B16 → B18; `queries/world_q.py` (`kit_of`) B12c → B18 (same step, different function); `rosters.yaml` (`matter_kinds`) B12c.25 (`arms`) → B18.04 (`arms_*`, `harness_*`), different members, merged in §2.1's order; `04_MB_unit_loadout_and_weapon_in_hand_B` stages 3–4 follow in B31 (U3 §4.1 row 61).
PARALLEL: S15 with B12c (SE+WR), B19 (MB), B21d (FA), B24a (SC), B41 (GO). Shared: `rosters.yaml` and `queries/world_q.py` with B12c (different keys and functions; B12c merges first); `modules/combat/` is read, not edited, by B19 (MBA-04 samples the contact table B19a measured; B18's `CARRY_CLOSE_K` at 0 and the relocated harness term leave the duel's numbers equal, so B19a's table stays valid — B18.07's gate is the check). Movers merge in §2.1's order: B12c, B18, B19, B24a, B21d, B41.
BACKGROUND RUN: B18.01's census (every startable weapon against every other at each armour tier), sized on two small runs (n 100 and n 200 per cell) at the batch's open, launched in the background, read at B18.04's gate; its wall time and worker count go in B18.01's commit body (the skill, "Running a slow instrument").
COST: small builds and one content landing; producer `valoria-author` on `sonnet`, `high`; the census and the workbench readings extracted on `haiku` (`valoria-measure`) and read by `opus` (the sources' "Lands" lines); Part B's values are Jordan's (`[ASSUMPTION; low]`); the close's terminal critique `opus`.
EST: 8.5 h [estimate: §2.4's formula over this block's 10 positions, 0.4 h × 10 + 2.5 h, + 2 h for the census instrument run]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B18.01 | a census before an inventory | `U5b_PC_residue` §3 | BUILD | EQUAL | Batch B15 (the calibration the census runs after) |
| B18.02 | the slot interface: the module declares what it can take | `03_PC_person_inputs_content` Part A | BUILD | EQUAL | Batch B14 (B14.11's four fields); Batch B15 (`IS-PC-05`) |
| B18.03 | the unarmed fighter | `03_PC_person_inputs_content` Part C | BUILD | EQUAL (season); re-records its two artifacts | B18.02 |
| B18.04 | a starter inventory, each kind with its census row | `03_PC_person_inputs_content` Part B | CONTENT | MOVER(behaviour) | B18.01, B18.03 |
| B18.05 | the martial lifepaths hold `arms` | `03_PC_person_inputs_content` Part D | BUILD | MOVER(behaviour) | B18.04 |
| B18.06 | one carry rule at the kit's owner | `03_PC_loadout_and_carry` item 1 (resolution 2) | BUILD | EQUAL | B18.05 |
| B18.07 | the shortfall rides the input; the harness term moves; the close slows | `03_PC_loadout_and_carry` items 2, 3 (resolution 3) | BUILD | EQUAL | B18.06 |
| B18.08 | a kit has a secondary | `03_PC_loadout_and_carry` item 4 (resolution 1) | BUILD | MOVER(behaviour) | B18.07 |
| B18.09 | the weapon in hand is round state; a switch costs tempo | `03_PC_loadout_and_carry` item 5 (resolution 5) | BUILD | MOVER(behaviour) | B18.08; Batch B16 (PB step 4) |
| B18.99 | re-pin and close readings | `_part4` E-1 | BUILD | MOVER (the re-pin) | B18.01 to B18.09 |

Not in this batch, and where each is: `U5b_PC_residue` §1, §2, §4–§10 (B14, B15); `03_PC_loadout_and_carry` resolutions 4 and 6 (the unit row, B31, `04_MB_unit_loadout_and_weapon_in_hand_B` stages 3–4); tradition and disposition carriers (PC-21, design-first, "no carrier is proposed here"); CHAR's authored attributes for realm persons (BA1, `IS-A-11`).

### B18.01 — a census before an inventory · `U5b_PC_residue` §3 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5b_PC_residue.md` §3 (pessimist R-9; F-PES-PC-12; R-PC-12), its "Lands in batch" ("§3 in B18 (`B18-pc-content`, before `03_PC_person_inputs_content.md` Part B)"), "Lands and tier" ("§3's census run by `haiku` (`valoria-measure`) and read by `opus`").
- ADVANCES: none of the nine; the reading Part B's content lands behind.
- INSTRUCTION (copied): "1. One workbench instrument, `workbench/balance.py::census(n)`: every startable weapon against every other at each armour tier, tracker-true (never `fight`'s integer), printing each cell beyond 95% with its disjoint-seed control. It is run **after** the calibration batch (the scale, the bare zone and the riposte each move the cells). 2. `03_PC_person_inputs_content.md` Part B admits a kind to `arms_kinds` only with its census row named in the commit body: either no cell beyond 95% against the kinds already admitted, or the answering kind admitted with it (the estoc with plate)." "This is a reading the content lands behind, not a guard: it has no CI row." `census` builds its fighters through `winrate`'s record builder (B14.11: the workbench calls `modules.combat.fight:fight`), never a second entry. Run it once here (BACKGROUND RUN line) and write the full table in this commit's body.
- WHERE: `systems/combat/combat_engine_v1/workbench/balance.py` (`census`, beside `winrate`).
- TESTS: none new ("Movers. None (an instrument)"); `tests/valoria -m combat` covers the module unchanged.
- FALSIFIER and CONTROL: "A season fight between two admitted kits whose census cell reads beyond 95% and was not named." Control: each printed cell beside its disjoint-seed control.
- GATE: `python -c "from systems.combat.combat_engine_v1.workbench.balance import census; census(200)"` → the table printed, every cell beyond 95% listed with its control; the full run's table (n sized by the two small runs) in the commit body; `git diff --stat` touches only `balance.py`.
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B15 (the calibration: the scale, the bare zone, `finalblow_riposte`); V12 Batch B14 (B14.11's one door); EXISTS-IN-TREE `workbench/balance.py::winrate`, `modules/combat/weapons.py::WEAPONS`.
- GLOSSARY: none.
- COST and TIER: small build (an instrument); `sonnet`, `high`; the run's extraction `haiku`, read by `opus`.
- LANDS IT: B18's `valoria-author` producer, `isolation: worktree`; `Item: B18.01`, `[skip ci]`.

### B18.02 — the slot interface: the module declares what it can take · `03_PC_person_inputs_content` Part A · BUILD · HASH EQUAL
- SOURCE: `proposals/03_PC_person_inputs_content.md` Part A (with its U5b, W3-1 and A-112 reconciliations), "Implementation" (order, call sites); `U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §1–§3 (the `fight` site), D-U1-08; `U5b_PC_residue` §1 item 4 ("the `axis` slot family … takes its bounds from the skill row (U1 §2 `scale`), and `technique` and `grab` are not members"); UNDECIDED (1), (2); closes R-PC-13 (the interface half).
- ADVANCES: none at the control; R-09's by-person reading for combat once B18.04 fills slots.
- INSTRUCTION (copied): "The module owns one list of input slots and nothing about who fills them. Extend `modules/combat/attributes.py` (already the one owner of the attribute spec, PC-14) with two more tuples in the same form, exported in the typed export's `attributes` section." The families, as the source's table states them: `attr` (`strength, agi, end, att, spirit, focus`; `attributes.SPEC`; 1 to 7; `faculty` already dropped by `IS-PC-05`); `pool` (`scores`, `addends`: "the party's **skill score** … and his registered pool addends, carried raw beside `pool_add`, `pool_floor`, `opposition_rate`. The opponent's obstacle is `opposed_ob(the defender's skill score, opposition_rate)`, the one rule"; "the pool is `sigma_leverage.pool_of(score, addends, pool_add, pool_floor)`"); `axis` (`balance, parry, dodge, bind`; "`technique` and `grab` … withheld from the slot family until a sweep shows otherwise"; "additive σ bonus, 0 untrained"); `lever` (`visual, precommit, tactile, tempo, balance, measure, leverage, counter_select, counter_success, anti_overcommit, edge_read, spine_press, edge_grab, choke_control, facing_regime`; "a factor (`*`) or a bonus (`+`)"); `temper` (`disp`; 1 to 7, 4 neutral); `kit` (`weapon`, `armor`). "`PersonalCombatInput` … carries, per party, a mapping per family. The module takes **numbers per slot**, never the name of a skill, technique or tradition: the host composes a person's skills into slot values by the authoring surface's rule. That makes `ABILITIES`, `TRADITION_KIT` and the tradition gate (`ability_primitives.py`) authoring data and host-side composition, not module code; the module keeps `ability_factor`'s clamp and the lever maths." Call sites: "The host fills the slots in `seam/wrappers/combat.py::combat_input` from the skill surface (`U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §8 reader interface); `modules/combat/fight.py` reads them." The per-family mappings are B14.11's four fields (`axes`, `traditions`, `techniques`, `dispositions`) plus the existing `kits` and the record's `scores` (B15); no new field duplicates one (UNDECIDED (2)). Every slot defaults to the value the engine uses today ("Part A: nothing until a slot is filled").
- WHERE: `modules/combat/attributes.py` (the two tuples); `tools/export_engine_params.py` (the `attributes` section carries them); `engine/engine_params/combat_engine_v1.json` (re-derived by the tool); `engine/season/seam/wrappers/combat.py` (`combat_input` fills the slots; empty while no person holds a value); `modules/combat/fight.py` (reads them into `Combatant`).
- TESTS: `[ASSUMPTION: test names; the item creates them]` `tests/valoria/test_combat_units_refactor.py::test_the_slot_tuples_are_in_the_export` and `::test_an_empty_slot_reproduces_todays_fight` (one seed, one matchup, record equal), red first.
- FALSIFIER and CONTROL: the source's "a skill or lever value that changes an outcome without appearing in the record". Control: the realm hash at seed 2, one season, equal to B17's close rebased (`reading @<sha>`); the combat goldens equal.
- GATE: `python tools/export_engine_params.py --check` → exit 0; `python -m pytest tests/valoria/test_combat_units_refactor.py tests/valoria/test_combat_invariants.py -q` → pass; the seed-2 one-season hash → equal.
- HASH MOVERS: "Part A none".
- DEPENDS ON: V12 Batch B14 (B14.11; `03_PC_weapon_records_in_the_export`); V12 Batch B15 (`IS-PC-05`; `U5b_PC_rulings_in_the_fight` §2's raw `scores`); V12 Batch B05 (`sigma_leverage.pool_of`, `opposed_ob`); V12 Batch B04 (the `fight` site rows, U1-A); EXISTS-IN-TREE `modules/combat/attributes.py::SPEC`, `queries/inputs.py::PersonalCombatInput`, `seam/wrappers/combat.py::combat_input`.
- GLOSSARY: *skill* row keeps "the slot family `axis` (was `skill`)" in its rejected column; no new word.
- NAMES: `faculty` (the source's U4d line) → skill score (A-112, `IS-PC-05`).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B18's producer; `Item: B18.02`, `[skip ci]`.

### B18.03 — the unarmed fighter · `03_PC_person_inputs_content` Part C · BUILD · HASH EQUAL (season); its two artifacts re-recorded here
- SOURCE: `proposals/03_PC_person_inputs_content.md` Part C, "Implementation" (tests), "Gate" 4.
- ADVANCES: none at the control; a person with no weapon fights unarmed once B18.04 lands.
- INSTRUCTION (copied): "`modules/combat/weapons.py` gains one record, `unarmed`: a one-handed blunt element with the mass and lever of a forearm and fist, `head_len` below `GRAB_SHORT_REACH_M` so `contact.py`'s open-contact exemption (which already speaks of an unarmed class) applies to it. It is a physical record like the other 54; nothing in the engine branches on its name. `engine/substrate/combat_kit.py` exposes it as the weapon a person holds when he holds none; `queries/world_q.py::kit_of` returns it for the weapon field when `ARMS_KINDS` is non-empty and neither his holdings nor his residence stock a weapon. While `ARMS_KINDS` is empty the default stays as it is, so nothing moves until Part B lands." "Cost stated: a new roster record re-records `tests/valoria/r3_identity_golden.json` and the armour reference (`workbench/data/combat_armour_reference.json`) by their own generators, and must pass `tests/valoria/test_combat_invariants.py`." The record's numbers are written `[ASSUMPTION; low; Jordan to correct]` and listed in the PR body (D-19). The record count "the other 54" is read by command at the open (B14's export work changed the startable set to 50: B14's "`WEAPONS` reads the 50").
- WHERE: `modules/combat/weapons.py` (`unarmed`); `engine/substrate/combat_kit.py` (the no-weapon default); `engine/season/queries/world_q.py` (`kit_of`); `engine/engine_params/combat_engine_v1.json` (re-derived); `tests/valoria/r3_identity_golden.json`, `systems/combat/combat_engine_v1/workbench/data/combat_armour_reference.json` (re-recorded by their generators); `engine/season/tests/test_cp_t03_03_kit.py`.
- TESTS (copied): "`engine/season/tests/test_cp_t03_03_kit.py::test_a_person_with_no_stocked_weapon_fights_unarmed_when_arms_kinds_is_nonempty` and `::test_kit_of_unchanged_while_arms_kinds_is_empty` (the control)"; `tests/valoria/test_combat_invariants.py` ("Part C must pass it"); red first where new.
- FALSIFIER and CONTROL: "a person with no stocked weapon who still fights with an arming sword" (once `ARMS_KINDS` is non-empty). Control: `ARMS_KINDS` empty → `kit_of` unchanged; the season hash at seed 2 equal.
- GATE: `python -m pytest engine/season/tests/test_cp_t03_03_kit.py tests/valoria/test_combat_invariants.py -q` → pass; `python tools/export_engine_params.py --check` → exit 0; the season hash at seed 2, one season → equal to B18.02's.
- HASH MOVERS: "Part C `r3_identity_golden.json` and the armour reference" — re-recorded in this commit (E-1: a pin only this item moves); the season pins none.
- DEPENDS ON: V12 B18.02; EXISTS-IN-TREE `modules/combat/weapons.py::WEAPONS`, `contact.py::GRAB_SHORT_REACH_M`, `engine/substrate/combat_kit.py`, `world_q.py::kit_of`, the generators of the two artifacts `[grep at the open; name each in the commit]`.
- GLOSSARY: none.
- COST and TIER: small build with two generated artifacts re-derived; `sonnet`, `high`.
- LANDS IT: B18's producer; `Item: B18.03`, `[skip ci]`.

### B18.04 — a starter inventory, each kind with its census row · `03_PC_person_inputs_content` Part B · CONTENT · HASH MOVER(behaviour)
- SOURCE: `proposals/03_PC_person_inputs_content.md` Part B (with the R-9 reconciliation), "Hash movers"; `U5b_PC_residue` §3 item 2; D-19 (authored values landed at their batch and ratified at its merge); "Every content value in Part B is `[ASSUMPTION; low; Jordan to correct]`: the roster's own note reserves the inventory to Jordan".
- ADVANCES: R-09 (by person, for combat); R-06 (a character is customised by kit).
- INSTRUCTION (copied): "`engine/season/rosters.yaml: matter_kinds` gains seven kinds; `arms_kinds: kinds:` maps them:" `arms_dagger` (weapon, `dagger`, 1), `arms_spear` (weapon, `spear`, 2), `arms_sword` (weapon, `arming`, 3), `arms_longsword` (weapon, `longsword`, 4), `harness_light` (armor, `light`, 1), `harness_mail` (armor, `medium`, 2), `harness_plate` (armor, `heavy`, 3). "`arms_at_build: kinds:` seeds a small count on the rung kinds that would hold them (a settlement's armoury, a seat-holder's own holding). The `rung_kinds` members are `person, hearth, community, settlement, territory, province, duchy, realm` …; the loader refuses a key that is not a member (`data/rosters.py::_check_arms_at_build`)." "The ranking is by the engine's own measured ordering against an arming sword at light armour, not by taste." "A kind joins `arms_kinds` only with its row of the roster census named in the commit (`U5b_PC_residue.md` §3): no cell beyond 95% against the kinds already admitted, or its answering kind admitted with it … the census is re-run after that batch and decides." So: each kind is admitted in census order with its row quoted in this commit's body; a kind that fails alone and has no answering kind is not admitted, and the PR body lists it for Jordan. The counts of `arms_at_build` are `[ASSUMPTION; low]`, listed in the PR body.
- WHERE: `engine/season/rosters.yaml` (`matter_kinds`, `arms_kinds`, `arms_at_build`).
- TESTS (copied): "`engine/season/tests/test_cp_t03_04_arms.py::test_an_arms_kind_outside_rung_kinds_is_refused_at_import`, `::test_an_arms_kind_key_outside_the_weapons_export_is_refused_at_import`", red first if absent.
- FALSIFIER and CONTROL: "A realm in which every fight is still pool 8 against obstacle 1.0 after the content lands" (pool and obstacle as B05 and B15 left them, re-read by command). Control (Gate 4): "With `arms_kinds` emptied and the templates reverted, the pre-change season hashes return."
- GATE: `python -m pytest engine/season/tests/test_cp_t03_04_arms.py engine/season/tests/test_cp_t03_03_kit.py -q` → pass; the realm reading of distinct kit tuples per seed 0–2 above 1, quoted; each admitted kind's worst census cell quoted.
- HASH MOVERS: "Parts B/D every season fight between persons whose inputs differ". Declared; B18.99.
- DEPENDS ON: V12 B18.01 (the census table), B18.03; EXISTS-IN-TREE `rosters.yaml: arms_kinds`, `arms_at_build`, `matter_kinds`, `data/rosters.py::_check_arms_at_build`; V12 Batch B12c (B12c.25 adds `arms` to `matter_kinds` in the same step: a different member).
- GLOSSARY: none.
- COST and TIER: content (an edit); `sonnet`, `high`; the census reading `opus`.
- LANDS IT: B18's producer; `Item: B18.04`, `[skip ci]`.

### B18.05 — the martial lifepaths hold `arms` · `03_PC_person_inputs_content` Part D · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/03_PC_person_inputs_content.md` Part D; UNDECIDED (3).
- ADVANCES: R-06 (a key `train` and build-by-doing can raise).
- INSTRUCTION (copied): "`rosters.yaml: lifepath_templates`: the martial lifepaths hold `arms` (the template already says which `verb_capability` values a lifepath's starting skills draw on; `arms` was added to `verb_capability` at CP-T03-04 and no template names it). Held at `pool_default`, so no pool moves at creation; it makes `arms` a key that `train` and build-by-doing can raise." "Authored attributes for realm persons are CHAR's … Tradition and disposition: no carrier is proposed here." Which lifepaths are martial is read off each template's `ground:` line (the archived source's `Starting Skills (★)` column) and listed with each line in the commit body `[ASSUMPTION; low; Jordan to correct]`.
- WHERE: `engine/season/rosters.yaml` (`lifepath_templates`).
- TESTS: `engine/season/tests/test_cr33_lifepaths.py` (existing) re-run; `[ASSUMPTION: test name]` `::test_a_martial_lifepath_holds_arms_at_pool_default` added, red first.
- FALSIFIER and CONTROL: a martial person holding no `arms` key after creation; a pool moved at creation. Control: Gate 4 (templates reverted → pre-change hashes).
- GATE: `python -m pytest engine/season/tests/test_cr33_lifepaths.py -q` → pass; the seed-2 one-season hash recorded.
- HASH MOVERS: as B18.04 ("Parts B/D"). B18.99.
- DEPENDS ON: V12 B18.04 (the order); V12 Batch B04 (the `capabilities:` row `arms`; `lifepath_templates`' second key re-pointed when CAP A3 deleted `verb_capability`); EXISTS-IN-TREE `rosters.yaml: lifepath_templates`, `data/rosters.py::_load_lifepath_templates`, `loop/effects_combat.py::_eff_train`.
- GLOSSARY: none.
- NAMES: `verb_capability`'s values → the `capabilities:` rows (`descriptors.CAPABILITIES`) (B04, CAP A3).
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B18's producer; `Item: B18.05`, `[skip ci]`.

### B18.06 — one carry rule at the kit's owner · `03_PC_loadout_and_carry` item 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/03_PC_loadout_and_carry.md` "The resolution, decided" 2, "Implementation" order (1); D-U1-11d ("the carry rule is one pure function in `engine/substrate/combat_kit.py`"); its head (3) ("the leaf takes masses").
- ADVANCES: none by itself.
- INSTRUCTION (copied): "**Carried mass is the quantity, Strength demand is the unit.** The leaf `engine/substrate/combat_kit.py` itself (the kit data's owner, D-U1-11d), reading the typed export and nothing else, owns one function:"
  ```python
  def carry_demand_of(masses: tuple, armour: str) -> float:      # (Reconciled) the ONE body
      """Strength points demanded by what is CARRIED: D_MASS per kilogram of every carried mass that is
      not in hand, plus the harness's ARMOR_DEMAND. Reads the export's `cfg`."""

  def carry_demand(weapons: tuple, armour: str) -> float:
      """The keyed spelling: looks each weapon's mass up in the export's `weapons` section and calls
      `carry_demand_of`. A person's kit uses this; a troop row, whose arm may have no key here, uses the
      mass form. One rule, two spellings of its argument."""
  ```
  "The export's `kit` section gains each weapon's `mass` (already a field of every record). No new constant: `D_MASS` and `ARMOR_DEMAND` exist and are exported." The `mass` in the `kit` section is landed by `03_PC_weapon_records_in_the_export` (B14); if it is absent at the open, this item adds it in `tools/export_engine_params.py::_kit_section` and re-derives the export.
- WHERE: `engine/substrate/combat_kit.py` (`carry_demand_of`, `carry_demand`); `tools/export_engine_params.py` (`_kit_section`, only if `mass` is absent); `engine/engine_params/combat_engine_v1.json` (re-derived if so).
- TESTS (copied): "`tests/valoria/test_combat_units_refactor.py::test_carry_demand_of_equals_the_keyed_spelling`", red first.
- FALSIFIER and CONTROL: "a second `carry_demand` in either module" (`git grep -n "def carry_demand" modules engine` → only `combat_kit.py`). Control: nothing calls it yet; the season hash equal.
- GATE: `python -m pytest tests/valoria/test_combat_units_refactor.py -q` → pass; `python tools/export_engine_params.py --check` → exit 0; the grep above.
- HASH MOVERS: none.
- DEPENDS ON: V12 B18.05 (the Lands line: "after `03_PC_person_inputs_content.md` Parts B–D"); V12 Batch B14 (`mass` in the export, `_kit_section`); EXISTS-IN-TREE `modules/combat/config.py` (`D_MASS`, `ARMOR_DEMAND`), `engine/substrate/combat_kit.py`.
- GLOSSARY: *loadout* (new row, if absent): "a kit with a secondary weapon: what a fighter carries, of which one weapon is in hand".
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B18's producer; `Item: B18.06`, `[skip ci]`.

### B18.07 — the shortfall rides the input; the harness term moves; the close slows · `03_PC_loadout_and_carry` items 2, 3 · BUILD · HASH EQUAL
- SOURCE: `proposals/03_PC_loadout_and_carry.md` "The resolution, decided" 3, "Implementation" order (2), (3), "Gate" 1; D-U1-11d; UNDECIDED (4).
- ADVANCES: none at the control (`CARRY_CLOSE_K` 0, no secondary).
- INSTRUCTION (copied): "**The penalty is the form the engine already uses,** `short = max(0, carry_demand − strength)`: fatigue as `ACT_WEIGHT / D_WT × short` stamina per action, added in `act_cost` where the harness term sits now (the harness term moves into `carry_demand`, same value); movement as a factor on `close_rate`, `1 / (1 + CARRY_CLOSE_K × short)`, one new `[SIM-CALIBRATE]` coefficient in `CFG`, 0 as the control. A fighter at or over the demand pays nothing, as now. … the host (`seam/wrappers/combat.py::combat_input`) evaluates `carry_demand` and hands each party's `short` raw on `PersonalCombatInput` (one value per kit he may have in hand: with the primary, with the secondary); `combat_systems.act_cost` and `close_rate` read it from the Combatant the module builds from its input. `modules/combat/` imports nothing from `engine/substrate/` for this." Order: "(2) `PersonalCombatInput` gains the per-party `short` pair; `seam/wrappers/combat.py::combat_input` fills it; (3) `combat_systems.act_cost` takes the harness term from the input and adds the carry term; `close_rate` gains `CARRY_CLOSE_K` (in `CFG`, exported, 0 shipped)." The workbench's record builder (B14.11) fills `short` the same way through `carry_demand`, so workbench and season stay one door.
- WHERE: `engine/season/queries/inputs.py` (`PersonalCombatInput`: the `short` pair, defaulting to the relocated harness value); `engine/season/seam/wrappers/combat.py` (`combat_input`); `modules/combat/fight.py` (passes it to `Combatant`); `modules/combat/combatant.py` (the field); `modules/combat/combat_systems.py` (`act_cost`, `close_rate`); `modules/combat/config.py` (`CFG['CARRY_CLOSE_K'] = 0`); `tools/export_engine_params.py` and `engine/engine_params/combat_engine_v1.json` (the coefficient exported, re-derived); `systems/combat/combat_engine_v1/workbench/balance.py` (the record builder fills `short`).
- TESTS: `[ASSUMPTION: test name]` `tests/valoria/test_combat_units_refactor.py::test_the_relocated_harness_term_charges_the_same_stamina` (one fight per tier, events equal before and after), red first; the workbench reading of Gate 2 with `CARRY_CLOSE_K` set in a `cfg` overlay (B14.11's `fight(..., cfg=...)`), 1,000 fights per cell, quoted in the commit body (a one-time reading, `R1_READ.md` 7b-20).
- FALSIFIER and CONTROL: "A carried secondary that costs nothing at any Strength" (read in the overlay arm). Control: "Hash EQUAL with every secondary absent (the harness term relocated, same value): season pins and the combat goldens unchanged."
- GATE: `python -m pytest tests/valoria/test_combat_units_refactor.py tests/valoria/test_combat_invariants.py -q` → pass; `python tools/export_engine_params.py --check` → exit 0; `python tools/ci_golden_modes_check.py` → equal; the season hash at seed 2, one season → equal to B18.06's.
- HASH MOVERS: none (`PersonalCombatInput` is not a `World` carrier, B14.11's reading).
- DEPENDS ON: V12 B18.06; V12 Batch B14 (B14.11's `cfg` overlay and one door); EXISTS-IN-TREE `combat_systems.py::act_cost`, `::close_rate` (callers in `wrapper.py`), `config.py::CFG`, `ACT_WEIGHT`, `D_WT`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`; the workbench reading `haiku`, read by `opus`.
- LANDS IT: B18's producer; `Item: B18.07`, `[skip ci]`.

### B18.08 — a kit has a secondary · `03_PC_loadout_and_carry` item 4 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/03_PC_loadout_and_carry.md` "The resolution, decided" 1, "Implementation" order (4), tests.
- ADVANCES: R-06 (a loadout is a choice: reach and a fallback against weight).
- INSTRUCTION (copied): "**A loadout is a kit with a secondary.** `kits` becomes `(primary, secondary, armor)` per party, `secondary` defaulting to none; `kit_of` returns the two highest-ranked weapon kinds the person's rungs stock instead of one. `rosters.yaml: arms_kinds` needs no new column." Every caller of `kit_of` in `seam/wrappers/combat.py` takes the triple (grep at the open, list in the commit).
- WHERE: `engine/season/queries/world_q.py` (`kit_of`); `engine/season/queries/inputs.py` (`PersonalCombatInput.kits`' shape); `engine/season/seam/wrappers/combat.py` (`kit_of`'s callers); `modules/combat/fight.py` (the triple into `Combatant`).
- TESTS (copied): "`engine/season/tests/test_cp_t03_03_kit.py::test_kit_of_returns_a_secondary_when_two_kinds_are_stocked`", red first.
- FALSIFIER and CONTROL: a person whose rungs stock two weapon kinds fighting with one in his kit. Control: a person stocking one weapon kind reads `secondary` none and fights as at B18.07.
- GATE: `python -m pytest engine/season/tests/test_cp_t03_03_kit.py -q` → pass; the seed-2 one-season hash recorded (moved only where a person's rungs stock two weapon kinds after B18.04).
- HASH MOVERS: "persons with a secondary". Declared; B18.99.
- DEPENDS ON: V12 B18.07; EXISTS-IN-TREE `world_q.py::kit_of`, `seam/wrappers/combat.py::combat_input`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B18's producer; `Item: B18.08`, `[skip ci]`.

### B18.09 — the weapon in hand is round state; a switch costs tempo · `03_PC_loadout_and_carry` item 5 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/03_PC_loadout_and_carry.md` "The resolution, decided" 5, "Implementation" order (5) ("`switch` in the consult's choice set (after PB step 4)"), "Gate" 3, tests; its head (2) and the A-101 line ("a switch spends the fighter's next action inside a round").
- ADVANCES: R-06, R-09 (a fight between unlike loadouts turns on a choice).
- INSTRUCTION (copied): "**The weapon in hand is round state, and changing it costs the round's tempo.** `DuelState.form` (PB §2) **is** this field: the key of the record in hand, whether a half-sword form of the primary or the secondary; no second field is added. The choice set a decider may answer at a phase entry gains `switch` beside the approaches (and `withdraw` at the top of a round): the fighter spends his next action's readiness (`ACT_THRESHOLD`, the unit the engine already debits) and fights the rest of the round with the other weapon; the secondary's mass leaves `carry_demand` and the primary's enters. An NPC's or a standing order's trigger for it reads what the engine already computes: how badly the weapon in hand serves the present measure (`close_unwieldiness`). The half-sword form change stays as it is; it is a grip, not a second weapon." The choice set is B16's (PB step 4's per-phase consult, `ROUND_CHOICES` after PCR-3).
- WHERE: `modules/combat/vocabulary.py` or the module holding `ROUND_CHOICES` (`switch`; SITE: grep at the open); `modules/combat/wrapper.py` (the consult: a `switch` debits `ACT_THRESHOLD` and swaps `DuelState.form`); `modules/combat/combat_systems.py` (`close_unwieldiness` read by the default decider's trigger); the `short` of the other in-hand state read from the input (B18.07).
- TESTS (copied): "`tests/valoria/test_combat_units_refactor.py::test_a_switch_debits_one_act_threshold`", red first; Gate 3 as a workbench reading in the commit body: "A spear-and-sword fighter closed on by a dagger switches (count reported) and his felled share is below the spear-only fighter's in that matchup and not below it at open measure."
- FALSIFIER and CONTROL: "a switch that takes no tempo". Control: a fighter with no secondary never forms `switch`; the combat goldens (single-weapon) equal.
- GATE: `python -m pytest tests/valoria/test_combat_units_refactor.py tests/valoria/test_combat_invariants.py -q` → pass; `python tools/export_engine_params.py --check` → exit 0 (if the choice set is exported); the Gate 3 reading quoted.
- HASH MOVERS: "persons with a secondary". Declared; B18.99.
- DEPENDS ON: V12 B18.08; V12 Batch B16 (`03_PC_duel_round_and_approach_B` steps 1–4: `DuelState.form`, the per-phase consult; PCR-3's `ROUND_CHOICES`); EXISTS-IN-TREE `combat_systems.py::close_unwieldiness`, `wrapper.py` (`ACT_THRESHOLD`'s debit).
- GLOSSARY: *switch* (new row): "changing the weapon in hand during a round, paid for with the fighter's next action".
- NAMES: `TURN_CHOICES` → `ROUND_CHOICES` (B16, PCR-3).
- COST and TIER: small build; `sonnet`, `high`; the workbench reading `haiku`, read by `opus`.
- LANDS IT: B18's producer; `Item: B18.09`, `[skip ci]`.

### B18.99 — re-pin and close readings · `_part4` E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12.
- INSTRUCTION: (1) Re-record, once, the realm pins in `engine/season/tests/_realm_goldens.py` and every seeded result B18.04, .05, .08, .09 moved, against B17's close rebased on B12c's merge (`reading @<sha>`); the commit says "re-pin" and lists them. (2) Seeds 0–2 for every item read at seed 2 only (E-2). (3) The close's readings (BATCH GATE), with the Part A–D gates 1, 2 and 4 and the loadout gates 1–3 quoted. (4) Part B's admitted and refused kinds and the census rows behind each, listed in the PR body for Jordan (D-19).
- WHERE: the pin files above.
- TESTS: the covering suites and the full suite once (CLAUDE.md §0.4).
- FALSIFIER and CONTROL: a pin moved by no declared item. Control: B18.01–.03, .06, .07 reproduce.
- GATE: the BATCH GATE.
- HASH MOVERS: the re-pin.
- DEPENDS ON: V12 B18.01 to B18.09.
- COST and TIER: `sonnet`, `high`; terminal critique `opus`.
- LANDS IT: B18's producer; `Item: B18.99`, without `[skip ci]`.

| STOP. Batch B18-pc-content closes here |

Last item written in this file: B18.99.
