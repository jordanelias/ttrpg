# PES-FA-C — "under the seat" is one predicate: the seat's ground, its ladder, and its sworn

Reconciled: 2026-11-12, U5d closure — folded **A-22** (command). `under_seat` is rewritten to the ruled three classes: (i) the sworn (a live `oblige` to this seat; the third disjunct, unchanged), (ii) the holder of a seat this seat may revoke (`may_revoke`, replacing the second disjunct "he holds a seat on its ground"), (iii) an **unseated** person in its land (the first disjunct, narrowed: `purview_reaches(seat, place_of(person))` and the person holds no seat). A seated resident who is neither sworn nor revocable is no longer under the seat by living there. A writ to a superior is a petition: edit 2 routes a Person referent who fails `under_seat` to the petition form, not to a refusal. Edit 3 (`dispatch` asks the same predicate) stands; this narrows the ED-IN-0256 (4) basis for `issue` and `dispatch` behind its revert, as the ruling says. Gate arms rewritten: the Duke of Varfell reaches the holders of Varfell seats he may revoke and his sworn men, wherever they live; the Royal Marshal no longer reaches seated residents of other factions.

## Status: PROPOSED

Source: `audits/16_PESSIMIST_FA.md` F-PES-FA-03 (premise P1.3; runs `pf2_premise.py` P1, `pf2b_followup.py`
§6, and the residence count in the audit's evidence log, seeds 0 and 1). Binds on, and does not redo:
`06_FA_decree_binds.md` (a writ's terms reach its addressees; the answers), `14_VERBS_BINDING_D_orders.md`
and CP-T09-08 (what an order does), `15_INSTITUTIONS_COLONIAL_B_distance.md` (who hears, and how late; the
`chronicle` channel), `06_FA_levy_through_the_seat_B.md` (the same two predicates for a levy).

## What it changes in `engine/season/` at runtime

1. A seat may address (`issue`) a person who lives on its ground (today's rule), **or who holds a seat on
   its ground, or who is sworn to it**. Today the Duke of Varfell can address none of Varfell's five
   members and the Restoration Movement's leader can address nobody.
2. `dispatch` asks the same predicate. Today it asks only that the named person exists, so any seat
   holding `dispatch` orders anyone in the world.

Movers: (1) widens `issue`'s admitted set (a hash mover where a seat-holder forms a writ to a person it
now reaches); (2) narrows `dispatch`'s (a hash mover: FA E-3 reads 12 executed `dispatch` in two seasons).

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

One predicate, in the gate, beside `purview_reaches`:

```
under_seat(w, seat: Office, person_id) -> bool
    purview_reaches(w, seat, place_of(person))                      # the ground (today)
 or any(purview_reaches(w, seat, w.offices[t.object].rung)         # the ladder: he holds a seat on it
        for t in w.seat_holds(person_id) if t.object != seat.id)
 or person_id in establishment_of(w, seat.id)                       # the sworn: a live `oblige` to this seat
```

Ladder step 4: the first disjunct is `issue`'s cell; the second is `may_fill`'s reading; the third is the
obligee relation `_ch_post_remit` already reads. No new relation is invented. A court at the capital stays
at the capital: where a person lives no longer decides whose man he is, so `npcs.yaml`'s homes need no
edit for governance to work (whether a duchess should live in her duchy is WR's and CHAR's, cross-listed).

## Exact edits

1. `engine/season/state/gate.py`: `under_seat` as above (reads `purview_reaches`, `World.seat_holds`; the
   establishment read is `queries/world_q.py::establishment_of`, which the gate may not import: the
   third disjunct is written as the live-`oblige` scan `establishment_of` performs, or the Query is moved
   under the gate as `seated_on_the_rung_above` was `[UNVERIFIED: which of the two the import graph
   allows]`).
2. `engine/season/data/requires.py`, the `purview` basis: when the referent is a Person, ask `under_seat`
   instead of `purview_reaches(seat, place)`. Rung referents are unchanged (`requisition`, `seize`).
3. `engine/season/loop/predicates.py::_req_dispatch`: after "the named person exists", refuse
   (`_refuse("not under the seat", …)`) unless `under_seat(w, w.offices[a.via], subject)`.

## Gate (execution artifacts)

Re-run `pf2_premise.py 0` (P1.3):

- **G1** Duke of Varfell: admitted addressees include the three holders of Varfell's council seats.
  Restoration leader: still 0 until someone is sworn to his seat or seated under it (his row lists one
  obligee, NPC-041; if that oath is built, 1). Control: the King's 42 and the Marshal's 15 residents are
  unchanged.
- **G2** the Royal Marshal's `dispatch` of the Katepano of Altonia: refused; of the Guard Captain
  (resident under T1's parent or seated on T1): `order.given`.
- **G3** over seeds 0 to 2, two seasons: executed `dispatch` before and after, and the count refused by
  the new clause; a refused share above half means the shipped orders were mostly to strangers, which is
  a finding about formation (the options fan), not a reason to drop the clause.

## Falsifier

If G1 shows the three council holders still refused, the council seats' rungs are not within the ducal
purview (then PES-FA-A edit 2's anchors and this predicate disagree, and the anchor is the defect).

## NERS reading (E last)

- **N.** Top-down: a superior's order has an address. Bottom-up: a subordinate knows whose orders can
  reach him (his ground's lord, his ladder's, the seat he swore to). Lateral: appointment, dismissal, levy
  and order ask one relation. Cut it and what dies is the difference between a duke and a stranger to his
  own council.
- **R.** Completeness: a rungless seat with sworn men (the oath clause) now has someone to order; a seat
  with no ground, no ladder and no sworn (the Restoration leader today) truthfully has nobody.
- **S.** Removes the two-ladder defect; `issue`, `dispatch`, `confer`, `revoke`, `recruit` (FA-B's levy)
  agree.
- **E, against that.** One predicate of three disjuncts, two call sites. A player can state it in a line.

## Cost class

Small build (one predicate, two call sites, one mover each way).
