# Mass Battle Sim — M3 §3c-σ: Canonical Sigma Apparatus + Derived Stats Applied

**Date:** 2026-05-29
**Skill:** valoria-simulator (NERS framing: valoria-resolution-diagnostic)
**Scope:** simulation
**Session token:** df5079812d207c7e
**Builds on:** `09_counter_geom_validated.md`. Jordan: "ratify 1, investigate 2, **ensure you are using the sigma stuff and derived stats**."
**Status:** MILESTONE + **CORRECTION + ARCHITECTURAL FINDING.** Applying the canonical sigma apparatus (σ-leverage engine + Wilson CIs) and derived stats (Army Morale §10.2) revealed that (a) **even the prior `09` count was over-stated** — proper Wilson CIs put the damage-mult engine at **6/11, not 9–10/11**; and (b) **the canonical σ-leverage substrate does not compose cleanly with the cell-geometry** (2/11 at canonical δσ). This surfaces an architectural decision for Jordan: mass-battle counters likely need the σ-leverage engine as the resolution *core* (Class-A migration), not σ bolted onto the attrition engine.

`[SELF-AUTHORED — bias risk]` I am correcting my own `09` result downward here. The correction comes from applying the statistical rigor (Wilson CIs, n=300+ pooled) that Jordan's instruction mandated and that I had not been using — every prior count was a bare Monte-Carlo point estimate judged by eye. Challenge surface §7.

---

## VERDICT

Jordan instructed me to use the sigma apparatus and derived stats. Doing so found three things:

1. **My evaluation method was wrong, and it inflated every prior count.** I reported raw win-rate frequencies (wins/n) judged against bands by eye. The canonical method is the **Wilson 95% CI** (`WILSON_Z=1.96`, used throughout `tests/sim/v32-combat-balance/`). Under it, **mean CI width at n=300 is ~11pp** — wider than several of the 10–15pp bands. **`09`'s "~9–10/11 pooled" for the damage-mult engine is over-stated; the honest CI-aware count is 6/11.** `[CORRECTION]`

2. **The canonical σ-leverage engine is the right resolution substrate** (uniform impact: a given δσ shifts win-probability identically at 2D and 18D — verified Δ=+0.000 across pools — dissolving the small-pool variance that made my single-seed tuning fragile). **But bolting it onto the attrition engine does not compose:** at canonical δσ ratios the σ-leverage counter gives **2/11**, because the δσ shift at the *contested* Ob interacts with the per-side pool asymmetry the cell-geometry produces. The clean per-matchup advantage the damage-multiplier gave does not transfer.

3. **Derived stats (§10.2 Army Morale) are now wired in** (`army_morale(unit) = floor(avg Morale) + Command_mod + Discipline_mod`, verified against the §10.2 thresholds), and the σ-counter is **casualty-neutral by construction** (~36% loser across all δσ — even cleaner than the damage-mult, since it shifts who-wins-the-roll, not damage).

**The architectural implication (for Jordan):** the combat-armature handoff (`sigma_leverage_handoff.md`) explicitly says combat should *be* the σ-leverage engine driven by strategic setup — "never reconstruct the attrition model." This mass-battle work has been tuning formation counters *on the attrition engine*. The non-composition (finding 2) is the predicted consequence. **The clean path is to make σ-leverage the mass-battle resolution core (Class-A), not patch σ onto attrition.** That is a Jordan architectural decision, surfaced not taken.

---

## §1 — What "the sigma stuff and derived stats" is (read, grounded)

`[READ: sim/autoload/dice_engine.py — _CONTINUOUS_PARAMS (TN7 μ=0.40 σ=0.800), roll_pool, roll_net_continuous (net~Normal(μN, σ√N)), degree_from_net]`
`[READ: tests/sim/v32-combat-balance/m1_dice_sigma_core.py — sigma_n=0.8√pool, soft_cap=M·tanh(net/M) M=1.5, eff_ob=base−softcap·σ_N, p_success=Φ(z), levels_to_net_sigma; the √N-cancels uniform-impact property]`
`[READ: tests/sim/v32-combat-balance/m8_integration_sweep.py + r8_parity_harness.py — wilson_ci(wins,n,z=1.96) score interval; the canonical significance method]`
`[READ: designs/scene/derived_stats_v30.md §7 TroopCount (Size=floor(TroopCount/block_size), Company block=100, output scaling), §10.2 Army Morale composite, §10.4]`
`[READ: designs/audit/2026-05-29-combat-armature/sigma_leverage_handoff.md — the σ-leverage engine §1, level→δσ table (Minor .25/Moderate .5/Strong .75; v31 ±1 Ob≈Moderate, ±2≈Strong), "combat IS σ-leverage, never reconstruct attrition"]`

Three canonical pieces, all previously unused in this mass-battle work:
- **σ-leverage engine:** modifiers are δσ; `Ob shift = δσ·σ_N`; √N cancels in the z-score → **uniform probability impact at every pool size** (≈25.8pp per Moderate at the 50% baseline). This is the NERS-Lesson-2 fix for the small-pool problem the resolution-diagnostic skill names.
- **Wilson CI:** the significance test for a Monte-Carlo win-rate. Band membership is only meaningful relative to the CI.
- **Derived stats:** Army Morale (§10.2), TroopCount (§7) — composites the engine should compute, not hardcode.

---

## §2 — Correction: Wilson CIs revise the `09` count downward

Re-evaluating the `09` damage-mult engine (v30) with the canonical method — pooled across 3 seed banks, n=300, Wilson 95% CI:

| Engine | `09` reported | **CI-aware (n=300 pooled)** | mean CI width | casualties |
|---|---|---|---|---|
| v30 damage-mult | "~9–10/11 pooled" | **6/11** | 11.1pp | 36% loser |
| v32 σ-leverage (canonical δσ) | — | **2/11** | 10.8pp | 35% loser |

**The 9–10/11 was point-estimate optimism.** At ~11pp CI width, an individual matchup whose point estimate sits in a 15pp band frequently has a CI straddling the boundary — it cannot be *confirmed* in-band. `09` counted point-in-band without the CI; `09`'s own §3 "over-fit 11/11 walked back to 9–10" was a step in the right direction but still short of the CI discipline. **Honest figure for the ratified damage-mult mechanism: 6/11 CI-confirmed.** `[CORRECTION: §3c-σ — v30 damage-mult is 6/11 CI-aware, not the 9–10/11 reported in 09; the gap was bare-frequency point estimates vs Wilson CIs]`

This also retroactively validates the `07` instinct that small-pool variance is the engine's core stress — the CIs *are* that variance, made visible.

---

## §3 — The σ-leverage non-composition (the real finding)

The σ-leverage counter (v32: δσ injected at the contested engagement Ob via canonical `eff_ob`) at canonical level ratios:

| # | Matchup | Band | p% [95% CI] | verdict |
|---|---|---|---|---|
| H1 | mirror | 45–55 | 50.0 [45.4, 54.6] | IN |
| H2 | wedge>line | 50–65 | 73.4 [69.3, 77.4] | OUT (over) |
| H3 | env>line | 50–65 | 45.6 [41.0, 50.2] | OUT (under) |
| H4 | env>wed (Cannae) | 40–60 | 61.7 [57.2, 66.1] | OUT (over) |
| H5 | refuse>env | 50–65 | 66.3 [62.0, 70.7] | OUT (over) |
| H6 | oblique>line | 45–60 | 63.2 [58.8, 67.7] | OUT (over) |
| H7 | manip>line | 50–65 | 41.0 [36.4, 45.5] | OUT (under) |
| H8 | manip>wed | 45–60 | 70.9 [66.8, 75.1] | OUT (over) |
| H9 | line<wed | 35–50 | 32.8 [28.5, 37.1] | OUT (under) |
| H10 | line<env | 35–50 | 46.0 [41.4, 50.6] | IN |
| H11 | wed<env | 40–60 | 35.2 [30.8, 39.6] | OUT (under) |

**2/11, misses in both directions** — at n=450 the CIs are tight (±4–5pp), so these are real, not seed swings.

**Why it doesn't compose:** the damage-multiplier (v30) scaled *damage dealt* by a matchup factor — a clean per-matchup offset that adds on top of whatever the geometry does. The σ-leverage counter shifts the *contested Ob* by `δσ·σ_N`, where `σ_N = 0.8·√pool` uses the *attacker's* pool. But the cell-geometry produces **different pool/contact sizes per side** (the H7 over-strength was exactly a contact-width asymmetry, `08`/`09`), so the same δσ produces a different Ob shift on each side, and it interacts non-linearly with the geometry's existing asymmetry. The system is **not separable** into "geometry baseline + counter offset" under the σ-substrate. H3 and H7 — over-strong under damage-mult — went *under* here, the geometry asymmetry now cutting the other way through the Ob.

This is not a tuning miss to grind out. It is the structural signal the combat-armature handoff predicted: **σ-leverage is a resolution-core architecture, not a modifier you bolt onto an attrition engine.** Attrition (damage accumulation → rout) and σ-leverage (Ob-space probability shaping) are different substrates; composing them re-introduces the pool-coupling σ-leverage exists to remove.

---

## §4 — What IS validated under the canonical method

- **σ-leverage uniform impact** (the small-pool fix): δσ=Moderate shifts win-probability by Δ=+0.000 difference across pools 2D/6D/12D/18D — verified. Bare-dice Δ shrinks with √N; σ-leverage does not. This is the correct mechanism for the small-pool variance that the CIs expose.
- **Casualty-neutrality**, σ-counter: ~36% loser / ≈26% per-side across all δσ and SIGMA_K (the σ-counter shifts who-wins-the-roll, not damage — neutral by construction). Holds in the damage-mult engine too.
- **SIGMA_K=0 neutrality:** with counters off, v32 ≈ v22_DB baseline (6/11, 36%) — the σ-wiring is correctly inert when disabled.
- **Derived Army Morale (§10.2):** `army_morale(unit)` computes the canonical composite correctly (verified: Resolute-8 and Wavering-1 test units match the §10.2 thresholds). Wired into v31/v32.
- **Wilson CI harness:** ported verbatim from `m8`; all counts now CI-aware.

---

## §5 — Historical validation (unchanged; the counters are real)

`precedents_warfare.md` §1.2/§6: formation counters + generalship-dominates are historically correct; Cannae the envelopment anchor. None of the above changes that. What changes is the *engineering*: the counters are real and the σ-leverage engine is the right substrate to express them with uniform impact — but on the *attrition* engine they don't compose, and bare-frequency evaluation over-stated how well even the damage-mult version reproduced the bands. The historical targets stand; the resolution architecture is the open question.

---

## §6 — The decision for Jordan (architectural — owner contract)

The honest state after using the canonical apparatus:

1. **Accept the damage-mult engine at its true 6/11 CI-aware** (v30, `09`), with the §A.6 values you ratified, and treat ~6/11 as the realistic-casualty mass-battle counter fidelity on the attrition substrate. Lightest; but `06`/`09` were over-stated and the σ-leverage engine is the canonical direction.
2. **Migrate mass-battle resolution to the σ-leverage core (Class-A).** Make the engagement a σ-leverage resolution (formation/stance/terrain as δσ, uniform impact, Ob-space), not attrition-with-σ-patches. This is what the combat-armature handoff mandates for personal combat and is the principled fix for the non-composition (§3) and the small-pool variance (§2). Heaviest — a new resolution architecture, full omega-framework vetting (PP-674) — but the only one that uses the sigma apparatus *as designed* rather than bolted on. **Recommended direction**, gated on your authorization (Class-A new system).
3. **Hybrid:** keep attrition for *casualties* (it's casualty-realistic) but resolve *who routs* via a σ-leverage contest seeded by Army Morale (§10.2) + formation δσ. Medium; needs design to avoid the §3 pool-coupling.

All three are yours. I will not pick the resolution architecture.

`[GAP: investigate-2 (RefusedFlank/side-bias) — NOT yet done this turn; the sigma/derived-stats instruction took priority and consumed the budget. The mirror-asymmetry investigation from `09` §5 remains open. It interacts with §3 here: if mass-battle migrates to σ-leverage, the attrition-side A/B orientation bug may be mooted; if it stays attrition, it must be fixed. Flag for next turn.]`

---

## §7 — Independent-reviewer challenge surface `[SELF-AUTHORED — bias risk]`

1. **"You reported 9–10/11 last turn and 6/11 now — which is it?"** 6/11 is correct; 9–10 was bare point estimates without CIs. The instruction to use the sigma apparatus is what surfaced the error. Reporting the correction is the discipline; the earlier number was optimistic, not the engine improving or degrading.
2. **"σ-leverage scored 2/11 — did you just implement it wrong?"** The implementation is the canonical `eff_ob`/`σ_N`/`tanh` ported verbatim and verified (uniform-impact Δ=0.000; SIGMA_K=0 neutral). The 2/11 is real: the non-composition with cell-geometry (§3) is structural, not a code bug. A reviewer should check whether a σ-leverage *core* (not bolt-on) composes — which is exactly the Class-A question for Jordan.
3. **"You didn't finish investigate-2."** Correct and flagged (§6 GAP). The sigma/derived instruction was the higher-priority of the three and the analysis was deep; I chose to do it properly rather than both shallowly. investigate-2 is queued with context.
4. **"Is 6/11 even a real improvement over the 5/11 lineage?"** Marginally, CI-aware — and the casualty-neutrality (the `07` blocker) IS a real, robust win regardless of band count. But the honest read is that on the attrition substrate, formation-counter fidelity tops out near the baseline; the σ-leverage core (option 2) is where a real gain likely lives. `[CONFIDENCE: high — Wilson-CI counts and the non-composition; medium — that a σ-leverage core would compose (untested; it's the next experiment if Jordan authorizes Class-A)]`

---

## §8 — Next steps

- **Jordan decision (§6):** which resolution architecture (accept 6/11 attrition / migrate to σ-leverage core / hybrid). Blocking.
- **investigate-2 (carried):** RefusedFlank/side-bias mirror asymmetry (`09` §5) — do next turn; may be mooted by a σ-leverage migration.
- **If σ-leverage core authorized (Class-A):** build the engagement as a σ-leverage resolution (Army Morale §10.2 + formation δσ + terrain δσ → eff_ob → degree), omega-vet (PP-674), validate ≥10/11 *CI-aware* at realistic casualties. This is the real fix.
- **All counts henceforth CI-aware** (Wilson 95%, n≥300 pooled across ≥3 seed banks). Bare frequencies retired.
- **Commit (B6 resolved):** this doc → `designs/audit/2026-05-29-massbattle-sim-foundation/10_sigma_derived_application.md`; engines `sim_mb_06_v31_sigma.py`/`v32_sigma_geom.py` → `tests/sim/` as σ-leverage prototypes; on Jordan's OK. Nothing to `mass_battle_v30.md` (the §A.6 values from `09` await the architecture decision — they may be re-expressed as δσ if option 2/3).

---

### Audit trail
- `[READ: dice_engine.py; m1_dice_sigma_core.py; m8_integration_sweep.py + r8_parity_harness.py (Wilson); derived_stats_v30 §7/§10.2/§10.4; sigma_leverage_handoff.md]`
- `[FIXED: evaluation method — all counts now Wilson 95% CI, n≥300 pooled ≥3 banks; bare frequencies retired]`
- `[FIXED: derived Army Morale §10.2 composite wired into v31/v32, verified vs thresholds]`
- `[CORRECTION: §3c-σ — v30 damage-mult is 6/11 CI-aware, NOT the 9–10/11 reported in 09; bare-frequency point estimates over-stated it]`
- `[FINDING: σ-leverage does not compose with cell-geometry on the attrition engine (2/11 at canonical δσ) — structural, predicted by the combat-armature "never reconstruct attrition" throughline; implies σ-leverage-as-core, not bolt-on]`
- `[ASSUMPTION: σ-leverage core would compose better than bolt-on — basis: uniform-impact property + the armature handoff; UNTESTED, the next experiment if Class-A authorized]`
- `[GAP: investigate-2 RefusedFlank/side-bias — carried, not done this turn (sigma instruction prioritized); may be mooted by σ-migration]`
- `[GAP: ED-875 low-Command sigma-leverage — now directly relevant; the σ-leverage engine IS the ED-875 substrate; reconcile if Class-A authorized]`
- `[CONFIDENCE: high — Wilson counts, uniform-impact, casualty-neutrality, non-composition; medium — σ-core composes (untested)]`
- `[DRIFT: B6 resolved on main; github_ops.py re-fetched]`
- `[PASS-3: verdict stands — sigma apparatus applied; corrects v30 to 6/11 CI-aware; σ-leverage doesn't compose on attrition (2/11), surfacing the σ-core architecture decision for Jordan; derived Army Morale wired; investigate-2 carried]`
