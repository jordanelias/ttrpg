# 10 · THE PORT — Godot 4.6

## Status: PROPOSED (2026-08-31). **HELD BACK. Nothing here ratifies on merge.**
## **No Godot project was opened, no `.gd` file was parsed, no scene was run, no benchmark was taken,
## no `class_name` was registered.** `[engine]` marks a claim about **published engine behaviour**,
## not about this repository. Layer: **L4.**

---

## §1 · THE VERSION, HANDLED HONESTLY

**This document is written to Godot 4.6 as directed. It does not settle the version, because settling it
by editing prose is forbidden.** Every place the choice is load-bearing is marked and carries its
fallback.

### §1.1 What 4.6 actually buys — and the fork is mislabelled

| # | feature | since | what the shape uses it for | fallback | load-bearing? |
|---|---|---|---|---|---|
| 1 | typed `Dictionary[K,V]` | **4.4** | `Stores`, the params holder, cardinality tables | `const` name->index map + packed arrays | **yes** — the largest ergonomic win |
| 2 | `@abstract` | **4.5** | parse-time checking of role methods on the contest base | base body `push_error` + **typed error result** — needed anyway, since [engine] GDScript has no exceptions | yes, weakly |
| 3 | `WorkerThreadPool.add_group_task` | 4.0 | the parallel DELIBERATE map | identical | **no** |
| 4 | `RefCounted`, `Vector2` as a value type, `.tres` cache semantics, JSON-as-doubles, the flat `class_name` namespace, the `Container` collision | all 4.x | everything else in this document | identical | **no** |
| 5 | **any 4.6-EXCLUSIVE feature** | — | **none is named anywhere in this repository** | — | — |

> ⊕ **THE FORK IS MISLABELLED, AND RE-LABELLING IT IS THE ONE USEFUL THING THIS SECTION DOES**
> [LANE E A5]. **Nothing in this shape needs 4.6. Two things need ≥ 4.4 and ≥ 4.5.** So the decision in
> front of anyone is **4.3 versus ≥ 4.5**, and "4.6" survives only as prose — **its one
> authoritative-looking citation points at a file that does not exist in the working tree.**
>
> **The evidence is asymmetric and whoever rules should see it that way.** The 4.3 side has a declared
> project file, a CI pin, and **two executed, reproducible headless runs**. The other side is prose. **A
> version can be correct without ever having been run** — but the ledger looks like this.

### §1.2 What a version ruling does to the compile ratchet

**The 84-error baseline is a property of `(this .gd tree x the 4.3 binary x the project settings)`.**
**Two of the three factors are version-coupled**, so **under a ruling for a later version the baseline is
void until re-measured** — same method, new number, re-pin. Comparing against it would be a confounded
measurement of exactly the kind this repository has already paid for once.

> ⚠ **AND ONE CAUSAL STORY ABOUT THAT NUMBER IS REFUTED BY THE ARTIFACT IT CITES** [LANE E H1]. A widely
> repeated claim holds that a single project-setting change took the error count from 121 to 16, making
> the setting the origin of most of the 84. **The executed baseline, four lines below the passage that
> claim cites, records the opposite: the setting alone moved 169 to 161 and cleared ZERO broken scripts.
> The defects did the work.** The conclusion — that a version bump is unlikely to relax the count —
> survives on other grounds. **The mechanism claim does not, and it should stop being repeated.**

---

## §2 · PROJECT LAYOUT

**This lives in the implementation repository. Nothing here creates apparatus in the design repository.**

```
res://
  project.godot              # [autoload] — the check surface for §3
  core/                      # THE SIMULATION. Headless. NOT ONE Node in this tree.
    world.gd                 # class_name World, RefCounted — DECLARED FIRST (§2.1)
    person.gd                # class_name Person   (weight >= 1; a cohort IS this type)
    rung.gd  office.gd  site.gd  proposition.gd
    tenure_store.gd          # struct-of-arrays rows
    claim_ledger.gd          # per-person packed ledger — rows, not objects
    event_log.gd             # append-only; the invariants of §6
    query.gd                 # class_name Query — static funcs only; resolver-side take World FIRST
    rng.gd                   # the owned versioned mix + per-operation substream factory
    fixedpoint.gd            # COND_SCALE, the rounding rule, the band compare
    address.gd               # NOT `path.gd` — [engine] Path2D/Path3D exist
    loop/
      season_driver.gd       # class_name SeasonDriver, RefCounted — season(w), four barriers
      calendar.gd  matter.gd  deliberate.gd  resolve.gd  witness.gd  census.gd
    seam/
      contest_resolver.gd    # the base the deferred subsystems extend (09_THE_SEAM.md)
    params/params.gd         # class_name Params — the typed holder, loaded ONCE by the driver
  data/                      # GENERATED .tres only — never hand-authored
  game/                      # presentation. Nodes live here and ONLY here.
    main.tscn / main.gd      # owns a SeasonDriver; renders; UI signals only
  headless/
    headless_main.gd         # extends SceneTree — runs N seasons, prints the world hash, quits
  tests/
```

### §2.1 `World` is declared first, because every refusal in this suite is written against it

**`World` has been the object every rule points at and the object nobody has ever written down.** It is
the first declaration in the port for that reason: **until it has fields, "resolver-side Queries take a
World first" is a sentence rather than a signature.**

**`headless_main.gd` is the execution-artifact factory for every step in `13_EXECUTION.md`.** A step is
done when this prints a hash somebody looked at.

---

## §3 · THE AUTOLOAD RULE — the load-bearing rule of the whole port

> ### **THE `[autoload]` TABLE CONTAINS NO SIMULATION STATE AND NO SIMULATION SERVICE.**
> **Target: empty. Permitted ceiling: presentation-only — a UI signal bus, audio. `World` is constructed
> by the driver and passed by parameter. Nothing under `core/` names an autoload, ever.**

**This rejects both shipped plans, and says so rather than pretending to agree with them:** a stale
architecture document proposes a global state singleton holding "all tracked state", and the live
implementation tree uses a singleton as "the single state owner."

**The mechanism is two parts:**

1. **No live world state behind any global name** — no autoload, no `class_name` static, no `res://` path
   that resolves to one.
2. **Every resolver-side Query takes an explicit `World` as its FIRST parameter**, so calling one from
   inside `choose` **fails at the call site for want of an argument.**

> ⚠ **WHAT IS STILL NOT ENFORCED, STATED PLAINLY.** [engine] GDScript has no module system and no
> visibility modifiers, so a determined author can still `load()` a path by string. **The guarantee is
> *unreachable-by-name*, not *unwritable*.**
>
> **The port's own skeleton is the proof rather than the hypothesis**: its resolver modules reach a
> global state object and an event bus **from inside their bodies**, and one of them **writes directly
> to a field its own manifest three lines above declares unwritable.**
>
> **Do not restore stronger wording without a mechanism that earns it.** A false claim of enforcement is
> worse than none, because it stops the next reader from checking.

**Two guards are licensed by this document and no others**, because each is load-bearing on the port
rather than on anybody's process:

1. **The autoload check** — one test asserting the `[autoload]` section contains nothing from `core/`.
   **Cheap, mechanical, and it fails on exactly the recurrence it exists to catch.**
2. **The token scan** — one test asserting no file under `core/` names a global state identifier,
   matching **by file path**, not by a token that can be spelled around.

> ⚠ **AND THE RULING THIS FORCES.** State ownership and the autoload table were **reserved for Jordan**
> in the governing port spec and the reservation is still open. **It is now forced**, because the purity
> fix and the singleton pattern are direct opposites. **Until it is ruled, no port work that touches
> state ownership starts.** Recommendation attached: **rule the design's way.**

---

## §4 · FIXED-POINT ARITHMETIC — closing the last FATAL

**The claim that was wrong:** that batching delivers order-independence for additive fields. **It
delivers CLAMP-order independence.** It does not deliver **SUMMATION-order independence**, because
[engine] IEEE addition is not associative — and **the band gate makes the difference observable.**

> ### THE SPECIFICATION
>
> - **`condition` is an `int` on `COND_SCALE = 10_000`.** `COND_SCALE` is an **exported params row, not
>   a literal in a `.gd` file.**
> - **`stores` are integers in whole `MatterKind` units.** No fractional matter.
> - **`wear(kind)` is an integer in condition-units per season**, exported per site kind.
> - **Every prose coefficient crosses as an integer pair over a stated denominator**, never as a decimal.
> - **Rounding is half-up computed on the NON-NEGATIVE MAGNITUDE, with the sign applied afterwards.**
>   **This is not pedantry:** Python floors toward negative infinity and [engine] GDScript's integer
>   division **truncates toward zero**, so a naive port **silently diverges on negative deltas** — and
>   negative deltas are `wear`, which fires every season on every site.
> - **Accumulate, then clamp ONCE**, with `clampi`.
> - **Band gates compare exactly**, and a coarse mean is compared by **cross-multiplication with no
>   division**: `a * d >= c * b` rather than `a/b >= c/d`.
> - **Interior-side floats are explicitly licensed**, because they never enter an order-free accumulator:
>   `Sensation`'s two scalars, claim confidence, salience. **Consumed inside one call, stored nowhere a
>   second writer reaches.**
> - **The boundary rule, stated once so it can be checked:** **no float may enter an order-free
>   accumulator or a band gate.** Everything else is a judgment call; this is not.

**With this, order independence stops being a claim and becomes a fact** — integer addition is
associative and commutative — **and the structural test can assert BIT-IDENTITY rather than approximate
equality**, which is the only assertion that can *observe* the failure it excludes.

> **`pytest.approx` on an exactness claim is not a weak test. It is an absent one.** This repository has
> already paid for that once, when a one-ulp aggregate error crossed a degree boundary while its own
> identity test passed.

---

## §5 · CARRIER PLACEMENT

`RC` = RefCounted · `Res` = Resource + generated `.tres` · `value` = built-in value type · `row` = a
record in a store with no per-instance object.

| object | placement | why | cost |
|---|---|---|---|
| **Person** (= cohort at weight > 1) | **RC, ONE class** | interior state, high N, no tree presence. **One class is the only honouring of "no conversion operation"** | reviewers will itch to subclass a cohort — **refuse** |
| **Rung** | **RC** | state, not a widget; **containment is a Tenure edge, never node-parenting** | — |
| **Office · Proposition · Record · Date · DocketItem · Petition · Dispensation** | **RC** | low N, id-referenced, create/destroy-able | per-object allocation at low N — acceptable |
| **Site** | **RC** | `condition` is primary state | every prose formula reads a scaled int |
| **Tenure** | **row in `TenureStore`** | **the largest N in the design**; per-edge objects make every derivation an O(N) scan and pay refcount traffic **inside the parallel map** | a store API instead of object fields |
| **Claim** | **row in the owner's packed ledger** | ~200 per person; N x 200 allocations is the wrong shape | struct-of-arrays discipline |
| **Event** | **row in an append-only log** | §6 | — |
| **Act** | **RC**, one tick | — | — |
| **View** | **`PackedInt64Array` of ids** | **a view must hold ids, never references** | — |
| **Sensation** | **`Vector2`** | §5.1 | `.x`/`.y` instead of field names |
| **Stores** | **value** — MatterKind id -> int | §4 | `[4.4-GATED]` typed `Dictionary`; fallback packed pair |
| **Envelope** | **value** — `PackedInt32Array` per band | matter does not act | — |
| **Venue · door · MatterKind** | **Res + generated `.tres`** | authored world data | [engine] **`load()` returns the CACHED instance — never use `Resource` for a carrier** |
| **Query** | **`static func` on `class_name Query`** | it is not a type | flat namespace — one holder class |
| **World** | **RC, owned by the driver, NEVER an autoload** | §3 | every resolver-side call threads `w` |

**Nothing in `core/` is a `Node`.** The carriers have no transform, no visibility, no per-frame behaviour
and no child list, and the containment ladder is deliberately an **edge** rather than a parent pointer.

### §5.1 `Sensation` as `Vector2` — the strongest row, with the disclosure that was missing

[engine] **A built-in value type has no reference-bearing fields**, so *"it cannot be widened into a
masked world"* stops being a convention and becomes **a property the compiler enforces: nobody can add a
third field to `Vector2`.**

**Two qualifications, and the second was found this pass and is not in any prior document** [LANE E B7]:

1. The type prevents **widening**, not **substitution** — so the convention is fixed at the single
   construction site, `sense()`, and documented there.
2. ⚠ **[engine] `Vector2` components are 32-bit floats in a standard build.** A Python-oracle double
   round-tripping through float32 **breaks cross-language threshold parity at the last bits.** Both
   scalars are interior-side, so no world state is at risk — but **define the sensation domain so that its
   values are float32-exact** (integer basis points below 2^24), and **assert parity in the integer
   domain.** **And `Vector2` must never be reused for a world-state pair.**

### §5.2 The module tree is a DIRECTORY tree and a DATA hierarchy — never a type hierarchy

**The containment ladder is the module hierarchy in MEANING** — parent-child in the tree means
containment in the world, which is what makes it a hierarchy rather than a filing system.

> ⚠ **BUT [engine] GDScript's `class_name` namespace is FLAT AND GLOBAL.** There is no
> `Settlement.Person` and `Territory.Person`; there is **one `Person`, project-wide.**
>
> **So the ladder is a directory tree and a `Rung.kind` enum. It is not a type hierarchy, and mirroring
> it in scripts buys nothing while importing collision risk into a design with thirty-plus object
> names.**
>
> **What survives, and it is the whole point:** **one rung type, instantiated at every rung, means a
> mechanism written for elites is automatically available to populations.** That is `R-4` made
> structural — and it is structural in the **data**, which is where it belongs.

**Union types have no GDScript representation.** `Tenure.subject`, `Claim.source` and `DocketItem.matter`
are sums; the representation is **`(kind_tag: int, id: int)`**, which is also what the store wants.
**A storage discriminator is NOT a resolver branch** — say so in one line, or the first reviewer deletes
the tag and the second re-adds it as a class hierarchy.

---

## §6 · THE EVENT LOG'S INVARIANTS — adopted because they are right

**The log is not a list. It is an append-only structure with enforced invariants, and this shape adopts
the executing set because nothing better was proposed:**

| # | invariant | why it matters here |
|---|---|---|
| 1 | **id unique across the log**, raised | ids are derived, so a collision means the substream is wrong — **loudly** |
| 2 | **the type is registered and its payload matches the contract** | an unregistered event cannot enter |
| 3 | **`causes[]` may only cite ids already in the log — raises otherwise** | **the provenance chain cannot dangle**, which is what makes `06`'s arc-as-projection sound |
| 4 | **cycle-freedom by construction** for an append-only log | a walk backwards terminates |
| 5 | **season index non-decreasing** | ordering is a structural property, not a convention |
| 6 | **canonical axis and role names** | no free-text dimension keys |
| — | **a content hash over the whole log** | **the replay and parity surface**, and the control arm for every change |

**Two behaviours worth copying exactly:**

- **The termination caps are REQUIRED constructor arguments with no defaults**, so no fabricated constant
  enters. **Adopt this for the contest depth cap too** (`09` §4).
- **Exceeding a cap RAISES rather than clamps.** A breach is a loud failure. **Do not soften this into a
  silent truncation** — a truncated tick is a tick that silently means something else.

---

## §7 · DETERMINISM IN THE PORT

- **One RNG per operation, constructed from the substream, used, discarded.** **Never a shared,
  re-seeded generator** — which is the anti-pattern the existing skeleton ships and which must be deleted
  rather than copied.
- **`H` is an owned, versioned mix**, with `HASH_VERSION` in the save header. **Never the built-in
  `hash()`**, whose value is not a cross-version contract.
- **[engine] Two traps, both real:** GDScript integers are **signed 64-bit** and `<<` on a high bit
  produces a negative number; the seed field is unsigned-backed, so **never `abs()` a negative seed** —
  it drops a bit and changes the stream. **The masking must exist identically in the Python oracle.**
- **[engine] JSON loses integer precision above 2^53.** **Ids cross as strings or as `store_64`, never as
  JSON numbers** — a corrupted id dangles three loads later, far from its cause.
- **`purpose` must be unique per DRAW, not per operation.**
- **No `randomize()`, no wall-clock read, no unsorted dictionary iteration feeding a draw or a sum**, in
  any step.
- **The parallel map writes `acts[i]` into a pre-sized array. It never appends.**

**Cross-language parity is asserted in the INTEGER domain**, which is what makes it assertable at all.

> ⚠ **AND THE ORACLE-SIDE GAP THIS DEPENDS ON.** The Python reference **has no substream
> implementation today** — it draws from one campaign stream. **Parity is Event-level and
> threshold-level until it does**, and the substream is a precondition of the person loader rather than
> a follow-up to it, because **a loader drawing from the shared stream moves every golden for reasons
> that have nothing to do with the people it added.**

---

## §8 · SAVE AND LOAD

**Two incompatible models are shipped in the corpus** — initial-conditions-plus-log replay, and a state
snapshot. **They are different load paths and cannot both be the format.**

> **RULED: THE SNAPSHOT IS THE SAVE FORMAT.** The event log is retained **for provenance and for the
> interface's history surfaces**. Re-run-from-seed stays a **test device**, where it is genuinely
> valuable — it is how byte-identity controls are taken — and **is not the player-facing load path.**
>
> **Ground:** replay-as-save makes every load O(campaign length) and makes any post-hoc balance fix
> **unloadable** — the old log no longer replays to the same world under new code.
>
> ⚠ **This amends a Jordan-vetoable spec that says the opposite, so it is flagged loudly rather than
> folded in.** It is one sentence to rule and a rewrite to leave.

**Mechanics, and each is a silent-corruption story avoided:**

- **Save as data, not as scripts.** [engine] **`.tres` carries a script path and is an execution surface,
  and the resource cache hands back a previously-loaded instance.** `.tres` is right for **generated
  authored data** under `data/` and **wrong for a save file** — and wrong twice over for a shared one.
- **Explicit serializer over `FileAccess`**, with a header carrying magic, format version, `HASH_VERSION`,
  `world_seed` and `tick`.
- **Ids are STORED, never recomputed at load.** They are derived from `(world_seed, tick, subject_id,
  purpose)` and all four are in the snapshot, so recomputation *would* work — **and the moment a
  `purpose` string changes, every id in every old save silently forks.**
- **Nothing derived is serialized:** no Query result, no barrier-built index, no View. **A serialized
  cache is a stored aggregate that survives a reload.**

---

## §9 · THE PARAMS PIPELINE

1. **Stage 1 — the authored source and its exporter, with a BLOCKING round-trip check in CI.** This is
   the transport between the two repositories, and it is the pattern this repository has already proven
   seven times.
2. **Stage 2 — a generator reading stage-1 output and emitting `res://data/*.tres`.** **`.tres` under
   `data/` is never hand-authored.** Ids and fixed-point values cross as **strings and ints**, never as
   JSON floats.
3. **Stage 3 — `Params`, a RefCounted holder loaded ONCE by the driver and read by value.**

**The rows this shape owes the pipeline before any code reads them:** `COND_SCALE` · `wear` per site
kind · `OB_MIN` · the per-band integer coefficients · the ledger cap `L` · the view budget `K`'s terms ·
the `Ob > 2 x Pool` refusal threshold · the publicity and attention coefficients of `07` §5.2 · the
commitment-degree weights · `season_factor`'s distribution (**open**).

> **Until each has an exported row it is reference, and it may not be transcribed by hand into a `.gd`
> literal.** A number in a source file is a number nobody can change without a code review, and a number
> in two source files is two numbers.

---

## §10 · THE SKELETON — judged

**It covers one of twenty-seven modules and does not compile.** It extends base classes and calls
services **defined nowhere in the corpus.**

> **It is not a head start and must not be presented as one.** Its value is entirely as **evidence of
> what a resolver module in this port actually reaches for** — which is how the purity problem was
> **proven rather than hypothesised**.

**One concrete defect, verified and worth fixing wherever this code goes:** a module **writes directly to
a field its own manifest declares unwritable**, three lines above, under an explicit guard comment.

> ⊕ **AND THE PROPOSED ONE-LINE FIX IS INSUFFICIENT** [LANE E H4]. Deleting the write breaks the slice,
> because **that illegal write is the slice's only termination input** — the fight-over check reads the
> same field. **The fix is two files: delete the write, and derive the value from the accumulated damage
> instead.** *A one-line fix that silently breaks a termination condition is worse than the defect.*

**Disposition: keep as reference; rewrite rather than extend.**

---

## §11 · HOSTILE VERSUS MERELY UNIDIOMATIC

**A Godot-fluent reviewer will propose four edits. Two are right and two would destroy the design.**

| they will say | verdict |
|---|---|
| *"use object references instead of ids"* | **REFUSE.** [engine] No cycle collector; the reference graph is **cyclic by construction** — the heir lives in the hearth. **This is an unbounded leak in the object graph the game is made of** |
| *"make the carriers Resources so they serialize for free"* | **REFUSE.** The resource cache hands back a shared instance and `.tres` is an execution surface |
| *"use signals for the witness fan-out"* | **REFUSE.** Three independent grounds; a subscription table is a stored aggregate, and it materialises the broadcast the design refuses |
| *"drive the season from `_process`"* | **REFUSE.** The driver is explicit and headless; a frame-driven season cannot be run 50 times in a test |
| *"type the collections"* | **ACCEPT** — that is what §1.1 row 1 is for |
| *"stop `abs()`-ing the seed"* | **ACCEPT** — it drops a bit |
| *"delete the write to the read-only field"* | **ACCEPT, and read §10 first** |
| *"the Query holder class is a god object"* | **ACCEPT the smell, REFUSE the fix.** It is static functions in a flat namespace, which is what GDScript supplies. **Splitting it by rung reintroduces the type hierarchy §5.2 refuses** |
