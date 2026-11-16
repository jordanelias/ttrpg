> **Location.** This directory is the scratch model that V2 (`../2026-11-15-social-contest-redesign-v2*.md`) cites as `sc_model_v2/`; paths in V2 such as `checks_v8.py`, `fix2/` and `pc_run1` are relative to here. It is PROPOSAL EVIDENCE, not Layer 2 code: nothing in `engine/` or `modules/` imports it, and it is not a test. Run from this directory: `python checks_v8.py` (the battery, long), `python transcripts_v8.py`. It reads the repo for `engine.dice_engine` through `VALORIA_REPO` (default `/home/user/ttrpg`). A 2026-11-16 full rerun reproduced `v8_out.txt` except two invariant beat counts (see V2 part 3).

# sc_model_v2 — the model of the v2 redesign

A copy of `../sc_model/` (the stress test's model of the 2026-11-14 design; `scmodel/`, `lane1..4/`, `selfcheck.py`
are that model, untouched, and still run) plus the v2 design as a new package:

| file | holds |
|---|---|
| `sc2/engine.py` | the module: `Present`, `Rite`, `Item`, `Sitting`, `Point`, `Cond`, `Beat`, `View`, `Option`; `proceed`, `exchange`, `speech`, `build_view`, `auto`, `_close`, `closing_odds`; `fit`, `aim`, `credit`, `insincerity` |
| `sc2/host.py` | the host side as a toy: the settings, the matters roster, the rites, context, disposal; `bearing`, `care`, `tie`, `power`, `strain_carried`, `tilt`; `build` (-> `Input`, `Card`); `act_band`; `fold`; `render` (test fixture) |
| `sc2/fixtures.py`, `sc2/lab.py` | toy persons and matters; runners and view-only choosers |
| `checks_core.py [n]` | D1..D8, the roles, determinism, the R13 and card invariants -> `core_out_final.txt` (n=1000) |
| `checks_world.py [n]` | played, simulated, bearing, context, roles, power, the fold, three seasons -> `world_out_final.txt` (n=600) |
| `transcripts.py` | six rendered sittings with their cards -> `transcripts_out.txt` |

Run each with `PYTHONHASHSEED=0` from this directory. Design: `proposals/2026-11-12-subsystem-audit-suite/proposals/2026-11-15-social-contest-redesign-v2.md` (+ parts 2 to 4).

## After the reconciliation (2026-11-15)

`sc2/engine.py` and `sc2/host.py` were rewritten to the reconciled design (nemo rule, temper, esteem, weary, heard,
gap, believes, believed odds, a played judge). **`checks_v3.py [n]` is the current check** (output `v3_out.txt`,
n=400) and `transcripts.py` prints seed 0 of each rite. `checks_core.py` and `checks_world.py` and their
`*_final.txt` outputs are the FIRST v2 run and no longer match the engine's API (they will not run).

## After A-139's correction and A-141..A-143
Current checks: `checks_v4.py` (the one-character invariant, both-cells cases, conversation/questioning/negotiation,
the noble's audience, invariants), `checks_v5.py` (the gauge and the frame), `checks_v6.py` (the four operands).
`checks_v3.py` no longer runs (it reads removed View fields); `v3_out.txt` is the earlier run.

## Current (after A-144, A-145, A-146 and the third critic pass)
ONE battery: `PYTHONHASHSEED=0 python checks_v7.py [n]` (runs checks_v7_core, checks_v4, checks_v5, checks_v6,
checks_v7_adj) -> `v7_out.txt` (n=300). `transcripts.py` -> `transcripts_out.txt` (seed 0 of each rite).
`checks_v3.py`, `checks_core.py`, `checks_world.py` and their outputs are superseded and do not run.

## Current (after the premise-check and the second fix pass, 2026-11-16)
ONE battery: `PYTHONHASHSEED=0 python checks_v8.py [n]` -> `v8_out.txt` (n=300). It runs `checks_v8_core`,
`checks_v8_a139`, `checks_v8_a141`, `checks_v8_a143`, `checks_v8_adj` (adapted copies of the v7 set) and the fix
pass's own probes under `fix2/` (`c1` .. `c5` the five root causes, `c_form`, `c2_n`, `c3_grid`, `d2` the season
driver, `b17`, `bitems`). `transcripts_v8.py` -> `transcripts_v8_out.txt` (seed 0 of nine sittings, with the world
each leaves). New model file: `sc2/acts.py` (the acts before and after a sitting, the season driver). The model as
it stood before this pass is kept in `fix2/before/sc2/`; adapted copies of two premise-check probes are in
`fix2/pc_run1/`, `fix2/pc_run4/` with their outputs. `checks_v7*.py` no longer match the API (`Cond.heat`, the
docket's dict entries) and are superseded.
