# Handoff

Plain, hand-maintained continuity for Valoria. Update this when you pause mid-task; a
git commit *is* the session close. The SessionStart banner (`tools/session_status.py`)
surfaces the "Next actions" section below, alongside `git status` / last commit.

This replaces the old session-log + `canon/session_checkpoint.md` + checkpoint machinery
(which depended on the retired GitHub-API harness and token budgets).

## Lane-tagged handoffs (2026-07-02)

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

**Note on `designs/audit/2026-06-30-open-items-adjudication-docket.md`:** that file (PR #68,
filed concurrently by a different session while this session was independently adjudicating the
same five items from a pasted copy) is now **ADJUDICATED, not still pending** — see its own
updated status header. Verdicts: D1/D5 resolved and struck, D2/D3 still open with materially
changed context, D4 partially done and narrowed. Detail lives in `handoffs/HANDOFF_PC.md` (D1),
`handoffs/HANDOFF_IN.md` (D2/D3/D4/D5), and `decision_queue.md` items 5/12/24/25 — not repeated
here.

**Full detail on the split itself, and every historical decision predating it, is filed at
`handoffs/HANDOFF_IN.md`'s Decisions log** — this root file does not duplicate that history.

## Next actions

- **START HERE — month-overview + consolidation (2026-07-01), doctrine + propagation spec
  RATIFIED (2026-07-02); HANDOFF split into per-lane files (2026-07-02).** The month's
  comprehensive review, the consolidation execution/reconciliation logs, and the single
  consolidated Jordan decision queue live at
  `designs/audit/2026-07-01-month-overview-architecture-consolidation/` (see `decision_queue.md`
  first — every gated cross-lane item is indexed there). For subsystem-specific continuity,
  go to your lane's file in the table above; `handoffs/HANDOFF_IN.md` carries the full
  cross-cutting/governance narrative (doctrine ratification, ED-<LANE>-NNNN namespace creation,
  merge-ratifies-by-default convention, ecosystem-review residuals not owned by another lane).
- **Reserved-ID state:** the flat `ED-NNNN` sequence is FROZEN at `ED-1094` (2026-07-02
  cutover, `ED-IN-0001`). All NEW EDs use `ED-<LANE>-NNNN` — `references/id_reservations.yaml`'s
  `lane_ids` section is the live allocation source; read `next_free` for your lane, allocate,
  bump, co-commit. Never max+1.
