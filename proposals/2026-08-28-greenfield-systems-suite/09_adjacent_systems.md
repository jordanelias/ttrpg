# 09 — Adjacent systems

> ⚠ **ARCHIVED / SUPERSEDED (2026-08-29).** This is the **pre-critique** version. It is retained
> unedited so the adversarial findings against it stay checkable — **do not build from it.** Six of
> its claims are known false; see [`ARCHIVED.md`](ARCHIVED.md). The live suite is
> `proposals/2026-08-29-greenfield-systems-suite-v2/`.


## Status: PROPOSED (2026-08-28) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) · [`05_faction_actions.md`](05_faction_actions.md) · [`06_faction_management.md`](06_faction_management.md)
## Produces: the four systems the eight named ones cannot be built without

Four things the brief's eight systems each reach for and none of them owns: what happens when a post
falls vacant at the top, what a faction's armed force actually *is*, where motions come from, and how
any of it crosses a scale boundary without a bespoke channel.

---

## 1. Succession and collapse

Under ED-IN-0201 a vacant head post stops a faction acting, so **succession is the mechanism that
decides whether a faction resumes existing as an actor.** It is the highest-stakes resolution in the
strategic layer and it must be the least eliminatory.

### 1.1 Two paths, declared by policy

`06 §5`'s `succession rule` policy picks one:

| policy | path |
|---|---|
| **designation** | the outgoing holder's declared successor takes the post, gated only on `pm.candidates`. If the designee no longer qualifies, fall through to claim-contest |
| **claim-contest** | the two highest-`preference` qualified candidates contest it (§1.2) |

Designation is cheap and produces continuity; contest is expensive and produces politics. Which a
faction uses is a property of the faction, declared as data, and it changes hands when a head changes
it — which is itself an action with a `Precedent` tag.

### 1.2 The claim contest

```yaml
resolver: d_sigma
shape: DO — both claimants roll; the margin between them decides
```

| element | value |
|---|---|
| pool, each side | `attr[social_a] + attr[social_b] + POOL_BASE`, plus the σ-space contribution of their backers' edge dispositions, capped per `01 §2.4` |
| obstacle | **none.** This is one of the few genuinely two-sided resolutions in the game |
| what is read | the single-owned margin ladder, applied directly to the **differential** `net_a − net_b` |

**"No obstacle" is a real distinction here, not a dodge.** `OB_MIN` floors an *obstacle* — a
difficulty the world presents. A claim contest has none: the difficulty is the other claimant, and
the quantity the ladder reads is how far one net cleared the other. Reading the same four bands off a
differential keeps the contest on the single-owned ladder without inventing a second degree
semantics, and without pretending a zero-valued obstacle is an obstacle.

Three outcomes, and none of them eliminates a faction:

| margin | outcome |
|---|---|
| ≥ 3 | **decisive** — the winner takes the post; the loser takes a `Grudge` and a `standing` deposit down |
| 1 … 3 | **contested** — the winner takes the post; the loser retains a durable `Leverage` tag on it (`04 §8`) — they hold custody without the office |
| < 1 | **split** — the post is filled by the winner, and a `Precedent` tag records an unresolved claim; the loser's faction-edge disposition is deposited sharply down, and they become a live claimant again the next time the post falls vacant |

The bands are total and nothing is unique to the near-miss window (P0-3). **The worst outcome is a
weak head with a rival holding leverage over them, which is a game state, not a game over.**

### 1.3 Collapse, restated because it is the same mechanism

`06 §6`. A faction fails by degrees: it stops acting, its posts fall vacant on their own terms, its
holdings' governance posts become claimable, its weight falls to what its remaining posts carry. No
detection routine, no elimination check, and the head post's demand always resolves at the seat node,
which cannot be lost.

---

## 2. Units, and the personnel↔battle seam

### 2.1 The unit record

Muster produces a unit (`05 §6`). Without an object to produce, muster necessarily writes an
aggregate, and an aggregate has no setter.

```
Unit
├── unit_id      : str
├── home_node    : tier node id — where it was raised, and where its entitlement was drawn
├── kind         : declared in the registry; gates what it can be ordered to do
├── size         : Gauge   attrition deposits down; reinforcement deposits up
├── discipline   : Gauge   trains up, degrades under privation
├── experience   : Gauge   accrues from engagements
├── assignment   : field | garrison        ← an assignment, never a kind
└── commander    : post_id | None
```

### 2.2 Garrison is an assignment, not a troop type

Four of four surveyed franchises treat garrison-versus-field as **the same pool wearing a different
assignment**, and none builds a separately-raised cheaper garrison tier. So `assignment` is a field on
the unit, changeable by an action, and it does three things:

- it changes which resolutions the unit participates in;
- it contributes to its node's `condition.defense` gauge while garrisoned;
- it changes the loss consequence — a garrisoned unit is lost with its node, a field unit is not.

**Open fork, named rather than decided:** whether garrisoned units may be ordered offensively without
first being reassigned. One surveyed franchise makes this a major feature. It is a design call with
real consequences for how static the map feels, and it is not this document's to make.

### 2.3 The commander, and the one place identity changes a battle

A unit's `commander` is a **post**, and the post's holder supplies attributes to the battle model.
That is the entire personnel↔battle seam: a battle whose outcome depends on *who is leading it*
rather than only on how big the force is.

**Q-2 — "no commander, no battle" is designed here as a gate**, matching C1's other two clauses: a
faction with no available commander **cannot declare a campaign**. The alternative reading — it can,
and an unled force fights at a penalty — is a modifier, and a flat penalty on an arbitrarily large
force is precisely the leverage failure §2.4 exists to prevent. ED-IN-0201 §20 flags this as the one
genuine ambiguity in the ruling and does not decide it; **this suite takes the gate and marks it as
the reading it took.**

### 2.4 The personal→mass leverage rule — a guard that belongs *before* the producer

The corpus's single most honest null: **no surveyed precedent demonstrates a mechanism whose
personal-scale contribution is provably leverage-in-band from N = 1 to N = 1000+.** Every surveyed
mechanism is either scale-blind — a flat effect that dominates at small N — or fully fused. Well-funded
teams tried and did not solve it.

Both failure poles are easy to write and hard to notice, so the rule goes in before anything can
produce one:

> **A personal-scale effect on a mass-scale outcome is expressed as a fraction of the affected unit's
> own size or cohesion. Never as a flat amount, and never as a flat obstacle shift.**

A commander's quality scales the unit's `discipline` gauge, which is per-unit and therefore
per-capita; a wounded commander deposits a proportional amount into it. Neither is a constant added to
an outcome whose spread grows as `√N`.

**Falsifier, in two parts, because the second cannot be written yet and saying so is the point.**

1. **The form check, available now.** Assert that no declared personal→mass input is expressed as an
   absolute — every one is a coefficient on a unit-scoped gauge. This is a check over the registry
   rows, it is arithmetic, and it needs no force model to exist.
2. **The sweep, available when the seam has an implementation.** Run the same personal-scale input
   across three orders of magnitude of unit size and assert the outcome probability moves by an
   in-band amount at every size.

Part 1 is what ships with this suite; part 2 lands with whatever implements `resolve_force`
(`05 §5.1`), and it is named here so it is scheduled rather than discovered. Both are load-bearing on
the game: they are the difference between a commander mattering and a commander deciding.

**The guard lands before the producer.** These two failure directions become the seam's semantics *by
default* the moment something queues a personal scene from a battle — inherited rather than chosen —
so the ordering is the whole value of stating it here.

### 2.5 Two-tier defeat severity

A unit that loses while its side holds takes a `discipline` deposit with `experience` intact. A unit
whose side breaks takes the harsher outcome. The distinction costs one branch and it softens the
hardest rule in the layer in a principled direction rather than by lowering a number: **losing a
battle and losing an army are different events, and only the second should be unrecoverable.**

---

## 3. The deliberative body

### 3.1 A body has no state of its own

It is a **set of posts** and a procedure. Membership is holding a post whose kind declares
`deliberative: true`; vote weight is a derivation over the post's kind and its holder's faction's
`acceptance`. There is no chamber object, no roster to maintain, no seat table — because posts already
carry all of it.

### 3.2 A motion has a subject, and the subject is a tag

```
Motion
├── subject   : tag_id        REQUIRED — a Grudge, a Debt, or a Precedent
├── proposer  : post_id
├── magnitude : float         chosen by the proposer, priced in standing (§3.4)
└── remedy    : the deposits that land if it carries
```

**`subject` is required and it is a tag.** A body that resolves a motion with no subject produces a
result the player cannot name and cannot lobby on, and the same contentless motion recurs every season
because nothing about the world selects it. Requiring a tag means motions come from what has actually
happened, they are different every season because the ledger is, and a fast resolution and a played-out
one are resolving *the same specific motion* rather than two different things wearing one name.

That last property is the one worth the requirement: the surveyed franchise with two resolution paths
for one event is also the only one whose two paths diverged for twenty years and were exploited in
both directions. **One engine, several entry points, resolving the same specific motion.**

### 3.3 Recorded defeat

A motion that is raised and fails **persists as a `Precedent` tag with no force and full
citability**. It changes nothing on its own; it is a fact later motions and later audits can cite.

Very few games have this and it is nearly free — one tag write on a branch that currently discards its
result. It also converts a discarded outcome into an object, which means a defeated motion is
available as a *subject* for a future one (§3.2), and the body starts having a history.

### 3.4 One sanction, with a dial

Not five tiers. **One parameterised action whose magnitude the proposer chooses at a price in their
own `standing`.**

```
price(magnitude) = k · magnitude          # a standing deposit, paid on proposal, win or lose
vote_bar(magnitude) = monotone increasing  # a bigger ask needs a wider margin
```

Five discrete tiers require machinery a body's resolver otherwise does not need — a second vote bar, a
recurring per-season effect, and a rescission path — and they give the layer a severity dial with five
detents. A continuous magnitude priced in a bounded gauge gives it a real dial and needs only a
magnitude argument.

**Bounded:** the magnitude a proposer can afford is capped by their `standing` gauge, which has a
declared ceiling. A dial that can be turned arbitrarily far is not what this is.

---

## 4. The wrapper layer

`01 §7` states the four rules. This is what they cost and what they buy.

### 4.1 One wrapper per subsystem, resolved by role

```yaml
composition_roles:
  wrapper.character_generation: {target: "<module>:run", needed_by: "engine — the ACTION phase"}
  wrapper.personnel:            {target: "<module>:run", needed_by: "engine — the ACTION phase"}
  wrapper.faction_actions:      {target: "<module>:run", needed_by: "engine — the ACTION phase"}
  wrapper.settlement_mgmt:      {target: "<module>:run", needed_by: "engine — the ACTION phase"}
  wrapper.places:               {target: "<module>:run", needed_by: "engine — ACCOUNTING_BOUNDARY"}
  wrapper.faction_mgmt:         {target: "<module>:run", needed_by: "engine — ACCOUNTING_BOUNDARY"}
```

The engine states the role; the registry states the module; the resolver imports by string at first
call, behind an exporter that resolves every declared target at export time under a blocking gate. So
a typo reds CI rather than a campaign run, and **the engine never names a subsystem.**

### 4.2 What each wrapper does, in order

```
in    drain the Keys addressed to this subsystem
      distribute DOWN — one Key, N targets, each carrying the deltas THAT receiver gets,
      at the granularity of the receiver, never one delta the receiver must interpret
run   invoke modules in declared order; a module touches primitives and nothing else
out   aggregate UP — at most one Key per resolved module, causes[] cited honestly,
      stat_deltas EMPTY on any target that is a derived aggregate
```

**Why fan-out width must not look like a cascade:** a peninsula-scale event reaching forty places is
one Key with forty targets. The re-entrancy meter counts *responses* — a consumer emitting a new Key
because it observed this one — not target-array width. Emitting forty Keys instead would make
legitimate wide delivery indistinguishable from runaway to the very guard that exists to catch
runaway.

### 4.3 Phase placement

| phase | wrappers |
|---|---|
| SEASON_TICK | none — the tick advances the clock and nothing else |
| ACTION | character generation, personnel, faction actions, settlement management |
| ACCOUNTING_BOUNDARY | places (gauge decay, tag sweep), faction management (derivations) |

Decay and derivation run **after** everything that deposits, once, at the boundary. Running decay
inside the action phase would make a gauge's value depend on the order in which actors happened to
act that season — which is a determinism defect that a stable iteration order hides rather than fixes.

### 4.4 The one convention that keeps the open hazard out of this suite

`propagation_spec_v1` §3 D.6 flags, as high-priority and explicitly not locally resolvable, that a
down-distributed place delta may overlap the state the up-aggregate reads — counting one outcome
twice. **Every wrapper here declares, per emission, which of its two channels carries the magnitude,
and never both.**

That keeps the suite internally disjoint. It is a convention, not a resolution, and a later emission
that routes a magnitude through both channels reintroduces the hazard regardless.

---

## 5. Module contracts

```yaml
- module: ad.succession
  parent: adjacent
  scales: [peninsula]
  tier: null
  resolver: d_sigma
  remit: []                               # triggered by a vacancy, not invoked
  budget: null
  consumes: [{type: post.vacant, from: [pm.vacancy]}]
  emits: [{type: post.granted, terminal: false}]
  state:
    - {name: post,     bucket: post,  writable: true, owner: substrate.post}
    - {name: standing, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag,      bucket: tag,   writable: true, owner: substrate.ledger}
  disclosure:
    - {of: claimants, inputs: published, presentation: exact, trigger: hidden}

- module: ad.unit
  parent: adjacent
  scales: [territory]
  tier: territory
  resolver: derivation
  remit: [commander]
  budget: null
  consumes: []
  emits: []
  state:
    - {name: unit.size,       bucket: gauge, writable: true, owner: ad.unit}
    - {name: unit.discipline, bucket: gauge, writable: true, owner: ad.unit}
    - {name: unit.experience, bucket: gauge, writable: true, owner: ad.unit}
    - {name: unit.assignment, bucket: tag,   writable: true, owner: ad.unit}
  disclosure:
    - {of: unit.size,       inputs: published, presentation: exact, trigger: hidden}
    - {of: unit.discipline, inputs: published, presentation: band,  trigger: hidden}
    - {of: unit.experience, inputs: published, presentation: band,  trigger: hidden}

- module: ad.motion
  parent: adjacent
  scales: [peninsula]
  tier: country
  resolver: d_sigma
  remit: [head, minister]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: []
  state:
    - {name: standing, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag,      bucket: tag,   writable: true, owner: substrate.ledger}
  disclosure:
    - {of: motion.subject,   inputs: published, presentation: exact, trigger: hidden}
    - {of: motion.magnitude, inputs: published, presentation: exact, trigger: hidden}
    - {of: vote_weight,      inputs: published, presentation: exact, trigger: hidden}
```

`ad.unit` discloses size exactly and discipline as a band: how many you have is a decision input, how
good they are is a condition.

---

## 6. Property audit

| property | verdict | reasoning |
|---|---|---|
| **P-i** legible odds | pass | Succession publishes both claimants' pools and their backers' contributions; the motion publishes its subject, its magnitude and every side's vote weight. What is hidden is the audit's tipping point, not the arithmetic |
| **P-ii** uniform leverage | pass, and §2.4 is the load-bearing case | Backer support in succession enters as a σ-space contribution, not extra dice. The personal→mass rule forbids a flat effect on a mass outcome by construction and ships with a leverage-in-band sweep across three orders of magnitude of N |
| **P-iii** bounded, monotonic | pass | Succession's three bands are total with nothing unique to the near-miss window. The sanction dial is bounded by the proposer's `standing` ceiling. Unit gauges are floor/ceiling-bounded with geometric decay |
| **P-iv** graded, recoverable | pass, and it is the strongest requirement here | Succession's worst outcome is a weak head with a rival holding leverage — a game state, not an elimination. A faction cannot be removed from play by any roll in this suite; only the gate can stop it acting, and the gate is recoverable at a node that cannot be lost. Two-tier defeat severity makes losing a battle and losing an army different events |
| **P-v** right engine | pass | Succession is genuinely two-sided and uses the rare **DO** shape, reading the margin between two nets rather than either against an obstacle — the right tool for a contest with no external difficulty. The motion is a contested vote. Unit state is accrual and decay. Assignment is a gate |

**N** — succession is what ED-IN-0201's gate makes load-bearing; the unit record is what stops muster
writing an aggregate; the motion's subject requirement is what stops the body resolving nothing.
None of the three is optional given the other documents. **R** — the extremes are a faction with no
holdings (still has a seat node, still produces a claimant), a unit of size 1 and a unit of size 1000
(the leverage rule is scale-free by construction), and a proposer at maximum standing (the dial is
ceiling-bounded). **S** — the same pool shape, obstacle owner and four primitives as `04`, `05` and
`08`; the wrapper shape is uniform across all six subsystems. **E** — three modules and a wrapper
convention; the body has no state object, the succession has no elimination branch, and garrison is
a field rather than a troop type.
