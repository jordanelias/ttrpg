# Digest proposals_recent3

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: proposals dated 2026-09-20 or later (and undated), third slice: 90 assigned entries from the thrust-layer toy code (2026-10-25), the content-architecture suite (2026-10-28), the army phase-5 note (2026-10-29), the parliament-and-debate / social-contest folder (2026-10-29 to 2026-11-02, with its stress harness code and probe logs), and six files of the content-parameters docket (2026-11-04).

**Reading-depth note (honest).** The assignment is about 2.6 MB of text (roughly 31,000 lines): more than one session can hold. Each entry begins with a depth tag: `[READ IN FULL]`, `[READ PARTLY: ...]`, or `[HEADINGS+HEAD ONLY: ...]`. `:line` references were opened; claims about unread remainders are marked `[UNVERIFIED]` or omitted. Python toy and stress code was read by docstring, class/def inventory and version-to-version `diff`, not line by line.

**Ratification summary for this lane.** Only `2026-11-02-social-contest-build-all-plan.md` carries a RATIFIED status ("RATIFIED on merge (ED-1094, ED-IN-0308)", source of CR-55..CR-67 / batch B10-18c in the active plan; "dies with its rows"). Everything else is PROPOSED / HELD BACK / REFERENCE. The content-architecture suite is "HELD BACK IN FULL". The social-contest proposals 1-4 are PROPOSED (reference; resolves nothing). The stress-test files are terminal-pass REFERENCE records.

---

### proposals/2026-10-25-thrust-layer/toy/regimes_v1.py
- **What it is:** [READ PARTLY: docstring, class/def inventory, first 70 lines; body not read line by line] Python toy world (stdlib only, fixed seeds) logic-testing four narrative regimes, v1 world and metrics; byte-identical to `regimes.py` (`cmp` same). 2026-10-25.
- **Status:** none in the file; README declares "Grade: model-internal, low confidence. Reference under CLAUDE.md §0.05. Not game code, not read by any tool" (`toy/README.md:3-5`). Reading: historical evidence for `../00_THRUST_LAYER_DESIGN.md`, frozen.
- **Bears on:** WR, CHAR, CORE (narrative emergence design).
- **Content that matters:**
  - Four regimes: BU (bottom-up local drives), TD (scripted director forces a five-beat schedule, blind), TDR (same but re-reads state and re-picks the most hostile pair, still forces), HY (standing referent-bound ambitions assigned by a tension graph, with fire/lapse lifecycle and a declinable "occasion" summons channel; "No outcome is ever written by anything but an actor's act") (:2-13).
  - Control by construction: RNG streams are separate (world/acts/ambition/director), so HY with `w_amb=0` and occasions off consumes the act stream exactly as BU: identical log hash is the control (:15-16). Every metric is computed from the event log alone (:17).
  - Constants: 24 seasons, beats at t=3,7,12,17,21, beat intensities 1,2,3,5,8 (:20-22); world 24 actors, 6 places, 6 prizes (`simulate` default :362); death probability 0.25 in class `W` (:36).
  - Metric functions: `arc_test` (three-act template), `violations`, `graph_stats`, `five_node`, `cv_gaps`, `run_metrics`, `log_hash` (:437-598).
- **Conflicts / stale:** README records that the freeze hashes cover the predictions, not the world: `regimes.py` (`predictions.sha`) does not match its recorded hash in the freeze, same for `regimes2/5/10` (`toy/README.md:32`). v1 thread identity split a conflict across two references (fixed in v2 after seeing v1 results).
- **Open items:** none stated in the file; the design doc's falsified-vs-confirmed prediction list is the record.

### proposals/2026-10-25-thrust-layer/toy/regimes6.py
- **What it is:** [READ PARTLY: diff against v1, def inventory] Toy world v6: adds goal LADDERS (HYg1-3) and set pieces that write a situation (TDS, TDSm, HYg3s). README table maps it to `exp_setpiece.py` (`toy/README.md:15`).
- **Status:** none in file; reference/historical.
- **Bears on:** WR, CHAR, CORE.
- **Content that matters:**
  - Ladder stage types per ambition kind: claim = [reach place, ally, weaken holder, hold(2 seasons)]; oppose = [reach_p, weaken_p, defeat(>=3 harms or dead)]; other = [befriend] (the `build_ladder`/`stage_done` diff: `stage_done` predicates `reach`, `reach_p`, `ally` (any live x with op>=0.5), `weaken`, `hold`, `defeat`, `befriend` (op>=0.7)). This is the toy of the "ladder of stage predicates" in the thrust design; the design says current stage is a query, the toy stores `idx` (`s.amb[a].update(ladder=..., idx=0, stage_t0=t)`).
  - New knobs on `W`: `ladder_depth=3`, `deadline=6`, `cap=2`, `THETA=6.0`, `engaged_flag`, `sp_mode` (set-piece), `eng` (an engagement multiplies harm/claim delta between the two principals when `mult>1`).
  - Thread identity: claims keyed `T{min}-{max}` for pair, `P{k}` for prize (diff: `snap['thread']`).
- **Conflicts / stale:** the toy stores a stage index while the engine design forbids a stored counter (`00_THRUST_LAYER_DESIGN.md:40`) [from `DG_proposals_recent2`; not re-opened here].
- **Open items:** none in file.

### proposals/2026-10-25-thrust-layer/toy/regimes7.py
- **What it is:** [READ PARTLY: diff against regimes6] Toy world v7: set pieces with a decisive FORM (`TDSc`, `TDScf`, `HYg3c`).
- **Status:** none; historical evidence.
- **Bears on:** WR, SC (a contest as the conclusive form of a climax), CORE.
- **Content that matters:**
  - `contest_form`: best-of-rounds contest (first to 2 wins, max 5 rounds) at the venue, each round `randint(1,6)+skill` per principal; tie goes to higher skill. "The director authors the form and the stakes of losing; WHO loses is the dice's and the principals' skill's" (docstring in `contest_form`).
  - Consequence of losing: holdings (prizes) pass to the winner, loser skill -1 (floor 1), opinion -0.3, and at beat index 4 (the last beat) the loser DIES; stakes = beat intensity `BEAT_I[i]` unless `sp_flat` (`TDScf`, flat stakes 3).
  - Event logged with `causes=[last_ref[ref], last_reloc]` and `closing=True` when death or prizes moved (`closing` is a field the later engine design strikes, see `DG_proposals_recent2` thrust entry).
- **Conflicts / stale:** the lethal last beat is what M20/M21 later cut (the `Slain` band) per the thrust design status [UNVERIFIED here].
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes8.py
- **What it is:** [READ PARTLY: diff against regimes7] Toy v8: non-lethal and settled climaxes (`TDScn`, `HYg3cn`, `TDSc_s2`, `HYg3c_s2`). README: "(run inline)", output "not saved" (`toy/README.md:16`).
- **Status:** none; historical. Results printed only, so not reproducible from saved files.
- **Bears on:** WR, FA (settlement/pact as closure), SC.
- **Content that matters:**
  - Flags `s.lethal` and `s.settle`. Non-lethal ending ("exiled"): loser keeps life, is stripped of holdings and moved to another place. Settlement (`_s2`): holdings pass, the feud is closed by pact (`op` set to 0.3 both ways, `last_harm` cleared), both stay in play.
  - `closing` is true for died, exiled, moved or settled: so a "closure" is any of those.
- **Conflicts / stale:** unsaved outputs; the design cites these numbers [UNVERIFIED].
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes9.py
- **What it is:** [READ PARTLY: diff against regimes8] Toy v9: adds standing snapshots on events (`astand`, `tstand`: number of prizes held by actor and by target at event time). README: "(run inline)", not saved.
- **Status:** none; historical.
- **Bears on:** WR, FA (standing as a held-prize count).
- **Content that matters:**
  - "Standing" in the toy = number of prizes held (`README.md:41` limit: "'Standing' is holding a prize; the 90% gate is a model setting that was not swept").
  - Used to review earlier arcs against the standing context; output printed, not saved.
- **Conflicts / stale:** none verified.
- **Open items:** the 90% gate not swept (README).

### proposals/2026-10-25-thrust-layer/toy/results_v1.json
- **What it is:** [READ PARTLY: keys and base-condition metrics via python] Saved output of `suite.py` (v1 instrument), N seeds per regime per condition.
- **Status:** none; frozen data (data file; read by nothing, README: "not read by any tool").
- **Bears on:** WR.
- **Content that matters:**
  - Top-level keys: `base, noent, engine, small, null, pert, dose, abl, ctl`; each condition has regimes `BU, TD, TDR, HY` (conditions: `noent`=entrenchment off, `engine`=refuse 0.8, `small`=12 actors/10 places/4 prizes, `null`=8/8/3).
  - v1 is superseded by v2 (instrument fix: pair-thread identity, plateau peak, burn-in, director thread).
- **Conflicts / stale:** v1 thread identity split a conflict across two references and climax sat outside its peak window (README:31).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/results_v2.json
- **What it is:** [READ PARTLY: keys and base metrics via python] Output of `suite2.py` (v2 instrument).
- **Status:** none; frozen data.
- **Bears on:** WR.
- **Content that matters:**
  - Same condition set as v1 plus per-regime metrics (`leg_apparent`, `leg_grounded`, `forced_in_sel`, `viol`, arc variants `arc_p92_relax_b4` etc., `depth`, `dir_is_main`, `dir_mass_rank`).
  - Base-condition readings (my read of the file): `arc_p92_relax_b4` BU 0.087, TD 0.16, TDR 0.35, HY 0.057; chain `depth` BU 23.0, TD 24.5, TDR 22.0, HY 30.1; `forced_in_sel` TD 0.147, TDR 0.332, BU/HY 0.0; `viol` TD 3.89, others 0.0; `dir_is_main` TDR 0.72. So the hybrid does not win the arc-shape metric; the scripted/replanned director does, at the cost of forced (ungrounded) events.
  - Depth 22.99 (BU) vs the "62.5 vs 23.0" figure the design cites for the unconstrained HYg3 world comes from `save_figs.py` re-run, not this file.
- **Conflicts / stale:** none verified.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/save_figs.py
- **What it is:** [READ IN FULL] 24-line script re-running and SAVING two figures the design v1 had only cited from the terminal; uses `regimes10` with `CON=dict(death_p=0.01, gate_p=0.9, accuse=True, truce=True, conseq=True, lethal=False, tdr_kill=False)`, N=300.
- **Status:** none; historical; output `save_figs_out.txt`.
- **Bears on:** WR, FA.
- **Content that matters:**
  - Computes chain depth for constrained world (BU, HYg3, HYg3d, HYg3c) vs unconstrained (BU, HYg3: "the 62.5 vs 23.0 figure"); and "killing at season 10" cascade: acts against the killer, distinct actors, tribunals naming the killer.
  - Constrained-world settings: death probability 0.01 (rare death), a 90% standing gate, accusation, truce, and consequences switched on.
- **Conflicts / stale:** world file `regimes10.py` hash does not match `con_pred.sha` (README:32).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/suite.py
- **What it is:** [READ IN FULL via diff + head] Driver for v1: imports `regimes`, `predictions`; runs N seeds (default 300) over `BU/TD/TDR/HY` and conditions `base/noent/engine/small/null`; writes `results.json`. Byte-identical to `suite_v1.py`.
- **Status:** none; historical.
- **Bears on:** WR.
- **Content that matters:** `CONDS` dict (base, noent=`entrench=0`, engine=`refuse=0.8`, small=`A=12,P=10,PR=4`, null=`A=8,P=8,PR=3`); `agg` averages every metric except thread signature fields.
- **Conflicts / stale:** writes `results.json` while the saved file is `results_v1.json` (naming only).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/suite2.py
- **What it is:** [READ IN FULL via diff + head] v2 driver: `regimes2` + `predictions_v2`; adds arc variants and director-thread rows; writes `results_v2.json`.
- **Status:** none; historical.
- **Bears on:** WR.
- **Content that matters:** only differences from suite.py are the import swap, NaN filtering in `mean`, `main_ref`->`main_thread`, and two extra report groups ("ARC variants", "DIRECTOR THREAD").
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/suite_v1.py
- **What it is:** [READ IN FULL: `diff` shows identical to `suite.py`] frozen copy named by `v1_files.sha`.
- **Status:** none; duplicate by design (README states it).
- **Bears on:** WR.
- **Content that matters:** nothing beyond suite.py; a doubled file kept for hash-pinning.
- **Conflicts / stale:** doubled with `suite.py`, `regimes_v1.py`==`regimes.py`, `predictions_v1.py`==`predictions.py`.
- **Open items:** none.

### proposals/2026-10-28-content-architecture-suite/00_INDEX.md
- **What it is:** [READ IN FULL] Index of a review suite written in a 2026-10-28 session (lane IN) that committed nothing; this directory is a reconstruction (2026-10-30) from the session transcript at repo head `be24c71`.
- **Status:** "PROPOSED ... HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing" (:3). Reading: historical/reference; every figure and line cite is as of be24c71 and unre-verified (:8).
- **Bears on:** CHAR, CORE, SE, FA, WR, GO, PROCESS.
- **Content that matters:**
  - One-page answer: "The engine is a lawful society simulator, not yet a game"; five gaps block play in order: a seat for a human, capability, an authoring layer, situations, words (:16).
  - Three proposal sets, recommended package P1-B (story openings drawn from pools at world build) + P2-A (the plan's nine attributes with Thread Sensitivity counted as tenth) + P3-B (management console plus scenes built on a text client) (:39-47).
  - 12 rulings needed from Jordan (:49-51); rulings 1, 2 and 5 reopen defaults confirmed 2026-10-26.
  - Recovery bookkeeping: part 06 and appendices A1-A5 recovered in a third pass, `fragments_of_unrecovered_parts.md` superseded by them (:37).
- **Conflicts / stale:** the map table lists `appendix/A1..A5` but they are flat files here (:37). Two numbers withdrawn inside: refusal percentages 77.8% and 58.8%, and "45-of-56 for an unseated person" (:37).
- **Open items:** the 12 rulings; ledger rows for three "yes" decisions, the no-forecast combat directive and troop/equipment directions "owed, not done" (:55).

### proposals/2026-10-28-content-architecture-suite/01_MAIN_REPORT.md
- **What it is:** [READ IN FULL] Part 01 sections 0-9: Q1-Q8 answered (content census, attributes, character, faction, settlement, event decks, storylines, the 55-arc register).
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference; many claims later corrected by 07a-07d (:12).
- **Bears on:** CHAR, FA, SE, WR, ARCS, CORE, DICE.
- **Content that matters:**
  - `build_realm(0)`: 83 persons (46 named + 37 cohorts), 32 offices, 322 sites, 67 Propositions, 56 verb rows of which 51 resolvable; `Person.capability` empty on 83/83; requirements met 3, partial 5, not met 1 (:22, :28, :48).
  - Chooser: Question -> View (<=12 claims) -> budget (5 +1 per live `hold` Tenure, minus body bands and legs, >=1; at most 5 scenes released a season, `loop/deliberate.py:85-113`) -> options -> score = sum(axis weight x verb alignment) + 2 x stance -> softmax at tau 0.1; score ignores capability, odds, goal text, scars, conviction (:106). "Values pick the verb, stance picks the target, the question picks the matter."
  - Faction = creed Proposition + live `commit` Tenures; `queries/faction_q.py:84-96` five-field view; `head` is None for all because nothing writes `Tenure.degree` (:114). Settlement = `Rung` of kind settlement; 4 gaps: cohort has empty pursuits/stance/conviction, no seat at any settlement, geography Prosperity/Defense/Order never read, `set.*` read by nothing (:137).
  - Tensions deck: no event/card carrier in code, `tensions.yaml` absent; the plan's deck is 6 cards, draw 1; a card "may not be data" for date, deadline, firing condition, outcome, standing write, seat, tenure, stance, or `closing`/`successor`/`deal` (`B10-18.md:183`) (:163-171).
  - Storyline form: a "scenario bundle" = role-bound goal rows + one seeded claim, drawn at `build_realm`, opened only by a bound person's own act; pool size P >= k^2 to keep overlap under one; needs B10-19 clause amended (:186-198).
  - 55-arc register: 31 reproduced-better, 2 reproduced, 16 transformed, 4 lost (5, 22, 27, 48), 2 never worked (19, 52); 1 of 50 traced arcs plays (ARC-06); reachable arcs ~17 as planned, ~36 with summons hook + TS + scenario rows, ~40 with `foreign` on, ~47 with a world Thread substrate (:210-228).
- **Conflicts / stale:** its "TS needs J-T2" and "naming TS unlocks 12 arcs" and "2 of 9 NEVER arcs numbered" are corrected in 07a/07c; `supersession_register.yaml:22-28` calls `fac.legitimacy` live though 29b superseded it (:129). [UNVERIFIED here: whether `engine/season` has since added `faculty` or `tensions.yaml`.]
- **Open items:** gap whether a boot-time date can be written without an act's token (:57); AX-7 deposit check for `seed_claim` (:193); Layer-1 rules S10.1 / 04 row 27a unchecked for the dossier layer (:157).

### proposals/2026-10-28-content-architecture-suite/01_MAIN_REPORT_part2.md
- **What it is:** [READ IN FULL] Part 01 sections 10-15: per-subsystem legibility cards, the 12 rulings, reliability, management surface, minigame contract, later directives.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference; contains Jordan's directives recorded as such.
- **Bears on:** GO, CORE, PC, MB, SC, FI, SE, FA, CHAR, WR.
- **Content that matters:**
  - Parity principle: the player is the decision procedure of one seated person; a scripted callback that returns the chooser's pick must reproduce `content_hash` (REM-31) (:16). Legibility policy: combat shows facts only, no forecast ("we wouldn't really forecast"); Proceedings shows no odds (`21_RECONCILIATION.md:617`); other rolled acts show band odds (v10 `part14:282`) (:16).
  - Rulings list (:53-64): troop counts [M3] amends Layer 1 `04:801/:810`; attribute list [J-T2]; training rule (additive excess instead of CR-20 `max`); who owns a sword; storyline form; mass-battle command (plan-before vs live); runtime faction founding; Mayor seats (37 towns, `confer` load); Thread substrate "dying vs misunderstood"; management surface weak vs strong reading; odds shown; console may show only ledger-held values (AX-7 vs `04:851-862`).
  - Management surface (§13): "weak reading" = batched front end over seat verbs the player's seated person holds (AX-1 unchanged; no menu when unseated); "strong" needs AX-1 / `04:853` amendment. An order writes exactly what its verb row writes; same eligibility and refusal gates; no scene budget implemented once in budget owner (`deliberate.py:252-258`) (:85-103).
  - Minigame contract (§14): input builder freezes world state; human replaces the chooser at defined moments (REM-31's six: measure, reopen, commit, mode, counter, contact); module returns a graded result, host folds it to writes at RESOLVE (or ENCOUNTER); three fidelities (auto, scripted, human) on one resolver (:117-123). Per-subsystem table: threadwork has no provider or role (:133).
  - Fire Emblem-style fight window with no forecast; combat trace has 16 event kinds, none naming a technique firing, so callouts need a new trace field (`seam/wrappers/combat.py:252`) (:146).
- **Conflicts / stale:** §14 table says personal combat "fight resolves at RESOLVE" but earlier draft said ENCOUNTER; corrected in 07d (:129). Not-read-in-full list: plan parts 6-14, `RULINGS.yaml`, Proceedings files beyond heads (:76).
- **Open items:** all 12 rulings; ledger rows owed.

### proposals/2026-10-28-content-architecture-suite/02_P1_templates.md
- **What it is:** [READ PARTLY: §1 head, §3, §4, §5 opened; §2 P1-A not opened] Three template packages: dossiers over existing carriers (A), dossiers plus pools drawn at world build (B, recommended), authored set pieces and per-season docket decks (C).
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference; proposes a new authoring layer, built nowhere.
- **Bears on:** CHAR, FA, SE, WR, ARCS, CORE.
- **Content that matters:**
  - Authoring-layer rule: a field is true at the start, has one author, no act has touched it; anything that counts, sums or compares is a query; the dossier becomes the head of `npc_registry.yaml`, the person fields of `npcs.yaml`, and the holder column of `offices.yaml`, behind an exporter `--check`, in `engine/season/dossiers/` with one loader, pending a `layer-conformance` check against 04 row 27a (:29-33).
  - Character dossier: identity, position, capability (attribute block, practice keys, TS, body, kit), ambition (goal rows, `goal_stages` ladder, catalyst want), values, personality (3 offsets behind spread-0 control), knowledge (up to 12 seed claims), history (lifepath key, never stored) (:35-46).
  - P1-B pool card fields: id, family, `source:`, eligible, attach, roles, role-bound goal rows, one seed claim, `opens_with` (:120-122). Worked Klapp example: archive pool of 6 cards; conceal -> seek counsel -> disclose/convert ladder writes nothing (:124-132).
  - P1-C amends T-c, AX-5 fourth motion, ED-IN-0225, ED-WR-0011, B10-19 (:151-156); arcs ~46 reachable vs B's ~36 (:144, :166).
  - Falsifier for B: between-world similarity falls and stock share does not rise; control: empty pools give identical hash (:140).
- **Conflicts / stale:** same "327 of 1,132 attempted acts" refusal figure as 01; relies on `proposals/2026-10-22-system-description/ctl/realm_seed0_2seasons.txt`.
- **Open items:** B4.1 (summons hook) held with no owner; Item kind needs `layer-conformance` and Jordan's yes if 04 §B.7 closes `hold`'s objects (:138).

### proposals/2026-10-28-content-architecture-suite/03_P2_attributes_skills_histories.md
- **What it is:** [READ PARTLY: §1, §3 head, §6 opened; §2 worked verbs, §4 P2-B, §5 P2-C not read] Three attribute/skill/history packages: P2-A plan's nine + TS tenth (recommended), P2-B demand-derived eight, P2-C six used as floors/ceilings.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference; no `Person.attributes` or `faculty` built.
- **Bears on:** CHAR, DICE, PC, SC, FI, MB.
- **Content that matters:**
  - Verb rule: a verb row never names an attribute; a contested row maps `verb_capability: verb -> key`, `key_base: key -> {act, resist}`; `resist` defaults to `act` (ED-IN-0185 Q2 "their corresponding score/2") (:36-39). 45 of 56 rows read no person quantity (`verb_table.yaml:33-35`).
  - 14 skill keys, only `copying` exists (`rosters.yaml:1232-1233`): copying, argue, inquiry, lore, watch, insight, stealth, reckoning, command, arms:<family>, craft, labour, fieldcraft, thread (:45).
  - Lifepath stages origin(8)/formation(7)/vocation(34)/catalyst(7+1) in `rosters.yaml: lifepath_templates`; catalyst seeds one OUGHT commit with `goal_stages` ladder (M20(b)) (:53-60).
  - P2-A table: 1-7 scale, STR END AGI FOC ACU WIL ATT CHA BON + TS 0-100 as addend on `thread`; "primary in" counts from A6's 104-moment matrix (ATT 27, ACU 21, CHA 17, AGI 15, END 11, TS 11, STR 10, WIL 9, BON 7, FOC 1) (:86-97).
  - Worked sheets Klapp (NPC-039) and Lord Steward Gerik Strand (NPC-009), all `[ASSUMPTION]` (:203-218). Migration touches `descriptor_registry.yaml:33-48`, Godot `CharacterData.gd:14-23` (:220-227).
- **Conflicts / stale:** "LANDED ALREADY: faculty" in CR-20 is false at HEAD (:42).
- **Open items:** training rule amendment (additive excess); Klapp's registry TS is null (`npc_registry.yaml:1032`).

### proposals/2026-10-28-content-architecture-suite/04_P3_player_surface.md
- **What it is:** [READ PARTLY: §1, §3, §4, §5 opened; §2 cards not opened] Three player-surface proposals: P3-A ledger and menu, P3-B management console plus minigame scenes (recommended), P3-C map-centred client.
- **Status:** PROPOSED, HELD BACK IN FULL (:3); line 13 repeats "PROPOSED; every instance is [ASSUMPTION; medium; Jordan to correct]". Reading: reference.
- **Bears on:** GO, CORE, CHAR, PC, SC, MB.
- **Content that matters:**
  - Measured: a rung 1-2 seat (Klapp, Lord Steward) is eligible for 45 of 56 rows (41 everyone has + 4 seat rows `issue/covenant/requisition/seize`); neither can `confer`, `revoke`, `dispatch`; the Confessor can (`engine/season/offices.yaml:364-369`) (:30).
  - Klapp seed-0 trace: budget 6 with 28 options; Lord Steward in season 2 picks `fight` on the King, showing the risk-free-fight defect (CP-T03-00) (:31).
  - Combat seam returns a 16-event-kind trace; every season fighter is a default `Combatant` (arming sword, light armour) (`queries/inputs.py:107-121`) (:32).
  - Army/kit: BUILT march, requisition, transfer, issue, seize, dispatch; 10 troop types (`troop_types/registry.py:39`); 54 weapon records; MISSING recruit, muster, supply, disband, merge, equip, repair, craft and `Person.kit` (:33).
  - Common items: parity seam, facts-only combat, trace viewer in B10-S, drop reasons, ledger-delta season account, do not display the unspendable budget surplus, M3(A) before any unit count (:85).
- **Conflicts / stale:** P3-C's map promise needs CP-T10-01 `route()` to price distance.
- **Open items:** L-3 (map of believed holdings acceptable?).

### proposals/2026-10-28-content-architecture-suite/05_A7_subsystem_merit.md
- **What it is:** [READ PARTLY: verdicts, §3 combat, §4 mass battle, §5 Proceedings, ranking, order, escalations; §1,2,6-10 not opened] Merit analysis of each subsystem alone and in the world.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference.
- **Bears on:** PC, MB, SC, FI, WR, SE, FA, CORE, GO.
- **Content that matters:**
  - "None of the ten is playable today"; `dispatching_chooser` is called only by tests (`harness/play_surface.py:41`) (:16-17).
  - Ranking: Proceedings H/H, Personal combat + kit H/H, Mass battle + troops M->H, Fieldwork M/H, Threadwork M/L->M, season loop frame, dice frame, settlements/economy and factions/war as management menu (:167-179). Order of becoming playable: frame, combat, Proceedings, fieldwork, menu, mass battle with troops, travel, threadwork (:181-191).
  - Mass battle: 18-tick grid engine, 10 troop types; army "is just whoever lives at home" (`loop/sides.py:116`); no battle fought at seed 0; recommendation K-MB-4 plan-before-battle (Dominions) is a research recommendation, not a ruling (:76-98).
  - Proceedings: pool reads nobody (`pool_default`, `sigma.py:119-131`); under H-213 ceiling 2 the room can only lower the obstacle (`roll.py:63-100`); `speak` changes nothing; speech cannot lie (J-C-6) (:100-111).
  - Escalations E1 (M3 counted troop stock in `Rung.stores`, amends Layer 1 `04:801/:810`), E2 (J-T5 kit as `hold` Tenures on equipment objects) (:193-195).
- **Conflicts / stale:** critic lens-3 finding 2 says "Decision taken (K-MB-4)" at :87 is wrong; the K-MB-4 is a recommendation (`critic_lens3.md`).
- **Open items:** troop-grade ladder, recruit share, A1 content, kit values left for Jordan (:191).

### proposals/2026-10-28-content-architecture-suite/06_A6_attribute_demand.md
- **What it is:** [READ PARTLY: §2, §3, §4, §6, §7 opened; §1 matrix and §5 touch list not opened] Attribute set re-derived from a 104-moment demand matrix.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference; 07a notes 83 of its 104 moments come from PROPOSED lexicons (07a correction 7).
- **Bears on:** CHAR, DICE, PC, SC, FI.
- **Content that matters:**
  - Verdict on the nine: keep STR END ACU AGI WIL CHA; merge FOC into WIL, BON into CHA; split ATT into PER + INS; TS stays on `Person.thread_sensitivity` (:65-76). Recommended eight on 1-7 plus TS 0-100 (:78-93).
  - `faculty(p,verb) = max(capability[k], attributes[vocation_attribute[k]])` else `pool_default`, `k = verb_capability[verb]`; opposition reads the subject's held key or the same attribute (:95-103).
  - "J-T2 is irrelevant": TS already has a build-only carrier (`state/carriers.py:717`); storing `attributes['ts']` would be a second copy (§0.05 cl.3). ED-IN-0185 "it will be 10" (2026-08-14) predates any demand table (:123-129).
  - Escalations: the count (eight vs ten), warmth vs presence (one stat or two), symmetric vs per-verb resist (:131-135).
- **Conflicts / stale:** A6's eight overwrites ED-IN-0185/ED-IN-0301 (07a Needs Jordan 1). Matrix scored by REASONED mapping, not execution.
- **Open items:** the three escalations.

### proposals/2026-10-28-content-architecture-suite/06b_A6_matrix_and_probe_evidence.md
- **What it is:** [HEADINGS+HEAD ONLY: headings and first lines] Scripts (`matrix.py`, `alt.py`, P2 probe) and printed output behind part 06's 104-moment demand matrix.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: evidence for 06; reference.
- **Bears on:** CHAR, DICE.
- **Content that matters:**
  - Matrix is a hand mapping: moment -> (subsystem, status B/M/D, primary capacities, secondary) with status B = built season contest, M = module code reads it (off season path), D = designed (lexicon) draw (:14-15).
  - Output blocks for all 104 moments, built+module only (21) and built-season only (11) (:306-321, :359-371): the built-only slice is tiny, so "dominance" of any attribute rests mostly on designed verbs.
- **Conflicts / stale:** `[REASONED mapping]` not measured.
- **Open items:** none.

### proposals/2026-10-28-content-architecture-suite/07a_ADJ1_character_verbs.md
- **What it is:** [READ PARTLY: lines 12-72 opened; resolved-by-class row tables after :73 not] Adjudication of conflicts C-001..C-100 and C-374..C-492 (219 rows, 32 clusters) on character and verbs/decision layer.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference; one of four adjudicators over 754 recorded conflicts ("0 of 754 needed a design ruling to settle what runs", 01 part2 :49).
- **Bears on:** CHAR, DICE, CORE, WR.
- **Content that matters:**
  - Verified: 9 attribute keys 1-7 plus unnamed tenth (`descriptor_registry.yaml:28-48`), `Person.attributes`/`faculty` not built; 15 pursuits x 7 axes + 5 affiliations; TS written once at build (`data/cast.py:283`), `thread_read` gate 30 (`fixtures.py:948`) (:14-17).
  - Chooser score = `damp * sum(axis_w * align) + stance + urgency` (`decision/choose.py:130-151`), Plackett-Luce at tau 0.1; no capability/odds term (:20).
  - Stale code comments say "thirteen", "four-axis", "13x4" at `decision/choose.py:440-441`, `decision/options.py:386-398`, `rosters.yaml:525`; code runs 15x7 (cluster 12).
  - Cast data errors: `npc_registry.yaml:981` names NPC-004 as Cardinal Justice but it is NPC-038 Olafsson (cluster 10).
  - Corrections list (:60-68): TS is BUILT; 77.8%/58.8% withdrawn; "budget 6" cannot be spent (5 releases/season); A6's eight is an overwrite only Jordan can take.
- **Conflicts / stale:** `derive_command(charisma, cognition)` exists in `modules/mass_battle/core/exchange.py:57`, so "zero occurrences" is false (cluster 6).
- **Open items:** J-T2 roster shape (:70-71).

### proposals/2026-10-28-content-architecture-suite/07b_ADJ2_faction_settlement.md
- **What it is:** [READ PARTLY: :14-22 and :56-72 opened] Adjudication of C-101..C-249 (149 rows) on faction and settlement/geography.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference.
- **Bears on:** FA, SE.
- **Content that matters:**
  - `fac.*` stat block retired at plan v8 position 29b (`descriptor_registry.yaml:76-79`, `engine/substrate/descriptors.py:19-22`, `restructure_ledger.md:2687-2701`); legitimacy is a per-knower query `queries/person_q.py:452`; `set.*` rows have no runtime reader (F1, F2).
  - Standing/stature bonus is not a stat: budget = base + office_bonus x live `hold` tenures - body - travel (`decision/budget.py:18-60`) (F4).
  - Corrections: 37 settlements under 16 (not 17) territories; troop levy is built and shipped off (`requisition` + `settlements.provision`, `test_levy_feed.py:1-6`, H-241); `adjacency:` (26 edges) is read for lattice coupling (`data/geography.py:43-61`, `loop/matter.py:156`) and `terrain:` by mass battle (:56-66).
  - Needs Jordan (3): Mayor seats (37 vacant seats, measure `confer` load), runtime founding of factions via `utter` OUGHT + `commit`, Altonia foreign default (IN-36) (:67-71).
- **Conflicts / stale:** Godot `ValoriaDataLibrary.gd:20-25` ships Niflhel and stat blocks (port-side correction owed).
- **Open items:** the three.

### proposals/2026-10-28-content-architecture-suite/07c_ADJ3_events_arcs_clocks.md
- **What it is:** [READ PARTLY: :16-41 and :100-115 opened; clusters :42-99 not] Adjudication C-250..C-373, C-629..C-670 (166 rows) on events/decks, arcs, clocks/world/victory.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference.
- **Bears on:** WR, ARCS, CORE.
- **Content that matters:**
  - Measured: `tensions.yaml` absent; 6 cards, draw 1; Jordan's "45" = 6 Tensions + 28 Goldenfurt + 11 named; grounded deck "58" is its own claim, 50 ids named, 8 written (:17-25).
  - Arcs: 55 numbers/58 titles; `ENDINGS_CLASSIFIED.yaml` 50 rows: 18 unforced DECIDER/ROLL, 11 forced, 8 THRESHOLD, 9 NEVER (arcs 05,16,24,25,26,28,36,38,39), 2 unclear (:26-31). 97 ARC-lane cases; 143 = 97 + 46 NPC.
  - Clocks: none runs in the loop ("six steps, four barriers... no container gets a clock", `loop/driver.py:239-240`; "NO CLOCK GENERATES", `loop/census.py:39`); `ms_track.py` still on disk with no importer (:32-37).
  - Endings: two rows (`peninsular_sovereignty`, `theocracy`, `rosters.yaml:2553-2615`), none reachable: H-176 graded `absent`; fix is CP-T09-04's unpeopled `seize` (:38-41).
  - Corrections: ED-IN-0225 refuses only an arc carrier, M20(b) narrowed it, so the question is not Jordan's; a plan-text amendment of `part12:276` suffices (:100-103). `open_case` mints kind `text` (`effects_information.py:286-287`); `assessment`/`exposure` Record kinds are NEW.
  - "Needs Jordan: None" (:112).
- **Conflicts / stale:** calendar: no year unless `season_factor_draw` has a table, which ships `()` (`queries/world_q.py:936-942`).
- **Open items:** GD-1's sustain/Accord/PS clauses held under a LEAVE trigger (`_part10:131`).

### proposals/2026-10-28-content-architecture-suite/07d_ADJ4_subsystems_ui_process.md
- **What it is:** [READ PARTLY: head, :69-86 opened; cluster table :24-68 not] Adjudication C-493..C-628, C-671..C-754 (220 rows, 37 clusters) on subsystem rules, UI/Godot, process.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference.
- **Bears on:** PC, SC, MB, GO, PROCESS, DICE.
- **Content that matters:**
  - Code answers: TN is 7; wounds add fractional Ob; a personal fight resolves at RESOLVE, only `a field` at ENCOUNTER (`rosters.yaml:1079`, `:1284`); mass-battle pool is quality x numbers with no Command term; Godot 4.7 (ED-GO-0002) (:16-23).
  - Since SC-02 22a the obstacle subtracts bench `reception` (gain 1.0, H-215) and unmirrored `proofs` (`roll.py:63-100`; `test_sc02_reception.py`); the pool itself reads nobody (`sigma.py:119-131`) (:73).
  - Command under `POOL_QUALITY_MODEL` (default on, `config.py:556`) does not enter the raw combat pool; derivation `round((2*CHA+COG)/3)` clamped 1-7 (`exchange.py:55-64`) (:77).
  - Odds policy settled: combat facts only; Proceedings none; the actor's own other rolled acts band odds (:75-76). Believed-odds mode (CP-T01-03 (b)) was released by M1 DECISION, not withdrawn (:78).
  - `valoria-game` pins Godot 4.3 vs ruled 4.7, hand-copied `game_constants.json` carries 7 retired-model keys (:80-85).
- **Conflicts / stale:** CLAUDE.md §3's "systems/ retained for combat, social_contest, mass_battle" line vs ED-SC-0033 / ED-IN-0284; today's CLAUDE.md already says systems holds only sim/ oracle homes [UNVERIFIED].
- **Open items:** the two Needs Jordan items.

### proposals/2026-10-28-content-architecture-suite/08_decks_and_template_in_engine_form.md
- **What it is:** [READ PARTLY: :6-40, :209-248 opened; cards §1 body and Goldenfurt §2 not read] The six Tensions cards and Goldenfurt's 28-card deck rewritten into `goals.yaml` rows; settlement template.
- **Status:** "PROPOSED — HELD BACK. Reference under CLAUDE.md §0.05 until a loader reads it ... Every row is [ASSUMPTION; medium; Jordan to correct; revert: delete the row]" (:3).
- **Bears on:** WR, SE, FA, CHAR, CORE.
- **Content that matters:**
  - Executed: 27 of 27 rows accepted by `data/goals.py::parse` atop 38 rows of `goals.yaml`; the nine Goldenfurt rows each mint a Proposition with exactly one committed person (e.g. `gf_commune_against_guild_toll` -> NPC-081); `content_hash` moves `3e31638ef6ee` -> `2e7f4f3d01da` with rows on (:11-16).
  - Attention reading (3 arms with placebo, seeds 0-1, 3 seasons): five rung-aimed persons' acts with subject in S-006: off 11/4, on 29/21, placebo 9/3 (placebo hits S-007 23/17) -> the rows redirect attention and do not add acts; "whether that is a story is not shown" (:231-245).
  - Tensions cards in engine form: Royal Crisis = goal on plotting faction with object `seat_holders` stance -1 (9 rows); Feldmark Famine = `yield_scale` 0.75 on `terr_T5`; others rung/territory goals (:21-28). Not executed: `yield_scale` cards (no loader), seed Records (no carrier), docket (no deal effect) (:17).
  - Settlement template: five opening kinds with seat slots; "no seat is anchored at a settlement (`offices.yaml:98`)"; type-eligibility reaches 36/37 for market dispute, 12 with a person homed there (:209-224).
- **Conflicts / stale:** the "12 unexpressed cards" stay unexpressed until engine has writer/verb/field (:246).
- **Open items:** needs a `settlement_openings` loader and goals visibility fix; deal effect for the docket.

### proposals/2026-10-28-content-architecture-suite/appendix_A1_content_census.md
- **What it is:** [READ PARTLY: verdicts head :17-29 opened; §1-9 not] Analyst report on Q1: carriers, content, player surface, narrative text, path to a playable slice.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference.
- **Bears on:** CORE, GO, WR, CHAR.
- **Content that matters:**
  - Layers: carriers partial, content thin, player surface none, narrative text none in game (:19-24).
  - "Does workplan v10 contain a path to a playable slice? No": "vertical slice/playable slice/first playable" return zero hits across `workplans/`, v10 folder, `CURRENT.md`, `HANDOFF.md` (:26).
- **Conflicts / stale:** refusal percentages withdrawn per 00_INDEX (:37).
- **Open items:** 3 escalations (:170).

### proposals/2026-10-28-content-architecture-suite/appendix_A2_character.md
- **What it is:** [READ PARTLY: verdicts :13-25 opened] Analyst report on Q2-Q3: attributes, verbs, character template, decision-making.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference.
- **Bears on:** CHAR, DICE.
- **Content that matters:**
  - "Prowess := faculty(p, verb)"; "aptitude" retired (three senses `proposals/2026-10-16-attribute-derivation_aptitudes.md:8-14`); count SETTLED at nine with tenth pending (ED-IN-0301, `registers/editorial_ledger_in.jsonl:87`); 13 Convictions RETIRED, live pursuit names doctrine and stewardship (ED-IN-0261) (:15-25).
  - Engine chooses every act; chooser ignores capability, odds, goal text, scars, conviction (:19).
- **Conflicts / stale:** A2 says nine+TS, A6 says eight (07a correction 7).
- **Open items:** escalations (:165).

### proposals/2026-10-28-content-architecture-suite/appendix_A3_faction_settlement.md
- **What it is:** [READ PARTLY: verdicts, :147-168 opened] Analyst report on Q4-Q5.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference.
- **Bears on:** FA, SE.
- **Content that matters:**
  - Faction = creed + commits; the old four hold 15 territories (Crown 6, Hafenmark 4, Varfell 4, Church 1); no player-faction flag (:150-152).
  - Decisions D1-D8: close stale `supersession_register` row; retire `set.*`; governance mode stays deleted (query over conferral/body in `governors_of`, H-100); no faction-named verbs; `declare` gated on `remit:dispatch`; seven `venues` types are the type roster; cards deposit a claim only; Guilds/Schoenland no template (:156-164).
  - Escalations: runtime founding (FA-G39 parked), Mayor seats (:166-168).
- **Conflicts / stale:** "37 settlements under 17 territories" wrong (07b correction 1).
- **Open items:** the two escalations.

### proposals/2026-10-28-content-architecture-suite/appendix_A4_subsystems_playable.md
- **What it is:** [READ PARTLY: gaps §4, decisions §6, escalations §7 opened] Analyst report on Q6.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference.
- **Bears on:** GO, CORE, PC, MB, SC.
- **Content that matters:**
  - Top 8 gaps: no seat; no odds at choice (`band_odds`, B10-08); menu names verbs not consequences; only the top question seen (`first`); silent nothing (empty menu returns `[]`; `finding.none` reaches nobody); no stake or end; acts cost nothing (H-205); no season account (:79-88).
  - Fights use three fidelities on one resolver; "duel mode keeps 3 closed moments (05 §4.2)" (:104).
  - E1 true odds vs held arithmetic (AX-7 `01_AXIOMS.md:301` vs `04:858`); E2 live vs plan-before command (K-MB-4, J-C-31) (:110-111).
- **Conflicts / stale:** "UI v4 jumps Part 9 -> 21" wrong (07d).
- **Open items:** E1, E2.

### proposals/2026-10-28-content-architecture-suite/appendix_A5_events_and_arcs.md
- **What it is:** [READ PARTLY: verdicts :12-21, §4 :131-144 opened] Analyst report on Q7-Q8.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: reference.
- **Bears on:** WR, ARCS.
- **Content that matters:**
  - Table of how pieces relate: arc register is outside the sim ("never runtime data", B10-19:93); goal rows and ladders person-side (38 goal rows BUILT; ladders: schema planned B10-05, content 0); Tensions/scenario rows world-side at build then person-side; world forcing BUILT (control 1.0); chronicle/journal render outside sim (:133-139).
  - CL-THRUST B0.1 BUILT (`engine/season/harness/arc.py:123`) while `_part4:529` still says "Built so far: nothing" (:19).
  - Escalations: build a world Thread substrate (unlocks 7 arcs incl. all four lost), TS as tenth (unlocks family G, 12 arcs), who authors ~60 scenario/ladder seeds (:141-146).
- **Conflicts / stale:** `Vaynard A/B empty` is a transcription loss (07c correction 3).
- **Open items:** the three escalations.

### proposals/2026-10-28-content-architecture-suite/critic_lens3.md
- **What it is:** [READ PARTLY: findings 1-5 opened (:16-60); remaining findings :61-139 and the brief :140+ not] Lens-3 (directive compliance and completeness) critic report on the suite.
- **Status:** PROPOSED, HELD BACK IN FULL (:3). Reading: historical critic record.
- **Bears on:** PROCESS, CHAR, GO.
- **Content that matters:**
  - Finding 1: most of the 12-13 "rulings" are not plain choices; #12 and #13 closable by precedent (not Jordan's); count conflict 8 vs 13.
  - Finding 2: mass-battle command presented as decided though K-MB-4 is a research recommendation (`research/by_lane/MB_mass_battle.md:707`).
  - Finding 3: "matchup preview" at 02:60 contradicts the no-forecast directive.
  - Finding 4: B10-S placement stated three ways (after B10-10 / ahead of B10-10 / dossier position).
  - Finding 5: the suite "overrides Jordan's [strong] reading, then calls the override approved".
- **Conflicts / stale:** line refs in the critic report are to pre-split numbering.
- **Open items:** findings 6+ unread [UNVERIFIED].

### proposals/2026-10-28-content-architecture-suite/fragments_of_unrecovered_parts.md
- **What it is:** [READ PARTLY: head only] Verbatim surviving lines of the then-unrecovered part 06 and appendices A1/A3/A5.
- **Status:** PROPOSED, HELD BACK IN FULL (:3); itself superseded by the recovered files (00_INDEX :37). Reading: superseded.
- **Bears on:** PROCESS.
- **Content that matters:** nothing beyond the recovered files.
- **Conflicts / stale:** superseded; kept "only as a record of the second pass".
- **Open items:** none.

### proposals/2026-10-29-army-phase5-design.md
- **What it is:** [READ IN FULL] Phase-5 design note of ED-IN-0306 (army chain): the 11 behaviours phases 1-4 missed, each resolved by precedent/architecture, plus the headless military menu and preset orders of battle. 2026-10-29.
- **Status:** "PROPOSED (design reference; the code is the mechanism, CLAUDE.md §0.05)" (:3). Reading: live reference for the built army chain (`harness/military_menu.py`, `modules/mass_battle/troop_types/presets.py` are named as built [UNVERIFIED here]); every number is an ASSUMPTION Jordan may correct (:9).
- **Bears on:** MB, FA, SE, CORE, CHAR.
- **Content that matters:**
  - M1: shipped realm cannot field a surviving army: cohort weight 2 -> `under_arms_cap(2)` = 20 troops; engine routs a unit under 100 (`Unit.recalc_size`, `BLOCK_SIZE` 100) and a subunit under 80; fix `TROOPS_PER_WEIGHT` 100 -> 300 (Crown could raise 900, Church 60) (:15).
  - M2: "An army is where its commander is": an army Record's troops all take the field when its holder is present at the place; cohorts stay home, bodies carry losses (:16). M3: a cohort may be raised by the faction governing where it lives (`holder_faction_of`) (:17). M4: cap counts across every army (`world_q.raised_from`) (:18).
  - M5: a territory is arrival-only (`rosters.yaml: arrival_only_kinds`); `move`/`migrate` decline it, only `march` puts people there (:19). M7: walls belong to a settlement; a field at a territory has `fort_level` 0 (:21). M8: ration billed on weight of cohorts the army drew from (:22). M9: new verbs `disband_unit`, `discharge_troops` (:23).
  - M11 RULED (Jordan 2026-09, clause (b)): casualties only on the losing side; winners never depleted; recorded "so it is not rediscovered as a defect" (:25).
  - Preset orders of battle for AI factions: doctrine 45% heavy foot, 25% missile, 20% horse, rest levy; group under the 80-troop floor dropped; ships "OFF BY CONSTRUCTION" (nothing in the loop calls `install`); deterministic, no draw; AI general planner stays MB-08's (:36-44).
- **Conflicts / stale:** relation to Jordan's mass-battle intent (squad of named characters, weapon-carry trade-off, one path for player and auto-resolve) not addressed here; troop stock here is a cohort-derived pool, whereas the content suite's M3 asked for a counted stock (see content-architecture 01 part2 :53). `TROOPS_PER_WEIGHT=300` and the rout floors are [UNVERIFIED against current code].
- **Open items:** H-166 (who may take UNHELD land), a Godot screen, winner depletion (M11), legacy headcount quirk `effective_size / size_max` (:48-49).

### proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md
- **What it is:** [READ PARTLY: :4-62, :86-126, :174-259 opened; §6-8 not] Design (CR-38's design file) for a parliament and debate: a motion drawn from the world, a sitting that argues it, a result the loop can feel. 2026-10-29.
- **Status:** "PROPOSED (2026-10-29). Design only. Nothing here runs." and "SUPERSEDED IN PART by `2026-10-29-resolution-design.md`" which withdraws its Speaker, `determine` on the council seat and the minted `resolution`, the evade/defy route, and several blockers/calls (:4). §12 calls HELD BACK from ED-1094's merge default. Reading: partly superseded; §3, 5, 7, 8, 9 survive as reference.
- **Bears on:** SC, FA, CORE, WR, CHAR.
- **Content that matters:**
  - Ask (Jordan 2026-10-29): two or more characters debate a worldly topic from the season loop; result renders impact at the seam; a basis for parliaments at realm, duchy, province, territory "even if it is just a change in opinions" (:6-10).
  - "The ratified architecture already has the right shape for a parliament. The running engine does not yet have the parts" (:15). Council = ONE seat per rung, members = persons who `oblige` to it, a join is the joiner's own act (`AX §E.2.5`); a vote = count of live `commit`s computed on read (CR-34); an assembly never acts, it mints a document and the owning seat acts on it (CR-36 `resolution`, CR-37 `joint_concurrence`) (:17-27).
  - Sitting is season-granular because no round is stamped on an Event or Tenure (`effects_information.py:1166-1167`; `driver.py:531-535`); 9-step table summons -> salience -> tabling -> attendance -> speeches -> division -> declaration -> execution -> lapse; step 9 lapse is NEW (:41-62).
  - Why `argue`/`speak` cannot move a vote about the subject: `argue` rolls pool_default 2 vs obstacle_default 2, leverage always 0, on a win the hearer moves toward the arguer's whole pursuit profile and "the Proposition is never read" (`person_q.py:652-658`, `effects_information.py:575`); `speak` writes nothing (H-63); a voter's pursuit term `align(c.verb)` (`choose.py:149`) is identical for every `commit` (:110-122). Three proposed builds: speech carries predicate verb, voter weighs content, room hears body-speech.
  - Rung table: realm King/Queen with Dukes; duchy Duke with Counts; province Count with Lords; territory Lord with Mayors; the authored realm has no province rung (`offices.yaml:505`) (:176-182). Jordan's call: marquis appears nowhere in canon; ladder fixed by 2026-09-02 verbatim ruling (H-90).
  - Blockers B-1..B-13 with owners (:191-207), e.g. B-3 a computed `open_case`/`carry` names no arrangement (H-80); B-10 a `declared` determination still rolls (CR-34); B-12 computed `give` does not form (H-229). 9 falsifiers (:213-225). Build order PD-1 probe .. PD-7 sub-realm councils (:247-257).
  - Hash: "every pin stays EQUAL until flipped" is false; new `questions_for` stamp and new conjunct on `give` are declared MOVERS (:209-211).
- **Conflicts / stale:** superseded in part by resolution-design (above); CR-38's gate "still names this file as approved" (:4). Line refs to `world_q.py`, `gate.py` are as of 2026-10-29 and may have drifted [UNVERIFIED].
- **Open items:** Jordan's calls 1-5 (titles, how far a parliament binds T3a vs T3b, chair/ruler separation, a motion losing on dice after carrying, debate depth) (:233-243); unverified: whether anyone hears a realm-venue `date.fired` first-hand, whether `convene` is in the King's grant (:231).

### proposals/2026-10-29-parliament-and-debate/2026-10-29-debate-corpus-by-theme.md
- **What it is:** [READ PARTLY: status, counts, lane table, reading key, headings, first A/CODED entries; the 757 entries not read line by line] Extraction of 757 mechanism/rule/finding entries from 7 lanes (CD coded 110, PR proceedings design 109, OP other proposals 110, GV governance 107, CL classical rhetoric 108, HP historical politics 108, NL emergent narrative 105), sorted into 13 themes; part 1 holds themes A, B, D, J, L. 2026-10-29.
- **Status:** "REFERENCE (2026-10-29). An extraction, not a design ... the gatherers extracted and classified, they did not judge" (:3). Reading: reference; the adjudication lists entries it found stale or wrong.
- **Bears on:** SC, FA, WR, CHAR.
- **Content that matters:**
  - Themes: A agenda/salience (42 entries), B convening/venue/procedure (97), D judgment/voting (76), J record/memory/reputation (23), L architecture constraints (32); C argument (147), E negotiation (53), F faction/patronage (28), M persons as inputs (18); G outcome/binding (59), H transfers (33), I disorder (28), K emergent narrative (121) (headings :56, :213, :535, :794, :888; part2/3 headings).
  - Class order: CODED, RATIFIED, INTENT, PROPOSED, ARCHIVED, NOTCODED, RESEARCH, CLASSICAL, HISTORICAL, GAME, NARRLIT (:7-23).
  - Code-surface entries worth an auditor's use: CD-019 `open_case` (puts a person-matter before the room, fills nearest open docket slot, `verb_table.yaml:958`), CD-020 docket item shape `{date, matter, arrangement, petition}` (`world_q.py:193,246,258`), CD-021 `carry` as the one seatless route to the docket (`verb_table.yaml:108`), CD-022 petition closers withdraw/deny not built (H-75), CD-023 `convene` (no invitation, summons or attendance list exists).
  - Lane gaps: CD lane found no vote/tally, Parliament seat, chair, order of speech, minutes, negotiation, tax/levy verb, bribery, veto in code (:40).
  - Scope note: the proceedings subsystem build is scope-banned from earlier social-contest work (README of `2026-09-05-proceedings-subsystem`); this survey does not lift it (:5).
- **Conflicts / stale:** line cites to `engine/season/*` are as of 2026-10-29 and have drifted [UNVERIFIED]. The proceedings README ban may conflict with Jordan's present directive to read everything.
- **Open items:** entries flagged stale/wrong in the adjudication's §6.

### proposals/2026-10-29-parliament-and-debate/2026-10-29-debate-corpus-by-theme_part2.md
- **What it is:** [READ PARTLY: status, headings, M/CODED entries CD-088/089/050] Corpus part 2: themes C (argument and persuasion, 147 entries), E (negotiation, 53), F (faction/patronage, 28), M (persons as inputs, 18).
- **Status:** REFERENCE (2026-10-29), continues part 1 (:3). Reading: reference.
- **Bears on:** SC, CHAR, FA.
- **Content that matters:**
  - CD-088/089: the kernel's per-side trackers (Standing/Face 0-10 with Face_max = Charisma x 3, Reserve 12 points, Room, Readiness) and the judge-armature (four-axis vector evidence/consequence/authority/insinuation) are NOT adopted (SC-05, ED-SC-0033); nothing in `engine/season` reads a judge's vector (:784-800).
  - CD-050 (ED-SC-0035, Jordan 2026-09-06): a want is a live commit to an OUGHT Proposition; fears pressed not spent; second-person lever refused (no creditor verb, T-m not amended); standing-gap pressure built but never fires in realm play (H-222).
  - Theme C contains 31 RESEARCH and 26 CLASSICAL entries (:7).
- **Conflicts / stale:** as part 1.
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/2026-10-29-debate-corpus-by-theme_part3.md
- **What it is:** [HEADINGS+HEAD ONLY] Corpus part 3: themes G (outcome, binding, enforcement, 59), H (transfers of land/office/asset, 33), I (disorder and failure modes, 28), K (emergent narrative and churn, 121 incl. CODED 16, RATIFIED 8, PROPOSED 28, NOTCODED 10).
- **Status:** REFERENCE (2026-10-29), continues part 1 (:3). Reading: reference.
- **Bears on:** SC, WR, FA, SE.
- **Content that matters:**
  - Theme K is the largest by entries (121), the home of the churn principle and the 42-source emergent-narrative corpus (NL lane) (:454).
  - Theme H (ARCHIVED 13 of 33) is mostly archived parliamentary-transfer design (:215).
- **Conflicts / stale:** entries not opened [UNVERIFIED].
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/2026-10-29-debate-fit-adjudication.md
- **What it is:** [READ PARTLY: :4-43 opened; §3-8 headings only] Three Opus adjudicators judged the 757 corpus entries against NERS and the churn principle with six verdicts (FITS, FITS-IF-ADAPTED, PARTIAL, MISFIT, ALREADY-HELD, HELD-FOR-REASON).
- **Status:** REFERENCE (2026-10-29): "a verdict here says whether a mechanism fits ... never that someone should build it" (:3). Reading: reference; its fit verdicts are the basis of the resolution design.
- **Bears on:** SC, FA, CHAR, WR.
- **Content that matters:**
  - Five facts decide most verdicts (:9-21): (1) no persuasion mechanism changes a vote about a subject (`argue` never reads the Proposition; voter's pursuit term reads only the verb; everyone argues at pool 2; 1 of 430 persons holds any capability; `person_q.py:638-658`, `effects_information.py:555-581`); (2) delivery does not form (computed `give` of a Rung: 0 cessions in 143 worlds, H-229); (3) persons do not differ in risk or horizon (no term, no `Person` carrier though Jordan ruled they differ); (4) a motion cannot end and silence is free; (5) of 13 arrangement keys only `disposes` has a runtime reader.
  - Best shapes: council = ONE seat with members by `oblige` (holds from all six NERS directions); a vote = count of live `commit`s declared by a later act (ED-SC-0034, CR-34); witnessed claims as institutional memory; `carry`/petition as the seatless route (:25-31).
  - Binding strength: "negative concurrence plus a witnessed held record", not obligation; H-90 and canon deny unilateral power, none grants command to the assembly (:40).
- **Conflicts / stale:** the `bench_quorum` of 1 means the quorum cannot refuse (noted in-line).
- **Open items:** see parts 2-4.

### proposals/2026-10-29-parliament-and-debate/2026-10-29-debate-fit-adjudication_part2.md
- **What it is:** [HEADINGS+HEAD ONLY] Verdicts for themes A, B, D, J: e.g. A1 docket ALREADY-HELD; A2 petition/carry ALREADY-HELD; A7 player-as-government policy sim MISFIT; B3 council one seat ALREADY-HELD; D2 vote as count of commits ALREADY-HELD (ratified; unbuilt); D4 faction-stat parliaments, D5 kernel win conditions, D8 sortition MISFIT; D6 first defector, D7 veto FITS-IF-ADAPTED; J3 witnessed claims ALREADY-HELD.
- **Status:** REFERENCE (2026-10-29) (:3). Reading: reference.
- **Bears on:** SC, FA.
- **Content that matters:** headings give the verdict per cluster (:28-157); section 6 "Verification" lists opened sources at `d90b6e8d` (:197); section 5 ranks clusters by fit (:162).
- **Conflicts / stale:** none verified.
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/2026-10-29-debate-fit-adjudication_part3.md
- **What it is:** [HEADINGS+HEAD ONLY] Verdicts for themes C, E, F, M.
- **Status:** REFERENCE (2026-10-29) (:3). Reading: reference.
- **Bears on:** SC, CHAR, FA.
- **Content that matters:** C1 two tracks ALREADY-HELD; C2 "logos on the motion" FITS-IF-ADAPTED; C7 Nyaya defeat catalogue and C10 kernel armature MISFIT; C11 social proof FITS-IF-ADAPTED; C13 lies and concealment FITS; E2 BATNA FITS-IF-ADAPTED; M3 risk appetite and horizon HELD-FOR-REASON (:37-151).
- **Conflicts / stale:** none verified.
- **Open items:** M3 awaits CR-17.

### proposals/2026-10-29-parliament-and-debate/2026-10-29-debate-fit-adjudication_part4.md
- **What it is:** [HEADINGS+HEAD ONLY] Verdicts for themes G, H, I, K, including §0.1 "Land/asset transfer as a social-contest outcome: persons through seats, holding a document" and K "what narrative theory requires".
- **Status:** REFERENCE (2026-10-29) (:3). Reading: reference; verification opened a sibling checkout `C:\Github\ttrpg-parliament` (:235).
- **Bears on:** SC, SE, FA, WR.
- **Content that matters:** the group's question "can a motion affect the world, and how hard should it bind?" (:9); clusters G (:41), H (:122), I (:158), K (:172); ranking (:223).
- **Conflicts / stale:** none verified.
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/2026-10-29-resolution-design.md
- **What it is:** [READ PARTLY: :1-76, :99-128, :174-212 opened; §2A measurements, §4-6, §9-10 not] Design of how debate and parliament change the world, revised after two blind passes: chain I1-I12 (world->topic, topic->room, summons, room->members, speech->hearer, hearer->vote, the count, count->licence, licence->owner's act, act->world, memory, stability).
- **Status:** "PROPOSED (2026-10-29), revised after two blind passes. Design only. Nothing here runs" (:3); Jordan's calls "taken provisionally" on his instruction "resolve for me for now" (2026-10-30), each with a revert (:4). Reading: supersedes parts of `2026-10-29-parliament-and-debate.md` (:6); live reference for CR-38.
- **Bears on:** SC, FA, CORE, CHAR, WR.
- **Content that matters:**
  - Decided by Jordan 2026-10-29: counted vote becomes an outcome by "licence by count": no new verb, no declaring act, C-7/ED-SC-0034 untouched (:176).
  - Motion = a petition Record naming a Proposition, tabled by `carry` into the nearest open slot; docket item is person-less `{date, matter: None, motion, file}`; count = share of sworn non-imposed council members holding a live `commit` made in a later season than tabling, starting 0.5 swept {0.5, 0.6, 2/3}; absent or abstaining is not an aye (I2, I7).
  - New `binds` basis `council` with its rule at all three sites reading sworn edges (`purview_reaches`, `guard_weight`, `admits_audience` limb 3) (I4). A fourth `score_terms` summand `motion` is a named Layer-1 amendment (`architecture/ARCHITECTURE_V2.md` §F2 D21) (RJ-layer1).
  - Consent rows as data: (executing verb, object kind, council seat, threshold); one starting row: a holder's `give` of his last territory (RJ-consent). No chair: council seat is an unheld container; any `convene`-holder at the council's rung may call it (RJ-chair).
  - Risk and horizon deferred to CR-17 (ED-IN-0304, `registers/editorial_ledger_in.jsonl:91`) (RJ-layer1 b).
  - Weakest points (§8): the licence cannot compel and does not yet check a ruler; the slice does not make the realm debate; 21-23 sittings/run but 11-17 empty; the design itself was never run; an altitude review noted a cheaper alternative (motion as docket matter via `carry`'s `_docket_item`) not compared (:199-210).
- **Conflicts / stale:** the `_ch_chronicle` summons channel is built on the refused echo model and scheduled for deletion; contract is channel-agnostic (:56).
- **Open items:** RJ-11 played debate; LP4/LP5/LP7 loops measured not prevented (I12).

### proposals/2026-10-29-parliament-and-debate/2026-10-29-reasons-to-convene.md
- **What it is:** [READ PARTLY: :9-19 opened; §1-8 not] Measured analysis (read-only out-of-tree probes at `120b3bf7`, seeds 0-2, unreproduced) of why `convene` has no reason and sittings are empty.
- **Status:** REFERENCE (2026-10-29): "a judgment about the engine as built, not a plan" (:3). Reading: reference; instruments "unreproduced" (:114).
- **Bears on:** SC, WR, CORE, FA.
- **Content that matters:**
  - Per four-season run: 21-23 sittings scheduled (12-17 fire) vs 4-9 person-matters waiting; 0-1 waiting matter placed in a slot; 11-17 sittings empty (:11).
  - `convene` forms on a "places-to-settle" stamp, not a venue where a matter waits; a sitting at a hearth-tier rung can hear only matters at that hearth (`slot_for` walks up) (:12-13).
  - Matter in a convener's top five questions in only ~14-20% of covering pairs; a convener faces 700-1,200 `claim_landed` questions vs 32-39 `need` per season (:14).
  - Seven levers in §6; three carry most leverage: put the convener's referent on the tier where a matter waits; manufacture demand by making some acts need a count; give strained matters a producer (:16).
  - Terms correction from Jordan: "rung", "tier", "venue" (§1 :20).
- **Conflicts / stale:** RL1/RL2 became CR-56 in the ratified build-all plan.
- **Open items:** the levers' falsifiers (§6).

### proposals/2026-10-29-parliament-and-debate/2026-10-30-lopsided-outcomes-inquiry.md
- **What it is:** [READ PARTLY: :2-30] Explains one stress-test finding (kernel proceedings lopsided) by two probes `lopsided_mechanism.py` and `lopsided_levers.py` and their logs.
- **Status:** none stated; "Reference, not a plan ... dies with the kernel it describes" (:2). Reading: reference about the NOT-adopted kernel.
- **Bears on:** SC, DICE.
- **Content that matters:**
  - The stress test's "weaker side share of decided contests" was measured with both sides on the logos-only policy, bare-integer sides, and conditioning on "decided" hides the middle (faculty 1 v 4 formal_contest: committee 85.3%, stronger 14.7%, weaker 0.02%) (:17-25).
  - Faculty->degree is concave (mean reception degree 1.06, 1.48, 1.83, 2.13, 2.31, 2.38, 2.49 for faculty 1..7); fixed obstacle `Venue.base_ob = 2.0` (`resolver.py:157`) faces every roll (:27-33).
- **Conflicts / stale:** kernel still exists in tree (`systems/social_contest/sim/contest/` present at my check).
- **Open items:** rest of the mechanism analysis unread [UNVERIFIED].

### proposals/2026-10-29-parliament-and-debate/2026-10-30-social-contest-armature.md
- **What it is:** [READ PARTLY: :4-55, :285-310, :358-367 opened] The "armature" of a social contest: a venue row, a matter, a sequence of acts, each act one draw; plus one commensurable scale. Producer's draft with a critic pass reconciled (§I).
- **Status:** PROPOSED (reference; resolves nothing) (:3). Reading: the shared base of proposals 1-4; its §I corrections "outrank" it.
- **Bears on:** SC, DICE, CHAR, FA.
- **Content that matters:**
  - Armature: row names authority, decider (target/parties/bench/count), admitted acts, weights, reach, appeal route; draw = one sigma-leveraged continuous roll with three channels (dice = what actor holds; obstacle = other side's score / 2; leverage = what lies between) (:15-39).
  - Common scale: `E[m] = 0.4*N + 0.8*sqrt(N)*softcap(s) - Ob`, spread `0.8*sqrt(N)`; at 5D one die ~ 0.25 sigma ~ 0.4 Ob (:36-40).
  - Questions for Jordan G1-G6: ceiling value (R-37), Layer-1 §A.3 wording for office weight, count weights (one seat one vote vs office-weighted), equals (R-5's /2 means an act against an equal fails 61% at 5D, 65% at 10D), what R-40's "5D" counts, where circumstantial leverage sits (:285-367).
  - `soft_cap` is `1.5*tanh(s/1.5)`, so s=1.5 gives only 1.14 sigma (`sigma_leverage.py:104,148,202-203`) (:299).
- **Conflicts / stale:** G1 first recommended deleting the ceiling; critic found grounds wrong, so the ruling R-37 stands.
- **Open items:** G1-G6.

### proposals/2026-10-29-parliament-and-debate/2026-10-30-social-contest-code-audit.md
- **What it is:** [READ PARTLY: :4-46, :94-125 opened] Comparative audit of the SC code against the 13-item model and kinds; three readers took code only.
- **Status:** PROPOSED (reference; resolves nothing, schedules nothing) (:3). Reading: reference; live-code claims as of 2026-10-30.
- **Bears on:** SC, DICE, FI, CORE.
- **Content that matters:**
  - Live path: `resolve._contest` -> `seam/contest.py::contest` -> `sigma.resolve` -> `modules/social_contest/roll.py::roll` -> `degree_from_net`; logged rolls all `pool=2`, `opposition=None`, `leverage=0.0`, `ob=2.0`; pool cast `int(...)` at `sigma.py:131`; at 2D vs Ob 2: Failure .744, Partial .187, Success .070; leverage 0.25..1.0 identical to 0.0 (:16-24).
  - Execution table over seeds 0-2 two seasons: `tell` runs (3-13 `news.told`); `speak` refused `speech.unheard` 13-34 times, rolled 0-4, writes `[]`; `argue` rolled once across six runs; `determine` never emitted `matter.determined`; `arrest` never (:26-34).
  - `arrangements.yaml`: 8 rows x 13 keys, all 8 `disposal: bench`; 12 of 13 keys have no non-test reader; only `disposes` read (`effects_information.py:336,521`; `state/gate.py:257`); six speech kinds loaded, no reader (:36-42).
  - Kernel is a separate system the game never reaches; only non-test caller `degree_extension.py`, called by three tests (:44-46).
  - Lacking, ranked (§4): the pool, continuous dice/obstacle, modifier sources, action surface limits, authority basis, count, Partial writes docket, reasons to convene, appeal, mutual and count structures (:94-107).
- **Conflicts / stale:** the module `social_contest/` still has `roll.py`; `def faculty` now exists at `engine/season/seam/wrappers/pool.py:78`, so "no capability producer" is partly stale [VERIFIED by grep].
- **Open items:** §5: ceiling value, Layer-1 §A.3 wording, R-34 mechanism.

### proposals/2026-10-29-parliament-and-debate/2026-10-30-social-contest-how-contests-occur.md
- **What it is:** [READ PARTLY: :13-32 opened] Answer to how a social contest occurs: the armature (four parts) is the structure; classical and modern persuasion theories explain what feeds the draw (Aristotle, Cicero/Quintilian, contemporary persuasion, other traditions).
- **Status:** PROPOSED (reference; resolves nothing, schedules nothing) (:3). Reading: reference.
- **Bears on:** SC, CHAR.
- **Content that matters:** four parts (venue-limited action surface R-33; one draw per act R-5/6/22/32; decider converting acts to disposal R-12/34 scaled by legitimacy R-36; world learns it at news speed R-21 and appeal goes to another authority R-35) (:15-31). Theories mapped to draw inputs (§2).
- **Conflicts / stale:** none.
- **Open items:** §4 "what is ruled, what is the repo's, and what is mine".

### proposals/2026-10-29-parliament-and-debate/2026-10-30-social-contest-kinds-of-contest.md
- **What it is:** [READ PARTLY: :1-20 opened] Descriptive survey of the contest kinds in the kernel (8 proceedings) vs the live module (5 contesting verbs + 3 graded inquiries); includes measured die/sigma worth (§7).
- **Status:** no Status line; "Reference, not a plan (CLAUDE.md §0.05) ... dies with the code it describes" (:3). Reading: reference.
- **Bears on:** SC, DICE.
- **Content that matters:** two systems share the name (kernel `systems/social_contest/sim/contest/`, not adopted SC-05, vs `modules/social_contest/roll.py`, one draw returning a `Margin`); numbers are for bare-integer logos-only sides (:5-19).
- **Conflicts / stale:** companion to stress report and lopsided inquiry.
- **Open items:** §8 "Not shown".

### proposals/2026-10-29-parliament-and-debate/2026-10-30-social-contest-primitives-and-kinds.md
- **What it is:** [READ PARTLY: :4-21, :105-119, :397-413 opened; §1 rulings R-1..R-41 and §2-5 not] Thirteen-reader survey of the whole SC corpus: Jordan's rulings in date order (R-1..R-41, S-1..S-8), flattened primitives, the eight kinds, gaps.
- **Status:** PROPOSED (reference; resolves nothing, schedules nothing) (:3). Reading: reference, but its R-n / S-n ruling numbers "outrank everything" in the later proposals.
- **Bears on:** SC, DICE, CHAR, FA.
- **Content that matters:**
  - Precedence: Jordan's rulings first, code second, proposals third, research last (:19-21).
  - Tensions among rulings: R-2 (no immediate contest after render) vs appeal to an authority (resolved by R-35); kernel adopt/retire (R-14 retire, SC-05 lean adopt); R-31 vs Layer 1 `03` §A.3 "A seat adds no verb and no modifier" answered "both" by Jordan 2026-10-30 (:105-112).
  - Still open on Jordan: D-6, D-7, J-C-6 (may a person lie), J-13 (what sets a pool), source of risk appetite and horizon (CR-17) (:113).
  - Gaps: three resolvers share one name; "kind" used at four levels; the research sits in quarantined `.designs/` and `.audit/`; Venice/Inquisition covered at the level of offices not trials; Cicero/Quintilian thin; church tribunal seat-A share reported as 84.5/84.2/84.7% in three documents (:397-413).
- **Conflicts / stale:** `module_contracts.yaml` still says the kernel is reached only via `emergency_council` (:411).
- **Open items:** the "13-family catalog of pre-1600 decision procedures" cited at `research/fa_se_historical_precedent_research_v1.md:75-77` has no file (:409).

### proposals/2026-10-29-parliament-and-debate/2026-10-30-social-contest-proposal-1-one-draw.md
- **What it is:** [READ PARTLY: :4-22 and headings] Proposal 1 "One draw, one roster": a speech is one act priced by aptness; kinds are rows; authority is a key; reception moves out of the draw into the decider's own choice; typed `Dice`/`Obstacle`/`Leverage` sub-records and a `weights:` column.
- **Status:** PROPOSED (reference; resolves nothing, schedules nothing) (:3). Reading: reference; the comparison picks it as the best base.
- **Bears on:** SC, DICE, CORE.
- **Content that matters:** fewest new objects; deletes more vocabulary than it adds (NERS 1st); replaces `_pool_of`, `_opposition_of`, room terms and capability map with one source roster (UP §1); sections 4 (eight kinds through it), 5 (keeps/changes/deletes), 8 (departures, questions) exist for look-up.
- **Conflicts / stale:** stress test: legitimacy index L near zero (Church L = 0 in 14 of 17 territories) and circular; appeal `void` cannot close edges; regard link flips decided outcome 0/197; R-11 many matters per party fails (1 of 50 docketed) (`2026-10-30-stress-test-proposal-1.md`).
- **Open items:** whether "audience" is a draw modifier (R-32) or an input to the decider's own choice.

### proposals/2026-10-29-parliament-and-debate/2026-10-30-social-contest-proposal-2-staged-proceeding.md
- **What it is:** [READ PARTLY: :4-22 and headings] Proposal 2 "Staged proceeding": a venue row lists stages as data (e.g. admit, forum, plea, proof, quality, judgment); position lives on a seizable case file Record.
- **Status:** PROPOSED (reference; resolves nothing, schedules nothing) (:3). Reading: reference; comparison says wait on it (rank NERS 3rd).
- **Bears on:** SC, FI, CORE.
- **Content that matters:** most procedural fidelity; a forensic row costs ~6 closing acts and an adjournment a season; its plea is weakly dominated; stress test: case-file claim true only of MATTER's maturation of a stage, `determine` never reads the file, `forge` cannot forge it, `create_record` overwrites the agenda for 3 of 3 actors (`2026-10-30-stress-test-proposal-2.md`).
- **Conflicts / stale:** S2 moves every computed roll (golden count low).
- **Open items:** Q1-Q3 (one-season hearings, case-file seizing, unwatched contests R-24).

### proposals/2026-10-29-parliament-and-debate/2026-10-30-social-contest-proposal-3-authority-first.md
- **What it is:** [READ PARTLY: :4-22 and headings] Proposal 3 "Authority first": an authority (parties, polity, church) is a grouping of offices by faction (`authority.by_faction`) with a per-territory legitimacy index; forum contest, custody as warrant, appeal to another authority, lay assessors.
- **Status:** PROPOSED (reference; resolves nothing, schedules nothing) (:3). Reading: reference; comparison takes its institutional readers (authority grouping, bench by authority, custody-as-warrant, appellate closure) and defers forum, assessors, index.
- **Bears on:** SC, FA, WR.
- **Content that matters:** 31-seat grouping 19 polity / 7 church / 5 party-only recomputes exactly; church commit share 7 commits, 6 at T9; case-opening reads `Office.rung` not `scope_rung` so church seats open 0 of 19 in T1 (stress P3); `defy` dominates.
- **Conflicts / stale:** opens the cross-ledger question (ED-SC-0040) a second time; legitimacy `opinion_of` reads exactly 0.50 for all four factions in 8 of 16 territories.
- **Open items:** Q1 church judging reach (`scope:`), Q2 F8 index, Q3 "royal person involved", Q4 church appeal destination.

### proposals/2026-10-29-parliament-and-debate/2026-10-30-social-contest-proposals-comparison.md
- **What it is:** [READ IN FULL: :4-157] Three-assessor comparison of P1-P3 on NERS, emergent narrative and season-loop compatibility, plus §9 added 2026-11-01 for P4 and a revised recommendation.
- **Status:** PROPOSED (reference; resolves nothing, schedules nothing) (:3). Reading: reference; the narrative thread leading to the RATIFIED build-all plan.
- **Bears on:** SC, CORE, FA.
- **Content that matters:**
  - Ranks: NERS P1>P3>P2; emergent narrative P3>P2>P1; season-loop fit P1>P2>P3. "All three proposals are paper": dead core = computed `open_case` names no arrangement (`effects_information.py:319-325`), `determine` has executed 0 times in computed play, a speech does not reach its judgment, computed petition addressed to its subject (H-94), not acting emits no Event, no capability authored (:56-71).
  - Overturned claims: act admission belongs in `loop/resolve.py::_eligible` and `data/requires.py` not `state/gate.py` (gate refusal raises `NotYours`, kills the season); `judging_set` and `may_determine` must be one test; deleting the kernel breaks `engine/tests/test_sigma_leverage_parity.py:52` (:74-100).
  - Recommendation: adopt P1 base + P3 readers (authority grouping, custody as warrant, appellate closure) + P2's case file later; reject P2 pleading as designed and P3 authority classification as an object (:107-120).
  - Revised (with P4): dead core first; portable repairs (MATTER `due <= tick`, `determine` requires a held case file, case-opening reads `scope_rung`, citation as `issue`d writ, one `may_determine` predicate, `scope` key, warrant duty); P4 choice layer cut back; "about five robust choices" (:141-157).
- **Conflicts / stale:** the shared "first work" list is now in the ratified plan as CR-55..CR-67.
- **Open items:** seven Jordan decisions (§6).

### proposals/2026-10-29-parliament-and-debate/2026-10-30-social-contest-reconciliation-and-distillation.md
- **What it is:** [READ PARTLY: :4-14 and headings] Reconciles conflicts among corpus claims by the §0 five-step ladder and distils a 13-item model; "Eight kinds become four"; edits to existing artifacts.
- **Status:** PROPOSED (reference; resolves nothing, schedules nothing) (:3). Reading: reference.
- **Bears on:** SC, PROCESS.
- **Content that matters:** §2.3 "what survives all five (for Jordan)" (:77); §3.1/3.1a the 13-item model incl. R-31..R-33 (:145-170); §3.2 eight kinds to four (:171); §3.3 what is cut (:186); §3.5 research as supplier of rows not mechanisms (:221); §4 edits (:245).
- **Conflicts / stale:** suggested narrow Layer-1 wording ("a seat adds no verb and no modifier of itself; a venue row may license an office-keyed act set and weight") is Jordan's to accept (G2).
- **Open items:** §2.3 items.

### proposals/2026-10-29-parliament-and-debate/2026-10-30-social-contest-unification-plan.md
- **What it is:** [READ IN FULL: 66 lines] Draft orchestration to unify SC: one roster of contest sources (producer, side, venue_key), eight batches B0-B7 with deletion first.
- **Status:** "PROPOSED (reference; resolves nothing; adopts nothing; it is a draft for one adversarial pass)" (:3). Reading: superseded in practice by the P1 base and the ratified CR-55..CR-67 plan.
- **Bears on:** SC, CORE, PROCESS.
- **Content that matters:**
  - Roster rows: `source`, `side` (pool or obstacle, declared once = double-counting rule), `producer`, `venue_key` (:16-29).
  - Batches: B0 settle (four Jordan rulings), B1 delete free cuts (kernel 18 files, 12 unread arrangement keys), B2 one engine (continuous pool, remove `int` cast at `sigma.py:131`), B3 action surface, B4 authority, B5 deciders, B6 reach, B7 rows (:36-45).
- **Conflicts / stale:** kernel file count 18 vs 16 tracked (stress comparison).
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/2026-10-30-stress-test-comparison.md
- **What it is:** [READ PARTLY: :4-40] Verdict across the three proposal stress tests (executable models on the real engine, logs ~4,250 lines).
- **Status:** REFERENCE (a terminal pass; queues no work) (:3). Reading: reference.
- **Bears on:** SC, CORE.
- **Content that matters:** "No proposal survives its stress test intact. Each one's arithmetic held and each broke on existing code" (:12). Common failures: first batch not green (kernel deletion breaks 6-7 test files incl. `test_sigma_leverage_parity`); legitimacy R-36 has no live content (seeds 0,1,2 build the same realm: n = 1); second case on a docketed matter refused; no appeal path; King/Queen on 319 of 319 non-empty benches; computed play never determines; capability authored for nobody (0 of 83); 7 of 18 spot-checked citations drifted ~25 lines (:15-26).
- **Conflicts / stale:** same-realm-for-every-seed finding bears on every multi-seed claim in the repo [flag for CORE].
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/2026-10-30-stress-test-proposal-1.md
- **What it is:** [READ PARTLY: verdict and ledger rows 1-10] Stress test of P1 (harness `stress_p1*.py`, logs `stress-log-p1-*`).
- **Status:** REFERENCE (2026-10-31), terminal pass (:3). Reading: reference.
- **Bears on:** SC, DICE.
- **Content that matters:** all 17 quoted probabilities reproduce; closed form holds for N >= 1 and breaks below 1D (engine floors mean and spread at 1D); L = 0 in 14 of 17 church territories (Church 7/83 = .084); regard link flips decided outcome 0/197; `void` appeal breaks 3 ways; 50 matters one party leaves 1 docketed.
- **Conflicts / stale:** none.
- **Open items:** ~148 roll-call lines unread.

### proposals/2026-10-29-parliament-and-debate/2026-10-30-stress-test-proposal-2.md
- **What it is:** [READ PARTLY: verdict and ledger rows 1-6] Stress test of P2.
- **Status:** REFERENCE (2026-10-30), terminal pass (:3). Reading: reference.
- **Bears on:** SC, FI.
- **Content that matters:** case-file claim true of MATTER stage maturation only; holder return does not resume (stage due during absence never matures: `matter.py` matures only at `due == w.tick`); `determine` still executes after `destroy_record`; `forge` refused; `create_record` overwrite 3/3 actors (:6-14).
- **Conflicts / stale:** none.
- **Open items:** remaining ledger and 76 roll-call lines unread.

### proposals/2026-10-29-parliament-and-debate/2026-10-30-stress-test-proposal-3.md
- **What it is:** [READ PARTLY: verdict and method] Stress test of P3 (real seasons 8 each at seeds 0-2, 540 s budget).
- **Status:** REFERENCE (2026-10-30), terminal pass (:3). Reading: reference.
- **Bears on:** SC, FA.
- **Content that matters:** counts honest, mechanism not buildable as written; 31-seat grouping recomputes; 11 of 14 legitimacy figures reproduce; `determine` attempted 65, executed 3 (all `matter.undetermined`), `arrest` attempted 4 all refused (comparison §4 E4).
- **Conflicts / stale:** none.
- **Open items:** roll-call unread.

### proposals/2026-10-29-parliament-and-debate/2026-10-30-stress-test-report.md
- **What it is:** [READ IN FULL: :4-77] Stress test of the SC module, the kernel and the season-loop debate surface, with logs.
- **Status:** REFERENCE (2026-10-30), terminal pass (:3). Reading: reference.
- **Bears on:** SC, CORE, DICE.
- **Content that matters:**
  - Module `roll.py`: 75,132 edge inputs, no undocumented exception, monotone in pool and opposition; NaN/inf not refused (7,844 NaN `net` trials) (:23-27).
  - Kernel: 751,619 resolutions no crash; draws from process-global RNG in 86% of resolutions; empty `Panel` raises `ZeroDivisionError`; proceedings lopsided (weaker side share: casual_dispute 21.6% ... formal_contest 0.04%); church_tribunal seat A wins 84.2% (:29-34).
  - Season loop seed 0, 13-14 seasons: 0-1 matters determined, 4 commitments, 0 arguments; season cost grew 11.7x (33 s to 387 s); docket 5 -> 72 items, 43 empty slots never filled; `question_aggregation_rule=all` collapses sittings (3 vs 51 dates) (:35-41).
  - Seed 0 twice: identical `content_hash` `920da131...` (:37).
- **Conflicts / stale:** native Windows test failure from path separators (:44).
- **Open items:** one seed only; kernel is a candidate not shipped.

### proposals/2026-10-29-parliament-and-debate/2026-10-31-stress-test-attribution.md
- **What it is:** [READ PARTLY: :4-40 opened] Terminal pass sorting the stress reports' findings into engine-side (stands with every proposal deleted), proposal-side, seam and instrument.
- **Status:** REFERENCE (2026-10-31), terminal pass on PR #536's reports (:3). Reading: reference.
- **Bears on:** SC, CORE.
- **Content that matters:** engine-side table E1-E16: E1 `open_case` refuses second case on a docketed matter (deliberate, `effects_information.py:355-368`); E2 no appeal path (`void` not in `DISPOSABLE_KINDS`; `pardon` closes only edges whose object is the exercised seat, `effects_governance.py:335-349`); E4 computed play reaches no determination (`docket_named_arrangement` 0 in 24 seasons); E5 MATTER matures only at `due == w.tick` (`matter.py:339-345`); E8 `open_case` reads `Office.rung`; E12 nothing ties a seat's authority to a row; E16 kernel removal reddens 6-7 files, `module_contracts.yaml:448-470` row load-bearing; C1 seeds 0,1,2 build the same realm (:17-40).
- **Conflicts / stale:** engine line cites drift.
- **Open items:** content table C1+ not read.

### proposals/2026-10-29-parliament-and-debate/2026-11-01-probe-controls-seed0.json
- **What it is:** [READ PARTLY: top-level keys] Output of `probe_controls.py` seed 0, 4 seasons: controls C1 comply/evade-defy by subject and whether the actor held a writ, C2 holders of forged sheets, C3 docket items with both date and matter, C4 opinion_of spread at tick 0 vs end, C5 confidence differences.
- **Status:** none (data); frozen probe output read by nothing.
- **Bears on:** SC, CORE.
- **Content that matters:** keys `C1_comply_evade_by_subject`, `C1_held`, `C1_dispensation_addressee`, `C3_docket_items_with_date_and_matter_at_each_season_end`; opinion spread identical at tick 0 and end (cited in companion §1 point 4).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/2026-11-01-probe-event-kinds-seed0.json
- **What it is:** [READ PARTLY: keys] `probe_event_kinds.py` seed 0, 4 seasons: `event_kinds`, `resolved_acts_by_verb`, `docket`, `dates`, `commits_live`, `commit_objects_mood`.
- **Status:** none (data).
- **Bears on:** SC, WR.
- **Content that matters:** among event kinds containing matter/compliance/argument: `compliance.impossible` 67, `matter.turned` 3, `matter.advanced` 1; no `matter.determined` (my python read).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/2026-11-01-probe-event-kinds-seed1.json
- **What it is:** [READ PARTLY: keys] Same probe at seed 1 (companion cites `determine.refused` 13, `comply`/`evade` 43 impossible).
- **Status:** none (data).
- **Bears on:** SC.
- **Content that matters:** same key set as seed 0.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/2026-11-01-probe-matters-intake-seed0.json
- **What it is:** [READ PARTLY: keys] `probe_matters_intake.py` seed 0, 4 seasons: questions per season, first-question source, ledger claims by predicate stem, claim source, docket items, `docket_with_arrangement`, records by kind, Propositions by mood.
- **Status:** none (data). Script notes: key `stamped_class_on_first_question` lists referent ids not classes, "a mislabel, left as run".
- **Bears on:** SC, CHAR, WR.
- **Content that matters:** companion cites 15,600 claims, 15,642 `claim_landed` questions vs 495 `need`, 258 of 261 Propositions OUGHT, none of 10 matter-holding docket items named a row.
- **Conflicts / stale:** mislabelled key.
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/2026-11-01-probe-routes-hand-built.json
- **What it is:** [READ PARTLY: keys] `probe_routes_hand_built.py` on the `test_u7_remit.py` hand-built bench world: Part A first Partial determination (who holds the claim, questions, disposal edge, judge's pursuits, second determine, non-person matter), Part B by band.
- **Status:** none (data).
- **Bears on:** SC, CHAR.
- **Content that matters:** the hand-built control showing routes 1 and 2 close when `determine` fires; legitimacy estimate of a judge +0.02 to +0.066 (cited in build-all plan acceptance table).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/2026-11-01-social-contest-matters-standpoints-and-fold.md
- **What it is:** [READ PARTLY: :4-66, :220-264 opened; §2, §4-10 headings only] Companion armature to P4: how worldly matters enter, the 18 families of matter, how standpoints occur, how decisions fold into the season loop.
- **Status:** PROPOSED (reference; resolves nothing, schedules nothing) (:3). Reading: reference; it is the document the RATIFIED build-all plan counts "all" from.
- **Bears on:** SC, CHAR, CORE, FA, WR.
- **Content that matters:**
  - "No act fetches a matter": `questions_for` builds Questions via one pipe (Event witnessed -> claim in ledger -> Question) and three direct entry points (vacancies, docket, sittings); seven entry points total (§2.2) (:33-39).
  - Seed 0 four seasons: 15,600 claims, 15,642 `claim_landed` vs 495 `need` questions; 258 of 261 Propositions OUGHT; 28 docket items, 18 empty slots; none of 10 matter-holding items named a row (:40-46).
  - Eighteen matter families (wrong done, heresy, contempt, holding dispute, office, grant, obligation, war/peace, provision, place, standing, fact-finding, bargain, procedure, opinion, membership, trade/levy, body contest) with per-family disposal and measured state; families 5, 6, 9 blocked at the consent/licence conjunct; 4 lacks a `hold` disposal site; 13 lacks computed `give` (:220-264).
  - Standpoint computed never stored (R-20, S-7); at seed 0 opinion of Hafenmark split 39 to 39 among 78 persons, same at tick 0, so it comes from the build (:47-52).
  - `determine` never executed at seeds 0/1 (`determine.refused` 8 and 13), `pursuit.moved` 0, all 67 (43) `comply`/`evade-defy` were `compliance.impossible`; none formed on a writ (:57-66).
  - The six speech kinds are all `genres: [forensic]`; deliberative/epideictic matters have no speech-kind roster (:260-263).
- **Conflicts / stale:** `[ASSUMPTION]` that "the subsystem" is social-contest. Probe latency not established.
- **Open items:** §6 what depends on which proposal; §7 assumptions and reverts.

### proposals/2026-10-29-parliament-and-debate/2026-11-01-social-contest-proposal-4-authority-staged.md
- **What it is:** [READ PARTLY: :4-40, :80-100, :765-871 opened; §3-§8 body not] Proposal 4: P3's authority framework carrying P2's staged hearing, with ten player decisions "computed" in `stress_p4_choices.py`, faculties from attributes, and the critic's reconciliation.
- **Status:** PROPOSED (reference; resolves nothing, schedules nothing) (:3). Reading: "target specification for the choice layer once Proposal 1's core and the dead core run, cut back" (critic verdict :869).
- **Bears on:** SC, CHAR, DICE, FA.
- **Content that matters:**
  - Ten decisions: appear/evade/defy, forum, plea, proofs, who speaks, speech kind, moves against bench/file, appeal, term of grace, warrant-holder duty; each tested for dominance at 2D, 5D, 12D (:30-33). Honest count: 14 of 14 under own test; 10 of 14 under headline weights; ~5 robust (proofs, self vs advocate, naming enemies, warrant duty, appear/evade/defy in polity rows) (:855-860).
  - Capability layer: `faculties:` table in `rosters.yaml` maps attribute keys to faculty with weights, e.g. eloquence = 0.7 charisma + 0.3 bonds (:98-100); attribute roster is a registry entry with no `Person` carrier; kernel `Pool.size = max(5, 2*faculty+3)` (`primitives.py:211`).
  - Critic (BREAKS IT): batch A1 cannot be green as ordered (deletes `VERB_CAPABILITY` whose readers include `data/verbs.py:1580`, `harness/corpus_run.py:353`, `sigma.py:143`); no verb rows exist for plea, offer-proof, speech kind, judge challenge, naming enemies, forum plea, coming forward; existing `challenge` is a duel call (:845-846).
  - Questions for Jordan Q1-Q5 (church judging reach, F8 index, attributes into roll, ceiling value, "royal person involved") (:765-784).
- **Conflicts / stale:** Q3 already answered by `workplans/valoria_master_workplan_v10_part6.md:33` (M2); `def faculty` now exists at `engine/season/seam/wrappers/pool.py:78` (verified).
- **Open items:** Q1-Q5; most decisions not yet acts the loop can form.

### proposals/2026-10-29-parliament-and-debate/2026-11-02-social-contest-build-all-plan.md
- **What it is:** [READ IN FULL: 156 lines] Ledger folding 28 items into the active plan: 11 already positions, 13 new positions CR-55..CR-67, 2 LEAVE rows, new batch B10-18c.
- **Status:** "RATIFIED on merge (ED-1094, ED-IN-0308), as the source of CR-55 to CR-67 and batch B10-18c in the active plan. The workplan governs; this file is its source and dies with its rows" (:3). Reading: the only RATIFIED file in this lane; live source of positions but not itself a plan.
- **Bears on:** SC, CORE, FA, PC (W27 yielded duel), CHAR (W5 attributes CR-20).
- **Content that matters:**
  - Position map (:40-70): CR-55 matter lapses; CR-56 stamp tier where a matter waits; CR-57 petition addressable (H-94); CR-58 consent rows + `<verb>.unlicensed`; CR-59 appellate closure basis; CR-60 `authority.by_faction`, `scope:`; CR-61 case file Record kind `case`; CR-62 plea with concession through the obstacle; CR-63 five robust decisions as verb rows; CR-64 forum stage; CR-65 legitimacy index (design-first, held); CR-66/67 design-first membership and trade/levy in B10-19; SC-05 kernel deleted last in B10-Z.
  - Acceptance table of observables zero today at seed 0, each with a control arm (`matter.determined` 0/0, `pursuit.moved` 0, docket items naming a row 0 of 10, `give` executed 0 of 7, `compliance.given` 0, `arrest.made` 0, persons with capability 0 of 78) (:106-118).
  - Declared movers: CR-55, 56, 57, 58, 60, 61, 62, 63; EQUAL: CR-59, CR-64. The pins pass under Python 3.13 and fail under CI's 3.11 on `main` today; parked as Jordan instructed (:120-123).
  - Held back: ARM G2 (Layer-1 §A.3 wording for office weight) and P4 Q2 (draw reads index of residents' ledgers) (:131-139).
- **Conflicts / stale:** "persons with capability 0 of 78" vs now `faculty` exists in `seam/wrappers/pool.py:78` [capability authored status UNVERIFIED]. The pytest Python-version pin split (3.13 vs 3.11) is a live CORE concern.
- **Open items:** B10-18c is not a port-gate precondition (`[ASSUMPTION]`, revert: add to port-gate line).

### proposals/2026-10-29-parliament-and-debate/lopsided_levers.py
- **What it is:** [READ IN FULL via docstring + def list] Probe: feeds kernel track-proceeding results to `narrative.summarize` and tests levers (evidence, raised standing, pressure) for faculty 1 v 4.
- **Status:** none; historical probe for a NOT-adopted kernel.
- **Bears on:** SC.
- **Content that matters:** 2 defs (`narrative_cell`, `main`); writes `2026-10-30-stress-log-lopsided-levers.jsonl`; the narrative summariser was written for winners 'a'/'b' while track proceedings return 'A_decisive', 'committee', ... (docstring).
- **Conflicts / stale:** imports `systems.social_contest.sim.contest` (still present).
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/lopsided_mechanism.py
- **What it is:** [READ PARTLY: docstring + def list] Mechanism probe: advantage-gap geometry, seat asymmetry (track start 6.0 vs 5.0), exchange-majority venue.
- **Status:** none; historical.
- **Bears on:** SC.
- **Content that matters:** 7 defs (`win_geometry`, `cell`, `degree_cell`); logs to `...-stress-log-lopsided-mechanism.jsonl`.
- **Conflicts / stale:** kernel-only.
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/probe_controls.py
- **What it is:** [READ PARTLY: docstring] Read-only controls C1-C5 for the matters/standpoints companion; `python probe_controls.py SEED SEASONS > out.json`, ~4 minutes.
- **Status:** none; probe.
- **Bears on:** SC, CORE.
- **Content that matters:** builds realm for one seed, measures at tick 0 and end; writes nothing in tree.
- **Conflicts / stale:** `sys.path` line made relative after run.
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/probe_event_kinds.py
- **What it is:** [READ IN FULL: 28 lines, docstring seen] Event kinds and folded acts after N seasons.
- **Status:** none; probe. **Bears on:** SC. **Content that matters:** shipped runs `0 4` and `1 4`.
- **Conflicts / stale:** none. **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/probe_matters_intake.py
- **What it is:** [READ PARTLY: docstring] What matters reach a person's ledger and question set; standpoint divergence.
- **Status:** none; probe. **Bears on:** SC, CHAR.
- **Content that matters:** key `stamped_class_on_first_question` is a mislabel (lists referent ids), "left as run".
- **Conflicts / stale:** mislabel. **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/probe_routes_hand_built.py
- **What it is:** [READ PARTLY: docstring] Stress of return routes (companion §5.5) on `test_u7_remit.py`'s hand-built bench world (a Duke judges `p_mid`).
- **Status:** none; probe. **Bears on:** SC.
- **Content that matters:** depends on test helpers in `engine/season/tests/test_u7_remit.py`; breaks if they move [UNVERIFIED].
- **Conflicts / stale:** none. **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/social_contest_stress.py
- **What it is:** [READ PARTLY: docstring + def list] Stress probe for module (`modules/social_contest/roll.py`) and kernel with JSONL audit log; 14 defs (`module_section`, `kernel_section`, `kernel_props`, `run_suites`...).
- **Status:** none; probe; budget-based sampling ("NO CHOSEN COUNT").
- **Bears on:** SC, DICE.
- **Content that matters:** each section samples until its time slice ends and logs `n`; run command `--label X --budget-s 1800 --log OUT.jsonl` (stress report :53).
- **Conflicts / stale:** its first suites attempt named a nonexistent test file (logged).
- **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/stress_p1.py
- **What it is:** [READ PARTLY: docstring + def list] Stress harness for P1; REAL = dice engine, `modules.social_contest.roll.obstacle`, `build_realm` worlds, `world_q`; MODEL = P1's `Dice/Obstacle/Leverage` records. 24 defs.
- **Status:** none; historical harness. **Bears on:** SC, DICE.
- **Content that matters:** sections legitimacy, model closed form, channels, regard, bench; JSONL convention (manifest, plan, claim, result, fail, null, blocked, skipped, unverified, error, summary).
- **Conflicts / stale:** evidence about a design not built. **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/stress_p1_b1.py
- **What it is:** [READ PARTLY: docstring] Applies P1's first batch (B1 delete) in a scratch git worktree in cumulative phases P0..P1d and runs the touched test files. 11 defs.
- **Status:** none; harness. **Bears on:** SC, PROCESS.
- **Content that matters:** result: kernel deletion + repointing reddens 14 of 29 test files in the batch-literal reading (stress comparison).
- **Conflicts / stale:** worktree-dependent. **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/stress_p1_b1_modules.py
- **What it is:** [READ IN FULL: 26 lines] P1 B1's own observable: `sys.modules` after a season holds no `systems.social_contest`; same-seed `content_hash` equal twice.
- **Status:** none. **Bears on:** SC, CORE. **Content that matters:** run inside a worktree. **Conflicts / stale:** none. **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/stress_p1_void.py
- **What it is:** [READ PARTLY: docstring] P1 claim (d): the `void` appeal disposal tried in a scratch worktree (adds `void` to `_DISPOSES_LITERALS` in `data/arrangements.py:68` and an appeal row).
- **Status:** none. **Bears on:** SC. **Content that matters:** result BROKE in 3 ways (stress P1 row 9). **Conflicts / stale:** none. **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/stress_p2.py
- **What it is:** [READ PARTLY: docstring + def list] Stress harness for P2: sections `model` (Markov chains over real band probabilities), `world` (real-code probes), `batches` (first-batch deletions and pinned hashes). 39 defs.
- **Status:** none. **Bears on:** SC, FI.
- **Content that matters:** exact computations over the engine's integer net pmf; pmf checked against `roll_pool`.
- **Conflicts / stale:** none. **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/stress_p3.py
- **What it is:** [READ PARTLY: docstring + def list] Stress harness for P3 with sections A (legitimacy), B (case-opening scope), C (`authority.by_faction`), ... S7b; run `--log OUT.jsonl --sections A C B`. 46 defs.
- **Status:** none. **Bears on:** SC, FA. **Content that matters:** reads tree, writes only the log; `Log` class with fsync per line.
- **Conflicts / stale:** none. **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/stress_p4_choices.py
- **What it is:** [READ PARTLY: docstring + def list] MODEL (not code) of P4's ten choices: hearing chains, plea tables, payoffs as arithmetic over real dice engine; 39 defs (`pareto`, `scalar`, `best_under`, `hearing`).
- **Status:** none. **Bears on:** SC, DICE.
- **Content that matters:** "Nothing here imports `engine/season/`: no proposal-4 code exists to run." Runs 1-3 are false starts kept in log; run 4 is the evidence.
- **Conflicts / stale:** payoffs are design arithmetic. **Open items:** none.

### proposals/2026-10-29-parliament-and-debate/stress_probe.py
- **What it is:** [READ PARTLY: docstring + def list] Stress probe for the season-loop debate surface: ticks `build_realm(seed)` with shipped chooser, flushed JSON line per event; flags `--rule`, `--bench-quorum`, `--determinism`.
- **Status:** none. **Bears on:** SC, CORE.
- **Content that matters:** no chosen horizon: seeds/seasons are outputs, bound by wall-clock `--budget-s`.
- **Conflicts / stale:** none. **Open items:** none.

