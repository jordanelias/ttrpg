session_id: 2026-04-19-throughlines-framework
session_close: 2026-04-19
phase: 0
status: complete
last_stage: PP-674 framework enforcement + tier N committed; framework now mandatory validation tool
next_action:
  skill: framework-use
  description: >
    Apply vetting framework to next design proposal. First real test candidates:
    Hafenmark/Löwenritter/RM institutional-attractor throughlines (closes ED-717
    M-4 gap). Workflow: task_gate('design_proposal') → classify per §8.1 →
    vetting chain per class → produce vetting: block → safe_commit invokes
    vetting_gate. Class C/D/E remain lightweight; Class A/B require full block.
  blockers:
    - Jordan decision: address ED-717 Hafenmark/Löwenritter/RM factions one-at-a-time or joint proposal
    - Jordan decision: retroactive canon audit timing (deferred until engine_v4 smoke-test data available)
commits:
  - 193d5ee: PP-664 VTM residual cleanup
  - d7c5f20: PP-665 Yrsa Vossen rename
  - c3de2ef: PP-666 three new systems (settlement adjacency, fractional ownership, succession split)
  - 2fd00f0: PP-667 gap sweep
  - b0dfcef: PP-668 OPEN ITEMS propagation
  - 53f7c5b: PP-669 skeleton freshness
  - 80294a3: PP-670 label audit + ED-716
  - 8498e97: PP-671 throughlines meta-synthesis + ED-717
  - 03da060: PP-672 throughlines hierarchical framework (canonical vetting guide) + ED-718
  - f2f3efe: PP-673 terminology cleanup (skeleton→index for auto-gen) + ED-719
  - 3fab28a: PP-674 framework enforcement + tier N (Necessity Test) + ED-720
session_highlights:
  - Canonical vetting framework adopted. Five tiers (N, Ω, Μ, М, Τ, Q, Μ̄) with scope classification (A-E), rating rubric (+/✓/−/○), 15-term Failure Lexicon. Skeleton/infill split for load efficiency.
  - Tier N (Necessity) added above Ω. Subject-grounding check against Renaissance-era political-leadership dynamics. Codifies user constraint that Valoria's complexity is earned only when modeling load-bearing historical dynamics, not added for its own sake.
  - Framework enforcement landed as vetting_gate() hook. Class A/B patch entries from PP-674 forward require vetting: block with class/necessity/omega/mu/m_ratings/q keys. Enforced at commit time and by CI. Grandfathering via pre-framework true.
  - Terminology collision resolved. "skeleton" now reserved for canonical rulesets in mechanical-spec-only style. Auto-generated heading/line/token companions renamed from *_skeleton.md to *_index.md. tools/skeleton_gen.py renamed to tools/doc_index_gen.py. 75 files renamed, 8 code/skill files migrated.
  - Meta-throughlines synthesis produced 6 structural patterns covering all 25 T-throughlines with primary/secondary tagging. М-3 and М-4 audit corrections applied (T-05 removed from М-3 conflation; T-18/T-19 split to М-2 geography from М-1 decay).
  - Hafenmark/Löwenritter/RM institutional-attractor gaps persist (ED-717). М-4 vetting of faction proposals involving them defaults to undefined baseline until own T-throughlines added.
  - PP-666 three systems validated against framework retroactively. Settlement adjacency, fractional province ownership, faction succession split all pass N (load-bearing Renaissance dynamics) and pass multiple М extensions.
open_items:
  - ED-717 (Hafenmark/Löwenritter/RM substrate-posture gaps) — persists; M-4 defaults to undefined baseline until resolved
  - Retroactive canon audit — deferred until engine_v4 smoke-test load-bearing data
  - Sparse throughline-interaction matrix — 7 of 25 throughlines have mapped cross-interactions; 18 unmodeled
  - Three sim_ttrpg_batch_legacy files with filename-only labels — low-priority, deferred (PP-670 note)
  - Skeleton-staleness no CI regeneration — skeletons (canonical rulesets) drift when canonical changes; no automated check currently
