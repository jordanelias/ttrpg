# R10 — Major takeaways, as first delivered

## Status: REFERENCE — HELD BACK IN FULL

> **Reference — PROPOSED, HELD BACK IN FULL.** Merging the PR that carries this file ratifies nothing in it (ED-1094's default is not applied). Delivered in chat during the session of 2026-10-24/25 and reproduced verbatim, except that session-scratchpad paths are rewritten to their committed locations. Figures were taken **before** the register's measurements (`../01_MISSING_IN_CODE.md` §2, probes P1–P12); where they differ, `../02_MAJOR_TAKEAWAYS.md` §9 (Corrections) governs.

**Asked by the user:**

> okay. so. what are the major takeaways from this session for improving game

**Expanded and corrected in `../02_MAJOR_TAKEAWAYS.md`.** The first delivery's figures for refusals, wrong-kind formation, the "51 of 803" ambition count and the 46-case classification are superseded there (§9); its statement that candidate typing "sits in no workplan" is wrong (H-156).

---

**Before anything else, make the existing verbs actually execute.** Every narrative design from this session sits on a substrate that mostly fails. The rest of the takeaways are ranked below that.

1. **Fix refusals first.**
   - In the one measured run (one seed, two seasons), 929 of 1,318 acts were refused (70.5%), and 33% targeted a subject of the wrong kind.
   - `determine` was refused 7 of 7, `confer` 4 of 4 and `commit` 74 of 74.
   - The deepest cross-person chains I rendered from the real engine over seeds 0–5 were 81% refusals (66 of 81 acts, by the proposal's suffix definition, which over-counts degree bands).
   - Top-down, bottom-up and hybrid designs all depend on closing acts like these.
   - [repo reading + my chronicle runs; the candidate-typing decision is unruled and sits in no workplan]
2. **The world needs a motive layer, and part of it is already there.**
   - Bottom-up gave causal depth without a "why". In the toy, standing ambitions raised motive depth from 0.43 to 0.80.
   - In the real engine, the ambition question won only 51 of 803 deliberations.
   - 24 of the 38 goal rows are orientation-only and mint no Proposition, so those organizations produce no thrust at all.
   - [repo + toy]
3. **Arc shape needs two things together: a goal ladder under each ambition, and a closure form.**
   - The ladder alone added cross-person chain depth (about 2.7 to 3.3 times) but no ordering signal.
   - Closure alone, without the ladder, showed none either.
   - Together, a ladder plus a decisive-form set piece with a bound peace gave arc minus null of +0.24 [+0.19, +0.30].
   - That arm killed 0.24 people per run.
   - Closure through settlement works; a plain exile does not (+0.01).
   - [toy, low confidence]
4. **Killing has no consequences today.**
   - The cast is closed, so every death is permanent.
   - A death never reaches anyone's questions (H-209), and a dead holder's seat is named by no claim (H-206).
   - `fight`'s `Felled` band deletes the person, and the "gate" that would make fighting authority hard guards 3 of 31 seats.
   - [repo reading]
5. **Don't build the tempting things.**
   - Lookahead-biased choice flipped 32% of leveraged decisions, cut explained motive, showed no ordering signal and cost about 270 times the run time.
   - A blind script violated world constraints in 96% of runs.
   - A forcing director gets its arcs by dictating a death.
   - [toy]
6. **The deepest premise is the least buildable.**
   - Healing the Calamity has no act.
   - Hiding the threadwork truth has no goal row.
   - Caste has no readable store.
   - Weather, ageing and hunger ship dark, so the world is quiet by construction.
   - [repo reading]
7. **Authoring is the largest content job.**
   - By my hand classification, 28 of the 46 character cases have no authored terminus or only a presumed one, and 16 have nothing.
   - The ten axes need referent-bearing goal rows before ladders can attach.
   - [repo + my classification]
8. **Metrics fail quietly.**
   - My own first arc test was met by witness bookkeeping.
   - It also credited a lone closing event, and counted silence as an ending.
   - Always read arc rate beside a shuffled null and a bookkeeping null, and have an independent critic attack it.
   - [process]

**Not answered:** whether players find any of this legible or compelling. Nothing here used human readers, and the repo's own research says no method certifies generated content as good. The toy runs are my construction, so treat them as directional.

The design (PR #506) turns items 2 to 4 into build batches. Item 1 is the gate on all of them.
