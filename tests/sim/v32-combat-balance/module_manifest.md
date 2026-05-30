# v32-combat-balance — Module Manifest (Mode-G)

Sim name: `v32-combat-balance` → `tests/sim/v32-combat-balance/`.
Source decomposition: designs/audit/2026-05-28-combat-reframe/i17_simulation_prep.md (committed 0271da2).
Acceptance: archetype matchups 40–60% (skill §8.8 band), no inversion, no non-viable baseline build.

| # | Module | Depends | Canonical sources (full-read before coding) | Status |
|---|--------|---------|----------------------------------------------|--------|
| 1 | Dice + σ-space core | — | params/core.md; modifier_system_spec.md (§12.3 rewrite) | verified (b9b6d4e) |
| 2 | Attribute → pool builder | 1 | params/core.md §Attributes/§Derived Scores; derived_stats_v30.md §4–§5; combat_v32 §2.1/§11 | verified (6d7b0e9) |
| 3 | Weapon-class layer | 1,2 | combat_v32 §8; combat_v30 §5 | verified |
| 4a | Bout state graph + control flow | 1 | combat_v32 §4.6–§4.9, §12.5–§12.6 | verified |
| 4b | Sub-action mechanics (Pool/Ob/degree) | 1,3,4a | combat_v32 §12.1–§12.4 | verified |
| 5 | Stance + Reaction + coherence | 4 | combat_v32 §7.1–7.3 | verified |
| 6 | Dual-resource economy | 4 | combat_v32 §11.5–11.6, §4.9 | verified |
| 7 | Facing / FoV (optional; stub-first) | 4 | combat_v32 §11.2 | verified |
| 8 | Integration + archetype sweep | all | — (wires modules) | verified |

Hard rules: one module/session; every constant ledgered or `# [canonical:]`; re-verify imported module values; no batch run until all modules verified.
Class split: ~14 of 34 constants Class A (canonical); ~20 Class B (v32 draft sim-seeds, tuned here).

## Remediation iteration (post-I-17, Jordan-authorized 2026-05-29)

| Module | Scope | Source | Status |
|---|---|---|---|
| M9 (bottom-up wound model) | replace multiplicative damage (M8 finding) with bottom-up severity; historical validation | combat_v30 §5/§8 (anchors) + proposed Class-C redesign | verified |
| M8b (re-sweep under M9) | historical validation (PASS 5/5) + build-axis balance stratified by armour tier | M9 wound model + i17_simulation_prep harness | verified |

## Combat armature reset (2026-05-29 — σ-leverage build on the corrected model)

Supersedes the M8/M8b attrition integration. Reuses M1/M3/M5/M9; replaces the Agility-scaled Combat Pool (the M8b-identified bottleneck) with a demoted History-driven pool + Agility-as-σ-leverage. Design spec: designs/audit/2026-05-29-combat-armature/ (Build-0).

| Module | Scope | Canonical sources | Status |
|---|---|---|---|
| R1 (σ-leverage resolution atom) | demoted Agi-independent pool + state-gated δσ → Effective Ob → degree/crit; crit = Overwhelming strike | params/core §Degrees/§Obstacle/§Derived/§Attributes + modifier_system_spec §4 (Class A); wound_model_resweep_results (Class C anchor) | verified (self-test 6/6) |
