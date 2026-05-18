---
session_id: "2026-05-17-v18-phase-9-faction-unique-actions"
session_close: "2026-05-18T01:00:00Z"
phase: simulation
status: complete
last_stage: phase_9_faction_unique_actions_committed
next_action:
  skill: valoria-simulator
  task: "Phase 7 Mass Battle port (per integration_plan §3 Phase 7, mass_battle_integration_v30.md 10-step plan). Phase 7 unblocked, READY per §1.4. Converts single-roll Conquest to multi-unit resolution and gives Excommunication state strategic teeth via canonical mass-battle penalties on excommunicated factions."
  files:
    - designs/provincial/mass_battle_integration_v30.md
    - designs/provincial/mass_battle_v30.md
    - tests/sim/v17-integration/m3_mass_battle.py
    - sim/provincial/massbattle.py
    - sim/provincial/units.py
blockers:
  - "Church win-share dropped 6.0% to 0.5% — Mass Seizure (CI>=60 Territorial Seizure per faction_canon §9 row 2) is Church's missing territory-gaining lever; depends on Pass 2f Church canon authoring which is BLOCKED on contamination audit"
  - "Phase 8 Strategic AI (GD-2 mandatory threat-response) deferred — current dispatch is stochastic 30% slot per M7_ASSUMPTION_SIX"
  - "7 PROVISIONAL flags in committed modules tracking v18 schema gaps (Circles, Reputation, public-office bar, Cohesion, Charters, Cardinal Focus, Crown-Church relations)"
commits:
  - "7ea85723: Phase 5/9 — wire Crown Initiative + Church faction-unique actions (5 modules + dispatch + Faction schema)"
decisions:
  - "Phase 5 in handoff (279e2e56) = Phase 9 in canonical integration_plan_v18.md §3; per §1.4 Provincial readiness table all four target modules marked READY"
  - "Excommunication: full §7.1 Tribunal procedure (Q1=B) — single-roll abstraction of multi-Exchange procedure; full Contest engine deferred to canonical Phase 5"
  - "Royal Progress Ob: POST-ED-840 closure formula max(2, floor((sum_max - sum_current) / 2)) — v17 M6 uses pre-closure broken formula"
  - "Church drop interpretation: committed honest data (option A) over dispatch-% tuning (option B); tuning invents game design without canonical basis per M7_ASSUMPTION_SIX"
v18_phase_9_summary:
  modules_implemented: 5
  modules_with_provisional_flags: 7
  ledger_entries: 33
  canonical_sources_cited: 7
  sim_gate_scope: "custom: core_engine, factions, social_debate"
  smoke_tests_passing: "T2 (excomm + tribunal), T3 (crown_initiative + absolution + council)"
  batch_n_200_base_seed_0:
    pre_phase_9_baseline:
      crown: 75.5
      varfell: 17.0
      church: 6.0
      hafenmark: 1.5
      battles_mean: 3.0
    post_phase_9:
      crown: 70.0
      varfell: 28.0
      church: 0.5
      hafenmark: 1.5
      battles_mean: 2.4
    delta:
      crown: -5.5
      varfell: +11.0
      church: -5.5
      hafenmark: 0
  drift_flags_surfaced:
    - "PI bootstrap script references g.print_status_block() not present in current github_ops.py"
    - "PI bootstrap script orders assert_bootstrap before read_files_graphql (corrected by quick_bootstrap)"
    - "Intervening session (Phase 1-2 commits 760f2d61..4e81887b plus handoff 279e2e56) did not run safe_session_close — directory-resident phase2_handoff.md substituted for log"
pass_3_findings_for_jordan:
  - "Church win-share regression is real strategic consequence, not bug — 30% faction-unique slot was previously no-op (returned 'invalid' -> fell through to Conquest); now state-mutating actions that cost L on Failure and never gain territory"
  - "Win-share diversification went to Varfell (no unique actions wired) — pure residual effect, not Varfell-mechanic strength"
  - "Seed variance ±2pp across base_seed=0 runs (74/22, 70/28, 69.5/29.5); committed numbers are one-slice, not confidence-interval validated"
  - "Crown Royal Progress dispatch rate low (~5% of Crown turns) — heuristic gate (Ob <= Pool+1) rejects RP at default Crown state (sum_accord ~30, Ob ~6, Pool 5); falls to Great Work when Wealth sufficient"
  - "Excommunication formal-grounds path (CI>=40 + Church.L>=4) rarely triggers — default CI=30, slow growth; need Phase 7+8 to make formal Excomm a viable Church strategy"
---
