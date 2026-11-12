# PC — make the duel chain formable: `challenge` on persons with a dispute, `accept` on challenge Records

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` §1.1) — three additions; no edit below is withdrawn. (1) The falsifier's second link (*an `accept` by the challenged*) needs a delivery this file does not build: the challenged forms `accept` on a challenge **addressed to him and heard of** (`14_VERBS_PHYSICAL_A_custody_and_force.md` A4), and that file's A3 drops `duel` from `fight`'s contexts (a challenger may not attack on his own unaccepted challenge), so A4 lands with or before A3. A-21 keeps a challenge in person, which the row's `with` conjunct already asks. (2) A challenge unanswered by its due tick emits `challenge.declined` (U5c's reconciliation of the SOCIAL verbs, its C-27); declining is a judged deed, not a dead end. (3) A-16 (a person may, rarely, try to kill of his own motive) adds an occasion outside this chain: `22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md` (U5d's) is its carrier and `U5b_PC_rulings_in_the_fight.md` §6 the opener's edge; neither changes an edit here.

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §1.1 (CONFORMS; the `[UNVERIFIED]` mark on edit 3 settled by `audits/25_GROUNDING_ENGINE.md` V-13 and re-read at the tree), 7b-1 (tests, call sites, lands-it; its call-site sentence corrected at the tree: the one production caller of `opening_set` is `decision/choose.py:541`, not `harness/play_surface.py`), 7b-19 (tier); `U3_DEPENDENCY_ORDER.md` node row and §4.1 row 0 (batch B01, the edge to `14_VERBS_PHYSICAL_A` cut as LANDED), `U3_CONFLICT_LEDGER.md` C3-A1/C3-A2 (lane A's branch built this; B01 rebases it). Added: `Depends on:` / `Lands in batch:` lines and an "Implementation" section. No edit or finding above is withdrawn. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "fought scene" → "fight" (glossary *scene*).

**Depends on:** nothing unlanded in this suite (U3 §4.1 row 0: implementation lane A's `e5d6ab9` already built the reach on its branch; `14_VERBS_PHYSICAL_A_custody_and_force.md` A4 then A3 follow it, B14/B15). Precondition: Jordan's permission to push lane A's branch (`unified/U3_JORDAN_CALLS.md` P-1, pending).
**Lands in batch:** B01 (`B01-laneA`, IN lane): the rebase of `e5d6ab9` + `c5bf18a` onto the working tree (C3-A2), with the H-id renumbering of C3-A1.

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
| `engine/season/decision/options.py`, `VIOLENCE_CONTEXT_READERS` | add a reader `dispute`: `person_q.holds_dispute(p, subject, scar_shift)` over the person's own ledger. Location verified (`audits/25_GROUNDING_ENGINE.md` V-13; re-read at the working tree 2026-11-12: `VIOLENCE_CONTEXT_READERS` is the dict at `decision/options.py:437`, filled by the decorator at `:444`, read at `:503`, cross-checked against `rosters.yaml: violence_contexts` at `:507-510`; `holds_dispute` at `queries/person_q.py:148`) |
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
`challenge.issued`, then an `accept` by the challenged, then a fight under `blood` terms with
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

## Implementation (test 9; `R1_READ.md` 7b-1, checked against the tree)

- **Order of edits.** (1) `verb_table.yaml` `challenge` row; (2) `rosters.yaml: violence_contexts` line and the
  `dispute` reader in `decision/options.py` (one commit: the loader cross-check at `options.py:507-510` refuses a
  roster member with no reader, so the two land together); (3) the `opening_set` kind filter.
- **Call sites.** The edits are internal to `opening_set` (`decision/options.py:63`) and `VIOLENCE_CONTEXT_READERS`.
  Production caller: `decision/choose.py:541` (unchanged). Harness callers that read the new formations without
  edit: `harness/aperture.py:534`, `:545`, `harness/corpus_run.py:1118`, `harness/probes.py`, `harness/decision_spread.py:388`.
- **Tests.** New file `engine/season/tests/test_duel_chain_reach.py`: `test_challenge_forms_only_on_a_person_with_a_held_dispute`
  (hand-built world, one person holding a deed claim his pursuits score below zero, a second person co-located; the
  Candidate set holds `challenge` on him and on no one else; `assert checked >= 2`),
  `test_accept_forms_only_on_a_challenge_record` (a `dispensation` and a `challenge` Record held; `accept` forms on the
  challenge only), `test_comply_forms_only_on_a_dispensation_record`, and
  `test_realm_challenge_refusals_with_exists_person_zero_are_zero` (`aperture 2 s`, s = 0..2 parsed; planted control:
  revert edit 1 and the count returns). The covering files `test_cp_t03_01_cohorts_never_fight.py` and
  `test_interactions_log.py` read `violence_contexts` and stay unchanged.
- **Gate** as above (`aperture 2 s`, s = 0, 1, 2, before and after, in the commit body); on lane A's branch it is
  re-run after the B01 rebase (C3-A2).
- **Hash movers.** Every seeded pin where `challenge`, `accept` or `comply` formed (declared above); recorded once at
  B01's close.
- **Lands:** an IN-lane implementation session under `/methodology-execute` with PC review (CLAUDE.md §9); edit class,
  `sonnet`.
