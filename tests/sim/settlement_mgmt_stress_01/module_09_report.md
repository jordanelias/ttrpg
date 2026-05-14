# Module 09 Report — Extended timeline + pressure clocks + Accounting hook

**Date:** 2026-05-13
**Session:** Mode G Module 9 of `settlement_mgmt_stress_01`
**Module file:** `tests/sim/settlement_mgmt_stress_01/module_09_timeline.py`

**Canonical sources read at full depth:**
- `designs/territory/settlement_layer_v30.md` §7.1, §7.2
- `designs/provincial/clock_registry_v30.md` (canonical clock registry)
- `params/bg/clocks.md` (canonical clock environmental effects)

## Summary

Module 9 closes the largest meta-throughline coverage gap surfaced by M8's retroactive audit: **М-1 PRESSURE IS CONTINUOUS** had zero primary bindings across M1-M8 (only secondary in M4). Module 9 IS the pressure-tick substrate. **T-04 MS Decay, T-05 CI Accumulation, T-06 IP Accumulation, T-07 Turmoil** all land as primary bindings.

Module 9 also wires:
- **T-25 Generational Arc** (secondary; М-5) — the 30-year clock that wraps personal Renown accumulation into generational succession
- **§7.2 Succession System** — unmanaged-settlement Order decrement + protégé inheritance
- **The canonical per-season Accounting hook** that composes all prior modules' per-season state advances

## Bottom-up emergent validation — T35 canonical 30-year game simulation

The most important test in M9: **T35 runs 120 consecutive seasons (30 years) through `per_season_accounting` and verifies the resulting clock state matches §7.1's worked example to the integer.**

- MS at game-end: **42** (matches §7.1: *"30-year game = MS ~42 at game end (Fragile band)"*)
- IP at game-end: **80** (matches §7.1: *"30-year game: IP ~80 (Altonian preparation)"*)
- Generational Shift at game-end: **6** (matches §7.1: 30 years / 5-years-per-tick)

**The canonical numbers emerge from pure per-season tick functions without any target value being hardcoded.** This is the strongest possible bottom-up validation — the long-horizon dynamics produced by primitive operations match the design-doc prose to the integer.

## Isolation tests — 36/36 PASS

Highlights:
- T1: ClockState defaults match `clock_registry_v30` canonical start values (MS 72, CI 28, IP 20, Turmoil 0)
- T2–T4: MS year-boundary decay + rupture clamp
- T5–T7: CI conditional accumulation (gated on Church Mandate ≥ 3)
- T8–T9: IP recalibrated rate (+1 per **2** seasons, not per season)
- T10–T12: Turmoil battle-gated accumulation + cap
- T13–T14: Generational Shift 5-year boundary
- T15–T19: §7.1 attribute-penalty schedule (-1/-2/-3 at Year 10/20/30) + TS-50 exemption (P-15 metaphysical)
- T20–T21: §7.2 unmanaged-settlement Order decrement
- T22–T26: §7.2 protégé eligibility + cross-generational Renown inheritance (Renown ÷ 2 round down)
- T28: Accounting hook fires year-boundary clock ticks
- T29: Accounting hook fires 5-year-boundary Generational Shift
- T30: Accounting hook orchestrates M7 siege surrender at Order 0
- T31: Accounting hook orchestrates §7.2 unmanaged decrement
- T32: Accounting hook orchestrates M6 emergent event sweep
- **T35: 30-year canonical simulation matches §7.1 worked numbers exactly**
- T36: Decade-boundary M3 facility-expansion-cap reset

## Throughline bindings — primary closures

This module closes **all four М-1 clock throughlines** as primary bindings:

| Throughline | Canonical title | Module 9 mechanism |
|---|---|---|
| T-04 | MS Decay | `tick_ms_decay`: -1/year on year boundary |
| T-05 | CI Accumulation | `tick_ci_accumulation`: +1/season conditional on Mandate ≥ 3 |
| T-06 | IP Accumulation | `tick_ip_accumulation`: §7.1 recalibrated +1 per 2 seasons |
| T-07 | Turmoil | `tick_turmoil`: +1/season-with-inter-faction-battle |

Plus:

| Throughline | Canonical title | Module 9 mechanism |
|---|---|---|
| T-25 | Generational Arc | `tick_generational_shift` + `attribute_penalty_for_age` with TS-50 exemption |

## Meta-throughline coverage

- **М-1 PRESSURE IS CONTINUOUS** — **PRIMARY** (closes the gap surfaced by M8 retroactive audit). T-04/T-05/T-06/T-07 all subordinate to М-1; Module 9 implements all four ticks.
- **М-5 SCALES CONNECT THROUGH SUBSTRATE** — secondary (Generational Arc scales personal-standing accumulation into institutional reality at 30-year horizon).

## Updated meta-throughline tally across M1-M9

| Meta | Primary bindings | Modules | Status |
|---|---|---|---|
| М-1 | 1 | **M9** | **NEWLY BOUND PRIMARY** |
| М-2 | 2 | M2, M7 | covered |
| М-3 | 3 | M1, M2, M6 | covered |
| М-4 | 3 | M3, M4, M5 | covered |
| М-5 | 2 | M5, M8 | covered |
| М-6 | 0 primary | (secondary in M7, M8) | **gap remains** |

М-6 CHOICE IS FORCED is the last remaining primary-binding gap. This is structurally appropriate for the *settlement-management* sim — forced-choice throughlines (T-12 Practitioner Arc, T-13 Certainty Journey, T-14 Conviction Architecture) are character-layer scopes that belong in a different sim. Module 13 audit should confirm.

## The canonical Accounting hook — per-season composition

`per_season_accounting(SeasonContext) -> AccountingReport` is the canonical composition function. Its order of operations:

1. Advance season counter; determine year-boundary + 5-year-boundary + decade-boundary flags
2. **Pressure-clock ticks** (МSnaturally —1 substrate) — MS, CI, IP, Turmoil, Generational Shift
3. **Per-settlement state advances** — M4 Chapel half-Order accumulators, M6 governance-transition state machines, M7 siege ticks, §7.2 unmanaged-settlement Order decrements
4. **Event sweep** (M6 composition) — emergent events fire from state mutations of step 3
5. **Decade-boundary resets** — M3 facility expansion-cap drains every 10 years

Returns `AccountingReport` carrying fired events, surrendered sieges, completed transitions, parish ticks, unmanaged settlements, and a clock-state snapshot. Module 12 (faction integration) consumes the report to apply province-level effects.

**This single function composes 6 prior modules' per-season effects via shared state.** Bottom-up: no module's per-season logic depends on others — the Accounting hook is the per-season clock tick that calls them in canonical order.

## Findings NEW this session

### F17 — Clock-rate drift between settlement_layer §7.1 and clock_registry_v30

§7.1 explicitly recalibrates IP to +1 per 2 seasons (halved from the original +1/season rate). But `clock_registry_v30.md` and `params/bg/clocks.md` do not reflect this recalibration:

- `clock_registry_v30` lists IP start 20 (matches §7.1) and direction up, but doesn't document the rate change.
- `params/bg/clocks.md` shows IP effects by range but not the rate.

Neither file marks itself as superseded by §7.1's recalibration. **§7.1 is the post-recalibration canonical source.** Module 9 honors §7.1.

**Editorial decision needed:** propagate §7.1's recalibration into `clock_registry_v30.md` (or mark §7.1 as the governing source for clock rates). This joins the **documentation drift family** (F2, F13, F14, F16, F17 — five surfacings now).

### Other findings from prior sessions

| ID | Status | Module | Type |
|----|--------|--------|------|
| F1 | open | M1 | Canonical type drift |
| F2 | open | M1 | Stats schema |
| F3 | resolved | M2 | (PP-726 §2.1) |
| F4 | partial | M2 | Granularity (F6 blocks) |
| F5 | open | M2 | Edge-count math |
| F6 | open (Mode-C blocker) | M2 | Intra-YAML S-ID drift |
| F7 | open | M3 | §1.4.1 omits extras |
| F8 | open (info) | M4 | §1.5/§1.6 asymmetry |
| F9 | open (info) | M5 | Pacify formula |
| F10 | open | M5 | §3.2 omits extras |
| F11 | open | M5 | §3.3 Guilds Market ref |
| F12 | open | M6 | §4.5 omits extras |
| F13 | open | M6 | §4.5 prose pre-rebuild |
| F14 | open | M7 | §5.1 stale S-IDs |
| F15 | open | M7 | §2.2 omits City |
| F16 | open (info) | M8 | §4.5/§4.6 stale T-NN |
| F17 | open (info) | M9 | clock_registry vs §7.1 IP rate |

**Type-taxonomy drift family** (F1, F7, F10, F11, F12, F14) — 6 surfacings.
**Documentation drift family** (F2, F13, F14, F16, F17) — 5 surfacings.

## Audit — patterns crystallizing across 9 modules

Three audit-grade patterns are visible across F1-F17:

1. **Type-taxonomy drift family (F1, F7, F10, F11, F12, F14):** the §2.1 settlement-registry rebuild (PP-726) introduced three new types not in §1.2's canonical eight; downstream mechanical tables (§1.4.1 facility matrix, §3.2 governor eligibility, §3.3 subnational alignment, §4.5 Local Actor counts, §5.1 + adjacency §3 examples) all still reference the pre-rebuild canonical eight or pre-rebuild S-IDs. **One editorial pass closes 6 findings.**

2. **Documentation drift family (F2, F13, F14, F16, F17):** prose / counts / T-NN numbers / clock rates in design docs preserve pre-rebuild or pre-recalibration state. F14 spans both families (stale S-IDs are also type-taxonomy issues). **Refresh pass closes 5 findings.**

3. **Intentional asymmetries (F8, F9 — informational only):** §1.5/§1.6 effect-timing asymmetry and §3.2 Pacify floor()-redundancy are not defects but worth surfacing for documentation.

**The high-impact editorial fix is the type-taxonomy reconciliation** — F1 + F7 + F10 + F11 + F12 + F14 all close together. Module 13's NERS audit (Necessary/Robust/Smooth/Elegant) will likely highlight the *Smoothness* failure cost of these drifts.

## Module 9 data model (downstream contract)

```
ClockState (dataclass)              # ms, ci, ip, turmoil, gen_shift, seasons_elapsed
Tick functions:
  tick_ms_decay(state, is_year_boundary) -> int
  tick_ci_accumulation(state, church_mandate) -> int
  tick_ip_accumulation(state) -> int                  # +1/2 seasons recalibrated
  tick_turmoil(state, inter_faction_battle) -> int
  tick_generational_shift(state, is_5y_boundary) -> int

attribute_penalty_for_age(gen_shift, ts) -> int       # TS-50 exempts
unmanaged_settlement_tick(stats) -> int               # §7.2
is_eligible_protege(disposition, standing) -> bool   # §7.2
cross_generational_inheritance(predecessor_renown) -> int   # §7.2

SeasonContext (dataclass)            # bundles state for Accounting hook
AccountingReport (dataclass)         # output of one tick

per_season_accounting(ctx) -> AccountingReport       # canonical composition

THROUGHLINE_COVERAGE_BY_THIS_MODULE: Dict[T-NN, str]    # T-04, T-05, T-06, T-07, T-25
META_THROUGHLINE_COVERAGE_BY_THIS_MODULE: Dict[М-N, str]   # М-1 PRIMARY, М-5 secondary
```

## Ledger entries this session

~22 new entries. Coverage: 5 clock-start values (MS 72, CI 28, IP 20, Turmoil 0, GS 0); 4 clock-max values; tick rates and conditional thresholds; §7.1 generational thresholds + attribute penalties; TS-50 exemption threshold; §7.2 protégé constants; battle-consequence constants.

## Cumulative status after M9

- **9 modules verified · 280 isolation tests · ~190 ledger entries · 17 findings (1 resolved, 1 partial, 15 open) · ~36 action handlers + Accounting composition · 4 modules remaining.**
- **All 6 primary meta-throughlines now have at least secondary binding; 5 have primary; only М-6 remains primary-unbound (structurally expected — character layer).**
- **11 throughlines bound across 9 modules** (T-01, T-04, T-05, T-06, T-07, T-08, T-15, T-18, T-19, T-20, T-22, T-23, T-25; plus T-11/15a/15b/15c faction postures = 14-15 total).

## Next session — Module 10 (Existing-systems impact + Provincial Authority)

Force-full read: settlement_layer_v30 §8.1, §8.2 (Changes to Existing Systems / What Does NOT Change). Module 10 wires:
- Black markets / intelligence brokers / Thread exploitation sites (§4.7, §4.8, §4.9)
- Provincial Authority dual-tier (the M5 §3.1 "Provincial Authority" half — the national-faction-level controller of military deployment, taxation, legal framework, province-level Domain Actions)
- §8.1 / §8.2 cross-system impact catalogue (audit reference for Module 13)

**3 modules remaining** before Module 13 integration runner.
