session_close: 2026-03-27
checkpoint: 14-sim-prep
model: claude-sonnet-4-6
completed_stages:
  - Identified all mechanics directly impacted by editorial decisions committed 2026-03-26
  - Mapped 12 mechanic groups requiring re-simulation
  - Discovered P1 attribute pool inconsistency (§2.2 vs §14.1/§12)
  - Prepared full simulation routing table and handoff

p1_finding:
  issue: Attribute pool contradiction
  location_1: "§2.2 — 31 points distributed across 10 attributes"
  location_2: "§14.1 (Session Zero checklist) — 18 attribute points"
  location_3: "§3772 (GM checklist) — 18 attribute points"
  location_4: "§12 (hybrid) — 18 attribute points"
  action_required: Propagate 31 to all checklist references before next push

mechanics_flagged_for_simulation:
  - id: M-11/M-12/M-13/M-14/M-15
    change: TPS (=TS÷10 round down) added to all Thread operation pools
    test_modes: [A_isolation, B_interaction]
  - id: M-16/M-17/M-18
    change: Co-movement d10 replacing d6; History Resonance and Flashback removed from co-movement
    test_modes: [A_isolation, D_edge_cases]
  - id: M-26
    change: Coherence renamed Intelligibility (10->0); effects table revised; separate Coherence track retained
    test_modes: [A_isolation, B_interaction_with_Knots, D_edge_cases]
  - id: M-32
    change: Knot Call = +2 strain for +3D; closer bonds = higher strain capacity
    test_modes: [B_interaction, D_edge_cases]
  - id: M-03_Composure
    change: Rattled = wound-equivalent track (-1D per mark, cumulative); Composure resets after each Rattled
    test_modes: [A_isolation, D_edge_cases]
  - id: M-42
    change: Domain Ob = direct target stat (1-7, no division); pool adds faction stat if leadership held
    test_modes: [A_isolation, B_interaction, C_scenario]
  - id: M-36
    change: Renown 0-10 full permission table; Debate bonuses at tier 5/6/7/8
    test_modes: [A_isolation, B_interaction_with_Debate]
  - id: M-47_Vaynard
    change: Ambition Track (0-100, 5 thresholds); TK system redesigned; TS via originary lock collection
    test_modes: [A_isolation_full_range, C_scenario]
  - id: M-44_Niflhel
    change: Four-network Supremacy Mechanic at seasonal accounting
    test_modes: [A_isolation, C_endgame_scenario]
  - id: M-46_TC
    change: TC pause threshold changed from Stability <= 5 to Stability <= 4
    test_modes: [A_boundary, C_scenario]
  - id: M-43_seasonal
    change: S-16 through S-20 added (five new event triggers)
    test_modes: [C_scenario, D_interaction_with_existing_events]

commits: {}

editorial_still_pending:
  - S-08 Einhir site name (deferred)
  - Co-movement d10 table in BG (uses card system; d10 is TTRPG only)
  - E-01 assassination perpetrator (intentionally unresolved)
  - Vaynard Private Collection transfer procedure (design pending)
  - Niflhel Supremacy seasonal resolution full procedure (design pending)
  - Coherence 0 saving attempt procedure (design pending)

next_action:
  task: Run full simulation suite on all 12 mechanic groups above
  skill: valoria-simulator
  modes: [A_isolation, B_interaction, C_scenario, D_edge_cases]
  priority_order:
    1: TPS across all Thread ops (Mode A)
    2: Co-movement d10 (Mode A + D)
    3: Intelligibility x Knot strain interaction (Mode B)
    4: Rattled stacking (Mode A + D)
    5: Domain Ob + leadership pool (Mode B with faction stats)
    6: Renown x Debate (Mode B)
    7: Vaynard Ambition Track full range (Mode A)
    8: Niflhel Supremacy endgame (Mode A + C)
    9: TC pause at Stability <= 4 (Mode C)
    10: Seasonal events S-16-S-20 (Mode C)
  output_file: tests/valoria_stress_tests_batch3.md
  also_repair: Propagate attribute pool = 31 to §14.1 and §12 checklist references in CP14
  model: Sonnet 4.6

