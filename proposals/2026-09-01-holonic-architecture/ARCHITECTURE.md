# THE SEASON LOOP — A HOLONIC ARCHITECTURE, AND THE GUIDE TO BUILDING IT IN GODOT

## Status: **PROPOSED (2026-09-01). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Under `CLAUDE.md` §0.05 this document is **REFERENCE, never mechanism.** Under §0.2 **nothing in it
## runs.** Part X says what would make each claim done and which steps cannot be satisfied by writing.

---

# PART 0 · HOW TO READ THIS

## §0.1 · Scope — the rule that decides what counts as evidence

**The only admissible sources are the design chain PR #337 → #352.** The head is
`proposals/2026-08-31-shape-tracer/04_UNIFIED_SHAPE.md` (#351). No file under `engine/`, no subsystem
`sim/`, and **no decision ratified before #337** is authority — not as support, not as precedent, not
as an incumbent to defer to. We are building the season loop's logic **from scratch** off that chain.

**Three qualifications, because the first revision of this document applied the rule inconsistently
and was caught doing it.**

1. **A pre-#337 document may be the SUBJECT of an in-chain claim, never the REASON one is correct.**
   Where an in-chain document rests a claim on older material, the claim travels as **that document's
   own proposal, at its own strength.**
2. **The chain's own execution-grounded adoptions travel with it.** The head's log invariants, the
   exporter round-trip pattern and role-resolution-by-string are each argued in-chain *and* grounded
   partly on what already runs. **Cutting the second half does not delete the first**, and the first
   revision pretended it cut cleanly in one place while relying on it in three others. Named here so
   the inconsistency is not repeated: §19.4, §41.3, §43.
3. **`proposals/2026-08-31-pr350-archive-recovery/02_SCENE_BUDGET_RULING.md` IS IN CHAIN.** It is part
   of #351 and it carries a Jordan ruling this document treats as binding. See §0.2 finding 5.

## §0.2 · What this revision retracts

Four read-only adversarial lanes ran against the first revision. **Their corrections were judged as a
set rather than applied one by one**, and the set changed the document's shape rather than its
details. Retractions are recorded, not deleted, because the correction record is what makes the rest
readable.

| # | the first revision claimed | verdict | lanes |
|---|---|---|---|
| **1** | **The missing object is a WRAPPER** that owns R-1/R-2 and checks that every Key crossing a rung boundary is an aggregate (up) or a refraction (down) | ⛔ **RETRACTED IN FULL.** The head has **no targeted module emission to check.** `Event` carries no target and no actor; up is a person's `carry` act, down is a person's `tell` act. The head's own adversarial pass: *"the only transport the suite defines **is** a chain of `tell` acts… there is no non-act news transport anywhere in the shape."* The rule was stated over a field that does not exist | B, C, D — **independently** |
| **2** | The rule's direction model | ⛔ **RETRACTED.** The head explicitly refuses it: a Dispensation *"travels by being noticed, **not down a chain of posts**"* and *"**scope enumerates EXECUTORS, not places**"*; a cluster's venue `container` **may be NONE**; Offices may have `rung? = null` — *"A Dicastery, a chivalric order and a trans-settlement guild have no containment node"* | B, C |
| **3** | **Two of six steps** partition per container (MATTER, DELIBERATE) | ⛔ **RETRACTED.** Two different tests were applied to two groups of steps. The honest frame is **per-owner**, and under it every step's *body* partitions except two. §31 | B, C |
| **4** | Per-container clocks delete the only within-tick bound (the four barriers) | ⚠ **RE-GROUNDED.** The conclusion stands; the ground was wrong and self-contradictory — §4.3 said barriers bound within-tick propagation while §7 said *"a spiral inside one tick is still unbounded."* The head **already permits within-tick reaction** (a nested contest re-runs DELIBERATE inside RESOLVE) and bounds it by **`max_depth`, not by barriers.** §40 | C |
| **5** | The act budget is *"the head's own unpriced reversal… Jordan's call, not mine"* | ⛔ **RETRACTED — it is RULED, in chain.** `02_SCENE_BUDGET_RULING.md` (#351): *"**THE ACT BUDGET IS ~5, NOT 1.** Verbatim: 'please note for the ideal proposal that i expect a character to get ~5 playable scenes per season, which may mean that they get ~5 actions.'"* **#351 §4.2 and #352 §6 both missed this file too.** What is genuinely open is narrower: whether a scene equals an act. §26.3 | A |
| **6** | The census holds **24** items, 20 unverified | ⛔ **CORRECTED to 27 and 23.** The document enumerated 27 and totalled 24 | A |
| **7** | Jordan's twelve trajectories: *"eleven of twelve work"* | ⛔ **RETRACTED — the source says FIVE.** *"Recomputed rather than adjusted: **FIVE OF TWELVE WORK TODAY**"* | A |
| **8** | The spine is a strict six-level tree | ⚠ **CORRECTED to four levels.** ROLE is engine-owned, and a KEY TYPE has many consuming modules — both are indices, not children. §41 | B |
| **9** | `phase:` is a required single value, and the count of steps does not matter | ⚠ **CORRECTED.** The matrix writes `Date` at CALENDAR **and** RESOLVE, so `phase:` must be a **set**; and one of its three checks is unaskable under a coarser vocabulary. Its N-line is also weaker than claimed — the head already makes the write check mechanical **per write site** | B, C |
| **10** | Structural-edge aggregation cannot rebuild a ratchet | ⚠ **NEEDS A THIRD CLAUSE.** Ended Tenures persist as *"historical claim subjects"*, so a count over live **and ended** edges is monotone. §22.4 | B |
| **11** | R-1/R-2 *"never appear again"* | ⚠ **CORRECTED.** R-1 recurs and does work — CALENDAR's convening predicate may read *"an R-1 compute-on-demand aggregate over its descendants"*. **R-2 does not recur.** The *no owner* claim survives; the sentence did not | A, B, C |
| **12** | Census item 16 (the twelve argument faults) was dropped | ⛔ **STRUCK.** Declared out of scope by a stated narrowing, not silently lost. A declared scoping is not a drop | D |
| **13** | **Petition spray is reopened at ~5 and must be re-answered by cost** | ⛔ **RETRACTED — RULED ALLOWABLE.** *"if a character wants to spend their entire season meeting with people to petition, let them."* **No cap, no dedup, no required cost gate**; the budget is the whole of the pricing, and spending it all on petitions **is** the triage the budget exists to create. §26.3 | Jordan, 2026-09-01 |
| **14** | *(gap — nothing said about inventing values a build needs)* | ➕ **ADDED.** The chain's own audit ranked *"declare the invented constants harness fixtures; run a 3-point sensitivity sweep"* as a remediation and this document did not carry it. **§42.2.1** — inject, grade, sweep, and **a verdict that flips across the sweep is itself a finding** | audit §6 item 9 |

> ### **WHAT SURVIVED, AND IT IS THE THESIS**
> **The season loop in the head is already holonic. It never uses the word.** R-1, R-2, T5 and T6
> are the container rules; `Rung` is the container, one type at eight scales; `contain` is an edge.
> **What is missing is not a wrapper. It is the `Event` record** — the object every other missing
> piece is stated over. §19.

## §0.3 · How to use this as a coding guide

Read **Parts I–II before writing a line.** Part I is why the shape is the shape; Part II is every
type you may declare. Part III is the loop you implement. Part IV is how scale works and is the part
most likely to be got wrong by analogy with engines you have used before. Part VI is the Godot
specifics.

**Three reading rules that will save rework:**

- **A refusal in this document is load-bearing.** Where it says *never*, the alternative was tried
  in the chain and named as a defect. Part VIII collects them.
- **Where something is unspecified, this document says so and does not invent it.** An `UNSPECIFIED`
  marker is a design decision someone owes, not a gap to fill at the keyboard. Part IX collects them.
- **`[engine]` marks a claim about published Godot behaviour**, not about this design.

## §0.4 · Vocabulary — every term, defined once

Terms are ordinary words wherever an ordinary word exists (`CLAUDE.md` §4). Coinages are marked ⊕.

| term | definition |
|---|---|
| **carrier** | an identity-bearing, mutable object. There are five: `Person`, `Rung`, `Office`, `Site`, `Record` |
| **rung** ⊕ | a container in the containment ladder. One type, eight `kind`s. Named `Rung` because [engine] `Node` and `Container` are both Godot built-ins and `class_name` collides |
| **holon** | a thing that is at once a whole and a part. Every `Rung` is one |
| **tenure** | the one edge type. Seven kinds. Carries `since`, optional `until` |
| **act** | what a person does. Produced by `choose`, consumed by `resolve` |
| **event** | what happened. Produced by `resolve` and by MATTER, appended to the log, witnessed |
| **claim** | what one person holds true. Deposited into that person's own ledger at WITNESS |
| **query** | a function over state. **Never stored.** Resolver-side takes `World` first; person-side takes the asker |
| **aggregate** | any value derived over more than one holder. Owned by **Nobody** |
| **ratchet** | a monotone counter. Legal only per `(Person, axis)` on a closed registry |
| **refraction** ⊕ | the downward distortion of an influence as it travels. ⚠ The head uses this word two ways — §37.4 |
| **barrier** | a global synchronisation point in the loop. There are four |
| **step** | one of the six named phases of a season |
| **write class** | which of `CALENDAR · MATTER · ACTS · INTERIOR` a write belongs to. **A write class is not a step** |
| **the Partition** | the `social: bool` column on `(record-kind, field)` that decides whether only an act may write it |
| **seam** | the one place a deferred subsystem attaches: RESOLVE, via `contest` |
| **descent** | the contract hierarchy a reader walks to find one module's I/O. Part V |

---

# PART I · THE ARCHITECTURE FROM THE TOP

## §1 · The one sentence

> **Every action in this game is performed by a person, every person is wrong about something, and
> everything a player sees is one person's view of what other persons did.**

**That is the whole architecture.** Everything below is what falls out of refusing to break it. When
a design question has no obvious answer, return here: the answer is almost always the one that keeps
a named person as the author of the change and keeps somebody able to be wrong about it.

## §2 · The nine throughlines, and where each becomes structure

A throughline is an intention. It is worth nothing until it is a signature, a table or a refusal.
This column is what makes each one real.

| | throughline | where it stops being an aspiration |
|---|---|---|
| **T1** | all actions are performed by characters | `resolve` has **no faction parameter**; a faction has no verbs |
| **T2** | characters have memories, feelings and commitments that change | **two layers, and conflating them is the most dangerous collision in the design**: the claim ledger is what they hold **TRUE**; convictions and beliefs are what they hold **RIGHT**. Evidence moves the first; argument and consequence move the second. **Nothing social moves on a clock** |
| **T3** | memories are fallible; multiple perspectives on one event | `witness(Person, Event)` is per-person **and there is no collection signature to call** |
| **T4** | no one is omniscient | `choose` has **no `World` parameter**, and every resolver-side Query takes `World` first — so calling one from inside `choose` **fails at the call site** |
| **T5** | demands aggregate **UPWARD** and are filtered at a rung | Petition → `carry` → DocketItem → sitting, **filtered by a named person who pays for the filtering** |
| **T6** | large actions ripple **DOWNWARD** | a Dispensation is published as a `tell`, **distorts in transit**, and reaches a postless person through **their own** `opening_set` |
| **T7** | events, clocks and gates are what gets debated | a `Date` is the spine; a sitting is a Date that has fired; the argument layer resolves by **named fault**, not by a persuasion threshold |
| **T8** | the world always churns; the player is not necessary | `wear`, the actorless event channel, vacancy, and the Partition's second row |
| **T9** | field investigation is first-class | six acts, every one available to any person; **eligibility never consults office** |

> ⚠ **T5 AND T6 ARE THE HOLONIC THROUGHLINES.** Everything in Part IV is their mechanism. If you
> implement one of them as a broadcast or as a tree walk, you have deleted the middle of the ladder —
> §6.3 explains why that is fatal rather than merely wrong.

## §3 · The five laws

Four are the head's parent suite's; the fifth is the head's own and is the one that makes stories
end.

### L1 · The person is the only actor

**No institution acts. No faction acts. No threshold acts.** An institution acts *by a named person
at a venue*. *"The Church excommunicates"* is not spellable; *"the Confessor, at a venue, issues"* is.

**The property this buys, and it is the best one in the design:** a stranger takes the seat someone
needed, and her ambition progress moves — with **no `obstruct` verb, no knowledge of her in the
stranger's decision, and no branch in the resolver.** Obstruction is not implemented. It falls out.

### L2 · Nobody is omniscient, and the signature is what enforces it

`choose` never receives a `World`. **Not by discipline — by type.** A person decides from a `View`
built of their own claims, which may be wrong, and a false conclusion is indistinguishable from a
true one to the person holding it.

### L3 · Every aggregate is a function, never a field

A stored `unrest` is a lie that outlives its reasons. **Two clauses, and the second is the binding
one:**

1. a monotone counter exists **only per `(Person, axis)` where `axis` is on a closed registry**;
2. **no resolver-side Query may aggregate per-person tallies across holders.**

> ⚠ **CLAUSE 2 EXISTS BECAUSE CLAUSE 1 DID NOT BIND.** Define a per-`(Person, axis)` counter — legal,
> since every increment is in the holder's own ledger — then `Query`-sum it over a cohort. *"That is
> stored, monotone, **never-decaying** unrest in all but name — **worse than the field L3 banned,
> because the banned field could at least go down.**"* Clause 2 is a **read-side** rule and is
> therefore checkable: grep the resolver for a Query crossing holders. A provenance rule is not.

**§22.4 adds the third clause this document found was still missing.**

### L4 · Every state change is partitioned by its subject, asymmetrically

`social: true` on a `(record-kind, field)` pair means **only an act may write it**. `social: false`
means **either** an act or the world may. The world may silt a harbour; it may not sour a town's mood.

**The membership test is a static schema column, not a judgement.**

### L5 · The Edge Law

> **Any monotone quantity may, on crossing a declared edge, change WHAT MAY BE CHOSEN AND BY WHOM —
> including to nothing. The crossing emits and is witnessable. It may never write a social row, and
> it may never produce an outcome.**
>
> **And every clock that moves such a quantity — other than the three the world already licenses
> (matter, bodies, the confidence of a memory) — was set by a nameable act**, so it can be bribed,
> delayed, burned, or killed.

**The second paragraph is the anti-scripting rule stated positively, and it is why the design has no
GM.** A quantity that advances on its own with no author is a **shadow actor**: unbuyable,
undelayable, unkillable — exactly the actor L1 forbids, arriving through a side door.

**What L5 buys, concretely:** 19 of 50 surveyed arcs want a crossing to *force a moment* and then
have a person choose. *"The head of state's forced choice is made — act, abdicate, or be replaced."*
L5 supplies exactly that and nothing more. **The corpus does not want the counter to ACT. It wants
the counter to COMPEL SOMEONE TO ACT.**

## §4 · The two module rules — the holonic core

These two sentences are the container contract. **They are stated once in the chain, applied once
more, and owned by nothing** — which is the gap §44 is about.

> **R-1.** *"A rung may read its own state and any message addressed to it. It may **not** read a
> sibling's state or a descendant's state directly. It **may COMPUTE an aggregate over its
> descendants ON DEMAND**; it may **not receive a pushed aggregate**, and it may **not store one.**"*
>
> **R-2.** *"A rung writes only its own state. **Upward influence is emitting an aggregate; downward
> influence is emitting a refraction. No module reaches through another.**"*

**And the one concession, made explicitly rather than discovered as a race:**

> **A Query MAY be cached. The cache is built AT A BARRIER, is READ-ONLY until the next barrier, and
> is DISCARDED there. Nothing inside a parallel map builds one.**

Without it six operations are O(N²) and the population ceiling is set by a scan rather than by
anything a designer chose. With it, *compute-on-demand* holds **at barrier granularity** — which
stores nothing that can go stale, because it does not survive the barrier.

> ⚠ **THE COST OF BREAKING R-1, IN THE CHAIN'S OWN WORDS:** *"A cross-rung read is the single easiest
> way to destroy T5 and T6, because **once the realm can read a person directly there is no reason
> for the ladder to exist and every intermediate rung quietly becomes decoration.**"*

## §5 · What "holonic" means here — three senses, three verdicts

The word bundles three separable claims. Bundled it is unanswerable; separated each has a clean
answer.

| | claim | verdict |
|---|---|---|
| **H1 · STRUCTURE** | one uniform container type at every scale; the ladder is data, not a type tree | **TRUE, and it is the design's best structural property.** §35 |
| **H2 · CONTRACTS** | every module declares its I/O against one descent a reader can walk | **THE WORK.** Part V |
| **H3 · EXECUTION** | each container runs its own slice of the loop, self-sustaining | **PARTIALLY, and not the way it sounds.** Containers partition a step's *body*; the *boundary* is always global; **no container gets a clock.** §31, §40 |

**The context argument, stated precisely because it is the reason to care:**

> **The bounded-context win comes from H2, not from H3.** A developer or a session that can walk to
> one module and read what it may receive, what it may emit and what it owns has bounded the problem
> **without reading the world, the loop, or a sibling.** That needs no change to the loop at all.
> **H3 buys parallelism**, which is not a context property.

## §6 · Two topologies, and only one of them is a tree

**This is the correction that most changes how the design should be built**, and the first revision
of this document got it wrong by assuming one topology.

### §6.1 The containment tree

`contain` Tenures, from `person` up to `realm`. **A strict single-parent tree.** R-1 and R-2 govern
**this** topology and nothing else.

### §6.2 The lateral graph — the heterarchy

The design has a second topology that is **not** a tree and is **not** governed by R-1/R-2:

- **`tie` and `knot`** — Person→Person **at any distance**, stored once on the lower-id endpoint.
- **`commit`** — Person→Proposition. **A faction is a Proposition plus its `commit` edges**, and
  those edges span rungs freely.
- **`hold` at distance** — Person→Rung outside their own subtree. That is what annexation *is*.
- **Offices with `rung? = null`** — *"A Dicastery, a chivalric order and a trans-settlement guild
  have no containment node."*
- **Containerless venues** — a cluster's `respondent_venue.container` **may be NONE**.

> ### **THE CONSEQUENCE, AND IT IS LOAD-BEARING FOR EVERY IMPLEMENTER**
> **R-1's "aggregate over descendants" is a claim about the CONTAINMENT TREE. Following a `tie`, a
> `knot`, a `commit` or a distant `hold` leaves the subtree and is NOT an R-1 aggregate.**
>
> **Lateral traversal is a resolver-side Query — `World` first — and is therefore unavailable inside
> `choose` by construction.** That is the correct and already-enforced boundary. Do not "fix" R-1 to
> cover lateral edges; the split *is* the design.

### §6.3 Why the distinction is not pedantry

A faction that spans three duchies has no parent rung. A Dicastery issuing to executors across the
realm has no containment node. **Any implementation that routes influence by walking the containment
tree cannot express either**, and both are core to the political layer. Meanwhile any implementation
that lets a realm read a person directly deletes the ladder. **The design needs both topologies, kept
apart, with different access rules.** §36–§38.

## §7 · Two hierarchies, and they are not the same tree

| | the WORLD hierarchy | the CODE hierarchy |
|---|---|---|
| **what it is** | `Rung.kind`: `person → hearth → community → settlement → territory → province → duchy → realm` | the contract descent a developer walks: role → module → key type → field |
| **parent relation** | a `contain` **Tenure edge** | a registry row |
| **realised as** | *"a directory tree and a `Rung.kind` enum. **It is not a type hierarchy**"* | a generated composite over authored registries |
| **governed by** | R-1, R-2 | Part V |

> ⚠ **CONFLATING THESE IS THE MISTAKE THE FIRST REVISION MADE.** It placed a rung-level rule on a
> code-level object and the rule had no referent. **A subsystem has no parent rung and no descendant
> rungs.** Keep the trees apart in your head and in your directory layout.

**And scale is not a level of the code hierarchy.** A module is not "a settlement-scale module"; it is
registered against a role and runs at whatever rungs the step hands it. **Indexing code by scale
deletes the property that makes the ladder worth having** — *"one rung type, instantiated at every
rung, means a mechanism written for elites is automatically available to populations."*

---

# PART II · THE PRIMITIVES

**Everything the engine may declare is in this Part.** If a thing you want is not here, the design's
own admission test (§0.3, Part X §60) applies before you add it — and the test's second question kills
most candidates, because the store's job is usually already being done.

## §8 · The inventory, on one page

```
IDENTITY-BEARING, MUTABLE   Person · Rung · Office · Site · Record         -- five carriers
IDENTITY-BEARING, IMMUTABLE Proposition                                     -- fixed at utterance
THE ONE EDGE                Tenure(kind in hold contain commit oblige succeed tie knot)
THE ONE STATE CHANGE        StateChange(subject, mode in create|alter|destroy, driver in Act|Event, ...)
THE QUERY CATEGORY          Query -- never stored, always recomputed
SEASON-LOCAL               Act · Event · Claim · View · Sensation · Candidate
PERSISTENT NON-CARRIERS    Date · DocketItem · Petition · Dispensation · Venue · ConveningCondition
VALUE TYPES                MatterKind · Envelope · Stores
```

**Eight kinds of thing. Nothing else exists.** A faction is not on this list because a faction *is* a
`Proposition` plus its `commit` edges (§14.2). An `address` is not on this list because it is a
`contain` Tenure. `needs` are not on this list because they are a `Sensation` plus a Query.

## §9 · `Person`

```
Person := (id, weight, marks[], capability, stance[], convictions, beliefs[], ledger, ties_index)
```

| field | type | domain | notes |
|---|---|---|---|
| `id` | id | `H(world_seed, tick, subject_id, purpose)` | minted once; §33 |
| `weight` | int | `>= 1`, default `1` | **a cohort IS a Person at weight > 1** |
| `marks[]` | list | heritage · grade · Church standing · office · residence | the stance table's first referent kind |
| `capability` | map practice → rank | rank `0..5` | **rank supplies dice; it gates no verb** |
| `stance[]` | list | `(referent, valence -5..+5, weight 0..5)` | referent ∈ `Person \| Proposition \| Place` |
| `convictions` | weights over the closed 13 | 1–3 primary + distributed | the moral axes |
| `beliefs[]` | moral commitments | `strong \| wavering \| revised` | **about MORALS, never veracity** |
| `ledger` | packed claim rows | cap `L`, evicted on `confidence_live × recency` | **what they hold TRUE** |
| `ties_index` | derived | — | **owned by Nobody.** The inverse index over `tie`/`knot`; **stored nowhere** |

### §9.1 One class, and reviewers will want to subclass it

> **A cohort is a `Person` at `weight > 1`. ONE CLASS.** There is no conversion operation between a
> named person and a cohort because there is no second type to convert to. **Refuse the subclass.**
> The moment `Cohort extends Person` exists, every mechanism has two code paths and they will drift.

### §9.2 `capability` supplies dice and gates nothing

`rank` contributes to a pool. **It never makes a verb available or unavailable.** The only
class-shaped gate in the design is Thread Sensitivity. If you find yourself writing
`if capability < N: return []` inside an option set, you are re-implementing a gate the design
deleted on purpose.

### §9.3 The moral layer is not the epistemic layer — T2's collision

| | the claim ledger | convictions / beliefs |
|---|---|---|
| holds | what is **TRUE** | what is **RIGHT** |
| moved by | evidence, at WITNESS | argument and consequence, at RESOLVE |
| may be wrong | yes, and that is the mechanism | not applicable — it is a commitment, not a proposition about the world |
| **written at** | **WITNESS** | **RESOLVE** |

> ⚠ **WITNESS NEVER TOUCHES A BELIEF.** If evidence can move a conviction, the moral layer has become
> a second epistemic layer and T2 is gone. This is the single most dangerous collision in the design.

## §10 · `Rung` — the holon

```
Rung := (id, kind, stake[], judging_set_rule, dates[], matter, envelope)
Rung.matter := ( stores : map MatterKind -> int      -- whole units, no fractional matter
               , sites  : list of Site ids
               , records: list of Record ids
               , transmission: Tenure id | null )    -- the succeed pointer for a hearth
Envelope    := packed per-band counts
```

```
Rung.kind in { person, hearth, community, settlement, territory, province, duchy, realm }
```

**Eight kinds, ONE type.** This is H1, and it is what makes a mechanism written for elites
automatically available to populations.

### §10.1 A Rung owns NO social aggregate

**No norms, no densities, no reputation, no unrest, no legitimacy, no discipline-as-a-stored-value.**
Every one is a
Query. **This is the row the whole ownership table exists to protect.**

### §10.2 `person` is a rung kind and a carrier type at once, deliberately

> **The `Rung` of kind `person` is the ADDRESS SLOT, and the `Person` is who stands in it.**

**Generalise that sentence to all eight kinds and you have the container rule:** a rung is *where* a
decision happens; a person is *who* makes it. A rung owns `matter`, `dates[]`, `stake[]`, `envelope`,
`judging_set_rule` — **arrangements, not choices.**

⚠ **One caveat, stated because building on it would be building on a hole:** `judging_set_rule` is
**unspecified** (§62). If it turns out to select *who decides*, it is decision-shaped state on a
container and the sentence above needs a third term. Do not cite it as evidence that rungs own only
arrangements until it is specified.

### §10.3 `envelope` is matter and does not act

Births add weight at the youngest band; deaths remove it. **Birth is envelope weight, not a `create`.**
The envelope is written at MATTER and reconciled at CENSUS. It has **no ledger, no stance and no act.**
The cohort acts; the envelope does not. **Conflating them produces a design in which demography can
choose.**

### §10.4 `MatterKind` is open, correctly

It is a **type parameter, not an enumeration.** Grain, salt, timber, ore and coin are rows in a
registry, not members of a closed set in a source file.

## §11 · `Office`

```
Office := (id, post, rung?, remit, conferral, revocation, establishment[], dates[], upkeep)
remit  := (acts[], scope_rung, binds)
binds  in { members_by_admission, persons_by_presence }
```

| field | notes |
|---|---|
| `rung?` | **optional; null is the office-cluster case** — a Dicastery, a chivalric order, a trans-settlement guild. **§6.2** |
| `remit.acts[]` | drawn from a **closed five**: `issue` · `determine` · `confer`/`revoke` · `dispatch` · `convene` |
| `conferral` | the basis, **per office** |
| `revocation` | who may revoke, and at what venue |
| `establishment[]` | the named persons the office employs. **Finite, contested, durable** |
| `upkeep` | what the post pays its establishment out of the office's stake |

### §11.1 An office adds NO verb and NO modifier

> **It makes ordinary acts eligible where they otherwise are not, and it substitutes the pool source:**
> `pool(act by remit) = capability of the dispatched establishment member(s) actually performing it`.
> **Neither the holder nor anyone else rolls differently for anything.**

**Who holds an office is NOT a field on the office.** It is a `hold` Tenure, owned by the holder.

## §12 · `Site`

```
Site := (id, rung, kind, condition, drawers[])
```

**`condition` is PRIMARY STATE, not a Query**, and the argument is worth keeping because it is the
model for every similar call:

1. An accumulator that reads its own previous value **is** primary state.
2. A draw-weighted mean over child sites **has no base case** and is not total at a leaf.
3. **Node-keying destroys site identity and yields two wrong answers at once** — a settlement holding
   a silted harbour at `0.1` and a healthy seam at `0.9` collapses to `~0.5`, which keeps the bulk
   shipping verbs the harbour should have closed and closes the mining verbs the seam should have kept.

### §12.1 `condition` gates verbs, and that is how damage removes an option

```
verbs(w, site, c) = { v : condition(c) >= floor(v) }
```

**A band edge crossing is an EMISSION, not a write** — and it is the L5 mechanism in its commonest
form. **This is also why §48's fixed point is not optional:** the gate is a comparison on a summed
value, so a one-ulp difference **is a verb that exists in one ordering and not another.**

## §13 · `Record`

```
Record := (id, rung, kind, forgery_quality, subject_matter)
```

**`Record` is a live carrier, promoted from an inert noun** — the head's single highest-leverage
change. It gets:

| | what | why it is lawful |
|---|---|---|
| **created by an act** | a `create`-mode StateChange whose subject is a Record | the write matrix already carries *carrier existence · RESOLVE · yes* |
| **held by a person** | a `hold` Tenure whose object is a Record | extends `hold`'s domain |
| **a `ttl`** | decremented at MATTER, emitting expiry | a licensed clock |
| **act-declared terms** | stages whose maturation is **the creating act's own term ripening** | §13.1 |
| **it gates, and it taxes** | a held Record may make others' acts **unavailable** or **more costly**, and may be the sole route to a function | custody finally carrying weight |

**Honest price:** two new fields, a `(Record, …)` Partition row (**the design currently has none, so
every Record write is an unmarked cell**), an opened kind roster, and one overturned ruling.

### §13.1 Terms are act-declared, NEVER MATTER-advanced — and this is a worked lesson

A case that ripens against you while you do nothing looks like it wants `Record.stage` advanced by
MATTER. **It does not, and adding that is a fourth clock-driven quantity that L5's carve-out forbids.**
Worse, *"the fiction of a case advancing is not weather — it is clerks filing, witnesses deposed, a
tribunal scheduled."*

> **The lawful version costs less and produces a better game.** The Inquisitor's `open_case` act
> **declares the stages and their terms.** MATTER matures terms; each maturation is *a person's past
> act ripening*, with `causes[]` pointing at the act that wound the clock.
>
> **Every capability survives, and one improves:** the case still ripens while the accused does
> nothing — **because the Inquisitor is not doing nothing** — and a half-made copy now correctly
> **stops** if the copyist is jailed, which the MATTER-driven version gets wrong: a copy that finishes
> itself.

**And the arcs get better by the design's own argument:** an act-declared term gives every accusation
handles — **bribe the clerk who set the term, burn the Record that carries it, kill the man who must
renew it.**

## §14 · `Proposition`

```
Proposition := (id, mood in { HOLDS, OUGHT }, subject, predicate, value, when, scope)
```

**Identity-bearing and IMMUTABLE.** Fixed at utterance, never destroyed. A Proposition of mood `OUGHT`
is an uttered Belief.

### §14.1 A Proposition outlives its utterer, unowned

**Nothing needs to own it, because nothing may change it.** It is referenced by every `commit` edge
and every stance row that names it, and those have owners.

### §14.2 A faction IS a Proposition plus its `commit` edges

Membership is `commit`. Leadership, presence, density and footprint are **Queries**. The persistent
part is the immutable Proposition; institutional memory is Records at a Rung.

> **Nothing is lost, and one thing is gained: a faction collapses when people leave, with no
> dissolution mechanism, because there is nothing left to be the faction.**

⚠ **THAT SENTENCE IS NOT YET TRUE, AND §54 FOLDS IN THE FIX.** A Proposition may be a `hold` subject
and is never destroyed, so a memberless faction leaves **territory held by a banner nobody carries**,
uncontestable because the holder can never appear at a venue.

## §15 · `Tenure` — the one edge

```
Tenure := (id, subject, object, kind, since, until?, conferrer?, degree?, payload?)
kind in { hold, contain, commit, oblige, succeed, tie, knot }
```

| kind | subject → object | cardinality | notes |
|---|---|---|---|
| `hold` | Person → Office \| Rung \| Record \| Proposition | **1 per object** | office-holding, tenancy, custody |
| `contain` | Rung → Rung | **1 parent** | **the containment ladder.** Never destroyed by a bare `revoke` |
| `commit` | Person → Proposition | many | **this is faction membership** |
| `oblige` | Person → Person \| Office | many | Duty |
| `succeed` | Rung → Person | 1 | the hearth's transmission pointer |
| `tie` | Person ↔ Person | many | **stored ONCE, on the lower id** |
| `knot` | Person ↔ Person | many | **stored ONCE, on the lower id** |

### §15.1 Every Tenure is owned by its SUBJECT

**One home, one writer, no reach-through. The object side is a derived index, never stored.**

`tie` and `knot` are stored once **on the endpoint with the lower id**, because a shared `strain` on a
directed record otherwise has two homes and **can disagree with itself.**

### §15.2 `until?` is what makes a destroyed tenure a fact

A revoked tenure is a **historical claim subject** — argued over, read for entrenchment. **Do not
delete rows.** `entrenchment(h, H) = min(1, seasons_held / 60)` has nothing to read if you do.

⚠ **THIS IS ALSO A HAZARD — see §22.4.** Because ended Tenures persist, a count over live *and* ended
edges is monotone, which is a ratchet built entirely out of "structural" edges.

### §15.3 Death writes `until`, and it is the Partition's one declared seam

> `(Tenure, until)` is `social: false` — **the Partition's one declared seam** — and death's `until`
> write is **the only Tenure write in the MATTER class.**
>
> **The seam is bounded by a CAUSATION rule, not by the column:** an actorless row may write `until`
> **only on a `(Person, exists)` change the same row also caused.** A plague that kills the praefect
> ends his tenure through the death; **a storm cannot touch it.**

**A second such seam means the column is the wrong mechanism.** Treat any proposal for one as a
redesign, not an addition.

### §15.4 `annex` and `secede` are not verbs

They are deleted from the vocabulary. Annexation is a `hold` at distance (§6.2); secession is the
`commit` edges moving.

## §16 · `StateChange` — the one state change

```
StateChange := (subject, mode in { create, alter, destroy }, driver in { Act, Event },
                field?, delta?, spec?)
```

**One shape for every mutation in the game.** `create`/`destroy` cover carrier existence; `alter`
covers everything else. **`social` on `(record-kind, field)` decides which drivers are admissible.**

> ⚠ **`destroy` sets `until = tick` on every Tenure whose subject or object is the destroyed id, and
> destroys nothing else.** It does not cascade into other carriers.

## §17 · `Query` — never stored, always recomputed

Two families, and **the side column IS the enforcement**:

```
-- RESOLVER-SIDE: World FIRST, always. Calling one from inside choose() fails at the call site.
leaders(w, ...)        presence(w, ...)      density(w, ...)       footprint(w, ...)
sovereign_fraction(w, ...) -> (fraction, undetermined_count)
condition_at(w, ...)   verbs(w, site, c)     judging_set(w, ...)   draw_share(w, ...)
share(w, ...)          filter_share(w, ...)  capacity(w, ...)      enforcer_presence(w, ...)
hold_force(w, ...)     establishment_of(w, ...) conferral_path(w, ...) retention(w, ...)
docket_of(w, ...)

-- PERSON-SIDE: takes the asker; may read the asker's OWN interior and nothing else.
assemble(p, question)  opening_set(p, view) -> Candidate[]        entrenchment(p, ...)
norm_as_claimed(p, ...) address(p)          trace(p, ...)         need(p, ...)
leaders_as_claimed(p, ...)
```

> ⚠ **`opening_set` RETURNS `Candidate[]`, NOT `Act[]`.** *"Typing it as acts makes the option set an
> authored list rather than a computed one."* The head's own player document still carries the old
> `-> Act[]` signature — a landed ruling that never reached one file (§54, item 1). **Use
> `Candidate[]`.**

**Caching:** a Query may be cached **only at a barrier**, read-only until the next, discarded there.

## §18 · Season-local records

`Act` · `Event` · `Claim` · `View` · `Sensation` · `Candidate`. All are created within one season.
Only `Event` and `Claim` persist beyond it — `Event` in the log, `Claim` in a ledger.

```
Act       := (id, actor, verb, changes[], reads[], contests[], payload)
View      := at most K claim ids from the holder's OWN ledger -- built, not filtered
Sensation := (subsistence, standing)   -- EXACTLY two scalars, and nothing else
```

### §18.1 `View` holds ids, never references

A view that holds references is a masked world. **Hold ids.**

### §18.2 `Sensation` is exactly two floats

Computed by `sense(person, frozen_world)` — **the one non-decision function permitted a `World`.**
`standing` is the gap between what everyone reads off you and what you hold.

## §19 · **`Event` — THE RECORD THAT WAS MISSING**

**This is the single most important section in Part II**, because four separate things in this
document are stated over `Event` and the chain never wrote its record down.

### §19.1 The state of the chain, measured

- **The head defines no `Event :=` anywhere.** Verified: zero occurrences across all nineteen files.
- **An earlier in-chain revision does:** `Event := (id, kind, subject, changes[], emitted_at)` — five
  fields. **It was carried as an open item, then dropped from the open register**, and never written.
- **The head's log invariants exist** and are good: id uniqueness, referential integrity on `causes[]`,
  cycle-freedom, a content hash, a non-decreasing season index, canonical axis and role names.
- **So the design has the LOG but not the RECORD.**

### §19.2 The record, proposed

```
Event := ( id            -- H(world_seed, tick, subject_id, purpose); unique, no allocator
         , kind          -- from the registered type roster; family.type, lowercase dotted
         , subject       -- the carrier the change is about
         , changes[]     -- StateChange rows, the applied mutation
         , causes[]      -- REQUIRED AND NON-EMPTY. ids already in the log, or [ROOT]
         , emitted_at    -- season index, non-decreasing
         , degree?       -- from the ONE ladder, when the event came from a contest
         )
```

### §19.3 Three fields that are NOT on it, and why each absence is a design decision

| absent field | why |
|---|---|
| **`actor` / `source_actor`** | **Attribution is a per-witness `Claim`, not a field on the Event.** The Event carries *what happened*; *who did it* is something each witness concludes, may be wrong about, and may not conclude at all. **This is what makes covert action and false attribution expressible**, and five arcs need it |
| **`target` / rung address** | **There is none, and the first revision of this document assumed there was.** The only transport the design defines is a chain of `tell` acts; there is no non-act news transport. Observers are computed at WITNESS from presence and channel — **the emitter declares no recipient** |
| **`stat_deltas` applied at emission** | changes are applied by the step that owns the write class, not by the log |

> ### ⚠ **THE CONSEQUENCE FOR ANYONE PORTING: DO NOT ADD A TARGET FIELD TO MAKE ROUTING EASIER.**
> It is the twin of the attribution field the design deliberately removed. **An Event that knows who
> it is for is an Event that cannot be misattributed**, and misattribution is a feature.

### §19.4 `causes[]` — required, non-empty, and one carve-out

**`causes[]` must be non-empty.** The design rests its narrative layer, audit trail and arc model on
this edge — *"the arc itself"* — and the measured state is that the specified loop emits `causes=[]`,
so **the substrate of the entire emergent-narrative claim is declared and never populated.**

> **The carve-out: an Event with no antecedent declares `causes: [ROOT]`, never `[]`.** A campaign
> seed and a licensed clock's first emission legitimately have no antecedent act; a rule they cannot
> satisfy would be amended away within a season. **`[ROOT]` makes the empty list unrepresentable
> rather than merely discouraged.**

### §19.5 One log, not two

**Two logs cannot share a `causes[]` chain**, so an Event in log A can never name one in log B as its
cause; T3's multiple perspectives on one event and arcs-as-provenance-chains both break at the seam.

⚠ **Honest note on this derivation (§0.1 qualification 2):** the referential-integrity invariant that
makes cross-log citation fail is *itself* scoped to "the log", so read strictly the argument
presupposes what it proves. **The non-circular grounds are stronger and are the ones to cite:**
WITNESS is one global pass; the design's predecessor loop was retired *because its WITNESS was not
global*; and the seam returns contest Events *"into the same log"*.

## §20 · `Claim`, and the epistemic layer

```
Claim := (id, holder, subject, predicate, value, when, source, confidence, visibility)
source in { firsthand, told_by, inferred, firsthand_via_knot }
```

- **`witness` is the only minter of a root token.**
- **Eviction ranks on `confidence_live × recency` only — never on salience.**
- Claims live in the **holder's own ledger**, cap `L`. Nobody else may read or write it.

**Five witness channels, no sixth:** `post_remit` · `co_located` · `witness_key` · `document_key` ·
`chronicle`.

## §21 · Persistent non-carriers

| type | note |
|---|---|
| `Date` | **the spine of T7.** A sitting is a Date that has fired. A vacant date **fires, allocates nothing, and lapses** |
| `DocketItem` | what a Date will consider |
| `Petition` | `(id, petitioner, proposition, respondent_venue, backing[])`. **§54 folds in multiplicity and supersession** |
| `Dispensation` | `(id, issuer, proposition, scope, terms[])` — **nine typed terms, no bare effect field**. §37 |
| `Venue` | **`container` may be a Rung, an Office, or NONE.** §6.2 |
| `ConveningCondition` | owned by the holder of the date it schedules. **Its predicate may read only the holder's own state, an R-1 aggregate over its descendants, or the calendar** |

## §22 · Ownership — six owners, one log, and Nobody

**The test of this table: name any value in the game and it says who owns it, or the table is
incomplete.**

| owner | owns | never owns |
|---|---|---|
| **Person** | everything interior — `marks`, `capability`, `stance`, **`convictions` and `beliefs`**, the claim ledger; **every Tenure whose subject they are**; the Propositions they utter | anything about another person; **any aggregate** |
| **Rung** | `matter` (`stores`, its Sites, its Records, the transmission pointer), `dates[]`, `envelope`, `stake[]`, `judging_set_rule` | **any social aggregate** |
| **Office** | `post`, `remit`, `conferral`, `revocation`, `establishment[]`, `dates[]`, `upkeep` | **who holds it** — that is a `hold` Tenure owned by the holder |
| **Site** | `condition`, `drawers[]`, `kind` | anything social |
| **the log** | itself, append-only | nothing else. Written by RESOLVE and MATTER, read by everyone |
| **params** | **every exported constant** — the condition scale, `wear` per site kind, the obstacle floor, band coefficients, the ledger cap. **Never in prose and never in two files** | anything that varies per instance |
| **the holder of a date** | its `ConveningCondition`s | — |
| **Nobody** | **every aggregate**: faction, leaders, presence, density, footprint, norm, scale, reputation, needs, openings, entrenchment, coarse condition, sovereignty | — these are Queries, **stored nowhere** |

### §22.1 Why Nobody owns an aggregate

**Stored aggregates are how a design acquires dead state that reads as mechanism** — a value
initialised once, never written, and cited for seasons as though it meant something. **If the
aggregate is a function it cannot go stale, and it cannot be initialised and then forgotten, because
there is nothing to initialise.**

### §22.2 The read/write asymmetry hazard — the guard this licenses

**When a getter starts computing from a new source while setters still write the old one, every
writer silently becomes a no-op.** Before changing such a field, grep its **assignments** — not its
readers — and fail on a *new* bare assignment.

> ⚠ **THE LIVE CASE:** a per-issue stance store exists **beside** `Person.stance` rather than being
> absorbed into it. **The carrier must ABSORB it, not sit beside it.** Two owners for one value is the
> hazard by construction.

### §22.3 Values with no owner — named rather than glossed

`season_factor`'s distribution (**this blocks `yield`**); the cohort's construal spread (the rule is
stated, the representation is not); the object-side Tenure index (**Nobody, by rule** — a
barrier-built cache); travel legs (**in the write matrix and the churn ledger, in no ownership row**).

### §22.4 **The aggregation boundary — three clauses**

This is L3 completed. **Clause 3 is this document's addition and it closes a hole two clauses left
open.**

> 1. A monotone counter exists **only per `(Person, axis)` where `axis` is on a closed registry.**
> 2. **No resolver-side Query may aggregate per-person tallies across holders.**
> 3. ⊕ **An aggregate composes only over LIVE edges (`until == null`). Any Query monotone in the
>    ENDED-edge set is a ratchet and is refused.**
>
> **Why clause 3 is needed.** Ended Tenures persist as historical claim subjects (§15.2), so
> `count{ t : kind=commit, object=prop }` over live **and** ended rows is monotone non-decreasing;
> `count{ hold : until != null }` is *revocations ever*; `count{ oblige ended by repudiation }` is a
> grievance ratchet. **Each is built only from "structural" edges and each evades clause 2**, because
> none is a per-person tally on an axis.
>
> **And the boundary between R-1 and the resolver, restated from §6.2:** an R-1 on-demand aggregate
> composes over the **containment subtree**. **`tie`, `knot`, `commit` and distant `hold` leave the
> subtree and are resolver-side Queries** — `World` first, and therefore unreachable from `choose`.

---

# PART III · THE SEASON LOOP

## §23 · The loop, whole, on one page

```
  ┌── CALENDAR ─────────── barrier 1 · fires occasions and DECIDES NOTHING
  │        dates come due · dockets form · option availability recomputed
  │
  ├── MATTER ───────────── barrier 2 · THE WORLD FREEZES AT ITS END
  │        events resolve FIRST · bodies · larders · yield · travel · wear
  │        NO social quantity moves here
  │
  ├── DELIBERATE ───────── a MAP, not a barrier · pure · any order · parallel
  │        choose(person, view, sensation) -> Act[]     bounded by budget(person, view)
  │        reads the frozen world through TWO FLOATS and nothing else
  │
  ├── RESOLVE ──────────── barrier 3 · the ONLY writing step for acts
  │        ordered fold · five strata · touch-graph conflict · contests · sum-then-clamp-ONCE
  │
  ├── WITNESS ─────────── barrier 4 · THE JOIN
  │        global fan-out, ONE pass · then per-person deposit into OWN ledger
  │
  └── CENSUS ──────────── shares WITNESS's join
           reads the post-eviction ledger set ONCE · individuation · envelope
```

**Six steps, four barriers, and the counts differ for two structural reasons:** DELIBERATE is a map,
not a barrier; CENSUS shares WITNESS's join rather than opening its own.

### §23.1 The three vocabularies, and which one binds

The chain carries a coarser three-phase tick and a retired seven-phase model. **The six steps are a
REFINEMENT of the coarse tick, not a replacement**, and the mapping is:

| coarse phase | steps |
|---|---|
| season tick | **CALENDAR** |
| action | **MATTER · DELIBERATE · RESOLVE** |
| accounting boundary | **WITNESS · CENSUS** |

**The step names are words, permanently.** `CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS ·
CENSUS`. Uppercase, English, **no letter-number spellings, ever** — a prior draft spelled them
`B1…M2` and then cited review findings `B1` and `M1` in the same file: two namespaces, one token
shape.

## §24 · CALENDAR — barrier 1

**Dates come due. Dockets form. Option availability is recomputed. NOTHING IS DECIDED.**

- **CALENDAR does not advance the season counter.** Exactly one module may, and it already does.
  A second advance double-ticks the world.
- **A vacant date fires, allocates nothing, and lapses.** It does not block.
- **A convening predicate may read only** the holder's own state, **an R-1 compute-on-demand aggregate
  over its descendants**, or the calendar — *never another person's interior, and never a descendant's
  stored state.* **This is the one place in the loop where R-1 is applied by name.**
- Death does **not** open the conferral Date. **The vacancy is a fact; the date is an occasion; CALENDAR
  is where facts become occasions.**

**Write class: CALENDAR.** Writes `Date`, `DocketItem`, `ConveningCondition` (firing and clearing).

## §25 · MATTER — barrier 2; the world freezes at its end

**Events resolve FIRST**, then bodies, larders, yield, travel, wear.

> **NO SOCIAL QUANTITY MOVES HERE.** This is L4 at its sharpest. The world may silt a harbour; it may
> not sour a town's mood.

| written | note |
|---|---|
| larders, `stores` | subsistence draw |
| bodies, ageing, natural death | one of the three licensed clocks |
| travel legs | ⚠ **crosses rungs** — §31 |
| `yield` | **only here.** Blocked on `season_factor`'s distribution (§22.3) |
| `condition(site)` | **`wear` ONLY.** Act deltas are RESOLVE's |
| `Tenure.until` on death | **the only Tenure write in the MATTER class**, bounded by §15.3's causation rule |
| carrier existence | death |
| envelope weight | births and deaths |

### §25.1 The three licensed clocks are exhaustive

**Matter, bodies, and the confidence of a memory.** Nobody wound any of the three, and you cannot
bribe silt. **Everything outside this list needs an author** — that is L5's second paragraph, and
§13.1 is the worked case.

### §25.2 MATTER touches persons, not only places

Subsistence is drawn from `stores`; condition is taken from the Sites you stand beside. **Bodies are
a licensed clock, so this is sanctioned world-driving, not a new exception.**

## §26 · DELIBERATE — a map, not a barrier

```
choose : (Person, View, Sensation) -> Act[]          -- ordered, bounded by budget(person, view)
budget : (Person, View)            -> int            -- a QUERY, never a field
sense  : (Person, frozen_world)    -> Sensation      -- the only bridge from world truth into choose
```

**Pure. Any order. Parallel. Writes nothing but the returned acts.**

### §26.1 `choose` has no `World`, and that is enforced by the parameter list

**Not by discipline — by type.** Every resolver-side Query takes `World` first, so calling one from
inside `choose` fails at the call site for want of an argument.

⚠ **[engine] In GDScript this becomes a CONVENTION plus a token scan, permanently**, because the
language has no module system and no visibility modifiers. §53.

### §26.2 The world is frozen from the end of MATTER to the start of RESOLVE

**This is what makes the map safe to parallelise**, and it is the property a per-container clock
would destroy (§40).

### §26.3 The act budget is ~5, and it is RULED

> **`02_SCENE_BUDGET_RULING.md` (#351), Jordan, verbatim:** *"please note for the ideal proposal that
> i expect a character to get ~5 playable scenes per season, which may mean that they get ~5
> actions."*

**This overturns "ONE ACT PER PERSON OR COHORT PER SEASON, UNIVERSALLY", which the design states
twice in bold.** It is in the chain and it is not a proposal.

**Why the number is not the finding.** At one act **nobody ever chooses what to leave undone.** A King
facing four simultaneous pressures who can substantively address two, with the other two compounding,
is doing the thing that high office *is*. **At one act per season a King's scarcity is identical to a
copyist's.**

**Three consequences to implement:**

1. **`budget` is a Query, never a field** — office, condition, distance travelled. A wounded duke gets
   fewer acts than a healthy one **without anybody storing a number.**
2. **The list is ORDERED**, so what he did first is legible when a season's later acts are foreclosed
   by its earlier ones.
3. **Petition spray is ALLOWABLE, and this is RULED** (Jordan, 2026-09-01): *"if a character wants to
   spend their entire season meeting with people to petition, let them."*

> ### **THE SPRAY QUESTION IS CLOSED, AND CLOSING IT THIS WAY STRENGTHENS §26.3 RATHER THAN WEAKENING IT.**
>
> The old closure was *"provisionally, by one act per person"*, and at ~5 that closure is void. **The
> replacement is not a cost gate and not a cap — it is nothing.** A character who spends all five acts
> petitioning **has chosen to leave four other things undone**, which is precisely the triage the
> budget exists to create. **Spray is the mechanism working, not a defect in it.**
>
> **Three consequences for an implementer:**
> - **No dedup, no cap, no per-venue limit, no "already before a body" rule.** Any of them would be
>   *an engine deciding a person's options*, which is L1.
> - **No cost clause is required.** A petition consumes budget like any act, and that is the whole of
>   the pricing. (An earlier revision of this document proposed *"a refused petition costs standing
>   with the venue"* as a necessary gate. **It is not necessary.** It may still be good design — a
>   venue that remembers being wasted is expressible through ordinary stance and claims — but it is
>   now optional colour, not a fix.)
> - **§54.1's close rule matters MORE, not less.** With spray allowed, several live petitions on one
>   matter is the normal case, so the rule that closes them must be right: **petitions never close each
>   other; a matter closes at RESOLVE by scarcity and at CALENDAR by lapse.**

> ⚠ **AND THE RULING CARRIES AN OBSERVATION WORTH RECORDING RATHER THAN FIXING** (Jordan, same):
> *"this may point towards the lack of actions available so far for characters to perform, which is
> okay at this point."*
>
> **If petitioning five times is an attractive way to spend a season, the act vocabulary is thin.**
> That is **an accepted state of the design at this stage, not a debt to close here.** §63.1 records
> it so a later reader does not mistake the silence for an oversight — and so that nobody "fixes" a
> thin vocabulary by capping the one act that is well specified.

⚠ **What remains genuinely open is narrower than the ruling:** whether a *scene* equals an *act*. The
ruling says *"~5 playable scenes… which may mean ~5 actions"*. §62.

## §27 · RESOLVE — barrier 3

```
resolve : (Act[], World) -> Event[]      -- signature unchanged
order   : (Act[], World) -> Act[]        -- a Query. Declared, inspectable, no new state
```

**The only writing step for acts.** Five strata: movement · binding decisions · contested physical ·
uncontested material · social.

### §27.1 Contention is an ORDERED FOLD, not a grouping

**Applying acts independently means two people cannot contend for one scarce thing in one season** — a
blocker cannot hold a line, helping one claimant cannot starve another, a shortfall cannot produce a
*pending* state. **Scarcity is what makes politics, and independent application has none at the moment
of resolution.**

> **The minimal fix is not a new function; it is a fold.** Each act sees the world its predecessors
> left. **Sequence, not simultaneity.**
>
> **Scarcity then falls out for free** — the second claimant on an emptied granary gets a *different
> Event* because the granary is already empty — **and no act needs to know that another act existed**,
> which preserves L1's best property at the level of resources.

⚠ **THE FOLD DEPENDS ON A PRECONDITION THAT IS NOT WRITTEN.** *"The second claimant on an emptied
granary gets a different Event"* is **false if `transfer` can mint from a negative larder.** §54 item 7
folds in `stores(hearth(giver), kind) >= amount`.

### §27.2 The one resolver — the highest-value refusal in the design

**No second resolver. No auto-resolve formula. No fast path.**

> ⚠ **THIS IS THE REFUSAL WITH NEITHER A MECHANISM NOR A CHEAP TEST. It is enforced by a person
> noticing.** It is also the refusal whose violation is most tempting, most locally reasonable, and
> most catastrophic. **Name it as the weak point rather than claiming a guarantee.**

### §27.3 Sum-then-clamp-once

Clamping may not depend on arrival order. Sum all deltas, clamp **once**.

### §27.4 An attempt at `Ob > 2 × Pool` is refused, and the season is spent

An uncontested attempt routes to a **gate**, never to an `Ob = 0` roll.

**Write class: ACTS.** Everything an act writes, and nothing else.

## §28 · WITNESS — barrier 4, the join

```
witness : (Person, Event) -> Claim[]        -- per person. NO collection signature exists.
```

**Two stages, and only the first is global:**

1. **FAN-OUT IS GLOBAL AND ONE PASS.** For each Event, compute its observer set from the presence
   index and the five channels. **No signals, no subscription table.**
2. **DEPOSIT IS PER-PERSON**, any order, into that person's **own** ledger and no other.

- **A Knot deposit reuses the event id.**
- **Eviction never ranks on salience.**
- **WITNESS never touches a Belief** (§9.3).

⚠ **The design's predecessor loop was retired precisely because its WITNESS was not global** — which
made its parallelism claim *unsound rather than merely unproven*. **Do not shard the fan-out.**

**Write class: INTERIOR.** The claim ledger, own only.

## §29 · CENSUS — shares WITNESS's join

Reads the post-eviction ledger set **once**. Demand-driven individuation and de-individuation;
envelope reconciliation.

> **DEMAND-DRIVEN ONLY. Nothing generates without a demand, and no clock generates anything.**

⚠ **A world-generation roster is not a clock**, and §54 item 18 folds one in. Say so on the row or the
next reader will strike it.

## §30 · The write matrix

**`CALENDAR · MATTER · ACTS · INTERIOR` are WRITE CLASSES. A write class is NOT a step.** One class
may be written in two steps.

| written thing | CALENDAR | MATTER | DELIBERATE | RESOLVE | WITNESS | CENSUS |
|---|---|---|---|---|---|---|
| `Date`, `DocketItem` | **yes** | no | no | **yes** (`carry`, `convene`) | no | no |
| `ConveningCondition` | **yes** (firing, clearing) | no | no | **yes** (`convene` attaches one) | no | no |
| larders, `stores` | no | **yes** | no | **yes** (`transfer`, `levy`) | no | no |
| bodies, ageing, death | no | **yes** | no | **yes** (killing, wounding — **an act**) | no | no |
| travel legs | no | **yes** | no | **yes** (movement) | no | no |
| `yield` | no | **yes, only here** | no | no | no | no |
| envelope weight | no | **yes** | no | no | no | **yes** |
| `condition(site)` | no | **yes — `wear` ONLY** | no | **yes — act deltas, only here** | no | no |
| `Tenure` | no | **yes** (`until` on death) | no | **yes** (`confer`/`revoke`/`create`/`destroy`) | no | no |
| carrier existence | no | **yes** (death) | no | **yes** (`create`/`destroy`) | no | **yes** (individuation) |
| `stance` | no | no | no | **yes** | no | no |
| the claim ledger | no | no | no | no | **yes, own only** | no |
| the returned `Act[]` | no | no | **yes** | — | no | no |

> **ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION.**

### §30.1 Two rows the matrix does not yet have

- **`(Record, …)`** — the design has **none**, so **every Record write is an unmarked cell.** §13.
- **`(Person, exists)`** — death. Without it a death write raises under the matrix's own rule.
  **Rule the row first, then add it**; the reverse order invents the thing the rule exists to prevent.

### §30.2 Make the write class a PARAMETER of the store API

> **Then "no write outside the matrix" is MECHANICAL rather than conventional** — and it is checked
> **per write site**, which is finer than any per-module declaration can be.

⚠ **And the gate must APPLY the write.** A gate that validates, logs and returns `true` while the
actual mutation happens beside it is worse than no gate: the logged value and the applied value
diverge, and *"enforced by construction"* becomes false while looking true. **Either the gate applies
the write, or direct assignment is made impossible.**

## §31 · The per-owner partition — which steps a container may run

⚠ **THIS SECTION REPLACES A RETRACTED CLAIM** (§0.2 finding 3). The first revision said "two of six
steps partition per container" and reached it by applying two different tests to two groups of steps.

**The correct frame is per-OWNER, not per-rung**, and the criterion is uniform: *a step's body
partitions by the single owner of what it writes; its boundary is always global.*

| step | body partitions by | global? | why |
|---|---|---|---|
| **CALENDAR** | **the date-holder** (a Rung *or* an Office, which may have `rung? = null`) | boundary only | writes `dates`/`dockets` owned by one holder; its predicate reads own + R-1 subtree + calendar |
| **MATTER** | **the Site, the body, the larder's Rung** | boundary only, **with three exceptions** | §31.1 |
| **DELIBERATE** | **the person** | **not a barrier at all** | pure map |
| **RESOLVE** | ⛔ **does not partition** | **GLOBAL BODY** | the ordered fold needs **one** order; a per-container fold has none |
| **WITNESS** | stage 1 ⛔ **global**; stage 2 **per person** | **stage 1 is a GLOBAL BODY** | fan-out is one pass over the presence index |
| **CENSUS** | **the Person or the Rung written** | boundary only | needs one snapshot, like DELIBERATE |

> ### **THE HONEST STATEMENT: EVERY STEP'S BODY PARTITIONS BY ITS WRITE'S OWNER EXCEPT TWO —
> RESOLVE'S ORDERED FOLD AND WITNESS'S FAN-OUT. EVERY STEP'S BOUNDARY IS GLOBAL.**

### §31.1 MATTER's three cross-owner operations — name them, do not hide them

The partition is **not free**, and these are where:

1. **Subsistence.** A `person`-kind rung draws from its **containing** rung's `matter.stores`.
   **This is lawful as an R-1 on-demand READ of the parent, not a cross-rung write** — but it means
   MATTER is not closed over one owner.
2. **Death's cascade.** `until = tick` on **every** Tenure the deceased held — including `hold` on
   offices at other rungs, and `tie`/`knot` rows stored on **another person's** endpoint.
3. **The actorless event channel.** A plague or a storm is **one Event spanning many rungs.**
   ⚠ **Sharding it per rung breaks `causes[]`**, because one cause is one id.

**Plus one unowned value:** travel legs are in the write matrix and the churn ledger and in **no**
ownership row (§22.3), and they move a person **between** rungs.

### §31.2 What this means for an implementer

**Parallelise the bodies, join at the boundary, and special-case nothing.** Concretely:
- DELIBERATE → a parallel map over persons. **This is the one that pays.**
- MATTER → parallel over Sites and bodies; **run the event channel and the death cascade serially**
  before the parallel section, because both cross owners.
- RESOLVE and WITNESS-fan-out → **serial, by design.** Do not attempt to shard either.
- CENSUS → parallel over written owners, from one snapshot.

## §32 · Order independence, and exactly what it rests on

**Five things. Four survive any partition; the first is the one a container clock would destroy.**

1. **The world is frozen** from the end of MATTER to the start of RESOLVE.
2. **No shared allocator.** Ids come from `H(world_seed, tick, subject_id, purpose)`. **There is no id
   service, no counter, and nothing to serialise on.**
3. **The act array is canonicalized before resolution** — sorted by a content-derived key, never by
   completion order. ⚠ Note this sorts **one global array**; per container the sort survives only per
   container, which is exactly why RESOLVE does not partition (§31).
4. **Sum-then-clamp-once.**
5. ⚠ **FIXED-POINT ARITHMETIC.**

> ### **THE PART THAT IS COUNTER-INTUITIVE AND MUST NOT BE SOFTENED**
> **Batching delivers CLAMP-order independence. It does not deliver SUMMATION-order independence.**
> [engine] IEEE float addition is **not associative**: `+0.3, −0.5, +0.3` applied to `0.9` lands on
> different last-bit values under different orders.
>
> **And this architecture makes that difference OBSERVABLE rather than cosmetic**, because
> `verbs(w, site, c)` is a **band gate on the summed value** — so a one-ulp difference at a floor is
> **a verb that exists in one ordering and not in another**, and a band-edge crossing is an Event
> people witness.
>
> **The fix is fixed-point integers** (§48). Integer addition is associative and commutative, so
> order independence **stops being a claim and becomes a fact** — and the structural test can then
> assert **bit-identity** rather than approximate equality, which is the only assertion that can
> observe the failure it excludes.
>
> **If fixed point is ever refused**, a canonical summation order plus the hash tiebreak makes the
> result **reproducible** — but then the honest word is **canonically ordered**, not
> *order-independent*, and **every document must change the word.**

## §33 · Determinism

| | |
|---|---|
| **the seed** | one `world_seed` per campaign |
| **substreams** | every roll draws from `H(world_seed, tick, subject_id, purpose)` — **never a shared, re-seeded generator** |
| **replay** | identical seed + identical code ⇒ identical event log ⇒ identical content hash |
| **the artifact** | a content hash over the log |

- **`purpose` must be unique per DRAW, not per operation**, or two draws inside one act collide.
- **`H` is an owned, versioned mix — never a language built-in `hash()`**, whose value is not a
  cross-version contract.

> ⚠ **THE MEASURED HAZARD, AND IT IS WHY SUBSTREAMS EXIST.** Drawing from a campaign RNG in a *new
> place* **shifts every downstream draw** — which is how *adding two NPCs* was observed to move a
> seeded winner. **A person loader that draws from the shared stream moves every golden for reasons
> that have nothing to do with the people it added.**

**Ties break on a hash. Rank never breaks a tie. There is no hidden turn order.**

## §34 · What the loop refuses — and whether the refusal is mechanical

**A refusal only a reader enforces is a convention.** Both kinds are listed, and **overstating this
column is the failure mode.**

| refusal | enforcement |
|---|---|
| `choose` sees no World | **mechanical in a typed language** (absent parameter + World-first Queries). **[engine] convention + token scan in GDScript, permanently** |
| `resolve` sees no Person | **mechanical** — absent parameter |
| no decision function reads the event log | **mechanical** — an AST clause |
| DELIBERATE writes nothing | **mechanical** — the return shape **plus the order-independence test** |
| `witness` never takes a collection | **convention with a named check** — the collection signature is writable in GDScript |
| no write outside the matrix | **mechanical if the write class is a parameter of the store API**; convention otherwise. **Make it a parameter** |
| **no fallback: if no person acts, the social thing does not occur** | **mechanical** once the personnel gate lands — **and it is a ruling, not a preference** |
| a vacant date lapses rather than blocking | **mechanical in CALENDAR** |
| an attempt at `Ob > 2 × Pool` is refused | **mechanical in RESOLVE** |
| eviction never ranks on salience | **mechanical in the comparator** |
| a Knot deposit reuses the event id | **mechanical in the deposit constructor** |
| nothing generates without a demand | **convention** — there is no clock to remove, but nothing stops one being added |
| **no scheduled social recovery** | **STRUCTURAL BY PHASE MEMBERSHIP** — there is no step in which a restoring timer could run, so a design that wanted one **has nowhere to put it** |
| CALENDAR decides nothing | convention |
| **no second resolver, no auto-resolve, no fast path** | **convention — and this is the highest-value conventional cell in the entire design** |
| `sense()` returns exactly two floats | convention — the named residual risk |

## §34.1 · What the loop deliberately does NOT contain

- **No phase in which a container decides.** Every decision has a person's id on it.
- **No phase in which an off-board polity acts without a person.** Off-board pressure enters as an
  **Event**, which is why it needs no phase of its own.
- **No reaction inside a season at person scale.** *"You anticipated, or you are late."*
  ⚠ **But see §40.2 — the seam qualifies this and the design has not reconciled the two.**
- **No hidden turn order.**
- **No step for the three deferred subsystems.** A contest **subdivides** the tick at RESOLVE.

---

# PART IV · SCALE — MACRO TO MICRO

**This Part is the holonic mechanism.** It is the part most likely to be got wrong by analogy with
entity-component systems, actor frameworks or message buses, because all three suggest solutions this
design refuses for reasons that are not obvious until you have seen the failure.

## §35 · The ladder — one type, eight kinds

```
person → hearth → community → settlement → territory → province → duchy → realm
```

**One `Rung` type. Eight `kind` values. The parent relation is a `contain` Tenure edge.**

### §35.1 Why the ladder is data and not a type hierarchy

> **The containment ladder is the module hierarchy IN MEANING** — parent-child in the tree means
> containment in the world, which is what makes it a hierarchy rather than a filing system.
>
> ⚠ **BUT [engine] GDScript's `class_name` namespace is FLAT AND GLOBAL.** There is no
> `Settlement.Person` and `Territory.Person`; there is **one `Person`, project-wide.**
>
> **So the ladder is a DIRECTORY TREE and a `Rung.kind` ENUM. It is not a type hierarchy**, and
> mirroring it in scripts buys nothing while importing collision risk into a design with thirty-plus
> object names.

**What survives, and it is the whole point: one rung type, instantiated at every rung, means a
mechanism written for elites is automatically available to populations.** That is structural in the
**data**, which is where it belongs.

### §35.2 Naming — `Rung`, not `Node`, not `Container`

[engine] **Both `Node` and `Container` are Godot built-ins**, and `class_name Container` collides
exactly as `class_name Node` does. Both fail loudly, in the same way.

### §35.3 Union types have no GDScript representation

`Tenure.subject`, `Claim.source` and `DocketItem.matter` are sums. **The representation is
`(kind_tag: int, id: int)`**, which is also what a struct-of-arrays store wants.

> ⚠ **A STORAGE DISCRIMINATOR IS NOT A RESOLVER BRANCH.** Say so in one line beside it, or the first
> reviewer deletes the tag and the second re-adds it as a class hierarchy.

## §36 · Aggregate-UP — T5, and how demands rise

> **T5: demands aggregate UPWARD and are filtered at a rung — filtered by a NAMED PERSON who pays for
> the filtering.**

### §36.1 The mechanism, end to end

```
a want                 -> Petition(petitioner, proposition, respondent_venue, backing[])
a person CARRIES it    -> `carry` is an ACT, by a named person, costing budget
                       -> DocketItem on a Date
the Date fires         -> a sitting
the sitting decides    -> Events
```

**Every arrow is a person's act or a calendar fact. There is no automatic promotion, no queue drain,
no priority function.** The filter is a person, and **the person pays** — which is why T5 produces
politics rather than a work queue.

### §36.2 What aggregate-up is NOT

| refused | why |
|---|---|
| **a pushed aggregate** | R-1: *"may not receive a pushed aggregate, and may not store one"* |
| **a stored roll-up at each rung** | L3 and §22: **Nobody owns an aggregate** |
| **a summation over per-person tallies** | §22.4 clause 2 |
| **a count over live AND ended edges** | §22.4 **clause 3** — that is a ratchet in disguise |
| **following `tie`/`knot`/`commit` "up"** | those are lateral edges (§6.2); leaving the subtree makes it a resolver-side Query, not an R-1 aggregate |

### §36.3 What it IS

**An R-1 on-demand aggregate over the containment subtree, computed at a barrier, cached read-only
until the next barrier, and discarded there.** Nothing is stored. Nothing goes stale.

## §37 · Refract-DOWN — T6, and how large actions ripple

> **T6: large actions ripple DOWNWARD** — and this is the direction that is most commonly
> mis-implemented, because every instinct says *tree walk*.

### §37.1 The head's mechanism, and it is not a tree walk

```
Dispensation := (id, issuer, proposition, scope, terms[])   -- NINE typed terms, no bare effect field
```

> **"It travels by being noticed, NOT DOWN A CHAIN OF POSTS. Publishing is a `tell`, so it distorts in
> transit, and what reaches the hamlet is often not what the Duke signed."**
>
> **"A published dispensation does not apply — it lands as a compliance contest, per relevant Rung,
> through `contest`, and SCOPE ENUMERATES EXECUTORS, NOT PLACES."**
>
> **"Delivery is not assumed, and an executor who never received it is DISTINCT from one who received
> it and refused."**

### §37.2 Then nothing further is needed

The person's own need, plus capability, plus this new **claim**, yields an opening through the same
`opening_set(person, view)` any act comes through — **now evaluated over changed CLAIMED terms.**
**No one authored an opportunity for anybody.**

### §37.3 Four things this forbids, and each is a tempting implementation

| forbidden | what it would delete |
|---|---|
| **broadcasting a dispensation to all descendants** | T3 and T6 both — everyone would receive identical, undistorted terms |
| **applying a dispensation as a state write** | the compliance contest, and therefore all political friction |
| **a `scope` that enumerates places** | office-clusters with `rung? = null`, which have no place |
| **assuming delivery** | the distinction between *never received* and *received and refused*, which is the whole of enforcement drama |

### §37.4 ⚠ The word "refraction" is used two ways in the chain

R-2 says downward influence is *"emitting a refraction"* — **emitter-side**. But the act vocabulary
puts `refract` at the **receiving** end, beside `comply`, `evade`, `defy`. **The chain has not
reconciled these**, and this document does not pick one: emitter-side and receiver-side distortion
are different games. **§62.** When you implement, pick one, write it down beside the code, and expect
the choice to be revisited.

## §38 · The lateral topology — the half R-1/R-2 do not govern

**§6.2 established that the design has a second, non-tree topology. This section is how to work with
it.**

| edge | reach | access rule |
|---|---|---|
| `tie`, `knot` | Person ↔ Person, **any distance** | **resolver-side Query.** Stored once, on the lower id. The inverse index is owned by Nobody and stored nowhere |
| `commit` | Person → Proposition, **spans rungs freely** | **resolver-side.** This is how a faction crosses three duchies |
| `hold` at distance | Person → Rung outside their subtree | **resolver-side.** This is what annexation *is* |
| Office with `rung? = null` | no containment node at all | **resolver-side.** A Dicastery, a chivalric order, a trans-settlement guild |
| Venue with `container = NONE` | a cluster: **a date and a door** | **resolver-side** |

> ### **THE RULE THAT KEEPS THE TWO TOPOLOGIES APART**
> **R-1's on-demand aggregate composes over the CONTAINMENT SUBTREE ONLY.**
> **Every lateral traversal is a resolver-side Query — `World` first — and is therefore unreachable
> from `choose` by construction.**
>
> This is not a limitation to work around. **It is why a person cannot know their faction's true
> strength**, only what they claim about it (`leaders_as_claimed`, `norm_as_claimed`).

### §38.1 Cyclic by construction — traverse iteratively

The reference graph is **cyclic on purpose**: the conferral path, the containment path, the tie graph
and the claim citation graph all admit cycles.

> ⚠ **Any traversal written as though it were a tree will hang on the NORMAL case, not on an edge
> case.** Use a visited set. **Never recursion.**
>
> ⚠ **[engine] Godot has no cycle collector.** Ids must never become object references in a cyclic
> structure, or the graph leaks. §46.

## §39 · The seam — a contest is the season loop, nested

```
contest : (World, Rung, prize, claimant[], depth, max_depth) -> Event[]
```

**A contest attaches at exactly ONE place — RESOLVE — where a conflict subdivides the tick and runs
the same steps over a smaller person set on a shorter clock.**

> **A battle, a hearing, an examination committee and two brothers arguing over a barn are THE SAME
> CALL with different act vocabularies. That is the entire integration story, and any part of it that
> needs a second story is a defect.**

### §39.1 Every argument is load-bearing

| argument | why it is there |
|---|---|
| `World` **first** | it is a resolver-side call. **Calling it from inside `choose` fails at the call site** |
| `Rung` | a contest happens **somewhere**; judging set, venue and witnesses all derive from it |
| `prize` | what is allocated. **A contest with no prize is a fight scene, and this engine has no use for one** |
| `claimant[]` | **persons, always.** Not factions, not units, not sides |
| `depth`, `max_depth` | **caller-supplied, NO DEFAULT** — §39.3 |

### §39.2 Four lines cross the boundary; a fifth is a leak

1. **loop → subsystem:** the call, when the touch graph says two acts contest the same subject, or an
   act's `contests[]` names one.
2. **subsystem → loop:** **Events**, into the same log, with `causes[]` naming the acts.
   **Not state writes. Not stat deltas applied in place. Events.**
3. **loop → subsystem:** the persons — claimants, capability, marks, stances — **read, never written.**
4. **subsystem → loop:** the outcome's **degree**, from the **one** ladder.

**And the four leaks, each of which was tried somewhere:**

- **No state write from inside a contest** — it would bypass the write matrix, the witness layer and
  the log at once.
- **No second resolver.**
- **No faction parameter** — a battle whose combatants are factions has deleted L1 at the seam.
- **No subsystem-specific key type family** — a contest's outcome is an Event like any other.

### §39.3 The depth cap has NO DEFAULT, for two reasons

1. **No fabricated constant enters the engine.** A default is a number somebody made up, and it will
   be cited later as though it were measured.
2. **[engine] In GDScript, exceeding recursion depth is a CRASH, not a catchable error.** An argument
   that *"a nested instance is an instance"* shows the barrier count survives nesting; **it is not a
   bound.** Exceeding the cap must produce a **typed error result**, checked by the caller.

### §39.4 One ladder, and the only variation is a declared, demote-only veto

**There is one degree ladder for every scale of the game** — four bands read off the **margin**, never
off the obstacle's size. A duel, a debate, a siege and an examination all use it.

> **The one permitted variation:** a subsystem's wrapper may pass an extension that **vetoes an
> Overwhelming and can do nothing else.** It is **injected by the wrapper, never resolved by the
> engine** — the engine does not know which subsystems exist.
>
> **This is the executing precedent for the whole seam: one resolver, subsystem variation by declared
> extension, injected by the wrapper. Whatever a deferred subsystem needs that the general ladder
> does not give it, it DECLARES — it does not FORK.**

**Design the type first, then the hook.** The extension returns a `bool`, so **there is no signature by
which it could promote a band, move the Partial window, touch Failure, or re-derive the ladder.**
The constraint is structural rather than asserted. **If a variation needs a richer return type, it is
an amendment to the one owner — made once, in that file, never a parallel enum in a subsystem.**

⚠ **A five-band ladder exists in the corpus and the owner implements four. A five-band ladder is an
amendment to the one owner, made once. Two ladders is the failure this seam exists to prevent.**

## §40 · Termination, and why no container gets a clock

⚠ **THIS SECTION IS RE-GROUNDED** (§0.2 finding 4). The first revision argued from the barriers and
contradicted itself two sections later.

### §40.1 What the design actually has

**No termination proof.** The head lists as an open debt: *"A termination argument per self-feeding
loop. Four arcs plus the King are spirals; **nothing bounds one.**"* **That debt is CROSS-SEASON** and
no within-tick argument touches it in either direction.

### §40.2 Within a tick, the bound is the CAP, not the barriers

The design **already permits within-tick reaction**: a contest *"runs the same steps over a smaller
person set on a shorter clock"* **inside RESOLVE**, and *"a contest can open a contest."* So
DELIBERATE re-runs inside RESOLVE against a partially-moved world.

> **The bound on that is `max_depth` — caller-supplied, no default — not the barrier count.**

⚠ **The design has NOT reconciled this with *"no reaction inside a season"*** (§34.1). Both sentences
are in the chain. **The honest reading: the season-level map has no reaction; the seam introduces a
bounded one, and the bound is the cap.** §62.

### §40.3 So why no clock?

**Because a per-container clock is a NESTING FORM WITHOUT A CAP ARGUMENT.**

The design's existing rule for nesting forms is a **required, caller-supplied depth cap with no
default**, because a default is a fabricated constant and because [engine] exceeding depth crashes.
**A container that schedules itself has no `depth`, no `max_depth`, and no caller to supply one** —
it is precisely the unbounded form the seam refused, arriving without the argument that made the seam
safe.

**Three further costs, each independent:**

1. **The frozen world is void.** With no shared tick, a `choose` in container A reads a world
   container B's MATTER has already moved (§32 rest 1). **L2 does not catch this** — the person is not
   omniscient, they are reading a world at an *undeclared time*.
2. **The canonical act order is void.** RESOLVE's fold sorts **one global array**; per container the
   sort survives only per container, and there is no global order to fold in (§31).
3. **`causes[]` can no longer be totally ordered by season index**, breaking a log invariant.

> ### **AND THE PARALLELISM A CLOCK WOULD BUY IS ALREADY AVAILABLE WITHOUT ONE.**
> DELIBERATE is a pure map. [engine] `WorkerThreadPool.add_group_task` has existed since **Godot 4.0**
> and is **not version-load-bearing** for this design. **The map is already parallel. The clock buys
> nothing and costs three invariants.**

---

# PART V · MODULARITY — THE CONTRACT DESCENT

## §41 · The descent — what a developer walks to bound a problem

**The problem this solves:** T5 needs to know, per module, what it may *receive*; T6 needs to know what
it may *emit*; R-2's *"no module reaches through another"* is the same requirement as a prohibition.
**No surface in the chain answers it for any module**, which means R-1 and R-2 are today unenforceable
in principle, not merely unenforced.

### §41.1 The spine — four levels, corrected

⚠ **THE FIRST REVISION PROPOSED SIX LEVELS AND TWO OF THE EDGES WERE NOT CONTAINMENT** (§0.2 finding
8). Applying this document's own test — *a LEVEL is a parent: knowing it constrains what the child may
be; an AXIS is an index: it selects nodes without containing them* — two of the six were axes.

```
GAME
 └── MODULE        the unit of work. One provider, one owned-state set, one declared I/O
      └── DECLARED EDGE     (direction, key type) — what it may emit, what it may consume
           └── FIELD             what a key of that type carries, and its bounds
```

**Three levels below GAME, and every parent relation carries meaning:**

| edge | what knowing the parent tells you |
|---|---|
| **game → module** | the complete set of units. There is no intermediate container, because the two candidates are axes |
| **module → declared edge** | **the module's complete I/O surface** — the level a developer reads to work one module without reading the world |
| **declared edge → field** | what a value means and what bounds it |

### §41.2 The axes — indices over MODULE, never parents

| axis | values | why it is an axis and not a level |
|---|---|---|
| **`role:`** | the engine's vocabulary | **The engine names the ROLE; the registry names the MODULE.** Roles belong to the *engine*, not to a subsystem — and one role (`contest`) has **three** providers. Either role sits above subsystem or they collapse; **either horn breaks a tree** |
| **`subsystem:`** | the three deferred systems | ⚠ In the chain "subsystem" means **only** personal combat, social contest and mass battle. **The loop's own modules have no subsystem**, so it cannot be a universal level |
| **`key type:`** | `family.type`, lowercase dotted | **A key type has MANY consuming modules.** Making it a child would duplicate FIELD under every consumer — the exact argument that disqualifies the others |
| **`phase:`** | a **SET** over the six steps | §41.4 |
| **`scale:`** | advisory annotation | §41.3 |

### §41.3 Scale is an annotation, never a level — the load-bearing negative

> **A module is not "a settlement-scale module."** It is registered against a role and runs at whatever
> rungs the step hands it. **Indexing code by scale deletes the property that makes the ladder worth
> having** (§35.1), and **scale-indexed code is scale-divergent code** — invisible until something
> composes across a boundary.

**And the world's containment ladder is a different thing entirely** (§7). Keep them apart.

### §41.4 `phase:` — a SET, and its honest N-line

⚠ **CORRECTED from the first revision** (§0.2 finding 9), twice over.

**It must be a set, not a value.** The write matrix writes `Date` at **CALENDAR and RESOLVE**, and
travel legs at **MATTER and RESOLVE**. The design's own rule is *"A WRITE CLASS IS NOT A PHASE — one
class, two phases."* A module firing dates at CALENDAR and creating them via `convene` at RESOLVE
**cannot declare one phase.**

**And its N-line is weaker than the first revision claimed.** §30.2's store-API write-class parameter
**already makes the matrix check mechanical, per write site** — which is finer than any per-module
declaration. **What `phase:` still buys, honestly:**

| check | survives? |
|---|---|
| *Is this module's declared write lawful?* | ⚠ **weakened** — the store-API parameter does it better and per site |
| *Can its `consumes` ever be satisfied?* | ✅ **survives.** A module consuming a type emitted only at a later step is a **one-season latency** — which is the design's real behaviour, but is today indistinguishable from a wiring bug |
| *Does anything write during DELIBERATE?* | ⚠ **unaskable under a coarser vocabulary**, where MATTER/DELIBERATE/RESOLVE collapse into one column |

> **So `phase:` is worth one check, not three.** Recorded at that strength rather than the first
> revision's.

## §42 · What a module declares

```yaml
module: <name>
role:        <engine-facing name>          # axis
phase:       [<step>, ...]                 # axis, a SET (§41.4)
scale:       [<advisory>]                  # axis, annotation only (§41.3)
consumes:    [{ type: family.type, from: [<module>, ...] }, ...]
emits:       [{ type: family.type }, ...]
owns:        [<the ownership-table rows this module writes>]
resolver:    <strategy label>              # NOT a signature (§42.1)
grade:       ruled | measured | assumption | absent
citation:    <file:line or command>
doc:         <pointer, or null with grade: absent>
```

### §42.1 `resolver:` is a strategy LABEL, not a signature

**Registered roles have mutually incompatible callable shapes.** A declared `consumes`/`emits` edge
list is a **shape precedent, not a wired signature.** Do not generate call sites from it.

### §42.2 `grade:` — the holes must be displayed, not hidden

**A third of the chain's contract surface is not yet an implementable spec.** The answer is not to
wait; it is to make the descent **show** it.

| grade | means | what a reader may do |
|---|---|---|
| `ruled` | a ruling or an in-chain adjudication decides it; the citation is on the row | build on it |
| `measured` | an execution artifact establishes it; the command is on the row | build on it |
| `assumption` | the row exists, nothing backs it | **use it, cite it AS an assumption, never as measured** |
| `absent` ⊕ | declared missing on purpose | **an authoring queue item with a name** |

⚠ **`absent` is this document's coinage**, merging two vocabularies the chain keeps separate
(`grade: measured|ruled|assumption` for values; `status: ruled|unruled|deliberately_absent` for rows).
**Marked rather than passed off as a citation.**

> **THE POLARITY RULE APPLIES HERE TOO: zero evidence maps to the verdict AGAINST the thing being
> measured. A row with no grade does not default to `assumption` — IT FAILS THE EXPORT.** A default
> grade is how an ungraded surface silently becomes a graded one.

### §42.2.1 Never invent a constant — inject it and sweep it

**Where a value is genuinely undecided, the honest state is `grade: absent` and the honest behaviour
is to REFUSE, not to pick a plausible number.** The design has paid for the alternative: an instrument
in the chain hardcoded a condition scale, three band edges, a wear table **with a silent default for
unregistered kinds**, and a confidence value — against a params document whose own first line reads
*"This document proposes NO VALUES"* and which rules that the condition scale is *"never a literal in a
source file."*

> **Where a probe or a build needs a number to run at all:**
> 1. **Inject it** — never a literal in a body, never a silent default.
> 2. **Declare it a harness fixture**, `grade: assumption`, with the injection site named.
> 3. **Run a 3-point sensitivity sweep.**
> 4. ⚠ **A verdict that FLIPS across the sweep is itself a finding**, and a more important one than
>    the verdict.

**And a silent default is the specific thing to refuse.** A wear table that returns `20` for an
unregistered site kind does not fail — it answers, plausibly and wrongly, forever.

### §42.3 The boundary test — what stays code, what stays prose

A thing enters the descent only if it passes **all three**: *(1) a total function from a small
enumerable key domain to plain values, no control flow; (2) changing it needs a design decision but no
new mechanism; (3) validatable without executing it.* **The moment a row wants an `if`, stop — you are
writing a worse programming language in configuration.**

| candidate | verdict |
|---|---|
| `phase:`, `consumes`, `emits`, `owns`, `grade:` | **in** |
| **a resolver's behaviour** | **out — stays code.** It has control flow by definition |
| **`judging_set_rule`** | **out — it is UNSPECIFIED. Configuring an unspecified thing invents it** |
| **rationale, ruling history, worked failures** | **out — stays prose, beside the row it governs** |
| **the write matrix** | **in**, and it is the item with real work |

⚠ **Configuration nothing reads is prose with worse ergonomics.** The chain has a live example of a
config key with **zero readers**.

## §43 · Registration — a registry row, never an import

> **A module is attached by declaring a row that names a role and its provider. The engine names the
> ROLE; the registry names the MODULE; resolution happens by string. A module is swapped by editing a
> row.**

**Resolution happens at BOOT, not lazily at first use.** *"A missing provider is a startup failure
with a name in it, not a `null` three seasons into a campaign."*

> ⚠ **THE ANTI-PATTERN, REFUSED BY NAME.** Loading modules **by bare name** off a path gives those
> modules a **second identity**. **[engine] The GDScript equivalent is `preload()` by a hardcoded path
> from inside a resolver body — the same shape with none of the declaration.**
>
> **The manifest is the seam. A path literal in a body is not.**

## §44 · The wrapper — post-mortem, and what actually survives

⚠ **The first revision of this document proposed a general wrapper layer as the missing object. Three
independent lanes killed it. The post-mortem is kept because WHY it died is the useful part.**

### §44.1 Why it died

**The proposed rule was:** *a Key crossing a rung boundary is either an aggregate (up, to its parent)
or a refraction (down, to its own descendants); nothing else crosses.* **Three fatal objections, each
independently sufficient:**

1. **There is nothing to check.** `Event` carries **no target and no actor** (§19.3). *"The only
   transport the suite defines is a chain of `tell` acts; there is no non-act news transport anywhere
   in the shape."* Observers are computed at WITNESS from presence. **The emitter declares no
   recipient**, so a direction check has no field to read.
2. **The rule contradicts the design.** T6 *"travels by being noticed, not down a chain of posts"*;
   `scope` *"enumerates EXECUTORS, not places"*; venues may be containerless; offices may have
   `rung? = null`. **A Dicastery's dispensation to executors across three duchies is neither
   up-to-parent nor down-to-descendants.**
3. **It was on the wrong tree.** The rule quantifies over *rungs* (the world tree); the wrapper sat at
   a *code*-tree level. **A subsystem has no parent rung and no descendant rungs** (§7).

**And the fix that suggests itself is refused:** *do not add a target field to `Event` to make routing
checkable.* It is the twin of the attribution field the design **deliberately removed**, and removing
attribution is what makes covert action and false attribution expressible.

### §44.2 What survives — the seam's extension injector, and nothing more

**The design already has exactly one wrapper, and it is correct:** the object that, for each of the
three deferred subsystems, (a) is that subsystem's **entry point, resolved by registry row at boot**,
and (b) **injects a declared, demote-only extension** into the one resolver (§39.4).

**Its four properties, which are the general rule for any future one:**

| property | statement |
|---|---|
| **one variation point** | not a policy object with N methods |
| **the TYPE is the bound** | a `bool` return cannot promote a band; the constraint is structural, not asserted |
| **the subsystem's own policy lives there** | the engine keeps only what is general |
| **injection is explicit at the call site** | and passing nothing yields the owner's unmodified behaviour |

### §44.3 What a wrapper is NOT — four nevers

| never | why |
|---|---|
| **holds state** | it becomes a second owner of a value §22 already assigns — the read/write asymmetry hazard by construction |
| **decides** | *"No phase in which a container decides"*; L1 |
| **resolves** | *"a contest is `resolve` at a smaller scale, not a different function"* — a wrapper that computes an outcome **is** the second resolver |
| **drives a clock** | §40.3 |

### §44.4 And routing is a ROW, never a computation

**Which modules receive a key type is a declared edge in the descent (§41.1), never inferred from a
payload.**

> ⚠ **THE CHAIN PAID FOR THIS.** A 114-line regex router *"reconstructing a fact the case author knew
> at authoring time"* produced eleven unreachable probes and a 46% miss rate. **The ruling is: don't
> route — declare.** A wrapper that must interpret a payload to route it has become that router.

---

# PART VI · THE GODOT PORT

## §45 · Project layout

```
res://
  project.godot              # [autoload] — the check surface for §47
  core/                      # THE SIMULATION. Headless. NOT ONE Node in this tree.
    world.gd                 # class_name World, RefCounted — DECLARE THIS FIRST (§45.1)
    person.gd                # class_name Person   (weight >= 1; a cohort IS this type)
    rung.gd  office.gd  site.gd  record.gd  proposition.gd
    tenure_store.gd          # struct-of-arrays rows
    claim_ledger.gd          # per-person packed ledger — rows, not objects
    event_log.gd             # append-only; the invariants of §19
    query.gd                 # class_name Query — static funcs only; resolver-side take World FIRST
    rng.gd                   # the owned versioned mix + per-operation substream factory
    fixedpoint.gd            # the condition scale, the rounding rule, the band compare
    address.gd               # NOT `path.gd` — [engine] Path2D/Path3D exist
    loop/
      season_driver.gd       # class_name SeasonDriver, RefCounted — season(w), four barriers
      calendar.gd  matter.gd  deliberate.gd  resolve.gd  witness.gd  census.gd
    seam/
      contest_resolver.gd    # the base the deferred subsystems extend (§39)
      <subsystem>_wrapper.gd # §44.2 — entry point + extension injector, one per deferred subsystem
    manifest/
      roles.gd               # role -> provider, resolved AT BOOT (§43)
    params/params.gd         # class_name Params — the typed holder, loaded ONCE by the driver
  data/                      # GENERATED .tres only — never hand-authored
  game/                      # presentation. Nodes live here and ONLY here.
    main.tscn / main.gd      # owns a SeasonDriver; renders; UI signals only
  headless/
    headless_main.gd         # extends SceneTree — runs N seasons, prints the world hash, quits
  tests/
```

⚠ **`manifest/` and `seam/<subsystem>_wrapper.gd` are additions to the chain's stated layout**, marked
here as departures rather than smuggled in. Both are §43's and §44.2's homes.

### §45.1 Declare `World` first

**`World` is the object every rule points at and that nobody has written down.** Until it has fields,
*"resolver-side Queries take a `World` first"* is a sentence rather than a signature.

### §45.2 `headless_main.gd` is the execution-artifact factory

**A step is done when this prints a hash somebody looked at** (§0.3, Part X).

## §46 · Type placement

`RC` = RefCounted · `Res` = Resource + generated `.tres` · `value` = built-in value type · `row` = a
record in a store with no per-instance object.

| object | placement | why | cost |
|---|---|---|---|
| **Person** (= cohort at weight > 1) | **RC, ONE class** | interior state, high N, no tree presence. **One class is the only honouring of "no conversion operation"** | reviewers will itch to subclass a cohort — **refuse** (§9.1) |
| **Rung** | **RC** | state, not a widget; **containment is a Tenure edge, never node-parenting** | — |
| **Office · Proposition · Record · Date · DocketItem · Petition · Dispensation** | **RC** | low N, id-referenced, create/destroy-able | per-object allocation at low N — acceptable |
| **Site** | **RC** | `condition` is primary state | every formula reads a scaled int |
| **Tenure** | **row in `TenureStore`** | **the largest N in the design**; per-edge objects make every derivation an O(N) scan and pay refcount traffic **inside the parallel map** | a store API instead of object fields |
| **Claim** | **row in the owner's packed ledger** | ~200 per person; N × 200 allocations is the wrong shape | struct-of-arrays discipline |
| **Event** | **row in an append-only log** | §19 | — |
| **Act** | **RC**, one tick | — | — |
| **View** | **`PackedInt64Array` of ids** | **a view must hold ids, never references** (§18.1) | — |
| **Sensation** | **`Vector2`** | §46.1 | `.x`/`.y` instead of field names |
| **Stores** | **value** — MatterKind id → int | §48 | typed `Dictionary` (≥4.4); fallback packed pair |
| **Envelope** | **value** — `PackedInt32Array` per band | matter does not act | — |
| **Venue · door · MatterKind** | **Res + generated `.tres`** | authored world data | ⚠ **[engine] `load()` returns the CACHED instance — never use `Resource` for a carrier** |
| **Query** | **`static func` on `class_name Query`** | it is not a type | flat namespace — one holder class |
| **World** | **RC, owned by the driver, NEVER an autoload** | §47 | every resolver-side call threads `w` |

> **NOTHING IN `core/` IS A `Node`.** The carriers have no transform, no visibility, no per-frame
> behaviour and no child list, and **the containment ladder is deliberately an EDGE rather than a
> parent pointer.**

### §46.1 `Sensation` as `Vector2` — the strongest row, with its disclosure

[engine] **A built-in value type has no reference-bearing fields**, so *"it cannot be widened into a
masked world"* stops being a convention and becomes **a property the compiler enforces: nobody can add
a third field to `Vector2`.**

**Two qualifications:**

1. The type prevents **widening**, not **substitution** — so fix the convention at the single
   construction site, `sense()`, and document it there.
2. ⚠ **[engine] `Vector2` components are 32-bit floats in a standard build.** A double round-tripping
   through float32 **breaks cross-language threshold parity at the last bits.** Both scalars are
   interior-side, so no world state is at risk — but **define the sensation domain so its values are
   float32-exact** (integer basis points below 2²⁴) and **assert parity in the integer domain.**
   **And `Vector2` must never be reused for a world-state pair.**

## §47 · The autoload rule — the load-bearing rule of the whole port

> ### **THE `[autoload]` TABLE CONTAINS NO SIMULATION STATE AND NO SIMULATION SERVICE.**
> **Target: empty. Permitted ceiling: presentation-only — a UI signal bus, audio. `World` is
> constructed by the driver and passed by parameter. Nothing under `core/` names an autoload, ever.**

**The mechanism is two parts:**

1. **No live world state behind any global name** — no autoload, no `class_name` static, no `res://`
   path that resolves to one.
2. **Every resolver-side Query takes an explicit `World` as its FIRST parameter**, so calling one from
   inside `choose` **fails at the call site for want of an argument.**

> ⚠ **WHAT IS STILL NOT ENFORCED, STATED PLAINLY.** [engine] GDScript has no module system and no
> visibility modifiers, so a determined author can still `load()` a path by string. **The guarantee is
> *unreachable-by-name*, not *unwritable*.**
>
> **Do not restore stronger wording without a mechanism that earns it. A false claim of enforcement is
> worse than none, because it stops the next reader from checking.**

**Two guards are licensed by this document and no others**, because each is load-bearing on the port:

1. **The autoload check** — one test asserting `[autoload]` contains nothing from `core/`.
2. **The token scan** — one test asserting no file under `core/` names a global state identifier,
   **matching by FILE PATH**, not by a token that can be spelled around.

## §48 · Fixed-point arithmetic — closing the last correctness hole

**Why it is not optional:** §32's band gate makes a one-ulp difference **observable as a verb that
exists in one ordering and not another**, and a band-edge crossing is an Event people witness.

- **`condition` as an int on an exported scale.** Never a float, never a literal in a source file.
- **`stores` in whole units.** No fractional matter.
- **Coefficients as integer pairs.**
- **Then the structural test asserts BIT-IDENTITY**, which is the only assertion that can observe the
  failure it excludes.

## §49 · Determinism in GDScript

- **Substreams, never a shared re-seeded generator** (§33).
- **`H` is an owned, versioned mix.** ⚠ **[engine] Never a built-in `hash()`** — its value is not a
  cross-version contract.
- **Stable iteration order.** [engine] Dictionary insertion order is stable in Godot, but **do not rely
  on it for cross-version determinism**; sort by a content-derived key.
- **The content hash over the log is the replay and parity surface.**

## §50 · Save and load

**Snapshot is the save; the log is retained for provenance; replay is a test device.**

⚠ **This is a departure from a plan that specifies log-replay, and it is marked as one.** The reason:
replay-as-load makes every load a full re-simulation, and any non-determinism becomes a corrupted save
rather than a failed test.

## §51 · Parallelism

| step | treatment |
|---|---|
| **DELIBERATE** | **`WorkerThreadPool.add_group_task` over persons.** [engine] Godot **4.0**. This is the one that pays |
| **MATTER** | parallel over Sites and bodies **after** the serial event channel and death cascade (§31.1) |
| **RESOLVE** | **serial.** The ordered fold has one order |
| **WITNESS** | fan-out **serial**; deposit parallel over persons |
| **CENSUS** | parallel over written owners, from one snapshot |

⚠ **Nothing inside a parallel map may build a cache** (§4). Caches are barrier-built only.
⚠ **`Tenure` as rows rather than objects is what keeps refcount traffic out of the parallel map** (§46).

## §52 · The version floor — measured, not assumed

| # | feature | since | used for | fallback | load-bearing? |
|---|---|---|---|---|---|
| 1 | typed `Dictionary[K,V]` | **4.4** | `Stores`, params holder, cardinality tables | `const` name→index map + packed arrays | **yes** — the largest ergonomic win |
| 2 | `@abstract` | **4.5** | parse-time checking of role methods on the contest base | base-body error + **typed error result** — **needed anyway, since [engine] GDScript has no exceptions** | yes, weakly |
| 3 | `WorkerThreadPool.add_group_task` | **4.0** | the parallel DELIBERATE map | identical | **no** |
| 4 | `RefCounted`, `Vector2` as value, `.tres` cache semantics, flat `class_name`, the `Container` collision | all 4.x | everything else | identical | **no** |
| 5 | **any 4.6-exclusive feature** | — | **none is named anywhere in the chain** | — | — |

> ### **NOTHING IN THIS DESIGN NEEDS 4.6. THE HONEST FLOOR IS ≥ 4.4.**
> One thing wants ≥ 4.4 (typed collections) and one wants ≥ 4.5 (`@abstract`), **and the second has a
> fallback that is needed anyway.** The real decision is **4.3 versus ≥ 4.4**. **The holonic
> decomposition adds no version pressure**: its heaviest requirement is 4.0.

## §53 · GDScript hazards — the list to hand a new contributor

| hazard | consequence | mitigation |
|---|---|---|
| flat, global `class_name` | one `Person` project-wide; `Node`/`Container` collide | §35.1–2 |
| no module system, no visibility | `choose`'s purity is unreachable-by-name, not unwritable | §47, token scan |
| no exceptions | a raise-based contract cannot be ported | **typed error results**, checked by the caller |
| recursion depth is a **crash** | a nested contest can kill the process | **`max_depth`, no default**; typed error at the cap (§39.3) |
| `load()` returns the **cached** Resource | shared mutable state through the back door | **never `Resource` for a carrier** (§46) |
| no cycle collector | the reference graph is cyclic **on purpose**; object refs leak | **ids, never references**; iterative traversal with a visited set (§38.1) |
| `Vector2` is float32 | last-bit parity breaks across languages | float32-exact domain; assert in the integer domain (§46.1) |
| IEEE addition is not associative | a verb appears in one ordering and not another | **fixed point** (§48) |
| built-in `hash()` is not a cross-version contract | replay breaks on an engine upgrade | **owned versioned mix** (§49) |

---

# PART VII · THE FOLD-IN — dropped rulings, adjudicated and incorporated

**The chain decided, endorsed or measured 27 things and then lost them** — each at a *later* section
that restates its neighbours without it. The census and its evidence are in
`03_DROPPED_IN_CHAIN.md`; **this Part is only what a read-only adjudication ruled should come back,
and where it lands in the architecture above.**

## §54 · The adjudicated set, in dependency order

**The order is a dependency order, not a priority list.** Item 14 is genuinely upstream: four of the
others are stated over the object it defines.

| # | folded in | verdict | lands at |
|---|---|---|---|
| **14** | **The `Event` record**, mapped onto the log's fields, **with `source_actor` explicitly NOT carried** | **FOLD-IN, sharpened** | **§19** — and it is the one thing to do first |
| **17** | The **contract-tree transport**: one validated parent over authored registries, generated, gated by a blocking round-trip | **FOLD-IN** | **§41–§42.** The descent has no other transport |
| **6** | The **Exposure collision** — three senses of one word, including a need scalar and a per-person tally | **FOLD-IN** | **§22.4** — the registry axis must not be spelled `exposure` bare, or it collides with the need |
| **7** | `transfer`'s precondition `stores(hearth(giver), kind) >= amount`, and restoration's mirrored form `Δ = +(1 − condition) × f(degree) × share` | **FOLD-IN** | **§27.1** — without it the ordered fold's own scarcity claim is false, since a transfer could mint from a negative larder. The mirror gives a dead site a road back |
| **13** | Four blocking gaps dropped from the open register — **the question `q`'s producer** (which makes `assemble(person, question)` unsatisfiable, so DELIBERATE has no entry point), establishment size, **the empty judging set**, the exchange form | **FOLD-IN as `grade: absent` rows** | **§42.2, §62** — with lineage, because one of them re-surfaced two generations later under a new name and uncited |
| **19** | **`disclosure:` as a schema column** — per-field, who may see it and at what granularity | **FOLD-IN, amended** | **§42** — it passes all three boundary tests and makes *"publish every input, never the trigger"* a row check. ⚠ **Amendment:** a hidden grade is admissible **only** for L3-clause-1 registry tallies, and **disclosure rows exist for owned fields only, never for Queries** — an aggregate across holders has no row to publish a band on |
| **21** | **Per-Conviction scarring** — the moral layer's missing motion. Blocks **7 arcs** | **FOLD-IN, amended** | **§9.3.** ⚠ **The amendment matters:** the source says *written at WITNESS*, which breaks two things — the moral layer's WITNESS row is *nothing*, and a scar written there is an Event writing a `(Person, …)` social row, which is L4. **Lawful form: a `(Person, scar[axis])` row, `social: true`, written at RESOLVE in the ACTS class by the outcome that names the person; `axis` on L3's closed registry; crisis is an L5 edge that rewrites an option set and never rolls an outcome** |
| **11** | **Dormant-grievance clearance gated on the holder's own ledger** — *"a row clears when a claim of the satisfying dispensation lands in that holder's ledger"* | **FOLD-IN** | **§28.** Required by the design's own *"It does NOT propagate. News travels"*; an all-holders clear is a broadcast |
| **20** | **A memberless faction's `hold`** — a Proposition may be a `hold` subject and is never destroyed, so a dissolved faction leaves **territory held by a banner nobody carries**, uncontestable because the holder can never appear at a venue | **FOLD-IN, amended** | **§14.2.** ⚠ **Lawful form: `confer` on an object whose holder-Proposition has zero live `commit` edges becomes ELIGIBLE at the Rung's venue; nothing writes `until` — the successful confer does, via the 1-per-object cardinality.** **REFUSED: "write `until` when the last commit reaches zero"** — that is an actorless social write outside the one declared seam (§15.3) |
| **15** | **`Coherence` is read in three places and owned in none** | **FOLD-IN, amended** | **§22** — Person-interior, written only through seam Events, read person-side only; else an `absent` owner row |
| **18** | A **person loader that seeds postless persons**, not only leaders and governors | **FOLD-IN, amended** | **§29.** ⚠ **Adopt the SHAPE — a roster read from a registry row at `grade: assumption` — not the number.** The design's own acceptance test needs a person with **zero `hold` Tenures** and is unreachable until one exists. A world-gen roster is not a clock (§29) |
| **22** | **Jordan's two long-arc trajectories, decomposed into twelve transitions** | **FOLD-IN** | **Part X §61.** ⚠ **The census misquoted the score: the source says FIVE of twelve work today, not eleven.** These are **the only supplied acceptance cases in the whole chain**, and no case runner has ever run one |
| **9** | **Petition multiplicity** — *"a person may put it to several offices"* | **FOLD-IN, unamended** | **§21.** *"No dedup, no 'already before a body' rule — that would be an engine deciding a person's options"* is L1 verbatim. ⚠ **The first revision held a cost clause pending the scene/act question. That hold is LIFTED: spray is ruled allowable (§26.3), so no cost gate is required and none is folded in** |
| **10** | **Petition supersession** — *"relocation, not decay"* | **FOLD-IN, amended** | **§21.** It needs **no new act**: the mechanism is already `ConveningCondition`. **Nothing cancels a petition automatically** |

### §54.1 The close rule the set produces

**Items 9 and 10 do not collide with each other; together they raise a question neither answers, and
the ordered fold answers it:**

> **Petitions never close each other. A matter closes at RESOLVE by scarcity — the second grant hits an
> emptied larder — and at CALENDAR by lapse.**

⚠ **And that answer depends on item 7 landing**, because scarcity-by-fold is false if `transfer` can
mint. **Land 7 before relying on the close rule.**

### §54.2 What was REFUSED, and why

| refused | killing argument |
|---|---|
| **The hook grammar** — *"a guaranteed fire at threshold with a fixed consequence"* | **L5 forbids exactly that**: a crossing *"may never produce an outcome."* **And the N-line is false** — the lawful residue, hooks that *compel*, is already `ConveningCondition` plus act-declared terms (§13.1) plus L5's option-set rewrite |
| **The Parliament Total Victory rider and its promised oracle run** | It writes a faction stat field that L3 forbids and the design deletes. **Running the measurement would measure a mechanism this architecture has no carrier for** |
| **Item 20's second half** (`until` written when the last commit reaches zero) | An actorless write on a social edge outside the one declared seam (§15.3) |

### §54.3 What was STRUCK from the census

**The twelve named argument faults and the stasis ladder** were not silently lost — they were **scoped
out by a declared narrowing** (*the three deferred subsystems are out of scope except at the seam*).
**A declared scoping is not a drop**, and the item fails the census's own fourth test.

### §54.4 If only one thing is done

> **Write `Event :=` and map it onto the log, field by field, with `source_actor` explicitly not
> carried.** The architecture's load-bearing rules are stated over an object with no fields; items 21,
> 11, 20 and 22 all depend on it; and *"compose onto the existing log"* is a decision whose cost the
> chain has never priced, because **one field of that log is forbidden by the design.**

---

# PART VIII · WHAT THIS ARCHITECTURE REFUSES

**A proposal is judged by what it declines.** Each refusal names what pays for it.

| refused | why | what pays |
|---|---|---|
| **a per-container clock** | §40.3 — a nesting form with no cap argument; voids the frozen world, the canonical order, and a log invariant | **nothing.** The DELIBERATE map is already parallel at Godot 4.0 |
| **a container that decides** | §34.1; L1 | nothing — every decision a rung "wants" belongs to a person standing in it |
| **a second resolver, an auto-resolve formula, a fast path** | §27.2 | nothing measured — the seam covers battle, hearing, committee, and two brothers over a barn |
| **a per-subsystem or per-scale key family** | §39.2's fourth leak | nothing — a subsystem varies by a **declared extension** (§39.4) |
| **a general wrapper layer** | §44.1 — three independent lanes; there is no targeted emission to check | nothing. **The seam's injector survives and is the whole of it** |
| **a `target` field on `Event`** | §19.3 — the twin of the attribution field the design deliberately removed | **covert action and false attribution stay expressible.** That is the point |
| **a stored aggregate** | L3, §22 | nothing — the Query is the aggregate |
| **a threshold that fires an OUTCOME** | L1/L5 | 8 of 50 surveyed arcs, honestly |
| **a MATTER-advanced `Record.stage`** | §13.1 — a fourth clock, and an institution's diligence rendered as weather | nothing — act-declared terms do it better |
| **mirroring the ladder in the type system** | §35.1 — [engine] flat global `class_name` | nothing |
| **broadcasting a dispensation** | §37.3 | nothing — the `tell` chain is the mechanism |
| **a "hidden modifier system"** | it is the ratchet plus a visibility rule, N times in different dress. **A registry for it is scripting drift with a registry** | nothing |
| **branching-outcome machinery** | that is an authoring convention over `Record`, not a primitive | nothing |
| **scene-device machinery** | forced dilemmas, letter-versus-spirit compliance, cross-thread interruption are **dramaturgy** — what a designer does with primitives | nothing |
| **a new guard, validator or dashboard** | only two checks are licensed anywhere here (§47), both load-bearing on the port | nothing |

---

# PART IX · WHAT IS OPEN

**Named, not flagged.** Nothing here is escalated: under §0.1's scope the two candidate escalations
both dissolve — the act budget is **ruled** (§26.3) and the log question is **decided** (§19.5).

## §61 · Specification debts — things a developer will hit

| debt | consequence |
|---|---|
| **`judging_set_rule` is unspecified** | **nothing is decided at a sitting.** T5's *"filtered at a rung"* runs straight through it, and §10.2's *"arrangements, not choices"* cannot be confirmed until it is |
| **The `question` `q` has no producer** | `assemble(person, question)` and `view(person, question)` are unsatisfiable — **DELIBERATE has no declared entry point** |
| **WITNESS as specified fans every Event to every person** | nothing said in private is private. **A wrapper does not fix this and must not be presented as fixing it** |
| **No termination argument per self-feeding loop** | four arcs plus the King are spirals; **nothing bounds one across seasons** (§40.1) |
| **`season_factor`'s distribution has no owner** | **this blocks `yield`** (§22.3) |
| **The cohort's construal spread** | the rule is stated; the representation is not |
| **Travel legs have no ownership row** | they are in the write matrix and the churn ledger and in no owner (§22.3, §31.1) |
| **`(Record, …)` and `(Person, exists)` have no Partition rows** | **every Record write is an unmarked cell**; a death write raises under the matrix's own rule (§30.1) |

## §62 · Live design choices — two defensible options, materially different games

| question | the two options |
|---|---|
| **Does a scene equal an act?** | The ruling is *"~5 playable scenes… which may mean ~5 actions"*. **The budget is settled at ~5; the identity is not.** §26.3 |
| **Is refraction emitter-side or receiver-side?** | R-2 says the emitter emits a refraction; the act vocabulary puts `refract` at the receiving end beside `comply`, `evade`, `defy`. **The chain has not reconciled these.** §37.4 |
| **Does "no reaction inside a season" survive the seam?** | The season-level map has none; a nested contest introduces a bounded one. **Both sentences are in the chain.** §40.2 |
| **May a social quantity sink by neglect alone**, as memory already does, and is a person acting on witnessed loss enough to turn that sinking into a crisis? | **Three arcs.** If yes, most of the cost vanishes and no law moves. If no, three arcs lose their engine and the design says so out loud |
| **How much does a dispensation distort in transit?** | T6 says it distorts; **nothing specifies by how much** |

## §63.1 · Accepted states — not debts, and not oversights

**Recorded so a later reader does not mistake silence for an omission, and does not "fix" them.**

| accepted state | ruling / basis |
|---|---|
| **The act vocabulary is thin.** If spending five acts petitioning is an attractive season, there is not yet enough for a character to do | **Ruled acceptable at this stage** (Jordan, 2026-09-01): *"this may point towards the lack of actions available so far for characters to perform, **which is okay at this point**."* ⚠ **Do not close this gap by capping petitions** — §26.3 |
| **Petition spray is allowable** | Ruled. §26.3. **No cap, no dedup, no required cost gate** |
| **`Record` and `(Person, exists)` have no Partition rows** | Known (§30.1). **Rule the row before adding it** |

## §63.2 · Two things a reader should carry about the chain itself

- **A ruling and a landed edit are different events.** The `opening_set` overturn landed in two files
  and not a third; the act-budget ruling was missed by the head's own §4.2 *and* by the audit that
  reviewed it. **When you find a signature that contradicts an adjudication, the adjudication is
  probably right and the file was probably missed.**
- **Prose registers are re-typed; rows are inherited.** Fourteen-plus of the census's items were lost
  at a section restating its neighbours, including five that fell out of a register whose own heading
  says *"stated so no later document can cite this one as though these were closed."* **This is the
  argument for §42's graded rows over any prose list of open items.**

---

# PART X · FALSIFIERS, AND WHAT WOULD MAKE THIS DONE

## §64 · Nothing here runs

**Under `CLAUDE.md` §0.2 a milestone is done when the behaviour EXECUTES.** By that standard **none of
this is done**, and that is the first thing to say about it. This document is a specification; every
claim below carries the test that would show it wrong.

## §65 · Falsifiers

| claim | what would prove it wrong |
|---|---|
| §5 · **H1 is already true** | a `Rung.kind` needing its own type. `person` is the candidate, and §10.2 pre-empts it |
| §6 · **two topologies, and R-1/R-2 govern only one** | show a lateral edge that IS an R-1 aggregate, or a containment operation that is not |
| §19.3 · **`Event` carries no target, by design** | a head mechanism that requires the emitter to name a recipient. **The `tell` chain is what makes this hard** |
| §19.5 · **one log, not two** | a two-log design where an Event in A names an Event in B in `causes[]` and the chain still walks |
| §22.4 · **clause 3 closes the ratchet hole** | an aggregation over live edges only that is still monotone in a quantity no one's ledger holds |
| §26.3 · **the budget is ruled at ~5** | the ruling file saying otherwise. **Checked: it says `~5, NOT 1`, verbatim** |
| §31 · **the per-owner partition** | a step whose body cannot be partitioned by the owner of what it writes and is not RESOLVE's fold or WITNESS's fan-out — **or a fourth MATTER cross-owner operation beyond the three named** |
| §32 · **fixed point is required, not preferred** | a band gate whose comparison cannot observe a one-ulp difference |
| §40.3 · **a clock buys nothing** | a per-container scheme that keeps the frozen world, the canonical order and the season-index invariant **without** a shared tick |
| §41 · **the spine is three levels below GAME** | a fourth relation that is genuinely containment rather than an index |
| §41.4 · **`phase:` is worth one check** | show the store-API write-class parameter cannot do the first check per site |
| §44.1 · **the wrapper is void** | show the head already stops a module emitting past its parent — **if it does, §44 is right for a second reason** |
| §52 · **nothing needs 4.6** | one engine feature this design requires above 4.4 |
| §54 · **the fold-in set is consistent** | two folded items that cannot both land. **§54.1 names the one interaction found and resolves it** |

## §66 · What would make each Part done — execution artifacts, in order

**Each is stated so a reader can check it rather than believe it. The ⚠ ones cannot be satisfied by
writing.**

| # | artifact | proves |
|---|---|---|
| 1 | **`World` declared with fields, and `headless_main.gd` prints a world hash for a seeded empty campaign** | §45.1's signature claim stops being a sentence |
| 2 | **`Event :=` written and mapped onto the log, `source_actor` absent, `causes: [ROOT]` for antecedent-free emissions** | §19, §54.4 — **the first thing to do** |
| 3 | **The autoload check and the token scan, both red on a planted violation, then green** | §47's two licensed guards work in both directions |
| 4 | ⚠ **A seeded 2-season run, twice, byte-identical including the log hash — with `condition` in fixed point** | §32/§48. **A float build must produce a DIFFERENT hash under a reordered fold, or the test cannot observe what it excludes** |
| 5 | ⚠ **The DELIBERATE map run serially and via `WorkerThreadPool`, producing the identical log hash** | §51's parallelism claim, and §32's order independence, at once |
| 6 | **The role manifest resolves at boot; one row's provider misspelled produces a STARTUP failure naming the row** | §43 — not a `null` three seasons in |
| 7 | ⚠ **A nested contest at `max_depth`, returning a typed error rather than crashing** | §39.3 — **[engine] the crash is the thing being excluded, so this test must actually reach the cap** |
| 8 | **`phase:` populated as a set on every module; the exporter prints per-grade counts** | §41.4, §42.2 |
| 9 | ⚠ **One descent, run: print one module's full subtree from the composite alone, and work that module from it** | §41's whole claim. **If the subtree is not enough, the level set is wrong** |
| 10 | ⚠ **The twelve trajectory transitions as executable cases, with the score re-derived** | §54 item 22. **The chain says five of twelve work; a runner has never confirmed it** |

> ### **ARTIFACT 2 IS THE ONE TO DO FIRST, AND ARTIFACT 10 IS THE ONE THAT WOULD SETTLE THE MOST.**
> Everything in Parts I–VI is architecture until something runs it. **Ten is the only one that tests
> the design against what a player is supposed to be able to do**, and it is the only supplied
> acceptance set the chain has.
