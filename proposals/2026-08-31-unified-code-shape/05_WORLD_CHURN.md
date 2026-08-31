# 05 · WORLD CHURN — what happens when nobody does anything

## Status: PROPOSED (2026-08-31). **HELD BACK. Nothing here ratifies on merge.**
## Layer: **L3 — one step, elaborated.** This document is MATTER (`04` §3) plus the half of CALENDAR
## that fires without a decider. Read `01_THROUGHLINE.md` Law 4 first; this is that law's second row.

---

## §1 · THE RULING THIS DOCUMENT EXISTS TO IMPLEMENT

> **Jordan, verbatim:** *"The world is neither dying nor misunderstood — rather, it is in a state of
> flux. If the world is not tended to by anyone, it will die. If it is tended to by everyone, it will
> thrive. What people think is the best way to tend to the world, though, and their ambitions within
> that world, are the regions that drive conflict."*

**This is a third answer, and neither of the two options on the table offered it.** The fork as filed
was *a real trajectory the player must arrest* against *a fact everyone reports wrongly*. **Both fix the
world's direction** — one at negative, the other at zero with the variance moved into the reporting.
**The ruling makes the direction an OUTPUT: the sum of what people do about it.**

**That is why the fork survived five audits undissolved. The missing option was not a parameter. It was
a sign.**

| tending | arithmetic | outcome |
|---|---|---|
| **nobody** | `sum(acts) = 0`; condition falls by `wear` every season | it crosses a band floor, verbs leave, **the world dies and no person did it** |
| **everyone** | `sum(restoration) >= wear` | condition holds or climbs — **it thrives** |
| **some** | the **distribution** of tending decides **which sites** live | **that is the game** |

**Net cost of implementing the ruling: one constant, zero objects.**

---

## §2 · `wear` — the world's entropy, and the only per-season constant in the shape

```
condition(site) <- clamp( condition(site)
                        + sum(this season's resolved act deltas)      # ACTS class, at RESOLVE
                        - wear(kind(site)),                           # MATTER class, at MATTER
                        0, COND_SCALE )
```

**Four properties, each stated because each was got wrong somewhere before:**

1. **`wear` is in the SAME UNITS as `condition`** — a fraction of full condition per season, expressed
   as an integer on `COND_SCALE`. **It is not weather, not a multiplier, and not a roll.** The weather
   term and the harvest die stay exactly where they are, inside `yield`.
2. **Two writers, two classes, ONE clamp, applied once.** `wear` is written at MATTER; the act deltas
   are written at RESOLVE; **the clamp fires once, after both.** Clamping as you go re-introduces
   order dependence at the bounds.
3. **`wear` IS AN EVENT under the Partition, and needs no special case at all.** A harbour silts because
   harbours silt — a non-social subject, so the world drives it. **Tending it is a choice.** Both move
   one quantity, which is exactly the flux model, and the Partition explains why without special-casing
   either.
4. **It clears the ban on a scheduled recovery tick, and on the right ground.** That refusal governs
   **standing** — a social quantity — and `wear` moves **matter**. The clean argument is the write
   class, not a phase-membership accident: *nothing social moves on a clock, and `condition` is not
   social.*
5. **It is an authored per-season constant, and this shape says so out loud.** A prior design
   congratulated itself on having *no hidden per-season constant anywhere in the fuse*. This ruling
   **requires one.** The honest position is that it is **justified rather than hidden**: it is the
   world's entropy, it is the quantity the whole political layer exists to argue about, and **it belongs
   in the exported parameter table where code reads it — one row per site kind.**

> ⚠ **AND THE OPEN MEASUREMENT, WHICH THIS SHAPE CANNOT SETTLE AND WILL NOT PRETEND TO.**
> **The ratio of `wear` to a restoration act's effect sets the entire difficulty curve of the game.**
> Too high and the world dies whatever anyone does; too low and tending is decoration. **No number in
> this design has been measured. Nothing has been run.** This is a measurement, not a ruling, and
> `CLAUDE.md` §0.1 point 4 forbids settling it by assertion in either direction.

### §2.1 What `wear` converts the act economy into

Under an act-only fuse, restoration was **pure gain** and neglect was **free**. Under `wear`,
**maintenance is a permanent tax and neglect has a price.** So *"how many person-seasons does this
harbour cost to keep open"* becomes a **real, computable political quantity** — and every one of those
person-seasons is drawn from the one-act budget.

> **The act economy stops being a bookkeeping fork and becomes the thing factions actually fight over.**
> The two rulings — one act per person, and the world in flux — were made independently and converge.

---

## §3 · THE WORLD-SUBSTRATE OBJECT — the one confirmed hole, closed with zero new objects

**Three independent arc lanes, by three different routes, found the same absence:** there is **no
world-substrate quantity** — nothing representing the state of the Thread substrate the setting's
metaphysics rests on.

| lane | the route it came by |
|---|---|
| 1 | the single genuine LOST arc in its band is **the arc the corpus itself calls the one that must fire** |
| 2 | a document defers Thread operations to another document **that owns none of it** — a dangling pointer |
| 3 | **five of seven LOST arcs die on it**, and the design's otherwise-exhaustive refusal list **does not name it** |

> **This settles it as an OMISSION, not a refusal. Every other absence in this design is argued for by
> name. This one has a broken cross-reference pointing at where it was supposed to be.**

> ### THE CLOSURE
>
> **A Thread seam is a `Site`. Its `condition` is the substrate quantity. Its `wear` is a row in the
> params table. That is the entire fix.**
>
> **No new type, no new field, no new write class, no new step, no new verb.**
>
> **The argument, which is the arc lane's own and this shape accepts it:** the spine refuses gauges on
> containers **because they are social.** A substrate's condition is **the same class as larders and
> harvests** — which MATTER already ticks. *The shelf exists; nobody wrote the object.*
>
> **It satisfies the meta-rule exactly.** A fix that adds a system has failed; this adds none. It is one
> row in the `Site.kind` registry and one row in the `wear` table.
>
> **N-line.** Cut it and *the world is not dying — it is only being misunderstood*, which is precisely
> the branch Jordan's ruling rejected. Five LOST arcs stay lost.
>
> **Falsifier, and it is real.** Wrong if any Thread-substrate mechanic requires a quantity that is
> **not per-place** — a single global scalar with no site identity. **If the metaphysics needs one
> number for the whole peninsula, this is the wrong object and a genuinely new one is owed.**

**And the play this buys, which is why it is worth more than a hole being closed.** A Thread seam is a
Site, so it has **`drawers[]`** — the persons who draw on it. It has a **`hold` Tenure** — someone holds
the ground. It has a **`condition`** that gates verbs. So *the seam is running out* is not a status
effect: it is **a stake, at a rung, with claimants, a date, and a doctrine fight about how to tend it** —
and the doctrine fight needs no new object either, because a tending-doctrine is a `Proposition` of mood
`OUGHT` scoped to a class of sites, and two of them with intersecting scope **collide automatically.**

---

## §4 · THE ACTORLESS CHANNEL — events with no person behind them

**An event is any state change whose subject is not peninsular human society.** There is **no list of
channels to extend**, because there is no list: the Partition is a predicate, and *"which channels may
fire without an actor"* is answered by reading the `social` column.

**What that covers:** weather · `wear` · a body ageing and failing · a landslide exposing a seam · a
storm destroying a harbour · a tear opening in the substrate · pressure from off the peninsula.

> ⊕ **AND ONE CLAIM ABOUT THE OLD FOUR-CHANNEL LIST IS RETRACTED RATHER THAN REPEATED.** It is often
> said that the list *licensed matter events with nothing generating one.* **An adversarial pass broke
> that**: a generator existed — a bad seasonal roll closing the channel for a season. **The true, and
> more useful, statement is narrower: the licence named no generator in its own section, and the
> generator that existed sat two hundred lines away, unlinked.** The other two failures stand — `wear`
> was unwritable, and an authored event deck had no home. *An overstated finding with a true core is
> worth more corrected than repeated.*

### §4.1 The event row — one schema, not a second catalogue

An actorless row is **the same row an act uses, with two deltas** — verified field-for-field:

```
event_row:
  id, family, scope                      # scope is place | faction; never "world"
  origin: exogenous
  remit_kinds: []                        # DELTA 1 — always empty: a world event has no holder.
                                         # An empty remit is already legal in the grammar; this is
                                         # the clause's inapplicable-by-construction case, not a
                                         # weaker gate.
  triggers: [ <state predicates> ]       # ALL must hold. A gate, never a roll.
  hazard_pool: <int>                     # DELTA 2 — stands in for the actor's attribute pair,
                                         # because there is no actor to draw attributes from.
  resilience: { target_score, modifiers, M_max }     # what derive_ob reads
  cooldown: <int seasons, >= 1>          # REQUIRED and checked at load
  excludes: [ <event ids> ]              # mutually exclusive this season
  deposits: { overwhelming, success, partial, failure }   # TOTAL over all four bands
  follow_on: { record, key, ttl }        # a Record with a ttl — NEVER a scheduled future event
```

>  ⊕ **TRIGGER PURITY — the rule that keeps the actorless channel from reading society's temperature.**
>
> **An event row's trigger predicate may read ONLY `social: false` rows, plus terrain and season. It may
> never read a social quantity.**
>
> **This is not hygiene; it is the defect that was MEASURED in the shipped event deck.** Every one of
> its cards gated on one composite pressure quantity, **three of whose four summands are social** — so
> *the deck selected its events by reading society's temperature.* An actorless channel whose triggers
> read grievance is **not actorless**: it is the world reacting to politics with nobody deciding, which
> is the authored feeling the whole Partition exists to remove.
>
> **The Partition already forbids an event from WRITING a social row. Trigger purity is the same rule on
> the READ side, and without it the channel launders social state into world behaviour.**
>
> **Falsifier.** An event row that cannot be gated without reading a social quantity. **If one exists,
> it is not a world event — it is a consequence of what people did, and it belongs to an act.**

**The gate is a predicate over state, read at the moment of evaluation, never a roll.** Terrain
(immutable) and season (world state) narrow eligibility **categorically**; a condition band narrows it
**temporally**. **A drought gate that never reads terrain fires on a mountain fortress as readily as a
floodplain**, which is exactly the arbitrariness that makes an event deck feel authored.

**The roll reuses the one obstacle owner and the one ladder.** The hazard's fixed severity pool contests
**the place's own condition**: a place with strong condition presents a higher `target_score`, therefore
a higher Ob, therefore a harder margin for the hazard to clear. **A well-run place weathers a bad season
better than a neglected one, for free, out of arithmetic already in the design.**

**Effects fire on THREE of four bands, never only the narrowest.** Overwhelming, Success and Partial each
carry a declared, non-empty effect; Failure carries none. A row that fires only on its narrow band is a
row that almost never happens and therefore never has to be balanced.

### §4.2 Persistence is a Record with a ttl, never a scheduled future event

> **A "three-season drought" may NOT be one event scheduling two future events.**

**It cannot be, and this is a fact about the substrate rather than a preference:** the event queue's
drain **raises** if it is non-empty at the tick boundary, and there is **no transport that lands an
emission in a later season** [verified].

**What replaces it, and it is better:** a fired event writes a **Record** with a `ttl`. A
**continuation row** for the same hazard class declares that Record's presence as part of **its own
gate** next season. **So a sustained drought is three independent seasons of the same row re-evaluating
a gate that happens to still read true, each a fresh roll against the now-lower resilience** — never a
single event reaching forward in time.

**And the Record is a thing in the world, not a hidden flag.** It sits at a Rung, it is `destroy`-able,
it is an admissible source at a venue, and someone can **burn it**. *The register recording the levy
remission is the reason the levy is not collected, and it can be burned.*

### §4.3 Rate bounds, and why they are structural rather than tuned

| bound | mechanism |
|---|---|
| **at most one fire per target per season** | structural — the gate is evaluated once per target per season |
| **per-row frequency ceiling** | `cooldown >= 1`, **checked at load**, so a bad row fails at boot rather than in season 40 |
| **global ceiling** | the tick-wide emission cap, which **raises rather than clamps** — a breach is loud |
| **mutual exclusion** | `excludes[]`, the holderless equivalent of two of one actor's options competing |

### §4.4 An off-board polity is an event source, not a simulation

> **AN OFF-BOARD POLITY IS NOT SIMULATED. IT IS A SOURCE OF EVENTS.** Its pressure arrives as events
> acting on the world — a fleet appears, a levy is demanded, a border is crossed, a subsidy stops —
> witnessed per person by presence and channel like every other event, and **as disputable as the
> weather.**

**Three things this buys that generating off-board persons did not:**

1. **A large DELETION.** No off-map realm needs an envelope, an establishment, individuated persons or a
   second fidelity tier. **The suite gets smaller, not bigger.**
2. **Law 1 is preserved properly rather than by straining.** The one-actor rule governs **persons**, and
   an empire is not a person. **There is no exception to make, because the rule was never about the
   weather or about foreign empires.**
3. **It composes with the Partition rather than sitting beside it.** Off-peninsular pressure is one row
   of the non-social column. It needs no fork and no licence of its own.

**What it costs, stated plainly:** a player who sails off the map finds **no simulation at all**, not
merely a thin one. **If the played region is ever extended to include an off-board polity, that polity
becomes peninsular by definition and its state changes become characters' choices** — which is the
Partition doing its work, and a re-scoping of the map rather than a change to the engine.

**Falsifier.** Wrong if an off-board polity must **respond** to a specific on-board act in a way no event
kind can express. Then it is not an event source and must be simulated.

> ⚠ **AND THE GATE ON THIS THAT IS NOT A CAVEAT** [LANE B A7].
>
> **An actorless row must declare whether it is AGENTIVE or NON-AGENTIVE**, and **agentive rows are
> blocked until a criterion exists that stops any actor being reclassified as weather.**
>
> *A storm* is uncontroversially non-agentive. *An empire demands a levy* is an **actor's decision
> rendered as weather** — and if that is permitted with no criterion, then **the Partition's whole force
> evaporates**, because anything inconvenient to simulate becomes an event. Law 1 says all actions are
> performed by characters; an agentive actorless row is the one shape that can eat it from inside.
>
> **The non-agentive channel ships. The agentive channel is specified and gated.** This is a real
> precondition on a real mechanism, and it is the only thing in this document held back.

---

## §5 · WHAT ELSE MOVES WITHOUT A DECIDER — and the exhaustive list is three

> **EXACTLY THREE QUANTITIES ARE CLOCK-DRIVEN: matter, bodies, and the confidence of a memory. No
> fourth may be added.**

**Standing, regard, grievance, cohesion and commitment move ONLY when an act causes an event.** This is
enforced **by phase membership rather than by discipline**: MATTER's write class admits only metabolism,
so **there is no step in which a restoring timer could run**, and a design that wanted one has nowhere
to put it.

**The consequence, and it is the good kind.** A governor does not decay on a timer. **He loses the town
by being forgotten** — because the query that counts his authority counts only links whose subordinate's
ledger *currently asserts* who decides here, and claim confidence decays under the same universal rule
that governs every memory.

### §5.1 The two things that are NOT events, and it matters that they are named

- **A memory's confidence decaying** is **interior**, in the INTERIOR write class, and belongs to its
  holder. It is not an event; nothing witnesses it.
- **A lapse** — a date passing with nothing heard — is the **CALENDAR** class and is **the absence of an
  act**, not a change with a driver. **Nobody's act; nobody to blame; a real consequence.**

**Neither is an event and neither needs to be.**

### §5.2 No threshold fires an outcome

**A band edge changes an OPTION SET, never a roll term and never an outcome** — and its crossing is an
**Event**, witnessable by presence at the site.

> **This is where thirteen arcs that end at a scheduled sitting survive and three that end at a counter
> do not** — *in the one eighteen-arc band where that was measured; another lane reports the threshold
> refusal costing nothing in its own band.* (`06` §6.1.) An arc ending at a sitting survives because the design has
> standing dates with **named conveners who can be bought, delayed or killed.** An arc ending at a
> counter with nobody deciding **loses its ending** — and the loss belongs to the **variable**, not to
> the threshold.
>
> **The honest cost, stated:** *the design cannot resolve an arc whose premise is that nobody wants it
> resolved.* The threshold's real job in the old corpus was to be **the world's own agency — the one
> actor that is not a person.** Three mechanisms partly substitute — material need at MATTER, confidence
> decay, dormant rows re-arming at CALENDAR — but **none FORCES a position.** They make holding one more
> expensive.
>
> **That is the trade this shape takes deliberately**, and `14_NERS.md` prices it rather than hiding it.

---

## §6 · THE CHURN LEDGER — every channel, its writer, its class, its N-line

| # | channel | driver | write class | step | N-line: what is lost if cut |
|---|---|---|---|---|---|
| 1 | `wear` on every Site | Event | MATTER | MATTER | the world's direction stops being an output; tending is decoration and neglect is free |
| 2 | `yield` (harvest, extraction) | Event | MATTER | MATTER | material scarcity has no producer; the larder stops being the generator of need |
| 3 | ageing, illness, death | Event | MATTER | MATTER | nobody leaves; succession never fires; every office is held forever |
| 4 | birth (envelope weight) | Event | MATTER | MATTER | population is static; a cohort cannot grow into a claimant |
| 5 | travel legs advancing | Event | MATTER | MATTER | distance stops costing anything; presence becomes free |
| 6 | the actorless event channel (§4) | Event | MATTER | MATTER | **nothing ever happens to a place that nobody chose to do to it** — no bad season, no reason a governor's competence is tested by anything but a rival |
| 7 | off-board pressure — **NON-AGENTIVE HALF ONLY** (§4.4) | Event | MATTER | MATTER | the peninsula has no outside. ⚠ **The agentive half — a levy demanded, a subsidy stopped — is an actor's decision rendered as weather, and §4.4 BLOCKS it.** This row is not a licence for it |
| 8 | a band edge crossing | Event | — (it is an emission, not a write) | MATTER or RESOLVE | verb sets never change; a silted harbour is indistinguishable from a working one |
| 9 | claim confidence decay | interior | INTERIOR | WITNESS | **you cannot lose a settlement by being forgotten**; authority becomes permanent once granted |
| 10 | a date lapsing unheard | — (absence) | CALENDAR | CALENDAR | **the specific injury of being ignored** disappears; every petition gets an answer |
| 11a | an **event-created** Record's `ttl` expiring | Event | MATTER | MATTER | a cooldown cannot end; a hazard's residue is eternal |
| 11b | an **act-created** Record's term maturing | ⚠ **neither** — it is **the creating act's own declared term ripening** | ACTS (at creation) | MATTER | a remission that never runs out, a truce with no expiry. **It is an act ripening, not an event, and calling it an event hides who set the clock** |
| 12 | de-individuation | Event | MATTER | CENSUS | the person count grows without bound; the compute dial has one direction |
| 13 | **individuation** — a Person created with no decider, on demand | Event | MATTER | CENSUS | **the world cannot produce the person a situation requires**; the praefect fines a smuggler and there is nobody to be one |
| 14 | **claim eviction at the ledger cap** | interior | INTERIOR | WITNESS | **forgetting.** Without it a ledger is a perfect archive and nothing is ever lost, misremembered or unavailable when needed |

**Fourteen rows, and the count is not the point** — four of them are one mechanism (`wear`, `yield`,
ageing, births) seen at different subjects, which is the Partition doing its job.

> ⚠ **AND THE EXHAUSTIVENESS CLAIM IS SCOPED RATHER THAN ASSERTED.** An earlier draft of this table
> ended *"there is no thirteenth"* and was **wrong twice**: it omitted **individuation** (a person
> created with no decider) and **claim eviction** (a destroy at the ledger cap, with no decider), both
> of which are decider-free changes this suite ships. **Rows 13 and 14 are those two.**
>
> **The honest statement is not a count. It is the predicate:** anything whose subject is **non-social**
> is already covered, and anything **social** needs a person. **The list cannot be extended, but it can
> be — and was — under-enumerated**, and a table claiming completeness by counting is exactly the shape
> that hides the row it missed.

---

## §7 · WHAT THIS DOCUMENT REFUSES

| refused | because | what does the job |
|---|---|---|
| a scheduled recovery tick on any social quantity | converts a consequence system into a treadmill | acts, or nothing |
| a stored `unrest`, `stability`, `mandate` or `pressure` field | dead state that reads as mechanism | a `Query` over stances and claims |
| an event that schedules a future event | the substrate has no cross-season transport, and a scheduled future is a threshold wearing a costume | a Record with a `ttl`, re-gated each season |
| an event that grants or revokes an office **as its own act** | offices are social | the event depresses `condition`; **a person** then acts on the consequence. ⚠ **But see the declared seam below — a death DOES end a tenure, and the column alone does not explain why a storm may not** |
| an event that writes an aggregate | Law 3 | events write primary state only |
| a global "world state" scalar | it has no site identity, so no verb gate can read it and no one can hold it | per-Site `condition` (§3) |
| an authored crisis timeline | the world would churn on rails | gates over state, each with a cooldown and a rate bound |
| an agentive actorless row, **for now** | no criterion yet stops any actor being reclassified as weather | §4.4's gate — specified, held |
