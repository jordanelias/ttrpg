# Scene-combat closing-distance/facing/grip redesign — design & audit trail (2026-07-02)

**Start here if you're picking up R2 implementation (or auditing how R1 was designed).**

## The one file you actually need to implement R2

**`plan_r1_RATIFIED.md`** — the final, Jordan-approved plan. Self-contained: context, 10 revised design
decisions (D0–D12), the re-staged I0→I8 increment sequence with falsifiable acceptance criteria, a complete
orphan cross-check table, and 9 explicit Jordan-decisions (JD-1…JD-9) each with its evidence and default.
This is a byte-exact copy of the canonical plan-mode file
(`C:\Users\Jordan\.claude\plans\things-like-a-feather-compressed-rivest.md`), copied here because that path
lives outside this repo and outside any git worktree — a new session in a different directory or branch has
no way to find it otherwise. **If the two ever diverge, the plan-mode path is upstream/canonical; this copy
should be re-synced from it, not edited independently.**

Also see `HANDOFF.md`'s 2026-07-02 Decisions entry and "START HERE" Next-actions bullet — this branch is
`scene-combat-morphology-rearch` in the isolated worktree `C:/Github/ttrpg-morph-rearch` (**not** the default
`C:/Github/ttrpg` checkout, which is on a different branch and does not have any of this work).

## Everything else here is provenance, not a dependency

The plan file is self-contained; nothing below is required to execute I0→I8. It's kept for anyone who wants
to audit *how* the plan reached its conclusions, or re-derive a Jordan-decision from first principles instead
of trusting the plan's summary of it.

### R0 — HEMA/biomechanics research (grounds the whole redesign)
- `r0_combined_brief.md` — the organized, cited synthesis (measure/closing footwork, facing/stance,
  commitment-depth/range-utilization, grappling), cross-checked for contradictions across clusters.
- `r0_flags.json` — 5 labeled contradiction/grounding flags (C1–C5) the plan respects throughout (e.g. C1:
  polearm facing direction is unresolved in the sources, C4: force-vs-distance is non-monotonic).
- `r0_research_*.json` — the 4 raw research-cluster outputs `combined_brief.md` synthesizes.
- `r0_workflow_script.js` — the Workflow script that ran R0 (4 sonnet research clusters + opus synthesis).
- `r0_ideal_state_audit_prep_notes.md` — prep notes mapping which Phase-B derivations were static/ideal-only
  vs already grip-aware, plus Jordan's architecture-placement and rearward-self-interference guidance.

### First audit generation — 6 independent lenses (replaced a Fable-tier audit that hung on the account's
weekly metering cap; see HANDOFF.md's process note)
- `audit1_lens_physics_kinematics.json`, `audit1_lens_primitive_schema.json`,
  `audit1_lens_geometry_bake_mode.json`, `audit1_lens_consumer_coupling.json`,
  `audit1_lens_architecture_orphan.json`, `audit1_lens_pipeline_trace.json` — the six lenses, each with
  BLOCKER/SERIOUS/MINOR findings against the pre-repair design.
- `audit1_antagonist_biomech_facticity.md`, `audit1_antagonist_morph_schema.md` — supplementary antagonist
  notes from the same generation.
- `audit1_consolidated_issue_register.md` — all six lenses deduplicated into one master register (7
  BLOCKER / 9 SERIOUS / 7 MINOR), with each of the original plan's design decisions (D1–D10) classified
  BROKEN / SALVAGEABLE / SOUND. This is what the agonist/antagonist repair loop below was driving against.

### Repair loop + capstone (not preserved individually — see the ratified plan + register instead)
A 4-round opus-max agonist/antagonist loop (22 agents) iteratively repaired the design against the register
above; its intermediate per-round drafts were process artifacts, not additional findings, and are **not**
copied here (they live only in session scratch and are safe to lose — the register + the two files below
already capture what changed and why). A follow-on 3-lens capstone verification pass then independently
re-derived and confirmed the outputs:
- `capstone_punchlist.md` — 4 more items found (1 new BLOCKER — a grip↔reach feedback oscillator, now JD-9
  — plus 1 SERIOUS plumbing gap and 2 MINOR wording fixes), each with a MUST-FIX / CONFIRMED-SOUND
  disposition and the exact required change.
- `capstone_verify_notes.md` — supporting verifier notes.

All 4 punch-list items are already folded into `plan_r1_RATIFIED.md` (verify: it contains `JD-9`).
