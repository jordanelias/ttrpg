---
name: valoria-workplan-navigator
description: >
  Answer "where are we?" and "resume from the workplan" for the Valoria master workplan.
  Use when Jordan asks any of: "where are we", "where are we in the workplan", "workplan
  status", "what's next", "show progress", "am I making progress", "resume from the
  workplan", "resume work", "pick up where we left off", "what should I work on". This
  skill owns workplan-position reporting and resume-option presentation — never answer
  those questions inline from memory or from the workplan doc alone; the position comes
  from the progress board, freshness-verified. Every answer ends with concrete options
  (AskUserQuestion) so a next step is always one selection away.
---

# Valoria Workplan Navigator

Reports the tracked position against `designs/workplans/valoria_master_workplan_v6.md`
(milestones M1/M2/M3), keeps the progress board honest, and always presents options.
Surfaces (established by ED-IN-0010):

- **Board** (the one rollup-status home): `designs/workplans/workplan_v6_progress.yaml`
- **Renderer** (one rule, one home): `python3 tools/workplan_status.py [--full|--check]`
- Status detail stays in `handoffs/HANDOFF_<LANE>.md`; decisions in the workplan §5
  register + the editorial ledger (`registers/editorial_ledger.jsonl` for pre-cutover flat
  IDs, plus every live `registers/editorial_ledger_<lane>.jsonl` for `ED-<LANE>-NNNN` entries
  — CLAUDE.md §3). The board only points at them.
- **Dashboard** (a published rendering, not an independent data source): `docs/dashboard/`
  (built by `tools/dashboard_data.py` from this board + `references/audit_registry.jsonl`)
  surfaces the same workplan progress plus a "needs your decision" inbox and
  audit/simulation verdicts. Useful as a mobile-friendly pointer for Jordan, but this
  skill's own board + freshness gate remain authoritative — the dashboard reads from them,
  never the other way around.

## Input validation (MANDATORY before any workflow)

Read from the working tree — never from memory:

- `designs/workplans/workplan_v6_progress.yaml` — the board. **If missing or unparseable,
  STOP and offer to regenerate it** from workplan v6 §1/§3/§4 + the lane handoffs (that
  regeneration is Workflow C run over every row).
- `designs/workplans/valoria_master_workplan_v6.md` — §1 (milestones/junctures), §5
  (tiered decision register; T0 list). If a v7+ exists per `CURRENT.md`'s workplan row,
  use it and flag that this skill + board need re-keying to the new version.
- Root `HANDOFF.md` "Next actions" (cross-lane in-flight work the board may not carry yet).

## Freshness gate (run FIRST, both workflows)

1. `python3 tools/workplan_status.py --check` — it warns when workplan-relevant paths
   (`designs/`, `handoffs/`, `canon/`, `sim/`) changed since the board's last-touch
   commit; the check is authoritative.
2. If it warns: BEFORE answering, find what changed (`git log --name-only
   <board-last-touch>..HEAD`), read the touched lanes' `handoffs/HANDOFF_<LANE>.md`
   (+ ledger for new ED resolutions), and update the affected board rows — state, `next`,
   `evidence`, `blocked_on` (a ruled fork comes OFF `decisions_t0_open`). Set `as_of` to
   current HEAD sha + date (the human-facing record), append one `last_progress` line for
   anything that landed. Commit `[editorial] Refresh workplan progress board (as_of
   <sha>)` — the refresh is part of answering, not a favor.
3. Never present a stale position silently. If you cannot refresh (e.g. read-only
   context), print the staleness warning verbatim above the report.

## Workflow A — "Where are we?"

1. Freshness gate.
2. Run `python3 tools/workplan_status.py --full` and present its output verbatim (the
   ASCII diagram IS the answer's lead — do not paraphrase it away), followed by, in prose:
   - **Progress since last check**: the `last_progress` delta — what landed, with PR/ED
     cites. This is the "you are making progress" signal; lead with it when non-empty.
   - **What's blocked and on whom**: the open T0 decisions, each with what ruling it
     unblocks (from workplan v6 §5).
3. End with **AskUserQuestion** built by the option rule below. Never end with a bare
   report.

## Workflow B — "Resume from the workplan"

1. Freshness gate (compressed report: the diagram + one line of delta).
2. **AskUserQuestion** with 2–4 resume options (option rule below).
3. On selection: read that lane's `handoffs/HANDOFF_<LANE>.md` in full + the workplan v6
   §4 row for the lane; declare the lane (allocate any EDs as `ED-<LANE>-NNNN` per
   `references/id_reservations.yaml` protocol); begin the increment. If the selection was
   a decision sitting, present each T0/T1 fork as its own AskUserQuestion with the
   register's default as the recommended option, then execute the rulings (ledger flips +
   board update + affected-doc edits).

## Option rule (2–4 options, priority order, each stating: what it advances · gate · size)

1. **Highest-leverage ready-now increment** — first board row with no `blocked_on`
   (M1-first). Say which juncture/milestone it advances and rough size (e.g. "WR sweeps —
   small, unblocks juncture 5").
2. **The in-progress thread nearest completion** — continue momentum.
3. **A Jordan decision sitting** — offer whenever ≥2 T0 forks are open (ruling them
   unblocks more than any single increment; say what each unblocks).
4. **Monthly reconcile** — only if `as_of.date` is >30 days old or the last reconcile in
   `CURRENT.md` is (workplan v6 §6 checklist).

Options must be concrete ("PC R3 U0 units-honesty", not "work on combat"). "Other" is
provided by the tool automatically — do not add a catch-all.

## Workflow C — "Record progress" (session close, or "update the board")

For each juncture/stage the session's landed work touched: update `state` (a juncture is
`done` only when its v6 §1 legibility bar is met — the three questions answerable from the
screen — not when its first PR merges), refresh `next` to the new next increment, append
`evidence` (PR/ED/sha), clear or set `blocked_on` from the ledger. Append ONE
`last_progress` line (date: what landed, PR/ED). Keep `last_progress` to ~10 entries
(drop oldest). Bump `as_of`. Commit `[editorial]`. The Stop hook nudges this when
`designs/`/`handoffs/` changed but the board didn't.

## Honesty rules

- Never mark `done` optimistically; evidence is required and cited.
- The board never grows narrative — one `next` line per row; detail belongs in handoffs.
- Do not duplicate a status that lives elsewhere; point at it (`evidence`, `blocked_on`).
- If board and handoff disagree, the handoff wins — fix the board, note the correction.
