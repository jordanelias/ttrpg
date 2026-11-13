# Workplan v12 — part 4: Batch B03-hygiene, first half (positions B03.01 to B03.28)

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12, `V12_STRUCTURE_part3.md` §8; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `aa31fd2` (branch `ccr-62958c70-0kjhsw`), read 2026-11-12; author lane A04 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2. Every item is written against the tree as B00, B01 and B02 will leave it; where B01 or B02 may have edited a named site, the item's first step opens it and records what it finds.

**What this part holds.** The head of `B03-hygiene` (IN), its first twenty-eight positions and the first rows of its position table: U3 §1 item 4 from `17_CENSUS_C1A_01` through `06_FA_hygiene`, with `CI-10`, `CI-08`, `CI-03`, `IS-B3-SE-04`, `CI-04` and `CI-05` placed as `V12_STRUCTURE.md` §2.2 orders them. The second half (positions from `B03.51`: `U5a_CORE_owed_edits`, `CI-06`, `09_WR_threadwork_module` edit 3, `IS-B2-CORE-06`, the intake's B03 entries, the cite fix, H-137, H-130, H-139), the `## Readings` block, the re-pin position `B03.99` and the boundary row are the second-half author's (`V12_STRUCTURE_part2.md` §4.2, part 5's row). A part cites another part's batch or item by handle only.

**Paths and words.** As `V12_STRUCTURE.md` states: a bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `CIP` is `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` and `_part2`; `the intake` is `master/eval/V12_INTAKE.md`. A path under `engine/`, `modules/`, `systems/`, `tools/`, `tests/`, `references/`, `registers/`, `godot/` is the repository's. Words are `unified/U1_GLOSSARY.md`'s (A-98, A-99, A-101): this batch lands before `PCR-4` (B04), so the season's within-season pass keeps the tree's identifier `round` where copied code names it, and prose says *lap*; nothing here renames a mass-battle identifier (B16L and B16M follow), so `Subunit`, `hierarchy/units.py` and `MB_REACH_FACING_GATE` are the tree's names at landing.

**Three things the sources did not have, each read at the tree** (each changes an item below):

1. **`Office.body_function` is a field of a hashed carrier.** `17_CENSUS_REST_1_deletions` D1 row 2 deletes it and says no hash moves. `World.content_hash()` folds `offices` (`state/world.py::World._STATE_COLLECTIONS`) and `_object_head` encodes every dataclass field *name*; the class's own comment says so of the two earlier deletions (`state/carriers.py::Office`, the `establishment` and `dates` notes: *"`Office`'s encoding folds into `World.content_hash` and carries every field NAME, so this deletion alone moves the digest of every world holding an office"*). By D-04 the row is `HASH MOVER(encoding)`, so **B03 is a mover batch with one re-pin, encoding only, controlled by tallies** (B03.28; RE-PIN below). The rest of B03's first half is hash EQUAL.
2. **`tools/export_composition.py::validate_wiring` refuses a `modules:` row with no `wiring:` block** (`"module:{name} has no `wiring:` block"`), and its `--check` is the gate of four items here. `06_FA_hygiene` item 5's "reduce each row to its `module:` name and a one-line note" would red it, so B03.26 keeps each row's `wiring:` block. At `aa31fd2` the check reads `OK — 16 role(s), every target resolved; wiring valid for 26 module(s)`.
3. **`ED-FA-0002` is already closed.** Its last row (`registers/editorial_ledger_fa_archive.jsonl`, 2026-10-06, `supersedes_row: true`, "SUPERSEDING ROW — CUT") governs, so `IS-B3-SE-04` step 4 (append a superseding row) is done (ladder step 1) and is not written; the stale "ED-FA-0002 is OPEN" banner in `references/action_vocabulary.yaml` is reworded in B03.13.

---

## Batch B03-hygiene · lane IN · wave W3 · step S3 · HASH MOVER(encoding B03.28; behaviour B03.86), one re-pin
INVOCATION: /methodology-execute Batch B03-hygiene
IN-FLIGHT ROW: registers/handoffs/HANDOFF_IN.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.harness.populated import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading") (this batch runs before B03c moves the builder to `engine/season/boot/realm.py`).
REQUIREMENT: none — deletions, owners and pointer text (`STAGES.md` stage 6, rule 5; `V12_STRUCTURE.md` §2.2: "none: deletions and owners"); what it serves: CLAUDE.md §0.05 (a contract row, a register row or a pointer that names code which is not there sends the next session to the wrong owner) and `CI-10`'s `FORK:` rows. R-01 to R-09 are re-read at the close and expected to print what B02's close printed (`reading @<B02 closing sha>`); no `status:` is edited (A-114)
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command):
  the realm reading `R(s)` for s = 0, 1, 2 (defined below) → the hash moved, as declared (B03.28, encoding only), and `acts` and `log` equal to B02's close (`reading @<B02 closing sha>`): D-04's control for an encoding mover is tallies-equal, never hash-equal;
  `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` → its `CONTENT HASH:` line is the value the re-pin records (moved only if the NPC-088 world holds an office; said either way), its act and Event tallies equal B02's close;
  `python -m engine.season.harness.report && python -m engine.season.harness.delta HEAD` → `PROBE FLIPS 0` (`16_PESSIMIST_CORE_no_stored_plan`'s gate; B03.16);
  `python tools/export_composition.py --check` → `OK — 17 role(s), every target resolved; wiring valid for 23 module(s)` (26 at `aa31fd2`, less B03.10's two rows and B03.13's one; 16 roles plus B03.12's one) `[derived from the items' own readings; re-read on the base]`;
  `python tools/export_sim_params.py --check` → `[SIM-PARAMS] current`; `python tools/export_game_constants.py --check` → current; `python tools/ci_golden_modes_check.py` → exit 0; `python tools/freshness_gate.py` → exit 0; `python tools/currency_consistency_check.py` → exit 0; `python tools/validate_ed_citations.py` → exit 0; `python tools/broken_dependency_checker.py` → exit 0; `python tools/valoria_local.py` → as CI runs it, green;
  the deletions' greps, each re-run on the closing tree and reading as its item's FALSIFIER line states (B03.01 to B03.10, B03.16, B03.25, B03.28);
  `python -m pytest engine/season/tests/test_cr30_heritage.py -q` → green (U3 §1.3's named instrument for B03);
  `python -m pytest -m mass_battle -q` once (`17_CENSUS_C1B_01` gate 2: the mass-battle goldens under `engine/tests/` unchanged after B03.06);
  `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `--verify-citations` → exit 0; `--requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  the gate lines of every item from B03.51 (the second half adds them in its items);
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (the batch edits engine core, tools and registries: the full gates, CLAUDE.md §0.4); the one full-suite run is at B03.99 (`V12_STRUCTURE_part4.md` E-2);
  the glossary rows B03.18 names, read against the code it landed (`STAGES.md`, "The glossary always matches", rule 2): a mismatch fails the close;
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<B02 closing sha>`) and after, and the batch's measured wall time; no conjunct is named, so no `reading:` record is written and `status:` is not edited (`IS-A-12`).
THE REALM READING `R(s)` (the plan's own instrument for this batch, a one-line read of existing code; nothing is added to the tree): `PYTHONHASHSEED=0 python -c "import sys; from engine.season.harness.populated import build_realm, run; s=int(sys.argv[1]); w=build_realm(s); o=run(1, s, w=w); print(w.content_hash(), o['acts'], len(w.log))" <s>` → three fields: hash, acts, log length (the shape of B02.01's `CENSUS` pin, `dict(acts=…, log=…)`). Per item (E-2): the covering test files and, for a mover, `R(0)`; at B03.99, `R(0)`, `R(1)`, `R(2)`.
RE-PIN: once, at B03.99 (the second half writes the position; `V12_STRUCTURE_part4.md` E-1): the realm pins in `engine/season/tests/_realm_goldens.py` (B02.01's one owner: `BUILD`, `SHIPPED`; `CENSUS` must not move) and the NPC-088 headless hash where it moved, read against B02's close (`reading @<B02 closing sha>`); the commit says "re-pin: encoding only (`Office.body_function` deleted in B03.28); tallies equal". (Patched: P-19: the second half's B03.86 (§H removes the office bonus, `budget_office_bonus`, C3-L8) is a declared behaviour mover, so the one re-pin records both and B03.99's commit text governs: "re-pin: B03.28 encoding (`Office.body_function` deleted from a class `World.content_hash()` encodes, D-04; tallies equal); B03.86 behaviour (`budget_office_bonus` removed, C3-L8, declared) — or 'B03.86 falsified and reverted'; every other item of B03 hash EQUAL". The tallies-equal control holds on B03.85's tree, before B03.86.) A test that pins one item's own literal keeps it in that item's commit (E-1).
IDS: ED-IN 0; H 0 for B03.01–B03.28 (no item here writes a new ED or hole-register id: B03.23 prepends text to existing rows; the `FORK:` rows take no id). The second half's items declare theirs in their own `IDS:` lines; H2 sums the batch from the items.
DIALS AT CONTROL: none in B03.01–B03.28 (no setting is added or shipped at a control value; B03.14 and B03.15 export existing values and change none).
UNDECIDED (each with the reading taken, the one that changes less, `V12_STRUCTURE_part2.md` §5.1):
  (1) B03.28: `17_CENSUS_REST_1` D1 row 2 is an encoding mover; taken: declare it and re-pin at B03.99 (D-04's rule, "co-batched with a re-pin"); the other reading moves the row to B04, whose B04.26 already re-pins by encoding, and keeps B03 hash EQUAL as `V12_STRUCTURE_part3.md` §7.1 item 7 lists it. The orchestrator may take either; the item is self-contained.
  (2) REST_1 D1 is one commit in its source; split here into B03.05 (rows 4–5, which its own head puts in `17_CENSUS_C1B_01` D1's commit), B03.09 (rows 1, 3) and B03.28 (row 2, the mover, placed last so the hash-EQUAL items come first, §5.9). E-13.
  (3) CIP §2 says `CI-10` joins B03 "first, with `17_CENSUS_C1A_01` D1"; taken as two items, B03.01 then B03.02 (no shared file, two gates), not one commit.
  (4) `11_GO_pointer_and_stale_text_resolutions` lands as one `[cleanup]` commit in its source; taken: B03.18 (its items 1, 2, 11, 12, 13), with its item 3 moved into B03.21 because `11_GO_design_reference_disposition` edit 2 says item 3's sentence "gains one clause, applied as one edit"; item 6 is HELD (B03.19); items 7–8 are a POINTER to GO-11 in B03g (B03.20).
  (5) Pointers to retired v11 files in copied text: `11_GO_pointer` item 1 ("the B10-20 card in `workplans/valoria_master_workplan_v11_part3.md`") and item 12 ("(B10-20)"), and `17_CENSUS_REST_3` H-238's new owner text (`valoria_master_workplan_v11.md` P9), are written against v12 (`B41-go-port-gate`; v12's head rule P9), because v11 is deleted in v12's adopting commit (`V12_STRUCTURE_part3.md` §8.1 steps 4, 8) and B03 runs after it. Each correction is said in its item.
  (6) Not carried, each a dead target: `11_GO_pointer` item 9 (edits `workplans/valoria_master_workplan_v11_part5.md`, deleted at adoption; GO-01's own control text is B03g's); `06_FA_hygiene` item 6's second half (edits the B10-17 card, `proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-17.md`, deleted at adoption, §8.1 step 5); `11_GO_pointer`'s closing of ED-1054 "at ladder step 1 with a row citing [the banners]" (the row's open residual, read in `registers/editorial_ledger.jsonl`, is (i) narrative markdown under `tests/` and (iii) stale `sim/README.md`, `sim/CONVENTIONS.md`, `tools/README.md`; the `godot/` banners answer neither, so a closing row would be false; left for the IN lane's queue, not this batch).
  (7) `09_WR_B_pointer_text_for_the_orchestrator` edit 1's new `CURRENT.md` row has four cells; the table has three (`| Subsystem | Head | Status and open items |`): the last two cells are joined with "; " (B03.17).
  (8) The intake's B03 entries A2-40 ("with `09_WR_B_pointer_text_for_the_orchestrator`") and H-291 ("item 2 already edits `_req_establish`", i.e. `06_FA_hygiene` item 2) name items of this half as neighbours; §4.2 gives the intake `:112` and `:227` to the second half, which places them; neither id is named by any source of this half (grep), so §5.6's first rule does not pull them here.
C(B03-hygiene) (this half's share; the second half's items add their WHERE files): this batch's entries; the plan's head parts; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_IN.md`, the skill and `methodology-close`);
  edited here: `tools/join_audit_workings.py`, `tools/verify_handoff_split.py`, `tools/link_values_pointers.py`, `tests/valoria/test_link_values_pointers.py`, `engine/engine_params/value_pointer_links.json` (deleted); `references/restructure_ledger.md`; `engine/season/gaps.py`; `engine/season/data/cast.py`; `engine/season/data/files.py`; `engine/season/state/world.py`; `engine/season/state/carriers.py` (`Office`); `engine/season/queries/world_q.py`; `engine/season/queries/person_q.py`; `engine/season/queries/faction_q.py`; `engine/season/loop/driver.py`; `engine/season/loop/deliberate.py`; `engine/season/loop/predicates.py`; `engine/season/seam/wrappers/sigma.py`; `engine/dice_engine/dice_engine.py`;
  `systems/combat/combat_engine_v1/workbench/calibrate_generics.py`; `systems/combat/combat_engine_v1/capabilities.py`; `systems/characters/sim/conviction.py`; `systems/fieldwork/sim/knots.py`; `systems/threadwork/sim/__init__.py`, `threadcut.py`, `co_movement.py` (deleted), `operations.py`; `modules/mass_battle/hierarchy/units.py`; `modules/mass_battle/perimeter.py`;
  `references/module_contracts.yaml`; `references/action_vocabulary.yaml`; `registers/mechanics_index.yaml`; `engine/season/hole_register.yaml`; `engine/season/requirements.yaml`; `engine/season/write_matrix.yaml` (header); `engine/engine_params/composition.json`, `sim_params.json` (re-derived); `tools/export_sim_params.py`; `tools/ci_golden_modes_check.py`; `tools/build_engine_atlas.py`; `CURRENT.md`; `godot/README.md`, `godot/godot_architecture_specification.md`, `godot/godot_conversion_strategy_v1.md`; `registers/handoffs/HANDOFF_GO.md`, `HANDOFF_FA.md`; `unified/U1_GLOSSARY.md`;
  tests edited: `engine/season/tests/test_cr30_heritage.py`, `test_person_projection.py` (deleted), `test_h11_affiliation_scar.py`, `test_social_contest_module.py`, `test_season_shape.py`, `test_in53_vacancy_need.py`, `test_faction_q.py`, `test_go07_canonical_digest.py`; `tests/valoria/test_reach_weapon_class.py`, `test_perimeter_geometry.py`, `test_dice_engine_properties.py`, `test_module_registrar.py`, `test_export_sim_params.py`;
  read only: `engine/season/harness/populated.py` (`build_realm`, `run`), `headless.py`, `aperture.py`, `report.py`, `delta.py`, `register.py`; `engine/season/manifest/registry.py`, `manifest/registrar.py::require_entries`; `engine/season/data/fixtures.py` (`DEFAULT_FIXTURES`); `engine/season/tests/_realm_goldens.py` (B02); `engine/reference/degree-sweep/sweep_core.py`; `tools/export_composition.py` (`validate_wiring`, `_ENTRIES`), `tools/mechanics_index_gen.py`, `tools/export_game_constants.py`, `tools/build_identifier_census.py`, `tools/ci_quantity_vocabulary_check.py`, `tools/tests_for_diff.py`; `tests/valoria/test_engine_does_not_import_systems.py`, `test_export_game_constants_ambiguity.py`, `engine/tests/test_knots_ed912.py`, `tests/valoria/test_mass_battle_maneuvers.py`, `test_body_primitive.py`, `engine/season/tests/test_rem31_grid_suspension.py`; `registers/editorial_ledger.jsonl` (ED-1054), `registers/editorial_ledger_fa_archive.jsonl` (ED-FA-0002);
  the closing SHAs of B00, B01, B02.
SERIAL EDGES and FILE CENSUS: written after the position table (E-11), at the end of this half.
PARALLEL: S3, alone (`V12_STRUCTURE.md` §2.3: S0–S3 hold one IN batch each). No other batch is open; nothing is shared.
COST: edits and deletions throughout, one exporter extension (B03.14, B03.15); producer `valoria-author` on `sonnet`, `high` unless an item says otherwise; no judgment node in this half (B03.19 is HELD, its wording Jordan's); the close's terminal critique `opus`.
EST: 0.4 h × (28 positions here + the second half's) + 2.5 h [estimate: `V12_STRUCTURE.md` §2.4's per-commit formula over positions (`V12_STRUCTURE_part4.md` E-15); this half alone is 11.2 h of build; the head parts total the batch]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B03.01 | three files nothing reads are deleted, with their `FORK:` rows | `CI-10` | BUILD | EQUAL | Batch B02 |
| B03.02 | names nothing calls: `Ineligible`, `name_of`, two path constants, two item getters | `17_CENSUS_C1A_01` D1 (less the `defects` row) | BUILD | EQUAL | Batch B02 |
| B03.03 | the person projection and its test file | `17_CENSUS_C1A_01` D2 | BUILD | EQUAL | B03.02 |
| B03.04 | two test-only twins of a live pair | `17_CENSUS_C1A_01` D3 | BUILD | EQUAL | Batch B02 |
| B03.05 | uncalled functions and unread fields in four oracle and module files | `17_CENSUS_C1B_01` D1 with `17_CENSUS_C1B_03` C-3 and `17_CENSUS_REST_1` D1 rows 4–5 | BUILD | EQUAL | Batch B02 |
| B03.06 | the reach-facing flag and the target-point half of the perimeter | `17_CENSUS_C1B_01` D2 with `17_CENSUS_C1B_03` C-2 | BUILD | EQUAL | B03.05 |
| B03.07 | two threadwork oracle files nothing imports | `17_CENSUS_C1B_01` D3 with `17_CENSUS_C1B_03` C-4, C-5 | BUILD | EQUAL | B03.01, B03.06 |
| B03.08 | a docstring that names a module by its old name | `17_CENSUS_C1B_03` C-1 | BUILD | EQUAL | Batch B02 |
| B03.09 | two dead fields: a roll's `pool_size`, a unit row's `merged_cells` | `17_CENSUS_REST_1` D1 rows 1, 3 | BUILD | EQUAL | B03.05 |
| B03.10 | two phantom contract rows | `17_CENSUS_REST_1` D4 | BUILD | EQUAL | Batch B02 |
| B03.11 | the driver imports what it uses | `CI-08` | BUILD | EQUAL | B03.10 |
| B03.12 | the obstacle composer is reached by its own composition row | `CI-03` | BUILD | EQUAL | B03.10, B03.11 |
| B03.13 | the `domain_actions` contract row is retired | `IS-B3-SE-04` | BUILD | EQUAL | B03.12 |
| B03.14 | the season's settings are in the typed export | `CI-04` | BUILD | EQUAL | B03.01, B03.07 |
| B03.15 | the realm's arms are in the same export | `CI-05` | BUILD | EQUAL | B03.14 |
| B03.16 | no stored plan: the queue-reuse branch that never fires | `16_PESSIMIST_CORE_no_stored_plan` | BUILD | EQUAL | B03.11 |
| B03.17 | pointer and register text for files only the orchestrator edits | `09_WR_B_pointer_text_for_the_orchestrator` edits 1–4 | BUILD | EQUAL | B03.13 |
| B03.18 | pointer and stale text at the owners a porter reads first | `11_GO_pointer_and_stale_text_resolutions` items 1, 2, 11, 12, 13 | BUILD | EQUAL | B03.17 |
| B03.19 | Layer 1's rejection-5 measurement paragraph becomes a command | `11_GO_pointer_and_stale_text_resolutions` item 6 | HELD (Jordan: a Layer 1 amendment) | — | — |
| B03.20 | the contract file's Key-era `parity:` values and the skeleton note | `11_GO_pointer_and_stale_text_resolutions` items 7–8 | POINTER (GO-11, Batch B03g) | — | — |
| B03.21 | which design reference binds the port: two owner sentences and a standing order | `11_GO_design_reference_disposition` edits 1, 2, 4, with `11_GO_pointer…` item 3 | BUILD | EQUAL | B03.18 |
| B03.22 | twenty-seven stale substrings, two contract rows, a header that claims a check | `17_CENSUS_REST_3` A, B, C | BUILD | EQUAL | B03.17, B03.10 |
| B03.23 | two register rows describe a tree that no longer exists | `06_FA_hygiene` item 1 | BUILD | EQUAL | B03.17, B03.22 |
| B03.24 | every refusal of `confer` and `establish` names its clause | `06_FA_hygiene` item 2 | BUILD | EQUAL | Batch B02 |
| B03.25 | `faction_q.superiors`, which nothing calls | `06_FA_hygiene` item 3 | BUILD | EQUAL | Batch B02 |
| B03.26 | contract rows for a retired faction | `06_FA_hygiene` item 5 | BUILD | EQUAL | B03.13 |
| B03.27 | a process row that orders work no plan schedules | `06_FA_hygiene` item 6 (first half) | BUILD | EQUAL | Batch B02 |
| B03.28 | `Office.body_function`, written and never read | `17_CENSUS_REST_1` D1 row 2 | BUILD | MOVER(encoding) | B03.09 |
| B03.51 … | the second half, from `U5a_CORE_owed_edits`; then `## Readings`, B03.99 and the boundary row | the second-half author's part | — | — | — |

Not in this batch, and where each is: `17_CENSUS_C1A_01` D1's `cast.defects` row (B10, in `17_CENSUS_C1A_02` W3's commit, which moves its paren check into the loader) and the comment `engine/season/seam/__init__.py` that names the deleted `COMBAT_SEAM_PY` (`17_CENSUS_C1A_02` C1, B10); every `tests/valoria/test_flow_skeletons.py` edit and gate line of `17_CENSUS_C1B_01` (the file is deleted by B02.03, `01_CORE_tests_delete_what_cannot_fail` row 2; C-U5a-19 makes those edits conditional on it); `17_CENSUS_C1B_01`'s SC-05 kernel rows (`05_SC_sc05_kernel_disposition_B`, B24); `17_CENSUS_REST_1` D1 row 6 (withdrawn, C-U5a-18), D2 (B11, with `08_FI_04_small-edits`), D3 (withdrawn: `stubwire.py` stays); `17_CENSUS_C1B_03` C-6 (carried by `09_WR_threadwork_module`'s own head, C-U5a-17); `11_GO_pointer…` items 4–5 (applied by A-97, node `L1-A30`; no batch), item 9 and the ED-1054 closure (UNDECIDED (6)), item 10 (a decision with no edit: `references/descriptor_registry.yaml`'s IN FLUX lines stay Jordan's); `11_GO_design_reference_disposition` edit 3 (no `ui` row: no edit); `17_CENSUS_REST_3` D (C-5, C-6, `12_ARCS_adjudication` row 19: sentences in suite proposals, not the tree) and E (the untracked census script; the locked worktree is the orchestrator's call); `06_FA_hygiene` item 4 (withdrawn, D-U1-11h) and item 6's card half (UNDECIDED (6)); `IS-B3-SE-04` step 4 (ED-FA-0002 already closed: fact 3 above).

### B03.01 — three files nothing reads are deleted, with their `FORK:` rows · CI-10 · BUILD · HASH EQUAL
- SOURCE: `master/CODEBASE_IMPROVEMENT_PROPOSAL_part2.md` "CI-10 · Three things nothing reads are deleted", and §4 (the `FORK:` row text); CIP §2 ("**B03-hygiene** … first"); closes H-10 (the part no other proposal carries).
- ADVANCES: none of the nine; reading cost (three tools and a generated artifact nothing calls).
- INSTRUCTION (copied):
  1. "Re-run the search on the base: `grep -rnw -e join_audit_workings -e verify_handoff_split -e link_values_pointers -e value_pointer_links --include=*.py --include=*.yml --include=*.yaml --include=*.json --include=*.md .` outside `registers/`, `.audit/`, `research/`, `proposals/` and `references/restructure_ledger.md`. Expected: the files themselves, the test, and the comment at `data/cast.py:432`." Record the output in the commit body.
  2. "`git rm` the five files" (`tools/join_audit_workings.py`, `tools/verify_handoff_split.py`, `tools/link_values_pointers.py`, `tests/valoria/test_link_values_pointers.py`, `engine/engine_params/value_pointer_links.json`). "Edit the comment at `data/cast.py:432` so it names no deleted tool" (find it by `grep -n "link_values\|value_pointer" engine/season/data/cast.py`).
  3. "Write the five `FORK:` rows of §4 into `references/restructure_ledger.md` (a shallow clone runs `git fetch --unshallow` first, CLAUDE.md §2)." `<sha>` is `git log -n1 --format=%h -- <path>` on the batch's base; `<date>` the landing date. The rows, in the table's own form:
     ```
     | `tools/join_audit_workings.py` | `FORK:<sha>` | FORKED (<date>, workplan v12 batch B03, item CI-10: no caller in engine, modules, tools, tests, skills or CI; its subject, the audit corpus's nested working tier, is retired as a category (`CLAUDE.md` section 3) and its test was dropped at ED-IN-0312. `<sha>` is the last commit touching it, so the text there is the file) |
     | `tools/verify_handoff_split.py` | `FORK:<sha>` | FORKED (<date>, workplan v12 batch B03, item CI-10: no caller; a one-time falsifier for the handoff split of 2026-09-13 (ED-IN-0221), which is complete; its test was dropped at ED-IN-0312. `<sha>` is the last commit touching it, so the text there is the file) |
     | `tools/link_values_pointers.py` | `FORK:<sha>` | FORKED (<date>, workplan v12 batch B03, item CI-10: its one output, `engine/engine_params/value_pointer_links.json`, was read by nothing but this tool and its test; in no CI job, hook or registry row. `<sha>` is the last commit touching it, so the text there is the file) |
     | `tests/valoria/test_link_values_pointers.py` | `FORK:<sha>` | FORKED (<date>, workplan v12 batch B03, item CI-10: deleted with its subject, `tools/link_values_pointers.py`. `<sha>` is the last commit touching it, so the text there is the file) |
     | `engine/engine_params/value_pointer_links.json` | `FORK:<sha>` | FORKED (<date>, workplan v12 batch B03, item CI-10: a generated artifact no engine, module, exporter or port file read. `<sha>` is the last commit touching it, so the text there is the file) |
     ```
  4. "`tools/build_identifier_census.py:269` reads the keys of every `engine/engine_params/*.json`: run it as CI runs it (the job step in `.github/workflows/valoria-ci.yml` that names it). If an identifier now reads as unknown, it was known only through the deleted link file; correct the document that uses it."
- WHERE: DELETE `tools/join_audit_workings.py`, `tools/verify_handoff_split.py`, `tools/link_values_pointers.py`, `tests/valoria/test_link_values_pointers.py`, `engine/engine_params/value_pointer_links.json`; `engine/season/data/cast.py` (the one comment naming the tool); `references/restructure_ledger.md` (five rows).
- TESTS: `tests/valoria/test_link_values_pointers.py` "is deleted with its subject. None added."
- FALSIFIER and CONTROL: "A caller: any line step 1 prints that is an import, a subprocess call or a workflow step. If one appears, that file is not deleted and the row is struck." Control: `R(0)` hash equal to B02's close (nothing at runtime read any of the five).
- GATE: step 1's grep, re-run → only ledger and history lines; `python tools/broken_dependency_checker.py` → exit 0; `python tools/valoria_local.py` → as CI runs it, green; `python tools/export_game_constants.py --check` → current; `python tools/export_sim_params.py --check` → current; each new row read as an exact row through `tools/pathres.py::load_alias_map()` (never `resolve()`, CLAUDE.md §8): `python -c "import sys; sys.path.insert(0,'tools'); import pathres; m=pathres.load_alias_map()[0]; print(all(p in m for p in ['tools/join_audit_workings.py','tools/verify_handoff_split.py','tools/link_values_pointers.py','tests/valoria/test_link_values_pointers.py','engine/engine_params/value_pointer_links.json']))"` → `True` (`load_alias_map()` returns `(exact rows, dir-prefix rows)`; index 0 is the exact rows, `tools/pathres.py`).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE the five files (opened at `aa31fd2`); `engine/season/data/cast.py` (the comment); `tools/build_identifier_census.py`; `tools/pathres.py::load_alias_map`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `low` (CIP).
- LANDS IT: B03's `valoria-author` producer, `isolation: worktree`; one `Item: B03.01` commit, `[skip ci]`.

### B03.02 — names nothing calls: `Ineligible`, `name_of`, two path constants, two item getters · 17_CENSUS_C1A_01 D1 · BUILD · HASH EQUAL
- SOURCE: `proposals/17_CENSUS_C1A_01_deletion_batches.md` "D1 · names nothing calls" (less its `defects` row, which its head moves to B10); closes F-C1A-01 (part).
- ADVANCES: none of the nine; what a reader is told exists.
- INSTRUCTION (the table, copied; each site found by its symbol):
  | file | delete | also |
  |---|---|---|
  | `engine/season/gaps.py` | `class Ineligible` | "nothing imports it; refusal by ineligibility is the Event kind `FOLD_INELIGIBLE`" |
  | `engine/season/data/cast.py` | `def name_of` | `engine/season/tests/test_cr30_heritage.py` (the `name_of` assertion): "replace the assertion with `assert (cast.row("NPC-020")["first_name"], cast.row("NPC-020")["last_name"]) == ("Almud", "Almqvist") and (cast.row("NPC-052")["first_name"], cast.row("NPC-052")["last_name"]) == ("Magnus", "Vaynard")`" |
  | `engine/season/data/files.py` | `SEAM_DIR`, the comment block under it, `COMBAT_SEAM_PY` | the stale comment in `engine/season/seam/__init__.py` is `17_CENSUS_C1A_02` C1's (B10) |
  | `engine/season/state/world.py` | `_FIRST, _SECOND = _itemgetter(0), _itemgetter(1)` | "drop `itemgetter as _itemgetter` from the import … (no other use)" |
  "A deleted symbol inside a surviving file does not [need a `FORK:` row] (the path still resolves), and its record is the commit." `cast.defects` is **not** deleted here (B10).
- WHERE: `engine/season/gaps.py` (`Ineligible`); `engine/season/data/cast.py` (`name_of`); `engine/season/data/files.py` (`SEAM_DIR`, `COMBAT_SEAM_PY`); `engine/season/state/world.py` (`_FIRST`, `_SECOND`, the `operator` import line); `engine/season/tests/test_cr30_heritage.py` (one assertion).
- TESTS: `test_cr30_heritage.py`'s rewritten assertion; green before (old spelling) and after (new spelling).
- FALSIFIER and CONTROL: "`grep -rn "Ineligible\b\|cast\.name_of\|cast\.defects\|COMBAT_SEAM_PY\|SEAM_DIR\|_FIRST\b\|_SECOND\b" engine modules systems tools tests --include=*.py` returns a use outside the deleted lines" (`cast.defects` stays until B10, so its hits are expected and named in the commit body). Control: `R(0)` hash equal to B03.01's.
- GATE: `python -c "import engine.season.gaps, engine.season.data.cast, engine.season.data.files, engine.season.state.world"` → exit 0; `python -m pytest engine/season/tests/test_cr30_heritage.py -q` → green.
- HASH MOVERS: none (`Ineligible` is never instantiated into a `World`; the two getters are module names).
- DEPENDS ON: EXISTS-IN-TREE `gaps.py::Ineligible`, `data/cast.py::name_of`, `data/files.py::SEAM_DIR`, `::COMBAT_SEAM_PY`, `state/world.py::_FIRST`, `::_SECOND` (each opened at `aa31fd2`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high` (the source's tier).
- LANDS IT: B03's producer; `Item: B03.02`, `[skip ci]`.

### B03.03 — the person projection and its test file · 17_CENSUS_C1A_01 D2 · BUILD · HASH EQUAL
- SOURCE: `proposals/17_CENSUS_C1A_01_deletion_batches.md` "D2 · the person projection"; C-U5a-15, C3-L4, C3-Y9; U3 §4.1 rows 2–6 (REV: the four re-pointed proposals depend on this, not the reverse); closes F-C1A-06.
- ADVANCES: none of the nine; one owner of "what a client reads for one person" (`account`, B34).
- INSTRUCTION (copied):
  | file | delete |
  |---|---|
  | `engine/season/queries/world_q.py` | "the section header …, `_person_or_refuse`, `witnessed`, `PersonProjection`, `projection`; then `import copy` if `grep -n "copy\." engine/season/queries/world_q.py` is empty" |
  | `engine/season/tests/test_person_projection.py` | "the file (115 lines, 5 tests, all on the deleted names)" |
  `FORK:` row, in `references/restructure_ledger.md` ("the sha is the last commit touching the test file; in this clone `git log -1 --format=%h -- engine/season/tests/test_person_projection.py` gives `60d13a7`, a shallow-boundary commit that holds the file; after `git fetch --unshallow`, re-run the command and use its result if it differs"):
  ```
  | `engine/season/tests/test_person_projection.py` | `FORK:60d13a7` | FORKED (<landing date>, census C1A D2: the five tests of `world_q.projection` / `witnessed` / `PersonProjection`, v9 PC-06 S-2/L-1, a per-person client read that no harness, tool or plan called; the player's reading is the ledger-only `account` of the player surface contract; `60d13a7` is the last commit touching it in a shallow clone, so the text there is the file) |
  ```
  "The readers that described `PersonProjection` as present … are re-pointed at `account` by their own `Reconciled:` lines (C-U5a-15); this commit edits none of them."
- WHERE: `engine/season/queries/world_q.py` (the projection section; `import copy` if unused); DELETE `engine/season/tests/test_person_projection.py`; `references/restructure_ledger.md` (one row).
- TESTS: `test_person_projection.py` deleted with its subject; none added.
- FALSIFIER and CONTROL: "`grep -rn "PersonProjection\|world_q\.projection\|world_q\.witnessed\|import.*\bprojection\b" engine modules tools --include=*.py` finds a call." Control: "a seeded one-season `content_hash` at seed 0 equals the hash before the commit": `R(0)` hash equal to B03.02's.
- GATE: `python -c "import engine.season.queries.world_q"` → exit 0; `R(0)` → hash equal to B03.02's reading; the new row read through `pathres.load_alias_map()` (as B03.01) → present.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `queries/world_q.py::PersonProjection`, `::projection`, `::witnessed`, `::_person_or_refuse`; `engine/season/tests/test_person_projection.py`; V12 B03.02 (same deletion series, one commit each).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B03's producer; `Item: B03.03`, `[skip ci]`.

### B03.04 — two test-only twins of a live pair · 17_CENSUS_C1A_01 D3 · BUILD · HASH EQUAL
- SOURCE: `proposals/17_CENSUS_C1A_01_deletion_batches.md` "D3 · two test-only twins of a live pair".
- ADVANCES: none of the nine; one ladder for "which elements an act violates".
- INSTRUCTION (copied):
  | file | delete | re-point |
  |---|---|---|
  | `engine/season/queries/person_q.py` | `violated_pursuits`, `violated_affiliations` | `engine/season/tests/test_h11_affiliation_scar.py` (8 uses): "`violated_pursuits(p, v)` becomes `broken_by(p, (elements_violated_by(v)[0], frozenset()))` and `violated_affiliations(p, v)` becomes `broken_by(p, (frozenset(), elements_violated_by(v)[1]))` (each half of the live pair, exactly); where the test wants both, `broken_by(p, elements_violated_by(v))` whole" |
  "Keep `_pursuits_violated_by` and `_affiliations_violated_by`: `elements_violated_by` calls them and `loop/resolve.py::_scar_witnesses` calls that. Move the two deleted docstrings' statement of the rule (which elements an act violates, and why by sign) onto `elements_violated_by`, which today defers to them; also reword `broken_by`'s docstring, which defines itself by the deleted names."
- WHERE: `engine/season/queries/person_q.py` (`violated_pursuits`, `violated_affiliations` deleted; `elements_violated_by`, `broken_by` docstrings); `engine/season/tests/test_h11_affiliation_scar.py` (eight call sites).
- TESTS: `test_h11_affiliation_scar.py`, re-pointed; green before and after.
- FALSIFIER and CONTROL: "a seeded season's scar counts differ before and after (they cannot: `resolve.py` never called the deleted names)". Control: `R(0)` hash equal to B03.03's.
- GATE: `python -m pytest engine/season/tests/test_h11_affiliation_scar.py -q` → green; `grep -rn "violated_pursuits\|violated_affiliations" engine modules tools tests --include=*.py` → no hit.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `queries/person_q.py::violated_pursuits`, `::violated_affiliations`, `::elements_violated_by`, `::broken_by`, `::_pursuits_violated_by`, `::_affiliations_violated_by`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B03's producer; `Item: B03.04`, `[skip ci]`.

### B03.05 — uncalled functions and unread fields in four oracle and module files · 17_CENSUS_C1B_01 D1 with 17_CENSUS_C1B_03 C-3 and 17_CENSUS_REST_1 D1 rows 4–5 · BUILD · HASH EQUAL
- SOURCE: `proposals/17_CENSUS_C1B_01_deletions.md` "Batch D1 · no caller anywhere" (its head: "D1 in one commit with `17_CENSUS_REST_1_deletions.md` D1 rows 4-5 (same file, `conviction.py`)"); `proposals/17_CENSUS_C1B_03_corrections.md` C-3 ("rides D1"); `proposals/17_CENSUS_REST_1_deletions.md` D1 rows 4, 5; C-U5a-18, C-U5a-19; ED-IN-0283 (RULED: the `systems/` homes stay; no file or folder is deleted here).
- ADVANCES: none of the nine.
- INSTRUCTION (one commit; copied):
  | file | delete | evidence |
  |---|---|---|
  | `systems/combat/combat_engine_v1/workbench/calibrate_generics.py` | `newcombe` | the def only |
  | `modules/mass_battle/hierarchy/units.py` | `_reach_throttle` | "the def only; not in `__all__`" |
  | `systems/characters/sim/conviction.py` | `mark_belief_revision_pending` | the def only |
  | same | "the field `ConvictionState.pending_belief_revisions` and its two (de)serialiser lines" | "written by the function above and by nothing else; read by nothing but `to_dict`/`from_dict`" |
  | same | C-3: "Delete the paragraph that begins `[ASSUMPTION: cycle resolution — beliefs.revise_belief calls into`. There is no `beliefs` module in the tree … Nothing replaces it." | |
  | same | REST_1 row 4, `ConvictionThresholdState.destabilised`: the field, its docstring line, the local, the keyword | |
  | same | REST_1 row 5, `ConvictionThresholdState.any_crisis`: the field, its docstring line, the keyword | |
  | `systems/fieldwork/sim/knots.py` | `get_knot`, `get_active_knots` | "the defs only; `engine/tests/test_knots_ed912.py` uses neither" |
  "`from_dict` must go on accepting a stored dict that still carries the key (read with `d.get` and ignored), so an old saved state does not fail to load." `scar_counts`, "which a test reads, stays." "No `FORK:` row: no file is deleted." The source's covering-test line naming `tests/valoria/test_flow_skeletons.py` and its `RETIRED_SYMBOLS` is not carried: B02.03 deleted that file.
- WHERE: `systems/combat/combat_engine_v1/workbench/calibrate_generics.py` (`newcombe`); `modules/mass_battle/hierarchy/units.py` (`_reach_throttle`); `systems/characters/sim/conviction.py` (`mark_belief_revision_pending`; `ConvictionState.pending_belief_revisions` with `to_dict`/`from_dict`; the module docstring's `beliefs` paragraph; `ConvictionThresholdState.destabilised`, `.any_crisis`); `systems/fieldwork/sim/knots.py` (`get_knot`, `get_active_knots`).
- TESTS: none added. `from_dict` on a dict carrying `pending_belief_revisions` still loads: `test_conviction_from_dict_ignores_a_retired_key` in `engine/tests/test_knots_ed912.py` `[ASSUMPTION: test name and file; the item creates it — basis: the source states the requirement and names no test; E-3]`, written before the edit and green before and after (it is the falsifier of the `d.get` rule).
- FALSIFIER and CONTROL: "A content hash that moves" (the source's), and the grep `grep -rnw -e newcombe -e _reach_throttle -e mark_belief_revision_pending -e pending_belief_revisions -e get_knot -e get_active_knots -e destabilised -e any_crisis engine modules systems tools tests skills` → no hit outside the deleted lines and the `d.get` read. Control: `R(0)` hash equal to B03.04's; `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` → `CONTENT HASH:` equal to B02's close.
- GATE: `python -m pytest engine/tests/test_knots_ed912.py tests/valoria/test_mass_battle_maneuvers.py -q` → green; `python -c "import modules.mass_battle.hierarchy.units, systems.characters.sim.conviction, systems.fieldwork.sim.knots"` → exit 0.
- HASH MOVERS: none (the oracle and module classes are not `World` carriers).
- DEPENDS ON: EXISTS-IN-TREE each symbol above (opened at `aa31fd2`); V12 B02.03 (deleted `test_flow_skeletons.py`, which makes its edits void).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B03's producer; `Item: B03.05`, `[skip ci]`.

### B03.06 — the reach-facing flag and the target-point half of the perimeter · 17_CENSUS_C1B_01 D2 with 17_CENSUS_C1B_03 C-2 · BUILD · HASH EQUAL
- SOURCE: `proposals/17_CENSUS_C1B_01_deletions.md` "Batch D2 · test-only, and superseded by what the resolver does run (one commit, with its test edits)", D2a and D2b; `proposals/17_CENSUS_C1B_03_corrections.md` C-2 ("rides D2a").
- ADVANCES: none of the nine; one owner of the facing rule (`geometry.reach_reaches`) and of the struck face (`orchestration._compute_atom_sides`).
- INSTRUCTION (one commit; copied):
  D2a, `modules/mass_battle/hierarchy/units.py::_effective_reach` and the flag only it reads:
  | edit | where |
  |---|---|
  | delete `_effective_reach` | `units.py` |
  | delete `MB_REACH_FACING_GATE` and the comment above it | `units.py`, and its name in `__all__` |
  | delete the key `'MB_REACH_FACING_GATE': '1'` | `tools/ci_golden_modes_check.py` (the canonical-modes table) |
  | C-2: `generous, non-facing-gated outer bound (see _effective_reach)` → `generous, non-facing-gated outer bound (the facing-gated test is geometry.reach_reaches)` | `units.py` (the comment) |
  | delete `test_facing_away_gets_no_reach` | `tests/valoria/test_reach_weapon_class.py` |
  "⚠ **The flag is the risk in this batch.** … The pin and the flag must leave in the same commit, or the golden-modes check (which compares each pin with a source-level `environ.get` default) goes red."
  D2b, `modules/mass_battle/perimeter.py`, the target-point half:
  | edit | where |
  |---|---|
  | delete `TargetPoint`, `_vertex_interior_angle`, `target_points`, `nearest_target`, `approach_alignment`, `SHARP_TIP_DEG` | `perimeter.py` |
  | "cut the module docstring to what remains: faces from the convex hull of the cell centres, with outward normals, read by `units._envelop_goal`" | `perimeter.py` (module docstring) |
  | keep `Face`, `_convex_hull`, `_centroid`, `_unit`, `perimeter_faces` | — |
  | `tests/valoria/test_perimeter_geometry.py`: "delete `test_nearest_target_picks_the_faced_side`, `test_approach_alignment_is_one_when_square_on`; in `test_line_is_a_four_face_rectangle`, `test_arrowhead_has_a_sharp_or_flagged_tip_geometry`, `test_degenerate_footprint_still_returns_a_target` and `test_determinism` keep the `perimeter_faces` assertions and drop the `target_points` ones (the determinism test compares `perimeter_faces(cells)` with `perimeter_faces(reversed(cells))`)"; the import line drops the deleted names | — |
  "If Jordan wants approach alignment to matter, the place is a term inside `_compute_atom_sides`'s reading, not a second geometry." (Decided on the ladder by the source, steps 2 and 5.)
- WHERE: `modules/mass_battle/hierarchy/units.py` (`_effective_reach`, `MB_REACH_FACING_GATE`, `__all__`, the reach comment); `tools/ci_golden_modes_check.py` (one key); `modules/mass_battle/perimeter.py` (six names, docstring); `tests/valoria/test_reach_weapon_class.py` (one test); `tests/valoria/test_perimeter_geometry.py` (two tests deleted, four narrowed, the import).
- TESTS: the narrowed perimeter tests, green before (on the old names) and after; `tests/valoria/test_body_primitive.py::test_front_reach_engages_only_in_front` green unedited (it holds the facing rule's one owner).
- FALSIFIER and CONTROL: "a mass-battle golden that moves on D2a: then something read `MB_REACH_FACING_GATE` or the deleted functions by a route the grep did not see; stop and find it." Control: `R(0)` hash equal to B03.05's; `R(2)` hash equal to B02's close (seed 2 sees a fought field at one season, CIP part 2 §5 note 3).
- GATE: `python tools/ci_golden_modes_check.py` → exit 0; `python -m pytest tests/valoria/test_perimeter_geometry.py tests/valoria/test_reach_weapon_class.py tests/valoria/test_body_primitive.py -q` → green; `python -c "import modules.mass_battle.perimeter, modules.mass_battle.hierarchy.units"` → exit 0; `grep -rn "MB_REACH_FACING_GATE\|_effective_reach\|target_points\|nearest_target\|approach_alignment\|TargetPoint\|SHARP_TIP_DEG" engine modules systems tools tests --include=*.py` → no hit. The source's "mass-battle goldens under `engine/tests/` unchanged (`-m mass_battle` at the close, once)" is read in the BATCH GATE (moved there, §5.8).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `hierarchy/units.py::_effective_reach`, `::MB_REACH_FACING_GATE`; `tools/ci_golden_modes_check.py` (the `MB_REACH_FACING_GATE` key); `perimeter.py::TargetPoint`, `::target_points`, `::nearest_target`, `::approach_alignment`, `::SHARP_TIP_DEG`, `::_vertex_interior_angle`; `geometry.reach_reaches`; V12 B03.05 (same file `units.py`, earlier commit).
- GLOSSARY: none.
- COST and TIER: edit with test changes and one CI table row (the source's class); `sonnet`, `high`.
- LANDS IT: B03's producer; `Item: B03.06`, `[skip ci]`.

### B03.07 — two threadwork oracle files nothing imports · 17_CENSUS_C1B_01 D3 with 17_CENSUS_C1B_03 C-4, C-5 · BUILD · HASH EQUAL
- SOURCE: `proposals/17_CENSUS_C1B_01_deletions.md` "Batch D3 · two oracle files nothing imports"; `proposals/17_CENSUS_C1B_03_corrections.md` C-4, C-5 ("ride D3"); its head (C-U5a-19): "D3's whole-file deletion of `co_movement.py` supersedes `17_CENSUS_REST_1_deletions.md` D1 row 6"; ladder steps 2 and 5 (the source's).
- ADVANCES: none of the nine.
- INSTRUCTION (one commit; copied): "Delete `systems/threadwork/sim/threadcut.py` (200 lines) and `systems/threadwork/sim/co_movement.py` (141 lines)."
  | edit | where |
  |---|---|
  | `git rm` the two files | — |
  | C-4: delete the two lines `  - co_movement: Co-Movement Version C + 15 cards (Part 4)` and `  - threadcut: Threadcut beings (Part 6)` | `systems/threadwork/sim/__init__.py` (module docstring) |
  | C-5: `sim_module: systems/threadwork/sim/co_movement.py` → `sim_module: null`; `sim_module: systems/threadwork/sim/threadcut.py` → `sim_module: null` ("the file's own form for 'no module', `tools/mechanics_index_gen.py`"; "`test_status: not_implemented` stays and is now true of both") | `registers/mechanics_index.yaml`, rows `co_movement`, `threadcut_beings` |
  | "re-derive, never hand-edit: `python tools/export_sim_params.py --build` (both files' constants are in `engine/engine_params/sim_params.json`)" | exporter output (`value_pointer_links.json` is already gone, B03.01) |
  | H-326, inside `hole:`: ``the Church-attention pool in `systems/threadwork/sim/co_movement.py`, not read by the season loop`` → ``the Church-attention pool, drafted only in the retired `systems/threadwork/sim/co_movement.py` (`FORK:` row) and never read by the season loop`` | `engine/season/hole_register.yaml` |
  | ``struck at position 27 in co_movement.py and opposing.py alike`` → ``struck at position 27 in opposing.py`` | `systems/threadwork/sim/operations.py` (comment) |
  | two `FORK:` rows (below) | `references/restructure_ledger.md` |
  "`FORK:` row text (the sha is the last commit that holds the files; `b8039982` holds them unchanged today, so use it or the parent of the deleting commit)":
  ```
  | `systems/threadwork/sim/threadcut.py` | `FORK:b8039982` | FORKED (census C1B, D3: an [ASSUMPTION]-graded draft of threadcut beings; no importer, no test, a module-level registry with no carrier in the season World; the directory's move to `modules/threadwork/` deletes module stores, and every function here reads or writes one. Design text: `threadwork_v30.md` Part 6, quarantined) |
  | `systems/threadwork/sim/co_movement.py` | `FORK:b8039982` | FORKED (census C1B, D3: the co-movement deck; no importer, no test; its one computed output, `ms_delta`, was reported and written nowhere since plan position 27, and its deck is persistent state with no carrier. Design text: `threadwork_v30.md` Part 4, quarantined) |
  ```
  `git cat-file -e b8039982:systems/threadwork/sim/threadcut.py` succeeds at `aa31fd2`. `registers/handoffs/HANDOFF_IN_history.md` "also names `co_movement.py`; it is a history file and stays as written." The source's `tests/valoria/test_flow_skeletons.py` edits are not carried (B02.03 deleted the file).
- WHERE: DELETE `systems/threadwork/sim/threadcut.py`, `systems/threadwork/sim/co_movement.py`; `systems/threadwork/sim/__init__.py`; `registers/mechanics_index.yaml` (two `sim_module:` values); `engine/engine_params/sim_params.json` (re-derived); `engine/season/hole_register.yaml` (H-326 `hole:`); `systems/threadwork/sim/operations.py` (one comment); `references/restructure_ledger.md` (two rows).
- TESTS: none added; covering: `tests/valoria/test_export_sim_params.py`, `tests/valoria/test_export_game_constants_ambiguity.py` (the two test readers of `sim_params.json`, `grep -rl sim_params.json tests`).
- FALSIFIER and CONTROL: "For D3, an `ImportError` anywhere in the import probe of `audits/17_CENSUS_C1B.md` §5 run 3, re-run after the deletion"; C-4/C-5's: "`grep -rn "threadcut\.py\|co_movement\.py" engine modules systems registers references tests tools` returns only the two `FORK:` rows, the reworded H-326 sentence and the history line named above." Control: `R(0)` hash equal to B03.06's.
- GATE: `python tools/export_sim_params.py --check` → current; `python tools/freshness_gate.py` → exit 0; `python tools/mechanics_index_gen.py` → no new warning for the two rows ("a `null` `sim_module` is a declaration there, not a violation"); `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `python -c "import systems.threadwork.sim"` → exit 0; `python -m pytest tests/valoria/test_export_sim_params.py tests/valoria/test_export_game_constants_ambiguity.py -q` → green; the two new rows read through `pathres.load_alias_map()[0]` (as B03.01) → present.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `systems/threadwork/sim/threadcut.py`, `co_movement.py`, `__init__.py` (the two docstring lines), `registers/mechanics_index.yaml` rows `co_movement`, `threadcut_beings`, `hole_register.yaml` H-326, `operations.py` (the comment); V12 B03.01 (`value_pointer_links.json` deleted first, so the rebuild has one artifact; CIP CI-04's "CI-10 first").
- GLOSSARY: none.
- COST and TIER: small build, cross-lane on `registers/`, `references/` and the exporter output (the source's class); `sonnet`, `high`.
- LANDS IT: B03's producer; `Item: B03.07`, `[skip ci]`.

### B03.08 — a docstring that names a module by its old name · 17_CENSUS_C1B_03 C-1 · BUILD · HASH EQUAL
- SOURCE: `proposals/17_CENSUS_C1B_03_corrections.md` "C-1 · `systems/combat/combat_engine_v1/capabilities.py` (`_affords_point`) — stands alone".
- ADVANCES: none of the nine.
- INSTRUCTION (copied): in `_affords_point`'s docstring,
  | old | new |
  |---|---|
  | `Local import (systems.py sits above this module in the dependency order` | `Local import (combat_systems.py sits above this module in the dependency order` |
  | `the weapon's DERIVED afforded-heads set (systems.afforded_heads` | `the weapon's DERIVED afforded-heads set (combat_systems.afforded_heads` |
  | `and systems.select_mode already lets it SELECT that spike` | `and combat_systems.select_mode already lets it SELECT that spike` |
  "The module docstring's phrase it quotes, 'pure data; no systems/core at module scope', is left as quoted … changing one and not the other would make the quotation false."
- WHERE: `systems/combat/combat_engine_v1/capabilities.py` (`_affords_point` docstring).
- TESTS: none.
- FALSIFIER and CONTROL: "After C-1, `grep -n "systems\.\(afforded_heads\|select_mode\)\|systems\.py" systems/combat/combat_engine_v1/capabilities.py` returns only the quoted phrase" in the module docstring. Control: the file's AST unchanged (`python -c "import ast; ast.parse(open('systems/combat/combat_engine_v1/capabilities.py').read())"` before and after, `ast.dump` equal but for the docstring constant).
- GATE: `python tools/valoria_local.py --staged` → green ("cheap, no pytest"); the falsifier's grep → the quoted phrase only.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `systems/combat/combat_engine_v1/capabilities.py::_affords_point` (the three strings, opened at `aa31fd2`). (B13's `CI-09` later re-points this tree's imports; this edit is docstring text and does not depend on it.)
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high` (the source's tier; `haiku` would do).
- LANDS IT: B03's producer; `Item: B03.08`, `[skip ci]`.

### B03.09 — two dead fields: a roll's `pool_size`, a unit row's `merged_cells` · 17_CENSUS_REST_1 D1 rows 1, 3 · BUILD · HASH EQUAL
- SOURCE: `proposals/17_CENSUS_REST_1_deletions.md` "D1 — six dead fields", rows 1 and 3 (row 2 is B03.28, rows 4–5 B03.05, row 6 withdrawn); C-U5a-18 ("#1 stands"); U3 §4.1 rows 9–10 (row 1 lands in B03; B05 re-reads `dice_engine.py` after it).
- ADVANCES: none of the nine.
- INSTRUCTION (copied; "Cut test for each: delete the field, run the one file named, same-seed hash unchanged"):
  | # | field | exact edit | test edit | file to run |
  |---|---|---|---|---|
  | 1 | `RollResult.pool_size` | `engine/dice_engine/dice_engine.py`: delete the field; in `roll_pool`'s return drop `pool_size=effective_pool,` (the parameter `pool_size` of `roll_pool` stays) | `tests/valoria/test_dice_engine_properties.py`: "delete the three-line assertion" on `result.pool_size`; the next assertion "already asserts `len(result.rolls) == expected_effective`, the same fact" | `tests/valoria/test_dice_engine_properties.py` |
  | 3 | `Subunit.merged_cells` | `modules/mass_battle/hierarchy/units.py`: delete the field; drop `; self.merged_cells = set()`; delete the line that reads it; drop the name from the docstring list | none | `tests/valoria/test_mass_battle_maneuvers.py` |
  "At this tree `pool_size == len(rolls)` by construction." "No `FORK:` row: no file is deleted."
- WHERE: `engine/dice_engine/dice_engine.py` (`RollResult.pool_size`, `roll_pool`'s return); `tests/valoria/test_dice_engine_properties.py` (one assertion); `modules/mass_battle/hierarchy/units.py` (`Subunit.merged_cells` and its three sites).
- TESTS: the two files named; green before and after.
- FALSIFIER and CONTROL: "a reader exists that the grep missed; the named test file, or an `AttributeError` at import, shows it" — `grep -rn "\.pool_size\b\|merged_cells" engine modules systems tools tests --include=*.py` → no read of either field. Control: `R(0)` and `R(2)` hashes equal to B03.08's and B03.06's (seed 2 reaches the field; `RollResult` and `Subunit` are not `World` carriers).
- GATE: `python -m pytest tests/valoria/test_dice_engine_properties.py tests/valoria/test_mass_battle_maneuvers.py -q` → green; `python -m engine.season.harness.register --requirements` → unchanged from B02's close.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `dice_engine.py::RollResult.pool_size`, `::roll_pool`; `hierarchy/units.py::Subunit.merged_cells`; V12 B03.05, B03.06 (same file `units.py`, earlier commits).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B03's producer; `Item: B03.09`, `[skip ci]`.

### B03.10 — two phantom contract rows · 17_CENSUS_REST_1 D4 · BUILD · HASH EQUAL
- SOURCE: `proposals/17_CENSUS_REST_1_deletions.md` "D4 — two phantom contract rows in `references/module_contracts.yaml`".
- ADVANCES: none of the nine; the IN → resolver → OUT reading (CLAUDE.md §9) loses two rows that describe nothing.
- INSTRUCTION (copied): "`settlement_economy` and `campaign_architecture`: `sim_module: none`, `wiring.godot: retire`, `port_rank: 9`; their own notes read 'phantom (in-3/out-0); ED-SE-0005 folds it into settlement_layer' and 'reclassified: a consolidation doc, not a runtime module'.
  - Delete both rows. Edit the head comment (`status: EXTRACTED_STAGE1   # campaign_architecture stub remains`) to drop the trailing comment. `references/canonical_sources.yaml`'s `campaign_architecture` entry points at the quarantined document, not at this row, and stays.
  - The other 16 code-less rows stay: each declares itself code-less (`sim_module: none`, `wiring.build: design|deferred`) and is the design ledger the IN → resolver → OUT reading uses. Their stale narration is accepted and nothing is written (§0.1 pt 5)." Before the edit, record `grep -n "settlement_economy\|campaign_architecture" references/module_contracts.yaml` in the commit body ("before: the two rows, the `:27` comment and one history note").
- WHERE: `references/module_contracts.yaml` (`modules:` rows `settlement_economy`, `campaign_architecture`; the head `status:` comment).
- TESTS: none added; covering: `tests/valoria/test_wiring_validation.py` (`validate_wiring`'s falsifier, `tools/export_composition.py`'s docstring).
- FALSIFIER and CONTROL: "a `with:` join or a `transitions:` row in a surviving contract names either module; `grep -n "settlement_economy\|campaign_architecture" references/module_contracts.yaml` after the edit shows it" (the one history note may remain, named in the commit body). Control: `R(0)` hash equal to B03.09's (nothing at runtime reads `modules:` rows' notes).
- GATE: `python tools/export_composition.py --check` → "`OK — 16 role(s) … wiring valid for 24 module(s)`" (26 at `aa31fd2`); `python tools/ci_quantity_vocabulary_check.py` → "unchanged in verdict"; `python -m pytest tests/valoria/test_wiring_validation.py -q` → green.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `references/module_contracts.yaml` rows `settlement_economy`, `campaign_architecture`, the `status: EXTRACTED_STAGE1` comment; `tools/export_composition.py::validate_wiring`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B03's producer; `Item: B03.10`, `[skip ci]`.

### B03.11 — the driver imports what it uses · CI-08 · BUILD · HASH EQUAL
- SOURCE: `master/CODEBASE_IMPROVEMENT_PROPOSAL_part2.md` "CI-08 · The driver imports what it uses"; CIP §2 ("**B03**, after the census deletions"); closes H-09.
- ADVANCES: none of the nine; reading cost of the hottest loop file.
- INSTRUCTION (copied):
  "**Preserved:** every import-time registration. Three of the driver's import statements name modules that register tables when imported: `..seam` (the providers; `seam/__init__.py`: *'IMPORTING `wrappers` IS WHAT REGISTERS THE PROVIDERS'*), `..loop.effects` (the `@effect_for` bodies) and `..loop.predicates`. Where every name of such a statement is unused, **the statement becomes a bare module import with its reason in a comment**; it is not deleted." "The lane re-derives the list on its base (the file will have moved) rather than trusting this one" (79 names at `4dc8a7b`, CIP's list).
  1. "Re-derive the list (ten lines of `ast`: names bound by `Import`/`ImportFrom` at module scope minus the `ast.Name` ids in the module). Note that the bindings at the foot of the file import the seven steps and are read there." The list goes in the commit body.
  2. "Delete each unused name from its statement. A statement left empty is deleted, **except** the three registering modules above, which become `from .. import seam  # registers the providers` and the like."
  3. "Rewrite the docstring's two paragraphs [that say the unused names are held for `sweep_core.py`] as one sentence: the driver constructs the tokens, binds the seven steps and owns `resolvable_verbs`."
  4. "`engine/reference/degree-sweep/sweep_core.py`: no change."
- WHERE: `engine/season/loop/driver.py` (module-scope imports; module docstring).
- TESTS: "None added. Covering: the two tests that import the sweep arms (`engine/season/tests/test_season_shape.py`), `tests/valoria/test_engine_does_not_import_systems.py`."
- FALSIFIER and CONTROL: "In a scratch worktree: delete the `..seam` import outright → the realm run must fail or its hash move (the control sees a lost registration). Restore. Delete one name the driver does read (`Token`) → the import must fail." Both plants are run before the edit and their readings recorded in the commit body. Control: `R(0)`, `R(2)` and the NPC-088 headless hash equal to B03.10's readings ("an unregistered provider or effect would refuse the first contest or write and move the hash").
- GATE: `python -c "import engine.season.loop.driver"` → exit 0; `python -c "import runpy; runpy.run_path('engine/reference/degree-sweep/sweep_core.py')"` → exit 0; `R(0)`, `R(2)` hashes equal to B03.10's; `python -m pytest tests/valoria/test_engine_does_not_import_systems.py -q` → green; `python -m pytest engine/season/tests/test_season_shape.py -q -k sweep` → green `[ASSUMPTION: `-k sweep` selects the two sweep-arm tests — basis: CIP names them by what they import, not by name; the producer confirms the selection prints two or more tests]`.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `engine/season/loop/driver.py` (its imports; `resolvable_verbs`); `engine/reference/degree-sweep/sweep_core.py`; V12 B03.02–B03.10 (the census deletions first, §2.2).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `medium` (CIP).
- LANDS IT: B03's producer; `Item: B03.11`, `[skip ci]`.

### B03.12 — the obstacle composer is reached by its own composition row · CI-03 · BUILD · HASH EQUAL
- SOURCE: `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` "CI-03 · The obstacle composer is reached by its own composition row"; CIP §2 ("after `17_CENSUS_REST_1` D4 (it edits `references/module_contracts.yaml` first)"); closes H-05. Earning: `architecture/holonic_ARCHITECTURE.md` §43 (a registered module is attached by a registry row, never an import).
- ADVANCES: none of the nine; one route to the obstacle every contest and every believed odds reads.
- INSTRUCTION (copied):
  1. "`references/module_contracts.yaml`, under `composition_roles:`, directly after the `social_contest.roll` row:
     ```yaml
       social_contest.obstacle:
         target: "modules.social_contest.roll:obstacle"
         entry: query
         needed_by: "engine/season/seam/wrappers/sigma.py — `_composed_obstacle` (the obstacle a contest is rolled against and the one believed odds read), called by role."
     ```
     No `verb:` (a `query` entry names none; `tools/export_composition.py` `_ENTRIES`)."
  2. "`python tools/export_composition.py` (rewrites `engine/engine_params/composition.json`; never by hand)."
  3. "`engine/season/seam/wrappers/sigma.py`: replace [`_ROLL_ROLE = "social_contest.roll"`] with `OBSTACLE_ROLE = "social_contest.obstacle"` and `QUERY_ENTRIES = ((OBSTACLE_ROLE, "query"),)`; replace the body of `_composed_obstacle` with `return composition.require(OBSTACLE_ROLE)(inp)` and a one-line docstring; delete `import importlib` (it has no other use in the file)."
  4. "`engine/season/loop/driver.py`: `require_entries(world_q.QUERY_ENTRIES + MATTER_STEP_CALLS)` gains `+ sigma.QUERY_ENTRIES`, importing the name from `..seam.wrappers.sigma` beside the existing `..seam` import (`loop/` already imports that file: `loop/deliberate.py`), so a missing row is refused at driver construction as the other host needs are (`manifest/registrar.py::require_entries`)."
- WHERE: `references/module_contracts.yaml` (`composition_roles:` new row `social_contest.obstacle`); `engine/engine_params/composition.json` (re-derived); `engine/season/seam/wrappers/sigma.py` (`_ROLL_ROLE` → `OBSTACLE_ROLE`, `QUERY_ENTRIES`, `_composed_obstacle`, the `importlib` import); `engine/season/loop/driver.py` (the `require_entries` call and one import); `engine/season/tests/test_social_contest_module.py` (one test); `tests/valoria/test_module_registrar.py` (only if an assertion lists production rows by name).
- TESTS: "Add to `engine/season/tests/test_social_contest_module.py`: `test_the_obstacle_is_reached_by_its_own_composition_row`: with `composition._CACHE["social_contest.obstacle"]` replaced (and restored) by a stub returning `7.0`, `sigma._composed_obstacle(inp)` returns `7.0` for any `SocialContestInput`. It executes the route." Written before step 3 and read red (no such row). "Change: whichever assertion in `tests/valoria/test_module_registrar.py` counts or lists the production entry rows gains the new role": at `aa31fd2` the set is derived from the rows (`production = sorted(r for r, row in composition.ROLES.items() if row.get("entry") …)`), so no edit is expected; the commit body says which.
- FALSIFIER and CONTROL: "In a scratch worktree, before the edit: make `modules/social_contest/roll.py::obstacle` return its value plus `1.0` → the seed-0 realm hash must move (the control sees the path). Revert. After the edit: misspell the new row's target (`roll:obstacel`) → `export_composition.py --check` must exit non-zero; that is the failure the reflective call could not give. Revert." Control: `R(0)` and NPC-088 headless hashes equal to B03.11's.
- GATE: `python tools/export_composition.py --check` → current, "17 roles" (`OK — 17 role(s) … wiring valid for 24 module(s)`); `grep -n "import_module" engine/season/seam/wrappers/sigma.py` → nothing; `python -m pytest engine/season/tests/test_social_contest_module.py tests/valoria/test_module_registrar.py -q` → green; `R(0)` and NPC-088 headless hashes equal to B03.11's ("the headless and realm hashes equal the opening reading").
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `seam/wrappers/sigma.py::_ROLL_ROLE`, `::_composed_obstacle`, the `importlib` import; `modules/social_contest/roll.py::obstacle`; `engine/substrate/composition.py::require`, `::_CACHE`; `manifest/registrar.py::require_entries`; `loop/driver.py` (the `require_entries(world_q.QUERY_ENTRIES + MATTER_STEP_CALLS)` call); V12 B03.10 (same file `module_contracts.yaml`, earlier), B03.11 (same file `driver.py`, earlier: the import list B03.11 re-derived gains one name here).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `medium` (CIP).
- LANDS IT: B03's producer; `Item: B03.12`, `[skip ci]`.

### B03.13 — the `domain_actions` contract row is retired · IS-B3-SE-04 · BUILD · HASH EQUAL
- SOURCE: `master/instructions/IS_B3_FA_SE_WR_GO.md` "Item: IS-B3-SE-04" (U4 G-7); `IS_B3_FA_SE_WR_GO_part2.md` §7.1 ("SE-04 after CI-03"); rulings A-10; ED-IN-0232 (the Key substrate retired); ladder steps 1 and 2 (the source's).
- ADVANCES: the settlement scale's row in `requirements.yaml` `scales:` (its note says "no domain-action mechanism exists"); hygiene. No conjunct is read.
- INSTRUCTION (copied, with step 4 dropped):
  "`references/module_contracts.yaml` carries, in its `modules:` list, `module: domain_actions` with `doc: null`, `registry_system: "da_framework"   # Key Type Registry vocabulary` and `accounting_phase: [DA_proposal]`, and in `accounting_sequence:` a phase `DA_proposal` that names functions (`select_proposal()`, `execute_proposed_domain_actions()`) no file defines. … the acts a 'domain action' named are verb rows carried by `14_VERBS_MATERIAL_A` to `_C` (`found`, `build`, `work`, `tend`, `restore`, `requisition`).
  (1) First open every parser of the `modules:` block: `grep -rl "module_contracts" tools/*.py` lists thirteen files at this SHA [13 at `aa31fd2` too]; for each, read whether it iterates `modules:` and whether a test pins the row count; list them in the commit.
  (2) Delete the `domain_actions` row, the `DA_proposal` phase, and `DA_proposal` from the `accounting_phase` list of the row [`faction_state`'s `accounting_phase: [DA_proposal, settlement_accounting]`, which becomes `[settlement_accounting]`].
  (3) Reword the `scales:` note in `engine/season/requirements.yaml`: 'declares `domain_actions` and `settlement_economy`' becomes a statement that the settlement scale's acts are the MATERIAL verb rows."
  The sentence (3) writes, replacing "`references/module_contracts.yaml` declares `domain_actions` and `settlement_economy` — BOTH with `doc: null`, two of the nine contracts §6 counts as unimplementable." in the `settlement management / city building / domain actions` row's note: "The settlement scale's acts are the MATERIAL verb rows of `verb_table.yaml` (`found`, `build`, `work`, `tend`, `restore`, `requisition`); `references/module_contracts.yaml` declares no `domain_actions` or `settlement_economy` contract (both retired: A-10, ED-IN-0232)." `[ASSUMPTION: the sentence's wording — basis: the source states its sense, not its text]`. The rest of the note stays (B03.17 rewords its `restore` clause).
  The falsifier's "provisional banner of `references/action_vocabulary.yaml`, which is reworded in the same commit": its two comment passages, "`# ⚠️ STATUS: PROVISIONAL — NOT the authoritative domain-action registry (the `domain_actions`` / `# home is unbuilt; see `blocked_on`)`" and "`# awaiting/pending: this roster is provisional until the authoritative domain_actions` / `# home is authored; regenerate or fold in then. ED-FA-0002 is OPEN …`", become "`# ⚠️ STATUS: PROVISIONAL — there is no domain-action registry to defer to: the `domain_actions` contract row is retired (A-10: a faction's acts are persons' verbs via their seats; ED-IN-0232).`" and "`# provisional: the strategic layer's acts are rows of `engine/season/verb_table.yaml`. ED-FA-0002 is CLOSED by its superseding row of 2026-10-06 (`registers/editorial_ledger_fa_archive.jsonl`); `blocked_on` keeps its value as a record.`" `[ASSUMPTION: wording; the key `blocked_on:` is kept because removing it is not in the source; no code reads it (`grep -rn blocked_on skills tools`)]`.
  Not written: the source's step (4), "Append a superseding row for `ED-FA-0002` … to `registers/editorial_ledger_fa.jsonl`": the row's last entry already closes it (fact 3 at this part's head; ladder step 1). "No `FORK:` row: no file is deleted."
- WHERE: `references/module_contracts.yaml` (`modules:` row `domain_actions`; `faction_state`'s `accounting_phase`; `accounting_sequence:` phase `DA_proposal`); `engine/season/requirements.yaml` (`scales:` row "settlement management / city building / domain actions", `note:`); `references/action_vocabulary.yaml` (two comment passages).
- TESTS: none added; covering: `tests/valoria/test_wiring_validation.py`, and any test step (1) finds that pins the `modules:` row count.
- FALSIFIER and CONTROL: "`python tools/export_composition.py --check` is current before and after (it reads `composition_roles:` only; if it moves, the edit touched the wrong block). Each parser found in step 1 runs its own check. `grep -rn "domain_actions\|DA_proposal" references engine tools` prints only the provisional banner of `references/action_vocabulary.yaml`" (and, after this edit, the new requirements sentence naming the retired row). Control: `R(0)` hash equal to B03.12's.
- GATE: `python tools/export_composition.py --check` → `OK — 17 role(s) … wiring valid for 23 module(s)`; `python -m engine.season.harness.register --requirements` → "loads and prints the nine"; `python tools/validate_ed_citations.py` → "passes".
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `references/module_contracts.yaml` row `domain_actions`, phase `DA_proposal`, `faction_state.accounting_phase`; `engine/season/requirements.yaml` `scales:` (the note survives B02: B02.31 edits the `scales:` block's `conjunct:` keys, its header and its first row's note only); `registers/editorial_ledger_fa_archive.jsonl` ED-FA-0002 (closed); V12 B03.10, B03.12 (`module_contracts.yaml`, earlier: "`17_CENSUS_REST_1` D4 first, then CI-03, then this"); V12 Batch B02 (B02.31).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B03's producer; `Item: B03.13`, `[skip ci]`.

### B03.14 — the season's settings are in the typed export · CI-04 · BUILD · HASH EQUAL
- SOURCE: `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` "CI-04 · The season's 101 settings are in the typed export"; CIP §2 ("after `17_CENSUS_C1B_01` D3 (it rebuilds `sim_params.json` first)"); closes H-04 (part). Earning: CLAUDE.md §5.
- ADVANCES: none of the nine; every setting a value the port reads from a typed artifact with a blocking round-trip (CLAUDE.md §5).
- INSTRUCTION (copied):
  "**What dies.** Nothing. **What is added** is the smallest thing that closes the chain: one more reader in the existing exporter."
  1. "`tools/export_sim_params.py`: a function `_setting_rows() -> list` that parses `engine/season/data/fixtures.py`, finds the module-scope assignment whose target is `DEFAULT_FIXTURES` and whose value is a call to `Fixtures`, and for each `keyword` whose value `_literal()` accepts (the file's own anti-fabrication reader) emits a row of the exporter's own shape `{key, name, value, kind, module, file, note}` with `module: "engine.season.settings"`, `key: "engine.season.settings.<name>"`, `file: "engine/season/data/fixtures.py"` and `note` the trailing comment of that line where one exists. A keyword whose value is not a literal (the five table names) is skipped and counted. The build appends these rows; `by_module` gains the key."
     Read at `aa31fd2` and added to the copy: the module-scope rows also carry `citation` and `citation_grade` (`_citation(note)`, `_citation_grade(...)`), so each setting row carries both, one shape for every row `[ASSUMPTION: CIP's shape list predates or omits the two provenance keys]`; `_literal()` returns `None` for a `None` literal and for a non-literal alike, and the module-scope loop also drops values `_is_numericish` refuses, which `_setting_rows` does not apply (a setting may be a bool or a string) `[ASSUMPTION: CIP names `_literal` alone as the filter]`.
  2. "The count the build prints states how many settings it read and how many it skipped, and the build **raises** if it read none (an assertion that it asserted, CLAUDE.md §0.1 pt 2: a renamed `DEFAULT_FIXTURES` must not produce a smaller artifact that still checks green)."
  3. "`python tools/export_sim_params.py --build`; commit the artifact with the tool."
  4. "`python tools/export_game_constants.py --check` (it composes from `sim_params.json`): expected current, because no mapped constant's key changes. If it is not, the new keys collided with a mapped name: give the setting rows the distinct module key above and rebuild."
- WHERE: `tools/export_sim_params.py` (`_setting_rows`; the build's append, `by_module`, the printed count); `engine/engine_params/sim_params.json` (re-derived); `tests/valoria/test_export_sim_params.py` (one test).
- TESTS: "Add to `tests/valoria/test_export_sim_params.py`: `test_the_season_settings_are_exported_and_a_rename_cannot_empty_them`: the artifact holds a row `engine.season.settings.pool_default` whose value equals `DEFAULT_FIXTURES.get("pool_default")`; the count of setting rows is at least 90; and pointing `_setting_rows` at a source with no `DEFAULT_FIXTURES` raises." Written before step 1 and read red (no row). Covering: `tests/valoria/test_export_game_constants_ambiguity.py`.
- FALSIFIER and CONTROL: "In a scratch worktree: change `pool_default=2` to `3` in `fixtures.py` without rebuilding → `--check` must exit 1. Revert → `current`." Control: `R(0)` hash equal to B03.13's ("nothing at runtime reads the artifact").
- GATE: `python tools/export_sim_params.py --check` → `[SIM-PARAMS] current`; `python tools/export_sim_params.py --search pool_default` → prints the row; `python tools/export_game_constants.py --check` → current; `python -m pytest tests/valoria/test_export_sim_params.py tests/valoria/test_export_game_constants_ambiguity.py -q` → green.
- HASH MOVERS: none; "`sim_params.json` is regenerated."
- DEPENDS ON: EXISTS-IN-TREE `tools/export_sim_params.py::_literal`, the module-scope record loop; `engine/season/data/fixtures.py::DEFAULT_FIXTURES` (`DEFAULT_FIXTURES = Fixtures(` at module scope, opened at `aa31fd2`); `tools/export_game_constants.py`; V12 B03.07 (`17_CENSUS_C1B_01` D3, "rebuilds the same artifact, earlier in B03"), B03.01 ("CI-10 first (it deletes `value_pointer_links.json`, which would otherwise need rebuilding against the new rows)").
- GLOSSARY: none (a *setting* is a `Fixtures` field, `unified/U1_GLOSSARY.md` §H, CIP's words).
- COST and TIER: edit; `sonnet`, `medium` (CIP).
- LANDS IT: B03's producer; `Item: B03.14`, `[skip ci]`.

### B03.15 — the realm's arms are in the same export · CI-05 · BUILD · HASH EQUAL
- SOURCE: `master/CODEBASE_IMPROVEMENT_PROPOSAL.md` "CI-05 · The realm's seven arms are in the same export"; closes H-04 (the rest).
- ADVANCES: none of the nine; the realm's shipped arm defaults readable by the port.
- INSTRUCTION (copied): "**What dies.** Nothing. **Preserved:** the defaults and every call that overrides one." ("Why not make them settings": rejected by the source; seven settings would be seven register rows.)
  1. "`tools/export_sim_params.py`: `_realm_arm_records()` parses `engine/season/harness/populated.py`, finds `def build_realm`, and for each parameter with a literal default emits a row with `module: "engine.season.realm"`, `key: "engine.season.realm.<param>"`. It raises if `build_realm` is not found. (If CI-07 has moved the builder, the path constant is the one line that changes; it is read from `engine/season/data/files.py` if CI-07 added one there.)" CI-07 has not moved it at B03 (it is B03c): the path is `engine/season/harness/populated.py`, and B03c's `CI-07` re-points this one line (serial edge, `tools/export_sim_params.py` B03 → B03c). Rows carry the same keys as B03.14's.
  2. "Rebuild in the same commit as CI-04's rebuild if both are in flight; otherwise `--build` again." (CI-04 committed in B03.14: `--build` again.)
  The source's `[ASSUMPTION]` on `cap`, read at `aa31fd2`: `_literal()` is `ast.literal_eval` returning `None` on failure, so `cap: int | None = None` cannot be told from a non-literal and is skipped; the arms emitted are `seed` and the seven booleans `from_roster`, `goals`, `goals_complete`, `foreign`, `guards`, `acquaintances`, `cast_attributes` (`build_realm`'s signature at `aa31fd2`).
- WHERE: `tools/export_sim_params.py` (`_realm_arm_records`; the build's append); `engine/engine_params/sim_params.json` (re-derived); `tests/valoria/test_export_sim_params.py` (CI-04's test extended).
- TESTS: "Extend CI-04's test: the artifact holds `engine.season.realm.cast_attributes` with value `False` and `engine.season.realm.foreign` with value `True` (the shipped defaults, `audits/25_GROUNDING_ENGINE.md` L-08)." The two values are the B02-closing tree's: read `build_realm`'s signature at the item's open and assert what it ships (B01's lane-A commits may move a default; the commit body names any that differ from L-08). Written before step 1, read red.
- FALSIFIER and CONTROL: "flip `cast_attributes` to `True` in a scratch worktree → `--check` exits 1." Control: `R(0)` hash equal to B03.14's.
- GATE: `python tools/export_sim_params.py --check` → current; `python tools/export_sim_params.py --search engine.season.realm` → "prints the seven arms and `seed`"; `python -m pytest tests/valoria/test_export_sim_params.py -q` → green.
- HASH MOVERS: none.
- DEPENDS ON: V12 B03.14 ("Depends on: CI-04"); EXISTS-IN-TREE `engine/season/harness/populated.py::build_realm`.
- GLOSSARY: none (an *arm* of `build_realm` is one of its boolean parameters, the tree's own word in `build_realm`'s docstring: "the CONTROL ARM").
- COST and TIER: edit; `sonnet`, `medium` (the same lane as CI-04, CIP).
- LANDS IT: B03's producer; `Item: B03.15`, `[skip ci]`.

### B03.16 — no stored plan: the queue-reuse branch that never fires · 16_PESSIMIST_CORE_no_stored_plan · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_CORE_no_stored_plan.md` "The resolution, decided", "Exact edits, by owner", "Gate", "Falsifier"; ladder step 5 (the source's); closes F-PES-CORE-07.
- ADVANCES: none of the nine; about a hundred lines and one per-lap computation leave.
- INSTRUCTION (copied; the tree's identifier `self.round` is kept: PCR-4 renames it in B04; prose says *lap*):
  "Delete the reuse branch and its fingerprint. … `_drop_what_was_already_done` and `_qualify_by_round` stay: both act on the freshly chosen list."
  Order of edits: "**Before deleting** … this check, then edit 1, then 2, then 3": "`rg -n '_inputs_fingerprint|_queued\b|\._inputs\b' engine/` must return only the lines edits 1-3 delete (run 2026-11-12, it returns `deliberate.py`, `driver.py`, `test_season_shape.py`, `test_in53_vacancy_need.py` sites, and four `cite:` strings in `engine/season/hole_register.yaml`, which are measured-history prose read by no code and stay as written; a hit anywhere else is a reader this proposal missed: stop)." The output goes in the commit body.
  1. "**`engine/season/loop/deliberate.py`**
     - [the branch] becomes `if b > 0:` followed by the existing `choose` / `as_scenes` / budget and slot checks / `_drop_what_was_already_done` / `_qualify_by_round`; `scenes` is that local list (empty when `b == 0`).
     - delete `fp = _inputs_fingerprint(p, qs)`, `self._inputs[p.id] = fp`, `self._queued[p.id] = scenes` and the function `_inputs_fingerprint` with its imports (`REQUIRES_STEMS`, `ledger_names` if no other use remains in the module).
     - keep `self._deliberated_at[p.id] = (w.tick, self.round)` (read by `_questions_at_barrier`)."
  2. "**`engine/season/loop/driver.py`** [the per-season reset] and `__init__`: drop `_queued` and `_inputs`."
  3. "**The two tests of the fingerprint** go with it: `engine/season/tests/test_season_shape.py` (`test_u2_the_inputs_fingerprint_is_complete_for_the_skip_it_licenses`, with its helper) and the fingerprint assertion in `engine/season/tests/test_in53_vacancy_need.py`. Both test that the skip is *safe*; with no skip there is nothing to keep safe. … Also strike the pointer comment at `test_season_shape.py` that names the deleted test." The two bodies are read before deletion ("located by grep, not read" in the source) and the commit body names what each asserted.
- WHERE: `engine/season/loop/deliberate.py` (the deliberation branch; `_inputs_fingerprint`; two imports if unused); `engine/season/loop/driver.py` (`__init__`, the per-season reset: `_queued`, `_inputs`); `engine/season/tests/test_season_shape.py` (`test_u2_the_inputs_fingerprint_is_complete_for_the_skip_it_licenses`, its helper, one pointer comment); `engine/season/tests/test_in53_vacancy_need.py` (one assertion).
- TESTS: the two deletions above; covering: `engine/season/tests/test_rem31_grid_suspension.py` (PART D 41a's permutation observable), `test_season_shape.py`, `test_in53_vacancy_need.py`.
- FALSIFIER and CONTROL: "Any pinned hash moves. Then some world does reuse a stored tail, the cut is not free there, and that world is the evidence this proposal lacked: keep the branch and cite it." Control: `R(0)`, `R(1)`, `R(2)` and the NPC-088 headless hash equal to B03.15's (the source's realm seed 0 three seasons and headless seed 0 four seasons are written at two seasons at most: the NPC-088 headless run at two seasons and the realm at one (four and three seasons in the source; A-114)).
- GATE: "`python -m engine.season.harness.report && python -m engine.season.harness.delta HEAD`, expected reading `PROBE FLIPS 0`"; `R(0)`, `R(1)`, `R(2)` hashes equal to B03.15's; `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` → `CONTENT HASH:` equal to B03.15's; "`engine/season/tests` goldens unchanged except the deleted reuse cases"; "`python -m pytest engine/season/tests/test_rem31_grid_suspension.py -q -k "deliberation_order or same_permutation"`" → green; `python -m pytest engine/season/tests/test_in53_vacancy_need.py -q` → green.
- HASH MOVERS: none ("No golden re-record expected; if one is needed the falsifier has fired").
- DEPENDS ON: EXISTS-IN-TREE `loop/deliberate.py::_inputs_fingerprint`, the `_queued`/`_inputs` reads, `_drop_what_was_already_done`, `_qualify_by_round`, `_deliberated_at`; `loop/driver.py` (`_queued`, `_inputs`); V12 B03.11, B03.12 (`driver.py`, earlier commits).
- GLOSSARY: none (prose *lap* for the season's pass; the identifier `round` until B04.01).
- COST and TIER: edit (a deletion); `sonnet`, `high` (the source's: "no judgment node").
- LANDS IT: B03's producer; `Item: B03.16`, `[skip ci]`.

### B03.17 — pointer and register text for files only the orchestrator edits · 09_WR_B_pointer_text_for_the_orchestrator edits 1–4 · BUILD · HASH EQUAL
- SOURCE: `proposals/09_WR_B_pointer_text_for_the_orchestrator.md` "The edits" 1–4, "The gate"; ladder step 1 (ED-IN-0232, ED-WR-0010); grouped as one item (one gate, one text-only change; E-13).
- ADVANCES: none of the nine; one head per subsystem, named where a reader looks first (CLAUDE.md §1).
- INSTRUCTION (copied):
  1. `CURRENT.md`, the narrative-engine row. Old: `| **Narrative engine** | `narrative_engine_design_v2_churn.md` — ED-IN-0011 | — |`. New (the source's four cells joined to the table's three, UNDECIDED (7)): `| **Narrative engine** | `engine/season/harness/` — `storybar.py`, `chronicle.py`, `strife.py`, `arc.py` (readings over the log, never carriers: ED-IN-0225); design intent `proposals/2026-11-04-strife-flows/00_MASTER.md` | ED-IN-0011 (history); ED-IN-0232; `registers/handoffs/HANDOFF_WR.md` |`. "`narrative_engine_design_v2_churn.md` stays where it is, unreferenced by the row."
  2. `CURRENT.md`, the threadwork row. Old: `| **Threadwork** | `threadwork_v30.md` + `thread_horizontal_integration_spec.md` | ED-WR-0010 (last row); `registers/handoffs/HANDOFF_WR.md` |`. New, "until `modules/threadwork/` exists": `| **Threadwork** | `systems/threadwork/sim/` (the oracle; Coherence per ED-WR-0010); design intent `threadwork_v30.md` (Part 3 superseded), `threadwork_applications.md`, `thread_horizontal_integration_spec.md` | ED-WR-0010 (last row); `registers/handoffs/HANDOFF_WR.md` |`. ("After the move … the code head becomes `modules/threadwork/`": that edit is `09_WR_threadwork_module`'s, not this item's.)
  3. `engine/season/requirements.yaml`, the settlement scale's note. Old (the clause): "in the realm only `restore` executes (cohorts mending / their own settlement's fabric since `24f`), while `found`, `build` and `work` are formed and / refused because no computed act declares a works (`H-165`);". New: "none of the four executes in the shipped realm: `restore` forms only / on a Site below a floor and no Site crosses one (wear-0 dwellings and garrisons; no wound, H-235/H-236), / and `found`, `build` and `work` are formed and refused because no computed act declares a works / (`H-165`);" (line breaks as the folded scalar takes them). "The row's `status:` is not moved by this text."
  4. `engine/season/hole_register.yaml`, "one sentence appended to each named row's cite … Each sentence is dated and attributed, in the register's own style; no row is re-graded except where said":
  | row | append to `cite` | re-grade? |
  |---|---|---|
  | H-05 | "CLOSED IN CODE (2026-11-12 audit, WR addendum B §6): `harness/populated.py::build_realm` is the world-generation roster's producer; `build_realm(0)` holds 83 persons (first WR audit E-13)." | `grade` stays; the empty cite is filled |
  | H-27 | "THE DEFAULT IS SUPERSEDED IN FORM (2026-11-12, WR addendum B §6): the leg is held as `Person.travel_leg` (`loop/matter.py`), not as a Tenure's subject; CP-T10-01 changes the leg's element to a tuple and must update this row." | no |
  | H-159 | "OBSERVED (2026-11-12, WR addendum B §3.2): at the shipped `oblige_term` 4, `tenure.closed` reads 27 in season 5 at seeds 0 and 2 and is absent at seed 1, whose duties were taken a season later; 'NOT MEASURED' is out of date." | no |
  | H-168 | "STALE (2026-11-12, first WR audit E-07, E-08): `migrate` executes 16 of 116 (seed 0, three seasons) and 36 of 217 (six seasons) in computed play." | SE re-reads |
  | H-172 | "CLOSED IN EFFECT (2026-11-12, first WR audit S2): same-season cross-person answers 128, 160, 158 at seed 0, three seasons." | to `measured`, closed |
  | H-209 | "MEASUREMENT NOT REPRODUCIBLE AT ITS SEED (2026-11-12, WR addendum B F-WR-22): seed 0 has no `person.died` in six seasons at HEAD; the mechanism claim is unfalsified. Re-measure at seed 2 (two deaths in six seasons) or under the illness arm, after the duel path executes." | no |
  | H-225 | as H-209, with "its counts are of death claims at two seasons, seeds 0 to 2; at HEAD, two seasons, seeds 0 and 1 hold no death". | no |
  | H-230 | "PREMISE NO LONGER OCCURS AT SEED 0 (2026-11-12, WR addendum B F-WR-22): the King `p_npc_020` does not die in season 1, nor anyone in six seasons; re-measure on a seed or arm in which an office-holder dies." | no |
  | H-107 | only if its row still reads open: "CLOSED (G1b, plan position 4, 2026-09-26): `Event.subject` is deleted; its two senses read through `state/attribution.py::actor_of` and `anchor_of`." | to closed |
  Each sentence is a dated reading of 2026-11-12 at the tree the audit read and says so; this item re-measures none of them (the register's R0 rule: append, never rewrite a measurement). B03.23 later prepends to H-230's `hole:` and `cite:`; this item appends to its `cite:` (serial edge).
- WHERE: `CURRENT.md` (rows *Narrative engine*, *Threadwork*); `engine/season/requirements.yaml` (`scales:` settlement row `note:`); `engine/season/hole_register.yaml` (`cite:` of H-05, H-27, H-159, H-168, H-172, H-209, H-225, H-230, H-107; `grade` or status of H-172 and H-107 as said).
- TESTS: none; covering: `engine/season/tests/test_season_shape.py -k register` for the register's schema `[ASSUMPTION: selector — basis: REST_3 names that file for "the register's schema"]`.
- FALSIFIER and CONTROL: "A `CURRENT.md` row naming a path that does not exist at HEAD; a register sentence citing a number its named run does not show" (each number is quoted as the audit's dated reading, not this tree's). Control: `R(0)` hash equal to B03.16's (nothing here is read by the loop).
- GATE: "`python tools/currency_consistency_check.py`; `python tools/freshness_gate.py`; `python -m engine.season.harness.register --requirements`" → "the two currency tools report no new defect for the two `CURRENT.md` rows (a bare filename that resolves; a code path that exists), and `register --requirements` loads the edited note"; `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `CURRENT.md` rows *Narrative engine* and *Threadwork* (opened at `aa31fd2`, a three-column table); `engine/season/harness/storybar.py`, `chronicle.py`, `strife.py`, `arc.py`; `proposals/2026-11-04-strife-flows/00_MASTER.md`; `requirements.yaml` (the clause, after B03.13's sentence); `hole_register.yaml` rows H-05, H-27, H-107, H-159, H-168, H-172, H-209, H-225, H-230; V12 B03.13 (the same note, earlier).
- GLOSSARY: none.
- COST and TIER: edit (text only); `sonnet` (the source's tier), `medium`.
- LANDS IT: B03's producer; `Item: B03.17`, `[skip ci]`.

*Continued at B03.18 in this part's `_cont` file (the 120 KB cap, `V12_STRUCTURE_part2.md` §4.1), which also holds this half's SERIAL EDGES and file census.*
