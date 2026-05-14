# Module 05 Report — Dual-authority governance

**Date:** 2026-05-13
**Session:** Mode G Module 5 of `settlement_mgmt_stress_01`
**Module file:** `tests/sim/settlement_mgmt_stress_01/module_05_governance.py`

**Canonical sources read at full depth:**
- `designs/territory/settlement_layer_v30.md` §3.1, §3.2, §3.3

## Summary

Module 5 brings the **maintenance arm** of the player-action loop live and adds the **governance-change problem-solve arm**. Encodes:

- **§3.1** two-tier authority model (Provincial Authority + Settlement Governor)
- **§3.2** governor assignment by Standing tier (Operative/Counselor/Lieutenant/Successor); four governance actions (Develop / Fortify / Pacify / Administer) with canonical Ob formulas; player-as-governor + companion-governor + Bishop-Governor mechanics
- **§3.3** seven subnational factions (Church / Guilds / Ministry / Löwenritter / RM / Wardens / Niflhel); Grant / Revoke management Domain Actions; RM cell resilience; contested-management framework

Also upgrades the M4 `GovernorState` stub to the canonical type (with standing, player/companion/bishop flags, managing-subnational reference, leader-approval flag).

## Isolation tests — 35/35 PASS

| # | Test | Result |
|---|------|--------|
| T1 | Four GovernorStanding tiers exist | PASS |
| T2 | tier_for_standing maps 0-5 correctly | PASS |
| T3 | ELIGIBLE_TYPES_BY_TIER matches §3.2 exactly | PASS |
| T4 | Standing 0 cannot govern anything | PASS |
| T5 | Counselor can govern Town, not City | PASS |
| T6 | Successor can govern Seat | PASS |
| T7 | Extra types (Village/Fortress-City/Cathedral-City) unmapped | PASS |
| T8 | develop_ob(0) == 1 | PASS |
| T9 | develop_ob(4) == 3 | PASS |
| T10 | fortify_ob(3) == 2 | PASS |
| T11 | pacify_ob(0) == 4 | PASS |
| T12 | pacify_ob(3) == 1 | PASS |
| T13 | pacify_ob(5) clamps at min 1 | PASS |
| T14 | Administer Ob is flat 2 | PASS |
| T15 | Develop success increments Prosperity | PASS |
| T16 | Develop clamps at STAT_MAX | PASS |
| T17 | Pacify success increments Order | PASS |
| T18 | Administer success sets no-decay flag + reveals conviction | PASS |
| T19 | Develop failure: no state mutation | PASS |
| T20 | Seven canonical subnational factions | PASS |
| T21 | Church natural type is Cathedral only | PASS |
| T22 | Guilds natural types exclude Market (F11) | PASS |
| T23 | Ministry order_decay_modifier == -1 | PASS |
| T24 | Löwenritter passive_defense_bonus == 1 | PASS |
| T25 | Wardens detection_band_shift == 1 | PASS |
| T26 | RM and Niflhel are covert | PASS |
| T27 | Löwenritter province does NOT retain military/legal | PASS |
| T28 | Grant management Ob is 1 | PASS |
| T29 | Revoke management Ob = ceil(Influence/2) | PASS |
| T30 | Grant management action succeeds | PASS |
| T31 | Revoke management applies Order -1 | PASS |
| T32 | Revoke fails on roll < Ob | PASS |
| T33 | RM cell resilience triggers at ≥ 3 presences | PASS |
| T34 | Successor blocked without leader approval | PASS |
| T35 | Successor succeeds with leader approval | PASS |

## Findings NEW this session

### F9 — §3.2 Pacify Ob formula notational quirk (informational)

§3.2 Pacify Ob is stated as `floor((3 − Order) + 1), min 1`. For integer Order in [0, 5], the floor is mathematically redundant — `(3 − Order) + 1` is always integer, and floor of an integer is the integer. The min-clamp at 1 IS load-bearing for Order ≥ 3 (where the raw value drops to 1 or below).

Module 5 implements `(3 - order) + 1` clamped at 1. Same result as the canonical formula. **F9 is informational only** — no functional divergence from canon. Worth surfacing if editorial wants to clean the formula presentation.

### F10 — §3.2 governor-eligibility table omits §2.1 extra types

Same gap class as F7 (which was about §1.4.1 facility capacity). §3.2's standing-tier eligibility table uses the §1.2 canonical eight settlement types. The §2.1 registry contains three extra types (Village, Fortress-City, Cathedral-City) — affecting 17 of 37 settlements (46%).

Module 5 surfaces the gap explicitly: `is_eligible_governor` returns False for extra types at any standing. **No silent reconciliation.** Module 13 Mode D should stress-test the gap — the failure mode is that 17 settlements cannot have ANY governor assigned (since no canonical Standing tier maps to their type), which would silently block 46% of the player-loop maintenance arm.

Provisional mapping surfaced (sim-side; not canonical):
- Village → Counselor (analogous to Town)
- Fortress-City → Successor (composite, canonical Cathedral-equivalent given Ehrenfeld's province-primary role)
- Cathedral-City → Successor (Himmelenger as Confessor's seat)

### F11 — §3.3 Guilds row lists pre-PP-726 'Market' as a settlement type

§3.3 Guilds row lists natural settlement types as "City, Port, Market, Mine". **Market is NOT in §1.2's canonical eight types.** Per PP-726, Market is a sub-feature (district within a settlement) per `settlement_layer_v30 §2.2` sub-features registry, not a settlement type itself.

Module 5 surfaces this by omitting Market from the Guilds natural-types tuple (`('City', 'Port', 'Mine')`). Editorial decision: §3.3 Guilds row should be amended to remove Market (and Market access handled at sub-feature level), OR Market should be promoted to §1.2 as a settlement type (unlikely given PP-726's siege-target rationale — Market is sub-settlement).

This is the **third instance** of the §2.1 / §1.2 type-list drift problem (F1, F7, F10 are about extra types in §2.1 not in §1.2; F11 is about a pre-PP-726 type still mentioned in §3.3 that was eliminated by PP-726). All four findings point to the same canonical hygiene need: a single comprehensive type taxonomy review.

## Findings from prior sessions revisited

- **F1, F2, F5, F6, F8:** unchanged.
- **F3 RESOLVED** (M2).
- **F4 PARTIALLY RESOLVED** (M2).
- **F7 unchanged** but now joined by **F10** at the same gap class.
- **F11 NEW** as a related drift in §3.3.

## Module 5 data model (downstream contract)

```
GovernorStanding (enum)                       # 4 tiers
TIER_STANDING_MIN                              # {tier: int}
ELIGIBLE_TYPES_BY_TIER                         # canon §3.2
SUCCESSOR_REQUIRES_LEADER_APPROVAL = True
PROVISIONAL_EXTRA_TYPE_ELIGIBILITY             # F10 fallback

GovernanceAction (enum)                       # Develop, Fortify, Pacify, Administer
ADMINISTER_OB = 2
PACIFY_OB_MIN = 1
PACIFY_FORMULA_BASELINE = 3
DEVELOP_FORTIFY_FORMULA_OFFSET = 1

develop_ob(prosperity) -> int
fortify_ob(defense) -> int
pacify_ob(order) -> int

GovernanceActionResult                         # extends ActionResult
execute_governance_action(action, stats, pool_roll) -> GovernanceActionResult

SubnationalFaction (enum)                     # 7 factions
NATURAL_SETTLEMENT_TYPES                       # {faction: tuple-of-types}
SubnationalManagementEffect                    # canonical effect dataclass
MANAGEMENT_EFFECTS                             # {faction: SubnationalManagementEffect}

RM_RESILIENCE_PRESENCE_THRESHOLD = 3
RM_RESILIENCE_OB_DELTA = 1
RM_NATURAL_PT_THRESHOLD = 2
NIFLHEL_DETECTION_EVIDENCE_THRESHOLD = 3
GRANT_MANAGEMENT_OB = 1
REVOKE_MANAGEMENT_ORDER_COST = 1
REVOKE_MANAGEMENT_DISPOSITION_COST = 2

revoke_management_ob(subnational_influence) -> int  # ceil(N/2)
rm_suppression_ob_modifier(rm_presence_count) -> int

GovernorState (dataclass) — UPGRADED FROM M4 STUB
can_assign_governor(standing, settlement, leader_approval) -> (bool, reason)
grant_subnational_management(gov, subnational, settlement) -> ActionResult
revoke_subnational_management(gov, stats, influence, roll) -> ActionResult

COMPANION_GOVERNOR_FREE_ACTIONS_PER_SEASON = 1
```

## Player-action loop — maintenance arm live; cumulative count 13

Module 5 brings the cumulative action-handler count to **13** (1 from M3 + 6 from M4 + 6 from M5):

| Module | Action | Effect | Arm |
|--------|--------|--------|------|
| M3 | `expand_institutional_capacity` | Treasury -300, +1 Wing | Improvement |
| M4 | 6 install_* actions | Church infrastructure axes | Improvement |
| M5 | `execute_governance_action(DEVELOP)` | Prosperity +1 | **Maintenance** |
| M5 | `execute_governance_action(FORTIFY)` | Defense +1 | **Maintenance** |
| M5 | `execute_governance_action(PACIFY)` | Order +1 | **Maintenance** |
| M5 | `execute_governance_action(ADMINISTER)` | Order no-decay + reveals Conviction | **Maintenance** |
| M5 | `grant_subnational_management` | Subnational governor takes settlement | Problem-solve |
| M5 | `revoke_subnational_management` | Revert subnational; Order -1 | Problem-solve |

### Closed loop now fully testable (provisional bindings)

Each governance action produces an `ActionResult` carrying `state_mutated`, `faction_standing_delta`, `renown_delta`. The closed loop:

```
Player at Counselor (Std 3) assigned Governor of S-005 Saatfeld (Village)
  → BLOCKED at can_assign_governor — F10 gap surfaces.
  → editorial decision OR sim-side fallback via PROVISIONAL_EXTRA_TYPE_ELIGIBILITY
  → assume sim-fallback used (Village → Counselor mapping)
  → governor assignment succeeds
  → each season: player chooses one governance action
    → Pacify at Order 2 (Ob 2; roll 4 succeeds)
    → Order → 3
    → ActionResult(success, +1 Order, faction_standing_delta=+1, renown_delta=+1)
    → faction_standing_delta consumed by Module 12 → faction Order shifts
    → renown_delta consumed by Module 8 → player UI shows renown gain
    → province_accord_from_settlements recomputes → province Accord updates
    → new actions become available at higher standing thresholds
```

The provisional `+1` standing/renown signals are placeholders. Module 12 (faction integration) will rebind them to canonical scalars derived from settlement type, governance action, and faction-stance state.

### Bishop-Governor + Province fracturing connection

§3.2 mentions: *"Bishop-Governor (PP-TBD): A special governor type installed via Church Ecclesiastical Appointment action. Settlement governance transfers to Church on appointment. Province fractionalizes if bishop-governor settlement's controller now differs from Seat holder."*

This wires directly to Module 2's `province_is_fractured` predicate. A Crown-province Seat with a Bishop-Governor settlement creates fracturing if Bishop ≠ Seat-holder. Module 13 Mode B chain test: install Bishop-Governor in Hafenmark province (Gransol is Seat) at S-020 Saltbrück → fracturing predicate fires → province fractures → political-value computation loses unification bonus.

## Ledger entries this session

26 new (100 total cumulative — 17 M1 + 11 M2 + 20 M3 + 26 M4 + 26 M5).

Coverage:
- 4 Standing tier minimums (0, 3, 4, 5)
- 4 governance-action Ob constants (Administer 2, Pacify min 1, Pacify baseline 3, Develop/Fortify offset 1)
- 3 Pacify worked-example values (Ob at Order 0 = 4, Order 3 = 1, Order 5 clamped to 1)
- 3 Develop / Fortify worked-example Ob values (1 at Pros 0, 3 at Pros 4, 2 at Fort 3)
- 4 subnational effect constants (Ministry decay -1, Löwenritter defense +1, Warden band shift 1, RM PT threshold 2)
- 3 RM cell-resilience constants (threshold 3, Ob delta 1, threshold-not-met 0)
- 1 Niflhel detection threshold (3)
- 1 Grant management Ob (1)
- 2 Revoke management costs (Order 1, Disposition 2)
- 2 Revoke management ceiling-division worked examples (Influence 5 → 3; Influence 4 → 2)
- 1 Companion-governor free-action allowance (1)
- 7 subnational-faction count (7)
- 4 governance action count (4)

## Next session — Module 6 (settlement events + thread ops)

Force-full read: settlement_layer_v30 §4.1, §4.2, §4.3 (Scene Slate Settlement Anchoring, Subnational Faction Visibility, Settlement Events). Module 6 brings the **problem-solve arm** more fully online (event resolution actions). The Templar interrupt action (from M4) lands here via the action-cancellation surface. Module 6 also surfaces Thread practitioner mechanics from §1.5 Axis 3 (Inquisitor surveillance Concealment test).

8 modules remaining before Module 13 integration runner.
