# WR — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

HEAD advanced to `6eff039` while this was written, by draft commits under this suite's directory only;
`git diff --stat 601e715 HEAD -- engine modules systems references architecture workplans registers research CURRENT.md`
is empty.

Lane: world, threadwork, clocks, travel, survival, strife flows, narrative engine. Every reading below is a
dated reading of the command in §12 (seed and season count stated with it, `PYTHONHASHSEED=0`). Design
documents are cited for intent and vocabulary only (CLAUDE.md §0.05); `.designs/` is not cited as authority.

## 0. Verdict

**No: as coded this subsystem is a sound causal substrate for an emergent narrative and not yet a source of
one.** What holds is real and measured: seasons tick scene by scene (same-season cross-person answers are
0 at one round and 128, 160, 158 at the shipped five), every Event carries its causes, about three times
as many executed acts sit at cross-person depth three or more as an edge-count-preserving null gives,
nothing is triggered, and the world's clocks are complete machinery. What does not hold is the thing asked for. With
no player, six seasons of the shipped realm at seeds 0 and 1 produce no ending, one death between them,
three `matter.determined` in eleven thousand acts, and a deepest consequence chain that is one concealment
answered by three records. Beginnings are plentiful; escalation and endings are not,
because the verbs that carry them are refused nearly every time (`challenge` 0 of 476, `accept` 0 of 186,
`covenant` 1 of 58 over the two six-season runs; seed 2 the same shape: no ending, two deaths,
`challenge` 0 of 223), the world's own motion ships at its controls, and threadwork is not in the game at
all. **The single largest obstacle is that the lane cannot tell:** the
story bar has one arm and no way to fail, its companion control points the wrong way on a real log, and
the strife reading calls a declared march a conclusion and, by season six, reads the whole realm as one
strand. The project has built the world a memory and has not yet built a way to know whether anything
happened in it. Five proposals address what this lane owns; the closing verbs are other lanes'.

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

**S6. Chains are probabilistic (R-09), as far as chains occur.** On one built world, varying only the
chooser's draw moves the verb-chain multiset (394 and 362 chains differ between draw seeds, E-02), and
every contested verb that resolves shows a spread of degrees: `argue` Failure 10, Partial 5, Success 4;
`research` 91, 26, 11; `surveil` 25, 7, 2; `tell` 6, 4, 2 (seed 0, three seasons, E-07). *Attack:* is any
multi-step chain inside one scene observed? *Outcome:* no. The only verbs that resolve are single-roll;
no duel executes (`fight`/`accept` deaths 0 in six seasons at seed 0) and one field in 29 marches is
fought. **Holds for single rolls; untested in the realm for a chain of exchanges, so `partial` stands**,
for a reason beside the one R-09's row names (H-98's fourth band).

**S7. The instruments are honest about what they are.** `storybar` "grades nothing"; `chronicle` says
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
ending appears at shipped fixtures. Seed 0, three seasons: none. Seed 1, three seasons (E-12): one
`matter.determined` (of 5 attempts), one `person.died`, one `field.lost`, no `covenant` (0/17), no
`challenge` (0/134), no `accept` (0/35), `endings == []`. So closure is not impossible; it is rare: two
closing Events in 5,276 attempted acts over the two seeds. Seed 0 at six seasons (E-08): 5,483 acts, 3,124
refused (57.0%); `endings == []` at all six; zero deaths; `challenge` 0/223, `accept` 0/102, `comply` 0/98,
`raze` 0/51, `capture` 0/32, `covenant` 0/27; `determine` 3/6 with one `matter.determined`; and the deepest
consequence chain at six seasons is still the four-act chain that closed in season 1. Seed 1 at six
seasons: 5,544 acts, 2,953 refused; `endings == []`; one death; `challenge` 0/253, `accept` 0/84, `comply`
0/99; `covenant` 1/31; `determine` 4/10 with two `matter.determined`; deepest consequence chain 3.

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
same-doer clause of `_links` (`world_q.py:5081-5083`) joins any two deeds of one busy person. At six
seasons (E-08) the reading is **one strand**: 234 moves, 55 doers, 60 parties, 154 terminal moves, 99
opening moves, `concluded 0 of 1`. (d) At the
person reading the roster's `concludes` list (`rosters.yaml:3396-3398`) holds `petition.filed`,
`dispensation.issued`, `transfer.made`, `record.given` and `tenure.opened`, so for a person a strand
"concludes" on the kind of act that also starts one; this list is read by the loop (`flow_stakes`
→ `questions_for`, shipped on).

**Falsifier run.** A strand read `concluded` whose final move is not an opening kind and that stays
concluded a season later. None in E-05, E-07, E-11. At seed 1 the strand `1886acfe0b` read `concluded`
at three seasons (3 moves, one doer, E-12) and reads open at six (13 moves, 3 doers, E-08).

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
→ 22.1%, executed share 14.4% → 13.4%, with deaths 0 → 8 and `oblige` executed 42 → 146; seed 1 cross share
22.3% → 24.4%, executed share 12.8% → 12.8%, with deaths 1 → 4. Two seeds are a direction, not a balance
claim; the direction is that the instrument does not register the events a reader would call story. (e) CR-69's
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
draw, coupling 250), seed 0: 8 deaths over three seasons against 0, `tenure.closed` 10 against 2, `oblige`
executed 146 against 42, one `confer` and one `determine` against none; seed 1: 4 deaths against 1,
`tenure.closed` 8 against 6, `determine` 1 against 1 (E-11, E-12). Deaths and the seats they empty move
with forcing at both seeds; determinations do not (the seed 1 control has one without it).

**Falsifier run.** A shipped-fixture run in which a death, a shortage or a band crossing occurs after season
0 with no act causing it. None at seed 0, three seasons. Seed 1 has one death in season 2, in the season
of its one `field.lost`; the bodies pass is skipped at shipped rates, so it cannot be an age or illness
death, and its causing act was not read `[UNVERIFIED]`.

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

### F-WR-07 · degrades narrative · the flow stamp's reach hangs on one Event kind

**Claim.** `stamp_flow_stakes` ships on and reaches between none and eleven per cent of persons at seeds 0
and 1 and 28% at seed 2; the difference is whether a field was fought.

**Evidence.** Persons for whom `flows_known` is non-empty, and for whom `flow_stakes` is: seed 0, two
seasons, 0 and 0 of 83; three seasons, 1 and 1 of 83; forcing arm, 7 and 6 of 75; seed 1 forcing, 4 and 3 of
79 (E-05, E-07, E-11, E-12); at six seasons, 5 and 5 of 83 (seed 0), 9 and 8 of 82 (seed 1) and 27 and 23
of 81 (seed 2) (E-08). Seed 2 is the seed with five `field.lost` (an `opens` kind) against one at each of
the others: an earlier draft of this finding, written before seed 2 finished, said "at most eleven per
cent", and seed 2 falsified it. H-274's own dose reading is "6 to 13 persons are ever stamped" and "at two
seasons the arms are byte-identical on 9 of 10 seeds". The cause is in the roster: only nine kinds open a
strand at the person reading, and the realm emits almost none of them (`field.lost` 1, no `arrest.made`,
`requisition.taken`, `rung.seized`, `rung.razed`, `site.damaged`, `compliance.withheld` in E-07).

**Touches.** R-01; strife ruling R2 ("flows condition how people behave").

**Consequence.** R2 is ruled and built, and whether it has any effect in a given realm is decided by
whether one of nine kinds happens to occur; where none does it conditions nobody (F-WR-01).

**Minimal fix.** None in this lane beyond F-WR-01's: the stamp is correct; its inputs are rare. Do not
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
three seasons decay is 34,837 of 74,510 Events (46.8%). At six (E-08): `claim.decayed` per season 0,
12,115, 22,722, 35,115, 48,781, 60,323; Events per season 13,379 rising to 85,591; decay is 179,056 of
273,067 Events (65.6%).

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
`provinces_of`, `footprint`, `slot_rank` and `presented` (harness only), `current_stage`'s
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
| flows condition behaviour | R2 | stamp reaches 0 to 11% of persons at two seeds, 28% at a third | code | R2 built; its reach rests on one rare kind (F-WR-07) |
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

**5.5 The NPC and AI-chooser surface of this lane** (the intent itself is the CHAR lane's to state:
`02_CHAR_audit.md`, its reconciliation of the NPC and chooser sources; not redone here).

(a) *Behaviours this lane needs.* WR decides nothing: CALENDAR "DECIDES NOTHING" (`calendar.py:35`), a
crossing "MAY NEVER PRODUCE AN OUTCOME" (`matter.py:103`), a flow "fires nothing". Every consequence of
the world's motion is somebody's act, so the lane needs five behaviours from the chooser: a governor who
answers a shortfall (`transfer`, `requisition`); a resident who mends a fabric that crossed a floor
(`restore`); a seat-holder who convenes for a waiting matter; a practitioner who works at a cost to
himself; a traveller who weighs a journey. Observed at seeds 0 and 1, three seasons: `transfer` 2 and 3
executed, `requisition` 0 and 1, `convene` 17 and 15, `restore` attempted 0 times, the practitioner's only
act `thread_read` (3 and 4), and no journey priced (CP-T10-01 ships its pricing off with "[GAP: unowned]":
no position gives a chooser a person-side reading of a leg's price).
(b) *One interface.* Yes. The lane adds no decision path: the player's callback and the shipped chooser
both receive `choose(p, v, s, ask_budget)` (`harness/play_surface.py::dispatching_chooser`), MATTER and
CALENDAR take no chooser, and ENCOUNTER's `host` is the one suspension point for both. One asymmetry
belongs to this file: `question_aggregation_rule = "first"` (`data/fixtures.py:547`) delivers `out[0]` of
`questions_for` to player and NPC alike, so neither chooses *what to attend to*. The ruled design intent
for the player is the opposite: a slate of specific events with more opportunities than scene actions,
"choosing what to attend is the gameplay" (`auto_manual_resolution_duality_v1.md` §1, ED-SC-0013; intent
only). `questions_for`'s sorted list is that slate in everything but delivery.
(c) *Hard-coded NPC rules in this lane.* One: `attention_key`'s five tiers (`world_q.py:3857-3989`) are
the same for every person; a person's pursuits order questions only *within* tiers 0 and 3. Whether a
zealot attends to a deed before his office, or a steward the reverse, is fixed by tier number and not by
who he is. The standing-occasion stampers that read the world rather than the person's ledger
(`vacancies`, `detainees_held`, `matters_awaiting`, `holdings_to_found`, `goal_referents`' `seat_holders`)
are recorded at their sites as "in tension with AX-7"; they inform rather than decide, and I add nothing
to those records.
(d) *Characterful, and legible afterwards.* A person is distinguishable here by what his ledger holds and
which tier it lands in. The reason trail is half-recorded: an act taken on a `claim_landed` question cites
the Event it answers (`occasioned_by`), but an act taken on a standing ambition cites nothing "on
purpose" (`world_q.py:4305-4308`), and the question it answered lives only in the live driver's `Scene`
(`soak._occasion_row`). At seed 0, three seasons, 690 of 2,630 acts have no antecedent of any class and
959 only the actor's own (E-07): for 63% of acts the log cannot say what another person or the world did
to occasion them, and for the 26% with none it cannot say why at all.
(e) *Missing, as proposals.* The chronicle's `why` column and the interface it needs from CORE
(`09_WR_story_instruments_that_can_fail.md` edit 5; the record itself is CORE's and CHAR's:
`01_CORE_reason_trail_in_the_act_store.md`, `02_CHAR_reason_trail_and_small_edits.md`); the mender's and the tally-holder's occasions (`09_WR_world_motion.md`,
`09_WR_provided_arcs.md` edit 1). Tier order by temperament is CHAR's (`02_CHAR_resolve_and_temper.md`);
this lane needs only that `attention_key` read it from the person.

**5.6 What the full design set adds** (read for intent; §12 lists what was read). Three things change the
weight of findings and none changes a verdict. (1) The design's frame is two simultaneous contests,
governance and survival, with "Mending Stability" as the second (`victory_v30.md`, `ms_trajectory_v1.md`,
`calamity_radiation_v30.md`): F-WR-04 is therefore not a missing feature but half the designed game. The
code's re-expression (matter wear plus a coupling, no stored scalar) follows later rulings and I accept
it; the design's radiation-by-distance survives as `radiation_bands` data and the breadth-first order
IN-35's test asserts. (2) The design's victory text names "all 15 playable territories (T1–T14, T17)",
which is exactly the settled set of E-13: F-WR-06's fix is the design's own count. (3) The design's
world-state transitions (Rupture, Occupation, Anarchy) are eras the game continues through, with one true
terminal; the code's `endings` roster has two rows and no era. That is prose, not yet game, and belongs
with CR-89 and CL-OPEN rather than with a new carrier. The 2026-08-08 world-churn audit's sentence, "the
world does not churn because the churn machinery is disconnected, not because it is scripted", was written
of the retired campaign driver; re-verified against the season loop it holds in kind (F-WR-01, F-WR-04):
the machinery is built and its inputs do not arrive.

## 6. Hole-register and workplan disposition, and resolutions

### 6.1 Disposition

Rows read in full at their register line: H-176, H-186, H-211, H-235, H-236, H-238, H-257, H-274 (and H-98
for R-09). The rest of the dossier's 56 primary rows were read at their excerpt and checked against the
code read for this audit; rows whose subject is another lane's mechanism are marked *not WR's*.

| item | listed | verified | evidence | action |
|---|---|---|---|---|
| H-04 `q`'s producer | closed? | closed | `questions_for` runs at every round (E-07: 2,630 acts formed) | none |
| H-05 world-gen roster | open? | closed by build | `build_realm` seats 83 persons, 37 cohorts | none |
| H-27 travel-leg ownership | open? | closed in code | `Person.travel_leg`; MATTER ends it (`matter.py:831-843`), `travel.ended` 24 in E-07 | re-grade at the row |
| H-32 `judging_set_rule` | open? | open, narrowed | `matter` unused, basis constant (`world_q.py:661-681`) | none (SC's) |
| H-34 establishment size | closed? | closed (moot) | field deleted; `establishment_of` | none |
| H-40 claim decay clock | closed? | closed | 179,056 `claim.decayed` (E-08) | see R-14 |
| H-51 what demands an individuation | closed? | closed | `demanded_person` | none |
| H-65 `requires:` is prose | open? | not WR's | CORE | none |
| H-95 two scale vocabularies | open? | closed in effect | `corpus_run`: 143 distinct worlds run, no unrepresentable line (E-15) | re-grade at the row |
| H-102 propagation loop | open? | open as a sign, measured as an edge | cross-person edges 363 to 1,372 (E-05, E-08) | none |
| H-103 claim decay bound | open? | closed as a bound; its cost is F-WR-09 | E-08 | R-14 |
| H-107 `Event.subject` | open? | not WR's | CORE | none |
| H-110 band crossing loses its Event | closed? | closed (dissolved) | no `band_crossed` source | none |
| H-118 `content_hash` | closed | closed | hashes reproduce (§4.4) | none |
| H-125 body step | open? | closed in effect (ships 10) | `body.changed` 37 in season 0 | see F-WR-10 |
| H-129, H-130, H-135, H-139 `World.write` | open? | not WR's | CORE | none |
| H-150 garrison strength unreachable | open? | not WR's (MB) | — | none |
| H-159 oblige term | open? | open; live | `tenure.closed` 0, 0, 2, 2, 2, 27 by season at seed 0 (E-08); that the 27 are matured `oblige` terms is inferred from `term.matured` and `duty.*` beside them, not read `[UNVERIFIED]` | FA's |
| H-164, H-167, H-168 fabric, capacity, migrate | open? | not WR's (SE) | `migrate` 36/217 executed (E-08): H-168's "0 executed" is stale | SE re-reads |
| H-172 `Claim.round` | open? | closed in effect | same-season cross edges 128, 160, 158 against 0 at one round (E-06, E-07) | re-grade at the row |
| H-176 no ending reachable | open? | open; **its second cause is stale** | F-WR-06 | R-04 |
| H-185 authored ought's predicate | open? | not WR's (CHAR) | — | none |
| H-186 insurgency beyond its first condition | open? | open | `uncontrolled` has one caller, a report | R-05 |
| H-208 bodies-clock values | closed? | built dark; deferred by ruling | fixtures 0.0 | §11 item 2 |
| H-209, H-225, H-227, H-230 | open? | not WR's (FI/CHAR/FA) | — | none |
| H-211 a body only falls | open? | open | `matter.py:119`, `:690-711` | R-13 |
| H-215, H-216, H-223 | — | not WR's (SC) | — | none |
| H-232 `pardon`, `raze` formed and refused | open? | open | `raze` 0/51, `pardon` 0/6 (E-08) | CHAR/FA |
| H-235 lattice coupling | closed? | built dark | weight 0 | R-03 |
| H-236 no source | (not in dossier) | open | E-13: no Site at T15 | R-03 |
| H-238 no corpus thread sensitivity | open? | open, answered at ladder step 1 by the row itself | `thread_read` never attempted in `corpus_run` (E-15) | none |
| H-242, H-243, H-245 to H-247 | closed? | closed as injected numbers | — | none |
| H-257 a real execution reads KL | open? | open | `strife.py:85` reads `exists` only | R-06 |
| H-274 the stamp | open? | open; dose 0 to 28% by seed | F-WR-07 | none |
| H-278, H-283, H-287, H-291, H-307, H-311, H-326, H-350, H-356 | open? | not WR's | — | none |
| B10-15 (12 positions) | open | open; precondition missing | F-WR-05 | R-08 |
| B10-18 (13 positions) | open | open | CL-EVENTS (2), CR-22, CP-T10-04 answer F-WR-04, -10, -11 | keep order |
| CL-THRUST | held | landed pieces dormant (`goal_stages: []`) | `stage_referents` returns `()` | R-10 |
| CL-OPEN, CR-80 | held | held | — | none |
| B11-F2, B11-F3 | open | open | CR-99's "positive control for the strife guard" is the same need as F-WR-03 | fold CR-99 into `09_WR_story_instruments…` edit 1 |
| WR-01 | BLK | blocked on a working with a cost in the season | F-WR-05 | follows R-08 |
| HANDOFF_WR item 2 (own-configuration Mending costs nothing) | open | open; unreached in play | oracle only | decided with B10-15 (CP-T07-04 "a price on self-repair") |

### 6.2 Inconsistencies, gaps and unclear passages: decided resolutions

Ladder steps: 1 superseded · 2 irrelevant · 3 answered by a design document · 4 by precedent · 5 by what
makes sense for the architecture. Twenty resolutions.

| id | what is inconsistent, missing or unclear | decided resolution | step | carried by |
|---|---|---|---|---|
| R-01 | Story bar specified as forcing on against off; code has one arm and says no forcing source is built | add arms composed from the built fixtures; delete the stale sentence | 3 (#457 `STORY-BAR`) | `09_WR_story_instruments_that_can_fail.md` e1 |
| R-02 | CR-69's control reads above the real log; its test asserts the opposite on a plant | replace with an edge-count-preserving null for the chain reading; keep shuffled-causes for the arc reader, where it holds | 5 | same, e2 |
| R-03 | The lattice coupling has no source (H-236), so a non-zero weight is not a Calamity | the source is an authored initial condition at T15 behind a build switch; the weight flips after H-165/H-07 | 3 (#457 D1, D-3) and 4 (`guards=`, `foreign=` switches) | `09_WR_world_motion.md` e1 |
| R-04 | Victory selects 16 territories; canon says 15; H-176 says no verb opens a territory hold | select settled territories; correct H-176's cite | 3 (GD-1) | same, e3 |
| R-05 | Who may take a place nobody holds (H-166), which leaves H-186's caller unbuildable | the occupier, by the rule `seize` already states | 4 (`_seize_rung`'s licence) | same, e2 |
| R-06 | A real execution reads KL, not XE (H-257) | half decided: `readers_for.victim_held` reads the death's `body` change as well as `exists` (one line, `strife.py:85`). The other half cannot be fixed in a harness: the `detain` edge leaves `w.tenures` with the dead man and its closure mints no Receipt (`arc.py`'s own note), so custody at the death's tick is not in a finished world. XE stays unreadable on a real log until a closed custody edge is recorded; that is a `state/` question, cross-listed to CORE | 5 | harness edit named here; the rest an interface need |
| R-07 | A strand concludes on an opening kind; the person-side `concludes` list holds content openers | an opening move is never terminal; `concludes` drops content-opening kinds | 3 (strife R6; §4 "cannot conclude on its own opening move") | `09_WR_strand_conclusion.md` e1, e2 |
| R-08 | Is the missing threadwork module a gap? | yes; move the oracle to `modules/threadwork/` as pure typed entries before CP-T07-02 builds its host | 4 (IN-07 E1 to E6; `fieldwork.find`) | `09_WR_threadwork_module.md` |
| R-09 | Threadwork's Ob tables and gates are module constants | one typed file under `engine/engine_params/`, read by the module | 3 (CLAUDE.md §0.05, §5) | same, e3 |
| R-10 | The thrust ladder is built and empty; the arc reader's positives are cohorts uttering | no code change: the ladder waits on content (B6.n); record that `read_arcs`' 21 to 33 persons are utterances and not climbs | 2 | this row |
| R-11 | `CURRENT.md:36` names a Key-substrate narrative design as the head | the row names the running instruments (`engine/season/harness/storybar.py`, `chronicle.py`, `strife.py`) and the ratified strife master by bare filename; the `.audit/` design is history | 1 (ED-IN-0232 retired its substrate) | orchestrator edit to `CURRENT.md` |
| R-12 | `CURRENT.md:28` and `module_contracts.yaml:302` name `threadwork_v30.md`, whose Part 3 ED-WR-0010 superseded | the row names the code head (`systems/threadwork/sim/`, then `modules/threadwork/`); the contract's `doc:` stays a quarantined pointer | 1 (ED-WR-0010) | orchestrator edit; `09_WR_threadwork_module.md` e2 |
| R-13 | A body only falls (H-211) | the signed step and an upward crossing for the body row, behind a fixture shipped off | 3 (r2 §A.4) | `09_WR_provided_arcs.md` e2; CP-T10-04 |
| R-14 | Claim decay is two thirds of the log by season 6 | decay is read from `(when, tick)` and not written; one Event when a claim's band of confidence changes | 5 | CORE's `01_CORE_claim_fade_as_read.md` (cited, not duplicated) |
| R-15 | `ENDINGS_CLASSIFIED.yaml` is prose planted into worlds through one column, and is mis-pathed in two cites | stop planting; correct the path | 3 (CLAUDE.md §0.05 cl. 2) | `09_WR_provided_arcs.md` e3 |
| R-16 | The provided arcs ask for automatic clocks and thresholds that fire | restate each as a person's tally, a fold of the log, or matter wearing; one new registry for the first | 3 (L3 cl. 1, L5) and 1 (CR-89 for the institutional clocks) | same, e1, e4 |
| R-17 | The sixteen links and the leave-and-rejoin profile read 0 on every run | keep as a reading; stop citing them as evidence either way until a strand has more than one kind of move in order (`PT→PT`, `WN→WN` at their shuffled control in E-07, E-08) | 2 | this row |
| R-18 | `storybar`'s headline counts refusals | the executed reading is the headline; the all-acts line stays beside it | 5 | `09_WR_story_instruments…` (gate uses `--executed-only`) |
| R-19 | `march_side` and strand links read live tenures, not the tenures at the move's tick | accept the stated limit; fix only with a log-tick read of holds, which `World` does not offer; not worth a carrier | 5 | this row |
| R-20 | The NINE's settlement note says `restore` executes in the realm; it is not attempted in three or six seasons at seed 0 | the note is stale; `restore` forms only on a Site-classed referent and none arises while no fabric crosses a floor | 1 (measured, E-07, E-08) | orchestrator edit to `requirements.yaml`'s note |

## 7. Research transfer

Research is tier 3: it informs and never settles (`research/00_INDEX.md` §1). Read: `00_INDEX.md`,
`by_lane/README.md`, `by_lane/WR_world.md` (§0, §2, §7), `emergent_narrative_literature/07_apparatus.md`
(gates A to D), and through them the summaries of the companion, EMG, THR and the precedent-nulls file.

**Used, and what each changes.**

| precedent or finding | source | what it changes here |
|---|---|---|
| "Generate on demand, never on a clock; a threshold may change options, never act" (CK3; Qud's reify-on-visit) | lane file T-WR-2; convergence of two programmes | confirms S3; and names its cost, which the same row records: political reversals "feel like weather rather than like consequence". F-WR-01 is that cost observed |
| "An emergent layer built as a single switch will be switched off, and the data behind it becomes decoration" (Guild 3, Bannerlord trait axes) | lane file T-WR-8 | this is F-WR-04 as a precedent failure shape: four world motions behind four fixtures at their controls. It argues for flipping with a measured control, not for more switches; `09_WR_world_motion.md` adds one switch and says so |
| Memory gates eligibility, not flavour (Dwarf Fortress grudges, CK hooks, the Nemesis vendetta) | EMG, lane file T-WR-5 | the private tally of `09_WR_provided_arcs.md` edit 1 is this shape; it is why a tally is a question and not a counter |
| Tracking is not expressing; a retelling needs a stage that selects, orders and frames, with a stated criterion (gate D1), and a ranking that beats random in comparison (D4) | literature apparatus | the chronicle is that stage; its criterion (deepest consequence chain) does not beat an edge-count null (F-WR-03). D4 is the test the instrument must pass, and is edit 2 |
| "Does the same target situation arise through different causal histories and casts across seeds?" (gate B4); "can the design name its target situations and report how often each occurs?" (C2) | literature apparatus | the strife registry is the only place the project names its target situations; C2 is what `ROUTE, NEVER TAKEN` reports |
| A crisis is a retroactive audit of neglected fabric (Lisbon 1755, the Zwin, the 1315 famine) | historical-concerns catalogue via lane file T-WR-1 | the one historical shape that reached code (wear crossing a floor); it supports the lattice as matter rather than as a scalar |
| The Tale-Spin effect, oatmeal, apophenia: authored predicate-triggered arcs fail as narrative | THR, lane file T-WR-3 | supports refusing an arc carrier and refusing to plant endings from `ENDINGS_CLASSIFIED` (R-15) |

**Tried, did not transfer.**

- *Storyteller directors* (RimWorld). A director is an agent that is not a person; Layer 1 has none, and
  the lane file records that the tree's own narrative design dropped it. Not proposed.
- *King of Dragon Pass advisers.* Expression without simulation; nothing for a loop with no text layer.
- *The study's sixteen links* as a target. The study's coded paths are not in the repository, the links
  are `[UNVERIFIED]` hand readings (`strife_moves.yaml:117`), and every run reads 0. They cannot be a bar.
- *The historical-concerns catalogue as an event deck.* Its triggers bind to stored scalars the plan cut;
  only its shapes transfer.

**Nulls, which are findings.** No surveyed game or source models a magic that costs the practitioner his
self (lane file T-WR-6; index §7): every threadwork number is internal, three are tagged "magnitude
invented" at their definitions, and no precedent can check them. No game certifies that generated content
is good rather than varied (N-5): the story bar cannot be given a pass mark from precedent, only a null it
must beat. No game defends a cross-scale bridge whose default state equals its absence: the flow stamp at
a dose of nil at one seed and 28% at another (F-WR-07) is that null arriving.

## 8. Best path forward

Ordered. "Alone" is what the lane needs to run well by itself; "compose" is what it needs from others.

| # | change | file | gate (execution artifact) | unblocks | cost |
|---|---|---|---|---|---|
| 1 | Give the story bar its arms, its null and a shape reading; print routes never taken | `harness/storybar.py`, `chronicle.py`, `strife.py`, `tests/test_cr69_chains.py` | the four commands of `09_WR_story_instruments_that_can_fail.md` | every later step's control; R-01, R-02 measures | edit / small build · alone |
| 2 | An opening move is never terminal; `concludes` drops content openers | `queries/world_q.py::flows_in`, `rosters.yaml: strife_kinds` | `strife 3 0 1 2 --strands`: no opener prints `concluded` | R-01, R-02 through the stamp | edit · alone |
| 3 | Victory counts settled territories; H-176 corrected | `rosters.yaml: endings`, `world_q._ending_edges` | `test_in27_endings.py` with the new plant | R-04 | edit · alone |
| 4 | CL-EVENTS commit (2): the weather draw live (already scheduled) | `data/fixtures.py` | storybar `off` against `weather` DIFFER; CR-73's SH reading | R-01, R-06 | edit · alone |
| 5 | The wound at Askeheim, switch then weight | geography data, `harness/populated.py`, `data/fixtures.py` | crossings ordered by distance from T15; `restore` executed > 0 | R-01, R-05 (`restore`) | small build · alone, then SE (H-165) |
| 6 | Threadwork as `modules/threadwork/`, typed and stateless | `modules/threadwork/`, `queries/inputs.py`, `module_contracts.yaml`, `engine_params/` | four oracle files green on unchanged numbers; import artifact clean | B10-15; R-05 | small build · alone |
| 7 | B10-15 in its card's order, on step 6 | per card | per card (`aperture 1 0`: a thread row offered and executed) | R-05, 33 case needs | design-first per position · compose (PC for CR-13, CHAR for cells) |
| 8 | A private tally raises a question | `rosters.yaml: tally_axes`, `world_q.tally_reached`, `questions_for` | the planted three-claim falsifier | R-06; seven core arc needs | small build · compose (CHAR authors axes) |
| 9 | A fed body mends, audibly | `loop/matter.py`, `modules/settlements/subsist.py` | MW-11 green with its control | H-211; R-07 | small build · compose (SE) |
| 10 | An unheld place is taken by occupation | `loop/effects_information.py::_seize_rung` | the occupied and unoccupied plants | H-166, H-186; R-04 | edit · compose (FA, MB) |
| 11 | Claim fade as a read | CORE's proposal | six-season Events per season flat | soak cost; R-07 | CORE |

**What moves the central ask most** is not in this lane: the closing verbs. Steps 1 to 5 make the world
move and make its stories measurable; they do not make a duel, a treaty or a judgment execute. Until
`challenge`/`accept`, `covenant` and `determine` execute at more than a few in five thousand acts (PC, SC,
FA lanes), the realm will open matters and not close them, whatever this lane ships.

## 9. Playable standalone and integrated

Judged against the standing requirement, point by point. The lane is four things, so four answers.

**9.1 The world clocks (CALENDAR, MATTER, ENCOUNTER).**
*Playable alone:* not a game and not meant to be one: they offer no choice. What exists as a scenario is
`harness/scarce.py` (a planted scarcity) and the IN-35 hand-built lattice world; neither has a choice
surface or an end condition. *One code path:* yes; there is no standalone fork, and the modules MATTER
calls (`settlements.subsist`, `settlements.produce`) are reached by composition row. *Integrates:* executed
edges both ways (§10). *Layer 1:* conformant with the three graded exceedances of §4.3. *No GM:* holds.
*Missing for play:* a survival scenario, which is §9.3.

**9.2 The narrative instruments.** Not gameplay; observers. What a player-facing layer needs from them
does not exist: nothing presents a strand, an era or an ending to a person. `presented`/`slot_rank`/
`flow_capacity` compute a presentation nobody reads (§5.3).

**9.3 A world scenario a player could enter today: "hold the valley".**

| element | exists | missing |
|---|---|---|
| scenario seed | `build_realm(seed)`; `harness/scarce.py` for a planted scarcity | a small fixture (one territory, three settlements, one seat) so a season costs seconds, not the realm's forty |
| entry point | `play_surface.dispatching_chooser` binds one person to a callback; `headless.py` runs a case | a named scenario in `exercises.py`'s overlay (no new harness) |
| choice surface | the verbs `opening_set` forms on the one delivered question | a slate: `question_aggregation_rule = "first"` delivers one question, so the player does not choose what to attend to (§5.5 b) |
| stakes | larders, bodies, fabric, seats | motion: at shipped fixtures nothing threatens (F-WR-04) |
| outcome legibility | the player's own ledger; `census`'s hunger and closed-uses report | a person-side reading of a settlement's hunger and a fabric's band (both are World reads today, `world_q.hunger`, `closed_uses`); a reason for others' acts (§5.5 d) |
| end condition | `endings_reached` (two rows) | a reachable ending (F-WR-06); any survival ending: the design's Rupture has no row and no carrier |
| instrument | `aperture`, `storybar`, `strife` | one that can fail (F-WR-03) |

Ordered work to close: steps 1, 3, 4, 5 of §8; then the slate (CHAR/GO: deliver the sorted questions to a
player callback); then a survival ending row once the lattice is live (Jordan's content).

**9.4 Threadwork.** *Playable alone:* no. No scenario, no verbs but `thread_read`, no host. *One code
path:* no; today there are zero game paths and one oracle path with held state. *Integrates:* no executed
edge (§10). *Layer 1:* not a registered module (F-WR-05). *Ordered work:* `09_WR_threadwork_module.md`
edits 1 to 3, then B10-15, then its edit 4 (the scenario).

## 10. Interfaces

| edge | direction | real (executed) or designed | evidence |
|---|---|---|---|
| MATTER → SE (`settlements.subsist`, `settlements.produce`) | consumes | real | `matter.py:600`, `:741`; `stores.changed` 185, `yield.taken` 111 (E-07) |
| MATTER → CHAR (claims of `condition.worn`, `stores.changed`, `body.changed`, shortfall Observations, through WITNESS) | emits | real, but few become acts | acts classed `world` 365 of 2,630 (E-07) |
| MATTER → FA (a matured `oblige` term closes the edge) | emits | real | `matter.py:428-435`; `tenure.closed` 27 in season 5 (E-08), cause not read `[UNVERIFIED]` |
| CALENDAR → SC (`date.fired`, docket slots, re-slot) | emits | real | `date.fired` 5, `docket.formed` 7 in two seasons (E-05); `determine` 3 of 6 (E-08) |
| ENCOUNTER → PC, MB (deferred contests) | calls | real for marches; **no duel reaches it** | `march` Declared 29, Unopposed 6, Lost 1; `fight`/`accept` deaths 0 (E-07) |
| `questions_for` → CHAR (`decision/`) | emits Questions | real | every act |
| `flow_stakes` → CHAR (the stamp) | emits classed referents | real, dose 0 to 28% of persons by seed | F-WR-07 |
| `endings_reached` → driver summary | emits | real, always `[]` | E-05 to E-12 |
| `hunger`, `uncontrolled`, `closed_uses` → anything that decides | emits | **designed only** | one caller each, `populated.census` |
| threadwork → loop | both | **designed only** | F-WR-05 |
| `thread_read` → FI (`fieldwork.find`) | consumes | real | 3 and 4 executed (E-07, E-12) |
| `kit_of` → PC (weapon and armour) | emits | real call, constant answer | `ARMS_KINDS` empty (H-350) |
| `practice` → DICE (pool addend) | emits | real | registered in `seam/wrappers/pool.py`; `practice_cap` 2 (E-13) |
| strife readings → GO (presentation) | emits | **designed only** | `presented` has no reader |

## 11. Survivors for Jordan

Three items survive the ladder. Each would overwrite a ratified or ruled item.

1. **The same-doer link (strife A9, ratified ED-IN-0316).** *As ratified:* any two deeds of one doer link
   two moves into one strand. *Observed:* at six seasons one strand holds all 234 moves and 55 doers
   (E-08). *Option A, keep:* the realm's strife is one river; R3 ("new events fold into existing flows")
   and R11 ("one era in lived terms") are served literally, and the era is the only flow a reading need
   present. As a game: one continuous "the troubles", legible as mood, with no sub-plots to follow.
   *Option B, bound it* (`09_WR_strand_conclusion.md` edit 3: a doer's later deed joins a strand he opened,
   or joins by referent): several strands at their own rungs beneath the era, which is R11's other half
   ("narrative chains within it sit at lower levels"). As a game: named, separable stories that can each
   end. I cannot choose between two sentences of one ruling.
2. **Natural death (`illness_rate`, `age_step`; deferred by ED-IN-0317).** *Option A, keep deferred:* no
   person dies except by another's act; succession is always somebody's doing; with duels refused, seats
   never empty (0 deaths in six seasons at seed 0). *Option B, a live rate:* seats empty with nobody to
   blame, and vacancy, obligation and conferral follow (E-11, E-12, E-16). As games: A is a realm of
   permanent incumbents until violence works; B is a realm whose cast turns over. The evidence is two
   seeds at one rate and is a direction, not a value; the value is Jordan's, and `age_at_build` must be
   authored first.
3. **The slate.** `question_aggregation_rule = "first"` (H-54's precedent) against the ruled auto/manual
   doctrine (ED-SC-0013: "choosing what to attend is the gameplay"). *Option A:* one question, the engine's
   pick, for player and NPC alike: a game of answering what arrives. *Option B:* the sorted list offered to
   the player, the first to NPCs: a game of triage for the player with NPCs unchanged, at the price of the
   player and the NPC no longer being served identically. Owned by CHAR and GO; listed here because
   `questions_for` is this lane's file and the conflict is with a standing requirement.

## 12. Evidence log

All runs `PYTHONHASHSEED=0`, shipped fixtures unless stated, full realm (`cap=None`), no pytest. Outputs:
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/WR/`. `wr_probe.py`,
`wr_null.py` and `wr_unc.py` are read-only scratch scripts in that directory (they build a realm in
memory, run seasons, read the log; they write nothing but stdout).

| id | command | seed · seasons | outcome |
|---|---|---|---|
| E-01 | `python -m engine.season.harness.chronicle --seed 0 --seasons 2 --chains --min-depth 2` | 0 · 2 | depth 4: `conceal → create_record ×3`; `consequence_acts=446`; `chain_ends=29` |
| E-02 | `… storybar --base-seed 0 --seasons 2 --draw-seeds 0 1 2` | 0 · 2 | base hash unmutated; draw 0 against 1: chains DIFFER (394), depth DIFFER; 0 against 2: DIFFER (362) |
| E-03 | `… storybar --base-seed 0 --n 2 --seasons 2 --arms off off --executed-only` | 0, 1 · 2 | EQUAL; pooled cross share 21.4%, max depth 10 |
| E-04 | `… register --requirements` | — | met 3, not_met 1, partial 5 |
| E-05 | `wr_probe.py 0 2` | 0 · 2 | season hashes `5ab73af2…`, `bacd687f…`; 1,703 acts, 898 refused; 3 strands, 1 "concluded" (15 marches); person reading 0 of 83; arcs 21, null [1,0,0], unrestricted 53; chain ends ≥2: 29 against shuffled 86 to 97 |
| E-06 | `wr_probe.py 0 3 1` (`scene_budget` swept to 1) | 0 · 3 | 519 acts; same-season cross edges 0; cross-season 51, 68 |
| E-07 | `wr_probe.py 0 3` | 0 · 3 | 2,630 acts, 1,440 refused; 74,510 Events; 0 deaths; same-season cross edges 128, 160, 158; 5 strands, 0 concluded, largest 63 moves and 17 doers; all 16 links observed 0; `PT→PT` 13 against control 11.09 |
| E-08 | `wr_probe.py 0 6`; `wr_probe.py 1 6` | 0, 1 · 6 | seed 0: 5,483 acts, 3,124 refused; 273,067 Events, 179,056 `claim.decayed`; `endings == []` ×6; 1 strand, 234 moves, 55 doers; arcs 33, null [2,0,0]; deepest consequence chain 4. Seed 1: 5,544 acts, 2,953 refused; 247,204 Events; `endings == []` ×6; 2 strands (119 moves and 30 doers; 13 moves), 0 concluded; arcs 34, null [0,1,1]; person reading 9 of 82; deepest consequence chain 3. Seed 2 (`wr_probe.py 2 6`): 5,509 acts, 2,908 refused; 277,603 Events; `endings == []` ×6; 2 deaths; 5 `field.lost`; `challenge` 0/223, `accept` 0/118, `covenant` 0/27, `determine` 1/6; 1 strand, 241 moves, 51 doers; arcs 34, null [0,0,1]; person reading 27 of 81, stamped 23; deepest consequence chain 3 |
| E-09 | `… strife 2 0`; `… strife 3 0 1 2` | 0 · 2; 0–2 · 3 | OBSERVED 4, UNOBSERVED 8, KIND-ONLY 25, GAP 3; and OBSERVED 6, UNOBSERVED 6, KIND-ONLY 25, GAP 3; terminal codes with no static route: DN |
| E-10 | `wr_null.py 0 2`; `wr_null.py 1 2` | 0, 1 · 2 | executed depth ≥3: 36 against null 10.8 (6..15); 27 against 9.0 (5..14). Consequence depth ≥3: 2 against 1.2 (0..3); 0 against 1.1 (0..4). 90 of 101 and 92 of 98 answering acts name the antecedent's actor or subject |
| E-11 | `WR_FORCING=1 wr_probe.py 0 3` (illness 0.05, weather draw, coupling 250) | 0 · 3 | 8 deaths; `tenure.closed` 10; `oblige` 146/277; `confer` 1; `determine` 1; cross share 22.1%; 0 band crossings; `restore` not attempted |
| E-12 | `wr_probe.py 1 3`; `WR_FORCING=1 wr_probe.py 1 3` | 1 · 3 | off: 1 death, 1 `matter.determined`, cross share 22.3%, 2 "concluded" one-doer march strands, largest strand 45 moves; on: 4 deaths, cross share 24.4% |
| E-13 | `python -` probe on `build_realm(0)` | 0 · build | 18 territories, 16 in the realm, 15 settled, 15 held; T15 no Site; 7 of 83 persons with a thread sensitivity; `capability` non-empty on 2 |
| E-14 | `grep` for callers and importers (commands in §3, §4) | — | as cited |
| E-15 | `python -m engine.season.harness.corpus_run` | 0 | 143 cases; R1, R3, R4, R5 pass 46/46 and 97/97; ENDS NOT-COMPUTABLE; verbs only refused include `accept`, `covenant`, `determine`, `exchange`, `train`; `thread_read` never attempted |
| E-16 | `wr_unc.py 0 3 on|off`; `wr_unc.py 1 3 on` | 0, 1 · 3 | unheld territories 1 throughout; vacant offices 0, 3, 5 of 35 (seed 0 on), 0, 1, 1 (off), 0, 0, 1 (seed 1 on); band crossings 0 |
| E-17 | `python -` over `run_cases.load_cases` (keyword tagging of `season_requires`) | — | 143 cases; 167 tagged needs, 79 `core`: COUNTER 87, SUBSTRATE 36, THREAD 33, BODY 22, TRAVEL 2, SEASONAL 1 (a need may carry two tags) |

**Read.** Code in full: `loop/calendar.py`, `loop/encounter.py`, `loop/matter.py`, the six harness files
and `strife_moves.yaml`, `ENDINGS_CLASSIFIED.yaml`, `play_surface.py`; `queries/world_q.py` lines 1 to
3,800 and 3,836 to 4,356 and 4,700 to 5,556. Design set (`.designs/`, intent only), in part: `victory_v30.md`
(index; Core Frame, §0, §4 to §6), `calamity_radiation_v30.md` (principle, distance map, first three
bands), `ms_trajectory_v1.md` (§1 to §3), `scale_transitions_v30.md` (index; §3.9 to §4.3.3),
`auto_manual_resolution_duality_v1.md` (§1, §2), `propagation_spec_v1.md` (status head),
`threadwork_v30_index.md`. Audit corpus (`.audit/`, lesser weight): `2026-08-08-world-churn-audit/00_findings.md`
(§0, §5), `2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md` (status, §0 head).

**Not read** (the receipt lists these as skipped, with the reason): the rest of the two design sets and
both audit entries; `world_q.py` 3,800 to 3,836 and 4,356 to 4,700 (`wounded_with`'s tail, `witnessed`,
`PersonProjection`, `WorldReader`); the test files beyond their names and the three opened; the threadwork
oracle beyond its docstrings, constants and signatures.

## 13. Provided arcs and characters — adjudication

`corpus_run` (E-15) runs all 143 cases and scores no ending (`ENDS = NOT-COMPUTABLE`), so "represented" is
judged here from the code path and the realm runs, never from the case file. Hardness is the case's own.
Proposal files are under `proposals/`; "arcs" is `09_WR_provided_arcs.md`.

| case(s) | need (short) | hardness | represented today? | evidence | change required | owner | proposal | gate |
|---|---|---|---|---|---|---|---|---|
| ARC-05, ARC-48, EMG-C3 | an ambient world quantity decays by itself on a schedule | core | **in kind**: fabric wears each season | `condition.worn` 322 a season (E-07); `matter.py:852-884` | none for decay; a source so it means the Calamity | WR | `09_WR_world_motion.md` e1 | crossings ordered by distance from T15 |
| ARC-48, ARC-27, ARC-43 | bands; crossing one changes what a class of acts can do in a territory | core | **in kind**: a Site below a floor closes its uses | `world_q.verbs`, `closed_uses`; 0 crossings in any run (E-16) | the live weight | WR, SE (H-165) | same | `closed_uses` non-empty at ring 1 |
| ARC-48 | higher difficulty → more failure → further decay (a closed loop) | core | no | no working exists to fail; `WorkingOutcome.strain` is the carrier | B10-15 with strain | WR | `09_WR_threadwork_module.md` | a failed working lowers a Site |
| ARC-05 | cost accrues invisibly across well-meant acts | core | no | as above | as above | WR | as above | as above |
| ARC-41, EMG-X8 | a capability dormant until the ambient quantity crosses a band, then open to all who have it | core | no | no reader of a band gates a thread row | a `scalar_threshold` cell on the thread rows reading the local fabric band (the `floor` stem exists) | WR | B10-15 (CP-T07-05's place gate) | the row forms below the band, not above |
| ARC-42 | an outcome moves the ambient quantity if sensitives were present | core | no | — | `mend`/`restore` by a sensitive | WR | B10-15 (CP-T07-04) | — |
| NPC-002, EMG-X7, SCN-LOOP-A | a working costs the practitioner a persistent personal resource, scaled by the working | core | no | `(Person, coherence)` unproduced (`write_matrix.yaml:206`) | the carrier and the host | WR | `09_WR_threadwork_module.md`; B10-15 | `coherence.changed` in a run |
| EMG-X7, ARC-09 | a floor state past which the capability, or agency, is lost | core | no | — | CP-T07-07 (permanent set narrows the season) | WR | B10-15 | budget falls at the band |
| NPC-075 | an unrewarded maintenance labour is a real season-to-season choice, and wears the labourer | core | half: `restore` is a choice; nothing wears the mender | `restore` attempted 0 (E-07): the choice never arises | the source (so there is something to mend) and the working's cost | WR | world_motion e1; B10-15 | `restore` attempted > 0 |
| NPC-004, NPC-005, ARC-51 | a hidden sensitivity, true and active, unknown to an institution; readable by another | core | half: `Person.thread_sensitivity` exists and gates `thread_read`; nobody can read another's | E-13 (7 of 83); `verb_table.yaml:1861` | what `thread_read` finds (CP-T07-10) | WR, FI | B10-15 | a finding naming another's sensitivity |
| ARC-51 | sensitivity advances by a low-cost mode of use, in bands | core | no: set at build, written by none (`harness/loops.py:96`) | — | a growth rule for the scalar | CHAR (capability growth) | §14 | — |
| ARC-34, ARC-47, ARC-31, ARC-32, NSC-05, NSC-08, EMG-C1 | a private counter fed by unrelated triggers that forces a formal step at its ceiling | core | no; the lawful form is permitted and unbuilt | `single_holder_counter` raises `Unspecified` (`world_q.py:162-168`) | the closed registry and a question at the count | WR, CHAR (axes) | arcs e1 | the three-claim falsifier |
| ARC-47, NSC-08 | that counter never decreases | core | **wrongly stated** | claims decay and evict by design | restate: a tally is what is still held | — | arcs e1, e4 | — |
| ARC-46, ARC-50, EMG-C2, NSC-09, ARC-03, ARC-45 | an institution's standing rises by itself; side effects feed it | core | no | — | clocks as folds of the log | FA, IN | CR-89 (B10-17b) | CR-90's arc instrument |
| ARC-46 | "purely from the passage of time, with no actor choosing" | core | **wrongly stated** under L5 and ED-IN-0301 | — | restate: from its members' acts, read as a fold | FA | arcs e4 | — |
| ARC-52 | a ceiling eliminates a faction with nobody declaring it | core | **wrongly stated** as an automatic outcome; lawful as a reported ending | `endings_reached` | an `endings` row | Jordan (content) | — | the row reached by acts |
| ARC-02 | a state-change check fires on a person with no actor initiating it | core | in kind for bodies only (the bodies clock, dark) | `matter.py:726-731` | §11 item 2 | Jordan | — | — |
| ARC-53, SCN-07 | an injury persists until a recovery act; no passive recovery | core | **yes** | `body.tended` 37, `tend` 37/69 (E-07); MATTER only lowers a body | none | — | — | — |
| SCN-06, SCN-LOOP-C | drains and restorations on one resource summed per season | core | half: the larder draw sums; a fed body does not mend | H-211 | the signed step | WR, SE | arcs e2 | MW-11 |
| ARC-23 | a threat that exists only while one person maintains it ends with him | core | **yes** | `remove_person` closes his edges; an ambition is a live `commit` (`world_q.ambitions`) | none | — | — | — |
| ARC-07 | a failed sub-check in battle leaves a condition that outlasts the battle | core | not WR's | — | — | MB, PC | — | — |
| NPC-052 | a removed leader's succession stays undetermined among claimants | core | half: the seat empties; no rival claims observed | vacant offices 5 of 35, 1 hold opened (E-16) | — | FA | — | — |
| EMG-10 | nine conditions across subsystems jointly open one flashpoint | core | no | — | a tally over nine axes is edit 1 at scale; the conditions are other lanes' | all | arcs e1 | — |
| ARC-01, ARC-44 | a cultural quantity drifts where no faction acts | core | no; a stored social scalar on a place is refused (`04` §B.3) | — | restate as persons' held affiliations by place, a Query | CHAR, SE | — | — |
| the 19 `forced_by_threshold` cases | a crossing forces the moment | — | **misrepresented** by a planted holderless date | `corpus_run.py:656-660` | stop planting; author a tally | WR | arcs e3 | no `d_forced` in any built world |

**Simulable end to end soonest, once this lane's changes land.** (1) ARC-53 and SCN-07 (injury and
recovery) run today; they need only an overlay row. (2) ARC-23 runs today. (3) EMG-C3 and ARC-48's first
two needs (a decaying world quantity in bands that persons may or may not attend to) after
`09_WR_world_motion.md` edit 1 and the weight: the artifact is a seeded run in which crossings spread by
distance from T15 and some person `restore`s. (4) ARC-34, ARC-47, NSC-08 (the private counter) after
`09_WR_provided_arcs.md` edit 1 and one authored axis each: the artifact is a seeded run in which the holder,
and only the holder, is offered the step when his ledger holds the triggers. (5) Every THREAD arc after
B10-15 on the module proposal.

**Dependency edges.** WR → PC, SC, FA: every arc whose close is a duel, a judgment or a treaty waits on
those verbs executing (F-WR-01). WR → SE: the lattice weight waits on H-165. WR → CHAR: tally axes and
sensitivity growth are capability and character content. FA → WR: CR-89's clocks. CORE → WR: the reason
trail and claim fade.

## 14. Capability authoring surface

**The existing owner, not a new one.** A character's capability reaches a roll through one function,
`seam/wrappers/pool.py::faculty` (the registered pool addends), keyed by `rosters.yaml: verb_capability`
(verb → vocation) and `vocation_attribute` (vocation → attribute), over `Person.capability` and the
attribute carrier (CR-20). CHAR's `02_CHAR_capability_uses_table.md` extends that owner; this section
states what WR reads and what it needs from it.

**(a) Where this lane takes a capability as input.**

| site | what it reads | from |
|---|---|---|
| `world_q.practice` (`:4703-4744`) | the verb's vocation; the person's own Success-or-better acts in a window; three fixtures | `VERB_CAPABILITY`; `w.log`; `practice_window`, `practice_step`, `practice_cap` |
| `world_q.kit_of` (`:3484-3509`) | arms kinds in the stores of the rungs he holds, else where he lives | `rosters.yaml: arms_kinds` (empty); `Rung.stores` |
| `thread_read`'s typed cell (`verb_table.yaml:1861-1862`) | `Person.thread_sensitivity` against `thread_sensitivity_gate` | cast row `ts:` via `data/cast.py::thread_sensitivity_of`; a fixture |
| `world_q.body_hazard` (`:1248-1270`) | `Person.born`, `is_cohort`; two rates | carrier; fixtures |
| `world_q.wounded_with`, `loop/matter.py`'s body pass | `Person.body`, `body_ceiling`; `body_step` | carrier; fixture; `band_floors.body` |
| `world_q.training_sites` (`:2261`) | Site conditions where a cohort resides | `w.sites` |
| threadwork oracle `_actor_pool` (`operations.py:235`) | `.spirit`, `.focus`, `.ts` on a duck-typed actor | the caller's object |
| threadwork oracle Ob and cost tables (`operations.py:73-168`), Coherence bands (`coherence.py:113-133`) | module constants | hard-coded |

**(b) Data-driven, hard-coded or doubled.** Data-driven: `practice`, `kit_of`, the thread-sensitivity gate,
the hazard rates, the body bands. Hard-coded: every threadwork table and band edge, three of them tagged
"magnitude invented" at the definition; the depth gates (`DEPTH_TS_MINIMUM`) duplicate in a second
vocabulary what `thread_sensitivity_gate` already says for one verb. Doubled: thread sensitivity has two
readers with two thresholds (the fixture gate for `thread_read`; the oracle's `LEAP_OB_TS_LOW/HIGH` and
`DEPTH_TS_MINIMUM` bands), and the practitioner's pool has two definitions (`faculty` for every loop verb;
`_actor_pool` for a working).

**(c) Target shape for this lane.** A capability definition must say, for WR to use it: its **id**; its
**kind** (attribute, vocation, or scalar aptitude such as thread sensitivity); its **scale and bounds**;
which **verbs** it feeds and whether as pool dice, as a gate (`scalar_threshold`) or as an obstacle band;
its **growth rule** (practice window, step and cap; or "set at build"); and, for a scalar aptitude, its
**bands** and what each band admits. One file carries it: the roster CHAR's proposal names as the
capability table (today `rosters.yaml: verb_capability` and `vocation_attribute`). WR adds no file. It
needs four things from that table: (1) a row kind for a *scalar aptitude with bands* (thread sensitivity:
bands gate `thread_read`, the Leap and each depth; one definition, read by the gate stem and by
`modules/threadwork`); (2) the working's pool expressed as a `faculty` addend like any other, so Spirit,
Focus and practice reach a working by the registered route (CP-T07-02's "registered `faculty` addend"
already says this); (3) a growth rule slot that a scalar aptitude can use (ARC-51 asks for it; today the
scalar has no writer); (4) the working's obstacle axes (depth, breadth, distance) as a typed parameter
file under `engine/engine_params/` (`09_WR_threadwork_module.md` edit 3), since they are properties of the
act and not of the character.

**The interface, for the merge:**
`capability(person, id) -> int` (attribute, vocation or scalar); `band(person, id) -> str` for a banded
scalar; `feeds(verb) -> ((id, role), …)` with role in `pool | gate | obstacle`; `growth(id) -> rule`. WR
reads the first two in `Practitioner` (module input) and in the gate stem; it never writes one.

**(d) RPG axioms, in the tradition's vocabulary.** Implemented: *use-based advancement with a cap and
decay* (`practice`: do it well, gain dice, for a while); *attribute-gated ability* (thread sensitivity as a
prerequisite score); *gear from holdings* (kit read off what you own, never consumed); *attrition tracks
with thresholds* (body bands; hunger as a save you fail by being unfed); *power at a price* (a working
costs Coherence: designed, unbuilt in the loop); *ageing* (a hazard by age: built, dark). Lacked, that a
designer would expect: *advancement of the casting stat* (sensitivity never changes); *a trained skill
for the craft* (no vocation maps to a thread verb, so `practice` cannot improve a practitioner);
*corruption or sanity as a second track with recovery rules visible to the player* (Coherence's elastic
and plastic halves exist in the oracle only); *survival skills* (nothing a person is good at changes what
a journey or a winter costs him: CP-T10-01's pricing has no person-side reader). Contradicted: *the
character's own sheet is the source of his pool*: the oracle takes whatever object the caller hands it.

**(e) Proposals, ordered.** (1) `09_WR_threadwork_module.md` edits 1 and 3: `Practitioner` built from the
capability table, the tables as typed data. (2) A banded-scalar row kind in CHAR's capability table, with
thread sensitivity as its first member and the two existing thresholds folded into its bands (CHAR's
file; this lane supplies the bands from `operations.py:95-124`). (3) A thread vocation in
`verb_capability` for the B10-15 rows, so `practice` reaches them (data, with B10-15). (4) A growth rule
for the scalar, design-first (ARC-51 states the need; nothing rules the rate).
