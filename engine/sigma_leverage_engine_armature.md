# σ-Leverage Engine — Portable Resolution Armature

**Consolidation · 2026-05-30 · status: CONSOLIDATED MASTER — NOT committed (placement + canonization are Jordan calls; see §I)**
**Scope: a system-agnostic resolution engine + the interface and method for porting it to any Valoria dice-resolved system.**

`[SELF-AUTHORED — bias risk]` This consolidates sim work authored by prior sessions (Claude). It is treated as external: where the source over-claimed (a dead canonical reference; a misattributed verification figure) the consolidation flags and corrects it rather than carrying it forward.

---

## §0 — What this is, and its true canon status (read first)

This armature **extracts the system-agnostic resolution engine** out of the in-progress combat work and packages it so it can be applied to other systems. It is a *consolidation*, not new design: every formula and constant below is either confirmed canonical or reproduced verbatim from the reference implementation, with provenance.

**Honest status of the parts** (this is the headline — the engine is *not* uniformly canonical):

| Part | Canon class | Where it lives | Verified? |
|---|---|---|---|
| d10 substrate (face map, per-TN μ/σ, σ_N, continuous engine, pool floor) | **A — canonical** | `params/core.md` | ✅ read + recomputed |
| σ-leverage layer (δσ levels, `tanh` soft cap, Ob-shift) | **B — draft sim-seed, NOT canonical** | `tests/sim/v32-combat-balance/m1_dice_sigma_core.py` + design conv `e401c72d` | ✅ reference impl read + recomputed |
| Combat application (levers, state-gating, 8-phase UI, wounding) | mixed / blocked | `designs/audit/2026-05-29-combat-armature/**` | partial; **resolution structure BLOCKED on Jordan** |

**Two drift findings surfaced during consolidation** (detail in §I):
- `[DRIFT]` The leverage layer's cited canonical home — `references/modifier_system_spec.md` (§2.1/§2.3/§3.1, and "§12.3" in the handoff) — **does not exist in the repo.** The layer is presently un-canonized; the M1 module's `[canonical: modifier_system_spec.md …]` comments point at a phantom file (they satisfy the fabrication scanner's *pattern*, not a real source). The module's own docstring is honest: "Class B = v32 draft sim-seed … NOT canonical."
- `[DRIFT]` The handoff (`sigma_leverage_handoff.md` §1a) states the uniform impact is "≈25.8pp at the 50% baseline for δσ = 1.0; verified 5D–18D." The reference implementation's actual verified result (M1 check c) is **+25.8pp for a +0.7σ modifier across 3D–20D**. Φ(0.7)−0.5 = 25.8pp confirms it analytically. For **δσ = 1.0** the impact is **34.1pp** (pre-cap) / **30.9pp** (post-cap). The 25.8pp figure is correct *for +0.7σ*, misattributed in the prose.

---

## §A — The portability boundary: engine vs application

The reason a *portable armature* exists at all: the resolution mechanism is **completely independent of what is being resolved.** Separating the two is the whole move.

| | **ENGINE (portable, system-agnostic)** | **APPLICATION (per-system, owned by each system)** |
|---|---|---|
| What it is | Convert a set of signed advantages (in σ-units) into an Effective Ob and a success probability, with impact uniform across pool size and no foreclosure. | What the advantages *are*, when each is live, how the player accrues and sees them, and what a success/failure *means*. |
| Owns | `sigma_n`, `levels_to_net_sigma`, `soft_cap`, `eff_ob`, `p_success`; the level→δσ table; `M_MAX`. | The lever catalogue; the state-gating table; level-surfacing UI; the resolution structure (one roll vs sequence); consequence/wounding. |
| Changes when | Almost never (it's math). | Per system, per design pass, per Jordan decision. |
| Combat instance | §C (the engine) | §F (combat levers, gating, the **blocked** resolution structure) |

**Thesis.** Any Valoria system that (a) resolves on a d10 success-pool and (b) applies modifiers can drive resolution through this engine. The engine guarantees the modifier's *probability impact is the same whether the pool is 2D or 18D* — which is precisely the architectural fix for the small-pool / non-uniform-impact defect class the `valoria-resolution-diagnostic` skill exists to find (its √N small-pool insight is *why* this engine was built; see §E).

---

## §B — The substrate (Class A — canonical, `params/core.md`)

These are confirmed by reading `params/core.md` and recomputed this session. **Do not approximate; do not edit here** (canon owns them).

**Face rule (d10, no chain):** `1 → −1 · 2–6 → 0 · 7–9 → +1 · 10 → +2`
(Recalculated 2026-05-15 to fix a prior error that scored face 10 as +1.)

**Per-die statistics** (used to parameterize the continuous engine):

| TN | μ (per die) | σ² | σ (per die) |
|---|---|---|---|
| 6 (Controlled) | 0.50 | 0.65 | 0.806 |
| 7 (Standard) | 0.40 | 0.64 | 0.800 |
| 8 (Desperate) | 0.30 | — | 0.781 |

**Continuous engine (canonical for Godot; ED-833 Decision E):** `net ~ Normal(μ·N, σ·√N)`. Discrete and continuous are statistically equivalent specifications (matches discrete Monte-Carlo to within ~0.03 mean / ~0.02 sd at pool 5–17, TN7). The continuous form is what the engine resolves against.

**Pool floor:** 1D (preserves agency; a 1D TN7 roll vs Ob1 ≈ 40% success — the floor does not prevent failure).

**Outcome-distribution width** (the quantity the leverage layer scales against): the SD of `net` is `σ_per_die[TN] · √N`. This is what `σ_N` *is*.

---

## §C — The leverage layer (Class B — draft; the portable kernel)

Reference implementation: `tests/sim/v32-combat-balance/m1_dice_sigma_core.py` (commit `b9b6d4e`, self-test PASS). Constants are **sim-tunable drafts, not canon.** Reproduced verbatim:

**Level → δσ map** (player-facing abstraction; the math is hidden from the player):

| Level | δσ | Migration anchor |
|---|---|---|
| Minor | 0.25 | — |
| Moderate | 0.50 | v31 ±1 Ob ≈ Moderate |
| Strong | 0.75 | v31 ±2 Ob ≈ Strong |
| Major | 1.00 | — |

**The four engine functions** (exact):

```
σ_N(pool)            = SIGMA_N_COEFF · √pool          # SIGMA_N_COEFF = 0.8   (see §D portability note)
net_σ                = Σ(advantage levels) − Σ(adverse levels)      # signed, pre-cap, in σ-units
eff_σ  = soft_cap    = M_MAX · tanh(net_σ / M_MAX)    # M_MAX = 1.5
Effective Ob         = base_Ob − eff_σ · σ_N
P(success)           = Φ( (μ·N − Effective Ob) / (σ·√N) )          # continuous engine
```

**Why impact is uniform (the F1 property).** `Ob shift = δσ · σ_N` and the z-score of that shift is `shift / σ_N = δσ`. The `√N` and the per-die σ cancel, so a given δσ moves the outcome's z by exactly δσ **at every pool size** → the same probability change everywhere. (A flat *dice* modifier's impact scales with 1/√N — small pools swing wildly; σ-leverage does not. This is what stops raw pool/dice count from dominating — the C-04 fix in combat terms.)

**Verified properties** (recomputed this session, continuous engine, 50% baseline; pre-cap unless noted):

*Uniform impact across pool size (δσ = +0.7σ):*

| Pool | P₀ | P₁ | Δ |
|---|---|---|---|
| 3D | 50.0% | 75.8% | +25.8pp |
| 5D | 50.0% | 75.8% | +25.8pp |
| 8D | 50.0% | 75.8% | +25.8pp |
| 12D | 50.0% | 75.8% | +25.8pp |
| 17D | 50.0% | 75.8% | +25.8pp |
| 20D | 50.0% | 75.8% | +25.8pp |

Spread across pools = **0.0pp**. (Φ(0.7)−0.5 = 25.8pp.) This reproduces M1 check (c).

*Per-level impact (corrected — supersedes the handoff's δσ=1.0/25.8pp):*

| δσ (level) | ΔP pre-cap | ΔP post-cap |
|---|---|---|
| 0.25 (Minor) | +9.9pp | +9.8pp |
| 0.50 (Moderate) | +19.1pp | +18.5pp |
| 0.75 (Strong) | +27.3pp | +25.6pp |
| 1.00 (Major) | **+34.1pp** | +30.9pp |

*Soft cap (M_MAX = 1.5):* `0.5σ→0.482 · 1.0σ→0.874 · 2.0σ→1.305 · 3.0σ→1.446`; saturates to ±1.5σ. **No dead-zone** (a hard clamp would create a threshold cliff — NERS Lesson 6; `tanh` does not).

*No foreclosure (the F2 property):* a fully saturated adverse stack caps at −1.5σ → at a 50% baseline the disadvantaged side floors at **Φ(−1.5) = 6.7%**, never 0%. Maximum single-direction swing = Φ(1.5)−0.5 = **43.3pp**, uniform across pool. (The handoff's "~9% / ~43pp": 43pp confirmed; the floor at a *50% baseline* is 6.7% — "~9%" is a specific non-50% engagement baseline, not the general floor.)

*Worked conversion (re-checked):* Closing, attacker Pool 6D, base Ob 2, live = Stance Counter Moderate (+0.50) + favourable Reaction Moderate (+0.50) + Reading Minor (+0.25) + perception Minor (+0.25) → net_σ = +1.50 → eff_σ = 1.5·tanh(1.0) = 1.142 → Effective Ob = 2 − 1.142·1.960 = **−0.239 → floored to 0**. ✓

---

## §D — The porting interface

A consuming system talks to the engine through exactly this contract.

**The system supplies:**
1. `pool` (N) — its resolution pool for the action (integer ≥ 1).
2. `base_Ob` — the unmodified obstacle.
3. `TN` — the system's target number for this roll (6 / 7 / 8).
4. A signed set of **δσ contributors** — each one of its modifiers, classified at a level (Minor/Moderate/Strong/Major → δσ via the §C table), with a sign (favouring the actor = +, opposing = −), and **gated** so only contributors physically relevant to the current state are non-zero.

**The engine returns:** `Effective Ob`, and `P(success)` under the continuous engine. (Resolution sampling, degrees, and consequence are the *system's* business — see §A/§F.)

**Portability generalization** `[ASSUMPTION: σ_N should track the system's own TN — basis: bottom-up = the M1 z-cancellation derivation; top-down = the engine's stated goal of exact uniform impact. Jordan-vetoable. Combat is unaffected (it uses TN7 where 0.8 is exact).]`

The reference implementation hardcodes `SIGMA_N_COEFF = 0.8`, which is **only** the per-die σ at **TN7**. For systems resolving at other TNs, the uniform-impact guarantee is exact only if `σ_N` uses *that system's* per-die σ:

```
σ_N(pool, TN) = σ_per_die[TN] · √pool      # 6→0.806, 7→0.800, 8→0.781   (from params/core.md §B)
```

Drift from using the hardcoded 0.8 instead (δσ=+0.7σ, 50% baseline):

| TN | hardcoded-0.8 | per-TN σ (exact) |
|---|---|---|
| 6 | 25.6pp | 25.8pp |
| 7 | 25.8pp | 25.8pp |
| 8 | **26.3pp** | 25.8pp |

Small (≤0.5pp), but the engine's *one promise* is exact uniformity, so the portable form should parameterize by TN. **Recommendation:** replace the constant `SIGMA_N_COEFF` with a per-TN lookup keyed to the canonical `params/core.md` σ table. This is the only change the engine needs to be system-general; it introduces nothing new (the σ values are already canonical).

---

## §E — Porting methodology (how to apply the engine to a system)

The engine is portable; *porting* is still per-system design work. Four steps, each grounded:

1. **Locate the resolution.** Identify where the system rolls a d10 pool for an outcome (vs deterministic accounting or a clock — most Valoria systems are composites; see the three-category model in the `valoria-resolution-diagnostic` skill). The engine drives the *dice-resolved* component only.
2. **Enumerate and classify modifiers.** Every existing modifier becomes a δσ contributor at a level. Ground each: the level must be justified bottom-up (what the modifier currently does) and top-down (real precedent or published design). v31 ±1 Ob → Moderate, ±2 → Strong is the migration anchor.
3. **Define state-gating.** Specify which contributors are live in which engagement/interaction states (this both shrinks the per-decision load — Elegance — and bounds the σ-sum feeding the cap). Combat's table (§F) is the template.
4. **Decide level-surfacing.** Players never see σ. Decide how the system shows advantage levels in its UI.

**Why this is the right kernel for the small-pool problem.** The `valoria-resolution-diagnostic` skill's core finding is that the d10 engine "does its worst work at small pools" because a flat die's marginal value scales with 1/√N. Its **Lesson 2** ("continuous resources and base parameters take uniform-*impact* steps") and **Lesson 3** (keep dice off small-pool, load-bearing, binary decisions) are exactly what this engine implements *architecturally*: σ-leverage delivers uniform *impact* (not uniform *form*) and decouples the outcome from raw pool size. **This armature is the realized form of that skill's prescribed fix.** Conversely, the skill's discipline applies in reverse — porting the engine is itself a mechanic that must pass NERS/Omega (§H); do not bolt it onto systems that don't have the defect (see §G).

---

## §F — Worked port #1: combat (the source application)

The engine was extracted *from* the combat work; combat is therefore the first (and only in-progress) port. It is **not** finished — its resolution structure is blocked.

**Combat's δσ levers** (the system-specific catalogue; magnitudes are draft sim-seeds, Jordan-tunable):
- **Stance Counter Matrix** — 5×5 anti-symmetric; ±1 Ob legacy → Moderate, ±2 → Strong. Live at *Closing*.
- **Reading sub-channels** (Tactile/Temporal/Geometric/Biomechanical/Rhythmic/Thread) + Intent-Reading tier 0–5 → an Ob modifier. *(C-06 fix: Cognition/Attunement matter in combat.)*
- **Reaction-aspect modifier** — `δσ = baseline_r + slope_r·(depth−3)`.
- **Facing / FoV** — Central 1.0 / Near-peripheral 0.6 / Far-peripheral 0.3 / Blind 0.0 scaling sight-mediated Reading; flank ≈ −1 Ob, rear ≈ −2. *(C-07 fix.)*
- **Weapon class** (phase-keyed) + **Coherence / named sets** (δσ set bonus, with two antagonism exceptions).

**Combat state-gating** (the template for step 3 of §E):

| Engagement state | Live δσ contributors |
|---|---|
| Out-of-contact | perception/FoV · Reading-mod · weapon phase-strength · set bonus |
| Closing | + Stance Counter · Reaction matchup |
| In-bind | Reaction matchup · Tactile Reading · Grip/weapon phase · set bonus (Stance Counter + sight-perception **drop** — bind is contact-mediated) |
| Breaking | perception/FoV · Reaction matchup · Reading-mod |

**⛔ BLOCKED — Jordan decision (handoff §2.5).** The combat *resolution structure* is unset and must not be invented: one decisive strike vs a short bounded exchange (NOT attrition); the role of any resolution pool and how it avoids re-introducing pool dominance; commit-depth-driven consequence/wounding without crits/multipliers. **The engine extraction (§C/§D) does not depend on this** — it is exactly the per-system "what does resolution look like here" question, and for combat it is Jordan's. The M9 bottom-up wound model (severity = net + bounded-Str − per-type armour-resist; historically validated 5/5) is the right *direction* for the damage layer but must be refitted to whatever §2.5 structure is chosen — not to the attrition loop it was tested in.

**Combat-application tuning (out of engine scope; Jordan-pending — see source files):** war-hammer / Heavy-Blunt profile (×3 STR + flat +5-vs-all-armour is the real Strength-dominance lever, *canonical*, in `combat_v30 §5`); weapon-speed→tempo channel; phase-dependent reach (the spear fix); Reading σ-magnitude; Stamina `End×5 → 3·End+2·Spirit`; Spirit reframed as cross-system (correctly weak in a duel). These are weapon/attribute-content calibrations, **not** engine properties — the Strength calibration in fact *demonstrates* the engine is sound: turning Str's tunable channels fully off moved Str only 83%→76%; the dominance was the canonical weapon table, not the engine. Full detail: `strength_calibration_result.md`, `weapon_balance_proposal.md`, `weapon_rebalance_data.json`.

---

## §G — Candidate ports (NOT performed; flagged for per-system work + Jordan)

These are **candidates only.** I have not read these systems' canonical docs this session, so nothing below is a port — each requires (a) fetching the target's canon, (b) the §E methodology, (c) Jordan's per-system design decision and Omega vetting. Listed worst-defect-first per the `valoria-resolution-diagnostic` initial hypotheses:

- **Faction action layer — strong candidate.** The diagnostic's worked example rates it *non-compliant*: bare faction stat (1–7D) rolled for pivotal, irreversible outcomes (seizure, vote) — a fragile small-pool binary, routine exposure. σ-leverage is the named architectural fix (decouple impact from the 2D pool). **Likely highest-value port.** Requires faction-layer canon + Jordan.
- **Personal combat (non-duel) / mass battle** — possible, where small pools meet load-bearing rolls; the diagnostic flagged the flat −1D wound at the 5D floor (Lesson 2 candidate). Requires the respective canon.
- **Social contest — likely does NOT need it.** Pools already 5–18D and the system is rated healthy; applying the engine here would be over-engineering (fails NERS-N/E). Listed to mark the boundary, not to port.

**Do not** treat §G as a backlog of approved ports. It is a map of where the defect the engine fixes is *likely* present (faction) vs absent (social).

---

## §H — Vetting status (Omega / NERS)

Per the Omega framework (`references/throughlines_meta.md`; handoff §3), **the σ-leverage engine is a Class-A new system** → full `N → Ω → Μ → М → Τ → Q` vetting and a `vetting:` block are **required before any canon commit** (enforced by `vetting_gate` on `patch_register_active.yaml` entries id ≥ PP-674). N/Ω/Μ are Jordan's to affirm — I do not assert them.

Provisional **Q-tier** self-assessment (Claude applies Q autonomously; iterate-don't-reject):
- **Elegant** — one rule a player can restate: *advantage is measured in σ-units and always changes your odds by the same amount, no matter your pool.* The math is hidden behind four levels.
- **Robust** — holds at the small-pool extreme (the F1 reason it exists); no foreclosure (F2, floors ~7%); modifiers are uniform-impact.
- **Smooth** — the *same* engine resolves every system that adopts it; no special-casing across scales; `tanh` removes the threshold cliff a hard cap would add.

`[N/Ω flag for Jordan]` Necessity/Intent are not mine to rule. The N case to make: this models how a leader's *prepared advantages* (position, reading, setup) decide a confrontation independent of raw stat-bulk — a real leadership dynamic. Flagged, not asserted.

---

## §I — Findings & decisions for Jordan (consolidated, worst-first)

1. **`[DRIFT — structural]` The leverage layer is un-canonized; its cited home `references/modifier_system_spec.md` does not exist.** Decision: **canonize this armature as the engine spec** (creating the missing `modifier_system_spec.md` / an engine-level doc, which also clears the M1 module's phantom `[canonical:]` citations) — *or* keep the layer Class-B draft. Canonization requires the §H Omega vetting. **This is the load-bearing decision; the engine cannot be "ported to systems" as canon until it is itself canon.**
2. **⛔ Combat resolution structure (§2.5)** — BLOCKED, Jordan-only: one strike vs bounded exchange (not attrition); resolution-pool role; commit-depth consequence. The engine does not need it; combat does.
3. **`[DRIFT — factual]` Correct the handoff's uniform-impact figure.** It reads "25.8pp for δσ=1.0 / 5D–18D"; verified truth is **+25.8pp for +0.7σ across 3D–20D**; δσ=1.0 = 34.1pp pre-cap / 30.9pp capped. (Corrected throughout this doc.)
4. **`[PORT-1]` Generalize `σ_N` to per-TN** (§D): `σ_N(pool,TN)=σ_per_die[TN]·√pool` so the uniform-impact guarantee is exact for TN6/TN8 systems (faction/thread). No new values — uses the canonical σ table. Combat unaffected. Jordan-vetoable mechanical refinement.
5. **`[CANDIDATE PORTS]`** Approve/deny per-system targeting (§G). Faction action layer is the strongest candidate; social contest likely should be excluded (over-engineering).
6. **Combat-application tuning** (war hammer, speed-tempo, phase-reach, Reading magnitude, Stamina, Spirit) — Jordan-pending **canon** calls, out of engine scope; detail in the source files.

**Why this master was not committed:** (a) placement of a *cross-system* engine doc is an architecture decision broader than the combat-armature handoff's owned paths; (b) canonical_sources.yaml is at 8,892 / 9,000 tokens — adding a new design-doc source (co-file rule) risks the size gate; (c) elevating the Class-B leverage layer to canon needs Jordan's ratification + Omega vetting (§H). On your word I will commit it — name the path (candidates: `designs/audit/2026-05-29-combat-armature/sigma_leverage_engine_armature.md` as a consolidation artifact, or an engine-level home such as `references/modifier_system_spec.md` / `designs/architecture/` if it is to become the canonical engine spec) — and stage the `vetting:` block + the supersession note for the engine portion of `sigma_leverage_handoff.md` §1.

---

## §J — Provenance (`[READ:]` trail)

- `[READ: designs/audit/2026-05-29-combat-armature/sigma_leverage_handoff.md — full (25,503 chars; §0–§7)]`
- `[READ: designs/audit/2026-05-29-combat-armature/strength_calibration_result.md — full]`
- `[READ: designs/audit/2026-05-29-combat-armature/weapon_balance_proposal.md — full]`
- `[READ: designs/audit/2026-05-29-combat-armature/harness_defect_handoff.md — full]`
- `[READ: designs/audit/2026-05-29-combat-armature/weapon_rebalance_data.json — full]`
- `[READ: tests/sim/v32-combat-balance/m1_dice_sigma_core.py — full (9,652 chars; reference implementation + self-test)]`
- `[READ: params/core.md — engine-relevant sections (face rule, per-TN μ/σ, continuous engine, pool floor)]`
- `[READ: references/canonical_sources.yaml — searched for engine/modifier/leverage sources; confirmed modifier_system_spec.md absent]`
- `[VERIFIED: uniform-impact, per-level ΔP, soft-cap checkpoints, foreclosure floor, TN-portability drift, worked example — recomputed this session, continuous engine, math.erf]`
- `[CONFIDENCE: high — substrate confirmed against canon; leverage layer reproduced from reference impl + recomputed; the two drift findings are evidenced (file-absence check; analytic Φ(0.7)=25.8pp).]`

*Engine vs application is the whole armature: the σ-leverage engine resolves any d10 success-pool with uniform impact and no foreclosure; each system supplies its own levers, gating, and meaning. Porting it to a given system — and canonizing it — is the next, Jordan-gated step.*
