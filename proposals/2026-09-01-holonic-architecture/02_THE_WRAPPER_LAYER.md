# 02 · THE WRAPPER — the owner R-1 and R-2 do not have

## Status: **PROPOSED (2026-09-01). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.** Nothing here runs.
## Scope: **PR #337 → #352 only** (`00_ADJUDICATION.md` §0). Nothing ratified before #337 is authority.
## This is **M1** — narrowed by `00` §5's N-line test to **the emission side only.**

---

## §1 · WHAT THIS IS FOR, IN ONE PARAGRAPH

`01_THROUGHLINE.md`'s **R-1** and **R-2** are the container rules: *a rung reads only its own state and
messages addressed to it, may compute an aggregate over descendants on demand but never receive or
store a pushed one; a rung writes only its own state; upward influence is emitting an aggregate,
downward influence is emitting a refraction; no module reaches through another.* **They are stated once
and no later document names anything that enforces them.** The wrapper is that owner.

**And it is deliberately smaller than the first draft of this document made it.** `00` §5 ran the
head's own admission test (`01_THROUGHLINE.md` §6) and the N-line came back **partly false**: the
`Rung`'s ownership already prevents most cross-rung *reads*, because a rung owns `matter` and no social
aggregate, so there is usually nothing to reach through *to*.

> ### **WHAT SURVIVES THE TEST, AND THEREFORE THE WHOLE OF THIS DOCUMENT'S CLAIM:**
> **Nothing in the head stops a module EMITTING a Key whose target is not its parent or its own
> descendants.** That is R-2's *"no module reaches through another"* with no owner. **The wrapper earns
> its place on the emission side. It has no business on the ownership side.**

---

## §2 · THE ONE RULE

> ### **A KEY CROSSING A RUNG BOUNDARY IS EITHER AN AGGREGATE (UP, TO ITS PARENT) OR A REFRACTION (DOWN, TO ITS OWN DESCENDANTS). NOTHING ELSE CROSSES.**

Not a state write. Not a pushed value. Not a read reaching through. **This is R-2 restated as something
a wrapper can check**, and each clause is already in the head:

| clause | where it already is |
|---|---|
| the two legal directions | **R-2**, verbatim |
| no pushed aggregate | **R-1** — *"may **not receive** a pushed aggregate, and may **not store** one"* |
| a rung writes only its own state | **R-2**; `03_OWNERSHIP.md`'s six owners, one log, and **Nobody** |
| the up direction is filtered by a **named person** | **T5** — Petition → `carry` → DocketItem → sitting |
| the down direction **distorts in transit** and lands in the receiver's own view | **T6** — a Dispensation published as a `tell`, reaching a postless person through *their own* `opening_set` |

**T5 and T6 are why the rule is not merely bookkeeping.** The up-stroke is not a summation; it is a
person choosing what to carry, and paying for it. The down-stroke is not a broadcast; it is a `tell`
that degrades. **A wrapper that "aggregates up" by summing, or "distributes down" by delivering
faithfully, has deleted both throughlines while satisfying R-2's letter.**

---

## §3 · FOUR DUTIES

A wrapper is **one file per subsystem**, at the `SUBSYSTEM` level of `01_THE_CONTRACT_HIERARCHY.md`
§2.1's spine.

### D1 · It is the subsystem's only entry point, resolved by registry row

`09_THE_SEAM.md` §5: *"the engine names the **ROLE**; the registry names the **MODULE**; resolution
happens by string"*, and *"the kernel resolves every registered row **at boot**, not lazily at first
use. A missing provider is a startup failure with a name in it, not a `null` three seasons into a
campaign."*

**The anti-pattern is named in the same section:** loading modules **by bare name** off a path, *"which
gives those modules a **second identity**."* **[engine] Its GDScript form is `preload()` by a hardcoded
path from inside a resolver body — the same shape with none of the declaration. The manifest is the
seam; a path literal in a body is not.**

### D2 · It owns its subsystem's Key emissions

**Every Key leaving the subsystem passes through the wrapper**, so §2's rule has a fixed address to be
checked at, and the module contracts' `emits:` lists become verifiable against **one file**.

⚠ **This is the duty with a live failure mode and the head's audit already found it once.**
`00_AUDIT.md` **C-1** reports a write gate that *"validates, logs, returns `True` — **and mutates
nothing.** All state change is direct assignment beside it"*, so *"'enforced by construction' is
false."* **A wrapper that is *a* path rather than *the* path is exactly that gate.** The audit's own
remediation is the rule to build to: ***"Make the write gate apply the write, or make direct assignment
impossible."***

### D3 · It injects declared extensions, and the extension's TYPE is the bound

`09_THE_SEAM.md` §3 specifies the pattern and calls it the executing precedent for the whole seam:
*"one resolver, subsystem variation by **declared extension, injected by the wrapper**… **Whatever a
deferred subsystem needs that the general ladder does not give it, it declares — it does not fork.**"*
The extension is **demote-only**: it *"vetoes an Overwhelming and can do nothing else"*, and it is
*"passed by the subsystem's wrapper, **never resolved by the engine** — the engine does not know which
subsystems exist."*

> **The generalisation, and it is the whole safety argument: DESIGN THE TYPE FIRST, THEN THE HOOK.** A
> hook returning `bool` **cannot** promote a band, move a window, or re-derive the ladder — not by
> convention but because there is no signature for it. **If a variation needs a return type rich enough
> to do more, it does not belong in an extension**; it is an amendment to the one owner, *"made once,
> in that file — never a parallel enum in a subsystem"* (`09` §3).

### D4 · It is where §2's rule is applied — and it does not decide what crosses

**The wrapper checks direction and target. It never selects recipients.**

> ⚠ **THE FAILURE MODE, NAMED SO IT IS NOT BUILT.** A wrapper distributing a Key to three of its five
> modules **has selected**, and selection computed from a payload is an inference engine. The chain
> already paid for this: `00_AUDIT.md` **D-2** found 11 unreachable probes behind *"a 114-line regex
> router"*, and `01_FORWARD_DOCTRINE.md` §3's ruling is **"Don't route — declare"**: *"an inference
> engine reconstructing a fact **the case author knew at authoring time**."*
>
> **So which modules receive a Key type is a ROW in the descent (`01` §2.1's `module → key type`
> edge), never a computation in the wrapper.** The wrapper enforces R-2; the registry says who listens.

---

## §4 · FOUR NEVERS

| never | why | citation |
|---|---|---|
| **a wrapper never holds state** | it becomes a second owner of a value `03_OWNERSHIP.md` already assigns — that document's §1.3 gap 4 (*"two owners today… the read/write asymmetry hazard **by construction**"*) reproduced on purpose | `03` §1 |
| **a wrapper never decides** | *"No phase in which a container decides. Every decision has a person's id on it"* | `04_THE_SEASON_LOOP.md` §8; LAW 1 |
| **a wrapper never resolves** | *"a contest is `resolve` at a smaller scale, not a different function."* A wrapper that computes an outcome **is** the second resolver — the refusal `04` §7 calls *"the highest-value conventional cell in the entire shape"*, enforced *"by a person noticing"* | `09` §2; `04` §7 |
| **a wrapper never drives a clock** | per-container clocks delete the barrier structure, which is the only within-tick bound the design has, against a termination debt #351 §6.2 already reports as unbounded | `00_ADJUDICATION.md` §4.3 |

> **The fourth is the one that will be argued for**, because a battle or a hearing feels like it should
> own its own time. **It already does, and it needs no clock:** `09` §1 — a contest *"subdivides the
> tick and runs the same steps over a smaller person set **on a shorter clock**"*, **inside** RESOLVE,
> inside the global tick, bounded by a `max_depth` that is *"caller-supplied, with **NO DEFAULT**"*
> because *"a default is a number somebody made up, and it will be cited later as though it were
> measured"* — and because [engine] exceeding GDScript recursion depth is *"a **CRASH**, not a catchable
> error."*

---

## §5 · WHERE IT LIVES IN GODOT

```
res://core/
  loop/            season_driver.gd + one file per step        # the four global barriers
  seam/
    contest_resolver.gd                                        # the one nesting form (09_THE_SEAM.md)
    wrappers/<subsystem>_wrapper.gd                            # D1-D4, one per subsystem
  manifest/roles.gd                                            # role -> provider, resolved AT BOOT
```

- **The autoload rule does the containment for free.** `10_GODOT_4_6.md` §3: *"THE `[autoload]` TABLE
  CONTAINS NO SIMULATION STATE AND NO SIMULATION SERVICE… `World` is constructed by the driver and
  passed by parameter."* **A wrapper is therefore not reachable by a global name, and neither is the
  state it would be tempted to hold.** The honest limit is stated there and not softened here: *"the
  guarantee is **unreachable-by-name**, not **unwritable**."*
- **`class_name` is flat and global** (`10` §5.2), so wrappers are **files in a directory, not a type
  tree**. There is no `Wrapper` base to subclass and no `Subsystem.Wrapper` namespace to reach for —
  the same ruling as the rung ladder, for the same reason.
- **No version pressure.** `10` §1.1 measures the shape's honest floor at **≥ 4.4** (typed
  `Dictionary`), with `@abstract` (4.5) buying one convenience whose fallback — a base-body error plus
  a typed error result — *"is needed anyway, since [engine] GDScript has no exceptions."* **The
  wrapper layer adds nothing above that**, and the parallelism it enables (`WorkerThreadPool.add_group_task`
  over DELIBERATE) is **Godot 4.0**.

---

## §6 · WHAT WOULD MAKE THIS DONE

Nothing here runs. Three artifacts, in order:

1. **The role manifest resolves at boot and fails loudly.** **Artifact:** a run with one row's provider
   misspelled, producing a **startup** failure that names the row — not a `null` later. This is `09` §5's
   own claim, executed.
2. **One subsystem's emissions pass through its wrapper, and §2's rule is checked there.**
   **Artifact:** the emitted-Key-type set read from the wrapper alone, diffed against that subsystem's
   `emits:` rows, **plus one negative case** — a Key aimed two rungs away, refused, with the refusal in
   the output. ⚠ **The negative case is the whole test**; without it this is D2 repeating C-1's
   "validates, logs, mutates nothing."
3. **The clause-2 grep, as a standing artifact.** The resolver grepped for a Query aggregating a
   per-person tally across holders, with the transcript. **This is the falsifier #351 asks for and
   nobody has run:** *"if one is needed for a case the ratchet was admitted for, clause 2 is too
   strong; if one is possible, it is too weak."*

⚠ **Step 2's negative case is the only one that cannot be satisfied by writing. Run it first.**

---

## §7 · FALSIFIERS

| claim | what would prove it wrong |
|---|---|
| §1 · the N-line survives on the emission side | show the head already stops a module emitting past its parent. **If it does, this document is void** and should be deleted rather than trimmed |
| §3 · D2 · one wrapper makes emissions checkable | a subsystem whose emissions cannot pass through one file **without that file interpreting a payload** — at which point it is D4's forbidden router. **This is the real risk, not a hypothetical** |
| §2 · nothing but aggregates and refractions crosses | a case in the head needing a third kind of boundary crossing. **T5 and T6 are the two the throughlines name; a third would mean the throughline set is incomplete** |
| §3 · D3 · the type is the bound | a subsystem variation that cannot be expressed as a declared extension with a bounding type **and** is not an amendment to the one owner |
| §4 · a wrapper never needs a clock | a subsystem behaviour not expressible as a nested `contest` at RESOLVE with a caller-supplied depth cap. `09` §1's *"a battle, a hearing, an examination committee and two brothers arguing over a barn are the same call"* is the claim under test |
| §5 · no version pressure | one engine feature the wrapper layer needs above the measured **≥ 4.4** floor |

**Standing weaknesses.**

- **The wrapper is one object justified by two sentences in a laws document.** R-1 and R-2 are stated
  once, in `01_THROUGHLINE.md`, and **no later document in the chain elaborates them** — so this
  document is building on the head's least-developed passage, not its most.
- **The downward half is under-specified and this does not fix it.** T6 says a Dispensation *"distorts
  in transit"*; **nothing specifies the distortion.** §2 gives the direction rule and stops, and a
  session that finds itself deciding *how much* a refraction distorts is past the edge of the chain.
- **Nothing here was executed.** Every claim about what a wrapper costs is argument from cited
  constraints — weaker than the instrument #351 built, and #352 showed even that instrument's case
  layer never ran.
