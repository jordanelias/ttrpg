# Mode D — Gap Detection: Faction / Political

Per the skill's Output Rules: P1 gaps get filed as `ED-<LANE>-NNNN` (lane=FA here, per
`references/id_reservations.yaml`'s allocation protocol) — this audit does **not** allocate the
actual ID (a downstream ledger step does that); lower-severity items resolve to an explicit
no-action line.

| ID | Type | Description | Location | Severity | Status |
|---|---|---|---|---|---|
| FA-D-01 | Referenced-but-undefined identifier | `cascade_alignment_modifier` (Ob_modifier component, §3.7) has zero formula anywhere in corpus; `expectation_alignment_modifier`'s `× {1,2}` term has no rule for selecting 1 vs 2 | `faction_behavior_v30.md` §3.7 | **P1** | Duplicate of Mode A finding FA-A-01 — see that file for full analysis. **PROPOSED-ED, lane=FA.** |
| FA-D-02 | Referenced-but-undefined generic mechanic | "Recognized Deed" is used as a Standing-5 gate condition across 4 primary ladders (Crown Seneschal, Hafenmark Chair, Varfell Jarl, Church Prelate — `faction_politics_v30.md` §1.1–§1.4) with per-faction prose ("an action... publicly endorsed") but **no universal mechanical procedure** (roll type, Ob/difficulty, adjudicator) the way "Formal Recognition Event" has (explicitly cites FAC-02, mandatory Zoom In). Four independent uses of the same named gate-type with no shared definition. | `faction_politics_v30.md` §1.1 row 5, §1.2 row 5, §1.3 row 5, §1.4 row 5 | P2 | **No action — flag for a future editorial pass to define "Recognized Deed" as a generic cross-faction mechanic (parallel to the existing "Formal Recognition Event" schema entry in `faction_canon_v30.md` §2).** Not filed as a new ED; each per-faction instance is individually flavorful enough that a GM/engine can adjudicate it narratively without a hard blocker, unlike FA-D-01's formula gap. |
| FA-D-03 | Orphaned namespace identifier | Löwenritter's `mission.primary_objective: victory.crown_peninsular_sovereignty` (`faction_state_authoring_v30.md` §7) is not one of the four non-Crown "approach-track identifiers" the FSA-1 reconciliation note explicitly enumerates (`solmundan_orthodoxy`, `dynastic_assertion`, `varfell_path_b`, `cultural_revolution` — see `faction_state_authoring_v30.md` §1 note). Löwenritter is the 6th canonical faction and has neither the universal-victory label nor a matching entry in that enumerated list; its own Mission-shift notes describe track-stage-driven shifts (Loyal→Restless→Autonomous→Split) that make the generic Mission-shift Trigger 1 ("victory-track milestone passes/fails") evaluation path ambiguous for this specific identifier. | `faction_state_authoring_v30.md` §1, §7 | P2 | **No action — flag for the next `victory_v30.md` cross-reference sweep** (out of this subsystem's target-doc set; `victory_v30.md` is the `victory` canonical system per `canonical_sources.yaml`, not one of the 5 faction_political heads). Low practical risk: Löwenritter's Mission-shift path is already separately and explicitly specified via Graduated Autonomy track-stage triggers in the same section, making the generic trigger largely redundant for this faction. Not filed as a new ED under lane FA — if pursued, this belongs with the `victory` system owner. |
| FA-D-04 | Self-contradictory in-doc status marker | `faction_behavior_v30.md` carries both `## Status: CANONICAL` (line 6) and, elsewhere in the same file, `**Status:** PROVISIONAL.` (line 11) and "End spec. PROVISIONAL pending ratification." (final line). `faction_canon_v30.md` has the identical pattern (`## Status: CANONICAL` at line 6 immediately followed by `## Status: PROVISIONAL — pending ratification` at line 7). | `faction_behavior_v30.md` lines 6/11/548; `faction_canon_v30.md` lines 6–7 | P3 (currency/editorial, adjacent to but outside strict mechanical scope) | **No action within this mechanical audit** — per the skill's "no editorial judgment" scope boundary, doc-status reconciliation belongs to `valoria-editorial-register` / the currency-consistency gate (`tools/currency_consistency_check.py`), not a mechanics audit. Noted here only because it affects how confidently the formula findings above (FA-A-01 etc.) should be treated as "blocking canonical mechanics" vs. "blocking a still-provisional draft" — recommend the editorial-register skill resolve the status line before/alongside any ED filed against FA-A-01. |
| FA-D-05 | Missing top-level range statement | Rank Standing's documented range (§1.0: "Standing 0 through Standing 7") omits the −1 Dismissed state introduced two subsections later (§1.0a). | `faction_politics_v30.md` §1.0 vs §1.0a | P3 | Duplicate of Mode B finding FA-B-01 — no action, documentation polish only. |
| FA-D-06 | Ambiguous shared-name track | Torben's "Generational Readiness" (§8.1, uncapped-sounding accrual, threshold ≥5) vs. "Readiness Track (0–10)" (§8.3, threshold ≥7) — unclear if same variable. | `faction_politics_v30.md` §8.1/§8.3 | P2 | Duplicate of Mode B finding FA-B-02 — no action, documentation-clarity flag only. |

## Gaps checked and found NOT present (verification, per skill's systematic-check requirement)

- **Placeholder sections** ("[Content as per prior ruleset]", "[TBD]"): none found literally in the
  5 target docs; the corpus's convention here is explicit `[GAP — Phase B authoring per ED-717]` /
  `[PROVISIONAL]` markers, all of which are already ledgered against named EDs (ED-717, ED-642,
  ED-649–658, etc.) — not unticketed placeholders.
- **Defined-but-never-referenced (orphaned) mechanics:** `institutional_culture` is narrow
  (single-consumer: feeds only α_institution) but is consumed, not orphaned — see Mode C.
  No fully-orphaned mechanic (defined with zero consumers) was found in-scope.
- **Missing edge-case rules** (value reaches 0, exceeds max, threshold crossed, simultaneous
  triggers): Stability=0 collapse (§1.5), Wealth=0 (§5.7), Deniability Debt cap=7 (§2.2b.ii),
  zero-territory factions (§11, cross-referenced to settlement_layer LPS-2d), and
  simultaneous-collapse ordering (§1.5 "process in descending Mandate order") are all explicitly
  specified. No missing edge case found beyond FA-A-05 (Standing-0 cascade participation, already
  logged as P3 in the formula audit).
- **Missing resolution procedures** (what happens when X and Y conflict?): Trigger-4/Trigger-5
  simultaneity, MS=0 vs IP≥80 simultaneous-catastrophe ordering (`stats_1_7_scale.md` §Simultaneous
  Catastrophe Rule), and Ransom-refusal vs ED-334 double-count (ED-NEW-007, resolved) are all present.
- **Missing tables:** Per-territory Public Temperament authoring (30–50 entries) is explicitly
  flagged as pending Phase B Stage 6 in `faction_canon_v30.md` §6 — already tracked, not a new gap.

**Overall Mode D disposition:** 1 P1 (FA-D-01, duplicate of FA-A-01, filed once — see formula_audit.md),
5 P2/P3 findings resolved to no-action documentation flags. No new gaps rise to P1 beyond the
`Ob_modifier` formula defect already captured under Mode A.
