# Mass-battle field-based stress test — 2026-07-22 (MB lane, ED-MB-0011 + ED-MB-0012)

> **Two landings on this branch.** §1–§6 are the DG-10 movement-freeze fix (**ED-MB-0011**, merged
> as PR #207). §7 is the follow-up **spatial-model v2 Stage B+C** (**ED-MB-0012**): the CIRCLE→OBB
> contact upgrade + the *collide-not-decelerate* correction (analytic swept-SAT TOI; halt on the BODY
> box, engage across the reach gap). See `spatial_model_v2_plan.md` for the full staged plan.

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
velocity the way the field engine can (the two are unreconciled, ED-IN-0074 D5). Representing 0.4/0.7
cells/tick on the grid would need the accumulator (rejected) or float positions (breaks integer
contact), so the fix **clamps to the grid's minimum quantum** — an advancing body takes at least one
whole cell instead of a frozen zero. **Disclosed cost (surfaced by the adversarial pass, §6):** this
flattens the sub-disc-5 speed gradient — disc 1/2/3/4 all advance at 1 cell/tick here, where the field
engine faithfully keeps 0.4/0.4/0.7/0.7; the field engine is the faithful one, this is an unfreeze
stopgap for the wired engine. Discipline≥5 (incl. the wired `resolve_mass_battle` default of 5) is
**byte-identical** (`round(1.0)==floor(1.0)`; an adversarial A/B incl. mid-battle degradation and
volley-under-approach found no disc≥5 outcome that differs — degradation lags contact when movement is
already moot). Guarded by `tests/valoria/test_mass_battle_systems_movement.py` (8 tests: per-disc
closing isolation + all-disc aggregate + disc≥5 regression/determinism).

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

- `tests/sim/mass_battle/hierarchy/units.py` — DG-10 field-movement fix (`_node_advance`, faithful float velocity).
- `tests/sim/mass_battle/bat.py` — field goldens re-recorded (`cell_field`/`unit_field`).
- `systems/mass_battle/sim/units.py` — DG-10 fix in the **wired** engine (`advance_cells`, grid clamp-to-1).
- `tests/valoria/test_mass_battle_systems_movement.py` — wired-engine movement tests (8).
- `audit/2026-07-22-mass-battle-stress-test/` — this harness + report + `spatial_model_v2_plan.md`.
- `registers/editorial_ledger_mb.jsonl` — ED-MB-0011 (DG-10), ED-MB-0012 (Stage B+C).
- **Stage B+C (ED-MB-0012):** `tests/sim/mass_battle/hierarchy/units.py` (analytic swept-SAT TOI +
  body-stop `resolve_toi_and_commit`), `tests/sim/mass_battle/core/contact.py` (OBB contact predicate),
  `tests/sim/mass_battle/geometry.py` (Stage A OBB primitive), `tests/valoria/test_obb_contact_toi.py`,
  `tests/valoria/test_obb_primitive.py`.

## 6. Adversarial pass (self-review)

Ran an antagonist pass against the two claims most likely to be wrong. Two survived, one landed.

- **A — "Discipline≥5 is byte-identical, so the wired `resolve_mass_battle` path is untouched": SURVIVED.**
  The attack: the wired engine degrades discipline mid-battle (`discipline_check_phase`, casualty-driven,
  incl. volley losses), so a disc-5 unit could drop to disc-4 *before contact* where old=frozen /
  new=moving would differ. Tested it hard — normal battles, long lethal battles that degrade to disc-4,
  and an 8000-archer force over a 33-row approach designed to force pre-contact degradation. **All
  byte-identical old-vs-new.** Degradation lags contact: by the phase boundary where a unit hits disc-4
  it is already in melee, where movement is moot. The claim holds; the *original justification*
  (`round(1.0)==floor(1.0)`) was incomplete and is now corrected to name the real reason.
- **B — "the 4 inert S3 flags are inert-on-scenario, not dead": SURVIVED.** All four are consumed at
  live call sites — `MORALE_FIX` (resolution.py:54), `PC_RECOIL_FRONTAL` (orchestration.py:897),
  `PC_WHEEL` (units.py:1187), `PC_BRACE_SETUP_DELAY` (resolution.py:66). None are dead gates; each
  simply needs a triggering scenario the S3 probe didn't supply (symmetry-cancel / construction-brace
  exemption / specific geometry).
- **C — "the wired fix takes the real velocity": LANDED (disclosure defect, now fixed).** `max(1,
  round(vel))` *clamps* sub-disc-5 velocity to 1 cell/tick, **flattening the speed gradient** (disc
  1/2/3/4 all move at 1, where the field engine keeps 0.4/0.4/0.7/0.7). Calling it "real velocity"
  overclaimed. The fix itself stands — an integer-contact grid can't carry sub-cell velocity without
  the rejected accumulator or float positions — but the wording in `units.py`, this README, and the
  ledger is corrected to name it a clamp/stopgap and point at the field engine as the faithful one.

## 7. Spatial-model v2 Stage B+C (ED-MB-0012) — CIRCLE→OBB contact + collide-not-decelerate

Follow-up to DG-10, executing Stages B+C of `spatial_model_v2_plan.md` (Jordan-directed "Euclidean
motion, boxed footprint"). Two parts.

### 7.1 Analytic swept-SAT time-of-impact (perf)
The parked Stage B+C prototype computed each cell-pair's contact fraction with a **scan+bisection** on
`obb_front_reach_overlap` (~200k list-allocating SAT calls/battle → the field path ran 20–60× slow and
stalled the producing agent). Replaced with a closed-form **`_swept_first_overlap_s`**: over one tick
the box axes and corner-offsets are constant (Euclidean motion translates only the centre), so on each
of the ≤4 SAT axes the strict-overlap condition `band_lo < P(s) < band_hi` is **linear in `s`** — an
`s`-interval. Intersect the ≤4 intervals; the first touch is the window's left edge. O(4)/pair, zero
iteration, ~15 µs/pair. **Verified** against the reference scan+bisection to **max error 1.7e-15 over
700 seeded fuzzed pairs** (281 genuine touches, 0 existence/value mismatches) — machine epsilon.

### 7.2 Collide, don't decelerate (the design correction)
Jordan, mid-review: *"why are we decelerating to halt instead of just colliding at whatever speed?"*
and *"wouldn't that break charging?"* — both land on a real bug.

**The bug.** The plan (and the prototype) made the TOI **halt** surface EQUAL the **contact** surface —
both the reach-extended box. That deadlocks: `resolve_toi_and_commit` parks a closing cell EXACTLY on
the `obb_front_reach_overlap` *touch* boundary, where the **strict**-overlap contact predicate returns
False. So contact never fires. Reproduced: a head-on Line-vs-Line **froze at gap 1.5 for the entire
battle, 0 casualties** (`reach_for=0.5` → reach surfaces touch at gap `2·(0.5+0.5)−0.5 = 1.5`), while
clean `main` (circle model) reaches contact. Isolation confirmed it was the contact-surface swap, not
the TOI: TOI-change + *circle* contact still reached contact.

**Why it happened.** Reach was being treated as a *wall to decelerate against* rather than a *weapon
envelope reaching across a gap*.

**The fix.** The hard geometric stop is **BODY vs BODY** — two unit squares (reach 0), the only thing
that physically cannot interpenetrate. **Contact/engagement stays on the reach-extended box** (Stage B,
unchanged). The body surface sits strictly *inside* the reach surface (reach>0 always), so contact
fires as cells close *through* the reach band into body contact. **Bodies collide; weapons reach across
the closing gap.** The stop is symmetric and reach-independent, so the reach **throttle**
(`_reach_throttle`/`_effective_reach`) is retired from the stop path — both cells cap at the shared
body-touch fraction; reach asymmetry (a longer weapon striking first) is expressed by contact firing
earlier for the longer-reach box, not a movement handicap.

**Charging — the answer to "wouldn't that break charging?": no, it RESTORES it.** Charge shock reads
`_momentum_speed` → `cell_last_speed`, which `_node_advance` sets to the cell's **pre-cap intended
step** (the charge velocity). So momentum reflects closing speed regardless of the body cap. Under the
old reach-stop, contact *never fired*, so `_charge_shock_sigma` never triggered at all — charging was
already dead. Post-fix, verified: head-on now closes to **gap 1.0 (body-touch)** and exchanges
casualties over time; a **Fast cavalry charge reaches contact and deals more than it takes on the
impact tick** (turn 8: INF −21 vs CAV −10).

### 7.3 Verification
- `tests/valoria/test_obb_contact_toi.py` (7): contact-fires-at-OBB, head-on **no body-interpenetration
  + no-stall**, **cavalry-charge-reaches-contact**, grid-path-**never**-calls-OBB (poisoned primitive),
  conservation (I1), determinism (I2). + `test_obb_primitive.py` (21, Stage A). **28 passed.**
- **I4 grid oracle untouched:** `resolve_toi_and_commit` runs only under `if FIELD_MOVEMENT`
  (`orchestration.py:1405`); the FIELD_MOVEMENT=0 byte-exact oracle is structurally unreachable.
  `test_mass_battle_byte_exact.py` → **`2 passed`** (grid `unit`/`cell` byte-identical).
- Full mass_battle/obb/field/movement subset → **57 passed, 13 skipped, 0 failed**.
- FIELD behaviour changes by design (bodies now close to touch and fight instead of standing off at
  gap 1.5 doing nothing) → `bat.py` field goldens (`cell_field`/`unit_field`, NOT CI-checked)
  re-recorded. **This moves the DG-6-gated 20-row Cannae gauge** (units that used to freeze at range
  now engage) — disclosed; **no balance constant tuned** (I5).

### 7.4 Departure from the written plan (flagged for merge-ratification)
Plan Stage C + risk R1 said halt == contact surface ("halt distance must equal the contact trigger").
The body-stop correction **departs from that shared-surface premise** — halt on the body, strictly
inside the reach-contact surface. `spatial_model_v2_plan.md` Stage C and R1 are amended to record it.
Per CLAUDE.md §2 (merge ratifies PROPOSED contents), merge-review of this PR ratifies the correction.

**Remaining v2 stages:** D (continuous frontage / delete the last recording integer), E (weapon-class
reach 0.1/0.2/0.3 + author a `pike` troop type), F (historical revalidation + digest re-record),
G (retire the integer engine, route `resolve_mass_battle` onto the field engine).
