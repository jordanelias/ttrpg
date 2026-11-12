# 28 · CORE · SCENE ACCESS · A — a visit occupies the person visited, and office orders who is seen first

## Status: PROPOSED (a plan for future execution; nothing here is executed by the authoring lane)

Carries `audits/28_SCENE_ACCESS.md` §2 and §3. Serves Jordan's A-63 and A-64 (1)
(`unified/DECISIONS_ANSWERED.md`). Extends `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` (A-9: its
edits 1 and 3 are the sites) and `18_DETERMINISM_rival_acts_in_one_fold.md` (one more rivalry key through
the same re-order). Reference only (CLAUDE.md §0.05). Not ratified by being written.

## What it changes in `engine/season/` at runtime (first)

With the new fixture `occupancy` at `off` (the control, shipped in the first commit): nothing; every
content hash is the A-9 tree's. At `seat_and_debit`:

1. In RESOLVE, a face-to-face interaction whose counterparty is already in another scene this round, or
   has no scene action left this season, is refused at a new clause, `occupied`, and emits
   `visitor.kept_waiting`. It costs the visitor his scene, as every refusal does.
2. A person received in a visitor's scene does not also run a scene of his own that round: his released
   scene goes back to the head of his queue and its debit is withdrawn.
3. The budget Query (`loop/deliberate.py:175-176`) subtracts the scenes a person was received in beside
   the scenes he opened.
4. The scenes that claim one person's round (his own, and each visitor's) are re-ordered among the fold
   positions they already hold by a precedence draw whose weights are office rank and a kept
   appointment.

A **declared hash mover** in every world where a face-to-face interaction is admitted in a round in
which its counterparty released a scene (22, 37 and 25 such rounds in two seasons at seeds 0, 1, 2;
audit §1.3). Nothing is added to `World`, to any carrier's fields or to any Event's `changes[]`.

## The problem (evidence)

- `state/carriers.py:602-632`: a `Scene` is `(id, actor, acts, occasion)`. No second person is in it.
- `loop/resolve.py::_admits` (`:187-313`) asks eligibility, the precondition, then the counterparty
  clause (`:305-312`: the operand names somebody other than the actor). Nothing asks whether that
  person is doing something else.
- `loop/deliberate.py:175-176`: `ask_budget = max(0, budget(p, v, k, fx) − self._spent.get(p.id, 0))`;
  `_spent` is debited at release (`:294`) for the opener only.
- Measured (audit §1.3; realm, seeds 0, 1, 2, two seasons): in 16 of 22, 24 of 37 and 16 of 25 rounds in
  which a person is the counterparty of an executed face-to-face act, he also executes an act of his own.
  Two to five rounds per run have two visitors on one person; 26 to 48 *attempted* rounds do.
- `loop/resolve.py:51-58`: the order among those acts is `(stratum, H(seed, tick, actor, "order:…"))`.
  Which of two visitors reaches a person first is a hash of the acts' content.

## The resolution, decided

Ladder: step 1 (A-63, A-64, A-62); step 4 for each mechanism (the precedents are named at the edit);
step 5 for the two choices marked **(decided here)**.

### 1. Which acts occupy: read off the row, no list

A row **occupies its counterparty** when its typed cell asks the `with` relation of the operand its
`counterparty:` column names. That is the cell's own statement that the two must be in one place. Today:
`accept`, `argue`, `capture`, `challenge`, `give`, `lie`, `tell`. A paper (`petition`, `issue`), a
conferral and an oath to a seat occupy nobody. `covenant` joins the day its lane adds `with` to its cell
(A-21 keeps covenants in person; `14_VERBS_SOCIAL1_B_documents_and_obedience.md`), with no edit here.
The counterparty must be an individual (`Person.is_cohort`, the owner the `individual` stem already
reads, `queries/world_q.py:4599-4606`): a crowd is not occupied by one speaker.

### 2. One scene per person per round: a fold-local read

The driver holds a round-local mapping `engaged: person id -> scene id`, emptied before each round's
RESOLVE, filled by the fold, read once more by ENCOUNTER (which shares barrier 3 and seats a sitting's
attendees, `05_SC_playable_hearing_B.md`), and never read after it (`04` PART D row 34's lifetime:
dropped at the next barrier). It is in no carrier, no hash and no Event. Walking the scenes in order:

- **The opener.** If the scene's actor is already engaged in another scene, the whole scene is
  **deferred**: none of its acts enters the act store (`resolve.py:1033`) or folds; the scene is handed
  back to the driver, which puts it at the head of that person's queue and withdraws the release debit
  (the inverse of `deliberate.py:294`). Precedent: `deliberate.py:187-189`, *"a queued scene is deferred,
  not dropped"*. Otherwise the actor is engaged in his own scene.
- **The counterparty.** For an occupying act that has passed eligibility, its precondition and the
  counterparty clause: if the counterparty is engaged in another scene, or his budget Query reads 0, the
  act is refused at `occupied`. Otherwise the counterparty is engaged in this scene. Two interactions
  with one person in one scene seat him once.
- **Across rounds** nothing is carried except what the engine already carries: the season's budget
  remainder (the Query), the deferred scene in the person's own queue, and an appointment (proposal B).
  A person received in round 2 is free again in round 3.

At `scenes_per_round` above 1 (swept, H-124) the rule reads "in at most `scenes_per_round` scenes".

### 3. The debit: the Query subtracts scenes received **(decided here: both arms of A-63, as one rule)**

A-63 gives two arms (*debited* or *unavailable to a second visitor*). They are one rule at two grains:
the round's seat (§2) and the season's budget. `SeasonDriver.season` already promotes realised acts into
a season-local set after the fold (`driver.py:519-534`, `_realised`); in the same pass it adds, for each
admitted occupying act, the act's scene id to `self._received[counterparty]` (a set of scene ids, reset
with the other season locals at `:472`). `ask_budget` becomes

```python
max(0, decision.budget(p, v, k_budget, w.fixtures) - self._spent.get(p.id, 0)
       - Scene.PLAIN_COST * len(self._received.get(p.id, ())))
```

`decision/budget.py::budget` is not edited and gains no `World` (S26; AX-2). What is kept is the set of
scenes that happened; the number is computed when asked (#353 `holonic_ARCHITECTURE.md:918-919`,
*"without anybody storing a number"*; A-62). No gate write, no receipt, no `changes[]` on any Event. A
received scene costs the host one scene action whatever it cost the visitor `[ASSUMPTION; medium; Jordan
to correct; revert: the visitor's own `cost(ext)`]`.

The fixture has three values so the two arms can be told apart: `off`, `seat` (§2 only),
`seat_and_debit` (§2 and §3). At the shipped `scene_budget = 5` rounds and base budget 5 the debit binds
only on a person whose budget is below the round count (a wounded or travelling one,
`decision/budget.py:58-61`): he is received until his scenes are gone and then receives no one.

### 4. Precedence: a draw over the claims on one person's round

- **The group.** `loop/resolve.py::rival_key` (the function `18_DETERMINISM_rival_acts_in_one_fold.md`
  adds) gains one key: `("round", person)` for a scene whose actor is that person and for every scene
  holding an occupying act that names him. Groups that share a scene are merged. As in that proposal, a
  group is re-ordered **among the positions it already holds**, so no scene outside it moves.
- **The draw.** One net per scene, drawn once: `roll_net(pool_default, rng)` through the one roller
  (A-5), on `draw_factory(seed, tick)(actor, f"precedence:{scene id}")` (`04` PART D row 35: a keyed
  purpose, no counter), with levels added through the one leverage form
  (`U5c_SC_one_obstacle_form.md` §3, `levels_to_net_sigma`, the soft cap):
  - one `precedence_level` per step by which the scene's actor stands above the lowest-ranked actor in
    the group, by **office rank**;
  - one `appointment_level` where the actor holds a live appointment with a person the scene names
    (proposal B's reader `world_q.appointment_with`).
  Highest net first; a tied net is re-drawn on the same stream.
- **Office rank, one reader.** New `queries/world_q.py::office_rank(w, pid) -> int`: the highest
  `RUNG_KINDS.index(rung.kind)` over the rungs of the seats `pid` holds live, 0 for the seatless. It is
  the existing `rank` stem's ordinal (`world_q.py:4634-4643`) asked of a seat's rung, and it reads
  every seat held because a visit is an `own` act and carries no `Act.via` (the same reading, and the
  same `[ASSUMPTION]`, as limb 2 of `world_q.py::admits_audience`). `rank_gap`
  (`U5c_SC_one_obstacle_form.md` §2 member 6) calls it for an act with no `via`.
- **The host is one of the claimants.** His own scene is in the group with his own office rank. A duke's
  business usually outranks a petitioner's call and usually yields to the king's; neither is certain.
  **(decided here)** Not chosen: the host's scene always first (measured as arm V2: meetings fall by half,
  audit §1.4) and the visitor always first (other people would spend a person's season for him, against
  S26.3's *"the PERSON chooses what to leave undone"*).

### 5. Three channels for rank, and none of them twice

| channel | reads | acts on | never |
|---|---|---|---|
| precedence (this file) | `office_rank` of each claimant; a live appointment | the order in which rival scenes fold | a pool, an obstacle, a band, eligibility |
| `rank_gap` (U5c §2 member 6) | how far the person acted on stands above the actor | the obstacle of the act's own roll | order |
| `office` (U5c §3; A-12) | the seat exercised before a bench or body | levels on the act's own roll | order |
| `regard` (U5c §2 member 7) | stance rows only, *"never rank or heritage"* | the obstacle of the act's own roll | order; rank |

Regard reaches access only through the host's own act of granting an appointment, which his chooser
ranks as it ranks any candidate (proposal B). The precedence net is not an input to any roll.

## Exact edits, by owner (in landing order; all after A-9's edits 1 to 4)

1. **`engine/season/data/verbs.py`** — `VerbRow.occupies` (a derived property: `counterparty` set and the
   typed cell holds a `relation` conjunct `with` of that operand); `OCCUPIED_CLAUSE = "occupied"` beside
   `COUNTERPARTY_CLAUSE` (`:452-457`), *derived like the other two: a keyed row keys it iff it occupies*;
   the loader's keyed-row rule (`:953-969`) adds it to the expected clauses.
2. **`engine/season/verb_table.yaml`** — the seven occupying rows carry
   `emits_on_refusal: {…, occupied: ["visitor.kept_waiting"]}`; a flat row among them becomes keyed with
   its existing kind on each existing clause (the shape A-9's `sequence` clause takes). One kind, shared
   by the seven rows, declared on each (so loader invariant 7 derives it; `04` PART D row 25).
3. **`engine/season/loop/resolve.py`** —
   - `rival_key`: the `("round", person)` key (§4); the group re-order and the precedence net inside
     `_canonical_order`, shared with `loop/encounter.py` as today.
   - `resolve`: the `engaged` local; the deferral of an engaged opener's scene (returned as
     `self._deferred`); `_admits` takes `engaged` and a `remaining(pid)` callable and asks the `occupied`
     clause after the counterparty clause (`:305-312`). The refusal Event names the counterparty as its
     subject, so the claim it deposits is about him `[UNVERIFIED: whether `_act_events` takes a subject;
     if not, it gains one, defaulting to today's]`.
4. **`engine/season/loop/driver.py::season`** — `self._received` reset at `:472`, promoted in the pass at
   `:519-534`; deferred scenes re-queued at the head and their debit withdrawn before the bookkeeping
   that counts `n_acts`; `remaining` built from the same expression `ask_budget` uses (one helper on the
   driver, called by both).
5. **`engine/season/loop/deliberate.py:175-176`** — `ask_budget` calls that helper.
6. **`engine/season/queries/world_q.py`** — `office_rank`.
7. **`engine/season/data/fixtures.py`** — `occupancy: off | seat | seat_and_debit` (control `off`);
   `precedence_level` and `appointment_level` (`LEVEL_SIGMA` names; first values `minor` and `major`;
   control `None`, at which the group is ordered by the bare draw); each with a `hole_register.yaml`
   row graded `assumption`, ids allocated at build from `references/id_reservations.yaml`.
8. **Layer 1 (drafted here, applied only by Jordan's amendment).** `04` PART D row 36, after *"rank
   never breaks a tie"*: *"Where several scenes claim one person's round, office rank is a declared
   weight of a keyed precedence draw (Jordan, A-64) and never a sort key: a lower rank is sometimes seen
   first."* #353 §27's order sentence (already owed under A-9) gains *"…and scenes that claim one
   person's round are ordered among themselves by that draw."*

## Gate (execution artifacts, §0.2): what the measurement must show before this ships

Realm, `build_realm`, seeds 0 to 4, four seasons, `PYTHONHASHSEED=0`, on the tree where A-9 and
`14_VERBS_SOCIAL1_A_formation.md` have landed (before that there are too few meetings to read: audit §0).

| # | reading | passes when |
|---|---|---|
| 1 | control: `occupancy: off` | content hash equal to the pre-edit tree at every seed |
| 2 | executed acts, `seat_and_debit` against `off` | not below 95% at any seed (the crude arm's worst reading is 96.1%) |
| 3 | admitted face-to-face interactions, `seat_and_debit` against `off` | not below 60% at four seeds of five (the crude host-always-first arm reads 46% to 50%; a design that does no better than that arm fails) |
| 4 | `visitor.kept_waiting` Events | above zero at every seed, each with a cause chain to its act |
| 5 | scenes deferred; of those, later released or still queued at season end | reported by office rank; **no individual with a deferred scene opens zero scenes that season** |
| 6 | `ask_budget()` read before and after a received scene | differs by one; the log holds no Event with a budget change and no refusal Event with `changes[]` (A-62) |
| 7 | planted: host of rank 4, visitors of rank 7 and rank 0, both present, 400 seeds | the rank-7 visitor is first more often; neither share is 0 or 1; the host keeps his own scene against the rank-0 visitor more often than not and loses it to the rank-7 visitor more often than not, neither with certainty |
| 8 | planted: the same visit with `precedence_level` on and off | the visit's own roll has identical pool, obstacle terms and levels in both arms; sweeping the host's stance toward the visitor from minimum to maximum leaves every precedence net unchanged |
| 9 | `seat` against `seat_and_debit` | reported: the persons for whom they differ are those with budget below the round count |
| 10 | DELIBERATE's permutation falsifier (`engine/season/tests/test_rem31_grid_suspension.py`, named at `loop/deliberate.py:126-130`) and the `ordp.py` strata-cut arm | the first unchanged; the second reported |

**Declared hash movers:** `occupancy` other than `off`; `precedence_level` or `appointment_level` other
than `None` in a world with a rivalry group. No other fixture moves.

## Falsifier

A visitor of the higher rank first at every seed (a sort, not a draw). A received person who also folds a
scene of his own in that round. A deferred scene that is neither released later nor still queued. A
refusal at `occupied` whose counterparty was free. A precedence net that changes when a stance row
changes. Gate 3 at or below the crude arm.

## NERS reading (E last)

- **N.** Cut it and a person is in any number of rooms at once, so nobody is ever hard to reach and the
  appointment and the waiting petition have no subject. Top-down: the ruling. Bottom-up: the fold already
  refuses on scarcity of grain and seats; a person's round is the same kind of thing. Laterally: a fight
  holds both fighters (`modules/combat/` takes both parties' state); a visit is the only two-person act
  that did not. Diagonally: a hearing's attendees (§ `05_SC_playable_hearing_B.md`, folded) are seated by
  the same read. Vertically: the budget Query already varies by office, body and travel; it now varies
  by who came. Horizontally: one rule for seven rows, read off the cell.
- **R.** Strategy: whom to see, when, and whether to go oneself. With no player: a busy lord, a crowded
  antechamber, a man who never gets in. Completeness: the reduced-budget host and the cohort are stated;
  the gate's row 5 is the starvation check.
- **S.** *Pauses correctly* at the smallest scale (the test PES_CORE §1.1 pt 3 found failing).
  *Calculations consistent in methodology*: the precedence draw is the rival-acts draw with one more
  key; its levels are the one leverage form's.
- **E.** One derived row property, one local mapping, one set on the driver, one key in an existing
  re-order, against what N and R found.

## Cost class

Small build, after two dependencies. Golden re-record at every fixture where a meeting is admitted: say
so plainly in the commit.

## Dependencies

A-9 (`16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` edits 1 to 4) → this file.
`18_DETERMINISM_rival_acts_in_one_fold.md` (`rival_key`, the group re-order) → §4.
`U5c_SC_one_obstacle_form.md` (levels; `rank_gap`'s reader) → §4, §5.
`14_VERBS_SOCIAL1_A_formation.md` (visits form where the other is believed to be) → the gate.
`16_PESSIMIST_CORE_a_refusal_is_remembered.md` reads `visitor.kept_waiting` with no edit (the kind is on
the row's `emits_on_refusal`). Proposal B supplies `appointment_with`; without it that level is never
added and the rest stands.
