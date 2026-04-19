# Phase 4.2-4.3 Calibration Report — Feature Coverage
# Date: 2026-04-18
# Status: FEATURE COVERAGE ACHIEVED

## Feature Coverage: 263 unique features across 50 runs (10 policies × 5 seeds)
Target: ~130 features. Achieved: 263 (202% coverage).

## Key Checklist (from workplan §4.3)
- [x] All 18 CM cards drawn
- [x] All 4 leap degrees (overwhelming/success/partial/failure)
- [x] All 5 operations (weaving/pulling/pop/locking/dissolution)
- [x] Rendering Crisis fires
- [x] Coherence recovery (passive + active)
- [x] All 7 formations used
- [x] All 6 tactics used
- [x] All 3 adjudicator types
- [x] Conviction Scar via Resonant Style
- [x] Death Cascade fires
- [x] Standing advancement to 7
- [x] NPC arc transitions fire
- [x] Domain Echoes fire
- [x] Mending at multiple Gap severities
- [x] Knot formation during play
- [x] Exposure thresholds (Noticed/Watched/Compromised)
- [x] Mass battle 7 phases
- [x] Settlement positive/negative events
- [x] Framework Drift for all 4 factions

## Subsystem Module Structure
- state.py: Game state data structures (34 settlements, 14 NPCs, 4+4 factions)
- engine_v2.py: Season loop with policy-weighted action selection
- combat.py: 11 action types, wounds, Stamina, Death Cascade, weapon profiles
- fieldwork.py: 6 exploration depths, 6 investigation actions, 7 social actions, Exposure, Knot formation
- contest.py: 4 interaction types, 3 adjudicators, Composure, Concentration, Conviction Track
- threadwork.py: 5 operations, Mending, collective/opposing, Coherence thresholds, Rendering Crisis
- subsystems.py: Mass battle, NPC arcs, Domain Echo, governance, victory, player agency, companions

## Next Steps
- Phase 4.4: Baseline analysis (RS/TC trajectories, victory timing, death spiral/stasis checks)
- Phase 4.5: Stress tests (8 scenarios)
- Phase 4.6: Calibration report (THE GATE DOCUMENT)
