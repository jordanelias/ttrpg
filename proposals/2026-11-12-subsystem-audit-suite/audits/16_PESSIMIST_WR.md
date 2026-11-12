# WR — pessimist audit: NERS, premise and emergent narrative, of the world, its clocks and the narrative engine

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: d161a61 (working tree)

Scope: world, threadwork, clocks, travel, survival, weather, strife and the narrative engine (`loop/encounter.py`,
`loop/calendar.py`, `loop/matter.py`, `queries/world_q.py`, `harness/strife.py`, `storybar.py`, `chronicle.py`,
`arc.py`, `ENDINGS_CLASSIFIED.yaml`), the coupling of eras, regimes and strife to allegiance, duty, obligation,
pursuit and conviction, and the five premise sentences of the world. The WR lane's audit and addendum
(`09_WR_audit.md`, `09_WR_audit_addendum_B.md`), the narrative-churn audit (`20_NARRATIVE_CHURN.md`), the SE
audit (`07_SE_audit.md`) and the game-level pessimist audit (`16_PESSIMIST_GAME.md`) are **cited, not
redone**; a number below is this lane's own run unless a lane is named beside it. All runs:
`PYTHONHASHSEED=0`; scripts and outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_WR/` (§12 lists
each). The machine was heavily loaded (load average 25 to 43, one out-of-memory kill elsewhere), so the
horizons are short and several arms planned were not run; each is named where it would have stood.
PROXY marks a hand-set state (a builder's write before any season).

## 0. Verdict

VERDICT_PENDING

## 1. NERS — the cut tests, executed where a run could decide

Method (`skills/ners/SKILL.md`; definitions `CLAUDE.md` §0.06): propose the cut, name what dies; N from
six directions; E last. A cut here is *executed* as an arm of one built realm (`p2_play.py`, seed 0, three
seasons, the shipped chooser) and read against a **noise control**: the same built realm with a different
chooser draw seed (`drawseed`), which says how far two runs of the *same* game lie apart. A cut whose
distance from the shipped arm is inside that noise, and whose own bookkeeping is all that vanished, is
free.

### 1.1 The noise floor, and the CALENDAR cut

Distance = L1 over the executed-verb counts. Shipped arm: 2,630 acts attempted, 1,190 executed, hash
`52ff67bc…`, which is the WR lane's E-07 world (their 74,510 Events and 1,190 executed), so the instrument
reproduces a sibling's reading before it is trusted.

| arm | executed acts | L1 to shipped (executed verbs) | L1 (attempted) | state components differing from shipped (of 24) | story bar: cross share · executed share | deepest executed chain | strands · concluded |
|---|---|---|---|---|---|---|---|
| shipped | 1,190 | 0 | 0 | 0 | 23.4% · 14.4% | 5: `utter, conceal, create_record ×3` | 5 · 0 |
| `drawseed` (noise) | 1,346 | **316** | 706 | 15 | 19.0% · 10.0% | 5: `commit, utter ×3, tell` | 7 · 2 |
| `calendar` (barrier 1 removed: no Date ever fires, no slot ever forms) | 1,198 | **38** | 145 | 9 | 23.3% · 13.5% | 5: the same five acts as shipped | 5 · 0 |

What the CALENDAR cut removed: 12 `date.fired`, 17 `docket.formed`, the 7 empty slots standing on the
docket at the end. What it did not move: `convene` executes 17 times in both arms (in the cut arm it
schedules 17 dates that never come); `determine` is 0 of 3 in both; `matter.determined` 0 in both;
`open_case` executes 9 times without a calendar against 7 with one; no component of body, conviction,
stores, seats, offices or persons differs. The cut's whole effect on what persons do is an eighth of the
distance between two draws of the uncut game.

**CALENDAR's N-line is false at shipped values.** The line as its design states it: *a sitting is the
occasion on which a matter is heard*. It is true only through `determine`, which the bench never executes
(SC F-SC-01, WR F-WR-13, cited): the calendar fires sittings, forms slots, re-slots waiting matters, and
nothing downstream consumes any of it. From the other directions: bottom-up (the docket item is a real
carrier), lateral (MATTER's lapse reads it), and S's *pauses correctly* (a dated sitting is where a playable
hearing would suspend: `05_SC_playable_hearing_B.md`) all still argue for keeping the barrier. So the
resolution is not to cut it; it is that **the barrier is unproven until a determination depends on a
fired date**, and that a cut arm is the cheap way to know when that becomes true (§4 F-PES-WR-04; §9).
Horizon caveat: three seasons; the lapse at `docket_lapse` 4 is outside it. One seed.

### 1.2 The cut table

| mechanism (owner) | the cut | what dies | evidence | verdict |
|---|---|---|---|---|
| CALENDAR (`loop/calendar.py`) | remove the barrier | its own Events and seven empty slots | §1.1 | **false N-line** today |
| site wear (`matter.py:852-870`) | wear 0 | 74 integers falling 10 a season; first visible Event at season 20 | P1 (§2.1); GAME X1 (site condition equal in the played and the unplayed realm at three seeds); SE F-SE-01 | free inside any played horizon (arm not run; inferred from those three) |
| lattice coupling (`_lattice_strain`) | ships cut | nothing | fixture 0 | not in the game; switched on it is §2.2 |
| weather draw (`season_factor_of`) | ships cut | nothing | fixture `()` | not in the game; switched on it cannot bite: the worst declared outcome halves 1,443 grain against 148 eaten (arithmetic on P1; the weather null arm was not run) |
| bodies clock (`matter.py:726-731`) | ships cut | nothing | rates 0 | not in the game; §4 F-PES-WR-07 on its shape |
| larder draw (`settlements.subsist`) | cut | 37 body falls in season 0, tended back the same season | P1; GAME F-PES-GAME-06 | free after season 0 |
| term maturation (`matter.py:428-435`) | cut | the realm's commonest closure (WR F-WR-13) | cited | **true N-line**, and that is the indictment: a clock is the best closer the game has |
| docket lapse (`matter.py:450`) | cut | petitions never leave | cited (WR F-WR-13) | true, as hygiene |
| claim decay (`matter.py:471-501`) | cut | nothing observable before season 20 (5 of 100 a season; the first claim reaches 0 at season 20) | by reading; the arm was not run | **untested at any horizon this suite has run**, at a cost WR F-WR-09 measures as two thirds of the log |
| the standing-gap crossing, "pressure" (`_standing_crossings`) | cut | nothing: `standing.band_crossed` was emitted 0 times in three seasons in all three arms | P2 kinds | **inert** (§4 F-PES-WR-10) |
| travel leg and its budget penalty (`matter.py:831-843`, `budget.py:60`) | cut | one scene of five, in the season of travel, charged the same to a move across the realm and a move to where the mover stands | §2.3 | free to cut as a *price*; the leg-end write is needed for the bookkeeping. The `leg0` arm was not run |
| flow stamp (`stamp_flow_stakes`) | cut | nothing on 9 of 10 seeds at two seasons | H-274, as WR F-WR-07 cites it | false N-line at short horizon |
| era (`world_q._eras`) | cut | nothing: no loop consumer | NARR §1 | free |
| endings (`endings_reached`) | cut | a list that is `[]` in every run and halts nothing | every arm here; WR F-WR-06 | free in computed play |
| `thread_read` | cut | 2 to 8 `finding.made` a run that find nothing (§2.5) | P2 | free |
| ENCOUNTER (`loop/encounter.py`) | fold the fight back into RESOLVE | the one step a playable host may suspend at (REM-31) | not attacked by a run | holds from one direction (S, *pauses correctly*): **narrowed, not established** |

Sixteen mechanisms: two true N-lines (both clocks that close things), one narrowed, one untested, and
twelve that are free, cut already, or inert at shipped values.

### 1.3 The other way: mechanisms that survive because nothing was tried against them

- **Claim decay.** Every sweep in the tree runs two to six seasons; decay cannot change a decision before
  a claim reaches a threshold a reader uses, and none is reached before season 20. It is the largest
  single cost in the engine and has never been observed to change an act.
- **The lattice coupling.** `test_in35_lattice_coupling.py` plants a harbour and reads the front. Nobody
  ran it on the realm with a source until §2.2(c): it works as documented and has no stopping rule.
- **The story bar's zero.** The WR lane found the bar "cannot fail" (F-WR-03). Tried against it here: a
  realm with no named person (`cap=0`) and with one (`cap=1`), three seasons each. Cross share **0.0%**,
  maximum depth **1**, zero strands, zero eras, in both. So the bar does read nothing where nobody can
  answer anybody, and the WR finding narrows to: *it has no level it calls a failure*, not *it cannot
  read low*. The steelman holds on that point.

### 1.4 E, last

Against what N and R found, the world's machinery is long for what it carries: `loop/matter.py` is 903
lines, about 9,900 Events a season in a realm where nothing happens (P1), to move 74 integers and close
terms. That ratio is the E defect, and it is not fixed by deleting clocks: it is fixed by the clocks
having something to say (§9).

## 2. Premise audit — the five sentences of the world, by execution

Method (`skills/premise-check/SKILL.md`): the ordinary meaning (O) written first; the notes' account (N);
the running code (C) on the smallest world that exhibits the premise, with a control. Verdict words are
the skill's (FOLLOWS, DEPARTS, INERT, WORD), with the depth reached (FORMS, EXECUTES).

### 2.1 "The world changes whether or not anyone acts"

**O.** Left alone, the world is not the same place a year later: seasons turn, harvests differ, people
age, sicken and die, things decay unevenly, one valley fares worse than the next. Waiting is a risk.

**N.** MATTER is "the three motions" (matter wears, memory decays, bodies fall) and the maturing of
terms; weather, ageing and illness and the lattice are built and ship at their controls
(`data/fixtures.py:535, 690-692, 700`; WR F-WR-04).

**C (P1).** `build_realm(0, cap=0)`: the realm's 322 Sites and 37 cohorts, no named person, a chooser
that returns no act, shipped fixtures, 41 seasons (`p1_s0_k125_shipped.txt`, stopped at 41 for load).
The SE lane ran the same shape to 120 seasons (`runs/SE/probe_noacts_s0_120.txt`, its §3 and line 305);
this run agrees with it and is read here for the premise.

| season | harbour, seam (37 each) | band crossings | realm grain yield | grain in store | grain eaten | cohorts, body |
|---|---|---|---|---|---|---|
| 0 | 990 | 0 | 1,480 | 1,480 | 0 (larders empty at build) | 37, all 1000 → 940 |
| 1 | 980 | 0 | 1,443 | 2,775 | 148 | 37, all 940 |
| 20 | 790 | **37 of 37 harbours, in one season** | 1,184 | 24,716 | 148 | 37, all 940 |
| 30 | 690 | **37 of 37 seams, in one season** | 1,036 | 34,114 | 148 | 37, all 940 |
| 40 | 590 | 0 | 888 | 42,032 | 148 | 37, all 940 |

| # | link | O | C observed | verdict |
|---|---|---|---|---|
| 1 | there is a year | seasons differ | `season_of_year` is `None` (no table); every season is the same season | INERT |
| 2 | places fare differently | yes | 37 settlements are one settlement: every band edge is crossed by all 37 in one season | DEPARTS |
| 3 | things decay | unevenly, with accidents | 74 of 322 Sites lose exactly 10 of 1000; 248 are written with a wear of zero (WR F-WR-21) | FOLLOWS in the letter, WORD (`condition.worn` ×322, 74 changes) |
| 4 | people age and die | yes | nobody ages (all 46 individuals `born` at tick 0, `age_at_build` 0), nobody dies | INERT |
| 5 | scarcity bites | sometimes | never after season 0: at season 40 the realm holds 284 seasons of grain, and ore, salt and timber have no eater at all (60,310 ore) | INERT |
| 6 | waiting is a risk | yes | the first Event anyone could notice is at season 20; its consequence is a yield change a tenth the size of the surplus | DEPARTS |

By arithmetic on the measured rate (not run): the last band edges fall at seasons 90 and 95, every
producing Site reaches 0 at season 100, and the stores then feed the cohorts for some 280 seasons more.
The steady-state season costs about 9,900 Events, of which 322 are the wear writes.

**The premise fails at shipped values**: it holds of 74 integers and of nothing a person in the fiction
could notice, fear or be harmed by. Carried by F-PES-WR-03.

### 2.2 "A calamity builds and breaks"

**O.** Something gathers; people can see it coming; it reaches a point and breaks; the breaking is an
event with a before and an after; what people did beforehand changes where and how badly.

**N.** `_lattice_strain`'s docstring: "THE CALAMITY RE-EXPRESSED AS A COUPLING RULE … a worn place drags
the fabric beside it down … one border a season … BOUNDED BY MENDING — persons' `restore` acts", and
what is not built: "the SOURCE … on `build_realm` a non-zero weight couples ordinary wear … not a
Calamity (H-236)". The Rupture has no ending row (WR F-WR-20, R-26). The WR lane's
`09_WR_world_motion.md` edit 1 supplies a source (a wound Site at Askeheim) and then flips the weight to
250.

**C, four arms.**

*(a) Shipped (weight 0).* Nothing: §2.1's table is the whole of it.

*(b) Weight 250, no source, nobody acting, 26 seasons* (`p1_s0_k60_lattice.txt`). The 248 wear-0 Sites
follow the 74 wearing ones down, 40 behind (season 20: dwelling and garrison 830, harbour and seam 790).
Yield, stores, bodies and crossings equal (a) to the unit. No front, because there is no gradient.

*(c) Weight 250, a source planted (PROXY: one dwelling in `terr_T1` at 0 before season 0), nobody acting,
14 seasons* (`p3_s0_k14_c250.txt`). Mean condition by border distance from the source:

| season | ring 0 (32 Sites) | ring 1 (76) | ring 2 (57) | ring 3 (119) | ring 4 (38) | realm yield, all kinds |
|---|---|---|---|---|---|---|
| 0 | 725 | 748 | 998 | 998 | 997 | 4,810 |
| 3 | 303 | 311 | 722 | 932 | 978 | 3,510 |
| 7 | 92 | 93 | 335 | 635 | 837 | 2,173 |
| 13 | 15 | 14 | 62 | 212 | 432 | 719 |

*(d) The same world, played by the shipped chooser, three seasons* (`p2_s0_k3_calamity.txt`):
CALAMITY_PLAY_PENDING

| # | link | O | C observed | verdict |
|---|---|---|---|---|
| 1 | it has a beginning | a cause in the world | none exists; one must be planted by hand (H-236) | INERT |
| 2 | it builds | gathers, unevenly | a ring a season, geometric: one ruined cottage takes the realm's yield from 4,810 to 719 in 14 seasons | FOLLOWS (PROXY) |
| 3 | it can be seen coming | signs, argument | 112 `condition.band_crossed` in 14 seasons, each "a witnessable Event; produce no outcome" | FOLLOWS at FORMS |
| 4 | it breaks | a moment | none: no death, no body falls (every cohort still at 940: §2.1's glut carries them), no Event marks a rupture, `endings_reached` is `[]`; the decay has no floor but zero and no reversal | INERT |
| 5 | people can bound it | at a cost, uncertainly | `restore` is the bound the docstring names: an ungraded, costless, certain rise (`effects_economy.py:181-211`), attempted **0 times** in three seasons in every shipped arm here and at three seeds of GAME's X1 | INERT in computed play |
| 6 | what people did changes it | yes | see (d) | CALAMITY_LINK6_PENDING |

**The premise fails in both halves at shipped values, and in "breaks" in every arm.** A consequence for
a sibling proposal: flipping `lattice_coupling` to 250 with a wound in place, as
`09_WR_world_motion.md` edit 1 schedules, starts an exponential that computed play does not answer and
that has no end. Carried by F-PES-WR-02 and the proposal
`16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md`.

### 2.3 "A journey is dangerous"

**O.** Going somewhere far takes time, costs something, and can go wrong: weather, bandits, a war on the
road, falling ill. Further is worse. Arriving is not certain, or not on time, or not whole.

**N.** `_relocate`: the `contain` edge is re-homed at RESOLVE and the destination appended to
`Person.travel_leg`, "the movement in progress", which MATTER ends at the next barrier; "the distance
penalty is a cost of THE SEASON YOU TRAVEL IN, and nothing after it" (`matter.py:812-815`). CP-T10-01's
person-side price is "[GAP: unowned]" (WR R-23).

**C (P2, the shipped realm, three seasons).**

| reading | seed 0 shipped | seed 0 `drawseed` | seed 1 shipped |
|---|---|---|---|
| executed `move` + `migrate` | 37 | 44 | S1_MOVES |
| to where the mover already stands | 20 | 30 | S1_SAME |
| to another territory | 14 | 10 | S1_OTHER |
| individuals who travelled, and of them harmed (a body fall or death, any cause) | 10, **0** | 12, **0** | S1_HARM |
| individuals who never travelled, harmed | 36, 0 | 34, 0 | S1_HARM_CTL |
| most journeys by one person in one season | 3 | 3 | S1_MAX |
| refused (`travel.blocked`, `migrate.refused`) | 77, 80 | 57, 35 | S1_REF |

| # | link | O | C observed | verdict |
|---|---|---|---|---|
| 1 | a journey goes somewhere | yes | 20 of 37 go to where the mover stands (SE F-SE-11, H-140: cited; SE decides it at R-SE-09) | DEPARTS (SE's) |
| 2 | it takes time | further is longer | arrival is in the same round; a person made three journeys in one season | DEPARTS |
| 3 | it has a price | further is dearer | one scene per leg whatever the distance (`budget.py:60`); 14 crossings of a territory border at the price of a walk across the room | DEPARTS |
| 4 | it can go wrong | a draw | no draw is taken; no code path reads a road (`travel_leg` has one reader, the budget) | INERT |
| 5 | the traveller may arrive harmed, late or not at all | yes | 0 of 10 and 0 of 12 harmed; nobody arrives late; `travel.blocked` is the ladder refusing a destination, not a road closing | INERT |
| 6 | others react | news travels with him | the only non-claim Events with a travel Event among their causes are `travel.ended` (15) and eleven information acts | FOLLOWS, thinly |

**The premise fails at links 2 to 5**: a journey is a free, instant, certain change of address. The
control is honest (non-travellers are unharmed too): nothing in the realm harms an individual at all in
these arms, so travel is not *safer* than staying; it is exactly as safe. Carried by F-PES-WR-06 and the
proposal `16_PESSIMIST_WR_A_the_road_is_drawn.md`.

### 2.4 "A story has a beginning, a turn and an end"

**O.** Someone wants something or is wronged (beginning); something reverses, an advantage is lost, an
ally defects, a promise is broken or kept at a cost (turn); it stops for a reason the people in it would
recognise (end); and it can be told afterwards.

**N.** The story bar counts cross-person antecedents and chain depth and "grades nothing"; the chronicle
renders the deepest chain; strands "conclude" on a terminal move; endings are a Query the season reports.

**C.** Beginnings and ends are the WR lane's measured ground (F-WR-01: openings accumulate; F-WR-13: the
realm closes by clock, 23 lapsed against 3 determined) and are cited. The **turn** had no reading, so
this lane built one (`p2_play.py` part (e)): for every Tenure that closed during the run, who opened it
and who closed it. A turn in the plain sense is an edge one person's act opened and *another* person's
act closed (a grant revoked, a prisoner freed, a pledge released by the one it was made to, a seat
taken).

TURN_PENDING

| # | link | O | C observed | verdict |
|---|---|---|---|---|
| 1 | a beginning | a want or a wrong | plentiful: 616 acts with another person's Event among their causes (seed 0); the deepest executed chain is five acts | FOLLOWS |
| 2 | escalation | a second party raises it | WR F-WR-01: `challenge` 0 of 118, `covenant` 0 of 18 | cited |
| 3 | a turn | reversal by another | TURN_LINK_PENDING | TURN_VERDICT_PENDING |
| 4 | an end | recognisable | `matter.determined` 0, `person.died` 0 at seed 0; closures are terms maturing (WR F-WR-13) | DEPARTS (cited) |
| 5 | the end is an event | a moment | an ending is a predicate recomputed each season (`endings_reached`), emits nothing, halts nothing, and stops holding when an edge closes; both rows read not-held at build (P4) and `[]` in every run | INERT |
| 6 | it can be retold | by a narrator | WR F-WR-14 (who and when, never what) | cited |

### 2.5 "The Thread can be read and mended at a cost"

**O.** There is a fabric with a state; a gifted few can perceive it and learn something true and useful;
perceiving costs the reader; it can be repaired, repairing costs more, and can fail.

**N.** `verb_table.yaml:1853-1870`: `thread_read` is gated on Thread Sensitivity ≥ 30, writes `[]`, emits
`finding.made`; "P-01 CO-MOVEMENT AND THE COHERENCE COST … ARE NOT EXPRESSED HERE"; `rosters.yaml:3295-3296`:
"An ungraded `finding.made` (`interview`, `reconstruct`, `thread_read`) reaches the row and finds
nothing". `(Person, coherence)` is `unproduced`; `systems/threadwork/sim/` is imported by nothing in the
loop (WR F-WR-05).

**C (P2).**

| reading | seed 0 shipped | seed 0 `drawseed` | seed 0 `calendar` | seed 1 shipped |
|---|---|---|---|---|
| `thread_read` attempted / executed | 3 / 3 | 8 / 8 | 2 / 2 | S1_TR |
| what it was pointed at | 1 person, 2 Records | 2 persons, 5 Records, 1 other | 1 person, 1 Record | S1_TR_SUBJ |
| degree | none | none | none | none |
| what the finding observed | the reader's own sensitivity and the gate (`thread_sensitivity` 75, `.gate` 30) and nothing else | same | same | same |
| the reader's body, before → after | 1000 → 1000 | | | |
| claims in the reader's ledger that name the Thread | 0 of 308 | | | |
| `restore` / `work` attempted | 0 / 0 | 0 / 0 | 0 / 0 | S1_RESTORE |

Four of the 46 individuals clear the gate (sensitivities 35, 50, 60, 75; six more are authored below
it).

| # | link | O | C observed | verdict |
|---|---|---|---|---|
| 1 | there is a Thread with a state | yes | no carrier: `Site.condition` under a coupling that ships at 0 is the nearest thing; no reading names it | INERT |
| 2 | a few can read it | yes | 4 of 46 pass the gate; the act forms and executes | FOLLOWS (EXECUTES) |
| 3 | they read *it* | the fabric of a place | pointed at Records and persons (in one small-world run, at the reader himself), never at a Site or a rung | DEPARTS |
| 4 | the reading tells them something | true, useful | finds nothing; the finding's only observations are the reader's own gate | INERT |
| 5 | reading costs | strain | no write; body unchanged; succeeds every time with no draw | INERT |
| 6 | it can be mended | by a working | no thread verb mends; `restore` raises a Site and is never attempted | INERT |
| 7 | mending costs and can fail | yes | `_rise` is certain and free | DEPARTS |

**The premise fails at every link but the gate.** The WR lane's two threadwork proposals carry the build
(the module, the session, the practitioner); what this lane adds is that the one thread verb that runs
today is aimed at the wrong class of thing and reports its own precondition as its finding (F-PES-WR-05).

## 3. Emergent-narrative audit

### 3.1 What stories the world's own machinery can produce (enumerated from the code)

| # | story, by its mechanism | the chain in code | in computed play (three seasons; seeds and arms of §12) | where it stops |
|---|---|---|---|---|
| W1 | a place decays and someone repairs it | wear → `condition.band_crossed` → a claim → a question → `restore` | no crossing before season 20; `restore` attempted 0 | never begins inside a played horizon |
| W2 | dearth | larder draw → shortfall Observation → `transfer` / `requisition` / `migrate` | season 0 only, an artefact of empty larders (WR F-WR-10); `transfer` 2 of 70, both into the giver's own rung (SE) | no dearth after season 0 |
| W3 | a term runs out | `oblige` → `Term` → MATTER closes it | the realm's commonest closure (WR F-WR-13); in the `drawseed` arm `oblige` is attempted **0** times against 111 | contingent on the draw (§3.3) |
| W4 | a sitting | `convene` → `date.fired` → slot → `open_case` → `determine` | 17 convened, 12 fired, 7 slots empty at the end, 0 determined | the bench (SC) |
| W5 | a journey | `move` → leg → `travel.ended` | 37; 20 to where the mover stands; none harmed | no road (§2.3) |
| W6 | the Thread is read | `thread_read` → `finding.made` | 3; finds nothing | §2.5 |
| W7 | the Calamity | lattice coupling → front → crossings → `restore` | cannot occur (weight 0, no source); planted: builds, never breaks, nobody mends | §2.2 |
| W8 | a natural death and a vacancy | bodies clock → `person.died` → `tenure.closed` → `confer` / `succeed` | cannot occur (rates 0); under the WR lane's illness arm 8 deaths, one `confer` (their E-11) | deferred by ruling; shape defect F-PES-WR-07 |
| W9 | a bad year | weather draw → yield | cannot occur (`()`); switched on, cannot bite (§1.2) | the surplus |
| W10 | a strand of strife concludes | `flows_in` → `concluded` | 0 of 5 (shipped), 2 of 7 (`drawseed`) | a reading with no reader (WR F-WR-02) |
| W11 | the realm ends | `endings_reached` | `[]` in every run of every lane | WR F-WR-06 |
| W12 | pressure on a person's standing | `_standing_crossings` → a question about the tellers | 0 Events in three arms | F-PES-WR-10 |

Twelve world stories. One (W3) completes, by clock; three (W4, W5, W6) run and arrive nowhere; eight do
not begin.

### 3.2 What a player's choice changes in them

Not run by this lane (GAME's X4 is the player-proxy reading and is cited). By reading only, marked
`[UNVERIFIED by run]`: a player who travels changes whom he is co-located with and therefore what he
witnesses, and pays one scene; a player who reads the Thread learns nothing; a player who restores raises
a Site by a certain amount that wear takes back at 10 a season; a player who convenes schedules a sitting
that will sit empty unless he also opens a case, which the bench will not determine. None of the twelve
stories offers the player a decision whose outcome is in doubt.

### 3.3 The shape of the tail: are all runs the same run?

Two runs of one built realm that differ only in the chooser's draw seed (§1.1) differ by 316 executed
acts of about 1,250, and are the same run in everything that happens to the world:

| | shipped | `drawseed` |
|---|---|---|
| deaths · determinations · covenants kept · seats changed | 0 · 0 · 0 · 0 | 0 · 0 · 0 (2 offered) · 0 |
| verbs that never execute | `challenge` 0/118, `accept` 0/45, `exchange` 0/79, `train` 0/119, `comply` 0/47, `raze` 0/22, `sabotage` 0/47 | 0/142, 0/49, 0/87, 0/81, 0/53, 0/29, 0/54 |
| fields | 1 lost, 3 unopposed | 1 lost, 4 unopposed |
| Site condition, seats, persons | equal | equal |
| paper | `create_record` 350, `utter` 199, `commit` 95 | 421, 206, 144 |
| **`oblige`** | **42 of 111** | **0 of 0** |

The tail is narrow where the world is concerned and one thing wide where it is not: **the obligation
layer is present or absent by draw seed**. In the `drawseed` arm nobody attempts `oblige` in three
seasons; at seeds 0, 1 and 2 of GAME's X1 it executes 42, 28 and 40 times. The cause was not traced
`[UNVERIFIED]`. Its consequence is for the WR lane's F-WR-13: the matured `oblige` terms that are the
realm's main closure exist only in the runs where the layer forms (F-PES-WR-08).

### 3.4 Eras, regimes and strife against allegiance, duty, obligation, pursuit and conviction

`20_NARRATIVE_CHURN.md` §1 owns the table of the eleven things and is cited. What these arms add: the era
is one, and OPEN, in every arm (73, 51 and 66 moves); strands are 5, 7 and 5 with 0, 2 and 0 concluded;
the CALENDAR cut moves the era by seven moves and no strand. So the strife reading varies more with the
chooser's draw than with the removal of a barrier, and neither changes an allegiance (`release` 2 and 4
executed; no seat changes hands in any arm). The coupling the direction asks about has no executed
instance in these runs: nothing an era, a strand or a regime reads is among the causes of an executed
act that closes or opens an allegiance or a duty.

### 3.5 Extremes

| extreme | run | reading |
|---|---|---|
| no named person (37 cohorts) | `p2_s0_k3_cap0.txt` | 1,049 acts, 494 executed; cross share 0.0%, depth 1; 0 strands; 25 executed moves, all 25 to where the cohort stands; a population attempts `forge` 107 times, `challenge` 79, `conceal` 21 (SE's cohort finding, cited) |
| one named person | `p2_s0_k3_cap1.txt` | the same: cross share 0.0%, depth 1 |
| nobody acting | P1 | §2.1 |
| a Date due in the past | P4 (PROXY) | never fires (F-PES-WR-09) |
| a hundred factions | not run | `[SKIPPED: no builder; `build_realm` has one authored realm (21_PROCEDURAL_GENERATION)]` |

## 4. Findings, ranked worst first

FINDINGS_PENDING

## 12. Evidence log

EVIDENCE_PENDING
