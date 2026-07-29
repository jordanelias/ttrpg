# Pointer — Mass Battle "nothing is golden" full implementation plan (MB lane)

**target:** `audit/2026-07-22-mass-battle-stress-test/full_implementation_plan_v1.md`
**lane:** MB · **ED:** none cited in the file; tracked under the MB lane's 2026-07-24 campaign
**liveness:** **LIVE-PARTIAL** — `Status: PROPOSED` (`:3`); `HANDOFF_MB.md:763` heads its section
"2026-07-24 — 'Nothing is golden' campaign … **(IN PROGRESS)**" and names this the
"Full steering doc + 6-phase plan". B1 has landed (`tests/sim/mass_battle/geometry.py:252` carries
`[Fable-audit B1 fix, 2026-07-24]`); the remainder is open.
**scope:** Part-A flips + Part-B fixes + the per-troop damage model, under Jordan's 2026-07-24
directive *"implement all proposals. nothing is golden here."* The byte-exact golden constraint is
**lifted** — goldens become a re-recorded regression snapshot and the honest gauge is the primary
oracle. `HANDOFF_MB.md:783` records a hard coupling: B1+B2+B3+B5 must land as ONE coherent set.

> **Added 2026-07-29 by adversarial review, correcting a triage miss.** The 58-file liveness triage
> classified this SUPERSEDED by `2026-07-26-mass-battle-fable-audit/03_execution_plan.md`. That was
> **wrong**: grepping the 07-26 plan for this plan's Phase-1 items (B1/B2/B3/B5, geometry, col_grid,
> octagon, `_node_pos`) returns only fork-5/G5/A4a hits — none of them. Partial execution makes the
> remainder *more* live, not less. Recorded here rather than silently fixed, per §0.1 point 3.

## Siblings in the same directory — triaged explicitly, not by silence

- `spatial_model_v2_plan.md` — **LIVE.** `Status: PROPOSED`, Jordan-directed 2026-07-22; source of the
  still-unbuilt P-DEC-2/P-DEC-3, cited live at `HANDOFF_MB.md:453,473`. Owned by the MB session.
- `ratified_but_unbuilt_backlog.md` — **LIVE (register, not a plan).** An exhaustive 3-way sweep of
  ratified-but-unbuilt MB items, all HIGH. A worklist the MB session draws from; no pointer of its own
  because it schedules nothing.
