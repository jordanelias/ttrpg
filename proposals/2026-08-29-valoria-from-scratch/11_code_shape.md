# 11 — The Idealized Code Shape

## Status: PROPOSED (2026-08-29) — adjudication. Nothing here ratifies on merge.
## Method: adjudicated WITHOUT REFERENCE TO ANY EXISTING CODE. No module, signature, registry or
## test in this repository was read, cited, or treated as a constraint. This describes what the code
## SHOULD be, derived from the design, so that it can be compared against what exists by someone
## else, later, deliberately.

**The adjudication in one sentence.** The module hierarchy *is* the containment ladder, the type
system is the throughline enforcement mechanism, and every rule in this document exists because a
design property that would otherwise be a discipline becomes, under it, something the compiler or
the call site refuses to express.

---

## 1. Why the levels are the game's levels

A hierarchy of code artifacts that does not correspond to a hierarchy in the world is a filing
system, and a filing system rots because nothing about the game tells you when a file is in the
wrong drawer. The containment ladder gives the module tree a meaning that is checkable against the
fiction:

```
world/
  rung/person/      rung/hearth/      rung/community/
  rung/settlement/  rung/territory/   rung/province/    rung/realm/
```

**Parent–child in the module tree means containment in the world.** Nothing else may be a parent of
anything. A module named for a concern that is not a place a person can stand is not a rung and does
not go here.

This is what makes the two hardest throughlines structural rather than aspirational:

| architecture property | throughline it discharges |
|---|---|
| inputs distribute downward at increasing granularity | **T6** — the down-stroke IS what the architecture does |
| outputs aggregate upward | **T5** — the up-stroke IS what the architecture does |
| every rung is the same module type at a different level | **T5/T6 at every rung**, and no elite-only mechanism |

A design where propagation *is* the architecture cannot fail Jordan's S criterion by omission. It can
fail only by a rung being missing — which is exactly why Hearth and Community had to be added, and
which is a failure you can see by reading the directory listing.

### 1.1 Alignment is not in the tree

`faction/` sits beside `world/`, never inside it. A faction is a set of persons; it composes *across*
rungs and is a child of none. The moment a faction becomes a node in the containment tree it acquires
a level, and the moment it has a level it cannot grow across one without an authoring act. **The
directory layout is load-bearing on Jordan's A-2 and A-4.**

---

## 2. The three signatures, as types

```
choose  : (Person, View)   -> Act
resolve : (Act,    World)  -> [Event]
witness : (Person, Event)  -> [Claim]
```

These are not conventions. They are the enforcement mechanism for T4, and they work because of what
they *omit*:

- **`choose` has no `World` parameter.** Not a masked world, not a read-only world, not a world
  behind an accessor. There is no world in scope inside any decision function, so omniscience is not
  something a reviewer must catch — it is something an author cannot write. A prior attempt's entire
  belief layer was decoration because its decision functions took the world; the fix is a signature,
  not a feature.
- **`resolve` has no `Person` parameter.** The world does not know who is asking. It receives acts.
  This is what keeps the resolver from acquiring per-actor special cases, which is how scripting
  drift begins.
- **`witness` takes the person FIRST.** It is the only bridge from truth to interior, and it is
  per-person by type. A function that deposits one value into many persons is unspellable: there is
  no signature that accepts a collection of persons and an event. **Consensus broadcast is a type
  error**, which is the structural answer to the failure where one event deposited the same sign and
  magnitude into every witness.

**The rule that keeps this honest:** `View` must be a distinct type from `World`, with no coercion
between them, no shared supertype, and no field of `View` holding a `World`. If a `View` can be
constructed from a `World` by masking, someone will eventually mask nothing.

### 2.1 View is built, not filtered

`View` is assembled from the person's own claim ledger by a bounded query. It is *smaller than* the
truth in the way an empty room is smaller than a furnished one — not blurrier. Absence of a claim
must produce absence in the view, never a widened interval, because a widened interval is
uncertainty and the design needs ignorance.

---

## 3. Ownership: who may write what

| owner | holds |
|---|---|
| **Person** | address, marks, capability, stance, claim ledger, ties. Everything interior. |
| **Container (a rung)** | its stake, its judging set, its standing dates. **Nothing else.** |
| **Faction** | its proposition and its commitment map. |
| **Nobody** | aggregates, norms, densities, needs, openings, scale, reputation |

The last row is the important one. **Every aggregate is a function, never a field.** A norm is the
stances of the members, computed on demand. A faction's density is a roll-up computed on demand. A
person's needs are computed from their situation. An opening is computed from need plus capability
plus terms.

This is not a style preference. Stored aggregates are how a design acquires dead state that reads as
mechanism — a value initialised once, never written, and cited for seasons as though it meant
something. If the aggregate is a function, it cannot go stale, and it cannot be initialised and then
forgotten, because there is nothing to initialise.

**Two module rules follow, and they are the whole of the architecture's discipline:**

- **R-1** A rung module may read its own state and any message addressed to it. It may **not** read a
  sibling's state and may **not** read a descendant's state — it receives aggregates.
- **R-2** A rung module may write only its own state. Upward influence is emitting an aggregate;
  downward influence is emitting a refraction. **No module reaches through another.**

A cross-rung read is the single easiest way to destroy T5 and T6, because once the realm can read a
person directly there is no reason for the ladder to exist, and every intermediate rung quietly
becomes decoration.

---

## 4. One resolver, and what "three fidelities" must mean in code

There is exactly one `resolve`. Played, witnessed and auto are **the same process run with different
amounts of deliberation**, not three functions calibrated to agree. The precedent here is
unambiguous: the only surveyed franchise with two resolution paths is also the only one with a
twenty-year unsolved divergence between them, and the diagnosis is that a played path is a *process*
while a fast path is a *formula* — two different kinds of thing cannot be calibrated to agree, only
made to agree on average.

So the fidelity parameter must control **who is asked to choose**, never **how the outcome is
computed**:

```
played    : the player supplies the Act at each decision point
witnessed : the engine supplies the Act; the player observes the trace
auto      : the engine supplies the Act; no trace is retained
```

Identical `resolve`, identical rolls, identical seeds. If a code path exists that computes an outcome
without running the same resolver, it is a second resolver whatever it is called, and it will diverge.

**The test that matters is a distribution-shape test, not a mean test.** The right question is
whether auto ever produces a result a player who played it out would call *unrecognisable* — so the
comparison harness must compare shapes and tails, and a passing mean is not evidence.

---

## 5. Determinism, seeding, and replay

The engine resolves everything and must run a whole world headless and reproducibly.

- **Per-attempt substreams, derived from stable identity**, not from a shared sequence. The seed for
  an attempt is a hash of (world seed, tick, actor id, attempt discriminator). Consequences: showing
  the player a possibility cannot change what happens; two attempts resolved in a different order
  give the same answers; and adding a person somewhere in the world does not re-phase every other
  roll in it.
- **The order-independence property is the one to guard**, because its absence is invisible. A shared
  stream makes the whole simulation a function of iteration order, and then any change anywhere —
  loading two extra people — silently moves every outcome.
- **Replay is a re-run, not a log.** Given the same seed and the same player inputs, the same world
  results. The log is for the player's benefit and for debugging; it is never the source of truth,
  and nothing may derive behaviour from it.

**A corollary that must be stated because it is easy to violate accidentally:** no decision function
may read the event log. Agents receive claims through `witness`. A module that reads the log has
reintroduced the world into the choosing signature by the back door, and it will not look like a
violation at the call site.

---

## 6. The compute budget is a design mechanism, not an optimisation

Cohorts are persons at coarse fidelity: one record, a weight, evaluated once, applied to all. A
cohort **individuates** — splits into a person and a smaller cohort — when an event names one of its
members, or when its internal stance spread exceeds the bound at which one answer is honest.

This must be one type, not two. If a cohort is a different type from a person, then every mechanism
gets written for one and not the other, and the design acquires an elite-only politics by accident —
which is precisely how a prior attempt ended up with a coalescing path that existed for officers and
did not exist for populations.

**Generation is on demand, never on a clock.** A world that manufactures people on a schedule
accumulates them without bound; the surveyed precedent reached twenty-four thousand characters in
late saves and had to throttle the tail. A person is generated when something needs them to exist,
and is then made consistent with the address, marks and history they must already have had.

---

## 7. What must NOT exist in the codebase

Each of these is refused because it re-enables a failure the design closed structurally.

| forbidden | because |
|---|---|
| a `World` parameter on any decision function | T4 collapses; every belief mechanism becomes decoration |
| a `view_of(world, person)` that masks rather than assembles | someone eventually masks nothing |
| any function taking `[Person]` and one `Event` | consensus broadcast; divergent perspective dies |
| a stored aggregate, norm, density, unrest or reputation field | dead state that reads as mechanism |
| a knowledge value stored on the thing known | knowledge with no knower cannot be planted or refuted |
| a second resolver, an auto-resolve formula, a fast path | guaranteed divergence, unsolved in the genre for twenty years |
| a `tier`, `level` or `scale` field on a faction | growth becomes discontinuous |
| a flat additive modifier from a person onto a roll | worth X/(0.8·√Pool), so it helps weak pools more — backwards |
| a personal effect on a group that is not a fraction of that group | the only concrete anti-leverage rule the precedent corpus supplies |
| a scheduled recovery tick on standing | converts a consequence system into a treadmill |
| a per-entity branch anywhere in the resolver | scripting drift; the exception becomes the mechanism |
| an authored per-person opportunity or quest object | a churning world turns back into content |

---

## 8. What a test proves here

Tests in this design are not coverage. They exist to make a structural claim falsifiable, and each of
the four below fails loudly the moment its property is lost:

1. **No decision function can see the world.** Assert by construction — inspect the signatures — not
   by grepping for a string. A property enforced by naming can be spelled around; a property enforced
   by a type cannot.
2. **Two witnesses of one event can disagree.** Construct two persons with opposed stances and
   different vantages, witness one event, assert the deposited claims differ. If they cannot differ,
   T3 is gone regardless of what the design documents say.
3. **A person with no office can act, petition, and receive an opportunity.** Three assertions, one
   fixture. This is the failure that killed the down-stroke last time, and it is cheap to detect.
4. **Order independence.** Resolve a tick, then resolve the same tick with the actor iteration order
   permuted; assert identical outcomes. This is the guard for §5, and it is the one property whose
   absence is otherwise invisible.

**What must NOT be built:** validators over the design documents, freshness checkers, guards on the
guards, or any apparatus whose subject is the repository's own process rather than the game. A guard
earns its existence only when the thing it protects is load-bearing on the game.

---

## 9. The honest limits of this adjudication

- **It is written without reading the existing code, by instruction.** So it says nothing about how
  far the current tree is from it, and a reconciliation is separate work that someone should do
  deliberately, with the two documents side by side.
- **The N=1 to N=1000+ leverage problem is not solved here** and is not solvable by architecture. §7
  bounds it — fractions rather than flat amounts, option-set changes rather than modifiers — but a
  bound is not a solution, and the surveyed precedent contains no solution either. Claiming otherwise
  would be the worst defect this document could carry.
- **Per-person claim ledgers have a cost that scales with tellings, not with persons.** The bound is
  the view budget K and the salience ranking, and whether that holds at world scale is an empirical
  question this document cannot answer by reasoning.
