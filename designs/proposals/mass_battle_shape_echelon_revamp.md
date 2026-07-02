# Mass-Battle Shape-Echelon Revamp — Scoping Plan

**Status:** PARTIALLY EXECUTED (updated 2026-07-02) · **Date:** 2026-06-09 · **Scope:** mass-battle engine (`tests/sim/mass_battle/`) + canon (ED-816, ED-909)

> **2026-07-02 update:** this scoping doc's "Headline: this is a build, not a deletion" section below —
> Horseshoe/RefusedFlank moving from `Subunit.shape` to `Unit`-level emergent presets — is now BUILT
> (`engine.build_envelopment`/`build_refused_flank`, Stage D 2026-07-01; the literal `Subunit.shape`
> retirement itself, LC-8, executed 2026-07-02 per ED-1088). The role/doctrine layer (`Unit.doctrine`,
> the allocation grid, `role` gating) landed too (ED-907 L1/L3), per `HANDOFF.md`'s mass-battle entry.
> **Not built:** the full player-facing allocation-grid UI and Cohesion-priority toggle (ED-907's own
> ratification note explicitly defers these to Stage E videogame-UI, "not gaps"). Treat this doc as a
> scoping reference for what was decided, not as an open task.

Implements **ED-909** (formation-taxonomy reconciliation; supersedes ED-816 in part), building on **ED-907** (FM three-level command architecture) and **ED-908** (echelon mapping: Unit = battalion = army / Subunit = company / cell = squad).

## Scoping decisions (Jordan, 2026-06-09)

1. **Unit-layer scope = FULL ED-907** — the allocation grid + doctrine + Aggression/Cohesion team-instruction layer, not the minimal two-preset version.
2. **§A.6 ↔ geometric mapping = ED-909 orthogonal** — geometry × posture as independent axes; this **supersedes ED-816's replacement framing** (Wedge→Arrowhead, Shield Wall→Line+heavy-front, Skirmish→spread-Line), which is amended in ED-816 at Stage 4.
3. **Setup UX = split flow** — per-Subunit geometry + posture, then Unit-level deployment preset + doctrine; intended per ED-820 (proposed — "select shape at setup").

## Headline: this is a build, not a deletion

Horseshoe and RefusedFlank move from `Subunit.shape` — where ED-816 validated them as sub-unit shapes — to `Unit`-level emergent deployment presets (Envelopment, Refused Flank), produced by positioning Subunits and assigning flanking roles so the wrap/refusal *emerges*. They cannot simply leave the shape set: the `Unit`-level layer they land in does not yet exist.

## Current state (grounded)

- `class Unit` (orchestration.py L999) is a bare container of Subunits — no allocation grid, no deployment presets, no doctrine / Aggression / Cohesion. ED-907 is filed but unbuilt.
- Horseshoe / RefusedFlank referenced as shapes in: `config.py` L62 (Disc/Cmd table); `geometry.py` L75–77, L112–129 (`_SHAPE_BUILD` + `horseshoe_cells` / `refused_flank_cells`), L337–347 (`cell_speed`); `orchestration.py` L881–899 (shape-keyed dice-modifier branches), comments L101–137 / L755 / L1539; `validators.py` V-CANNAE L215.
- ED-816 validated values — **STAYS:** Line (Disc 1, Cmd 1, baseline), Arrowhead (Disc 4, Cmd 2, center +2D Off / flanks −1D Off; counters GappedLine), GappedLine (Disc 5, Cmd 3, gap channel / kill-zone). **DEMOTE:** Horseshoe (Disc 5, Cmd 3, center −2D Off / +1D Def, flanks +2D Off; 54% winrate; Cannae), RefusedFlank (Disc 3, Cmd 2, refused −2D Off / engaged +1D Off; Leuctra).
- ED-816 cited a phantom **"Composition"** entry (the bare number was never filed); corrected to **ED-907** (the real FM command-architecture entry).

## Build

### A. Unit-level layer — FULL ED-907 (decision 1)

On `class Unit`:
- **Allocation grid** — an adjustable allocation surface: player sets intent (e.g. "60% melee, hold defensive") → auto-distribute across the deployment, with manual override.
- **Deployment presets** — Envelopment, Refused Flank, and a Line-of-battle default: position Subunits (`starting_position`, `advance_dir`) and assign flanking roles; the wrap/refusal emerges via the existing `envelop` / `sweep` maneuvers and the flanking-detection already in resolution.
- **Doctrine + team-instruction layer** — Aggression {Cautious, Balanced, Pressing}, Cohesion-priority {Hold shape, Adapt}; conditions subordinate behaviour under stress.
- **Intervention windows** — ~5–20 per battle (set intent, watch, intervene at punctuated decision points; not per-tick control).

### B. Demote the two shapes — orthogonal geometry × posture (decision 2)

- Remove Horseshoe / RefusedFlank from the Subunit shape set (`config.py`, `geometry.py`, `orchestration.py`, stress harness `SHAPES`).
- **Subunit shape = GEOMETRY axis:** Line, Arrowhead, GappedLine.
- **§A.6 dice-modifier formations = POSTURE axis, orthogonal to geometry:** a Subunit picks a geometry *and* a posture independently — e.g. Shield Wall = a Line/heavy-front geometry in a defensive posture; Wedge = Arrowhead geometry in an offensive posture; Skirmish = a spread/GappedLine geometry in a harass posture. This supersedes ED-816's replacement mapping.
- **Re-express the demoted shapes' effects as emergent:** Horseshoe's flank +2D becomes the existing flanking-detection bonus when wings actually reach a flank; RefusedFlank's oblique becomes the deployment preset.

### C. Setup UX — split flow (decision 3, per ED-820 — proposed)

Two-stage selection: (1) per-Subunit geometry + posture; (2) Unit-level deployment preset (Envelopment / Refused Flank / Line-of-battle) + doctrine.

## Canon amendments (Stage 4)

- **ED-816** — mark Horseshoe / RefusedFlank demoted to `Unit`-level (per ED-909); preserve Line / Arrowhead / GappedLine validations; flag the static modifiers superseded by emergent flanking (re-validation required); replace the replacement-mapping with the orthogonal geometry × posture model (decision 2); fix the stale composition reference → ED-907.
- **ED-909** — update the §A.6↔geometric residual from "open / orthogonal-hypothesis" to "decided: orthogonal" (decision 2).

## Re-validation (mandatory)

Removing validated shape-static modifiers shifts calibration (orchestration notes RefusedFlank-vs-Horseshoe at 47.4%, target 50–65%). After the change: re-run a SIM-MB-05-style Monte Carlo batch + V-CANNAE / V-ENVELOP to confirm the emergent envelopment reproduces comparable outcomes, and set new calibration bands.

## Staging (each its own verified commit)

1. Build the `Unit`-level ED-907 layer (allocation grid + Envelopment / Refused-Flank presets + doctrine) — non-breaking; shapes still present.
2. Re-express the two shapes' effects as emergent; verify outcomes hold with shapes still present.
3. Remove Horseshoe / RefusedFlank from the Subunit shape set (config / geometry / orchestration / harness).
4. Amend ED-816 + update ED-909.
5. Re-validate (validators + stress + calibration MC); set new bands.

## Risks / watch

- **Calibration drift** — static-shape values won't transfer 1:1 to emergent flanking; re-tuning likely.
- **Build size** — the full ED-907 layer (allocation grid + doctrine + intervention windows) is substantially larger than the shape demotion itself; it is the bulk of the effort.
- **Cross-system fidelity** — the emergent envelopment must still reproduce V-CANNAE (Subunits positioned + flanking), not a Horseshoe shape.

---

*Provenance: engine grep `tests/sim/mass_battle/{config,geometry,orchestration,validators}.py` (2026-06-09); ED-816 full entry; ED-907 / ED-908 / ED-909 (filed 2026-06-09); historical anchors Cannae 216 BC, Leuctra 371 BC, Leuthen 1757.*
