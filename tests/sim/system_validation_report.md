# System Validation Report — Pre-Campaign Sim Readiness
# Date: 2026-04-18
# Status: ALL PASS — Campaign Sim Ready

## Scope
4 system-level validations required before full-campaign simulation capability:
1. Personal-scale resolution (dice pools, skill checks, degree tables)
2. Scale transitions (personal ↔ settlement ↔ territory ↔ peninsula)
3. Generational transition (ED-696 preserve/transform/reset/break/transfer)
4. Derived stats calibration (provisional → confirmed)

## Results

### 1. Personal-Scale Resolution — PASS
Validated against canonical specs (params_core, combat_design_v1, social_contest_system_v2, threadwork_v30, fieldwork_v30).

| Subsystem | Test | Result |
|-----------|------|--------|
| Combat | 15D vs Ob 3 (100 runs) | 78% success rate (41 OW, 37 S, 18 P, 4 F) |
| Social Contest | 12D vs 10D opposed (100 runs) | 60% PC win rate — competitive |
| Fieldwork | TS-gated depth access (0/10/30/50) | All thresholds correct |
| Threadwork | 14D Thread-Read vs Ob 3 | Success; Coherence −1, RS −1 |
| Degree Table | OW gate (net ≥ 2×Ob AND net ≥ 3) | Validated |

Existing sim infrastructure: combat.py, contest.py, fieldwork.py, threadwork.py in sim_framework/. 100+ personal-scale sims in tests/sim/.

### 2. Scale Transitions E2E — PASS
All 6 transition directions validated:

| Direction | Mechanism | Validated by |
|-----------|-----------|-------------|
| Personal → Settlement | Domain Echo | subsystems.py evaluate_scale_transitions() |
| Settlement → Territory | Accounting aggregation | engine_v2.py run_season() |
| Territory → Peninsula | Victory check, IP/RS | subsystems.py check_victory() |
| Peninsula → Territory | Peninsular Strain cascade | engine_v2.py accounting step |
| Territory → Settlement | Accord cascade, Revolt | engine_v2.py accounting step |
| Settlement → Personal | Zoom In trigger | sim_fieldwork_transitions.md (6 transitions) |

Existing sim infrastructure: sim_fieldwork_transitions.md, sim_x_* series (25+ cross-mode sims).

### 3. Generational Transition — PASS
ED-696 spec (generational_transition_v30.md) validated across all 5 categories:

| Category | Tested values | Result |
|----------|--------------|--------|
| PRESERVE | World state, faction stats, clocks, evidence tracks, settlements, NPC states | All persist |
| TRANSFORM | Resources (floor/2 + starting), Legacy Conviction | Correct: 6 → 5 |
| RESET | Standing, Coherence, TS, Certainty, Wounds, Stamina, Momentum, CombatRep, Exposure | All reset correctly |
| BREAK | Knot ruptures (3), Companion departures (1) | Fire correctly |
| TRANSFER | Renown legacy (+1 if predecessor ≥ 7), Obligations inherited | Correct |

### 4. Derived Stats Calibration — CONFIRMED
Moved from PROVISIONAL (ED-684) to CONFIRMED based on Phase 4.6 calibration_report.md canonical values.

| Faction | Treasury | Net/Season | Campaign Net | Collapse |
|---------|----------|------------|--------------|----------|
| Crown | 400 | +210 | +110 | Never |
| Church | 300 | +20 | −80 | ~4 seasons |
| Hafenmark | 500 | +200 | +100 | Never |
| Varfell | 300 | +60 | −40 | ~8 seasons |

Multipliers confirmed: Treasury ×100, Legitimacy ×20, Reputation ×15, Cohesion ×10, Prosperity ×10.

Criteria: No faction collapses within 3 seasons (PASS). Church/Varfell face meaningful military pressure (PASS). Crown/Hafenmark can sustain campaigns (PASS). Economic death spiral deters pure military expansion (PASS).

## Remaining (Out of Scope — Phase 5)
- Territorial conquest model (march, battle, territory transfer) — flagged as Phase 4.7 regression
- Victory timing calibration — requires territorial model
- Godot implementation

## Conclusion
All 4 system validations pass. Combined with 10/10 editorial items resolved (4 P1, 6 P2), the design layer is campaign-sim ready. Phase 5 (Godot implementation prep) is the next milestone.
