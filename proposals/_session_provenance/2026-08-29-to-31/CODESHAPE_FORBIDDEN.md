## 7. What must NOT exist in the codebase

Each of these is refused because it re-enables a failure the design closed structurally.

| forbidden | because |
|---|---|
| a `World` parameter on any decision function | T4 collapses; every belief mechanism becomes decoration |
| a `view_of(world, person)` that masks rather than assembles | someone eventually masks nothing |
| any function taking `[Person]` and one `Event` | consensus broadcast; divergent perspective dies |
| **a deposit into a cohort that carries a VALUE rather than a DISTRIBUTION** | consensus broadcast laundered through the cohort type — one sign and one magnitude into hundreds of people, and the type checker sees a single legal write. A cohort claim stores the construal spread its members would have produced (doc 03 §2); an individuating member **draws** from it and never inherits it (doc 09 §10). This row exists because the defect passed every other row in this table. |
| a pushed aggregate, or a field one is stored in | R-1; a push needs a landing site and the landing site is stored aggregate state |
| a stored aggregate, norm, density, unrest or reputation field | dead state that reads as mechanism |
| a knowledge value stored on the thing known | knowledge with no knower cannot be planted or refuted |
| a second resolver, an auto-resolve formula, a fast path | guaranteed divergence, unsolved in the genre for twenty years |
| a `tier`, `level` or `scale` field on a faction | growth becomes discontinuous |
| a flat additive modifier from a person onto a roll | worth X/(0.671·√Pool) — doc 10 §6's constant — so it helps weak pools more, backwards |
| a personal effect on a group that is not a fraction of that group | the only concrete anti-leverage rule the precedent corpus supplies |
| a scheduled recovery tick on standing | converts a consequence system into a treadmill |
| a per-entity branch anywhere in the resolver | scripting drift; the exception becomes the mechanism |
| an authored per-person opportunity or quest object | a churning world turns back into content |

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
  sibling's state and may **not** read a descendant's state directly. It **may COMPUTE an aggregate over
  its descendants on demand**, when asked; it may **not** receive a pushed aggregate, and it may **not
  store one**.

  ⚠ **This rule was written as "it receives aggregates" and that wording is retracted — adjudication
  C-1 corrected it, and this document is older than the correction.** As written, R-1 forbade the very
  aggregations the suite computes everywhere (a settlement's Order capacity, a faction's estimated
  profile, `carriage_mass`, `Hold`, `concord`, `rarity`, `price`), and simultaneously licensed the one
  thing the architecture exists to abolish: a per-tick push flow, which requires somewhere for the
  pushed value to land, which is stored aggregate state — the row three lines down in §7's forbidden
  list. The corrected rule says the opposite on both halves. **Compute-on-demand, never push, never
  store.**
- **R-2** A rung module may write only its own state. Upward influence is emitting an aggregate;
  downward influence is emitting a refraction. **No module reaches through another.**

A cross-rung read is the single easiest way to destroy T5 and T6, because once the realm can read a
person directly there is no reason for the ladder to exist, and every intermediate rung quietly
becomes decoration.

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
