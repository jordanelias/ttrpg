# Digest proposalsB6

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane scope: `proposals/2026-10-25-thrust-layer/{probes,reports,toy}` and 17 files of `proposals/2026-10-28-content-architecture-suite/` (02-08, appendices A1-A5, critic_lens3, fragments). The thrust-layer `00/01/02` and content-suite `00/01/01_part2` are digested in `DG_proposals_recent2.md` / `DG_proposals_recent3.md` and not repeated. All figures below are as of the 2026-10-25 / 2026-10-28 engine heads; none re-run by this lane. The probes are the measurement layer beneath `01_MISSING_IN_CODE.md`; they import `engine.season.*` directly (hard-coded `sys.path.insert(0, "/home/user/ttrpg")`) and are not wired to any test or CI (one grep per symbol not made; they are scripts named in the register, run as `PYTHONHASHSEED=0 python3 probes/<file> SEASONS SEED...`).

### proposals/2026-10-25-thrust-layer/probes/p1_s2.txt
- **What it is:** Output of probe P1 (verb funnel, attempted/executed/refused per verb), 5 seeds x 2 seasons on `build_realm`; 2026-10-25; thrust-layer lane (no script file for P1 in this directory).
- **Status:** none (raw output). Reading: historical measurement, live as evidence behind `01_MISSING_IN_CODE.md`.
- **Bears on:** CORE, CHAR, FA, SE, PC.
- **Content that matters:**
  - Pooled 2 seasons: attempted 7402, executed 1763, refused 5639, null 0 (:6); per seed 1448-1511 attempted, 335-374 executed (:1-5). Refused share 76.2%.
  - Never executes (0 of N): examine 256, train 169, carry 157, tend 154, restore 137, sabotage 127, build 122, raze 89, argue 62, march 56, requisition 30, covenant 28, revoke 26, determine 25, pardon 17 (:15-51). Near-zero: migrate 3/714, work 2/333, found 1/105, commit 6/302 (:8,:11,:13,:37).
  - Always executes (0 refused): create_record 404, utter 213, conceal 138, thread_read 10, forgive 5 (:10,:19,:30,:52,:53).
  - Closers table (:55-73): `succeed` is in the verb table but `resolvable=False`, att 0 (:64); `arrest` att 0 though resolvable (:65). Refusal kinds are single-kind per verb (e.g. `work.unavailable` 331, `commitment.refused` 296).
  - Hash per seed printed (:1-5, e.g. seed0 `5301d6b62af614f4`) - a regression anchor for any engine change that moves seed-0 two-season output.
- **Conflicts / stale:** `report` says "929/1,318 refused" was the earlier wrong figure; this file is the corrected 76.2% source. Hashes are not valid after any output-moving engine commit since 2026-10-25 [UNVERIFIED].
- **Open items:** none in file.

### proposals/2026-10-25-thrust-layer/probes/p1_s2_seed0.txt
- **What it is:** P1 output for seed 0 only, 2 seasons.
- **Status:** none (raw output). Reading: historical; duplicate subset of `p1_s2.txt`.
- **Bears on:** CORE.
- **Content that matters:**
  - seed 0: attempted 1511, executed 335, refused 1176, hash `5301d6b62af614f4`, log 21710 (:1-2); identical to the first line of `p1_s2.txt`.
  - In this seed `confer` and `oblige` and `give` are att 0 (:50,:55,:64) while the 5-seed pool has confer 35, oblige 115 - closers are seed-sparse.
  - research 132 attempted / 8 executed, migrate 121 / 0 (:4-5).
- **Conflicts / stale:** redundant with p1_s2.txt (same seed, same hash).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p1_s4.txt
- **What it is:** P1 output, 5 seeds x 4 seasons.
- **Status:** none (raw output). Reading: historical measurement, live as evidence.
- **Bears on:** CORE, CHAR, FA, SE.
- **Content that matters:**
  - Pooled 4 seasons: attempted 16116, executed 3744, refused 12372 (:6) = 76.8% refused; per-seed hashes (:1-5).
  - Closers at 4 seasons (:57-74): determine 3/43, confer 10/111, covenant 0/70, revoke 0/32, commit 8/564, release 63/460, oblige 301/642 (refusal `duty.refused` 341), petition 120/287, issue 73/112, found 1/208, build 0/230, work 3/726, restore 0/250, tend 0/302; `arrest` and `succeed` att 0 (:65-66).
  - `oblige` is the only closer with a large executed count (301) - and its refusals grow from 10 (2 seasons) to 341 (4 seasons) (:63 vs p1_s2 :62), i.e. refused re-attempts accumulate once seats are vacated (cf. p4's `duty.refused` 116-123 after a death).
  - `seize` appears (3 att, 0 exe) only at 4 seasons (:55).
- **Conflicts / stale:** seed 5 appears in `p7_s4.txt` but not here (this file seeds 0-4).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p2_goals_and_need.py
- **What it is:** Probe P2 script: `goals.yaml` rows by object kind/org kind, which goal Propositions `build_realm` mints, and the occasion source of every Scene over a run plus `news.told` counts.
- **Status:** none (script). Reading: historical instrument; reads `engine.season.data.goals`, `decision.make_chooser`, `loop.driver.SeasonDriver`, `queries.world_q`.
- **Bears on:** CHAR, CORE, WR.
- **Content that matters:**
  - Counts goal Propositions minted vs rows (`goal_props_minted=N/38`), `commit` edges to goals, persons with a goal ambition, persons with non-empty `need` referents at t0 (:30-40).
  - Classifies Scenes by `occasion.source` (`need` vs `claim_landed`) and whether a `need` scene's `about` is a goal (:50-56) and resolved acts by occasion source (:57-61).
  - Uses `WQ.ambitions`, `WQ.goal_referents` - the very readers the thrust layer would extend.
  - Hard-coded absolute path `/home/user/ttrpg` (:10); not portable.
- **Conflicts / stale:** none found; symbol names (`WQ.goal_referents`, `d.scenes`) not re-verified against current `engine/season` [UNVERIFIED].
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p2_s2.txt
- **What it is:** Output of P2, 5 seeds x 2 seasons.
- **Status:** none (raw output). Reading: historical measurement.
- **Bears on:** CHAR, WR, FA.
- **Content that matters:**
  - 38 goal rows: kinds `seat_holders` 6, `orientation` 24, `deed_doers` 4, `rung` 4; org kinds faction 20, body 16, seat 2 (:2-3). Only two seat-attached goals (`goal_katepano_press_the_capital`, `goal_kommerkiarios_treaty_order`) (:4).
  - Every seed: 12/38 goal Propositions minted, 55 commit edges, 12 goals with committers, 35 persons with a goal ambition, 46 with non-empty need at t0 (:6,:11,...). Uncommitted non-orientation goals: `goal_altonia_conquer_valoria`, `goal_katepano_press_the_capital` (:7).
  - Scenes ~606-642 per seed; `need` 149-174, `claim_landed` 453-475; `need` about a goal only 43-53 vs 101-121 about something else (:8,:13,...). Resolved acts by source: need 227-272 of ~1107-1182.
  - `news.told` 4-10 vs `news.untold` 17-31 per seed in two seasons; `person.died` 1-4 (:10,:15,...).
  - Persons identical across seeds (83) and counts identical across seeds - the goal seeding is not seed-varying.
- **Conflicts / stale:** the `01_MISSING_IN_CODE.md` claim "need scenes 24-28% of scenes, about a goal only 7.1-8.5%" is derived from these figures (e.g. 149/619 = 24%, 48/619 = 7.8%).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p3_refusal_reasons.py
- **What it is:** Probe P3 script: wraps `SeasonDriver._admits` to log, per act of 23 listed verbs, eligibility, verdict, subject collection kind, first failing Observation.
- **Status:** none (script). Reading: historical instrument; reads `loop/resolve.py` `_eligible`/`_admits` (cited as the single owner of eligibility + requires for both paths).
- **Bears on:** CORE, FA, SE.
- **Content that matters:**
  - CLOSERS list (:20-22) is 23 verbs incl. migrate, research, examine, fight, accept, challenge.
  - `kind_of` (:25-31) checks the seven world collections (persons, rungs, offices, sites, records, propositions, dates) - a closed list hard-coded in the probe.
  - Monkey-patches `d._admits` on the instance (:55) so the run is observed, not moved.
- **Conflicts / stale:** line citation `loop/resolve.py:196` in its docstring may have drifted [UNVERIFIED].
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p3_s2.txt
- **What it is:** Output of P3, seeds 0-2 x 2 seasons: why closers refuse.
- **Status:** none (raw output). Reading: historical measurement.
- **Bears on:** CORE, FA, SE, FI.
- **Content that matters:**
  - Closers refuse at the typed precondition on a subject of the wrong collection: `commit` 177/180 `req:False`, ('persons','ref') 75 + ('rungs','ref') 68 + records 25, only 3 on a Proposition (:21-25); first failing Observation `exists:Proposition value 0` on a Person (:23-25).
  - `found`/`build` fail `exists:works` 0 on persons and rungs (:44-53) - no `works` Record exists to found/build on. `restore` fails `exists:Site` on persons/rungs (:63-67). `research` fails `exists:Record` (:76-80).
  - `work`: all 227 are `req:UNKNOWN`, first Observation `condition` UNKNOWN on persons/rungs (:54-58) - the work precondition cannot read a condition, so it never passes.
  - `confer` 16 `UNKNOWN` of offices, `release` 121 `UNKNOWN`, `revoke` 13 `UNKNOWN` (:9-10,:26-31): UNKNOWN-valued typed requirements refuse like False.
  - `oblige`: 38/38 ok, all on offices (:28-29) - the only closer whose subject kind matches.
  - `migrate`: 463 ok on rungs (:73-75) yet executes 0-13 (p1) - refusal is post-admission (see p3b).
  - Players' own `p_npc_020`/`p_npc_003` recur as the subject-kind-mismatched referent - the subject is the actor's own id.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p3b_kind_mismatch.py
- **What it is:** Probe P3b script: across all verbs, count admissions refused because the subject exists in another collection (wrong kind), split by clause (ineligible / False / UNKNOWN), plus admitted-then-refused acts (refusal at effect or ENCOUNTER).
- **Status:** none (script). Reading: historical instrument; the basis of the "wrong-kind formation" claim and H-156.
- **Bears on:** CORE, CHAR.
- **Content that matters:**
  - Defines mismatch as an `exists:<Kind>` Observation with value 0/False on a subject that exists in a different collection (:49-52).
  - Wraps `d.resolve` to detect admitted acts whose Event is in `VERB_TABLE[verb].emits_on_refusal` (:60-71) - the same refusal definition as `loop/driver.py:489-505`.
  - Counts `admissions` per `_admits` call, not per act (:38), which is why totals exceed attempted acts.
- **Conflicts / stale:** `_admits` called more than once per act would double count (see p3b_s2 where 7737 admissions vs 7402 attempted) [UNVERIFIED cause].
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p3b_s2.txt
- **What it is:** Output of P3b, 5 seeds x 2 seasons.
- **Status:** none (raw output). Reading: historical measurement.
- **Bears on:** CORE, CHAR, FA.
- **Content that matters:**
  - Totals: admissions 7737, admitted 3619, refused UNKNOWN 715, refused False 3403, kind-mismatch 2560 (:6) = 33.1% of admissions, 62% of the refused ones. (Register's "28.7-32.2%" is the per-attempt form.)
  - Mismatch by verb: research 599, commit 289, examine 256, carry 153, restore 136, sabotage 126, build 119, found 104, speak 102, interview 99, petition 91, accept 75, challenge 74 ... (:7).
  - Admitted-then-refused (refusal at effect/ENCOUNTER): migrate 705, transfer 136, move 112, forge 90, surveil 89, raze 84, survey 70, tell 65, train 44, tend 33 (:8) - these refusals are not a formation problem.
- **Conflicts / stale:** the sum (3619 + 715 + 3403 = 7737) matches; `ineligible` count not printed (ref_inelig absent => 0).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p4_killing_consequence.py
- **What it is:** Probe P4 script: for each real `person.died` in computed play, the seats held, claims about the dead, vacancy claims on seats, the killer, and later scene occasions naming dead/killer (H-206, H-209).
- **Status:** none (script). Reading: historical instrument.
- **Bears on:** CORE, CHAR, FA, PC.
- **Content that matters:**
  - Death attributed to the act whose Event the `person.died` Event cites (:47-49); a death with no act is marked `<no act: MATTER/ENCOUNTER>`.
  - Consequence test: later scene occasions whose referents include the killer AND whose `about` is a claim about the dead (:71-72).
  - Reads `claims` from all persons' ledgers (:53) - consequence is a ledger fact only.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p4_s4.txt
- **What it is:** Output of P4, 5 seeds x 4 seasons: each death.
- **Status:** none (raw output). Reading: historical measurement.
- **Bears on:** CORE, CHAR, FA, PC, WR.
- **Content that matters:**
  - TOTAL: 20 deaths, 16 seat-holders, 20 with a killer, 395 claims about the dead, 36 later occasions naming the dead, 1276 seat claims after (:26).
  - Killers by act: `accept` 11, `fight` 9 (count from :1-24); `accept` deaths come from the same actors repeatedly (p_npc_034/013/038/004 appear as killer across seeds).
  - `occasions_naming_killer_about_dead=0` for all 20 (:1-24): no killer ever faces a consequence question.
  - Vacated seats: `tenure.opened` 48-63 claims then `duty.refused` 39-123 and `confer.refused` 8-28 per vacated seat (:2,:5,:10,:16,:18,:19,:21,:22,:23); 12 of 16 seat-holder deaths produce 70-231 seat claims, 4 produce 0 (:11,:12,:24...). No `person.died` claim names the seat.
  - Several deaths have `claims_about_dead=0` (:2,:3,:5,:8-10,:16,:18-19,:21-23) - killing leaves no ledger trace at all about the dead man in 11 of 20.
- **Conflicts / stale:** `01_MISSING_IN_CODE.md` cites these as "0 of 11 `accept` deaths had a challenge from the other party" (P4/P11b); P11b is not in this directory.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p5_exogenous_switches.py
- **What it is:** Probe P5 script: run each "dark" exogenous-motion fixture switch at the sweep value named in its own comment in `data/fixtures.py`, one at a time against control, same seed.
- **Status:** none (script). Reading: historical instrument.
- **Bears on:** CORE, WR, CHAR, SE.
- **Content that matters:**
  - Eight arms (:19-26): body_step=10, age_step=0.01, illness_rate=0.05, age_at_build=160 + age_step=0.01, season_factor_draw=(0.5,1,2)x4, lattice_coupling=250, season_factor_draw=(0.5,)x4. Applied via `w.fixtures.sweep(k, v)` (:36).
  - Reports hash, log len, persons, `person.died`, `body.changed`, site/condition events, vacant offices (:48-50).
  - Catches exceptions and prints RAISED (:51) - a switch that raises is reported, not hidden.
- **Conflicts / stale:** `fixtures.sweep` API and the fixture names [UNVERIFIED against today's `data/fixtures.py`].
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p5_s2.txt
- **What it is:** Output of P5, seed 0, 2 seasons.
- **Status:** none (raw output). Reading: historical measurement.
- **Bears on:** CORE, WR, SE.
- **Content that matters:**
  - Control hash `5301d6b62af6`, log 21710, persons 80, died 3, vacant offices 2 (:1).
  - DEAD switches (hash identical to control): `age_step=0.01`, `age_at_build=160,age_step=0.01`, `season_factor_draw=(0.5,1,2)x4` (:3,:5,:6) - three of seven arms move nothing in two seasons.
  - Live: `body_step=10` (log 21894, body.changed 37); `illness_rate=0.05` (died 4, persons 79, log 21082); `lattice_coupling=250` (hash only, log unchanged); `season_factor_draw=(0.5,)x4` (hash only) (:2,:4,:7,:8).
  - `site/condition_ev` = 644 in every arm including the two that change the hash (:1-8): the site-condition event count is invariant under the season-factor and lattice arms.
- **Conflicts / stale:** `age_step` being inert in two seasons means no aging death path is observed by this run (lifespan beyond 2 seasons not tested).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p6.txt
- **What it is:** Output of P6: lexical classification of the 46 NPC cases' `ends_when`.
- **Status:** none (raw output). Reading: historical measurement; supports "all 46 NPC `ends_when` are prose".
- **Bears on:** CHAR, ARCS, WR.
- **Content that matters:**
  - 46 cases, `ends_when` type `str` for all 46 (:1); never-marked 40, presumed-marked 13, either 40; branch count >=2 for 41, ==1 for 5 (:2-3).
  - STRICT subset: no authored terminus 22 (NPC-007, -009, -011, -013, -033, -034, -036, -037, -039, -040, -041, -071, -072, -073, -074, -080, -083, -084, -085, -088, -089, -090), extractor-presumed only 6 (NPC-002, -005, -006, -010, -035, -086), total 28 of 46 (:51-53).
  - Thinnest: NPC-072 "no goal, arc, or consequence is recorded" (:41); NPC-035 has 6 branches (:35).
- **Conflicts / stale:** the `NONE_S` regex classes NPC-007 and NPC-013 (which name tenure-ending branches) as none, so 22 is an upper bound under its own regex [UNVERIFIED by manual read].
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p6_case_termini.py
- **What it is:** Probe P6 script: classifies `ends_when` of the 46 NPC cases by lexical markers via `harness/run_cases.load_cases("NPC")`; cross-reads `engine/season/ENDINGS_CLASSIFIED.yaml`.
- **Status:** none (script). Reading: historical instrument.
- **Bears on:** CHAR, ARCS, CORE.
- **Content that matters:**
  - Regexes NEVER (:18-19), PRESUMED (:20), NONE_S/PRES_S (:49-52) define "no authored terminus" lexically - not semantics.
  - Reads `/home/user/ttrpg/engine/season/ENDINGS_CLASSIFIED.yaml` (:38); P6 output shows its top level is a `list` (p6.txt:4), so the `list(ec)[:8]` print is not keys.
- **Conflicts / stale:** `ENDINGS_CLASSIFIED.yaml` is described as an "agent's prose classification, its own weakest-evidence label" (:5-6 docstring).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p7_chain_refusals.py
- **What it is:** Probe P7 script: do the committed story instruments (`harness/storybar.py`, `chronicle.deepest_chain`) count refused acts as story? Recomputes cross-person share with refused antecedents removed.
- **Status:** none (script). Reading: historical instrument.
- **Bears on:** CORE, WR, PROCESS.
- **Content that matters:**
  - Uses `SB.drive(seed, seasons, "off", None)` / `SB.read` / `CH.deepest_chain` (:22-34).
  - "refused" = any of an act's Events is of a row's `emits_on_refusal` kind (:32) - the driver's definition.
  - Adds a "refusal null" the storybar lacks: `cross_exec` counts only executed acts with an executed cross antecedent (:39-41).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p7_s4.txt
- **What it is:** Output of P7, seeds 0,1,2,4,5 x 4 seasons.
- **Status:** none (raw output). Reading: historical measurement.
- **Bears on:** WR, CORE, PROCESS.
- **Content that matters:**
  - Deepest causal chains are 11-15 acts and mostly refusals: TOTAL chain 66, chain_ref 55 (:6); e.g. seed 2 chain of 15 has 14 refused (:3).
  - Acts with depth >= 2: 4951, of which refused 3604 (73%) (:6).
  - cross-person share as read 4951/16295 = 30.4%; recomputed executed-on-executed 679/3786 = 17.9% (:6) - the register's G-27 numbers.
  - Seed 5 is included, seed 3 is not (:5; :1-4 are 0,1,2,4).
- **Conflicts / stale:** acts counts here (3256, 3259, 3279, 3217) equal p1_s4's attempted for the same seeds; seed 5 (3284) has no counterpart in P1.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p8.txt
- **What it is:** Output of P8: one season, any threadwork code loaded?
- **Status:** none (raw output). Reading: historical measurement.
- **Bears on:** WR, CORE.
- **Content that matters:**
  - No module with "thread" in its name is loaded (:1); the only verb row containing "thread" is `thread_read` (:2); no thread/lattice/calamity event kinds in a season log (:3); log 7018, hash `b2464a6c87dd` (:4).
- **Conflicts / stale:** `p9` shows `thread_read` executed 1 (2 seasons) and 20 (4 seasons); it is a verb row, not a module.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p8_thread_import.py
- **What it is:** Probe P8 script: one season through `storybar.drive(0, 1, "off", None)`; lists `sys.modules` names containing "thread" and verb rows containing "thread".
- **Status:** none (script). Reading: historical instrument; absence claim was run, not inferred (CLAUDE.md §0.1 pt 3).
- **Bears on:** WR, CORE.
- **Content that matters:**
  - Excludes `threading`, `_thread`, `_threading_local` (:12); also counts event kinds with "thread"/"lattice"/"calamit" (:16).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p9_aperture_s2_seed0.txt
- **What it is:** Output of the "aperture" instrument (P9): per-row, per-holder, per-verb funnel (eligible, formed, offered, attempted, executed, refused) over two worlds, seed 0, 2 seasons: REALM (83 persons, 31 seated) and SPINE (13 persons, all seated).
- **Status:** none (raw output). Reading: historical measurement; the control proves the instrument did not move the season (content hash equal) (:11,:162).
- **Bears on:** CORE, CHAR, FA, SE, SC, PC.
- **Content that matters:**
  - 56 verb rows; 51 resolvable; unresolvable: `construe`, `evade / defy`, `exchange`, `succeed`, `tie / knot` (:3-5). 15 seat-gated rows (`remit:` eligibility alternative) (:7).
  - Realm: 52 unseated persons are eligible for 41 of 56 rows, non-eligible for the 15 seat-gated ones (:82-83); 31 seated holders are eligible for 44-56 (:19-80). Only King/Duke p_npc_020, Confessor p_npc_021, Queen p_npc_032, guild leader p_npc_084 are eligible for all 56 (:33,:35,:41,:79).
  - Per verb, "formed" and "offered" are 83 for nearly all rows, but `arrest`, `comply`, `destroy_record`, `oblige` formed 0 (:88,:93,:100,:117) and `construe`/`evade`/`exchange`/`succeed`/`tie` formed 83 but offered 0 (:96,:104,:106,:131,:137): formation is not the bottleneck; foldability (resolvability) and then refusal are.
  - Realm refused-as: `commitment.refused` 63/63 attempts, `work.unavailable` 72/72, `migrate.refused` 121/121, `train.refused` 42/42, `tend.refused` 42/42, `restore.refused` 21/21, `found.refused` 21/21; `build`/`carry`/`sabotage`/`raze` all 100% refused (:89-141).
  - Questions delivered at barrier 2: `claim_landed` 13074 (83 persons) vs `need` 1283 (55 persons, 31 seated) (:144-145); claims by source: firsthand 6904, told_by 3006, inferred 27, `firsthand_via_knot` 0 (:148-151) - no claim ever arrives through a knot.
  - Aggregation-rule probe: shipped rule `first` gives 0.94 referents/deliberation and 34.7 candidates; `all` would give 6.61 referents and 296.7 candidates (max 2462); `one_per_source` 1.31 / 50.2 (:154-156). Re-aggregation mismatch 0.
  - SPINE: every holder eligible for all 56 rows (:170-195) - the seated-only world is a different access profile from the realm; same refusal pattern (build/carry/commit/found/restore/work all 100% refused, :203-206,:222-224,:240-241).
- **Conflicts / stale:** realm `tell`: `att 25 ex 25 ref 18 both 18` and `march` `att 17 ex 17 ref 17 both 17` (:114,:134) - an act can be both executed and refused (two Events), so executed + refused can exceed attempted; the file says they are never summed (:1).
- **Open items:** `arrest` forms for nobody in either world (:88,:202); `seize` forms for one person (:129,:243).
