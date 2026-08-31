# F3 — ADJUDICATION: the Godot 4.6 code shape

**Adjudicator:** Fable 5, read-only over `/home/user/ttrpg`, 2026-08-31.
**Status of this document:** REFERENCE, not mechanism (`CLAUDE.md` §0.05). Nothing in it executes
(`CLAUDE.md` §0.2). Where a claim is about the engine rather than this repository, it is labelled
**[engine]** = published Godot semantics, never presented as repo evidence. Repo claims carry
`path:line` against the working tree.

---

## 0. METHOD, and what I verified myself

**Read in full:** `proposals/2026-08-31-ideal-v2/04_GODOT_IMPLEMENTABILITY.md` (all 941 lines);
all 8 `.gd` files under `godot/skeleton/`; `godot/godot_conversion_strategy_v1.md` (via R3's
line-verified transcription plus direct reads of lines 41, 97, 126-129, 149-151, 154, 163-168,
177-184, 213); the trace logs R3 (full), R1, R6, PR344.

**Verified directly against the working tree** (not inherited from any log):
- `01_ARCHITECTURE.md` at 144-160 (carriers), 196-215 (identity/substream), 280-300 (Tenure kinds
  + cardinality), **444-470 (the commutativity block — see the correction below)**, 555-570 (Query
  catalogue tail), 700-712 (§3.1a's F-1/F-2 downgrade), 1160-1185 (demotion gate), 1362-1382
  (`wear`), 1440-1455 (Events/determinism head).
- `02_THE_SEASON_LOOP.md` at 440-492, 558-600, 605-614, 640-650, 708, 725-760, **840-858 (F-2's
  claim, uncorrected — see §12)**, 1000-1016, 1109-1145.
- `03_COMPENDIUM.md` at 435-450 (inverse index, cycles) and the §5 Query catalogue via PR344's
  row-faithful transcription cross-checked at `01:555-570`.
- `godot/skeleton/`: every line of all 8 `.gd` files, including `wound_module.gd:31` vs `:55` and
  `strike_module.gd:38-39,67,138`, `combat_engine.gd:43,52,55,60`.
- `engine/substrate/composition.py:1-30`; `engine/engine_params/` listing (10 artifacts).
- Version evidence: `README.md:3,10`; `godot/godot_conversion_strategy_v1.md:41`;
  `find -iname "*ecosystem_versions*"` → 0 hits; `workplans/return_to_game_queue.yaml:74-82`
  (the 4.3 baseline block, verbatim); `proposals/2026-08-21-execution-order-v1.md:849`;
  `godot/scene_tree_architecture.md:3-6,16-24` (STALE banner + `GameState` autoload plan).

**Where I disagree with the inputs.** The commissioning brief (inheriting R3 §6) states F-4 is
"STILL UNADDRESSED: `01_ARCHITECTURE.md:445-449` … still assert the false stronger claim with no
fixed-point fix." **That is wrong about `01_ARCHITECTURE.md` as it stands on disk.** Lines
`01:454-470` are a block headed *"⚠ AND CLAMP ORDER IS NOT THE ONLY ORDER. `condition` AND `stores`
ARE FIXED-POINT INTEGERS"* — it states float non-associativity, the observable band gate, cites
`CLAUDE.md` §0.1 point 2's paid-for precedent, and adopts fixed point, deferring only the scale
value. R3 grepped `01:445-449` and stopped five lines short of the fix. What R3 is right about:
`02_THE_SEASON_LOOP.md:570-578` and `02:844-846` do **not** carry the corrections (see §5, §12).
F-4's *residue* is real; its *location* was misreported. Everything else in R3 that I re-checked
held (the version table, the skeleton census, `wound_module.gd:55`, the module-contract parse).

**Adversarial pass on my own output:** the falsifier for each ruling below is named inline where
one exists; §16 carries confidence per ruling with the weakest links stated.

---

## 1. ⭐ THE VERSION, HANDLED HONESTLY

`CLAUDE.md` §3 records the version as UNRESOLVED and forbids settling it by editing prose. I do not
settle it. **The user directs Godot 4.6 logic; this document is written to 4.6, and every place
that choice is load-bearing is marked `[4.6-GATED]` with its cross-version fallback.**

### 1.1 The evidence, both sides, complete

| # | for | source | content |
|---|---|---|---|
| 1 | 4.3 | `CLAUDE.md:10` | `project.godot:11` declares `features=("4.3")`; CI pins the 4.3 binary (asserted of `valoria-game`, which is not in this checkout — I could not read `project.godot` directly) |
| 2 | 4.3 | `workplans/return_to_game_queue.yaml:74-79` | executed baseline: *"2026-08-19, Godot 4.3.stable.official.77dcf97d8, headless --editor --quit, valoria-game@5e01065"*, error counts recorded stock/setting-only/post-fix |
| 3 | 4.3 | `proposals/2026-08-18-recursion-interrogation-log.md:445,636` (per R3 §5.1; not re-read) | a second, independent headless 4.3 run against the real clone |
| 4 | 4.3 | `proposals/2026-08-21-execution-order-v1.md:849` | *"84 errors reproduce exactly, 63 of them `Cannot infer the type of X`"* — under the 4.3 binary |
| 5 | 4.6 | `README.md:3,10` | "a Godot 4.6 videogame" / "Godot 4.6 implementation" — prose |
| 6 | 4.6 | `godot/godot_conversion_strategy_v1.md:41` | *"`ecosystem_versions.yaml` pins Godot 4.6"* — **the cited file does not exist**: 0 hits for `ecosystem_versions*` in the working tree; `references/restructure_ledger.md` routes it to a `FORK:` ref unreachable in this shallow clone (R3 §5.2, mechanism re-verified: the find returned nothing) |
| 7 | loose | `godot/godot_architecture_specification.md:4,675` (per R3; STALE REFERENCE per `CLAUDE.md` §6) | "Godot 4.x", "Download Godot 4.3+" — a floor, not a target |

**The asymmetry, stated plainly:** the 4.3 side has a declared `project.godot`, a CI pin, and two
executed, reproducible headless runs. The 4.6 side is prose, and its one authoritative-looking
citation points at a file that no longer exists on `main` and cannot be recovered from this
checkout. **Nobody has ever run 4.6 against `valoria-game`.** A version can be correct without ever
having been run — but whoever rules should know the ledger looks like this.

### 1.2 What targeting 4.6 changes, and what it does not

**[engine]** for all rows; none was executed here.

| surface | 4.3 | 4.6 | consequence for this architecture |
|---|---|---|---|
| typed `Dictionary[K,V]` | absent | present (introduced 4.4) | `[4.6-GATED]` — `Stores` and the params holder use `Dictionary[int,int]` / typed maps directly; **fallback everywhere**: packed arrays + `const` name→index map (`STRAT:150`'s conviction-vector pattern) |
| `@abstract` | absent | present (introduced 4.5) | `[4.6-GATED]` — role methods on `ContestResolver`/engine bases become parse-time-checked; **fallback**: base body `push_error` + typed error result (`STRAT:154`) |
| `Container` built-in collision (F-3) | present | present | version-independent; `Rung` regardless |
| `Vector2` as value type; `RefCounted` refcount-only; `.tres` cache; JSON 2^53 | identical | identical | version-independent |
| `INFERENCE_ON_VARIANT` promoted to error | **at 4.3** | not relaxed in any later 4.x I know of | the 84-error class exists under both; a 4.6 run is expected to reproduce the same class or a superset |
| `WorkerThreadPool` map ergonomics | present | present, incrementally hardened | **[unclear]** beyond "API exists in both" — no repo evidence measures a difference |

**What the 84-error ratchet means if it was measured on 4.3 and the tree is 4.6-authored.** The
number 84 is a property of *(this `.gd` tree × the 4.3 binary × the project settings)*. Two of the
three factors are version-coupled. If Jordan rules 4.6: the ratchet baseline is **void until
re-measured under a 4.6 binary** — same method as `return_to_game_queue.yaml:75-76`, new number,
re-pin. The dominant class (`Cannot infer the type of X`, 63/84) is a strictness default introduced
*at* 4.3 and not relaxed since, so the count is unlikely to fall on upgrade — but "unlikely to
fall" is a prediction, not a measurement, and a ratchet pinned to a prediction is exactly what
§0.1's measurement discipline forbids. If Jordan rules 4.3: the 84 stands, and both `[4.6-GATED]`
items above become their fallbacks permanently.

### 1.3 The escalation for Jordan (survives all five §0 tests — see §15)

> **Q3, restated as one decision with its consequences priced.** Rule the engine version.
> - **If 4.6:** (a) `valoria-game/project.godot` `features` and the CI binary pin change together
>   in one commit; (b) the compile ratchet is re-baselined under the 4.6 binary before any other
>   port work — the 84 is a 4.3 artifact and comparing against it under 4.6 is a confounded
>   measurement (§0.1 pt 4: a number without a control); (c) typed `Dictionary` and `@abstract`
>   are adopted and their fallbacks retired.
> - **If 4.3:** (a) `README.md:3,10` and the `CLAUDE.md` §3 bullet are corrected; (b) the two
>   fallbacks become permanent; (c) the 84 baseline stands as-is.
> - **What would settle it on evidence rather than preference:** nothing in this repo can — the one
>   artifact that pinned 4.6 is unrecoverable here. The ruling is a *target* choice, not a fact
>   recovery. The only new evidence worth collecting first is one 4.6 headless run of
>   `valoria-game` (≈minutes), which prices option (a)'s re-baseline before committing to it.

---

## 2. ⭐ THE AUTHORITATIVE CODE SHAPE

This is the binding statement. It lives in `valoria-game` (the implementation repo); nothing below
creates apparatus in `ttrpg` (`04:22-24`'s constraint, honoured).

### 2.1 Project layout

```
res://
  project.godot                # [autoload] section: see §2.2 — the check surface for §4
  core/                        # THE SIMULATION. Headless. NOT ONE Node in this tree.
    world.gd                   # class_name World, RefCounted — declared FIRST (O-6)
    person.gd                  # class_name Person (weight >= 1; Cohort IS this type — M-10)
    rung.gd                    # class_name Rung (F-3 executed)
    office.gd  site.gd         # class_name Office, Site
    tenure_store.gd            # class_name TenureStore — struct-of-arrays rows, per §3
    claim_ledger.gd            # per-person packed ledger (rows, not objects)
    event_log.gd               # append-only rows; the substrate precedent (keys.py:319-419)
    query.gd                   # class_name Query — static funcs ONLY; resolver-side take World first
    rng.gd                     # class_name Substream — the owned hash + per-op RNG factory (§7)
    fixedpoint.gd              # COND_SCALE, the rounding rule, the cross-mult band compare (§5)
    loop/
      season_driver.gd         # class_name SeasonDriver, RefCounted — season(w) with the 4 barriers
      calendar.gd  matter.gd  deliberate.gd  resolve.gd  witness.gd  census.gd
    seam/
      contest_resolver.gd      # the base the three deferred subsystems extend (§10)
    params/
      params.gd                # class_name Params — the typed holder, loaded ONCE by the driver
  data/                        # GENERATED .tres only — never hand-authored (§2.4)
  game/                        # presentation. Nodes live here and only here.
    main.tscn / main.gd        # the ONE Node layer; owns a SeasonDriver; renders; UI signals only
  headless/
    headless_main.gd           # extends SceneTree; runs N seasons, prints the world hash, quits
  tests/                       # gdUnit4 + plain headless scripts; incl. the two §0.1-pt-5 guards (§4.4, §10)
```

### 2.2 Autoload policy — the load-bearing rule of the whole port

> **THE `[autoload]` TABLE CONTAINS NO SIMULATION STATE AND NO SIMULATION SERVICE. Target: empty.
> Permitted ceiling: presentation-only entries (a UI signal bus, audio). `World` is constructed by
> the driver and passed by parameter. Nothing under `core/` names an autoload, ever.**

This *rejects* both shipped plans: `godot/scene_tree_architecture.md:16-24` (a `GameState` autoload
holding "all tracked state" — the doc is STALE and says so at `:3-6`) and the live `valoria-game`
pattern `STRAT:97` records (`Meta` … "the single state owner"). `STRAT:213` (Part VIII item 5)
reserved the autoload ruling for Jordan and it is still open; §15 escalates it **with this
direction attached**, because the design's F-1 remediation (`01:700-712`) is unbuildable under the
`Meta` pattern. Until ruled, no port work that touches state ownership starts.

### 2.3 The `class_name` roster, with collision status

**[engine]** for the collision column; the discipline is one scratch-project line per name before
first use (the same check §13 step 1 executes — F-3's own limit at `04:927-929` applies to every
row until then).

| name | collision status |
|---|---|
| `World` | free in 4.x — Godot 3's `World` became `World3D` in 4.0. **Would have collided in 3.x; probe it anyway** |
| `Person`, `Rung`, `Office`, `Site`, `Tenure`, `TenureStore`, `Act`, `Event`*, `Claim`, `Query`, `Record`*, `Date`*, `Venue`, `Petition`, `Dispensation`, `Proposition`, `Sensation`† | no built-in of that exact name; * = near a family of built-ins (`InputEvent`, `RecordDialog`? none, `Time`) — probe; † = never a class at all, it is a `Vector2` (§3) |
| `Container` | **TAKEN** (Control-derived base of `VBoxContainer` et al.) — F-3, executed as `Rung` at `01:150-156` |
| `Path` | removed in 4.x (`Path2D`/`Path3D` remain) — m-3 confirmed; the address query returns a typed array of Rung ids, not a `Path` |
| `Derived` | free in the engine, **taken in this corpus with the opposite meaning** (`references/glossary.md:75-82`, stored per-character values; R1 §8 confirms zero live code uses) — M-1, executed as `Query` |

### 2.4 How the Godot side ingests `engine/engine_params/`

The four-stage pipeline of `04 §5.2`, adopted as binding, with the stage-3 generator named as the
missing piece:

1. **Stage 1 (exists):** `engine/engine_params/*.json` — 10 artifacts (listing verified), each
   behind a `tools/export_*.py` with blocking `--check` (`.github/workflows/valoria-ci.yml`, per
   R3 §9 / R6 §5). This is mechanism under `CLAUDE.md` §0.05 and is the transport between repos.
2. **Stage 2 (to build, in `valoria-game`):** a generator that reads stage-1 JSON and emits
   `res://data/*.tres`. **`.tres` under `data/` is never hand-authored** (`STRAT:149,151` already
   rule this; the skeleton's hand-authored `.tres` set is grandfathered as reference only, §11).
   Ids and fixed-point values cross as **strings/ints, never JSON floats** — M-6b (§8).
3. **Stage 3:** `Params` (`class_name`, RefCounted) — loaded once by the driver, read by value.
   `[4.6-GATED]` typed `Dictionary` fields; fallback packed arrays + const index maps.
4. **New rows this design owes the pipeline (M-8):** the ~9 prose constants (`f(degree)` ladder,
   `K` budget terms, `stanceweight` clamp, `(3+d10)/8.5`, `entrenchment/60`, `bandwidth`, `L=200`,
   `Obstacle > 2×Pool` refusal, the five degree bands) plus **`COND_SCALE`, the per-band `floor(v)`
   integers, and `wear` per site kind** (§5) each get an exported artifact row before any code
   reads them. Until then they are reference (`CLAUDE.md` §0.05) and may not be transcribed by hand
   into a `.gd` literal.

### 2.5 The headless driver

`SeasonDriver.season(w: World)` is a plain function on a RefCounted — the shape at `04 §6.1`,
which is already the port's floor (`STRAT:41` "kernel scene-tree-free", `STRAT:184` "headless-
testable"). `headless/headless_main.gd extends SceneTree` runs it under
`godot --headless --script`, prints the world hash, quits — **this file is the execution-artifact
factory for every §13 step.** `_process` drives nothing; if a season exceeds a frame budget in the
shipped game, the presentation layer `await`s between barriers (main-thread slicing, no threading
implied).

---

## 3. ⭐ CARRIER PLACEMENT, RULED

`RC` = RefCounted · `Res` = Resource (+`@export`+generated `.tres`) · `value` = built-in value
type · `row` = record in a store, no per-instance object.

| object | placement | why | what it costs | 4.6-specific notes |
|---|---|---|---|---|
| Person (=Cohort at weight>1) | **RC, one class** | interior state, high N, no tree presence; `01:482-483` "no conversion operation" is honoured only by one class (M-10) | weight-1-vs-cohort logic lives in data, not types; reviewers will itch to subclass — refuse | none |
| Rung | **RC** | state, not a widget; containment is a Tenure edge, never node-parenting (`01:286-292`) | the rename (done) | none |
| Office, Record, Proposition, Date, DocketItem, Petition, Dispensation, ConveningCondition | **RC** | low-N, id-referenced, mint/efface-able | per-object allocation at low N — acceptable | none |
| Site | **RC** | `condition` is primary state (`01:173-176`); written at RESOLVE + `wear` at MATTER only (`02:390-406` write matrix) | `condition` field is `int` fixed-point (§5), so every prose formula reads scaled | none |
| Tenure | **row in TenureStore** | largest N in the design; per-edge objects make every derivation an O(N) scan and pay refcount traffic in the parallel map (`04 §6.2`) | a store API instead of object fields; the object-side index is derived, matching `01:238` | typed `Dictionary` for per-kind cardinality tables `[4.6-GATED]` |
| Claim | **row in the owner's packed ledger** | `L=200` per person (`03` §2.1); N×200 RC allocations vs rows | struct-of-arrays discipline | none |
| Event | **row in append-only log** | the substrate already does exactly this (`engine/substrate/keys.py:319-419` per R1 §2) | — | none |
| Act / touch / spec / Candidate / View | **RC (Act, one tick) / value / value / value / `PackedInt64Array`** | one tick each; views must hold ids, never references (`02:348-352` region) | — | none |
| Venue / door / MatterKind | **Res + generated `.tres`** | authored world data; `combat_config.gd:1-12` is the proven pattern in this very tree | m-5's trap: never a carrier — `load()` returns the cached instance **[engine]** | none |
| Stores | **value** — map MatterKind-id → int, whole units | §5's fixed point; `01:466-467` | integer-only economy | typed `Dictionary[int,int]` `[4.6-GATED]`; fallback PackedInt64Array pair |
| Envelope | **value** — `PackedInt32Array` per band | matter, does not act (`01:471-473` region) | — | none |
| **Sensation** | **`Vector2`** — RULED, see below | | | |
| Query | **`static func` on `class_name Query`** — not a type | M-1/M-2; resolver-side rows take `World` first (§4) | no namespacing (flat global) — one holder class | none |
| World | **RC, owned by the driver, never an autoload** | §2.2; the whole of §4 | every resolver-side call threads `w` | none |

**`Sensation` as `Vector2` — CONFIRMED, with the precision caveat both audits missed.**
The audit's argument (`04 §2.2`) is correct and is the strongest row in the table: a built-in value
type has no reference-bearing fields, so *"cannot be widened into a masked world"* stops being a
convention and becomes a property the compiler enforces — nobody can add a third field to
`Vector2`. **[engine]** Two qualifications, stated so they are not discovered later:
(1) `Vector2` components are **32-bit floats in a standard build** (64-bit only under the
`precision=double` build option). That is fine *here* — subsistence and standing are belief-side
scalars consumed inside one `choose` call, never summed into world state, so §5's fixed-point rule
does not reach them — but it means `Vector2` must never be reused for any world-state pair.
(2) The type prevents *widening*, not *substitution*: `choose(p, view, sensation: Vector2)` still
depends on the signature being typed. Convention fixed at the single construction site:
`sense()` returns `Vector2(subsistence, standing)`, documented there and nowhere else.
Cost accepted: `.x/.y` instead of field names. A `class Sensation extends RefCounted` is REFUSED
(`04:166-168`'s ground: the first added field is invisible at every call site).

---

## 4. ⭐ THE PURITY PROBLEM, RULED (F-1)

**The audit's diagnosis is CONFIRMED against the engine and against this repo's own code.**
GDScript has no module system, no visibility modifier, no way to scope an identifier out of a body;
an autoload is a global identifier in every script; `class_name` statics and `load()` by string are
two further doors (**[engine]**, and `04 §3.2` argues it correctly). The skeleton is the live
exhibit: `godot/skeleton/engines/combat/modules/strike_module.gd:38-39` (`GameState.get_actor`
inside a resolver), `:67` (`GameState.rng.seed =`), `combat_engine.gd:60` (`KeyBus.emit_key`) —
all read directly this pass. And the design has already adopted the downgrade: `01:700-712`
(§3.1a) states *"unwritten, not unwritable"* and the two-part fix.

### 4.1 The mechanism, exactly

1. **No live world state behind any global name.** No autoload holds it (§2.2), no `class_name`
   static holds it, no `res://` path resolves to a live state object. Then `choose`'s body has
   nothing to reach — not because a type forbids it, but because no identifier names it. The check
   surface is the `[autoload]` section of `project.godot`: one screen, human-checkable.
2. **`World` first on every resolver-side Query; person-side Queries take the asking person and
   nothing else.** Calling a resolver-side query from inside `choose` then fails at the call site
   for want of an argument.
3. `sense(p: Person, w: World) -> Vector2` is the one licensed World-taking function on the
   DELIBERATE side (`02:1122-1128` states the honest limit: it decides nothing and returns two
   scalars; if it ever returns more, nothing at a call site says so — that is the residual risk and
   it is named, not hidden).

### 4.2 The affected signatures, enumerated

Top-level three (`01:132-136` shape): `choose(p, view, sensation) -> Act` ·
`resolve(acts, w) -> Array[Event]` · `witness(p, event_id) -> Array[Claim]`.

Resolver-side Queries — **18 rows of `03_COMPENDIUM.md` §5's 23-row catalogue** — each
`static func` on `Query` with `w: World` first: `faction, presence, density, footprint,
sovereign_fraction, condition, verbs, norm, eligible, judging_set, draw_share, share, capacity,
entrenchment, address, regard, retention, filter_share`.
Person-side — 5 rows, no World, ever: `leaders, opening_set, occupation, estimated_profile, trace`.

> **Finding of this pass, in neither audit:** `03_COMPENDIUM.md` §5's header mandates *"Every
> resolver-side Query takes World as its FIRST parameter"* — and then **12 of its own 18
> resolver-side signature cells omit it** (e.g. `condition: Rung → [0,1]∪⊥`,
> `sovereign_fraction: Rung → [0,1]`, `verbs: (Site,Rung)`, `judging_set: Rung → …`; only
> `presence/density/footprint/regard/retention/filter_share` show `World`). Cross-checked against
> `01:555-570`'s catalogue tail, which has the same omissions. One editorial pass owes the
> catalogue its own rule. (Also corrects `04 §3.3`'s "12 of the 20 rows" count: the shipped
> catalogue is 23 rows, 18 resolver-side.)

### 4.3 What still is NOT enforced, and what would check it

Not enforced by anything above: (a) a body calling `load("res://…")` on a path that happens to
reach live state (closed only by rule 1 — there must be no such path); (b) a future `class_name`
static acquiring state; (c) `sense` widening its return; (d) a second `witness` signature (§6);
(e) an autoload added later.

**The check, and whether it is earned.** One headless test in `valoria-game`, two assertions:
parse `project.godot`'s `[autoload]` section against the allowlist (empty / presentation-only);
scan `core/**.gd` for the tokens `preload(`, `load(`, and any allowlisted-autoload identifier —
zero hits permitted in `core/`. Under `CLAUDE.md` §0.1 point 5's predicate this guard is
**EARNED**: its subject is the port, and its output gates the port's one structural guarantee —
it is load-bearing on the game and the port, not on this repository's process. It is the exact
analogue of `tests/valoria/test_engine_does_not_import_systems.py` (which pins the same property on
the Python side by subprocess-import probe — R6 §4 row 1), and like that test it must match on
something that cannot be spelled around (token scan of `core/` files by path, not by name —
the `combat_bridge.py` lesson, `CLAUDE.md` §3). It lives in the game repo as a test, not in
`ttrpg` as apparatus. **Falsifier:** add a dummy autoload or a `load()` in `core/` — the test must
red.

---

## 5. ⭐ F-4, RULED — order independence and floating point

**The arithmetic claim is CONFIRMED. [engine-independent mathematics]** IEEE-754 addition is not
associative; a batched sum's value depends on summation order in the last bits. The design makes
the difference observable, not cosmetic: `verbs(site,c) = { v : condition(c) ≥ floor(v) }`
(`02:708`) is a band gate on the summed value, a band-edge closure is a witnessable Event
(`01:1440-1444`), and this repository has already paid for the class once (`CLAUDE.md` §0.1 pt 2's
1-ulp damage-degree crossing).

**The status correction (see §0):** the fix is **ADOPTED in `01_ARCHITECTURE.md:454-470`** —
fixed-point integers for `condition` and `stores`, band gate exact, `[0,1]` re-read as the scaled
integer — with the scale deferred ("the scale is a parameter and no value is proposed here",
`01:466-468`). **The residue:** `02_THE_SEASON_LOOP.md:570-578` (§5.2) still teaches
batching-only with no fixed-point mention or cross-reference, and `02` §10's order-independence
table never lists float summation among its breakers. One cross-reference in `02` closes the prose
side. What was genuinely missing everywhere — and what this section supplies — is the **concrete
representation.** This closes the last FATAL.

### 5.1 The representation, specified

- **Type:** GDScript `int` — signed int64 **[engine]**. No 32-bit anything in the accumulator path.
- **`condition`:** integer in `[0, COND_SCALE]`, **`COND_SCALE = 10_000`** (1 unit = 10⁻⁴ of full
  condition). Ground: decimal scale keeps exported params and design prose legible (0.25 → 2500);
  10⁴ keeps the smallest live deltas — `wear` per season, `f(degree)·share` at large N —
  representable as ≥ 1 unit at any population the design contemplates, while every sum below stays
  ≥ 5 decimal orders inside int64. A power-of-two scale buys nothing because §5.3 eliminates
  division from every comparison. `COND_SCALE` is an exported-param row (§2.4), not a `.gd` fiat.
- **`stores`:** integers in whole units of their `MatterKind` (`01:466-467`, adopted verbatim).
- **`f(degree)`:** declared as the integer pair over denominator 16 — `f_num ∈ {0, 0, 1, 2, 4}`
  for Disaster/Failure/Costed/Clean/Overwhelming (the prose 0 · 0 · 1/16 · 1/8 · 1/4, `02:598`
  region). Exported, not inlined.
- **`wear(kind)`:** an integer in `condition` units per season, one exported row per site kind
  (`01:1362-1372` already requires the table row; this fixes its unit).

### 5.2 The rounding rule (the cross-language trap, closed)

Every delta becomes an integer **before** it enters an accumulator. For
`Δcondition = −condition_fp × f(degree) × share(actor, site)` with `share = draw_a / draw_total`
(both integers once stores are integers):

```
num := condition_fp * f_num * draw_a          # int64 product
den := 16 * draw_total
mag := (2*num + den) / (2*den)                # ROUND HALF UP, computed on NON-NEGATIVE ints only
delta := -mag                                  # sign applied AFTER
```

**Why this exact shape:** Python `//` floors; GDScript integer `/` truncates toward zero
**[engine]** — the two disagree on negative operands, which is precisely `STRAT:167-168`'s
integer-division watchlist entry. Computing magnitude on non-negative integers and applying sign
afterwards makes Python oracle and GDScript port agree bit-for-bit in the integer domain, which is
what `STRAT:163` ("assert in integer domain at degree thresholds") has been asking for.
Restoration mirrors with `(COND_SCALE − condition_fp)` as the first factor (`02` §5.7's formula).
**Overflow bound:** `condition_fp ≤ 10⁴`, `f_num ≤ 4`, `draw_a ≤ draw_total ≤` total annual stores
— the product stays under 2⁶³ for any `draw_total < 10¹⁴`; assert it anyway at the one site.

### 5.3 Clamp and band semantics

- **Accumulate-then-clamp-once:** `delta_sum: int` summed in any order (integer addition is
  associative and commutative — order-independence is now a fact, not a claim);
  `site.condition_fp = clampi(site.condition_fp + delta_sum, 0, COND_SCALE)`. `wear` is applied at
  MATTER, strictly before, needing no commutativity argument (`02` §3.1 / write matrix `02:399`).
- **Band edges:** each `floor(v)` is an integer in `COND_SCALE` units, exported. The gate is
  `condition_fp >= floor_fp` — exact.
- **The coarse read** `condition(c)` (draw-weighted mean over Sites) **never divides.** The gate on
  a mean is evaluated by cross-multiplication in int64:
  `Σ(w_i * c_i_fp) >= floor_fp * Σ(w_i)`. Exact, order-independent, division-free. Bound: with
  `Σw ≤ 10¹³` and `c ≤ 10⁴` the left side stays under 10¹⁷ < 2⁶³.
- **`yield`** lands in `stores` units: a single declared evaluation order — integer numerator
  product (base_units × condition_fp × season_factor_fp × (3+d10)), one division by the combined
  denominator at the end, round half up as §5.2, per (site, season) — then integer sums. This
  **requires `season_factor` to be declared fixed-point when its distribution is ruled**
  (`02` §3.2 carries it OPEN); until then `yield` cannot be implemented, and that dependency is now
  explicit rather than discovered.
- **The float boundary, stated so it is not overrun:** fixed point governs the additive world
  quantities — `condition`, `stores`, envelope weights. Belief-side arithmetic (salience,
  stanceweight, recency, the d+σ combat interior) **remains float and is allowed to**, because it
  feeds per-person sequential decisions and contest interiors, never a cross-act commutative sum.
  The rule is not "no floats"; it is "no float ever enters an order-free accumulator or a band
  gate."
- **The honest word:** with this in place, `additive` fields are genuinely order-independent.
  Where any prose still wants the weaker mechanism (a canonical summation order), the word is
  *canonically ordered*, never *order-independent* — `04 §6.5` fix 1 is refused as the primary
  mechanism because it survives only as long as every future accumulation site remembers to sort.

**Falsifier (build order step 2):** permute delta application order across a seeded season; the
world hash must be byte-identical. That test is the first of the design's four structural tests
ever to execute.

---

## 6. WITNESS AND FAN-OUT (F-2)

**Signals are ruled out of the simulation entirely**, on the audit's three grounds (`04 §4.2`:
shape = the forbidden §14-row-3 broadcast materialised; presence is a computation, not a
subscription — connect/disconnect traffic ∝ persons × events × seasons; signal order is a hidden
global order, synchronous and re-entrant) — and the governing spec already rules it:
`STRAT:128` verbatim, *"the EventBus carries UI/lifecycle signals only — signals are not Keys."*
Signals live in `game/` for presentation, full stop (m-7: the design should say this once, citing
STRAT:128).

**The shape that works** — two passes, matching `02` §6's own split (step 1 global, step 2
interior), as `04 §4.3` gives it: `fan_out(w, events) -> Dictionary[person_id -> PackedInt64Array]`
walking the barrier-built presence index, the latency-gated channel index, and knot partners
(reusing the event's own id, `02:840-842`); then `witness(p, event_id)` per person, any order,
writing one ledger.

**F-2 itself: CONFIRMED, and the claim is still live in `02`.** `02:844-846` still asserts
*"CONSENSUS BROADCAST IS A TYPE ERROR … a shape the type system makes unwritable"* — false in
GDScript (the collection signature `func witness_all(ps: Array[Person], e: int)` type-annotates
happily, **[engine]**). `01:707-709` carries the correction; `02` does not. **The replacement
guarantee is a call-site property:** `witness` has exactly ONE call site, inside `witness.gd`'s
step-2 loop. **What enforces it now that the type system does not:** (a) code shape — the
per-person function is file-internal to `core/loop/witness.gd`, `_`-prefixed, with `run_witness(w)`
the only public entry (convention, and stated as only that); (b) the same §4.4 port-repo test gains
one assertion: exactly one call site of `_witness(` under `core/`, and zero functions under `core/`
whose typed signature is `(Array[Person], …Event…)`. Earned under §0.1 pt 5 by the same ground as
§4.4. **Falsifier:** add a second call site; the test reds.

---

## 7. DETERMINISM IN 4.6

**The substream is the best structural decision in the design** (`04 §7.1` — concurred):
`substream(op) = H(world_seed, tick, subject_id, purpose)`, the same hash minting ids
(`01:203-210`) — no allocator, nothing to serialise on, parallelism and determinism closed by one
mechanism.

### 7.1 The concrete implementation

- **One `RandomNumberGenerator` per operation — constructed from the substream, used, discarded.**
  Never a shared instance re-seeded in place. The skeleton's `strike_module.gd:67`
  (`GameState.rng.seed = key.rng_seed`) is the named anti-pattern (M-15: mutable global + data race
  under any parallel map + silent stream coupling for any path that draws without re-seeding).
- **`H` is an owned, versioned mix — never a built-in.** `hash()`/`String.hash()` are not
  stable-across-versions contracts, and ids are save-critical (M-6) **[engine]**. Implement
  SplitMix64 (or 64-bit FNV-1a) over UTF-8 bytes in `core/rng.gd`, with `const HASH_VERSION := 1`
  serialized into every save header. Two GDScript traps, closed explicitly:
  - `int` is **signed** int64 and `>>` is arithmetic **[engine]**: every logical right shift is
    written `(x >> n) & ((1 << (64 - n)) - 1)`.
  - `RandomNumberGenerator.seed` is a `uint64` property **[engine]**: pass the signed value as-is;
    `abs()` discards a bit and changes the stream.
  - **[unclear]** GDScript integer overflow semantics (wrap vs debug-error) on the SplitMix64
    multiplies: published behaviour is two's-complement wrap, but I have not executed it and debug
    builds may differ. §13 step 1's scratch probe includes one line settling it; if wrap is not
    dependable, the mix falls back to 32-bit-halves multiplication, specified then.
- **`purpose` uniqueness is per DRAW** within `(world_seed, tick, subject_id)` — m-1's widening,
  adopted; a re-roll or second `alter` in one act takes a new purpose slot.
- **Nothing in DELIBERATE or RESOLVE touches `randomize()`, `Time`, or a `Thread`-shared RNG**
  (m-6), and no `Dictionary` iteration feeds a draw or a sum without key-sorting
  (`STRAT:168`'s watchlist; breaker 5 of `04 §7.3`).
- **Parallel map discipline:** results written `acts[i]` into a pre-sized array, never `append`
  (M-11); no lazily built cache inside the map — every index is built at the barrier, read-only
  until the next, discarded there (M-3, adopted as stated).

### 7.2 Replay and cross-language parity

Replay is a **re-run** (a testing device), never the load path (§8). Bit-parity with the Python
oracle is a non-goal — `STRAT:159` rules it; what replaces it is `STRAT:160-164`: named draws,
recorded-draw replay, log-equality as the master check, **integer-domain assertions at degree
thresholds** — which §5's fixed point finally makes cheap. One oracle-side fact neither audit
carries: **the Python reference has no substream implementation** — it runs one shared
`random.Random(seed)` on `World.rng` with derived sub-streams only at two call sites
(`engine/autoload/game_state.py:265,306`; `combat_bridge.py:140`; per R1 §5, spot-confirmed via
R1's line citations). Parity for the new design therefore compares at the Event/threshold level
until the oracle grows a hash-substream twin; that is oracle-side work and it is now named.

---

## 8. SAVE / LOAD

**RULED: the save is a STATE SNAPSHOT. The event log serializes as part of state (Events are
permanent, never effaced, and Claims cite event ids — `03` §1's identity register), but it is never
the load path and no decision function may read it (`01:1174-1176` via `02:511`, `02:1131`).
`STRAT:19`'s initial-conditions-plus-log model is retired as the *save* model and retained in full
as the *test harness* model** — re-run-from-seed plus log-hash equality stays the master parity
check (`STRAT:164`, "one harness, three uses" — it keeps two of the three uses). Ground
(M-12, and this is the architecture answering under `CLAUDE.md` §0's test 5): loading a season-200
save by re-simulating 200 seasons has unbounded load time and breaks on every code change; the
design's own text already forbids the log as an input. Cheap to state, expensive to leave open —
stated. Flagged in §15 as a veto-able ruling since it touches the governing spec's line 19.

**Format, ruled:**
- **`.tres` is REFUSED for saves** — M-5's three grounds, all **[engine]**: embedded script paths
  break on file moves; `ResourceLoader` instantiates scripts, making a shared/edited save an
  execution surface; the resource cache can hand back the pre-save instance on reload. `.tres` is
  for generated authored data (`data/`) only. The one shipped save sketch
  (`godot_architecture_specification.md:660-667`, STALE) used `ResourceSaver` and is not followed.
- **The save is binary via `FileAccess` with an explicit, versioned, per-store serializer.**
  Header: magic, format version, `HASH_VERSION`, `world_seed`, `tick`. Ids via
  `FileAccess.store_64` — exact, no 2^53 issue. **Not** `var_to_bytes(_with_objects)` — with
  objects it is the same execution surface as `.tres`; without objects it cannot encode the stores.
- **JSON is debug-export only, ids as hex strings** (M-6b: `JSON.parse_string` yields doubles;
  ints above 2^53 corrupt silently **[engine]**).
- **What serializes / what must not:** exactly `04 §9.1`'s table, adopted — carriers at current
  weight (one array; Person and Cohort are one type), all Tenures including `until`-stamped
  history, ledgers, the log, `Site.condition_fp`/`stores`/envelope, `world_seed`+`tick`; never any
  Query result, any barrier index, `Sensation`/`View`/`Candidate`/`Act`, or `Person.address`/
  `ties` (views of Tenures — a second update path otherwise).
- **Ids are STORED, never recomputed at load** (`04 §9.2`'s misreading trap — the sentence goes in
  the serializer's doc comment).
- **Load-time invariants**, copied from the working precedent (`engine/substrate/keys.py:357-392`
  per R1 §2: unique id; references resolve; cycle-freedom of the log by construction): GDScript
  form is `push_error` + typed error result (`STRAT:154`), never a crash.

---

## 9. IDS NOT POINTERS

**The cycle-collector argument is VERIFIED. [engine]** Godot has no garbage collector;
`RefCounted` is pure reference counting and a reference cycle is a permanent leak — in every 4.x
(and 3.x). **The design's reference graph is cyclic by construction and documents it:**
`03` §3.4 (read at `03:435-450` context): `succeed ∘ contain` (Rung→Person→Rung) is *"the NORMAL
case — the heir lives in the hearth"*; `Claim.subject → Claim` and `inferred(claim_id…)` cycle;
*"the reference graph is not a DAG."* Because every stored reference is an **id** (`Tenure.subject/
object`, `Claim.source`, `Ground.support[]`, `Petition.backing[]`), a faithful port allocates no
cycle and leaks nothing. Object references may exist only within one barrier's local scope and are
never stored on a carrier.

**The standing note** (to sit verbatim atop `core/world.gd`, and once in the design per O-1):

> IDS, NOT POINTERS — LOAD-BEARING, DO NOT "FIX".
> Every cross-record reference in this simulation is a 64-bit id resolved through a store.
> This is not a style choice. (1) Godot's RefCounted has no cycle collector; this design's
> reference graph is cyclic BY CONSTRUCTION (a hearth's succeed edge points at the heir who
> lives in the hearth — 03_COMPENDIUM §3.4), so replacing ids with object references creates
> permanent leaks. (2) Ids are minted from the determinism substream and are save-critical;
> pointers do not survive serialization, ids do, exactly. (3) Every traversal over these ids
> carries an explicit visited-set and is iterative — an unguarded recursion over a legal cycle
> is a stack-overflow crash, not a catchable error (m-2; the cyclic Office.conferral path is
> the documented case). Replacing any id field with a direct reference is a regression even
> though it will look like idiomatic Godot. It has been reviewed. Leave it.

m-2 adopted with it: `sovereign_fraction`, `address`, `condition(c)`, `conferral_path` are the four
traversals that get visited-sets and iterative form.

---

## 10. THE SEAM

The three deferred subsystems (mass battle, personal combat, social contest) attach at `resolve`,
where a routed conflict opens a `contest` that subdivides the tick (`01:1362-1380` region /
`02:745-748`: nested instance, same barriers, smaller person set, shorter clock; no second
resolver, no fourth signature, Events upward only).

**In Godot terms, ruled:**
- `core/seam/contest_resolver.gd` — `class_name ContestResolver extends RefCounted`, declaring
  `run(w: World, contest: Contest, depth: int, max_depth: int) -> Array[Event]`.
  `[4.6-GATED]` `@abstract` on `run`; fallback `push_error` + typed error result.
- **The registry row is the seam.** A generated manifest (`data/`, from stage-2 `.tres`) maps
  subsystem-role → script path; the kernel `load(path).new()`s **every declared row at boot**, and
  a headless boot in CI is the check — the Godot analogue of `composition.py`'s export-time
  resolution (`engine/substrate/composition.py:16-19`: *"a typo or a moved module reds CI, not a
  campaign run"* — same property, moved to boot). The skeleton's `engine_manifest.gd:1-4` already
  states this pattern (O-3: the two sides need pointing at each other, no new mechanism).
- **Depth is capped by a caller-supplied parameter with no default** — M-7, and the Python
  substrate's own discipline (`TickScheduler` requires both termination caps as constructor
  arguments, `keys.py:428-437` per R1 §2: *"no fabricated constant enters the repo"*). Exceeding it
  is a typed error result, never recursion — **[engine]** GDScript stack overflow is a crash, not
  an exception.
- **O-4 RULED an anti-pattern, binding:** `combat_bridge.py`'s bare-name `sys.path` seam
  (`CLAUDE.md` §3 — invisible to every instrument until an adversarial read, because it dodged both
  regexes and the module-prefix probe) must not be reproduced as a `preload()`/`load()` path
  literal inside a resolver body. The manifest is the seam; a path literal in a body is not — and
  it is exactly what §4.4's token-scan test catches, which is why that test scans by file path
  under `core/`, not by identifier name.
- **O-5's three-way disagreement, reconciled in one sentence rather than escalated:**
  `STRAT:75-77` (three `dice_pool` resolvers; a 2026-06-10 snapshot, stale on its own terms — the
  live `references/module_contracts.yaml` has `personal_combat: d_sigma`, R3 §4 parse row 26) and
  `01:1372-1373`'s "adds no resolver" are answers to different questions. "No resolver" governs the
  **outer** loop: conflict routing and the tick are never duplicated. Each attached subsystem still
  owns its **interior** dice model (d_sigma for personal combat, per the live registry). No
  contradiction survives once the two scopes are named; the registry is current, STRAT's table is
  history.

---

## 11. THE SKELETON — every file judged

Preliminary fact, confirmed exhaustively by R3 §3 and consistent with my reads: **no `.gd` file in
this repo defines `BaseEngine`, `EngineModule`, `Key`, `KeyBus`, `GameState`, `Resolver`,
`MechanicsRegistry`, or `Kernel`.** The skeleton extends and calls a spine that exists nowhere.

| file | verdict | ground |
|---|---|---|
| `core/engine_manifest.gd` | **KEEP as the pattern; rewrite for the new spine** | the manifest-as-data seam is correct and matches `composition.py` (O-3); self-contained |
| `core/key_type_resource.gd` | **KEEP as the pattern** | same; its loader (`KeyTypeRegistry.load_from_dir`) exists only in a docstring — the stage-2 generator supersedes hand-authored type `.tres` anyway |
| `engines/combat/combat_engine.gd` | **REWRITE wiring; harvest structure** | `_fight_over`/`_emit_combat_resolved` reach `GameState`/`KeyBus` globals (`:43,52,55,60`) — §4's anti-pattern; the manifest-driven module list and `consume()` dispatch shape are worth keeping |
| `engines/combat/modules/strike_module.gd` | **HARVEST the math; REWRITE the wiring** | the ported oracle math is real value: the ER-2 continuity correction (`:141-151`), the ED-PC-0037 attacker-bias removal with its ED-1050 rationale (`:60-62`), the bilateral-Ob term (`:59`). The wiring is the named anti-pattern three times over: `GameState.get_actor` (`:38-39`), the shared re-seeded global RNG (`:67`, M-15), `GameState.rng.randfn` (`:138`) |
| `engines/combat/modules/wound_module.gd` | **FIX ONE LINE; harvest the rest** | **the contract violation, confirmed by direct read:** `:29-31` declares `{"name": "health", "bucket": "derived_value", "writable": false}` under the F1 GUARD comment (`:12-13`), and `:55` then executes `actor.set("health", maxf(0.0, health_full - cum))` — a direct write to the field its own manifest declares non-writable, with a comment calling it "(read-only)". **The write is not even needed**: the felled test (`:57`) uses `cum >= health_full` directly. Fix: delete `:55`; `health` becomes a computed read (`health_full − cum`), i.e. a Query — which is what the F1 comment already claims it is. Neither `04` nor the five runners caught this; R3 did |
| `engines/combat/resources/combat_config.gd` | **KEEP** — the proven Resource-for-tunables pattern (`:1-12` records the dead-DAMAGE_SCALE defect it fixed; `:53-58` records the ED-1050 oracle-discipline resolution). Its four untyped `Dictionary` `@export`s (`:27-41`) are m-4: `[4.6-GATED]` typed dictionaries, fallback const index maps |
| `resources/weapon_resource.gd`, `tradition_resource.gd` | **KEEP** — data-not-code, correct |
| the `.tres` set under `data/` | **KEEP as reference; regenerate** — internally consistent with their `.gd` shapes (R3 §3 spot-checks) but hand-authored, which stage 2 (§2.4) forbids going forward |

**Is it a head start? NO — ruled plainly.** It does not compile, extends a spine defined nowhere,
and its wiring pattern is the one §4 exists to forbid. It is two other things: the only
executable-shaped statement of intent (evidence, which §3.2 of the audit used correctly), and a
partial transcription of oracle math with its editorial history attached (worth harvesting line by
line, never bulk-copying). **And one decision it forces, ruled here under §0's test 5:** the
skeleton's `BaseEngine`/`EngineModule` names must **not** become a parallel hierarchy — R3 §10
records that `valoria-game` already has a working, compiling `CoreEngine`/`CoreResolver` tree.
Harvest skeleton content into the existing compiled hierarchy; do not author `BaseEngine` from
scratch beside it. Recorded here so the next session doesn't re-derive it.

---

## 12. THE RANKED REGISTER, RE-ADJUDICATED

Verdicts: **CONFIRMED** (the finding is right) · **ALREADY-FIXED** (right, and the tree has
adopted the remedy — where, cited) · **OVERSTATED / WRONG** where earned.

| id | verdict | ground |
|---|---|---|
| F-1 | **CONFIRMED · fix ADOPTED in 01** (`01:700-712` §3.1a; honest residual also stated at `02:1122-1128`). Skeleton evidence re-verified (`strike_module.gd:38-39,67`, `combat_engine.gd:60`). §4 here is the binding mechanism + the earned check |
| F-2 | **CONFIRMED · fix ADOPTED in 01 ONLY** — `01:707-709` corrects it; **`02:844-846` still asserts the false claim verbatim** ("a shape the type system makes unwritable"). One edit owed to 02. §6 gives the enforcement |
| F-3 | **CONFIRMED · ALREADY-FIXED** — `Rung` adopted at `01:150-160` (read directly), `03` records it ADOPTED. Still unexecuted as a parse fact (`04:927-929`'s own limit); §13 step 1 executes it |
| F-4 | **CONFIRMED as arithmetic · fix ADOPTED in 01 (`01:454-470`) — correcting the brief and R3 §6 · UNSPECIFIED until now · residual in 02 (`02:570-578`, §10 table)**. §5 closes it: COND_SCALE=10_000, f as /16 integer pairs, half-up-on-magnitude rounding, clampi-once, cross-multiplied band gates, the float boundary named |
| M-1 (`Derived`) | **CONFIRMED** — collision established independently by R1 §8 (glossary rows; zero live code uses, so a pure vocabulary fix). `Query` adopted |
| M-2 (side column) | **CONFIRMED, and extended** — the fix's own carrier is incomplete: 12 of 18 resolver-side signature cells in `03` §5 omit the mandated `World` (§4.2, new finding). Also corrects 04's "12 of 20 rows" to 18 of 23 |
| M-3 (lazy caches) | **CONFIRMED** — barrier-built, read-only, discarded; adopted as stated |
| M-4 (de-individuation scan) | **CONFIRMED** — the named-by refcount is the design's own only-refcount (`03` §3.3's guard note); maintained at deposit/eviction which WITNESS already visits |
| M-5 (`.tres` saves) | **CONFIRMED [engine]** — ruled in §8 |
| M-6 / M-6b (hash, JSON 2^53) | **CONFIRMED [engine]** — §7/§8; plus this pass's [unclear] on GDScript int-overflow wrap, probed at §13 step 1 |
| M-7 (nesting depth) | **CONFIRMED** — caller-supplied cap, no default; the substrate precedent (`keys.py:428-437`) |
| M-8 (prose constants) | **CONFIRMED** under `CLAUDE.md` §0.05 — §2.4 item 4 adds three rows the audit didn't list (COND_SCALE, floor_fp table, wear) |
| M-9 (union types) | **CONFIRMED** — `(kind_tag, id)` pairs; the one-liner distinguishing a storage discriminator from a §14-row-13 resolver branch goes in `world.gd`'s comment block |
| M-10 (one class) | **CONFIRMED** — §3 row 1 |
| M-11 (`append`) | **CONFIRMED** — pre-sized `acts[i]` |
| M-12 (save models) | **CONFIRMED · RULED here** (§8): snapshot; STRAT:19 retained as harness. Veto-able, flagged §15 |
| M-13 (autoload plan) | **CONFIRMED** — `scene_tree_architecture.md:16-24` read directly; `STRAT:97,213` verified; the ruling is still open and now doubly load-bearing. **Escalated**, §15 |
| M-14 (`Rung.matter` untyped) | **CONFIRMED** — typed sub-record (Sites / stores / Records / transmission pointer as separate typed fields), before anything writes it |
| M-15 (shared RNG) | **CONFIRMED** — `strike_module.gd:67,138` read directly; §7.1 |
| m-1…m-9 | **ALL CONFIRMED**; m-3 (`Path` removed in 4.x) and m-5 (Resource cache) are [engine]; m-4 is the `[4.6-GATED]` pair's second member; m-9's three load invariants adopted in §8 |
| O-1 (cycles) | **CONFIRMED [engine]** — §9, standing note supplied |
| O-2 (engine_clock canon) | **CONFIRMED** — `references/module_contracts.yaml:1128-1160` (R3 §4 parse; gap_notes quote) vs `02`'s six-step spine. The re-point is a one-line editorial action on the contract's gap_notes, assigned as next-session work, **not** a Jordan question |
| O-3 (registry row proven both sides) | **CONFIRMED** — `composition.py:1-24` read directly; `engine_manifest.gd:1-4` read directly |
| O-4 (combat_bridge shape) | **CONFIRMED** — §10; the §4.4 test is its detector |
| O-5 (three resolvers vs none) | **CONFIRMED as a discrepancy · RECONCILED here** (§10): outer-loop "no resolver" vs interior dice regimes; live registry current, STRAT stale. And R3 is right that it is three-way, not two-way |
| O-6 (`World` undeclared) | **CONFIRMED** — `world.gd` is file one; its field list *is* the answer to "what may a resolver reach" |

**Added by this adjudication (missed by both formal audits):**
1. `wound_module.gd:55` self-contradiction (R3's independent find, confirmed; fix specified §11).
2. `03` §5's 12-of-18 missing `World` parameters (§4.2).
3. `Vector2` single-precision components — fine for Sensation, forbidden for any world-state pair
   (§3).
4. `World` was a Godot-3 built-in (now `World3D`) — free in 4.x, but the per-name scratch-probe
   discipline is extended to the whole roster (§2.3, §13 step 1).
5. The Python oracle has no substream implementation — parity is threshold-level until it does
   (§7.2).
6. `season_factor`'s open distribution now *blocks* `yield`'s fixed-point implementation
   explicitly (§5.3) — previously open-but-unwired.

---

## 13. THE BUILD ORDER — each step ends in something running

All steps in `valoria-game`. Per `CLAUDE.md` §0.2, each names its execution artifact; a step
without its artifact is not done, whatever documents exist.

1. **Scratch probes under the pinned binary** (whichever Q3 rules; until ruled, run under BOTH
   binaries and file both outputs). One script: register the full §2.3 `class_name` roster
   (executes F-3 and every collision claim); one line settling int-overflow wrap (§7.1);
   `RandomNumberGenerator.seed` negative-int round-trip. **Artifact:** the headless run log,
   zero parse errors on the roster file. *(This does not settle Q3 — `04:916-919`'s point stands —
   it prices it and executes the parse claims.)*
2. **The spine:** `World`, four carriers, `TenureStore`, fixed-point `condition`/`stores` +
   `fixedpoint.gd`, `Substream`. **Artifact:** a headless test that mints/alters/effaces under a
   seed, then re-runs with permuted delta order and asserts a byte-identical world hash — **the
   first of the design's four structural tests ever to run** (order independence, §5's falsifier).
3. **Params ingestion:** stage-2 generator (JSON → `data/*.tres`) + `Params` holder. **Artifact:**
   boot log printing loaded row counts + a round-trip equality check against the stage-1 JSON.
4. **The loop, minimally:** six steps over a toy world (no contest, no channels). **Artifact:**
   an N-season headless run log, plus snapshot save → load → identical world hash (§8's falsifier).
5. **WITNESS + CENSUS:** fan-out, per-person deposit, eviction, de-individuation refcount (M-4).
   **Artifact:** the two-witnesses-of-one-event-disagree test — structural test 2 — green in the
   run log.
6. **The two §0.1-pt-5 guards** (§4.4 autoload/token scan; §6's one-call-site assertion) wired
   into the game repo's CI. **Artifact:** a deliberately-broken branch showing each red.
7. **The seam:** `ContestResolver`, one manifest row, boot-time full-resolution pass, a stub
   contest with a depth cap. **Artifact:** boot log resolving every row + one contest resolving to
   an Event.

Steps 2-7 are gated behind the two escalations in §15 only where they touch state ownership
(step 2 onward assumes the §2.2 autoload direction; if Jordan rules for `Meta`, everything from
step 2 is re-planned — which is exactly why §15 item 2 goes first).

---

## 14. WHAT I OVERTURN

1. **The brief's / R3 §6's "F-4 is STILL UNADDRESSED at `01:445-449`"** — overturned as to
   `01_ARCHITECTURE.md`: the fixed-point block is adopted at `01:454-470`, five lines below where
   R3 stopped reading. Sustained as to `02_THE_SEASON_LOOP.md:570-578` and `02` §10. F-4's
   remaining substance was the missing concrete spec; §5 supplies it.
2. **"F-1, F-2 … are already remediated" (the brief, from R3)** — refined: remediated in **01**;
   `02:844-846` still carries F-2's false claim verbatim. One edit owed.
3. **`STRAT:19` as the save model** — overturned (§8): snapshot saves; the log-replay machinery
   survives as the test harness, not the load path.
4. **The skeleton's implied `BaseEngine`/`EngineModule` parallel hierarchy** — overturned (§11):
   harvest into `valoria-game`'s existing compiled `CoreEngine`/`CoreResolver` tree.
5. **`04 §3.3`'s "12 of the 20 rows"** — corrected to 18 resolver-side of 23 catalogue rows, and
   the catalogue's own cells owe 12 `World` parameters (§4.2).
6. **`04 §6.5`'s fix 1 (canonical summation order) as an acceptable alternative** — demoted:
   permitted only as a fallback wording, never the mechanism; fixed point is ruled, not preferred.

Not overturned, explicitly: the audit's headline verdict (buildable, and buildable well, as a
headless value-graph transaction — §2/§3 here are that verdict made binding); the four-FATAL
census; `STRAT:128` on signals; the module-contract facts (independently re-parsed by R3 and
matching `CLAUDE.md` §6's corrected nine-module `doc: null` set).

---

## 15. WHAT ESCALATES TO JORDAN

Applying `CLAUDE.md` §0's five tests in order to every candidate; only survivors listed. Closed
without escalation: the save model (test 5 — architecture answer taken, §8, recorded); the O-5
resolver-count discrepancy (test 3/5 — reconciled §10); the engine_clock re-point (test 5 —
editorial action, assigned); the skeleton-hierarchy question (test 5 — ruled §11); "does the
twelve-act table subsume combat/social/mass battle" (R6's flag; test 3 — answered by `01` §8's
seam: they are contest-interior, out of the seasonal vocabulary by design); the wound_module fix
(test 5 — one-line engineering).

1. **Q3 — the engine version.** Survives all five: no successor ruling exists (`CLAUDE.md:10`
   explicitly awaits one); not irrelevant (the ratchet and two language features hang on it); no
   design doc answers it (the one that did no longer exists on `main` and is unreachable at its
   fork ref from this shallow clone); no precedent; and the architecture cannot answer it because
   it is a *target* declaration binding two repos' CI, prose, and `project.godot` at once — and
   `CLAUDE.md` §3 forbids a session picking it. **The precise ask is §1.3.** The one fact to carry
   into the ruling: 4.6's documentary anchor is gone; 4.3 has two executed runs; and **whichever
   way it goes, the 84-error ratchet is only meaningful under the binary it was measured on.**
2. **`STRAT:213` (Part VIII #5) — the autoload ruling.** Survives: explicitly reserved for Jordan
   in the governing spec since 2026-06-10; still open (nothing in `godot/` or the ledgers records a
   ruling — R3 §1, consistent with everything read here); and the two defensible options now lead
   to materially different ports — the live `Meta`-single-state-owner pattern versus the new
   design's no-live-state-behind-any-global-name rule are direct opposites
   (`scene_tree_architecture.md:16` / `STRAT:97` vs `01:700-712`). **Recommendation attached
   (§2.2): rule autoloads presentation-only; `World` driver-owned.** This is the fork every
   state-touching build step waits on; it goes first.

Nothing else survives. The `needs_jordan` queue gains at most these two rows.

---

## 16. CONFIDENCE per ruling

| ruling | confidence | weakest link |
|---|---|---|
| §1 version handling (evidence table, 4.6-gated writing) | **high** on the repo facts (all read directly or via R3's line-verified table, spot-confirmed); **medium** on "4.6 would reproduce the error class" (a prediction, labelled as one) |
| §2 code shape | **high** — every constraint traces to a verified source; the layout itself is judgment, offered as binding but revisable at file granularity |
| §3 carriers, incl. Sensation=Vector2 | **high**; Vector2 32-bit component claim is [engine], standard-build only — the double-precision build option note is the hedge |
| §4 purity mechanism + earned check | **high** on the mechanism (design already adopted it; engine facts uncontroversial); **high** on the §0.1-pt-5 justification (the port is a named qualifying subject). The 12-of-18 catalogue finding: **high** (counted twice, in 03-via-PR344 and 01:555-570 directly) |
| §5 F-4 spec | **high** on the arithmetic and the adoption-status correction (read `01:454-470` directly); **medium** on the specific constants (COND_SCALE=10_000, half-up) — deliberately parameterized and exported so a re-ruling is one row, not a rewrite |
| §6 witness | **high**; the one-call-site guard is convention+test, honestly labelled weaker than a type |
| §7 determinism | **high**, except the GDScript int-overflow wrap **[unclear]** — probed at step 1 before the hash ships |
| §8 save/load | **high** on format facts [engine]; **medium-high** on the snapshot ruling — architecture-answered, veto-able, flagged |
| §9 ids | **high** — engine fact + design's own documentation of its cycles |
| §10 seam | **high**; O-5 reconciliation is interpretive but grounded in the live registry |
| §11 skeleton | **high** — every file read in full; the wound_module defect verified at both cited lines |
| §12 register | **high** — each verdict carries its own ground above |
| §13 build order | **medium-high** — sequencing judgment; each artifact is falsifiable |
| §15 escalations | **high** — the five-test walk is shown for the closures as well as the survivors |

**Standing limit:** nothing in this document has executed. Every [engine] claim awaits §13 step 1's
scratch log; every repo claim is text at a cited line; `04:933-934`'s rule applies to this file
too — where a citation is wrong, the ruling resting on it is wrong.
