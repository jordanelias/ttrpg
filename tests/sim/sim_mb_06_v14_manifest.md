# SIM-MB-06 v14 — Manifest

**Session:** 2026-05-13
**Iteration:** v13 → v14
**Commit scope:** simulation
**File:** `tests/sim/sim_mb_06_v14.py`

## Summary

v14 adds one structural change: **phase / tick architecture**. `TICKS_PER_PHASE = 6` defines a phase as the gallop-and-charge cycle (per historical research). Every 6 ticks within `run_battle` triggers a `phase_boundary` call that runs six empty hook stubs in canonical order, providing landing points for stamina, rally, reform, threadwork, morale, and rout-resolution mechanisms in subsequent cycles.

Empty hooks mean v14 has identical combat output to v13. Battery confirmed at 12/13 in-band at n=500 (same as v13). The deliverable is the structure; the mechanics land later.

## Historical grounding

The 6-tick phase length comes from cross-referencing several converging sources during this session's research:

- **Operational Studies Group (Napoleonic):** "It takes trotting cavalry 2 minutes to cross one hex (246 yards/min), while the actual charge (at a gallop) would only be the last two hexes and take 3 minutes (410 yards/min). Thus, a three-hex charge would take about 5 minutes in real time."
- **Wikipedia cavalry tactics:** Charge cycle = acceleration over 400m in 2 min + final gallop 150m + impact. Reform-to-charge-again adds 1-2 minutes per Napoleonic and earlier accounts of cycle-charging.
- **Hoplite phalanx exhaustion bound:** Sustained close combat caps at ~10-15 minutes before exhaustion forces rotation/breakdown (multiple sources; the science-and-fiction.org analysis is particularly clear that physical combat in armor is not sustainable beyond ~10 minutes without rotation).

→ One phase = one gallop-and-charge cycle (or its infantry equivalent: ephodos → krousis → doratismos → othismos → pararrhexis) = 5-6 ticks of close action + 1-2 ticks of reform = **6 ticks lock-in**.

A pre-modern battle is then ~3-6 phases = 30-90 minutes of active fighting, matching the historical battle-duration range (hoplite to medieval to early-modern).

## Tick budget within a phase

For cavalry (the calibration target):
1. **Tick 1-2:** Approach/closing (acceleration, infantry braces)
2. **Tick 3:** Impact (gallop hits the line — decisive moment for puncture/break)
3. **Tick 4-5:** Contact resolution (melee in place if not broken through)
4. **Tick 6:** Disengage/reform (winner exploits, loser routs, or mutual withdrawal)

For infantry (same 6-tick frame):
1. **Tick 1-2:** Approach
2. **Tick 3-4:** Initial clash and spear exchange
3. **Tick 5:** Sustained push (othismos)
4. **Tick 6:** Resolution (one side breaks or both withdraw)

## Phase-boundary hook order

Defined in `phase_boundary(unit_a, unit_b, phase_idx)`:

1. **stamina_check** — depletion accumulated over the 6 ticks of contact, applied. (Empty in v14; will land in a later cycle paired with combat-pool degradation based on stamina state.)
2. **morale_check_phase** — accumulated casualties + stamina state vs threshold. The existing per-tick morale degradation continues to run inside the turn loop; this is for phase-level accumulation.
3. **rout_resolution** — units with broken morale flee the field. Pursuit damage applies here.
4. **rally_check** — non-routed units with degraded morale attempt to rally and continue fighting.
5. **reform_check** — formation drift correction, broken sub-units re-cohere.
6. **threadwork_check** — narrative/agent threadwork at phase seams (Valoria-specific extension point).

All six are no-op stubs in v14. The order is canonical: stamina degrades first (drives morale), morale evaluates (drives rout), rout resolves (removes routed unit from further phases), rally happens for surviving degraded units, reform tidies formations, threadwork fires for narrative state.

## Why structure before mechanism

The depth-as-replacement design I started implementing earlier in the session (rear cells absorbing size-drops in `recalc_size`) was reverted. Historical research showed it was the wrong framing: depth's real role is **stamina-replacement**, not casualty-replacement. Rear ranks rotate forward to give exhausted front-rankers a chance to recover; that needs the stamina_check hook to exist before it can land cleanly. Wiring the phase structure first gives later work clean landing points instead of patchwork.

Same reasoning for rally, reform, morale-from-casualty-threshold, threadwork: they all want phase boundaries to fire at. Putting the boundaries in first means later cycles add one mechanism at a time, in the right place, without rewriting flow control each time.

## Return-dict expansion

`run_battle` return dict now contains:

```python
{"winner": "A"|"B"|"draw", "turns": int, "phases": int, "tick_in_phase": int}
```

Existing callers using only `winner` and `turns` are unaffected. The new fields let downstream code observe phase progression for diagnostics.

## Battery (n=500)

| Test | A vs B | Result | Target | Status |
|------|--------|--------|--------|--------|
| H1 | Line vs Line | 51.6 | 45-55 | ✓ |
| H2 | Arrowhead vs Line | 54.4 | 50-65 | ✓ |
| H3 | Horseshoe vs Line | 61.6 | 50-65 | ✓ |
| H4 | Horseshoe vs Arrowhead | 48.2 | 40-60 | ✓ |
| **H5** | **RefusedFlank vs Horseshoe** | **47.4** | **50-65** | **← OUT** |
| H6 | RefusedFlank vs Line | 56.8 | 45-60 | ✓ |
| H7 | GappedLine vs Line | 51.6 | 50-65 | ✓ |
| H8 | GappedLine vs Arrowhead | 49.6 | 45-60 | ✓ |
| H9 | Line vs Arrowhead | 48.2 | 35-50 | ✓ |
| H10 | Line vs Horseshoe | 37.6 | 35-50 | ✓ |
| H11 | Arrowhead vs Horseshoe | 51.0 | 40-60 | ✓ |
| R1 | Ranged vs Line | 34.6 | 30-50 | ✓ |
| R3 | Ranged vs Ranged | 47.2 | 45-55 | ✓ |

**In-band: 12/13** (same as v13). H5 unchanged at 47.4% — carries forward to a later cycle where stamina mechanism is expected to address it (since the current sim's run-to-destruction dynamic is the structural reason H5 doesn't track historical Theban-deep-column outcomes; stamina + rout-from-morale fixes that at the structural level).

## Carried forward to later cycles

- **Stamina mechanism** — depletes per contact tick, depth permits front-rank rotation to refresh stamina, low stamina degrades combat pool. Goes on `stamina_check` hook.
- **Morale-from-casualty-threshold** — historical 5-15% casualty rates trigger rout, not 100% destruction. Goes on `morale_check_phase` + `rout_resolution` hooks.
- **Rally** — degraded units attempt to recover and continue. Goes on `rally_check` hook.
- **Reform** — formation drift correction, separated sub-units re-cohere. Goes on `reform_check` hook.
- **Threadwork** — narrative/agent threadwork at phase seams. Goes on `threadwork_check` hook.
- **Cavalry charge cycle** — cycle-charging built into the phase structure (one phase = one charge attempt; multiple phases for cycle-charging). Wires once cavalry units exist in the battery.
- **H5 (RF vs HS)** — expected to track up to 50-65% once stamina + rout-from-morale lands and battles end at historical casualty rates rather than running to destruction.

## Drift risk

- The depth-pool code I wrote earlier in the session was reverted before commit. No residue in v14. Confirmed via diff vs v13.
- Empty hook stubs are explicit no-ops with `# noqa: ARG001` markers. They cannot accidentally fire mechanism.
- Return-dict addition is additive (existing callers unaffected) but downstream consumers should be aware of the new fields when they reach for them.

## Files

- `tests/sim/sim_mb_06_v14.py` — phase/tick structure wired
- `tests/sim/sim_mb_06_v14_manifest.md` — this file
- `tests/coverage_matrix.md` — v14 entry added
