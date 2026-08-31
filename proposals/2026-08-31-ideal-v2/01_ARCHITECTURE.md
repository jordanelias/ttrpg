# THE IDEALIZED ARCHITECTURE — v2

## Status: PROPOSED (2026-08-31). **Nothing here has executed.** No simulation was run, no test was
## written, no number was measured. `CLAUDE.md` §0.2 applies in full: **done means it runs, and none of
## this runs.** Every claim below is an argument about text. Where a claim would be settled by
## execution, it is marked as unsettled rather than asserted.

---

## §0 · WHAT THIS IS, WHAT IT MAY DO, AND HOW TO READ IT

**What it is.** The idealized code architecture for Valoria's seasonal loop, shaped to the gameplay
demands rather than to the shape of the documents that preceded it. It is one of three: this document
owns the **primitives and the refusals**; `02_THE_SEASON_LOOP.md` owns **how a season executes on
them**; `03_COMPENDIUM.md` owns **the cross-referenced register of keys, inputs, outputs and terms**.

**What it supersedes, and what it does not.** It supersedes the synthesis brief that preceded it,
which five independent audit runners broke in 12 FATAL, 35 MAJOR and 27 MINOR findings, all accepted.
It does **not** supersede `proposals/2026-08-31-ideal/10_SUPERSEDING.md` (cited `SUP:NNN` throughout).
**`SUP` remains the source of truth for everything this document does not change**, and §10 below lists
every change with its ground. Where this document is silent, read `SUP`.

**Scope.** The seasonal loop. **Mass battle, personal combat and social contest are DEFERRED** — they
attach at one seam, specified at §8, and this document specifies the seam and not the subsystems.
**Argument at a sitting is NOT one of the three.** Parliament, the sitting, the motion and the named
fault are IN scope and are specified at §5.7; a *social contest* in the deferred sense is the nested
exchange loop a contest opens, which is a different object. The brief that preceded this one risked
reading the two as one, and that reading is refused here by name.

### §0.1 · Citation key

| form | resolves to |
|---|---|
| `SUP:NNN` | line NNN of `proposals/2026-08-31-ideal/10_SUPERSEDING.md` — the prior design |
| `REV:NNN` | line NNN of the adversarial review of that design: `proposals/2026-08-31-ideal/`, document **20** |
| `ABS:NNN` | line NNN of `CODE_SHAPE_ABSTRACT.md`, in the **2026-08-31 review directory** under `proposals/_session_provenance/` — the prior design's full inventory |
| `NN:LLL` | line LLL of `proposals/2026-08-29-valoria-from-scratch/NN_*.md` — the seventeen-document suite, read directly |
| a bare repo path | read at the working tree, per `CLAUDE.md` §2 |

### §0.2 · Namespace key — **read this before any cross-reference**

Five id families are in circulation and three of them share token shapes. A reader who does not hold
this table will resolve half the citations in these three documents to the wrong thing.

| family | shape | example | means |
|---|---|---|---|
| **review findings** | `A#`, `B#`, `C#`, `M#`, `O#`, `F#` | `REV`'s `B1`, `M1`, `C13` | a finding in the adversarial review |
| **runner findings** | `F-#`, `M-#`, `m-#`, letter-suffixed | `F-2`, `M-a`, `m-5` | a finding by one of the five audit runners |
| **reserved forks** | `D-#`, `S##` | `D-2`, `S19` | a fork the prior design reserved |
| **module rules** | `R-#` | `R-1`, `R-2` | an architecture rule, `SUP:374`, `SUP:379` |
| **loop steps** | **words only** | `CALENDAR`, `RESOLVE` | a step of the season |

> **THE LOOP STEPS HAVE NO LETTER-NUMBER NAMES.** The prior brief spelled them `B1 … M2` and cited
> review findings `B1` and `M1` seventy-six lines away in the same file. **Two namespaces, one token
> shape, one document.** The steps are named by their words and by nothing else, permanently. The
> legacy phase names `P0 … P7` (`SUP:641-654`) are **retired** by this document and appear below only
> where a `SUP` line is quoted.

### §0.3 · What this document may not do

- **It may not treat itself as mechanism.** `CLAUDE.md` §0.05: prose is reference, code is mechanism.
  Nothing here may be cited as the reason a behaviour is correct. It is an argument for what to build.
- **It proposes no apparatus.** `11_code_shape.md:243-245` forbids *"validators over the design
  documents, freshness checkers, guards on the guards, or any apparatus whose subject is the
  repository's own process rather than the game."* **No validator, guard, register, checker or process
  document is proposed here, and none of the architecture below requires one.**
- **It may not claim a measurement.** Every number below is either quoted from a cited line or is a
  design proposal. Nothing was computed by running anything.

---

## §1 · THE DIAGNOSIS, AND THE SPECIFICATION IT ANSWERS

### §1.1 The diagnosis

The review's surviving verdict, after its own absolutes were broken four times by an independent
reader (`REV:1770-1790`): **the design can change the STATE of what exists, and cannot change WHICH
things exist or WHO HOLDS THEM.** What is confirmed absent in `SUP`, by that review's greps:
creation and destruction of Site, Container and Office (`REV:610-625`); tenure over sites and nodes
(`REV:779-830`); birth; character generation; caused advancement; a faction's leader.

Measured on Jordan's own long-arc trajectories, **five of twelve transitions work** (`REV:286-304`),
and the cut between the columns is exact: *every transition that works is a state change on an object
that already exists; every transition that fails is a change to what exists, or to who holds it*
(`REV:306-309`).

### §1.2 The specification

Jordan stated the loop's intent in five paired flows: *"things can be built or destroyed, people can
be born or die, ideas can be disseminated or purged, demands can aggregate upwards, directives can
propagate downwards — the world is always in flux"* (`REV:25-27`). Plus two constraints on factions:
*"All starting national royal factions may collapse in the game to be replaced with dynamically
generated ones"*, and *"Power is not static — power is something that happens. Factions are only as
strong as the people under their purview"* (`REV:27-30`).

**So the architecture's organising question is: what is the smallest primitive set under which
EXISTENCE, TENURE and STATE are the same kind of change?** The answer is four carriers, one edge, one
act, and one query category — §2.

### §1.3 The coverage map — Jordan's in-scope list, and where each is answered

Nothing in this column is deferred. The three deferred subsystems are named at §8 and appear nowhere
else.

| demanded | answered at | primitive it rides on |
|---|---|---|
| worldly state | §2.1, §5.12 | Container `matter`, Site `condition`, `stores` |
| clocks | §5.12, `02_THE_SEASON_LOOP.md` §2 | `Date`, and the three admitted clock quantities only |
| pressures | §5.12 | need exceeding own reach → petition |
| threats | §5.12 | convening condition — a published band predicate that schedules a date |
| world churn | §5.12 | MATTER, the `condition` accumulator, matter events, the act stream |
| character generation | §5.3 | demographic envelope + the five person-generation triggers |
| event generation | §5.15 | `resolve` emits Events; four decider-free channels and no fifth |
| governance at every scale | §5.8 | address (tree) + remit (office) + commitment (faction) + `hold` |
| advancement | §5.9 | `alter` up on a bounded field, gated by `02:186-189` |
| demotion | §5.9 | `alter` down, `revoke`, and `principals` returning someone else |
| conflict | §3.3 | `contest(container, prize, claimants)` |
| obligation | §5.10 | `oblige` — the seventh `Tenure` kind |
| offices | §2.1, §5.6 | `Office`, `remit`, `conferral`, `establishment` |
| occupations | §5.10 | a stance row whose referent is a Proposition |
| roles | §5.10 | establishment · judging set · carrier · convener · backer · executor · claimant |
| petitions | §5.5 | `Petition`, `carry`, the docket item |
| orders | §5.6 | `Dispensation`, `remit.acts`, one order many executors |
| field investigation | §5.11 | `investigate` — an ordinary act, obstacle composed per `SUP:517-528` |
| parliament, parliamentary debate | §5.7 | the sitting, `determine` at a date, the stasis ladder, twelve faults |
| factions | §2.7 | a Proposition plus the `commit` Tenures pointing at it — derived |
| competing beliefs | §5.14 | one ledger per person; collision at deposit; no consensus type |
| epistemics | §5.14 | `Claim`, five sources, `view`, `salience` |
| memory | §5.14 | the ledger; decay; eviction on clock quantities only |
| truth | §5.14 | no true-profile read; `investigate`; `strike` |
| built / destroyed | §5.1 | `mint` / `efface` on Site, Container, Office |
| born / die | §5.2 | envelope weight in MATTER; individuation in CENSUS |
| disseminated / purged | §5.4 | telling; `strike` at a venue; `efface` a Record |
| demands up | §5.5 | petition → carriage → docket item → sitting |
| directives down | §5.6 | dispensation → notice → per-executor compliance contest |

---

## §2 · THE PRIMITIVE SET

### §2.1 The four carriers — things that exist

```
Person    := (id, address, marks, capability, stance, ledger, ties)
Container := (id, kind, stake[], judging_set_rule, dates[], matter, envelope)
Office    := (id, post, container?, remit, conferral, revocation, establishment,
              dates[], upkeep)
Site      := (id, container, kind, condition, drawers[])
```

**`Container` is the name, and `Node` is refused.** `SUP:337` already calls the object *"Container (a
rung)"* and `ABS:50` carries it forward. `Node` would be a third name for one object — the failure
`CLAUDE.md` §4 records this repository having paid for once — **and it collides head-on with the port
target**: `Node` is Godot's scene-tree base class, written `root (Node)` at
`godot/scene_tree_architecture.md:15`, and `CLAUDE.md` §6 makes the port the live destination. Two
independent grounds, one word, no cost to using it.

⚠ **`Site` IS A CARRIER, and the brief that deleted it is reversed.** The deletion made `Site` matter
held by a Container, keyed the `condition` accumulator to the Container, and derived a coarse
`condition(n)` as a draw-weighted mean. **Three limbs fail, and the third is decisive:**

1. `condition` was declared derived, and a Derived is *never stored* (`SUP:1239-1242` forbids a
   coarser rung storing one) — **but the accumulator reads its own previous value**
   (`SUP:1333-1334`). An accumulator that reads its own previous value is primary state.
2. The draw-weighted mean `condition(n) = Σ condition(c) × draw_share(c, n)` (`SUP:1245`) has **no
   base case** and is not total at a leaf.
3. **Node-keying destroys site identity, and both answers come out wrong.** A settlement holding a
   silted harbour at 0.1 and a healthy seam at 0.9 collapses to one scalar near 0.5, which **keeps the
   bulk-shipping verbs the harbour should have closed and closes the mining verbs the seam should have
   kept.** And `yield(H) = base(H) × condition(site(H))` (`SUP:1396`) and `share(actor, site)`
   (`SUP:1264`) both require sites to have identity.

> **THE RULE, stated once. `condition` is PRIMARY STATE on the Site an act names. Coarser reads are
> derived and stored nowhere. The base case is written: at a Container with no Sites beneath it,
> `condition` is undefined and the verb gate does not fire.** That is `SUP:1240-1242`'s three
> cross-rung rules with the missing base case supplied and the identity kept.

**`Container.envelope`** is the demographic envelope — §2.6. **`Container.matter`** holds `stores`,
the transmission pointer, and the Records kept there (§5.4). **`Office.container?`** is optional and
null is the office-cluster case (`SUP:850-853`); §7's F3 resolution is what makes a null-container
office still carry a clock.

⚠ **`Office` keeps `revocation`.** The prior brief silently dropped it from the nine-field form at
`SUP:416`. `seat_items` is **deleted deliberately**, not dropped — §7's D-2 resolution unifies it with
`capacity(date)`, and §10 records the change.

### §2.2 Identity — how everything is named

**The prior brief declared zero identifier fields across eleven record definitions while consuming
eight id-shaped things it never minted** — `event_id` (`SUP:243`), the knot deposit's reuse of that
same id (`SUP:245-246`), `claim_id…` (`SUP:243`), `claim ids` in `Ground.support[]` (`SUP:1516`),
`act-id` in the conflict tiebreak (`SUP:692`), `actor_id`/`target_id` in the determinism substream,
and `handle` in `told_by(person, handle)` (`SUP:243`). Every carrier, every edge, every Act, Event,
Claim, Date, DocketItem and Record above and below **carries an `id`**.

> **IDS ARE MINTED FROM THE DETERMINISM SUBSTREAM AND FROM NOTHING ELSE.**
> ```
> id(x) = H(world_seed, tick, subject_id, purpose)
> ```
> This is `SUP:607-609`'s per-attempt substream, generalised from `(world seed, tick, actor id,
> attempt discriminator)` so that actorless rolls are covered — and `purpose` absorbs the missing
> subject for a `mint`, whose object does not exist yet.

**One mechanism closes two gaps that were filed separately.** Ids are deterministic, order-independent
and unique **without a shared allocator** — and a shared allocator is exactly the mutable global state
that would break the per-person maps' parallelism licence. There is no id service, no counter, and
nothing to serialise on.

`purpose` is a short discriminator naming the operation and, for a multi-`mint` act, its slot:
`mint:0`, `mint:1`, `yield`, `festering`, `ageing`, `attempt:2`. **`purpose`'s domain is open and its
stability across runs is the determinism requirement** — changing a `purpose` string changes every id
downstream of it, which is the same hazard `SUP:611-613` names for the substream generally.

The executable substrate in this repo already does all of this and is the precedent to copy rather
than re-derive: `Key.id: str` at `engine/substrate/keys.py:145`; uniqueness enforced as invariant 1 at
`keys.py:379-381`; **referential integrity as invariant 3 — a `causes` entry naming an unknown id
raises** (`keys.py:384-388`); cycle-freedom by construction for an append-only log (`keys.py:389-392`);
lookup by id as a first-class operation (`keys.py:363-365`).

### §2.3 The one edge — `Tenure`

**This is the record that carries every disputable political fact in the design** — who holds what, who
is committed at what degree, who contains whom, who owes whom. The prior brief gave it no id, no
owner, no storage and no index, which meant **the record the politics is made of could not be a
`Claim` subject** while the design's whole thesis is that everything is disputable.

```
Tenure := (id, subject, object, kind, since, until?, conferrer?, degree?, payload?)
   subject   ∈ Person | Container | Proposition
   object    ∈ Person | Container | Office | Site | Proposition
   conferrer ∈ Person | Office | null
   kind      ∈ hold | commit | contain | succeed | tie | knot | oblige
```

> **A TENURE IS OWNED BY ITS SUBJECT.** `SUP:337` already files *"`Holding` edges and commitment
> edges"* on the Person row, so this is the shipped placement and not a new owner. One home, one
> writer, no reach-through: **`confer` writes an edge on the subject, and R-2 (`SUP:379-380`) is
> satisfied because only one side stores it.** The object side is an **index**, derived, never stored.

**`until?` is what makes a destroyed tenure a fact.** A revoked tenure is a historical claim subject —
argued over, read for entrenchment, and cited in a succession dispute. Without it, re-conferral after
revocation is indistinguishable from an unbroken tenure, and `entrenchment(h, H) = min(1,
seasons_held / 60)` (`ABS:555`) has nothing to read.

⚠ **`avowed?` is DELETED.** It appeared once, with no producer, no reader and no meaning, and it was
written as an optional flag over a domain that ships **three** states — `avowed · private · covert`
(`ABS:239-240`). Avowal is a property of a `commit` edge and lives in that kind's `payload`.

⚠ **`payload?` is an ADDITION the ruled tuple does not carry, and it is flagged rather than smuggled.**
The eight named fields have no home for `knot`'s `depth ∈ {1,2}` and its **one shared `strain` gauge**
(`ABS:77`), which `bandwidth(k) = max(0, 2 − floor(strain/3))` reads every season (`ABS:502`), nor for
`tie`'s `(familiarity, last_contact, channel_class)` (`ABS:76`). `payload` is the kind's own record,
and `degree?` is retained as a named field because `commit` reads it by name everywhere.

#### The seven kinds

| kind | subject → object | what it is | created by | destroyed by | **cardinality** |
|---|---|---|---|---|---|
| `hold` | Person → Office | office | `confer` | `revoke` | **1 per Office object** |
| `hold` | Person \| Proposition → Site \| Container | enfeoffment, lordship, **annexation** | `confer` | `revoke` | **1 per object** |
| `commit` | Person → Proposition | faction membership at a degree | `commit(+Δ)` | degree → 0 | 1 per (subject, object) |
| `contain` | Person → Container, Container → Container | address; the containment tree | `admit`, `migrate` | **never bare** — see below | **1 per subject** |
| `succeed` | Container → Person | the hearth's succession pointer | a naming act | re-naming | **1 per Container subject** |
| `tie` | Person → Person | ordinary contact | co-presence | decay | 1 per unordered pair |
| `knot` | Person → Person | the deep channel | `form_knot` (`02:399`) | rupture | 1 per unordered pair |
| `oblige` | Person → Person | **kin obligation** | kinship, admission, oath | discharge, death, repudiation | 1 per (subject, object) |

> **CARDINALITY IS DECLARED PER KIND, ON THE SCHEMA, AND THE CONFLICT RULE READS IT.** Two acts
> conflict if they *both `mint` edges that jointly break a declared cardinality* — §2.5. Without this,
> two `succeed` edges on one hearth, two `hold` edges on one office and two `contain` edges on one
> person are **each individually legal, no conflict fires, and the invariant breaks only after both
> resolve.** Declaring cardinality is also the validation point single-parent containment needed and
> never had: an invariant on an edge kind *is* a uniqueness constraint, and a uniqueness constraint
> needs a key.

**`tie` and `knot` are stored ONCE, on the endpoint with the lower id.** A shared `strain` gauge on a
directed record otherwise has two homes and can disagree with itself. The other endpoint reads it
through the derived inverse index.

⚠ **`contain` is never destroyed by a bare `revoke`.** A person's address is *their path to the root*
(`SUP:98`); revoking their `contain` edge orphans them, and revoking a Container's orphans a whole
subtree. **Migration and secession are `confer` to a DIFFERENT parent**, atomically, in one act. There
is no operation that leaves a subject unparented.

⚠ **`annex` and `secede` are NOT verbs and are deleted from the vocabulary.** Zero occurrences in the
prior design's corpus. **Annexation is a `hold` Tenure over a Container changing hands. The tree does
not move.** This is Jordan's own ontology — *"the tree is geography, and allegiance lives in
factions… a hamlet does not move because a King won a war"* (`REV:618-625`) — and the review's rank 1
says outright that *"Re-parenting is not added and should not be — who holds the ground is `Tenure`,
not a parent pointer"* (`REV:628-629`). It is also the better mechanism: it keeps geography and
allegiance as the two objects Jordan separated, and it makes annexation *a conferral by a named person
exercising a remit, public and witnessed, whose subject then complies or does not* through the shipped
compliance contest (`REV:1667-1671`).

⚠ **`secede` is additionally BARRED as a word.** `05:594` ships *secession* for a duke's **defection**
— a `commit` moving away — and one word with two shipped meanings is the exact failure `CLAUDE.md` §4
records. A duke defects (`commit`); a territory changes hands (`hold`); a hearth moves parents
(`confer` on `contain`). Three operations, three words, no collision.

**What the seven kinds buy, in one line each.** Enfeoffment and confiscation are `confer`/`revoke` on
`hold` over a Site. Annexation is `confer` on `hold` over a Container. Kin obligation is `oblige`, and
`requisition` reads it. Deposition is **not an operation at all** — it is `leaders(prop, container)`
returning somebody else. Membership is not holding: `commit` and `hold` are different kinds and stay
different kinds, which is Jordan's distinction preserved rather than collapsed.

### §2.4 The one act

```
Act    := (id, actor, verb, touches[], payload)
touch  := (target, mode, field?, delta?)
target := object_id                                   -- read | alter | exclude | efface
        | spec                                        -- mint only
spec   := (type, kind?, parent, initial[], slot)
mode   ∈ read | alter | exclude | mint | efface
```

**`mint` and `efface` close existence, and they are the review's rank 1** (`REV:1584-1600`). `mint` a
Site is building; `mint` a Container is founding a settlement; `mint` an Office is establishment;
`efface` is each one's inverse. **`mint` a Person is individuation of an existing envelope weight**
(§2.6) — not birth, which is metabolism.

⚠ **`mint` a Proposition is REMOVED.** Three runners hit this independently. A proposition is
**free-form content** (`SUP:1036`) and needs no constructor; the surviving fix is that *uttering a
proposition is part of an ordinary act*, so it is witnessed and a second person can `commit`
(`REV:1727-1728`). **Founding a faction is uttering plus `commit`.** No new object.

⚠ **`efface` may NOT target a Claim in another person's ledger.** R-2 forbids reaching through a
person (`SUP:379-380`), and the review's own rank 6 spends its argument insisting a person's memory
must not be deletable by a motivated process. The purge limb is closed at §5.4 by a different
mechanism, which is better and is shipped rather than invented.

#### `mint`'s three problems, and their one closure

A `mint` entry addresses an object that does not exist, so it cannot carry a reference. It carries a
**spec** instead, and three consequences follow:

1. **The minted id is computable before resolution.** `id = H(world_seed, tick, actor_id, "mint:" +
   slot)`. It is therefore **available to the same act's later `touches` entries** — "make a Container
   of kind Hearth inside C, and let the resulting id be the object of this `contain` edge" — which is
   the output binding the prior brief had no way to express.
2. **A `mint` declares `(parent_of(object), alter)` in its own `touches`.** That is what makes
   `mint` visible to the conflict rule at all: two acts founding a settlement on one spot both `alter`
   the same parent. It also closes the mint-racing-an-efface pair — effacing the parent and minting a
   child inside it now share an object.
3. **Cardinality closes the rest.** Two `mint`s of edges that jointly break a declared cardinality
   conflict, per §2.3.

⚠ **`mint` on a practice rank is WITHDRAWN, and advancement is an `alter`.** A rank is a bounded scalar
field of a `Practice` tuple (`02:153`), not an object. Using one word for *bring an object into
existence* and *raise a scalar* is the non-idempotent meaning `CLAUDE.md` §4 forbids, and it would put
the same operation under two modes with no rule saying which wins.

#### `verb` is a name; `touches[]` is the mechanism

> **THE RESOLVER READS `touches[]` AND NEVER BRANCHES ON `verb`.** A verb is a *bundle* of `touches`
> entries with an eligibility predicate and an obstacle composer. **Adding a verb adds no resolver
> case.**

This is the architecture's answer to a real defect: the prior brief asserted that *"none [of the new
operations] needs a verb that does not already exist in `remit.acts`"* while itself naming at least
nine verbs outside that closed five. **The assertion is withdrawn.** The correct statement is:

- **The verb vocabulary is OPEN**, and it is what a person's practice ladder supplies — rank ≥ 3 adds
  verbs to the option list, rank ≥ 5 adds verbs unattemptable below it (`SUP:504-505`, `02:204-206`).
  A site's band gate removes verbs from it (`SUP:1313`). An office's remit makes verbs eligible where
  they otherwise are not.
- **`remit.acts` is NOT the act vocabulary.** It is the closed set of five acts an **office's remit**
  makes eligible somewhere they otherwise are not: **issue · determine · confer/revoke · dispatch ·
  convene** (`SUP:421-424`). It is unchanged and untouched here. `transfer`, `carry`, `commit`,
  `requisition`, `investigate`, `migrate`, `admit`, `form_knot` and every `mint` are ordinary acts
  available to any person subject to their preconditions, and always were.
- **The MODE set is CLOSED at five**, and that is what keeps the open verb vocabulary safe. The
  resolver's whole behaviour is a function of `(target, mode, field, delta)` — so an open verb list
  cannot grow the resolver, and §14 row 13's ban on a per-entity branch is strengthened rather than
  strained.

#### Commutativity, and the conflict rule

> **COMMUTATIVITY IS A PROPERTY OF THE FIELD, DECLARED WHERE THE FIELD IS DECLARED.**
> `additive` — all writers apply, order-independent: `condition`, `stores`, envelope weights.
> `exclusive` — contested: a succession pointer, an office's remit, an address.
> **The default for an undeclared field is `exclusive`.**

⚠ **`additive` is order-independent ONLY under batching, and the correction is load-bearing.** `clamp`
does not commute with addition at the bounds: applying `+0.3`, `−0.5`, `+0.3` to a `[0,1]` quantity at
0.9 gives three different answers in three different orders if each is clamped as it lands. **The
resolver sums a season's deltas for a field and applies the clamp once.** That is what makes
`SUP:1333`'s accumulator honest and it is what makes the tragedy-of-the-commons shape reachable at
all: without it, all forty `alter` acts on a harbour conflict pairwise and route to a contest.

> **THE CONFLICT RULE.** Two acts conflict iff they share a target and either mode is
> `exclude`/`efface`, **or** both `alter` an `exclusive` field, **or** both `mint` edges that jointly
> break a declared cardinality. Everything else resolves independently. Conflicts route to
> `contest(container, prize, claimants)`. **Ties break on `H(act_id, world_seed)`** — never on rank,
> office or list position, because a rank-ordered tiebreak is a hidden power stat (`SUP:692-694`).

The rule quantifies over a **field**; `touch` therefore carries one. The prior brief stated the rule
over fields and typed `touches` as `(object, mode)`, which made the rule **not computable from the
declared data**. `field?` is null for `read`, `exclude` and `efface`, which touch the object as a
whole.

### §2.5 `Derived` — the query category

A **Derived** is a named pure function over state, **never stored, recomputed on demand**. It is the
formal version of `SUP:340`'s *"Nobody"* row and of R-1's *"compute-on-demand, never push, never
store"* (`SUP:374-377`), and it is what makes several missing objects disappear rather than be built.

⚠ **The word collides with a shipped quantity family and the collision is recorded rather than
renamed.** `engine/engine_params/params_tables.yaml` ships sections named *"Derived Values"* and
*"Derived Scores"*, and `references/glossary.md:75-82` lists their members — Health, Stamina,
Coherence, Composure, Momentum — which are **stored per-character values**. The word means the
opposite thing on the two surfaces. **The mandatory qualifier, which must travel with every use: a
Derived is never stored.** `Query` is the available alternative and is recorded in
`03_COMPENDIUM.md` §7; it is not taken here because the dispositions this document builds on are
written in this word, and a third name for one category is the failure being avoided.

> **THE TABLE HAS A SIDE COLUMN, AND THAT COLUMN IS THE DESIGN'S CENTRAL RULE.** A **resolver-side**
> query may read true state. A **person-side** query may read only the asking person's own ledger.
> The prior brief printed one flat table and erased the distinction — which typed `principals` as a
> **true-profile read, which nobody may perform** (`SUP:124-128`).

| derived | signature | side | range | replaces |
|---|---|---|---|---|
| `faction(prop)` | `Proposition → Set[Tenure]` | resolver | — | a stored faction object |
| `leaders(prop, c, observer)` | `(Proposition, Container, Person) → List[Person]` | **person** | ranked list | a faction leader field. **Deposition = this returning someone else** |
| `presence(prop, c)` | `(Proposition, Container) → count` | resolver | ℕ | faction scale |
| `density(prop, c)` | `(Proposition, Container) → [0,1]` | resolver | fraction of members | faction scale |
| `footprint(prop)` | `Proposition → Set[Container]` | resolver | — | faction scale |
| `sovereign_fraction(root)` | `Container → [0,1]` | resolver | partial (§7 F1) | stored control |
| `condition(c)` | `Container → [0,1] ∪ ⊥` | resolver | draw-weighted mean; ⊥ at a Site-less leaf | a stored coarse condition |
| `verbs(site, c)` | `(Site, Container) → Set[Verb]` | **resolver** | — | **world truth about what is possible** |
| `opening_set(person, view)` | `(Person, View) → List[Candidate]` | **person** | — | an authored opportunity |
| `norm(c, prop)` | `(Container, Proposition) → [−5, +5]` | resolver | member-stance mean over the judging set | a stored norm/unrest/reputation |
| `occupation(p, observer)` | `(Person, Person) → Proposition?` | **person** | — | a profession field |
| `estimated_profile(p, prop)` | `(Person, Proposition) → Profile` | **person** | — | reading true state |
| `eligible(p, verb, c)` | `(Person, Verb, Container) → bool` | resolver | — | `SUP:435` |
| `judging_set(c)` | `Container → Set[Person]` | resolver | — | a stored membership list |
| `draw_share(x, c)` | `(Site \| Container, Container) → (0,1]` | resolver | shares sum to 1 | `SUP:1245` |
| `share(actor, site)` | `(Person, Site) → (0,1]` | resolver | `SUP:1264` | — |
| `capacity(date)` | `Date → ℕ` | resolver | items a sitting processes | the second allowance (§7) |
| `entrenchment(p, obj)` | `(Person, Object) → [0,1]` | resolver | `min(1, seasons_held/60)` | read off `since`/`until` |
| `address(p)` | `Person → Path` | resolver | the `contain` chain to the root | — |
| `regard(p, c)` | `(Person, Container) → scalar` | resolver | member-stance sum | a stored reputation |

**Nothing stores an aggregate. Every one of these is a query, and that is why power is not static.**

⚠ **`presence`, `density` and `footprint` are THREE functions and the prior brief gave them one
signature.** `footprint` takes one argument at `SUP:116`. They are split above.

⚠ **`sovereign_fraction`'s `root` is a distinguished Container the design does not declare an
invariant for.** `SUP:475-478` already rules that a contested succession undefines *the choice of
ROOT, not the function*, so **callers must handle root-plurality and a unique root is a political
condition, not an invariant.**

### §2.6 Populations — the cohort ACTS, the envelope does NOT

⚠ **THIS IS THE WORST ERROR THE PRIOR BRIEF MADE AND IT IS FULLY REVERSED.** It replaced the cohort
with a demographic envelope and made population *matter*. **Matter does not act.** Under that reading
nobody outside a handful of triggers chooses an act, commits to a proposition, or holds anything —
which negates *"every active decision is made by a character"* and **manufactures elite-only politics
by construction**, the exact defect `SUP:205-206` names and the one-type rule exists to prevent. It
also breaks the demand the Faction deletion was built to serve, because every derived faction would be
elite.

> **THERE ARE TWO OBJECTS AND THEY WERE CONFLATED.**
>
> - **A COHORT IS PERSONS, AT COARSE FIDELITY** — one record, a weight, evaluated once, applied to all
>   (`SUP:202-204`). **It acts. One act per cohort per season** (`SUP:628`), and it is **exactly one
>   type with an individuated person** (`SUP:205-206`). Cohorts hold `commit` edges, carry stance, and
>   can be petitioned, levied and roused.
> - **A DEMOGRAPHIC ENVELOPE IS THE INFLOW RESERVOIR ONLY** — counts by age band, marks bundle,
>   capability distribution. It is matter, it does not act, and it is **not** the representation of the
>   living population.
>
> Individuation draws a Person out of a cohort; **the envelope only supplies new weight.**

```
Cohort   := (id, container, weight, marks, capability, stance, ledger, ties)
Envelope := (container, counts_by_age_band[], marks_bundle, capability_distribution)
```

A Cohort is a Person record at weight > 1 — **no conversion operation exists** (`02:555`), which is
what *one type, not two* means mechanically. `View` for a cohort is `K = 3` (`SUP:650`).

⚠ **The ownership claim is this document's, and it is stated as a ruling rather than quoted.**
`09:533` says *"**the world holds** a demographic envelope per containment node"* — the world, not the
Container. **This document assigns it to the Container, as `Container.envelope`,** on the ground that
§4.2's amended Container row already admits matter and only matter (`SUP:355-360`), and *"the world"*
names no owner in the five-owner table. The prior brief wrote *"each Node carries"* and added *"as
matter, not as a social aggregate"*, neither of which `09` says; the quotation is corrected and the
assignment is owned.

⚠ **The five person-generation triggers are ONE OF TWO DECLARED-EXHAUSTIVE ROSTERS, and this document
rules between them.** `09:535-537` gives five churn-side triggers (an event names them · a telling
puts them in someone's ledger · they occupy a role or office · they enter a Knot · they are
individuated as decisive in a contest). `02:573-576` gives five person-generation triggers
(individuation · a succession pointer resolving to an heir who does not yet exist · an admission act
needing a candidate · a petition needing a carrier at a rung with no live person · a view assembly
requiring a subject the observer is looking at), and `02:543-552` gives **four** individuation triggers
(Named · Spread · Divergent view · Capability demand).

> **RULED under `SUP:271-273`'s conflict rule — the document whose declared subject is the object
> wins. Doc 02's declared subject is the person. `02:573-576` is the person-generation roster;
> `02:543-552` is the individuation roster nested inside its first trigger; `09:535-537` is a
> restatement of individuation from the churn side and is subsumed.** Recorded here so nobody
> re-derives it from the other document.

⚠ **The draw is conditioned in two different ways and the prior brief flattened them.** `09:539-540`
reads: *"Minting draws address from the cohort, marks from the cohort plus its variation, **capability
from its distribution conditioned on the naming event**, stance from its aggregate **plus
dispersion**."* Capability is conditioned on the naming event; dispersion applies to stance. Not "from
the envelope plus its dispersion".

### §2.7 `Faction` is not a carrier — and this is an AMENDMENT to the five-owner table

**A faction is a Proposition plus the set of `commit` Tenures pointing at it.** It is entirely derived.
This is the largest deletion in the architecture and it is what makes *"dynamically generated
factions"* fall out rather than be built: **founding a faction is uttering a proposition and one
person committing to it**, and a royal faction collapses when its members' degrees go to zero, with no
lifecycle object anywhere.

⚠ **`Faction` IS one of the five owner rows at `SUP:339`, and deleting it must be stated as an
amendment to that table.** The prior brief presented the deletion as *formalising the "Nobody" row*,
which never mentions Faction. It is not a formalisation; it is a deletion of a row, and the row's
contents have to be re-homed:

| the row held | now lives |
|---|---|
| *its commitment map* | the `commit` Tenures, **owned by their subjects** (§2.3) |
| *its proposition* | **the Person row.** A Proposition is uttered inside an ordinary act, witnessed, and thereafter exists as the referent of the claims and commitments naming it |

> **THE AMENDED OWNERSHIP TABLE — four owners and Nobody.**
>
> | owner | holds |
> |---|---|
> | **Person** | id, address, marks, capability, stance, claim ledger, ties; **every `Tenure` whose subject they are**; the Propositions they have uttered. Everything interior |
> | **Container** | its id, stake(s) · judging set rule · standing dates, each date's `capacity`, and their convening conditions · **and the matter it holds**: `stores`, its Sites, its Records, the transmission pointer, its envelope. **No social aggregate, ever** |
> | **Office** | its id, post, container, remit, conferral, revocation, establishment, upkeep — **and its own standing dates, each date's `capacity`, and their convening conditions** |
> | **Nobody** | aggregates, norms, densities, needs, openings, scale, reputation, **leadership**, **and every row of §2.5** |

⚠ **`subject ∈ Person | Container | Proposition` — and `Faction` as a union member is DEAD.** No kind
uses a Faction subject and Faction is deleted as a carrier. The union member the design actually
promises is `hold | Proposition → Container` — annexation as a tenure changing hands.

⚠ **The stance referent set still names `Faction` as one of four kinds** (`ABS:188`: `Person |
Faction | Proposition | Place`). After this deletion, `Faction` and `Proposition` denote the same
thing. **`Faction` is struck from the referent set; the set is three kinds — `Person | Proposition |
Place` — and `Place` is defined here, because it is defined nowhere in the corpus: `Place = Container
| Site`.** That is a widening the prior work needed and never performed: without it you cannot hold an
attitude toward a harbour.

---

## §3 · THE SIGNATURES

### §3.1 The three, and the one change

```
choose  : (Person, View, Sensation) -> Act        # NO World, ever
resolve : (Act[], World)            -> Event[]    # NO Person
witness : (Person, Event)           -> Claim[]    # per-person; a collection is a type error
```

These are the enforcement mechanism and they work by what they omit (`SUP:142-157`). `choose` has no
`World` — not masked, not read-only, not behind an accessor. `resolve` has no `Person`, so the
resolver acquires no per-actor special case. `witness` takes the person first and **there is no
signature accepting a collection of persons and one event.**

> **`Sensation` IS THIS DOCUMENT'S PROPOSAL AGAINST A PROBLEM THE REVIEW LEFT OPEN.**

⚠ **It is not a corrected version of the review's fix, and the misattribution is the load-bearing
kind.** The review **withdrew** its needs-as-claims fix with **no replacement**, three times over
(`REV:574`, `REV:585-589`, `REV:400-402`), because minting needs as claims made P2 a second root-token
minter and **made hunger evictable**. Calling `Sensation` *"the review's fix, corrected"* converts an
open problem into a solved one. It is offered here as a new proposal and stands or falls on its own.

**The problem, restated.** `SUP:185-190` says subsistence and standing read **the world**; needs are
*"Pure, parallel, never stored"* (`SUP:649`); the Nobody row holds *needs* (`SUP:340`); and the View is
assembled from claims only (`SUP:153-155`). **There is no legal path from a need to the function that
uses it.**

```
Sensation := (subsistence, standing)      -- exactly two scalars
```

⚠ **TWO scalars, not four.** Only subsistence and standing read the world (`SUP:187-188`). Commitment
and exposure read **the view** (`SUP:189-190`) and are therefore computed inside `choose` from the
View the person already holds — they need no channel because they already have one.

**What the record is, and what it is not.** It is computed at MATTER over the frozen world, **never
stored**, **carries no references**, and **answers no query**. `choose` still cannot see the world; it
sees what a body reports. The type now tells the truth the prose already stated.

> **A Sensation is UN-NAMEABLE, THEREFORE UNDISPUTABLE.** No person can hold a claim about another
> person's hunger. Claims reach the **larder** (matter on a Container) and the **body**, and stop
> there. That consequence is written down here rather than discovered later.

**Four attacks that fail.** It is constructible over the frozen post-MATTER world. It re-admits no
omniscience — two floats cannot become a masked world. Nothing is stored, so the Nobody row keeps
*needs*. And the cohort/person one-type claim survives, because a cohort's subsistence and standing are
each a single well-defined scalar.

### §3.2 The belief/truth split — `verbs(site, c)` against `opening_set(person, view)`

`choose` has no `World`, and yet a person must know their options. The prior brief had one function
doing both jobs, and `verbs(site, n) = { v : condition(n) ≥ floor(v) }` (`SUP:1313`) **reads hidden
world state**. The resolution is to split the one name into the two functions it was conflating:

> - **`verbs(site, c)` is WORLD TRUTH, read only by `resolve`.**
> - **`opening_set(person, view)` is BELIEF, computed inside `choose` from the person's own ledger,
>   stance, capability, `Sensation`, and the remits they hold.**
>
> **A person may therefore attempt a verb the world has already removed, and discover the harbour
> silted.**

That is better fiction than a menu that greys out, it needs no new primitive, and `SUP:1218-1221`
already argues for it: *"the people who notice first are the ones whose practice used that verb."*
It is also `opening_set`'s own promise kept — *"exactly one routine, and it is the same routine that
lists any person's available acts at any time"* (`SUP:1134-1135`) — because there is now exactly one
routine on the belief side and exactly one on the truth side, and they are different functions with
different signatures rather than one function with an ambiguous reading.

⚠ **`opening_set` returns CANDIDATES, not Acts.** The prior brief typed it `Person → [Act]`, which
gave one type two lifecycle states with no discriminator. A `Candidate` is `(verb, target_spec[],
believed_obstacle_band)`; `choose` returns exactly one `Act`, constructed from one Candidate.

⚠ **Option availability is RECOMPUTED at CALENDAR, and the prior brief dropped that operation.**
`SUP:647` lists four operations at the calendar step and the fourth is *"recompute option
availability"*. Dropping it silently breaks `SUP:1098-1102`: a suppressed grievance re-arms because its
enabling condition is *"recomputed at P0 like every other option"*. Restored.

### §3.3 `contest(container, prize, claimants)` — the conflict-routing primitive

⚠ **The prior brief deleted it along with the conflict routing, and it is restored.** It is the single
sibling-competition function (`SUP:327`), the destination of every act conflict (`SUP:691`), and the
form a published dispensation takes when it lands (`SUP:1141`). It is **not** the deferred social-contest
subsystem; it is the governance-conflict primitive, and it has three shipped call sites.

```
contest : (Container, Prize, Claimant[]) -> Event[]
Prize   ∈ the container's stake | the regard of its members | one of its offices
        | compliance-here | any object two acts conflicted over
```

**Claimants are always a set of persons with a stake** — the prior design types them as *factions*
at `SUP:327` and as `{enforcement, resistance}` at `SUP:1141`, which are person sets under two
descriptions. Unified here as person sets, with their proposition recorded, because `resolve` has no
Person parameter and must not acquire a claimant-type branch.

**A contest subdivides the tick** (`SUP:658`), opening a nested loop of exchanges over a smaller
person set on a shorter clock. §8 states what that means for the deferred subsystems.

---

## §4 · THE LOOP, IN OUTLINE

Stated here as a primitive; executed in detail in `02_THE_SEASON_LOOP.md`.

```
season(world):
  ── CALENDAR    barrier · global    writes: dates, dockets              class: calendar
  ── MATTER      barrier · global    writes: larders, bodies, travel,
                                             yield, envelope weights     class: matter
     DELIBERATE  map · per person or cohort · PURE
                                     writes: nothing but the returned Act
  ── RESOLVE     barrier · global    writes: everything else             class: acts
  ── WITNESS     barrier · global    fan-out by presence and channel;
                                     then, per person: witness · decay · eviction
                                     writes: that person's own ledger only  class: interior
     CENSUS      global pass         individuation · de-individuation ·
                                     envelope weight                     class: matter
```

⚠ **FOUR global barriers, not three, and WITNESS is one of them.** The prior brief moved WITNESS inside
the per-person map. It is **cross-person by construction** — *"events fan out by presence and
channel"* (`SUP:653`) — so it cannot be. Two runners found this independently.

⚠ **FOUR write classes, not three, and the fourth is stated rather than left unlicensed.**
`SUP:661-678` licenses three by phase — calendar, matter, acts — and leaves the reckoning operations
outside all of them. The **interior** class is the per-person map's licence: *the person's own ledger
and nothing else*. It is safe precisely because it cannot reach anything else, which is a strictly
stronger statement than the prior three-class table makes.

⚠ **A write class is a CLASS, not a PHASE.** Two barriers write the matter class — MATTER (metabolism
and nature) and CENSUS (population bookkeeping). `SUP:669-674` binds class to phase; that binding is
what made the classes look violated every time an operation moved. The classes are unchanged in
membership; only their phase-exclusivity is dropped, with the ground stated.

⚠ **CENSUS exists because the per-person maps DO write globally, and de-individuation is
order-dependent.** Individuation moves envelope weight; de-individuation's predicate reads *other
people's ledgers* (`SUP:209-210`), so X survives or vanishes depending on whether Y's eviction ran
first. **CENSUS reads the post-eviction ledger set ONCE, globally, and settles the population in one
pass** — which is what makes the parallelism claim true rather than asserted.

⚠ **BIRTH IS NOT `mint`, and the prior brief put it in two write classes at once.** Birth and death
move **envelope weights** in MATTER, as metabolism. **`mint` a Person is individuation of a record**,
in CENSUS. One operation per class, and the *"born or die"* flow is answered by the first while
character generation is answered by the second.

⚠ **Eviction ranks on `confidence_live × recency` and on nothing else.** Never on stance-weighted
salience, or motivated *retrieval* silently becomes motivated *deletion* — under stance-ranked
eviction the Templar's exonerating claim is the lowest-salience row in his ledger every season, and
`SUP:262-263`'s *"what is attenuated is retrieval, not value"* stops being true within a few seasons.
Those two quantities are also the only clock-driven ones the design admits for memory (`ABS:280`,
citing `09:562-564`). **The eviction ranking is therefore a DIFFERENT function from the retrieval
ranking** — retrieval's `salience` carries a `relevance(c, q)` term (`SUP:254`) and **`relevance` is
never defined anywhere in the corpus**, while eviction has no question `q` in scope at all.

---

## §5 · WHAT THE LOOP MUST CARRY

Each subsection names the demanded capability, the primitive it rides on, and what — if anything — is
new.

### §5.1 Built and destroyed

`mint` and `efface` on **Site**, **Container** and **Office**, as ordinary `touches` modes: witnessed
by presence, contested where someone objects, resolved in RESOLVE's existing acts class, sized by the
existing degree bands (`SUP:540-546`).

**Preconditions are material, not authorial.** Founding a settlement requires `stores` of the right
`MatterKind` (§7 F2), a `hold` Tenure or standing at the parent Container, and an act. Razing is an
`efface` and is a **contested physical act** against whoever defends it — the `exclude` limb, which
`SUP:1839-1844` records as **not cleared** against the anti-leverage row and which this document
inherits rather than repairs (§11).

⚠ **`efface` on a Container, Office, Person or Site widens the uncleared discrete limb of §14 row 11
by four object classes, and the prior brief left that unremarked.** It is remarked here and carried
open at §11.

**Cascade on destruction is declared, not discovered.** Effacing an object leaves every Tenure naming
it dangling. The rule: **`efface` sets `until = tick` on every Tenure whose subject or object is the
effaced id, and effaces nothing else.** A tenure over a razed settlement becomes a historical fact
that people still argue about, which is correct and is exactly what `until?` was added for. Effacing a
Container additionally requires its `contain` children to have been re-parented in the same act — there
is no orphaning operation (§2.3).

### §5.2 Born and die

**Birth and death are metabolism.** MATTER moves envelope weights: `counts_by_age_band` advances,
births add weight at the youngest band, deaths remove it. This is licensed decider-free exception 1 —
*larders consume, crops yield, wounds close or fester, bodies age* (`ABS:271-273`, citing `09:55-59`).

**A named person's death is the same event at weight 1**, and it is the one place a Person leaves
existence without an act. It fires `until = tick` on every Tenure they held, opens a conferral date at
the horizon its date-holder carries (`SUP:1200-1206`), and — critically — **propagates at telling
speed, not in the same tick**: every standing dispensation the holder issued keeps its terms and loses
its complier *as and when a claim of the death reaches each person* (`SUP:1188-1198`). A withheld
death-notice is therefore one of the most powerful acts in the game.

### §5.3 Character generation

Restored from `09:528-548` and `02:571-578`, with the roster ruling of §2.6.

A Person record is minted, in CENSUS, on any of **doc 02's five triggers**. Minting draws address from
the cohort, marks from the cohort plus its variation, **capability from its distribution conditioned on
the naming event**, and stance from its aggregate **plus dispersion** (`09:539-540`).

**Memory is the trick that makes it consistent** (`09:541-548`): tellings are stored *at the channel*,
not per person, until individuation, so a person minted in season 40 is handed the claims their
address's channels would have deposited, and **draws** from a construal distribution rather than
inheriting a value. Two brothers minted out of one hamlet in one season can hold opposite construals of
the same twenty-year-old proclamation.

⚠ **WHERE THE CHANNEL STORE LIVES IS OPEN, AND THE PRIOR BRIEF'S ANSWER IS WITHDRAWN.** It relocated
the store to the Container as matter, citing the amended Container row. **Three independent grounds
refute that placement:**

1. *"Knowledge lives only in ledgers"* (`SUP:74-75`) — **a Container is no more a ledger than a channel
   is**, so the relocation made it worse, not better.
2. The Container row's own test is *"The line is provenance, not location"* (`SUP:355-360`). **Stored
   tellings ARE derived from persons and DO go stale against them**, so they fail the row's test.
3. **The dormancy ruling already decided this exact move** (`SUP:746-748`): *"a banked claim is a
   claim, and claims live in ledgers; and the alternative is a stored flag on a container, which the
   amended Container row admits only for matter."* The placement is not merely unlicensed; it is ruled
   against.

§14 row 7 independently forbids a knowledge value stored on the thing known. **The channel store is
carried as OPEN at §11.** Character generation works without it — a minted person can be handed nothing
and simply have a thin past — but the *"plausible past"* property `09:544` promises is not delivered
until this is closed.

### §5.4 Disseminated and purged

**Dissemination is shipped and needs nothing.** A telling deposits claims into ledgers by **presence
and channel** (`SUP:1128-1131`). Distortion in transit is free; what reaches the hamlet is often not
what the Duke signed. A person with no post receives it because deposit is never by post.

**The purge limb was broken in the prior brief and the replacement is better because it is shipped.**

⚠ **What was wrong.** It had `efface` remove a *record* and drop confidence *"for everyone whose claim
cites it"*. **No claim can cite a record** — `Claim.source` is closed at four (`SUP:243-245`) and none
is documentary. And its second limb, *"`SAID` claims already make a recantation collide"*, is false:
collision needs *"same subject, same predicate form, **same arguments**"* (`SUP:229`), and
`SAID(A, ¬C, s12)` differs in arguments from `SAID(A, C, s12)`. `SAID` occurs **once** in the prior
design's 2,017 lines; `recant` occurs zero times.

> **THE CORRECTED PURGE. You cannot delete another person's memory, and that is CORRECT — R-2 forbids
> it and the design is right to. What can be destroyed is an idea's STANDING, and the design already
> has the mechanism: `strike`, which *"kills the ground at every venue for everyone"* (`SUP:1540`).**
>
> **IDEAS ARE PURGED AT THE VENUE, NOT IN THE LEDGER.** A struck ground is dead everywhere, publicly,
> by a named person, on a named fault — which is exactly how heresy, attainder and the discrediting of
> a witness actually work. Four of the twelve faults carry `strike`: F5 repetition, F7 rootless
> ground, F10 speaking without standing, F11 incoherent assertion (`SUP:1536-1540`).

**Plus one deliberate addition, argued rather than assumed: a fifth claim source.**

```
Claim.source ∈ firsthand(event_id) | told_by(person, handle) | inferred(claim_id…)
             | firsthand_via_knot(event_id) | documented(record_id)
Record       := (id, container, kind, forgery_quality, subject_matter)
                kind ∈ register | charter | deed | roll | letter
```

**The design already needs it twice.** `admissible_source` is a Venue door — *"a venue that hears
instruments only cannot be reached by forty hamlet witnesses"* (`SUP:1589-1591`) — and *a document's
forgery quality* is a named resistance pool (`SUP:524`). With `documented`, a register is `efface`-able
matter at a Container, forgery has a home, and burning the archive drops confidence **only for claims
that actually cited it** — no reach into any ledger.

⚠ **AND THE CONFIDENCE DROP IS GATED ON A CLAIM, or arson becomes a §14 row 3 broadcast.** Without the
gate, a burned register drops a fjord fisher's confidence in the same tick, six weeks before news of
the fire could reach him. **The drop fires for a holder when a claim that the record is gone lands in
THAT holder's ledger** — which makes arson's effect map onto the news map, exactly as vacancy does
(`SUP:1188-1198`).

⚠ **`witness`'s monopoly on root tokens survives this.** `documented(record_id)` is not a root token: a
person acquires it by **reading the record**, which is an act, resolved into an Event, and `witness`
mints the token from that Event. The source constructor records *what was read*, exactly as
`told_by(person, handle)` records *who spoke*.

### §5.5 The up-stroke — demands aggregate upward

Petition → carriage → **docket item** → sitting. The first, second and fourth are shipped
(`SUP:835-1115`); the third is new and is what the flow was missing.

```
Petition   := (id, petitioner, proposition, respondent, backing[])
              respondent ∈ Container | Office
Date       := (id, holder, form, when, capacity, convener_office?, docket[])
              holder ∈ Container | Office
DocketItem := (id, date, matter, placed_by, placed_at)
              matter ∈ Petition | Motion | Report | Conferral | Determination
```

> **A DOCKET ITEM IS A FIRST-CLASS OBJECT MINTED BY AN ACT.** `carry(person, petition, date)` is an act
> whose `touches` **mints a DocketItem on that Date's `docket[]` and `alter`s the Date**. That is what
> gives a matter a clock, and it is what makes lapse computable: **a petition lapses when the Date its
> item sits on passes without the item being reached** (`SUP:1010-1011`).

**Backing is the aggregation, and it is why there is no crowd object:** *a town's demand* is a petition
with four hundred backers (`SUP:843-845`).

**Standing at an office is standing at the office's Container, or leave from a person who holds it**
(`SUP:877-883`). For an office on a cluster root, which has no Container, standing is membership in the
office's own judging set or establishment, or leave from a member.

**A petitioner may address many offices** (`SUP:913-937`), and they are independent objects — each
carried separately, each expiring separately, none cancelling another. Under §7's one-act ruling,
three petitions cost three seasons of a famine, which is a real price and is what keeps petition-spray
from dominating.

**`compose_agenda` is an act** costing the convener one of his acts, ranking the items *he holds a
claim of* by his own valuation and admitting the top `capacity(date)` — **and an omitted petition is a
DROP and deposits exactly as one** (`SUP:938-1004`). Burial is not free; it is merely safe.

**Termination has three cases and the third is real:** lapse (a date passed) · supersession (a motion,
moved and decided at a venue) · **and at a rootless vacant office it never ends at all**, which is S19
and which §7's F3 resolution closes.

### §5.6 The down-stroke — directives propagate downward

`Dispensation(issuer, proposition, scope, terms)` (`SUP:1121`), with **nine typed terms and no bare
effect field** (`SUP:1123-1125`). **`remit.acts` is the down-stroke's vocabulary**: `issue` a
dispensation, `determine` at a venue, `confer`/`revoke`, `dispatch` (requisition on the
establishment), `convene` (`SUP:421-424`).

**It travels by being noticed, not down a chain of posts.** Publishing is a telling.

**Then nothing further is needed**: the person's own need plus capability plus this new claim yields an
opening through the same `opening_set(person, view)` any act comes through, now evaluated over changed
believed terms. **No one authored an opportunity for anybody** (`SUP:1132-1137`).

**A published dispensation does not apply — it lands as a compliance contest**, per relevant Container,
through `contest` and no second resolver (`SUP:1139-1147`).

**One order, many executors** (`SUP:1149-1183`): scope enumerates **executors, not places**; delivery
is not assumed, and an executor who never received it is *distinct from one who received it and
refused*; **reports are claims, not state**. Under §7's one-act ruling this is paid for out of a budget
that exists: the King spends **one** act — `dispatch` — and thirty-five named people each spend
**theirs** deciding what to do about it.

### §5.7 Parliament, the sitting, and argument

⚠ **This has ZERO mechanism in the brief that preceded this document, and it is neither deferred nor
optional.** It is `SUP:1509-1594`, and it is the resolution layer for everything the up-stroke and the
down-stroke produce.

```
Proposition := (mood, subject, predicate, value, when, scope)   mood ∈ HOLDS | OUGHT
Case        := (id, holder, motion, rung, grounds[])
Ground      := (id, proposition, warrant, support[])            support[] are claim ids
Venue       := (container, prize, standing_date, judging_set_rule, decision_rule,
                admission_floor, privileged_custody, exchange_budget, article_count,
                coupling_depth, veto_holders, record_custody)
door        := (convener, enter, speak, admissible_source, attendance_cost)
```

**A sitting is a Date that has fired.** Its items are DocketItems. **The binding decision at it is
`determine`** — one person's decision at a venue, one of `remit.acts`' five — and every price charged
against it is charged in the one allowance (§7).

**Four stasis rungs, strongest first** — Denial · Definition · Quality · Jurisdiction (`SUP:1525-1527`).
**The position you stand on is what you conceded**, and descending is irrevocable and public.

**Resolution is by named fault against a checklist, not by a persuasion threshold** — which is what
lets the whole thing run headless with no GM. Twelve faults with three severities: `strike` kills the
ground at every venue for everyone; `descend` concedes a rung and **closes nothing**; `close`
force-closes the sitting against the faulting party (`SUP:1536-1542`).

**Exclusion is at the second gate, not the first.** A fisher may walk into the court; he may not
*speak* unless a person with standing carries his petition. **Caste is not a locked door; it is a room
you may stand in silently** (`SUP:1580-1583`).

**Nothing about the sitting is a deferred subsystem.** The deferred *social contest* is the nested
exchange loop `contest` opens (§8); the sitting is a global-barrier operation resolved at RESOLVE like
every other act.

### §5.8 Governance at every scale

Three orthogonal structures, and every rung is governed by all three:

| structure | what it supplies | reaches |
|---|---|---|
| **containment** — a strict single-parent tree | address, jurisdiction, aggregation, the judging set | every rung, Person → Realm (`SUP:96`) |
| **office** — a post whose holder's decision binds persons who never agreed to it | remit, dates, establishment, conferral | any rung, **and clusters with no rung at all** |
| **alignment** — a Proposition plus its `commit` map | allegiance, at any scale, concealable | any scale, no tier field (`SUP:110-133`) |
| **`hold`** — the fourth thing, new here | **who holds the ground** | any Site or Container |

⚠ **The upper rungs owning no state is the architecture working, not a gap.** Political action above
Settlement runs through **factions and offices**, not through container state. What the prior design
lacked was the fourth row: a faction that had won a realm's allegiance **owned nothing, taxed nothing,
garrisoned nothing and could lose nothing but members**. `hold` gives power a material referent, and it
is why annexation now has an object to transfer.

**Single-parent containment is a property of the TREE, not only of Persons** — *"every person has
exactly one parent hearth; every hearth exactly one community"* (`SUP:97-98`). The cardinality
declaration at §2.3 is stated over `contain` subjects generally, which is what closes the prior brief's
accidental licence of a multi-parent graph.

**What breaks if two `contain` edges name one subject, and why nothing errors today:** `presence` and
`sovereign_fraction` leave `[0,1]`, `draw_share` stops summing to 1, and a judging set votes one person
twice — **while the derivation the whole design rests on (`SUP:102-104`) evaporates silently.** The
cardinality declaration is the validation point that was missing.

### §5.9 Advancement AND demotion

**Advancement — restored from `02:186-189` verbatim, not invented.**

> A practice gains a rank when an attempt at a standard **above** its rank resolves **AND** one of: it
> was witnessed by a person holding the practice higher (a master saw it), **or** it failed at a cost
> the person actually paid. **There is no experience clock.**

It is an **`alter` up on a bounded field** (rank 0–5, `02:153`), not a `mint`. It clears §14 row 12 on
**`02:189`'s own words** — *"the precedent's refusal of the scheduled recovery tick applied at person
scale"* — which says it directly and is the citation to use, because row 12 fences itself to
**standing**, a social quantity, and a practice rank is capability.

⚠ **DEMOTION HAD NO LIMB WHILE ADVANCEMENT GOT ONE. This is the inverse gate, and it is this
document's construction rather than a restoration.** It mirrors the shipped gate's structure exactly —
an attempt resolving, plus a two-limb disjunction, and no clock:

> **A practice LOSES a rank when an attempt at a standard at or below its rank resolves at Disaster
> AND one of: it was witnessed by a person holding the practice at least as high, OR the failure cost
> the person a thing they cannot re-acquire within a season. There is no decay clock.**
>
> **Falsifier:** if a rank can fall with no attempt behind it, the scheduled tick is back and this gate
> is wrong.

**Demotion at every other scale needs no new mechanism, and that is the point:**

| lose | mechanism | shipped? |
|---|---|---|
| an office | `revoke` on a `hold` Tenure | yes, `SUP:416`, `SUP:423` |
| your holdings | `revoke` on a `hold` Tenure over a Site | new object, no new verb |
| a territory | the same, over a Container | new object, no new verb |
| the leadership of a faction | **`leaders` returning someone else** — no verb exists or is needed | derived |
| standing | `regard` falling as member stances move | derived |
| your address | `confer` on `contain` to a lower rung — admission's inverse | shipped |
| a practice rank | the gate above | **new** |
| personhood | de-individuation, in CENSUS | shipped, `SUP:209-210` |

**Deposition needs no verb at all.** It is the query returning somebody else, when members `commit`
away from you (`SUP:130`, *"Degree to zero is departure"*) or a rival's raisable backing overtakes
yours. **That is *"power is not static — power is something that happens"* falling out of a query
rather than a mechanism**, which is the strongest form the requirement could take.

### §5.10 Obligation, offices, occupations, roles

⚠ **KIN OBLIGATION WAS DELETED BY THE PRIOR BRIEF and is restored as the seventh `Tenure` kind.**
`SUP:302-304` gives the Hearth *"the obligation edge — kin may `requisition` each other's acts, which
surfaces another person's act as **theirs to refuse**"*. Without it a family has an inheritance
pointer and nothing else, and the first of the five channels open to a postless person — *requisition
kin* (`ABS:264`) — has no edge to walk.

```
oblige : Person → Person       created by kinship, admission or oath
                               read by requisition(obligor, act)
                               destroyed by discharge, death, or repudiation
```

**`requisition` surfaces an act as theirs to refuse — it does not compel one.** Refusal is always
available and is itself an act with consequences in stance. `dispatch` is `requisition` on the
establishment (`SUP:423`) and is the same operation over a different edge.

**Offices** are §2.1's carrier. `establishment` is *the named persons the office employs* — finite,
contested (they can be bribed, killed or turned) and durable (they persist and remember). Under §7's
one-act ruling **the establishment is the office's throughput**, which is what makes it the *"finite,
contested, durable capacity object"* the prior design's own open finding was looking for
(`SUP:409-412`).

⚠ **OCCUPATION IS DERIVABLE IN NEITHER HALF OF THE PRIOR BRIEF'S PROPOSAL** — no term associates a
Practice with the larder, and no per-actor per-site draw is stored. **The repair: occupation is a
stance row whose referent is a Proposition.**

> **`occupation(p, observer)` returns the Proposition *"p is a fisher of Hafenmark"*, read from the
> observer's own ledger like every other faction-shaped reading.** It is a thing you *say you are*, that
> others hold claims about, that can be false, contested, lost and taken up. **No new object, no new
> field, and it is readable by others** — which a `(Practice, Site)` pair computed from private draws
> never was.

**Non-office roles the design already has**, and they are all `Tenure`s, memberships or act-derived:
**establishment** member · **judging set** member · **carrier** · **convener** · **backer** ·
**executor** · **claimant** · **obligor**. The prior review's claim that *"there is no role a person
occupies that is not an office"* was struck (`REV:869-874`); what the design lacked was the
*occupation*, above.

### §5.11 Field investigation

⚠ **The detective seat exists nowhere in the prior design except as one sentence with no verb, no
cost, no obstacle owner and no resolution path** (`SUP:1715-1718`). It is built here entirely from
existing parts.

```
investigate(actor, question, subject) -> Event
   subject ∈ Person | Site | Container | Record | Tenure | Claim
   cost:            the actor's one act for the season
   obstacle:        composed per SUP:517-528 — the concealment of what is hidden, as a
                    resistance pool in the same dice-equivalent unit as a lock's fineness
   degree:          SUP:540-546 decides how much comes back and at what cost
   OUTPUT:          an Event the actor WITNESSES
```

> **`investigate` RESOLVES TO AN EVENT THE ACTOR WITNESSES. It does not deposit claims directly.**
> Otherwise it becomes a second root-token minter alongside `witness`, whose monopoly `SUP:243-245`
> declares. The act resolves; an Event is emitted; the actor is present at it by construction;
> `witness` mints `firsthand(event_id)` into his ledger, exactly as it does for every other act.

⚠ **`spend` is deleted.** The prior brief gave `investigate` a fourth argument naming an unnamed third
capacity quantity, next to a live fork about capacity. Under §7 it costs **the season's one act**, like
everything else.

**The person he questions may lie**, which is a first-class object at `SUP:238`. **This is the only way
the design's central disputable object is ever settled** — *"Settling it requires a named person to go
and look, and that person can be deceived"* (`SUP:1699-1700`).

### §5.12 Clocks, pressures, threats, world churn

**Clocks.** The calendar advances one season per tick. **Exactly three quantities are clock-driven —
matter, bodies, and the confidence of a memory** (`ABS:280`, citing `09:562-564`) — and no fourth may
be added. Standing, regard, grievance and commitment move **only when an act causes an event**.

**Dates.** A `Date` is the design's spine. It is owned by a Container or an Office, carries a
`capacity`, and is scheduled either unconditionally by charter arithmetic or by a convening condition.

**Threats and pressures ride the convening condition, and the prior brief invoked it at one line and
never defined it.** Its tuple:

```
ConveningCondition := (id, holder, predicate, date_form, set_by, set_at)
   holder    ∈ Container | Office
   predicate : pure over the holder's OWN readable state — its stake, the norm of its judging
               set on a named proposition, an R-1 compute-on-demand aggregate over its
               descendants, or the calendar.  PUBLISHED AS A BAND, never as a trigger point
   date_form : (venue, horizon, convener office)
   set_by    : the person whose act attached it
```

**Five provenance rules, unchanged** (`SUP:760-789`): attaching is an exercise of `convene`'s *first*
operation and costs the setter an act · a fired date consumes the convener's allowance and its items
compete for that date's `capacity` · **it decides nothing** · the predicate may read own state, an R-1
aggregate, or the calendar, and never a descendant's stored state or a true faction profile · a vacant
convener may not attach one and does not stop existing ones firing.

**A threat is a published band predicate that schedules an occasion.** A famine coming, a seam running
out, a garrison's arrears compounding, a neighbour's density rising at your border: each is a band over
the holder's own readable state, and each schedules a date at which **a person decides**. **It
guarantees an occasion, not a hearing** (`SUP:791-801`).

**A pressure is a need that exceeds what your own acts can reach**, which is the definition of a
petition's producer (`SUP:842-843`). Pressure is therefore always someone's, and always addressed to
someone.

**World churn** is four channels and exactly four (`ABS:269-277`): metabolism and nature · matter events
(a storm, a silted channel, a worked-out seam, and a band-edge closure under §10.6's three conditions)
· the confidence of a memory decaying · the calendar, **lapse only**. **There is no fifth, and no
threshold that fires an outcome.**

The slow fuses are **act-only**: `condition(site) = clamp(condition + Σ this season's resolved deltas,
0, 1)`, written at RESOLVE and nowhere else, with `base(H)` constant and weather living in `yield`
where it belongs (`SUP:1329-1336`). **A site that decays with nobody touching it must be a matter
event, not a term in the accumulator** — a real narrowing, taken deliberately.

### §5.13 Conflict

§3.3's `contest`. Every act conflict routes to it; sibling competition at every rung is it; a published
dispensation lands as it. **One function, three shipped call sites, no second resolver.**

### §5.14 Factions, competing beliefs, epistemics, memory, truth

**Factions** are §2.7's derived object. **Scale is derived and gates nothing** (`SUP:116-119`): no act
is unlocked or forbidden by a faction's size and no roll takes it as a term. **Nobody may read the true
profile**; every observer holds a different estimate computed from their own ledger, and
underestimation is the default.

**Competing beliefs** need no mechanism beyond the ledger: claims collide *iff same subject, same
predicate form, same arguments, intersecting `when`, incompatible values*, computed at deposit time,
**in one ledger at a time** (`SUP:228-229`). There is no consensus object and no signature that could
build one.

**The predicate vocabulary is CLOSED and the referent space is OPEN** (`SUP:231-234`) — because
collision, entailment and relevance are all functions of the predicate's *form*, and open forms would
make each of them authored per form. ⚠ **The closed vocabulary's actual membership is never
enumerated anywhere; `SAID(…)` is its one worked example.** Carried open at §11.

**Memory** is the ledger, with `view(person, question) → at most K claims`,
`K = 7 + Focus + 2 per Knot consulted − Coherence penalty` (`SUP:251-253`), and

```
salience(c) = recency(c) × confidence_live(c) × relevance(c, q) × stanceweight(c, person)
stanceweight(c) = clamp(1 + λ·agreement(c), 0.05, 2.0),   λ = obstinacy / 5
```

**What is attenuated is retrieval, not value** (`SUP:262-263`) — which is why eviction must rank on a
different function (§4).

**Truth** is what `investigate` reaches, `strike` destroys the standing of, and nothing stores. **The
design has no fact of the matter available to any person**, and that is the point.

### §5.15 Event generation

`resolve` emits Events; every Event carries an `id` and a degree band; `witness` is the only bridge
from an Event to a Claim, and it is per-person. Beyond acts, events arise from exactly the four
decider-free channels of §5.12 and nowhere else. **A band-edge closure is an Event, witnessable by
presence at the site** — it has a place and a season, and everybody else learns by telling
(`SUP:1378-1381`).

---

## §6 · DETERMINISM

```
substream(op) = H(world_seed, tick, subject_id, purpose)
```

Generalised from the shipped `(world seed, tick, actor id, attempt discriminator)` (`SUP:607-609`) so
that **actorless rolls are covered** — `yield`, festering, ageing, weather — and so that **`mint` is
covered**, where `purpose` absorbs the missing subject.

**Consequences, all shipped and all load-bearing** (`SUP:609-615`): showing a player a possibility
cannot change what happens · two attempts resolved in a different order give the same answers · adding
a person somewhere does not re-phase every other roll · **replay is a re-run, not a log, and no
decision function may read the event log.**

**Two die readings exist and are DECLARED:**

| reading | form | used for |
|---|---|---|
| **pool** | N d10; 1–6 nothing, 7–9 one success, 10 two (`SUP:494`) | anything with a performer |
| **magnitude** | `(3 + d10) / 8.5` — range `0.47×` to `1.53×`, mean exactly 1.0 (`SUP:1398-1400`) | nature, which has no skill |

**Three fidelities, one resolver.** Played, witnessed and auto differ only in **who is asked to
choose**, never in how the outcome is computed (`SUP:617-620`).

---

## §7 · THE FORKS, RESOLVED

Each was reserved by `SUP:1858-1874`. All seven are worked here; **one is returned to Jordan and six
are answered**, each with the line that would falsify it.

### D-2 · THE ACT ECONOMY

> **ONE ACT PER PERSON OR COHORT PER SEASON. UNIVERSALLY. No office, rank, or holding changes it,
> ever.**
>
> **An office's throughput is its ESTABLISHMENT's acts** — and every member of an establishment is a
> named person who has exactly one act, their own stance, their own ledger, and the standing option to
> refuse, comply badly, or defect.

**The fork is false because one word was doing two jobs.** *Personal attention* — what you do with your
season — is scarce **identically at every rung**: a Duke has the same hours as a fisher. *Institutional
throughput* — what your office does, performed by the people it employs — is also scarce, but **it
scales with the establishment, not with the holder**. `SUP:434-438` already ships that distinction and
stops one step short of it: *"when an act is performed by remit, the pool is drawn from the
establishment … not from the holder's own capability."*

> **If the POOL for an act by remit comes from the establishment, the ACT does too.** The design
> already moved the dice off the holder and left the act on him.

**It is the personnel game, and it removes the demotion the fork was worried about.** The Duke's
leverage was never more hours; it is that **his one act moves other people's acts**. A fisher's `alter`
moves a boat; a Duke's `dispatch` moves thirty-five seasons. Same allowance, incomparable reach.

**It prices the cohort exploit and turns it into content.** Individuating your cohort to farm acts
gives you eleven *persons* — each with a ledger, a stance toward you, needs of their own, and the
ability to refuse. **You did not buy eleven acts; you created eleven people who might hate you.** No
rule forbids it and none needs to, which matters because §14 row 13 refuses a special case.

**The fourth quantity dissolves.**

> **ONE ALLOWANCE — the act, one per person per season. ONE CAP — items a sitting processes.**

`seat_items` and `capacity(date)` are the same quantity seen from the office's side and the date's
side, which is why the review found `capacity(date)` **double-counted** — spent at `carry`, then used
again as the admission cap at `compose_agenda` (`REV:1712-1720`). **Unify them and the double-count
cannot be written.** `carry` spends the carrier's act; the sitting admits what it can process.
`14:91-92`'s own gloss — *"Holding two offices does not double a day"* — is the one-act rule already,
stated in the vocabulary of hours. **Consequence: the cap on live convening conditions at a holder is
`Σ capacity(d)` over the dates it holds**, replacing `SUP:775-780`'s `seat_items(office)` cap with the
one surviving quantity.

**Three shipped mechanisms stop being in tension.** Multi-petition keeps its scarcity — three petitions
still cost three seasons. A lord paying his retinue no longer eats his own season: he `dispatch`es a
steward and the steward spends the act. And the establishment finally is the finite, contested,
durable capacity object `SUP:409-412` was looking for.

**THE ALTERNATIVE, stated fairly.** Several acts for an office-holder, scaling with rank. It makes the
top of the ladder feel powerful *directly*, needs no establishment roster authored before a Duke is
playable, and matches the convention where a bigger polity does more per turn. **What it costs:**
scarcity is the only thing making refusal, delay and obstruction matter, and it is the same scarcity at
every rung that makes the low end playable — which `SUP:1887-1891` records as a positive result of the testing. A Duke with ten acts does not need his people; he routes around them, and the
establishment, the compliance contest and the whole one-order-many-executors register become
decoration. It also leaves the cohort exploit unpriced, so it must then *forbid* it by rule.

**Not settled by this:** how large an establishment is, who authors the first one, what an office costs
to staff (`upkeep`). **Recommended and not ruled:** an unspent act does not bank — an unspent season is
the design's characteristic outcome, not a resource.

### F1 · CONFERRAL BASIS — person-rooted or office-rooted? **DISSOLVES.**

`Tenure(kind=hold)` carries a `conferrer`, and nothing requires every office to fill it the same way.

> **`Office.conferral` names the basis, PER OFFICE**, and **`conferrer ∈ Person | Office | null`** —
> the one field the fork lives in, now typed.

A warband's oath to its captain is person-rooted and dies with him. A praefecture is office-rooted and
survives its holder. **Both ship, in one primitive, and which one an office uses is world-authoring — a
fact about that institution, not a law of physics.** It is historically exact, and it makes a
military order's warrant *"sworn to the Crown as institution, not the bloodline"* **a contested design
of that order** rather than a global rule, so a faction can try to convert an office from one basis to
the other. That is a political move neither branch offered.

**What it costs:** `sovereign_fraction(root)` is **total only over the office-rooted subgraph**, and
person-rooted chains genuinely terminate at dead conferrers. **Callers must handle a partial answer.**
**Falsifier:** if some caller needs a total sovereignty answer over ALL offices, this fails and one
global basis is forced.

### F2 · IS `stores` THE REALM'S DENOMINATOR? **DISSOLVES into a type parameter.**

The refusal of a second unit needing conversion (`13:285-287`) was correct; the conclusion was wrong.
Keep one *shape* and give it a kind.

```
Stores     := map[MatterKind -> quantity]
MatterKind := (name, perishability, bulk, edible)
```

`transfer` is unchanged and still needs no conversion — it moves a quantity of **one** kind. **grain**
is edible, perishable, bulky: it feeds mouths and cannot cross the realm without spoilage. **silver**
is inedible, imperishable, dense: it **never satisfies `subsistence` directly** and must be exchanged,
which requires a counterparty who wants it.

**Both answers are now true of different things, which is what an economy is.** Force is
logistics-real where wages are grain; money exists where they are silver; and choosing which to pay in
is a real decision. Coin does not return by the back door — it walks in the front, typed, and unable
to be eaten.

**What it costs:** the market path still needs an exchange form — two transfers plus a binding — and
this does not supply one. It makes the market *expressible*, not *reachable*. **Falsifier:** if
`need(subsistence)` can be satisfied by silver anywhere in the model, the kinds have collapsed and this
is one scalar again.

### F3 · S19 — THE ROOTLESS CLUSTER VACANCY. **DISSOLVES.**

It is a defect, and it is caused by an under-specified field rather than by a design choice. Under F1,
`Office.conferral` must name a basis for **every** office. Make that a **completeness requirement**:

> **A conferral rule names a Container, a parent Office, OR THE OFFICE'S OWN JUDGING SET.** The third
> limb is the one that was missing, and it is how conclaves actually work — **a body with no superior
> convenes itself.** The cluster's own members hold the date.

Then the Church that stalls is still fully available as content: the conclave convenes and the men in
the room fail to agree. **A stall by human disagreement is the design working. A stall because no
object holds a date is a hole**, and this closes the hole without closing the story. With M-1's docket
item, the petition filed there now has a dated item and can lapse.

**What it costs:** every office must now carry a well-formed conferral rule, which is authoring work.
**Falsifier, unrepaired:** an office whose judging set is **empty** has no self-convening route either,
so the rule needs a floor and this document does not specify one. Carried at §11.

### F4 · THE COHERENCE-0 ONTOLOGY. **NOT A FORK — a state.**

Coherence is a Person field. At 0 the person **stops generating acts** — a capacity fact — and
**remains a Person record**, because other people's claims about them persist and their ties still
exist. *"Became an object"* is the in-world **reading** of *"no longer acts"*, and the design already
has a machine state for exactly that: **a cohort member is a person who is not currently generating
individual acts.** So Coherence-0 is **de-individuation by a different cause** and needs no new
ontology.

**What it costs:** a Coherence-0 person holding an office **freezes that seat**, and the
vacancy-by-absence rule must reach them or the seat is stuck. **Falsifier:** if anything in the design
must ask *"is this still a person?"* and branch on the answer, this is a real ontological fork after
all.

### F5 · OFF-BOARD POLITIES. **RESOLVES — generate persons, and take no exception.**

An off-board polity is a **Container outside the played region** with an establishment — named persons,
minted from a demographic envelope exactly like any other, at whatever coarse fidelity is affordable.
Their acts arrive as ordinary events and their claims travel by ordinary channels, slowly.

> **`SUP:88-92`'s one-actor rule keeps its NO-EXCEPTION status**, which is worth a great deal: the
> moment one actorless pressure is licensed, every future pressure has a precedent.

**Why it is cheap now and was not before:** it was expensive when persons had to be authored; under
the envelope and mint-on-demand, an off-board realm costs one envelope and a handful of records that
individuate only when someone here hears of them.

**What it costs:** off-board persons are simulated at low fidelity, so their decisions are coarse and a
player who sails there finds a thinner world than home. **Falsifier:** if off-board pressure must
respond to on-board events faster than telling-speed, no person-based model can carry it.

### F6 · IS THE WORLD DYING OR MISUNDERSTOOD? **STAYS JORDAN'S.**

Whether slow material decline is a real trajectory the player must arrest, or a fact everyone reports
wrongly. **This one does not dissolve and should not.** It is not a missing primitive — the machinery
is identical either way. It is a question about **what the game is about**, and the answer changes what
a twenty-season campaign feels like without changing one line of the architecture.

> **That is the signature of a real fork: THE CODE IS THE SAME AND THE GAME IS DIFFERENT.** The other
> six failed that test — every one of them changed the code.

---

## §8 · THE SEAM FOR THE THREE DEFERRED SUBSYSTEMS

Mass battle, personal combat and social contest are deferred by Jordan's ruling. **This document
specifies the seam and nothing else.**

> **THE SEAM IS `resolve`, AND THE MECHANISM IS THAT A CONTEST SUBDIVIDES THE TICK.**
> `SUP:658-660`: *"inside a contest the tick subdivides, opening a nested loop of exchanges over a
> smaller person set on a shorter clock. Fidelity is how deep that nesting individuates and nothing
> else."*

**Consequences, all of which bind the deferred work without specifying it:**

1. **A deferred subsystem re-enters at RESOLVE as a NESTED INSTANCE of the same loop** — the same four
   barriers over a smaller person set on a shorter clock — and **adds no write class.** Its writes are
   RESOLVE's acts class, at the outer tick.
2. **It adds no resolver.** *"A path that computes an outcome without running the same resolver is a
   second resolver whatever it is called, and it will diverge"* (`SUP:618-620`). §14 row 8.
3. **It adds no signature.** `choose`, `resolve` and `witness` are the only three, at every nesting
   depth.
4. **It reports upward as Events, and only as Events.** Whatever happens inside a battle reaches the
   season as events people witnessed, and therefore as claims that can be false.
5. **The three barriers count is not violated by nesting.** A nested instance is an instance, not a
   fourth class — which is what makes *"four barriers, four write classes, exactly"* survive contact
   with the deferred subsystems rather than constrain them.

Nothing else about the three is stated here, and nothing below should be read as a statement about
them.

---

## §9 · §14 — THE FOURTEEN REFUSAL ROWS, WALKED FOR EVERY NEW OBJECT

`SUP:1726-1757` makes this mandatory: *"Every new object … is walked against every row. **'Clear by
gloss' is not clearance**; each row names the object that comes nearest it and says why it does not
cross."* The brief that preceded this document walked **none** of its new objects against **any** row.

**The fourteen rows** (`SUP:1732-1747`, `ABS:283`): 1 a `World` parameter on any decision function · 2
a `view_of(world, person)` that masks rather than assembles · 3 any function taking `[Person]` and one
`Event` · 4 a deposit into a cohort carrying a VALUE rather than a DISTRIBUTION · 5 a pushed aggregate,
or a field one is stored in · 6 a stored aggregate, norm, density, unrest or reputation field · 7 a
knowledge value stored on the thing known · 8 a second resolver, an auto-resolve formula, a fast path ·
9 a `tier`, `level` or `scale` field on a faction · 10 a flat additive modifier from a person onto a
roll · 11 a personal effect on a group that is not a fraction of that group · 12 a scheduled recovery
tick on standing · 13 a per-entity branch anywhere in the resolver · 14 an authored per-person
opportunity or quest object.

**The ten new objects walked below**, each against all fourteen: **`Tenure`** · **`Site` readmitted as
an identity** · **`Sensation`** · **`Derived`** · **`mint`/`efface`** · **the docket item** · **the
demographic envelope** · **`Record` + `documented(record_id)`** · **`oblige`** · **`MatterKind`-typed
`stores`**.

### 9.1 · `Tenure`

| # | verdict and ground |
|---|---|
| 1 | **Clear.** A Tenure is read by `resolve` and by person-side queries over the reader's own ledger. `choose` receives no Tenure set; it receives a View and a Sensation |
| 2 | **Clear.** Nothing assembles a View from Tenures. What a person believes about who holds what is ordinary claims |
| 3 | **Clear.** Conferral is witnessed per person by presence, like any act. No function takes a person set and one conferral |
| 4 | **Clear.** A cohort holds `commit` edges as a *subject*, at one degree, which is a property of that record and not a deposit into it |
| 5 | **Clear.** Nothing pushes a Tenure anywhere. The object-side index is derived on demand and stored nowhere |
| 6 | **Clear, and this is the row the object had to be engineered against.** A Tenure is a **relation**, not an aggregate: `hold` is one edge, not a control number. `sovereign_fraction` is a query over the edge set and stores nothing. Compare the alternative repairs the design refuses — a `territory` field on a faction, a `ruler` field on a Container — each of which *is* a stored aggregate |
| 7 | **Clear.** Who *knows* about a tenure is claims in ledgers. The Tenure carries no confidence, no visibility, and no reader set |
| 8 | **Clear.** `confer` and `revoke` run through `resolve` like every act; the conflict rule routes contested ones to the shipped `contest` |
| 9 | **Clear.** `hold | Proposition → Container` gives a faction an **edge**, not a tier. Nothing about the edge is a level, and no roll takes it as a term |
| 10 | **Clear.** No Tenure enters a roll as an addend. Where holding matters to an attempt it changes **eligibility** and the **pool source** — `eligible(p, verb, c)` and the establishment (`SUP:433-438`) — which is a substitution, not a modifier |
| 11 | **Clear for `confer`/`revoke`; the fraction question does not arise.** A conferral moves one edge, not a share of a group. ⚠ **The nearest strain is annexation:** a single `confer` of `hold` over a Container changes who holds a whole province at one stroke. It is not a personal effect on a group — it is a change to one edge, and **the group's compliance is a separate per-person contest at every relevant Container** (`SUP:1139-1147`), which is exactly the fractionation the row asks for |
| 12 | **Clear.** No Tenure field moves on a clock. `since` and `until` are stamps, not accumulators, and `entrenchment` is **read off** them rather than ticked into anything |
| 13 | **Clear.** Seven kinds, each a rule over a type. No kind names an entity, and the resolver branches on `mode`, never on `kind` — cardinality is data on the schema, not a case |
| 14 | **Clear.** A tenure is not an opportunity. What it changes is `eligible`, which feeds the same `opening_set` every act comes through |

### 9.2 · `Site` readmitted as an identity

| # | verdict and ground |
|---|---|
| 1 | **Clear.** `verbs(site, c)` is **resolver-side by construction** (§3.2) and is the reason the split exists: `choose` sees `opening_set(person, view)`, which reads belief |
| 2 | **Clear.** A person's belief about a harbour is claims about it. Nothing masks a Site into a View |
| 3 | **Clear.** A band-edge closure is an Event witnessed **per person, by presence at the site** (`SUP:1380-1381`) |
| 4 | ⚠ **NOT CLEARED, and the gap is inherited rather than introduced.** Where a **cohort** witnesses a closure, `SUP:1737`'s rule requires the cohort's claim to store *"the construal spread its members would have produced"*, and it never says where that spread lives, what produces it, or what an individuating member draws from. The review could not close it inside the design's refusals and neither can this document. §11 |
| 5 | **Clear.** Coarser conditions are computed by the draw-weighted mean and **stored nowhere**; the primary scalar lives at the Site an act names |
| 6 | **Clear.** `condition` is **matter**, not an aggregate of persons — it exists whether or not anybody believes in it. `SUP:355-360` is the general line and the Container row owns it |
| 7 | **Clear.** A site's condition is a physical fact, not knowledge of one. Who knows the harbour has silted is claims in ledgers, and the scalar is readable by nobody — only the band is published |
| 8 | **Clear.** A Site resolves nothing. Acts touch it through `alter` and `exclude` |
| 9 | **Clear.** Untouched. The faction that forms out of a lost verb is an ordinary proposition plus commitments |
| 10 | **Clear.** Damage never enters a roll as a term. Where a site's condition must reach an obstacle it enters as **the band's representative value**, which is a substitution of the pool source (`SUP:1356-1360`) |
| 11 | **The `alter` limb is CLEAR and is what the sizing rule exists for.** `Δ = −condition × f(degree) × share(actor, site)` is a degree-scaled fraction sized by the actor's own share, and **falls as the number of drawers rises**. At `share = 1` there is no group. ⚠ **The `exclude` limb is NOT CLEARED** and is inherited from `SUP:1839-1844`: one person destroying an undefended shared thing is bounded only by the `contest` against whoever defends it, and where nothing defends it there is no bound |
| 12 | **Clear, on the row's own subject.** The row governs **standing**, a social quantity. `condition`'s only non-act term is `season_factor`, which is weather and lives in `yield`, not in the accumulator |
| 13 | **Clear.** Any site may lose a verb. No branch names one |
| 14 | **Clear, and improved.** A lost verb reaches a person through the same computed `opening_set` any dispensation reaches them through. Nothing is authored for anybody |

### 9.3 · `Sensation`

| # | verdict and ground |
|---|---|
| 1 | **Clear, and this is the row it was built for.** `Sensation` is **two floats**. It carries no references, answers no query, and cannot be widened into a masked world — that is the whole of the argument, and it is checkable by reading the type |
| 2 | **Clear.** It is not a View and cannot be coerced to one; it is computed at MATTER and passed beside the View, not inside it |
| 3 | **Clear.** It is per-person, computed in the per-person map, and no signature takes a set of persons and one Sensation |
| 4 | **Clear.** A cohort's subsistence and standing are each a single well-defined scalar over one record at one weight — no distribution is required because no distribution is lost |
| 5 | **Clear.** Nothing is pushed and nothing is stored; it exists for the duration of one `choose` call |
| 6 | **Clear.** `standing` is *regard among your siblings-in-container*, computed on demand from member stances at the moment of asking. **The Nobody row keeps `needs`** because nothing holds them |
| 7 | **Clear.** It is not knowledge and is not stored on anything |
| 8 | **Clear.** It resolves nothing and decides nothing; it is an input to `choose` |
| 9 | **Clear.** Untouched |
| 10 | **Clear.** It is not a roll term. It ranks motives inside `choose` and never reaches `resolve` |
| 11 | **Clear.** It is one person's own body reporting to that person. There is no group |
| 12 | ⚠ **The nearest strain, and it clears on the row's own subject.** `standing` is a social quantity, and the row bans a **scheduled recovery tick** on one. `Sensation` schedules nothing: `standing` is **recomputed** each season from live member stances, which move only when acts cause events. **A recomputation is not a tick** — no value is added to a stored quantity on a clock, because no quantity is stored |
| 13 | **Clear.** Two fields, computed identically for every person and cohort |
| 14 | **Clear.** It is a motive, not an opportunity. Opportunities come from `opening_set` |

### 9.4 · `Derived` (the query category)

| # | verdict and ground |
|---|---|
| 1 | **Clear, and the side column is what makes it so.** A **person-side** Derived may read only the asking person's ledger. A **resolver-side** Derived is never in `choose`'s scope. The prior brief's flat table erased this and typed `principals` as a true-profile read |
| 2 | **Clear.** No Derived constructs a View; `view(person, question)` is itself person-side and assembles from claims |
| 3 | **Clear.** No Derived takes a person set and an Event |
| 4 | **Clear.** No Derived deposits anything anywhere; the category is defined by writing nothing |
| 5 | **Clear.** The category **is** the answer to this row: compute-on-demand, never push, never store (R-1, `SUP:374-377`) |
| 6 | **Clear, and it is the row the category exists to satisfy.** `norm`, `density`, `regard` and `presence` are queries precisely so that no field holds them |
| 7 | **Clear.** `estimated_profile` reads the reader's ledger and writes nothing to the thing known |
| 8 | **Clear.** A Derived returns a value; it resolves nothing and has no outcome |
| 9 | **Clear.** `presence`, `density` and `footprint` are queries. **No field on any faction-shaped object holds a scale**, because there is no faction-shaped object |
| 10 | **Clear.** No Derived is added to a pool. Where one reaches an attempt it is as a **resistance pool** composed on demand (`SUP:530-535`) or as a band representative |
| 11 | **Clear.** A query has no effect at all |
| 12 | **Clear.** No Derived is stored, so nothing can be ticked into one |
| 13 | **Clear.** Each is one function over a type |
| 14 | **Clear.** `opening_set` is the row's own named alternative to an authored opportunity |

### 9.5 · `mint` and `efface` (the two new modes)

| # | verdict and ground |
|---|---|
| 1 | **Clear.** A mode is data on a `touch`. `choose` constructs the Act from a Candidate; it does not consult the world to know whether the mint will succeed, and a mint may fail |
| 2 | **Clear.** Neither mode builds a View |
| 3 | **Clear.** A founding, a razing and an establishment are each witnessed per person by presence |
| 4 | **Clear.** Neither mode deposits into a cohort. `mint` a Person **draws from** a cohort, which is the row's own licensed direction |
| 5 | **Clear.** Neither pushes anything. A minted object's id is computed from the substream, not allocated by a service |
| 6 | **Clear.** Neither creates a field that holds an aggregate |
| 7 | **Clear.** ⚠ **The nearest strain was `efface` on a Claim, and it is REMOVED** (§2.4): a claim lives in another person's ledger and reaching it violates R-2 |
| 8 | **Clear.** Both resolve in RESOLVE's existing acts class, through the same resolver, sized by the same degree bands. **No fast path and no auto-resolve** |
| 9 | **Clear.** Neither mode touches a faction, which has no fields to give |
| 10 | **Clear.** Neither enters a roll. What varies with degree is the *magnitude of the effect*, per the shipped bands |
| 11 | ⚠ **`mint` is CLEAR; `efface` is NOT CLEARED and the widening is stated.** `efface` on a Container, Office, Person or Site extends the uncleared discrete limb of this row by four object classes. `SUP:1839-1844` already inherits the shape from #342's willingness table pricing `burn` as a severity; **this document declines to invent a bound for a case the design has decided to allow, and records the widening rather than passing over it.** §11 |
| 12 | **Clear.** Neither is scheduled, and neither touches standing |
| 13 | **Clear, and it is the argument for the modes over the alternative.** Every alternative is an authored subsystem — a birth system, a construction system, a founding system — each a top-level special case. **Two modes on an existing tuple close five gaps as a property of the act primitive** |
| 14 | **Clear.** A minted object reaches other people through their own `opening_set`, recomputed at CALENDAR |

### 9.6 · The docket item

| # | verdict and ground |
|---|---|
| 1 | **Clear.** Minted at CALENDAR or by `carry` at RESOLVE. `choose` sees a docket only as claims about it |
| 2 | **Clear.** A person's belief about what is on the agenda is claims; **the convener himself composes from *"the petitions he holds a claim of, not the petitions that exist"*** (`SUP:944-946`) |
| 3 | **Clear.** The deposit on backers is *"as and when they learn"* (`SUP:949-950`) — a telling each, never a broadcast |
| 4 | **Clear.** Nothing is deposited into a cohort by placing an item |
| 5 | **Clear.** The item is on the Date, which the Date's holder owns. Nothing is pushed anywhere |
| 6 | **Clear.** It is a scheduling fact, not a social aggregate. Compare the alternative it replaces — a *priority score* on a petition — which would be one |
| 7 | **Clear.** The item carries no knowledge value about the matter |
| 8 | **Clear.** It resolves nothing; it gives a matter a clock |
| 9 | **Clear.** Untouched |
| 10 | **Clear.** No roll reads a docket |
| 11 | **Clear.** Placing an item is one act on one date. Its effect on the backers is per-person and epistemic |
| 12 | ⚠ **The nearest strain, and it clears.** Lapse is a **date passing**, not a recovery tick, and it is the design's **one licensed decider-free ending** (`SUP:1010-1011`, `ABS:277`). Nothing recovers; a matter dies |
| 13 | **Clear.** Any date may carry any item |
| 14 | **Clear.** An item is a matter somebody carried, not an opportunity authored for anybody |

### 9.7 · The demographic envelope

| # | verdict and ground |
|---|---|
| 1 | **Clear.** Read at MATTER and CENSUS, never inside `choose` |
| 2 | **Clear.** It is not a View and never enters one |
| 3 | **Clear.** It fans nothing out |
| 4 | ⚠ **The nearest row, and the reason the envelope is NOT the population.** The row forbids a deposit into a cohort carrying a value rather than a distribution. **The envelope is not a cohort and receives no deposits** — it holds counts and distributions, and what it emits is a **draw** (`09:539-540`), which is the row's own licensed shape. It is because the prior brief conflated the two objects that this row would otherwise have been crossed |
| 5 | **Clear.** It is not pushed to any rung; it is owned by the Container it describes |
| 6 | ⚠ **This is the hardest row for this object and it clears on `SUP:355-360`'s test.** *"The line is provenance, not location."* An envelope is **counts of bodies by age band** — matter, not derived from persons' beliefs and not stale against them, exactly like the larder the amended Container row already admits. A *norm*, a *density* or an *unrest level* is derived from persons; a body count is not |
| 7 | **Clear.** It stores no knowledge |
| 8 | **Clear.** It resolves nothing |
| 9 | **Clear.** It is not on a faction |
| 10 | **Clear.** No roll reads it |
| 11 | **Clear.** No person's act moves an envelope. It moves in MATTER, by metabolism |
| 12 | **Clear on the row's own subject** — the row governs **standing**. Age-band advance is **bodies**, which is licensed clock quantity 2 of the three admitted (`ABS:280`) |
| 13 | **Clear.** One envelope per Container, one rule |
| 14 | **Clear.** It authors no opportunity; it supplies weight |

### 9.8 · `Record` and the `documented(record_id)` claim source

| # | verdict and ground |
|---|---|
| 1 | **Clear.** A Record is matter at a Container; reading one is an act, and `choose` sees only the claims that reading produced |
| 2 | **Clear.** The claim it produces enters the ledger and is assembled like any other |
| 3 | ⚠ **THE ROW THIS OBJECT NEARLY CROSSED, and the gate is the fix.** An ungated `efface` of a register would drop confidence for every distant holder in the same tick — a broadcast, six weeks before news of the fire could travel. **The drop fires for a holder only when a claim that the record is gone lands in THAT holder's ledger**, which makes arson's effect map onto the news map exactly as vacancy does (`SUP:1188-1198`) |
| 4 | **Clear.** A cohort reading a record deposits at cohort fidelity, and an individuating member draws — the same rule as any telling |
| 5 | **Clear.** Nothing is pushed; the citation edge is the claim's own `source` field |
| 6 | **Clear.** A Record is a physical object with a `forgery_quality`, not an aggregate over persons |
| 7 | ⚠ **The nearest row, and it clears by direction.** The row forbids a **knowledge value stored on the thing known**. The Record is the thing *cited*, not the thing *known*: it stores no confidence, no reader set and no truth value. **The knowledge stays in the ledgers that cite it**, which is the row's own required placement |
| 8 | **Clear.** Reading and effacing are ordinary acts through the ordinary resolver |
| 9 | **Clear.** Untouched |
| 10 | **Clear.** `forgery_quality` is a **resistance pool**, in the same dice-equivalent unit as a lock's fineness (`SUP:524`) — the obstacle side, never an addend on a person's pool |
| 11 | **Clear for reading; the `efface` limb inherits 9.5's uncleared discrete case** |
| 12 | **Clear.** A Record does not recover and is not ticked |
| 13 | **Clear.** Five kinds, one rule; `admissible_source` is a **door predicate** on a Venue, not a resolver branch |
| 14 | **Clear.** A record is not an opportunity, and finding one is `investigate` |

### 9.9 · `oblige` (the seventh Tenure kind)

| # | verdict and ground |
|---|---|
| 1 | **Clear.** The obligor's own edges are interior state, in his own scope |
| 2 | **Clear.** Nothing masks obligations into a View |
| 3 | **Clear.** `requisition` addresses one person. **A kin-wide levy is many requisitions, each refusable** |
| 4 | **Clear.** A cohort may hold `oblige` edges as subject or object at cohort fidelity; individuation draws, as with every other edge |
| 5 | **Clear.** Owned by the subject; the inverse index is derived |
| 6 | **Clear.** It is an edge between two named persons, not an aggregate of loyalty. Compare the alternative — a *family cohesion* score — which would be one |
| 7 | **Clear.** It carries no knowledge; whether you know you are owed is claims |
| 8 | **Clear.** Refusal is an ordinary act; there is no compliance formula |
| 9 | **Clear.** Not on a faction |
| 10 | **Clear.** It changes **whose act is surfaced**, not anyone's dice. `SUP:302-304`: it *"surfaces another person's act as theirs to refuse"* |
| 11 | **Clear.** One edge, one person, one refusable act. A requisition on n kin is n separate acts by n people |
| 12 | **Clear.** Obligation does not accrue on a clock |
| 13 | **Clear.** One kind, one rule, no entity named |
| 14 | ⚠ **The nearest strain, and it clears.** A requisition *surfaces an act* for the obligee — which is close to an authored opportunity. It clears because **the surfaced act is not authored for that person: it is the requisitioner's own act, offered, and the obligee's response runs through his ordinary `opening_set` with `refuse` always in it.** Nothing was written for him; somebody asked him |

### 9.10 · `MatterKind`-typed `stores`

| # | verdict and ground |
|---|---|
| 1 | **Clear.** `stores` is matter on a Container; `choose` reaches it only through `Sensation.subsistence` and through claims |
| 2 | **Clear.** No View is built from it |
| 3 | **Clear.** A transfer is witnessed by whoever was present and by nobody else (`SUP:1462-1466`) |
| 4 | **Clear.** A cohort's larder is one quantity at one weight; nothing is deposited into it as a value standing for a distribution |
| 5 | **Clear.** Each Container owns its own; no coarser rung is handed one |
| 6 | **Clear.** A larder is *"a physical quantity that exists whether or not anybody believes in it"* (`SUP:357-359`) — the amended Container row's own worked example |
| 7 | **Clear.** How full the granary is, is a fact; who believes it is claims |
| 8 | **Clear.** `transfer` is an ordinary act. **`transfer` moves a quantity of ONE kind and needs no conversion**, so no exchange formula is introduced |
| 9 | **Clear.** Not on a faction |
| 10 | ⚠ **The nearest row, and it clears by the same reasoning the design already applies to `condition`.** Wealth is not an addend on any roll. Where it reaches an attempt it does so by changing **what you can attempt** — an option-set change, `SUP:1216-1221`'s inversion — or by paying an establishment, which changes **whose pool is rolled** |
| 11 | **Clear.** `transfer` moves an amount the giver has, from one larder to another. ⚠ **And it needs the precondition the design lacks: `stores(hearth(giver), kind) ≥ amount`**, or a negative larder mints matter (`REV:1704-1706`) |
| 12 | **Clear.** Larders move in MATTER by metabolism, which is licensed clock quantity 1, and by acts. Standing is untouched |
| 13 | **Clear.** A kind is a **type parameter**, not a branch: `transfer` reads `perishability`, `bulk` and `edible` as data. **`edible` is what stops silver satisfying hunger, and it is a field, not a case** |
| 14 | **Clear.** A full granary is not an opportunity until somebody's `opening_set` finds a use for it |

### 9.11 · The three refusals outside the fourteen rows

1. **No apparatus.** *"Validators over the design documents, freshness checkers, guards on the guards,
   or any apparatus whose subject is the repository's own process rather than the game"*
   (`11_code_shape.md:243-245`). **This document proposes none and its architecture requires none.**
2. **No threshold that fires an outcome, no stored gauge, no second resolver, no pushed aggregate.**
   The one licence claimed against the first of these is the **matter channel** — a band edge closing a
   verb — under `SUP:1370-1381`'s three conditions, all of which hold: the quantity crossed is matter,
   what changes is an **option set** and never a roll term or an outcome, and the closure is an Event
   witnessable by presence. **A social threshold remains forbidden.**
3. **VARIABLE, NOT THRESHOLD.** The enforceable form: **`force` and `hold` never appear in a
   precondition.** ⚠ **`hold` is now also the name of a `Tenure` kind, and the refusal must not be read
   as banning that.** The refusal is about the *quantities* `force` and `hold` from the coercion layer,
   not about the edge kind. **The disambiguation ruled: the edge kind is always written
   `Tenure(kind=hold)` or `hold`-edge in this document's prose; the coercion quantity is not used in
   this document at all.** Applied here: no convening-condition predicate, no band floor, no compliance
   term and no cardinality declaration sits in a precondition on either.

**Four structural tests remain the ones worth running, and NONE HAS BEEN RUN because nothing executes**
(`SUP:1767-1770`): no decision function can see the world · two witnesses of one event can disagree ·
a person with no office can act, petition, and receive an opportunity · order independence.

---

## §10 · WHAT DEPARTS FROM THE PRIOR DESIGN, AND ON WHAT GROUND

`SUP` remains the source of truth for everything not in this table.

| # | departure | from | ground |
|---|---|---|---|
| 1 | `Site` is a carrier with an id; `condition` is primary state at the Site an act names | `SUP:1232-1254` (site as matter, `condition(n)` derived at nodes) | node-keying gives two wrong verb sets from one collapsed scalar; a derived accumulator reads its own previous value; the mean has no base case |
| 2 | `Container` is the object's name; `Node` is refused | the prior brief | `SUP:337` already says *"Container (a rung)"*; `Node` collides with the port target at `godot/scene_tree_architecture.md:15` |
| 3 | The owner table has **four** owners and Nobody; the Faction row is deleted and its contents re-homed | `SUP:334-340`'s five rows | a faction is derivable in full from a Proposition plus its `commit` edges; the deletion is stated as an amendment because the row exists |
| 4 | `Tenure` is the one edge, with an id, `until?`, seven kinds and declared cardinality; `Holding` is an instance of it | `SUP:367`'s `Holding := (person, office, since, conferrer)` | nothing could hold ground; the record carrying every disputable political fact could not be a `Claim` subject |
| 5 | `touches` modes are **five** | `SUP:689`'s three | nothing created or destroyed anything; the review's rank 1 |
| 6 | `touch := (target, mode, field?, delta?)`, with a `spec` for `mint` | `SUP:689`'s `(object, mode)` | the conflict rule quantifies over a field the record did not carry; a `mint` has no object to address |
| 7 | **Four** write classes; a class is not a phase | `SUP:661-678`'s three, bound to phases | the reckoning operations were licensed by nothing; two barriers legitimately write matter |
| 8 | **Six loop steps, four barriers**, named by words | `SUP:641-654`'s eight labels under a seven-phase header | the eight phases conflate barrier with step; WITNESS is global; CENSUS is required for order-independence |
| 9 | `choose : (Person, View, Sensation) -> Act` | `SUP:138`'s `(Person, View)` | there was no legal path from a need to the function that uses it, and both repairs the review tried broke a rule of the subject |
| 10 | `verbs(site, c)` splits from `opening_set(person, view)` | `SUP:1313` and `SUP:1134` under one reading | one function was both world truth and belief, and the world-truth half read hidden state from inside `choose` |
| 11 | `remit.acts` is not the act vocabulary; the verb space is open, the mode space closed | the prior brief's claim that no new verb was needed | at least nine verbs the design itself names sit outside the closed five |
| 12 | One allowance (the act) and one cap (`capacity(date)`); `seat_items` is deleted | `SUP:387-412`'s two quantities | they are one quantity seen from two sides, and treating them as two produced a double-count |
| 13 | **D-2 is ruled**: one act per person or cohort, universally | `SUP:628-639`, `SUP:1864` reserved it | licensed by Jordan this session; the establishment carries institutional throughput |
| 14 | Conferral basis is **per office** | `SUP:447-487`'s global recommendation, reserved at `SUP:1868` | nothing requires every office to fill `conferrer` the same way, and the difference between the two is the political question of the age |
| 15 | `stores` is typed by `MatterKind` | `SUP:1472-1484`'s single scalar, reserved | one shape with a kind keeps the no-conversion refusal and makes both branches true of different things |
| 16 | A conferral rule may name the office's **own judging set** | `SUP:1015-1026`'s S19, reserved | a body with no superior convenes itself; a stall by disagreement is content, a stall for want of a date-holder is a hole |
| 17 | `Claim.source` has **five** constructors | `SUP:243-245`'s closed four | `admissible_source` and `forgery_quality` both already require a documentary source, and the purge limb has no citation edge without one |
| 18 | The purge is `strike` at a venue, plus `efface` on a Record gated on a claim landing | the prior brief's `efface` a record + `SAID` collision | no claim can cite a record; `SAID(A,¬C,s12)` does not collide with `SAID(A,C,s12)` on arguments; and the ungated drop is a §14 row 3 broadcast |
| 19 | `oblige` is the seventh `Tenure` kind | `SUP:302-304`'s obligation edge, which the prior brief deleted | without it a family has an inheritance pointer and nothing else |
| 20 | A demotion gate mirrors the advancement gate | nothing — the limb did not exist | advancement got a limb and demotion did not; the mirror keeps *no clock* |
| 21 | Every record carries an `id`, minted from the determinism substream | nothing declared ids | eight id-shaped things were consumed and none minted; a shared allocator would break the parallelism licence |
| 22 | Eviction ranks on `confidence_live × recency` only | `SUP:654`'s *"evict lowest salience"* | motivated retrieval otherwise becomes motivated deletion, and `relevance(c, q)` has no `q` at eviction |
| 23 | Advancement is an `alter` on a bounded field, not a `mint` | the prior brief | a rank is a scalar field, not an object; two meanings for one word |
| 24 | Annexation is a `hold` Tenure over a Container; `annex`/`secede` are deleted | the prior brief's `confer` on a `contain` edge | the tree is geography and allegiance lives in factions; `secede` additionally collides with `05:594`'s shipped use for defection |
| 25 | The docket item is a first-class object | nothing — the up-stroke had no dated item | S19 was unstatable without one, and lapse had nothing to be computed against |
| 26 | The cohort **acts**; the envelope is inflow only | the prior brief's replacement of the cohort | matter does not act; the replacement manufactured elite-only politics by construction |
| 27 | `Faction` is struck from the stance referent set; `Place = Container | Site` is defined | `ABS:188`'s closed four | `Faction` and `Proposition` denote the same thing after §2.7, and `Place` was defined nowhere |
| 28 | Claimants in `contest` are person sets under a proposition | `SUP:327` (factions) vs `SUP:1141` (`{enforcement, resistance}`) | `resolve` has no Person parameter and must not acquire a claimant-type branch |

---

## §11 · WHAT IS CARRIED AS OPEN

Stated so no later document can cite this one as though these were closed.

1. **Is the world dying or misunderstood?** — **Jordan's**, and the only one of the seven forks that
   stays his. The code is identical either way.
2. **Where the channel store lives.** Ruled against three ways (§5.3). Character generation works
   without it; the *plausible past* property does not.
3. **§14 row 4's construal-spread rule** — where a cohort's stored spread lives, what produces it, and
   what an individuating member draws from. Under-specified upstream at `SUP:1737`; the review could
   not close it inside the design's refusals and neither can this document.
4. **The `exclude` limb of §14 row 11**, now widened by four object classes through `efface` (§9.5).
   Inherited, not introduced; no bound is invented here.
5. **The closed predicate vocabulary's actual membership.** One worked example, `SAID(…)`, and no
   roster.
6. **`season_factor(territory)`'s distribution** — range, mean, shape, and what a bad draw is. Read
   four times, stated nowhere.
7. **`Venue`'s twelve fields plus a five-field door**, eight of which appear once and carry no value.
8. **`relevance(c, q)`** — never defined, and `q`'s type, origin and lifetime are unstated.
9. **`Profile`** — the return type of `estimated_profile`, described in prose and never given a record.
10. **The empty judging set** — F3's own falsifier: an office whose judging set is empty has no
    self-convening route, and no floor is specified.
11. **The Coherence-0 officeholder** — F4's own cost: a frozen seat that vacancy-by-absence must reach.
12. **How large an establishment is**, who authors the first one, and what `upkeep` costs — D-2's
    residue.
13. **The exchange form** — two transfers plus a binding. Rescue-by-gift constructs; rescue-by-market
    is asserted (`SUP:1797-1798`).
14. **Re-denominating the coercion layer's coin arithmetic** into typed `stores`. Unwritten work
    (`SUP:1795-1796`).
15. **L-4, the playable-seat list**, on which every necessity claim in `SUP` is conditional.
16. **Vacancy-by-absence's two named falsifiers** — the deliberate absence, and the hostage repricing's
    cost at the top of the ladder.
17. **The two incompatible shipped Coherence band tables** (`ABS:221-225`), unresolved.

---

## §12 · STATED LIMITS

1. **Nothing here has executed.** No test, no simulation, no measurement, no probe. Under `CLAUDE.md`
   §0.2 none of it is done, and it cannot be until something runs it.
2. **The four structural tests have not been run**, and three of them are precisely the properties this
   architecture claims (§9.11).
3. **Every claim about a source document is a claim about text at a cited line.** Where a citation is
   wrong, the claim resting on it is wrong; nothing here is corroborated by execution.
4. **The design's own evidence base is hand-assembled and elite-heavy**, and no rate about play appears
   anywhere in this document (`SUP:32-38`).
5. **Two of #342's seventeen documents — `06_down_stroke.md` and `12_coercion_and_force.md` — are not
   covered by the verified fact base** (`SUP:1845-1848`). §5.6's dispensation material and F2's
   coin-hole material both rest partly on them.
6. **The five audit runners that produced the dispositions behind this document measured nothing
   either.** Their strongest results are the four findings rediscovered independently by runners that
   could not see each other — the channel store's missing licence, the loop's barrier count, `mint`
   outside the conflict rule, and the purge limb's missing claim source. Everything else in them is one
   reader's argument.
7. **This document is REFERENCE, not mechanism** (`CLAUDE.md` §0.05). If it were deleted, no behaviour
   would change, because no behaviour exists yet. **The test to apply to every line above: what would
   have to run for this to be true?**
