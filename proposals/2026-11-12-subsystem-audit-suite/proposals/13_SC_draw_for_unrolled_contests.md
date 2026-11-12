# SC — every contest draws: a roll for negotiation, questioning, docketing, the ballot and the appeal

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-07, C-11, C-12) — of the five rolls here, three yield and two stand. Negotiation: acceptance is not the offerer's roll; it is the accepter's own sampled `commit` (`05_SC_negotiation_scene.md`; `14_VERBS_SOCIAL1_B_documents_and_obedience.md` §3), because one person's roll cannot open another's edge (`04` D-10a). Questioning: the `interview` row is `14_VERBS_SOCIAL2_C_case_question_confession.md` §3's. Docketing: `carry`'s draw is `14_VERBS_SOCIAL1_D_grievance_and_settlement.md` §1's, and `open_case` on one's own bench is a remit act and is not drawn. The ballot stands, owned by the hearing's close (edits 3 and 4 yield to `U5c_SC_proceedings_residue.md` §6; Jordan, A-14). The appeal stands as `19_LACUNA_verdict_ladder_and_reversal.md`'s, on new grounds only (A-39).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.4 row (VIOLATES for `carry`/`open_case`), §2 row A-81, §7; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-02, D-U1-07, D-U1-11i, ledger C-04; `unified/U3_CONFLICT_LEDGER.md` C3-R1, C3-C11, C3-C13, §9; `unified/U3_DEPENDENCY_ORDER.md` node B07). The body is brought to the head: every one of the five rolls is carried by its owner, so the resolution table and the exact edits (which used loader keys that do not exist, `emits_by_degree`/`writes_by_degree`, put a docketing write on a graded route that the loader refuses, `data/verbs.py:872-876`, `audits/25_GROUNDING_ENGINE.md` G-01, and read the half-score opposition and a subtracted regard) are removed and replaced by a pointer table; the standing rule, the "outside this lane" list and an integration check stand. The `verb_capability` rows become the verb-row column's (U1 §5) and are each owner's. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "graded route" → "task route" (glossary *task*).

**Lands in batch:** no code of its own (node B07 kept for the order). Its check is read once, at the close of B28, the last batch that carries one of the five. **Depends on:** `05_SC_negotiation_scene.md` (B24), `14_VERBS_SOCIAL2_C_case_question_confession.md` §3 (B25), `19_LACUNA_verdict_ladder_and_reversal.md` (B27), `U5c_SC_proceedings_residue.md` §6 (B27), `14_VERBS_SOCIAL1_D_grievance_and_settlement.md` §1 (B28), `18_DETERMINISM_task_draw_for_uncontested_verbs.md` item 4 (B07; the loader edit any graded-route row with writes needs, C3-R1).

## Status: PROPOSED — a pointer file: each of its five rolls is carried by the owner named below

Written by the contest-interrogation lane (`audits/13_SC_contest_interrogation.md` §4 cells 8–11, §8
R-7, R-8) under the standing rule Jordan set on 2026-11-12 (`AUDIT_BRIEF.md`, *"We do not do
deterministic!!!!!"*): every consequential outcome resolves by a draw with a graded, recoverable result;
state sets the odds, the draw sets the outcome. Ratifies nothing; reference under `CLAUDE.md` §0.05.

## What it changes in `engine/season/` at runtime

Five contest types that resolve today as a fixed function of state get the one social roll
(`modules/social_contest/roll.py`), through routes the tree already has, with band maps on their verb
rows. Every act of these verbs that executes today now draws and can come out four ways. A declared
mover for every world in which they execute (in the realm: `petition`, `carry`, `open_case` and
`interview` execute every season; `covenant` is formed and only refused today, so its draw is reached
once the refusal is cleared by the SOCIAL verb lanes). Eligibility and `requires:` stay checks: who may
attempt the act is unchanged.

## The problem, with evidence

1. **Negotiation.** `covenant` (`verb_table.yaml`: `stratum: social`, no `contests:`) offers terms and
   emits `covenant.offered`; acceptance is not resolved at all, and `exchange` is uncontested. The
   `negotiation` arrangement row (`disposal: mutual`) is read by no roll (audit §1.1).
2. **Questioning.** `interview` (`own`, uncontested) emits `finding.made` with no resistance from the
   witness; `interrogate`, the bench's questioning, rolls (audit §1.2, degenerate cell 8).
3. **Docketing.** `petition` mints a Record and `carry` / `open_case` put a matter on the docket with
   certainty (SC audit §1); whether a room takes up a matter could go either way and never does.
4. **The ballot.** On a `disposal: declared` row the outcome is `world_q.declared_votes`: a count of live
   commits — a verdict by count.
5. **The appeal.** Four arrangement rows carry `appeal_basis: determine`; no verb reads the column, so a
   verdict is final by construction.

Each is a thing that could go either way for the people in the fiction, and each is decided by state
alone.

## The resolution, decided

One roll, one composition (`U5c_SC_one_obstacle_form.md`: the even line, difficulty, `opposed_ob` on the
skill score, hostile terms; what a party brings is leverage), routed by what exists. Each contest has one
owner; this file states the rule and checks that all five draw.

| contest | owner (the file that carries the row and the edit) | route and form, as the owner decides it |
|---|---|---|
| negotiation | `05_SC_negotiation_scene.md`; `14_VERBS_SOCIAL1_B_documents_and_obedience.md` §3 | acceptance is the accepter's own sampled `commit` (C-07: one person's roll cannot open another's edge, `04` PART D row 10a); covenants are made in person (A-21) |
| questioning | `14_VERBS_SOCIAL2_C_case_question_confession.md` §3 (the `interview` row); `19_LACUNA_questioning_has_an_approach_and_a_cost.md` (the approach) | `interview` contests a prize against the witness; the witness's skill score opposes (A-79); `interview` engages the interviewee's scene (A-63; C3-C13) |
| docketing | `14_VERBS_SOCIAL1_D_grievance_and_settlement.md` §1 (`carry`) | `carry`'s draw is that file's; `open_case` on one's own bench is a remit act and is not drawn. A docketing write on a task route needs 18-A's loader edit (C3-R1) |
| the ballot | `U5c_SC_proceedings_residue.md` §6 (the hearing's close); A-14 | each vote is a draw on the voter inside the presiding person's act; the `lean` leverage source (OBS §3); `ballots` default 1 |
| appeal | `19_LACUNA_verdict_ladder_and_reversal.md` | on new grounds only (A-39); the appellate bench writes `reversed`; the disposing seat's bench closes the edge by its own `pardon` |

Two rules hold across the table:

- **The draw sets the outcome; the counterparty's choice sets whether there is a contest.** A
  counterparty may still decline to negotiate (not answer), which is his act formed by the chooser; an
  offer once made resolves by the draw. This keeps the person-side decision (CHAR's chooser, AX-2) and
  removes the deterministic acceptance.
- **Evidence and pursuit costs reach the draw, never as a gate.** A hostile cost is an obstacle term; a
  cited item is leverage (`proofs`, A-25); neither fixes the band (the standing rule's *"not 'evidence
  enters when presented'"*).
- **Every band writes something readable (A-81).** A Failure band names its durable write: a witnessed
  Failure Event deposits a claim to those present, a solitary act deposits the actor's own claim of the
  failure (C3-C11). Each owner states it at its row.

### Outside this lane, listed for the owning lanes

- The binding acts (`issue`, `confer`, `revoke`, `pardon`, `release`, `surrender`, `establish`): *"a decree
  binds"* is the rule's own case — `audits/14_VERBS_BINDING.md` / the INSTITUTIONS brief.
- `comply`, `evade / defy`, `construe`, `conceal`: `audits/14_VERBS_SOCIAL1.md` / `SOCIAL2.md`.
- SC's played hearing: *present* and *answer* (`05_SC_playable_hearing_B.md`, `05_SC_evidence_and_rebuttal_B.md`,
  `19_LACUNA_admission_rides_the_citing_draw.md`): `answer` is a rolled move (D-02), entry rides the citing
  draw.

## Exact edits, by owner

None here: each edit is its owner's (table above). Removed from this file (superseded): the `covenant`
`contests:` row, the `interview` row (S2_C §3's), `carry`/`open_case` on the task route, the ballot loop
and `world_q.declared_votes`'s per-member count (proceedings residue §6's), the appeal row (LACUNA's), and the
`verb_capability` rows (the verb-row `capability:` column, U1 §5, each owner's).

## Gate (execution artifacts)

- Exact: for each new row, `odds_of` mode (a) on a planted act returns four non-zero-sum bands, and
  no cell of the audit's planted grid gives P(Failure) 0 or 1.
- Realm, `build_realm(0)` and `(1)`, two seasons, `PYTHONHASHSEED=0`, after B28: rolls occur for
  `interview` and `carry` (read from SC-P1's record; the absent scratch `realm_tap.py` is restated as
  `engine/season/tests/test_sc_calibration_targets.py::test_every_rolled_verb_with_five_rolls_shows_more_than_two_obstacles`
  and, for this file, `engine/season/tests/test_every_contest_draws.py::test_five_contest_types_each_take_more_than_one_value`).
- A planted `declared` sitting of five members with commits 3 for / 2 against, run at 200 seeds: the
  matter carries in some seeds and fails in others (the count is not the verdict).
- Determinism: same seed, same hash, twice.

## Falsifier

Any of the five contest types whose outcome, over 200 seeds of one planted state, takes a single value.

## NERS reading

- **N**: a negotiation that can be won or lost, a witness who may or may not talk, a court that may not
  take the case, a vote that can surprise and a verdict that can be overturned: remove the draw and each
  is a script.
- **R**: the no-player half gains five sources of reversal; every outcome is graded (Partial gives a
  counter-offer, a delayed hearing, a half-finding), so failure is recoverable rather than a dead end.
- **S**: one roll, one ladder, one obstacle composition; the ballot is many draws of the same kind, not a
  second resolver; eligibility stays a check everywhere, as for every other verb.
- **E** (last): five band maps and two routes that already exist, against five contest types that become
  legible as chances with reasons.

## Cost class

None of its own (each owner's cost class governs). The integration test is an edit.

**Lands it and tier.** The test `test_every_contest_draws.py` is written in the B28 batch after its last
owner lands, `sonnet` (`high`, `valoria-author`), read at B28's `methodology-close`. **Hash movers.** None of
its own.
