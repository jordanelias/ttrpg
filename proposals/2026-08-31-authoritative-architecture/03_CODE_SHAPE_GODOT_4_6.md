# 03 · THE CODE SHAPE — Godot 4.6

## Status: PROPOSED (2026-08-31). **No Godot project was opened, no `.gd` file was parsed, no scene
## was run, no benchmark was taken, no `class_name` was registered.** `CLAUDE.md` §0.2 applies in full.
## `[engine]` marks a claim about published Godot behaviour rather than about this repository.

---

## §1 · THE VERSION, HANDLED HONESTLY

`CLAUDE.md` §3 records the engine version as UNRESOLVED and forbids settling it by editing prose.
**This document does not settle it. It is written to Godot 4.6 as directed, and every place that
choice is load-bearing is marked `[4.6-GATED]` with its fallback.**

### The evidence, both sides, complete

| for | source | content |
|---|---|---|
| **4.3** | `CLAUDE.md:10` | `project.godot:11` declares `features=("4.3")`; CI pins the 4.3 binary |
| **4.3** | `workplans/return_to_game_queue.yaml:74-79` | an **executed** baseline: Godot 4.3.stable, headless `--editor --quit`, error counts recorded |
| **4.3** | `proposals/2026-08-18-recursion-interrogation-log.md` | a **second, independent** headless 4.3 run against the real clone |
| **4.3** | `proposals/2026-08-21-execution-order-v1.md:849` | *"84 errors reproduce exactly, 63 of them `Cannot infer the type of X`"* — under the 4.3 binary |
| **4.6** | `README.md:3,10` | "a Godot 4.6 videogame" — prose |
| **4.6** | `godot/godot_conversion_strategy_v1.md:41` | *"`ecosystem_versions.yaml` pins Godot 4.6"* — **the cited file does not exist.** Zero hits in the working tree; the restructure ledger routes it to a `FORK:` ref unreachable in this shallow clone |

> **The asymmetry, stated plainly.** The 4.3 side has a declared `project.godot`, a CI pin, and two
> executed, reproducible headless runs. **The 4.6 side is prose, and its one authoritative-looking
> citation points at a file that no longer exists.** Nobody has ever run 4.6 against `valoria-game`.
> A version can be correct without ever having been run — but whoever rules should know the ledger
> looks like this.

### What targeting 4.6 changes, and what it does not

| surface | 4.3 | 4.6 | consequence |
|---|---|---|---|
| typed `Dictionary[K,V]` | absent | present (4.4+) | **`[4.6-GATED]`** — `Stores` and the params holder use typed maps. **Fallback:** packed arrays + a `const` name→index map |
| `@abstract` | absent | present (4.5+) | **`[4.6-GATED]`** — role methods become parse-time-checked. **Fallback:** base body `push_error` + a typed error result |
| `Container` collision | present | present | **version-independent.** `Rung` regardless |
| `Vector2` as a value type; `RefCounted` refcount-only; `.tres` cache; JSON 2^53 | identical | identical | version-independent — **everything hard about this port is here** |
| `INFERENCE_ON_VARIANT` as an error | promoted **at** 4.3 | not relaxed since | the 84-error class exists under both |

> ### ⚠ WHAT THE 84-ERROR RATCHET MEANS UNDER A 4.6 RULING
>
> **84 is a property of *(this `.gd` tree × the 4.3 binary × the project settings)*.** Two of the three
> factors are version-coupled. **If Jordan rules 4.6, the ratchet baseline is void until re-measured
> under a 4.6 binary** — same method, new number, re-pin. The dominant class (63 of 84,
> `Cannot infer the type of X`) is a strictness default introduced *at* 4.3 and not relaxed since, so
> the count is unlikely to fall on upgrade — **but "unlikely to fall" is a prediction, and a ratchet
> pinned to a prediction is exactly what `CLAUDE.md` §0.1 forbids.**
>
> **This is escalation 3 in `06_ADJUDICATIONS.md`. Do not open a Godot project to settle it —
> nothing in this document turns on the answer except the two gated rows above.**

---

## §2 · PROJECT LAYOUT

This lives in `valoria-game`, the implementation repo. **Nothing here creates apparatus in `ttrpg`.**

```
res://
  project.godot              # [autoload] — the check surface for §3
  core/                      # THE SIMULATION. Headless. NOT ONE Node in this tree.
    world.gd                 # class_name World, RefCounted — declared FIRST
    person.gd                # class_name Person  (weight >= 1; a Cohort IS this type)
    rung.gd  office.gd  site.gd
    tenure_store.gd          # struct-of-arrays rows
    claim_ledger.gd          # per-person packed ledger — rows, not objects
    event_log.gd             # append-only; the keys.py precedent
    query.gd                 # class_name Query — static funcs only; resolver-side take World first
    substream.gd             # the owned hash + per-operation RNG factory
    fixedpoint.gd            # COND_SCALE, the rounding rule, the band compare
    loop/
      season_driver.gd       # class_name SeasonDriver, RefCounted — season(w), four barriers
      calendar.gd  matter.gd  deliberate.gd  resolve.gd  witness.gd  census.gd
    seam/
      contest_resolver.gd    # the base the three deferred subsystems extend (§8)
    params/params.gd         # class_name Params — the typed holder, loaded ONCE by the driver
  data/                      # GENERATED .tres only — never hand-authored
  game/                      # presentation. Nodes live here and ONLY here.
    main.tscn / main.gd      # owns a SeasonDriver; renders; UI signals only
  headless/
    headless_main.gd         # extends SceneTree — runs N seasons, prints the world hash, quits
  tests/
```

**`headless_main.gd` is the execution-artifact factory for every step in `07_EXECUTION_PATH.md`.**

---

## §3 · THE AUTOLOAD RULE, AND THE PURITY PROBLEM

> ### THE LOAD-BEARING RULE OF THE WHOLE PORT
>
> **The `[autoload]` table contains no simulation state and no simulation service. Target: empty.
> Permitted ceiling: presentation-only entries — a UI signal bus, audio. `World` is constructed by the
> driver and passed by parameter. Nothing under `core/` names an autoload, ever.**

**This rejects both shipped plans**, and says so rather than pretending to agree with them:
`godot/scene_tree_architecture.md:16` proposes a `GameState` autoload holding "all tracked state" (the
doc is STALE and says so), and the live `valoria-game` tree uses a `Meta` singleton as "the single
state owner" (`STRAT:97`).

**The mechanism, in two parts:**

1. **No live world state behind any global name.** No autoload, no `class_name` static, no `res://`
   path that resolves to one.
2. **Every resolver-side Query takes an explicit `World` as its first parameter.** Calling one from
   inside `choose` then **fails at the call site for want of an argument.**

**Twelve signatures plus one rule.** This takes enforcement-by-omission from 3 signatures to 23 and
converts the resolver-side/person-side split from a table a reader must honour into a call site that
fails.

**What is still NOT enforced, stated plainly.** [engine] GDScript has no visibility modifiers, so a
determined author can still `load()` a path by string. **The guarantee is *unreachable-by-name*, not
*unwritable*. It is human-checkable on one screen of project settings.** Do not restore the stronger
wording without a mechanism that earns it.

**Is a guard worth building?** Under `CLAUDE.md` §0.1 point 5, a guard is earned only if the artifact
is load-bearing on the game, the exported params, the port, or a Jordan decision. **The port
qualifies.** The guard that earns its existence is one test asserting `project.godot`'s `[autoload]`
section contains nothing from `core/` — cheap, mechanical, and it fails on exactly the recurrence it
exists to catch. **No other guard in this document is licensed.**

**⚠ `STRAT:213` reserved the autoload ruling for Jordan and it is still open.** It is now forced: the
purity fix and the `Meta` pattern are direct opposites. Escalation 2 in `06_ADJUDICATIONS.md`, with
the recommendation attached. **Until it is ruled, no port work that touches state ownership starts.**

---

## §4 · FIXED-POINT ARITHMETIC — closing the last FATAL

**The claim that was wrong:** that batching delivers order-independence for `additive` fields. It
delivers *clamp*-order independence. It does not deliver *summation*-order independence, because
[engine] IEEE float addition is not associative, and the degree-band gate makes the difference
observable at the last bit.

> ### THE SPECIFICATION
>
> - **`condition` is an `int` on a scale of `COND_SCALE = 10_000`.** `COND_SCALE` is an **exported
>   params row, not a literal in a `.gd` file** (`CLAUDE.md` §0.05).
> - **`stores` are integers in whole `MatterKind` units.** No fractional matter.
> - **`f(degree)` and every other prose coefficient cross as integer pairs over a stated denominator**
>   (sixteenths), never as decimal literals.
> - **Rounding is half-up computed on the non-negative magnitude, with the sign applied afterwards.**
>   This is not pedantry: Python floors toward negative infinity and [engine] GDScript's integer
>   division truncates toward zero, so a naive port silently diverges on negative deltas. Fixing the
>   rule here is what gives the parity protocol its integer-domain thresholds.
> - **Accumulate, then clamp once**, with `clampi`.
> - **Band gates compare exactly.** A coarse mean is compared by **cross-multiplication with no
>   division** — `a * d ≥ c * b` rather than `a/b ≥ c/d`.
> - **Belief-side floats are explicitly licensed**, because they never enter an order-free
>   accumulator: `Sensation`'s two scalars, claim confidence, and salience are consumed inside one
>   call and stored nowhere that a second writer reaches.

**With this, order independence stops being a claim and becomes a fact:** integer addition is
associative and commutative, so the post-state hash is bit-identical across permutations, and the
structural test in `07` §2 can assert bit-identity rather than approximate equality — which is the
only assertion that can *observe* the failure it excludes (`CLAUDE.md` §0.1 point 2).

---

## §5 · CARRIER PLACEMENT

`RC` = RefCounted · `Res` = Resource + generated `.tres` · `value` = built-in value type · `row` = a
record in a store with no per-instance object.

| object | placement | why | cost |
|---|---|---|---|
| **Person** (= Cohort at weight > 1) | **RC, ONE class** | interior state, high N, no tree presence. One class is the only honouring of "no conversion operation" | reviewers will itch to subclass Cohort — refuse |
| **Rung** | **RC** | state, not a widget; containment is a Tenure edge, never node-parenting | — |
| **Office, Record, Proposition, Date, DocketItem, Petition, Venue-door** | **RC** | low N, id-referenced, mint/efface-able | per-object allocation at low N — acceptable |
| **Site** | **RC** | `condition` is primary state | every prose formula reads a scaled int |
| **Tenure** | **row in `TenureStore`** | the largest N in the design; per-edge objects make every derivation an O(N) scan and pay refcount traffic inside the parallel map | a store API instead of object fields |
| **Claim** | **row in the owner's packed ledger** | ~200 per person; N×200 RC allocations is the wrong shape | struct-of-arrays discipline |
| **Event** | **row in an append-only log** | `engine/substrate/keys.py` already does exactly this | — |
| **Act** | **RC**, one tick | — | — |
| **touch, spec, Candidate** | **value** | — | — |
| **View** | **`PackedInt64Array`** of ids | a view must hold ids, never references | — |
| **Venue, MatterKind** | **Res + generated `.tres`** | authored world data; `combat_config.gd` is the proven pattern in this tree | [engine] `load()` returns the **cached** instance — never use `Resource` for a carrier |
| **Stores** | **value** — MatterKind-id → int | §4 | `[4.6-GATED]` typed `Dictionary[int,int]`; fallback packed pair |
| **Envelope** | **value** — `PackedInt32Array` per band | matter does not act | — |
| **Sensation** | **`Vector2`** | see below | `.x`/`.y` instead of field names |
| **Query** | **`static func` on `class_name Query`** | not a type | flat global namespace — one holder class |
| **World** | **RC, owned by the driver, NEVER an autoload** | §3 | every resolver-side call threads `w` |

**Nothing in `core/` is a `Node`.** The four carriers have no transform, no visibility, no per-frame
behaviour and no child list, and the containment ladder is deliberately an edge rather than a parent
pointer. A simulation shaped like that wants `RefCounted` and packed value arrays, and Godot serves
both well.

**`Sensation` as `Vector2` — confirmed, and it is the strongest row in the table.** [engine] A
built-in value type has no reference-bearing fields, so *"it cannot be widened into a masked world"*
stops being a convention and becomes a property the compiler enforces: **nobody can add a third field
to `Vector2`.** Two qualifications, stated now rather than discovered later: (1) [engine] `Vector2`
components are 32-bit floats in a standard build — fine here, because both scalars are belief-side and
never enter world state, but **`Vector2` must never be reused for a world-state pair**; (2) the type
prevents *widening*, not *substitution*, so the convention is fixed at the single construction site,
`sense()`, and documented there.

---

## §6 · DETERMINISM IN THE PORT

- **One RNG service**, constructed by the driver, never an autoload, never re-seeded in place. The
  skeleton's shared re-seeded generator is an anti-pattern to delete, not to copy.
- **Per-operation substreams** from `H(world_seed, tick, subject_id, purpose)`.
- **[engine] Two traps, both real:** GDScript integers are signed 64-bit and `<<` on a high bit
  produces a negative number, and `RandomNumberGenerator.seed` takes an unsigned 64-bit value — so the
  hash mix must be written with explicit masking, and the same masking must exist in the Python
  oracle. **Ids are save-critical: a hash that differs between the two languages silently forks every
  id in the game.**
- **[engine] JSON loses integer precision above 2^53.** Ids cross between repos as **strings**, never
  as JSON numbers.
- **Cross-language parity** is asserted on the integer domain (§4), which is what makes it assertable
  at all.

---

## §7 · SAVE AND LOAD

**Two incompatible models are shipped in the corpus:** `STRAT:19`'s initial-conditions-plus-log
replay, and the head's snapshot. **They are different load paths and cannot both be the format.**

> **Recommendation, for Jordan's ruling (escalation 2b):** **the snapshot is the save format.** The
> event log is retained for provenance and for the UI's history surfaces. Re-run-from-seed stays a
> **test device**, where it is genuinely valuable — it is how byte-identity controls are taken — and
> is not the player-facing load path. Replay-as-save makes every load O(campaign length) and makes any
> post-hoc balance fix unloadable.

**Mechanics.** Save as data, not as scripts. **[engine] `.tres` carries a script path and an execution
surface, and the resource cache will hand back a previously-loaded instance** — so `.tres` is correct
for *generated authored data* under `data/` and wrong for a save file. Derived ids survive a round
trip because they are recomputed from `(world_seed, tick, subject_id, purpose)`, all four of which
are in the snapshot.

---

## §8 · THE SEAM FOR THE THREE DEFERRED SUBSYSTEMS

Mass battle, personal combat and social contest attach at **one** place: `resolve`, where a contest
subdivides the tick. They are nested `resolve` instances, not a second resolver.

```
class_name ContestResolver          # 4.6: @abstract; fallback: push_error base body
    func contest(rung, prize, claimants) -> ContestOutcome
```

**Registration is a registry row, not an import.** This is already proven on both sides —
`engine/substrate/composition.py` resolves roles by string in Python, and the port has an engine
manifest doing the same. **Do not reproduce `engine/cross_scale/combat_bridge.py`'s bare-name
`sys.path` seam as a `preload()` path literal**: that seam is declared and shrink-only in the Python
tree precisely because it gives its modules a second identity, and a path literal in GDScript would
reproduce the defect with none of the declaration.

---

## §9 · THE SKELETON — judged

`godot/skeleton/` covers **1 of 27 modules** and **does not compile**. It `extends` `BaseEngine`,
`EngineModule` and `Key` and calls `GameState` and `KeyBus`, none of which are defined anywhere in the
corpus.

> **It is not a head start, and it must not be presented as one.** It is the only executable-shaped
> statement of intent that exists, and its value is entirely as *evidence of what a resolver module in
> this port actually reaches for* — which is how the purity problem was proven rather than
> hypothesised.

**One concrete defect found by an independent sweep, worth fixing wherever this code goes:**
`wound_module.gd:55` writes directly to `health`, a field its own manifest three lines above declares
`writable: false` under an explicit guard. **The skeleton contradicts its own documented contract.**
The fix is to delete the line.

**Disposition:** keep as reference; hand-authored `.tres` under it is grandfathered as reference only;
rewrite rather than extend.

---

## §10 · THE PARAMS PIPELINE

1. **Stage 1 — exists.** `engine/engine_params/*.json`, each behind a `tools/export_*.py` with a
   **blocking `--check` round-trip** in CI. This is mechanism under §0.05 and is the transport between
   the two repos.
2. **Stage 2 — to build, in `valoria-game`.** A generator reading stage-1 JSON and emitting
   `res://data/*.tres`. **`.tres` under `data/` is never hand-authored.** Ids and fixed-point values
   cross as strings and ints, never as JSON floats.
3. **Stage 3.** `Params`, a RefCounted holder loaded once by the driver and read by value.
4. **The rows this architecture owes the pipeline before any code reads them:** the ~9 constants
   currently defined only in prose — the `f(degree)` ladder, the `K` budget terms, the stance-weight
   clamp, `(3 + d10)/8.5`, `entrenchment/60`, `bandwidth`, the ledger cap, the `Ob > 2 × Pool` refusal
   threshold, the degree bands — **plus `COND_SCALE`, the per-band integers, and `wear` per site
   kind.** Until each has an exported row it is reference, and **may not be transcribed by hand into a
   `.gd` literal.**
