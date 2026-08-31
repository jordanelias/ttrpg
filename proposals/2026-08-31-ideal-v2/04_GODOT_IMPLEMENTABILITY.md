# GODOT IMPLEMENTABILITY — the port axis

## Status: PROPOSED (2026-08-31). **Nothing here has executed.** No Godot project was opened, no
## `.gd` file was parsed, no scene was run, no benchmark was taken, no `class_name` was registered.
## Every claim below is an argument about text — the design's text, this repository's text, and the
## published behaviour of the engine. `CLAUDE.md` §0.2 applies in full: **done means it runs, and
## none of this runs.** Where a claim would be settled by opening a project, it is marked as
## unsettled rather than asserted.

---

## §0 · WHAT THIS IS, AND WHAT IT MAY NOT DO

**What it is.** One axis only: **can `01_ARCHITECTURE.md` and `02_THE_SEASON_LOOP.md` be built well in
Godot — as a modular game assembled from primitives with centralized data — and where they cannot, what
exactly must change?** Factuality and internal consistency are another reader's job and are not
duplicated here. Where this document disagrees with the design it says whether **the design is wrong**
or **the design is right and the port is hard**, because the two have opposite remedies.

**What it may not do.**

- **It proposes no repository apparatus.** No validator, guard, register, checker, freshness gate or
  process document (`11_code_shape.md:243-245`). Everything recommended below is a shape *inside the
  game*: a parameter list, a class base, a file format, a summation order. Where it recommends the
  **existing** typed-export pipeline (§5), that is not new apparatus — `CLAUDE.md` §0.05 names *"an
  exporter with a blocking `--check` round-trip"* as **mechanism**, and `CLAUDE.md` §0.1 point 5
  explicitly KEEPS `export_engine_params.py --check` because it produces the bridge the port ingests.
- **It asserts no measurement.** No number below was produced by running anything. Cost claims are
  stated as **operation counts over declared quantities**, never as timings.
- **It asserts no engine version.** `CLAUDE.md` §3 records the version as UNRESOLVED — `project.godot`
  declares 4.3, this repository and `godot/` say 4.6 — and forbids picking one. **Exactly three
  recommendations below are version-gated, and each carries its fallback inline** (§5 typed
  `Dictionary`, §8 `@abstract`, §6 `WorkerThreadPool` ergonomics). Everything else holds across the
  whole 4.x line.

### §0.1 Citation key

| form | resolves to |
|---|---|
| `01:NNN` · `02:NNN` · `03:NNN` | line NNN of the numbered document in this directory |
| a bare repo path with `:NNN` | line NNN at the working tree, per `CLAUDE.md` §2 |
| `STRAT:NNN` | line NNN of `godot/godot_conversion_strategy_v1.md` — the governing port spec, **PROPOSED** |

### §0.2 What is true of the port target before anything is judged

Stated once so no finding below has to re-establish it.

- **The governing spec is PROPOSED with unexecuted Gate-0 preconditions** — KeyStore v2, base classes,
  the seeded RNG service (`STRAT:177-184`). Nothing in it is a ratified contract.
- **`godot/skeleton/` covers 1 of 27 modules and does not compile.** It `extends` `BaseEngine`,
  `EngineModule`, `Key`, and calls `GameState` and `KeyBus`, none of which are defined in the corpus
  (`godot/README.md:11`, `combat_engine.gd:13`, `strike_module.gd:21`). **It is not a head start.** It
  is, however, the only executable-shaped statement of intent that exists, and §3 uses it as evidence
  of what a resolver module in this port *actually reaches for*.
- **`references/module_contracts.yaml` carries 27 modules, 9 with `doc: null`** — parsed, not grepped:
  `npc_memory, scene_slate, game_director, scene_timer, audit, domain_actions, settlement_economy,
  engine_clock, scenario_authoring`. `engine_clock` — the temporal spine — is one of them
  (`references/module_contracts.yaml:1128-1136`).
- **The four 2026-04-18 docs are STALE** and each says so (`godot/scene_tree_architecture.md:3-6`).
  They are read below for what was *intended*, never for what is true.

---

## §1 · THE VERDICT, IN ONE PAGE

**The design is buildable in Godot, and it is buildable well — as a headless value-graph transaction
that never touches the scene tree.** That is not a hedge: the four carriers have no transform, no
visibility, no per-frame behaviour and no child list, and the containment ladder is deliberately an
edge rather than a parent pointer (`01:280-298`). A simulation shaped like that wants `RefCounted` and
packed value arrays, and Godot serves both well.

**Four things cannot be built as specified. Two of them are one defect wearing two hats; the third is a
name; the fourth is arithmetic.**

> **THE ONE DEFECT, STATED ONCE. The design's enforcement mechanism is *the absence of a parameter*
> (`01:564-567`, `02:756`). In Python that is a real constraint, because a name a function did not
> import and was not passed is genuinely not in its scope. In GDScript it constrains nothing: there is
> no module system, no visibility modifier, no import graph, and no way to make an identifier
> unreachable from a function body. Every autoload and every `class_name` is a global identifier
> resolvable from any script — `RefCounted` and `Resource` included, not only `Node`.**

So **both** claims of the form *the type system makes X unwritable* — `choose`'s missing `World`, and
the witness collection form — are false in GDScript. The third FATAL is that the design's central
object cannot carry the name the design chose for it, on the very ground it chose it. The fourth is
arithmetic rather than linguistic: order-independence of `additive` fields does not survive IEEE
floating-point addition, and the design conflates *clamp*-order independence (which batching does
deliver) with *summation*-order independence (which it does not).

| rank | count | what they are |
|---|---|---|
| **FATAL** | **4** | the purity guarantee (§3) · the witness collection form (§4) · the name `Container` (§2) · `additive` order-independence (§6.5) |
| **MAJOR** | **16** | buildable, and will be rewritten later if built as written |
| **MINOR** | **9** | real, cheap, and will not force a rewrite |
| **OBSERVATION** | **6** | where the design is right, sometimes for a reason it did not know it had |

**The full register is §11.** Each section below carries its own findings inline with their ids.

---

## §2 · CARRIER PLACEMENT — Node, Resource, RefCounted, or value (Q1)

> **NOTHING IN THE SIMULATION IS A `Node`. NOT ONE OBJECT.** This is the single most expensive
> decision in the port and it goes the same way for all four carriers, the edge, the act, the claim
> and the query category.

**Why, in four consequences rather than by taste.**

1. **A `Node` can reach `get_tree()`, `get_parent()` and the whole scene from any method.** That is
   the mechanism §3 is about; making a Person a Node hands every future `choose` implementation the
   world for free.
2. **`Node` lifetime is frame-scoped, and `efface` is barrier-scoped.** `queue_free()` runs at the end
   of the frame; `free()` mid-iteration invalidates references. `efface` sets `until = tick` on every
   Tenure naming the id **in the same resolution step** (`01:732-737`, `02:579-585`). A deferred
   destructor and an instantaneous cascade cannot be made to agree without a second lifecycle.
3. **`Node` allocation is the heaviest thing Godot offers**, and the design's population is the one
   quantity it never bounds (§6.6).
4. **The scene tree is a rendering structure.** The design's containment ladder is a `Tenure` edge
   precisely so that *"a hamlet does not move because a King won a war"* (`01:286-292`). If Container
   were a Node and containment were node-parenting, the first `reparent()` anybody writes contradicts
   the architecture's central ontology.

### §2.1 The table

`RC` = `RefCounted` · `Res` = `Resource` · `value` = a built-in value type (`Vector2`, packed arrays,
int/float/`StringName`) · `row` = a record inside a store, with no per-instance object.

| object | declared at | Godot form | why |
|---|---|---|---|
| **Person** | `01:144`, `03:129` | **RC**, one `class_name` | interior state, high N, no tree presence, must not be reachable by name |
| **Cohort** | `01:478`, `03:130` | **the SAME `class_name` as Person**, `weight ≥ 1` | *"exactly one type with an individuated person"*, *"no conversion operation exists"* (`01:482-483`, `02:401-403`). **Two `class_name`s is the rule broken at declaration** — see M-10 |
| **Container** | `01:145` | **RC** — under a different name, see F-3 | a rung is state, not a widget and not a tree node |
| **Office** | `01:146` | **RC** | low N, referenced by id |
| **Site** | `01:148` | **RC** | `condition` is primary state written only at RESOLVE (`01:173-176`, `02:986`) |
| **Tenure** | `01:228` | **`row` in a `TenureStore` RC** | every disputable political fact is one of these; N is the largest object count in the design, cardinality is per kind, and the object-side index is derived (`01:238`). One object per edge makes every derivation an O(N) scan — see §6.4 |
| **Act** | `01:309` | **RC**, one tick | returned by value from the map; N = individuated persons |
| **touch** | `01:310` | **value** — a 4-field struct-of-arrays inside the Act | `(target, mode, field?, delta?)`; the conflict rule reads only these four (`02:454-458`) |
| **spec** | `01:313` | **value** | mint-only payload |
| **Claim** | `03:223` | **`row` in the owning Person's packed ledger** | budget `L = 200` per person (`03:143`); one object per claim is `N × 200` allocations. Struct-of-arrays; see M-4 and §6.6 |
| **Event** | `03:80` | **`row` in an append-only log** | the substrate precedent already does exactly this (`engine/substrate/keys.py:145`, `379-392`) |
| **Proposition** | `03:82` | **RC**, interned by structural equality | *"it persists as long as anything names it"* — never effaced |
| **Record** | `01:813` | **RC** | matter at a Container; `efface`-able |
| **Date · DocketItem · Petition · Dispensation · ConveningCondition** | `01:841-845`, `01:1082` | **RC** | low N, referenced by id, minted by acts |
| **Case · Ground** | `01:903-904` | **RC**, one sitting | transient per sitting |
| **Venue · door** | `01:905-908`, `03:257-260` | **`Resource` + `@export` + `.tres`** | **authored world data** (`03:85` *"authored"*), 12 + 5 fields — the exact shape `@export` serves, and the exact shape `combat_config.gd:11-40` already proves |
| **MatterKind** | `01:1278` | **`Resource`** | authored, `never` effaced (`03:97`); a small generated `.tres` set |
| **Stores** | `01:1277` | **value** — `Dictionary[MatterKind id → int]`, fixed-point | see §6.5 on why not float |
| **Envelope** | `01:479` | **value** on the Container — `PackedInt32Array` counts by band | matter, does not act (`01:471-473`) |
| **Sensation** | `01:583` | **`Vector2`** — a built-in value type | see below; this is the strongest recommendation in the table |
| **View** | `03:93` | **value** — `PackedInt64Array` of claim ids | *"assembled, not filtered"* (`02:348-352`); it must not hold object references |
| **Candidate** | `01:625` | **value** | `(verb, target_spec[], believed_obstacle_band)`; not an Act (`02:380-382`) |
| **Derived / the query category** | `01:404`, `03:544` | **`static func` on a namespace class — NOT a type, and NOT named `Derived`** | see M-1 and M-2 |
| **World** | `03:463` (`⛔`, G-13) | **RC**, owned by the driver, **never an autoload** | see §3 |

### §2.2 `Sensation` as `Vector2` — the one place the design's own argument gets stronger in Godot

The design argues that `Sensation` clears §14 row 1 because *"it is two floats… and it is checkable by
reading the type"* (`01:1450`). In GDScript that argument can be made **exact rather than rhetorical**:

```gdscript
# subsistence = x, standing = y.  A Vector2 is a built-in VALUE type: it has no fields that
# can hold a reference, so "it cannot be widened into a masked world" stops being an argument
# and becomes a property of the type the compiler already enforces.
func choose(p: Person, view: PackedInt64Array, sensation: Vector2) -> Act:
```

⚠ **A `class Sensation extends RefCounted` throws this away.** The moment `Sensation` is an object,
somebody adds a third field, and nothing at the call site says a rule was crossed — which is exactly
the failure `02:1011-1016` names against itself. **`Vector2` is the enforcement; the record is not.**

### §2.3 Findings

- **F-3 · FATAL — the object cannot be named `Container` in Godot, and the design's ground for the
  name is inverted.** `01:151-156` and `03:642` refuse `Node` because it *"collides head-on with the
  port target"* and adopt `Container` on that ground. **`Container` is itself a built-in Godot class**
  — the `Control`-derived base of `VBoxContainer`, `HBoxContainer`, `GridContainer` and the rest — and
  `class_name Container` is refused at parse for shadowing a native type. The collision register
  closes the `Node` row (`03:642`) and opens an identical one it did not check. *(Not executed: no
  project was opened to confirm the parse error. The name's occupancy is a fact about the engine's
  class list in both 4.3 and 4.6, so this finding is version-independent.)* **Fix: rename before the
  word reaches a `class_name`.** `Rung` is the design's own gloss (`01:151`, *"Container (a rung)"*)
  and passes both of `CLAUDE.md` §4's tests; a prefix (`ValoriaContainer`) passes neither and should
  not be taken.
- **M-10 · MAJOR — Person and Cohort must be one `class_name`.** *"A Cohort is a Person record at
  weight > 1 — no conversion operation exists"* (`01:482-483`). GDScript gives exactly one place to
  honour that and one place to break it. Two classes, or a `Cohort extends Person`, both re-introduce
  the conversion the design deleted; `03:145`'s *"at weight 1 the record IS a person"* is then a
  comment rather than a fact.
- **M-14 · MAJOR — `Container.matter` is untyped and must be typed before anything is written**
  (`03:149`, G-14). It is asked to hold five distinct kinds and four are addressed *by name* from
  elsewhere. In GDScript an untyped field is a `Variant`; every read is a dynamic lookup returning
  `Variant`, and static typing — the port's engineering floor (`STRAT:41`) — cannot reach inside it.
  This is the one field that blocks the carrier layer.
- **m-5 · MINOR — `Resource` is for tables, never for a carrier.** `load()` returns the **cached**
  instance for a path, so two loads share one object; a `Resource` used as per-entity runtime state is
  silently shared unless `.duplicate()`d at every site. `combat_config.gd` and `longsword.tres` are
  the correct use; a `Person.tres` would be the incorrect one.
- **m-8 · MINOR — `Site.drawers[]` is stored while `judging_set(c)` is derived**, and the two are the
  same shape. `01:148` stores the drawer list; `01:437` deletes *"a stored membership list"* for the
  judging set. `share(actor, site)` and `draw_share` (`03:566-567`) can both be computed from the draw
  relation. Deriving it removes one update path that can disagree with the Tenure set.
- **m-3 · MINOR — `Person.address → Path`** (`01:442`, `03:570`). `Path` was a Godot 3 class name,
  removed in 4.x in favour of `Path2D`/`Path3D`; the bare word is free but sits one letter from two
  built-ins in a codebase full of trees. `Address` is the idiomatic word and the design already uses it.

---

## §3 · THE PURITY PROBLEM (Q2)

**This is the question the design stakes itself on, and it is where the port is hardest.**

### §3.1 What the design claims

> `choose : (Person, View, Sensation) -> Act` — *"NO World, ever"*; *"not masked, not read-only, not
> behind an accessor"*; *"these are the enforcement mechanism and they work by what they omit"*
> (`01:559-567`). And, of the fan-out form: *"§14 row 3 is not a rule the resolver checks; it is a
> shape the type system makes unwritable"* (`02:754-756`).

### §3.2 Why the claim is false in GDScript — three mechanisms, none of which is `Node`

**⚠ The framing in the brief that commissioned this audit is one step too narrow.** It asks whether
the guarantee survives because *"any `Node` can call `get_tree()`"*. The scene tree is the **least** of
it, and avoiding `Node` (§2) closes only that door. Three doors remain, and all three are open to a
`RefCounted`:

1. **An autoload is a global *identifier*, not a Node privilege.** Registering `GameState` in project
   settings makes the bare token `GameState` resolve inside **every** script in the project —
   `RefCounted`, `Resource`, static function, inner class. The port's own skeleton is the proof, and
   it is not hypothetical: `strike_module.gd:38-39` calls `GameState.get_actor(...)` from inside a
   resolution module, `:67` writes `GameState.rng.seed`, `:86-90` reads `GameState.new_key_id()` and
   `GameState.season_index`, `combat_engine.gd:60` calls `KeyBus.emit_key(k)`, and
   `wound_module.gd:40` reaches `GameState.get_actor` again. **The one module that exists for this
   port already does, from inside a resolver, exactly what `choose` is forbidden to do.**
2. **`class_name` is a flat global namespace.** Any `static func` on any registered class is callable
   from any body. `Query.presence(prop, c)` compiles inside `choose` with no parameter and no import.
3. **`preload()` / `load()` take a string.** `load("res://state/world.tres")` inside `choose` returns
   the cached live instance, and no signature anywhere records that it happened.

GDScript has no `private`, no module-private, no package, no friend, no import graph and no way to
scope a name out of a body. **The parameter list is the only thing the design controls, and the
parameter list controls nothing about what the body may reach.**

- **F-1 · FATAL — the guarantee, *as an enforcement mechanism*, cannot be built in GDScript.** The
  design is not wrong about what it wants; it is wrong about what carries it. `02:1011-1016` already
  half-admits this — *"nothing enforces it structurally except the absence of a `World` in `choose`'s
  signature"* — and that sentence is the whole of the enforcement in Python and none of it in GDScript.

### §3.3 What CAN be preserved, and it is very nearly as strong

**The guarantee moves from the type system to the name table.** Not a downgrade to nothing — a
downgrade from *unwritable* to *unreachable-by-name*, which is a different, weaker, but genuinely
structural property, and it is checkable by a human reading one screen of project settings.

> **THE RULE, STATED ONCE. NO LIVE WORLD STATE MAY BE REACHABLE BY A GLOBAL NAME.** No autoload holds
> it. No `class_name` static holds it. No `res://` path resolves to it. **The world is a `RefCounted`
> constructed by the season driver and passed down the RESOLVE path by parameter, and DELIBERATE is
> the one place it is not passed.** Then `choose`'s body has nothing to reach, not because a type
> forbids it, but because no identifier names it.

**And the second half, which is the cheap one and which the design should adopt outright:**

> **EVERY RESOLVER-SIDE `Derived` TAKES `World` AS ITS EXPLICIT FIRST PARAMETER. EVERY PERSON-SIDE
> `Derived` TAKES THE ASKING PERSON AND NOTHING ELSE.** Then calling a resolver-side query from inside
> `choose` fails for want of an argument, at the call site, in the reader's face.

```gdscript
# resolver-side — 12 of the 20 rows of 01:422-443.  Unreachable from choose(): no `w` in scope.
static func presence(w: World, prop: int, c: int) -> int:
static func judging_set(w: World, c: int) -> PackedInt64Array:
static func verbs(w: World, site: int, c: int) -> PackedInt64Array:      # world truth, 01:609

# person-side — 5 rows.  Takes no world and cannot acquire one.
static func opening_set(p: Person, view: PackedInt64Array) -> Array[Candidate]:
static func leaders(observer: Person, prop: int, c: int) -> PackedInt64Array:
```

- **M-2 · MAJOR — the side column is a table when it could be a parameter list.** `01:417-420` calls
  the resolver/person split *"the design's central rule"* and then carries it in a documentation
  column (`01:422-443`, `03:550-571`). Nothing in any signature records the side. **Putting `World`
  first on the resolver-side rows converts the design's own enforcement philosophy — constraint by
  omission — from the three top-level signatures, where it is already applied, to the twenty queries,
  where it is not.** This is the highest value-per-character change in the audit.
- **M-13 · MAJOR — the port's existing plan destroys this on day one.** `godot/scene_tree_architecture.md:16`
  makes `GameState` an autoload holding *"all tracked state"*, and `STRAT:97` records the live tree's
  `Meta` autoload as *"the single state owner"*. **Both are the exact shape the rule above forbids.**
  The port's autoload ruling is still open (`STRAT:213`, Part VIII #5), so this is a live decision and
  not a fait accompli — but it must be decided **for this reason**, which is not currently among the
  reasons on the table.
- **O-6 · OBSERVATION — `World` is the one type in the design with no record** (`03:463`, G-13), and
  it is the type every one of the fourteen refusals is written against. In a statically typed port it
  is the first type you must declare, and its field list *is* the answer to *what may a resolver
  reach*. Declaring it is not documentation work; it is the boundary.

### §3.4 What does NOT close it, so nobody spends a week on it

- **Threads do not sandbox.** `WorkerThreadPool` runs GDScript with the same global identifiers.
- **Inner classes do not scope.** A `class Foo:` inside a script is invisible *outward*, not inward;
  its body still sees every autoload.
- **`@tool`, `@onready`, static typing, `Callable` indirection** — none of these remove a name.
- **A wrapper that hides the world behind an accessor is explicitly refused by the design itself**
  (`01:565`: *"not behind an accessor"*), and correctly so: it is `view_of(world, person)` with extra
  steps, which is §14 row 2.

---

## §4 · SIGNALS, AND FAN-OUT BY PRESENCE (Q3)

### §4.1 Where signals belong: nowhere in the simulation, and the port already ruled it

> `STRAT:128`, verbatim and load-bearing: *"the EventBus carries **UI/lifecycle signals only** —
> **signals are not Keys** (Keys are persisted facts; signals are transient wiring)."*

**That line is already the answer, it is already in the governing spec, and the new design should
inherit it by citation rather than re-derive it.** Signals are for presentation: a view observing that
a barrier completed, a camera following a resolved contest, a log panel appending. **No simulation
state is ever written by a signal handler.**

### §4.2 Why signals are wrong for `witness`, on three independent grounds

1. **Shape.** `emit_signal` delivers one payload to N connected receivers. If the receivers are
   persons, that is §14 row 3's forbidden form, materialized (`01:1395`, `02:754-756`).
2. **Presence is a computation, not a subscription.** `reach(e)` is *persons present + persons a
   channel carries to at that channel's latency + Knot partners reusing the event's own id*
   (`02:731-734`). Presence changes every season. Expressing that with connections means
   connect/disconnect traffic proportional to persons × events × seasons, which is strictly more work
   than the loop it replaces and buys nothing.
3. **Order.** Signal invocation order is a hidden global order, and it is synchronous and re-entrant —
   a handler that emits recurses immediately. The design requires order independence (`02:1000-1009`),
   and the Python substrate carries an explicit re-entrancy meter and a Level-B termination guard for
   exactly this hazard (`engine/substrate/keys.py:1-45` docstring, propagation_spec §4.2). **Signals
   give you no meter and no cap.**

### §4.3 The shape that works

Two passes, matching the design's own split — *"the fan-out is global; the deposit is per person"*
(`02:94`, `02:744-748`):

```gdscript
# WITNESS step 1 — global, one pass, no signals, no subscription table.
func fan_out(w: World, events: PackedInt64Array) -> Dictionary:      # person_id -> PackedInt64Array
    var reach := {}
    for e in events:
        for pid in w.presence_index.at(w.place_of(e)):               # built at MATTER, never lazily
            reach.get_or_add(pid, PackedInt64Array()).append(e)
        for pid in w.channel_index.carried(e, w.tick):               # latency-gated
            reach.get_or_add(pid, PackedInt64Array()).append(e)
        for pid in w.knot_partners_of(e):
            reach.get_or_add(pid, PackedInt64Array()).append(e)      # REUSES e's id — 02:750-752
    return reach

# WITNESS step 2 — per person, any order, writes one ledger.
func witness(p: Person, event_id: int) -> void:                      # 03:462 — never a person SET
```

- **F-2 · FATAL — *"a consensus broadcast is a type error"* is false in GDScript.**
  `func witness_all(ps: Array[Person], e: int)` is as easy to write as the correct form and as easy to
  type-annotate. `02:756`'s claim — *"a shape the type system makes unwritable"* — does not transfer.
  **What replaces it is weaker and real: `witness` has exactly ONE call site, in one file, inside the
  step-2 loop above.** A second call site is a diff a reader can see; a second *signature* is not
  prevented by anything. **The design should restate the guarantee as a call-site property**, because
  a claim that a type forbids something, when it does not, stops the next reader from checking.
- **m-7 · MINOR — say where signals DO go, once.** The design mentions signals nowhere. Silence in a
  Godot-facing design reads as permission, and `emit_signal` is the first thing a GDScript author
  reaches for when a fan-out is described. One sentence citing `STRAT:128` closes it.

---

## §5 · CENTRALIZED DATA (Q4)

### §5.1 The four candidate shapes, judged

| shape | right for | wrong for | evidence |
|---|---|---|---|
| **`Resource` + `@export` + `.tres`** | authored, designer-tunable, low-cardinality tables — `Venue`, `MatterKind`, band floors, `f(degree)` | anything hand-edited that also has a generator; per-entity runtime state | `combat_config.gd:11-40` is the correct use; `combat_config.gd:5-9` records the defect it fixed — two scales, one live, one dead, and editing the dead one changed nothing |
| **a data autoload** | read-only constants loaded once | anything holding live world state — §3's rule | — |
| **generated GDScript `const`** | hot scalars read every roll | anything a designer tunes without a rebuild | constant-folded, typed, and impossible to hand-edit invisibly |
| **`engine_params/*.json` at load** | the transport between the two repositories | the runtime read path — every lookup returns `Variant`, and int64 loses precision (§9.3) | ten artifacts exist today under `engine/engine_params/` |

### §5.2 The ruling

> **THE PIPELINE HAS FOUR STAGES AND ONE GENERATOR PER STAGE BOUNDARY: code or authored prose →
> `engine/engine_params/*.json` (exists, behind a blocking `--check`) → generated `res://data/*.tres`
> (NEVER hand-authored) → one typed `RefCounted` holder, loaded once, owned by the driver, read by
> value.** The `.tres` layer exists so a designer can inspect and a diff is legible; the JSON layer
> exists because it is where the round-trip gate already lives.

**This is not a new recommendation — it is the one the port already made and has not executed.**
`STRAT:149`: registries *"Generated from the ttrpg yaml by the export ritual — **never hand-transcribed**"*.
`STRAT:151`: *"Generated, generator-stamped export per system → `res://data/<system>_params.tres|json`"*.
And the cost of not doing it is measured in this repository's own words: the port's current answer to
the 55-type Key registry is *"four files, HAND-MADE, covering 4 of 55 types… **93% incomplete before it
has even started drifting**"* (`tools/export_key_types.py:17-19`, restated at
`engine/substrate/keys.py:194-195`).

### §5.3 What this design specifically owes the pipeline

- **M-8 · MAJOR — the design defines its numeric constants in prose and names no artifact for any of
  them.** A partial roster, all currently prose-only: `f(degree) = 0 · 0 · 1/16 · 1/8 · 1/4`
  (`02:598`); `K = 7 + Focus + 2 per Knot − Coherence penalty`, and `K = 3` per cohort (`02:340`,
  `02:346`); `stanceweight = clamp(1 + (obstinacy/5)·agreement, 0.05, 2.0)` (`02:343`);
  `(3 + d10)/8.5` (`03:527`); `entrenchment = min(1, seasons_held/60)` (`03:536`);
  `bandwidth = max(0, 2 − floor(strain/3))` (`03:539`); `L = 200` (`03:143`, marked ASSUMPTION);
  `Obstacle > 2 × Pool` refuses the roll (`02:540`); the five degree bands (`03:293`).
  **Under `CLAUDE.md` §0.05 every one of these is reference today and mechanism nowhere**, and the
  documents say so about themselves (`01:1713-1715`). Naming the artifact costs one row per constant
  and is the difference between the design being ingestible and being transcribed by hand.
- **m-4 · MINOR — `@export var qual: Dictionary` is untyped at the value level.**
  `combat_config.gd:29-38` ships four such fields and every read casts (`float(cfg.qual[quality])`).
  **Version-gated:** typed `Dictionary` exists in later 4.x and removes the cast. **Fallback, which
  works everywhere and is what the port already prescribes for the conviction vectors (`STRAT:150`):**
  a typed array plus a `const` name→index map.
- ⚠ **Do not lift a number out of `params_tables.yaml`.** The compendium already carries this warning
  (`03:868-871`) and `CLAUDE.md` §5 carries it harder: the capture is a byte-frozen snapshot of prose
  that can no longer be regenerated, and its *Degrees of Success* section holds a **pre-ruling**
  ladder. **The code is the formula.**

---

## §6 · THE SEASON LOOP IN ENGINE TERMS (Q5)

### §6.1 Not `_process`. An explicit driver, headless, on a `RefCounted`

A season is a discrete transaction with four synchronisation points (`02:29-78`). `_process` is
frame-driven and offers no barrier. **The driver is a plain function on a `RefCounted`, callable with
no scene tree at all** — which is already the port's engineering floor (*"kernel scene-tree-free"*,
`STRAT:41`; *"Build… scene-tree-free and headless-testable"*, `STRAT:184`).

```gdscript
func season(w: World) -> void:
    calendar(w)                       # barrier · writes dates, dockets
    matter(w)                         # barrier · writes larders, bodies, travel, yield, envelope
    w.freeze()                        # 02:246 — and see M-3: every index is BUILT HERE, never later
    var acts := deliberate_map(w)     # map · pure · any order
    resolve(w, acts)                  # barrier · writes everything else
    witness(w, w.events_this_tick)    # barrier · global fan-out, then per-person interior
    census(w)                         # global pass, shares WITNESS's join
```

A `Node` appears exactly once in the whole simulation, at the outermost layer, to give the driver a
callback and to own the presentation. **If a season exceeds a frame budget, the barriers are the
natural yield points** — `await` between steps slices it across frames without threading. `await`
resumes on the main thread, so it buys responsiveness and no parallelism.

### §6.2 Is the parallelism claim realisable? Yes, and it is bounded by refcounting, not by GDScript

`WorkerThreadPool.add_group_task()` is the idiomatic data-parallel primitive and GDScript genuinely
runs on worker threads — there is no interpreter-wide lock of the CPython kind. **The binding
constraint is different and specific: every assignment of a `RefCounted` reference performs an atomic
refcount operation.** A per-person map that walks an object graph of 200 claim objects, N tenure
objects and a view of object references pays atomic traffic on every hop, across every core, on shared
cache lines. **The speedup is real and it is eaten by refcounting unless the hot per-person data is
value-typed** — packed arrays, ints, floats, `Vector2`.

> **THIS IS WHY §2's TABLE PUTS CLAIMS, VIEWS, TOUCHES AND `Sensation` IN VALUE TYPES.** The parallelism
> licence at `02:118-135` is a licence about *observation*; the thing that makes it *pay* is a
> representation decision the design does not make.

### §6.3 The three hazards inside the frozen map

- **M-3 · MAJOR — a lazily-built cache inside the map is a data race, and the design's purity claim
  does not cover it.** `02:246` freezes the world; freezing prevents writes to *state*. A resolver-side
  `Derived` that memoizes — a presence index, a `judging_set`, a `draw_share` denominator — **writes to
  a cache while N threads read it.** The design calls these functions pure (`01:404`) and says nothing
  about memoization, and R-1's *"compute-on-demand, never push, never store"* (`01:406`) is read by
  most engineers as licensing a cache. **State the rule:**

  > **A DERIVED MAY BE CACHED. THE CACHE IS BUILT AT A BARRIER, READ-ONLY UNTIL THE NEXT BARRIER, AND
  > DISCARDED THERE. NOTHING INSIDE A MAP BUILDS ONE.** A barrier-scoped rebuild-from-primary-state is
  > compute-on-demand at barrier granularity; it stores no state that can go stale, because it does not
  > survive the barrier. **A cache built inside the map is both a race and a stored aggregate.**

- **M-11 · MAJOR — a parallel map must not `append`.** Under `add_group_task` the completion order of
  elements is unspecified, so `acts.append(a)` produces an act array whose order varies run to run,
  and every downstream order — the stratum sort, the delta accumulation order, the conflict graph
  build — inherits it. **Pre-size the array to the person count and write `acts[i]`.** This single line
  is the difference between the determinism claim at `02:1007-1009` holding and failing.
- **m-6 · MINOR — no `Thread`-local RNG sharing, no `randomize()`, no `Time` anywhere in the map.**
  See §7.

### §6.4 The O(N²) surfaces — where the cliff is, and it is not where the design looks

Every one of these is a consequence of *"nothing stores an aggregate"* (`01:445`), which is the right
rule. The cost is the price of the rule and the design does not name it.

| operation | declared at | naive cost | what makes it linear |
|---|---|---|---|
| **de-individuation** — *"no other person's ledger names them"* | `01:691`, `02:828-830` | **N persons × N ledgers × L claims** | a "named-by" count maintained at deposit and eviction — **the design already calls this the only refcount it has** (`03:420-421`) and then evaluates it by scan |
| `presence` · `density` · `footprint` | `01:426-428` | per call, a scan of every `commit` edge | one pass at the MATTER barrier building `(prop, container) → count` |
| `judging_set(c)` | `01:437` | a scan of addresses per call, and it is called per sitting and per `norm` | barrier-built index |
| `draw_share` · `share` | `01:438-439` | a scan of a Site's drawers per act | barrier-built denominators |
| WITNESS fan-out | `02:731-734` | events × persons if presence is scanned | the presence index above |
| `condition(c)` coarse read | `01:430` | a tree recursion per call | memoize at the barrier; **and see m-2 on the visited-set** |

- **M-4 · MAJOR — CENSUS's de-individuation predicate as written is quadratic in persons and linear in
  ledger budget.** At the design's own `L = 200` (`03:143`), scanning is 200 × N² claim comparisons per
  season. The fix is one integer per person, incremented when a claim naming them is deposited and
  decremented when one is evicted, and it costs nothing because WITNESS already visits every deposit
  and every eviction (`02:735-742`). **This is not an optimization; at any interesting N it is the
  difference between the step running and not running.**

### §6.5 Order independence and floating point — the fourth FATAL

RESOLVE step 6: *"sum a season's deltas for a field and apply the clamp once"* (`02:446-447`,
`01:384-389`). The design's argument for it is correct as far as it goes: **`clamp` does not commute
with addition at the bounds**, and batching removes that.

⚠ **But it then claims the stronger property, and the stronger property is false.** `02:486`: *"`additive`
is order-independent ONLY under batching"* — implying that with batching it *is*. `02:1007`: *"two
attempts resolved in a different order give the same answers"*. **IEEE 754 addition is not associative.**
`(a + b) + c ≠ a + (b + c)` in the last bits, for ordinary values. So the batched sum still depends on
summation order, and the design's own architecture makes that difference observable rather than
cosmetic: `verbs(site, c) = { v : condition(c) ≥ floor(v) }` (`02:621`) is a **band gate on the summed
value**, so a one-ulp difference at a floor is a verb that exists in one ordering and not in another —
and a band-edge closure is an Event that people witness (`01:1156-1158`). **This repository has already
paid for this exact defect class once: `CLAUDE.md` §0.1 point 2 records a 1-ulp aggregate error crossing
a damage-degree boundary while its own identity test passed.**

- **F-4 · FATAL — order-independence of `additive` fields does not hold, and the design conflates two
  properties.** Batching delivers **clamp-order independence**. It does not deliver
  **summation-order independence**. Two fixes, and the second is better:

  1. **Canonical summation order.** A total order over acts already exists — the five strata plus
     `H(act_id, world_seed)` (`02:460`). Sum deltas in that order and the result is *reproducible*.
     But then the honest word is **canonically ordered**, not *order-independent*, and `02:1007`'s
     wording must change.
  2. **Fixed point, and this is the recommendation.** `condition ∈ [0,1]` (`03:157`) and `stores` is a
     quantity. Represent both as integers — `condition` as an int in `[0, 10_000]`, `stores` in whole
     units of its `MatterKind` — and integer addition **is** associative and commutative. Then
     order-independence is a fact rather than a claim, the band gate at `02:621` is exact, and the
     port's own parity protocol gets what it already asked for: *"assert in integer domain at degree
     thresholds… never assert raw float equality across languages"* (`STRAT:163`).

  ```gdscript
  # condition as fixed point: additive is genuinely commutative, and the band gate is exact.
  const COND_ONE := 10_000
  var delta_sum: int = 0
  for d in deltas_for_field:  delta_sum += d          # int64; order cannot change the result
  site.condition_fp = clampi(site.condition_fp + delta_sum, 0, COND_ONE)
  ```

### §6.6 What the counts can be — and the honest answer is that the design does not say

**No population figure appears anywhere in these three documents, in `SUP`, or in the exported world
state.** What the repository does state is geography: 16 territories in `engine/engine_params/world_initial_state.json`,
and *"3 duchies → 14 provinces → 35 settlements"* plus two extra-kingdom settlements
(`references/propagation_map.md:153`). Persons are unbounded.

**And that is defensible, because the design supplies a dial instead of a number.** A Cohort is persons
at coarse fidelity acting once (`01:467-470`), individuation is demand-driven — *"nothing generates
without a demand"* (`02:918`) — and de-individuation returns weight when nobody remembers you
(`02:902`). **The count that costs is INDIVIDUATED PERSONS, not souls**, and the design's own
mechanisms hold it down.

**So the load-bearing statement is not a number, it is a shape:** the population term appears **linearly**
in DELIBERATE (one `sense` + one top-`K` selection over ≤ `L` claims + one `choose`, so O(N·L)), and it
appears **quadratically** in exactly the places §6.4 lists. **Fix those five, and the loop is linear in
individuated persons and linear in events; leave them, and the population ceiling is set by CENSUS's
scan rather than by anything the designer chose.** *(No timing was taken. This is an operation count
over quantities the design declares, not a measurement.)*

---

## §7 · DETERMINISM (Q6)

### §7.1 The shape

`substream(op) = H(world_seed, tick, subject_id, purpose)` (`01:1165`), and the same hash mints ids
(`01:196-202`) — one mechanism closing the determinism and parallelism requirements together, with **no
allocator and nothing to serialise on** (`01:204-207`, `02:132-135`). **This is correct and it is the
best structural decision in the design.**

### §7.2 The Godot implementation

> **ONE `RandomNumberGenerator` PER OPERATION, CONSTRUCTED FROM THE SUBSTREAM, USED, AND DISCARDED.
> NEVER A SHARED INSTANCE RE-SEEDED IN PLACE.**

```gdscript
static func substream(world_seed: int, tick: int, subject_id: int, purpose: StringName) -> RandomNumberGenerator:
    var rng := RandomNumberGenerator.new()
    rng.seed = mix64(world_seed, tick, subject_id, id_hash(purpose))
    return rng
```

- **M-15 · MAJOR — the skeleton's pattern is the one to abandon.** `strike_module.gd:67` writes
  `GameState.rng.seed = key.rng_seed` — a single global RNG object, re-seeded per operation. It is (a)
  a mutable global, which §3's rule forbids; (b) a data race under any parallel map; (c) a silent
  coupling, because any code path that draws *without* re-seeding first inherits the previous
  operation's stream and nothing says so. `strike_module.gd:138` then draws `GameState.rng.randfn(...)`
  from that shared object. **Per-operation instances make the coupling unwritable.**
- **M-6 · MAJOR — `H` must be an owned, versioned mix, and never a built-in.** GDScript's `hash()` and
  `String.hash()` are not specified as stable across engine versions, and `Object.hash()` is identity-
  based. **Since the same function mints ids, an engine upgrade that changes the hash renames every
  object in every save.** Write the mix explicitly — a 64-bit FNV-1a or SplitMix64 over UTF-8 bytes —
  and version it. Two GDScript-specific traps in doing so: `int` is **signed** int64 and `>>` is an
  arithmetic shift, so an unsigned right-shift must be masked; and `RandomNumberGenerator.seed` is a
  `uint64` property, so passing a negative int is correct and `abs()`ing it throws away a bit and
  changes the stream.

### §7.3 What breaks order independence in practice — the checklist

| # | breaker | where it would land here |
|---|---|---|
| 1 | a shared RNG | `strike_module.gd:67` — the existing precedent |
| 2 | **two draws sharing a `purpose` within one `(subject, tick)`** | `01:209-212` requires a slot *"for a multi-`mint` act"* and gives `attempt:2` only as an example. **A second `alter` touch in one act, or a re-roll, silently reuses a stream.** See m-1 |
| 3 | collecting map results by `append` | §6.3, M-11 |
| 4 | float summation order | §6.5, F-4 |
| 5 | `Dictionary` iteration feeding a draw or a sum | insertion-ordered in GDScript, and insertion order is a function of act order — **sort keys at every serialization and every accumulation point**, which `STRAT:167` already names as one of the two semantics that *"corrupt silently"* |
| 6 | `hash()` / `String.hash()` / `randomize()` / `Time` | M-6 |
| 7 | a lazily-built index | §6.3, M-3 |

- **m-1 · MINOR — widen the `purpose` rule.** *"`purpose` must be unique per DRAW within
  `(world_seed, tick, subject_id)`"* — not merely per mint slot. One clause, and it closes breaker 2.

### §7.4 Cross-language parity

Bit-parity between the Python oracle and GDScript is **not a goal and should not become one** —
`STRAT:159` rules it, `STRAT:161-164` supplies what replaces it (named draws · recorded-draw replay ·
key-log equality · integer-domain assertions at thresholds). `randfn` in particular is an
implementation detail whose exact stream is not contractual. **The design's `(3 + d10)/8.5` magnitude
reading (`01:1182`) and its N d10 pool reading (`01:1181`) are both integer-then-divide, which is
exactly the shape that survives; nothing in the design requires a Gaussian.** Worth noting, because it
means the new design is *easier* to port for parity than the shipped combat engine is.

---

## §8 · MODULARITY, AND THE ONE SEAM (Q7)

### §8.1 "A subsystem is swapped by editing a registry row" — proven on both sides already

- **Python side:** `engine/substrate/composition.py:1-24` resolves a **role** to a callable by string
  from `engine/engine_params/composition.json`, exported from `references/module_contracts.yaml:70-100`'s
  `composition_roles:` block. *"Adding a subsystem to the campaign loop is a row in the registry, not an
  import in the engine"* (`composition.py:13-14`). Late failure is not a risk because *"the exporter
  imports and resolves every declared target AT EXPORT TIME, behind a blocking CI gate"*
  (`composition.py:16-19`).
- **Godot side:** `godot/skeleton/core/engine_manifest.gd:1-4` already states the identical pattern —
  *"a new engine is registered by DATA, with zero edits to Kernel/Bus/BaseEngine"* — with
  `@export_file("*.gd") var engine_script` and `modules: Array[String]` of `res://` paths.

**O-3 · OBSERVATION — §7's modularity claim needs no new mechanism. It needs the two existing ones
pointed at each other.** The registry row is the contract; `load(path).new()` is the resolution.

### §8.2 What GDScript costs at the seam, and what to use instead of an interface

Resolving a script by path yields an `Object`; static typing stops at the seam. GDScript has **no
interface keyword and no namespaces**. Two substitutes:

- **A base class per role, which the loaded script `extends`** — `BaseEngine` / `EngineModule` in the
  skeleton (`combat_engine.gd:13`, `strike_module.gd:21`). This is the right one: the base declares the
  methods and `is` gives you a checked cast at the seam.
- **Duck typing via `has_method()`** — avoid; it moves the contract into a string.

**Version-gated:** `@abstract` exists in later 4.x and makes an unimplemented role method a parse
error. **Fallback that works across the whole line, and which the port already prescribes:** a base
method body of `push_error(...)` plus a typed error result, since *"no exceptions in GDScript"*
(`STRAT:154`) and *"a violated invariant must be visible in the result, not swallowed"*.

### §8.3 ⚠ "The module tree is the containment ladder" does not cash out in Godot

**GDScript's `class_name` namespace is FLAT and GLOBAL.** There is no `Settlement.Person` and
`Territory.Person`; there is one `Person`, project-wide. So a module tree can be a **directory** tree,
and it can be a **data** hierarchy (`Container.kind`, the seven rungs at `03:292`), but it cannot be a
*type* hierarchy that mirrors containment. **Mirroring the ladder in scripts buys nothing and imports
the collision risk of a flat namespace into a design with 30+ object names.**

- **M-1 · MAJOR — `Derived` must not be the code-side name, and the collision is worse in Godot than
  the design's own register says.** `01:408-415` and `03:590` record the repo collision — this
  repository's *"Derived Values"* / *"Derived Scores"* are **stored per-character values**
  (`references/glossary.md:75-82`: Health, Stamina, Coherence, Composure, Momentum) — and keep the word
  with a qualifier. **A prose qualifier does not travel into a flat global class namespace.** The
  skeleton already writes `derived_value` in a comment describing a write-protected stat
  (`combat_engine.gd:9`), and the port's law 1 is *"Downward = derivation (read-only)… no setters,
  getters only"* (`STRAT:126`) — so a Godot reader meets *derived* meaning **a stored, write-protected
  field** before they ever meet this design. **Take `Query`, which both documents already name as the
  available alternative** (`01:414`, `03:590`), and which R-1 already defines.
- **M-9 · MAJOR — the union types have no GDScript representation.**
  `Tenure.subject ∈ Person | Container | Proposition` and `object ∈ Person | Container | Office | Site |
  Proposition` (`01:229-232`); `Claim.source` is a five-constructor sum (`03:224-225`);
  `DocketItem.matter` is a five-way sum (`03:251`). GDScript has **no sum type, no tagged union and no
  narrowing**. The representation is `(kind_tag: int, id: int)` — which also happens to be the
  representation §2 wants for storage reasons. ⚠ **And a distinction the port will otherwise lose:
  §14 row 13 forbids *a per-entity branch anywhere in the resolver*, and the design itself says the
  resolver *"branches on `mode`, never on `kind`"* (`01:1424`). A storage discriminator is not a
  resolver branch. Say so in one line, or the first reviewer deletes the tag and the second reviewer
  re-adds it as a class hierarchy.**

### §8.4 The seam for the three deferred subsystems

`01:1362-1380` is clean and correct as an architecture: one seam at `resolve`, a contest subdivides the
tick, no second resolver, no fourth signature, events upward only. In Godot it is one registry row per
subsystem naming a script that `extends ContestResolver`. **Two things it does not say and must.**

- **M-7 · MAJOR — nesting has no declared depth bound, and in GDScript overflow is a crash rather than
  an exception.** *"A nested instance is an instance"* (`01:1378-1380`) is an argument that the barrier
  count survives nesting; it is not a bound. The Python substrate treats this as serious enough that
  its two termination caps are **required constructor arguments with no default value**, precisely so
  *"no fabricated constant enters the repo"* (`engine/substrate/keys.py:1-45` docstring, propagation_spec
  §4.2 Theorem B). **The seam must carry an explicit depth parameter and a cap the caller supplies**;
  in GDScript, exceeding it must produce a typed error result, not recursion.
- **O-5 · OBSERVATION — the shipped contract table and this design disagree about the three deferred
  subsystems.** `STRAT:75-77` gives `personal_combat`, `social_contest` and `mass_battle` three
  separate `dice_pool` resolvers and three separate homes; `01:1372-1373` says a deferred subsystem
  *"adds no resolver"*. Both readings are coherent and they are not the same plan. Reconciliation is
  owed before any of the three is ported.
- **O-4 · OBSERVATION — do not reproduce `combat_bridge.py`'s shape.** `CLAUDE.md` §3 records the one
  surviving seam in `engine/`: `engine/cross_scale/combat_bridge.py` puts a subsystem directory on
  `sys.path` and loads modules **by bare name**, and it was invisible to every instrument in the
  repository until an adversarial read found it. The Godot equivalent — `preload()` by a hardcoded
  path from inside a resolver — is the same shape and is equally invisible. **The manifest is the
  seam; a path literal in a body is not.**

### §8.5 The bridge nobody has noticed

- **O-2 · OBSERVATION — this design supplies the canon `engine_clock` has never had.**
  `references/module_contracts.yaml:1128-1136`: `doc: null`, `sim_module: none`, and a comment recording
  that *"engine/autoload/season_manager.py advances the season counter but does not emit either declared
  Key type — the temporal-spine gap `CLAUDE.md` §6 names"*. **`CALENDAR · MATTER · DELIBERATE · RESOLVE ·
  WITNESS · CENSUS`, with four barriers, four write classes and the write matrix at `02:978-991`, IS
  that specification.** `CLAUDE.md` §6 names `engine_clock` as the module to author canon for first.
  This is the highest-leverage connection between these documents and the 27-module contract layer, and
  neither surface currently points at the other.

---

## §9 · SAVE / LOAD AND SERIALIZATION (Q8)

### §9.1 What serializes, and what must not

| serializes | does not |
|---|---|
| the four carriers, at their current weight — **one array, because Person and Cohort are one type** (`01:482`) | every row of the Derived catalogue (`03:550-571`) — *"nothing stores an aggregate"* (`01:445`) |
| every `Tenure`, **including `until`-stamped historical ones** (`01:240-243`) | `Sensation`, `View`, `Candidate` — one `choose` call each (`03:92-99`) |
| every ledger: claims with `source`, `confidence`, `when`, `visibility` | `Act`, `touch` — one tick |
| Propositions, Records, Dates, DocketItems, Petitions, Dispensations, ConveningConditions | any barrier-scoped index (§6.3) |
| `Site.condition`, `Stores`, `Envelope` counts | `Person.address` and `Person.ties` — **both are VIEWS of Tenures** (`03:139`, `03:144`), and writing them is a second update path |
| **`world_seed` and `tick`** | — |

### §9.2 Do derived ids survive a round trip? Yes — and the trap is a misreading, not a mechanism

> **STORE THE ID. DO NOT STORE A COUNTER. NEVER RECOMPUTE AN ID AT LOAD.**

`id = H(world_seed, tick, subject_id, purpose)` is derived **at mint time**, from a tick and a purpose
that are not recoverable later. What the design deletes is the **allocator** (`01:204-207`), not the
field: `03:106` says every row carries one, and `03:72` calls `Person.id` *"stable — a substream hash,
not a path"*. **The design is right and consistent here.** The failure mode is a reader concluding
"derived ⇒ not serialized" and reconstructing ids at load, which renames every object in the save.
One sentence in the design prevents it.

### §9.3 The Godot mechanics, and the silent corruption

- **M-5 · MAJOR — `.tres` is the wrong save format, for three reasons.** (a) A `.tres` embeds script
  paths and breaks when a script moves. (b) `ResourceLoader` **instantiates scripts**, so a save file
  becomes an execution surface the moment a save is shared or edited. (c) The resource cache returns
  the same instance for a path, so reload-after-save can hand back the pre-save object. **Use
  `FileAccess` plus an explicit serializer.**
- **M-6b · MAJOR (same root as M-6) — 64-bit ids through Godot's JSON lose precision silently.**
  `JSON.parse_string` produces numbers as doubles; **integers above 2^53 do not round-trip**, and every
  id in this design is a 64-bit hash. The corruption is silent, it appears only for ids in the top
  ~99.9% of the space, and it manifests as a dangling reference three loads later. **Fix: ids cross the
  serialization boundary as hex `String`, or the save is binary (`var_to_bytes` / `FileAccess.store_64`).**
- **M-12 · MAJOR — the design and the port's governing spec carry two different save models, and
  neither cites the other.** `01:1174-1176`: *"replay is a re-run, not a log, and no decision function
  may read the event log"* — which reads as *a full-state snapshot, and there is no log to replay*.
  `STRAT:19`: *"save state = initial conditions + Key log; replay = deterministic re-execution"* — and
  `STRAT:164` makes key-log equality *"the master parity check… one harness, three uses"*. **These are
  incompatible load paths:** initial-conditions-plus-log means loading a season-200 save re-simulates
  200 seasons. **Recommended ruling, and it costs nothing to state:** the save is a **state snapshot**;
  the event log is retained for fiction, UI and witness provenance but is never the load path; and
  re-run-from-seed stays a **testing** device, which is exactly what `01:1176` wants it to be.
- **O-1 · OBSERVATION — the design is already right about ids-not-pointers, for a Godot reason it did
  not know it had.** Godot has **no garbage collector**; `RefCounted` is pure reference counting, and a
  reference cycle is a **permanent leak**. `03:441-446` documents cycles as **normal**:
  `succeed ∘ contain` is *"the NORMAL case — the heir lives in the hearth"*, `Claim.subject → Claim`
  and `inferred(claim_id…)` both cycle, and *"the reference graph is not a DAG"*. **Because every
  reference in the design is an id and not a pointer** — `Tenure.subject/object`, `Claim.source`,
  `Ground.support[]`, `Petition.backing[]` — **a faithful port leaks nothing.** The only way to
  introduce the leak is to "improve" the port by replacing ids with object references, which is exactly
  what a Godot-idiomatic reviewer will suggest. **Say once, in the design, that ids are load-bearing
  against object-graph cycles, and the suggestion dies where it is made.**
- **m-2 · MINOR — every traversal needs an explicit visited-set and must be iterative.** `03:442`
  states the requirement (*"every traversal needs a visited-set"*) and `03:446` names the case that
  bites: a cyclic `Office.conferral` path *"never reaches root, so a cycle SILENTLY EXCLUDES the office
  from its cluster instead of being detected"*. In GDScript an unguarded recursive traversal exhausts
  the stack as a hard crash, not as an exception you can catch. `sovereign_fraction`, `address`,
  `condition(c)` and `conferral_path` are the four.
- **m-9 · MINOR — invariant checking on load has a precedent to copy verbatim.** The substrate raises
  on a duplicate id and on a `causes` entry naming an unknown id (`engine/substrate/keys.py:379-381`,
  `384-388`), and gets cycle-freedom by construction from an append-only log (`:389-392`). GDScript has
  no exceptions, so the port's form is `push_error` plus a typed error result (`STRAT:154`) — but the
  three checks are the same three, and `03:858-866` already lists them as the precedent.

---

## §10 · HOSTILE, versus MERELY UNIDIOMATIC (Q9)

**The distinction matters because the two have opposite remedies: hostile means change the design;
unidiomatic means defend the design against the first Godot-fluent reviewer.**

### §10.1 Hostile to Godot — change these

| # | what | why hostile | rank |
|---|---|---|---|
| 1 | the name `Container` | the engine owns it; `class_name` is refused; **and the port was the design's own ground for choosing it** | F-3 |
| 2 | *"the type system makes it unwritable"* — for `choose`'s `World` and for the witness collection form | GDScript has no scoping mechanism that carries either claim | F-1, F-2 |
| 3 | `additive` order-independence over floats | false by arithmetic, and the band gate makes it observable | F-4 |
| 4 | the name `Derived` on the code side | flat global namespace + an established opposite meaning in this repository and in the port's law 1 | M-1 |
| 5 | the side column as a table | one parameter converts it into a call-site impossibility | M-2 |
| 6 | lazily-computed resolver-side queries inside the frozen map | a data race dressed as purity | M-3 |
| 7 | de-individuation by ledger scan | quadratic, and the refcount the design needs is already named | M-4 |
| 8 | unbounded contest nesting | GDScript recursion overflow is a crash | M-7 |
| 9 | union types as prose | no sum type exists; `(kind_tag, id)` or a class hierarchy, and the second is worse | M-9 |
| 10 | `Container.matter` untyped | static typing cannot reach inside a `Variant` | M-14 |

### §10.2 Merely unidiomatic, and correct — defend these

| # | what a Godot reviewer will say | why the design is right |
|---|---|---|
| 1 | *"Person should be a Node so it can be in the scene"* | §2's four consequences; and `efface` is barrier-instant while `queue_free` is frame-deferred |
| 2 | *"use signals for the witness fan-out, that's what they're for"* | §4's three grounds — and the port's own spec already ruled it at `STRAT:128` |
| 3 | *"ledgers should be `Array[Claim]` of objects, not packed arrays"* | §6.2 — refcount traffic is the parallel map's binding constraint |
| 4 | *"drive the season from `_process`"* | a season is a transaction with four barriers, and the kernel must run headless (`STRAT:41`, `STRAT:184`) |
| 5 | *"replace the id references with object references"* | O-1 — that is the one edit that turns a documented, normal cycle into a permanent leak |
| 6 | *"the option list should grey out unavailable verbs"* | `01:609-614` — `verbs` is world truth and `opening_set` is belief; *"a person may attempt a verb the world has already removed, and discover the harbour silted"*. **A UI that greys out re-admits omniscience through the interface layer.** This is the one place a *presentation* decision can violate the architecture |
| 7 | *"`Sensation` should be a class so it can grow"* | §2.2 — the whole guarantee is that it cannot grow |
| 8 | *"one act per person per season is very few"* | not an engine matter; `01:1194-1250` rules it |

### §10.3 Where the design is right and the port is simply hard

Three, and they should be recorded as costs rather than as defects: **the purity guarantee** (§3 — the
goal is right, the mechanism does not transfer), **order independence** (§6.5 — real, and it needs the
fixed-point and collection-order disciplines to be true rather than asserted), and **nothing stores an
aggregate** (`01:445` — right, and it buys a barrier-built index layer the design does not budget for).

---

## §11 · THE RANKED REGISTER

**FATAL — cannot be built as specified.**

| id | finding | at | remedy |
|---|---|---|---|
| **F-1** | `choose`'s no-`World` guarantee is stated as a type-level enforcement; GDScript has no mechanism that carries it — autoloads, `class_name` statics and `load()` are all reachable from a `RefCounted` body | `01:559-567`, `02:1011-1016`; skeleton evidence at `strike_module.gd:38-39,67`, `combat_engine.gd:60` | §3.3: no live world behind any global name; `World` as the explicit first parameter of every resolver-side query |
| **F-2** | *"a consensus broadcast is a type error"* — the collection signature is writable in GDScript | `02:754-756`, `01:561` | restate as a **one-call-site** property; §4.3 |
| **F-3** | `class_name Container` collides with a Godot built-in, and the port was the design's ground for the name | `01:151-156`, `03:642`, `03:586` | rename to `Rung` before the word reaches code |
| **F-4** | `additive` order-independence conflates clamp order with float summation order; the band gate makes the difference observable | `01:384-389`, `02:486-489`, `02:621`, `02:1007` | fixed-point `condition` and `stores`; §6.5 |

**MAJOR — buildable, and will be rewritten if built as written.**

| id | finding | at |
|---|---|---|
| **M-1** | `Derived` as a code-side name, into a flat global namespace, against an established opposite meaning | `01:408-415`, `03:590`, `references/glossary.md:75-82`, `STRAT:126` |
| **M-2** | the resolver/person side column is documentation, not a signature | `01:417-443`, `03:550-571` |
| **M-3** | lazily-built derived caches inside the frozen parallel map | `02:246`, `01:404-406`, `02:118-135` |
| **M-4** | de-individuation evaluated by scanning every ledger | `01:691`, `02:828-830`, `03:420-421` |
| **M-5** | `.tres` as the save format — script-path fragility, execution surface, resource cache | `03:399-416` |
| **M-6** | `H` delegated to a built-in hash; ids are save-critical; signed-int64 shift and `uint64` seed traps | `01:196-202`, `01:1165` |
| **M-6b** | 64-bit ids through Godot JSON lose precision above 2^53, silently | `01:194`, `03:106` |
| **M-7** | contest nesting carries no depth bound; GDScript overflow is a crash | `01:1362-1380`, `engine/substrate/keys.py:1-45` |
| **M-8** | ~9 numeric constants defined in prose with no named artifact, against `CLAUDE.md` §0.05 | `02:340,343,598`; `03:143,527,536,539` |
| **M-9** | union types have no GDScript representation; and the storage tag must not be read as a resolver branch | `01:229-232`, `03:224-225`, `03:251`, `01:1424` |
| **M-10** | Person and Cohort must be one `class_name`, or *"no conversion operation"* is broken at declaration | `01:482-483`, `02:401-403` |
| **M-11** | a parallel map that `append`s produces a nondeterministic act array | `02:1007-1009` |
| **M-12** | two incompatible save models — snapshot versus initial-conditions-plus-log | `01:1174-1176` vs `STRAT:19,164` |
| **M-13** | the port's existing autoload plan puts all tracked state behind a global name | `godot/scene_tree_architecture.md:16`, `STRAT:97`, `STRAT:213` |
| **M-14** | `Container.matter` untyped; four things are addressed by name inside it | `03:149`, G-14 |
| **M-15** | a shared, re-seeded RNG — mutable global, race, and silent coupling | `strike_module.gd:67,138` |

**MINOR.**

| id | finding | at |
|---|---|---|
| **m-1** | `purpose` uniqueness is scoped to mint slots; it must be per draw | `01:209-212` |
| **m-2** | traversals need explicit visited-sets and must be iterative | `03:442`, `03:446` |
| **m-3** | `Path` as `address`'s return type, beside `Path2D`/`Path3D` | `01:442`, `03:570` |
| **m-4** | untyped `@export var … : Dictionary`; typed dictionaries are version-gated | `combat_config.gd:29-38` |
| **m-5** | `Resource` for a carrier shares one cached instance | `03:129-134` |
| **m-6** | int-division and signed-shift semantics in the hash mix | `STRAT:167` |
| **m-7** | the design says nothing about signals; silence reads as permission | `STRAT:128` |
| **m-8** | `Site.drawers[]` stored while `judging_set` is derived | `01:148` vs `01:437` |
| **m-9** | the three load-time invariants have a working precedent; GDScript's form is `push_error` + a typed error result | `engine/substrate/keys.py:379-392`, `03:858-866`, `STRAT:154` |

**OBSERVATION.**

| id | finding |
|---|---|
| **O-1** | ids-not-pointers is load-bearing against `RefCounted`'s absent cycle collector, and the design does not know it (`03:441-446`) |
| **O-2** | this design **is** the missing `engine_clock` canon (`references/module_contracts.yaml:1128-1136`, `CLAUDE.md` §6) |
| **O-3** | the registry-row swap is already proven on both sides (`composition.py:1-24`, `engine_manifest.gd:1-4`) |
| **O-4** | do not reproduce `combat_bridge.py`'s bare-name seam as a `preload()` path literal (`CLAUDE.md` §3) |
| **O-5** | the shipped contract table gives the three deferred subsystems three resolvers; `01:1372-1373` gives them none (`STRAT:75-77`) |
| **O-6** | `World` — the type every refusal is written against — has no record (`03:463`, G-13), and it is the first thing a typed port must declare |

---

## §12 · THE THREE CHANGES TO MAKE FIRST

Ordered by value per character changed, not by severity.

> **1 · PUT `World` FIRST ON EVERY RESOLVER-SIDE QUERY, AND PUT NO LIVE WORLD STATE BEHIND ANY GLOBAL
> NAME.** Twelve signatures and one rule about the autoload table. This is the only thing that
> preserves any part of the purity guarantee in GDScript, it extends the design's own enforcement
> philosophy from three signatures to twenty-three, and it converts the side column from a table a
> reader must remember into a call site that fails. Closes F-1, M-2, M-13; makes M-3 statable.

> **2 · MOVE `condition` AND `stores` TO FIXED-POINT INTEGERS, AND SAY WHICH PROPERTY BATCHING
> DELIVERS.** Integer addition is associative and commutative, so order independence becomes a fact
> instead of a claim, the band gate at `02:621` becomes exact, and the port's parity protocol gets the
> integer-domain thresholds it already asked for (`STRAT:163`). Closes F-4; retires a defect class this
> repository has already paid for once (`CLAUDE.md` §0.1 point 2).

> **3 · RENAME `Container` AND `Derived` BEFORE EITHER REACHES A `class_name`.** The engine owns the
> first; this repository owns the second, with the opposite meaning, in a namespace that is flat and
> global. Both documents already carry the replacement words — `Rung` is the design's own gloss
> (`01:151`), `Query` is the alternative both registers name (`01:414`, `03:590`). A rename now is two
> find-and-replaces; a rename after the port is a rename across two repositories. Closes F-3, M-1.

**And one thing NOT to do first:** do not open a Godot project to settle the version. Nothing in this
audit turns on 4.3 versus 4.6 except three fallback-carrying recommendations (§5 typed `Dictionary`,
§8 `@abstract`, §6 `WorkerThreadPool` ergonomics). **The version question is load-bearing on the
compile ratchet's meaning (`CLAUDE.md` §3, plan Q3) and on nothing here.**

---

## §13 · STATED LIMITS

1. **Nothing here has executed.** No Godot project was opened, no `.gd` file parsed, no `class_name`
   registered, no `.tres` loaded, no season stepped, no allocation counted, no frame timed.
2. **F-3 rests on the engine's class list, not on a parse error anybody observed.** `Container` is a
   built-in `Control`-derived class across the 4.x line and `class_name` rejects shadowing a native
   type. **One line in a scratch project settles it and that line has not been run.**
3. **Every cost claim in §6 is an operation count over quantities the design declares** — `L = 200`
   (`03:143`), `K` (`02:340`), the person count (undeclared) — and not a benchmark. No timing appears
   anywhere above, deliberately.
4. **Every claim about the design is a claim about text at a cited line.** Where a citation is wrong,
   the finding resting on it is wrong.
5. **The design's own four structural tests remain unrun** (`01:1616-1618`), and three of them are the
   properties §3 and §6.5 attack. **This audit does not run them either; it argues that two of the
   three cannot be *enforced* by the stated mechanism in the stated language, which is a different
   claim from their being false.**
6. **This document is REFERENCE, not mechanism** (`CLAUDE.md` §0.05). If it were deleted no behaviour
   would change, because no behaviour exists yet. **The test to apply to every line above: what would
   have to run for this to be true?**
