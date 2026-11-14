# Workplan v12 — part 11, continued: batch B09-memory

## Status: PROPOSED (the continuation of part 11 of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `aa31fd2`, read 2026-11-12; author lane A11. The head of part 11 (its first file) states the words, paths and renamed identifiers this file uses; B09 lands after B04, so the season's within-season pass is `lap` (`Claim.lap`, `SeasonDriver.lap`, `scenes_per_lap`) wherever copied text says `round` for it.

---

## Batch B09-memory · lane IN · wave W10 · step S10 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B09-memory
IN-FLIGHT ROW: registers/handoffs/HANDOFF_IN.md, Open table
GATE: Batch B00-ids @c3418a6a160fc6a17e5a8bf45112a0e55699a695
GATE: Batch B01-laneA @cfd9aefb049c2fe49b55c7ada1b0b624919af23d
GATE: Batch B02-tests
GATE: Batch B05-one-roll
GATE: Batch B07-task-draw
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading").
REQUIREMENT: re-read R-01.b, R-01.c, R-02.a, R-02.b, R-07.a → unchanged (each conjunct `holds: yes` as B02 left it, `IS_A_NINE_part2.md` §12.2 row B09); rulings served: A-24 (a crisis is drawn and seen: the scar half here), A-33, A-47, A-62, A-81 (a refusal is remembered), D-46, D-48
BATCH GATE (read once, on the closing tree; `PYTHONHASHSEED=0` on every seeded command):
  `python -m pytest engine/season/tests/test_claim_fade_as_read.py engine/season/tests/test_refusal_memory.py engine/season/tests/test_one_reader_of_a_ledger.py engine/season/tests/test_g1a_act_store_and_receipts.py engine/season/tests/test_g4_no_op_receipt.py engine/season/tests/test_in53_vacancy_need.py engine/season/tests/test_in50_refusals_carry_the_occasion.py engine/season/tests/test_choose_watch.py engine/season/tests/test_in62_decision_spread.py engine/season/tests/test_scene_store.py engine/season/tests/test_g2_token.py engine/season/tests/test_seen_why.py engine/season/tests/test_predicates_clause.py engine/season/tests/test_gate_observation.py -q` → all pass;
  the control arms, each at seed 0, two seasons, against the reading named: `refusal_memory = 0.0` → content hash equal to B09.03's reading (U3 §1 item 10's gate, "`refusal_memory = 0.0` equal"); `weigh_confidence = False` → equal to B09.06's; `standing_occasion_cause = False` → equal to B09.11's; `connection_chance = 0.0` and `finding_none_deposit: none` as shipped (no move);
  `python -m engine.season.harness.decision_spread --retries --seed 0 --seasons 2` → B09.05's five rows, quoted;
  `python -m engine.season.harness.chronicle --seed N --seasons 2 --chains --min-depth 2`, N = 0, 1, 2 → exit 0, a `for:` line per act (B09.16);
  `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` → its act and Event tallies quoted against the S9 merged head's (`reading @<sha>`);
  the realm content hash of `build_realm(s)`, two seasons, s = 0, 1, 2 → moved (declared) and re-recorded by B09.99;
  `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `--requirements` → nine lines, R-01.b, .c, R-02.a, .b, R-07.a `holds: yes`; `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (engine core and registries: the full gates);
  the glossary rows each item names, read against the code it landed (`STAGES.md`, "The glossary always matches", rule 2);
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the five named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; B09.99 writes the five conjuncts' `reading:` records; `status:` is not edited (`IS-A-12`).
RE-PIN: once, in B09.99: every realm pin in `engine/season/tests/_realm_goldens.py`, `test_go07_canonical_digest.py`'s vectors where they moved, and every content hash pinned under `engine/tests` (the record proposal: "one deliberate golden re-record across `engine/season/tests` and `engine/tests` wherever a content hash is pinned"), read against the S9 merged head (B07's and B17's merges, `reading @<sha>`); the commit says "re-pin: fewer Events (B09.01), a filled `Receipt.delta` and `scar.taken` Events (B09.10, B09.11), the opening Event in `causes` (B09.12), the shipped `refusal_memory` and `weigh_confidence` (B09.05, B09.08), the re-pointed belief readers (B09.07), no zero-wear `condition.worn` (B09.21), a seat's closing names its holder (B09.22, lane D4)".
EXPECTED RED UNTIL B09.99 (under `[skip ci]`, E-1; one batch line, repair lane R1): the realm and corpus pins any mover item of this batch moves read red from its first mover (B09.01) to the re-pin; the files that pin them (`git grep -lE '"[0-9a-f]{32}"'` over the test trees and the golden files, those this batch names): `engine/season/tests/_realm_goldens.py` (B02's one pin file); `engine/season/tests/test_go07_canonical_digest.py` (its asserting test, `SHIPPED`/`CENSUS`).
IDS: ED-IN 0; H 4 (B09.03: `refusal_memory`'s HOLE row; B09.12: `standing_occasion_cause`'s row; B09.17: `connection_chance`'s row; B09.20: `sworn_bond`'s NUMBER row, added by lane D4 — B00's H block for B09 is owed one more slot; each `[JUSTIFIED: … H-nnn]` line cites its slot)
DIALS AT CONTROL: `refusal_memory` = 0.0 at B09.03; set by this batch's B09.05 (0.5); target: the five readings of `16_PESSIMIST_CORE_a_refusal_is_remembered` "Gate". `weigh_confidence` = `False` at B09.06; set by B09.08 (`True`); target: `16_PESSIMIST_SC_B` "Gate". `standing_occasion_cause` = `True` shipped by B09.12 (control `False`). `finding_none_deposit` = `none`; set by B98; target: "failed inquiry aims tried again fall at the `actor` arm with `refusal_memory` above 0 … deposits to non-actors equal across arms" (`U5a_DICE_owed_edits` §4 "Gate", seeds 0–2, two seasons). `connection_chance` = 0.0; set by B98; target: `16_PESSIMIST_GO_a_witness_may_connect_what_he_holds` gates 2–5 on-arm ("proposed on-value 0.6, + 0.2 where his claim on the antecedent carries a `who`", `[ASSUMPTION; medium; Jordan to correct]` in the source). `sworn_bond` = 0.0 at B09.20 (lane D4); set by no batch of v12; target: IN-58's falsifier (two judges with equal stance and pursuits, one sworn, read different regard for the killer) at a swept arm; no value stated.
UNDECIDED: (1) `01_CORE_claim_fade_as_read` edit 5 (raise `corpus_run.MAX_SEASONS` to 16 "once the gate below reads flat") is not carried: its condition is an eight-season reading that A-114 holds to B99; the clamp stays 6 and H2's held table is owed the row (the other reading: raise it now, which no gate before B99 can justify). (2) The source gates at three, four and eight seasons (`claim_fade` tests, `a_refusal_is_remembered`'s five readings, `test_scene_store`'s "three seasons") are written at two ("(… seasons in the source; A-114)"), `V12_STRUCTURE_part2.md` §5.8. (3) `U5c_VERBS_residue_and_governance_owner` §3 is not in this batch although U3 §4.1 row 28 puts it here: step 1 extends CP-T06-04's deposit ("Plan CP-T06-04 (B10-14) already deposits …"), which is not in the tree at `aa31fd2` and lands in B11 (the intake's merged item H-314, CP-T06-03, CP-T06-04), and step 2 edits `person_q.present_persons`, which `08_FI_02` edit 5 builds in B11: the dependency wins (`V12_STRUCTURE_part4.md` E-8); owed to the B11 authors (A16, A17). (4) `01_CORE_predicates_name_their_clause` step two's four keyed rows (`confer`, `establish`, `revoke`, `oblige`) need kinds "authored in `verb_table.yaml` by the FA lane … in the same batch or B21": B09 lands the channel (B09.19, hash EQUAL with no keyed row); the four rows, one commit each, go to B21 (owed to A14, A15). (5) H-145 with NM-W9 (b): the intake's `settled:` says "register row governs (E7:30)", so the item is E7's (`EventLog.append` refuses a bare `StateChange`), not E2's reading ("a closure write emits its receipt with before ≠ after"); NM-W9's `Receipt.before/after` half is `16_PESSIMIST_CORE_the_record_holds_what_changed` edit 1 (B09.10). (6) H-135's two fix shapes ("judge closure writes for F9 or skip the write when `wear` is 0"): B09.21 takes the narrower (skip the zero-wear write in MATTER's clock writer); judging every closure write is the other. (7) `02_CHAR_reason_trail_and_small_edits` Part C's two `requirements.yaml` `measured:` head rewrites (R-06, R-08) are dead edits after B02.13 (`measured:` leaves; readings sit on conjuncts) and are not carried. (8) `16_PESSIMIST_GO_a_witness…`: "raising the chance is its own commit and re-pin" names no batch; B98 sets it (D-22). (9) IN-58 has no carrier in v12 (B09.20, BLOCKED). (D4) Lane D4 (CLAUDE.md §0 ladder, step 5 with step 4): IN-58's carrier is not owed to another batch: B09.22 makes the seat Subject of a death carry one Observation naming the closed holder, on CP-T03-02's existing `Subject.observed` channel (`state/gate.py`: "no new channel"), which adds no Claim, Event or World field (`Subject.seat`'s own carrier rule); B09.20 is then its reader, shipped at control (`sworn_bond` 0, the entry's "ships OFF"). Execution order: B09.21 → B09.22 → B09.20 → B09.99. The rejected carriers: a pairing field on `Claim` (a hashed carrier's shape change) and reading a shared `when`/`lap` as a pairing (`deed_doer` refuses to guess). B32.07's `prior_holders` premise ("a `tenure.closed` claim's subject names both person and seat", `[UNVERIFIED]` there) can read the same claim; B32 is not edited here.
C(B09-memory): this batch's entries; the plan's head parts; `unified/U1_GLOSSARY.md` rows *occasion*, *refusal*, *sworn*;
  `engine/season/state/ledgers.py`; `engine/season/state/world.py` (`write`, `content_hash`, `last_emission_of`); `engine/season/state/log.py` (`EventLog.append`); `engine/season/state/acts.py` (`ActStore`); `engine/season/state/carriers.py` (`subject_of`, `Scene`, `Claim`); `engine/season/state/gate.py` (`Subject.entity`); `engine/season/loop/matter.py`; `engine/season/loop/resolve.py` (`resolve`, `_occasion_ids`, `_occasion_of`, `_scar_witnesses`, `_admits`); `engine/season/loop/deliberate.py`; `engine/season/loop/driver.py` (`SeasonDriver.scenes`); `engine/season/loop/witness.py`; `engine/season/loop/predicates.py`; `engine/season/epistemic.py` (`_term_why`, `seen_of`, `TERM_READERS`);
  `engine/season/queries/person_q.py` (`LedgerReader`, `said_of`, `lie_said_of`); `engine/season/queries/world_q.py` (`current_stage`, `reception`); `engine/season/decision/choose.py` (`score_terms`, `odds_weight`, `make_chooser`, `make_ranker`, `pack_scenes`); `engine/season/decision/options.py` (`teller_weight`, `ledger_weigh`, `opening_set`, `project`); `engine/season/decision/questions.py`; `engine/season/decision/sheet.py` (`chronicle`, `Chronicle`); `engine/season/seam/wrappers/sigma.py`; `engine/season/data/fixtures.py`; `engine/season/data/rosters.py`; `engine/season/data/verbs.py`; `engine/season/data/cast.py` (docstring);
  `engine/season/rosters.yaml` (`undeposited_kinds`, `observation_terms`, NEW `standing_occasion_opened_by`); `engine/season/verb_table.yaml`; `engine/season/write_matrix.yaml` (`(Claim, confidence)`); `engine/season/hole_register.yaml` (H-183, H-189, H-237, H-145, H-135, H-111, the three new rows); `engine/season/requirements.yaml` (R-08 `disposition:`); `CURRENT.md` (character-model row); `proposals/2026-09-20-pursuit-basis-worksheet.yaml`; `references/restructure_ledger.md`;
  `engine/season/harness/decision_spread.py`, `interactions.py`, `aperture.py`, `chronicle.py`, `probes.py` (`about`), `report.py`, `delta.py`, `headless.py`, `corpus_run.py` (read only);
  the tests named in the items; `engine/season/tests/_realm_goldens.py` (B02); the closing SHAs of B00, B01, B02, B05, B07 and the S9 merged head; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_IN.md`, the skill and `methodology-close`).
SERIAL EDGES: within the batch (U3 §1.2's B09 row, in its order): B09.01 (`present_confidence`) → B09.02 → B09.03 → B09.04 (`admission_weight` is the arm's reader, C3-Y10) → B09.05 (the shipped value is read with the arm); B09.01 → B09.06 → B09.07 → B09.08 (SC_B's own order: control, callers, flip); B09.09 → B09.10 (H-145 before the record proposal that names it, §5.6) → B09.11 (edit 1 with its tests, then edit 2) → B09.12 (U3: after the record proposal) → B09.13 → B09.14 (the test file) → B09.15; B09.13 → B09.16 (the chronicle line reads the hook) → B09.17 (`_term_why` reads `scene_of` for the actor's occasion); B09.18 → B09.19 (step one before step two); B09.01 → B09.21 (`loop/matter.py`: the ledger walk deleted before the clock writer is narrowed); B09.99 last. B09.20 has no edge (BLOCKED). Within-file order: `decision/choose.py` B09.03 → B09.13 → B09.14 → B09.15; `decision/sheet.py` B09.07 → B09.15 → B09.17; `epistemic.py` B09.16 → B09.17; `loop/resolve.py` B09.11 → B09.12 → B09.16 → B09.19; `data/fixtures.py` B09.03 → B09.04 → B09.05 → B09.06 → B09.08 → B09.12 → B09.17; `rosters.yaml` B09.04 → B09.12 → B09.17; `hole_register.yaml` B09.03 → B09.05 → B09.06 → B09.08 → B09.09 → B09.12 → B09.15 → B09.17 → B09.21.
  With other batches, by file (U3 §5.1's lists in v12 step order): `fixtures.py`, `rosters.yaml`, `verb_table.yaml` (B07, B17 at S9) → B09 → B10; `world_q.py`, `person_q.py`, `options.py`, `choose.py` B04/B05/B07 → B09 → B10; `matter.py` B03 → B09 → B12a–c; `resolve.py` B05 → B07 → B09 → B10 (B08 at S13, after); `epistemic.py` B09 → B11; `sheet.py` B04 → B09 → B10 → B34; `predicates.py` B04 → B09 → B21; `world.py` B03 → B06 → B09 → B12a–c; `driver.py` B03 → B09 → B12a–c → B28; `deliberate.py` B03 → B09 → B34 → B28; `write_matrix.yaml` B03 → B09 → B10; `requirements.yaml` B03 → B17 → B09 → B11; `hole_register.yaml` B17 → B09 → B10; `chronicle.py` B02 → B05 → B14 → B09 → B28. Serial instrument files (`V12_STRUCTURE_part3.md` §7.3): `loop/witness.py::_told_value` is not edited here (B09.04 edits the `finding.none` skip only).
PARALLEL: S10, alone (`V12_STRUCTURE.md` §2.3). It rebases on the S9 merged head (B07 and B17).
COST: small builds and edits; producer `valoria-author` on `sonnet`, `high`; `opus` reads the shipped `refusal_memory` (B09.05) and H-135's narrowing (B09.21); the close's terminal critique `opus`.
EST: 11 h [estimate: `V12_STRUCTURE.md` §2.4's per-commit formula over this batch's 23 positions (0.4 h × 23 + 2.5 h = 11.7 h; B09.22 added by lane D4); §2.2's 7 h counted members]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B09.01 | fading is computed where a claim is read | `01_CORE_claim_fade_as_read` edits 1–4 | BUILD | MOVER(behaviour) | Batch B02, Batch B07 |
| B09.02 | the reader of a refusal one remembers, and its five readings | `16_PESSIMIST_CORE_a_refusal_is_remembered` edit 1 | BUILD | EQUAL | B09.01 |
| B09.03 | the factor a remembered refusal puts on a candidate, at control | `16_PESSIMIST_CORE_a_refusal_is_remembered` edits 2–3 | BUILD | EQUAL | B09.02 |
| B09.04 | a failed search may be remembered by the one who searched, behind an arm | `U5a_DICE_owed_edits` §4 | BUILD | EQUAL | B09.03 |
| B09.05 | the shipped weight of a remembered refusal | `16_PESSIMIST_CORE_a_refusal_is_remembered` edit 3's shipped value | BUILD | MOVER(behaviour) | B09.03, B09.04 |
| B09.06 | one comparator weighs every belief, at control | `16_PESSIMIST_SC_B_one_reader_of_a_ledger` edits 1, 2, 6 | BUILD | EQUAL | B09.01 |
| B09.07 | what a person says, shows and plans by reads the one comparator | `16_PESSIMIST_SC_B_one_reader_of_a_ledger` edits 3–5 | BUILD | MOVER(behaviour) | B09.06 |
| B09.08 | the comparator weighs how sure the holder still is | `16_PESSIMIST_SC_B_one_reader_of_a_ledger` the flip | BUILD | MOVER(behaviour) | B09.07 |
| B09.09 | the log refuses a change no gate vouches for | H-145 with NM-W9 (b) (intake `:142`) | BUILD | EQUAL | Batch B02 |
| B09.10 | a receipt carries the value the gate saw | `16_PESSIMIST_CORE_the_record_holds_what_changed` edit 1 | BUILD | MOVER(behaviour) | B09.09 |
| B09.11 | a scar is recorded and witnessed by nobody | `16_PESSIMIST_CORE_the_record_holds_what_changed` edit 2 | BUILD | MOVER(behaviour) | B09.10 |
| B09.12 | an act on a standing occasion names the Event that opened it | `16_PESSIMIST_GAME_standing_occasions_carry_their_cause` | BUILD | MOVER(behaviour) | B09.11 |
| B09.13 | the chooser's observer hook; three harness wrappers deleted | `02_CHAR_reason_trail_and_small_edits` Part A (the hook) | BUILD | EQUAL | B09.12 |
| B09.14 | subjects packed by first appearance, not by name | `02_CHAR_reason_trail_and_small_edits` Part B row B2 | BUILD | EQUAL | B09.13 |
| B09.15 | superseded sentences corrected at their owners | `02_CHAR_reason_trail_and_small_edits` Part C | BUILD | EQUAL | B09.14 |
| B09.16 | the Scene is kept beside its acts | `01_CORE_reason_trail_in_the_act_store` | BUILD | EQUAL | B09.13 |
| B09.17 | a witness may connect what he holds, at control | `16_PESSIMIST_GO_a_witness_may_connect_what_he_holds` | BUILD | EQUAL | B09.16 |
| B09.18 | a predicate never raises and names the clause that refused | `01_CORE_predicates_name_their_clause` step one | BUILD | EQUAL | Batch B02 |
| B09.19 | the refused clause can reach the Event's kind (the channel) | `01_CORE_predicates_name_their_clause` step two, edit 4's mechanism | BUILD | EQUAL | B09.18 |
| B09.22 | a seat closed by a death names its holder (IN-58's carrier, lane D4) | v11 IN-58 NARROWED; CP-T03-02's `Subject.observed` | BUILD | MOVER(behaviour) | B09.21 |
| B09.20 | the sworn-to half of grievance at read | IN-58 (intake `:143`) | BUILD (at control; lane D4) | EQUAL | B09.22 |
| B09.21 | a zero-wear clock write is not written | H-135 (intake `:144`) | BUILD | MOVER(behaviour) | B09.01 |
| B09.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | B09.01 to B09.22 |

Not in this batch, and where each is: `U5c_VERBS_residue_and_governance_owner` §3 (B11, UNDECIDED (3)); `01_CORE_predicates_name_their_clause` step two's four keyed rows (B21, UNDECIDED (4)); `01_CORE_claim_fade_as_read` edit 5 (held to B99, UNDECIDED (1)); `02_CHAR_reason_trail_and_small_edits` Part A's sheet `terms` (B34, with `person_q.explain`) and Part B row B1 (deleted, C3-L8; `U5a_CORE_owed_edits` §H in B03) and B3 (`02_CHAR_resolve_and_temper` edit 3, B10); `16_PESSIMIST_CORE_the_record_holds_what_changed`'s `conviction.moved` (`16_PESSIMIST_CHAR_A`, B10); the refusal-by-a-person half of A-81 (`30_WR_D_momentum_and_its_brakes` §3, B38).

### B09.01 — fading is computed where a claim is read · 01_CORE_claim_fade_as_read edits 1–4 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/01_CORE_claim_fade_as_read.md` "Edits, by owner" 1–4, "Gate", "Falsifier"; D-48 (Option A); `04` §B.13 invariant 7, §A.2; closes F-CORE-01 (resolution 1).
- ADVANCES: re-read R-07.a (memory that weakens) unchanged; the log stops growing by fades.
- INSTRUCTION (copied):
  1. "`engine/season/state/ledgers.py` (the owner of the eviction comparator; the confidence reader joins it). New function, the single owner of the rule:
     ```python
     def present_confidence(confidence: int, when: int, tick: int, decay: int) -> int:
         """A claim's confidence at `tick`: what was deposited, less `decay` per season elapsed."""
         return max(0, confidence - decay * max(0, tick - when))
     ```
     `[ASSUMPTION; medium]` This reproduces today's schedule exactly for a claim that has a deposit Event and has faded once per season since. Today a claim with no deposit Event is skipped … and so never fades; under this edit it fades. That difference is intended and is the one behavioural change beyond the log."
  2. "**Every reader of `Claim.confidence`** routes through it (§0.1 pt 1: grep the field's readers and its assignments)." Known sites, by symbol: `state/ledgers.py::eviction_key`'s caller; `queries/person_q.py` (`LedgerReader._best` and the reader's other confidence reads); `loop/deliberate.py` (the inputs fingerprint); `seam/wrappers/sigma.py`; `queries/world_q.py::reception`; `loop/witness.py` (two sites); `decision/options.py`; `decision/questions.py`; `state/ledgers.py` (two sites). "The reader needs `tick` and the fixture `claim_decay`; `LedgerReader` is constructed with both." "The `decision/` readers read through the ledger reader the person is handed (constructed with `tick` and `claim_decay`), never `World`; the executing session re-runs the grep before the edit and routes every site found": `grep -rn "\.confidence\b" --include=*.py engine/season` (non-test, non-harness), its list in the commit body.
  3. "`engine/season/loop/matter.py`: the per-claim write is deleted and nothing replaces it: MATTER stops walking ledgers … No Event marks a claim reaching zero: 'it reached zero' is a function of `present_confidence`, and a reader that wants the moment calls it at two ticks." (Today the walk calls `World.write(… record_kind="Claim", fieldname="confidence", emits="claim.decayed")` per live claim.)
  4. "`engine/season/write_matrix.yaml`, row `(Claim, confidence)`: remove `MAT` from `steps:` and `claim.decayed` from `emits:`. No new kind."
- WHERE: `engine/season/state/ledgers.py` (`present_confidence`); `engine/season/queries/person_q.py` (`LedgerReader`); `engine/season/queries/world_q.py` (`reception`); `engine/season/loop/deliberate.py`; `engine/season/loop/witness.py`; `engine/season/loop/matter.py` (the ledger walk); `engine/season/seam/wrappers/sigma.py`; `engine/season/decision/options.py`; `engine/season/decision/questions.py`; `engine/season/write_matrix.yaml` (`(Claim, confidence)`); NEW `engine/season/tests/test_claim_fade_as_read.py`.
- TESTS (the scratch `probe_growth.py` restated, written before the edit, read red): `test_present_confidence_matches_the_schedule_of_the_old_write` ("a hand-built ledger, ticks 0 to 7, `==` against the old write's values for a claim with a deposit Event"); `test_no_claim_decayed_in_a_two_season_log` (headless, seeds 0, 1, 2, two seasons; "eight seasons" in the source, A-114); `test_season_one_log_holds_no_fade_events` (season 1's new log entries hold no `claim.decayed`, and their count equals the before-reading's season-1 count less its `claim.decayed` count within the act changes the fade causes, `reading @<sha>` quoted in the commit body; the source's `test_log_growth_per_season_is_flat` over eight seasons is B99's reading, A-114) `[ASSUMPTION: test name; the item creates it]`. "Two runs at one seed give one hash."
- FALSIFIER and CONTROL: "A person's choices change. Control: run the present tree and the edited tree at seed 0 for four seasons [two, A-114] with `claim_decay` swept to 0 (no fading in either); the act multiset must be identical. With fading on, the act multisets must also be identical for every claim that had a deposit Event; a difference is the proposal read wrong, except where assumption 1 names it."
- GATE: `python -m pytest engine/season/tests/test_claim_fade_as_read.py -q` → pass; the control above (two seasons, `claim_decay_per_season` 0) → act multisets identical, quoted; the realm content hash (`HASH READING`) at seed 0, two seasons → moved (fewer Events; `Claim.confidence` holds the deposited value), recorded for B09.99.
- HASH MOVERS: "Every world (fewer Events; `Claim.confidence` holds the deposited value)". Declared; B09's one re-pin in B09.99.
- DEPENDS ON: EXISTS-IN-TREE `state/ledgers.py::eviction_key`, `queries/person_q.py::LedgerReader`, `data/fixtures.py::Fixtures.claim_decay` (`claim_decay_per_season`), the MATTER ledger walk, `write_matrix.yaml` row `(Claim, confidence)`; V12 Batch B02 (`01_CORE_tests_one_golden_owner`: one pin file).
- GLOSSARY: none (fading is not a new word; no row names `claim.decayed`).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B09's `valoria-author` producer, `isolation: worktree`; `Item: B09.01`, `[skip ci]`.

### B09.02 — the reader of a refusal one remembers, and its five readings · 16_PESSIMIST_CORE_a_refusal_is_remembered edit 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_CORE_a_refusal_is_remembered.md` "Exact edits" 1, "Gate" ("The batch's first commit writes"); A-81 (1), A-62, D-46; `04` §B.2 (own-ledger carve-out); closes F-PES-CORE-01 (with B09.03, B09.05).
- ADVANCES: re-read R-07.a unchanged; R-08's "not perfectly rational" gains a memory of failure (no conjunct moves).
- INSTRUCTION:
  1. "`engine/season/queries/person_q.py` (the single owner of ledger reads) — new reader:
     ```python
     def refused_before(p: Person, kinds: tuple, subject: str) -> int:
         """The present confidence (0..confidence_default) of the NEWEST firsthand claim in `p.ledger`
         in which `p` was himself refused this opportunity -- predicate in `kinds` (the verb row's
         `emits_on_refusal`), subject `subject`, `doer == p.id` -- or 0 when there is none, or when
         he holds ANY newer claim about `subject` (news of the subject supersedes the memory: the
         thing may have changed). Confidence is read through `state/ledgers.py::present_confidence`
         (`01_CORE_claim_fade_as_read.md`, one owner of fading), never the stored deposit value."""
     ```
     Own ledger only (AX-2; `04` §B.2, the own-ledger carve-out): the reader takes the `Person` … No World. 'Newer' compares `(when, round)`, the pair `questions_for`'s `since` already uses" — after B04 the pair is `(when, lap)`.
  2. The committed form of the five readings: "a `--retries` mode of `harness/decision_spread.py` (it already plays seasons and imports `score_terms`; `[ASSUMPTION: the nearest existing instrument — basis: harness/ listing and its module docstring]`), printing the five rows for `--seed 0`" over two seasons ("three" in the source; A-114): (a) the control arm's content hash; (b) refused opportunities attempted again, world-only and unobserved classes; (c) individuals' refusal share of acts, season 1 against season 0; (d) `(actor, verb)` pairs attempted three or more times and refused every time; (e) retries that succeed. Definition of (c) as the source states it: acts by individuals, not cohorts, refused at the fold, over all acts by individuals (C3-N13).
- WHERE: `engine/season/queries/person_q.py` (`refused_before`); `engine/season/harness/decision_spread.py` (`--retries`); NEW `engine/season/tests/test_refusal_memory.py`.
- TESTS (the batch's first commit writes the file, `python -m pytest engine/season/tests/test_refusal_memory.py -q`): `test_newer_claim_about_subject_supersedes_the_memory`, `test_reader_takes_the_person_not_a_ledger` ("a planted second person's ledger cannot be passed") green here; `test_control_value_zero_leaves_hash_equal`, `test_factor_never_reaches_zero_below_one`, `test_unwired_verb_has_factor_one` red until B09.03.
- EXPECTED RED UNTIL: B09.03 for the three tests named (under `[skip ci]`).
- FALSIFIER and CONTROL: a memory read from another person's ledger, or a claim older than news of its subject that still counts. Control: the realm content hash at seed 0, two seasons, equal to B09.01's (the reader has no caller).
- GATE: the two green tests above; `python -m engine.season.harness.decision_spread --retries --seed 0 --seasons 2` → five rows printed, recorded in the commit body as the before-reading (`reading @<sha>`).
- HASH MOVERS: none.
- DEPENDS ON: V12 B09.01 (`present_confidence`); EXISTS-IN-TREE `queries/person_q.py`, `harness/decision_spread.py` (`play_season`), the verb rows' `emits_on_refusal`.
- GLOSSARY: none.
- NAMES: `(when, round)` → `(when, lap)` (B04, PCR-4).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.02`, `[skip ci]`.

### B09.03 — the factor a remembered refusal puts on a candidate, at control · 16_PESSIMIST_CORE_a_refusal_is_remembered edits 2–3 · BUILD · HASH EQUAL
- SOURCE: the same file, "Exact edits" 2, 3 (at the control), 4; "Cost class" ("order of edits 1 → 2 → 3 … the fixture last at the control, then the shipped value in its own commit").
- ADVANCES: as B09.02.
- INSTRUCTION (copied):
  1. "`engine/season/decision/choose.py` — beside `odds_weight`, same shape:
     ```python
     def admission_weight(p: Person, c: Candidate, fx: "Fixtures") -> float:
         """THE FACTOR A REMEMBERED REFUSAL PUTS ON A CANDIDATE'S PURSUIT TERM:
         1 - refusal_memory * refused_before(...) / confidence_default. 1.0 at `refusal_memory` 0.0
         (CONTROL), for a verb whose row declares no refusal kind, and where nothing is remembered."""
     ```
     and in `score_terms`, after the existing `pursuit *= odds_weight(p, c, fx, odds)` line: `pursuit *= admission_weight(p, c, fx)`. `score_terms` stays the one owner of the formula."
  2. "`engine/season/data/fixtures.py` — `refusal_memory=<value>`, with a `[JUSTIFIED: … H-nnn]` line and a hole-register row graded `assumption`, swept `0.0 / 0.5 / 1.0`", landed here at the control `0.0`. The row is a `HOLE` row in `engine/season/hole_register.yaml`, its id B09's H block slot 1 (B00; not `next_free`, which holds no H key).
  3. "Nothing in `loop/`. `_drop_what_was_already_done` keeps its rule; a refused act is still retryable and is now retried at lower odds."
- WHERE: `engine/season/decision/choose.py` (`admission_weight`, `score_terms`); `engine/season/data/fixtures.py` (`refusal_memory`); `engine/season/hole_register.yaml` (one new row).
- TESTS: the three red tests of B09.02 turn green.
- FALSIFIER and CONTROL: the factor below 1.0 at `refusal_memory` 0.0. Control: "`python -m engine.season.harness.report && python -m engine.season.harness.delta HEAD` at `refusal_memory = 0.0`, expected `PROBE FLIPS 0`"; the realm hash at seed 0, two seasons, equal to B09.02's.
- GATE: `python -m pytest engine/season/tests/test_refusal_memory.py -q` → five pass; `report` then `delta HEAD` → `PROBE FLIPS 0`; `python tools/ci_sim_fabrication_check.py` → exit 0 (the new fixture's tag); `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`) (the new row).
- HASH MOVERS: none at the control.
- DEPENDS ON: V12 B09.02; EXISTS-IN-TREE `decision/choose.py::odds_weight`, `::score_terms`, `confidence_default`.
- GLOSSARY: none.
- IDS: H block slot 1.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.03`, `[skip ci]`.

### B09.04 — a failed search may be remembered by the one who searched, behind an arm · U5a_DICE_owed_edits §4 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5a_DICE_owed_edits.md` §4 (F-PES-DICE-05); C3-Y10 (co-lands with the refusal reader); U3 §4.1 rows 23–24.
- ADVANCES: none of the nine; "the search the memory its own row said it lacked".
- INSTRUCTION (copied): "**Edit, owner `engine/season/rosters.yaml: undeposited_kinds` and `loop/witness.py`.** The roster's row for `finding.none` becomes actor-only: the Event deposits to its own doer (the `witness_key` channel's rule, *change claims about self*) and to nobody else. This is the narrower skip the roster's own note names (H-111, *Jordan to correct*). Behind a fixture arm (`finding_none_deposit: none | actor`; control `none`). No other reader is added: `admission_weight` then discounts a search he remembers failing, until the claim fades or news of the subject lands." The fixture's `[JUSTIFIED: …]` line cites H-111; the arm ships `none`.
- WHERE: `engine/season/rosters.yaml` (`undeposited_kinds`); `engine/season/loop/witness.py` (the `finding.none` skip); `engine/season/data/fixtures.py` (`finding_none_deposit`); `engine/season/tests/test_refusal_memory.py`.
- TESTS: `engine/season/tests/test_refusal_memory.py::test_finding_none_deposits_to_its_actor_only_at_the_actor_arm` `[ASSUMPTION: test name; the item creates it]` (a planted failed inquiry: the actor holds the claim at `actor`, nobody at `none`; no non-actor holds it at either arm).
- FALSIFIER and CONTROL: "The retry share is unchanged with both edits in" (read at B09.05). Control: at `none` (shipped) the realm hash at seed 0, two seasons, equal to B09.03's.
- GATE: the test above → pass; the hash control → equal; the arm's reading ("Seeds 0–2, two seasons, both arms: failed inquiry aims tried again fall at the `actor` arm with `refusal_memory` above 0, and do not fall at `refusal_memory` 0 … deposits to non-actors equal across arms") is moved to B09.05's GATE (it needs `refusal_memory` above 0, §5.8).
- HASH MOVERS: none as shipped; "the `actor` arm" when set (B98).
- DEPENDS ON: V12 B09.03 (`admission_weight`), B09.01 (`present_confidence`); EXISTS-IN-TREE `rosters.yaml: undeposited_kinds` (`values: ["finding.none"]`), H-111.
- GLOSSARY: none.
- COST and TIER: edit behind an arm; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.04`, `[skip ci]`.

### B09.05 — the shipped weight of a remembered refusal · 16_PESSIMIST_CORE_a_refusal_is_remembered edit 3's shipped value · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, "Exact edits" 3 ("**Proposed shipped value 0.5** `[ASSUMPTION; medium; Jordan to correct; revert: 0.0, the control]`: half the pursuit weight is withheld immediately after a refusal and returns as the claim fades at `claim_decay_per_season`"), "Gate", "Falsifier"; D-19 (an authored value, ratified at the batch's merge).
- ADVANCES: re-read R-07.a; the refused stop retrying blindly.
- INSTRUCTION: `engine/season/data/fixtures.py`: `refusal_memory` `0.0` → `0.5`, in its own commit, the `[JUSTIFIED: …]` line and the HOLE row's `default:` naming the shipped value as an assumption for Jordan (revert `0.0`). Read the five readings and U5a §4's arm reading, both at two seasons ("three" in the source; A-114).
- WHERE: `engine/season/data/fixtures.py` (`refusal_memory`); `engine/season/hole_register.yaml` (slot 1's `default:`).
- TESTS: none new.
- FALSIFIER and CONTROL: "The retry rate of the unteachable classes does not move at `refusal_memory = 1.0`. That would mean the re-formed Candidates are not pursuit-priced …, and the factor belongs on the sum; say so and move it." Control: `refusal_memory = 0.0` reproduces B09.04's hash.
- GATE: `python -m engine.season.harness.decision_spread --retries --seed 0 --seasons 2` against B09.02's before-reading, "passes when": (a) control `0.0` hash equal; (b) refused opportunities attempted again, world-only and unobserved classes: "at or below the executed-act control (about 20%)"; (c) season 1's refusal share "not rising" against season 0; (d) "fewer than half" of the before-reading's pairs; (e) retries that succeed "not lower". One run at `1.0` for the falsifier. U5a §4's arm, seeds 0–2, two seasons: at `finding_none_deposit: actor` failed inquiry aims tried again fall against `none`, and do not fall at `refusal_memory` 0; deposits to non-actors equal across arms. A reading that misses is written in the commit body and the shipped value is not changed by the producer (an `opus` read of the readings decides keep or revert to `0.0`, and the PR body names it for Jordan).
- HASH MOVERS: "every seeded result at any shipped value (one re-pin in B09)". Declared; B09.99.
- DEPENDS ON: V12 B09.03, B09.04.
- GLOSSARY: none.
- COST and TIER: calibration (a value flip and its readings); `sonnet` runs; "the shipped value 0.5 is an `opus`-or-Jordan judgment" — `opus` reads.
- LANDS IT: B09's producer; `Item: B09.05`, `[skip ci]`.

### B09.06 — one comparator weighs every belief, at control · 16_PESSIMIST_SC_B_one_reader_of_a_ledger edits 1, 2, 6 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_SC_B_one_reader_of_a_ledger.md` "The resolution, decided", "Exact edits" 1, 2, 6, "Gate", "Cost class" ("order 1 → 2 (with the control at `False`, hash-equal) → 3 → 4 → 5 → the flip to `True`"); D-48; closes F-PES-SC-01 (with B09.07, B09.08).
- ADVANCES: re-read R-07.a; R-08's one definition of what a person believes (no conjunct moves).
- INSTRUCTION (copied). The rule:
  ```
  weigh(c) = (present_confidence(c) / confidence_default) × ( 1.0                              if c.chain is empty
                                                              told_weight^hops × relation × record   otherwise )
  ```
  1. "`engine/season/decision/options.py::teller_weight` — `weigh(c)` multiplies its result by `present_confidence(c) / fx.get("confidence_default")` for every claim, told or not (the empty-chain branch returns that share instead of `1.0`). Control: a fixture `weigh_confidence` (bool, shipped `True`, swept `False`), read once per closure; at `False` the function is today's, exactly." Landed here at `False` (B09.08 flips it).
  2. "`engine/season/decision/options.py::ledger_weigh` — returns the closure whenever the ledger holds *any* claim below full confidence or any told claim (today: any told claim), so a ledger of fresh firsthand claims still takes the plain reader and reads as before" — at `weigh_confidence: False` it returns today's condition.
  3. "**Hole register**: the row that carries `H-183` gains this proposal's control; no new row (`weigh_confidence` is a switch on an existing magnitude, `claim_decay_per_season`)." The fixture's `[JUSTIFIED: …]` line cites H-183.
- WHERE: `engine/season/decision/options.py` (`teller_weight`, `ledger_weigh`); `engine/season/data/fixtures.py` (`weigh_confidence`); `engine/season/hole_register.yaml` (H-183); NEW `engine/season/tests/test_one_reader_of_a_ledger.py`.
- TESTS (written first): `test_weigh_confidence_false_reproduces_today` (green here); `test_said_of_sheet_and_belief_contradicts_agree_on_every_cell`, `test_stale_sighting_falls_to_enough_tellers`, `test_fresh_sighting_holds_against_one_teller` (red until B09.08).
- EXPECTED RED UNTIL: B09.08 for the three tests named.
- FALSIFIER and CONTROL: at `False`, any weight that differs from today's. Control: the realm content hash at seed 0, two seasons, equal to B09.05's.
- GATE: `python -m pytest engine/season/tests/test_one_reader_of_a_ledger.py -k weigh_confidence_false -q` → pass; the hash control → equal; `python tools/ci_sim_fabrication_check.py` → exit 0.
- HASH MOVERS: none at the control.
- DEPENDS ON: V12 B09.01 (`present_confidence`); EXISTS-IN-TREE `decision/options.py::teller_weight`, `::ledger_weigh`, `queries/person_q.py::LedgerReader` (`weigh`), `epistemic.belief_contradicts`, H-183.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.06`, `[skip ci]`.

### B09.07 — what a person says, shows and plans by reads the one comparator · 16_PESSIMIST_SC_B_one_reader_of_a_ledger edits 3–5 · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, "Exact edits" 3–5 (grouped: one gate, the three call sites, `V12_STRUCTURE_part4.md` E-13).
- ADVANCES: as B09.06.
- INSTRUCTION (copied):
  1. "`engine/season/queries/person_q.py::said_of` and `::lie_said_of` — a keyword `weigh=None`, handed to `LedgerReader(pool, weigh)`. Caller: `decision/options.py::opening_set` passes `weigh=ledger_weigh(p, fx)` at the one call site (`said_of_entity[entity] = …`). `person_q` imports nothing from `decision/` (the closure is an argument, as it is for `LedgerReader`)." "⚠ `_support` under a `weigh` ranks `latest_about` across predicates … Decided here: accepted. A person passes on what he is surest of about a subject, not the newest thing he holds."
  2. "`engine/season/decision/sheet.py::chronicle` — signature `chronicle(p, fx=None)`; `reader = LedgerReader(p.ledger, ledger_weigh(p, fx) if fx is not None else None)`; its callers in `decision/sheet.py` and the harness pass the fixtures they already hold."
  3. "`engine/season/queries/world_q.py`" (the stage reader, `current_stage`) "— take the closure as a parameter from its one caller, as its docstring's revert line says."
- WHERE: `engine/season/queries/person_q.py` (`said_of`, `lie_said_of`); `engine/season/decision/options.py` (`opening_set`); `engine/season/decision/sheet.py` (`chronicle` and its callers); `engine/season/queries/world_q.py` (`current_stage` and its caller); the harness callers of `chronicle`.
- TESTS: none new (B09.06's file).
- FALSIFIER and CONTROL: "Any (holder, cell) in a seeded realm season for which `said_of`'s value, the sheet's value and `belief_contradicts`' value differ." Control: "`weigh_confidence=False` reproduces today's weighed column, and the three re-pointed callers then agree with it."
- GATE: `python -m pytest engine/season/tests/test_one_reader_of_a_ledger.py -k "weigh_confidence_false" -q` → pass; then `python -m engine.season.harness.report && python -m engine.season.harness.delta HEAD` → the declared move, quoted.
- HASH MOVERS: "every world where a person holds two values for one cell from different sources". Declared; B09.99.
- DEPENDS ON: V12 B09.06; EXISTS-IN-TREE `person_q.said_of`, `lie_said_of`, `decision/options.py::opening_set`, `decision/sheet.py::chronicle`, `world_q.current_stage`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.07`, `[skip ci]`.

### B09.08 — the comparator weighs how sure the holder still is · 16_PESSIMIST_SC_B_one_reader_of_a_ledger the flip · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, "Exact edits" 1 ("shipped `True`"), "Gate", "Cost class" ("→ the flip to `True`").
- ADVANCES: as B09.06.
- INSTRUCTION: `engine/season/data/fixtures.py`: `weigh_confidence` `False` → `True`, in its own commit; H-183's row names the shipped value.
- WHERE: `engine/season/data/fixtures.py` (`weigh_confidence`); `engine/season/hole_register.yaml` (H-183).
- TESTS: B09.06's three red tests turn green.
- FALSIFIER and CONTROL: as B09.07. Control: `False` reproduces B09.07's hash.
- GATE: `python -m pytest engine/season/tests/test_one_reader_of_a_ledger.py -q` → four pass. The scratch readings, committed as the tests: "the two columns are equal on every row (32 / 32 and 27 / 27 for the knowing hearer)"; "at `c0 = 80` the sighting holds against one teller and falls to a number of tellers the run prints; at `c0 = 5` it falls to one" (the number printed in the commit body).
- HASH MOVERS: as B09.07; declared; B09.99.
- DEPENDS ON: V12 B09.07.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.08`, `[skip ci]`.

### B09.09 — the log refuses a change no gate vouches for · H-145 with NM-W9 (b) · BUILD · HASH EQUAL
- SOURCE: the intake `:142` (H-145, NM-W9; `settled:` "register row governs (E7:30 STILL-NEEDED)"); its carry-forward `master/eval/E7.md` "H-145 (STILL-NEEDED) lane IN, batch B09-memory (one item with v11 NM-W9)"; `engine/season/hole_register.yaml` H-145; `master/eval/E1.md` NM-W block (v11 `_part4.md:292-307`, NM-W9 "conformance items"); `unified/U5_FINDINGS_CLOSURE_U5a.md` F-CORE-11. Placed by `V12_STRUCTURE_part2.md` §5.6 rule 1: immediately before the first item whose source names H-145 (`16_PESSIMIST_CORE_the_record_holds_what_changed`, "which is H-145 (F-CORE-11) and stays that row's").
- ADVANCES: none of the nine; one provenance check at the log.
- INSTRUCTION (E7's, copied): "tighten `EventLog.append` (`state/log.py`) to refuse a bare `StateChange`; first make `harness/probes.py::about` stop building one; then flip the pinned test." OWNER (verbatim): "state/log.py -- the append-time check that only inspects `Receipt`-typed changes; harness/probes.py::about -- the one production-adjacent source of a bare `StateChange` (probe-only; G1b closed the production sources)". The second `StateChange(` construction in `harness/probes.py` (the `alter` of a Site's `condition`) is converted with `about`. H-145's row is closed in the same commit (its `default:` and `hole:` kept as history; the closing line names this item).
- WHERE: `engine/season/state/log.py` (`EventLog.append`); `engine/season/harness/probes.py` (`about`, the second `StateChange(` site); `engine/season/tests/test_g1a_act_store_and_receipts.py` (the pinned test); `engine/season/hole_register.yaml` (H-145).
- TESTS: `test_g1a_act_store_and_receipts.py`'s pinned falsifier "goes red as its own docstring says, then is re-pinned" (its assertion inverted: a bare `StateChange` is refused).
- FALSIFIER and CONTROL: a bare `StateChange` appended to the log. Control: the realm content hash at seed 0, two seasons, equal to B09.08's `[ASSUMPTION: HASH EQUAL — basis: E7's line "HASH: EQUAL [ASSUMPTION]"; G1b closed the production sources]`; if it moves, the commit body names the source and the item stops.
- GATE: `python -m pytest engine/season/tests/test_g1a_act_store_and_receipts.py -q` → pass after the re-pin of its falsifier; `git grep -n "StateChange(" -- engine/season ':!engine/season/tests'` → no construction outside `harness/probes.py`'s converted sites and the `state/carriers.py` comments; the hash control → equal.
- HASH MOVERS: none `[ASSUMPTION]` (above).
- DEPENDS ON: EXISTS-IN-TREE `state/log.py::EventLog.append`, `harness/probes.py::about`, `test_g1a_act_store_and_receipts.py`; V12 Batch B02.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet` (E7's tier).
- LANDS IT: B09's producer; `Item: B09.09`, `[skip ci]`.

### B09.10 — a receipt carries the value the gate saw · 16_PESSIMIST_CORE_the_record_holds_what_changed edit 1 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/16_PESSIMIST_CORE_the_record_holds_what_changed.md` "Exact edits" 1, 3 (its tests), "Gate"; `04` §C.2; closes F-PES-CORE-02; NM-W9's `Receipt.before/after` half.
- ADVANCES: none of the nine; the record says how much a write moved.
- INSTRUCTION (copied, line numbers dropped): "`engine/season/state/world.py::World.write`, the `Change` branch:
  - keep the pair instead of the subject: `moved = [(s, b, a) for s, b in zip(change.subjects, was) for a in (… self.state_of(s) …,) if … a != b]` (edge subjects keep their tenure-diff test; their `delta` stays `None`: the Tenure is its own record).
  - `self.gate.mint(s.id, "set", driver, fieldname, _delta(s, b, a))`, where `_delta` returns `(b, a)` when `s` names `fields`, and `None` for a whole-entity digest subject. For that case set `mode` honestly instead: `"create"` when `b == (False,)`, `"delete"` when `a == (False,)`, else `"set"`.
  - The closure branch (`apply=`) is untouched: it has no observed value, which is H-145 (F-CORE-11) and stays that row's." (B09.09 carried H-145's own fix.)
- WHERE: `engine/season/state/world.py` (`World.write`'s `Change` branch, `_delta`); `engine/season/tests/test_g1a_act_store_and_receipts.py`.
- TESTS (edit 1 with its tests): `test_g1a_act_store_and_receipts.py::test_receipt_delta_decodes_before_after_for_fields_subject` ("the planted 940 → 1000 case"), `::test_every_minted_receipt_is_in_an_event` (red until B09.11).
- EXPECTED RED UNTIL: B09.11 for `test_every_minted_receipt_is_in_an_event`.
- FALSIFIER and CONTROL: a fields-naming `Change` receipt with `delta is None`. Control: acts and per-act outcomes at seed 0, two seasons, identical to B09.09's (only the hash moves).
- GATE: `python -m pytest engine/season/tests/test_g1a_act_store_and_receipts.py -k delta_decodes -q` → pass; "a planted `Change` raising one cohort's `body` 940 → 1000: receipt's `delta` decodes to `(940, 1000)`".
- HASH MOVERS: every content hash (`content_hash` folds `Receipt.delta`, an existing field of a hashed record (`state/carriers.py::Receipt`) now filled). Declared `MOVER(behaviour)`: D-04's encoding class is a field or class added, removed or renamed, and no field is (repair lane R2a, K2 #9); the control stays as written (acts and per-act outcomes equal, only the hash moves). Re-pinned in B09.99.
- DEPENDS ON: V12 B09.09; EXISTS-IN-TREE `World.write`, `World.state_of`, `gate.mint`, `Receipt.delta`, `.mode`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.10`, `[skip ci]`.

### B09.11 — a scar is recorded and witnessed by nobody · 16_PESSIMIST_CORE_the_record_holds_what_changed edit 2 · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, "Exact edits" 2, 3, "Gate", "Falsifier"; A-24 (scar only; `conviction.moved` is `16_PESSIMIST_CHAR_A`'s, B10); C3-Y8; closes F-PES-CORE-03.
- ADVANCES: none of the nine; the interior writes reach the log.
- INSTRUCTION (copied): "`engine/season/loop/resolve.py::_scar_witnesses` (its `w.write` call): add `emits="scar.taken"`, `causes=[a.id]` to the existing `w.write`, with each `Subject.entity(…, earns="scar.taken")` (`state/gate.py`) so the gate's `extra` path … puts the per-person receipts on one Event. Any `subject=` argument the write path takes feeds the **receipt's** subject id only: an `Event` has no `actor`, `target` or `subject` field (`04` §B.9, STRUCTURAL), and the persons scarred are named only by the receipts in `changes[]`. If the gate's single-kind `emits` path would mint a second, redundant receipt, emit through `extra` alone; the implementer picks the form that yields exactly one Event per write carrying exactly the minted receipts. Delete the docstring paragraph that says nothing is emitted. `_conviction_crisis` is **not** edited here." "*Why WITNESS does not fan these out.* … the code reads RESOLVE's returned list …, as `claim.deposited` relies on … the code reading is kept, named here, and the deposit count below is the observer; `04` is not cited as the reason and is not edited."
- WHERE: `engine/season/loop/resolve.py` (`_scar_witnesses`); `engine/season/tests/test_g4_no_op_receipt.py`.
- TESTS: `test_g4_no_op_receipt.py::test_scar_taken_event_deposits_no_claim`, `::test_gate_emitted_event_names_persons_only_in_changes`; B09.10's `test_every_minted_receipt_is_in_an_event` turns green.
- FALSIFIER and CONTROL: "Deposits per season change. Then a gate-emitted Event in RESOLVE does reach WITNESS by a path this proposal did not see, the stated objection was right, and edit 2 is withdrawn (edit 1 stands alone)." Control: claims deposited per season at seed 0 equal to B09.10's (two seasons).
- GATE: `python -m pytest engine/season/tests/test_g1a_act_store_and_receipts.py engine/season/tests/test_g4_no_op_receipt.py -q` → the four named tests pass; on `build_realm(0)`, two seasons: receipts minted and carried by no Event → 0; "`scar.taken` Events / `Person.scar` write calls" → equal; claims deposited per season → unchanged; acts and per-act outcomes → identical.
- HASH MOVERS: the log gains `scar.taken` Events. Declared; B09.99.
- DEPENDS ON: V12 B09.10; EXISTS-IN-TREE `loop/resolve.py::_scar_witnesses`, `state/gate.py::Subject.entity` (`earns`), `write_matrix.yaml` `(Person, scar)` `emits: scar.taken`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.11`, `[skip ci]`.

### B09.12 — an act on a standing occasion names the Event that opened it · 16_PESSIMIST_GAME_standing_occasions_carry_their_cause · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/16_PESSIMIST_GAME_standing_occasions_carry_their_cause.md` "Edits" 1–3, "Gate"; A-33, A-47; closes F-PES-GAME-03.
- ADVANCES: re-read R-01.b, .c (a consequence's cause is readable) unchanged as a conjunct; the chronicle can read a closing act's reason.
- INSTRUCTION (one commit: roster, branch, fixture, test; copied):
  1. `engine/season/rosters.yaml`, a new roster, appended at the end of its family's block:
     ```yaml
     # the Event kinds that OPEN a standing occasion of each referent class, most specific first
     standing_occasion_opened_by:
       Office:    [tenure.closed, office.established]
       Record:    [dispensation.issued, petition.filed, record.created]
       Person:    [body.changed]            # `wounded_with`
       Detainee:  [person.captured, arrest.made]
       Rung:      [stores.changed, rung.seized]
       Site:      [condition.band_crossed]
       Proposition: [proposition.uttered]
     ```
     "`[ASSUMPTION; medium; Jordan to correct]` the kind lists are this proposal's reading of each source's docstring; the loader (`data/rosters.py`) exposes it as `STANDING_OCCASION_OPENED_BY` and refuses a kind that is not an `emits` of some verb row or a MATTER/CALENDAR kind, by the check that already validates `strife_kinds`." A listed kind the loader refuses at this tree is removed from its list and named in the commit body.
  2. `engine/season/loop/resolve.py::_occasion_ids`, the one branch:
     ```python
         if (subj and subj not in getattr(occ, "referents", ())
                 and any(r == subj for r, _ in getattr(occ, "classes", ()))):
             if not w.fixtures.get("standing_occasion_cause"):          # control arm: today's `[]`
                 return []
             cls = next(c for r, c in occ.classes if r == subj)
             for kind in STANDING_OCCASION_OPENED_BY.get(cls, ()):
                 eid = w.last_emission_of(kind, subj, written=True)
                 if eid is not None and eid != a.id:
                     return [eid]
             return []
     ```
     "Resolver-side … One id at most, so `causes[]` does not fan."
  3. "`engine/season/data/fixtures.py` — `standing_occasion_cause`, graded `assumption`, shipped `True`. The control (`False`) reproduces every base hash." Its `[JUSTIFIED: …]` line and HOLE row: B09's H block slot 2.
- WHERE: `engine/season/rosters.yaml` (`standing_occasion_opened_by`); `engine/season/data/rosters.py` (`STANDING_OCCASION_OPENED_BY`, the loader check); `engine/season/loop/resolve.py` (`_occasion_ids`); `engine/season/data/fixtures.py` (`standing_occasion_cause`); `engine/season/hole_register.yaml` (one new row); `engine/season/tests/test_in53_vacancy_need.py`; `engine/season/tests/test_in50_refusals_carry_the_occasion.py`.
- TESTS (written before the edit, read red): in `test_in53_vacancy_need.py`, "build the governance spine, end the holder of a seat that `rosters.yaml: successions` names (the bodies hazard at 1 for that person …), run two seasons; assert a `succession.claimed` Event exists **and** that its `causes` contains the id of the `tenure.closed` Event naming that seat; assert the loop asserted (`checked >= 1`)", named `test_a_succession_names_the_tenure_closed_that_opened_it` `[ASSUMPTION: test name; the item creates it]`; `test_in50_refusals_carry_the_occasion.py` "gains the mirror assertion".
- FALSIFIER and CONTROL: "the test fails if the branch returns `[]` (today's code), and the control fails if the fixture is ignored." Control arm (`False`): "the same run, `causes == [act id]`, and the world hash equals the base hash."
- GATE: `python -m pytest engine/season/tests/test_in53_vacancy_need.py engine/season/tests/test_in50_refusals_carry_the_occasion.py -q` → pass; `rg -n "STANDING_OCCASION_OPENED_BY" engine` → the loader constant and `_occasion_ids`' read; the control at seed 0, two seasons → hash equal to B09.11's.
- HASH MOVERS: "every Event folded from an act on a classed referent (`causes` is hashed)". Declared; B09.99.
- DEPENDS ON: EXISTS-IN-TREE `World.last_emission_of`, `loop/resolve.py::_occasion_ids`, the `strife_kinds` loader check; V12 B09.11 (U3's order).
- GLOSSARY: row *occasion*: "the Event that opened a standing occasion is its **opening Event**" — the row's owner column gains `rosters.yaml: standing_occasion_opened_by` (P); "opening Event": the Event that began the situation an act answers, as a door's opening begins a visit.
- IDS: H block slot 2.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.12`, `[skip ci]`.

### B09.13 — the chooser's observer hook; three harness wrappers deleted · 02_CHAR_reason_trail_and_small_edits Part A (the hook) · BUILD · HASH EQUAL
- SOURCE: `proposals/02_CHAR_reason_trail_and_small_edits.md` Part A (the hook and the three harness repoints; the sheet `terms` are B34's), "Gate", "Falsifier"; the observer rule of `ED-IN-0225`; closes the CHAR audit §0A item (d).
- ADVANCES: none of the nine; one owner of "what the chooser saw".
- INSTRUCTION (copied): "`make_chooser` takes one more optional argument:
  ```python
  def make_chooser(fx, mint, verbs=None, draw=None, watch=None):
      # watch(p, q, ranked, terms, sampled) -> None, called once per deliberation after the order is
      # sampled and before it is packed. `ranked` is `score_order`'s list, `terms` the parallel
      # `score_terms` tuples, `sampled` `_sample_order`'s list. The chooser ignores its return value and
      # passes copies; a watcher that mutates changes nothing that is packed.
  ```
  - `harness/decision_spread.py`, `interactions.py` and `aperture.py` pass a `watch` and delete their wrappers and their second scoring (one owner of 'what the chooser saw')." `decision_spread.attribute_top`'s rule moves "beside `score_order` so the rule has one owner under `decision/`".
- WHERE: `engine/season/decision/choose.py` (`make_chooser`, the deciding-term rule beside `score_order`); `engine/season/harness/decision_spread.py` (`play_season`'s `watched`, `attribute_top`), `interactions.py`, `aperture.py`; NEW `engine/season/tests/test_choose_watch.py`.
- TESTS (new): `test_a_recording_watcher_leaves_the_hash_equal`, `test_a_reordering_watcher_changes_no_act`, `test_decision_spread_counts_equal_through_hook_and_wrapper`; "the existing `engine/season/tests/test_in62_decision_spread.py` stays green unedited".
- FALSIFIER and CONTROL: "A watcher that returns a reordered list changes no act: if the hash moves, the hook is a steering surface and is wrong." Control: `watch=None` and a recording `watch`: equal `content_hash` at seeds 0–2.
- GATE: `python -m pytest engine/season/tests/test_choose_watch.py engine/season/tests/test_in62_decision_spread.py engine/season/tests/test_g2_token.py -q` → pass; `decision_spread --decisions` at seed 0 → "the same deciding-term counts through the hook as through the wrapper" (the source's `223 draw, 265 pursuit, 10 stance` is `main`'s older reading; the before-reading is taken at this item's base, `reading @<sha>`).
- HASH MOVERS: none (control `watch=None`).
- DEPENDS ON: EXISTS-IN-TREE `decision/choose.py::make_chooser`, `score_order`, `score_terms`, `_sample_order`, `harness/decision_spread.py::attribute_top`; V12 B09.03 (`score_terms` now carries `admission_weight`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.13`, `[skip ci]`.

### B09.14 — subjects packed by first appearance, not by name · 02_CHAR_reason_trail_and_small_edits Part B row B2 · BUILD · HASH EQUAL
- SOURCE: the same file, Part B row B2 (ladder step 4: "U4 removed the alphabet as a tie-break for verbs; this is the same defect for subjects on an unshipped arm").
- ADVANCES: none of the nine.
- INSTRUCTION: "`pack_scenes`' `by_subject` arm orders subjects by first appearance in the ranked list, not `sorted(seen)`."
- WHERE: `engine/season/decision/choose.py` (`pack_scenes`, the `by_subject` arm); `engine/season/tests/test_choose_watch.py`.
- TESTS: "`engine/season/tests/test_choose_watch.py::test_by_subject_packing_ignores_id_names`" (new; red before the edit).
- FALSIFIER and CONTROL: "at `scene_packing_rule: by_subject`, renaming a subject id does not change which scene runs first" fails. Control: at the shipped `greedy` the realm hash at seed 0, two seasons, equal to B09.13's.
- GATE: `python -m pytest engine/season/tests/test_choose_watch.py -q` → pass; the control → equal.
- HASH MOVERS: none ("moves nothing at the shipped `greedy`").
- DEPENDS ON: V12 B09.13 (the test file); EXISTS-IN-TREE `pack_scenes`, the `scene_packing_rule` fixture.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B09's producer; `Item: B09.14`, `[skip ci]`.

### B09.15 — superseded sentences corrected at their owners · 02_CHAR_reason_trail_and_small_edits Part C · BUILD · HASH EQUAL
- SOURCE: the same file, Part C (each "a superseded sentence; ladder step 1"); the `decision/sheet.py` docstring row is `U5a_CORE_owed_edits.md` §B row 10, "carried here".
- ADVANCES: none of the nine ("None of Part C changes behaviour").
- INSTRUCTION (the rows, copied; R-06's and R-08's `measured:` heads not carried, UNDECIDED (7)):

  | file | now reads | should read |
  |---|---|---|
  | `decision/options.py::project` docstring; `decision/choose.py` comment in `make_ranker` | *"thirteen conviction weights, in the four-axis basis"*; *"weights over the THIRTEEN ... four-axis basis"* | fifteen pursuits over seven bipolar axes (`ED-IN-0261`, the 2026-10-06 row) |
  | `decision/sheet.py` module docstring | the design is *"PROPOSED and HELD BACK (ED-1094)"* | RATIFIED (Jordan, 2026-11-05, ED-IN-0349), as `proposals/2026-10-07-character-sheet-spaces.md`'s Status line reads |
  | `data/cast.py` module docstring | *"31 a `territory`, 30 `goals`, 29 `stats`, 32 `ts`"* (keys present) | the non-null counts at this tree, or no counts (the source's figures re-read at the item's tree; "no counts" if they differ) |
  | `engine/season/requirements.yaml` R-08 `disposition:` | cites `engine/season/decision.py::make_chooser` | `engine/season/decision/choose.py` (`make_ranker`, `score_order`) |
  | `hole_register.yaml` H-189 `default:` | *"whether a crisis fires within a season is not measured here"* | measured 2026-11-12, `build_realm`, two seasons: `Person.conviction` rewritten for 0 of 46 cast at seed 0 and 6 of 46 at seed 1 (re-read at this tree and the reading written with its SHA) |
  | `hole_register.yaml` H-237 | *"over 2 seasons at seed 0 there are 0 told claims with a chain"* | re-read: 12 chained claims of 22,958 at seed 0, 5 of 21,469 at seed 1, none at two hops; `teller_weight` is reached, rarely (re-read at this tree, with its SHA) |
  | `CURRENT.md` character-model row | head `proposals/2026-09-20-pursuit-basis-worksheet.yaml` | the owners the worksheet's own header names (`references/descriptor_registry.yaml: pursuit_roster`, `axis_roster`; `engine/season/rosters.yaml: tables.pursuit_projection`, `tables.alignment`); then the worksheet is deleted with an exact-file `FORK:` row, as its header says it is once its values land |

  STOPS IF: B02 removed R-08's `disposition:` key; then that row is dropped and the commit body says so. The `FORK:` row: `| \`proposals/2026-09-20-pursuit-basis-worksheet.yaml\` | \`FORK:<sha>\` | FORKED (<date>, workplan v12 B09.15: its values landed at the owners its header names, \`02_CHAR_reason_trail_and_small_edits.md\` Part C; \`<sha>\` is the last commit carrying the file) |`, read back through `pathres.load_alias_map()`.
- WHERE: `engine/season/decision/options.py` (`project` docstring); `engine/season/decision/choose.py` (`make_ranker` comment); `engine/season/decision/sheet.py` (module docstring); `engine/season/data/cast.py` (module docstring); `engine/season/requirements.yaml` (R-08 `disposition:`); `engine/season/hole_register.yaml` (H-189, H-237); `CURRENT.md` (the character-model row); DELETE `proposals/2026-09-20-pursuit-basis-worksheet.yaml`; `references/restructure_ledger.md` (one `FORK:` row).
- TESTS: none new.
- FALSIFIER and CONTROL: a corrected sentence that still says the opposite of the code. Control: the realm hash at seed 0, two seasons, equal to B09.14's.
- GATE: `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`) (R1 repair 1's form; this line's "and `--requirements`" wording escaped it; repair lane R2a); `python -m engine.season.harness.register --requirements` → exit 0; `python tools/currency_consistency_check.py` → exit 0; `python tools/freshness_gate.py` → its reading quoted. Record line, not a gate arm (it observes the edit to a pointer index, not behaviour; repair lane R2a, K2 #12): `git grep -n "pursuit-basis-worksheet" -- CURRENT.md` → nothing.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE the seven sites (opened at `aa31fd2`: `options.py` `project` docstring, `choose.py` comment, `sheet.py` header, R-08 `disposition:` citing `decision.py::make_chooser`, `CURRENT.md:21`); V12 Batch B02 (the requirements file's shape).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B09's producer; `Item: B09.15`, `[skip ci]`.

### B09.16 — the Scene is kept beside its acts · 01_CORE_reason_trail_in_the_act_store · BUILD · HASH EQUAL
- SOURCE: `proposals/01_CORE_reason_trail_in_the_act_store.md` "Edits" 1, 2, 4, 5 (3 is B09.13's hook), "Gate", "Falsifier"; `04` §A.2, §C.1, PART D rows 41, 41a; C3-C16, C3-N27; closes F-CORE-12.
- ADVANCES: re-read R-01.b, .c unchanged; a past act's question survives the driver.
- INSTRUCTION (copied):
  1. "`engine/season/state/acts.py` — the Scene store:
     ```python
     class ActStore:
         def add_scene(self, sc: Scene) -> None      # append-only; refuses a repeated id, as `add` does for an Act
         def scene_of(self, act_id: str) -> Optional[Scene]
         def scenes(self) -> tuple                    # in release order
     ```"
  2. "`loop/deliberate.py` keeps returning its `Scene` map … and stores nothing (its line `self.scenes[sc.id] = sc` is deleted with `SeasonDriver.scenes`). `loop/resolve.py::resolve`, which holds the ACTS token and the act store, calls `w.acts.add_scene(sc)` for each Scene of its `scenes` argument immediately before it appends that Scene's acts (`w.acts.append`). `_occasion_of` reads `w.acts.scene_of(a.id)`; `epistemic._term_why` (the one other reader of `Scene.occasion`) reads the same accessor."
  3. "`engine/season/state/world.py::content_hash` — not folded. The Scene store is left out of the digest `[ASSUMPTION; medium; Jordan to correct; revert: fold it]`."
  4. "`engine/season/harness/chronicle.py` — the reader: `--chains` prints, per act, `for: <occasion.source> <occasion.about>` (and the deciding term where the CHAR proposal's watcher supplied one)."
  The standing-occasion case "needs no new field … `causes[]` stays `[act]`" for an occasion that is no Event (B09.12 adds the opening Event where the log holds one).
- WHERE: `engine/season/state/acts.py` (`ActStore.add_scene`, `scene_of`, `scenes`); `engine/season/loop/deliberate.py` (the store line); `engine/season/loop/driver.py` (`SeasonDriver.scenes`); `engine/season/loop/resolve.py` (`resolve`, `_occasion_ids`: the source's `_occasion_of` is that function at `resolve.py:159`, K2 check); `engine/season/epistemic.py` (`_term_why`'s scene read); `engine/season/harness/chronicle.py` (`--chains`); NEW `engine/season/tests/test_scene_store.py`.
- TESTS (written first): `test_the_driver_holds_no_scenes`; `test_every_stored_act_answers_scene_of` (headless, seed 0, two seasons; "three" in the source, A-114); `test_a_fresh_driver_answers_a_season_0_acts_question` ("a second `SeasonDriver(w)` prints the same `for:` line"); `test_hash_equal_with_the_scene_store_unfolded` (the content hash at seed 0, two seasons, equal to B09.15's reading, re-read on the batch's tree, C3-N27). The existing `test_g2_token.py::test_g2_deliberate_mutates_no_store_by_any_route` "is the falsifier of the Layer 1 rewrite".
- FALSIFIER and CONTROL: "Construct a fresh driver … and ask for a season-0 act's question. `None` falsifies the edit. A changed content hash falsifies edit 4's claim."
- GATE: `python -m pytest engine/season/tests/test_scene_store.py engine/season/tests/test_g2_token.py -q` → pass; `python -m engine.season.harness.chronicle --seed 0 --seasons 2 --chains --min-depth 2` → exit 0 with `for:` lines.
- HASH MOVERS: none (edit 4: not folded).
- DEPENDS ON: V12 B09.13 (the hook the chronicle line reads, U3 §1.2 B09 row 7); EXISTS-IN-TREE `state/acts.py::ActStore`, `loop/driver.py::SeasonDriver.scenes`, `loop/resolve.py::_occasion_ids`, `epistemic._term_why`, `harness/chronicle.py`.
- GLOSSARY: none.
- COST and TIER: edit (four files); `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.16`, `[skip ci]`.

### B09.17 — a witness may connect what he holds, at control · 16_PESSIMIST_GO_a_witness_may_connect_what_he_holds · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_GO_a_witness_may_connect_what_he_holds.md` "The resolution, decided" §1–§3, "The gate", "The falsifier", "Cost class" ("one commit at the control"); D-U1-07; closes F-PES-GO-04 (R8.4, narrowed).
- ADVANCES: re-read R-07.a unchanged; a relation between memories (no conjunct moves at the control).
- INSTRUCTION (copied):
  1. What `why` holds: "For a witness `pid` of Event `e`: walk `e.causes` in order, skipping `ROOT` and act ids. For the first cause that is an Event `c` (`state/attribution.py::event_by_id`) for which `pid`'s ledger holds a claim WITNESS deposited from `c`, `why` is that claim's id. Otherwise `None`. **The claim is found by look-up**: the `claim.deposited` Event whose `causes[0]` is `c.id` and whose receipt names `pid`'s ledger …. The id formula WITNESS mints … is only a fallback, used if the look-up is measured too slow at build, and then only after verifying that a deposit's tick is the Event's `emitted_at` `[ASSUMPTION; verify at build]`." "His own act is not a draw: where `pid` is the actor (`doer` is stamped), `why` is the occasion he acted on, with certainty" (read through `w.acts.scene_of`, B09.16).
  2. `rosters.yaml`, `observation_terms.supplied_by`:
     ```
     co_located:   [stratum, marks, who, why]
     witness_key:  [stratum, who, why]
     document_key: []            # unchanged (R8.5, ruled)
     post_remit:   [stratum]     # unchanged
     chronicle:    [stratum]     # unchanged
     ```
     "A channel that supplies `why` makes the witness **eligible**. Whether he connects them is one keyed draw, `draw(pid, f"why:{e.id}")`, against a chance": `data/fixtures.py` `connection_chance = 0.0  # CONTROL (shipped at first landing): no draw, hash EQUAL`, with its `[JUSTIFIED: …]` line and HOLE row (B09's H block slot 3; "proposed on-value 0.6, + 0.2 where his claim on the antecedent carries a `who`" in the row, `[ASSUMPTION; medium; Jordan to correct; revert: 0.0]`).
  3. "`epistemic.py`: the term readers take the witness (`TERM_READERS[t](w, e, act, pid)`; three of the four ignore it); `_term_why` returns the claim id per §1; `seen_of` takes the draw for an eligible witness. The docstring's 'ALWAYS `None`' paragraph is replaced." "`rosters.yaml`: … the `⚠ NO CHANNEL SUPPLIES why` note replaced by what `why` is." "`decision/sheet.py::chronicle`: `Chronicle` gains `threads`, a tuple of `(claim id, why id)` for each `seen` claim of his whose `why` names a claim he still holds." "Nothing in `decision/choose.py` reads it."
- WHERE: `engine/season/epistemic.py` (`TERM_READERS`, `_term_why`, `seen_of`); `engine/season/rosters.yaml` (`observation_terms.supplied_by`, the note); `engine/season/data/fixtures.py` (`connection_chance`); `engine/season/hole_register.yaml` (one new row); `engine/season/decision/sheet.py` (`Chronicle.threads`, `chronicle`); NEW `engine/season/tests/test_seen_why.py`.
- TESTS (committed first): `test_control_chance_zero_takes_no_draw_and_hash_equal` (gate 1), `test_every_why_names_a_claim_in_the_holders_ledger` (gate 2, `checked >= 100`), `test_share_with_why_inside_binomial_band` (gate 3), `test_document_channel_never_carries_why`, `test_chronicle_threads_empty_at_control` (gate 5). Gates 2 and 3 run the on-arm inside the test (the chance set in the test's own fixtures; the shipped value stays 0.0).
- FALSIFIER and CONTROL: "A `why` naming a claim the holder does not hold. A `why` on a document-channel deposit. An on-arm run in which every eligible witness connects (the draw is decoration) or none does. A hash move at the control." Control: "`connection_chance = 0.0`, seeds 0–2, two seasons: every hash equal" to B09.16's reading; "`seen` claims with `why`: 0".
- GATE: `python -m pytest engine/season/tests/test_seen_why.py -q` → five pass; the control → hashes equal; reading 4 (`chronicle --chains --min-depth 2`, seeds 0–2, two seasons) → 0 at the control, quoted.
- HASH MOVERS: none at the control; "a declared mover when the chance is raised" (B98).
- DEPENDS ON: V12 B09.16 (`scene_of`, the actor's occasion); EXISTS-IN-TREE `epistemic._term_why`, `seen_of`, `TERM_READERS`, `state/attribution.py::event_by_id`, `observation_terms`, `decision/sheet.py::Chronicle`.
- GLOSSARY: none (`why` is a term of `observation_terms`, not a new word).
- IDS: H block slot 3.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.17`, `[skip ci]`.

### B09.18 — a predicate never raises and names the clause that refused · 01_CORE_predicates_name_their_clause step one · BUILD · HASH EQUAL
- SOURCE: `proposals/01_CORE_predicates_name_their_clause.md` "Step one" edits 1–3, its "Gate", "Falsifier"; closes F-CORE-14 (step one).
- ADVANCES: none of the nine; a malformed act is refused, not fatal.
- INSTRUCTION (copied):
  1. "`engine/season/state/carriers.py::subject_of` … Old: `return d.get("subject") or ""`. New:
     ```python
     s = d.get("subject")
     return s if isinstance(s, str) else ""
     ```
     A sibling `operand_of(a, name) -> str` with the same rule serves `office`, `to`." `[UNVERIFIED in the source: that no computed act carries a non-string subject today … if either [gate hash] moves the edit is confined to the four predicates and `subject_of` is left alone.]`
  2. "`_req_dispatch`, `_req_convene` and `_req_revoke` read `payload` directly; `_req_oblige` passes a possibly unhashable `seat` to `dict.get`. Each reads `subject_of(a)` / `operand_of(a, "office")`. `_req_convene`'s carve-out (no subject admits) is kept by testing the raw key's absence before the read. The three inline guards (*'a list … is unhashable: refuse, never raise'*) become the same call, so the rule lives once."
  3. "The twenty-one bare `return False` in `confer`, `establish`, `oblige`, `succeed` become `return _refuse("<clause>", "<ids>")`":

     | predicate | clauses (in branch order) |
     |---|---|
     | `establish` | `office resolves`, `rung held`, `conferral basis`, `filler`, `re-founding`, `may fill`, `reduction needs revocation` |
     | `confer` | `office`, `basis`, `conferee`, `purview`, `held`, `displacement` (the decorator below) |
     | `oblige` | `seat`, `binds`, `own_seat`, `one_edge`, `banned` `[ASSUMPTION: names from the branch comments of `_req_oblige`]` |
     | `succeed` | `operand`, `banned` `[ASSUMPTION: from the branch comments of `_req_succeed`]` |

     The count is re-read at the item's open (`ast` walk, the test below) and a branch the table does not name takes its comment's phrase, named in the commit body.
- WHERE: `engine/season/state/carriers.py` (`subject_of`, NEW `operand_of`); `engine/season/loop/predicates.py` (`_req_dispatch`, `_req_convene`, `_req_revoke`, `_req_oblige`, `_req_confer`, `_req_establish`, `_req_succeed`, the three inline guards); NEW `engine/season/tests/test_predicates_clause.py`.
- TESTS (the scratch `probe_predicates.py` restated, written first, read red): `test_every_refusing_branch_names_a_clause` ("an `ast` walk of the nine registered predicates: zero bare `return False`, with a population floor of nine and a planted bare branch caught"); `test_a_list_operand_is_refused_not_raised` ("each predicate on `{"subject": ["a", "b"]}` refuses, none raises").
- FALSIFIER and CONTROL: "Any predicate still raising on `{"subject": ["a", "b"]}`; a changed headless hash." Control: `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` → hash equal to B09.17's reading (the source's literal is pre-B01; re-read on the batch's base, C3-N27).
- GATE: `python -m pytest engine/season/tests/test_predicates_clause.py -q` → pass; the headless control → equal; the realm hash (`HASH READING`) at seed 0, two seasons → equal to B09.17's.
- HASH MOVERS: none ("a trace row is not world state").
- DEPENDS ON: EXISTS-IN-TREE `state/carriers.py::subject_of`, `loop/predicates.py::_refuse` and the nine registered predicates; V12 Batch B02.
- GLOSSARY: none (prose says "sworn man"; the tree key `obligees` keeps its name, D-06).
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.18`, `[skip ci]`.

### B09.19 — the refused clause can reach the Event's kind (the channel) · 01_CORE_predicates_name_their_clause step two, edit 4's mechanism · BUILD · HASH EQUAL
- SOURCE: the same file, "Step two" edit 4 and its "Gate", "Falsifier"; the four authored rows go to B21 (UNDECIDED (4)).
- ADVANCES: none of the nine; "predicate rows and typed rows report a failed clause the same way".
- INSTRUCTION (copied): "A predicate may return `(ok, clause)` where `clause` is one of the names it declares:
  ```python
  @requires_predicate("confer", clauses=("office", "basis", "conferee", "purview", "held", "displacement"))
  def _req_confer(w, a) -> tuple[bool, Optional[str]]: ...
  ```
  `_admits` builds `Verdict(UNKNOWN, (), failed=clause)` for a predicate row (it builds `Verdict(UNKNOWN, ())` today) and already calls `row.refusal_for(verdict.failed)`. No `observed` reads are attached, so WITNESS deposits nothing new from the read itself; what changes is the refusal *kind*. The loader's rule *'a keyed row must be typed'* gains its second arm: a keyed predicate row is admitted when its keys equal the clause names passed in by the driver (`precondition_evaluable(predicates)` already receives the predicate table as a parameter for the same import-direction reason). A flat predicate row is unchanged." The four predicates of B09.18's table declare their `clauses=`; no `verb_table.yaml` row is keyed here.
- WHERE: `engine/season/loop/predicates.py` (`requires_predicate`'s `clauses=`, the four predicates' returns); `engine/season/loop/resolve.py` (`_admits`); `engine/season/data/verbs.py` (`precondition_evaluable`, the keyed-row rule); `engine/season/tests/test_predicates_clause.py`.
- TESTS: `test_predicates_clause.py::test_a_keyed_predicate_row_emits_its_clauses_kind` on a planted keyed `confer` row in the test's own table ("a `confer` … refused at the purview clause emits the purview kind and not the cardinality kind, and the actor's ledger holds a claim keyed by it"); `test_a_keyed_predicate_row_with_unknown_keys_is_refused` `[ASSUMPTION: test name; the item creates it — the loader arm's refusal]`.
- FALSIFIER and CONTROL: "Two refusals for different clauses emitting one kind on a keyed row." Control: with every shipped predicate row flat, the realm hash at seed 0, two seasons, equal to B09.18's.
- GATE: `python -m pytest engine/season/tests/test_predicates_clause.py -q` → pass; the control → equal.
- HASH MOVERS: none here ("step two each keyed row (declared)": in B21).
- DEPENDS ON: V12 B09.18; EXISTS-IN-TREE `loop/resolve.py::_admits`, `row.refusal_for`, `data/verbs.py::precondition_evaluable`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.19`, `[skip ci]`.

### B09.22 — a seat closed by a death names its holder · IN-58's carrier (lane D4; v11 IN-58 NARROWED: "Reopens when a claim names the dead holder with the seat (a CP-T02-01 follow-up …)") · BUILD · HASH MOVER(behaviour)
- SOURCE: carry-forward `master/eval/E1.md` "### IN-58" (NARROWED, REMAINING UNBUILT); `engine/season/state/gate.py::Subject.seat` (its docstring: "THE CARRIER CHOICE: the receipt is what WITNESS deposits a claim about … no Claim field, no Event field and no world stamp is added") and `Subject.observed` (CP-T03-02: "They ride, through `loop/resolve.py::_fold`, the Event of each kind this subject earns … so WITNESS deposits them by its shipped `observation_deposit_mode` with no new channel"); `queries/person_q.py::deeds_judged`'s docstring ("What is missing is the PAIRING, not the edge"); lane D4's ladder record (`checks/D4_APPLIED.md`).
- ADVANCES: R-07 (contributor, as IN-58); the precondition of B09.20.
- INSTRUCTION:
  1. `engine/season/state/gate.py::Subject.seat(t)`: the seat Subject carries one Observation, the value the write leaves (CP-T03-02's rule), naming the holder whose `hold` closed: `observed=(Observation(t.object, "hold", t.subject),)` `[ASSUMPTION: the predicate `hold`, the closed edge's own kind — basis: `data/requires.py::Observation`'s docstring, "THE PREDICATE IS DERIVED FROM THE FORM, NEVER LOOKED UP IN A ROSTER"; if `grep -rn "\"hold\"" engine/season/queries/person_q.py engine/season/decision` shows a claim reader already keyed on that predicate for another meaning, the item takes `closed_holder` and says so]`. The docstring gains one sentence: the Observation is the pairing IN-58 lacked (a claim that names the dead holder with the seat), carried by the existing channel; no Claim, Event or World field is added.
  2. No reader is added here (B09.20 is the reader). `death_subjects` is unchanged (it calls `Subject.seat`).
- WHERE: `engine/season/state/gate.py` (`Subject.seat`); NEW `engine/season/tests/test_sworn_grievance.py` `[ASSUMPTION: test-file name; the item creates it, E-3]`.
- TESTS: `test_a_witness_of_a_seat_holders_death_holds_the_seat_and_its_holder` (through the real fold and the real WITNESS barrier on a hand-built world, the `g6` tests' method: a seat-holder killed in a witnessed act; the witness's ledger holds `(seat, tenure.closed, True)` and `(seat, hold, victim)` with the same `when` and `lap`) `[ASSUMPTION: test name; E-3]`, written first and read red.
- FALSIFIER and CONTROL: a witness of the death who holds the `tenure.closed` claim and no claim naming the holder with the seat; a claim naming a holder whose `hold` did not close in that write. Control: a death of a person who holds no seat: tallies and ledgers equal to B09.21's tree.
- GATE: `python -m pytest engine/season/tests/test_sworn_grievance.py -q` → pass; the realm content hash (`HASH READING`) at seed 0, one season → moved where a seat-holder dies, equal where none does, which holds read off the log (`person.died` Events whose person held a seat) and quoted beside the two hashes.
- HASH MOVERS: ledgers wherever a seat-holder's death is witnessed (one more claim per witness). Declared; B09.99.
- EXPECTED RED UNTIL: B09.99 for the realm pins (under `[skip ci]`).
- DEPENDS ON: V12 B09.21 (the batch's last tree before it); EXISTS-IN-TREE `state/gate.py::Subject.seat`, `Subject.observed`, `death_subjects`, `data/requires.py::Observation`, `loop/witness.py` (the observation deposit).
- GLOSSARY: none (no new word: a claim that a seat was held by a person).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.22`, `[skip ci]`.

### B09.20 — the sworn-to half of grievance at read · IN-58 · BUILD (lane D4: its carrier is B09.22) · HASH EQUAL
- SOURCE: the intake `:143` (IN-58, STILL-NEEDED); its carry-forward `master/eval/E1.md` "IN-58" (v11 `_part4.md:680-693`: WHAT, NARROWED, GATE's LIMITS and revert, EXIT and FALSIFIER), `E2.md` "BLOCK IN-58", `E3.md` Block 14; rulings RS-23, RS-24, RS-29 (as cited there). Placed at the batch's tail in the intake's order (`V12_STRUCTURE_part2.md` §5.6), after its carrier B09.22.
- ADVANCES: R-07 (contributor).
- WHAT (copied): "Build the sworn-to half of grievance-at-read: a judge sworn to the victim's seat reads a different regard for the killer than an unsworn judge with equal stance and pursuits." "It ships OFF" (the entry; "Revert: factor off and cells unauthored").
- INSTRUCTION:
  1. `engine/season/queries/person_q.py::_bond(p, patient, lean)` (the judge's allegiance to the patient: `1 - a · sign(lean)`, `a = clamp(stance_toward(p, patient) / STANCE_MAX, -1, 1)`, "the stored half only"): gains the sworn arm. When `p` holds a live, un-`imposed` `oblige` Tenure (`p.tenures`, person-side: the entry's NARROWED, "the edge is person-side; the v9 blocker is gone") whose object is a seat `S`, and `p`'s own ledger holds B09.22's claim `(S, hold, patient)`, `sworn_bond` is added to `a` before the clamp. `_bond` and `deeds_judged` gain a keyword `sworn_bond: float = 0.0` (the control), on `deeds_judged`'s own `scar_shift=0.0` pattern; each caller that holds `fx` passes `fx.sworn_bond` `[ASSUMPTION: the callers holding `fx` are the ones that pass it; one holding none reads the control — basis: the keyword-default pattern already on `deeds_judged`]`. Person-side, no World (AX-2). Only `deeds_judged`'s paired-deed term (`lean · bond`) reads it, so the allegiance still "only scales a pursuit lean" (the entry's LIMITS).
  2. `engine/season/data/fixtures.py`: `sworn_bond = 0.0` (control, SHIPPED: "it ships OFF"), swept {0, 0.5, 1.0} `[ASSUMPTION; medium; Jordan to correct — the sweep's points; basis: `stance_toward` is bounded in [-1, 1], so the oath is weighed on the stance's own scale]`, its `[JUSTIFIED: …]` tag naming one NUMBER row in `hole_register.yaml` (B09's H block, the IDS line's fourth slot).
  3. The `deeds_judged` docstring's "⚠ THE SWORN-TO HALF IS NOT BUILT" paragraph is rewritten to say it is built, at control, and where the pairing comes from (B09.22).
- WHERE: `engine/season/queries/person_q.py` (`_bond`, the `deeds_judged` docstring); `engine/season/data/fixtures.py` (`sworn_bond`); `engine/season/hole_register.yaml` (one NUMBER row); `engine/season/tests/test_sworn_grievance.py` (B09.22's file).
- TESTS: `test_a_sworn_judge_reads_the_killer_differently` (the entry's falsifier: "two judges with equal stance and pursuits, one sworn to the victim's seat, read different regard for the killer", at `sworn_bond` 0.5) and `test_sworn_bond_zero_is_todays_regard` `[ASSUMPTION: test names; E-3]`, written first, red.
- FALSIFIER and CONTROL: the entry's ("… -> else that half is not built"), and a sworn judge whose regard moves with no claim naming the victim in the seat (the pairing guessed from `when`/`lap`, which `deed_doer` refuses). Control: `sworn_bond = 0.0`: the realm content hash at seed 0, one season, equal to B09.22's reading.
- GATE: `python -m pytest engine/season/tests/test_sworn_grievance.py -q` → pass; the control → equal.
- HASH MOVERS: none at control ("equal at shipped" control; "a declared mover wherever it executes", the entry, when `sworn_bond` leaves 0).
- DEPENDS ON: V12 B09.22 (the claim naming the dead holder with the seat); LANDED ALREADY (re-checked at the item's open): the stance-only half (`3bf936ee`), CR-16's `stance_polarity: declared` (`142e91e22`), IN-40's `oblige` edge; EXISTS-IN-TREE `queries/person_q.py::_bond`, `::deeds_judged`, `::deed_doer`, `Person.tenures`.
- GLOSSARY: none (*sworn* is a `U1_GLOSSARY.md` row this batch's C(k) names).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.20`, `[skip ci]`.

### B09.21 — a zero-wear clock write is not written · H-135 · BUILD · HASH MOVER(behaviour)
- SOURCE: the intake `:144` (H-135; `settled:` "register row governs (E6:148 STILL-NEEDED)"); its carry-forward `master/eval/E6.md` row H-135 and Block 5 ("`H-135`: judge closure writes for F9 or skip the write when `wear` is 0 (the shipped dwelling kind); 248 of 322 `condition.worn` Events a season are zero writes"; "`H-135` joins `B09-memory` because it is the one declared mover (event counts)"); `engine/season/hole_register.yaml` H-135 (owner: "state/world.py -- `write()`'s closure branch; loop/matter.py's clock writers specifically"). Placed at the batch's tail in the intake's order (§5.6).
- ADVANCES: none of the nine; no Event reports a change that did not happen.
- INSTRUCTION: the narrower of the two fix shapes (UNDECIDED (6)): in `engine/season/loop/matter.py`'s clock writer that emits `condition.worn`, a Site whose wear this season is 0 is not written and emits nothing; the closure branch of `World.write` is unchanged. H-135's row is narrowed in the same commit: the live instance closed, the closure branch's F9 judgment left as the row's remainder (its `hole:` text kept; one closing line naming this item).
- WHERE: `engine/season/loop/matter.py` (the `condition.worn` clock writer); `engine/season/hole_register.yaml` (H-135); `engine/season/tests/test_gate_observation.py` (NEW if B03 has not created it, else edited: B03's H-137, H-130, H-139 name the same file, `[ASSUMPTION: name]` in E6).
- TESTS (E6's gate, written first, read red): `engine/season/tests/test_gate_observation.py::test_a_zero_wear_write_emits_no_condition_worn` `[ASSUMPTION: test name; the item creates it]` ("a zero-wear write emits no `condition.worn` … and the control keeps the old count").
- FALSIFIER and CONTROL: a `condition.worn` Event whose Site's condition did not move. Control: a Site with non-zero wear still writes and emits `condition.worn` (the count of non-zero writes at seed 0, two seasons, equal to B09.19's reading).
- GATE: `python -m pytest engine/season/tests/test_gate_observation.py -q` → pass; at seed 0, two seasons: `condition.worn` Events with zero wear → 0; with non-zero wear → equal to the before-reading (`reading @<sha>`).
- HASH MOVERS: "event counts and the log hash" (E6). Declared; B09.99.
- DEPENDS ON: V12 B09.01 (MATTER's ledger walk gone; `loop/matter.py` edited once per batch in order); EXISTS-IN-TREE `loop/matter.py` (the clock writers), H-135.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`; "`opus` read of the F9 design for `H-135`" (E6) — `opus` reads the narrowing at the close.
- LANDS IT: B09's producer; `Item: B09.21`, `[skip ci]`.

### B09.99 — re-pin and close readings · V12_STRUCTURE_part4.md E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12; the record proposal's "Cost class" (the re-record across `engine/season/tests` and `engine/tests`).
- ADVANCES: the five re-read conjuncts' readings on one tree.
- INSTRUCTION:
  1. Re-record, once, every pin the batch moved: `engine/season/tests/_realm_goldens.py` (every world); `engine/season/tests/test_go07_canonical_digest.py` where it moved; every content hash pinned under `engine/tests`; baseline the S9 merged head (`reading @<sha>`). The commit says the re-pin sentence of the RE-PIN line.
  2. Read R-01.b, R-01.c, R-02.a, R-02.b, R-07.a by their `argv` (`register --requirements` and each conjunct's command) and write their `reading:` records (`tree`, `date`, `seed`, `seasons`, `line`, `control`, `does_not_show`); `status:` not edited.
  3. Take the batch gate's seeded readings (seeds 0 to 2, E-2) and the close record.
- WHERE: `engine/season/tests/_realm_goldens.py`; `engine/season/tests/test_go07_canonical_digest.py` (if moved); the `engine/tests` pin files that moved; `engine/season/requirements.yaml` (five `reading:` records).
- TESTS: every test of the BATCH GATE green after the re-pin.
- FALSIFIER and CONTROL: a pin moved that no item declared. Control: the control arms of the BATCH GATE.
- GATE: the BATCH GATE.
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: V12 B09.01 to B09.22 (B09.22 lane D4).
- GLOSSARY: none.
- COST and TIER: reading and re-pin; `sonnet`, `high`.
- LANDS IT: B09's producer; `Item: B09.99`, the batch's last `Item:` commit (no `[skip ci]`).

| STOP. Batch B09-memory closes here |
