# HANDOFF — what is pending, in dependency order

## Status: **PROPOSED. Nothing here is ratified.** Written 2026-09-03, at the end of the session that
## rewrote #358 to rev. 2, conditioned #357 against it, and evaluated #359 against both.
## ⚠ **UPDATED 2026-09-03 (rev. 3)** — the evaluation's §6A change list is now APPLIED. Read
## `README.md`'s rev. 3 banner for what landed; PART 1 and PART 2 below are re-cut against it.
## ⚠⚠ **UPDATED 2026-09-04 — §2's backlog is now MEASURED rather than argued. See PART 2A.**

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

⚠ *(This read SIX and listed `1f`, which is prose in #358 and has nothing for `shape.py` to enforce. Closed and struck 2026-09-03, leaving five. `1g` was then ADDED 2026-09-04, so the count is six again and the heading is right by accident — recorded rather than silently re-adjusted, because "the five below" stood over six rows for one commit.)*

`proposals/2026-09-01-season-loop-tests/tracer/shape.py`

| # | change | done when |
|---|---|---|
| 1a | **the gate asserts `subject == actor` on every Tenure write**, admitting only the three declared exceptions (`T-n` matured term · `T-o` seat revocation **with `Act.via` present** · a destroy cascade citing its own existence change) | a planted non-owner write of `Tenure.until` raises; `revoke` with no `via` raises; `revoke` with `via` passes |
| 1b | **the gate refuses a receipt with `before == after`** | a planted no-op write raises. ⚠ **Run `work` first** — this is `ID-9`'s own measured instance and it may already be live |
| 1c | **the three fabricated Event kinds** — `act.ineligible`, `act.refused`, `contest.resolved` are body literals at **`shape.py` `:4411`, `:4428`, `:4485`, `:4668`** (four SITES, three kinds — `act.refused` is emitted twice). Give each a declared column. ⚠ *These four numbers read `:4107`, `:4124`, `:4167`, `:4331` until 2026-09-04 and every one of them was wrong — `:4107` is MATTER rung accounting, `:4124` a `stores` lambda, `:4167` and `:4331` comments. Found by the same critic pass that corrected row `1g`'s count, one row below; the producer fixed 1g and did not sweep this row.* | the derived kind roster covers every kind the fold can emit; no literal remains |
| 1d | **invariant 4 widened in code** — every failable eligibility alternative needs a refusal kind | `destroy_record` (which declines on both alternatives) emits a declared refusal instead of a literal |
| 1g | ⚠ **THE APPEND-SIDE INTEGRITY CHECK, WHICH IS `ID-9`'S OWN MECHANISM AND HAS NO IMPLEMENTATION.** Stage 4 `§C.2` says *only the gate mints a Receipt* and *the log's append asserts every receipt id is in the gate's minted set for this tick*, so **an Event reporting a write the gate did not apply fails at append**. In the tracer `Event.changes` is a fold-built `StateChange[]` and the log is appended to with a bare `list.append` at **five** sites (`shape.py` 1985, 3973, 4010, 4173, 4852 — this row said `season()`'s alone until 2026-09-04, which reads as a one-line fix and is not); `Event.__post_init__` checks only `causes`. **Nothing refuses a fabricated change**, and the fix is ONE append-side owner every site routes through, not a check bolted to the driver. ⚠ **AND THE FIVE ARE EXHAUSTIVE ONLY WITHIN `shape.py`, WHICH MATTERS BECAUSE THE ACCEPTANCE CRITERION IS ABOUT PLANTING.** The tests and the corpus plant Events from OUTSIDE that file — `corpus_run.py:437` uses `w.log.extend([e1, e2])`, and `probes.py` appends at `:1431`, `:1507`, `:1510`, `:1513`, `:2224`. So an owner that wraps the five in-engine sites would leave every planting path untouched, and one of them is `extend`, not `append`. Whoever builds this decides whether the owner sits on `World` (catching all eleven, and forcing the probes to plant through a declared test seam) or only on the fold; the criterion below is written as if it catches planting, so the first reading is the one it implies. | a planted Event whose `changes[]` names a receipt the gate never minted raises at append |
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

### 2A · ⚠ **THE BACKLOG, MEASURED** (2026-09-04, `proposals/2026-09-04-degree-sweep`)

§2 above was written as an argument from reading. It has now been **executed** against all 143 ARC
and NPC cases, and the result changes the *ordering* rather than the content: **the five rows are
real and none is the bottleneck.** The bottleneck is one row further down, and it is `H-72`.

**THE MEASUREMENT.** Every mechanical decision in the corpus was flipped every way it could be
flipped and each fork followed forward three decisions — **2,403 forks across 89 cases.** All 2,403
changed the act taken *and* the event stream written. **Not one changed any of the next three
decisions**, and the acts diff positionally at the fork index alone. Controls: the world *does*
change; deliberation counts align; the harness re-derives rather than replays.

**THE CAUSE.** `Query.opening_set` has four clauses and **none consults world state** — that is
`§F1`'s deliberate epistemic design. The single channel from consequence to decision is a claim in
the actor's ledger, and **that channel is closed by a type mismatch**: `belief_contradicts` fires
only on `predicate ∈ PERSON_PREDICATES ∧ value is False`, and over 4,800 measured claims the two
predicate vocabularies are **disjoint** and **zero** claims are falsy. A refusal is deposited as
`predicate=travel.blocked value=True`.

⚠ **`opening_set`'s own docstring describes this loop as working** — *"a person who wrongly
believes the granary full still forms the Candidate, acts, and gets `transfer.refused` from the
fold. That is T3 and L2 working."* The fold **does** deposit that refusal. Nothing can read it.
**The design's own worked example is one type mismatch from running.**

**WHAT THIS DOES TO THE ORDERING.** `H-72` / `F.24` / `H-94` — typing `requires` so a belief can
reach a decision — moves **ahead of all five** of §2's rows, because a discovery model, a degree
ladder or a `release` verb that cannot reach a later decision is a better-labelled log line. §2's
rows are then worth building in their own order.

| | |
|---|---|
| **new rows in `hole_register.yaml`** | `H-113` `emits_at` has zero callers, so every degree emits the union and `Untouched` announces `person.died` · `H-114` `_eff_kill` is degree-blind and defaults harm to the whole body, so `Wounded` deletes the person · `H-115` the four degree branches raise `SystemExit`, escaping `run_case`'s handlers · **`H-116` the severed edge, above** · `H-117` the act budget never binds, so `§26.3`'s triage never happens · `H-118` `content_hash` reads the log, not the world · `H-119` the seam's two degree surfaces contradict on ~5% · `H-120` 3 of 4 declared prizes are claimed by no verb |
| **corpus demand, for prioritising** | 972 `season_requires` rows, 427 `core`. Blocked families by cases wanting them: belief/knowledge **58**, roll/contest **51**, investigation **37**, social/speech **31**, third-party-substitute **22**, degree/partial **19**. **113 of 143 cases (79%) touch at least one.** |
| **what the two lanes want** | NPC leans *interiority* (relationship 46%, belief 41%, observability 37%); ARC leans *machinery* (accumulator 53%, threshold 48%, roll/contest 43%). Both ~79% blocked, by different routes. |
| **the design's own bar** | the v30 counterfactual corpus branches by *"alternate degree"* in **7 of 11** scenarios — **64% of its own way of making an alternative future is unreachable.** |

⚠ **One finding indicts a habit rather than a row.** #362 applied `ID-13` — *a declared field
reaching no reader is one that does not exist* — to delete `Tenure.conferrer`, and did **not** apply
it to `emits_by_degree`, which the same revision added. `H-113` is that field. **Apply `ID-13` to
what a revision ADDS, not only to what it inherits.**

### 3 · Open questions — ⚠ **these need Jordan, and only these**

| | |
|---|---|
| **H-98's remainder** | The felled/unresolved split is ruled and implemented. **The engine does not separate a decisive win from a narrow one** beyond wound count on the victor, so a fourth band has no source in the data. Either that distinction is not wanted, or `systems/combat/` must expose it |
| **`levy`'s remit** | `levy` is not in `remit_acts`; W3 substituted `remit:issue` silently and it is now declared. Either `levy` is a **seventh remit act**, or `issue` is genuinely what a levy exercises |
| **`scale:` on ten verb rows** | Fails rev. 2's invariant 10. rev. 2's answer is `Act.via.scope`. The keys are **not deleted** because they answer a real question of yours; retire them when `Act.via` carries the scope |

### 4 · Deferred deliberately

- ✅ **`ID-16`'s DECLARED HALF IS BUILT (2026-09-03).** `hole_register.yaml` carries a `LOOP` row kind and an optional `sign: +|-` column, and **`register.py`'s `G13` validates its shape** — a LOOP row must carry a sign, a non-LOOP row must not, and an amplifying loop must name what bounds it. Mutation-checked 3 of 3. ⚠ **`G13` VALIDATES THE SHAPE; IT DOES NOT MAKE THE COLUMN A MECHANISM** — no resolver reads `sign`, and deleting it leaves the season loop byte-identical, which is `§0.05`'s test. Corrected 2026-09-04; the first wording claimed the stronger thing. Six rows now: `H-102` propagation (`+`), `H-112` WITNESS re-witnessing its own emissions (`+`, found by audit, bounded by one `if` in `World.write`), `H-103` decay (`-`), `H-104` eviction (`-`), `H-105` site condition (re-filed PRODUCER — a severed loop is not a loop), and `H-106`, which says the enumeration is **not complete**. ⚠ **THE DERIVED HALF IS STILL BLOCKED, AND ITS DEFINITION WAS ALSO WRONG**: stated as `writes` × verb `requires` it excludes all four declared loops, because the WRITE edge on each belongs to a STEP rather than a verb (`tell` does have a precondition on the propagation cycle — the first writing of this said it did not, and a critic overturned that). The graph is *what is written* × *every typed reader*. `H-106` is the row. **A table of loops in a markdown file would still be reference.**
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
