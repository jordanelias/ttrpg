# 14 · VERBS · SOCIAL2 · A — formation on what the person can know: a docket class, a Record sub-kind, a present subject

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-19, C-28) — edit 2 (`Record.<kind>`): `_stamped` carries both pairs, the bare `Record` and the qualified one, so `research` and `seize` still form (`research` was missing from this file's list of bare-`Record` rows, `audits/14_VERBS_MATERIAL.md` §17.2); it lands as one commit across families. §4 reads `person_q.present_persons`.

## Status: PROPOSED

Carries `audits/14_VERBS_SOCIAL2.md` §3 (`open_case` formation), §4 (`construe` formation), §5 (`speak`
formation), §6 (`tell` formation, adopted from FI-02), §7 (`interview` formation). Batch S2-A.

## What this changes in `engine/season/` at runtime

Fewer Candidates, and the ones removed are those the fold refuses for a reason the actor could have read:
`speak` on a matter that is not docketed, `open_case` on a matter already docketed, `construe` on a
document that is no writ, `interview` of a rung, a Record or a Proposition, and of a person not present.
A declared hash mover in every world (the refusal Events and their WITNESS deposits stop). Nothing new
executes that could not before; executions must not fall (the gate).

## The problem (evidence)

`aperture 1 0` and the three-seed probe (`audits/14_VERBS_SOCIAL2.md` §0.3, §12 of that file's sources):
`speak` 7 of 8 attempts refused `exists:DocketItem=0`; `open_case` 3 of 11 refused on the `write`
clause, the matter already docketed (`queries/world_q.py:418-426` names this as limit 3 of
`docket_question`); `construe` 4 of 4 on a non-dispensation (`faction_sheet`, `cover`, `petition`,
`text` across seeds, while 8–15 writs exist), because the `Record` class is one class shared by every held
kind (`rosters.yaml: referent_classes`, REM-25 note); `interview` 14 of 19 on a non-person, one
self-interview at seed 1. The same sub-kind defect produces `comply` 16 and `evade / defy` 1 wrong-kind
refusals in the same run (`aperture`, WRONG KIND AT ADMISSION: `record_subkind`).

## The resolution, decided

The partition `Question.classes` already exists to carry a world fact the chooser cannot read as a
classed referent (`state/carriers.py::Question`, IN-53 D1; an id may be both plain and classed). Use it
three times; add no mechanism. Ladder: step 4 (`petition`'s and `open_case`'s `Person` class, REM-24 and
CP-T05-04, which removed exactly the wrong-kind formations; `interrogate`'s `Detainee` class, H-232's
named shape), step 5 for the rest.

## Exact edits, by owner

1. **A docket class.**
   - `engine/season/rosters.yaml: referent_classes` gains `Matter`: *a matter on the docket the person saw
     docketed or was asked to sit on; stamped by `docket_question` and the sitting question; the
     referent's id is the party (a person), so `determine`'s `party` conjunct reads it unchanged.*
   - `engine/season/queries/world_q.py::docket_question` and the sitting-question loop in
     `questions_for` (`:4180-4185`): carry the matters as `classes` `(m, "Matter")` **instead of** plain
     `referents` (the Question keeps `about`; `referents` is `()` for these two questions). The docstring's
     limits (2) and (3) are deleted as resolved; the REVERT line becomes: *restore plain referents and
     delete the two `referent_class: Matter` columns*.
   - `engine/season/verb_table.yaml` `speak` and `determine`: `referent_class: Matter`, with a note citing
     this proposal and the measurement. `speak`'s `subject_may_be_self` is unchanged (the accused's own
     docket question carries himself as `Matter`).
   - Consequence: `open_case` (class `Person`) no longer forms on a docketed matter, because
     `own_referents_of_class` stamps a question's plain referents only `[UNVERIFIED: read the function at
     :3714 before landing; if it also walks `classes`, exclude `Matter` there]`.
2. **A Record sub-kind class.**
   - `rosters.yaml: referent_classes`: the `Record` class is qualified: `Record.<kind>`, `<kind>` a
     `record_kinds` member. Authored on the row (data a designer reads), validated by
     `engine/season/data/verbs.py` at load: the qualifier must equal the kind the row's typed
     `existence(subject, <kind>)` cell names (a row without such a cell may not qualify).
   - `queries/world_q.py::_stamped` stamps a Record id as `Record.<its kind>` (the World answers the kind;
     `opening_set` still never asks, L2).
   - `verb_table.yaml`: `construe` `referent_class: Record.dispensation`. **The same edit, in the same
     commit, on every row that declares `Record` today** (`comply`, `evade / defy` →
     `Record.dispensation`; `accept` → `Record.challenge`; `carry` → `Record.petition`; `found`, `build` →
     `Record.works`), because once `_stamped` qualifies the class a row still declaring bare `Record`
     forms on nothing. Those rows belong to other families; this landing is one commit or none.
   - `data/verbs.py::RECORD_REFERENT_KINDS` and `HOLDING_RECORD_KINDS` become readings of the qualifiers
     (one owner) rather than derivations from the typed cells.
3. **`open_case`.** No row edit: edit 1 removes its docketed formations.
4. **`tell`.** Adopt `08_FI_02_rumour-that-travels.md` edit 5 (`person_q.present_persons`, the
   `telling_hearers` fixture) as this row's formation. No second edit here.
5. **`interview`.**
   - `verb_table.yaml` `interview`: `referent_class: Person`; `counterparty: subject` (the existing
     person-side self decline, `opening_set` `:346-353`); `requires_typed: {all: [{form: existence, of:
     subject, kind: Person}, {form: relation, of: subject, relation: with, conjunct: present}]}`;
     `emits_on_refusal: {present: [interview.refused], …}` (S2-C renames the kinds; until then
     `finding.none`).
   - `decision/options.py::opening_set`: a row whose typed cell carries a `relation: with` conjunct on
     `subject` forms only on subjects in `person_q.present_persons(p.ledger, p.id)` under the
     `telling_hearers: seen_since_move` arm (FI-02's reader and fixture; at `known`, today's behaviour).
     Read off the row's cell, never the verb name.

## Order of landing

FI-02 edit 5 (the reader) → edit 5 here → edits 1 and 2 (independent; edit 2 is one commit across
families) → the gate.

## Gate (execution artifact)

`build_realm(s)`, s = 0, 1, 2, one season, `PYTHONHASHSEED=0`, read by `aperture 1 s` and the family probe
(`scratchpad/runs/VERBS_SOCIAL2/probe_state.py`):
- refusals 0 for: `speak` on `exists:DocketItem=0`; `open_case` on clause `write`; `construe`, `comply`,
  `evade / defy` on `record_subkind`; `interview` on `exists:Person=0`, and self-subject 0.
- executions of `speak`, `open_case`, `interview`, `comply` not lower than the baseline (1/5/4; 6/8/5;
  5/3/5; 0) at each seed. A fall is the stopping rule (CP-T05-04's AM-A-09 rule): revert that edit.
- Control: the pre-edit tree's hashes at the three seeds (5ab73af282d0, aa58ef0b71c9, a21ab6e12e35 from
  the probe).

## Falsifier

A hand-built world with one docketed party P and one undocketed person Q, both known to a seat-holder:
`speak` forms on P and not on Q; `open_case` forms on Q and not on P; a writ and a faction sheet held by
one person: `construe` forms on the writ alone. If any of these forms on the other, the partition is not
carrying the class.

## NERS reading

N: these formations are scene tax with no story; removing them returns scenes to acts that can happen
(top-down the verb's meaning; bottom-up the partition exists; lateral the same fix three rows already
took). R: no choice is lost that the person could have made knowingly; the epistemic refusals (a seat's
reach, a hearer who moved this round) stay. S: one partition, one stamp site. E, last: two roster values
and column edits, against 25–30 refused acts a season.

## Cost class

Edit (1, 3, 5 after FI-02) and small build (2, cross-family, one commit).
