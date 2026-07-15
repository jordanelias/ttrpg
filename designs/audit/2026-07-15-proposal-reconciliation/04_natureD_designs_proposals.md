# 04 — Nature-D: the dashboard-invisible proposals in `designs/proposals/`

## Status: REFERENCE (analysis + executed status-line additions; anchors ED-IN-0068)

**Systemic finding.** `designs/proposals/` holds **9 design proposals the dashboard never surfaced.** The
scan (`tools/dashboard_data.py::build_proposals`) is anchored on a markdown **heading** —
`^#{1,3}\s*Status:` — but all 9 carry their status as a **bold inline** line (`**Status:** …`), which the
regex does not match. So a whole directory literally named `proposals/` was invisible to the
"awaiting ratification" register. This pass adds a `## Status:` heading to each (reconciled disposition
below), which both fixes the invisibility and records the reconciliation verdict. **Recommended follow-up
(IN lane, tooling):** widen `build_proposals()` to also read bold-inline `**Status:**` lines, or add a CI
nudge that flags a `designs/**` doc with a bold status but no heading status — otherwise the next
bold-status proposal is invisible again.

Dispositions were verified against the current canonical heads (`designs/scene/combat_engine_v1/`,
`designs/provincial/mass_battle_v30.md`, `designs/provincial/faction_*_v30.md`) + `handoffs/HANDOFF_MB.md`
/`HANDOFF_PC.md` + the lane ledgers. (Repo git history is squashed to one 2026-07-08 snapshot, so
absorption was checked by grepping the head docs for each proposal's distinctive mechanic names, not by
commit dates.)

| # | Doc | Lane | Disposition | Evidence (head / ED) | Reconciled `## Status:` added |
|---|---|---|---|---|---|
| 1 | `2026-05-16-PC-4.4-unified-success-stress.md` | FA | **LIVE / UN-ADOPTED** | No trace of success-stress / Bureaucratic-Independence / Schism triggers in `faction_behavior_v30`/`faction_politics_v30`/`params/factions`; only the pre-existing Löwenritter Coup trigger — the status quo this doc set out to generalize | `PROPOSED — LIVE/UN-ADOPTED … HELD FOR JORDAN` |
| 2 | `2026-05-16-faction-audit-followup-plan.md` | FA/IN | **STALE / OBSOLETE** | Phase-0/1 closed same-day; Phase-2 Jordan decisions never taken; already a 2026-06-28 sweep Bucket-B archive candidate | `SUPERSEDED / OBSOLETE … archive candidate` |
| 3 | `2026-05-25-mechanics-integration-v3_1.md` (1288L) | FA/SE | **LIVE / UN-ADOPTED** (functionally stale) | None of the 31 proposals' distinctive names (Puppet Title, Provincial Charter Track, Leagues, Crown Legitimacy Contestation, …) appear in current `provincial/`/`territory/`/`governance_play_redesign`; Sprint-0 prereqs never run | `PROPOSED — LIVE/UN-ADOPTED (31 proposals) … HELD FOR JORDAN — review vs the 2026-07-08/09 comparative-governance-research corpus first` |
| 4 | `mass_battle_fighting_withdrawal_v1.md` | MB | **PARTIAL** | §4 step-1 yield BUILT (ED-MB-0005, 2026-07-08; `test_mass_battle_yield.py` 9 green) | `PARTIALLY SUPERSEDED … live record HANDOFF_MB; residual §2.2/§2.4 + calibration HELD` |
| 5 | `mass_battle_shape_echelon_revamp.md` | MB | **ABSORBED** | `mass_battle_v30 §A.6` carries the matching ED-909/ED-1088 Unit-level `build_envelopment`/`build_refused_flank` banner; only allocation-grid UI deferred to Stage-E | `SUPERSEDED — absorbed into mass_battle_v30 §A.6` |
| 6 | `multiunit_envelopment_plan.md` | MB | **LIVE / UN-ADOPTED** | HANDOFF_MB states Path-B cross-Unit envelopment is distinct + unbuilt; `run_multi_unit_battle` still resolves 1v1 lane pairings | `PROPOSED — LIVE/UN-ADOPTED (Path-B distinct, unbuilt) … HELD FOR JORDAN` |
| 7 | `pc_formation_system.md` | MB | **PARTIAL** | Engine half BUILT (brace/missile-density/ROLE_SPEC/kiting, §11/§13 commits, `tests/sim/mass_battle/`) | `PARTIALLY SUPERSEDED … residual §8 canon reconcile (ED-909 park) + §9 opens HELD` |
| 8 | `stub_infill_plan.md` | IN | **ABSORBED** | Doc's own final amendment: "Pass 2l stub infill — COMPLETE, 37/45 implementable"; `sim/` progressed past it | `SUPERSEDED — Pass-2l complete; historical roadmap` |
| 9 | `weapon_physics_and_concentration_model.md` | PC | **PARTIAL** | §§1–6 composite-mass/PoB BUILT (`combat_engine_v1/weapon_physics.py`; ED-PC-0010 resolved recalibration) | `PARTIALLY SUPERSEDED … residual §7 concentration-error (T_err/ERR_K) never built, HELD` |

## Held-for-Jordan (from Nature D) — see `01_reconciliation_map.md §Held-back`

- **#1 PC-4.4 success-stress** (FA) — revive or drop the turn-on-you faction-vulnerability generalization.
- **#3 mechanics-integration-v3.1** (FA/SE, 31 items) — a *scoping* decision: none built, heavy thematic
  overlap with the newer, evidence-grounded comparative-governance-research corpus. Recommend a triage
  pass mapping its 31 items against `ED-FA-0008..0044` / `ED-SE-0007..0044` before reviving any.
- **#6 multiunit Path-B envelopment** (MB) — greenlight the still-unbuilt army-scale spatial mechanism or not.
- **Residuals of the 3 PARTIALs** (#4 yield exits/calibration, #7 §A.6 dice-vs-geometry reconciliation,
  #9 §7 concentration-error) — each already scoped in its head/handoff; recommend filing as lane handoff
  items (MB/MB/PC) rather than leaving them buried in a proposals doc.

**Recommended lane routing** if Jordan greenlights any: #1/#3 → FA (+SE for #3); #4/#6/#7 → MB;
#9 → PC. No ED allocated by this pass for these — they are decisions, not defects.
