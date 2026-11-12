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

(Reading note for the nine `regimes*.py` files below: `regimes.py` and `regimes_v1.py` were compared with `cmp` (byte-identical) and `regimes.py` was read whole; each later file was read as a full `diff` against its predecessor in the chain `regimes -> 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10`, which shows every added or changed line and is equivalent to a full read of a cumulative file. Each entry states only what that file adds. All are toy-world code with no `engine/` import; none is read by any tool or test.)

### proposals/2026-10-25-thrust-layer/toy/regimes.py
- **What it is:** The v1 toy world and metrics: 24 actors, 6 places, 6 prizes, 24 seasons; regimes BU (bottom-up), TD (blind script), TDR (replanning director), HY (hybrid: referent-bound ambitions with lifecycle and an occasion channel).
- **Status:** none (module docstring :1-15). Reading: historical; freeze `predictions.sha` records a different hash for this file than it has now (README :25).
- **Bears on:** WR, CHAR, PROCESS.
- **Content that matters:**
  - Separate RNG streams (world/acts/ambition/director) so HY with weight 0 and occasions off reproduces BU's log exactly - the control (`log_hash`, :598-599; K1 = 300/300).
  - Act model: 1d6 + skill vs difficulty; `refuse` probability turns any non-forced act into a refused roll of -99 (:116-118) - the toy's "engine refusal rate".
  - Drive priority `choose` (:162-213): reaction (0.6), standing ambition (coin w), local opportunity (0.4), hostility (0.5), affinity (0.3), wander. Forced director beats carry `forced=True`; `injected` counts forced events with delta > 0 (:534).
  - Ambition assignment is a "tension graph": each prize gets two factions' claimants; others oppose or protect (:220-235); lifecycle fires on holding for two seasons, then successor by predicate (the lowest-opinion rival) (:237-257).
  - Metrics are log-only: arc_test is peak/rise/fall + closing event; null is a time-shuffle (:437-457); `why_linked` counts ambition or in-selection reaction motives (:524-532).
- **Conflicts / stale:** v1 thread identity used `ref` (D-pair or prize) which split a conflict across two references; fixed in `regimes2.py`.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes10.py
- **What it is:** The final world in the chain: constrained world (rare death, standing gate, accusation, truce/bound peace, killing consequences, `inject_killing`). Read as a diff against `regimes9.py` (152 diff lines).
- **Status:** none. Reading: historical; its hash does NOT match the freeze in `con_pred.sha` (README :25).
- **Bears on:** WR, PC, FA, SC, CHAR.
- **Content that matters:**
  - New world state: `gate_p`, `accuse_on`, `truce_on`, `conseq`, `rep` (repute), `truce`, `gate_refused`, `avenge`, `tdr_kill`.
  - Gate (in `do`): a non-forced harm against a target with more standing (more prizes held) than the actor is refused with probability `gate_p` unless provoked (a harm by that target within 2 seasons); a pair under truce cannot act on each other (:144-154 of the diff region). Refusals are logged as zero-delta events, not dropped.
  - `attack()` routes violence against a higher-standing target to an `accuse` act 70% of the time; `accuse` is a contest of standing that raises the target's repute (`rep`) on success and the accuser's on failure (new verb branch).
  - `on_death()` (consequences): kin/faction/friends of the victim lose opinion of the killer by 0.8 and get a revenge window; witnesses at the killer's place by 0.4; killer repute +2 and forfeits holdings; an `outcry` event is logged; optional `avenge` makes the 2 closest kin adopt an `oppose` ambition against the killer.
  - Stage predicates read repute: a `weaken`/`defeat` stage can be satisfied by the target's repute >= 1.0 / 2.0 when accusation is on - so accusation substitutes for violence in ladder progress.
  - Non-lethal TDR climax yields: holdings pass to the director's favourite and a truce is bound for 8 seasons (`truce[...] = t + 8`).
  - `simulate(..., con=, killing_t=)` takes a constraint dict (`death_p`, `gate_p`, `accuse`, `truce`, `conseq`, `avenge`, `tdr_kill`, `lethal`).
- **Conflicts / stale:** none beyond the freeze mismatch.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes2.py
- **What it is:** v2 instrument. Read as a diff against `regimes.py` (259 diff lines).
- **Status:** none. Reading: historical; hash not equal to `v2_frozen.sha`.
- **Bears on:** WR, PROCESS.
- **Content that matters:**
  - Thread identity: every act gets a `thread` (pair `T{a}-{b}` or prize `P{k}`), replacing `ref`-based identity; `executed()` and `select()` key on `thread`.
  - arc_test: peak is the centre of the smoothed maximum plateau; peak window up to 0.92n; closing allowed AT the peak season (`strict_close` variant); burn-in of 4 seasons; four variants (`p92_relax_b4`, `p92_relax_b0`, `p85_strict_b4`, `p85_strict_b0`) with a null each.
  - `endow()`: the director writes initial state (declared as a forced zero-delta event) so its beats are not asserted on a world that contradicts them; `HYc` regime = fired ambitions simply end (terminal).
  - New director metrics: `arc_dir`, `dir_is_main`, `dir_mass_rank`, `grounded_forced`, `director_writes`, `forced_in_sel`.
- **Conflicts / stale:** the strict-close variant changes TD/TDR conclusions at 80% refusal (see `results_v2.json`).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes3.py
- **What it is:** Adds the threshold-raised tribunal (HYd). Read as a diff against `regimes2.py` (54 diff lines).
- **Status:** none. Reading: historical.
- **Bears on:** WR, FA, SC.
- **Content that matters:**
  - `tribunals(t, theta=6.0)`: when a pair thread's cumulative executed intensity crosses theta, a `summon` is logged; the decider is the highest-skill other living actor; all three must accept (each with probability 0.7 -> 0.343 joint); on acceptance the decider favours the party with the better opinion of them, holdings of the loser pass, opinions reset, and a `rule` event with closing=True and delta 5.0 is logged. The crossing itself writes no outcome - only an accepted tribunal does. A pair re-summons no sooner than 6 seasons.
  - `THETA = 6.0` is a module constant (the later threshold sweep 3, 4.5-10, 16 was run inline, not saved).
- **Conflicts / stale:** the declinable tribunal fires 31.6 times per run (exp_closure_out :35), so it is a routine template, not a rare closure.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes5.py
- **What it is:** Adds goal ladders (HYg1/2/3, HYg3d). Read as a diff against `regimes3.py` (134 diff lines).
- **Status:** none. Reading: historical.
- **Bears on:** CHAR, WR.
- **Content that matters:**
  - `build_ladder(kind, ref)`: claim ambition = [reach(place), ally] + [weaken(holder)] + hold(prize), depth-dependent; oppose = [reach_p, weaken_p] + defeat; protect = [befriend]. `stage_done` predicates read live state (place, opinions, skill below base, holder dead, 3 harms delivered, opinion >= 0.7).
  - `ladder_act`: each season advance as many already-met stages as possible (guard 6), log `goal_met`; a stage unmet for `deadline` = 6 seasons logs `goal_failed` and advances anyway; after the last stage `ambition_fired` and a successor claim on the best unheld prize, capped at 2 cycles (`cap`).
  - Ladders replace the lifecycle (`life = False`); HYg3d adds the tribunal.
  - Ladder stages are typed per referent kind (place / person / prize), not per axis; no stage names an institutional object.
- **Conflicts / stale:** stage failure by deadline advances the ladder regardless of outcome (so ladders always "complete"; K7's 0.957 means at least one goal met, not that the ambition succeeded).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes6.py
- **What it is:** Adds situation-only set pieces (TDS, TDSm, HYg3s) and the `LAST` world handle. Read as a diff against `regimes5.py` (99 diff lines).
- **Status:** none. Reading: historical.
- **Bears on:** WR, SC, PC.
- **Content that matters:**
  - `setpiece(t, i, mult_on)` relocates the director's principals to one venue (logged as a zero-delta forced `relocate`) and opens an engagement window (1 season; 2 at the climax beat) in which they may only engage each other; `engage_act` picks aid / claim / harm from opinion and holdings. `mult_on` multiplies delta by the beat intensity inside the window (`TDSm`).
  - `s.eng`, `engaged_flag` and `sp_mode` are new state; `global LAST` lets experiments read the last world.
- **Conflicts / stale:** the window forces the principals' choices (they "may only engage each other") - so a set piece is not declinable.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes7.py
- **What it is:** Adds the decisive-form contest set pieces (TDSc, TDScf, HYg3c). Read as a diff against `regimes6.py` (81 diff lines).
- **Status:** none. Reading: historical.
- **Bears on:** WR, PC, SC.
- **Content that matters:**
  - `contest_form(t, i)`: best-of-rounds (first to 2 wins, max 5) with 1d6 + skill each round; tie broken by skill; winner takes the loser's prizes; loser skill -1; opinion -0.3; at the climax beat (i == 4) the loser dies (`lethal`). The contest is one Event with delta = stakes (`BEAT_I[i]`, or flat 3 for TDScf), `closing` if died or holdings moved.
  - The contest has its own dice and does not pass through `do()` so it ignores `refuse` - the artifact R05 flags.
- **Conflicts / stale:** the toy dice are 1d6 + skill; Valoria's resolution is dice pools with `d+sigma` - no structural resemblance.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes8.py
- **What it is:** Adds non-lethal and settled climaxes (TDScn, HYg3cn, TDSc_s2, HYg3c_s2). Read as a diff against `regimes7.py` (60 diff lines).
- **Status:** none. Reading: historical; its runs were printed, not saved.
- **Bears on:** WR, PC, SC.
- **Content that matters:**
  - `lethal` and `settle` flags: non-lethal loser is exiled (sent to another place, holdings stripped, alive); `settle` (suffix `_s2`) passes holdings, sets mutual opinion 0.3 and clears grudges - "closed by pact, both stay in play". Regime names are parsed by suffix (`endswith('n')`, `endswith('_s2')`) - a string-sniffing dispatch.
- **Conflicts / stale:** results referenced in R06 only; no saved output.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes9.py
- **What it is:** Adds standing snapshots on events (`astand`, `tstand`) - the number of prizes held by actor and target at the time of the act. Read as a diff against `regimes8.py` (7 diff lines).
- **Status:** none. Reading: historical.
- **Bears on:** WR.
- **Content that matters:**
  - `snap` now carries `astand`/`tstand`; used by R07's review of earlier arcs ("19-36% of harm events hit someone holding a prize") and by the gate in `regimes10.py`.
- **Conflicts / stale:** the R07 review table was printed, not saved.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes_v1.py
- **What it is:** Byte-identical copy of `regimes.py` (`cmp` equal), named by `v1_files.sha`.
- **Status:** none. Reading: duplicate, historical.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Same content as `regimes.py` (verified by `cmp`); `v1_files.sha` pins hash `20e5ff98...` for it.
- **Conflicts / stale:** duplicate file.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/results_v1.json
- **What it is:** Raw aggregate output of the v1 suite (`results.json` renamed): conditions base/noent/engine/small/null, perturbation, dose, ablation, control; regimes BU/TD/TDR/HY.
- **Status:** none. Reading: historical data behind `out_v1.txt`.
- **Bears on:** WR.
- **Content that matters:**
  - Base HY: why_linked 0.455, arc_all 0.20, arc_null 0.267 (:102-134); BU arc_all 0.08 vs null 0.157 (:3-35).
  - Engine (80% refusal) condition: n_exec drops to ~41.6 (BU) - 56.7 (HY) from ~240-270 (:295,:394), TD viol_any 0.987 (:314).
  - Dose key "1.0": why_linked 0.976, arc_all 0.15, dangling 0.813 (:831-863).
  - Control `ctl`: equal 300 of 300 (:966-969).
- **Conflicts / stale:** the v1 instrument's defects; superseded by `results_v2.json`.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/results_v2.json
- **What it is:** Raw aggregate output of the v2 suite, with the four arc-criterion variants and nulls per condition.
- **Status:** none. Reading: historical data behind `out_v2.txt`; the only place the sensitivity grid per condition is saved.
- **Bears on:** WR.
- **Content that matters:**
  - At 80% refusal, TDR arc_all (p92_relax_b4) = 0.71 vs its null 0.33 (:480-483), but the strict variant `p85_strict_b4` gives TDR 0.087 vs null 0.192 and TD 0.037 vs 0.161 (:434-441,:484-485): the forcing director's "robustness under refusal" (R03/R04/R05's 0.71 vs the ladder's 0.21) is an artifact of the lenient arc criterion (peak up to 0.92n and closing allowed at the peak).
  - Same condition: TD/TDR arc_peak 1.0, arc_fall 0.98-0.99, arc_closed 1.0, dangling 0 (:443-447,:489-493) - every forced run ends with a closing event; `n_exec` ~46 per run (:457,:504).
  - Base: TDR five_node 0.76 vs BU 0.11 (:128 vs :36) - the director's beat structure is real under the toy's metric.
  - Dose HY w=0 -> 1: arc_p92 0.093 -> 0.033; arc_closed 0.36 -> 0.173; why_linked 0.423 -> 0.992 (:958-1188).
- **Conflicts / stale:** no document reports the strict-variant result for TD/TDR at 80% refusal; R02-R05 quote only `arc_p92_relax_b4`.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/save_figs.py
- **What it is:** Script re-running and saving two figures that design v1 had cited from the terminal: cross-person chain depth (constrained and unconstrained) and the killing-at-season-10 cascade.
- **Status:** none (script). Reading: historical; closes the "printed, not saved" gap for these two figures.
- **Bears on:** WR, PROCESS.
- **Content that matters:**
  - Computes `depth` for BU/HYg3/HYg3d/HYg3c under CON (`death_p=0.01, gate_p=0.9, accuse, truce, conseq`) and for BU/HYg3 unconstrained (:5-13).
  - Cascade: `simulate(s,'HYg3d',con=CON,killing_t=10)`; counts later `harm`/`accuse`/`claim` acts against the killer, distinct actors, and `rule` events naming the killer (:17-24).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/save_figs_out.txt
- **What it is:** Output of `save_figs.py`.
- **Status:** none. Reading: historical measurement; resolves R13 F14's "figure in no cited output" for these numbers.
- **Bears on:** WR.
- **Content that matters:**
  - Chain depth constrained: BU 25.8, HYg3 85.6, HYg3d 90.1, HYg3c 86.7 (:2-5); unconstrained BU 23.0 vs HYg3 62.5 (the "62.5 vs 23.0", 2.7x) (:7-9).
  - Killing at season 10 (HYg3d, n=300): acts against killer 9.54, distinct actors 4.86, tribunals naming killer 1.31 (:10).
- **Conflicts / stale:** the HYg3d world (ladder + tribunal) is the one used for the killing cascade; R07 reports these as "ladder-plus-tribunal world".
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/suite.py
- **What it is:** v1 aggregate runner: conditions base/noent/engine/small/null; perturbation; dose; ablation; control; prints and checks `predictions.py`; writes `results.json`.
- **Status:** none (script). Reading: historical; byte-identical to `suite_v1.py`.
- **Bears on:** PROCESS, WR.
- **Content that matters:**
  - Condition dict (:9-15): base `{}`, noent `entrench=0`, engine `refuse=0.8`, small `A=12,P=10,PR=4`, null `A=8,P=8,PR=3`.
  - Writes `results.json` to the cwd (:78); the committed file is `results_v1.json` (renamed). Imports `regimes as R` and `predictions as PR`.
- **Conflicts / stale:** the script writes a filename that does not exist in the directory; duplicate of `suite_v1.py`.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/suite2.py
- **What it is:** v2 aggregate runner (imports `regimes2`, `predictions_v2`); same structure as `suite.py`, nan-safe mean, writes `results_v2.json`, extra "ARC variants" and "DIRECTOR THREAD" report blocks.
- **Status:** none (script). Reading: historical.
- **Bears on:** PROCESS, WR.
- **Content that matters:**
  - Perturbation uses `R.main_thread` on events at/after the kill (:59-61); control compares `log_hash` BU vs HY with weight 0 (:72-76).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/suite_v1.py
- **What it is:** Byte-identical copy of `suite.py` (`cmp` equal).
- **Status:** none. Reading: duplicate, historical.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Same content as `suite.py` (verified by `cmp`); pinned in `v1_files.sha`.
- **Conflicts / stale:** duplicate file.
- **Open items:** none.

## Part 2 - proposals/2026-10-28-content-architecture-suite/ (17 files)

Common to every file in this suite: all carry "PROPOSED (2026-10-28 session; reconstructed 2026-10-30) - HELD BACK IN FULL. Reference under CLAUDE.md s0.05: not a mechanism; merging ratifies nothing", lane IN. They are a reconstruction from a transcript of an uncommitted session; every figure and `path:line` is as of repo head `be24c71` (2026-10-28) and unre-verified; the "Provenance" paragraph of each lists which patch scripts were replayed. Ruling labels (M3, J-T2, J-T5, M16, M20(b), ruling 10/11/12, L-1, L-3) refer to the suite's own list in `01_MAIN_REPORT_part2.md` (digested in `DG_proposals_recent3.md`). The recommended package is P1-B + P2-A (amended) + P3-B reached through P3-A.

### proposals/2026-10-28-content-architecture-suite/02_P1_templates.md
- **What it is:** Part 02, P1 "Templates": three packages (A dossiers only; B dossiers + story pools drawn at world build; C authored set pieces + per-season docket decks), plus the shared dossier/order/provider/troop/kit/variety designs; lane IN, 2026-10-28.
- **Status:** "PROPOSED ... HELD BACK IN FULL" (:3). Reading: historical/reference; recommendation is B (:15, :170).
- **Bears on:** CHAR, FA, SE, WR, ARCS, MB, GO, CORE.
- **Content that matters:**
  - Authoring-layer rule (:31): a field is true at the start, has one author, and no act has touched it; anything that counts/compares or could be made wrong by a season-1 act is a query; starting values are compiled into the owning record at build and the dossier is not read again. The dossier becomes the head: `npc_registry.yaml`, person fields of `npcs.yaml` and holder column of `offices.yaml` move into `engine/season/dossiers/` behind an exporter `--check`, pending a Layer-1 check against `04` row 27a.
  - Pool card (P1-B, :119): fields id, family, `source:` (an arc quote), eligible (build query), attach (seat or place), roles (queries to seats), role-bound goal rows, one seed claim in one ledger, `opens_with` (an existing verb). Nothing on the card may be a date, deadline, firing condition or outcome (B10-18:183's list kept whole). Nothing drawn in a season; no clock emits an event; keeping pool size P >= k^2 keeps expected overlap between two worlds under one (:143).
  - B+ (not recommended): cards read inside an act with staged `exposure` Records would need B10-18:183/:193, B10-19:95 amended, the T-c default (ED-IN-0301) reopened, and `research`'s `writes: []` given writes (:130). C amends T-c, AX-5's fourth motion, ED-IN-0225 (whole-arc scripting Jordan excluded), ED-WR-0011, B10-19 (:150-154).
  - Management orders (:57-59): which verbs are orders is decided only by a `management:` column on the verb row; candidates `confer`, `revoke`, `establish`, `dispatch`, `issue`, `requisition`, `transfer`, `seize`, `covenant`; what a seat can order depends on `remit_acts` not rank (Confessor rung 1 holds `confer`/`revoke`). "Free of the scene budget" would change the number ruled 2026-09-02 (`decision/budget.py:19-20`) and should live in the budget owner (`Scene.cost`, `deliberate.py:252-258`).
  - Troop stock M3 option A (:64-68): stored commander, type (10 rows of `TROOP_TYPE_STATS`), count, kit kind (`TROOP_LOADOUT`), home rung; grade/discipline/morale/upkeep are queries; Layer 1 refuses a stored discipline on a Rung (`holonic_ARCHITECTURE.md:384`). **Amends ratified `04:801` ("units = PersonId[] ... NO unit class") and `:810`; needs Jordan's yes.** Kit: weapons from `modules/combat/weapons.py` (54 keys) physics; no fixed weapon triangle (:70-73).
  - Variety instrument (NEW `harness/variety.py`, reuse `storybar.chains`): per world sign every cross-person chain of depth >= 3 by (verb sequence, actor role classes, subject kind); report mean pairwise Jaccard and the stock share (signatures in >= half the worlds); controls same seed twice reads 1.0 and `draw_seed_arm` gives the floor (:75-77).
  - TS gap in every form (:83): "TS is written by none" (`harness/loops.py:96`); fix = one TS writer on the character's own `research` of a Thread-significant Record at RESOLVE on the `train` precedent; Klapp's starting TS is `null`, a [GAP] (`npc_registry.yaml:1032`). "Exposure" = a query counting claims in an Inquisitor's own ledger about Klapp (:84).
  - Cell counts (:106-110, :143, :165): A ~690 person cells + 50 faction + 222 settlement + 16 set pieces x 5; B adds 16 set pieces x 8 and 12 pools x 6 = 72 cards; C 48 local persons x 15, 36 set pieces, 102 cards. Arcs reachable of 55: A ~25, B ~36 (foreign off, the confirmed default) or ~40 (on), C ~46 (:24).
- **Conflicts / stale:** line 23 keeps a residue `04:801/:802` where other cites read `:810`. Cites `proposals/2026-10-22-system-description/ctl/realm_seed0_2seasons.txt` for "327 of 1,132 attempted acts produced a non-refusal" (:145), versus P1's 335 executed / 1,511 attempted for the same seed (different definition). `harness/loops.py:96`, `deliberate.py:252-258`, `verb_table.yaml:963` [UNVERIFIED now].
- **Open items:** M3 (troop count amends Layer 1), the B10-19 clause for role-bound scenarios, B4.1 owner, whether the item kind needs Layer-1 sign-off (04 B.7 `hold` objects) (:132, :139).

### proposals/2026-10-28-content-architecture-suite/03_P2_attributes_skills_histories.md
- **What it is:** Part 03, P2 "Attributes, skills, histories": P2-A (plan's nine attributes, TS named the tenth), P2-B (demand-derived eight), P2-C (six as ceilings), with shared verb rule, 14 skill keys, four-stage lifepath, worked sheets for Klapp and the Lord Steward.
- **Status:** "PROPOSED ... HELD BACK IN FULL" (:3). Reading: historical/reference; recommends P2-A amended with B's Perception/Insight split held until fieldwork verbs are built (:15, :231-235).
- **Bears on:** CHAR, DICE, PC, FI, SC, WR.
- **Content that matters:**
  - Verb rule (:37-41): a verb row never names an attribute; a contested row (declares `contests:`) maps `verb_capability: verb -> key` and `key_base: key -> {act, resist}`; `resist` defaults to `act` (ED-IN-0185 Q2 "their corresponding score/2"); module verbs (`fight`, `accept`, `march`) map in the module adapter; 45 of 56 rows read no person quantity (`verb_table.yaml:33-35`: eligibility never gates on capability). CR-20's "LANDED ALREADY: `faculty`" is false at HEAD (:41).
  - Faculty formula (A): `attr[base] + min(3, max(0, key - pool_default)) + practice`, replacing CR-20's `max` (under which training is invisible in anyone talented) (:101). Falsifier: attribute 6 with key 5 rolls 9; a planted `max` makes it 6 (:119).
  - 14 skill keys, only `copying` exists (`rosters.yaml:1232-1233`) (:43); "aptitude" retired -> skill key / base / cap (:49). Lifepath rows in `rosters.yaml: lifepath_templates`: origin 8, formation 7, vocation 34 (extends CR-33), catalyst 7+1 (:53-58).
  - A6's 104-moment demand matrix "primary in" counts: STR 10, END 11, AGI 15 (+7 stealth), FOC 1, ACU 21, WIL 9, ATT 27, CHA 17, BON 7, TS 11 (:88-99). A6 contradicts itself on combat `reading` (matrix codes notice/PER, module map INS); on the 11 built / 21 built-and-module moments ACU dominates every set at 55% - ATT's 29% exists only in the 83 lexicon draws (:159-161). A ten-score variant "B-10" (split ATT, fold FOC into WIL, keep BON, count TS) has min 7 uses and max share 22% and overrides nothing (:162).
  - Override costs (:137-141): P2-B would override ED-IN-0185 Q7 (Jordan verbatim "it will be 10 attributes", entry marked "THE AGENDA IS CLOSED; DO NOT RE-RAISE IT"; registry says "THE COUNT IS RULED", `descriptor_registry.yaml:27`) and ED-IN-0301's nine-key default; P2-C overrides ED-IN-0185, J-13 (iii), Jordan's view 3, and re-roots combat's ladder (floor `max(1, attr-1)`, ceiling `2*attr`, unauthored score reads 3, :178-183).
  - Cell counts: A 956, B 910, C 818 instance cells for 46 cast (:31, :113, :149, :191). Family G arcs (12: 2 9 26 28 29 30 32 35 39 41 51 54) need TS on persons with readers, the TS writer, a pooled `thread_read` (CP-T07-02) (:115).
  - March: Command is derived from CHA and COG clamped 1-7 (`core/exchange.py:55-64`) and does not enter the pool under the pool-quality model (:80).
- **Conflicts / stale:** the nine-vs-ten attribute count conflicts with `descriptor_registry.yaml` as the suite quotes it ("COUNT IS RULED"). Result of the patch replay could not be checked against a later full read (:8). `Person.thread_sensitivity` at `carriers.py:717` [UNVERIFIED now].
- **Open items:** J-T2 (is TS the tenth), M2 amendment (additive excess instead of `max`), M3, J-T5 (who owns a sword); `resolution-diagnostic` run for 12-die top pools (:117).

### proposals/2026-10-28-content-architecture-suite/04_P3_player_surface.md
- **What it is:** Part 04, P3 "The player surface": P3-A ledger and menu (text client), P3-B management console plus minigame scenes, P3-C map-centred client; subsystem cards; combat-window and army/loadout surfaces.
- **Status:** "PROPOSED ... HELD BACK IN FULL" (:3). Reading: historical/reference; recommends P3-B reached through P3-A (:15, :85).
- **Bears on:** GO, CORE, PC, MB, SC, FI, SE, FA, CHAR.
- **Content that matters:**
  - One working seam, `dispatching_chooser` (`harness/play_surface.py:41`); re-run for Klapp and the Lord Steward over two seasons the world was identical to the plain run (`content_hash` `5301d6b6...` both ways) (:15). Parity = the human picks from exactly the NPC chooser's options for that person (:13).
  - Measured (:31-32): a rung 1-2 seat is eligible for 45 of 56 rows (41 every person has + 4 seat rows `issue`, `covenant`, `requisition`, `seize`); 40 of the 45 resolve; neither Klapp nor the Steward can `confer`/`revoke`/`dispatch`, so a management menu holds four orders. The Confessor's remit holds `issue`, `determine`, `confer`, `revoke`, `convene` (`offices.yaml:364-369`); `dispatch` survives on loop-built seats via `remit_unruled` (`offices.yaml:141`). Klapp's first question is a `need` about NPC-003 with stated budget 6 and 28 options; by season 2 budget 9 (each held tenure adds 1, `budget.py:55-61`) but at most 5 scenes released a season (`loop/deliberate.py:85-113`, H-92) - the surplus is unspendable and should not be displayed as spendable. The Steward in season 2 picks `fight` on the King (risk-free-fight defect CP-T03-00).
  - Combat seam (:33): trace returns 16 event kinds (`seam/wrappers/combat.py:244-252`; `wrapper.py` `_emit`); none names a technique firing (9 abilities act as continuous modifiers); in the season every fighter is a default `Combatant` (arming sword, light armour, no tradition) (`queries/inputs.py:107-121`).
  - Odds policy: (i) facts only for combat (Jordan: "we wouldn't really forecast"; L-1 limits v10 `part14:282`); (ii) believed-word reopens only if AQ-X1 ruled (b) (AM-B-03 withdrew it, `workplans/valoria_master_workplan_v10_part13.md:244-248`) = ruling 11; (iii) true band on request; Proceedings shows none (`21_RECONCILIATION.md:617`, ED-SC-0039) (:21-24, :76-79).
  - Subsystem cards (:43-52): biggest gaps per subsystem - empty menu silent (`choose.py:435`); `p_success` wrong at small pools (`band_odds` B10-08); attacker takes no harm (CP-T03-00); 0 fields fought in the stored seed-0 run; Proceedings pool reads nobody (`pool_default`, `sigma.py:119-131`; under the H-213 ceiling of 2 the room can only lower the obstacle); `finding.none` reaches nobody; threadwork has no provider role; hunger hurts no body; no succession (IN-61 stopped at H-230); distance is free (CP-T10-01).
  - Army/kit: BUILT `march`, `requisition`, `transfer`, `issue`, `seize`, `dispatch` (writes nothing); DESIGNED `levy`, recruit regrowth, order of battle, `marshal`, `besiege`, `surrender`, `exchange`; MISSING recruit, muster, supply, disband, merge, equip, repair, craft, `Person.kit`, durability (:34). No live UI spec exists - old UI docs all archived (ED-IN-0231) (:35).
  - P3-C: map renders only what the seated person holds claims about (AX-2, `04:851-862`); promises a distance cost the engine does not charge unless CP-T10-01 `route()` lands (:82).
  - Klapp hook (:71): player is a person at the cathedral whose ledger receives the seeded claim first; `destroy_record` is withheld for everyone (`engine/season/data/fixtures.py:958`, `withheld_verbs`).
- **Conflicts / stale:** an earlier analyst count of 45 eligible rows for an unseated person is superseded by this measurement (:31); the aperture P9 in the thrust-layer probes gives 41 of 56 for an unseated person (`probes/p9_...:83`), consistent. `seat_probe.py` scratch not in repo.
- **Open items:** ruling 10 (management reading and budget), 11 (believed word), 12 (what console may show), L-3 (map of believed holdings), M3 before unit counts (:27, :85).

### proposals/2026-10-28-content-architecture-suite/05_A7_subsystem_merit.md
- **What it is:** Part 05 (analyst report A7): what each of ten subsystems needs to be worth playing alone and to matter to the world; ranking; order of becoming playable; two escalations.
- **Status:** "PROPOSED ... HELD BACK IN FULL" (:3). Reading: reference; analyst figures not re-verified.
- **Bears on:** CORE, PC, MB, SC, FI, WR, SE, FA, DICE, GO.
- **Content that matters:**
  - Test for earning a place (:19): a small game with one central tension AND it writes something the season loop reads back. "None of the ten is playable today": no seat for a human - `dispatching_chooser` is called only by tests (`harness/play_surface.py:41`). Four can stand as minigames (personal combat, Proceedings, mass battle with troops, fieldwork), threadwork as a small one; dice and season loop are the frame; settlements/factions/travel-NPC life become the management menu (:20-23).
  - Per-subsystem gaps (:29-163): dice - three rollers (social, mass battle's own, a smooth `p_success` curve wrong at small pools: pool 2 vs obstacle 2 the dice fail 74.0% and the curve says 85.6%) (:32); season loop - only the top question kept (`fixtures.py:481`), no season report, no stakes (no ending stops the game; succession unbuilt IN-61/B10-09) (:40-42); personal combat - attacker risks nothing, kit belongs to the fight not the person (`combatant.py:94`), `challenge` writes nothing (VT:772), no yield in the season; the personal fight resolves at RESOLVE (`rosters.yaml:1080`; ENCOUNTER holds only `a field`, :1284) (:62-68).
  - Mass battle: no battle fought at seed 0 (`.../ctl/realm_seed0_2seasons.txt:41-42`); army is whoever lives at home (`loop/sides.py:116`); no troop stock (CL-TROOP held on M3); upkeep IN-52 switched off; no siege. K-MB-4 (a research recommendation, ruling 6): plan fixed before battle as in Dominions, no live command (:85-98).
  - Proceedings: pool reads nobody (`pool_default`, `sigma.py:119-131`); under the H-213 ceiling of 2 the room can only lower the obstacle (`roll.py:63-100`, `test_sc02_reception.py`) [UNVERIFIED non-zero reception]; `speak` changes nothing; nested run unbuilt; speech cannot lie (J-C-6). `21_RECONCILIATION.md:617` (ED-SC-0039) refuses to show the room, the obstacle or the odds (:100-108).
  - Fieldwork: a failed inquiry tells even the investigator nothing (`rosters.yaml:1147-1151`); `interview` uncovers nothing; no case object; rule AX-7: nothing grades the player's conclusion (:114-119). Threadwork: not plugged into the season loop (`loop/matter.py:135`); `thread_read` writes nothing; mending is free (TW-T:137-143) (:128-131). Settlements: hunger hurts no one (`body_step=0`, `fixtures.py:594`), harvests do not depend on labour (:143). Distance is free (`budget.py:60`); ageing, illness and hunger all off (:159).
  - Order of becoming playable (:181-189): frame (seat, season report, heir handoff) -> combat (both fighters risk injury, kit slots, text replay) -> Proceedings (trial where pool and obstacle read the case) -> fieldwork -> management menu (hunger, labour, levy; needs M3) -> mass battle with troops -> travel -> threadwork.
  - Escalations (:193-195): E1 M3 allow a counted troop stock in `Rung.stores` (amends Layer 1 `04_CODE_ARCHITECTURE.md:801`, `:810`; recommends yes, option A of `proposals/2026-10-16-troop-stock-design.md`); E2 J-T5 where a person's kit lives (`hold` Tenures on equipment objects, K-5; whether that is a Layer-1 amendment [UNVERIFIED]).
- **Conflicts / stale:** "Threadwork ... `thread_read` writes nothing" vs 07a row 27 (thread_read formed 4, executed 1 in the stored run). Combat resolve-timing was corrected at 07d to RESOLVE. Cites `04:793/:802` replaced by `:801`.
- **Open items:** E1, E2; troop-grade ladder, recruit share, A1 content, kit values left for Jordan (:191).

### proposals/2026-10-28-content-architecture-suite/06_A6_attribute_demand.md
- **What it is:** Part 06 (analyst report A6): re-derives the attribute set from verb/module demand (104-moment matrix); verdict eight attributes, TS on its own carrier.
- **Status:** "PROPOSED ... HELD BACK IN FULL" (:3). Reading: reference; analyst figures not verified (:8); the suite's three-lens review found errors in some (:8).
- **Bears on:** CHAR, DICE, PC, MB, SC, FI, WR, GO.
- **Content that matters:**
  - Verdict (:12): six stay (STR END AGI ACU WIL CHA); Focus merges into Will, Bonds into Charisma, Attunement splits into Perception + Insight: eight on 1-7. TS stays on its own carrier (`Person.thread_sensitivity`, `state/carriers.py:717`) and is not a tenth.
  - Built evidence (:16-23): `verb_table.yaml` 56 rows; 8 carry `contests:` (`fight`, `accept` -> combat; `march` -> mass battle; `tell`, `arrest`, `speak`, `argue`, `determine` -> `social_contest.roll`); 3 graded inquiries (`research`, `examine`, `surveil`, `rosters.yaml:1143-1145`); 45 of 56 rows read no person quantity (`verb_table.yaml:33-35`); `capability[verb_capability[verb]]` else `pool_default` (`sigma.py:119-131`), only `tell`/`speak` map to `copying`, 1 of 430 persons holds it. None of the nine attributes is read on the season path - no `Person.attributes`, no `faculty` (CR-20 "LANDED ALREADY" is wrong, `workplans/valoria_master_workplan_v10_part4.md:184`).
  - Module readers (:26-32): `Combatant(strength, agi, end, cog, att, spirit, focus, history, disp)` (`modules/combat/combatant.py:93`; `att` is used for `reflex = (2*agi+att)/3` and `reading = (2*cog+att)/3`, `combat_systems.py:171-172`; `focus` feeds `conc_max = 3F+2S`); mass battle `derive_command(charisma, cognition)` 2:1 (`core/exchange.py:57-66`); threadwork pool `2*spirit + min(3, history+3) + ts//10` (`systems/threadwork/sim/operations.py:235-247`, Leap gate TS>=30); knots gate/cap on `bonds` (`bonds//2+1`) (`systems/fieldwork/sim/knots.py:185-216`).
  - Matrix "primary in": ATT 27 (29% of 94 contested draws), ACU 21, CHA 17, AGI 15 (22 with stealth), END 11, TS 11, STR 10, WIL 9, BON 7 (orphan), FOC 1 (orphan); gaps stealth (8) and lore close as keys on AGI/ACU (:38-54). 83 of the 104 moments are designed (from PROPOSED lexicons `proposals/2026-10-16-verbs/` files -09..-18), 11 built, 10 module (:34-36).
  - Set: STR END AGI ACU PER INS WIL CHA with key bases - labour, fieldcraft, stealth/craft, argue/inquiry/reckoning, watch, insight, thread, copying/command (:80-89). `faculty(p, verb) = max(capability[k], attributes[vocation_attribute[k]])` else `pool_default` (:97); opposition symmetric (same attribute resists) (:100).
  - Touch list (:105-121): `references/descriptor_registry.yaml:24-53`; re-derive `names_index.yaml:75-84` then `tools/export_descriptors.py` -> `engine/engine_params/descriptors.json`; `tests/valoria/test_descriptor_registry.py:19,21,33,39,43`; CR-20, CR-33; one ED-IN row from `id_reservations.yaml` `next_free`; port `CharacterData.gd:14-23` already exports ten legacy fields on 22 `.tres` files despite the IN FLUX bar (re-bind after ruling, ED-1050).
  - Escalations (:131-135): the count (eight overrides ED-IN-0185 "it will be 10"; recommends yes), warmth vs presence, who resists.
- **Conflicts / stale:** this file claims ED-IN-0301 "re-opening on his word, which he has now given" (:128); `07a` (adjudication) says only Jordan can take A6's eight and recommends nine + TS (Needs Jordan 1); `03` says an override "needs his explicit word". Three documents disagree on whether the override is already given. The scratch path for `matrix.py` is a /tmp path (:36), not in repo; `06b` holds its text.
- **Open items:** the three escalations; REM-30 / fieldwork verbs to re-measure PER/INS demand.

### proposals/2026-10-28-content-architecture-suite/06b_A6_matrix_and_probe_evidence.md
- **What it is:** Recovered scripts and printed output behind A6: `matrix.py` (104 moments), `alt.py`, the P2 probe script and output.
- **Status:** "PROPOSED ... HELD BACK IN FULL" (:3); evidence "of how the counts were made, not tools of this repository, and nothing here has been re-run" (:8). Reading: reference, reproducible by pasting into Python (not run by this lane).
- **Bears on:** CHAR, DICE, PROCESS.
- **Content that matters:**
  - `matrix.py` enumerates moments as `(verb, subsystem, status B/M/D, primary caps, secondary caps)` with a `CAP` map (force->STR, tough->END, quick/hand->AGI, reason->ACU, notice/readp->ATT, presence->CHA, warmth->BON, resolve->WIL, attend->FOC, thread->TS, stealth/lore->None=GAP) (:14-72). The mapping of each moment to capacities is the analyst's judgement ("[REASONED mapping]"); `readp` (reading people) is a single capacity merged into ATT in the "nine" set, which is why ATT dominates.
  - Printed results (:240-323): 104 moments = 83 D + 11 B + 10 M; primary counts ATT 27, ACU 21, CHA 17, AGI 15, END 11, TS 11, STR 10, WIL 9, stealth 8, BON 7, FOC 1; Jaccard >= 0.3 only AGI-STR 0.39 and TS-WIL 0.33. Contested draws 94: ATT 29%, ACU 21%, CHA 17%.
  - Set comparison (:303-311, :359-364): nine max ATT 29% min 1 (FOC); A6 eight max CHA 23% min 10; nine+TS=10 keeping BON max AGI 22% min 7 (this is the "B-10" option the suite later names); #505's six max Sense 29% min 9.
  - On the 21 built+module moments every set has ACU/Wit at 55% max (:313-317), and on the 11 built season moments ACU 6 of 11 (:319-323) - the demand evidence on code that exists cannot separate the sets.
- **Conflicts / stale:** alt.py contains a dead expression (`... if False else`) in its print line (:126, :239) - cosmetic. The `-10` in `nine(reg)` row reports n=10 because TS is counted.
- **Open items:** none; re-run after REM-30 and the fieldwork verbs (per `03` falsifier).

### proposals/2026-10-28-content-architecture-suite/07a_ADJ1_character_verbs.md
- **What it is:** Conflict adjudication ADJ1: 219 rows (clusters of C-001..C-100 character and C-374..C-492 verbs/decision) of the suite's 754 recorded conflicts; table of 32 clusters with winner and basis; corrections to the main report and proposals.
- **Status:** "PROPOSED ... HELD BACK IN FULL" (:3); unlike parts 01-04 "nothing in this file is known to be missing" (:8). Reading: reference; the strongest single digest of what code actually does at `be24c71`.
- **Bears on:** CHAR, CORE, DICE, PC, WR, FI.
- **Content that matters:**
  - Verified verdicts (:16-23): nine 1-7 attribute keys + a tenth ruled-but-unnamed (`references/descriptor_registry.yaml:36-48`, `:28-33`; ED-IN-0301 "nine keys; the pending slot refuses a value", `registers/editorial_ledger_in.jsonl:87`); 15 pursuits x 7 bipolar axes and 5 affiliations on `Person.conviction` 0-5 (`descriptor_registry.yaml:134-168`; 13 convictions and 4 axes RETIRED); TS written once at world build from the registry (`engine/season/data/cast.py:283`), never in play; `thread_read` gate 30 (`fixtures.py:948`); Coherence has no season carrier (its `write_matrix.yaml:185-192` row is seam-only, no producer) and the T2 model is a DISTANCE with 0 equilibrium (ED-WR-0010); 56 verb rows, 51 `resolvable_verbs()`, 50 offered by the populated chooser (`destroy_record` withheld, `fixtures.py:958`; `populated.py:1710`), 8 contested; chooser score `damp*sum(axis_w*align) + stance + urgency` (`decision/choose.py:130-151`), Plackett-Luce at tau 0.1, no capability or odds term; budget 5 + 1 per live hold - body bands - legs, floor 1 (`decision/budget.py:55-61`), extended scene costs 2, a scene holds at most 3 interactions (`fixtures.py:488-489`).
  - Row 1 (J-T2): winner "nine keys plus a pending tenth" (ED-IN-0185 narrowed by ED-IN-0301 and v10 M2 `workplans/valoria_master_workplan_v10_part6.md:33`); #505's six, template A-1's eight, from-scratch eleven/fourteen all PROPOSED under CL-ATTR (`_part12.md:12`). Recommendation (:71): hold to the ruling - nine plus TS counted by reference to `Person.thread_sensitivity`; take A6's merges later as a separate amendment once designed verbs exist.
  - Row 26-27 (:52-53): quotes "seed 0, 2 seasons: 1,176 of 1,511 attempted acts carry a refusal (77.8%); 888 (58.8%) refused with no execution (`scratchpad/aperture_out.txt:143`); 67%, 76.8% and 28.7% are other denominators"; per-verb: work 0/72, restore 0/21, train 0/42, commit 0/64, carry 0/31, convene 1/5, utter 44/44, examine 61 all `finding.none`, research 131 executed (124 `finding.none`); stance written by march and forgive only (`effects_combat.py:327,475`); `write_matrix` 40 rows + 6 retired. "`work`, `train`, `restore` never succeeding is a live defect for the plan."
  - Row 28 (:54): `determine`'s typed cell drops the fired-Date clause its prose names; `verb_capability` = {tell, speak -> copying} only; cohorts have no commit gate (NP-G36 PROPOSED); `succeed` not resolvable.
  - Row 31 (:57): the K-register K-01..K-56 (`proposals/2026-10-03-verb-coverage-and-gap-fill.md:2570-3144`, RATIFIED AS INTENT, ED-IN-0288): no `proclaim`, `besiege`, `execute`, `steal`, `interrogate`, `truce` rows; Record kinds are text, dispensation, petition, works, faction_sheet, cover (no war, treaty, alliance, custody).
  - Stale-comment fixes called for (:38): `decision/choose.py:440-441`, `decision/options.py:386-398` and `rosters.yaml:525` still say "thirteen", "four-axis", "13x4" while the code runs 15x7; `npc_registry.yaml:981` names Cardinal Justice as NPC-004 where it is NPC-038 Olafsson (:36).
  - Corrections list (:60-68): REPORT's "TS on persons needs J-T2" is wrong (TS is built; 10 cast rows authored; 4 persons pass gate 30; `thread_read` formed 4, attempted once, executed once); "naming TS unlocks 12 arcs" is wrong; "LANDED ALREADY: faculty" is false.
- **Conflicts / stale:** the note at top (:12) withdraws "77.8%/58.8%" for having no named instrument and substitutes "327 of 1,132" from `proposals/2026-10-22-system-description/ctl/realm_seed0_2seasons.txt:1-40`; but the saved thrust-layer probe P1 (`probes/p1_s2_seed0.txt:1`) reproduces 1,176 refused of 1,511 attempted = 77.8% by the driver definition (and aperture P9 gives 1,182 acts) - so the "withdrawn" figure has a named, reproducible instrument, and three different attempted-act denominators (1,132 / 1,182 / 1,511) circulate. Row 26 (:52) predates the note and is left unedited.
- **Open items:** J-T2 (the one live question); fix stale comments; correct `determine`'s prose requires or type the Date.

### proposals/2026-10-28-content-architecture-suite/07b_ADJ2_faction_settlement.md
- **What it is:** Conflict adjudication ADJ2: 149 faction and settlement/geography rows (C-101..C-249) of the suite's 754 recorded conflicts; clusters F1-F15, S1-S13, precedent rows; corrections list; three "Needs Jordan".
- **Status:** "PROPOSED ... HELD BACK IN FULL" (:3); "nothing in this file is known to be missing" (:8). Reading: reference; strong snapshot of what `build_realm(0)` and the faction/settlement code do at `be24c71`.
- **Bears on:** FA, SE, CORE, GO, WR.
- **Content that matters:**
  - Measured (:12): `build_realm(0)` gives realm 1, duchy 3, territory 17, settlement 37, community 60, hearth 211; 32 offices (31 `offices.yaml` seats + the rowless `off_npc_084`); 2 foreign seats not built; territories held 15 of 17 (T15 Askeheim, T16 Schoenland unheld); no office sits on a settlement rung; GEO has 17 provinces, 37 settlements over 16 territories, 26 territory edges, 55 settlement edges, 7 types. `test_in35_lattice_coupling.py` 8/8.
  - F1/F2: `fac.*` stat block, Mandate, Influence, Intel key and legitimacy scalars RETIRED at plan v8 position 29b (2026-10-01) (`references/descriptor_registry.yaml:76-79`, `engine/substrate/descriptors.py:19-22`, `restructure_ledger.md:2687-2701`); legitimacy is a per-knower query (`queries/person_q.py:452`); `set.*` rows (`descriptor_registry.yaml:84-90`) have no runtime reader - retire (A3 D2). Faction is a frozen five-field view never stored (`queries/faction_q.py:84-96`).
  - F6: `systems/factions/` deleted (29b, PR #450); ED-IN-0284 makes factions a module (unbuilt - `modules/` has no `factions`); ED-IN-0283 (Jordan: retire-set "all of this is wrong") is newer than CLAUDE.md s3's "three retained" sentence and wins - "correct CLAUDE.md s3 to cite ED-IN-0283/0284".
  - F7: seats conferral appointed 17 / elected 8 / null 6; revocation basis on 15 seats; 7 built seats cannot refill (6 by rows, 7 by world); `succeed` unresolvable (aperture "no"); its W3 cell exists (`verb_table.yaml:1205-1216`).
  - S2: no `levy` verb row. The troop levy is **built, shipped off**: `requisition` -> treasury -> `settlements.provision` -> field (`tests/test_levy_feed.py:1-6`, `fixtures.py:696` `field_provisioning=False`, H-241) - "flip is a default decision, not a build".
  - S4: Rung has 8 fields (`carriers.py:1050`); tiers realm/duchy/territory/settlement/community/hearth (`province` is in `rung_kinds` but never built); size 0-3; 26 territory edges read for lattice coupling (`data/geography.py:43-61`, `loop/matter.py:156`), 55 settlement edges read by nothing; gate edges exist (2) but type unread; 8 `settlements.*` contracts; one cohort per settlement (`cohorts.yaml`).
  - S11: nothing in `engine/` reads a territory temperament; cohort `pursuits` are empty; M1 NARROWED (SE-06): territory vectors into `cohorts.yaml` behind a check. S8: GEO `proximity_calamity` T8=4 and T17=4 contradict band 5 and no code reads the field - fix or delete.
  - F11: Godot port `valoria-game/systems/data/ValoriaDataLibrary.gd:20-25` ships `_niflhel()` and per-faction stat blocks and has no Schoenland or Altonia - re-export from the oracle (ED-1050).
  - Needs Jordan (:68-70): (1) Mayor seats - title ruled (`offices.yaml:171`) but no seat authored; all 37 towns governed from territory/duchy/realm seats (4-14 governors each); recommends 37 vacant `appointed` Mayor seats after measuring `confer` load; (2) runtime founding of factions (FA-G39 PARKED) - Restoration Movement can never rise; recommends `utter` OUGHT + `commit`, new seats only via `establish`, name into a runtime roster; (3) Altonia/foreign default (IN-36) - keep off until a `foreign` relation has a producer.
- **Conflicts / stale:** `dice_engine.py:245-251` still cites the deleted `crown_initiative.py` (F13). `supersession_register.yaml:17-36` still calls `fac.legitimacy` live - owed a close. Corrections to A3: "37 settlement rungs under 17 territories" should read 16 (:57); the engine reads `adjacency:` and `terrain:` (:63). Numbers dated `be24c71`.
- **Open items:** the three Needs-Jordan items; build `succeed`'s effect; move temperament vectors into `cohorts.yaml`; decide the `field_provisioning` default.

### proposals/2026-10-28-content-architecture-suite/07c_ADJ3_events_arcs_clocks.md
- **What it is:** Conflict adjudication ADJ3: 166 rows (events/decks C-250..282, arcs/NPC arcs C-283..373, clocks/world/victory C-629..670).
- **Status:** "PROPOSED ... HELD BACK IN FULL" (:3); "Every cite was opened or re-measured" (:12). Reading: reference; "Needs Jordan: None" (:113).
- **Bears on:** WR, ARCS, CORE, FA, CHAR.
- **Content that matters:**
  - Measured (:16-40): `engine/season/tensions.yaml` absent; plan adopts 6 cards (Royal Crisis, Feldmark Famine, Cardinal Independence, Guild Fracture, Einhir Incident, Ministry Crisis), `build_realm(tensions=True)` draws one, switch ships off (`workplans/valoria_master_workplan_v10_part4.md:526-527`). Jordan's 45 = Tensions 6 + Goldenfurt 28 + 11 named cards; grounded deck "58" is its own claim (by script 50 ids named, 8 written; 40 KEEP + 19 REVISE = 59), not in the 45.
  - Arcs (:22-28): 55 numbers / 58 titles; `ENDINGS_CLASSIFIED.yaml` 50 rows = 48 ARC + EMG-10/11 = 18 unforced DECIDER/ROLL, 11 forced, 8 THRESHOLD, 9 NEVER, 2 UNCLEAR; the 9 NEVER rows are ARC-05, 16, 24, 25, 26, 28, 36, 38, 39 (39 forced); ARC-46..55 unclassified (only in `cases/ARC4.yaml`); 97 ARC-lane cases; 143 = 97 + 46 NPC.
  - Clocks: "None runs in the loop" - "six steps, four barriers... no container gets a clock" (`engine/season/loop/driver.py:239-240`), "NO CLOCK GENERATES" (`loop/census.py:39`); CI, IP, RS retired at 29a/29b (`systems/overview/sim/__init__.py:9-13`); `ms_track.py` (MS_START 60) still on disk with no importer (retirement owed at 29a-ms); lattice coupling replaces the MS scalar (`hole_register.yaml:4884`; `loop/matter.py:136-138`). Stale registry: `references/module_contracts.yaml:542` and `registers/mechanics_index.yaml:140` still call `ms_track` the "live tick" (:98).
  - Endings (:35): two rows exist, `peninsular_sovereignty` (victory) and `theocracy` (`rosters.yaml:2553-2615`), both read by `endings_reached`; none reachable - H-176 graded `absent` (`hole_register.yaml:3969-3978`); fix is CP-T09-04's unpeopled `seize`. Calendar: no year unless `season_factor_draw` has a table, which ships `()` (`queries/world_q.py:936-942`); a card may not carry a date (T-c).
  - Records/tenures (:37-40): `record_kinds` text, dispensation, petition, works, faction_sheet, cover; `tenure_kinds` 10 members incl. detain, ban, tie, knot; `open_case` mints kind `text` (`loop/effects_information.py:286-287`) - `assessment` and `exposure` are not record kinds (NEW).
  - Arc form: M20(b): ordered stage conditions on the person's own ledger; `closing`, `successor`, `deal` struck (`scratchpad/src/v10-05-jordan-queue.md:165-170`) (:66). Vaynard A/B and Himlensendt C bodies are recoverable in the v1 file (`.designs/systems/npcs/reference/npc_behavior_system_v1.md:496-506`, `:466`) (:68, :105).
  - Correction 1 (:101-103): the ED-IN-0225 sub-question is not Jordan's - it refuses only an arc *carrier*; M20(b) narrowed it; amend `_part12:276` "no arc is a carrier, a card field or a loaded row" to allow `source:` quotation. Level-0 name: canon says "Coherence Failure" (`canon/01_foundations_amendment_self_rendering.md:92`), skill says "Rendering Crisis" (`coherence-tiers.md:264`) - rename the skill heading (:74).
  - Narrative voice (:69): no CURRENT.md voice row; `skills/prose-writer/SKILL.md` is the one live surface (render-only); no Person coherence field exists, only a write guard (`state/world.py:1010-1017`) [GAP].
- **Conflicts / stale:** `ms_track`/"live tick" in two registries; REPORT "2 of 9 NEVER arcs numbered" and "ARC 19 NEVER and dead" are wrong (:104). "Hunger binds after CR-22" and "hunger cover counts ore and timber as food" are [UNVERIFIED] (:81, :84).
- **Open items:** CP-T09-04 (B10-17) to make an ending reachable; 29a-ms deletes `ms_track.py`; GD-1 sustain/Accord/PS clauses held as the `rosters.yaml:2590-2600` assumption under the plan's LEAVE trigger.

### proposals/2026-10-28-content-architecture-suite/07d_ADJ4_subsystems_ui_process.md
- **What it is:** Conflict adjudication ADJ4: 220 rows (subsystem rules C-493..C-628, process C-671..C-754) in 37 clusters; corrections to the proposals; two "Needs Jordan".
- **Status:** "PROPOSED ... HELD BACK IN FULL" (:3); "none needs a new design ruling" (:14). Reading: reference; the most code-anchored account of PC / MB / SC / FI / TW rules at `be24c71`.
- **Bears on:** DICE, PC, MB, SC, FI, WR, GO, PROCESS, CORE.
- **Content that matters:**
  - Dice (:28): TN is 7 and refused otherwise (`engine/dice_engine/dice_engine.py:182-199` `_require_tn7`; MB `roll_pool` asserts it `modules/mass_battle/resolution.py:46`). Advantage is a mu-shift (`seam/wrappers/sigma.py:41`); the room's favour and forgery quality are instance modifiers under "score/2 plus modifiers" (`modules/social_contest/roll.py:63-100`); the Gaussian `p_success` gap is real (R-F11) -> build `odds_of` (B10-08).
  - Wounds (:30): ED-PC-0005 - each wound adds a fractional Ob, 0.15 attacking and 0.25 defending (`modules/combat/config.py:123`), folded into net_sigma; `WOUND_POOL_PENALTY` removed (`combatant.py:16`); "-1D per wound" loses. `modules/combat/` is the resolver head (`CURRENT.md:21`); seize is DEAD in code (`ability_primitives.py:25`, `combat_systems.py:1069`); LOC combat 5,727, MB 10,163; 54 weapon keys.
  - Fight timing (:32): "the body" carries no `step:` so a personal fight resolves at RESOLVE (`engine/season/rosters.yaml:1079`, :1293-1300); only "a field" has `step: ENCOUNTER` (:1284); the move to ENCOUNTER is REM-31 (B10-10, unbuilt); trace returned (`seam/wrappers/combat.py:252`).
  - Margin ladder (:33): one owner `seam/ladder.py::degree_of` with separate bands per subsystem (`combat_degree` :136, `field_degree` :185); errata G5 and F-S1-3 ("shared four-band ladder") are wrong.
  - Mass battle (:34-35): `POOL_QUALITY_MODEL` on (`modules/mass_battle/config.py:556`): pool = eff_power x eff_size x 0.5 with **no Command** (Jordan 2026-07-08); Command = (2*CHA+COG)/3 clamped 1-7 (`core/exchange.py:55-64`); morale starts from members' mean stance toward their faction (`massbattle.py:119`); encirclement flat -1D floor 1 (`orchestration.py:1304`); a same-faction field cannot occur (`loop/sides.py:130-133` subject None -> Unopposed).
  - Threadwork (:38-39): `DEPTH_OB`, `DEPTH_TS_MINIMUM` (`operations.py:77-95`), Leap gate TS 30 (:358-366, beating the registry's 25); M18 TAKEN (b) `min(3,history)+3` but the code still reads `min(3, history+3)` (`operations.py:246`) -> build REM-45 (B10-15). Knots: ED-912 -5..+5 gauge, formation Spirit x2 + History at Ob 2 (`systems/fieldwork/sim/knots.py:13-95`), knots.py is test-only; the case board is unbuilt (0 symbols in engine/modules).
  - Social contest (:40-43): old kernel retired by ED-SC-0033 (2026-09-06), SC-05 (2026-10-16) kept `roll.py`; opposed Ob = score/2 + modifiers (`roll.py:67-69`); pool is `pool_default` for everyone (`sigma.py:119-131`); the plan contradicts itself on SC-05 timing (`_part3:489` vs `_part5:301`); 6 speech kinds built, all forensic (`arrangements.yaml` `speech_kinds`), 12 is the design list (`04_VERBS.md:236-239`); `systems/social_contest` has 18 files.
  - Corrections (:71-79): `21_RECONCILIATION.md:617` refuses to show the room, obstacle or odds - Proceedings shows no odds; P3 L-1 is Jordan's own directive (record as a GO/PC ledger row); believed odds: M1 DECISION *releases* CP-T01-03 mode (b) (v10 `-05` M1; `_part4:144`) so a display reader is a build, not a ruling - contradicts `04` which says AM-B-03 withdrew it and makes it ruling 11.
  - Godot (:47-48, :79, :84): states "4.7 (ED-GO-0002, `editorial_ledger_go.jsonl:1`, RULED 2026-10-09)", `valoria-game` pins 4.3 (`project.godot:11`, `godot-ci.yml:68`), README says 4.6; port repo has 8 .tscn, 129 .gd, 37 .tres (22 characters, 15 triggers), 13 GdUnit suites, 289 `func test_`; `game_constants.json` carries 13 keys against ttrpg's 6, 7 extras from retired models; `KeyStore.gd` survives; `godot/skeleton` has 20 files (GO-14).
  - Needs Jordan (:83-84): (1) CLAUDE.md s3's line "systems/ - design source of truth for combat, social_contest and mass_battle (retained by ED-IN-0204)" contradicts ED-SC-0033 and ED-IN-0284; ED-IN-0283 (d) leaves it to Jordan; recommend rewording - **that exact sentence is still in the current `CLAUDE.md` s3**; (2) one port PR to the ruled engine version, drop the 7 stale constants, delete `KeyStore.gd` and the 15 trigger resources.
  - ED id locations: ED-IN-0204, 0225, 0231, 0232 are in `registers/archive/editorial_ledger_in_archive_pre-2026-09.yaml` (:1956, :3209, :3697, :3779), not the jsonl files (:56). PP numbering: PP-684..688 became PP-711..715 (`patch_register_active.yaml:17`); PP is not frozen (:62).
- **Conflicts / stale:** the Godot version "4.7" is asserted here but current CLAUDE.md says nothing here asserts a version and the ruling lives only in ED-GO-0002 - treat the number as unverified. ADJ4's believed-odds correction contradicts `04_P3` and `01_MAIN_REPORT_part2` ruling 11. CLAUDE.md s3 wording item (1) unresolved at repo head.
- **Open items:** the two Needs-Jordan items; REM-31, REM-45, `odds_of`; correct `_part5:301`; M2 carrier text.

### proposals/2026-10-28-content-architecture-suite/08_decks_and_template_in_engine_form.md
- **What it is:** Part 08: rewrites the old Tensions deck (6 cards) and Goldenfurt deck (28 cards) into the only forms `engine/season/` carries (`goals.yaml` rows, a `yield_scale`, a held Record), with 27 YAML goal rows, a generative settlement template, a specified-not-tested seasonal docket, and a three-arm attention measurement.
- **Status:** "PROPOSED - HELD BACK. Reference under CLAUDE.md s0.05 until a loader reads it; merging ratifies nothing. Every row is [ASSUMPTION; medium; Jordan to correct; revert: delete the row]" (:3). Reading: reference; the YAML blocks are the only content-as-data in this suite and nothing loads them (no loader, not under `engine/season/`).
- **Bears on:** WR, FA, SE, CHAR, ARCS, CORE.
- **Content that matters:**
  - Executed (:12-17): each of 27 rows alone and all together (65 rows with the 38 existing) is accepted by `data/goals.py::parse` when swapped in via `goals.rows_replaced`; the 9 Goldenfurt rows each mint a Proposition with exactly one committed person (`gf_commune_against_guild_toll` -> NPC-081, `gf_guild_holds_the_ford` -> NPC-007, `gf_law_sides_with_commons` -> NPC-074, `gf_crown_wants_men` -> NPC-036, `gf_crown_wants_grain` -> NPC-037, `gf_crown_watches_the_comptroller` -> NPC-033, `gf_church_draws_near` -> NPC-021, `gf_old_rite_in_the_hamlets` -> NPC-003, `gf_levy_grievance` -> NPC-081); content hash moves with rows on (`3e31638ef6ee` -> `2e7f4f3d01da`).
  - Tensions cards (:19-30): 1 Royal Crisis = goal on a plotting faction (Varfell / Restoration Movement / Hafenmark) with object `seat_holders` of `off_king`/`off_widow_regent`/`off_heir` stance -1 (9 rows); 2 Feldmark Famine = `yield_scale` 0.75 on `terr_T5` (no loader); 3 Cardinal Independence (4 rows, rung `set_s_001`); 4 Guild Fracture (`off_guild_comptroller`, rung `set_s_018`); 5 Einhir Incident (`off_restoration_leader`, `terr_T4`, `terr_T13`); 6 Ministry Crisis (stance -1 on `off_parliamentary_clerk`). Lost: the date (T-c), "succeeds when it fires" (T-b).
  - Goldenfurt (:140-160): persons G01-G06 not added (cast closed at 46, ED-WR-0011); 13 of 28 cards expressed in whole or part by validated rows, 2 by `yield_scale`, 1 by an owed seed Record (G505), 12 with no engine form (Directive with no verb G205; no event writer G301/G401/G403/G501; field force G302/G404; foreign actor G504/G604; no province rung G601; no Thread site at S-006 G701/G702).
  - A `works` seed for a chapel is refused: `site_kinds` has no chapel and `mint_planned_works` rejects an unpriced plan (:152).
  - Settlement template (:209-225): five opening kinds (market dispute, levy grievance, church draws near, old rite, law sides) with slots as seat/body roles; type-eligible settlements 36/37 (Guild), 37 (Church), 32 (Einhir), 20 (court/Parliament) but only 12/13/10/9 have a cast person homed there; no seat is anchored at a settlement (`offices.yaml:98`) so all bind to seats elsewhere; motives live in pursuits and goal rows, never cast `want:` (scored 0.0 salience).
  - Docket (:227-229): `deal: build | convene`; a `convene` effect that deals, write-matrix row, keyed draw (`draw_factory`, seed*tick*convener*"docket"), Proposition-carried visibility of drawn goals; needs plan-text amendments of B10-18 ("no step of the season loop reads a card") and B10-19 ("no dealing per season"). None built.
  - Attention reading (:235-246), 3 seasons, seeds 0 and 1, arms off / nine Goldenfurt rows on / placebo aiming the five rung-targeted rows at S-007: acts by the five persons with subject in S-006 = 11 / **29** / 9 (seed 0) and 4 / **21** / 3 (seed 1); placebo moves it to S-007 (23, 17). Total acts barely change (2088/2059/2072; 2080/2143/2170): rows redirect, they do not add.
- **Conflicts / stale:** the cited `goals.rows_replaced` and `data/goals.py::parse` are real symbols per the probes (`p2_goals_and_need.py` imports `engine.season.data.goals`) but `rows_replaced` is not confirmed [UNVERIFIED]. Home positions CL-OPEN / CL-EVENTS commits (3)(4) are in `workplans/valoria_master_workplan_v10_part4.md`, a v10 plan file [UNVERIFIED whether still live]. Whether the rows produce a story is explicitly "NOT shown" (:233).
- **Open items:** `settlement_openings` loader; corrected goals visibility; the seed-Record carrier; `yield_scale` loader; classify the produced acts and count cross-person chains / executed vs refused (:233).

### proposals/2026-10-28-content-architecture-suite/appendix_A1_content_census.md
- **What it is:** Analyst report A1 (Q1): world/character/narrative content in the game as coded, a four-layer verdict, blockers to a playable slice, and the "B10-S" text-client repair; 2026-10-28, repo head `be24c71`.
- **Status:** "PROPOSED ... HELD BACK IN FULL" (:3). Reading: reference, partly self-corrected by a three-lens note (:11).
- **Bears on:** CORE, GO, CHAR, WR, SE, FA, ARCS.
- **Content that matters:**
  - Verdicts (:19-26): carriers partial; content thin; player surface none; narrative text none in game. "Does workplan v10 contain a path to a playable slice? No" - "vertical slice", "playable slice" and "first playable" return zero hits across `workplans/`, the v10 proposal folder, `CURRENT.md`, `HANDOFF.md`.
  - `build_realm(0)` measured (:32): 83 persons (46 named, 37 cohorts), 32 offices, 412 rungs, 322 sites, 683 tenures, 67 Propositions, 0 Records; verb table 56 rows / 58 names, 51 resolvable, 5 not (`construe`, `evade/defy`, `exchange`, `succeed`, `tie/knot`), 40 `@effect_for` registrations; `Person` fields `id, name, weight, capability, stance, pursuits, ledger, body, born, scar` + `tenures`, `travel_leg` (`state/carriers.py:655`); CALENDAR fires `World.dates` when `due_at` arrives (`loop/calendar.py:39`); only `convene` writes them (`loop/effects_governance.py:413`).
  - Missing, ranked (:35-40): `Person.capability` empty on 83 of 83 (every pool is the default 2); no event carrier (no deck/card/omen; `season_factor_draw` ships `()`, `data/fixtures.py:469`); no text-bearing record kind (NM-W4); no kit/tradition/troop carrier, `tie`/`knot` declined (H-182); no arc/stage carrier by ruling (ED-603/604/605); closed cast of 46 (ED-WR-0011), AX-5 lists three self-moves only (`architecture/meta/01_AXIOMS.md:164`).
  - Content counts (:48-60): cast 46 (35 canonical, 11 proposed), 36 with a non-empty `arc_trajectory`; 10 factions incl. placeholder `faction x`; 17 provinces / 37 settlements / 20 terrain; 74 `description:` strings, 31 POIs unnamed; 38 goals (24 orientation mint no Proposition, 14 object-bearing); 42 buildings / 8 arrangements; 2 endings (H-176 none reachable, `hole_register.yaml:3972`); attribute values for 1 of 46; `register --requirements` met 3, partial 5, not_met 1 (R-05).
  - Stale parallel set (:62): `valoria-game` has 22 character `.tres`, 15 trigger `.tres`, 8 factions, 17 territories, 36 settlements; no GDScript reads any engine export; the 13 `trajectory_script_path` targets do not exist; 9 of 17 trajectory evaluators are `pass`. 8 `.tscn` each a bare node; KeyStore autoload live [RETIRED]; HEAD 6b0df3d (2026-08-19); declares 4.3, README 4.6; 289 tests excluded from CI (:80).
  - Narrative text (:91-96): `harness/chronicle.py::render` (:115) prints the deepest chain as `<n>. season <s> | <actor> <verb> | emitted <kinds> | answers <m>`, observer only; `skills/prose-writer` (SKILL.md 219 lines, 19 references, five coherence tiers) and Rendstad (7 scenes, 192 lines) are authored text wired to nothing; the skill selects voice by PC coherence, TS and Spirit, none of which `Person` carries.
  - Blockers table (:104-115): client over the `choose` seam (unscheduled); refusal ("67% of resolved acts refuse; 16 of 48 attempted verbs never succeed"); words; playable person; odds; stakes (halting ending, loss state, time box; H-176; CP-T09-04); seed-varying world pressure; freestanding storylines; bonds/companions; menus/save/art. Classes: (a) scheduled engine work (B10-04..18), (b) Jordan's content (attribute values of 46, weather, CL-THRUST ladders, heritage beyond two, lifepath key map, Tensions content, arms inventory), (c) nobody provides (client, text layer, fragments, storylines, loss state, companion, save/load, art/audio, POI names, slice-ending rule).
  - B10-S repair (:127-137): text-first Python client over `dispatching_chooser`, one seated mid-rung holder, screens "What I know" / `opening_set` candidates with `odds_of` band odds / act-degree-witnessed, stop at PC's line (CP-T02-06 / IN-61) or season N (default 12), control scripted-callback-equals-chooser hash test.
  - Freestanding storylines (:143-160): AX-5/T-c forbid an *unwound* clock but allow a clock "wound by a nameable act", and "a world-generation roster is not a clock and is lawful" - a world-generation-wound **fuse** writing only a situation (a dated Docket item, Record, Claim, Proposition) needs no amendment; proposed `engine/season/storypatterns.yaml` row fields (`id, scale, roles, precondition, fuse, question, exits, fragments, draw`) and a six-pattern seed pool (Rendstad jurisdiction, Disputed Succession, Feldmark Famine, Heresy at Himmelenger, Border Incident at Ehrenfeld, Guild Fracture; 3 of 6 = 20 combinations).
- **Conflicts / stale:** note (:11): refusal figures withdrawn (see 07a, but P1 reproduces them); "unseated has 45 of 56" superseded by 41; "appointing starts at a duchy seat" false. D3e's 64 Propositions stale (67 measured). "Does the v10 plan contain a path to a playable slice? No" is as of `be24c71`.
- **Open items:** E1 (may agents draft [ASSUMPTION] content), E2 (add B10-S ahead of the port gate), E3 (first playable person seated or unseated; recommends seated rung 1-2); [GAP] whether a boot-time Date can be written without an act's token.

### proposals/2026-10-28-content-architecture-suite/appendix_A2_character.md
- **What it is:** Analyst report A2 (Q2/Q3): the character - attributes, the verb-to-attribute rule, template layers, progression, and how a character chooses; code-first, with decisions taken.
- **Status:** "PROPOSED ... HELD BACK IN FULL" (:3). Reading: reference; the chooser account (:145-163) is a clean statement of what the code does at `be24c71`.
- **Bears on:** CHAR, DICE, CORE, PC, WR.
- **Content that matters:**
  - Verdict (:14): store nine 1-7 attributes + TS; a verb never names an attribute but a capability key which names one attribute; prowess := `faculty(p, verb)`. None built. Amend CR-20's `max(key, attribute)` to additive `faculty = attribute + min(cap, max(0, key - pool_default)) + practice_addend` (:83) - under `max` training is invisible for the talented (S defect, R loss); revert `max`.
  - Rule shape (:54-59): an attribute reaches a verb only if the row declares `contests:` (V-2); pool verbs map `verb_capability` then `vocation_attribute` (`key -> {act, resist}`; NEW optional `resist:` default `act`); module verbs map in the module adapter; gates are only own, remit, hold, presence, typed own-state (`decision/options.py:463-466`) - V-2a answered no.
  - Table of eight worked verbs (:61-70): `determine` has no key -> `pool_default` (`verb_table.yaml:383`); season command fixed at 4 (`modules/mass_battle/massbattle.py:183`); module fight pool `max(5, History+6)` (ED-901); seam derives only `end` from body (`seam/wrappers/combat.py:129-138`).
  - Character template four layers (:89-115): capability, ambition (commits to OUGHTs `queries/world_q.py:2168`), values (15 pursuits, stance, conviction inert at weight 0, scar inert at shift 0), personality (PROPOSED: three offsets rigid_flexible, grandiose_humble, deontological_instrumental, spread 0.15; built behind a spread-0 control - the only layer separating persons sharing a faction and office). Kit GAP (J-T5), TAKE `hold` Tenure on an item.
  - Lifepath four stages (:117-127): origin -> heritage + conviction intensity; formation -> keys + pursuit tilt; vocation -> keys (34 rows, CR-33); catalyst -> an authored OUGHT commit with a ladder + `tie` Tenures - "the freestanding-storyline hook"; magnitudes need a `source:`; content for 46 is Jordan's.
  - Progression (:129-143): `train` +1 on a held key (`loop/effects_combat.py:421-446`); pursuit shift 0.1 on a judgement (`loop/effects_information.py:550,580`); scars at 1/2/3 destabilise / weight shift / crisis (`queries/person_q.py:468-469`); conviction written at resolve (`loop/resolve.py:706`); attributes change only by age band and permanent wound.
  - How a character chooses (:145-163): `questions_for` (`queries/world_q.py:2717`) with sources `claim_landed`, `need`, and five standing occasions ordered by `attention_key`; rule `first` (`decision/questions.py:62`); View = <= 12 own-ledger claims; budget `5 + offices - body bands - travel legs` min 1; `opening_set` drops withheld / own-remit-hold-presence / TS >= 30 / no-referent rows; score `sum(axis_w*align) + 2*stance + urgency` (`decision/choose.py:130-151`); Plackett-Luce at tau 0.1; empty set returns `[]` silently. Stored but unused by a choice: capability/attributes (no odds term; CR-17 would weight by believed odds), name/born/weight, scar/conviction, goal/want text.
- **Conflicts / stale:** "choose" account does not mention that stance weight is 2x vs 07d's `stance_gain` documented as 2x via 1+g (consistent). The "nine" count conflicts with A6 (eight) - see 06/07a.
- **Open items:** escalations J-T2 (TS as tenth; recommends TS) and `max` vs additive excess.

### proposals/2026-10-28-content-architecture-suite/appendix_A3_faction_settlement.md
- **What it is:** Analyst report A3 (Q4, Q5): what a faction is and what a settlement is in the coded engine; templates as views/queries; generated-vs-authored stacks; MVP sets; eight decisions and two escalations.
- **Status:** "PROPOSED ... HELD BACK IN FULL" (:3). Reading: reference; partially corrected by 07b (settlements "under 16" territories, `adjacency:` is read).
- **Bears on:** FA, SE, CORE, WR, GO.
- **Content that matters:**
  - Faction verdict (:15, :21): a faction is a creed `Proposition` + live `commit` Tenures; the view `Faction(proposition, members, holdings, seats, head)` (`queries/faction_q.py:84-96`) is "NEVER a member of `World` ... `Act.actor` ... or a `hold` subject" (:86-90); membership is `commit`, "THE WHOLE OF MEMBERSHIP AND THERE IS NO SECOND ROUTE" (`world_q.py:1548-1559`); creed is an OUGHT whose subject is the authored leader (`harness/populated.py:1079-1091`).
  - Measured members/held rungs/seats (:26): Crown 11/6/11, Church 7/1/7, Hafenmark 4/4/4, Varfell 5/4/4, Lowenritter 4/0/3, Restoration 4/0/1, Guilds 4/0/2, Schoenland 1/0/0; `head` None for all (no writer of `Tenure.degree`, `faction_q.py:116-147`). Role templates cover 6 of 9 factions (`rosters.yaml:1598`); leaders cover 6 + Altonia (`:1640`); 38 goals: 20 owned by a faction, 18 by a body or seat (:27).
  - Missing (:31-36): no `declare` producer (CP-T09-02); no computed route to join (CP-T09-01) or `recruit` (CP-T09-07); `head` empty; no `conspire` (CP-T09-09); runtime founding parked (FA-G39). Canon "unique actions" become seat verbs (Royal Decree -> King's `issue`; Excommunication -> Church `determine` + ban; Economic Leverage -> `transfer`; Martial Law -> `arrest`/`march`) (:81). Verbs `covenant`, `seize`, `march` run in tests only (:78).
  - Settlement verdict (:85): a `Rung` (`carriers.py:1050-1106`, "owns NO social aggregate ... EVERY ONE IS A QUERY", `:1097`); no `class Settlement`. 37 settlement rungs; seven types (Town 15, Village 14, Seat 2, Fortress 2, City 2, Fortress-City 1, Cathedral-City 1); one cohort per settlement (weight 2) with empty `pursuits`, `stance`, `conviction` and no `commit` - "the people have no politics" (:89). 36 of 37 settlements reached by 4-14 governors from territory/duchy/realm seats; no seat at a settlement rung; `Mayor: settlement` ruled (`engine/season/offices.yaml:171`, H-90) but no seat (:91).
  - Missing (:95-100): motives for the people; `unrest` (CP-T08-06); a standing levy `tax` (CP-T08-07); local seat; ground endowment (CP-T08-02); `work` cannot run on dwellings or garrisons (empty floors).
  - VSG/VSG-stack decisions (:125-130): `build_realm` already is the generator; P1 location, P2 starting faction, P4 type, P7 infrastructure built; P3 size, P5 piety -> cohort `conviction`, P8 economy -> Site endowment, P12 temperament -> cohort `pursuits` seeded; P6 Altonian scalar, P9 caste scalar, P10 governance type, P11 allegiance die (D3 governance mode stays deleted -> query over conferral and body).
  - Decisions D1-D8 (:156-164): close stale `supersession_register` `fac.legitimacy` row; retire `set.*` (`descriptor_registry.yaml:84-90`; only `engine/substrate/descriptors.py:56` touches it; `governance_modes` deleted as unread `rosters.yaml:86`); no faction-named verbs (scripting drift); `declare` gated on `remit:dispatch`; the seven `venues` types are the type roster (Port, Mine, Outpost, Cathedral die); a deck card only deposits a claim or question to a named person; Guilds and Schoenland stay without a template.
- **Conflicts / stale:** "37 settlement rungs under 17 territories" -> 16 (07b). "engine reads only `territory` and `type`" - false for the file's `adjacency:` (07b). `registers/supersession_register.yaml:22-28` stale.
- **Open items:** E1 runtime founding (recommend `utter` OUGHT + `commit`, seats via `establish`); E2 vacant Mayor seat in each of 37 settlements after measuring `confer` load.

### proposals/2026-10-28-content-architecture-suite/appendix_A4_subsystems_playable.md
- **What it is:** Analyst report A4 (Q6): what each of ten subsystems needs to be legible and playable; the PARITY rule; session shape; top eight gaps; verb-menu taxonomy.
- **Status:** "PROPOSED ... HELD BACK IN FULL" (:3). Reading: reference; two statements are corrected by 07d (verdict "reads nobody"; "UI v4 jumps Part 9 -> 21").
- **Bears on:** GO, CORE, PC, MB, SC, FI, WR, SE, FA, DICE.
- **Content that matters:**
  - Verdict (:12): no subsystem is playable; the loop runs 83 persons with no seat for a human; every subsystem fails on no seat, no odds before a choice, no account afterwards. Seat unbuilt: `dispatching_chooser` (`engine/season/harness/play_surface.py:41-54`) has callers only in `tests/test_play_surface_dispatch.py` and `tests/test_combat_trace_returned.py`; v10 renamed IN-46 -> REM-31 and IN-47 -> REM-30, both in B10-10 (`workplans/valoria_master_workplan_v10.md:114`, `_part3.md:200`).
  - THE RULE: parity (:41) - a seated person's menu, budget, admission and resolution are byte-identical to what `make_chooser` would face; a callback returning `auto`'s pick must reproduce `content_hash`; presentation may be richer, the option set may not. Falsifier already in the plan: REM-31's exit (`_part3.md:201`). Source: "for a player character the player IS the decision procedure" (`architecture/meta/04_CODE_ARCHITECTURE.md:853`).
  - Subsystem cards (:50-61): per-subsystem gap - dice `p_success` 10-17 points wrong at small pools (R-F11); personal combat attacker takes no band (CP-T03-00, B10-09); mass battle 0 fields fought at seeds 0-2, army is whoever lives at home (`sides.py:115`); Proceedings verdict "reads nothing: pool 2 vs Ob 2 for every party (VT:384)" (corrected in 07d); fieldwork `finding.none` goes to nobody including the actor (FW-C:21); threadwork oracle not called by the loop, a practitioner's first season is empty (TW-T:87-88); settlements - yield has no labour term and `body_step` 0 so hunger hurts no body (08 G1, G3); factions - no succession (IN-61 stopped on H-230; 7 seats can never refill, R-F1); world - distance is free, map has no reader (WT-C A).
  - Taxonomy (:92-98): player-available = the seated person's `opening_set` (41/56 eligible unseated, 56/56 for the King); delegable = through a `binding_decision` edge (`dispatch`, `issue`, `confer`, `oblige`); engine-only. "No verb exists only for the player"; of 128 lexicon names, 52 have a row.
  - Seat-holders die by `fight` early (aperture seed 0: 3 deaths, 2 seat-holders) so the first big choice is a vacancy, needing IN-61 (:68); directive 8: draw one authored opening Tension per game as world-gen content (:69).
  - Top 8 gaps (:79-88): no seat; no odds (`band_odds`/`odds_of`, B10-08); menu names verbs not consequences (render each row's `requires`, `writes` by degree, `emits_on_refusal` as its card); only the top question is seen (`first`) (CP-T02-07); silent nothing (`choose.py:435-436, :481`) - add a read-only drop-reason trace in `opening_set`, deposit `finding.none` to the actor; no stake/end; acts cost the actor nothing (H-205, CP-T03-00 first); no season account (ledger delta is the log).
  - Escalations (:108-111): E1 true odds vs held arithmetic - AX-7 "No state is hidden from the player" (`01_AXIOMS.md:301`) vs `04:858` "the ARITHMETIC of what the character already holds"; v10 took true odds (CP-T01-03 mode (a)); recommends true band odds and narrowing 04's clause to world facts; E2 whether the player commands a battle after contact (K-MB-4, J-C-31).
- **Conflicts / stale:** the "verdict reads nobody" and "UI v4 jumps Part 9 -> 21" statements (:25, :56) are corrected in 07d. 41/56 unseated figure matches thrust-layer P9 (`probes/p9...:83`).
- **Open items:** the two escalations.
