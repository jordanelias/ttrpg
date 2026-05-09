# Module Manifest — NERS Stress Test (Randomized Starting Conditions)
## Sim name: ners_stress_01
## Date: 2026-05-08
## Base harness: tests/sim/valoria_full_campaign_sim.py (Sessions 1–3, 153-entry ledger)
## Mode: G (Incremental Build Protocol)

---

## Scope

Stress-test the existing Tier A harness under randomized starting conditions.
Evaluate results against NERS criteria (Necessary, Robust, Smooth, Elegant)
from all directions (top-down faction strategy, bottom-up action economy,
lateral inter-faction, diagonal cross-system, vertical scale, horizontal
within-scale).

**This is NOT a new full-stack sim.** The existing harness mechanics are not
re-implemented. Only new code: (1) randomization wrapper, (2) NERS scoring
layer, (3) batch runner.

Existing harness mechanical constants are already verified (153 ledger entries).
New ledger entries required only for randomization bounds.

---

## Modules

| # | Name | Depends On | Canonical Sources (new fetches only) | Status |
|---|------|-----------|--------------------------------------|--------|
| 1 | Randomization Layer | existing harness | `params/factions/stats_1_7_scale.md` (stat ceilings/floors), `params/bg/core.md §Starting Values`, `designs/world/geography_v30.md §T1-T17 table` | pending |
| 2 | NERS Evaluation + Batch | Module 1 + existing harness | NERS definitions from PI canon_terms (in context); no new canonical docs | pending |

---

## Module 1 — Randomization Layer

**Session protocol:**
1. Fetch `params/factions/stats_1_7_scale.md` at full depth — stat ceilings,
   floors, and starting values for all 4 playable factions.
2. Fetch `params/bg/core.md §Starting Values` — canonical clock starting values
   and hard caps (RS 0-100, CI 0-100, IP 0-100, PI 0-20, Strain 0-30).
3. Fetch `designs/world/geography_v30.md §T1-T17 table` — canonical territory
   ownership and PV values for perturbation bounds.
4. Build verification ledger entries for all randomization bounds.
5. Call `h.sim_gate('custom', systems=['faction_layer', 'clock_system', 'territory_model'])`.
6. Implement `initial_campaign_randomized(seed, perturbation)`.
7. Smoke test: canonical starting state (perturbation=0) must match
   `initial_campaign_tier_a(seed=0)` exactly.
8. Commit.

**Randomization design (to implement):**

```python
def initial_campaign_randomized(
    seed: int,
    perturbation: str = 'mild',  # 'mild' | 'moderate' | 'extreme'
) -> Campaign:
    """
    Perturb canonical starting state. All bounds verified against ledger.

    Perturbation levels:
      mild:     stats ±1 (clamped 1–7), clocks ±10% of canonical, 0–1 territory swaps
      moderate: stats ±2 (clamped 1–7), clocks ±20% of canonical, 1–3 territory swaps
      extreme:  stats ±3 (clamped 1–7), clocks ±30% of canonical, 3–5 territory swaps

    Stat ceilings/floors: [canonical: params/factions/stats_1_7_scale.md §Stat Ceilings and Floors]
    Clock starting values: [canonical: params/bg/core.md §Starting Values (v04 B2, PP-188)]
    Territory ownership: [canonical: designs/world/geography_v30.md §T1-T17 table]
    """
```

**Verification gate:** smoke test must pass before commit.

---

## Module 2 — NERS Evaluation + Batch Runner

**Prerequisite:** Module 1 status = verified.

**Session protocol:**
1. Read module manifest from GitHub — confirm Module 1 verified.
2. NERS definitions already in context (PI canon_terms). No new canonical fetches.
3. Call `h.sim_gate('custom', systems=['faction_layer', 'clock_system', 'territory_model'])`.
4. Implement NERS scoring per run.
5. Implement batch runner (100 seeds × 3 perturbation levels = 300 total runs).
6. Run batch. Collect results.
7. Produce `tests/sim/ners_stress_01/ners_report.md` in Mode D format.
8. Update `sim_coverage_matrix.md`.
9. Commit.

**NERS evaluation design (to implement):**

Per run, evaluate from all directions:

| Direction | N | E | R | S |
|-----------|---|---|---|---|
| Top-down (faction strategy) | Do all factions have viable DA options each season? | Are inter-faction power gaps predictable from starting stats? | Can any starting configuration produce a non-Crown winner? | Does each DA action class produce proportionate outcomes? |
| Bottom-up (action economy) | Is there ever a season with zero valid DAs? | Does action choice matter, or does stat advantage dominate? | Can weak-start factions recover via action sequences? | Is action resolution consistent across stat levels? |
| Lateral (inter-faction) | Do all 4 factions interact each run, or do some become irrelevant? | Is power shift between factions legible from state deltas? | Do faction interactions produce varied outcomes, not scripted arcs? | Are faction interactions symmetric (Crown v Church ≠ Church v Crown)? |
| Diagonal (cross-system) | Do clocks interact with DA outcomes non-trivially? | Are clock-DA coupling effects predictable? | Do extreme clock values produce appropriate DA modifiers? | Is the clock-DA interface free of contradictions? |
| Vertical (scale) | Do BG-layer outcomes produce plausible personal-scale hooks? | Is the BG→TTRPG translation legible from state? | Does scale transition preserve causality? | Are BG outcomes proportionate to TTRPG-scale inputs? |
| Horizontal (within-scale) | Are all BG systems active each run, or do some go idle? | Do within-scale calculations share consistent methodology? | Do BG system interactions produce clean handoffs? | Are all BG calculations at comparable complexity levels? |

**Batch runner:**
- 100 seeds × 3 perturbation levels = 300 runs
- Max 60 seasons per run (matching Tier A)
- Collect per run: winner, seasons, final clock states, elimination events,
  DA distribution, NERS scores per direction
- Flag any run where NERS score drops below threshold in Mode D format

---

## Output Files (committed to tests/sim/ners_stress_01/)

| File | Produced in | Content |
|------|------------|---------|
| `module_manifest.md` | this session | this file |
| `module_01_randomization.py` | Module 1 session | randomization layer |
| `module_02_ners_batch.py` | Module 2 session | NERS scoring + batch runner |
| `ners_report.md` | Module 2 session | Mode D findings |
| `sim_verification_ledger_ners.json` | Module 1 session | ledger for new bounds |

---

## Open Questions (resolve at Module 1)

- Does `designs/world/geography_v30.md` use T1-T17 table or is territory
  data embedded differently? (Check index before fetch.)
- Perturbation percentages for clocks: ±10/20/30% of canonical or absolute
  delta? Resolve against `params/bg/core.md §Starting Values` to pick
  bounds that stay within mechanically meaningful range.
- Vertical scale direction: BG→TTRPG evaluation requires knowing what
  TTRPG-layer events BG outcomes are supposed to generate. Confirm against
  `designs/architecture/campaign_architecture_v30.md` at Module 2 if needed.

---

## Status Log

| Date | Module | Event |
|------|--------|-------|
| 2026-05-08 | — | Manifest produced, existing harness surveyed |
