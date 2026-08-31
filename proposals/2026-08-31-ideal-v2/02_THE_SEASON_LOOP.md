# THE SEASON LOOP — v2

## Status: PROPOSED (2026-08-31). **Nothing here has executed.** No season has been run, no trace below
## was produced by a program, and every ordering claim is an argument about text rather than an
## observation. `CLAUDE.md` §0.2 applies: **done means it runs, and none of this runs.**

---

## §0 · WHAT THIS IS

`01_ARCHITECTURE.md` owns the primitives. **This document owns how one season executes on them** — what
each step reads, what it writes, in what order, under what invariant, and what it refuses to do. It
adds no primitive. Where it needs one, it names the section of `01` that defines it.

**Citation key**, identical to `01_ARCHITECTURE.md` §0.1: `SUP:NNN` is
`proposals/2026-08-31-ideal/10_SUPERSEDING.md`; `REV:NNN` is the adversarial review of that design,
document **20** in `proposals/2026-08-31-ideal/`; `ABS:NNN` is `CODE_SHAPE_ABSTRACT.md` in the
2026-08-31 review directory under `proposals/_session_provenance/`; `NN:LLL` is
`proposals/2026-08-29-valoria-from-scratch/NN_*.md`; `ARCH §N` is a section of `01_ARCHITECTURE.md`.

**The step names have no letter-number spellings.** `CALENDAR · MATTER · DELIBERATE · RESOLVE ·
WITNESS · CENSUS`, and nothing else. The legacy `P0 … P7` (`SUP:641-654`) are retired and appear only
inside a quotation.

---

## §1 · THE SHAPE OF A SEASON

```
season(world) -> world':

  ══ CALENDAR ══════════════ barrier · global
       advance the date
       fire every due Date into its docket
       evaluate every live convening condition; schedule the dates they name
       recompute option availability
       writes: dates, dockets                                    class: CALENDAR

  ══ MATTER ════════════════ barrier · global
       larders consume against mouths
       production resolves — `yield` is rolled here
       wounds close or fester; bodies age; bodies die
       travellers advance one leg
       envelope weights move: births in, deaths out
       every Site loses `wear(kind)` of its condition          — ENTROPY
       writes: larders, bodies, travel, yield, envelope weights,
               and `condition` BY `wear` ONLY                    class: MATTER
       ── the world is now FROZEN for the map ──

     DELIBERATE ──────────── map · per person or cohort · PURE · any order · parallel
       sensation <- sense(person, frozen_world)         # two floats; ARCH §3.1
       view      <- assemble(person, question)          # top-K by salience; SUP:251-255
       act       <- choose(person, view, sensation)     # exactly one Act
                    -- opening_set(person, view) runs INSIDE choose; ARCH §3.2
       writes: nothing but the returned Act                       class: —

  ══ RESOLVE ═══════════════ barrier · global
       build the touch graph over every declared Act
       detect conflicts; route them to `contest`
       order by the five strata
       compose obstacles; roll; band; apply touches
       sum additive deltas per field and clamp once
       mint ids from the substream; set `until` on effaced edges
       emit Events
       writes: everything else                                    class: ACTS

  ══ WITNESS ═══════════════ barrier · global
       fan every Event out by presence and channel
       then, per person, independently, in any order:
         witness(person, event) -> claims, deposited with collision
         confidence decays
         the ledger evicts on confidence_live x recency
       writes: that person's own ledger only                      class: INTERIOR

     CENSUS ──────────────── global pass · shares WITNESS's join
       evaluate individuation over the post-eviction ledger set, ONCE
       evaluate de-individuation over the same set, ONCE
       reconcile envelope weight against the records drawn and returned
       writes: the population                                     class: MATTER
```

### §1.1 Four barriers, six steps, and why the counts differ

A **barrier** is a synchronisation point: every prior step must be complete before it begins. A **step**
is a named unit of work. There are **six steps and four barriers**, and the two counts differ for two
reasons, both stated:

- **DELIBERATE is not a barrier.** It is a map whose instances cannot observe one another. It writes
  nothing global, so nothing has to be joined before it or inside it.
- **CENSUS is not a barrier.** It runs after WITNESS's join and needs no join of its own, because
  WITNESS already supplied one and nothing between them writes.

⚠ **WITNESS *is* a barrier, and the brief that preceded this document moved it inside the per-person
map.** It cannot be there: *"events fan out by presence and channel"* (`SUP:653`) is cross-person by
construction — one Event reaches many ledgers, and which ledgers it reaches is a function of where
everyone is. **The fan-out is global; the deposit is per person.** Two independent runners found this
separately, which makes it one of the four highest-confidence results in the exercise behind these
documents.

### §1.2 Four write classes

⚠ **The prior design licenses three classes and binds each to one phase** (`SUP:661-678`), which left
the reckoning operations — decay, eviction, individuation — licensed by nothing at all. Four classes,
and a class is a **class of write**, not a phase:

| class | written at | what may be written | licensed because |
|---|---|---|---|
| **CALENDAR** | CALENDAR | dates and dockets | a date is not an outcome; it is an occasion |
| **MATTER** | MATTER **and** CENSUS | larders, bodies, travel, the season's `yield` roll, envelope weights, individuation bookkeeping | metabolism and nature — the world is not a caretaker for having weather |
| **ACTS** | RESOLVE | everything else, **including every `condition` delta an act caused** | a person did something |
| **INTERIOR** | inside WITNESS | **one person's own ledger and nothing else** | it cannot reach anything but its owner, which is a stronger guarantee than any of the other three carries |

**If a future object cannot be placed in one of these four, it does not go in the engine.**

⚠ **Dropping phase-exclusivity is a real change and is stated rather than smuggled.** Two barriers write
the MATTER class. That is honest — MATTER moves envelope weight by birth and death, CENSUS moves it by
individuation — and the alternative is what the prior design produced: every time an operation moved
between phases, the class table read as violated when nothing had changed about what was written.

### §1.3 The parallelism licence, and exactly what it rests on

> **DELIBERATE may run in any order, in parallel, at any degree of concurrency, because no instance can
> observe another's effect.** It reads a frozen world and one person's own interior, and returns a
> value.

That licence held in the prior brief only by accident, and **two things had to be fixed for it to be
true**:

1. ⚠ **Individuation was inside the per-person map and mints a globally addressable object.**
   Individuation moves envelope weight and creates a Person; **de-individuation's predicate reads other
   people's ledgers** (`SUP:209-210`, *"no other person's ledger names them"*). So X survives or
   vanishes depending on whether Y's eviction ran first. **Both moved to CENSUS**, which reads the
   post-eviction ledger set **once**, globally.
2. ⚠ **Id allocation is the textbook parallelism hazard and the prior brief never mentioned it.**
   **There is no allocator.** `id = H(world_seed, tick, subject_id, purpose)` (`ARCH §2.2`) is computed
   independently by whoever needs it, is identical on every re-run, and requires no shared mutable
   state. **One mechanism closes both the determinism requirement and the parallelism requirement.**

**The remaining order-independence obligations are RESOLVE's**, and `SUP:611-613` already requires them:
two attempts resolved in a different order give the same answers; adding a person somewhere does not
re-phase every other roll. §10 walks how each is obtained.

---

## §2 · CALENDAR

**Barrier. Global. Write class: CALENDAR — dates and dockets, and nothing else.**

```
CALENDAR(world):
  1. tick <- tick + 1
  2. for each Date d with d.when == now:
        d.fired <- true
        d.docket stays as carried; nothing is added here
  3. for each live ConveningCondition k:
        if evaluate(k.predicate) is true:
            schedule a Date from k.date_form, at the horizon its date-holder carries
  4. recompute option availability
```

### §2.1 What fires, and what merely becomes reachable

**Step 2 fires dates; it does not decide anything at them.** A fired Date is an **occasion**. What
happens at it is `compose_agenda` and `determine`, both of which are acts by named persons, resolved at
RESOLVE in the same season. **A Date that fires with a vacant convener is a date nobody is ordering**,
and that is correct behaviour rather than a defect (`SUP:786-789`).

> **VACANT-ALLOCATOR SEMANTICS, unchanged and load-bearing** (`SUP:1611-1616`). **A standing date whose
> allocating office is vacant fires, allocates nothing, and lapses. The stock sits.** It is not
> redistributed, not held over, not split by default, not allocated by seniority or by any other engine
> rule. The claimants left unfed carry their mouths-deficit straight into their hearths' own need
> computation, by the ordinary larder line and with no crisis object anywhere.
>
> That is the famine writing itself: the grain exists, the granary is full, the praefect is dead, no one
> has been conferred, no sitting is convened, no dispensation is issued — **and people starve inside a
> system that is working exactly as written.**

### §2.2 Convening conditions — what step 3 may and may not read

`ConveningCondition := (id, holder, predicate, date_form, set_by, set_at)`; `holder ∈ Container |
Office` (`ARCH §5.12`).

**The predicate may read exactly three things** (`SUP:783-785`): the holder's **own state**; an **R-1
compute-on-demand aggregate over its descendants**; or **the calendar**. It may never read a
descendant's stored state, never a social quantity that is not itself a computed norm, and never the
true faction profile.

**The predicate is published as a BAND, never as a trigger point.** This is the same discipline the
larder already runs on (`13:31-32`): everyone can see that the granary is *Thin*, and nobody can see the
number at which it becomes *Hungry*. Without it, a published trigger point is a threshold every player
optimises against and every NPC is blind to.

**It decides nothing.** It schedules an occasion. Whether the matter is *reached* is `compose_agenda`'s
convener's choice, and whether it is *decided* is a determination.

**Attaching one is an act, in an earlier season.** It is `convene`'s first operation — *setting a date*,
performed conditionally in advance — by a person holding an office whose remit includes `convene` at
that holder, and it cost that person their season when they did it. **So the object is not decider-free
at its root**: it traces to an act, seasons or generations earlier.

⚠ **The cap on live conditions is now `Σ capacity(d)` over the dates the holder carries**, not
`seat_items(office)`. `seat_items` was deleted when D-2 was ruled (`ARCH §7`), and this is the one
place in the prior design that spent it as a cap rather than as an allowance.

### §2.3 Step 4 — recompute option availability, and why dropping it breaks a shipped mechanism

⚠ **The prior brief dropped this operation, and it is one of four `SUP:647` lists.** It is not
bookkeeping. `SUP:1098-1102` makes a suppressed grievance *"an ordinary stance row at full magnitude
whose act-proposition has an unmet enabling claim … the 're-arm predicate' is just the proposition's own
enabling condition, **recomputed at P0 like every other option**."*

**Drop step 4 and every suppressed grievance in the world stays suppressed forever**, because nothing
re-evaluates the enabling condition. The road to revolt closes silently, with no error anywhere.

**What step 4 actually recomputes**: for every Container and Site, the band memberships that gate
`verbs(site, c)`; for every Date, whether it is live; for every act-proposition in every stance table,
whether its enabling claim is now held. **It writes no option list** — `opening_set` is a person-side
query computed fresh in DELIBERATE (`ARCH §3.2`). What it writes is dates and dockets, which is its
class.

### §2.4 CALENDAR's refusals

| it may not | because |
|---|---|
| decide anything | `SUP:717`'s C3: a convening condition decides nothing, and neither does the calendar |
| place an item on an agenda | `SUP:791-793`: it schedules a **date**, never an item; that is `compose_agenda`'s job and it costs an act |
| write matter | wrong class |
| read a true faction profile | `SUP:785`, C4 |
| end a petition by a fact about the world | `SUP:1027-1030`: *no petition is ended by a fact about the world; it ends by a date passing, or by a person's motion* |

---

## §3 · MATTER

**Barrier. Global. Write class: MATTER — metabolism and nature only.**

```
MATTER(world):
  1. for each Hearth h:
        for each Site H drawn by h:
            yield(H, season) = base(H) x condition(site(H))
                             x season_factor(territory) x (3 + d10)/8.5
        draw(h)   = SUM yield - SUM levy + SUM transfers_in - SUM transfers_out
        stores(h, kind) += draw(h, kind) - mouths(h, kind)      # may go negative
  2. wounds close or fester; bodies age one season; bodies at term die
  3. travellers advance one leg
  4. envelope: births add weight at the youngest band; deaths remove weight
  5. for each Site: condition <- clamp( condition - wear(kind(site)), 0, 1 )   # ENTROPY
  6. the world is frozen
```

### §3.1 What may move here, and the one thing that emphatically may not

**No social quantity moves at MATTER, and NO ACT'S EFFECT LANDS AT MATTER** (`SUP:648-650`,
`SUP:679-684`).

⚠ **That refusal is a correction the prior design made against itself and it must not be undone.** An
earlier version of `SUP` put an act's effect on a site into this barrier as a deferred write, *which is
neither metabolism nor nature* and therefore broke the licence it had just stated. **Every act delta to
a Site's `condition` is written at RESOLVE and nowhere else.** Weather reaches matter where #342 puts
it: **inside the `yield` roll**, as `season_factor` and `(3 + d10)/8.5`.

⚠ **BUT `condition` IS WRITTEN HERE BY ONE TERM, AND IT IS NEW: `wear`.** Jordan ruled F6 — *"if the
world is not tended to by anyone, it will die"* — and an act-only fuse cannot say that: with
`Σ acts = 0` an untended site **freezes**, it does not decay (`ARCH §7` F6).

```
condition(site) <- clamp( condition(site) - wear(kind(site)), 0, 1 )      # MATTER, entropy
condition(site) <- clamp( condition(site) + Σ this season's act deltas, 0, 1 )   # RESOLVE, acts
```

**`wear` is a per-site-kind constant in `condition`'s own units** — not weather, not a multiplier, not
a roll — and it sits in **decider-free channel 1, metabolism and nature**, beside *crops yield, wounds
close or fester, bodies age.* **Entropy belongs with metabolism.** It is an authored per-season
constant and it belongs in the centralized parameter table, one row per site kind; **no value is
proposed anywhere in this suite, because none has been measured.**

**The two writers do not conflict and the clamp rule survives.** §5.2's *"sum the deltas and clamp
once"* quantifies over **concurrent** writers inside RESOLVE. `wear` is applied at MATTER, **strictly
before** all of them, in an ordered step — so it needs no commutativity argument at all.

### §3.2 `yield` is a roll, and the roll is load-bearing

`(3 + d10)/8.5` ranges `0.47×base` to `1.53×base`, mean exactly 1.0, and *"a bad season is `d10 ≤ 3` —
a 30% event costing between a quarter and a half of a holding's contribution"* (`SUP:1398-1401`, citing
`04:59-63`).

⚠ **An earlier version of the prior design dropped this term**, which made `stores` deterministic and
**stopped the larder bands moving at all.** With no variance there is no bad year, no shortfall that
nobody caused, and no need that rises without an enemy — which is most of what the season loop is for.

Its substream is `H(world_seed, tick, site_id, "yield")` — **actorless, which is exactly the
generalisation `ARCH §6` exists to supply.** Nature has no performer, so it uses the magnitude reading
and not the pool reading.

⚠ **`season_factor(territory)`'s distribution is stated nowhere in the corpus** — no range, no mean, no
shape, no definition of a bad draw — while it is read four times and an extreme draw on it is a storm.
Carried open (`ARCH §11`).

### §3.3 Death at MATTER, and the one thing it does not do

A body at term dies here. This is licensed decider-free channel 1 (`ABS:271-273`). It:

- sets `until = tick` on every `Tenure` the person held, of every kind;
- ⚠ **it does NOT open the conferral Date. THE NEXT CALENDAR DOES** — dates are the CALENDAR class and
  MATTER may not write one (§1.2). The vacancy is a *fact*; the date is an *occasion*; CALENDAR is
  where facts become occasions. The following CALENDAR schedules it at the horizon its date-holder
  carries — the Container for a hearth or heritable seat, the parent Office for an appointed one
  (`SUP:1200-1206`). **Nothing observable changes**, because that horizon is a future date anyway;
  what changes is that no step writes outside its class. *An earlier version had MATTER open it, which
  its own write matrix forbade.*
- resolves the hearth's `succeed` pointer, which is *"the only route by which anything changes hands"*
  in the prior design and is decider-free (`REV:833-836`).

> **And it does NOT propagate.** Nothing about the death is written into any other person's state.
> **`licensed_standing`, compliance and every dispensation the holder issued lose their complier for a
> given person only as and when a claim of the death reaches THAT person** (`SUP:1188-1198`). A
> synchronous drop would be a polity-facing quantity computed off true world state, and persons would
> react to a death they had not heard of.
>
> **The withheld death-notice is therefore one of the most powerful acts in the game**, and the
> interregnum is smeared along the channels: three days to the capital, six weeks to the fjord hamlets.
> *The map of where obedience has lapsed is exactly the map of where the news has gone.*

### §3.4 Birth is envelope weight, and is NOT `mint`

⚠ **The prior brief put birth in two write classes at once.** Births move **envelope weight** here, as
metabolism. **`mint` a Person is individuation of a record and happens at CENSUS** (§7). One operation
per class; the *born or die* flow is answered here and character generation is answered there.

### §3.5 The frozen world, and `sense`

At the end of MATTER the world is frozen for the duration of DELIBERATE. **Nothing in the map writes to
it and nothing in the map can observe another instance's effect**, because there are none.

> **`sense(person, frozen_world) -> Sensation` TAKES A WORLD, AND THIS IS LEGAL.** §14 row 1 forbids a
> `World` parameter **on a decision function**. `sense` decides nothing: it returns **two floats** —
> `subsistence` and `standing` — carrying no references and answering no query (`ARCH §3.1`). `choose`,
> which is the decision function, still has no `World` in scope by omission.
>
> **This is the whole of the answer to a gap the review left open with no fix**, and it is offered as a
> proposal rather than as a repair of anything. It is checkable by reading two type signatures.

**Why the other two needs need no channel.** `commitment` and `exposure` read **the view**
(`SUP:189-190`), and `choose` already has the View. They are computed inside `choose` from claims the
person holds. So a fisher whose Duke signed a treaty three days ago has no changed `exposure` until the
crier reaches him, and if the crier's version is distorted his need is computed from the distortion.

---

## §4 · DELIBERATE

**Map. Per person and per cohort. Pure. Any order. Writes nothing but the returned Act.**

```
deliberate(person, frozen_world) -> Act:
  sensation <- sense(person, frozen_world)       # two floats. NOT a decision function
  question  <- the question the person is asking this season
  view      <- assemble(person, question)        # at most K claims, by salience
  return      choose(person, view, sensation)    # exactly one Act
                 |
                 +-- INSIDE choose: openings <- opening_set(person, view)   # BELIEF
                     and the pick among them.  opening_set takes NO third argument,
                     which is why choose's signature is (Person, View, Sensation).
```

### §4.1 View assembly

```
K = 7 + Focus + 2 per Knot consulted - Coherence penalty (Dissonant 1 ... Severed 5)

salience(c) = recency(c) x confidence_live(c) x relevance(c, q) x stanceweight(c, person)
stanceweight(c) = clamp(1 + lambda x agreement(c), 0.05, 2.0),   lambda = obstinacy / 5
```

**`K = 3` per cohort** (`SUP:650`).

**The view is ASSEMBLED, not filtered.** *Absence of a claim produces absence in the view, never a
widened interval, because a widened interval is uncertainty and the design needs ignorance*
(`SUP:154-157`). **`View` must be a distinct type from `World`, with no coercion, no shared supertype,
and no field of `View` holding a `World`** — if a `View` can be built from a `World` by masking,
someone eventually masks nothing.

**The one multiplication that is all of motivated reasoning.** A Templar with obstinacy 5 holding an
exonerating claim about a Southern Einhir smith gets `stanceweight = 0.05`: the claim is in his ledger,
at high confidence, and its salience is one twentieth of an agreeing claim's. **He is not hiding it and
he is not lying; he is not thinking of it.** The floor is 0.05 rather than 0 so a devastating firsthand
contradiction can still cross. **What is attenuated is retrieval, not value** (`SUP:248-263`).

**`relevance(c, q)` IS DEFINED, in full, at `03:342-344`:**

```
relevance(c, q) = 1.0  if (subject, predicate) is in q's read-set
                  0.3  if c's subject is within two graph edges of a read-set referent
                  0    otherwise
```

⚠ **An earlier version of this document said it was "never defined anywhere in the corpus", in five
places across three files. That was false, and the cause is recorded at `ARCH §12.8`.**

**What IS open is `q`'s PRODUCER.** `assemble` takes a question; `choose` does not. The defensible
default, stated as a default and not as a ruling: the question is the person's highest-ranked unmet
need, which makes assembly need-directed and gives `q` a producer. **Nothing in the corpus says this
and it is not asserted as canon.**

**And `03:377-407` supplies what happens when relevance is 0 for everything — the EMPTY VIEW, which is
a shipped four-rung ladder this loop must run and an earlier version of this document did not carry:**
**(1)** a marks-based expectation, deposited at 0.35 with source `inferred(MARKED(subject, m))` —
*"prejudice as the literal default of an empty ledger"*, and **deposited with its root, so it can be
refuted by investigation like any other claim**; **(2)** a rumour draw at 0.2 from the place's ambient
claim; **(3)** what the person believes his neighbours hold — **an inference over claims he actually
holds about their expressed positions**, at 0.25, never the container's true aggregate; **(4)** if all
three are silent, **the option leaves the person's act list.**

> **IGNORANCE NARROWS THE OPTION SET. UNCERTAINTY WIDENS THE OUTCOME DISTRIBUTION. THE ENGINE MUST
> NEVER SUBSTITUTE ONE FOR THE OTHER** (`03:405-407`).

**Ties in view assembly break deterministically** — firsthand > told_by > inferred, then more recent,
then lower claim id — *"because randomness here would make a person's beliefs shimmer between two
decisions in the same hour"* (`03:369-372`).

### §4.2 `opening_set` is belief, and it can be wrong

> **`opening_set(person, view)` is computed INSIDE `choose`, from the person's own ledger,
> stance, capability, `Sensation`, and the remits they hold. `verbs(site, c)` — the world's actual verb
> gate — is READ ONLY BY `resolve`.**
>
> **A person may therefore attempt a verb the world has already removed, and discover the harbour
> silted.**

That is better fiction than a menu that greys out, and `SUP:1227-1228` already argues for it: *"the
people who notice first are the ones whose practice used that verb."* The seam is also what makes the
silting **legible without a gauge** — you find out by trying, or by being told, and both are ordinary
epistemics.

**A Candidate is `(verb, target_spec[], believed_obstacle_band)`**, not an Act. The prior brief typed
`opening_set : Person → [Act]`, which gave one type two lifecycle states with no discriminator.
`choose` returns exactly one Act, constructed from exactly one Candidate.

**What contributes a verb to the set:** practice rank ≥ 3 adds verbs, rank ≥ 5 adds verbs unattemptable
below it (`SUP:504-505`); a remit makes the closed five eligible where they otherwise are not
(`SUP:421-424`, `SUP:433-435`); a `hold` Tenure makes acts over the held thing eligible; an `oblige`
edge surfaces a requisition **as theirs to refuse**; a believed dispensation changes terms, so old
verbs price differently and new ones appear (`SUP:1132-1137`); a believed band closure removes one.
**Nothing is authored for anybody** — §14 row 14.

**An untrained attempt is always legal and is just a small pool** (`SUP:503-504`). A postless fisher's
shortfall arithmetic is identical to a Duke's, and **the design's low end is right and this document
does not touch it.**

### §4.3 One act, and what that means at every rung

**One act per person or cohort per season. Universally.** No office, rank or holding changes it
(`ARCH §7`). An act is not everything a person does in three months; it is **the one discretionary
commitment**. Subsistence, craft and travel-in-progress happened *to* them at MATTER.

**A cohort acts, and acts exactly once.** A cohort is persons at coarse fidelity — one record, a
weight, evaluated once, applied to all — and it is **exactly one type with an individuated person**
(`SUP:202-206`). It holds `commit` edges, carries stance, and can be petitioned, levied and roused.

⚠ **If the cohort did not act, the design would have elite-only politics by construction**, which is the
defect `SUP:205-206` names in as many words. That is the single worst error in the brief this document
replaces, and it is fully reversed at `ARCH §2.6`.

**A Duke takes one act.** He `dispatch`es — and thirty-five named people each spend **their** one act
deciding what to do about it. That is `SUP:1149-1183`'s one-order-many-executors, now paid for out of a
budget that exists. **Same allowance, incomparable reach.**

**An unspent season is the design's characteristic outcome, not a failure**, and the recommendation is
that an unspent act does not bank (`ARCH §7`).

### §4.4 DELIBERATE's refusals

| it may not | because |
|---|---|
| see a `World` | `SUP:143-147`; enforcement is by omission, not by inspection |
| observe another instance | it writes nothing global; that is the whole parallelism licence |
| write a person's ledger | the ledger is written at WITNESS, by `witness`, and by nothing else |
| mint a Person | that is CENSUS (§7); minting here was what broke the prior brief's parallelism claim |
| read a true faction profile | `SUP:121-128`: nobody may |
| read the event log | `SUP:613-615`: *no decision function may read the event log* — that reintroduces the world by the back door and it will not look like a violation at the call site |
| consult office for eligibility to act at all | `SUP:194-196`: every act is offered to every person; office changes whether your decision **binds others**, not whether you may act |

---

## §5 · RESOLVE

**Barrier. Global. Write class: ACTS — everything not written by the other three.**

```
RESOLVE(acts, world):
  1. graph  <- touch graph over every declared Act
  2. C      <- conflicts(graph)
  3. route every conflict to contest(container, prize, claimants)
  4. order  <- strata(acts)
  5. for each act in stratum order:
        if refused: emit a refusal Event; continue
        obstacle <- compose(context)
        margin   <- roll(pool) - obstacle
        band     <- degree(margin)
        apply the act's touches at that band
  6. for each additive field touched this season:
        value <- clamp(value + SUM deltas, lo, hi)      # ONE clamp, at the end
  7. mint ids; set until on effaced edges; cascade
  8. emit Events
```

### §5.1 The touch graph and the conflict rule

Every Act declares `touches[]`, each entry `(target, mode, field?, delta?)` (`ARCH §2.4`).

> **THE CONFLICT RULE.** Two acts conflict iff they share a target and **either mode is
> `exclude`/`efface`**, **or both `alter` an `exclusive` field**, **or both `mint` edges that jointly
> break a declared cardinality.** Everything else resolves independently.

**Ties break on `H(act_id, world_seed)` — never on rank, office or list position** (`SUP:692-694`),
because a rank-ordered tiebreak is a hidden power stat that never appears on a factor sheet.

⚠ **Three things had to be added for this rule to be computable, and each closes a case that would
otherwise break an invariant silently:**

1. **`touch` carries a `field`.** The rule quantifies over a field; the prior brief typed `touches` as
   `(object, mode)`, so the rule **was not computable from the declared data**.
2. **A `mint` declares `(parent_of(object), alter)` in its own touches.** Otherwise two `mint` acts
   share no object — the object does not exist yet — and **two settlements can be founded on one spot
   with the resolver seeing nothing.** It also closes the mint-racing-an-efface pair.
3. **Cardinality is declared per kind.** Otherwise two `succeed` edges on one hearth, two `hold` edges
   on one office and two `contain` edges on one person are **each individually legal, no conflict
   fires, and the invariant breaks only after both resolve.**

**Why the third case matters more than it looks.** If two `contain` edges name one Person, *nothing
errors*: `presence` and `sovereign_fraction` leave `[0,1]`, `draw_share` stops summing to 1, and the
judging set votes that person twice — while the derivation the whole design rests on (`SUP:102-104`)
evaporates in silence. **A cardinality declaration is the validation point an "invariant on the edge
kind" always needed and never had.**

### §5.2 Commutativity, and the one clamp

> **`additive` — all writers apply, order-independent. `exclusive` — contested. The default for an
> undeclared field is `exclusive`.** Declared on the field, where the field is declared.

⚠ **`additive` is order-independent ONLY under batching.** `clamp` does not commute with addition at the
bounds: `+0.3`, `−0.5`, `+0.3` applied to a `[0,1]` quantity sitting at 0.9 gives three different
answers in three different orders **if each is clamped as it lands**. **Step 6 sums a season's deltas
per field and applies the clamp once**, which is what makes `SUP:1333`'s accumulator honest.

**And without per-field commutativity the commons does not work at all.** Under the prior design's rule
— *two acts conflict iff they share an object and either mode is `exclude`, or both `alter` the same
field* (`SUP:689-691`) — **all forty `alter` acts on a harbour conflict pairwise and route to a
contest**, so the summation never happens and the tragedy-of-the-commons shape §10 exists to produce is
unreachable.

### §5.3 The five strata, and why the order is that order

`SUP:695-698`, unchanged:

| # | stratum | why here |
|---|---|---|
| 1 | **movement** | every stratum below asks who was there |
| 2 | **binding decisions at docket dates** | a determination changes the terms the strata below act under |
| 3 | **contested physical acts** | who holds the ground before anybody draws from it |
| 4 | **uncontested material acts** | draws, transfers, repairs |
| 5 | **social acts** | **last, because social acts are *about* what happened** — which is what makes a season's gossip be about that season's deeds |

**`mint` and `efface` sit in stratum 3 when contested and stratum 4 when not.** Founding a settlement,
building, razing and establishment are material acts; nothing about the new modes needs a stratum of
its own.

### §5.4 One roll, one obstacle

```
Pool(person, practice) = Attribute[relevant](person) + Practice[practice](person)
   attributes 1-7 ; practice 0-5 ; realistic pool 1-12

obstacle(context):
    if context.opponent is a person: return OPPOSED
    R = resistance_pool(context)
    if R <= 1: return 0
    return round_half_up(R / 2)

Margin = successes - Obstacle
   <= -2 Disaster | -1 Failure | 0 Costed Success | +1,+2 Clean | >= +3 Overwhelming
```

**The target is computed, never assigned** (`SUP:508-512`) — which matters because a difficulty number
must be *decided* by somebody, and that somebody is the GM this game does not have.

**`resistance_pool` is composed on demand, never stored.** The Masterpiece Examination's obstacle is
computed from the individual stances of the sitting masters toward the candidate's marks: change the
masters — a schism, a retirement, a bribe — and the number changes with no edit anywhere
(`SUP:530-535`).

**An opposed contest is the identical `roll` called twice**, with the deterministic obstacle replaced by
an actual draw. **It is not a second resolver.**

⚠ **If `Obstacle > 2 × Pool` the resolver refuses to roll.** The act must change under a manoeuvre or it
does not happen (`SUP:527-528`). **The season is still spent**, and the actor witnesses an Event: *the
attempt was made and was impossible.* Otherwise impossibility is a free probe of hidden world state, and
the actor learns nothing from having tried — both of which the design refuses elsewhere.

⚠ **The `R ≤ 1 → return 0` branch is a fast path, and the review's rank 7 argues it should be deleted**
because §14 row 8 marks fast paths refused and this document marks that row **Clear** (`REV:1704-1706`).
**This document does not rule it**; it is carried open at §12, because deleting it changes the odds of
every trivial attempt in the game and that is a balance question nothing here can settle.

### §5.5 The exposure preview, and what may cross it

Before any die is drawn the resolver publishes the inputs a player would need to compute the odds
himself. **Computing that table never calls `roll`** — *"looking at the odds cannot consume the die"*
(`SUP:574-575`).

⚠ **That is a channel, and it is ASYMMETRIC: `choose` has no `World`, so no NPC can run the same
probe.** The partition (`SUP:578-586`):

| what resists | published | why |
|---|---|---|
| material and publicly inspectable — a lock's fineness, a wall's sheerness | **the scalar** | anyone standing there can look at the wall |
| a resistance composed from persons' private stances — a judging set, an admission committee | **a BAND, never the scalar** | the scalar is an aggregate of private stances, and nobody may read a true profile |
| hidden world state gated behind investigation — a Site's `condition` | **a band, and the scalar is never an operand of any roll** | so there is nothing finer for a repeated preview to invert out |
| the opponent's pool in an opposed contest | **published, deliberately** | the honest response to a mismatch is to publish it, not to dress a 3-vs-14 roll as a rich tactical scene |

> **THE RESIDUAL, carried rather than repaired** (`SUP:1826-1830`): **only the third row is enforced by
> construction.** A resistance that is neither plainly material nor plainly stance-composed — a forged
> document's quality, a fortification nobody has seen — **has no ruled row**, and this document does not
> invent one.

### §5.6 What `mint` and `efface` do at RESOLVE

**`mint`.** The spec `(type, kind?, parent, initial[], slot)` is realised: `id = H(world_seed, tick,
actor_id, "mint:" + slot)`; the object is created with its declared initial state; **the id is available
to the same act's later touches**, which is how "found a hearth here and make me its head" is one act.
The declared `(parent_of(object), alter)` entry is applied, which is what put the act into the conflict
graph.

**`efface`.** The object is destroyed, and:

> **`efface` sets `until = tick` on every `Tenure` whose subject or object is the effaced id, and
> effaces nothing else.** A tenure over a razed settlement becomes a **historical fact people still
> argue about**, which is what `until?` was added for. **Nothing cascades into a ledger**: claims about
> the destroyed thing remain, at their existing confidence, until their holders learn — which is the
> ordinary epistemics and is the whole point.

**Effacing a Container requires its `contain` children to be re-parented in the same act.** There is no
orphaning operation, because a person's address is *their path to the root* and a bare `revoke` on
`contain` leaves them with none (`ARCH §2.3`).

⚠ **`efface` may not target a Claim in another person's ledger** (R-2, `SUP:379-380`). The purge runs
through §5.9 instead.

### §5.7 The `condition` accumulator

```
Δcondition(site) = − condition(site) x f(degree) x share(actor, site)
f(Disaster) = f(Failure) = 0 · f(Costed) = 1/16 · f(Clean) = 1/8 · f(Overwhelming) = 1/4
share(actor, site) = the actor's own draw ÷ the site's total draw  ∈ (0, 1]

condition(site) = clamp(condition(site) + Σ this season's deltas, 0, 1)   -- RESOLVE ONLY
```

**Restoration is the mirrored form**, `Δ = +(1 − condition) × f(degree) × share`, so a dead site has a
road back and the restoration faction has an achievable programme.

> **You can never move more of a site than your own share of it, times a degree fraction.** At a commons
> with many drawers, **single-act closure is impossible** — one boat among forty moves at most a
> fortieth of a quarter in a maximum-degree season — so **closure is a collective outcome**, which is
> the tragedy-of-the-commons shape the mechanism exists to produce.
>
> ⚠ **At `share = 1` one Overwhelming season moves a quarter of the condition, and that is correct
> behaviour rather than leverage**: §14 row 11 forbids *a personal effect on a group that is not a
> fraction of that group*, and **at `share = 1` there is no group.** A man working out his own hearth's
> private seam in one hard season is wrecking his own property.

**Falsifier, stated and NOT run:** one person, one season, maximum-degree `alter` at a site with N
drawers — the fraction moved must be `≤ 1/4 × share` and **must fall as N rises.** If it does not fall
with N, the object has leverage.

**Band gating happens on the resolver's side.** `verbs(site, c) = { v : condition(c) ≥ floor(v) }`, and
**bands are published in full with their inputs and never with the trigger point that separates one band
from the next**. A closure is an Event, witnessable by presence at the site.

### §5.8 The sitting, at RESOLVE

A Date fired at CALENDAR. In the same season, at stratum 2:

1. **`compose_agenda(convener, container, date)`** — an act, costing the convener their season. The
   input is **the petitions the convener holds a claim of, not the petitions that exist**
   (`SUP:944-946`). He ranks them by his own valuation — the same `choose` every other act runs through
   — and admits the top `capacity(date)`.
2. **`determine`** — one person's decision at the venue, one of `remit.acts`' five, subject to the
   venue's `decision_rule` and `veto_holders`.
3. **The argument runs between them**, bounded by the venue's `exchange_budget` and `article_count`.

**Argument is resolved by named fault against a checklist, not by a persuasion threshold** — which is
what lets it run headless with no GM. Twelve faults, three severities: `strike` kills the ground at
every venue for everyone; `descend` concedes a rung and **closes nothing**; `close` force-closes the
sitting against the faulting party (`SUP:1536-1542`). **Force-close is the normal ending** — *most
arguments end because somebody was caught doing something that has a name*, and a threshold roll cannot
distinguish *he was wrong* from *he was caught lying*.

**The stasis ladder is entered by diagnosis, not by escalation.** Denial · Definition · Quality ·
Jurisdiction, strongest first. **The position you stand on is what you conceded, and how you arrived
there does not matter**: opening at rung *r* writes every rung above *r* into the record as conceded,
exactly as descending to *r* would. **Descending is irrevocable and public** (`SUP:1529-1531`).

**The door is two gates and the second is the one that bites.** A fisher may *enter* the Goldenfurt
court; he may not *speak* unless a person with standing carries his petition. **Caste is not a locked
door; it is a room you may stand in silently** (`SUP:1580-1583`). `admissible_source` is a **door for
evidence, not a grade**: a venue that hears instruments only cannot be reached by forty hamlet
witnesses — which is where `research`'s `told_by(record, …)` with a **verified** rootprint
(`03:528`) becomes load-bearing, and it is why *"archives are the only non-person root-bearers"*.

> **Where the fault check is not decisive and the venue's `decision_rule` requires a contested judgment,
> that judgment is a `contest`, and a contest subdivides the tick.** That is the seam at `ARCH §8`. The
> sitting itself is in scope and resolves here; the deferred **social contest** subsystem is the nested
> opposed-roll loop a contest may open, and nothing about it is specified in these documents.

**An omitted petition is a DROP and deposits exactly as one** (`SUP:953-958`). So burial is not free; it
is merely **safe** — it loses on `regard_cost` and forfeits `regard_gain`, and wins only on capacity.
**The counter to a burying convener is not a mechanism, it is another door** (`SUP:913-937`), and
burying only wins outright where the obstructor controls every venue that could hear the matter.

### §5.9 The purge, at RESOLVE and at the venue

> **YOU CANNOT DELETE ANOTHER PERSON'S MEMORY, AND THAT IS CORRECT. What can be destroyed is an idea's
> STANDING, and the mechanism is shipped: `strike`, which *"kills the ground at every venue for
> everyone"* (`SUP:1540`).**
>
> **Ideas are purged at the venue, not in the ledger.** A struck ground is dead everywhere, publicly, by
> a named person, on a named fault — which is exactly how heresy, attainder and the discrediting of a
> witness actually work.

**Plus the documentary limb, and it needs NO fifth claim source.** `efface` a **Record** — a register,
a charter, a deed — which is matter at a Container. Every claim sourced `told_by(that record, …)`
(`03:528`) loses its corroboration, because the token it copied is void. ⚠ **An earlier version of this
document added a fifth constructor, `documented(record_id)`. It was a reinvention of shipped machinery
and is withdrawn** (`ARCH §5.4`).

⚠ **AND THE CONFIDENCE DROP IS GATED, or arson is a §14 row 3 broadcast.** **The drop fires for a holder
only when a claim that the record is gone lands in THAT holder's ledger** — at WITNESS, in whatever
season the news arrives. **Arson's effect map is the news map**, exactly as a death's is.

⚠ **The pre-v2 brief's version of this limb is withdrawn in full.** It had `efface` drop confidence *"for
everyone whose claim cites it"* with no gate at all, and it claimed *"`SAID` claims already make a recantation
collide"*, which is false: collision needs *same subject, same predicate form, **same arguments***
(`SUP:229`), and `SAID(A, ¬C, s12)` differs in arguments from `SAID(A, C, s12)`.

### §5.10 Compliance, at RESOLVE

⚠ **A compliance contest is ENTERED BY AN ACT ON EITHER SIDE, and this document rules it so.**
`SUP:1139-1147` can be read as an automatic per-Container contest each season. **That reading is refused
on `SUP:1599-1601`: there is no fallback — if no person acts, the thing does not occur.** The ruling:

> **The compliance contest fires at RESOLVE when a person acts on either side** — an enforcement act
> (stationed, dispatched, or the executor's own compliance), or a resistance act (evasion, open
> defiance, a countermanding dispensation, arrears carried to the next date). **Where neither side acts,
> nothing happens, and the dispensation is simply unobserved.**

The roll reads **enforcer_presence** (zero if the issuer has no one to send), **local judging-set
stance** (derived on demand, never stored) and **distance**. **Failure is never an exception**: partial
compliance per hearth, quiet evasion, open defiance, local countermanding, or arrears compounding
toward the next standing date.

**Three rules, and the third is the whole of it** (`SUP:1155-1163`): scope enumerates **executors, not
places**; **delivery is not assumed**, and an executor who never received it is *distinct from one who
received it and refused* — the two being indistinguishable from above without an act that goes and
looks; and **reports are claims, not state.** *"Compliance was rendered"* is a claim by a named person,
with all the ordinary properties of claims. **It can be false, and it is what the centre has instead of
knowledge.**

### §5.11 RESOLVE's refusals

| it may not | because |
|---|---|
| take a `Person` parameter | `SUP:148-149`: the world does not know who is asking, which is what keeps the resolver from acquiring per-actor special cases |
| branch on `verb` | `ARCH §2.4`: a verb is a name, `touches[]` is the mechanism, and an open verb list must not grow the resolver |
| branch on a named entity | §14 row 13 |
| carry a second resolver, an auto-resolve formula or a fast path | §14 row 8; the three fidelities differ only in **who is asked to choose** (`SUP:617-620`) |
| write a ledger | that is WITNESS's class, and `witness` is the only bridge |
| depend on act order | `SUP:611-613`; §10 below |
| read the event log | `SUP:613-615` |

---

## §6 · WITNESS

**Barrier. Global fan-out, then a per-person map. Write class: INTERIOR — one person's own ledger.**

```
WITNESS(events, world):
  1. for each Event e:
        reach(e) <- persons present at e
                  + persons a channel carries e to, at that channel's latency
                  + Knot partners, REUSING e's own event id
  2. for each person p, independently, in any order:
        for each e in reach(p) this season:
            claims <- witness(p, e)
            deposit each, computing collision at deposit time
        confidence of every claim decays
        while ledger(p) is over budget:
            evict the lowest confidence_live x recency
```

### §6.1 Step 1 is global; step 2 is interior

**Which ledgers an Event reaches is a function of where everybody is** — presence, channels, Knots —
and that is cross-person by construction. **Which claims it becomes is a function of one person's
ledger** and touches nothing else.

**A Knot deposit REUSES the originating event's id** (`SUP:245-246`), so five partners feeling one
rupture supply **one** token — exactly as five men repeating one rumour supply one. **This is the
corroboration mechanism and it fails closed.**

> **CONSENSUS BROADCAST IS A TYPE ERROR.** There is no signature accepting a collection of persons and
> one Event (`SUP:150-151`). §14 row 3 is not a rule the resolver checks; it is a shape the type system
> makes unwritable.

### §6.2 Deposit and collision

```
Claim = (id, subject, predicate, value, when, source, confidence, visibility)
source ∈ firsthand(event_id) | told_by(person, handle) | inferred(claim_id…)
       | firsthand_via_knot(event_id) | documented(record_id)
```

**`when` is a mandatory closed interval and it is universal, never existential** — a claim asserts its
value held *throughout*. If intervals were existential, denial would need a universal over the
complement and the engine would carry two claim logics with two collision rules (`SUP:223-226`).

**Claims collide iff same subject, same predicate form, same arguments, intersecting `when`,
incompatible values. Collision is computed at deposit time, in ONE LEDGER AT A TIME**
(`SUP:228-229`). There is no world-level consistency check and there is nothing that could perform one.

**The predicate vocabulary is CLOSED; the referent space is OPEN** (`SUP:231-234`), because collision,
entailment and relevance are all functions of the predicate's *form*. **The membership is enumerated in
full at `03:66-79` — FOURTEEN forms**, listed at `03_COMPENDIUM.md` §2.7. ⚠ *An earlier version of this
document said the membership was enumerated nowhere. It was, in the document that owns it.*

**One entailment table, no grammar** (`03:104-108`): `LOCATED` at a district entails `LOCATED` at its
settlement; `ALIGNED` at member entails `ALIGNED` at sympathiser; `HOLDS_STANCE` at *primary* entails
*held*; **a narrower interval entails nothing about a wider one but is contradicted by a wider
denial.** And **negation is a VALUE, not a form**, which is why assert and deny land on the same row.

**There is no null source, and `witness` is the only operation that MINTS a root token**
(`SUP:243-245`, `03:411-413`). **Four constructors and no fifth**, and `03:432-464` proves the closure
rather than asserting it: `firsthand` mints and requires an event and a witness with vantage;
`told_by` **copies** tokens and cannot create them — including `told_by(record, …)`, whose rootprint is
*verified* rather than *asserted*; `inferred` **unions** premises and **refuses the inference if the
union is empty**; `firsthand_via_knot` **reuses the originating event's id**, so five partners feeling
one rupture supply one token. **There is no path to an empty ancestry, so repetition cannot become
corroboration**: a rumour told three times hashes to one synthetic root and the multiplier stays 1.0.

### §6.3 Decay and eviction

> **EVICTION RANKS ON `confidence_live × recency` AND ON NOTHING ELSE.**

⚠ **Never on stance-weighted salience, or motivated *retrieval* silently becomes motivated *deletion*.**
Under stance-ranked eviction the Templar's exonerating claim is the lowest-salience row in his ledger
every season, so `SUP:262-263`'s *"what is attenuated is retrieval, not value"* stops being true within
a few seasons — and the worked example the epistemic layer is built on becomes false about itself.

Those two are also **the only clock-driven quantities the design admits for memory**: matter, bodies,
and the confidence of a memory (`ABS:280`, citing `09:562-564`). Ranking eviction on anything else adds
a fourth.

⚠ **The eviction ranking is therefore a DIFFERENT FUNCTION from the retrieval ranking.** Retrieval's
`salience` carries `relevance(c, q)` and `stanceweight`; **eviction has no question `q` in scope at
all** — and `relevance(c, q)` is *defined* (`03:342-344`) precisely **against a question**, so with no
`q` it has no value. The prior design says only *"evict lowest salience"* (`SUP:654`), which therefore
**names a function that cannot be evaluated at the point it is invoked.** That is the defect, and the
two-term ranking is the repair. ⚠ *An earlier version of this document said `relevance` was undefined
in the corpus; the true and narrower claim is the one above.*

**This is forgetting, not a data limit** (`SUP:654`).

### §6.4 WITNESS's refusals

| it may not | because |
|---|---|
| deposit into more than one ledger per call | `witness` is per person; the collection form does not exist |
| deposit a claim with no source | `SUP:243-245` |
| mint a root token anywhere but here | same. The six investigative acts do not breach it: `examine`, `surveil` and `Thread-Read` register **facets** `resolve` emitted; `reconstruct` **unions** existing roots and refuses an empty union; `interview` and `research` produce `told_by`, which **copies** (`03:432-464`, `ARCH §5.11`) |
| reach into another person's ledger | R-2, `SUP:379-380` |
| write anything but a ledger | wrong class |
| evict on salience | §6.3 |

---

## §7 · CENSUS

**Global pass. Shares WITNESS's join. Write class: MATTER.**

```
CENSUS(world):
  1. L <- the post-eviction ledger set, read ONCE
  2. for each cohort c:
        for each individuation trigger that fires over L:
            mint a Person out of c; weight(c) -= 1
  3. for each person p:
        if  no Knot  and  no office  and  no live petition
        and no other person's ledger in L names them:
            de-individuate p into their cohort; weight += 1
  4. reconcile envelope weight against records drawn and returned
```

### §7.1 Why this is one global pass and not part of the map

⚠ **De-individuation is order-dependent, and the prior brief had it inside the per-person map.** Its
predicate reads *"no other person's ledger names them"* (`SUP:209-210`). **X survives or vanishes
depending on whether Y's eviction ran first** — if Y's ledger evicts the only claim naming X before X is
evaluated, X de-individuates; in the other order, X survives. Both orders are legal in a parallel map,
and **nothing errors either way.**

**CENSUS reads the post-eviction ledger set ONCE, and evaluates every person against that one snapshot.**
That is what makes the parallelism claim true rather than asserted.

**Individuation also writes globally** — it creates an addressable object and moves cohort weight — so
it belongs here for the same reason.

### §7.2 The triggers, and the roster ruling

⚠ **Two declared-exhaustive rosters ship and they are not the same five.** `09:535-537` gives five
churn-side triggers; `02:573-576` gives five person-generation triggers; `02:543-552` gives **four**
individuation triggers.

> **RULED under `SUP:271-273` — the document whose declared subject is the object wins, and doc 02's
> declared subject is the person.**
>
> **Person generation, exhaustive** (`02:573-576`): individuation · a succession pointer resolving to an
> heir who does not yet exist · an admission act needing a candidate · a petition needing a carrier at a
> rung with no live person · a view assembly requiring a subject the observer is looking at.
>
> **Individuation, exhaustive** (`02:543-552`), nested inside the first: **Named** (an act, telling,
> witness resolution or petition-backing requires a *specific* referent inside the cohort — the praefect
> fines "a smuggler" and the engine must produce one) · **Spread** (`spread > 3` on the −5..+5 scale
> with `weight ≥ 2`, split at the modal cleavage) · **Divergent view** (a claim whose channel reaches
> only part of the cohort — a Knot, a parish, one alley — split by channel reach) · **Capability
> demand** (an attempt needs a practice at rank ≥ r that the centroid lacks but the spread implies some
> members hold).
>
> `09:535-537` is a restatement of individuation from the churn side and is subsumed.

**The split is moment-preserving**: children's weighted stance means reconstruct the parent's, and
`weight −= n`. **When weight reaches 1 the record *is* a person — there is no conversion operation**
(`02:553-555`), which is what *one type, not two* means mechanically.

### §7.3 What a minted person is handed

**Address from the cohort. Marks from the cohort plus its variation. Capability from its distribution
CONDITIONED ON THE NAMING EVENT. Stance from its aggregate PLUS DISPERSION** (`09:539-540`).

⚠ **The two conditionings are different and the prior brief flattened them into one.** Capability is
conditioned on the event; dispersion applies to stance. Not "from the envelope plus its dispersion".

**And the memory.** `09:541-548`: tellings are stored **at the channel**, not per person, until
individuation, so a person minted in season 40 is handed the claims their address's channels would have
deposited. *They have a plausible past because their channel has a real one.* **Handed, not copied:**
each stored channel claim carries a construal distribution and **the minted person DRAWS from it**, so
two brothers minted out of one hamlet in one season can hold opposite construals of the same
twenty-year-old proclamation.

⚠ **WHERE THE CHANNEL STORE LIVES IS OPEN, AND THE PRIOR BRIEF'S ANSWER IS RULED AGAINST THREE WAYS**
(`ARCH §5.3`): *"Knowledge lives only in ledgers"* (`SUP:74-75`) and a Container is no more a ledger
than a channel is; the Container row's own test is *"The line is provenance, not location"*
(`SUP:355-360`) and stored tellings **are** derived from persons and **do** go stale against them; and
the dormancy ruling already decided this exact move (`SUP:746-748`). §14 row 7 independently forbids a
knowledge value stored on the thing known.

**CENSUS works without it** — a minted person can be handed nothing and simply have a thin past — but
the *plausible past* property is not delivered until this is closed.

### §7.4 De-individuation, and the design principle inside it

> **A PERSON PERSISTS EXACTLY AS LONG AS SOMEBODY REMEMBERS THEM** (`SUP:212`).

The predicate is conjunctive and has four clauses: no Knot **and** no office **and** no live petition
**and** no other person's ledger names them. **It is a design principle rather than a budget cap**
(`SUP:207-210`), and it is what makes the ledger the substrate of existence rather than a memory
optimisation.

**Coherence-0 is de-individuation by another cause** (`ARCH §7`, F4): at 0 the person stops generating
acts and **remains a Person record**, because other people's claims about them persist and their ties
still exist. ⚠ **Its cost is stated and unrepaired: a Coherence-0 person holding an office freezes that
seat, and vacancy-by-absence must reach them or the seat is stuck.**

### §7.5 CENSUS's refusals

| it may not | because |
|---|---|
| create a person for whom nothing asked | `02:577`: *nothing generates without a demand* — no monthly cohort of parentless sixteen-year-olds |
| run on a clock | same |
| read a partially-evicted ledger set | §7.1; the whole reason it is one pass |
| write anything social | wrong class |
| convert a cohort into a person by an operation | `02:553-555`: at weight 1 the record **is** a person |

---

## §8 · THREE SEASONS, WALKED

⚠ **These traces were not run. They are hand-worked arguments about what the steps above would do, and
every number in them is illustrative rather than computed.** They are here because a loop that cannot be
walked by hand is a loop nobody can debug.

### §8.1 A famine season at a hamlet whose praefect died last winter

| step | what happens |
|---|---|
| **CALENDAR** | the tithe reckoning fires at Grauwald. The **granary allocation date** at the hamlet also fires — **and its allocating office is vacant.** A convening condition attached three generations ago by a praefect nobody alive met — *"when the container's larder band reaches Hungry, schedule a relief sitting at the territory court"* — evaluates **true** and schedules a date at the court's next horizon. Step 4 recomputes options: the hamlet's `condition`-gated verbs are unchanged; two suppressed grievance rows at the hamlet find their enabling claim still unmet |
| **MATTER** | `yield` rolls `d10 = 2` on the hamlet's two holdings — a bad season, 0.59× base. `stores` goes negative at four hearths. Bodies age; one infant dies; envelope weight moves. **The vacant allocation date allocated nothing. The stock sits in the granary.** Nobody did anything wrong |
| **DELIBERATE** | at each hearth, `sense` returns `subsistence` above 1.0, which **outweighs stance entirely** (`SUP:1408`). `opening_set` offers the five channels open to a postless person: requisition kin, petition, take an opening, migrate, commit to a rival proposition. The cohort of forty landless labourers, evaluated **once**, chooses `commit` toward a proposition its members already hold grievance toward the container about — **grievance makes commitment cheap** (`SUP:1085-1088`). Three named hearth-heads each choose `petition`; one chooses `carry`, because he is the only man in the hamlet with standing at the court |
| **RESOLVE** | stratum 2: nothing is on the court's docket yet, because the carrier's `carry` resolves **this** season and the relief date is next season. Stratum 4: `commit(+Δ)` edges are minted — one from a cohort of weight 40. Stratum 5: three petitions exist as objects; the carrier's `carry` mints a **DocketItem** on the court's relief Date. Events emitted |
| **WITNESS** | the carriage is witnessed by the eleven people in the market square. It reaches the backers of the petition **as and when the telling arrives**, not now. The `commit` is **covert** and deposits nothing anywhere — concealed alignment deposits no claims, which is why the praefect who will drop this petition next season *"holds no claim that the hamlet can hurt him"* (`SUP:900-904`) |
| **CENSUS** | the cohort's spread on the referent *the territory court* now exceeds 3 with weight ≥ 2 — **Spread fires** — and the cohort splits at the modal cleavage. One of the children has weight 1 and **is** a person. He is handed his channel's claims and **draws** a construal of the twenty-year-old proclamation that differs from his brother's |

**What the design produced with nothing authored:** a famine, a faction forming out of a physical fact,
a named man who will be blamed, and a person who did not exist last season and now has an opinion.

### §8.2 A founding-and-annexation season

| step | what happens |
|---|---|
| **CALENDAR** | a conferral date opens at the parent office, because the Duke of Varfell died at MATTER two seasons ago and the news has now reached the capital |
| **MATTER** | ordinary. `yield` is average. The march that has been travelling for two seasons advances its last leg and **is now present** at the Varfell territory |
| **DELIBERATE** | the King, who holds one act like everyone else, chooses `confer` — a `hold` Tenure over the **Varfell Container**, to a Proposition (his own realm-faction). **Annexation.** A rival Duke, who does not yet hold a claim that the King is present, chooses `confer` of the same `hold` to *his* proposition. A hearth-head in a river hamlet chooses an act whose `touches` **mints a Container** of kind Hearth for his second son, plus a `contain` edge putting the son inside it — one act, two touches, the minted id available to the second because it was computed from the substream before resolution |
| **RESOLVE** | **the conflict rule fires on cardinality**: `hold` over a Container is **1 per object**, and two `mint`s of that edge jointly break it. Routed to `contest(Varfell, hold-of-Varfell, {King's men present, rival's men present})`. The King's side rolls the establishment's pool, not his own — *choosing which of your people performs the act is the whole of a leader's tactical choice* (`SUP:436-438`). He wins at Clean Success. **The containment tree does not move.** Varfell is where it always was; who holds it changed. The hamlet founding is uncontested and resolves at stratum 4 |
| **WITNESS** | the conferral is **public, because every act by remit is public** (`SUP:441-443`) — an office-holder cannot act quietly. It deposits by presence and channel, at channel latency. **The fjord hamlets do not know yet.** The rival's failed attempt is witnessed by whoever was there and by nobody else |
| **CENSUS** | the second son, who was a cohort member, is **Named** by the founding act and individuates. The new hearth's envelope is initialised from its parent Container's |
| **next season** | the compliance contest. The Varfell praefects each hold, or do not hold, a claim that they are now the King's. **Thirty-five separate decisions**, and `enforcer_presence` is zero everywhere the march did not go |

**What did not happen:** no war layer, no annexation verb, no re-parenting, no second resolver, and no
faction gained a `tier` field.

### §8.3 An investigation-and-sitting season

| step | what happens |
|---|---|
| **CALENDAR** | the chapter sitting fires. Its door reads `admissible_source = witnessed deed only` — **so a document cannot reach it**, which is why the Löwenritter is caste-open in fact and not by policy (`SUP:1589-1591`) |
| **MATTER** | ordinary |
| **DELIBERATE** | an investigator's `Sensation.standing` is low and his `commitment` need — read from his **view** — is unmet: he holds a claim that a steward reported compliance that was never rendered, and his own proposition says the steward is lying. `opening_set` offers the six investigative acts. He chooses **`interview`** — cheap, fast, and it leaks. **It costs his season, like everything else.** The steward, elsewhere, chooses `tell` — a distortion |
| **RESOLVE** | stratum 2: the chapter's convener spends **his** act on `compose_agenda`, admitting the top `capacity(date)` items **from the petitions he holds a claim of**, and omitting one. That omission **is a drop and deposits as one**. The determination runs: a party pleads a Ground whose `support[]` cites claims he does not hold — **F7, rootless ground, severity `strike`** — and the ground is dead **at every venue for everyone**. That is the purge limb, working. Stratum 3: `investigate` resolves against a `resistance_pool` composed from the concealment of what is hidden, in the same dice-equivalent unit as a lock's fineness. **Costed Success**: something comes back, and something is given up for it |
| **WITNESS** | `interview` yields the target's **`SAID` row** — a `told_by` claim, which **may be a lie** — plus, unconditionally, `INTENDS(the investigator, investigate X)` deposited **in the target's own ledger**, tellable onward (`03:527`). **The target now knows what he is asking.** No root token is minted: `told_by` copies. The steward's telling reaches four other ledgers at a distortion. **Two witnesses of one event now disagree**, which is one of the four structural tests and has never been run |
| **CENSUS** | the struck party holds no Knot, no office, no live petition — but three ledgers still name him, so he persists. **A person persists exactly as long as somebody remembers them** |

---

## §9 · THE WRITE MATRIX

What may be written, by which step, and what happens if it is written elsewhere.

| written thing | CALENDAR | MATTER | DELIBERATE | RESOLVE | WITNESS | CENSUS |
|---|---|---|---|---|---|---|
| `Date`, `DocketItem` | **yes**, including every conferral date a vacancy opens | **no** — a death sets `until`; the DATE waits for CALENDAR | no | **yes** — `carry` mints an item, `convene` sets a date | no | no |
| larders, `stores` | no | **yes** — metabolism | no | **yes** — `transfer`, `levy` | no | no |
| bodies, ageing, death | no | **yes** | no | no — killing is an act's effect, and that is ACTS class | no | no |
| travel legs | no | **yes** | no | **yes** — a movement act, stratum 1 | no | no |
| `yield` | no | **yes**, and only here | no | no | no | no |
| envelope weight | no | **yes** — births, deaths | no | no | no | **yes** — individuation |
| `condition(site)` | no | **yes — `wear` ONLY** | no | **yes** — every act delta, and only here | no | no |
| `Tenure` | no | **yes** — `until` on death | no | **yes** — `confer`, `revoke`, `mint`, `efface` | no | no |
| Person, Container, Office, Site existence | no | **yes** — death only | no | **yes** — `mint`, `efface` | no | **yes** — individuation |
| `stance` | no | no | no | **yes** — an act's effect | no | no |
| ledger | no | no | no | no | **yes**, own only | no |
| a returned `Act` | no | no | **yes**, and nothing else | — | no | no |

**Any cell not marked `yes` is a write-class violation.** Four worked cases where a cell was wrong:
an **act's effect** on `condition` at MATTER (corrected at `SUP:679-684`, and still forbidden — the
MATTER cell above is `wear` and nothing else); individuation inside the per-person map (corrected
here); the reckoning operations, which had no class at all (corrected here by naming the INTERIOR
class); and **a death opening a conferral Date at MATTER, which this document did in its own first
version against its own matrix** (corrected at §3.3).

⚠ **`condition` now has TWO writers in one season, and the clamp rule survives it.** §5.2's *"sum the
deltas and clamp once"* quantifies over **concurrent** writers inside RESOLVE, where order is not
defined. `wear` is applied at MATTER, **strictly before** any of them, so it needs no commutativity
argument at all: one ordered subtraction, then one summed-and-clamped batch.

---

## §10 · ORDER INDEPENDENCE — FOUR PROPERTIES, AND HOW EACH IS OBTAINED

**Order independence is the property to guard, because its absence is invisible** (`SUP:611-613`).

| property | obtained by | what would break it |
|---|---|---|
| **showing a player a possibility cannot change what happens** | per-operation substreams; the exposure preview never calls `roll` (`SUP:574-575`) | a shared RNG sequence |
| **two attempts resolved in a different order give the same answers** | substreams keyed on `(world_seed, tick, subject_id, purpose)`, never on a sequence position | any counter |
| **adding a person somewhere does not re-phase every other roll** | the same | a global draw order |
| **the per-person maps may run in any order** | they write nothing global — individuation and de-individuation moved to CENSUS, and ids need no allocator | a shared id allocator; de-individuation reading a partially-evicted ledger set |

**And one property that is NOT obtained and must be stated:** ⚠ **the DELIBERATE map's purity is a
property of what `sense`, `assemble`, `opening_set` and `choose` are allowed to touch, and nothing
enforces it structurally except the absence of a `World` in `choose`'s signature.** `sense` *does* take
a world. **If `sense` ever returned anything but two scalars, the enforcement would be gone and nothing
would say so at the call site.** That is the one place in this loop where a careless implementation is
not caught by a type.

**Replay is a re-run, not a log**, and **no decision function may read the event log** (`SUP:613-615`).

---

## §11 · WHAT THE LOOP REFUSES TO DO

1. **There is no fallback.** *If no person acts, the thing does not occur.* No distribution just
   happens, no garrison is assumed paid, no repair is presumed made. **The engine has no caretaker,
   because there is no GM to be one** (`SUP:1599-1603`).
2. **Production is metabolism; distribution is politics.** Nature yields, larders consume, bodies age —
   no act required. **Grain moves because a named person decided it should** — an act, always.
3. **Exactly four decider-free channels and no fifth** (`ABS:269-277`): metabolism and nature · matter
   events · the confidence of a memory decaying · **the calendar, LAPSE ONLY**.
4. **Exactly three clock-driven quantities** (`ABS:280`): matter, bodies, and the confidence of a
   memory. **Standing, regard, grievance, cohesion and commitment move only when an act causes an
   event**, and **no band edge may ever be defined over one of them**.
5. **Reaction latency at person scale is one season**, so surprise is structurally possible: no policy
   can say *"if he does X, I do Y, this turn."* **You anticipated or you are late** (`SUP:656-658`).
6. **Nothing happening is the characteristic outcome, and it is not repaired.** A vacant office is not a
   defect to route around. A three-of-four conclave with two seats empty is **not a soft-lock; it is a
   Church that stalls**, and breaking the stall is political work for characters (`SUP:1053-1064`).
7. **No threshold fires an outcome.** The one licence claimed is the **matter channel** — a band edge
   closing a verb — under three conditions, all of which hold: the quantity crossed is matter, what
   changes is an **option set** and never a roll term or an outcome, and the closure is an **Event
   witnessable by presence** (`SUP:1370-1381`).
8. **No apparatus.** This document proposes no validator, guard, register, checker or process document,
   and the loop requires none (`11_code_shape.md:243-245`).

---

## §12 · OPEN, AND STATED LIMITS

**Open, carried rather than answered** — the full list is `ARCH §11`; these are the ones that bite
*inside the loop*:

1. **Where the season's question `q` comes from.** §4.1 names a defensible default and does not assert
   it. ⚠ **`relevance(c, q)` is NOT open — it is defined at `03:342-344`.** What has no producer is
   `q`, and that is what makes `SUP:654`'s *"evict lowest salience"* uncomputable at eviction.
2. **Where the channel store lives.** §7.3. CENSUS runs without it; the *plausible past* does not.
3. **`season_factor(territory)`'s distribution.** §3.2. MATTER rolls it every season and nothing states
   its range, mean, shape or tail.
4. **The `R ≤ 1 → return 0` branch.** §5.4. A fast path by the review's reading; deleting it moves the
   odds of every trivial attempt, which is a balance question nothing here can settle.
5. **§14 row 4's construal-spread rule** — where a cohort's stored spread lives, what produces it, and
   what an individuating member draws from. Under-specified upstream at `SUP:1737`; it bites at §7.3
   and at every cohort witnessing.
6. **The empty judging set.** An office whose judging set is empty has no self-convening route, so
   CALENDAR can schedule nothing for it. No floor is specified.
7. **The `exclude` limb of the anti-leverage row**, now widened by `efface` across four object classes.
   Inherited; no bound is invented.
8. ⚠ **STRUCK — the predicate vocabulary IS enumerated**, fourteen forms at `03:66-79`. This row
   previously called it open. See `ARCH §12.8`.
9. **The ratio of `wear` to a restoration act's effect** — Jordan's F6 ruling makes it the world's
   whole difficulty curve, and **no number in this design has been measured.**

**Stated limits:**

1. **Nothing here has executed.** The three traces at §8 were walked by hand; no program produced them
   and no number in them was computed.
2. **The four structural tests have not been run** (`SUP:1767-1770`), and three of them are exactly the
   properties this loop claims: no decision function can see the world · two witnesses of one event can
   disagree · order independence.
3. **The `Δcondition` falsifier at §5.7 is stated and has not been run.**
4. **The parallelism claim is an argument about what the steps touch, not a measurement.** It would be
   falsified by any shared mutable state this document has failed to notice, and the honest position is
   that a reading found none rather than that a run found none.
5. **This document is REFERENCE, not mechanism** (`CLAUDE.md` §0.05). If it were deleted, no behaviour
   would change — because no behaviour exists yet.
