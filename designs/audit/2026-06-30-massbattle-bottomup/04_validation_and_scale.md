# Mass-Battle Engine — Top-Down Validation & Multi-Scale Deployment

**Date:** 2026-06-30 · **Directive (6):** emergent results validated top-down by historical data; every
scenario deployable at unit vs subunit vs cell scale.

---

## 1. Current top-down validation (what's already right)

`tests/sim/gauge_mb.py` validates the engine against **11 historical bands** (H1–H11, R1–R3, C1–C7)
documented with academic citations and DOIs in `references/historical/mass_battle_gauge_grounding.md`
(v2.4). The relationship is correct and must be preserved:

- **Bands are derived bottom-up from history/academia, not fitted to engine output.** The grounding doc
  states it explicitly: "the band is not lowered to make the engine pass." A divergence is **flagged**,
  not fitted.
- **Behavioral, not value-level.** The metric is the *decisive split* `decA = A_wins/(A_wins+B_wins)`
  ("who wins when a result is reached"), with the draw rate validated separately. The gauge asserts
  *behaviors* (who wins / how / the casualty-curve shape), never internal constant values — exactly the
  firewall directive (6) requires.
- **Differentiation is emergent.** The cavalry block (C1 contested ≈46% ≠ C2 braced ≈2% ≠ C5 shaken
  ≈95% ≠ C7 envelop =100%) falls out of the grounded mechanics, not band-fitting (grounding §4).

This is a genuine top-down validation harness and stays the G4 gate instrument for every roadmap stage.

## 2. The two gaps

### 2.1 Scale: validation is unit-only; the subunit layer is inert in default runs
The substrate for multi-scale exists — per-subunit stats (ED-1016), stamina (ED-1017), rout/morale
(ED-1019), and the per-column cell layer (`PER_CELL=1`). But:
- The gauge builds units and validates at **unit** granularity; cavalry rows are `PER_CELL=1`-only
  (gauge L227), and `single` mode currently returns all-draws at the tick cap (a tick-cap artifact), so
  bands are only evaluated in `multi`.
- In default runs the subunit layer is **byte-exact-inert** (single-subunit collapses to the unit
  value). So "unit vs subunit vs cell" — the directive's explicit requirement — is **not exercised as a
  first-class capability**; it is latent.

### 2.2 Granularity is selected by scattered env reads, not one model
`PER_CELL`, `SIGMA_HEAD`, `MORALE_FIX`, `LANCHESTER_ENABLED`, `COMMAND_SIGMA_ENABLED` are read
ad-hoc at import (config L74–139). There is no single "what scale am I resolving at?" control.

## 3. The fix — one model, three resolutions of detail

The core resolver already operates on a `SubunitState` (`subunit_combat_pool` orch L1203; per-subunit
drain/rout orch L290–339, ED-1019). Therefore:

> **subunit is the resolver's *default shape*; unit is the degenerate single-subunit case; cell is the
> per-column refinement.** Not three resolvers — one model at three levels of detail.

Introduce one wrapper-level dial:

```
GRANULARITY ∈ {unit, subunit, cell}
```

It selects (a) how many bodies the wrapper's `build_side` instantiates, and (b) which mod-modules are
active:
- `unit` — one subunit per unit; per-cell modules off ≡ today's `PER_CELL=0` (the byte-exact baseline).
- `subunit` — real multi-subunit units; per-subunit morale/stamina/rout active; cells aggregate per
  subunit. The currently-latent middle scale becomes first-class.
- `cell` — additionally build the `col_grid` (percell L25) and activate the cell mod-modules
  (charge-shock, fatigue-σ, wrap) ≡ today's `PER_CELL=1`.

This replaces the scattered env reads with one configuration surface (consolidation, §13 of inventory).

## 4. Gauge extension spec

1. **Every band × every granularity.** Run all 11 scenarios at `{unit, subunit, cell}`. Assert each
   lands its band at each granularity **and** a new **cross-granularity-consistency** assertion: the
   decisive split must not swing wildly across granularities — a large swing is a *bug* (e.g. the known
   pattern that cross-unit envelopment only fires at cell scale). Bands are granularity-invariant in
   expectation; the consistency check is what catches a scale-specific defect.
2. **New finer-scale signature rows** (behavioral, not value):
   - **Sectional rout** (ED-1019): a two-subunit unit with one section gutted — assert that section
     routs while the fresh sibling holds (the line fails piecewise, Cannae/Hastings) and the broken
     section stops contributing. Only meaningful at `subunit`/`cell`.
   - **Lanchester signatures** (`lanchester_signature.py`, `mb_lanchester_design.md` §4.2/4.3): in pure
     melee the larger equal-quality force's survivors ≈ the difference of sizes (linear law); in pure
     volley, concentration advantage scales super-linearly (square law). Requires contact-frontage from
     the cell layer.
3. **Byte-exact toggle-off (G5 invariant):** `GRANULARITY=unit` reproduces `PER_CELL=0` digit-for-digit;
   a single-subunit unit at `subunit` equals `unit` (the ED-1017/1019 invariant already holds). This is
   the safety rail that lets the dial land without behavior drift.

## 5. How this satisfies directive (6) end-to-end

- **Top-down validation:** the 11 bands stay the authority; never lowered; divergence flagged. Adding
  the cross-granularity and signature rows *strengthens* the top-down check without converting it into a
  value check.
- **Multi-scale deployment:** any scenario runs at `unit | subunit | cell` from one model via the dial;
  the subunit layer stops being inert; and Path B (army-scale, `multiunit_envelopment_plan.md`) is the
  *same dial* pushed to N-units-on-one-grid at cell granularity — scale deployment and emergent
  army-scale envelopment are the same unification reached from two ends (roadmap Stages 3 → 4).
