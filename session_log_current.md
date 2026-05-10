session_id: 2026-05-09-restoration-verified-solmund-hook-installed
session_close: 2026-05-09
phase: infrastructure
status: complete
last_stage: forbidden_token_gate-deployed
next_action:
  task: paste architecture-spec enforcement_spectrum table update from 2026-05-09 chat reflecting Solmund-Galbados Level 4 promotion via forbidden_token_gate plus task_gate skill-fetch and sim_gate manifest at Level 4
  skill: none
blockers: none
commits:
  - bc3a95a: infrastructure task_gate skill-fetch enforcement + sim_gate manifest check
  - c4bafb3: simulation ners_stress_01 module manifest Mode G step 1 (parallel session)
  - 816dd24: simulation ners_stress_01 Module 1 randomization layer (parallel session)
  - 887cb46: simulation ners_stress_01 Module 2 NERS batch 300 runs no P1 or P2 findings (parallel session)
  - da1a7bb: REGRESSION simulation NERS stress_01 Module 1 — bootstrapped on stale session log, overwrote 816dd24 + cleared 887cb46 coverage entries
  - fbe6fb5: fix restore 887cb46 NERS state — reverted da1a7bb regression on 4 files
  - 80fd04c: infrastructure session close — race-condition recovery
  - 56acefc: skill valoria_hooks forbidden_token_gate — Solmund-Galbados Level 4 enforcement
key_developments:
  - PARALLEL SESSION VERIFIED — 887cb46 Module 1 + Module 2 reproduce; ran Module 2 locally with PYTHONPATH=tests/sim and cwd=tests/sim/ners_stress_01, output byte-identical to committed ners_report.md (Crown 62, Varfell 35, Church 19, Hafenmark 17 wins; 16 to 24 percent Crown win rate monotonic across mild-moderate-extreme perturbation). Restoration via fbe6fb5 was the correct call.
  - PROVISIONAL AUTHORING DRIFT in 816dd24/887cb46 modules — Faction stat references include "legitimacy" and "popular_support" but the harness Faction class at tests/sim/valoria_full_campaign_sim.py L108 uses "mandate" (single field, pre-PP-686 v2 split). The modules use hasattr-guards and getattr-with-default so they degrade silently — only influence/wealth/military/stability are actually perturbed, NOT the L+PS dimension that the post-2026-05-02 ED-784 Faction model splits out. The smoke tests pass because they only validate bounds for attributes that exist. Either harness refactor to split Faction.mandate into legitimacy and popular_support fields, or update the modules to use mandate. Tracked as P1 follow-up for Module 2 sim correctness.
  - FORBIDDEN-TOKEN HOOK DEPLOYED — valoria_hooks.forbidden_token_gate now fires inside pre_commit_gate. Rule per file:  (a) no Galbados present, OR (b) Solmund also present (canonical-contrast convention reflecting actual repo usage in name_collision_database.yaml and similar), OR (c) every Galbados occurrence has "never" within plus-or-minus 30 char immediate context. Exempted prefixes archives/, deprecated/, references/atoms_pending/. Exempted paths skills/prose-writer/scripts/consistency_check.py and skills/valoria-orchestrator/scripts/valoria_hooks.py. All 6 active-canonical files containing Galbados pass under the rule. Promotes Solmund-Galbados from Level 2 (skill-side, prose-writer only) to Level 4 (every commit, RuntimeError).
  - ARCHITECTURE-SPEC TABLE UPDATE STILL OUTSTANDING — Stage A1 paste-ready text is in 2026-05-09 chat history, project knowledge can only be edited from claude.ai UI. Reflects forbidden_token_gate + task_gate skill-fetch + sim_gate manifest check at Level 4.
  - HOOK ARCHITECTURE DEFECT (still open) — read_active_sessions returned empty across every bootstrap in this session despite the parallel session being active. Concurrent same-files writes were not detected at commit time. Recommend path-locking or HEAD-OID stale-read check before commit.
  - MANIFEST NAMING DRIFT — module_manifest.md sim_gate systems clock_system and territory_model are not registered in canonical_sources.yaml; correct keys are clocks and territories. designs/world/geography_v30.md is not registered as canonical for any system though it is the actual data source per the manifest. Non-blocking cleanup.
  - PAT EXPOSURE — VALORIA_PAT was printed in diagnostic output during this session. Recommend rotation per identity rules.
open_items:
  - Paste architecture-spec enforcement_spectrum table update from 2026-05-09 chat into project knowledge
  - L+PS-vs-Mandate authoring drift in 816dd24 modules — 4 of 6 stats actually perturbed, fix before any further NERS production runs
  - Investigate hook concurrent-session detection — read_active_sessions returned empty during a real concurrent session
  - canonical_sources.yaml cleanup — register geography_v30.md or rename manifest sim_gate systems to clocks and territories
  - Rotate VALORIA_PAT
  - Add CI job invoking forbidden_token_gate-equivalent check (Level 5 mirror of new Level 4 hook)
  - Design-input items pending Jordan — ED-777, ED-780, ED-788, ED-776, ED-781, ED-710, ED-711
