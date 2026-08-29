# 07 — Places and settlements

> ⚠ **ARCHIVED / SUPERSEDED (2026-08-29).** This is the **pre-critique** version. It is retained
> unedited so the adversarial findings against it stay checkable — **do not build from it.** Six of
> its claims are known false; see [`ARCHIVED.md`](ARCHIVED.md). The live suite is
> `proposals/2026-08-29-greenfield-systems-suite-v2/`.


## Status: PROPOSED (2026-08-28) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md)
## Produces: the Place object, the tier registry, and the gauge set every other document deposits into

---

## 1. One object for every node of the map

A settlement, a territory, a province and a country are the same object at different tiers. Building
them as separate types is how one word ends up naming two tiers, how a settlement can name a parent
that does not exist, and how a stat scale at one tier is never cross-referenced against the
differently-scaled stat at the tier above.

A Place is an **entity of kind `place`** (`01 §1`) — the same primitive as a person, a faction or a
unit, with a different declared identity field set. Nothing about it is a separate object type.

```
identity(place)                       immutable after load
├── kind          : declared in the tier registry — Settlement, Town, Port, Fortress, …
├── tier          : declared by the kind — settlement | territory | province | country
├── parent        : node_id | None      MUST resolve to a live node of the tier above
└── owner_faction : faction_id | None   ← changes only through the campaign seam (05 §5.1)

posts    : [post_id]           sited here; see §4
tags     : [Tag]               durable memory of what was done here
gauges   : {gauge_id: Gauge}   see §3
residents: derived — the persons whose current node is this one
```

**`kind` is data and `tier` follows from it.** Adding a place kind is a registry row: a name, a tier,
a base yield, a base accrual rate, which posts it sites, and its gauge floors and ceilings. There is
no branch on a place kind anywhere in this suite, and no place is named in code.

---

## 2. `references/tier_registry.yaml` — the new registry

This is the fourth registry `00 §6` names. It carries the map's *shape*, which is not a descriptor
(it is not a quantified-qualitative value), not a module contract (it has no resolver), and not a key
type.

```yaml
version: 1
tiers: [settlement, territory, province, country]     # the containment ladder — ORDERED

kinds:
  - kind: Settlement
    tier: settlement
    sites_posts: [governor]
    base_yield: <n>
    base_accrual: {entitlement: <n>, budget: <n>}
    gauge_bounds:
      acceptance.legitimacy: {floor: 0, ceiling: 7, lambda: <λ>, rest: <r>}
      condition.order:       {floor: 0, ceiling: 5, lambda: <λ>, rest: <r>}
      # …
  - kind: Fortress
    tier: settlement
    sites_posts: [governor, commander]
    # …

nodes:
  - node_id: <id>
    kind: <kind>
    parent: <node_id | null>
    adjacency: [<node_id>, …]           # symmetric; validated at load
```

Cooked to a typed artifact by an exporter with a **blocking `--check` round-trip**, and read at
runtime by one leaf module under `engine/substrate/`, on the pattern the three existing cooked
artifacts already set: the authored surface stays reviewable, code reads the cooked one, and one
exporter owns the parse.

### 2.1 Four load-time validations, and each kills a whole defect class

| # | validation | the class it kills |
|---|---|---|
| **V-1** | every `parent` resolves to a live node **of the tier immediately above** | a place sited in a container that does not exist — which is how a node ends up hosting a settlement while being absent from the map, invisible to every count-based check because both counts match |
| **V-2** | `adjacency` is symmetric, and every member is a live node | a one-way edge that any graph walk reaching it dead-ends on |
| **V-3** | every `kind` is in the declared set, and every kind declares bounds for every gauge it carries | a place kind with no entry in the table that reads it — a hole that only surfaces when the table is consulted |
| **V-4** | every declared gauge satisfies `rest + max_seasonal_accrual/λ ≤ ceiling` | a gauge whose declared accrual sources can pin it at its ceiling (`01 §4.1`) |

**All four are arithmetic over the registry and need no campaign run.** They are load-time raises, not
warnings: a malformed map fails at startup, which is the only place it is cheap to fail.

### 2.2 Tier is not scale

`tier` answers *what contains what*. `scale` answers *how far an event's consequence reaches*, and its
enum is the ruled runtime four. A place declares both; a Key carries only `scale`. This is the axis
split from `00 §1.1`, and it is what lets the containment ladder be as deep as the world needs
without proposing a fifth member of an enum that raises on one.

---

## 3. The gauge set — eight gauges, three disclosed groups

| group | gauges | what it is |
|---|---|---|
| **acceptance** | `acceptance.legitimacy`, `acceptance.support` | whether the people here accept who governs them, and whether they accept *how*. The consent gate on everything extracted from here |
| **condition** | `condition.order`, `condition.prosperity`, `condition.defense` | what the place is materially like |
| **pressure** | `pressure` | how much unattended business has accumulated. The season's business is drawn against it (`08 §5`) |
| **accrual** | `accrual.entitlement`, `accrual.budget` | what fills up here: soldiers owed, and the governor's action points |

**Eight gauges, three bars.** The player sees an acceptance band, a condition band and a pressure
band — not eight numbers. Bands are what the disclosure contract publishes for values whose precise
magnitude is not a decision the player makes; the individual gauges and every deposit into them,
with provenance, remain inspectable underneath. Nine parallel meters is what a design looks like when
each mechanic brings its own; three is what it looks like when they share primitives.

### 3.1 Every one of them decays geometrically

`01 §4.1`. Order slips without attention, prosperity reverts toward what the place naturally
supports, acceptance drifts toward its rest, pressure bleeds off. All four with the same arithmetic
and the same guarantee: for a bounded per-season accrual `a`, the fixed point is `rest + a/λ`, finite
for every `λ > 0`.

**This is where the death-spiral class dies.** A restoring term that pulls back by at most a fixed
step per season is bounded above by that step, so any accrual larger than it pins the value and holds
it there — a state that ordinary play can reach and cannot leave. A geometric restoring term has no
such ceiling on its own strength. The property is checked at load by V-4, not discovered in a
playtest.

### 3.2 Accrual is a property of what is built here

```
accrual_rate(place) = base_accrual(kind) + Σ_facility  facility_rate(f)
```

One accrual primitive, several typed consumers: `accrual.budget` is spent by governance verbs,
`accrual.entitlement` is spent by the levy channel of muster. Three independent things-that-fill-up
per place, each with its own rate, cap and consumer, is the same failure three more times; one rate
with typed spenders is one bifurcation analysis.

---

## 4. Posts are sited by kind, and that is the whole of "who governs here"

A place kind declares `sites_posts`. A Settlement sites a `governor`; a Fortress sites a `governor`
and a `commander`; a country's seat node sites a `head` and its ministers.

Three consequences:

1. **Which places have governance is data.** Not every node needs a governor, and which do is a
   registry decision rather than a code branch.
2. **The C1 gate at settlement scale is the same check as at faction scale.** No governor → this
   place's governance modules do not run this season. Same gate, same emission, same recovery path.
3. **`residents` and `posts` are different things.** A person resident at a place is a candidate; a
   person holding a post there is an officeholder. The distinction is what makes `pm.candidates`
   (`04 §3`) have anything to choose from.

---

## 5. Yield, and why holding pays

```
yield(place) = base_yield(kind)
             · f(condition.prosperity band)
             · compliance(acceptance band)
             · fiscal_stance_multiplier(owner.policy)
```

`compliance` is monotone in the acceptance band and lies in `[0, 1]`. It is the term that makes
extraction self-limiting: taking more lowers acceptance, and lower acceptance realises less of what
is taken.

**This is a place property, which is what closes the economy's open circuit at the root.** A faction's
treasury is an aggregate over its holdings' yields (`06 §2`), so holding pays, losing a place costs
twice — once in weight, once in income — and every extraction mechanic finally has a quantity to
modulate. Nothing about this is a balance change; it is the difference between a resource with a
source and one without.

---

## 6. Facility — the progression axis, with a writer

`facility` is the set of things built at a place. It raises `accrual_rate` (§3.2), it raises
`yield` (§5), it can raise a gauge ceiling, and it can site an additional post.

**It is raised by a governance verb** (`08 §4`), which is the point. A progression axis that nothing
ever raises is flat, and a flat progression axis makes every place at every tier interchangeable for
the whole campaign. Facility is the one quantity in the place object whose whole job is to change,
and the verb that changes it is a normal budget-costing action with a graded outcome.

**Bounded:** each kind declares a facility ceiling, so the accrual it feeds is bounded, so §2.1's V-4
check stays satisfiable. That bound is also what keeps `03 §3`'s population ceiling computable — more
facility can site more posts, and posts are a term in the population bound.

---

## 7. Adjacency, and what it is for

The adjacency graph in the tier registry is used for exactly three things in this suite, named so the
graph does not accrete consumers:

| consumer | uses adjacency for |
|---|---|
| `act.campaign` (`09 §2`) | which holdings a faction may campaign against |
| `08 §5` the season's business | whether a neighbour's crisis is visible from here |
| `06 §2` the yield aggregate | nothing — yield is local, deliberately |

The third row is a refusal. Making yield depend on a supply chain through the adjacency graph is a
tempting and expensive mechanic that would put a graph traversal in the innermost economic loop and
make every place's income depend on distant state the player cannot see. If a supply mechanic is
wanted later it enters as a *facility* that raises a local gauge, not as a term in the yield formula.

---

## 8. Module contracts

```yaml
- module: pl.registry
  parent: places
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: gate
  remit: []
  budget: null
  consumes: []
  emits: []
  state:
    - {name: entity, bucket: entity, writable: false, owner: substrate.entity}   # loaded, not written
  disclosure:
    - {of: place, inputs: published, presentation: exact, trigger: hidden}

- module: pl.gauges
  parent: places
  scales: [settlement, territory]
  tier: settlement
  resolver: accrual
  remit: []
  budget: null
  consumes: []
  emits: []
  state:
    - {name: acceptance.legitimacy, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: acceptance.support,    bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: condition.order,       bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: condition.prosperity,  bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: condition.defense,     bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: pressure,              bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: accrual.entitlement,   bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: accrual.budget,        bucket: gauge, writable: true, owner: substrate.gauge}
  disclosure:
    - {of: acceptance.legitimacy, inputs: published, presentation: band, trigger: hidden}
    - {of: acceptance.support,    inputs: published, presentation: band, trigger: hidden}
    - {of: condition.order,       inputs: published, presentation: band, trigger: hidden}
    - {of: condition.prosperity,  inputs: published, presentation: band, trigger: hidden}
    - {of: condition.defense,     inputs: published, presentation: band, trigger: hidden}
    - {of: pressure,              inputs: published, presentation: band, trigger: hidden}
    - {of: accrual.entitlement,   inputs: published, presentation: exact, trigger: hidden}
    - {of: accrual.budget,        inputs: published, presentation: exact, trigger: hidden}

- module: pl.yield
  parent: places
  scales: [settlement, territory]
  tier: settlement
  resolver: derivation
  remit: []
  budget: null
  consumes: []
  emits: []
  state:
    - {name: yield, bucket: gauge, writable: false, owner: pl.yield}
  disclosure:
    - {of: yield, inputs: published, presentation: exact, trigger: hidden}
```

The two accruals disclose **exact** rather than band: they are spent directly by the player's own
actions this season, so their remaining magnitude is a decision input rather than a background
condition. Everything else is a band.

`pl.yield` is `writable: false`. Nothing writes an income; income is what the place's state comes to.

---

## 9. Property audit

**Scope.** Nothing in this document rolls. `pl.registry` is a validated load, `pl.gauges` is accrual
and decay, `pl.yield` is a derivation. The five properties are applied to the gauges and the loops;
**no N/R/S/E verdict is offered for a store**, because manufacturing one for state with no draw is
the error the methodology explicitly names.

| property | verdict | reasoning |
|---|---|---|
| **P-iii** bounded, monotonic | pass, and it is the strongest claim in the suite | Every gauge is bounded by declared floor and ceiling and restores geometrically, so the fixed point is finite for every bounded accrual. V-4 checks that property at **load time**, against the registry, with no campaign run. Facility is ceiling-bounded per kind, so the accrual it feeds cannot grow without limit |
| **P-v** right engine | pass | Accrual, decay and derivation. Nothing here is uncertain and nothing here rolls. The place is the state the rest of the game resolves *against*, and a place that rolled for its own condition would be resolving a question nobody asked |

**Loops.** Facility → accrual → verbs → facility is positive, bounded by the per-kind facility
ceiling, and its gain is **unmeasured** — the same loop `03 §7` and `06 §7` name from their own ends,
and the same honest answer: it is campaign-reachable, so it is measurable with a control, and it
should be measured before the facility writer lands.

**Necessary** — eight gauges, each with at least one named depositor and one named consumer; a ninth
was not added because the mechanics that would have wanted one are expressible as tags. **Robust** —
the two failure directions the corpus measured, an unrecoverable pressure state and a flat progression
axis, are closed by an arithmetic property and by a writer respectively. **Smooth** — one object for
every tier, one decay law for every gauge, one registry for the map's shape. **Elegant** — three
modules, one new registry, and no branch on a place kind anywhere.
