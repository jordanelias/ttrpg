# Toy-world evidence for `../00_THRUST_LAYER_DESIGN.md`

**Grade: model-internal, low confidence. Reference under CLAUDE.md §0.05. Not game code, not read by
any tool, creates no obligation.** Nothing here runs `engine/season/` except the five chronicle files
below. Everything else is a small abstract world (24 actors, 6 places, 6 prizes, 24 seasons) built to test
the *logic* of narrative regimes (bottom-up, scripted/forcing director, motive hybrid, goal ladders,
closure engines, set pieces, a constrained world). It says nothing about Valoria's balance or content.

Run any script from this directory with `python3 <script>.py [N]` (stdlib only; seeds are fixed).

| Module | Adds | Used by | Output |
|---|---|---|---|
| `regimes.py` (= `regimes_v1.py`, byte-identical, named by `v1_files.sha`) | v1 world and metrics | `suite.py` (= `suite_v1.py`), `predictions.py` (= `predictions_v1.py`) | `out_v1.txt`, `results_v1.json` |
| `regimes2.py` | v2 instrument: pair-thread identity, plateau peak, burn-in, director thread | `suite2.py`, `predictions_v2.py`, `posthoc.py` | `out_v2.txt`, `results_v2.json`, `posthoc_out.txt` |
| `regimes3.py` | terminal-lifecycle and threshold-raised tribunal arms | `exp_closure.py`, `lookahead.py` | `exp_closure_out.txt` |
| `lookahead.py` | choice-level "narrative leverage" with rollouts | `lb_sweep.py`, `lb_more.py` | `lb_sweep_out.txt`, `lb_more_out.txt` |
| `regimes5.py` | goal ladders (HYg1-3), ladder + tribunal | `exp_ladder.py` | `exp_ladder_out.txt` |
| `regimes6.py` | set pieces that write a situation (TDS, TDSm, HYg3s) | `exp_setpiece.py` | `exp_setpiece_out.txt` |
| `regimes7.py` | set pieces with a decisive form (TDSc, TDScf, HYg3c) | `exp_contest.py` | `exp_contest_out.txt` |
| `regimes8.py` | non-lethal and settled climaxes | (run inline) | not saved |
| `regimes9.py` | standing snapshots on events | (run inline) | not saved |
| `regimes10.py` | constrained world: rare death, standing gate, accusation, bound peace, killing consequences | `exp_con.py`, `save_figs.py` | `exp_con_out.txt`, `save_figs_out.txt` |

**Pre-registration.** `predictions*.py` and `exp_*.py` were frozen before their first run; the `*.sha`
files hold the checksums and times. **Checked 2026-10-28:** the prediction and experiment scripts match their recorded hashes (13 of 17 entries); the world file recorded beside them does NOT in four freezes — `regimes.py` (`predictions.sha`), `regimes2.py` (`v2_frozen.sha`), `regimes5.py` (`ladder_pred.sha`), `regimes10.py` (`con_pred.sha`) — so the freezes cover the predictions, not the world they ran on. This README names a generator change only for v1. v1's predictions were blind; every later set was written after seeing
earlier results (informed) and is labelled so in its docstring. HYc, HYd, the bootstrap intervals, the
sifting test, the lookahead arm, the ladder, set-piece and constrained arms are **post hoc**. The design
document lists the falsified predictions beside the confirmed ones.

**Known limits.** The arc test is a three-act template; it credits a lone interior closing event and ends
arcs by silence, so read arc rate beside its shuffled null. "Standing" is holding a prize; the 90% gate is
a model setting that was not swept. v1's thread identity split a conflict across two references and its
climax sat outside its own peak window; v2 fixed both after v1's results were seen (recorded in the
design). A generator bug fix and a lethality calibration (survivors, bottom-up only) preceded the first
comparison run.

**Printed, not saved:** the review of earlier arcs under `regimes9.py`; the non-lethal and settlement runs
(`regimes8.py`); the threshold-sensitivity and per-property tables (`regimes5.py`, reproduced in part by
`exp_ladder_out.txt`); the killing-at-season-10 cascade tables except the figures in `save_figs_out.txt`.

`real_engine_chronicles/` holds `python -m engine.season.harness.chronicle --seed S --seasons 4` output
for seeds 0, 1, 2, 4 and 5 (seed 3 was shown in the session and not saved). Across those five, 53 of 66
chain acts end in a refused, blocked, unavailable or empty result by the suffix definition in
`proposals/2026-10-13-narration-mechanisms.md` (which over-counts degree bands).
