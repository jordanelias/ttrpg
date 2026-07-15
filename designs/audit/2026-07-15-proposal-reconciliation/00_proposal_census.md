# 00 — Proposal Census (awaiting-ratification reconciliation, 2026-07-15)

## Status: REFERENCE (analysis-only; no canon flipped by this file)

The live inventory of design docs whose first `## Status:` line reads PROPOSED / PROVISIONAL /
DRAFT, as computed by `tools/dashboard_data.py::build_proposals` over `designs/**` (excl.
`deprecated/`, `archives/`) — **55 docs** — plus **9 dashboard-invisible proposals** under
`designs/proposals/` that carry no `## Status:` line (Nature D). Grouped by editorial lane and
classified into the four natures that drive handling (see `../2026-07-15-proposal-reconciliation/`).

**Depth** = line count (the offset signal for recency-vs-depth). **Cited EDs** = capstone/anchor found in the doc head.

| Nature | Count | Handling |
|---|---|---|
| A1 | 29 | Bulk-flip first `## Status:` → SUPERSEDED by ratified capstone (ED-IN-0011) |
| A2 | 10 | Reclassify to a truthful non-proposal status (READ-ONLY AUDIT / RATIFIED-as-record) |
| B | 13 | Cross-read → `01_reconciliation_map.md` + `governance_cluster_reconciliation_v1.md` (PROPOSED) |
| C | 3 | `03_natureC_dispositions.md` — ratify/hold/needs-edits, all needs_jordan |
| D | 9 | `designs/proposals/` un-statused — assessed vs canon; add status lines so the dashboard catches them |

## Lane IN  (51)

| Nature | Date | Depth | Doc | First `## Status:` (trunc) | Cited EDs |
|---|---|---|---|---|---|
| A1 | 2026-07-05 | 179L | `audit/2026-07-05-emergent-narrative-engine/00_grounding/00_engine_charter.md` | PROPOSED (design-effort charter — Jordan-vetoable) | ED-681,ED-IN-0003,ED-IN-0004 |
| A1 | 2026-07-05 | 76L | `audit/2026-07-05-emergent-narrative-engine/00_grounding/01_arc_corpus.md` | PROPOSED (design-effort grounding — Jordan-vetoable) | — |
| A1 | 2026-07-05 | 76L | `audit/2026-07-05-emergent-narrative-engine/00_grounding/02_prose_render_stack.md` | PROPOSED (design-effort grounding — Jordan-vetoable) | — |
| A1 | 2026-07-05 | 91L | `audit/2026-07-05-emergent-narrative-engine/00_grounding/03_prior_art_and_module_homes.md` | PROPOSED (design-effort grounding — Jordan-vetoable) | ED-1009,ED-412,ED-479,ED-609 |
| A1 | 2026-07-05 | 21L | `audit/2026-07-05-emergent-narrative-engine/01_workings/README.md` | PROPOSED working record (companion to ../narrative_engine_de | — |
| A1 | 2026-07-05 | 364L | `audit/2026-07-05-emergent-narrative-engine/01_workings/arch_A_minimal_detector.md` | PROPOSED (design-effort lane output, 2026-07-05) — Jordan-ve | ED-681,ED-IN-0003,ED-IN-0004 |
| A1 | 2026-07-05 | 294L | `audit/2026-07-05-emergent-narrative-engine/01_workings/arch_B_arc_vector_engine.md` | PROPOSED (design-effort working notes — Jordan-vetoable) | ED-IN-0003,ED-IN-0004 |
| A1 | 2026-07-05 | 363L | `audit/2026-07-05-emergent-narrative-engine/01_workings/arch_C_director_layer.md` | PROPOSED (design-effort architecture lane — Jordan-vetoable) | ED-761,ED-IN-0003 |
| A1 | 2026-07-05 | 210L | `audit/2026-07-05-emergent-narrative-engine/01_workings/critic.md` | PROPOSED (critic lane, 2026-07-05 · Lane IN) | ED-681,ED-IN-0003 |
| A1 | 2026-07-05 | 308L | `audit/2026-07-05-emergent-narrative-engine/01_workings/dossier_register_formalizability.md` | PROPOSED (design-effort working notes — Jordan-vetoable) | ED-416 |
| A1 | 2026-07-05 | 308L | `audit/2026-07-05-emergent-narrative-engine/01_workings/dossier_transport_fitness.md` | PROPOSED (lane working notes — Jordan-vetoable) | — |
| A1 | 2026-07-05 | 64L | `audit/2026-07-05-emergent-narrative-engine/01_workings/draft_s2_q3_arcs.md` | PROPOSED working notes (Jordan-vetoable) · Lane IN · 2026-07 | ED-936,ED-IN-0003 |
| A1 | 2026-07-05 | 86L | `audit/2026-07-05-emergent-narrative-engine/01_workings/draft_s3_q4_render.md` | working notes (render-lane drafter, 2026-07-05). Deliverable | ED-681 |
| A1 | 2026-07-05 | 157L | `audit/2026-07-05-emergent-narrative-engine/01_workings/judge_architecture_integrity.md` | PROPOSED (design-effort judgment — Jordan-vetoable) | ED-936,ED-IN-0003,ED-IN-0004 |
| A1 | 2026-07-05 | 217L | `audit/2026-07-05-emergent-narrative-engine/01_workings/judge_buildability.md` | PROPOSED (design-effort judge notes — Jordan-vetoable) | ED-416,ED-681,ED-781,ED-IN-0004 |
| A1 | 2026-07-05 | 134L | `audit/2026-07-05-emergent-narrative-engine/01_workings/judge_player_experience.md` | PROPOSED (design-effort judge working notes — Jordan-vetoabl | — |
| A1 | 2026-07-05 | 212L | `audit/2026-07-05-emergent-narrative-engine/01_workings/refute_determinism_replay.md` | PROPOSED (adversarial working notes — Jordan-vetoable) | — |
| A1 | 2026-07-05 | 129L | `audit/2026-07-05-emergent-narrative-engine/01_workings/refute_integration_reality.md` | PROPOSED (adversarial-skeptic lane, 2026-07-05) | ED-1051,ED-1094,ED-935 |
| A1 | 2026-07-05 | 143L | `audit/2026-07-05-emergent-narrative-engine/01_workings/refute_railroad_windows.md` | PROPOSED (adversarial-skeptic lane, 2026-07-05) | — |
| A1 | 2026-07-05 | 257L | `audit/2026-07-05-emergent-narrative-engine/01_workings/refute_v2_determinism_cost.md` | PROPOSED (adversarial working notes — Jordan-vetoable) | ED-1050 |
| A1 | 2026-07-05 | 190L | `audit/2026-07-05-emergent-narrative-engine/01_workings/refute_v2_light_function.md` | PROPOSED (adversarial-skeptic lane, LIGHT-FUNCTION lens · 20 | — |
| A1 | 2026-07-05 | 224L | `audit/2026-07-05-emergent-narrative-engine/01_workings/refute_v2_veto_railroad.md` | PROPOSED (adversarial-skeptic lane, 2026-07-05) | — |
| A1 | 2026-07-05 | 166L | `audit/2026-07-05-emergent-narrative-engine/01_workings/refute_veto_and_drift.md` | PROPOSED (adversarial-skeptic lane, 2026-07-05) | — |
| A1 | 2026-07-05 | 474L | `audit/2026-07-05-emergent-narrative-engine/01_workings/spec_sections/s1_q1_q2.md` | PROPOSED (spec-section draft, 2026-07-05 · Lane IN) | ED-681 |
| A1 | 2026-07-05 | 748L | `audit/2026-07-05-emergent-narrative-engine/01_workings/spec_sections/s2_q3_arcs.md` | PROPOSED (spec-section draft — Jordan-vetoable, ratified-on- | ED-1094 |
| A1 | 2026-07-05 | 774L | `audit/2026-07-05-emergent-narrative-engine/01_workings/spec_sections/s3_q4_render.md` | PROPOSED (spec-section draft, render lane, 2026-07-05) | ED-681,ED-IN-0004 |
| A1 | 2026-07-05 | 633L | `audit/2026-07-05-emergent-narrative-engine/01_workings/spec_sections/s4_substrate.md` | PROPOSED (spec-section drafter lane, 2026-07-05 · Lane IN) | ED-IN-0003 |
| A1 | 2026-07-05 | 808L | `audit/2026-07-05-emergent-narrative-engine/01_workings/spec_sections/s5_season_trace.md` | PROPOSED (spec-section draft, emergent-narrative-engine effo | — |
| A1 | 2026-07-05 | 315L | `audit/2026-07-05-emergent-narrative-engine/01_workings/synthesis.md` | PROPOSED (synthesis-architect lane output, 2026-07-05) | ED-IN-0003,ED-IN-0004 |
| A2 | 2026-07-07 | 109L | `audit/2026-07-07-unaddressed-areas-audit/00_grounding/00_charter.md` | PROPOSED (Jordan-vetoable throughout; the audit half of this | ED-1042,ED-IN-0017 |
| A2 | 2026-07-08 | 312L | `audit/2026-07-08-attribute-value-coherence-audit/attribute_value_coherence_v1.md` | PROPOSED (read-only audit, 2026-07-08) · Lane: IN · Anchor:  | ED-1021,ED-1094,ED-899,ED-IN-0008 |
| A2 | 2026-07-08 | 140L | `audit/2026-07-08-attribute-value-coherence-audit/finding_status.md` | PROPOSED (read-only audit, 2026-07-08) · Lane: IN · Anchor:  | ED-1085,ED-644,ED-830,ED-920 |
| A2 | 2026-07-08 | 135L | `audit/2026-07-08-crunch-cascade-pessimist-ners-contamination/01_pessimist_subtractive_ners/00_corpus_synthesis.md` | PROPOSED (read-only synthesis, 2026-07-08) · Lane: IN · aggr | ED-MB-0004,ED-PC-0007 |
| A2 | 2026-07-08 | 130L | `audit/2026-07-08-pessimist-action-audit/00_grounding/00_charter.md` | RATIFIED 2026-07-08 (Jordan: 'Please ratify all'; ED-IN-0027 | ED-IN-0027,ED-PC-0007 |
| A2 | 2026-07-08 | 84L | `audit/2026-07-08-pessimist-action-audit/ed_options.md` | RATIFIED 2026-07-08 (Jordan: 'Please ratify all'; ED-IN-0027 | ED-1061,ED-IN-0027,ED-PC-0007 |
| A2 | 2026-07-08 | 47L | `audit/2026-07-08-pessimist-action-audit/finding_status.md` | RATIFIED 2026-07-08 (Jordan: 'Please ratify all'; ED-IN-0027 | ED-1061,ED-921,ED-IN-0016,ED-IN-0027 |
| A2 | 2026-07-08 | 80L | `audit/2026-07-08-pessimist-action-audit/pessimist_action_audit_v1.md` | RATIFIED 2026-07-08 (Jordan: 'Please ratify all'; ED-IN-0027 | ED-1061,ED-IN-0027,ED-PC-0007 |
| A2 | 2026-07-08 | 38L | `audit/2026-07-08-pessimist-action-audit/workplan_v6_register_deltas.md` | RATIFIED 2026-07-08 (Jordan: 'Please ratify all'; ED-IN-0027 | ED-921,ED-IN-0016,ED-IN-0027,ED-PC-0007 |
| A2 | 2026-07-12 | 554L | `audit/2026-07-12-pr119-harness-verification/narrative_ners_review.md` | PROPOSED, read-only. NOT canon. Does not ratify anything. | — |
| B | 2026-07-11 | 559L | `architecture/governance_ripple_substrate_v1.md` | PROPOSED (2026-07-11) · Lane: IN (cross-cutting) · Author-pa | — |
| B | 2026-07-11 | 335L | `audit/2026-07-11-grounded-event-card-deck/grounded_event_card_deck_v1.md` | PROPOSED (2026-07-11) · Lane: IN (cross-cutting; SE, FA) · A | — |
| B | 2026-07-12 | 64L | `audit/2026-07-12-governance-compendium/00_index.md` | PROPOSED — 2026-07-12 · Lane: IN (cross-cutting; SE, FA, GO) | — |
| B | 2026-07-12 | 254L | `audit/2026-07-12-governance-compendium/42_action_verb_catalogue.md` | PROPOSED — compiled 2026-07-12, Lane: IN (cross-cutting; tou | — |
| B | 2026-07-12 | 120L | `audit/2026-07-12-governance-compendium/43_directive_types.md` | PROPOSED (research-derived; not yet ratified into `faction_p | — |
| B | 2026-07-12 | 273L | `audit/2026-07-12-governance-compendium/44_standing_institutions.md` | PROPOSED (research-derived; not yet ratified into `faction_p | ED-1094 |
| B | 2026-07-12 | 151L | `audit/2026-07-12-governance-compendium/45_hidden_longfuse_stats.md` | PROPOSED — needs a granularity ruling | — |
| B | 2026-07-12 | 285L | `audit/2026-07-12-governance-compendium/event_cards/00_integration_map.md` | PROPOSED — compendium integration pass, not yet Jordan-ratif | — |
| B | 2026-07-12 | 82L | `audit/2026-07-12-governance-compendium/reeval/reeval_jp_se.md` | PROPOSED / provisional re-evaluation artifact — 2026-07-12.  | ED-SE-0020 |
| B | 2026-07-13 | 298L | `architecture/governance_type_registry_v1.md` | PROPOSED / REFERENCE — 2026-07-13 · Lane: IN (cross-cutting  | — |
| B | 2026-07-14 | 296L | `audit/2026-07-14-gameplay-subsystem-observatory/remediation_plan_v1.md` | PROPOSED — 2026-07-14 · Lane: IN (program umbrella; executio | ED-1083,ED-1094,ED-IN-0031,ED-IN-0064 |
| B | 2026-07-14 | 191L | `audit/2026-07-14-holistic-unification/unification_v1.md` | PROPOSED (audit synthesis; ED-IN-0065, 2026-07-14) | ED-1094,ED-IN-0063,ED-IN-0065 |

## Lane SE  (1)

| Nature | Date | Depth | Doc | First `## Status:` (trunc) | Cited EDs |
|---|---|---|---|---|---|
| B | 2026-07-14 | 227L | `territory/lps_wiring_v1.md` | PROPOSED (buildable spec) — 2026-07-14 · Lane: SE · executes | ED-1050,ED-FA-0004,ED-SE-0007 |

## Lane FA  (1)

| Nature | Date | Depth | Doc | First `## Status:` (trunc) | Cited EDs |
|---|---|---|---|---|---|
| C | 2026-05-04 | 205L | `provincial/franchise_v30.md` | DRAFT — awaiting Jordan review | — |

## Lane PC  (1)

| Nature | Date | Depth | Doc | First `## Status:` (trunc) | Cited EDs |
|---|---|---|---|---|---|
| C | 2026-05-07 | 439L | `npcs/character_canon_v30.md` | PROVISIONAL — pending ratification. | — |

## Lane WR  (1)

| Nature | Date | Depth | Doc | First `## Status:` (trunc) | Cited EDs |
|---|---|---|---|---|---|
| C | ????-??-?? | 584L | `world/solmund_master_document.md` | DRAFT — all content PROVISIONAL pending Jordan editorial app | — |

## Nature D — dashboard-invisible proposals in `designs/proposals/` (9)

Not among the 55: these carry status as **bold inline** (`**Status:**`) not a `## Status:` heading, so the
scan skips them. Assessed against current canon and given reconciled `## Status:` headings this pass. Full
detail + evidence: `04_natureD_designs_proposals.md`.

| Lane | Depth | Doc | Disposition |
|---|---|---|---|
| FA | 200L | `proposals/2026-05-16-PC-4.4-unified-success-stress.md` | LIVE / UN-ADOPTED → held |
| FA/IN | 226L | `proposals/2026-05-16-faction-audit-followup-plan.md` | STALE / OBSOLETE → superseded |
| FA/SE | 1288L | `proposals/2026-05-25-mechanics-integration-v3_1.md` | LIVE / UN-ADOPTED (31 items) → held (scoping) |
| MB | 284L | `proposals/mass_battle_fighting_withdrawal_v1.md` | PARTIAL (yield built, ED-MB-0005) → residual held |
| MB | 79L | `proposals/mass_battle_shape_echelon_revamp.md` | ABSORBED (ED-909/1088) |
| MB | 87L | `proposals/multiunit_envelopment_plan.md` | LIVE / UN-ADOPTED (Path-B) → held |
| MB | 285L | `proposals/pc_formation_system.md` | PARTIAL (engine built) → §8/§9 held |
| IN | 380L | `proposals/stub_infill_plan.md` | ABSORBED (Pass-2l complete) |
| PC | 94L | `proposals/weapon_physics_and_concentration_model.md` | PARTIAL (§§1–6 built, ED-PC-0010) → §7 held |

**Systemic finding:** the register's heading-anchored scan misses bold-inline status. Recommend widening
`build_proposals()` or a CI nudge (see `04_natureD_…` and `01_reconciliation_map.md §Held-back`).
