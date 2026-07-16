# Handoff

Plain, hand-maintained continuity for Valoria. Update this when you pause mid-task; a
git commit *is* the session close. The SessionStart banner (`tools/session_status.py`)
surfaces the "Next actions" section below, alongside `git status` / last commit.

This replaces the old session-log + `canon/session_checkpoint.md` + checkpoint machinery
(which depended on the retired GitHub-API harness and token budgets).

## History

Full narrative for the work below (2026-06-24 through 2026-07-02) moved to
`handoffs/HANDOFF_archive.md` (2026-07-08, token-efficiency pass) — this file had drifted from
"index" to a full append-only session log. Nothing was deleted, only relocated; the archive is
frozen, do not resume work from it.

Per-lane continuity now lives in `handoffs/HANDOFF_<LANE>.md`, using the same 9 lane codes as
the `ED-<LANE>-NNNN` editorial namespace (`ED-IN-0001`, `CLAUDE.md` §3). This file is the
**index** plus genuinely cross-cutting items — read the lane file(s) relevant to your session
before starting work, and keep your own updates scoped to your lane's file (or this one, only
for cross-cutting items).

| Lane | Subsystem | File |
|---|---|---|
| `MB` | Mass battle | `handoffs/HANDOFF_MB.md` |
| `PC` | Personal / scene combat | `handoffs/HANDOFF_PC.md` |
| `FI` | Field investigation | `handoffs/HANDOFF_FI.md` |
| `SC` | Social contest | `handoffs/HANDOFF_SC.md` |
| `FA` | Faction actions | `handoffs/HANDOFF_FA.md` |
| `WR` | World | `handoffs/HANDOFF_WR.md` |
| `IN` | Infrastructure / cross-cutting | `handoffs/HANDOFF_IN.md` |
| `GO` | Godot conversion | `handoffs/HANDOFF_GO.md` |
| `SE` | Settlements | `handoffs/HANDOFF_SE.md` |

**Why the split:** the ID-collision incidents that motivated `ED-<LANE>-NNNN` (two same-session
concurrent-allocation collisions on the flat sequence within one PR — see `ED-1094`'s ledger
entry) are the same failure class that makes one shared `HANDOFF.md` a merge-collision magnet
once multiple lane-sessions run concurrently. This is a **partial, deliberate exception** to the
repo's earlier "one continuity surface" consolidation (`deprecated/session_machinery/` retired
per-topic session-log files because they rotted independently) — the difference is this split is
keyed to the SAME lane taxonomy the ID system already enforces, not an ad-hoc per-topic split,
and this root file remains the one stable SessionStart entry point.

**Full detail on the split itself, and every historical decision predating it, is filed at
`handoffs/HANDOFF_IN.md`'s Decisions log** — this root file does not duplicate that history.

## Next actions

_(Reserved-ID state healthy as of 2026-07-01: **LB-21 executed** — `id_reservations.yaml` v3
verified live max, allocated ED 1081–1087 to the month-overview consolidation from
block D, and pre-provisioned disjoint Round-3 block E (ED 1100–1149 / PP 830–849). Allocate
per the file's protocol; never max+1. Since the 2026-07-02 cutover (ED-IN-0001), new EDs
allocate per-lane from `lane_ids` — the flat sequence is frozen.)_

- **Current state (2026-07-16).** The **sole remaining T0 blocker** on M1 is **ED-1051**
  (engine_clock ratification — default: flip `references/module_contracts.yaml` `engine_clock`
  `doc:null` → `designs/architecture/propagation_spec_v1.md`); it also gates the GO lane's
  Gate-0 entry. Governance **D1–D6 RULED 2026-07-13** (ED-IN-0046/0047): the FA §1.0c/§1.0d/§2.5
  riders, B1 faction-count = 4, and B12's new Settlement→Territory→Province→Duchy→Country
  hierarchy await ratification-flip + authoring (E11 symmetric suspicion-reduction; **L/PS
  wiring** is flagged the single highest-priority open item). The dashboard's proposals register
  was made honest 2026-07-16 (**ED-IN-0071**): of the open work, ~136 items are genuinely
  agent-executable (no ruling needed) and ~97 need your decision — see
  `tools/observability/PROPOSALS.md`. Lane detail in each `handoffs/HANDOFF_<LANE>.md`.
- **Mobile-friendly status dashboard built (2026-07-11, ED-IN-0031)** — `docs/dashboard/`,
  published by `.github/workflows/dashboard.yml` to GitHub Pages. Surfaces workplan progress,
  recent activity, a "needs your decision" inbox, and audit/simulation-balance verdicts
  (`references/audit_registry.jsonl`, now kept current by the 8 audit/simulation skills'
  retrofitted registry-append step). **One manual step needed from Jordan before it goes
  live:** repo Settings → Pages → Source: "GitHub Actions" (the default token can't flip this).
  **Extended 2026-07-11 (ED-IN-0037** — renumbered from a collision with PR #122's concurrent
  audit-ecosystem batch, which independently claimed ED-IN-0032 through 0036; see
  `references/id_reservations.yaml`'s IN-lane comment**)**: Balance & victory data card (personal-combat weapon
  matrix — flagged stale; faction win-share goldens from `sim/tests/`, labeled as CI regression
  guards, not a persisted full-campaign run; honest no-data flags for mass_battle/social_contest/
  threadwork/settlement_territory) + Registers card (editorial-ledger open/needs_jordan counts by
  lane, active patch-register counts). Also corrected a stale dashboard callout that had been
  repeating the now-debunked "~87% degenerate win-share" claim (CLAUDE.md §7) — see
  `sim/tests/test_f7_smoke_oracle.py`'s docstring for the actual correction.
- **ED-IN-0044 RATIFIED 2026-07-12 (simulation/test harness methodology + Gate-0 prototype).**
  `designs/audit/2026-07-12-simulation-test-harness-methodology/` +
  `tools/sim_harness/` (six rounds of adversarial review/stress-testing since filing, 34 real bugs
  found and fixed — see the package's own README). §11's four open questions were put to Jordan
  directly, not assumed: rollout order extended (§8 gained faction actions/settlement-territory/
  threadwork as waves 5–7, per Jordan flagging the gap; field investigation excluded as still
  stub-only); Wave 1 CI burn-in stays full report-only; `mc_v18` never gates a PR; the four §9
  quick wins filed separately as **ED-IN-0045** (open, execution pending — see
  `handoffs/HANDOFF_IN.md`). Full resolution text: `canon/editorial_ledger_in.jsonl`.
- **JORDAN RULING NEEDED — ED-SC-0015 (Parliamentary total-victory Mandate stacking).** Full
  detail in `handoffs/HANDOFF_SC.md`'s Pending section (also cross-referenced from
  `handoffs/HANDOFF_FA.md`). The one item from the 2026-07-08 FA/SE historical-precedent build
  genuinely needing Jordan's own call, not routine merge-ratification — everything else in that
  build ratifies normally on merge per ED-1094.
- **START HERE — Master Workplan v6 is the live steering surface, RATIFIED with the whole
  of PR #78 (2026-07-05, ED-IN-0009/ED-IN-0011 — Jordan: "Ratify commit merge all").** `designs/workplans/valoria_master_workplan_v6.md`: North-Star milestones (M1 one
  playable season · M2 any-seed story bar · M3 Godot slice), per-lane workstreams (status
  stays in `handoffs/HANDOFF_<LANE>.md` — v6 only sequences), and the tiered T0/T1/T2
  Jordan-decision register (§5) that **supersedes the 2026-07-01 `decision_queue.md` as the
  live decision list** (that file is now a dated snapshot; its items 1–3 were refreshed at
  supersession). Steering reconciliation ED-IN-0006 EXECUTED: `roadmap_state.yaml` retired to
  `deprecated/references/`, workplan v5 archived with banner (its J-38 contradiction
  corrected), hierarchy adopted (CURRENT.md → lane handoffs → workplan-derived). Same PR:
  the **narrative engine v2 "Churn Engine"** (`designs/audit/2026-07-05-emergent-narrative-engine/
  narrative_engine_design_v2_churn.md`, five-refuter adversarial pass applied) — **RATIFIED
  in full 2026-07-05 (ED-IN-0011), including F-F/fork-8 at its default** (subtract-only +
  the weight set as versioned data; values revisable anytime). Remaining T0 wall: **ED-1051
  (engine_clock) alone** — JD-1 RULED 2026-07-08 (U1/ED-PC-0010) and fork 10's faction count
  RULED = 4 (2026-07-13, ED-IN-0047, resolves ED-FA-0001); both struck from the wall.
- **Month-overview + consolidation (2026-07-01), doctrine + propagation spec RATIFIED (2026-07-02).**
  Full narrative + the 23-item Jordan decision queue: `designs/audit/2026-07-01-month-overview-architecture-consolidation/`
  (`decision_queue.md` first) and `handoffs/HANDOFF_IN.md`'s Next actions. Doctrine ratification
  (ED-1083) and J-38 propagation-spec authorship (ED-1093) are both **CANONICAL** as of PR #58
  (ED-1094 merge-ratifies-by-default).
- **Per-lane "Next actions" content lives in each lane's own file (2026-07-08 atomization pass)** —
  this root file no longer carries lane-owned detail, only genuinely cross-cutting items. Every
  lane-specific bullet previously here was cross-checked against its lane file first and dropped only
  where already covered (one gap found and backfilled: the R2 capstone finding → `HANDOFF_PC.md`;
  J-36 → `HANDOFF_IN.md`). Start with:
  - **Mass battle** (coordinate-field engine, DG-1..DG-5, the open partition-invariance ruling):
    `handoffs/HANDOFF_MB.md`.
  - **Personal / scene combat** (R2 capstone finding, Track-2 residuals, weapon-morphology
    consolidation, JD-1..JD-9): `handoffs/HANDOFF_PC.md`.
  - **Infrastructure / CI** (LB-22/23/24 residuals, LA-23 ledger reconciliation, J-36):
    `handoffs/HANDOFF_IN.md`.
  - **Social contest** (ED-SC-0015, J-31): `handoffs/HANDOFF_SC.md`.
- **Reserved-ID state:** the flat `ED-NNNN` sequence is FROZEN (2026-07-02 cutover,
  `ED-IN-0001`) — the ruling `ED-1094` established the freeze; the live ceiling is `ED-1096`
  (ED-1095/1096 landed same-day). All NEW EDs use `ED-<LANE>-NNNN` — `references/id_reservations.yaml`'s
  `lane_ids` section is the live allocation source; read `next_free` for your lane, allocate,
  bump, co-commit. Never max+1.
