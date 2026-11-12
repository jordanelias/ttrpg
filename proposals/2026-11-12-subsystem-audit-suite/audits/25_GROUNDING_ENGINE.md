# 25 · Grounding: the suite's claims about the engine, settled at the line

## Status: REFERENCE (a grounding pass over documents that already exist; resolves nothing at runtime, CLAUDE.md §0.05; queues nothing)

## Read at: `870c661` (working tree, 2026-11-12). The suite was written across `54e6661` … `870c661`; no file under `engine/`, `modules/`, `references/` or `architecture/` changed between those (see §0).

Jordan, 2026-11-12: *"All ungrounded information should have info available on repository."* *"Do not
guess."* This file takes the suite's statements about the engine that their own authors marked as not
checked (`[UNVERIFIED]`, `[ASSUMPTION]`, "not opened", "by search only", "inferred", "cited second-hand"),
and the figures several proposals depend on, and settles each by opening the code or data at the cited
place, or by a short read-only probe.

**Statuses.** `VERIFIED` (the opened path:line is given). `VERIFIED-CORRECTED` (true in substance; a
line number, count or wording was wrong and is corrected in the suite text). `REFUTED` (what is true is
given with the opened path:line, and the suite text is corrected). `UNRESOLVABLE` (what would settle it is
named; the suite's mark stays).

**Method.** Each row was settled by `Read`/`grep` of the cited file at the cited line at the SHA above.
Where a behaviour is claimed, a probe was run with `PYTHONHASHSEED=0` at one seed; outputs are under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/GROUND_ENGINE/`
(called `runs/GROUND_ENGINE/` below). No pytest was run and no long aperture run. Other lanes' saved run
outputs (`runs/<LANE>/`) are cited as *their* evidence and say so; a figure this lane did not reproduce is
marked "as recorded, not re-run".

**What this file does not do.** It does not grade a design, and it does not re-audit a fix. A claim about
history, a game precedent or research is another grounding lane's subject and is not listed.

**Edits made to other suite files** are listed in §9; each edited file carries a `Grounded:` line at its
head. No finding of another lane was deleted.

