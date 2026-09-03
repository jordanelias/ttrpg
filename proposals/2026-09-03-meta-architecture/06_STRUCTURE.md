# READINGS · 06 — HIERARCHIES, NESTINGS, DEPENDENCIES, STATE CHANGES

## Status: **PROPOSED (2026-09-03). HELD BACK IN FULL.**
## A **reading** of Stages 1–4. ⚠ **If this and a stage disagree, the stage is right.**
## Answers: *"How do we structure our design going forward?"*

> **All four are the same question in different tenses: WHO OWNS THIS?** Containment asks it of
> places, subordination of persons, dependency of modules — and a state change asks it of a value at
> a moment.

---

# §1 · Hierarchies — three shapes the chain calls by one word

| | shape | walkable? | answers |
|---|---|---|---|
| **CONTAINMENT** | **tree**, single parent, `Rung → Rung` | **yes — the only true hierarchy** | where a thing is |
| **SUBORDINATION** | **graph** of sworn person-edges, lateral, **no root** | traversable, not walkable | who owes whom |
| **RANK** | **total order** — the ordinal of a seat's domain in the containment roster | **nothing to walk** | how wide a warrant is |

**Rank needs no storage and no second ladder** — the roster is already ordered. And it asks *how wide
a KIND of thing*, never *how many things*, which is why a Lord governing three territories still ranks
under a Count governing one province.

> ⚠ **THE SUBORDINATION GRAPH MUST NEVER BE GIVEN A ROOT.** A root is a sovereign nobody swore to —
> an institutional relation through the back door. **Its absence is what makes a contested realm
> expressible:** two people each claiming the top, with no node above them to adjudicate.

**The CODE hierarchy is a fourth thing, not a mirror of the first:** `GAME → MODULE → DECLARED EDGE →
FIELD`. Three levels, every parent constraining its child. **Role, subsystem, key type, phase and
scale are AXES** — indices that select without containing. A module has no parent rung.

---

# §2 · Nestings — two kinds, opposite bounding problems

**ONLY PLACES NEST.** Factions do not (a person's edges, many at once, spanning places). Offices do
not (same relation, same reason). Rank does not (an ordering has no parent).

The second kind is **process**, nesting *time* rather than space: a contest is the season loop over a
smaller person set on a shorter clock.

| | place-nesting | process-nesting |
|---|---|---|
| bounded by | **the roster** — finite by construction | ⚠ **nothing intrinsic** |
| needs a cap | no | **yes — caller-supplied, NO DEFAULT** |
| a cycle means | impossible | legitimate, and must terminate |

**A default depth is a fabricated constant** that gets cited later as though measured. Exceeding the
cap returns a **typed refusal**, never a raise — a refusal is an outcome the fiction can carry; a
crash is not.

---

# §3 · Dependencies — one rule, two levels

> **A module writes only what it owns, reads its own state and an aggregate over its descendants, and
> never reaches through another.**

**That is the container contract with one noun changed.** One ownership rule governing both the world
and the code is why `AX-4` is the most productive axiom in the set.

**Resolution is a registry row, never an import.** The engine names the ROLE; the registry names the
MODULE; resolution happens by string.

⚠ **So the import graph can be acyclic while the dependency graph is not — and *acyclic* must never be
read as *runs without them*.**

**The reference graph is cyclic on purpose** — conferral paths, containment, ties, claim citation. A
cycle is a mutual obligation, or a rumour citing itself. **Every traversal therefore carries a visited
set and is written iteratively; one written as a tree hangs on the NORMAL case, not an edge case.**

---

# §4 · State changes

**One shape:** `(subject, mode ∈ create | alter | destroy, driver ∈ Act | Event, field?, delta?)`.

**Four write classes — and a class is NOT a step.** One class can be written in two steps, which is
why `phase` must be a set rather than a value.

**The matrix is keyed on `(kind, field)`, never on things.** Key it on things and one field rides on
another's row, and a real gap reads as a pass. **Any unmarked cell is a violation.** Each row declares
`writer: act_only | world_or_act` and what it emits.

**The world may write only three motions: matter, bodies, and the fading of memory.** Everything else
has an author.

> ### **EVERY WRITE GOES THROUGH ONE GATE, AND THE GATE APPLIES IT.**
> It returns a **receipt**; an Event's `changes[]` *are* receipts; the log refuses an Event carrying a
> receipt the gate never minted. **That is what makes "reports success for something that did not
> happen" unwritable rather than merely detectable.**

**A crossing emits and never decides.** A quantity passing a declared edge changes what may be chosen
and by whom — including to nothing — and produces no outcome.

---

# §5 · The one test that runs through all four

> **Name the writer.**
> **One** → a unit, a parent, a dependency edge, a lawful write.
> **None** → the model is incomplete.
> **Two** → a defect, and you have just located it exactly.
