# DICE — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

Subject: the resolution substrate — `engine/dice_engine/` (`dice_engine.py`, `sigma_leverage.py`),
`engine/substrate/` (leaf readers and the `pc_engine` path seam), `engine/engine_params/` and its exporters
(`tools/export_*`), `engine/tests/`, and the call sites in `engine/season/` and `modules/` through which a draw
reaches the fold. Instrument: the `resolution-diagnostic` skill's five properties, applied to the real
functions; its output is evidence carried into a NERS reading (§5), not a verdict.

## 0. Verdict

(written last; see the end of §3 for the ranked findings it rests on)

## 1. What it is, as coded

### 1.1 The modules

| file | what it owns | state |
|---|---|---|
| `engine/dice_engine/dice_engine.py` | the face rule (`_die_result`: 1 → −1, 2–6 → 0, 7–9 → +1, 10 → +2); `roll_pool` (whole dice, floor 1D, TN refused unless 7); `continuous_engine_sample` (Normal(0.4·N, 0.8·√N), fractional N, returns 0.0 at N ≤ 0); `degree_from_net` (the margin ladder, four bands, `margin = net − ob`); `BandExtension` (veto-the-top-band seam); `MU_PER_DIE`/`SIGMA_PER_DIE`; `DEGREE_LABEL`/`DEGREE_ORDINAL` | none; stdlib only |
| `engine/dice_engine/sigma_leverage.py` | the advantage layer: `soft_cap` (1.5·tanh(x/1.5)), `net_boost` (the μ-shift: capped σ × 0.8 × √max(1, N)), `levels_to_net_sigma` (named levels 0.25/0.50/0.75/1.00), `p_success` (Gaussian closed form), `band_odds` (exact enumeration of the dealt roll), `settle_margin`/`settle_record` (the fraction of a margin realised by one uniform draw), `record_odds`, `roll_net` (whole dice, `max(1, round(pool))`), `roll_net_continuous` (fractional pool, floor 1.0), and `eff_ob`/`effective_ob`/`sigma_space_ob_shift` (display only) | one `lru_cache` (`_net_counts`), pure |
| `engine/substrate/` | seven leaves, each stdlib-only, each reading one cooked JSON at import: `descriptors` (attribute, pursuit, axis, affiliation, heritage rosters), `names` (canonical naming, raises on ambiguity and legacy tags), `composition` (role → module attribute, by string, cached), `combat_kit` (weapon and armour key sets), `battle_orders` (order roles, retreat values), `stubwire` (the typed not-built result and its counter), `pc_engine` (the one `sys.path` seam into `modules/combat/`) | `composition._CACHE`, `pc_engine._LOADED`, `stubwire.invocations` |
| `engine/engine_params/*.json` | eight cooked artifacts, each written by one `tools/export_*.py` behind a `--check` | none |

### 1.2 How the season loop reaches the dice

One path, by composition row, for every graded social act and inquiry:

`loop/resolve.py::_contest` → `seam/contest.py::contest` (or `::grade` for an inquiry) → `manifest` provider
lookup → `seam/wrappers/sigma.py::resolve` → `contest_input` (pool from `seam/wrappers/pool.py::faculty`,
obstacle operands raw) → the module entry `modules/social_contest/roll.py::roll` →
`sigma_leverage.roll_net(pool, rng) + net_boost(leverage, pool)` and `roll.py::obstacle(inp)` → a
`Margin(net, ob)` → S27.4 refusal on the pair → `sigma_leverage.settle_record` (one `rng.random()` only where
`boost − ob` has a fraction) → `seam/ladder.py::degree_of` → `degree_from_net(settled_margin, 0)`.

Two other providers return something that is not a margin and are graded off their own result by ruling
(Jordan, 2026-09-03): personal combat (`wound_state` → `combat_degree`) and mass battle (`attacker_wins` →
`field_degree`). Both draw their randomness inside the module. Their relation to the dice engine is §3
(F-DICE-01, F-DICE-02).
