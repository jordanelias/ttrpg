# WR — adversarial steelman audit, addendum B

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: a3ee7e6 (working tree)

The first WR audit (`09_WR_audit.md`) was read at `601e715`. `git diff --stat 601e715 a3ee7e6 -- engine modules
systems references architecture workplans registers research CURRENT.md` is empty: no code, registry, plan or
research file moved between the two readings, so every run the first audit logs (its §12, E-01 to E-17) is a
reading of the tree this addendum was written against. Findings continue the first audit's numbering from
`F-WR-13`; resolutions continue from `R-21`; evidence ids are `EB-nn` so they cannot be confused with the
first audit's `E-nn`. Nothing in the first audit or its five proposals is edited; where this file disagrees
it says so, and where a proposal is replaced the replacement carries a `_B` suffix and names what it
supersedes.

Design documents under `.designs/` and audits under `.audit/` are cited as referents for intent, vocabulary
and history (CLAUDE.md §0.05); none is the reason a behaviour is correct, and no proposal here makes code,
a tool or a test read either tree.

## 1. What was read

Written as the reading proceeded; the list at the end of this section is the final one.

**Read in full, block 1 (research and the narrative-engine referents).**
`research/emergent_narrative_literature/00_README.md`, `01` to `07` and `08_not_read.md` (all 42 entries and
the 75-row apparatus); `.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v1.md`,
`narrative_engine_design_v2_churn.md`, `integration_with_ners_audit.md`.

<!-- READ-LIST-CONTINUES -->

## 2. Corrections to the first audit, and new findings

<!-- SECTION-2 -->

## 3. The emergent-narrative engine, read against the full design set and the literature

**Verdict.** The engine has the one property the literature treats as the hardest to retrofit (a recorded,
walkable cause for every Event: gate B2, D5) and lacks the three that turn a causal record into a story
anyone can find: a **close that is an act**, a **telling with a viewpoint and a subject**, and a
**reading of tension** (what is open, between whom, and whether it is rising or releasing). The design set
knew all three in July (`narrative_engine_design_v2_churn.md` §4: connected, continuous, rooted, live); the
season loop kept the first two invariants as substrate and dropped the last two with the Key substrate
they were written on. The shortest faithful path does not rebuild that engine. It is four readings over
what the loop already records, one content change to how weather is drawn, and the closing verbs other
lanes own.

### 3.1 What a story is, for this engine

Each term is given a definition the engine can compute from what it stores today, in the vocabulary of the
tradition, and the place the definition comes from. None needs a carrier (ED-IN-0225, T-a); each is a
reading. Where the first audit already fixed a term, this section adopts it.

| term | definition over the engine's own records | source of the shape | computable today? |
|---|---|---|---|
| **beat** | one executed act whose own Event wrote a consequence cell (`harness/arc.py::consequence_acts`), together with the question it answered | Façade: "the smallest unit of dramatic action that moves a story forward" (T03a); the engine's unit is an act, not an authored bundle | yes: 446 at seed 0, two seasons (first audit E-01) |
| **incident** | a state with duration that a person did not choose and that more than one person can answer: a shortfall, a fabric below its floor, a vacancy, a term running, a detention | Sylvester as reported (G14.Q4): "the richness comes when several events interact"; incidents must last and overlap | partly: terms, dockets and legs have duration; weather does not (§5) |
| **situation** | two or more persons whose live edges cannot all be satisfied on one referent: two ambitions on one seat, a holder and an occupier of one rung, a creditor and a defaulting obligor, a party who is also the judge, a custodian and the kin of the held | Lessard & Paré-Chouinard (E04): "dramatic situations are not sequences but states", reachable by many histories; Kybartas et al. (E05): conflict potential is computable before a run | **no reading exists** (F-WR-15) |
| **strand** | the strife design's: a connected component of strife moves around shared referents, read at the lowest rung covering it | `00_MASTER.md` §4 (ratified) | yes; collapses to one by season six (first audit F-WR-02) |
| **reversal** | within one strand or one person's record, an edge that closes against its holder after having opened for him: a hold lost, a seat vacated, a field lost after a march declared, a commitment closed unmet | Kreminski et al. (E11): none reads as a steady rise, "a few (up to three) feel compelling, and more begin to feel incoherent" (anecdotal, n=2) | not read |
| **arc** (of a person) | he wrote on his own thrust and on the world, in that order, and a later Event changed what his thrust stands on | `harness/arc.py` (CL-THRUST B0.1), whose two nulls hold on real logs (first audit §4.5) | yes; its positives today are cohorts uttering (first audit R-10) |
| **ending**, three scales | *strand*: a terminal, non-opening move with no open referent; *person*: `exists` goes false, or his last live `commit` closes; *realm*: a row of `rosters.yaml: endings` reached | strife R6; `endings_reached` | strand: mis-read (F-WR-02); person: readable, unread; realm: never reached |
| **tension** | the number of open situations and open incidents at a season boundary, and its change: how many opened, how many closed by an act, how many closed by a clock | Booth (G10.Q1, Q2): a tension variable with named inputs and a designed fall after a peak; here it is read, never steered | **no reading exists** (F-WR-15) |
| **telling** | a selection with a stated criterion, an order, a subject for every line and a named viewpoint | Ryan as reported by Short (E12.Q1); Aylett (T11.Q2): "whose viewpoint it is told from"; Juul (T06.Q1): a retelling that only recounts moves loses the system | half: selection and order exist; subject and viewpoint do not (F-WR-14) |
| **retelling** | a second person's account of the same Events from his own ledger, which differs from the first | Eladhari's fourth layer (E01) moved inside the fiction: `tell`, `forge`, `lie`, the `chronicle` channel | the acts exist (`tell` 12 of 72 executed, seed 0, three seasons); no reading compares two accounts |

Two consequences of writing the terms down. First, **the engine's story unit is the situation, and it has
no word for it.** The strife registry names forty *moves* and sixteen *links*, which are sequences; the
study it reads found the categories "alike between opening and ending" (`00_MASTER.md` §2), which is the
finding that sequence does not discriminate. A situation is a state the engine can already evaluate from
`w.tenures` and the docket, and it is the level at which apparatus rows C2 ("name its target situations,
show each is reachable, report how often each occurs") and B4 ("the same target situation through
different causal histories and casts across seeds") can be answered at all. Second, **tension is defined
by what is open, so a world that never closes anything has monotone tension and no shape.** That is what
the runs show (§3.2).

### 3.2 What the runs say about closure: the realm closes by clock, not by act (F-WR-13)

Read from the first lane's six-season outputs (its E-08; seeds 0, 1, 2; `PYTHONHASHSEED=0`; shipped
fixtures), by Event kind per season. No new run.

| what opens, six seasons | seed 0 | seed 1 | seed 2 | what closes it | seed 0 | seed 1 | seed 2 |
|---|---|---|---|---|---|---|---|
| `petition.filed` | 51 | 59 | 68 | `matter.determined` (an act) | 1 | 2 | 0 |
| `docket.formed` | 31 | 30 | 17 | `matter.lapsed` (MATTER, at `docket_lapse` 4) | 8 | 8 | 7 |
| `duty.taken` | 67 | 42 | 152 | `tenure.closed` | 33 | 16 | 37 |
| `march.declared` | 78 | 22 | 56 | `field.lost` + `field.unopposed` | 7 | 7 | 15 |
| `case.opened` | 11 | 16 | 11 | (no closing kind in any run) | 0 | 0 | 0 |
| `challenge` attempted | 223 | 253 | 223 | executed | 0 | 0 | 0 |

`matter.lapsed` occurs in exactly one season of each run, the sixth (per-season `[0, 0, 0, 0, 0, 8]`,
`[0, 0, 0, 0, 0, 8]`, `[0, 0, 0, 0, 0, 7]`), and `tenure.closed` is `[0, 0, 2, 2, 2, 27]` at seed 0 and
`[1, 1, 2, 3, 3, 27]` at seed 2. The shipped terms are `oblige_term = 4` and `docket_lapse = 4`
(`data/fixtures.py:1104`, `:1168`), so both spikes fall where a term wound in season 1 runs out. The
first audit left "the 27 are matured `oblige` terms" unverified. It is still not traced to the closing
Event's causes, but the three seeds make a natural control: `duty.taken` in season 1 is 26 at seed 0, 26 at
seed 2 and **0** at seed 1 (its duties are taken in season 2), and the season-5 spike is 27, 27 and
**absent** (seed 1 reads `[1, 2, 3, 5, 1, 4]`). The inference is corroborated; `[UNVERIFIED]` narrows to
the one extra closure per seed.

**Claim.** In the shipped realm a matter is nine times likelier to end by expiry than by judgment (23
lapsed against 3 determined over the three runs), and the first closures of any size arrive at the season
the terms mature. The storyline the engine produces unaided has the shape *opened, unanswered, expired*.

**Falsifier.** A season in which `matter.determined` is at least `matter.lapsed`, after season 4. None in
the six season-readings past season 4 at three seeds.

**Why it matters here and not only in SC's audit.** Expiry is lawful (a declared term, T-n) and it is
the engine's own form of forgetting, which the design wants (primitives-v2 proposal 12: "he loses the town
by being forgotten"). But in the literature's terms an expiry has none of Schmid's eventfulness properties
that Lessard & Paré-Chouinard use (unpredictability, effect, irreversibility, non-iterativity, relevance):
it is predictable to the season, changes no one's options, and repeats. A world whose closures are mostly
expiries reads as "boring football matches" (Aylett, T11) however dense its causal graph is, and no
instrument in the tree distinguishes the two kinds of close. The first audit's strand-shape reading counts
`closed`; it should count *closed by an act* and *closed by a clock* separately (proposal
`09_WR_B_readings_of_closure_and_tension.md`, edit 1).

**Touches.** R-02, R-05; NERS-R's no-player half.

### 3.3 The telling: omniscient, without subjects, picked by forward depth (F-WR-14)

**Claim.** `harness/chronicle.py` is a selection stage and not yet a telling. Against gate D of the
apparatus it passes D5 (a stored, finite cause set) and E15.Q2 (every stated cause is a recorded fact,
labelled "had among its causes"), and fails four rows by construction:

| row | what it asks | what `chronicle.py` does | line |
|---|---|---|---|
| T06.Q1 | a retelling that keeps the existents, and does not only recount moves | a line is `season · actor · verb · emitted kinds · answers n`; **no line says what the act was about**. The rendered chain at seed 0 is `conceal → create_record → create_record → create_record`: three records about what, concealing what, is not printed | `:128-162` |
| T11.Q2, D6 | the viewpoint of each telling is nameable | it reads `w.log` and the driver's `act_of`: world truth, no focalizer. The per-person, label-free render that was ratified as intent (primitives-v2 proposal 1; narration-mechanisms §2.1's journal, NM-W5) is unbuilt | `:227-245`; `workplans/…part4.md:300` |
| E10.Q1 | when many matches exist, a rule better than first-found | the end of the chain is "the first-logged act of maximal depth"; the walk back takes "the smallest act id on a tie", a hash order | `:93-101` |
| E12 (Labov, as Short reports Ryan) | start at the most interesting final event and chain backwards to one that needs no explanation | the pick starts from depth, never from what closed. The Events a reader would call story (seed 1, six seasons: one `person.died`, one `rung.razed`, one `covenant.offered`, two `matter.determined`) are never the end of a rendered chain unless they happen to be deepest | `:86-104` |

**Evidence that the missing fields exist.** `state/carriers.py::subject_of` is "THE ONE READ" of an act's
subject (`:949`); `soak._occasion_row` returns the question an act answered; narration-mechanisms §3.2
already assigns each line field to its owner. Nothing needs inventing.

**Falsifier.** A rendered chain at any seed whose lines let a reader who did not build the engine say what
was concealed, recorded or contested. `runs/WR/chronicle_s0_k2.txt` is the counter-example.

**Consequence.** The project's first answer to "why did that happen?" (`04` §C.11) prints who and in what
order and omits what. Proposal 1 of the primitives set named this risk itself ("a wall of lines fails the
same way the almanac does") and asked for a cheap falsifier before any design: hand one reader another
run's record. That test (apparatus D7, a `rater` row) has not been run, and cannot pass on a render with no
subjects. This is recorded as `paper`, not as failed.

**Minimal fix.** Proposal `09_WR_B_chronicle_that_tells.md`: an `about` field from `subject_of`; a pick
that starts from closing Events, defined structurally (an Event whose Receipt writes a `Tenure.until` or an
`exists` cell); ties broken by rarity within the seed (StU's form, E10) and no longer by hash. The
focalized journal stays NM-W5's; this proposal only removes what would make it unreadable when it lands.

### 3.4 No reading of situations, tension or starvation (F-WR-15)

**Claim.** The engine cannot say what is at stake between whom at a season boundary, whether that set grew
or shrank, or which persons did nothing.

**Evidence.** (a) No function under `engine/season/` (tests aside) computes a set of open conflicts:
`grep -rn tension --include=*.py engine/season` returns docstring uses of the ordinary word and nothing
else (§9 EB-03). The pieces exist as separate stampers (`vacancies`, `detainees_held`, `matters_awaiting`,
`holdings_to_found`, `ambitions`, `at_war`, the docket), each read by `questions_for` for one person at a
time. (b) Narration-mechanisms §3.4 refused need-triggered injection and said starvation "is detected
outside the sim, as a group-by over `storybar.read` rows"; no such group-by is in `harness/`. (c)
`harness/soak.py::grade_mix` grades drift of the act mix and cost, not what is open.

**Against the apparatus.** F3 ("an explicit pacing target or tension variable with named inputs, a decay
rule and thresholds that a log can show") and F4 ("an alarm for the pacing mechanism running out of
suitable content") are the two rows a no-GM design is asked first. The design's ruled answer to pacing is
that nothing steers (strife R1; narration §3.4; the Light Function's "can never inject content"), and I
accept it. But refusing to *steer* tension is not a reason to refuse to *read* it: without the reading,
"the world generates drama when nobody is watching" has no observable at all, and F-WR-13's shape (opens
accumulate, closes are expiries) was found here by hand from Event-kind counts.

**Falsifier.** A harness command that prints, per season, the count of open situations by kind and how
many closed by an act. None exists.

**Minimal fix.** `09_WR_B_readings_of_closure_and_tension.md`, edits 2 and 3: `harness/storybar.py` gains
a `situations` block composed on the existing World-first stampers, and a per-season idle count.

### 3.5 Does character change the story? The ablation (apparatus E7)

Kreminski et al.'s one transferable experiment (E11.Q3): disable the system that is supposed to make
stories and see whether the stories get worse. Their Prom Week arm replaced social reasoning with random
choice. The tree already owns the equivalent control: `harness/decision_spread.py::apply_control` gives
every pursuit-holder the realm-mean pursuits and the realm-mean conviction, with `build_realm(goals=False)`
and `no_goals()` so no authored ambition is seated or read. `wrb_ablate.py` (§9 EB-01) runs the season loop
under that control and under the shipped build and reads both with the existing instruments. Control on the
probe itself: the shipped arm at seed 0 reproduces the first audit's season-1 hash `bacd687f…` and its
1,703 acts with 898 refused.

| reading, two seasons | seed 0 shipped | seed 0 flat | seed 1 shipped | seed 1 flat |
|---|---|---|---|---|
| acts · executed | 1,703 · 805 | 1,639 · 760 | 1,706 · 830 | 1,655 · 826 |
| executed cross-person share | 12.5% | 14.5% | 11.8% | 13.9% |
| executed acts at cross depth 3 or more | 36 | 15 | 27 | 37 |
| consequence chain ends, depth 2 or more · 3 or more | 29 · 1 | 52 · 1 | 27 · 0 | 35 · 7 |
| `utter` + `commit` executed | 194 | 31 | 186 | 72 |
| `oblige` executed | 26 | 168 | 0 | 27 |
| `march` executed · fields met (`lost` + `unopposed`) | 3 · 3 | 7 · 7 | 3 · 3 | 23 · 23 |
| deaths · `matter.determined` | 0 · 0 | 0 · 0 | 0 · 1 | 1 · 0 |
| distinct executed-verb sets over 83 actors (largest shared) | 80 (2) | 66 (11) | 79 (2) | 80 (3) |

**Reading (F-WR-16, degrades narrative).** Two seeds and two seasons are a direction and not a measure,
and the arm removes two things at once (authored goals and per-person spread), so nothing here is a balance
claim. The direction is plain at both seeds: **with every person flattened to the realm mean and no
authored ambition, no story reading falls, and the world-changing acts rise.** The executed cross share is
higher flat at both seeds; consequence chain ends are higher flat at both seeds; marches that reach a field
go 3 to 7 and 3 to 23; the only death in the four runs is in a flat arm. What character visibly buys in
the shipped arm is 186 to 194 executed `utter` and `commit` acts (23% of everything executed), the
declaration of ambitions: beats by the definition of §3.1, and beats that change no one else's options.
The one reading that moves the expected way is the spread of what persons did (66 distinct sets against
80, eleven persons sharing one set against two) and it moves at one seed only.

Two explanations fit and the runs cannot separate them: the instruments are blind to what character
contributes (the first audit's F-WR-03, again), or the authored goal layer spends the scene budget on
declaring and not on doing. Either is a defect; the second is CHAR's subject and is cross-listed to
`02_CHAR_goal_lean_on_its_own_question.md`. **Falsifier:** a reading on which the shipped arm exceeds the
flat arm at three seeds. None of the nine readings above does at two. Step 7 of §3.8 makes the arm
standing so every later instrument is asked this question first.

### 3.6 How the world should generate drama when nobody is watching

The literature converges on five conditions, and the design set agrees with all five; the table says which
the shipped realm meets. "Converges" means two or more independent sources of different kinds.

| condition | sources | Valoria's ruled form | shipped realm |
|---|---|---|---|
| **1. Conflicting drives and specified relationships** | Aylett (T01.Q2); Jenkins (T05.Q3); Kybartas (E05) | pursuits, convictions, `incompatible` affiliation pairs, seats with one holder | **met in data**: 46 of 83 hold a conviction; whether it changes what happens is §3.5 |
| **2. Events outside the characters' control, with duration, that overlap** | Aylett (T01); Sylvester as reported (G14.Q4); the churn audit's "wiring, not redesign" | AX-5's three motions; weather, bodies, the Calamity as matter (#457 §4.1) | **not met**: all three forcings ship at their controls (first audit F-WR-04), and the one that is scheduled to flip is drawn independently each season (§5, F-WR-19) |
| **3. Stakes that are rivalrous and irreversible** | Short on Ryan (E12.Q4: "things characters could want, lose or fight over"); Schmid via Lessard (irreversibility) | one seat, one hold, a body, a razed Site | **thin**: deaths 0, 1, 2 in six seasons; one `rung.razed` in two of three seeds |
| **4. A close that someone does** | Façade's beat needs an effect; strife R6 ("terminates or resolves with a concluding outcome, or it is not a flow") | `determine`, `covenant`, `fight`/`accept`, `seize`, `pardon` | **not met** (first audit F-WR-01; F-WR-13 here) |
| **5. A trace another agent can meet and act on** | Fernández-Vara (G04.Q2, Q4); Jenkins (T05.Q4); Aylett's off-stage reporting (T11.Q3) | WITNESS, `tell`, Records, fabric bands, `deeds_judged` | **met and the strongest part**: same-season cross-person answers 128, 160, 158 (first audit S2) |

Three things follow that the first audit did not say.

**(a) "Hurt but not kill" is an authored property, and the engine has its mirror image.** Sylvester's rule
(G14.Q3, secondary source) is that the generator damages a colony without ending it, so decline is a long
arc that can reverse. Valoria has no generator to damp, and rightly; but its hunger pass does the opposite
of the rule by accident: a body only falls (H-211), so a cohort that has been hungry once never recovers
without `tend`, and a first-season famine that is a build artefact (first audit F-WR-10) is permanent
damage. The lawful equivalent of the damping rule is not a director. It is that **every world motion has a
rising half**: fabric that can be restored (built), a body that mends when fed (R-13), a larder that
refills (built), a season after winter (unbuilt, CP-T10-03). Where a motion only falls, the world is a
ratchet and its drama is a countdown.

**(b) The off-stage problem is solved in the engine and unsolved for a player.** Aylett's Holodeck needs
"gossip or a recap voice-over" for what happened where the user was not. The season loop simulates
everything off-stage and delivers it by WITNESS and `tell`; what it lacks is the recap, which is the
focalized journal (NM-W5). This is the one place the July design's "re-light renders the catch-up
retroactively … always focalized" (`v2_churn.md` §4) survives intact as a requirement: a returning player
must read what his person learned, from whom, as of when (narration-mechanisms §3.3 rules 1 to 3).

**(c) The realm's cast is too large to follow and the strand reading makes it larger.** Sylvester's
remembered-cast argument (G13.Q1: about 12 named colonists against Dwarf Fortress's 200) is a secondary
report with no measurement, so it is a shape. The shape applies: 83 persons, strands of 17 to 55 doers,
one strand by season six. The strife design's capacity rule ("n+1" per rung, A1) is the engine's lawful
form of a remembered cast, a subtract-only ration of what a reading *presents*; it is the Light Function's
only surviving descendant, and it is the right one to keep. It has no reader (first audit §5.3). It should
get one before it is tuned: the journal.

### 3.7 What survives of the July design, and what must not be rebuilt

`narrative_engine_design_v1.md` and `v2_churn.md` are ratified (ED-IN-0011) and written on the Key
substrate that ED-IN-0232 retired; `CURRENT.md:36` still names v2 as the head (first audit F-WR-12). Read
whole, eleven of its objects have a fate at HEAD:

| July object | fate at HEAD | where |
|---|---|---|
| `causes[]` on everything, total accounting | **kept and stronger**: every Event carries causes; refusals are Events | `state/world.py::write` |
| invariant (i) proximate connectivity | kept as a reading | `storybar.read`'s `cross` edges; the edge null (first audit E-10) |
| invariant (iii) player-rooting / tie-graph casting | kept, re-expressed person-side | `questions_for`, `reach` |
| invariant (ii) light-inertia, anti-strobe | **dropped**; nothing rations attention across seasons | `question_aggregation_rule = "first"` |
| invariant (iv) liveness (no proximate climax forecloses unsurfaced) | **dropped**; expiry forecloses silently (F-WR-13) | `matter.lapsed` |
| the Light Function (subtract-only ration) | survives only as `flow_capacity`, `presented`, `slot_rank`, unread | `world_q.py:4747-5556` |
| forecast field, `stake_horizon`, never-a-meter | **not built, and should stay so**: a person-side estimate is CR-21/§C.11's; a world-side forecast is an actor-invisible apparatus with no consumer | — |
| R-AI (no actor reads a forecast) and F8 (anti-self-fulfilment control) | survives as the strife §6 guard: stamp on against off, terminal-code histogram | H-274 |
| arc-vector templates, COLLISION priors, the 138-arc corpus | **retired with the corpus**; the cases under `engine/season/cases/` are the successor as a *specification*, not a compile target | `corpus_run` |
| claim grammar (evidence, precedent, commitment, bluster) | alive as SC's and FI's proposals in this suite | `05_SC_evidence_and_rebuttal.md`, `08_FI_05_evidence-interface.md` |
| anti-slop theorem: binding, consequence, scarcity, memory, range | binding and consequence hold by construction; **scarcity, memory and range have no reading** | this section |
| F1 any-seed regression (five seeds, chronicles differing in actors, stakes, outcomes) | unbuilt; `storybar --draw-seeds` compares chain multisets, not tellings | first audit E-02 |

The row that matters is the fourth from the bottom. The July design's failure, on its own later audit
(`.audit/2026-08-08-world-churn-audit/06_master_synthesis.md` Part VII.0, "J-O"), was to assume a mesh of
declared consumers was the engine; the season loop is the answer J-O proposed ("keep [events] as an
append-only … causality log, drive churn through the boundary directly"). So nothing here proposes a
detector, a director, a salience field or a template compiler. What the July design had right and the loop
lost is narrower: **liveness** (a close should be surfaced to someone before a clock takes it) and
**focalization** (every telling has a viewpoint). Liveness has a lawful form in this architecture, and it
is a question, not a trigger: a matter within one season of lapsing is an occasion for the seat that could
hear it (`matters_awaiting` exists; whether it ranks is `attention_key`'s). That is SC's and CHAR's edit;
it is listed in §3.8 step 3 so the dependency is on file.

### 3.8 The shortest faithful path from the present substrate

Ordered. Each step names its owner, its gate as an execution artifact, and which apparatus rows it moves
from `paper` or `fail`. Steps 1 and 2 are this lane's and are hash EQUAL.

| # | step | owner · file | gate | moves |
|---|---|---|---|---|
| 1 | Read closure and tension: closes by act against by clock; open situations per season; idle persons | WR · `harness/strife.py`, `harness/storybar.py` (`09_WR_B_readings_of_closure_and_tension.md`) | the block prints at seeds 0 to 2 and a planted world with one determined and one lapsed matter reads 1 and 1 | F3, F4, C2, C3 |
| 2 | A chronicle that says what each act was about, starts from what closed, and breaks ties by rarity | WR · `harness/chronicle.py` (`09_WR_B_chronicle_that_tells.md`) | a planted `detain → determine → fight` reads back from the death with three subjects; the seed-0 render names what was concealed | T06.Q1, E10.Q1, E12; prepares D7 |
| 3 | The closing verbs execute; a matter about to lapse is an occasion | PC, SC, FA, CHAR (their proposals in this suite) | step 1's block: closes by act above closes by clock at some seed | condition 4 |
| 4 | Weather with memory, then the year, then the wound | WR · data (`09_WR_B_weather_with_memory_and_the_year.md`; first lane's `09_WR_world_motion.md`) | a two-season shortfall in one territory under the live arm; step 1's incident count above zero | condition 2; G14.Q4 |
| 5 | The focalized journal | NM-W5 (CHAR/GO), on step 2's fields | NM-W5's own three falsifiers | T11.Q2, D6, H3 |
| 6 | The reader test | Jordan or a rater, ten minutes, one seed's journal | a reader who did not build it writes an account containing one situation, from logged facts only | D7, E04.Q4 |
| 7 | Character ablation as a standing arm | WR · `harness/storybar.py`, composing on `decision_spread.apply_control` | §3.5's reading at three seeds | E7 |

What is deliberately absent: a pass bar for "a story happened". Compton's and Smith's point (P01, P02)
and the first audit's null (no game certifies generated content as good) stand: the instruments can show
that closure, tension, situations and tellings are *zero* or *indistinguishable from a control*, which is
the failure the project needs to be able to see; they cannot certify the opposite, and step 6 is the only
row that can.

## 4. Threadwork as a registered module: the design set in full, its playable form, its season integration

<!-- SECTION-4 -->

## 5. World motion: travel, survival, weather and the Calamity, as playable and as ambient

<!-- SECTION-5 -->

## 6. The 48 primary hole rows not read by the first lane, dispositioned

<!-- SECTION-6 -->

## 7. Capability-authoring consequences

<!-- SECTION-7 -->

## 8. Proposals written by this addendum

<!-- SECTION-8 -->

## 9. Evidence log

<!-- SECTION-9 -->

