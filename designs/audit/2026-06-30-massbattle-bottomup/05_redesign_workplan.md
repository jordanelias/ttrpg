# Mass-Battle Engine — Staged, Gated, Adversarial Redesign Workplan

**Date:** 2026-06-30 · **Status:** PROPOSED (gated; Jordan-vetoable). Execution is **not** part of the
audit pass — this is the roadmap the audit produces. **Method gate every stage:** bottom-up build from
primitives → audits → adversarial pass → top-down historical validation → byte-exact toggle-off →
editorial co-file + ED → commit.

`[SELF-AUTHORED — bias note: the engine being re-architected is largely Claude-authored; the adversarial
pass (G3) exists specifically to red-team that bias. All magnitudes Jordan-vetoable.]`

---

## 0. Principles this workplan enforces (the acceptance contract)

1. **Wrapper resolves nothing · core resolves only · every module wired** (full clean module split,
   `01_architecture_audit.md` §3).
2. **No asserted values.** Every value is `derived`; only laws are `academic-law`; history is a
   behavior gate only (`03_provenance_ledger.md`).
3. **Everything wired + consolidated.** No inert scaffold; one package, one wrapper entry, one
   validator, one granularity dial (`00_inventory.md` §13).
4. The plan is **not complete until the calibrated-debt count is zero and the provenance CI is
   blocking** (Stage 5).

## 1. The per-stage gate sequence (G1–G6)

No stage advances until all gates are green. A failed audit or adversarial pass sends the stage back to
build. The instruments are existing repo skills + CI.

| Gate | Name | Instrument | Passes when |
|---|---|---|---|
| **build** | bottom-up build | — | new values land `derived` (or explicit `calibrated`-debt with a `retire_to`); no flat σ added. |
| **G1** | code-architecture audit | `valoria-module-adjudicator` (Key IN→resolver→OUT closure) + `valoria-mechanic-audit` (no inert mechanics, formula consistency) + an import-direction check | wrapper resolves nothing; core authors no law; no module imports up the DAG; no dead scaffold. |
| **G2** | evidentiary-primitive audit | `valoria-vector-audit` + the provenance CI pass | every touched literal is `derived` or a gated `calibrated`-debt row; **zero `ungrounded`**; no historical magnitude baked into a value. |
| **G3** | adversarial pass | independent red-team subagent (fresh context) | the red-team *cannot* find: an asserted value masquerading as derived, a top-down imposition, a band-fit smuggled in, an upward coupling letting the core reach up, or a behavior that only passes because a band was loosened. Findings are blockers. |
| **G4** | top-down historical validation | `gauge_mb.py` + the 11 bands (× 3 granularities from Stage 3 on) | emergent behavior holds every in-scope band; **bands never lowered** — divergence is flagged, not fitted. |
| **G5** | byte-exact toggle-off | gauge digest diff | the new path defaults OFF / instruction-less reproduces the prior engine digit-for-digit. |
| **G6** | editorial co-file + ED | `tools/ci_co_file_checker.py`, `tools/valoria_local.py --staged` | `canonical_sources.yaml` co-file satisfied; ED entry filed; naming/CI green. |

**G3 adversarial pass — standing charge sheet** (what every red-team subagent must try to break):
(a) point to one value that is called `derived` but is really a free number; (b) find a module that
imports something above it in the DAG; (c) find a place the core asks "what formation/troop is this?";
(d) find a band that was widened/removed to make a stage pass; (e) find a flat per-shape bonus
re-introduced under a new name. Any single hit blocks the stage.

## 2. Stages

### Stage 0 — Provenance inventory + consolidation baseline (FIRST; additive, low-risk)
- Build `provenance.py` to **100% literal coverage** via `tools/extract_values.py`; every uncatalogued
  literal becomes an `ungrounded` row → the retirement worklist with a **starting count**.
- Produce the archival worklist (`00_inventory.md` §13): the `sim_mb_06_v*` lineage, `v17-integration/`,
  dead stubs.
- Gates: G2 self-test (warnings day-1), G3 "is the inventory complete / any literal missed?", G5
  byte-exact (additive only).
- *Rationale:* you cannot remediate what you have not inventoried; cheapest, riskless; sets the metric.

### Stage 1 — Wrapper/core split (refactor, behavior-frozen)
- Extract `core/{exchange,attrition,state,contact}` and `hierarchy/units.py`; rewrite `engine.py` as the
  true wrapper (`build_side` adapter + `resolve_battle` router + I/O); `orchestration.py` keeps only the
  phase loop. Migration map in `01_architecture_audit.md` §4.
- **G1 is the spotlight** (the separation is the whole point); **G5 = `PER_CELL=0` byte-exact +
  `PER_CELL=1` numerically identical** on all 11 bands; `mechanics_selftest` green.
- No new values, so G2/G4 are regression-only.

### Stage 2 — Wire the behavioral modules (incremental; each sub-stage runs the full gate)
- **2a `troop_types/`** — wire `ROLE_SPEC`/`TROOP_TYPE_ROLES` into a real type→role gate; move
  `DAMAGE_BY_DEGREE` (F3) onto the troop-atom as a lethality primitive.
- **2b `cells/`** — retire the shape switches: `cell_speed`→`kinematics.momentum` (F1), `*_cells`→the
  `footprint_for` solver (F2), `SUPPORT_WEIGHTS`→`_support_along_vector` (F4). **This is where the two
  `ungrounded` rows go to `derived`.**
- **2c `formations/`** — a `Formation` object (template | custom allocation → cells), `MIN_DISCIPLINE`
  derived (F5). Reuses `pc_formation_system.md` §7 + `mb_engine_workplan.md` P-C inc. 1.
- **2d `doctrine/` + `tactics/`** — Aggression/Cohesion doctrine + the 4 GAP tactics (feigned-retreat,
  ambush, hammer&anvil, skirmish), each a Command-run ploy resolved vs opponent Command/Discipline (no
  flat modifier). P-C inc. 2–5.
- Each sub-stage: **G3 specifically hunts re-introduced flat bonuses / asserted magnitudes**; G4 must
  hold the relevant bands (H2/H3/H4/H5/H8 for the geometry derivations); G5 byte-exact for
  instruction-less scenarios.

### Stage 3 — Scale deployment (the granularity dial)
- Replace scattered `PER_CELL`/etc. reads with one wrapper-level `GRANULARITY ∈ {unit, subunit, cell}`
  (`04_validation_and_scale.md`). Make the latent subunit layer first-class.
- G4 adds the **cross-granularity-consistency** assertion + the sectional-rout and Lanchester-signature
  rows; G5: `unit ≡ PER_CELL=0`, single-subunit ≡ unit.

### Stage 4 — Multiunit field unification (Path B)
- Generalize `find_contacts`/`resolve_cross_side_contention`/`_front_fixers` from pairwise to all-units
  on one grid so envelopment **emerges** (`multiunit_envelopment_plan.md`; Phase 0 already confirmed).
- Preserve the envelop-shock double-count guard (`PC_ENVELOP_SIGMA=0`, config L93). G3 adversarial: does
  cross-unit envelopment *emerge* or was it scripted? G4: Cannae re-validated at army scale.

### Stage 5 — Debt-retirement sweep (the "never an assertion" endgame)
- Drive the `calibrated`+`ungrounded` count to **zero**: every residual `PC_*`/coefficient (F6/F7/F8/F9)
  either `derived` (charge-mass/closing-velocity primitives; the ~9 shock dials collapsed to one scale)
  or **removed**. Promote provenance CI from warnings to **blocking errors**.
- Complete consolidation: retire ED-1032 orphans, dormant `_envelopment_sigma`, dead stubs; archive the
  legacy sim lineage.
- **G3 = a full adversarial re-audit of the whole engine for any surviving assertion;** G4 re-validates
  all bands at all granularities. **This stage is the acceptance of §0.4.**

### Stage 6 — Canon reconciliation (editorial)
- Strip the flat A.6 dice rules from `mass_battle_v30.md` (Shield-wall +2D Def, Wedge +2D Off, … — the
  engine already ignores them); reconcile A.5 Command weighting to the engine's Charisma-primary form
  (ED-899); reframe general-death → capture (`mb_engine_workplan.md` P-B). G6 is the focus.

## 3. Critical path & dependencies

```
Stage 0 ─► Stage 1 ─► Stage 2 (2a→2b→2c→2d) ─► Stage 3 ─► Stage 4
                                   └────────────► Stage 5 ─► Stage 6
```
Stages 0→1 gate everything. Stage 2 is the largest but each sub-stage is independently gated and
byte-exact-for-instruction-less, so it lands safely. Stages 3–4 share the unification machinery. Stage 5
is the acceptance stage (debt = 0, provenance CI blocking). Stage 6 is deferrable editorial cleanup.

## 4. Build on, don't rebuild
Package split (P-A partial), Lanchester (config L119–128; F8 law), Command-only base (ED-899),
per-subunit stamina/rout/taxonomy (ED-1017/1018/1019), kiting primitive (`pc_formation_system.md` §13),
the `footprint_for` solver and `_support_along_vector` (the F2/F4 derivation targets already exist).

## 5. Effort & risk (indicative)
| Stage | Size | Conceptual risk | Note |
|---|---|---|---|
| 0 | S | very low | additive; sets the metric |
| 1 | L | low | big surface, pure refactor; G5 catches any drift |
| 2 | XL (4 sub-stages) | medium | the behavioral layer; each slice gated |
| 3 | M | low | dial + gauge axis; substrate exists |
| 4 | M–L | medium | contact generalization + perf (spatial bucketing) |
| 5 | M | medium | the derivations (shock scale) are the real design work |
| 6 | S | low | editorial; engine already conformant |

No stage ships without all six gates green. The adversarial pass (G3) is non-negotiable on every stage —
it is the structural answer to the self-authorship bias.
