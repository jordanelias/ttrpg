# Threadwork — Mode D: Gap Detection

**Scope:** `designs/threadwork/threadwork_v30.md`, `params/threadwork.md`,
`designs/threadwork/thread_horizontal_integration_spec.md`.

Findings from Modes A–C that are themselves gaps (P-25 truncated table, homeless Coherence cap,
Thread Debt homing gap, empty Combat Timing section, History-bonus ambiguity) are cross-referenced
here rather than fully repeated — see the disposition column for the owning file.

| ID | Type | Description | Location | Severity | Status |
|---|---|---|---|---|---|
| D1 | Missing table (content-loss) | P-25 "Scale-based Mending Stability" override table truncated to header row + "Object" with zero data. Present since the line's introduction (confirmed via `git log --follow -p`: no prior revision had complete data — this is an original authoring truncation, not a regression). | `threadwork_v30.md` line 40 | P1 | See `formula_audit.md` A7 — **PROPOSED-ED, lane=WR** |
| D2 | Referenced but undefined (partially — homing gap) | "Thread Debt" token consumed/cleared in both target docs (CM-12; mass-battle expiry line) with no accrual/definition in either. | `threadwork_v30.md` line 770; `params/threadwork.md` line 180 | P2 | See `mechanic_dependency_graph.md` — **no action, already surveyed 2026-07-08, KEEP/homing-gap verdict** |
| D3 | Missing resolution procedure (empty section) | `### Combat Timing` subsection header under §2.6 Opposing Operations has no body content. | `threadwork_v30.md` line 599 | P2 | See `mechanic_dependency_graph.md` — **PROPOSED-ED, lane=WR** |
| D4 | Referenced but undefined (broken internal cross-reference) | "Chronic perception (P-13): *Already patched into §2.7 chronic table.*" — **§2.7 does not exist.** Section headings in Part Two run 2.1 → 2.2 (struck) → 2.3 → 2.4 → 2.5 → 2.6, then jump directly to Part Three. The chronic table this patch presumably means is the "Chronic consequences" table inside §2.4 Locking. | `threadwork_v30.md` line 442 | P2 | **[NEW] PROPOSED-ED, lane=WR** |
| D5 | Doc-status contradiction | Document header simultaneously declares `## Status: CANONICAL` (line 7) and `## Authority: ... this document (design proposal, requires editorial approval)` (line 9) — self-contradictory status framing for the entire skeleton. | `threadwork_v30.md` lines 7–9 | P2 | **[CONFIRMED-OPEN, prior audit]** — already flagged in `references/module_contracts.yaml` line 299 as `[OPEN — Jordan]` doc-status ambiguity. **no action — already tracked** |
| D6 | Missing edge case — cumulative Leap-failure TPS penalty floor | Leap Failure imposes "−1D to Thread Pool Score for remainder of scene" with no stated floor on TPS itself if a practitioner fails multiple Leaps in one scene (unlike the universal 1D pool floor in `params/core.md`, which floors the total pool, not an intermediate term). | `threadwork_v30.md` §2.3, Leap degree table | P3 | See `formula_audit.md` boundary-check note — **no action, insufficient evidence of an actual negative-pool outcome; recommend stating a TPS floor of 0 for completeness only** |
| D7 | Missing cross-reference — seasonal MS cap vs. per-scene PP-197 drain | PP-197 (TS90+ Coherence-0 Reality Strain) states an uncapped-looking "−1 MS per scene" cost with no explicit statement of whether it counts against the stated "±10 per season" seasonal MS cap (§5.5 Hybrid) or bypasses it. | `threadwork_v30.md` §3.7 (PP-197) vs. §5.5 | P3 | See `formula_audit.md` A6 — **no action, not confirmed as an actual conflict; recommend an explicit cross-reference note only** |
| D8 | Ambiguous formula — History-bonus sub-term | Two non-identical natural-language statements of the Thread Pool's History-bonus term across the two co-canonical sources. | `params/threadwork.md` §Thread Pool vs. `threadwork_v30.md` §2.3 | P2 | See `formula_audit.md` A2 — **PROPOSED-ED, lane=WR** |
| D9 | Undocumented asymmetric floor | Pulling alone carries a special 5D pool floor (R-57); the other five Thread ops fall back to the generic 1D `params/core.md` floor with no stated rationale for the difference. | `params/threadwork.md` R-57 | P2 | See `formula_audit.md` A3 — **PROPOSED-ED, lane=WR** |
| D10 | Missing rounding rule | Fractional +0.15 Ob/wound stacked against an otherwise-all-integer Three-Axis Ob system, with no stated rounding convention, and a self-contradicting "integer Ob"/"fractional Ob" pair in the doc threadwork cites as authoritative (`derived_stats_v30.md` §13). | `threadwork_v30.md` §2.3 (×3), §2.4 | P2 | See `formula_audit.md` A4 — **PROPOSED-ED, lane=WR** |
| D11 | Terminology collision | "Knot Strain" names two mechanically unrelated tracks (ED-912 bond-strain gauge vs. §2.6 opposing-ops Ob/Composure penalty). | `params/threadwork.md` §Knot Mechanics vs. `threadwork_v30.md` §2.6 | P2 | See `mechanic_dependency_graph.md` — **PROPOSED-ED, lane=WR** |
| D12 | Namespace collision | Local "P-11..P-31" stress-test-patch IDs collide with `canon/02_canon_constraints.md`'s P-01–P-15 constraint IDs within the same document, sometimes both meanings appearing in the same file. | `threadwork_v30.md`, multiple locations (see number_systems_audit.md) | P2 | **[NEW] PROPOSED-ED, lane=WR** — same finding as `number_systems_audit.md`; not double-filed. |
| D13 | Placeholder/orphaned section headers with no content | `## PHILOSOPHICAL FOUNDATION` (line 96) is a bare heading with nothing beneath it before `# PART TWO: OPERATIONS` begins two lines later; similarly `## 6.1 Ontological Status` (line 873) and `## 3.1 What Coherence Measures` region both open with blank space before their first real content line (the latter recovers content quickly; the former, `## PHILOSOPHICAL FOUNDATION`, never does within this skeleton — consistent with the file's own header note "SKELETON — mechanical spec only... DO NOT add prose. Rationale/examples live in the infill file," so this is very likely correct-as-designed co-filing, not a defect). | `threadwork_v30.md` line 96; line 873 | P3 | **no action — working as intended, skeleton/infill co-filing convention (CLAUDE.md §4); confirmed the corresponding prose exists in `threadwork_v30_infill.md` §3.1/§6.1** |
| D14 | Stale target paths in a CANONICAL cross-cutting spec | `thread_horizontal_integration_spec.md`'s own propagation-map table cites target paths from the pre-2026-04-13 directory layout that no longer exist verbatim: `designs/hybrid/scale_transitions_v30.md` (now `designs/architecture/scale_transitions_v30.md`), `designs/systems/player_agency_v30.md` (now `designs/architecture/player_agency_v30.md`), `designs/systems/settlement_layer_v30.md` (now `designs/territory/settlement_layer_v30.md`), `designs/conviction_track/conviction_track_v30.md` (now `designs/scene/conviction_track_v30.md`), `designs/systems/npc_behavior_v30.md` (now `designs/npcs/npc_behavior_v30.md`), `designs/ttrpg/threadwork_v30.md` (now `designs/threadwork/threadwork_v30.md`, ED-673/677/681's own self-referential target), `designs/characters/character_histories_v30.md` (now `designs/world/character_histories_v30.md`), `designs/systems/investigation_systems_proposal_2026-04-15.md` (superseded entirely by `designs/scene/investigation_systems_v30.md`). Cross-checked: the actual content changes (ED-673 through ED-681) **are** present at the *correct current* locations (verified via grep across the corpus — see below) — the propagation clearly executed successfully at some point. Only the spec's own self-documenting "PROPAGATION MAP" table (§ near end of file) was never updated to reflect the 2026-04-13 rename sweep, so a future reader trying to verify "did ED-674 actually land?" by following this doc's own pointer would be sent to a path that doesn't exist. | `thread_horizontal_integration_spec.md` §PROPAGATION MAP table (all 11 rows) | P2 | **[NEW] PROPOSED-ED, lane=WR** |

## Verification detail for D14 (propagation actually landed, just at stale-cited paths)

Confirmed via corpus grep (`ED-673`..`ED-680`, excluding archives/audit workings):
- ED-673 (Thread Domain Echo) → present in `designs/architecture/scale_transitions_v30.md` and `scale_transitions_v30_index.md`.
- ED-674 (Scene Slate Thread-State Factor) → present in `designs/architecture/player_agency_v30.md`.
- ED-675 (Settlement Thread Environment) → present in `designs/provincial/faction_layer_v30.md` and `faction_layer_v30_index.md`.
- ED-676 (CV Movement from Thread ops) → present in `designs/scene/conviction_track_v30.md` and `conviction_track_v30_index.md`.
- ED-678 (Lifepath → TS/Certainty) → present in `designs/provincial/faction_layer_v30.md`.
- ED-679 (Thread Warfare NPC AI Doctrine) → present (referenced in multiple audit dossiers as applied).
- ED-680 (Case Board Dual-Depth Overlay) → present in `designs/scene/investigation_systems_v30.md` and `investigation_systems_v30_index.md`.
- ED-677 and ED-681 are directly visible, applied in-place, inside `threadwork_v30.md` itself (§2.3 "Rendered-Level Thread Event Visibility (ED-677)"; §3.7 "Rendering Crisis — Narrative Structure (ED-681)").

So the mechanical content is not missing — only the spec's own self-referential map is stale. This downgrades what could otherwise look like a P1 "propagation never happened" finding to a P2 documentation-currency issue.

## Disposition summary

| Finding | Severity | Disposition |
|---|---|---|
| D1 — P-25 table truncated | P1 | **PROPOSED-ED, lane=WR** (= formula_audit A7) |
| D2 — Thread Debt homing gap | P2 | no action — already surveyed 2026-07-08 |
| D3 — empty Combat Timing section | P2 | **PROPOSED-ED, lane=WR** (= mechanic_dependency_graph finding) |
| D4 — broken §2.7 cross-reference | P2 | **PROPOSED-ED, lane=WR** |
| D5 — CANONICAL vs. "design proposal" header contradiction | P2 | no action — already tracked, `module_contracts.yaml` `[OPEN — Jordan]` |
| D6 — TPS cumulative-failure floor | P3 | no action — not confirmed as a live defect |
| D7 — PP-197 vs. seasonal MS cap cross-reference | P3 | no action — not confirmed as a live conflict |
| D8 — History-bonus ambiguity | P2 | **PROPOSED-ED, lane=WR** (= formula_audit A2) |
| D9 — Pulling-only pool floor | P2 | **PROPOSED-ED, lane=WR** (= formula_audit A3) |
| D10 — fractional-Ob rounding gap | P2 | **PROPOSED-ED, lane=WR** (= formula_audit A4) |
| D11 — Knot Strain terminology collision | P2 | **PROPOSED-ED, lane=WR** (= mechanic_dependency_graph finding) |
| D12 — P-NN namespace collision | P2 | **PROPOSED-ED, lane=WR** (= number_systems_audit finding) |
| D13 — bare Part-header placeholders | P3 | no action — working as intended, skeleton/infill convention |
| D14 — stale propagation-map target paths | P2 | **PROPOSED-ED, lane=WR** |
