# META-ARCHITECTURE — STAGE 2 · HIERARCHIES, DEPENDENCIES, NESTS, SCALES

## Status: **PROPOSED (2026-09-03). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Derives from `01_AXIOMS.md`. Sources: the axioms, and the PR chain #337 → #357. **Nothing else.**
## Top-down. **Nothing here runs and nothing here is meant to.**

---

# PART A · WHAT A HIERARCHY IS, AND THE THREE THINGS THE CHAIN CALLS ONE

## §A.1 · The test

> **A hierarchy is a relation you can WALK. If you can only compare two things, you have an
> ORDERING. If you can only ask whether one reaches another, you have a GRAPH.**

`ID-8` said it in one line — *a label cannot be walked* — and every authority question in the design
is a walk: *does this person's warrant reach that place?* is answered by ascending until you hit a
seat, or failing.

**Applying the test separates three things the chain names with one word:**

| | what it is | shape | walkable? |
|---|---|---|---|
| **CONTAINMENT** | a place inside a place | **tree**, single parent | **yes** — this is the only true hierarchy |
| **SUBORDINATION** | a person sworn to a person or a seat | **graph** — cyclic, lateral, spans everything | **traversable**, not walkable: no root, no depth |
| **RANK** | how wide a seat's domain is | **total order** | **no** — there is nothing to walk. It is a comparison |

> ### **THE CONFLATION THIS ENDS**
> The chain asks *"is the Löwenritter under the Crown?"* in the same breath as *"is this hamlet in
> that duchy?"* and *"does a Duke outrank a Count?"* — **three different questions with three
> different shapes, and only the middle one is containment.** Answering the first by walking a tree
> is what made faction nesting look necessary; answering the third by walking anything is what made
> rank look like a second ladder.

## §A.2 · Rank is not a ladder, and needs no storage

**Rank is the ordinal of a seat's domain in the containment roster.** A Duke's domain is a duchy, a
Count's a province, and the roster is already ordered, so the comparison falls out. **Nothing stores
a rank. Nothing needs a second scale.**

⚠ **AND RANK IS NOT HEADCOUNT, WHICH THE ORDINAL GETS RIGHT AND A COUNT WOULD GET WRONG.** A seat
whose domain is a tier that has not been assembled upward may govern several of them, while a
higher-ranked seat governs one. **Rank asks *how wide a kind of thing*, never *how many things*** —
and a design that ranked by holdings would invert the ladder for exactly that case.

## §A.3 · Subordination is a graph, and Stage 1 already decided its carrier

From `01_AXIOMS.md` §E.1.5: **there are no institutional relations, only people's relations read in
aggregate.** A body's subordination is a Query over the sworn edges of whoever is currently seated.

**What follows for this Part, and it is the load-bearing consequence:**

> **THE SUBORDINATION GRAPH HAS NO ROOT AND MUST NEVER BE GIVEN ONE.** A root would be a sovereign
> nobody swore to — an institutional relation by the back door. **The absence of a root is what makes
> a contested realm expressible**: two people each claiming the top, with neither position being a
> node in a tree that could adjudicate between them.

---

# PART B · NESTS — WHAT CONTAINS, AND WHAT MERELY RELATES

## §B.1 · The rule

> ### **ONLY PLACES NEST. EVERYTHING ELSE RELATES.**

**Derived.** Nesting means a parent whose identity constrains the child. `contain` does that: knowing
the duchy bounds what the province can be. Subordination does not — a person sworn to a distant seat
is constrained in *authority*, not in *identity*, and can be sworn to two at once. **A relation that
permits many parents is not a nesting**, and calling it one forces a single-parent rule the fiction
immediately breaks.

| candidate | nests? | why |
|---|---|---|
| place in place | **yes** | single parent, walkable, finite by roster |
| faction under faction | **no** | a person's edges; many at once; spans places freely. ⚠ **But see §B.1.1 — *not a nesting* is not the same as *not a container*** |
| office under office | **no** | same relation, same reason (§A.3) |
| rank under rank | **no** | an ordering has no parent |
| **a contest inside a season** | **YES — and it is the other kind** | §B.2 |

### §B.1.1 · ⚠ A container for READING is not a nesting — added 2026-09-03

Jordan: *"Factions could also be a container for people and holdings."* **Both halves are true and
they are not in tension, because they answer different questions.**

| | |
|---|---|
| **NESTING** — asked of the containment tree | **no.** A person commits to several factions at once, so single-parent fails and *aggregate over my descendants* stops being well-defined |
| **CONTAINER** — asked of what code may hold | **yes**, as a resolved view (Stage 1 §D.11): members, holdings, seats, resolved at a barrier and owning nothing |

> **The stored version is what breaks things, and precisely because it would be a second home.**
> Membership written on the faction disagrees with the `commit` edges the moment either moves. **The
> view is the same data read from the other end**, and it cannot drift because it is not a copy.

**So: `holdings(faction)` and `members(faction)` are NAMED QUERIES** — first-class things to *ask
for*, never things to *own*. `ID-15`.

## §B.2 · The second kind of nesting, and it is PROCESS not PLACE

**A contest is the season loop, nested** — the same steps over a smaller person set on a shorter
clock. That is a genuine nesting and it is not containment: **it nests TIME, not SPACE.**

> **The two kinds have opposite bounding problems, and conflating them loses the argument for both.**
>
> | | place-nesting | process-nesting |
> |---|---|---|
> | bounded by | **the roster** — finite by construction | ⚠ **nothing intrinsic.** A contest can open a contest |
> | needs a depth cap | **no** | **YES, caller-supplied, no default** |
> | what a cycle means | impossible (single parent) | legitimate and must terminate |

⚠ **A DEFAULT DEPTH IS A FABRICATED CONSTANT AND MUST STAY REFUSED.** A number nobody measured gets
cited later as though somebody had. **The cap is the caller's, always** — and exceeding it returns a
typed refusal rather than raising, because a refusal is an outcome the fiction can carry and a crash
is not.

## §B.3 · What a container may do, stated as one contract

Two rules, and they are the whole holonic core:

> **A container reads its own state and any message addressed to it. It may compute an aggregate over
> its descendants ON DEMAND; it may not receive a pushed one, and it may not store one.**
>
> **A container writes only its own state. Upward influence is emitting an aggregate; downward
> influence is emitting a refraction. No container reaches through another.**

**Why the middle of the ladder dies without this:** once the realm can read a person directly, no
intermediate rung has a reason to exist and every one becomes decoration. **The prohibition is not
about coupling — it is what makes the ladder a thing rather than a filing system.**

⚠ **AND THESE TWO RULES GOVERN CONTAINMENT ONLY.** Following a sworn edge, a commitment or a distant
holding **leaves the subtree**, and is therefore a resolver-side question — `World` first, and by
`T-f` unreachable from a person's decision. **That split IS the design**: it is why a person cannot
know their faction's true strength, only what they claim about it.

---

# PART C · SCALES

## §C.1 · Scale is read, never written

> **Scale is a position in the containment tree. It is derived on demand and stored nowhere.**

By `T-a` it could not be stored anyway — a scale is an aggregate over the tree, so nothing owns it.
**But the stronger reason is `ID-8`:** a stored scale is a label, and a label cannot be walked, so
every authority question would need a second mechanism beside it.

## §C.2 · The branching rule, which is the one that gets broken

> ### **BRANCH ON THE ORDINAL OR ON THE RELATION. NEVER ON THE MEMBER.**

`if rung.kind == "duchy"` is scripting drift with a schema's face. `if rank(seat) >= rank(other)` and
`if contains(a, b)` are lawful, **and they stay correct for any roster membership** — which is the
property that makes one type with many kinds worth having at all.

**The falsifier is exact:** *change the roster's membership and see what breaks.* A mechanism that
breaks is branching on a member. **A roster is only data if nothing branches on its members** — which
is what makes `ID-13`'s *declared fields must reach a reader* and this rule the same rule seen from
two ends.

## §C.3 · Scale is not a level of the code hierarchy

**A module is not "a settlement-scale module".** It is registered against a role and runs at whatever
rungs the step hands it.

> **Indexing code by scale deletes the property that makes the ladder worth having**, because a
> mechanism written once for one rung type is automatically available at every rung. **Scale-indexed
> code is scale-divergent code** — and it is invisible until something composes across a boundary,
> which is the worst failure signature available.

---

# PART D · DEPENDENCIES

## §D.1 · Two hierarchies, and they are not the same tree

| | the WORLD hierarchy | the CODE hierarchy |
|---|---|---|
| what it is | places containing places | the contract descent a developer walks |
| parent is | a `contain` edge | a registry row |
| governed by | §B.3's two rules | this Part |

⚠ **A MODULE HAS NO PARENT RUNG AND NO DESCENDANT RUNGS.** Placing a rung-level rule on a code-level
object gives the rule no referent, and mirroring the world tree in the code tree buys nothing while
importing name collisions into a design with thirty-plus object names.

## §D.2 · The descent — three levels, and every parent means something

```
GAME
 └── MODULE          one provider · one owned-state set · one declared I/O
      └── DECLARED EDGE     (direction, key type) — what it may emit, what it may consume
           └── FIELD             what a key of that type carries, and its bounds
```

> **The test that decides a level from an axis: A LEVEL IS A PARENT — knowing it constrains what the
> child may be. AN AXIS IS AN INDEX — it selects nodes without containing them.**

**Role, subsystem, key type, phase and scale are all AXES**, and each fails the test for its own
reason: a role has several providers; a key type has many consuming modules, so making it a child
would duplicate FIELD under every consumer; phase is a **set**, not a value, because one write class
is written in two steps; scale is §C.3.

## §D.3 · What may reference what — one rule, derived

> ### **A MODULE MAY WRITE ONLY WHAT IT OWNS, READ ITS OWN AND AN AGGREGATE OVER ITS DESCENDANTS, AND MUST NOT REACH THROUGH ANOTHER.**

**That is `AX-4` applied to code rather than to state**, and it is the same sentence as §B.3's second
rule with *container* replaced by *module*. **The unification is the point: one ownership rule,
stated once, holding at both the world level and the code level.**

## §D.4 · Resolution by declaration, not by import

> **The engine names the ROLE. The registry names the MODULE. Resolution happens by string.**

**Why this and not an import graph:** an import binds a caller to a provider at authoring time, which
makes the dependency a fact about the *text*. A registry row makes it a fact about the *world*, so a
subsystem is swapped by editing a row.

⚠ **AND IT CHANGES WHAT "ACYCLIC" CAN MEAN, WHICH MUST BE SAID PLAINLY.** An acyclic import graph is
not an acyclic dependency graph. **The engine depends on subsystems exactly as much as it ever did**;
the dependencies are declared and resolved by string at first call. **Do not read *acyclic* as *the
engine runs without them*.**

## §D.5 · The reference graph is cyclic on purpose

The conferral path, the containment path, the sworn-edge graph and the claim-citation graph all admit
cycles, **and each of them should**: a cycle is a mutual obligation, a disputed parentage, a rumour
that cites itself.

> ⚠ **SO EVERY TRAVERSAL CARRIES A VISITED SET AND IS WRITTEN ITERATIVELY. A traversal written as
> though it were a tree hangs on the NORMAL case, not on an edge case** — and ids must never become
> object references inside a cyclic structure, or the graph cannot be collected.

---

# PART E · WHAT STAGE 3 INHERITS

1. **One true hierarchy (containment), one graph (subordination), one ordering (rank).** Three
   shapes, three mechanisms, and mixing them is what produced the faction-nesting question.
2. **Only places nest; process nests separately and needs a cap.** The season loop's one nesting
   point is the contest, and it is bounded by the caller.
3. **Scale is derived, and code branches on the ordinal or the relation, never on the member.**
4. **One ownership rule at both levels** — §B.3's container contract and §D.3's module contract are
   the same sentence, which is why `AX-4` is the most productive axiom in the set.
5. **The subordination graph has no root**, so any mechanism that needs one has smuggled an
   institution back in.

## §E.0 · ⚠ Where THIS stage hands properties forward — recorded 2026-09-03

**Stage 4 §G.4.1 says a stage may state a property only with the representation that carries it, or a
register row grading its absence. Applied to this document, two claims have neither:**

| claim | what it lacks |
|---|---|
| *"only places nest"* | **no check.** Nothing refuses a second nesting relation if someone adds one |
| *"the subordination graph has no root"* | **no check.** Nothing detects a root being introduced, and a root is a sovereign nobody swore to |

**Recorded rather than repaired**, because a guard over a shape nothing yet builds would be apparatus
ahead of its subject. ⚠ **But they are hereby graded ABSENT rather than left as assertions** — which
is the honest state, and the difference between a property handed forward *deliberately* and one
handed forward *silently*.

## §E.1 · Open, and neither is Stage 2's to settle

| | where it belongs |
|---|---|
| **What a contest's depth cap should BE at a given venue** | **Stage 3** — it is a property of the act that opens one, and `T-n` says the opener declares its terms |
| **Whether the containment roster carries a sub-settlement tier** | **content, by §C.2's rule** — the architecture is correct for any membership, so this costs nothing to defer and nothing to change later |
