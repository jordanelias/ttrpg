# 01 · THE DESCENT — what a module may receive, emit and own, in one hierarchy

## Status: **PROPOSED (2026-09-01). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.** Nothing here runs.
## Scope: **PR #337 → #352 only** (`00_ADJUDICATION.md` §0). Nothing ratified before #337 is authority.
## This is **M2** — the missing descent named in `00` §1.

---

## §1 · WHY THE HEAD NEEDS ONE, IN ITS OWN TERMS

`01_THROUGHLINE.md` makes two throughlines structural and both of them are per-module claims:

- **T5** — *"demands aggregate **UPWARD** and are filtered at a rung."*
- **T6** — *"large actions ripple **DOWNWARD**"*, a Dispensation *"published as a `tell`, **distorts in
  transit**, and reaches a postless person through **their own** `opening_set`."*

**Both require knowing, per module, what it may receive and what it may emit.** R-2's *"no module
reaches through another"* is the same requirement stated as a prohibition. **The head has no surface
that answers it for any module**, which means R-1 and R-2 are today unenforceable in principle, not
merely unenforced.

**The chain has raised this twice already, and both attempts are in scope.**

| # | in-chain incumbent | its levels | status |
|---|---|---|---|
| **A** | `proposals/2026-08-28-greenfield-systems-suite/00_INDEX.md` §1 (PR #339) | `GAME → (SCALE ⊥ TIER) → SUBSYSTEM → MODULE → {STATE · KEYS · REMIT · VIEW}` | **ARCHIVED** by its own adversarial pass (#340) — but #345 records that *"its resolution mechanics survived intact into v2; **its scope is what died**"*, and the hierarchy was not what failed |
| **B** | `proposals/2026-08-31-authoritative-architecture/04_THE_REGISTER.md` §3 (PR #345) | `family → type → contract → module → role` — *"one validated parent, three leaves"*, generated, blocking `--check` round-trip, *"deliberately ontology-neutral"* | **PROPOSED, live, uncontradicted** |

**What each got right, and it is most of the work:**

- **B is the transport, and nothing below changes it.** *One validated parent, generated, gated by a
  round-trip.* B's own closing line binds here: *"**A specification is not a discharge; the exporter
  is.**"*
- **A is the root and the axis insight.** It roots at `GAME` — B does not, and a hierarchy a reader
  cannot enter from the top is a provenance chain rather than a descent. And **A's `SCALE ⊥ TIER`
  split is the best single move in either**: *"two different questions have been forced into one
  field"*, and forcing them apart *"routes around"* a vocabulary collision rather than pretending to
  resolve it. **That move is adopted below, generalised.**
- **A also carries `SUBSYSTEM` with one wrapper owning all its Key I/O** — which is `00` §1's M1,
  correctly placed as a level rather than as a runtime afterthought.

**Three departures, each with its reason:**

1. **B's order runs the wrong way for a descent.** `family → type → contract → module → role` reads
   upward — this type, the contract carrying it, the module, the role it fills. As a *descent*,
   `role → module` is the direction `09_THE_SEAM.md` §5 already fixes: *"the engine names the **ROLE**,
   the registry names the **MODULE**, resolution happens by string."* **Inverted below.**
2. **B is "deliberately ontology-neutral", and the levels are the question.** Neutrality defers exactly
   what T5 and T6 need decided. **§2 decides it, including the negative half.**
3. **A's leaf set is its archived primitive roster.** `{entity · gauge · tag · post}` did not survive
   #340/#345/#350. **The leaves below are the carriers and Key types the head specifies.**

---

## §2 · A SPINE, AND AXES THAT ARE NOT LEVELS

> **A LEVEL is a parent: knowing it constrains what the child may be.**
> **An AXIS is an index: it selects a set of nodes without containing them.**
>
> **Promoting an axis to a level is how you get a hierarchy in shape and not in meaning.** Incumbent A
> found this once for `scale` vs `tier`; the same distinction, one level up, resolves the rest.

### §2.1 The SPINE — six levels, a strict tree

```
GAME
 └── SUBSYSTEM     one lane · one folder · ONE WRAPPER owning all its Key I/O      [A §1; 00 §1 M1]
      └── ROLE          what the engine calls by name, never by import             [09_THE_SEAM.md §5]
           └── MODULE        the provider the registry names — swapped by editing a row
                └── KEY TYPE      what this module may emit and consume            [T5/T6's requirement]
                     └── FIELD        what a Key of that type carries, and its bounds
```

| edge | what knowing the parent tells you |
|---|---|
| **game → subsystem** | **whose wrapper owns the Key I/O** — the one file every Key crossing that boundary passes through. This is the level that makes R-2 checkable at all |
| **subsystem → role** | **what the engine is entitled to ask of it.** The engine never learns which module answers |
| **role → module** | **who provides it, and what may be swapped** — *"a subsystem is swapped by editing a row"* |
| **module → key type** | **the module's complete declared I/O.** The level a session reads to work one module without reading the world |
| **key type → field** | **what a value means and what bounds it** |

### §2.2 The AXES — `phase:`, and scale

```
MODULE ──indexed by──►  phase:   CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS · CENSUS   (required, closed)
       ──indexed by──►  scale/tier   A's split, kept as an annotation                          (advisory)
```

#### `phase:` is what this document adds, and the write matrix is why

`04_THE_SEASON_LOOP.md` §4's write matrix is **indexed by phase**, with *"any unmarked cell is a
write-class violation."* **So a module that does not declare its phase cannot be checked against it**,
and three things stay unaskable that become row checks the moment it does:

1. **Is this module's declared owned state write lawful?** Cross `phase:` against the matrix.
2. **Can its `consumes` ever be satisfied?** A module at DELIBERATE consuming a type only emitted at
   CENSUS is a **one-season latency** — which `04` §8 rules is the design's real behaviour
   (*"you anticipated, or you are late"*) but which today is indistinguishable from a wiring bug.
3. **Does anything write during DELIBERATE?** `04` §7 lists that refusal as mechanical **via the return
   shape only**. At the registry level it becomes a row.

**And it is an axis, not a level, for a structural reason:** a subsystem spans phases and a phase spans
subsystems. Nesting either inside the other duplicates one at every node of the other.

#### Scale stays an annotation — the negative answer, and it is load-bearing

> **SCALE IS NOT A LEVEL OF THE CODE HIERARCHY.**
>
> **It is the wrong axis for code.** A module is not "a settlement-scale module"; it is registered
> against a role and runs at whatever rungs the phase hands it. Indexing code by scale deletes the
> property that makes the ladder worth having — `10_GODOT_4_6.md` §5.2's *"**one rung type,
> instantiated at every rung, means a mechanism written for elites is automatically available to
> populations**."* **Scale-indexed code is scale-divergent code**, and the divergence is invisible
> until a wrapper composes across a boundary.
>
> **This is incumbent A's move, re-aimed.** A split `scale ⊥ tier` and said of it: *"This does not
> resolve the collision; it routes around it… compatible with either outcome."* **The same holds here:
> an annotation on a leaf's parent costs nothing if the vocabulary later changes; a spine does.**
>
> **The world's containment ladder is a different thing and is already specified:** `Rung.kind`'s eight
> members (`02_ONTOLOGY.md` §2.2.1), realised as *"a directory tree and a `Rung.kind` enum… not a type
> hierarchy"*, with `contain` **Tenure edges** as the parent relation. **A `Tenure` edge is how a holon
> names its parent.** That is the WORLD hierarchy; this section specifies the CODE hierarchy; **the
> whole point of `00` §2.1 is that they are not the same tree.**

---

## §3 · VIEWS OF ONE ARTIFACT, GENERATED

**Views, and the artifact is generated rather than authored** — because three files nested under a new
top-level key would create a **fourth hand-maintained surface that can disagree with the three it
indexes**, which is a hierarchy in shape and not in meaning.

```
AUTHORED (three surfaces, each keeping its own owner and its own review)
   the module contracts        role · module · consumes · emits · owned state · resolver
                               + NEW: phase: (§2.2)   + NEW: grade: (§4)
   the key type registry       key type · payload shape · who emits and consumes it
   the descriptor registry     field · bounds · roster membership
        │
        ▼   ONE PARSER — the sole reader of all three, validating at export time
   one exporter                resolves every parent edge; RAISES on a dangling one
        │                      blocking --check round-trip
        ▼
   GENERATED composite         never hand-edited · _generated banner · schema_version
        │
        ▼   LEAF READER — RAISES on a non-member; never get(x, default)
   the descent a session and the port both use
```

> ⊕ **THE TRANSPORT IS INCUMBENT B'S AND IS ADOPTED RATHER THAN RE-DERIVED** (§1). Everything this
> document changes is **above** the transport, in §2's level set.

### §3.1 Total provenance — the one invariant the composite adds

> **Every leaf carries the `file:line` of the authored row it came from, and the exporter FAILS if any
> leaf does not.** The composite stores **no content of its own**; every row in it resolves to a row in
> one of the three authored surfaces.

`01_FORWARD_DOCTRINE.md` §4 is the rule this instantiates: an owner column must be *"grep-backed with
`file:line`, **never prose**, or it becomes one more unconditional authored claim."*

### §3.2 The round-trip, and when it may block

`--check` regenerates and diffs. **Two qualifications, both from the chain:**

- **Not blocking before ratification.** `01_FORWARD_DOCTRINE.md` §4: *"Do not wire proposal-tree
  exporters into blocking CI before ratification — that makes unratified material load-bearing."*
- **Commit nothing generated.** *"The self-test must regenerate, not read. A test that reads a
  committed artifact is exactly the test that passes on stale data and fails when its own generator
  runs."* **The composite is built in the check.**

---

## §4 · THE HOLES DO NOT WAIT — `grade:` PER ROW

**The head's contract surface is incomplete, and a descent over an incomplete surface centralises the
holes as much as the content.** The answer is not to wait; it is to make the hierarchy **display**
them.

Every row at every level carries `grade: ruled | measured | assumption | absent`, the vocabulary
`01_FORWARD_DOCTRINE.md` §3 specifies for constants — *"the sin was never that 1000 is wrong; it is
that a guess carried no grade."*

| grade | means | what a reader may do |
|---|---|---|
| `ruled` | a ruling or an in-chain adjudication row decides it; the citation is on the row | build on it |
| `measured` | an execution artifact establishes it; the command is on the row | build on it |
| `assumption` | the row exists, nothing backs it | **use it, cite it AS an assumption, never as measured** |
| `absent` | declared missing on purpose | **an authoring queue item with a name** |

**Three consequences:**

1. **A missing contract stops being a silence** and becomes `grade: absent` with a reason — a countable
   queue. The head's own list of specification debts (#351 §6.2: `judging_set_rule`, witness channels,
   the termination argument) **becomes rows rather than prose.**
2. **The port sees the grade beside the value**, which is the condition under which an incomplete
   surface can be worked incrementally instead of as one block.
3. **The polarity rule applies.** `01_FORWARD_DOCTRINE.md` §4: *"zero evidence maps to the verdict
   AGAINST the thing being measured."* **A row with no grade does not default to `assumption` — it
   fails the export.** A default grade is how an ungraded surface silently becomes a graded one.

---

## §5 · WHAT THIS BUYS, AND THE TWO CHECKS IT LICENSES

### §5.1 The context property, stated so it can be falsified

> **A session working on one module reads: its own row, the Key types that row names, and the fields
> those Key types carry. Nothing else.** No world model, no sibling subsystem, no loop source — because
> the row carries its own `doc:` pointer for when intent is needed and its `grade:` for whether the
> pointer is worth following.

**Deliberately modest**: it does not claim a session needs less judgement, only fewer **files**, and it
names which. **§7 step 4 is the executable form of the test.** The same descent is what the port
ingests — a port that can walk `role → module → key type → field` generates its manifest instead of
hand-transcribing it.

### §5.2 Two checks, and no others

1. **The exporter's own `--check` round-trip** (§3.2).
2. **A dangling-parent check *inside* the exporter** — every `role → module`, `module → key type`,
   `key type → field` edge resolves or the export fails. **Inside**, because a separate checker is a
   second parser.

**Explicitly not licensed:** a coverage dashboard, a freshness checker over the composite, a test that
the grades are honest, a report of how many rows are `absent`. **The `absent` count is readable by
looking.**

---

## §6 · THE BOUNDARY TEST — WHAT STAYS CODE, WHAT STAYS PROSE

A thing enters the hierarchy only if it passes all three of `01_FORWARD_DOCTRINE.md` §3's tests:
*(1) a total function from a small enumerable key domain to plain values, no control flow; (2) changing
it needs a design decision but no new mechanism; (3) validatable without executing it.* **The moment a
row wants an `if`, stop.**

| candidate | verdict |
|---|---|
| `phase:` on a module | **in** — six-member closed set |
| `consumes` / `emits` key types | **in** — a list of names |
| owned state | **in** — it is the `03_OWNERSHIP.md` row, restated where code reads it |
| `grade:` + citation | **in** — §4 |
| **a resolver's behaviour** | **OUT — stays code.** A resolver has control flow by definition |
| **`judging_set_rule`** | **OUT — it is unspecified** (#351 §6.2). **Configuring an unspecified thing invents it** |
| **rationale, ruling history, worked failures** | **OUT — stays prose**, beside the row it governs |
| **the write matrix** | **in, and it is the item with real work** — it is what `phase:` indexes into |

---

## §7 · WHAT WOULD MAKE THIS DONE

Nothing here runs. Four artifacts, in order, each stated so a reader can check it rather than believe
it:

1. **`phase:` on every module contract** — closed vocabulary, each citable against `04` §4's matrix.
   **Artifact:** a parse showing every module populated.
2. **`grade:` on every row that carries a value**, including the `absent` ones. **Artifact:** the
   per-grade counts, printed by the exporter.
3. **`--build` emits the composite and prints its leaf count and grade distribution; `--check`
   reproduces it byte-identically.** **Artifact:** both commands and their output, in the
   `MEASURED-BY:` block `01_FORWARD_DOCTRINE.md` §4 specifies.
4. **One descent, run:** pick a module, print its full subtree from the composite alone.
   **Artifact:** that output. ⚠ **This is the falsifier for §5.1 and the one step that cannot be
   satisfied by writing.** If the subtree is not enough to work the module, §2.1's level set is wrong.

---

## §8 · FALSIFIERS

| claim | what would prove it wrong |
|---|---|
| §2.2 · scale must not be a level | a module whose contract is genuinely different at two rungs in a way `Rung.kind` cannot express. `10` §5.2's *"one rung type"* is what makes this hard — **and if it is easy, the ladder is not holonic** |
| §2.1 · the six spine levels are the right set | a routine module task whose complete input is not `{row, key types, fields, doc pointer}` — §7 step 4 |
| §2.2 · `phase:` is the missing index | show a module's lawful write set is already derivable from `consumes`/`emits` without it |
| §3 · views beat a hand-authored parent | a parent edge that cannot be derived from the three authored surfaces. **If one exists it belongs on one of the three, not in the composite** |
| §3.1 · total provenance | one leaf in a built composite with no `file:line`. If it can be built without one, the invariant is decorative |
| §5.2 · two checks suffice | a defect class neither check catches **and that is load-bearing on the port** — the second clause is where most candidate guards die |
| §1 · these two are the only in-chain incumbents | a third specification of this descent anywhere in #337–#352 |

**Standing weaknesses.**

- **This document's contribution is the level set and the level/axis distinction — not the hierarchy
  and not its transport**, both of which are incumbent B's. B's own warning binds: *"Whichever is
  built, it should be built once."*
- **`grade:` is a display, not a fix.** The head's specification debts stay debts; they merely become
  countable. Authoring the missing contracts is the larger half and this does not do it.
- **The `phase:` proposal assumes the six-step vocabulary settles.** `04` §2 is explicit that the six
  steps are a refinement of a coarser tick. **Nothing in §2.2 depends on the count** — with a coarser
  vocabulary `phase:` takes those values instead and every claim survives.
- **No exporter was written and no composite was built.** Every claim about what the descent yields is
  argument; §7 step 4 is the only thing that would settle it.
