# PES-FA-C — the command basis is one predicate: a seat's sworn, the seats it may revoke, and the unseated on its ground

Reconciled: 2026-11-12, U5d closure — folded **A-22** (command). `under_seat` is rewritten to the ruled three classes: (i) the sworn (a live `oblige` to this seat; the third disjunct, unchanged), (ii) the holder of a seat this seat may revoke (`may_revoke`, replacing the second disjunct "he holds a seat on its ground"), (iii) an **unseated** person in its land (the first disjunct, narrowed: `purview_reaches(seat, place_of(person))` and the person holds no seat). A seated resident who is neither sworn nor revocable is no longer under the seat by living there. A writ to a superior is a petition: edit 2 routes a Person referent who fails `under_seat` to the petition form, not to a refusal. Edit 3 (`dispatch` asks the same predicate) stands; this narrows the ED-IN-0256 (4) basis for `issue` and `dispatch` behind its revert, as the ruling says. Gate arms rewritten: the Duke of Varfell reaches the holders of Varfell seats he may revoke and his sworn men, wherever they live; the Royal Marshal no longer reaches seated residents of other factions.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §2 and §1 (A-22: the resolution block,
"What it changes" and the gate rewritten to the three ruled classes; the body no longer carries the old "holds a seat on
its ground" disjunct), §1 (placement: the predicate is a read-only Query and goes in `queries/world_q.py` beside
`establishment_of`, not in `state/gate.py`; the `[UNVERIFIED]` import question is resolved at the tree: `world_q` already
imports `purview_reaches` and `sworn_to` from the gate, `world_q.py:96-103`), §7/§7b (tests, tier); U3 B21, C3-D5 (this
file is the batch's carrier of the command predicate, before `14_VERBS_BINDING_D_orders.md`), §4.1 row 74 (COLONIAL_B's
`distance` is added in B33); U1 glossary *command basis* ("under the seat" is a refused word; the predicate is
`commands`, the basis value `command`). **One owner.** `14_VERBS_BINDING_D_orders.md` commit D2 writes a second
`commands(w, actor, via, person)` in `state/gate.py` and a `basis: command` value; this file takes BIND_D's name and
signature (the tree's seat-predicate convention: `may_fill`, `may_revoke` take `(w, actor, via, …)`) and is the one
body; BIND_D's edits 3-5 compose on it (for lane W3-4a). The writ-to-a-superior rule (A-22) is a formation rule, not a
fold transformation: the fold refuses an `issue` its addressee is not commanded by, and the chooser forms `petition`
for a superior. The filename keeps its words (no retrofit, CLAUDE.md §4).

## Status: PROPOSED

Lands in batch: **B21** (FA), in C3-D5's order: after `14_VERBS_BINDING_C_turnover.md`'s `revoke` draw at control and
`06_FA_decree_binds.md`, before `16_PESSIMIST_FA_A` and `14_VERBS_BINDING_D_orders.md`. Depends on: `may_revoke`,
`purview_reaches`, `establishment_of`, `place_of`, `World.seat_holds` (all exist); `15_INSTITUTIONS_COLONIAL_B_distance.md`
widens it later (B33, LATER).

Source: `audits/16_PESSIMIST_FA.md` F-PES-FA-03 (premise P1.3; runs `pf2_premise.py` P1, `pf2b_followup.py`
§6, and the residence count in the audit's evidence log, seeds 0 and 1). Binds on, and does not redo:
`06_FA_decree_binds.md` (a writ's terms reach its addressees; the answers), `14_VERBS_BINDING_D_orders.md`
and CP-T09-08 (what an order does), `15_INSTITUTIONS_COLONIAL_B_distance.md` (who hears, and how late; the
`chronicle` channel), `06_FA_levy_through_the_seat_B.md` (the same two predicates for a levy).

## What it changes in `engine/season/` at runtime

1. A seat commands (may `issue` to) three classes of person (A-22): **the sworn** (a live `oblige` to this
   seat, wherever he lives), **the holder of a seat this seat may revoke**, and **an unseated person in its
   land**. A seated resident who is neither sworn nor revocable is no longer commanded by living there; a
   writ to a superior is a petition (the chooser forms `petition`, the existing row). Today the Duke of
   Varfell can address none of Varfell's five members and the Restoration Movement's leader can address
   nobody.
2. `dispatch` asks the same predicate. Today it asks only that the named person exists, so any seat
   holding `dispatch` orders anyone in the world.

Movers: (1) widens `issue`'s admitted set for the sworn and the revocable, and narrows it for seated
residents of other chains of seats (a hash mover either way); (2) narrows `dispatch`'s (a hash mover: FA E-3
reads 12 executed `dispatch` in two seasons). This narrows the ED-IN-0256 (4) basis for `issue` and
`dispatch`, as A-22 says, behind its revert (`basis: purview`).

## The problem (evidence, by execution, `build_realm(0)`)

- `issue`'s cell asks whether the issuing seat's purview reaches the **addressee's place**
  (`effects_information.py:260-262`). Tried for every living individual as addressee: the King 42 of 45;
  the Royal Marshal (a `terr_T1` seat) 15, of eight factions; **the Duke of Varfell 2, both members of the
  Restoration Movement, and none of Varfell's five members; the Restoration leader 0 of 45**.
- Cause: residence is `npcs.yaml`'s authored `home:`, and **18 of 34 seat-holds are held by a person who
  does not live on the seat's ground** (identical at seeds 0 and 1; residence is not seeded). 32 of the 46
  individuals live in the Duchy of Valorsmark; the Duchess of Hafenmark lives at the royal court
  (`b_s_001_court`, `terr_T1`), the Duke of Varfell at an inn in `terr_T1`, the Confessor in a market in
  `terr_T1`, the Restoration leader in `terr_T2`. The Duchess's purview reaches the home of none of
  Hafenmark's four members, herself included.
- `may_fill` and `may_revoke` ask the **seat's rung**, so the Duke of Varfell may appoint the Military
  Jarl and may not write to him: two ladders for one quantity (NERS-S, §0.06).
- `_req_dispatch` (`loop/predicates.py:619-624`): "the named person exists". No purview.

## The resolution, decided

One predicate, a read-only Query in `queries/world_q.py` beside `establishment_of` (`04` PART E step 4 puts
purview, rank and `establishment` reads in `world_q`; the gate asks it only if a Tenure write basis needs it,
and `issue` / `dispatch` write no Tenure):

```
commands(w, actor, via, person_id) -> bool          # queries/world_q.py, beside establishment_of
    seat = w.offices[via]
    person_id in establishment_of(w, via)                          # (i) the sworn: a live `oblige` to this seat
 or any(may_revoke(w, actor, via, w.offices[t.object])             # (ii) the holder of a seat this seat may revoke
        for t in w.seat_holds(person_id) if t.object != via)
 or (not w.seat_holds(person_id)                                   # (iii) an unseated person in its land
     and purview_reaches(w, seat, place_of(w, person_id)))
```

Ladder step 1 (A-22) for the three classes; step 4 for the parts: (i) is the obligee relation
`_ch_post_remit` already reads (`establishment_of` composes on the gate's `sworn_to`); (ii) is `may_revoke`
(`state/gate.py:830`), so whom a seat may order and whom it may dismiss are one relation; (iii) is `issue`'s
cell narrowed to the unseated. No new relation is invented. A court at the capital stays at the capital:
where a person lives no longer decides whose man he is, so `npcs.yaml`'s homes need no edit for governance
to work (whether a duchess should live in her duchy is WR's and CHAR's, cross-listed).

## Exact edits

1. `engine/season/queries/world_q.py`: `commands` as above; `may_revoke` joins the existing
   `from ..state.gate import …` line (`world_q.py:96`). The docstring defines the word (CLAUDE.md §4): *the
   command basis: whom a seat may order (A-22)*.
2. `engine/season/data/requires.py`: the `basis` form gains the value `command`, dispatched to
   `world_q.commands` exactly as `purview` is dispatched to `purview_reaches` (a value of an existing form,
   not a new stem). `engine/season/verb_table.yaml`, row `issue`: its `authority` conjunct `basis: purview` →
   `basis: command` (revert: `basis: purview`). Rung referents keep `purview` (`requisition`, `seize`). An
   `issue` whose addressee is not commanded is refused at the fold on that conjunct; formation does not
   offer it, and the same matter toward a superior is formed as `petition` (A-22: a writ to a superior is a
   petition) through `14_VERBS_BINDING_D_orders.md` edit 6's fan, which reads the person-side reflection of
   this relation.
3. `engine/season/loop/predicates.py::_req_dispatch`: after "the named person exists", refuse
   (`_refuse("not commanded", …)`) unless `world_q.commands(w, a.actor, a.via, subject)`.

Order of edits: 1 → 2 → 3, one commit each; the tests below with edit 1.

## Gate (execution artifacts)

`pf2_premise.py` and `pf2b_followup.py` were lane scratch (not in the repository, U3 §6.2). Written first as
NEW `engine/season/tests/test_command_basis.py`: `test_sworn_man_is_commanded_wherever_he_lives`,
`test_seated_resident_not_sworn_not_revocable_is_not_commanded`, `test_unseated_resident_is_commanded_by_the_land_lord`,
`test_dispatch_to_a_stranger_refused`, `test_holder_of_a_revocable_seat_is_commanded`. Command:
`python -m pytest engine/season/tests/test_command_basis.py -q`. Readings (`build_realm(0)`):

- **G1** Duke of Varfell: admitted addressees include the holders of Varfell seats he may revoke and his
  sworn men, wherever they live (with `16_PESSIMIST_FA_A` edit 2 landed, the three Varfell council holders).
  Restoration leader: still 0 until someone is sworn to his seat (his row lists one obligee, NPC-041; if that
  oath is built, 1). Control: the King's unseated residents are unchanged; his reach over seated residents of
  other chains of seats falls (A-22's narrowing).
- **G2** the Royal Marshal's `dispatch` of the Katepano of Altonia: refused; of an unseated resident of T1
  or a man sworn to the Marshal's seat: `order.given`. The Marshal no longer reaches seated residents of
  other factions.
- **G3** over seeds 0 to 2, two seasons: executed `dispatch` before and after, and the count refused by
  the new clause; a refused share above half means the shipped orders were mostly to strangers, which is
  a finding about formation (the options fan), not a reason to drop the clause.

## Falsifier

If G1 shows the three council holders still refused, the council seats' rungs are not within the ducal
purview (then PES-FA-A edit 2's anchors and this predicate disagree, and the anchor is the defect).

## NERS reading (E last)

- **N.** Top-down: a superior's order has an address. Bottom-up: a subordinate knows whose orders can
  reach him (the seat he swore to, the seat that may dismiss him, his land's lord if he holds no seat).
  Lateral: dismissal and order ask one relation. Cut it and what dies is the difference between a duke and
  a stranger to his own council.
- **R.** Completeness: a rungless seat with sworn men (the oath clause) now has someone to order; a seat
  with no ground, no chain of seats and no sworn (the Restoration leader today) truthfully has nobody.
- **S.** Removes the two-methodology defect; `issue`, `dispatch`, `revoke`, `recruit` (FA-B's levy)
  agree.
- **E, against that.** One predicate of three disjuncts, two call sites. A player can state it in a line.

## Cost class

Small build (one predicate, two call sites, one mover each way). Tier: `opus` for the A-22 reading (the one
judgment: the petition routing), `sonnet`, effort `high`, for the edits. Hash movers declared: `issue`'s
admitted set both ways and `dispatch`'s narrowing (every seeded world with a writ or an order). Lands it: B21,
before `14_VERBS_BINDING_D_orders.md`.
