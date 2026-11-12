# U5d-FA — after a won march: seize, occupy or withdraw. One writer of title, and the seats go with the land when it is taken

## Status: PROPOSED (a plan for a later implementation lane; nothing here was executed)

Author: U5d closure lane (Fable), 2026-11-12, on Jordan's rulings A-57, A-58, A-65, A-66 and A-67
(`unified/DECISIONS_ANSWERED.md`), which replace the ladder's reading of D-20. This file owns the title
write. The battle side (which end state is the aggressor's win) is
`26_MASS_BATTLE_aggression_and_land.md`'s; the five land cases that file lists are decided below.

Revised twice on the day: first written on A-57 and A-58 as a transfer in the field's own effect; A-65
made the rescuer's taking a chosen act; A-66 then ruled the same choice for every winner. The transfer
in `_eff_march` is withdrawn. What remains is smaller and closer to the code as built.

Carries: `audits/06_FA_audit_addendum_B.md` F-FA-13, R-22 and C-7;
`architecture/meta/10_FACTIONS_AND_DEPLOYMENT.md:90` (the roster contract's `stakes`: "`holdings` and
`seats`, for what a defeat costs"). Amends by their `Reconciled:` lines: `06_FA_war_lives_in_seats_B.md`
edit 6, `14_VERBS_BINDING_E_war_seats.md`, `15_INSTITUTIONS_COLONIAL_D_accomplishment.md` edit 5,
`15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md`, `16_PESSIMIST_FA_A_dismissal_survives_the_king.md`,
`09_WR_world_motion.md` and `09_WR_B_draws_not_thresholds.md`.

## The rule, as ruled (quoted from the record)

- A-57: *"a won battle takes land if and only if the aggressor marched in an effort to take land (as
  opposed to battle in a neutral location or a defending army wins)"*.
- A-58: *"Seats pass with holdings."* · *"Draw on land taking march means defender retains land."* ·
  *"sending your military into another's territory is a pretty clear sign of aggression"*.
- A-65: *"uninvited rescuer who beats an invader CAN occupy the territory but it's their choice and with
  that comes all repercussions from doing so or not"*.
- A-66: *"yes, a land taking aggressor can choose to occupy without seizing territory, which has
  historical precedent"*.
- A-67: a drawn aggressor's army returns to its original station, where its march began.

Read together: a field never writes title. An aggressor who wins on a march into land another holds
stands on that land and **chooses**: **seize** (the title passes, and the seats that go with the land
pass with it), **occupy without seizing** (his army holds the ground; title and seats stay with the
holder, whose claim stands), or **withdraw**. The rescuer who beats an invader on a third party's land
has the same three. A draw or a defender's win leaves the aggressor nowhere to choose from: he does not
stand on the ground. Ground no party holds is outside the rule.

## Confirmed against the title owner (the record's marked assumption)

A-66's record marks as an assumption that seizure is an act the aggressor forms after the win, not a
default. The code agrees and already has the act:

- `loop/effects_combat.py::_eff_march`: on `Won` and `Unopposed` the claimants are relocated and
  `army.arrived` is emitted; *"no `hold` moves (R-6, β: title moves by `seize`, `give`, `release` or
  death)"*, tagged `[ASSUMPTION; medium; Jordan to correct; revert: Jordan states α, and title moves
  here]`. A-66 keeps β: the tag is discharged as ruled, not reverted.
- `loop/effects_information.py::_seize_rung` (`:1038`): *"THE LICENCE IS OCCUPATION"*: the exercised
  seat's faction stands at the place and another faction holds it. It *"asks nothing of the defenders:
  an opposed `Won` that removed nobody still leaves the attacker mustered there, so the seizure is
  admitted"*. Its tail is `_take_hold` (`:978`), the one writer of a title changing hands.
- `loop/effects_shared.py::occupying_faction` (`:149`): *"A defended territory therefore stays its
  holder's AGAINST A MARCH: one that lost never arrived, so nothing occupies and nothing is seized."*

So the three choices exist today as: form `seize`; form nothing; move the army away. No flag to Jordan
follows from the confirmation: the game is the one A-66 describes.

## What it changes in `engine/season/` at runtime

1. `seize` of a place carries the **seats anchored on it** (A-58). Today it moves the rung's `hold` only,
   and the gate states *"A SEAT IS NEVER SEIZED"* (`state/gate.py:291-300`).
2. A faction standing on another's land **by that holder's leave** does not occupy it, so it holds no
   licence to seize while the leave stands (A-58's marked assumption, made a rule).
3. Nothing else. `_eff_march` writes what it writes today. Occupation without seizure is the state
   `world_q.occupies` already reads (`queries/world_q.py:2152`).

Hash movers (declared): runs in which a `seize` of a rung executes on a place with a seat anchored on
it (`seize` 0 of 14 executed at seed 1 in the WR pessimist's reading, so the first reading is expected
near zero; `[unverified]`, not run by this lane); runs in which a guest by leave formed a `seize` (none
possible today: `covenant` executes 0 of 10).

## The resolution, decided

| # | decision | basis |
|---|---|---|
| 1 | **The field writes presence, never title.** The winner's army arrives (`Won`, `Unopposed`); nothing arrives on a draw or a loss | A-66; `_eff_march` as built |
| 2 | **The taking is `seize`, formed by the winner**, on the occupation licence. Its row and its draw are the MATERIAL lane's (`14_VERBS_MATERIAL_D_paper.md` §6); this file changes its tail only | A-66 (record's assumption, confirmed above) |
| 3 | **Seats go with the land when it is seized**: every `Office` whose `rung` is the seized rung, or a `march_target_kinds` rung beneath it that the taking carries (`occupies`' own descent). Seats anchored on a duchy or the realm are never taken this way, because those rungs are not march targets (`rosters.yaml:1178`: `[settlement, territory]`); the throne (`offices.yaml`: `off_king`, `rung: {realm: true}`) is one of them | A-58 (1) |
| 4 | **To whom**: the seizer, in the same write ("pass *with* holdings"); a seat he may not sit (`16_PESSIMIST_FA_B` edit 1: a cohort) is closed and left vacant. Only seats of the dispossessed holder's faction pass. `[ASSUMPTION; medium; Jordan to correct; revert: the seats close and stand vacant for the seizer's conferral (`15_INSTITUTIONS_COLONIAL_D` edit 5's `annex` basis); or every seat on the rung]` | A-58 (1), read literally; ladder step 4 (`_seize_rung`: "the title written is the ACTOR'S OWN hold") |
| 5 | **Occupation without seizure is a state with its own readings**, none stored: the holder's `hold` stands; `occupies(rung, faction)` is true of the occupier; it ends when the occupier leaves (`march`, `move`), when a `covenant` between seats of the two closes it, when he later seizes, or when the holder's counter-march beats him (`14_VERBS_PHYSICAL_B_field_and_ruin.md` B1 forms a field against a non-holder on the marcher's own land). The occupier's army eats from his own treasury while it stands on land his faction does not hold (`07_SE_campaign_supply_and_muster.md` R-SE-34, R-SE-36) | A-66 ("a recognised state … ends by treaty, withdrawal, a later seizure or a counter-march") |
| 6 | **Leave**: a faction standing on another's land under a live `covenant` between a seat of each faction that names the marcher's faction or the rung does not occupy it. Until `covenant` executes in computed play (0 of 10 formed, FA audit E-3) nobody stands anywhere by leave | A-58's marked assumption; plan CP-T09-03's alliance and passage shape |
| 7 | **A surrender under siege** is a cession (a title write through the same tail), so it carries the seats as a seizure does | A-3 (the end state is read off which side broke or conceded) with A-58 (1) |

## The five open cases (`26_MASS_BATTLE_aggression_and_land.md` §3, §4), decided

| case | decided | basis | edit |
|---|---|---|---|
| the uninvited rescuer who beats an invader on a third party's land | he stands there and chooses: seize, occupy or withdraw | A-65, A-66 | none: when allied relief forms such a field his arrival gives him the licence `_seize_rung` already reads |
| an `Unopposed` entry onto held land | the same three choices: he arrived, so he occupies | ladder step 4 (`_eff_march` arrives on `Unopposed`; `_seize_rung`'s licence) | none |
| where a drawn aggressor's army stands | **ruled (A-67): it returns to its original station, where its march began.** In the code this is no journey: `_eff_march` relocates claimants only on `Won` and `Unopposed`, so on a draw (as on `Lost`, #453 R-7) the army was never moved from its station. Unstated by A-67 and decided here by the ladder: (i) the return is immediate, not a march that takes time or can be contested, because the loop carries no army between stations (a `march` is one act resolved in one season; a pursuit is inside the field, the MB lane's pursuit draw); (ii) the defender's army keeps its station, since no band relocates a defender; (iii) what the returning army carries back in losses is the drawn band's body write, each side's share (`04_MB_headcount_grade_and_scale.md`), and fatigue has no carrier across seasons in the field today, so none is carried: both are the MB lane's to change. None is flagged: each follows from what the loop can represent, and the alternative (an army in transit as a state) is a build nobody has asked for | A-67; ladder step 4 (`_eff_march`; R-7) and step 5 | none here; the drawn band's write is the MB lane's |
| does leave shield a guest who attacks his host | no. Leave is consent to presence. A guest who marches on the holder's own force has ended his leave by the act: the field forms as any field does, and if he wins he occupies as an aggressor does | ladder step 5, on A-58's own reason ("because the holder consented") | edit 3's conjunct reads leave **at the time of asking**; a `march` by the guest against the holder's faction on that rung closes the reading for that rung (the covenant's own breach is the instruments kit's, `15_INSTITUTIONS_COLONIAL_A_instruments.md`: `breaches`) |
| is presence by leave occupation | no | ladder step 5 | edit 3 |

## Exact edits, by owner, in order

**1. `engine/season/state/gate.py`** (owner of what admits a tenure write). A twelfth basis,
`conquest`, beside `seizure` (`:291-301`), in `tenure_write_basis` (`:1137`): the closure of another
person's live `hold` on an Office whose `rung` is a `MARCH_TARGET_KINDS` rung, and the opening of the
seizer's, in the same Change as a `seizure` of that rung or a rung above it in the taking, when `via` is
the seat the seizure is exercised through. As with `seizure`, the licence is the effect's (K-52): the
gate reads Tenures and `state/` readers only. The comment "A SEAT IS NEVER SEIZED" stays true of
`seizure` and gains one line naming `conquest`.

**2. `engine/season/loop/effects_information.py::_take_hold`** (`:978`, the one tail of a title write).
It gains `seats: tuple = ()`: for each `(office_id, sitting_hold)` it closes the sitting hold and opens
the taker's in the same `perform`, each edge named in the Change (G4). A helper beside it,
`seats_on(w, rid, faction) -> tuple`, returns the offices anchored on `rid` and on the settlements under
a territory (`Office.rung`; the descent is `occupies`' own) whose `seat_faction` is `faction`, each with
its live seat-`hold` or `None`. `_seize_rung` (`:1038`) and `_eff_surrender` (`:1092`) pass
`seats=seats_on(w, rid, dispossessed_faction)`; the Record half of `seize` passes nothing. The Event
`rung.seized` (the kind the deed ledger already reads as dominance:
`15_INSTITUTIONS_PAPACY_C`'s `deed_doers` lists it) names the seats in its changes; no new kind.

**3. `engine/season/queries/world_q.py::occupies`** (`:2152`, the one reading of occupation). One
conjunct: not `passage_granted(w, faction, holder_faction, rung)`, a new Query over live `covenant`
Records between seats of the two factions whose terms name the faction or the rung; `False` for every
world today. `occupying_faction`'s docstring loses its named weakness for the guest's case.

**4. `engine/season/loop/effects_combat.py::_eff_march`.** No code edit. The docstring's R-6 tag
(`[ASSUMPTION … revert: Jordan states α]`) is replaced by a citation of A-57, A-58 and A-66: presence is
the field's write by ruling.

**5. Layer 1 (text owed, not applied; by the rulings, in the same commit as edits 1–3).**
`10_FACTIONS_AND_DEPLOYMENT.md:90`'s `stakes` row is met as written: a defeat puts the holding and its
seats at the victor's choice. #453 R-6's sentence (title moves by `seize`, `give`, `release` or death)
stands and gains "and a seized place's seats pass with it (A-58)".

**6. Tests** (`engine/season/tests/test_march.py` and the file covering `seize`'s rung half; find it with
`grep -rl "_seize_rung\|rung.seized" engine/season/tests`). The β pin stands. Added arms below. Said
plainly: `seize`'s golden outputs move where a seat is anchored on the seized place; an intended re-pin.

Order: 1, 2, 3, then 4 to 6 in the same commit. Depends on: `06_FA_remit_grant_by_row.md` (which seats
hold `issue` and `dispatch`); `16_PESSIMIST_FA_B_who_may_sit_join_and_declare.md` edit 1 (`may_sit`).
The occasion on which the winner is offered the taking is `06_FA_war_lives_in_seats_B.md` edit 6 (plan
CP-T09-04 (d) widened to rungs his faction occupies whatever their holder).

## Gate (execution artifact)

`python -m pytest engine/season/tests/test_march.py -q` and the `seize` file, with hand-built arms on
one world, each a single change from the first: (a) aggressor wins on a held territory with a seat
anchored on it, then forms `seize` → the rung's `hold` and the seat's `hold` are the seizer's; (b) the
same win and no `seize` → no tenure moves in any later season, `occupies` is true, and the holder's
`hold` stands; (c) the same win, then the army moves away → `occupies` false, nothing moved; (d) the
field `Lost` → nobody arrives, `seize` refused; (e) `Unopposed` on held land → as (a) and (b); (f) a
seat anchored on the duchy above the seized territory keeps its holder in every arm; (g) a faction
standing there under a live covenant is refused `seize`, and admitted after the covenant closes. Then
the realm instrument: `python -m engine.season.harness.strife 2 0` before and after, recording
`rung.seized` and the seat-hold changes that cite it.

## Falsifier

A tenure moved by the field itself in any arm; arm (a) leaving the seat with its old holder; arm (b)
moving a tenure; a seat on a duchy or the realm changing hands by a seizure; a guest by leave admitted
to `seize`.

## Not decided here (unstated by the rulings; marked, not assumed)

Which person on the winning side may seize is today's rule (eligibility `remit:issue` through a seat
whose purview reaches the place), so a commander whose seat holds `dispatch` and not `issue` wins the
field and cannot take the place himself; that is content on `offices.yaml` rows
(`06_FA_remit_grant_by_row.md`) and is left there. Whether a seized seat's remit snapshot is re-stamped
at the new hold (it is stamped when a hold opens, `World._grant_remit`: `[unverified]` that this is
wanted for a conquered council). How long an occupation may stand is not bounded by any rule here.

## NERS (E last)

N: the Layer 1 stakes row has no other carrier, and without the seats a conquest changes a map and no
government (F-FA-13). R: three different victories from one win (conquest, occupation, the raid that
goes home), each read by everyone who learns of it; a victor's restraint is a deed; an occupied duke
still holds and can treat, resist or wait, with nobody watching. S: one tail writes every title; the
field's end state decides only who stands where; leave is one conjunct in the one reading of
occupation. E: "win, and the land is yours to take, hold or leave" is one sentence, and the build is one
basis, one helper and one conjunct.

## Cost class

Small build, one declared re-pin.
