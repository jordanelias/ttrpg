# 03 · SINGLE OWNERSHIP — every value in the game, in exactly one row

## Status: PROPOSED (2026-08-31). **HELD BACK. Nothing here ratifies on merge.**
## Layer: **L2.** This is Law 3 of `01_THROUGHLINE.md` made exhaustive. Its test is mechanical:
## **name any value in the game and this document says who owns it, or this document is incomplete.**

---

## §1 · THE TABLE — four owners, one log, and Nobody

| owner | owns | never owns |
|---|---|---|
| **Person** | everything interior — `marks`, `capability`, `stance`, **`convictions` and `beliefs` (the moral layer)**, the claim ledger (**what they hold true**); **every Tenure whose subject they are**; the Propositions they utter | anything about another person; any aggregate |
| **Rung** | `matter` (`stores`, the Sites beneath it, the Records kept there, the transmission pointer), `dates[]`, `envelope`, `stake[]`, `judging_set_rule` | **any social aggregate** — no norms, densities, reputation, legitimacy, unrest, cohesion |
| **Office** | `post`, `remit`, `conferral`, `revocation`, `establishment[]`, `dates[]`, `upkeep` | **who holds it** — that is a `hold` Tenure, owned by the holder |
| **Site** | `condition`, `drawers[]`, `kind` | anything social |
| **the log** | itself, append-only | nothing else; it is written by RESOLVE and MATTER and read by everyone |
| **params** | **every exported constant** — `COND_SCALE`, `wear` per site kind, `OB_MIN`, the band coefficients, `L`, `K`'s terms. Owned by the typed artifact and read by code; **never in prose and never in two files** (`11_PARAMS.md`) | anything that varies per instance |
| **the holder of a date** | **its `ConveningCondition`s** — a Rung or an Office owns the conditions attached to the dates it holds | — |
| **Nobody** | **every aggregate**: faction, leaders, presence, density, footprint, norm, scale, reputation, needs, openings, entrenchment, coarse condition, sovereignty | — these are Queries, recomputed, **stored nowhere** |

**Six owners, one log, and Nobody. Every value in the game is in exactly one row.**

> ⚠ **The `params` and `ConveningCondition` rows were ADDED by the adversarial pass, and their absence
> was a real hole rather than an omission of detail.** Twenty-five exported constants had no owner in a
> table whose own test is *name any value and this says who owns it* — including `wear`, which `05` §2
> calls the quantity the whole political layer exists to argue about. And `ConveningCondition` is a
> six-field object with **two mechanisms depending on it** — the threat layer, and hostage politics —
> that had no owner, no write class and no N-line anywhere in the suite.

### §1.1 The Faction row is deleted, and the deletion is an amendment because the row existed

A faction is derivable **in full** from a Proposition plus its `commit` edges. Membership is `commit`;
leadership, presence, density and footprint are Queries; the persistent part is the immutable
Proposition; institutional memory is Records at a Rung.

**Nothing is lost, and one thing is gained:** a faction **collapses when people leave**, with no
dissolution mechanism, because there is nothing left to be the faction.

### §1.2 Every Tenure is owned by its subject, whichever carrier that is

> **One home, one writer, no reach-through. The object side is a derived index, never stored.**

Stating this on the Person row alone leaves `succeed` (a Rung subject) and `hold` (which permits a
Proposition subject) with no owner at all, and the Rung and Office rows silent about Tenures.

**`tie` and `knot` are stored ONCE, on the endpoint with the lower id**, because a shared `strain` on a
directed record otherwise has two homes and **can disagree with itself.**

### §1.3 The gaps — values with no owner, named rather than glossed

**A single-ownership table that quietly omits a value is worse than one that admits the hole.** Six.
[LANE F §G]

| # | value | status |
|---|---|---|
| 1 | **a Proposition after its utterer dies** | Person owns *the Propositions they utter*; **permanence and custody after death are unstated.** The shape's answer, proposed here: a Proposition is immutable and **outlives its utterer unowned** — it is referenced by every `commit` edge and every stance row that names it, and those have owners. **Nothing needs to own it, because nothing may change it.** |
| 2 | **`Record`, `Venue`, `Dispensation`** | implied by Rung-matter and Office; **never stated.** Ruled here: a **Record** is Rung matter; a **Venue** is owned by its `container` when it has one and **by its convening Office when it does not**; a **Dispensation** is owned by its issuing Office |
| 3 | **the object-side Tenure index** | **Nobody, by rule** — but its *maintenance* has no named owner and no measured cost. Ruled here: it is a **barrier-built cache** under Law 3's cache rule, rebuilt at the MATTER barrier and discarded at the next |
| 4 | **a per-issue stance store that already exists in running code** | **two owners today** — a live NPC record carries a stored per-issue opinion with no witness path, and `Person.stance` is the design's home for the same thing. **This is the read/write asymmetry hazard by construction**: the carrier must **absorb** it, not sit beside it |
| 5 | **`season_factor`'s distribution** | no owner, and it **blocks `yield`** |
| 6 | **the cohort's construal spread** | the rule is stated (a distribution, never a value); **the representation is not** |
| ~~7~~ | ~~`ConveningCondition`~~ | **CLOSED by this pass** — owned by its `holder`, the Rung or Office whose date it schedules. It was the seventh gap, found by an adversarial attack on this very table |

---

## §2 · WHY NOBODY OWNS AN AGGREGATE — the argument, once, properly

**Stored aggregates are how a design acquires dead state that reads as mechanism.** A value initialised
once, never written, and cited for seasons as though it meant something.

**Three live instances in this repository, each found by measurement rather than by reading:**

- a settlement's `legitimacy` and `popular_support` — **never read, never written**, and the module
  says so itself;
- a territory's turmoil — **written at exactly one site, read at exactly one site**, connecting nothing;
- a faction's `intel` — **declared in the registry and in the dataclass, and unreachable**: the
  multiplier table has no entry for it, so a write raises.

**If the aggregate is a function it cannot go stale, and it cannot be initialised and then forgotten,
because there is nothing to initialise.**

### §2.1 The cost of the rule, priced rather than hidden

**Every one of these is O(N²) naive, and each has a linear form.** The rule is right; **the cost is the
price of the rule, and a design that states the rule without the cost has not finished.**

| operation | naive cost | the linear form |
|---|---|---|
| **de-individuation** (*"no other ledger names them"*) | N persons x N ledgers x L claims — **200·N² comparisons a season** | **one integer per person**, incremented at deposit, decremented at eviction. WITNESS already visits both |
| `presence` · `density` · `footprint` | a scan of every `commit` edge per call | one pass at the MATTER barrier building `(proposition, rung) -> count` |
| `judging_set(c)` | a scan of addresses per call, **and it is called per sitting and per norm** | barrier-built index |
| `draw_share` · `share` | a scan of a Site's drawers per act | barrier-built denominators |
| WITNESS fan-out | events x persons | the presence index above |
| coarse `condition` at a rung | a tree recursion per call | memoized at the barrier, **with a visited set** — the graph is cyclic by construction |

> **Fix those six and the loop is linear in individuated persons and linear in events. Leave them and
> the population ceiling is set by CENSUS's scan rather than by anything the designer chose.**

---

## §3 · THE FOUR WRITE CLASSES — ownership in time

Ownership says *who* may write a value. The write class says *when*. **Both are needed: a single owner
writing at the wrong barrier is still a defect**, and it is the one that produces off-by-one-tick bugs
nobody can see.

**`CALENDAR · MATTER · ACTS · INTERIOR`** — the full matrix is `04_THE_SEASON_LOOP.md` §4.

> **A WRITE CLASS IS NOT A PHASE.** One class may be written in two phases; the running barrier already
> does this by ratified design. **What is forbidden is a write outside its class**, not a class
> appearing twice.

**Make the write class a PARAMETER of the store API.** Then *"no write outside the matrix"* is
**mechanical** rather than conventional, which is the difference between an invariant and a hope.

---

## §4 · THE READ/WRITE ASYMMETRY HAZARD — the guard this shape licenses

> **The hazard is not "change". It is read/write asymmetry.** When a getter starts computing from a new
> source while setters still write the old one, **every writer silently becomes a no-op.**

Before measuring anything about such a change, **grep the field's ASSIGNMENTS — not its readers, which
are unbounded and mostly harmless** — and ship a guard that fails on a **new bare assignment.**

**This shape licenses exactly one guard of this class, and names why it qualifies:** any state that
migrates from a stat-bag field to a carrier-owned value inherits the **write-sweep** pattern, because
the artifact is load-bearing on **the game**. A guard whose subject is this repository's process is
forbidden, and the difference is the predicate, not the technique.

---

## §5 · THE MIGRATION THIS TABLE IMPLIES, PRICED

**This is the largest cost in the whole suite and it is stated in full rather than deferred.**

The running tree ships a faction stat-bag — six stored floats plus stored standing, territories and
per-arc flags — **written at 31 non-test sites, 20 of which write one field.** [LANE D, counted
independently]

**And the fact that matters more than the count: 30 of the 31 bypass the event log entirely.** Only one
write path is Key-mediated. **So *"all state change flows through the event channel"* is false of the
executing tree**, and any plan written as though it were true is planning against a repository that does
not exist.

| what | this shape's answer |
|---|---|
| **is the stat-bag the base to refactor?** | **no** — it is the shape Law 3 forbids |
| **is it deleted on a Tuesday?** | **no** — adopting the table day-one invalidates the entire executing game at once, **unattributably**, which is the exact failure `CLAUDE.md` §0.1 point 4 forbids |
| **so what happens?** | **build beside, flag-gate, golden-control, cut over** — the repository's own established path, sequenced in `13_EXECUTION.md` |
| **what proves each step?** | flag-OFF **byte-identity including the log hash** as one arm; an n≥100-campaign comparison as the other **where the change is campaign-reachable** |
| **and where it is not campaign-reachable?** | **both arms are identical by construction and running one would be a fake control.** Saying so is part of the discipline |

> **This is the one place where "not bound to precedent" and "do not break the running game" both
> apply, and they do not conflict.** The ideal shape is the destination; the controls are how you get
> there without losing the ability to tell whether you have arrived.

---

## §6 · THE OWNERSHIP TEST

**Name any value. This table says who owns it.** Worked, on the twelve most-cited values in the corpus:

| value | owner | how it is obtained |
|---|---|---|
| where a person is | **Nobody** | `address(p)` — the derived view of their one `contain` Tenure |
| who holds the praefecture | **Nobody** | a Query over `hold` Tenures whose object is that Office |
| a faction's membership | **Nobody** | the `commit` edge set |
| a faction's leader | **Nobody** | `leaders(w, prop, rung)` — **and deposition is this returning somebody else** |
| a settlement's grain | **the Rung** | `matter.stores[grain]` — primary state |
| a harbour's condition | **the Site** | primary state, fixed-point |
| what a person holds true | **that Person** | their ledger; **nobody else may read or write it** |
| what a person holds **right** | **that Person** | their `beliefs` and `convictions` — **a different record from the ledger, moved by argument and consequence, never by evidence** |
| what a person is committed to | **that Person** | the `commit` Tenures whose subject they are |
| whether a village exists | **the Rung**, and only an **act** may end it | `(Rung, exists)` is `social: true` |
| how much authority a governor has | **Nobody** | a Query counting links whose subordinate's ledger **currently asserts** who decides here |
| what a person wants | **Nobody** | `need(p, ·)` rows + `Sensation`, recomputed, stored nowhere |
| what happened | **the log** | append-only, id-unique, referentially checked, content-hashed |
