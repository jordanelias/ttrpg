# WR — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

Lane: world, threadwork, clocks, travel, survival, strife flows, narrative engine. Every reading below is a
dated reading of the command in §12 (seed and season count stated with it, `PYTHONHASHSEED=0`). Design
documents are cited for intent and vocabulary only (CLAUDE.md §0.05); `.designs/` is not cited as authority.

## 0. Verdict

VERDICT_PLACEHOLDER

## 1. What it is, as coded

**The lane has no module of its own.** Unlike combat, mass battle, social contest, settlements and fieldwork,
nothing under `modules/` is "world", "threadwork" or "narrative". WR as coded is four things inside
`engine/season/`, plus an unplugged oracle:

| piece | file | what it is | reached by the loop? |
|---|---|---|---|
| CALENDAR, barrier 1 | `engine/season/loop/calendar.py` (109 lines) | fires a `Date` whose `due_at == w.tick` (`date.fired`), forms an empty docket slot per held date (`docket.formed`), re-slots waiting person-matters (CR-56). Decides nothing | yes: `loop/driver.py::season`, once per season, before MATTER |
| MATTER, barrier 2 | `engine/season/loop/matter.py` (903 lines) | the licensed clocks: record-stage maturation, `Tenure.term` maturation, docket lapse, claim-confidence decay, standing-band crossing, the larder draw (`settlements.subsist`), the body fall and death at zero, the bodies clock (age, illness), yield (`settlements.produce`), travel-leg end, site wear plus the lattice coupling, band crossings | yes: once per season, after CALENDAR |
| ENCOUNTER, step 7 | `engine/season/loop/encounter.py` (84 lines) | fights the contests RESOLVE declared and deferred (`Declared` degree), in `_canonical_order`; the one step a playable host may suspend at | yes: once per round, after RESOLVE |
| the world-first Queries | `engine/season/queries/world_q.py` (5,556 lines, 251 top-level definitions) | every resolver-side read: containment, docket, works, bench, reception/proofs, place, reach, larder projections, housing, hunger, polity (`members`, `leaders`, `provinces_of`, `uncontrolled`), `endings_reached`, ambitions and stages, the standing-occasion stampers, `questions_for`, `occasioned_by`, `WorldReader`, and the strife readings (`flows_in`, `flows_known`, `flow_stakes`) | yes: `questions_for` at every DELIBERATE round; the rest by their callers |
| the narrative instruments | `engine/season/harness/storybar.py`, `chronicle.py`, `arc.py`, `strife.py`, `strife_data.py`, `strife_moves.yaml` | observers over a finished log: cross-person antecedent share and chain depth; the deepest consequence chain rendered; the thrust-arc reader with two nulls; the strife-move reach table and the strand reading | **no**. None is imported by `loop/`. One strife reading has a loop consumer: `world_q.flow_stakes`, stamped by `questions_for` when `Fixtures stamp_flow_stakes` is on (shipped on) |
| `ENDINGS_CLASSIFIED.yaml` | `engine/season/ENDINGS_CLASSIFIED.yaml` (224 lines) | a blind agent classification of 50 arc `ends_when` strings into DECIDER / ROLL / THRESHOLD / NEVER / UNCLEAR. Its own header: "AN AGENT CLASSIFICATION OF PROSE, NOT AN EXECUTION" | no code reads it for a game fact (§4.2) |
| the threadwork and overview oracles | `systems/threadwork/sim/*.py` (1,950 lines), `systems/overview/sim/ms_track.py` (92 lines) | the pre-season-loop thread operations (Leap, Weave, Pull, Lock, Dissolve, Mend), coherence, co-movement, the Mending Stability track | **no**. The season loop reaches none of it; `thread_read` is the one thread verb the loop resolves (through fieldwork) |

**State the lane owns** (by write-matrix cell, written only at the barrier named): `Date.fired`, the
`DocketItem` (CALENDAR; MATTER lapses it); `Record.matured`, `Tenure.until` on a matured term,
`Claim.confidence`, `Person.body` and `Person.exists` (hunger, age, illness), `Rung.stores`, `Rung.yield`,
`Person.travel_leg`, `Site.condition` (MATTER). Nothing in `world_q.py` or the harness owns state; every
Query recomputes (T-a).

**How the season reaches it** (`loop/driver.py::season`, read at `:388-563`): `calendar` then `matter` once;
then `scene_budget` rounds (shipped 5) of `deliberate → resolve → encounter → witness`; MATTER's and
CALENDAR's Events join round 0's WITNESS fan-out only; `w.tick` advances once; `world_q.endings_reached(w)`
is read once at the end of the season and returned in the season summary. The run does not halt on an
ending.

Execution evidence is in §12; the readings that carry the findings are quoted where they are used.

**What a season of the shipped realm does with nobody playing** (`build_realm(0)`, three seasons, shipped
fixtures, `wr_probe.py 0 3`, §12 E-07): 83 persons; 2,630 acts attempted, 1,190 executed, 1,440 refused
(54.8%); 74,510 Events, of which `claim.deposited` 35,115 and `claim.decayed` 34,837 (93.9% together);
zero `person.died`; `endings == []` at every season. The acts that executed most: `create_record` 350,
`reconstruct` 115, `commit` 95, `forge` 52, `oblige` 42, `conceal` 34, `issue` 29, `petition` 28. The acts
that never executed: `challenge` 0 of 118, `exchange` 0 of 79, `comply` 0 of 47, `accept` 0 of 45,
`raze` 0 of 22, `covenant` 0 of 18, `capture` 0 of 14, `determine` 0 of 3, `train` 0 of 119.

## 2. Steelman

Ranked by the weight each bears.

**S1. The causal substrate is real, and it is the right one.** Every Event carries `causes[]`; an act formed
from a `claim_landed` question cites the Event the claim is about (`world_q.occasioned_by`, `:4286-4356`);
MATTER's clocks chain to their own previous tick and a matured term cites the act that wound it
(`matter.py:428-435`). So "what led to this" is a walk over recorded facts and never a rationalisation
written afterwards, which is gate B2 of the read literature (§7). *Attack:* sever the edge and see whether
the reading notices. *Outcome:* it does. The edge-count-preserving null (§12 E-10) puts executed chains
well above chance: at seed 0, two seasons, 36 executed acts sit at cross-person depth 3 or more against a
null mean of 10.8 (range 6 to 15); at seed 1, 27 against 9.0 (5 to 14). **Holds.**

**S2. Seasons tick scene by scene (R-03).** The season is `scene_budget` rounds with WITNESS inside each, so
a deposit in round 1 raises a question in round 2 (`driver.py:486-507`; `questions_for`'s `since`).
*Attack:* the one-round arm must show no same-season answer. *Outcome:* at `scene_budget = 1`, seed 0, three
seasons, same-season cross-person edges are 0 in every season and every cross edge crosses a season
boundary (51, 68); at the shipped 5 they are 128, 160, 158, of which 104 are between executed acts (§12
E-06, E-07). **Holds, and is the strongest single result in the lane.**

**S3. Nothing is triggered.** No clock produces an outcome (L5), no flow fires a move, an ending is a Query
the season reports and never an actor (`world_q.endings_reached`; `rosters.yaml: endings`), and the strife
reading stores nothing (T-a, ED-IN-0225). This is the convergent precedent finding "generate on demand,
never on a clock; a threshold may change options, never act" (§7, T-WR-2), and it removes the Tale-Spin
failure shape at the root. *Attack:* find a MATTER write that decides. *Outcome:* none found; the two
hand-built Events (`_crossings`, `_standing_crossings`) carry no `changes`. **Holds.** Its cost is F-WR-01
and F-WR-04: a world that only ever responds needs something to respond to.

**S4. The licensed clocks are complete as machinery.** Wear, claim decay, the larder draw and body fall,
term maturation, travel-leg end, docket lapse and the bodies clock are each one gate write with a declared
kind and a control arm at which the season is byte-identical. *Attack:* is any of them inert at shipped
values? *Outcome:* three are (§3 F-WR-04). The machinery holds; the shipped world does not use it.

**S5. The strife design asks the right question of history.** Forty move codes and sixteen links read off
102 historical cases, with a static route check that names which openings can reach which endings, is a
falsifiable reachability target that no surveyed game states for itself (§7). *Attack:* run it. *Outcome:*
the route check reads 13 of 312 pairs routeless, all on DN (natural death, deferred by ruling); but every
one of the study's 16 drawn links reads 0 observed on the shipped realm at seeds 0 and 1 (§12 E-07, E-09),
and the conclusion test does not discriminate (F-WR-02). **The target holds; the reading of it does not.**

**S6. The instruments are honest about what they are.** `storybar` "grades nothing"; `chronicle` says
"answers" means "had among its causes"; `arc.py` ships two nulls; `strife.py` separates route from observed
and refuses to guess a side. *Attack:* does that honesty leave any instrument that can report failure?
*Outcome:* no (F-WR-03). **Holds as honesty; fails as a measure.**

## 3. Adversarial findings

Ranked worst first. "Runs" are §12 entries.

### F-WR-01 · blocks a requirement · no story in the shipped realm escalates or ends

**Claim.** With no player, the realm generates linked civic paperwork and no arc with an escalation or an
ending. The verbs that carry escalation and closure form and are refused every time.

**Evidence.** Seed 0, three seasons, shipped fixtures (E-07): `endings == []` at seasons 0, 1 and 2; zero
`person.died`; executed over attempted: `challenge` 0/118, `accept` 0/45, `capture` 0/14, `comply` 0/47,
`covenant` 0/18, `determine` 0/3, `exchange` 0/79, `raze` 0/22, `train` 0/119; one `field.lost` and six
`field.unopposed` from 29 declared marches. Consequence acts (an act whose own Event wrote an `ARC_SELF` or
`ARC_WORLD` cell, `arc.py:289`): 670, whose kinds at two seasons are `record.created` 231, `commitment.made`
65, `record.forged` 31, `duty.taken` 26, `cover.assumed` 23, `petition.filed` 20, `dispensation.issued` 19
and nothing else above 12 (E-10). The deepest consequence chain the chronicle renders is, at two and at
three seasons, `conceal → create_record → create_record → create_record` (E-01, E-07). Seed 1 at two
seasons has the same shape (`record.created` 252 of 440 consequence acts, E-10).

**Falsifier run.** A seed in which an executed `determine`, `covenant`, `fight`/`accept` death or reached
ending appears at shipped fixtures. Seeds 0 and 1 at three seasons: none. [Six-season readings: §12 E-08.]
With the forcing arm on (illness 0.05) one `matter.determined` appears at each of seeds 0 and 1 (E-11):
the route exists and needs an occasion.

**Touches.** R-05 (verbs built out), R-02, R-06; NERS-R's no-player half.

**Consequence.** Openings accumulate and nothing closes them. A realm that only opens matters reads as
noise: by season 2 one strand holds 63 moves by 17 doers (F-WR-02).

**Minimal fix at the owner.** The refusals are other lanes' (PC: `challenge`/`accept`; SC: `determine`,
`covenant`; SE: `exchange`; CHAR: `train`). What WR owns: make the reachability check dynamic so the gap is
a reading, not an inference. `harness/strife.py::opening_routes` is "STATIC, AND ONLY THAT" (`:170-181`);
add the executed count per terminal verb beside each route so a route whose every terminal verb executed 0
times prints as `ROUTE, NEVER TAKEN` (proposal `09_WR_story_instruments_that_can_fail.md`, edit 4).

### F-WR-02 · degrades narrative · a strand's conclusion does not discriminate, and strands collapse into one

**Claim.** `world_q.concluded` cannot tell a story that ended from one that paused, and the linking rule
merges the realm's strife into a single strand as the log grows.

**Evidence.** (a) 24 of 40 codes are terminal (`strife.terminal_codes`), and they include the kinds a strand
opens on: `march.declared` is an opener for sides R and O (`world_q.py:5207`) and its sided codes FR, WN and
OW are all terminal (`strife_moves.yaml:74,84,91`), so a strand whose latest move is a declared march is
"concluded". Seed 0, two seasons (E-05): strand `7ebe96bc03`, 15 moves, 13 of them terminal, 11 of them
openers, by 2 doers, reads `concluded`; its code sequence is `WN-WN-WN-SB/SZ-FR-…-WN-WN`. Forcing arm, seed
0 (E-11): strand `30d01a0ca6`, 8 moves, 8 terminal, all `march.declared`, `concluded`. (b) The open-referent
test has three arms and two are vacuous in every run: `detain 0, ban 0, at_war 0, docketed 3..5`. (c) At
three seasons the two-season "concluded" strand no longer exists: it has merged into `4ec32c3adc`, now 63
moves, 17 doers, 50 terminal moves, 34 opening moves, `concluded=False`, and `concluded 0 of 5` (E-07). The
same-doer clause of `_links` (`world_q.py:5081-5083`) joins any two deeds of one busy person. (d) At the
person reading the roster's `concludes` list (`rosters.yaml:3396-3398`) holds `petition.filed`,
`dispensation.issued`, `transfer.made`, `record.given` and `tenure.opened`, so for a person a strand
"concludes" on the kind of act that also starts one; this list is read by the loop (`flow_stakes`
→ `questions_for`, shipped on).

**Falsifier run.** A strand read `concluded` whose final move is not an opening kind and that stays
concluded a season later. None in E-05, E-07, E-11.

**Touches.** R-01, R-02 (through the stamp); NERS-E (legibility) and NERS-S (zoom: every strand reads at
the realm rung at seed 0, three seasons: `per rung kind: hearth 2, realm 2, settlement 1`).

**Consequence.** The one reading built to say "this story is over" says it of a march declaration and
un-says it a season later. A presentation layer built on it would announce and retract endings.

**Minimal fix.** Proposal `09_WR_strand_conclusion.md`: an opening move is never terminal (the rule
`flows_in` already applies to content openers, `:5212-5213`, extended to every opener); `concludes` drops
the content-opening kinds. The linking rule's same-doer clause is ratified assumption A9 with a stated
revert; narrowing it is §11 item 1.

### F-WR-03 · degrades narrative · the story bar cannot fail, has no forcing arm, and one of its controls is inverted

**Claim.** The M2 instrument does not measure story, cannot report failure, and was specified to compare
forcing on against off but has only `off`.

**Evidence.** (a) `storybar.ARMS = ("off",)` (`storybar.py:87`); the module says "No forcing source is built
yet" (`:38-39`), which is false at HEAD: `season_factor_draw` (IN-21), `age_step`/`illness_rate` (IN-34) and
`lattice_coupling` (IN-35) are built fixtures. Its CLI comparison is `off` against `off`, EQUAL by
construction; `test_storybar.py:83` asserts that equality and nothing else about the arms. (b) It "grades
nothing" (`:6-8`): there is no value of any reading at which it reports a defect. (c) Its headline counts
refusals: seed 0, three seasons, cross-person share 23.4% over all acts, 14.4% over executed acts; 355 of
616 acts at depth 2 or more are refused (E-07). (d) Run with the three forcing fixtures on (E-11, E-12), the
headline does not move in a consistent direction while the world visibly changes: seed 0 cross share 23.4%
→ 22.1%, executed share 14.4% → 13.4%, with 8 deaths, `oblige` executed 42 → 146, `confer` 0 → 1,
`determine` 0 → 1. The instrument is insensitive to the events a reader would call story. (e) CR-69's
control is inverted on real logs. `test_cr69_chains.py:99-112` asserts the shuffled-causes null reads
**below** the linked log, on a plant of six disjoint chains. On the shipped realm it reads **above**: chain
ends at depth 2 or more, real 29 against null 86 to 97 (seed 0, two seasons); real 44 against 104 to 114
(three seasons); at depth 3, real 1 and 3 against 16 to 26 and 19 to 25 (E-05, E-07). The real-seed test
(`:174-185`) asserts only `null != real`, which either direction passes. Permuting cause lists among all
Events hands each act a random Event's causes, most of which resolve to some other person's act, so the
null is denser than the log. (f) Against a null that keeps each act's number of cross antecedents and
redraws which earlier acts they are (E-10): executed chains exceed chance (S1), **consequence chains do
not**: depth 3 or more, real 2 against null mean 1.2 (range 0 to 3) at seed 0, real 0 against 1.1 (0 to 4) at
seed 1. The chronicle's default pick (CR-68) is over consequence acts, so the chain it renders is no deeper
than chance would make it.

**Falsifier run.** E-10 is the falsifier for "consequence chains carry structure"; it fails at both seeds.

**Touches.** R-01, R-02 (their measure); NERS-R ("fully formed, error-free").

**Consequence.** The project's one measure of "does the engine produce stories" would read the same for a
world of clerks filing records as for a succession war, and its companion control passes while pointing
the wrong way.

**Minimal fix.** Proposal `09_WR_story_instruments_that_can_fail.md`: forcing arms composed from the built
fixtures; the edge-count-preserving null as `storybar`'s control; a strand-shape reading (opening,
escalation by a second doer, a terminal move of a different kind) reported per seed.

### F-WR-04 · degrades narrative · the world's own motion ships off, and the world's readings of itself have no reader

**Claim.** At shipped fixtures the world does not move except by wear and memory decay, and the Queries that
read the world's condition feed no decision.

**Evidence.** `season_factor_draw=()` (`fixtures.py:535`), `age_step=0.0`, `illness_rate=0.0` (`:690-691`),
`lattice_coupling=0` (`:700`). MATTER's bodies pass is skipped (`matter.py:726`), `_lattice_strain` returns
`{}` (`:176-177`), every rung reads the bare `season_factor`. Seed 0, three seasons: `body.changed` 37, 0, 0
(F-WR-10), `person.died` 0, `condition.worn` 322 a season, no `condition.band_crossed`. Non-test callers of
the world-state Queries: `hunger`, `uncontrolled`, `closed_uses` one each, all `harness/populated.py::census`
(a report); `sovereign_fraction`, `density`, `within`, `provinces_of` none outside this file or tests;
`flows_in`, `presented` the strife harness only (grep, §12 E-14). With forcing on (illness 0.05, the weather
draw, coupling 250), seed 0: 8 deaths over three seasons, 10 `tenure.closed`, the run's only `confer` and
`determine`; seed 1: 4 deaths, 8 `tenure.closed`, one `determine` (E-11, E-12).

**Falsifier run.** A shipped-fixture run in which a death, a shortage or a band crossing occurs after season
0 with no act causing it. None at seeds 0 and 1, three seasons.

**Touches.** R-01, R-06; NERS-R's no-player half; T-WR-8 of the research lane file (§7).

**Consequence.** "The world generates drama when nobody is watching" is false at shipped values for every
drama that begins with matter or bodies. The one forcing that produced a determination in my runs (natural
death) is deferred by ruling (ED-IN-0317): §11 item 2.

**Minimal fix.** B10-18's CL-EVENTS commit (2) already flips the weather draw; the lattice needs its source
(H-236), for which proposal `09_WR_world_motion.md` gives a data-only answer; the story bar's forcing arms
(F-WR-03) supply the control each flip is owed.

### F-WR-05 · blocks a requirement · threadwork is not in the game and is not a module

**Claim.** The setting's defining practice has no executable presence in the season loop beyond one
perception verb, and its code cannot be registered as it stands.

**Evidence.** `systems/threadwork/sim/` is imported by no file under `engine/season/` or `modules/` (grep,
E-14; `loop/matter.py`'s one hit is a docstring naming `ms_track.py`). `references/module_contracts.yaml:300-319`
declares a `threadwork` contract; the `composition_roles:` block holds no `threadwork.*` role. `modules/`
holds `combat`, `fieldwork`, `mass_battle`, `settlements`, `social_contest` and nothing else.
`write_matrix.yaml:199-206`: `(Person, coherence)` is `unproduced`. The sim keeps game state at module level
(`coherence.py:142` `_practitioner_state`) and reads a duck-typed actor (`.spirit`, `.focus`, `.ts`,
`operations.py:14-18`), so it violates the registered-module contract (typed input, typed outcome, no held
state). In the realm, `thread_read` executed 3 times in two seasons at seed 0; 7 of 83 persons carry a
`thread_sensitivity` (E-13). Batch B10-15 (twelve positions) is unbuilt.

**Falsifier run.** `grep -rn "systems.threadwork" engine/season modules --include=*.py` returning a call
site; it returns none.

**Touches.** R-05; the standing requirement (playable alone, one code path); 33 case needs (§13).

**Consequence.** No arc that turns on a working, its cost to the practitioner or its cost to the world can
occur, and the Calamity has no act behind it.

**Minimal fix.** Proposal `09_WR_threadwork_module.md`: the settlements precedent (IN-07 E1 to E6), a
`modules/threadwork/` package of pure typed entries reached by a composition row, the state in
`Person.coherence`, before CP-T07-02 builds its host.

### F-WR-06 · degrades narrative · the victory ending is unreachable on one territory, and its register row is stale

**Claim.** `peninsular_sovereignty` cannot be reached, for one reason that a canon reading removes; and
H-176 states a second reason that is no longer true.

**Evidence.** `_ending_edges` selects every `territory` under a `realm` rung (`world_q.py:2681-2682`). In
`build_realm(0)`: 18 territories, 16 under the realm, 15 with a settlement beneath them, 15 held at build;
`terr_T15` is the one with no settlement, no Site and no holder (E-13). `_seize_rung` declines a place
nobody holds (`effects_information.py:1061`, H-166), so no act can ever open a hold there. GD-1's text, as
the roster quotes it, is "control all 15 territories" (`rosters.yaml: endings.peninsular_sovereignty.source`).
H-176 (`hole_register.yaml:4017`) says "NO VERB OPENS A `hold` ON ANY TERRITORY … `march_target_kinds` is
`[settlement]`"; the roster's value is `[settlement, territory]` (`rosters.yaml`, the `march_target_kinds`
row) and `_seize_rung`'s docstring says "a territory IS one since ED-IN-0306 phase 4".

**Falsifier run.** E-13 (the count); the roster line and the effect opened at the lines cited.

**Touches.** R-04, R-02; NERS-R completeness (a mechanism that cannot reach its own end state).

**Minimal fix.** `rosters.yaml: endings.peninsular_sovereignty.holds` selects settled territories (a
territory with a settlement beneath it), which is 15 and is GD-1's number; H-176's cite is corrected.
Proposal `09_WR_world_motion.md`, edit 3.

### F-WR-07 · degrades narrative · the flow stamp conditions almost nobody

**Claim.** `stamp_flow_stakes` ships on and reaches between none and eight per cent of persons.

**Evidence.** Persons for whom `flows_known` is non-empty, and for whom `flow_stakes` is: seed 0, two
seasons, 0 and 0 of 83; three seasons, 1 and 1 of 83; forcing arm, 7 and 6 of 75; seed 1 forcing, 4 and 3 of
79 (E-05, E-07, E-11, E-12). H-274's own dose reading is "6 to 13 persons are ever stamped" and "at two
seasons the arms are byte-identical on 9 of 10 seeds". The cause is in the roster: only nine kinds open a
strand at the person reading, and the realm emits almost none of them (`field.lost` 1, no `arrest.made`,
`requisition.taken`, `rung.seized`, `rung.razed`, `site.damaged`, `compliance.withheld` in E-07).

**Touches.** R-01; strife ruling R2 ("flows condition how people behave").

**Consequence.** R2 is ruled and built and has almost no effect in play, because its trigger kinds do not
occur (F-WR-01).

**Minimal fix.** None in this lane beyond F-WR-01's: the stamp is correct; its inputs are absent. Do not
widen `opens` to raise the dose (that would make civic life strife, the reason the kind list exists).

### F-WR-08 · hygiene, with one live defect · `ENDINGS_CLASSIFIED.yaml` is prose read by a builder

**Claim.** A blind agent classification of prose is an input to a world builder, through one column, and
what it builds cannot produce the ending it stands for.

**Evidence.** `corpus_run.py:656-660`: for a case whose row carries `forced_by_threshold`, `build_at` plants
a holderless Date due at tick 1 and a docket item whose matter is a Proposition id. CALENDAR fires a vacant
date and forms no slot (`calendar.py:50-67`); `slot_for` and `sittings_before` admit person-matters only
(`world_q.py:286`, `:332`), so `determine` can never clear the item and MATTER lapses it at `docket_lapse`
(`matter.py:450`). The `label` and `phrase` columns have no reader (grep, E-14). The file's own header calls
it "the weakest evidence in the suite". Its path is cited as `cases/ENDINGS_CLASSIFIED.yaml` in
`corpus_run.py:36,79` and H-176; it is at `engine/season/ENDINGS_CLASSIFIED.yaml` (`data/files.py:103`).

**Touches.** R-02 (the corpus measure); §0.05.

**Minimal fix.** Keep the file as the measurement vocabulary it says it is; stop planting from it. The
19 "forced" endings are the THRESHOLD class of §13, whose lawful form is a question raised to a person,
not a date nobody holds. Proposal `09_WR_provided_arcs.md`, edit 4.

### F-WR-09 · degrades narrative (cost) · memory decay is half the log and grows with every season

**Claim.** The claim-decay clock emits one Event per live claim per season, so the log and the season's cost
grow with the square of the season count.

**Evidence.** `matter.py:471-501`: one gate write and one `claim.decayed` per claim whose confidence moves.
Seed 0: `claim.decayed` per season 0, 12,115, 22,722; Events per season 13,379, 24,267, 36,864 (E-07). At
three seasons decay is 34,837 of 74,510 Events (46.8%).

**Touches.** R-07 (memory); standalone operability (a soak of N seasons costs O(N²)).

**Minimal fix.** Decay is a function of `(Claim.when, w.tick)`; read it instead of writing it. That is a
Layer-1 question (H-12 rules "MATTER emits an Event per write") and a declared hash mover: §6 R-14 records
the resolution and its gate; it is not proposed as an edit here because the owner of `Claim.confidence`'s
readers is the CHAR lane.

### F-WR-10 · hygiene · every cohort starves in season 0 and never again

**Evidence.** `body.changed` 37, 0, 0 and `body.tended` 37, 0, 0 at seed 0 (E-07); `matter.py:639-641`:
"the populated realm holds nothing before its first yield". The draw precedes production by design
(#353 §25), so a world built with empty larders opens on a universal famine that is an artefact of build
order. CR-22's "season-0 floor rule" (B10-18) is the scheduled answer. **Fix:** none beyond CR-22; noted so
a first-season `body.changed` count is not read as hunger binding.

### F-WR-11 · hygiene · MATTER recovery is silent (H-211, verified open)

`_crossings` fires on `before >= floor > after` only (`matter.py:119`); the body pass writes only falls
(`:690-711`). A fed cohort below a floor stays there; `tend` is the only riser (37 executed in season 0,
E-07). CP-T10-04 (B10-18) is the scheduled owner. **No change proposed.**

### F-WR-12 · hygiene · currency rows point at retired or superseded documents

`CURRENT.md:36` names `narrative_engine_design_v2_churn.md` (ED-IN-0011) as the Narrative-engine head; the
file is under `.audit/2026-07-05-emergent-narrative-engine/` and is written on the retired Key substrate.
`CURRENT.md:28` names `threadwork_v30.md` while `coherence.py` implements the model ED-WR-0010 ruled.
`module_contracts.yaml:301` carries `registry_system: "threadwork"   # Key Type Registry vocabulary`.
**Fix:** §6 R-11, R-12.

## 4. Code matters

**4.1 Ownership.** `world_q.py` is the season's whole resolver-side surface, not a WR file: of its 251
top-level definitions about forty are WR's (the strife readings, `:4747-5556`; `endings_reached`; the
weather, age and hazard reads; `enclosing_territory`, `closed_uses`). Layer 1 names it as one module
(`04` §A.2), so its size is conformant; the cost is that every lane's serialisation point is one file.
No second owner of a WR rule was found. Three single-owner moves done correctly and worth keeping:
`governors`/`side_against` moved out of the harness so `world_q` does not import it (`:4844-4878`);
`_links`/`_attach`/`_concluded` are shared by both readings (`:5068`, `:5094`, `:5158`); `requisitionable`
is asked by both the stamp and MATTER's report (`:3383`).

**4.2 Dead or unreached code.** No loop or decision caller: `sovereign_fraction`, `density`, `within`,
`provinces_of`, `slot_rank` and `presented` (harness only), `footprint` (one caller), `current_stage`'s
ladder (dormant: `goal_stages` ships `[]`). `systems/threadwork/sim/` and `systems/overview/sim/ms_track.py`
are reached by tests and one exporter only. `ENDINGS_CLASSIFIED.yaml`'s `label` and `phrase`. The five
"guard" Queries at the top of the file (`r1_aggregate`, `aggregate_guard`, `single_holder_counter`,
`commit_count_guard`, `lateral`) are called by `harness/probes.py` only.

**4.3 Seam fidelity.** MATTER reaches `settlements.subsist` and `settlements.produce` by role through
`manifest.MODULE_ENTRIES` (`matter.py:45-61`) and refuses if absent: conformant with `04` §A.2 and the
composition rows. Three graded exceedances are recorded at their sites and are accurate as written:
`lapsing_items` reads the log and act store from MATTER (`matter.py:443-447`); CALENDAR's re-slot reads
containment and RESOLVE-formed items (`calendar.py:83-89`); the two hand-built crossing Events bypass the
gate (they carry no `changes`). ENCOUNTER matches its `04` row exactly (selects `degree == Declared`,
re-admits nothing).

**4.4 Determinism.** Same seed twice: season-1 hash `bacd687f…` in E-05, E-07 and E-10 (three processes);
season-0 hash `5ab73af2…` in E-05 and E-07. The one-round arm and the forcing arm each hash differently
from the shipped arm, as they must. No nondeterminism observed.

**4.5 Test strength.** Strong: the strife loaders' refusals; `test_in27_endings` (planted-with-no-act
control, redundant-commit control, writes-nothing arm); `test_cl_thrust_b01_arc_reader`'s two nulls, which
do hold on real logs (arc reader: 21 to 23 persons against a shuffled null of 0 or 1 and an unrestricted
null of 48 to 54, E-05, E-07, E-11). Weak: `test_storybar.py:83` (two identical arms read equal);
`test_cr69_chains.py:99` (the direction of the null is asserted on a plant where it is true by
construction; the real-seed assertion is `!=`); `test_strife_execution.py` tests XE on a planted death
because a real death carries its change on `body` (H-257, verified open: `strife.py:85` reads `exists`
only). An assertion that cannot observe the failure it excludes is absent (§0.1 pt 2): the CR-69 control
is that case.

**4.6 Performance.** Season cost grows with the log: F-WR-09. `flows_known` runs for every person at every
deliberation when the stamp is on (H-274: about 5% CPU). `lapsing_items`, `practice`, `_creating_act`,
`ever_named` and `_opened_by_acts` each scan the whole log per call.

## 5. Design matters

**5.1 Where intent, ruling and code agree.** No stored flow, no arc carrier (ED-IN-0225, R15); endings as
Queries (#457 D6); the Calamity as matter wear with Mending as persons' acts (IN-35); subsistence as a
territorial matter carried by cohorts (ED-IN-0255); the foreign nations outside the realm (R16, R18). I
accept each as binding and re-raise none.

**5.2 Where they disagree, and which the game follows.**

| subject | intent or ruling | code | the game follows | cost |
|---|---|---|---|---|
| story bar | "forcing on against off" (#457 `STORY-BAR`) | `ARMS = ("off",)` | code | the instrument has no subject (F-WR-03) |
| conclusion | R6: "terminates or resolves with a concluding outcome, or it is not a flow" | 24 terminal codes, openers among them | code | conclusions announced on declarations (F-WR-02) |
| flows condition behaviour | R2 | stamp reaches ≤ 8% of persons | code | R2 built, near-inert (F-WR-07) |
| victory | GD-1: 15 territories | 16 selected, one unholdable | code | victory unreachable (F-WR-06) |
| the world substrate | arc-reachability §2: "the one hole" | lattice coupling built, weight 0, no source | code | the world is not dying (F-WR-04) |
| threadwork | ED-WR-0010: in scope | unreached oracle | code | F-WR-05 |
| narrative engine head | `CURRENT.md:36` | harness instruments | code | a stale pointer (F-WR-12) |

**5.3 NERS cuts.** Read by the definitions of CLAUDE.md §0.06; E last, as a ratio.

- *The strife reading as an instrument* survives N (cutting it loses the only reachability target the
  project has) and fails R on completeness (the conclusion test) and S on zoom (every strand at the realm
  rung). What dies under a cut of the **sixteen links and the leave-and-rejoin profile**: nothing in play;
  they read 0 observed on every run here and compare against a study whose paths are not in the
  repository. They are a second ladder for "did a story happen" beside the story bar (an S defect: two
  methodologies for one quantity). E, as a ratio: 517 lines of harness and 144 of registry for a reading
  that is all zeros; low.
- *The era* (the realm's one slot) survives N by ruling (R4, R11); as coded it is one object that is
  always `OPEN` in every run and whose `concluded` needs a realm-rung terminal move that no run produced.
  It is prose until something concludes one.
- *Capacity and presentation* (`flow_capacity`, `presented`, `slot_rank`) fail N today: no presentation
  layer reads them and the realm never has more open strands at a rung than its capacity (`presented: 3
  in 2 rungs; grouped 2`). What dies if cut: nothing executed. Ratified (A1, A2), so not proposed for
  deletion; recorded as unearned until a surface reads them.
- *The arc reader* (`arc.py`) survives: its nulls hold on real logs and it is the only reading that
  separates "wrote something on his own thrust and on the world" from bookkeeping. Its positive is thin:
  the arcs it finds at seed 0 are cohorts whose on-thrust act is one `utter` (E-05).
- *MATTER's clocks* survive every cut; they are the game's only world-first motion.

**5.4 Design that is prose and therefore not yet game.** The Calamity's source; threadwork's twelve
positions; the year (`year_length`, CP-T10-03); weather's live arm; kin, estates and marriage (CP-T10-06 to
-08); the deck (CR-80); story openings (CL-OPEN); the thrust ladder's content (`goal_stages: []`); the
clocks as folds of the log (CR-89); the regime credit term is built (CR-79) but its strand inputs are
near-empty.
