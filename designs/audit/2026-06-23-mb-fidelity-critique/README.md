# Mass-Battle Fidelity Critique + Hierarchy Enforcement — Track Anchor

**Status:** CONFIRMED part of the bottom-up re-architecture workplan (Jordan, 2026-06-30). This is the
**fidelity-first track**, sequenced **after Stage 1** (the wrapper/core split, now landed) and run with
the same gate sequence as `../2026-06-30-massbattle-bottomup/05_redesign_workplan.md` (G1–G6) plus a
NERS Stage-4 re-test. Decisions on record: **fidelity fixes first**, then the 3×3 hierarchy; **full
execution + verification**; every effect **emergent from cell state** (no flat per-shape bonus); on lens
conflict **history > theory > games**.

```
Stage 1 (DONE: wrapper/core split + equipment split)
   └─► THIS TRACK
         Phase 0  critique → NERS → reconcile           (read-only; produces the 3 artifacts below)
         Phase 1  fidelity fixes  D1 → D2 → D4 → D3      (+ checks f, a)   [Track B, FIRST]
         Phase 2  3×3 hierarchy enforcement              (byte-exact-defaulted) [Track C]
         Phase 3  consolidate & present
   └─► Stage 2 broader module wiring (troop_types / formations / tactics / doctrine) — 05_redesign_workplan.md
```

Phase 0 deliverables (to be produced by the Phase-0 workflow): `register.md` (region×lens → findings →
skeptic survival), `ners_verdict.md` (N/E/R/S per finding, gauge-band-as-R), `reconciliation.md`
(precedence-ordered conflicts → worst-first fix list). This README is the **track anchor** + the
**reconciliation of the directive against the current tree** (the "have we missed anything" pass).

---

## Reconciliation 1 — every fix site re-anchored to the post-Stage-1 tree

The directive's `file:line` references predate the Stage-1 wrapper/core split (which moved the data model
to `hierarchy/units.py` and the phase hooks to `core/`). Verified current locations (read-only audit,
2026-06-30):

| Mechanic (directive's stale anchor) | Current location | Status |
|---|---|---|
| charge-recoil application (`orch L1922-1926`) | `orchestration.py:728-730` (`PC_CHARGE_RECOIL * _wall_prep * SIGMA_PER_D`) | present, moved |
| cavalry charge / momentum / puncture / charge-shock (`orch L1877-1916`) | `orchestration.py:681-730` | present, moved |
| wrap / pocket / roll-up (`orch L1745-1830`) | `orchestration.py:549-658` | present, moved |
| `morale_check_phase` / `rout_resolution` / `discipline_check_phase` (`orch L290-337`) | **`core/state.py:14-38 / 41-60 / 63-94`** | **extracted to core/ (Stage 1)** |
| `_charge_shock_sigma` / `_wall_prep` / `_morale_sigma` / brace gates (`resolution L83/77/45/55-64`) | `resolution.py:83-114 / 77-81 / 45-54 / 55-64` | present (unchanged lines) |
| `Subunit.charge_pen` (`L750`) / `Unit.base_combat_pool` (`L1343`) / `check_drift` (`L1364`) | **`hierarchy/units.py:244-249 / 785-804 / 806-819`** | **extracted to hierarchy/ (Stage 1)** |
| `reset_positions` (`L2466`) | `orchestration.py:1270-1278` | present, moved |
| `MORALE_PHASE_CAP` / `MORALE_EROSION_DAMP` | `config.py:47 / 78` — **both DEAD** (defined, never read) | confirms D4 |
| `PC_CHARGE_RECOIL` / `PC_SHOCK_*` family / `ROLE_SPEC` / `STANCE_SPEED_MOD` | `config.py:108 / 96-103 / 164-180 / 71` | present |
| `refused_flank_cells` / `gapped_line_cells` / `cell_speed` | `geometry.py:60-73 / 47-58 / 335-363` | present |
| `_envelopment_sigma` (DISABLED) / `_fatigue_sigma` / `distribute_casualties` | `percell.py:127-148 / 110-125 / 66-89` | present (`_envelopment_sigma` returns 0 when `PER_CELL=0`) |

**D4 confirmed at the code level:** `core/state.py:38` hard-codes `atom.erode_morale(min(loss, 3.0))`
while `MORALE_PHASE_CAP=3` and `MORALE_EROSION_DAMP=0.7` sit **dead** in config. D4 = replace the literal
with `MORALE_PHASE_CAP` and wire the concentration/encirclement → morale-erosion → rout channel through
`MORALE_EROSION_DAMP` (a dead knob scaling an already-computed cell quantity — NERS-N clean).

## Reconciliation 2 — the directive's named harnesses are not in the tree

`tests/sim/massbattle_battery/run_gauge.py`, `controlled_sweeps_fixed.py`, and `FINDINGS_2026-06-23.md`
**do not exist** in the current checkout. The actual validators are:
- `tests/sim/gauge_mb.py` — the 20-band historical gauge (H1–H11, R1/R3, C1–C7; `decA` decisive split,
  `rawA` for braced rows; n=120; `PER_CELL=1` gates the C-series).
- `tests/sim/battery_v22.py` — v22 multi-turn accuracy battery.
- `tests/sim/mass_battle/lanchester_signature.py` — the exponent validator (melee p ≤ 1.4, volley p ≥ 1.6).
- `tests/sim_verification_ledger.json` — the re-pin baseline ledger.

**Action for Phase 1:** the controlled-sweep verifications must be rebuilt on `gauge_mb.py` (+ a small
sweep harness) rather than the non-existent `controlled_sweeps_fixed.py`. The `bat.py` digest battery
(Stage 1) is the byte-exact gate.

## Reconciliation 3 — engine-defect vs gauge-construction tension (Phase 0 must adjudicate)

Two prior analyses disagree on the **root cause** of the C-band divergences:
- **2026-06-23 framing (this directive):** the shock/charge path *over-fires* (ignores defender
  steadiness) and the infantry-formation path *under-delivers* — i.e. **engine defects**.
- **2026-06-30 audit (`../2026-06-30-massbattle-bottomup/`):** the engine's frontal-cavalry mechanics
  were *already grounded*; the **gauge** wasn't triggering them — C2/C6 built "braced" as `hold`+disc8
  **without the `brace` instruction** (so `PC_CHARGE_RECOIL` never fired); C5 forced
  `morale_start = morale` so the "shaken" line read as 100% relative morale (so `PC_SHOCK_SHAKEN_GAIN`
  and `_morale_sigma` never fired).

These are not fully contradictory — D1's recoil **does** lack an octagon-zone/actor gate
(`grounding §4.3` flags exactly this latent defect), which is a genuine engine issue independent of gauge
construction. **Phase 0's adversarial pass resolves, per finding, which of D1–D4 is an engine defect vs a
gauge-construction artifact**, under the standing rule: *a band divergence is an engine defect, never a
band to lower; history > theory > games.*

---

## Acceptance constraints (every gate)

- **Bottom-up / no flat bonus.** `SHAPE_OFF_MOD`/`SHAPE_DEF_MOD` retirement is canon (`config.py` L58-60).
  Legitimate forms only: gate an *existing* δσ term on a cell-derived predicate, or revive a *dead knob*
  that scales an *already-computed* cell quantity. `if shape == X: bonus` is rejected on sight.
- **Fidelity.** Targets are `gauge_mb.py` bands cited to `grounding §3/§4.3/§8` + DOI.
- **NERS-clean.** N (no bolted-on apparatus), E (outcome legible from cell state), R (in-band across the
  whole input range = the gauge-band test), S (smoothness/sufficiency). `skills/valoria-resolution-diagnostic`.
- **Byte-exact default.** All Phase-2 hierarchy state defaults to a no-op; instruction-less / default
  scenarios reproduce the `bat.py` digests digit-for-digit. Outcome-altering Phase-1 changes re-pin the
  gauge and update `tests/sim_verification_ledger.json`.

## Guardrails (from the directive, preserved)
- **D3 must NOT re-enable `PC_ENVELOP_SIGMA`** (double-counts the depth-aware contact fraction; breaks H4
  Cannae — documented at `orchestration.py:1604-1611`). Formation upside flows through the D4 morale
  channel + the existing wrap.
- **D2 must NOT raise `PC_CAVALRY_SPEED_MULT`** (3× over-saturates C4 and erodes the brace-repel — measured).
- **Order:** D1 → D2 → **D4 (morale channel; prerequisite for D3)** → D3.
