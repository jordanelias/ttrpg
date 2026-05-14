# Module 03 Report — Facility tiers + capacity pressure (PP-rebuild +1)

**Date:** 2026-05-13
**Session:** Mode G Module 3 of `settlement_mgmt_stress_01`
**Module file:** `tests/sim/settlement_mgmt_stress_01/module_03_facilities.py`

**Canonical sources read at full depth:**
- `designs/territory/settlement_layer_v30.md` §1.4.1, §1.4.2, §1.4.3, §1.4.4

## Summary

Module 3 lights up the **improvement arm** of the player-action loop. It encodes §1.4's Institutional Facility Tiers (PP-rebuild +1):

- **§1.4.1 capacity matrix** — 4 tiers (Wing / Suite / Chamber / Billet) × 8 canonical settlement types (Seat / City / Town / Fortress / Cathedral / Port / Mine / Outpost), with Billet treated as unlimited.
- **§1.4.2 allocation rules** — Standing 6+ requires an available Wing slot; durable occupancy across seasons; faction leader auto-occupies one Wing at Seat settlements.
- **§1.4.3 capacity-pressure mechanic** — when full, the three canonical outcomes drive: (1) existing holder departs, (2) settlement expands capacity (the **canonical Improvement Action** with Treasury cost 300, +1 Wing, per-decade cap), (3) player accepts Prince-in-Waiting provisional rank with social-contest cost.
- **§1.4.4 cross-faction wing allocation** — Wings belong to the settlement's direct controller, not the province's. Cathedral inside Crown province remains Church-controlled. Ceded Wings still count against the ceding faction's capacity.

## Isolation tests — 25/25 PASS

| # | Test | Result |
|---|------|--------|
| T1 | Capacity matrix covers all 8 canonical types | PASS |
| T2 | Seat row matches §1.4.1 (Wing 3 / Suite 5 / Chamber 8 / Billet unlim) | PASS |
| T3 | City row matches §1.4.1 (Wing 1 / Suite 3 / Chamber 5 / Billet unlim) | PASS |
| T4 | Mine row matches §1.4.1 (Wing 0 / Suite 0 / Chamber 1 / Billet unlim) | PASS |
| T5 | Cathedral row matches §1.4.1 (Wing 1 / Suite 3 / Chamber 5 / Billet unlim) | PASS |
| T6 | base_capacity returns None for §2.1 extra types | PASS |
| T7 | effective_capacity falls Village → Town (provisional, F7) | PASS |
| T8 | Fortress-City unmapped (F7 gap) | PASS |
| T9 | Cathedral-City unmapped (F7 gap) | PASS |
| T10 | Village-count == 14 (registry-derived; corrects M1 F1 typo) | PASS |
| T11 | TIER_STANDING_MIN['Wing'] == CAPACITY_PRESSURE_TRIGGER_STANDING == 6 | PASS |
| T12 | FacilityState defaults occupied=0 across all tiers | PASS |
| T13 | is_full negative case | PASS |
| T14 | is_full positive at capacity | PASS |
| T15 | Billet tier never registers full (unlimited sentinel) | PASS |
| T16 | expand_institutional_capacity success path mutates state correctly | PASS |
| T17 | expand fails on insufficient_treasury (< 300) | PASS |
| T18 | expand fails on decade_cap_exhausted | PASS |
| T19 | advance_decade resets the cap counter | PASS |
| T20 | Three canonical CAPACITY_PRESSURE_OUTCOMES enumerated | PASS |
| T21 | Outcome 1 (existing departs) frees a Wing | PASS |
| T22 | Outcome 3 (prince_in_waiting) does not mutate state | PASS |
| T23 | §1.4.4 Wing belongs to direct controller (Church > Crown for Cathedral) | PASS |
| T24 | Ceded Wing belongs to allied faction | PASS |
| T25 | Improvement action carries faction_standing + renown signal | PASS |

## Findings NEW this session

### F7 — §1.4.1 matrix omits §2.1 extra types (Village / Fortress-City / Cathedral-City)

The §1.4.1 capacity matrix rows cover the canonical 8 settlement types from §1.2 (Seat, City, Town, Fortress, Cathedral, Port, Mine, Outpost). The §2.1 registry uses 3 additional types not in §1.2 — see Module 1 finding F1. These extra types account for **17 of 37 settlements** (46%):

- **Village** (14 settlements) — heavily used. Module 3 provisionally falls Village → Town (smallest-canonical-analogue interpretation). Plausible and low-risk; Town is the §1.2 "smaller settlement, local governance" entry.
- **Fortress-City** (1 settlement: S-014 Ehrenfeld) — composite. Capacity should plausibly be `max(Fortress, City)` per tier, but the canon doesn't say. **Surfaced as gap.**
- **Cathedral-City** (1 settlement: S-036 Himmelenger) — sovereign city-state, simultaneously a Cathedral. Capacity should plausibly be `max(Cathedral, Seat)` or higher given canonical-significance, but canon doesn't say. **Surfaced as gap.**

**Module 13 Mode D stress target:** the unmapped settlements are excellent degenerate-input cases. Mode D should verify the gap doesn't silently zero-out (zero Wings means no Standing-6 rank-holders can reside, which would silently prevent the entire inner-circle player progression for those settlements — that would be the "broken loop" failure mode).

**Editorial decision needed:** add §1.4.1 rows for the three extra types, OR resolve F1 by reclassifying §2.1 entries to canonical-eight types (and revisiting district-aggregation per F6).

### Module 1 F1 typo correction

M1's report claimed "Village (used heavily — 15 settlements)". The actual registry count is **14 Villages and 15 Towns**. The "15" was misattributed to Village. Module 3 T10 codifies the corrected 14. Module 1's F1 finding remains valid (3 extra types exist in registry but not in §1.2); only the per-type count was off.

## Findings from prior sessions revisited

- **F1, F2:** unchanged.
- **F3 RESOLVED** (Module 2).
- **F4 PARTIALLY RESOLVED** (Module 2).
- **F5 unchanged** — edge-count comment math (geography YAML).
- **F6 unchanged** — intra-YAML S-ID granularity drift (geography YAML).

F6 remains the most consequential blocker for Module 13 Mode C. F7 surfaces a related but distinct gap (canonical capacity matrix doesn't cover all registered types).

## Module 3 data model (downstream contract)

```
FACILITY_TIERS = ('Wing', 'Suite', 'Chamber', 'Billet')
TIER_STANDING_MIN -> Dict[tier, int]
_CAPACITY_BY_TYPE -> Dict[canonical-type, (Wing, Suite, Chamber, Billet)]
UNLIMITED_BILLET = -1 (sentinel)

base_capacity(settlement_type) -> Dict[str, int] | None
effective_capacity(settlement) -> Dict[str, int] | None   # F7 fallback included
PROVISIONAL_EXTRA_TYPE_MAPPING -> Dict[extra-type, canonical-type | None]

EXPAND_CAPACITY_TREASURY_COST = 300
EXPAND_CAPACITY_WING_DELTA = 1
EXPAND_CAPACITY_DECADE_CAP = 1
CAPACITY_PRESSURE_TRIGGER_STANDING = 6
PRINCE_IN_WAITING_SOCIAL_OB = 2
PRINCE_IN_WAITING_FAILURE_STANDING = 5
CAPACITY_PRESSURE_OUTCOMES = (existing_departs, expands, prince_in_waiting)

@dataclass FacilityState                                     # MUTABLE
  - is_full(tier) -> bool
  - slots_available(tier) -> int

@dataclass(frozen=True) ActionResult
  - success, reason, state_mutated
  - treasury_delta, faction_standing_delta, renown_delta
  - new_capacity

expand_institutional_capacity(facility, treasury) -> ActionResult
resolve_capacity_pressure(facility, outcome, treasury) -> ActionResult

@dataclass(frozen=True) WingControl
wing_belongs_to(wing) -> str                                 # §1.4.4 predicate

advance_decade(facility) -> None                             # Module 9 hook
```

## Player-action loop — improvement arm now live

Module 3 is the **first module with player-action handlers**. The loop signal flow:

```
1. Player invokes Domain Action 'Expand Institutional Capacity'
       |
       v
2. expand_institutional_capacity(facility, treasury_available)
       |
       v
3. ActionResult returned with:
       - state_mutated = True
       - treasury_delta = -300
       - faction_standing_delta = +1 (provisional)
       - renown_delta = +1 (provisional)
       - new_capacity = facility.capacity['Wing'] (post-mutation)
       |
       v
4. Module 12 (faction integration) consumes treasury_delta → faction Treasury
   Module 5 (governance) consumes faction_standing_delta → faction Order/Accord
   Module 8 (Stature) consumes renown_delta → player renown UI
       |
       v
5. New Wing now visible to player — Standing 6+ claimants can occupy it
   without triggering capacity pressure. Loop CLOSED.
```

Degenerate-loop test cases for Module 13 Mode D:
- **Broken loop**: action succeeds but `faction_standing_delta == 0` (the player did something but it didn't change their standing). Module 3 sets +1 by default; Mode D should detect if the chain breaks downstream (Module 5 or 12 zeros the signal).
- **Over-coupled loop**: expansion in one settlement cascades to faction-wide standing change disproportionate to the action (would require Module 11 Domain Echo misfire — Mode D territory).
- **Unreadable loop**: expansion succeeds but the new Wing is allocated to a different controller via §1.4.4 cross-faction rules (player loses the slot they paid for). Module 3 T23 confirms direct-controller rule; Mode D should stress it with hostile cross-faction control.
- **Decade-cap exhaustion**: T18 confirms the action fails gracefully when cap hit. Mode D should verify the failure surfaces a clear UI message rather than silently consuming Treasury.

## Ledger entries this session

12 new (40 total cumulative — 17 M1 + 11 M2 + 12 M3). Coverage:
- 8 facility capacity-table values (Seat Wing 3, Seat Suite 5, Seat Chamber 8, City Wing 1, City Suite 3, City Chamber 5, Mine Chamber 1, Cathedral Wing 1, Cathedral Suite 3, Cathedral Chamber 5)
- 3 expand-capacity constants (Treasury 300, +1 Wing, decade cap 1)
- 1 capacity-pressure trigger standing (6)
- 2 prince-in-waiting constants (Ob 2, fall-to-standing 5)
- The "three outcomes" enumeration count (3)
- Village-count correction (14)

## Next session — Module 4 (Church / parish / pastoral)

Force-full read: settlement_layer_v30 §1.5, §1.6, §1.7 + historical_precedents_analysis §1 (if it exists as canonical companion).

Module 4 consumes Module 3's FacilityState (Cathedral slot allocations) and adds Church's four-axis infrastructure layer + the Geneva-trap Parish Stability bonus + Pastoral Assumption Domain Action. This is the second improvement-arm action surface (Templar/Inquisitor/Governor installation are Church-side improvement actions).
