# INST-VENICE-A — a tie changes the odds: the `obligation` obstacle term, and the ask as one roll form

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-20, X-29, X-31) — the term's "lifted by" row is replaced: an edge counts 0 when the one asked is `excused` from its holder (`person_q.excused`, `15_INSTITUTIONS_SYNTHESIS_C_crossings.md` edit 1: he has himself complied with an `avoidance` naming him, or holds a breach against him), not on the bare existence of a ban; an `oblige` counts only if `gate.py::sworn_to` counts it, so an obedience carrying `OBEYED_WRIT` is not an oath for the odds; `oath_step` in the colonial lane is this term. The term, its three fixtures, `owed_to` and the ask stand and are the kit's. Every finding below stands.

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_VENICE.md` §0 (gap 6), §6.1 part 1, §6.2, §8, §12. Batch A of that
file's plan. Not ratified by being written (CLAUDE.md §2).

## What it changes in `engine/season/` at runtime

Every contested social act whose counterparty holds a live obligation edge toward the actor (or toward
the actor's opponent in a heard matter) gains one named term in its composed obstacle. At
`obligation_step: 0` (the control arm, and the shipped value of the first commit) nothing moves and the
content hash is equal to the pre-item hash. At the proposed value the term is live for the four vassal
oaths the built realm holds (probe E-1 of the audit: 4 live `oblige` edges) and for every edge later
lanes add (clients, debtors, members, captains). The outcome of the act is still the draw's: the term
moves the odds and decides nothing.

## The problem (evidence)

- An `oblige` edge is read by `purview_reaches` (ground) and by `_renewals` (upkeep) and by no roll
  (`state/gate.py:386-470`; `verb_table.yaml`, `transfer` row's `writes_note`). A `commit` to a covenant's
  terms is read by nothing ("a reading nothing performs yet", `loop/effects_information.py::_eff_covenant`
  docstring).
- SC's proposed obstacle roster (`proposals/05_SC_obstacle_difficulty_and_modifiers_B.md`, "The terms")
  carries `difficulty`, `opposition`, `standard`, `subject`, `stakes`, `regard`, `capability`,
  `reception`, `evidence`, `plea`. None reads what the one acted upon **owes**.
- D-5 (Jordan, 2026-09-06) refuses any lever on another's obligation (`state/gate.py:1415-1417`). So the
  only lawful effect an obligation can have on the obligor's conduct is on the odds of his own answer when
  he is asked. Today it has none.
- Historical ground (audit §2.2–§2.3, §3): the Medici ruled by favours called in as votes; the Hanse by
  members' compliance with a withdrawal; Venice sealed its ballots precisely so that such ties could not
  be collected in the room.

## The resolution, decided

**One term, `obligation`, in SC's one composer; one roll form, the ask, on existing verbs.** Ladder step 5
(architecture): the composer and its roster are SC's single owner; a second composer or a per-verb bonus
would be a second ladder for one quantity (NERS-S).

### The term

| | |
|---|---|
| name | `obligation` (a member of `rosters.yaml: obstacle_terms`, after `regard`) |
| what it is | what the one acted upon owes, by an edge he himself owns |
| read from | the counterparty's own live Tenures (his interior, the same kind of read as his stance; AX-2: no world read on the person side): (a) a live, un-imposed `oblige` whose object is a seat the **actor** holds; (b) a live `commit` to a Proposition that is the `terms` of a Record the actor holds (a covenant or, with proposal B, a debt). Each such edge counts 1; an edge whose `term` matures within one season counts `obligation_arrears` |
| sign | favourable (subtracted) for edges toward the actor; hostile (added) for edges toward the **other party** of a heard matter (the docketed counterparty, or the rival candidate) |
| size | count × `obligation_step`, bounded by the composer's existing bound |
| the room | multiplied by `sealed_obligation` when the act is heard under an arrangement row with `records_dissent: false` (a sealed ballot or chamber): a tie that cannot be checked cannot be collected |
| lifted by | a live `ban` on the actor whose seat's faction is the counterparty's (an oath to the excluded does not bind; the Church lane's excommunication is the first case): count 0 |
| applies to | every contested act with a person counterparty (`argue`, `petition` once contested by SC's hearing, `speak` where a bench member is rolled, `interrogate`, `interview`); and the answer rolls of `comply` / `evade / defy` where FA's repair makes them rolls |

### The ask

No verb is added. "The ask" names the use of `petition` (or `argue`) by a person toward one who owes
him: a favour called, a vote canvassed, a bond presented (proposal B), an order to withdraw, a better
offer to another man's captain (where the captain's edge to his employer is the *hostile* case). The
band is read by the act's own row. For `petition` to a person the bands are, in the ordinary meaning:
Overwhelming, he does it and more; Success, he does it; Partial, he does the least he can; Failure, he
refuses, and a refusal before witnesses is a deed.

## Exact edits, by owner

1. **`engine/season/rosters.yaml: obstacle_terms`** (created by SC's proposal B; this edit lands after
   it): add the member `obligation` with the row above (`read_from`, `sign`, `applies_to`).
2. **`engine/season/data/fixtures.py`**: three fixtures, each with a hole-register row and a sweep:
   `obligation_step: 0.0` (swept {0, 0.25, 0.5, 1.0}; proposed 0.5), `obligation_arrears: 1.0`
   (swept {0.5, 1.0}; proposed 0.5), `sealed_obligation: 1.0` (swept {0, 0.5, 1.0}; proposed 0).
   Shipped values are the control arm. `[ASSUMPTION; medium; Jordan to correct; revert: the control
   values]`.
3. **`engine/season/queries/person_q.py`**: one reader, `owed_to(p, holder_seats, held_terms) -> (whole,
   lapsing)`: the counts of the person's own live edges of the two shapes above. Person-side: it reads
   `p.tenures` only.
4. **`engine/season/seam/wrappers/sigma.py::contest_input`** (the host that builds the roll's input):
   carry three raw operands: the counterparty's `owed_to` toward the actor, his `owed_to` toward the
   opposing party where the matter has one, and the docketed arrangement row's `records_dissent`. The
   host sums nothing.
5. **`modules/social_contest/roll.py::obstacle`**: compose the term as stated and return it in the term
   list SC-P1 records on the Event.
6. **No `verb_table.yaml` row changes.**

## Gate (execution artifact)

- Hand-built, real fold: one `argue` at a person with a live `oblige` to the actor's seat, and the same
  act at a person without, same seed stream: the recorded term list differs by exactly `obligation`.
- Seeded: `build_realm`, seeds 0, 1, 2, three seasons, `PYTHONHASHSEED=0`. Arm 0 (`obligation_step` 0):
  content hash equal to the pre-item hash at build and at each season. Arm 1 (0.5): every contested act
  whose counterparty is NPC-050, NPC-052 or NPC-070 and whose actor holds `off_king` carries the term;
  the band counts of asks to obliged and to unobliged counterparties are **read and reported** for the
  three seeds. Three seeds are three trajectories, not a rate.
- Sealed room: the same hand-built act heard under `council_of_state` (`records_dissent: false`) with
  `sealed_obligation: 0` carries the term at size 0.

## Falsifier

- The control: any hash move at arm 0.
- Mutation: read the **actor's** edges instead of the counterparty's; the hand-built pair then shows no
  difference and the gate reddens.
- A planted certainty: with `obligation_step` set to 100 the bound must still leave a non-zero chance of
  Failure (the composer's bound is the owner of that; if an obliged man can be made unable to refuse, the
  term has become a lever and D-5 is broken).

## What it does not do

It makes nobody ask. Whether a patron calls a favour is the chooser's (CHAR's
`02_CHAR_goal_lean_on_its_own_question.md`); this gives the ask a reason to succeed more often than a
stranger's.

## NERS reading

- **N.** Top-down, the King's ask of a sworn duke is likelier to be met than of a stranger. Bottom-up, a
  client's vote leans to the house that keeps him. Laterally, the same term serves the feudal oath, the
  monastic vow, the debt and the contract; diagonally, a hearth-scale tie moves a realm-scale ballot.
  Remove it and every obligation in the tree is an edge that changes ground and nothing else.
- **R.** A player builds a following and can see it in the recorded terms; lets it lapse and loses it;
  chooses a sealed or an open room. With no player, bodies drift toward whoever keeps the most men.
  Complete at the extremes: zero edges is today; a hundred is bounded.
- **S.** One composer, one roster, one unit; the room's key (`records_dissent`) is an existing one;
  nothing pauses or sequences differently.
- **E, last.** One roster member, three fixtures, one person-side reader, one host operand group. Against
  what N and R found (every tie in every institution family gains its effect) the ratio is the best in
  this lane.

## Cost class

Small build. Hash EQUAL at ship; the fixture change is a declared mover and its own commit.
