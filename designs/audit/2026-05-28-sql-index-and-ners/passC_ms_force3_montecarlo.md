# Pass C — MS / Force-3 Empirical Validation

**Date:** 2026-05-28. **Task:** audit. Monte-Carlo (N=5000/scenario) on the MS-trajectory model.
**Status of inputs:** base rates cited from Pass B (`passB_master.md`); the per-season *tearing intensities* (μ per scenario) and the Force-1 calibration are **ILLUSTRATIVE** — flagged below. The structural conclusions hold across plausible parameterizations; exact pacing needs the repo's `mc` engine with calibrated tearing distributions. `[CONFIDENCE: high on structure; low on absolute pacing numbers.]`

Model per season: `ΔMS = Force1(MS) − tearing`, clamped `≥ −10` (the contested cap, under test), MS∈[0,100]. Maintain overlay: WC2 halves tearing, WC3 +2/s, Sanctuary +1/s (params §WC).

`[CORRECTION of my batch-4 claim]` — Force 1 is **small** (+13 over 257 yr ⇒ ~0.05–0.35/s, larger at low MS). I'd called it the primary damper; it is **not**. It enables recovery-when-idle and slightly decelerates decline, but the **−10/s cap is what enforces the guardrail.**

---

## Results

**Q1 — does the cap enforce the 4-season guardrail?** Sustained climax tearing:
- from **MS 60 → MS≤5: median 6 seasons** (P5=P95=6 — tight, because tearing always clamps to −10).
- from the **Fragile floor MS 40 → MS≤5: median 4 seasons.**
→ **Guardrail satisfied exactly.** 55 points ÷ 10/s ≈ 6; 35 ÷ 10 ≈ 4. The cap is the binding constraint; the tight distribution confirms heavy threadwork is always at the ceiling.

**Q2 — arc pacing.** Composite peace→escalation→climax → MS≤5: median **21 seasons (~5 yr)** at escalation μ5/s; **33 seasons (~8 yr)** at the softer μ3/s. *But in both, MS is already Fractured (~8–10) at climax onset* — the escalation phase drives most of the decline; the climax is brief. **Pacing is highly sensitive to escalation-phase tearing intensity.** For the climax to *be* the dramatic crash (MS still ~30–40 entering it), escalation tearing must be mild — a calibration target, not settled here.

**Q3 — is the maintain path winnable?** Maintain (WC) from MS 20, over 30 seasons:
| Tearing during maintain | MS after 30s | stayed >5 |
|---|---|---|
| peace ~1/s | **100** (full recovery) | 100% |
| escalation ~5/s | **37** (recovers) | 100% |
| **climax ~14/s** | **0** (crashes) | **0%** |

**Break-even:** WC maintain nets **positive below ~6.5/s raw tearing, negative above** (μ6 → +0.3/s; μ7 → −0.2/s). Climax (14/s) is far above → maintain fails.

---

## Refined Force-3 bound (empirically backed)

1. **The −10/s net-loss cap is the guardrail** (not Force 1). It makes climax MS40→≤5 take ≥4 seasons — exactly Jordan's floor — and makes the timing near-deterministic under heavy tearing. *Adopt the cap as the explicit Force-3 guardrail* (resolving the ED cap-contradiction toward the cap, as the guardrail requires).
2. **The multiplier has teeth and is bounded.** Heavy Foundational/Structural threadwork saturates −10/s (crashes MS in ~6s from 60); warfare alone (−3/s) → ~20s and cannot approach the ceiling. Exactly the lock: threadwork is the crash driver, warfare can't.
3. **Pacing for the intended civil-war→invasion→unification arc is a calibration job** for the real sim: tune escalation-phase tearing so MS enters the climax still in Fragile/Fractured, letting the climax deliver the final crash. My run shows the arc is ~5–8 years; the shape depends on escalation intensity.

---

## NEW FINDING (P2, design) — "winnable on maintain" requires *de-escalation*, not just WC

WC mitigation (halve tearing + ~3/s healing) **breaks even at ~6.5/s raw tearing.** So:
- Maintain **wins** if the player **reduces tearing below ~6/s** (ends wars, stops heavy threadwork) — then MS recovers (fully at peace, partially at escalation) and the Calamity-site Mend becomes pursuable.
- Maintain **fails** if the player keeps tearing at climax intensity — WC only slows the crash.

This is coherent (you cannot tear reality apart and maintain it at once) and worth stating as canon: **the maintain victory is "de-escalate + heal," not "out-heal heavy tearing."** *Owner decision:* if you intend maintain to be survivable *even under* sustained heavy tearing, the WC mitigation needs strengthening (raise the WC3/Sanctuary rate, or make WC2 a larger reduction) — a balance lever, flagged not chosen. Staged ED (`[DRIFT]`, B6):
```yaml
- id: ED-<next>  severity: P2  system: threadwork / Warden Cooperation / MS
  type: balance_finding
  summary: WC maintain mitigation (WC2 halve + WC3 +2/s + Sanctuary +1/s) breaks
    even at ~6.5/s raw tearing; fails against sustained climax-intensity tearing
    (~14/s). Maintain victory requires de-escalation, not WC alone.
  decision_needed: Confirm "maintain = de-escalate+heal", or strengthen WC mitigation
    so maintain survives heavy tearing.
  status: open
```

---

## Feeds the MS-system NERS (Pass C remaining)
- **R (Robust):** the MS engine holds at its extreme (small-pool/low-MS) — the cap prevents single-Accounting Rupture and the 4-season floor; **passes R given the cap**. Without the cap (params/PP-603 reading), it would fail R (instakill possible) — *the ED cap decision is load-bearing for the NERS verdict.*
- **S (Smooth):** Force-1 + tearing + cap compose cleanly across scales; geographic radiation (calamity_radiation) graduates by distance — smooth.
- **E (Elegant):** two forces + one cap + per-scale drains — simple to reason about; **the maintain-requires-de-escalation property is intuitive** (don't tear what you're mending).
- **N (Necessary):** the cap is necessary (guardrail); Force 1 is necessary (recovery path + Catastrophe-to-now history). Nothing redundant.

Remaining Pass C: rebuild the loop map from `passB_master §4`; scale-ladder re-anchor (DC-7); per-system NERS write-ups (faction-collapse passes R — no Lesson 5; faction-action small-pool bare-stat fails R — Lesson 3; L-DEFECT/L-INSURG fail R on incompleteness); fold DC-1..12. Then, for true pacing numbers, run the repo `mc` engine with canonical tearing distributions.
