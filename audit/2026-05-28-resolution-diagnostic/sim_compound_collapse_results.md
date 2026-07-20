# Integrated Compound-Collapse Simulation — Results

**Date:** 2026-05-28
**Sim:** `sim_compound_collapse.py` (this folder)
**Task:** Model the 3+-system emergent interaction the 2026-05-28 resolution diagnostic named as a blind spot but never simulated — a weak faction defending one contested territory under simultaneous (a) military pressure → Trigger 5, (b) Wealth-0 → Military cascade (L7), and (c) a practitioner doing Structural threadwork → Coherence drain / Rendering Crisis / regional RS drain.
**Skill:** valoria-simulator Mode B (interaction chain) + Mode D (cascade/regression). Bootstrap live; `task_gate('audit')` passed; couplings read from canon this session (cited below).
**Bias:** `[SELF-AUTHORED — bias risk]` — extends my own diagnostic. §5 is the honest negative result on what this sim *cannot* answer.

---

## §0 — Headline (what the sim actually establishes)

**The compound death-spiral I hand-traced earlier does not behave as I claimed — because the canonical Trigger-5 gate decouples small-scale battle loss from faction Stability, and it shields the weakest factions specifically.** The payoff question ("does the compound of three loss pressures overwhelm the ~26% per-gate recovery into determinism?") is answered: **no — but not for the reason I expected.** The compound doesn't overwhelm recovery; the *battle→faction edge barely transmits force at small scale*, so the loop is starved at its input, not balanced at its output.

And the sim found a **non-obvious structural result that is robust to all modeling uncertainty** (it is pure battle resolution, recovery-independent): **Trigger-5 exposure is non-monotonic in faction strength, peaking at the middle, not the bottom.**

---

## §1 — The robust finding: Trigger-5 firing is non-monotonic (recovery-independent)

Trigger-5 (faction_layer_v30) fires — i.e. a lost battle costs faction Stability — only when **all three** conditions hold: (A) Military pool ≥ 4, (B) degree = Failure (net ≤ 0), (C) net ≤ −2 **OR** pool ≥ 6 **OR** a named officer is lost. Firing rate by the defender's pool (`Pool = min(Size,Cmd)+Cmd`, MB5 no-floor), 80k trials/row, attack Ob 3:

| Faction Mil/Cmd | Pool | P(battle Failure) | P(net ≤ −2) | **P(Trigger-5 fires)** | Mechanism |
|---|---|---|---|---|---|
| 1 / 1 | 2D | 0.418 | 0.010 | **0.000** | pool < 4 → Condition A blocks entirely |
| 2 / 2 | 4D | 0.252 | 0.018 | **0.019** | needs the rare net ≤ −2 (C) |
| 3 / 2 | 4D | 0.250 | 0.019 | **0.019** | needs net ≤ −2 (C) |
| **3 / 3** | **6D** | 0.166 | 0.017 | **0.166** | **pool ≥ 6 → C auto-fires on ANY failure** |
| 4 / 3 | 6D | 0.166 | 0.018 | **0.166** | pool ≥ 6 auto |
| 4 / 4 | 8D | 0.112 | 0.014 | **0.112** | pool ≥ 6 auto |
| 5 / 4 | 8D | 0.115 | 0.015 | **0.115** | pool ≥ 6 auto |
| 6 / 5 | 10D | 0.079 | 0.012 | **0.079** | pool ≥ 6 auto; strong factions just fail less |
| 7 / 5 | 10D | 0.080 | 0.012 | **0.080** | as above |

**The curve is non-monotonic: 0% → 1.9% → (jump) → 16.6% → declining to 8%.** Two mechanisms produce it:
1. **The bottom is shielded twice.** A Cmd-1 faction (pool 2D) is fully blocked by Condition A (pool < 4 = "raid, no consequence"). A Cmd-2 faction (pool 4D) clears A but its failures rarely reach the net ≤ −2 that C requires, so it fires only 1.9%.
2. **The middle is maximally exposed by a cliff.** At Cmd 3 the pool hits exactly 6D, tripping Condition C's `pool ≥ 6` clause — which auto-fires the gate on *any* failure (16.6%), an **8.7× jump** from Cmd 2. Then exposure declines as stronger factions simply fail less often.

`[CONFIDENCE: high]` — pure battle-resolution Monte Carlo, recovery-independent, sanity-checked die rule. This finding does not depend on any of the uncertain recovery/coupling assumptions below.

**Reconciliation with prior work:** this *corrects* my earlier emergent hand-trace, which assumed every battle loss pressured Stability and concluded the weak faction faced a "deterministic" then "loss-weighted probabilistic" spiral. The canonical gate says otherwise — the weakest faction's battles barely touch Stability at all. The faction-layer's real battle→Stability exposure lives at **Cmd 3 (pool 6D)**, which is a *mid-tier* faction, and the cause is the `pool ≥ 6` cliff in Condition C. **This is a new NERS-S finding: Condition C stacks a pool-size cliff (≥6) onto a magnitude threshold (net ≤ −2), so a single point of Command (2→3) jumps battle→Stability exposure 8.7×.**

---

## §2 — Isolated loops (corrected model, directional only)

With each pressure applied alone to a weak faction (Stab 3, Mil 2, Wealth 2, Cmd 2), conditional recovery:

| Pressure alone | P(collapse / 20 seasons) | median season |
|---|---|---|
| Battle only (Trigger 5) | ~0.6% | 13 |
| Wealth drain only (L7) | ~0.1% | 11 |
| Practitioner only (Coherence) | ~1.5% | 6 |

**Directionally:** none of the three loops alone is a strong collapse driver at this faction's scale. The practitioner loop is the *fastest* to bite (median season 6 — Coherence drains deterministically at −2/op) but rarely reaches faction collapse because the RS→Stability coupling [A3] is weak/qualitative. The L7 Wealth cascade is slow (drains Military, not Stability directly). These are **directional**, not magnitudes to trust (see §5).

---

## §3 — The compound (and why the magnitude is NOT reportable)

Running all three simultaneously, the compound P(collapse) came out *near the isolated-battle level* (~0.4–4.5% depending on Stab0), **not** amplified. The naive read would be "the compound is safe." **I do not report that as a finding, because the sensitivity sweep shows the result is dominated by an unmodeled assumption, not by the mechanics** (§5). The one compound result I trust is **directional**: collapse, when it happens, clusters at **season 3** — the Coherence-drain timeline (8 Coherence ÷ ~3/op-season → crisis ≈ season 3), confirming the *practitioner* loop is the compound's fastest hand even though it's the weakest at causing faction collapse. The phase coupling (Coherence crisis season ≈ 3 driving the RS→Stab pressure spike) is real; its *magnitude* is not.

---

## §4 — Canonical couplings used (cited)

- **Trigger 5** — `faction_layer_v30` Trigger 5 three-condition gate, verbatim (A: Mil pool ≥ 4; B: net ≤ 0 Failure, Partial excluded; C: net ≤ −2 OR pool ≥ 6 OR officer lost). Costs −1/−2 (+1 officer killed). **This is the load-bearing canon for §1.**
- **L7** — `faction_layer_v30` Wealth-0: "Military −1 at each subsequent Accounting while Wealth = 0; Military does not auto-recover."
- **Collapse** — `faction_layer_v30` ED-675: Stab 0 at Accounting end → Mandate 0, territories Uncontrolled, units Masterless.
- **Muster** — `military_layer_v30` §A.13: unit Power = floor(Military/2)+1, Wealth-gated.
- **Mass battle** — `mass_battle_v30` PP-233: Pool = min(Size,Cmd)+Cmd (MB5 no-floor); damage = successes×(1+Power); Morale rout.
- **Threadwork** — `threadwork_v30`: Structural op −2 Coherence; Coherence 0 → Rendering Crisis arc (Pool ≈ Close-Knot Bonds vs Ob 3; success → Coherence 3, else NPC); Substrate Saturation cap.
- **Domain Echo** — `scale_transitions_v30`: Success +1 / Overwhelming +2 faction stat, cap ±2.
- Die rule, Ob = floor(stat/2)+1: `params/core.md`, F2-ruling.

---

## §5 — What this sim CANNOT answer (honest negative result)

**The compound P(collapse) magnitude is assumption-dominated and I decline to report it as a finding.** Evidence:

1. **The recovery mechanic is not canonically specified in what I read.** `faction_layer_v30`'s Accounting Stability recovery — the per-season +Stab that opposes the loss pressures — was not in the sections I fetched (the `[A1]` assumption). I modeled two versions: a "free" roll (Stab climbs to 7, unrealistic) and a "conditional" consolidate (recovery withheld while besieged). **The two give materially different collapse rates, and the conditional version fails its own sanity check** — a strong faction under zero pressure collapsed ~21%, which is impossible. That means my conditional model is *too punitive*, the free model is *too generous*, and the true mechanic is between them and **unread**. The collapse magnitude is therefore a function of an unmodeled rule, not of the compound dynamics.

2. **The ER-9 counterfactual inverted under both recovery models** — "aggregate the pool" produced *higher* modeled collapse — because aggregation changes battle outcomes, which changes the `besieged` flag, which my broken recovery gate keys on. That inversion is a pure artifact of the unspecified recovery model, not a result about aggregation. **I therefore cannot use this sim to confirm or deny that ER-9 rescues the compound case** (the engine-reconciliation recommendation stands on the §1 / armature evidence, not on this sim).

3. **Two couplings are qualitative in canon, not formulas.** [A2] territory→muster and [A3] RS→Stability have no read numeric law; I parameterized and swept them. The structural finding (§1) doesn't use them; the magnitude (§3) does.

**This is the correct scientific outcome, not a failure of the run:** the sim *definitively* answers the structural question (Trigger-5 decoupling + non-monotonic exposure, §1) and *definitively identifies* that the magnitude question is blocked on an unread/unspecified recovery mechanic. Shipping collapse percentages here would be exactly the "confidently-wrong number" failure this session has repeatedly caught (F1 twice, the die-rule error). I am not shipping them.

---

## §6 — Findings & next steps

| # | Finding | Confidence | Status |
|---|---|---|---|
| **CC-1** | Trigger-5 exposure is **non-monotonic in faction strength**; a `pool ≥ 6` cliff in Condition C jumps battle→Stability exposure **8.7×** at Cmd 2→3. Mid-tier (Cmd 3) factions are *most* exposed; the weakest are shielded by Conditions A+C. | **high** (recovery-independent) | NEW — ledger candidate |
| **CC-2** | The compound spiral does **not** amplify into determinism; the battle→faction edge is starved at the input (weak factions rarely fire Trigger 5), correcting my earlier "deterministic/loss-weighted" hand-trace. | **high** (structural) | corrects prior diagnostic |
| **CC-3** | Practitioner/Coherence is the compound's *fastest* loop (crisis ≈ season 3) but weakest at causing *faction* collapse (RS→Stab coupling qualitative). | medium (direction only) | informational |
| **CC-4** | **Faction Accounting Stability-recovery mechanic is unspecified / unread** — and it dominates every collapse-magnitude question. Until specified, no faction-collapse-rate sim is trustworthy. | high (negative result) | **PREREQUISITE — blocks magnitude sims** |

**Ledger candidate (staged, not filed — JSONL migration owns the ledger):**
- CC-1 → new P2: Trigger-5 Condition C stacks a pool-size cliff (≥6) on a magnitude threshold (net ≤ −2), making a single Command point (2→3) jump battle→Stability exposure 8.7×. Consider smoothing (e.g. severity scaled by margin rather than a hard pool≥6 auto-fire). Hand off to the same consolidation queue as ED-868..873.
- CC-4 → flag for Jordan: locate or specify the canonical Accounting Stability-recovery mechanic; it is the missing damper that every collapse analysis (this sim, F3, F5, F6) implicitly depends on.

`[CONFIDENCE: high]` — §1 (CC-1/CC-2) and §5 (CC-4 negative result). `[CONFIDENCE: medium]` — §2/§3 directional. **No collapse-magnitude percentages reported, by design.**
