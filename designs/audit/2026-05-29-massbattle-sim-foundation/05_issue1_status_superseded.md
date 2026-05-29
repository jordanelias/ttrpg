# Mass Battle Sim — Issue-1 Fix Status + Corrected Diagnosis

**Date:** 2026-05-29
**Task:** simulation (re-gated; `sim_gate('custom', systems=['mass_combat'])` passed — full-depth reads + 6-entry verification ledger)
**Scope:** Issue 1 (lethality regression) from `tests/sim/sim_audit_v5_to_v22.md`
**Commit status:** blocked (B6) — engine edits are local only; staged for manual push.

---

## Verdict

**Issue 1 (lethality) is fixed in mechanism and necessary — but NOT sufficient.** Re-introducing damage scaling restores battle *pacing* (t ≈ 2 turns, was 4–8) and the *symmetric* matchups, but the 13-matchup battery only reaches **3/13** (best). The audit's implied "fix Issue 1 → battery recovers to ~12/13" is **empirically false**: the remaining 10 failures are formation-geometry matchups blocked by the audit's **Issues 2/3/4** (broken formation mechanics), plus ranged matchups blocked by volley calibration (ED-822). Full recovery requires a **coordinated formation-mechanics + lethality pass**, not a single-constant tune — and the lethality value cannot be finalized until the mechanics are fixed (the battery is the calibration instrument and is currently confounded).

---

## What I did (audit trail)

1. Re-gated to `simulation`; built `/home/claude/sim_verification_ledger.json` (6 entries, quotes grepped from canonical docs, not recalled); `sim_gate` passed.
2. Staged `sim_mb_06_v22.py` + `battery_v22.py` to disk; **reproduced the regression: 1/13 in-band (8%)** — confirming the arc audit's finding (it had said 1–2/13).
3. Confirmed the engine's engagement model directly from code: `DAMAGE_BY_DEGREE = {Overwhelming: 1+P, Success: P, Partial: 1, Failure: 0}`, applied per engaged cell-pair as `max(0, BAND(degree, P) − DR)`, parallel + simultaneous. (This is the PP-233 degree-banded model — confirms the prior turn's correction that §A.7's additive text is the stale drift.)
4. Implemented Issue-1 fix: re-introduced a damage multiplier on `DAMAGE_BY_DEGREE` (the `LETHALITY_SCALE` v19 dropped) and **calibrated it empirically by sweeping against the battery** (not guessing the constant).

## Sweep result (LETHALITY_SCALE baked into DAMAGE_BY_DEGREE, battery n=40)

```
scale   in-band/13
1.0     1/13   (baseline / current main — reproduces the regression)
1.5     0/13
2.0     1/13
2.5     3/13   ← best
3.0     2/13
4.0     3/13
```

Non-monotonic → the battery is confounded by broken formation mechanics; no clean optimum exists yet.

## Best-scale (2.5) matchup breakdown — the diagnostic

```
RECOVERED (symmetric / pacing-driven):
  H1  Line vs Line (mirror)        45/55  t=2.6  OK   ← mirror now symmetric (was 60/32)
  H8  GappedLine vs Arrowhead    52.5/47.5 OK
  H10 Line vs Horseshoe            35/65  OK

STILL OUT (formation geometry — blowouts):
  H4  Horseshoe vs Arrowhead       10/87   ← encirclement geometry broken
  H5  RefusedFlank vs Horseshoe    85/15
  H6  RefusedFlank vs Line       22.5/77.5
  H7  GappedLine vs Line         97.5/2.5  ← gapped crushes line (wrong)
  H11 Arrowhead vs Horseshoe     82.5/15
  H2/H3/H9 (Arrowhead/Horseshoe vs Line and rev) all OUT
STILL OUT (ranged — volley not scaled, ED-822 territory):
  R1  Ranged vs Line              0/100
  R3  Ranged vs Ranged          67.5/32.5
```

**Battles now resolve in t ≈ 2.0–2.6 turns** (was 3.8–7.8) — lethality fix worked for tempo. The failures are concentrated in geometry-dependent formations (Horseshoe/Arrowhead/RefusedFlank/Gapped), exactly the mechanics the audit flags as unwired/unbuilt.

## Corrected diagnosis — what's actually binding

| Audit Issue | Status | Effect on battery |
|---|---|---|
| **Issue 1** Lethality (v19 drop) | **Fixed (mechanism); value provisional** | Fixes pacing + symmetric matchups → 1/13 → 3/13 |
| **Issue 4** Equal-speed contention no-op | unfixed | "Degenerate geometry"; cells overlap → angle/engagement-count errors → formation blowouts |
| **Issue 3** Cell-displacement ripple never built | unfixed | Penetration (Arrowhead/cavalry) is a stat bonus, not physical push → Arrowhead/Horseshoe wrong |
| **Issue 2** Within-side formation-hold unwired | unfixed | No discipline penalty for cells merging → formation integrity unmodeled |
| **Issue 5** rally/reform empty stubs | unfixed | Battles can only degrade, not recover |
| **Volley/ED-822** | out of Issue-1 scope | Ranged matchups (R1/R3) off |

The lethality **value** is gated on Issues 2–4: the battery confounds lethality with formation-geometry error, so the constant can't be locked until the mechanics are correct. Issue 1 and Issues 2–4 are **coupled**, not sequential.

## Supersession note

This finding **supersedes two prior framings**:
- `ed811_engagement_formula_resolution.md`'s R1–R4 "open design fork" — the engine settled on the degree-banded PP-233 model; that's confirmed in code.
- The "fix Issue 1 → battery recovers" reading — false; Issue 1 alone yields 3/13.

The engagement-damage *model* (degree-banded, mult-on-Power) is settled. What remains is **engine-mechanics correctness** (Issues 2–4) + **co-calibration** of lethality + **volley** (ED-822), then **canon reconciliation** (write the validated model + calibration into §A.7/PP-233, strike the additive §A.7 text).

## Remaining work — sequenced (multi-session; each ~1 session)

1. **Issue 4 — equal-speed cell-contention tiebreakers** (cheapest; high suspected impact). Re-introduce Jordan's v13 rule: size tiebreaker then random for equal-speed overlap; stop cells occupying the same grid cell. Likely removes a large chunk of the geometry blowouts.
2. **Issue 3 — cell-displacement ripple** (the puncture system). High-speed cell forces overlap → loser shifts back one cell along attacker vector; propagate with discipline check. Makes Arrowhead/cavalry penetration physical.
3. **Issue 2 — within-side formation-hold** with a *bad-facing* discipline trigger (not a blanket — that over-tuned 12/13→9/13 before).
4. **Co-calibrate LETHALITY_SCALE** against the battery once 1–3 land (the battery is then trustworthy). Target ~15%/turn casualties (audit Issue-1 target).
5. **Volley / ED-822** — separately, for the ranged matchups.
6. **Canon reconciliation** (Jordan ratifies) — §A.7 step 5/6 + PP-233 → the degree-banded model; record the calibrated LETHALITY_SCALE.

## Confidence & limits

- `[CONFIDENCE: high]` — regression reproduced (1/13), fix mechanism + sweep are direct measurements; matchup breakdown is the battery's own output.
- `[CONFIDENCE: high]` — Issue 1 necessary-not-sufficient: the OUT set is geometry-dominated, matching Issues 2–4 exactly.
- `[CONFIDENCE: medium]` — that Issue 4 is the highest-leverage *next* fix (inferred from the geometry-failure pattern; not yet tested by implementing it).
- Engine edits are local (`/home/claude/sim_v22.py`); **main is unchanged** (B6). Verification ledger at `/home/claude/sim_verification_ledger.json`.
- Freshness: mass-battle files confirmed fresh (declared SHA == HEAD); the bootstrap's stale-source warnings are non-mass-battle.
