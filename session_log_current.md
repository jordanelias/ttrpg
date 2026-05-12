session_id: 2026-05-11-mb-redesign-phase2
session_close: 2026-05-11
phase: simulation
status: complete
last_stage: phase-2-shape-mechanics-validated-via-SIM-MB-05ABC-with-branch-exploration
next_action:
  skill: mass-battle-redesign-phase-3-battle-resolution
  description: >
    Phase 3 per references/mass_battle_redesign_workplan_v1.md §6.
    Write ED-811 (engagement formula degree-gated symmetric), ED-818 (combined attack
    single-column concentration), ED-820 (shape locking + emergency reshape Command Ob 3).
    Pre-work: resolve ED-822 secondary measure (composition balance), ED-823 (Fibonacci
    recalibration) via SIM-MB-06 if Jordan prioritises before Phase 6 propagation.
blockers: []
commits_this_session:
  - fe47325 [editorial] mass battle redesign workplan v1.1 ratified
  - b1ffec0 [editorial] Phase 1 — ED-815 + ED-812 closure
  - 239c56b [session] session close
  - 15d5475 [simulation] SIM-MB-05 Phase 2 shape mechanics initial validation
  - cb95385 [editorial] Phase 2 closed — ED-816/817/821 ratified, ED-822/823 raised; ledger archived
open_items:
  - ED-811 engagement formula degree-gated symmetric — Phase 3 implementation
  - ED-813 withdrawal Phase 1 declaration — Phase 4 implementation
  - ED-814 compositional grid + shape templates — Phase 4 implementation
  - ED-818 combined attack single column concentration — Phase 3 implementation
  - ED-819 unit parameters standing orders — Phase 4 implementation
  - ED-820 shape locking + emergency reshape — Phase 3 implementation
  - ED-822 Volley TN6→7 + secondary composition balance measure — needs Jordan ratification
  - ED-823 combined attack Fibonacci recalibration — needs SIM-MB-06 test harness
  - Propagation pending ED-800..820 to canonical docs (Phase 5-6)
  - VALORIA_PAT rotation outstanding
sim_artifacts:
  - tests/sim/sim_mass_battle_SIM-MB-05.md (full report with appendix)
  - tests/sim/sim_mass_battle_SIM-MB-05.py (sim engine)
  - tests/sim/sim_mass_battle_SIM-MB-05c.py (branch exploration)
empirical_findings:
  - Lethality 3.95t mean, 0/600 one-turn kills (target 3-6 ✓)
  - 5×5 shape matrix produces rock-paper-scissors strategic depth
  - Horseshoe H-2 positional trigger: 54% mean winrate vs all opponents
  - Volley TN6→7: partial composition rebalance (+8pp pure-melee competitiveness)
  - Direct-to-Line drift selected over tiered (simplicity vs 5-15pp historical fidelity)
