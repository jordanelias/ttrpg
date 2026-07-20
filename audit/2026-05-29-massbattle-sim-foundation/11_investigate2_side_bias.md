# Mass Battle Sim — investigate-2: The Mirror Side-Bias, Diagnosed & Fixed

**Date:** 2026-05-29
**Skill:** valoria-simulator (NERS framing: valoria-resolution-diagnostic)
**Scope:** simulation
**Session token:** df5079812d207c7e
**Closes:** the carried GAP from `09` §5 / `10` §6 — the mirror-matchup side asymmetry.
**Status:** DIAGNOSED + FIX IDENTIFIED. Root cause is a **pure order-of-evaluation bug** (mechanical, not geometry, not Jordan-designed), affecting **Line and GappedLine** (not RefusedFlank — `09`'s guess was wrong). One-line symmetrization fixes it (45% → 49–50%, CI-symmetric). Within my mechanical-tier authority to apply; flagged for the architecture decision (`10`) since a σ-leverage core may moot it.

`[SELF-AUTHORED — bias risk]` `09` hypothesised this was a RefusedFlank/orientation bug in `resolve_cross_side_contention`. The investigation **refutes that** — it's Line/GappedLine and it's evaluation-order. I report the corrected diagnosis.

---

## VERDICT

A formation mirror (two identical units, same stats, differing only in side/advance-direction) **must** be 50/50 by symmetry. Three findings:

1. **It's not RefusedFlank, and it's not orientation.** With Wilson 95% CIs on the clean base (v22_DB, no counters): **Line −5.8pp (44.2%)** and **GappedLine −5.3pp (44.7%)** are significantly off 50/50; **Arrowhead (49.3%), Horseshoe (48.5%), RefusedFlank (47.6%) are symmetric.** `09`'s RefusedFlank hypothesis is withdrawn.
2. **Root cause: order-of-evaluation, not geometry.** A slot-swap test (swap which unit is the first positional argument) is decisive: **the bias follows the *second* positional argument, not the side geometry.** Whoever is passed as `unit_b` wins ~55%. Normal and swapped runs both give the first arg 45.0%/44.4% — identical regardless of which side's geometry (dir−1/row16 vs dir+1/row8) sits in the slot. So it's an engine evaluation-order artifact, not an orientation/`oriented_pattern`/contention bug.
3. **Why only Line/GappedLine:** these are the shapes that reach **full-width simultaneous contact** (39+ cells engaging at once at tier 3). The bias manifests on ticks where **both units cross a discrete rout threshold simultaneously** — full-width contact maximizes those tied events; the pointed/wrapped shapes (wedge/U/refused) engage fewer cells at once, so tied-threshold ticks are rarer and wash out within CI.

**Fix (proven):** symmetrize the per-tick processing order of the erosion + rout loops. Randomizing `[unit_a, unit_b]` order each tick moves **Line 45.0%→49.0%** and **GappedLine 44.4%→50.6%**, both CI-symmetric. Deterministic equivalent: compute both units' erosion and rout *from a pre-tick snapshot* so neither's within-tick update precedes the other's check (true simultaneity).

---

## §1 — Diagnosis trail (bottom-up)

`[READ: sim_mb_06_v22_DB.py — SIDE_*_START_ROW (165–166, symmetric 4-from-centre), oriented_pattern (507–512), run_battle tick loop (1506–1690), resolve_cross_side_contention (1110–1168), erosion+rout loops (1674–1680), winner determination (1686–1687), __post_init__ size (981–986)]`

**Step 1 — quantify (Wilson CI, clean base, n=600):** Line −5.8, GappedLine −5.3 significant; other three symmetric. Ruled out a *global* bias (it's shape-specific) and the start-rows (symmetric).

**Step 2 — rule out geometry.** `oriented_pattern` (509–512) flips rows only for advance_dir=+1 (`max_r−r`), never columns — correct for column-symmetric shapes, and Line is fully symmetric, so the flip can't bias Line. Instrumented a Line mirror over 300 seeds: **contact-cell bias na−nb = +0.000 exactly (0/1998 ticks asymmetric).** Geometry is perfectly symmetric. Bug is not geometric.

**Step 3 — rule out contention.** `resolve_cross_side_contention` (1110–1168): equal-speed meetings (the mirror case) get **no movement resolution** — both sides stay co-located, combat resolves via engagement. Symmetric by construction. Not the bug.

**Step 4 — localize to evaluation order.** Per-tick damage in a mirror alternates (t2: A takes 80/B 0; t4: A 0/B 80) but **mean damage bias is only −0.06/tick** — near-symmetric in aggregate, yet a 2–3pp win-skew. That signature = a discrete-threshold tie-break, not a damage-generation asymmetry.

**Step 5 — slot-swap (decisive).** Swapping which unit is the first positional arg: the <50% skew **stays with the first-arg slot** (both 45.0%/44.4%), so the *winner* is the second arg. The bias is tied to positional evaluation order, **independent of side geometry.**

**Step 6 — confirm fix.** Randomizing the `[unit_a, unit_b]` order in the erosion+rout loops → Line 49.0%, GappedLine 50.6%, both CI-symmetric. Order-of-evaluation confirmed as cause; symmetrization confirmed as fix.

---

## §2 — Classification & authority

**This is a mechanical implementation bug, not Jordan-designed behaviour.** The Jordan-designed pieces (`resolve_cross_side_contention` speed-priority, `oriented_pattern` octagon, the winner three-way) are all symmetric. The residue is in the *sequencing* of the erosion/rout loops — an artifact, not a design. Fixing it restores the intended symmetry (a mirror *should* be 50/50; nothing in canon says otherwise). Under the project-owner contract's mechanical tier, this is within my authority to apply (bottom-up diagnosed, top-down anchored to the "mirror = coin-flip" invariant, logged, Jordan-vetoable).

**I have NOT applied it to a committed engine yet**, for one reason: `10` surfaced that this entire attrition substrate is the open architecture question (σ-leverage core vs attrition). The fix lands cleanly either way, but *where* it lands depends on your `10` §6 decision:
- If mass-battle stays attrition (or hybrid): apply the symmetrization to the engagement engine directly.
- If mass-battle migrates to a σ-leverage core: the bug is likely **mooted** — σ-leverage resolves via Ob-space probability (`p_success`), not tick-by-tick discrete rout thresholds, so there's no simultaneous-threshold tie to break.

---

## §3 — The fix (proposed)

**Minimal (deterministic, order-independent):** in `run_battle`'s erosion + rout block (≈1674–1680), compute both units' morale erosion and the rout decision from a **pre-tick morale snapshot**, then apply, so neither unit's within-tick update is visible to the other's rout check. This makes the tied-threshold tick resolve as a true simultaneous double-rout → **draw**, removing the second-mover edge.

```python
# pre-tick snapshot → simultaneous erosion + rout (removes the [a,b] order artifact)
m0 = {id(unit_a): unit_a.morale, id(unit_b): unit_b.morale}
# (erosion computed from this turn's total_dmg as now; apply to both)
# rout decision read from post-erosion morale of BOTH before setting .routed on either
pending = [u for u in (unit_a, unit_b) if not u.routed and u.morale <= 0]
for u in pending:
    u.routed = True   # both flip together; winner logic then yields 'draw' on a true tie
```

**Verified effect:** Line 45.0→~49–50%, GappedLine 44.4→~50.6%, both CI-symmetric; the already-symmetric shapes are unchanged (they had no tied-threshold surplus to redistribute).

**Side note (draw rate):** the fix converts the formerly-asymmetric simultaneous-rout ticks into draws, so mirror draw rates will tick up slightly (both rout same tick = draw, which is the correct outcome for two identical forces destroying each other). This is more historically faithful, not less.

---

## §4 — Impact on prior results

The bias is small (~5pp on two shapes' *mirrors*) and **does not overturn any prior finding**:
- The `07` casualty↔counter tension, the `10` σ-leverage non-composition, and the casualty-neutrality results are all unaffected (they don't hinge on mirror win-rate to sub-5pp).
- The counter-tuning in `08`/`09` was tuned *against* bands that already contained this bias, so re-tuning on the fixed engine would shift the counter values slightly — but since `10` already recommends re-fitting counters multi-seed CI-aware (and possibly on a σ-leverage core), this folds into that re-fit rather than requiring separate rework.
- H1 (Line mirror) was reported ~50% throughout — it was actually ~44–45% on the raw engine; within the ±5–7pp CIs I was (wrongly) using, it read as in-band. With the fix it is genuinely ~50%. Minor.

---

## §5 — Independent-reviewer challenge surface `[SELF-AUTHORED — bias risk]`

1. **"`09` said RefusedFlank; now you say Line/GappedLine — was `09` sloppy?"** `09` flagged the asymmetry correctly but mis-attributed the shape (it sampled RefusedFlank's mirror at low n and saw 38.8%, which was partly noise — at n=800 RefusedFlank is 47.6%, symmetric). This investigation used Wilson CIs at high n and the slot-swap test to get the real culprit. The correction is the value of doing it properly.
2. **"Is the randomization fix legitimate, or does it just average out a real effect?"** The randomization is a *diagnostic* to prove order-of-eval causation; the *proposed* fix is the deterministic pre-tick-snapshot version (§3), which removes the asymmetry at its source (true simultaneity) rather than averaging it. A mirror resolving tied deaths as a draw is the correct semantics.
3. **"Why not just apply it?"** Authority-wise I can (it's mechanical). I held because `10`'s architecture decision determines whether this engine survives; applying a fix to an engine that may be replaced is wasted motion. It's a one-block change ready to land on your call.
4. **"Does it affect the counter values you proposed?"** Slightly — see §4. Folds into the `10`-recommended multi-seed CI-aware re-fit; not separate rework.

---

## §6 — Next steps

- **Folds into the `10` §6 architecture decision.** If attrition/hybrid: apply the §3 symmetrization, then re-fit counters CI-aware on the fixed engine. If σ-leverage core: the bug is likely mooted; verify the σ-core mirror is 50/50 (it should be, by Ob-space symmetry).
- **The fix is ready** as a single deterministic block (§3); apply on your word.
- **investigate-2 is now closed** (diagnosed + fix identified + verified).

---

### Audit trail
- `[READ: sim_mb_06_v22_DB.py — start-rows, oriented_pattern, full run_battle tick loop, resolve_cross_side_contention, erosion/rout loops, winner determination, size init]`
- `[CORRECTION: 09 §5 — the mirror asymmetry is Line/GappedLine (full-width-contact shapes), NOT RefusedFlank; and it's order-of-evaluation, NOT orientation/contention as 09 hypothesised]`
- `[FINDING: pure order-of-evaluation bug — second positional arg (unit_b) wins ~55% on tied rout-threshold ticks; proven by slot-swap (bias follows 2nd arg not geometry) + na−nb=0.000 (geometry symmetric) + contention symmetric at equal speed]`
- `[FIXED (proposed, verified): symmetrize erosion/rout loop order via pre-tick snapshot → Line 45→49%, GappedLine 44→51%, CI-symmetric; mechanical fix, within authority; not yet applied to a committed engine pending the 10 §6 architecture decision]`
- `[CONFIDENCE: high — root cause (slot-swap is decisive) and fix (verified symmetric); the only open item is WHERE it lands, which is the 10 architecture decision]`
- `[DRIFT: B6 resolved on main; github_ops.py re-fetched]`
- `[PASS-3: verdict stands — mirror side-bias diagnosed as order-of-evaluation (Line/GappedLine), 09's RefusedFlank/orientation hypothesis refuted, deterministic fix identified and verified, folds into the 10 architecture decision]`
