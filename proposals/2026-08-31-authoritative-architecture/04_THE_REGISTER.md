# 04 · THE REGISTER — keys, names, collisions, closed sets

## Status: PROPOSED (2026-08-31), except §1, which describes **code that executes today** and is
## therefore mechanism under `CLAUDE.md` §0.05. Everything else here is reference until it runs.

---

## §1 · THE KEY SUBSTRATE AS IT EXISTS — this part is not a proposal

`engine/substrate/keys.py` is executable, canonical (ratified 2026-07-07), and **runs default-ON in
every seeded campaign** — the goldens pin its emission counts and its content hash.

```python
class Key:
    id: str
    type: str
    emitted_at: EmittedAt
    source_actor: str | None
    causes: list        # provenance — ids of the Keys that caused this one
    targets: list       # list[Target]
    scale_signature: list[str]
    symbolic_dimensions: dict
```

**What it already guarantees, and therefore what must never be re-implemented beside it:**

| guarantee | where |
|---|---|
| append-only log | `KeyLog` |
| **id uniqueness**, raised as an invariant | load-time invariant 1 |
| **referential integrity** — a `causes` entry naming an unknown id **raises** | invariant 3 |
| **cycle-freedom by construction** for an append-only log | invariant |
| **content hash** over the log — the replay and parity surface | `KeyLog.content_hash()` |
| lookup by id as a first-class operation | — |
| deferred-apply barrier semantics (OF-7) | the scheduler's phase check |

> ### ⭐ THE RULING THAT DECIDES THE WHOLE ARCHITECTURE'S SHAPE
>
> **The Key substrate IS the design's `Event` mechanism, in substance.** Same id discipline, same
> append-only log, same `causes[]` provenance, same content-hash replay surface — and it executes.
> **`Event` is built AS a Key type family, or as Key's successor sharing `KeyLog`'s invariants. Never
> as a second log.**
>
> **The Key substrate is NOT the design's `Claim`/`witness`/`Query` mechanism.** `compute_observers`,
> `memory.record`, `memory_query` and `MemoryIndex` exist **only as pseudocode** in
> `systems/_architecture/key_substrate_v30.md`; the executable substrate's own docstring says
> observer resolution is deliberately unimplemented. Under §0.05 a design document may not be cited
> as the reason a behaviour exists. **That half is greenfield.**
>
> Two independent sweeps reached opposite verdicts here — one said "zero design objects exist in
> `engine/`", the other said "already canonical and executable" — and **both were half right.** The
> line between the halves is one docstring.

**Consequence for `resolve`.** `references/module_contracts.yaml`'s `resolver:` field is a
**strategy label**, not a signature; the 27 registered roles have mutually incompatible callable
shapes. A declared consumes/emits edge list is a *shape precedent*, not a wired signature. `resolve`
is greenfield; the contract table is the registration pattern to copy.

---

## §2 · THE KEY NAMESPACE

**The roster is `engine/engine_params/key_types.json`'s registered types**, of which a subset is
flow-bound in `references/module_contracts.yaml` and the remainder is registry-only. **Cite the two
numbers separately or not at all** — a single figure for "the number of key types" has been quoted
three different ways in this corpus and each was true of a different set.

### The naming rule, made mechanical

Casing is the membership test, so a reader can tell whether a new name obeys the rule without asking.

| thing | form | example |
|---|---|---|
| **event / key type** | `family.type`, lowercase, dotted, regex-enforced | `scene.accord_echo`, `mechanical.season_change` |
| **state identifier** | owner-dotted, spelled out, no abbreviations | `site.condition`, `office.upkeep` |
| **record type** | `Capitalized`, registered in `references/names_index.yaml` | `Person`, `Tenure`, `Claim` |
| **kind value** | lowercase, **never exported bare** — always qualified by its record | `tenure.hold`, never a bare `kind: hold` |
| **loop step** | `UPPERCASE`, words only, no letter-number spellings | `RESOLVE` |
| **Query** | verb or noun function, arguments always shown | `presence(f, n)`, never bare `presence` |

**The `family.type` event namespace is the one measured-working namespace in this repo.** It is
regex-enforced and it has not drifted. **Extend it; do not invent a second scheme beside it.**

---

## §3 · ED-IN-0200, DISCHARGED

**The ruling, verbatim (Jordan, 2026-08-27/28):** *"KEY CONTRACTS AND MODULE CONTRACTS ETC NEED TO BE
EXPLICITLY DEFINED IN A CENTRALIZED HIERARCHICAL MANNER."*

**Its ledger status is `open`, `needs_jordan: false`** — Jordan has ruled; what is missing is
execution. Flagging it back to him would be the parking-space misuse `CLAUDE.md` §0 forbids.

**The measured current state:** three registries exist and **none is hierarchically related to any
other** — `references/module_contracts.yaml` (the 27 modules and their IN/OUT key flows),
`engine/engine_params/key_types.json` (the type registry), and
`references/descriptor_registry.yaml` (the attribute roster). Each is separately exported, separately
validated, and flat.

> ### THE DISCHARGE — a specification, deliberately ontology-neutral
>
> **One validated parent, three leaves.** The three registries become the leaves of a single
> contract tree whose parent declares the hierarchy: family → type → contract → module → role. The
> parent is generated, and generation is checked by a **blocking `--check` round-trip**, exactly like
> the seven exporters that already gate CI.
>
> **Why a round-trip and not a new validator:** `CLAUDE.md` §0.1 point 5 licenses a guard only when
> the artifact is load-bearing on the game, the exported params, the port or a Jordan decision. **The
> contract tree is the thing the Godot port ingests, so it qualifies** — and the `--check` pattern is
> the one this repo has already proven seven times rather than a new mechanism.
>
> **This stays `open` until it runs** (§0.2). A specification is not a discharge; the exporter is.

**⚠ And the reconciliation nobody has made.** ED-IN-0200 and the #337–#344 design line **never cite
each other**, and they land three days apart. They are plausibly independent answers to the same
problem: the design line's `Tenure`-and-`Query` unification *is* a hierarchical contract definition,
arrived at from the game side rather than the registry side. **Whichever is built, it should be built
once.**

---

## §4 · THE COMPLETED COLLISION REGISTER

The head ruled on ~22 colliding words. **Independent sweeps of the working tree found more, and the
new ones matter most because several are in running code — and a meaning in executing code outranks a
meaning in prose (§0.05).**

| word | meanings the head found | **meanings it MISSED** | ruled form |
|---|---|---|---|
| **`hold`** | Tenure kind · Proposition mood `HOLDS` · predicate `HOLDS(p,x)` · coercion quantity | **⚠ a mass-battle unit's tactical stance — live code, `systems/mass_battle/sim/config.py:269`**; and a process sense, "HELD for Jordan" | `Tenure(kind=hold)` / exported `tenure.hold`; `HOLDS` capitalised for the mood; `HOLDS(p, x)` with arguments; the MB stance keeps the bare string inside its own module |
| **`stance`** | `Person.stance` | **⚠ FIVE senses, none registered** — the live mass-battle unit stance; **the live NPE per-issue stance that drifts every campaign** | `Person.stance` always carries its record. **The NPE store must be ABSORBED by the carrier, not doubled beside it** |
| **`witness`** | the function; the loop step | **⚠ a live Key `Target` role, and a registered `scene.witness` key type** | the step is `WITNESS`; the function is `witness(person, event)`; the Key role keeps its own name |
| **`strike`** | fault severity | **⚠ the live `combat.strike` ported module and `scene.combat_strike` key** | the office action is `strike from the roll`, written in full |
| **`presence`** | the Query; deposits-by-presence | **⚠ `Presence` was the legacy Core Attribute name, now an alias of `Charisma`** | the Query always carries its arguments |
| **`View`** | the type; the function | **⚠ one of four documentation lenses in the engine atlas** | the type keeps the word; the function is `assemble(person, question)` |
| **`kind`** | seven record senses | **⚠ the registry's own `KIND:` taxonomy enum and `module_contracts.yaml`'s `kind:` field** — pre-existing YAML keys the "qualify by record" rule does not reach | always qualified by its record; **never exported bare** |
| **`Derived`** | the query category | — | **`Query`.** Verified necessary: three live registries use `Derived` for *stored* values |
| **`Container`, `Node`** | Godot built-ins | — | **`Rung`** |
| `subject`, `object`, `condition`, `act`, `matter`, `root`, `degree`, `stake`, `address`, `magnitude`, `standard`, `commit`, `envelope`, `payload`, `ledger` | ruled by the head | — | as the head ruled: **always qualified by its record; bare tokens never used** |

> **The register's own lesson, and it is the method's.** The head's first pass renamed the containment
> object `Node → Container` **on the ground of avoiding a Godot collision, and landed on a worse
> one.** A register that can miss a self-inflicted collision on its own first pass will miss live-code
> meanings, and it did — five of them. **Grep the running code before ruling a name.**

---

## §5 · THE NAMING RULES

`CLAUDE.md` §4's two tests bind, and they bind because **there is no context between sessions**:

- **Idempotent in meaning** — reading the word cold, later, must yield the same meaning.
- **Idiomatic in choosing** — use the word ordinary usage already supplies.

| term | verdict |
|---|---|
| `Rung` | **keep.** Ordinary, collision-free, and the tree's own word |
| `Query` | **keep.** Ordinary; the rename off `Derived` was forced by three live registries |
| `Tenure` | **keep.** Ordinary usage supplies exactly this meaning — a holding, for a term, conferred |
| `Office`, `Site`, `Claim`, `Act`, `Event`, `View` | **keep** — all ordinary, all qualified in use |
| `Sensation` | **keep, with a caveat.** Slightly coined; it survives because the ordinary alternative, `needs`, is already taken by the Nobody row |
| `mint` / `efface` | **kept under protest, for collision-avoidance only.** `create`/`destroy` are the ordinary words and would read better cold — but they are near-universal identifiers likely to collide in GDScript. **The exception §4 permits is exactly this one**, and the words must therefore be defined **in the exported schema's own comment**, not only in prose |
| the six step words | **keep** — ordinary English, uppercase, no letter-number spelling, ever |

> **DEFINE IT IN BOTH PLACES.** A process term that lives only in prose is half-defined: the next
> session meets it *in code* first and infers the meaning from the call site. Every coined term above
> must appear in the exported schema, the registry `role:` line, or the module docstring that calls it.

---

## §6 · THE CLOSED SETS

A set declared closed that is in fact open is a fence someone will climb. Each is judged.

| set | members | genuinely closed? |
|---|---|---|
| **`Tenure.kind`** | `hold, commit, contain, succeed, tie, knot, oblige` | **YES** — each carries a distinct cardinality rule; a new kind needs a new rule, which is the right friction |
| **`StateChange.mode`** | `mint, alter, efface` | **YES** — exhaustive over "begins to exist / changes / ceases to exist" |
| **`StateChange.driver`** | `Act, Event` | **YES** — the Partition is a total function on the schema column |
| **`Claim.source`** | four constructors | **YES**, and the head's own proposed fifth was correctly withdrawn as already covered by `told_by(record, …)` |
| **write classes** | `CALENDAR, MATTER, ACTS, INTERIOR` | **YES** — the write matrix is total |
| **loop steps** | six | **YES** |
| **predicate forms** | fourteen | **closed with a stated test for a fifteenth** — which is the honest form |
| **`remit.acts`** | five | **NO, and the head says so.** The verb space is **open**; the mode space is closed. At least nine verbs the design itself names sit outside the five |
| **degree bands** | — | **⚠ CONTESTED.** The compendium describes a five-band ladder as shipped; the live single owner, `engine/autoload/dice_engine.degree_from_net`, implements the **ruled four-band** ladder. **The code is the mechanism (§0.05). The compendium is wrong and is overturned here** |
| **`MatterKind`** | — | **open, and correctly so** — it is a type parameter, not an enumeration |
| **stance referents** | `Person, Place, Proposition` | **YES** after `Faction` is struck (it denotes the same thing as `Proposition`) and `Place = Rung | Site` is defined |
