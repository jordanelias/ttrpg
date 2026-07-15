# 02 — Nature-A status flips (executed 2026-07-15)

## Status: REFERENCE (log of executed status-line changes; anchors ED-IN-0068)

Nature A = docs the awaiting-ratification scan flagged that are **not open design proposals** — they are
either (A1) working record of a design effort whose head is already ratified, or (A2) read-only
audit/review/charter artifacts mis-tagged as pending proposals. Per the approved plan, these are flipped
to a truthful status so the dashboard stops surfacing them as decisions Jordan still owes. **No design
content changed; only `## Status:` lines.** All flips verified against the working tree before writing.

## A1 — working record of the ratified emergent-narrative-engine effort (29 docs)

**Ratified head (verified):** `designs/audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md`
`## Status: RATIFIED (Jordan, 2026-07-05, PR #78; ED-IN-0011)`, with the normative spec being
`narrative_engine_design_v1.md`-as-amended + `spec/churn_amendments.md` (also RATIFIED). The 29 docs under
`00_grounding/` and `01_workings/` (grounding, charter, arch lanes, critic, judges, refutes, drafts,
spec-section drafts, synthesis) are the **drafter/adversarial/judge lane outputs** that fed that head — not
independently ratifiable.

**Flip applied (uniform):**
`## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as
../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md,
ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15,
proposal-reconciliation pass, ED-IN-0068]`

All 29 first-`## Status:` lines were previously `PROPOSED …` (design-effort grounding / working notes /
adversarial-skeptic / judge / spec-section draft / synthesis). Full list: `00_grounding/{00_engine_charter,
01_arc_corpus,02_prose_render_stack,03_prior_art_and_module_homes}.md`; `01_workings/{README,
arch_A_minimal_detector,arch_B_arc_vector_engine,arch_C_director_layer,critic,dossier_register_formalizability,
dossier_transport_fitness,draft_s2_q3_arcs,draft_s3_q4_render,judge_architecture_integrity,judge_buildability,
judge_player_experience,refute_determinism_replay,refute_integration_reality,refute_railroad_windows,
refute_v2_determinism_cost,refute_v2_light_function,refute_v2_veto_railroad,refute_veto_and_drift,synthesis}.md`;
`01_workings/spec_sections/{s1_q1_q2,s2_q3_arcs,s3_q4_render,s4_substrate,s5_season_trace}.md`.

## A2 — read-only audit/review/charter artifacts mis-tagged PROPOSED (10 docs)

These were never ratifiable *design proposals*; each is an audit output. Reclassified to a status that
reflects what it actually is (no PROPOSED/PROVISIONAL/DRAFT token → clears the scan).

| Doc | Was | Now | Verified anchor |
|---|---|---|---|
| `2026-07-08-pessimist-action-audit/ed_options.md` | `RATIFIED … Originally PROPOSED (2026-07-08) …` | same, `Originally filed 2026-07-08` | ED-IN-0027 **ratified** (ledger) — only the stray "Originally PROPOSED" phrase tripped the scan |
| `…/finding_status.md` | ″ | ″ | ED-IN-0027 ratified |
| `…/workplan_v6_register_deltas.md` | ″ | ″ | ED-IN-0027 ratified |
| `…/00_grounding/00_charter.md` | ″ | `Originally a read-only audit, 2026-07-08` | ED-IN-0027 ratified |
| `…/pessimist_action_audit_v1.md` | ″ | ″ | ED-IN-0027 ratified |
| `2026-07-08-attribute-value-coherence-audit/attribute_value_coherence_v1.md` | `PROPOSED (read-only audit) · Anchor ED-IN-0029` | `READ-ONLY AUDIT … Anchor: ED-IN-0029 (findings tracked; not a ratifiable design doc)` | ED-IN-0029 mostly resolved (1 open sub-item, tracked) |
| `…/finding_status.md` | ″ | ″ | ″ |
| `2026-07-08-crunch-cascade-…/00_corpus_synthesis.md` | `PROPOSED (read-only synthesis)` | `READ-ONLY SYNTHESIS …` | read-only; aggregates 9 lane critic-passes |
| `2026-07-07-unaddressed-areas-audit/00_grounding/00_charter.md` | `PROPOSED (Jordan-vetoable; edits no canon)` | `AUDIT CHARTER (Anchor ED-IN-0017); scaffolding; edits no canon` | ED-IN-0017 audit scaffolding |
| `2026-07-12-pr119-harness-verification/narrative_ners_review.md` | `PROPOSED, read-only. NOT canon.` | `READ-ONLY REVIEW — NOT canon; does not ratify anything` | self-declared non-ratifying |

## Result

Dashboard awaiting-ratification count: **55 → 16** (the 13 Nature-B + 3 Nature-C docs, all genuinely
held for Jordan). Verified by re-running the `build_proposals()` scan. No Nature-A doc was dropped that
wasn't deliberately reclassified; no design content touched.
