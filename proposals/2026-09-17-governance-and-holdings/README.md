# Governance at every rung, and the built world

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Lane: `IN` (cross-cutting), with `SE` for `02`. Ids: **`ED-IN-0231`**, **`ED-IN-0232`**, **`ED-SE-0052`**.
## Grade under `CLAUDE.md` §0.2: **`paper`** for every document. Nothing here executes. `04` names what would move it.

---

> Jordan, 2026-09-17: *"I do not want this work to be constrained by existing work. I want the best
> possible design ideas and concepts, and we can modify code accordingly."* · *"Your remit is to
> develop the most NERS-positive work possible."* · *"a player whose character can govern a settlement
> would like to be able to explicitly set policies or advance a project to build something."* ·
> *"Policies aren't just a number added to a roll, but a way to change or impact how a governed rung
> functions."* · *"a change to how a rung functions will likely have impacts on rungs below it. A
> provincial policy on farming taxation may end up impacting a hearth, you know?"*

## What this is

Four documents on two subjects investigated together, because they turn out to be one mechanism seen
from two sides: **governance and management at each rung of the containment ladder, hearth → realm**,
and **the relationship between settlements and their buildings, infrastructure and fortifications, as
the expression of factions and the contents of their holdings.**

| | | lane · id |
|---|---|---|
| **`01_SEATS_AND_POLICY.md`** | the seat, the policy instrument, the cascade down and the response up | `IN` · `ED-IN-0231` |
| **`02_THE_BUILT_WORLD.md`** | fabric, address, the five site families, fortification, holdings, the works lifecycle | `SE` · `ED-SE-0052` |
| **`03_THE_SURFACE.md`** | what the player sees, touches, is asked, and comes to believe | `IN` · `ED-IN-0232` |
| **`04_BUILD_ORDER.md`** | the sequence, the pre-flight, the rulings closed and surviving | `IN` · `ED-IN-0232` |

## ⚠ The standing instructions, and they are the point of this file

1. **NOTHING HERE RATIFIES ON MERGE.** `ED-1094`'s default is suspended for this directory, loudly and
   on purpose. Merging adopts no design, flips no `## Status:` line, and moves no `CURRENT.md` head.
   A reader who wants to know what is canonical should read `CURRENT.md`, not this.
2. **`ED-SE-0051` STAYS OPEN.** `02` *recommends* its capacity arm. It does not close it, and no row
   here may be cited as having closed it.
3. **`ED-IN-0231` carries one `needs_jordan: true` fork** — whether a nearer rung's clause or a higher
   rank wins a policy collision. Nine other candidate requests were **closed with citations** rather
   than escalated, per `CLAUDE.md` §0's five-step gate; `04` §C.5 lists each closure so nobody re-asks
   it. Clearing a stale question is session work, not conservatism.
4. **The spine is a CONFORMANCE DIVISION, not a design claim.** Most of the seat model is **already
   ratified Layer 1 and merely unbuilt** — `architecture/meta/04_CODE_ARCHITECTURE.md` §B.7 ships
   `Seat`, states that no `is_title` branch exists anywhere, rules `establishment` a Query over
   `oblige` and rejects the field form, deletes `judging_set_rule` from `Rung`, and carries the
   MECHANICAL invariant that *purview is asked of the seat exercised, not the actor*, through
   `Act.via`. Each document separates **conformance** from **extension** from **departure**. Do not
   read an extension as ratified, and do not credit a conformance item as new design.
5. **Corrections are struck and kept in place, never deleted.** Four read-only antagonist passes
   overturned real work here — a policy carrier built on a deleted field, a grant placed on a field
   ratified Layer 1 retires, an unsound licensing argument, and two "free cuts" that were breakages.
   Each is marked where it stood. A document that hid its corrections would be less useful, not more.
6. **Cite `04_CODE_ARCHITECTURE.md` as `§Letter.Number`, never as `04:NNN`.** Its line numbers have
   drifted twice. The same caution applies to every citation in these files: **open it before you
   rely on it.** Citation drift was the single most common defect found in the work behind this suite.

## The measurement block — run these rather than trusting a number here

Per `CLAUDE.md` §0.2 a juncture is done only when the behaviour executes, and per §0.1 pt 4 a number
without a control is not a measurement. Every figure below was taken on 2026-09-17 and **carries the
command that reproduces it**. None of it is cached for citation; re-run before planning against it.

| measured | command |
|---|---|
| `met 1 · not_met 4 · partial 4`; **`R-04 not_met`** — *"the loop runs at person, settlement and realm only"* | `python -m engine.season.harness.register --requirements` |
| the rung census `{realm 1, duchy 3, territory 17, settlement 37, community 60, hearth 211, person 46}`, `province 0` (a province is a Query) | `python -m engine.season.harness.populated 2` |
| **37 settlements hold 4,810 units of matter after one season and 211 hearths hold none** — every site hangs from a settlement, every person lives in a hearth | as above, reading `Rung.stores` by kind |
| `NOT MET`, failing on row 4 — the **doc-derived** board row, which §0.2 calls bookkeeping rather than evidence | `python tools/m1_acceptance.py --summary` |
| `0` citation-integrity violations | `python tools/validate_ed_citations.py` |

⚠ **The `§0.4` close gate — `python -m pytest tests/valoria -q -n auto` — was NOT RUN for the commits
that landed this directory.** The sandbox denied pytest partway through the session. This is stated
rather than implied, per §0's requirement that a skipped step be said aloud; CI is the authoritative
tier and runs it. Do not read the absence of a failure here as a pass.

## How it was made

Seventeen collation agents over `research/`, `proposals/` and `engine/season/` plus `architecture/` and
the settlements/factions canon; three Opus design passes; one Opus engine-fit pass that derived the
loaders' refusal set **empirically, by planting each defect**; four structurally read-only antagonist
passes (`.claude/agents/valoria-critic.md` — no write tools, so the independence is structural rather
than declared); and a read-only Fable reconciliation that adjudicated the disagreements, divided
conformance from extension, and closed nine ruling requests. The evidence base and the adjudications
are not in this directory — they were working material, and `CLAUDE.md` §0 forbids an adversarial pass
from minting documents. What survived is here.
