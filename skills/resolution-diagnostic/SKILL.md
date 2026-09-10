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
(N / E / R / S) and issues the verdict. `ners` §1 routes here; Phase 6 routes back. A target with no
draw runs `ners` alone — that is a normal NERS pass, not an incomplete one.

**Ground every claim at `file:line`, read from the working tree** (CLAUDE.md §2). Where a design
document and the code disagree, **the code is the mechanism and the prose is reference**
(CLAUDE.md §0.05): diagnose the code and record the disagreement as a defect in one of them.

> **THERE IS ONE ENGINE.** *"d10 everywhere, fractional, σ-leveraged"* — Jordan, 2026-08-14, cited at
> `systems/factions/sim/faction_action.py:126`. The **deterministic-odds / stochastic-resolution**
> resolver that this file used to carry as a co-equal "Instance B" **has no implementation anywhere in
> `engine/` or `systems/`** — its constants (`BASE`, `SLOPE`, `OVW_OFFSET`, `PARTIAL_BAND`,
> `FAIL_FLOOR`) appear in no live module, its spec is at the fork, and the faction layer it was
> written for now resolves through σ-leverage on a fractional pool. Under CLAUDE.md §0.05 the code is
> the mechanism, so it is **dead canon** and is not an engine to diagnose against.

### §1 The stack, and its live owners

Two layers, deliberately separated (D0-2) — diagnose them separately:

| layer | owner | what it does |
|---|---|---|
| **substrate** | `engine/autoload/dice_engine.py` | pool and degree primitive. `roll_pool` (discrete), `continuous_engine_sample` (fractional), `degree_from_net` (**the** ladder, single owner for every scale) |
| **advantage** | `engine/autoload/sigma_leverage.py` — `[CANONICAL — Stage 1a port 2026-06-30]` | turns signed advantages in σ-units into a **μ-shift** on the roll. Stdlib only. Single-sources σ-leverage for **combat and social contest both** |
| pinned by | `engine/tests/test_sigma_leverage_parity.py` + `engine/tests/goldens/sigma_leverage_parity.json` | the execution artifact. Read it before claiming behaviour |

**The API you are auditing against** — read it, do not restate it from memory:
`sigma_n(pool)` = `0.8·√max(1,pool)` · `soft_cap(σ)` = `M_MAX·tanh(σ/M_MAX)`, `M_MAX = 1.5` ·
`levels_to_net_sigma(agg, def)` · `net_boost(σ, pool)` · `p_success(base_ob, pool, net_sigma)` ·
`roll_net_continuous(pool)`.

### §2 ⚠ ADVANTAGE IS A μ-SHIFT. IT IS NOT AN Ob REDUCTION.

This is the single most-drifted fact about this engine, and the previous revision of this file taught
the retracted form.

```
net_boost(σ, N) = soft_cap(σ) · σ_per_die · √N        # boosts the ROLL
p_success       = 1 − Φ( (base_Ob − (μ·N + net_boost)) / (σ_per_die·√N) )
```

**`base_Ob` and TN are never modified.** The earlier `Eff_Ob = base_Ob − eff_σ·σ_N` form drove
effective Ob below 1, violating **P-232** (*Ob minimum 1*) and making the old `2·Ob` Overwhelming bar
nonsensical at negative Ob. That was **F1, resolved by ED-884** with this reformulation.

**Two consequences that change what you look for:**

- **The `Ob ≥ 1` floor is unreachable by advantage, by construction.** "An Ob-shift collides with the
  P-232 floor" is no longer a live hazard on this engine — do not go looking for it, and treat a
  document that describes advantage as an Ob reduction as **stale**, not as a second design.
- **`eff_ob()` / `effective_ob()` are DISPLAY ONLY** and say so in their own docstrings. A caller that
  resolves on `eff_ob` instead of `p_success` has reintroduced the retracted form — **that** is the
  finding to look for.

**Uniform impact is exact, not approximate, and it is worth verifying rather than assuming.**
`σ_per_die·√N` cancels in the z-score, so `Δz = soft_cap(net_σ)` at *every* pool size and every TN.
Measured 2026-09-04, re-verified 2026-09-10, across pool ∈ {0.5, 1, 4, 9, 16, 25} at
`net_σ = 1.0`: **Δz = 0.874174 at all
six**, equal to `soft_cap(1.0)` to six decimals. P-ii holds **by construction here**, so a
P-ii finding on this engine means a caller bypassed `net_boost`, not that the engine drifted.

**The bypass to hunt for:** a flat `+X` to net or `−X` to Ob that is *not* σ_N-scaled gives
`Δz = X/(0.8·√pool) ∝ 1/√pool` — hot at small pools, the exact non-uniformity this engine exists to
kill, re-imported through a bonus. Advantage enters through `levels_to_net_sigma` → `net_boost`, or
it is a defect.

### §3 Fractional pools and fractional obstacles

Both are canonical, and they are at different stages of reality. **Say which you are looking at.**

**Fractional POOL — live.** `continuous_engine_sample(pool: float)` and
`roll_net_continuous(pool: float)` take floats; `faction_action.py` already passes 4.3, 4.6, 4.9, 5.3.
`roll_pool` is the **discrete** path and keeps `int(round(pool))`, correctly — it deals actual dice
rather than sampling their limit distribution. A fractional pool routed to `roll_pool` is a finding.

**Fractional Ob — RULED, and the derivation is IMPLEMENTED NOWHERE.** Jordan ruled 2026-08-14 that an
obstacle rolled against a character or faction is *"their corresponding score/2 plus whatever specific
modifiers exist for them in that instance."* **Every call site in the tree still passes a hand-set
Ob.** `degree_from_net`'s own docstring flags this, and the distinction matters more here than
anywhere, because this is the function a reader consults to learn what an obstacle *is*. Treat "Ob is
derived" as **a ruling awaiting execution**, never as an accomplished fact.

What *is* live and verified (measured 2026-09-04, re-verified 2026-09-10):

| claim | verified |
|---|---|
| fractional Ob is **strictly monotonic** — no integer collapse | ✅ pool 9: Ob 1.4 → 0.8203, Ob 1.6 → 0.7977. `Ob 1.4 ≢ 1.6` |
| the degree ladder bands a fractional Ob correctly | ✅ net 1.9 / Ob 1.4 → margin +0.50 → **Partial** |
| the **whole-success-wide Partial window** (`0 ≤ margin < 1`) is what keeps Partial reachable | ✅ on point-equality (`margin == 0`) Partial would essentially never fire against a fractional Ob |

### §4 The pool floor is 1D, and it applies to the MEAN as well as the VARIANCE

**RULED 2026-09-04 (Jordan): "1D is floor."** `params/core.md §Pool Floor (all systems)`.

This is worth stating in a diagnostic because the engine got it wrong in a way that only fractional
pools could expose. `p_success` floored the **spread** and not the **location**:

```
was:   shifted_mean = mu * pool                        # NOT floored
       z = (ob - mean) / (sigma * sqrt(max(1, pool)))  # floored
now:   effective_pool = max(1.0, float(pool))          # floor once, use everywhere
```

while `roll_net_continuous` — the sampler the game actually draws from — floored both. **Two
flooring conventions in one module**, disagreeing by up to ~10 pp below 1D:

| pool | before: `p_success` vs sampled | after |
|---|---|---|
| 0.25 | 0.1303 vs 0.2275 — **9.7 pp** | 0.2266 vs 0.2275 — noise |
| 0.50 | 0.1587 vs 0.2275 — **6.9 pp** | 0.2266 vs 0.2275 — noise |
| 1.00 | 0.2266 vs 0.2275 — noise | unchanged |

**Fixed** in `engine/autoload/sigma_leverage.py::p_success` and, byte-identically, in the
`m1_dice_sigma_core` seed the parity goldens are generated from. **The control:** no golden row
carries a sub-1D pool (`p_success` pools are 1/5/10/26) and `max(1.0, pool) == pool` for all of
them, so the change is **value-identical at and above 1D** — 901 parity assertions pass against
**byte-unchanged** goldens.

**What this leaves for a diagnostic to check, which is the reusable part:**

- **A floor applied to one moment of a distribution and not the other is a defect that hides above
  the floor.** Every pool ≥ 1 agreed to noise, so no test, golden or campaign could see it; it was
  reachable only by evaluating below the floor. When you meet a clamp, ask **which terms it reaches**
  — not whether it exists.
- **`dice_engine.continuous_engine_sample` is the raw primitive and does NOT floor**, deliberately:
  it is the mathematical sampler, and the floor is a game rule its callers apply
  (`roll_net_continuous`, `p_success`, and `tools/balance_oracle.py` all do). That is fine while
  every caller floors — **a new caller reaching the primitive directly bypasses the floor**, and
  that is the thing to check at Phase 0, not a defect in the primitive.
- **`roll_pool` is the discrete path and keeps `int(round(pool))`.** Whole dice are correct there; it
  deals actual dice rather than sampling their limit distribution. A fractional pool sent to
  `roll_pool` is a P-v finding.

### §5 The five properties, on this engine

| # | property | what failing looks like HERE |
|---|---|---|
| **P-i** | **Legible odds** | the player cannot read their chance; advantage surfaced only as an opaque roll modifier rather than a named level (minor/moderate/strong/major) |
| **P-ii** | **Uniform leverage** | exact by construction — so a failure means a **caller bypassed `net_boost`** with a flat bonus (§2), not engine drift |
| **P-iii** | **Bounded, monotonic** | resolving on `eff_ob` (display) instead of `p_success`; a discrete boundary jumping a continuous input; a clamp that reaches one moment of the distribution and not the other (§4) |
| **P-iv** | **Graded, recoverable** | a bare binary on an irreversible outcome where `degree_from_net` was available; a Partial band collapsed to point-equality against a fractional Ob |
| **P-v** | **Right engine** | anything resolving by a bespoke draw instead of this stack; a fractional pool sent to `roll_pool`; a second degree ladder |

### §6 Phases

| phase | do |
|---|---|
| **0** | Draw present? Decompose. Every rolled component routes to `dice_engine` + `sigma_leverage`; anything else is a P-v finding. Flag bare-pool-vs-flat-Ob leftovers |
| **1** | Locate the stress point — the **low-pool end** (and the floor itself, §4), the **soft-cap saturation** region (`net_σ` well past `M_MAX = 1.5`), and any fractional-Ob call site. **1b:** how often is it reached? A fractional pool is routine; a sub-1D pool is not — yet |
| **2** | What does it decide? Outcome type · stakes & reversibility · (impact, exposure, irreversibility) each H/M/L against numbers. Two H = candidate finding |
| **3** | **3a** advantage enters via `levels_to_net_sigma`→`net_boost`, not a flat bonus · **3b** nothing resolves on `eff_ob` · **3c** the fractional-pool and fractional-Ob paths agree with the closed form · **3d** role conflation on a variable feeding or reading the roll |
| **4** | Loops running through the engine's output or gating its input, cross-scale included. Defect = **both undamped and unbounded** — damper and cap are two separate checks |
| **5** | **Intent gate.** Deliberate + adequate safeguard → pass. Deliberate without → finding. Accidental or undetermined → finding, `[INTENT UNDETERMINED]`. Do not guess |
| **6** | Score and triage, worst first. **Carry the findings back to `ners`** — they enter its ledger (§2–§9 there) as evidence and do not short-circuit it |

### §7 What is NOT a defect on this engine

- **The level values** (minor 0.25 / moderate 0.50 / strong 0.75 / major 1.00) are **Class B draft
  sim-seeds, explicitly NOT canonical** and sim-tunable. A level number you disagree with is
  `[OPEN — Jordan tuning]`, not a structural finding. Same for `M_MAX = 1.5`.
- **Soft-cap saturation is the design**, not a cliff: `M·tanh(net/M)` has no hard ceiling and no
  dead-zone. Check it is smooth, not that it is absent.
- **TN never varies.** `PER_DIE` is a one-key dict so a stray TN raises `KeyError` **loudly** rather
  than silently resolving as TN 6 or 8. A mechanism that wants a varying difficulty wants an **Ob**.
  (ED-IN-0196: *"TN7 always. Never change TN anywhere ever."*)
- **`systems/combat/combat_engine_v1/core.py`'s second, `2·Ob`-keyed ladder** is a **declared HELD**
  exception guarded by `tests/valoria/test_degree_ladder_single_owner.py`. Known, tracked, **not yours
  to re-file** — though it is a live instance of the charter's *calculations consistent in
  methodology* (S) defect, and worth naming as such rather than as news.

## §8 · GUARDRAILS

- **This diagnostic produces edits and evidence, not documents.** No `audit/` directory, no verdict
  file, no ledger append that does not require a human decision (CLAUDE.md §0). The verdict is
  `ners`'s to issue; a finding that needs no ruling is fixed in this commit or dropped.
- **Parameters are Jordan's.** The level values, `M_MAX`, and any tuned number are
  `[OPEN — Jordan tuning]`, not a structural defect (§7). The *form* is this diagnostic's business;
  the *values* are not.
- **No false universals.** A linear clock is not a cliff; a multi-threshold tracker is not a
  violation; a deliberate absolute effect with an adequate safeguard is not a finding. Run the
  intent gate (Phase 5) before flagging, and do not guess intent.
- **A repair that adds a system has failed.** Prefer the deletion. A guard is minted only where the
  defective artifact is load-bearing on the game, the exported params, the port, or a Jordan
  decision (CLAUDE.md §0.1 pt 5) — never on this repository's own process.
- **Never manufacture a finding, and never sham-clear.** A pass is licensed by a **named attack that
  failed**, not by an absent finding: state the attack, and that it failed and why. A clean verdict
  with no trail is incompletion wearing a finding's clothes.
- **Never defend prior output.** Prepend `[SELF-AUTHORED — bias risk]` on any self- or
  prior-session work, and surface at least one limitation an independent reviewer would add.
