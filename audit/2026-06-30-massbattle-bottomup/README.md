# Mass-Battle System — Bottom-Up Audit & Re-Architecture (2026-06-30)

A six-part audit of the mass-battle system against a **bottom-up, evidentiary-primitives, emergent**
standard, plus a staged/gated/adversarial roadmap to bring it fully there. Audit pass is **read-only +
additive** — no engine behavior changed. Approved plan:
`/root/.claude/plans/using-opus-4-8-ultracode-floating-tiger.md`.

## The directive → artifact map

| # | Directive | Artifact |
|---|---|---|
| 1 | Survey the whole system incl. orphans/audits/sims/WIP | `00_inventory.md` |
| 2 | Audit code architecture (wrapper vs engine; modules) | `01_architecture_audit.md` |
| 3 | Find every pattern-match / imposition / weight / assertion | `02_antipattern_census.md` |
| 4 | Ensure granular/modular/bottom-up emergent from primitives | folded into 01 + 02 |
| 5 | Primitives grounded in academic/historical sources | `03_provenance_ledger.md` + `tests/sim/mass_battle/provenance.py` |
| 6 | Emergent results validated top-down; multi-scale (unit/subunit/cell) | `04_validation_and_scale.md` |
| — | The staged, gated, adversarial roadmap | `05_redesign_workplan.md` |

## Headline findings

- **Architecture:** `engine.py` (74 L) is an inert re-exporter; `orchestration.py` (**2,899 L**) is a
  god-file conflating data model + targeting + attrition-law authoring + volley + resolution + turn loop
  + I/O; troop-types/formations/tactics/strategy are inert data. Fix = full clean module split (wrapper
  resolves nothing · core resolves only · every module wired).
- **Anti-patterns:** 9 findings, 8 isolated to `geometry.py` + `config.py`. Dominant: shape-name lookup
  (`cell_speed`, four `*_cells` tables) — pure assertion; and ~20 calibrated-to-band `PC_*` magnitudes.
  The substrate (cells, Lanchester, du-Picq σ, per-subunit rout) is sound and stays.
- **Grounding:** laws are excellently cited (Lanchester, du Picq, cavalry bands); a cluster of *values*
  is asserted. The bar: **history validates behavior, never licenses a number.** Seed provenance count:
  **2 ungrounded + 13 calibrated-debt = 15 to retire → 0.**
- **Validation/scale:** the 11-band gauge is a real top-down validator (bands never lowered); gaps are
  unit-only scale (subunit layer latent) and scattered granularity toggles — fixed by one `GRANULARITY`
  dial + a cross-granularity gauge axis.

## What this pass changed

Documents only, plus the additive data-only `tests/sim/mass_battle/provenance.py` seed (byte-exact: no
engine behavior touched). The re-architecture itself (Stages 1–6) is gated for separate approval.
