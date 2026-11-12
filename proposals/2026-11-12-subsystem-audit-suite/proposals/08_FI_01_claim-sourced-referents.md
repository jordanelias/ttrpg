# 08 · FI · 01 — Referents about other people's state come from the asker's own ledger

## Status: PROPOSED

Carries audit `audits/08_FI_audit.md` F-FI-01 and resolutions R-01, R-02, R-03. Builds a decision already
recorded as taken: `registers/editorial_ledger_in.jsonl`, ED-IN-0292, last row (2026-10-26, A1-02,
TAKEN-ARCH): *a vacancy reaches a person as a claim deposited through the channels, not as a world stamp.*

## What this changes in `engine/season/` at runtime

`queries/world_q.py::questions_for` stops handing a person referents read from another person's or seat's
current state. After it: a `seat_holders` ambition is about whoever the asker's own ledger names as holding
the seat; `confer` forms on a seat the asker has heard is vacant; a rung aim reads `met` once the asker has
heard who holds the rung; a docketed matter is stamped for a convener who holds a claim of its docketing.
Stamps over the asker's OWN live edges are unchanged. A declared hash mover on every realm world.

## The problem, with evidence

`r08_probe.py` (scratchpad `runs/FI/`; `build_realm(0..2)`, tick 0, `PYTHONHASHSEED=0`). A `hold` is edited
directly on the World: no Event, no WITNESS; the subject's ledger and own tenures are byte-identical before
and after.

| arm | candidates moved |
|---|---|
| no edit | no |
| an unrelated seat changes hands | no |
| the seat a `seat_holders` goal names changes hands (`p_npc_088`, `off_cardinal_justice`) | yes: 44 → 43, re-aimed at the new holder |
| a seat a conferrer may fill is vacated (`p_npc_020`, `off_archbishops_rep`) | yes: 152 → 180, the printed gains all `confer` on it |

In play (`dynamics.py`, one season, seeds 0 / 1 / 2): 81 / 82 / 84 chosen acts (30 / 32 / 29 folded) aimed at a
subject the actor held no claim about, was not, and held no edge on.

## The rule (R-03)

> A stamp or referent computed from the asker's **own** live edges may read the World (he knows his own
> lands, writs, works and prisoners). One computed from **anyone else's** state must be named by a claim in
> the asker's own ledger.

Own-edge, unchanged: `writs_held`, `records_held_for_holding_rows`, `works_sites`, `detainees_held`,
`holdings_to_found`, `larders_in_purview` (already ledger-named), `seats_named`, `places_named`,
`propositions_heard`, `wounded_with`, `enemies_heard`. Changed: the four below. Precedent inside the same
function: `sittings_before` and `docket_question` already require a held claim.

## Edits, by owner

1. **`queries/person_q.py` — one new reader, `holders_named(ledger, obj) -> tuple`.** The persons the
   holder's own claims name as holding `obj` (a seat or a rung), newest first: for each claim about `obj`
   whose predicate is a kind a `hold` opener emits (read off `data/verbs.py`'s derived openers, never
   spelt), the person-subject claims of the same predicate deposited at the same `(when, round)` — the
   pairing key `deed_doer` / `_seen_index` already use for a deed and its sighting. A holder is dropped when
   a newer claim about `obj` or about him carries a kind a `hold` closer or a death emits. World-free; it
   imports nothing new. `[ASSUMPTION; medium; Jordan to correct]`: two seat changes one person witnesses in
   one round name both holders (over-inclusive, from his own ledger, never from the world).
   Sibling: `vacant_named(ledger, obj) -> bool` — the newest opening-or-closing claim about `obj` is a
   closing one.
2. **`queries/world_q.py::_goal_referents`, the `seat_holders` branch.** Old: *"the persons now holding any
   listed seat (a live `hold`, `w.tenures` order)"*. New: `holders_named(p.ledger, seat)` for each listed
   seat, in seat order, each once. Rewrite the docstring's paragraph that begins *"⚠ `seat_holders` IS A
   WORLD READ WITH NO CLAIM BEHIND IT"*: the precedent it cites was answered the other way (R-02).
3. **`queries/world_q.py::vacancies`.** Old: every Office with no live `hold` that `may_fill` admits. New:
   every Office in `ledger_names(p.ledger)` for which `vacant_named(p.ledger, o)` and `may_fill` (his own
   seat's authority, an own-edge read) hold. The world's "no live `hold`" test is **removed**: a man who
   wrongly believes a seat empty forms the `confer`, and the fold refuses him (§F1's asymmetry, the rule
   `belief_contradicts`' docstring states).
4. **`queries/world_q.py::aim_state`.** `met` only where the shipped rule holds **and**
   `holders_named(p.ledger, rung)` contains the rung's governing holder: he keeps working until he hears.
5. **`queries/world_q.py::matters_awaiting`.** Keep the seat and tier logic; admit a matter only where
   `docketed_by` finds a claim of its docketing Event in `p.ledger` (`docket_question`'s own gate).
6. **`harness/populated.py` — the realm does not start blind.** Beside `seed_acquaintances` (CR-81's
   shape), `seed_seat_news(w)`: for each person, the claims a witness of each seat's opening would hold, for
   the seats the `reach` roster (CR-29) carries to him, source `told_by`, empty chain, built from
   `claim_subjects`' own subjects so the starting ledger and a played deposit are one shape. Until CR-29
   lands the map is "the seats of his own realm" (audit §11 item 1, option A, shipped; option B the
   control).
7. **`engine/season/requirements.yaml`, R-07 and R-08 `measured:`.** Replace *"IMPERFECT KNOWLEDGE IS
   STRUCTURAL AND HOLDS"* / *"NON-OMNISCIENCE HOLDS, structurally"* with the reading: holds for claims;
   referents were world-read until this position; cite the probe.
8. **One test, in `engine/season/tests/test_season_shape.py` beside the `r7` group** (it executes the
   behaviour and its subject crosses into the engine's decisions, `CLAUDE.md` §0.1 pt 5's predicate): a
   silent seat change moves no candidate; the same change by a witnessed act does; the unrelated-seat arm
   is the control. Add its name to R-07's `measure:`.

## Gate (execution artifact)

`r08_probe.py` re-run on the edited tree: P1 and P2 read *candidates moved: no*; both controls unchanged.
Then the positive arm: the same seat change performed by a real `confer` / `release` the subject is
admitted to (or told of) moves his candidates in the next round.

## Falsifier

After the edits a `need` question's referent, or a `confer` Candidate's subject, that `ledger_names` /
`known_persons` of the actor does not contain. Planted failure for the test: restore the `w.tenures` scan in
`_goal_referents`; the silent arm must go red.

## Risks, stated

- Formation falls at world start (ledgers hold 3 claims at tick 0): edit 6 exists for that; measure
  `confer`, `petition` and `challenge` formation before and after at seeds 0–2 and report both.
- H-230 (the heir never told) is the same gap from the other side and closes with this plus CP-T02-01.

## NERS reading

N: without it R-07/R-08's own statements are false, and every "news arrives late" story is impossible; holds
top-down (requirements), bottom-up (one reader, four call sites), lateral (CHAR's goals, FA's conferral).
R: adds the no-player half directly: people act on stale appointments. S: one rule for every stamp, replacing
two families in one function; the pairing key is the one `deed_doer` already uses. E, last: one reader and
four small edits against a class of five world reads: cheaper than what it replaces.

## Cost class

Small build. Lanes: FI (reader), CHAR (goals), FA (conferral). Depends on nothing; better measured after
CR-29.
