# Envelopment Stability Diagnosis — the H3/H10 side-asymmetry root-caused (ED-MB-0039, 2026-07-24)

**Status: DIAGNOSTIC + engine-design fork flagged for Jordan.** Continues ED-MB-0038 (matched command-
granularity). Reproducible: `audit/2026-07-22-mass-battle-stress-test/envelopment_stability_probe.py`.

## The question ED-MB-0038 left open

Matched command-granularity (ED-MB-0038) fixed the envelopment *measurement* artifact and landed H3
"full envelopment" at 70.7% (band 55-72, OK) — but the **reverse rows stayed broken**: H10 (Line vs
Envelopment) read 83% for the line (band 28-45), i.e. the enveloper won only ~17% as side B while
winning ~71% as side A. Same armies, same seeds, sides swapped: a **~54pp side-asymmetry**.

## Root cause (measured, not inferred)

**It is not an RNG-stream artifact** (`side_probe.py`: army construction does not consume `random`).
**It is not a simple side bias** — the composed *mirrors* (envelop-vs-envelop, 3-command-vs-3-command)
are side-symmetric within noise (~50-58% @ n=120). It is a **deployment-chaotic knife-edge amplified by
Lanchester positive feedback**:

- A **parity centre is NARROWER than the 3-command enemy** (200 troops @ 100/cell = 2 cells vs the
  defender's 6). So the *enemy out-flanks the centre* while the enveloper's wings try to wrap the enemy —
  a two-way race. Whoever tips first snowballs (Lanchester: the side slightly ahead kills faster, takes
  less return fire, runs away with it). A position trace (seed 1, `side_face_probe`-style) shows the
  closing **geometry is mirror-identical** in both orientations, but the **casualty exchange is not** —
  the enveloper stays near-full as side A and bleeds to a rout as side B, at the same positions.
- The tip is decided by **integer deployment parity**: sweeping start rows (A=34/B=15 → A=34/B=14 →
  A=35/B=15 → A=30/B=20) swings the enveloper's win-rate 54pp → 50pp → 17pp → 9pp. There is **no stable
  envelopment "strength"** — it is chaotically position-dependent. The side-symmetric *average* is ~44%
  (the enveloper slightly *loses* at parity). **H3's 70.7% is the favourable side of the chaos, not a
  robust edge.**

## Three regimes — and the gap between them (`envelopment_stability_probe.py`, vs the 3-command Line)

| enveloper | env-A | env-B | swing | avg | reading |
|---|---|---|---|---|---|
| pure-infantry, thin centre | ~64-74% | ~17-23% | **~41-54pp** | **~44%** | chaotic, side-asymmetric, ~even |
| deep-narrow centre (width=1,depth=2) | ~20% | ~10-13% | **~7-10pp** | ~15% | **stable but LOSES** (too narrow → bypassed) |
| combined-arms (infantry pin + CAVALRY orbital-wheel rear) | ~93-100% | ~96-100% | **~0-14pp** | **~93-100%** | **stable, side-symmetric, decisive** |

Two structural facts fall out:

1. **Depth confers no holding power without frontage.** `width`/`depth` reshape the footprint only when
   *both* keys are set (width alone is silently ignored — `build_army`/`footprint_for`); with a genuine
   deep-narrow centre the swing collapses (51→7pp) — the knife-edge *was* the thin flat centre — but the
   centre is now too narrow to pin the enemy's frontage, so the enemy flows around it and the envelopment
   loses. The frontage-capped attrition model gives a deep column no lower casualty *rate*, only a narrower
   front; a narrow front is bypassed. Jordan's "deep centre holds via rotational depth" is **not modelled**.
2. **Combined-arms is the only stable regime, and it is total.** The cavalry orbital-wheel (ED-MB-0035)
   reaches the **rear** — which cannot be refaced ("you cannot face the rear", Burkholder; the C7
   rationale) — so the rear octagon multiplier (2×) × multi-side shock annihilates. It reads ~100% and
   side-symmetric against **every** defender toughness tested: deep commands, discipline 8, braced+d8,
   6-command. **Nothing moderates it** to 55-72.

## Conclusion: the moderate-envelopment bands sit in an engine gap

The engine produces **two envelopment regimes and nothing between**: chaotic-even pure-infantry (~44% ±
a 54pp deployment/side swing) or total combined-arms (~100%). The history-grounded **H3 55-72 / H4 45-62**
bands — a *moderate, reliable* infantry edge — are **not stably reachable**. The gauge's H3=70.7 "pass"
is the favourable side of the infantry chaos; its H10/H11 failures are the same chaos seen from the other
side. This is an **engine limitation, not a gauge-calibration knob** — matched granularity (ED-MB-0038)
was necessary and correct, but it exposed that the underlying envelopment mechanic is bimodal.

## The fork (needs Jordan — a grounding + engine-design call, touches PASSING rows)

Jordan's standing directive is combined-arms ("the envelopment needs to be cavalry that moves quickly").
Two ways to close the gap; both change history-grounded bands or a core mechanic, so they are flagged
rather than executed unilaterally (the grounding doc forbids band-fitting; C4/C7 currently PASS):

- **(A) Reframe H3/H4 as combined-arms Cannae** (infantry pin + cavalry rear, per the directive). Honest
  reading ~90-100% → the H3/H4 bands rise toward C4/C7's 75-100, at the cost of H3/H4 becoming near-
  duplicates of C4/C7. Cheap; loses the infantry/cavalry *distinction* the grounding draws.
- **(B) Add a moderate-envelopment mechanism** — grounded **seal-failure / breakout variance**: an
  encircled body is not always annihilated; with a discipline/morale-modulated probability the pocket
  fails to seal or the encircled break out, spreading combined-arms from ~100% into a 60-90% distribution
  and giving pure-infantry a stable moderate outcome. Historically real (envelopments often failed to
  seal). **Blast radius: it would lower C4 (93→?) and C7 (100→?), which currently pass — needs an A/B that
  keeps them in-band.** This is the "right" fix but a substantial new primitive.

**Recommendation: (B)**, staged behind a gated flag with a C4/C7-preserving A/B, as the honest way to make
envelopment a *gradient* (moderate infantry → decisive combined-arms) rather than a bimodal switch. (A) is
the fast fallback if the gradient proves too costly to calibrate.

## What stands from ED-MB-0038

Matched command-granularity is correct and lands: it removed the monolithic-defender artifact (envelopment
was pinned to 0% regardless of geometry) and is the honest granularity constant. H3's 70.7 is real *for
side A* — the gauge is correctly flagging the engine's envelopment side-asymmetry via the H10/H11 failures.
This diagnosis explains *why* those reverse rows fail and what the fix requires; it does not retract 0038.
