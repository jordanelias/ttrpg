# U5d-FA — land and its seats pass on a won march into held territory: one writer of title, read from the field's end state

## Status: PROPOSED (a plan for a later implementation lane; nothing here was executed)

Author: U5d closure lane (Fable), 2026-11-12, on Jordan's rulings A-57, A-58 and A-65
(`unified/DECISIONS_ANSWERED.md`), which replace the ladder's reading of D-20 ("presence only"). The
battle side (which end state is the aggressor's win) is `26_MASS_BATTLE_aggression_and_land.md`'s; this
file owns the title write and decides the five land cases that file lists (section "The five open
cases").

Carries: `audits/06_FA_audit_addendum_B.md` F-FA-13, R-22 and C-7 (as re-decided by the rulings);
`architecture/meta/10_FACTIONS_AND_DEPLOYMENT.md:90` (the roster contract's `stakes`: "`holdings` and
`seats`, for what a defeat costs"). Amends by its `Reconciled:` line: `06_FA_war_lives_in_seats_B.md`
edit 6, `14_VERBS_BINDING_E_war_seats.md`, `15_INSTITUTIONS_COLONIAL_D_accomplishment.md` edit 5,
`15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md`, `16_PESSIMIST_FA_A_dismissal_survives_the_king.md`,
`09_WR_world_motion.md` edit 2 and `09_WR_B_draws_not_thresholds.md`.

## The rule, as ruled (quoted from the record; nothing added)

- A-57: *"a won battle takes land if and only if the aggressor marched in an effort to take land (as
  opposed to battle in a neutral location or a defending army wins)"*.
- A-58: *"Seats pass with holdings."* · *"Draw on land taking march means defender retains land."* ·
  *"sending your military into another's territory is a pretty clear sign of aggression"* (purpose is
  read from the act; a casus belli is context for legitimacy and regard, not a precondition).
- A-65: *"uninvited rescuer who beats an invader CAN occupy the territory but it's their choice and with
  that comes all repercussions from doing so or not"*.

So: on a `march` in force onto a rung **another faction holds**, an **aggressor's win over that holder's
own force** moves the `hold` on that rung, and the seats that go with it, to the aggressor. A draw, a
defender's win, and a field on ground no party holds move nothing. A win over an army that is **not the
holder's** (the rescuer's case) moves nothing by itself: the winner may take the place by an act he forms
(A-65).

## What it changes in `engine/season/` at runtime

1. `_eff_march` on the band `Won` (the attacker's own outcome, `seam/ladder.py::field_degree`), when the
   target rung is held by a faction other than the marching seat's, writes the title in the same Change
   as the arrival: the defender's `hold` on the rung closes and the marcher's opens.
2. In that same write, every seat anchored on the taken rung (and on the rungs the taking carries with
   it, by `world_q.occupies`' own reading: a taken territory's settlements) changes hands: the sitting
   holder's seat-`hold` closes and one opens for the taker.
3. `Lost`, a drawn field (when the MB lane's drawn end state lands, A-3), `Unopposed`, `Invested` and
   `Declared` write no title. A march onto a rung no faction holds writes no title (neutral ground).
4. `seize` of a held, occupied place stops being the way a won field is cashed: after (1) the seat's own
   faction already holds it and `_seize_rung` declines (`occupying_faction` returns `None` when
   `holder == mine`). `seize` keeps its Record half, unheld land (`09_WR_world_motion.md` edit 2) and a
   held place entered **without a field** (`Unopposed`), which neither ruling speaks to.

Hash movers (declared): every seeded run in which a `march` on held land reaches `Won`. First reading to
record before the edit: the count of such Events per seed (realm seeds 0–2, the army verbs withheld
today at `data/fixtures.py:1157`, so the expected count is the `march`-by-headcount fields only;
`[unverified]`, not run by this lane).

## The problem (evidence at HEAD `4ae20f0`)

- `loop/effects_combat.py::_eff_march` docstring: *"ONE WRITE IS ADDED, AND IT IS PRESENCE, NOT TITLE …
  no `hold` moves (R-6, β: title moves by `seize`, `give`, `release` or death)"*, and the comment at the
  arrival: *"β, occupation then `seize` … not α (a won field transferring the hold) [ASSUMPTION; medium;
  Jordan to correct; revert: Jordan states α, and title moves here]"*. A-57 and A-58 are that correction,
  with conditions.
- `state/gate.py:291-300`: *"A SEAT IS NEVER SEIZED: a `hold` on an Office is `conferral`'s and `T-o`'s
  alone"*. No tenure-write basis admits a seat changing hands with its ground.
- `architecture/meta/10_FACTIONS_AND_DEPLOYMENT.md:90` names `holdings` and `seats` as the stakes of a
  defeat; the FA addendum measured that the code passes and writes neither (F-FA-13).

## The resolution, decided (and what the rulings do not state)

| # | decision | basis |
|---|---|---|
| 1 | **Aggression is read from the act**: the marching seat's faction (`gate.seat_faction(a.via)`) differs from the target's holder (`world_q.holder_faction_of(target)`) and that holder is not `None`. Both values are already computed in `_eff_march` (`attacker_faction`, `defender_faction`). No purpose operand, no declaration field | A-58 (3) |
| 2 | **Who takes the hold**: the act's actor, exercising `a.via`, as `seize` writes "the ACTOR'S OWN hold" (`_seize_rung`). `[ASSUMPTION; medium; Jordan to correct; revert: the holder of the faction's `head_seat`]` — the rulings say land passes to the aggressor and do not name the person | ladder step 4 (`_seize_rung`) |
| 3 | **Which seats go with the land**: every `Office` whose `rung` is the taken rung, or a `march_target_kinds` rung beneath it that the taking carries. Seats anchored on a duchy or the realm are never taken by a field, because those rungs are not march targets (`rosters.yaml: march_target_kinds` is `[settlement, territory]`) | A-58 (1); `rosters.yaml:1178` |
| 4 | **To whom the seats pass**: the same taker, in the same write ("pass *with* holdings"). He holds them as any holder does and may `confer` them onward; a seat whose row he cannot lawfully sit (`16_PESSIMIST_FA_B` edit 1: a cohort) is closed and left vacant instead. `[ASSUMPTION; medium; Jordan to correct; revert: close the seats and leave them vacant for the taker's conferral, `15_INSTITUTIONS_COLONIAL_D` edit 5's `annex` basis]` | A-58 (1), read literally |
| 5 | **A march by the holder's leave is not aggression** `[ASSUMPTION, marked in A-58]`. Leave is read as a live `covenant` Record between a seat of each faction whose terms name the marcher's faction or the rung (the alliance and passage shape of plan CP-T09-03). Until `covenant` executes in computed play (0 of 10 formed, FA audit E-3) no march is by leave | A-58's own marked assumption; step 4 |
| 6 | **Relief and pursuit**: a march onto a rung the marcher's own faction holds takes nothing (decision 1 is false). A march onto a third party's held rung against an army that is **not the holder's** (the uninvited rescuer; a pursuit of a beaten enemy) passes nothing on a win: the winner stands there and **may** take the place by his own act, `seize` on the occupation licence (`_seize_rung`: his faction mustered there, the place held by another faction). Taking or declining is his choice and every repercussion is read by the ordinary rules (regard, claims, war), none fixed here | A-65 (this row replaces the earlier reading that a win on such a march passed the land) |
| 7 | **A surrender under siege is the aggressor's win by concession** (A-3: the end state is read off which side broke or conceded), so `_eff_surrender`'s cession carries the seats by the same tail | A-3 with A-58 (1) |
| 8 | **`Unopposed` entry into held land** is not a battle. Today's write stands (presence), and the entrant may take the place by `seize` on the occupation licence: the same chosen act A-65 gives the rescuer | ladder step 4 (`_seize_rung`; A-65's shape) |

## Exact edits, by owner, in order

**1. `engine/season/state/gate.py`** (owner of what admits a tenure write). A twelfth basis, `conquest`,
beside `seizure` (`:291-301`), in `tenure_write_basis` (`:1137`): the closure of another person's live
`hold` on (a) a Rung of a `MARCH_TARGET_KINDS` kind or (b) an Office whose `rung` is such a rung, and the
opening of the taker's, when `via` is a seat the actor sits in whose grant carries `MUSTER_ACT`
(`may_muster`'s first two conjuncts). As with `seizure`, the licence (a won field on held land) is the
effect's: the gate reads Tenures and `state/` readers only (K-52). The comment "A SEAT IS NEVER SEIZED"
stays true of `seizure` and gains one line naming `conquest`.

**2. `engine/season/loop/effects_information.py::_take_hold`** (the one tail of a title write; `:978`).
It gains `seats: tuple = ()`: for each `(office_id, sitting_hold)` it closes the sitting hold and opens
the taker's in the same `perform`, each edge named in the Change (G4). `_eff_seize`'s callers pass
nothing and are unchanged. A helper beside it, `seats_on(w, rid) -> tuple`, returns the offices anchored
on `rid` and on the settlements under a territory (`Office.rung`; the descent is `occupies`' own), each
with its live seat-`hold` or `None`.

**3. `engine/season/loop/effects_combat.py::_eff_march`** (owner of what a field writes). After the
arrival is composed and only when `res.degree == WON`, `defender_faction is not None`,
`attacker_faction is not None`, `attacker_faction != defender_faction`, **the beaten side is the holder's
own** (the losers' faction, read as `loop/sides.py::sides_of` derives it, equals
`holder_faction_of(target)`; today every field's defender is the holder's faction, so this conjunct is
true of every field the tree can form, and it becomes live when allied relief forms a field against a
non-holder), and no leave stands (decision 5:
`world_q.passage_granted(w, attacker_faction, defender_faction, target)`, a new Query over live
`covenant` Records, `False` for every world today): join `_take_hold(w, a, target, held, earns=…,
seats=seats_on(w, target))` to the Change. Emit `rung.taken` beside `army.arrived` (one new Event kind on
the `march` row's `emits`, so `standing_routes.kinds.dominance` can list it and the deed ledger's
`took_by_force` reads it). The docstring's "PRESENCE, NOT TITLE" paragraph and the R-6 comment are
rewritten to the rule above; the `[ASSUMPTION … revert: Jordan states α]` tag is removed and A-57/A-58
cited.

**4. `engine/season/loop/effects_information.py::_eff_surrender`** (`:1092`): its `_take_hold` call
passes `seats=seats_on(w, obj)` (decision 7).

**5. `engine/season/rosters.yaml`**: `tenure_write_bases` (or the roster the gate's bases load from;
`[unverified: the roster's key name was not opened]`) gains `conquest`; `standing_routes.kinds.dominance`
gains `rung.taken`; the `march` verb row in `verb_table.yaml` gains `rung.taken` under `emits` at `Won`.

**6. Layer 1 (text owed, not applied; by the ruling, in the same commit as edits 1–5).**
`10_FACTIONS_AND_DEPLOYMENT.md:90`'s `stakes` row is met as written (holdings and seats); the sentence
that title moves only by `seize`, `give`, `release` or death (#453 R-6) gains "or by a won march onto
land another faction holds (A-57, A-58)".

**7. Tests** (`engine/season/tests/test_march.py`, the file that pins exit (i) and R-6/R-7): the β pin is
re-recorded as the rule, with the controls below. Said plainly: this is an intended golden re-pin.

Order: 1, 2, then 3 and 4 together, 5 with 3, 6 and 7 in the same commit. Depends on:
`06_FA_remit_grant_by_row.md` (only commanding seats hold `dispatch`, so the taker is a commander);
`16_PESSIMIST_FA_B_who_may_sit_join_and_declare.md` edit 1 (`may_sit`, for decision 4's cohort case). The
drawn end state is U5b's (`04_MB_*`); this file needs only that a draw is not `Won`.

## Gate (execution artifact)

`python -m pytest engine/season/tests/test_march.py -q` with five hand-built arms on one world, each a
single change from the first: (a) aggressor wins on a held territory with a seat anchored on it → the
rung's `hold` and the seat's `hold` are the taker's, `rung.taken` emitted once; (b) the same field
`Lost` → no tenure moves; (c) the same target unheld → arrival only; (d) the target held by the
marcher's own faction → arrival only; (e) `Unopposed` on held land → arrival only, and a following
`seize` still takes it; (f) a hand-built field on a third party's land against an army that is not the
holder's, won → arrival only, the winner's `seize` candidate forms, and in a twin arm he declines and
no tenure moves; (g) a guest by leave is refused `seize` while the covenant stands. Then the realm instrument: `python -m engine.season.harness.strife 2 0` before and
after, recording the count of `rung.taken`.

## Falsifier

Arm (b) or (c) moving a tenure; arm (a) leaving the seat with its old holder; a seat anchored on a duchy
or the realm changing hands in any arm; `_seize_rung` still admitting a seizure of the rung taken in (a)
(it must decline: own faction holds). Any of these fails the proposal.

## The five open cases (`26_MASS_BATTLE_aggression_and_land.md` §3, §4), decided

| case | decided | basis | edit |
|---|---|---|---|
| the uninvited rescuer who beats an invader on a third party's land | no transfer by the field; he may `seize`, his choice | A-65 | decision 6; edit 3's "beaten side is the holder's own" conjunct |
| an `Unopposed` entry onto held land | no transfer by the arrival; he may `seize` | ladder step 4 (the code's licence; A-65's shape) | decision 8; no code edit |
| where a drawn aggressor's army stands | at its origin: nobody arrives, as `Lost` leaves a routed army (#453 R-7) and as `04_MB_headcount_grade_and_scale.md` writes the drawn band. `[ASSUMPTION; medium; Jordan to correct; revert: the army stands on the ground it contested and may `seize` nothing while the holder's force is unbeaten]` | ladder step 4 (R-7; the MB proposal) | none here; the drawn band's write is the MB lane's |
| does leave shield a guest who attacks his host | no. Leave is consent to presence. A field in which the holder's own faction defends against the guest is itself the absence of consent for that act, so `passage_granted` is not read when the defenders are the holder's faction; the guest who wins is an aggressor who won | ladder step 5, on A-58's own reason ("because the holder consented") | edit 3: the leave conjunct applies only where the beaten side is not the holder's, that is, it shields entry and passage and never an attack on the host |
| is presence by leave occupation | no. `world_q.occupies` (`queries/world_q.py:2152`) declines a faction for which `passage_granted` is true on that rung, so a guest holds no `seize` licence while his leave stands and gains it the moment it ends (the weakness `loop/effects_shared.py::occupying_faction`'s docstring names: "people placed on a territory by other means … occupy it as well") | ladder step 5 | one conjunct in `occupies`; gate arm: an ally mustered by leave is refused `seize`, and admitted after the covenant closes |

## For Jordan: does the winner of a land-taking march choose, as the rescuer does?

A-57 reads as a transfer ("a won battle takes land"); A-65 makes the rescuer's taking a chosen act. Both
are Jordan's words and they describe different winners, so the ladder does not settle whether the
election extends to the aggressor who beats the holder.

- **(A) The win takes the land (built here).** On an aggressor's win over the holder's force the land and
  its seats pass in the field's own effect. A commander who wanted only to punish must hand the place back
  by a later act (`give`, `release`), and the record shows a conquest and a return. Every won invasion is
  a conquest; raids are told as conquests undone.
- **(B) The win opens the choice.** The field writes presence; the winner is put the question that
  season (mandatory, by A-47's form) and takes the land and seats by his own act or declines; until he
  acts the beaten holder still holds. Punitive expeditions and raids are first-class; a victor's restraint
  is a deed others read; the cost is one more formed act per won field and a season in which a routed
  holder still holds title.

This plan builds (A) because A-57's and A-58's words are a transfer, and carries (B) as a fixture arm
`conquest_election` (control `off` = (A)) so the two can be read side by side before the choice is made.

## Not decided here (unstated by the rulings; marked, not assumed)

Whether the taken seats' remit snapshots are re-stamped at
the new hold (they are stamped when a hold opens, `World._grant_remit`, so they will be: `[unverified]`
that this is wanted for a conquered council); what happens to a seat whose faction is not the land's
holder (a Church seat on Crown ground): this plan passes only seats whose `seat_faction` is the defending
faction `[ASSUMPTION; medium; Jordan to correct; revert: every seat on the rung]`.

## NERS (E last)

N: the Layer 1 stakes row has no other carrier; cutting this leaves a defeat costing bodies only
(F-FA-13). R: conquest becomes a strategic act with a visible prize and a visible loss, and a succession
or a council can be changed by a field with nobody watching. S: one tail (`_take_hold`) writes every
title; no second seizure path; the field's end state (A-3) is the only reader of who won. E: one
conditional in one effect, one helper, one basis; legible as "win a march onto their land and it, with
its offices, is yours".

## Cost class

Small build (one basis, one helper, one conditional, one Event kind), one declared re-pin.
