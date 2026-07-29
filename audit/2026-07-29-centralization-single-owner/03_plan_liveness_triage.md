# Plan-liveness triage manifest — every plan-shaped file under `audit/`

## Status: EVIDENCE MANIFEST (read-only; rules nothing) — ED-IN-0103, 2026-07-29

**Why this file exists.** `01_orchestration_plan_v1.md` §7 and `workplans/README.md` both assert
"58 plan-shaped files, 7 live" (corrected to 8). Two independent critics flagged that as a **result
claim shipping without a reproducing instrument** — §0.1 point 4: *a number without a control is not
a measurement.* This is the manifest. It is the falsifier for those counts: if a row here is wrong,
the count is wrong, and both are checkable against the tree.

**Enumeration rule (stated, so it is reproducible):**
```
find audit -iname "*plan*.md" -o -iname "*workplan*.md" -o -iname "*roadmap*.md" \
        -o -iname "*execution*.md" -o -iname "*remediation*.md" -o -iname "*schedule*.md"
```
58 files. "Plan-shaped" means *filename*-shaped — a deliberately mechanical rule, so the population
is reproducible rather than judged. It over-includes (some hits are registers or reviews, noted per
row) and may under-include a plan with an unconventional name; that limit is real and stated.

**Evidence priority:** `CURRENT.md` → `HANDOFF.md` + all 9 `HANDOFF_<LANE>.md` →
`workplans/workplan_v6_progress.yaml` (contributed nothing — it references no `audit/` path) →
the file's own status text → `registers/editorial_ledger*.jsonl` → the ED-IN-0091 program's
documents → git recency (**mostly useless**: 51 of 58 carry the same `2026-07-21 22:22:34`
bulk-consolidation timestamp, not a real edit date).

**The measured finding that shaped the convention:** a `## Status:` heading is **not** a liveness
signal in either direction. Only 10 of 58 carry the canonical heading; **7 of those 10 are dead**;
and 3 of the live plans carry one reading "PROPOSED". Pointer files therefore carry an **explicit**
`liveness:` field. Inference was measured wrong in both directions, not assumed to be.

---

## LIVE (8) — the pointer work-list

| path | lane | ED | pointer |
|---|---|---|---|
| `2026-07-26-mass-battle-fable-audit/03_execution_plan.md` | MB | ED-MB-0045 v2 | `POINTER_2026-07-26_mass_battle_execution.md` |
| `2026-07-26-combat-balance-customization-state/combat_execution_plan.md` | PC | **none** (`HANDOFF_PC.md:9`) | `POINTER_2026-07-26_combat_execution.md` |
| `2026-07-26-combat-balance-customization-state/combat_remediation_plan.md` | PC | **none** | `POINTER_2026-07-26_combat_remediation.md` |
| `2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md` | IN | ED-IN-0091 | `POINTER_2026-07-29_code_shape_open_items.md` |
| `2026-07-29-code-shape-open-items/04_execution_ledger.md` | IN | ED-IN-0091/0092 | `POINTER_2026-07-29_code_shape_execution_ledger.md` |
| `2026-07-17-character-decision-adversarial-audit/01_remediation_L1_L2.md` | SC exec / IN umbrella | ED-IN-0073 | `POINTER_2026-07-17_character_decision_L1_L2.md` |
| `2026-07-17-character-decision-adversarial-audit/03_remediation_program.md` | IN | ED-IN-0073 | `POINTER_2026-07-17_character_decision_program.md` |
| **`2026-07-22-mass-battle-stress-test/full_implementation_plan_v1.md`** | MB | none | `POINTER_2026-07-22_mass_battle_full_implementation.md` |

⚠️ **The last row is a CORRECTION, recorded not hidden.** The first triage pass classified it
**SUPERSEDED** by the 07-26 MB plan. The third adversarial pass refuted that: it is `Status: PROPOSED`,
`HANDOFF_MB.md:763` heads its section "(IN PROGRESS)" under Jordan's "nothing is golden" directive,
and grepping the 07-26 plan for its Phase-1 items (B1/B2/B3/B5, geometry, col_grid, octagon,
`_node_pos`) returns only fork-5/G5/A4a — none of them. B1 has landed
(`tests/sim/mass_battle/geometry.py:252`), which makes the remainder *more* live, not less.
**A triage that buries a live plan is the precise failure the convention exists to prevent, and it
happened on the first attempt.** That is the argument for `ci_workplan_pointer_check.py`, and the
reason the liveness half of the guard is honestly deferred rather than faked.

Two siblings in that directory are live but get no pointer of their own, triaged explicitly rather
than by silence: `spatial_model_v2_plan.md` (LIVE — source of unbuilt P-DEC-2/3, cited
`HANDOFF_MB.md:453,473`) and `ratified_but_unbuilt_backlog.md` (LIVE, but a *register*, not a plan —
it schedules nothing). Both are named in the MB full-implementation pointer.

## SUPERSEDED (13)

`2026-06-10-master-workplan-v3/{README.md,valoria_master_workplan_v3.md}` (→ v4, own banner) ·
`2026-06-16-combat-reconciliation/combat_reconciliation_plan.md` (→ the 07-26 PC arc) ·
`2026-06-29-combat-corpus-recovery/{combat_foundation_build_plan.md,combat_workplan_v1_2026-06-18.md}` ·
`2026-06-30-combat-grounding/forward_roadmap.md` · `2026-06-30-massbattle-bottomup/05_redesign_workplan.md`
(⚠️ `valoria_master_workplan_v6.md` called this "the governing plan" via an **unresolvable path** —
corrected this commit) · `2026-07-14-gameplay-subsystem-observatory/remediation_plan_v1.md`
(⚠️ see disagreement 3) · `2026-07-22-mass-battle-stress-test/spatial_model_v2_plan.md`
(⚠️ **reclassified LIVE** by the third pass — see above; retained here to show the correction) ·
`2026-07-26-mass-battle-fable-audit/02_remediation_plan.md` · `2026-07-26-mass-battle-vector-audit/04_solutions_plan.md`
(both ~80% confidence, **no supersession banner on either** — the softest calls; an independent
critic separately confirmed the substance via `03_execution_plan.md:34-39` refuting
`02_remediation_plan.md:18-27`'s three headline mechanisms) · `ecosystem_workplan_2026-04-30.md`
(own banner) · `workplan_v1_throughline_2026-04-26.md` (v2's header supersedes it)

## COMPLETE (7)

`2026-06-28-deprecation-currency-sweep/{deprecation_currency_plan.md,v40_generation_plan.md}` ·
`2026-07-01-month-overview-architecture-consolidation/01_consolidation_execution.md` (every step-row
`done`) · `2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md` (merged PR #72) ·
`2026-07-08-crunch-cascade-cogload-legibility-audit/00_workplan.md` (`Status: COMPLETE`) ·
`2026-07-08-pessimist-action-audit/workplan_v6_register_deltas.md` (RATIFIED; ED-FA-0006/ED-FI-0004
both `resolved`) · `2026-07-14-gameplay-subsystem-observatory/00_workplan.md` (ED-IN-0064 `resolved`)

## HISTORICAL (29)

The 2026-04/05 bootstrap chain and frozen master-workplan records — `2026-04-30-architecture-session/×2`,
`2026-04-30-geography-audit/×3`, `2026-05-14-balance-audit/×2`, `2026-05-15-mb-comparative-audit/plan.md`,
`2026-05-16-multi-session-workplan/workplan.md` (self-declared "Active until v17 M7 ships"; repo is v40),
`2026-05-17-scene-combat-contest/planning_v0.md`, `2026-05-17-v18-integration/integration_plan_v18.md`
(carries `Status: CANONICAL` — the clearest proof a Status line is not a liveness signal; it targets
the retired `sim/` v18 tree), `2026-05-28-resolution-diagnostic/faction_remediation_development.md`,
`2026-05-29-massbattle-sim-foundation/13_massbattle_workplan.md`, `2026-05-31-percell-combat/percell_integration_plan.md`,
`2026-06-01-massbattle-stub-wiring/mb_engine_workplan.md`, `2026-06-11-orchestration/valoria_master_workplan_v4.md`
(frozen record per v6's own header), `2026-07-07-unaddressed-areas-audit/resolution_plan_v1.md`
(Stratum A executed; Stratum B residuals now tracked as per-lane EDs), `ecosystem_workplan_v2_2026-04-30.md`,
`initial_roadmap_2026-04-26.md`, `lane-c/2026-06-01-…_resume_audit_workplan.md`,
`other/workplan_v2_round{2,3}_audit_2026-04-27.md`, `valoria_systems_workplan{,_index}.md`,
`valoria_workplan_final{,_index}.md`, `workplan_review_2026-04-26.md`,
`workplan_v2_{gap_addendum,throughline}_2026-04-26.md`

## UNKNOWN (1)

`2026-07-08-crunch-cascade-pessimist-ners-contamination/00_workplan.md` — zero references anywhere in
`CURRENT.md`, any handoff, or any ledger; its three named entry points (thread-engine migration,
attribute-roster ratification, Godot export gap) trace to no ED I could find. **An UNKNOWN with no
pointer is silently treated as dead, which is the wrong default** for a file nothing disproves.
Settling it needs Jordan, or a corpus grep for those three entry points to see whether a
differently-titled ED absorbed them. Carried as an open question, not resolved by omission.

---

## Disagreements — recorded, deliberately not resolved here

1. **`HANDOFF_MB.md` labels the live MB plan "v1 (superseded)."** That bullet predates PR #250's
   in-place v2 correction and PR #252 naming it current. Recorded in the MB pointer so it is not
   inherited. **Not** silently reconciled — `HANDOFF_MB.md` is the MB session's to write.
2. **`valoria_master_workplan_v6.md`'s MB row** called `05_redesign_workplan.md` "the governing plan"
   at a path that resolves nowhere. **Corrected this commit** (it is an IN-owned file).
3. **`ED-IN-0066` is still `status: open`** with an unruled D1–D16 docket, though its execution
   surface was absorbed into ED-IN-0091. A naive ledger check reads it as live. Either the ledger row
   flips with a stated absorber, or the plan gets a pointer — currently neither.
4. **The two ~80%-confidence MB SUPERSEDED calls** carry no supersession banner on either file, and
   both are still bulleted under `HANDOFF_MB.md`'s `## Next actions`. The primary resume surface
   still points at them even though the pointer surface does not.

## Limits of this triage

Filename-shaped enumeration can miss an unconventionally-named plan. Classification of the 29
HISTORICAL rows was not individually re-verified by a second reader — the LIVE and SUPERSEDED rows
were. Git recency contributed nothing (bulk-consolidation timestamps). And the first pass got a LIVE
row wrong, which is the honest measure of how much confidence this manifest deserves: enough to act
on, not enough to skip the guard.
