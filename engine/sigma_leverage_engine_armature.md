# σ-Leverage Engine — Portable Resolution Armature

**Consolidation · 2026-05-30 · status: COMMITTED to `engine/` (4e6df85); audit-revised — advantage reformulated as a μ-shift (resolves the P-232 conflict). Canonization still pending Jordan + Omega vetting (§H/§I).**
**Scope: a system-agnostic resolution engine + the interface and method for porting it to any Valoria dice-resolved system.**

`[SELF-AUTHORED — bias risk]` This consolidates sim work authored by prior sessions (Claude). It is treated as external: where the source over-claimed (a dead canonical reference; a misattributed verification figure) the consolidation flags and corrects it rather than carrying it forward.

---

## §0 — What this is, and its true canon status (read first)

This armature **extracts the system-agnostic resolution engine** out of the in-progress combat work and packages it so it can be applied to other systems. It is a *consolidation*, not new design: every formula and constant below is either confirmed canonical or reproduced verbatim from the reference implementation, with provenance.

**Honest status of the parts** (this is the headline — the engine is *not* uniformly canonical):

| Part | Canon class | Where it lives | Verified? |
|---|---|---|---|
| d10 substrate (face map, per-TN μ/σ, σ_N, continuous engine, pool floor) | **A — canonical** | `params/core.md` | ✅ read + recomputed |
| σ-leverage layer (δσ levels, `tanh` soft cap, **μ-shift** outcome boost) | **B — draft sim-seed, NOT canonical** | `tests/sim/v32-combat-balance/m1_dice_sigma_core.py` + design conv `e401c72d` | ✅ reference impl read, recomputed, **audited 2026-05-30** |
| Combat application (levers, state-gating, 8-phase UI, wounding) | mixed / blocked | `designs/audit/2026-05-29-combat-armature/**` | partial; **resolution structure BLOCKED on Jordan** |

**Two drift findings surfaced during consolidation** (detail in §I):
- `[DRIFT]` The leverage layer's cited canonical home — `references/modifier_system_spec.md` (§2.1/§2.3/§3.1, and "§12.3" in the handoff) — **does not exist in the repo.** The layer is presently un-canonized; the M1 module's `[canonical: modifier_system_spec.md …]` comments point at a phantom file (they satisfy the fabrication scanner's *pattern*, not a real source). The module's own docstring is honest: "Class B = v32 draft sim-seed … NOT canonical."
- `[DRIFT]` The handoff (`sigma_leverage_handoff.md` §1a) states the uniform impact is "≈25.8pp at the 50% baseline for δσ = 1.0; verified 5D–18D." The reference implementation's actual verified result (M1 check c) is **+25.8pp for a +0.7σ modifier across 3D–20D**. Φ(0.7)−0.5 = 25.8pp confirms it analytically. For **δσ = 1.0** the impact is **34.1pp** (pre-cap) / **30.9pp** (post-cap). The 25.8pp figure is correct *for +0.7σ*, misattributed in the prose.

**Audit 2026-05-30 (`audit/lane-c/sigma_leverage_engine_audit.md` + `engine_audit_harness.py`).** A granular logic-pipeline audit found the engine's math internally exact (reference impl == its own continuous spec to 1e-16) but surfaced two real findings, resolved/scoped here:
- **F1 [was P1] — RESOLVED.** The prior **Ob-reduction** form (`Eff_Ob = base_Ob − eff_σ·σ_N`) drove Effective Ob below 1 — violating canon **P-232** ("Ob minimum 1; no modifier may reduce Ob below 1") — and made the Overwhelming threshold `2·Eff_Ob` nonsensical when Ob went negative. **Fix (mechanical-tier, Jordan-vetoable):** advantage is now a **μ-shift** — it boosts the *roll* (`mean += eff_σ·σ·√N`) and leaves `base_Ob`/TN untouched, so P-232 is never triggered. Identical odds at TN7, TN-exact elsewhere. The P-232-*exemption* alternative was considered and rejected (it leaves F3 + the degree-ladder bug unsolved). Logged **ED-884**.
- **F3 [PORT-1] — RESOLVED by the same change.** The hardcoded `SIGMA_N_COEFF = 0.8` was the TN7 σ; the μ-shift uses the system's own σ, so uniform impact is exact at every TN by construction.
- **F2 [P2] — scoped.** Uniform impact is a *continuous-engine* property; under *discrete* success-counting it degrades at small pools (canon ED-836 flags bare 1–7D as "shaky"). Stated wherever the uniform claim appears. Godot resolves continuously, so it holds there.

---

## §A — The portability boundary: engine vs application

The reason a *portable armature* exists at all: the resolution mechanism is **completely independent of what is being resolved.** Separating the two is the whole move.

| | **ENGINE (portable, system-agnostic)** | **APPLICATION (per-system, owned by each system)** |
|---|---|---|
| What it is | Convert a set of signed advantages (in σ-units) into an Effective Ob and a success probability, with impact uniform across pool size and no foreclosure. | What the advantages *are*, when each is live, how the player accrues and sees them, and what a success/failure *means*. |
| Owns | `levels_to_net_sigma`, `soft_cap`, `net_boost`, `p_success`; the level→δσ table; `M_MAX`. (`eff_ob`/`sigma_n` are now a P-232-floored *display* helper, not resolution.) | The lever catalogue; the state-gating table; level-surfacing UI; the resolution structure (one roll vs sequence); consequence/wounding. |
| Changes when | Almost never (it's math). | Per system, per design pass, per Jordan decision. |
| Combat instance | §C (the engine) | §F (combat levers, gating, the **blocked** resolution structure) |

**Thesis.** Any Valoria system that (a) resolves on a d10 success-pool and (b) applies modifiers can drive resolution through this engine. Under the continuous engine (canonical for Godot), the engine guarantees the modifier's *probability impact is the same whether the pool is 2D or 18D* (exact at all pools incl. 1D) — which is precisely the architectural fix for the small-pool / non-uniform-impact defect class the `valoria-resolution-diagnostic` skill exists to find (its √N small-pool insight is *why* this engine was built; see §E). *Caveat: this is a continuous-engine identity. Under literal discrete success-counting the modifier's impact is lumpy at small pools — canon ED-836 flags bare 1–7D as "shaky" — so a discrete-resolved port needs its own small-pool handling (clock/aggregate, per the diagnostic). Godot resolves continuously, so it holds there.*

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
net_σ                = Σ(advantage levels) − Σ(adverse levels)      # signed, pre-cap, in σ-units
eff_σ  = soft_cap    = M_MAX · tanh(net_σ / M_MAX)                  # M_MAX = 1.5
net boost (μ-shift)  = eff_σ · σ_per_die[TN] · √N                   # advantage boosts the ROLL
P(success)           = Φ( (μ·N + boost − base_Ob) / (σ·√N) )       # = Φ(z_base + eff_σ); base_Ob & TN untouched
```

**Why impact is uniform (the F1 property), and why μ-shift not Ob-reduction.** The boost `eff_σ·σ·√N` enters the z-score over `σ·√N`, so the per-die σ and `√N` cancel and the modifier moves the outcome's z by exactly `eff_σ` at **every pool size and every TN** → the same probability change everywhere, TN-exact. Advantage is applied to the *roll* (a μ-shift), **not** as an Ob reduction: the earlier Ob-reduction form drove Effective Ob below 1 (violating canon P-232) and corrupted the degree ladder; the μ-shift leaves `base_Ob`/TN fixed and is identical at TN7. (A flat *dice* modifier's impact scales with 1/√N — small pools swing wildly under the continuous engine; σ-leverage does not. This is the C-04 fix in combat terms.)

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

Spread across pools = **0.0pp** (Φ(0.7)−0.5 = 25.8pp), and now **TN-exact** at TN6/7/8 under the μ-shift. This reproduces M1 check (c). *Continuous-engine property; under discrete resolution it degrades at small pools — canon ED-836 (see §E).*

*Per-level impact (corrected — supersedes the handoff's δσ=1.0/25.8pp):*

| δσ (level) | ΔP pre-cap | ΔP post-cap |
|---|---|---|
| 0.25 (Minor) | +9.9pp | +9.8pp |
| 0.50 (Moderate) | +19.1pp | +18.5pp |
| 0.75 (Strong) | +27.3pp | +25.6pp |
| 1.00 (Major) | **+34.1pp** | +30.9pp |

*Soft cap (M_MAX = 1.5):* `0.5σ→0.482 · 1.0σ→0.874 · 2.0σ→1.305 · 3.0σ→1.446`; saturates to ±1.5σ. No hard clamp (which would be a threshold cliff — NERS Lesson 6; `tanh` is smooth, slope 1 at 0, so small modifiers apply ~fully). Marginal value falls off **steeply**, though — per added *major* (50% base): +30.9 / +9.5 / +2.2 / +0.5 pp; past ~2 stacked advantages the next is nearly worthless (intended Lesson-5 bound, but the player cannot easily intuit it — F4).

*No foreclosure (the F2 property):* a fully saturated adverse stack caps at −1.5σ → at a 50% baseline the disadvantaged side floors at **Φ(−1.5) = 6.7%**, never 0%. Maximum single-direction swing = Φ(1.5)−0.5 = **43.3pp**, uniform across pool. (The handoff's "~9% / ~43pp": 43pp confirmed; the floor at a *50% baseline* is 6.7% — "~9%" is a specific non-50% engagement baseline, not the general floor.)

*Worked conversion (re-checked, μ-shift):* Closing, attacker Pool 6D, base Ob 2, live = Stance Counter Moderate (+0.50) + favourable Reaction Moderate (+0.50) + Reading Minor (+0.25) + perception Minor (+0.25) → net_σ = +1.50 → eff_σ = 1.5·tanh(1.0) = 1.142 → boost = 1.142·(0.8·√6) = **+2.238** → shifted mean 2.40 → **4.64**, base Ob stays **2** → P = Φ((4.64−2)/1.96) = **91.1%**. Overwhelming threshold stays 2·Ob = 4. (The old Ob-reduction form gave Eff_Ob = −0.239 — a P-232 breach; see §0 F1.) ✓

---

## §D — The porting interface

A consuming system talks to the engine through exactly this contract.

**The system supplies:**
1. `pool` (N) — its resolution pool for the action (integer ≥ 1).
2. `base_Ob` — the unmodified obstacle.
3. `TN` — the system's target number for this roll (6 / 7 / 8).
4. A signed set of **δσ contributors** — each one of its modifiers, classified at a level (Minor/Moderate/Strong/Major → δσ via the §C table), with a sign (favouring the actor = +, opposing = −), and **gated** so only contributors physically relevant to the current state are non-zero.

**The engine returns:** `P(success)` under the continuous engine (advantage applied as a μ-shift; `base_Ob` and TN unchanged), plus an optional P-232-floored *display* "effective difficulty." (Resolution sampling, degrees, and consequence are the *system's* business — see §A/§F.)

**Portability generalization — RESOLVED by the μ-shift (audit 2026-05-30, ED-884).** The engine no longer carries a hardcoded `σ_N` coefficient in resolution: the μ-shift uses the system's own `σ_per_die[TN]·√N`, so the uniform-impact guarantee is **exact at every TN by construction** (the σ and `√N` cancel in the z-score). The former hardcoded `SIGMA_N_COEFF = 0.8` (the TN7 σ) survives only in the P-232-floored *display* helper `eff_ob`, never in resolution.

What the prior hardcoded-0.8 form drifted by (δσ=+0.7σ, 50% baseline) — now eliminated:

| TN | old hardcoded-0.8 | μ-shift (per-TN, exact) |
|---|---|---|
| 6 | 25.6pp | **25.8pp** |
| 7 | 25.8pp | **25.8pp** |
| 8 | 26.3pp | **25.8pp** |

So a faction (TN6) or thread (TN8) port inherits exact uniformity with no extra calibration. No new values — the σ table is canonical (`params/core.md §B`).

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
- **Elegant** — one rule a player can restate: *advantage always changes your odds by the same amount, no matter your pool.* The math is hidden behind four levels. (Caveat F4: stacking saturates steeply — the 4th advantage is ~worthless, and the player cannot easily intuit that.)
- **Robust** — uniform impact and no foreclosure (the *modifier* floors at Φ(z_base−1.5) = 6.7% at a 50% base; never 0/1). **Uniform impact holds exactly under the continuous engine at all pools incl. 1D; under discrete resolution it degrades at small pools (canon ED-836 — 1–7D "shaky"), so discrete-resolved ports need their own small-pool handling.** The P-232 conflict is resolved via the μ-shift (no Ob reduction).
- **Smooth** — the *same* engine resolves every system that adopts it; no special-casing across scales; `tanh` removes the threshold cliff a hard cap would add.

`[N/Ω flag for Jordan]` Necessity/Intent are not mine to rule. The N case to make: this models how a leader's *prepared advantages* (position, reading, setup) decide a confrontation independent of raw stat-bulk — a real leadership dynamic. Flagged, not asserted.

---

## §I — Findings & decisions for Jordan (consolidated, worst-first)

1. **`[RESOLVED — mechanical tier, Jordan-vetoable]` F1: P-232 conflict.** The Ob-reduction form violated canon P-232 (drove Eff_Ob < 1). **Fixed** by the μ-shift (advantage boosts the roll; `base_Ob`/TN untouched) — applied to the M1 reference impl and this doc; logged **ED-884**. You can **veto** in favour of the alternative (exempt the σ-transform from P-232), but that is strictly worse: it leaves F3 and the degree-ladder bug unsolved.
2. **`[RESOLVED — same change]` F3 (PORT-1): TN calibration.** The μ-shift is TN-exact by construction; the hardcoded `SIGMA_N_COEFF = 0.8` is out of the resolution path.
3. **`[OPEN — load-bearing]` Canonize this armature as the engine spec?** Still the gating decision — the engine cannot be "ported as canon" until it *is* canon, and canonizing clears the phantom `references/modifier_system_spec.md` reference. Requires the §H Omega vetting. (Sequence: this audit + μ-shift fix → your ratification → Omega vet → canon.)
4. **⛔ Combat resolution structure (§2.5)** — BLOCKED, Jordan-only: one strike vs bounded exchange (not attrition); resolution-pool role; commit-depth consequence. The engine does not need it; combat does.
5. **`[CANDIDATE PORTS]`** Approve/deny per-system targeting (§G). Faction action layer (TN6) is the strongest candidate — and now inherits exact uniformity for free; social contest likely excluded (over-engineering).
6. **Combat-application tuning** (war hammer, speed-tempo, phase-reach, Reading magnitude, Stamina, Spirit) — Jordan-pending **canon** calls, out of engine scope.
7. **`[DOC-FIXED]` F2 (scope) + F4 (saturation framing) + the handoff's δσ=1.0/25.8pp drift** — corrected throughout this doc (uniform impact scoped to the continuous engine, ED-836 cited; saturation table added).

**Status.** This master is **committed to `engine/sigma_leverage_engine_armature.md`** (initial `4e6df85`; this revision adds the μ-shift + audit corrections). It remains a **Class-B consolidation artifact** — deliberately *not* registered in `references/canonical_sources.yaml` — pending the canonization decision (#3) and Omega vetting (§H).

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
- `[READ: engine/sigma_leverage_engine_armature.md — this doc, prior commit 4e6df85]`
- `[VERIFIED: audit 2026-05-30 (sigma_leverage_engine_audit.md + engine_audit_harness.py) — T1 code==spec 1e-16; T2 continuous uniformity exact incl. 1D; T3 discrete/continuous divergence; T4 P-232 breach quantified; T5 TN drift; μ-shift re-test RT1–RT6 PASS]`
- `[FIXED: F1 (P-232) + F3 (PORT-1) via μ-shift in m1_dice_sigma_core.py (self-test 7/7); F2/F4 doc-scoped; logged ED-884]`
- `[VERIFIED: uniform-impact, per-level ΔP, soft-cap checkpoints, foreclosure floor, TN-portability drift, worked example — recomputed this session, continuous engine, math.erf]`
- `[CONFIDENCE: high — substrate confirmed against canon; leverage layer reproduced from reference impl + recomputed; findings evidenced numerically; μ-shift fix re-tested.]`

*Engine vs application is the whole armature: under the continuous engine the σ-leverage kernel resolves any d10 success-pool with uniform, TN-exact impact and no foreclosure, applying advantage as a μ-shift that never reduces Ob below 1; each system supplies its own levers, gating, and meaning. Canonizing it is the next, Jordan-gated step.*
