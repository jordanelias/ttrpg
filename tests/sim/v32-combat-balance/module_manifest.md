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
| R2 (consequence/wounds) | canonical strike damage (net + STR x mult + weapon-vs-armour) -> authoritative wound-gate tracker; crit = Overwhelming doubles weapon-mod; unified armour = canon table | combat_v30 §5/§6 + derived_stats §4.1 (Class A); M9 resist = historical oracle | verified (self-test 7/7) |
| R3 (parity sweep) | equal-budget Agi/Str/End matchups, Wilson CI, Ω-d no-dominant-strategy | params/core §Attributes (Class A) + simulator §8.8 band (Class M); wires R1+R2 | verified; FINDING: C-04 closed, End-dominance (63.4%) surfaced for Jordan calibration |
| R4 (full-channel equal-value sweep) | full Agi stack (init+tempo+facing[M7]+reaction[M5]) + Reading[Cog/Att] into decisive phrase; tuned toward equal value | params/core + R1/R2/M5/M7 + simulator §8.8 | verified; FINDING: C-04 closed, End tamed, Reading in-band 46%, Strength DEAD 23% (+0.00 σ-leverage) -> needs landing/control channel = Jordan decision |
| R5 (Strength leverage + Stamina recomposition) | Str landing/control channels (bind/stagger/armour-defeat/wield/stamina-efficiency) + Stamina=f(End,Spirit) | combat_v30 §5 + derived_stats §4.2 (Class A) + Jordan decisions 2026-05-29 (Class-C) | verified (self-test 6/6); Str leverage +0.00 -> +0.88 in-bind |
| R6 (equal-value re-sweep) | 6-attr sweep with R5 wired; decisive phrase | params/core + R1/R2/R5/M5/M7 + simulator §8.8 | IN-PROGRESS harness, NOT a verdict (field aggregate confounded by loadout-symmetry; single-loadout traces show Str channels work) |
| R8 (defect-immune parity harness) | rebuilt sweep; budgets asserted; JSON output; each build best-loadout then asymmetric | params/core + R1/R2/R5/M5/M7 + simulator §8.8 | TRUSTWORTHY VERDICT (supersedes R3/R4/R6/R7): Str 85% over-tuned, Agi/End/Reading cluster 58/43/49, Spirit 12% dead. Findings: Str magnitude calibration (Jordan); Spirit needs 2nd channel (design) |
| R9 (weapon engagement: phase reach+speed) | reach governs closing, speed governs bind (reach inverts); the spear fix | combat_v30 §5 reach + m3 speed (Class A); HEMA (top-down) | verified (self-test 5/5); spear niche restored; full 8-way convergence = joint-fit/design call |
| R10 (duel vs battlefield context) | engaged foe -> suppressed defence -> heavy armour-defeating weapons dominate (their niche); duel weapons win duels | combat_v30 §5 + R1/R2 (Class A); Jordan battlefield insight + HEMA (top-down) | verified (self-test 3/3); resolves weapon convergence by CONTEXT not canon nerf |
| weapon_axes_v2 (hands+head substrate) | reclassifies all weapons as axis-vectors + tonfa/flail; point-vs-armour row; head/hands sigma-modifiers | combat_v30 §5 + W1 ratified (Class A); weapon_axes_v2 proposal | verified (self-test 7/7); duel+battlefield audit matches historical precedent; bare-mace duel-top = the R10 blunt-battlefield artifact |
| armour_axes (material+coverage substrate) | (head x material) mitigation matrix reproducing the ratified weapon-vs-armour table + material/coverage axes + sigma-tempo/Stamina/Health costs | 3.4 Armour + combat_v30 §5 W1/W5 (Class A reproduced); armour_system_design proposal | verified (self-test 7/7); matrix reproduces ratified table exactly; weapon-head-vs-plate matches history; fatigue-erodes-duel claim FALSIFIED & corrected (plate 1v1 dominance historical; counters = blunt/gaps/grappling) |
| grappling (close-combat substrate) | grapple = innermost engagement state; Strength-dominant sigma-contest (ST1) + canonical Disarm/Tie Up/Escape/Retrieve + the NEW dagger-finish (point to gaps, bypasses armour mitigation) | 3.6 Actions (Class A reused); grappling_system_design proposal | verified (self-test 6/6); the third plate-counter -- grappler fells full-harness in 4.2 (vs blunt 3.0, cut deflected); context-gated (0%% vs spacer unarmoured, 98%% vs spacer in plate); fills ED-129 |
| damage_model (ground-up rebuild) | Damage = Impact(STR+heft, additive) x Coupling(head-vs-armour, from material resistance-per-mode) x Quality(degree); supersedes the multiplier formula + folds in the weapon-vs-armour mod | derived_stats §4.1 wound model + params/core degrees (Class A consumed); damage_model_design proposal | verified (self-test 8/8); Success~=1 WI anchor; matrix emerges; pacing sane; STR additive |
| combat_resolution (UNIFIED pipeline) | composes R1+m1+weapon_axes_v2+armour+damage_model+grappling through ONE path w/ ground-up damage; sigma-leverage gates degree->damage | all armature modules (composed) | verified (self-test 6/6); INTEGRATION surfaced + fixed the duel/damage mismatch (leverage now gates hit quality, not just frequency) |
