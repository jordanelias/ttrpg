# Backwards analysis — mass-battle outcome → primitives → inputs

Traced from a real instrumented battle (field engine, `random.seed(3)`, heavy_infantry Line **A**
vs cavalry Arrowhead charge **B**), 128 unique `mass_battle.*` primitives consumed. Outcome:
`{winner: draw, a_hp_pct: 64.3, b_hp_pct: 78.8, turns: 30}`. Each layer below is what the layer
above *consumed*, with the actual caller→callee edges from the profile trace and file:line for every
primitive/flag/constant. **⚠ = a position-grid integer-snap (the "grids snap to integers" problem).**

## L0 — CONCLUSION: `winner`
`orchestration.run_battle` returns `{winner, a_hp_pct, b_hp_pct, a_morale, b_morale, turns}`. `winner`
is decided from the two units' terminal **routed flag + retained hp**. Consumes nothing new — it reads
the end state produced below.

## L1 — terminal state ← rout + attrition
- **routed** ← `state.rout_resolution` ← `units.derive_rout` ← `units.agg_morale` (troop-weighted mean
  of subunits' `eff_morale`). Trace: `rout_resolution <- phase_boundary(x5)`; `derive_rout <-
  run_battle(x60), rout_resolution(x10)`; `agg_morale <- derive_rout(x70)`.
- **hp** ← the running sum of casualties applied each tick.

## L2 — casualties ← degree × damage
- `percell.distribute_casualties` (trace: `<- run_battle(x60)`) spreads each engagement's losses over the
  target's cells. Magnitude ← `DAMAGE_BY_DEGREE[degree]` (`Overwhelming:1+p / Success:p / Partial:1 /
  Failure:0`, config.py) × `CASUALTY_SCALE` / `K_LINEAR` (Lanchester).

## L3 — degree ← pool roll + σ-leverage
`resolution.compute_degree` (trace: `<- resolve_engagements(x56)`) compares the two sides' rolled pools.
Ingredients, all consumed by `resolve_engagements`:
- `resolution.roll_pool` — d10 successes vs TN. **RNG enters here** (`random.randint(1,10)`, units.py:1389).
- base pool ← `exchange.subunit_combat_pool` (`<- resolve_engagements(x56)`) = **`eff_power × eff_size ×
  POOL_QUALITY_SCALE`** (POOL_QUALITY_MODEL — troop *quality* × *numbers*, Command abandoned, ED-MB-0006).
- `attrition._lanchester_strength` (LANCHESTER_ENABLED) — engaged frontage × density; **numbers** re-enter here.
- σ-head leverage: `_sigma_net_boost` (SIGMA_HEAD) + `_morale_sigma` (MORALE_FIX) + `_charge_shock_sigma`
  (PER_CELL; du Picq moral impulse) + `orchestration._momentum_speed` (PC_REFUSE, envelopment wrap).
- `exchange._pair_engaged_troops` ← `pair_pool_contribution`; `_convergence_scale` (PC_CONVERGENCE_NORM,
  `<- resolve_engagements_cascading(x30)`) renormalizes multi-atom convergence (ED-MB-0004).

## L4 — WHICH atoms fight ← contact detection  ⚠ THE GRID
`compute_degree`/`subunit_combat_pool` only run for pairs that are **in contact**. Contact is decided by
`contact.find_contacts` / `assign_targets` (trace: `<- run_battle(x60/x30)`) which **snap each atom's
continuous float position to an integer cell and test integer-cell adjacency**:
- `contact.py:175` `(int(round(_pr)), int(round(_pc / COL_WIDTH)))`  ⚠
- `contact.py:292-294` `contact_cells_{a,b}.add((int(round(ar)), int(round(ac / COL_WIDTH))))`  ⚠
- `units.py:1017` `_probe = (int(round(nr)), int(round(nc / COL_WIDTH)))`  ⚠
- `units.py:631` `cells()` emits `(int(round(r)), int(round(c / COL_WIDTH)))`  ⚠

**This is the grid the directive bans.** Two bodies at continuous x = 24.4 and 25.6 are "in contact"
or not depending on which integer cell each rounds into — a discretization artifact sitting directly
on the causal path to who-fights-whom, hence to every casualty and the winner.

**⚠ Correction (verified, 2026-07-22).** An earlier draft of this doc claimed `FIELD_CONTACT` was the
"float-native" lever that removes this grid. **That is wrong** — `core/contact.py:303`
`_find_contacts_field` *also* `int(round())`-snaps each atom's `cells_float()` to integer cells
(lines 316/319) and its own docstring says it "reduces **exactly** to OFF adjacency" at the shipped
`CONTACT_REACH=0.0`. An A/B (`FIELD_CONTACT=0` vs `=1`, 10 seeds) confirmed **byte-identical**
outcomes. So there is **NO toggle** that removes the contact grid; the int-round snap is unconditional
on both contact paths. Truly banning it requires a code change to Euclidean **float-distance** contact
(compute adjacency on raw floats, no `int(round)`), which moves the balance gauge and touches the live
field path — a real, DG-6-gated refactor, not a flag flip.

## L5 — positions ← movement (float) + TOI
- `units.resolve_toi_and_commit` (trace: `<- run_battle(x30)`) — continuous time-of-impact collision on
  the float field (this part is already grid-free).
- `units._node_advance` (trace: `<- advance_cells(x60)`) — the per-tick step. **DG-10 fix (ED-MB-0011):
  on the field path `step` is the real float velocity, no `math.floor`** (units.py:869). Velocity =
  `cell_speed(shape,tier) × disc_mult(discipline) (+ stance_mod)(× PC_CAVALRY_SPEED_MULT)`. Residual ⚠:
  the field cell-membership probe still `int(round)`s (units.py:1017) for halted-cell bookkeeping.

## L6 — START / inputs (grid-free)
`build_army` specs → `Subunit.of_type`: **shape, troop_type → (power/discipline/morale via
TROOP_TYPE_STATS §B.2), troops, concentration, stance, instructions, starting_position**; parent Unit
command/dr/speed; + config constants (`CASUALTY_SCALE`, `K_LINEAR`, `POOL_QUALITY_SCALE`, degree
thresholds, `DAMAGE_BY_DEGREE`, `PC_*`); + the **RNG seed** feeding every `roll_pool` d10.

---

## Integer-snap census — two kinds, only one is a "grid"

**A. POSITION GRIDS (banned — discretize continuous position → contact/movement artifacts):**
| site | what it snaps |
|---|---|
| `tests/sim/.../core/contact.py:175,292-294,316` | float atom positions → integer cells for contact ⚠ |
| `tests/sim/.../hierarchy/units.py:631,1017` | `cells()` / halted-probe float → integer cell ⚠ |
| `systems/mass_battle/sim/units.py:158` `max(1,round(vel))` | **my wired-engine DG-10 clamp** — a velocity→integer snap ⚠ |
| `systems/mass_battle/sim/units.py:192` `round(actual_speed*…)` | wired step decomposition → integer offsets ⚠ |
| `systems/mass_battle/sim` `cell_offsets` (int) + integer-set contact | the wired engine is integer-grid *throughout* ⚠ |

**B. Magnitude floors (NOT position grids — quantize troop counts / damage / dice; defensible: you
can't kill half a soldier or roll a fractional die):**
`distribute_casualties` floor · pool floors (`massbattle.py:880-881`, `resolution`) ·
`effective_size` floor (`units.py:1642`) · damage floor (`massbattle.py:972,1462,1522`) ·
`int(my_loss / DISCIPLINE_LOSS_THRESHOLD)` · `random.randint(1,10)` dice.

## Conclusion of the backwards trace
The winner traces back, unavoidably, through **contact detection**, and contact detection is where the
banned grid lives: continuous float positions are `int(round)`-snapped to integer cells to decide
adjacency. Movement was de-gridded by the DG-10 fix (field path). **Contact is the remaining grid on the
live path, and — verified above — NO flag removes it** (both `_find_contacts` and the `FIELD_CONTACT`
`_find_contacts_field` path `int(round)`-snap; they are byte-identical at the shipped `CONTACT_REACH=0.0`).
Banning it = a real refactor to **Euclidean float-distance contact** (adjacency on raw floats, no
`int(round)` / no integer-cell membership), which necessarily shifts the DG-6-gated balance gauge and
touches the live field path — so it is a scoped, verified change, not a flag flip or a blind edit.
The magnitude floors (troop/damage/dice) are a separate, defensible quantization, not position grids.
The wired `systems/mass_battle/sim` engine is integer-grid end-to-end (positions *and* contact — incl.
my own DG-10 `round()` clamp there, itself a ⚠), so it cannot be de-gridded in place; that is the
field↔grid reconciliation (ED-IN-0074 D5).

### What "ban grids" concretely requires (scoped, not yet executed)
1. **Field engine contact** → replace the `int(round)` cell-snap in `core/contact.py` (`_find_contacts`
   / `_find_contacts_field`) and the `cells()` / halted-probe snaps (`units.py:631/1017`) with raw-float
   Chebyshev/Euclidean adjacency at a ratified reach. Re-record field gauge digests; expect a
   DG-6-relevant balance shift (disclose, do not tune).
2. **Wired engine** → it is grid throughout; the honest path is to route `resolve_mass_battle` onto the
   (de-gridded) field engine and retire the integer engine, i.e. the reconciliation — not another
   in-place grid patch.
Both move the balance gauge, so they are done deliberately with A/B evidence, not as a reflex to a
one-line directive. This doc is the map that makes that change targeted.
