# VERBS · MILITARY — build-out of the seven army rows and the two `movement` rows

## Status: REFERENCE (a verb build-out audit; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: 84d2a02 (working tree)

Work order: `VERBS_BRIEF.md`, FAMILY = MILITARY. Verbs: `train`, `recruit`, `form_unit`, `assign_troops`,
`disband_unit`, `discharge_troops`, `order_unit` (stratum `uncontested_material`) and `migrate`, `move`
(stratum `movement`), nine rows of `engine/season/verb_table.yaml`. The exact edits are in the proposals
named in §0.4; this file holds, per verb, the premise, the state today with its reading, the decided
build-out, and the family's order.

## 0. Verdict and reading

### 0.1 Verdict

**One of the nine works (`migrate`); one executes and goes nowhere (`move`); one forms for everybody and
has never executed (`train`); and six are sound commands that no person in the world can give (`recruit`,
`form_unit`, `assign_troops`, `disband_unit`, `discharge_troops`, `order_unit`).** The six are not stubs: each has a row, an effect, a
pure rule in `modules/mass_battle/armyrecord.py`, a refusal, and a headless menu that lists exactly what
the fold would accept. What is missing is the person. The command rides the act's payload, the operand
vocabulary is closed, so `Fixtures withheld_verbs` holds all six out of formation for everybody
(`data/fixtures.py:1157`), and the one caller that gives them for a faction nobody plays
(`harness/army_presets.py::install`) is shipped off by construction: nothing in the loop, the harness
`run` functions or the corpus calls it. So in every seeded run no `army` Record exists, no field is fought
from an order of battle, and the six `army.*` kinds are in the never-emitted list. The single largest
obstacle for the family is therefore **not an effect but a chooser: there is no commander** (the general
is the unbuilt `MB-08`), and the army economy that would give a commander reasons to raise, keep, order
and send home (wage, ration, readiness, loss) has no cost and no clock, so raising is free and
discharging has no motive.

`train` fails differently: it forms 83 of 83 and executed 0 of 85 attempts, because its subject is the
question's referent (a non-person 39 times, an absent person 33 times) and, when the pupil is present,
he holds no key in the vocation (13 of 13 post-admission refusals): the J-13 (iii) interim forbids
minting a key, and at `build_realm(0)` two of 83 persons hold any key (both `inquiry`; probe, §12). It is
a verb whose every refusal the actor could have read.

`move` emits `travel.moved` 15 times in the reading, and the hole register's own classifier
(`hole_register.yaml` H-329, same seed and span, an earlier HEAD; not re-run here) found 16 of 17 such
moves went to the rung the mover already stood on. Its 40 refusals are 33 journeys *into a person or a
Record* (the question's referent, which the ladder will not seat him in) and 7 unknown audiences. Nobody
in the realm travels to do anything, which is why `with=False` is the commonest refusal of five other
verbs (`train` 33, `give` 17, `surveil` 15, `capture` 7 in the same reading).

Two defects of state were found on the way and are carried in the muster proposal: **a dead commander's
troops stay counted against their cohorts for ever** (probe: after the Duke of Varfell's death
`army_of` reads `None` and the cohort's 40 levy still count against a successor's army,
`world_q.other_army_records` has no holder test), and **nothing lowers an army when the cohort it was
drawn from shrinks or leaves the faction's ground** (the cap is asked only at `recruit`).

### 0.2 What this is read against

- HEAD `84d2a02`. One seeded instrument reading, shared with the PHYSICAL lane so the two families read
  one trajectory: `aperture 2 0` (realm and ladder arms, seed 0, two seasons, `PYTHONHASHSEED=0`, control
  hash EQUAL; copy at `scratchpad/runs/VERBS_MILITARY/aperture_2_0_shared_from_PHYSICAL.txt`) and
  `corpus_run` (`scratchpad/runs/VERBS_PHYSICAL/corpus_run.txt`). The family's own probes are in
  `scratchpad/runs/VERBS_MILITARY/` and are listed in §12.
- One seed is a reading of a trajectory, not a rate (CLAUDE.md §0.1 pt 4); nothing below is a balance
  claim.

### 0.3 State today, one line per verb

`elig` = persons eligible at build (seated / unseated); `formed` = persons who formed it; `att / ex / ref`
= acts attempted, executed (emitted a declared `emits:` kind), refused. Realm arm, `aperture 2 0`.

| verb | elig | formed | att | ex | ref | deciding read of the refusals | verdict |
|---|---|---|---|---|---|---|---|
| `train` | 33 / 50 | 83 | 85 | 0 | 85 | `exists:Person=0` 39 · `with=False` 33 · post-admission 13 (the pupil holds no key) | **forms but is refused**; `capability.raised` never emitted |
| `recruit` | 33 / 50 | 0 | 0 | 0 | 0 | — (withheld) | **unreachable in computed play**; executes by hand-built act |
| `form_unit` | 33 / 50 | 0 | 0 | 0 | 0 | — (withheld) | **unreachable in computed play**; executes by hand-built act |
| `assign_troops` | 33 / 50 | 0 | 0 | 0 | 0 | — (withheld) | **unreachable in computed play**; executes by hand-built act |
| `disband_unit` | 33 / 50 | 0 | 0 | 0 | 0 | — (withheld) | **unreachable in computed play**; no caller at all outside tests and the menu |
| `discharge_troops` | 33 / 50 | 0 | 0 | 0 | 0 | — (withheld) | **unreachable in computed play**; no caller at all outside tests and the menu |
| `order_unit` | 33 / 50 | 0 | 0 | 0 | 0 | — (withheld) | **unreachable in computed play**; no caller at all outside tests and the menu |
| `migrate` | 33 / 50 | 83 | 84 | 10 | 74 | `room` 60 · `path` 13 · `write` 1 | **works** (throttled by capacity, which is the design); its refusals teach the migrant |
| `move` | 33 / 50 | 83 | 55 | 15 | 40 | post-admission 33 (the effect's ladder decline: the destination is a person or a Record) · `audience=UNKNOWN` 7 | **executes and goes nowhere** (H-329: 16 of 17 to the mover's own rung); 33 of 40 refusals are a dead end the actor could have read |

Never emitted in this run, of the family's declared kinds: `army.recruited`, `army.formed`,
`army.assigned`, `army.disbanded`, `army.discharged`, `army.ordered`, `capability.raised`, and the six
`*.refused` kinds of the army rows. Emitted: `travel.moved` 15, `travel.blocked` 53, `residence.changed`
10, `migrate.refused` 61, `train.refused` 85. In the ladder arm (13 persons): `migrate` 0 of 9 (all
`room`), `move` 0 of 3, `train` 0 of 12.

### 0.4 The proposals that carry the edits

| file | verbs | batch |
|---|---|---|
| `proposals/14_VERBS_MILITARY_A_movement.md` | `move`, `migrate` | M-A |
| `proposals/14_VERBS_MILITARY_B_train.md` | `train` | M-B |
| `proposals/14_VERBS_MILITARY_C_the_muster.md` | `recruit`, `discharge_troops` | M-C |
| `proposals/14_VERBS_MILITARY_D_the_order_of_battle.md` | `form_unit`, `assign_troops`, `disband_unit`, `order_unit` | M-D |

### 0.5 The standing rule (Jordan, 2026-11-12: *"we do not do deterministic"*), applied to this family

`AUDIT_BRIEF.md` "Standing rule": every consequential outcome resolves by a draw with a graded,
recoverable result; state sets the odds, the draw sets the outcome. Read against the code at HEAD,
**every one of the nine is a fixed function of state once admitted**, and each is a finding of the same
kind (degrades narrative; touches R-09):

| id | verb | the fixed function today | at |
|---|---|---|---|
| F-VM-01 | `train` | a held key rises by exactly one, every time (probe: `{arms: 2}` to `{arms: 3}`) | `loop/effects_combat.py::_eff_train`, `raised_capability` |
| F-VM-02 | `recruit` | exactly `count` men come, whoever asks and however the place stands toward him | `loop/effects_army.py::_eff_recruit`; `armyrecord.raised` |
| F-VM-03 | `discharge_troops`, `disband_unit`, `assign_troops`, `form_unit`, `order_unit` | the roll changes as written; men, units and orders comply with certainty | `effects_army.py::_apply` |
| F-VM-04 | `move` | an admitted journey always arrives | `loop/effects_migration.py::_eff_move` |
| F-VM-05 | `migrate` | an admitted settler is always housed | `_eff_migrate` |
| F-VM-06 | the unplayed commander | *"The plan is deterministic: it draws nothing"*, and it is folded outside DELIBERATE | `harness/army_presets.py:10`, `troop_types/presets.py` |

What stays arithmetic, and why it may: the cap (`recruit_limit`), the conservation of troopers between
pool and unit, the typed requirements (a path exists, the place has room, the actor holds the roll and
the seat). Those decide whether an act may be attempted and how much there is to move; they are the
rule's own exemptions. **The build-out below gives each of the nine one draw on the engine's one
roller, graded on the four bands, with a recoverable worst band.** The plan a doctrine computes for an
unplayed commander stays arithmetic (it is what he asks for); what he gets is drawn.

Listed for the owning lanes (their files are not edited here):

- **FA** `06_FA_levy_through_the_seat_B.md`: a levy that passes `may_levy` raises its whole count. The
  seat decides who may ask; the answer must be drawn (§3, `recruit`).
- **MB** `audits/04_MB_audit.md` F-MB-01: at the shipped scale the attacker loses 60 of 60, a battle
  whose outcome has one value; its `04_MB_headcount_grade_and_scale.md` repairs it and this family's
  field gate depends on it. `audits/04_MB_audit_addendum_B.md` R-42: `experience` rises "+1 Power a
  step" on a fixed rule, and §B4.3's standing orders fire and are obeyed with certainty once their
  trigger is met `[UNVERIFIED: core/contact.check_orders was not opened by this lane]`.
- **SE** `07_SE_campaign_supply_and_muster.md` R-SE-34: an unfed army is *bounded* at its next field by
  arithmetic. Whether hungry men stay is the thing that could go either way; §3 (`discharge_troops`)
  gives the draw this family owns and names the MATTER half for SE.

## 1. Three mechanisms the family shares

Stated once; each verb section cites them.

**S1. The draw.** Every row of the family joins the graded route (`rosters.yaml: graded_inquiries`,
the tree's one carrier for an act graded by degree with no prize: `research`, `examine`, `surveil`
today; provider `social_contest`, entry `social_contest.roll`, pool by `seam/wrappers/sigma.py::faculty`).
The roster keeps its key; its note gains "and graded acts" (a rename is CORE's and is not asked for).
The obstacle is composed by the one function `proposals/05_SC_obstacle_difficulty_and_modifiers_B.md`
adds (`difficulty + modifiers`, the terms returned and recorded on the Event), never by a second
composer; this family supplies rows of data to it. Each effect reads `res.degree` and writes by band.
`[UNVERIFIED: that the fold runs an effect per band for a graded-route row; the three rows on the route
today write nothing. If it does not, that is the first edit of batch M-A and is CORE's seam.]`

**S2. Two capability keys**, added to `rosters.yaml: verb_capability` (and to the capability table of
`01_CORE_capability_authoring_surface.md` when it lands): `command` (the six army rows) and `wayfaring`
(`move`, `migrate`). A person who holds neither rolls the untrained default, as everybody does today.
Each new key adds one `train` Candidate per formation (`vocation_sourced`), a declared formation mover.

**S3. The commander's occasion and the army's state.** A person forms an army verb only on an `army`
Record he holds (the rows gain `referent_class: Record`; `data/verbs.py::HOLDING_RECORD_KINDS` then
derives `army` and `world_q.records_held_for_holding_rows` stamps it; no new stamp). What the army
needs is read by one reader, `world_q.army_state`, which asks the module's existing
`mass_battle.army_options` entry, the same function the headless menu shows a player; each row's third
conjunct asks one key of it, so a command the army does not need is refused on a read the commander
keeps, and he does not form it again. A command with no payload is carried out to the army's doctrine
(the precedent is `work`: the act's declared delta where it declares one, the engine's rule otherwise);
a command with a payload is the player's, as now.

## 2. The movement rows

### 2.1 `move`

1. **Premise.** *A person goes from where he is to another place he can reach, and is then there.*
   Links: he knows of a place (or of a person and where that person is) → the road is open to him → he
   makes the journey, which can go well or badly → he is present at the destination → what presence
   allows (speaking to, giving to, seizing, training, witnessing) opens there and closes where he was →
   the journey costs him part of the season.
2. **State today.** Row `verb_table.yaml:1188`, `own`, no `referent_class`; cell `contain_path` ∧
   `audience`; effect `_eff_move` → `_relocate` (close the live `contain`, open one, append
   `travel_leg`); refusal `travel.blocked` (flat). Readers of the result: every presence consumer
   (`with`, WITNESS co-location, `standing_at`, the budget's distance penalty until the next MATTER).
   Reading: formed 83, attempted 55, executed 15, refused 40 (33 post-admission, the effect's
   `contain_ascends` decline). H-329: nearly every executed move is to the mover's own rung; H-140: a
   same-place move is not a no-op; H-327: arriving teaches the traveller nothing; H-325: nothing is
   exploration. **Verdict: executes and goes nowhere.**
3. **Build-out, decided.**
   - *Who forms it, when.* On a `Rung` the question carries as a place: the places he has been told
     of (`places_named`), his own home when he is away from it (his own `reside` and `contain` edges),
     and **the place his ledger says a person the question names is at** (a new own-ledger term,
     `whereabouts_named`, fed by an `at` Observation on `travel.moved`, `residence.changed` and
     `army.arrived`). The last is the link the realm lacks: to act on a man who is elsewhere, go to
     him.
   - *Requirements.* Unchanged (path, audience), plus custody and the ladder, which the class now
     makes unreachable for a computed act.
   - *Roll.* Pool `faculty(wayfaring)`. Obstacle: the journey's difficulty (how far up the
     containment tree the common ancestor lies: same settlement 1, same province 2, beyond 3) plus
     named modifiers (winter; a body below its first band; a destination under occupation or siege).
   - *Effects by degree.* Overwhelming: arrives and the leg costs nothing next season. Success:
     arrives (today's write). Partial: arrives spent, two legs laid, so the distance penalty is
     doubled until MATTER. Failure: turned back; he stays where he was, one leg laid, `travel.turned_back`.
     None is a dead end: the worst band costs a scene and a leg.
   - *Writes / emits.* `Person.travel_leg`, `Tenure.until`, `Tenure.since`; `travel.moved`,
     `travel.turned_back`; refusal `travel.blocked`.
   - *Refusals and why each stays.* `path` (the world's shape; deposited, so he does not re-form);
     `audience` (a guard's answer; world-only by ruling); custody. The same-place move is declined in
     the effect on `migrate`'s precedent (H-140 answered at ladder step 4) and is no longer formable.
   - *Reason trail.* The Event carries the obstacle's terms (SC-B) and the `at` Observation.
   - *Readers.* `with` in every family; FI (H-327's arrival deposit is FI's and SE's, cross-listed).
4. **Scales and play surface.** A person-scale act; at settlement and faction scale its sum is who is
   present where (garrisons, courts, `mustered`). The player picks a destination from the places and
   persons he knows; the engine resolves the journey. An NPC forms one Candidate per stamped place.
5. **Tuning hooks.** Season: `calendar` (winter term). Venue: `venues.yaml` guard weight (audience).
   Office and relationship: the audience rule (`world_q.admits_audience`). Geography: the settlement
   graph's cost matrix has no reader (SE F-SE-06, design-first); the difficulty row is where it would
   enter. Data: `rosters.yaml` obstacle rows (S1).
6. **Exact edits.** `proposals/14_VERBS_MILITARY_A_movement.md` §3.
7. **Gate and falsifier.** Same file §4.
8. **Cases.** Every case whose need is a person reaching another (the `with=False` refusals): M-INFO
   and M-SIT cases by way of presence; NSC-05 N5 (retrieving a held person) needs a traveller who
   arrives where the held man is; ARC-20 N2 (a person sent away).
9. **NERS.** N: remove it and presence is frozen at world-gen; holds from below (every `with` cell)
   and laterally (`march`'s arrival is its body). R: the journey can fail, so distance is a strategic
   fact. S: one journey body for `move`, `migrate`, `march`. E, against that: one class, one stamp
   term, one Observation, four bands. Cut test: merged into `migrate`, a visit becomes a change of
   home and the capacity throttle falls on every traveller.

### 2.2 `migrate`

1. **Premise.** *A household leaves the place it lives and settles in another that has room and will
   have it.* Links: it knows of a better place → the road is open → the place has room → it makes the
   journey → it is taken in or it is not → its home is now there, it eats and works there, and it
   counts in that place's people.
2. **State today.** Row `:1153`, `own`, `referent_class: Rung` (`places_named`); cell `path` ∧
   `audience` ∧ `room`; effect `_eff_migrate` (journey plus `reside`); refusals keyed per clause;
   `room`'s read is deposited to the migrant (REM-29). Reading: formed 83, attempted 84, executed 10,
   refused 74 (`room` 60, `path` 13, `write` 1). Readers: `world_q.population`, `capacity`, the larder
   ladder, `raisable_by`, `training_sites`. **Verdict: works**, and it is the only verb of the nine
   that does; its outcome is certain once admitted (F-VM-05).
3. **Build-out, decided.**
   - *Roll.* Pool `faculty(wayfaring)`. Obstacle: the journey's difficulty (as `move`) plus settling
     modifiers: the destination is held by a faction not his own; the destination's larder is in
     shortfall; he owes a live sworn `oblige` to a seat there (easier).
   - *Effects by degree.* Overwhelming and Success: settled (today's write). **Partial: lodged, not
     housed**: the journey is made and `reside` does not move, which is exactly a `move`; he may
     settle next season from where he stands. Failure: turned back, as `move`.
   - *Writes / emits.* As now, with `travel.moved` on Partial and `travel.turned_back` on Failure.
   - *The stale `room` belief* (the row's own stated limit) is answered by
     `01_CORE_claim_fade_as_read.md`; no second fade is built here.
   - *A seat-holder who migrates keeps the seat* (H-309). Answered at ladder step 5: an office is a
     `hold`, not a residence; nothing in Layer 1 ties the two; removal is `revoke`'s. The row's
     `[INTENT UNDETERMINED]` closes as "absence is not vacancy".
   - *A cohort with men under arms that migrates* off its faction's ground: its troops become
     surplus in the army's state (§3.2), and are drawn home there.
4. **Scales.** Person and household; summed, a settlement's growth and decline, and the levy a place
   can answer. The player chooses the destination; an NPC forms it on a place he has been told of.
5. **Tuning hooks.** Affiliation (holder faction of the destination), season, the larder's state,
   capacity (`world_q.capacity`), relationship (oath). Why a household wants to go is the chooser's
   (`01_CORE_unmet_need_is_attended_first.md`), not this row's.
6. **Exact edits.** `14_VERBS_MILITARY_A_movement.md` §3.
7. **Gate.** Same file §4.
8. **Cases.** SE's population cases (`07_SE_arc_needs.md`, cited); ARC-20 (a person sent away to
   live elsewhere); EMG-11 (a rank gated by a place's capacity).
9. **NERS.** N: remove it and no place grows or empties except by death. R: with no player,
   households drift toward room and food, and a levy follows them. S: `move`'s journey, one throttle.
   E: one band added (lodged), which reuses `move`. Cut test: merged into `move`, residence and
   presence are one edge again and one journey bypasses the throttle (the row's own argument).

## 3. The muster rows

### 3.1 `recruit`

1. **Premise.** *An officer who may call men to arms calls them from a place his lord governs, and
   they come, in numbers that depend on the place, its training grounds and how its people stand
   toward him.* Links: he holds the roll of an army and a seat that may muster → the place is within
   that seat's reach and its people are his faction's to call → the call is answered well or badly →
   the men are on the roll, by kind → the place has fewer hands and the treasury another mouth →
   organised into bodies, they fight.
2. **State today.** Row `:1922`, `own`, cell `existence(army)` ∧ `held_by`; payload `cohort`,
   `troop_type`, `count`; effect `_eff_recruit` (the cap is `recruit_limit`); refusal `recruit.refused`
   (flat). Withheld (`data/fixtures.py:1157`). Probe (`probe_army_s0.txt`): by hand through the fold it
   executes (`army.recruited`) and an over-cap ask is refused; the menu offers ten cohorts at 60 levy
   each and no other kind, because the realm holds no training Site (site kinds: dwelling, harbour,
   seam, garrison). FA's probe: a seatless member mints the faction's army and the Duke is then
   refused. Readers: `_order_of_battle` at a field, when a field is fought. **Verdict: unreachable in
   computed play**; certain when reached (F-VM-02).
3. **Build-out, decided.**
   - *Who forms it.* S3: the holder of the army's Record. Eligibility `remit:dispatch` and `may_levy`
     are FA's (`06_FA_levy_through_the_seat_B.md`, adopted whole). Third conjunct `muster_room`: the
     army may raise more under its doctrine and footing from cohorts this seat may levy.
   - *The command.* With a payload: one cohort, kind and count (the player's). Without: the
     doctrine's shortfall, cohort by cohort in id order, each bounded by `recruit_limit`.
   - *Roll.* Pool `faculty(command)`. Obstacle: the kind's `muster_difficulty` (levy 1, trained 2,
     elite 3; a column of the troop table) plus modifiers: a negative stance row of the cohort toward
     the faction; the place's larder in shortfall; more than half the cohort's cap already under
     arms; easier when the cohort is committed to the faction, and when the army's footing is `war`.
   - *Effects by degree.* Overwhelming and Success: the men asked for come. Partial: half come.
     Failure: none come this season (`levy.shirked`); the roll is unchanged and he may ask again or
     ask elsewhere. A doctrine step shares one draw across its cohorts.
   - *Costs.* The scene; the place's hands (SE R-SE-33) and the standing ration abroad (R-SE-34),
     both SE's and shipped off; this row writes no stores.
   - *Unlocks / forecloses.* `form_unit`, `assign_troops`; forecloses the same men for any other army.
   - *Reason trail.* The Event carries the obstacle's terms and the army-state Observations.
   - *Readers.* The field (`_order_of_battle`); SE's `under_arms`; FA's seats; the cohort, which
     witnesses its own levy.
4. **Scales.** A seat's act over a settlement's people, summed to a faction's army and a realm's
   wars. The player's surface is the menu (`harness/military_menu.py`), unchanged; the NPC forms one
   Candidate a season on his army and the doctrine says what it asks.
5. **Tuning hooks.** Office (`offices.yaml`: which posts grant `dispatch`; FA's remit-by-row).
   Affiliation and relationship (the cohort's stance and commit). Venue (training Sites:
   `rosters.yaml: training_endowment`, SE). Season (harvest: a modifier row). Doctrine and footing
   (`references/troops.yaml: doctrines`, MB §B3.3; until it lands, the module's one doctrine).
6. **Exact edits.** `proposals/14_VERBS_MILITARY_C_the_muster.md` §3.
7. **Gate.** Same file §4.
8. **Cases.** M-STORES "a levy per territory" (`levy` 0 in the requirement file); ARC-07, ARC-23,
   ARC-20 N6, NSC-05 N5 need an army to exist before their field does; NPC-072 (a commander on an
   inner council) needs the roll to be held through a seat.
9. **NERS.** N: remove it and armies are world-gen constants. R: an unloved lord raises a thin
   army; a lost war makes the next levy harder (the grudge rows a field writes feed the obstacle).
   S: `requisition`'s authority, the inquiry's roller. E: one conjunct, one draw, no new operand.
   Cut test: merged into `requisition` (men as a store kind) it loses the cohort, who is a person
   and remembers.

### 3.2 `discharge_troops`

1. **Premise.** *A commander sends men home; they go back to their fields and stop eating his
   stores.* Links: he holds the roll → some of his men are not needed or cannot be kept → he
   dismisses them → they go, or they will not go unpaid → they are off the roll and count again as
   the place's hands.
2. **State today.** Row `:2014`; payload `cohort`, `troop_type`, `count`; only trained, unassigned
   troops may go; refusal flat; withheld; no caller outside tests and the menu. Probe: executes by
   hand (`army.discharged`). Nothing gives a reason to do it: an army costs nothing to keep.
   **Verdict: unreachable, and motiveless.**
3. **Build-out, decided.**
   - *Formation.* S3, conjunct `surplus`: troops above the footing's target, troops of a cohort the
     faction may no longer levy, troops above a shrunken cohort's cap. Eligibility as `recruit` (FA).
   - *The command.* Without a payload: the surplus, unassigned first, then released from the
     largest units. With one: as now.
   - *Roll.* Pool `faculty(command)`. Obstacle 1 plus: arrears (a live ration shortfall on the
     army's treasury, SE); the army stands on another faction's ground; easier for levy.
   - *Effects by degree.* Overwhelming and Success: they go. Partial: half go. Failure: none go
     (`discharge.balked`): unpaid men do not disband on a word. Recoverable: pay, march home, ask
     again.
   - *The half with no commander.* An army whose Record nobody holds, and troops the army may no
     longer keep, face a dispersal draw at MATTER (a hazard, as bodies face one), graded: hold, half
     go, all go; `army.dispersed`. A successor takes up the old roll at his mint and does not start
     a second.
4. **Scales.** As `recruit`, in reverse; at realm scale, demobilisation after a war.
5. **Tuning hooks.** Footing (the army-level order); doctrine's peace share; season; SE's ration.
6. **Exact edits.** `14_VERBS_MILITARY_C_the_muster.md` §3.
7. **Gate.** Same file §4.
8. **Cases.** ARC-07 "The Army That Stayed" is this verb's failure band and the leaderless draw: an
   army that does not go home is a story about persons who would not.
9. **NERS.** N: without it an army only grows. R: standing down is a decision with a loser. S: the
   op and its cap are `recruit`'s. E: the surplus is one key of the state the menu already shows.
   Cut test: merged into `assign_troops` with a negative count it loses the difference between
   leaving a unit and leaving the army.

### 3.3 `train`

1. **Premise.** *A person practises a skill, or teaches someone who is with him, and over a season
   the learner may get better at it.* Links: a learner and a skill → a teacher who knows more, or
   none → a place suited to it, or none → the season's work succeeds or does not → the learner's
   rank rises → every later roll on that skill draws on it. For soldiers: a cohort drilled at a
   barracks fights better.
2. **State today.** Row `:1898`, `own`, cell `existence(Person)` ∧ `with`; one Candidate per
   vocation; effect `_eff_train` raises a held key by one and never mints. Reading: 83 formed, 85
   attempted, 0 executed. Probe: self-training `arms` and `copying` with no key is `train.refused`;
   with `{arms: 2}` it is `capability.raised` to 3, every time. The corpus ranking excludes it (no
   celled axis). **Verdict: forms but is refused.**
3. **Build-out, decided.**
   - *Formation.* `referent_class: Person`, so the subject is a person the question names (himself
     included) and never a Record, a place or a Proposition (39 of 85 refusals). The teacher's own
     capability is not read at formation: capability gates nothing (ruled, #353 §9.2; probe P11).
     An absent pupil is refused on `with`, and that read is deposited to the actor (§2.1's edit), so
     it is not formed twice.
   - *Minting.* `01_CORE_capability_authoring_surface.md` Edit 9 (a first rank is never a loss) is
     adopted; this row depends on it and does not restate it.
   - *Roll.* Pool: the teacher's `faculty` in the vocation taught. Obstacle: the learner's present
     rank (1 at least) plus: self-taught; no Site or venue of the vocation's training kind where
     they stand; a teacher who does not outrank the learner.
   - *Effects by degree.* Overwhelming and Success: one rank. Partial: no rank; the season counts
     as a good result in the learner's practice record (the CR-18 addend), so his next rolls on the
     skill draw a little more. Failure: nothing (`training.fruitless`). At the ceiling the write is
     refused and the read deposited.
   - *Drill.* Training a cohort `Person` in `arms` is training soldiers; the field reads the
     cohort's `arms` as the quality of troops drawn from it (MB §14, its step 8). No unit object is
     trained (§6).
   - *P-08.* Thread Sensitivity stays outside the range.
4. **Scales.** Person to person; a cohort is a person at weight, so the same act drills a levy.
   Faction scale is its sum (a faction with barracks and drillmasters fields better men).
5. **Tuning hooks.** Venue (`trained_at` on the capability row, CORE's table; Sites and
   `venues.yaml`); relationship (teacher and learner regard, a modifier row); season; ceiling
   (`scale.ceiling`). Alignment cells so the chooser can prefer it: `rosters.yaml: tables.alignment`
   (CHAR's `02_CHAR_choice_alignment.md`).
6. **Exact edits.** `proposals/14_VERBS_MILITARY_B_train.md` §3.
7. **Gate.** Same file §4.
8. **Cases.** M-CAP (12 cases, 15 core needs: "`train` attempted and never executed"): SCN-05,
   NPC-087, -032, -006, -009; ARC-23 N2 (whether anyone invested in a rarely used skill); the §14
   advancement row (training by another; a ceiling).
9. **NERS.** N: remove it and capability changes only by bleeding (`_grown`). R: characters become
   what they spend seasons on. S: the pool is the roll every skill already uses; the Partial band
   is the practice rule, not a second progress track. E: one class, one route row, four bands.
   Cut test: merged into practice-by-doing, nobody can learn what he has not yet dared to do.

## 4. The order-of-battle rows

Common to the four: formation S3; pool `faculty(command)`; with no payload the command is the
doctrine's step; the Event carries the obstacle's terms and the army-state Observations; the reader
of every result is the field (`seam/wrappers/mass_battle.py::_order_of_battle` → `armyrecord.fielded`).
Layer 1's bearing on them is §6. The unit row gains one field, `raw` (a body not yet steady: one
Discipline lower in the field until a later order or drill succeeds), which carries the graded half
of forming and filling. Exact edits and gates: `proposals/14_VERBS_MILITARY_D_the_order_of_battle.md`.
Verdict for all four: **unreachable in computed play; certain when reached (F-VM-03).**

### 4.1 `form_unit`

1. **Premise.** *A commander makes a body of one kind of soldier, under a name and a role.* Links:
   trained men of that kind → a place on the roll (twelve at most) → the body takes shape, well or
   raggedly → it can be filled, ordered and fielded.
2. **State.** Row `:1945`; payload `name`, `troop_type`, `role`; probe: `army.formed`.
3. **Build-out.** Conjunct `unformed` (trained troops of a kind that has no unit). Obstacle: the
   kind's `drill_difficulty` plus no training Site of its kind where the commander stands. Bands:
   Overwhelming and Success, formed and steady; Partial, formed `raw`; Failure, not formed this
   season (`unit.unformed`).
4. **Scales / surface.** The player names and shapes bodies in the menu; an NPC forms what the
   doctrine prescribes for the troops he has.
5. **Hooks.** Troop table (`roles`, `drill_difficulty`), doctrine rows (`default_role`, post).
8. **Cases.** SCN-14 and ARC-23 need named bodies with officers (MB R-40's `officer` column).
9. **NERS / cut test.** Folded into `assign_troops` (assigning to a name that does not exist forms
   it), what dies is the empty unit, which the field drops anyway, and one scene a unit. It is kept
   because the draw differs: forming is drill, filling is obedience. Listed in §9 with the fold as
   the other option.

### 4.2 `assign_troops`

1. **Premise.** *A commander puts trained men into a body, or takes them out.* Links: men on the
   roll in no body → a body of their kind → they join it, all or some → the body is as strong as its
   men.
2. **State.** Row `:1968`; payload `name`, `cohort`, `count` (negative releases); probe:
   `army.assigned` both ways.
3. **Build-out.** Conjunct `unassigned`. Obstacle 1 plus: an influx larger than the body's present
   strength; a `raw` body. Bands: Overwhelming, all move and the body is steady; Success, all move;
   Partial, half move, and a body more than doubled turns `raw`; Failure, none move (`assign.balked`).
9. **Cut test.** Removed, trained men never fight (`unassigned` troops do not field).

### 4.3 `disband_unit`

1. **Premise.** *A commander breaks up a body; its men stay with the army.* Links: a body too weak
   or of the wrong kind → the order to break it up → the men return to the pool, or some go home, or
   the body will not be broken.
2. **State.** Row `:1991`; payload `name`; probe: `army.disbanded`.
3. **Build-out.** Conjunct `understrength` (a body under the rout floor, the menu's
   `subformation_routs` advisory). Obstacle 1 plus the body's `experience` (MB R-42) and arrears.
   Bands: Overwhelming and Success, broken up, every man to the pool; Partial, broken up, half its
   men to the pool and half gone home; Failure, it stands (`unit.balked`).
9. **Cut test.** Folded into `assign_troops` (release to zero drops the row), what dies is a
   veteran body's refusal to be broken, the one band with a story in it.

### 4.4 `order_unit`

1. **Premise.** *A commander tells a body how to fight (its role, how hard it presses, whom it
   seeks, when it falls back), or sets the whole army's footing and doctrine; in the field the body
   does as it was told, if it took the order in.* Links: a body and an order within its kind's menu →
   the order is understood or not → the body carries it into the next field → the field goes
   differently.
2. **State.** Row `:2037`; payload `name` with `role`, `stance`, `target`, `fall_back_at`, or
   `strategy` alone; probe: `army.ordered`, and the same order twice is `order_unit.refused` (a
   no-op).
3. **Build-out.** Conjunct `off_doctrine` (a body whose orders differ from its doctrine's, or the
   army's footing differs from what the commander's faction is at). Army-level payload: `footing`
   (`peace`, `war`) or `doctrine`, each alone, as `strategy` is today (MB R-34 takes `strategy` off
   the choice surface). Obstacle: 1, plus one when more than two fields change, plus one for a `raw`
   body, eased or hardened by the kind's Discipline. Bands: Overwhelming, taken in, and a `raw` body
   is steadied; Success, taken in; Partial, role and stance taken in, the rest unheeded; Failure,
   the old orders stand (`order.unheeded`). MB's standing orders (§B4.3) ride this row's payload
   when they land; whether a standing order is *obeyed in the field* is the resolver's draw and MB's
   to state (§0.5).
9. **Cut test.** Removed, every army fights by its kind's default and composition is the only
   choice. Under an auto-resolve that is a calculation (§6, option (b)), this row is decorative for
   every battle nobody watches.

## 5. The family, from above

### 5.1 Dependency graph (an arrow reads "must land before")

```
[S1 graded route carries writes] ─┬─> move ──> migrate
                                  │      └──(the `at` Observation, the `with` deposit)──> train
[CORE Edit 9: first rank] ────────┴─────────────────────────────────────────────────────> train
[FA levy through the seat] ──> recruit ──> discharge_troops
[S3 class, state reader, doctrine step] ──> recruit ──> form_unit ──> assign_troops ──> order_unit
                                                              └─────> disband_unit
train (cohort `arms`) ──> [MB step 8: quality from training]
```

### 5.2 Cross-family and cross-lane dependencies

| needs | from | why |
|---|---|---|
| the graded route runs a degree-keyed effect | CORE (the seam) | S1; `[UNVERIFIED]` whether it already does |
| one obstacle composer, terms on the Event | SC (`05_SC_obstacle_difficulty_and_modifiers_B.md`) | S1; this family adds rows only |
| a first rank is never a loss; the capability table | CORE (`01_CORE_capability_authoring_surface.md` Edit 9) | `train` |
| claim fade | CORE (`01_CORE_claim_fade_as_read.md`) | the stale `room`, `muster_room` and `with` beliefs |
| `may_levy`, `may_wage`, the seat on the mint | FA (`06_FA_levy_through_the_seat_B.md`, `06_FA_war_lives_in_seats_B.md`) | `recruit`, `discharge_troops`, the footing |
| a held Record's kind narrows formation | this family's M-C edit, shared with every `Record`-classed row (`carry`, `comply`, `found`, `build`) | S3; a declared mover for those four (REM-25's wrong-kind residue stops) |
| `create_record` forms the army mint for a muster-seat holder whose faction has none | the family that owns `create_record` | an NPC's first army; until then `armies_at_build` |
| the scale and the grade of a field | MB (`04_MB_headcount_grade_and_scale.md`) | the M-D gate (a fought field that varies) |
| the troop file, doctrines, standing orders, `experience` | MB (`04_MB_unit_loadout_and_weapon_in_hand_B.md`, `04_MB_manager_battle_one_resolver.md`, R-42) | data the muster and the orders read; staged, not blocking |
| training Sites, hands under arms, the standing ration | SE (`07_SE_campaign_supply_and_muster.md`) | more than levy; the cost that makes `discharge_troops` a choice |
| a `march` candidate on a defended enemy place | PHYSICAL (`14_VERBS_PHYSICAL_B_field_and_ruin.md`), CHAR | an army with somewhere to go |
| the carry rule for a unit's second weapon | PC (`03_PC_loadout_and_carry.md`), MB `_B` | a loadout rides `order_unit` (`in_hand`) only after both |

### 5.3 Landing order

| batch | lands | gate (execution artifact) |
|---|---|---|
| M-A | `move`, `migrate` (proposal A) | `aperture 2 s`, s = 0 to 2: `travel.moved` to a rung other than the mover's own above 0 at every seed; no `move` aimed at a person or a Record; all four bands of `move` occur across the three seeds; `migrate`'s Partial leaves `reside` unmoved |
| M-B | `train` (proposal B), after CORE Edit 9 | `capability.raised` leaves the never-emitted list; a person with no key gains a rank and his pool is not lower; over 200 seeds of one hand-built lesson the four bands each occur |
| M-C | `recruit`, `discharge_troops`, S3 (proposal C), after FA's levy | with `armies_at_build: empty`, `army.recruited` in a seeded realm run from an NPC's own act through DELIBERATE; a levy by a hated seat raises fewer men than one by a loved seat over 200 seeds; the successor takes up the dead commander's roll |
| M-D | `form_unit`, `assign_troops`, `disband_unit`, `order_unit` (proposal D), after MB's scale and grade | the six `army.*` kinds out of the never-emitted list; a seeded field fought from an NPC-raised order of battle; two commanders of different `command` field different armies from equal means over seeds |

## 6. The Layer 1 conflict, named

Not edited by this lane; the passages were opened by the MB lane at the lines it gives
(`audits/04_MB_audit_addendum_B.md` §B5.4), and are cited from there, not re-opened here.

- **"Units are persons, at weight. One type; there is no unit class"**
  (`architecture/meta/03_VERBS_AND_LOOPS.md:258-270`, `10_FACTIONS_AND_DEPLOYMENT.md:89`,
  `04_CODE_ARCHITECTURE.md:802`), amended for armies by ED-IN-0306 at `04:813` only. Four of this
  family's rows make and order "units". The build-out stays on the amended text: a unit is a row of a
  Record a person holds; its men are headcounts of cohort persons; training is `train` on the cohort
  person; loss is the cohort's `body`; `raw` and MB's `experience` are columns of the row. The two
  un-amended sites are IN's pointer edit (MB R-38).
- **"No second resolver. No auto-resolve formula. No fast path"** (`holonic_ARCHITECTURE.md:984-990`).
  The doctrine step is not one: it resolves no contest and takes no shortcut through the fold; it is
  the payload a commander leaves unsaid, carried out by the same verb, the same module operation and
  the same draw as a spoken one. The muster's draw uses the one roller.

Both go to Jordan with two options each (§9), as the brief requires.

## 7. Resolutions decided by this lane

| # | kind | what | decided | ladder step | proposal |
|---|---|---|---|---|---|
| 1 | gap | the nine rows are fixed functions of state (F-VM-01 to -06) | one draw each on the graded route | ruling (the standing rule) | A to D |
| 2 | gap | `move` forms on persons and Records, and on the mover's own rung (H-329) | `referent_class: Rung`; the home term; the whereabouts term | 4 (`migrate`'s class) | A |
| 3 | unclear | is a same-place move a no-op (H-140) | declined in the effect, as `migrate` declines a same-home migration | 4 | A |
| 4 | unclear | does migrating away vacate a seat (H-309) | no; an office is a `hold`, removal is `revoke`'s | 5 | A (note only) |
| 5 | gap | `with` is world-only, so an absent subject is re-formed every season | the refusal's `with` read is deposited to the actor | 4 (`room`, REM-29) | A |
| 6 | inconsistency | `train` forms on any referent | `referent_class: Person` | 4 | B |
| 7 | inconsistency | J-13 (iii): no key is ever minted, so nobody learns | superseded by CORE Edit 9 | 1 | B (pointer) |
| 8 | gap | the army verbs are withheld for want of a payload carrier | a payload-less command is the doctrine's step; formation on the held roll | 4 (`work`) | C |
| 9 | inconsistency | a dead commander's troops count against their cohorts for ever | the successor takes up the unheld roll; a leaderless army faces a dispersal draw | 5 | C |
| 10 | gap | nothing lowers an army when its cohort shrinks or leaves | `surplus` in the army's state; the same dispersal draw | 5 | C |
| 11 | unclear | "unit" against "subformation" | MB R-30 (the record's key keeps its spelling) | 1 | none |
| 12 | gap | the unplayed commander is folded outside DELIBERATE (F-MB-16, F-VM-06) | he forms the same six verbs through the one chooser; `army_presets.install` stays as a world-gen arm only | 5 | C, D |
| 13 | gap | each army verb once a season by the opportunity key (F-MB-13) | a doctrine step is one act a season; a spoken command is keyed by its payload | 4 (`act_key`'s choice suffix) | C |

## 8. Capability and chooser surface (for the holistic stage)

- Capabilities read: `command`, `wayfaring`, and the vocation taught (S2). All through `faculty`; no
  private scheme. Axioms: skill check against a difficulty with situational modifiers; training by a
  teacher with a ceiling; a levy as an opposed-by-disposition check; morale as obedience.
- The chooser: one interface for a player and an NPC. The player's army acts come from the menu
  through `play_surface.dispatching_chooser`; an NPC's from `opening_set`. Both fold the same act.
  What makes commanders differ: their `command`, their doctrine and footing (data on the roll they
  hold), their seat's reach, and how their people stand toward them. What is still missing for a
  characterful choice *among* doctrines is content-aware scoring (CHAR's `02_CHAR_choice_alignment.md`).

## 9. Decisions that survive to Jordan

1. **A unit: a row on a roll, or a thing in the world** (§6; MB §B11 item 2). *(a) A row* (this
   build): bodies are groupings of cohort persons' headcounts; their quality is their people's;
   Layer 1 as amended stands; "the army that stayed" is a story about persons. *(b) A thing:* a
   regiment has identity, memory, reputation and its own training; `train`, `form_unit` and
   `disband_unit` act on it; persons hold claims about it; §C.5.1 is amended again and the knowledge
   model gains a kind.
2. **Auto-resolve: a mode of the one resolver, or a calculation** (§6; MB §B11 item 1). *(a) A
   mode:* every battle runs the cell resolver on the orders these verbs wrote, so `order_unit` and
   `form_unit` matter to every war. *(b) A calculation:* unwatched wars are cheap, and the four
   order-of-battle verbs decide nothing in any battle the player skips.
3. **Three organising verbs, or one.** *(a) Three* (this build): `form_unit`, `assign_troops` and
   `disband_unit` each carry their own draw (drill, obedience, a body's pride). *(b) One:* forming
   and disbanding fold into `assign_troops`; a commander spends fewer scenes on his roll and the
   `raw` and `unit.balked` bands go. Shown with its cut test in §4.1 and §4.3; (a) is taken because
   R-05 asks for the rows built and each survives its cut by one band.

## 12. Evidence log

`PYTHONHASHSEED=0`, read-only, no `pytest`, nothing written to a tracked file. Outputs in
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/VERBS_MILITARY/`.

| run | seed, span | outcome |
|---|---|---|
| `aperture 2 0` (shared; the PHYSICAL lane's run, copied as `aperture_2_0_shared_from_PHYSICAL.txt`) | 0, two seasons, realm and ladder arms | §0.3; control hash EQUAL |
| `corpus_run` (shared, `runs/VERBS_PHYSICAL/corpus_run.txt`) | 0 | executed 23 of 67, `move` among them; `train` only refused; `migrate` and the six army rows never attempted; ranking excludes `train` |
| `probe_army.py 0` → `probe_army_s0.txt` | `build_realm(0)`, hand-built acts through `SeasonDriver.resolve` | 0 army Records at build; 2 of 83 persons hold a capability key (`inquiry`); site kinds dwelling, harbour, seam, garrison; mint, `recruit`, `form_unit`, `assign_troops`, `order_unit`, release, `discharge_troops`, `disband_unit` each emit their kind; a repeated order and an over-cap levy are refused; after the commander's death through the gate: `army_of` None, `other_army_records` 1, the cohort's 40 levy still counted against the successor's army, and the faction can raise nobody (the cohort is not `raisable_by` it while the seat is vacant); `train` on self: refused with no key, `{arms: 2}` to `{arms: 3}` with one |
| MB lane's `presets_probe.py` (`runs/MB/presets_on.txt`), read, not re-run | 0, two seasons | preset armies are levy only (600, 900, 600); no field fought with or without them |

Not read by this lane: `core/contact.check_orders`; every reader of `row.counterparty`; the in-season
WITNESS deposit for an army Event (the probe folds between seasons, where WITNESS does not run); the
`.designs/` mass-battle set beyond what the MB audit and addendum quote.

