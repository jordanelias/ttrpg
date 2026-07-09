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
  the weight set as versioned data; values revisable anytime). Remaining T0 wall: JD-1 (PC)
  + ED-1051 (engine_clock); fork 10's faction count = ED-FA-0001 (needs_jordan).
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
- **Reserved-ID state:** the flat `ED-NNNN` sequence is FROZEN at `ED-1094` (2026-07-02
  cutover, `ED-IN-0001`). All NEW EDs use `ED-<LANE>-NNNN` — `references/id_reservations.yaml`'s
  `lane_ids` section is the live allocation source; read `next_free` for your lane, allocate,
  bump, co-commit. Never max+1.
