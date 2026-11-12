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

**The world, as it runs, is a set of clocks that keep time for nobody: none of the five sentences that
describe it survives execution past its first or second link, and the one thing the narrative engine was
never asked is the thing it lacks, a turn.** Run with nobody acting for 41 seasons the realm is one ramp
in 37 identical places, with its first noticeable Event at season 20 and 284 seasons of grain in store
at season 40. Switched on, the Calamity is a second uniform ramp; given a hand-planted source it takes
the realm's yield from 4,810 to 719 in fourteen seasons without one death, one rupture or one ending,
and the played realm decays exactly as the unplayed one (ring means equal to the unit; `restore`
attempted 0 times while 24 band crossings were witnessed). A journey harms none of 33 travellers at
three arms, takes no time and costs the same across the realm as across a room. The Thread is read 17
times in four arms, off nine documents and seven persons and no place, and each reading reports the
reader's own entry requirement as its finding. And of 33 edges that closed in two seeds, 33 were closed
by their own holder and none by anyone else, against 2,298 left open: stories here begin, and are
answered, and do not turn.

The cut tests agree. Against a noise control (the same realm, another chooser draw: 316 executed acts
apart), removing CALENDAR entirely moves the realm by 38 and no story reading at all; planting the
Calamity moves it by 24; removing the stock report moves it by 161 and kills exactly one verb
(`migrate`, 16 to 0). Of seventeen world mechanisms three have a true N-line, and two of those are
clocks that close things because nothing else does.

The steelman is owed and partly holds: replay is exact (the same seed twice gives one hash); the story
bar does read zero where nobody can answer anybody (a realm of 37 cohorts, and of one named person:
cross share 0.0%, depth 1), which narrows the WR lane's "cannot fail"; L5 is kept everywhere (no clock
decides anything); and the lattice rule does exactly what its docstring says. The burden stays on the
mechanism: every one of those virtues is a property of a substrate, and none is a thing that happens.
**The single largest obstacle in this scope is that the world emits and nobody is asked:** crossings,
journeys, sittings and readings each end in an Event that raises no question carrying the place or the
person it is about, so the clocks cannot be answered even where a verb exists to answer them. Four
proposals carry what this lane can decide; nothing here needs Jordan.

*Cited, not redone:* escalation and endings (WR F-WR-01, F-WR-13), the instruments' design (F-WR-03,
F-WR-14), threadwork as a module (F-WR-05, F-WR-17), the surplus and the identical settlements (SE
F-SE-01), the game-level seam matrix (GAME §1.2), the eleven things (NARR §1).

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
| `stock0` (MATTER's stock report off, CR-23) | 1,191 | **161** | 438 | 20 | 21.8% · 11.8% | 5: `dispatch, issue, dispatch ×2, reconstruct` | 2 · 0 |
| `calamity` (weight 250, a source planted; §2.2) | 1,196 | **24** | 96 | 13 | 23.0% · 14.0% | 5: the same five acts as shipped | 6 · 1 |
| shipped, run a second time (replay control) | 1,190 | 0 | 0 | 0 (hash equal) | equal | equal | equal |

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

**The stock report's N-line is true, narrowly.** With the report off the realm is 161 from shipped, half
the noise, and the story bar sits inside the spread the two draws span (cross share 19.0 to 23.4%). The
acts that answer a clock do not fall (story-bar class `world`: 368 against 365), so the GAME lane's
reading that persons mostly answer the granary is not the stock report's doing. One thing dies outright:
**`migrate` executes 0 of 101 against 16 of 116** (13 in the noise arm), so the report is what a migration
is admitted on. The cause was not traced `[UNVERIFIED]`. A cut that looks free on every aggregate and
kills one verb is the case for reading a cut by component, never by headline.

### 1.2 The cut table

| mechanism (owner) | the cut | what dies | evidence | verdict |
|---|---|---|---|---|
| CALENDAR (`loop/calendar.py`) | remove the barrier | its own Events and seven empty slots | §1.1 | **false N-line** today |
| the stock report (`matter.py::_stock_report`, CR-23) | `stock_report = off` | every executed migration (16 → 0); nothing else outside the noise | §1.1 | **true N-line, one verb wide** |
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

Seventeen mechanisms: three true N-lines (two clocks that close things, and a report one verb depends
on), one narrowed, one untested, and twelve that are free, cut already, or inert at shipped values.

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
producing Site reaches 0 at season 100, and the stores then feed the cohorts for some 400 seasons more.
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
the ring means after seasons 0, 1 and 2 are 725, 542, 405 (ring 0) and 748, 559, 417 (ring 1), **equal
to arm (c) to the unit**. Twenty-four `condition.band_crossed` Events were emitted and witnessed;
`restore` was attempted 0 times, `work` 0 times; nobody died; the story bar reads 23.0% against the
shipped realm's 23.4%; the executed-verb distance from the realm with no Calamity is **24**, against a
noise of 316 (§1.1). The realm does not notice that it is collapsing. The cause is stated in the verb
table's own `restore` row ("no question the realm delivers carries a Site among its referents"); this
arm is the first run in which crossings actually occurred and the absence could be seen.

| # | link | O | C observed | verdict |
|---|---|---|---|---|
| 1 | it has a beginning | a cause in the world | none exists; one must be planted by hand (H-236) | INERT |
| 2 | it builds | gathers, unevenly | a ring a season, geometric: one ruined cottage takes the realm's yield from 4,810 to 719 in 14 seasons | FOLLOWS (PROXY) |
| 3 | it can be seen coming | signs, argument | 112 `condition.band_crossed` in 14 seasons, each "a witnessable Event; produce no outcome" | FOLLOWS at FORMS |
| 4 | it breaks | a moment | none: no death, no body falls (every cohort still at 940: §2.1's glut carries them), no Event marks a rupture, `endings_reached` is `[]`; the decay has no floor but zero and no reversal | INERT |
| 5 | people can bound it | at a cost, uncertainly | `restore` is the bound the docstring names: an ungraded, costless, certain rise (`effects_economy.py:181-211`), attempted **0 times** in three seasons in every shipped arm here and at three seeds of GAME's X1 | INERT in computed play |
| 6 | what people did changes it | yes | (d): the played and the unplayed realm decay identically | INERT |

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
| executed `move` + `migrate` | 37 | 44 | 41 |
| to where the mover already stands | 20 | 30 | 36 |
| to another territory | 14 | 10 | 5 |
| individuals who travelled, and of them harmed (a body fall or death, any cause) | 10, **0** | 12, **0** | 11, **0** |
| individuals who never travelled, harmed | 36, 0 | 34, 0 | 35, 1 (killed in a `capture`) |
| most journeys by one person in one season | 3 | 3 | 1 |
| refused (`travel.blocked`, `migrate.refused`) | 77, 80 | 57, 35 | 55, 54 |

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

| three seasons, shipped | seed 0 | seed 1 |
|---|---|---|
| non-`contain` edges open at the end | 1,138 (`hold` 766, `commit` 243, `reside` 83, `oblige` 46) | 1,160 (819, 226, 82, 33) |
| edges that closed | 19 | 14 |
| … closed by their own subject | 19: 16 `reside` (a migrant's own), 2 `release`, 1 `give` | 14: 5 `reside`, 5 `release`, 4 `give` |
| … closed by a clock | 0 (the first `oblige` term matures at season 4) | 0 |
| … **closed by another person's act** | **0** | **0** |
| deaths caused by an act | 0 | 1 (`capture`) |
| interior movement logged (`pursuit.moved`) | 2 | 0 |

The stock-report arm reads the same (4 closed, all by their own subject; one killing). So in three
seasons, at two seeds and three arms, **nothing one person opened was closed by anyone else**: no grant revoked (`revoke` 0 of 6), no prisoner freed, no pledge released by the one it
was made to, no seat taken (`seize` 0 of 14, `confer` 0). The single way one person ends something of
another's is to kill him, once in six seed-seasons. Limits of the reading, stated: it reads Tenures only
(a rebutted claim or a destroyed Record is not a Tenure); a dead man's edges are removed with him and are
counted under his death; `reside` closures carry no receipt of their own, so their closer is read from
the verb that executes them (`migrate`, the migrant's own).

| # | link | O | C observed | verdict |
|---|---|---|---|---|
| 1 | a beginning | a want or a wrong | plentiful: 616 acts with another person's Event among their causes (seed 0); the deepest executed chain is five acts | FOLLOWS |
| 2 | escalation | a second party raises it | WR F-WR-01: `challenge` 0 of 118, `covenant` 0 of 18 | cited |
| 3 | a turn | reversal by another | 0 of 33 closures in two seeds; one killing | **INERT** |
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
| `thread_read` attempted / executed | 3 / 3 | 8 / 8 | 2 / 2 | 4 / 4 |
| what it was pointed at | 1 person, 2 Records | 2 persons, 5 Records, 1 other | 1 person, 1 Record | 3 persons, 1 Record |
| degree | none | none | none | none |
| what the finding observed | the reader's own sensitivity and the gate (`thread_sensitivity` 75, `.gate` 30) and nothing else | same | same | same |
| the reader's body, before → after | 1000 → 1000 | | | |
| claims in the reader's ledger that name the Thread | 0 of 308 | | | |
| `restore` / `work` attempted | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |

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

Severity words are the suite's. "Touches" names the nine requirements (`dossiers/00_NINE.md`). Each
falsifier is a run that would have shown the claim wrong, with its outcome and its control.

### F-PES-WR-01 · blocks a requirement · no story in computed play has a turn

**Claim.** Nothing one person opens is ever closed by another person's act; the only reversal the realm
performs is a killing.
**Evidence.** §2.4's table: 33 closures at two seeds, 33 by the edge's own subject, 0 by another, against
2,298 edges left open; `revoke` 0 of 6, `seize` 0 of 14, `release` 2 of 17 (both the releaser's own).
**Falsifier run and control.** An edge closed by an act whose actor is not its subject, in any arm:
none in `p2_s0_k3_shipped_b`, `p2_s1_k3_shipped_b`, `p2_s0_k3_stock0`. Control: the reading does see
closures (the 33) and does see an act-caused death (seed 1), so the zero is observed, not unread.
**Touches.** R-02 (consequence), R-06, R-05; NERS-R's no-player half.
**Consequence.** A chain of answers with no reversal is a correspondence, which is what the chronicle
prints. Escalation and ending are the WR lane's F-WR-01; this is the middle, and it was unmeasured.
**Minimal fix at the owner.** The closing verbs are other lanes' (FA `revoke`, `seize`; SC `pardon`,
`determine`; PC the duel). What WR owns is the reading, so the gap is a number:
`16_PESSIMIST_WR_D_small_clock_repairs_and_two_readings.md` edit 4.

### F-PES-WR-02 · degrades narrative · the Calamity has no source, no break and no answer, and the scheduled flip starts an exponential nobody stops

**Claim.** §2.2. At shipped values there is no calamity; switched on it is a uniform ramp; with a source
it builds as documented and never breaks; the played realm decays exactly as the unplayed one.
**Evidence.** `p1_s0_k60_lattice.txt`, `p3_s0_k14_c250.txt`, `p2_s0_k3_calamity.txt`; `matter.py:139-201`.
**Falsifier run and control.** A played season in which a ring mean differs from the unplayed arm's, or
a `restore` is attempted: none in three seasons (ring means equal to the unit; `restore` 0, `work` 0).
Control: the played arm does differ from the shipped realm in 13 state components, `sites` among them,
so the comparison can see a difference when there is one.
**Touches.** R-01, R-02, R-09 (the pull is exact; WR F-WR-24); NERS-R completeness (no end state).
**Consequence.** `09_WR_world_motion.md` edit 1's second commit (weight 0 → 250 with a wound) would take
the realm's yield from 4,810 to 719 in fourteen seasons at every seed with no Event to mark it.
**Minimal fix.** `16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md`.

### F-PES-WR-11 · degrades narrative · the band-crossing channel is dead from end to end

**Claim.** A band crossing is emitted "so somebody's later act can be its consequence" (L5,
`matter.py:103-104`), and no act can be.
**Evidence.** The calamity arm is the first run in the suite in which crossings occur inside a played
horizon: 24 `condition.band_crossed`, witnessed, and `restore` 0 attempted, `work` 0 attempted. The
`restore` row's own note gives the cause ("no question the realm delivers carries a Site among its
referents"); `rosters.yaml:1903-1906` says the opposite ("`restore` now executes on the populated
realm's SETTLEMENT fabrics"). The run agrees with the verb table; the roster note is stale.
**Falsifier.** A `restore` or `work` attempt in the calamity arm. None.
**Touches.** R-01 (propagation), R-02.
**Minimal fix.** Proposal B edit 4 (the occasion), at CORE's owner; the stale roster sentence is §9 R-4.

### F-PES-WR-03 · degrades narrative · the world's own change is one ramp in 37 places (cross-listed)

§2.1. SE F-SE-01 and GAME F-PES-GAME-05 own the defect and its fixes (`07_SE_ground_and_granaries.md`,
`16_PESSIMIST_GAME_the_world_draws.md`); this lane adds the premise verdict and nothing to build.
**Falsifier.** Two settlements differing in any MATTER-written quantity after 41 unplayed seasons. None.
**Touches.** R-01, R-09.

### F-PES-WR-05 · degrades narrative · the Thread is read off letters, finds nothing and costs nothing

**Claim.** §2.5. **Evidence.** Four arms: 17 executed `thread_read`, subjects 9 Records, 7 persons, 1
other, 0 places; every finding ungraded with the reader's own gate as its only observation; body
unchanged; `rosters.yaml:3295-3296`. **Falsifier.** A `thread_read` whose finding observes anything but
the gate, or whose subject is a Site: none. Control: an `examine` finding in the same world was looked
for and none executed in these arms (`examine` attempted 0), so the comparison with a sibling inquiry is
by the roster's statement, not by run `[UNVERIFIED by run]`.
**Touches.** R-05; the setting's premise. **Minimal fix.** Proposal D edit 2; the build is the WR lane's
two threadwork proposals.

### F-PES-WR-06 · degrades narrative · a journey is free, instant and certain

**Claim.** §2.3. **Falsifier.** A traveller harmed, or arriving later than the round he set out: none of
33 individuals at three arms. Control: non-travellers (105 person-arms) are unharmed too, bar one
killing. **Touches.** R-09, R-05. **Minimal fix.** `16_PESSIMIST_WR_A_the_road_is_drawn.md` (the shape
of CP-T10-02).

### F-PES-WR-07 · degrades narrative (R-09) · the bodies clock is a coin, the same coin for everyone

**Claim.** The one draw the world owns for persons is binary, irrecoverable, off the ladder, and no
state sets its odds; every individual is the same age.
**Evidence.** `matter.py:726-731`; `world_q.py:1262-1270`; `build_realm(0)`: all 46 individuals
`born == 0` (`fixtures.py:692`). **Falsifier.** Two individuals with different hazards at one tick:
none can exist (one formula, one age). **Correction owed to a sibling:**
`09_WR_B_draws_not_thresholds.md` lists illness as complying with the standing rule; it meets "a draw"
and misses "graded", "recoverable" and "state sets the odds". Listed for that lane.
**Touches.** R-09, R-06. **Minimal fix.** `16_PESSIMIST_WR_C_illness_on_the_body_ladder.md` (ships dark).

### F-PES-WR-04 · degrades narrative · CALENDAR can be removed and no reading notices

§1.1. **Falsifier.** A cut arm further from shipped than the noise: 38 against 316. Control: the cut
does remove its own Events (12 and 17 to 0), so the arm is the arm. **Touches.** R-03, R-04.
**Minimal fix.** None to the barrier; proposal D edits 3 and 5.

### F-PES-WR-08 · degrades narrative · every run is the same run, and one layer comes and goes with the draw

§3.3. **Falsifier.** Two draws of one realm differing in a death, a seat, a determination or a Site:
none. **Control.** They do differ (316 acts), in paper. **Touches.** R-09 in its honest sense (variety
of outcome, not of bookkeeping); R-02. **Minimal fix.** None here: it is the sum of F-WR-01 and
F-PES-WR-01. The `oblige` observation is listed for FA and for the churn lane.

### F-PES-WR-10 · hygiene · "pressure" never fires

`_standing_crossings` (`matter.py:211-264`) emitted `standing.band_crossed` 0 times in three seasons in
six full-realm arms at two seeds. **Falsifier.** One such Event: none. The cause was not traced `[UNVERIFIED]`;
listed for SC (SC-02 step 23 is its owner).

### F-PES-WR-09 · hygiene · a Date due in the past never fires

§3.5; P4. `calendar.py:48` uses the `==` MATTER replaced with `<=` twice. Not reached by computed play
(`convene` always schedules the next tick). **Minimal fix.** Proposal D edit 1.

## 5. False N-lines found

1. **CALENDAR** (§1.1): free to cut at shipped values; true only once `determine` executes.
2. **Site wear**, inside any played horizon (§1.2).
3. **The travel-leg budget penalty** as a price (§1.2; by reading and §2.3, the `leg0` arm not run).
4. **`thread_read`** (§2.5).
5. **The standing-gap crossing** (F-PES-WR-10).
6. **The flow stamp, the era, endings** (cited: H-274, NARR, WR F-WR-06).

And one N-line found **true where the aggregate said false**: the stock report (migration depends on
it). And one found true for a bad reason: term maturation is necessary because it is the only thing
that closes anything.

## 6. Premises, summary

| premise | verdict | first link that fails | finding |
|---|---|---|---|
| the world changes whether or not anyone acts | does not hold at shipped values | 1 (there is no year) | F-PES-WR-03 |
| a calamity builds and breaks | does not hold; "builds" holds only from a planted source | 1 (no beginning); 4 (never breaks) | F-PES-WR-02, -11 |
| a journey is dangerous | does not hold | 2 (takes no time) | F-PES-WR-06 |
| a story has a beginning, a turn and an end | holds to link 1, then breaks | 3 (no turn) | F-PES-WR-01 |
| the Thread can be read and mended at a cost | holds to link 2 (the gate), then breaks | 3 (read off letters) | F-PES-WR-05 |

## 7. Stories that can happen, and that cannot

**Can, and do, in computed play:** a term runs out by itself (in the runs where the obligation layer
forms); a sitting is convened and sits empty; a person changes address; a practitioner reads a letter;
a matter is petitioned and waits; one person in six seed-seasons is killed in a capture; a chain of five
or six people write, speak and record in answer to one another.

**Can, but only from a hand-set state:** the Calamity's front (a planted source); a natural death and
the vacancy after it (a test arm's rate); a hungry town after season 0 (a planted famine, GAME X3).

**Cannot, as built:** a place decays and is repaired; a bad year; a journey that goes wrong; a reading
of the Thread that tells anything; a mending that costs; a calamity that breaks; an illness that is
survived; a grant, a pledge or a custody reversed by someone other than its holder; a realm that ends.

## 8. The standing rule, checked against this lane's text and its subject

*Subject.* MATTER takes no draw at shipped fixtures; CALENDAR and ENCOUNTER decide nothing of their own.
The two draws the world owns ship off, and one of them is not the kind the rule describes
(F-PES-WR-07). The lattice pull, the wear, the leg's end, the lapse and the maturing of terms are exact
(WR F-WR-24, cited; a term maturing is bookkeeping and is not a finding).
*This lane's proposals.* A: the road resolves on the ladder; the price is bookkeeping. B: the break is
drawn; the pull's source rule is eligibility (what can pull), not an outcome; `restore`'s decline at a
broken Site is eligibility. C: graded on the ladder; exposure is a keyed chance, as now. D: edit 1 is a
clock's tick; edit 2 is eligibility; the rest are readings. No proposal here makes a consequential
outcome a fixed function of state.
*Listed for other lanes.* `09_WR_B_draws_not_thresholds.md` (illness is not yet "graded, recoverable");
`09_WR_world_motion.md` edit 1 (the flip is a fixed-function collapse until proposal B's edits 1 and 2).

## 9. Resolutions decided, proposals, and what is left for Jordan

| id | inconsistency, gap or unclear passage | decided resolution | ladder step | carried by |
|---|---|---|---|---|
| R-1 | CALENDAR is free to cut | keep; record the N-line as resting on `determine`; give the instrument a cut arm | 5 | proposal D edits 3, 5 |
| R-2 | the lattice pulls toward any weaker Site, so anything starts the Calamity | pull only toward a broken Site | 5 | proposal B edit 1 |
| R-3 | the Calamity has no break and no bound that is used | a drawn break; mending by the working only; the crossing carries its Site | 4, 5; the standing rule | proposal B edits 2 to 4 |
| R-4 | `rosters.yaml:1903-1906` says `restore` executes on the realm; `verb_table.yaml`'s `restore` row says attempted 0/0/0; six full-realm arms and two small realms here say 0 | the verb table is right; the roster sentence is corrected to "formed nowhere since REM-22" | 1 (REM-22 superseded it) | text for the orchestrator: strike the "CORRECTED (`24f`…)" sentence's claim of execution |
| R-5 | H-140: is a same-place move travel | declines (SE R-SE-09, cited); the road draw skips a journey of zero borders | 4 | SE's proposal; proposal A |
| R-6 | CP-T10-02 (exposure) has no decided shape | one draw on the ladder at the leg's end, four graded arrivals | 4; the standing rule | proposal A |
| R-7 | illness is a draw but not a graded one | a fall of the body by degree; death at zero | 4 | proposal C |
| R-8 | `age_at_build` 0 for everyone | authored per cast row where an age exists; the default stays | 5 | proposal C edit 4 |
| R-9 | CALENDAR's `==` against MATTER's two `<=` | `<=`, once | 4 (CR-55) | proposal D edit 1 |
| R-10 | `thread_read` forms on Records and persons | `referent_class: Site` | 4 (REM-22) | proposal D edit 2 |
| R-11 | no instrument reads a reversal | `storybar.turns` | 5 | proposal D edit 4 |
| R-12 | an arm comparison cannot be told from noise | print the draw-seed distance beside it | 5 | proposal D edit 5 |

Twelve resolutions. **Nothing survives the ladder to Jordan from this lane.** Two items touch rulings
and are stated so they are not mistaken for re-raising them: natural death stays deferred (ED-IN-0317;
proposal C changes a dark mechanism's shape and switches nothing on); the same-doer strand link stays
the WR audit's §11 item 1.

Proposals written (four): `proposals/16_PESSIMIST_WR_A_the_road_is_drawn.md`,
`16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md`, `16_PESSIMIST_WR_C_illness_on_the_body_ladder.md`,
`16_PESSIMIST_WR_D_small_clock_repairs_and_two_readings.md`.

## 12. Evidence log

All under `runs/PES_WR/` in the scratchpad; `PYTHONHASHSEED=0`; three seasons unless stated; the full
realm is `build_realm(seed)`, 83 persons.

| id | command | seed · seasons | outcome |
|---|---|---|---|
| P1-a | `p1_null_long.py 0 125 0 shipped` (stopped at season 41) | 0 · 41 | §2.1's table; first crossing season 20 (37), second season 30 (37); 9,905 Events a season at steady state |
| P1-b | `p1_null_long.py 0 60 0 lattice` (stopped at 26) | 0 · 26 | wear-0 kinds follow 40 behind; yield and stores equal P1-a |
| P1-c | `p1_null_long.py 3 8 0 shipped`; `… 0 40 0 weather` | — | **not run** (load; the second was killed with its launcher) |
| P3 | `p3_calamity.py 0 14 250` | 0 · 14 | §2.2(c); 112 crossings; no death |
| P2-a | `p2_play.py 0 3 shipped` (twice) | 0 · 3 | hash `52ff67bc…` both times; 2,630 acts, 1,190 executed; reproduces WR E-07 |
| P2-b | `p2_play.py 0 3 drawseed` | 0 · 3 | 1,346 executed; L1 316; `oblige` 0 attempted |
| P2-c | `p2_play.py 0 3 calendar` | 0 · 3 | L1 38; `date.fired` 0, `docket.formed` 0 |
| P2-d | `p2_play.py 0 3 calamity` | 0 · 3 | L1 24; rings equal P3; `restore` 0; 24 crossings |
| P2-e | `p2_play.py 0 3 stock0` | 0 · 3 | L1 161; `migrate` 0 of 101; one death (`capture`) |
| P2-f | `p2_play.py 1 3 shipped` (twice) | 1 · 3 | hash `26d2091b…`; 2,646 acts, 1,290 executed; one death; one `matter.determined` |
| P2-g | `p2_play.py 0 3 shipped 0` and `… 1` | 0 · 3 | cohort-only and one-person realms: cross share 0.0%, depth 1, 0 strands |
| P2-h | arms `decay0`, `wear0`, `leg0`, `stamp0` | — | **not run** (load); §1.2 says so at each row |
| P4 | `p4_small.py` | 0 · 4 | both endings not held at build; King under `fac_valorsmark`; 16 of 18 territories held, five factions; the past-due Date never fires |
| P5 | inline: `born`, `thread_sensitivity` at build | 0 · 0 | 46 individuals `born == 0`; sensitivities 0, 0, 0, 15, 25, 28, 35, 50, 60, 75; gate 30 |

`git status --short` at the end: this lane's files are the audit and the four proposals named in §9.
No tracked file was written; no `pytest` was run.
