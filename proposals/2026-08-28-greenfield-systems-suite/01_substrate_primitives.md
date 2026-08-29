# 01 — Substrate: four stored primitives, two engine extensions, one wrapper shape

> ⚠ **ARCHIVED / SUPERSEDED (2026-08-29).** This is the **pre-critique** version. It is retained
> unedited so the adversarial findings against it stay checkable — **do not build from it.** Six of
> its claims are known false; see [`ARCHIVED.md`](ARCHIVED.md). The live suite is
> `proposals/2026-08-29-greenfield-systems-suite-v2/`.


## Status: PROPOSED (2026-08-28) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md)

Everything in this suite is a composition of what is on this page. If a later document needs a fifth
kind of stored thing, that is a defect in this page, not a licence to add a field somewhere else.

---

## 1. P-1 — Entity

One identity primitive with **declared kinds**. A person, a place, a faction, a unit and a relation
are the same shape: an id, a kind, immutable identity fields declared per kind, and ownership of
gauges, tags and posts. Making Person a primitive while Place was something else would put two
containers with identical structure into two taxonomies, which is the shape-divergence failure this
suite is supposed to be immune to.

```
Entity
├── entity_id  : str
├── kind       : person | place | faction | unit | edge      ← closed at five
├── identity   : {…}    immutable after creation; the field set is declared per kind
├── gauges     : {gauge_id: Gauge}
├── tags       : [Tag]
└── posts      : [post_id]      for kinds that site or hold posts
```

**Entities are loaded or generated and never written.** All mutable state on an entity lives in its
gauges, its tags and its posts — which is the one write rule (§2 of `00`) stated from the other side.

### 1.1 Kind: person

The only kind that appears at every scale of play. A combatant, a governor, a commander, a voter, a
disputant — one object, each scale reading the facet it needs and none redefining it.

**Built edges-first, deliberately.** The precedent survey's structural finding is that every surveyed
personnel system is *primarily a relationship model indexed by a roster*: the roster is the index, the
relationships are the mechanism. A person built as a stat block with relationships bolted on later
satisfies the index and none of the mechanism. So edges are constructor arguments, not optional
extras: **a person cannot be created without at least two edges** (see `02 §4`).

```
identity(person)
├── name                  : str
├── origin_node           : tier node id — where they are from, not where they are
├── convictions           : [(name, weight)]  names resolved through descriptors.resolve_conviction
├── capability            : {attribute_key: int}   keys and scale FROM descriptors.ATTRIBUTES
└── capability_provenance : "authored" | "derived"      ← disclosed; see §6

derived
└── posts : [post_id]     the posts whose holder is this person
```

### 1.1.1 Capability reads the registry, it does not restate it

`engine/substrate/descriptors.py` owns the attribute roster, its scale, and the fact that the roster
is **incomplete by ruling** — nine defined, a tenth ruled and unnamed, exposed as
`ATTRIBUTES_PENDING_TENTH`. A person's attribute map is keyed on `descriptors.ATTRIBUTES` and nothing
in this suite names an attribute literally. When the tenth is named, every person gains it by
regeneration and no design below changes.

The same discipline binds convictions: names go through `descriptors.resolve_conviction`, which
raises on an unknown name rather than silently scoring zero.

### 1.2 Kind: edge — the relationship, and where continuous state actually lives

An edge is an entity, not a field on one. It has an id, it owns a gauge and a tag list, and it is
addressable as a tag owner and a Key target — exactly like a place. Modelling it as a field on the
person would have made person→person relations first-class and faction→faction relations a bag of
tags, which is two mechanisms for one job.

```
identity(edge)
├── endpoints : (entity_id, entity_id)      ordered; direction is meaningful
└── relation  : patron | client | kin | peer | rival | sworn      ← closed at six

gauges
└── disposition : −5 … +5, geometric decay toward rest 0

tags
└── what has passed between them, each with provenance
```

**Disposition is a Gauge on an edge, not a field on a person.** That single choice is what makes the
relationship model a mechanism rather than a roster annotation: it decays, it is deposited into with
provenance, it is bounded, and it is derived-not-written like everything else.

`relation` is a closed set of six, so a design cannot invent a relation kind to hold a mechanic — the
mechanic goes in tags and the gauge.

**A faction's enmity toward another faction is an edge**, not a special faction field: the same
disposition gauge, the same tags, the same decay, read by the same functions that read personal
edges (`06 §4`). One relation primitive, every pair of entities that can have a relation.

### 1.3 `posts` is derived, and that is the whole answer to the vocabulary collision

*Officer* means a mass-battle unit commander and nothing else. *Governor* means the holder of a
settlement's governance post. *Companion* is a relationship, not an office. All three legitimately
compose on one person, and they compose because **`posts` is a derived set, not a `role` string**.
There is no field to collide in. Nothing in this suite coins a new word for a rank-holder: a person
*holds a post*, which is what ordinary English already says.

⚠ **`seat` is not available as a synonym for post.** It is already a settlement type. Use *post*.

---

## 2. P-2 — Tag

Durable, discrete memory on **any** entity. This is the primitive six otherwise-unrelated
requirements all land on: a faction's grudge, a place's precedent, a person's obligation, a body's
record of a defeated motion, a fiscal claim that outlives its season, and the demoted officeholder's
residual.

```
Tag
├── owner_ref     : (entity_kind, entity_id)   person | faction | place | post | edge
├── kind          : Precedent | Grudge | Debt | Reputation | Leverage      ← closed at five
├── key           : str          what specifically; the dedupe axis
├── value         : float
├── created_season: int
├── ttl           : int | None   None = durable; durable tags survive succession
└── provenance    : key_id       REQUIRED, NON-EMPTY — the Key that caused this tag
```

**Five kinds, closed.** A recurring, term-limited claim is a `Debt` with `recurs=True` and a `ttl`,
not a sixth family. The enum is closed so that a mechanic cannot be smuggled in as a tag family;
mechanics go in modules.

### 2.1 Provenance is required, and it is the guard

A tag with an empty `provenance` cannot be appended. The rule exists because the failure it prevents
is documented and severe: a convenience path that produces a relational outcome the history does not
justify corrodes the system *for players who never use it*. Binding every durable tag to the Key that
caused it means the history is queryable, and it means `Key.causes[]` finally does the job it was
built for — it becomes a biography rather than a write-only chain.

**Falsifier:** a test asserting no reachable tag in a seeded campaign has empty provenance. This
guard is load-bearing on the game — the mechanic is *why did this actor turn on me* — not on the
repository.

### 2.2 Dedupe, and why it bounds an otherwise unbounded counter

`tag_append` dedupes on `(owner_ref, kind, key)` and **refreshes in place**. `Reputation` is
single-valued per owner: the latest replaces the prior.

That is not housekeeping. A post that is contested repeatedly generates one grudge per passed-over
candidate *per post*, refreshed — not one per attempt, stacked. Without dedupe, a popular post is an
unbounded ramp on the number of tags, and the value carried on those tags feeds selection. With it,
the count is bounded by (candidates × posts) and the magnitude is bounded by the gauge the tag's
value is deposited into.

### 2.3 The sweep

At the accounting boundary, every ledger drops its expired tags. Durable tags (`ttl=None`) survive
sweeps **and survive succession** — a place remembers what was done to it after the officeholder is
gone, which is the residual the genre's best-documented demotion failure lacks.

### 2.4 A tag may bias a decision; it may never substitute for one

**Binding on every selection function in this suite.** Wherever a decision function sums a
relational or leverage term alongside structural terms — a candidate's fitness, an action's appeal,
a target's hostility — the relational term's contribution is **capped as a fraction of the function's
structural range**:

```
|relational terms|  ≤  RELATION_SHARE_MAX · (max structural term − min structural term)
```

The failure this prevents is documented and specific: relationship modifiers large enough to dissolve
structural conflict produce a game in which *you can generally succeed at things rulers historically
wanted to do and could not*, because opinion bonuses paper over the positional facts. **Some conflicts
must be positional and unbuyable.**

It binds hardest on custody (§3.2): a `Leverage` tag on a post biases its holder toward the
controller's preferences; it never replaces them. A custodian who fully determined a holder's choices
would make custody strictly better than holding the post, at a fraction of the exposure — which is the
mechanic eating itself.

`RELATION_SHARE_MAX` is declared in the exported params. Its reachability bar: **at the maximum
reachable relational total, the structurally-worst option must still be unable to outrank the
structurally-best one.**

---

## 3. P-3 — Post

The delegation object. Acting *on behalf of* something at a scale requires a post that can be granted
and revoked; acting *within* is a claim on someone else's. Both stances need this object and neither
needs a second one.

```
Post
├── post_id       : str
├── kind          : head | governor | minister | commander | envoy | clerk   ← closed at six
├── tier_node     : place/tier node id where this post has authority
├── principal     : faction_id | post_id      who granted it, and who may revoke it
├── holder_id     : person_id | None          None = VACANT, and a vacancy is first-class
├── remit         : [module_id]               the option set this post unlocks
├── granted_season: int | None
├── term          : int | None                None = at pleasure
└── budget        : Gauge                     (P-4) — action count per season; see §4.3
```

### 3.1 A vacancy is a state, not an absence

`holder_id = None` is the object that closes ED-IN-0201's gate. It is queryable, it is a demand
signal for generation, and it is the reason a faction that cannot find a head **stops acting** rather
than acting badly. That is a better failure state than any collapse procedure, and it needs no
detection mechanism: the gate reads the field.

### 3.2 Custody is a tag, not a field

Controlling a post-holder without deposing them is a five-source convergence in the precedent survey
and the sharpest architectural gap the roster research named. It is **not** a second identity field.

`Leverage(owner_ref=(post, post_id), key=<controller person_id>, provenance=<the Key that established it>)`

carries exactly the same information as a `custodian_id` field, and carries it with a ttl, a
provenance chain and a decay the field would not have. Establishing custody is a contested action
(`09 §3`); losing it is the tag expiring or being stripped. **No new field.**

### 3.3 `remit` is how a person changes the option set

ED-IN-0201 clause 2 says the person shapes *which* action is chosen from the same option set with the
same information — and its own NERS constraint says that must not be a flat trait bonus on a
selection roll, because a flat shift is worth systematically more to a small pool than a large one.

`remit` is the shape that satisfies both. A module is invocable only by a post whose remit names it.
Two holders of the same post get the same remit; two different post kinds get different remits; and a
holder's *convictions* rank the remit's contents (`05 §3`). Nothing adds a die and nothing shifts an
obstacle. **The choice differs; the odds do not.**

### 3.4 The player holds a post — and that is the entire player model

There is no player entity, no player faction flag and no player-only module anywhere in this suite.
**The player is a person, and they act by holding posts.**

| | |
|---|---|
| **What the player may do this season** | exactly the modules in the remit of the posts they hold, exactly as for any other holder |
| **What the player spends** | the `budget` gauge on those posts, exactly as for any other holder |
| **What happens to a post the player does not attend to** | the same module runs, with the holder's own `appeal` / `preference` (`04 §4.2`, `05 §3.2`) supplying the choice |
| **How the player gains reach** | by being appointed to, or claiming, more posts — which routes through `04` like everyone else's |
| **How the player loses it** | audit, recall, succession, or the gate closing — the same four paths |

Three properties follow, and the third is the one worth the design:

1. **No special-casing.** A player-only branch anywhere would be scripting drift by definition, and
   the surest way to grow one is to give the player a different object to act through.
2. **Delegation is free.** A player who holds three posts and attends to one has not lost the other
   two; they resolve on their holders' declared preferences. That is the auto-resolution tier, and it
   is **the same module run headless**, not a second cheaper path.
3. **One engine, several entry points.** The surveyed franchise whose fast path is a *different
   algorithm* from its played path spent two decades with a divergence exploited in both directions;
   the one whose three fidelities are the same engine resolving the same specific fixture did not.
   Because a played action and an unattended action here are the same module with the same pool, the
   same obstacle and the same ladder, there is no divergence to calibrate — only the *choice* differs,
   and that difference is the point rather than a defect.

---

## 4. P-4 — Gauge

Every continuous quantity in the game. A Key is a typed one-shot emission — exactly right for a flag,
structurally wrong for a value that is read continuously between emissions and decays. Acceptance,
order, pressure, disposition, standing, exposure, an accrual, a budget: none of these *emit*, they
*are*.

```
Gauge   (declared in references/descriptor_registry.yaml; instantiated per owner)
├── gauge_id   : str
├── owner_ref  : (entity_kind, entity_id)
├── scale      : one of the runtime four
├── floor, ceiling : float
├── lambda     : float in (0, 1]     the geometric decay coefficient
├── rest       : float               the value it decays toward
├── bands      : [(threshold, label)]  what the player is shown (E-2)
└── history    : [(season, delta, provenance_key_id)]
```

API, and it is deliberately three functions:

- `gauge_deposit(gauge, delta, provenance)` — appends. **Provenance required.**
- `gauge_value(gauge, season)` — the current value.
- `gauge_band(gauge, season)` — the label. This is what a player sees.

**There is no setter.** That is the whole point: `propagation_spec_v1` §2 AU-1 says no aggregate is
ever written, and a primitive with no setter is what makes that structural instead of a discipline
every future author has to remember.

### 4.1 Decay is geometric, never a saturating additive step

```
value(t+1) = rest + (value(t) − rest)·(1 − λ)  +  Σ deposits(t)
```

**This is the single most load-bearing arithmetic choice in the suite**, and it is chosen against a
measured failure. A restoring term that saturates — one that pulls back by *at most* a fixed step per
season — is bounded above by that step, so any accrual larger than it pins the value at its ceiling
and holds it there. That is not a tuning problem; it is a property of the shape, and it produces an
unrecoverable state from ordinary play.

A geometric restoring term has no such ceiling on its own strength. For a bounded per-season accrual
`a`, the fixed point is `rest + a/λ` — **finite for every λ > 0 and every bounded `a`**. There is no
value of `a` that pins the gauge, and the settling time is `≈1/λ` seasons regardless of magnitude.

Consequences that follow for free:

- **Contractivity is structural.** `propagation_spec_v1` AU-4 requires `decay()` to be a pure
  function of elapsed time for determinism, and §4.3 makes cross-tick convergence conditional on it
  being *strictly contractive*. `(1 − λ)` with `λ ∈ (0, 1]` is strictly contractive by construction.
- **Every gauge is bounded** by `[floor, ceiling]`, clamped on read.
- **Monotonic response.** More deposit is never less value.

**Falsifier:** an arithmetic test, requiring no campaign run, asserting for every declared gauge that
`rest + max_seasonal_accrual/λ ≤ ceiling`. A gauge whose declared accrual sources can exceed that
fails at declaration time. This guard is load-bearing on the game — it is the difference between a
settlement that can recover and one that cannot.

### 4.2 Where gauges are used, and what each one retires

| Gauge instance | Owner | Retires (as a separate mechanism) |
|---|---|---|
| `disposition` | person→person / person→faction edge | a bespoke loyalty scalar per subsystem |
| `standing` | person | the public half of nine parallel personal meters |
| `exposure` | person | the private half — everything a player accrues by acting covertly |
| `acceptance.legitimacy`, `acceptance.support` | place | per-settlement political acceptance |
| `condition.order`, `condition.prosperity`, `condition.defense` | place | the settlement stat block |
| `pressure` | place | the event-draw driver |
| `accrual.entitlement` | place | the levy channel's supply |
| `budget` | post | every proposed action economy in the corpus |

**Two personal meters, not nine.** One public (`standing`), one private (`exposure`). Nine bounded
meters differing only in their trigger lists is nine bars a player watches; the triggers are the
design, the meters were duplication. Anything the retired meters gated is gated on a band of one of
these two, or on a tag.

### 4.3 Budget is a gauge, and it buys actions — never modifiers

A budget is an accrual with a spender. Making it the same primitive is what closes the *three rival
accrual clocks* problem structurally: one rate, one cap, one bifurcation analysis, several typed
consumers.

**The restriction, and it is not optional.** One budget point buys **one attempt at one module**. It
never converts into dice and never into an obstacle shift.

The arithmetic that forces this: in the deterministic-plus-stochastic resolver a point returns a flat
`SLOPE` per point, engine-wide. In the continuous engine an added die at a balanced check is worth
`≈0.204σ` at pool 5 against `≈0.115σ` at pool 18 — and the value is obstacle-dependent too, ranging
roughly `0.107σ`–`0.302σ` at pool 5 alone. So a single currency spendable as a modifier in both is
worth **something like twice as much** on a small pool as a large one, and more once the obstacle
varies. A player who notices routes their budget wherever it pays. Buying *actions* keeps the budget
out of the resolution arithmetic entirely, which is also the simpler design.

**Falsifier:** a test asserting no module contract declares a `budget:` whose cost is consumed inside
a pool or obstacle expression. Load-bearing on the game: it is the difference between a budget and an
exploit.

---

## 5. E-1 — `derive_ob`, the obstacle's owner

```python
def derive_ob(target_score: float, modifiers: float = 0.0) -> float:
    """The obstacle. Jordan, 2026-08-14: an obstacle rolled against a character or faction is
    their corresponding score/2 plus whatever specific modifiers exist for them in that instance."""
    return max(OB_MIN, target_score / 2.0 + modifiers)
```

It belongs beside `roll_pool` in `engine/autoload/dice_engine.py`, for the reason the corpus already
measured: the margin ladder is single-owned and guarded, and the obstacle is derived locally in most
resolving subsystems and arrives at the roller as a bare parameter. **Ruling the obstacle without
giving it an owner predicts the same fork recurring**, and there is a measured precedent for exactly
that in six private roll/degree implementations.

Three properties, each of which is a defect avoided rather than a feature added:

1. **The result is fractional and stays fractional.** The ladder's own contract says both operands
   may be fractional; every existing obstacle-derivation site rounds or floors, against a ladder built
   to consume fractions. Producers that were correct when written stopped being correct when the
   ladder moved underneath them. A single owner cannot drift that way.
2. **Modifiers are σ-space, not obstacle-space.** A modifier reaches the roll through
   `sigma_leverage.net_boost` — a μ-shift scaled by `σ_N = 0.8·√Pool` — never as a flat addition to
   `derive_ob`'s output. A flat obstacle shift is worth more to a small pool than a large one, which
   is the same non-uniformity the budget restriction rules out, one level down. The `modifiers`
   argument above is reserved for terms that are genuinely properties *of the target* (a fortification,
   a legal protection), not for the actor's advantages.
3. **The floor is `OB_MIN`**, so an advantage cannot drive the obstacle below the ruled minimum and
   create a cliff at the floor.

**One leverage note, stated because it is the obvious objection.** Raising an attribute adds a die,
and a die is worth roughly `0.204σ` at pool 5 against `0.115σ` at pool 18 — so capability investment
is worth about 1.8× as much to a weak actor as to a strong one. That is **non-uniform in the correct
direction**: it is self-damping, it makes the weak actor's improvement matter more than the strong
one's, and it is the shape a bounded system wants. It is a property of the continuous engine, not
something this suite introduces, and it is recorded here so a later reader does not mistake it for an
unnoticed P-ii defect.

**This suite derives every obstacle here and nowhere else.** It takes no position on the three
existing sites whose reconciliation is suspended; those are a different lane's question and a
greenfield module has no ratified canon to overwrite.

---

## 6. E-2 — The disclosure block

There is no GM. Nobody narrates why a candidate was passed over, why a faction declined to act, or
why a place's pressure rose. The only surveyed evidence that speaks to that constraint is a game
whose social layer was loved and whose tactical math was resented *in the same title*, separated by
nothing but whether the model was visible — and whose community fix **exposed the models rather than
changing them**.

**The contract, owned once and inherited by every state row in the suite:**

> **Publish every input. Publish a band, never a number. Never publish the trigger point.**

It is asymmetric on purpose. Five independent sources keep the threshold hidden; four say legibility
is what separates a celebrated system from a resented one. Publishing the trigger destroys the
mechanic; publishing the inputs is what makes the outcome feel principled rather than arbitrary.

```yaml
disclosure:
  - of: pressure
    inputs: published          # every deposit and its provenance is inspectable
    presentation: band         # the player sees "strained", not 6.4
    trigger: hidden            # the player is never told the draw threshold
```

**It is a registry field, not documentation.** A state row without a `disclosure:` block fails the
contract check. That is what makes this a design object rather than an intention — and it is the cell
the existing slice taxonomy (primitive · derivative · formula · mechanic · process) has no home for,
which is why disclosure keeps being filed as prose and keeps not happening.

**Falsifier:** a test asserting every state row in the suite's module contracts carries a disclosure
block, and that no block sets `trigger: published`.

---

## 7. The wrapper — one per subsystem, owning all Key I/O

ED-IN-0200's runtime half: each subsystem has a wrapper handling all Key I/O; inputs trickle down
with increasing granularity, outputs aggregate up.

```
                 engine_clock.run_tick
                          │
        SEASON_TICK ── ACTION ── ACCOUNTING_BOUNDARY
                          │
                    subsystem wrapper          ← resolved by composition role, never imported
                     ├── in:   drain the Keys addressed to this subsystem's modules
                     │         distribute DOWN: one Key, N targets, each with its own
                     │         stat_deltas and impact_vector at the granularity of the receiver
                     ├── run:  invoke modules; modules touch primitives and NOTHING else
                     └── out:  aggregate UP: emit at most one Key per resolved module,
                               with causes[] cited honestly and stat_deltas empty on any
                               aggregate-typed target
```

**Four rules the wrapper enforces so no module has to.**

| # | Rule | The failure it prevents |
|---|---|---|
| W-1 | A module never emits. It returns a result; the wrapper emits. | Emission scattered across a subsystem is how `causes[]` chains get fabricated or dropped |
| W-2 | A module never imports another subsystem. Cross-subsystem needs resolve through `composition.require(role)`. | The package cycle that a function-local import hides from the interpreter without removing |
| W-3 | Fan-out is one Key with N targets, never N Keys. | The re-entrancy meter counts *responses*, not target-array width, so wide legitimate delivery must not look like runaway |
| W-4 | Any Key naming a derived aggregate in `targets[]` carries `stat_deltas: {}` for that target. The magnitude rides in the payload and is read at derivation. | Writing an aggregate, which the one write rule forbids and the generic per-observer write path would otherwise do silently |

**Down-distribution is where granularity increases.** A peninsula-scale Key addressed to eight places
carries eight `targets[]` entries, each with the deltas *that place* receives — not one delta the
receiver has to interpret. A wrapper that emits a Key with a sparse `targets[]` array delivers blind,
which is the documented failure mode of the eight declared down-seams that populate nothing.

⚠ **The double-count hazard is open and this suite does not resolve it.** If a down-targeted place
delta overlaps the state the up-aggregate reads, the same outcome is counted twice — once as the
write that feeds the aggregate, once as the modifier term. `propagation_spec_v1` §3 D.6 flags this as
needing a ruling and forbids resolving it locally. **Every wrapper in this suite therefore declares,
per emission, which of its two channels carries the magnitude — and never both.** That is a
convention that keeps the suite internally disjoint; it is not a resolution of the general question.

---

## 8. What is deliberately not a primitive

A cut list is only credible next to what it refuses to add.

| Considered | Verdict | Why |
|---|---|---|
| A separate **Accrual** primitive | **folded into Gauge** | An accrual is a gauge with a positive rest and a rate; a budget is an accrual with a spender. Three rival accrual clocks in the corpus become one primitive with three consumers |
| A separate **Standing/rank** primitive | **folded into Gauge** | A rank ladder is a bounded personal meter with bands. Keeping it separate is what produced nine parallel meters |
| `custodian_id` as a **field on Post** | **folded into Tag** | §3.2. A field would carry less (no ttl, no provenance, no decay) at the same conceptual cost |
| A **role** string on Person | **rejected** | §1.3. `posts` is derived; there is no field to collide in |
| A **Compact** tag family | **rejected** | A recurring term-limited claim is `Debt(recurs=True, ttl=term)`. Adding a sixth family to hold one mechanic is how a closed enum stops being one |
| A **second resolver** of any kind | **rejected** | The only surveyed franchise with two resolution paths is also the only one with a two-decade unfixed divergence between them, exploited in both directions. One engine, several entry points |
| A **view** primitive | **rejected as a primitive** | Disclosure stores nothing and resolves nothing. It is a declaration attached to state (E-2), which is what makes it checkable rather than aspirational |

---

## 9. Module contracts — the substrate's own

```yaml
- module: substrate.entity
  parent: substrate
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: derivation
  remit: []                      # not invocable; a store
  budget: null
  consumes: []
  emits: [{type: person.generated, terminal: false}]
  state:
    - {name: entity, bucket: entity, writable: false, owner: substrate.entity}
    - {name: edge.disposition, bucket: gauge, writable: true, owner: substrate.entity}
  disclosure:
    - {of: entity, inputs: published, presentation: exact, trigger: hidden}
    - {of: edge.disposition, inputs: published, presentation: band, trigger: hidden}

- module: substrate.ledger
  parent: substrate
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: derivation
  remit: []
  budget: null
  consumes: []
  emits: []
  state:
    - {name: tag, bucket: tag, writable: true, owner: substrate.ledger}
  disclosure:
    - {of: tag, inputs: published, presentation: exact, trigger: hidden}

- module: substrate.post
  parent: substrate
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: gate
  remit: []
  budget: null
  consumes: []
  emits:
    - {type: post.granted, terminal: false}
    - {type: post.revoked, terminal: false}
    - {type: post.vacant,  terminal: false}
  state:
    - {name: post, bucket: post, writable: true, owner: substrate.post}
    - {name: post.budget, bucket: gauge, writable: true, owner: substrate.post}
  disclosure:
    - {of: post, inputs: published, presentation: exact, trigger: hidden}
    - {of: post.budget, inputs: published, presentation: exact, trigger: hidden}

- module: substrate.gauge
  parent: substrate
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: accrual
  remit: []
  budget: null
  consumes: []
  emits: []
  state:
    - {name: gauge, bucket: gauge, writable: true, owner: substrate.gauge}
  disclosure:
    - {of: gauge, inputs: published, presentation: band, trigger: hidden}
```

Note `substrate.post` and `substrate.gauge` disclose **exact**, not band: a post's holder and a
budget's remaining points are things the player is acting on directly this season, and hiding them
would obscure an input rather than a threshold. Bands are for values whose precise magnitude is not a
decision the player makes.
