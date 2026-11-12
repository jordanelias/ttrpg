# U5d-FA — land after a march: who stands where, who may take what, and the seats that go with the land (rulings A-57 to A-70)

Reconciled: 2026-11-12, wave 3 (W3-3) — C3-L7 (edit 1: no new `conquest` gate basis; the seats anchored on the seized rung close by the existing `T-o` revocation basis under a new `revocation:` value `holder_of_rung`, data plus its `REVOCATION_RULES` entry), corrected at the tree in two places: `Act.via` is a typed seat id (`state/carriers.py:721`), so the basis is exercised through the seizer's licensing seat and the new rule reads his holdings, not "`via` = his new hold"; and the `claim` basis C3-L7 names for re-opening the seat admits only an heir under a `successions` row (`state/gate.py:236-253`), so the seizer's opening is not admitted by it and is written below as D3's revert (the seats stand vacant for the ordinary `conferral` path) with the two-option note; C3-L12 (the taking is the aggressor's chosen `seize` act, already this file's D1; the field writes no title); A-76 ("For Jordan" block deleted; D7 is ruled B, built switchable); A-85 (D6's pool gains the realm's strife level; the `ED-IN-0352` (3) clause is owed text); 7b-9 (d) (`passage_granted` placed and tested); D8's `[unverified]` deed-lean home resolved at the tree (`data/verbs.py::align_kind`, `:2101-2113`); tier and batch (R3 7b-0; U3 B23).
Reconciled: 2026-11-12, wave-3 mop-up (`unified/work/W3_4a_DONE.md` row 7 and "For another lane", first item; C3-L7): the cession case (`14_VERBS_BINDING_E_war_seats.md`'s `surrender`) named beside the won-field case; edit 2 no longer has `_eff_surrender` pass `seats=` (its actor is the yielder and closes no seats; they pass by the receiver's own act); the `seize_place` name stays `[ASSUMPTION]`.

## Status: PROPOSED (a plan for a later implementation lane; nothing here was executed)

Lands in batch: B23 (land), after `06_FA_war_lives_in_seats_B.md` edit 6, with `14_VERBS_MATERIAL_D_paper.md` §6 (`seize`'s Rung half, moved into B23 by C3-L12) and before `26_MASS_BATTLE_aggression_and_land.md` (U3 §1 item 23).
Depends on: `06_FA_remit_grant_by_row.md` and `16_PESSIMIST_FA_B` edit 1 (B21); `06_FA_war_lives_in_seats_B.md` (B21 edits 1–3, B23 edit 6); `09_WR_strand_conclusion.md` edit 3 (B12); `30_WR_A_the_era_is_a_named_period.md` (B38) for D6's era level only (the level reads nothing until it lands).

Author: U5d closure lane (Fable), 2026-11-12. This file owns the title write and carries Jordan's land
rulings A-57, A-58 and A-65 to A-70 (`unified/DECISIONS_ANSWERED.md`) as settled rules. The battle side
(which end state is the aggressor's win) is `26_MASS_BATTLE_aggression_and_land.md`'s. What an army
carries home (loss kinds, recuperation, fatigue: A-69) is the MB lane's
(`audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md`, being written by that lane; `[not opened]`) and is
pointed to, not restated.

Revision note: written on A-57 and A-58 as a transfer in the field's effect; that design is withdrawn.
A-65 and A-66 made the taking a victor's chosen act; A-67 to A-70 settled the draw, the unopposed entry
and the questions about leave. The file's name is kept so earlier citations resolve.

Carries: `audits/06_FA_audit_addendum_B.md` F-FA-13, R-22, C-7;
`architecture/meta/10_FACTIONS_AND_DEPLOYMENT.md:90` (`stakes`: "`holdings` and `seats`, for what a
defeat costs").

## The settled rules (each from the record; the code fact beside it)

| # | rule | ruling | what the code does today |
|---|---|---|---|
| 1 | A field writes presence, never title | A-66 | `loop/effects_combat.py::_eff_march`: "no `hold` moves (R-6, β)"; its `[ASSUMPTION … revert: Jordan states α]` tag is discharged as ruled |
| 2 | An aggressor who wins on a march into land another holds stands there and **chooses**: seize, occupy without seizing, or withdraw | A-57, A-66 | on `Won` the claimants are relocated (`army.arrived`); `seize` forms on the occupation licence (`loop/effects_information.py::_seize_rung`, `:1038`) |
| 3 | When a place is seized, **the seats that go with it pass with it** | A-58 | not done: `state/gate.py:291-300`, "A SEAT IS NEVER SEIZED" (edit 1, 2) |
| 4 | A rescuer who beats an invader on a third party's land has the same three choices | A-65, A-66 | no such field can form yet (allied relief is unbuilt); when it does, his arrival is the licence |
| 5 | On a **draw** the defender keeps the land; the aggressor's army is back at its station **at once**; the defender's army returns to its own base | A-58, A-67, A-68, A-70 | no band but `Won` and `Unopposed` relocates anyone, so on a draw neither army has left its station; nothing to write |
| 6 | Armies carry **fatigue and losses** back; losses are written; some are injury or flight and partly recuperate; the defender the same `[ASSUMPTION by symmetry, the record's]` | A-69 | the body writes of `_eff_march`; kinds and recovery are the MB lane's |
| 7 | An **unopposed entry** onto held land is a tolerated trespass when the realm's parliament is working and the parties are at peace, **and the holder dislikes it**; it is aggression when there is enough tension or strife | A-68 | not done: today every `Unopposed` arrival occupies (edit 4) |
| 8 | An attack is an attack whoever invited the attacker; standing on land by its holder's leave is not occupying it `[ASSUMPTION, reversible; the record's plain reading, A-70]` | A-70 | not done for the second half (edit 3) |
| 9 | Ground no party holds is outside all of this | A-58 | `occupying_faction` returns `None` for an unheld place; `09_WR_world_motion.md` edit 2 owns it |

## What it changes in `engine/season/` at runtime

1. `seize` of a place carries the seats anchored on it (rule 3).
2. A faction standing on another's land by that holder's leave does not occupy it (rule 8).
3. An `Unopposed` arrival on another's held land takes one graded draw that reads it as a trespass or as
   aggression; only aggression occupies; either way the holder comes to hold a deed against the entrant
   (rule 7).
4. Nothing else: `_eff_march`'s `Won`, `Lost` and (when the MB lane adds it) drawn bands write what they
   write today for station and title.

Hash movers (declared): runs with a `seize` of a rung carrying a seat; every run with an `Unopposed`
arrival on held land (the FA pessimist read `field.unopposed` 8 at seed 2, so this one moves shipped
runs; the first reading to record is the count per seed and the band each entry draws).

## The resolution, decided

| # | decision | basis |
|---|---|---|
| D1 | **The taking is `seize`**, formed by the winner on the occupation licence. Its row and draw are the MATERIAL lane's (`14_VERBS_MATERIAL_D_paper.md` §6); this file changes its tail | A-66; confirmed at the owner (`_seize_rung`, `_take_hold`) |
| D2 | **Which seats**: every `Office` whose `rung` is the seized rung or a `march_target_kinds` rung beneath it that the taking carries (`occupies`' own descent), and whose `seat_faction` is the dispossessed holder's. Seats on a duchy or the realm are never taken this way: those rungs are no march targets (`rosters.yaml:1178`, `[settlement, territory]`), so the throne (`off_king`, `rung: {realm: true}`) cannot pass by arms | A-58 |
| D3 | **To whom** (wave 3, reading (i) of edit 1): the seats close in the seizing act and stand vacant; the ordinary `conferral` path fills them (the seizer where `may_fill` admits him), and a seat he may not sit (`16_PESSIMIST_FA_B` edit 1) stays vacant for another's conferral. The earlier reading (the seizer opens each seat in the same write) needs an opening basis §C.2 does not list (edit 1) and is held as reading (ii), Layer 1 text owed. `[ASSUMPTION; medium; Jordan to correct; `15_INSTITUTIONS_COLONIAL_D` edit 5's `annex` basis is the other carrier named]` | A-58; C3-L7 as corrected at the tree; ladder step 4 (`_seize_rung`: "the title written is the ACTOR'S OWN hold") |
| D4 | **Occupation without seizure** is the state `world_q.occupies` reads, with nothing stored: the holder's `hold` stands; it ends when the occupier leaves, when a `covenant` between seats of the two closes it, when he seizes, or when the holder's counter-march beats him (`14_VERBS_PHYSICAL_B_field_and_ruin.md` B1). The occupier's men eat from his own treasury meanwhile (`07_SE_campaign_supply_and_muster.md` R-SE-34, R-SE-36) | A-66 |
| D5 | **Leave** is read as a live `covenant` Record between a seat of each faction whose terms name the entrant's faction or the rung (plan CP-T09-03's alliance and passage shape). A faction present under it does not occupy. A guest who marches on the holder's own force has attacked: the field forms as any field does and the rules above apply to its result | A-70's plain reading; `[ASSUMPTION, reversible]` as the record marks it |
| D6 | **The unopposed entry's reading is one graded draw**, taken when the arrival is folded, keyed on the act (`state/ids.py::draw_factory`, purpose `entry`). **Pool (tension)**: open strife strands that name both factions (A-45's several strands; `queries/world_q.py::flows_in`, `:5172`), the holder's regard for the entrant below zero (`person_q.regard`), a standing war between the two (`world_q.at_war`, `:3566`), and **the realm's strife level** (A-85: the era reads `troubled`, `30_WR_A_the_era_is_a_named_period.md`'s condition, a world-level read licensed by A-85 as `ED-IN-0352` (3)'s first named exception), each a named level. **Obstacle (peace)**: a base difficulty, raised when the realm's parliament is working (D7) and when no war stands. **Bands**: Overwhelming and Success read as aggression (the entrant occupies; rules 2 and 3 apply); Partial reads as a trespass that the holder may cite as a grievance; Failure reads as a tolerated trespass. In the two trespass bands the entrant does not occupy and holds no `seize` licence. Every level and the band map `[ASSUMPTION; medium; Jordan to correct]`: the ruling gives the inputs and that it is graded, not the numbers. A standing war is a large level, not a bypass (a thing that could go either way goes by a draw) | A-68 (2), (3) and its marked assumption |
| D7 | **"The kingdom parliament is functional."** What the tree has: a body named `Court Parliament` (`rosters.yaml: office_bodies`, faction Valorsmark, function "Recommends policies, nominates Ministers/Rectorates/Magistrates") and an arrangement row `parliamentary_debate` (`arrangements.yaml`, a bench with `disposal_reach: realm`). What it lacks: any seat whose `body` is that body (the one seat with the word, `off_parliamentary_clerk`, sits in `Ministries`), and any reading of a working state; `offices.yaml:150` records the Parliament as "RULED AND NOT BUILT, `H-90`" (plan CR-35 to CR-37). So no referent for "functional" exists in code. Proposed: a Query `world_q.parliament_sits(w) -> bool`, true when a matter under an arrangement of `disposal_reach: realm` was determined within the last declared year by a bench with at least `bench_quorum` live members. It reads acts, stores nothing, and is false in every world today. **Ruled A-76 (B):** any working realm bench stands in until the Court Parliament (H-90) is built and supplies its own working state; built switchable, fixture `parliament_reading: bench | body`, shipped `bench` | found by search at HEAD; A-76 |
| D8 | **The holder dislikes it**: an `army.arrived` Event on land a person holds, by a faction not his own, is a deed against him by the entrant's commander, in every band of D6, so his regard falls by the ordinary deed reading and the grievance is a claim he can cite. `[unverified]` which roster carries a deed kind's lean for `regard` (`person_q.deed_term`, `_lean`); the edit is one row there | A-68 (2): "the land holder WILL dislike it" |

## Exact edits, by owner, in order

**1. No new gate basis (C3-L7). The seats close by `T-o` under a revocation value in data.**
`engine/season/rosters.yaml: revocation_bases` gains `holder_of_rung` (B.7 call 1: "the revocation rule
is data"), and `state/gate.py::REVOCATION_RULES` (`:617`) gains its one rule, `in_holdings(w, actor,
off.rung)` (`:530`): the actor holds the rung the seat is anchored on. (It is the second conjunct of the
existing `rung_above_in_holdings` alone, without the seat-on-the-rung-above conjunct, because a seizer
holds no seat above a seized territory; the import check at `:620-625` refuses a value with no rule.) The
seat rows anchored on a `MARCH_TARGET_KINDS` rung (D2) carry `revocation: holder_of_rung` in
`offices.yaml`; a row whose `revocation:` is anything else passes nothing (the control and the
mutation). `Act.via` is a typed seat id (`state/carriers.py:721`; `04` §B.9), so the closure is exercised
through the seat that licensed the `seize` (today's rule, `remit:issue` through a seat whose purview
reaches the place; "Not decided here" below), and the rule reads the actor's holdings, not the via seat.
"A SEAT IS NEVER SEIZED" (`:291-301`) stays true: no seat is seized, its holder is revoked by the rung's
new holder. `[ASSUMPTION: within one Change, the `T-o` check of a seat's closure sees the seizer's `hold`
on the rung opened earlier in the same effect — basis: `_take_hold` performs the title write first;
verify at build that `tenure_write_basis` reads the post-write store]`.

**The opening, corrected at the tree.** C3-L7 names "the existing claim basis" for the seizer's hold on
the freed seat; `claim` (`state/gate.py:236-253`) admits only an opening of the actor's own `hold` on a
vacant seat whose `successions` title he ended in the same write, so it does not admit a seizer. Two
readings: (i) **taken, conforms**: D3's own revert — the closed seats stand vacant, `world_q.vacancies`
offers them, and they are filled by the existing `conferral` basis through whoever `may_fill` admits (the
seizer, when he holds the seat above or the row's conferral admits him); A-58's "seats pass with
holdings" is then met as "they leave the dispossessed with the land, and the land's new holder fills
them"; (ii) a new opening basis that admits the seizer in the same Change, which is a §C.2 enumeration
change and needs Jordan's amendment (`04:377`: "§C.2's pseudocode is the current, complete test"), text
owed, not applied. This file builds (i). **INCOMPLETE:** whether (i) meets A-58 is U3's to re-check
against C3-L7 (listed in the wave-3 receipt).

**The cession case, beside the won-field case (C3-L7; `14_VERBS_BINDING_E_war_seats.md`'s `surrender`).** A
surrender under siege is the aggressor's win by concession (A-3), but its actor is the **yielder**, not the
receiver (`_eff_surrender` returns `NO_CHANGE` when `receiver == a.actor`; `loop/effects_information.py:1092-1124`),
and `_take_hold` there writes only the rung's hold to `to=receiver`. The seats anchored on the place have other
persons as holders and `04` §C.2 lists no basis by which the yielder's act closes their holds, so the cession
writes no `seats=` and closes none. Those seats pass exactly as after a won field, by the **receiver's** own act
through the same `revocation: holder_of_rung` rows: once he holds the rung, he closes them and fills them by the
existing bases, or chooses not to (A-66). The title half of a won march is `14_VERBS_MATERIAL_D_paper.md`'s
`seize_place` `[ASSUMPTION: the name — that file marks it; G-03's fallback `occupy` collides with A-66's
"occupy without seizing"]`, whose act is the seizer's own; so only that act and `_seize_rung` pass `seats=`.

**2. `engine/season/loop/effects_information.py::_take_hold`** (`:978`, the one tail of a title
changing hands) gains `seats: tuple = ()`: each `(office_id, sitting_hold)` anchored on the seized rung
(helper `seats_on(w, rid, faction)` beside it, decision D2) is closed in the same `perform` by the `T-o`
basis of edit 1, each edge named in the Change; none is opened (reading (i) above). `_seize_rung` (`:1038`) passes it; `_eff_surrender` (`:1092`) does NOT (see "The cession case" below); the Record half of `seize`
passes nothing. `rung.seized` names the seats in its changes; no new kind.

**3. `engine/season/queries/world_q.py::occupies`** (`:2152`) gains two conjuncts: not
`passage_granted(w, faction, holder_faction, rung)` (a new Query over live `covenant` Records, placed in
`queries/world_q.py` beside `occupies`; false in every world today; test
`test_a_faction_present_under_a_live_covenant_does_not_occupy`), and the faction's latest `army.arrived` Event at the rung does not carry
`ending.entry: trespass` (edit 4). `loop/effects_shared.py::occupying_faction`'s docstring loses the
weakness it names.

**4. `engine/season/loop/effects_combat.py::_eff_march`**, the `UNOPPOSED` branch, when the target is
held by another faction: the host takes D6's draw and the arrival Event's `ending` carries `entry:
aggression | trespass` with the band and the named terms (`05_SC_contest_record_on_event.md`'s shape).
New Query `world_q.parliament_sits` (D7); fixtures `entry_draw` (control `off` = every unopposed entry
is aggression, today's behaviour) and `parliament_reading`. The docstring's R-6 tag is replaced by a
citation of the rulings. The drawn band's station writes (rule 5) need no edit; its loss writes are the
MB lane's (rule 6).

**5. The deed row** for D8: a deed's lean is read by `data/verbs.py::align_kind` (`:2101-2113`), which
takes an authored `deed:<kind>` cell of the alignment table (`_load_alignment`, from `rosters.yaml`)
before falling back to the emitting verb's alignment. The edit is one `deed:army.arrived` cell per axis
on that table `[ASSUMPTION; medium; values Jordan's content: the cell must make the holder's regard
for the entrant fall, as A-68 (2) rules]`.

**6. Layer 1 and ledger text (owed, not applied; by the rulings).** `10_FACTIONS_AND_DEPLOYMENT.md:90`'s
`stakes` row is met as written: a defeat puts the holding and its seats at the victor's choice. #453 R-6
stands and gains "a seized place's seats pass with it (A-58)". `ED-IN-0352` (3)'s exception clause
("except where Jordan rules that a draw reads a strife level; the first is A-68") is owed (drafted by
lane 30 §11, A-85; `OWED_TO_UNIFICATION.md` §A), not applied.

**7. Tests**: `engine/season/tests/test_march.py` and the file covering `seize`'s rung half
(`grep -rl "_seize_rung\|rung.seized" engine/season/tests`). The β pin stands; `seize`'s outputs move
where a seat is anchored on the seized place; `Unopposed` arms gain the entry reading. Intended re-pins,
said plainly.

Order: 1, 2 (one commit); 3 with 4 (one commit, behind `entry_draw`); 5; 6 and 7 with each. Depends on:
`06_FA_remit_grant_by_row.md`; `16_PESSIMIST_FA_B` edit 1; `09_WR_strand_conclusion.md` edit 3 (several
strands, for D6's pool); the occasion on which a victor is offered the taking is
`06_FA_war_lives_in_seats_B.md` edit 6.

## Gate (execution artifact)

Hand-built arms on one world, each a single change from the first, in the two test files: (a) aggressor
wins on a held territory with a seat anchored on it carrying `revocation: holder_of_rung`, then seizes →
the rung is the seizer's and the seat's old holder is closed (vacant, offered by `vacancies`; reading
(i) of edit 1); (a′) the same with that seat's `revocation:` null → the seat keeps its holder (C3-L7's
control); (a″) a `surrender` of the same place under siege → the rung is the receiver's and the anchored
seat keeps its holder until the receiver's own `revoke` (the cession case; BIND_E's gate reads it);
(b) wins and does nothing → no tenure moves, `occupies` true, the holder still holds; (c) wins and
leaves → `occupies` false; (d) `Lost` → nobody arrives, `seize` refused; (e) a seat on the duchy above
keeps its holder in every arm; (f) a faction present under a live covenant is refused `seize`, admitted
after it closes; (g) an `Unopposed` entry over 20 dice seeds with no strand, neutral regard, no war and
`parliament_sits` true reads trespass in most seeds **and not all**, and the holder's regard for the
entrant falls in every seed; (h) the same entry with an open strand between the factions and a standing
war reads aggression in most seeds and not all; (i) `entry_draw: off` reproduces today's hash. Then
`python -m engine.season.harness.strife 2 0` before and after, recording `rung.seized`, the seat-hold
changes that cite it, and the entry bands.

## Falsifier

A tenure moved by a field; arm (a) leaving the seat with its old holder; arm (a′) closing it; arm (b) moving a tenure; a
duchy or realm seat changing hands by a seizure; a guest by leave admitted to `seize`; arm (g) or (h)
giving one reading in every seed (a fixed outcome); a trespass that leaves the holder's regard
unmoved.

## Not decided here (unstated by the rulings; marked)

Which person on the winning side may seize is today's rule (`remit:issue` through a seat whose purview
reaches the place), so a commander holding `dispatch` and not `issue` cannot take the place himself:
content on `offices.yaml` rows. Whether a seized seat's remit snapshot is re-stamped (it is stamped when
a hold opens, `World._grant_remit`; `[unverified]` that this is wanted). How long an occupation may
stand. Whether an entrant read as a trespasser who stays is read again next season (this plan reads the
entry once, at arrival).

## NERS (E last)

N: the Layer 1 stakes row has no other carrier; without the seats a conquest changes a map and no
government (F-FA-13). R: one win, three victories (conquest, occupation, the raid that goes home); a
crossing that is a courtesy in a calm realm and an invasion in a tense one, with nobody watching; an
occupied duke who still holds and can treat, resist or wait. S: one tail writes every title; one
reading of occupation; the entry's draw is the ladder's, its record the contest record's. E: "win, and
the land is yours to take, hold or leave; walk in unopposed, and how it is taken depends on the times".

## Cost class

Small build (edits 1 to 3), design-first for the levels of D6 and for D7's referent, one declared
re-pin per commit. Tier: edits 1–2 (the seats mechanism) `opus` with a `sonnet` critic; the rest
`sonnet` (R3 7b-0).
