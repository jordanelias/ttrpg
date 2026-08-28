# 02 — Character generation

## Status: PROPOSED (2026-08-28) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md)
## Produces: entities of kind `person`, and the `edge` entities that attach them (P-1)

---

## 1. The shape of the problem

Character generation in a no-GM engine has to satisfy four things at once, and three of them are in
tension:

1. **It must be total.** Under ED-IN-0201 a vacant head post stops a faction acting. If generation can
   fail to satisfy a demand, an unlucky world-gen permanently bricks a faction and the campaign has no
   recovery path. **Generation therefore has no failure branch** — see §5.
2. **It must be conditioned.** A person generated from a ruined frontier place and a person generated
   from a cathedral city must be recognisably different, or the population is wallpaper.
3. **It must not be uniform.** Conditioning taken to its conclusion makes every person from the same
   place identical, which reads as scripted — the opposite failure and the more common one.
4. **It must be deterministic and attributable.** Same seed, same demand, same person; and the
   draws must not re-phase anything else in the campaign.

The layered approach — **condition first, reify second** — is the shape four independent generation
programmes arrived at separately, and it is the one that satisfies (2) and (3) simultaneously: the
conditioning layer decides the *distribution*, a bounded deviation step decides how far this
individual sits from it.

---

## 2. Four stages

Four, not six. `deviate` is part of drawing, not a stage after it; `commit` is part of attaching, not
a stage after that. A stage that does not change the shape of the object is apparatus.

```
  cg.demand  ──►  cg.condition  ──►  cg.draw  ──►  cg.attach
  a vacancy       a distribution     a person      edges, and the Key
  or a scene      over the person    with a        that says where they
  needs someone   space              deviation     came from
```

### 2.1 `cg.demand` — generation is demand-driven, and there is no spawner

A demand is a typed request:

```
Demand
├── tier_node   : where the person is needed
├── faction     : whose person they are, or None for a local actor
├── post_kind   : the post they are wanted for, or None for a scene participant
└── cause       : key_id — the Key whose resolution created this need
```

Demands come from exactly three places: a **post vacancy** (`04`), a **scene** that requires a
participant with no available person, and **world-gen**, which issues one demand per required post
(`03 §2`).

**There is no ambient spawn, no population target, and no turnover rate.** The refusal is against a
documented failure: the closest-analogue franchise ships roughly six or seven parentless adults per
month, reaches five-figure character counts in a long campaign, and has two community mods pulling in
*opposite* directions to fix it — one to cull, one to populate. Its own developers' fix was throttling
the tap at the low-value tail. **Generate on demand, not on a clock.**

### 2.2 `cg.condition` — build the distribution, draw nothing

Conditioning reads three sources and consumes **no randomness**:

| source | contributes |
|---|---|
| the tier node's gauges (`condition.*`, `acceptance.*`, `pressure`) | how prosperous, ordered and strained the place is |
| the faction's tag ledger and its held posts | what this faction rewards |
| the demand's `post_kind` remit | which capabilities the role actually reads |

Output is a **distribution object**, not a person: a per-conviction weight vector, a per-attribute
mean and spread, and an origin distribution. Being a separate stage matters — it is inspectable, it
is testable without drawing, and it is what the disclosure contract publishes when the player asks why
this person is like this.

#### 2.2.1 Conditioning enters as a bounded additive log-odds shift

The obvious implementation — multiply the prior by a factor per condition — has a leverage defect:
a multiplicative factor is worth far more to a category that is already likely than to one at the
tail, so a unit of conditioning does not move the distribution by a consistent amount and the tails
get swamped. That is the same non-uniformity the suite rules out one level up in the resolution
kernel, appearing here in a categorical draw.

```
logit_i  =  logit(prior_i)  +  clamp( Σ_c  w_c · signal_c(i),  −Δ_MAX, +Δ_MAX )
p_i      =  softmax(logit)_i
```

A unit of signal moves the log-odds by the same amount wherever it lands, and `Δ_MAX` bounds how far
any one category can be driven. Both properties are checkable without a campaign run.

#### 2.2.2 An entropy floor, because full conditioning is the other failure

```
p'_i = (1 − ε)·p_i + ε/n            ⇒   p'_i ≥ ε/n = p_floor  for every i
```

One line after the softmax, and it makes the floor a property of the arithmetic rather than a
post-hoc clamp that could be forgotten at one call site. Without it, a place at its gauge extremes
produces a degenerate distribution and every person from a ruined province is the same person — which
reads to a player as authored, and is the exact thing conditioning was supposed to avoid.

`p_floor` and `Δ_MAX` are the two tuning parameters of this stage. They are declared in the exported
params, not buried, and each has a stated reachability bar: at the map's most extreme node, the
conditioned distribution must still admit every conviction at ≥ `p_floor`.

### 2.3 `cg.draw` — one deterministic sequence, with a bounded deviation

The draw sequence is fixed and its order is part of the determinism contract:

| # | draws | from | bounded by |
|---|---|---|---|
| 1 | primary convictions (1–3) and their weights | the conditioned conviction distribution | weights sum into the registry's declared concentration band |
| 2 | attributes | per-attribute mean and spread | `descriptors.ATTRIBUTE_FLOOR` … `ATTRIBUTE_CEILING`, clamped |
| 3 | origin node | the origin distribution | must be a live tier node |
| 4 | **one deviation** | uniform over the axes drawn above | **exactly one axis, moved by at most one band** |

**The deviation is what makes a population, and its bound is what keeps it a population.** One axis,
one band, then clamp. An unbounded deviation on top of an already-extreme conditioned draw produces
out-of-band people, and an unclamped one produces people the registry's own scale does not admit.

**Every drawn field must be load-bearing on at least one resolution branch.** This is a gate on the
generator, not a stylistic preference: a field nobody reads is a field that will be cited as
characterisation and will never change an outcome. Before a field is added to the draw, the module
that consumes it is named. The current draw has four fields and each has a named consumer:
convictions rank a post-holder's option set (`05 §3`), attributes are the pool of every roll they
make, origin conditions their edges (§2.4), and the deviation axis is the reason two people from one
place differ.

### 2.4 `cg.attach` — a person is born owing someone something

A person is created with **at least two edges**: one **upward** (a patron, a kin elder, an institution
that placed them) and one **lateral** (a peer or a rival at the same node). Both carry a `disposition`
gauge seeded from conviction alignment between the two parties, and both carry a provenance tag citing
the demand Key.

This is the inversion the precedent survey argues for and the one this suite takes seriously: the
roster is the index, the relationships are the mechanism. A person generated without edges is a stat
block, and every mechanic that reads relationships — defection, patronage, succession claims,
appointment grudges — is then reasoning about an empty graph.

The wrapper then emits one `person.generated` Key with the person as subject, the demand's `cause` in
`causes[]`, and the counterparties of both edges in `targets[]`.

---

## 3. Authored characters are the head of the same pipeline

An authored roster and a generator are not two systems. A demand is satisfied in this order:

1. **An unassigned authored character matching the demand's `faction` and `post_kind`.**
2. Otherwise, generation.

That makes the authored cast the *first* answer to every demand rather than a parallel content path
that has to be separately loaded and separately reasoned about.

### 3.1 Capability is generated until it is authored — and it says which it is

Identity is what authoring is for: a name, a faction, a role, convictions, an arc. Capability is a
1–7 vector that authoring has historically not supplied. Blocking every downstream mechanic until a
full capability set is hand-authored for the whole cast is a content dependency with no fallback.

**Rule:** an authored character missing capability receives it from `cg.condition` + `cg.draw`, seeded
on their own id, and carries `capability_provenance: "derived"`. When capability is authored later, the
field flips to `"authored"` and the drawn values are discarded.

Two properties make this safe rather than a fudge:

- **It is deterministic and reproducible.** Same character, same campaign seed, same capability, every
  run. It is not a random roll at load.
- **It is disclosed.** `capability_provenance` is published under E-2. A player, or a reviewer, can
  see which numbers are canon and which are the engine's placeholder. A derived capability that is
  silently indistinguishable from an authored one is how a placeholder becomes canon by accident.

### 3.2 The identity fields authoring must supply

Because they are the fields the pipeline cannot invent without deciding canon: `name`, `faction`,
`post_kind` eligibility, and `convictions` (names resolved through `descriptors.resolve_conviction`,
which raises rather than guessing at a legacy label whose migration the corpus deliberately left open).

---

## 4. The determinism contract

```
substream = Random( H(campaign_seed, "cg", tier_node, faction, ordinal) )
```

Three properties, and the third is the one that matters most:

1. **Reproducible.** The same demand at the same node in the same campaign yields the same person.
2. **Isolated.** The generator draws from its own substream, never the shared campaign stream.
   Population size therefore cannot re-phase any other consumer of randomness in the game.
3. **The isolation lands first and is proved byte-identical** (P0-2). It is the only step in this
   entire suite that can be proved to change nothing, and it is what makes every later step's effect
   attributable to that step.

⚠ **A guard that counts generator calls does not observe this.** Any population guard must read the
person store itself. A guard on a call counter is invisible to a loader, a restore, or any other path
that constructs people without going through the generator — which is to say it cannot see the change
it exists to catch.

---

## 5. Generation is total

**For any well-formed demand, `cg.draw` returns a person.** There is no failure branch, no "no
suitable candidate", and no empty return.

Ill-formed demands — a tier node that does not exist, a faction that does not exist, a `post_kind`
outside the closed set — are **load-time validation errors**, raised when the registries are read, not
runtime dead ends. The distinction is the whole safety property: a malformed world fails loudly at
startup; a well-formed world can never reach a state where a required post cannot be filled.

This is what lets ED-IN-0201's gate be a clean precondition rather than a trap. A faction's head post
can always be filled by *someone*; whether that someone is any good is the game.

---

## 6. Module contracts

```yaml
- module: cg.demand
  parent: character_generation
  scales: [personal]
  tier: null
  resolver: gate
  remit: []                     # not player-invocable; raised by other modules
  budget: null
  consumes:
    - {type: post.vacant, from: [pm.vacancy]}
  emits: []
  state: []
  disclosure: []

- module: cg.condition
  parent: character_generation
  scales: [personal, settlement]
  tier: null
  resolver: derivation
  remit: []
  budget: null
  consumes: []
  emits: []
  state: []                     # pure; consumes no RNG and stores nothing
  disclosure:
    - {of: distribution, inputs: published, presentation: band, trigger: hidden}

- module: cg.draw
  parent: character_generation
  scales: [personal]
  tier: null
  resolver: derivation          # a draw from a declared distribution, not a contest
  remit: []
  budget: null
  consumes: []
  emits: []
  state:
    - {name: entity, bucket: entity, writable: false, owner: substrate.entity}
  disclosure:
    - {of: person.capability_provenance, inputs: published, presentation: exact, trigger: hidden}

- module: cg.attach
  parent: character_generation
  scales: [personal]
  tier: null
  resolver: derivation
  remit: []
  budget: null
  consumes: []
  emits:
    - {type: person.generated, terminal: false}
  state:
    - {name: edge.disposition, bucket: gauge, writable: true, owner: substrate.entity}
    - {name: tag, bucket: tag, writable: true, owner: substrate.ledger}
  disclosure:
    - {of: edge.disposition, inputs: published, presentation: band, trigger: hidden}
```

---

## 7. Property audit

**Engine class.** A conditioned categorical draw is neither the continuous engine nor the
deterministic-plus-stochastic resolver. It is diagnosed against the five properties directly and
carries a `[NEW ENGINE]` flag: if it is ever to be treated as a canonical resolution instance rather
than a generator, that is a ratification act, not an inference.

| property | verdict | reasoning |
|---|---|---|
| **P-i** legible odds | pass, scoped | The player does not choose against this draw, so predicting its odds is not a decision they make. What P-i requires here is that the *result* be legible: `capability_provenance` and the conditioning inputs are published under E-2 |
| **P-ii** uniform leverage | pass | §2.2.1 — additive log-odds with a bounded shift; a unit of conditioning moves the distribution by the same amount wherever it lands. A multiplicative form fails this and is the version not built |
| **P-iii** bounded, monotonic | pass | The deviation moves exactly one axis by at most one band and the result is clamped to the registry's declared scale. `Δ_MAX` bounds conditioning; `p_floor` bounds degeneracy in the other direction |
| **P-iv** graded, recoverable | pass | §5 — generation is total. The failure mode this property exists to catch is a fragile all-or-nothing outcome on a load-bearing event, and the load-bearing event here (can a required post be filled) cannot fail |
| **P-v** right engine | pass | Not a contest, so neither canonical resolver applies. A draw from a declared distribution is the right tool; putting a contested roll here would be a resolution where the answer is a construction |

**Loops.** Generation feeds population (`03`), which feeds posts filled, which feeds demands. The
cycle is bounded because demands are raised only by vacancies and scenes, and both are bounded by the
map. It is not a gain loop: satisfying a demand *removes* it.

**N / R / S / E.** Necessary — a game whose strategic layer is gated on people existing cannot omit
the thing that makes people. Robust — the two failure directions (degenerate conditioning, unbounded
deviation) are each bounded by a declared parameter with an arithmetic check. Smooth — one pipeline
for authored and generated characters, one substream, one attribute roster read from the registry.
Elegant — four stages, four drawn fields, each with a named consumer.
