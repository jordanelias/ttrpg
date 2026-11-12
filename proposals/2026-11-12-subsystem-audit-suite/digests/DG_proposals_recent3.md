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

