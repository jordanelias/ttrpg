# PR #350 vs the 2026-06-28 archive — reading order

## Status: **PROPOSED (2026-08-31). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**

Jordan-directed: interrogate `archives/audit/` and `designs/` at tag `v30-snapshot-2026-06-28`, insofar
as they concern **NPCs, the world, factions, settlements and governance**, and determine whether the
idealized code shape proposed in PR #350 (`proposals/2026-08-31-unified-code-shape/`) is missing
anything that still provides value.

**The standard, ruled by Jordan mid-session:** *"It doesn't matter if anything was already built — it
only matters if it was built extremely well. We are reviewing all prior work only to identify the best
ideas possible."* Every finding here is judged on merit; `## Status: CANONICAL` and Jordan
ratifications are treated as evidence about quality, never as a substitute for it. §5 of the findings
rejects canonical and ratified archive material on those grounds, and §4 names PR #350's own best ideas.

| file | what it is |
|---|---|
| **`00_FINDINGS.md`** | **the deliverable.** The best ideas found, ranked on merit; what PR #350 is missing; what it already does excellently; what the archive got wrong; and what to adopt, correct or escalate |
| `01_CONVERGENCE.md` | the eleven cross-lane convergences, each marked for whether the agreement is real independence or one ruling propagating |
| `02_SCENE_BUDGET_RULING.md` | Jordan's ~5-scenes ruling of 2026-08-31, what it overturns in PR #350, and the canonical prior art the suite never read |
| `evidence/LANE_A..L.md` | the twelve archive-scrape reports, blind to PR #350 by instruction |
| `evidence/COMPARE_1..3.md` | the three read-only comparative analyses |

**Read `00_FINDINGS.md`.** The rest is the evidence that makes it falsifiable.

---

## Method, and what it licenses

**Twelve scrape lanes** over disjoint file sets across the whole snapshot (114 archive + 705 design
files) — ~42,000 words, ~200 findings, each carrying `path:line`, the source's own status marker, and a
rediscovery note. Each lane was instructed not to read PR #350, so its findings could not be shaped by
what the proposal happens to contain.

**Three comparative lanes**, read-only **by agent definition** rather than by instruction: the
`valoria-critic` definition carries `Read`, `Grep`, `Glob` and no `Write`, `Edit` or `Bash`, so a lane
cannot write whatever its prompt says. Each was given a different axis (governance/factions/settlements
· NPCs/world/narrative · adversarial cross-cut) and the same disposition test.

**The disposition test.** Not "is it in the archive" but: **COVERED** (PR #350 provides it, possibly
better and under another name) · **SUPERSEDED** (the archive answer is worse and the refusal is argued)
· **MISSING**. Roughly two-thirds of what the lanes surfaced was COVERED or SUPERSEDED, which is the
honest headline about PR #350 and is stated first in the findings for that reason.

**What is deliberately absent.** Material the corpus itself retracted is never reported as a finding —
each lane produced a DEAD ENDS section for exactly this, and the inverted `Legitimacy = Mandate×20`
arrow, faction-level L/PS, the "treated as Ob 4" floor, Niflhel, VTM and the R6 death-spiral drain
locations a grep proved absent from the code appear nowhere.

## Reproducing it

The two trees are readable at the tag without a working-tree change:

```
git archive v30-snapshot-2026-06-28 archives/audit designs | tar -x -C <somewhere>
```

## The honest state

**Nothing here executes**, and it audits a suite that does not execute either — under `CLAUDE.md` §0.2
both are prose. The synthesis verified by hand every claim it builds a conclusion on and says which in
`00_FINDINGS.md` §7; individual lane citations not in that list are advisory. Twelve lanes read the
archive at varying depth, and one covered roughly 20% of a single 1.26M-character file. **This
investigation has not read it all either.**
