---
name: resolution-diagnostic
description: >
  THE RESOLUTION DIAGNOSTIC — the Phase 0-6 stress test on anything in Valoria that resolves an
  outcome by a DRAW, run against the ONE engine: the sigma-leverage mu-shift layer
  (engine/autoload/sigma_leverage.py) atop the d10 substrate (engine/autoload/dice_engine.py),
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

Run this when the target resolves an outcome by a **draw**. It produces **stress points and property
violations against the one engine** — nothing else. It does not grade a design.

**Its findings are evidence for a NERS pass and are carried back to `ners`**, which owns the cut test
(N / E / R / S) and issues the verdict. `ners` calls this diagnostic **Instrument B**; if you were
invoked directly by a draw-shaped question, that is still what your output is. `ners` §1 routes here;
Phase 6 routes back. A target with no draw runs `ners` alone — that is a normal NERS pass, not an
out-of-scope one.

**Ground every claim at `file:line`, read from the working tree** (CLAUDE.md §2). Where a design
document and the code disagree, **the code is the mechanism and the prose is reference**
(CLAUDE.md §0.05): diagnose the code and record the disagreement as a defect in one of them.

> **THERE IS ONE ENGINE.** *"d10 everywhere, fractional, σ-leveraged"* — Jordan's ruling, carried at
> `systems/factions/sim/faction_action.py:126`. A **deterministic-odds / stochastic-resolution**
> resolver appears in older prose as though it were a second engine. It **has no implementation
> anywhere in `engine/` or `systems/`** — its constants (`BASE`, `SLOPE`, `OVW_OFFSET`,
> `PARTIAL_BAND`, `FAIL_FLOOR`) appear in no live module, and the faction layer it was written for
> resolves through σ-leverage on a fractional pool. Under CLAUDE.md §0.05 the code is the mechanism,
> so it is **not an engine to diagnose against**; a document describing it is reference, not a
> second design.

## §1 · THE STACK, AND ITS LIVE OWNERS

Substrate and advantage are separate modules. Diagnose them separately:

| layer | owner | what it does |
|---|---|---|
| **substrate** | `engine/autoload/dice_engine.py` | pool and degree primitive. `roll_pool` (discrete), `continuous_engine_sample` (fractional), `degree_from_net` (**the** ladder, single owner for every scale) |
| **advantage** | `engine/autoload/sigma_leverage.py` — `[CANONICAL]` | turns signed advantages in σ-units into a **μ-shift** on the roll. Stdlib plus `dice_engine`; no third-party dependency. Single-sources σ-leverage for **combat and social contest** — and for those two only |
| pinned by | `engine/tests/test_sigma_leverage_parity.py` + `engine/tests/goldens/sigma_leverage_parity.json` | the execution artifact. Read it before claiming behaviour |
| ⚠ **a second σ path** | `systems/mass_battle/sim/resolution.py` | **declared divergent** (J2: no `engine.*` dependency). It carries its own `_sigma_softcap`, `_sigma_net_boost` with a local `_SIG_PER_DIE`, `roll_pool_fractional`, and a local `compute_degree` with `_DEGREE_EPS`. The **ladder** half is guarded by `tests/valoria/test_degree_ladder_single_owner.py` — known, not yours to re-file. The **σ** half and the **pool floor** are guarded by nothing. Diagnose it; it is in scope |

⚠ **"One engine" is the ruling, not a description of the tree.** Mass battle is one of the three
subsystems ED-IN-0204 retained, and it runs the second path above. A diagnostic that reads only
`engine/autoload/` will report a single-owner engine and miss it.

**The API you are auditing against** — read it, do not restate it from memory:
`sigma_n(pool)` = `0.8·√max(1,pool)` · `soft_cap(σ)` = `M_MAX·tanh(σ/M_MAX)`, `M_MAX = 1.5` ·
`levels_to_net_sigma(agg, def)` · `net_boost(σ, pool)` · `p_success(base_ob, pool, net_sigma)` ·
`roll_net_continuous(pool)`.

## §2 · ⚠ ADVANTAGE IS A μ-SHIFT. IT IS NOT AN Ob REDUCTION.

This is the single most-drifted fact about this engine.

```
net_boost(σ, N) = soft_cap(σ) · σ_per_die · √N        # boosts the ROLL
p_success       = 1 − Φ( (base_Ob − (μ·N + net_boost)) / (σ_per_die·√N) )
```

**`base_Ob` and TN are never modified.** An `Eff_Ob = base_Ob − eff_σ·σ_N` form drives effective Ob
below 1, violating **PP-232** (*Ob minimum 1*) and making a `2·Ob` Overwhelming bar nonsensical at
negative Ob (ED-884). That form is retracted; recognising it is the point of this section.

**Two consequences that change what you look for:**

- **The `Ob ≥ 1` floor is unreachable by advantage, by construction.** "An Ob-shift collides with the
  PP-232 floor" is no longer a live hazard on this engine — do not go looking for it, and treat a
  document that describes advantage as an Ob reduction as **reference that has decayed**, not as a
  second design.
- **`eff_ob()` / `effective_ob()` are DISPLAY ONLY** and say so in their own docstrings. A caller that
  resolves on `eff_ob` instead of `p_success` has reintroduced the retracted form — **that** is the
  finding to look for.

**Uniform impact is exact — but exact INSIDE `p_success`, not everywhere.** `σ_per_die·√N` cancels
in the z-score, so `Δz = soft_cap(net_σ)` at every pool and every TN. **That cancellation depends on
the same pool reaching both terms.** `p_success` floors once and passes the floored pool into
`net_boost` and into its own denominator, so it cancels. A caller that boosts with `net_boost` — which
floors its own `√N` — while dividing by an **unfloored** pool does not: below 1D it gets
`Δz = soft_cap(σ)·√(1/pool)`, which at pool 0.25 is exactly **twice** the soft cap.

**Evaluate it against the module rather than reading it off this page:** import `net_boost` and
`soft_cap`, sweep a pool range at one `net_σ`, and check `net_boost(σ,N)/(σ_per_die·√N)` is constant
and equal to `soft_cap(σ)` — then check the same for the caller you are auditing, using **its** pool.

**Three bypasses to hunt for.** Advantage enters through `levels_to_net_sigma` → `net_boost`, or it
is a defect — and the defect wears three shapes:

1. **A flat bonus.** A `+X` to net or `−X` to Ob that is *not* σ_N-scaled gives
   `Δz = X/(0.8·√pool) ∝ 1/√pool` — hot at small pools, the exact non-uniformity this engine exists
   to kill, re-imported through a bonus.
2. **`capped=False`.** Both `net_boost(..., capped=False)` and `p_success(..., capped=False)` route
   through the right function and delete the soft cap: `eff = soft_cap(σ) if capped else σ`. A live
   resolver passing it has unbounded advantage — a **P-iii** finding, not a P-ii one. It is a
   legitimate axis in the parity goldens and in the frozen oracle; it is not legitimate on a game path.
3. **An inline re-derivation.** `soft_cap(σ) · sigma_n(pool)` computed at a call site is arithmetically
   `net_boost` and passes every scaling test — and is a **second owner of one operation**, which is
   an S *calculations consistent in methodology* defect. `systems/combat/combat_engine_v1/core.py`'s
   `resolve` is the live instance. Check for the formula, not only for the wrong answer.

## §3 · FRACTIONAL POOLS AND FRACTIONAL OBSTACLES

Both are canonical, and they are at different stages of reality. **Say which you are looking at.**

**Fractional POOL — live.** `continuous_engine_sample(pool: float)` and
`roll_net_continuous(pool: float)` take floats, and `faction_action.py:126` passes a fractional pool
straight through. `roll_pool` is the **discrete** path and keeps `int(round(pool))`, correctly — it
deals actual dice rather than sampling their limit distribution. A fractional pool routed to
`roll_pool` is a finding.

**Fractional Ob — RULED, and there is NO SINGLE OWNER for the derivation.** Jordan's ruling: an
obstacle rolled against a character or faction is *"their corresponding score/2 plus whatever
specific modifiers exist for them in that instance."* ⚠ **Do not repeat the claim that no call site
derives its Ob — `degree_from_net`'s docstring records that as false and names the counter-examples**
(`systems/factions/sim/crown_initiative.py::coronation_renewal_ob` implements `floor(L/2)+1`
exactly; Royal Progress derives from the standing gap; the tribunal derives under formal grounds).
**Read that docstring before writing anything about derived Ob.** What is true is narrower and is the
finding to carry: most sites still hand-set, the sites that do derive **disagree with each other**,
and no module owns the derivation — which is a *calculations consistent in methodology* defect, not a
missing feature.

What is live, and the check that shows it — **run these, do not cite them**:

| claim | how to check it |
|---|---|
| fractional Ob is **strictly monotonic** — no integer collapse | `p_success` at one pool for two obstacles a fraction apart must differ. At pool 9: Ob 1.4 → 0.8203, Ob 1.6 → 0.7977 |
| the degree ladder bands a fractional Ob correctly | `degree_from_net` on a fractional pair: net 1.9 / Ob 1.4 → margin +0.50 → **Partial** |
| the **whole-success-wide Partial window** (`0 ≤ margin < 1`) is what keeps Partial reachable | read the band in `degree_from_net`. Narrow the window to point-equality and Partial stops firing against a fractional Ob — which is why the width is the mechanism, not a rounding allowance |

## §4 · THE POOL FLOOR IS 1D — AND IT REACHES THE MEAN, NOT ONLY THE VARIANCE

**RULED (Jordan): "1D is floor."** Read it in the code — `sigma_leverage.py:276` and `:331`. The
`params/core.md §Pool Floor` tag those lines carry is the module's citation convention, not an
openable path: `engine/params/` is a dissolved tree (CLAUDE.md §3).

The floor is a game rule, and it must reach the **location** as well as the **spread**. Flooring
`√pool` in the denominator while leaving `μ·pool` unfloored is the shape to recognise: it agrees to
noise at every pool ≥ 1 and diverges by up to ~10 pp below 1D, so nothing above the floor can see it.

**What to check:**

- **A floor applied to one moment of a distribution and not the other hides above the floor.** No
  test, golden or campaign reaches it, because every pool ≥ 1 agrees; it is reachable only by
  evaluating below the floor. When you meet a clamp, ask **which terms it reaches** — not whether it
  exists.
- **`dice_engine.continuous_engine_sample` is the raw primitive and does NOT floor**, deliberately:
  it is the mathematical sampler, and the floor is a game rule its callers apply. **Re-grep the
  roster; do not trust this line.** At the last look it was reached from exactly two places —
  `sigma_leverage.roll_net_continuous` (which floors) and `tools/balance_oracle.py` inside
  `_pool_arm`, a patch that builds an experiment's two arms rather than a game path. `p_success`
  is **not** on that list: it is the closed form and never samples, though it floors separately.
  **A new caller reaching the primitive directly bypasses the floor** — that is the Phase 0 check,
  not a defect in the primitive.
- **There is NO single owner for the pool floor.** It is re-applied at each entry point —
  `sigma_n`, `net_boost`, `p_success`, `roll_net`, `roll_net_continuous`, `dice_engine.roll_pool` —
  and the literals differ (`max(1, …)` against `max(1.0, float(…))`) even where the values agree.
  A session that assumes the clamp is centralised will not look for the next site.
- **`roll_pool` is the discrete path and keeps `int(round(pool))`.** Whole dice are correct there; it
  deals actual dice rather than sampling their limit distribution. A fractional pool sent to
  `roll_pool` is a P-v finding.

## §5 · THE FIVE PROPERTIES, ON THIS ENGINE

| # | property | what failing looks like HERE |
|---|---|---|
| **P-i** | **Legible odds** | the player cannot read their chance; advantage surfaced only as an opaque roll modifier rather than a named level (minor/moderate/strong/major) |
| **P-ii** | **Uniform leverage** | exact inside `p_success` because the pool is floored before it reaches `net_boost` (§4) — never "by construction" in general. A failure means a **caller bypassed `net_boost`** (§2's three shapes) **or** boosted correctly while scaling z by an unfloored pool. Check both |
| **P-iii** | **Bounded, monotonic** | resolving on `eff_ob` (display) instead of `p_success`; a discrete boundary jumping a continuous input; a clamp that reaches one moment of the distribution and not the other (§4) |
| **P-iv** | **Graded, recoverable** | a bare binary on an irreversible outcome where `degree_from_net` was available; a Partial band collapsed to point-equality against a fractional Ob |
| **P-v** | **Right engine** | anything resolving by a bespoke draw instead of this stack; a fractional pool sent to `roll_pool`; a second degree ladder |

## §6 · PHASES

| phase | do |
|---|---|
| **0** | Draw present? Decompose. Every rolled component routes to `dice_engine` + `sigma_leverage`; anything else is a P-v finding. Flag bare-pool-vs-flat-Ob leftovers |
| **1** | Locate the stress point — the **low-pool end** (and the floor itself, §4), the **soft-cap saturation** region (`net_σ` well past `M_MAX = 1.5`), and any fractional-Ob call site. **1b:** how often is it reached? A fractional pool is routine; a sub-1D pool is not — yet |
| **2** | What does it decide? Outcome type · stakes & reversibility · impact, exposure and irreversibility. **This phase is judgment, not a rubric** — there is no H/M/L scale here and inventing one would be a number with no control. Say what the draw decides and how badly a wrong answer lands, in words, and carry that to `ners` unscored |
| **3** | **3a** advantage enters via `levels_to_net_sigma`→`net_boost` and none of §2's three bypasses · **3b** nothing resolves on `eff_ob` · **3c** the fractional-pool and fractional-Ob paths agree with the closed form — **run them; do not read them off §3** · **3d** role conflation on a variable feeding or reading the roll · **3e** advantage reaches the player as a **named level** (minor/moderate/strong/major), not a bare σ float — this is the only phase that can see **P-i** · **3f** an irreversible outcome returns the owner's four bands, not a bare pass/fail — the only phase that can see **P-iv** |
| **4** | Loops running through the engine's output or gating its input, cross-scale included. Defect = **both undamped and unbounded**. A **damper** is anything that shrinks the loop's gain per pass; a **cap** is a hard bound on the accumulated value. They are two separate checks, and one without the other is not a defect |
| **5** | **Intent gate.** Deliberate + adequate safeguard → pass. Deliberate without → finding. Accidental or undetermined → finding, `[INTENT UNDETERMINED]`. Do not guess |
| **6** | Score and triage, worst first, then **carry the findings back to `ners`** — they enter its ledger as evidence and do not short-circuit it. The table below says which axis each one lands on |

**Where a finding lands in the NERS pass.** The five properties do not map onto one axis, and posting
them all to R-COMPLETE loses two of them:

| property | lands on (in `ners`) | because |
|---|---|---|
| **P-i** legible odds | **E-LEGIBILITY** | the player cannot intuit the outcome from the choice |
| **P-ii** uniform leverage · **P-v** right engine | **S — calculations consistent in methodology** | a bypass or a bespoke draw is a *second convention for one quantity*, which is the S test verbatim |
| **P-iii** bounded, monotonic · **P-iv** graded, recoverable | **R-COMPLETE** | it breaks at its extremes, or a branch is unwritten |

Carry three things with each finding: the **property name**, the **`file:line`** it was found at,
and either **the call that reproduces its number** or the words **"by construction, algebra shown"**.
`ners` §6.2 refuses a number with no control, so a finding that arrives without one cannot be banked.
A property that produced no finding is reported as a **named attack that failed**, not as silence.

## §7 · WHAT IS NOT A DEFECT ON THIS ENGINE

- **The level values** (minor 0.25 / moderate 0.50 / strong 0.75 / major 1.00) are **Class B draft
  sim-seeds, explicitly NOT canonical** and sim-tunable. A level number you disagree with is
  `[OPEN — Jordan tuning]`, not a structural finding. Same for `M_MAX = 1.5`.
- **Soft-cap saturation is the design**, not a cliff: `M·tanh(net/M)` has no hard ceiling and no
  dead-zone. Check it is smooth, not that it is absent.
- **TN never varies**, and the three layers refuse differently — write the falsifier for the layer
  you are on. `sigma_leverage` raises `KeyError` (one-key `PER_DIE`); `dice_engine` raises
  `ValueError` (`_require_tn7`); `systems/mass_battle/sim/resolution.py` uses a bare `assert`, which
  `python -O` strips. A mechanism that wants a varying difficulty wants an **Ob**.
  (ED-IN-0196: *"TN7 always. Never change TN anywhere ever."*)
- **`systems/combat/combat_engine_v1/core.py`'s second, `2·Ob`-keyed ladder** is a **declared HELD**
  exception guarded by `tests/valoria/test_degree_ladder_single_owner.py`. Known, tracked, **not yours
  to re-file** — though it is a live instance of the charter's *calculations consistent in
  methodology* (S) defect, and worth naming as such rather than as news.

## §8 · GUARDRAILS

> **The pass discipline is owned by `ners` §11 and binds this diagnostic unchanged** — a named failed
> attack licenses a pass, withholding is symmetric, never manufacture and never sham-clear, never
> defend prior output, a repair that adds a system has failed. Read them there. Restating them here
> would make a second owner of rules `CLAUDE.md` §0.06 already assigns to one file.

Only the two carve-outs that are specific to a **draw** live here:

- **Parameters are Jordan's.** The level values, `M_MAX`, the soft cap and any other tuned number are
  `[OPEN — Jordan tuning]`, never a structural defect (§7). The *form* is this diagnostic's business;
  the *values* are not.
- **No false universals about an engine.** A linear clock is not a cliff; a multi-threshold tracker is
  not a violation; soft-cap saturation is the design, not a ceiling; a deliberate absolute effect with
  an adequate safeguard is not a finding. Run the intent gate (Phase 5) first, and do not guess intent
  — `[INTENT UNDETERMINED]` is the honest tag.
