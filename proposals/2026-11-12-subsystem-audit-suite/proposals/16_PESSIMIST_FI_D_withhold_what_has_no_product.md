# 16 · PESSIMIST · FI · D — Withhold the three inquiry rows that have no product, until they have one

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §1 (CONFORMS: a withheld verb forms no
Candidate, so `04` §B.13 inv. 4 is not engaged), §2 (A-81: the three rows are in the measured gap, "the 53 owed a draw";
withholding is the interim and each product proposal gives its row a graded band with a write), §7/§7b (R-05 opened at
the tree, the gate on a committed test and `aperture`, tier); U3 B26, §6.2 (`fi_arms.py`, `p5_crime.py` are not in the
repository). Changed: edit 2's basis (the row was read), the gate.

## Status: PROPOSED

Lands in batch: **B26** (FI; the fixture is IN's file). Depends on: `08_FI_03_playable-inquiry.md` and
`19_LACUNA_conclusion_is_a_committed_assertion.md` (B11), which name the products; CP-T06-05 and B10-15 (plan positions,
MISSING as code until v12 disposes them) for `interview` and `thread_read`.

**A-81.** Every scene writes a durable change. The three rows as formed write nothing and grade nothing (a
`finding.made` claim of the actor's own admission, which cannot fail): withholding them from formation removes 157
still scenes from a seeded realm. Each product proposal's change that removes its row from `withheld_verbs` must give
the row a graded band with a write in the same change (A-81 consequence 2), or the row stays withheld.

Carries `audits/16_PESSIMIST_FI.md` F-PES-FI-05 (the part with a clear owner) and F-PES-FI-11 (two of
its fixed outcomes). It is the formation half of the first FI audit's sentence on `reconstruct`,
`interview` and `thread_read` (*"each needs a product or to leave formation"*, `08_FI_audit.md` §5),
which no proposal carries.

## What this changes in `engine/season/` at runtime

`interview`, `reconstruct` and `thread_read` form no Candidate for anybody at the shipped fixtures.
Their rows, effects and hand-built acts are untouched. Declared hash mover for every seeded realm
(the three rows are 157 of 1,394 acts carried out at seed 0 over three seasons).

## The problem, with evidence

- The three rows carry no `contests:`, no `graded_inquiries` route, no bands and no `writes:`
  (`engine/season/verb_table.yaml`). Once admitted they emit `finding.made` with certainty:
  `p5_crime.py`, 40 `interview` acts and 40 `reconstruct` acts, 40 of 40 each, and the actor then
  holds `(subject, finding.made, True)` and nothing about the subject. Under the standing rule
  (`AUDIT_BRIEF.md`, *we do not do deterministic*) a finding that cannot fail and finds nothing is two
  defects in one row.
- In the shipped realm (seed 0, three seasons): `interview` 37, `reconstruct` 117, `thread_read` 3.
- **The cut, run** (`fi_arms.py 0 3 nod3`: the three verbs removed from the chooser's set, which is
  what `withheld_verbs` does one layer down; control `draw1`, the chooser's draw seed changed):

  | | `ship` | `draw1` (control) | `nod3` |
  |---|---|---|---|
  | acts carried out | 1,394 | 1,465 | 1,410 |
  | an information Event answered by a non-information act | 16 | 23 | 14 |
  | seats, deaths, site conditions, stores total against `ship` | — | 1 seat, 1 death | none |
  | `create_record` + `utter` | 549 | 613 | 625 |
  | `research` | 128 | 159 | 160 |
  | `march` | 29 | 14 | 39 |

  Nothing that happens with the three rows present fails to happen without them. The cut is free.

## Resolution, decided

The three rows ship withheld from formation until each has its product, and each product's own
proposal removes its row from the list in the same change:
`interview` when the person questioned answers by his own act (CP-T06-05, scheduled);
`reconstruct` when it states a conclusion (`08_FI_03` §3 as amended by
`19_LACUNA_conclusion_is_a_committed_assertion.md`); `thread_read` when it reads a bond or a hazard
(B10-15).

Ladder: step 4. `marshal`, `surrender`, `destroy_record` and the four army verbs ship withheld for
the same reason and by the same fixture (`data/fixtures.py`, `withheld_verbs`, H-156; the hole
register's `site:` text for it: *"a member forms no Candidate for anybody"*); `verb_table.yaml:1116`
gives the ground in one line (*"Ships WITHHELD (`Fixtures withheld_verbs`, `marshal`'s precedent):
formable, it moves every seeded season"*). No new mechanism.

## Edits, by owner

1. **`engine/season/data/fixtures.py`, `withheld_verbs`**: the shipped tuple gains `"interview"`,
   `"reconstruct"`, `"thread_read"`. The sweep comment gains the arm without them as the control (it
   is today's behaviour).
2. **`engine/season/requirements.yaml`, R-05's `measured:` text**: the three rows are named as
   withheld, with the product each waits on, so the row does not count them as verbs "built out on
   execution" (the phrase is the first FI audit's reading of the row, F-FI-03). Read 2026-11-12:
   `requirements.yaml` R-05 (`:926`) is `status: not_met` and its `measured:` text counts executing verbs
   ("13 of 38 AS OF 2026-09-20"); the sentence added names the three rows as withheld, beside that count.
   Text only; the row's status is unchanged by this proposal.
3. **The three product proposals named above** each carry one more line: remove the row from
   `withheld_verbs`, in the same change that gives the row a graded band with a write (A-81).

## Not edited here, named for the orchestrator

**The sink is not these three rows.** `audits/16_PESSIMIST_FI.md` §1.2 (N-2 decomposed): with every
information verb cut (`nofi`) the realm marches 53 times for 29, moves 94 times for 21 and carries
`determine` through three times for none; with only the inquiry rows cut (`noinq`) it does not. The
scenes are held by `create_record` and `utter`, about 550 to 625 acts in three seasons in every arm
that has them, with `commit` following (95 to 180). What a scene is spent on is the chooser's scoring
(`decision/choose.py`, `decision/budget.py`) and the question projection that occasions the acts
(`queries/world_q.py::questions_for`: the GAME lane read `stores.changed → create_record` and
`yield.taken → create_record` as the realm's commonest answers). That is CHAR's and CORE's surface;
this lane measured it and does not author it.

## Gate (execution artifact)

Committed: NEW `engine/season/tests/test_withheld_inquiry_rows.py`: `test_three_rows_form_no_candidate`,
`test_hand_built_interview_and_reconstruct_still_execute` (the rows are not deleted). Command:
`python -m pytest engine/season/tests/test_withheld_inquiry_rows.py -q`; then
`python -m engine.season.harness.aperture` at seeds 0-2: the three verbs attempted 0 times (expected reading), and
`report` / `delta HEAD` moving every seeded realm once (declared). `fi_arms.py` was lane scratch (not in the
repository); its census comparison, once committed as an `aperture` arm, is:

`fi_arms.py 0 3 ship` after the edit reproduces `nod3`'s per-verb census for every verb (the same
candidates are removed one layer down; a difference is a finding about `opening_set`'s read of the
fixture), and at seeds 1 and 2 the three rows are attempted 0 times. `p5_crime.py`'s hand-built
`interview` and `reconstruct` still execute (the rows are not deleted).

## Falsifier

After the edit, a seeded realm run in which an act that the shipped arm carried out, and that was
caused (through `causes[]`) by one of the three rows' `finding.made` Events, has no counterpart: that
would be a possibility the cut lost. This lane did not split `finding.made` antecedents by the row
that emitted them `[UNVERIFIED]`; pooled over every information Event, the non-information answers by
another person are 16 in `ship` and 14 under the cut, against 23 in the control.

## NERS reading

N: the rows as formed have no N-line (disqualifier 2, no producer of any possibility: nothing is
written, deposited or graded). The *verbs* keep theirs for the day they have products, which is why
the rows stay and only formation leaves. R: a seat that resolves identically every time and emits
nothing another person answers is a dead seat; withholding it removes 157 such resolutions. S:
`finding.made` stops meaning "was admitted" in play (H-318's ambiguity is not exercised). E, last:
three strings in one tuple; the vocabulary a seeded run uses is three verbs shorter.

## Cost class

Edit. Lane FI (the fixture is IN's file; the rows are FI's). Tier: `sonnet`, effort `high`. Hash movers
declared: every seeded realm (157 of 1,394 acts at seed 0); one re-pin in B26. Lands it: B26, after
`16_PESSIMIST_FI_B`; order 1 → 2, then the test.
