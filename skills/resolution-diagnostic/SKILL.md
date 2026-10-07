---
name: resolution-diagnostic
description: >
  THE RESOLUTION DIAGNOSTIC — the Phase 0-6 stress test on anything in Valoria that resolves an
  outcome by a DRAW, run against the ONE engine: the sigma-leverage mu-shift layer
  (engine/dice_engine/sigma_leverage.py) atop the d10 substrate (engine/dice_engine/dice_engine.py),
  with FRACTIONAL dice pools and FRACTIONAL obstacles. Five properties — legible odds, uniform
  leverage, bounded and monotonic response, graded and recoverable output, right engine for the
  pool regime. Its output is EVIDENCE, NOT A VERDICT: findings return to the `ners` skill, which
  owns the cut test that grades them. The single most-drifted fact it exists to protect:
  advantage is a mu-SHIFT on the roll and never an Ob reduction — base_Ob and TN are never
  modified, so a caller resolving on eff_ob has reintroduced a retracted form.
  ALWAYS use for: "engine audit", "resolution audit", "resolution diagnostic audit",
  "diagnose this resolver", "stress test this roll", "sigma leverage", "mu-shift vs Ob-shift",
  "leverage non-uniformity", "fractional pool", "fractional obstacle", "sub-1D pool",
  "soft cap saturation", "is this the right engine for this pool". Do NOT use on a design object
  that does not resolve by a draw — that is `ners` alone; or for internal-consistency checks with
  no draw (formula gaps, redundancy) — that is valoria-mechanic-audit.
---

# RESOLUTION DIAGNOSTIC — the σ-leverage engine

## WHAT THIS IS, AND WHERE ITS OUTPUT GOES

Run when the target resolves an outcome by a **draw**. Output: stress points and property
violations against the one engine — **evidence, never a verdict**. `ners` calls this
**Instrument B** and routes here from its §1; Phase 6 carries the findings back to its cut test.

**Ground every claim at `file:line` in the working tree.** Where a document and the code
disagree, diagnose the code and record the disagreement as a defect (CLAUDE.md §0.05).

> **THERE IS ONE ENGINE:** *"d10 everywhere, fractional, σ-leveraged"*
> (`systems/factions/sim/faction_action.py:126`). The deterministic-odds / stochastic-resolution
> resolver of older prose (`BASE`, `SLOPE`, `OVW_OFFSET`, `PARTIAL_BAND`, `FAIL_FLOOR`) is
> implemented nowhere in `engine/` or `systems/`. Never diagnose against it.

## §1 · THE STACK, AND ITS LIVE OWNERS

Diagnose substrate and advantage separately:

| layer | owner | what it does |
|---|---|---|
| **substrate** | `engine/dice_engine/dice_engine.py` | `roll_pool` (discrete), `continuous_engine_sample` (fractional), `degree_from_net` (**the** ladder, single owner for every scale) |
| **advantage** | `engine/dice_engine/sigma_leverage.py` — `[CANONICAL]` | turns signed σ-unit advantages into a **μ-shift** on the roll; single-sources σ-leverage for **combat and social contest only** |
| pinned by | `engine/tests/test_sigma_leverage_parity.py` + `engine/tests/goldens/sigma_leverage_parity.json` | the execution artifact. Read it before claiming behaviour |
| ⚠ **a second σ path** | `systems/mass_battle/sim/resolution.py` | **declared divergent** (no `engine.*` dependency): own `_sigma_softcap`, `_sigma_net_boost` with a local `_SIG_PER_DIE`, `roll_pool_fractional`, local `compute_degree` with `_DEGREE_EPS`. Ladder half guarded by `tests/valoria/test_degree_ladder_single_owner.py` — do not re-file. σ half and pool floor unguarded. **In scope: reading only `engine/dice_engine/` misses it** |

**The API you are auditing against** — read it, do not restate it from memory:
`sigma_n(pool)` = `0.8·√max(1,pool)` · `soft_cap(σ)` = `M_MAX·tanh(σ/M_MAX)`, `M_MAX = 1.5` ·
`levels_to_net_sigma(agg, def)` · `net_boost(σ, pool)` · `p_success(base_ob, pool, net_sigma)` ·
`roll_net_continuous(pool)`.

## §2 · ⚠ ADVANTAGE IS A μ-SHIFT. IT IS NOT AN Ob REDUCTION.

```
net_boost(σ, N) = soft_cap(σ) · σ_per_die · √N        # boosts the ROLL
p_success       = 1 − Φ( (base_Ob − (μ·N + net_boost)) / (σ_per_die·√N) )
```

**`base_Ob` and TN are never modified**, so advantage cannot reach the `Ob ≥ 1` floor: a PP-232
collision is not a live hazard here — do not hunt for it. The retracted form
`Eff_Ob = base_Ob − eff_σ·σ_N` drives Ob below 1 (**PP-232**, *Ob minimum 1*) and breaks the
`2·Ob` Overwhelming bar (ED-884). A document describing advantage as an Ob reduction is decayed
reference: record it, never diagnose against it. **`eff_ob()` / `effective_ob()` are DISPLAY
ONLY:** a caller resolving on `eff_ob` instead of `p_success` has reintroduced the retracted form.

**Uniform impact is exact inside `p_success`, not everywhere.** `σ_per_die·√N` cancels in the
z-score, giving `Δz = soft_cap(net_σ)` at every pool and TN, only if the same pool reaches both
terms. `p_success` passes one floored pool to `net_boost` and its denominator. A caller using
`net_boost` (floored `√N`) over an **unfloored** denominator gets `Δz = soft_cap(σ)·√(1/pool)`
below 1D — **twice** the soft cap at 0.25. **Evaluate it:** sweep pools at one `net_σ`, check
`net_boost(σ,N)/(σ_per_die·√N)` is constant and equals `soft_cap(σ)`; repeat with the caller's
pool.

**Three bypasses** — advantage not entering via `levels_to_net_sigma` → `net_boost` is a defect:

1. **A flat bonus.** A `+X` to net or `−X` to Ob not σ_N-scaled gives
   `Δz = X/(0.8·√pool) ∝ 1/√pool` — hot at small pools.
2. **`capped=False`** on `net_boost` or `p_success` deletes the soft cap
   (`eff = soft_cap(σ) if capped else σ`). On a game path: unbounded advantage, a **P-iii**
   finding, not a P-ii one. Legitimate only in the parity goldens and the frozen oracle.
3. **An inline re-derivation.** `soft_cap(σ) · sigma_n(pool)` at a call site passes every scaling
   test and is a **second owner of one operation** — an S *calculations consistent in
   methodology* defect. Live instance: `systems/combat/combat_engine_v1/core.py`'s `resolve`.
   Check for the formula, not only the answer.

## §3 · FRACTIONAL POOLS AND FRACTIONAL OBSTACLES

Both are canonical, at different stages. **Say which you are looking at.**

**Fractional POOL — live.** `continuous_engine_sample(pool: float)` and
`roll_net_continuous(pool: float)` take floats; `faction_action.py:126` passes a fractional pool
straight through. `roll_pool` is the **discrete** path and keeps `int(round(pool))`, correctly. A
fractional pool routed to `roll_pool` is a **P-v** finding.

**Fractional Ob — no single owner for the derivation.** An obstacle rolled against a character or
faction is *"their corresponding score/2 plus whatever specific modifiers exist for them in that
instance."* ⚠ **Do not claim no call site derives its Ob:** `degree_from_net`'s docstring names
counter-examples, e.g. `systems/factions/sim/crown_initiative.py::coronation_renewal_ob`
(`floor(L/2)+1`). Read that docstring before writing anything about derived Ob. The finding: most
sites still hand-set, deriving sites **disagree with each other**, and no module owns the
derivation — an S *calculations consistent in methodology* defect, not a missing feature.

**Run these, do not cite them:**

| claim | how to check it |
|---|---|
| fractional Ob is **strictly monotonic** — no integer collapse | `p_success(1.4, 9, 0.0)` → 0.8203 against `p_success(1.6, 9, 0.0)` → 0.7977. Two obstacles a fraction apart must differ |
| the degree ladder bands a fractional Ob correctly | `degree_from_net(1.9, 1.4)` → margin +0.50 → **Partial** |
| the **whole-success-wide Partial window** (`0 ≤ margin < 1`) keeps Partial reachable | read the band in `degree_from_net`. Narrowed to point-equality, Partial stops firing against a fractional Ob |

## §4 · THE POOL FLOOR IS 1D — AND IT REACHES THE MEAN, NOT ONLY THE VARIANCE

**1D is the floor:** `sigma_leverage.py:276` and `:331`. Their `params/core.md §Pool Floor` tag is
a citation convention, not an openable path (`engine/params/` is dissolved).

The floor must reach the **location** as well as the **spread**. Flooring `√pool` while leaving
`μ·pool` unfloored agrees to noise at pool ≥ 1 and diverges by up to ~10 pp below 1D: only
evaluating below the floor sees it. **When you meet a clamp, ask which terms it reaches.**

- **`dice_engine.continuous_engine_sample` does NOT floor**; its callers do. **Re-grep them.** Last
  seen: `sigma_leverage.roll_net_continuous` (floors) and `tools/balance_oracle.py` inside
  `_pool_arm` (an experiment arm, not a game path). `p_success` never samples; it floors itself.
  A new direct caller bypasses the floor — a Phase 0 finding, not a defect in the primitive.
- **No single owner for the pool floor:** re-applied at `sigma_n`, `net_boost`, `p_success`,
  `roll_net`, `roll_net_continuous` and `dice_engine.roll_pool`, with differing literals
  (`max(1, …)` against `max(1.0, float(…))`). Check every entry point.

## §5 · THE FIVE PROPERTIES, ON THIS ENGINE

| # | property | what failing looks like HERE |
|---|---|---|
| **P-i** | **Legible odds** | the player cannot read their chance; advantage surfaced only as an opaque roll modifier rather than a named level (minor/moderate/strong/major) |
| **P-ii** | **Uniform leverage** | exact inside `p_success` because the pool is floored before `net_boost` (§4) — never "by construction" in general. Failure: a **caller bypassed `net_boost`** (§2's shapes 1 and 3) **or** boosted correctly while scaling z by an unfloored pool (§2). Check both |
| **P-iii** | **Bounded, monotonic** | resolving on `eff_ob` (display) instead of `p_success`; a discrete boundary jumping a continuous input; a clamp that reaches one moment of the distribution and not the other (§4) |
| **P-iv** | **Graded, recoverable** | a bare binary on an irreversible outcome where `degree_from_net` was available; a Partial band collapsed to point-equality against a fractional Ob |
| **P-v** | **Right engine** | anything resolving by a bespoke draw instead of this stack; a fractional pool sent to `roll_pool`; a second degree ladder |

## §6 · PHASES

| phase | do |
|---|---|
| **0** | Draw present? Decompose. Every rolled component routes to `dice_engine` + `sigma_leverage`; anything else is a P-v finding. Flag bare-pool-vs-flat-Ob leftovers |
| **1** | Locate the stress point — the **low-pool end** (and the floor, §4), the **soft-cap saturation** region (`net_σ` well past `M_MAX = 1.5`), any fractional-Ob call site. **1b:** how often is it reached? A fractional pool is routine; a sub-1D pool is not — yet |
| **2** | What does it decide? Outcome type · stakes & reversibility · impact, exposure and irreversibility. **Judgment, not a rubric** — no H/M/L scale. Say in words what the draw decides and how badly a wrong answer lands; carry it to `ners` unscored |
| **3** | **3a** advantage enters via `levels_to_net_sigma`→`net_boost`, none of §2's three bypasses · **3b** nothing resolves on `eff_ob` · **3c** the fractional-pool and fractional-Ob paths agree with the closed form — **run them** · **3d** role conflation on a variable feeding or reading the roll · **3e** advantage reaches the player as a **named level**, not a bare σ float — the only phase that sees **P-i** · **3f** an irreversible outcome returns the owner's four bands, not a bare pass/fail — the only phase that sees **P-iv** |
| **4** | Loops running through the engine's output or gating its input, cross-scale included. Defect = **both undamped and unbounded**. A **damper** shrinks the loop's gain per pass; a **cap** hard-bounds the accumulated value. Two separate checks; one without the other is not a defect |
| **5** | **Intent gate.** Deliberate + adequate safeguard → pass. Deliberate without → finding. Accidental or undetermined → finding, `[INTENT UNDETERMINED]`. Do not guess |
| **6** | Order findings worst-first — by how much their absence changes the game, not a score — then **carry them back to `ners`** as evidence; they do not short-circuit it. Axis per the table below |

**Where a finding lands in the NERS pass:**

| property | lands on (in `ners`) | because |
|---|---|---|
| **P-i** legible odds | **E-LEGIBILITY** | the player cannot intuit the outcome from the choice |
| **P-ii** uniform leverage · **P-v** right engine | **S — calculations consistent in methodology** | a bypass or a bespoke draw is a *second convention for one quantity* |
| **P-iii** bounded, monotonic · **P-iv** graded, recoverable | **R-COMPLETE** | it breaks at its extremes, or a branch is unwritten |

Each finding carries the **property name**, the **`file:line`**, and **the call that reproduces
its number** or **"by construction, algebra shown"**; a finding without one cannot be banked
(`ners` §6.2). An `[INTENT UNDETERMINED]`
finding keeps its axis, the tag in the row's *what would overturn it* cell — never a downgrade.
A property with no finding is reported as a **named attack that failed**, not as silence.

## §7 · WHAT IS NOT A DEFECT ON THIS ENGINE

- **Tuned values are Jordan's.** The levels (minor 0.25 / moderate 0.50 / strong 0.75 / major
  1.00) are **Class B draft sim-seeds, NOT canonical**. They, `M_MAX = 1.5` and the soft cap are
  `[OPEN — Jordan tuning]`, never a structural defect. The *form* is this diagnostic's business.
- **Soft-cap saturation is the design:** `M·tanh(net/M)` has no hard ceiling and no dead-zone.
  Check it is smooth, not that it is absent.
- **TN never varies**; a mechanism wanting varying difficulty wants an **Ob**. Falsifier per layer:
  `sigma_leverage` raises `KeyError` (one-key `PER_DIE`); `dice_engine` raises `ValueError`
  (`_require_tn7`); `systems/mass_battle/sim/resolution.py` uses a bare `assert`, stripped by
  `python -O`.
- **`systems/combat/combat_engine_v1/core.py`'s second, `2·Ob`-keyed ladder** is a declared HELD
  exception (`tests/valoria/test_degree_ladder_single_owner.py`): name it as a live S instance; do
  not re-file it.

## §8 · GUARDRAILS

The pass discipline is `ners` §11's and binds here unchanged. Carve-outs specific to a draw:
tuned values (§7), and:

- **No false universals.** A linear clock is not a cliff; a multi-threshold tracker is not a
  violation; a deliberate absolute effect with an adequate safeguard is not a finding (Phase 5).
