# Stress-Test Audit — σ-Leverage Combat Engine (NERS Resolution Diagnostic)

**Date:** 2026-05-31 · **Skill:** `valoria-resolution-diagnostic` (Stage 1–4) · **Surface:** claude.ai + Code Interpreter
**Target:** the σ-leverage combat **resolution engine** — the core every other combat layer hangs on (not the full damage/lever calibration).
**Bootstrap token:** `88268ce73afbbf91` · all 115 canonical sources fresh.

`[SELF-AUTHORED — bias risk]` This engine was built by prior sessions in this same project. Treated as external work; the criticism an independent reviewer would raise is surfaced, not softened. Positives appear only where they narrow the fix.

---

## 0 · What "latest combat engine" resolves to (+ a record-drift flag)

| Thing | Path | Status |
|---|---|---|
| **Canonical `combat`** | `designs/scene/combat_v30.md` (per `canonical_sources.yaml`) | the **old d10 success-counting engine** — explicitly being abandoned |
| **Latest engine (the target)** | `designs/audit/2026-05-29-combat-armature/RATIFIED_*` + `tests/sim/v32-combat-balance/{m1,r1,...}.py` | the **σ-leverage armature**, ratified 2026-05-29 + four addenda 2026-05-30 |

`[DRIFT: handoff #5 "blocked on Jordan doc-2.5 decision" — STALE.]` Handoff #5 (timestamp 2026-05-29T23:06) calls the build blocked on the §2.5 resolution-structure decision. The **four RATIFIED addenda dated 2026-05-30 postdate that handoff** and settle the structure (decisive phrase, demoted pool, ground-up damage). The §2.5 question was resolved; the handoff was never updated.

`[READ: RATIFIED_2026-05-29.md, RATIFIED_addendum_2026-05-30{,_tempo_axes,_damage,_leverage_gating}.md, sigma_leverage_handoff.md — full; m1_dice_sigma_core.py, r1_sigma_resolution.py — full; sweep_results_v32.md, module_manifest.md, r3/r4/r8/r5_r6 result.md — coverage scan; canon/02_canon_constraints.md, canonical_sources.yaml — task-gate]`

---

## VERDICT (review-first)

**NON-COMPLIANT** — fails **R** (two inconsistent resolution definitions; a favorable-side dead-zone) and **S** (model fidelity frays <5D; the canonical record disagrees with the ratified design). The failures are **localized and fixable**, and the engine's core balance purpose is **achieved**: C-04 (pool-size dominance) is genuinely closed in the runtime engine, foreclosure is removed, and leverage gates quality smoothly. This is "settle the resolution form + bound the validity + propagate the record," not a redesign.

```
SYSTEM: σ-leverage combat resolution engine   COMPONENTS: dice (Strike) + deterministic (δσ stack, D1 damage) + selector (commit depth / intent tier)
N: PASS  — engine is load-bearing; one dead constant (POOL_FLOOR=5 unreachable in combat).        [F5]
R: FAIL  — m1 prescribes μ-shift, r1 resolves Ob-shift (diverge off-TN7 + low-Ob); Ob-floor dead-zone. [F1 P2, F2 P2]
S: FAIL  — uniform impact is a continuous-model property, validated >=5D only; record drift.        [F3 P3, F4 P3]
E: PASS* — σ-leverage idea is elegant; *the Ob-floor dead-zone dents "intuit outcomes" on easy strikes. [F2]
```

---

## 1 · STAGE 1 — Diagnostic (Phase 0–6)

### Phase 0 — Decompose
- **Dice-resolved:** the single-Action σ-leverage Strike (`r1.resolve_action`) — pool rolled, net banded against an Obstacle. A fight is **one short bounded exchange** (R2), not attrition.
- **Deterministic-accounting:** the δσ stack (Stance / Reading / Reaction / Facing / weapon-phase / coherence → `net_σ` → `tanh` soft-cap → `eff_σ` → Ob shift), and damage **Impact × Coupling × Quality** (D1).
- **Clock/selector:** Intent-Reading tier (0–5), Commit depth (1–5). Not stress drivers here.

### Phase 1 — Stress points
- **Pool floor (by design):** `resolution_pool = max(5, History+6)`, `BASE_POOL=6` (Class-C), `POOL_FLOOR=5` (Class-A) → effective combat pool **6D–13D**. The sub-5D danger zone is **structurally unreachable in combat**.
- **Engine substrate floor:** the σ-leverage engine is the *general* substrate (`modifier_system_spec §12.3`); its own pool floor is **1D**. Sub-5D exposure exists for *non-combat* reuse.
- **Saturation tail:** the `tanh` cap (`M_MAX=1.5`) **and** the canonical Ob floor (=1) — two separate caps that interact.

### Phase 2 — What the stress point decides
A Strike is **graded-magnitude** (degree → Quality factor → damage via L1), not a bare binary. Stakes recoverable-to-load-bearing. Small-pool risk **for combat**: Exposure **L** (floored out) → not a combat finding. **For substrate reuse**: (Impact M, Exposure M, Irreversibility L) → carried as a scoped engine boundary (F3).

### Phase 3 — Effect curves

**MECHANICAL LOG A — uniform-impact claim, discrete d10 vs continuous, pools 1D–18D.**
Claim (`sigma_leverage_handoff §1a`; `m1` self-test c): *a fixed δσ gives the same probability impact at every pool size.* Test δσ = 0.70 (= m1's own test value → continuous +25.8pp). Baseline = continuous 50% point. **Exact discrete convolution, no sampling.**

| Pool | cont Δpp | disc Δpp | divergence | note |
|---:|---:|---:|---:|---|
| 1D | 25.80 | **0.00** | −25.80 | sub-5D; Ob-floor + 4-value granularity kill the shift |
| 2D | 25.80 | **0.00** | −25.80 | sub-5D |
| 3D | 25.80 | 28.20 | +2.40 | sub-5D |
| 4D | 25.80 | 23.76 | −2.04 | sub-5D |
| 5D | 25.80 | 19.80 | −6.00 | continuous-approx validity edge |
| **6D** | 25.80 | 20.04 | −5.77 | **<< COMBAT POOL FLOOR** |
| 7D | 25.80 | 17.87 | −7.93 | |
| 8D | 25.80 | 33.25 | +7.45 | |
| 10D | 25.80 | 14.83 | −10.98 | |
| 12D | 25.80 | 25.92 | +0.12 | |
| 18D | 25.80 | 32.62 | +6.82 | |

- **CONTINUOUS Δpp spread 1–18D: 0.00pp** (flat 25.80 — uniform by construction; the √N cancels in the z-score).
- **DISCRETE Δpp spread 1–18D: 33.25pp** | sub-5D (1–4D): 28.20pp | combat band (6–18D): **18.43pp**.
- Exact 1D net PMF: `{-1:10%, 0:50%, +1:30%, +2:10%}` — only 4 realizable values; a 0.7σ Ob shift (≈0.56 Ob at 1D) crosses **no** integer boundary → **0pp** impact.

**Reading.** The shipping engine resolves on the **continuous** sampler (`roll_net_continuous`, params/core "Decision E"), where uniform impact holds at every pool. So **combat (≥6D) gets uniform impact and C-04 is genuinely closed** — *this is not a combat balance defect.* The 18–33pp discrete swing shows the property is a **property of the continuous approximation, not of the d10 dice**, and runtime/dice only agree ≥5D (m1 test b validated discrete≈continuous over 5D–17D). → carries as **F3** (engine reuse + model-fidelity boundary), not a combat finding.

- **3b cliffs:** the `tanh` soft-cap deliberately avoids a hard ceiling on `eff_σ` (no cliff). **But** the Ob floor (=1) reintroduces a downstream cap — see MECHANICAL LOG C / **F2**.
- **3c role conflation:** none material. The R1 demotion *removed* a conflation (Combat Pool no longer carries Agility-dominance + skill).

### Phase 4 — Loops
- **Within combat:** the decisive-phrase model (R2) removes the iterated attrition loop → **no within-combat death spiral** (C-05 fixed). The σ-leverage→degree→damage chain (L1) is one-directional, not feedback.
- **Cross-scale:** combat death → faction Stability → muster → combat exists, but its damper/cap lives in the faction/military layer; out of scope for a combat-engine audit. No new undamped+unbounded loop introduced by the armature.

### Phase 5 — Intent gate
Most structure is **Jordan-ratified** (RATIFIED docs, "ratify all"): pool demotion (closes C-04), decisive phrase (not attrition), `tanh`-not-clamp (avoid cliff), multiplicative damage D1 (Jordan-directed), plate ~95% dominance (intended/historical). Calibration constants (`M_MAX`, `SIGMA_N_COEFF` kept; Stance cells / Reaction coeffs / set bonuses / `AGI_TEMPO_PER_POINT` / `DMG_SCALE` / `LEVERAGE_TO_DEGREE=3.5` / armour σ-tempo) are flagged Class-C sim-seeds — acknowledged-unpinned, not defects. The findings below are **execution gaps in ratified intent**, not intent disputes.

### Phase 6 — MECHANICAL LOG B + C

**MECHANICAL LOG B — `tanh` soft-cap foreclosure floor (F2-design-goal).**
`eff_σ = 1.5·tanh(net_σ/1.5)`; μ-shift z-shift = `eff_σ`. Floor/ceiling from a 50% baseline.

| net_σ | eff_σ | P(disadvantaged), continuous | cap Δpp (50% base) |
|---:|---:|---:|---:|
| 1.0 | 0.874 | 19.1% | 30.9 |
| 1.5 | 1.142 | 12.7% | 37.3 |
| 2.0 | 1.305 | 9.6% | 40.4  (handoff "heavy stack ~9%") |
| →∞ | 1.500 | **6.7%** | 43.3  (absolute saturation) |

Discrete realization at the **combat floor (6D)**, base Ob 2.4: full adverse → **P(success) 5.9%**; neutral 47.0%; full favour → 83.5% (Ob floored). **F2 holds — the disadvantaged side never reaches 0%, continuous and discrete-at-combat-floor.** The `tanh`-vs-clamp choice is correct (smooth, no dead-zone *on eff_σ*, no cliff). **PASS.**

**MECHANICAL LOG C — degree/Quality distribution vs leverage (L1 + the Ob-floor dead-zone).**
Pool 8D; base strike Ob 2 *[illustrative — base-Ob is a per-action parameter]*. Canonical bands (params/core §Degrees): Overwhelming `net≥2·Ob AND net≥3`; Success `net≥Ob`; Partial `0<net<Ob`.

| net_σ | eff_Ob | Fail | Partial | Success | Overwhelming | E[Quality] |
|---:|---:|---:|---:|---:|---:|---:|
| −1.5 | 4.58 | 11.3% | 60.9% | 27.5% | 0.3% | 0.645 |
| −0.5 | 3.09 | 11.3% | 44.8% | 36.5% | 7.4% | 0.745 |
| 0.0 | 2.00 | 11.3% | 11.5% | 33.3% | 43.9% | 1.060 |
| +0.5 | **1.00** | 11.3% | 0.0% | 27.3% | 61.4% | 1.194  ← Ob floor binds |
| +1.0 | **1.00** | 11.3% | 0.0% | 27.3% | 61.4% | 1.194  ← identical |
| +2.0 | **1.00** | 11.3% | 0.0% | 27.3% | 61.4% | 1.194  ← identical |

- **L1 confirmed:** leverage gates Quality smoothly (E[Quality] 0.645 → 1.194). The σ-leverage→damage chain works as designed. Quality swing Partial→Overwhelming = 0.6→1.5 = **2.50×**, multiplied (D1) by Impact (Str+Heft, additive) × Coupling (material×mode×coverage).
- **F2 surfaced:** from net_σ ≥ +0.5 (≈ one Strong contributor) the Ob floor (=1) binds, and **all further leverage is wasted** — the degree distribution is identical from +0.5 to +2.0. The `tanh` cap governs `eff_σ`, not `eff_Ob`; the Ob floor is a second, downstream cap that flattens the favorable-side response on low-Ob strikes — exactly the dead-zone `tanh` was chosen to avoid.

`[GAP: damage magnitude — resistance grid + DMG_SCALE unread (damage_model_design.md).]` Damage-*number* distribution not reproduced (would require fabricating the resistance grid). Quality/degree contribution is computed above; the magnitude layer is the next stress-test target (see §5).

---

## 2 · STAGE 2 — Findings → Lessons (severity-ranked, worst-first)

| # | Sev | Finding | Lesson | Remediation |
|---|---|---|---|---|
| **F1** | **P2** | **Resolution-form contradiction.** `m1.eff_ob` is documented "DISPLAY ONLY … resolution uses the μ-shift (`p_success`), base_Ob untouched." `r1.resolve_action` actually resolves via `effective_ob` (Ob-shift, floored at 1) and bands the degree against the shifted Ob. z-equivalent **only at TN7** (σ_per_die≈0.80=`SIGMA_N_COEFF`); diverges at Controlled/Desperate and (LOG C) at low-Ob/high-leverage. The balance validation (r3/r4) ran on the Ob-shift form → it validates a resolution the engine spec does **not** prescribe. | **L1** (one path, one role — pick the canonical resolution form) | Adopt the μ-shift as canonical (per m1's own docstring): boost the rolled net by `eff_σ·σ·√N`, band the **boosted** net against the **fixed** base Ob. Re-run r3/r4 on that form. |
| **F2** | **P2** | **Ob-floor premature saturation (favorable dead-zone).** Under r1's Ob-shift, favorable leverage above ~net_σ 0.5 on a low base-Ob strike drives `eff_Ob` to the floor (1); additional leverage yields **zero** marginal effect (LOG C). Undercuts "every advantage pays" (Ω-d) and distorts build incentives on easy strikes. | **L6** (don't stack caps that flatten the response) | **Subsumed by the F1 fix:** the μ-shift has no Ob floor (it moves the mean, not the threshold), so the favorable side stays smooth (ceiling ~98% vs Ob-shift's ~89% at 8D/Ob2). Fixing F1 fixes F2. |
| **F3** | **P3** | **Uniform impact is a continuous-model property, validated ≥5D only.** Discrete d10 swings 33pp across 1–18D (0pp at 1–2D). **Not a combat defect** (combat resolves continuous, ≥6D). Risk lands on (a) any reuse of the shared σ-leverage substrate <5D, (b) the dice-based player mental model vs the continuous runtime <5D. | **L3/L4** (don't resolve load-bearing small pools on the raw substrate) | Already applied to combat via the 6D floor. Document a **≥5D validity bound** on the engine; apply the same floor/aggregation discipline to any sub-5D substrate reuse. |
| **F4** | **P3** | **Canonical-record drift.** `canonical_sources.yaml` still maps `combat → combat_v30.md` (abandoned engine); every addendum says "prose-propagation PENDING"; base `RATIFIED_2026-05-29.md` still states R2/W1/W5 forms the D1 addendum superseded, with no inline supers_by marker. A reader fetching the canonical combat doc gets the OLD engine. | n/a (consolidation) | Per PI `<document_consolidation>`: the **2026-05-30 ratified set is the master**; propagate into `combat_v30.md` + `canonical_sources.yaml`; mark R2/W1/W5 superseded-by-D1 inline. **Lane-A / gated work** (see §4). |
| **F5** | **P3·minor** | (a) `sigma_leverage_handoff §1a` misstates the F1 anchor: 25.8pp is the **δσ=0.7** impact (Φ(0.7)−0.5), not δσ=1.0 (=34.1pp); m1 code is correct. (b) Canonical `POOL_FLOOR=5` is unreachable in combat (base +6 ⇒ min 6) → dead constant for combat. (c) Lever/damage magnitudes are Class-C sim-seeds (acknowledged-unpinned). | L2/triage | Doc fix (a); decide whether the canonical floor is meant to bind elsewhere (b); calibrate (c) once F1 settled. |

**Passes that narrow the fix:** `tanh` soft-cap (no foreclosure) ✓; C-04 closure / uniform impact in the continuous runtime ✓ (corroborated by r3/r4); L1 leverage→quality smooth ✓; decisive-phrase removes the attrition loop ✓.

---

## 3 · STAGE 3 — NERS verdict (per criterion)

- **N — PASS.** No redundant roll or variable; σ-leverage, state-gating, degree bands all load-bearing. Nit: the canonical `POOL_FLOOR=5` never binds in combat (F5b).
- **R — FAIL (P2).** Two inconsistent definitions of the *same* resolution (F1) and a favorable-side dead-zone (F2). The adverse extreme is robust (F2-goal verified, no foreclosure), but "fully formed / error-free" fails while the engine has two resolution forms and the validation runs on the non-prescribed one.
- **S — FAIL (P3, boundary).** Smooth and uniform ≥5D on the continuous runtime (combat safe), but the runtime-vs-dice model diverges <5D (F3) and the canonical record disagrees with the ratified design (F4). Friction at the continuous/discrete category boundary below 5D.
- **E — PASS (caveat).** The σ-leverage idea is elegant (one δσ currency, hidden math, smooth `tanh`). Caveat: the Ob-floor dead-zone (F2) makes "more advantage, identical result" on easy strikes — denting "intuit outcomes from simple choices." The F1→μ-shift fix restores it.

---

## 4 · STAGE 4 — Re-test of proposed fixes

| Fix | Re-test (Phases 1–6 on the fix) | Result |
|---|---|---|
| **F1 → adopt μ-shift** (per m1 docstring) | Removes the Ob floor from resolution ⇒ **also fixes F2** (favorable side smooth to ~98%). Uniform impact preserved (z-shift = `eff_σ` at every TN, TN-exact). No new cliff (`tanh` still governs `eff_σ`). Degree banded against fixed base Ob ⇒ Overwhelming `2·Ob` threshold stable. Clean for combat (≥6D). | **PASS** — F3 sub-5D caveat unchanged (orthogonal). |
| **F3 → document ≥5D bound + floor sub-5D reuse** | Adds a documented constraint; no mechanic change; prevents silent misuse of the substrate. Doesn't harm E. | **PASS** |
| **F4 → propagate ratified set to master** | Per `<document_consolidation>`: regenerate-not-hand-merge for derivative files; authored docs (combat_v30, canonical_sources) edited to the 2026-05-30 master; supersessions marked. No mechanic change. | **PASS** — but Lane-A / gated (below). |

`[OPEN — Jordan decision]` The F1 fix raises the **max-favorable ceiling** from ~89% (Ob-shift, floored) to ~98% (μ-shift) on low-Ob strikes. This is the *inverse* of the foreclosure question: **how dominant should a maximally-leveraged fighter be?** A ~98% ceiling means even total setup advantage whiffs ~2%; a lower intended ceiling would argue for a different cap shape. Design intent, not a balance bug.

---

## 5 · Persistence, gating, and next targets

**Not auto-committed — by design:**
- **Active 3-lane write-disjoint model.** Lanes A (canon/** + designs/{personal,proposals}/**), B (infra), C (sim/tests) are **all active** (handoffs 1–3). Editorial findings live in `canon/editorial_ledger.jsonl` (Lane A's exclusive territory); filing them now would violate write-disjointness.
- **ED-NNN ID-collision backlog.** ~94 same-ID/different-finding collisions are open for **Jordan adjudication** (canon authority). Assigning new ED IDs for F1–F5 risks colliding; ID assignment is Jordan's call.

→ Findings are **staged inline** (this artifact). On request I can: (a) write this audit to `designs/audit/2026-05-31-combat-stress/` via `safe_commit` (scope `cleanup`/`audit`); (b) draft the F1–F5 editorial entries for Jordan to ID-assign and Lane A to file; (c) implement the F1 μ-shift fix in `r1` and re-run r3/r4.

**Next stress-test targets (this was the resolution-engine core; "begin"):**
1. **Damage magnitude** — needs `damage_model_design.md` (resistance grid, `DMG_SCALE`): stress the D1 `Impact × Coupling × Quality` distribution and the plate ~95% / blunt-thrust-grapple counters.
2. **Lever magnitudes** — Stance 5×5 cell values, Reaction coefficients, set bonuses, `AGI_TEMPO_PER_POINT` under **equal-budget 31-pt** builds (the parity axis r3/r4 began).
3. **Duel vs battlefield (C1)** — the suppressed-defence battlefield context and the mass-battle bridge.

`[CONFIDENCE: high — every number traces to a canonical constant (params/core, modifier_system_spec) or the actual r1/m1 code; computed by exact convolution, not memory or sampling.]`

---
---

# PART 2 — Damage Magnitude (extension)

Extends Part 1 to the **consequence/damage layer**. `[READ: damage_model.py, m9_wound_model_bottomup.py, r2_consequence_wounds.py, m3_weapon_class_layer.py, damage_model_design.md, armour_axes.py — full; r3_parity_sweep.py, r4_full_channel_parity.py — import scan]` `[CONFIDENCE: high — all numbers reproduced from the three damage models' actual constants; exact arithmetic.]`

## PART-2 VERDICT

**NON-COMPLIANT (damage layer)** — fails **R** and **S**, driven by a ratification-vs-implementation split, not by any single model being bad. **The ratified damage model (D1) is wired into nothing**; the combat the game runs uses the pre-D1 formula D1 was ratified to replace; and **wiring D1 in (the obvious fix) would introduce a Strength-dominance inversion in light weapons.** The damage layer needs a genuine reconciliation decision, not a mechanical propagation.

```
N: PASS* — wound-gate model necessary & clean; *D1 is canon-of-record but currently necessary-for-nothing (orphaned).
R: FAIL  — ratified D1 != wired r2 (D-F1); degree defined two ways in one pipeline (D-F2).             [D-F1 P1, D-F2 P2]
S: FAIL  — runtime under-protects armour vs the ratified design (2–4×); 4 armour representations.       [D-F1 P1, D-F5 P3]
E: borderline — D1's 3-factor model is elegant, but the SYSTEM carries 3 damage models + 4 armour grids.
```

## The three damage models found in the repo

| Model | Form | Status | Strength handling |
|---|---|---|---|
| **r2** `r2_consequence_wounds.py` | `net + STR×mult + weapon_mod`; **crit (net≥3) doubles weapon_mod** | **WIRED + VALIDATED** — r3/r4 `import strike_damage from r2` | multiplicative `STR×mult` (heavy-blunt ×3, canonically kept W4) |
| **D1** `damage_model.py` | **Impact × Coupling × Quality** | **RATIFIED 2026-05-30 (canon-of-record) — orphaned, imported by nothing in the resolution chain** | additive Impact (`Str+Heft`) inside a multiplicative product |
| **M9** `m9_wound_model_bottomup.py` | `net + bounded-Str(cap 3) − resist` | **ORACLE ONLY** (r2 self-test historical check; not a damage path) | additive, **capped at +3** |

## D-F1 [P1] — D1 ratified but orphaned (with real balance divergence)

`from r2_consequence_wounds import strike_damage` in **both** `r3_parity_sweep.py` and `r4_full_channel_parity.py`; `damage_model.py` (D1) is imported by nothing in the resolution/validation chain. So the validated "C-04 closed / Str near-band 46.5%" result is on the **old formula**, not the ratified D1.

**MECHANICAL LOG D — wired (r2) vs ratified (D1), Str4, base Ob 2, End4 (WI 10):**

| weapon | armour | degree | r2 dmg (wnd) | D1 dmg (wnd) | Δ |
|---|---|---|---:|---:|---:|
| arming sword | none | Success | 9 (0) | 8 (0) | −1 |
| arming sword | **plate** | Success | **6** (0) | **2** (0) | −4 |
| longsword | none | Success | 16 (1) | 15 (1) | −1 |
| longsword | **plate** | Success | **10** (1) | **3** (0) | −7 |
| war hammer | none | Overwhelming | 26 (2) | 26 (2) | 0 |
| war hammer | **plate** | Success | **19** (1) | **13** (1) | −6 |

The models roughly agree **unarmoured**, but diverge **2–4× vs armour**: under the ratified D1 plate is far more protective (cut mitigation 75–80% vs r2's 33–38%; see LOG F). **The combat the game runs (r2) materially under-protects armour relative to the ratified design.** Orphaning is not cosmetic.

## D-F2 [P2] — degree/Overwhelming defined two ways in one pipeline

`combat_v30 §5` Degree Table is **flat** (`1=Partial / 2=Success / 3+=Overwhelming`; `m3.DEGREE_OVERWHELMING_MIN=3`, `r2` crit `net≥3`). `params/core §Degrees` is **Ob-scaled** (`net≥2·Ob ∧ net≥3`; `r1.degree_of_success`, `damage_model.degree_of`). The σ-leverage pipeline uses **both**: r1 bands Ob-scaled for the resolution outcome, r2 crits on flat net≥3.

**MECHANICAL LOG E — divergence at net=3, base Ob=2:** r2 → **crit** (weapon_mod doubled, dmg 13); D1/r1 → **Success** (net 3 < 2·Ob 4; dmg 8). Same hit, two verdicts on whether it's a crit. Canon contradicts itself; the contradiction is live in code.

## D-F3 [P2] — D1's additive Impact gives a non-uniform Strength *ratio* (light-weapon inversion)

**MECHANICAL LOG G — Str7/Str1 damage ratio, Success hit vs none:**

| weapon | r2 ratio | D1 ratio |
|---|---:|---:|
| arming sword (light) | 2.0× | **7.5×** |
| longsword (heavy) | 2.2× | 2.6× |
| war hammer (heavy) | 2.8× | 2.5× |
| estoc / thrust (light) | 2.0× | **8.0×** |

D1's `Impact = Str + Heft` (light +0, heavy +3) gives a **constant absolute Str gap** (self-test-verified: light gap 13 = heavy gap 13) — but a **wildly non-uniform ratio**, because the same gap sits on a small light baseline (Str1→2 dmg) vs a large heavy baseline (Str1→8 dmg). Ratio = `(7+H)/(1+H)` → light **7×**, heavy **2.5×**. **D1 makes light/finesse weapons *more* Strength-dominant than heavy ones** — inverting the historical/intuitive direction and undercutting the L1 "skilled fencer's modest-Impact light weapon kills via placement" story (under D1 the light weapon's damage is dominated by raw Str, not finesse). r2 has the sensible ordering (heavy ≥ light, all 2.0–2.8×).

This is the skill's **Lesson 2** in action: D1 achieves uniform *form* ("additive, constant gap") but non-uniform *impact* (ratio). Goal-over-form says target the impact — and the ratio impact is non-uniform.

## D-F4 [P3] — multiplicative one-shot tail (both models; intent check)

**MECHANICAL LOG H — max blow (Str7, Overwhelming net6, vs unarmoured), End4 Health 40:**
war hammer → **37 dmg = 92% of Health, 3 wounds (near-fell)** in *both* models; longsword ~80%; arming sword/estoc ~48–60%. Intended "lethal unarmoured combat / decisive phrase," but a 92%-Health single blow is at the one-shot edge. r2's WoundTracker caps multi-gate at MW+1 (no unbounded overkill), so it's bounded — but confirm a near-one-shot max blow is the desired ceiling.

## D-F5 [P3] — armour represented four ways

`m3.WEAPON_ARMOR_MOD` (+mod table, **wired** via r2) · `m9.ARMOR_RESIST` (subtractor, oracle) · `damage_model.RESIST` (continuous fractions by mode, **orphaned** D1) · `armour_axes.MITIGATION` (reproduces the table; the A2 material/coverage axes). "Unified by canon" in principle; four representations in fact; only the M3 table is wired. **LOG F — plate mitigation (Success, vs heavy):** r2 cut 33–38% / war hammer **0%** (heavy_blunt +5 ignores plate); D1 cut **75–80%** / war hammer 24%. D1's plate-vs-cut better matches "plate negates cuts"; r2's war-hammer-vs-plate 0% is arguably too strong.

---

## PART-2 Stage 2 → lessons + remediation (severity-ranked)

| # | Sev | Lesson | Remediation |
|---|---|---|---|
| **D-F1** | **P1** | **L1** (one model, one role) | **Decision required.** Per `<document_consolidation>` the 2026-05-30 ratified set is the master → D1 should win → **wire D1 into r2 and re-run r3/r4**. *But* see D-F3: wiring D1 as-is imports the light-weapon Str inversion. So: wire D1 **and** fix D-F3 first, **or** keep r2 and back-port only D1's better plate-vs-cut. Either way, one model. **P1 → would file to `editorial_ledger.jsonl` (see gating).** |
| **D-F2** | **P2** | consistency / L6 | Pick one degree definition. Ob-scaled (params/core, used by r1/D1) is the more recent/principled; reconcile `combat_v30 §5` flat table + `m3`/`r2` crit-trigger to it. **P2 → editorial.** |
| **D-F3** | **P2** | **L2** (uniform *impact*) | If D1 is chosen: bound the light-weapon Str ratio — e.g. a heft floor on *all* weapons, a multiplicative Str term `(1+k·Str)`, or M9-style capped additive Str — so the ratio is uniform across weights. Validate on the equal-budget duel sweep. |
| **D-F4** | **P3** | intent gate | Confirm the ~92%-Health max blow is the intended unarmoured ceiling; if not, lower `DMG_SCALE` or cap per-blow wounds. |
| **D-F5** | **P3** | **L1** | Collapse to one armour representation (D1's coupling/A2 matrix if D1 wins; the M3 table if r2 wins). Delete the others or mark oracle-only. |

**Passes (narrow the fix):** the `WoundTracker` (WI/MW/Health/decisive-multi-gate/felled-cap) is clean, canonical, and reproduces `derived_stats §4.1` ✓; all three models reproduce the historical *directions* (plate negates cut; blunt/thrust beat plate) ✓; the decisive multi-gate strike (one big hit crosses several WI gates, capped at MW+1) is a sound "one telling blow" model ✓.

## PART-2 Stage 4 — re-test of the obvious fix (wire D1 + reconcile degree)

| Fix | Re-test | Result |
|---|---|---|
| **Wire D1 into r2; re-run r3/r4** | LOG G shows D1 introduces a **7.5–8× light-weapon Str ratio** (vs r2's 2.0×). The existing "Str near-band 46.5%" is on r2; under D1 the build-axis parity **must be re-derived** and will likely shift (finesse builds become Str-hungry). | **NEW FINDING (D-F3)** — wiring D1 as-is fails L2; **must fix D-F3 first.** |
| **Reconcile degree to Ob-scaled** | Changes r2's crit trigger (flat net≥3 → Ob-scaled) → fewer crits at Ob≥2 → lower damage distribution → re-validate pacing. No new cliff. | **PASS** pending re-validation. |

`[OPEN — Jordan / design decision]` The damage layer's reconciliation is **not** a mechanical propagation: (1) which model is canon — the ratified-but-orphaned D1, or the wired-but-superseded r2? (2) if D1, how to bound its light-weapon Str inversion (D-F3)? (3) the one degree definition (flat vs Ob-scaled)? These are design calls, surfaced with the numbers; not Claude's to settle.

## PART-2 gating (same constraints as Part 1)

D-F1 and D-F2 are **P1/P2 canon-integrity** findings → per the audit gate they belong in `canon/editorial_ledger.jsonl`. **Not filed**, because: (a) the 3-lane write-disjoint model is active and `canon/**` is Lane A's exclusive territory; (b) the ~94-entry ED-ID collision backlog is Jordan-adjudication. They are drafted ready-to-file here. On request I can draft the exact ED entries (un-numbered, for Jordan ID-assignment) and a reconciliation proposal for the damage-model decision.

`[DRIFT: sigma_leverage_handoff §4 lists M9 as "the right direction for the damage layer" — superseded twice over: D1 (ratified, multiplicative) replaced M9's additive form, and r2 (wired) never used either. The §4 work-log is stale on the damage layer.]`
