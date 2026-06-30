# Mass-Battle Engine — Anti-Pattern Census

**Date:** 2026-06-30 · **Directives (3)(4)(5):** find every pattern-match / top-down imposition /
arbitrary weight / assertion; confirm what is and isn't bottom-up; assess evidentiary grounding.

`[SELF-AUTHORED — bias note: verdict-first; every finding is file:line-anchored to the working tree.]`

---

## 0. The bar (from the approved plan)

**No mechanical *value* may be an assertion.** A value is acceptable only if **derived-from-primitive**.
A *law/relationship* may be **academic-cited** (it parameterizes a derivation, supplies no magnitude).
**Historical data is validation-only** — it gates emergent *behavior*, it never licenses a *number*.
A value that exists only because it matches a band is **calibrated-debt** (a temporary state that must
carry a retirement gate to `derived`); a value with no source at all is **ungrounded** (a CI failure).

So the census classifies each finding by what it currently is and what primitive it must derive from.
The provenance registry in `03_provenance_ledger.md` tracks the disposition machine-readably.

---

## 1. Findings (each: file:line · class · disposition)

### F1 — `cell_speed` shape-name switch · PATTERN-MATCH/ASSERTION · `geometry.py` L335–363
A 7-way `if shape == "X"` returning hardcoded speeds (`2`/`1`/`0`) plus three tier→size dicts
(Horseshoe wing `{1:2,2:2,3:3,4:3}`, etc.). "The Arrowhead tip moves at speed 2" is asserted, not
derived; the Leuctra comment justifies a *name*, not the number.
**Disposition (i) DERIVE** → `cells/kinematics.momentum(cell, advance_vec, footprint)`: a leading cell
has fewer cells ahead along the advance vector → higher local momentum. "Tip is faster" then *emerges*.
The literal `2` disappears.

### F2 — table-driven `*_cells` dimensions · LOOKUP-TABLE/ASSERTION · `geometry.py` L19/33/47/60
`line_cells sizes={1:(3,3),2:(5,3),3:(5,5),4:(7,5)}`; same shape for `horseshoe`/`gapped_line`/
`refused_flank`. Why Horseshoe-T3 = (3,3)? No formation was exactly 3×3; the comment "sized to match
Line cell count" gives a *constraint*, not a derivation.
**Disposition (i) DERIVE** → route all layout through the existing `footprint_for` solver (geometry
L122): frontage = troops × drill-spacing(troop_type) ÷ depth, with depth taken from the formation's
geometry record in `research/pre_firearms_formations/`. Retire the four tier tables.
*Counter-evidence the bar is reachable:* `arrowhead_cells` (L9) and `column_cells` (L25) are **already
generative** — a triangle algorithm and a transposed line. The four offenders are the holdouts.

### F3 — `DAMAGE_BY_DEGREE` lambdas · ASSERTION (value) / OK (shape) · `config.py` L72
`{"Overwhelming": 1+p, "Success": p, "Partial": 1, "Failure": 0}`. The *degree→multiplier shape* is a
cited convention (params/core.md); the magnitudes (why `Partial=1` flat?) are asserted.
**Disposition (ii) law-cite + DERIVE** → move to the troop-atom as a per-soldier lethality primitive;
the degree *ladder* is law-cited, the magnitude is the atom's lethality, not a free lambda.

### F4 — `SUPPORT_WEIGHTS` depth decay · ARBITRARY-WEIGHT · `config.py` L31 (`{1:1.0,2:0.7,3:0.5}`, floor `0.3`)
Depth-2 contributes 70%, depth-3 50% — exponent unsourced.
**Disposition (iii) DERIVE-THEN-VALIDATE** → `_support_along_vector` (geometry L186) already weights
supporters by perpendicular distance along the attack lane (the generative form). Migrate
`support_engage_frac` onto it; validate H3/H5/H8 hold.

### F5 — `MIN_DISCIPLINE` per-shape gate · LOOKUP-TABLE · `config.py` L61
`{"Line":1,"Arrowhead":4,"Horseshoe":5,"GappedLine":5,"RefusedFlank":3,"Column":3}`.
**Disposition (ii) law-cite + DERIVE** → ED-815 supplies the *law* (a more complex shape needs more
drill to hold); the value derives from shape complexity (cell-count / aspect irregularity), not
per-name literals. Open: hard gate vs smooth drift (`pc_formation_system.md` §9.3).

### F6 — morale caps `−3` / `−2` · MAGIC-THRESHOLD/CALIBRATED · `config.py` L47 `MORALE_PHASE_CAP=3`; applied `morale_check_phase` `orchestration.py` L290–317
The `−3` cascade cap is canonical (mass_battle_v30 §A.4) and du-Picq/Clausewitz-shaped, but the
magnitude is asserted; the `−2` general term reframes to incapacitation (workplan P-B).
**Disposition (ii) law-cite, magnitude is calibrated-debt** → the cap *law* (graded collapse, bounded
per phase) is cited; the magnitude derives from the morale-erosion-per-casualty primitive or is logged
as calibrated-debt with a gate. Never kept as a bare `−3` with no derivation.

### F7 — `PC_*` σ magnitudes (~20) · CALIBRATED-TO-BAND · `config.py` L82–117
`PC_STAM_SIGMA=1.5`, `PC_CHARGE_SIGMA=0.55`, `PC_SHOCK_FRONT=0.15`, `PC_SHOCK_REAR=1.6`,
`PC_CHARGE_RECOIL=6`, `PC_KITE_STANDOFF=5`, `PC_SHOCK_DISC_FULL=0.35`, … Several comments are explicit:
"CALIBRATED vs Courtrai/Swiss/Waterloo", "Stage-4 calibration vs Waterloo-square bands" — i.e. the
value was tuned until the sim matched, the inverse of derivation.
**Disposition (iii) per-constant split** → each splits into a **structural ratio** (front<flank<rear;
brace×disc×depth gates — these are du-Picq *shapes*, law-cited and kept) and an **absolute magnitude**
(derive from charge-mass / closing-velocity primitives; collapse the ~9 shock dials toward **one**
momentum-derived charge-shock scale). Magnitudes that survive only as band-fits are **calibrated-debt**
with a retirement gate; if they cannot be derived they are **removed**, not asserted.

### F8 — Lanchester coefficients · LAW OK / COEFF CALIBRATED · `config.py` L39/125/126
`CASUALTY_SCALE`, `K_LINEAR=12`, `K_SQUARE=0.25`. The **law** is academic-cited (Hillestad/Taylor/
Armstrong; `mass_battle_gauge_grounding.md` §1; `mb_lanchester_design.md`). The coefficients are
legitimately calibrated.
**Disposition (ii) GROUND-as-law + DERIVE coeffs** → move the law to `core/attrition.py`, inject coeffs
derived from block-size × per-soldier-lethality × contact-frontage primitives; residual is gated debt.

### F9 — `ANGLE_DEF_MOD` 0/−1/−2 + octagon 45°/90° · FACING TABLE · `config.py` L65; `geometry.py` octagon (`octagon_angle`)
The octagon thresholds are geometric face-boundaries (already derived); the `0/−1/−2` vulnerability is
du-Picq flank/rear (validated by C4/C7).
**Disposition (ii) law-cite + DERIVE** → magnitude derives from how much of a cell's frontage the
attack angle exposes; the *shape* (flank worse than front, rear worst) is law-cited.

---

## 2. What is NOT an anti-pattern (the bottom-up core — directive 4)

To keep the census honest: the following are genuinely emergent and must be *preserved*, not "fixed":
- **Cells/columns** as spatial primitives (`_ColBlock` percell L10; `build_column_grid` percell L25
  derives frontage+depth from the live footprint).
- **Lanchester attrition** as a law application (linear melee / square volley) — the magnitude question
  is F8, but the mechanism is correct and grounded.
- **du-Picq graded morale σ** (`_morale_sigma` resolution L45) and **charge-shock σ**
  (`_charge_shock_sigma` resolution L83) as *shapes* gated by stance/discipline/depth/facing.
- **Per-subunit rout/stamina/stats** (ED-1016/1017/1019) — the substrate for multi-scale.
- The **retired** `SHAPE_OFF_MOD`/`SHAPE_DEF_MOD` (config L58) — the precedent proving flat-bonus
  elimination is the house style, not a novelty.

## 3. Evidentiary grounding scorecard (directive 5)

| Grounding | Items |
|---|---|
| **Strong (academic-law, DOIs)** | Lanchester linear/square; du-Picq graded morale; cavalry regime bands (Sidnell/Burkholder/Boddy/Barua); per-subunit rout/relief (Sabin/Zhmodikov/du Picq/Clausewitz) — `mass_battle_gauge_grounding.md` §1–8. |
| **Law cited, value asserted** | F3 damage ladder, F5 discipline gate, F6 morale cap, F9 facing — the *shape* is sourced, the *number* is not. |
| **Calibrated-to-band (debt)** | F7 `PC_*` magnitudes, F8 coefficients. |
| **Ungrounded (CI failure target)** | F1 cell speeds, F2 cell dimensions — the four table shapes + the speed switch. |

## 4. Top-down validation status (directive 6 — detail in `04_validation_and_scale.md`)

The gauge validates 11 historical bands top-down and explicitly **does not lower bands to pass** — a
divergence is flagged. This is the correct relationship (history validates behavior). Two gaps:
(a) validation is unit-scale only; the subunit layer is inert in default runs, so the "unit vs subunit
vs cell" deployment the directive requires is not exercised; (b) bands are outcome-level (who/how wins),
not per-turn casualty traces — acceptable as behavioral gates, and intentionally *not* value checks.

## 5. Summary

8 of 9 findings are isolated to two files (`geometry.py`, `config.py`); the resolver and per-cell
mechanics are sound. The dominant anti-pattern is **shape-name lookup** (F1/F2) — pure assertion, the
Stage-2b derive targets — followed by **calibrated-to-band magnitudes** (F7/F8) — the Stage-5
debt-retirement targets. None require rebuilding the substrate; all are derive-or-remove against
primitives the engine (and `research/pre_firearms_formations/`) already provides.
