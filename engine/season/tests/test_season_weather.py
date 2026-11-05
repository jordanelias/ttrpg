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
# RE-PINNED at v10 CP-T05-04 (B10-05), A BEHAVIOUR MOVE DECLARED: `argue` declares `referent_class: Proposition` and
# `open_case` declares `Person` (`aperture 1 s`, realm: `argue` formed for 37/35/39 of 83 persons -> 0/0/0, attempted
# 8/10/5 -> 0, every one refused on `exists:Proposition=0`; `open_case` formed for 8/8/8 -> 6/6/8, executed 4/2/1 ->
# 2/1/1), and `world_q.docket_question` asks the witness of a docketing about the matter docketed (asked in 41/8/3
# calls, delivered as the question he answers in 20/1/0, `docket_reach` reading; `speak` and `determine` formed counts
# unmoved). The build hash is equal (the build reads no verb row); one and two seasons move. Was da1ce5eb... /
# 0f791e81... (one, two seasons). CONTROL, run: the same script (this file's `_digest` and `POP.run`, one world
# continued through two seasons) on a detached worktree at the REM-25 tree (`92892b09`) reads the old pair, the old
# `BASE_EVENTS` and the old thread-read arm exactly; and in-process on this tree the columns alone (the docket term stubbed to `None`) read
# 7f36d369... at one season and 8fe360af... at two, the docket question alone (the two columns blanked) 66a48d9a... and
# 2e37c57c..., so each unit moves the hash by itself.
# RE-PINNED at v10 REM-2C (B10-05), A BEHAVIOUR MOVE DECLARED: `research` declares `referent_class: Record` and
# `Record` leaves `rosters.yaml: occasion_only_classes`, so the own-referent term stamps the question's own Records
# (`aperture 1 s`, realm: `research` formed for 83/83/83 persons -> 23/20/25, attempted 69/66/53 -> 5/8/1, refused
# at admission on `exists:Record=0` 67/62/53 -> 0/0/0, att - ref 2/0/0 -> 2/3/1; the five Record rows' wrong-kind
# refusals 68/65/55 -> 6/9/12, the four others' 1/3/2 -> 6/9/12). The build hash is equal (the build reads no verb
# row); one and two seasons move. Was 26bcb37d... / 8d91a374... (one, two seasons). CONTROL, run: the same script
# (this file's `_digest` and `POP.run`, one world continued through two seasons) on a detached worktree at the
# CP-T05-04 tree (`ea6f1dba`) reads the old pair, the old `BASE_EVENTS` and the old thread-read arm exactly; and
# in-process on this tree the column alone (`Record` held back in `occasion_only_classes`) reads 0ee23110... at one
# season and 0553ebbb... at two, the roster release alone (`research`'s class blanked) 325edb92... and 18a38e76...,
# so each unit moves the hash by itself.
# RE-PINNED at v10 REM-52 (B10-05), A BEHAVIOUR MOVE DECLARED: `Fixtures body_step` ships at `10`, `H-125`'s live arm
# (it was the control `0`), so the realm's first MATTER draw, which finds every larder empty, falls each short cohort's
# body by `10` x its unmet units (36 of the 37 cohorts from 1000 to 940 at seed 0; `body.changed` 0 -> 37 Events), and
# the act mix moves (`aperture 1 0`, realm: acts 577 -> 576, `tend` executed 1 -> 2, `utter` attempted 28 -> 29). The
# build hash is equal (the build reads no `body_step`); one and two seasons move. Was 8bec380b... / 174b6547... (one,
# two seasons). CONTROL, run: the same script (this file's `_digest` and `POP.run`, one world continued through two
# seasons) on a detached worktree at the REM-2C tree (`a397fa16`) reads the old pair and the old `BASE_EVENTS`
# exactly; and on the REM-52 tree with `body_step` swept back to `0` in `data/fixtures.py` (a scratch worktree,
# `written=True` left in `loop/matter.py`) it reads the old pair too, while `body_step = 10` alone (`written` left
# as it was) reads the new one-season values at seeds 0 / 1 / 2, so the move is `body_step`'s and `written=True`
# (H-129's `body.changed` read) moves nothing here.
# RE-PINNED at v10 REM-27 (B10-06), A BEHAVIOUR MOVE DECLARED: `march` declares `referent_class: Rung`, so it forms
# only on a Rung the question carries as `Rung` (`places_named`, `larders_in_purview`), and `RUNG_REMIT_ACTS` widens
# by derivation to `{issue, dispatch}` (`aperture 1 s`, realm: `march` attempted 10/15/3 -> 8/24/10, every one still
# refused, `exists:Rung=0` 2/0/0 -> 0; `migrate` attempted 59/144/104 -> 56/139/104; `requisition` formed 16/16/16,
# unmoved; `field.*` 0 -> 0). The build hash is equal (the build reads no verb row); one and two seasons move. Was
# 5d2e5f77... / 05352e22... (one, two seasons). CONTROL, run in process on this tree: `march`'s column blanked in
# the shared `VERB_TABLE` and `RUNG_REMIT_ACTS` narrowed back to `{issue}` reads the old pair, the old `BASE_EVENTS`
# and the old `give`- and `thread_read`-withheld arms exactly.
# RE-PINNED at v10 REM-28 (B10-06), A BEHAVIOUR MOVE DECLARED: `convene` declares `referent_class: Rung`, so it forms only
# on a Rung the question carries as `Rung` (`places_named`, `larders_in_purview`) -- never on a person-rung or a
# Proposition, the 9 of 11 pooled attempts the fold refused -- and `RUNG_REMIT_ACTS` widens by derivation to `{issue,
# dispatch, convene}` (no offer moves: no seat grants `convene` without `issue` or `dispatch`, and `larders_in_purview`
# offers nothing to anyone). `aperture 1 s`, realm: `convene` attempted 3/0/5 -> 4/5/6 and executed 1/0/1 -> 4/5/5 (spine
# 0/0/0 -> 3/0/0), so the dates convened carry a holder and CALENDAR forms their docket slots (events 6482 -> 7193 at one
# season); `migrate` and `requisition` formed counts unmoved. The build hash is equal; one and two seasons move. Was
# ecb47cd0... / 5d7f362d... (one, two seasons). CONTROL, run in process on this tree: `convene`'s column blanked in the
# shared `VERB_TABLE` and `RUNG_REMIT_ACTS` re-derived reads the old pair, the old `BASE_EVENTS` and the old `give`- and
# `thread_read`-withheld arms exactly.
# RE-PINNED at v10 REM-28 `dispatch` (B10-06), A BEHAVIOUR MOVE DECLARED: `dispatch` declares `referent_class: Person`, so
# it forms only on a person the question names and never on a rung, a Record or a Site -- `_req_dispatch`'s 'names no
# person the world holds', 16 of 33 pooled attempts at `aperture 1 s`, all refused -- and no derived set moves
# (`DECLARED_CLASSES` already holds `Person`, `RUNG_REMIT_ACTS` reads `Rung` rows alone). `aperture 1 s`, realm:
# `dispatch` attempted 11 / 8 / 8 -> 2 / 8 / 6, refused 9 / 0 / 2 -> 0, executed 2 / 8 / 6 unmoved; `convene`, `migrate`
# and `requisition` formed counts unmoved. The build hash is equal; one and two seasons move. Was 7d99c0f7... /
# 1196f86b... (one, two seasons). CONTROL, run in process on this tree: `dispatch`'s column blanked in the shared
# `VERB_TABLE` reads the old pair, the old `BASE_EVENTS` and the old `give`- and `thread_read`-withheld arms exactly.
# RE-PINNED AT v10 REM-28 `revoke` (B10-06), TWO SEASONS ONLY: `revoke` declares `referent_class: Office`, so it forms only on a
# seat the question carries as an Office and never on a person, a rung, a Record or a Site (`names no office the world holds`,
# 18 of 18 pooled attempts at `aperture 1 s`, all refused); it executes nothing either way (`_req_revoke` reads `office`, a
# computed act carries `subject`), and no derived set moves. One season is unmoved (no `revoke` was attempted in the seed-0
# realm's first season), so are the build, the `give`- and `thread_read`-withheld arms; the second season moves (`revoke`'s
# attempts and their scenes). Was fe3cc6d3... (two seasons, the dispatch commit). CONTROL, run in process on this
# tree: `revoke`'s column blanked in the shared `VERB_TABLE` reads the old two-season hash and events exactly.
# RE-PINNED at v10 CR-23 (B10-06), A BEHAVIOUR MOVE DECLARED: MATTER's last `stores` write to a rung carries the stock
# report (`stores:<kind>`) when `requisitionable` flips across the barrier (`Fixtures stock_report = crossing`, `H-243`),
# and WITNESS deposits it to the seats over the larder: the realm's 37 settlements cross into stock at the first yield, so
# one season's events grow by the deposits (7196 -> 9270) and `requisition` executes in computed play. The build hash is
# equal (the build runs no MATTER); one and two seasons move. Was 30a95964... / 920da131... (one, two seasons). CONTROL,
# run in process on this tree: `stock_report = off` reads the old pair, the old `BASE_EVENTS`, the old `give`-withheld
# arm and the old `thread_read`-withheld arm exactly.
# RE-PINNED at v10 REM-29 (B10-06), A BEHAVIOUR MOVE DECLARED: `migrate`'s capacity throttle is a `room` conjunct
# (`world_q.has_room`, the one owner), so the fold refuses a full rung AT ADMISSION with the read `(to, room:<actor>,
# False)` on the Event, WITNESS deposits it to the migrant, and he does not re-form that `migrate`: `aperture 1 s`, realm,
# `migrate` attempted 67 / 135 / 88 -> 41 / 80 / 61, executed 3 / 3 / 4 unmoved, and the freed scenes are taken by other
# acts. The build hash is equal; one and two seasons move. Was 1d402d15... / b2276c73... (one, two seasons). CONTROL, run on
# this tree: the `room` conjunct and its refusal key deleted from `migrate`'s row (stem, `has_room` and the effect's call
# kept) reads the old pair, the old `BASE_EVENTS`, the old `give`-withheld arm and the old `thread_read`-withheld arm exactly.
# RE-PINNED at v10 REM-2B (B10-06), A BEHAVIOUR MOVE DECLARED AND A TRAJECTORY MOVE (HR-3): `evade / defy`, `construe` and
# `exchange` are typed and resolvable again (restored from v9 IN-09 / IN-33's checkpoints), so the chooser offers them: `aperture
# 1 0`, realm, `exchange` formed 83, attempted 21, executed 0; `construe` and `evade / defy` form on a held petition or works
# the shared `Record` class stamps and are refused (`exists:dispensation=0`); the freed and taken scenes move the act mix. The
# build hash is equal (the build reads no verb row); one and two seasons move. Was 4cc07cbe... / 333396e9... (one, two
# seasons). CONTROL, run in process on this tree: the three rows put back to their base shape (untyped, unclassed, their
# decline notes, `exchange` writing one pair with no effect) read the old pair and the old `BASE_EVENTS` exactly.
# RE-PINNED at v10 IN-45 (B10-06), A DATA MOVE DECLARED: `venues.yaml: planned_works` authors two works (a `hearth` at Auerheim, a
# `dwelling` at the Royal Court), minted last in `build_realm` through `create_record`'s own effect, so the BUILD hash moves (two
# Records and their masters' `hold` edges), and so do one and two seasons (each works's terms ripen: `term.matured` Events; the
# masters' `found` and `build` form on them and rank at the chooser's tail -- `aperture 4 s`, realm: executed 0 at seeds 0 and 1,
# 1 each at seed 2: the Duke founds at tick 2, the Steward builds at tick 3). Was 9ff53909... / 41ffb48b... / 3afa013b... (build, one, two seasons). CONTROL, run in process on this
# tree: `planned_works` emptied reads the old triple, the old `BASE_EVENTS` and the old `thread_read`-withheld arm exactly.
# RE-PINNED AT ED-IN-0306 phases 4 and 5 (on top of main at 59f2f97f, ONE AND TWO SEASONS; the build is unmoved): `arrival_only_kinds`
# declines a computed `migrate` onto a territory, so the seed-0 realm's act mix moves (one season: `migrate.refused` 35 -> 40,
# `residence.changed` 3 -> 1, `claim.deposited` 8190 -> 8233; 9334 -> 9378 events). Was 6c26053b... / 299f019e... (one, two
# seasons). CONTROL: main at 59f2f97f, probed in its own checkout by the same run, reads the old pair and the old `BASE_EVENTS`.
# RE-PINNED at v10 SE-06 (B10-07b), A DATA MOVE DECLARED AND A TRAJECTORY MOVE: the 37 population cohorts hold their territory's
# temperament as pursuits (`cohorts.yaml: temperaments:`), so the BUILD hash moves (the cohorts' `pursuits`), and so do one and two
# seasons (the cohorts deliberate with a declared vector instead of the uniform arm). Was fe427626... / 873525df... / 9e71dfe9...
# (build, one, two seasons); events 9378 -> 8913, 28665 -> 27020. CONTROL, run in process on this tree: `temperaments:` deleted from a
# copy of `cohorts.yaml` reads the old triple, the old `BASE_EVENTS` and the old `thread_read`-withheld arm exactly.
# RE-PINNED at v10 CR-21 (M14, B10-07b), A DATA MOVE DECLARED AND A TRAJECTORY MOVE: `happiness`'s `deontological_instrumental` cell
# +0.4 -> 0.0, and SE-06's cohort vectors read that column of `PURSUIT_PROJECTION` (`temperament_pursuits`), so the BUILD hash moves
# (measured alone on the SE-06 tree: that one cell moves the build; `intelligence-diplomatic`'s `community` and the `deed:commitment.ended`
# cells do not); `restore` celled (P/S -0.2) and the deed cells re-rank candidates, so one and two seasons move with it. Was
# aef556ac... / 31e39c05... / 329fa072... (build, one, two seasons); events 8913 -> 9180, 27020 -> 27827. CONTROL: an extracted copy of
# the SE-06 tree (`bcaf1d519`) reads the old build and two-season hashes at seed 0 (`PYTHONHASHSEED=0`). A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at v10 CR-16 (B10-07b), A BEHAVIOUR MOVE DECLARED: `Fixtures stance_polarity` `legacy` -> `declared` (H-194), so a grudge
# pulls the contested acts against its object UP and the act mix moves; `Fixtures` is not hashed, so the BUILD is equal and one and two
# seasons move. Was e9f81463... / f145b1e4... (one, two seasons); events 9180 -> 9347, 27827 -> 27605. CONTROL, run in process on this tree:
# `stance_polarity` swept back to `legacy` reads the old pair, the old `BASE_EVENTS` and the old `thread_read`-withheld arm exactly. A
# GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at v10 CP-T02-01 (B10-09), A BEHAVIOUR MOVE DECLARED: a death names the seats it empties (one `tenure.closed`
# per death write, its receipts the Offices), so every witness's ledger gains a claim on each vacated seat and the act mix
# moves; the BUILD is equal. Was 056584ed... / 71ac6881... (one, two seasons); events 9347 -> 9138, 27605 -> 27154. CONTROL,
# run in process on this tree: `World.seat_holds` stubbed to `[]` (no seat named, the emission off) reads the old pair, the
# old `BASE_EVENTS`, the old `give`- and `thread_read`-withheld arms exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at v10 CP-T02-02 (B10-09), AN ID MOVE DECLARED: a loop-built seat keeps its `offices.yaml` row's id (`populated._seat_id`;
# the throne is `off_king`), so the BUILD moves with every hash that folds an Office id, and the ids seed the draws, so one and two
# seasons move further. Was 3e31638e... / b4aa3024... / 8d535aab... (build, one, two seasons); events 9138 -> 9760, 27154 -> 28883.
# CONTROL, run in process on this tree: `_seat_id` replaced by the slug rule reads the old triple and the old `BASE_EVENTS`
# exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at v10 CP-T03-00 (B10-09), A BEHAVIOUR MOVE DECLARED: both parties of a fight take their band (a felled attacker
# dies; each kind's Event carries only its earners' changes), so the deaths and the deposits move; the BUILD is equal. Was
# ebe18510... / 6f2ec528... (one, two seasons); events 9760 -> 9338, 28883 -> 24224. CONTROL: the pre-item tree (`68767e731`)
# reads the old two-season hash (measured, `build_realm(0)` + `populated.run(seasons=2)`). A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at v10 CP-T02-03 (B10-09), A BEHAVIOUR MOVE DECLARED: a `rung` goal whose rung its org's member governs is MET
# (`world_q.aim_state`) and forms no `need`; `goal_varfell_oastad_gate` is met at build, so its five Varfell members stop asking
# it and the act mix moves; the BUILD is equal. Was 921de777... / cdeb64c2... (one, two seasons); events 9338 -> 9154, 24224 -> 24039.
# CONTROL, run in process on this tree: `aim_state` reading `open` always (`AIM_RULES` cleared) reads the old pair, the old
# `BASE_EVENTS` and the old `thread_read`-withheld arm exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# CP-T02-05 (B10-09) added a stamp, `world_q.oughts_named`, and B10-09 close one REVERTED it (falsified on HR-9 control (4), `Falsified:
# CP-T02-05`): the BASE_HASHES pins below are the reading with the stamp reverted; the build is equal throughout.
# RE-PINNED at v10 IN-61 (B10-09), A DATA MOVE DECLARED: `off_king`'s conferral `null` -> `inheritance` and `off_heir`'s `null` ->
# `appointed` (RS-27), and `Office.conferral` folds into the content hash, so the build and both seasons move; NOTHING ELSE DOES:
# the act sequence (582 / 1230 acts) and the event kinds are equal. Was 4ab812ba... / f699c1d4... / 36d1e6c3... (build, one, two
# seasons). CONTROL, run in process on this tree: the two seats' `conferral` set back to `None` on the built world reads the old
# two-season hash exactly, at seeds 0, 1 and 2. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at B10-09 close one (D2 + D3, then the CP-T02-05 revert), A BEHAVIOUR MOVE DECLARED: a felled attacker's own `person.died` is
# placed where he fell (`world_q.event_place`), and a second `commit` on a held cause is declined person-side (`rosters.yaml:
# held_edge_declines`); the `oughts_named` stamp is reverted, so this is the reading with the stamp reverted. The BUILD is equal. Was
# 763402... (one season) / a7ad6b62... (two seasons); events 8958 -> 9172, 24959 -> 24060. CONTROL, run in process on the pre-revert tree
# (`f28c3f33c`): `oughts_named` stubbed to `()` reads the new two-season hash exactly at seeds 0-2 (8195c6e3... / d44e4b85... / 7d5e3643...; seed 0 is the pin).
# RE-PINNED at ED-IN-0310, A DATA MOVE AND A TRAJECTORY MOVE DECLARED: Jordan, 2026-11-04, "Set foreign=True as the default"
# (ED-IN-0301 had held it off), so `build_realm` seats the Altonian Empire by default: its Proposition, three persons, two seats
# (`off_katepano`, `off_kommerkiarios`), its root territory and settlement outside the realm, and its two goal rows. The BUILD hash
# moves, and so do one and two seasons. Was c7ca8d50... / 53469c5c... / 8195c6e3... (build, one, two seasons); events 9172 -> 9929,
# 24060 -> 26090; the `thread_read`-withheld arm 9161 -> 9918. CONTROL, run in process on this tree: `build_realm(0, foreign=False)`
# reads the old triple, the old `BASE_EVENTS`, the old `thread_read`-withheld arm and `test_go07_canonical_digest.BASE` exactly. A GOLDEN
# RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at CR-10 (B10-09 close two), A BEHAVIOUR MOVE DECLARED: `attention_key` spares a tier-1 own-act echo (arm D2, A1-05), so
# a person answers his own act's echo on his tenure's object or his seat's purview as a tier-1 question; the BUILD is equal. Was
# 5e4d77d3... / 3cfe6b39... (one, two seasons); events 9929 -> 9739, 26090 -> 26934. CONTROL, run in process on this tree: the tier-1
# branch returning tier 4 for an own-act claim (the every-tier screen) reads the old pair and the old `BASE_EVENTS`. A GOLDEN
# RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at v11 CR-28 (B10-09 close two; CP-T02-05's re-take), A BEHAVIOUR MOVE DECLARED: `questions_for` stamps the
# Propositions a person heard of from another (`world_q.propositions_heard`) as `Proposition`, so `commit` and `argue` form on
# them; the BUILD is equal. Was a2ff6dfe... / 01203898... (one, two seasons); events 9739 -> 9741, 26934 -> 27396. CONTROL, run
# in process on this tree: `propositions_heard` stubbed to `()` reads the old pair (two seasons, seeds 0-2: 01203898... /
# fb576b8a... / 39a03ca8..., CR-10's). A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at v11 CR-81 (B10-09 close two, ED-IN-0318), A DATA MOVE AND A TRAJECTORY MOVE DECLARED: `build_realm` writes the
# realm's starting acquaintances (236 `exists:Person` claims, faction co-members and the high-status seats), so the BUILD hash
# moves, and so do one and two seasons. Was 70ea49cb... / 1f573c4c... / 5cfba712... (build, one, two seasons); events 9741 ->
# 10847, 27396 -> 29286; the `thread_read`-withheld arm 9741 -> 10847. CONTROL, run in process on this tree: every
# `build_realm` forced to `acquaintances=False` reads the old triple, the old `BASE_EVENTS`, the old `thread_read`-withheld arm
# and `STEP_OFF_ONE_SEASON` exactly (this file, `test_go07_canonical_digest.py` and `test_governance_build.py`, 117 passed).
# A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at v11 CR-25 (B10-09 close two), A BEHAVIOUR MOVE DECLARED: a computed `establish` founds an office over a
# holding (`establish` declares `Rung`; `questions_for` stamps `holdings_to_found`); two offices founded by two seasons at
# seed 0. The BUILD is equal. Was 5fece5d9... / a38723fd... (one, two seasons); events 10847 -> 10316, 29286 -> 29399.
# CONTROL, run in process on this tree: `holdings_to_found` stubbed to `()` AND `establish`'s `referent_class` dropped reads the
# old pair, the old `BASE_EVENTS`, the old `STEP_OFF_ONE_SEASON` and the old `thread_read`-withheld arm exactly (the term alone
# stubbed does not: 273b223d... / 10843 events, the column moving formation by itself). A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at v11 CR-82 (B10-09 close two, ED-IN-0319), A FIXTURE MOVE DECLARED: `ledger_cap` 200 -> 3200. A realm ledger
# reaches 200 in season 1 and no longer evicts there, so what a person holds moves (one season) and then what he does (two).
# The BUILD is equal (no ledger at build exceeds 12). Was f47dfa8c... / 2f1ba769... (one, two seasons); events 10316 -> 10316
# (the season-1 sequence is byte-identical), 29399 -> 29401. CONTROL, run in process on this tree: the cap swept back to 200
# after `build_realm` reads the old pair, the old `BASE_EVENTS` and the old `STEP_OFF_ONE_SEASON` exactly (and
# `test_go07_canonical_digest.BASE`, seeds 0-2). A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED at v11 CR-17 (B10-09 close two, the series' last item), TWO BEHAVIOUR MOVES DECLARED: commit 1 ships
# `Fixtures odds_weighting` `believed` (H-248: a contested candidate's pursuit term is weighted by the person's believed
# chance of the bands its verb writes in) and commit 2 re-derives `choice_temperature` 0.1 -> 0.05 (H-96, the largest grid
# value at which REM-12's split reads strict-top-decided above one half at seeds 0-2). `Fixtures` is not hashed, so the BUILD is
# equal. AT COMMIT 1 ALONE seed 0 does not move at all (one and two seasons, events and sequence hashes read the old pins: the
# weighting reaches `determine`'s pursuit term only and no seed-0 top changes; seeds 1 and 2 DO move at two seasons, 02a72390...
# and e9bec19c..., measured on a scratch harness, and the `give`-withheld arm below moves). AT COMMIT 2 everything moves.
# Was bdff0832... / a75b8227... (one, two seasons); events 10316 -> 11775, 29401 -> 30477. CONTROL, run in process on this
# tree: `odds_weighting` swept to `none` and `choice_temperature` to 0.1 reads the old triple, the old `BASE_EVENTS`, the old
# `STEP_OFF_ONE_SEASON` and the old `thread_read`-withheld arm exactly; `believed` at 0.1 reads the old triple and the old
# `BASE_EVENTS` and only the step-off arm moves. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-RECORDED at v11 CR-86 (ED-IN-0342; Valorsmark a faction, `fac_crown` -> `fac_valorsmark`, the two vassals' `oblige`
# tenures, the head seats): 3ae970a1... -> b4bc2df0..., 4761e5ca... -> 87b9d1f1..., 7d2adfc5... -> 48f9f394...; the event
# count and digest of `BASE_EVENTS` do not move (the state does, the sequence does not).
# RE-RECORDED at v10 REM-31 (IN-46), A DECLARED MOVER: `the body` carries `march`'s `step: ENCOUNTER` / `declares:
# Declared`, so every `fight`/`accept` is declared at RESOLVE (`fight.declared`/`accept.declared`) and fought at ENCOUNTER on
# the round's settled world. 87b9d1f1... -> 36378f25..., 48f9f394... -> e39919be...; the build is equal. CONTROL, run in
# process on this tree: `the body`'s `step:`/`declares:` popped reads the old pins exactly (this file, go07, cr17, cr81,
# in27 and the corpus pins, 45 passed). A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-RECORDED at v10 REM-30's `verb_capability` rows (`argue: argue`; `research`, `examine`, `surveil: inquiry`), A DECLARED
# MOVER: `train` forms one Candidate per vocation and its act id carries the vocation (`data/verbs.py::act_key`). 36378f25... ->
# 027c7516..., e39919be... -> 4b0f02bd...; the build is equal. CONTROL: the commit's four source files reverted read the old pins
# exactly (this file and the six named with it, 409 passed on the parent tree). A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v10 CR-30's commit for CR-20 + CR-30 TOGETHER (`Person.attributes`, `Person.heritage` in every Person's repr, and
# four authored `heritage:` cast rows whose co-located witnesses hold a different `seen` claim `marks`): build b4bc2df0... ->
# d61848d3..., 1 season 027c7516... -> f2e5e265..., 2 seasons 4b0f02bd... -> 7fbfbe54.... CONTROL, run in process on the parent tree
# (3ce1f08e) and this one: the ordered (kind, id) event list over two seasons is EQUAL at seeds 0 / 1 / 2 (31452 / 30075 / 31432
# events), and so is every ledger's claim list with the heritage rows removed; with them present only `seen` claims differ, in
# their `marks` term alone (158 / 143 / 124 claims). So `BASE_EVENTS` below do not move. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
BASE_HASHES = {0: "d61848d3a174464f9c96fe81fe0204f2",
               1: "f2e5e265012d1d96333a43ff514d2b13",
               2: "7fbfbe54dcfa51f0a7f1663acf6550b8"}

# THE ONE-SEASON PIN WITH CR-81'S STEP OFF (`build_realm(0, acquaintances=False)`: the hash and the event count and digest
# `BASE_HASHES[1]` / `BASE_EVENTS[1]` held before CR-81). The `give`-withheld arm's control, below.
# RE-RECORDED at v11 CR-25: a computed `establish` executes on the step-off arm too. Was 1f573c4c... / (9741, 8eefa8b6...);
# the CR-25 control (the term stubbed and the column dropped) reads the old value exactly.
# RE-RECORDED at v11 CR-82 (`ledger_cap` 200 -> 3200): the hash moves, the event count and digest do not. Was 9368bffe...;
# the cap swept back to 200 reads it exactly.
# RE-RECORDED at v11 CR-17: commit 1 (`odds_weighting` `believed`) moves this arm alone of the pins at tau 0.1 (f5987a4b... ->
# 0aa9d2e1..., events 9952 -> 9952, sequence hash 63160817... -> 33632f41...); commit 2 (tau 0.05) moves it again: f5987a4b... ->
# b82178e8..., events 9952 -> 11808. The two fixtures swept to `none` and 0.1 read the old value exactly.
# RE-RECORDED at v11 CR-86: b82178e8... / (11808, ffbcfc50...) -> 782560b3... / (11822, 477d2d19...).
# RE-RECORDED at v10 REM-31 (every fight deferred to ENCOUNTER): 782560b3... / (11822, 477d2d19...) -> bb5a28b7... / (12257,
# aa01176b...); `the body`'s `step:`/`declares:` popped in process reads the old value exactly.
# RE-RECORDED at v10 REM-30's `verb_capability` rows: bb5a28b7... / (12257, aa01176b...) -> 38b4ff49... / (11807, 8dc5b5fb...); the
# commit's four source files reverted read the old value exactly.
# RE-PINNED ONCE at v10 CR-30 for CR-20 + CR-30 (the Person repr, the heritage rows): 38b4ff49... -> 4cb09ae3...; the event count and
# digest do not move.
STEP_OFF_ONE_SEASON = ("4cb09ae32ace132838ae3e723ea21516",
                       (11807, "8dc5b5fb3768ca1fbd9a790a646e32ca7dcc95037972a1aa7579764170415ff0"))

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
# RE-RECORDED at v10 CP-T05-04 with `BASE_HASHES` (6348 -> 6267, 22009 -> 20840).
# RE-RECORDED at v10 REM-2C with `BASE_HASHES` (6267 -> 6377, 20840 -> 20479).
# RE-RECORDED at v10 REM-52 with `BASE_HASHES` (6377 -> 6484, 20479 -> 20701: the 37 `body.changed` Events of the first
# draw and what the hungry cohorts' bodies move after them; `body_step` swept back to `0` reads the old pair).
# RE-RECORDED at v10 REM-27 with `BASE_HASHES` (6484 -> 6482, 20701 -> 21258; REM-27 reverted in process reads the old pair).
# RE-RECORDED at v10 REM-28 with `BASE_HASHES` (6482 -> 7193, 21258 -> 24535; REM-28 reverted in process reads the old pair).
# RE-RECORDED at v10 REM-28 `dispatch` with `BASE_HASHES` (7193 -> 7196, 24535 -> 24107; the column blanked in process reads the old pair).
# RE-RECORDED at v10 REM-28 `revoke` with `BASE_HASHES` (two seasons only: 24107 -> 24109; one season unmoved at 7196).
# RE-RECORDED at v10 CR-23 with `BASE_HASHES` (7196 -> 9270, 24109 -> 27482; `stock_report = off` in process reads the old pair).
# RE-RECORDED at v10 REM-29 with `BASE_HASHES` (9270 -> 9316, 27482 -> 28806; the `room` conjunct deleted reads the old pair).
# RE-RECORDED at v10 REM-2B with `BASE_HASHES` (9316 -> 9319, 28806 -> 28490; the three rows put back in process read the old pair).
# RE-RECORDED at v10 IN-45 with `BASE_HASHES` (9319 -> 9334, 28490 -> 28526; `planned_works` emptied in process reads the old pair).
# RE-RECORDED at ED-IN-0306 with `BASE_HASHES` (9334 -> 9378, 28526 -> 28665; main at 59f2f97f reads the old pair).
# RE-RECORDED at v10 SE-06 with `BASE_HASHES` (9378 -> 8913, 28665 -> 27020; `temperaments:` deleted in process reads the old pair).
# RE-RECORDED at v10 CR-21 with `BASE_HASHES` (8913 -> 9180, 27020 -> 27827).
# RE-RECORDED at v10 CR-16 with `BASE_HASHES` (9180 -> 9347, 27827 -> 27605; `stance_polarity` swept back to `legacy` reads the old pair).
# RE-RECORDED at v10 CP-T02-01 with `BASE_HASHES` (9347 -> 9138, 27605 -> 27154; `World.seat_holds` stubbed to `[]` reads the old pair).
# RE-RECORDED at v10 CP-T02-02 with `BASE_HASHES` (9138 -> 9760, 27154 -> 28883; `populated._seat_id` replaced by the slug
# rule in process reads the old pair and the old build hash).
# RE-RECORDED at v10 CP-T03-00 with `BASE_HASHES` (9760 -> 9338, 28883 -> 24224; both parties of a fight take their band).
# RE-RECORDED at B10-09 close one (D2 + D3, the CP-T02-05 stamp reverted) with `BASE_HASHES` (9154 -> 9172, 24039 -> 24060).
# RE-RECORDED at CR-10 with `BASE_HASHES` (9929 -> 9739, 26090 -> 26934).
# RE-RECORDED at v11 CR-28 with `BASE_HASHES` (9739 -> 9741, 26934 -> 27396; `propositions_heard` stubbed reads the old pair).
# RE-RECORDED at v11 CR-81 with `BASE_HASHES` (9741 -> 10847, 27396 -> 29286; `acquaintances=False` reads the old pair).
# RE-RECORDED at v11 CR-25 with `BASE_HASHES` (10847 -> 10316, 29286 -> 29399; the CR-25 control reads the old pair).
# RE-RECORDED at v11 CR-82 with `BASE_HASHES` (season 2 only: 29399 / 356dba1b... -> 29401 / 77ef3d40...; season 1 unmoved,
# 10316; `ledger_cap` swept back to 200 reads the old pair).
# RE-RECORDED at v11 CR-17 with `BASE_HASHES` (10316 -> 11775, 29401 -> 30477; commit 1 `believed` alone moves neither at seed 0;
# `odds_weighting` `none` and `choice_temperature` 0.1 in process read the old pair).
# RE-RECORDED at v11 CR-86 with `BASE_HASHES` (11775 -> 11793, 30477 -> 30734). CONTROL, run in process on this tree: the
# two vassals' `oblige` rows (`offices.yaml` `off_king` obligees) dropped read the old season-1 sequence exactly (11775 /
# 87c51e92...) with the build and season hashes still moved by the `fac_crown` -> `fac_valorsmark` rename alone
# (build 2a1d39a5..., season 1 e03b429a...).
# RE-RECORDED at v10 REM-31 with `BASE_HASHES` (11793 / 454fdfe6... -> 11846 / e7a4f9a1..., 30734 / 05951be7... -> 30822 /
# 03960f4d...: each fight's declaration Event and the trajectory the deferral moves); `the body`'s `step:`/`declares:` popped
# in process reads the old pair.
# RE-RECORDED at v10 REM-30's `verb_capability` rows with `BASE_HASHES` (11846 / e7a4f9a1... -> 11581 / 21e9e3eb..., 30822 /
# 03960f4d... -> 31452 / 5417daa3...: `train` forms `argue` and `inquiry` Candidates and its act id carries the vocation, so the
# draws walk another trajectory). CONTROL: the rows commit's four source files reverted read the old pair (the file, 409 passed).
BASE_EVENTS = {1: (11581, "21e9e3eb5b4effd26c1b4541105b502b8f0f9140665ec25c1c10659e773615b7"),
               2: (31452, "5417daa367ae252a81af3225ac1cfcee510116cba57349982bac38cf00f36b4a")}


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
    this arm stops matching: the re-pin would then need a new control, not a re-recorded one.

    ⚠ v11 CR-81: IT DID, AND THIS IS THAT NEW CONTROL. With the realm's starting acquaintances a `give` receiver is known in
    season one, so withholding `give` now moves the shipped season (measured: b3fd7f90... / 10849 events against the pin's
    5fece5d9... / 10847). The equality is kept where it still holds -- on the step-off arm (`acquaintances=False`), whose
    one-season reading is `STEP_OFF_ONE_SEASON` -- and the shipped arm is asserted to DIFFER, so `give` forming in season
    one is what the step changed.

    ⚠ v11 CR-17 (`choice_temperature` 0.1 -> 0.05): `give` no longer forms in season one at the shipped arm, so the
    shipped-arm half reads the equality again (hash, count and digest of `BASE_HASHES[1]` / `BASE_EVENTS[1]`)."""
    for acq in (False, True):
        w = POP.build_realm(0, acquaintances=acq)
        shipped = tuple(w.fixtures.get("withheld_verbs"))
        assert "give" not in shipped, "fixture: `give` is already withheld at the shipped arm"
        w.fixtures = w.fixtures.sweep("withheld_verbs", shipped + ("give",))
        POP.run(seasons=1, seed=0, w=w)
        if not acq:
            assert (w.content_hash(), _digest(w)) == STEP_OFF_ONE_SEASON, (w.content_hash(), _digest(w))
        else:
            # v11 CR-17 (tau 0.1 -> 0.05): `give` no longer forms in season one at the shipped arm, so withholding it
            # moves nothing and the equality holds on BOTH arms again (it was a difference from CR-81 to CR-82; swept
            # back to tau 0.1 the shipped arm differs again: e6dc2911... / 10310 events against 10316, measured in process).
            assert (w.content_hash(), _digest(w)) == (BASE_HASHES[1], BASE_EVENTS[1]), (w.content_hash(), _digest(w))


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
#: RE-RECORDED at v10 CP-T05-04 with `BASE_HASHES`: 6353 / 09edad05... -> 6272 / 70a5221e... (`argue` declares
#: `Proposition`, `open_case` declares `Person`, and the docket question).
#: RE-RECORDED at v10 REM-2C with `BASE_HASHES`: 6272 / 70a5221e... -> 6382 / adb6a991... (`research` declares `Record`
#: and `Record` leaves `occasion_only_classes`; the CP-T05-04 tree `ea6f1dba` reads the old value exactly).
#: RE-RECORDED at v10 REM-52 with `BASE_HASHES`: 6382 / adb6a991... -> 6489 / 177721d7... (`body_step` ships at `10`; the
#: REM-2C tree `a397fa16` reads the old value exactly, and so does this tree with `body_step` swept back to `0`).
#: RE-RECORDED at v10 REM-27 with `BASE_HASHES`: 6489 / 177721d7... -> 6487 / a23c37a6... (`march` declares `Rung`; REM-27
#: reverted in process reads the old value exactly).
#: RE-RECORDED at v10 REM-28 with `BASE_HASHES`: 6487 / a23c37a6... -> 7198 / c05bfef8... (`convene` declares `Rung`; REM-28
#: reverted in process reads the old value exactly).
#: RE-RECORDED at v10 REM-28 `dispatch` with `BASE_HASHES`: 7198 / c05bfef8... -> 7201 / 9a156ea6... (`dispatch` declares `Person`; the
#: column blanked in process reads the old value exactly).
#: RE-RECORDED at v10 CR-23 with `BASE_HASHES`: 7201 / 9a156ea6... -> 9275 / d87f09b9... (the stock report at crossings;
#: `stock_report = off` in process reads the old value exactly).
#: RE-RECORDED at v10 REM-29 with `BASE_HASHES`: 9275 / d87f09b9... -> 9321 / 41d96575... (`migrate`'s `room` conjunct; the
#: conjunct and its refusal key deleted read the old value exactly).
#: RE-RECORDED at v10 REM-2B with `BASE_HASHES`: 9321 / 41d96575... -> 9324 / f14e03ba... (`evade / defy`, `construe` and
#: `exchange` restored; the three rows put back to their base shape in process read the old value exactly).
#: RE-RECORDED at v10 IN-45 with `BASE_HASHES`: 9324 / f14e03ba... -> 9339 / a5cb2f02... (the planned works's terms ripen;
#: `planned_works` emptied in process reads the old value exactly).
#: RE-RECORDED at ED-IN-0306 with `BASE_HASHES`: 9339 / a5cb2f02... -> 9383 / 1b8ac5b5... (the computed `migrate` onto a territory is
#: declined; main at 59f2f97f reads the old value exactly).
#: RE-RECORDED at v10 SE-06 with `BASE_HASHES`: 9383 / 1b8ac5b5... -> 8918 / 0e529f09... (the cohorts' territory pursuits;
#: `temperaments:` deleted in process reads the old value exactly).
#: RE-RECORDED at v10 CR-21 with `BASE_HASHES`: 8918 / 0e529f09... -> 9185 / b82a1ea2... (the cell-value pass).
#: RE-RECORDED at v10 CR-16 with `BASE_HASHES`: 9185 / b82a1ea2... -> 9350 / 714b9f7f... (`stance_polarity` `declared`; swept back to
#: `legacy` in process reads the old value exactly).
#: RE-RECORDED at v10 CP-T02-01 with `BASE_HASHES`: 9350 / 714b9f7f... -> 9137 / 6ba88aae... (a death names its seats;
#: `World.seat_holds` stubbed to `[]` in process reads the old value exactly).
#: RE-RECORDED at v10 CP-T02-02 with `BASE_HASHES`: 9137 / 6ba88aae... -> 9759 / e17367f6... (a loop-built seat keeps its row's id;
#: `populated._seat_id` replaced by the slug rule in process reads the old value exactly).
#: RE-RECORDED at v10 CP-T03-00 with `BASE_HASHES`: 9759 / e17367f6... -> 9337 / c50d4c47... (both parties of a fight take
#: their band); still differs from `BASE_EVENTS[1]` (9338).
#: RE-RECORDED at v10 CP-T02-03 with `BASE_HASHES`: 9337 / c50d4c47... -> 9143 / 2a17f775... (a met rung goal forms no `need`;
#: `aim_state` reading `open` always reads the old value exactly); still differs from `BASE_EVENTS[1]` (9154).
#: RE-RECORDED at B10-09 close one (D2 + D3, the CP-T02-05 stamp reverted) with `BASE_HASHES`: 9143 / 2a17f775... -> 9161 /
#: c808dea8...; still differs from `BASE_EVENTS[1]` (9172).
#: RE-RECORDED at CR-10 (arm D2) with `BASE_HASHES`: 9918 / 37fa2d30... -> 9739 / fde8ab3f... (same count as `BASE_EVENTS[1]`, a
#: different digest); the tier-1 branch returning tier 4 for an own-act claim reads the old value exactly.
#: RE-RECORDED at v11 CR-28 with `BASE_HASHES`: 9739 / fde8ab3f... -> 9741 / 1e77a5a4... (same count as `BASE_EVENTS[1]`, a
#: different digest).
#: RE-RECORDED at v11 CR-81 with `BASE_HASHES`: 9741 / 1e77a5a4... -> 10847 / 83f4c9a2... (same count as `BASE_EVENTS[1]`, a
#: different digest); `acquaintances=False` in process reads the old value exactly.
#: RE-RECORDED at v11 CR-25 with `BASE_HASHES`: 10847 / 83f4c9a2... -> 10316 / af2eb292... (same count as `BASE_EVENTS[1]`, a
#: different digest); the CR-25 control (the term stubbed and the column dropped) reads the old value exactly.
#: RE-RECORDED at v11 CR-17 with `BASE_HASHES`: 10316 / af2eb292... -> 11781 / 43774342... (commit 1 `believed` alone moves it not
#: at all; commit 2, tau 0.05, moves it, and the count now differs from `BASE_EVENTS[1]` too); `none` and 0.1 in process read the
#: old value exactly.
#: RE-RECORDED at v10 REM-31 with `BASE_HASHES`: 11799 / 07b7a36b... -> 11852 / e6f3edeb... (every fight deferred to ENCOUNTER;
#: `the body`'s `step:`/`declares:` popped in process reads the old value exactly); still differs from `BASE_EVENTS[1]` (11846).
#: RE-RECORDED at v10 REM-30's `verb_capability` rows with `BASE_HASHES`: 11852 / e6f3edeb... -> 11582 / e23a1f6e... (the rows
#: commit's four source files reverted in process reads the old value exactly).
THREAD_READ_WITHHELD_EVENTS_1 = (11582, "e23a1f6e568a536f5d34ba1e39b21fc6dd5400feca4bbbec71effeff8f10996e")   # REM-30 rows: was 11852 / e6f3edeb...   # REM-31: was 11799 / 07b7a36b...   # CR-86: was 11781 / 43774342...   # CR-17: was 10316 / af2eb292...; CR-25: was 10847 / 83f4c9a2...; CR-81: was 9741 / 1e77a5a4...


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
