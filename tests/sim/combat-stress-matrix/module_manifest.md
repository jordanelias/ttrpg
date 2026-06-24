# combat-stress-matrix — module manifest

**Purpose:** comprehensive one-factor-at-a-time (OFAT) isolation stress matrix for personal combat
(`combat_engine_v1`). Each character attribute, derived score, and state-graph component (approach →
disengage) is varied as a single variable with all else controlled.

## Files
- `_engine/` — staged copy of `designs/scene/combat_engine_v1/` with two **inert** per-fighter isolation
  hooks (`derived_scale['pool'|'health']`, default empty). Imports the r1/r8/m1 substrate from
  `tests/sim/v32-combat-balance/` via sys.path. **Test instrumentation — not canonical.**
- `stress_matrix.py` — the harness. Blocks: 1 attributes (1→7 sweep), 2 derived scores (×0.5/×1.5),
  3 state-graph components (config-ablation across a mirror/reach/skill/armour panel). Position-swapped,
  uniform-4 baseline, seeded. Flags: `--n --mb --smoke --block --out`.
- `render.py` — `results.json` → `results.md` (sorted-by-effect tables).
- `results.json` / `results.md` — latest run (N=200, mb=40, seed=20260623).

## Method / controls
- Baseline: all 9 attributes = 4, arming sword, light armour, tradition `none`.
- Each cell = N fights × 2 (attacker/defender positions swapped to cancel first-mover), fresh seeded RNG.
- Primary metric: win% of the isolated fighter (B1/B2); Δwin% vs the full engine (B3).
- Model: canonical d_sigma; pool=max(5,History+6); additive-coupled damage ×1.55; **ED-1041 bilateral-Ob
  wounds** (so numbers differ from the pre-ED-1041 2026-06-22 analysis — by design).

## Known limitations (see results.md header + the coverage audit)
- Single-seed mirror baseline ≈ 54.8% (not 50) — read cells as marginals; multi-seed averaging recommended
  for a publishable final.
- `max_bouts=40` drives draws ≈ 0 (mirror_draw_delta column all 0); rerun `--mb 12` to expose
  resolution/draw effects.
- Some derived-score isolations are confounded (a scaled fn read at multiple call-sites; an attribute split
  across channels) — the coverage workflow flags these.

## Reproduce
```
python stage_engine.py                         # (re)create the .gitignored _engine/ instrumentation
python stress_matrix.py --n 200 --mb 40        # full
python stress_matrix.py --smoke                # quick
python render.py
```

## Known coverage limits (per the 2026-06-23 coverage audit — see PR notes)
- Block 2 scales a *function* read at many call-sites at once → it ranks channel **sensitivity**, not a
  clean per-quantity isolation (e.g. `reading` is read at 7+ sites; hence the `leverage` sign anomaly).
- Block 3 zeros for `push_shove`/`oob`/`disrupt_focus`/`displace_inside` are **false negatives** — the
  4-matchup panel never enters their trigger state (distinct from a genuinely dead lever).
- Not yet isolated: the damage/lethality channel (`damage`/`coupling`/`p_auth`), the initiative dynamic
  loop (gain/loss/decay/cap), the disposition hooks, the half-sword switch, `UPSET_FLOOR`, and the whole
  tradition/ability layer (every fighter is tradition `none`). Add a damage block + mb-12 + multi-seed +
  a non-`none` tradition pairing before publishing as a completeness/isolation proof.
