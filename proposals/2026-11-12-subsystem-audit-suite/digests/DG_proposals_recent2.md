# Digest proposals_recent2

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: proposals dated 2026-09-20 or later, second half (100 assigned entries, 2026-10-21 through 2026-10-25 families: verb-key-rows, system-description, subsystem-completion, character layers, master-workplan-v10 build files, thrust-layer).
**Reading-depth note (honest):** the assignment is about 3.2 MB (~30,000 lines), more than one session can hold. Each entry begins with a depth tag: `[READ IN FULL]`, `[READ PARTLY: what was and was not opened]`, or `[HEADINGS+HEAD ONLY: ...]`. Nothing is summarised from memory; `:line` references were opened. Where a tag says partly, claims about the unread remainder are marked `[UNVERIFIED]` or omitted.
Ratification summary for this lane: nothing in these files is RATIFIED by its own Status line. Every proposal file is PROPOSED / HELD BACK; the master-workplan-v10 build files are "instructions under the adopted plan" (the plan itself was adopted, ED-IN-0299 / ED-IN-0301 cited inside the files); the system-description suite is PROPOSED (reference).

### proposals/2026-10-25-thrust-layer/00_THRUST_LAYER_DESIGN.md
- **What it is:** [READ IN FULL] Design (v2, 2026-10-25, one adversarial round) for a "thrust layer" in `engine/season/`: authored typed LADDERS of stage predicates under an ambition, plus closure engines, constraints on death and a standing gate. Producer + opus critic.
- **Status:** "PROPOSED — HELD BACK IN FULL (v2). PARTLY RULED since" (:3): the v10 plan folds it in as `CL-THRUST` (`workplans/valoria_master_workplan_v10_part12.md`); M20/M21 (ED-IN-0301, `v10_part6.md`) exclude R3' and the stage `deadline`, strike `closing`, `successor`, `deal`, and cut the `Slain` band and B5.1; B4.x, B5.2, B6.n held. Reading: partly superseded/live-in-plan; line numbers cited inside it have drifted (:5).
- **Bears on:** CHAR, CORE, WR, FA, PC, SC.
- **Content that matters:**
  - Thrust = an existing `commit` tenure to an OUGHT Proposition (`world_q.ambitions`); ladder = authored data; "current stage" is a query over the person's OWN ledger (person-side, AX-2), never a stored counter (:8-21, :40, :172, :194-197). Closed roster `thrust_axes` (ten axes plus opposite poles) in `rosters.yaml`, new `axis:` / `ladders:` keys on `goals.yaml` through the one loader `data/goals.py` (:107-142).
  - ARC predicate (:48-56): an act formed from a `need` question about the thrust, with a self-effect and a world-effect Receipt linked by `causes[]`. v1 was met by WITNESS bookkeeping (`witness.py:654-657` + `world.py:1306-1322`); v2 restricts to `arc_effect_fields` rosters, driver-side reading; the filter is itself flagged as insufficient because MATTER rewrites `Person.body`, `Rung.stores`, `Site.condition` every season (:65). Built reader `harness/arc.py` states the same limit.
  - R3' (promote a `need` question to tier 0 for one season per `deadline`, keyed-draw phase) replaces a standing promotion because unconditional tier-0 starved news (events 21,735 to 15,738; `news.told` 14 to 7, `world_q.py:2608-2612`) (:174-182, :213-230). Falsifier: `news.told` falls beyond seed spread.
  - Closure only by lawful forms: threshold-raised docket matter (a MATTER step on `_standing_crossings`' shape that writes nothing), bound peace via `covenant` + a NEW `(verb, referent)` decline reader, succession belongs to IN-61 (RULED RS-27: heir is a title, still has to claim), authored set piece via `arrangements.yaml` (:245-261).
  - Death is rare: `Felled` currently deletes (`verb_table.yaml:716,:802`); proposal splits `Felled`=down-alive from a new `Slain` band (:267-280; later CUT by M20/M21). Standing gate: `admits_audience` reaches only 3 of 31 seats (`cohorts.yaml:127-130`), so G1-G3 would seat guards for every seat that is a -1 `seat_holders` referent and add an `audience` conjunct to `fight/challenge/accept` (:282-307).
  - Per-axis ladder buildability (:332-418): axis J (heal Calamity) unbuildable (threadwork "built and inert"); caste has no store (D3: a Query over affiliation convictions); `construe` is `grade: absent` and not a weapon; 13 of 56 verbs write nothing (:89-90).
- **Conflicts / stale:** Cited line numbers in `queries/world_q.py` drifted (:5). The measured figures (51/803 need; 929/1,318 refused) are SUPERSEDED inside by `01_MISSING_IN_CODE.md` P1/P2/P10. Cites retired `valoria_master_workplan_v9*.md`. The toy-world results (:513) are post hoc with informed predictions.
- **Open items:** D1 (is a beaten fighter ever killed; where the `Slain` edge sits; later cut), D4 (line between licensed "sequence" and unlicensed "entire arc", Jordan 2026-08-18) (:496-497); `WoundTracker` separating down from dead is [ASSUMPTION]; G2's `audience` reader widening and R1's `subject := referent` binding are Layer-1 questions (:462-467).

### proposals/2026-10-25-thrust-layer/01_MISSING_IN_CODE.md
- **What it is:** [READ IN FULL] Gap register (29 rows G-01..G-29) beneath the thrust layer, built from probes P1-P12 run on `build_realm` seeds 0-4; v2 after one antagonist pass.
- **Status:** "PROPOSED — HELD BACK IN FULL; its gaps are folded into the v10 plan as `CL-THRUST`" (:5). Grades are as of 2026-10-25; B10-02 (#509) later landed instruments for G-02, G-08, G-11, G-12, G-20, G-27-G-29, so those rows need re-reading. Reading: reference; live as a measurement record.
- **Bears on:** CORE, CHAR, FA, PC, WR, SC, FI.
- **Content that matters:**
  - Headline measurement: 76.2% (2 seasons) / 76.8% (4 seasons) of 7,402 / 16,116 attempted acts are REFUSED on the driver's definition (`loop/driver.py:489-505`); 73.8-73.9% with graded losses excluded (:37, :76). 28.7-32.2% are refused at admission because the subject lives in another collection (wrong-kind formation) (:47, :74).
  - Closers barely execute at 4 seasons (exe/att): determine 3/43, confer 10/111, covenant 0/70, revoke 0/32, commit 8/564, restore 0/250, tend 0/302, build 0/230, found 1/208, work 3/726; `arrest` never forms; `succeed` not in `resolvable_verbs()` (:37, :77-80). `build/found/work` cannot execute in computed play at all (ED-IN-0297: a computed act "always mints `text`") (:78).
  - Deaths: 20 in 5 seeds x 4 seasons, 16 seat-holders, 11 by `accept`, 9 by `fight`; 0 of 11 `accept` deaths had a challenge from the other party (P4, P11b); no `person.died`/`tenure.closed` claim ever names the dead holder's seat (H-206, H-209) (:41, :48, :103-106).
  - H-156 (decline wrong-kind formation vs accept the tax) is the register's largest OPEN ruling and "survives all five steps"; only H-156's options (a) `withheld_verbs`, (b) more classed sources, (c) person-side known-false test survive; the v1 rule is withdrawn for six reasons (:74, :177, :182).
  - Of 38 `goals.yaml` rows only 12 mint a Proposition in the shipped realm; no seat-attached goal binds anyone; `need` scenes 24-28% of scenes, about a goal only 7.1-8.5% (:38, :87-89).
  - Executable terminus exists and TL misses it: `world_q.endings_reached` over `rosters.yaml: endings`, reported once per season (:97, :153); suggested key name `goal_stages` because `ladders` names two other things (:96).
- **Conflicts / stale:** G-02: a contested act refused at admission never enters `SeasonDriver.resolved`, so aperture's attempted count (1,182) differs from the driver's (1,511) (:75). Four readers classify "refused" differently (G-03, :76). `age_at_build` is not sweepable on a built world (G-22, :120). `storybar`/`chronicle` count refused acts as story: 30.4% cross-person as read vs 17.9% executed-on-executed (G-27, :135). Row grades older than B10-02.
- **Open items:** H-156 ruling; H-240 route for PC-10b (`accept` with no challenge); ED-IN-0297 (where a works comes from); share of delivered questions fed by a refusal-kind claim not measured (:186, :210); player seat bypasses `opening_set` (O1, :186).

### proposals/2026-10-25-thrust-layer/02_MAJOR_TAKEAWAYS.md
- **What it is:** [READ PARTLY: lines 1-120, 149-400 opened; §4 second half (lines 120-148) not opened] Expansion of eight session takeaways (T1-T8) with evidence tags [engine]/[toy]/[critic], corrections table and a "needs Jordan" list.
- **Status:** "PROPOSED — HELD BACK IN FULL" (:3). Currency note (:5-8): folded into v10 as `CL-THRUST`; M19/M20/M21 and ED-IN-0301 decided H-156, D4, D1 since (:386). Reading: reference; derivative of 00 and 01.
- **Bears on:** CORE, CHAR, PC, WR, FA.
- **Content that matters:**
  - The decided-since list (:386): H-156 = M19(a) (`v10_part11.md:13`); D1 = M21(a), no `Slain` band (`v10_part6.md:181`); D4 = M20 narrowed (`v10_part6.md:172`); PC-10b/H-240 = route (1) (`v10_part3.md:192`); ED-IN-0297 closed by a superseding row (`editorial_ledger_in.jsonl:81`). An audit must read those rows, not the open-looking text above them.
  - Toy table (:154-167): arc-minus-null for ladder + decisive-form set piece + bound peace = +0.244 [+0.188, +0.303] (0.24 deaths/run); same set piece without ladder +0.016; ladder + tribunal under constraints +0.010; bottom-up -0.056. Unconstrained ladder+tribunal was +0.09; "does not transfer under the constraints".
  - T5 "do not build" (:249-283): lookahead-biased choice costs ~270x run time and cuts explained motive 0.58 to 0.29; a blind script violated world constraints 96% of runs; a forcing director dictates a death in 99% of arc-passing runs. Any sigma-leverage correlate would live at the choice stage in tau units of `choice_temperature`, soft-capped (:271-274).
  - T6/T7 (:287-330): 0 threadwork modules load in a season; 29 of 46 registry rows have `age: null` (H-208); all 46 NPC `ends_when` are prose; every axis has a non-lethal closing act in existing verbs.
  - Corrections table (:357-369): 929/1,318 refused → 76.2%; 33% wrong-kind → 28.7-32.2%; "51 of 803 need" not reproduced; the claim H-156 "sits in no workplan" was wrong.
  - Excludes: human legibility testing; player character (bypasses `opening_set`); share of questions fed by refusal-kind claims (:371-382).
- **Conflicts / stale:** the exile-vs-settlement toy comparison was run inline and not saved [UNVERIFIED] (:172-173, :368). Primary literature (Compton, Ryan, Façade, Riedl) read via repo research files only (:377).
- **Open items:** human-reader test of narrative quality; refusal-kind-claim share; exile arm.

### proposals/2026-10-25-thrust-layer/probes/p10_clean_remeasure.py
- **What it is:** [READ PARTLY: docstring and imports, lines 1-22 of 192] Scratch probe (P10) re-taking wrong-kind refusal per act, graded-loss share and `_admits` double calls; orchestrator, v2, 2026-10-25.
- **Status:** no Status line (script). Reading: historical measurement instrument, not wired into CI; hard-codes `sys.path.insert(0, "/home/user/ttrpg")` and wraps driver-instance methods.
- **Bears on:** CORE, CHAR.
- **Content that matters:**
  - Classifies refusals into collection_mismatch / subkind_mismatch / subkind_wrong_coll / world_read_docket / absent_subject (:3-12); graded loss = every refusal-kind Event degree Failure AND kind also in the row's `emits` (:13-15).
  - Output saved as `p10_out.json` and `p10_s4.txt`; reads `engine/season` owners (`SeasonDriver`, `build_realm`, `loop.resolve._admits`) by import, so it breaks if those are renamed.
- **Conflicts / stale:** Reproduces P1 totals exactly per `01` §2; Line refs it uses into `loop/resolve.py` have drifted since (the design says so for `world_q.py`).
- **Open items:** none stated.

### proposals/2026-10-25-thrust-layer/probes/p10_out.json
- **What it is:** [READ IN FULL] Saved output of P10: counters at 2 and 4 seasons, seeds 0-4 pooled.
- **Status:** data file. Reading: historical record of one run.
- **Bears on:** CORE.
- **Content that matters:**
  - s2: attempted 7,402; refused 5,639; executed 1,763; wrongkind_collection 2,385; graded_loss 175; refused_kind_also_in_emits 1,299 (:1-17).
  - s4: attempted 16,116; refused 12,372; executed 3,744; wrongkind_collection 4,620; graded_loss 469; subkind_mismatch 174; world_read_docket 216 (:18-34).
  - Internal check: 4,063 + 557 = 4,620 (collection_mismatch + subkind_wrong_coll), matching `01` G-01.
- **Conflicts / stale:** `wrongkind_any` (2,442 / 4,794) is a third figure the prose never quotes.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p11b_accept_challenge.py
- **What it is:** [READ PARTLY: docstring, lines 1-22 of 82] Probe P11b: for each death whose cause is an `accept`, whether a `challenge.issued` Event or ledger claim stood behind it.
- **Status:** script. Reading: historical.
- **Bears on:** PC, CORE.
- **Content that matters:**
  - Measures `issued_by_subject`, `issued_either`, `ledger_claim` per accept-death, plus supply of `challenge.issued` per seed (:1-10).
  - Result per `01` G-15: 0 of 11 accept-deaths had a challenge from the other party; 4 of 11 ledgers hold some challenge claim.
- **Conflicts / stale:** its usage line names `p11_accept_challenge.py` (the superseded name), not the file's own name (:11).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p12_fallback_kinds.py
- **What it is:** [READ PARTLY: lines 1-22 of 42] Probe P12: acts whose only Events are the fallback kinds `act.ineligible`/`act.refused`.
- **Status:** script. Reading: historical.
- **Bears on:** CORE.
- **Content that matters:**
  - Checks `FALL & set(REFUSAL_KINDS)` (empty per `01`): fallback kinds sit in no row's `emits_on_refusal`, so such acts count as EXECUTED (:3-4, :14-16); 6 of 681 executed acts (0.9%) at seeds 0-1.
- **Conflicts / stale:** none noted.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p1_out_s2.json
- **What it is:** [READ PARTLY: head 1.2 KB of 5.4 KB for the sibling seed0 file; this file's per-verb table opened only via `01` §3] Saved P1 output, 2 seasons x seeds 0-4, pooled per verb.
- **Status:** data file. Reading: historical.
- **Bears on:** CORE.
- **Content that matters:**
  - Per-verb attempted/executed/refused with refusal-kind keys (`rk:accept.refused` etc.); pooled totals reproduce `01` §3 (7,402 / 1,763 / 5,639).
- **Conflicts / stale:** `[UNVERIFIED]` against the file itself beyond the head; figures taken from `01`.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p1_out_s2_seed0.json
- **What it is:** [READ PARTLY: first ~1.2 KB of 4.2 KB] Saved P1 output, seed 0, 2 seasons.
- **Status:** data file. Reading: historical; a hash-stamped control.
- **Bears on:** CORE.
- **Content that matters:**
  - seed 0: log_len 21,710; hash `5301d6b62af614f4`; persons 80; attempted 1,511; executed 335; refused 1,176; null 0 (head). The 1,511 vs aperture's 1,182 is the G-02 gap.
  - accept 48 attempted / 44 refused / 4 executed; commit 64 / 63 refused; covenant 14 / 14 refused; determine 6 / 6 refused (head).
- **Conflicts / stale:** none. Note: this hash is the content hash of a 2026-10-25 tree; the engine has moved (B10-xx), so it will not reproduce today [UNVERIFIED].
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p1_out_s4.json
- **What it is:** [NOT OPENED beyond `01`'s account: SKIPPED body] Saved P1 output, 4 seasons x seeds 0-4.
- **Status:** data file. Reading: historical.
- **Bears on:** CORE.
- **Content that matters:**
  - [SKIPPED: /home/user/ttrpg/proposals/2026-10-25-thrust-layer/probes/p1_out_s4.json body — a 5.6 KB data table duplicating `01` §3; the pooled 4-season totals (16,116 / 3,744 / 12,372) are cited from `p10_out.json` instead]
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p1_refusal_census.py
- **What it is:** [READ PARTLY: docstring and imports, lines 1-22 of 115] Probe P1: per-verb attempted/executed/refused/null census copying `loop/driver.py:489-505`.
- **Status:** script. Reading: historical, but it IS the pattern later landed as `harness/aperture.py`'s pooled block (B10-02).
- **Bears on:** CORE.
- **Content that matters:**
  - Wraps `SeasonDriver.resolve` and `.encounter` on the instance, composition copied from `harness/storybar.py::drive` (:3-5); usage via `PYTHONHASHSEED=0 python3 probes/p1_refusal_census.py SEASONS SEED...` (:10-11).
  - Imports `make_chooser`, `SeasonDriver`, `resolvable_verbs` (:20-22) — three engine seams.
- **Conflicts / stale:** docstring says "run as ... python3 probes/..." but file hard-codes the absolute repo path.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p2_goals_and_need.py
- **What it is:** [READ PARTLY: lines 1-22 of 66] Probe P2: goals.yaml by object/org kind; what `seed_goals` minted; scene occasion source over a run.
- **Status:** script. Reading: historical.
- **Bears on:** CHAR, CORE, FA.
- **Content that matters:**
  - Reads `engine.season.data.goals` (`G.goals()`), `harness.populated.build_realm`, `queries.world_q` (:10-16); reports occasion source of every Scene via the Scene's `occasion` (:2-4).
  - Result per `01`: 38 rows (24 orientation / 6 seat_holders / 4 rung / 4 deed_doers); only 12 mint a Proposition in the shipped realm.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p3_refusal_reasons.py
- **What it is:** [READ PARTLY: lines 1-22 of 68] Probe P3: wraps `loop/resolve.py::_admits` to record why closer verbs refuse.
- **Status:** script. Reading: historical.
- **Bears on:** CORE, FA, SC.
- **Content that matters:**
  - CLOSERS list of 23 verbs (:20-22) including determine, confer, covenant, open_case, commit, release, oblige, revoke, arrest, issue, petition, found, build, work, give, restore, tend, migrate, research, examine, fight, accept, challenge.
  - Finding: no closer refusal is an eligibility refusal; refusals are precondition refusals on wrong-kind subjects (`01` §2 P3).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p3b_kind_mismatch.py
- **What it is:** [READ PARTLY: lines 1-22 of 83] Probe P3b: kind mismatch across all verbs; refusals after admission.
- **Status:** script. Reading: SUPERSEDED by P10 (own v2 account, `01` §2 P3b): its 7,737 counted `_admits` CALLS, not acts, and mis-classed Record sub-kinds and DocketItem.
- **Bears on:** CORE.
- **Content that matters:**
  - Still-valid output: 0 ineligible refusals; admitted-then-refused leaders migrate 705, transfer 136, move 112, forge 90, surveil 89, raze 84, survey 70, tell 65 (`01` P3b).
- **Conflicts / stale:** the 33.1% headline is withdrawn.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p4_killing_consequence.py
- **What it is:** [READ PARTLY: docstring, lines 1-22 of 83] Probe P4: what a death does in computed play (seats held, killer act, claims, later occasions).
- **Status:** script. Reading: historical.
- **Bears on:** PC, CORE, WR.
- **Content that matters:**
  - For each removed person: seats at start of season, claims naming him by predicate, claims naming his seats at/after death (H-206), later occasions naming killer AND about a claim on the dead (H-209) (:3-10).
  - Result: 20 deaths, 16 seat-holders, `accept` 11, `fight` 9; 0 `person.died`/`tenure.closed` seat claims; 0 later killer-about-dead occasions.
- **Conflicts / stale:** matches claims against end-of-run ledgers, so an evicted claim would be missed (R14 "could not verify").
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p5_exogenous_switches.py
- **What it is:** [READ PARTLY: lines 1-22 of 52] Probe P5: each dark exogenous switch set to its own fixture comment's sweep value, seed 0, 2 seasons.
- **Status:** script. Reading: historical.
- **Bears on:** WR, CORE, CHAR.
- **Content that matters:**
  - Arms: control, `body_step=10`, `age_step=0.01`, `illness_rate=0.05` and others (:19-22). Results per `01`: `body_step`/`illness_rate`/`season_factor_draw`/`lattice_coupling` move the hash; `age_step=0.01` and `age_at_build=160` do NOT (ages 0-1; `Person.born` fixed at construction).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p6_case_termini.py
- **What it is:** [READ PARTLY: lines 1-22 of 58] Probe P6: classifies the 46 NPC cases' `ends_when` strings by lexical markers via `harness/run_cases.load_cases("NPC")`.
- **Status:** script. Reading: historical; `01` itself says its strict-regex 28 "is a fit to the strings, not a measurement".
- **Bears on:** CHAR, ARCS.
- **Content that matters:**
  - NEVER and PRESUMED regexes (:18-21); cross-reads `engine/season/ENDINGS_CLASSIFIED.yaml` (an agent's prose classification).
  - Count: 40 of 46 by the extractor's own marker; 28 by the strict regex.
- **Conflicts / stale:** uses `python3 -I` in usage (:9) yet imports via `sys.path.insert`; fine.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p7_chain_refusals.py
- **What it is:** [READ PARTLY: lines 1-22 of 51] Probe P7: do `storybar`/`chronicle` count refused acts as story.
- **Status:** script. Reading: historical.
- **Bears on:** CORE, WR.
- **Content that matters:**
  - Runs `storybar.drive`, reads `storybar.read` + `chronicle.deepest_chain`, classifies by the driver's rule; recomputes cross-person share with refused antecedents removed (:1-9). Result: 55 of 66 deepest-chain acts refused; cross-person 30.4% as read vs 17.9% executed-on-executed.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p8_thread_import.py
- **What it is:** [READ IN FULL, 17 lines] Probe P8: lists `sys.modules` with "thread" after one season and verb rows/event kinds naming thread/lattice/Calamity.
- **Status:** script. Reading: historical; the strongest single execution-evidence that threadwork is not in the season loop.
- **Bears on:** WR, CORE.
- **Content that matters:**
  - Result per `01`: 0 threadwork modules loaded; one verb row (`thread_read`); 0 thread/lattice/Calamity event kinds; log 7,018 events (:6-17).
- **Conflicts / stale:** it is a snapshot (2026-10-25); a later B10 position could have wired threadwork [UNVERIFIED].
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/reports/R01_partial_top_down.md
- **What it is:** [READ IN FULL] Chat report: is pure bottom-up emergence a problem; can partial top-down guides help (with the oatmeal-problem literature).
- **Status:** "REFERENCE — HELD BACK IN FULL"; figures predate the register's probes (:5).
- **Bears on:** WR, CHAR, CORE.
- **Content that matters:**
  - Verdict: partial top-down in three places only: standing motives held by actors, selection of what the player is shown, a narrow declinable occasion channel; every state change stays bottom-up.
  - `goals.yaml` already has referents/attention-only shape (`goals.yaml:9-12`) but no lifecycle field; offices: `remit_acts` is a licence not an obligation, 2 of 38 goal rows attach to a seat; cohorts carry no wants (`cohorts.yaml:18-23`).
  - Keeps refusal of need-triggered outcome injection even with Jordan's permission to overrule: a threshold that acts is an actor; an injected beat cannot be contested; storybar would measure its own injections.
- **Conflicts / stale:** 929/1,318, 51/803, 33% figures superseded (`02` §9).
- **Open items:** [GAP] primary literature not re-fetched; human-reader ablation of the recognition layer not run.

### proposals/2026-10-25-thrust-layer/reports/R02_arcs_deconstruction_and_logic_tests.md
- **What it is:** [READ IN FULL] Chat report: seven ways the corpus achieves arcs; toy logic tests of BU/TD/TDR/HY.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** ARCS, WR, CHAR.
- **Content that matters:**
  - Seven arc engines: accrual, exposure, succession, decision point, contest, conjunction, held control state; closes by decider 20/50, crossing-forced 19/50, never 10/50, roll 9/50, threshold 8/50.
  - Hand classification of the 46 NPC cases by `ends_when`: forks 11, exit-only 7, presumed 12, nothing authored 16 (names ids) — one reader, since superseded in count by P6.
  - "~13 shapes" figure comes from 24 of 138 arcs; the calibration set was evacuated.
- **Conflicts / stale:** "the corpus is top-down by origin" — every arc is an authored predicate (Jordan 2026-08-18).
- **Open items:** spirals (ARC-05) not visible to the three-act test.

### proposals/2026-10-25-thrust-layer/reports/R03_sigma_leverage_correlate.md
- **What it is:** [READ IN FULL] Chat report: is there a sigma-leverage correlate for the likelihood of subsequent events.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** DICE, CHAR, WR.
- **Content that matters:**
  - Yes in form: `decision/choose.py::_sample_order` orders by `softmax(score/tau)`, `choice_temperature = 0.1`; a narrative term would be expressed in tau units, soft-capped like `sigma_leverage.py`'s `soft_cap`, on the choice stage, never the dice resolution, never removing an option.
  - Toy table: ladder+tribunal arc-minus-null +0.09 [+0.04, +0.15]; lookahead strength 4 = -0.08 [-0.14, -0.01], ~270x run time; explained motive 0.58 → 0.29.
  - It would override v2 narrative-engine rules R-AI and F8 (F8 would become a dosimeter).
- **Conflicts / stale:** toy only.
- **Open items:** two-level lookahead, human judgement of "construable".

### proposals/2026-10-25-thrust-layer/reports/R04_ladder_tribunal_best.md
- **What it is:** [READ IN FULL] Chat report: is ladder + threshold-raised tribunal the best.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** WR, CHAR.
- **Content that matters:**
  - "No": leads only on arc rate without outcome-writing; ordering signal depends on threshold (holds at 4.5-10, weak at 3, gone at 16); closure is one template (192 of 293 runs close on a tribunal ruling); thread continuity lowest of six arms (0.58).
  - Ladder alone: multiplies cross-person chain depth ~2.7x (62.5 vs 23.0) and keeps legibility 0.72.
- **Conflicts / stale:** the threshold-sensitivity table was printed, not saved.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/reports/R05_scripted_director_set_pieces.md
- **What it is:** [READ IN FULL] Chat report: a director that injects set pieces rather than outcomes.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** WR, SC, PC.
- **Content that matters:**
  - Situation-only set piece fizzles (ordering -0.04); decisive-form set piece (best-of contest, lethal climax) +0.14; ladder + decisive form +0.20; at 80% refusal the decisive-form arm holds 0.81 but "likely an artifact" because the toy contest bypasses the act layer.
  - Trade: "dictated outcome for dictated form and stakes" — an authored occasion that is not declinable.
- **Conflicts / stale:** cites `regimes7.py`, which is in `toy/` but not in this lane's assignment.
- **Open items:** declinable set pieces, mid-run stake adjustment untested.

### proposals/2026-10-25-thrust-layer/reports/R06_npc_deaths_clarification.md
- **What it is:** [READ IN FULL] Chat report: "94% end with both principals alive" does mean toy NPC deaths.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** WR, PC.
- **Content that matters:**
  - Decisive-form lethal arms kill one principal per run (principals dead 1.00); the ordering signal depends on that death (exile +0.01, pact +0.03, lethal +0.14) partly because the test requires a post-peak fall. Tribunal kills no one and keeps +0.09.
  - Corrects R05's headline: holds only for the lethal climax.
- **Conflicts / stale:** the non-lethal run was printed not saved; code `regimes8.py` (not in assignment).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/reports/R07_arcs_without_deaths.md
- **What it is:** [READ IN FULL] Chat report: arcs without NPC death; death rare, fighting authority hard, killing consequential.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** PC, WR, FA.
- **Content that matters:**
  - Prior arc-passing runs closed on a death in 99% (forcing director), 94% (lethal set piece), 98% (ladder + lethal), 3% (ladder + tribunal); 19-36% of harm events hit a prize holder.
  - Constrained-world table (:20-30); killing consequence package: kin grievance, witnesses turn, forfeiture, infamy, vacated holdings → ~9.5 acts by ~4.9 actors, ~1.3 tribunals, no runaway feud.
  - Real engine: `fight` needs only existence and co-location; `Felled` deletes the person; the "deontological gate" the row mentions does not exist.
- **Conflicts / stale:** `regimes10.py` + `exp_con_out.txt` saved; review table and killing-at-season-10 printed only.
- **Open items:** trial, succession politics, longer feud unbuilt.

### proposals/2026-10-25-thrust-layer/reports/R08_ten_axes.md
- **What it is:** [READ IN FULL] Chat report: the user's ten goal axes mapped to `goals.yaml` rows, existing verbs and gaps; the arc criterion as a test.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** CHAR, FA, WR, ARCS.
- **Content that matters:**
  - Ten axes list and per-axis table (:25-36): rows today, verb ladders, gap. Tension already authored for four (1 vs 10, 5 vs Kommerkiarios, 2 vs Varfell thread-truth, 3 vs Church orthodoxy); missing poles block caste (4) and healing (9).
  - Arc criterion: one actor's goal-driven chain with a self effect and a world effect, linked by `causes[]` — the form later made the `ARC(p, a)` predicate.
  - Says at least nine verbs write nothing (later corrected to thirteen by R12).
- **Conflicts / stale:** "nine verbs" superseded by thirteen (R12).
- **Open items:** the 46 character cases not mapped onto the axes.

### proposals/2026-10-25-thrust-layer/reports/R09_design_verdict.md
- **What it is:** [READ IN FULL] Chat verdict after the design relay (thrust layer designable, not buildable yet).
- **Status:** "REFERENCE — HELD BACK IN FULL"; carries a recorded correction that "sits in no workplan" is wrong (H-156).
- **Bears on:** CHAR, CORE, WR.
- **Content that matters:** one-page summary of design v2; four critic breaks (vacuous arc test, succession duplicate of IN-61, gate protecting 3 of 31 seats, R3 synchrony); asks Jordan D1 and D4.
- **Conflicts / stale:** cites `toy/thrust_layer_design_v2.md` (the design now lives one directory up).
- **Open items:** D1, D4 (since decided M21, M20).

### proposals/2026-10-25-thrust-layer/reports/R10_major_takeaways_as_first_delivered.md
- **What it is:** [READ IN FULL] The eight takeaways as first delivered in chat.
- **Status:** "REFERENCE — HELD BACK IN FULL"; superseded by `02_MAJOR_TAKEAWAYS.md` (:7).
- **Bears on:** CORE, CHAR, WR.
- **Content that matters:** same eight takeaways with first-delivery figures (929/1,318; 51/803; 28 of 46); says design item 1 "is the gate on all of them".
- **Conflicts / stale:** first-delivery figures wrong, see `02` §9.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/reports/R11_register_verdict.md
- **What it is:** [READ IN FULL] Chat verdict on the gap register after the relay.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** CORE, PC.
- **Content that matters:** G-01 design withdrawn (passed over open ruling H-156); P3b's 33.1% was calls not acts; G-16 re-owned to PC-10b; `endings_reached` added; stopped after one round per CLAUDE.md §0.
- **Conflicts / stale:** none beyond what 01 §7 records.
- **Open items:** share of questions fed by refusal-kind claims; player seat.

### proposals/2026-10-25-thrust-layer/reports/R12_design_producer_receipt.md
- **What it is:** [READ PARTLY: lines 1-66 of 113; the verbatim brief (:67-113) not opened] Design producer's hand-back for v1.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** CORE, CHAR, PC.
- **Content that matters:**
  - Corrections to the brief: thirteen verbs write nothing (adds `dispatch`, `challenge`, `evade / defy`, `speak`); `construe` is `grade: absent`; `offices.yaml` has 31 seats (16 null revoker / 13 same-faction / 2 in-holdings; header "14 of 29" stale); orientation rows mint no Proposition (:15-26).
  - `succeed`, `tie`, `knot` have no opener (`rosters.yaml:141-143`); ED-IN-0225 is cited in four `.py` files, not three.
  - Cheapest sinking test: count executed determine/confer/covenant/open_case over several seeds (:63).
- **Conflicts / stale:** v1 file not committed.
- **Open items:** the unverified list (:56-62).

### proposals/2026-10-25-thrust-layer/reports/R13_design_critic_report.md
- **What it is:** [READ PARTLY: lines 7-74 of 100; the verbatim brief (:75-100) not opened] Critic's report on design v1: findings F1-F16 with evidence.
- **Status:** "REFERENCE — HELD BACK IN FULL"; dispositions are in `00` final section.
- **Bears on:** CORE, CHAR, FA.
- **Content that matters:**
  - F1 BLOCKER: ARC clause (3) vacuous via `witness.py:654-657` + `world.py:1306-1322`; F2 BLOCKER: §4.3 chose the rejected succession carrier; F3 BLOCKER: gate reaches 3 of 31 seats; F6: `of: referent` unspellable, builder exits `SystemExit` (`data/requires.py:973-978`).
  - Confirmed true: 22 of 29 loop-built seats keep `dispatch`; 31 seats, 16/13/2 revocation split; conferral 6 null / 8 elected / 17 appointed (:62-64).
- **Conflicts / stale:** critic could not run code.
- **Open items:** none left (all accepted).

### proposals/2026-10-25-thrust-layer/reports/R14_register_producer_receipt.md
- **What it is:** [READ PARTLY: lines 44-70 of 106; head 1-43 and the verbatim brief not opened] Register producer's hand-back for v1.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** CORE, PC.
- **Content that matters:** findings outside the brief: G-02, G-03, G-27, G-16 (non-lethal duel already exists, unwired), G-15; `REFUSAL_KINDS` is at `data/verbs.py:1403` not `:1073`; could not verify why `arrest` never forms, whether `survey` mints a works record.
- **Conflicts / stale:** its S12 answer (IN-53 precedent) was overturned by the critic.
- **Open items:** its two escalations (fight_terms default, H-240) — the first withdrawn.

### proposals/2026-10-25-thrust-layer/reports/R15_register_critic_report.md
- **What it is:** [READ PARTLY: lines 7-64 of 89; the verbatim brief not opened] Register critic's report, findings A1-A14, O1.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** CORE, PC, FA.
- **Content that matters:** A1 BLOCKER G-01 passes over H-156; A2 BLOCKER rule unsound; A10 `world_q.endings_reached` missed (`world_q.py:1990-2024` at the time); lists six NEEDS-RUN probes (graded-loss share, clean P3b, refusal-fed questions, clause-4 decay, accept deaths, G-03 hash move) and what holds (P1 capture, hashes, P4 counts).
- **Conflicts / stale:** 12 of 46 citations failed in v1.
- **Open items:** refusal-fed-question share still unrun.

### proposals/2026-10-25-thrust-layer/reports/README.md
- **What it is:** [READ IN FULL] Index of R01-R15 with reproduction rules and a known-errors pointer.
- **Status:** "REFERENCE — PROPOSED, HELD BACK IN FULL"; R12-R15 kept under CLAUDE.md §0's terminal-verdict exception, "delete them if the exception becomes the general case" (:5-10).
- **Bears on:** PROCESS.
- **Content that matters:** R09 and R10 error (H-156 "unruled") and superseded refusal figures (:50-56); path rewrites only (:41-47).
- **Conflicts / stale:** R01-R11 are chat transcripts under `proposals/` — a candidate for deletion by the repo's own rule if the exception widens.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/README.md
- **What it is:** [READ IN FULL] Module table for the toy world (24 actors, 6 places, 6 prizes, 24 seasons) with pre-registration status.
- **Status:** "Grade: model-internal, low confidence. Reference ... Not game code, not read by any tool" (:3-4).
- **Bears on:** WR, PROCESS.
- **Content that matters:**
  - Only v1's predictions were blind; every later set is informed; HYc, HYd, bootstrap CIs, ladder, set-piece, constrained arms are post hoc (:30-38).
  - Checked 2026-10-28: prediction/experiment scripts match recorded hashes (13 of 17); `regimes.py`, `regimes2.py`, `regimes5.py`, `regimes10.py` do NOT match their freezes (:25-30) — the freezes cover predictions, not the world.
  - Several runs (`regimes8.py`, `regimes9.py`, review table, killing-at-season-10 cascade) printed not saved (:40-44). `real_engine_chronicles/` holds seeds 0,1,2,4,5 chronicles (:46-50).
- **Conflicts / stale:** README says `regimes.py` = `regimes_v1.py` byte-identical — verified by `cmp` (identical); `predictions.py` = `predictions_v1.py` also identical.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_closure.py
- **What it is:** [READ PARTLY: lines 1-16 of 25] Post-hoc experiment: threshold-forced, decider-closed moment (BU/TDR/HY/HYd) at base and 80% refusal, 300 seeds, bootstrap CIs. Imports `regimes3`.
- **Status:** script; labelled "POST-HOC, exploratory" (:1). Reading: historical; reference-only.
- **Bears on:** WR, PROCESS.
- **Content that matters:** the HYd arm (tribunal) experiment behind R02's 0.26 arc rate; output `exp_closure_out.txt`.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_con.py
- **What it is:** [READ PARTLY: lines 1-16 of 69] Constrained-world experiment: death_p=0.01, gate_p=0.9, accusation, truce, consequences; CON1 non-lethal and CON2 lethal. Imports `regimes10`.
- **Status:** script; "Predictions registered BEFORE the first run" (:2); see README on hash mismatch for `regimes10.py`.
- **Bears on:** PC, WR.
- **Content that matters:** constants `CON1`, `CON2` (:5-6) define the constrained-world parameters whose results the design quotes (+0.244 etc.).
- **Conflicts / stale:** world file's freeze hash does not match (README :25-30).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_contest.py
- **What it is:** [READ PARTLY: lines 1-16 of 66] Conclusive-form set piece experiment (best-of contest at a venue, lethal at climax); imports `regimes7` (not in this lane's list).
- **Status:** script; predictions frozen (`setpiece2_pred.sha`).
- **Bears on:** WR, PC, SC.
- **Content that matters:** arms BU, TDR, TDSc, TDScf, HYg3c, HYg3d at N=300 (:15).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_ladder.py
- **What it is:** [READ PARTLY: lines 1-16 of 52] Ladder experiment with pre-registered predictions H1-H7 (`ladder_pred.sha`); imports `regimes5`.
- **Status:** script; "Exploratory, post hoc to v2" (:2).
- **Bears on:** CHAR, WR.
- **Content that matters:** H1 ladder adds closure (>= +0.10); H2 depth dose; H4 ordering signal >= +0.05 (FALSIFIED per design); H5 motive preserved >= 0.70 (:5-14).
- **Conflicts / stale:** H1, H4, H7 falsified (4 of 7 held).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_setpiece.py
- **What it is:** [READ PARTLY: lines 1-16 of 79] Set-piece director writing a situation (relocation + engagement window + optional stake multiplier); imports `regimes6` (not in lane).
- **Status:** script; frozen (`setpiece_pred.sha`); post hoc to v2.
- **Bears on:** WR.
- **Content that matters:** arms BU, TDR, TDS, TDSm, HYg3d, HYg3s (:16).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/lb_more.py
- **What it is:** [READ PARTLY: lines 1-16 of 26] Lookahead leverage comparison, lam 0 vs 4, 120 seeds, multiprocessing Pool(4).
- **Status:** script. Reading: historical.
- **Bears on:** DICE, CHAR.
- **Content that matters:** produces `lb_more_out.txt` (the lookahead -0.08 result); uses `lookahead.simulate_lb`.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/lb_sweep.py
- **What it is:** [READ PARTLY: lines 1-16 of 23] Lookahead leverage sweep lam in (0,1,2,4), 40 seeds, Pool(3).
- **Status:** script. Reading: historical.
- **Bears on:** DICE, CHAR.
- **Content that matters:** the lam sweep behind `lb_sweep_out.txt`.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/lookahead.py
- **What it is:** [READ PARTLY: docstring, lines 1-16 of 155] Toy implementation of choice-level "narrative leverage" with rollouts.
- **Status:** script. Reading: historical.
- **Bears on:** DICE, CHAR.
- **Content that matters:**
  - Models the engine's `choose.py::_sample_order` (Plackett-Luce/Gumbel over candidates with keyed noise) and adds `lam * tau * soft_cap(z_c)` with z_c standardised over THAT actor's candidates — "the mu-shift-in-sigma-units idea of sigma_leverage.py" (:3-9). Only "relevant" actors (participants of the top-3 threads) are leveraged — the casting rule (:13).
- **Conflicts / stale:** a rejected design (T5): reference only.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/metrics2.py
- **What it is:** [READ PARTLY: lines 1-16 of 235] Metric library for the toy (event selection `select(ev, B=12, top=3)`, etc.). No docstring.
- **Status:** script. Reading: historical.
- **Bears on:** WR, PROCESS.
- **Content that matters:** defines `executed(ev)` as events with delta > 0, a thread and an int actor (:1-3).
- **Conflicts / stale:** not imported by files read in this lane (regimes* define their own `run_metrics`) [UNVERIFIED by grep].
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/posthoc.py
- **What it is:** [READ PARTLY: lines 1-16 of 43] Post-hoc analysis after v2: HYc arm, bootstrap CIs, director templating, sifting availability; imports `regimes2`.
- **Status:** script; "POST-HOC (exploratory, run after v2)" (:1).
- **Bears on:** WR.
- **Content that matters:** output `posthoc_out.txt`; the HYc ("fired ambitions simply end") change-nothing result.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/predictions.py
- **What it is:** [READ PARTLY: docstring, lines 1-16 of 160] Pre-registered v1 predictions (blind): conditions base/noent/engine(80% refusal)/small/null/pert.
- **Status:** script; byte-identical to `predictions_v1.py` (`cmp`).
- **Bears on:** PROCESS, WR.
- **Content that matters:** "the real engine refuses ~70-80% of acts" is embedded as a model parameter `refuse=0.8` (:5-6).
- **Conflicts / stale:** DOUBLED file: `predictions.py` and `predictions_v1.py` are the same bytes.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/predictions_v1.py
- **What it is:** [READ PARTLY: lines 1-16 of 160] Identical copy of `predictions.py` (verified `cmp`).
- **Status:** script. Reading: duplicate.
- **Bears on:** PROCESS.
- **Content that matters:** see `predictions.py`.
- **Conflicts / stale:** pure duplicate (README :8 names `predictions.py` = `predictions_v1.py`).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/predictions_v2.py
- **What it is:** [READ PARTLY: lines 1-16 of 112] v2 predictions registered after v1 results (L1 etc.).
- **Status:** script; "informed, not blind" (:1-3).
- **Bears on:** PROCESS, WR.
- **Content that matters:** L1 "apparent legibility does not discriminate: spread < 0.05".
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes.py
- **What it is:** [READ PARTLY: docstring, lines 1-16 of 599] v1 toy world: BU, TD, TDR, HY regimes; separate RNG streams (world / acts / ambition / director) so HY(w_amb=0, occasions off) hashes identical to BU as control.
- **Status:** script; byte-identical to `regimes_v1.py` (`cmp`). Reading: historical.
- **Bears on:** WR, PROCESS.
- **Content that matters:** the control idea (identical log hash when the feature is off) mirrors the repo's hash controls; the regime definitions (TD = blind script forcing a five-beat schedule; TDR = replan; HY = standing referent-bound ambitions + declinable occasion channel) (:3-14).
- **Conflicts / stale:** world-file freeze hash does not match (README).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes10.py
- **What it is:** [READ PARTLY: docstring, constants and function index; lines 1-60 and a `def` index of 1025] Final toy world: constrained world with rare death (`death_p`), standing gate (`gate_p`), accusation, bound peace (truce), killing consequences, `simulate(..., con=, killing_t=)` (:739).
- **Status:** script. Reading: historical; freeze hash mismatch (README).
- **Bears on:** PC, WR.
- **Content that matters:** W init defaults (:32-60): `death_p=0.25`, `gate_p=0.0`, `ladder_depth=3`, `deadline=6`, `cap=2`; metrics `arc_test` with `peak_hi=0.92` (:836); THETA=6.0 (:21).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes2.py
- **What it is:** [READ PARTLY: docstring, lines 1-16 of 649] v2 instrument: pair-thread identity, plateau peak, burn-in, director thread.
- **Status:** script. Reading: historical; freeze mismatch.
- **Bears on:** WR.
- **Content that matters:** same regime docstring as v1.
- **Conflicts / stale:** four near-identical copies of the same ~600-line world (regimes, 2, 3, 5, 10 differ by added features).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes3.py
- **What it is:** [READ PARTLY: lines 1-16 of 686] Adds terminal-lifecycle and threshold-raised tribunal arms.
- **Status:** script. Reading: historical.
- **Bears on:** WR.
- **Content that matters:** base for `exp_closure.py` and `lookahead.py`.
- **Conflicts / stale:** as above.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes5.py
- **What it is:** [READ PARTLY: lines 1-16 of 793] Adds goal ladders (HYg1-3) and ladder + tribunal.
- **Status:** script. Reading: historical; freeze mismatch.
- **Bears on:** CHAR, WR.
- **Content that matters:** base for `exp_ladder.py`.
- **Conflicts / stale:** as above.
- **Open items:** none.

### proposals/2026-10-24-character-layers-capability-ambition-values-personality.md
- **What it is:** [READ IN FULL] v1 design (2026-10-24, lane IN) splitting a person into four layers (capability, ambition, values, personality) and deciding what the seven pursuit axes become; one producer + one critic + orchestrator.
- **Status:** "PROPOSED (2026-10-24). HELD BACK ... superseded in part by character-layers-v2.md ... v1 still carries the cuts Jordan withdrew on 2026-10-25" (:3). Reading: partly superseded; its §5 cuts (boldness, patience, vindictiveness) are overruled by Jordan's "don't cut anything because there isn't a code reader yet" (v2 :10) and ED-IN-0304 ruling noted at :129.
- **Bears on:** CHAR, CORE, PC, SC.
- **Content that matters:**
  - Four membership tests in order (:49-54): capability = more always helps; ambition = some state satisfies it; value = direction nothing finishes; personality = varies independently of values, leaves odds untouched, no pole always wins.
  - Split of the seven axes (:25-27, :95-103): four are value readouts at spread 0 (`selfish_selfless`, `partisan_equitable`, `hierarchical_equal`, `precedent_substantive`); three get a stored per-person offset (`rigid_flexible`, `grandiose_humble`, `deontological_instrumental`) at ±0.15, derived as one corpus sd (0.12/0.11/0.15 over 46 authored rows, measured at :107-111) rounded up to 0.05.
  - Carrier proposed `Person.personality: dict`, absent key = offset 0 = control; build-only like `thread_sensitivity` (:84-85). Likeness readers read the prior over all seven columns so spread 0 keeps `World.content_hash()` exact (:116, :206).
  - Worked example (:152-166): A/B/C with identical pursuits rank `comply`/`challenge`/`forge` differently only with offsets; the armed deontology gate "hardly discriminates" at these magnitudes (:168).
  - Cut rows: `forgiving_vindictive` "dead reader" (grudge row keyed by faction name, `effects_combat.py:311-313`; candidates' subjects are persons); `choice_temperature` fails test 4 (:126-137).
  - Every authored NPC holds all 15 pursuits (`data/cast.py:209-211`), minted persons (`loop/census.py:106`) hold none; cohorts hold none (SE-06 / ED-IN-0296) (:79, :194).
- **Conflicts / stale:** overrides the ED-IN-0261 R7 dissolution clause ("two people with identical pursuits ARE identically disposed") for three axes (:37) — held for Jordan (v2 :25). Line numbers are of HEAD `d59acc9`.
- **Open items:** [GAP] candour/discretion/credulity/dogmatism untested (:135); `Combatant.disp` unmapped (two ladders for one trait family, :136, :216); gate convention is H-146's (:195); whether example verbs share one real `opening_set` (:220-221).

### proposals/2026-10-24-character-layers-v2.md
- **What it is:** [READ IN FULL] Reconstruction (2026-10-30) of a lost v2 design (session 2026-10-24/25) from a digest of that session's closing summary: ten axes, fifteen personality traits, attribute readers.
- **Status:** "PROPOSED — HELD BACK IN FULL; reconstructed from a digest, not from the original file; where this file and a re-derivation from the tree disagree the tree wins" (:3). Original `layers_v2.md`: LOST (:5). The session's closing line asked "want the v2 design landed as a replacement" and Jordan's answer is not on record (:8). Reading: design exercise record; figures unverified.
- **Bears on:** CHAR, PC, SC, CORE.
- **Content that matters:**
  - Ten axes: the 4 value readouts (spread 0) + 3 prior-plus-offset (±0.15) + 3 new personality-only axes `cautious_bold` (derived from verb-table exposure, 12 of 56 verbs), `hasty_patient` (declared per verb, 13 delay cases), `conciliatory_coercive` (declared per verb) (:50-59).
  - Fifteen traits = six manner offsets + nine per-person copies of global gain settings (`forgiving_vindictive`, `trusting_sceptical`, `open_dogmatic`, `guarded_open`, `steadfast_malleable`, `callous_scrupulous`, `serene_torn`, `frugal_lavish`, `steady_capricious`) (:65-69). Sorting rule: effect varies by VERB → axis; by claim/stance/deposit/scar → per-person gain (:103).
  - Attribute readers: Body → budget base and combat strength; Hand → forgery and combat agility; Wit → Recall (`claim_decay_per_season`, `ledger_cap`, `view_k`); Nerve → wound-band penalty and combat spirit; Sense → Watchfulness and `record_gain`; Presence → none (:86-95).
  - Measured example (unreproduced): identical pursuits, `cautious_bold` -1/+1 → chance of landing a duel in top five 0.130 vs 0.324 vs control 0.208 (:121-122).
  - Session findings (:127-131): capability empty for 429 of 430 persons; only `tell`/`speak` read it; candidate gaps 0.01-0.06 at tau 0.1, top candidate reaches top five 41% of the time, stance term -8.0 on every candidate; `selfish_selfless` has no nonzero cell on any verb; growth loop has no start and no exit (`train` raises only if already held). Conclusion: wiring what exists comes before new layers.
- **Conflicts / stale:** v1's "no per-verb cell, no new reader" is contradicted by v2's per-verb columns (:39). Falsifiers are carried from v1, restated "at v2's numbers" nowhere (:148-155).
- **Open items:** four owner calls (`selfish_selfless` spread; `choice_temperature` swallows personality, tied to CR-17 and ED-IN-0304; `payoff`/`force` columns are unargued judgement cells; refusal gate convention) (:137-142); progression open gaps (Thread Sensitivity among the six; floors for unrostered persons; mapping `stats:`; decay period N; Nerve tension) (:97).

### proposals/2026-10-24-character-progression-adjudication.md
- **What it is:** [READ PARTLY: lines 1-260, 275-394, 547-754 opened; §4.7-§8 (lines 395-546) not opened] One first-principles adjudication of character progression by a read-only agent (HEAD `b7a1e1b`), with a §10 addendum by the orchestrating session on Nerve/Composure.
- **Status:** "PROPOSED (2026-10-24); partly superseded since by the ratified v10 plan (M2 / ED-IN-0301: nine stored attributes on 1-7 with practice live; CR-18 takes the practice arm of CP-T01-02; CR-20 keeps `max(held key, base)` floor)" (:3). Reading: partly superseded; the six-attribute roster and the cut of accrual are overtaken, the code premises in §2 remain a usable map.
- **Bears on:** CHAR, DICE, PC, SC, MB, CORE.
- **Content that matters:**
  - Architecture (:246-253): six immutable stored attributes (Body, Hand, Wit, Nerve, Presence, Sense) setting a ceiling and floor on capability, never a dice term; one capability ladder; decisive-event writer at RESOLVE (+1 at most once per key per season) and decay; no lifepath bundle; tradition as an input/label; attributes never move; no mechanical specialness for the player's seat.
  - Code facts (§2): `Person` has no attribute/tradition field (`carriers.py:655-729`); `pool_default = obstacle_default = 2` (`fixtures.py:414,416`, graded assumption H-126/H-127); `_eff_train` only raises a held key (`effects_combat.py:421-446`); `verb_capability` maps only `tell`/`speak` to `copying` (`rosters.yaml:1232-1233`); one of 430 persons holds any capability (NPC-088); 8 of 56 verbs contest (`argue`, `arrest`, `determine`, `fight`, `accept`, `march`, `speak`, `tell`).
  - Combat's pool: `resolution_pool = max(POOL_FLOOR=5, int(round(history)) + BASE_POOL=6)`, obstacle `defender.history / 2.0`; the season seam derives exactly one `Combatant` field (`end`) so every season fighter rolls max(5, 3+6) = 9 and familiarity is always 1.0 (:160-186). Two ladders for one quantity (C-4).
  - Corrections C-1..C-10 (:547-625): familiarity does not reach the obstacle; `march` reads no capability; the handoff is `dispatching_chooser` not `choose.py:433`; "no switch while a contest is open" is not held by the seam; name collisions Body/`Person.body`/`agg.body`, Presence alias of Charisma.
  - Addendum §10: chooser score = pursuit term + stance + urgency, no risk term, no timing term (`choose.py:130-151`); ED-IN-0304 (2026-10-29) rules risk appetite and short/medium/long horizon wanted; Nerve is decision-side (Jaccard overlap nerve/composure 0.09); verdict "not both as attributes" but the adjudication keeps Nerve (:750-753).
- **Conflicts / stale:** the six-attribute roster vs v10 M2 nine attributes; claims about `rosters.yaml` line numbers drift. Outside-literature grades: Juul, Hunicke & Chapman read; Ryan/Rigby/Przybylski abstract only; Lundblade abstract only; game precedents "community-grade or from memory" (:229-236).
- **Open items:** [GAP] J-T1/J-T2/J-T4 open decisions not read by the agent (:24); authoring source for persons outside the registry (C-9); the Nerve/chooser tension (:751-753).

