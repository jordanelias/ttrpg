# INST-VENICE-C — the roll, the lot and the ballot; a cooling-off and an audit at exit

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_VENICE.md` §1.3, §1.4, §2.1, §2.2, §5.3, §6.1 parts 2 and 3, §6.2, §14.
Batch C. Depends on FA-P3 (`proposals/06_FA_seat_terms_and_turnover.md`: the seat-row `term:` key and
its loader), FA-B3 (which rows carry it), CR-35 and CR-36 (workplan `v11_part12:140-141`: an elected seat
filled by its faction's bench; nominate-then-confirm). Not ratified by being written. **Edit 5 changes a
shipped conjunct (CR-34's `vote`) and is design-first.**

## What it changes in `engine/season/` at runtime

1. A seat may be joined only by warrant, where its row says so.
2. A seat may be filled only from a named roll, where its row says so.
3. A seat whose conferral basis is `lot` is filled by a draw among the eligible on that roll.
4. A person whose termed hold on a seat has matured may not be seated in it again until a stated number
   of seasons has passed; a termed hold's maturing on a row that names an audit raises that audit as a
   referent for the seats that may open it.
5. Under a `declared` arrangement row, a matter is decided by ballots **drawn at the sitting**, one per
   bench member, and not by a count of standing commits.

With every new key null and no row using the new roster members, edits 1 to 4 move nothing (hash EQUAL).
Edit 5 moves every run in which `determine` executes under `excommunication_deliberation`: a declared
mover.

## The problem (evidence)

- The tree's own cross-civilisation finding: *"the decisive lever is who controls the list, not the
  nominal selection procedure"* (`research/governance/political_hierarchy_standing.md` §The standing
  currency, compared). The engine has no list: `binds_bases` has one value, `members_by_admission`
  ("a person joins by their OWN `oblige`"), "a roster with one value and one reader, conceded"
  (`rosters.yaml: binds_bases` note).
- `conferral_bases` is `[appointed, elected, annex, inheritance]`; "NOTHING DISCRIMINATES BETWEEN THE
  THREE YET … no election or annexation verb exists" (its note). Sortition is inexpressible.
- Canon names a gate nothing implements: "Burgher status: Guild Masters and Free Masters qualify for
  political participation" (`office_bodies: Guild` function cell).
- FA-P3 gives a seat a term and nothing stops the outgoing holder being re-seated at once; nothing asks
  him for an account. 0 termed live tenures at build (audit E-1).
- `excommunication_deliberation` (`arrangements.yaml:265-285`) admits `determine` when `quorum` distinct
  bench members hold a live `commit`: a count decides the matter. The standing rule (Jordan, 2026-11-12)
  forbids "the bench rules by score".
- 8 of 34 seats are `elected` and none can be filled by an election (audit E-1; CR-35 not built).

## The resolution, decided

### 1. A roll is an establishment kept by warrant

`binds_bases` gains `members_by_warrant`. `_req_oblige` admits an `oblige` to a seat whose `binds` is that
value only if the joiner **holds a `dispensation` whose `terms` is that seat and of which he is an
addressee**, minted through that seat (the Record's rung is the seat's rung, as `_seat_rung` writes it).
The keeper edits the list with `issue` and `give` (to admit) and by not renewing (to drop): a member's
`oblige` carries a term and lapses at MATTER unless the seat renews it, which is D-5's own expulsion rule
(#453 `:2076`, "the seat withholding renewal"). A purge is therefore quiet, costs no accusation and is
visible only as a `tenure.closed` by term: the Florentine bag purge. Where the body, not the keeper,
admits, the keeper's `issue` follows a ballot on the candidate (edit 5) in which the candidate's deeds
are the `evidence` term (audit §5.3). Ladder step 4: the roster's own note says a second value "arrives
WITH its rule in `_req_oblige`".

### 2. Eligibility from a roll

A seat row may carry `eligible_from: <seat id> | null`. `state/gate.py::may_seat(w, off, person)` is the
one reader: true when the row names no roll, or the person holds a live `oblige` to the named seat. Asked
by `_req_confer`, by CR-35's bench election and CR-36's nomination when they land, and by the lot. The
person-side decline (a conferrer who holds no claim that the candidate is enrolled does not form the act)
follows `confer`'s ban decline in `audits/14_VERBS_BINDING.md` §1.

### 3. The lot

`conferral_bases` gains `lot`. `FILLED_BY["lot"] = {CONFERRAL}`. For a seat of that basis `_eff_confer`
ignores the act's `to` and **draws** the conferee with `draw(off.id, "lot")` (`state/ids.py`, the one draw
owner) uniformly from the persons for whom `may_seat` holds and who are present at the seat's rung or
below it. A drawn person who is barred (edit 4's cooling-off; a live `ban` within the seat's purview) is
*seen and not seated*: the act emits `lot.seen` naming him, and the draw repeats over the remainder; an
empty bag leaves the seat vacant and emits `lot.empty`. The presiding seat (any seat for which `may_fill`
holds) chooses when to hold the draw and nothing else. The odds are the composition of the roll, which
persons made (edit 1). A roll of one is a certainty only in the sense that eligibility is: whoever
emptied the bag did it by acts others could see.

Venice's two-stage election needs no further mechanism: a nominating seat with `conferral: lot`,
`eligible_from` the body's roll and `term: 1`, whose holder nominates under CR-36; the body confirms by
ballot (edit 5). Florence's is one `lot` seat. One alternation, not nine (audit §5.2).

### 4. Cooling-off and the audit at exit

Two optional seat-row keys beside FA-P3's `term`:

- `cooling_off: <positive int> | null` (seasons). `may_seat` is false for a person whose most recent
  `hold` on this seat closed by term maturity fewer than that many ticks ago. Computed from the closed
  Tenure's `until`; stored nowhere.
- `audit_at_exit: <arrangement id> | null`. When a termed `hold` on the row's seat matures, MATTER's
  existing `term.matured` Event is stamped on the questions of every seat-holder who may open a case on
  that person (those for whom `may_fill` holds over the seat, and any seat of the same body whose remit
  carries `determine`) as a classed referent `Party` naming the outgoing holder and the arrangement
  (`14_VERBS_BINDING_B_sittings.md`'s class). **Nothing is docketed by the engine.** A person opens the
  case or does not; subjects' told complaints are the evidence; the verdict is the bench's roll.

### 5. Ballots are drawn

Under a row with `disposal: declared`, `determine`'s resolution is: for each member of the judging set
present, one `social_contest.roll` whose actor is the proposer (the candidate, the accuser, the sponsor
of the measure) and whose counterparty is that member, with SC's composed obstacle. The terms that
matter: the member's `regard`; `obligation` (proposal A), scaled by `sealed_obligation` when the row's
`records_dissent` is false; `evidence`; the row's `standard`; a live `commit` by the member to the
matter's Proposition as a favourable term of fixed size `pledge_step` (a promise is odds, not a vote,
and under a sealed ballot it is scaled as `obligation` is). Each roll yields a ballot: Overwhelming or
Success, *for*; Partial, *doubtful*; Failure, *against*. The tally is arithmetic over the drawn ballots:

| matter's band | condition | what it writes |
|---|---|---|
| Overwhelming | *for* ≥ two thirds of ballots, and ballots ≥ `quorum` | the row's disposal (or the seating), and a prestige deed for the proposer |
| Success | *for* > half, and ballots ≥ `quorum` | the row's disposal (or the seating) |
| Partial | neither *for* nor *against* > half, or ballots < `quorum` | nothing is disposed; the matter stays on the docket for the next sitting (`matter.undetermined`); where several options stand, the one with the fewest *for* is dropped |
| Failure | *against* > half | `matter.dismissed`; the proposer may not bring the same matter before this body during the present holders' terms |

`quorum` keeps its meaning (the least number of ballots). Where `records_dissent` is true each ballot is
an Event others witness; where false only the tally is. `world_q.declared_votes` loses its reader in
`determine`'s `vote` conjunct, which becomes "a judging set of at least `quorum` is present", an
eligibility check.

## Exact edits, by owner

1. **`engine/season/rosters.yaml`**: `binds_bases.values: [members_by_admission, members_by_warrant]`;
   `conferral_bases.values: [appointed, elected, annex, inheritance, lot]`. Each with its note.
2. **`engine/season/offices.yaml`** and **`data/rosters.py::_load_offices`**: admit `eligible_from`,
   `cooling_off`, `audit_at_exit` (and `binds`, if the loader does not already admit it on a row
   `[UNVERIFIED]`); refuse at load an `eligible_from` that is no row id, a `cooling_off` that is not a
   positive whole number, an `audit_at_exit` that is no `arrangements.yaml` id, and any of the three on a
   row with no `term` where the key presupposes one (`cooling_off`, `audit_at_exit`).
3. **`engine/season/state/carriers.py::Office`**: three optional fields, folded into the hashed
   representation only when not `None` (FA-P3's rule, so an unkeyed world's hash does not move).
4. **`engine/season/state/gate.py`**: `may_seat`; `FILLED_BY["lot"]`; the import-time totality checks
   extended over the new members.
5. **`engine/season/loop/predicates.py`**: `_req_oblige` gains the warrant clause for
   `members_by_warrant`; `_req_confer` asks `may_seat` for every basis but `lot` (where the effect asks it
   of each drawn name).
6. **`engine/season/loop/effects_governance.py::_eff_confer`**: the `lot` branch. `verb_table.yaml`,
   `confer` row: `emits` gains `lot.seen`, `lot.empty`.
7. **`engine/season/loop/matter.py`** and **`queries/world_q.py::questions_for`**: the `audit_at_exit`
   stamp.
8. **Design-first, with SC and FA:** `loop/effects_information.py::_eff_determine`,
   `seam/wrappers/sigma.py`, `data/requires.py` (`vote` conjunct), `data/fixtures.py` (`pledge_step`,
   proposed 0.5, shipped 0, swept {0, 0.5, 1.0}), `verb_table.yaml` `determine` row's notes.

## Gate (execution artifact)

- **Spine fixture, rotating council.** One settlement on `governance_spine.yaml`'s chain: a roll seat
  (`members_by_warrant`) with eight enrolled persons; three council seats (`conferral: lot`,
  `eligible_from` the roll, `term: 4`, `cooling_off: 4`, `audit_at_exit: tribunal`); a presiding seat.
  Seeds 0–2, twelve seasons, `PYTHONHASHSEED=0`. Read and reported per seed: every council seat's holders
  in order; `lot.seen` and `lot.empty` counts; audits opened by a person. Asserted: no holder is seated
  inside his cooling-off; no holder is off the roll; the three seeds do not seat the same sequence.
- **Control.** All new keys null and both new roster members unused: content hash equal to the pre-item
  hash at build and at four seasons.
- **Ballot, hand-built.** A five-member bench under a `declared` row, fixed positions, forty seeds: all
  four matter bands occur at least once across the seeds for a middling position (asserted that it
  observed at least three distinct bands); with `records_dissent: false` and `sealed_obligation: 0` the
  recorded term lists carry `obligation` at size 0.
- **Capture reading.** In the council fixture, the keeper admits only persons obliged to one house: the
  share of council-seasons held by that house's clients is read against the unpacked control.

## Falsifier

- Planted: the lot ignoring `may_seat` seats a stranger; the gate's "no holder is off the roll" reddens.
- Planted: the lot reading the act's `to`; the three seeds then seat the presiding officer's choice and
  the "not the same sequence" assertion cannot distinguish it, so the test also asserts that the seated
  person differs from the act's `to` in at least one draw.
- Mutation: `cooling_off` read against the hold's `since` instead of its `until`.
- The ballot: a tally computed from `declared_votes` (the old count) reproduces one band at every seed;
  the forty-seed assertion reddens.

## NERS reading

- **N.** Top-down, a body's seats are filled from its own list. Bottom-up, a craftsman's enrolment is
  the first rung of every office above. Laterally, the peerage roll, the college of electors, the guild
  matricula and the company's register are one mechanism. Diagonally, a hearth's client packed onto a
  settlement's roll moves a realm seat's election. Remove the roll and capture has nowhere to happen;
  remove the lot and the roll has no pay-off an election does not already give; remove the drawn ballot
  and every council in the game is arithmetic.
- **R.** Strategy at the list (enrol, lapse, challenge), at the calendar (when to hold the draw), at the
  room (sealed or open). Customisable per seat by five row keys. With no player: turnover, cooling-off
  gaps, audits and tied ballots that return next sitting. Extremes: an empty bag is a vacancy with an
  Event; a bench below quorum is a Partial, not a crash.
- **S.** The lot uses the one draw owner; the ballot the one roll owner and SC's one composer; the term
  the one clock. A ballot's Partial pauses the matter on the docket it was already on.
- **E, last.** Two roster members, three row keys, one gate predicate, one effect branch, one stamp, and
  one changed resolution. The last is the heavy part and is why this is design-first; against it stands
  every election, enrolment, decree and threshold vote in all the institution families.

## Cost class

Small build for edits 1 to 7 (hash EQUAL at ship; each authored row a declared mover). Design-first for
edit 8.
