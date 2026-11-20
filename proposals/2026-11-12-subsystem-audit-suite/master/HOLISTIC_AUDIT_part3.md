# Holistic audit — part 3: the nine requirements, the cost of porting, the evidence log

## Status: REFERENCE (part 3 of `master/HOLISTIC_AUDIT.md`; resolves nothing at runtime)

Reconciled: 2026-11-12, A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "capability" in prose → skill (2).

## 7. The nine requirements, read against the code as it stands

**The instrument's reading**, run by this lane: `python -m engine.season.harness.register --requirements`
prints `met 3 · not_met 1 · partial 5` (R-01, R-02, R-03 met; R-05 not met). It is doc-derived by its own
statement (CLAUDE.md §0.2; `layer-conformance` THE CONTROL: *"its counts are hand-edited YAML"*).
`python tools/m1_acceptance.py --summary` prints `verdict: NOT MET`, one row failing: rows 1, 2 and 4
execute the engine (0 stub invocations; the same hash from two runs at seed 20260819, `bbf88d55e218…`; 0
invariant violations over 24 seeds of four seasons and two populated runs), row 3 is the 3 of 9.

**This lane's reading** is beside it, per row, from runs it made (§9) or opened. "Executes" below means a
seeded run of the shipped realm showed the behaviour; it is not a claim that the row's own `measure:` was
re-run, and where that matters the row says so. A verdict is this lane's, on what it could observe.

| row | statement (short) | register | what a run shows | verdict of this audit | what moves it, and where |
|---|---|---|---|---|---|
| **R-01** | decisions propagate | met | seed 0, one season: 749 resolved acts leave 13,379 Events, 12,115 of them `claim.deposited`; ledgers grow from 236 to 12,351 claims, 6,040 of them `told_by` and 297 `inferred` (`runs/HOLISTIC/nine_probe.json`). `loop/witness.py` 9 of 12 functions entered (`W4`) | **executes.** The row's own criterion is a degree-sweep reading on one committed log (`audits/01_CORE_audit.md:174`), not re-run here | the measure replaced by one a batch can re-run: `proposals/16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md` (B02) |
| **R-02** | decisions affect later decisions | met | not observed by this lane: the measure is `proposals/2026-09-04-degree-sweep/wd_collect.py` after 36 chunk cells, about 75 minutes (`dossiers/00_NINE.md`; `audits/01_CORE_audit.md:175`) | **INCONCLUSIVE here**; the register's `met` rests on a committed log. Placement defect H-12 | the same proposal (B02) |
| **R-03** | seasons tick scene by scene | met | `headless --case NPC-088 --seasons 2 --seed 0`: `rounds=5 acts=16 events=17` then `rounds=5 acts=17 events=92`, hash `5405522c36b0399247f83fd9f6d29494` | **executes** as rounds within a season. A-9 changes a turn to a short sequence, so the row's meaning moves | `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order` (B08) |
| **R-04** | strategic and management actions at differing scales | partial | settlements' `produce` and `subsist` run once a season from MATTER; the field resolver is entered at seed 0 in the third season and at seed 2 in the first; the army record's four rows and `effects_army.py` are entered by no run; founding 1 of 9 functions (`W3`, `W4`) | **partial, and narrower than the register's sentence**: two of the management engines (the army, founding and works) have code and rows and no computed act reaches them (H-01) | B12 (ground, works), B21 (governance), B22 (armies); CI-11 gives the reading |
| **R-05** | all verbs built out | not_met | one season at seed 0: 42 verbs are attempted, 26 execute and 16 are only refused (`audits/25_GROUNDING_ENGINE.md` L-14; this lane's run of the same world counts 39 verbs in the fold set); 34 of 67 execute in neither the corpus nor three seasons (`audits/17_CENSUS_REST.md` §0) | **not met**, and it is the largest obstacle: H-01 is this row seen from the engines | B07 (the task draw), then the verb families' batches |
| **R-06** | characters robustly built (goals, convictions, values) | partial | at `build_realm(0)`: all 83 persons carry `pursuits`; 35 carry `stance`; 2 carry `capability` (`{inquiry: 2}` each); 0 carry `attributes` (`nine_probe.json`; `audits/25` L-06, L-08: `cast_attributes=False` ships) | **partial**: people differ in what they pursue and hold, not in what they can do. Any two persons roll the same pool on a verb unless one of them is one of the two who hold a skill | B04 (the capability home), B10 (character) |
| **R-07** | memory, feelings, attitudes, relationships; imperfect knowledge | partial | ledgers fill by channel (above); the chooser's module imports no `World`: `decision/` has five import edges into `state/`, all to `carriers.py` (`W2`). The row's measure is three tests, not run (no `pytest`) | **partial; the knowledge half executes and is separated by module path**; feelings and relationships were not observed by this lane | B09 (memory), B10 |
| **R-08** | decisions not omniscient, not perfectly rational | partial | the chooser takes a draw (`harness/probes.py:288-289`, `draw_factory`) at `choice_temperature = 0.05` (`nine_probe.json`); its measure (`corpus_run`, the ranking line) was not re-run | **partial; mechanism present, effect not measured here** | B10 (`02_CHAR_choice_alignment`, `02_CHAR_resolve_and_temper`) |
| **R-09** | chains of events within a scene are probabilistic | partial | seed 0, one season: 61 of 13,379 Events carry a degree; 48 rolls and 62 graded findings account for them (`W3`); 92.7 % of success Events carry none (`audits/25` L-15) | **partial, and by execution closer to not met in the shipped realm**: most outcomes are a fixed function of state, against the standing rule (A-24) | B05 (the one roll), B06 (the keyed draw), B07 (the task draw) |

**Across the nine.** The three rows the register reads `met` are the three the season core, the chooser and the readers serve (E1 to E3):
propagation, consequence, ticking. The six that are not met are served by the resolver engines and the
character data (E5 to E9, and the cast), which is where H-01, H-04 and the skill lanes sit. The core
is ahead of the engines it hosts.

## 8. The cost of porting each engine to Godot

**What this section can and cannot say.** `valoria-simplify` THE PORT NOTE requires the GDScript side to be
read in the reference for the ruled series (`ED-GO-0002`) and quoted. This lane made no outbound read, so
**the GDScript half of every line is `[NOT READ]`** and each line names the Python construct only. `04`
§C.8–§C.10 and §C.12 state the degradations the architecture already accepts (*"No private constructors …
No module system … No exceptions (typed results everywhere; a refusal is a value) … Recursion depth is a
crash"*, `04:899-903`); those are cited as Layer 1's statements, not as facts about GDScript checked here.
Cost class is this lane's ordering by the size of the Python and the count of constructs `04` names as
degrading; it is a ranking (`valoria-simplify` I7: rank only), not a measurement.

Construct counts per engine (`ast`, non-test; `runs/HOLISTIC/` and §9):

| engine | code lines | `def` | `raise` | `try` | comprehensions | lambdas | reflection calls | import by string | decorated `def` |
|---|---|---|---|---|---|---|---|---|---|
| season core (`loop`, `state`) | 4,871 | 395 | 86 | 9 | 206 | 42 | 139 | 0 | 79 |
| chooser and readers (`decision`, `queries`, `epistemic`) | 4,057 | 397 | 67 | 2 | 364 | 30 | 74 | 0 | 9 |
| data channel (`data`, `manifest`, `substrate`) | 4,279 | 284 | 267 | 8 | 186 | 7 | 151 | 4 | 2 |
| seam | 835 | 71 | 20 | 1 | 25 | 4 | 18 | 1 | 6 |
| dice engine | 216 | 30 | 3 | 0 | 6 | 0 | 0 | 0 | 1 |
| personal combat | 2,560 | 195 | 11 | 1 | 42 | 6 | 59 | 0 | 7 |
| mass battle | 5,194 | 339 | 66 | 5 | 264 | 34 | 99 | 0 | 23 |
| social contest, fieldwork, settlements | 196 | 13 | 2 | 0 | 13 | 1 | 0 | 0 | 1 |
| instruments (`harness`, `reference`) | 9,619 | 601 | 153 | 23 | 832 | 96 | 114 | 0 | 123 |

(Reflection calls are `isinstance`, `getattr`, `setattr`, `hasattr`. The grounding lane counts 586 `raise`
statements in non-test `engine/season`, `audits/25` L-24; the table's rows sum to the same order.)

| engine | what must be ported | the Python constructs that carry the cost | what lowers it | class |
|---|---|---|---|---|
| **dice engine** | all of it; it is the oracle's roller | arbitrary-precision `int` and float arithmetic in the leverage sums (`04` §C.8–§C.10: *"Fixed point for `condition`, `stores`, `margin`"*); the draw, which `04` §C.12 as amended on 2026-11-12 (A-30) makes a function of its key | A-30 (one draw per key, the same keyed hash on both sides: B06) and A-29 (declared floats: `11_GO_float_contract`) settle both | **small** |
| **the small modules** | all; 196 code lines, dataclasses in and out | frozen dataclasses | nothing needed | **small** |
| **the contest seam** | all | one import by string (`sigma.py:246`, H-05); the adapters' `dict` return (H-06); `raise` for refusals (20) | CI-03 removes the reflective edge; the typed-outcome proposals (B14, B17) remove the `dict` | **small, after those** |
| **the data channel** | the loader and its invariants; the registries as `Resource` or JSON (`04:924`) | 267 `raise` sites are the loader's refusals: each becomes a boot failure with the row named (`04` §C.12 row *"a failed invariant must abort the boot"*); 713 KB of the two largest registries is mostly text the port does not need (H-03); the 101 settings are not in any export (H-04) | CI-01 shrinks what is shipped; CI-04 and CI-05 put every value in one artifact with a round-trip check | **medium** |
| **the chooser and readers** | all; this is the people | 364 comprehensions over stores (density, and order: dict iteration and `sorted` at 95 sites decide ties); 39 dataclasses; `world_q` as 191 free functions over `World` | a keyed draw for every tie (B06); nothing structural | **medium to large**: the largest body of logic with the least apparatus |
| **the season core** | all | unforgeable tokens (`04` §A.3 row 3) need a private constructor; `04` §C.8 already grades that MECHANICAL by scan in GDScript; 79 decorated functions (`@effect_for`, the registries filled at import): import-time registration has to become an explicit table; 86 `raise` | CI-08 (the driver's imports); the effects' registration is one table either way | **large** |
| **personal combat** | all; `04` and CLAUDE.md §6 make it the first slice | the flat module set and its path insert (H-08); a `dict` outcome (H-06); 59 reflection calls | CI-09 (a package: one import form); `03_PC_typed_outcome_one_door` (B14) | **medium**; the only engine with an export chain the port already validates against (`combat_engine_v1.json`) |
| **mass battle** | the resolver's reached part first: 141 of 339 functions are entered by a fought field (`W4`) | 91 environment reads select behaviour (H-10, carried); 264 comprehensions; the largest files in `modules/` (`hierarchy/units.py` 1,486 code lines, `orchestration.py` 1,119) | the census deletions (B03) and the environment-read removal (B41) come first: porting before them ports dead arms | **large** |
| **the instruments** | **not ported.** The port is validated against pinned readings of the oracle (`proposals/11_GO_port_gate_order_and_coverage.md`, `tools/export_oracle_pins.py`, B41) | — | H-02: the realm builder is in this package today, so "not ported" is false for 982 lines of it until CI-07 lands | none, **after CI-07** |
| **the apparatus** (`tools/`) | not ported; the exporters run in this repository and the port reads their artifacts | — | — | none |

**Order the port would want** (a reading, not a plan: porting beyond the combat slice waits on the port
gate, CLAUDE.md §6): dice engine, small modules, seam, combat, then the data channel with the season core, the
chooser, and mass battle last. Every "lowers" entry above is hash-EQUAL work in the improvement proposal
or a batch the unified order already carries; none shapes Python toward a Godot idiom (`valoria-simplify`
port rule (c)).

## 9. Evidence log

Every command was run from the repository root with `PYTHONHASHSEED=0` where it runs the engine. Probe
scripts and outputs are in the session scratchpad under `runs/HOLISTIC/` (not committed); extracts are in
`master/work/`. This lane wrote only under `master/`. `git status --short` at the end also shows files other
lanes were editing during the run (`architecture/`, `references/id_reservations.yaml`, two ED ledgers);
this lane did not touch them.

| # | command or probe | seed, seasons | outcome |
|---|---|---|---|
| 1 | `python -m engine.season.harness.register --requirements` | — | `met 3 · not_met 1 · partial 5`; 0.6 s |
| 2 | `python tools/m1_acceptance.py --summary` | 20260819 ×1; 24 seeds ×4 | `verdict: NOT MET`, 1 row failing (the nine, 3/9); rows 1, 2, 4 PASS; hash `bbf88d55e218…` twice; 20 s |
| 3 | `runs/HOLISTIC/reach.py realm` (`sys.setprofile`, the season only) | 0, 1 | hash `5ab73af282d0779646c38839fbab85d8`, 13,379 Events; 815 functions called; 45 s |
| 4 | `runs/HOLISTIC/reach_all.py` (profile on before the first import) | 0, 1 | same hash; 1,429 code objects called; 50 s → `W3`, `W4` |
| 5 | `runs/HOLISTIC/reach.py headless` (`headless --case NPC-088 --seasons 2 --seed 0`) | 0, 2 | hash `5405522c36b0399247f83fd9f6d29494`; rounds 5 and 5; 66 of 67 verbs foldable |
| 6 | `runs/HOLISTIC/reach_mon.py 0 3` (`sys.monitoring`) | 0, 3 | hash `52ff67bc45c5b956cd99215f6ba3097f`; combat functions 0, 0, 0; mass battle 18, 18, 152; 55 s |
| 7 | `runs/HOLISTIC/reach_mon.py 2 4` | 2, 4 | hash `b4bae063f33476988db678b5aae62a28` (equal to `audits/25` L-18); combat 155 → 161; mass battle 149 → 153; 120 s |
| 8 | `runs/HOLISTIC/nine_probe.py` | 0, 1 | same hash as 3; ledgers 236 → 12,351 claims; 61 Events with a degree; 749 resolved acts |
| 9 | `python tools/export_sim_params.py --check` | — | `[SIM-PARAMS] current` |
| 10 | `ast` probes: areas and import edges (`W2`), line kinds (`W1`), never-referenced imports (H-09), construct counts (§8), `Fixtures` keywords (`W5`) | — | as tabulated |
| 11 | importing each module entry in a fresh process and listing `sys.modules` | — | three `engine.season` modules, no `yaml`, 0.03 to 0.04 s each (§6 attack 1) |
| 12 | greps quoted in the findings, each run as quoted | — | as stated at the finding |
| 13 | `ast` and regex over the sweep tree, the tests and every importer of `loop/driver.py` (H-09) | — | 26 distinct `S.<name>` reads; 0 of the driver's 79 never-referenced imports obtained through the driver by any file |

**Controls and their limits.** Replay: probes 3, 4 and 8 give one hash at seed 0 for one season; probe 7
reproduces another lane's hash. The reach figures are from two seeds and at most four seasons, so
*"entered by no run"* means these runs, and every such statement is marked unobserved, not dead. The
profile hook of probes 3 and 4 slows the season eightfold and does not change the hash (the same hash
without it, probe 8). No number here is a balance claim.

**What would change a verdict.** H-01: a seed-0 run of six or more seasons entering `modules/combat` would
narrow *"not reached at seed 0"* to *"not reached in the first three seasons"* (it is written that way).
H-04: a setting's name found in `sim_params.json`. H-05: a composition row targeting `roll:obstacle`.
H-09: a file that obtains one of the 79 names through the driver by a route the two searches cannot see.
