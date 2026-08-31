# 01 · THE THROUGHLINE — a person is the unit, and everything else is bookkeeping about persons

## Status: PROPOSED (2026-08-31). **HELD BACK. Nothing here ratifies on merge.**
## Layer: **L1 — the laws.** Read `00_INDEX.md` (L0) first. Every later document is an elaboration of
## this one, and any later row that contradicts a law here is a defect in the later row.

---

## §0 · THE POSTURE OF THIS SUITE, STATED BEFORE ANYTHING ELSE

> **This is the IDEAL code shape. It is not bound to precedent, to any prior proposal, to any
> `## Status: RATIFIED` line, or to the code that happens to run today. It takes only what is best.**

That instruction cuts in a specific direction, and the direction is worth stating precisely, because
the opposite failure is available and this repository has recorded it more than once.

| what "not bound to precedent" DOES mean | what it does NOT mean |
|---|---|
| a shipped answer is adopted **because it is the best answer**, never because it shipped | that the running tree's answers are wrong by default |
| a coined word with a weak justification is dropped (§2.7 of `02` drops two) | that vocabulary churns for its own sake |
| a stat-bag with 31 writers is replaced rather than wrapped | that the replacement may be asserted without a control |
| a design's own confession of a hole is taken at face value and the hole is closed | that a hole may be closed by declaring it closed |

**And one thing does not become optional under it.** A claim about the world can be wrong; a claim about
**this repository** can be checked. Every `path:line` in this suite was opened during the pass that
wrote it, and the register of those traces is `TRACE_REGISTER.md`. Where the ideal shape departs from
what the tree does, **the departure is stated as a departure with its cost priced**, because a design
that does not know what it is walking away from is not choosing — it is guessing.

**Where the running tree already holds the best answer, this suite says so and adopts it.** There are
six such places and they are named in `15_ADJUDICATIONS.md`: the event log's invariant set, the
single-owner degree ladder, role-resolution-by-string, per-operation RNG substreams, the
required-with-no-default termination caps, and the exporter round-trip. **None is adopted for being
precedent. Each is adopted because nothing better was proposed and the reasoning behind it is sound.**

---

## §1 · THE ONE SENTENCE

> **Every action in this game is performed by a person, every person is wrong about something, and
> everything a player sees is one person's view of what other persons did.**

That is the whole architecture. The rest of this suite is what falls out of refusing to break it.

**The nine throughlines this shape answers to** — and where each stops being an aspiration and becomes
structure:

| | throughline | where it becomes structural |
|---|---|---|
| **T1** | all actions are performed by characters | `resolve` has no faction parameter; a faction has no verbs (`02` §3.1) |
| **T2** | characters have memories, feelings and commitments that change | **two separate layers, and conflating them is the suite's most dangerous collision:** the claim ledger is **what they hold TRUE**; `convictions` and `beliefs` are **what they hold RIGHT** (`02` §5.5). Evidence moves the first; argument and consequence move the second. Nothing social moves on a clock |
| **T3** | memories are fallible; multiple perspectives on one event | `witness(Person, Event)` is per-person **and there is no collection signature to call** |
| **T4** | no one is omniscient | `choose` has no `World` parameter, and every resolver-side Query takes `World` first, so calling one from inside `choose` **fails at the call site** |
| **T5** | demands aggregate UPWARD and are filtered at a rung | Petition -> `carry` -> DocketItem -> sitting, filtered by a **named person** who pays for the filtering |
| **T6** | large actions ripple DOWNWARD | a Dispensation is published as a `tell`, distorts in transit, and reaches a postless person through **their own** `opening_set` |
| **T7** | events, clocks and gates are what gets debated | a `Date` is the spine; a sitting is a Date that has fired; the argument layer resolves by **named fault**, not by a persuasion threshold |
| **T8** | the world always churns; the player is not necessary | `05_WORLD_CHURN.md` — `wear`, the actorless event channel, vacancy, and the Partition's second row |
| **T9** | field investigation is first-class | six acts, every one available to any person; **eligibility never consults office** |

> ⚠ **TWO DIFFERENTLY-SCOPED THROUGHLINE SETS SHARE ONE NAME IN THIS REPOSITORY** [LANE B C13]. The
> nine above are the set this shape answers to. Where a document cites *throughlines* meaning the older
> corpus-wide set, it is talking about something else. **Say which set, every time.**

---

## §2 · THE FOUR LAWS

Everything in this suite is derivable from four laws. Each is stated with what it forbids, how it is
enforced, and — honestly — whether the enforcement is **mechanical** or **conventional**.

### LAW 1 — THE PERSON IS THE ONLY ACTOR

> **Nothing acts except a person. Not a faction, not a settlement, not an institution, not a clock,
> not the design.** A cohort acts because a cohort **is** a person at weight > 1. An office acts
> because the persons it employs act. A faction acts because its members act.

| forbidden | enforcement |
|---|---|
| a faction verb | **mechanical** — `resolve` takes `(Act[], World)` and an Act's `actor` field is a Person id |
| a settlement or institution as a speaker | **mechanical** — a Petition addresses a **Venue**, whose door names a **convener**, who is a person |
| a threshold firing an outcome with nobody deciding | **mechanical in CALENDAR** — a band edge changes an **option set**, never a roll term and never an outcome |
| an authored per-person opportunity or quest object | **convention**, and it is the one this shape watches hardest |

**The consequence that makes this a game rather than a rule.** *"No leader, no faction action"* is
Jordan's ruling, and under it **a campaign with no people in it performs zero faction actions.** That is
not a bug to route around — it is Law 1 arriving at its own conclusion, and it is why the person loader
is the first thing `13_EXECUTION.md` builds.

**And the second clause is the interesting one.** *The leader's identity changes which choice is made.*
This shape implements that as **an option-set change and a pool substitution — never as a modifier on a
roll.** The arithmetic is in `02` §2.3 and the reason is that a flat shift of size `X` is worth
`X / (0.800 · sqrt(Pool))`, so it helps a weak pool more than a strong one, **backwards from every
intent anyone has when adding one.**

### LAW 2 — NOBODY IS OMNISCIENT, AND THE SIGNATURES ARE HOW

```
choose  : (Person, View, Sensation) -> Act        # NO World, ever
resolve : (Act[], World)            -> Event[]    # NO Person
witness : (Person, Event)           -> Claim[]    # per person; a collection is not spellable
```

**They work by what they omit.** `choose` has no `World` — not masked, not read-only, not behind an
accessor. `resolve` has no `Person`, so the resolver cannot acquire a per-actor special case. `witness`
takes the person first, and **no signature accepts a collection of persons and one event.**

**`View` is a distinct type from `World`**, with no coercion, no shared supertype, and no field of a
`View` holding a `World`. **If a `View` can be built from a `World` by masking, someone will eventually
mask nothing.**

**`View` is built, not filtered**, and the distinction is the design: a View is smaller than the truth
the way an **empty room** is smaller than a furnished one — **not blurrier**. Absence of a claim produces
**absence**, never a widened interval, because a widened interval is uncertainty and this game needs
**ignorance**.

> ⚠ **AND THE HONEST STATEMENT OF STRENGTH, WHICH THIS SUITE WILL NOT OVERSTATE.**
>
> In the Python oracle these omissions are **mechanical**: the parameter is absent, and a resolver-side
> Query called from inside `choose` fails for want of an argument.
>
> **[engine] In GDScript they are not.** There is no module system, no visibility modifier, and no way
> to scope an identifier out of a function body. An autoload is reachable from any script; `class_name`
> statics and `load()` by string are two more doors. **So omitting `World` does not make world access
> unwritable — it makes it unwritten.**
>
> **The port's own skeleton is the proof rather than the hypothesis**: its resolver modules reach a
> global state singleton and an event bus from inside their bodies.
>
> **The guarantee therefore moves from *unwritable* to *unreachable-by-name*** — human-checkable on one
> screen of project settings, plus one token-scan test. **A false claim of enforcement is worse than
> none, because it stops the next reader from checking.**

### LAW 3 — EVERY AGGREGATE IS A FUNCTION, NEVER A FIELD

> **Nobody owns an aggregate.** No stored norm, density, unrest, reputation, legitimacy, cohesion,
> footprint, presence or leadership. Every one is a `Query`: computed on demand, from primary state,
> stored nowhere.

**This is not a style preference.** Stored aggregates are how a design acquires **dead state that reads
as mechanism** — a value initialised once, never written, and cited for seasons as though it meant
something. If the aggregate is a function it cannot go stale, and it cannot be initialised and then
forgotten, **because there is nothing to initialise.**

**Two module rules follow, and they are the whole of the discipline:**

- **R-1.** A rung may read its own state and any message addressed to it. It may **not** read a
  sibling's state or a descendant's state directly. It **may COMPUTE an aggregate over its descendants
  ON DEMAND**; it may **not receive a pushed aggregate**, and it may **not store one.**
- **R-2.** A rung writes only its own state. Upward influence is **emitting an aggregate**; downward
  influence is **emitting a refraction**. **No module reaches through another.**

**A cross-rung read is the single easiest way to destroy T5 and T6**, because once the realm can read a
person directly there is no reason for the ladder to exist and every intermediate rung quietly becomes
decoration.

> ⊕ **AND THE ONE CONCESSION, MADE EXPLICITLY RATHER THAN DISCOVERED AS A RACE.**
>
> **A Query MAY be cached. The cache is built AT A BARRIER, is READ-ONLY until the next barrier, and is
> DISCARDED there. Nothing inside a parallel map builds one.**
>
> Without this, six operations are O(N²) and the population ceiling is set by a scan rather than by
> anything the designer chose. With it, "compute-on-demand" holds at **barrier granularity**, which
> stores nothing that can go stale because it does not survive the barrier.

### LAW 4 — EVERY STATE CHANGE IS PARTITIONED BY ITS SUBJECT

> **A change whose subject is peninsular human society — polities, institutions, offices, occupations,
> religion, settlements, marriage — is driven by a character's choice, ALWAYS. A change whose subject is
> anything else — weather, the non-peninsular, tears in the substrate — is an event acting on the world.
> Creation and destruction included.**

**And the membership test is a static schema column, not a judgment.** `social: bool` on the
`(record-kind, field)` pair, declared in the exported schema and read by the resolver — **and the rule
is ASYMMETRIC:**

```
social: true   =>  ACT-DRIVEN ONLY.  An Event may never write this row.
social: false  =>  EITHER DRIVER.    An Event may write it, and so may an act.
```

**The row does not say who may act. It says what an EVENT may not touch.** Stated as a biconditional it
is simply false: a restoration **act** writes `(Site, condition)`, a `social: false` row, every season —
**`wear` and a tending act land on the same field by design**, and that is the flux model.

**The worked case is the law's own proof:** `(Site, condition)` is `false`, so a plague may move it;
`(Rung, exists)` is `true`, so **a plague may kill every body in a village and may not destroy the
village.** The village empties and still legally exists **until an office strikes it from the roll.**

> ⚠ **AND THE COLUMN IS KEYED ON `(record-kind, field)` FOR A REASON.** Stated over *subjects*, the
> Partition concedes a mixed class — *a plague is biology but it empties institutions* — and **"both"
> is not a partition.** Keyed on the field, a plague is not one change with a disputable subject but
> **several, each writing a different field**, and each is answered separately. **The mixed class
> dissolves because there was never one change to classify.** (`02` §5.1.)

**The half most easily lost, restated:** an event reaches society **only through what people choose to
do about it.** The plague does not depose the mayor. It kills people, and then people act.

---

## §3 · THE PLAYER IS A PERSON, AND THAT IS THE WHOLE OF THE PLAYER MODEL

> **The player supplies one Act, for one Person, through the same `choose` every NPC goes through.
> There is no player-only mechanism anywhere in this shape, and no NPC-only mechanism either.**

| | what the player has | what an NPC has |
|---|---|---|
| the function | `choose(person, view, sensation) -> Act` | the same function |
| the world | none | none |
| the budget | one act per season | one act per season |
| the attention surface | a **cast** and a **rank** over candidates | a **ledger** and a **rank** over claims — *the same mechanism at a different fidelity* (`02` §5.4) |
| the advantage | **deliberation time, and nothing else** | — |

**Fidelity is a camera, never a formula.** `played`, `witnessed` and `auto` control **who is asked to
choose**, never **how the outcome is computed.** Identical resolver, identical rolls, identical seeds.

> **A code path that computes an outcome without running the same resolver is a second resolver
> whatever it is called, and it will diverge.** The only surveyed franchise with two resolution paths is
> also the only one with a twenty-year unsolved divergence between them, and the diagnosis is that a
> played path is a **process** while a fast path is a **formula** — two different kinds of thing cannot
> be calibrated to agree, only made to agree on average.
>
> **And this is the refusal that only discipline enforces** [LANE F §E]. Nothing in the type system
> stops someone adding a fast path. It is the highest-value conventional cell in the whole shape, and
> the correct response to that is to say so here rather than to claim a guarantee that does not exist.

### §3.1 The player without a post is the design's real test

**A person holding no office can act, petition, investigate and receive an opportunity.** Office changes
whether a decision **binds others** — never whether you may act.

This is not a nicety. It is **S-DOWN**, one half of Jordan's smoothness criterion, and it has a
falsifier that runs: **T3** in `12_TESTS.md`. It is also the criterion the running tree fails today, for
a reason that is not subtle — **there are no people in it at all.**

**What an ordinary person holds that is scarce**, and it is not skill:
a **channel** (a tie, a knot, an ear), a **custody** (a register, a key, a roll), a **gate** (a door
somebody must pass), or a **unique root** (a thing only they witnessed). Every character who holds one
of those plays richly. Every character who holds none is thin — **and that correlation, not rank and not
office, is what predicts whether a season is worth playing.**

---

## §4 · WHAT THIS SHAPE REFUSES, AND WHAT COVERS THE REFUSAL

A refusal without a replacement is an amputation. Each row names what does the job instead.

| refused | because | what does the job |
|---|---|---|
| a `World` parameter on any decision function | Law 2 collapses; the whole epistemic layer becomes decoration | `View` + `Sensation` |
| a `view_of(world, person)` that masks rather than assembles | someone eventually masks nothing | `assemble(person, question)` over the ledger |
| any function taking `[Person]` and one `Event` | consensus broadcast; divergent perspective dies | `witness(person, event)`, called per person |
| a cohort deposit carrying a **value** rather than a **distribution** | consensus broadcast **laundered through the cohort type** — one sign into hundreds of people, and the type checker sees a single legal write | a construal distribution; an individuating member **draws** |
| a pushed aggregate, or a field one lands in | a push needs a landing site, and the landing site is stored aggregate state | R-1: compute on demand |
| a stored aggregate, norm, density, unrest or reputation field | dead state that reads as mechanism | `Query` |
| a knowledge value stored on the thing known | knowledge with no knower cannot be planted or refuted | the per-person ledger |
| a second resolver, an auto-resolve formula, a fast path | guaranteed divergence, unsolved in the genre for twenty years | one `resolve`, fidelity as a camera |
| a `tier`, `level` or `scale` field on a faction | growth becomes discontinuous | scale **derived** as a presence/density/footprint profile |
| a flat additive modifier from a person onto a roll | worth `X / (0.800 · sqrt(Pool))` — **helps weak pools more, backwards** | option-set change + pool substitution |
| a personal effect on a group that is not a **fraction** of that group | the only concrete anti-leverage rule the precedent corpus supplies | fractional effects |
| a scheduled recovery tick on standing | converts a consequence system into a treadmill | nothing social moves except by an act |
| a per-entity branch anywhere in the resolver | scripting drift: the exception becomes the mechanism | the resolver branches on **mode**, never on kind and never on a name |
| an authored per-person opportunity or quest object | a churning world turns back into content | `opening_set` recomputed from need + capability + the terms they hold a claim of |

> ⊕ **ONE NOTE ON THIS ROW'S CONSTANT — AND AN EARLIER DRAFT OF THIS NOTE WAS WRONG ABOUT WHAT KIND OF
> ERROR IT IS.** The corpus prices flat shifts at `X / (0.671 · sqrt(Pool))`; the executing owner has
> `sigma = 0.800`. **This is a MODEL DIVERGENCE, not an arithmetic error.** The design line **declares
> its own die** — no botch face, `mu = 0.5`, `sigma ≈ 0.671` — and derives that constant correctly from
> it. The executing die has a botch face (face 1 scores **−1**), `mu = 0.40`, `sigma = 0.800`. **Both
> constants are exact for their own die.**
>
> **So `0.671` is not "wrong wherever it is quoted", and editing it to `0.800` while leaving `mu = 0.5`
> would break the document it is edited in.** `sigma` and `mu` come from one die: **you change the die
> or you change nothing.** This shape adopts the **executing** die, and `15_ADJUDICATIONS.md` R-18
> declares that as a departure and prices it.
>
> **The rule is untouched either way** — a flat shift is worth more to a small pool than a large one
> for any `sigma > 0`.

---

## §5 · THE THREE THINGS THIS SHAPE IS FOR

Stated so that a later reader can tell whether a proposed addition belongs.

1. **THE SEASON LOOP.** One tick, six steps, four barriers, four write classes, and a determinism
   story that survives being run in parallel. `04_THE_SEASON_LOOP.md`.
2. **WORLD CHURN.** What happens with no player and no actor: `wear`, the actorless event channel,
   vacancy, decay of memory, and the one confirmed hole this suite closes with zero new objects.
   `05_WORLD_CHURN.md`.
3. **EMERGENT NARRATIVE.** How a story arises with nobody authoring one: candidates, salience, arcs as
   **provenance chains you can walk**, ambition as a derived progress read, and the refusal of a quest
   object. `06_EMERGENT_NARRATIVE.md`.

**And one thing this shape deliberately says almost nothing about.** Personal combat, social contest and
mass battle are **out of scope as systems.** They appear here at exactly one place — `09_THE_SEAM.md` —
which specifies **how a contest plugs into the season loop and nothing about what happens inside one.**
That is a scope decision, not an oversight, and it is why `09` is four pages rather than forty.

---

## §6 · THE TEST TO APPLY TO ANY PROPOSED ADDITION

Before an object, field, verb or step enters this shape, it answers four questions **in this order**.

1. **N — name the emergent possibility lost if this is cut.** Not "it would be useful"; name the thing
   a player could no longer do or the story that could no longer happen. **An object that cannot name
   one is surplus and is cut here rather than shipped.**
2. **Is the N-line FALSE?** — does the named possibility **survive the cut**, because something already
   ruled in provides it? **This is the highest-value check available, and it fired six times during
   this pass** (`02` §9.1). Every one of the six was proposed by a competent pass with a plausible
   argument, and in every one the store's job was already being done.
3. **E as a RATIO, never a fourth averaged axis.** Distil as far as possible **without losing** the
   possibilities N named or the choices R needs. **An audit that scores four axes and averages them
   rates an amputated design as elegant.**
4. **R at seats a player can occupy.** A structurally dominant option is a design failure — check the
   **shape** of gain against the **shape** of cost over time; decaying gain against compounding cost is
   dominance. **But apply it only where a player can sit.** An act that dominates an NPC's menu is
   **characterisation**, not a defect: a zealot *should* accumulate relentlessly without deliberating,
   and the design reproducing that from his stance table rather than from a script is a success.
5. **S is T5 and T6 restated, and it is not a stylistic judgment.** **S-UP:** can a demand travel up the
   ladder and be **filtered by a named person at a rung**? **S-DOWN:** can an opportunity travel down and
   reach a person **who holds no post**?

**And one meta-rule, which is the one that keeps the object count honest: a fix that ADDS a system has
failed.** The standard to hold every proposal to is the best repair this corpus produced — **three
edits, two of them deletions, and the vocabulary got shorter.**
