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

### proposals/2026-10-25-thrust-layer/reports/R01_partial_top_down.md
- **What it is:** Chat report (2026-10-24/25 session, verbatim) answering whether pure bottom-up emergence is a problem and whether partial top-down guides help, with "oatmeal" research (Compton, Tale-Spin effect).
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3). Reading: historical; figures predate the register and are corrected by `../02_MAJOR_TAKEAWAYS.md` s9.
- **Bears on:** WR, CHAR, CORE, FA.
- **Content that matters:**
  - Verdict: partial top-down in three places only - standing motives held by actors, selection of what the player is shown, a narrow channel of declinable occasions; "every state change stays bottom-up" (:17).
  - Three lawful channels (:34-40): (1) motive inside the actor with a lifecycle (form, advance, obstruct, lapse or fire, succeed) - `goals.yaml` has the right shape (referents, attention only, `goals.yaml:9-12`) but no lifecycle field; (2) selection outside the world (observer/slate reads, writes nothing); (3) occasion channel (predicate hooks per the 2026-08-18 ruling; boot-time authored occasion rows, W8 Rung 2). Control: zero rows must leave the world hash byte-identical (:40).
  - Per-layer state in code (:46-51): ambition question wins ~6% of deliberations and putting it first cut `news.told` 14 -> 7 and events 21,735 -> 15,738; only 2 of 38 goal rows attach to a seat (`goals.yaml:450,468`); cohorts carry no wants (`cohorts.yaml:18-23`).
  - Would narrow ED-IN-0225's wording but keep the refusal of need-triggered outcome injection even with permission to overrule (:42).
  - Falsifier: raise ambition weight; hybrid fails if chain-acts-from-ambition rises while `news.told` collapses (:53).
- **Conflicts / stale:** uses the superseded 929/1,318 and 51/803 figures (:22); "55 of 67 chain acts refused (82%)" uses the over-counting suffix definition (:20-21); `[GAP: primary literature not re-fetched]` (:55).
- **Open items:** human-reader ablation of the recognition layer (CK2 apophenia item) (:53).

### proposals/2026-10-25-thrust-layer/reports/R02_arcs_deconstruction_and_logic_tests.md
- **What it is:** Chat report: logic tests of top-down/bottom-up/hybrid emergence in a self-built toy world, and a deconstruction of the studied arcs.
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3). Reading: historical; toy results are model-internal, low confidence.
- **Bears on:** ARCS, CHAR, WR.
- **Content that matters:**
  - Seven ways arcs are achieved (:20-28): accrual, exposure, succession, decision point (largest: 20/50 arcs close by a decider), contest (9/50 roll), conjunction, held control state (10/50 never close; a state, not an arc). 19/50 are crossing-forced.
  - Hand classification of the 46 character cases by `ends_when` (:34-38): forks 11 (004, 020, 021, 050, 052, 070, 003, 032, 031, 030, 001), exit events only 7, terminus presumed by extractor 12, nothing authored 16 (033, 071, 034, 036, 037, 041, 072-074, 080-082, 084, 085, 089, 090). So 28 of 46 have none or presumed.
  - Arc lane is not mostly arcs: of 50 classified endings 16 (32%) are not multi-season arcs (10 never close, 3 no condition, 3 one roll: ARC-21, 23, 27) (:40). The "~13 shapes" figure rests on 24 of 138 arcs and an evacuated calibration set (:41).
  - Toy table (:48-55): legibility (motive outlasts moment) BU 0.43 / TD 0.36 / TDR 0.23 / HY 0.80; blind-script violated world constraints in 96% of runs; arc rate BU 0.09 (null 0.10), TDR 0.35 (null 0.25). HYd (threshold raises a declinable tribunal, decider rules) lifted arc rate to 0.26 but its shuffled null is 0.26 too (the test credits a lone interior closing event) (:61-62). At 80% refusal HYd's gain vanishes, TDR reaches 0.71.
  - Implication: lawful top-down is arming decider and threshold closure engines, not writing beats (:64).
- **Conflicts / stale:** v1 had four instrument defects fixed in v2; v2 predictions registered after seeing v1 (13/21 scored); A6 had a key-filter bug (:67). The word "Key" in toy code is unrelated to the retired Key substrate.
- **Open items:** whether to accept TDR's injected ordered arcs is left to Jordan (:64).

### proposals/2026-10-25-thrust-layer/reports/R03_sigma_leverage_correlate.md
- **What it is:** Chat report: is there a sigma-leverage correlate for the likelihood of subsequent events; toy results for lookahead leverage versus goal ladders.
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3). Reading: historical; recommendation "do not build lookahead" carried into `02_MAJOR_TAKEAWAYS.md` T5.
- **Bears on:** CHAR, DICE, CORE, WR.
- **Content that matters:**
  - The chooser already has the slot: `engine/season/decision/choose.py::_sample_order` softmax(score/tau), `choice_temperature = 0.1`, noise keyed per candidate (:28); a narrative term would be expressed in tau units, soft-capped like `soft_cap` in `sigma_leverage.py`, kept on the choice stage not the dice, never removing an option (:29-33).
  - Toy table (:37-45): ladder + threshold-raised tribunal 0.38 arc rate, +0.09 over null, closure 0.85; scripted director 0.35 / +0.10; lookahead leverage strength 4 (120 seeds) arc rate 0.09, minus-null -0.08 [-0.14, -0.01]. Last two rows use a different base chooser (:47).
  - Lookahead cost: 126 leveraged decisions per run, ~3,200 rollouts, ~270x run time; 32% of decisions flipped; chain depth 18 -> 31 (partly circular); explained motive 0.58 -> 0.29 (:60-64).
  - Both lawful routes collapse on a mostly-refusing substrate: ladder + tribunal falls to 0.21 at 80% refusal, forced director holds 0.71 (:65). Recommendation: fix the refusal rate before either (:67).
  - Would override v2 narrative-engine rules R-AI and F8 (forecast objects actor-invisible); if adopted F8 becomes a dosimeter (:69).
- **Conflicts / stale:** ladder predictions scored 4 of 7, H1/H4/H7 falsified (:72).
- **Open items:** two-level lookahead, other value proxies and human "construable" judgement untested (:71).

### proposals/2026-10-25-thrust-layer/reports/R04_ladder_tribunal_best.md
- **What it is:** Chat report answering "is ladder + threshold-raised tribunal the best?"
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3). Reading: historical.
- **Bears on:** WR, CHAR, FA.
- **Content that matters:**
  - Answer: No; it leads only on arc rate with no outcome written (0.38, +0.09 [+0.03,+0.15]) and ties the director (:21-23).
  - It loses on motive legibility (0.43 vs 0.80 ambition alone), thread continuity (0.58, lowest of six arms), complete beats (0.43 vs 0.76), 80% refusal robustness (0.21 vs 0.71) (:27-32).
  - Threshold-sensitive: signal holds for thresholds 4.5-10, weakens at 3, gone at 16 (:35). In 192 of 293 runs the main thread closes on a tribunal ruling - one template (:36).
  - Ladder alone multiplies cross-person chain depth ~2.7x (62.5 vs 23.0) and keeps legibility 0.72 (:40).
  - No arm dominates; weighting is a Jordan choice (:42).
- **Conflicts / stale:** ~20 arms compared with no multiple-comparison correction (:38); threshold sensitivity run not saved (:46). The critic later found "2.7x" in no saved output (R13 F14).
- **Open items:** none beyond the trade-off.

### proposals/2026-10-25-thrust-layer/reports/R05_scripted_director_set_pieces.md
- **What it is:** Chat report: a director that injects set pieces (venue, engagement window, decisive form) rather than outcomes.
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3). Reading: historical.
- **Bears on:** WR, PC, SC, MB.
- **Content that matters:**
  - Situation alone fizzles (arc rate 0.07, -0.04 vs null; 94% of runs end with both principals alive); a decisive form (best-of-rounds contest at the venue, lethal at climax, dice and skill pick the loser) gives arc 0.33 (+0.14 [+0.09,+0.20]), complete beats 0.67 (:17-29).
  - Escalating stakes carry much: flat stakes drop complete beats 0.67 -> 0.17; but the director now writes intensity (main-thread peak 7.65 vs 2.36 BU) (:30).
  - Ladder + decisive-form set pieces 0.41 / +0.20 / beats 0.79 (:24). The dictated outcome is traded for dictated form and stakes - "an authored occasion that is not declinable" between lawful occasion and refused scripted beat (:32).
  - The 80% refusal result (0.81) is likely an artifact because the toy contest bypasses the act layer (:35).
- **Conflicts / stale:** R06 immediately corrects the headline (decisive form only matches when the climax is lethal).
- **Open items:** declinable set pieces, mid-run stake adjustment (:38).

### proposals/2026-10-25-thrust-layer/reports/R06_npc_deaths_clarification.md
- **What it is:** Chat report clarifying that "94% end with both principals alive" is toy-world removal, and that the decisive-form arms kill one principal per run.
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3). Reading: historical correction of R05.
- **Bears on:** WR, CHAR.
- **Content that matters:**
  - Decisive-form set piece with lethal climax: 1.00 principal dead per run, +0.14; loser exiled +0.01 [-0.03,+0.07]; settled by pact +0.03; ladder + decisive form lethal +0.20 vs pact +0.03 (:18-25). The ordering signal depends on the death.
  - Ladder + tribunal kills no one and keeps its signal (+0.09) (:29).
  - Mechanism: a lethal climax leaves the thread silent after (0.00 intensity after season 22) and the arc test requires a post-peak fall - partly an artifact of the arc definition (:28).
  - In Valoria the cast is closed and authored (ED-WR-0011) so every death is permanent (:30).
- **Conflicts / stale:** `[CORRECTION]` of R05's headline (:32). Output printed, not saved (:33).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/reports/R07_arcs_without_deaths.md
- **What it is:** Chat report: arcs without NPC death; death rare, fighting authority hard, killing consequential (toy constrained world, 300 seeds/arm).
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3). Reading: historical; source of the "+0.244" toy figure and the real-engine note on `fight`.
- **Bears on:** WR, PC, FA, CHAR.
- **Content that matters:**
  - Among runs that passed the arc test the main thread closed on a death in 99% (forcing director), 94% (lethal set piece), 98% (ladder + lethal), 3% (ladder + tribunal) (:17). 19-36% of harm events hit someone holding a prize (:18).
  - Constrained table (:22-30): ladder + decisive form + bound peace +0.24 [+0.19,+0.30], deaths 0.24/run, beats 0.52; decisive form without ladder +0.02; ladder + tribunal +0.01 ("does not transfer"); bottom-up -0.06 [-0.08,-0.03]; lethal climax with consequences on +0.29, 1.20 deaths. Constraints used: death needs a skill-1 target and 1% roll; harm against a standing-holder refused 90% unless provoked; accusation as usual weapon; peace bound eight seasons (:32).
  - Killing at season 10 in ladder + tribunal world: ~9.5 acts by ~4.9 actors target the killer, ~1.3 tribunals name him, no runaway feud, world ~7 events quieter; avenge ambition added +0.5 acts (:38-43). Not saved.
  - Real-engine note: `fight` requires only existence + co-location; `Felled` deletes the person and emits `person.died`; the "deontological gate" does not exist (`verb_table.yaml`, row `fight`) (:46).
- **Conflicts / stale:** only 3 of 7 pre-registered predictions held (:49); "standing" = holding a prize is the toy's choice (:48); review table and killing runs not saved (:51).
- **Open items:** trial, succession politics for vacated offices, longer feud unbuilt (:44).

### proposals/2026-10-25-thrust-layer/reports/R08_ten_axes.md
- **What it is:** Chat report mapping the user's ten goal axes to `goals.yaml` rows, verb ladders and gaps; defines the arc criterion as self effect + world effect.
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3). Reading: live as a mapping of axes to engine content; cites 38 rows.
- **Bears on:** CHAR, WR, FA, ARCS, FI.
- **Content that matters:**
  - Axes: (1) suppress Einhir Revival, (2) hide threadwork truth, (3) overthrow Church, (4) overthrow caste, (5) purge Altonian influence, (6) maintain/expand authority, (7) standing within faction, (8) benevolent community action, (9) heal the Calamity, (10) revive Einhir heritage (:9-19).
  - Coverage (:34-45): rows exist for 1 and 10 (direct opposition), partial for 3, 5 ("resist" not "purge"), 6 well covered, 8 only Knights/Cardinal of Prudence rows, none for 2 (Varfell's row is the opposite pole), 7 (only 2 of 38 rows attach to a seat), 9. Caste has no store in engine code (canon: informal geographic stigma) and no row defends it; healing has no act (`WR_world.md` T-WR-7, T-WR-11).
  - Arc criterion: self effect = write to actor's own standing/holdings/stance/capability/knowledge; world effect = write to a store the actor does not own (Record, Site, Rung, DocketItem, another's Tenure/stance); checkable statically from `verb_table.yaml` `writes:` (:28-31). At least nine verbs write nothing (examine, interview, research, surveil, thread_read, reconstruct, tell, construe, comply) (:32) - R12 corrects to thirteen.
  - Authority stripping: only the rung above in the same faction can strip a seat (ED-IN-0256 ruling 3); an outsider's route is force (`seize`) (:38).
  - Non-lethal closing acts exist for every axis (determination, exposure, schism, establishment, revocation, conferral, completed work, restoration) (:54).
- **Conflicts / stale:** uses the superseded 929/1,318 figure (:56); whether each listed verb executes was unverified (:61), and P1 later showed most do not.
- **Open items:** map the 46 case files onto the axes (:58).

### proposals/2026-10-25-thrust-layer/reports/R09_design_verdict.md
- **What it is:** Chat report: verdict after the producer/critic relay on the thrust-layer design (v1 -> v2).
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3). Reading: historical summary of `../00_THRUST_LAYER_DESIGN.md`.
- **Bears on:** CORE, CHAR, WR, FA.
- **Content that matters:**
  - Verdict: designable, not buildable yet; every closure route ends through verbs the measured run refused almost every time (:15).
  - Critic opened ~125 citations: 114 held, 9 failed, 2 unverifiable (:17). Four critic findings that changed the design (:31-34): arc test vacuous via witness bookkeeping (`loop/witness.py:654-657`, `state/world.py:1144-1160`); succession piece duplicated ruled IN-61 (`workplans/valoria_master_workplan_v9_part5.md:129-133`); standing gate protects 3 of 31 seats; R3 would repeat the news-starvation regression (all goal commits minted at season 0).
  - Design: current stage read from the person's own ledger (no arc store); ten-axis roster in `rosters.yaml`; stage referents added to the `need` question and promoted to top tier one season per deadline period with staggered phase (:20-21).
  - Axis 9 out of scope until a thread-operation act exists; axes 2 and 4 need authored content; the Church holding axis 2 is an assumption (:38).
- **Conflicts / stale:** `Correction recorded after delivery` (:11): "candidate typing unruled and in no workplan" is wrong; it is H-156 (`engine/season/hole_register.yaml:3615`). References `toy/thrust_layer_design_v2.md` and `..._v1_as_attacked.md` (:43), which are not in this directory (the committed design is `../00_THRUST_LAYER_DESIGN.md`).
- **Open items:** `Slain` edge and D4 (sequence vs arc) for Jordan (:39) - later decided by M20/M21 per `DG_proposals_recent2.md`.

### proposals/2026-10-25-thrust-layer/reports/R10_major_takeaways_as_first_delivered.md
- **What it is:** Chat report: the eight takeaways as first delivered.
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3); points to `../02_MAJOR_TAKEAWAYS.md` as expanded and corrected (:11). Reading: superseded by 02.
- **Bears on:** CORE, WR, CHAR.
- **Content that matters:**
  - Ranking: (1) make existing verbs execute (929/1,318 refused; determine 7/7, confer 4/4, commit 74/74 refused); (2) motive layer partly there (24 of 38 goal rows orientation-only and mint no Proposition); (3) goal ladder + closure form; (4) killing has no consequences (H-209, H-206; gate guards 3 of 31 seats); (5) do not build lookahead / blind script / forcing director; (6) deepest premise least buildable (heal Calamity no act, hide threadwork no row, caste no store, exogenous motion dark); (7) authoring is the largest content job; (8) metrics fail quietly (:15-59).
  - Not answered: whether players find any of it legible; no human readers (:61).
- **Conflicts / stale:** all first-delivery figures (929/1,318; 33%; 51/803; 28/46 as measurement) are superseded in `02` s9 (:11).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/reports/R11_register_verdict.md
- **What it is:** Chat report: verdict on the missing-in-code register after the relay.
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3). Reading: historical; the lead design (G-01) withdrawn.
- **Bears on:** CORE, CHAR, PC.
- **Content that matters:**
  - G-01 (stamp every referent with its collection class) withdrawn: Record sub-kinds (`works`, `dispensation`) are not collections, `DocketItem` is a world read, `determine` has two existence conjuncts of different kinds, stamping would starve untyped rows, and the loader refusal would reject the shipped `comply` row (:17-24). What survives is H-156's three options; choosing is Jordan's (the register's one escalation, :25) - later decided M19(a) per `DG_proposals_recent2.md`.
  - P3b's "33.1%" counted `_admits` calls, not acts; P10 re-takes it per act: 32.2% of attempts at 2 seasons and 28.7% at 4 are refused at admission on a wrong-kind subject (:26). Headline 76.2% / 76.8% holds; 73.8% / 73.9% excluding graded losses (:27).
  - G-16 re-owned to PC-10b: "default for an un-negotiated fight" answered: lethal per PC-10b (:28).
  - `build`/`found`/`work` cannot execute by any typing (ED-IN-0297); `endings_reached` is an existing executable terminus both documents missed (:31-33). `accept` deaths: 0 of 11 had a challenge by the accept's subject (P11b); only 15 challenge events against 11 kills; cutting `accept` depends on PC-10b's H-240 route (:43).
  - Control for any G-01 option must read questions delivered and claims deposited, not executed counts (:45). Degree-aware retry change in G-03 not run (moves the hash by construction). Player seat bypasses `opening_set` (:47).
- **Conflicts / stale:** points to `toy/missing_in_code_v2.md` and probes p10/p11b/p12 (:51-54); in this tree they are `../01_MISSING_IN_CODE.md` and `probes/p10_*`, `p11b_*`, `p12_*` (outside this lane's list).
- **Open items:** whether register + probes go in PR #506 or a new PR (:56).

### proposals/2026-10-25-thrust-layer/reports/R12_design_producer_receipt.md
- **What it is:** Producer (opus) hand-back for design v1 plus the verbatim brief it was given.
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3). Reading: historical; kept as terminal verdict about an existing artifact.
- **Bears on:** CORE, CHAR, WR, FA, PC.
- **Content that matters:**
  - Corrects the brief: thirteen verbs write nothing, not nine (add `dispatch`, `challenge`, `evade / defy`, `speak`) (:16); `construe` is `grade: absent` with `requires_typed: none` so cannot serve as non-violent weapon (:17); `offices.yaml` has 31 seats: 16 no revoker, 13 strippable by rung above in same faction, 2 by rung above in holdings (:18).
  - Orientation-only goal rows mint no Proposition so produce no thrust: Crown resist-Altonia, both Einhir-revival rows, caste-ended, community rows (:19). Standing gate can build on `admits_audience` / `guard_weight` (`world_q.py:1250-1344`) but binds nobody because guards are off by default (:20). `succeed`, `tie`, `knot` have no code opening their tenures (`rosters.yaml:141-143`) so hereditary seats cannot be filled (:21).
  - Silent consequence channels: death never reaches questions (H-209), empty seat named by no claim (H-206) (:22). `_standing_crossings` (`loop/matter.py:187-240`) is the precedent for a threshold that writes nothing (:24).
  - Brief (verbatim :71-112) gives the evidence base: `goals.yaml` 38 rows, chooser `_sample_order` Plackett-Luce via Gumbel at `data/fixtures.py:286`, `ENDINGS_CLASSIFIED.yaml` (DECIDER 20, ROLL 9, THRESHOLD 8, NEVER 10, UNCLEAR 3), 143 cases (46 characters, 97 arcs) (:90-93).
  - Cheapest sinking test: executed `determine`/`confer`/`covenant`/`open_case` over seeds (:63).
- **Conflicts / stale:** brief states "9 verbs write nothing" - corrected here. The brief cites the retired-Key `09_ambitions_and_arcs.md` proposals as reference-only (:92).
- **Open items:** D1 (beaten fighter killed), D2 (who holds axis 2 / defends caste), D3 (caste store) - D2 later answered from canon by R13 F13.

### proposals/2026-10-25-thrust-layer/reports/R13_design_critic_report.md
- **What it is:** Read-only critic's report on design v1 (findings F1-F16, ~125 citations opened: 114 held, 9 failed, 2 unverifiable).
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3). Reading: historical terminal verdict; dispositions live in `../00_THRUST_LAYER_DESIGN.md`.
- **Bears on:** CORE, CHAR, FA, WR, PC.
- **Content that matters:**
  - F1 BLOCKER: ARC predicate vacuous - every witnessed act yields a `claim.deposited` Receipt whose subject is the claim id (`loop/witness.py:654-657`; `state/world.py:1144-1160`), and any self-write (`move` writes `Person.travel_leg`) meets clause (2) (:18). F2 BLOCKER: succession carrier rejected by ruling IN-61 (`valoria_master_workplan_v9_part5.md:131`, `04_CODE_ARCHITECTURE.md:195`) (:19). F3: standing gate seats only 3 principals (`cohorts.yaml:127-130`); −1 `seat_holders` goals target unguarded Church seats (`goals.yaml:161-163`) (:20).
  - F4: R3 reintroduces news starvation because goal commits are minted at `since` 0 (`harness/populated.py:709`) so stages come due together (:21). F5: `harness/arms.py:135-170` is wired to `field_casualty_model`, so it cannot produce the named measurements (:22). F6: `of: referent` cannot be spelled - operands closed, builder `SystemExit` not `Unspecified` (`data/requires.py:973-978`) (:23).
  - F10: `held_document_declines` (`rosters.yaml:2020-2033`; `decision/options.py:857-874`) maps verb -> document kind and cannot key on a covenant's referent (:27). F11: contraventions understated (ED-IN-0225, R3 deadline as a timer no act declared, `Slain` vs 2026-09-04 "accept the result") (:28). F9: "pure read over a finished world" false - the question lives on the driver's `Scene` (`state/carriers.py:574-584`) (:26).
  - Holds: 13 verbs write nothing; 31 seats (revocation 16 null / 13 / 2; conferral 6 null / 8 elected / 17 appointed); 22 of 29 loop-built seats keep `dispatch` (`data/rosters.py:709-717`); ED-IN-0225 cited in four `.py` files (chronicle, populated, soak, storybar) (:57-62).
  - Observations: no path for a player character; a detained holder with a due stage forms acts the custody decline refuses (`verb_table.yaml:913`) (:36-37).
- **Conflicts / stale:** many `path:line` cites will have drifted [UNVERIFIED]. F14 notes the "~2.7x" and "~9.5 acts by ~5 actors" toy figures appear in no cited output (:31).
- **Open items:** none beyond the dispositions (in 00).

### proposals/2026-10-25-thrust-layer/reports/R14_register_producer_receipt.md
- **What it is:** Register producer's hand-back (29 entries, probes P1-P9) with the verbatim brief.
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3). Reading: historical; superseded by `../01_MISSING_IN_CODE.md` v2.
- **Bears on:** CORE, CHAR, FA, PC, WR, FI.
- **Content that matters:**
  - Grades (:18-24): PRESENT-BROKEN 9 (G-01-06, G-14, G-15, G-27), ABSENT-RUN 5, ABSENT-READ 7, PRESENT-INERT 4, PRESENT-USED narrowed 4.
  - P5: `body_step`, `illness_rate`, `season_factor_draw`, `lattice_coupling` change the world when set; `age_at_build` does nothing on a built world because `Person.born` fixed at construction (`state/carriers.py:687`) (:36).
  - G-02: contested act refused before its contest never reaches `SeasonDriver.resolved` (`loop/resolve.py:1039-1045` vs `:377-379`); aperture reads `accept` as 4 attempted/4 executed when it was 48 attempted/44 refused (:45). G-27: cross-person share 30.4% -> 17.9% executed-only (:47).
  - G-16: non-lethal duel exists unwired - RS-25 rules it in, PC-10a built it in `modules/combat/wrapper.py`, the season never passes it terms (:48). G-15: PC-10b's planned refusal of `accept` with no challenge would remove most measured deaths (:49). Rename `ladders` -> `goal_stages` because `ladders` already names two other things (:50).
  - Brief corrections: `REFUSAL_KINDS` is at `data/verbs.py:1403`, not `:1073` (:59).
  - Wrote the narration proposal's open S12 as "answered from precedent: IN-53 declines wrong-kind `confer` formations" (:65) - R15 A1 shows that was wrong.
- **Conflicts / stale:** "28 of 46 by a text rule written after reading the strings" is non-independent (:37).
- **Open items:** why `arrest` is never formed (R15 A14a answers: it forms only on a held warrant, `verb_table.yaml:179`); whether `survey` mints a `works` record (R15 A9: already answered in tree).

### proposals/2026-10-25-thrust-layer/reports/R15_register_critic_report.md
- **What it is:** Read-only critic's report on the register v1 (A1-A14, O1; ~46 citations opened: 34 held, 12 failed) plus verbatim brief.
- **Status:** "REFERENCE - HELD BACK IN FULL" (:3). Reading: historical terminal verdict; dispositions in `../01_MISSING_IN_CODE.md` s7.
- **Bears on:** CORE, CHAR, FA, SE, PC.
- **Content that matters:**
  - A1 BLOCKER: G-01 passed over open RULING H-156 (`hole_register.yaml:3615`, "survives all five ... THE ROW STAYS OPEN"; `withheld_verbs` at `:3619`); `decision/options.py:94-100` says a filter on world truth would be `choose` reading the world (:19). A2 BLOCKER: the class rule is unsound (works/petition/dispensation are Record sub-kinds; DocketItem is a world-state read; `determine` has two existence conjuncts; `examine` conjunct is `of: site`; stamping collides with source-qualified classes and would undo IN-45, IN-49, IN-09) (:20).
  - A3: 7,737 counts calls of `_admits`, not acts: a contested or graded act calls it twice (`resolve.py:1039`, `:428`); per act 2,560/7,402 = 34.6% (:21). A6: "refused" has at least four readers (`witness.py:245-256`; `person_q.py:364-368`; `data/verbs.py:1406`); 44 of seed 0's 1,176 refusals are "both" (:24). A8: G-02 is already a recorded instrument limit (`requirements.yaml:993-996`, R-05) (:26). A9: `build`/`found` cannot execute because a computed `create_record` mints `text` (`effects_information.py:82-84`; H-165; ED-IN-0297) (:27). A10: `world_q.endings_reached` (`world_q.py:1990-2024`; `driver.py:520-523`) missed (:28).
  - A5: refusals carry the world's motion - seat claims are mostly `duty.refused`/`confer.refused` and `claim_landed` is 13,074 of 14,357 questions (:23). A4: `commit` executes in baseline (IN-11: 8 times in the realm; `hole_register.yaml:3622`) (:22).
  - A14: `act.ineligible` and the fallback `act.refused` count as EXECUTED under the driver rule (`resolve.py:88`, `:229`) (:32); P6's strict regex embeds verbatim fragments and omits NPC-081/082/087 (:32).
  - NEEDS-RUN list (:35-44) of six measurements; O1: player seat bypasses `opening_set` via `harness/play_surface.py:8-29` (:33).
  - What holds: P1's capture is valid (driver calls `self.resolve`/`self.encounter` `driver.py:473,:480`); hashes agree across P1/P3b/P4/P5; P4 counts hold; `arms.py:153-165` hard-codes `field_casualty_model`; `guards=False` default (`populated.py:725`) (:54-59).
- **Conflicts / stale:** the "8 times" and similar counts are as of 2026-10-25 [UNVERIFIED now].
- **Open items:** the six NEEDS-RUN items; P10 (not in this lane) is the re-measurement.

### proposals/2026-10-25-thrust-layer/reports/README.md
- **What it is:** Index of the 15 reports and reproduction notes.
- **Status:** "REFERENCE - PROPOSED, HELD BACK IN FULL" (:3). Reading: live as an index.
- **Bears on:** PROCESS, WR.
- **Content that matters:**
  - R01-R11 are the assistant's chat answers verbatim; R12-R15 are subagent hand-backs with briefs (:39-40). Only path rewrites were applied (:46).
  - R12-R15 kept as terminal verdicts about existing artifacts per CLAUDE.md s0's exception; "Delete them if the exception becomes the general case" (:7-9).
  - Known errors (:54-56): R09/R10 say candidate typing "unruled and in no workplan" (it is H-156); first-delivery refusal figures (929 of 1,318; 33%; 51 of 803; 28 of 46) superseded.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/README.md
- **What it is:** Module map and grade statement for the toy-world evidence directory (24 actors, 6 places, 6 prizes, 24 seasons; stdlib only, fixed seeds).
- **Status:** "Grade: model-internal, low confidence. Reference under CLAUDE.md s0.05. Not game code, not read by any tool, creates no obligation." (:3-4). Reading: reference, correctly bannered; nothing in it runs `engine/season/` except the five chronicle files.
- **Bears on:** WR, CHAR, PROCESS.
- **Content that matters:**
  - Module table (:11-22): `regimes.py` = `regimes_v1.py` (v1 world, byte-identical, hash in `v1_files.sha`); `regimes2.py` v2 instrument (pair-thread identity, plateau peak, burn-in, director thread); `regimes3.py` terminal-lifecycle and tribunal arms; `lookahead.py`; `regimes5.py` goal ladders HYg1-3; `regimes6.py` situation set pieces (TDS, TDSm, HYg3s); `regimes7.py` decisive-form set pieces (TDSc, TDScf, HYg3c); `regimes8.py` non-lethal/settled climaxes (run inline, not saved); `regimes9.py` standing snapshots (inline, not saved); `regimes10.py` constrained world.
  - Pre-registration audit (:25): checked 2026-10-28, prediction/experiment scripts match their recorded hashes (13 of 17 entries) but the world file recorded beside them does NOT in four freezes (`regimes.py` in `predictions.sha`, `regimes2.py` in `v2_frozen.sha`, `regimes5.py` in `ladder_pred.sha`, `regimes10.py` in `con_pred.sha`): the freezes cover predictions, not the world.
  - v1 predictions were blind; every later set is informed; HYc, HYd, bootstrap CIs, sifting test, lookahead, ladder, set-piece and constrained arms are post hoc (:25-28).
  - "Printed, not saved" list (:37-39): `regimes9.py` review of earlier arcs; `regimes8.py` non-lethal/settlement runs; threshold-sensitivity and per-property tables; killing cascade tables except `save_figs_out.txt`.
  - Five real-engine chronicles (seeds 0,1,2,4,5, 4 seasons) show 53 of 66 chain acts refused by the suffix definition of `narration-mechanisms.md` (:41-44).
- **Conflicts / stale:** R01 cites 55 of 67 and R02/R10 cite 66 of 81 for the same chains; README says 53 of 66. Three different numerators for one measurement (suffix definition over-counts degree bands). P7 (`probes/p7_s4.txt`) counts 55 of 66 on the driver definition.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_closure.py
- **What it is:** Post-hoc script: does a threshold-forced, decider-closed moment (HYd) produce arcs? 300 seeds; base and 80% refusal; bootstrap CIs; tribunal count; single-closing-spike sifting.
- **Status:** none (script, "POST-HOC, exploratory", :1). Reading: historical.
- **Bears on:** WR, FA, CHAR.
- **Content that matters:**
  - Imports `regimes3 as R`; regimes BU, TDR, HY, HYd (:10-11). `boot()` is a naive percentile bootstrap (:6-9).
  - Last block counts `summon`/`rule` events to report tribunals raised and ruled per run (:22-25), but it reads `e['thread']` on every event and crashes (see output).
- **Conflicts / stale:** script crashes with `KeyError: 'thread'` at :24 (visible in `exp_closure_out.txt`).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_closure_out.txt
- **What it is:** Output of `exp_closure.py` (base and 80% refusal) plus the tribunal counts and spike test from a patched re-run.
- **Status:** none. Reading: historical measurement, partly inconsistent (see below).
- **Bears on:** WR, FA, CHAR.
- **Content that matters:**
  - Base: HYd arc_all 0.260 vs its own null 0.258; HYd - BU +0.173 [+0.113,+0.233]; `HYd arc_all - arc_null: 0.002` (:3-13) - the headline gain over BU is entirely matched by the shuffled null.
  - 80% refusal: HYd - BU +0.027 [-0.037,+0.090], CI spans 0; TDR 0.710 vs null 0.330 (:14-26).
  - After the traceback (:27-34) the file continues with a different run's lines: "HYd: tribunals raised per run 31.59, ruled (all three accepted) per run 11.11" (:35) and a single-closing-spike test: spike at season 4 -> arc False, seasons 8-20 -> arc True (:36-40). The arc test therefore passes a lone interior closing event at any season >= 8 (the R02 caveat).
- **Conflicts / stale:** the file is a splice of two runs (the committed script still crashes at :24); tribunals/run (31.6 raised, 11.1 ruled) shows HYd is a high-volume tribunal arm, not a rare closure.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_con.py
- **What it is:** Constrained-world experiment: NPC death rare, violence against standing gated, accusation as usual weapon, bound peace, killing consequences; nine arms; seven pre-registered predictions K1-K7.
- **Status:** none (script; predictions "registered BEFORE the first run", hash in `con_pred.sha`). Reading: historical.
- **Bears on:** WR, PC, FA, CHAR.
- **Content that matters:**
  - CON1 = `death_p=0.01, gate_p=0.9, accuse=True, truce=True, conseq=True, lethal=False`; CON2 lethal + `tdr_kill` (:5-6). Metrics added: deaths, harm on standing, gate refusals, accusations, revenge events (reaction to a death id), outcry, late events (t>=22) (:18-26).
  - `ladder_rate` computes share of ambitions with at least one `goal_met` (:29-38).
  - Imports `regimes10 as R` - the code in the file whose hash does not match its freeze (README :25).
- **Conflicts / stale:** none beyond the README caveat.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_con_out.txt
- **What it is:** Output of `exp_con.py`: nine arms, 300 seeds.
- **Status:** none. Reading: historical; source of the "+0.244" figure.
- **Bears on:** WR, PC, FA.
- **Content that matters:**
  - HYg3c nonlethal (ladder + decisive form + bound peace): deaths 0.24, harm on standing 0.127, arc 0.470, arc-minus-null +0.244 [+0.188,+0.303] (:7). Its sibling TDSc nonlethal (set piece without ladder): +0.016 [-0.019,+0.051] (:6). BU: -0.056 [-0.083,-0.027] (:2). HYg3d (ladder+tribunal): +0.010 [-0.046,+0.067] (:4). TDR forced yield: +0.099 (:5).
  - Lethal + consequences arms: HYg3c 1.20 deaths, revenge 3.68/run, +0.291 (:9); TDSc lethal+conseq 1.35 deaths, +0.044 (:8).
  - Ladder survives the gate: 0.957 of ambitions meet a goal (:12).
  - Predictions: 3/7 confirmed (:14-22). FALSIFIED: K1 (deaths <= 0.6 and harm on standing <= 0.10 -- ladder arms have 0.12-0.13), K2 (BU has an ordering signal: -0.056, below chance), K3 (bound peace gives >= +0.08 for TDSc nonlethal: it gives +0.016), K5 (revenge >= 3.0 lethal arms: TDSc lethal+conseq 2.87 fails; nonlethal revenge 0.53-0.68, above 0.5).
- **Conflicts / stale:** R13 F14 says `+0.244` is quoted without its sibling arm's +0.016 - this file shows both. The ordering signal in the ladder + peace arm depends on the ladder, not the peace alone.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_contest.py
- **What it is:** Conclusive-form set-piece experiment (best-of contest at a venue, decisive, lethal at climax); ten predictions C1-C10; uses `regimes7`.
- **Status:** none (script; predictions frozen, `setpiece2_pred.sha`). Reading: historical.
- **Bears on:** WR, PC, SC.
- **Content that matters:**
  - Arms BU, TDR, TDSc (set piece), TDScf (flat stakes), HYg3c, HYg3d (:16); also computes P(protagonist wins climax) (:22-29) and violations after killing the protagonist at season 10 (:31-35).
  - C-predictions encode: winner stays open (0.25-0.75), signal >= +0.05, close to forcing director, complete beats >= 0.50, 80% refusal still >= 0.50, quiet world stakes >= 2x BU.
- **Conflicts / stale:** the 80% refusal arm uses `refuse=0.8` on the toy's own act layer; the toy contest has its own dice and bypasses it (R05 :35), so C6's pass is partly an artifact.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_contest_out.txt
- **What it is:** Output of `exp_contest.py`.
- **Status:** none. Reading: historical.
- **Bears on:** WR, PC, SC.
- **Content that matters:**
  - TDSc arc 0.330, +0.142 [+0.090,+0.197], closed 0.793, five_node 0.673, why_linked 0.268; HYg3c +0.199, five_node 0.787, why_linked 0.446 (:5-7).
  - 80% refusal: TDSc +0.561, HYg3c +0.627, HYg3d -0.023 (:23-26) - the toy contest does not pass through the act layer.
  - P(protagonist wins climax) = 0.64 / 0.647 (:29). Quiet-world peak magnitude: BU 2.36, TDSc 7.65, TDScf 4.27 (:28).
  - 9/10 confirmed; C10 FALSIFIED (HYg3c why_linked 0.446 < 0.55) (:42-43).
- **Conflicts / stale:** R05's table lists HYg3c "+0.20 [+0.14,+0.26]" and "ladder + decisive-form 0.41"; matches :7.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_ladder.py
- **What it is:** Hierarchical-ambition experiment: ladders of depth 1-3 (HYg1-3) under an ambition, versus BU/TDR/HY/HYd; seven predictions H1-H7.
- **Status:** none (script; "written BEFORE this script was first run", `ladder_pred.sha`, :2). Reading: historical.
- **Bears on:** CHAR, WR.
- **Content that matters:**
  - Regimes BU, TDR, HY, HYd, HYg1, HYg2, HYg3 at base and `refuse=0.8` (:23-26). Contrast list includes HYg3 vs HY, HYg3 vs HYd, TDR vs HYg3 (:43).
  - Contains a dead conditional (`if False else`) in the `d` lambda (:35) - a leftover.
  - Imports `regimes5` (hash mismatch with `ladder_pred.sha` per README).
- **Conflicts / stale:** none further.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_ladder_out.txt
- **What it is:** Output of `exp_ladder.py`.
- **Status:** none. Reading: historical.
- **Bears on:** CHAR, WR.
- **Content that matters:**
  - Base: HYg3 arc_all 0.143 vs null 0.140 (arc-null +0.003); HYg3 - HY +0.087 [+0.043,+0.137]; HYg3 - BU +0.057 [+0.007,+0.107]; why_linked 0.721 (:9-18). HYd arc 0.260/null 0.258 (:6).
  - At 80% refusal HYg3 - BU +0.000 [-0.063,+0.063], TDR - HYg3 +0.520 (:28,:33).
  - Predictions 4/7: FALSIFIED H1 (ladder >= +0.10 over HY), H4 (HYg3 arc-null >= +0.05), H7 (five_node +0.15); CONFIRMED H2 (depth dose), H3, H5, H6 (:38-46).
  - HYg1's arc_null is 0.179, higher than any other arm's (:7, :18 -0.089) - an unexplained outlier in the null.
- **Conflicts / stale:** R03 says "two tiers give about the same as three, one tier does nothing" - HYg1-HY +0.033 spans 0 (:17), HYg2-HY +0.097 (:16), consistent.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_setpiece.py
- **What it is:** Situation-only set-piece director (TDS: relocate principals + engagement window; TDSm: stakes multiplier) versus BU, TDR, HYg3d, HYg3s; nine predictions S1-S9.
- **Status:** none (script; predictions frozen in `setpiece_pred.sha`). Reading: historical.
- **Bears on:** WR, SC.
- **Content that matters:**
  - Computes outcome openness by who is dead at the end (protagonist only / antagonist only / both alive) for TDR, TDS, TDSm (:22-30), violations after killing the protagonist (:31-36), quiet-world peak magnitude (:21,:50).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_setpiece_out.txt
- **What it is:** Output of `exp_setpiece.py`.
- **Status:** none. Reading: historical.
- **Bears on:** WR.
- **Content that matters:**
  - TDS (situation only) arc 0.070, arc-null -0.042 [-0.073,-0.009]; TDSm -0.069 [-0.090,-0.049]; HYg3s -0.020; HYg3d +0.092 [+0.033,+0.152] (this is the "ladder + tribunal" arm's +0.09) (:5-8).
  - Outcome openness: TDR (0,1,0) - the forcing director always kills the antagonist; TDS and TDSm 94% both alive (:30).
  - 5/9 predictions confirmed; FALSIFIED S1 (outcomes stay open), S2, S6, S8 (:34-44). Quiet-world peak magnitude TDSm 14.52 vs BU 2.36 (:28).
- **Conflicts / stale:** the "94% both alive" in R05/R06 is :30.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/lb_more.py
- **What it is:** 120-seed lookahead-leverage run (lambda 0 vs 4) with bootstrap differences; multiprocessing Pool(4).
- **Status:** none (script). Reading: historical.
- **Bears on:** CHAR, DICE, CORE.
- **Content that matters:**
  - Compares arc_all, arc_null, arc_closed, dangling, five_node, why_linked, depth, n_exec; reports changed/leveraged, leveraged decisions per run, rollouts per run (:17-26).
  - Uses `lookahead.simulate_lb` on the `regimes3` world.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/lb_more_out.txt
- **What it is:** Output of `lb_more.py`.
- **Status:** none. Reading: historical; source of R03's lookahead numbers.
- **Bears on:** CHAR, DICE.
- **Content that matters:**
  - lam 4 vs lam 0: arc_all 0.092 vs 0.017 (+0.075); arc_null 0.167 vs 0.022 (+0.144 - null rises more); arc_closed 0.492 vs 0.150; why_linked 0.579 -> 0.287; chain depth 18.0 -> 30.6 (:2-8).
  - `lam4 arc_all - arc_null = -0.075 [-0.144,-0.008]` (:10); changed/leveraged 0.324; 126 leveraged decisions and 3,179 rollouts per run; zero injected outcomes, zero violations (:11).
  - R03 states "explained motive 0.58 -> 0.29" - this file has why_linked 0.579 -> 0.287.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/lb_sweep.py
- **What it is:** 40-seed lambda sweep (0, 1, 2, 4) of lookahead leverage; Pool(3).
- **Status:** none (script). Reading: historical.
- **Bears on:** CHAR, DICE.
- **Content that matters:**
  - Prints per-lambda means of 11 metrics, injected total, changed/leveraged, rollouts/run (:16-23).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/lb_sweep_out.txt
- **What it is:** Output of `lb_sweep.py`.
- **Status:** none. Reading: historical.
- **Bears on:** CHAR, DICE.
- **Content that matters:**
  - Dose: changed/leveraged 0.077 (lam 1), 0.154 (2), 0.287 (4); rollouts/run ~3,000; why_linked 0.610 -> 0.333; depth 16.2 -> 26.6; arc_all 0.100 vs arc_null 0.158 at lam 4 (:2-5). Zero violations and zero injections at every lambda.
- **Conflicts / stale:** 40 seeds only (the 120-seed run supersedes it).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/lookahead.py
- **What it is:** Toy-world choice-level "narrative leverage" with M=4 rollouts of H=2 seasons, standardised per actor and soft-capped, applied only to actors in the top-3 threads.
- **Status:** none (script; module docstring is the design). Reading: historical; the only code in the directory that models the proposed sigma-leverage correlate.
- **Bears on:** CHAR, DICE, CORE.
- **Content that matters:**
  - Mirrors `choose.py::_sample_order` (Plackett-Luce/Gumbel, tau; here `TAU = 0.15`, `M_MAX = 1.5`, :17-18) and adds `lam * soft_cap(z)` where z standardises the lookahead value across the actor's candidates (:98-100) - the mu-shift-in-sigma-units idea of `sigma_leverage.py`. The real engine's tau is 0.1, so the toy's tau differs.
  - Proxy Q = mean of cross-person involvement, thread concentration and escalation (:140-146), "deliberately not the evaluation metrics" (:8-9).
  - `clone()` copies the world per rollout (:26-36) - the cost driver (~3,000 rollouts per run).
  - Casting rule: only actors in the current top-3 threads are leveraged (:107-119, :96).
- **Conflicts / stale:** the lookahead value V is an in-sim local proxy that correlates with the arc metric's ingredients (cross-person depth) - R03 notes partial circularity.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/metrics2.py
- **What it is:** Fragment of the v2 metrics module (selection, arc test, violations, graph stats, five-node, `run_metrics`, `log_hash`); has no imports header and uses `Counter`, `math`, `hashlib`, `json`, `T_DEF` unimported - it is spliced into `regimes2.py` (not independently runnable).
- **Status:** none (code fragment). Reading: historical duplicate of the metrics section of `regimes2.py`.
- **Bears on:** WR, PROCESS.
- **Content that matters:**
  - `arc_test` (:46-65): thread intensity per season, 3-wide smoothed plateau peak at 0.2n..0.92n, rise = Spearman >= 0.5 before peak, fall = post-peak mean <= 0.6 x peak AND a closing event at/after the peak. A single closing event at the peak season satisfies it.
  - `shuffled` null shuffles event times (:68-70). `five_node` needs >= 4 beats, a turn, and a closing beat at/after peak (:109-121).
  - Variants grid VARIANTS (peak_hi, strict_close, burn) (:134-135); `arc_all` = `p92_relax_b4`.
  - `why_linked` = motive is an `ambition` or a `reaction` to a selected event (:146-149). `violations` counts dead_actor, dead_target, not_colocated, bad_cause (:73-87).
  - `select` keeps top-3 threads capped at 12 beats - the "chronicle" selection (:5-14).
- **Conflicts / stale:** `arc_any3` is assigned twice (:203-209) with a dead `if False` generator - leftover.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/out_v1.txt
- **What it is:** Saved output of the v1 suite (blind predictions), N=300, T=24.
- **Status:** none. Reading: historical; v1 instrument had defects fixed in v2.
- **Bears on:** WR.
- **Content that matters:**
  - 11/21 predictions confirmed (:110). Blind-falsified: A1 (TD >= BU + 0.20; TD 0.143 vs BU 0.080), A3, D1, D2, B1, B2, E1, R1, K3 (:81-108).
  - v1 TD violated constraints 99.7% of unperturbed runs (:74); post-kill violation rate TD 1.0, others 0 (:78).
  - Control K1: 300/300 identical (HY with weight 0 equals BU) (:97).
- **Conflicts / stale:** superseded by `out_v2.txt`.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/out_v2.txt
- **What it is:** Saved output of the v2 suite.
- **Status:** none. Reading: historical; the base table behind R02.
- **Bears on:** WR, CHAR.
- **Content that matters:**
  - Regime table: why_linked BU 0.428 / TD 0.357 / TDR 0.229 / HY 0.801 (:5-8); arc_all/null BU 0.087/0.102, TD 0.160/0.168, TDR 0.350/0.254, HY 0.057/0.081 (:19-22); five_node 0.110/0.337/0.760/0.113 (:40-43).
  - Dose: raising ambition weight w from 0 to 1 raises why_linked 0.423 -> 0.992 but lowers arc_all 0.093 -> 0.033 and arc_closed 0.36 -> 0.173 (:59-63).
  - Ablation: removing the lifecycle raises HY arc_closed 0.233 -> 0.387 (:67): the lifecycle hurt closure.
  - 80% refusal: TDR 0.71 vs null 0.33 (:74).
  - 13/21 confirmed (:124); FALSIFIED A5 (hybrid has no signal over null: HY-null -0.024), R1, K2, K3.
- **Conflicts / stale:** `out_v2.txt` K2 shows the "more ambition weight lowers arc rate" result that R02 reports (0.09 -> 0.03).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/posthoc.py
- **What it is:** Post-hoc script on v2: HYc arm, bootstrap CIs, director-template signature counts, and "sifting availability" (does any top-6 thread and any window >= 8 seasons satisfy the arc test).
- **Status:** none (script, "POST-HOC (exploratory, run after v2)", :1). Reading: historical.
- **Bears on:** WR, PROCESS.
- **Content that matters:**
  - `available(ex)` searches threads and windows for any arc-test pass (:28-36); the shuffled null is computed the same way (:38-43).
  - Counts distinct forced-beat signatures for TD and TDR (:21-27).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/posthoc_out.txt
- **What it is:** Output of `posthoc.py`.
- **Status:** none. Reading: historical.
- **Bears on:** WR, PROCESS.
- **Content that matters:**
  - Sifting: real vs shuffled-null availability BU 0.887 vs 0.960, TD 0.943 vs 0.980, TDR 0.993 vs 0.993, HY 0.860 vs 0.947 (:28-33) - an arc-shaped window exists in almost every run and every shuffle; arc-shape is nearly always findable by sifting.
  - Director templating: TD forced-beat signatures structural distinct = 1, slot distinct = 298 of 300; TDR structural 4 (:25-26) - the "oatmeal" evidence: different proper nouns, one structure.
  - HYc (fired ambitions simply end) vs HY: arc +0.020 [-0.020,+0.063], CI spans 0 (:13).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/predictions.py
- **What it is:** v1 blind pre-registered predictions (21 items: L1-3, C1-4, A1-3, D1-2, B1-3, K1-3, R1, N1, E1) as decorator-registered check functions.
- **Status:** none (script; "PRE-REGISTERED ... sha256 saved to predictions.sha first", :1-2). Reading: historical; byte-identical to `predictions_v1.py`.
- **Bears on:** WR, PROCESS.
- **Content that matters:**
  - Condition vocabulary: base, noent (no entrenchment), engine (`refuse=0.8`, "the real engine refuses ~70-80% of acts"), small, null (quiet world), pert (kill leader at t=10) (:3-6).
  - `from regimes import spearman` in K2 (:127).
- **Conflicts / stale:** the 70-80% refusal figure anchoring the `engine` condition is the pre-register figure (76.2% measured later).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/predictions_v1.py
- **What it is:** Byte-identical copy of `predictions.py` (`cmp` equal).
- **Status:** none. Reading: duplicate, historical.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Same content as `predictions.py` (verified by `cmp`); both named in the sha ledger (README :13).
- **Conflicts / stale:** duplicate file.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/predictions_v2.py
- **What it is:** v2 predictions, registered after v1 results and before the v2 run (informed, not blind).
- **Status:** none (script, :1-3). Reading: historical.
- **Bears on:** WR, PROCESS.
- **Content that matters:**
  - Replaces v1 L2/A1/A2/A3/A6/B1 with director-thread measures (arc_dir, dir_is_main, grounded_forced) and a four-variant sensitivity prediction A6 (:40-67); `from regimes2 import spearman` (:86).
  - E1 now reads "the TD-BU gap in arc rate widens under 80% refusal" (:109-112).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/real_engine_chronicles/chronicle_seed0.txt
- **What it is:** Saved `engine.season.harness.chronicle` output for seed 0, 4 seasons: deepest cross-person chain, 14 acts.
- **Status:** none. Reading: historical measurement of the real engine at 2026-10-25.
- **Bears on:** CORE, WR, CHAR.
- **Content that matters:**
  - acts=3256 (matches p1_s4 seed 0); 14 chain links, 11 of which emitted refusal kinds (commitment.refused, restore.refused, travel.blocked, march.refused, kill.refused, transfer.refused, raze.refused, challenge.refused, tend.refused) and only `dispatch` x2 (order.given) and `reconstruct` (finding.made) executed (:1-15).
  - Chain participants are a handful of recurring names (Sigrid Torsvald, Torben Almqvist, Elske Almqvist, Wilhelm Voss, Gerik Strand) - the same actors in every seed.
- **Conflicts / stale:** `PYTHONHASHSEED=None` in the header (:1): not run with a fixed hash seed.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/real_engine_chronicles/chronicle_seed1.txt
- **What it is:** Chronicle, seed 1, 11 links.
- **Status:** none. Reading: historical.
- **Bears on:** CORE, WR.
- **Content that matters:**
  - acts=3259; 11 links: 10 refusal-kind (transfer, march, build x2, argue, move, survey, transfer ...) plus one executed (`forge` record.forged) and a `finding.none` (examine) (:1-12). Two characters (Joren Bergvall, Annika Feldhaus) alternate for most of the chain.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/real_engine_chronicles/chronicle_seed2.txt
- **What it is:** Chronicle, seed 2, 15 links.
- **Status:** none. Reading: historical.
- **Bears on:** CORE, WR.
- **Content that matters:**
  - acts=3279; 15 links, only `reconstruct` (finding.made) executed; all others are refusals (accept.refused x3, restore.refused, work.unavailable x2, kill.refused, covenant.refused, release.refused x2, travel.blocked, commitment.refused) (:1-16).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/real_engine_chronicles/chronicle_seed4.txt
- **What it is:** Chronicle, seed 4, 12 links.
- **Status:** none. Reading: historical.
- **Bears on:** CORE, WR.
- **Content that matters:**
  - acts=3217; 12 links; executed: `dispatch` order.given x2, `issue` dispensation.issued x2; the rest refusals (kill.refused opens the chain, work.unavailable x3, accept.refused, news.untold, pardon.refused) (:1-13).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/real_engine_chronicles/chronicle_seed5.txt
- **What it is:** Chronicle, seed 5, 14 links (seed 5 is not in the P1 5-seed set).
- **Status:** none. Reading: historical.
- **Bears on:** CORE, WR.
- **Content that matters:**
  - acts=3284; 14 links; executed: `reconstruct`, `tell` (news.told); refusals the rest (commitment.refused x4, challenge.refused x2, kill.refused, found.refused, release.refused, march.refused, travel.blocked x2, news.untold) (:1-15).
- **Conflicts / stale:** README says seed 3 "was shown in the session and not saved" (README :41-42).
- **Open items:** none.
