"""v9 IN-21 -- FORCE-WEATHER: a keyed seasonal draw on MATTER's yield term (`H-26`).

The draw is `world_q.season_factor_of`, read at the yield step in `loop/matter.py`; its distribution is
the `season_factor_draw` fixture (one tuple of equally likely multipliers per season of the year,
`()` = off). Each test asks the real MATTER barrier, never a re-derivation of the arithmetic.

THE FALSIFIERS, each with the failure it would show:
  * CONTROL: with the draw off, `build_realm(0)`'s content hash is the pre-change reading at build, after
    one season and after two; and, on the one-town world, a declared all-1.0 table (the draw ON but
    degenerate) reads the same as no table over two seasons -- a draw that perturbed the arithmetic
    when it multiplies by 1.0 would move it;
  * DROUGHT: a drought-only table leaves the larder below the control arm's after the same barriers,
    and the control arm emits no `shortfall:` observation where the drought arm does;
  * KEYED: the same seed twice gives one hash; a different seed reads a different factor sequence; the
    factor at a tick is the table's entry at `tick % len(table)` (the season of the year, read off the
    clock and stored nowhere).
"""

from __future__ import annotations

import hashlib

from ..data.matrix import Step, WriteClass
from ..data.requires import SHORTFALL_PREDICATE
from ..harness import populated as POP
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.carriers import Person, Rung, Site, Tenure
from ..state.world import World

DEFAULT = POP.P.DEFAULT_FIXTURES

# `build_realm(0)`'s content hash, originally on the base commit (068ec322, re-pinned below), taken before this position changed
# anything: at build, after one season, after two. With `season_factor_draw` at its shipped `()` all
# three must still read these.
# RE-PINNED 2026-10-11 (Jordan's ruling "null" on seven `offices.yaml` seats): `Office.revocation` is in
# the content hash, and seven seats moved from `rung_above_same_faction` to `null`. Restoring those seven
# values on the built world reproduces the old three hashes (2d0d1200..., a53cceff..., 286fd568...)
# exactly, so the move is that data change alone.
# RE-PINNED at v9 IN-34, A SCHEMA MOVE DECLARED: `Person.born` adds a field to every person's `repr`,
# which `content_hash` folds, so all three move with the bodies clock at its control (both rates 0).
# Was 5812a959... / 0d4f7ae4... / 6bc6123e.... The ordered (kind, id) event sequence over one and two
# seasons is identical to the pre-IN-34 base's (`BASE_EVENTS`, below), so the move is the field alone.
# RE-PINNED 2026-10-12 (`rung_above_in_holdings`, Jordan's holdings ruling): `off_duchess_hafenmark` and
# `off_duke_varfell` moved from `rung_above_same_faction` to the new basis, a data change alone
# (`Office.revocation` is hashed). Was 0a7e27c4... / d188461a... / 33b1ae3b.... `BASE_EVENTS` below is
# unchanged, which is the proof that no event moved.
# RE-PINNED at v9 IN-53 (H-207, DECISION 2026-10-13 D1/D2), A DELIBERATION MOVE DECLARED BY OUTCOME:
# `confer` now forms only on a referent its question carries as `Office` (the vacant seats a conferrer
# may fill, riding on the question he answers), so its always-refused attempts on persons, Sites and
# Records stop from season 1; `revoke` and every other row form exactly as before (the class is a
# partition). The build hash is unchanged (nothing stored moves). Was c2230a36... / 88f6f243... after
# one and two seasons at e716f10b; `BASE_EVENTS` re-recorded with it (was 7526/e56f8652...,
# 21508/dc3c440a...).
# IN-10 (c) (a writ minted into its addressee's hand) WAS PINNED HERE AND IS REVERTED, 2026-10-14
# (ED-IN-0292 (1), the user: no): the hashes below are the pre-(c) values, 56d44b5a... / 808951dd...
# after one and two seasons, reproduced exactly; `BASE_EVENTS` likewise (7527/05d85451...,
# 21735/680e93d8...).
# RE-PINNED at v9 SC-03a, A SCHEMA MOVE DECLARED: the docket item gains `arrangement` and `petition`
# (both None on the realm's one item, `b_s_036_cathedral`, since no computed `open_case` names a row),
# and `content_hash` folds a docket item as a sorted dict of reprs. Was 56d44b5a... / 808951dd...
# after one and two seasons. The build hash and `BASE_EVENTS` are unchanged; deleting the two keys from
# the docket after each season reproduces the old pair exactly, so the move is the keys alone.
# RE-PINNED at v9 IN-57 (B-W), A HASH MOVE DECLARED: the attention key re-orders each person's questions
# and `Claim.doer` is a hashed field. Was 0f8e0144... / ccb33d62... after one and two seasons; the build
# hash is unchanged. The base values reproduce on the pre-IN-57 commit 5b5e31ef; IN-58 moved nothing.
# RE-PINNED at v9 IN-64 (B-X), A DATA MOVE DECLARED: the cast's fifteen pursuits and three-concern
# affiliations (ED-IN-0293, `4e942bac`), opponents at 0 (IN-63), and the two Riskbreakers seat rows
# (anchored at T1). Every stored vector of the 46 cast persons moves, so the build hash moves too.
# Was 11989dcf... / 8840d8f9... / 2eedf7b0... (build, one, two seasons) on IN-63's tree e6adc4bf.
# RE-PINNED at v9 IN-71 (B-X), A MECHANISM MOVE DECLARED: `crisis_weights` scales `doctrine` by religious
# conviction (H-188). The BUILD hash is equal (no stored vector moved); one and two seasons moved,
# a0e82b82... -> cc650fcf... and dc561dd5... -> 8f4d2088...; `BASE_EVENTS` re-recorded with them.
# RE-PINNED at v9 FA-05 (B-X), MECHANISM AND DATA MOVES DECLARED, taken once for the three movers since the
# last pin: IN-69 (salience orders questions within tiers 0 and 3: one season 9095b921... -> a74673b1...,
# the build hash equal), IN-72 (equal in seed 0) and FA-05 (nine goal rows seeded: the build hash moves, 25
# commits and 29 stance rows, plus the `influences` seeding fix, 29 and 33). The pin sat red between IN-69's
# commit and this one (no per-item run of this file). Was 33c20c4c... / 9095b921... / 10b1abab...
# RE-PINNED at v9 FA-06 (B-X), A DATA MOVE DECLARED: 26 goal rows beside FA-05's nine (35; 12 mint a
# Proposition, 23 are orientations; commits 29 -> 55, stance rows 33 -> 44), and the Inquisitors' row now
# `establishes` over the Church's heresy goal. Was 41fdb685... / c7f7506f... / ec6b82f3... (build, one, two
# seasons); one season 585 -> 602 acts, `fight` 4 -> 4 (Olafsson on Haelgrund gone, Jarnstal on Vossen new).
# RE-PINNED at the v9 B-X BATCH-CLOSE (d84e98eb), A DATA MOVE DECLARED: `goals.yaml`'s two heresy goals'
# `text:` changed and a Proposition's value is hashed, so all three hashes moved; the event counts and digests
# below are unchanged. Was 545729e9... / 93608c22... / 61782df4... (build, one, two seasons).
# RE-PINNED at v9 IN-10 (B-K), A BEHAVIOUR MOVE DECLARED: `issue` joined the known-person fan for `to`
# (its `terms` conjunct binds `subject`; a writ with nothing to say about its terms is declined) and a
# fanned row's bags gain a held Record's addressee (`record_sourced_operands`). The build hash is equal;
# one and two seasons move. Was bb08f4b2... / cdeda7fd... (one, two seasons); `aperture 1 0` realm acts
# 602 -> 598, `issue` attempted 3 -> 2 (executed 1 -> 1), `requisition` attempted 3 -> 2.
# RE-PINNED at v9 IN-45 `forge` (B-K), A BEHAVIOUR MOVE DECLARED: `forge` entered `resolvable_verbs()`
# (typed with `survey`'s cell, `_eff_forge`), so the chooser offers it. The build hash is equal; one and
# two seasons move. Was 5bbcba33... / 39bf9d83... (one, two seasons). CONTROL, run: the same tree with
# `forge` withheld from the chooser's verbs reproduces both old values exactly, so the sheet consumer
# (`record_sourced_operands.faction_sheet`) and the shared mint move nothing here. `forge` wrote no
# `forgery_quality` then (`H-210`, deferred to SC-02 `22b`, which writes it -- re-pinned below).
# RE-PINNED at v9 IN-12 `survey` + Rung (B-K), A BEHAVIOUR MOVE DECLARED: a Rung subject is answered by
# `world_q.holder_faction_of` (`loop/effects_information.py::_resolved_sheet`), so a survey -- and a
# forge, which shares the helper -- of a held place mints instead of declining. The build hash is equal;
# one and two seasons move. Was 002af955... / 1282141c... (one, two seasons). CONTROL, run: the same tree
# with the rung branch answered by `faction_holding` (the pre-IN-12 reading) reproduces both old values
# and both old `BASE_EVENTS` exactly. `aperture 1 0` realm acts 603 -> 613; `survey` att 30 -> 29, ex
# 4 -> 6, ref 26 -> 23; `forge` att 28 -> 25, ex 3 -> 7, ref 25 -> 18 (read, not asserted, v9 §0.5).
# RE-PINNED at v9 IN-45 `carry` (B-K), A BEHAVIOUR MOVE DECLARED: `carry` gains an effect
# (`_eff_carry`) and enters `resolvable_verbs()`, so it is offered and the chooser's sets change. The
# build hash is equal; one and two seasons move. Was da764853... / 0ae0dc8b... (one, two seasons).
# CONTROL, run: the same tree with `carry`'s effect withheld (`EFFECTS` entry deleted) reproduces both
# old values and both old `BASE_EVENTS` exactly, so the shared `_declared_stages`/`_docket_item`
# factoring moved nothing. `aperture 1 0` realm acts 613 -> 615; `carry` offered 0 -> 83, att 0 -> 15,
# ex 0, ref 15 (every attempt on a referent that is not a petition; read, not asserted, v9 §0.5).
# RE-PINNED at v9 IN-45 `migrate` (B-K, on 4cee0de5), A BEHAVIOUR MOVE DECLARED: `migrate` declares
# `referent_class: Rung` and forms only on a place `world_q.places_named` stamps (H-168 limit 1), so
# the chooser's sets change. The build hash is equal; one and two seasons move. Was b1d8ab94... /
# ca8a89d6... (one, two seasons). CONTROL, run: the same tree with `migrate`'s `referent_class` blanked
# in `VERB_TABLE` (the stamp and `_derive_operand`'s document gate left in) reproduces both old values
# and both old `BASE_EVENTS` exactly, so the stamp and the gate move nothing on their own. `aperture 1 0`
# realm acts 615 -> 612; `migrate` formed 83 -> 71, att 31 -> 31, ex 0 -> 1, ref 31 -> 30, every
# refusal now `_eff_migrate`'s capacity decline (read, not asserted, v9 §0.5).
# RE-PINNED at v9 IN-49 `requisition` (B-K, on ccf16bc3), A BEHAVIOUR MOVE DECLARED: `requisition` declares
# `referent_class: Rung` and forms only on a `Rung`-classed referent (`world_q.larders_in_purview`'s
# stocked larders in purview, and `places_named`' places, the class being shared), so the chooser's
# sets change. The build hash is equal; one and two seasons move. Was bedb32d5... / 547d3e62... (one,
# two seasons). CONTROL, run: the same tree with `requisition`'s `referent_class` blanked in `VERB_TABLE` and
# `larders_in_purview` stamping nothing (`_derive_operand`'s widened claim gate and
# `RUNG_REMIT_ACTS` left in) reproduces both old values and both old `BASE_EVENTS` exactly.
# `aperture 1 0` realm acts 612 -> 612; `requisition` formed 16 -> 11, att 3 -> 0, ex 0, ref 3 -> 0 (read,
# not asserted, v9 §0.5); `larders_in_purview` returned `()` in all 766 calls over two realm seasons.
# RE-PINNED at v9 SC-01 step 12 `speak` (B-N, on ffd753f6), A BEHAVIOUR MOVE DECLARED: `speak` is a typed
# contested cell (`existence` of `subject`, kind `DocketItem`; `contests: "a matter"`), so a `speak` on
# a matter no docket names is refused `speech.unheard` and one on a docketed matter is drawn through
# `sigma_leverage`. The build hash is equal; one and two seasons move. Was 3ff10d3c... / 15598353...
# (one, two seasons). CONTROL, run: the same tree with `verb_table.yaml` and `rosters.yaml` at
# ffd753f6 (the old `speak` row, no `a matter` prize row) reproduces both old values and both old
# `BASE_EVENTS` exactly. Over the two seasons `speech.made` 30 -> 0, `speech.unheard` 0 -> 22, one
# `matter.turned` (a docketed `speak` that executed); `aperture 1 0` realm acts 612 -> 608, `speak`
# formed 83 -> 80, att 12 -> 1, ex 12 -> 1 -- its refusals are not counted as attempts there (a
# contested refusal never enters `driver.resolved`) (read, not asserted, v9 §0.5).
# RE-PINNED at v9 SC-03b `determine` contested (B-O), A BEHAVIOUR MOVE DECLARED: `determine` rolls through
# the `social_contest` provider (`contests: "a proposition"`) and writes `Tenure.degree` on the edge it
# opens. The build hash and the ONE-season hash are equal; the TWO-season hash moves, because the realm's
# one executed `determine` (season 2) now draws `Failure` -- `matter.undetermined`, nothing opens, the
# matter stays docketed -- where it used to open the disposal. Was f6972f5b... (two seasons), 23288 events,
# 00bd3227... (digest). CONTROL, run: the same tree with `determine`'s row planted back to its pre-SC-03b
# shape (flat `writes:`/`emits:`, no `contests:`, the two-kind refusals; `(Tenure, degree)`'s `unproduced:`
# restored for the load) reproduces the old hash, event count and digest exactly, and over the two seasons
# `matter.determined` 1 -> 0, `matter.undetermined` 0 -> 1 (read, not asserted, v9 §0.5). No Tenure carries
# a degree in the realm's two seasons (the one draw was `Failure`).
# RE-PINNED at v9 FI-01 (B-O, on bc860c6a, 2026-10-17), TWO BEHAVIOUR MOVES DECLARED: (1) `research`,
# `examine` and `surveil` are GRADED through their `graded_inquiries` route (the `social_contest` provider
# and module entry, no prize), so a Failure draw emits `finding.none` carrying a degree; (2) THE SKIP ARM
# (`undeposited_kinds`, RS-21 item 1): WITNESS deposits nothing for a `finding.none`. The build hash is
# equal; one and two seasons move. Was 27717c62... / c8561121... (one, two seasons). ARM, run: the same
# tree with the skip arm off (`loop/witness.py`'s `UNDEPOSITED_KINDS` emptied, grading on) reads
# e642d1e8... / 43c45874..., 7086 / 23298 events, and holds 251 `finding.none` claims after two seasons;
# with both on, 0. Over the two seasons with both on: 32 `finding.none` at `Failure`, 6 `finding.made` at
# `Partial`, 3 at `Success` (read, not asserted, v9 §0.5). CONTROL: the base commit reproduces the old
# values (this file green there before the change).
# RE-PINNED at v9 SC-02 `22b` steps 24 + 25 (B-P, on 2c8cdcec), A DATA MOVE DECLARED, the event sequence
# UNMOVED: `forge` now writes `Record.forgery_quality` (the shipped `default_forgery_quality` 1, `H-210`),
# so each forged sheet's digest moves -- `record.forged` 7 (one season) / 13 (two). The build hash is
# equal; one and two seasons move. Was 508ac85a... / 89bc9c0a... (one, two seasons). CONTROL, run: the
# same tree at `default_forgery_quality` 0 reproduces both old values and both `BASE_EVENTS` exactly; at
# `pursuit_shift` 0 (step 24's control) it reads the new values unchanged -- `determine` reaches its
# contest 0 times in the realm's two seasons (`determine.refused` 1, no `matter.determined`/
# `.undetermined`), so step 24 moves no realm hash (read, not asserted, v9 §0.5).
# RE-PINNED at v9 IN-12 step 7 `covenant`, A BEHAVIOUR MOVE DECLARED: the new row is `remit:issue`-eligible,
# so the realm's `issue`-granted seat holders FORM it (its cell binds `to` beside `subject`, the known-person
# fan) and the chooser ATTEMPTS it -- every attempt refused (`covenant.refused`: 8 in season 1, 12 by season
# 2; none executed), so the act mix moves. The build hash is equal; one and two seasons move. Was
# e5611ae0... / 6cee9b66... (one, two seasons). ARMS, run on this tree: `covenant` withheld from every
# `opening_set` reproduces the old hashes and event counts exactly (6111 / 18920); `terms_sourced` emptied
# (the `commit` route, `decision/options.py`) moves nothing -- no realm person holds a writ naming a Proposition.
# RE-PINNED at v9 IN-12 step 9 (`argue`, `sabotage`, `tend`, `train`), A BEHAVIOUR MOVE DECLARED: four new `own`
# rows the realm's persons FORM on their questions' referents and the chooser ATTEMPTS -- every attempt refused
# by two seasons (`sabotage.refused` 35: no realm referent is a Site; `tend.refused` 35: a non-person referent or
# a whole body; `train.refused` 41: a non-person referent, or a subject holding no vocation -- nobody in the
# realm holds a `capability`; `argument.refused` 5: no subject is a Proposition; plus one `sabotage`
# `act.ineligible`; none executed), so the act mix moves. The build hash is equal; one and two seasons move.
# Was b3e7784f... / da8e0167... (one, two seasons). ARM, run on this tree: the four withheld from every
# `opening_set` reproduces the old hashes and event counts exactly (6178 / 17855).
# RE-PINNED at v9 IN-12 step 10 (`conceal`), A BEHAVIOUR MOVE DECLARED: a new `own` row with no precondition the
# realm's persons FORM on their questions' referents and the chooser ATTEMPTS, and it EXECUTES (`cover.assumed`
# 19 by two seasons, 19 covers minted); a covered person's later acts anchor on the alias
# (`state/attribution.py::anchor_of`), which moves what the deposits about them are about. The build hash is
# equal; one and two seasons move. Was e28a0d36... / b7367802... (one, two seasons). ARM, run on this tree:
# `conceal` withheld from every `opening_set` reproduces the old hashes and event counts and digests exactly
# (6321 / 17559) -- with no cover held, the `anchor_of` cover read moves nothing.
# RE-PINNED at v9 IN-12 step 13 (`forgive`), A BEHAVIOUR MOVE DECLARED: a new `own` row with no precondition,
# formed only on a referent the person holds a negative stance row against (`rosters.yaml:
# own_stance_declines`). The realm fights no field (H-149/H-175), so every row it can end is a SEEDED one
# (`stance_from_loyalty`): formed 24 times by two seasons, attempted once, executed once (`stance.moved`,
# `p_npc_013` forgiving `p_npc_003`), refused 0; field-planted forgivenesses 0. The build hash is equal; one and
# two seasons move. Was 38cc3da0... / e1fbb610... (one, two seasons). ARM, run on this tree: `forgive` withheld
# from every `opening_set` reproduces the old hashes and event counts and digests exactly (6642 / 19553).
# RE-PINNED at B-Q's BATCH-CLOSE (Phase 1 findings, reproduced red first), A DATA MOVE DECLARED: a covered
# actor's deposit names the alias and not himself (`epistemic.claim_subjects`: three covered `travel.moved`
# in the realm's two seasons), `world_q.event_place` places an act-caused Event by its actor, and a covered
# mover's `travel.ended` chains to his move (`loop/matter.py`). Was ed761c59... / ee8e5500... (one, two
# seasons); the build hash and the season-1 event sequence are unmoved.
# RE-PINNED at v9 IN-12 step 5 (`arrest`, `pardon`), A BEHAVIOUR MOVE DECLARED: `pardon` is a new
# `remit:determine` row the realm's bench-holders FORM on their questions' referents and the chooser ATTEMPTS
# -- every attempt refused (`pardon.refused` 2 in season one, 5 by two seasons: no realm person holds a live
# restraint on the pardoner's seat), so the act mix moves. `arrest` forms 0 times (the realm's two warrants,
# both `p_npc_040`'s, name a Record, and their holder's seat grants no `dispatch`), so it moves nothing; IN-70
# moved nothing. The build hash is equal; one and two seasons move. Was 8bfd47a9... / 8abd76f3... (one, two
# seasons). ARMS, run on this tree: `arrest` and `pardon` withheld from every `opening_set` (`Fixtures
# withheld_verbs`) reproduces the old hashes, event counts and digests exactly (6633 / 19535), and so does
# `pardon` ALONE withheld -- the mover is `pardon`'s formation and refusals, `arrest` none.
# RE-PINNED at v9 IN-12 step 11 (`raze`), A BEHAVIOUR MOVE DECLARED: `raze` is a new `remit:dispatch` row on
# `march`'s cell (`existence` of a Rung) that the realm's dispatch-holders FORM on their questions' Rung
# referents and the chooser ATTEMPTS -- every attempt refused (`raze.refused` 10 in season one, 28 by two
# seasons; `rung.razed` 0: no realm `march` reaches a foreign settlement, H-149/H-175, so no seat's faction
# occupies one), so the act mix moves. The build hash is equal; one and two seasons move. Was c9e46891... /
# 47eda125... (one, two seasons). CONTROL, run on this tree: `raze` withheld from every `opening_set`
# (`Fixtures withheld_verbs`) reproduces the old hashes, event counts and digests exactly (6635 / 18681) --
# the mover is `raze`'s formation and refusals.
# RE-PINNED at v9 IN-12 `give` + Rung (cession), A BEHAVIOUR MOVE DECLARED: `give`'s typed cell dropped its
# `existence` conjunct (kind `Record`; the grammar has no disjunction) and `give` joined
# `rosters.yaml: own_hold_declines`, so a person forms a gift only of a referent he HOLDS. In the realm almost
# no question's referent is a thing its asker holds (H-229 counts one held-rung question), so `give` forms 0 times (33 formed, `give.refused` 7 in
# season one and 18 by two seasons before; `record.given` and `rung.ceded` 0 in both), and the act mix moves.
# The build hash is equal; one and two seasons move. Was 00f9b52c... / 195b1ac6... (one, two seasons).
# CONTROL, run on BOTH trees (this one and its base, 68eaaa41): `give` withheld from every `opening_set`
# (`Fixtures withheld_verbs`) gives 8cb4f4e2... / cf3625f5... (6603 / 19990) on each, equal to this pin -- the
# mover is `give`'s formation alone, and nothing else in the change reaches the realm.
# RE-PINNED at v9 PC-06 K-3 (`H-85`), A SCHEMA AND BEHAVIOUR MOVE DECLARED. (1) THE BUILD HASH MOVES: `Person`
# gains `thread_sensitivity` (`None` unless authored), so every person's `repr` -- folded into `content_hash`
# -- changes, and ten cast persons carry an authored value (four at or above the gate). (2) ONE AND TWO
# SEASONS MOVE: `thread_read` is typed and forms for the four persons whose own sensitivity passes it; one
# reading executes in the realm's first season (`aperture 1 0`: formed 4, offered 4, attempted 1, executed 1),
# so the act mix moves. Was d3edd90a... / 8cb4f4e2... / cf3625f5... (build, one, two seasons). CONTROL, run on
# this tree: `thread_read` withheld from every `opening_set` (`Fixtures withheld_verbs`), and separately the
# gate swept out of reach (`thread_sensitivity_gate` 999), each reproduces the OLD event counts and digests
# exactly (6603 / 19990, `BASE_EVENTS` as it was) under the new build hash -- the event-level mover is
# `thread_read`'s formation alone, and the hash-only mover is the field.
# RE-PINNED at v9 IN-59 (a) (RS-26, the attack half of the access gate), A BEHAVIOUR MOVE DECLARED: `fight`,
# `challenge` and `accept` gain a `relation: with` conjunct on `subject`, so the fold refuses a duel verb whose
# subject is not where the actor is, and the act mix moves (`aperture 1 0`, realm, seed 0: `fight` att/ex/ref
# 4/4/0 -> 1/1/0, `accept` 11/11/0 -> 1/1/0, `challenge` 13/4/9 -> 17/1/16). The build hash is equal (the
# build reads no verb row; `guards=True` and `foreign=True` equal too); one and two seasons move. Was
# 628830a8... / 74ce9a1e... (one, two seasons). The `give`-withheld arm still reads the one-season pin.
# RE-RECORDED at v9 IN-59 (b) (RS-26, the audience half), A HASH-ONLY MOVE STATED: `move` and `migrate` gain
# a `relation: audience` conjunct on `to`, and at the shipped default build (`guards` OFF) every `guard_weight`
# is 0 (MEASURED at the B-Y close, seed 0: no rung of `build_realm(0)` reads above 0; a live sworn `oblige`
# standing with its principal would close a rung wherever one arises), so every audience reads admitted in
# these runs and the act mix is EQUAL -- `BASE_EVENTS` reproduce exactly (7018 /
# e3d6e385..., 21710 / 2da1c8f4...). What moves the hash is the conjunct's own `audience:<actor>`
# Observation on each `move`/`migrate` Event's `observed` (44 Events in season one). CONTROL, run on this
# tree: those Observations stripped from the one-season log re-read 57fae32f... exactly. The build,
# `guards=True` and `foreign=True` hashes are equal (8e4032a2 / c98563e0 / 90b531a1). Was 57fae32f... /
# 3c4e03e6... (one, two seasons).
# RE-PINNED at GO-07 (B10-03b), A DIGEST-FORMAT MOVE DECLARED, NO GAME MOVE: `content_hash` folds the
# canonical encoding instead of `repr()`. Was 8e4032a2... / b2464a6c... / 5301d6b6... (build, one, two
# seasons); `BASE_EVENTS` unmoved, and the old `repr` digest over the same worlds still read those three
# when measured at GO-07. `test_go07_canonical_digest.py`'s control re-reads the build (seed 0) and one
# season (seeds 0-2); the two-season reading was taken once and is not re-run.
# RE-PINNED at v10 REM-22 (B10-05), A BEHAVIOUR MOVE DECLARED: `restore`, `work` and `examine` declare
# `referent_class: Site`, so they form only on a Site the question the person answers carries, and the
# realm's questions carry none (`aperture 1 s`, realm: `restore` att 6/21/15 -> 0/0/0, `work` 35/37/38 -> 0/0/0,
# `examine` 29/34/22 -> 0/0/0 at seeds 0/1/2). The build hash is equal (the build reads no verb row); one and
# two seasons move, as does every other seeded realm reading. Was 947c190b... / 52a106bc... (one, two seasons).
# CONTROL, run: with the three columns removed (the REM-21 tree) the old pair reads again.
# RE-PINNED at v10 REM-23 (B10-05), A BEHAVIOUR MOVE DECLARED: `commit` declares `referent_class: Proposition`, so
# it forms only on a Proposition the question the person answers names, and the realm's questions seldom do
# (`aperture 1 s`, realm: `commit` formed for 83 of 83 persons -> 6 / 2 / 1, attempted 38/33/34 -> 1/1/1,
# `exists:Proposition=0` 36/32/33 -> 0 at seeds 0/1/2; 61 -> 1 commit acts over two seasons at seed 0). The build
# hash is equal (the build reads no verb row); one and two seasons move. Was 3c627dea... / 39fc1d62... (one, two
# seasons). CONTROL, run: this same script on the REM-22 tree (`e66a22ec`) reads the old pair again.
# RE-PINNED at v10 REM-24 (B10-05), A BEHAVIOUR MOVE DECLARED: `petition` declares `referent_class: Person`, so it
# forms only on a person the question the person answers names (`aperture 1 s`, realm: `petition` formed for
# 82/81/82 of 83 persons -> 40/39/43, attempted 19/17/20 -> 10/4/8, refused 9/13/12 -> 0, each of those refusals
# on `exists:Person=0`; executed 10/4/8 -> 10/4/8). The build hash is equal; one and two seasons move.
# Was 290655d8... / 7084faf2... (one, two seasons). CONTROL, run: this same script on the REM-23 tree
# (`409c467b`) reads the old pair again.
# RE-PINNED at v10 REM-25 (B10-05), A BEHAVIOUR MOVE DECLARED: `carry`, `found` and `build` declare
# `referent_class: Record`, and the `Record` term widens to the Records a person holds that those rows ask him to
# hold (`records_held_for_holding_rows`), so they form only on a held petition or works (`aperture 1 s`, realm:
# `carry` attempted 15/18/12 -> 2/0/1 with 0/0/0 -> 2/0/1 executed, `found` 11/14/21 -> 0/0/0, `build` 12/13/12 ->
# 0/1/1; `comply` 0/0/0 -> 2/2/1 attempted on a held petition, refused on `exists:dispensation=0`; wrong-kind
# refusals over the four rows 38/45/45 -> 2/3/2). The build hash is equal (the build reads no verb row); one and two
# seasons move. Was cd0ea7bc... / c010a137... (one, two seasons). CONTROL, run: this file on the REM-24 tree
# (`f2381695`) is green against the old pair; and in-process on the REM-25 tree the three columns alone (the holding
# term stubbed to `()`) read d7c03c2d... at one season and the term alone (the three columns blanked) 8f6e7aac...,
# so each unit moves the hash by itself.
BASE_HASHES = {0: "9ff5390939742b7bbb3af0fa2551e958",
               1: "da1ce5ebe72129fb5fbc829afdd9b49c",
               2: "0f791e815897aae99594d888ffe29cf9"}

# `build_realm(0)` driven by `POP.run`, seed 0: the whole log's event count and the sha256 of its
# ordered `kind|id` lines after one season and after two. FIRST RECORDED on the pre-IN-34 base
# (d47077d5) as a one-time proof that the schema re-pin of `BASE_HASHES` moved nothing at the event
# level; it is NO LONGER that base's values. Re-recorded with `BASE_HASHES` at v9 IN-53 (7526 -> 7527,
# 21508 -> 21735: `confer`'s always-refused attempts stopped), so the values below are IN-53's and this is a change detector on
# the seasons-1-2 event sequence, not a pre-IN-34 control. Unmoved by the batch B-I close's fixes
# (fingerprint, conferee, founding, occasion). Re-recorded together with `BASE_HASHES`, never alone.
# RE-RECORDED at v9 IN-57 (B-W) with `BASE_HASHES`: the attention key re-orders each person's questions, so
# fewer and different acts follow (7527 -> 6624, 21735 -> 17285); IN-58 moved nothing.
# RE-RECORDED at v9 IN-64 with `BASE_HASHES`: full pursuit vectors re-rank every cast person's
# candidates (6624 -> 7309, 17285 -> 20220).
# RE-RECORDED at v9 IN-71 with `BASE_HASHES`: the doctrine coupling re-ranks the devout and the lukewarm
# apart (7309 -> 7186, 20220 -> 19797).
# RE-PINNED at v9 FA-04 (B-X), A DATA MOVE DECLARED: the Grand Master's oath is one seeded `oblige` Tenure
# (`off_king`'s `obligees: ["NPC-070"]`), so the build hash moves and the log gains its one build-time event.
# Was 472050b8... / cc650fcf... / 8f4d2088... (build, one, two seasons); events 7186 -> 7187, 19797 -> 19798.
# RE-RECORDED at v9 FA-05 with `BASE_HASHES` (7187 -> 6542, 19798 -> 18583).
# RE-RECORDED at v9 FA-06 with `BASE_HASHES` (6542 -> 7094, 18583 -> 19454).
# RE-RECORDED at v9 IN-10 with `BASE_HASHES` (7094 -> 7056, 19454 -> 20148).
# RE-RECORDED at v9 IN-45 `forge` with `BASE_HASHES` (7056 -> 7338, 20148 -> 21313).
# RE-RECORDED at v9 IN-12 `survey` + Rung with `BASE_HASHES` (7338 -> 7391, 21313 -> 22130).
# RE-RECORDED at v9 IN-45 `carry` with `BASE_HASHES` (7391 -> 7186, 22130 -> 21338).
# RE-RECORDED at v9 IN-45 `migrate` with `BASE_HASHES` (7186 -> 7160, 21338 -> 23584).
# RE-RECORDED at v9 IN-49 `levy` with `BASE_HASHES` (7160 -> 7157, 23584 -> 23361).
# RE-RECORDED at v9 SC-01 step 12 `speak` with `BASE_HASHES` (7157 -> 7060, 23361 -> 23220).
# RE-RECORDED at the merge of main's `levy` -> `requisition` rename (#482, #485) into batch B-N (season 2 only, with
# `BASE_HASHES[2]`): act ids and draw streams hash the verb name, so the same seed walks another trajectory from season 2.
# Main alone read 18ffd214... / 23241 events; B-N alone read ef1c9ad8... / 23220; the merged tree reads f6972f5b... / 23288.
# Season 0 and season 1 are unchanged by the merge (d3edd90a / 27717c62, 7060 events).
# RE-RECORDED at v9 SC-03b with `BASE_HASHES` (season 2 only: 23288 -> 23215; season 1 unchanged, 7060).
# RE-RECORDED at v9 FI-01 with `BASE_HASHES` (7060 -> 6111, 23215 -> 18920: the skip arm's absent
# `claim.deposited` Events, and the trajectory the graded inquiries and the missing claims move).
# RE-RECORDED at v9 IN-12 step 7 `covenant` with `BASE_HASHES` (6111 -> 6178, 18920 -> 17855).
# RE-RECORDED at v9 IN-12 step 9 with `BASE_HASHES` (6178 -> 6321, 17855 -> 17559).
# RE-RECORDED at v9 IN-12 step 10 `conceal` with `BASE_HASHES` (6321 -> 6642, 17559 -> 19553).
# RE-RECORDED at v9 IN-12 step 13 `forgive` with `BASE_HASHES` (6642 -> 6633, 19553 -> 19538).
# RE-RECORDED at B-Q's BATCH-CLOSE with `BASE_HASHES` (season 1 events unmoved, 6633; season 2 19538 -> 19535).
# RE-RECORDED at v9 IN-12 step 5 `pardon` with `BASE_HASHES` (6633 -> 6635, 19535 -> 18681).
# RE-RECORDED at v9 IN-12 step 11 `raze` with `BASE_HASHES` (6635 -> 6655, 18681 -> 18608).
# RE-RECORDED at v9 IN-12 `give` + Rung with `BASE_HASHES` (6655 -> 6603, 18608 -> 19990).
# RE-RECORDED at v9 PC-06 K-3 `thread_read` with `BASE_HASHES` (6603 -> 6594, 19990 -> 19221).
# RE-RECORDED at v9 IN-59 (a) with `BASE_HASHES` (6594 -> 7018, 19221 -> 21710).
# RE-RECORDED at v10 REM-22 with `BASE_HASHES` (7018 -> 7345, 21710 -> 21490).
# RE-RECORDED at v10 REM-23 with `BASE_HASHES` (7345 -> 6647, 21490 -> 21312).
# RE-RECORDED at v10 REM-24 with `BASE_HASHES` (6647 -> 6396, 21312 -> 21342).
# RE-RECORDED at v10 REM-25 with `BASE_HASHES` (6396 -> 6348, 21342 -> 22009).
BASE_EVENTS = {1: (6348, "e4c6a90cebbeb0f53b64e8e823622add79b43f59239c563c0c53aa6cd8c35ec9"),
               2: (22009, "b4b399316e52ed2502425fbc56892796079a84546d37d1cc6ec0cc2efafdd2bf")}


def _digest(w) -> tuple:
    seq = [f"{e.kind}|{e.id}" for e in w.log]
    return len(seq), hashlib.sha256("\n".join(seq).encode()).hexdigest()

# H-26's declared sweep, as tables: a year of four seasons each time.
YEAR = 4
DROUGHT = ((0.5,),) * YEAR                    # every season draws the 0.5 point
UNIT = ((1.0,),) * YEAR                        # the draw on, degenerate at the control value
SPREAD = ((0.5, 1.0, 2.0),) * YEAR            # the swept points, equally likely


def _matter(w):
    """MATTER alone, through the real barrier and a real MATTER token (the `24f` tests' helper)."""
    d = SeasonDriver(w)
    w.step = Step.MATTER
    return d.matter(mint_token(w, WriteClass.MATTER), [])


# --- a world where the control feeds everyone and a drought does not -----------------------------
# Test data, not a claim about Valoria's economy: one harbour at full condition (40 grain, 30 salt a
# season at factor 1) under a cohort that eats 30 grain and 15 salt a season at the shipped
# `subsistence_weight`, opening with exactly one season's want. Control: surplus every season.
# Drought (x0.5): the yield falls to 20 grain, so the second draw runs the larder dry.
TOWN, COHORT = "set_town", "p_town_folk"
# [JUSTIFIED: a test-fixture size, not a game value -- 15 mouths want 30 grain and 15 salt a season at the shipped weights, sized so a 0.5 yield cannot cover them and a 1.0 yield can]
COHORT_WEIGHT = 15
# [JUSTIFIED: a test-fixture stock, not a game value -- exactly one season's want, so the first draw empties nothing early]
OPENING = {"grain": 30, "salt": 15}


def _town(table, seed: int = 0) -> World:
    w = World(seed, DEFAULT.sweep("season_factor_draw", table))
    scale = w.fixtures.get("condition_scale")
    for rid, kind, stores in (("r_realm", "realm", None), ("terr_town", "territory", None),
                              (TOWN, "settlement", dict(OPENING))):
        w.rungs[rid] = Rung(rid, kind, stores=stores)
    w.add_tenure(Tenure("t_in_0", "terr_town", "r_realm", "contain", 0))
    w.add_tenure(Tenure("t_in_1", TOWN, "terr_town", "contain", 0))
    w.sites["s_town_harbour"] = Site("s_town_harbour", TOWN, "harbour", condition=scale)
    w.persons[COHORT] = Person(COHORT, "the town folk", weight=COHORT_WEIGHT)
    w.rungs[COHORT] = Rung(COHORT, "person")
    w.add_tenure(Tenure("t_folk_in", COHORT, TOWN, "contain", 0))
    w.add_tenure(Tenure("t_folk_home", COHORT, TOWN, world_q.RESIDE_KIND, 0))
    return w


def _seasons(w, n: int):
    """`n` MATTER barriers with the clock advanced between; returns (stores after each, the shortfall
    observations each emitted)."""
    stores, shorts = [], []
    for _ in range(n):
        evs = _matter(w)
        w.tick += 1
        stores.append(dict(w.rungs[TOWN].stores))
        shorts.append([(o.subject, o.predicate, o.value) for e in evs for o in e.observed
                       if str(o.predicate).partition(":")[0] == SHORTFALL_PREDICATE])
    return stores, shorts


def test_in21_control_draw_off_and_draw_at_one_reproduce_the_base_hashes():
    h, events = {}, {}
    w = POP.build_realm(0)
    h[0] = w.content_hash()
    assert w.fixtures.get("age_step") == 0 and w.fixtures.get("illness_rate") == 0
    for n in (1, 2):
        POP.run(seasons=1, seed=0, w=w)   # continuing one world reads the fresh two-season hash
        h[n] = w.content_hash()
        events[n] = _digest(w)
    assert w.fixtures.get("season_factor_draw") == (), "the shipped default is not the control arm"
    assert h == BASE_HASHES, f"draw off moved a hash: {h}"
    assert events[1][0] >= 5000 and events[2][0] >= 15000, f"the seasons emitted too little: {events}"
    assert events == BASE_EVENTS, f"the bodies clock at its control moved the event sequence: {events}"


def test_the_give_withheld_arm_reproduces_the_one_season_pin():
    """THE `give` + Rung RE-PIN'S CONTROL, ENCODED (it stood as prose above): `give` added to the shipped
    `Fixtures withheld_verbs` reads the CURRENT one-season pin exactly -- hash, event count and digest --
    so at the shipped arm the realm forms no `give` in season one. That `give` formation is the re-pin's
    ONLY mover is the commit's measurement, not this test's: it needs the base tree (the pre-change pin,
    `195b1ac6`/`47eda125`, is no longer producible on one tree). If `give` forms again in the realm, `BASE_HASHES[1]` moves with it and
    this arm stops matching: the re-pin would then need a new control, not a re-recorded one."""
    w = POP.build_realm(0)
    shipped = tuple(w.fixtures.get("withheld_verbs"))
    assert "give" not in shipped, "fixture: `give` is already withheld at the shipped arm"
    w.fixtures = w.fixtures.sweep("withheld_verbs", shipped + ("give",))
    POP.run(seasons=1, seed=0, w=w)
    assert w.content_hash() == BASE_HASHES[1], w.content_hash()
    assert _digest(w) == BASE_EVENTS[1], _digest(w)


#: The one-season event sequence BEFORE v9 PC-06 K-3 (`BASE_EVENTS[1]` at `26884a93`), kept as the K-3
#: re-pin's control: the event-level mover must be `thread_read`'s formation and nothing else.
#: RE-RECORDED at v9 IN-59 (a), STATED: the duel verbs' `with` conjunct moves the `thread_read`-withheld arm
#: too (6603 / 958f4283... -> 7028 / 4f9b8312...), so the K-3-time sequence is no longer producible on one
#: tree. The value below is that arm on the IN-59 tree, `PYTHONHASHSEED=0`; from here it is a change detector
#: that still shows `thread_read` moves the season (it differs from `BASE_EVENTS[1]`), as `BASE_EVENTS` became.
#: RE-RECORDED at v10 REM-22 with `BASE_HASHES`: 7028 / 4f9b8312... -> 7354 / eb995a13... (the three Site rows).
#: RE-RECORDED at v10 REM-23 with `BASE_HASHES`: 7354 / eb995a13... -> 6652 / 98bef289... (`commit` declares `Proposition`).
#: RE-RECORDED at v10 REM-24 with `BASE_HASHES`: 6652 / 98bef289... -> 6401 / 71a40c5a... (`petition` declares `Person`).
#: RE-RECORDED at v10 REM-25 with `BASE_HASHES`: 6401 / 71a40c5a... -> 6353 / 09edad05... (`carry`, `found` and `build`
#: declare `Record`).
THREAD_READ_WITHHELD_EVENTS_1 = (6353, "09edad057844f642fc6aed2fd442c305fa36662f0bb877c9e66b372a104f2b4c")


def test_the_thread_read_withheld_arm_is_pinned_and_differs_from_the_shipped_season():
    """THE THREAD-READ-WITHHELD ARM, A CHANGE DETECTOR: `thread_read` added to the shipped `Fixtures
    withheld_verbs` reads `THREAD_READ_WITHHELD_EVENTS_1` -- the arm's own event count and digest on the IN-59 tree, no
    longer the PRE-K-3 sequence it was recorded as at K-3 (IN-59 (a) moved that arm too; see the
    constant's comment) -- and that differs from the shipped season's `BASE_EVENTS[1]`, so
    `thread_read`'s formation still moves what a season does. The K-3-time control (the arm equalling the
    pre-K-3 sequence) can no longer be read on one tree."""
    w = POP.build_realm(0)
    shipped = tuple(w.fixtures.get("withheld_verbs"))
    assert "thread_read" not in shipped, "fixture: `thread_read` is already withheld at the shipped arm"
    w.fixtures = w.fixtures.sweep("withheld_verbs", shipped + ("thread_read",))
    POP.run(seasons=1, seed=0, w=w)
    assert _digest(w) == THREAD_READ_WITHHELD_EVENTS_1, _digest(w)
    assert THREAD_READ_WITHHELD_EVENTS_1 != BASE_EVENTS[1], "the arm equals the shipped pin -- withholding `thread_read` moved nothing"


def test_in21_a_table_of_ones_reads_the_same_as_no_table():
    """The draw ON but degenerate at 1.0: base * 1.0 is the bare constant. Compared on the one-town
    world (`content_hash` folds state and the log, not fixtures), over two seasons, exactly."""
    off, unit = _town(()), _town(UNIT)
    assert _seasons(off, 2) == _seasons(unit, 2)
    assert off.content_hash() == unit.content_hash(), "a table of 1.0 moved the hash"


def test_in21_drought_leaves_stores_below_control_and_a_drained_larder_reports_shortfall():
    control, c_short = _seasons(_town(()), 2)
    drought, d_short = _seasons(_town(DROUGHT), 2)
    # Non-vacuity: the control world actually produced and fed (stores moved, nothing short), so a
    # "below control" reading is a difference and not two empty larders.
    assert control[0] == {"grain": 40, "salt": 30}, f"control world is not the one sized: {control[0]}"
    assert drought[0] == {"grain": 20, "salt": 15}, f"drought did not halve the yield: {drought[0]}"
    checked = 0
    for kind in ("grain", "salt"):
        for season in (0, 1):
            assert drought[season][kind] < control[season][kind], (
                f"season {season}: drought {kind} {drought[season][kind]} is not below control "
                f"{control[season][kind]}")
            checked += 1
    assert checked == 4
    assert c_short == [[], []], f"the control arm reported a shortfall: {c_short}"
    # The second draw wants 30 grain of the 20 the drought left: the larder drains, one unit kind short.
    assert d_short[0] == []
    assert d_short[1] == [(TOWN, f"{SHORTFALL_PREDICATE}:grain", 10)], d_short[1]


def test_in21_same_seed_twice_one_hash_and_the_draw_moves_it_off_control():
    a, b = _town(SPREAD, seed=7), _town(SPREAD, seed=7)
    _seasons(a, 6)
    _seasons(b, 6)
    assert a.content_hash() == b.content_hash(), "the same seed twice gave two hashes"
    off = _town((), seed=7)
    _seasons(off, 6)
    assert a.content_hash() != off.content_hash(), "the draw on moved nothing; it is not wired"


def test_in21_the_factor_is_keyed_on_the_seed_and_the_season_of_the_year_is_read_off_tick():
    def factors(seed):
        w = _town(SPREAD, seed=seed)
        out = []
        for t in range(24):
            w.tick = t
            out.append(world_q.season_factor_of(w))
        return out

    seq = {s: factors(s) for s in range(4)}
    assert all(set(f) <= {0.5, 1.0, 2.0} for f in seq.values())
    # FULL SUPPORT, not only a subset: a modulus that never reaches the last outcome (`% (n - 1)`)
    # draws only members of the set and would pass the line above.
    assert set().union(*(set(f) for f in seq.values())) == {0.5, 1.0, 2.0}
    assert len({tuple(f) for f in seq.values()}) > 1, "four seeds drew one sequence; the key ignores the seed"
    assert len(set(seq[0])) > 1, "one seed drew one value for 24 seasons; the key ignores the tick"
    assert factors(0) == seq[0], "the same seed read a different sequence the second time"
    # The season of the year IS tick % len(table): with a distinct single outcome per season the
    # factor is the table's entry at that index, for every tick, and the year wraps.
    year = ((0.5,), (1.0,), (2.0,), (1.5,))
    w = _town(year)
    seen = 0
    for t in range(2 * len(year) + 1):
        w.tick = t
        assert world_q.season_of_year(w) == t % len(year)
        assert world_q.season_factor_of(w) == year[t % len(year)][0]
        seen += 1
    assert seen == 9
    # And no table, no year: the control returns the bare constant and no season.
    w = _town(())
    assert world_q.season_of_year(w) is None
    assert world_q.season_factor_of(w) == DEFAULT.get("season_factor")
