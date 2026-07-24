# Mass-Battle Full Implementation Plan — Part-A flips + Part-B fixes + per-troop damage model

**Status: PROPOSED (steering surface for the multi-stage effort).** Jordan directive 2026-07-24:
*"implement all proposals. nothing is golden here."* The byte-exact golden constraint is **lifted** —
goldens become a re-recorded regression snapshot, not a freeze. Companion to `fable_logic_audit_v1.md`
(the Part A/B findings) and `honest_gauge_readout.md` (the ruler).

## 0. The regime inversion (read first)

- **The honest gauge is now the primary correctness oracle** — the 20-row Dupuy/Sabin history bands
  (`gauge_mb.py`). A change is *good* when it moves rows **into band for a grounded mechanistic reason**,
  never when it merely fits the band.
- **Goldens (`bat.py`) become a re-recorded regression snapshot**, refreshed after each landed stage to
  catch *unintended* drift. Every `PC_*` flag is **kept** (Jordan-ruled: A/B ablation is how we measure
  emergence); defaults flip as explicit ratification steps.
- **Every stage is its own small PR:** reproduce the audit ablation → fix → re-record goldens →
  re-measure gauge → independent read-only adversarial critic → commit + ledger (`ED-MB-NNNN`). No
  mega-PR. Every numeric constant cited (anti-fabrication discipline stands).

## 1. The per-troop damage primitive (Jordan directive 2026-07-24) — the substrate for Phase 2

> *"The damage any cell emits is modulated by density (troops in cell), the troop type's weaponry, the
> troop's experience/quality, intent (defend↔aggress continuum), and morale. Consider each troop as an
> isolate/sub-primitive with its own quality, weapon, intent; aggregate their actions in one cell for the
> density, then abstract to manage the scale."*

Formalized:

```
per_troop_emission = f(weapon[troop_type], quality[experience/discipline], intent[defend↔aggress], morale)
cell_emission      = Σ_troops per_troop_emission   =   density × per_troop_emission   (homogeneous cell)
```

**Scale abstraction:** do NOT iterate individual troops. The σ-leverage head resolves the per-troop
**quality** factors (weapon × quality × intent × morale, each a Δσ) into a **net → degree** — "how good
is one troop's blow." The troop **count** (`density × engaged_frontage`) is a **linear magnitude**
multiplier on the resulting damage. Two orthogonal channels:

| channel | driven by | enters as |
|---|---|---|
| **degree** (quality of the exchange) | weapon, quality, intent, morale — all *per-troop* | Δσ in the σ-head → `compute_degree` |
| **magnitude** (how much) | troop **count** = density × engaged frontage | LINEAR multiplier on casualties |

**This resolves B4 by construction:** count must NOT appear in the degree (that is the double-count).
Strip `eff_size` out of the pool's degree computation; keep it as the linear emitter-count on damage.
This is "casualties-only linear," re-grounded in the primitive rather than a Lanchester assertion.

## 2. Phases (ordering is load-bearing: frame → accounting → behavior → calibrate)

### Phase 0 — Repair the ruler before calibrating to it *(no engine behavior change)*
The gauge battery itself is bent (audit gauge-lane): **C6 is a byte clone of C2** (no braced-shallow
control), **R3 never fires** (hold at 18 rows vs volley range 8 → all-draw), explicit wing placements in
`_envelop_army`/`_refused_army` suppress the echelon/apex geometry H5/H6 cite. Fix the battery; add a fast
gauge runner + a per-finding **ablation-repro harness** (each Phase-1+ fix begins by reproducing the
audit's ablation number, then shows the fix moving it). *Foundation; low risk.*

### Phase 1 — The geometry frame (root of the out-of-band rows)
> **Coupling discovered 2026-07-24 (measuring B1 in isolation):** B1 fixes the wedge (H2 0→37.5 as the
> audit predicted) but the **braced-wall C-rows regress** (`REPELLED`→`NOT-REPELLED`, C2/C6 cav wins
> 87.5%). The brace-repel was silently relying on the broken `(0,0)`-collapsed contact map feeding the
> charge-shock / `_wall_prep` / defender-depth inputs. **Consequence:** B1+B2+B3 + the **B5 charge-zone
> fix** are coupled through the contact map and MUST land as ONE coherent set, measured together — B1
> alone commits a net gauge regression (5/20→4/20). Do NOT land the frame pieces piecemeal.

- **B1** (CRITICAL, verified) — `_oriented_abs_map` node branch (`geometry.py:252`) iterates
  `oriented_pattern(shape,tier)` but keys `_node_pos` by the continuous `_build_shape_n` ids; the
  `.get(..., (0,0))` default silently collapses every mismatch to the origin (Arrowhead: 1/6 ids match →
  contact `[]` → pool floored). Fix: iterate `_oriented(atom)`; skip ids absent from `_node_pos` (no
  origin default). *Repro: H2 0/100 → 33/67.*
- **B3** (HIGH) — octagon/facing (`_per_cell_angle_mod`/`_octagon_dmg_mod`) run off the dead
  `starting_position + cell_offsets` lattice; route onto the same live `_node_pos` identity map (shares
  B1's substrate). Fixes flank/rear muting for every moved unit.
- **B2** (CRITICAL) — `col_grid`/`_fatigue_sigma`/`update_stamina` key `b.col` by SPAWN columns vs live
  contact files → GappedLine fatigue immunity. Rebuild the column grid from live file bins per tick;
  re-center `ANCHOR_MAP` for the 6-cell footprints. Also fixes B2b (`distribute_casualties` engaged-front
  filter) and `_defender_depth`. *Repro: H7 87/13 → 27/70, H1 → 50/50.*

### Phase 1.5 — SYSTEMIC FINDING (2026-07-24): the geometry layer needs a coordinated rebuild
Building the frame revealed the honest (density-matched) gauge exposes systemic failures, not isolated
bugs — **only ~4/20 rows pass**, and the dominant one is **envelopment delivering 0%** (H3/H4/H5/H6 all
0/100; C4 = 6). The density-match (ED-MB-0027, merged) correctly removed the density artifact that used to
drive envelopment to 100%, exposing that the flanking geometry delivers ~nothing at matched force. Root:
an enveloping army (center + wings) *loses* to a single line because the split center is crushed before the
wings arrive — the "Cannae centre marches forward instead of holding" problem. This couples:
- **intent** (ED-MB-0029, gated OFF) — the Cannae centre must HOLD to pull the enemy in; flip it on.
- **B6** — multi-side shock is computed per cascade sub-phase, so it never fires for a front+rear body.
- **wing timing/pathing** — the wings must reach flank/rear before the centre breaks.
- **B3 octagon** (now fixed) — the flank/rear damage multiplier now reads the live map.
**Consequence:** the gauge will not climb until several mechanics land *together* (intent-on + B6 + wing
timing + brace box-model + fatigue col-grid). Land the correct field-coordinate fixes (B1/B2/B3) first as
tested increments, then rebuild envelopment+intent+B6 as a coordinated set, THEN calibrate.

### Phase 2 — Damage model reformulation (per §1) + accounting
- **B4 / per-troop model** — strip `eff_size` from the degree; density = linear emitter count on
  casualties. Config toggle (`MB_NUMBERS_MODEL`, default `linear`) so the alternative (numbers-in-pool)
  stays measurable. Make `per_troop_emission` explicitly weapon×quality×intent×morale.
- **B6** (HIGH) — compute multi-side shock / encirclement / fixing **once per tick** (like `conv_scale`),
  not per cascade sub-phase → encirclement actually fires (Cannae).
- **Lethality re-baseline** (Jordan: *"far too much damage too quickly"*) — with the model corrected,
  re-tune `K_LINEAR`/`CASUALTY_SCALE`/`DAMAGE_BY_DEGREE` so battles run a realistic **30–90 min** AND
  stochastic-rout breaks distribute across **15–30%** instead of overshooting in ~1 turn.

### Phase 3 — Orders / charge / movement behavior
B5 (charge/recoil zone from the true arc, not the `PC_REFUSE`-bundled `angle_mod`), B7 (`assign_targets
'weakest'` liveness filter — skip 0-troop/routed corpses), B8 (`stance:'hold'` stale-movement teleport),
B9 (DG-2 yielding actually gives ground — exempt `yield_active` cells from the halt), B10 (retreat/yield
step-cap only on closing motion), then the B11 MEDIUM/LOW catalogue batched by subsystem.

### Phase 4 — Flip on + calibrate the Part-A mechanics (`needs_jordan` set)
Frame now correct: flip `PC_INTENT_RESOLUTION`, `PC_STOCHASTIC_ROUT`, `PC_FRACTIONAL_POOL`,
`PC_CLOSE_RANKS` (and the other gated flags) **one at a time**, re-measuring the gauge each step,
calibrating each constant to its **mechanism** (cited), never to the band. Resolve DG-6 over-decisiveness
(ED-MB-0016) here.

### Phase 5 — Rotation model *(DEFERRED per Jordan default — separate follow-on)*
T1 finish (cell coverage shrink), T2 (inter-subunit blended cascading rotation), T3 (bounded decaying
non-death troop recovery). Interacts with the geometry frame → land after the frame is proven.

### Phase 6 — Final validation
All-mechanics-on gauge sweep with documented rationale for any residual out-of-band row; re-record all 4
golden modes as the new baseline; full `pytest` + sim-regression; seeded-campaign win-share sanity (the
degenerate ~87% issue); ratify EDs, update `CURRENT.md` / coverage matrix / HANDOFF.

## 3. Decisions locked (Jordan default, reversible)
- **B4 numbers** → **casualties-only linear** (per §1 primitive), behind a toggle.
- **PC_* flags** → **kept** post-ratification (A/B measurement preserved).
- **Rotation (Phase 5)** → **deferred**.

## 4. Cross-cutting controls
Independent read-only adversarial critic per geometry/accounting fix (structural independence). Ledger
one `ED-MB-NNNN` per stage; `needs_jordan` on genuine design forks. Gauge measured every stage. Keep the
sim-anti-fabrication + naming + register-size gates green throughout.
