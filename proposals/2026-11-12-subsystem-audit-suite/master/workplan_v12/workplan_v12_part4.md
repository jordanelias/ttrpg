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

## Batch B03-hygiene · lane IN · wave W3 · step S3 · HASH MOVER(encoding), one re-pin
INVOCATION: /methodology-execute Batch B03-hygiene
IN-FLIGHT ROW: registers/handoffs/HANDOFF_IN.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
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
  `python -m engine.season.harness.register --check` → exit 0; `--verify-citations` → exit 0; `--requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  the gate lines of every item from B03.51 (the second half adds them in its items);
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (the batch edits engine core, tools and registries: the full gates, CLAUDE.md §0.4); the one full-suite run is at B03.99 (`V12_STRUCTURE_part4.md` E-2);
  the glossary rows B03.18 names, read against the code it landed (`STAGES.md`, "The glossary always matches", rule 2): a mismatch fails the close;
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<B02 closing sha>`) and after, and the batch's measured wall time; no conjunct is named, so no `reading:` record is written and `status:` is not edited (`IS-A-12`).
THE REALM READING `R(s)` (the plan's own instrument for this batch, a one-line read of existing code; nothing is added to the tree): `PYTHONHASHSEED=0 python -c "import sys; from engine.season.harness.populated import build_realm, run; s=int(sys.argv[1]); w=build_realm(s); o=run(1, s, w=w); print(w.content_hash(), o['acts'], len(w.log))" <s>` → three fields: hash, acts, log length (the shape of B02.01's `CENSUS` pin, `dict(acts=…, log=…)`). Per item (E-2): the covering test files and, for a mover, `R(0)`; at B03.99, `R(0)`, `R(1)`, `R(2)`.
RE-PIN: once, at B03.99 (the second half writes the position; `V12_STRUCTURE_part4.md` E-1): the realm pins in `engine/season/tests/_realm_goldens.py` (B02.01's one owner: `BUILD`, `SHIPPED`; `CENSUS` must not move) and the NPC-088 headless hash where it moved, read against B02's close (`reading @<B02 closing sha>`); the commit says "re-pin: encoding only (`Office.body_function` deleted in B03.28); tallies equal". A test that pins one item's own literal keeps it in that item's commit (E-1).
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
