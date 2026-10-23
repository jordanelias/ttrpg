# Threadwork — completion proposal (T07 · lane IN)
## Status: PROPOSED. Merging this file ratifies nothing (ED-1094's loud exception); every item and ask is held back for Jordan's adoption, item by item, as edits to the v9 parts it names.
## Lane: IN (cross-cutting). A proposal for edits to `workplans/valoria_master_workplan_v9*.md`, not a second plan (`CLAUDE.md` §2).
## Grade under `CLAUDE.md` §0.2: `paper`. Nothing here executes. What it changes in `engine/season/`: nothing, until adopted.
## Written against: HEAD `2decf4a`. Inputs: `proposals/2026-10-22-system-description/…-08-t07-threadwork.md` ("T07", whole), `…-00-overview.md` §3, §5.2, §6; `…-03-t02-season-persons-choosing.md:175`, `:238-244`, `:630-649`; `research/game_precedent_suite/dispositions/D_T07.md` (whole); `research/game_precedent_suite/THROUGHLINES.md` (whole); `proposals/2026-10-16-verbs/2026-10-16-verbs-13-lexicon-threadwork.md` ("verbs-13", whole); `…-22-gap-register-fi-and-tw.md` (TW rows by grep); `proposals/2026-10-21-v9-remediation/` (grep: REM-45 at part 03 `:165-176`, RB-4a/B-S at `:10-11`, JQ-1..6 headings in part 04); `workplans/valoria_master_workplan_v9_part3.md:234` (B-S row), `_part4.md:96-104` (IN-06), `_part5.md:73-99` (IN-32, IN-35), `_part7.md:42-46` (PC-06 K-3), `:77-82` (WR-01); `proposals/2026-10-07-unplugged-systems-replug.md:215-295` (IN-06's threadwork design); code opened at HEAD as cited.

**Frame.** Threadwork's mechanism is the oracle `systems/threadwork/sim/` (1,955 LOC with the package `__init__`, T07 §9). This file
does not redesign it. It designs the path by which a person's act at DELIBERATE reaches the oracle at RESOLVE, and the carriers the
oracle's results land on, so that the price it already computes is paid by a `Person` the season loop holds and is felt in that
person's later seasons and in the world. Terms used below and defined in T07 §0: `Person`, `Site`, `Tenure`, `Claim`, WITNESS,
RESOLVE, seam Event, Calamity, Locked Zone. Two coinages of this file: **headroom** (T07 §5(a): `HUMAN_BAND_LIMIT` minus the resting
point, what a practitioner protects) and **the crossing** (resting point > 5, `coherence.py:215-219`).

## §0 The genre loop

The yardstick: what a player of costly-magic and sanity games (Darkest Dungeon II, Sunless Sea, Eternal Darkness, Don't Starve,
Bloodlines, RimWorld psycasts) expects to be able to do, stated in this engine's terms. Grades: AFFORDED / PARTLY / ABSENT today, with
the suite's evidence grade (T07 §0: nothing in threadwork is RUNS-IN-LOOP at any seed). Precedent cites are tier 3 (reference).

| # | play opportunity (what a person chooses · at what cost · with what lasting consequence) | precedent | today | evidence |
|---|---|---|---|---|
| G1 | **Perceive what others cannot.** A sensitive reads a site or a person's substrate, paying a little stretch, and learns a Claim no inquiry by a non-sensitive can mint. | verbs-13 §3.2 row 1 [MEMORY]; P26 (ledger) | ABSENT: `thread_read` has a row (`verb_table.yaml:1496-1509`, `writes: []`) outside `resolvable_verbs()` | DESIGN-ONLY |
| G2 | **Spend power at a price that accrues on the practitioner.** Choose the depth of a working: deeper reaches more and costs more stretch, a bad roll costs more again. | P39; D_T07 #6, #17 (DIFFERS: one channel, ruled C-2) | PARTLY: the oracle prices it (`operations.py:290-348`); no person in the loop pays | TESTS-ONLY |
| G3 | **Feel the meter before it breaks.** Displacement bands change what the practitioner can do (odds, refusals, what he may risk) well before the breach. | P01; TM01; D_T07 #5 (LACKS) | ABSENT: bands are labels read by nothing (`coherence.py:154-162`; T07 §2.3) | TESTS-ONLY (labels only) |
| G4 | **Face the breach, and have it mean something.** Crossing the line fires one event with a consequence the world sees, with odds the practitioner's own state sets. | P02; TM01; D_T07 #21, #22 (LACKS); #7 (DIFFERS, ruled: a latch, not a game over) | PARTLY: the crossing latches a report and blocks self-Mending (`coherence.py:400-432`); nothing follows (`:67-70`) | TESTS-ONLY |
| G5 | **Choose how to recover, at a price.** Rest a season where things stand in equilibrium, or mend another and be repaid, or mend yourself; each recovery costs acts, place or risk. | P40; TM01; D_T07 #4, #23, #28, #30 | PARTLY: `recover` and Mending exist, recovery is free and ungated in rate (`operations.py:159-167` `[GAP]`); no clock or verb calls `recover` (K-WR-8) | TESTS-ONLY |
| G6 | **Carry a lasting mark.** Pressing on without rest leaves set that rest never removes. | P32; D_T07 #27 (HAS), #29 (DIFFERS) | PARTLY: set is built (`coherence.py:328-336`); `Person` holds no Coherence, so nothing survives a season | TESTS-ONLY |
| G7 | **Change the world with a working.** A weave holds a thing, a lock stops a place changing, a dissolution ends it, a mend repairs it, and the change outlives the act. | verbs-13 §3.2 rows 2-5 [MEMORY]; D_T07 #36 (LACKS) | ABSENT: no operation writes its target (T07 §8 trap 3) | DESIGN-ONLY |
| G8 | **Be seen, and be feared for it.** A witnessed working moves the convictions of those present and gives the orthodox something to charge. | P13 (Bloodlines Masquerade); D_T07 #19 (LACKS) | ABSENT: the sign cells `thread_read: -1/+1` (`rosters.yaml:2793-2797`) are unread because the verb never resolves | DESIGN-ONLY |
| G9 | **Work together, or against a rival.** Pool practitioners for a deep working; contest a rival's working. | verbs-13 §3.2 row 9 [MEMORY] | PARTLY: lattice and opposed workings run in the oracle (`collective.py:71`, `opposing.py:102`) | TESTS-ONLY |
| G10 | **The world works when nobody watches.** NPC practitioners work, take set, cross, recover and are seen, so threadwork drama occurs in seasons with no player in it. | throughline 6; D_T07 #14, #24 (LACKS) | ABSENT: no NPC carries TS; the chooser never forms a thread verb | DESIGN-ONLY |

Two expectations of the genre are **excluded by ruling** and are not on the yardstick: a separate refillable power pool (D_T07 #6, #17;
C-2 couples cost to Coherence) and drain by mere presence or time (D_T07 #2, #13; E-4 and the write gate at `state/world.py:1010-1019`
allow only a Seam driver). Advancement by study is excluded by canon (P-08, TW-G42).

**What v9 already schedules, which this file builds on and never repeats** (all in batch B-S, `_part3.md:234`, unless named):
IN-06's build (the store-shed: each operation returns its cost and the host writes `(Person, coherence)` as two quantities; composition
rows `threadwork.<operation>` (`verb_call`) and `threadwork.coherence_band` (`query`), the latter "lands only with a consumer";
`proposals/2026-10-07-unplugged-systems-replug.md:235-275`); PC-06 K-3 (`thread_read`'s TS operand typed on `Person`; it leaves the
no-predicate set, `_part7.md:44-46`); IN-35 (the Calamity as one coupling rule on lattice Sites in the wear loop, Mending as persons'
acts, a `+` LOOP row; weight 0 = today, `_part5.md:87-98`); IN-32 (`tie / knot`'s effect, reader and partner operand, `_part5.md:73-78`);
WR-01 (R-14 resilience reaching `engine/season/`, gain at control 0, `_part7.md:77-82`); REM-45 in RB-4a, before B-S (the history term
`min(3, history) + 3`, gated on hand-verifying PP-624, remediation part 03 `:165-176`). After all of these land, G2 and G6 are reachable
for `thread_read` only, a person pays a charge, and the charge leaves no mark on play. Everything below is what remains.

## §1 Gap ledger

Rows are D_T07's LACKS (12), DIFFERS (10) and CONTRADICTS (2) rows: **24 addressed of 24**. HAS rows (#3, 12, 15, 20, 23, 27, 32,
34, 35) are carried for their grade only (all TESTS-ONLY). DISCARD rows (#8-11, 16, 26, 31, 40) are not re-opened. Tutorial gaps from
§0 with no disposition row are listed last.

| gap | rows | what is missing | ending |
|---|---|---|---|
| A. Free self-repair dominates the meter | #4 (LACKS), #28, #29 (DIFFERS, evidence and risk) | own-aim Mending has no cost, cadence or raised Ob, so set walks back at 0.85 a cast (`operations.py:159-167` `[GAP]`) | closed by **CP-T07-04** (one act per cast, a swept self-aim Ob step) |
| B. The meter is not felt before the breach | #5 | bands are labels (`coherence.py:154-162`); no pool, Ob or act reads them | closed by **CP-T07-07** |
| C. The breach changes nothing and forks nothing | #21, #22 (LACKS), #7 (DIFFERS, ruled: a latch, not a game over) | the crossing latches a report (`coherence.py:411-432`); what follows has no carrier (`:67-70`, TW-G11, K-WR-5) | closed by **CP-T07-08** (the breach Event, its witnesses and a TS-keyed outcome slot at control); the outcome's content is **Jordan ask A1** |
| D. Recovery never runs | #30 | no caller of `recover` in the season (K-WR-8, TW-G29) | closed by **CP-T07-06** |
| E. Nothing decides where equilibrium holds | #23 (HAS shape; the boolean is caller-supplied) | `environment_in_equilibrium` is a flag, default False for Mending (`operations.py:544-548`) | closed by **CP-T07-05** |
| F. The meter spawns nothing into the world | #14 | displacement creates no threat (Don't Starve's shadows) | closed by **v9 IN-35** (the Calamity worsens as a consequence of held configurations), fed by **CP-T07-03**'s strain. `threadcut.py` stays unplugged (IN-06's design, `:280-284`) |
| G. A witnessed working costs nothing socially | #19 | the sign cells `thread_read: -1/+1` (`rosters.yaml:2793-2797`) cannot fire: the scar needs an outcome that moved state (`:2776-2778`) | closed by **CP-T07-09** |
| H. One practitioner's displacement never moves another's | #24 | lattice charges each participant separately; opposed composure is returned only | closed by **CP-T07-08**'s knot arm (P-12, propagation along a live knot, control 0) |
| I. Endurance is not a build axis | #1 | range 6 and limit 5 for every being; R-14 resilience at gain 0 | declined — step 2 for this file: v9 WR-01 owns the per-practitioner term and carries it to `engine/season/` at gain 0 with the slot and the gain still unruled (`workplans/valoria_master_workplan_v9_part7.md:79`); not closed until WR-01's slot is ruled. CP-T07-01 fills `.resilience` from WR-01's slot when it exists. The range stays a per-being constant by E-3 (`coherence.py:31-32`) |
| J. Past workings never change the roll | #33 | history is a dead term (`operations.py:246`) | declined — step 2/3: REM-45 makes the term live, but its input has **no producer**: `train` raises only `VOCATIONS`, the values of `verb_capability`, and "Thread Sensitivity is outside it" (`engine/season/data/verbs.py:1508-1511`), it raises only a key the person already holds (`write_matrix.yaml:220`), and nothing seeds a thread key. A producer by study collides with P-08 ("by study alone"). CP-T07-01 reads history 0 for everyone, so the term is a constant 3 until a producer is ruled; not raised as an ask (no item here waits on it) |
| K. Options with no distinguishable outcome | #36 | Locking = Dissolution in Ob, cost and MS (`operations.py:417-438`) | closed by **CP-T07-03** (`lock` writes what `weave` does not); `dissolve` is PARKED by §3's cut test |
| L. No precedent handle for threadwork | #37 | — | declined — step 1, superseded: T07 §5(f) carries the handles (T07 round-3 correction 8) |
| M. Ruled differences, no item | #2, #13 (E-2, E-4; write gate `state/world.py:1014-1021`), #6, #17, #38 (C-2: one channel), #18 (P-10/P-15; T07 trap 17 exists), #25 (E-2: displacement buys nothing) | the precedent's trade is given up by ruling | declined — step 3, each row's ruling; CP items respect all of them (no presence drain, no power pool, no cost-as-power term) |
| N. Stale or unsupported citations | #39, #41 (CONTRADICTS) | verbs-13 cites `verb_table.yaml:1212`, `rosters.yaml:2349-2354`; T07's old support for "0 attempts" | declined — step 1, superseded: this file cites HEAD (`verb_table.yaml:1496-1509`; `rosters.yaml:2793-2797`); T07 §0 round-3 correction 1 fixed #41 |
| O. Perception yields nothing a sensitive alone can learn (§0 G1) | — | `thread_read` writes `[]`; FI's content yield FI-G01 | closed by **CP-T07-10** (two finding contents) |
| P. A working changes nothing in the world (§0 G7) | — | no operation writes its target | closed by **CP-T07-02**, **-03**, **-04** |
| Q. No person can pay, and nobody can work but `thread_read` (§0 G2, G10) | — | IN-06/K-3 give the carrier and one row | closed by **CP-T07-01**, **-02**, **-09** |
| R. Working together or against (§0 G9) | — | lattice and opposed run in the oracle only | opposed: closed by **CP-T07-11** (`ward`). Collective: declined — step 5: gathering same-round workings onto one target needs ENCOUNTER-time resolution (the `a field` prize's shape, `rosters.yaml:1281-1286`), and `(Person, coherence)` is admitted at RES only (`write_matrix.yaml:186-187`); trigger in §7 |

Count: 24 rows addressed — 11 closed by CP items (#4, 5, 7, 19, 21, 22, 24, 28, 29, 30, 36), 1 by a named v9 item (#14 IN-35),
12 declined (#1, 2, 6, 13, 17, 18, 25, 33, 37, 38, 39, 41). One Jordan ask (A1) rides gap C.

## §2 Items

Common to every item. **Layer:** all items bind Layer 2 (the game code and the registries `engine/season/` opens at runtime);
`architecture/` is not edited. **Seam:** every write to `(Person, coherence)` goes through the one host of CP-T07-02, at RESOLVE,
with `driver="Seam"` (`state/world.py:1014-1021`). **Control arm** shared by all: `ts_seed: none` (every Person seeded TS 0), under
which no thread candidate forms; the hash must equal the post-B-S base hash. **Test home:** one new file,
`engine/season/tests/test_threadwork_loop.py` [proposed], one test per falsifier below. **Tiering:** producer Sonnet; the judgment
nodes (CP-T07-03's Site semantics, CP-T07-08) get an Opus critic.

### CP-T07-01 · The practitioner on the Person (join with T01, T02 / J-T1 and K-3) · size S

- **Adds.** The host's actor adapter: the oracle reads a duck-typed actor (its docstring names `.spirit`, `.focus`, `.ts`, `.history`,
  `operations.py:15-19`; the code also reads `.resilience` and, in `collective.py`, `.cognition`, T07 §1), built from `Person` by the
  host, never stored as a second object. `ts` = K-3's operand. `spirit` and `history` are **addends registered through T01's
  `faculty(p, verb)`**, the one person-capacity owner (cross-file ruling R3): T01's `verb_capability` rows for the thread verbs register
  them, and the adapter hands each to the oracle under its name; there is no parallel read. V-3's `faculty(domain)` is not used (LEAVE
  pending the unratified K-2, `workplans/valoria_master_workplan_v9_part7.md:44`). A **stored** `spirit` is gated on **JQ-2**
  (remediation part 04 `:32-55`: whether J-13's "not a character attribute in and of itself" binds resolutions beyond the
  proceeding); until JQ-2 and J-T1 are answered, `spirit` is the oracle default 4 for everyone. `history` has no producer (gap J) and
  reads 0. `resilience` = WR-01's slot when ruled, absent until then. TS **seeding** at
  world build from `references/npc_registry.yaml` `ts:`: an integer stands; a range (`75–80`) seeds its low end; `~50` seeds 50;
  `null` and absent seed 0 (TW-G04's parse rule, which verbs-13 §3.6 assigns to M2 and no v9 item builds).
- **Owner.** `harness/populated.py` (seeding, beside the conviction read at `:1011`); the adapter in CP-T07-02's host; the parse
  rule as one function next to it. TS is fixed after build (P-08; J-T4): no writer in play.
- **Primitives.** P24 (TS ≥ 30, the one class gate, H-85), P15-like holder-scaled output (Spirit doubles the pool).
- **Reads/writes.** Reads `Person` fields and the registry; writes K-3's TS field at build only (outside the gate, as `cast:` overlays
  are, `write_matrix.yaml:220`).
- **Joins.** T01: *need* `faculty(p, verb)` to expose its registered addends by name (or the thread rows register `spirit` and
  `history` as two keys read separately), and `verb_capability` rows for `thread_read`, `weave`, `lock`, `mend`, `ward`.
  T02 / J-T1 and JQ-2: *need* the ruling on a stored Spirit, or J-T1's ruling that it is derived (then T01's addend carries the
  derivation; the adapter does not change). PC-06 K-3: *need* the TS field and a typed precondition evaluable **at
  formation**, so that a non-sensitive never forms a thread candidate (the gate belongs in the option set: #353 §9.2 as quoted at
  `hole_register.yaml:1062`) `[UNVERIFIED: where typed preconditions are evaluated today]`.
- **Chooser / unwatched.** Nothing chosen; it decides who can choose. At HEAD's registry, four of the 46 rows seed TS ≥ 30: NPC-001
  Edeyja (75), NPC-075 Orm (60), NPC-002 Maret Uln (50), NPC-005 Sigrid Torsvald (35); 25 and 28 seed below the gate. More
  practitioners are an authoring call on the registry, not this item.
- **Falsifier.** A Person seeded from `ts: 75–80` reads TS 75 and forms a `thread_read` candidate; one seeded from `ts: 25` forms none.
  Fails if either is otherwise. **Control.** `ts_seed: none` gives the base hash.
- **Hash movers.** None alone (no row yet executes on TS). **Revert.** Delete the seeding call.

### CP-T07-02 · The Leap stage and the one working host · size M

- **Adds.** `engine/season/seam/wrappers/threadwork.py` [proposed]: the one host every thread row dispatches through. Order, fixed:
  (1) materialise elapsed recovery (CP-T07-06); (2) roll `attempt_leap`; on Failure the act ends, `working.failed`, and the Leap's
  charge stands (the oracle's own −1, C-TW-3, is carried, not fixed here); Partial proceeds, the reading `collective.py:116-118`
  already makes; (3) roll the operation (`attempt_weaving` / `_locking` / `_mending`, or the read of CP-T07-10); (4) sum the charges
  into one seam Event `coherence.changed` carrying both quantities before and after (the matrix's declared kind, `write_matrix.yaml:191`);
  (5) return the degree as the act's `Resolution`, so each row's effect (CP-T07-03, -04) reads `res.degree`. **Scale is read off the
  target, not chosen**: a roster `thread_scales` maps the target's class (Person → Personal; Tenure → Relational; Site by kind, a
  lattice Site → Structural) `[ASSUMPTION — basis: `DEPTH_OB` is "how deep in the substrate the target sits", T07 §1]`. The choice
  left to the person is which target.
- **Owner.** The host; one prize row in `rosters.yaml: contest_subsystems.prizes` (as I expect it: `"a configuration"` → module
  `threadwork`, `module_entry: threadwork.work`), on `determine`'s precedent of a single-actor roll through `contest`
  (`verb_table.yaml:383-384`). IN-06 left B-S to choose between this and a second `_ROLE_ROSTERS` row
  (`manifest/registry.py:38-39`); every item here is indifferent to which.
- **Primitives.** P23 (the draw), P39 (cost on the practitioner), P24 (the gate).
- **Reads/writes.** Writes `(Person, coherence)` (RES, Seam). Reads the actor adapter, `thread_scales`.
- **Joins.** IN-06: *need* each oracle entry to return its cost rather than write a store (the store-shed); *need* the composition rows.
  T01 resolution core: the degree is `dice_engine`'s single ladder (`test_degree_ladder_single_owner.py`); no second ladder.
- **Chooser / unwatched.** Every thread row is now one act of the scene economy (7 acts at budget 5, T07 §0): a working displaces a
  `tell` or a `move`.
- **Falsifier.** A planted practitioner's `weave` at seed s writes exactly one `coherence.changed` whose deltas equal the oracle's
  `OperationResult.coherence_delta` plus the Leap's for the same dice; a Leap Failure writes the Leap's charge and no target change.
  Mutation: skip step 2, and the Leap-Failure test reds. **Control.** `ts_seed: none`.
- **Hash movers.** Every executed thread row, by outcome. **Revert.** Delete the thread rows and the prize row in one commit (deleting
  the prize row alone refuses at boot, IN-06's deletion refusal, which is a breakage and not a revert).

### CP-T07-03 · `weave` and `lock` on Sites: two held shapes that write different things · size L

- **Adds.** Two verb rows (verbs-13 names; R-10 keeps `dissolve` apart), one Tenure kind `weave` in `rosters.yaml: tenure_kinds`,
  and one Site field `locked` with its write-matrix row `(Site, locked)`, RES, ACTS, `social: false` (as `(Site, condition)` is,
  `write_matrix.yaml:373-379`). The lock is **not** a Tenure, deliberately: a Tenure owned by the locker would close when he dies
  (the cascade on `(Person, exists)`) and could be closed by nobody else (the gate admits a Tenure write only by its owner, a term,
  a seat's revocation or a cascade, `engine/season/state/gate.py:109-117`), so it could neither outlive him nor be mended
  (cross-file ruling R8):

  | | `weave` (Things Cohere) | `lock` (Unable to Become) |
  |---|---|---|
  | on Success+ | opens Tenure `weave` (weaver → Site) | sets `Site.locked` |
  | wear (`loop/matter.py:659-673`) | skipped while live | skipped while live |
  | staged condition deltas (`loop/resolve.py:1113-1132`: `restore`, `work`, `sabotage`) | admitted | refused, every sign (`<verb>.refused`) |
  | yield (`loop/matter.py:591`) | as today | 0 `[ASSUMPTION — basis: a Locked Zone is "a place where becoming has been precluded", `canon/philosophy/09_terminology.md:117`]` |
  | the worker's headroom | its cost stays in his elastic while the Tenure is live (held load; `recover` cannot empty it) `[ASSUMPTION — basis: "It stands only while it is held, and the holding is the practitioner's", `06_operations.md:195-197` as quoted in verbs-13 §3.3 B]` | not held: the lock persists by itself ("Persists indefinitely", `09_terminology.md:117`) |
  | ends by | the weaver's `release`; his death (the Tenure-closing cascade on `(Person, exists)`). Nobody else ends it (gate F3) | `mend` by any practitioner present, which clears the field (CP-T07-04); neither the locker's choice nor his death |
  | strain for IN-35 | +1 per live Tenure in the Site's territory | +1 per locked Site |

  So `weave` is upkeep a weaver carries (a held load that occupies headroom, P20's shape paid in headroom rather than stock), and `lock`
  is a one-time price that outlives the locker and denies everyone the place, its owner included.
- **Owner.** `verb_table.yaml` rows; `rosters.yaml: tenure_kinds`; `state/carriers.py` (`Site.locked`) and its write-matrix row; the
  wear reader in `loop/matter.py`; the refusal in the staged accumulator `loop/resolve.py`; one Query `held_load(w, person)` and one
  `strain(w, territory)` in `queries/world_q.py`. `release`'s `domain:` (`verb_table.yaml:1034`) gains `weave`, as its loader
  invariant requires (verbs-13 §3.3 C).
- **Primitives.** P20 (a standing charge, here on headroom), P07-like lockout (a locked place cannot change), P38 via IN-35 (the world's
  threat sized by what practitioners hold).
- **Reads/writes.** Writes Tenure `weave` (open; the weaver's own edge) and `(Site, locked)` at RES; reads both in MATTER (wear,
  yield) and RESOLVE (accumulator).
  **Asymmetry check (§0.1 pt 1):** this changes what the condition getter's writers achieve. Writers of `Site.condition` at HEAD:
  the wear write `loop/matter.py:672-673`, the staged accumulator `loop/resolve.py:1132` (fed by `effects_economy.py:105`, `:176`,
  `:210`), and the harness `harness/probes.py:1717` (a probe, outside the season). The item routes the first two through the lock and
  weave readers; the probe is named in the test so a new bare writer reds.
- **Joins.** IN-35: *need* a strain input on its coupling rule (`strain(territory)`, weight at IN-35's control 0). REM-21 (RB-2a, Site
  referents): *need* questions to carry Site referents so `weave`/`lock` can form on a Site (T02 `:633-635`). T08 settlements: *give*
  locked and woven Sites; their yield and repair rules change where a shape is live.
- **Chooser / unwatched.** A weaver chooses what to preserve and how much headroom to tie up; a locker chooses to deny a place for
  good. Unwatched: an NPC practitioner's weave holds his town's mill against wear and raises his territory's strain; when he dies the
  weave falls and wear resumes.
- **Falsifier.** Paired seeds, one planted Site woven and its twin not: after one MATTER the woven Site's condition is unchanged and
  the twin's falls by `wear_per_season`. A locked Site refuses a planted `restore` and a planted `sabotage` and yields 0. A weaver
  with one live Relational weave rests a season in equilibrium and ends with elastic ≥ 1. Each fails if otherwise.
  **Control.** `ts_seed: none`; IN-35 weight 0 for strain.
- **Hash movers.** `Site.locked` is a SCHEMA mover (a new carrier field moves the hash by schema alone, H-208), declared; then wear
  and yield on shaped Sites, refusals on locked Sites, strain at IN-35 weight > 0. **Revert.** Delete the two rows, the kind, the field
  and its matrix row together; the readers have nothing to read.

### CP-T07-04 · `mend`'s targets beyond IN-35's lattice, and a price on self-repair · size M

- **Adds.** The `mend` row (R-26: `mend` is Mending; `restore` stays fabric) routes by target, each route on an existing owner:

  | target | on Success+ (Partial for another's configuration, as the oracle pays, `operations.py:494-509`) | owner it composes on |
  |---|---|---|
  | a lattice Site | IN-35's raise | IN-35 (`_rise`, `effects_economy.py:109`) |
  | a locked Site | clears `Site.locked` (a Site field, not anyone's edge, so no gate basis is needed) | `(Site, locked)` at RES, as `restore` writes `condition` |
  | another person | the **target's** elastic falls by the restorative term, if the target stands in equilibrium | the oracle's `recover(..., mending=term)` (`coherence.py:341-377`; E-1 "mending accelerates") |
  | oneself | resting point −1 (refused past the crossing) | `mend_resting_point` (`coherence.py:380-408`) |

  The mender's own elastic feedback stays as the oracle computes it (1-2, in equilibrium). **Price on self-repair:** each cast is one
  act (it now competes with the person's other ~6 acts), and the self-aim Ob gains a swept step `self_mend_ob_step ∈ (0, 2, 4)`,
  shipped at 0, passed by the host as one keyword on `attempt_mending` — the place the oracle's own `[GAP]` note puts the difficulty
  (`operations.py:159-167`; C-1 "extremely difficult to do but possible"). Today's arm is 0.
  **Not a target:** another person's live Tenure (his `weave`, his `ward`). The gate admits a Tenure write only by its owner, a
  maturing term, a seat's revocation or a cascade (`engine/season/state/gate.py:109-117`, 04 §C.2), and no basis lets a third party
  close another's edge; verbs-13's "undo another's weave" fold is therefore not built (cross-file ruling R8, the reshape preferred over
  a Layer 1 amendment). A weave ends by its weaver's `release` or death only.
- **Owner.** The `mend` row and its effect; the fixture in `Fixtures`; one keyword on the oracle entry (the only oracle edit in this
  file, a parameter, not a rule).
- **Primitives.** P40 (recovery bought by an act, gated by place through CP-T07-05), TM01's recovery leg.
- **Reads/writes.** `(Person, coherence)` for mender and target (both through the seam, one Event each); `(Site, locked)`; lattice
  Site via IN-35.
- **Joins.** IN-35: *need* its Mending arm to be `mend`. This is an **edit to IN-35's text** (`workplans/valoria_master_workplan_v9_part5.md:91`
  reads "Mending as persons' acts (the `restore` arm)"), proposed on verbs-13 §3.3 D's fold test, held back with the rest of this file.
  The roster clause at `rosters.yaml:2765-2770` is a separate matter: it withholds two affiliation cells from `restore` until "a
  thread-operation verb … exists", and CP-T07-09 lands both on `mend`. T10 NPC life: `tend` stays bodies; thread healing of a body is
  not built here.
- **Chooser / unwatched.** A mender chooses between holding back the Calamity, freeing a locked place, easing another practitioner
  (a social bond the healer earns), or walking back his own set. Unwatched: menders work the lattice; a stretched NPC practitioner can
  be eased by a knotted friend.
- **Falsifier.** At `self_mend_ob_step` 4, a planted practitioner at resting 2 does not reach resting 0 within one season in more than a
  stated share of 100 seeds where at step 0 he does (the share is the measurement; it must differ between arms or the knob is dead).
  `mend` on a locked Site clears `Site.locked`; `mend` on another person lowers that person's elastic and leaves his resting point; a
  `mend` naming another's live `weave` cannot form. **Control.**
  Step 0 = today's oracle; `ts_seed: none`.
- **Hash movers.** Every executed `mend`. **Revert.** Step to 0; delete the non-lattice routes.

### CP-T07-05 · Equilibrium decided by place · size S

- **Adds.** One Query `in_equilibrium(w, person)`: True unless the Site the person is contained at is `locked`, or its
  territory's Calamity band, read through `calamity_band(w, territory)`, is below `equilibrium_band_floor` (a fixture).
  `calamity_band` is the name this file expects for IN-35's "effect per territory as a Query over band floors" (`_part5.md:91-92`);
  IN-35 owns it, and T10 depends on the same Query (T10's demand, not this file's). The host
  passes it as the oracle's `environment_in_equilibrium` for recovery (CP-T07-06) and Mending feedback (CP-T07-04).
- **Owner.** `queries/world_q.py`; the fixture in `Fixtures`. **Control:** `equilibrium: everywhere` (always True), a fixed arm.
- **Primitives.** P40 (recovery gated by place: Darkest Dungeon II's Inn, Pathologic 2's beds; D_T07 #23).
- **Reads.** `contain` Tenure, `Site.locked`, `calamity_band`. Writes nothing.
- **Joins.** IN-35: *need* its effect-per-territory Query (named in IN-35's *Builds*, `_part5.md:91-92`). T10 travel: *give* a reason to
  `move` (a stretched practitioner travels to a stable place to recover, paying a leg).
- **Falsifier.** A planted practitioner contained at a locked Site recovers 0 over a season; moved to an unlocked Site he recovers 6.
  At `equilibrium: everywhere` both recover 6. **Hash movers.** Recovery amounts where a place fails. **Revert.** The fixed arm.

### CP-T07-06 · Recovery as a projection, written at the next seam write (K-WR-8 answered) · size S

- **Adds.** IN-06's `[ASSUMPTION]`, specified: no step writes coherence. The **read** (`threadwork.coherence_band` and the host) projects
  elastic return as the oracle's `recover(seasons=Δ, environment_in_equilibrium=…)` where Δ = seasons since the person's last
  `coherence.changed` (`w.last_emission_of`, the reader `matter.py:670` already uses), floored at CP-T07-03's `held_load`; the **write**
  materialises the projection inside the next seam Event, before that act's stress. Equilibrium is read at materialisation
  (one read for the interval; stated, not hidden).
- **Why this is not an ask.** verbs-13 §3.9 item 1 asked "a licensed clock or a rest a person chooses". Step 3 answers the game: E-1
  is ruled ("time is the mechanism, environmental equilibrium is the condition, mending accelerates", `coherence.py:39-40`). Step 5
  answers the mechanism: a read-time projection writes nothing on its own, so it is not a fourth clock (`write_matrix.yaml:190`), and
  no rest verb is needed (verbs-13's `anchor` cull stands).
- **Owner.** The host and the query. **Primitives.** P03 (a value that reaches the world with elapsed time), P40.
- **Asymmetry check.** This changes what the coherence getter computes. Assignments to `(Person, coherence)`: the gate admits only
  `driver="Seam"` (`state/world.py:1014-1021`), so the only writer is CP-T07-02's host; the test greps for a second assignment.
- **Falsifier.** A practitioner at elastic 4 who takes no thread act for one season reads band Stable at the next deliberation and
  writes elastic 0 at his next working, in equilibrium; out of equilibrium he reads Fragmented. **Control.** `ts_seed: none`.
- **Hash movers.** Every later working's charge arithmetic. **Revert.** Projection off (Δ = 0): today's oracle-only behaviour.

### CP-T07-07 · Permanent set narrows the season · size M

- **Adds.** The scene budget subtracts a coherence penalty beside the body's: `budget()` already does `b -= body_band_penalty(p, fx)`
  (`decision/budget.py:57-60`). The penalty reads the **resting point's band**, carried on `Person` and written by the seam in the
  same `coherence.changed` write that moves the resting point (the oracle's band owner, `coherence._displacement_band`,
  `:154-162`, computes it; nothing else writes it). Why the resting band and not the present one: `budget(p, k, fx)` is person-side
  and admits `fx` only because it is "identical for every person … not world state" (`decision/budget.py:49-55`); a present band
  projected from `w.last_emission_of` and a place-based equilibrium would be a World read handed in. The resting point changes only at a
  seam write (recovery never assigns it, `coherence.py:28-30`), so the carried band is never stale and no World is read. A per-band
  table `coherence_band_penalty` (Stable, Dissonant, Fragmented, crossed), swept `(0,0,0,0)` / `(0,0,1,2)` / `(0,1,1,2)`, shipped at
  all-zeros. No band edges are copied into a second table (the rule `body_band_penalty`'s docstring states, `budget.py:72-76`).
- **Owner.** `decision/budget.py` (one term); `Fixtures`; the band carried in IN-06's `(Person, coherence)` value (a third member
  of the structured field, beside the two quantities IN-06 keeps apart).
- **Primitives.** P01 (bands that apply modifiers), P05 (the per-season budget), P32 (a lasting mark that changes the person's numbers).
- **Joins.** IN-06: *need* the structured coherence field to carry the resting band written at the seam. T08: CP-T08-10 edits the
  same lines (`budget.py:57-58`); the two items are **serialised** on that file (whichever lands second rebases and re-runs the
  other's falsifier).
- **Chooser / unwatched.** Stretch is felt as headroom and in CP-T07-06's band reading; set is felt every season: a practitioner who
  takes permanent set has fewer acts until he mends it back. Unwatched NPCs who overwork shrink their own seasons for good.
- **Falsifier.** At `(0,1,1,2)` a planted practitioner at resting 2 (Dissonant) has a budget one less than his resting-0 twin at the
  same holdings, and his elastic stretch changes neither; at all-zeros they are equal. **Control.** All-zeros = today. **Hash movers.**
  Budgets of practitioners with set at a non-zero arm. **Revert.** All-zeros.

### CP-T07-08 · The crossing as a witnessed breach, with an outcome slot · size M

- **Adds.** When a seam write carries a resting point past `HUMAN_BAND_LIMIT` for the first time, the host emits one Event
  `coherence.crossed` (subject: the person), fanned at WITNESS like any Event, so those present hold a Claim about it. A roster
  `crossing_outcomes` keyed by TS band (P-15's "TS-gated branching", `coherence.py:67-70`) names the consequence, shipped as `none`
  for every band (today). A knot arm (P-12, drift propagates along knots): each live `knot` partner of the crossed person takes one
  stress event of `crossing_knot_stress` (control 0) through the seam. The crossed person keeps acting; no game over (D_T07 #7, ruled).
- **Owner.** The host (the Event), `rosters.yaml: crossing_outcomes`, the fixture. The outcome **content** is Jordan ask A1 (§6).
- **Primitives.** P02 (breach event with an outcome fork, odds from the holder's own state), P27 (others learn of it), P11 via knots.
- **Reads/writes.** Event; `(Person, coherence)` of knot partners (seam); IN-32's `knot` Tenure as reader.
- **Joins.** IN-32: *need* a directed, readable `knot` Tenure. T09 factions / T05 social: *give* a witnessed Claim the orthodox can act
  on (charge, `arrest`).
- **Falsifier.** A planted practitioner driven 0 → crossing by three Structural lock Failures (T07 §2.3) emits `coherence.crossed`
  exactly once, and a co-located witness holds the Claim after WITNESS; a fourth working emits none. At `crossing_knot_stress` 1 his
  knot partner's elastic rises by 1; at 0 it does not. **Control.** Outcomes `none`, knot stress 0.
- **Hash movers.** The Event and its Claims (new kinds), wherever a crossing occurs. **Revert.** Delete the emission.

### CP-T07-09 · Every thread row is a witnessable, celled deed · size S

- **Adds.** On `weave`, `lock`, `mend`, `ward`: affiliation cells on the three columns `thread_read` already has
  (`solmund_orthodoxy` −1, `inner_tradition` +1, `thread_truth` +1; `rosters.yaml:2793-2797`); on `mend` also the cell the roster's
  revert clause holds for "a thread-operation verb", `einhir_restoration` + (`rosters.yaml:2765-2770`), landing with that clause's
  `solmund_orthodoxy` − `[UNVERIFIED: at HEAD `einhir_restoration` appears as a pole at `rosters.yaml:2712-2724`, not as a `cells:`
  column, so carrying it may add the column]`; and pursuit-axis cells or an
  `uncelled:` reason per IN-08's loader rule (`_check_alignment_density`, `_part5.md:43`). Conspicuousness is the observer set
  WITNESS already computes (ED-FI-0009's retraction; T07 §0): no Exposure meter. Because every row now moves state at RESOLVE
  (`coherence.changed`, a Tenure, or `Site.locked`), the scar can fire (`rosters.yaml:2776-2778`). A Personal-scale `thread_read`
  whose Leap takes costs 0 and writes nothing (`COHERENCE_COST_BY_SCALE`, `operations.py:128-136`), so a quiet reading is no deed to a
  witness; a Relational one is, and so is a fumbled Leap (−1).
- **Owner.** `rosters.yaml` cells (data). **Primitives.** P13 (a breach count, here scars on witnesses), P33 (a conviction folds at scar
  ≥ 3, `person_q.py:579-580` per D_T10 #25).
- **Joins.** T02 / IN-08: the cell values ride the CELL-VALUE AND COSINE PASS (remediation JQ-3's annex); this item adds rows to it,
  not values of its own beyond the three signs already authored.
- **Chooser / unwatched.** Working in front of the orthodox is a choice with a social price; the unwatched world scars orthodox
  witnesses of an NPC weaver and may fold a conviction.
- **Falsifier.** A planted orthodox witness co-located with an executed `weave` gains a scar on `solmund_orthodoxy`; with the witness
  absent, none. **Control.** `ts_seed: none`. **Hash movers.** Scars and pursuit scores for thread rows. **Revert.** Remove the cells.

### CP-T07-10 · What `thread_read` finds · size M

- **Adds.** Two finding contents a non-sensitive cannot mint: on a Site, which shapes it carries (live `weave` and `ward` Tenures,
  `Site.locked`, and `calamity_band` where IN-35 has one); on a person (verbs-13's `diagnose` fold), his band and whether his TS is
  ≥ 30. **Why today's route cannot carry it:** `inquiry_modules` is keyed by the emitted kind, `finding.made` already maps to
  `fieldwork.find`, and an ungraded `finding.made` (`thread_read` is one) "reaches the row and finds nothing" because `finding_terms`
  keys on the degree (`rosters.yaml:2486-2500`); `trail_of` returns covert deed Events, not live shapes or bands. **So:** the row's
  roll is its Leap stage in CP-T07-02's host (canon's stand-alone perceptive Leap, verbs-13 §3.3.0), which grades it; on Partial or
  better the row emits a **new kind `thread.read`** carrying that degree; on Failure it emits `finding.none`, which no row claims, so
  nothing is found (the existing rule, no band branch). A row `inquiry_modules.findings."thread.read"` →
  `{module: threadwork, provider: threadwork, module_entry: threadwork.read}` mints the Claim at WITNESS.
- **Owner.** The **single owner of what a shape is** is `threadwork.read` (the module entry), which reads `weave`/`ward` Tenures and
  `Site.locked` through Queries and the person's carried band; `thread_read`'s `emits:` changes from `finding.made` to `thread.read`.
- **Primitives.** P26 (the ledger), P24 (TS gate).
- **Joins.** T06 fieldwork (FI-G01): T06 replied "none required … finds through `trail_of`"; that answer covers `finding.made`, which
  this row stops emitting. *Need* T06 to accept, in its file, the `thread.read` row under the `inquiry` role (R-13: TW owns the gate
  and cost, FI the finding shape) and the graded-event shape its provider reads `[UNVERIFIED: the field a graded inquiry's Event
  carries its degree in]`.
- **Chooser / unwatched.** A sensitive hunts hidden practitioners (an orthodox inquisitor with TS has a reason to exist) or scouts a
  place before working it. **Falsifier.** A planted practitioner reads a woven Site and holds a Claim naming the weave; a reader at TS
  25 cannot form the act. **Control.** `ts_seed: none`. **Hash movers.** `thread_read`'s Claims. **Revert.** Drop the kind.

### CP-T07-11 · `ward`: protection that routes a working into a contest · size M

- **Adds.** The `ward` row: Tenure `ward` (warder → Site or person) with a one-season `Term` (the field `oblige` uses). Any working on a
  warded target by someone other than the warder resolves through `opposing.resolve_opposing_operations(actor, warder, …)`
  (`opposing.py:102`) instead of the solo entry, and both sides pay through the seam. No "hostile" classifier: the ward routes every
  other person's working. `release`'s domain gains `ward`.
- **Owner.** The row, the kind, a branch in CP-T07-02's host. **Primitives.** P23 opposed, P14-like term (`Term`, lapses unless renewed).
- **Joins.** Builds with CP-T07-03 (its first reader: a `lock` on another's Site), verbs-13 §3.3 E's build condition.
- **Chooser / unwatched.** Pay now against a working that may never come; an unwatched ward that fires on a rival's lock is a story
  nobody scripted. **Falsifier.** A planted `lock` on a warded Site rolls the opposed resolver (both sides charged); on an unwarded
  twin it rolls solo. **Control.** No ward. **Hash movers.** Workings on warded targets. **Revert.** Delete the row and kind.

## §3 NERS

Method per `skills/ners/SKILL.md`; definitions `CLAUDE.md` §0.06. Cut test, item by item, then E as a ratio.

- **Cut proposed and taken: `dissolve`** (not an item). With no item it dies: an operation that ends a Site's fabric and leaves residue.
  **False N-line:** ending fabric is already `sabotage` (`_fall` brings a fabric to 0 alone, `effects_economy.py:141-158`) and `raze`
  (`verb_table.yaml:1105`); ending a held shape is `mend`, which costs 0. What would be unique is residue, which matters only once
  something reads it (equilibrium, strain), and a `dissolve` that wrote only `_fall` plus a Coherence charge would be verbs-13's own PARK
  falsifier ("writes exactly what `lock` writes", or here, what `sabotage` writes). PARKED, trigger: a reader of residue is ruled in.
- **Cut proposed and taken: collective workings** (gap R). Dies: deep work beyond one pool (Foundational Ob 13 fails 0.988 at pool 14,
  T07 §2.1). The narrowed N-line is real (menders against the Calamity), but it holds in one direction only (top-down, IN-35) until IN-35's
  managed arm is measured with solo menders; the structural cost (ENCOUNTER-time coherence writes) is large. Trigger in §7.
- **Cut proposed, refused: CP-T07-07 (permanent set narrows the season).** Without it set is felt only at the crossing (gap B), against
  the genre's central expectation (TM01, every sampled title, T07 §2.3). False N-line check: CP-T07-03's held load already makes
  displacement matter — but only for weavers, and only as headroom, which is the label problem again. It stays; its magnitudes ship at
  0. Narrowed by the fix pass: it reads the resting band only (person-side), so stretch alone never costs acts.
- **Cut proposed, refused: CP-T07-11 (`ward`).** Without it, a `lock` on another's Site has no counter but `mend` after the fact.
  N holds bottom-up (a person protects his place) and laterally (social: a warder is an ally worth having). It is the item most likely to
  be thin in play; it is ordered last.
- **CP-T07-05 vs a fixed True.** Cutting it leaves recovery free everywhere: R loses place as a strategic variable (P40 dies). Kept.
- **R, the half with no player.** Every item runs for NPCs through the same chooser: four seeded practitioners weave, lock, mend and
  are seen; the Calamity's strain is theirs; crossings are Events others witness. R's completeness clause: at the extremes — TS 100
  (pool 8 + 3 + 10), resting 5 (one unit of headroom), a weaver who dies holding three weaves — each item's rule still writes a defined
  value (the cascade closes his Tenures; headroom 1 still admits an Object working at cost 0).
- **S.** One host, one ladder, one seam writer; condition readers reuse `_rise`/`_fall`, the accumulator and the wear loop; budget reuses
  `body_band_penalty`'s shape; recovery reuses `recover`. Carried S defects, not fixed: `MENDING_OB` beside `DEPTH_OB` (a second Ob table,
  canon-sanctioned, verbs-13 §3.3 D); the thread pool as a separate practice-to-dice formula (J-T6, TW-G27).
- **E, scored last, as a ratio.** Eleven items against the ten-row yardstick: G1-G10 go from five ABSENT, five PARTLY, zero AFFORDED to
  eight AFFORDED-by-design and two PARTLY (G4 until A1 fills the slot; G9, opposed only), for four verb rows (`weave`, `lock`, `mend`,
  `ward`), two Tenure kinds and one Site field, one host, three Queries, four swept fixtures, two Event kinds and one oracle keyword. The overhead a player must hold is small: pick a
  target, pay headroom, rest somewhere stable. The weakest ratio is CP-T07-08 (an Event and a slot whose content is unruled).

## §4 One season, after

Practitioner: NPC-001 Edeyja, Warden-Chief, seeded TS 75 (`npc_registry.yaml:55`), Spirit 4 (oracle default until J-T1), history 0:
pool 8 + 3 + 7 = 18, Leap Ob 1 (TS 50+). Fixtures at the non-zero arms named; degrees are **illustrative** (no run exists); costs and
state transitions are the oracle's arithmetic (T07 §2.2-2.3) applied to those degrees.

1. **Round 1.** A Site referent in her ledger is a mill in her territory, worn toward a band floor. She forms `weave` (Site → Field,
   Ob 5, cost −1). Leap: Success (0). Weave: Partial (−1 −1 = −2). Resting 0, elastic 2, Dissonant. Partial opens no Tenure (Success+
   only); the charge stands. An orthodox clerk is present: the act moved state (`coherence.changed`), so his `solmund_orthodoxy` scar
   rises (CP-T07-09).
2. **Round 2.** She weaves again: Success (−1). Elastic 3; Tenure `weave` live; the mill's wear is skipped this MATTER; her territory's
   strain is +1 (at IN-35's weight 0, nothing follows). Her held load is 1.
3. **Round 3.** A rival practitioner's `lock` on the mill would now be one other person's working on a woven Site; it is unwarded, so it
   rolls solo. She instead reads the rival (`thread_read`, Personal, cost 0, no deed): her ledger now holds his band and that his TS ≥ 30.
4. **Round 4.** She mends a friend knotted to her (another person: Ob 2, cost 0): Success. If both stand in equilibrium, her elastic −1
   (the oracle's feedback, Personal priced as Relational) and his −1 (CP-T07-04). Her state: resting 0, elastic 2.
5. **Next season's deliberation.** She ends the season present-Dissonant with resting point 0, so at `coherence_band_penalty
   (0,1,1,2)` her budget loses nothing: only set narrows the season (CP-T07-07). The projection (CP-T07-06) reads one season elapsed,
   in equilibrium: elastic max(0, 2 − 6) floored at her held load 1 → present 1, Stable, and that is what her next working starts from.
   Had she stood at a locked Site, the projection would return nothing and she would start her next working at elastic 2, with 4 units
   of stretch before set; a stable place is worth a `move`. Had she taken 2 units of set, she would deliberate one act short until she
   mended it back. Her mill weave still holds.

**Unwatched, same season (illustrative).** NPC-075 Orm locks a rival hamlet's granary out of pursuit; it yields 0 from the next
MATTER, nobody can repair it, and it persists after him. NPC-002 Maret, pressing three Structural workings without rest, crosses: one
`coherence.crossed` Event, Claims in the ledgers of everyone present, and nothing more until A1 is ruled. The clerk's scar reaches 3
across the season; his conviction may fold (D_T10 #25's crisis).

## §5 Order and dependencies

**Within the proposal.** CP-T07-01 → CP-T07-02 → {CP-T07-05, CP-T07-06} → CP-T07-04 → CP-T07-03 → CP-T07-11 (with -03's first hostile
reader); CP-T07-09 lands with each row it cells; CP-T07-10 after -03 (it reads shapes); CP-T07-07 after -06 (it reads the projection);
CP-T07-08 last. Each item is its own commit with its falsifier.

**Needs from others (interface, as expected).**

| from | interface |
|---|---|
| v9 IN-06 (B-S) | oracle entries return their cost; composition rows `threadwork.<op>` and `threadwork.coherence_band`; `(Person, coherence)` as two quantities plus the resting band written at the seam (CP-T07-07) |
| v9 PC-06 K-3 (B-S) | the TS field on `Person` and a typed precondition evaluable at formation |
| v9 IN-35 (B-S) | a strain input on the coupling rule; its per-territory band Query, expected as `calamity_band(w, territory)` (T10 depends on the same Query); `mend` as its Mending arm, an edit to `_part5.md:91` |
| v9 IN-32 (B-S) | a directed `knot` Tenure that can be read |
| v9 WR-01 (B-S) | the resilience slot the adapter fills |
| REM-45 (RB-4a) | the corrected history term, before B-S |
| REM-21 (RB-2a) | Site referents on questions, so Site-aimed rows form |
| T01 | `faculty(p, verb)` exposing `spirit` and `history` as registered addends by name; `verb_capability` rows for the five thread verbs |
| T02 / J-T1, JQ-2 | the ruling on a stored Spirit (JQ-2 gates it) or on its derivation |
| T06 / FI-02 | acceptance, in T06's file, of a `thread.read` row under the `inquiry` role and the graded-event shape its provider reads |
| T08 settlements | serialisation of CP-T08-10 with CP-T07-07 on `decision/budget.py:57-58`; otherwise they receive the wear, yield and repair readers |

**Gives others.** T08: woven and locked Sites (preservation, denial). T09/T05: witnessed thread deeds and `coherence.crossed` Claims
for persecution (`arrest` exists since B-R). T10: a reason to travel (equilibrium by place). T04: nothing; `threadwork_check`
(`modules/mass_battle/orchestration.py:333`) stays an empty hook (TW-G30, PARKED).

**Placement.** B-S is the earliest batch that holds the carriers; the items edit `verb_table.yaml`, `rosters.yaml`, `loop/matter.py`
and `loop/resolve.py`, so `_part3` §B.0's R1/R3 rules place them in or after B-S, serial with B-Y and B-T on the shared files.

## §6 Jordan asks

**A1 · What does a person become when he crosses?** P-15 requires a consequence gated by reach ("TS-gated branching",
`coherence.py:67-70`); no document gives its content (K-WR-5, TW-G11; verbs-13 §3.9 item 3). Five steps: not superseded; not irrelevant
(the latch exists and every heavy worker reaches it); no design document names the branches; the tree's precedent (a scar crisis folds
a conviction, D_T10 #25) gives the *shape* — CP-T07-08 builds it — not the content; architecture is silent between materially different
games: **(a)** he stays a person who acts, rewritten (a conviction folds toward `thread_truth`, witnesses fear him), or **(b)** he leaves
the cast as persons know it and becomes a standing source of strain on his territory for IN-35. Either fills `crossing_outcomes`, by TS
band. Nothing waits on the answer: the slot ships at `none`.

**Asks not raised** (one line each, five-step order):
- K-WR-8 (recovery: clock or rest act) — step 3, E-1 ruled; step 5, a read-time projection (CP-T07-06).
- Knot permanence (verbs-13 §3.9 item 2) — step 2 for this file: no item opens a knot; IN-32 owns it.
- Self-repair difficulty (TW-G09, M7) — step 5: a swept fixture at control 0 (CP-T07-04), H-94's shape.
- Resilience arithmetic (R-14, TW-G28) — step 2 here: WR-01 owns it.
- History term (TW-G26) — owned by REM-45, gated on PP-624.
- Leap's blanket −1 (C-TW-3) — step 1: carried on ED-WR-0005; this file applies the oracle as built.
- Locked-Site yield 0 and target-derived scale — step 5: `[ASSUMPTION]`s with their canon basis, revert = today.
- Cell values — step 2 here: the CELL-VALUE AND COSINE PASS (remediation JQ-3).
- JQ-1…JQ-6 are not duplicated. **JQ-2** touches threadwork: whether J-13's "not a character attribute in and of itself" binds
  resolutions beyond the proceeding (remediation part 04 `:32-55`) gates CP-T07-01's stored `spirit` read; it is cited, not re-asked.
- The gate basis for a third party closing another's Tenure (a Layer 1 amendment to 04 §C.2 / `state/gate.py:109-117`) — not raised:
  CP-T07-03/-04 are reshaped so that no item needs it (cross-file ruling R8).

**Rulings the items touch** (each respected, none reopened): C-1, C-2 (one channel; stacking), E-1..E-4 (time and equilibrium recover;
sensitivity orthogonal; no hardening; only events deform), ED-871 (Mending costs 0), P-08 (TS fixed), P-12, P-15, R-02/R-10/R-13/R-26,
#457 D1 (the Calamity is a consequence of held configurations), the write gate on `(Person, coherence)`.

## §7 Risks and what this deliberately does not do

- **Few practitioners.** Four persons seed TS ≥ 30 at HEAD's registry; the unwatched half is thin until the cast is authored. The
  registry is the owner; this file invents no values.
- **NPCs who never stop.** The chooser has no state term reading displacement (its score is pursuit + stance + a constant urgency,
  `decision/choose.py:130-151`), so an NPC with strong `thread_truth` pursuit keeps working while Fractured. CP-T07-07 bounds it by
  budget; it does not make NPCs prudent. A state-aware score is T02's D-V6, not this file's.
- **The weave is strong.** A one-time cost for indefinite wear suspension is held back only by held load and strain; if IN-35's weight
  stays 0, weaving is close to dominant for practitioners with headroom. The measurement is the paired-Site falsifier plus IN-35's arm.
- **Lock as griefing.** A lock denies a place for good and only `mend` clears it; with few menders, locked places accumulate. That is
  canon's Locked Zone, and the risk is measured by counting live locks per territory over seasons.
- **Projection staleness.** Equilibrium is read once per interval at materialisation (CP-T07-06); a practitioner who rested in a stable
  place and moved into a locked one before his next working is credited at the second place.
- **Does not do:** `dissolve` (PARKED, §3); collective workings (trigger: IN-35's managed arm fails to stabilise with solo menders at
  control magnitudes); `pull` and past-pulling (PARKED on P-09's orphan carrier, M9); involuntary Leap knots (M3's `[ASSUMPTION]`);
  co-movement cards and threadcut beings (unplugged per IN-06); the mass-battle hand-off (TW-G30); person-targeted `lock` or `weave`;
  `mend` on another's live `weave` or `ward` (no gate basis; a weave has no counter but its weaver's release or death, which is a
  known strength of the weave, see the risk above); a producer for thread `history` (gap J);
  any guard over process; any screen.
