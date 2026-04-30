session_id: 2026-04-29-mass-battle-ners
session_close: 2026-04-29
phase: "2 — ongoing"
status: audit complete, patch proposals committed, terminology workplan committed
last_stage: >
  mass battle NERS stress test (batches 1+2) + historical review + patch proposals,
  systems overview compiled, connections artifact v1 produced,
  terminology conversion workplan drafted and committed (PP-675/ED-759 provisional)
next_action:
  skill: editorial
  description: >
    NEXT-SESSION PRIORITY (set by Jordan 2026-04-29):
    Re-do the connections artifact at designs/audit/2026-04-29-connections-artifact/
    with rigorous relationship audit. v1 (committed this session, /mnt/user-data/outputs/valoria_connections.jsx)
    was a first sketch — relationships were assigned by quick inspection of canonical_sources.yaml
    and the architecture skeletons, not by reading every system spec end-to-end.
    Required v2 work:
    (1) Read every system doc listed in canonical_sources.yaml at least to skeleton depth;
        for high-traffic hubs (faction_layer, scale_transitions, conflict_arch) read in full
    (2) For every node pair, decide: edge or no edge; if edge, then type (foundational/cascade/
        bidirectional/containment/gating), strength (1-4 rubric in node), state (canonical/
        provisional/gap), and label
    (3) Audit the v1 edges against the audit and remove/correct any that don't survive
    (4) Add edges that v1 missed (likely candidates: military_layer→faction_layer details,
        ms_trajectory↔threadwork specifics, throughlines→every Class A/B touchpoint,
        any second-order intersections through Self-Rendering/Leap)
    (5) Encode relationship quality not just by color but also by proximity/clustering
        and dash-pattern variation
    (6) Output: revised valoria_connections.jsx with audit log of edge decisions inline
        in a hidden EDGE_AUDIT comment block

    JORDAN DECISIONS REQUIRED (still pending from prior session):
    Mass battle (mass_battle_patch_proposals_2026-04-29.md):
    (1) DECISION-MB-01 through DECISION-MB-08 — 8 design decisions, recommended answers given
    Terminology conversion (designs/audit/2026-04-29-terminology-conversion/00_workplan.md §4):
    (2) 4.1 Strategic Mode vs Map Mode for BG (recommend: Strategic Mode)
    (3) 4.2 Scene Mode vs Encounter Mode for TTRPG (recommend: Scene Mode)
    (4) 4.3 Confirm Hybrid mode retired (3-mode → 2-mode + Zoom-In) — load-bearing
    (5) 4.4 Adjudicator → Resolver, or keep (recommend: keep)
    (6) 4.5 "session" policy (recommend: retire TTRPG-evening sense; allow hooks/UI senses)
    Standing decisions (still pending from prior sessions):
    (7) Intelligence stat restoration — see designs/audit/faction_stats_renaissance_review.md
    (8) LICENSE decision (GOV-08)
    (9) 1.1 Knot Formation During Play
    (10) 1.2 Accord Propagation
blockers:
  - "Connections artifact v2 audit pass (next session priority)"
  - "5 terminology workplan decisions (Jordan)"
  - "8 mass battle design decisions (Jordan)"
  - "8 auto-approvable mass battle patches awaiting approval (Jordan)"
  - "Intelligence stat decision (Jordan)"
  - "LICENSE decision (Jordan)"
notes:
  - "Stress test committed: designs/audit/mass_battle_stress_test_2026-04-29.md (13c11a9)"
  - "Patch proposals committed: designs/audit/mass_battle_patch_proposals_2026-04-29.md (1d9f864)"
  - "Terminology workplan committed: designs/audit/2026-04-29-terminology-conversion/00_workplan.md (PP-675, ED-759)"
  - "Connections artifact v1 produced (not yet committed to repo — lives at /mnt/user-data/outputs/valoria_connections.jsx)"
  - "v1 has 31 nodes, 53 edges — relationship judgments need full re-audit per next-session directive"
  - "2 math failures still open: MATH-FAIL-01 (siege calibration impossible), MATH-FAIL-02 (H fixed contradiction)"
  - "27 provisionals still requiring resolution before Godot implementation"
  - "canonical_sources.yaml at 4670/5000 tokens — approaching threshold; pruning needed before terminology_canon entry added"
