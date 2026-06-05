# Mass-Battle Engine — Scale-Atomization Audit
**2026-06-05 · Stream B · grounds builds A–E**

## Frame

Every mechanic resolves at one of three scales:

- **Unit / formation** — a scalar per unit (`Unit` fields: power, command, discipline, morale, hp, size, stamina, routed/broken). One number stands for the whole body.
- **Subunit / subformation** — `Subunit` owns shape, stance, targeting (`order_target_idx`/`target_condition`/`maneuver`) and *contains* the cells. Per-subunit rout exists (`SUBUNIT_ROUT_FLOOR`).
- **Cell / troops** — the atomic substrate: `cell_troops` (count), `cell_offsets`/`cell_offsets_c` (position), `cell_facing_vec` (facing), node-cohesion (`_node_pos`/`_node_rel`). Behaviour is meant to *emerge* from here.

**Atomization principle (why it matters).** A mechanic is *atomized* when it reads/writes cell-or-troop state, so outcomes emerge bottom-up. A mechanic is *de-atomized* when it operates on a unit/subunit scalar that flattens the cells beneath it. De-atomization is the failure mode behind the inert envelopment: the flank bonus computes per-cell angles but **gates the bonus on a unit-scalar (frontage width)**, so a detached same-width flanker — geometrically on the flank at the cell level — is invisible to the gate.

**This audit does not assume "atomize everything."** Some scalars are *correctly* unit-level (a general's Command is a unit property by nature). Each de-atomized mechanic gets an explicit *should-atomize* verdict with a reason.

---

## Scan — mechanics by scale and atomization status

### Already atomized (cell/troop) — emergence works here
Movement and space are fully atomized: `advance_cells`, `_node_advance`, `_maneuver_target`, `get_cell_facing`, `_oriented`, `centroid`, `cells`/`iter_cells`, `find_contacts`, `resolve_cross_side_contention`, `resolve_internal_collisions`, `distribute_casualties` (damage spread across `cell_troops`), and the geometry primitives (`octagon_angle`, `cell_facing`, `_support_along_vector`, `cell_speed`, shape generators). **Verdict: keep.** This is the substrate the rest should lean on.

### Column-aggregate (cell→column, partially atomized)
`build_column_grid`/`sync_col_grid`, `_fatigue_sigma`, `_defender_depth`, `update_stamina`, `_lanchester_strength`, `_volley_density_mult`. Columns are rebuilt from cells each tick (`sync_col_grid`), so they track the atomic state. **Verdict: keep at column.** A file tires/wraps as a body; per-cell would add cost without behavioural gain. (du Picq's fatiguing front is a column phenomenon, not a per-man one.)

### Subunit-scale
`assign_targets`/`_pick` (target selection), `role_at_contact`, `count_engagements_per_atom`, `_atom_distance`, the `maneuver`/`target_*` fields. **Verdict: correct scale** — a subunit is the natural unit of tactical intent (who it targets, how it approaches).

### Unit-scale scalars — the de-atomization surface
| Mechanic | State | Atomized? | Should-atomize? |
|---|---|---|---|
| Flank/rear bonus (`_per_cell_angle_mod`) | per-cell angle **gated on unit frontage-width** (wrapper) | **partial — gate is the problem** | **YES → A.** Bonus must fire per-cell when *any* attacker cell sits in a defender cell's flank/rear arc and that cell is pinned — independent of unit width. This is the inert-envelopment root cause. |
| Morale (`morale_check_phase`, `_morale_sigma`) | one `unit.morale` | **no** | **YES → subunit (B-adjacent).** A flanked subunit should waver locally while the rest holds (Cannae's wings break first); a single unit scalar erodes everyone uniformly and cannot model local collapse. |
| Discipline *disruption* (cohesion) | one `unit.discipline` | **no** | **YES → cell/subunit via node-cutoff → B.** Discipline-as-cohesion should be *locally* disruptable: a sudden new-front hit suspends the node-relational hold for N ticks (cells scatter) + a temp discipline penalty on the struck subunit — not a uniform unit decrement. |
| Volley targeting (`volley_phase`/`fire`) | unit `Power` pool; density mult is cell-aware | **partial** | **PARTIAL → E.** Power-as-capability is fine unit-level; *target selection* should atomize (a flanker/archer-hunter picks the enemy archer subunit, ideally its exposed cells). |
| Exchange pool (`resolve_engagements`, `command_base_pool`) | per-engagement pool from unit Command/Power + cell-frontage (Lanchester) | **mixed — correctly** | **NO.** Command/Power are leadership/quality — inherently unit-level; numbers already enter through the cell-derived frontage term. Atomizing Command would be wrong (a general commands the unit, not a cell). Keep mixed. |
| `unit.stamina` | unit scalar (legacy) beside column stamina | redundant | **NO (dedupe later).** Column stamina is the live atomized path; the unit scalar is vestigial — a hygiene item, not an atomization gain. |
| Rout (`rout_resolution`) | `unit.routed/broken` + per-subunit `SUBUNIT_ROUT_FLOOR` | **partial (subunit floor exists)** | **LOW.** Per-subunit rout already exists; whole-unit rout on top is acceptable (a broken core routs the body). Revisit only if local rout/morale (B) makes it salient. |
| `_charge_shock_sigma` | cell facing-zone → applied to unit offence; charge-gated | **mixed** | **PARTIAL → A/B.** The zone read is atomized; generalise its *trigger* (charge-only → any sudden flank/rear contact, A/B) and let it bite a *subunit's* local effectiveness once morale is subunit-scale. |
| `_envelopment_sigma` (percell) | unit column-count overhang (width) | **no — and DISABLED** (`PC_ENVELOP_SIGMA=0`) | **N/A.** Already dormant; the width model it encodes is exactly what A replaces with per-cell flank detection. Leave dead. |

---

## Validator framework (top-down goal-shaping — never mechanics)

**Contract.** A validator is a *test*: it runs a scenario and asserts the engine's **emergent** behaviour matches a historical/theoretical goal. It **never** sets a modifier, gates a condition, or orchestrates an outcome. It shapes *what the bottom-up mechanics must achieve*, then checks they did. If a validator fails, the *mechanic* is wrong, not the validator — and the fix lives in the atomized mechanic, never in the validator.

**Form.** `validators/historical_goals.py` — each goal a function returning `(pass: bool, measured, expected_band, anchor)`. Run as a suite; report pass/fail with the measured value. They consume only public battle outputs (winner, casualties, positions, traces), never engine internals they could perturb.

**Goal schema (the top-down lens for A–E):**
- **V-CANNAE (A).** A detachment striking the flank/rear of a unit *pinned* frontally inflicts a measurable defender disadvantage vs an unpinned/frontal control. *Anchor: Cannae 216 BC; du Picq — the unseen attack.*
- **V-FIXING (A/D).** Removing the pin (no holding force) collapses the envelopment advantage — the bonus is *conditional on the enemy being fixed*, not on mere flank position. *Anchor: the pin-and-flank doctrine.*
- **V-SHOCK (B).** A unit hit on a new front while engaged loses local cohesion (scatter / temp discipline) beyond its morale erosion, transiently. *Anchor: du Picq surprise; flank-shock disproportion.*
- **V-SQUARE (existing).** A braced, deep, disciplined wall facing a cavalry charge is near-immune; shallow/green is ridden down. *Anchor: Waterloo / Courtrai.* (Already ~held by the recoil calibration.)
- **V-WIDTH (existing).** Equal-quality wider line beats narrower via frontage. *Anchor: Lanchester linear.* (Held by counters.)
- **V-ARCHER (E).** Archers caught in melee from the flank are destroyed disproportionately (weak in melee + unfaced). *Anchor: light-troops-ridden-down.*

These formalise what the counters (`deepColumn>thinLine`, `ShieldWall>Wedge`, `command-dominates`) already do informally, and extend the schema to the envelopment doctrine.

---

## Build sequence (mapped to verdicts)
- **A** — atomize the flank-bonus gate: per-cell flank/rear detection of a *detached* attacker against a *pinned* defender cell, replacing the unit-width wrapper gate. Validated by V-CANNAE + V-FIXING. *(Counters/fuzz must stay byte-exact when no detached flank exists.)*
- **B** — shock on new-front contact: temp discipline penalty + N-tick node-cohesion cutoff (cell scatter), local to the struck subunit. Validated by V-SHOCK. (Pairs with subunit-morale atomization.)
- **C** — maneuver targets flank/rear cells, not nearest; commit only once around.
- **D** — wired fixing/pin role (hold contact, deny disengage).
- **E** — sweep/horizontal path mode + atomized volley/flanker targeting of archers. Validated by V-ARCHER.
