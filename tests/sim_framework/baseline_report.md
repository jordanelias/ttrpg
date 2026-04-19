# Phase 4 Baseline Report — Framework Validation
# Date: 2026-04-18
# Status: FRAMEWORK OPERATIONAL — subsystem infill required

## Architecture (Phase 4.0)
Season loop implemented: Briefing → Duty → Scene Slate → Personal Phase → Faction AI → Accounting.
10 player policies defined. 50-run baseline (10 policies × 5 seeds) executes in <2 seconds.

## State Initialization (Phase 4.1)
- 4 active factions + 4 dormant initialized from canonical values
- 34 settlements across 15 territories with P/D/O stats
- 14 named NPCs with full stat blocks (TS, Certainty, Convictions, RS)
- PC with 7 attributes, Standing, Renown, Coherence
- Global clocks: RS 72, TC 28, IP 5, PI 7, Strain 0
- PT per territory from canonical starting values
- 18-card Co-Movement deck

## Baseline Results (50 runs, 120 seasons each)
- Feature coverage: 25/~130 features fired (19%). EXPECTED — simplified subsystems.
- TC trajectory: reaches 49 (target 75 by S47). Church Assert fires but drift not fully modeled.
- RS trajectory: stays at 72 (Thread ops only fire for practitioner policy). Infill needed.
- Standing: reaches 7 for all policies. Advancement model working.
- No victories (simplified territorial model doesn't produce conquests). Infill needed.

## Infill Required (Phase 4.2 continuation)
Each subsystem needs expansion to fire all ~130 features:
1. Combat: all 11 action types, wound intervals, Stamina, Fibonacci bonus
2. Fieldwork: 6 depths, 6 investigation actions, 7 social actions, Exposure
3. Contest: 4 interaction types, 3 adjudicator types, Composure, Concentration
4. Threadwork: 5 operations, Mending, collective ops, opposing ops
5. Mass battle: 7 phases, formations, tactics, General Duel
6. Domain Echo: 16 echo types, Sufficient Scope
7. NPC arcs: state machine transitions, death/replacement
8. Victory: all faction-specific conditions

## Gate Status
FRAMEWORK GATE: PASSED (architecture + initialization validated).
FEATURE GATE: NOT YET PASSED (25/130 features, 19%). Requires infill.
CALIBRATION GATE: NOT YET EVALUATED. Requires infill + re-baseline.
