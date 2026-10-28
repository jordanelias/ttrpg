# R02 — Logic tests of top-down, bottom-up and hybrid emergence; deconstruction of the studied arcs

## Status: REFERENCE — HELD BACK IN FULL

> **Reference — PROPOSED, HELD BACK IN FULL.** Merging the PR that carries this file ratifies nothing in it (ED-1094's default is not applied). Delivered in chat during the session of 2026-10-24/25 and reproduced verbatim, except that session-scratchpad paths are rewritten to their committed locations. Figures were taken **before** the register's measurements (`../01_MISSING_IN_CODE.md` §2, probes P1–P12); where they differ, `../02_MAJOR_TAKEAWAYS.md` §9 (Corrections) governs.

**Asked by the user:**

> Perform a series of logic tests to evaluate legibility, coherency, arc and beats/nodes for the following: top-down narrative emergence, bottom-up narrative emergence, and a hybrid of top-down/bottom-up narrative emergence.
> (sent mid-turn) Alternatively, let's critically deconstruct our body of studied character arcs. What are the different ways in which these arcs can be achieved?

---

**Verdict.** The corpus achieves arcs in seven ways. Most of its "character arcs" are positions rather than trajectories: 28 of the 46 character cases author no terminus, or one the extractor only presumed. The logic tests point the same way. Motive makes events legible. Arc shape appeared only where something forced closure.

## Ways the studied arcs are achieved

Sources: the census (`.audit/2026-07-05-emergent-narrative-engine/_workings_joined.md` §3.2), `engine/season/ENDINGS_CLASSIFIED.yaml`, and the 143 cases.

| Engine | What moves | Corpus weight | Closes by |
|---|---|---|---|
| Accrual | a slow variable crosses a line | clock arcs (6 of 7) and the loyalty-clock family (~12–15 arcs, "the most duplicated shape"); characters 020, 052, 070, 031 | threshold (8/50 arcs; 19/50 are crossing-forced) |
| Exposure | a concealed fact surfaces | 11 of 46 characters hold one: 088, 087, 086, 005, 010, 007, 038, 039, 004, 033, 080 | discovery |
| Succession | a seat empties and a pre-wired successor moves | ~6 faction arcs; characters 006, 081, 002, 032, 030, 031 | holder changes |
| Decision point | a person or body picks among named options | ~16–19 arcs | decider (20/50, the largest class) |
| Contest | opposed parties resolve by roll or vote | ~11–12 arcs | roll (9/50) |
| Conjunction | several arcs' states coincide | 13 (8 collisions, 5 one-time multi-stat triggers) | one permanent change |
| Held control state | a condition with cascading effects | 20–25 of 29 territory entries | never (10/50). This is a state, not an arc. |

Internal transformation has no shape of its own in the census list. Where characters carry it (052, 021, 039, 080), it is accrual with a fork. That gap is my inference from the list.

## What the deconstruction shows

1. **Positions, not trajectories.** I classified all 46 character cases by `ends_when`, by hand and as a single reader:
   - **Forks (11):** 004, 020, 021, 050, 052, 070, 003, 032, 031, 030, 001.
   - **Exit events only (7):** 088, 087, 075, 012, 008, 038, 013.
   - **Terminus presumed by the extractor (12):** 086, 005, 010, 002, 083, 007, 006, 009, 011, 035, 039, 040.
   - **Nothing authored (16):** 033, 071, 034, 036, 037, 041, 072, 073, 074, 080, 081, 082, 084, 085, 089, 090.
2. **Where a trajectory exists, it is accrue-then-fork.** 10 of the 11 forks name a cumulative or graded variable. Examples: 020 has cumulative private doubt plus the army's reassessment stage, and 052 has advancement toward a transformation threshold. No middle beats are authored; the middle is a variable. Rise, peak and fall are not in the data at all, only thresholds and exits.
3. **The ARC lane is not mostly arcs.** Of the 50 classified endings, 16 (32%) are not multi-season arcs: 10 never close, 3 name no closing condition, and 3 resolve in one roll (ARC-21, 23, 27).
4. **The "~13 shapes" figure is thin.** It comes from 24 of 138 arcs classified, with a stated range of 12–15. The calibration set was evacuated, so it can't be re-checked (`09_ambitions_and_arcs.md` §7.2).
5. **The corpus is top-down by origin.** Every arc is an authored predicate, per your 2026-08-18 ruling. It records what was wanted, not whether emergence delivers it.

## Logic tests

I ran four regimes in a toy world of my own construction, 300 seeds each. The regimes are bottom-up (BU), blind script (TD), replanning director (TDR) and motive hybrid (HY).

| Property | BU | TD | TDR | HY |
|---|---|---|---|---|
| Legibility: fields present | 1.00 | 1.00 | 1.00 | 1.00 |
| Legibility: motive outlasts the moment | 0.43 | 0.36 | 0.23 | 0.80 |
| Coherency: constraint violations, unperturbed / after killing the thread leader at season 10 | 0 / 0 | 0.96 / 1.00 | 0 / 0 | 0 / 0 |
| Arc rate (shuffled null) | 0.09 (0.10) | 0.16 (0.17) | 0.35 (0.25) | 0.06 (0.08) |
| Beats: complete setup, turn, climax, resolution | 0.11 | 0.34 | 0.76 | 0.11 |
| Runs containing a forced outcome | 0 | 1 | 1 | 0 |

- **Legibility.** The fields-present measure doesn't discriminate. Standing motives deepen the "why": HY minus BU is +0.35 to +0.39 (95% CI), and the sign held in all five world conditions.
- **Arcs.** Bottom-up and motive-only arcs sit at chance. Raising ambition weight lowered the arc rate from 0.09 to 0.03. Searching a log for an arc-shaped thread and window finds arcs at or below the shuffled null in every regime except TDR.
- **Schedule.** Only the forced, state-reading schedule beat chance on ordering (TDR minus BU +0.26, CI +0.20 to +0.33). The blind script violated world constraints in 96% of runs, by construction.
- **Refusal rate.** With the real engine's refusal rate (81% of chain acts, 66 of 81), the gap between TDR and BU widens.
- **Closure engine (post hoc).** HYc, a version where fired ambitions simply end, changed nothing. HYd, where a threshold raises a declinable tribunal and a decider actor rules, lifted the arc rate to 0.26 (+0.11 to +0.23 over BU). It also lifted closure from 0.23 to 0.77 and complete beats to 0.55, with no injected outcome.
- **Why HYd is not a clean win.** Its shuffled null is also 0.26, because the arc test passes a lone interior closing event at any season (I checked seasons 8–20). So it measures closure more than ordering. Under 80% refusal HYd's gain over BU vanishes, while TDR reaches 0.71.

**Design implication.** The hybrid I tested lacked a closure engine, and the corpus's dominant ones are decider and threshold. Lawful top-down is arming those engines, not writing beats. Whether to accept TDR's injected, ordered arcs instead is yours to decide.

[ASSUMPTION: the toy world, metrics and arc template are mine; the results test the regimes' logic under my operationalizations, not Valoria's engine. Only the refusal rate comes from the real chronicles.]
[CORRECTION: v1 had four instrument defects, so I fixed the metrics and re-ran as v2. The defects were a prize/duel thread split, a climax outside my own peak window, tied climax events, and an early transient inflating the null. The v2 predictions were registered after seeing v1; HYc, HYd, the bootstrap intervals and the sift test are post hoc. v1 scored 11/21 and v2 13/21. A6 had a key-filter bug; its result is right by luck and I re-derived it by hand.]
[CONFIDENCE: medium — a three-act test can't see spirals such as ARC-05, and the case classification is one reader's judgement.]

Code and raw outputs are in `proposals/2026-10-25-thrust-layer/toy/`: `regimes2.py`, `regimes3.py`, `predictions_v2.py`, `out_v1.txt`, `out_v2.txt`, `posthoc_out.txt` and `exp_closure_out.txt`.
