# R04 — Is ladder plus threshold-raised tribunal the best?

## Status: REFERENCE — HELD BACK IN FULL

> **Reference — PROPOSED, HELD BACK IN FULL.** Merging the PR that carries this file ratifies nothing in it (ED-1094's default is not applied). Delivered in chat during the session of 2026-10-24/25 and reproduced verbatim, except that session-scratchpad paths are rewritten to their committed locations. Figures were taken **before** the register's measurements (`../01_MISSING_IN_CODE.md` §2, probes P1–P12); where they differ, `../02_MAJOR_TAKEAWAYS.md` §9 (Corrections) governs.

**Asked by the user:**

> Ladder + threshold-raised tribunal
> 0.38
> +0.09 [+0.04, +0.15]
> 0.85
> 0.43
> none
> 
> 
> is this the "best"?

---

**No.** It leads on one criterion only, and I haven't shown it's best overall.

**Where it leads.** Arc rate with no outcome written: 0.38, with an ordering signal of +0.09 [+0.03, +0.15]. The scripted director scores 0.35 and +0.10, a statistical tie, and it forces outcomes.

**Where it doesn't lead** (base world, 300 seeds):

| Property | Leader | Ladder + tribunal |
|---|---|---|
| Motive legibility (outlasts the moment) | ambition alone 0.80, ladder alone 0.72 | 0.43 (same as bottom-up) |
| Thread continuity | bottom-up 0.77, ambition alone 0.78 | 0.58, the lowest of the six arms |
| Complete beats | scripted director 0.76; tribunal alone 0.55 | 0.43 |
| Survives 80% refusal | scripted director 0.71 | 0.21 |

**What undercuts the lead**
- **It depends on the threshold I picked.** The ordering signal holds for thresholds 4.5 to 10 (+0.13, +0.09, +0.11). At 3 it weakens (+0.05, interval spans zero) and at 16 it is gone (−0.01).
- **Closure is mostly one template.** In 192 of 293 runs with a closing event, the main thread closes on a tribunal ruling. At threshold 6, a third of the chronicle beats are rulings, about 12.6 per run. Structural variety (39 to 56 distinct signatures per ~295 runs) is no better than the scripted director's (84). I can't call that variety.
- **My own process inflates it.** I designed this arm after seeing the earlier results, and I compared roughly twenty arms and variants. The intervals are per-comparison, with no multiple-comparison correction.
- **The measure is limited.** The arc test is a three-act template, and it passes a lone closing event. Only the shuffled-null comparison speaks to ordering.

**The ladder alone has a separate merit.** Without the tribunal, it multiplies cross-person causal chain depth by about 2.7 over bottom-up (62.5 against 23.0) and keeps legibility at 0.72. Those two properties may matter more to you than arc rate.

No arm dominates. The honest framing is a trade-off between ladder alone (legible, deep causal chains, weak arcs), ladder plus tribunal (arcs without forcing, thinner "why", threshold-sensitive) and the scripted director (best beats and robustness, injects outcomes). Which one is best depends on how you weight those properties, and the toy can't weight them for you.

[CONFIDENCE: low — one toy world of my construction, no human readers, and an arm chosen after seeing results.]

Raw output is in `proposals/2026-10-25-thrust-layer/toy/exp_ladder_out.txt`. I did not save the threshold-sensitivity and per-property run to a file.
