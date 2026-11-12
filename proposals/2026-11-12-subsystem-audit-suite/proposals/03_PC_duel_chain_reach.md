# PC — make the duel chain formable: `challenge` on persons with a dispute, `accept` on challenge Records

## Status: PROPOSED

Lane: PC, with CORE (`decision/options.py` is CORE's file). Source: `audits/03_PC_audit.md` F-PC-01,
R-PC-06, R-PC-07, R-PC-08. Read at `601e715`. Reference only (CLAUDE.md §0.05); not ratified by being
written.

## What it changes in `engine/season/` at runtime

Which Candidates form. A person stops forming `challenge` on a referent that is not a person or
against whom he holds no dispute, and stops forming `accept` on a Record that is not a challenge. No
effect, band, write or draw changes. It is a declared hash mover wherever those Candidates formed.

## The problem, with evidence

`python -m engine.season.harness.aperture 2 s`, `PYTHONHASHSEED=0`, realm, two seasons:

| seed | `challenge` attempted / refused | last read at refusal | `accept` attempted / refused | last read | `fight` formed | deaths |
|---|---|---|---|---|---|---|
| 0 | 84 / 84 | `exists:Person=0` 65 · `with=False` 13 · `dispute=False` 6 | 27 / 27 | `exists:challenge=0` 27 | 0 | 0 |
| 1 | 105 / 105 | `exists:Person=0` 75 · `with=False` 22 · `dispute=False` 8 | 27 / 27 | `exists:challenge=0` 27 | 0 | 0 |

In the realm no challenge is issued, so no `challenge` Record exists, so `accept` cannot bind one and
the `duel` context of `rosters.yaml: violence_contexts` names nobody. The chain is dead at its head,
and persons spend more than a hundred scene acts a world on acts the fold must refuse. In the 143
case worlds (`python -m engine.season.harness.corpus_run`, seed 0) `challenge` is among the executed
verbs and `accept` is among the thirteen only ever refused, so the second link is dead there too.

Three causes, each at its owner:

1. `engine/season/verb_table.yaml:923-940`: the `challenge` row declares no `referent_class`, so it
   forms on the question's plain referents of any kind. Other person-targeted rows declare
   `referent_class: Person` (`verb_table.yaml:431`, `:1234`, `:1288`, `:1552`).
2. The `dispute` conjunct is evaluated only in the fold (the row's note: "WORLD-ONLY, so he forms the
   Candidate on anyone he knows and the fold refuses a challenge with no wrong behind it"). Its owner,
   `engine/season/queries/person_q.py:148-156` (`holds_dispute`), reads nothing but the actor's own
   ledger and pursuits, which the chooser may read (AX-2).
3. `accept` is classed `Record` (`verb_table.yaml:956-958`) and forms on held Records of other kinds;
   its own cell already says `existence … kind: challenge`. `comply` shows the same shape at the same
   instrument (33 refusals on `exists:dispensation=0` at seed 0), so the gap is general to
   Record-classed rows.

## The resolution, decided

1. Give `challenge` `referent_class: Person` (ladder rung 4, precedent: REM-28 classed `convene` and
   removed its wrong-kind formations).
2. Decline `challenge` person-side when the actor holds no dispute with the subject (rung 5: it is the
   actor's own knowledge; the fold's conjunct stays for a hand-built act).
3. A Record-classed row whose cell carries an `existence` conjunct with a `kind:` forms only on a
   Record of that kind (rung 4: the cell already states the kind; no new column).

Co-location stays world-only, as ruled for `fight` (IN-59): a man may form a challenge to someone who
turns out not to be where he is.

## Exact edits

| file (owner) | edit |
|---|---|
| `engine/season/verb_table.yaml`, row `challenge` | add `referent_class: Person` and a `referent_class_note` citing this file and REM-28 |
| `engine/season/rosters.yaml: violence_contexts` | add the line `challenge: [dispute]` |
| `engine/season/decision/options.py`, `VIOLENCE_CONTEXT_READERS` | add a reader `dispute`: `person_q.holds_dispute(p, subject, scar_shift)` over the person's own ledger. `[UNVERIFIED: this file was not opened; the closed set and its location are as `rosters.yaml:2749-2752` describes them]` |
| `engine/season/decision/options.py::opening_set` | for a row with `referent_class: Record` whose `requires_typed` has `form: existence, of: subject, kind: K` with `K` a record subkind, keep only referents whose Record is of kind `K`. One rule for `accept`, `comply` and any later row; the kind is read off the row's own cell |

Nothing in `modules/combat/`, the seam or the effects changes.

## Gate (execution artifact)

`aperture 2 s` for s = 0, 1, 2, before and after, quoted in the commit body:

- `challenge` refusals with last read `exists:Person` = 0 and `dispute=False` = 0;
- `accept` refusals with last read `exists:challenge=0` = 0 (and `comply`'s `exists:dispensation=0` = 0);
- the `ex` column of `challenge`, `accept` reported as measured, whatever it is.

## Falsifier

A seeded realm with one planted dispute (one deed claim in one person's ledger that his pursuits score
below zero, about a co-located person) produces, through the real chooser and with no hand-built act,
`challenge.issued`, then an `accept` by the challenged, then a fought scene under `blood` terms with
`duel.yielded`. If it does not, the chain has a further break and this proposal has not closed
F-PC-01. Planted failure: remove the `dispute` reader and the pre-change count of refused challenges
returns. Control: with the three edits reverted the pre-change hash is reproduced.

**Stated limit.** These edits remove formations that cannot succeed. They may leave the realm with
very few challenges, because few persons hold a dispute (6 and 8 passed the first two conjuncts at
seeds 0 and 1 and failed the third). Whether duels then occur depends on CHAR's deed judgement
(`deeds_judged`) and on CR-88's `grievance_against`; that is a dependency edge, not this proposal's
claim.

## NERS reading

- N: from below, the Record, the terms and the `blood` duel already exist and are unreachable; from
  above, R-05 counts `challenge` and `accept` as not built out while they execute 0 times; laterally,
  `comply` gains the same repair. Removing the change leaves all three as measured.
- R: adds no option; makes an existing one reachable and stops a person wasting his season. The
  no-player half gains its first route to a duel.
- S: one formation rule for every Record-classed row; the dispute is read by one owner in both places.
- E, last: three small edits against roughly 190 wasted acts a world over two seeds. High.

## Cost class

Edit (three data lines and two small reads in `opening_set`), plus one declared re-record of the
season pins that carry these formations.
