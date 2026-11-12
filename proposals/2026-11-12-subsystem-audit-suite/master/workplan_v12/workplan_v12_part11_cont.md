# Workplan v12 — part 11, continued: batch B09-memory

## Status: PROPOSED (the continuation of part 11 of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `aa31fd2`, read 2026-11-12; author lane A11. The head of part 11 (its first file) states the words, paths and renamed identifiers this file uses; B09 lands after B04, so the season's within-season pass is `lap` (`Claim.lap`, `SeasonDriver.lap`, `scenes_per_lap`) wherever copied text says `round` for it.

---

## Batch B09-memory · lane IN · wave W10 · step S10 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B09-memory
IN-FLIGHT ROW: registers/handoffs/HANDOFF_IN.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B05-one-roll
GATE: Batch B07-task-draw
REQUIREMENT: re-read R-01.b, R-01.c, R-02.a, R-02.b, R-07.a → unchanged (each conjunct `holds: yes` as B02 left it, `IS_A_NINE_part2.md` §12.2 row B09); rulings served: A-24 (a crisis is drawn and seen: the scar half here), A-33, A-47, A-62, A-81 (a refusal is remembered), D-46, D-48
BATCH GATE (read once, on the closing tree; `PYTHONHASHSEED=0` on every seeded command):
  `python -m pytest engine/season/tests/test_claim_fade_as_read.py engine/season/tests/test_refusal_memory.py engine/season/tests/test_one_reader_of_a_ledger.py engine/season/tests/test_g1a_act_store_and_receipts.py engine/season/tests/test_g4_no_op_receipt.py engine/season/tests/test_in53_vacancy_need.py engine/season/tests/test_in50_refusals_carry_the_occasion.py engine/season/tests/test_choose_watch.py engine/season/tests/test_in62_decision_spread.py engine/season/tests/test_scene_store.py engine/season/tests/test_g2_token.py engine/season/tests/test_seen_why.py engine/season/tests/test_predicates_clause.py engine/season/tests/test_gate_observation.py -q` → all pass;
  the control arms, each at seed 0, two seasons, against the reading named: `refusal_memory = 0.0` → content hash equal to B09.03's reading (U3 §1 item 10's gate, "`refusal_memory = 0.0` equal"); `weigh_confidence = False` → equal to B09.06's; `standing_occasion_cause = False` → equal to B09.11's; `connection_chance = 0.0` and `finding_none_deposit: none` as shipped (no move);
  `python -m engine.season.harness.decision_spread --retries --seed 0 --seasons 2` → B09.05's five rows, quoted;
  `python -m engine.season.harness.chronicle --seed N --seasons 2 --chains --min-depth 2`, N = 0, 1, 2 → exit 0, a `for:` line per act (B09.16);
  `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` → its act and Event tallies quoted against the S9 merged head's (`reading @<sha>`);
  the realm content hash of `build_realm(s)`, two seasons, s = 0, 1, 2 → moved (declared) and re-recorded by B09.99;
  `python -m engine.season.harness.register --check` → exit 0; `--requirements` → nine lines, R-01.b, .c, R-02.a, .b, R-07.a `holds: yes`; `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (engine core and registries: the full gates);
  the glossary rows each item names, read against the code it landed (`STAGES.md`, "The glossary always matches", rule 2);
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the five named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; B09.99 writes the five conjuncts' `reading:` records; `status:` is not edited (`IS-A-12`).
RE-PIN: once, in B09.99: every realm pin in `engine/season/tests/_realm_goldens.py`, `test_go07_canonical_digest.py`'s vectors where they moved, and every content hash pinned under `engine/tests` (the record proposal: "one deliberate golden re-record across `engine/season/tests` and `engine/tests` wherever a content hash is pinned"), read against the S9 merged head (B07's and B17's merges, `reading @<sha>`); the commit says "re-pin: fewer Events (B09.01), a filled `Receipt.delta` and `scar.taken` Events (B09.10, B09.11), the opening Event in `causes` (B09.12), the shipped `refusal_memory` and `weigh_confidence` (B09.05, B09.08), the re-pointed belief readers (B09.07), no zero-wear `condition.worn` (B09.21)".
IDS: ED-IN 0; H 3 (B09.03: `refusal_memory`'s HOLE row; B09.12: `standing_occasion_cause`'s row; B09.17: `connection_chance`'s row; each `[JUSTIFIED: … H-nnn]` line cites its slot)
DIALS AT CONTROL: `refusal_memory` = 0.0 at B09.03; set by this batch's B09.05 (0.5); target: the five readings of `16_PESSIMIST_CORE_a_refusal_is_remembered` "Gate". `weigh_confidence` = `False` at B09.06; set by B09.08 (`True`); target: `16_PESSIMIST_SC_B` "Gate". `standing_occasion_cause` = `True` shipped by B09.12 (control `False`). `finding_none_deposit` = `none`; set by B98; target: "failed inquiry aims tried again fall at the `actor` arm with `refusal_memory` above 0 … deposits to non-actors equal across arms" (`U5a_DICE_owed_edits` §4 "Gate", seeds 0–2, two seasons). `connection_chance` = 0.0; set by B98; target: `16_PESSIMIST_GO_a_witness_may_connect_what_he_holds` gates 2–5 on-arm ("proposed on-value 0.6, + 0.2 where his claim on the antecedent carries a `who`", `[ASSUMPTION; medium; Jordan to correct]` in the source).
UNDECIDED: (1) `01_CORE_claim_fade_as_read` edit 5 (raise `corpus_run.MAX_SEASONS` to 16 "once the gate below reads flat") is not carried: its condition is an eight-season reading that A-114 holds to B99; the clamp stays 6 and H2's held table is owed the row (the other reading: raise it now, which no gate before B99 can justify). (2) The source gates at three, four and eight seasons (`claim_fade` tests, `a_refusal_is_remembered`'s five readings, `test_scene_store`'s "three seasons") are written at two ("(… seasons in the source; A-114)"), `V12_STRUCTURE_part2.md` §5.8. (3) `U5c_VERBS_residue_and_governance_owner` §3 is not in this batch although U3 §4.1 row 28 puts it here: step 1 extends CP-T06-04's deposit ("Plan CP-T06-04 (B10-14) already deposits …"), which is not in the tree at `aa31fd2` and lands in B11 (the intake's merged item H-314, CP-T06-03, CP-T06-04), and step 2 edits `person_q.present_persons`, which `08_FI_02` edit 5 builds in B11: the dependency wins (`V12_STRUCTURE_part4.md` E-8); owed to the B11 authors (A16, A17). (4) `01_CORE_predicates_name_their_clause` step two's four keyed rows (`confer`, `establish`, `revoke`, `oblige`) need kinds "authored in `verb_table.yaml` by the FA lane … in the same batch or B21": B09 lands the channel (B09.19, hash EQUAL with no keyed row); the four rows, one commit each, go to B21 (owed to A14, A15). (5) H-145 with NM-W9 (b): the intake's `settled:` says "register row governs (E7:30)", so the item is E7's (`EventLog.append` refuses a bare `StateChange`), not E2's reading ("a closure write emits its receipt with before ≠ after"); NM-W9's `Receipt.before/after` half is `16_PESSIMIST_CORE_the_record_holds_what_changed` edit 1 (B09.10). (6) H-135's two fix shapes ("judge closure writes for F9 or skip the write when `wear` is 0"): B09.21 takes the narrower (skip the zero-wear write in MATTER's clock writer); judging every closure write is the other. (7) `02_CHAR_reason_trail_and_small_edits` Part C's two `requirements.yaml` `measured:` head rewrites (R-06, R-08) are dead edits after B02.13 (`measured:` leaves; readings sit on conjuncts) and are not carried. (8) `16_PESSIMIST_GO_a_witness…`: "raising the chance is its own commit and re-pin" names no batch; B98 sets it (D-22). (9) IN-58 has no carrier in v12 (B09.20, BLOCKED).
C(B09-memory): this batch's entries; the plan's head parts; `unified/U1_GLOSSARY.md` rows *occasion*, *refusal*, *sworn*;
  `engine/season/state/ledgers.py`; `engine/season/state/world.py` (`write`, `content_hash`, `last_emission_of`); `engine/season/state/log.py` (`EventLog.append`); `engine/season/state/acts.py` (`ActStore`); `engine/season/state/carriers.py` (`subject_of`, `Scene`, `Claim`); `engine/season/state/gate.py` (`Subject.entity`); `engine/season/loop/matter.py`; `engine/season/loop/resolve.py` (`resolve`, `_occasion_ids`, `_occasion_of`, `_scar_witnesses`, `_admits`); `engine/season/loop/deliberate.py`; `engine/season/loop/driver.py` (`SeasonDriver.scenes`); `engine/season/loop/witness.py`; `engine/season/loop/predicates.py`; `engine/season/epistemic.py` (`_term_why`, `seen_of`, `TERM_READERS`);
  `engine/season/queries/person_q.py` (`LedgerReader`, `said_of`, `lie_said_of`); `engine/season/queries/world_q.py` (`current_stage`, `reception`); `engine/season/decision/choose.py` (`score_terms`, `odds_weight`, `make_chooser`, `make_ranker`, `pack_scenes`); `engine/season/decision/options.py` (`teller_weight`, `ledger_weigh`, `opening_set`, `project`); `engine/season/decision/questions.py`; `engine/season/decision/sheet.py` (`chronicle`, `Chronicle`); `engine/season/seam/wrappers/sigma.py`; `engine/season/data/fixtures.py`; `engine/season/data/rosters.py`; `engine/season/data/verbs.py`; `engine/season/data/cast.py` (docstring);
  `engine/season/rosters.yaml` (`undeposited_kinds`, `observation_terms`, NEW `standing_occasion_opened_by`); `engine/season/verb_table.yaml`; `engine/season/write_matrix.yaml` (`(Claim, confidence)`); `engine/season/hole_register.yaml` (H-183, H-189, H-237, H-145, H-135, H-111, the three new rows); `engine/season/requirements.yaml` (R-08 `disposition:`); `CURRENT.md` (character-model row); `proposals/2026-09-20-pursuit-basis-worksheet.yaml`; `references/restructure_ledger.md`;
  `engine/season/harness/decision_spread.py`, `interactions.py`, `aperture.py`, `chronicle.py`, `probes.py` (`about`), `report.py`, `delta.py`, `headless.py`, `corpus_run.py` (read only);
  the tests named in the items; `engine/season/tests/_realm_goldens.py` (B02); the closing SHAs of B00, B01, B02, B05, B07 and the S9 merged head; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_IN.md`, the skill and `methodology-close`).
COST: small builds and edits; producer `valoria-author` on `sonnet`, `high`; `opus` reads the shipped `refusal_memory` (B09.05) and H-135's narrowing (B09.21); the close's terminal critique `opus`.
EST: 11 h [estimate: `V12_STRUCTURE.md` §2.4's per-commit formula over this batch's 22 positions (0.4 h × 22 + 2.5 h); §2.2's 7 h counted members]

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
| B09.10 | a receipt carries the value the gate saw | `16_PESSIMIST_CORE_the_record_holds_what_changed` edit 1 | BUILD | MOVER(encoding) | B09.09 |
| B09.11 | a scar is recorded and witnessed by nobody | `16_PESSIMIST_CORE_the_record_holds_what_changed` edit 2 | BUILD | MOVER(behaviour) | B09.10 |
| B09.12 | an act on a standing occasion names the Event that opened it | `16_PESSIMIST_GAME_standing_occasions_carry_their_cause` | BUILD | MOVER(behaviour) | B09.11 |
| B09.13 | the chooser's observer hook; three harness wrappers deleted | `02_CHAR_reason_trail_and_small_edits` Part A (the hook) | BUILD | EQUAL | B09.12 |
| B09.14 | subjects packed by first appearance, not by name | `02_CHAR_reason_trail_and_small_edits` Part B row B2 | BUILD | EQUAL | B09.13 |
| B09.15 | superseded sentences corrected at their owners | `02_CHAR_reason_trail_and_small_edits` Part C | BUILD | EQUAL | B09.14 |
| B09.16 | the Scene is kept beside its acts | `01_CORE_reason_trail_in_the_act_store` | BUILD | EQUAL | B09.13 |
| B09.17 | a witness may connect what he holds, at control | `16_PESSIMIST_GO_a_witness_may_connect_what_he_holds` | BUILD | EQUAL | B09.16 |
| B09.18 | a predicate never raises and names the clause that refused | `01_CORE_predicates_name_their_clause` step one | BUILD | EQUAL | Batch B02 |
| B09.19 | the refused clause can reach the Event's kind (the channel) | `01_CORE_predicates_name_their_clause` step two, edit 4's mechanism | BUILD | EQUAL | B09.18 |
| B09.20 | the sworn-to half of grievance at read | IN-58 (intake `:143`) | BLOCKED (v12: a carrier is owed) | — | — |
| B09.21 | a zero-wear clock write is not written | H-135 (intake `:144`) | BUILD | MOVER(behaviour) | B09.01 |
| B09.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | B09.01 to B09.21 |

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
- GATE: `python -m pytest engine/season/tests/test_claim_fade_as_read.py -q` → pass; the control above (two seasons, `claim_decay_per_season` 0) → act multisets identical, quoted; the realm content hash at seed 0, two seasons → moved (fewer Events; `Claim.confidence` holds the deposited value), recorded for B09.99.
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
- GATE: `python -m pytest engine/season/tests/test_refusal_memory.py -q` → five pass; `report` then `delta HEAD` → `PROBE FLIPS 0`; `python tools/ci_sim_fabrication_check.py` → exit 0 (the new fixture's tag); `python -m engine.season.harness.register --check` → exit 0 (the new row).
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
- COST and TIER: a value flip and its readings; `sonnet` runs; "the shipped value 0.5 is an `opus`-or-Jordan judgment" — `opus` reads.
- LANDS IT: B09's producer; `Item: B09.05`, `[skip ci]`.
