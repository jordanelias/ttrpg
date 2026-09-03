# READINGS · 05 — OBJECTS, RELATIONS, EDGES AND FIELDS

## Status: **PROPOSED (2026-09-03). HELD BACK IN FULL.**
## A **reading** of Stages 1–4, indexed by question rather than by stage. It introduces nothing.
## ⚠ **If this and a stage disagree, the stage is right and this is stale.**
## Answers: *"How do objects, relations, edges and fields work?"*

---

# §1 · There are FOUR kinds of value, not two — and one question sorts them

| answer to *who writes this?* | it is a… | owned by |
|---|---|---|
| one writer, about **one** thing | **FIELD** | that thing |
| one writer, about **two** things | **EDGE** | its **subject** |
| **no writer possible** — it spans many owners | **QUERY** | Nobody. Computed, stored nowhere |
| no writer, but recomputing is too costly | **BARRIER CACHE** | Nobody. Built at a barrier, **discarded at the next** |
| ⚠ **two writers** | **a defect** | — and you have just located it exactly |

**That is the whole taxonomy.** Most schema arguments are really an unasked ownership question.

---

# §2 · Objects

**Identity-bearing carriers:** `Person` · `Rung` · `Site` · `Record` · `Seat` — mutable — plus
`Proposition`, **immutable and never destroyed**.

**Ids are typed**, minted `H(world_seed, tick, subject, purpose)`. **No allocator, no counter,
nothing to serialise on** — which is what makes the loop order-independent, and why a new draw in a
new place must never reuse a `purpose`.

**Each object is defined by an ADMISSION TEST, never a field list:**

> **IS** — the one sentence · **OWNS** — what it is sole writer of · **ADMITS** — the test a proposed
> field must pass · **NEVER** — what may not be on it, with why.

**A field list can only grow. A test can ANSWER a requirement** — often by showing it is already
expressible, sometimes by showing it belongs to something else entirely.

---

# §3 · Fields — and the three clauses that decide admission

A field is a value the object owns and is the **only writer of**. Two clauses decide most cases, and
**using the wrong one is what makes a schema over- or under-refuse:**

| category | admitted when |
|---|---|
| what a thing **HOLDS** | **a decision reads it.** If nothing it decides consults it, it is dead state |
| what the world **READS OFF it** | **a resolver reads it.** It never enters a decision and by construction cannot |

**The split is not invented to save the test.** `standing` is defined as *the gap between what
everyone reads off you and what you hold* — a definition that presupposes both sides.

**NEVER a field:** anything about another object · any aggregate · the reverse of its own edges.

⚠ **AND A THIRD CLAUSE, ADDED TO STAGE 1 ON 2026-09-03 (`§D.0`) — WHAT KIND OF ASSERTION IS IT?**
Owner and reader are two questions; the third is independent of both. **A field asserts what is
DECLARED** (somebody said so, and the saying is the fact), **what IS THE CASE** (true whether or not
anybody says so), **or what is READ OFF** (others take you to be this). **A field that cannot be
sorted into one of the three is mis-modelled** — and the usual verdict is not *refused* but *filed on
the wrong object*: `judging_set_rule` was a declared thing on a place, and moved to a Query over
seats. The stage is the authority; this line only records that the reading's two clauses are no
longer the whole test.

---

# §4 · Edges

**One edge type — `Tenure`, seven kinds — and no second relation mechanism anywhere.** Adding one is
the violation, not the solution.

> **Every edge is owned by its SUBJECT.** One home, one writer, no reach-through.
> **The object side is a DERIVED INDEX — never stored.**

**`until` is what makes an ended relation a fact.** Rows are never deleted, because an ended tenure is
a historical claim subject — argued over, read for entrenchment.

**Three routes end one, and they are exhaustive** ⚠ *(this read TWO until 2026-09-03; Stage 1
`§E.1.2` found a third in the live vocabulary and made it lawful as `T-o` rather than tolerated —
the stage governs and this reading was stale)*:

1. **The owner's discretion.** You may always end what you own, because `until` is a field of a thing
   you already write. **It binds by cost, not by impossibility** — forswearing spends a scene, emits,
   and witnesses mint claims about it. What you cannot do is forswear *unnoticed*.
2. **A declared term**, set by the act that opened it and matured by the world, citing that act.
3. **A revocation declared on the SEAT** (`T-o`) — the seat's own `revocation` basis, exercised
   through `Act.via` by whoever currently occupies it, and refused the instant they do not. **It is
   still declared**, which is why three ways is still a closed set: what changes is *where* the
   declaration lives — `T-n` puts it on the Tenure, `T-o` on the Seat.

**That exhaustiveness is what makes open-without-close UNSPELLABLE** rather than a thing you remember
to check. Four of seven relations currently fail it.

---

# §5 · The two failure modes, and they are mirrors

> **An edge whose subject cannot act is a FIELD wearing a relation's shape.**
> **A field that is about two things is an EDGE that has not been named.**

| case | the tell | the repair |
|---|---|---|
| `succeed` | subject is a `Rung`; a Rung cannot act, so it has an owner that can never write it — **which is exactly why it is one of the four nothing can end** | re-subject onto the holder, whose act maintains it |
| a seat's membership list | a list of persons on a seat is **a set of edges pretending to be a field** — two homes for one fact | each person `oblige`s to the seat; the roster is a Query |

⚠ **`contain` is the honest exception** — `Rung → Rung`, subject cannot act, and correctly nobody ends
it by choice; it moves when a person moves.

> **So the test is not "can the subject act" alone. It is: SHOULD THIS END BY SOMEBODY'S DECISION?**
> If yes, the subject must be able to act. If no, it is a field of the world.

---

# §6 · Existence and destruction

One shape for every mutation: **`create | alter | destroy`.**

**`destroy` sets `until` on every Tenure naming the id — and destroys nothing else.** It does not
cascade into other carriers, because a cascade is one object writing another's state.

**A `Proposition` has no setter and no delete**, which is why it needs no owner: nothing may change
it. That immutability is also what makes a faction collapse for free — a faction *is* a Proposition
plus its `commit` edges, so when the last person releases there is nothing left to be it.

⚠ **Provided nothing else can hold it.** `hold`'s subject must be a Person only, or you get territory
held by a banner nobody carries — **uncontestable, because the holder can never appear at a venue.**

⚠ **AMENDED 2026-09-03 — *a faction IS a Proposition plus its edges* is right about IDENTITY and was
wrong about DEPLOYMENT.** `Faction` is now a type: a **Query return** resolving that proposition into
`(members, holdings, seats, head?)`, built at a barrier and dropped at the next (Stage 4 §B.6.1). It
owns nothing, admits no field, and appears in no actor position — **so the collapse-for-free property
above is untouched**, because the view is the edges and the edges are still the only state. `hold`'s
subject is still `Person` only. See `10_FACTIONS_AND_DEPLOYMENT.md` and Stage 1 §D.11.
