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

- **New master-workplan revision:** author it directly in this directory (not a new `designs/audit/`
  folder). Move the previous live version to `deprecated/archives/workplans/`. Update `CURRENT.md` and
  `references/lane_assignments.yaml` source pointers in the same commit. (`references/roadmap_state.yaml`
  was a third pointer until 2026-07-05 — retired to `deprecated/references/` by ED-IN-0006/ED-IN-0009.)
- **Exception — intentionally frozen historical versions:** a major version that's bundled with sibling
  audit artifacts (e.g. v4 in `designs/audit/2026-06-11-orchestration/`, alongside its authoritative
  graph/map docs) can stay in its dated audit folder rather than being physically relocated here, *if*
  `CURRENT.md` explicitly documents it as a frozen record. Don't invent new frozen exceptions casually —
  the default is: the live head lives here.
- **Per-audit-session workplans** (a workplan scoped to one dated audit's findings, e.g.
  `designs/audit/2026-04-30-geography-audit/00_phase2_workplan.md`) are a different thing and stay with
  their audit session — this directory is for the top-level *master* workplan only.
