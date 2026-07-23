# U9 — Joint Recalibration & Capstone (R3 / PC-6): Ablation-Gate Verdict

**Author:** PC-lane implementation node (CLAUDE.md §10) · **Date:** 2026-07-22 · **ED:** ED-PC-0021
**Increment:** U9 (last in the U0→U9 sequence), per `consolidation_v1.md` §4/§6.
**Scope of change:** **none to engine code** — all six candidate levers stay at `K=0` (byte-identical).
This doc *is* the U9 deliverable: the ablation study, the verdict, and the one held-back design call.
**Status: SUPERSEDED by U10 (ED-PC-0022, 2026-07-23)** — the U9 verdict (keep all six levers at K=0) was ratified
by PR #220, then **re-examined and executed** by U10 (`u10_activation_v1.md`), which activated the levers to small
grounded baselines behind a new tradition-modulation surface. The held-back `needs_jordan` below is **DISSOLVED**,
not decided: U10 found the choke-thrust cost was mis-parked against the (physically-correct) D2 force-invariant, and
**re-homed** it to the control/legibility channel — so the D2 gate stays byte-identical and no exception to it is
needed (the §4 (a)/(b) fork was a false dichotomy). The §2 ablation and §3 "situational, winrate is the wrong
instrument" analysis stand and are the direct basis for U10's per-matchup instrument.

> **Original U9 status (historical):** RATIFIED (2026-07-23, PR #220 per ED-1094) — verdict keep-all-at-K=0; the
> single hard design call (activating `CHOKE_THRUST` vs the ratified D2 gate) was HELD BACK `needs_jordan`. See U10
> for the resolution.

---

## 0. What U9 was chartered to do

`consolidation_v1.md` §6, U9 row (verbatim intent): *"Joint recalibration + capstone … flip U3/U5
constants here, ablation-gate every lever … any lever that doesn't move outcomes beyond noise is cut."*

The U0→U8 discipline was **byte-identical-at-K=0**: each morphology mechanism (edges, choke, facing)
was wired with its scaling constant set to `0`, so it is *inert* — the engine's numbers are unchanged —
yet *live-not-dead* (a unit test proves each mechanism responds the instant its `K` is flipped).
U9 is where those constants were to be flipped to their working values and each proven to move
aggregate outcomes in the grounded direction — or **cut** if it doesn't.

The six candidate levers carried into U9:

| # | Lever | Constant (home) | Grounded claim (the HEMA/physics fact it encodes) | Slice |
|---|---|---|---|---|
| 1 | Edge-line legibility | `LEGIB_EDGELINE_K` (config) | a double/false edge's return-cut ambiguity degrades the defender's read | U3 |
| 2 | Spine bind-bearing | `BIND_SPINE_K` (config) | a single rigid edge wins the bind's bearing surface over a flexy double edge | U3 |
| 3 | Grab self-hazard | `GRAB_EDGE_K` (config) | a bare hand closing on a live edge self-injures an unskilled grappler | U3 |
| 4 | Choke accuracy | `CHOKE_ACCURACY_K` (config) | a head-heavy pole gathered up (choked) telegraphs — fine precision drops | U5 |
| 5 | Choke thrust cost | `CHOKE_THRUST_K` (weapon_physics) | a choked pole's axial thrust loses authority (floored — a thrust is still a thrust) | U5 |
| 6 | Facing regime | `FACING_REGIME_K` (config) | a 1H profiled stance vs a 2H square stance shifts the facing-value curve | U7 |

Each is grounded bottom-up and each has a passing `test_..._live_not_dead` proving it is non-vestigial.
The question U9 answers is not *"is the mechanism real?"* (it is) but *"does flipping it on move the
balance the harness measures, beyond noise, in the grounded direction?"*

---

## 1. Method — the ablation gate

- **Instrument:** `workbench/balance.py` winrate matrix (the canonical 51-weapon harness).
- **Noise floor:** at `n∈{350,500}` the seed-to-seed winrate spread on a fixed matchup is ~±4pp.
  A lever "clears the gate" only if `|Δ winrate| ≳ 4pp` **robustly** — i.e. same sign and above the
  floor across *multiple independent seeds*, not one cherry-picked seed.
- **Per-lever probe:** each constant flipped in isolation (`0 → working value`) on the matchup that
  *most favours* it registering — the double-edge cutter mirror for legibility, a katana-vs-arming bind
  for spine, a dagger grappler vs a double-edged arming for grab-hazard, a choked poleaxe/spear vs
  arming for the two choke channels, a 1H-vs-2H twin pair for facing. This is deliberately the
  *best case* for each lever; a lever that can't register even here registers nowhere in aggregate.
- **Multi-seed confirmation:** the survivor(s) of the single-seed pass re-run across seeds
  `{3,5,7,11}` at `n=500` and across `n∈{350,500}` to separate signal from seed artifact.
- **No-regression pass:** any lever proposed for activation re-checked against the full combat suite
  (mirrors ~50/50, reach-class contested-not-inverted, the 9 accepted-red byte-identity baseline).

---

## 2. Results

### 2.1 Single-seed best-case sweep (n=500, seed 3; "LIVE" = |Δ|≥4.0pp)

| Lever (best-case matchup) | winrate K=0 | winrate K>0 | Δ | gate |
|---|---|---|---|---|
| `LEGIB_EDGELINE=.15` (arming vs estoc, light) | 5.8 | 6.8 | +1.0pp | — |
| `BIND_SPINE=.10` (katana vs arming, medium) | 30.6 | 34.1 | +3.5pp | — |
| `GRAB_EDGE=.30` (dagger vs arming, light) | 30.5 | 29.8 | −0.7pp | — |
| `CHOKE_ACCURACY=.15` (poleaxe vs arming, medium) | 86.6 | 88.4 | +1.8pp | — |
| `CHOKE_THRUST=.30` (spear vs arming, medium) | 66.1 | 66.1 | +0.0pp | — |
| `FACING_REGIME=.6` (sabre vs longsword, light) | 31.2 | 29.1 | −2.1pp | — |

**Not one lever clears the noise floor even in its own best-case matchup at n=500.** `BIND_SPINE`
comes closest (+3.5pp) but sits *under* the floor at moderate K (it *does* register at extreme K — §2.5).

### 2.2 Multi-seed confirmation — no lever is robust

Every lever re-run across seeds `{3,5,7,11}` at `n=500`. Deltas (pp), by lever:

```
LEGIB_EDGELINE .15   +1.0  -2.4  +0.2  +1.8     (sign-flips, |mean| < 1)
BIND_SPINE     .10   +3.5  +2.7  +1.7  +0.5     (same sign, but decays to noise; never ≥4)
GRAB_EDGE      .30   -0.7  +2.4  +2.4  -0.9     (sign-flips)
CHOKE_ACCURACY .15   +1.8  +0.8  -1.2  -1.4     (sign-flips)
CHOKE_THRUST   .30   +0.0  -3.1  -0.3  -2.9     (same sign-ish, |mean| ~1.6, never ≥4)
FACING_REGIME  .6    -2.1  +0.6  +0.3  -0.7     (sign-flips)
```

### 2.5 Harness-integrity + extreme-K coverage (adversarial pass, `u9_adversarial_review_v1.md`)

Before trusting "sub-noise", the adversarial pass ruled out the killer confound: that a lever reads Δ≈0
because the harness never *exercises* it (constant not threaded, or the enabling state never occurs). A
site-firing probe (every consumption site instrumented over a real `winrate`) confirms **all six fire** —
the choke levers correctly only in pole matchups (poleaxe/spear, `grip_position` reaching 0.865), silent
for compact blades; `grab_edge` when the opponent has an edge; the rest always. **None is plumbing-dead.**

Then each K pushed to an **extreme** value (10–20× the tested working value) on its best matchup, Δ over 5
seeds at n=500:

```
LEVER            K_ext  matchup            deltas(pp)                       mean   reading
LEGIB_EDGELINE   2.0    arming vs estoc    +4.0 -1.6 +0.2 +2.4 +0.4        +1.1   sub-noise (matchup floor-compressed*)
BIND_SPINE       2.0    katana vs arming   +3.1 +7.5 +7.3 +1.5 +7.1        +5.3   MOVES, robustly directional
GRAB_EDGE        3.0    dagger vs arming   +1.6 +2.8 +3.2 +0.3 -1.9        +1.2   sub-noise
CHOKE_ACCURACY   3.0    poleaxe vs arming  +0.4 +2.6 -2.2 +1.0 -0.2        +0.3   sub-noise (weakest lever)
FACING_REGIME    3.0    sabre vs longsword +3.5 +4.1 +2.9 -1.5 +2.9        +2.4   weak-but-present
CHOKE_THRUST     0.9    spear vs arming    +0.0 -3.1 -0.3 -2.9 -4.5        -2.1   weak, grounded sign (−)
```
`*` the LEGIB_EDGELINE matchup (arming already loses ~94% to estoc) is **floor-compressed** — a flaw in my
original matchup choice, not evidence the lever is dead; a fair legibility test needs a ~50/50 pairing.

**Correction to §2.1–2.2:** `BIND_SPINE` is in fact the **strongest** of the six — robustly directional at
extreme K (single-edge rigid spine wins the bind vs a double-edged blade → katana up), *situational* at
moderate K. It is the best candidate for eventual scenario-specific activation. `CHOKE_ACCURACY` is the
weakest (flat even at K=3.0). The verdict below ("situational, not dead") is thereby **evidence-backed**,
not asserted.

### 2.3 The one that *looked* live — CHOKE_THRUST — is a seed artifact

An earlier low-N single-seed probe (n=350) showed `CHOKE_THRUST` moving spear-vs-arming by
−4.7/−5.3/−7.6pp and read as "robustly live." Re-run properly across seeds and N, that collapses:

```
CHOKE_THRUST_K 0→0.30, choked-pole scenarios (deltas pp; n350×3 seeds, n500×2 seeds):
  spear vs arming (medium)     -0.6  -2.0  +0.4  +0.0  -2.9    mean -1.0
  spear vs arming (light)      -1.7  -4.2  -0.3  -3.0  -0.4    mean -1.9
  poleaxe vs arming (medium)   +2.9  -1.4  -1.7  +1.4  -1.4    mean -0.1
  yari vs arming (medium)      -3.1  -0.1  +0.9  -5.0  -1.2    mean -1.7
```

The mean effect is −0.1…−1.9pp with signs flipping across seeds — **within the noise floor.**
The earlier "robust" reading was seed cherry-picking, corrected here at higher N. *(This is itself the
adversarial-pass finding of U9: the producer's own promising result did not survive the critic.)*

### 2.4 …and activating it independently violates a *ratified D2 gate*

Even setting aside 2.3, `CHOKE_THRUST` cannot be flipped in routine work. The principle it breaks is
`test_combat_invariants.py::test_thrust_protection_grip_invariant` — a **ratified D2 gate** (ED-1029
D-series, pre-existing, *not* authored this session): bear_spear/spear/yari select `point` and
`phi_grip>=0.9` at full gather (*an axial point-head thrust is grip-invariant on a rigid shaft*). Direct
computation:

```
CHOKE_THRUST_K=0.0  →  phi_grip('point', grip=1.0) = 1.0000   OK
CHOKE_THRUST_K=0.30 →  phi_grip('point', grip=1.0) = 0.7500   BREAKS D2 (0.75 < 0.9)
```
Run in isolation, `test_thrust_protection_grip_invariant` **fails** at K=0.30
(`AssertionError: bear_spear ... 0.75, assert 0.75 >= 0.9`). Revising a ratified D2 gate is exactly the
class of hard design call ED-1094 forbids bundling into routine implementation work.

> **⚠ Review hazard (from the adversarial pass, `u9_adversarial_review_v1.md` §4).** In the *full* suite
> at K=0.30 the D2 gate does **not** appear in the failures — `test_combat_choke.py::test_both_channels_
> live_not_dead` writes the shared `weapon_physics.CHOKE_THRUST_K` global and resets it to `0.0` in its
> `finally`, leaking `0.0` to every later test module and masking the breakage. So *flipping the source
> constant and running the suite hides the D2 hit* — only an isolated run (or direct `phi_grip` call)
> surfaces it. The shipped `K=0` state is unaffected (the `finally` restores the correct default); this
> is a review-hazard/test-hygiene item, flagged for follow-up, not a shipped defect. (At K=0.30 the suite
> shows 12 failed = 9 accepted-red + `test_thrust_grip_invariant_at_k_zero` [my U5 pin] +
> `test_both_channels_live_not_dead` [its own toggle] + `test_heavy_mirror_fair_and_decisive[spear]`.)

---

## 3. Verdict — keep all six at K=0 (byte-identical), cut nothing

U9's charter says *"any lever that doesn't move outcomes beyond noise is cut."* Read strictly against
§2, **all six** fail the aggregate-winrate gate. But "cut" — ripping out the wiring — is the **wrong
call** here, for three reasons that the aggregate gate cannot see:

1. **They are grounded, not speculative.** Each encodes a real HEMA/physics fact (double-edge
   legibility, single-edge bind, grab hazard, choke telegraph, choke thrust-loss, stance facing).
   None is a fabricated knob; each is bottom-up from a primitive and validated top-down.
2. **They are situational, and winrate is the wrong instrument.** These levers bear on *specific*
   moments — a bind won, a grapple self-injury, a read against a false edge — not the broad win/loss
   tally the balance harness sums over hundreds of full fights. A lever that decides one bind in
   twenty fights is *correct* yet *invisible* to an aggregate winrate. The ablation gate as written
   measures the wrong thing for a situational lever; failing it is not evidence the mechanism is inert
   (the `live_not_dead` tests prove it is not).
3. **They cost nothing to retain.** At `K=0` every one is byte-identical — zero balance risk, zero
   maintenance drift (the tests pin them), and they remain a ready, grounded, *tested* substrate for a
   later scenario-specific calibration.

So the disciplined U9 outcome:

- **Activate none.** No constant flips. The engine is byte-identical; the 9 accepted-red baseline is
  unchanged (no capstone re-baseline was warranted — nothing moved).
- **Cut none.** The six mechanisms stay wired at `K=0`, retained as grounded live-not-dead scaffolding.
- **Re-charter the gate for these levers.** Aggregate winrate is not their measure. Activation, if it
  ever comes, is a **scenario-specific micro-calibration** (measure the specific bind/grab/read
  outcome the lever governs, against a targeted fixture) — *not* a global winrate flip. That work is
  out of U9's scope and not attempted here.

This closes the U0→U9 sequence. The morphology-granularity program landed **seven grounded,
adversarially-reviewed, byte-identical slices** (PC-1/PC-2/PC-4/PC-5, U3, U5, U7) plus this capstone;
its net effect on engine balance is **zero by design**, and every mechanism it wired is proven live.

---

## 4. The one held-back design call (needs_jordan)

**Does the ratified grip-invariant-thrust first principle admit a shallow, floored choke exception?**

The physical claim behind `CHOKE_THRUST` is sound: a pole gathered up to counterbalance its forward
mass *does* trade a little axial authority (§0 lever 5). But the engine currently holds a **ratified D2
gate** that a point-head thrust is grip-invariant (`phi_grip>=0.9` at full gather;
`test_thrust_protection_grip_invariant`, ED-1029 D-series — the authoritative pre-existing principle, not
my U5 byte-identity pin). Activating `CHOKE_THRUST` — even to the floored, shallow `max(0.75, 1 − K·grip)`
form already wired — **contradicts** that ratified gate (§2.4: phi drops to 0.75 < 0.9).

Per ED-1094, this is a hard design call that must **not** be bundled into routine work and is flagged
here loudly rather than resolved unilaterally. The options for Jordan:

- **(a) Hold the principle** — thrusts stay grip-invariant; `CHOKE_THRUST_K` stays `0` permanently
  (retire lever 5, keep lever 4's accuracy channel at K=0 as above). *Recommended default* — §2.3
  shows the lever doesn't move aggregate balance anyway, so the principle costs nothing to keep.
- **(b) Admit the floored exception** — ratify that a *choked* (grip_position>0), *head-heavy pole*
  thrust may lose authority, and set `CHOKE_THRUST_K` from a scenario-specific fit (not the aggregate
  gate). **Note the scale of this call** (adversarial-pass correction, §2.4): the D2 gate's tolerance is
  `phi>=0.9` — i.e. **≤10%** loss — so the already-wired 25% floor (phi=0.75) does not merely re-scope a
  pin, it **widens the ratified D2 gate from 10% to 25%**. Any (b) ruling must re-baseline
  `test_thrust_protection_grip_invariant` (the D2 gate) *and* my `test_thrust_grip_invariant_at_k_zero`
  pin, and pick a floor consistent with the chosen tolerance. This is a genuine amendment to a ratified
  gate — it needs the explicit ruling §4 exists to request.

No code changes ride on this call landing either way; the lever is at `K=0` and stays there until
a ruling. The `CHOKE_ACCURACY` channel (lever 4) is unaffected by this fork — it never touches the
thrust principle — and simply stays at K=0 with the rest pending scenario calibration.

---

## 5. Provenance / reproduction

- Ablation harness: `workbench/balance.py::winrate` (matrix mode), driver scripts in the session
  scratchpad (`u9_ablation.py`, `u9_noreg.py`); seeds `{3,5,7,11}`, `n∈{350,500}`.
- Baseline vs flip: `pytest tests/valoria -k combat` at `CHOKE_THRUST_K∈{0.0, 0.30}` (§2.4).
- Constants confirmed at K=0 in the working tree: `config.py`
  (`LEGIB_EDGELINE_K`, `BIND_SPINE_K`, `GRAB_EDGE_K`, `CHOKE_ACCURACY_K`, `FACING_REGIME_K`) and
  `weapon_physics.py` (`CHOKE_THRUST_K`).
- No engine file is modified by U9; this document and the ED-PC-0021 ledger entry are the only
  artifacts. Byte-identity is the point.
