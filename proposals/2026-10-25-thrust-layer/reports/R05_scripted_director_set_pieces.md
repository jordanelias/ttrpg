# R05 — A scripted director that injects set pieces rather than outcomes

## Status: REFERENCE — HELD BACK IN FULL

> **Reference — PROPOSED, HELD BACK IN FULL.** Merging the PR that carries this file ratifies nothing in it (ED-1094's default is not applied). Delivered in chat during the session of 2026-10-24/25 and reproduced verbatim, except that session-scratchpad paths are rewritten to their committed locations. Figures were taken **before** the register's measurements (`../01_MISSING_IN_CODE.md` §2, probes P1–P12); where they differ, `../02_MAJOR_TAKEAWAYS.md` §9 (Corrections) governs.

**Asked by the user:**

> "ladder plus tribunal (arcs without forcing, thinner "why", threshold-sensitive)"
> 
> and what if the scripted director didn't dictate outcomes but injected set pieces

---

**Verdict.** It works if the set piece has a decisive form. As a situation alone, it does nothing. In the toy world, set pieces that conclude by contest, with the winner left to dice and skill, matched the forcing director on arcs without dictating who wins.

| Arm | Arc rate | Arc minus shuffled null | Complete beats | Motive outlasts the moment | Arc rate at 80% refusal |
|---|---|---|---|---|---|
| Bottom-up | 0.09 | −0.02 | 0.11 | 0.43 | 0.19 |
| Set piece, situation only (relocate, engagement window) | 0.07 | −0.04 [−0.07, −0.01] | 0.11 | 0.42 | 0.17 |
| Same, with stakes multiplied | 0.01 | −0.07 | 0.07 | 0.10 | 0.08 |
| Set piece with a decisive form | 0.33 | +0.14 [+0.09, +0.20] | 0.67 | 0.27 | 0.81 |
| Same, flat stakes | 0.26 | +0.11 | 0.17 | 0.28 | 0.41 |
| Ladder + decisive-form set pieces | 0.41 | +0.20 [+0.14, +0.26] | 0.79 | 0.45 | 0.85 |
| Ladder + tribunal (the earlier arm) | 0.38 | +0.09 | 0.43 | 0.43 | 0.21 |
| Forcing director | 0.35 | +0.10 [+0.04, +0.16] | 0.76 | 0.23 | 0.71 |

- **Situation alone fizzles.** With a venue and an engagement window but no conclusive form, 94% of runs end with both principals alive. Arc rate is no better than bottom-up, and the ordering signal is slightly below chance.
- **The decisive form is what restores arcs.** The director authors a best-of-rounds contest at the venue, lethal at the climax. Dice and skill pick the loser. The protagonist wins 64% of climaxes, and no outcome is forced. It stays within 0.02 of the forcing director on arc rate (interval spans zero) and beats it on the ordering signal.
- **Escalating stakes carry much of it.** With flat stakes, complete beats fall from 0.67 to 0.17 and the arc rate from 0.33 to 0.26. The cost is that the director now writes intensity. In a quiet world the main thread's peak is 7.65, against 2.36 for bottom-up.
- **Adding the ladder helps.** The arc rate is 0.41, and the "why" recovers from 0.27 to 0.45. It still falls short of the 0.55 I predicted. The contest events carry an occasion motive, not an ambition.
- **You have traded the dictated outcome for dictated form and stakes.** In the repo's terms, this is an authored occasion that is not declinable. It sits between the lawful occasion and the refused scripted beat.

**Treat two results with suspicion.**
- **The 80% refusal result is likely an artifact.** My toy contest uses its own dice and bypasses the act layer, so refusals can't touch it. In the real engine, scenes resolve in the ordinary engines, which refuse.
- **The predictions were registered after I saw the first set-piece variant fizzle,** then run blind. 9 of 10 were confirmed, and the one miss was the "why" threshold.

[GAP: declinable set pieces, mid-run stake adjustment and any human reading of the results were not tested.]
[CONFIDENCE: low-medium — one toy world of my construction, and the arc test credits a lone closing event at any season.]

Raw outputs are in `proposals/2026-10-25-thrust-layer/toy/`: `exp_setpiece_out.txt`, `exp_contest_out.txt` and `regimes7.py`.
