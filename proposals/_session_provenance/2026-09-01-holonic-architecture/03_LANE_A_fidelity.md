# Lane A — chain fidelity and factuality

**Model:** Fable 5.1 · **Agent:** `valoria-critic` (Read/Grep/Glob only) · **Grep and Glob worked; no
fallback needed.**

## Verdict (lane's own words, condensed)

The proposal's quotations from the head suite are, in the main, verbatim and correctly placed. The
four hand-verified census items reproduce exactly, and **of the twenty-one further census items
opened, none is a strict false positive.** What fails is at the edges, and some edges matter: the
census miscounts itself; item 22 quotes a figure that exists nowhere on disk; the §4 quotation is
spliced from two out-of-chain sources; **an in-chain Jordan ruling is missed everywhere**; §4.1's
"nothing in MATTER crosses a rung boundary" is contradicted by the head's own §4.5; and the scope cut
applied loudly to R-2 is silently not applied to three adoptions grounded the same way.

## Findings that changed the proposal

| # | claim | what is wrong | severity |
|---|---|---|---|
| **F1** | "24 items"; "twenty unverified" | **27 items are enumerated; every integer 1–27 present once.** 23 unverified, not 20 | high |
| **F2** | item 22: *"eleven of twelve work"* | **The phrase appears nowhere in the repo.** The source says the opposite: *"Recomputed rather than adjusted: **FIVE OF TWELVE WORK TODAY**"* | high |
| **F3** | §4's *"the chain already wrote it down"* quotation | **Zero hits in any #337–#352 directory.** A splice of root `HANDOFF.md` and an `FA` ledger row, both 2026-08-27. **Under the proposal's own §0 that is not the chain** | medium |
| **F4** | item 24 marked ⚖ (pre-#337); *"the head's own unpriced reversal… Jordan's call"* | **`02_SCENE_BUDGET_RULING.md` is part of #351:** *"JORDAN RULING, 2026-08-31 — **THE ACT BUDGET IS ~5, NOT 1**"*, verbatim. **Marking its subject pre-#337 is the inverse scope error.** The scene≠act hedge is genuinely open, so "which way it goes" survives narrowly. **The proposal never cites this file** | medium-high |
| **F5** | R-1/R-2 *"never appear again"* | R-1 appears three more times and **is applied in CALENDAR**: *"a convening predicate may read only the holder's own state, **an R-1 compute-on-demand aggregate over its descendants**, or the calendar"*. **The *no owner* claim survives; the sentence carrying it does not** | medium |
| **F6** | R-1/R-2 called "in the head" | The head is #351's `04_UNIFIED_SHAPE.md`, which **contains no R-1/R-2 text** — it carries L3 by reference. **The rules are in the head BY REFERENCE**, which is the sweep-strength status the census itself warns about | medium |
| **F7** | *"Nothing in MATTER crosses a rung boundary, so the partition is free"* | The head: *"**MATTER touches persons**, not only places: subsistence drawn from `stores`"* — a person-rung drawing from its containing rung's matter. Plus travel legs and death's `until` on objects at other rungs. **The proposal's own §8 falsifier fires on the head's text.** The two-step conclusion may survive as a read-side carve-out; **"free" is false as written** | medium-high |
| **F9** | §0: R-2's ground is *"it runs default-on"*, and that ground is cut | **Execution is ONE CLAUSE of a compound ground.** The re-derivation (two logs cannot share `causes[]`) **is invariant 3**, which the chain says is *"copied from the executing substrate, not re-derived."* **The cut is cosmetic** | low-medium |
| **F10** | the scope was cut *"cleanly"*; *"the one place"* | **Three more adoptions rest on the same kind of ground and are not cut** — incumbent B's transport (*"the seven exporters that already gate CI"*), the seam's *"executing precedent"*, and boot-time registry rows (*"proven on both sides"*). Each also has a design argument, so no conclusion falls; **"one place" is false** | low-medium |
| **F13** | item 2 typed *contradicted-silently* | The same section **withdraws it loudly**: *"A MECHANICAL CONSEQUENCE THIS RULING ORIGINALLY CARRIED IS WITHDRAWN… It is deleted."* **Stale text, not a drop. Item real; type wrong** | low |
| **F14** | *"Fourteen of the twenty-four"* | No reading of the type column yields 14 of 24; the honest range is 16–18 of 27 | low-medium |
| **F16** | C1 says the canonicalized act array *survives* a split; §4.1 says a per-container fold has no order | **Internal tension between two rows of the same document.** The sort survives per container; the global order does not | low |

**Mechanical re-citations (F11a–f):** the *"114-line regex router"* is `01_FORWARD_DOCTRINE.md` §3, not
`00_AUDIT.md` D-2; *"grep-backed with `file:line`"* in full is `00_AUDIT.md` §6 item 4, not the forward
doctrine's §4; the *"its own HEAD"* quote is a file, not a PR body, and dropped a word; D-20's verbatim
text is `workings/prbody.md`, not the archive-recovery file; the `grade` vocabulary is three values
plus a coinage, not a citation; *"advance the season counter"* appears **once**, not twice.

**F12 · UNVERIFIED and left so.** Neither #338's nor #343's PR body is on disk. *"The honest
disposition is UNVERIFIED, and reporting them as false would be the exact failure this lane is warned
against."*

## Corrections it would NOT make

- **Not strike item 2** despite F13 — *"a rejected true item is worse than a mis-typed one."*
- **Not re-derive C3's one-log claim without invariant 3** to make the §0 cut real: *"the
  re-derivation would be fake (the argument IS the invariant)"* — say so in a sentence instead.
- **Not chase the two PR bodies.**
- **Not restate "fourteen" precisely** — *"the type column is itself sweep-strength; a re-derived ratio
  would be a second uncontrolled number. Delete it."*
- **Not add a citation to rescue "twice"** — it is out of scope; delete the word.
- **Not overturn item 17's ⚖** — it cannot be settled from disk; *"upholding as 'consistent,
  unconfirmed' is the correct strength."*

## Disposition in this session

**F1, F2, F3, F4, F13, F14, F12 → applied to the census** (`03` §8 rows 1, 2, 6, 4, 5, 7, 10).
**F5, F6, F7, F9, F10 → applied to `ARCHITECTURE.md`** — §4 no longer says "never appear again"; §0.1
carries three qualifications instead of one clean cut; §31 replaces the MATTER claim; §19.5 marks the
one-log derivation's circularity honestly.
**F4 verified by hand before use** — the ruling file reads `THE ACT BUDGET IS ~5, NOT 1`.
