# Faction Layer — Comprehensive Resolution Audit (σ-Leverage Engine as Diagnostic)

**Scope:** all faction items. **Instrument:** the σ-leverage engine (`engine/`) used as a diagnostic yardstick — every faction quantity is classified, every dice-resolved component is *numerically instrumented* against the engine's two guarantees (uniform per-point impact; no foreclosure wall), and each is given a NERS verdict + Stage-4 re-test.
**Method:** `valoria-resolution-diagnostic` skill, Stage 1–4.
**Date:** 2026-05-30.

`[SELF-AUTHORED — bias risk]` Two layers of self-authorship here, both flagged and actively countered:
1. The **engine** is mine (built/fixed this session). Using it as the yardstick risks confirmation. Counter: I instrument the *defect* numerically and report where the engine is **contraindicated** (most faction items) as forcefully as where it helps.
2. The **prior faction diagnostic** (`designs/audit/2026-05-28-resolution-diagnostic/`, prior session, also Claude) is my evidentiary base. The skill guardrail forbids defending prior output. Counter: §6 re-examines the prior verdicts independently and records where an independent reviewer pushes back.

---

## VERDICT (worst-first, no false balance)

**The faction layer is *mostly* NERS-compliant on resolution, and the engine's principle is already canon where it matters** — the ratified `d+σ` Domain Action resolver (`stats_1_7_scale.md`, ED-865/874: slope **+10%/point constant**, floor 0.05, cap 0.90) *is* the σ-leverage engine applied to faction actions. **It does not help most faction items** (they are deterministic, clock-driven, or route to healthy personal pools — forcing it in fails NERS-N/E). **The one genuine, unfixed defect is a residual set of bare-stat faction actions still on the legacy dice method** that the migration's "governed checks" list silently omitted:

- **F-RESID [P2] — five+ bare-stat Unique Actions never migrated.** `stats_1_7_scale.md` ratified the resolver for Domain Actions / Suppress / Rebuttal / Treaty / §1.4, but the **Unique Actions table on the same page still reads "vs Ob N" on raw dice**: Crown **Royal Decree** (Mandate vs Ob 2), Church **Excommunication** (Mandate vs target/2+1 or Ob 2), Hafenmark **Sovereign Authority Doctrine** (Mandate vs **Ob 4**), Varfell **Private Collection** (Intel vs Ob 2), Guilds **Economic Leverage** (Wealth vs Wealth). These are the exact small-pool bare-stat family the resolver was built to fix — numerically instrumented in §3. This is the same class the prior diagnostic flagged as `FCN-1 / "bare-stat tactic migration (sim-deferred)"`; it remains open.
- **F-BAL [P2 — blocker, not a defect] — two governed migrations are balance-load-bearing and fail Stage-4 as naive swaps.** Parliamentary transfer (PT-PARL-1) and Treaty re-bind (TE-1) were balance-validated at N=1000 *on dice*; the resolver's floor 0.05 raises weak-actor odds → shifts the validated v12c equilibrium. The engine improves resolution quality but is **gated behind re-tuning** here.
- **F-LESS2 [P3] — open Lesson-2 item.** The prior faction-layer loop work left "F4 (Lesson-2, ratifiable next)" open — a residual non-uniform absolute modifier; carried forward, not closed.

Everything else passes. **Net: the engine helps exactly one place new — F-RESID — and even there one sub-case (CI-60 Seizure) is borderline-healthy and should be left alone.**

---

## §0 — BALANCE & GAMEPLAY IMPACT (where the engine actually helps)

The engine improves things in two registers: **balance** (outcome fairness — no dominant/dead strategy, comeback paths, validated equilibria) and **gameplay** (player experience — legible odds, agency, decisions that reliably translate to outcomes). Explicit, bounded map:

**1. ALREADY improving — combat (engine deployed).**
- *Balance — closes C-04 (pool-size dominance).* Sim history (R1, M8b) found raw pool size (Agi×2+History) dominated outcomes, because the d10 S-curve compounds a pool-size edge (the √N small-pool dynamic — a bigger pool simply wins more). R1 demoted the Agi-scaled pool and re-expressed Agility as a *bounded σ-tempo* contributor → "bring the bigger pool" is no longer a dominant strategy. **Caveat:** the engine closed *C-04 specifically*; it did **not** balance combat alone — R8 still shows Strength ~85% dominant / Spirit ~12% dead, which is channel-magnitude tuning, not the engine.
- *Gameplay — setup becomes the decider and is intuitable.* A flat −1D wound is brutal at 5D, trivial at 18D; under σ-leverage a "Moderate" advantage is the *same* probability swing at any pool, so stacking stance/reading/position does a predictable thing — the intended "set up before you strike" feel.

**2. CAN NEWLY improve — faction Unique Actions (F-RESID, the bare-stat actions still on legacy dice).**
- *Balance — removes the ~0% lockout, adds a comeback floor.* §3B: a Mandate-1 faction vs Hafenmark's Ob-4 Doctrine succeeds **0.00%** on dice — its identity action is *impossible*, so a weak faction has no comeback vector (death-spiral / runaway-dominance risk). The resolver floors at **5%** ("hard but never impossible"). Direct balance fix.
- *Balance — equalizes marginal stat value.* §3A: a stat point is worth **+13.7pp** at low stat but **+6.6pp** at high on dice (2× non-uniform) vs a flat **+10pp** on the resolver → stat investment is fairly priced across the whole 1–7 range.
- *Gameplay — legible odds; structure (not noise) decides pivotal acts.* "vs Ob 4 on bare dice" is opaque; `50% + 10%·M` is instantly readable. A bare 2D roll deciding "strip the Circles bonus / swing CI ±3" is a coin-flip on a near-irreversible outcome; the resolver makes the *margin* (structural position) the driver, with only a stochastic tail.

**3. The biggest, least-obvious win — balance-ABILITY.** The engine replaces the lumpy √N dice curve with three clean, monotonic balance knobs: **slope** (+10%/pt = how much stats matter), **floor** (0.05 = comeback reliability), **cap** (0.90 = overmatch reliability) — all "tunable by future Jordan-logged ratification." On dice, tuning fights non-uniformity (a change does different things at different pools); on the engine a knob change does the same thing everywhere. The engine's largest balance contribution is making *balancing itself tractable and honest* — it does **not** auto-deliver balance (channel δσ magnitudes still need tuning, but on a uniform substrate that tuning behaves predictably).

**4. A balance RISK, not an improvement — F-BAL (parliamentary_transfer + treaty re-bind).** Same resolution defect, but balance-validated at **N=1000 on dice** (v12c: Crown 24.7 / Church 28.6 / HF 24.2 / Varfell 22.5). The 5% floor raises weak-actor odds off the ~1% dice wall → more transfers / cheaper Crown maintenance → **shifts the validated equilibrium.** Here the engine *changes* balance; whether that is an *improvement* is **unverified** pending a resolver re-sweep + re-tune. A naive swap is a balance-regression risk, not a win.

**5. NO balance gain — do not apply.** Deterministic / accounting (Treasury, muster, tallies — no variance); clocks / accumulators (CI, MS, PI, Deniability Debt, Graduated Autonomy — linear/stepped is *correct*); healthy dice (personal combat resolution, social contest 5–18D, aggregated mass battle, CI-60 Seizure's ~8D pool — variance already low).

**One line.** The engine already fixed combat pool-dominance (C-04); can newly fix the faction Unique Actions' lockout + non-uniformity (free migration, clear balance + gameplay win); turns faction balancing into three legible knobs; is a balance *risk* pending re-tuning on the two equilibrium-pinned actions; and does nothing for the deterministic/clock/healthy-pool majority.

---

## §1 — THREE-CATEGORY CLASSIFICATION (load-bearing; lessons apply differently per category)

Per the diagnostic's category model. Misclassifying produces false findings — a linear clock is *not* a Lesson-2 violation.

| Faction quantity | Category | Engine relevance |
|---|---|---|
| Faction stats — Mandate / Influence / Wealth / Military / Intel / Stability (1–7) | **Base parameter** | **YES when rolled bare as a pool** — the small-pool source. This is the engine's domain. |
| Per-territory Legitimacy / Popular Support (0–7) | Base parameter (per-territory; LPS-1) | Feed Mandate aggregation; not rolled bare → engine N/A |
| CI / Mending Stability / Institutional Pressure / Public Instability | **Discrete accumulator (clock)** | **NO** — linear/stepped is *correct*; exempt from Lessons 2 & 6. Engine contraindicated. |
| Deniability Debt 0–7 / Shadow Renown 0–10 / Graduated Autonomy 0–4 / Warden tracks | **Discrete accumulator** | **NO** — bounded, spaced thresholds, intended. Engine contraindicated. |
| Treasury / muster / CI-vote tallies | **Deterministic accounting** | **NO** — computed, no roll. Engine N/A. |
| Domain Action / Suppress / Vote / Treaty resolution | **Dice → (now) resolver** | **ALREADY MIGRATED** — resolver = the engine's principle. |
| Unique Actions (Royal Decree, Excommunication, …) | **Dice (base parameter rolled bare)** | **YES — UNMIGRATED (F-RESID).** |

---

## §2 — PER-ITEM DIAGNOSIS (Phase 0 decomposition → engine-fit verdict)

Verdict legend: **MIGRATED** (resolver already applied) · **ENGINE-INDICATED** (real defect the engine fixes, not yet applied) · **CONTRAINDICATED** (no defect; engine would fail NERS-N/E) · **N/A** (no resolution mechanic).

| # | Faction item | Phase-0 components | Engine-fit verdict | Basis |
|---|---|---|---|---|
| 1 | **Domain Action resolver** (Assert, Reconstitute, Govern, Suppress, Rebuttal, Treaty, §1.4) | dice→**resolver** | **MIGRATED** | `stats_1_7_scale §Domain Action Resolution` (ED-865/874). Slope 0.10 constant = uniform impact; floor 0.05 = no wall. |
| 2 | **Unique Actions** (Royal Decree, Excommunication ×2, Hafenmark Doctrine, Private Collection, Guild Leverage) | **dice (bare stat)** | **ENGINE-INDICATED (F-RESID)** | Same page, Unique Actions table — still "vs Ob N" raw dice. §3 instruments. |
| 3 | **CI-60 Territorial Seizure** | dice (Influence+⌊CI/15⌋) | **CONTRAINDICATED (borderline)** | §3D: pool ≈ 8D, not a small-pool bare stat. Migrating adds churn without fixing a defect. Leave. |
| 4 | **parliamentary_transfer** core roll | dice (bare stat) | **ENGINE-INDICATED but BALANCE-PINNED (F-BAL)** | Prior PT-PARL-1: resolver fix correct in principle, fails Stage-4 naive (equilibrium shift). |
| 5 | **treaty_expiration** re-bind (Senator Outward) | dice (bare stat) | **ENGINE-INDICATED but BALANCE-PINNED (F-BAL)** | Prior TE-1: same class; re-bind rate sets Crown maintenance cost. |
| 6 | **ci_political** forum modifier | dice + tally + resolver | **PARTIALLY MIGRATED** | Prior CIP-1: Parliament=tally (Lesson-4 correct), resolver paths done, **Treaty path open**. |
| 7 | **faction_succession_split** | dice→**two-stage resolver** | **MIGRATED (engine-pattern)** | Prior FSS-1 + FSS-LOOP-1: Stage-1 contested resolver + Stage-2 deterministic gap. |
| 8 | **faction_layer collapse loop** (§1.4/§1.5/§5.7) | dice (Stab check) + determ | **MIGRATED + LOOP-BOUNDED** | §1.4 Stab check → resolver; FSS-LOOP-1 determ Stab≤2 floor; FSS-LOOP-2 Wealth≥1 re-muster (Lesson 5). |
| 9 | **peninsular_strain** | clock + determ | **CONTRAINDICATED** | Prior PST-1 (P3, the only finding) is a *warning-window* consistency fix; advance capped+damped; MS=0 intended+safeguarded. No dice defect. |
| 10 | **faction_behavior** | determ + resolver-fed | **CONTRAINDICATED** | §3.7 Ob_modifier clamped ±2, *feeds the resolver and inherits its uniformity*; loops bounded+damped. Already engine-consistent. |
| 11 | **faction_politics** | determ progression + accumulators | **CONTRAINDICATED** | Pivotal rolls route to **personal** engines (fieldwork Ob2/3, social Ob2) on large pools; ladders bounded+spaced. Not the bare-stat family. |
| 12 | **clock_registry** | clock registry | **N/A** | No roll-fed shallow disguised-binary; Evidence clock owned by fieldwork (determ five-filter). |
| 13 | **faction_state_authoring** | authored values | **N/A** | No resolution mechanic; values within consuming bounds. |
| 14 | **faction_canon** | reference mirror | **N/A** | Mirrors source mechanics; surfaces FCN-1 (= F-RESID) by design. |
| 15 | **Institutional Mandate / Uphold-Appease, Covert +1 Ob, Embedding +1D, Wealth sink** | modifiers on DA | **MIGRATED-by-inheritance** | These are ±Ob / ±D inputs to actions that now resolve via the resolver; they inherit uniform impact. (Caveat: ±1 Ob on a *dice* Unique Action is non-uniform — folds into F-RESID.) |

---

## §3 — ENGINE-AS-DIAGNOSTIC: NUMERICAL INSTRUMENTATION OF F-RESID

Continuous engine, TN7 (`params/core.md`: μ=0.40, σ=0.800), the canonical NPC faction-roll TN. Dice = bare stat as pool vs the action's Ob. Resolver = ratified `clamp(0.50+0.10·M, 0.05, 0.90)`.

**(A) Non-uniform impact of a stat point — the core σ-leverage defect.** Royal Decree / Excommunication-nonleader / Private Collection (stat vs **fixed Ob 2**):

| stat | P (dice, Ob2) | Δ per +1 stat (dice) | P (resolver, M=s−2) | Δ per +1 (resolver) |
|---|---|---|---|---|
| 1 | 2.3% | — | 40.0% | — |
| 2 | 14.4% | **+12.2pp** | 50.0% | +10.0 |
| 3 | 28.2% | **+13.7pp** | 60.0% | +10.0 |
| 4 | 40.1% | +11.9pp | 70.0% | +10.0 |
| 5 | 50.0% | +9.9pp | 80.0% | +10.0 |
| 6 | 58.1% | +8.1pp | 90.0% | +10.0 |
| 7 | 64.7% | +6.6pp | 90.0% | +0.0 |

Dice: a stat point is worth +13.7pp at the bottom and +6.6pp at the top — **non-uniform by 2×** (the 1/√N signature). Resolver: flat +10pp. This is exactly the engine's Lesson-2 fix.

**(B) Foreclosure wall — "punching up" against a hard fixed Ob.** Hafenmark Sovereign Authority Doctrine (Mandate vs **Ob 4**):

| Mandate | P (dice, Ob4) | P (resolver, M=Mand−6) |
|---|---|---|
| 1 | **0.00%** | 5.0% |
| 2 | **0.23%** | 10.0% |
| 3 | 2.17% | 20.0% |
| 4 | 6.68% | 30.0% |

A Mandate-1 faction is **walled at ~0%** under dice — the pivotal action is *impossible*, not merely hard. The resolver floors at 5% ("hard but never impossible"). Lesson-3 + the foreclosure guarantee.

**(C) Lumpy contested Ob.** Excommunication-vs-leader (Mandate vs ⌊target/2⌋+1), attacker Mandate 4: dice P steps 64.6 → 40.1 → 40.1 → 19.1 → 19.1 → 6.7 → 6.7% as the target's Ob jumps on the floor function — a **step-function** in the defender's stat. Resolver margin is smooth/linear (80→20%). Lesson-2 (uniform) + Smooth.

**(D) The exception that proves the scope.** CI-60 Seizure (Influence+⌊CI/15⌋ ≈ **8D** vs Ob 7−PT): P = 10.8/21.3/36.2/53.5/70.2% across prosperity tiers. An 8D pool is **not** the bare-stat small-pool case — variance is already low and impact near-uniform. **Migrating this fails NERS-N** (no defect to fix). It belongs *out* of F-RESID — recorded to prevent over-application.

---

## §4 — NERS VERDICTS (per affected item; verdict-first)

```
ITEM: Domain Action resolver (item 1)   COMPONENTS: dice→resolver
VERDICT: NERS-compliant. N pass (one resolver, no redundancy) · R pass (uniform +10pp,
  floor 0.05 no wall, four-degree ladder intact) · S pass (consistent with the determ
  spine; output unchanged so Domain Echo/costs untouched) · E pass (legible odds: 50%+10·M).

ITEM: Unique Actions (item 2 — F-RESID)   COMPONENTS: dice (bare stat)
VERDICT: NON-COMPLIANT.
  N pass — the actions themselves are necessary (faction identity levers).
  R FAIL — small-pool bare-stat rolls on pivotal/irreversible effects (Decree ±1 stat;
    Excommunication strips Circles + territory Legitimacy; Doctrine swings CI ±3): §3A 2×
    non-uniform, §3B ~0% wall for weak actors. P2.
  S FAIL — paradigm-inconsistent: these sit on the SAME PAGE as the migrated resolver but
    use the superseded "vs Ob" dice method. P2.
  E pass — individually legible; the inconsistency is the S/R problem, not E.
  → Lesson 3 (don't roll bare small pools on pivotal outcomes) + Lesson 2 (uniform impact).

ITEM: parliamentary_transfer / treaty_expiration re-bind (items 4,5 — F-BAL)
VERDICT: resolution-defective (same Lesson-3 class) BUT remediation is BALANCE-GATED.
  R FAIL on resolution grounds; remediation BLOCKED — naive swap fails Stage-4 (below).

ITEMS 9,10,11 (peninsular_strain / faction_behavior / faction_politics)
VERDICT: NERS-compliant. Engine CONTRAINDICATED — adding σ-resolution here would add
  apparatus to systems with no small-pool dice defect → fails N and E. Do not touch.
```

---

## §5 — STAGE-4 RE-TEST OF PROPOSED ENGINE PORTS

Run the diagnostic on the *fix*, not the original.

- **F-RESID → migrate Unique Actions to the resolver.** Re-test: legacy "vs Ob O" maps by the ratified rule `D = max(1,(O−1)·2)` (Ob2→D2, Ob4→D6); contested actions use target-stat as difficulty. Slope 0.10/floor/cap apply unchanged. **Re-test result: clean for the *non-balance-pinned* members** (Royal Decree, Excommunication, Private Collection, Guild Leverage are not part of the v12c N=1000 equilibrium). Output ladder unchanged → named hooks (strip Circles, ±1 stat, CI swings) reattach to the same degrees. **No new cliff, no new loop, uniform + floored.** ✅
  - *One Stage-4 caveat (honest):* the resolver removes the ~0% wall, so a Mandate-1 faction's Doctrine/Excommunication goes from impossible to 5–10%. That is *intended* (foreclosure is the defect) but it is a **frequency change** to rare pivotal actions — flag for Jordan as the deliberate consequence, not a hidden one.
- **F-BAL → migrate parliamentary_transfer / treaty re-bind.** Re-test: **FAILS.** The floor 0.05 raises weak-proposer / re-bind odds off the ~1% dice wall → more transfers / cheaper Crown maintenance → **shifts the v12c equilibrium** (Crown 24.7% etc.) the balance pass validated *on dice*. `[OPEN TRADE-OFF]` — requires re-running the N=1000 sweep on the resolver and re-tuning, a Jordan-gated balance decision. The engine is *resolution-correct* here but cannot be dropped in without re-validation.
- **F-LESS2 → close the open Lesson-2 item (F4).** Not re-tested here — needs the specific residual modifier identified in the prior faction-layer loop work; carried forward as a pointer, not closed.

---

## §6 — INDEPENDENT RE-EXAMINATION OF THE PRIOR DIAGNOSTIC (guardrail: do not defend prior output)

Where an independent reviewer pushes on the prior faction diagnostic:

1. **The migration's "governed checks" list is presented as complete; it is not.** The prior work ratified Domain Actions / Suppress / Rebuttal / Treaty / §1.4 and then *separately* logged the Unique-Action residual as "sim-deferred." Reading `stats_1_7_scale.md` top-to-bottom, a player/implementer sees a ratified resolver section immediately followed by Unique-Action tables still in dice — **the document contradicts itself on the same page.** The prior diagnostic under-weighted this as a deferral; it is a live S-failure (F-RESID, P2), not a backlog note. *(This is the independent-reviewer criticism the skill demands I surface.)*
2. **"Sim-deferred" conflates two different reasons.** Royal Decree / Excommunication / Private Collection / Guild Leverage are deferred for *no load-bearing reason* (they are not equilibrium-pinned) — they can migrate now. Only parliamentary_transfer / treaty re-bind are *genuinely* sim-blocked (F-BAL). Lumping all of them as "sim-deferred" hides that ~4 of them are free, low-risk migrations. **§3/§5 separate them; the prior diagnostic did not.**
3. **CI-60 Seizure was not explicitly excluded.** §3D shows it is borderline-healthy (8D pool). Absent an explicit exclusion, a "migrate the bare-stat residual" instruction would wrongly sweep it in. Recorded here as **CONTRAINDICATED**.
4. **Where the prior diagnostic holds (confirmed, not rubber-stamped):** the 6 CONTRAINDICATED systems (peninsular_strain, faction_behavior, faction_politics, clock_registry, faction_state_authoring, faction_canon) are correctly compliant — I re-checked each against the three-category model and the bare-stat test; none has a small-pool dice defect. The resolver ratification itself (slope/floor/cap) is sound and is the engine's principle. FSS-1's two-stage resolver is the correct engine-pattern fix.

---

## §7 — REMEDIATION (worst-first)

| Sev | Finding | Action | Gate |
|---|---|---|---|
| **P2** | **F-RESID** — 4 free bare-stat Unique Actions unmigrated (Royal Decree, Excommunication, Private Collection, Guild Leverage) | Migrate to the resolver (`D = max(1,(O−1)·2)`; contested → target-stat). Re-tests clean (§5). | Jordan ratify (mechanical-tier; **frequency caveat** on weak-actor wall removal). |
| **P2 (blocker)** | **F-BAL** — parliamentary_transfer + treaty re-bind | Do **not** naive-swap. Re-run N=1000 on the resolver, re-tune, then migrate. | Jordan balance decision (`[OPEN TRADE-OFF]`). |
| **P2** | **F-RESID/S** — `stats_1_7_scale.md` self-contradiction (resolver section vs Unique-Action dice tables) | Even if migration is deferred, annotate the Unique-Action tables "pending resolver migration (ED-865/874 class)" so the page stops contradicting itself. | Editorial. |
| **P3** | **F-LESS2** — open Lesson-2 residual (prior "F4") | Identify the specific residual absolute modifier; close per Lesson 2. | Jordan ratify. |
| **P3** | **CI-60 Seizure** | Record as **CONTRAINDICATED** so future migration does not sweep it in. | Note only. |

---

## §8 — STAGED LEDGER CANDIDATES (NOT auto-filed)

The audit task-gate routes P-findings to `editorial_ledger.jsonl`, but ID self-assignment is barred by the 94-ID-conflict backlog + Jordan canon-authority. Staged for your call (next free above ledger max 884 → ED-885+):

```json
{"id":"ED-885","type":"audit_finding","severity":"P2","status":"open-jordan-ratify","system":"faction-unique-actions",
 "finding":"F-RESID: bare-stat Unique Actions (Royal Decree, Excommunication, Private Collection, Guild Leverage) still on the legacy dice 'vs Ob' method on the same page as the ratified d+sigma resolver; small-pool non-uniform impact (2x, §3A) + ~0% foreclosure wall (§3B). Not equilibrium-pinned -> free migration.",
 "fix":"Migrate to the resolver (D=max(1,(O-1)*2); contested=target stat). Stage-4 clean (engine_audit_harness-class check). Frequency caveat: removes the weak-actor ~0% wall (intended).",
 "evidence":"stats_1_7_scale.md §Domain Action Resolution + §Unique Actions; faction-sigma audit §3","authority":"Claude mechanical-tier, Jordan-vetoable","id_provisional":true}
{"id":"ED-886","type":"audit_finding","severity":"P2","status":"open-jordan-balance","system":"parliamentary_transfer+treaty_expiration",
 "finding":"F-BAL: resolver migration is resolution-correct but BALANCE-LOAD-BEARING; floor 0.05 shifts the v12c N=1000 equilibrium. Naive swap fails Stage-4.",
 "fix":"Re-run N=1000 on the resolver, re-tune, then migrate. OPEN TRADE-OFF.","authority":"Jordan balance decision","id_provisional":true}
{"id":"ED-887","type":"audit_finding","severity":"P3","status":"open-editorial","system":"stats_1_7_scale",
 "finding":"F-RESID/S: §Unique Actions tables contradict the ratified resolver section on the same page. Annotate as pending-migration even if deferred.","authority":"editorial","id_provisional":true}
```

---

## §9 — PROVENANCE (`[READ:]` trail)

- `[READ: references/canonical_sources.yaml — enumerated 31 faction/provincial canonical paths]`
- `[READ: params/factions/stats_1_7_scale.md — FULL (31,388 chars): the ratified d+σ resolver, governed-checks list, Unique Actions tables, CI/PI clocks]`
- `[READ: designs/audit/2026-05-28-resolution-diagnostic/ledger_candidates_consolidated.json — all 10 system diagnostic verdicts + resolver_spec + faction_layer_loop_ratifications + LPS redesign]`
- `[READ: canon/02_canon_constraints.md — P-constraints (audit gate)]`
- `[READ: skills/valoria-mechanic-audit/SKILL.md + valoria-resolution-diagnostic SKILL (project file) — diagnostic method]`
- `[VERIFIED: §3 numerical instrumentation — continuous engine TN7 (math.erf), dice-vs-resolver across stat 1–7 and Ob 2/4 + contested step-Ob + 8D seizure pool, recomputed this session]`
- `[CONFIDENCE: high — every verdict traces to a canon cite or a recomputed number; the one assertion I cannot fully close without a sweep is F-BAL's equilibrium-shift magnitude (the prior N=1000 was on dice), which is exactly why it is flagged OPEN TRADE-OFF rather than resolved.]`
- `[ASSUMPTION: "all faction items" = the faction/provincial canonical set + the action/Unique-Action resolution mechanics — basis: that is the faction layer's resolution surface; deep accumulator/clock internals were confirmed by category + the prior diagnostic rather than re-derived, since the engine is contraindicated there by category. If you want a full Stage-1–4 re-run on a specific compliant system, name it.]`
```
