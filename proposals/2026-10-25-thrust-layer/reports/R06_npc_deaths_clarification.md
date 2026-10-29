# R06 — Does "94% end with both principals alive" mean NPC deaths

## Status: REFERENCE — HELD BACK IN FULL

> **Reference — PROPOSED, HELD BACK IN FULL.** Merging the PR that carries this file ratifies nothing in it (ED-1094's default is not applied). Delivered in chat during the session of 2026-10-24/25 and reproduced verbatim, except that session-scratchpad paths are rewritten to their committed locations. Figures were taken **before** the register's measurements (`../01_MISSING_IN_CODE.md` §2, probes P1–P12); where they differ, `../02_MAJOR_TAKEAWAYS.md` §9 (Corrections) governs.

**Asked by the user:**

> "94% of runs end with both principals alive."
> 
> you don't mean NPC deaths, do you?

---

**In the toy world, yes.** "Dead" means the actor was removed from the run. The 94% figure comes from the situation-only arm, where no climax was built to kill. The decisive-form arms I then praised do kill: one principal dies in every run. That matters more than my last answer let on.

| Arm | Principals dead per run | Arc minus shuffled null | Complete beats |
|---|---|---|---|
| Bottom-up | 0 | −0.02 | 0.11 |
| Decisive-form set piece, lethal climax | 1.00 | +0.14 [+0.09, +0.20] | 0.67 |
| Same, loser exiled but alive | 0.02 | +0.01 [−0.03, +0.07] | 0.73 |
| Same, settled by pact | 0.05 | +0.03 [−0.02, +0.08] | 0.74 |
| Ladder + decisive form, lethal | 1.00 | +0.20 [+0.13, +0.26] | 0.79 |
| Ladder + decisive form, pact | 0.04 | +0.03 [−0.02, +0.10] | 0.81 |
| Ladder + tribunal | 0.00 | +0.09 [+0.03, +0.15] | 0.43 |

- **The ordering signal depends on the death.** Without it, the signal disappears. Complete beats stay high, so the beat structure survives, but the arc test fails.
- **Why:** a lethal climax leaves the principals' thread silent afterward (0.00 intensity after season 22). A living loser keeps acting (1.27 average). My test requires that post-peak fall, so part of this is an artifact of the test's definition of an arc ending.
- **The tribunal arm kills no one.** It keeps its signal, so a non-lethal closure that actually works exists in the toy.
- **The toy is violent on its own.** Even bottom-up loses 4.4 of 24 actors per run, which I calibrated only to a survivor share. The deaths-per-run figures are toy-scale. In Valoria the cast is closed and authored (ED-WR-0011), so every death is a permanent loss.

[CORRECTION: my last answer headlined the decisive-form set piece as matching the forcing director without dictating outcomes. That holds only for the lethal climax. The form dictates that someone dies, though not who.]
[CONFIDENCE: low-medium — I ran this once in a toy of my construction, and I printed the output without saving it.]

The code is `proposals/2026-10-25-thrust-layer/toy/regimes8.py`.
