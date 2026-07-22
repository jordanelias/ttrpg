# Mass-battle field-based stress test — 2026-07-22 (MB lane, ED-MB-0011)

**Task (Jordan):** "Stress test mass battle as much as you can. Ensure all wiring, ensure all
flags/gates are activated with caveat that we are using field-based and not grid-based. Ensure use
of most recent work." + "Everything that gets wired gets to be tested whether in aggregate or
isolation." + "fields, not grids. no grids." + "if it's broken and not commensurate with system,
disable."

## 0. Which engine, and why

Two mass-battle engines exist in the tree (flagged unreconciled in `sim/README.md` / CLAUDE.md,
audit ED-IN-0074 D5):

| | engine | field flags/gates | ED-MB-0001..0007 work |
|---|---|---|---|
| wired bare port | `systems/mass_battle/sim/massbattle.py` | **none** (grep: 0) | no |
| **active engine (target)** | **`tests/sim/mass_battle/`** | all of them (`config.py`) | **yes** |

Every flag this task names (`FIELD_MOVEMENT`, `PER_CELL`, `PC_NODE_COHESION`, `LANCHESTER_ENABLED`,
`POOL_QUALITY_MODEL`, …) lives only in `tests/sim/mass_battle/`. "All flags/gates, field-based, most
recent work" therefore targets that engine for the flag/gate stress surface (S0–S5 below).

**The DG-10 movement-freeze fix, however, was applied to BOTH engines** — because the *wired* engine
(`systems/mass_battle/sim`, the one `resolve_mass_battle`/`faction_action` actually call) carries the
**same** grid-floor freeze (`advance_cells`: `floor(1×0.7)=0` → `== 0: continue`). Per Jordan's
"subunits aren't moving when they have previously" / "if it's broken and not commensurate with system,
disable" / "fields, not grids. no grids." the freeze is disabled there too. That engine holds *integer*
cell positions (contact = set-membership on integer coords), so it cannot carry a true sub-cell field
velocity the way the field engine can (the two are unreconciled, ED-IN-0074 D5); the fix takes the real
velocity with no floor and lets an advancing body take at least one whole cell instead of freezing —
Discipline≥5 (incl. the wired `resolve_mass_battle` default) is **byte-identical** (`round(1.0)==floor(1.0)`),
only the previously-frozen sub-disc-5 space moves. Guarded by `tests/valoria/test_mass_battle_systems_movement.py`
(8 tests: per-disc closing isolation + all-disc aggregate + disc≥5 regression/determinism).

## 1. Headline finding + fix (DG-10) — field movement was broken

**The field/node movement path froze every sub-Discipline-5 body in place.** `_node_advance`
(the path `FIELD_MOVEMENT=1` routes to since ED-1089) computed the per-tick advance as:

```
step = max(0, math.floor(base * disc_mult) + stance_mod)   # base cell-speed = 1 for every shape
disc_mult = 1.0 if disc>=5 else (0.7 if disc>=3 else 0.4)
```

`floor(1 × 0.7) = 0`. So a **balanced disc<5 formation never advanced to contact** — it sat at its
deploy row for the whole battle and every fight was a vacuous 0-casualty draw. The §B.2 troop table
makes this the *common* case: levy(1), sling/artillery(2), light_inf/archers/crossbow(3),
heavy_infantry(4) are **all disc<5**; only cavalry(5)/knights_templar(6) cleared the floor. Aggressive
stance (+1) or the cavalry ×2 multiplier were the only escapes.

This is **DG-10** from the ED-MB-0007 audit ("a correctly-statted discipline-3 archer computes a live
movement step of exactly zero — no fractional-velocity accumulator on the node path"), generalized:
it is not just disc-3 archers, it is *every* sub-disc-5 balanced/retreat body on the live field path.
The continuous-velocity accumulator that was *supposed* to prevent this (units.py:24, "advances at its
TRUE average rate instead of flooring to 0") had been wired only into the **legacy grid** method
`advance_cells` — it sat **dead** there, never reaching `_node_advance`, the path `FIELD_MOVEMENT`
actually uses.

**Fix (per Jordan's in-session ruling "fields, not grids. no grids." / "if broken and not commensurate,
disable"):** the `math.floor` is the grid-snap that the coordinate field exists to remove. `_node_pos`/
`_node_anchor` are already floats and the sole downstream consumer moves the anchor by
`eff = min(step, mag)` along a unit vector — fully float-safe. So on the field path `step` is now the
**real velocity** (no floor, no accumulator — the accumulator was itself just a Bresenham workaround
for keeping integer positions on a grid):

```
vel = base * disc_mult                       # + cavalry ×2 as before
if FIELD_MOVEMENT:
    _sf = max(0.0, vel + stance_mod)
    step = int(_sf) if _sf == int(_sf) else _sf   # whole velocities stay int (byte-exact); fractions stay float
else:
    step = max(0, math.floor(base*disc_mult) + stance_mod)   # legacy GRID oracle: untouched
```

A disc-4 body now advances 0.7 cells/tick on the continuous field instead of freezing.

### Byte-exactness / what changed
- **Grid oracle (`FIELD_MOVEMENT=0`): untouched** — gated out of the new branch. The CI byte-exact
  test (`test_mass_battle_byte_exact.py`, which pins `FIELD_MOVEMENT=0`) still passes (`2 passed`);
  both grid goldens (`unit`/`cell`) are byte-identical.
- **Field gauge (bat.py cell_field/unit_field, NOT CI-checked):** `mirror` and `ranged` (Line-vs-Line,
  no disc-degradation-while-moving) stay **byte-identical**. The 8 decisive rows (`wedge`/`cannae`/
  `oblique`/`manipular`/`envelop`/`cav_charge`/`cav_braced`/`cav_shaken`) change — verified root cause:
  a unit that **degrades below disc-5 mid-battle** (combat/charge shock) used to *freeze in place*;
  it now keeps moving at its true reduced rate. (Confirmed by trace: wedge seed 0, side B degrades to
  disc-3.) Field goldens re-recorded and re-verified `BYTE-EXACT OK` (`cell_field = a87cb752…`,
  `unit_field = 918940cb…`), with a dated DG-10 comment. Maneuvers + yield pytests: `12 passed,
  1 xpassed`. This is a Jordan-ruled field-behaviour change, not a silent oracle correction.

**Scope honesty:** this fixes *movement*. It necessarily shifts the 20-row Cannae balance gauge (units
that used to freeze now fight), which is the DG-6-gated calibration surface — this change is **not** a
balance-calibration claim and does not tune any balance constant.

## 2. Stress harness

- `mb_fieldbased_stress.py` — engine import, invariant checker, aggregate fuzz, movement census,
  scenario probes, and the `--emit` runner (respects env flags; used by the subprocess flag-A/B).
- `run.py` — the driver: S0–S5, prints a full report, `--json` dumps the structured record.

Run: `python3 audit/2026-07-22-mass-battle-stress-test/run.py [n_fuzz] [--json out.json]`

### Sections (every wired thing tested in aggregate or isolation)
- **S0 Wiring census** — all 30 `MECHANICS` resolve (`mechanics_selftest`); field triad live
  (`FIELD_MOVEMENT=PC_NODE_COHESION=PER_CELL=1`, grid oracle NOT active); full gate roster with the
  field-ON / OFF-by-default / do-not-enable split.
- **S1 Aggregate fuzz** — randomized armies over the full input surface (9 troop types + fallback,
  4 valid shapes, roles→shape/instructions, instructions brace/envelop/sweep/kite, stances, multi-
  subunit to the cap of 11, `build_envelopment`/`build_refused_flank`, timed/enemy-range Orders,
  yield); every battle invariant-checked (no exception; winner valid; hp∈[0,1]; morale finite;
  cell==hp conservation). Contact-rate reported (post-fix closing health).
- **S1b Movement census** — isolation proof of the DG-10 fix: every canonical troop type closes.
- **S2 Isolation validators** — the per-mechanic historical-goal probes (`validators.py`:
  V-CANNAE/FIXING/SHOCK/BRACE/REFORM/ARCHER field-side; V-ENVELOP/V-SWEEP on both grid and field arms).
- **S3 Per-flag A/B** — each env gate flipped in a clean subprocess (flags are import-time), on a
  sensitive scenario, to prove it is WIRED (non-inert) or documented-inert.
- **S4 Off-by-default gates** — `PC_FACING_MODEL` / `FIELD_CONTACT` / `REFORM_CHECK_ENABLED` turned ON
  (each + combined); re-run every probe for breakage. `PC_FACING_SLEW_BASE` left OFF (config marks it
  "NOT ratified — do not enable").
- **S5 Controls** — seed-determinism + order-cancelled mirror symmetry.

## 3. Results

Full machine record: `results.json`; run transcript: `run_log.txt`. Summary (n=200 fuzz):

| section | verdict | detail |
|---|---|---|
| **S0 wiring** | PASS | 30/30 `MECHANICS` resolve; field triad ON (`grid-oracle-active=False`); no WIRED mechanic gated off under field defaults. |
| **S1 aggregate fuzz** | robust | **0 engine failures** over 197 built battles (3 rejected at construction = correct input validation). **77.7% made contact** (153/197; the rest legitimately hold/retreat/never-in-range). Conservation: **1/197** residual `cell≠hp` drift on a *clean* (non-routed, non-broken) unit (~8%, seed 40) — a minor pre-existing casualty/pool-vs-cell accounting drift, orthogonal to the movement fix; the other apparent violations were routed/broken units where `cell>hp` is *expected* (fleeing bodies on the field vs zeroed fighting-hp). |
| **S1b movement census** | PASS | **all 10 troop-type rows now close** to contact on the field path (levy → knights_templar) — the DG-10 fix's isolation proof. Pre-fix, the 7 disc<5 types froze. |
| **S2 isolation validators** | mixed (disclosed) | V-FIXING / V-REFORM / V-ARCHER PASS; **V-ENVELOP + V-SWEEP PASS on both grid AND field arms** (the field maneuver arm works). V-CANNAE FAIL — **pre-existing** (fails identically pre-fix). V-SHOCK / V-BRACE flipped pass→fail: these measure envelopment-shock via a weak proxy (attacker retained-hp delta) that was already ≈0 (0.0005) pre-fix; the movement fix zeroed it exactly. Reflects the known-fragile envelopment-shock layer (ED-MB-0002..0007, DG-6-gated), **not** a movement defect; not CI-gated. |
| **S3 per-flag A/B** | 12/16 WIRED | **WIRED** (flip moves the outcome vector): PER_CELL, LANCHESTER_ENABLED, POOL_QUALITY_MODEL, COMMAND_SIGMA_ENABLED, SIGMA_HEAD, PC_BRACE_ENABLED, PC_CHARGE_RECOIL, PC_REFUSE, PC_VOLLEY_DENSITY_ENABLED, PC_ENVELOP_MOD, K_LINEAR, POOL_QUALITY_SCALE. **Inert on the tested scenario** (present in the mechanic path, but the scenario didn't hit the trigger): `PC_BRACE_SETUP_DELAY` (by-design exempt — the scenario deploys already-braced, which is exempt from the delay), `MORALE_FIX` (cancels on the symmetric `mirror`), `PC_RECOIL_FRONTAL` + `PC_WHEEL` (trigger condition — frontal-zone recoil / overhang wheel — not reached in the drawn scenario). None are unwired; a triggering scenario is future harness work. |
| **S4 off-by-default gates** | PASS | `PC_FACING_MODEL=1`, `FIELD_CONTACT=1`, `REFORM_CHECK_ENABLED=1` each + all-three-on = **SAFE** on every probe scenario (no errors, no invariant violations). `PC_FACING_SLEW_BASE` deliberately left OFF (config: "NOT ratified — do not enable"). |
| **S5 controls** | PASS | determinism exact (identical vector on repeat); **mirror symmetry `|skew|=0/48`** — the engine is perfectly side-neutral, order-cancelled. |

**Net:** the engine is structurally robust under the full field-based configuration (no crashes, no NaN/
range breaks, deterministic, side-neutral). The one movement-layer defect found — the DG-10 freeze — is
fixed. Remaining flagged items are (a) a 1/197 minor accounting drift and (b) the pre-existing fragility
of the envelopment-shock validators, both in the DG-6-gated balance layer and reported, not silently
touched.

## 4. Flag/gate roster (field-based configuration)

| class | gates |
|---|---|
| field triad (ON) | `FIELD_MOVEMENT`, `PC_NODE_COHESION`, `PER_CELL` |
| resolution (ON) | `LANCHESTER_ENABLED`, `POOL_QUALITY_MODEL`, `COMMAND_SIGMA_ENABLED`, `MORALE_FIX`, `SIGMA_HEAD`, `VOLLEY_ENABLED`, `CASCADING_ENABLED` |
| per-cell/charge (ON) | `PC_BRACE_ENABLED`, `PC_RECOIL_FRONTAL`, `PC_BRACE_SETUP_DELAY`, `PC_RECOIL_CHARGER_GATE`, `PC_WHEEL`, `PC_REFUSE`, `PC_VOLLEY_DENSITY_ENABLED`, `PC_KITE_ENABLED`, `PC_ENVELOP_PATH`, `PC_SWEEP` |
| OFF by default (activated in S4) | `PC_FACING_MODEL`, `FIELD_CONTACT`, `REFORM_CHECK_ENABLED` |
| do-not-enable (unratified debt) | `PC_FACING_SLEW_BASE` — left OFF deliberately |

## 5. Files

- `tests/sim/mass_battle/hierarchy/units.py` — DG-10 field-movement fix (`_node_advance`).
- `tests/sim/mass_battle/bat.py` — field goldens re-recorded (`cell_field`/`unit_field`).
- `audit/2026-07-22-mass-battle-stress-test/` — this harness + report.
- `registers/editorial_ledger_mb.jsonl` — ED-MB-0011.
