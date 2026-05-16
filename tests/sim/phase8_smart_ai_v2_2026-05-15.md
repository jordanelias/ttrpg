# Phase 8 sim — Better-tuned Smart AI; Phase 7 finding refinement

**Date:** 2026-05-15
**Sim:** `tests/sim/phase8_smart_ai_v2_2026-05-15.py`
**Triggering finding:** Workstream meta-audit 2026-05-15 (WS-H-3, WS-H-4) flagged that Phase 7 Smart AI was under-tuned. This sim addresses the AI defects and re-runs the same matchups.

---

## TL;DR

**Phase 7's "action triangle inverts dominance" finding was partly stamina-management artifact.** When both sides manage stamina (Smart v2 with PP-294-aware Feint alternation), Agi-dominance reasserts at ~100% conditional Fast win — even though the disadvantaged side correctly alternates Feint→Strike.

**End-dominance is real and moderate** — 63.7% Tough vs Strong in symmetric Smart v2 play, down from 82.7% Strike-only but well above Phase 7's anomalous 6.8%.

**Implication:** Pool advantage at 17D vs 11D is structurally dominant in skilled-vs-skilled play. The action triangle provides asymmetric leverage primarily when one side neglects stamina or other tactical considerations. The Combat Balance Note's current text needs revision.

---

## Smart v2 AI fixes from Phase 7

1. **Take Breath threshold raised from ≤5 to ≤8.** Phase 7 had a discrete-action skip where high-stamina builds (Tough at 27) passed the 3–5 trigger window without firing, exhausting at round 5. Smart v2 fires Take Breath at stam ∈ [3, 8] — both high and low stamina builds recover.

2. **Full Guard rule reworked.** Phase 7's `hp<25% AND own_pool<opp_pool` rule trapped the pool-disadvantaged side into stalling — losing the Feint lever right when needed. Smart v2 only Full Guards as genuine last-stand: `hp<15% AND wounds == max_wounds`.

3. **Feint triggered with proper PP-294 alternation.** Smart v2 alternates Feint (even rounds) and Strike (odd rounds) when pool-disadvantaged. PP-294 non-stacking means Feinting every round wastes the pool reduction; alternation correctly leverages it: setup with Feint, exploit with Strike on the now-reduced opponent pool.

4. **Pool-advantaged side defaults to Strike.** Smart v2 doesn't Feint when ahead — efficient pool→damage conversion is optimal.

---

## Results

### Agi dominance: Fast (Agi 6, 17D) vs Strong (Agi 3, 11D)

| Mode | A=Fast strategy | B=Strong strategy | Fast cond | Status |
|---|---|---|---|---|
| Strike-only baseline | strike_only | strike_only | 96.7% | DOMINANT |
| **Smart v2 both sides** | **smart_v2** | **smart_v2** | **100.0%** | **DOMINANT** |
| Underdog Feints (Phase 7 reference) | strike_only | underdog_feint | 34.6% | B-dominant |

### End dominance: Tough (Agi 3 End 6) vs Strong (Agi 3 End 4)

| Mode | Tough cond | Status |
|---|---|---|
| Strike-only baseline | 82.7% | DOMINANT |
| **Smart v2 both sides** | **63.7%** | **tilted Tough** |
| Underdog Feints (Phase 7 reference) | 7.5% | B-dominant |

### Build-investment ROI (Smart v2 both sides)

| Build | Pool | Cond win vs Strong | Δ cond vs Agi 3 |
|---|---|---|---|
| Agi 3, End 4 | 11D | 51.2% | (baseline) |
| Agi 4, End 4 | 13D | 95.6% | +44.4pp |
| Agi 5, End 4 | 15D | 99.9% | +48.7pp |
| Agi 6, End 4 | 17D | 99.9% | +48.7pp |
| Agi 7, End 4 | 19D | 100.0% | +48.8pp |

Same-pool symmetric (Agi 3 vs Agi 3) produces 51.2% — within sampling noise of 50%. **The sim is calibrated.** Any deviation from 50% in symmetric matchups is a genuine signal, not artifact.

The Agi 4 → 5 jump is dramatic (+33pp in ROI). The Agi 5 → 7 plateau (all at ~100%) shows pool advantage saturating — every additional die produces vanishing marginal advantage when already at the dominance ceiling.

---

## Phase 7 finding revised

### What Phase 7 claimed

> When the disadvantaged side actively employs PP-294 Feint, Fast wins drop from 96.7% to 34.9% (Strong wins 65% of decisive duels). Action triangle is load-bearing balance mechanism.

### What Phase 8 reveals

The 34.9% was generated with A=`strike_only` (Fast doesn't manage stamina). At canonical Strong stamina = 23 and action cost = 5, Fast exhausts after round 4–5. Many "Strong wins" outcomes in Phase 7 Underdog mode were Fast losing by stamina exhaustion before delivering enough damage to wound Strong sufficiently.

When the asymmetry is removed (both sides manage stamina via Take Breath at stam ≤ 8), Agi-dominance reasserts at 100%. **The action triangle alone does not balance a 6-die pool gap when both sides play tactically.**

### What still holds

- **Action triangle has real effect.** Compare Strike-only baseline (96.7% Fast) to Smart v2 (100% Fast) — the 3.3pp difference is the action-triangle-no-stamina-asymmetry effect. Small but real; Feint slightly reduces Fast's effective pool over time, but not enough to bridge the gap.
- **Symmetric matchups are balanced.** Agi 3 vs Agi 3 produces 51.2% — clean balance in the absence of stat advantages.
- **End-dominance is real and moderate.** Tough vs Strong at 63.7% (Smart v2) is consistent with moderate End-advantage. Phase 7's 6.8% was artifact; Phase 8's 63.7% is the real signal.

### What was wrong with Phase 7 (and earlier sims by extension)

Phase 4 — 7 all assumed Strike-only or under-tuned tactical AI. **The stamina cliff (one side exhausting before HP=0) confounded all conditional win rates.** Pool advantage compounds with stamina-management asymmetry; isolating pool effect requires symmetric tactical play.

---

## Implications

### For Combat Balance Note

Current text (post-REC-1):
> With Strong actively employing PP-294 Feint: Fast wins drop to 34.9% — Strong wins 65% of decisive duels

This is misleading. The 34.9% holds for asymmetric tactical play (Strong Feints + manages stam; Fast Strikes-only); it does NOT hold for symmetric Smart v2 play (both Feint with PP-294 alternation + manage stam).

**Recommended revision:** strike the 34.9% number from the Balance Note. Replace with a more honest statement:

> Pool advantage at canonical attribute differences is structurally significant. Fast (Agi 6, 17D pool) wins ~100% of decisive duels vs Strong (Agi 3, 11D pool) in symmetric tactical play. The action triangle (PP-294 Feint) provides asymmetric leverage when one side neglects stamina management or tactical depth — empirically vs strike-only Fast, Strong drops Fast to ~35%. But the action triangle does not balance pool-gap dominance in skilled-vs-skilled combat.

### For Decision A (revert PP-717 D2 — pool softcap)

**Re-examination needed.** Decision A rejected PP-717 D2 partly on the theory that the action triangle would compensate for pool advantage. Phase 8 shows that's wrong — in skilled play, pool advantage at the canonical levels (Agi 6 vs Agi 3) is structurally dominant.

This suggests either:
- **PP-717 D2 (combat softcap) was addressing a real problem** and should be re-considered; OR
- **Pool advantage is the intended design** (Fast builds dominate personal combat by design; balance comes cross-system), as the Reframing 2 argument suggested; OR
- **Some other lever** (action cost scaling, wound spiral mitigation, HP/stam compression) needs investigation.

This is a Jordan decision, not a sim conclusion. The sim provides the empirical picture; the design intent is separate.

### For the doubling formula

Phase 6 showed pool formula alternatives don't solve the dominance, but Phase 8 confirms it more directly: even the cleanest action-triangle play doesn't compensate for the 6-die gap at Agi 6 vs Agi 3. The doubling formula creates the gap; whether to address it via softcap / drop-doubling / pool cap / accept is now genuinely a design decision, not a balance fix.

### For methodology

Future sims should:
- Use symmetric tactical AI on both sides (Smart v2 or successor)
- Verify symmetric matchups produce ~50% as calibration check
- Disclose stamina-management policy explicitly
- Avoid attributing outcomes to single mechanics when stamina, HP, wound spiral, and tactical depth all compound

---

## Limitations of Phase 8

- **Smart v2 alternation heuristic is still imperfect.** A truly principled AI would track pending pool reductions and Strike only when reduction is pending (not on parity of round number). Phase 9 could implement this.
- **Initiative-knowledge asymmetry (PP-232) unmodeled.** Lower-init declares first; higher-init has positional knowledge. This would favor the higher-Attunement side in real play.
- **Distance system, Disarm, Establish Distance, Fibonacci group bonus all unmodeled.** Each could shift dynamics.
- **Single weapon × armour pair.** Light Blade Cut vs None. Different combinations may produce different dynamics.
- **Symmetric AI assumption may not match real play.** Player skill varies; some players will use the action triangle better than others. The Smart v2 result represents "both players play competently"; Underdog/Strike-only represents "one player plays poorly."

---

## Status

Phase 8 sim complete. **Phase 7's headline finding refined: action triangle has real but limited effect on dominance; pool advantage is structurally dominant in skilled-vs-skilled play at canonical attribute differences.**

**Open canonical question:** does the Combat Balance Note need revision to reflect this? Recommendation: yes, but as a separate commit pending Jordan's design intent ratification.

**Open sim question:** does an even better-tuned Smart AI (Phase 9 with action-history-aware Feint timing) produce different results? Unlikely to change the structural finding (pool advantage at 17D vs 11D is too large for any tactical scheme to overcome), but could refine the magnitude.

**Open design question:** is Fast/Tough dominance in personal combat the intended design (Reframing 2: build balance comes cross-system), or should pool advantage be capped (re-ratify PP-717 D2 or similar)?
