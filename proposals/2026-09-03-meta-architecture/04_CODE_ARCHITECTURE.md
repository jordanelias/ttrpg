# META-ARCHITECTURE — STAGE 4 · CODE SHAPE, TYPES, SEAMS, IMPOSSIBILITIES

## Status: **PROPOSED (2026-09-03). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE. Nothing here runs.**
## Produced by a **read-only** Fable 5.1 synthesis holding Stages 1–3 in context. Concrete shapes taken
## from, amended against, or rejected from the chain (#353 `ARCHITECTURE.md`, `ARCHITECTURE_V2.md`,
## the three YAML files). **Nothing under `canon/`, `systems/`, `research/` or `engine/` was read.**
## ⚠ **AMENDED 2026-09-03 (Jordan-directed, `10_FACTIONS_AND_DEPLOYMENT.md`)** — §B.6.1 `Faction` as a
## Query return · §C.5.1 the roster contract · **D-18 upgraded, D-47..D-51 added, D-1/14 reconstructed
## and the STRUCTURAL count corrected** · F.23 narrowed, F.32–F.33 opened · **§G.2.8**, the general rule.
## ⚠ **REV. 3, 2026-09-03** — `Tenure.conferrer` **deleted** (§B.8) · `T-o` added to §B.8's closing
## paths · `PART D` **27a** (content-layer proper-noun scan) and **41a** (`DELIBERATE` permutation
## falsifier), **30b** amended · **§G.2.9** the procedure/order criterion · `F.28` amended and `§F.34`
## given the two items that sat in neither register · three stale counts corrected. **See `README.md`.**

---

> # ⚠ **REWRITTEN 2026-09-03 (rev. 2). WHAT CHANGED AND WHY, BEFORE ANYTHING ELSE.**
>
> **A read-only adversarial pass over this document, the executable chain (#357) and an independent
> governance design (#359) found TWENTY defects. Fourteen are in this document.** Every change below
> is marked in place with its finding id; nothing is overwritten silently, because *a superseded
> derivation that stays legible is how the next session avoids re-deriving it.*
>
> | | the defect | where |
> |---|---|---|
> | **F3** | **the gate never checks `subject == actor`** — `AX-4`'s second clause was enforced by per-verb eligibility alone, and two live verbs write another person's `Tenure.until` | `§C.2`, `§B.8`, `PART D` |
> | **F6** | **a LOST contest still writes.** `writes:` is unconditional, so `kill / wound` kills on any degree; `Event.degree` has no reader in four stages | `§C.4`, `§B.9` |
> | **F4** | **loader invariant 6 is unsatisfiable.** `release`'s domain is `tenure_kinds`, which contains `contain`, whose subject can never act | `§B.13`, `PART E` step 6 |
> | **F5** | **build step 2 undercounts its own failure ~4×** — nine matrix rows have no producing verb, not two, and four of them are `Person` interior fields | `PART E` step 2, `PART F` |
> | **F9** | **`STRUCTURAL` is claimed where only a checker or a scan exists**, and the count of structural rows is a hand tally its own `G.3.3` forbids | `PART D` |
> | **F8** | **this document forbids the ledger read two live verbs need** | `§B.2`, `§C.3` |
> | **F10** | **`PART D` row 1 contradicted `§D.11`** — "a faction has no type and no id" versus a declared `Faction` view type. ⚠ **FOUND TWICE, INDEPENDENTLY, AND `origin/main` GOT THERE FIRST WITH A BETTER ANSWER.** PR #360 folded the faction amendment into Stage 4 as `§B.6.1` and rewrote the row on a stronger ground than this pass had: not *"the type exists after all"* but ***"you cannot pass a `Faction` where a `PersonId` is required, and there is nothing to pass it to."* The merge takes main's text.** Two adversarial passes on disjoint branches converging on one row is the corroboration signature `G.4.3` wants | `PART D` — **resolved on main** |
> | **F7** | `F.1`'s demand needs a per-conjunct refusal kind the fold cannot emit | `§C.7`, `PART F` |
> | **F13** | the live fold mints **three Event kinds no column declares**, which invariant 7 would refuse | `PART F` |
>
> **What #359 contributed, and it is one thing rather than the two the cross-read claimed:** the
> **degree-keyed consequence column** (`§C.4`, `§A.1`). It was filed as mere corroboration of `T-k`
> and is not — it exposes `F6`, gives `Event.degree` its reader, gives the four `Person` interior
> rows a producer, and gives `H-98` the shape of its missing mapping. **Everything else it offered
> was already derivable here, and one thing the cross-read graded as its own gap was not a gap.**
>
> ---
>
> # COMPLETE — PARTS A THROUGH G
>
> **PART G is the durable one, and the one to read first.** A–F describe how *this* design came out;
> **G says how design proceeds going forward** — shape · organize · articulate · orchestrate, kept
> apart because collapsing them into the word *architecture* is itself the failure. Its one sentence:
>
> > **Derive the shape from the axioms WITH THE TREE CLOSED; decompose it by WHO WRITES WHAT; write it
> > in a form A LOADER OR A FALSIFIER CAN EVALUATE; and close a stage ONLY ON REPRESENTATIONS.**
>
> **Every rule in G names the corpse that would return if it were dropped**, and it ends by saying
> that a rule with no corpse behind it should be deleted.
>
> **PART F is the section to read second.** It carries thirty-three gaps, and its closing finding is
> about this exercise rather than about the architecture: **the architecture is derived through
> Stages 1 and 2 and ASSUMED through Stage 3.** Stage 3 states its subjects as properties without
> representations, which is where the gap density is.
>
> ⚠ **Two gaps block the build outright.** `F.20` — nothing founds a hearth or builds a site, so
> **the world only decays** — fails the loader at build step 2. `F.24` — every verb's `requires` is a
> **prose string**, so evaluating it needs a body per verb, and *the resolver has no body* returns as
> **the resolver has thirty**.

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

⚠ **AND THE FIRST PUBLICATION BROKE ITS OWN RULE, WHICH IS `F9`.** Several `PART D` rows read
**"STRUCTURAL (typed)"** with **no checker named**, in a Python build that has no enforced type
checker — while `§B.1`'s very first row honestly concedes *"STRUCTURAL under a checker; MECHANICAL at
runtime"* for the same class of claim. **The concession is the correct form and it is now applied
uniformly.**

> ### **THE RULE, STATED SO THE COLUMN CANNOT DRIFT AGAIN**
> **`STRUCTURAL` means the defect HAS NO SPELLING in the target language as built.** A property that
> holds only when an optional checker is run is **`STRUCTURAL under a checker · MECHANICAL at
> runtime`**, written out, both halves. **If the build does not run the checker in CI, the runtime
> grade is the real one.**

⚠ **AND THE COUNT IS DELETED RATHER THAN CORRECTED.** The closing note said *"of forty-six rows,
sixteen are STRUCTURAL in Python"*. An independent recount reached **22 rows with a structural
component**, and the discrepancy is not the point — **`G.3.3` forbids a count typed by hand**, and
this one had no stated counting rule, so neither figure is reproducible. **The ratio claim now names
the rule instead of the number:** count the rows whose grade column contains no `CONVENTION` term and
names no scan, and report it with the command.

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
| **the ledger is never read by ANOTHER person** | STRUCTURAL by signature | `person_q` takes the asker. ⚠ **CORRECTED (F8): the first wording said a resolver-side Query over ledgers *"does not exist and must not be added"*, and that forbids what two live verbs require.** `tell`'s precondition is *"the teller holds a claim on the subject"* and `comply`'s is *"a claim of the dispensation's terms is in the actor's OWN ledger"* — both evaluated at RESOLVE. **The carve-out is exact and it is not a widening: the fold may ask the ACTOR'S OWN ledger, through the `PersonInterior` snapshot the act carries, and no other.** A Query taking a ledger and an asker who is not its holder still does not exist |

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

### §B.6.1 · ⚠ **AMENDED — `Faction` IS A TYPE, AND IT IS A QUERY RETURN** (Jordan, 2026-09-03)

The paragraph above is right about **ownership** and was wrong about **deployment**: it left every
consumer — the battle seam, the squad grid, the UI, the AI — to recompute a set nobody had named.

```
Faction := ( proposition : PropositionId   -- identity. Immutable, uttered by a named person (AX-6)
           , members     : PersonId[]      -- live `commit` edges
           , holdings    : RungId[]        -- the union of members' `hold` objects
           , seats       : SeatId[]        -- the seats members hold
           , head?       : PersonId )      -- by the proposition's own rule. Input is F.4
faction_q.resolve(w, prop) -> Faction      -- built at a barrier, handed on, dropped at the next
NEVER: a member of `World` · a field of its own · `Act.actor` · a `contest` claimant · a `hold` subject
```

**It is the barrier cache's shape, not a new mechanism** — which is why it costs nothing and cannot
go stale. **A stored roster drifts from the commit edges and needs a reconciliation pass; a resolved
one IS the edges.**

| what changed | what did **not** |
|---|---|
| `holdings(faction)` is a **named Query**, so faction territory is first-class to *ask for* | `hold.subject` is still `PersonId` — D-14 is untouched, and the banner still holds nothing |
| code holds a real object with real rosters | it has **no verbs**, and `resolve` still has **no faction parameter** |

> **THE PRICE, AND IT IS REAL.** *A faction cannot gain a field* was previously STRUCTURAL **by
> absence of a type**. A type now exists, and that guard drops to **the view's lifetime** — see D-47.
> This is the only grade in Part D that the amendment weakens, and it is recorded rather than absorbed.

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

## §B.8 · `Tenure` — the one edge, the three DECLARED ways it closes, and the existence cascade

```
Tenure := ( id, kind, subject (THE OWNER), object, since, until?
          , term? (matures_at, declared_by : ActId, closer)   -- T-n. Replaces payload?
          , degree? )
tie · knot   DIRECTED     succeed : Person -> Person     hold.subject : Person only
NEVER: deletion.  LIVE: tenures.live(...) is the default iterator; tenures.ended(...) is separate and named
```

| path | authority | step |
|---|---|---|
| **the owner's discretion** (T-m) | `subject == actor`. One verb, `release`, generic over kind | RESOLVE / ACTS |
| **a declared term** (T-n) | the Tenure's own `term`: a `closer` basis exercised by an act, or a `matures_at` MATTER matures with `causes[] = term.declared_by`. ⚠ **The basis resolves against the Seat** — `Seat.revocation` is authoritative and `term.closer` names a basis, not a second authority (Stage 1 `§E.1.2` asks that this be said at both sites) | RESOLVE, or MATTER |
| **a revocation on the seat** (T-o) ⚠ **ADDED — and the count needs saying, because two readings of *three* were in circulation.** This table's three were `T-m`, `T-n` and the cascade; Stage 1 `§E.1.2`'s three are the **declared** ways — `T-m`, `T-n`, `T-o` — with the cascade filed separately as an existence change. **The type section was one short of Stage 1's set and the heading hid it** | the **Seat's** `revocation` basis, exercised through `Act.via`, refused the instant the occupant is not seated. **`PART D` row 10a already gates it; the type section never named it** | RESOLVE |
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
| **what an act can open, an act can close** (ID-14) | MECHANICAL at load | the loader asserts `release`'s kind domain equals `tenure_kinds \ {contain}` ⚠ *(this cell and `D-15` both said **equals `tenure_kinds`** after invariant 6 was corrected for F4 — `contain`'s subject can never act, so the unqualified form is unsatisfiable. Corrected 2026-09-03)* |
| no ratchet over ended edges | MECHANICAL | `ended()` is separate; a scan forbids an int-returning `world_q` function from calling it |
| **a symmetric relation with one owner** | STRUCTURAL | `tie`/`knot` are directed; no symmetric kind exists. *I have cut you off and you do not know it* is free |
| **a relation whose subject cannot act** | STRUCTURAL (typed) | the subject type admits `RungId` for `contain` only |

> ### ⚠ **`conferrer? : SeatId` IS DELETED — `ID-13` ADMITS NO THIRD STATE, AND THIS FIELD HAD NO
> ### READER ANYWHERE IN THIS EXERCISE (added 2026-09-03)**
> It was declared here and **read nowhere in the whole exercise** — the same defect as `degree?`, on
> the same line, and `degree?` was in the hole register (`§F.4`) while this was in neither the
> register nor `§F.34`'s not-a-gap list. **The register works; it was not run across the line it was
> written on.**
>
> **Deletion rather than a reader, and the derivation is short.** Who may end a hold is answered by
> `Seat.revocation` (`T-o`) — the *revoking* seat's declared remit, not the *conferring* seat's
> identity — so the revocation path never asks this question. What conferred the Tenure is already
> carried, once, by the opening `Act`: its `actor` and its `via : SeatId?`, in an append-only log with
> `causes[]`. **A field on the Tenure would therefore be a second home for a fact the act already
> holds** — `ID-2`, and `G.2.1`'s *you can name two* firing inside the schema exactly as `§E.1.2` says
> it does for `Seat.revocation` and `term.closer`.
>
> ⚠ **The reader an outside evaluation offered is REFUSED, and refusing it is the point.** It proposed
> patronage — *who raised whom*, so that a patron's fall exposes their clients. That is a
> **person→person** relation hung off a **seat** pointer, which is a type mismatch before it is
> anything else — and `§E.2.2` is what makes it visible: **authority is a property of the seat, and
> patronage is not authority.** Who raised whom is a fact about two people, and it survives the
> abolition of every seat either of them ever held. If that graph is wanted it is an `oblige` edge
> between the raiser and the raised, owned by its subject, and it needs nothing on `Tenure`. **`ID-13` says
> find a reader or delete; it does not license finding the wrong one.**

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
faction_q.resolve(w, prop) -> Faction -- §B.6.1. A VIEW: same lifetime rule as the cache
faction_q.at_war(w, a, b) -> bool     -- over live `commit`s to a WAR Proposition. NEVER a stored flag
cache.build(w) at a barrier -> Cache -- built and dropped by the driver
```

**The barrier cache reconciles `T-a` with `ID-1`** exactly as Stage 1 says: *discarded at the next
barrier and therefore cannot go stale.* STRUCTURAL in one respect — the cache is a local of the
driver's step call, so nothing inside a step can hold it past the barrier without the driver handing
it on.

> **`Faction` inherits that property whole, and this is the whole of its defence.** It is a return
> value, never a member of `World`; a field set on one is dropped with the view. **The lifetime rule
> is doing the work that the absence of a type used to do** — which is weaker, and is why D-47 exists.

## §B.13 · The data layer, and the loader's twelve invariants

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

1. every `verb.writes` pair is a matrix row — **for every `Degree` branch of a degree-keyed verb** ·
2. every matrix row with `RES` has ≥1 producing verb ·
3. eligibility kinds ⊆ the roster, **`capability` refused by name** ·
4. **every failable clause has a refusal kind** — ⚠ **WIDENED (F7)**: not only a verb with a
`requires`, but each **conjunct** of it, and any eligibility alternative that can decline. The first
wording covered `requires` alone and was satisfied by luck, because every verb with no `requires` is
`own`, which cannot fail ·
5. **`act_only` ⇒ steps ⊆ {RES}; `MAT` ⇒ `world_or_act`** — the fourth-clock refusal, at load ·
6. ⚠ **CORRECTED (F4): `release`'s kind domain == `tenure_kinds \ {contain}`**, and **every kind's
OPENER set is declared too** (`ID-14`'s added half) ·
7. the Event-kind roster is **derived** from every emission column, and the log accepts no other kind ·
8. alignment keys ⊆ axes × verbs, and not all zero · 9. contest prizes ⊆ the subsystem roster ·
10. **unknown keys rejected — a `scale:` key fails the load** · 11. every fixture the code names has
a register row not graded `absent`, or the run refuses **at that site, with the row's id** ·
12. ⚠ **NEW (F6): a verb declaring `contests:` has a `Degree`-keyed `writes`, and one without it does
not** — the two shapes are not interchangeable and a flat list on a contested verb is the `kill`
defect at load.

> ### ⚠ **F4 · WHY INVARIANT 6 WAS UNSATISFIABLE, AND IT WOULD HAVE FAILED THE BUILD AT STEP 2**
> `tenure_kinds` is `[hold, contain, commit, oblige, succeed, tie, knot]` — **`contain` is in it.**
> `release`'s eligibility is `own`, which means `subject == actor`; `contain`'s subject is a `Rung`;
> **`AX-1` says a Rung can never act.** So the invariant demanded a `release` declaration for a kind
> no actor can ever exercise — a declared row that reaches no caller, which is `ID-13` **created by a
> loader invariant.** Build step 6's proof, *"`release` closes a Tenure of every kind"*, was
> unsatisfiable as written.
>
> **`contain` is the honest exception and Reading 05 already said so** — *"`contain` is `Rung → Rung`,
> subject cannot act, and it is correctly not something anybody ends by choice; it moves when a person
> moves."* The invariant now says what the ontology already said.

⚠ **AND INVARIANT 11 IS NOT A LOAD CHECK.** It refuses *"at that site"* — at the first call reaching a
fixture — which is run-time. **Eleven of the twelve fire at load** ⚠ *(this read TEN, which was
correct of eleven invariants and was not re-counted when the twelfth landed — corrected 2026-09-03
in the same pass as the heading)*. **It is listed here because it belongs to
the same discipline and it is graded separately**, rather than left to imply a guarantee the loader
does not give.

**Grade: MECHANICAL, all twelve.** ⚠ *(This said ELEVEN while the list above had already grown to
twelve — the F6 invariant landed on 2026-09-03 and neither the heading nor this line was re-counted.
Corrected 2026-09-03.)* What stays CONVENTION is a session editing the data to make a
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
gate.write(token, kind, field, id, change, actor?, via?) -> Receipt
  row = matrix[(kind,field)]                     or raise Unmarked        -- ID-5 polarity
  token.class in classes_of(row.steps)           or raise WrongStep
  row.writer == act_only => token.class == ACTS  or raise

  -- ⚠ F3 · AX-4 CLAUSE 2, ENFORCED HERE FOR THE FIRST TIME
  kind is Tenure => one of:
      actor == subject(id)                                   -- T-m, the owner's discretion
      cause is this Tenure's declared `term` maturation       -- T-n
      via is a Seat whose `revocation` basis reaches it       -- T-o, and `via` MUST be present
      cause is an existence change this same act caused       -- destroy's cascade
    otherwise                                                 raise NotYours

  before = get(); store._set(); after = get()                             -- THE GATE APPLIES THE WRITE
  before == after                                or raise NoOpReceipt     -- ⚠ F9 · see PART D row 5
  r = Receipt(...); minted[t].add(r.id)
  emit row.on_write; if band(before) != band(after): emit row.on_condition.crossing
```

> ### ⚠ **F3 · WHAT THIS FIXES, AND IT IS THE LARGEST DEFECT IN THE FIRST PUBLICATION**
> **`AX-4` says the owner is the value's ONLY writer. The gate never checked it.** It matched the
> row, the token class and the `writer:` column — all three about *which STEP may write* — and
> **nothing about WHO.** Ownership was enforced by per-verb eligibility, which is `CONVENTION`, in
> the document whose `PART D` row 10 claims *"two homes for one relation — STRUCTURAL"*.
>
> **The tree shows what that costs.** `verb_table.yaml` has `revoke` (`remit:revoke`) and `confer`
> (`remit:confer`) **both writing `Tenure.until` on an edge whose subject is somebody else**, and
> `kill / wound` writing `Tenure.until` on the victim's edges. Under the first gate all three are
> lawful and none is declared as an exception.
>
> **`T-o` (Stage 1 `§E.1.2`) is what makes the third case lawful rather than merely tolerated**, and
> the `via` requirement is what makes it checkable: **a revocation with no seat in `Act.via` is
> refused at the gate**, so "a superior may revoke" cannot degrade into "anyone with a remit string".

⚠ **`NoOpReceipt` IS `ID-9` MADE MECHANICAL, AND `ID-9`'S OWN WORKED EXAMPLE SURVIVED WITHOUT IT
(F9).** `PART D` row 5 claimed to make *a success Event for a write that did not happen* unwritable,
by checking that every receipt was minted by the gate. **A receipt with `before == after` IS minted by
the gate** — so `work` emitting `site.worked` while accumulating no delta, which is the instance
`ID-9` is written from, passes the check unchanged. **The append-side test could not observe the
failure it excludes; the write side can.**

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
  eligible or emit(row.refusal_for(ELIGIBILITY)); continue
  (ok, failed_conjunct) = eval(row.requires, world_as_predecessors_left_it)
  ok or emit(row.refusal_for(failed_conjunct)); continue   -- THE SCARCITY CHANNEL · ⚠ F7
  degree = FULL
  if row.contests: degree, evs = seam.contest(...)         -- Refusal => emit refusal kind
  receipts = [gate.write(..., actor=a.actor, via=a.via)
              for (k,f) in row.writes_at(degree)]          -- ⚠ F6 · DEGREE-KEYED
  emit(row.emits, changes=receipts, causes=[a.id]+occasion, degree)
```

> ### ⚠ **F6 · `writes_at(degree)` IS THE ONE THING #359 CONTRIBUTED, AND IT WAS FILED AS A
> ### CORROBORATION FOR A DAY BEFORE ANYBODY NOTICED WHAT IT EXPOSED.**
>
> **The defect.** Stage 3 `§A.1` fixes a verb at **five columns** — who may attempt it, what must
> hold, what it writes, what it emits, what it emits on refusal. **None of the five is conditional on
> the outcome.** So the fold above ran `row.writes` **unconditionally after resolving a contest**,
> and the live table proves the cost: `kill / wound` declares `contests: the body` and
> `writes: [Person.body, Person.exists, Tenure.until]`. **Losing the fight kills you exactly as
> winning it does.**
>
> **The second half of the defect is quieter and worse.** `Event.degree?` is declared in `§B.9` and
> **read nowhere in four stages** — `ID-13`, in the same type block that carried
> `Tenure.conferrer` until it was deleted for the identical reason (§B.8). A degree that no
> consequence consumes is not a weak outcome model; **it is a resolution
> whose result is discarded.** The tracer already lives it: the live seam records `contest.resolved`
> with `changes=[]` because *"turning 'p_low won' into 'p_mid died' is the mapping nobody has made."*
>
> **The repair, and it is an AMENDMENT to `§A.1` stated as one.** A verb with `contests:` declares
> `writes` **as a map from `Degree`**, not as a list:
>
> ```
> writes:                      # a verb with no `contests:` keeps the flat list
>   Overwhelming: [Person.exists, Person.body, Tenure.until]
>   Success:      [Person.body, Tenure.until]
>   Partial:      [Person.body]
>   Failure:      []           # ⚠ AN EMPTY LIST IS LAWFUL HERE AND NOWHERE ELSE
> ```
>
⚠ **AND THE BAND NAMES ABOVE ARE ILLUSTRATIVE, NOT A ROSTER — RULED 2026-09-03.** Jordan:
> *"kill/wound degrees should be directly taken from scene combat, which is what actually needs to
> be called when kill/wound is considered."* **The degree is READ OFF THE SUBSYSTEM, never mapped
> onto it by the table.** A contested verb's branches are named by what its subsystem can actually
> distinguish, and where the subsystem distinguishes fewer states than a four-band ladder, **the
> verb declares fewer branches rather than the table inventing the difference.** The live instance
> is exactly this: personal combat separates *felled* from *unresolved* and grades the second by
> wound count, so `kill / wound` carries **three** branches and the fourth is registered as having
> no source in the data.
>
> **That is `T-k` holding rather than bending.** One ladder still reads the margin; what this says
> is that a verb may not declare a band its subsystem cannot report, which is `ID-5`'s polarity
> applied to the outcome column — absence refuses, it does not default to a full write.

> **`Failure: []` is the only place in this architecture where writing nothing is correct**, and it is
> correct because the act still **emits**: the fold reaches `emit(row.emits, …, degree)` with an empty
> receipt list, so the attempt happened, was witnessed, and cost a scene. **That is the difference
> between a refusal (the precondition failed, no contest occurred) and a loss (the contest occurred
> and went against you)** — two outcomes the five-column table could not tell apart.

> ### ⚠ **AND `emits` KEYS THE SAME WAY — FOUND BY APPLYING THIS SECTION TO THE LIVE TABLE, 2026-09-03.**
> Keying only `writes` is half the repair, and the missing half is the more dangerous one. With
> `kill / wound`'s bands landed and its `emits` still flat, **a wound emitted `person.died`** — the
> verb whose own name carries the distinction reporting the wrong one, on every band. That is
> `ID-9`'s class *inside the epistemic layer*, where WITNESS then mints a claim from it and every
> ledger in the world records a living man as killed.
>
> **A degree changes what happened AND what is reported, and the second is what other people act
> on.** So both columns key on the band, and the loader asserts **the two key sets are equal** — a
> band in one and not the other is an outcome that either changes the world silently or reports a
> change it did not make.
>
> ⚠ **The kinds for it were already declared.** `write_matrix.yaml`'s `Person.body` row carries
> `body.changed` · `person.died`; the verb table used one of them for both outcomes. **This was a
> transcription defect, not a design gap** — which is the third time in this chain that a column
> was honoured and its content quietly collapsed.

⚠ **THIS IS A SIXTH AND SEVENTH COLUMN, AND `§A.1` SAYS A VERB NEEDING MORE COLUMNS IS ONE THE
DESIGN HAS NOT FINISHED THINKING ABOUT.** That rule stands and this is the exception it warns about, so it is stated
at full strength rather than smuggled: **the sixth column exists only for verbs that declare
`contests:`, it is a re-keying of the third column rather than a new kind of thing, and any verb
without `contests:` is refused if it uses it.** A seventh column has no such argument available.

> ### **AND IT IS WHY `T-k` SURVIVES CONTACT WITH #359 RATHER THAN LOSING TO IT.**
> #359's own principle is *"every consequence table is keyed by `Degree` and by nothing else"*, with
> the generator private to each scale. **The keying is right and the privacy is wrong** — one ladder
> in the seam is `T-k`, and a per-scale generator is the second ladder `T-k` refuses. **Take the
> column; refuse the placement.**

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

### §C.5.1 · ⚠ **THE ROSTER CONTRACT — added 2026-09-03, and it is a STATEMENT, not a new mechanism**

Stages 1–3 said *a read-only projection* and stopped, leaving the roster's stability implicit. Made
explicit:

> ### **THE SIDES ARE RESOLVED ONCE, AT THE SEAM BOUNDARY, AND HELD FOR THE CONTEST'S DURATION.**

```
sides = (faction_q.resolve(proj, A), faction_q.resolve(proj, B))   -- ONCE, before provider.run
units = PersonId[] at weight            -- one type. There is NO unit class, at any scale
stakes = holdings + seats               -- what a defeat can cost, already typed
```

| | |
|---|---|
| **why it must be stated** | otherwise an implementer hands the wrapper a live world and a unit changes side mid-battle **because somebody repudiated three duchies away** |
| **why it costs nothing** | `proj` is built at the barrier and `commit` edges move only through an Act — so re-resolving *from the projection* returns the identical roster. **The freeze is a consequence, not an addition** |
| **what it actually forbids** | handing the wrapper anything that is not the projection. That is the whole content of the contract |
| **grid squad combat** | the same thing one scale down — the squad is `members ∩ present-at-rung`, resolved once, every combatant a `Person` |

⚠ **In GDScript the consequence does not hold for free.** `proj` there is a reference to live objects
unless it is actually copied, so the guarantee Python gets from the snapshot **must be bought with a
copy or a lock**. See D-49, which is the one row in Part D whose Python and GDScript grades diverge
for this reason.

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

## §C.11 · ⚠ **THE EXPLANATION CONTRACT — added 2026-09-03. There is no referee, so the engine inherits the referee's SECOND job**

`CLAUDE.md` opens with *"There is no GM — the engine resolves everything."* Four stages read that as a
**constraint on authoring** — every rule must be evaluable, nothing may be adjudicated. **It is also
an obligation**, and removing the referee does not remove the question the referee answered: *why did
that happen?*

⚠ **THE OBVIOUS FORMULATION IS WRONG AND MUST BE REFUSED BY NAME.** *"The player is not an actor, so
`AX-2` does not reach them"* fails immediately: **the player CONTROLS a person.** For an NPC, `choose`
is the decision procedure; **for a player character the player IS the decision procedure**, so
anything shown before they declare is shown *inside a decision* in the only sense `AX-2` cares about.
A split on **who is looking** breaches the axiom.

> ### **THE SPLIT THAT HOLDS IS ON WHAT IS SHOWN.**
> **The engine owes the ARITHMETIC of what the character already holds, and nothing else.**
>
> | | |
> |---|---|
> | **what the person holds** | `AX-2`, absolutely. The `View` is `ClaimId[]`; nothing is added and no resolver-side Query becomes visible |
> | **why what they hold says what it says** | ⛔ **not information about the world.** It is the derivation of a value the character already has, and displaying it adds no world truth |

**The signature, and it is what keeps the contract from widening:**

```
explain(p : PersonInterior, v : Value) -> Derivation      -- person_q. NO World parameter.
```

**By `T-f` it cannot reach `World`**, so it cannot explain a resolver-side Query even by accident.
**And it may NOT walk `causes[] → state/acts → Act.actor`** — that path reaches the attribution `T-d`
forbids, is resolver-side, and `F.13` grades its guard `CONVENTION`. The derivation is assembled from
the holder's own `Claim` rows — their `source`, `confidence` and `when` — and from nothing else.

**Hidden actors are hidden in their EXISTENCE, never in their ARITHMETIC.** *"Subsistence fell by 1
from a cause you cannot name"* is admissible, because the character can already see the fall; what
they are additionally given is that it has an author they do not know. **A preview naming the author
is a breach; one saying the effect is unattributed is not** — and the second is what makes
investigation worth a scene.

⚠ **WHAT THIS DOES NOT CLOSE, said because a cross-read claimed it did.** Reading 09 `§2.2`'s revolt
Query is **resolver-side by construction** — *"the mayor does not know how bad it is"* — and this
contract does not reach it. A mayor who holds claims about three angry guilds is owed the sum of
**those claims**; a mayor who holds nothing is owed nothing. **The decomposition is admissible exactly
to the extent the character's own ledger already names its terms**, which is a narrower promise than
the one #359 makes and the only one `AX-2` permits.

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
| 1 | **an institution acts** | ⚠ **CONSTRUCTION AMENDED, GRADE UNCHANGED (§B.6.1).** A faction now *has* a type. What carries the row is that the type has **no verbs**: `Act.actor : PersonId`, no institution parameter anywhere, `resolve` takes no faction, and a seat enters only through `Act.via`. **You cannot pass a `Faction` where a `PersonId` is required, and there is nothing to pass it to** | STRUCTURAL / MECHANICAL |
| 2 | **a decision reads world truth** | `choose` has no `World`; `decision/` cannot name `state/` or `world_q`; `View` holds ids; `PersonInterior` is a frozen copy | STRUCTURAL / MECHANICAL |
| 3 | a write outside the matrix | one path; an unmarked cell raises; no public setters | MECHANICAL |
| 4 | a write at the wrong step | tokens; the gate matches class to row | MECHANICAL / CONVENTION + scan |
| 5 | **a success Event for a write that did not happen** | ⚠ **STRENGTHENED (F9).** Append checks the minted set — **which a no-op receipt passes**, so `ID-9`'s own worked instance (`work` emitting `site.worked` with no delta) survived this row. The gate now refuses `before == after` at the write, so the receipt is never minted and there is nothing to append | MECHANICAL, at the write rather than at the append |
| 6 | a causal orphan | non-empty by constructor; `ROOT` typed; integrity over `log ∪ acts` | STRUCTURAL at the constructor |
| 7 | a refusal that raises | the failure path is `emit`; loader invariant 4 | MECHANICAL |
| 8 | a stored aggregate | no field slot; a Query is a function; a cache is driver-local | STRUCTURAL at the type; CONVENTION at a schema edit |
| 9 | **an Event with an actor, target or subject** | the fields do not exist; `changes[]` is plural | STRUCTURAL |
| 10 | two homes for one relation | one store keyed by subject; the object side is a cache | STRUCTURAL |
| **10a** | ⚠ **NEW (F3) · a write by a non-owner** | the gate checks `actor == subject(id)` on every Tenure write, and admits three declared exceptions only — `T-n`'s matured term, `T-o`'s seat revocation **with `Act.via` present**, and a destroy cascade citing the existence change that caused it | MECHANICAL at the gate — **and it was CONVENTION before, enforced by per-verb eligibility alone** |
| 11 | a seat that knows its holder | no field | STRUCTURAL |
| 12 | **a relation with two owners** | directed `tie`/`knot`; no symmetric kind exists | STRUCTURAL |
| 13 | a relation whose subject cannot act | `subject` admits `RungId` for `contain` only | STRUCTURAL (typed) |
| 14 | **a banner holding territory** | `hold`'s subject is `PersonId`. **`Faction.holdings` is a Query that READS members' holds and cannot write one** — the debt closes on the read side without reopening on the write side | STRUCTURAL (typed) |
| 15 | **open-without-close in the vocabulary** | `release` generic; the loader asserts its domain equals `tenure_kinds \ {contain}` (invariant 6, as corrected for F4) | MECHANICAL at load |
| 16 | a ratchet over ended edges | `ended()` separate; a scan forbids int-returning callers | MECHANICAL |
| 17 | a fourth clock | the MATTER token; loader invariant 5 | MECHANICAL at load |
| 18 | **evidence moving a conviction** | ⚠ **UPGRADED 2026-09-03 — it was MECHANICAL on a check `F.24` disarms.** The INTERIOR write is performed by a function whose signature takes `PersonInterior` **and no ledger reference**, exactly as `choose` takes no `World` (D-2). *A conviction cannot be moved by evidence the writer cannot name.* The loader check becomes a second line, not the only one | **STRUCTURAL by signature** / MECHANICAL |
| 19 | **a default contest depth** | `max_depth` has no default in the signature | STRUCTURAL |
| 20 | a nested contest that crashes | the cap returns `Refusal` | MECHANICAL; **in GDScript the test must actually reach the cap** |
| 21 | a container with a clock | carriers have no behaviour; only the driver calls a step; `t` advances in one line | STRUCTURAL by absence of a method |
| 22 | a subsystem writing state | no token crosses the seam; the projection is read-only | STRUCTURAL / MECHANICAL |
| 23 | a subsystem widening an outcome | `veto : bool`; the ladder takes the minimum | STRUCTURAL by signature |
| 24 | a subsystem returning a winner | the return type is `Margin` | MECHANICAL |
| 25 | **a subsystem-specific Event family** | the kind roster is **derived** (loader inv. 7) from the matrix's `on_write`/`on_condition` and the table's `emits`/`emits_on_refusal`; `log.append` refuses any other kind, **and a subsystem has no data file of its own in which to add one** | MECHANICAL |
| 26 | a silent default for an unregistered kind | every table lookup raises on a missing key; `default_cell` applies only to an unlisted *pair* of registered keys | MECHANICAL |
| 27 | a roster literal in a body | **none** — a list can always be typed into code | CONVENTION + a scan of `loop/`, `seam/`, `decision/` |
| **27a** | ⚠ **NEW · a proper noun in the CONTENT layer** — *`D-27` scans code, and content is where a rule system rots* | **none at the type, and none possible**: the content layer is data, and data may say anything. **A scan of the data files for proper nouns**, run beside `D-27`'s scan of `loop/`, `seam/`, `decision/`. **Every hit is a scenario declaration or a defect, and there is no third case** — a rule keyed to a named faction is scripting drift that has moved out of the code where `D-27` can see it. ⚠ **And the discriminator has to be stated or the scan is noise, because one of the two cases is LICENSED and populous:** the world-generation roster (`F.31`, build step 9) is where proper nouns belong, and it will hit on every row. **The scan's domain is the RULE-BEARING files — the verb table, the write matrix, the register — where a proper noun cannot be a declaration because those files declare no world.** A hit there is a defect; a hit in the world roster is the roster doing its job ⚠ **It binds harder here than in the design it came from.** Under `§D.11` a faction is any uttered `Proposition` plus its `commit` edges, so **every faction that will ever exist is manufactured at runtime** — a content rule naming one is a promise the ontology cannot keep for any of them | CONVENTION + a scan of **the rule-bearing data files** — the verb table, the write matrix and the register; **not** the world-generation roster, which is where proper nouns belong |
| 28 | **a branch on a rung-kind member** | none at the type; **the falsifier IS the mechanism** — re-run the seeded season with `rung_kinds` extended by a synthetic kind and permuted; any test that moves branched on a member | CONVENTION at authoring; MECHANICAL as that one test |
| 29 | order-dependent summation | `condition`, `stores`, `margin` are integers, and integer addition is associative; the act array is canonicalised | STRUCTURAL for the sum; MECHANICAL for the order |
| 30 | **two degree ladders** | one `seam/ladder`; subsystems return a `Margin` | **CONVENTION** — Stage 1's named weak point, carried at that strength |
| **30a** | ⚠ **NEW (F6) · a contest whose outcome changes nothing** | `writes` is `Degree`-keyed for any verb declaring `contests:`; loader invariant 12 refuses a flat list on one; the fold calls `writes_at(degree)` | MECHANICAL at load |
| **30b** | ⚠ **NEW (`ID-18`) · a schema permanence nobody enumerated** | the three the schema grants are listed here rather than left implicit: **`Tenure` is never deleted** (`until` is what makes an ended relation a fact) · **`Proposition` has no setter and no delete** (its immutability is what lets a faction collapse for free) · **the log is append-only**. Each is authored by the designer at a commit, not by an act, and `AX-6`'s scope clause says so. ⚠ **The four open-only relation kinds are NOT on this list, and the distinction is the point** — a duty that could not be discharged, a bond that could not be broken, a succession pointer that could not be changed were **permanences nobody authored**, granted by an incomplete vocabulary rather than by a decision. They are the corpse that motivates the list, not a member of it, and `ID-14` plus the generic `release` is what closed them. **A permanence this row may hold is one a designer chose; one nobody chose is a defect, and the two must not be filed together.** ⚠ **This does not weaken `ID-18`'s claim that a list would have found all four at once** — it is how: enumerating permanences means asking of each *who authored this one*, and the four are exactly the entries where that question has no answer. **The list finds them by the question it forces, not by containing them** | **CONVENTION, and deliberately** — a loader cannot see a language-level guarantee, which is why `ID-18` puts the list here and not in `§B.13` |
| 31 | a cohort subclass | one class; no conversion exists because there is nothing to convert to | CONVENTION + one test |
| 32 | a title/office collision | **there is no `Title` type to collide with** | STRUCTURAL by absence |
| 33 | eligibility by capability, or a seat with a modifier | no bonus field; no modifier column; `capability` is not an eligibility kind and the loader raises on one | STRUCTURAL at the type; MECHANICAL at load |
| 34 | a stale cache | a local of the driver's step call, dropped at the next barrier | STRUCTURAL for lifetime; CONVENTION that a step builds no private dict |
| 35 | **a new draw moving unrelated goldens** | `H(seed, tick, subject, purpose)`; no counter, no service | MECHANICAL (a pinned golden); CONVENTION on `purpose` uniqueness — **the chain's own measured hazard** |
| 36 | a hidden turn order | the canonical key is declared data plus a hash tiebreak; rank never breaks a tie | MECHANICAL |
| 37 | a `social:` value that varies by step | `writer:` is a static column; loader inv. 5 | MECHANICAL at load |
| 38 | a constant invented at the keyboard | every fixture injected by name from a register row; a missing row raises **at the named site** | MECHANICAL + a numeric-literal scan |
| 39 | eviction ranking on salience | the comparator's signature takes `confidence` and `recency` **and nothing else** | STRUCTURAL by signature |
| 40 | a knot deposit minting a new id | the deposit constructor reuses the event id | MECHANICAL |
| 41 | **a decision reading a moving world** | DELIBERATE runs with no token in scope, on a projection built at barrier 2 | STRUCTURAL (no token) / MECHANICAL (scan) |
| **41a** | ⚠ **NEW · an order-dependent DELIBERATE** — *the pure-map claim, asserted structurally and never observed* | `D-41`'s construction is an **absence** — no token in scope — which by `ID-10` is a check that cannot see the failure it excludes. **The observable is a permutation:** shuffle the order in which persons are deliberated and the resulting **`Scene` SET and the season hash must be identical.** ⚠ *Set, not list — `RESOLVE` canonicalises the act array by `(stratum, actor-hash, intra-person position)`, so a differing `Scene[]` ORDER out of a pure map is not the defect; a differing MEMBERSHIP is.* ⚠ **`PART E` step 12 is the nearest thing that exists and is weaker** — it compares a serial run against a pooled one, which varies the *execution mode*, and it is graded *beside — an optimisation* rather than as a property of the loop | **MECHANICAL — one permutation test.** ⚠ *The grade is not a claim that structural absence is generally weak — `D-41` is STRUCTURAL and correctly so **for the property it carries**, which is that a decision cannot read a moving world. **Order-independence is a different property, and no absence carries it**: nothing about having no token stops a pure map from being written order-sensitively* |
| 42 | **a person knowing their faction's true strength** | every lateral traversal lives in `world_q`, which `decision/` cannot name; the person has `leaders_as_claimed` and nothing else | STRUCTURAL (typed) / MECHANICAL |
| 43 | a convening predicate reading another person's interior | the predicate is a declared form over three named sources, not code | MECHANICAL at load; CONVENTION that nobody adds a fourth |
| 44 | **a belief as a private, uncontestable field** | the field is deleted; a belief is a `commit` to an `OUGHT` — utterable, shareable, releasable | STRUCTURAL by absence |
| 45 | the season advanced twice | `t += 1` occurs once, in the driver; CALENDAR has no access to `t` | MECHANICAL |
| 46 | world state behind a global name (Godot) | `World` constructed by the driver and threaded by parameter; the two licensed guards | MECHANICAL — *unreachable-by-name, not unwritable* |
| **47** | ⚠ **a faction field that outlives a barrier** — *the guard the amendment cost* | `Faction` is a **Query return, never a member of `World`**; a field set on one is dropped with the view, exactly as D-34 drops the cache | STRUCTURAL for lifetime; **CONVENTION that nobody promotes it into `World`** |
| **48** | **a war nobody declared, or that nobody can end** | war is a `WAR` Proposition with an `utterer` (AX-6) plus `commit` edges owned by their subjects; `at_war` is a Query over the live ones; peace is `until`, written by an owner (T-m). **There is no boolean between two factions to set, because there is no faction record to hold one** | STRUCTURAL at the type |
| **49** | **a unit changing side mid-contest** | the roster resolves once from `proj` (§C.5.1); `commit` moves only through an Act, and no Act resolves inside another's resolution | STRUCTURAL in Python **/ MECHANICAL in GDScript — `proj` is a live reference there unless copied, and the guarantee must be bought** |
| **50** | ⚠ **a test that cannot observe its own failure** — *`ID-10`'s first representation* | conditional assertions go through `assert_over(iter, pred, min_checked)`, which **raises when `min_checked` was never reached**; §0.1 point 2's rule made callable | **CONVENTION** + a scan for a bare `for … if … assert` under `tests/` |
| **51** | **an unpriced refusal** | the budget is debited **at RESOLVE entry, before eligibility is evaluated**, so a refused act costs exactly what a made one costs. *Attempting and being turned away at the venue is a real expenditure of a season* | STRUCTURAL by ordering — one debit, ahead of the branch. **Falsifier: a refusal Event's `changes[]` is non-empty, carrying the debit's receipt — a refusal is no longer a no-op** |

> ### **WHAT THE TABLE SAYS ABOUT ITSELF, AND IT IS THE HONEST PRICE**
> **Of fifty-one rows, twenty-seven carry a Python grade beginning STRUCTURAL, and fewer hold in
> GDScript; the rest are one path with one test.** ⚠ **The denominator is the NUMBERED rows**; the
> lettered ones (`10a`, `27a`, `30a`, `30b`, `41a`) are amendments to their neighbour and are not
> counted, which is why the table has fifty-six entries and the sentence says fifty-one. **Stated
> because the counting rule has to be re-runnable by a reader who did not write it**, which is the
> whole point of the correction below.
>
> **Twenty-seven of fifty-one is the price of the design**, and it is
> why **the loader and the two scans carry more weight than any single type**: most of what this
> architecture refuses, it refuses by making the bypass **visible**, not by making it **unspellable**.
> Three of the twenty-seven pair the STRUCTURAL clause with a CONVENTION one covering a *different*
> bypass (**8, 34, 47**), and reading them as wholly structural is the misreading this column exists
> to prevent.
>
> ⚠ **THIS CORRECTS THE PREVIOUS SENTENCE, WHICH SAID *sixteen of forty-six* AND DID NOT RECONCILE
> AGAINST THE TABLE.** The counting rule is now stated so a reader can re-run it: *the first word of
> the Python clause.* Five rows were added and one upgraded on 2026-09-03; those account for **five**
> of the eleven (rows 47, 48, 49, 51 and the D-18 upgrade; row 50 is CONVENTION), and **the remaining
> six were a miscount in the original** — recorded here rather than
> quietly replaced, because a self-authored number that nobody could reproduce is exactly what §0.1
> point 4 is about.

---

# PART E · THE BUILD ORDER

Derived from what each module reads. **A step is on the critical path if one NPC's season cannot
execute without it.** Each names the artifact that proves it, because a step is done when the
behaviour executes — and **step 1 is the one deliverable here that writing can satisfy**, which is
why its proof is step 2 loading against it.

| # | delivers | done when | path |
|---|---|---|---|
| **0** | typed ids · the owned versioned `H` · fixed-point scale and band compare | 1,000 ids minted twice under one seed are bit-identical; a golden hash pinned; `H` is not a language `hash()` | **critical** |
| **1** | the carrier types as field declarations, **no behaviour** | nothing on its own — **its proof is step 2** | **critical** |
| **2** | `data/` + the one loader with the **twelve** invariants; `release` as a row; the `writer:`/`on_write` re-keying; **the `Degree`-keyed `writes` for every contested verb** | every file loads; **each invariant fails on a planted violation naming the row, then passes**; a `scale:` key is refused. ⚠ **THIS STEP CANNOT PASS TODAY, AND THE FIRST PUBLICATION UNDERSTATED BY HOW MUCH — `F5`.** It named **two** rows failing invariant 2. Against the live matrix there are **nine**: `(Rung, exists)`, `(Site, exists)`, `(Rung, dates)`, `(Date, fired)`, and — the four that matter — **`(Person, convictions)`, `(Person, stance)`, `(Person, scar)`, `(Person, axis_count)`. No verb in the table writes any `Person` interior field at all**, which is tier-0 `H-62` in the executable chain and is graded **nowhere in this document**. See `F.20`. | **critical** |
| **3** | the stores with private setters · the gate · the four tokens · the receipt mint · the log · the ledgers · the act store · `World` | a wrong-token write raises; an unmarked cell raises; a planted direct assignment is caught by the setter scan; **an Event carrying an unminted receipt fails `append`** | **critical** |
| **4** | live/ended Tenures · `world_q` (the `contain` walk, purview, rank, `holder_of`, `establishment`, `judging_set`, `place_of`) · the barrier cache | walk and rank stay green under the **permuted-roster run** (D-28); the object-side cache equals a brute-force scan; `ended()` is named by no int-returning function | **critical** |
| **5** | the driver · MATTER · CALENDAR · the headless runner | a seeded two-season run with **no acts**, twice, byte-identical including the hash; every MATTER Event has non-empty `causes[]`; a vacant date fires and lapses | **critical** |
| **6** | RESOLVE: canonical order, the fold, eligibility over `Act.via`, refusals that emit, writes through the gate | an **authored** `Act[]` runs a season; `transfer` twice on one larder → `made` then `refused`; **`confer` twice on one seat → `opened` then `confer.refused` with no `obstruct` anywhere**; `release` closes a Tenure of every kind | **critical** |
| **7** | WITNESS: fan-out `total` first, then the five predicates and the per-channel `mints:` | after a co-located act **the witness's ledger holds a `did` claim and the document holder's does not**; eviction holds the cap | **critical** |
| **8** | `decision/` + `loop/deliberate` + the `alignment` sweep | ⭐ **ONE NPC'S SEASON RUNS END TO END FROM Q1–Q4 WITH ZERO AUTHORED ACTS**, and `causes[]` walks from the resolved Event back to the raising Event; the import scan is green; the three-point sweep is run and any flip reported | **critical — THE BAR** |
| **9** | CENSUS: demand-driven individuation · the world-gen roster | a `dispatch` to a non-existent clerk emits `person.demanded`; next season a Person exists whose `person.individuated` cites it | beside |
| **10** | `seam/contest` · `manifest/` · a stub wrapper returning a `Margin` | a `kill/wound` routes to the seam; the nested run returns `Refusal` at the cap — **and in GDScript actually reaches it without a crash**; a misspelled manifest row fails at boot naming the row | beside |
| **11** | the real subsystem wrappers | out of this chain's scope by ruling | beside |
| **12** | the parallel DELIBERATE map | serial and pooled runs produce the identical hash | beside — an optimisation |
| **13** | the Godot shell · the two licensed guards | both guards red on a planted violation, then green; a headless run prints the Python oracle's hash in the integer domain | beside, from step 3 |

**Critical path: 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8.** Step 8 is the bar; nothing after it is on the path.

## §E.1 · Ordering constraints this design adds that the chain's plan does not have

- **Step 2 is a gate the chain never had.** The data must be *consistent* before any store exists —
  and **two of the chain's rows fail it today.**
- **`release` is authored in step 2 and executes in step 6.** ID-14's check runs at load, so a build
  that lands the verb table without `release` **fails step 2, not step 6.**
- **The act store lands in step 3**, before `causes[]` integrity can be written, because that check
  reads it. The chain's log has no such dependency.
- **`decision/` is a directory from its first commit.** The isolation scan matches by path, so a
  `choose` drafted inside `loop/` and moved later **would have been green while violating AX-2.**
- **`titles.domains` moves off the critical path** — under §B.7 it is world-generation content read
  at step 9, not architecture read by the loader.

---

# PART F · WHERE THE THREE STAGES ARE INSUFFICIENT

**Thirty-three entries** (thirty-one from the stages; **F.32 and F.33 were opened by the 2026-09-03
faction amendment and charge to no stage**). Format throughout: what was needed · which stage should
have supplied it · what was assumed · what goes wrong if the assumption is wrong. The numbering is
fixed so the six forward references in PARTS B and C resolve, **and each is a real gap rather than a
number filled to make a reference resolve.**

| § | the gap | assumed | if the assumption is wrong |
|---|---|---|---|
| **F.1** | **what a DEMAND is** *(§C.7)* — Stage 1 rules individuation demand-driven and stops | a refusal Event kind `person.demanded` | a demand arising from a Date or a Petition individuates nobody, and *nothing generates without a demand* **starves the political layer of the persons it needs** |
| **F.2** | **what opens a contest** — Stage 3 gives two triggers and never relates them | only a declared `contests:`; undeclared contention is scarcity | every collision on an undeclared subject is a refusal where it should be a fight |
| **F.3** | **where a declared term lives, and who matures it** — Stage 1 gives `T-n`; nothing says where it is stored | `Tenure.term`; MATTER matures it; the causation rule generalises to two causes | if #353's *"only Tenure write in MATTER"* is literal, **a term of service has no lawful end and `T-n` is unimplementable** |
| **F.4** | **what `Tenure.degree` IS** *(§B.8)* — a field with a writer and no reader | carried unread — which under ID-13 is a field that does not exist | if it is the strength of a `commit`, **every faction's leadership Query has no input and every faction is leaderless** |
| **F.5** | **`coherence`'s reader** *(§B.2)* | carried unread, flagged for deletion | if the social-contest wrapper's margin reads it, **social contests are undecidable** |
| **F.6** | **`capability`'s season writer** *(§B.2)* — Stage 1 keeps the field and says nothing about advancement | world-gen writes it once; nothing else does | **a character never improves at anything** — a constant no act can move, which is `AX-6` applied to skill. The repair is a `practice` verb, not a field |
| **F.7** | **what bounds `establish`** *(§B.7)* | remit ⊆ the exercised seat's; scope under its purview | the subset rule **forbids constitutional invention**, and Stage 1's own sovereign-power falsifier fires here rather than being answered |
| **F.8** | **the judging set** — every stage leaves it open; Stage 1 calls it *the live threat* | a Query over seats whose remit covers the matter | if judges are a venue's custom, **two venues with identical seats must decide identically** and local custom is unrepresentable |
| **F.9** | **the ladder's margin model and band edges** | only the type — four bands on a fixed-point margin | **nothing runs at the seam until the edges exist**, and an implementer writes the ladder in the subsystem — the refusal `T-k` says is enforced by a person noticing |
| **F.10** | refraction's side | receiver-side, per the chain's held-back closure | `terms.distorted` needs a mutable emitter-side object, which §37.1 forbids |
| **F.11** | `standing`'s formula and **polarity** | V2's, as amended | if standing reads others' regard, it needs a cross-holder read §20 forbids — and the fallback is **one scalar**, weakening the `Vector2` argument |
| **F.12** | **scene packing, what expands a scene, and where `max_depth` comes from** | packing by the assumption row; NPC scenes expand only through `contests:`; the cap is a fixture for NPCs | if accepting a duel is an NPC choice, **`choose` needs a depth term and the budget's meaning changes** |
| **F.13** | whether an `Act` persists | a resolver-side act store | if a future Query exposes it person-side, **attribution becomes world truth and `AX-2` breaks silently.** The guard is a scan, and it is CONVENTION |
| **F.14** | **an Event's place** | `place_of` — the scene's place, or the changed thing's rung | a plague is *one Event spanning many rungs* and **has no single place**; `place_of` must return a set and my signature does not |
| **F.15** | **the nine dispensation terms** *(§B.5)* — *"nine typed terms"* and nothing lists them | a schema for one Record kind, **unspecified** | **not an assumption so much as an absence: the entire downward mechanism has no executable content**, and `issue` produces a document nobody can comply with |
| **F.16** | **what each witness channel mints** — `T-d` says attribution is per-witness; no stage says which witness gets which claim | a `mints:` column; only `co_located` mints attribution | covert action against an office becomes impossible where it should be **a report that can be false** |
| **F.17** | how a person joins an establishment | `oblige`'s `requires` reads the seat's `binds` | if admission is a seat's own act, the closed remit roster **needs a sixth member — a ruling, not a row** |
| **F.18** | **upkeep's source** — *"out of the office's stake"*, and `stake` was retired | unpaid; establishment persists until released | **no economic pressure on any office**, and *"finite, contested"* has no mechanism. A MATTER payment would be a fourth clock, so the repair is a verb |
| **F.19** | the envelope, individuation, and `weight` | individuation decrements a band and mints at weight 1 | without the construal spread, **a cohort at weight 200 chooses as one mind** |
| **F.20** | ⚠ **FOUNDING VERBS** — no stage names a verb that founds a hearth or builds a site | the rows are dropped until a verb is ruled | **the world only decays — nothing is ever founded or built.** This is what blocks build step 2 |
| **F.20a** | ⚠ **NEW (F5) · NO VERB WRITES ANY `Person` INTERIOR FIELD.** `§B.2` carries `convictions`, `stance[]`, `scar[axis]`, `axis_count[axis]` and names a reader for each; **it names no writer for any of them.** The four are `RES`-stepped matrix rows with no producing verb | that a consequence table would supply them | **every interior consequence is inert.** A person's convictions cannot move, so `choose` scores against a constant, `standing` has nothing to diverge from, and the epistemic layer has no moral layer to disagree with. ⚠ **This is the gap the degree-keyed column (`§C.4`, `F6`) is the shape of the answer to** — an interior write is a *consequence of an outcome*, which is exactly what the sixth column declares |
| **F.20b** | ⚠ **NEW (F13) · THE FOLD MINTS EVENT KINDS NO COLUMN DECLARES.** The live implementation emits `act.ineligible`, `act.refused` and `contest.resolved` as **body literals**, as a fallback where a row declares no refusal kind | that invariant 7's derived roster covers every kind | **invariant 7 refuses all three at `append`**, so the loop as built cannot run under the loader as specified. Either the three become declared columns — an eligibility-refusal kind per verb (`F7`, invariant 4 widened) and a `contest.resolved` emission column — **or the derived roster is not derived.** A definition living as a literal in a body is what `ID-12` refuses |
| **F.21** | the rank of a cluster seat (`scope = null`) | no rank; the loader forbids a `higher_rank` conjunct on one | church seats become revocable by purview alone — **which they also lack** |
| **F.22** | **how succession fills a seat** — death does not open a conferral Date | the named heir is eligible by `own` — **an eligibility the four kinds cannot spell** | every death is a vacancy only a superior can fill, **which may be right for an office and is wrong for a crown** |
| **F.23** | the `AX-3` loader check | no verb writing a conviction has a ledger-phrased `requires` | ⚠ **NARROWED 2026-09-03.** It read *unenforceable while `requires` is prose (F.24) — the check is a comment*, and **that made `AX-3` the least-defended axiom in the design, guarded only by something F.24 disarms.** D-18's signature construction now carries it, so this entry covers **the second line only**. The gap survives at its own reduced strength; the axiom no longer depends on it |
| **F.24** | ⚠ **THE GRAMMAR OF `requires`** — Stage 3 fixes five columns and never says what the second contains; every row carries it as **a prose string** | ⚠ **NO LONGER ASSUMED — DERIVED. See `§F.24a`** | **the resolver needs a body per verb to evaluate prose, and `D20 — the resolver has no body` returns as `the resolver has thirty`. This is still the item everything dynamic depends on:** `ID-16`'s loop enumeration and `F.1`'s per-conjunct demand are both blocked on it. ⚠ **`F.23`'s `AX-3` check IS NO LONGER ONE OF THEM** — a merge with `origin/main` (2026-09-03) landed `D-18`'s signature construction, which carries `AX-3` **STRUCTURALLY** by giving the interior write no ledger reference to name. The loader check is now a second line rather than the only one, so the axiom does not wait on this row. |

## §F.24a · ⚠ **THE GRAMMAR, READ OFF THE 32 LIVE CELLS RATHER THAN DESIGNED — added 2026-09-03**

`F.24` said *"assumed: a small typed predicate grammar"* and supplied none, which is the shape of
handing a property forward. **The 32 `requires` cells in the executable chain are the specification,
and reading them yields SEVEN forms.** They are listed with their live instance so a later session
can check the derivation rather than trust it:

| # | form | live cell |
|---|---|---|
| 1 | **existence over an edge kind** | `repudiate` — *a live commit exists* · `revoke` — *a live hold exists* |
| 2 | **a computed scalar against a threshold** | `transfer` — `stores(hearth(giver), kind) >= amount` · `work` — `condition >= floor(verb)` |
| 3 | **path existence in the containment tree** | `move` — *a contain path exists* |
| 4 | **cardinality on an object** | `confer` — *1-per-object: no live hold on the object* |
| 5 | **a relation between actor and subject** | `succeed` — *the actor holds the office whose heir is being designated* |
| 6 | ⚠ **membership in the ACTOR'S OWN ledger** | `tell` — *the teller holds a claim on the subject* · `comply` | 
| 7 | ⚠ **a basis lookup on the exercised seat** | `confer` / `revoke` — *the office's conferral / revocation basis* |

⚠ **AND TWO CELLS ARE NOT PREDICATES AT ALL, WHICH IS THE FINDING RATHER THAN A ROUNDING ERROR.**
`issue` — *"scope enumerates executors, not places"* — and `open_case` — *"the act DECLARES the stages
and their terms"* — are **constraints on the well-formedness of the Act**, not questions asked of the
world. **They belong in the `Act` schema and are refused at construction**, not evaluated at RESOLVE.
A grammar that admitted them would have to be able to talk about the act's own payload, which is how
a predicate language becomes a second resolver.

> **Forms 6 and 7 are the two the cross-read missed**, and each carries a consequence: **6 is why
> `§B.2` needed the own-ledger carve-out (`F8`)**, and **7 is why `T-o` exists (`F3`)** — a basis
> lookup on a seat is exactly the authority a revocation exercises.

**The grammar is small, and that is the claim `F.24` assumed and never demonstrated.** Seven forms,
two of which are lookups, closes 30 of 32 cells; the other two are schema constraints. **An
independent governance design reached the same shape from a disjoint corpus** — a quantifier, a
comparison and a relation, and nothing else — which is corroboration rather than a source.

⚠ **THE TABLE RESUMES HERE.** `§F.24a` was inserted between `F.24` and `F.25` on 2026-09-03 and the
remaining rows were concatenated onto its closing line, so `F.25`–`F.33` — including `F.28`, `F.32`
and `F.33` — rendered as prose with literal pipes. **Header restored 2026-09-03 (rev. 3).**

| § | the gap | assumed | if the assumption is wrong |
|---|---|---|---|
| **F.25** | sum-then-clamp against the sequential fold | bounded scalars clamp at stratum end; integer stores check sequentially | a `restore` in the same stratum is invisible to a `work`'s band gate — **a site that was repaired refuses the verb the repair reopened** |
| **F.26** | the canonical order key | `(stratum, actor-hash, intra-person position)` | **a hash decides who eats when two people reach one larder, and the design has no better answer — which should be said aloud rather than discovered** |
| **F.27** | Thread Sensitivity — *the only class-shaped gate* | not modelled | nothing. **Named because an implementer will look for it in the eligibility kinds and it is deliberately not there** |
| **F.28** | termination across seasons | ⚠ **AMENDED 2026-09-03 — *and nothing here pretends to* was true when written and is not now.** Stage 1's `ID-16` states the axis (*a design enumerates its loops and signs each one*) and splits the representation: the **declared** signed list is buildable today as a `LOOP` row kind with a `sign` column in `hole_register.yaml` (not in this markdown table, which would be reference), and the **derived** check that recomputes the cycle set from `writes` × typed `requires` — the thing that would give that column a reader — is blocked on `F.24`. **The spiral is still unbounded** — what changed is that the hole now has a shape and a first half that can be built | `ID-16`; **derived half blocked on `F.24`** |
| **F.29** | act cost beyond the budget | the budget is the whole price, as ruled | **a scene yields unbounded forgeries** |
| **F.30** | a person and their person-rung sharing an id | same `n`, different tag | an individuated Person needs a new person-rung and `contain` edge in the same CENSUS write, or **the new Person is nowhere**, which `co_located` reads as unwitnessable |
| **F.31** | the world-generation roster | a registry row read once at boot | nothing architectural — but **the acceptance case needing a postless person is unreachable** |
| **F.32** | ⚠ **WHOSE EDGE A WAR IS, AND THEREFORE WHO MAY MAKE PEACE** *(§B.6.1, D-48)* — opened by the 2026-09-03 amendment, charged to no stage | a `commit` whose subject is the declaring **person**, so `T-m` gives peace to the declarer | **the declarer dies and the war can be ended by nobody** — an open-only relation, which is precisely the ratchet `AX-6`/`T-m` were written to eliminate. The repair is an edge subjected to *the seat's holder*, and **the design has no Tenure that changes hands** |
| **F.33** | **whether `at_war` may appear in a verb's `requires`** *(D-48)* | it is asked by the **seam**, never by the resolver — so a declaration licenses no act by itself | if raising levies or crossing a border is gated on it, war stops being a Query the combat seam asks and becomes **an input to eligibility** — and `F.24`'s grammar then needs a Query term it does not have |

## §F.34 · What is NOT a gap, said so the count is honest

The `writer:` renaming and the `on_write`/`on_condition` split are **calls, not gaps** — the chain's
shapes were expressible and are re-keyed for idempotence. The `Seat` unification, `release`, directed
`tie`/`knot`, deleted `beliefs` and `judging_set_rule`, and `hold`'s Person-only subject are
**derivations the stages force**, recorded in §A.3 rather than here.

**Added 2026-09-03, so the amendment does not inflate the count either.** `Faction.head?`'s rule is
**not a new gap** — it is a *consumer* of `F.4`, and if `Tenure.degree` gets a reader the head
resolves with it. `holdings(faction)` over two members holding one rung is **not a gap** — it is a
set union. **The roster contract (§C.5.1) is not a gap and not an addition:** it states a property the
projection already had, and its entire content is *do not hand the wrapper a live world*.

**Added 2026-09-03 (rev. 2 follow-up), for two items an outside evaluation found graded in neither
list — which is the failure mode this section exists to prevent, since a defect in neither the gap
register nor the not-a-gap register is invisible to both counts.**

- **`Tenure.conferrer` is not a gap — it is DELETED** (§B.8). It had no reader in any file of this
  exercise, and the fix `ID-13` licenses is a reader **or** removal, not a hole row. Its removal opens nothing:
  who may revoke is `Seat.revocation` (`T-o`), and what conferred a Tenure is the opening `Act`'s
  `actor` and `via` in an append-only log.
- **Stage 1's `establishment` field is not a gap — it is SUPERSEDED** by `§B.7`'s Query over
  `oblige`, and Stage 1 now says so at **both** sites: `§E.2.5`'s council row and `§D.6`'s `OWNS`
  line, which listed it as owned state. ⚠ **It sat in neither register**, which is how a reader
  arriving at Stage 1 got a shape Stage 4 had already refused, with no marker — and the second site
  was found only because the first was being fixed. *The register works; nobody had run it across
  the surfaces the rev. 2 pass had itself edited.*

## §F.35 · **THE SHAPE OF THIS LIST, WHICH IS ITSELF THE FINDING**

> **Thirty-three entries, and they are not evenly distributed.**
>
> **Stages 1 and 2 are nearly closed on their own subjects.** The gaps tracing to them — `F.3`, `F.6`,
> `F.7`, `F.17`, `F.21`, `F.22` — are places where **a theorem was stated and its mechanism left to
> Stage 3.**
>
> **Stage 3 is where the density is.** What a verb's second column contains (`F.24`), what opens a
> contest (`F.2`), what a witness mints (`F.16`), what a dispensation says (`F.15`), what a scene
> packs (`F.12`), and what the loop's one new step reads (`F.1`) are **all Stage 3's subjects, and
> Stage 3 states each as a property without a representation.**
>
> **That is not a criticism of the exercise — the ordering put representation last on purpose — but
> it is the honest finding: THE ARCHITECTURE ABOVE IS DERIVED THROUGH STAGES 1 AND 2 AND ASSUMED
> THROUGH STAGE 3.** A reader deciding what to build first should weight these entries by which
> stage they charge.
>
> ⚠ **AND THE 2026-09-03 AMENDMENT IS THIS THESIS RUNNING LIVE, WHICH IS WORTH MORE THAN THE TWO
> ENTRIES.** Jordan stated two properties — *a faction is a deployable container* and *factions can
> be at war* — and the design absorbed both **without a new primitive**: a Query return and a
> Proposition with an owned edge. **What it could not absorb was their representation**, and the two
> unabsorbed pieces (`F.32` whose edge a war is, `F.33` whether `at_war` reaches `requires`) are both
> *"a property was stated and its representation was left to later"* — **the same failure mode, from a
> different author, on the first try.** The list's shape is not an artefact of who wrote Stage 3.

---

# PART G · THE METHOD — HOW DESIGN PROCEEDS FROM HERE

PARTS A–F describe how *this* design came out. **This Part says how design is done so that the next
one comes out the same way without this session in the room.**

Four questions, kept apart on purpose: **SHAPE** (what form, and what fixes it) · **ORGANIZE** (what
the unit of decomposition is) · **ARTICULATE** (how it is written so it survives a session boundary)
· **ORCHESTRATE** (how the work is run). **They are usually collapsed into the word *architecture*,
and the collapse is the failure: a session that cannot say which of the four it is doing does all
four badly at once.**

> **Where a principle below has a corpse behind it, the corpse is cited. A principle with a corpse
> beats one with an argument, because the argument can be re-litigated next session and the corpse
> cannot.**

---

## §G.1 · SHAPE — what determines the form

**G.1.1 · Shape is derived, and the derivation runs in ONE direction.** Axioms → theorems → idioms →
admission tests → fields. **Nothing runs the other way.** A field is admitted because a predicate
admits it; a predicate exists because a theorem needs it; a theorem is a theorem because an axiom
forces it. ⚰ *The tracer's entity model — every new requirement landing as another field.* **A schema
that lists fields can only grow; a schema that states what a thing IS can answer a requirement.**

**G.1.2 · Know which statements are axioms.** *"Break an axiom and you have chosen a different game —
deliberately, and you can say what you chose. Break a theorem and you have introduced a
contradiction, which shows up later as a defect nobody can localise."* ⚰ *`L3`, argued for four
revisions as free-standing when its clause-2 hole is exactly what `AX-4` predicts.* **A session
defending a rule by repetition has not asked which kind of rule it is.**

**G.1.3 · The axiom-set falsifier is live and has a hit rate.** *Derive any one from the other five*
found `AX-6` missing. **So every time a derivation reaches for something it cannot name, the reaching
is evidence about the axiom set, not about the derivation.**

**G.1.4 · A shape is a set of refusals, each with what pays for it.** Where the answer is *nothing*
the refusal is free; where it is *8 of 50 surveyed arcs, honestly*, the price is on the row. **A
design that cannot say what each refusal costs has not refused anything — it has merely not built
something yet.**

**G.1.5 · Where the design reaches for a TRACK, find two things that can disagree and band their
gap.** *A track is a stored aggregate wearing a stage's clothes.* The general instance is `AX-3`: two
layers that *look alike from any distance* need different homes, different movers, different times.
**Any proposal with one quantity that both measures and decides is that collision in a new dress.**

**G.1.6 · Architecture fixes the ordering and the walkability; content fixes the membership.**
> **A shape decision is one that would be correct for ANY membership of the data it governs.** If a
> rule is correct only for this roster, it is content. If it branches on a member, it is drift.

**G.1.7 · Structural before mechanical before convention — and say which.** ⚰ *A claim of STRUCTURAL
that is MECHANICAL is "a guard that cannot observe what it guards."* **Design the type first, then
the hook:** a constraint carried by a return type — `veto : bool` — cannot be argued around; one
carried by a rule can.

**G.1.8 · Derive first; compare to what exists second; NEVER the reverse.** ⚰ *Stage 1's first PART E,
withdrawn in full: "evidence that something is already so is not an argument that it should be so."*
§G.4.6 says what structure makes this hold under pressure.

---

## §G.2 · ORGANIZE — the unit of decomposition

**G.2.1 · The unit is an OWNER.** The module rule is `AX-4` applied to code rather than to state, and
it generalises into a test for a decomposition nobody here has seen:

> **Name the writer of every value the proposed module touches.**
> **Exactly one, and it is this module** → you have found a unit.
> **You cannot name one** → the model is incomplete — that is `AX-4`'s own test.
> **You can name two** → you have found a defect, and the decomposition is wrong at that value.

⚰ *A per-issue stance store sitting beside `Person.stance`; `Coherence` read in three places and
owned in none; travel legs in the write matrix and in no ownership row.*

**G.2.2 · Decompose along ownership — never along subject, scale or phase.** Each is an *axis*, and
the test is exact: **a LEVEL is a parent (knowing it constrains the child); an AXIS is an index.**
⚰ *`here.kind == "person"` inside a resolver precondition; `phase:` needing to be a set because one
write class is written in two steps; a rung-level rule placed on a code-level object, where the rule
had no referent.*

**G.2.3 · One type, many kinds; the membership in data.** **The test before adding a type: does any
mechanism need to behave differently for this variant in a way a data row could not express?** If
no, it is a kind. ⚰ *`Title` — one class doing two jobs, patched by a refusal asserting the two are
mutually exclusive categories, which the ruling contradicts.*

**G.2.4 · A relation whose subject cannot act is a field wearing a relation's shape.** Name the
subject; ask whether it can act; if not, re-subject the edge onto the person whose act maintains it,
or admit it is a field. ⚰ *`succeed` — the only Tenure whose subject is not a person, and the only
one nothing can end.*

**G.2.5 · The reverse index is owned by Nobody and stored nowhere.** Covers every *index*, *lookup*,
*summary* and *roll-up* a session proposes: recomputable → not stored; needed for cost → built at a
barrier, discarded at the next.

**G.2.6 · Resolution is a row — never an import, never an inference.** ⚰ *The 114-line regex router
with eleven unreachable probes and a 46% miss rate, and its five recurrences ending in `age\w*`
matching agent / agency / agenda.* **A module that must interpret content to decide where it goes has
become that router.**

**G.2.7 · A boundary enforced by a scan is a DIRECTORY.**
> **When the strongest enforcement available is a scan, the unit of organisation must be the unit the
> scan can see. A boundary drawn inside a file is drawn nowhere.**

**G.2.8 · FIRST-CLASS FOR CONSUMERS IS NOT FIRST-CLASS FOR STATE** *(added 2026-09-03 — the general
rule Jordan's faction ruling settles, and the only §G.2 entry whose corpse is this exercise's own).*

> **Never ask *"should this exist as an object?"* — that conflates DEPLOYING with OWNING and has no
> right answer. Ask both halves:**
> **1 · What does code need to HOLD?** → if a consumer must iterate it, name it and build it.
> **2 · What WRITES it?** → if the answer is *nothing*, it is a **view**, and it is built at a
> barrier and dropped at the next.
> **Two yeses give a carrier; hold-yes and write-nothing give a view; neither gives a Query.**

⚰ *Stages 1–3 answered the single question, concluded a faction is not an object, and left the battle
seam, the squad grid, the UI and the AI each recomputing a roster nobody had named. The conclusion was
right about ownership and wrong about deployment, and it took a ruling to catch — which is the point:*
**the single question cannot express the case, so no amount of care answering it would have found this.**

⚠ **The rule has a price and it is charged in Part D.** A view is a type, and a type can gain a field.
The defence is **lifetime, not absence** (D-47) — strictly weaker than the guard it replaces. **State
the drop when you take it**; a rule whose cost is unrecorded is how a design accretes carriers one
reasonable step at a time.

**G.2.9 · A PROCEDURE IS REQUIRED WHEREVER THE ORDER OF SUB-STEPS CHANGES THE OUTCOME — AND
NOWHERE ELSE** *(added 2026-09-03).*

> **This design carries both forms and never said which decides which.** `RESOLVE` is an **ordered
> fold** — *each act sees the world its predecessors left* — and `DELIBERATE` is a **pure map**, where
> order is not merely unnecessary but forbidden. **The criterion is the whole difference:** if
> permuting the sub-steps can change the result, the order **is** the mechanism and the thing is a
> procedure; if it cannot, order is an implementation detail and the thing is a map, an edge or a
> Query.

**What it buys, stated as the two errors it refuses in opposite directions.** Modelling a genuine
procedure as a rate or an equilibrium **deletes the mechanism** — a siege, a succession and a vote are
sequences whose intermediate states are the play, and an edge with a weight cannot hold *what happened
between the second and third reading*. Modelling a rate as a procedure **invents an order nobody
authored**, and an order nobody authored is `AX-5`'s fourth motion arriving through the back door: a
step that advances because the code reached it.

⚠ **AND THE CRITERION IS ITS OWN FALSIFIER, WHICH IS WHY IT IS A RULE AND NOT A PREFERENCE.** For
anything claimed to be order-independent, **permute and compare** — that is `PART D` row 41a for
`DELIBERATE`, and it is available anywhere the claim is made. **A property that cannot be permuted is
a procedure whether or not it was written as one.**

⚠ **Provenance, because the scope rule requires it.** This arrived from an independent governance
design (#359), **as a falsifier and not as a source** — and it arrived inside a section
this exercise's own evaluation had dismissed wholesale, which is the over-refusal `G.4.3`'s second
direction exists to catch, committed against the document that names it. **The rule is admitted on its
derivation here, not on that document's authority**: both forms were already in this architecture, and
what was missing was the sentence that tells them apart.

---

## §G.3 · ARTICULATE — how it is written so it survives

**Load-bearing here in a way it would not be elsewhere, and the reason is in the governing document:
there is no context between sessions.** A design that cannot be re-read correctly by someone with no
memory of it has failed whatever its merits. ⚰ *"Prose registers are re-typed; rows are inherited.
Fourteen-plus of the census's items were lost at a section restating its neighbours."*

**G.3.1 · A design statement survives only in a form something other than a reader can evaluate.**

| form | survives because | what belongs in it |
|---|---|---|
| **data a loader validates** | **a contradiction fails the load, with the row named** | every closed set, table, fixture, the write matrix, the verb table, the register, the manifest |
| **code with a falsifier** | **red before the change, green after; a later session runs it** | every mechanism; every claim of the form *X reads Y* or *nothing writes Z* |
| **prose** | **it does not, on its own** — only as a *pointer* to one of the above | intent · history · the worked failure · the rejected alternative · the corpse |

> ### **THE RULE: A STATEMENT THAT BINDS BEHAVIOUR GOES IN THE FIRST OR THE SECOND. Prose may carry
> it only as a pointer, with the command or the row id.**

⚰ **This document's own `F.24`.** *A verb is a declaration in five columns* — and every row's second
column was written as a **prose string**, so the load-time guard `F.23` proposes over it *is a
comment*. The same shape three times in the chain: an eligibility cell carrying a precondition, where
the fold split on the first `:` and **never matched**; `contests:` transcribed as a note nothing
reads, **so the fold executed a kill as a direct write**; and the write matrix's own verdict on
itself, *a comment is not a constraint*.

> ### **THE GENERALISATION OF THE `F.23`→`F.24` CHAIN:**
> **A CHECK IS EXACTLY AS STRONG AS THE REPRESENTATION OF THE THING IT CHECKS.** Before writing any
> guard, ask what form the guarded thing is in. **If it is prose, the guard is prose, and the honest
> act is to type the thing first.**

**G.3.2 · What must be written down, and where.**

| what | where | ⚰ corpse |
|---|---|---|
| the **admission test** of every entity — IS · OWNS · ADMITS · NEVER, *including the reader clause* | beside the type, **on every entry** | `Rung.stake` re-admitted silently because its entry lacked the clause |
| the **reader of every declared field, with the command to re-run the claim** | the field's row; the `ID-13` scan | *"no formula reads any of them"* was true of #353 and **false at HEAD** — the claim carried no command, so it aged into falsehood between revisions |
| the **closer of every opener**, per kind | the verb table; `ID-14` at load | four of seven relations open-only |
| the **grade, default, site and sweep** of every hole | the register, as rows | an `absent` hole filled *inside a subscript* for four revisions |
| the **falsifier of every claim, and its outcome** | the same commit | fifteen of twenty PASS probes with no assertion — *a PASS meant did not crash* |
| the **rejected alternative** of every call | beside the call | the regency menu — *the menu was false, and the derivation is what caught it* |
| the **correction, recorded rather than overwritten** | in place, marked | *a superseded derivation that stays legible is how the next session avoids re-deriving it* |
| the **enforcement grade**, in both target languages | beside the invariant | *overstating this column is the failure mode* |

**G.3.3 · What must NOT be written.**

- **A count typed by hand.** ⚰ *A tally summing to 34 over 32 rows; a header saying "ten holes" over
  twelve.* **A number appears in prose only with the command that reproduces it.**
- **A definition twice.** ⚰ *A definition living twice in one file with a test guarding that the two
  copies agree — guarding a duplicate is the shape §8 asks you not to create.* And its asymmetric
  successor: *add one roster row and an office silently became a title, flipping its revocation, with
  133 tests green.*
- **A coined word where a plain one exists**, or a letter-number where a word exists. ⚰ *A draft
  spelling the steps `B1…M2`, then citing review findings `B1` and `M1` in the same file: two
  namespaces, one token shape.*
- **A default in a body.** ⚰ *A wear table returning `20` for an unregistered kind — it answers,
  plausibly and wrongly, forever.*
- **A finding as a document.** A finding is an edit, or a row that needs a human, or nothing.
- **A fact about the tree stated as timeless.** Every *X is / X does* about code is a fact **at a
  commit** and must say so.
- **A "structural" that is mechanical.** PART D exists to prevent it.

**G.3.4 · Define a term where it is INVOKED, not only where it is described.** The data row carries
its meaning in its own column; the loader's refusal message names the rule it enforces; the register
row carries its citation. ⚰ *`evacuate` — a word coined for what `retire` already covered, read cold
by a later session as "queued for deletion", escalating a non-existent blocker across three surfaces.*

**G.3.5 · The single test, applied in both directions.** *If this document were deleted, would the
game behave differently?* **No** → it is reference. **Yes** → the mechanism is in the wrong place;
move it into data or code and leave a pointer. **Run it over every design statement at a stage
boundary.** It is the one articulation rule that needs no judgement.

---

## §G.4 · ORCHESTRATE — how the work is run

**G.4.1 · What a stage boundary is FOR: it closes on REPRESENTATIONS, not on properties.**

The evidence is PART F's own distribution. Stages 1 and 2 are nearly closed on their subjects; Stage
3 carries most of the gaps, **and the reason is uniform — it was asked for properties and delivered
each as a sentence without a form.**

> ### **A STAGE MAY STATE A PROPERTY ONLY TOGETHER WITH THE REPRESENTATION THAT CARRIES IT, OR A HOLE
> ROW THAT GRADES ITS ABSENCE. A property with neither is not a result of the stage — it is work the
> stage has handed forward without saying so.**

**Applied mechanically at the boundary:** for every sentence of the form *an X does / has / never Y*,
point at the type, the column, the row or the falsifier — or at the graded hole. **This is §G.3.5 run
as a gate**, and it would have turned Stage 3's twenty-odd forward-handed properties into twenty
register rows **at the moment they were written, which is when they were cheapest.**

⚠ **AND A REPRESENTATION IS NOT ENOUGH, WHICH IS THE CLAUSE THIS RULE WAS MISSING (added
2026-09-03).** A stage can close on representations and still be **behaviourally wrong**: `PART D`
row 5 was a typed representation of *no false success report* that a no-op receipt walked straight
through, and loader invariant 6 was a typed representation of a property **no actor could ever
satisfy.** Both are consistent; both are wrong; **no amount of pointing at the type would have found
either.**

> ### **THE FALSIFIER FOR A DESIGN CLAIM IS A TRACE, NOT A GREP.**
> The evidence is an audit whose seven principle-derived findings were **all** local inconsistencies
> between two passages — findable by turning a statement into a grep — while an independent pass that
> traced the mechanics found **three behavioural bugs in text that reads perfectly.** *Principles
> catch contradiction; only tracing catches error.*
>
> **`§0.2` already owns the answer and `G.4.1` did not cite it:** a stage boundary closes on a
> representation **plus one execution** of the thing it represents, or the representation is a
> hypothesis. Build step 8 is that execution for this document, and every claim above it is a
> hypothesis until it runs.

**G.4.2 · Producing and checking are different jobs, and the division is STRUCTURAL.** Independence
is a tool list, not a sentence — a critic declared `Read, Grep, Glob` **cannot write, whatever its
prompt says.** Put the stronger tier where the error is silent: *a synthesis artifact is reviewable
and cheap to revise; an audit verdict or a guardrail decision is where being wrong is silent.*

**G.4.3 · The critic attacks the SETUP, not only the result — and in BOTH directions.**
⚰ *An adversarial pass that attacked a result's statistics and never its setup — "are the two arms
the same experiment?"* ⚰ *And the mirror: a pooled faction-wide resource refused wholesale, which
**survived all four adversarial passes** because every critic was checking for inventions and none for
over-refusals. Correcting it unblocked ten arcs.*

> **An error AGAINST the design is as serious as one FOR it, and is harder to see, because it looks
> like rigour.** A critic's charter names both questions: *did the producer invent?* and *did the
> producer refuse what the design permits?*

⚠ **THERE IS A THIRD DIRECTION AND THE CHARTER MISSED IT (added 2026-09-03).** An independent design
audited itself against its own principles, found seven violations, and **listed a defect among the
things it had got right** — a feedback loop that penalises good governance, filed in the table headed
*the negative loops that are correct*. Neither invented nor over-refused: **misclassified in sign, by
the author, inside the section built to catch exactly that.**

> **So the charter has three questions, and the third is a `§0.1` pt 4 setup error rather than a
> reading error:** *did the producer invent?* · *did the producer refuse what the design permits?* ·
> **and *did the producer grade something backwards?*** The third is the one an author cannot ask of
> themselves, because the misgrading and the confidence come from the same place.

⚠ **AND THIS DOCUMENT'S OWN REWRITE IS THE FOURTH INSTANCE OF THE SECOND DIRECTION.** The cross-read
that fed it graded `contract` — what a subordination owes — as *"a real question #358 leaves open"*,
**with `§E.1.6`'s pattern in front of it and already banked as that section's best result.** The
answer was one derivation away (`§E.1.7`). **A critic charter that names the direction is not the same
as a critic that runs it.**

**G.4.4 · The adversarial pass produces EDITS, and at most one row.** Everything else is fixed in the
commit or dropped. **The generalisation of why:** the loop's carrier is prose — forbid the guard and
a session writes a finding; forbid the finding and it writes a plan. **The only terminal states are
an edit, or a row that has survived the five tests.**

**G.4.5 · Anything that looks like a ruling gets the five tests before it gets a human.** Superseded ·
irrelevant · answered by a design document · answered by precedent · answered by what makes sense for
the architecture. ⚰ *Corpses run both ways: `budget`'s placement escalated when precedent answered
it; and a 156-row queue that formed because nothing ran the tests.* **And the grade decides the
behaviour** — refuse at `absent`; inject · declare · sweep at `assumption`; *and a verdict that flips
across the sweep is itself a finding, and a more important one than the verdict.*

**G.4.6 · The one hazard a session under pressure repeats, and the structure that prevents it.**

> **DEFERRING TO WHAT EXISTS INSTEAD OF DERIVING FROM WHAT IS TRUE.**

This session's three worst failures — sweeping a repository that was out of scope, treating the prior
chain as a baseline, and recording findings instead of resolving them — **are one mistake.** It has a
signature: **the session opens the tree FIRST, because the tree is enumerable and derivation is
not**, and everything it then produces is the tree with better prose. ⚰ *Stage 1 fell into it and
withdrew a whole Part; the chain fell into it and "built the model that does not need conferral, and
then found conferral missing"; and it is the exact mechanism of §0.3's loop, where a doctrine
demanding exhaustiveness drifts to whichever surface is enumerable.*

**The structure that prevents it — a synthesis call, with its alternative named:**

> ### **THE DERIVATION RUNS WITH THE TREE CLOSED. THE TREE IS OPENED ONLY TO FALSIFY.**
> A design session's **first** artifact is the derivation from the axioms, produced by an agent whose
> scope **excludes** the implementation trees — enforced the way the critic's read-only status is
> enforced, **by what the agent can reach, not by a sentence in its prompt.** Its **second** artifact
> is the comparison: for each place the tree and the derivation differ, either the tree is defective
> (an edit) or the derivation is (a correction recorded in place). The prior chain is read *between*
> the two, as evidence at its own strength.

**The rejected alternative is the instruction *"do not read `canon/`, `systems/`, …"* — which is a
display string.** This session was given exactly that instruction and honoured it; an earlier draft
was given the same instruction and did not. **The difference between an instruction and a scope is
the difference the critic's tool list already demonstrates, and it is the only kind of difference
that survives pressure.**

**G.4.7 · A session's product is an edit, a commit and a handoff — and the milestone is done when the
behaviour EXECUTES.** ⚰ *The reward term moved last: "a clean tree, a passing suite and a banked
ratchet still read as a finished session."* **So a session closes on the artifact the milestone
names — a hash somebody looked at, a case that ran, a falsifier that was red and is green — and not
on the document that describes it.**

**G.4.8 · An instrument may fill only what the register declares.** *A fill off the register is a
defect,* which **makes the antagonist's question a grep rather than a judgement.** ⚰ *The session
diagnosed mid-run: "it fixes errors with scripts to make them run, followed by antagonists
identifying that the scripts no longer possess fidelity to the ideal code shape" — sixteen forced
inventions, twenty-four avoidable, no fixed point.* **The register is what turns the loop into a list
with a bottom.**

---

## §G.5 · The one sentence, and how to falsify this Part

> ### **DERIVE THE SHAPE FROM THE AXIOMS WITH THE TREE CLOSED; DECOMPOSE IT BY WHO WRITES WHAT; WRITE IT IN A FORM A LOADER OR A FALSIFIER CAN EVALUATE; AND CLOSE A STAGE ONLY ON REPRESENTATIONS.**
> **Everything else in this Part is a corpse that shows what happens when one of the four is skipped.**

| claim | what would show it wrong |
|---|---|
| **G.1** — shape is fully determined by derivation | a field the admission tests admit that the game needs refused, or refuse that it needs admitted, **and** no axiom or theorem accounts for the disagreement. `F.4`'s `Tenure.degree` is the standing candidate |
| **G.2** — the owner is the unit | a value with exactly one writer whose module boundary is nonetheless wrong for a reason ownership cannot express |
| **G.3** — data and falsifiers survive, prose does not | a design statement carried correctly across three sessions **by prose alone**, with no row and no test, and still read the same way |
| **G.4.1** — stages close on representations | a stage whose forward-handed properties would have been **cheaper** to represent later than at the boundary |
| **G.4.6** — a tree-closed derivation prevents the deferral hazard | a session **with the tree closed** that still produced the existing tree with better prose. If that happens, the hazard is not scope and this Part has misdiagnosed it |
| **G.2.8** — the two-question test separates views from carriers | a value that **must be held by a consumer AND written by exactly one owner**, where making it a carrier is nonetheless wrong; or a view whose lifetime defence (D-47) is found insufficient in practice, which would mean *absence of a type* was load-bearing after all |

> ### **WHAT THIS PART IS NOT**
> **It is not a process document to be maintained.** It is a set of rules each of which names the
> corpse that would come back if it were dropped. **If a rule here ever has no corpse behind it,
> delete the rule** — a principle that has never been paid for is exactly the kind of apparatus §0.3
> measured, and this Part would rather be short than be that.
