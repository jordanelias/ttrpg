# Workplan v12 — batches B22-mb-armies and B26-fi-inquiry

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; ratified only when Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05)

## Written against: working tree HEAD `8ce8d6a` (2026-11-12). Producer: author lane A33. Form: `master/workplan_v12/V12_STRUCTURE_part2.md` §5–§6. Decisions cited `D-nn` are the structure's §1.

**What this part holds.** Two batches, in §2.1's order: `B22-mb-armies` (MB) and `B26-fi-inquiry` (FI). Both open at step S17 and share no gate. Each is one block with one close; its items land as one commit each, in the order of its position table. A source cited as `proposals/<file>` is under `proposals/2026-11-12-subsystem-audit-suite/proposals/`; `IS-MB-*` is `master/instructions/IS_B1_PC_MB_DICE_part2.md`; `IS-A-*` is `master/instructions/IS_A_NINE_part2.md`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `the intake` is `master/eval/V12_INTAKE.md`.

**Words.** `unified/U1_GLOSSARY.md`. A person's numbers: attribute, skill, skill score, martial skill, derived score (A-98); the tree's `capability` identifiers keep their names and prose says *skill*. Armies: army, unit, army formation, unit formation (A-99, the MB lexicon); no size words. A *lap* is one pass of the season's scene budget; a *round* is one engagement of a fight (A-101). Where copied source text said "round" for the season's pass, it is corrected to "lap" and the correction is said at the item.

---

## Batch B22-mb-armies · lane MB · wave W17 · step S17 · HASH MOVER, one re-pin

INVOCATION: /methodology-execute Batch B22-mb-armies
IN-FLIGHT ROW: registers/handoffs/HANDOFF_MB.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B16L-mb-words
GATE: Batch B04-capability-home
GATE: Batch B05-one-roll
GATE: Batch B07-task-draw
GATE: Batch B10-character
GATE: Batch B12c-material-verbs-and-valley
GATE: Batch B17-mb-scale
GATE: Batch B19-mb-field-calibration
GATE: Batch B20-mb-orders
GATE: Batch B21-fa-governance
GATE: Batch B21b-fa-war
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading").
REQUIREMENT: R-04.c1 (`train`); `BUILT OUT`: `train`, `recruit`, `discharge_troops`, `form_unit`, `assign_troops`, `disband_unit`, `order_unit`, `raze`, and `march` with posture `besiege` (`IS-MB-02`, read through `IS-A-09`); `ENGINES`: `mass_battle.army` and `mass_battle.army_order` → each built out; both `ENGINES` rows above 0 (IS-A §12.2 row B22). Milestones: M3 (every verb), M4 (every scale).
BATCH GATE (read once, on the closing tree; every seeded command under `PYTHONHASHSEED=0`; two seasons at most, A-114):
  1. `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `python -m engine.season.harness.register --requirements` → nine lines, recorded.
  2. `python tools/m1_acceptance.py --summary` → its verdict line, recorded.
  3. the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names → green; `-m mass_battle` first where it names only that subsystem.
  4. `python -m engine.season.harness.aperture 2 --seeds 0 1 2` → the `BUILT OUT` line reads built out for `train`, `recruit`, `discharge_troops`, `form_unit`, `assign_troops`, `disband_unit`, `order_unit`, `raze`, and for `march` with posture `besiege` formed and executed (IS-A-08, IS-A-09 (1)); `field.invested` in `EMITTED KINDS` (IS-A-09 (1)); the `ENGINES` rows `mass_battle.army` and `mass_battle.army_order` above 0. A verb not built out is a failed gate (IS-A-08).
  5. B22.R1 (IS-MB-05): `python -m engine.season.harness.aperture 2 s`, s = 0, 1, 2 → `field.won + field.lost + field.drawn` above 0 at every seed; the `ENGINES` lines for `mass_battle.resolve_field`, `mass_battle.army`, `mass_battle.army_order` above 0; `attempted` and `executed` for `march`, `marshal`, `recruit`, `form_unit`, `assign_troops`, `order_unit` quoted; the counts of `field.won`, `field.lost`, `field.drawn`, `field.unopposed`, `siege.pressed` quoted.
  6. B22.R2 (`17_CENSUS_C1A_02` W2, the rows of this batch): `python -m engine.season.harness.corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's] → `recruit`, `form_unit`, `assign_troops`, `disband_unit`, `discharge_troops`, `order_unit` and `march` appear under `VERBS THAT EXECUTED`; the line `<n> of <N> executed` quoted before (`reading @<sha>`) and after.
  7. `04_MB_playable_field_scenario` gate 4 and gate 7 on the closing tree: `aperture 2 s`, s = 0 to 2 → `army.recruited`, `army.formed`, `army.assigned`, `order.marshaled` out of the never-emitted list; `python -m pytest engine/season/tests/test_field_scene.py::test_no_field_band_without_a_durable_write -q` → pass (the count of folded field bands whose Event carries zero durable writes is 0 over gate 4's fields).
  8. `python tools/export_troops.py --check` → exit 0 (the `fatigue`, `aftermath` and `doctrines` sections of B22.03, B22.04 and B22.32 round-trip); `python tools/ci_golden_modes_check.py` → every digest equal to B20's close (`reading @<sha>`), none of this batch's items touching the field resolver's arithmetic.
  9. `IS-MB-02`'s table, read by `opus` at the close (B22.11's commit body): over `field_scene` seeds 0–39, the `win` share and the seasons taken under `storm` and under `besiege_then_storm`, each with its disjoint-seed control.
  10. The close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`, B21b's or B20's close, whichever merged last) and after, and the batch's measured wall time; the last `Item:` commit writes the conjuncts' `reading:` records; `status:` is not edited (`IS-A-12`).
RE-PIN: every seeded realm, spine and corpus pin, the field goldens a moved field reaches, and `engine/season/tests/test_in12_raze.py`'s H-228 pin, re-recorded once in B22.99 (the batch's last `Item:` commit; moved from B22.35 by repair lane R1, E-1), said plainly as a re-pin; the before-reading is the previous close's after-reading (`reading @<sha>`).
EXPECTED RED UNTIL B22.99 (under `[skip ci]`, E-1; one batch line, repair lane R1): the realm and corpus pins any mover item of this batch moves read red from its first mover (B22.04) to the re-pin; the files that pin them (`git grep -lE '"[0-9a-f]{32}"'` over the test trees and the golden files, those this batch names): `engine/season/tests/_realm_goldens.py` (B02's one pin file); `engine/season/tests/test_go07_canonical_digest.py` (its asserting test, `SHIPPED`/`CENSUS`); `tools/ci_golden_modes_check.py`.
IDS: ED-MB 0; H 2 (the NUMBER rows of B22.22 `leaderless_dispersal` and B22.31 `raze_sack_share`)
DIALS AT CONTROL:
  - `references/troops.yaml: aftermath.recuperation` = `off` (with `aftermath.return: unprompted`, `aftermath.acting: on`, every share table and `window` absent; the loader refuses `on` while any is absent); set by: none in v12 — the values are not established (`IS-MB-B3`: Jordan, or a source search filed under `research/historical/`); target: `27_MB_E` §5 rows T-11 to T-16b, T-18 (orderings, no figure).
  - `references/troops.yaml: fatigue.carry` = `off`, `fatigue.carry_laps` = 0; set by: none stated in the source (control 0, "no reasoned value"); target: `27_MB_E` §5 row T-17.
  - `data/fixtures.py: standing_ration` = `False`; set by: none stated (the source: "each flip a declared mover in its own commit", no batch named); target: none stated.
  - `data/fixtures.py: leaderless_dispersal` = 0 (no dispersal) `[ASSUMPTION: 0 as the control — basis: 14_VERBS_MILITARY_C Edit 6 gives no figure, names it "swept; NUMBER row"]`; set by: B98; target: B22.22's dispersal gate (more than two values across seeds; full strength at some seed and below at another).
  - every obstacle term and leverage level of `14_VERBS_MILITARY_A`–`_D` and `14_VERBS_PHYSICAL_B` that the sources ship absent (0) until U1 names it (listed at B22.01); set by: B98, after B22.01's design names each; target: none stated.
  - `rosters.yaml: march_postures.values` = `[storm]`; set by this batch (B22.12), conditionally on its gate table.
  - `data/fixtures.py: armies_at_build` = `"off"`; set by this batch (B22.33).
C(B22-mb-armies): this batch's entries; the plan's head parts; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_MB.md`, `.claude/skills/methodology-execute/SKILL.md`, `methodology-close`);
  edited: `modules/mass_battle/armyrecord.py`, `modules/mass_battle/massbattle.py`, `modules/mass_battle/orderofbattle.py`, `modules/mass_battle/config.py`, `modules/mass_battle/troop_types/presets.py`,
  `engine/season/queries/inputs.py`, `engine/season/queries/world_q.py`, `engine/season/seam/wrappers/mass_battle.py`, `engine/season/seam/wrappers/sigma.py`, `engine/season/loop/effects_combat.py`,
  `engine/season/loop/effects_army.py`, `engine/season/loop/effects_migration.py`, `engine/season/loop/effects_information.py`, `engine/season/loop/effects_founding.py`, `engine/season/loop/effects_shared.py`,
  `engine/season/loop/matter.py`, `engine/season/loop/sides.py`, `engine/season/decision/options.py`, `engine/season/data/requires.py`, `engine/season/data/verbs.py`, `engine/season/data/fixtures.py`,
  `engine/season/rosters.yaml`, `engine/season/verb_table.yaml`, `engine/season/write_matrix.yaml`, `engine/season/boot/realm.py`, `engine/season/harness/army_presets.py`, `engine/season/harness/field_scene.py`,
  `references/troops.yaml`, `references/module_contracts.yaml`, `references/descriptor_registry.yaml`, `engine/season/hole_register.yaml`, `unified/U1_GLOSSARY.md`;
  tests: `tests/valoria/test_mass_battle_army_record.py`, `tests/valoria/test_army_battle.py`, `tests/valoria/test_army_verbs.py`, `tests/valoria/test_army_menu_presets.py`, `tests/valoria/test_mass_battle_order_of_battle.py`,
  `engine/season/tests/test_march.py`, `engine/season/tests/test_cr_24_winner_casualties.py`, `engine/season/tests/test_in12_raze.py`, `engine/season/tests/test_rem32_scale.py`, `engine/season/tests/test_cp_t04_02_marshal.py`, `engine/season/tests/test_field_scene.py`,
  NEW `engine/season/tests/test_vm_mil_a_movement.py`, `test_vm_mil_b_train.py`, `test_vm_mil_c_muster.py`, `test_vm_mil_d_order_of_battle.py`, `test_vm_phy_b_field_ruin.py`, `test_v14_march_on_a_field.py`, `test_v14_raze_after_occupation.py`, `test_standing_ration.py`, `test_resv_field_defender.py`;
  read only: `engine/season/state/gate.py` (`may_levy`, `may_wage`, B21), `engine/season/loop/effects_economy.py` (`_fall`), `engine/season/loop/resolve.py`, `engine/season/loop/witness.py`, `engine/dice_engine/dice_engine.py` (`Degree`), `engine/dice_engine/sigma_leverage.py` (`pool_of`),
  `engine/season/harness/aperture.py`, `engine/season/harness/corpus_run.py`, `engine/season/harness/military_menu.py`, `tools/export_troops.py`, `tools/ci_golden_modes_check.py`, `engine/engine_params/troops.json`;
  the closing SHAs of B00, B01, B02, B16L, B04, B05, B07, B10, B12c, B17, B19, B20, B21, B21b.
  Read whole (an item says so): `proposals/27_MB_E_what_an_army_carries_back.md` §5 (the calibration rows the DIALS line cites); `audits/14_VERBS_PHYSICAL.md` §5.7 and §6.7 are copied into B22.29 and B22.31, not read.
SERIAL EDGES:
  within the batch: B22.02 → B22.03 → B22.04 → B22.05 (`27_MB_E`'s edit order: the row and its ops, the carried stamina, the write by kind, the read and its write-through);
  B22.06 → B22.07 → B22.08 → B22.09 (`14_VERBS_MILITARY_A` §3's order); B22.08 → B22.11 (`IS-MB-02` depends on `14_VERBS_MILITARY_A` edits 1–5) → B22.12 (its step 2 after its step 6's policy, whose table decides whether step 2's commit is made);
  B22.09 → B22.13 (`train` after `14_VERBS_MILITARY_A` Edit 6, the `with` deposit); B22.14 → B22.16 (`(d)` reads `away`) and B22.14 → B22.18 (the muster after the supply file, U3 §1.2 row B22 item 6); B22.02 → B22.18, B22.05 → B22.22 (`cohort_claims` and the strength read count absent men);
  B22.17 → B22.18 → B22.19 → B22.20 → B22.21 → B22.22 → B22.23 (`14_VERBS_MILITARY_C` §3's landing order) → B22.24 → B22.25 → B22.26 → B22.27 (`14_VERBS_MILITARY_D` after C, reusing `army_state`, the class, the keys, `present_strength`);
  B22.28 → B22.29 → B22.30 → B22.31 (`14_VERBS_PHYSICAL_B`'s order of landing: the move of `occupying_faction`, then B1, then B2's class, then its grading);
  B22.23 → B22.32 → B22.33 → B22.34 (the fixture, then `04_MB_playable_field_scenario` §E's arm and data, then its two flips, each its own commit); B22.35 last (U3 order) and carrying the re-pin.
  with other batches: `engine/season/rosters.yaml`, `engine/season/verb_table.yaml`, `engine/season/queries/world_q.py`, `engine/season/data/fixtures.py`, `engine/season/loop/effects_information.py`, `engine/season/data/verbs.py`, `engine/season/seam/wrappers/sigma.py`, `engine/season/decision/options.py`: hot files (U3 §5.1), B21 → B22 → B23 and B21b → B22; `modules/mass_battle/armyrecord.py`, `orderofbattle.py`: B19 → B20 → B22 → B31; `engine/season/loop/effects_army.py`: B20 → B21 → B22; `engine/season/data/requires.py`: B21 → B22 → B33; `engine/season/loop/effects_founding.py`: B12c → B22 → B39; `engine/season/loop/effects_migration.py`: B12c → B22; `engine/season/harness/field_scene.py`: B20 (IS-MB-01) → B22 (IS-MB-02 step 6) → B30 (IS-MB-04); `engine/season/loop/matter.py`: B12c → B22 → B27.
PARALLEL: S17 with B11F2 (IN), B26 (FI), B28 (SC), B32 (FA), B37p (WR). Shared hot files, each to be edited in different top-level keys or functions (§7.3 of the structure; the coordinator checks the census at the step's open): with B26 `rosters.yaml`, `verb_table.yaml`, `world_q.py`, `fixtures.py`, `effects_information.py`, `data/verbs.py`, `sigma.py`, `options.py`; with B28 `rosters.yaml`, `verb_table.yaml`, `world_q.py`, `fixtures.py`, `effects_information.py`, `options.py`, `sigma.py`, `data/verbs.py`, `matter.py` (U3 §5.1 rows naming both); with B32 `rosters.yaml`, `verb_table.yaml`, `world_q.py`, `fixtures.py`, `effects_information.py`, `data/verbs.py`, `sigma.py`, `matter.py`. Merge order in the step (§7.4): after B11F2, before B26, B28, B32, B37p; B22 rebases on B11F2's merge and re-pins once.
COST: build (eleven proposals and one instruction item, mostly small builds behind shipped-off arms; two flips and four formation movers); producer `sonnet`, effort high; judgment nodes `opus`: B22.01 (the design), B22.04's read-and-write move (the double count), B22.11's table (it decides B22.12), B22.22's strength read, B22.26's field gate (the `raw` step's size), B22.30–B22.31 (the contested `raze` row and its gates); the readings of B22.R1 to B22.R3 `haiku` (`valoria-measure`).
EST: 6 h [estimate: the structure's §2.4 formula; nothing timed]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B22.01 | which military and physical obstacle terms join the obstacle roster, and which levels join the leverage roster | `U5b_VERBS_military_physical_residue` §1 rule 3; `IS-MB-B1` | DESIGN-FIRST | EQUAL | Batch B05, Batch B07 |
| B22.02 | the unit row holds what the army lost, by kind | `27_MB_E` 27E-1 | BUILD | EQUAL | Batch B17, Batch B16L |
| B22.03 | the battle returns the stamina each unit ended with; a second battle in a lap starts from it | `27_MB_E` 27E-2 | BUILD | EQUAL | B22.02; Batch B19 |
| B22.04 | a battle's losses are written on the unit row by kind, and counted once | `27_MB_E` 27E-3 | BUILD | EQUAL (MOVER(behaviour) under `recuperation: on`) | B22.03 |
| B22.05 | the strength a reader sees adds the men who came back, by a draw; an act writes them | `27_MB_E` 27E-4 | BUILD | EQUAL (MOVER(behaviour) under `recuperation: on`) | B22.04 |
| B22.06 | `move` forms only on places | `14_VERBS_MILITARY_A` Edits 1 (class), 2 | BUILD | MOVER(behaviour) | Batch B07, Batch B12c |
| B22.07 | the journey's Event says where the mover went | `14_VERBS_MILITARY_A` Edit 3 | BUILD | MOVER(behaviour) | B22.06 |
| B22.08 | a journey is one draw, written by band | `14_VERBS_MILITARY_A` Edits 1 (bands), 4, 5 | BUILD | MOVER(behaviour) | B22.07; Batch B05, Batch B07 |
| B22.09 | a refusal on `with` teaches the actor | `14_VERBS_MILITARY_A` Edit 6 | BUILD | MOVER(behaviour) | B22.08 |
| B22.10 | — (pointer row: `IS-A-09`'s instruction is withdrawn; its readings are B22.R3) | `IS-A-09` | POINTER | — | — |
| B22.11 | a siege that wears nothing still writes; the scenario offers besiege then storm | `IS-MB-02` steps 1, 3, 4, 5, 6 (the policy) | BUILD | EQUAL | B22.08; Batch B12c, Batch B20 |
| B22.12 | `besiege` joins the march's postures | `IS-MB-02` step 2, step 6 (the override's deletion) | BUILD | MOVER(behaviour) | B22.11 and its table |
| B22.13 | `train` is a lesson that may or may not take | `14_VERBS_MILITARY_B` Edits 1–4 | BUILD | MOVER(behaviour) | B22.09; Batch B04, Batch B05, Batch B07 |
| B22.14 | the army module answers how many men each cohort has under arms; who is away | `07_SE_campaign_supply_and_muster` (a), (b) | BUILD | EQUAL | B22.05 |
| B22.15 | a soldier is not a farmer while he is a soldier | `07_SE_campaign_supply_and_muster` (c) | BUILD | EQUAL | B22.14; CP-T08-01's item (Batch B12c) |
| B22.16 | an army away from home eats from its holder's treasury | `07_SE_campaign_supply_and_muster` (d), (e), (g) | BUILD | EQUAL | B22.14 |
| B22.17 | a fortress trains foot; training Sites stand where the realm's venues name them | `07_SE_campaign_supply_and_muster` (f) with `U5b_MB_residue` §3 | BUILD | EQUAL | B22.16; `07_SE_ground_and_granaries` (Batch B12c) |
| B22.18 | the army record carries a doctrine and a footing, and steps toward them | `14_VERBS_MILITARY_C` Edit 1 | BUILD | EQUAL | B22.02, B22.17 |
| B22.19 | one reader of an army's state as its commander may command it | `14_VERBS_MILITARY_C` Edit 2 | BUILD | EQUAL | B22.18; Batch B21 |
| B22.20 | a held Record forms only the rows that ask for its kind | `14_VERBS_MILITARY_C` Edit 3 | BUILD | MOVER(behaviour) | B22.19 |
| B22.21 | `recruit` and `discharge_troops` are task rows on `command` | `14_VERBS_MILITARY_C` Edits 4, 5 | BUILD | EQUAL | B22.20 |
| B22.22 | the roll outlives its holder; a leaderless army thins when read | `14_VERBS_MILITARY_C` Edit 6 | BUILD | EQUAL | B22.21, B22.05 |
| B22.23 | the fixture for armies at build; the levy verbs leave the withheld list | `14_VERBS_MILITARY_C` Edit 7 | BUILD | EQUAL | B22.22 |
| B22.24 | the unit row gains `raw`; the module steps the four organising ops by band | `14_VERBS_MILITARY_D` Edit 1 | BUILD | EQUAL | B22.23 |
| B22.25 | four stems answered by the army's state | `14_VERBS_MILITARY_D` Edit 2 | BUILD | EQUAL | B22.24 |
| B22.26 | `form_unit`, `assign_troops`, `disband_unit`, `order_unit` are task rows on `command` | `14_VERBS_MILITARY_D` Edits 3, 4, 5 | BUILD | EQUAL | B22.25 |
| B22.27 | the four leave the withheld list; the preset arm says what it draws | `14_VERBS_MILITARY_D` Edits 6, 7 | BUILD | EQUAL | B22.26 |
| B22.28 | `occupying_faction` moves to its query owner | `14_VERBS_PHYSICAL_B` B2 (first row) | BUILD | EQUAL | B22.27 |
| B22.29 | `march` forms only on a `Field`; one owner says who defends | `14_VERBS_PHYSICAL_B` B1 | BUILD | MOVER(behaviour) | B22.28; Batch B21, Batch B21b |
| B22.30 | `raze` forms only on a town its seat may ruin | `14_VERBS_PHYSICAL_B` B2 (the class) | BUILD | MOVER(behaviour) | B22.29 |
| B22.31 | `raze` is one draw over four bands | `14_VERBS_PHYSICAL_B` B2 (the grading) | BUILD | MOVER(behaviour) | B22.30 |
| B22.32 | armies at build, doctrines as data, `marshal` fans its fall-back point only | `04_MB_playable_field_scenario` §E | BUILD | EQUAL | B22.27, B22.23 |
| B22.33 | armies are mustered at realm build | `04_MB_playable_field_scenario` §E (the `armies_at_build` flip) | BUILD | MOVER(behaviour) | B22.32 |
| B22.34 | `marshal` and `surrender` leave the withheld list | `04_MB_playable_field_scenario` §E (the `withheld_verbs` flip) | BUILD | MOVER(behaviour) | B22.33 |
| B22.35 | a detained man musters nowhere; the batch's one re-pin | `U5b_VERBS_military_physical_residue` §4 | BUILD | MOVER(behaviour) | B22.34 |
| B22.R1 | the integrated reading of mass battle | `IS-MB-05` | READING | — | B22.35 |
| B22.R2 | the census rows `_army`, `_payload`, `_siege` close | `17_CENSUS_C1A_02` W2 | READING | — | B22.35 |
| B22.R3 | `march` with `besiege` read through `BUILT OUT`; `field.invested` emitted | `IS-A-09` (1), (2) | READING | — | B22.35 |
| B22.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1; B22.35 step 3, moved | BUILD | MOVER (the re-pin) | B22.35, B22.R1 to B22.R3 |

**Not carried, with the reason.** `04_MB_playable_field_scenario` §E's bullet "one training Site of each kind at each faction's seat settlement": replaced by `U5b_MB_residue` §3 (that file's own head line, item (2): "Training Sites are planted where the realm's venues already name them"), landed in B22.17. `IS-MB-06`: SUPERSEDED by MBA-04 (D-15). The intake's IN-52 (lane's target "B22 after `07_SE_campaign_supply_and_muster`") sits under the intake's B12 heading, which governs (D-14); it is not an item here (see the receipt).

### B22.01 — which military and physical obstacle terms join the obstacle roster, and which levels join the leverage roster · `U5b_VERBS_military_physical_residue` §1 rule 3, `IS-MB-B1` · DESIGN-FIRST · HASH EQUAL
- SOURCE: `proposals/U5b_VERBS_military_physical_residue.md` §1 rule 3 ("Which of the MILITARY and PHYSICAL terms are new members and which fold into existing ones is U1's, not yet decided"); `IS-MB-B1`; `unified/U4_DOCUMENT_STATUS.md` §3.4 rows for `14_VERBS_MILITARY_A`–`_D` and `14_VERBS_PHYSICAL_B` (code DESIGN); rulings A-25; D-18.
- ADVANCES: nothing by itself; it settles the INCOMPLETE part of five members of this batch (their terms ship absent until it is settled).
- INSTRUCTION: write the design stating (1) to (6) with falsifiers; no code.
  1. For each hostile term the five sources list, whether it becomes a member of the obstacle roster (`rosters.yaml: obstacle_terms`, `U5c_SC_one_obstacle_form.md` §2) or folds into an existing member (named): from `14_VERBS_MILITARY_A` Edit 4: `winter`, `body_below_first_band`, `destination_occupied`, `foreign_holder` (R4's suggestion: a `rank_gap`-like member), `larder_short` (R4's suggestion: `stakes`); from `14_VERBS_MILITARY_B` Edit 2: `learner_rank` (the source's warning: it reads the subject's skill score, the operand `opposition` reads for a person opposite, "so folding it there would make the lesson opposed"), `self_taught`, `no_training_place`, `teacher_no_better`; from `14_VERBS_MILITARY_C` Edit 5: `muster_difficulty`, `cohort_resents` (the source: "may be the existing member `regard`"), `larder_short` ("may be `stakes`, as for `migrate`"), `half_under_arms`, `arrears`, `on_foreign_ground`; from `14_VERBS_MILITARY_D` Edit 4: `drill_difficulty`, `no_training_place`, `influx_exceeds_body`, `body_raw`, `body_experienced`, `arrears`, `many_fields`, `undisciplined` (the source: `body_raw` and `undisciplined` "read the same Discipline step the field's obedience draw reads as `unsteady`, `27_MB_A` §3, and should be one member"); from `14_VERBS_PHYSICAL_B` B2: the town's fabric as the existing member `ruin` (member 27; "R4 7b.5's default, U1 to confirm — no new `fabric` member").
  2. For each favourable term, whether it becomes a named source of `rosters.yaml: advantage_sources` (a level for the roller, A-25, never an obstacle subtraction): `sworn_there` (`migrate`), `learner_regards_teacher` (`train`), `cohort_committed`, `footing_war` (`recruit`), `levy` (`discharge_troops`), `disciplined` (`order_unit`), and the army's size against the town for `raze` (R4 7b.5 suggests "a `levy`-like source").
  3. One term, one member: a term two verbs name (`larder_short`, `no_training_place`, `arrears`) is one member read by both.
  4. For each new member, the reader it calls (a `world_q` Query or the composer's own operand), named by symbol.
  5. What ships until values are set: every term absent (0), the sources' control ("the control is `routine`"; `move`'s "`routine` + `distance`").
  6. The falsifier of each member: a reading in which the term's fact holds and the obstacle does not rise; for each level, a reading in which a favourable term lowers the obstacle (a defect, A-25).
  No build item of this batch gates on this item: each source ships its terms absent; the members and sources this design names join their rosters, with values, in B98 (DIALS AT CONTROL). What the ladder cannot settle ends the run `STOPPED` for Jordan (D-18).
- WHERE: NEW `proposals/2026-11-12-subsystem-audit-suite/proposals/U1_obstacle_terms_military_physical.md` `[ASSUMPTION: the path — basis: IS-MB-B1 names the U1 owners ledger as owner and CLAUDE.md §3 sends new design work to proposals/; the roster rows themselves are code-read facts and live in rosters.yaml, never in this file]`.
- TESTS: none (a design).
- FALSIFIER and CONTROL: a term the design leaves undecided; a favourable term placed on the obstacle side. Control: nothing in `engine/` changes in this commit.
- GATE: `test -f proposals/2026-11-12-subsystem-audit-suite/proposals/U1_obstacle_terms_military_physical.md && grep -c -E 'winter|learner_rank|muster_difficulty|drill_difficulty|ruin' <that file>` → the file exists and names every term of (1) and (2); `git diff --stat <batch-start-sha>..HEAD -- engine modules references` → empty for this commit (no code).
- HASH MOVERS: none.
- DEPENDS ON: V12 the obstacle composer and `obstacle_terms` roster (`U5c_SC_one_obstacle_form`, Batch B05); V12 the `a task` prize (`U5c_VERBS_residue_and_governance_owner` §1, Batch B07); EXISTS-IN-TREE `engine/season/rosters.yaml: advantage_sources` `[ASSUMPTION: present after B05 — basis: U5c_SC_one_obstacle_form §3 named by the source]`.
- GLOSSARY: none (no new word; each term keeps its source name until the design renames it, and a rename edits its glossary row in the commit that lands it).
- COST and TIER: design; `opus`, high; a `ners` critic.
- LANDS IT: B22's producer; `Item: B22.01`, `[skip ci]`.

### B22.02 — the unit row holds what the army lost, by kind · `27_MB_E` 27E-1 · BUILD · HASH EQUAL
- SOURCE: `proposals/27_MB_E_what_an_army_carries_back.md` "Instructions to code it", row 27E-1; §2; "Tests"; rulings A-69, A-78; `unified/U3_CONFLICT_LEDGER.md` C3-L11.
- ADVANCES: A-69, A-78 (losses are written); the row B22.04 writes and B22.05 reads.
- INSTRUCTION:
  1. `modules/mass_battle/armyrecord.py`: the unit row gains `absent: ((cohort, kind, count, tick), ...)` and `last_field: (lap, stamina_left) or None`, both optional and absent by default; `ABSENT_KINDS = ('injured', 'fled')`; new `lose(record, name, losses)` lowers `assigned` by the four counts (dead, injured, fled, taken) and appends the injured and fled to `absent`; new `restore(record, name, cohort, kind, count)` moves a count back; `OPS` and `_apply` gain both ops; `cohort_claims` counts absent men ("Men in `absent` are alive, are still the cohort's, and still count against what the army may hold of that cohort"); `options()` gains `absent_men`; `validate` accepts and checks the two keys. (The source's `last_field: (round, stamina_left)` is the season's pass: corrected to `lap`, A-101.)
  2. `armyrecord` gains the two ops on the existing `mass_battle.army` composition row.
  3. `engine/season/rosters.yaml: record_kinds.values.army`: the unit row's key set gains `absent`, `last_field`.
- WHERE: `modules/mass_battle/armyrecord.py` (the unit row; `ABSENT_KINDS`; `lose`; `restore`; `OPS`; `_apply`; `cohort_claims`; `options`; `validate`); `engine/season/rosters.yaml` (`record_kinds.values.army`).
- TESTS: in `tests/valoria/test_mass_battle_army_record.py`, written before the edit and read red (no `lose`, no `restore`): `test_lose_lowers_assigned_by_the_four_kinds_and_holds_two`, `test_restore_returns_absent_men_and_refuses_more_than_are_absent`, `test_absent_men_still_count_against_their_cohort`, `test_absent_kinds_are_a_closed_set`.
- FALSIFIER and CONTROL: a `restore` that returns more than is absent; absent men not counted by `cohort_claims`. Control: the realm content hash at seeds 0 to 2 equal to the previous close's (`reading @<sha>`): no caller yet.
- GATE: `python -m pytest tests/valoria/test_mass_battle_army_record.py -q` → the four pass; the rest of the file green (the key set the test pins equal to `rosters.yaml`'s, `:189-190`).
- HASH MOVERS: none (no caller; no shipped world holds an `army` Record).
- DEPENDS ON: EXISTS-IN-TREE `modules/mass_battle/armyrecord.py::OPS`, `::_apply`, `::cohort_claims`, `::options`, `::validate`; V12 Batch B16L (the row key `units`, L1-1), Batch B17 (`04_MB_typed_outcome_and_one_path`).
- GLOSSARY: row *loss* (MB lexicon D-17: dead, captured, injured, fled; regroup, deserters) gains a pointer to `armyrecord.ABSENT_KINDS` for the two kinds the row holds.
- NAMES: `subformations` → `units` (B16L, L1-1); `Claim.round` → `Claim.lap` (B04, PCR-4).
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B22's producer, `isolation: worktree`; one `Item: B22.02` commit, `[skip ci]`.

### B22.03 — the battle returns the stamina each unit ended with; a second battle in a lap starts from it · `27_MB_E` 27E-2 · BUILD · HASH EQUAL
- SOURCE: `proposals/27_MB_E_what_an_army_carries_back.md` row 27E-2; §4; gate 6; D-U1-11e (`stamina_left` is declared here, first to land).
- ADVANCES: A-69 (armies carry fatigue back).
- INSTRUCTION:
  1. `engine/season/queries/inputs.py::FieldOutcome` parts gain `stamina_left: float` (a share in [0, 1]) and `ended: str` (the end-state word per part: `stood`, `gave_ground`, `routed`, `rallied`, `withdrew`).
  2. `modules/mass_battle/massbattle.py::_grade` fills them from each unit's column blocks: `stamina_left` is "the troop-weighted mean of that unit's column blocks at the field's end (`Unit.agg_stamina()` as `16_PESSIMIST_MB_one_stamina_ledger.md` step 2 redefines it, taken per unit)".
  3. The season records a crossing, not a level: the unit row holds `last_field: (lap, stamina_left)` (written by B22.04's commit).
  4. `engine/season/seam/wrappers/mass_battle.py::field_input` computes `entry_stamina` per part from the row's `last_field` "when its round is the current round, else the proposal 26 writers": in the **same lap**, the `stamina_left` it holds plus one lull's recovery (`fatigue.lull_recover`), in place of the flat `fatigue.entry.second_field` seed of `26_MASS_BATTLE_movement_and_fatigue_as_data.md` §3, which becomes the fallback for a part with no record; in a **later lap**, full, times that file's other entry writers (a hard march; a short ration). (Source "round" → "lap" throughout this step, A-101.)
  5. `references/troops.yaml`: `fatigue: {carry: off, carry_laps: 0}` (`carry` `off | on`; the source's `carry_rounds` is named for the lap, A-101; control 0, "within a lap only"). (Patched: P-10) The two keys join the `fatigue` block B19.28 created (it holds `lull_recover`); never a second block. `entry_stamina` and `fatigue.lull_recover` exist from B19.28.
- WHERE: `engine/season/queries/inputs.py` (`FieldOutcome`); `modules/mass_battle/massbattle.py` (`_grade`); `engine/season/seam/wrappers/mass_battle.py` (`field_input`); `references/troops.yaml` (`fatigue`).
- TESTS: in `engine/season/tests/test_march.py`, written before step 4 and read red: `test_a_second_field_in_one_round_is_entered_at_the_stamina_left` (gate 6; the source's name kept; it asserts on the built input that the second field's `entry_stamina` per part equals the first's `stamina_left` plus one lull's recovery, with `fatigue.carry: on` set in the test).
- FALSIFIER and CONTROL: a second battle in a lap entered at full stamina. Control: with `fatigue.carry: off`, the realm content hash at seeds 0 to 2 equal to the previous item's reading.
- GATE: `python -m pytest engine/season/tests/test_march.py::test_a_second_field_in_one_round_is_entered_at_the_stamina_left -q` → pass; `python tools/export_troops.py --check` → exit 0; `python tools/ci_golden_modes_check.py` → digests equal.
- HASH MOVERS: none at `carry: off`. Under `carry: on`: a second field in a lap (declared; not shipped).
- DEPENDS ON: V12 Batch B17 (`04_MB_typed_outcome_and_one_path`: the per-part outcome; `references/troops.yaml` and `tools/export_troops.py`); V12 Batch B19 (`16_PESSIMIST_MB_one_stamina_ledger` steps 2 and 3); EXISTS-IN-TREE `engine/season/seam/wrappers/mass_battle.py::field_input`; V12 B22.02. `26_MASS_BATTLE_movement_and_fatigue_as_data.md` §3 lands in B31 (cut edge, U3 §4.1 row 79): until then the fallback is today's entry value.
- GLOSSARY: none (`stamina_left`, `last_field` are code names; prose says "the stamina a unit ended with").
- NAMES: `hierarchy.units.Unit` → `Army` and `Subunit` → `Unit` (B16M, L2-1): "`Unit.agg_stamina()` … taken per unit" is read on the renamed classes by symbol; `Claim.round` → `Claim.lap` (B04).
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B22's producer; `Item: B22.03`, `[skip ci]`.

### B22.04 — a battle's losses are written on the unit row by kind, and counted once · `27_MB_E` 27E-3 · BUILD · HASH EQUAL
- SOURCE: `proposals/27_MB_E_what_an_army_carries_back.md` row 27E-3; §1, §2; "Data rows and schema"; gates 1–3; rulings A-30, A-69, A-78; `IS-MB-B3` (the share tables BLOCKED: values not established).
- ADVANCES: A-69, A-78 (a loss has a kind; losses are written).
- INSTRUCTION ("These three edits are one commit"):
  1. `engine/season/loop/effects_combat.py::_eff_march`, inside `_casualties`: under `recuperation: on`, for each army part, the two draws of §1, then one `ArmyCommand(record, 'lose', …)` through the `mass_battle.army` composition row and the army verbs' write path; the cohort's `body` scaled by the dead share only; `last_field` written. The two draws, per part: "(a) of `fight_loss`, the share that is injured and not dead; (b) for a routed, unrallied part, the share of its survivors that fled. Each is a draw on the one sampler and ladder, keyed `(field, part, "injured")` and `(field, part, "fled")` (A-30), whose band selects a share from a four-row table (`aftermath.injured_share`, `aftermath.fled_share`), the form `26_…` §4 already uses for `taken`." Odds terms (signs are the design; sizes are parameters): for (a), the side held the field at the end (raises the injured share; ships at control 0 until a source is filed); the part was pursued (lowers it). For (b): the rally band (a `withdrew` part loses none this way); mounted pursuit against it (raises it); the part's Discipline (lowers it). Men lost in a pursuit are dead or taken, never injured. A rallied part and a part that withdrew in order have no fled men. The kinds: dead (a drawn share of `fight_loss`; the untaken part of `pursuit_loss`), captured (`taken`), injured (the rest of `fight_loss`), fled (a drawn share of the survivors of a part that ended `routed`).
  2. `engine/season/seam/wrappers/mass_battle.py::_order_of_battle`: passes fitness 1.0 under the arm.
  3. `modules/mass_battle/armyrecord.py::to_order_of_battle`: reads `assigned` less nothing under the arm ("the loss is already in it"). "A field that scaled a cohort's body **and** lowered `assigned` would count the loss twice."
  4. `references/troops.yaml`, new section, copied (every value absent until set; the loader refuses `recuperation: on` while any is absent):
     ```yaml
     aftermath:
       recuperation: off                    # off | on.   off is today's loop: the control
       return: unprompted                   # unprompted | off      (A-78: unprompted is the rule; off is the test's control)
       acting: on                           # on | off              (ASSUMPTION, reversible)
       injured_share:  {Overwhelming: ~, Success: ~, Partial: ~, Failure: ~}    # NOT ESTABLISHED
       fled_share:     {Overwhelming: ~, Success: ~, Partial: ~, Failure: ~}    # NOT ESTABLISHED
       recover_share:  {Overwhelming: ~, Success: ~, Partial: ~, Failure: ~}    # NOT ESTABLISHED
       regroup_share:  {Overwhelming: ~, Success: ~, Partial: ~, Failure: ~}    # NOT ESTABLISHED
       window: ~                            # laps. NOT ESTABLISHED
       wounds_turn: off
     ```
     (The source's `window: ~  # rounds` counts the season's passes: corrected to laps, A-101.) Its loader (`tools/export_troops.py` and the module's table reader, B17) refuses `recuperation: on` with any `~` value.
  5. (Patched: P-05) **The fatigue half of the `Drawn` write.** B17.01 writes `Drawn`'s shares and the re-homing and leaves "the fatigue half of 'losses and fatigue are written for each (A-69)'" to `27_MB_E` here (B17's UNDECIDED (1)). Step 1's per-part write, `last_field: (lap, stamina_left)` included, is made on a `Drawn` field for every part of **both** sides, as on `Won` and `Lost`, at the same site in `_casualties`, not by a branch on the band's name; under the arms' control values it writes what the shipped loop writes. `[ASSUMPTION: `_casualties` is reached on `Drawn` after B17.01 — basis: B17.01 step 8 scales both sides' bodies "under `field_casualty_model` as the winners' write is today"; the item's first step opens `_casualties` and records in the commit body that the `Drawn` arm reaches it]`.
- WHERE: `engine/season/loop/effects_combat.py` (`_eff_march`, `_casualties`); `engine/season/seam/wrappers/mass_battle.py` (`_order_of_battle`); `modules/mass_battle/armyrecord.py` (`to_order_of_battle`); `references/troops.yaml` (`aftermath`); `engine/engine_params/troops.json` (re-exported, never hand-edited).
- TESTS: in `engine/season/tests/test_march.py`, written before the edit: `test_recuperation_off_is_the_body_loop_unchanged` (control, hashes equal; green before and after), `test_a_loss_is_never_counted_in_both_the_body_and_the_row` (gate 2; red before the edit; reddens on a planted "still multiply by fitness"); in `engine/season/tests/test_cr_24_winner_casualties.py`: `test_winner_and_loser_write_losses_the_same_way`; (Patched: P-05) in `engine/season/tests/test_march.py`, beside B17.01's `test_a_drawn_field_writes_both_sides_losses`: `test_a_drawn_field_writes_both_sides_last_field` `[ASSUMPTION: test name; the item creates it, E-3]` (a hand-built stalemate with `fatigue.carry: on` set in the test: both sides' parts hold `last_field` with this lap and their `stamina_left`; red before step 5). Each test that needs the arm on sets the share tables in the test's own `troops` override (the loader refuses them absent).
- FALSIFIER and CONTROL: a loss present in both the cohort's body and the unit's `assigned`; a unit that stood with fled men. Control: `recuperation: off` — hashes EQUAL; 200 seeded army fields fold to the same cohort bodies as before (gate 1).
- GATE: `python -m pytest engine/season/tests/test_march.py engine/season/tests/test_cr_24_winner_casualties.py -q` → green; with the arm on in a test world, gate 2: for each unit, `assigned` after equals `assigned` before less the four kinds, and the unit's strength at an immediate second field equals `assigned`; gate 3 over 400 routed fields: a routed unrallied unit has fled men in some seeds and none in some, a unit that stood has none in all, a rallied unit none in all (`assert checked >= 400`); `python tools/export_troops.py --check` → exit 0. The covering files the source names (`tests/valoria/test_army_battle.py`, `test_army_verbs.py`, `test_mass_battle_army_record.py`, `test_mass_battle_order_of_battle.py`, `engine/season/tests/test_rem32_scale.py`, `test_cp_t04_02_marshal.py`) → unchanged at `recuperation: off`.
- HASH MOVERS: none at the shipped arm. Under `recuperation: on`: every army field's fold (declared; not shipped, and not settable until the values exist).
- DEPENDS ON: V12 B22.02, B22.03; V12 Batch B19 (`26_MASS_BATTLE_rout_pursuit_and_giving_ground` §4: `fight_loss`, `pursuit_loss`, `taken`; `16_PESSIMIST_MB_rout_has_two_exits`: the end states); V12 Batch B05 (the one sampler); V12 Batch B06 (the keyed draw); EXISTS-IN-TREE `engine/season/loop/effects_combat.py::_eff_march` (`_casualties` inside it), `engine/season/seam/wrappers/mass_battle.py::_order_of_battle`, `modules/mass_battle/armyrecord.py::to_order_of_battle`. SITE: "where the army verbs' write path takes an `ArmyCommand` from a non-verb caller (`_eff_march` is the first effect outside `effects_army.py` to write the Record)" was not opened by the source (`IS-MB-B4`): the INSTRUCTION's first step is "open `engine/season/loop/effects_army.py` and record in the commit body how an `ArmyCommand` reaches the write path from a non-verb caller", then the edit.
- GLOSSARY: none new (the kinds are MB lexicon D-17's words).
- NAMES: `Subunit` → `Unit` (B16M) where the module's parts are read; `Claim.round` → `Claim.lap` (B04).
- COST and TIER: small build; `sonnet`, high; the batch's `opus` closing critique on the read-and-write move (the double-count hazard).
- LANDS IT: B22's producer; `Item: B22.04`, `[skip ci]`.

### B22.05 — the strength a reader sees adds the men who came back, by a draw; an act writes them · `27_MB_E` 27E-4 · BUILD · HASH EQUAL
- SOURCE: `proposals/27_MB_E_what_an_army_carries_back.md` row 27E-4; §3; gates 4, 5; "Tests"; `unified/U3_CONFLICT_LEDGER.md` C3-L11 (computed when read; no MATTER row, no clock); rulings A-54, A-78.
- ADVANCES: A-78 ("a beaten commander who does nothing recovers some").
- INSTRUCTION:
  1. `engine/season/queries/world_q.py`, new `army_strength(w, record, unit)`: "`assigned` plus the recovered share of each `absent` entry by the keyed graded draws of §3, computed when read; the one reader every consumer of an army's strength calls (`seam/wrappers/mass_battle.py::_order_of_battle`, `armyrecord.options` via the host, the military menu)". For each season elapsed since the loss, a keyed graded draw `H(seed, army, loss, season)`:
     ```
     the injured:
     pool      the endurance of the place the army is stationed at            (A-54's pool; the WR lane's reader)
     levels    + a healer's `tend` on the army this lap (his `healing` rank, as a named level for the roll)
     obstacle  the season's hardship                                            (A-54's obstacle)
               + the army marched this lap        + its ration was short (SE's debit)
               + the unit ended its last field routed
     band  ->  aftermath.recover_share[band] of the injured count as returned, at the read; the rest stay
               absent and are drawn again for the next season elapsed

     the fled:
     pool      the endurance of the place the army is stationed at
     obstacle  the season's hardship
               + the unit is in `arrears`             + the army stands far from the cohort's home
               + the part was ridden down by horse    + the cohort's stance toward the commander is hostile
     band  ->  aftermath.regroup_share[band] of the fled count as returned, at the read; the rest stay
               absent and are drawn again for the next season elapsed
     ```
     (Source "this round" → "this lap", A-101.) Injured men still absent after `aftermath.window` laps are struck from `absent`. Fled men still absent when `aftermath.window` seasons have passed are read as **deserted**; "the next act on the Record strikes them from `absent`, and the strike is an Observation on that act's Event (how many, from which unit; an `observation_terms` member, D-U1-06)". `aftermath.wounds_turn: off` (whether a Failure turns injured to dead is not established).
  2. `engine/season/loop/effects_army.py`: "every army verb that writes the Record first writes the read's recovered men through `restore` and strikes the deserted (with the Observation); `assign_troops` on a unit with fled men adds one further draw (the recall), behind `aftermath.acting`" — the recall is "one **further** draw that round, on his `command` as that verb is already drawn (`14_VERBS_MILITARY_D_the_order_of_battle.md` Edit 4), its band returning a share of those still absent"; a muster at the cohort's home removes the distance term for that lap. `aftermath.return: off` is the control (nobody returns); `aftermath.acting: off` the reversible arm (the recall's draw and the muster's term not applied).
  3. Order: the reader, then its callers (`_order_of_battle`, `armyrecord.options` via the host, the military menu), then the write-through in `effects_army.py`.
- WHERE: `engine/season/queries/world_q.py` (NEW `army_strength`); `engine/season/seam/wrappers/mass_battle.py` (`_order_of_battle`); `engine/season/harness/military_menu.py` (its strength read); `engine/season/loop/effects_army.py` (the write-through before each army verb's write; the recall); `engine/season/rosters.yaml` (`observation_terms` gains the desertion strike's term).
- TESTS: in `engine/season/tests/test_march.py`, written before the edit and read red: `test_the_strength_read_twice_at_one_tick_is_one_value`, `test_an_act_after_the_read_writes_the_share_and_the_next_read_adds_nothing_new` (C3-L11's falsifier), `test_a_commander_who_does_nothing_recovers_some_and_not_all` (gate 5, A-78), `test_the_dead_the_captured_and_the_deserted_never_return` (gate 4 and the falsifier), `test_a_recall_brings_more_back_or_sooner_and_acting_off_brings_nothing_extra`. The arm-on tests set the share tables and `window` in the test's own override.
- FALSIFIER and CONTROL: a unit whose every loss returns, or none, at every seed; a return of the same share at every seed; a dead man restored by `tend`; a captive or a deserter back on the row; fled men who return only when an act is formed. Controls: `recuperation: off` (today), `return: off` (nobody returns), `acting: off` (acts add nothing).
- GATE: `python -m pytest engine/season/tests/test_march.py -q` → green. In the tests (two laps of seasons at most; the source's "three rounds after a lost field" is read at two seasons, "(three rounds in the source; A-114)"): gate 4, 200 seeds: some injured have returned and some have not in most seeds; the dead count unchanged by any `tend`. Gate 5, 200 seeds, no act on the army for the window: fled men return in most seeds, never all in every seed, and the men struck at the window's close are above zero in some seeds; with a recall each lap, more return or as many sooner beyond the sampling band; `acting: off`, the recall changes nothing field for field; `return: off`, nobody returns. `assert checked >= 200` in each.
- HASH MOVERS: none at the shipped arms. Under `recuperation: on`: every reader of an army's strength (declared; not shipped).
- DEPENDS ON: V12 B22.04; V12 the reader of a place's endurance and of the season's hardship (A-54's pool and obstacle), named by `16_PESSIMIST_GAME_the_world_draws.md` (Batch B12a); V12 SE's ration debit (`07_SE_campaign_supply_and_muster` (e), B22.16 — a later item of this batch: until it lands the "ration was short" term reads false); V12 `14_VERBS_MILITARY_C`, `_D` (B22.21, B22.26: the muster and `assign_troops` as draws, which the recall reads; until they land the recall arm reads nothing) — U3 §1.2 lands this file first ("the loss ledger MILITARY_A, _C and _D read"); EXISTS-IN-TREE `engine/season/loop/effects_army.py`, `engine/season/harness/military_menu.py`. The cohort's dead remain a known gap (27_MB_E INCOMPLETE item 3: the census's `weight` write is SE's, not opened); the captured cohort share is a count on the band Event until SE has a place for prisoners (item 4).
- GLOSSARY: row *regroup* / *deserter* (MB lexicon D-17) gains a pointer to `world_q.army_strength` as the reader that computes them.
- NAMES: `Claim.round` → `Claim.lap` (B04).
- COST and TIER: design-first for the terms and the window in the source (`opus`), then `sonnet`; here the form lands behind its arm with no value, so: small build; `sonnet`, high; `opus` reads the terms at the close. Sweeps `haiku` (`valoria-measure`).
- LANDS IT: B22's producer; `Item: B22.05`, `[skip ci]`.

### B22.06 — `move` forms only on places · `14_VERBS_MILITARY_A` Edits 1 (the class), 2 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_MILITARY_A_movement.md` §3 Edit 1 (first commit: "the class and the stamp terms first (flat `writes:`/`emits:` as today)") and Edit 2; §4; closes H-329, H-140 (with B22.08); H-309 closes as answered with no code change.
- ADVANCES: R-05 (`move` built out); H-329.
- INSTRUCTION:
  1. `engine/season/verb_table.yaml`, the `move` row: add `referent_class: Rung` and the note, writes and emits left flat as today:
     ```yaml
         referent_class: Rung
         referent_class_note: "14-VM-A: `migrate`'s class. FORMED ONLY ON A PLACE: `places_named` (told of, not lived under), `home_when_away` (his own `reside` object when his live `contain` is elsewhere) and `whereabouts_named` (the rung his own ledger's newest `at` claim gives for a Person the question names). Not on a person, a Record or the rung he stands on (H-329). REVERT: delete this column and the two stamp terms."
     ```
  2. `engine/season/queries/world_q.py`, two stamp terms beside `places_named` (resolver-side standing occasions, `larders_in_purview`'s shape; each reads the person's own edges and own ledger):
     ```python
     def home_when_away(w: World, p: Person) -> tuple:
         """`(reside object,)` when p's live `contain` object is another rung; `()` otherwise."""

     def whereabouts_named(w: World, p: Person, persons: tuple) -> tuple:
         """For each Person id in `persons` (the question's own Person referents): the value of the newest
         `at` claim about him in p's OWN ledger, if it is a Rung the ladder would seat p in
         (`contain_ascends`) and p is not already there. Sorted, de-duplicated."""
     ```
     `questions_for` splices both onto the first question as `Rung`-classed referents, where it splices `places_named`. No new class, no operand.
  3. (Patched: P-03) **`migrate` keeps its settlement-only restriction.** B12c.14 (`U5d_SE_owed_edits` §2, the `migrate` half) made `migrate`'s class read only settlement rungs, "the restriction at the stamper that forms it, never a test of the verb's name", with a `distinct: [from, to]` decline. The two stamp terms of step 2 do not widen it: a referent they splice reaches a `migrate` candidate only through the settlement-rung reading B12c.14 placed at the stamper (a territory, a duchy or the realm is never a `migrate` destination); `move` takes the unrestricted `Rung` reading. Open `questions_for` and B12c.14's stamp at this item's base and record in the commit body where the restriction sits; if splicing the terms would bypass it, the splice goes beneath it. (B12c.14 chose `14_VERBS_MATERIAL_B`'s `Needy`/`Market` classes for `transfer`/`exchange` over U5d §2's shared `Rung` and kept U5d's restriction for `migrate`; B22's sources predate that choice.)
- WHERE: `engine/season/verb_table.yaml` (`move`); `engine/season/queries/world_q.py` (NEW `home_when_away`, `whereabouts_named`; `questions_for`); NEW `engine/season/tests/test_vm_mil_a_movement.py`.
- TESTS: NEW `engine/season/tests/test_vm_mil_a_movement.py` ("one function per §4 reading; `aperture 2 s` called inside it"), written first: `test_moves_go_to_another_rung_and_none_to_the_same` (reading (i)) and `test_no_move_attempted_on_a_person_or_record` (reading (ii)), each read red at the base (H-329: 16 of 17 executed moves at seed 0 went to the mover's own rung).
- FALSIFIER and CONTROL: planted, `whereabouts_named` returning the person's rung id itself: (ii) fails. Control: same seed twice, equal `content_hash`.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mil_a_movement.py -q` → (i) and (ii) pass: over `aperture 2 s`, s = 0, 1, 2, moves to a rung other than the mover's own above 0 at every seed, same-place moves 0; no `move` attempted whose `to` is a person or a Record. (Patched: P-03) `python -m pytest engine/season/tests/test_vm_mat_b_stores.py -k no_migrate_candidate_names_a_non_settlement_rung -q` → pass (B12c.14's test, still green with the two new stamp terms).
- HASH MOVERS: formation of `move` in every seeded realm, spine and corpus world (declared; B22's one re-pin).
- DEPENDS ON: EXISTS-IN-TREE `engine/season/queries/world_q.py::places_named`, `questions_for`; V12 Batch B12c (`07_SE_kernel_repairs`: a move to where the mover stands declines, H-329's other half); (Patched: P-03) V12 B12c.14 (`migrate`'s settlement-only stamp and its test).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B22's producer; `Item: B22.06`, `[skip ci]`.

### B22.07 — the journey's Event says where the mover went · `14_VERBS_MILITARY_A` Edit 3 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_MILITARY_A_movement.md` §3 Edit 3; §1 item 3.
- ADVANCES: R-05 (a witness knows where a traveller now is); the downstream read of §4.
- INSTRUCTION: `engine/season/loop/effects_migration.py::_relocate` returns the destination to its caller; `_eff_move`, `_eff_migrate` and `loop/effects_combat.py::_eff_march` put `Observation(mover, "at", dest)` on the Event beside what they already carry (`body_observed`'s shape). `rosters.yaml: observation_terms` gains `at`. WITNESS deposits it to whoever it deposits the Event to; nothing new decides who that is. SITE (the source's `[UNVERIFIED]`): first open `engine/season/loop/witness.py` and record in the commit body whether an Observation whose value is a rung id needs a change there (`broke_observed` carries a bool); if it does, the change is made in this commit and named.
- WHERE: `engine/season/loop/effects_migration.py` (`_relocate`, `_eff_move`, `_eff_migrate`); `engine/season/loop/effects_combat.py` (`_eff_march`); `engine/season/rosters.yaml` (`observation_terms`); `engine/season/loop/witness.py` (only if the SITE step finds it needed).
- TESTS: in `test_vm_mil_a_movement.py`: `test_a_traveller_is_believed_at_his_destination` — after one `move` through the fold, a witness holds the claim `(mover, at, dest)`; red before the edit.
- FALSIFIER and CONTROL: a `travel.moved` Event with no `at` Observation. Control: same seed twice, equal hash.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mil_a_movement.py -q` → green.
- HASH MOVERS: every seeded world with a journey or a march (the Observation is a deposit; declared; B22's one re-pin).
- DEPENDS ON: V12 B22.06; EXISTS-IN-TREE `engine/season/loop/effects_migration.py::_relocate`, `engine/season/loop/effects_combat.py::_eff_march`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B22's producer; `Item: B22.07`, `[skip ci]`.

### B22.08 — a journey is one draw, written by band · `14_VERBS_MILITARY_A` Edits 1 (the bands), 4, 5 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_MILITARY_A_movement.md` §3 Edit 1 (second commit: "the bands with Edit 4"), Edit 4, Edit 5; §4; "Standing" (A-5, A-6, A-7, A-8, A-25, A-30, A-81); closes H-329 and H-140 with B22.06.
- ADVANCES: R-05 (`move`, `migrate` built out); R-09 (an outcome drawn).
- INSTRUCTION:
  1. `engine/season/verb_table.yaml`, the `move` row, final text of the changed columns (Edit 1):
     ```yaml
         contests:    "a task"        # shape (b): bands write different cells (VRES §1)
         capability:  none            # `wayfaring` once its definition row lands (U1 D-U1-07)
         difficulty:  routine         # + `distance` (OBS member 20), the hops between origin and destination
         writes:
           Overwhelming: ["Tenure.until", "Tenure.since"]
           Success:      ["Person.travel_leg", "Tenure.until", "Tenure.since"]
           Partial:      ["Person.travel_leg", "Tenure.until", "Tenure.since"]
           Failure:      ["Person.travel_leg"]
         writes_note: "14-VM-A: ONE JOURNEY BODY (`_relocate`), FOUR BANDS. Overwhelming: arrives, no leg laid (the journey costs nothing next season). Success: today's write. Partial: arrives spent, the destination appended to `travel_leg` twice (`decision/budget.py`'s distance penalty reads its length). Failure: turned back; no `contain` moves, one leg laid. [ASSUMPTION; medium; Jordan to correct; revert: the flat three pairs and the route row.]"
         emits:
           Overwhelming: ["travel.moved"]
           Success:      ["travel.moved"]
           Partial:      ["travel.moved"]
           Failure:      ["travel.turned_back"]
         emits_on_refusal:
           path:     ["travel.blocked"]
           audience: ["travel.blocked"]
           write:    ["travel.blocked"]
         grade:       "assumption"
         source:      "ARCHITECTURE_V2.md §E3, transcribed; bands and class: proposals/2026-11-12-subsystem-audit-suite/proposals/14_VERBS_MILITARY_A_movement.md"
     ```
     (`stratum: "movement"`, `eligibility: ["own"]`, `beneficiary: "actor"`, `requires`, `requires_typed` (`contain_path` of actor to `to`, conjunct `path`; `relation` of `to`, relation `audience`, conjunct `audience`) as the row has them.)
  2. Edit 4, the draw: both rows are contest rows on the `a task` prize (VRES §1 shape (b)); the prize row binds the roll, so neither joins the route roster; the skill is the row's own `capability:` cell (`wayfaring` once U1's surface defines it), not a `verb_capability` line. Obstacle and leverage through the one composer:
     | verb | difficulty | obstacle members | leverage (levels for the roller, A-25) |
     |---|---|---|---|
     | `move` | `routine` | `distance` (OBS member 20: the hops between origin and destination on the containment tree, `world_q.ancestry`, the one walk; fixture `distance_step`) · `winter` · `body_below_first_band` · `destination_occupied` | — |
     | `migrate` | `routine` | the four above · `foreign_holder` (the destination's `holder_faction_of` is not the migrant's faction) · `larder_short` | `sworn_there`: a `favour` level (a live sworn `oblige` to a seat whose purview reaches the destination; C3-C10) |
     `winter`, `body_below_first_band`, `destination_occupied`, `foreign_holder`, `larder_short` and the level `sworn_there` ship absent (0) until B22.01's design names them: the control is `routine` + `distance`. `loop/effects_migration.py::_eff_move(w, a, res)`: after the declines (custody, arrival-only, the ladder, and **a destination that is his live `contain` object**, H-140), dispatch on `res.degree`: `Failure` → `Change((Subject.entity("persons", a.actor, fields=("travel_leg",)),), lay_one_leg)`; the others → `_relocate(w, a, dest, legs=0 | 1 | 2)`. `_relocate` gains `legs: int = 1`, the count of times `dest` is appended; `_eff_march` passes nothing and is unmoved. `_eff_migrate(w, a, res)`: `Overwhelming`, `Success` → today's `perform`; `Partial` → `_relocate` alone (the `reside` edge untouched), emitting `travel.moved`; `Failure` → as `move`.
  3. Edit 5, the `migrate` row (cell, class and refusals unchanged):
     ```yaml
         contests:    "a task"        # shape (b)
         capability:  none            # `wayfaring` once defined
         difficulty:  routine
         writes:
           Overwhelming: ["Tenure.until", "Tenure.since"]
           Success:      ["Person.travel_leg", "Tenure.until", "Tenure.since"]
           Partial:      ["Person.travel_leg", "Tenure.until", "Tenure.since"]
           Failure:      ["Person.travel_leg"]
         emits:
           Overwhelming: ["residence.changed"]
           Success:      ["residence.changed"]
           Partial:      ["travel.moved"]
           Failure:      ["travel.turned_back"]
         writes_note: "14-VM-A: Partial is LODGED, NOT HOUSED -- the journey is made and `reside` is untouched, which is a `move`; he may settle from where he stands next season. [ASSUMPTION; medium; Jordan to correct]"
     ```
  4. Draws: `H(w.world_seed, w.tick, <actor id>, "move.task")`, `"migrate.task"` (A-30). A-81: Failure lays one leg and emits `travel.turned_back`, witnessed by those present.
- WHERE: `engine/season/verb_table.yaml` (`move`, `migrate`); `engine/season/loop/effects_migration.py` (`_eff_move`, `_eff_migrate`, `_relocate`); `engine/season/rosters.yaml` (the composer's rows for `move`, `migrate`; fixture `distance_step` is B12c's).
- TESTS: in `test_vm_mil_a_movement.py`, written before the edit and read red (no draw today: every admitted journey arrives): `test_each_band_of_move_occurs` (reading (iii): across seeds 0–2 each of `move`'s four bands at least once, `travel.turned_back` emitted), `test_a_partial_migrate_lodges_and_does_not_house` (reading (iv)).
- FALSIFIER and CONTROL: planted, `_eff_move` ignoring `res.degree`: (iii) fails, no `travel.turned_back`; the `legs` argument dropped: a Partial and a Success leave equal `travel_leg` lengths. Control: same seed twice, equal `content_hash`; the `contests:` column removed (B22.06's flat columns): every admitted journey arrives, band `Success` only.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mil_a_movement.py -q` → green: (iii) and (iv) over `aperture 2 s`, s = 0, 1, 2. Not claimed: no rate, no balance (three seeds are three trajectories). The band table is read once by `opus`.
- HASH MOVERS: every seeded world with a journey ("There is no draw today, so every arm of this edit is a mover"; declared; B22's one re-pin).
- DEPENDS ON: V12 B22.07; V12 Batch B07 (`18_DETERMINISM_task_draw_for_uncontested_verbs` item 4: the loader edit; `U5c_VERBS_residue_and_governance_owner` §1: the `a task` prize); V12 Batch B05 (`05_SC_obstacle_difficulty_and_modifiers_B`, `U5c_SC_one_obstacle_form`: `difficulty`, the `favour` source); V12 Batch B12c (`14_VERBS_MATERIAL_B_stores`: the `distance` member and `distance_step`); V12 Batch B04 (`wayfaring`'s definition row, CAP Part A); V12 Batch B19 (`16_PESSIMIST_MB_one_stamina_ledger`).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high; one `opus` read of the band table (reading (iii)).
- LANDS IT: B22's producer; `Item: B22.08`, `[skip ci]`.

### B22.09 — a refusal on `with` teaches the actor · `14_VERBS_MILITARY_A` Edit 6 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_MILITARY_A_movement.md` §3 Edit 6; §1 item 4; owner of the ruling `ED-IN-0282`; `U5b_VERBS_military_physical_residue` §5 ("the `with` deposit (MIL-A Edit 6): one owner: MIL-A carries it once; PHY-A and the SOCIAL verbs cite it").
- ADVANCES: R-05 (the 33 absent-pupil refusals of `train` and the repeated `give`, `surveil`, `capture` refusals stop re-forming).
- INSTRUCTION: `engine/season/data/requires.py`, the stem's world-only flag: `with` leaves the world-only set, so a refusal's read `(subject, with:<actor>, False)` rides `Event.observed` and is deposited to the actor (`observation_deposit_mode: actor`), as `room` is since REM-29. "It is listed here because presence is this family's; it moves `train`, `tend`, `give`, `capture` and `surveil` formation, and the PHYSICAL and SOCIAL families cite the same refusals. Whichever batch lands first carries it once." First, `git grep -n "with" engine/season/data/requires.py` at the batch's open and record whether an earlier batch already carried it; if so this item is dropped and its commit body says which item did.
- WHERE: `engine/season/data/requires.py` (the world-only set).
- TESTS: in `test_vm_mil_a_movement.py`: `test_a_refusal_on_with_is_not_repeated_next_season` (reading (v): a refusal on `with` is followed by no second act of the same `(actor, verb, subject)` in the next season); red before the edit.
- FALSIFIER and CONTROL: the same actor forms the same act on the same absent person the next season. Control: same seed twice, equal hash.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mil_a_movement.py -q` → green; the downstream read of §4 quoted in the commit body: over seeds 0–2, a person who moved to `whereabouts_named`'s rung executes, the next lap or season, an act whose cell asks `with` of the person he went to — one such pair is the artifact; none is "a reading that the chooser does not yet want to (CHAR's), stated as such". (Source "the next round or season" → "the next lap or season", A-101.)
- HASH MOVERS: formation of `train`, `tend`, `give`, `capture`, `surveil` in every seeded world (declared; B22's one re-pin).
- DEPENDS ON: V12 B22.08; EXISTS-IN-TREE `engine/season/data/requires.py` (`REQUIRES_STEMS`, the world-only set); `ED-IN-0282` (the ledger row that owns the ruling).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B22's producer; `Item: B22.09`, `[skip ci]`.

### B22.10 — the siege instruction of `IS-A-09` is carried by B22.11 and B22.12 · `IS-A-09` · POINTER · HASH —
`IS-A-09`'s INSTRUCTION, WHERE, FALSIFIER and GATE are withdrawn by its own Sonnet check ("v12 keeps one item"): the siege is `IS-MB-02` (B22.11, B22.12). Target files and symbols: those of B22.11 and B22.12 (`loop/effects_combat.py::_siege`, `rosters.yaml: march_postures`). Gate: none of its own; what `IS-A-09` still adds is read at the close as B22.R3. Closes G-1 with B22.12.

### B22.11 — a siege that wears nothing still writes; the scenario offers besiege then storm · `IS-MB-02` steps 1, 3, 4, 5, 6 (the policy) · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_B1_PC_MB_DICE_part2.md` `IS-MB-02` (steps 1–6, FALSIFIER, GATE); `IS-A-09` (2); rulings A-81; closes G-1 of `unified/U4_TRACEABILITY.md` §6 (with B22.12); retires v11 CP-T04-06; unblocks `17_CENSUS_C1A_02`'s `_siege` row and `U5d_STORY_owed_edits` §1.
- ADVANCES: R-04, R-05 (a chain whose first link nothing can fire); the *invested* end state.
- INSTRUCTION (in order; the step numbers are the source's; step 2 is B22.12, because the gate's table that decides whether step 2's commit is made reads step 6's policy `[ASSUMPTION: this split of one source item into two commits — basis: IS-MB-02 GATE: "If besieging first wins at least as often … the mover commit of step 2 is not made"]`):
  1. **The roster's own precondition, read first.** `engine/season/rosters.yaml` `march_postures` note says `besiege` joins "in its own declared-mover commit, whose body must state that `restore` executed on a garrison Site in a natural run (seeds 0-2)", because until then "besiege-then-storm dominates storm, since the wear is permanent". Run `python -m engine.season.harness.aperture 2 s`, s = 0, 1, 2, and read `restore`'s `executed` on a garrison Site. `restore` is landed by `14_VERBS_MATERIAL_A_mending` (B12c). If it reads 0 at any seed the item stops (`STOPPED`), with the reading, and nothing below (nor B22.12) ships.
  3. The `march` row and `seam/wrappers/mass_battle.py::resolve` already answer an opposed `besiege` as `Invested` (the roster's note); `loop/effects_combat.py::_siege` (reached from `_eff_march`) wears each garrison Site. No edit; name both in the commit.
  4. **A siege that wears nothing still writes (A-81).** `_siege` returns `NO_CHANGE` when no Site would fall, and the act then reads `march.refused`. Change it so the `siege.pressed` Event (`verb_table.yaml`) is emitted and witnessed whether or not a wall fell, by the mechanism `03_PC_typed_outcome_one_door.md:92` gives an `undecided` fight. `[ASSUMPTION: the durable write is the witnessed claim that the place is besieged — basis: U3 C3-C11's precedent, and `14_VERBS_BINDING_E_war_seats` reads `siege.pressed` claims for its `Besieged` class]`
  5. **The wear is a draw, by its one owner.** `_siege` takes its fall from `loop/effects_economy.py::_fall`, `sabotage`'s formula; the draw on it is SE's (`U5b_MB_residue` §8). Open `_fall`: if it is the drawn form, `_siege` inherits it; if it is still a fixed fraction, this item stops and reports to the SE lane. No second formula is written here. (Read at the tree on 2026-11-12: `_fall` is `(max(0, site.condition) * num) // den`, a fixed commons fraction; it passes only if B12 turns `_fall` into a draw (`16_PESSIMIST_SE_B` / `U5b_MB_residue` §8).)
  6. (Its first half.) Add `besiege_then_storm` to `IS-MB-01`'s `POLICIES` in `engine/season/harness/field_scene.py`. The scenario's `march_postures: [storm, besiege]` override "for this world only" stays until B22.12.
  `IS-A-09` (2): the `march` row's built-out reading counts a besiege that wears nothing but leaves its claim (step 4) as a clean execution, not a refusal.
- WHERE: `engine/season/loop/effects_combat.py` (`_siege`); `engine/season/harness/field_scene.py` (`POLICIES`); `engine/season/tests/test_march.py`.
- TESTS: in `engine/season/tests/test_march.py`, written before step 4: `test_an_opposed_besiege_is_invested_and_wears_the_garrison` (planted garrison; control: `storm` against the same garrison fights a battle; G-1's test; green at control where the field scene's override holds besiege, written on a hand-built world); `test_an_invested_siege_that_wears_nothing_still_leaves_a_claim` (step 4; red before; with the edit reverted the act reads `march.refused`); `test_one_besiege_does_not_ruin_the_walls_at_every_seed` (a rung with one person present, seeds 0–19, `assert checked >= 20`: the garrison's condition is above 0 at some seed; the roster warns that today "a single besiege act zeroes the walls").
- FALSIFIER and CONTROL: the three tests' planted arms. Control: with step 4 reverted, the act reads `march.refused`.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_march.py -q` → the three pass; step 1's reading (`restore` executed on a garrison Site at seeds 0, 1, 2) and step 5's reading (`_fall` drawn) quoted in the commit body; and the table, written in this commit's body and read by `opus` at the batch's close: over `field_scene` seeds 0–39, the `win` share and the seasons taken under `storm` and under `besiege_then_storm`, each with its disjoint-seed control. The arm "`aperture 2 0`: `march` with posture `besiege` formed and executed at least once, `Invested` read" reads the effect of B22.12 and of the armies B22.33 musters: moved to the batch gate (line 4, B22.R3).
- HASH MOVERS: none in the realm (no realm person forms `besiege` while the roster ships `[storm]`); the field scene's worlds move (declared; harness only).
- DEPENDS ON: V12 `14_VERBS_MILITARY_A` edits 1–5 (B22.06–B22.08); V12 `14_VERBS_MATERIAL_A_mending` (Batch B12c: `restore`); V12 `16_PESSIMIST_SE_B` / `U5b_MB_residue` §8 (Batch B12c, B12c.04: `_rise` and `_fall` take the band through `graded_amount`; if not landed, `STOPPED`); V12 `IS-MB-01` and `04_MB_playable_field_scenario` §A (Batch B20: `field_scene.py`, `POLICIES`); EXISTS-IN-TREE `engine/season/loop/effects_combat.py::_siege`, `engine/season/loop/effects_economy.py::_fall`, `engine/season/rosters.yaml: march_postures`.
- GLOSSARY: none (*besiege*, *invested* have rows).
- COST and TIER: edit; `sonnet`, high; the table read by `opus`.
- LANDS IT: B22's producer; `Item: B22.11`, `[skip ci]`.

### B22.12 — `besiege` joins the march's postures · `IS-MB-02` step 2, step 6 (the override's deletion) · BUILD · HASH MOVER(behaviour)
- SOURCE: `master/instructions/IS_B1_PC_MB_DICE_part2.md` `IS-MB-02` steps 2 and 6, GATE ("If besieging first wins at least as often at every seed and costs nothing the table can show, the mover commit of step 2 is not made and the close says why"); closes G-1.
- ADVANCES: R-04, R-05 (`march` with posture `besiege`).
- INSTRUCTION:
  0. Read B22.11's table. If besieging first wins at least as often at every seed and costs nothing the table can show, this item is not made; the commit body of the batch close says why and quotes the table, and the B22.R3 arm "`besiege` formed and executed" is then read as not built out with that reason (a failed gate of IS-A-08, reported, not a silent pass).
  2. `rosters.yaml: march_postures.values`: `[storm]` becomes `[storm, besiege]`, in its own commit, declared as a mover. `choice_sourced` already ranges `march`'s `posture` over this roster, so `_fanned_choices` (`decision/options.py`) begins to form a `besiege` Candidate with no further edit. The commit body states B22.11 step 1's reading (`restore` executed on a garrison Site in a natural run, seeds 0–2), as the roster's note requires.
  6. (Its second half.) Delete the scenario's `march_postures: [storm, besiege]` override "for this world only" (`04_MB_playable_field_scenario` §A) in `engine/season/harness/field_scene.py`: the roster now ships both.
- WHERE: `engine/season/rosters.yaml` (`march_postures.values` and its note's "SHIPPED `[storm]`" line); `engine/season/harness/field_scene.py` (`build`'s `Fixtures` override).
- TESTS: none new; B22.11's three stay green.
- FALSIFIER and CONTROL: the table above. Control: same seed twice, equal hash.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_march.py engine/season/tests/test_field_scene.py -q` → green; `python -m engine.season.harness.aperture 2 0` → a `march` Candidate with `posture: besiege` formed (quoted); its execution is read at the batch gate after B22.33 (armies exist only then).
- HASH MOVERS: any seeded realm in which a chooser forms `besiege` (declared; B22's one re-pin, B22.35).
- DEPENDS ON: V12 B22.11 and its table.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B22's producer; `Item: B22.12`, `[skip ci]`.

### B22.13 — `train` is a lesson that may or may not take · `14_VERBS_MILITARY_B` Edits 1–4 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_MILITARY_B_train.md` §3 Edits 1–5, §4; "Standing" (A-5, A-6, A-7, A-8, A-25, A-30, A-81); A-11 (training gates no act), A-2 (a drilled cohort is a person at weight).
- ADVANCES: R-04.c1 (`train`); R-05 (`train` built out).
- INSTRUCTION:
  1. Edit 1 — `engine/season/verb_table.yaml`, the `train` row, final text of the changed columns (eligibility, beneficiary, cell and their notes stand):
     ```yaml
         referent_class: Person
         contests:    "a task"        # shape (b): three kinds across the bands (VRES §1)
         difficulty:  routine
         referent_class_note: "14-VM-B: FORMED ONLY ON A `Person`-CLASSED REFERENT -- the person the question he answers is about, himself included (`queries/world_q.py::own_referents_of_class`). The class removes the 39-of-85 formations on a Record, a place or a Proposition and claims no execution. The teacher's own skill is NOT read here: skill gates nothing (#353 §9.2, probe P11). REVERT: delete this column."
         writes:
           Overwhelming: ["Person.capability"]
           Success:      ["Person.capability"]
           Partial:      []
           Failure:      []
         writes_note: "14-VM-B: ONE RANK ON THE TWO UPPER BANDS (`raised_capability`, minting per `01_CORE_capability_authoring_surface.md` Edit 9). Partial writes nothing and emits `training.practised`, a kind `queries/world_q.py::practice` counts as a good result for the LEARNER in the skill carried (CR-18's addend), so a lesson that did not take still leaves him readier. Failure: `training.fruitless`. At the ceiling of the skill's scale the effect declines (`train.refused`, the read `(subject, capability:<kind>, <rank>)` on the Event). [ASSUMPTION; medium; Jordan to correct; revert: the flat write.]"
         emits:
           Overwhelming: ["capability.raised"]
           Success:      ["capability.raised"]
           Partial:      ["training.practised"]
           Failure:      ["training.fruitless"]
         emits_on_refusal: ["train.refused"]
     ```
  2. Edit 2 — `engine/season/rosters.yaml`: no `graded_inquiries` line (`train` is a contest row on the `a task` prize). The pool key is the skill the act carries (`vocation_sourced: {train: kind}`, unchanged): the roll's input builder reads the one pool reader (`pool.py`, over `sigma_leverage.pool_of`, D-U1-08) on `a.payload[kind]` for a row `vocation_sourced` names, and `verb_capability` gains no `train` line — one clause in `seam/wrappers/sigma.py::contest_input` (the one input builder), reading the roster, never the verb's name. Obstacle and leverage through the one composer: `train` | `routine` | obstacle terms `learner_rank` (the subject's effective rank in the skill, 1 at least) · `self_taught` (subject is the actor) · `no_training_place` (no Site or venue of a kind the skill row's `trained_at` lists where they stand) · `teacher_no_better` (the actor's rank does not exceed the subject's; not applied to self-teaching) | leverage `learner_regards_teacher`: a `favour` level (a positive stance row of the subject toward the actor; C3-C10). The four terms and the level ship absent (0) until B22.01's design names them: the control is `routine`. U1's skill rows (`references/descriptor_registry.yaml: capabilities`, D-U1-07) gain one optional column, `trained_at: [site or venue kinds]` (`arms: [barracks, garrison]`, `copying: [archive]`; content, Jordan's; listed in the PR body); until that column holds a value the term reads an empty list and applies everywhere.
  3. Edit 3 — `engine/season/loop/effects_combat.py::_eff_train(w, a, res)`:
     ```python
     who, key = _operand(a, "subject"), _operand(a, VOCATION_SOURCED[a.verb])
     p = w.persons.get(who)
     if p is None or key not in VOCATIONS:            return NO_CHANGE          # as now
     raised = raised_capability(p, key)               # mints per CORE Edit 9; None at the ceiling
     if raised is None:                               return NO_CHANGE
     return Change((Subject.entity("persons", who, fields=("capability",)),), set_capability)
     ```
     The effect is reached only at Overwhelming and Success: `loop/resolve.py` computes `row.writes_at(degree)` and calls the effect only when that list is non-empty, so a `Partial: []` or `Failure: []` band emits its kind and never runs `_eff_train`.
  4. Edit 4 — `engine/season/queries/world_q.py::practice`: its set of counted kinds gains `training.practised`, read off the `train` row's `Partial` emit (`VERB_TABLE["train"].emits_at`), never a literal; the credit is the subject's, in the skill the causing act carried.
  5. Edit 5 — not edited here: `rosters.yaml: tables.alignment` cells for `train` are CHAR's (`02_CHAR_choice_alignment.md`); until they exist the row stays out of the corpus ranking. Draw: `H(w.world_seed, w.tick, <actor id>, "train.task")` (A-30).
- WHERE: `engine/season/verb_table.yaml` (`train`); `engine/season/rosters.yaml` (composer rows for `train`); `engine/season/seam/wrappers/sigma.py` (`contest_input`, one clause); `references/descriptor_registry.yaml` (`capabilities`: `trained_at`, optional column); `engine/season/loop/effects_combat.py` (`_eff_train`); `engine/season/queries/world_q.py` (`practice`); NEW `engine/season/tests/test_vm_mil_b_train.py`.
- TESTS: NEW `engine/season/tests/test_vm_mil_b_train.py` (one function per §4 reading; the scratch probe `probe_army.py` restated as reading (ii)'s function, U3 §6.2's rule), written before Edit 1 and read red: `test_capability_raised_is_emitted_and_no_train_refused_on_existence` (i), `test_a_lesson_has_four_bands` (ii: a hand-built lesson through the fold on `build_realm(0)`, 200 seeds; all four bands occur; the learner's pool after a first rank is not below `pool_default`), `test_a_better_teacher_raises_more_often` (iii: teacher at 5 against none, n 200 each, same-run control; the share of the two upper bands differs beyond sampling error), `test_a_new_rank_widens_the_next_pool` (iv: a learner who gained a rank in `argue` rolls a pool one larger in his next `argue`).
- FALSIFIER and CONTROL: planted, `_eff_train` ignoring `res.degree`: (ii) shows two bands only; the `teacher_no_better` row at 0: (iii) shows no difference (read once B98 sets the term; until then (iii) reads the pool's own difference); `training.practised` left out of `practice`'s kinds: a Partial lesson leaves the learner's next pool unchanged. Control: `Fixtures practice_cap: 0` and the `contests:` column removed (flat write): every admitted lesson raises one rank.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mil_b_train.py -q` → green; (i) over `aperture 2 s`, s = 0 to 2: `capability.raised` out of the never-emitted list at one seed at least; `train`'s refusals read 0 on `exists:Person`. Reading (iii) read once by `opus`.
- HASH MOVERS: formation (the class) and every executed `train` (declared; B22's one re-pin).
- DEPENDS ON: V12 B22.09 (the `with` deposit, on which the 33 absent-pupil refusals depend); V12 `01_CORE_capability_authoring_surface` Edit 9 (Batch B04); V12 `05_SC_obstacle_difficulty_and_modifiers_B`, `U5c_SC_one_obstacle_form` (Batch B05); V12 `U5c_VERBS_residue_and_governance_owner` §1, `18_DETERMINISM_task_draw_for_uncontested_verbs` item 4 (Batch B07); EXISTS-IN-TREE `engine/season/loop/effects_combat.py::_eff_train`, `engine/season/queries/world_q.py::practice`, `::own_referents_of_class` `[ASSUMPTION: present — the source cites it; not opened by this lane]`.
- GLOSSARY: none new (the prose word is *skill*; `Person.capability` keeps its name, D-06). The two copied note strings of Edit 1 say *skill* where the source said *capability* (A-98); identifiers (`raised_capability`, `capability.raised`, `capability:<kind>`) are unchanged.
- NAMES: `VOCATIONS`, `VOCATION_SOURCED`, `vocation_sourced`, `pool.py::faculty` → read at the tree as B04 (CAP A2/A3, D-U1-08) left them `[ASSUMPTION: CAP A3 derives VOCATIONS from the skill rows or deletes it; the producer composes on the owner B04 left]`; `faculty` → the skill score read through the skill table (B15, `IS-PC-05`).
- COST and TIER: small build; `sonnet`, high; one `opus` read of reading (iii).
- LANDS IT: B22's producer; `Item: B22.13`, `[skip ci]`.

### B22.14 — the army module answers how many men each cohort has under arms; who is away · `07_SE_campaign_supply_and_muster` (a), (b) · BUILD · HASH EQUAL
- SOURCE: `proposals/07_SE_campaign_supply_and_muster.md` §4 (a), (b); R-SE-33, R-SE-34; rulings A-69, A-78, J-C-2; C3-L11; closes the direction of H-212 with B22.16.
- ADVANCES: none by itself (the readers B22.15 and B22.16 call).
- INSTRUCTION:
  1. (a) Army module (owner: MB) — one query entry. `mass_battle.under_arms`: input the `army` Records' `subject_matter` in id order; output `((cohort id, weight units), ...)`, the troops each cohort has under arms rounded *up* to whole weight units by the module's own `TROOPS_PER_WEIGHT`. The module owns its record shape and its constant; the host learns neither. The strength it reads is the Record's present strength after the losses a field wrote, with the recoverable share added as MB's reader computes it when read (`world_q.army_strength`, B22.05); a recovered man returns to the Record, never to `Person.weight` (J-C-2). Registered as a composition row in `references/module_contracts.yaml` with `entry: query` (the `settlements.larder_draw` and `settlements.provision` rows are the precedent), and declared in `world_q.QUERY_ENTRIES` so `manifest/registrar.py::require_entries` refuses its absence. SITE (the source's `[UNVERIFIED: the Record's per-cohort field]`): first open `modules/mass_battle/armyrecord.py` and record in the commit body the field that holds per-cohort troops (`world_q.other_army_records` and `recruit_limit`'s `raised` argument show it is held), then the edit.
  2. (b) `engine/season/queries/world_q.py` — two readers:
     ```python
     def under_arms(w: World) -> dict:          # {cohort id: weight units}; {} when no army holds troops
     def away(w: World) -> dict:                # {cohort id: (weight units, treasury rung)}: the part of
                                                # `under_arms` in an army whose holder's `march_origin` is a
                                                # place `holder_faction_of` gives to another faction, with the
                                                # treasury of the march that brought it there
     ```
     The treasury is read off the log on the pattern `world_q.siege_pressed_by` already uses (the latest Event of a `march` kind whose causing act is a `march` by this holder; that act's `via` office's rung, which is what `seam/wrappers/mass_battle.py::_seat_treasury` returns at field time). `siege_pressed_by` itself reads this season's sieges only and is not reused; no state is added to the army Record.
- WHERE: `modules/mass_battle/armyrecord.py` or the module's query entry file (the `under_arms` entry; `TROOPS_PER_WEIGHT` read, not restated); `references/module_contracts.yaml` (one composition row, `entry: query`); `engine/season/queries/world_q.py` (`QUERY_ENTRIES`; NEW `under_arms`, `away`).
- TESTS: NEW `engine/season/tests/test_standing_ration.py` (U3 §6.1: MISSING; written in this item, before the edit, as the source's hand-built world: a cohort of weight 6 at a field town, 300 troops raised from it into an army, one weight unit), with `test_under_arms_counts_the_raised_troops_in_weight_units` and `test_away_names_the_treasury_of_the_march` — red before (no reader).
- FALSIFIER and CONTROL: `under_arms` reporting troops that no army Record holds. Control: the realm at seeds 0 to 2 equal (no army exists at shipped fixtures).
- GATE: `python -m pytest engine/season/tests/test_standing_ration.py -q` → the two pass; `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`) (the registrar refuses an absent entry).
- HASH MOVERS: none.
- DEPENDS ON: V12 B22.05 (`army_strength`); EXISTS-IN-TREE `engine/season/queries/world_q.py::QUERY_ENTRIES`, `::siege_pressed_by`, `::holder_faction_of`, `::other_army_records`, `engine/season/seam/wrappers/mass_battle.py::_seat_treasury` `[ASSUMPTION: present — cited by the source, not opened]`, `references/module_contracts.yaml` rows `settlements.larder_draw`, `settlements.provision`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B22's producer; `Item: B22.14`, `[skip ci]`.

### B22.15 — a soldier is not a farmer while he is a soldier · `07_SE_campaign_supply_and_muster` (c) · BUILD · HASH EQUAL
- SOURCE: `proposals/07_SE_campaign_supply_and_muster.md` §4 (c); R-SE-33.
- ADVANCES: none of its own (an arm shipped off).
- INSTRUCTION: CP-T08-01's `labour(w, rung)` (`queries/world_q.py`): the sum over presence becomes `(weight − under_arms.get(pid, 0)) × body / body_scale`, floored at 0. One term in one function; read only under CP-T08-01's `labour_mode`.
- WHERE: `engine/season/queries/world_q.py` (`labour`).
- TESTS: in `engine/season/tests/test_standing_ration.py`: `test_the_home_rung_labour_falls_by_the_hands_under_arms` (with `labour_mode` on: the home rung's labour is five units while the army is raised, six when it is disbanded); red before.
- FALSIFIER and CONTROL: labour unchanged by troops raised. Control: `labour_mode` off: hashes equal.
- GATE: `python -m pytest engine/season/tests/test_standing_ration.py -q` → green.
- HASH MOVERS: none at `labour_mode` off.
- DEPENDS ON: V12 B22.14; V12 B12c.02 (CP-T08-01, the intake's B12 entry `:313`: `labour(w, rung)` and `labour_mode`) — if `labour` is not in the tree at this item's turn, the item is `BLOCKED (SE: CP-T08-01's labour reader)` and the batch reports it.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B22's producer; `Item: B22.15`, `[skip ci]`.

### B22.16 — an army away from home eats from its holder's treasury · `07_SE_campaign_supply_and_muster` (d), (e), (g) · BUILD · HASH EQUAL
- SOURCE: `proposals/07_SE_campaign_supply_and_muster.md` §4 (d), (e), (g); §5; R-SE-34, R-SE-36; A-57, A-58, A-66, A-67 (the U5d fold); H-212.
- ADVANCES: none of its own (an arm shipped off); H-212's direction.
- INSTRUCTION:
  1. (d) `larder_input` (`queries/world_q.py::_larder_parts`): when `standing_ration` is on, an `Eater`'s weight is `person.weight − away.get(pid, (0, None))[0]`. The module (`larder_draw`) is unchanged.
  2. (e) `engine/season/loop/matter.py`, after the subsistence pass and before yield, when `standing_ration` is on: group `away` by treasury; for each, `p = provision(provision_input(w, Σ weight units, treasury))` (the existing entry, by role string) and debit `p.consumed` from the treasury through the owner of debits, emitting `stores.changed`; where `p.troops < Σ weight units` the write carries a `shortfall:<kind>` Observation exactly as a drained larder's does. Nothing else is written. MATTER reads the army Records and the march only through the `world_q.away` Query, as it already reads `body_hazard` and `residence_of` (R3 §1 (e), Option A). The debit at RESOLVE is not taken.
  3. (g) `engine/season/data/fixtures.py`: `standing_ration=False`; H-212's row in `engine/season/hole_register.yaml` gains the arm and stops reading `absent`.
- WHERE: `engine/season/queries/world_q.py` (`_larder_parts`); `engine/season/loop/matter.py` (the standing-ration pass); `engine/season/data/fixtures.py` (`standing_ration`); `engine/season/hole_register.yaml` (H-212's row).
- TESTS: in `engine/season/tests/test_standing_ration.py`, written before the edit and read red: `test_an_army_away_eats_from_its_treasury_and_not_at_home` (the source's execution artifact: marched to a settlement another faction holds and left there two seasons with `labour_mode` and `standing_ration` on; each MATTER the treasury falls by one weight unit's ration, the home cohort's `want` is five units' worth; marched home, the treasury stops falling and the want returns to six); `test_a_head_eats_once` (conservation: in every season the units eaten at home plus the units eaten from the treasury equal the whole cohort's want when both are stocked); `test_no_debit_from_the_occupied_settlement_or_on_own_land`.
- FALSIFIER and CONTROL: a season in which the sum is more (a head eating twice) or less with both stocked; a debit from the occupied settlement's stores; a debit while the army stands on its own faction's land. Mutation: read `under_arms` where `away` is meant in (d), and the army at home goes unfed. Control: all three arms off reproduce the shipped hashes.
- GATE: `python -m pytest engine/season/tests/test_standing_ration.py engine/season/tests/test_levy_feed.py -q` → green (two seasons).
- HASH MOVERS: none at `standing_ration` off ("each flip a declared mover in its own commit"; no flip in this batch).
- DEPENDS ON: V12 B22.14; EXISTS-IN-TREE `engine/season/queries/world_q.py::_larder_parts`, `engine/season/loop/matter.py`, the `settlements.provision` entry and `provision_input` `[ASSUMPTION: present — cited by the source]`. IN-52's flip (`field_provisioning`): untouched ("a field's ration and the standing ration are two calls to one entry on one stock").
- GLOSSARY: row *standing ration* (new): "the grain an army away from its own land eats from its lord's treasury each season"; owner `data/fixtures.py: standing_ration` and `loop/matter.py`.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B22's producer; `Item: B22.16`, `[skip ci]`.

### B22.17 — a fortress trains foot; training Sites stand where the realm's venues name them · `07_SE_campaign_supply_and_muster` (f) with `U5b_MB_residue` §3 · BUILD · HASH EQUAL
- SOURCE: `proposals/07_SE_campaign_supply_and_muster.md` §4 (f), §5 "For (f)", R-SE-35; `proposals/U5b_MB_residue.md` §3 (addendum R-44, first audit R-07): "plants each training Site at the settlement whose venue already carries the name (`b_s_014_barracks`, `b_s_007_barracks`), so one place is one thing"; U3 §1 item 22 ("with `U5b_MB_residue`'s realm item").
- ADVANCES: none of its own (an arm shipped `uniform`).
- INSTRUCTION:
  1. `engine/season/rosters.yaml`, beside the first lane's `site_endowment`, one table read by the same loader:
     ```yaml
       training_endowment:
         source: "proposals/2026-11-12-subsystem-audit-suite/proposals/07_SE_campaign_supply_and_muster.md; ED-IN-0306"
         keys: [settlement types (the geography file's `type`), site_kinds]
         uniform: {}                                   # the control: today's realm, no training Site
         ground:                                       # [ASSUMPTION; medium; Jordan to correct; revert: {}]
           Fortress:      [barracks]
           Fortress-City: [barracks]
     ```
  2. `engine/season/boot/realm.py` (the builder after B03c; the source's `harness/populated.py::build_realm`) mints one Site per entry at full condition in the loop that mints garrisons, under `endowment_mode == "ground"`. Each minted training Site at a settlement whose venue already carries the name (`engine/season/npcs.yaml`'s `b_s_014_barracks`, `b_s_007_barracks`) is that venue's Site, so one place is one thing (`U5b_MB_residue` §3).
  3. The loader refuses a type the geography file does not use and a kind outside `site_kinds`.
- WHERE: `engine/season/rosters.yaml` (`training_endowment`); `engine/season/boot/realm.py` (the garrison-minting loop); `engine/season/data/rosters.py` (the `site_endowment` loader, two refusals).
- TESTS: in `engine/season/tests/test_standing_ration.py` (or the endowment test B12c wrote, `test_endowment.py`, beside its `site_endowment` cases): `test_ground_plants_a_barracks_at_each_fortress` (under `ground`, `training_sites` for the cohort at S-014 returns a `barracks` at scale and `recruit_limit('spearmen', …)` there is positive, while at a town it is 0; under `uniform` both are 0); `test_training_endowment_refuses_an_unknown_type_and_kind`; red before.
- FALSIFIER and CONTROL: a `barracks` minted under `uniform`; a second Site minted where a venue already names one. Control: `uniform` reproduces the shipped hashes.
- GATE: `python -m pytest engine/season/tests/test_standing_ration.py engine/season/tests/test_endowment.py -q` → green; under `ground`, `armyrecord.options` on that realm offers a trained kind beside levy (`U5b_MB_residue` §3's gate), quoted in the commit body.
- HASH MOVERS: none at `endowment_mode: uniform` ("Movers. Declared, at SE's landing": the `ground` flip is `07_SE_ground_and_granaries`', not this batch's).
- DEPENDS ON: V12 B22.16; V12 `07_SE_ground_and_granaries` (Batch B12c: `endowment_mode`, `site_endowment` and its loader); V12 Batch B03c (`boot/realm.py`); EXISTS-IN-TREE `engine/season/queries/world_q.py::training_sites`, `engine/season/npcs.yaml` venue `b_s_014_barracks` (`:114`).
- GLOSSARY: none.
- NAMES: `harness/populated.py::build_realm` → `boot/realm.py` (B03c).
- COST and TIER: small build (data); `sonnet`. The two-row table is authored content listed in the PR body.
- LANDS IT: B22's producer; `Item: B22.17`, `[skip ci]`.

### B22.18 — the army record carries a doctrine and a footing, and steps toward them · `14_VERBS_MILITARY_C` Edit 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/14_VERBS_MILITARY_C_the_muster.md` §3 Edit 1; the 27-lane fold (A-69: what the army holds of a cohort counts absent men); U3 §1 item 22.
- ADVANCES: none of its own (the module half of the muster).
- INSTRUCTION (`modules/mass_battle/armyrecord.py`; owner MB, reviewed by it):
  1. `KEYS = ('faction', 'strategy', 'trained', 'units', 'doctrine', 'footing')`; `new(faction, strategy='line', doctrine=DEFAULT_DOCTRINE, footing='peace')`; `validate` accepts a record lacking the two new keys as carrying the defaults (no minted Record exists in any shipped world); `rosters.yaml: record_kinds.army` mirrors the six. (The source's `'subformations'` is `'units'` after B16L.)
  2. `target(record, cohorts, full, others) -> {(cohort, troop_type): count}`: the doctrine's shares (`references/troops.yaml: doctrines` once B22.32 moves them; `troop_types/presets.py::ARM_SHARES` until then) of each cohort's `under_arms_cap`, times the footing's share (`FOOTING_SHARE = {'peace': 0.25, 'war': 1.0}`, `[ASSUMPTION; medium; Jordan to correct; revert: 1.0 for both]`), each entry bounded by `recruit_limit`. What the army holds of a cohort counts its absent men (`cohort_claims`, B22.02).
  3. `step(record, op, facts) -> ((op, args), ...)`: the primitive commands a payload-less `op` stands for. `recruit`: `target − by_type`, per cohort, positive entries. `discharge`: `by_type − target`, plus every trooper of a cohort absent from `facts.cohorts`, plus the excess over a cohort's present cap; unassigned first, then released from the largest unit.
  4. `_apply`: an op whose `args` carry no command key runs `step` and folds its commands in order; `args['share']` (the host's `rosters.yaml: task_fraction` value for the band, read through `loop/effects_shared.py::graded_amount`'s table and never restated) scales each count, rounding up.
  5. `options(q)` gains three keys beside `raise` and `advisories`: `muster_room` (bool: `step('recruit')` is non-empty), `surplus` (bool: `step('discharge')` is non-empty), and the three booleans `14_VERBS_MILITARY_D` reads (B22.24). One function decides what the menu shows and what the cell asks.
- WHERE: `modules/mass_battle/armyrecord.py` (`KEYS`, `new`, `validate`, NEW `target`, NEW `step`, `_apply`, `options`); `engine/season/rosters.yaml` (`record_kinds.army`).
- TESTS: in `tests/valoria/test_mass_battle_army_record.py`, written first: `test_step_recruit_is_target_less_held`, `test_step_discharge_releases_unassigned_first`, `test_share_scales_each_count_rounding_up`, `test_a_record_without_doctrine_and_footing_validates_with_the_defaults`; red before.
- FALSIFIER and CONTROL: planted, `share` ignored in `_apply`: Partial raises 60 (read in B22.21's gate). Control: realm hash at seeds 0 to 2 equal (no caller).
- GATE: `python -m pytest tests/valoria/test_mass_battle_army_record.py tests/valoria/test_army_verbs.py -q` → green.
- HASH MOVERS: none.
- DEPENDS ON: V12 B22.02 (absent men), B22.17; V12 B12c.04 (`engine/season/loop/effects_shared.py::graded_amount`: absent from the tree today, created by B12c.04); EXISTS-IN-TREE `modules/mass_battle/armyrecord.py::KEYS`, `::_apply`, `::options`, `modules/mass_battle/troop_types/presets.py::ARM_SHARES`.
- GLOSSARY: rows *doctrine* and *footing* (new if absent): *doctrine* "the share of each kind of troop an army is raised to"; *footing* "whether an army is kept at peace strength or war strength"; owner `armyrecord.KEYS`.
- NAMES: `subformations` → `units` (B16L, L1-1).
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B22's producer; `Item: B22.18`, `[skip ci]`.

### B22.19 — one reader of an army's state as its commander may command it · `14_VERBS_MILITARY_C` Edit 2 · BUILD · HASH EQUAL
- SOURCE: `proposals/14_VERBS_MILITARY_C_the_muster.md` §3 Edit 2; G-04 (`audits/25_GROUNDING_ENGINE.md`).
- ADVANCES: none of its own (the reader the six army rows ask).
- INSTRUCTION:
  1. `engine/season/queries/world_q.py`:
     ```python
     def army_state(w: World, rid: str, actor: str) -> dict:
         """The module's `options` for the army `rid` as `actor` may command it: `ArmyOptionsQuery(record,
         cohorts the actor may levy (state/gate.py::may_levy through his muster seat), full, others)`.
         The one reader the six army rows' third conjunct asks; `harness/military_menu.py::menu` calls it."""
     ```
     `other_army_records` is unchanged.
  2. `data/requires.py: REQUIRES_STEMS` gains the relation stems `muster_room` and `surplus`, asked `of: subject` and the actor (`room`'s shape), answered by `army_state`; neither is world-only, so a refusal's read is deposited to the actor.
  3. `harness/military_menu.py::menu` calls `army_state`.
- WHERE: `engine/season/queries/world_q.py` (NEW `army_state`); `engine/season/data/requires.py` (`REQUIRES_STEMS`); `engine/season/harness/military_menu.py` (`menu`).
- TESTS: in NEW `engine/season/tests/test_vm_mil_c_muster.py` (one function per §4 gate), written first: `test_army_state_reads_the_cohorts_the_seat_may_levy` (planted, `may_levy` replaced by `raisable_by`: FA's seatless-member probe executes again); red before.
- FALSIFIER and CONTROL: a seatless member's cohort counted. Control: hashes equal.
- GATE: `python -m pytest engine/season/tests/test_vm_mil_c_muster.py tests/valoria/test_army_menu_presets.py -q` → green.
- HASH MOVERS: none.
- DEPENDS ON: V12 B22.18; V12 `06_FA_levy_through_the_seat_B` (Batch B21: `state/gate.py::may_levy`, `may_wage`); EXISTS-IN-TREE `engine/season/queries/world_q.py::other_army_records`, `::raisable_by`, `engine/season/harness/military_menu.py::menu`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B22's producer; `Item: B22.19`, `[skip ci]`.

### B22.20 — a held Record forms only the rows that ask for its kind · `14_VERBS_MILITARY_C` Edit 3 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_MILITARY_C_the_muster.md` §3 Edit 3 ("Declared mover for `carry`, `comply`, `found`, `build`").
- ADVANCES: R-05 (REM-25's wrong-kind residue stops: 2 / 3 / 2 refusals a season at seeds 0 to 2).
- INSTRUCTION: `engine/season/decision/options.py::opening_set`: after `refs = row.referents_of(q)`: for a row whose class is `Record` and whose cell asks `existence` of a record sub-kind and `held_by` of `subject` (read off the cell, `data/verbs.py::_asks_subject_held`, never a verb name), keep only the referents whose `content:<kind>` claim in the person's own ledger is of an asked kind. New helper beside `held_record_claims`: `held_record_kinds(p) -> {record id: kind}` (the same read without the `record_sourced_operands` filter). SITE (the source's `[UNVERIFIED]`): first check whether a minter's ledger receives `content:army` in season (WITNESS's fourth deposit, `loop/witness.py`, reads `newly_held`) and record the finding in the commit body; if it does not, the mint's Event is added to `newly_held`'s sources; no other deposit is proposed.
- WHERE: `engine/season/decision/options.py` (`opening_set`; NEW `held_record_kinds`); `engine/season/data/verbs.py` (`_asks_subject_held`, if not present: read only otherwise); `engine/season/loop/witness.py` (only if the SITE step finds it needed).
- TESTS: in `test_vm_mil_c_muster.py`: `test_a_held_record_of_another_kind_is_not_a_referent`; red before.
- FALSIFIER and CONTROL: `carry`, `comply`, `found`, `build` still refused on a Record of the wrong kind. Control: same seed twice, equal hash.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mil_c_muster.py -q` → green; `aperture 2 s`, s = 0 to 2 → the wrong-kind refusals of `carry`, `comply`, `found`, `build` read 0 (before: 2 / 3 / 2 a season, `reading @<sha>`).
- HASH MOVERS: formation of `carry`, `comply`, `found`, `build` in every seeded world (declared; B22's one re-pin).
- DEPENDS ON: V12 B22.19; EXISTS-IN-TREE `engine/season/decision/options.py::opening_set`, `::held_record_claims` `[ASSUMPTION: present — cited]`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B22's producer; `Item: B22.20`, `[skip ci]`.

### B22.21 — `recruit` and `discharge_troops` are task rows on `command` · `14_VERBS_MILITARY_C` Edits 4, 5 · BUILD · HASH EQUAL
- SOURCE: `proposals/14_VERBS_MILITARY_C_the_muster.md` §3 Edits 4 and 5; §4; "Standing" (A-5, A-6, A-7, A-8, A-25, A-30, A-59, A-81; D-U1-01); `U5b_VERBS_military_physical_residue` §1 (shape (a)); G-04.
- ADVANCES: R-05 (`recruit`, `discharge_troops` built out, read at the batch gate after B22.33); the edits ride one commit `[ASSUMPTION: the grouping — basis: the source orders Edits 4 and 5 and names no commits; a row in `graded_tasks`, its `draw` clause and the effect that reads the band are one loadable state]`.
- INSTRUCTION:
  1. Edit 4 — `engine/season/verb_table.yaml`, `recruit`, final text of the changed columns:
     ```yaml
       - verb:        "recruit"
         stratum:     "uncontested_material"
         eligibility: ["remit:dispatch"]
         beneficiary: "none"
         referent_class: Record
         referent_class_note: "14-VM-C: FORMED ONLY ON AN `army` RECORD THE PERSON HOLDS -- `records_held_for_holding_rows` stamps it (`HOLDING_RECORD_KINDS` derives `army` off this cell), and `opening_set` keeps a held Record only where his own `content:` claim is of the asked kind. REVERT: delete this column; the row is hand-built only, as before."
         requires:    "the subject is an army record the actor holds, and the army may raise more men from cohorts his seat may levy"
         requires_typed:
           all:
             - form:      existence
               of:        subject
               kind:      army
               conjunct:  army
             - form:      relation
               of:        subject
               relation:  held_by
               conjunct:  command
         capability:  command          # U1 capability architecture §5; `27_MB_A` §1 defines it
         difficulty:  routine
         writes:      ["Record.subject_matter"]   # shape (a): one cell, the band scales the count
         writes_note: "14-VM-C: `armyrecord.apply` with `share` = `task_fraction[band]` (1, 1, 0.5); a failed draw writes nothing and emits `levy.shirked` (the `draw` refusal clause). A payload naming `cohort`, `troop_type`, `count` is one levy; none is the doctrine's step (`armyrecord.step`). The seat's right over the cohort is `state/gate.py::may_levy` (FA). [ASSUMPTION; medium; Jordan to correct; revert: the flat write without the draw.]"
         emits:       ["army.recruited"]
         emits_on_refusal:
           eligibility: ["recruit.unauthorized"]
           army:        ["recruit.refused"]
           command:     ["recruit.refused"]
           write:       ["recruit.refused"]
           draw:        ["levy.shirked"]
         refusal_note: "KEYED PER CLAUSE. `room` is not a typed conjunct (G-04): it is asked at formation (`belief_contradicts`) and by the effect for a payload-less act, and refused under `write`; its read `(army, muster_room:<actor>, False)` rides the Event and is deposited to the actor, so a commander at strength does not call the levy again until he learns otherwise (REM-29's limit applies and is `01_CORE_claim_fade_as_read.md`'s to lift). `write` also covers a payload the module refuses (an unknown kind, a count over the cap), or a cohort the seat may not levy."
         grade:       "assumption"
     ```
     `discharge_troops`: the same row with `surplus` (asked as `room` is) for `muster_room`; flat `emits: ["army.discharged"]`; `draw: ["discharge.balked"]`; refusal kinds `discharge_troops.unauthorized` and `discharge_troops.refused`. A spoken command (a payload naming cohort, kind and count) is bounded by the cap alone, in the effect.
  2. Edit 5 — `rosters.yaml: graded_tasks.values` gains `recruit` and `discharge_troops` (shape (a)); the skill is each row's own `capability: command` cell (D-U1-07), not a `verb_capability` line; `army_verbs` is unchanged. Obstacle and leverage through the one composer: `recruit` | `routine` | obstacle `muster_difficulty` (by troop kind: a column of the troop table; until it lands, 1 for a kind with no training Site, 2 for one with, 3 where `TRAINING_SITE`'s floor is above 0) · `cohort_resents` (the cohort holds a negative stance row toward the faction; for a doctrine step, any cohort in the step) · `larder_short` · `half_under_arms` | leverage `cohort_committed` · `footing_war`; `discharge_troops` | `routine` | obstacle `arrears` (a live ration `shortfall` on the army's treasury) · `on_foreign_ground` | leverage `levy`. Every term and level ships absent (0) until B22.01's design names it: the control is `routine`.
  3. `loop/effects_army.py`: `_eff_recruit(w, a, res)` and `_eff_discharge_troops(w, a, res)` are reached only on a won draw; they build `args` as now, adding `share` (`task_fraction[res.degree]`) and, when the payload names no command, `cohorts` (`may_levy`'s set with weights and sites). Every army Event carries `Observation(rid, "muster_room:<actor>", bool)` and `Observation(rid, "surplus:<actor>", bool)` read from `army_state` after the write.
  4. `data/verbs.py::act_key` and `opportunity_key`: for a verb in `ARMY_VERBS` whose operands carry a command key, the key gains a digest of the command (the choice suffix's shape), so the menu may give several spoken commands a season; a doctrine step carries none and is once a season (MB R-17's disposition). This is the one such edit (`04_MB_playable_field_scenario` §E names it and does not repeat it).
  5. Draws: `H(w.world_seed, w.tick, <actor id>, "recruit.task")`, `"discharge_troops.task"` (A-30). A-81: `levy.shirked` and `discharge.balked` are refusal Events witnessed by the commander and the cohort persons at the muster rung.
- WHERE: `engine/season/verb_table.yaml` (`recruit`, `discharge_troops`); `engine/season/rosters.yaml` (`graded_tasks.values`; composer rows; `observation_terms` gains `muster_room`, `surplus` if absent); `engine/season/loop/effects_army.py` (`_eff_recruit`, `_eff_discharge_troops`); `engine/season/data/verbs.py` (`act_key`, `opportunity_key`).
- TESTS: in `test_vm_mil_c_muster.py`, written first and read red: `test_a_levy_has_four_bands` (a hand-built run on `build_realm(0)`, 200 seeds, one levy of 60: all four bands occur; the counts on the roll are 60, 60, 30, 0 by band); `test_a_resented_seat_is_shirked_more_often` (a seat whose cohort holds a negative stance row toward the faction against one with none, n 200 each, same-run control; read once B98 sets `cohort_resents`, until then asserting the two equal: the term ships absent); `test_a_commander_at_strength_does_not_call_the_levy_again` (planted, the `muster_room` Observation dropped: refused on `room` in consecutive seasons).
- FALSIFIER and CONTROL: planted, `share` ignored in `_apply`: Partial raises 60. Control: `task_fraction` at its control arm (`1 / 1 / 1 / 0`) with the rows out of `graded_tasks`: every levy raises its whole count.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mil_c_muster.py tests/valoria/test_army_verbs.py -q` → green. The source's `aperture 2 s`, s = 0 to 2, `armies_at_build: empty` arm (`army.recruited` emitted by an act that passed through DELIBERATE at every seed; `room` refusals not repeated) reads the effect of B22.23: moved there.
- HASH MOVERS: none at `armies_at_build: off` (no one holds an army).
- DEPENDS ON: V12 B22.20; V12 `18_DETERMINISM_task_draw_for_uncontested_verbs` items 2, 4 (Batch B07: `graded_tasks`, the loader); V12 `05_SC_obstacle_difficulty_and_modifiers_B` (Batch B05); V12 `27_MB_A_command_and_the_obedience_draw` §1 (Batch B19: `command`'s definition row); V12 `06_FA_levy_through_the_seat_B` (Batch B21: `may_levy`); EXISTS-IN-TREE `engine/season/data/verbs.py::act_key`, `::opportunity_key`, `engine/season/loop/effects_army.py`.
- GLOSSARY: none new (*recruit*, *levy*, *muster* are MB lexicon D-6's).
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B22's producer; `Item: B22.21`, `[skip ci]`.

### B22.22 — the roll outlives its holder; a leaderless army thins when read · `14_VERBS_MILITARY_C` Edit 6 · BUILD · HASH EQUAL
- SOURCE: `proposals/14_VERBS_MILITARY_C_the_muster.md` §3 Edit 6 (as rewritten under C3-L11: the `loop/matter.py` pass is deleted); §4 "The successor", "Dispersal"; A-15 (natural death on), A-30, A-78.
- ADVANCES: R-08 (a world that thins armies nobody holds, with no player); the successor's roll.
- INSTRUCTION (order: the reader, then its callers, then the write-through):
  1. `queries/world_q.py::present_strength(w, rid) -> dict` (new): returns the Record's `by_type` counts less, for an unheld `army` Record (and for troops a held one may no longer keep: `army_state(...)['surplus']` true for a cohort gone or shrunk), the dispersed share: for each season since it became unheld (or since the surplus arose), one keyed graded draw `H(w.world_seed, rid, "army.disperse", season)` at rate `Fixtures leaderless_dispersal` (swept; NUMBER row in `hole_register.yaml`), reading hold · half of the affected troops go home · all go, composed in season order. It composes on `world_q.army_strength` (B22.05) for the recovered share, so one reader answers an army's strength.
  2. Every reader of an army's strength reads it: `army_state`, `other_army_records`' counts, `armyrecord.cohort_claims`' input, `seam/wrappers/mass_battle.py::_order_of_battle`.
  3. `loop/effects_information.py::_eff_create_record`, the `army` branch: where an unheld `army` Record of the minter's faction exists (lowest id), the effect opens the minter's `hold` on it and mints nothing (`record.taken_up`); `_army_mintable` admits it under the same conjuncts.
  4. The **next act** on the Record (the successor's `record.taken_up`, or any army verb) writes the read value into `subject_matter` first, through `armyrecord.apply('discharge', ...)` inside that act's effect (`_eff_create_record`'s army branch and `loop/effects_army.py`'s effects), and the read then starts from the written value (no `army.dispersed` Event and no MATTER write).
  5. `data/fixtures.py`: `leaderless_dispersal` = 0 `[ASSUMPTION: 0, no dispersal, as the shipped control — basis: the source names the fixture "swept" with a NUMBER row and gives no figure; B98 sets it]`; its NUMBER row in `engine/season/hole_register.yaml` from B22's H block.
- WHERE: `engine/season/queries/world_q.py` (NEW `present_strength`; `army_state`, `other_army_records`); `modules/mass_battle/armyrecord.py` (`cohort_claims`' input, via the host); `engine/season/seam/wrappers/mass_battle.py` (`_order_of_battle`); `engine/season/loop/effects_information.py` (`_eff_create_record`, `_army_mintable`); `engine/season/loop/effects_army.py` (the write-through); `engine/season/data/fixtures.py` (`leaderless_dispersal`); `engine/season/hole_register.yaml` (one NUMBER row).
- TESTS: in `test_vm_mil_c_muster.py` (the scratch probe `probe_army_s0.txt`'s death sequence restated as the successor function, U3 §6.2's rule), written first and read red: `test_a_successor_takes_up_the_roll` (after the commander's death the next `may_wage` leader's mint emits `record.taken_up`, `army_of` returns the old id, and the cohort's room is 60 less the troops still on the roll (20 in the probe), not 0 and not 60); `test_a_leaderless_army_disperses_when_read` (a leaderless army of 600 over two seasons at 50 seeds, `leaderless_dispersal` set in the test: `present_strength` takes more than two values across seeds, is 600 at some seed and below 600 at another; the written `subject_matter` unchanged until an act touches it — "over 8 seasons in the source; A-114"); `test_the_strength_read_twice_is_one_value_and_an_act_writes_it` (C3-L11's falsifier).
- FALSIFIER and CONTROL: the read twice at one tick returning two values; a planted act after the read that does not write the share, or a next read that adds again. Control: `armies_at_build: off`: hashes equal (no army exists).
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mil_c_muster.py -q` → green; the successor and dispersal gates read once by `opus`.
- HASH MOVERS: every reader of an unheld army's strength (none at `armies_at_build: off`; after B22.33, worlds with an unheld army — declared, B22's one re-pin).
- DEPENDS ON: V12 B22.21, B22.05; V12 `06_FA_levy_through_the_seat_B` (Batch B21: `may_wage`); EXISTS-IN-TREE `engine/season/loop/effects_information.py::_eff_create_record`, `engine/season/queries/world_q.py::army_of`, `::other_army_records`.
- GLOSSARY: none.
- IDS: H block slot 1 (`leaderless_dispersal`'s NUMBER row).
- COST and TIER: small build; `sonnet`, high; the strength read (a keyed graded draw that sets an army's strength) `opus`.
- LANDS IT: B22's producer; `Item: B22.22`, `[skip ci]`.

### B22.23 — the fixture for armies at build; the levy verbs leave the withheld list · `14_VERBS_MILITARY_C` Edit 7 · BUILD · HASH EQUAL
- SOURCE: `proposals/14_VERBS_MILITARY_C_the_muster.md` §3 Edit 7; §1 item 5; §4 (the `armies_at_build: empty` arm); `04_MB_playable_field_scenario` head item (2) ("one fixture, `armies_at_build: off | empty | mustered`").
- ADVANCES: none at shipped (`off`); the `empty` arm that B22.21's and B22.26's aperture gates read.
- INSTRUCTION (`data/fixtures.py`):
  1. `armies_at_build: "off"` (shipped) | `"empty"` (each faction's first `may_wage` leader mints an empty army through the fold at build, in `boot/realm.py`, the source's `harness/populated.py`) | `"mustered"` (today's `army_presets.install`, kept as a world-gen arm and no longer the unplayed commander's only path; B22.32 wires it).
  2. `withheld_verbs` drops `recruit` and `discharge_troops` in this item (the other four in B22.27). With `armies_at_build: off` no one holds an army, so nothing forms.
- WHERE: `engine/season/data/fixtures.py` (`armies_at_build`, `withheld_verbs`); `engine/season/boot/realm.py` (the `empty` arm's mint through the fold).
- TESTS: in `test_vm_mil_c_muster.py`: `test_armies_at_build_off_holds_no_army_record`; `test_empty_mints_one_empty_army_per_faction_leader`; red before for the second.
- FALSIFIER and CONTROL: an army Record at `off`. Control: `armies_at_build: off`: hashes EQUAL to the base but for B22.20's declared mover.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mil_c_muster.py -q` → green; and the source's arm, moved here: `aperture 2 s`, s = 0 to 2, `armies_at_build: empty` → `army.recruited` emitted by an act that passed through DELIBERATE (the act store names a chooser lap, not a hand-built id) at every seed; `recruit`'s refusals on `room` not repeated by the same actor the next season. (Source "chooser round" → "chooser lap", A-101.)
- HASH MOVERS: none at `off`.
- DEPENDS ON: V12 B22.22; V12 Batch B03c (`boot/realm.py`); V12 Batch B21 (`may_wage`); EXISTS-IN-TREE `engine/season/data/fixtures.py: withheld_verbs` (shipped `("destroy_record", *ARMY_VERBS, "marshal", "surrender")`, H-156), `engine/season/harness/army_presets.py::install`.
- GLOSSARY: none.
- NAMES: `harness/populated.py` → `boot/realm.py` (B03c).
- COST and TIER: small build; `sonnet`.
- LANDS IT: B22's producer; `Item: B22.23`, `[skip ci]`.

The batch B22-mb-armies continues at B22.24, in the next file in reading order. Last item written here: B22.23.



