# workplans/ — the one live home for the master workplan

**Rule:** the current master workplan lives here, under a version-suffixed filename
(`valoria_master_workplan_vN.md`). `CURRENT.md`'s "Master workplan" row always names the exact
file — trust that row over guessing from this directory alone, since a stale copy can briefly
coexist during a handoff.

## Why this exists

Before 2026-07-01, this directory held two already-superseded files (`valoria_workplan_v3_consolidated.md`,
`wave1_workplans.md`) while every subsequent master-workplan revision (v4, v5, ...) got authored in a
fresh one-off `designs/audit/<date>-<slug>/` folder instead. `CURRENT.md` had to be hand-updated to
point at wherever the latest one landed, with no stable directory to check first — that's how workplans
kept getting lost. See `HANDOFF.md` 2026-07-01 entry for the cleanup that fixed this.

## Convention going forward

- **New master-workplan revision:** author it directly in this directory (not a new `audit/`
  folder). Move the previous live version to `deprecated/archives/workplans/`. Update `CURRENT.md` and
  `references/lane_assignments.yaml` source pointers in the same commit. (`references/roadmap_state.yaml`
  was a third pointer until 2026-07-05 — retired to `deprecated/references/` by ED-IN-0006/ED-IN-0009.)
- **Exception — intentionally frozen historical versions:** a major version that's bundled with sibling
  audit artifacts (e.g. v4 in `audit/2026-06-11-orchestration/`, alongside its authoritative
  graph/map docs) can stay in its dated audit folder rather than being physically relocated here, *if*
  `CURRENT.md` explicitly documents it as a frozen record. Don't invent new frozen exceptions casually —
  the default is: the live head lives here.
- **Per-audit-session workplans** (a plan scoped to one dated audit's findings) stay physically with
  their audit session **and get a pointer file here.** This supersedes the former rule that this
  directory was "for the top-level *master* workplan only."

## Every plan is reachable from this directory (RULED 2026-07-29, Jordan)

**Rule:** *any* plan — workplan, session plan, implementation schedule, execution plan, remediation
plan, roadmap — requires **either direct placement in this directory or a pointer file here.** A plan
buried in `audit/` that nothing in `workplans/` names is invisible to a resuming session and to the
agents that scope work from this directory. That is how workplans kept getting lost before, and the
2026-07-01 cleanup only fixed it for the *master* workplan.

**Pointer file convention:**

- Filename: `POINTER_<date>_<slug>.md`.
- Required fields: `target:` (repo-relative path to the real plan), `lane:`, `ED:`, `liveness:`,
  `scope:` (one paragraph).
- **`liveness:` is explicit, never inferred.** A `## Status:` heading is *not* a liveness signal in
  either direction — measured 2026-07-29 across all 58 plan-shaped files under `audit/`: only 10
  carry the canonical heading and 7 of those 10 are dead, while 3 of the 7 live plans carry one
  reading "PROPOSED". Inference is wrong in both directions.
- Record known-stale upstream text in the pointer (e.g. a HANDOFF bullet that mislabels the plan's
  version) so the pointer does not silently inherit it.
- **Only LIVE plans get pointers.** Pointing agents at a superseded plan is worse than not pointing.
  As of the 2026-07-29 backfill: **9 pointers** — the triage's 7 live, plus this program's own plan (authored after the triage), plus `full_implementation_plan_v1.md`, which the triage misclassified SUPERSEDED and an adversarial pass corrected to LIVE-PARTIAL. Remainder: 13 superseded, 7 complete, 29 historical, 1 unknown.

## Enforcement — the half that is deterministic is guarded

`tools/ci_workplan_pointer_check.py` (ED-IN-0103) checks the mechanically-checkable half: every
`POINTER_*.md` parses, carries all five required fields, names a real lane, claims no target twice,
and — the load-bearing one — **its `target:` resolves on disk.** A pointer to a nonexistent plan is
the same defect class this whole program exists to hunt, so leaving it unguarded inside the
program's own deliverable was not defensible. Mutation-verified: planting a dead target turns it red.

**The other half is deliberately NOT guarded, and this is why.** "Every live plan has a pointer"
needs a liveness oracle, and liveness was measured to be un-inferable (the `## Status:` finding
above). A guard that guessed would be wrong in both directions — flagging live plans as missing and
passing dead ones. That half stays a docket question
(`audit/2026-07-29-centralization-single-owner/01_orchestration_plan_v1.md` §6 row 7). Per
CLAUDE.md §0.1 point 5: ship the guard you can actually write, and say plainly which half you did not.
