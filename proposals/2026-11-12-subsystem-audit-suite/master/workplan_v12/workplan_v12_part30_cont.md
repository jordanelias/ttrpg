# Workplan v12 — part 30, continued: Batch B25-fi-questioning

## Status: PROPOSED (continuation of `workplan_v12_part30.md`, `V12_STRUCTURE_part2.md` §4.1's `_cont` rule; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

Written against `9700714`, author lane A30. Words, paths and the names after earlier batches are in `workplan_v12_part30.md`'s head. Short names of this file: **S2A** `proposals/14_VERBS_SOCIAL2_A_formation_on_what_is_known.md`; **S2B** `proposals/14_VERBS_SOCIAL2_B_a_word_with_content.md`; **S2C** `proposals/14_VERBS_SOCIAL2_C_case_question_confession.md`; **S2D** `proposals/14_VERBS_SOCIAL2_D_tie.md`; **FI08** `proposals/08_FI_08_knots-season-form.md`; **MC** `proposals/14_VERBS_MATERIAL_C_works.md`; **OBS** `proposals/U5c_SC_one_obstacle_form.md`; **IS-B2** `master/instructions/IS_B2_SC_FI_CORE_CHAR.md`; **CF-E8-3** `master/eval/E8.md` §CF-E8-3 (`:183-218`).

**Two rules from other batches every item here keeps.** (a) B04.04 deleted `rosters.yaml: verb_capability`; a source's "`verb_capability: <verb>: <skill>`" is written as the row's own `capability:` cell, and a contested row with no skill carries `capability: none` with a `capability_note:` (B04.03's loader refusal). (b) B07 (its UNDECIDED (1)) made every writing row a member of exactly one class: `contests:`, a route in `graded_tasks`, or `bookkeeping_verbs`; the roster `contest_owed` lists the rows still owed a `contests:`. A row that gains `contests:` here leaves whichever class roster held it, in the same commit, and `interview` leaves `contest_owed` (the orchestrator's relay of A10's receipt: "Each batch that gives a verb its `contests:` must delete that verb from `contest_owed` in the same commit, with a test").

---

## Batch B25-fi-questioning · lane FI · wave W16 · step S16 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B25-fi-questioning
IN-FLIGHT ROW: registers/handoffs/HANDOFF_FI.md, Open table
GATE: Batch B00-ids @c3418a6a160fc6a17e5a8bf45112a0e55699a695
GATE: Batch B01-laneA @cfd9aefb049c2fe49b55c7ada1b0b624919af23d
GATE: Batch B02-tests
GATE: Batch B11-fi-readers
GATE: Batch B12c-material-verbs-and-valley
GATE: Batch B24-sc-hearing
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading").
  (Earlier in the schedule but not edges of §2.1, read by STOPS IF steps rather than added: B24a (CR-61's `case` Record kind, S15; B25.09) and B21 (A-23's detained-questioner clause in `_req_interrogate`, `U5d_FA_owed_edits` §2, S12; B25.11). B04, B05 and B07 are reached through B11.)
REQUIREMENT: R-04.a (`open_case`) → its `via` column at least 1 on `aperture 2 --seeds 0 1 2` (four seasons in the source's `aperture 4 0`; A-114); `BUILT OUT`: `construe`, `interrogate`, `tie` → each built out; the verb table reads 68 by command (IS-A §12.2 row B25). `status:` is not edited (A-114).
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command):
  `python -m pytest engine/season/tests/test_vm_s2_a_formation.py engine/season/tests/test_vm_s2_b_word.py engine/season/tests/test_vm_s2_c_case.py engine/season/tests/test_vm_s2_d_tie.py engine/season/tests/test_knots_season_form.py engine/tests/test_knots_ed912.py engine/season/tests/test_conclusion.py engine/season/tests/test_task_draw.py engine/season/tests/test_season_shape.py engine/season/tests/test_sc_hearing_evidence.py engine/season/tests/test_fi_evidence_interface.py -q` → all pass;
  `python -m engine.season.harness.aperture 2 --seeds 0 1 2` → the `BUILT OUT` lines for `construe`, `interrogate`, `tie`, `interview`, `utter`, `oblige`, `open_case` (each built out for the first three; `open_case`'s `via` column at least 1) (`IS-A-08`: every verb this batch adds, splits or re-draws);
  `python -c "from engine.season.data.verbs import VERB_TABLE; print(len(VERB_TABLE))"` → 68 (S2D edit 6: "the count is quoted as a reading at the batch that lands it (B25), never typed"; the pin B02 kept, `01_CORE_tests_one_golden_owner` item D, is re-read and re-recorded in B25.99) `[ASSUMPTION: `VERB_TABLE` is the loaded row mapping's name — basis: the pin `len(VERB_TABLE) == 67` quoted in part 3 (B02); the item reads the name at the open]`;
  Reading R1 (the moved B11.74 arm) and Reading R2 (the count) quoted;
  `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `--requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  `python tools/ci_sim_fabrication_check.py` → exit 0 (the new fixtures); the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (engine core and registries: the full gates);
  the glossary rows the items name, read against the code they landed (a mismatch fails the close);
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`, B20's after-reading, B20 merging before B25 in S16, part 2 §3; lane H3) and after, and the batch's measured wall time; B25.99 writes the conjuncts' `reading:` records; `status:` is not edited (`IS-A-12`).
RE-PIN: once, in B25.99: the realm pins in `engine/season/tests/_realm_goldens.py` and every committed digest the batch's movers reach (`engine/season/tests/test_go07_canonical_digest.py` if its vectors encode a `Tenure` of kind `tie` or a `Proposition` with content: read, re-recorded if moved, said plainly), against the step's base, B20's after-reading (`reading @<sha>`; S16's merge order is B11F1, B20, B25, B27, B37, part 2 §3, so "the step's base" in this block means B20's after-reading; lane H3); the commit says "re-pin" and names the movers B25.02, B25.03, B25.04, B25.05, B25.06, B25.09, B25.10, B25.14, B25.15, B25.16, B25.19.
EXPECTED RED UNTIL B25.99 (under `[skip ci]`, E-1; one batch line, repair lane R1): the realm and corpus pins any mover item of this batch moves read red from its first mover (B25.02) to the re-pin; the files that pin them (`git grep -lE '"[0-9a-f]{32}"'` over the test trees and the golden files, those this batch names): `engine/season/tests/_realm_goldens.py` (B02's one pin file); `engine/season/tests/test_go07_canonical_digest.py` (its asserting test, `SHIPPED`/`CENSUS`).
IDS: ED-FI 0; H 0 (rows H-36, H-63, H-94, H-182, H-226, H-313 are edited in place, closed by their items; no row is added)
DIALS AT CONTROL: `dissent_step` = 0 (OBS member 13; S2B §1, S2C §4), `clarity_step` = 0, `deference_step` = 0 (members 24, 25; S2B §2), `establishment_step` = 0 (member 26; S2B §4): each "with its step at control 0 first; equal at control; a declared mover when the step ships" (OBS §4 step 6+); set by B98; target: S2B's gate lines ("`proposition.believed` … a fraction strictly between 0 and 1"; "over seeds 0–9 with the shipped odds, all four bands occur"; `duty.taken` or `duty.probation` at some seed) and S2C §4's ("`news.told` / (`news.told` + `news.untold`) … stays below 1"). `tie_gain` = 0 (S2D edit 4, "control 0; NUMBER row"); set by B98; target: FI08 §3 / S2D gate ("`tied()` is called more than 0 times in a seeded realm and the `tie_gain` 0 and 0.5 arms hash differently"; 0.5 is IN-32's value, FI08 "The problem") — the value to ship is not stated, so B98 reads the gate at 0.5 and writes `BLOCKED (design: no target reading)` if the source gives none beyond that arm. Shipped off control (not dials): `utter_content: on`, `petition_addressee: seat_holders`, `oblige_admission` the draw (control `fiat`) — S2B: "declared hash movers at the shipped arm".
UNDECIDED:
  (U-1) **CP-T06-05 is a POINTER (B25.08) to S2C §3 (B25.14).** The v11 card retypes `interview` with `subject` the topic and `to` the person questioned; S2C §3, which "owns the `interview` row" (its head, C-29) and cites CP-T06-05 as its precedent (ladder step 3), keeps `subject` the person questioned (with S2A edit 5) and derives the topic as the operand `on`. This session's content wins (STAGES step 6). CP-T06-05's falsifier (40 act-id draws; the questioned man forms `tell(X, to=A)` at a share above zero) is carried into B25.14's TESTS. Other reading: build CP-T06-05's cell shape; it contradicts S2A edit 5 and S2C §3.
  (U-2) **S2C §2 is a POINTER (B25.12).** Its head: "§2's `speak` bands yield to `19_LACUNA_admission_rides_the_citing_draw.md` (entry) and `05_SC_evidence_and_rebuttal_B.md` (answer)"; both landed in B24 (B24.19 to B24.25, B24.27: the `proofs` levels, the band dispatch, `speak.writes` `Record.stages` at all four bands, the answering `speak`). Nothing of §2 is left to write.
  (U-3) **S2C §5's stage shape.** S2C §5 appends `(tick, "proof:confession", <event id>, weight, a.id)`; B24's one reader of the case file's stages (B24.21) reads `filed` stages (EVID_B's shape, B24.25). B25.10 files the confession as a `filed` stage of proof kind `confession` at `task_fraction[degree]` (the shape the reader reads), not a second stage shape. Other reading: S2C's literal tuple, which no reader reads.
  (U-4) **The `case` Record kind has two writers** (S2C §1 and CR-61, B24a, S15). B25.09's first step reads `rosters.yaml: record_kinds`: if `case` is there, its fields gain `charge` (and `terms`, `arrangement` where absent) and no second row is written; else S2C §1's row is added.
  (U-5) **`open_case`'s class.** B07 left it on 18-A's default task route ("B25 and B28 move each row to its owner's form"). S2C §1: "Opening is a remit act and is not drawn: whether the case is won is `determine`'s draw." B25.09 moves `open_case` from `graded_tasks` to `bookkeeping_verbs` with that sentence as its `why:` line. Other reading: keep the task route; it draws an act its owner says is not drawn.
  (U-6) **Classes of the rows that gain `contests:`** (`utter`, `oblige`, `construe`, `interview`, `tie`): each leaves the B07 class roster that held it in the commit that adds `contests:`; which roster held each is read at the item's open (SITE) and named in the commit body.
  (U-7) **S2D's hash at landing.** U4c's line says "none at landing if `tie_gain` is landed at its control"; FI08 §3 says the re-land is "declared". A row split that puts `tie` in `resolvable_verbs()` with a working effect opens `Tenure`s in seeded play, which moves the content hash whatever `tie_gain` is. B25.19 is declared MOVER(behaviour); B25.20 (the `tied` term at 0) is EQUAL. Other reading: U4c's (EQUAL), which the first seeded run would falsify.
  (U-8) **`oblige`'s skill.** S2B §4 makes `oblige` contested and names no skill; B04.03's loader refuses a contested row with no `capability:`. B25.04 writes `capability: none` with `capability_note:` "undeclared at authoring; every person rolls the untrained default" (B04.03's form). Other reading: name a skill (`argue`?) — a design choice no source makes.
  (U-9) **IS-B2-SC-07's named test** (`test_a_construal_contradicting_the_terms_loses_at_the_bench`) needs the bench comparator of its step 2 (B27); B25.17 writes the citable half with its own test, and the named test is B27's (§5.8: a gate arm reading a later item's effect moves there).
  (U-10) **H-313 is placed after S2C §5 (B25.11)**, by its own text ("`14_VERBS_SOCIAL2_C_case_question_confession.md` §5 edits `_req_interrogate`"; "same predicate edit"), as its own commit with its own test (CF-E8-3 gives it its own falsifier).
  (U-11) **FI08 §2 lands first (B25.01)**, before U3's position 5: it is hash EQUAL, touches only the unplugged oracle, and depends on nothing in the batch (§5.9: EQUAL first where the source allows).
C(B25-fi-questioning): this batch's entries; the plan's head parts; `unified/U1_GLOSSARY.md` rows *matter*, *construal*, *case file*, *confession*, *interview*, *tie*, *knot*, *sworn*, *utterance*;
  `engine/season/verb_table.yaml` (rows `speak`, `determine`, `open_case`, `interview`, `interrogate`, `utter`, `construe`, `petition`, `oblige`, `tell`, `comply`, `evade / defy`, `accept`, `carry`, `found`, `build`, `research`, `seize`, `tie / knot`); `engine/season/rosters.yaml` (`referent_classes`, `record_kinds`, `question_sources`, `utter_mood_by_source`, `told_on_kinds`, `graded_tasks`, `bookkeeping_verbs`, `contest_owed`, `contest_subsystems`, `task_fraction`, `proofs`, `obstacle_terms`); `engine/season/data/verbs.py` (`RECORD_REFERENT_KINDS`, `HOLDING_RECORD_KINDS`, the loader); `engine/season/data/rosters.py`; `engine/season/data/fixtures.py`;
  `engine/season/queries/world_q.py` (`docket_question`, `questions_for`, `_stamped`, `own_referents_of_class`, `restrained`, `seats_named`, `establishment_of`, `case_file_of`); `engine/season/queries/person_q.py` (`ABOUT_KEYS`, `said_of`, `present_persons`, `holders_named`, `proof_kind`); `engine/season/decision/options.py` (`opening_set`, `operand_bags`, `_derive_operand`, `teller_weight`); `engine/season/loop/effects_information.py` (`_eff_open_case`, `_eff_utter`, `_eff_commit`, `_mint_document`, `_docket_item`); `engine/season/loop/effects_governance.py` (`_eff_oblige`); `engine/season/loop/predicates.py` (`_req_interrogate`, `_req_oblige`); `engine/season/loop/witness.py` (the told deposit); `engine/season/seam/wrappers/sigma.py` (`contest_input`, the obstacle composer's members); `engine/season/state/gate.py` (`purview_reaches`); `engine/season/hole_register.yaml` (H-36, H-63, H-94, H-182, H-226, H-313);
  `systems/fieldwork/sim/knots.py`; `engine/tests/test_knots_ed912.py`; `engine/season/harness/aperture.py` (`verb_counts`); FI-03 §1's `inquiry_world` (B11); `build_hearing` (B24.15);
  the tests named in the items; instruments: `aperture`, `register`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`, `tools/ci_sim_fabrication_check.py`; `engine/season/tests/_realm_goldens.py`;
  the closing SHAs of B00, B01, B02, B11, B12c, B24 (and B24a, B21 for the two STOPS IF reads); the permanent surface.
SERIAL EDGES: within the batch: B25.01 first (EQUAL, independent; U-11). S2A's order ("FI-02 edit 5 (the reader) → edit 5 here → edits 1 and 2"): B25.02 → B25.03; S2A edit 2 last of the three, after S2B and S2C add their kinds (C3-Y10): B25.03 → … → B25.15. S2B's order ("§4 → §3 → §1 → §2 (after S2-A edit 2)"): B25.04 → B25.05 → B25.06; B25.15 → B25.16 (`construe`'s `Record.dispensation`) → B25.17 (the construal is citable). B25.06 → B25.07 (Reading R1 needs typed `utter`). S2C's order ("§1 (after CR-61) → §5 (reads §1's kind) → §2 → §4 → §3 (after FI-02 edit 5 and S2-A edit 5)"): B25.08 (POINTER, placed before S2C's first item, `_part2` §5.6) → B25.09 → B25.10 → B25.11 (the same predicate, U-10) → B25.12 (POINTER) → B25.13 → B25.14; B25.02 → B25.14 (the `interview` row's formation first). U3 §1.2's member order (S2A → S2B → S2C → S2A edit 2 with MC's pair → FI08 → S2D): B25.14 → B25.15 → B25.18 (FI08 §3's conditions read) → B25.19 → B25.20 → B25.21; B25.99 last.
  With other batches, by file (U3 §5.1 rows, v12 landing order): `world_q.py`, `person_q.py`, `verb_table.yaml`, `rosters.yaml`, `fixtures.py`, `effects_information.py`, `options.py`, `sigma.py`, `data/verbs.py` (hot files): B24 → (B20 in S16) → B25 → B26 → B27 → B28; `loop/predicates.py` B04 → B09 → B21 → B25 → B32 (`_req_interrogate`: B21's A-23 clause, if B21 wrote one, lands first, then B25.10 and B25.11); `epistemic.py` B11 → B25 → B27 (FI08 §1 is the Thread lane's, B35; B25 edits no `epistemic.py` line); `loop/witness.py` (the told deposit, a serial instrument file's neighbour `_told_value`, C3-K1) B24 → B25 → B26 → B28; `knots.py` B03 → B25; `engine/season/hole_register.yaml` (permanent surface): rows edited in place, merged in §2.1's order.
PARALLEL: S16 with B11F1-flow-se (SE), B20-mb-orders (MB), B27-sc-proceedings (SC), B37-happenings (IN). Shared files: with B20, `rosters.yaml`, `data/fixtures.py`, `data/verbs.py`, `seam/wrappers/sigma.py` (different keys and functions: B20's `window_responses`, `observation_terms`, `believed_field_samples`, `field_aftermath`, `CHOICE_RANGES`, `believed_chance`); with B27, the case file's stages and `speak`/`determine` rows (B27 edits `determine`'s and the arrangement rows; B25 edits `determine`'s `referent_class` only, B25.03: the coordinator checks the row by key at the step's open, `V12_STRUCTURE_part3.md` §7.3, and serialises the pair if both edit one row); with B37, `verb_table.yaml` and `options.py` by key. Merge order by §2.1: B11F1, B20, B25, B27, B37; B25 rebases on B20's merge, takes its after-reading as baseline, re-pins once in B25.99 (§7.4).
COST: edits and small builds; producer `valoria-author` on `sonnet`, `high`; the contested rows (`utter`, `construe`, `oblige`, `interview`, `tie`) and §2/§3's draws read by `opus` (S2B, S2C tier lines); one `opus` read each of S2A's executions-not-lower table, S2C's ten-seed band tables and the `tie_gain` arms; the close's terminal critique `opus`.
EST: 11 h [estimate: `V12_STRUCTURE.md` §2.4's per-commit formula over this batch's 22 positions (0.4 h × 22 + 2.5 h); §2.2's 6 h counted the members, not the commits]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B25.01 | the oracle fails loudly | FI08 §2 | BUILD | EQUAL | — |
| B25.02 | `interview` forms only on a person who is present | S2A edit 5 | BUILD | MOVER(behaviour) | Batch B11 (B11.08) |
| B25.03 | a docket class: `speak` and `determine` form on a docketed matter | S2A edits 1, 3 | BUILD | MOVER(behaviour) | B25.02 |
| B25.04 | a person knows the seats over his home; swearing to a seat is drawn | S2B §4 | BUILD | MOVER(behaviour) | Batch B11 (B11.08) |
| B25.05 | a petition goes to a seat-holder | S2B §3 | BUILD | MOVER(behaviour) | B25.04 |
| B25.06 | `utter` says what he holds, and whether he is believed is drawn | S2B §1 | BUILD | MOVER(behaviour) | B25.05 |
| B25.07 | the moved B11.74 arm: a Proposition uttered after a winning `reconstruct` | `19_LACUNA_conclusion_is_a_committed_assertion` gate 1 | READING | — | B25.06; Batch B11 (B11.74) |
| B25.08 | the person questioned answers by his own act | CP-T06-05 (intake `:476`) | POINTER | — | B25.14 |
| B25.09 | the case file carries the charge | S2C §1 | BUILD | MOVER(behaviour) | B25.03; Batch B24 (B24.01) |
| B25.10 | a confession on file, by degree | S2C §5 | BUILD | MOVER(behaviour) | B25.09 |
| B25.11 | `interrogate` asks whose custody and whose duchy | H-313 (intake `:284`; CF-E8-3) | BUILD | EQUAL | B25.10 |
| B25.12 | `speak`: evidence sets the odds, the band sets what enters | S2C §2 | POINTER | — | Batch B24 |
| B25.13 | a telling's odds the hearer sets | S2C §4 | BUILD | EQUAL | B25.06 |
| B25.14 | `interview`: a draw to engage, then the questioned answers | S2C §3 | BUILD | MOVER(behaviour) | B25.02, B25.13 |
| B25.15 | a Record sub-kind class; `research` keeps its bare pair | S2A edit 2 with MC's `research` pair | BUILD | MOVER(behaviour) | B25.03 to B25.14; Batch B12c |
| B25.16 | `construe`: a reading of an order, drawn | S2B §2 | BUILD | MOVER(behaviour) | B25.15 |
| B25.17 | a construal is citable beside the terms | `IS-B2-SC-07` step (1) | BUILD | EQUAL | B25.16; Batch B24 |
| B25.18 | the reader first, then the producer | FI08 §3 | POINTER | — | B25.19 |
| B25.19 | `tie`: a chosen bond, drawn for; `knot` handed on | S2D edits 1–3, 6 | BUILD | MOVER(behaviour) | B25.14, B25.13 |
| B25.20 | a tie weighs the teller, behind `tie_gain` at 0 | S2D edit 4 | BUILD | EQUAL | B25.19 |
| B25.21 | the verb table's count | S2D edit 6 | READING | — | B25.19 |
| B25.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | B25.01 to B25.21 |

Not in this batch, and where each is: FI08 §1 and §4 (handed to the Thread lane, B35, A-28); S2D's `knot` half (B35); S2A edit 4 (`tell`'s formation is `08_FI_02` edit 5, landed in B11.08; "No second edit here"); S2C §2 (B24; U-2); IS-B2-SC-07 step (2) and its named test (B27; U-9); `19_LACUNA_questioning_has_an_approach_and_a_cost` (the `approach` source S2C §3 reads at `interview.pressed`: B26.01); `28_CORE_scene_access_A`–`C` (A-63/A-64's occupancy and precedence: B28, B38); `IS-B2-SC-05` (`covenant` opens a negotiation: B28); CR-61's rest (B24a; U-4); the `comply` / `evade / defy` reading of the construer's Proposition (S2B §2's last bullet: "Named for the owning lane", B28).

### B25.01 — the oracle fails loudly · FI08 §2 · BUILD · HASH EQUAL
- SOURCE: FI08 "Edits and decisions" 2 (copied), "Gate" §2, named test; closes R-50 of `audits/08_FI_audit_addendum_B.md` (the 2026-08-08 churn audit's D6 second layer).
- ADVANCES: none of the nine; the oracle that FI's port validates against cannot hide a failed import (CLAUDE.md §7).
- INSTRUCTION (copied): "Delete both `try/except` wrappers in `knots.py`. An oracle whose callee cannot be imported should raise; `engine/tests/test_knots_ed912.py` then observes the lateral calls it asserts on." The two wrappers are the `try:` / `except (ImportError, AttributeError): pass` pairs in `systems/fieldwork/sim/knots.py` (at `9700714`: `try:` at lines 348 and 374, `except` at 365 and 378; cited by symbol at the open, the enclosing functions named in the commit body).
- WHERE: `systems/fieldwork/sim/knots.py`; NEW `engine/season/tests/test_knots_season_form.py`.
- TESTS: `test_knots_season_form.py::test_the_oracle_raises_on_a_failed_lateral_import`, written first, red ("with the conviction module's name misspelt on purpose the same test errors where today it passes", monkeypatched in the test); `engine/tests/test_knots_ed912.py` green.
- FALSIFIER and CONTROL: a misspelt lateral module that the oracle swallows. Control: `engine/tests/test_knots_ed912.py` green before and after; realm hashes unchanged (the oracle is unplugged from the season).
- GATE: `python -m pytest engine/season/tests/test_knots_season_form.py engine/tests/test_knots_ed912.py -q` → pass.
- HASH MOVERS: none ("§2 none").
- DEPENDS ON: EXISTS-IN-TREE `systems/fieldwork/sim/knots.py` (the two wrappers), `engine/tests/test_knots_ed912.py`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B25's `valoria-author` producer, `isolation: worktree`; `Item: B25.01`, `[skip ci]`.

### B25.02 — `interview` forms only on a person who is present · S2A edit 5 · BUILD · HASH MOVER(behaviour)
- SOURCE: S2A "Exact edits, by owner" 5 (copied), "Order of landing", "Gate", "Falsifier"; rulings A-63 (an `interview` is a visit), A-64; closes the `interview` half of `audits/14_VERBS_SOCIAL2.md` §7 (14 of 19 refused on a non-person; one self-interview).
- ADVANCES: R-03 (fewer scenes spent on acts the fold refuses for a reason the actor could read); FI standalone.
- INSTRUCTION (copied): "`verb_table.yaml` `interview`: `referent_class: Person`; `counterparty: subject` (the existing person-side self decline, `opening_set`); `requires_typed: {all: [{form: existence, of: subject, kind: Person}, {form: relation, of: subject, relation: with, conjunct: present}]}`; `emits_on_refusal: {present: [interview.refused], …}` (S2-C renames the kinds; until then `finding.none`)." "`decision/options.py::opening_set`: a row whose typed cell carries a `relation: with` conjunct on `subject` forms only on subjects in `person_q.present_persons(p.ledger, p.id)` under the `telling_hearers: seen_since_move` arm (FI-02's reader and fixture; at `known`, today's behaviour). Read off the row's cell, never the verb name." Standing (S2A): "An `interview` is a visit: it occupies its interviewee for the round [lap] (A-63)" — the occupancy itself is `28_CORE_scene_access_A`'s (B28); "round" corrected to "lap" (A-101).
- WHERE: `engine/season/verb_table.yaml` (`interview`); `engine/season/decision/options.py` (`opening_set`); NEW `engine/season/tests/test_vm_s2_a_formation.py`.
- TESTS: in the new file, written first: `test_interview_forms_only_on_a_present_person` `[ASSUMPTION: test name; the item creates it]` (hand-built: a seat-holder knowing a present person, an absent person, a rung and a Record: `interview` forms on the first only; no self-subject); and the gate's reading function `test_s2a_refusals_and_executions` (S2A Gate, written now and extended by B25.03 and B25.15: "per verb: attempted, executed, refused by deciding read … over `harness/aperture.py`'s per-verb counts (`verb_counts`)"; this item's arm: "`interview` on `exists:Person=0`, and self-subject 0", and "executions of … `interview` … not lower than the baseline" — the baseline re-read on the batch's base and quoted (C3-N27: the source's `4/5/5` was read before B01)).
- FALSIFIER and CONTROL: an `interview` formed on a rung, a Record, a Proposition or an absent person. Control: `telling_hearers: known` reproduces the pre-item formations (`reading @<sha>`, the step's base).
- GATE: `python -m pytest engine/season/tests/test_vm_s2_a_formation.py -q` → pass; executions of `interview` at seeds 0–2, one season, not lower than the base reading ("A fall is the stopping rule (CP-T05-04's AM-A-09 rule): revert that edit").
- HASH MOVERS: "A declared hash mover in every world (the refusal Events and their WITNESS deposits stop)." B25.99.
- DEPENDS ON: V12 B11.08 (`08_FI_02` edit 5: `person_q.present_persons`, the `telling_hearers` fixture; not in the tree at `9700714`); EXISTS-IN-TREE `decision/options.py::opening_set`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `medium` (S2A's tier line).
- LANDS IT: B25's producer; `Item: B25.02`, `[skip ci]`.

### B25.03 — a docket class: `speak` and `determine` form on a docketed matter · S2A edits 1, 3 · BUILD · HASH MOVER(behaviour)
- SOURCE: S2A "Exact edits, by owner" 1 and 3 (copied), "Gate", "Falsifier"; ladder step 4 (REM-24, CP-T05-04's `Person` class); closes the `speak`/`open_case` halves of `audits/14_VERBS_SOCIAL2.md` §3, §5 (`speak` 7 of 8 refused `exists:DocketItem=0`; `open_case` 3 of 11 on the `write` clause).
- ADVANCES: R-03; R-04.a (`open_case`, `determine` form where they can execute).
- INSTRUCTION (copied):
  1. "`engine/season/rosters.yaml: referent_classes` gains `Matter`: *a matter on the docket the person saw docketed or was asked to sit on; stamped by `docket_question` and the sitting question; the referent's id is the party (a person), so `determine`'s `party` conjunct reads it unchanged.*" (appended at the end of the roster's values.)
  2. "`engine/season/queries/world_q.py::docket_question` and the sitting-question loop in `questions_for`: carry the matters as `classes` `(m, "Matter")` **instead of** plain `referents` (the Question keeps `about`; `referents` is `()` for these two questions). The docstring's limits (2) and (3) are deleted as resolved; the REVERT line becomes: *restore plain referents and delete the two `referent_class: Matter` columns*."
  3. "`engine/season/verb_table.yaml` `speak` and `determine`: `referent_class: Matter`, with a note citing this proposal and the measurement. `speak`'s `subject_may_be_self` is unchanged (the accused's own docket question carries himself as `Matter`)."
  4. Edit 3, `open_case`: "No row edit: edit 1 removes its docketed formations" ("`own_referents_of_class` stamps a question's plain referents only … its body is `_of_stamped_class(w, q.referents, classes)`"; re-read at the open and the line quoted in the commit body).
  5. Glossary: row *matter* (add or edit): "a matter: a case on the docket, as a matter before a court is"; owner `rosters.yaml: referent_classes` `Matter`.
- WHERE: `engine/season/rosters.yaml` (`referent_classes`); `engine/season/queries/world_q.py` (`docket_question`, `questions_for`'s sitting loop); `engine/season/verb_table.yaml` (`speak`, `determine`); `engine/season/tests/test_vm_s2_a_formation.py`; `unified/U1_GLOSSARY.md` (*matter*).
- TESTS: `test_vm_s2_a_formation.py::test_speak_and_open_case_partition_the_docket` (S2A Falsifier: "A hand-built world with one docketed party P and one undocketed person Q, both known to a seat-holder: `speak` forms on P and not on Q; `open_case` forms on Q and not on P"), written first, red; `test_s2a_refusals_and_executions` gains: "refusals 0 for: `speak` on `exists:DocketItem=0`; `open_case` on clause `write`", executions of `speak`, `open_case` not lower than the base reading.
- FALSIFIER and CONTROL: "If any of these forms on the other, the partition is not carrying the class." Control: the base reading of `speak`, `open_case` executions (`reading @<sha>`).
- GATE: `python -m pytest engine/season/tests/test_vm_s2_a_formation.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 s`, s = 0, 1, 2 → the two refusal counts 0, executions not lower ("A fall is the stopping rule … revert that edit").
- HASH MOVERS: declared, every world (refusal Events stop). B25.99.
- DEPENDS ON: EXISTS-IN-TREE `world_q.docket_question`, `::questions_for`, `::own_referents_of_class`, `state/carriers.py::Question` (`classes`, IN-53 D1); V12 B25.02.
- GLOSSARY: *matter* (step 5).
- COST and TIER: edit; `sonnet`, `medium`.
- LANDS IT: B25's producer; `Item: B25.03`, `[skip ci]`.

### B25.04 — a person knows the seats over his home; swearing to a seat is drawn · S2B §4 · BUILD · HASH MOVER(behaviour)
- SOURCE: S2B §4 (copied, as W3-4a rewrote it onto C-20), "Gate" §4, "Falsifiers" §4; OBS §2 members 6, 7, 26; decision register D-31 (taken A under A-24); VRES §6's reconciliations, as B11.08's part names them ("the private table `oblige_obstacle` is the roster member `establishment`" and "the control fixture `oblige_admission: fiat` stays the hash-equal arm", both landing here); rulings A-24, A-81; closes the `oblige` half of `audits/14_VERBS_SOCIAL2.md` §9 (`seats_named` empty at three seeds).
- ADVANCES: R-04.c2's ground (persons enter service by their own act); R-06 (a seat may refuse a man).
- INSTRUCTION (copied):
  1. "The news of who holds the seats over a person's home is seeded at build by `seed_seat_news` (`08_FI_01_claim-sourced-referents.md` edit 6 …) and kept current by the existing `tenure.opened` / `tenure.closed` deposits; it is read by `person_q.holders_named` (edit 1). This file adds neither; its §3 and `oblige` read them."
  2. "`oblige`: `seats_named` now returns the home's seats; `_req_oblige`'s five clauses stay as eligibility. **Admission becomes a draw** …: `verb_table.yaml` `oblige` gains `contests: "a standing"` with the seat's live holder as opponent where the joiner's ledger names one (`holders_named`), else the composer's stand-in for a vacant or unknown holder (`counterparty: subject` resolves to the seat); obstacle through the one composer: `rank_gap` (OBS member 6), the holder's `regard` of the joiner (member 7), `establishment` (member 26, `establishment_step` per 5 sworn men)." "`writes:` `Tenure.since`, `Tenure.term` at Ov / Su / Pa, `[]` at Fa; `emits:` `duty.taken` at Ov / Su, `duty.probation` at Pa, `duty.refused` at Fa. `_eff_oblige` opens the edge with `degree=res.degree` and, at Pa, half `oblige_term` (the term's one owner, `H-159`, read and halved, no second constant)." "`oblige_admission: fiat` stays the control arm."
  3. `establishment` joins `rosters.yaml: obstacle_terms` "with its step at control 0 first" (OBS §4 step 6+): `establishment_step = 0` in `data/fixtures.py`, its tag naming this item; its host function reads `world_q.establishment_of` (OBS §2 row 26).
  4. The row's class (U-6): `oblige` leaves the B07 class roster that held it (`graded_tasks` or `bookkeeping_verbs`, read at the open) in this commit. Its `capability:` cell is `none` with `capability_note:` "undeclared at authoring; every person rolls the untrained default" (U-8).
  5. A-81: "`duty.refused` [is a] witnessed deed deposited to those present (the issuer, the seat's holder)". Draw key (A-30): `H(w.world_seed, w.tick, <actor id>, "oblige.standing")`.
- WHERE: `engine/season/verb_table.yaml` (`oblige`); `engine/season/loop/effects_governance.py` (`_eff_oblige`); `engine/season/queries/world_q.py` (`seats_named`); `engine/season/rosters.yaml` (`obstacle_terms`: `establishment`; the B07 class roster); `engine/season/data/fixtures.py` (`establishment_step`, `oblige_admission`); `engine/season/seam/wrappers/sigma.py` (the `establishment` member's host function); NEW `engine/season/tests/test_vm_s2_b_word.py`.
- TESTS: in the new file (S2B's test file, "one function per gate line"), written first, red: `test_oblige_forms_and_admission_is_drawn` (gate §4: "`oblige` formed > 0 at every seed, attempted ≥ 1; across seeds at least one `duty.taken` or `duty.probation` and the sworn man in `establishment_of`; a planted `Failure` opens no edge"; `build_realm(s)`, s = 0–2, two seasons); `test_no_seat_reaches_his_home_no_oblige` (falsifier §4: "a person whose home no seat reaches is offered no `oblige` (`seats_named` empty)"); `test_oblige_admission_fiat_hashes_as_the_control` (the control arm). `[ASSUMPTION: test names; the item creates them — basis: S2B names no function, "one function per gate line"; E-3]`
- FALSIFIER and CONTROL: as the falsifier test. Control: `oblige_admission: fiat` reproduces the step's base hashes at seeds 0–2.
- GATE: `python -m pytest engine/season/tests/test_vm_s2_b_word.py -k oblige -q` → pass; `python -m pytest engine/season/tests/test_task_draw.py -q` → pass (the class refusals of B07 accept the moved row); `python tools/ci_sim_fabrication_check.py` → exit 0.
- HASH MOVERS: "declared hash movers at the shipped arm in every world." B25.99.
- DEPENDS ON: V12 B11.08 (`08_FI_01` edits 1 and 6: `person_q.holders_named`, `seed_seat_news`; neither in the tree at `9700714`); V12 Batch B05 (the composer, OBS §2); V12 B21 (`rank_gap`, with `14_VERBS_BINDING_A`; reached by schedule: S12); EXISTS-IN-TREE `loop/effects_governance.py::_eff_oblige`, `loop/predicates.py::_req_oblige`, `world_q.seats_named`, `world_q.establishment_of`.
- GLOSSARY: row *sworn* (U4d's): its owner gains `oblige`'s draw ("a sworn man: one a seat has admitted to its service by his own oath, as a man is sworn in").
- COST and TIER: small build; `sonnet`, `high`; the contested row read by `opus` (S2B tier).
- LANDS IT: B25's producer; `Item: B25.04`, `[skip ci]`.

### B25.05 — a petition goes to a seat-holder · S2B §3 · BUILD · HASH MOVER(behaviour)
- SOURCE: S2B §3 (copied, rewritten by W3-4a onto C-20), "Gate" §3, "Falsifiers" §3; closes the `petition` half of §2 of the audit (`to == subject` 12/12, 14/14, 13/13) and H-94's binding of `to`.
- ADVANCES: R-06 (people petition their lords with no player present).
- INSTRUCTION (copied): "`decision/options.py::operand_bags`: `petition`'s `to` fans over the holders `person_q.holders_named` (`08_FI_01` edit 1, the one reader of "who holds a seat, as I believe it") gives for the seats over the petitioner's home, minus `p.id` and the subject; read off the row's existing counterparty operand and the reader the row's note names, never the verb. Else the existing `known_persons` fan." "`verb_table.yaml` `petition`: `requires_typed_note` gains *`to` is fanned over the seat-holders the petitioner believes rule his home (`person_q.holders_named`); `H-94`'s single referent now binds `subject` alone*." "`rosters.yaml: petition_addressees` is **not** added." "Fixture `petition_addressee: seat_holders | referent` (control `referent`: today)." `engine/season/hole_register.yaml` H-94: its text records that `to` and `subject` no longer bind one referent (the row's other fields kept).
- WHERE: `engine/season/decision/options.py` (`operand_bags`); `engine/season/verb_table.yaml` (`petition`'s note); `engine/season/data/fixtures.py` (`petition_addressee`); `engine/season/hole_register.yaml` (H-94); `engine/season/tests/test_vm_s2_b_word.py`.
- TESTS: `test_petition_goes_to_a_seat_holder` (gate §3: "`to == subject` 0; every `to` holds a seat reaching the petition's `from`", seeds 0–2, two seasons); `test_no_seat_news_no_petition` (falsifier §3: "a petitioner with his seat news deleted (no `holders_named` entry) forms no petition"). Written first, red. `[ASSUMPTION: test names; the item creates them — basis: S2B names no function; E-3]`
- FALSIFIER and CONTROL: as the tests. Control: `petition_addressee: referent` reproduces B25.04's hashes.
- GATE: `python -m pytest engine/season/tests/test_vm_s2_b_word.py -k petition -q` → pass; `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`).
- HASH MOVERS: declared at the shipped arm (`seat_holders`). B25.99.
- DEPENDS ON: V12 B25.04; V12 B11.08 (`holders_named`); EXISTS-IN-TREE `decision/options.py::operand_bags`, `person_q.known_persons`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B25's producer; `Item: B25.05`, `[skip ci]`.

### B25.06 — `utter` says what he holds, and whether he is believed is drawn · S2B §1 · BUILD · HASH MOVER(behaviour)
- SOURCE: S2B §1 (copied: the row, the rosters, the operand, the effect, the WITNESS trigger, the fixture), "Gate" §1 and "§1, the draw", "Falsifiers" §1; OBS member 13 (`dissent`); R4 §1.6 (`04` PART D 27: no verb literal in a WITNESS body); rulings A-30, A-81; closes `audits/14_VERBS_SOCIAL2.md` §1 (moods `{OUGHT}`, predicates `{''}`, values `{None}`).
- ADVANCES: R-07 (a statement others can carry and compare); the readers that "can therefore never fire on a computed word" (`world_q`'s judge vote, `aim_state`, `_req_interrogate`'s `HOLDS` charge).
- INSTRUCTION (copied):
  1. The row (S2B §1, byte for byte):
     ```yaml
     - verb:        "utter"
       stratum:     social
       eligibility: [own]
       beneficiary: none
       requires:    "the speaker holds a claim on what he speaks of"
       requires_typed: {form: own_ledger, of: subject, conjunct: holds}
       contests:    "a standing"          # against the room: whether he is believed (standing rule)
       writes:
         Overwhelming: ["Proposition.exists"]
         Success:      ["Proposition.exists"]
         Partial:      ["Proposition.exists"]
         Failure:      ["Proposition.exists"]
       emits:
         Overwhelming: ["proposition.uttered", "proposition.believed"]
         Success:      ["proposition.uttered", "proposition.believed"]
         Partial:      ["proposition.uttered"]
         Failure:      ["proposition.uttered"]
       emits_on_refusal: {holds: ["utterance.empty"]}
       grade:       assumption
     ```
     "(notes carried forward; `writes_note` gains: *the cell is the `said` the named `holds` conjunct carries; the mood is `rosters.yaml: utter_mood_by_source`'s for the question's source; that he said it is not in doubt, so every band mints; whether the room believes it is the draw, and only `proposition.believed` triggers the told deposit*)." The row's skill: "`verb_capability: utter → copying` (new row; the row's own `capability:` cell at CAP A2/A3, D-U1-07)" → `capability: copying` on the row (B04.04). The row leaves its B07 class roster (U-6).
  2. "`rosters.yaml: contest_subsystems.prizes`: `a standing` already routes to the `social_contest` provider (`tell`'s); the opponent is the room — the one composer's stand-in (`opposed_ob(pool_default)`, OBS §2 …) plus `dissent` (OBS member 13, `dissent_step`: one step per hearer present whom the speaker's own ledger holds as believing the contrary; `sigma.py::contest_input`, the speaker's own-ledger read, F8)." `dissent` joins `obstacle_terms` with `dissent_step = 0` (control first, OBS §4 step 6+).
  3. "`engine/season/rosters.yaml`: new closed table `utter_mood_by_source` (keys: `question_sources` members, validated at load): `claim_landed: HOLDS`, `need: OUGHT`. A source with no row forms no `utter`."
  4. "`engine/season/decision/options.py::_derive_operand`: operand `mood` → the table's value for `q.source`. (No branch on the verb: any row naming a `mood` operand gets it.)"
  5. "`engine/season/loop/effects_information.py::_eff_utter`: content from `payload["said"]` (`Said`: subject, predicate, value) and `payload["mood"]`; the existing defaults kept only for a hand-built act with neither (fixture `utter_content: off` is the control: ignore both, today's behaviour). Typed in: `Act` with `said: Said | None`, `mood: str | None`. Out: `Change` naming the Proposition." The mint goes through `_mint_proposition(w, actor, prop)` (created here, shared with B25.16: S2B §2 step 3 names it "the same two lines `_eff_utter` performs"). B11.74's `Proposition.support` from `cites` is kept.
  6. "`engine/season/loop/witness.py`, the told deposit: fires for an Event whose kinds include a member of a new closed roster `rosters.yaml: told_on_kinds` (`values: [proposition.believed]`, checked against `EVENT_KINDS` at load), depositing the told copy on those present with the utterer on its chain (FI-05B E-3's channel); at Pa / Fa the ordinary deposit of `proposition.uttered` about the speaker is all that lands." SITE (`[UNVERIFIED: whether today's trigger keys on the payload's `said`; if so the roster test is added beside it]`, S2B): open the told deposit's trigger (B24.24 widened it to "`said` or `cites`") and add the roster arm beside it; record which in the commit body.
  7. "Fixture `utter_content: on | off` in `engine/season/data/fixtures.py`" (shipped `on`; its tag names this item). Draw key (A-30): `"utter.standing"`.
  8. Glossary: row *utterance* (add or edit): "an utterance: a statement a person makes of what he holds, whether or not the room believes it"; owner `verb_table.yaml: utter`.
- WHERE: `engine/season/verb_table.yaml` (`utter`); `engine/season/rosters.yaml` (`utter_mood_by_source`, `told_on_kinds`, `obstacle_terms`: `dissent`; the B07 class roster); `engine/season/data/rosters.py` (the two tables' loaders and refusals); `engine/season/decision/options.py` (`_derive_operand`); `engine/season/loop/effects_information.py` (`_eff_utter`, `_mint_proposition`); `engine/season/loop/witness.py` (the told deposit's trigger); `engine/season/seam/wrappers/sigma.py` (`dissent`'s host function); `engine/season/data/fixtures.py` (`utter_content`, `dissent_step`); `engine/season/tests/test_vm_s2_b_word.py`; `unified/U1_GLOSSARY.md` (*utterance*).
- TESTS (written first, red): `test_utter_carries_what_he_holds` (gate §1: "≥ 90% of computed Propositions carry a non-empty predicate; every `HOLDS` cell equals a claim its utterer held at the act tick; ≥ 1 judge vote … or ≥ 1 `decision.agreement` disagreement between two utterances read at one seed"; seeds 0–2, two seasons); `test_belief_is_drawn` (gate "§1, the draw": "`proposition.believed` is emitted for some utterances and not for others (a fraction strictly between 0 and 1); a planted `Failure` mints the Proposition and deposits no told copy"); `test_an_evicted_said_refuses_utterance_empty` (falsifier §1); `test_a_source_with_no_mood_row_forms_no_utter` and `test_told_on_kinds_refuses_an_unknown_event_kind` `[ASSUMPTION: test names, all five of this item; the item creates them — basis: S2B names no function; E-3]`.
- FALSIFIER and CONTROL: "an act whose `said` claim was evicted between formation and fold refuses `utterance.empty`, never mints the cell." Control: `utter_content: off` reproduces B25.05's hashes at seeds 0–2.
- GATE: `python -m pytest engine/season/tests/test_vm_s2_b_word.py engine/season/tests/test_conclusion.py engine/season/tests/test_fi_evidence_interface.py -q` → pass; `python tools/ci_sim_fabrication_check.py` → exit 0.
- HASH MOVERS: declared "at the shipped arm in every world" (every computed `utter`). B25.99.
- DEPENDS ON: V12 B25.05; V12 B11.74 (`Proposition.support`); V12 B24.24 (the told deposit's trigger); V12 Batch B05 (`opposed_ob`, the composer); EXISTS-IN-TREE `loop/effects_information.py::_eff_utter`, `decision/options.py::_derive_operand`, `state/carriers.py::Said`, `Proposition`.
- GLOSSARY: *utterance* (step 8).
- COST and TIER: small build; `sonnet`, `high`; the contested row `opus`; one `opus` read of the gate's band fractions.
- LANDS IT: B25's producer; `Item: B25.06`, `[skip ci]`.

### B25.07 — the moved B11.74 arm · READING
- In the position table only; its text is Reading R1 below.

### B25.08 — the person questioned answers by his own act · CP-T06-05 · POINTER
- SOURCE: the intake `:476` (CP-T06-05, STILL-NEEDED; target "FI · B25-fi-questioning (+B26 questioning file)"); carry-forward `master/eval/E1.md` `:700-719` (the card and the entry); placed by `_part2` §5.6's first rule (before the first item whose source names its id: S2C, ladder step 3, "CP-T06-05 for the interview"); U-1.
- What it points at: S2C §3 (B25.14) builds the behaviour CP-T06-05 names — "His answer is his own `tell(topic, to=asker)` at a later deliberation … or no answer" — in this session's shape (`subject` the person questioned, `on` the topic as a derived operand), with S2A edit 5 (B25.02). CP-T06-05's own falsifier is carried as a test of B25.14 ("Hand-built: A and B at R, B holding a claim on X; A interviews B about X in lap 1, so B holds the question. Across 40 act-id draws of B's later deliberations that season, B forms `tell(X, to=A)` at a share above zero"; "round 1" → "lap 1", A-101). B26.01 (`19_LACUNA_questioning_has_an_approach_and_a_cost`) depends on this POINTER's target, B25.14.
- Target files and symbols: `verb_table.yaml: interview`; `world_q.questions_for` (source `asked`); `decision/options.py::operand_bags`.
- GATE: B25.14's. The intake entry CP-T06-05 is closed by B25.14's commit (its body names it).

### B25.09 — the case file carries the charge · S2C §1 · BUILD · HASH MOVER(behaviour)
- SOURCE: S2C §1 (copied), "Order of landing" ("§1 (after CR-61)"), "Gate" §1; `IS-B2-SC-02` (B24.01: the docket item names its case file, CR-61's one fact these files read); `unified/U4_DOCUMENT_STATUS.md` §3.4 (S2C INCOMPLETE, DEP-v11 on CR-61, narrowed by B24.01); U-4, U-5; closes the `open_case` half of `audits/14_VERBS_SOCIAL2.md` §3 ("the case file is kind `text` with no content").
- ADVANCES: R-04.a (`open_case` forms and executes with its seat); SC standalone (the case file as the board).
- INSTRUCTION:
  1. SITE (U-4): open `rosters.yaml: record_kinds`. If `case` is a member (B24a's CR-61), its fields gain `charge` (and `terms`, `arrangement` where absent) and no row is added; otherwise, copied: "`rosters.yaml: record_kinds`: new kind `case: [terms, charge, arrangement]`". Record which in the commit body.
  2. Copied: "`person_q.ABOUT_KEYS` gains `case: terms` (the one owner of "what a document is about", so `_req_interrogate` clause 3 and `ledger_names` read a case file with no new code path)." (`ABOUT_KEYS` is derived from `_requires.RECORD_SOURCED_OPERANDS` at `9700714`: the entry is added at that owner, and the derived mapping read back in the test.)
  3. Copied: "`verb_table.yaml` `open_case`: `requires_typed` gains `{form: own_ledger, of: subject, conjunct: charge}` (named, so the Candidate carries `said`: the opener's own claim about the party, by `person_q.said_of` with FI-06's pool, which prefers his attributed deeds). Refusal key `charge: [case.refused]`."
  4. Copied: "`_eff_open_case`: mint kind `case` with content `{terms: matter, charge: <said as a dict>, arrangement: <payload or None>}` instead of `text` with none; the docket item names the case file (CR-61's key) [B24.01's `DOCKET_CASE`, read through `world_q.case_file_of`]. Opening is a remit act and is not drawn: whether the case is won is `determine`'s draw."
  5. U-5 (B07's relay): `open_case` leaves `rosters.yaml: graded_tasks` (18-A's default route) and joins `bookkeeping_verbs` with `why:` "a remit act; whether the case is won is `determine`'s draw (S2C §1)". The B07 loader's bookkeeping refusals do not touch it (it writes a Record and a `DocketItem`, neither in the refused list).
- WHERE: `engine/season/rosters.yaml` (`record_kinds`, `graded_tasks`, `bookkeeping_verbs`); `engine/season/data/requires.py` (`RECORD_SOURCED_OPERANDS`, `case`) `[ASSUMPTION: `_requires` is `data/requires.py` — basis: `person_q.py:1383` imports it as `_requires`; the item confirms at the open]`; `engine/season/verb_table.yaml` (`open_case`); `engine/season/loop/effects_information.py` (`_eff_open_case`); NEW `engine/season/tests/test_vm_s2_c_case.py`.
- TESTS: in the new file (S2C's, "one function per gate line"), written first, red: `test_every_case_file_carries_its_openers_charge` (gate §1: "every case file has `charge` equal to a claim its opener held at the act", on FI-03 §1's `inquiry_world` and `build_hearing`, seeds 0–9); `test_open_case_is_bookkeeping_not_a_task` `[ASSUMPTION: test name; the item creates it]` (the loader reads `open_case` in `bookkeeping_verbs` and in no other class).
- FALSIFIER and CONTROL: "If any step reads a ledger other than the actor's own, the case file is not carrying the `Said`" (S2C). Control: `aperture 1 0`'s `open_case` executed count not lower than B25.03's reading.
- GATE: `python -m pytest engine/season/tests/test_vm_s2_c_case.py engine/season/tests/test_task_draw.py engine/season/tests/test_docket_names_its_case_file.py -q` → pass; `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`).
- HASH MOVERS: declared, every world in which `open_case` executes (the Record's kind and content change; the task route's draw leaves). B25.99.
- DEPENDS ON: V12 B24.01 (`DOCKET_CASE`, `case_file_of`); V12 B25.03 (the `Matter` partition); V12 Batch B07 (`graded_tasks`, `bookkeeping_verbs`); V12 Batch B11 (`08_FI_06`, `said_of`'s widened pool); B24a's CR-61 (read by step 1, not a gate); EXISTS-IN-TREE `loop/effects_information.py::_eff_open_case`, `::_mint_document`, `person_q.ABOUT_KEYS`, `person_q.said_of`.
- GLOSSARY: row *case file* (add or edit): "the case file: the paper that holds a case's charge, what was filed and how each sitting went, as a court's case file does"; owner `rosters.yaml: record_kinds` `case`.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B25's producer; `Item: B25.09`, `[skip ci]`.

### B25.10 — a confession on file, by degree · S2C §5 · BUILD · HASH MOVER(behaviour)
- SOURCE: S2C §5 (copied), "Gate" §5; OBS §3 (`proofs`, `custody` sources; C3-C10: nothing lowers the obstacle); rulings A-25, A-81 ("`interrogate`'s Failure is witnessed by the prisoner and the interrogator"); U-3; closes H-226 by route (b) for this row, H-310's carrier (`master/eval/E8.md`: SUPERSEDED by this §).
- ADVANCES: `BUILT OUT` `interrogate`; R-04.c3 (a confession is an exhibit).
- INSTRUCTION (copied, with U-3's stage shape):
  1. "`verb_table.yaml` `interrogate`: `writes:` Ov / Su / Pa `[Record.stages]`, Fa `[]`; emits unchanged."
  2. "`loop/predicates.py::_req_interrogate` clause 3: the charge may be the docket item's petition **or its case file**, both through `ABOUT_KEYS` (one owner); no other change."
  3. "New `_eff_interrogate(w, a, res)`: appends … to the matter's case file, weight `task_fraction[degree]` (Ov / Su 1.0, Pa 0.5). Closes `H-226` by route (b) for this row: the fold runs the effect because the band now writes." The stage is written in B24's filed shape (B24.25: `(tick, "filed", side, rung, <event id>, weight, origin, act id)`, its proof kind `confession` read by `person_q.proof_kind`, B24.22–B24.23), not S2C's `(tick, "proof:confession", …)` (U-3). The case file is `world_q.case_file_of`.
  4. "Odds, as levels for the interrogator (A-25; C3-C10): the standing weight of items already on the case file against the prisoner is the `proofs` source; custody is the `custody` source (OBS §3: one `custody_level` per season held, soft-capped) — custody wears a man down, and still he may withhold." (Both sources are B05's; this item confirms the row reaches them and adds none.) "`rosters.yaml: verb_capability`: `interrogate: "inquiry"`" is already the row's `capability:` cell (B04.03's list).
  5. `engine/season/hole_register.yaml` H-226: closed for `interrogate` (its `cite:` names this item and the test).
- WHERE: `engine/season/verb_table.yaml` (`interrogate`); `engine/season/loop/predicates.py` (`_req_interrogate` clause 3); `engine/season/loop/effects_information.py` (new `_eff_interrogate`, `@effect_for("interrogate")`); `engine/season/hole_register.yaml` (H-226); `engine/season/tests/test_vm_s2_c_case.py`.
- TESTS: `test_a_confession_is_filed_by_degree` (gate §5: "with one planted `detain` and a case file, `interrogate` executes; at planted `Success` one … stage at weight 1.0, at planted `Partial` at 0.5, at planted `Failure` none"), written first, red; `test_fi_evidence_interface.py::test_a_withheld_confession_is_no_proof_and_a_full_one_is` (B24.23) stays green. `[ASSUMPTION: test name `test_a_confession_is_filed_by_degree`; the item creates it — basis: S2C names no function; E-3]`
- FALSIFIER and CONTROL: "If any band outcome above occurs at every seed of ten under the shipped odds (or never), the odds are degenerate" (S2C). Control: an `interrogate` with no case file (petition only) still folds as before (clause 3's petition arm).
- GATE: `python -m pytest engine/season/tests/test_vm_s2_c_case.py engine/season/tests/test_fi_evidence_interface.py -q` → pass; `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`).
- HASH MOVERS: declared, wherever `interrogate` folds at a winning band. B25.99.
- DEPENDS ON: V12 B25.09 ("§5 (reads §1's kind)"); V12 B24.22, B24.23, B24.25 (`proof_kind`, the filed shape); V12 Batch B05 (`custody`, `proofs` sources; `task_fraction`, B07); EXISTS-IN-TREE `loop/predicates.py::_req_interrogate`, `world_q.restrained`.
- GLOSSARY: row *confession* (add if absent): "a confession: what a prisoner admits under questioning, filed on the case at the weight the questioning earned".
- COST and TIER: small build; `sonnet`, `high`; the draw read by `opus` (S2C tier).
- LANDS IT: B25's producer; `Item: B25.10`, `[skip ci]`.

### B25.11 — `interrogate` asks whose custody and whose duchy · H-313 · BUILD · HASH EQUAL
- SOURCE: the intake `:284` (H-313, STILL-NEEDED; target "FA/FI lane, B25 (same predicate edit); CF-E8-3"); CF-E8-3 (`master/eval/E8.md:183-218`: the register row verbatim, INSTRUCTION, FALSIFIER, GATE); placed by `_part2` §5.6's second rule (its own text names S2C §5's predicate edit; U-10); A-23 (the detained-questioner case, `U5d_FA_owed_edits` §2, B21); closes H-313.
- ADVANCES: R-06 (a seat's reach bounds who it may question); none of the nine by count (hand-built acts only).
- INSTRUCTION (CF-E8-3, copied): "(H-313) in `_req_interrogate` require that the custody edge is the questioner's own seat's (`world_q.restrained` by a seat of the questioner's purview) and the subject within the questioner's purview; the detained-questioner case is A-23's (`U5d_FA_owed_edits.md` §2, B21) and is not repeated." The purview read is `state/gate.py::purview_reaches` (the owner the establish path asks through `founds_over`), routed through `_refuse(…)` with a named clause (B09's `01_CORE_predicates_name_their_clause`). The `[ASSUMPTION]` in `_req_interrogate`'s text that reads custody as "any seat" is deleted. SITE: open `_req_interrogate` and record whether B21 added the detained-questioner clause (if not, that is B21's, not added here). `engine/season/hole_register.yaml` H-313 closed (its `cite:` names this item and the tests).
- WHERE: `engine/season/loop/predicates.py` (`_req_interrogate`); `engine/season/hole_register.yaml` (H-313); `engine/season/tests/test_vm_s2_c_case.py`.
- TESTS (CF-E8-3 FALSIFIER, "one hand-built test per row, each red before the edit"): `test_interrogate_with_another_seats_custody_is_refused`, `test_interrogate_of_a_subject_outside_the_duchy_is_refused` `[ASSUMPTION: test names; the item creates them]`, with "a positive control for each (the lawful act still executes)".
- FALSIFIER and CONTROL: "a hand-built `interrogate` with custody held by another seat, or the subject outside the duchy" admitted. Control: the lawful act executes; realm hashes at seeds 0–2 equal to B25.10's ("hash-EQUAL for computed play (hand-built acts only …)", CF-E8-3).
- GATE: `python -m pytest engine/season/tests/test_vm_s2_c_case.py -k interrogate -q` → pass; realm hash (`HASH READING`) at seed 0, one season → equal to B25.10's reading; the batch's close (CF-E8-3: "the B32/B03/B25 close's own gate").
- HASH MOVERS: none for computed play; "fixtures that hand-build such acts need updating" (grep `interrogate` under `engine/season/tests` at the open; each such fixture edited in this commit, named in the body).
- DEPENDS ON: V12 B25.10 (same function, after); V12 Batch B09 (the named-clause `_refuse`); EXISTS-IN-TREE `world_q.restrained`, `state/gate.py::purview_reaches`, `loop/predicates.py::_req_interrogate`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet` (CF-E8-3).
- LANDS IT: B25's producer; `Item: B25.11`, `[skip ci]`.

### B25.12 — `speak`: evidence sets the odds, the band sets what enters · S2C §2 · POINTER
- What it points at: S2C §2 ("cited items … enter as the `proofs` leverage source"; "`_eff_speak` … appends … one band stage"; "an answering `speak` carries `answers:`"), which by S2C's own head "yield[s] to `19_LACUNA_admission_rides_the_citing_draw.md` (entry) and `05_SC_evidence_and_rebuttal_B.md` (answer)" (U-2). Landed in B24: the `proofs` levels (B24.20), the host's exhibits (B24.21), the band dispatch and `speak.writes` `Record.stages` at all four bands (B24.25), the citing variants (B24.27).
- Target files and symbols: `loop/effects_information.py` (the `speak` effect); `seam/wrappers/sigma.py::contest_input`; `modules/social_contest/evidence.py::standing`.
- GATE: B24.25's (`test_sc_hearing_admission.py`, `test_sc_hearing_evidence.py`), re-read green in this batch's gate.

### B25.13 — a telling's odds the hearer sets · S2C §4 · BUILD · HASH EQUAL
- SOURCE: S2C §4 (copied), "Gate" §4, "Control"; OBS §2 members 6, 13; OBS §3 (`favour`: "a live `tie` of the actor to the counterparty"); C-21 (no `tell_obstacle` table).
- ADVANCES: R-07 (a telling to a friend is likely, never certain).
- INSTRUCTION (copied): "A telling's obstacle, through the one composer: `difficulty` + the stand-in or the hearer's `opposition` + `dissent` (OBS member 13: the teller's own ledger holds the hearer as believing the contrary on the cell; landed with `_SOCIAL2_B`) + `rank_gap` (member 6); a `tie` of the teller to the hearer is a `favour` level (OBS §3); a venue term from `venues.yaml` only where the SC lane lands one as a member. FI-02 edit 6 is answered by this composition: an ordinary telling to a friend is likely, never certain. Control: each member at its control step (today)." The edit is `tell`'s member list in the composer (`dissent` and `rank_gap` named for `tell`); each step stays at its control value (`dissent_step` 0, B25.06; `rank_step` at B21's control).
- WHERE: `engine/season/seam/wrappers/sigma.py` (the composer's member list for `tell`); `engine/season/verb_table.yaml` (`tell`'s note: the members named); `engine/season/tests/test_vm_s2_c_case.py`.
- TESTS: `test_tell_composes_dissent_and_rank_gap` `[ASSUMPTION: test name; the item creates it]` (a hand-built telling whose `terms` name `dissent` and `rank_gap` at their steps, and whose odds move when `dissent_step` is set in the test); the gate §4 reading function `test_news_told_share_is_strictly_between_0_and_1` (gate §4: "in `build_realm(0..2)` one season, `news.told` / (`news.told` + `news.untold`) rises above the baseline (2/6, 1/13, 0/2) and stays below 1": the baseline predates B05's composer, so the test asserts the share strictly between 0 and 1 and the commit body quotes it beside the source's baseline and the step's base reading `[ASSUMPTION: the reading that can be wrong at control — basis: at control steps the composition equals today's, so "rises" cannot be asserted until a step ships (B98)]`).
- FALSIFIER and CONTROL: "If any band outcome … occurs at every seed of ten under the shipped odds (or never), the odds are degenerate." Control: "every fixture at its control reproduces the pre-edit content hash."
- GATE: `python -m pytest engine/season/tests/test_vm_s2_c_case.py -k tell -q` → pass; realm hashes (`HASH READING`) at seeds 0–2, one season → equal to B25.11's.
- HASH MOVERS: none at the members' control steps (OBS §4 step 6+); the step flips are B98's.
- DEPENDS ON: V12 B25.06 (`dissent`); V12 Batch B05 (the composer, `favour`); V12 B21 (`rank_gap` with `14_VERBS_BINDING_A`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B25's producer; `Item: B25.13`, `[skip ci]`.

### B25.14 — `interview`: a draw to engage, then the questioned answers · S2C §3 · BUILD · HASH MOVER(behaviour)
- SOURCE: S2C §3 (copied), "Gate" §3, "Order of landing" ("§3 (after FI-02 edit 5 and S-A edit 5)"); C-29 ("§3 owns the `interview` row"); OBS §2 members 6, 7, §3 `favour`; rulings A-30, A-63, A-81 ("`interview.declined` is deposited to both parties"); B07's `contest_owed` (the orchestrator's relay); U-1; closes CP-T06-05 (intake `:476`, B25.08) and `audits/14_VERBS_SOCIAL2.md` §7.
- ADVANCES: FI standalone (questioning); R-06 (the questioned man chooses to answer, lie or stonewall).
- INSTRUCTION (copied):
  1. "`verb_table.yaml` `interview`: `contests: "a standing"`; `counterparty: subject`; `writes:` `[]` at every band (the product is a deposit and a question; no world cell moves); `emits:` Ov `[interview.asked, interview.pressed]`, Su `[interview.asked]`, Pa `[interview.asked, interview.disclosed]`, Fa `[interview.declined]`; `emits_on_refusal: {present: [interview.refused]}`. `finding.made` / `finding.none` leave the row (the inquiry roster's `finding.made` row then claims only graded inquiries)."
  2. "`rosters.yaml: verb_capability`: `interview: "inquiry"`" → the row's `capability: inquiry` cell (B04.04). "Obstacle, through the one composer: `difficulty` + `opposition` (the interviewee's skill score) + `rank_gap` (OBS member 6) + `regard` (member 7, the subject's hostile stance toward the asker); a `tie` of the asker to the subject is a `favour` level for the asker (OBS §3)."
  3. B07's relay: `interview` is deleted from `rosters.yaml: contest_owed` in this commit (the loader refuses a `contest_owed` member that declares `contests:`), and leaves any other class roster it sits in (U-6).
  4. "`rosters.yaml: question_sources`: new source `asked` (ordered after `claim_landed`, before `need` — a person asked a question attends to it; `attention_key` reads the order)."
  5. "`queries/world_q.py::questions_for`: for each `interview.asked` claim in the person's own ledger deposited this tick, one Question `q:asked:<claim id>`, source `asked`, plain referents `(on,)`, about the claim. The topic `on` is the interview act's operand: the subject of the asker's question's `about` claim, else the interviewee (derived in `_derive_operand`, no free choice)."
  6. "`decision/options.py::operand_bags`: on a Question of source `asked`, the `to` fan of `tell` and `lie` is the asker alone (read from the `about` claim's value, own ledger). The interviewee's chooser forms `tell`, `lie` or neither; his answer is that verb's own draw. At `interview.pressed` the questioner's press enters the answering act as the `approach` source (OBS §3: one `press_level` against the questioned person's answering `lie`), for this tick only (read off the claim, not held state; the source is `19_LACUNA_questioning_has_an_approach_and_a_cost.md`'s)" — that source lands in B26.01; until then the press term reads nothing (its control).
  7. "`loop/witness.py`: no edit. … at `interview.disclosed` the deposit also names the asker's own question's `about` claim, so the interviewee learns why he was asked." (SITE: if the disclosed deposit needs a line to name the `about` claim, it is written in the effect's receipt, not in `witness.py`; record which.)
  8. Draw key (A-30): `"interview.standing"` `[ASSUMPTION: the prize suffix — basis: S2C's form `"<verb>.<prize>"` with the prize `a standing`]`. A-63: "An `interview` debits the interviewee's scene for the round [lap]" — the debit is `28_CORE_scene_access_A`'s (B28); "round" → "lap" (A-101).
  9. Glossary: row *interview*: "to interview: to question a person who is present, who then answers, lies or keeps silent by his own choice".
  10. A pointer for the FI lane (Batch B24p-sc-proceeding, RD §D.1): when `interview` is drawn its row takes `proceeds: {row: questioning, form: full}`; OBS's `approach` source (`press_level`, step 6) is the `press` move and is not a second lever (read at stage 3: this body was opened, so the proposal's `[UNVERIFIED]` mark is struck).
- WHERE: `engine/season/verb_table.yaml` (`interview`); `engine/season/rosters.yaml` (`question_sources`, `contest_owed`, the class roster); `engine/season/queries/world_q.py` (`questions_for`); `engine/season/decision/options.py` (`_derive_operand`: `on`; `operand_bags`: the `asked` fan); `engine/season/tests/test_vm_s2_c_case.py`; `unified/U1_GLOSSARY.md` (*interview*).
- TESTS (written first, red): `test_the_questioned_answer_or_decline` (gate §3: "across seeds the interviewee forms `tell` or `lie` to the asker in the interview's tick at ≥ 1 seed, and `interview.declined` occurs at ≥ 1 seed; the asker then holds the answer with the interviewee on its chain"; seeds 0–9); `test_the_questioned_answers_the_asker_at_some_draw` `[ASSUMPTION: test name]` (CP-T06-05's falsifier, B25.08: 40 act-id draws, share above zero; its control arm "the shipped row … in the same world" is the tree before this item, read as `reading @<sha>`); `test_interview_has_left_contest_owed` `[ASSUMPTION: test name; the item creates it]` (the B07 loader reads `interview` as class `contest` and not in `contest_owed`).
- FALSIFIER and CONTROL: "Equal shares mean the item does nothing, and it is reverted" (CP-T06-05). Control: "realm `interview` and `tell` attempted/ok at seeds 0-2" before (the step's base) and after, quoted.
- GATE: `python -m pytest engine/season/tests/test_vm_s2_c_case.py engine/season/tests/test_task_draw.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 s`, s = 0, 1, 2 → `interview` attempted and executed, `interview.asked` and `interview.declined` counts quoted.
- HASH MOVERS: declared ("declared hash movers wherever these verbs execute"). B25.99.
- DEPENDS ON: V12 B25.02 (S2A edit 5), B25.13; V12 B11.08 (`08_FI_02` edit 5); V12 Batch B07 (`contest_owed`); V12 Batch B05 (the composer, `opposition`, `favour`); EXISTS-IN-TREE `world_q.questions_for`, `options.operand_bags`, `options._derive_operand`.
- GLOSSARY: *interview* (step 9).
- COST and TIER: small build; `sonnet`, `high`; §3's draw `opus`; one `opus` read of the ten-seed band tables.
- LANDS IT: B25's producer; `Item: B25.14`, `[skip ci]`.

### B25.15 — a Record sub-kind class; `research` keeps its bare pair · S2A edit 2 with MC's `research` pair · BUILD · HASH MOVER(behaviour)
- SOURCE: S2A "Exact edits, by owner" 2 (copied), its first Reconciled line (C-19, C-28: "`_stamped` carries both pairs, the bare `Record` and the qualified one, so `research` and `seize` still form"), "Order of landing" ("edit 2 is one commit across families"), "Gate", "Falsifier"; MC's Lands line and §4 step 1 ("SOCIAL2-A edit 2, with the correction `audits/14_VERBS_MATERIAL.md` §17.2 lists (both pairs stamped)"); U3 §4.1 row 46 (C-28: "the `_stamped` pair for `research` lands with `14_VERBS_SOCIAL2_A` edit 2 in B25"); C3-Y10 (after S2B and S2C add their kinds); closes `construe`'s, `comply`'s and `evade / defy`'s `record_subkind` refusals (`audits/14_VERBS_SOCIAL2.md` §4).
- ADVANCES: R-03; `BUILT OUT` `construe` (its formation; B25.16 its effect).
- INSTRUCTION (copied):
  1. "`rosters.yaml: referent_classes`: the `Record` class is qualified: `Record.<kind>`, `<kind>` a `record_kinds` member. Authored on the row (data a designer reads), validated by `engine/season/data/verbs.py` at load: the qualifier must equal the kind the row's typed `existence(subject, <kind>)` cell names (a row without such a cell may not qualify)."
  2. "`queries/world_q.py::_stamped` stamps a Record id as `Record.<its kind>` (the World answers the kind; `opening_set` still never asks, L2)" — and, by C-19/C-28, "carries both pairs, the bare `Record` and the qualified one": `(id, Record)` beside `(id, Record.<kind>)` (B26's part, its `14_VERBS_MATERIAL_E` item, relies on the bare pair: "`research` forms on bare `Record`").
  3. "`verb_table.yaml`: `construe` `referent_class: Record.dispensation`. **The same edit, in the same commit, on every row that declares `Record` today** (`comply`, `evade / defy` → `Record.dispensation`; `accept` → `Record.challenge`; `carry` → `Record.petition`; `found`, `build` → `Record.works`), because once `_stamped` qualifies the class a row still declaring bare `Record` forms on nothing. Those rows belong to other families; this landing is one commit or none." `research` and `seize` keep bare `Record` (the pair). SITE: `git grep -n "referent_class: *Record\b" engine/season/verb_table.yaml` at the open; every row it lists is either in the list above, or keeps bare `Record` by the pair rule, and is named in the commit body.
  4. MC's interim works stamp (B12c: "carried on the classed tuple as `Record` with the plan kind on the stamp") is replaced by `Record.works` in this commit ("`Record.works` replaces it when SOCIAL2-A edit 2 lands").
  5. "`data/verbs.py::RECORD_REFERENT_KINDS` and `HOLDING_RECORD_KINDS` become readings of the qualifiers (one owner) rather than derivations from the typed cells."
- WHERE: `engine/season/rosters.yaml` (`referent_classes`); `engine/season/queries/world_q.py` (`_stamped`; MC's works stamp in `questions_for`); `engine/season/verb_table.yaml` (`construe`, `comply`, `evade / defy`, `accept`, `carry`, `found`, `build`); `engine/season/data/verbs.py` (the qualifier check, `RECORD_REFERENT_KINDS`, `HOLDING_RECORD_KINDS`); `engine/season/tests/test_vm_s2_a_formation.py`.
- TESTS: `test_vm_s2_a_formation.py::test_construe_forms_on_the_writ_alone` (S2A falsifier: "a writ and a faction sheet held by one person: `construe` forms on the writ alone"), `::test_research_and_seize_still_form_on_a_bare_record` (C-28), `::test_a_qualifier_unequal_to_the_existence_cell_is_refused` `[ASSUMPTION: test names; the item creates them]`; `test_s2a_refusals_and_executions` gains "refusals 0 for … `construe`, `comply`, `evade / defy` on `record_subkind`" and "executions of … `comply` not lower than the baseline". Written first, red.
- FALSIFIER and CONTROL: a row still declaring bare `Record` (other than `research`, `seize`) that forms on nothing; executions of `found`, `build`, `research`, `seize` falling. Control: those four verbs' executions at seeds 0–2, one season, equal to or above B25.14's reading ("A fall is the stopping rule … revert that edit").
- GATE: `python -m pytest engine/season/tests/test_vm_s2_a_formation.py engine/season/tests/test_works_founding.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 s`, s = 0, 1, 2 → the `record_subkind` refusals 0; one `opus` read of "the executions-not-lower table" (S2A tier).
- HASH MOVERS: declared, every world (wrong-kind formations stop). B25.99.
- DEPENDS ON: V12 B25.03 to B25.14 (S2B and S2C add their kinds first, C3-Y10); V12 Batch B12c (MC's works rows and interim stamp); EXISTS-IN-TREE `world_q._stamped`, `data/verbs.py::RECORD_REFERENT_KINDS`, `::HOLDING_RECORD_KINDS`.
- GLOSSARY: none (*referent class* keeps its row; the qualifier is a form of it).
- COST and TIER: small build (cross-family, one commit); `sonnet`, `high`; one `opus` read of the executions table.
- LANDS IT: B25's producer; `Item: B25.15`, `[skip ci]`.

### B25.16 — `construe`: a reading of an order, drawn · S2B §2 · BUILD · HASH MOVER(behaviour)
- SOURCE: S2B §2 (copied), "Gate" §2, "Falsifiers" §2; OBS members 24, 25; rulings A-27 ("§2's construal toward his own interest"), A-30, A-81 ("`construal.failed` … [is a] witnessed deed"); closes H-36 (the row's falsifier, two holders and two readings).
- ADVANCES: `BUILT OUT` `construe`; R-06 (a man reads an order his way).
- INSTRUCTION (copied):
  1. "`verb_table.yaml` `construe`: `contests: "a proposition"` (against the writ; the standing rule: whether a reading takes could go either way); `writes:` `Proposition.exists` at Ov / Su / Pa, `[]` at Fa; `emits:` Ov `[terms.construed, construal.credited]`, Su `[terms.construed]`, Pa `[terms.construed, terms.distorted]`, Fa `[construal.failed]`; `emits_on_refusal: [construal.impossible]` (requirement checks only); `writes_note` replaced: *the construer attempts a `HOLDS` reading of the terms' subject and predicate with his own held value; the draw decides whether it takes; the writ is unchanged*; `referent_class: Record.dispensation` [B25.15]. `terms.distorted` keeps its name and moves to Pa, where witnesses hold the reading as a twist." The row leaves its B07 class roster (U-6).
  2. "`rosters.yaml: verb_capability`: `construe: "argue"`" → `capability: argue`. "Obstacle, through the one composer: `difficulty` + the stand-in (no person opposite: the writ) + `clarity` (OBS member 24 …; `clarity_step`) + `deference` (member 25 …; `deference_step`)." Both join `obstacle_terms` with steps at 0 (OBS §4 step 6+).
  3. "`loop/effects_information.py`: new `_eff_construe(w, a, res) -> Change`, called by the fold at Ov / Su / Pa only: 1. read the writ `w.records[subject]`, its `terms` (a Proposition id via `ABOUT_KEYS["dispensation"]`); decline `NO_CHANGE` (→ `construal.impossible`) if no Proposition; 2. the construer's own value on `(terms.subject, terms.predicate)`: the newest such claim in his own ledger (`person_q` `LedgerReader`, the one comparator) — decline if none or equal to `terms.value`; 3. mint `Proposition(f"prop:{a.id}", "HOLDS", terms.subject, terms.predicate, his_value, w.tick)` and `_makers_hold` — … called through a shared `_mint_proposition(w, actor, prop)` helper [B25.06]." "Steps 1–2 are asked again in the row's predicate before the draw, so a refused act costs no draw (`_req_interrogate`'s placement)."
  4. Draw key (A-30): `"construe.proposition"`.
  5. Glossary: row *construal* (add or edit): "a construal: a person's reading of what an order means, which may be bent toward his own interest (A-27)".
- WHERE: `engine/season/verb_table.yaml` (`construe`); `engine/season/rosters.yaml` (`obstacle_terms`: `clarity`, `deference`; the class roster); `engine/season/data/fixtures.py` (`clarity_step`, `deference_step`); `engine/season/seam/wrappers/sigma.py` (the two members' host functions); `engine/season/loop/effects_information.py` (`_eff_construe`); `engine/season/loop/predicates.py` (`construe`'s predicate, steps 1–2); `engine/season/hole_register.yaml` (H-36); `engine/season/tests/test_vm_s2_b_word.py`; `unified/U1_GLOSSARY.md` (*construal*).
- TESTS (written first, red): `test_construe_two_holders_two_readings` (gate §2: "hand-built: issuer, writ with `HOLDS` terms, two holders, one believing otherwise: at a planted `Success` the two holders hold different readings (the row's falsifier, `H-36`); at a planted `Partial` witnesses hold `terms.distorted`; at a planted `Failure` no Proposition is minted; `construal.impossible` (no draw) for the holder who agrees. Over seeds 0–9 with the shipped odds, all four bands occur"); `test_a_construer_who_agrees_forms_none` (falsifier §2). `[ASSUMPTION: test names; the item creates them — basis: S2B names no function; E-3]`
- FALSIFIER and CONTROL: "a construer whose value equals the terms forms none." Control: the step's base hashes with `construe` unformed (B25.15's reading for a world with no writ).
- GATE: `python -m pytest engine/season/tests/test_vm_s2_b_word.py -k construe -q` → pass; `python tools/ci_sim_fabrication_check.py` → exit 0.
- HASH MOVERS: declared, every world in which `construe` folds. B25.99.
- DEPENDS ON: V12 B25.15 ("§2 (after S2-A edit 2)"), B25.06 (`_mint_proposition`); EXISTS-IN-TREE `person_q.ABOUT_KEYS`, `loop/effects_information.py::_makers_hold`.
- GLOSSARY: *construal* (step 5).
- COST and TIER: small build; `sonnet`, `high`; the contested row `opus`.
- LANDS IT: B25's producer; `Item: B25.16`, `[skip ci]`.

### B25.17 — a construal is citable beside the terms · `IS-B2-SC-07` step (1) · BUILD · HASH EQUAL
- SOURCE: IS-B2 §1.1 "Item: IS-B2-SC-07" (step (1) copied; step (2) is B27's; U-9); `unified/U4_TRACEABILITY.md` G-13 (the carry text); ruling A-27 ("a construal is testable by a court against the terms").
- ADVANCES: A-27; FI and SC integrated.
- INSTRUCTION (copied): "(1) B25: an edit 5 to `14_VERBS_SOCIAL2_B_a_word_with_content.md` §2: a construal's Proposition (`prop:{act id}`, minted by `_mint_proposition` …) is citable at a sitting as an exhibit beside the writ's `terms` Proposition." WHERE (IS-B2): "`engine/season/loop/effects_information.py` (the citing `speak`'s admitted kinds), `engine/season/rosters.yaml: proofs`" — the construal's Proposition joins the kinds the citing `speak` admits (B24.25's filing refusal reads `proof_kind`, B24.22), and `proofs` admits it under the arrangement rows that admit a `dispensation`'s terms `[ASSUMPTION: which `proofs:` rows admit it — basis: IS-B2-SC-07 names `rosters.yaml: proofs` and no row; the item writes it beside each row that admits the terms and names them in the body]`.
- WHERE: `engine/season/loop/effects_information.py` (the `speak` effect's admitted kinds); `engine/season/rosters.yaml` (`proofs`); `engine/season/queries/person_q.py` (`proof_kind`, if a Proposition needs its kind there); `engine/season/tests/test_vm_s2_b_word.py`.
- TESTS: `test_a_construal_proposition_is_citable_beside_the_terms` `[ASSUMPTION: test name; the item creates it]` (a hand-built sitting: a party holding a construal cites it; the filing `speak` files it at its band beside the terms); the named test `test_a_construal_contradicting_the_terms_loses_at_the_bench` is B27's (U-9).
- FALSIFIER and CONTROL: a cited construal refused at filing while the terms are admitted. Control: "a construal equal to the terms forms no act (S2-B `:204`)"; realm hashes equal to B25.16's.
- GATE: `python -m pytest engine/season/tests/test_vm_s2_b_word.py -k citable -q` → pass; realm hash (`HASH READING`) at seed 0, one season → equal.
- HASH MOVERS: "none until a bench convenes on a construal."
- DEPENDS ON: V12 B25.16; V12 B24.22, B24.25.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`; the contested degree is B27's `opus` read.
- LANDS IT: B25's producer; `Item: B25.17`, `[skip ci]`.

### B25.18 — the reader first, then the producer · FI08 §3 · POINTER
- What it points at: FI08 §3 ("`_eff_tie` is not re-designed; IN-32's commit is the build. It re-lands when both hold: (a) chained told claims exist in seeded play, which is `08_FI_02`'s gate (two-hop chains above 0) …; (b) the person-side decline … is in place … (`08_FI_02` edit 5's `present_persons` reader serves both)"), which S2D carries and "does not redo" (S2D: "Follows `08_FI_08_knots-season-form.md` §3 (the reader first, then the producer)"). Built as B25.19 (the row and the effect, written from the row, W3-4a: IN-32's attempt `53ed995d` is not reachable) and B25.20 (the `tied` term).
- The two conditions are read at B25.19's open (its STOPS IF): (a) B11's close reading of FRES §2 row 3 ("two-hop chains above 0 at two of three seeds", B11.99); (b) `present_persons` (B11.08).
- GATE: FI08 "§3: at re-land, `tied()` is called more than 0 times in a seeded realm and the `tie_gain` 0 and 0.5 arms hash differently" — read in B25.20's GATE (named test `test_knots_season_form.py::test_tied_is_called_and_tie_gain_arms_hash_differently`). FI08's falsifier: "if chained claims exist and `tied()` still reads 0 calls, the relation term is not reached for another reason; stop and report, as IN-32 did."

### B25.19 — `tie`: a chosen bond, drawn for; `knot` handed on · S2D edits 1–3, 6 · BUILD · HASH MOVER(behaviour)
- SOURCE: S2D "Exact edits, by owner" 1, 2, 3, 6 (copied), "Gate", "Falsifiers"; A-28 (the split); `04` §A.3 row 9 (directed edges); rulings A-30, A-81 ("`bond.refused` is witnessed by both parties"); U-7; closes H-182 (the `tie` half; `knot` stays declined, the Thread lane's).
- ADVANCES: `BUILT OUT` `tie`; R-06 (networks of trust form with no player).
- INSTRUCTION:
  0. STOPS IF (FI08 §3, B25.18): B11's close reads two-hop told chains at 0 at two or more of three seeds, or `person_q.present_persons` is absent: the item stops (`STOPPED`) with the reading, and the row stays declined.
  1. S2D edit 1, copied: "**`engine/season/verb_table.yaml`**: delete the `tie / knot` row; add, carrying its notes forward:"
     ```yaml
     - verb:        "tie"
       stratum:     social
       eligibility: [own]
       beneficiary: actor
       counterparty: to
       requires:    "the partner is with him and known to him"
       requires_typed: {all: [{form: relation, of: to, relation: with, conjunct: present},
                              {form: own_ledger, of: to, conjunct: known}]}
       contests:    "a standing"
       writes:
         Overwhelming: ["Tenure.since"]
         Success:      ["Tenure.since"]
         Partial:      ["Tenure.since"]
         Failure:      []
       emits:
         Overwhelming: ["bond.formed"]
         Success:      ["bond.formed"]
         Partial:      ["bond.formed"]
         Failure:      ["bond.refused"]
       emits_on_refusal: {present: ["tie.refused"], known: ["tie.refused"]}
       grade:       assumption
     - verb:        "knot"
       stratum:     thread
       eligibility: [own]
       requires:    "—"
       writes:      ["Tenure.since"]
       emits:       ["bond.formed"]
       emits_on_refusal: []
       grade:       ruled
       effect_decline_note: "<the H-182 text for knot; owned by the 29f / Thread lane; FI-08 §1>"
     ```
     "`resolvable_verbs()` admits `tie` once its effect exists; `knot` stays out." `tie` is placed in no B07 class roster but `contests:` (a new row); `knot` (declined, no effect) is placed where the B07 loader puts a declined row `[ASSUMPTION: a declined row needs no class — basis: B07's refusal reads "a row that writes or emits a finding and is in none of the three"; `knot` writes `Tenure.since`, so the item reads the loader at the open and, if it refuses `knot`, lists it under `bookkeeping_verbs` with `why:` "declined; owned by the Thread lane (A-28)"]`.
  2. S2D edit 2: "`verb_capability: tie: "copying"`" → `capability: copying` on the row (B04.04). "The obstacle, through the one composer: `difficulty` + `opposition` (the partner's skill score, A-79) + `regard` (OBS member 7 …) + `rank_gap` (member 6); the partner's favourable stance is a `favour` level for the actor (OBS §3), not a −1."
  3. S2D edit 3, copied: "**`loop/effects_information.py`** (the module holding `_eff_commit`, beside it; the `"tie"` literal must sit in a file `_derive_openers_from_effects` walks)."
     ```python
     @effect_for("tie")
     def _eff_tie(w, a, res=None) -> Change:
         to = _operand(a, "to")
         if res is None or to is None or to not in w.persons:
             return NO_CHANGE
         if any(t.kind == "tie" and t.subject == a.actor and t.object == to and t.live for t in w.tenures):
             return NO_CHANGE                      # he already owns a live tie to `to`
         edge = Tenure(H(w.world_seed, w.tick, a.actor, f"tie:{to}:{a.id}"), a.actor, to, "tie",
                       since=w.tick, degree=res.degree)
         return Change((Subject.edge(edge),), lambda: w.add_tenure(edge))
     ```
     "Typed in: `(World, Act, Resolution)`; out: `Change`. The edge is the actor's own (T-m); no edge is opened for the partner (directed, `04` §A.3 row 9)." Draw key (A-30): `"tie.standing"`.
  4. S2D edit 6: "the split adds one verb row, so the count read by R-05's instrument moves; no code names the count, and the count is quoted as a reading at the batch that lands it (B25), never typed into prose (C3-N30 …)" — Reading R2.
  5. `engine/season/hole_register.yaml` H-182: closed for `tie` (its `cite:` names this item); its `knot` half stays (the Thread lane's, B35).
  6. Glossary: rows *tie* and *knot* (A-28): "a tie: a bond a person chooses to make to someone present, owned by him alone"; *knot* keeps "the Thread lane's bond; declined here".
- WHERE: `engine/season/verb_table.yaml` (`tie / knot` → `tie`, `knot`); `engine/season/loop/effects_information.py` (`_eff_tie`); `engine/season/rosters.yaml` (the class roster, if `knot` needs one); `engine/season/hole_register.yaml` (H-182); NEW `engine/season/tests/test_vm_s2_d_tie.py`; `unified/U1_GLOSSARY.md` (*tie*, *knot*).
- TESTS: in the new file (S2D's test file), written first, red: `test_tie_is_attempted_and_both_bands_occur` (gate: "`build_realm(s)`, s = 0, 1, 2, two seasons, `PYTHONHASHSEED=0`: `tie` attempted > 0, both `bond.formed` and `bond.refused` occur across seeds"); `test_a_tie_by_a_to_b_does_not_lower_bs_tellings_to_a` (falsifier 2: "directed: B owns no edge"); `test_knot_never_forms_while_declined` (falsifier 3). `[ASSUMPTION: test names; the item creates them — basis: S2D names no function; E-3]`
- FALSIFIER and CONTROL: as the three tests. Control: the step's base `aperture` reading of every other verb's executions (a `tie` that starves another verb is read there).
- GATE: `python -m pytest engine/season/tests/test_vm_s2_d_tie.py engine/season/tests/test_task_draw.py -q` → pass; `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`).
- HASH MOVERS: declared (U-7): every seeded world in which `tie` executes (a `Tenure` of kind `tie` per taken bond). B25.99.
- DEPENDS ON: V12 B25.13, B25.14 (the composer's members on a person-to-person row); V12 B11.08 (`present_persons`); V12 Batch B05 (`regard`, `favour`); V12 B21 (`rank_gap`); EXISTS-IN-TREE `loop/effects_information.py::_eff_commit` (`@effect_for`, `_operand`, `Change`, `Subject.edge`), `state/carriers.py::Tenure` (`degree`).
- GLOSSARY: *tie*, *knot* (step 6).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B25's producer; `Item: B25.19`, `[skip ci]`.

### B25.20 — a tie weighs the teller, behind `tie_gain` at 0 · S2D edit 4 · BUILD · HASH EQUAL
- SOURCE: S2D edit 4 (copied), edit 5 ("no edit"), "Gate", first "Falsifier"; FI08 §3's gate; U-7.
- ADVANCES: R-07 (who believes whom follows who is bound to whom).
- INSTRUCTION (copied): "**`decision/options.py::teller_weight`**: a `tied` term reading the hearer's own live `tie` to the teller and its `degree`, scaled by `rosters.yaml: task_fraction[degree]` (… Partial half), times fixture `tie_gain` (control 0; NUMBER row)." `tie_gain = 0` in `data/fixtures.py` with its tag. Edit 5: "The teller's own live `tie` to the hearer already enters a telling's odds as the `favour` source (OBS §3 …)" — no edit.
- WHERE: `engine/season/decision/options.py` (`teller_weight`: `tied`); `engine/season/data/fixtures.py` (`tie_gain`); `engine/season/tests/test_knots_season_form.py`; `engine/season/tests/test_vm_s2_d_tie.py`.
- TESTS: `test_knots_season_form.py::test_tied_is_called_and_tie_gain_arms_hash_differently` (FI08 §3: "`tied()` is called more than 0 times in a seeded realm and the `tie_gain` 0 and 0.5 arms hash differently"; two seasons, seeds 0–2, the 0.5 arm set inside the test); `test_vm_s2_d_tie.py::test_tie_gain_zero_hashes_as_the_control` ("`tie_gain` 0 must hash as the control; if not, a tie is read somewhere it should not be"). Written first, red.
- FALSIFIER and CONTROL: "`tie_gain` 0 must hash as the control." Control: B25.19's after-reading (`tie_gain` 0).
- GATE: `python -m pytest engine/season/tests/test_knots_season_form.py engine/season/tests/test_vm_s2_d_tie.py -q` → pass; `python tools/ci_sim_fabrication_check.py` → exit 0; realm hashes (`HASH READING`) at seeds 0–2 → equal to B25.19's.
- HASH MOVERS: none at `tie_gain` 0 ("the one declared mover is the later flip of `tie_gain` off 0 … re-pinned once in that flip's own commit": B98, DIALS AT CONTROL).
- DEPENDS ON: V12 B25.19; EXISTS-IN-TREE `decision/options.py::teller_weight`; V12 B07.02 `rosters.yaml: task_fraction` (not in the tree: B07.02 creates the roster and `data/rosters.py::TASK_FRACTION`).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`; one `opus` read of the `tie_gain` arms.
- LANDS IT: B25's producer; `Item: B25.20`, `[skip ci]`.

### B25.21 — the verb table's count · READING
- In the position table only; its text is Reading R2 below.

## Readings (B25)

R1 (moved from B11.74 to this batch by B11's part, §5.8; the source `proposals/19_LACUNA_conclusion_is_a_committed_assertion.md` "Gate (execution artifacts)" first line, copied byte for byte): "On `inquiry_world(seed)` (`08_FI_03` §1), seeds 0-19, four seasons, `PYTHONHASHSEED=0`: - a Proposition is uttered after a winning `reconstruct` in more than zero runs (today `reconstruct` deposits nothing), every one carrying a non-empty `support` whose ids the utterer held at the act". Read here at **two seasons** (four seasons in the source; A-114), after B25.06 (typed `utter` forms from a held claim, S2B §1) and on B07's `reconstruct` as an inquiry (`form: inquiry`, B07's UNDECIDED (2)). Expected: above zero runs, every such Proposition's `support` non-empty and held. A zero is reported in the close with the run's `reconstruct` and `utter` counts, as a finding about the two-season horizon or the chain, not hidden.

R2 (S2D edit 6; IS-A §12.2 row B25, "the table reads 68 by command"): `python -c "from engine.season.data.verbs import VERB_TABLE; print(len(VERB_TABLE))"` on the closing tree → 68, quoted with its SHA. The pin B02 kept for R-05's denominator ("a reading of `main` (67), re-read and re-recorded at B25 (A-28's `tie`/`knot` split, 68)", part 3's B02 item) is re-recorded in B25.99, said plainly.

### B25.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12; `IS-A-12`.
- ADVANCES: R-04.a (`open_case`); `BUILT OUT` `construe`, `interrogate`, `tie`.
- INSTRUCTION: (1) re-record the realm pins in `engine/season/tests/_realm_goldens.py` and every digest the movers reached (the batch's RE-PIN line), once, against the step's base (`reading @<sha>`: B20's after-reading, B20 merging before B25 in S16, part 2 §3; lane H3), act and Event tallies quoted beside each moved pin; the commit says "re-pin" and names the movers; (2) re-record the R-05 denominator pin (Reading R2: 68); (3) run the batch gate's seeded commands (two seasons at most) and the one full-suite run (CLAUDE.md §0.4); (4) write the `reading:` record of R-04.a for `open_case` in `engine/season/requirements.yaml` (no `status:` edit); (5) the commit body carries Readings R1, R2, the `BUILT OUT` lines and the close's record (§5.12).
- WHERE: `engine/season/tests/_realm_goldens.py`; the R-05 denominator pin's file (B02's; read at the open); `engine/season/requirements.yaml` (`reading:` only); `engine/season/tests/test_go07_canonical_digest.py` (only if its vectors moved).
- TESTS: none new; every test file in the batch gate.
- FALSIFIER and CONTROL: a pin re-recorded whose tallies moved with no declared mover in the batch; `construe`, `interrogate` or `tie` not built out (`IS-A-08`: a failed gate). Control: each fixture at its control (`utter_content: off`, `petition_addressee: referent`, `oblige_admission: fiat`, `tie_gain` 0) reproduces the base hashes at seeds 0–2 (S2B, S2C "Control" lines), read once.
- GATE: the BATCH GATE above.
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: V12 B25.01 to B25.21.
- GLOSSARY: none.
- COST and TIER: reading (and the re-pin edit); `sonnet`; the close's terminal critique `opus`.
- LANDS IT: B25's producer; `Item: B25.99`, the batch's last `Item:` commit (no `[skip ci]`).

| STOP. Batch B25-fi-questioning closes here |

The last item this file wrote: B25.99.
