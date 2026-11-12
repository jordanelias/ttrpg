# 16 · PESSIMIST · CORE — a refusal is remembered: the person weighs what he has already been refused

## Status: PROPOSED

Carries F-PES-CORE-01 of `audits/16_PESSIMIST_CORE.md` (§1.3, §1.6). Reference only (CLAUDE.md §0.05).

## What it changes in `engine/season/` at runtime (first)

`decision/choose.py::score_terms` multiplies a Candidate's pursuit term by one more factor, the person's
believed chance that the act is **admitted at all**, read from his own ledger: he discounts an
opportunity he holds a firsthand claim of having been refused, until that claim fades or newer news of
its subject lands. No fold, effect, predicate, verb row or witness rule changes. At the control value of
the new fixture (`0.0`) every content hash is today's.

## The problem (evidence; seed 0, shipped realm, shipped chooser, no player)

- 828 of 1,487 individuals' acts in three seasons are refused (56%); the share does not fall by season
  (47%, 61%, 58%). 41% of refused opportunities are attempted again by the same person; the retry is
  refused again 328 times in 342. An executed act's opportunity is re-attempted 21% of the time: a
  refusal makes a second attempt **more** likely. (`run_dump.py 0 3`, `an1.py`.)
- The design already has a teaching channel (the fold's reads ride the refusal as `Event.observed`,
  WITNESS deposits them, `opening_set` clause 4 declines what the person knows to be false), and it works
  where it is wired: refusals whose failing read is deposited are retried 8% of the time. 62% of refusals
  are outside it (a world-only stem, chiefly `with`, which `loop/witness.py:780-790` rules is *"observed,
  never deposited"*; or a cause that is not among the fold's reads). Those are retried 57% of the time
  and fail 96% of the time. (`p34.py 0 2`.)
- **The person already holds the lesson.** In season 0, for 184 of 226 refused acts the actor's ledger
  holds a firsthand claim `(subject = the act's subject, predicate = the row's refusal kind, doer =
  himself)` (`refclaim.py`; the other 42 are fieldwork kinds on `undeposited_kinds`). Nothing in
  `decision/` reads it (`grep -i refus engine/season/decision/*.py`: no reader of a held refusal claim).
- Sibling inconsistency (NERS-S): `odds_weight` already weights a contested Candidate by the believed
  chance of its bands. Nothing weights any Candidate by the believed chance of admission, though
  admission alone decides 13 verbs (GAME §1.3).

## The resolution, decided

A refusal is evidence about the odds, and it is weighed, not obeyed. The person does not learn *why*
(the `with` ruling, ED-IN-0282, stands untouched: no `with:` claim is deposited); he learns *that he tried
this and could not*, which the ledger has stored all along.

Not chosen, and why: **(a)** recording a refused opportunity in the driver's `_realised` set so it cannot
re-form that season. That is a fixed outcome of state (the standing rule: *we do not do deterministic*),
it closes the retry channel `driver.py:508-518` keeps open on purpose, and it puts a person-side rule in
the driver. **(b)** depositing the `with` read. Ruled out by ED-IN-0282 for the reason
`witness.py:780-790` gives.

## Exact edits, by owner

1. **`engine/season/queries/person_q.py`** (the single owner of ledger reads) — new reader:

   ```python
   def refused_before(ledger, holder: str, kinds: tuple, subject: str) -> int:
       """The present confidence (0..confidence_default) of the NEWEST firsthand claim in which
       `holder` was himself refused this opportunity -- predicate in `kinds` (the verb row's
       `emits_on_refusal`), subject `subject`, `doer == holder` -- or 0 when there is none, or when
       he holds ANY newer claim about `subject` (news of the subject supersedes the memory: the
       thing may have changed)."""
   ```

   Own ledger only (AX-2); no World. "Newer" compares `(when, round)`, the pair `questions_for`'s
   `since` already uses.

2. **`engine/season/decision/choose.py`** — beside `odds_weight`, same shape:

   ```python
   def admission_weight(p: Person, c: Candidate, fx: "Fixtures") -> float:
       """THE FACTOR A REMEMBERED REFUSAL PUTS ON A CANDIDATE'S PURSUIT TERM:
       1 - refusal_memory * refused_before(...) / confidence_default. 1.0 at `refusal_memory` 0.0
       (CONTROL), for a verb whose row declares no refusal kind, and where nothing is remembered."""
   ```

   and in `score_terms`, after the existing `pursuit *= odds_weight(p, c, fx, odds)` line:
   `pursuit *= admission_weight(p, c, fx)`. `score_terms` stays the one owner of the formula.

3. **`engine/season/data/fixtures.py`** — `refusal_memory=<value>`, with a `[JUSTIFIED: … H-nnn]` line
   and a hole-register row graded `assumption`, swept `0.0 / 0.5 / 1.0`. **Proposed shipped value 0.5**
   `[ASSUMPTION; medium; Jordan to correct; revert: 0.0, the control]`: half the pursuit weight is
   withheld immediately after a refusal and returns as the claim fades at `claim_decay_per_season`.
   The id is allocated from `references/id_reservations.yaml` at build, not here.

4. **Nothing in `loop/`.** `_drop_what_was_already_done` keeps its rule; a refused act is still
   retryable and is now retried at lower odds.

## Gate (an execution artifact, §0.2)

On `build_realm(0)`, three seasons, `PYTHONHASHSEED=0`, the reading of §1.3 and §1.6 re-run:

| reading | today | passes when |
|---|---|---|
| control arm `refusal_memory = 0.0`: content hash | `52ff67bc…` | equal (the factor is exactly 1.0) |
| refused opportunities attempted again, world-only and unobserved classes | 57% | at or below the executed-act control (about 20%) |
| individuals' refusal share of acts, season 2 against season 0 | 58% against 47% (rising) | not rising |
| `(actor, verb)` pairs attempted three or more times and refused every time | 69 pairs, 378 acts | fewer than half |
| retries that succeed | 14 | not lower (the channel `driver.py:508-518` protects is still open) |

## Falsifier

The retry rate of the unteachable classes does not move at `refusal_memory = 1.0`. That would mean the
re-formed Candidates are not pursuit-priced (their score is the stance term), and the factor belongs on
the sum; say so and move it.

## NERS reading (E last)

- **N.** Cut it and what dies is the only thing that makes "refused" cost the person anything he can act
  on. Top-down (the premise sentence), bottom-up (the claim is already deposited and unread), lateral
  (the odds factor's sibling), horizontal (every verb with a refusal kind, by its row, no verb named):
  holds from four directions. Vertical and diagonal: not tried.
- **R.** No player needed: an NPC who stops walking to an absent man spends those scenes on something
  else, which is where variety comes from. Extreme: a person refused at everything keeps a non-zero
  score on everything (the factor never reaches 0 below `refusal_memory = 1`), so he is never stuck.
- **S.** Same methodology as `odds_weight` (a believed chance on the pursuit term). No new carrier, no
  new Event, no new step.
- **E.** One reader, one factor, one fixture, against 300-odd wasted scenes a run.

## Cost class

Small build (two functions, one fixture, one register row), with a golden re-record at any non-control
shipped value: say so plainly in the commit (CLAUDE.md §7).
