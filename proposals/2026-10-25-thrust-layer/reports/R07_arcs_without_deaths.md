# R07 — Arcs without NPC death; making death rare, fighting authority hard, killing consequential

## Status: REFERENCE — HELD BACK IN FULL

> **Reference — PROPOSED, HELD BACK IN FULL.** Merging the PR that carries this file ratifies nothing in it (ED-1094's default is not applied). Delivered in chat during the session of 2026-10-24/25 and reproduced verbatim, except that session-scratchpad paths are rewritten to their committed locations. Figures were taken **before** the register's measurements (`../01_MISSING_IN_CODE.md` §2, probes P1–P12); where they differ, `../02_MAJOR_TAKEAWAYS.md` §9 (Corrections) governs.

**Asked by the user:**

> ...review the arcs that we had generated. an arc does not need an NPC to die. we want an NPC death to be an extremely rare event, and we want to make it hard to even FIGHT anyone with authority/standing
> (sent mid-turn) or at least make the consequences of killing significant

---

**Verdict.** Arcs don't need deaths, but most of what I generated did lean on them. Under your constraints, one arm kept a strong ordering signal and the old tribunal route did not.

**Review of the arcs already generated**
- Among runs that passed the arc test, the main thread closed on a death in 99% of runs for the forcing director, 94% for the lethal set piece and 98% for the ladder with a lethal set piece. The ladder-plus-tribunal arm was 3%. In the lethal arms, every run killed one principal.
- Fighting people with standing was common: 19–36% of harm events hit someone holding a prize.

**Constrained world** (300 seeds per arm; the world is my construction)

| Arm | Deaths per run | Harm aimed at standing | Arc minus shuffled null | Complete beats |
|---|---|---|---|---|
| Bottom-up | 0.36 | 0.08 | −0.06 [−0.08, −0.03] | 0.08 |
| Ladder | 0.30 | 0.13 | −0.02 [−0.06, +0.02] | 0.16 |
| Ladder + tribunal | 0.28 | 0.12 | +0.01 [−0.05, +0.07] | 0.36 |
| Forcing director, forced yield | 0.41 | 0.09 | +0.10 [+0.04, +0.16] | 0.77 |
| Decisive-form set piece, bound peace | 0.33 | 0.08 | +0.02 [−0.02, +0.05] | 0.12 |
| Ladder + decisive form, bound peace | 0.24 | 0.13 | +0.24 [+0.19, +0.30] | 0.52 |
| Same, lethal climax, consequences on | 1.20 | 0.13 | +0.29 [+0.24, +0.35] | 0.54 |

- **What I changed.** Death needs a skill-1 target and a 1% roll. Harm against a standing-holder is refused 90% of the time unless provoked, and the usual weapon becomes an accusation (a contest of standing). Settlements bind a peace for eight seasons.
- **The ladder carries the result.** The ladder with a decisive-form set piece and a bound peace is the only arm with a strong signal and the lowest death rate. The decisive-form set piece without the ladder shows no signal.
- **Ladder + tribunal does not transfer.** Its earlier +0.09 disappears under the constraints.
- **Bottom-up falls below chance,** at −0.06 [−0.08, −0.03].
- **The ladder survives the gate.** 96% of ambitions meet at least one goal.

**Making killing heavier.** I tested a killing at season 10 in the ladder-plus-tribunal world, paired against the same seed without it. The consequence package is grievance in kin and faction, witnesses turning on the killer, forfeiture of holdings, infamy and vacated holdings.
- About 9.5 acts target the killer, from about 4.9 distinct actors.
- About 1.3 tribunals name the killer, and the killer's repute ends at about 4.3.
- There are no extra deaths, so no runaway feud.
- The world is still about 7 events quieter, because the victim's activity is lost.
- Giving the victim's kin a standing "avenge" ambition added nothing measurable (+0.5 acts).
- That is moderate, not significant by your standard. A trial, succession politics for vacated offices and a longer feud are the obvious next mechanisms, and I haven't built them.

**Real-engine note.** `fight` requires only existence and co-location. Its `Felled` band deletes the person and emits `person.died`, and the "deontological gate" the row mentions does not exist yet (`verb_table.yaml`, row `fight`). Both of your rules would be new work there.

[ASSUMPTION: "standing" in the toy is holding a prize, and the 90% gate is my setting. I did not sweep the gate strength.]
[CONFIDENCE: low-medium — the constrained design came after seeing the results. Only 3 of 7 pre-registered predictions held. The misses were harm on standing slightly above 0.10, bottom-up significantly below chance rather than at it, and the peace helping only in the ladder arms.]

Files are in `proposals/2026-10-25-thrust-layer/toy/`: `regimes10.py` and `exp_con_out.txt` are saved. The review table and the killing-at-season-10 runs were printed, not saved.
