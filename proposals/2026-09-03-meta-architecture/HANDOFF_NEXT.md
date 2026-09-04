# HANDOFF — what is pending, in dependency order

## Status: **PROPOSED. Nothing here is ratified.** Written 2026-09-03, at the end of the session that
## rewrote #358 to rev. 2, conditioned #357 against it, and evaluated #359 against both.
## ⚠ **UPDATED 2026-09-03 (rev. 3)** — the evaluation's §6A change list is now APPLIED. Read
## `README.md`'s rev. 3 banner for what landed; PART 1 and PART 2 below are re-cut against it.

**Read `README.md`'s rev. 3 banner first, then `04_CODE_ARCHITECTURE.md`'s rev. 2 banner** — the
first lists what the evaluation's change list moved, the second the twenty findings and where each
landed. This file is only *what is left*, and every item names the file, the change, and the test
that would show it done.

---

## PART 1 · WHAT LANDED THIS SESSION, so nothing is redone

| | |
|---|---|
| **#358 rev. 2** | `AX-3` carve-out · `AX-6` scope clause · `T-o` (a seat may end what its remit reaches) · degree-keyed `writes` **and** `emits` · `ID-16`/`17`/`18` · `§C.11` explanation contract · `§F.24a`'s seven-form `requires` grammar · `§E.1.7` (what an oath owes) · loader invariant 12 · `PART D` rows 1, 5, 10a, 30a, 30b |
| **#358 rev. 3** ⚠ **the evaluation's §6A list, APPLIED** | **ADDED** `§D.0` third admission clause · `§G.2.9` procedure/order criterion · `PART D` `27a` and `41a` · `§E.2.2a` two in-fiction corpses · `§D.9`'s `Claim` word reservation. **CORRECTED** `Tenure.conferrer` deleted · `establishment` is a Query at `§D.6` **and** `§E.2.5` · `T-o` added to `§B.8`'s closing paths · `ID-16`'s *unbuildable* retracted in half · `F.28` amended · `§F.34` given both ungraded items · three stale counts. **REGRADED** `§F.4`'s `ID-15` row — ⚠ **it was first marked survived on a candidate that could not fire it; it is now RUN against both and OPEN.** **PROPAGATED** into Readings 05/07/09 and `00_THE_METHOD.md` |
| **#357 conditioned** | `kill / wound` degree-keyed on **three** bands read from scene combat · `combat_seam.resolve` returns `wound_state` · `shape.py` loader enforces invariant 12 both ways and asserts the two keyed columns agree · `writes_at`/`emits_at` wired into `_fold` · `Date.fired`'s spurious `RES` dropped · five register rows corrected · conditioning headers on three data files |
| **Ruled by Jordan** | *kill/wound degrees are taken from scene combat* — the degree is **read**, never mapped |

---

## PART 2 · PENDING, IN DEPENDENCY ORDER

**Nothing below depends on a ruling except where marked. Items 1–4 are mechanical.**

### 1 · Finish enforcing rev. 2 in `shape.py` — the SIX that are documented and not implemented

⚠ *(This read SIX and listed `1f`, which is prose in #358 and has nothing for `shape.py` to enforce. Closed and struck 2026-09-03; the five below are the code items.)*

`proposals/2026-09-01-season-loop-tests/tracer/shape.py`

| # | change | done when |
|---|---|---|
| 1a | **the gate asserts `subject == actor` on every Tenure write**, admitting only the three declared exceptions (`T-n` matured term · `T-o` seat revocation **with `Act.via` present** · a destroy cascade citing its own existence change) | a planted non-owner write of `Tenure.until` raises; `revoke` with no `via` raises; `revoke` with `via` passes |
| 1b | **the gate refuses a receipt with `before == after`** | a planted no-op write raises. ⚠ **Run `work` first** — this is `ID-9`'s own measured instance and it may already be live |
| 1c | **the three fabricated Event kinds** — `act.ineligible`, `act.refused`, `contest.resolved` are body literals at `:4107`, `:4124`, `:4167`, `:4331`. Give each a declared column | the derived kind roster covers every kind the fold can emit; no literal remains |
| 1d | **invariant 4 widened in code** — every failable eligibility alternative needs a refusal kind | `destroy_record` (which declines on both alternatives) emits a declared refusal instead of a literal |
| 1g | ⚠ **THE APPEND-SIDE INTEGRITY CHECK, WHICH IS `ID-9`'S OWN MECHANISM AND HAS NO IMPLEMENTATION.** Stage 4 `§C.2` says *only the gate mints a Receipt* and *the log's append asserts every receipt id is in the gate's minted set for this tick*, so **an Event reporting a write the gate did not apply fails at append**. In the tracer `Event.changes` is a fold-built `StateChange[]` and `season()` appends with a bare `list.append`; `Event.__post_init__` checks only `causes`. **Nothing refuses a fabricated change.** | a planted Event whose `changes[]` names a receipt the gate never minted raises at append |
| 1e | **`ID-14`'s opener/closer map** as a loader function over `verb_table.yaml` | the map is computed; the four open-only kinds fail the load with their names |
| ~~1f~~ | ✅ **CLOSED (rev. 3) — already done, and it never belonged under this heading.** `ID-18`'s list is `PART D` row **30b**, which PART 1 records as landed in rev. 2, and rev. 3 amends that row to say why the **four open-only relation kinds are NOT on it**: a permanence nobody authored is a defect, not a grant. ⚠ **The closure ground is NOT §0.2** — `ID-18` and row 30b both say the enumeration is *not a loader invariant* (*"a loader cannot see a language-level guarantee"*), so a prose row is the right home and there is nothing for `shape.py` to enforce. **Citing §0.2 here would be done-on-a-document quoting the section that forbids exactly that** | — |

### 2 · The five root causes that block #359's actions — ⚠ **this is the real backlog**

Measured this session: of ~30 distinct actions in #359, **~21 are expressible in #357 and 9 are not.**
The nine collapse to five causes, and four are holes #357 already registers.

| # | cause | blocks | fix |
|---|---|---|---|
| **2a** | **`oblige` has an opener and no closer** | `defect` · `betray` · breaking a treaty · releasing a guarantee — **four of the nine** | the generic `release` verb (#358 `A.3` #14), eligibility `own`, domain `tenure_kinds \ {contain}`. ⚠ **Also fixes a defect neither #358 nor the critique named: `hold` is closable only by `revoke` (remit), so A PERSON CANNOT RESIGN AN OFFICE — a direct `T-m` violation.** ⚠ **SCOPE, CHECKED rev. 3: this is a #357 DATA defect, not a #358 design gap.** #358 already carries the fix — `§A.3` row 14's generic `release` with eligibility `own`, and invariant 6's domain `tenure_kinds \ {contain}`, which reaches `hold`. **The design says a person may resign; the verb table does not let them.** Fix the table, and do not re-open the design |
| **2b** | **`the six investigation acts` is one row with `writes: []`** | `expose` · `Investigate` — discovery is inert | split into six rows with writes; #359's discovery model (a contest of capability against secrecy, emitting a Degree) is the shape, and rev. 2's degree-keyed columns are the home |
| **2c** | **`determine` is `absent`; `judging_set` is `D11` absent** | `vote` — nothing is decided at a sitting | `judging_set` as a Query over seats whose remit covers the matter (#358 `§B.7`) |
| **2d** | **`Rung.exists` and `Site.exists` have ZERO producers** | `incorporation` · building a holding — **`F.20`: the world only decays** | a founding verb writing `Site.exists`; #359's holdings model says what it confers, #358 `§D.3` says a Site gates verbs by band |
| **2e** | **no `bargain`** | the third response at every tier | ⚠ **test composability first** — `utter` a counter-`OUGHT` + `commit` may already express it. Adding a verb is the last resort, not the first |

### 3 · Open questions — ⚠ **these need Jordan, and only these**

| | |
|---|---|
| **H-98's remainder** | The felled/unresolved split is ruled and implemented. **The engine does not separate a decisive win from a narrow one** beyond wound count on the victor, so a fourth band has no source in the data. Either that distinction is not wanted, or `systems/combat/` must expose it |
| **`levy`'s remit** | `levy` is not in `remit_acts`; W3 substituted `remit:issue` silently and it is now declared. Either `levy` is a **seventh remit act**, or `issue` is genuinely what a levy exercises |
| **`scale:` on ten verb rows** | Fails rev. 2's invariant 10. rev. 2's answer is `Act.via.scope`. The keys are **not deleted** because they answer a real question of yours; retire them when `Act.via` carries the scope |

### 4 · Deferred deliberately

- ✅ **`ID-16`'s DECLARED HALF IS BUILT (2026-09-03).** `hole_register.yaml` carries a `LOOP` row kind and an optional `sign: +|-` column, and **`register.py`'s `G13` validates its shape** — a LOOP row must carry a sign, a non-LOOP row must not, and an amplifying loop must name what bounds it. Mutation-checked 3 of 3. ⚠ **`G13` VALIDATES THE SHAPE; IT DOES NOT MAKE THE COLUMN A MECHANISM** — no resolver reads `sign`, and deleting it leaves the season loop byte-identical, which is `§0.05`'s test. Corrected 2026-09-04; the first wording claimed the stronger thing. Six rows now: `H-102` propagation (`+`), `H-112` WITNESS re-witnessing its own emissions (`+`, found by audit, bounded by one `if` in `World.write`), `H-103` decay (`-`), `H-104` eviction (`-`), `H-105` site condition (re-filed PRODUCER — a severed loop is not a loop), and `H-106`, which says the enumeration is **not complete**. ⚠ **THE DERIVED HALF IS STILL BLOCKED, AND ITS DEFINITION WAS ALSO WRONG**: stated as `writes` × verb `requires` it excludes all four declared loops, none of which has a verb precondition on its cycle. The graph is *what is written* × *every typed reader*. `H-106` is the row. **A table of loops in a markdown file would still be reference.**
- **`Rung.dates`** still carries `RES` with no producer. Unlike `Date.fired` this may be a real hole rather than a data error; establish which before editing.

---

## PART 3 · THE TRAP TO AVOID, stated because this session nearly fell in it twice

**Do not invent a mapping where the data already carries the answer.** Twice this session a gap that
looked like a missing design decision was a value being **discarded at an interface**:

- `wrapper.fight` computes the whole outcome and returns `+1/-1/0`. The `WoundTracker` was on objects
  the seam already held. **The degree was never missing; it was thrown away at the return.**
- `write_matrix.yaml` declares `body.changed` for `Person.body`. The verb table emitted `person.died`
  for every band. **The kind was never missing; the column used one value for two outcomes.**

**Before registering a hole, check whether the value exists one field deeper.** Both of these were
graded as design gaps for weeks.
