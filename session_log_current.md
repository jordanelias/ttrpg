session_id: 2026-04-19-engine-v3-rebuild-plus-canon-strikes
session_close: 2026-04-19
phase: 0
status: complete
last_stage: engine_v3.6 committed + workplan for v4 rebuild + VTM and Cultural Reformation struck from canon
next_action:
  skill: engine_v4 rebuild — Phase 0 canon audit
  description: >
    Start Phase 0 of the engine rebuild workplan at
    tests/sim_framework/workplan_rebuild_2026-04-19.md (commit 13b8f30).
    Phase 0 is a canon audit only — no engine changes. Full reads of:
    mass_battle_v30, settlement_layer_v30, faction_layer_v30, faction_politics_v30,
    factions_personal_v30, npc_behavior_v30, params/bg/* (all 15+ files),
    threadwork_v30, calamity_radiation_v30, southernmost_v30.
    Output: tests/sim_framework/canon_audit.md listing every system + source +
    gap flag. Six gaps already flagged in workplan as editorial blockers:
    mine income rate, food vulnerability mechanic, Crown Einhir suppression action,
    RM activation trigger, Thread ops in mass battle, subnational faction emergence.
    Phase 0 confirms whether these gaps are real or exist in canon sections
    not yet read. After audit, Phase 1 (substrate — territory graph + settlement
    sublayer + Calamity radiation state) starts. Do not touch engine_v3 until
    audit complete.
  blockers: []
commits:
  - 422fa07: Mass Seizure exponential declaration curve P=((CI-60)/40)^3.3 + supersession_check hook
  - 2e70d77: Engine v3.1 — 6 bug fixes + Warden emergence
  - 3f07396: Engine v3.2 — territory inheritance + LocalMilitia revolt + 0-territory elimination
  - f7aa0ed: Engine v3.3 — VTM struck from engine + RS seasonal decay
  - bc57b6c: Engine v3.4 — Church infrastructure buildup + heresy investigation + Hafenmark wealth
  - d225feb: Engine v3.5 — earlier Mass Seizure curve P=((CI-40)/60)^2.5 + elimination cascade
  - 297f892: Engine v3.6 — Cultural Reformation struck from engine + Varfell pure military
  - 13b8f30: Workplan for engine_v4 full rebuild from canonical game systems
  - 613ebf9: VTM + Cultural Reformation struck from canon — ED-706, ED-707
session_highlights:
  - Engine v3 went through 6 iterations. Final state at 297f892 has correct dice, CI, RS, territory inheritance, LocalMilitia revolt, exponential seizure curve. Still structurally wrong for rebuild (no geography, no settlements, no mass battles).
  - Supersession register infrastructure now live. canon/supersession_register.yaml + supersession_check hook in valoria_hooks.py fires during pre_commit_gate as non-blocking warning when commits touch flagged files. Verified live during commits 422fa07 and 613ebf9.
  - VTM struck — no canonical advancement mechanic existed, was placeholder. Varfell victory paths A/B/C + Cultural Reformation pool formula need rewrite (ED-706).
  - Cultural Reformation struck — Jordan clarified Vaynard is Reinhardt von Lohengramm parallel. Military conqueror, not ideological converter. Varfell expansion is purely military. Tribune intel remains, Thread operations remain as personal-scale actions. (ED-707)
  - Extensive faction identity canon review: Almud = best player at table playing defense on all fronts (weaponizes Einhir question, redirects threats into each other, wins late by absorbing wreckage). Baralta = iron personality + parliamentary prowess + mining wealth → best troops, food vulnerability. Vaynard = revolutionary southern Einhir, closest to Thread, hemmed in by fortresses. Himlensendt = true believer whose pastoral service drifts into theocracy. Caste system = binary (Einhir-heritage vs not), structurally load-bearing for NPC ecosystem.
  - Engine v3 is architecturally wrong. Has been building NPC-vs-NPC stat-comparison loop without player, scenes, zoom-in, actual mass battles, Thread operations, terrain, adjacency, settlement-level Church infrastructure, or geographic constraints. Correct dice/CI/RS mechanics but wrong faction model.
  - Workplan for engine_v4 full rebuild from game systems up, not from faction win-rate targets down. 6 phases, ~8 sessions.
open_items:
  - ED-706 VTM strike — Varfell victory paths A/B/C need rewrite (P2)
  - ED-707 Cultural Reformation strike — faction_actions, Varfell ladder, NPC priority trees need rewrite (P2)
  - Six canon gaps flagged in workplan blocking parts of v4 rebuild (mine income rate, food vulnerability, Einhir suppression action, RM activation trigger, Thread ops in mass battle, subnational faction emergence)
  - coverage_matrix at 4537/5000 tokens — warning threshold
  - editorial_ledger at 1652/2000 tokens — warning threshold (after ED-706 and ED-707 added)
  - ED-671 Thread-perception census (P1)
  - ED-666 Path B speed-run calibration (P1) — note: Path B itself pending rewrite after VTM strike
  - ED-667 Coup Counter readiness gap (P1)
  - ED-632 Shadow Renown mechanic (P1)
  - ED-633 Deniability Debt (P1)
  - ED-629 Heresy Proceedings auth loop (P1)
  - ED-663 Wealth cap (P1)
