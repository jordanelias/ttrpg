---
name: valoria-resolution-diagnostic
description: >
  Diagnostic + NERS-compliance wrapper for any Valoria **rolling engine** — any mechanism
  that turns a contest or state into an outcome via a draw (dice, U[0,1), card, etc.). It is
  NOT a general "any mechanic" auditor: systems with no draw (character sheets, pure
  deterministic ledgers, static stat blocks, bare accumulators) are OUT OF SCOPE and route to
  valoria-mechanic-audit. The skill tests a rolling engine against five engine properties,
  using the two current canonical instances (sigma-leverage continuous engine;
  deterministic+stochastic resolver) plus an explicit branch for any new/third rolling engine.
  Pipeline: (Stage 0) validate the skill against adjudicated cases; (1) Phase 0–6 diagnostic
  to locate where the engine fails under stress; (2) map findings to the scoped lessons;
  (3) per-engine NERS verdict + remediation; (4) re-test the fix. ALWAYS use when checking
  whether a ROLLING ENGINE is NERS-compliant, stress-testing a resolver, or checking leverage
  uniformity / clamp-or-floor cliffs / wrong-engine-for-the-pool. Trigger on: "is this rolling
  engine NERS compliant", "diagnose this resolver", "stress test this roll", "engine audit", "resolution diagnostic audit", "resolution audit", "is this sigma-leverage or deterministic+stochastic", "does this resolution scale",
  "leverage non-uniformity", "clamp/Ob-floor conflict", or when the orchestrator routes a
  resolution diagnosis. The bare word "audit" routes to nothing; the audit-word phrases that route here are "engine audit", "resolution diagnostic audit", and "resolution audit" — NOT "NERS audit" (currently unassigned). Do NOT trigger to audit a character sheet, inventory, pure economy
  ledger, or other non-rolling system — that is valoria-mechanic-audit's job.
---

**Prerequisite:** This skill reads the engine mechanics from a **canonical reference baseline** AND the **session-local target**; never diagnose from *memory* — read the actual artifact, never a remembered or hallucinated version. Read from the working tree the canonical reference baseline below, plus the target (which may be session-local work, not canon — see the last bullet):
- `params/core.md` — core engine: **Die Rule (legacy/TTRPG), Continuous Engine (Decision E), Degrees, Obstacle Scale, Expected Value table, Pool Floor**.
- `designs/audit/2026-05-28-resolution-diagnostic/domain_action_resolver_spec.md` — the **deterministic+stochastic resolver** spec (ratified per ED-874).
- `designs/audit/2026-05-28-engine-replacement/engine_replacement_reconciled.md` — the engine-replacement reconciliation (continuity correction; resolver-vs-engine boundary).
- `canon/02_canon_constraints.md` (P-01–P-15 + GD-1/2/3) and `canon/definitions.yaml` (NERS criteria).
- **Target rolling engine — whatever work/files exist local to the session** (a draft, an in-progress design, an uncommitted artifact, the latest local revision). It need **NOT** be canon (D2): the point of the modular architecture is to bring canon in from the repo as the *baseline* while the latest **local session work supersedes the stale canon**. If a canonical version of the target exists, read it from the working tree and declare which local artifact supersedes which canonical source; otherwise audit the local work directly. This breaks the canonical-bootstrap circularity — a system can be NERS-audited *en route to* becoming canon, not only after it already is.

**Relationship to `valoria-mechanic-audit`:** that skill checks *internal consistency* (formulas, gaps, redundancy) for **any** system, rolling or not. This skill checks **resolution fitness under stress for rolling engines specifically**, plus the loops/cliffs a rolling engine's output drives, and ends in a NERS verdict. A non-rolling system, or pure non-roll balance (a deterministic feedback loop with no draw), belongs to `valoria-mechanic-audit` or a dedicated balance pass — not here. Run consistency first if the engine is unverified; run this when the question is "does this rolling engine hold up at its extremes, on the right engine model, and is it NERS-compliant."

---

## SCOPE GATE (apply first — before any phase)

**Is there a rolling engine here?** A *rolling engine* = a mechanism that resolves an outcome by a **draw** (dice net, `U[0,1)`, card, shuffle, any randomized resolution). If the answer is **no** — the target is pure state (a character sheet, attribute block, inventory), a pure deterministic ledger (CI economy math, Treasury accounting with no draw), or a bare accumulator/clock with no per-segment roll — **this skill DOES NOT APPLY.** Say so plainly and route to `valoria-mechanic-audit` (consistency) or a balance pass. Do not manufacture a NERS verdict for a non-rolling system.

**Non-rolling components inside a composite are recognized, not diagnosed.** Most systems are composites (a social contest = an exchange *roll* + a Persuasion *clock*; mass battle = engagement *rolls* + a TroopCount *ledger* + a Morale *clock*). Tag the non-rolling parts only to **bound scope** — so a linear clock feeding a roll is not mis-flagged as a cliff, and a stat that feeds a pool is treated as the roll's *input*, not as a thing this skill verdicts. The one apparent-non-roll that IS in scope: a **shallow clock where one roll ≈ one segment** is a disguised rolling binary — treat it as a rolling engine (Lesson 4).

> Recognize-and-route-out (do not diagnose here): deterministic-accounting (no draw); continuous resources (Health, Stamina, Composure, Coherence — data that *feeds* a roll); base parameters (1–7 stats — roll *inputs*); bare/deep accumulators (Evidence, CI, MS — legitimately linear, multi-threshold; not a resolver). Guard: a linear clock is not a cliff, a multi-threshold tracker is not a Lesson-6 violation, a base parameter is not a pool.

---

## WHY THIS SKILL EXISTS

Valoria no longer resolves anything by **raw d10-vs-raw-obstacle success-counting**. That discrete success-pool is retained **only** as the legacy TTRPG-mode specification (`params/core.md §Die Rule (d10)`); it is **not** the videogame's resolution path, and any claim that a live videogame system "rolls N d10 and counts successes ≥ TN against a flat Ob" is a defect to flag (Lesson 3), not a baseline.

A rolling engine fails at the **extremes of its input range** and at the **boundaries between engines**, not at "the small dice pool where 1/√N bites" — both current engines were built to kill that. The live failure surface:
- a component on the **wrong engine for its pool regime** (raw dice on a bare strategic pool; a deterministic resolver bolted onto a healthy skill contest that wanted leverage);
- **leverage that escapes its band** at an input extreme (sigma-leverage runs too hot at low base-stat — ED-875);
- **clamp / floor collisions** (the continuous engine's Ob-shift hitting the P-232 Ob≥1 floor — ED-884; a resolver's `FLOOR`/`CAP` saturating);
- the continuous engine **missing its continuity correction** and misreading small-pool odds (ER-2);
- and a **new/third rolling engine** that satisfies none of the property guarantees the two canonical engines were designed to give.

---

## THE ROLLING-ENGINE PROPERTY TEST (genericity core — read before diagnosing)

A rolling engine is diagnosed against **five properties**, regardless of which engine it is. The two named modes below are the *current canonical instances* that satisfy them; a rolled component matching neither is diagnosed against these properties directly.

| # | Property | Failing looks like |
|---|---|---|
| **P-i** | **Legible odds** — the player can read/predict their chance from the board. | Odds emerge only from opaque dice interactions; the player cannot anticipate them. |
| **P-ii** | **Uniform / in-band leverage** — a unit of advantage moves P(success) by a consistent, in-band amount across the *whole* input range. | Per-point dP varies wildly by scale (1/√N), or spikes out of band at an extreme (ED-875). |
| **P-iii** | **Bounded + monotonic response** — no cliffs; respects floors/caps; more advantage never lowers success. | A continuous input crosses a discrete boundary that jumps the outcome (ED-884 Ob-floor; stacked cliffs). |
| **P-iv** | **Graded, recoverable output** — emits degrees (not a fragile binary) on pivotal stakes; failure is survivable. | A bare binary on an irreversible, load-bearing outcome; no underdog floor. |
| **P-v** | **Right engine for the pool regime** — the resolution method fits the pool size and the presence/absence of a setup axis. | Raw bare-stat dice on a pivotal action; a deterministic resolver on a healthy skill contest. |

### Instance A — Sigma-leverage (Continuous Engine)

**Base distribution** (`params/core.md §Continuous Engine`, §Expected Value): `net ~ Normal(μ·N, σ·√N)`.

| TN | μ (E[net]/die) | σ/die |
|---|---|---|
| 6 (Controlled) | 0.50 | 0.806 |
| 7 (Standard) | 0.40 | 0.800 |
| 8 (Desperate) | 0.30 | 0.781 |

At TN 7: `net ~ Normal(0.4·pool, 0.8·√pool)`; **`σ_N = 0.8·√Pool`** is the spread the leverage layer scales against.

**Continuity correction (REQUIRED for fidelity; ER-2, `engine_replacement_reconciled §2/§5`).** Raw continuous `P(success)` runs **4–32% low** vs discrete below ~5D (missing continuity term). Fix: resolve against **`net − (Ob − 0.5)`** → agreement to ~1–3% across the whole range (0.067 vs 0.070 at 2D, Ob 3). One-line engine edit — **status: LANDED 2026-06-22 in `params/core.md §Continuous Engine` (commit a3d3888).** A continuous component without it = a P-iii/P-i defect: TTRPG and videogame modes disagree on the same action's odds.

**Leverage layer** (`designs/audit/2026-05-29-combat-armature/`, handoff `2026-05-29-combat-armature-sigma-leverage`): strategic-setup advantages accumulate as **Δσ**, **tanh soft-capped**, converted to an **Ob shift scaled by `σ_N`**, so probability impact is **uniform regardless of pool size** (P-ii). This is the **C-04 (Agi-OP) fix**: outcome decoupled from raw pool/dice count.

**Leverage axis — the μ-shift / Ob-shift relation (exact for P(success), not for degrees).** Advantage can enter `net ~ Normal(0.4·Pool, σ_N)` on **either** axis: shift the **roll mean** `μ_net = E[net]` (a "+X to net" / innate or trait bonus), or shift the **obstacle Ob** (the leverage layer above). On the **success boundary** the two coincide: with `z = (μ_net − Ob)/σ_N`, a μ-shift of `+δ` and an Ob-shift of `−δ` both move `z` by `+δ/σ_N` — **identical P(success)**, and identical `net − Ob` margin-gauge distribution.
- **Off the success line the axes diverge — the degree ladder is not a function of the margin.** Overwhelming keys on `2·Ob` (and absolute `net ≥ 3`), Failure on absolute `net ≤ 0`. A μ-shift slides the whole `net` distribution up: it pulls away from the Failure floor, but the `2·Ob` ceiling does not approach. An Ob-shift drops that ceiling twice as fast (`2·Ob → 2·Ob − 2δ`) while the absolute Failure floor does not move. *Worked (Pool 9, Ob 4, δ/σ_N = 0.5): P(success) identical at 0.63, but P(Overwhelming) 0.09 (μ) vs 0.20 (Ob), P(Failure) 0.02 (μ) vs 0.07 (Ob).* So the axis is a real lever — **μ-shift = floor protection, Ob-shift = ceiling inflation, interchangeable only at Success.** The relation also breaks at the `Ob ≥ 1` floor (P-232/ED-884): the Ob-axis saturates there; the μ-axis has no analogous bound.
- **Uniformity (P-ii) lives in the scaling, not the axis.** `Δz = δ/σ_N`. A shift gives in-band uniform leverage **iff `δ` scales with `σ_N` (= 0.8·√Pool)** → `Δz = k`, pool-independent. The Ob-axis leverage layer already does this (Δσ → tanh → Ob shift scaled by σ_N); a μ-axis modifier must scale the **same way**.
- **The flat-shift trap (a P-ii defect — and it requires a *varying* pool).** Across cases where Pool differs, a **flat** advantage — constant `+X` to net, or constant `−X` Ob, *not* σ_N-scaled — gives `Δz = X/(0.8·√Pool) ∝ 1/√Pool`: hot at small pools (flat `+1` to net → `Δz` 0.625 @4D vs 0.3125 @16D, 2× hotter, `= √(16/4)`) — the `1/√N` non-uniformity the engine exists to kill, re-imported through a flat bonus. A naive "+X to net" skill/trait bonus is a **wrong-form leverage defect (Lesson 2 / P-ii)** unless σ_N-scaled. *Scope:* the non-uniformity lives in N — a fixed-/no-pool continuous resolver (a σ-space engine with no pool count) has no `√N` term and is exempt; there a flat shift is uniform.
- **Neither axis de-swings.** A μ-shift and an Ob-shift both leave `σ_N` (the absolute spread of the draw) unchanged — they relocate the operating point without tightening it. Small-pool swing is a property of N (a wide, discrete, skewed draw relative to the degree bands), dissolved only by more dice or aggregation (Lesson 3 / Lesson 4), never by a location shift on either axis.
- **Sub-5D (ER-2) binds both axes.** A μ-shifted `net` read through the raw Normal below ~5D still carries the continuity error (ER-2 order — the 4–32% seen at the floor); resolve against `net − (Ob − 0.5)` (Phase 3c), and never report flat-Normal μ-shift odds at the floor.

**Degree output** (`params/core.md §Degrees of Success`): magnitude `net − Ob` as a gauge; Overwhelming (`net ≥ 2·Ob` AND `net ≥ 3`), Success (`net ≥ Ob`), Partial (`0 < net < Ob`), Failure (`net ≤ 0`). Ob cap 20, **Ob min 1 (P-232)**. Pool floor 1D.

**Obstacle is a continuous axis (videogame mode; `params/core.md §Obstacle Scale` + §Continuous Engine).** Ob is continuous, not integer-quantized: fractional Ob (weapon condition, cover, terrain) is canonical, and a fractional base Ob is a real intermediate *difficulty* setting (`P = Φ((μ_net − Ob)/σ_N)` is strictly monotonic in Ob — Ob 1.4 ≠ Ob 1.6). It rides the same continuous Ob axis as the leverage layer's Ob-shift and composes with it, but it is *difficulty*, not a structural lever: it relocates the operating point without changing `σ_N` (tunes difficulty, and via the `2·Ob` bar the Overwhelming rate; never small-pool swing). The integer collapse `Ob 1.4 ≡ 1.6 ≡ 2` happens only in discrete/TTRPG mode (integer `net`); the videogame resolves continuously, so fractional Ob is live — and below ~5D its odds take the continuity correction `net − (Ob − 0.5)` like any continuous read (now canonical, §Continuous Engine).

**Scope:** healthy pools with a real setup/skill axis — personal combat (~5–18D), social contest, thread operations, **aggregated** mass battle.

**Stress points (where it violates a property):**
- **Low-input leverage spike (P-ii; ED-875, OPEN, Gate G8):** sigma-leverage is **hot at low Command (~0.500/pt at Cmd 2)**, in-band only by Cmd 4–7. Check per-point dP across the *whole* range, not the midpoint.
- **Ob-floor collision (P-iii; ED-884, resolved):** advantage as an Ob reduction can push `eff_Ob` below the P-232 floor of 1; it must saturate at the floor (or convert to magnitude), never violate Ob≥1.
- **Sub-5D approximation (P-i/P-iii):** below ~5D the Normal model is shaky; with the continuity correction it tracks, without it it does not. Routine sub-5D use without the correction = finding.
- **Flat (un-scaled) advantage (P-ii; the μ/Ob leverage axes):** advantage added as a flat "+X to net" or flat "−X Ob" instead of σ_N-scaled — `Δz = X/(0.8·√Pool) ∝ 1/√Pool`, hot at small pools (varying-pool only). The leverage layer avoids this by scaling its Ob-shift by σ_N; a bypassing flat bonus does not.

### Instance B — Deterministic+stochastic resolver (Domain Action Resolver)

**Concept** (`domain_action_resolver_spec.md §0`): *deterministic odds, stochastic resolution* (P-i by construction). `P(success)` is a clean function of the stat contest the player can read; the outcome is still drawn. Chance is kept (a deterministic outcome would be exploitable); only the **odds** are made legible. CK3/EU/KoDP idiom; removes the faction layer's NERS-S inconsistency of dice on a deterministic ledger.

**Resolver** (`domain_action_resolver_spec.md §1`):
- Margin **`M = acting_stat − difficulty`** (difficulty = contested target's stat, or a fixed action-difficulty). Ob inverts via **`D = max(1, (Ob − 1)·2)`** (ED-885).
- `P_success(M)        = clamp(BASE + SLOPE·M, FLOOR, CAP)`
- `P_overwhelming(M)   = clamp(BASE + SLOPE·M − OVW_OFFSET, 0, OVW_CAP)`
- `P_atleast_partial(M)= clamp(BASE + SLOPE·M + PARTIAL_BAND, P_success, FAIL_FLOOR)`
- Draw `r ~ U[0,1)` (lower better): `< P_overwhelming` → Overwhelming; `< P_success` → Success; `< P_atleast_partial` → Partial; else Failure.

**Tuned parameters (PROPOSED — Jordan's to ratify/tune; *form* canonical, *numbers* a starting point):** BASE 0.50, SLOPE 0.10 (**flat +10%/pt — uniform legible leverage, P-ii**), FLOOR 0.05, CAP 0.90, OVW_OFFSET 0.35, OVW_CAP 0.55, PARTIAL_BAND 0.20, FAIL_FLOOR 0.97 (≥3% residual failure even at max overmatch — P-iv).

**Pathologies it fixes** (`domain_action_resolver_spec.md §3`, vs the legacy bare dice):

| Pathology | Legacy bare dice | Deterministic+stochastic |
|---|---|---|
| Floor degeneracy (stat 2 vs Ob 3) | 0.069 | 0.300 |
| Punching-up wall (stat 2 vs strong 7, Ob 4) | 0.010 | 0.050 |
| Leverage uniformity | non-uniform (1/√N: 0.354/pt @ stat 2 → 0.189/pt @ stat 7) | **flat 0.10/pt** |

The leverage-uniformity row is the one the Stage-4 aggregation sweep **proved cannot be fixed by any pool transformation** — only deterministic+stochastic makes leverage constant.

**Drop-in output** (`§4`): same four-degree ladder → Domain Echo (`scale_transitions_v30 §5`: Success → +1, Overwhelming → +2, cap ±2), cost tables, CI formula all unchanged. Only the resolution *method* changes.

**Scope** (`§5`): bare-stat faction checks — **Domain Actions** (Assert, Reconstitute, Govern, Claim Masterless; ratified ED-874), **Suppress** (Mandate; Failure → Stab −1 preserved on the Failure degree), **Parliamentary Rebuttal** (graded; Overwhelming → +1 preserved), **§1.4 Accounting Stability Check** (`M = Stability − loss_magnitude`; **co-design with §1.3 recovery, CC-4** — don't double-count). **Keep dice** for aggregated mass battle and personal/social (5–18D, healthy).

**Authority note (ED-865):** the resolver is **not** mandated by GD-2. GD-2 (`canon/02 §B`) governs faction action-**selection** ordering, not resolution; the "GD-2 mandates a deterministic+stochastic resolver" text was a struck miscitation. The resolver stands on acclaimed-game precedent, ratified by ED-874 ("works well", Jordan 2026-05-31).

**Stress points:** clamp saturation outside `M ∈ [−4, +4]` (intended bounds, not cliffs — verify monotonic across the boundary, `§6` confirms for the proposed params); parameter calibration ("form right, numbers unverified" → `[OPEN — Jordan tuning]`, not a structural defect); hook preservation (Suppress→Stab−1, Rebuttal-Overwhelming→+1 must attach to the right degree).

### Instance C — `[NEW ENGINE]` (anything matching neither A nor B)

A rolled component that is neither the continuous engine nor the deterministic+stochastic resolver — e.g., a card/deck draw, an opposed-pool contest with different statistics, a timing mechanic, a weighted-event table — is **diagnosed against P-i…P-v directly**, not forced into A or B. Output: a property-by-property verdict plus `[NEW ENGINE — diagnose by properties; surface for canon ratification]`. The remedy is normally to bring it onto an engine that satisfies the five properties, or to ratify it as a new canonical instance after it passes them.

### The legacy raw-d10 pattern

`params/core.md §Die Rule (d10)` (face 1 = −1, 2–6 = 0, 7–9 = +1, 10 = +2; net may be negative; no chain) is **TTRPG-mode only**. In videogame canon it is superseded: healthy pools → A; bare-stat strategic → B. **Flag any videogame system whose canonical resolution is "roll a bare pool vs a flat Ob and count successes" as a wrong-engine defect** (Lesson 3).

---

## ENGINE-SELECTION DECISION RULE (apply in Phase 0; testable)

For each rolling component, pick the engine by this rule (not by feel):

- **pool ≥ ~5D AND a genuine setup/skill axis exists** → **Instance A (sigma-leverage).**
- **bare stat (1–7D), pivotal/load-bearing outcome, no aggregation available** → **Instance B (deterministic+stochastic).**
- **pool is aggregable** (sum unit/derived values to a healthy pool, as mass battle does) → **aggregate, then A.**
- **shallow clock (one roll ≈ one segment)** → a disguised rolling binary → route to B or deepen the clock (Lesson 4).
- **matches neither / ambiguous** → **Instance C** property test + `[NEW ENGINE]` flag.

`~5D` is the boundary because below it the continuous Normal model needs the continuity correction to stay faithful (ER-2) and bare dice become degenerate at high stakes (the faction 0.069/0.010 case).

---

## STAGE 0 — VALIDATION (run once to confirm the skill is calibrated)

Before trusting the skill's verdicts, confirm it reproduces canon-adjudicated ground truth. **The skill is correct iff, run blind, it returns these known answers; if it does not, fix the *skill*, not the canon.** Re-run after any change to the skill's logic (regression guard).

| Calibration case | Adjudicated answer the skill must reproduce | Source |
|---|---|---|
| **Pre-resolver faction layer** (bare-stat Domain Actions) | **NON-COMPLIANT** (R/S/E fail: fragile bare-stat binary on pivotal, irreversible outcomes; dice on a deterministic ledger) → remedy "route bare-stat Domain Actions to deterministic+stochastic." | engine_replacement_reconciled §0/§3 (diagnostic NON-COMPLIANT ≡ repair-and-keep); ED-874 |
| **Post-resolver faction layer** | **Compliant** for the resolved Domain Actions (legible, flat-leverage, ledger-consistent). | ED-874 ("works well") |
| **Continuous engine used below 5D without `Ob − 0.5`** | **Finding** — fidelity defect (P-iii/P-i), TTRPG vs videogame odds diverge 4–32%. | ER-2, engine_replacement §2 |
| **Sigma-leverage advantage driving `eff_Ob < 1`** | **Finding** — Ob-floor cliff (P-iii); must respect P-232 Ob≥1. | ED-884 |
| **Mass-battle Size/Command pre-fix cliff** | **Finding** — stacked cliff (Lesson 6); resolved by the ED-876 fix. `[verify ED-876 internals before relying on this row]` | engine_replacement §3 (MB5/ER-9); ED-876 |

A run that flips a verdict on any row, or invents a defect canon ratified as fine, means the skill is miscalibrated — diagnose the skill.

---

## STAGE 1 — THE DIAGNOSTIC (Phase 0–6)

Run in order. Phase 0 applies the Scope Gate + Engine-Selection Rule and routes the rest.

### Phase 0 — Scope gate, decompose, assign engine
1. **Scope gate:** is there a rolling engine? If none → out of scope; route to mechanic-audit; stop.
2. **Decompose** the system; for each **rolling** component assign its engine via the Decision Rule (A / B / C). **Recognize** non-rolling components only to bound scope (do not diagnose them).
3. **Flag raw-d10 leaks** — any rolling component whose canonical resolution is bare-pool-vs-flat-Ob.

### Phase 1 — Locate the stress point (per engine)
- *Instance A:* the **low-input end** (low stat / low Command) where per-point leverage runs hot (ED-875), AND the sub-5D continuity-correction region.
- *Instance B:* the **clamp boundaries** (`M` near FLOOR/CAP) and any matchup pushing `M` outside `[−4, +4]`.
- *Instance C:* the input extremes where each of P-i…P-v is most likely to break.
- **1b. Exposure:** how often the stress point is reached — (i) condition enumeration, (ii) degradation/advantage-path count, (iii) canon frequency signals. Weak/low-stat actors are routine, not edge.

### Phase 2 — Characterize what the stress point decides
- **2a. Outcome type:** binary / graded magnitude / clock increment. For B, the four-degree ladder is graded — preserve the *degree distribution*, not just P(success).
- **2b. Stakes & reversibility:** low / recoverable / irreversible-load-bearing.
- **2c. Risk profile (operationalized — tie to numbers, not feel):**

  | Dimension | Low | Medium | High (flag) |
  |---|---|---|---|
  | Impact | per-point dP in-band; outcome non-critical | dP near a band edge; affects one track | **dP outside the engine's target band, OR the outcome flips a load-bearing state** |
  | Exposure | extreme/rare states only | minority of scenarios | routine or by design |
  | Irreversibility | retryable / Fail-Forward | recoverable in 1–2 seasons | permanent or compounding |

  Rank (H/M/L)³. Any H is a flag; two+ H is a candidate finding.

### Phase 3 — Check the engine's curves (and the loops/cliffs its output drives)
- **3a. Leverage uniformity (P-ii):** does the engine deliver in-band uniform leverage across the *whole* input range? (Both A and B target this by construction; ED-875 proves it can still fail at an extreme.) **Instance-A axis check:** an advantage injected as a flat μ-shift ("+X to net") or flat Ob-shift — not σ_N-scaled — reintroduces 1/√Pool non-uniformity where the pool varies (see Instance A — the μ/Ob relation and its limits); uniform leverage requires σ_N-scaling on *whichever* axis.
- **3b. Cliffs (P-iii):** continuous input crossing a discrete boundary that jumps the outcome; engine-internal risks — the sigma Ob-shift hitting the P-232 floor (ED-884), Mode-B clamp edges (verify monotonic). **Scope:** cliffs *in the engine's response* or that a discrete boundary forces on the engine's output. A cliff in a purely non-roll quantity → mechanic-audit.
- **3c. Continuity correction (Instance A):** resolving against `net − (Ob − 0.5)`? Absent + routinely-small-pool = finding (ER-2).
- **3d. Role conflation, scoped to the roll:** does a variable that **feeds or reads** this engine carry more than one independent role (capacity AND cohesion AND collapse), such that the roll's input/output is overloaded? Pure non-roll role conflation → mechanic-audit.

### Phase 4 — Check the loops the engine participates in (highest severity)
- **4a.** Identify feedback loops whose gain runs **through this rolling engine's output, or that gate its input** — including cross-system / cross-scale couplings (e.g., a resolved Domain-Action/Suppress outcome → Stability → territory → muster → military → back into the resolver's inputs). List inter-system edges; read cross-referenced docs from the working tree. *(A feedback loop with no rolling engine in its cycle is out of scope — route to mechanic-audit or a balance pass.)*
- **4b.** For each in-scope loop: **damper present?** (gain < 1 per loop cycle) and **cap present?** (hard bound on the amplified variable) — two separate checks; defect = **both undamped and unbounded**. *(Re-evaluate gain under the correct engine: `engine_replacement_reconciled §6` reclassified faction collapse from "deterministic" to "probabilistic, loss-weighted" once bare dice → Mode B; the resolver raises recovery odds.)*

### Phase 5 — Intent gate (every candidate finding)
Is the discontinuity / asymmetry / absolute-effect / loop **deliberate**? Evidence (≥1): explicit design-doc statement; a paired safeguard designed for it; designer (Jordan) confirmation. Underdetermined → `[INTENT UNDETERMINED]`, carry forward. Don't guess.
Safeguard adequacy: adequate if it bounds the loop/cliff to a recoverable state within the system's natural recovery timescale.
- Deliberate **with** adequate safeguard → pass. Deliberate **without** → true finding. Accidental / undetermined → true finding.

### Phase 6 — Score & triage
Per engine, risk profile (impact / exposure / irreversibility), worst-first. Carry each true finding to Stage 2.

**Stage 1 output:** `resolution_diagnostic_<engine>.md`
```
| Finding | Component | Engine (A/B/C) | Property (P-i..P-v) | Stress point | Outcome@stress | Impact | Exposure | Irreversibility | Intent | Phase | Severity |
```

---

## STAGE 2 — MAP FINDINGS TO LESSONS

Each true finding maps to one or more corrective lessons. Lessons are **scoped conditions, not universals**; several are now **embodied by the engines** — the lesson is "use/verify the engine that delivers the property," not "hand-build it."

| # | Lesson (scoped) | Property | Fixes |
|---|---|---|---|
| **1** | **One variable, one role** — split only where a roll-input/output variable genuinely carries two independent jobs. *(Minimal — over-splitting harms Elegance.)* | — | Phase 3d role conflation |
| **2** | **Leverage must be empirically in-band across the whole input range** — verify it, don't assume it. The engine *targets* uniform impact; this lesson is the *verification obligation* that catches the extreme where it doesn't (ED-875). | P-ii | Phase 3a out-of-band leverage |
| **3** | **Right engine for the pool regime (master lesson)** — apply the Decision Rule. Healthy pool + axis → A; bare-stat pivotal → B; neither → C. **Raw d10-vs-Ob on a bare strategic pool is the defect** this removes. Don't put a roll where deterministic-accounting/clock is the right tool, and don't put a deterministic resolver on a healthy skill contest. | P-v | Phase 0/1/2 wrong-engine |
| **4** | **Route unavoidable accumulation through a clock deep enough to average** — a shallow clock (one roll ≈ one segment) is a disguised binary and is in scope as a rolling engine. *(Distinct from Lesson 3: clocks are for genuine accumulation; a single pivotal decisive check routes to B, not a 1-segment clock.)* | P-iv | disguised-binary clock |
| **5** | **No loop the engine drives — including cross-system — both undamped and unbounded.** One safeguard sized to per-cycle gain. *(`intent_of_game` is itself a positive feedback loop — doubly critical.)* | P-iii/P-iv | Phase 4 undamped+unbounded loop |
| **6** | **Bounded, continuous engine response; never stack cliffs** — sigma Ob-shift respects P-232 Ob≥1 (ED-884); Mode-B clamps stay monotonic; the continuity correction is present (ER-2). | P-iii | Phase 3b/3c cliffs / missing continuity |

**Mapping rule:** a finding mapping to no lesson is either not a real resolution defect (recheck Phase 5) or needs a seventh lesson — surface it. For an **Instance-C** finding, map to the violated property (P-i…P-v) directly. Multi-defect engines map to several lessons.

**Stage 2 output:** append `| Lesson(s)/Property | Remediation |` to each finding row.

---

## STAGE 3 — NERS VERDICT

Convert lesson-tested findings into the canonical NERS criteria (`canon/definitions.yaml`). The verdict is **the rolling engine's contribution to system NERS** (this skill scopes to the engine, not the whole system). NERS-compliant only when all four pass.

> **Verdict framework note.** NERS (N/R/S/E) is in active use in the 2026-05-29 resolver/engine docs and is the verdict here. A separate **"omega" Class-A-new-system vetting framework** is referenced in the combat-armature handoff; its spec was **not read this session** (`[UNVERIFIED — omega not read; do not assume it supersedes NERS]`). A brand-new Class-A engine additionally goes through omega; do not substitute it for NERS here without reading its definition.

| Criterion | Pass test (rolling-engine lens) |
|---|---|
| **Necessary (N)** | No roll redundant. Watch the inverse: do **not** migrate a healthy dice engine to Mode B (over-correction — `domain_action_resolver_spec.md §5`). A Lesson-1/5 fix that *adds* apparatus must itself be necessary. |
| **Robust (R)** | Holds at its extremes: leverage in-band across the *whole* range (ED-875); continuity correction present (ER-2); Ob-floor respected (ED-884); clamps monotonic; loops bounded; no fragile bare-stat binary; graded recoverable output. |
| **Smooth (S)** | Transitions cleanly across scales; resolution consistent with sibling engines and with any deterministic spine it sits on (faction layer's old S-failure was dice-on-a-ledger — Mode B removes it). |
| **Elegant (E)** | Player can intuit outcomes from legible odds (Mode B: P read off the board, flat SLOPE/pt). A fix that bolts on structure the engine doesn't need fails E. |

**Verdict format** (verdict first, severity-ranked, no false balance):
```
ENGINE: <name>   INSTANCE: <A | B | C>   COMPONENTS: <per Phase 0>
VERDICT: NERS-compliant | non-compliant — <one-line reason>

N: pass/fail — <defect, severity, lesson/property>
R: pass/fail — <defect, severity, lesson/property>
S: pass/fail — <defect, severity, lesson/property>
E: pass/fail — <defect, severity, lesson/property>

REMEDIATION (worst-first):
  <severity> <finding> → Lesson <n> / P-<x>: <concrete fix>
```
**Output:** `ners_verdict_<engine>.md`. P1/P2/P3 canonical-gap findings append to `canon/editorial_ledger.jsonl` (commit gate; if blocked, stage inline and flag `[DRIFT]`).

---

## STAGE 4 — RE-TEST PROPOSED FIXES

Run Stage 1 Phases 1–6 on the **proposed fix**, not the original, to verify no new defect. Then re-run the **Stage 0 calibration** if the fix touched the skill's logic.

Common re-test failures (engine-aware):
- Lesson 3 fix (route bare-stat → B) → resolver params left at illustrative defaults without flagging them as Jordan's (fails R-claim honesty); or one resolver variable now carries two roles (Lesson 1).
- Lesson 6 fix (Ob-shift floor for sigma-leverage) → the saturation itself creates a new cliff at the floor (re-check monotonicity).
- Lesson 3 over-application → migrating a **healthy** dice engine to Mode B (fails N/E — over-correction).
- Continuity correction added → verify it does not shift already-validated 5–17D combat odds (should not, by construction; confirm).
- Instance-C engine "fixed" by forcing it into A/B → confirm the forced fit actually satisfies P-i…P-v rather than hiding the violation.

Iterate until clean or flag `[OPEN TRADE-OFF]`.

**Stage 4 output:** append `RE-TEST: <pass | new findings + revised remediation>` to `ners_verdict_<engine>.md`.

---

## GUARDRAILS

- **Rolling engines only.** No draw → out of scope; route to `valoria-mechanic-audit`. Do not verdict a character sheet, ledger, or bare clock.
- **Loops/cliffs/roles are in scope only where a rolling engine drives them.** Pure non-roll balance → mechanic-audit or a balance pass.
- **Never defend prior output.** Self/prior-session work → prepend `[SELF-AUTHORED — bias risk]`; surface the independent reviewer's criticism. Treat all work as external.
- **No false universals.** Every lesson is scoped. A linear clock, a multi-threshold tracker, a deliberate absolute effect, and a clamp boundary are NOT violations — check the Scope Gate and Phase 5 intent first.
- **Over-engineering is a defect.** Lessons 1 and 5 add structure; apply only where the failure is live (Phase 1b exposure). Migrating a healthy dice engine to Mode B is the canonical over-correction.
- **Engine parameters are Jordan's.** Mode-B BASE/SLOPE/CAP/offsets and the sigma tanh cap / `σ_N` constant are tuned; *form* is canonical (Decision E, ED-874), *numbers* are ratify/tune calls → `[OPEN — Jordan tuning]`, not a structural defect.
- **Goal over form.** Target the five properties on the correct engine — not a surface form.
- **Ground every claim.** Cite the canonical mechanism (file + section) for every mechanical value, loop, and intent; else flag `[UNGROUNDED]`. Do not assert from memory.
- **RuntimeError from any hook = hard halt.** Report verbatim, stop.

---

## WORKED EXAMPLE 1 — Faction Action Layer (Instance B; also the Stage-0 anchor)

*(Abbreviated; a real run produces full tables.)*

- **Phase 0:** scope gate — rolling engine present (Domain Action resolution). Components: (B) **deterministic+stochastic** Domain Actions (Assert, Suppress, Rebuttal) — **ratified ED-874**; recognize-and-exclude the CI economy / Treasury ledgers (deterministic-accounting → out of scope) and the CI/Mandate clocks (accumulators → out of scope). No raw-d10 leak post-ED-874.
- **Phase 1:** Instance-B stress = clamp edges (`M` near ±4) and the punching-up corner (stat 2 vs 7). Exposure: routine.
- **Phase 2:** graded four-degree ladder on pivotal outcomes; some irreversible-load-bearing (Suppress→Stab−1). Pre-resolver profile was (H,H,H); **under the resolver, Impact + Irreversibility are mitigated** (legible odds, 5% floor, 3% residual) — the (H,H,H) bare-dice finding is **closed by ED-874**.
- **Phase 3:** 3a leverage **flat 0.10/pt by construction** (P-ii satisfied). 3b clamp edges monotonic (`§6`: pass); no Ob-floor collision (margin-based, not Ob-shift — N/A). 3d Stability carries political-health AND collapse-trigger (a roll-input role conflation) → Lesson-1 candidate.
- **Phase 4:** loop through the resolver's output: resolved Suppress/Domain outcome → Stability → territory → muster → military → back into resolver inputs. **Loss-weighted probabilistic, not deterministic** (`engine_replacement_reconciled §6`); recovery odds raised, but terminal Stability-0 collapse is a bound-by-extinction, not a recovery cap → Lesson-5 finding (recovery path short of extinction).
- **Phase 5:** the resolver is **ratified** (ED-874) — intent confirmed. Open items are Jordan's: BASE/SLOPE values; full bare-stat migration vs Domain Actions only; §1.4 ↔ §1.3 (CC-4).
- **Stage 3:** **R/S/E for the resolved Domain Actions: PASS** (legible, uniform, ledger-consistent) — reversing the pre-resolver NON-COMPLIANT verdict (this reversal is exactly the Stage-0 calibration). **Residual:** Lesson-5 collapse-loop bound; Lesson-1 Stability split; param calibration + migration scope (`[OPEN — Jordan]`); §1.4↔CC-4.

## WORKED EXAMPLE 2 — Social Contest (Instance A; proves genericity off-faction)

*(Sketch — a real run reads the system doc from the working tree. System-specific values below are flagged `[verify: params/contest.md / social_contest_v30 — not read this session]`.)*

- **Phase 0:** scope gate — rolling engine present (the exchange roll). Components: (A) **sigma-leverage** exchange roll on a healthy pool `[verify ~5–18D]`; recognize-and-exclude the **Persuasion clock** (0–10 accumulator → out of scope as a resolver) and **Composure** (continuous resource feeding the roll → roll-input, not diagnosed). Engine-Selection Rule → A (pool ≥ ~5D, genuine setup/skill axis via stance/reading).
- **Phase 1:** Instance-A stress = the **bottom of the pool band** (a Rattled/Spent contestant dragged toward the 5D floor) and the **sub-5D continuity-correction** region if penalties push below 5D; NOT a faction-style bare-stat binary.
- **Phase 3:** 3a verify leverage (stance/positioning advantage) is in-band across the pool range — the same ED-875-class check (does a point of social setup move P uniformly at 5D and 16D?). 3c **continuity correction present?** — if the social roll can drop below 5D and resolves without `net − (Ob − 0.5)`, that is the finding (ER-2). 3b the Persuasion clock's thresholds are intended/spaced → not cliffs.
- **Phase 4:** if a social outcome feeds a loop (Composure damage → worse pool → worse outcome), check damper/cap; Composure floor + recovery is the candidate damper `[verify]`.
- **Stage 3 (expected):** likely **compliant** as a healthy Mode-A contest, with the one live caveat being **continuity-correction presence** at the low-pool edge — the same Robustness check as combat, demonstrating the pipeline runs identically on a non-faction engine.

This example exercises Instance A, the Scope Gate (clock + resource recognized-and-excluded), and the continuity-correction check — none faction-specific — proving the diagnostic is generic across rolling engines, not faction-fitted.

---

## INITIAL HYPOTHESES (untested — validate by running the pipeline)

Starting assessments, **not** pipeline-confirmed. Each needs a full Stage 0→4 run.

- **Faction Domain Actions (Instance B)** — likely **compliant** post-ED-874; residual: collapse-loop bound, Stability role split, Jordan's param/migration calls.
- **Social contest (Instance A)** — likely compliant; live check is continuity-correction presence at the low-pool edge (Worked Example 2).
- **Thread operations (Instance A)** — likely compliant; Coherence is a depleting continuous resource feeding the roll — verify in-band leverage + continuity correction; recognize-and-exclude Coherence-as-resource from the verdict.
- **Personal combat (Instance A)** — **gated**: the armature/resolution *structure* is Jordan's (handoff 2026-05-29 doc 2.5). Validate the **engine** (continuity correction, in-band leverage) separately from the **structure**.
- **Mass battle (Instance A, aggregated)** — pool aggregated/healthy; **watch ED-875** (low-Command leverage too hot, OPEN Gate G8).
- **Non-rolling systems** (CI economy, Treasury, peninsula/victory clocks, investigation five-filter, character sheet) — **out of scope**; route to `valoria-mechanic-audit`.
- **Continuity correction (ER-2)** — **LANDED 2026-06-22** in `params/core.md §Continuous Engine` (commit a3d3888).
- **Settlement resolver (ER-6)** — **unspecified**; specify deterministic-first to avoid importing the faction degeneracy.

---

## OPEN / JORDAN-DECISION POINTS

- `[OPEN — Jordan tuning]` Mode-B parameter values (BASE/SLOPE/FLOOR/CAP/offsets) — *form* ratified (ED-874), *numbers* illustrative.
- `[OPEN — Jordan scope]` Full bare-stat migration (Domain Actions + Suppress + Rebuttal + §1.4) vs Domain Actions only (`domain_action_resolver_spec.md §5`).
- `[OPEN — Gate G8, Jordan]` ED-875: mass-battle low-Command sigma-leverage too hot (~0.500/pt @ Cmd 2).
- `[OPEN — co-design]` §1.4 Accounting Stability Check ↔ §1.3 recovery (CC-4) — avoid double-counting.
- `[LANDED 2026-06-22]` Continuity correction `Ob − 0.5` in `params/core.md §Continuous Engine` (ER-2, commit a3d3888).
- `[OPEN — Jordan, gated]` Personal-combat resolution STRUCTURE (handoff 2026-05-29 doc 2.5) — must not be invented; build blocked until set.
- `[UNVERIFIED]` "omega" Class-A-new-system vetting framework — spec not read this session; NERS retained as the verdict.
- `[CALIBRATION DEPENDENCY]` Stage 0 assumes ED-876 (mass-battle cliff fix) and ED-884 (Ob-floor) as settled ground truth; if either reopens, recalibrate Stage 0.
- `[HOUSEKEEPING]` The deterministic+stochastic resolver lives as a ratified candidate spec under `designs/audit/2026-05-28-resolution-diagnostic/` + ED-874. Promote the ratified form into `params/core.md` (or a canonical resolution doc) so this skill's primary reference is canon, not an audit-dir file. (The property abstraction above reduces but does not remove this dependency.)
