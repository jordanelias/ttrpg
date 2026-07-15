# Implementation Plan — Army-Scale Multi-Unit Envelopment

## Status: PROPOSED — LIVE / UN-ADOPTED. Path-B cross-Unit spatial envelopment is a distinct, still-unbuilt mechanism (HANDOFF_MB.md: do not conflate with the Unit-level Envelopment that shipped). Phase-1 never started. HELD FOR JORDAN. [## Status: heading added 2026-07-15]

**Date:** 2026-06-22 · **Status:** PROPOSED (Jordan-vetoable) · **Scope:** mass-battle sim engine (`tests/sim/mass_battle/`); Godot implementation is downstream · **Tier:** mechanical/systemic gap-fill (project-owner contract) — bottom-up from the traced engine, top-down against Cannae + acclaimed spatial wargame design.

## Thesis

The hardest part is already built. The per-cell envelopment-shock — a unit fixed frontally by one body and struck on the flank/rear collapses — is **unit-agnostic at its core**: it triggers off `_front_fixers`, a registry keyed by `id(subunit)` that does not care whether the fixing and flanking bodies belong to the same unit or different units. The only reason cross-unit envelopment does not happen today is that `run_multi_unit_battle` resolves each pairing as an **isolated 1v1 `run_battle`**, so only two units' cells are ever on the grid at once. **The work is not to build envelopment; it is to stop siloing the engagement field, so the machinery that already exists sees across units and envelopment emerges.** Recommended path: phased spatial unification, with the §A.12 morale cascade preserved as a layer on top.

## Current state (bottom-up — traced this session)

`[READ: orchestration.py run_multi_unit_battle L2636-2899, resolve_engagements/_per_cell_angle_mod L1670-1865, _front_fixers/b_fixed_other L1860-1861, function map]` · `[READ: mass_battle_v30.md §A.3 scale L68, §A.3b battlefield L94, §A.12 rout/pursuit L583]`

- **Multi-unit battle exists** (`run_multi_unit_battle`) but as a **1-D lane abstraction**: `pairings` is a list of `(a_idx, b_idx)` engagement lanes, "ordered spatially (adjacent pairs = adjacent on battlefield)." Each turn, each lane runs an isolated `run_battle(ua, ub)` after `reset_positions` places the two units fresh.
- **Cross-lane interaction is abstracted, not spatial:** (a) rout contagion to adjacent lanes (±1 in the list) — §A.12; (b) a **sequential** freed-attacker — after a unit wins its lane it deals bonus flank damage to an *adjacent* lane's enemy; (c) Fast-unit pursuit of routers.
- **Concurrent multi-unit convergence is explicitly stubbed.** The cascade block carries the comment: *"Check other A units in this pair (for future 2v1 support) — for now, same-engagement only has one unit per side."* The authors flagged 2v1 as unbuilt.
- **The seed is unit-agnostic but siloed.** `b_fixed_other = bool(_front_fixers.get(id(atom_b), set()) - {id(atom_a)})` fires envelop-shock when a subunit is front-fixed by any body other than the current attacker. In a single `run_battle` this only ever contains the two engaged units' subunits — so today it fires only *within* one engagement (e.g. the 2-subunit fix+envelop test that validated Cannae last turn).
- **The spatial container is canon.** §A.3b establishes the cell-level 25×25 `BATTLEFIELD_SIZE` grid; §A.3 sets scales (army-scale = Battle/Campaign/War, 500–5,000 soldiers per Size point). The substrate for army-scale spatial play already exists and is canonical.
- **Double-count is already guarded.** Envelop-shock is an `elif` with the charge path (mutually exclusive); `_envelopment_sigma` is held dormant at 0.0 (NERS-N/E). Any generalization must preserve this so cell-level and unit-level envelopment do not both fire (the PP-683 lesson).

## The gap (precise)

Concurrent **N-on-1 fix-and-flank** is not modeled. Cannae was a *simultaneous* envelopment — the wings and cavalry struck the Roman flanks and rear *while* the center fixed them. The engine can only approximate this **sequentially** (a unit wins its lane, then swings to an adjacent lane) and **abstractly** (morale contagion between lanes). Multiple units converging on one unit, fixing it frontally while others wrap its flanks at the same time, has no representation.

## Two architectures

### Path A — extend the lane abstraction (incremental)
Add an N-on-1 convergence rule to the lane model: when multiple A units target one B unit (collapsed/converging pairings), apply a unit-level envelopment penalty reusing the shock magnitude, gated on the convergents actually occupying distinct arcs.
- **Pros:** small; matches the existing architecture; low risk; no contact-detection rework.
- **Cons:** a special-case convergence rule (NERS-E cost — bolted-on apparatus); not true 2-D wrapping; does **not** reuse the per-cell machinery, so it duplicates envelopment logic at a second level (double-count risk against the cell-level shock); the freed-attacker-vs-convergence distinction stays awkward.

### Path B — unify the engagement field (principled target)
Stop running isolated 1v1 engagements. Place every non-routed engaged unit's cells on the single 25×25 grid at their army positions, detect contacts across **all** units, populate `_front_fixers` across all subunits regardless of unit, and run the per-cell resolution over the union. **Envelopment then emerges**: B fixed frontally by A1's cells and flanked by A2's cells yields `b_fixed_other = True` automatically → existing envelop-shock fires.
- **Pros:** envelopment is emergent, not scripted (NERS-S/E win); reuses the unit-agnostic machinery wholesale; matches §A.3b spatial canon and acclaimed design (Total War's emergent flanking, Field of Glory's zone-of-control + flank/rear modifiers); the Cannae behavior falls out of the substrate rather than a rule; the lane abstractions (sequential freed-attacker, special convergence) dissolve into emergent spatial behavior.
- **Cons:** the larger lift — contact detection and `_front_fixers` population must generalize from pairwise to all-units; a persistent multi-unit positioning layer is needed; performance (N units × cells on one grid is O(cells²) without spatial bucketing).

**Recommendation: Path B, reached in phases.** Path A's special-case convergence collides with the very double-count guard the PP-683 work just established; Path B extends the mechanism that already works.

## Recommended phasing (toward Path B)

- **Phase 0 — Spike (cheap thesis validation).** Take the 2-subunit fix+envelop scenario that already fires cross-subunit envelop-shock and re-run it with the fixer and enveloper as **separate units** placed on one grid. If `_front_fixers` / `b_fixed_other` fire across the unit boundary as predicted, Path B is validated for a few dozen lines of harness, before any engine change. (Highest-leverage first step — confirms the core claim or kills it.)
- **Phase 1 — Shared-field static resolution.** Generalize `find_contacts` / `resolve_cross_side_contention` / `count_engagements_per_atom` and the `_front_fixers` population from pairwise `(unit_a, unit_b)` to **all units' cells on one grid** for a *static* deployment (units placed at army positions, no maneuver yet). Envelopment emerges for any given layout. Preserve the envelop-shock `elif` and dormant `_envelopment_sigma` so no double-count crosses the unit boundary.
- **Phase 2 — Army-scale positioning + maneuver.** A unit-positioning layer: units hold distinct 2-D positions and advance / wheel / envelop over turns, so an envelopment *develops* dynamically (the Cannae wings closing) rather than being pre-placed. This is where the geometry becomes the historical maneuver.
- **Phase 3 — Command & control (ED-907).** The envelopment as a *commanded* maneuver — the general directs units, gated on command/discipline per ED-907's ratified 3-level command architecture. The wrap costs command, can fail, and models the historical difficulty of coordinating a converging attack (why Cannae was rare).
- **Phase 4 — NERS + historical re-validation.** Re-run Cannae at army scale; confirm emergent double-envelopment → disintegration (the behavior validated last turn at sub-unit scale, now at army scale); full NERS pass; re-confirm the double-count guard holds across units.

## NERS analysis

- **N (necessary):** the Cannae target and strategic depth (envelopment as a winnable plan against a larger force) require it; without it army battles are parallel duels with morale contagion. Necessary.
- **R (robust):** emergent envelopment gives the player a real spatial strategy (fix-and-wrap) and generates emergent narrative (a flanking maneuver that turns a battle) — robustness gain.
- **S (smooth):** Path B *removes* the lane/spatial seam (one resolution model instead of isolated-duels-plus-abstraction), a smoothness gain; the §A.12 cascade layers cleanly on top.
- **E (elegant):** emergent-from-substrate beats special-case rules — but the Phase 2–3 maneuver/command layers are where elegance is at risk. Keep Phase 1 minimal; do not build a full RTS. The elegance case holds only if envelopment stays emergent rather than accreting bespoke rules.

## Risks + guards

- **Double-count (highest).** Preserve the envelop-shock `elif` and the dormant `_envelopment_sigma` across the unit boundary; do not add a unit-level envelopment term on top of the cell-level shock (that is Path A's trap and the PP-683 lesson).
- **Performance.** All cells on one grid → contact detection scales poorly; add spatial bucketing before the unit count grows. Set the target unit count with Jordan (decision below).
- **Over-engineering (NERS-E).** The maneuver and command layers (Phases 2–3) are the biggest scope risk; Phase 1 alone unlocks static-position envelopment and is the safe first deliverable.
- **§A.12 preservation.** The morale cascade, rout contagion brake, and pursuit must still operate on the unified field — port them as a morale layer, do not drop them.
- **Repo boundary.** This is the sim engine; the Godot port is downstream and out of scope here.

## Decision points for Jordan

1. **Path A vs Path B** — recommend B (emergent, reuses the machinery, avoids the double-count trap). 
2. **Army-scale unit count** — realistic max units per side (2–3? 10+?). Sets the performance target and whether spatial bucketing is Phase 1 or later.
3. **Maneuver/command scope** — are Phases 2–3 (dynamic wrap + commanded envelopment) in scope now, or is Phase 1 (static-deployment emergent envelopment) the target deliverable, with maneuver deferred?
4. **Canon** — army-scale envelopment is currently undesigned; confirm this is a gap to fill (not a retcon) and whether the resulting mechanics should be written back into §A.12 / a new §A-section once validated.

---

## Execution log — 2026-06-22 (decisions locked + Phase 0 confirmed)

**Decisions (Jordan, 2026-06-22).** Path B confirmed — bottom-up emergent, no scripted convergence rules. Work phase by phase in order; validate top-down (historical) *after* the phases. Army-scale envelopment was always intended (Cannae); the engine must handle the full strategy range — single-wing, double-wing (Cannae), partial envelopment — which emergent Path B gives for free, since envelopment arises wherever units converge rather than from per-pattern rules.

**Spatial parameters (reconciled against `config.py`).**
- `MAX_TROOPS_PER_UNIT = 10000` — matches the intended cap. ✓
- `UNIT_GRID_SIZE = 30` (30×30 max unit footprint), `BATTLEFIELD_SIZE = 50` (50×50 field) — the actual grids; the "15×15 / 225-cell" recollection is superseded. A unit occupies a *dynamic* cell subset by density (`CELL_FLOOR = 40` … `CELL_CAP = 200` troops/cell), so a 10,000-troop unit spans ~50 cells (dense) to ~250 (loose), not a fixed 225.
- Depth:width is set by `LINE_ASPECT = 1.4`. The wider, more realistic target (the 25×11 ≈ 2.27:1 sketch) means raising LINE_ASPECT toward ~2.0–2.3 — a one-line generator parameter. [DECISION: set LINE_ASPECT now, or after Phase 1 emergence is validated? Recommend after, so the formation-shape change and the field-unification change don't confound each other.]

**Phase 0 — CONFIRMED (thesis holds at the line level).** `[READ: _front_fixers build L1685-1693, b_fixed_other use L1860-1861]` The envelopment machinery is purely id-keyed and unit-agnostic: `_front_fixers.setdefault(id(_d), set()).add(id(_e))` (build) and `bool(_front_fixers.get(id(atom_b)) - {id(atom_a)})` (use) never reference a unit. The only thing scoping envelopment to two units is the input `pairs` (contacts within one unit-pair) plus the `unit_a`/`unit_b` references in the per-atom pool fractions. Combined with last turn's cross-*subunit* shock (enveloped unit routed 12/15), this confirms: unify the contact field → cross-unit envelopment emerges with **no change to the shock logic**.

**Phase 1 — precise change-set (next phase).**
1. **Cross-unit contact detection.** Generalize `find_contacts` / `resolve_cross_side_contention` to produce `pairs` across *all* units' cells on the field, not one `(unit_a, unit_b)` pair. Add spatial bucketing if the unit count warrants (decision below).
2. **Owner-unit resolution in `resolve_engagements`.** Replace the `unit_a`/`unit_b` assumption in the per-atom pool fractions (`atom.troop_count / unit_X.total_troops()`, `subunit_combat_pool(unit_X, atom)`) with an atom→owner-unit lookup, so each cell's pool uses its own unit's command/total.
3. **Multi-unit field harness.** Place N units at army positions on the 50×50 grid; run the unified resolution over the union of contacts.
4. **No change** to `_front_fixers`, the envelop-shock, or the `elif`/dormant-`_envelopment_sigma` double-count guard — all already unit-agnostic; preserve them exactly.

**Open decisions for Phase 1.** Max units per side (sets whether spatial bucketing is Phase 1 or deferred); LINE_ASPECT timing (above). §A.12 cascade/pursuit must be ported onto the unified field, not dropped.
