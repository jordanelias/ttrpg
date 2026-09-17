# Governance at every rung, and the built world

## Status: **PROPOSED (2026-09-17). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Lane: `IN` (cross-cutting), with `SE` for `02`. Ids: **`ED-IN-0231`**, **`ED-IN-0232`**, **`ED-SE-0052`**.
## Grade under `CLAUDE.md` §0.2: **`paper`** for every document. Nothing here executes. `04` names what would move it.
## ⚠ **UNIFIED 2026-09-17.** The four documents were authored in parallel from one plan and had drifted. `00_THE_DESIGN.md` is the unified statement and the entry point; the four were reconciled in place and every correction is **struck and kept**, never deleted.

---

> Jordan, 2026-09-17: *"I do not want this work to be constrained by existing work. I want the best
> possible design ideas and concepts, and we can modify code accordingly."* · *"Your remit is to
> develop the most NERS-positive work possible."* · *"a player whose character can govern a settlement
> would like to be able to explicitly set policies or advance a project to build something."* ·
> *"Policies aren't just a number added to a roll, but a way to change or impact how a governed rung
> functions."* · *"a change to how a rung functions will likely have impacts on rungs below it. A
> provincial policy on farming taxation may end up impacting a hearth, you know?"*

## What this is

**One design on two subjects investigated together, because they turn out to be one mechanism seen
from two sides:** **governance and management at each rung of the containment ladder, hearth → realm**,
and **the relationship between settlements and their buildings, infrastructure and fortifications, as
the expression of factions and the contents of their holdings.**

**Read `00_THE_DESIGN.md` first.** It states the whole design once, in one vocabulary; the four
subject files carry the detail, the measurements and the falsifiers, and `00` points at the file that
owns each.

| | | lane · id |
|---|---|---|
| **`00_THE_DESIGN.md`** | ⭐ **THE ENTRY POINT.** The unified statement: what a seat is, what a policy is, what a built thing is, how the cascade runs, what the player sees, what it costs to build. Introduces **no claim of its own** and shares `01`'s id | `IN` · `ED-IN-0231` |
| **`01_SEATS_AND_POLICY.md`** | the seat, the policy instrument, the cascade down and the response up. Owns **RR-1** and the `works` noun | `IN` · `ED-IN-0231` |
| **`02_THE_BUILT_WORLD.md`** | fabric, address, the five site families, fortification, holdings, the `works` lifecycle. Owns the `hold`-guard argument, the `fort_level`/`facility_tier` withdrawal and the commons `share` reading | `SE` · `ED-SE-0052` |
| **`03_THE_SURFACE.md`** | what the player sees, touches, is asked, and comes to believe. Owns the Surface Law, the read licences and **RR-3** | `IN` · `ED-IN-0232` |
| **`04_BUILD_ORDER.md`** | the sequence, the pre-flight, and **the suite's single ruling ledger** — three surviving requests, thirteen closed | `IN` · `ED-IN-0232` |

## ⚠ The standing instructions, and they are the point of this file

1. **NOTHING HERE RATIFIES ON MERGE.** `ED-1094`'s default is suspended for this directory, loudly and
   on purpose. Merging adopts no design, flips no `## Status:` line, and moves no `CURRENT.md` head.
   A reader who wants to know what is canonical should read `CURRENT.md`, not this.
2. **`ED-SE-0051` STAYS OPEN.** `02` *recommends* its capacity arm. It does not close it, and no row
   here may be cited as having closed it.
3. **THREE ruling requests survive, and `04` §C.4 is the single ledger** (⚠ *corrected 2026-09-17:
   this said "one", `04` said "two" and `03` raised a third under its own heading — three files, three
   counts*):
   **RR-1** (`ED-IN-0231`, `needs_jordan: true`) — does a nearer rung's clause or a higher rank win a
   policy collision? Owned and argued by `01` §C.6.
   **RR-2** (`ED-SE-0051`, already queued) — matter only, or matter plus hearth capacity? `02` §A.7
   recommends the capacity arm and does not close it.
   **RR-3** (`ED-IN-0232`) — adopt `03`'s claim-landing replacement for the thirteen authored zoom
   triggers, or keep the table? Raised by `03` §A.7/§C.3, and marked the **weakest** of the three in
   `04` §C.4 for the reasons `03` itself measures.
   **Thirteen** other candidate requests were **closed with citations** rather than escalated, per
   `CLAUDE.md` §0's five-step gate (⚠ *`01` and `04` each listed a different "nine"; `04` §C.5 now
   carries the union and is the single owner*). Clearing a stale question is session work, not
   conservatism.
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
   **The 2026-09-17 unification pass added its own**, and they are struck the same way: a policy
   described as *a named list of people* where the reach is computed (`03`), a building described as
   *being* a hearth where it stands on one (`03`), an `inferred` producer routed to an unresolvable
   verb (`04`), a `723` figure called `transfer`'s when the tree measures it for `work` (`04`), two
   different sets of "nine closed rulings" (`01` and `04`), and roughly twenty line-number drifts.
   Each is marked where it stood. A document that hid its corrections would be less useful, not more.
6. **CITATION PREFIXES, UNIFIED 2026-09-17, because the old ones collided with this directory's own
   file numbers.** ~~`04 §B.7`~~ and ~~`01:443`~~ read as pointers to `04_BUILD_ORDER.md` and
   `01_SEATS_AND_POLICY.md`, and `04_BUILD_ORDER.md` really does have a `§A.3` of its own. So:
   **`ARCH` = `architecture/meta/04_CODE_ARCHITECTURE.md`** and **`AX` = `architecture/meta/01_AXIOMS.md`**,
   and a bare `01`/`02`/`03`/`04` now always means a file in THIS directory. Cite `ARCH` as
   `§Letter.Number`, never as a line number — its lines have drifted twice; where a section pointer
   still carries a line (`ARCH §B.3:235`), **the section is authoritative and the line is advisory.**
   The same caution applies to every citation in these files: **open it before you rely on it.**
   Citation drift was the single most common defect found in the work behind this suite.

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
| **re-measured for the unification, 2026-09-17** — 38 verb rows · **18 resolvable** · **28 person-side formable** (an `own` alternative) · **13 both** · **10 formable by nobody** (the nine `remit:` rows plus `destroy_record`) · **9 `binding_decision` rows, 2 of them `own`** · **11 `@effect_for` bodies** | `resolvable_verbs()` + `VERB_TABLE` over `engine/season/data/verbs.py` |
| **10 producerless `[RES]` matrix rows** of 40 — `write_matrix.yaml`'s own header says eleven and projects nine and **both are stale** | the reproduce command at `write_matrix.yaml:38-42` |
| **the first band crossing fires at MATTER pass 21** (37 of them, `s_s_001_harbour` `bulk_shipping` 800 → 790). CI runs the populated world 1 season and the corpus ≤ 6, so `w.crossings` is empty in every world any gate executes | drive `matter()` on `build_realm(0)` and read `w.crossings` |

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
conformance from extension, and closed the ruling requests. **Then, 2026-09-17, a unification pass**:
the four had been written in parallel from one plan and had drifted in the way four readings of one
spec always drift — the same term under two names, the same claim graded twice, the same argument made
in two files, two different sets of "nine", and line numbers that had never been re-opened. That pass
re-measured every contested number against the tree, adjudicated the judgment calls on stated ground
(the code over prose, a later ruling over an earlier, the file that opened the source over the file
that did not), struck what it overturned in place, and wrote `00_THE_DESIGN.md`. The evidence base and
the adjudications are not in this directory — they were working material, and `CLAUDE.md` §0 forbids an
adversarial pass from minting documents. What survived is here.
