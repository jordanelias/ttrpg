# Mass Battle Sim — Comprehensive Audit (v5 → v22)

**Date:** 2026-05-14
**Scope:** every mechanic introduced v5 through v22, status in v22, supersession/drop analysis
**Trigger:** v22 multi-turn battery shows 1-2 of 13 matchups in-band despite v14 achieving 12/13. Audit identifies regressions.
**Terminology note:** the legacy term *atom* (used in v5-v10 manifests) was renamed to *subunit* in v11. This document uses *subunit* throughout. Cell remains cell.



## Method

For each version: read manifest/handoff, identify mechanics introduced. For each mechanic: grep v22 for token presence, then check call sites and active values. Categorize as **PRESENT** (active in execution path), **PRESENT-NOOP** (code exists but never called or has no effect), **SUPERSEDED** (replaced by named newer mechanic), or **DROPPED** (removed or rendered non-functional without successor).

## Summary table

| Mechanic | Intro | v22 Status | Notes |
|---|---|---|---|
| Bii pool formula (POOL_VARIANT) | v5 | PRESENT | C-ii default since v6 |
| Side mirroring (oriented_pattern) | v5 | PRESENT | |
| Per-cell movement (cell_offsets) | v5 | PRESENT | |
| 25×25 battlefield + 5-cell buffer | v5 | PRESENT | |
| Halt-cell mirror bug fix | v6 | PRESENT | |
| Per-cell facing (cell_facing_vec) | v6 | PRESENT | |
| Engagement angle FRONT/FLANK/REAR | v6 | PRESENT | Renamed GREEN/YELLOW/RED in v10 octagon |
| ANGLE_DEF_MOD = {0,-1,-2} | v6 | PRESENT | |
| Pool variant C-ii | v6 | PRESENT | Active default |
| Tip support gap (TIP_SUPPORT_GAP=2) | v7 | PRESENT | Default no-op at gap=2 |
| **F-i: Cell support stacking** | v8 | PRESENT | SUPPORT_WEIGHTS={1:1.0, 2:0.7, 3:0.5} |
| **F-ii: Puncture (pool bonus)** | v8 | PRESENT | Pool bonus only — no cell displacement |
| **F-iii: Cascading sub-phases** | v8 | PRESENT | CASCADING_ENABLED, MAX_SUB_PHASES=5 |
| Unit-type field (melee/ranged) | v9 | PRESENT | |
| Phase 2 Volley (VOLLEY_TN=6) | v9 | PRESENT | |
| Historical battery script | v9 | **DROPPED** | Only `sim_mb_06_v9_battery.py` exists — no v22 equivalent until I wrote one this session |
| SHAPE_OFF_MOD removed | v10 | SUPERSEDED | Replaced by geometric mechanisms (correct) |
| Octagon facing model | v10 | PRESENT | |
| Per-cell octagon angle (`_per_cell_angle_mod`) | v11 | PRESENT | Called in resolve_engagements |
| Vector halt-at-contact (`halt_before_enemy`) | v11 | **PRESENT-NOOP** | Function body is essentially a no-op since v11 ("over-run correction disabled") |
| Ranged melee penalty (pool/3) | v11 | PRESENT | Strengthened from /2 to /3 in v12 |
| Column-local targeting | v12 | PRESENT | Each cell maintains starting column |
| **Cross-side cell contention** | v13 | **PRESENT-WEAK** | Fires but only resolves on strict speed differential; equal-speed overlaps PERSIST (tied case is no-op) |
| **Within-side formation hold (`resolve_internal_collisions`)** | v13 | **DROPPED** | Implemented but NEVER INVOKED ("over-tuned battery 12/13→9/13"). Still present, still uncalled. |
| Snapshot pre-offsets (`_prev_offsets`) | v13 | PRESENT | Used by contention revert |
| TICKS_PER_PHASE=6 architecture | v14 | PRESENT | |
| `phase_boundary` dispatcher | v14 | PRESENT | Called every 6 ticks |
| `stamina_check` hook | v14 | PRESENT (v15 filled) | |
| `morale_check_phase` hook | v14 | PRESENT (v15 filled) | |
| `rout_resolution` hook | v14 | PRESENT (v15 filled) | |
| **`rally_check` hook** | v14 | **EMPTY STUB** | Never implemented |
| **`reform_check` hook** | v14 | **EMPTY STUB** | Never implemented |
| **`threadwork_check` hook** | v14 | **EMPTY STUB** | Never implemented |
| G-1 Stamina (per-tick drain) | v15 | PRESENT but RE-MODELED | Original: 16/tick uniform. v22: per-contact-cell (variable). Different semantic |
| Stamina phase-boundary recovery | v15 | PRESENT | Recovery=8 per reserve rank |
| Stamina exhausted pool penalty (-1D) | v15 | PRESENT | |
| G-2 Rout-at-casualty (20%, exhausted) | v15 | PRESENT | ROUT_FLOOR_LOSS_PCT=0.20 |
| Pursuit damage on rout (flat Power) | v15 | SUPERSEDED | v22 cavalry pursuit (G-11) replaces |
| Continuous effective_size | v16 | PRESENT | Float, not floored |
| **LETHALITY_SCALE=0.10** | v16/v17/v18 | **DROPPED v19** | Removed without compensating for HP model change → **root cause of decisive-battle failure** |
| Casualty-pct morale triggers (30%/50%) | v16 | PRESENT | |
| Multi-turn structure (run_multi_turn_battle) | v16 | PRESENT | |
| h_per_size = min(Disc,Cmd)+DR | v16 | PRESENT | |
| **HP model: Size × h_per_size (~5)** | v14 | **SUPERSEDED v19** | Replaced by BLOCK_SIZE=100 (20× inflation) |
| **HP model: Size × BLOCK_SIZE (100)** | v19 | PRESENT | Without lethality compensation |
| v20 stamina recovery, between-turn | v20 | PRESENT | BETWEEN_TURN_STAMINA_RECOVERY=30 |
| v21 simultaneous resolution (centroid cache, simultaneous HP/morale) | v21 | PRESENT | Eliminated BIAS-1 |
| v22 multi-unit orchestrator | v22 | PRESENT | run_multi_unit_battle |
| v22 freed-attacker (flank -1D) | v22 | PRESENT | Non-Fast victors |
| v22 morale cascade (Ob 1) | v22 | PRESENT | |
| v22 rout contagion (-1 braked) | v22 | PRESENT | |
| v22 cavalry pursuit (G-11) | v22 | PRESENT | Speed field, recall Ob 2, rearguard -2D |

## Critical issues requiring action

### Issue 1 — LETHALITY_SCALE dropped without HP-model compensation (v19)

**What:** v17 introduced `LETHALITY_SCALE = 0.10` to calibrate ~15% casualties per 3-phase engagement. v18 kept it. **v19 dropped it** alongside switching HP model from `Size × h_per_size` (~5 HP) to `Size × BLOCK_SIZE` (100 HP) — a 20× HP inflation. Rationale stated in v19 header: "HP = TroopCount; damage = soldier casualties (no scaling)." But the damage formula `(1+Power)-DR ≈ 3-5 per success` was unchanged, applied to 20× more HP.

**Effect:** single-engagement `run_battle` cannot produce a decisive outcome in 18 ticks. The v9-v18 historical battery (calibrated against decisive single engagements) returns 100% draws on v22. Multi-turn structure was added to compensate but the calibration was never redone — the v22 multi-turn battery shows 2/13 in-band because formation advantages now accumulate over 5-10 turns and amplify into landslides.

**Severity:** highest. This single change explains the entire battery regression.

**Fix options:**
1. Re-introduce damage scaling tuned for multi-turn target (~15% per battle turn, ~30-35% at rout)
2. Reduce BLOCK_SIZE to a value that makes single-engagement damage proportional
3. Increase damage formula magnitude (multiply success damage by ~5×)

### Issue 2 — Within-side formation hold never wired (v13)

**What:** `resolve_internal_collisions` is implemented on `Subunit` but `0 call sites`. Jordan's design (v13 manifest, quoted): "a cell of troops joining another cell of troops, then that cell will have a vector that faces the midpoint of that troop... subunits abandoning their subformation where cells merge partially/completely into other cells is a tactical failure... this comes down to discipline." Was disabled because it "over-tuned battery 12/13 → 9/13" without a paired discipline-gated trigger.

**Effect:** within-side formation cohesion is not modeled. Cells of the same unit can merge into each other (the "tactical failure" Jordan flagged) with no discipline penalty.

**Severity:** medium. Affects formation integrity over time but not directly decisive.

**Fix:** wire `resolve_internal_collisions` with a bad-facing trigger (only apply discipline penalty when the failure is geometrically real, not as a blanket).

### Issue 3 — Cell displacement / ripple effect never built (v13 deferred)

**What:** Jordan's v13 design (quoted in manifest): "if a phase ends and a subunit cell like cavalry is occupying the same spot as an opponent, then the opponent cells will shift back to accommodate them." Documented as deferred: "Charge-through (cavalry past static infantry) and end-of-phase displacement: deferred — no cavalry in current battery."

Now cavalry exists (v22 G-11). But displacement still isn't built. The v22 cell contention only handles overlap on strict speed differential (reverts loser to prev position); it does NOT ripple displacement through neighboring cells.

**Effect:** the puncture system is incomplete. F-ii in v8 added a pool bonus from speed differential but no physical displacement. Cavalry that pierces a line doesn't push cells out of the way — it just gets a +D bonus and stops at adjacency.

**Severity:** high for Arrowhead/cavalry mechanics. Penetration is not modeled physically; only as a stat bonus.

**Fix:** implement displacement ripple: when a high-speed cell forces overlap with a lower-speed cell, the loser shifts back one cell along the attacker's vector. If that displaces another cell of the loser's unit, propagate (with discipline check for chain length).

### Issue 4 — Equal-speed cell contention is a no-op (v13)

**What:** `resolve_cross_side_contention` skips ties (`if a_speed == b_speed: continue`). Verified by trace: Arrowhead vs Line at speed-1 each produces 5-16 cells of cross-side overlap per tick that persist post-contention.

**Effect:** cells from opposing sides occupy the same grid positions during engagement. The find_contacts function then treats these as in-contact (but with degenerate geometry). Octagon facing computes angles between cells at the SAME position. Encirclement counts may be inflated.

**Severity:** medium. Doesn't crash but produces sloppy geometry that interacts badly with the angle and engagement-counting mechanics.

**Fix:** Jordan's full v13 rule specifies size tiebreaker, then random. Re-introduce these for equal-speed cases.

### Issue 5 — Three phase-boundary hooks remain empty stubs (v14)

**What:** `rally_check`, `reform_check`, `threadwork_check` defined in v14 as no-op stubs. v15 implemented stamina_check and morale_check_phase. The other three never got mechanics.

**Effect:** units don't rally (degraded morale never recovers within a battle), don't reform (formations don't re-cohere after disruption), threadwork doesn't fire (no narrative state integration).

**Severity:** medium. These were planned mechanics with documented behaviors. Their absence means battles can only degrade, not recover.

**Fix:** implement minimum-viable versions — rally as `Command check Ob 2` (canonical: §A.4), reform as a discipline-gated check to restore cells to original positions after non-engaged ticks.

### Issue 6 — Historical battery not maintained (v9 → v22)

**What:** `tests/sim/sim_mb_06_v9_battery.py` exists; no v22 equivalent until I wrote `tests/sim/battery_v22.py` this session. The historical-accuracy spec in `tests/sim/sim_mb_06_v9_historical_spec.md` was the calibration target for v9-v15 (12/13 in-band achieved). After v16's multi-turn shift, the battery was never updated to test multi-turn outcomes.

**Effect:** between v16 and v22, formation-matchup correctness was untested. The v20-v22 work focused on different surfaces (bias, multi-unit, pursuit) without re-checking that core matchups still worked.

**Severity:** medium. Process gap, not a code defect.

**Fix:** keep `battery_v22.py` updated per version, treat as required gate before commit.

### Issue 7 — `halt_before_enemy` is a no-op since v11

**What:** function body comment says "over-run correction disabled." The function is called twice but does nothing.

**Effect:** cells continue past the contact line into enemy positions, contributing to the persistent overlap (Issue 4).

**Severity:** low. Redundant with `resolve_cross_side_contention`, but documents intent.

**Fix:** delete or implement.

## Other observations

- **STAMINA_DRAIN model changed** v15 → v20: from `16/tick uniform` to `1/contact-cell`. Different semantic — wide-contact formations now drain faster (GappedLine penalized more than Horseshoe). Not a regression per se but worth documenting that v15's calibration is no longer valid.

- **`_moved_this_turn` tracking** (v13) only marks cells that ACTUALLY moved (not halted). Cells that hit the contact line and stopped advancing are not counted, which interacts with contention's "stale" check. Worth a trace pass.

- **POOL_VARIANT C-ii** uses `max(base × 0.5 × engage_frac, base × troops_frac × engage_frac)`. The 0.5 is uncited (not in ledger). Should be canonical or removed.

## Priority order for next session

1. **Fix Issue 1 (lethality calibration)** — the foundational issue. Without this, no other fix matters because the battery can't be trusted.
2. **Re-run battery** — see if the v8-v15 mechanics that were correct now produce correct results.
3. **Fix Issue 3 (cell displacement ripple)** — completes the puncture system Jordan described.
4. **Fix Issue 4 (equal-speed tiebreakers)** — addresses persistent overlap.
5. **Fix Issue 5 (rally/reform implementations)** — these have canonical mechanics (§A.4) and clear interfaces (the hooks already exist).
6. **Address Issue 2 (within-side formation hold)** — needs a bad-facing trigger before re-enabling.
7. **Issue 6 (process)** — make `battery_v22.py` part of the standard sim-version workflow.

[ASSUMPTION: the LETHALITY_SCALE drop in v19 is the primary regression — basis: file header explicitly notes the change; v17-v18 had it active; v22 single-turn run_battle produces 100% draws which matches the predicted effect]
[ASSUMPTION: `resolve_internal_collisions` not being called is intentional but unresolved — basis: v13 manifest documented disabling it pending bad-facing trigger; no trigger has been added since]
[CONFIDENCE: high on Issues 1, 2, 4, 5, 7 — verified by code reading + execution traces. Medium on Issue 3 — Jordan's mention of "puncture with cell displacement ripple effect" matches v13 deferred design but I haven't found explicit ripple-propagation spec in repo]
