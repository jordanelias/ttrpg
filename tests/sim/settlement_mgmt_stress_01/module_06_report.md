# Module 06 Report — Settlement events + Thread ops + Local Actors

**Date:** 2026-05-13
**Session:** Mode G Module 6 of `settlement_mgmt_stress_01`
**Module file:** `tests/sim/settlement_mgmt_stress_01/module_06_events.py`

**Canonical source read at full depth:**
- `designs/territory/settlement_layer_v30.md` §4.1, §4.2, §4.3, §4.4, §4.5

## Summary

Module 6 wires the problem-solve arm of the player-action loop via canonical Settlement Events (§4.3), Thread Operations at settlement scope (§4.4), and Local Actor Disposition tracking (§4.5).

**Architectural commitment for this module: BOTTOM-UP GRANULAR EMERGENT.** Every event-trigger is a pure predicate on settlement state. No event "knows" about another. Composition emerges from the per-season sweep:

```
season N state -> predicate sweep -> fired event list -> resolution handlers
                                                                  |
                                                                  v
                                                         state mutations
                                                                  |
                                                                  v
season N+1 state -> predicate sweep -> potentially different fired list -> ...
```

T43 validates this empirically: a settlement at (Prosperity=0, Order=1) fires Famine at season N. The Famine resolution applies Order −1 automatically per §4.3. Season N+1 begins at (Prosperity=0, Order=0), and the same predicate sweep — unchanged code — produces both Famine AND Local Revolt firings. **The chain emerges from atomic predicates; nothing in the codebase anywhere connects Famine to Revolt explicitly.** This is the structural property Jordan's scope addendum requires.

## Isolation tests — 43/43 PASS

(See module_06_events.py run_isolation_tests for full set — T1 through T43.)

Highlights:
- T10: registry-wide sweep against mixed state produces 4 distinct event firings (Famine + Flourishing + Raid + Revolt) without any event-to-event coupling
- T18-T19: Disestablishment mode applies Order −1 for 2 consecutive seasons, then activates Accord growth — the multi-season state machine works
- T23: Thread-op cap (±1 per stat per season per §4.4) correctly refuses a second Weaving in the same season
- T26-T27: Community Organizing gated by province PT ≤ 2 (low-PT province succeeds; high-PT blocked)
- T43: **the emergent Famine → Revolt chain** — atomic predicates compose via state mutation

## Findings NEW this session

### F12 — §4.5 Local Actor table omits §2.1 extra types

Same gap class as F1 / F7 / F10 / F11. The §4.5 Local Actor count table uses §1.2 canonical eight types (Seat/City/Town/Fortress/Port/Cathedral/Mine/Outpost). §2.1 registry contains 3 extra types (Village, Fortress-City, Cathedral-City). Module 6's `local_actor_count` returns None for extras; `effective_local_actor_count` falls back to a provisional mapping (Village → 1 like Town; Fortress-City → 2; Cathedral-City → 2).

This is now the **fifth** distinct surfacing of the same type-taxonomy hygiene gap. Editorial pass on §1.2 / §2.1 type alignment is overdue.

### F13 — §4.5 prose count is pre-PP-rebuild

§4.5 states *"Total: ~45–50 across 36 settlements."* Two errors:

1. **"36 settlements"** is the pre-PP-rebuild count. Post-rebuild canonical count is **37** per §2.1 summary (35 Kingdom + Himmelenger + Schoenland).

2. **"~45–50 actors"** doesn't match the post-rebuild registry. Computing the §4.5 table × actual registry yields **25 Local Actors** from canonical-eight types alone (Seat × 2 + City × 2 + Town × 1 + Fortress × 1 + Port × 0 + Cathedral × 0 + Mine × 0 + Outpost × 0 = 4 + 4 + 15 + 2 + 0 + 0 + 0 + 0 = 25). The "~45–50" estimate appears to predate the PP-rebuild §2.1 reorganization, where standalone Port / Cathedral / Mine / Outpost settlements were collapsed into composite types (Fortress-City, Cathedral-City) and into sub-features (Mines now districts within parent settlements).

Adding F12's provisional fallback: +14 (Village × 1) + 2 (Fortress-City) + 2 (Cathedral-City) = 18 → grand total 43. Still well below 45–50.

**Editorial decision needed:** refresh §4.5 actor counts to match the post-rebuild §2.1 registry. Likely the correct revision either:
- Adds Village / Fortress-City / Cathedral-City rows to the §4.5 table (resolving F12 in the same pass), bringing total to ~43, OR
- Increases per-type actor counts (e.g., Village 2 instead of 1) to reach the "~45–50" range, OR
- Updates the prose total to match a recomputed per-registry sum.

The fact that the prose estimate is so far off suggests the §4.5 table itself may also need refreshed counts.

## Findings from prior sessions revisited

- **F1, F2, F5, F6, F8, F9, F10, F11:** unchanged.
- **F3 RESOLVED** (M2).
- **F4 PARTIALLY RESOLVED** (M2).

The cumulative finding ledger now stands at **13 findings** (F1–F13). F1, F7, F10, F11, F12 all surface the same canonical type-taxonomy drift pattern.

## Bottom-up architectural notes

Three structural choices in Module 6 are worth flagging for downstream modules:

### Event predicates are pure
None of the predicates depend on globally-stored state. `predicate_famine(stats)` is a pure function of one settlement's stats. This means the per-season sweep can be parallelized (Module 13 batch runner can fork settlements without coordination overhead) and the event log is replayable from state snapshots.

### Multiple events can fire per settlement per season
The sweep produces a `List[FiredEvent]`, not `Optional[FiredEvent]`. A Cathedral-typed settlement at Prosperity=0 fires both Famine AND (if CV changed) Religious-Event in the same season. The Scene Slate consumer (Module 12) prioritizes within the firing list, but Module 6 doesn't impose an artificial single-event constraint.

### Resolution effects respect stat clamps
All resolution handlers route stat mutations through `max(STAT_MIN, ...)` / `min(STAT_MAX, ...)`. A Famine at Order=0 doesn't push Order to −1; the predicate fires once and the resolution clamps. This makes the predicates idempotent against repeated firing.

### Thread-op cap is the emergence safety valve
§4.4's `Cap: ±1 per settlement stat per season from Thread operations` is enforced via the `delta_already_applied_this_season` parameter. This prevents an aggressive Church Mending strategy from blowing up Prosperity in one season. It is a CANONICAL constraint on emergence — the design wants emergence to feel earned, not exploited.

## Module 6 contribution to the player-action loop

Cumulative action-handler count: **22** (1 M3 + 6 M4 + 6 M5 + 9 M6).

| Module | Action | Arm |
|---|---|---|
| M6 | `resolve_famine` | Problem-solve (automatic on predicate) |
| M6 | `resolve_local_revolt` | Problem-solve (governor or garrison) |
| M6 | `resolve_flourishing` | Problem-solve (rewards trigger) |
| M6 | `resolve_rm_governance_transition` (3 modes) | Problem-solve (player choice) |
| M6 | `apply_templar_interrupt` | Problem-solve (Church cancels rival) |
| M6 | `attempt_niflhel_detection` | Problem-solve (Investigation) |
| M6 | `apply_thread_op` (7 ops) | Maintenance / Problem-solve |

(Counting Thread ops as 1 action with 7 variants rather than 7 separate actions.)

### The emergent player loop is now visible end-to-end

```
Player at Seat S-001 governs Crown territory.
  Season 1: Player Develops (Prosperity 3 → 4). Disposition with local
            actors trends +1 (governs + order improves).
  Season 2: Player Pacifies (Order 3 → 4). Player Fortifies (Defense 2 → 3).
            Two governance actions this season because companion-governor
            (M5).
  Season 3: Adjacent Hafenmark army marches to S-003. Defense=1 → Raid
            predicate would fire next season if Defense reaches 0.
            Player chooses Lock (Thread op) → Defense 3 → 4. Raid averted.
  Season 4: Cathedral S-003 (under Church management per M5 grant) accrues
            +1 Piety per season. Player Crown faction's PT vs Church
            Piety divergence widens.
  Season 5: Church installs Chapel in S-004 Kronmark (M4 install action).
            Geneva trap activates: +0.5 PT/season to Church AND +0.5 Order/
            season to Crown's settlement.
  Season 8: Chapel accumulator triggers +1 Order at Kronmark.
            Crown player gains renown (Module 8 binds the +1 renown signal).
            Church gains +4 PT cumulative. CI=80, approaching mass-seizure.
  Season 9: Crown player attempts seizure: Cathedral-installed seizure-Ob
            modifier is −2 (M4). High-tier infrastructure becomes
            expensive to remove — strategic tension.
```

Every transition in that loop fires a canonical predicate, returns an `ActionResult` with `faction_standing_delta` and `renown_delta` signals, and mutates state in a way the next season's predicate sweep responds to. **No part of this chain is authored — it emerges from M3/M4/M5/M6 atomic mechanisms composing.**

## Ledger entries this session

23 new (123 total cumulative — 17 + 11 + 20 + 26 + 26 + 23).

Coverage:
- 2 travel-cost constants (intra 0, per-province 1)
- 4 event-threshold constants (Famine 0, Raid 0, Revolt 0, Flourishing Order 5)
- 1 Flourishing prosperity threshold (4)
- 1 Flourishing Disposition bonus (+1)
- 1 Mine surplus Prosperity threshold (3)
- 1 Mine surplus Treasury per season (50)
- 1 Fortress mobilize Defense Ob (2)
- 4 Governance Transition mode constants (Disestablishment penalty seasons 2, PT immediate cost 1, Accord half/season post 1, Transformation duration 4)
- 4 Consensus Delay constants (1 season, waiver Mandate 1, Presence loss 1, emergency-action set count 3)
- 1 Thread-op cap (1)
- 1 Niflhel detection evidence threshold (3)
- 1 Faction emergence Disposition threshold (3)
- 1 Actors-from-canonical-eight worked sum (25)

## Next session — Module 7 (military granularity)

Force-full read: settlement_layer_v30 §5.1, §5.2 (Invasion and Defense, Garrison and Defense). Module 7 picks up:
- Settlement-scoped Mass Battle resolution (the Raid/Siege event triggers from M6 § 4.3)
- Garrison mechanics (the `garrison_present` flag in M6's `resolve_local_revolt` becomes a settled mechanic here)
- §5.1 Invasion sequencing — uses M2's EDGES (army movement on the adjacency graph)
- Bypass / Assault / Siege resolution at settlement scope (settlement_adjacency_v30 §2 mass-battle-at-settlement integration)

This will bring the **maintenance arm** more fully online (Fortify already maps to Module 5; Garrison reinforcement is a Module 7 maintenance action).

**7 modules remaining** before Module 13 integration runner.
