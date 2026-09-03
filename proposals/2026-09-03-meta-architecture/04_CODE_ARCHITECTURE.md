# META-ARCHITECTURE — STAGE 4 · CODE SHAPE, TYPES, SEAMS, IMPOSSIBILITIES

## Status: **PROPOSED (2026-09-03). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE. Nothing here runs.**
## Produced by a **read-only** Fable 5.1 synthesis holding Stages 1–3 in context. Concrete shapes taken
## from, amended against, or rejected from the chain (#353 `ARCHITECTURE.md`, `ARCHITECTURE_V2.md`,
## the three YAML files). **Nothing under `canon/`, `systems/`, `research/` or `engine/` was read.**

---

> # ⚠ THIS DOCUMENT IS INCOMPLETE, AND THE MISSING PART IS THE ONE THAT MATTERED MOST
>
> **Stage 4 was truncated by a session rate limit mid-sentence at item 25 of PART D.** It delivered
> PART A (the architecture), PART B (the type shapes), PART C (the seams) and PART D items 1–24.
>
> **PART E (the build order) and PART F (where the three stages are insufficient) were never
> produced.** PART F was commissioned in these terms: *"name every place you needed something the
> stages do not supply, and say what you assumed. Do not paper over a gap to make the architecture
> look complete — a named gap is worth more than a smooth design resting on an invention."*
>
> **Nothing has been written in its place, and nothing should be.** The synthesis marks its own
> assumptions inline throughout — every one tagged *my call* with the alternative it rejected, and
> several forward-referencing a §F that does not exist (`§F.1`, `§F.4`, `§F.5`, `§F.6`, `§F.7`,
> `§F.15`). **Those dangling references are the honest record of what is missing**, and they are the
> first thing a completion pass should collect.

---

## §0 · How enforcement is graded, and why the grade is stated per invariant

Stage 1's `T-f` says enforcement is *"by parameter list, not by discipline"*, then honestly that
*"in GDScript this degrades to a convention plus a token scan, permanently."* Three grades, applied
to every invariant in both target languages:

| grade | means |
|---|---|
| **STRUCTURAL** | the defect has no spelling. The type, the parameter list, or the absence of a name makes it unwritable — **a reviewer cannot let it through because it cannot be written** |
| **MECHANICAL** | exactly one path exists and it refuses. A bypass must go *around* the only path, and one named test or scan sees it |
| **CONVENTION** | a reader notices. **Stated as such, never dressed up** |

> **A claim of STRUCTURAL that is actually MECHANICAL is the defect class Stage 1 §0.2 names** — *a
> guard that cannot observe what it guards.* So the grade is stated per invariant, and the Python and
> GDScript grades are stated separately wherever they differ.

---

# PART A · THE CODE ARCHITECTURE

## §A.1 · What each axiom forces

The decomposition derives from the axioms first, and is compared to the chain's layout only after
(§A.3). Stage 2 fixes the descent — `GAME → MODULE → DECLARED EDGE → FIELD` — and the one rule:
*a module may write only what it owns, read its own and an aggregate over its descendants, and must
not reach through another.* **A module is therefore an owned-state set with a declared I/O, and the
axioms say what the owned-state sets are.**

| axiom / theorem | what it forces | module |
|---|---|---|
| **AX-4** one owner, one writer | one store per carrier; **one write path** that *applies* the write and returns a receipt; every object-side index is a barrier cache owned by Nobody | `state/` + **the gate** |
| **AX-2** no privileged access | the decision compiled where `World` is not a name; the two Query families split **by module**, not by first parameter; `sense()` called by the loop, never by the decision | `decision/` · `queries/person_q` vs `queries/world_q` |
| **AX-3** true ≠ right | ledger and conviction state in **different sub-stores with different write tokens** — INTERIOR at WITNESS, ACTS at RESOLVE. A step holding one cannot reach the other | `state/ledgers` ≠ `state/persons` |
| **AX-5** three motions | exactly one step holds the MATTER token; a matured term cites the act that wound it | `loop/matter` |
| **AX-6** nothing permanent without an author | every Tenure carries an optional declared term; **one generic closing verb whose eligibility is ownership**; a load-time check that every opened kind has a closer; ended edges reachable only through a separate accessor | `state/tenures` · the verb table · `data/loaders` |
| **AX-1** only a person acts | `Act.actor : PersonId` and nothing else has that type; `resolve` has no institution parameter; a seat enters through `Act.via` | `loop/resolve` |
| **T-i** no container gets a clock | the driver is the only caller of any step; **carriers have state and no behaviour** | `loop/driver` |
| **T-k** one resolver, one ladder | the fold lives once; the ladder lives once, in the seam | `loop/resolve` · `seam/ladder` |
| **T-l** a cohort is a Person at weight > 1 | one `Person` class; **no subclass exists** | `state/persons` |
| **ID-12 · ID-5 · ID-13** | every roster, table, fixture, matrix and verb row read at load by **one** loader that cross-validates and raises on any absence or any declared-but-unread row | `data/` |
| **Stage 2 §D.4** resolution by declaration | the seam names a role; a manifest row names the provider; resolved at boot | `manifest/` |

## §A.2 · The nine modules

```
state/       the owned stores · the gate · the log · the ledgers · the id mint
data/        every closed set, table, fixture, the write matrix, the verb table — and the ONE loader
queries/     ownerless functions: world_q (World first) · person_q (asker first) · cache (barrier-built)
decision/    AX-2's island: questions · opening_set · choose · budget.   NO World in scope.
loop/        driver + six steps.  The driver is the ONLY constructor of write tokens.
seam/        contest() · ladder · one wrapper per deferred subsystem
manifest/    role -> provider rows, resolved at boot
port/        the Godot shell; nothing under it is simulation
tests/       falsifiers, including the two licensed guards
```

**A module with no token cannot write, and that is the whole of the write discipline.**

| module | owns (writes) | may read | emits | token |
|---|---|---|---|---|
| `state/ids` | the mint `H(seed, tick, subject, purpose)`; typed ids | `world_seed` | — | — |
| `state/<carrier>` | its own rows. **No public setter on any of them** | — | — | — |
| `state/gate` | **nothing.** The one write path: `write(token, kind, field, id, change) -> Receipt` | the write matrix | the row's `emits` kinds | consumes the caller's |
| `state/log` | itself, append-only; the invariants; the content hash | — | — | — |
| `state/ledgers` | per-person packed claim rows; the eviction comparator | — | — | — |
| `data/loaders` | the in-memory forms; the cross-validation invariants (§B.13) | the data files | — | — |
| `queries/world_q` | **nothing** — no token parameter exists on any function | any store, via `World` | — | — |
| `queries/person_q` | nothing | **a `PersonInterior` snapshot only** | — | — |
| `queries/cache` | barrier indexes: presence, object-side Tenures, subtree aggregates | any store, **at a barrier only** | — | — |
| `decision/` | **nothing.** Returns `Scene[]` | `PersonInterior`, `View`, `Sensation`, `budget`, `Question[]`, the table's declarations | — | **none** |
| `loop/driver` | the season index; the tokens; the caches' lifetimes | everything, by construction | — | **mints all four** |
| `loop/calendar` | `Date.fired`, `DocketItem`, `ConveningCondition` | own state, an R-1 subtree aggregate, the calendar | `date.fired` · `docket.formed` | CALENDAR |
| `loop/matter` | the three motions; maturation of declared terms | Sites, bodies, larders, ttl/term | per matrix row | MATTER |
| `loop/deliberate` | **nothing.** Calls `sense()`, builds `View`, calls `choose` per person | frozen `World`, for `sense` only | — | **none** |
| `loop/resolve` | every ACTS row, through the gate; the ordered fold | `World`, the verb table, the `Act[]` | each verb's `emits` / `emits_on_refusal` | ACTS |
| `loop/witness` | claim deposits into each holder's **own** ledger | this tick's log, presence cache, channel predicates, the act store | `claim.deposited` | INTERIOR |
| `loop/census` | `(Person, exists)` on individuation, `weight`, `envelope` | post-eviction ledgers once; the log for demand kinds | `person.individuated` | MATTER |
| `seam/contest` | **nothing.** Dispatches; enforces `max_depth`; returns Events + degree, or a typed refusal | a read-only projection | the contest's Events, **into the same log** | **none** |
| `seam/ladder` | nothing. `degree(margin, veto?) -> Degree` | the exported band edges | — | — |
| `seam/wrappers/*` | **nothing, ever** | the projection | a `Margin` | **none** |

## §A.3 · Fifteen differences from the chain, each with its forcing clause

| # | the chain | this | forced by |
|---|---|---|---|
| 1 | `deliberate` beside `resolve`, in a directory whose every other file names `World` | **`decision/` is a separate module** | AX-2 via T-f. A module boundary is the only thing making *no World in scope* checkable by path rather than by reading bodies |
| 2 | one `Query` class holding both families | **two modules**; the second cannot import the first | T-f. In one class, a person-side function calls a resolver-side one with no import to scan |
| 3 | write class as a **parameter** of the store API | an **unforgeable token type**, one per step, minted only by the driver; DELIBERATE receives none | AX-4 + ID-9. A parameter can be passed by anyone; a token only by whoever was handed it |
| 4 | `scale:` on modules and on seven verb rows | **deleted; the loader rejects the key** | Stage 1 §E.3, Stage 2 §C.3, ID-13 |
| 5 | `Office` with `establishment[]`; `Title` via a roster and a collision check | **one `Seat` type; no `Title` type; no membership field** | §D.7 (*not an entity*), §E.2.2 (*authority is a property of the seat*), ID-1, ID-2 |
| 6 | `Event` with a `subject` field | **no `subject`.** `changes[]` are gate receipts; place is a Query | T-d as Stage 1 sharpens it — *"currently a naming convention, not a mechanism"* |
| 7 | `Rung.judging_set_rule` | **deleted**; the judging set is a Query over seats | §D.2's NEVER — *decision-shaped state on a container* |
| 8 | `Rung.matter.transmission` | **deleted**; `succeed : Person → Person`, owned by the holder | §E.1.3 |
| 9 | `tie`/`knot` stored once on the lower id | **two directed edges**; strain is a Query | §E.1.3 |
| 10 | `Person.beliefs[]` | **deleted**; a belief is a `commit` to an `OUGHT` | §D.1.1 |
| 11 | `Petition`, `Dispensation` as separate non-carriers | **kinds of `Record`** *(synthesis call)* | ID-7; §D.4's admission test |
| 12 | `hold` with a Proposition subject | **`hold`'s subject is a Person, only** | §E.1.3 — *an edge whose subject cannot act is not a relation* |
| 13 | only `Event` and `Claim` persist past a season | **`Act` persists**, resolver-side, unreachable from any person-side surface *(synthesis call)* | `causes[]` must resolve **and** T-d must hold. Both cannot be had if the Act is discarded |
| 14 | four closing verbs missing | **one `release` verb**, eligibility `own`, generic over kind; `Tenure.term?` for declared ends | T-m, T-n, ID-14 |
| 15 | `budget` includes an `office_bonus` | **refused.** A seat's capacity is its establishment — more named persons, each with their own budget | Stage 3 §A.3 — *no seat carries a bonus* |

---

# PART B · THE TYPE SHAPES

## §B.1 · Ids and tokens

```
Id     := (kind_tag, n)      n = H(world_seed, tick, subject, purpose)   -- no allocator, no counter
PersonId · RungId · SiteId · RecordId · SeatId · PropositionId · TenureId · ActId · EventId · ClaimId · DateId
       := DISTINCT TYPES, not one type with a tag read at runtime
ROOT   := a distinguished EventId                 -- the antecedent-free sentinel

WriteClass := { CALENDAR, MATTER, ACTS, INTERIOR }
Token      := (write_class, tick)                 -- constructed by loop/driver and NOWHERE ELSE
```

| invariant | Python | GDScript |
|---|---|---|
| `Act.actor` cannot hold a `SeatId` | STRUCTURAL under a checker; MECHANICAL at runtime | MECHANICAL — tag assertion in the fold |
| ids never become object references in a cyclic structure | CONVENTION + scan | CONVENTION + scan (**Godot has no cycle collector**) |
| only the driver mints a Token | MECHANICAL — a test asserts `Token(` appears in `loop/driver` only | MECHANICAL, same scan; **GDScript has no private constructors** |
| `H` is owned and versioned, never a built-in `hash()` | MECHANICAL — one function, pinned by a golden | same |

## §B.2 · `Person` — *the only thing that can be wrong*

Fields are grouped by Stage 1's split reader clause — **held** fields need a *decision* to read them,
**read-off** fields need a *resolver* — and each names its reader, because *a schema claim about what
code reads must ship the way to re-run it*.

```
Person := ( id, weight, capability, marks[], body, exists, travel_leg
          , stance[], convictions, scar[axis], axis_count[axis], coherence?
          , ledger )
NOT ON IT:  beliefs (a commit to an OUGHT) · ties_index (Nobody's) · any aggregate · anything about another person
LOCATION:   the person-kind Rung sharing its n; its contain edge is where they are
```

| invariant | grade (Py / GD) | construction |
|---|---|---|
| **one class; a cohort is not a subclass** | CONVENTION + a test asserting no subclasses exist | there is nothing to convert to |
| **`choose` cannot read another person, an aggregate, or world truth** | STRUCTURAL (typed) / MECHANICAL (path scan) | it receives a `PersonInterior` — **a frozen copy with no store handle.** A smuggled global would still have to be looked up through a store the module cannot name |
| **WITNESS never touches a conviction** | MECHANICAL / CONVENTION + scan | the INTERIOR token opens only the ledger path; convictions are ACTS rows, and the gate refuses an INTERIOR token on one |
| **evidence cannot move a conviction** | MECHANICAL | *a loader check the stages do not name:* a verb writing a category-3 field may not phrase its `requires` over the actor's ledger. **Synthesis addition** |
| **a field nothing reads is not a field** | MECHANICAL, weakly — a static-reference scan | **not structural; the honest state** |
| **the ledger is never read by another person** | STRUCTURAL by signature | `person_q` takes the asker; a resolver-side Query over ledgers does not exist and must not be added |

## §B.3 · `Rung` — *the address, never the occupant*

```
Rung := ( id, kind (ORDERED; the ordinal is rank), matter(stores, sites[], records[]), dates[], envelope, exists )
DELETED:  stake (retired, no producer) · judging_set_rule · transmission
NEVER:    any social aggregate — no norms, unrest, legitimacy, reputation, discipline
```

**On the no-social-aggregate rule the synthesis refuses to overclaim:** STRUCTURAL at the type (the
field set is closed and every member is matter or calendar), **CONVENTION at the schema edit** — a
session can add a field. What it cannot do is add one *without* a matrix row, and a `Rung` row whose
writer is `act_only` and whose name is not on the closed matter/calendar list fails the loader.
**MECHANICAL against the accidental case, CONVENTION against the deliberate one.**

Scale is STRUCTURAL-by-absence: there is no field. Branching on a member is CONVENTION + a scan for
`kind ==` against a literal, and the falsifier is exact — *change the roster and see what breaks.*

## §B.4 · `Site` · §B.5 · `Record`

`Site` gates verbs by band on a **fixed-point integer**, so the one-ulp hazard has no representation.
Node-keying is structurally unwritable: a Rung has no condition field, so the collapse cannot be
spelled.

**Synthesis call — `Petition` and `Dispensation` become `Record` kinds.** A petition is a document
that is carried, backed, forgeable and burnable; a dispensation is a signed document learned through
claims. Folding them in means `forge`, `destroy_record`, `hold` and `carry` reach them with no new
rows, and two existence rows collapse into one. **Rejected alternative:** the chain's two separate
non-carriers, each then needing its own existence row and custody semantics while being unreachable
by the verbs the design already has for documents. **Cost:** the nine typed dispensation terms become
a schema for one Record kind and remain unspecified.

## §B.6 · `Proposition`, and why the faction debt closes

Immutable, never destroyed, no setter, no delete. `utterer` is on it because **AX-6 requires a
permanent thing to have an author** — and this is not the attribution T-d forbids, which is about the
*Event*.

> **The chain's standing debt — *territory held by a banner nobody carries* — has no spelling here.**
> With `hold` re-subjected to Person only, the Tenure store's subject type does not admit a
> `PropositionId`. A faction's claim on territory is a `HOLDS` Proposition its members commit to, and
> a person holds the seat. **STRUCTURAL.**

## §B.7 · `Seat` — the chain's `Office`. **There is no `Title` type.**

```
Seat := ( id, post, body?, scope? (null = a cluster), remit(acts[], binds)
        , conferral  -- which ACT fills it: confer by <seat> | determine by <judging seats> | succeed
        , revocation -- which seat may revoke, and the CONJUNCTS
        , upkeep, dates[], exists )
NEVER:   who holds it · who serves it · a modifier of any kind
```

**Three calls, each marked:**

1. **No `Title` type; the revocation rule is data.** An ordinary seat revocable on purview alone and
   a title needing purview + holdings + higher rank are two *values* of `revocation.conjuncts`,
   declared at `establish`. **No `is_title` branch exists anywhere** — ID-4 — which dissolves the
   `__post_init__` collision Stage 1 calls *a symptom marker*.
2. **`establishment` is a Query over `oblige`, not a field.** A set of persons on a seat is two homes
   for one fact. A person joins by `oblige : Person → Seat` and leaves by `release`. A council is one
   seat whose members oblige. **Rejected:** the chain's field, with *establishment size* as a number
   nobody can source; under this reading the size is whatever the holder admits and the upkeep pays.
3. **`judging_set_rule` deleted from `Rung`.** The judging set is *the seats whose remit covers the
   matter at that venue* — a Query over seats, which are arrangements of the political layer, not a
   rule stored on a place.

| invariant | grade | construction |
|---|---|---|
| a seat adds no verb and no modifier | STRUCTURAL | no bonus field; no modifier column; `eligibility_kinds` has no `capability` member and the loader raises on one |
| a seat does not know its holder | STRUCTURAL | no field; `holder_of` is a cache lookup |
| **purview is asked of the seat exercised, not the actor** | MECHANICAL | `Act.via : SeatId?`; every purview walk uses `via.scope`. **A regent has the seat's purview** |
| delegation = `establish` → `confer` → `revoke` | MECHANICAL | three rows the table already has |

## §B.8 · `Tenure` — the one edge, and the three ways it closes

```
Tenure := ( id, kind, subject (THE OWNER), object, since, until?
          , term? (matures_at, declared_by : ActId, closer)   -- T-n. Replaces payload?
          , degree?, conferrer? : SeatId )
tie · knot   DIRECTED     succeed : Person -> Person     hold.subject : Person only
NEVER: deletion.  LIVE: tenures.live(...) is the default iterator; tenures.ended(...) is separate and named
```

| path | authority | step |
|---|---|---|
| **the owner's discretion** (T-m) | `subject == actor`. One verb, `release`, generic over kind | RESOLVE / ACTS |
| **a declared term** (T-n) | the Tenure's own `term`: a `closer` basis exercised by an act, or a `matures_at` MATTER matures with `causes[] = term.declared_by` | RESOLVE, or MATTER |
| **subject or object ceases to exist** | `destroy` sets `until` on every Tenure naming the id **and nothing else** | MATTER (death) or RESOLVE (kill) |

> **Synthesis call, and it resolves a real tension.** #353 says death's `until` is *the only Tenure
> write in the MATTER class* and that *a second such seam means the column is the wrong mechanism.*
> Stage 1's `T-n` — which is later and governs — needs a term of service to end without an act.
> **Read as ONE seam, not two:** §15.3's own words say the seam is *bounded by a CAUSATION rule, not
> by the column*, and the rule generalises from one licensed cause to two — an actorless row may
> write `until` only where its cause is the existence change it also caused, **or** the maturation of
> a term declared by the act that opened this Tenure. Both are causation-bound; both cite an author.
> **Rejected:** routing term expiry through CALENDAR, which makes a term un-endable when nobody acts
> — the exact ratchet `T-n` exists to forbid.

| invariant | grade | construction |
|---|---|---|
| one home, one writer | STRUCTURAL | one store keyed by subject; the object side is a barrier cache |
| **what an act can open, an act can close** (ID-14) | MECHANICAL at load | the loader asserts `release`'s kind domain **equals** `tenure_kinds` |
| no ratchet over ended edges | MECHANICAL | `ended()` is separate; a scan forbids an int-returning `world_q` function from calling it |
| **a symmetric relation with one owner** | STRUCTURAL | `tie`/`knot` are directed; no symmetric kind exists. *I have cut you off and you do not know it* is free |
| **a relation whose subject cannot act** | STRUCTURAL (typed) | the subject type admits `RungId` for `contain` only |

## §B.9 · `Act` · `Scene` · `Event` · `Claim` · **`Receipt`**

```
Act     := ( id, actor : PersonId, via : SeatId?, verb, refs, payload, terms?, scene )
Scene   := ( id, person, occasion : Question, place : RungId, interactions : Act[] )
Receipt := ( id minted BY THE GATE, kind, field, subject id, before, after )
Event   := ( id, kind, changes[] : Receipt[], causes[] NON-EMPTY or [ROOT], emitted_at, degree? )
Claim   := ( id, holder, subject, predicate, value, when, source, confidence, visibility? )
```

**No `actor`, no `target`, no `subject` on `Event` — STRUCTURAL:** the fields do not exist, and
`changes[]` carries the changed things individually, so **the fold has no single field into which to
put the actor.** Place is `place_of(w, event)`.

> ### **`Receipt` IS THE CONSTRUCTION THAT MAKES `ID-9` MECHANICAL**
> `Event.changes[]` is typed `Receipt[]`; **only the gate mints a Receipt**; the log's append asserts
> every receipt id is in the gate's minted set for this tick. **An Event reporting a write the gate
> did not apply fails at append.**

**Synthesis call — `Act` persists.** `causes[]` must name ids already in the log, and the seam's
Events name the acts that caused them; **both cannot hold if the Act is discarded.** Logging the Act
as an Event would put an actor on a witnessed record, which T-d forbids. So `state/acts` is
append-only, **resolver-side**, and no person-side Query reaches it. **Rejected:** discarding Acts and
letting `causes[]` name only occasion Events — which severs every arc at the decision that produced
it, and *an arc is a chain of these links*.

**`Scene` is what the budget counts**, not the Act. `choose` returns `Scene[]` of length ≤ `budget`.

## §B.10–§B.12 · Season-local values, calendar objects, Queries

```
View      := ClaimId[]   -- IDS. STRUCTURAL: a packed int array holds no reference
Sensation := (subsistence, standing)  -- GDScript Vector2 is STRUCTURAL against widening; Python a 2-field tuple is CONVENTION
Refusal   := typed result -- what the seam returns at the depth cap. NEVER a raise
world_q.<n>(w : World, ...)          person_q.<n>(p : PersonInterior, ...)
cache.build(w) at a barrier -> Cache -- built and dropped by the driver
```

**The barrier cache reconciles `T-a` with `ID-1`** exactly as Stage 1 says: *discarded at the next
barrier and therefore cannot go stale.* STRUCTURAL in one respect — the cache is a local of the
driver's step call, so nothing inside a step can hold it past the barrier without the driver handing
it on.

## §B.13 · The data layer, and the loader's eleven invariants

Adopted verbatim from the chain: *would changing this change the GAME, or change how the code works?*
And: *a number that is a property of a roster member travels with the roster; a number standing free
of any roster is a fixture.*

**Two renamings, for idempotence.** `social:` means *only an act may write it*, not *is a social
quantity* — under that name a `(Rung, exists)` row reads as "social: true" while §D.2's whole point is
that a Rung owns nothing social. **Renamed `writer: act_only | world_or_act`.** And `emits:` splits
into `on_write` and `on_condition`, which is what the conditional-emission roster was invented to say
beside it.

**The loader's cross-validation — each an ID-13 or ID-14 check firing at load, not at the first act
that would have hit it:**

1. every `verb.writes` pair is a matrix row · 2. every matrix row with `RES` has ≥1 producing verb ·
3. eligibility kinds ⊆ the roster, **`capability` refused by name** · 4. a verb with a `requires` has
a non-empty `emits_on_refusal` · 5. **`act_only` ⇒ steps ⊆ {RES}; `MAT` ⇒ `world_or_act`** — the
fourth-clock refusal, at load · 6. **`release`'s kind domain == `tenure_kinds`** · 7. the Event-kind
roster is **derived** from every emission column, and the log accepts no other kind · 8. alignment
keys ⊆ axes × verbs, and not all zero · 9. contest prizes ⊆ the subsystem roster ·
10. **unknown keys rejected — a `scale:` key fails the load** · 11. every fixture the code names has
a register row not graded `absent`, or the run refuses **at that site, with the row's id**.

**Grade: MECHANICAL, all eleven.** What stays CONVENTION is a session editing the data to make a
contradiction consistent — **which is a visible diff, and the only honest thing to say.**

---

# PART C · THE SEAMS

## §C.1 · Driver ↔ steps

```
season(w):
  cal  = Token(CALENDAR,t); calendar(w,cal); drop            -- barrier 1
  mat  = Token(MATTER,  t); matter(w,mat);   drop            -- barrier 2 · THE WORLD FREEZES
  cache = cache.build(w); frozen = w.frozen(cache)
  scenes = deliberate(frozen)                                 -- a MAP. No token exists in this scope
  act  = Token(ACTS,    t); resolve(w,act,scenes); drop      -- barrier 3
  cache = cache.build(w)
  intr = Token(INTERIOR,t); witness(w,intr,cache); drop      -- barrier 4
  mat2 = Token(MATTER,  t); census(w,mat2); drop
  t += 1                                                      -- the ONE place the season advances
```

> **The frozen world is STRUCTURAL: no token exists in DELIBERATE's scope, and the gate cannot be
> called without one.**

## §C.2 · The write gate — the seam every mutation crosses

```
gate.write(token, kind, field, id, change) -> Receipt
  row = matrix[(kind,field)]                     or raise Unmarked        -- ID-5 polarity
  token.class in classes_of(row.steps)           or raise WrongStep
  row.writer == act_only => token.class == ACTS  or raise
  (Tenure, until) under MATTER => cause is a death it caused, or this Tenure's declared maturation
  before = get(); store._set(); after = get()                             -- THE GATE APPLIES THE WRITE
  r = Receipt(...); minted[t].add(r.id)
  emit row.on_write; if band(before) != band(after): emit row.on_condition.crossing
```

## §C.3 · DELIBERATE ↔ decision

**In:** a frozen `PersonInterior`, a `View` of ids, two scalars, an int, `Question[]`, and the verb
table's *declarations* — `requires` evaluated as **not known-false from the person's own claims.**
**Out:** `Scene[]`.

`decision/` imports `person_q` and `data/`. **It does not import `state/`, `world_q` or `loop/`.**
STRUCTURAL in a typed build; MECHANICAL by path scan in Python and GDScript.

## §C.4 · RESOLVE ↔ the verb table — the one fold

```
acts = canonical_order(flatten(scenes))     -- (stratum, actor-hash, intra-person position)
for a in acts:
  eligible or emit(row.emits_on_refusal); continue
  row.requires AGAINST THE WORLD ITS PREDECESSORS LEFT
      or emit(row.emits_on_refusal); continue          -- THE SCARCITY CHANNEL
  if row.contests: degree, evs = seam.contest(...)     -- Refusal => emit refusal kind
  receipts = [gate.write(...) for (k,f) in row.writes]
  emit(row.emits, changes=receipts, causes=[a.id]+occasion, degree)
```

| property | construction | grade |
|---|---|---|
| **no second resolver** | the table is data; an inexpressible verb is `grade: absent` and refuses | **CONVENTION** — Stage 1 names this as *the one enforced by a person noticing.* Stated at that strength |
| a refusal emits, never raises | no raise path after eligibility; loader invariant 4 | MECHANICAL |
| obstruction and scarcity need no verb | `confer`'s 1-per-object and `transfer`'s `stores >= amount`, checked against the folded world | MECHANICAL — **and it is why the fold is serial by design** |

> **Synthesis call — a contest is opened by DECLARATION, not by inference.** The fold opens one only
> where the verb row declares `contests: <prize>`. Contention on a subject *without* a declared prize
> is **scarcity** — the second claimant is refused by the fold. **Rejected:** a touch-graph inferring
> contests from write collisions, *which is the regex router in a new dress* and would give an
> undeclared contest to every pair of `work` acts on one site.

## §C.5 · The contest seam

```
seam.contest(proj : ReadOnlyWorld, place, prize, claimants : PersonId[], depth, max_depth)
  depth < max_depth        or return Refusal(depth_cap), []     -- NO DEFAULT. Typed, never a crash
  provider = manifest.resolve("contest", prizes[prize])         -- by string, at boot
  margin   = provider.run(proj, place, claimants, depth+1, max_depth)   -- a MARGIN. Never a winner
  degree   = ladder.degree(margin, veto = provider.veto)        -- ONE ladder; the veto can only demote
```

| the four crossings | construction |
|---|---|
| the call | `World` first — **STRUCTURAL that `choose` cannot make it** |
| the persons, read never written | **a read-only projection and NO TOKEN** — the wrapper has nothing to write with |
| Events back | the same `log.append`, same invariants; an unregistered kind fails |
| the degree | the subsystem returns a `Margin`; **a subsystem returning a winner has not met the contract** — a type assertion |

The five leaks: a state write from inside — **no token, STRUCTURAL**; a second resolver — CONVENTION;
a faction as combatant — `claimants : PersonId[]`, STRUCTURAL; a subsystem event family — the derived
roster, MECHANICAL; a widened outcome — `veto : bool` and the ladder takes the minimum, **STRUCTURAL
by signature.**

## §C.6 · WITNESS ↔ the ledgers — attribution is per channel, per witness

**Synthesis call, and it is the mechanism `T-d` needs.** The Event has no actor. A witness who was
*present* saw who did it; a witness who *holds the changed document* saw only that it changed. **So
the claim shape is a property of the channel**, declared in data beside its predicate:

| channel | mints |
|---|---|
| `co_located` | the change claims, `firsthand` — **and**, if `causes` names an Act, an attribution claim read from the act store |
| `document_key` | **the change claims only. No attribution** |
| `witness_key` | change claims about self; via a knot, the partner's deposits, reusing the event id |
| `post_remit` | the change claims, `inferred` |
| `chronicle` | the change claims, `told_by` |

> **Covert action then needs no flag:** an act performed where nobody is co-located has **no
> `firsthand` attribution anywhere**, and false attribution is a `tell` carrying a claim whose subject
> is the wrong person. **Rejected:** a global claim-subject rule, which gives a document holder an
> attribution they could not have seen.

## §C.7 · CENSUS ↔ demand

Stage 1 resolves individuation as demand-driven. **The stages do not say what a demand IS**, and the
synthesis assumes the smallest shape that preserves the derivation: **a demand is a refusal Event**,
which a verb declares when its `requires` names a person who is not individuated. CENSUS reads that
kind once and individuates from the envelope with `causes[]` naming the refusal. **The absence of a
fourth clock stays CONVENTION**, as the chain already says.

## §C.8–§C.10 · Data, the log, and the Godot boundary

A value lives in one file, read by one loader, so *never in prose and never in two files* is a fact
about the import graph. `append` asserts: unique id · registered kind · non-empty causes · every
cause in `log ∪ acts ∪ {ROOT}` · non-decreasing season · **every receipt in the gate's minted set** ·
and that the record type has no actor, target or subject field.

**Godot, with the degradations named rather than glossed:** `core/` has no `Node`; `World` is
`RefCounted`, never an autoload. **No private constructors** (tokens: scan). **No module system**
(`decision/` isolation: path scan). **No exceptions** (typed results everywhere; a refusal is a
value). **Recursion depth is a crash** (`max_depth`, no default, typed refusal at the cap).
`Vector2` is float32. **Fixed point for `condition`, `stores`, `margin`.**

---

# PART D · WHAT IS STRUCTURALLY IMPOSSIBLE, BY CONSTRUCTION

**A row graded MECHANICAL or CONVENTION is here because the reader will assume it is structural, and
the assumption is the failure mode.**

| # | the defect | the construction | grade (Py / GD) |
|---|---|---|---|
| 1 | **an institution acts** | a faction has no type and no id; `Act.actor : PersonId`; no institution parameter anywhere; a seat enters only through `Act.via` | STRUCTURAL / MECHANICAL |
| 2 | **a decision reads world truth** | `choose` has no `World`; `decision/` cannot name `state/` or `world_q`; `View` holds ids; `PersonInterior` is a frozen copy | STRUCTURAL / MECHANICAL |
| 3 | a write outside the matrix | one path; an unmarked cell raises; no public setters | MECHANICAL |
| 4 | a write at the wrong step | tokens; the gate matches class to row | MECHANICAL / CONVENTION + scan |
| 5 | **a success Event for a write that did not happen** | `changes[] : Receipt[]`; only the gate mints; append checks the minted set | MECHANICAL |
| 6 | a causal orphan | non-empty by constructor; `ROOT` typed; integrity over `log ∪ acts` | STRUCTURAL at the constructor |
| 7 | a refusal that raises | the failure path is `emit`; loader invariant 4 | MECHANICAL |
| 8 | a stored aggregate | no field slot; a Query is a function; a cache is driver-local | STRUCTURAL at the type; CONVENTION at a schema edit |
| 9 | **an Event with an actor, target or subject** | the fields do not exist; `changes[]` is plural | STRUCTURAL |
| 10 | two homes for one relation | one store keyed by subject; the object side is a cache | STRUCTURAL |
| 11 | a seat that knows its holder | no field | STRUCTURAL |
| 12 | **a relation with two owners** | directed `tie`/`knot`; no symmetric kind exists | STRUCTURAL |
| 13 | a relation whose subject cannot act | `subject` admits `RungId` for `contain` only | STRUCTURAL (typed) |
| 14 | **a banner holding territory** | `hold`'s subject is `PersonId` | STRUCTURAL (typed) |
| 15 | **open-without-close in the vocabulary** | `release` generic; the loader asserts its domain equals `tenure_kinds` | MECHANICAL at load |
| 16 | a ratchet over ended edges | `ended()` separate; a scan forbids int-returning callers | MECHANICAL |
| 17 | a fourth clock | the MATTER token; loader invariant 5 | MECHANICAL at load |
| 18 | evidence moving a conviction | INTERIOR cannot reach an ACTS row; the ledger-phrased-`requires` loader check | MECHANICAL |
| 19 | **a default contest depth** | `max_depth` has no default in the signature | STRUCTURAL |
| 20 | a nested contest that crashes | the cap returns `Refusal` | MECHANICAL; **in GDScript the test must actually reach the cap** |
| 21 | a container with a clock | carriers have no behaviour; only the driver calls a step; `t` advances in one line | STRUCTURAL by absence of a method |
| 22 | a subsystem writing state | no token crosses the seam; the projection is read-only | STRUCTURAL / MECHANICAL |
| 23 | a subsystem widening an outcome | `veto : bool`; the ladder takes the minimum | STRUCTURAL by signature |
| 24 | a subsystem returning a winner | the return type is `Margin` | MECHANICAL |
| 25 | *a subsystem-specific Event family* | ⚠ **TRUNCATED MID-SENTENCE BY THE RATE LIMIT** | — |

> ### ⚠ **THE DOCUMENT ENDS HERE.**
> **PART E (the build order) and PART F (where the three stages are insufficient) were commissioned
> and never produced.** See the notice at the head of this file. **Do not treat the absence of a
> §F as the absence of gaps** — the synthesis marks assumptions inline throughout and forward-
> references a §F that does not exist at `§F.1`, `§F.4`, `§F.5`, `§F.6`, `§F.7` and `§F.15`.
> **Those six dangling references are the known-incomplete set, and there may be more.**
