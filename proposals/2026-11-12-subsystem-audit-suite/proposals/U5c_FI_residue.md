# U5c · FI — fieldwork residue: one change to the question loop, the order across three lanes, and the reconciled inquiry rows

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.4 row FRES (CONFORMS), §7 (INCOMPLETE: scratch probes, no named tests), §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-11i, ledger S-07, S-21, S-22; `unified/U1_GLOSSARY.md` *task*, *inquiry*, *party* ("patient" → counterparty); `unified/U3_DEPENDENCY_ORDER.md` node B11, §6.2). Changed: the four scratch probes the gates read (`r08_probe.py`, `p1_belief.py`, `p1d_where.py`, `fi_arms.py`; none is in the repository) are restated as named tests the batch writes first, with the expected readings quoted here; `graded_inquiries` is `graded_tasks` (D-U1-11i: renamed once in 18-A's commit, B07); §4's "judge whom evidence moves" points at the reconciled carrier (`02_CHAR_which_ground_moves_whom.md`'s `edge` rows; SC-P7 edit 3 is superseded); §7's "patient" is the counterparty (glossary); lands-it and tier. The order, the reconciled slants and the two-act conclusion stand.

**Lands in batch:** B11 (§1–§3, §6; §7 and §8 inside their sources' batches, B11 and B26). **Depends on:** B07 (`graded_tasks` and 18-A's loader edit), B10 (CHAR's chooser), plan position CR-29 (the `reach` roster) `[PL]`.

## Status: PROPOSED (written by the U5c closure lane; a plan for a later implementation lane, executed by nobody here; not ratified by being written, `CLAUDE.md` §2)

Carries the rows of `unified/U5_FINDINGS_CLOSURE_U5c.md` whose carrier column reads **FRES**, and conflicts
C-14, C-15, C-22 (the inquiry half), C-24 of `unified/U5_CONFLICTS_U5c.md`. Sources:
`audits/08_FI_audit.md`, `08_FI_audit_addendum_B.md`, `16_PESSIMIST_FI.md`,
`19_LACUNA_investigation_to_proceedings.md`. It edits no first-lane design: where it changes one, the
changed file carries a `Reconciled:` line pointing here.

## What it changes in `engine/season/` at runtime

§1: nothing beyond what `08_FI_01` and `16_PESSIMIST_FI_C` edit 4 already change; it makes them one
commit. §2, §3, §4, §5: nothing (an order, text, two closings, an acceptance reading). §6: the telling's
slant arms. §7: `reconstruct` deposits a conclusion to its maker and writes nothing. §8: what a look
teaches is read off one band-keyed table. Declared movers: §6 to §8, as their source proposals state.

## §1 One change to `questions_for`, not two (F-FI-01, F-PES-FI-04; R-04 corrected)

`08_FI_01_claim-sourced-referents.md` edits 2 to 5 (seats, vacancies, aims, matters) and
`16_PESSIMIST_FI_C_what_a_deed_leaves_behind.md` edit 4 (who exists, and where) rewrite the same function
for the same reason (ED-IN-0292, last row). The first audit's R-04 left clause 2 standing; the pessimist's
runs show it removes referents on world truth (`p1_belief.py` `dead-silent`: −28; `p1d_where.py`: 38 → 10).

Order, one commit: (1) `08_FI_01` edit 1 (`holders_named`, `vacant_named`); (2) `08_FI_02` edit 5
(`present_persons`); (3) `08_FI_01` edits 2 to 5 and `16_PESSIMIST_FI_C` edit 4; (4) `08_FI_01` edit 6
(`seed_seat_news`) in the same commit, so the realm does not start blind; (5) `08_FI_01` edits 7 and 8
(the requirement text; the one test).

Gate (one run of each, quoted in the commit body). The three probes are scratch scripts not in the
repository; the batch first writes their readings as tests in `engine/season/tests/test_fi_referents.py`:
`test_a_silent_seat_change_moves_no_candidate` (the `r08_probe.py` P1 and P2 readings: *candidates moved:
no*, both controls unchanged; it is `08_FI_01`'s "one test"), `test_a_silent_death_removes_no_candidate`
(`p1_belief.py` `dead-silent`: 0 candidates lost), `test_who_is_where_is_read_from_the_askers_ledger`
(`p1d_where.py`: 38 → 38), and `test_a_witnessed_change_does_move_the_candidates` (the positive arms).
`confer`, `petition` and `challenge` formed counts at seeds 0 to 2, before and after, are quoted.
Falsifier: `08_FI_01`'s and `16_PESSIMIST_FI_C`'s, unchanged. Hash: declared mover on every realm world.

## §2 The order across the FI, pessimist and LACUNA proposals, and CR-29's gate (R-06; F-PES-FI-10)

| # | lands | needs | gate (the proposal's own unless stated) |
|---|---|---|---|
| 1 | `16_PESSIMIST_FI_D` (three product-less rows withheld) | nothing | `fi_arms.py 0 3 ship` reproduces `nod3`'s census (the scratch `fi_arms.py` is restated first as `engine/season/tests/test_fi_arms.py`, parametrised over its arms `ship`, `draw1`, `nod3`, `nochron` as fixture sweeps; each row below reads it) |
| 2 | plan CR-29, taken first in B10-14 (`08_FI_02` edit 1) | the `reach` roster | **added here:** `fi_arms.py 0 3` and `1 2` under the new channel: `march` and `migrate` attempts inside the spread of today's `ship` and `draw1` arms (29 and 14 marches; 116 and 74 migration attempts at seed 0). `nochron` read 4 and 17. If the reading is outside, the roster lacks the kinds those candidates form on: add roster rows, never a second channel |
| 3 | `08_FI_02` edits 2 to 5 as reconciled (§6); `16_PESSIMIST_FI_A` edits 1 to 3 and 5 | 2 | two-hop chains above 0 at two of three seeds |
| 4 | §1 above | 2, 3 | §1 |
| 5 | `08_FI_07` Cut A (harness) | nothing | every run ends by a predicate |
| 6 | B10-14's cards with `16_PESSIMIST_FI_C` edits 1 to 3 | 2 | found deposits above 0 in a seeded realm |
| 7 | `08_FI_06`; then `16_PESSIMIST_FI_A` edit 4 | 3 | a hearer names the hand; a `Partial` telling withholds it |
| 8 | `08_FI_07` §2 (a); the look's reads (§8 here) | 6 | `examine` folded above 0 |
| 9 | plan CP-T06-05 with `14_VERBS_SOCIAL2_C` §3 and `19_LACUNA_questioning_has_an_approach_and_a_cost.md`; `interview` leaves `withheld_verbs` | 3, 7 | the questioned person answers by his own act |
| 10 | the conclusion (§7 here; `19_LACUNA_conclusion_is_a_committed_assertion.md`); `reconstruct` leaves `withheld_verbs` | 7, 9 | a conclusion that names someone other than the Event's actor at some seed |
| 11 | `16_PESSIMIST_FI_B` | 6 | a holder who knows a paper false reads nothing off it |
| 12 | `08_FI_05_evidence-interface_B.md` with `05_SC_evidence_and_rebuttal_B.md` and `19_LACUNA_admission_rides_the_citing_draw.md` | CR-61, plan SC-02, the hearing | their gates |
| 13 | `08_FI_08` §3; `08_FI_04` (its §4 budget row last, with `test_n3` read before and after) | 3 | theirs |

The `reach` roster has two cells Jordan has answered (`unified/DECISIONS_ANSWERED.md`), and they are
separate rows because the answers differ. **Seat changes** ship realm-wide, with presence, purview and
telling built as the test arm (A-32). **The death that emptied a seat** travels apart from the seat's
news: by presence, trail and telling only (A-33), so a realm can know a throne is empty and not know why.
`08_FI_01` edit 6 seeds the first cell; the second has no seed and is carried by `08_FI_06` and
`16_PESSIMIST_FI_C`'s deposits. Gate for the second cell: at one seed, a person holds the vacancy and no
`person.died` claim about its last holder.

## §3 Register and pointer text (edits; no behaviour)

One `[editorial]` commit. `engine/season/hole_register.yaml`: H-42, H-43, H-84 marked closed (the code
paths the first FI audit §6a cites); H-45 closed as rows with its residue named (`interview`,
`reconstruct`, `thread_read` have no product until §2 steps 9 and 10); H-116 as `08_FI_04` §5 words it.
Re-filings, as the register carries a lane: H-62, H-92 to CHAR; H-106 to IN; H-138 to SE with its cite
corrected (`_eff_transfer` is not in `effects_information.py`); H-217, H-219, H-279, H-285, H-295, H-299,
H-301, H-302, H-335, H-336 to SC or FA as the first FI audit lists them; H-325 to SE. H-182's text is
replaced by `08_FI_08`'s correction (the effect was built and reverted; it waits on rumour traffic).

A reading rule, recorded where a builder will look (the note of the corpus loader,
`engine/season/harness/run_cases.py`, one sentence): where a case file cites an archived fieldwork term,
the parent `fieldwork_v30.md` is the reading of that term, and nothing is built from it without a new
design (`08_FI_audit_addendum_B.md` F-FI-13, R-47). Gate: `register --requirements` exits 0.

## §4 Two items the evidence interface left to SC, closed (addendum E-9, E-10)

- **Precedent as a proof kind:** no fifth member of `rosters.yaml: proofs`. A prior finding is a Record
  (the `resolution` kind, plan CR-36/37) and is cited as `record`; `05_SC_evidence_and_rebuttal_B.md`'s
  `bears_on` column may then say it bears on `definition`. Waits on CR-36/37.
- **The opponent's own word:** no new kind. A held claim of his `commitment.made` is `testimony`; set
  against his plea it is an ordinary contradiction (EVID rule 2).
- **A judge whom evidence moves more or less:** `02_CHAR_which_ground_moves_whom.md` (the `moved_by_*`
  traits as `edge` rows of `capability_uses`, on the leverage channel); `05_SC_capability_surface.md` edit 3
  is superseded into those rows and its edit 4 (the believed trait) stands.
- **The band ceiling for an unsupported case (E-9):** not built; it becomes worth building when a
  disposal's `degree` has a reader, which `05_SC_arrangement_rows_that_bind.md` supplies. Recorded so the
  next reader does not re-derive it.

## §5 The scene sink: the reading any fix must show (F-PES-FI-05)

The pessimist measured that `create_record` and `utter` hold about 550 to 625 of the acts carried out in
three seasons, and that with every information verb cut the realm marches 53 times for 29, moves 94 times
for 21 and determines three matters for none. The fix is the chooser's scoring and is another family's.
This lane fixes only the acceptance, so the claim cannot be made by writing: on `test_fi_arms.py`'s shape,
seed 0, three seasons, against the `draw1` control, a fix must show (a) acts carried out that are not
information verbs above the control's spread (367 and 332 today); (b) information Events answered by a
non-information act above 23; (c) `march`, `move` and `determine` counts reported beside both. A fix that
moves none of the three has not touched the sink.

## §6 The telling's slants, reconciled (C-14)

Three proposals touch `rosters.yaml: said_slants`. One roster text:

```yaml
said_slants:
  values: [newest, valence, unshared, unshared_first]
  # unshared:        excludes_kinds_of: [tell, lie]                      (08_FI_06 §5; the register's own follow-up, H-197)
  # unshared_first:  the same exclusion, plus prefers: [told, inferred, deed, quantity, other]
  #                  (08_FI_02 edit 2, with 16_PESSIMIST_FI_A edit 5's tiers: `deed` and `quantity` in place of `cell`)
```

`Fixtures.said_slant` is swept `newest` (control), `unshared`, `unshared_first`; it ships `unshared_first`
when §2 step 3's gate reads, and `valence` stays an arm. `08_FI_02` edits 2 to 4 are read with this text.

Two duplicates are carried once (C-15): `argument.held` at `argue`'s Partial is
`16_PESSIMIST_SC_D_an_argument_moves_someone.md` edit 1 (`08_FI_04` §1's row for it is withdrawn); reading a
`detain` or `ban` edge as its two ends is `16_PESSIMIST_SC_C_a_verdict_names_its_party.md` edit 1, which is
wider and carries the `patient_kinds` consequence (`08_FI_04` §3's second bullet is withdrawn).

## §7 The conclusion, in two acts (C-22; F-FI-03; R-27; LACUNA R-19-03 to R-19-05)

Three proposals grade `reconstruct` and have it mint a Proposition (`08_FI_03` §3,
`19_LACUNA_conclusion_is_a_committed_assertion.md`, `14_VERBS_MATERIAL_E_knowledge.md` §3). The loader
refuses that shape: a row on the graded route *"keys its emissions by Degree and writes nothing"*, and a
degree-keyed `writes:` with no `contests:` does not load (`engine/season/data/verbs.py:848-851`, `:870-874`;
`04` §B.13 invariant 12, §C.4). Giving the row a prize would make an inquiry a contest, which the tree
rules out (`rosters.yaml: inquiry_modules`, SM-3; the loader's own message: *"giving an inquiry a prize is
scripting drift"*). So the conclusion is two acts, both of which exist:

1. **`reconstruct` reasons.** `rosters.yaml: graded_tasks` (renamed from `graded_inquiries` in 18-A's
   commit, D-U1-11i) gains `reconstruct` (the existing route; it is an inquiry, writing nothing).
   Row: `writes: []`; `emits:` Overwhelming, Success, Partial `[conclusion.reached]`, Failure
   `[finding.none]`; `difficulty:` as `U5c_SC_one_obstacle_form.md` §4 gives the inquiries; leverage source
   `proofs`: one level per independent origin beyond the first among the claims it reasons from.
   The value space is `queries/person_q.py::concluded_of(ledger, subject, fx)`
   (`14_VERBS_MATERIAL_E` §3 item 1), carried on the act as `concluded`, choice-sourced where his ledger
   names several doers.
2. **Its product is a deposit to its maker.** At WITNESS the observation deposit lands one claim on the
   actor: `(the deed's counterparty or object, concluded:<deed kind>, doer)`, source `inferred`. What it shows
   is read off `rosters.yaml: finding_terms` by band, the table that already decides what a finding shows:
   Partial withholds the hand; Success names it; Overwhelming names it at full confidence. Nothing wrong
   is deposited by the roll (K-37): the doer is whoever his own ledger names.
3. **`utter` commits it.** `14_VERBS_SOCIAL2_B_a_word_with_content.md` §1 already makes `utter` say what
   the speaker holds. A `concluded:` claim is a held claim; uttered, it is a `HOLDS` Proposition naming
   the deed and the doer. The act carries `cites` (the claims `concluded_of` reasoned from), which
   `_eff_utter` stores as `Proposition.support` (`19_LACUNA_conclusion…` edit 1). `commit`, `petition`
   from the held Proposition (`terms_sourced`), and `record`'s pairing of a concluder
   (edit 4 (b), behind `record_concluders`) are unchanged.

Gate: `19_LACUNA_conclusion…`'s four gates, read with "a Proposition uttered after a winning
`reconstruct`" for "`reconstruct` deposits a Proposition"; plus the loader accepts the row (it refuses the
banded-`writes:` form: plant it and the import fails). Falsifier: a `concluded:` claim whose doer the
maker's ledger did not name at the act; an uttered conclusion with empty `support`. Hash: declared mover
wherever `reconstruct` folds. Lanes: FI (row, deposit), IN (the carrier field), CHAR (the chooser's
variants, `record`).

## §8 What a look teaches is read off one table (C-24; R-35; H-218)

Three statements: `08_FI_03` §2 (an `observes:` column, deposited at Partial or better), `08_FI_07` §2 (b)
(deposited at every band; the band gate dropped because a degree-keyed product column would be a second
owner of what a finding deposits), `14_VERBS_MATERIAL_E` §2 (the column keyed by degree). One rule:

1. `observes:` is a **flat list** per inquiry row of the non-gating reads that look takes (the table in
   `08_FI_03` §2). It names what is looked at, never a band.
2. **Which reads a band deposits is `rosters.yaml: finding_terms`'**, the one band-keyed table: at
   Overwhelming and Success every listed read; at Partial every listed read but `held_by`, with numeric
   values passed through the lossy-copy rule (`loop/witness.py::_told_value`); at Failure none.
3. **The gating reads** (the conjuncts of the row's own cell) are deposited to the actor at every band and
   on a refusal: plan CP-T06-04, unchanged.

So a failed look is not silence (he learns the thing is there and that he was where it is), the content
is behind the draw, and one table owns the band. The rows stay on the graded route and write nothing.
Gate: `08_FI_07` §2 (b)'s, with the Failure row reading *gating reads only*; `14_VERBS_MATERIAL_E` §5's
`research` gate unchanged. Falsifier: a `content:` claim deposited at Failure; a second band-keyed table
beside `finding_terms`.

## Layer 1 reading

§1: `decision/` still names no `World`; every referent about another person's state comes from the
asker's ledger (`04` PART D row 2; ED-IN-0292). §7 and §8: the graded route writes nothing and a deposit
is WITNESS's INTERIOR write into the holder's own ledger (`04` §A.2 row `loop/witness`; §B.13 invariant 12).
`Proposition.support` is set at construction on an immutable carrier (`04` §B.6) and has two named
readers (`record`, the board). Grades: MECHANICAL for the loader's refusal; CONVENTION for the may-read
reading of `questions_for` until `08_FI_01` edit 8's test lands, then MECHANICAL.

## Cost class

§1: small build (as its sources). §2 to §5: edit or none. §6: edit. §7, §8: small builds inside their
sources' batches.

**Lands it and tier.** The B11 batch (`methodology-execute`, in §2's order), an FI `valoria-author` session on
`sonnet` (`high`); one `methodology-close` with its terminal `opus` critique. **Hash movers.** §1 on every
realm world; §6 to §8 as their sources state (declared).
