# CORE — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

Scope: the season loop's spine — `engine/season/loop/{driver,calendar,census,deliberate,encounter,effects,effects_shared,matter,predicates,resolve,sides}.py`,
`state/`, `seam/`, `manifest/`, `data/`, `queries/{cache,inputs}.py`, the YAML registries the loop opens
(`verb_table`, `write_matrix`, `rosters`, `requirements`, `hole_register`) and the `harness/` instruments.
Subsystem effect bodies, `decision/` and the strife harness are other lanes'; they are cited only where the
core's contract with them is the thing judged. **What was read in full, what was read as code-only, and what
was not read is stated in §12; a claim about a file not read in full is marked `[UNVERIFIED]`.**

## 0. Verdict

**The core is a sound basis for a dynamic emergent narrative game as a *kernel* — one clock, one write
gate, one fold, one causal log, seeded and replayable, all of it observed running — and it is not yet a
basis for *judging* that game, because its instruments do not test the stories it is meant to produce.**
The single largest obstacle is on the measuring side, not the mechanism side: the 143-case arc and
character corpus is executed as 143 parameterisations of one template world (`harness/corpus_run.py:467-662`),
35 of its NPC need-rows and none of its ARC need-rows are bound to anything checkable (`harness/exercises`
run, §12), and the two requirement rows that claim the loop's central property — R-01, R-02, decisions
propagate and shape later decisions — read `met` on a single-seed reading from a 75-minute instrument
whose own positive control does not fire. Behind that sits one mechanism defect that will bind as soon as
anyone runs long: the event log, the substrate every narrative instrument reads, is more than four-fifths
memory-fade bookkeeping by the eighth season of a three-person world (F-CORE-01), and its cost grows
with history. The kernel's rules (token, matrix, basis, receipt, referential `causes[]`) held against
every attack tried here. The size charge resolves the same way: the engine is small — about 14,000
executable lines of game code — and what is large is narrative carried in comments, tests and a register.

## 1. What it is, as coded

### 1.1 The loop (read at `loop/driver.py:388-563`)

`SeasonDriver.season(choose, question, actorless, contest_max_depth, host)` is the game's only clock:

1. `w.draw = 0`; season-local driver state cleared (`driver.py:468-473`).
2. **CALENDAR** once (`loop/calendar.py:36`): fires `w.dates` due at this tick, forms docket items.
3. **MATTER** once (`loop/matter.py:284`): actorless events, term maturation, docket lapse, claim decay,
   subsistence and production (two module `step_call` entries, `matter.py:45-47`), body falls and deaths,
   travel, site wear with band crossings; ends frozen.
4. **R rounds**, `R = fixtures.scene_budget` (`driver.py:479`). Each: `_rehome`; freeze; **DELIBERATE**
   (no token; per person `sense` → `assemble` a View → `choose`; scenes queued and released at most
   `scenes_per_round` per round, `deliberate.py:131-320`); **RESOLVE** (token `ACTS`; order = stratum, then
   a seeded hash, `resolve.py:51-58`; survive → obstacle gate → eligibility/`requires` (`_admits`) →
   contest, graded inquiry or plain fold → effect through `World.write`; staged site deltas summed and
   clamped once, `resolve.py:1163-1198`); **ENCOUNTER** (fights the acts RESOLVE declared and deferred,
   `encounter.py:43`); events appended to the one log; **WITNESS** (token `INTERIOR`).
5. **CENSUS** once: individuates a person only for a `person.demanded` Event (`census.py:46-100`).
6. `world_q.endings_reached(w)` (a read); `w.tick += 1`; returns `{acts, events, rounds, deposits, hash, endings}`.

The seven steps and RESOLVE's helpers are module functions bound onto the class (`driver.py:597-620`).

### 1.2 State and the gate

`World` (`state/world.py:357`) owns six entity stores, `dates`, `docket`, an append-only `EventLog`
(`state/log.py`) and `ActStore` (`state/acts.py`). Tenures live on their subject Person; `w.tenures` is a
read-only concatenation rebuilt at every access (`world.py:455-471`).

`World.write` (`world.py:1138-1555`) is the single write path: a real `Token` at the current tick; the
`write_matrix.yaml` row admits the step and class; `social: true` only by `driver="Act"`; a MATTER write
on an emitting row names a declared kind; then the gate opens, tenures are snapshotted, the change
applies, an unauthored tenure change is refused against fourteen named bases
(`state/gate.py:1137-1481`), a `Change` that moved none of its named subjects is refused (`NoOpReceipt`),
receipts are minted and the Event emitted. `EventLog.append` refuses a receipt the gate did not mint and a
`causes[]` id that is no prior Event, no stored Act and not `ROOT` (`log.py:64-101`).

Ids and draws are `H(seed, tick, subject, purpose)` (`state/ids.py:16`); `content_hash()` folds stores,
docket, tenures and the whole log (`world.py:1667-1726`).

### 1.3 Seam, manifest, data

`seam/contest.py::contest` dispatches a contested act to a provider found by
`manifest.resolve("contest", prize)`; the four providers (`seam/wrappers/{sigma,combat,mass_battle,fieldwork}.py`)
build a typed input (`queries/inputs.py`), call a module entry the registrar recorded from
`references/module_contracts.yaml` (`manifest/registrar.py:77-129`) and return a dict the one ladder
reads (`seam/ladder.py:225-272`). `SeasonDriver.__init__` runs `load_all()`, the registrar and six
refusals on every construction (`driver.py:255-302`).

### 1.4 Execution evidence (commands and outputs in §12)

| what ran | seed / seasons | result |
|---|---|---|
| `register --requirements` | — | 0.5 s; `met 3 · not_met 1 · partial 5`; shape check over `status:` strings |
| `tools/m1_acceptance.py --summary` | 20260819 ×1 season ×2; 24 seeds ×4 + 2 populated ×1 | stub calls 0; same-seed hash equal; nine met 3/9 (self-declared DOC-DERIVED); 0 invariant violations over 49,735 events; verdict NOT MET |
| `harness.corpus_run` | seed 0, 143 cases | `RUNS-UNDECLARED 103 · SPAN-UNAUTHORED 40`; R1/R3/R4/R5 pass 143/143; planted control False→True; verbs executed 23 of 67; degrees Failure 1,552 of 2,152; claims firsthand 93,696, told_by 64 |
| `harness.headless --case NPC-088 --seasons 2 --seed 0` | seed 0, 2 | rounds 5/5, acts 16/17, events 17/92, hash `5405522c…` |
| growth probe (headless world, 8 seasons) | seed 0 | events per season 17 → 982; `claim.decayed` 938 of 1,164 new log entries in season 7; log 4,621 for 182 acts |
| depth-cap arms 1/2/3/7; one-round arm | seed 0, 2 | hash identical at every depth; `scene_budget=1` arm differs (acts 1/4 against 16/17) |
| `harness.exercises` | — | `NPC: 35/292 rows authored (32/122 core)`; `ARC: 0/611 (0/300 core)` |
| `register --check` | — | 22 s; 352 rows; R2 27 violations, G6 3; tier-0 `absent` on H-49, H-62, H-98, H-101, H-105, H-108 |

## 2. Steelman (ranked by the weight each bears)

1. **One write path that can refuse, and does.** Every mutation in the spine goes through `World.write`
   with a token only `mint_token` constructs (`driver.py:80-98`); DELIBERATE receives none, so a chooser
   — a player's callback included — cannot write. *Attack:* searched for a second path. Found three
   direct `w.log.append` sites in MATTER (`matter.py:129`, `:258`, `:325`) and the round's own append
   (`driver.py:536`); all append Events with `changes=[]` or events the fold already produced, none
   mutates an entity. *Survived.* The freeze flag itself is read once (`deliberate.py:80`) and is not
   what protects the map; the absent token is.
2. **A causal log with referential integrity.** `Event.__post_init__` forbids `causes=[]`; the log
   refuses a cause that resolves to nothing. This is the edge an arc is made of. *Attack:* m1's sweep
   (24 seeds × 4 seasons, 49,735 events) and the corpus run found no violation; I found no append that
   bypasses `EventLog.append`. *Survived* — as integrity. What the log *contains* is F-CORE-01.
3. **Seeded and replayable.** Same seed, same hash, observed twice (m1 row 2; corpus `R4` 143/143).
   *Attack:* looked for an unseeded generator. `seam/wrappers/sigma.py:533` falls back to
   `random.Random()` when handed no `rng`; the driver always hands one (`resolve.py:833,893`), so the
   door is open only to a harness caller. *Survived on the run path; narrowed to it.*
4. **The round tick is behaviourally real** (R-03). The one-round arm produces a different season
   (1 act against 16; 34 deposits against 159 over two seasons), so later rounds are not a relabelling.
   *Survived.*
5. **Data-driven verbs with refusals at boot.** A verb row with a precondition nothing evaluates, an
   effect nothing carries, an unclaimed prize or an unregistered provider stops driver construction
   naming the row (`manifest/registry.py:330-716`). *Attack:* the corpus run reports `1 have no
   predicate/effect` of 67, declared by note, not silent. *Survived.*
6. **Modules reached by composition row, typed in and out.** `registrar.py` refuses a doubled entry and
   a row naming no verb. *Attack:* the provider-to-seam hop is an untyped dict read by key presence
   (F-CORE-10). *Survived for the module boundary; narrowed at the seam boundary.*
7. **Instruments that refuse to flatter.** `corpus_run` prints `RUNS-UNDECLARED` and `NOT-COMPUTABLE`
   rather than a pass; `m1_acceptance` labels its doc-derived row. *Survived* — and it is the reason
   F-CORE-02 could be found from the instrument's own output.

## 3. Adversarial findings (worst first)

### F-CORE-01 · degrades narrative, and blocks long arcs · the log is mostly memory-fade bookkeeping

- **Claim.** MATTER writes one `claim.decayed` Event per live claim per season
  (`loop/matter.py:471-501`). The log therefore grows with ledger size, not with what happened, and
  `content_hash()` re-walks the whole log every season (`world.py:1709-1725`).
- **Evidence / falsifier run.** Headless world (three persons), seed 0, eight seasons
  (`probe_growth.py`, §12): new log entries per season 86, 182, 310, 481, 621, 790, 987, 1,164, of which
  `claim.decayed` 0, 69, 159, 276, 439, 583, 747, 938. Acts per season stay between 16 and 30. After
  eight seasons: 182 acts, 4,621 events, 1,120 claims, 15,774 trace rows. `content_hash` is 0.63 s of a
  2.65 s profiled season. The falsifier was the same run showing a flat event count; it did not.
- **Touches.** R-01, R-02 (what a propagation instrument must sift), R-03 (cost of a round), every arc
  whose span exceeds six seasons — `corpus_run.py:72` clamps at `MAX_SEASONS = 6` and says why: *"the
  flood … makes that unaffordable"*.
- **Narrative consequence.** A reader of the log — `harness/chronicle.py`, a future story sifter, a
  player-facing "what happened" — reads four fade records for each thing a person did or learned.
  Cross-season arcs are the ones the cost forbids running.
- **Minimal fix at the owner.** Make fading a read, not a write: `Claim.confidence` as deposited, and
  `person_q` computing present confidence from `(confidence, when, tick, claim_decay)`; one Event only
  when a claim reaches zero or is evicted. H-12's ruling (a MATTER *write* emits) is kept, because the
  write is gone. Proposal `01_CORE_claim_fade_as_read.md`.

### F-CORE-02 · blocks the arc charge · the corpus runs one template 143 times and checks no case need

- **Claim.** `build_at` (`harness/corpus_run.py:467-662`) builds every case as: a rung chain from the
  case's `scale` upward, one Site per yielding kind, persons `p_a…` seated from a cast overlay where
  one exists, pursuits from `seed_pursuits(seed, case id, pid)`, a ring of `OUGHT` propositions each
  about the next person with one predicate from `wants_of(case)`, and a lapsing date for the nineteen
  `forced_by_threshold` arcs. Nothing in `season_requires`, `who_acts`, `knowledge` or `ends_when`
  shapes the world or is checked against the run.
- **Evidence / falsifier run.** `corpus_run`, seed 0: statuses are `RUNS-UNDECLARED` 103 and
  `SPAN-UNAUTHORED` 40, with `R2`, `A2`, `A3` printed `NOT-COMPUTABLE`. `harness.exercises`: 35 of 292
  NPC rows and 0 of 611 ARC rows bound. Overlay rows exist for eight cases (NPC-002, -005, -010, -012,
  -075, -086, -087, -088). The falsifier would be an ARC row with an `exercises:` binding; there is none.
- **Touches.** R-01, R-05, R-06 as measured on the corpus; the whole of §13.
- **Narrative consequence.** No statement of the form "the engine can simulate ARC-nn" is available
  from any instrument. `DISTINCT EXECUTED SETS 136` measures variety between seeds of a template.
- **Minimal fix at the owner.** A typed `setup:` and `beats:` pair per case, read by `build_at` and by
  a beat matcher over the log; proposal `01_CORE_case_setup_and_beats.md`.

### F-CORE-03 · blocks honest reading of THE NINE · statuses are strings; two `met` rows lack a control

Per row, from the `measured:` block opened in `engine/season/requirements.yaml` and the instrument run
or reasoned from:

| row | status | instrument named | what supports the status | verdict |
|---|---|---|---|---|
| R-01 | met | `corpus_run` R3 rows + planted control | R3 143/143 and the control re-run here. But the block's own `met` criterion is the degree-sweep reconvergence reading (`none` 80.45 %, `actor` 64.38 % at `2x3`, tree `2ca90dce7`), one seed, no noise estimate, and its positive line reads *"detected OVER THE BASELINE on ALL 4 plants: False"* | execution artifact exists; **not a measurement with a control** (§0.1 pt 4). R3 shows an edge can exist on a template world; it does not show a decision reaching a later decision |
| R-02 | met | `proposals/2026-09-04-degree-sweep/wd_collect.py` after 36 chunk cells (about 75 min) | *"rests only on the committed `WD_LOG.txt` reading"*; cells untracked; same single seed, same undetected plants | execution-derived, **not reproducible inside a session and without a working positive control**; `[UNVERIFIED by re-run]` |
| R-03 | met | `headless --case NPC-088 --seasons 2 --seed 0` + `pytest -k test_u2_` | headless re-run here (rounds 5/5); the one-round arm differs (§1.4) | **supported by execution** |
| R-04 | partial | `aperture 4 0` | recorded readings at seeds 0–2 (`found`/`build` execute 0 at seeds 0, 1) | supported as `partial` by the block's recorded runs; `[UNVERIFIED this tree]` (run stopped, §12) |
| R-05 | not_met | `corpus_run` "WHERE THE n GO" | re-run: 23 of 67 executed, 13 only refused, 30 never attempted | **supported by execution**; the block's last figure (20 of 56) is stale against the tree |
| R-06 | partial | `corpus_run` "RANKING DISCRIMINATION" | re-run: 9..14 of 14 celled candidates score non-zero | supported as a reading of the ranker at tick 0, *"not of play"* (the block's words) |
| R-07 | partial | `pytest -k 'choose_receives_no_world or a_view or r7_two_persons'` | tests exist by name (`register --requirements` checks that); not run (suite is a close step) | structural half enforced by type (`carriers.py:504-509`); behaviour half `[UNVERIFIED]` |
| R-08 | partial | `corpus_run` | same line as R-06; sampler test not re-run | supported as `partial` |
| R-09 | partial | `aperture 4 0` | block: *"NO TWO PERSONS SEPARATE … the two reports are byte-identical"*, seed 0 only | supported as `partial`; the corpus run agrees in kind (pool default everywhere) |

- **Claim.** `register --requirements` verifies that each row has a status word, a `measure:` naming an
  existing file or test name, and non-empty `measured:` text (`harness/register.py:631-701`); CI runs
  exactly that (`.github/workflows/valoria-ci.yml:447`). Nothing executes a `measure:`. The `measured:`
  fields total about 135,000 characters; R-01's begins *"[SUPERSEDED by the IN-50 (B-I) paragraph at the
  end of this block"* and runs to 35,912.
- **Falsifier.** A row whose current reading can be found without reading superseded paragraphs. None.
- **Minimal fix.** A typed `reading:` record per row (command, tree, seed, seasons, control, result,
  date), history left to git; R-01 and R-02 re-pointed to a session-affordable causal-chain reading
  with a planted control. Proposal `01_CORE_requirements_reading_record.md`.

### F-CORE-04 · degrades narrative · in computed play most graded acts fail and almost nothing is told

- **Claim / evidence.** Corpus run, seed 0: 1,552 of 2,152 graded outcomes are `Failure` (72 %);
  `argue` 660 of 947. Claims by source: `firsthand` 93,696, `told_by` 64; 49 of 442 persons hold a told
  claim. The core's part of the cause: `build_at` seats no `capability` (`corpus_run.py:537-540` copies
  an overlay's, which one case has), so `seam/wrappers/pool.py:94-100` returns `pool_default` for
  everyone.
- **Touches.** R-06, R-07, R-09. Owner of the capacity source: CHAR / SC lanes (research T-IN-1). The
  core edge is the case builder (F-CORE-02's proposal carries cast capability in `setup:`).
- **Narrative consequence.** Knowledge moves by presence, not by speech; persons are distinguished by
  what they want and by the draw.

### F-CORE-05 · blocks "playable" · the play surface is a seam with no client

- **Claim.** A player's entry is `harness/play_surface.py::dispatching_chooser` (a seven-line
  dispatch), `decision/sheet.py`'s spaces and `queries/inputs.py::PlayHost` for a fight. No module under
  `engine/season` reads input (`grep "input("`: none); every `__main__` is an instrument.
  `dispatching_chooser` has test callers and one docstring example (`harness/military_menu.py:8`).
- **Missing, by the standing requirement:** a scenario seed a person can enter; a loop that shows the
  sheet and takes picks season after season; outcome legibility (`driver.season` returns counts and a
  hash; nothing renders what the player's act caused); stakes and an end condition the player can read
  (`world_q.endings_reached` is computed and returned, `driver.py:549`, and shown by nothing).
- **Touches.** All nine as *play*; R-03 in particular (Jordan: only players need the scene whole).
- **Minimal fix.** A headless player loop in `harness/` composed from what exists; step 4 of §8.

### F-CORE-06 · degrades narrative for seat-holders · the round count caps a budget the design varies

`rounds = scene_budget` (`driver.py:479`) and at most `scenes_per_round` scenes are released per round
(`deliberate.py:287`), while `decision.budget` may exceed `scene_budget` by office. The excess cannot be
spent (H-10's cite measured 5 → 6 with five releasable). Open as IN-14 (*BUILD … MORE ROUNDS*);
verified open in code. Touches R-04: the persons whose acts are strategic are the ones capped.

### F-CORE-07 · hygiene · the contest depth cap decides nothing

`contest()` takes `depth`, `max_depth` and `extension` (`seam/contest.py:182-186`); the one caller passes
`depth=0` (`resolve.py:847`); `extension` is read nowhere; nothing recurses. **Falsifier run:** headless,
seed 0, two seasons, seven graded events, `contest_max_depth` 1, 2, 3, 7 — one hash. H-87's swept arms
are identical by construction, the fake control `CLAUDE.md` §7 names. Thirty-one non-test references
carry the argument. `_contest` returns `[]` on `ContestError` (`resolve.py:861-863`), an act with no
Event at all, reachable only if a caller passes a cap of zero.

### F-CORE-08 · code matter · size (the special charge)

Measured with `sloc.py` (tokenize + AST; §12) over `engine/season/**/*.py`:

| slice | lines | code lines | comment-only | docstring |
|---|---|---|---|---|
| all | 127,105 | 60,008 | 23,021 | 31,032 |
| tests | 71,169 | 37,231 | 12,468 | 12,849 |
| non-test | 55,936 | 22,777 | 10,553 | 18,183 |
| of which `harness/` | 16,041 | 8,795 | 2,413 | 3,379 |
| of which `loop/` | 9,673 | 3,081 | 2,604 | 3,462 |
| of which `state/` | 5,742 | 1,790 | 1,310 | 2,245 |

- The game code (non-test, non-harness) is **13,982 executable lines**. By bytes the non-test tree is
  1.18 MB of code and 2.45 MB of comment and docstring. `loop/driver.py` is 170 code lines of 620.
  `hole_register.yaml` is 1.32 MB — larger than all non-test code — with 638,014 characters in `cite:`
  fields and one cite of 42,845. `tests/test_season_shape.py` is 17,880 lines in one file.
- **So the charge "127,000 lines against what it does" is answered: the mechanism is proportionate; the
  prose is not.** The prose is history, written where the rule should be: *"THIS DOCSTRING WAS STALE THE
  MOMENT L5 LANDED AND SAID SO FOR A DAY"* (`driver.py:11`).
- **Cost, observed.** (a) Stale claims beside live code: `seam/contest.py:222-233` says wiring the
  engines is out of scope, above the line that dispatches to them; `driver.py:110-112` says the seam
  does not return yet, thirty lines above the paragraph retracting it; `loop/matter.py:663` says
  `census` counts `_subsistence_shortfall`, which only `harness/populated.py:2012` reads;
  `resolve.py:154` traces a refusal as H-33 where its own comment says the cause is now H-75. (b) Tests
  that read source text: the driver binds steps so that `inspect.getsource` reaches bodies eight tests
  scan (`driver.py:574-581`); a test asserting on a comparator *string* cannot observe the behaviour it
  excludes (§0.1 pt 2). (c) Reading cost roughly triples.
- **Fix.** Per file touched for another reason: keep the rule and one line of why; history is the
  commit. No sweep, no guard (§0.1 pt 5).

### F-CORE-09 · code matter · per-access scans on the hot path `[timing on the realm UNVERIFIED]`

`w.tenures` sorts persons and concatenates on each access (`world.py:455-471`) and is read inside loops:
`containment.parent_of` once per ancestry step (`containment.py:33-37,131-133`), `gate.seat_hold`,
`resolve._eligible` (`resolve.py:131`). `attribution.event_by_id` and `matured_terms` scan the log
(`attribution.py:238-277`); `matter.py:355,369` scan it per maturing record. `TRACE.rows` is a
process-global list appended on every write, event and query and cleared only by `harness/soak.py:292,412`.
The requirement file records the four-season realm run at *"about 25 minutes"*. I could not complete
that run on a contended machine (§12), so the realm figure is the file's, not mine.

### F-CORE-10 · hygiene · the seam reads provider results by key presence

`degree_of` branches on `"wound_state" in result`, `"attacker_wins" in result`, `"net" in result`
(`seam/ladder.py:247-264`); provider statuses are strings (`contest.py:43,100-115`). The combat provider
discards the driver's `rng` and seeds its own from `H(...)` (`seam/wrappers/combat.py:388-397`),
deterministic but a second derivation of a generator the driver was to construct once. Three ladders
(wounds, field bands, dice margin) are ruled (Jordan, 2026-09-03, recorded at `ladder.py:151`); accepted.

### F-CORE-11 · hygiene · two gate conformance gaps already filed, verified open

A closure write (`apply=`) is not observed before and after and still mints a receipt with `delta=None`
(`world.py:1394-1395,1494`) — H-145 / NM-W9. `EventLog.append` checks no kind (`log.py:64-101`), and
MATTER's crossings append literal kinds directly (`matter.py:126-129,256-258`) — H-220.

## 4. Code matters

- **Ownership and duplication.** One fold, one gate, one ladder, one pool reader: confirmed at their call
  sites. Second owners found: the generator in the combat provider (F-CORE-10);
  `World._subsistence_shortfall`, a world attribute set outside `__init__` and outside `content_hash`
  (`matter.py:666`), read by a harness only; the Event-kind check, owned by `_act_events`
  (`resolve.py:1228`) for acts and by `World.write` for writes, with the log itself checking nothing.
- **Dead or unreached.** `extension`, `depth`, `ContestError` (F-CORE-07); `_eligible`'s `presence:`
  arm, which always declines (`resolve.py:142-156`); `World.boot`'s `check_roles`, called by two probes
  and three tests and by no run path (`driver.py:262-274` says so itself).
- **Seam fidelity.** Module entries: typed input, typed outcome, reached by composition row — holds for
  `social_contest` (`Margin`), `fieldwork` (`Findings`) and the settlement step calls
  (`SubsistOutcome`, `ProduceOutcome`), each type-checked on return (`sigma.py:535`, `fieldwork.py:73`).
  Personal combat's entry returns a dict (`combat.py:398-401`) `[04 row not opened: UNVERIFIED against
  Layer 1's text]`.
- **Determinism.** Holds on the run path (§2 item 3). `PYTHONHASHSEED` is not needed by the hash itself
  (blake2b over canonical bytes, `world.py:279-340`); set anyway per the brief.
- **Test strength.** Not assessed by running (pytest is a close step). By reading: the refusals have
  execution falsifiers named at their sites; the source-text tests (F-CORE-08 b) are the weak class.
  43 test files were listed for this lane; none was opened `[SKIPPED, §12]`.
- **Performance.** F-CORE-01 and F-CORE-09. The first is structural (cost grows with history); the
  second is constant-factor.

## 5. Design matters

- **Agree (intent, ruling, code):** only a person acts, a seat enters by `Act.via` (`resolve.py:78-81`,
  `deliberate.py:315-319`); no social quantity moves at MATTER (`world.py:64-107`); a crossing emits and
  produces no outcome (`matter.py:132-135`); the scene is the budgeted unit and five the number
  (RULED, H-35); refraction is receiver-side (RULED, H-36); a contest is a dispatch to a subsystem
  (RULED). Accepted as binding and not re-raised.
- **Disagree, and the game follows the code:** budget varies by office in intent and is capped by the
  round count in code (F-CORE-06). "Every MATTER write emits" is honoured so literally that fading
  dominates the log (F-CORE-01).
- **NERS cuts.**
  - *The depth cap (`contest_max_depth`).* N: removable with no change in play (hash identical at four
    values) — fails N in every direction tried (top-down: no rule reads it; bottom-up: no provider reads
    it; lateral: no sibling step passes a depth). What the cut loses: the refusal that would fire once
    nesting is built. E, last: overhead with no outcome to intuit.
  - *Per-claim decay Events.* N: the fade itself is necessary (R-07: memory); the *Event per fade* is
    removable without worsening play, since `claim.decayed` deposits nothing a person acts on
    `[UNVERIFIED: `undeposited_kinds` not opened]`. S: fails "zooms out well across scales" — its cost
    scales with ledger size times seasons. The cut loses a causal antecedent for each fade, which no
    arc in the corpus asks for.
  - *The round tick.* Survives: R (strategic sequencing within a season), S (pauses correctly: ENCOUNTER
    is the one step that suspends, `driver.py:434-443`). A cut would lose R-03.
  - *The write gate's fourteen tenure bases.* Survives N from below (each basis has an effect that needs
    it) and from above (L1/AX-4). E, last, against what N and R found: the single function is long
    (`gate.py:1137-1481`) but each arm is one rule; legible enough.
- **Design that exists only as prose (not yet game):** a nested DELIBERATE inside a contest (H-56's held
  half); `Coherence` (a matrix row and a gate branch, no writer); the player's explanation of an
  outcome; an ending shown to anyone.

## 6. Hole-register and workplan disposition, and resolutions

### 6.1 Disposition

"Verified" means checked against code or a run in this pass; "carried" means the listed status was read
in the row and not re-derived. Full rows were read to a bounded length (§12).

| item | listed | verified status | evidence | action |
|---|---|---|---|---|
| H-01, H-02 | ruled | closed | `data/matrix.py:162` (a row without `social` fails at load); `manifest/registry.py:641-716` | none |
| H-06, -07, -08, -09, -11, -26, -93 | assumption | open by design (declared, swept fixtures) — carried | sites named in each row | none |
| H-10 | assumption | **open, live** | `driver.py:479`, `deliberate.py:287` (F-CORE-06) | IN-14 as ruled (more rounds) |
| H-12 | ruled | closed, and the cause of F-CORE-01 | `world.py:1344-1354`; `matter.py:498-501` | proposal 01 |
| H-20, H-74, H-80 | assumption | carried | — | none |
| H-23, H-28, H-35, H-36, H-37 | ruled | accepted as binding | — | none |
| H-24 | ruled, empty cite | closed | writers `census.py:97-100`, `matter.py:277-281` | fill the cite |
| H-25 | absent | open | no row states a bound; nothing recurses | owner CR-98 |
| H-29, H-53 | assumption | closed as declared defaults — carried | — | none |
| H-30 | assumption, no site, no sweep | **closed in code, misgraded** | `resolve.py:51-58`: `(stratum, H(seed, tick, actor, "order:verb:id"))` | regrade `measured`, name the site |
| H-39 | assumption | open, nothing built (row says so) — carried | — | none |
| H-44 | absent | re-scoped — carried | — | FA lane |
| H-47 | absent, empty cite | **wrongly filed** | the row exists: `write_matrix.yaml:200-205`; the gate branch `world.py:1305`; no writer in any `.py` | refile as "row present, producer absent" |
| H-48 | absent, empty cite | **irrelevant** | no `disclosure` column in `write_matrix.yaml` or `verb_table.yaml` (grep) | close |
| H-49 | absent, tier 0 | open | no runtime writer of `weight` (row's cite; `carriers.py:741`) | mark the matrix row `unproduced` |
| H-50 | ruled | closed | `world.py:798-880` (`_grant_remit`), reader `resolve.py:122-124` | none |
| H-52, H-57, H-61 | closed by IN-43 | carried | — | none |
| H-56 | absent (half closed) | closed half verified by the one-round arm; held half **irrelevant until nesting exists** | `contest.py:182-300` never recurses | regrade; see R-11 below |
| H-59 | absent, empty cite | **superseded** | H-57: a grudge ends by `forgive` | close, citing H-57 |
| H-63 | assumption | closed for the registry | `effects_shared.py:42-49`; `resolve.py:452-461` | `speak`'s values: SC lane |
| H-75 | absent | open | `resolve.py:139-141` declines a `hold:<kind>` placeholder | none (no row needs it today `[UNVERIFIED]`) |
| H-76, -77, -78, -124 | assumption | open by design | `deliberate.py:243-259,287` | none |
| H-81, H-83 | ruled | closed | `resolve.py:1046-1047`; `resolve.py:1287-1298` | none |
| H-82 | assumption | **closed in code** | `log.py:84-87` (log ∪ act store); m1: 0 violations over 49,735 events | regrade `measured` |
| H-86 | assumption | closed as declared | `world.py:1344-1346` | none |
| H-89 | absent | open; CR-07 holds the cut | `Tenure.seat_rung` (`carriers.py:175-192`) already carries an act's scale | retire the column (CR-07) |
| H-109, H-254, H-344 | measured | carried (FA / SC mechanisms) | — | those lanes |
| H-145, H-220 | measured / absent | **open** (F-CORE-11) | `world.py:1394-1395,1494`; `log.py:64-101` | NM-W9; kind check at `EventLog.append` |
| H-153, H-154 | assumption | irrelevant to the core: fixtures nothing reads | rows' own `site:` | SC lane |
| B10-18b (CR-46…CR-54) | open | open; its base figure is stale | corpus run here: 23 of 67 executed (card: 36 of 60 pooled, 62 rows) | CR-46 re-reads first, as the card orders |
| IN-14 | BUILD | open | F-CORE-06 | build |
| CR-98, CR-99 | EDIT / BUILD | open — carried | — | none |
| CR-07 | HELD | open | as H-89 | release |
| NM-W9 | HELD | open | F-CORE-11 | none |
| IN-18, IN-44, IN-58, IN-30, IN-32, IN-36, IN-48, IN-52, CL-MGMT, CR-95, CR-97, CR-100…105, NM-W4…W8 | various | carried, not opened | — | none |

### 6.2 Resolutions decided (22)

| # | inconsistency / gap / unclear passage | resolution | ladder step | carried by |
|---|---|---|---|---|
| 1 | every fade is a logged write; the log is mostly fades | fading becomes a read; one Event at zero or eviction | 5 | proposal 01 (and §11) |
| 2 | a case's needs build nothing and check nothing | typed `setup:` and `beats:` per case | 5 | proposal 02 |
| 3 | `span_seasons` prose ("ongoing") runs as 2 seasons | an integer `span_seasons` plus `ongoing: true`; 86 rows re-authored | 5 | proposal 02 |
| 4 | sixteen cases wait on a player the runner never supplies | the runner seats a declared policy proxy through `dispatching_chooser` | 4 (`play_surface.py`) | proposal 02 |
| 5 | `measured:` holds superseded narrative; no current reading is findable | one typed `reading:` per row; history is git | 4 (`CLAUDE.md` §1's pointer rule) | proposal 03 |
| 6 | R-01 / R-02 read `met` on an instrument without a working control | re-point both to a chain reading with a planted control; status follows the reading | 5 | proposal 03 |
| 7 | R-05's block says 20 of 56; the tree reads 23 of 67 | the reading record carries the tree's figure | 3 (the instrument) | proposal 03 |
| 8 | depth cap: required of every caller, decides nothing | keep S39.3's refusal and the signature; strike H-87's sweep as a fake control; build nothing until nesting is designed | 2 | edit to H-87's row |
| 9 | H-30 graded `assumption` with no site | regrade `measured`, site `loop/resolve.py::_canonical_order` | 5 | edit to the row |
| 10 | H-47 says no row exists | refile: row present, producer absent | 1 | edit to the row |
| 11 | H-48 `disclosure:` column | close as never built | 2 | edit to the row |
| 12 | H-59 grievance clearance | close, superseded by H-57 | 1 | edit to the row |
| 13 | H-49 `(Person, weight)` tier-0 `absent` | mark the matrix row `unproduced` (the field `MatrixRow.unproduced` exists, `matrix.py:132`); regrade `measured` | 5 | edit to `write_matrix.yaml` and the row |
| 14 | H-56's held half | closed as irrelevant until a nested contest is designed; returns with its reader | 2 | edit to the row |
| 15 | H-82 graded `assumption`, behaviour enforced | regrade `measured` on the log's refusal and m1's sweep | 3 | edit to the row |
| 16 | H-24 empty cite | cite the two writers | 3 | edit to the row |
| 17 | four stale comments (F-CORE-08 a) | correct each at its site to the present behaviour | 5 | edits |
| 18 | `World._subsistence_shortfall` set outside `__init__`, described as read by `census` | initialise it beside `_departed` (`world.py:437`), clear it per tick, say "read by `harness/populated.py`" | 4 (`_departed`) | edit |
| 19 | `sigma.resolve` builds an unseeded generator when handed none | refuse (`InstrumentDefect`) when `rng is None` | 5 | edit to `seam/wrappers/sigma.py:533` |
| 20 | `_contest` returns no Event on `ContestError` | emit the row's refusal through `_refuse_party_gap`, as the `ContestRefused` arm two lines above does | 4 | edit to `resolve.py:861-863` |
| 21 | `scale:` column with no reader against CR-07's held cut | retire the column; an act's scale is its seat's rung | 5 | CR-07 |
| 22 | no client plays a season | a headless play loop composed from existing parts (§9) | 5 | §8 step 4 |

## 7. Research transfer

Read: `research/00_INDEX.md` (§1 and its precedent rows by grep), `research/by_lane/IN_infrastructure.md`
(§0 verdict, §7 throughline register, §10.0, the rest by heading), `research/emergent_narrative_literature/04_sifting_curation_and_simulation.md`
(headings only). Everything else under `research/` was not opened `[SKIPPED, §12]`.

**Changes what to build**

- **T-IN-1, "persons differ in wants, not capacities"** (repository pattern, IN §7.1). Re-observed
  here from the other side: 72 % Failure and a pool of 2 everywhere. It transfers as the reason the
  case `setup:` block must carry capability and why F-CORE-04 is not the core's to fix alone.
- **T-IN-4, "acts record that something happened, not what"**. Bears directly on beat matching: a
  beat can only be matched on kind, actor, subject and cause, so `beats:` is specified over those
  (proposal 02) and not over content the Events do not carry.
- **Story sifting** (the *Felt* / *Winnow* / *Select the Unexpected* cluster, `LIT` file 04; I rely on
  the file's headings and on the papers' general thesis, not on the repository's write-up): a sifter
  matches event patterns over a simulation's record, so the record's signal-to-noise is a design
  quantity. F-CORE-01 is that quantity measured. This is the precedent for building `beats:` as a
  pattern over the log rather than as a scripted check.
- **T-IN-3, "built ahead of its readers; armed controls shipped at off"**. The depth cap and the
  `scale:` column are two more instances; resolutions 8 and 21 follow the lane file's own verdict.

**Decorative for this lane**

- **T-IN-5, one resolver at several fidelities.** Already the code's shape (one ladder, providers);
  nothing to change.
- **Dwarf Fortress simulation principles, RimWorld's storyteller** (`LIT` 04, G13/G14). A storyteller
  that injects events is the actorless channel the loop already has (`season(actorless=…)`); adopting
  a pacing director would be a second clock, which the ruled design refuses. Tried; does not transfer.

**Nulls**

- **T-IN-7: no precedent solves the scale handoff above the bout.** Holds here: ENCOUNTER suspends
  for one provider call only (`driver.py:434-443`); there is no precedent to borrow for pausing a
  season inside a field battle for a person's act.
- **No precedent in the corpus for testing an emergent-narrative engine against authored arcs without
  scripting them.** The index names none; proposal 02's off-arm control (the beat must not occur when
  the enabling setup is withheld) is this lane's own answer, not a borrowed one.

## 8. Best path forward (ordered)

Alone = needed for the core to run and be judged by itself; Compose = needed for other lanes to land on it.

| # | what changes | where | gate (execution artifact) | unblocks | cost | alone / compose |
|---|---|---|---|---|---|---|
| 1 | fading as a read | `loop/matter.py:471-501`, `queries/person_q.py` (the confidence reader), `write_matrix.yaml` `(Claim, confidence)` | growth probe re-run: new events per season flat within ±20 % over 8 seasons at seed 0, 1, 2; same-seed hash equal; `claim.decayed` absent | long arcs; R-01/R-02 readings | small build, hash mover | alone |
| 2 | `reading:` record; R-01/R-02 re-pointed | `requirements.yaml`, `harness/register.py:631-701` | `register --requirements` prints each row's command, tree and seed; the chain reading's planted control flips | honest NINE | edit + small build | alone |
| 3 | `setup:` / `beats:` on eight overlay cases, then by lane | `cases/exercises/*.yaml`, `harness/corpus_run.py::build_at`, `harness/arc.py` | per case: beats matched in the on-arm, not in the off-arm, at three seeds | §13; R-05, R-06 on real casts | small build, then data authoring | compose |
| 4 | a headless play loop | new `harness/play.py`, composing `dispatching_chooser`, `decision/sheet.py`, `world_q.endings_reached`, `harness/chronicle.py` | a scripted-policy client plays NPC-088's world for four seasons; a planted deviation moves the hash, the echo policy does not | playable (F-CORE-05) | small build | alone |
| 5 | IN-14: rounds follow the largest budget | `driver.py:479` | a seated person spends budget + bonus scenes in one season | R-04 | edit (ruled shape) | compose |
| 6 | resolutions 17–20 | named sites | each site's existing test file | hygiene | edit | alone |
| 7 | `w.tenures` served from the barrier cache; `TRACE` bounded or off outside instruments | `world.py:455-471`, `queries/cache.py`, `trace_log.py` | realm `aperture 1 0` wall time before and after, same hash | iteration speed (three-seed controls become affordable) | small build, hash EQUAL | alone |
| 8 | register rows regraded (9–16) | `hole_register.yaml` | `register --check` R2/G6 counts fall by the rows named | — | edit | alone |

Deletions available and not scheduled: the `scale:` column (CR-07); comment history, file by file, when
a file is opened for another reason.

## 9. Playable standalone and integrated

| point | exists today | missing | work |
|---|---|---|---|
| **Entry point** | `python -m engine.season.harness.headless` (one fixed world, automated); `populated.run` (the realm, automated) | any entry where a person's choices are taken from outside the engine | §8 step 4 |
| **Scenario seed / fixture** | `headless.build_world(seed)`; `populated.build_realm(seed)`; `corpus_run.build_at(case, seed)` (template) | a scenario stating who the player is, what is at stake and when it ends | proposal 02's `setup:` is the scenario format; reuse it |
| **Choice surface** | `DevelopmentSheet` offers the ranked candidate set and takes indices (`decision/sheet.py`, per its docstring; body `[UNVERIFIED]`) ; `PlayHost.decide` for a duel | a loop presenting it each round; a menu for seat verbs (CL-MGMT, held) | §8 step 4 |
| **Outcome legibility** | the Event log with `causes[]`; `harness/chronicle.py --chains` | a per-act answer to "what did my act cause", shown to the chooser; refusals name a clause (`row.refusal_for`) but nothing returns it to the actor | step 4 prints the acting person's Events and their one-hop effects each round |
| **Stakes** | pursuits and `commit`-to-OUGHT questions exist per person | nothing tells a player his own | step 4 prints the sheet's questions |
| **End condition** | `endings_reached` in the season's return value | nobody reads it; case endings are `NOT-COMPUTABLE` | terminal beat (proposal 02); the play loop stops on a non-empty `endings` or a dead player with no continuation (`carry_on`, `play_surface.py:61-95`) |
| **Instrument / golden** | m1's same-seed hash; corpus R4 | a golden for a *played* season | step 4's echo-policy control |
| **One code path** | yes: a player's `choose` is called by the same DELIBERATE, folded by the same RESOLVE; an echo callback leaves the hash equal (the file's stated control, not re-run here) | — | keep: the play loop must construct `auto` exactly as `headless.run` does |
| **Layer-1 conformance** | the core is the host, not a registered module; its module boundary is typed (§4) | provider→seam result typing (F-CORE-10) | a typed `ContestResult` when a fourth provider shape appears; not before |
| **Integration** | executed edges in §10 | — | — |
| **No GM** | the engine resolves every act it admits; what it cannot evaluate it refuses with a named kind | sixteen corpus cases presuppose a player; `presence:` eligibility always declines | resolution 4; H-75 |

"Resolves correctly" is established (§2). "Plays" is not: no person has been offered a choice by this
code outside a test.

## 10. Interfaces

| with | core consumes | core emits | executed? |
|---|---|---|---|
| `decision/` (CHAR) | `choose(p, view, sensation, ask_budget)` → Acts/Scenes; `budget`, `assemble`, `standing_of` | `Question[]` per person (`driver.py:377-385`), a `View` | executed (every run) |
| `modules/social_contest` (SC) | `Margin(net, ob)` via `sigma.resolve` | `SocialContestInput` | executed: corpus `argue` 947, `tell` 158, `lie` 138, `speak` 19 |
| `modules/combat` (PC) | result dict with `wound_state` | `PersonalCombatInput`; `PlayHost.decide` | executed: corpus `fight` 13 (Felled 8), `capture` 2 |
| `modules/mass_battle` (MB) | field result (`attacker_wins`, `unopposed`, `invested`) | `MassBattleInput` at ENCOUNTER | designed and tested; **not reached in the corpus** (`march` in "never attempted"); realm reach is the requirement file's reading, not re-run |
| `modules/fieldwork` (FI) | `Findings` | `FieldworkInput` | executed: `research` 639, `surveil` 236 graded; trail finds `[UNVERIFIED count]` |
| settlements (SE) | `SubsistOutcome`, `ProduceOutcome` | `SubsistInput`, `ProduceInput` at MATTER | executed every season (`matter.py:600,741`) |
| governance / factions (FA) | effects and predicates keyed by verb; `gate` bases | tenure changes judged by `refuse_unauthored` | executed for `issue`, `release`, `petition`, `carry`; `determine` only refused in the corpus |
| information (SC/FI) | `witness` deposits | Events to fan out | executed: 93,760 claims |
| Godot (GO) | — | `content_hash`, the canonical encoding (`world.py:279-340`) | executed in Python; port edge designed |

## 11. Survivors for Jordan

One.

**The fading of memory: a logged write per claim, or a read.** It touches AX-5's licensed clock and the
`(Claim, confidence)` row of the write matrix, which descend from ratified Layer 1, so it is listed
here as well as proposed.

- *Option A (proposal 01): fading is a read.* Confidence is computed from the deposit and the elapsed
  seasons. The log holds what persons did, learned and lost entirely. A sifter or a chronicle cannot
  cite the season in which a belief weakened, only compute it. Long arcs become affordable.
- *Option B: fading stays a write, aggregated.* One `ledger.faded` Event per person per season,
  carrying a count. The log keeps a seasonal trace of forgetting that an arc could cite ("by the third
  winter he had lost the thread"), at one Event per person per season instead of one per claim.

They differ as games only if forgetting is meant to be a *story beat with a cause*. Nothing in the
corpus asks for that; precedent in the tree (L5: a crossing emits, a level does not) favours A. A is
taken as the decided resolution, `[medium; Jordan to correct; revert: B]`.

## 12. Evidence log

All at tree `601e715`, `PYTHONHASHSEED=0`. Outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/CORE/`.

| command | seed · seasons | outcome |
|---|---|---|
| `python -m engine.season.harness.register --requirements` | — | exit 0; 3 met · 1 not_met · 5 partial (`register_requirements.txt`) |
| `python tools/m1_acceptance.py --summary` | 20260819 · 1; 24 seeds · 4 | NOT MET on the doc-derived row only (`m1_summary.txt`) |
| `python -m engine.season.harness.corpus_run` | 0 · per case 1–6 | exit 0 (`corpus_run.txt`); figures in §1.4 |
| `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` | 0 · 2 | hash `5405522c36b0399247f83fd9f6d29494`; "verbs the fold can execute: 66 of 67" |
| `probe_growth.py 8` (headless world; cProfile on season 7) | 0 · 8 | `probe_growth.txt`; hash `d444b0f32c2f39e9129b58089362c9f2` |
| `probe_arms.py` (depth cap 1/2/3/7; `scene_budget` 1) | 0 · 2 | depth arms all `5405522c…`; one-round arm `a3382906…` |
| `python -m engine.season.harness.exercises` | — | NPC 35/292 (32/122 core); ARC 0/611 (0/300 core) |
| `python -m engine.season.harness.register --check` | — | exit non-zero by its own rules: R2 27, G6 3 (`register_check.txt`) |
| `sloc.py engine/season` | — | `sloc.txt` |
| case census (inline) | — | 143 cases; core needs NPC 126, ARC 301; spans: 86 prose, 52 ≤ 6, 5 > 6; `needs_deadline` yes 26; `ends_when` never 52; 19 `forced_by_threshold` |
| `python -m engine.season.harness.aperture 4 0` and a profiled `aperture 1 0` | 0 · 4 / 1 | **not completed.** The first launch failed (`/usr/bin/time` absent; caught by checking the empty output). Relaunched; stopped by me after about eight minutes with no output, the machine carrying a dozen sibling instrument runs. No realm reading in this audit is mine |

**Reading coverage.** Read in full with comments: `loop/driver.py`, the brief, both dossiers,
`harness/play_surface.py` (head), `cases/chain/CASE_BRIEF.md`. Read as executable lines only (comments
and docstrings stripped by `strip.py`, original line numbers kept): `loop/{resolve,encounter,deliberate,census,calendar,effects,effects_shared,sides,matter}.py`,
all of `state/`, `seam/{contest,ladder,__init__}.py`, `seam/wrappers/{sigma,combat,pool,fieldwork,_entry,_estimate}.py`,
all of `manifest/`, `queries/{cache,inputs}.py`, `gaps.py`, `trace_log.py`, `data/{__init__,files,matrix}.py`,
`harness/{headless,invariants,exercises,delta,register}.py`, `harness/corpus_run.py:460-1089`.
`requirements.yaml`: every row's `measure:` and the first 2,600 and last 1,500 characters of each
`measured:`. Hole register: the 53 primary rows to 650 characters of cite (2,300 for fifteen), the last
nine of them (H-86 onward) from the dossier excerpt only.

`[SKIPPED: loop/predicates.py — outline only; governance predicates, FA lane's mechanism]`
`[SKIPPED: loop/witness.py, seam/wrappers/mass_battle.py — not opened; other lanes' bodies]`
`[SKIPPED: data/{fixtures,requires,rosters,verbs}.py and the four large YAML registries as files — read only through the loaders' behaviour and greps; context budget]`
`[SKIPPED: harness/{aperture,soak,populated,probes,run_cases,report,loops,interactions,arms,scarce}.py — not opened beyond greps; context budget]`
`[SKIPPED: the 43 listed test files — none opened]`
`[SKIPPED: HANDOFF_IN.md, workplan positions other than the B10-18b card head, architecture/meta/04 — not opened; statements about Layer 1 rest on code comments and are marked]`
`[SKIPPED: research/ beyond the files named in §7]`
`[SKIPPED: individual case files and proposals/2026-08-30-arc-reachability/ — the corpus was read by census, not case by case]`

## 13. Provided arcs and characters — adjudication

The core owns the mechanisms a case's `temporal`, `who_acts`, `knowledge` and `ends_when` blocks turn
on, and the instrument that would check any need. Needs whose mechanism is a verb, a contest or a
character field are other lanes'; they are cross-listed by class, because the cases were censused, not
read one by one (§12).

| case(s) | need (short) | hardness | represented today? | evidence | change required | owner | proposal | gate |
|---|---|---|---|---|---|---|---|---|
| all 143 | the case's own cast, seats, relations and records exist in the world | core (implicit in every row) | **no** — one template | `corpus_run.py:467-662`; statuses `RUNS-UNDECLARED` / `SPAN-UNAUTHORED` | `setup:` block read by `build_at` | CORE | 02 | two cases at one scale build different worlds (hash differs at tick 0) |
| all 143 | each `season_requires` need is checked by a run | core 427 · important 463 | **no**: 35 of 292 NPC rows bound, 0 of 611 ARC | `harness.exercises` | `beats:` matched over the log, with an off-arm | CORE | 02 | beat present on-arm, absent off-arm, seeds 0–2 |
| all | one person's act is cited by another person's later Event | core (propagation) | **yes** | R3 143/143; planted control False→True | none | CORE | — | held |
| all | what a person holds differs from what another holds | important (`knowledge`) | **yes, structurally** | `carriers.py:504-509`; firsthand 93,696 | none in the core | CORE | — | held |
| cases whose `knowledge` turns on being *told* | a third party learns later, by report | core where stated | **barely**: `told_by` 64 of 93,760 | corpus run | odds and capacity of `tell` | SC, CHAR | — | told share rises against a control |
| ARC-44, EMG-C4, EMG-C3, EMG-X8, ARC-20 | spans of 16, 10, 9, 9, 8 seasons | core (`temporal`) | **no**: clamped to 6 | `corpus_run.py:72,460-464` | proposal 01, then lift `MAX_SEASONS` | CORE | 01 | the case runs its authored span inside the corpus budget |
| 86 cases (40 ARC flagged) | a span stated as prose | — | **wrongly stated**: two readers would run different lengths; the runner picks 2 | `corpus_run.py:73`; `SPAN-UNAUTHORED 40` | integer span plus `ongoing:` | CORE (data) | 02 | no `SPAN-UNAUTHORED` row |
| 26 cases with `needs_deadline` | something must happen by a date | core where stated | **mechanism yes, case no**: CALENDAR fires due dates (`calendar.py:47-76`); only the 19 `forced_by_threshold` arcs get one, always at tick 1 with no holder | `corpus_run.py:655-661` | `setup.dates` with holder, venue and tick | CORE | 02 | `date.fired` at the authored tick, with a sitting when held |
| 91 cases with a stated `ends_when` | the case concludes on a condition | core | **no**: `ENDS = NOT-COMPUTABLE`; `ENDINGS_CLASSIFIED.yaml` holds labels and one flag | corpus run | a terminal beat | CORE; FA for endings that are binding decisions (A2) | 02 | terminal beat matched; run length recorded |
| 52 cases, `ends_when: never` | a stable continuation | important | **yes** as "the season keeps running" | m1's 24 seeds × 4 seasons, no violation | proposal 01 for affordability | CORE | 01 | flat cost per season |
| 16 cases naming a player (NPC-002, -003, -008, -013, -030, -031, -032, -050, -070, -075, -086 and five more) | a player's choice changes the outcome | core | **no**: the runner passes the automated chooser only (`corpus_run.py:953`) | `WAITS-ON-PLAYER 16` | a declared policy proxy through `dispatching_chooser` | CORE | 02 | beat present with the proxy, absent with the echo policy |
| NPC-088 | labour ripening over seasons by her own act | core | **yes** | headless run: `record.created` 4, `term.matured` 5 in season 1 (`probe_growth.txt`); `matter.py:338-395` | none | CORE | — | held |
| NPC-088 | possession of the product has consequences for whoever holds it | core | `[UNVERIFIED]` | — | to be read with `setup:` | FA / SC | — | — |
| cases needing memory across seasons | a fact persists and is acted on later | core | **yes, with a cost**: ledgers persist (1,120 claims, three persons, eight seasons) | `probe_growth.txt` | proposal 01 | CORE | 01 | — |
| arcs ending in a ruling, a battle or a duel | a binding decision / a field / a fight concludes the arc | core | **partly**: `fight` executes (13); `determine` only refused; `march` never attempted in the corpus | corpus run | docket and party reach (H-254); march referents | FA, MB, PC | — | those lanes' gates |
| all | persons differ in what they can do | important | **no**: pool default for all but one corpus person | corpus degrees; `pool.py:94-100` | capability in `setup.cast` | CHAR (data), CORE (reader exists) | 02 | two persons roll different pools |

**Needs wrongly stated (core's share).** Prose spans (above). Cases at `scale: faction` or `world` were
re-scaled by overlay to `realm`/`duchy` (`cases/exercises/ARC-22.yaml` is one); the re-scale is recorded
with a reason per file and is accepted. Rows beginning `UNCLEAR:` are the source's own admission and
stay unrouted.

**Soonest, in order.**

1. **NPC-088** — already the headless artifact with a cast overlay; add `beats:` and it is the first
   case checked end to end. Depends on nothing.
2. **The other seven overlay cases** (NPC-002, -005, -010, -012, -075, -086, -087) — bindings exist;
   convert them to `setup:`/`beats:`. NPC-002, -075, -086 need the player proxy (resolution 4).
3. **The nineteen `forced_by_threshold` arcs** — once `setup.dates` can name a holder, the deadline
   beat is the core's own. Their conclusions depend on FA (`determine`).
4. **The five long arcs** — after proposal 01.

**Dependency edges out of this lane.** CHAR → cast capability and goals (every case). SC → `tell`,
`argue`, `speak` odds (cases turning on report or persuasion). FA → `determine`, docket, writs (arcs
ending in a decision). MB, PC → arcs ending in a field or a duel. SE → cases at settlement scale whose
needs are stores and works. None of these blocks proposals 01–03.
