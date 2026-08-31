# 01 · THE ARCHITECTURE — the primitive set

## Status: PROPOSED (2026-08-31). **Nothing here executes.** `CLAUDE.md` §0.05: this is reference, the
## code is the mechanism. §0.2: done means it runs. Every claim below is an argument about text, and
## where a claim would be settled by execution it is marked unsettled rather than asserted.

**Citation key.** `keys.py:NNN` and other bare repo paths resolve at the working tree (`CLAUDE.md` §2).
`ARCH:NNN` is `proposals/2026-08-31-ideal-v2/01_ARCHITECTURE.md`. `SUP:NNN` is
`proposals/2026-08-31-ideal/10_SUPERSEDING.md`. `[engine]` marks a claim about published Godot
behaviour rather than about this repository.

---

## §1 · THE GROUND THIS SET IS CHOSEN ON

Four primitive sets were proposed across #337–#344. The authoritative one is the head's
(`ARCH` §2), with four amendments ruled in below. **It is chosen on grounds, not recency:**

1. It carries Jordan's verbatim rulings *as structure* rather than as commentary — the Partition, the
   containment axiom, Kingdom-and-Duchy-as-factions, D-2's one act, community and family as required
   rungs.
2. It composes on the executing substrate by citation rather than beside it.
3. It survived structurally-independent adversarial review — five audit runners, an antagonist that
   broke four of its own parent review's claims, and two Jordan ontology corrections.

**What the other three are now.** #339 is archived by its own adversarial pass. #340 is neither
authoritative nor dead: it is **the content-layer quarry** — its world-events schema, its ambition
carrier and its slate remain the best worked versions of mechanisms this set specifies only
abstractly. #343's `SUP` remains source-of-truth for everything the head's §10 does not depart from.

---

## §2 · THE PRIMITIVE SET

### §2.1 The four carriers — things that exist and change

```
Person := (id, weight, marks, capability, stance, ledger, ties)   -- weight >= 1, default 1
Rung   := (id, kind, stake[], judging_set_rule, dates[], matter, envelope)
Office := (id, post, rung?, remit, conferral, revocation, establishment, dates[], upkeep)
Site   := (id, rung, kind, condition, drawers[])
```

**A cohort IS a Person at weight > 1.** One type, no conversion operation. This is not a convenience:
it is what prevents elite-only politics by construction. A design with a separate cohort type
manufactures a world in which only named people act.

**`Rung` is the name.** `Node` and `Container` are both refused, and the second refusal corrects the
head's own earlier choice — `Container` is *also* a Godot built-in (the `Control`-derived base of
`VBoxContainer`), and it collides worse than `Node` because `Node` would fail loudly at once while
`Container` silently shadows a UI type. `Rung` is the tree's own word, from `SUP:337`'s own gloss.

**`Site` is a carrier and `condition` is primary state on it.** The argument is short and decisive:
an accumulator that reads its own previous value *is* primary state, so `condition` cannot be a
Query; a draw-weighted mean over child sites has no base case; and node-keying destroys site identity
— a settlement holding a silted harbour at 0.1 and a healthy seam at 0.9 collapses to one scalar near
0.5, which keeps the bulk-shipping verbs the harbour should have closed and closes the mining verbs
the seam should have kept. **Base case, stated: at a Rung with no Sites beneath it, `condition` is
undefined and the verb gate does not fire.**

### §2.2 ⊕ AMENDMENT A1 — the fifth identity-bearing record, stated rather than fudged

The head says "four carriers" while `Proposition` carries an id, persists, is a Tenure subject and
object, and is a stance referent. Left unstated, "four carriers" is quotable into a false claim.

> **A carrier is an identity-bearing record with MUTABLE state. A `Proposition` is the one
> identity-bearing IMMUTABLE record — fixed at utterance, never effaced.**
> **Five identity-bearing kinds. Four carriers.**

This costs one sentence and closes a real seam: it is why a faction can be fully derived from a
Proposition plus its `commit` edges without the Proposition being a fifth owner.

### §2.3 Identity — how everything is named

> **IDS ARE MINTED FROM THE DETERMINISM SUBSTREAM AND FROM NOTHING ELSE.**
> ```
> id(x) = H(world_seed, tick, subject_id, purpose)
> ```

`purpose` is a short discriminator naming the operation and, for a multi-`mint` act, its slot:
`mint:0`, `mint:1`, `yield`, `festering`, `ageing`, `attempt:2`. **Its domain is open and its
stability across runs is the determinism requirement** — changing a `purpose` string changes every id
downstream of it.

**One mechanism closes two problems that were filed separately.** Ids are deterministic,
order-independent and unique **without a shared allocator** — and a shared allocator is exactly the
mutable global that would break the per-person parallelism licence. There is no id service, no
counter, and nothing to serialise on.

**This is copied from the executing substrate, not re-derived.** `Key.id: str` at
`engine/substrate/keys.py:145`; uniqueness enforced as an invariant; referential integrity as a
further invariant — a `causes` entry naming an unknown id raises; cycle-freedom by construction for
an append-only log; lookup by id as a first-class operation.

> ### ⚠ STANDING NOTE — DO NOT "FIX" IDS INTO POINTERS
>
> Storing ids and resolving them looks like avoidable indirection to anyone who knows Godot. **It is
> load-bearing for a reason the design did not originally know it had: [engine] Godot has no cycle
> collector.** `RefCounted` is reference-counted only, so a reference cycle is a permanent leak.
>
> **And this reference graph is cyclic by construction.** `succeed ∘ contain` — Rung → Person → Rung
> — is the *normal* case, because the heir lives in the hearth. Ties and knots are symmetric. Claims
> cite claims. Conferral paths may cycle.
>
> **Ids break every one of those cycles at the storage layer.** Anyone proposing to replace them with
> typed object references is proposing an unbounded leak in the object graph the game is made of.

### §2.4 The one edge — `Tenure`

**This is the record every disputable political fact is made of** — who holds what, who is committed
at what degree, who contains whom, who owes whom.

```
Tenure := (id, subject, object, kind, since, until?, conferrer?, degree?, payload?)
   subject   ∈ Person | Rung | Proposition
   object    ∈ Person | Rung | Office | Site | Proposition
   conferrer ∈ Person | Office | null
   kind      ∈ hold | commit | contain | succeed | tie | knot | oblige
```

#### The seven kinds, with cardinality declared on the schema

| kind | subject → object | what it is | created by | destroyed by | cardinality |
|---|---|---|---|---|---|
| `hold` | Person → Office | office | `confer` | `revoke` | **1 per Office** |
| `hold` | Person \| Proposition → Site \| Rung | enfeoffment, lordship, **annexation** | `confer` | `revoke` | **1 per object** |
| `commit` | Person → Proposition | faction membership at a degree | `commit(+Δ)` | degree → 0 | 1 per (subject, object) |
| `contain` | Person → Rung, Rung → Rung | address; the containment tree | `admit`, `migrate` | **never bare** | **1 per subject** |
| `succeed` | Rung → Person | the hearth's succession pointer | a naming act | re-naming | **1 per Rung** |
| `tie` | Person → Person | ordinary contact | co-presence | decay | 1 per unordered pair |
| `knot` | Person → Person | the deep channel | `form_knot` | rupture | 1 per unordered pair |
| `oblige` | Person → Person | kin obligation | kinship, admission, oath | discharge, death, repudiation | 1 per (subject, object) |

> **CARDINALITY IS DECLARED PER KIND, ON THE SCHEMA, AND THE CONFLICT RULE READS IT.** Two acts
> conflict if they both `mint` edges that jointly break a declared cardinality. Without this, two
> `succeed` edges on one hearth, two `hold` edges on one office and two `contain` edges on one person
> are **each individually legal, no conflict fires, and the invariant breaks only after both
> resolve.**

**`tie` and `knot` are stored ONCE, on the endpoint with the lower id.** A shared `strain` gauge on a
directed record otherwise has two homes and can disagree with itself. The other endpoint reads it
through the derived inverse index.

**`contain` is never destroyed by a bare `revoke`.** A person's address is their path to the root;
revoking their `contain` edge orphans them, and revoking a Rung's orphans a subtree. **Migration and
secession are `confer` to a different parent, atomically, in one act.** No operation leaves a subject
unparented.

**`annex` and `secede` are not verbs and are deleted from the vocabulary.** Annexation is a `hold`
Tenure over a Rung changing hands; **the tree does not move.** This is Jordan's own ontology — the
tree is geography, allegiance lives in factions, a hamlet does not move because a King won a war.
`secede` is additionally barred as a word because the corpus already ships *secession* for a duke's
**defection**, which is a `commit` moving away. Three operations, three words, no collision.

### §2.5 ⊕ AMENDMENT A3 — a Tenure is owned by its subject, whichever carrier that is

The head's ownership table states the rule only on the Person row ("every Tenure whose subject they
are"), while `succeed` has a Rung subject and `hold` permits a Proposition subject. The Rung and
Office rows never mention Tenures at all.

> **EVERY TENURE IS OWNED BY ITS SUBJECT, WHICHEVER CARRIER THAT IS. One home, one writer, no
> reach-through. The object side is a derived index, never stored.**

### §2.6 ⊕ AMENDMENT A4 — the `hold` collision with live code, recorded and disarmed

The head's collision register found four meanings of `hold`. **There is a fifth, and it is in running
code:** a mass-battle unit's tactical stance, `systems/mass_battle/sim/config.py:269`
(`STANCE_SPEED_MOD['hold'] = -99`). A meaning in executing code outranks a meaning in prose
(`CLAUDE.md` §0.05), so the disambiguation must survive it.

> **The edge kind is always written `Tenure(kind=hold)` or "a `hold`-edge", and is exported as
> `tenure.hold`, never as a bare `kind:` value. The mass-battle stance keeps the bare string inside
> its own module. The Proposition mood is `HOLDS`, capitalised. The predicate form is always written
> with its arguments, `HOLDS(p, x)`.** Four spellings, four meanings, no bare token.

### §2.7 The one state change, and Jordan's Partition

```
StateChange := (subject, mode, driver, field?, delta?, spec?)
   mode   ∈ mint | alter | efface
   driver ∈ Act | Event
```

carried in `Act := (id, actor, verb, changes[], reads[], contests[], payload)` and
`Event := (id, kind, subject, changes[], emitted_at)`.

> **PARTITION EVERY STATE CHANGE BY ITS SUBJECT.** A change whose subject is peninsular human society
> — polities, institutions, offices, organizations, occupations, religion, settlements, marriage — is
> **driven by a character's choice, always.** A change whose subject is anything else — weather, the
> non-peninsular, tears in the metaphysical substrate — is **an event acting on the world.**
> **Creation and deletion included: events create and destroy too.**

### §2.8 ⊕ AMENDMENT A2 — the Partition's membership test is a schema column, not a judgment

This is the amendment that makes the Partition implementable. As stated, the Partition is a
predicate over "subjects", and a predicate a programmer must adjudicate per instance is a convention,
not a mechanism — it will drift the first time a hard case arrives.

> **`social` IS A STATIC BOOLEAN COLUMN ON THE (subject-type, field) PAIR, DECLARED IN THE EXPORTED
> SCHEMA AND READ BY THE RESOLVER.** A change is Act-driven if and only if its `(subject-type, field)`
> row is marked `social: true`. `Event` drivers may write only rows marked `social: false`.
>
> The test is then decidable at the call site and at load time, not by argument. **The hard case the
> Partition exists to settle is a schema row, and it reads exactly as Jordan stated it:**
> `(Site, condition)` is `social: false` — a plague or `wear` may move it — while
> `(Rung, exists)` is `social: true`, so **a plague may kill every body in a village and may not
> efface the village.** The roll is struck by an office, or not at all.

**Ruled `mint`/`efface` naming.** `CLAUDE.md` §4 requires words that are *idiomatic in choosing* and
*idempotent in meaning* to a session with no context. `mint` and `efface` are coinages where
**`create` and `destroy` are the ordinary words**, and a later session reading `efface` cold will not
reliably recover "delete". This suite records the objection and **keeps `mint`/`efface` in the schema
for one reason only: `create`/`destroy` are near-universal identifiers likely to collide in GDScript
and in every module that already uses them as method names.** The coinage is therefore justified by
collision-avoidance, which §4 permits, and **it must be defined at the call site as well as here** —
in the exported schema's own comment, not only in prose.

---

## §3 · THE OWNERSHIP TABLE

**Four owners and Nobody.** Every value in the game is in exactly one row.

| owner | owns | never owns |
|---|---|---|
| **Person** | everything interior — marks, capability, stance, the claim ledger, ties; every Tenure whose subject they are; the Propositions they utter | anything about another person; any aggregate |
| **Rung** | matter (`stores`, the transmission pointer, Records kept there), dates, the demographic envelope, `stake[]`, the judging-set rule | **any social aggregate** — no norms, no densities, no reputation |
| **Office** | post, remit, conferral rule, revocation rule, establishment, dates, upkeep | who holds it (that is a `hold` Tenure on the holder) |
| **Site** | `condition`, `drawers[]`, kind | anything social |
| **Nobody** | **every aggregate**: faction, leaders, presence, density, footprint, norm, scale, reputation, needs, openings, entrenchment, coarse condition | — these are Queries, recomputed, stored nowhere |

**The Faction row is deleted, and the deletion is stated as an amendment because the row existed.**
A faction is derivable in full from a Proposition plus its `commit` edges. `SUP:334-340`'s five-row
table had a Faction owner; this set has four. Nothing is lost: membership is `commit`, leadership is
a Query, footprint is a Query, and the thing that persists — the proposition itself — is the
immutable record of §2.2.

**⚠ Where this collides with running code, and it does.** `engine/autoload/game_state.py` ships
`Faction` as a stat-bag with stored aggregates and roughly 31 `.adjust()` writer sites. **That is not
a base to refactor — it is the thing this table forbids.** The path is the repo's own established
one: build beside it, flag-gated, golden-controlled, cut over. `07_EXECUTION_PATH.md` sequences it.

---

## §4 · THE THREE SIGNATURES

```
choose  : (Person, View, Sensation) -> Act        # NO World, ever
resolve : (Act[], World)            -> Event[]    # NO Person
witness : (Person, Event)           -> Claim[]    # per-person; a collection is a type error
```

**They are the enforcement mechanism and they work by what they omit.** `choose` has no `World` — not
masked, not read-only, not behind an accessor. `resolve` has no `Person`, so the resolver acquires no
per-actor special case. `witness` takes the person first, and no signature accepts a collection of
persons and one event.

> ### ⚠ THE GUARANTEE IS WEAKER IN THE PORT THAN IN THE ORACLE, AND SAYING SO IS THE POINT
>
> **[engine] GDScript has no module system, no visibility modifiers, and no way to scope an
> identifier out of a function body.** An autoload is a global identifier reachable from any script,
> `RefCounted` included; `class_name` statics and `load()` by string are two further doors. **So
> omitting `World` from `choose` does not make world access unwritable — it makes it unwritten.**
>
> The port's own skeleton is the proof rather than the hypothesis: `godot/skeleton/.../strike_module.gd`
> and `combat_engine.gd` reach `GameState` and `KeyBus` **from inside a resolver module.**
>
> **The guarantee moves from *unwritable* to *unreachable-by-name*** — human-checkable on one screen
> of project settings rather than compiler-checked. `03_CODE_SHAPE_GODOT_4_6.md` §3 specifies what
> restores most of its force. **A false claim of enforcement is worse than none, because it stops the
> next reader from checking.**

**`Sensation` is a proposal against a problem the review left open, and is offered as new.**

```
Sensation := (subsistence, standing)      -- exactly two scalars
```

The problem: subsistence and standing read *the world*; needs are pure, parallel and never stored;
the View is assembled from claims only. **There was no legal path from a need to the function that
uses it.** `Sensation` is computed inside DELIBERATE, over the world as frozen at the end of MATTER,
by `sense(person, frozen_world)` — which is not a decision function and may therefore take a World.
It is never stored, carries no references, and answers no query. Two scalars, not four: commitment
and exposure read the *view* and are computed inside `choose` from what the person already holds.

**A Sensation is un-nameable, therefore undisputable.** No person can hold a claim about another's
hunger. Claims reach the larder and the body, and stop there.

---

## §5 · THE QUERY CATEGORY

**A `Query` is never stored and always recomputed.** The rename from `Derived` is not cosmetic and was
verified necessary: `references/glossary.md:75-82`, `params_tables.yaml` and
`references/descriptor_registry.yaml:284` all use `Derived` for **stored** per-character values, in a
flat global namespace — the exact opposite meaning.

**Two classes, and the split is the enforcement point.**

| class | takes | may read | examples |
|---|---|---|---|
| **resolver-side** | **`World` as the FIRST parameter** | world truth | `leaders`, `presence`, `density`, `footprint`, `verbs(site, c)`, `condition` at a rung, `sovereign_fraction`, `filter_share` |
| **person-side** | the asker | only the asker's own ledger | `opening_set(person, view)`, `entrenchment`, `norm` as believed, `address` |

**Putting `World` first on every resolver-side Query is what preserves the purity guarantee in the
port.** Calling one from inside `choose` then fails at the call site for want of an argument. It takes
enforcement-by-omission from 3 signatures to 23 — and converts a table a reader must remember into a
call site that fails.

**Executable precedent exists and should be copied:** `canon_buckets.canonical_accord` and
`descriptors.faction_bounds` are already Query-shaped — computed, not stored.

---

## §6 · WHAT IS EXCLUDED, AND WHAT ALREADY COVERS IT

Every exclusion is justified by what covers it, per `CLAUDE.md` §0's bottom-up rule.

| excluded | covered by | ground |
|---|---|---|
| **Entity** with a closed kind enum (#339/#340) | four typed carriers | #339's own archival lesson: a closed kind enum on one struct froze what must grow |
| **Tag** (5 then 7 kinds) | `Claim` + `stance` + `Tenure` + `until?`-as-history | a tag family is a claim vocabulary wearing a struct |
| **Gauge** (bounded, decaying, no setter) | `Query` for every aggregate; primary state only on `Site.condition` and `stores` | the refusal of scheduled social recovery. The decay law survives narrowly, in claim confidence and recency |
| **Post budget** | D-2's one act + `capacity(date)` | they are one quantity seen from two sides; treating them as two produced a double-count |
| a **Faction** carrier | Proposition + `commit` Tenures | §3 |
| a **second resolver** | one `resolve` for all fidelities | fidelity controls who supplies the act, never how the outcome is computed |
| **`annex`/`secede`** verbs | `confer` on `hold` | §2.4 |
| a **fifth `Claim` source** | `research → told_by(record, …)` | already shipped; the head withdrew its own proposed fifth |
| **`seat_items`** | D-2 unifies it with `capacity(date)` | deliberate deletion, recorded, not a silent drop |

---

## §7 · WHAT IS CARRIED AS OPEN

Stated so no later document can cite this one as though these were closed. The full gap register is
`05_COVERAGE_AND_SUPERSESSION.md` §4; these are the ones that bear on the primitive set itself.

1. **The `wear`-to-restoration ratio.** Jordan's F6 ruling — the world is in flux and its direction is
   the sum of what people do about it — cost one constant, `wear`. **The ratio of `wear` to a
   restoration act's effect sets the entire difficulty curve.** Too high and the world dies whatever
   anyone does; too low and tending is decoration. **This is a measurement, not a ruling, and nothing
   has been run.**
2. **`leaders`' comparator.** Deposition and faction demotion both rest on it. Faction-as-Proposition
   forces a commitment-derived comparator; *commitment degree × backing raisable* is the proposal on
   file. Adopt and record rather than escalate.
3. **Where the channel store lives** — a minted person's *plausible past*. Ruled against three ways.
   Character generation works without it; the plausible-past property does not.
4. **The cohort's construal spread** — where it lives, what produces it, what an individuating member
   draws from. Under-specified upstream; not closable inside this set's refusals.
5. **`Rung.matter`'s structure.** Four things are addressed by name inside it — Sites, `stores`,
   Records, the transmission pointer — and an unstructured field cannot be indexed. Needs a typed
   sub-record per kind.
6. **`World`'s record.** Every refusal is written against it and it has no fields. **It is the first
   thing a typed port must declare** — which is why `03` declares it first.
7. **`Event`'s record beyond id and degree band** — resolved in this suite by composing Event onto the
   executing `Key`, but the field mapping is unwritten.
8. **Age-band boundaries in `Envelope`; channel latency values; `season_factor`'s distribution.** All
   three are numbers with no home. The third may already be answered by `11_world_events.md`'s rate
   bounds, which this line has still not read.
