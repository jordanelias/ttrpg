# 08 — Settlement management

> ⚠ **ARCHIVED / SUPERSEDED (2026-08-29).** This is the **pre-critique** version. It is retained
> unedited so the adversarial findings against it stay checkable — **do not build from it.** Six of
> its claims are known false; see [`ARCHIVED.md`](ARCHIVED.md). The live suite is
> `proposals/2026-08-29-greenfield-systems-suite-v2/`.


## Status: PROPOSED (2026-08-28) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) · [`07_places_and_settlements.md`](07_places_and_settlements.md)
## Produces: the governor's season — the two-stroke loop that makes a place a thing you govern rather than a thing you own

---

## 0. The unsettled-problem warning, stated first

The appointed-governor role is one of the genre's genuinely open problems. One franchise added,
removed and re-added it **three times for three different reasons across twenty years**, and the
survey's verdict is explicit: there is no convergent answer here. Nothing in this document should be
read as catching up to a solved design. The *components* — a budget, a mandatory demand from above,
methods that trade one thing for another, and a memory of what was chosen — are agreed; the
composition is not.

---

## 1. The gate

Same shape as `05 §1`, one tier down. A place whose governance post is vacant runs no governance
modules this season and emits `faction.action_declined(place, reason="vacant_governor")`.

Recoverable by the same path: the vacancy raises a demand, and generation is total.

---

## 2. The season, in two strokes

```
        ┌─────────────── the world acts on the place ───────────────┐
        │   sm.business    the season's business, drawn from the    │
        │                  place's own ledger and gauge extremes    │
        │   sm.directive   one typed order from the principal       │
        └───────────────────────────┬───────────────────────────────┘
                                    ▼
        ┌──────────────── the place acts on the world ──────────────┐
        │   sm.respond     answer the directive: 4 responses        │
        │   sm.verb        spend accrual.budget on governance verbs │
        └───────────────────────────────────────────────────────────┘
```

**Both strokes always fire.** A season always presents business and always presents a demand, and the
budget is never enough to serve both. That gap is the game: the tension is not in any single verb, it
is in the fact that the directive and the place's own needs routinely want the same points.

---

## 3. `sm.directive` — the down-stroke, with four responses

The principal issues **one** typed directive per place per season: `extract` · `levy` · `suppress` ·
`install` · `host` · `cede`. Which one is a derivation over the principal's state and the place's,
consuming no randomness.

| response | resolver | what it costs | what it gains |
|---|---|---|---|
| **Comply** | `gate` — deterministic | the demanded deposit lands on the place's gauges | `standing` deposit up for the governor; the principal's trust |
| **Bargain** | `d_sigma` — **SO** against `derive_ob(principal_holder.standing)` | a budget point; a `suspicion` deposit even on success | softer terms, scaled by degree |
| **Commute** | `gate` on the place's own state | trades one extraction type for another (§3.1) | terms the place can actually meet |
| **Defy** | `gate` — deterministic, no roll | a `standing` deposit down, a `suspicion` deposit up, a `Precedent` tag on the place | the demanded deposit does not land; `acceptance.support` deposit up |

Four responses, **three resolver kinds**, each matched to its question: compliance and defiance are
choices with determinate consequences, bargaining is genuinely uncertain, and commutation is a
threshold on whether the place can support the alternative.

### 3.1 Commute — the response this layer is usually missing

Comply / Bargain / Defy offer *more or less of the same thing*. Commute offers **a different thing**,
and that is what turns the directive from a compliance check into a decision:

| commutation | trades away | takes on |
|---|---|---|
| **money for service** | a higher `extract` deposit | a much lower `levy` obligation |
| **service for money** | a higher `levy` obligation and a `condition.defense` commitment | a much lower `extract` deposit |
| **autonomy for reputation** | reduced obligation on both axes | a `standing` deposit for both parties, and a durable `Debt` tag naming the terms |

Availability is a gate on the place's own state: a place with no prosperity cannot buy out of service,
and a place with no defensible position cannot offer one. So the same directive presents different
options at different places, which is the whole point.

The terms are a `Debt` tag with a `ttl` and `recurs=True` — a claim that fires every season of its
term and then expires. That is what a term-limited recurring obligation *is* under the closed tag
enum; it is not a sixth tag family.

### 3.2 The frequency cap, from the start

**One directive per place per season, and repeated directives of the same type against the same place
within a term cost the principal an escalating `standing` deposit.**

Every mature example of this surface ships a cap of this shape, and ships it *as an
anti-micromanagement guardrail* rather than trusting players to self-regulate. It is one comparison
and one deposit now; retrofitting it later means retuning every directive's weight against a loop
that has already been balanced without it.

### 3.3 Suspicion is a gauge and it is not a countdown

Defiance and hard bargaining deposit into a `suspicion` gauge on the post. Its band is what
`pm.audit` (`04 §5`) reads as a modifier, and a sustained high band is what makes a principal reach
for `pm.recall` — which still requires a citable tag, so suspicion alone never removes a governor.

It decays geometrically like everything else. A governor who defied once and then complied is
recovering; a governor who defies every season is not. There is no threshold at which something fires
automatically, and there is no published trigger point.

---

## 4. `sm.verb` — the up-stroke, four verbs, two forks each

**Four shipped verbs, eight leaves total.** The compression is deliberate and it is the discipline the
survey's own best example sets: a franchise that reduced a five-layer morale stack, a pairwise opinion
matrix, event deltas and prejudice axes to two one-line rules did not lose the feel. Every research
lane recommends its own subject's full apparatus; the ratio to aim for is the compressed one.

| verb | cost | pool attrs | obstacle | fork A | fork B |
|---|---|---|---|---|---|
| **Develop** | 2 | mind pair | `derive_ob(condition.prosperity)` | **charter** — faster; writes a `Leverage` tag for the chartered party | **corvée** — cheaper; deposits down on `acceptance.support` |
| **Order** | 1–2 | varies by fork | `derive_ob(pressure)` | **consent** — 2 points, social attrs; deposits up on `acceptance.support` | **force** — 1 point, martial attrs; deposits down on `acceptance.support`, up on `condition.order` |
| **Court** | 1 | social pair | `derive_ob(disputant score)` — **SO** | **judge** — settles it; writes a `Precedent` tag biasing related business | **defer** — costs nothing now; deposits up on `pressure` |
| **Build** | 2 | mind pair | `derive_ob(2·(facility_tier + 1))` — see §4.0 | **treasury** — spends the owner's yield | **levy-in-kind** — spends `accrual.entitlement`; deposits down on `acceptance.support` |

### 4.0 Why Build's target score is `2·(tier + 1)` and not the tier itself

`derive_ob` halves its target score, so feeding it the raw facility tier (0–3) yields obstacles of
0 … 1.5, all of which floor at `OB_MIN`. **Every tier of the progression axis would then cost the
same, and the cheapest one would be free** — a progression track with no increasing price, which is
the failure mode of a progression track that nothing ever raises, arrived at from the opposite
direction.

`2·(tier + 1)` halves back to `tier + 1`, giving obstacles of 1, 2, 3, 4 — monotone increasing, floored
at the ruled minimum at the bottom, and expressed entirely through the single obstacle owner rather
than by special-casing this verb's arithmetic.

The other three verbs need no such adjustment: their target quantities already span a range whose half
is meaningful (`condition.prosperity` 0–5, `pressure` 0–10, a disputant's score 1–7).

### 4.1 The rule that keeps the fork set from collapsing

> **Each fork of a verb must change a *different pair* of gauges. A fork that differs only in
> magnitude is cut.**

This is not tidiness. The closest existing analogue to a menu of graded manoeuvres collapsed in play
because players found the two highest-magnitude options and stopped using anything else — and one
option went entirely unused because too many things beat it. **Manoeuvres must differ in what they
change about the state, not in how much they subtract.** A fork rule that is checkable at the registry
row is the version of that lesson that survives contact with a later author.

Check it by reading the table above: `consent` and `force` do not differ in how much order they buy;
they differ in which gauge pays. `judge` and `defer` do not differ in strength; one settles the matter
and one converts it into pressure.

### 4.2 Failure is fail-forward and never removes the post

Every verb's effects table is total over the four bands. On Failure the budget point is spent, the
intended deposit does not land, and **a `Precedent` tag is written recording what was attempted** —
so a failed attempt is a fact the place remembers and a later audit can read, rather than a wasted
season with no trace. On Partial the deposit lands at reduced magnitude and no tag is written.

Nothing in the table fires only on Partial (P0-3), and **no verb outcome revokes the governor's
post.** Removal runs through `pm.recall` or `pm.audit`, both of which require either a citable tag or
an expired term. A verb that could remove its own actor would make an ordinary season's routine
action an elimination check.

### 4.3 The candidate verbs

The compression is the shipped set, not the ceiling. Further verbs enter as registry rows in the same
shape, each subject to the §4.1 fork rule and the §4.2 outcome rule: *Survey* (locks an assessment
that later extraction reads), *Sponsor* (a durable `Debt` toward a named person), *Treat* (a bilateral
side-agreement with a local actor), *Retain* (buys accrual for treasury and a hidden cost). Each is
one row and none is a precondition of the others.

---

## 5. `sm.business` — the ledger is the deck

The season's business at a place is drawn against its `pressure` band:

```
n = 1 + floor(pressure_band)
```

**And what is drawn is the place's own state, not an authored card.** The candidate pool for a place's
business is:

| candidate source | becomes |
|---|---|
| an open `Grudge` tag on the place or on its governor | someone is aggrieved, and this season they act on it |
| an unserved `Debt` tag whose term is running | a claim comes due |
| a gauge at or near an extreme band | the condition itself is the business — a place at low order presents disorder |
| a `Precedent` tag being tested by a new event | the ruling you made last year is cited back at you |
| an adjacent place at an extreme band | your neighbour's crisis is visible from here (`07 §7`) |

**Three things this buys, and the first is the reason for it.**

1. **It closes the loop that everything else in the corpus leaves open.** Events flow out of
   resolutions and are never read back in. Here the ledger a verb writes *is* what the next season
   presents, so a governor's choices become the world's demands on them. `Key.causes[]` becomes a
   chain that a player can follow from a decision to its consequence three seasons later.
2. **It needs no authored content to function.** A deck is content, and content that does not exist
   makes the mechanic inert. A place with tags and gauges always has business. Authored cards remain
   possible later as an *enrichment* — an entry in the same candidate pool with a hand-written frame —
   never as a precondition.
3. **It cannot present something the world has not caused.** Every item of business traces to a tag or
   a gauge, and every tag carries provenance. There is no channel by which business appears for no
   reason, which is the property that makes the layer trustworthy in a game with no GM.

### 5.1 Pressure

`pressure` accrues from unserved business — an item presented and not answered deposits — and decays
geometrically toward `rest`. `07 §3.1` is the whole safety argument: the fixed point for a bounded
per-season accrual `a` is `rest + a/λ`, finite for every `λ > 0`, and V-4 checks at load that the
declared accrual sources cannot exceed what the ceiling admits.

**The version not built, and why:** a restoring term that pulls back by at most a fixed step per
season is bounded above by that step. Any accrual larger than it pins pressure at its ceiling
permanently, and a design with several concurrent accrual sources reaches that regime as its *default*
rather than as an edge case. That is not a tuning failure; it is the shape, and no amount of
rebalancing the sources recovers a system whose restoring term has a ceiling lower than its input.

---

## 6. Module contracts

```yaml
- module: sm.gate
  parent: settlement_management
  scales: [settlement]
  tier: settlement
  resolver: gate
  remit: []
  budget: null
  consumes: [{type: post.vacant, from: [pm.vacancy]}]
  emits: [{type: faction.action_declined, terminal: true}]
  state: []
  disclosure: [{of: decline_reason, inputs: published, presentation: exact, trigger: hidden}]

- module: sm.business
  parent: settlement_management
  scales: [settlement]
  tier: settlement
  resolver: derivation          # a draw over the place's own state; the pool is not authored
  remit: []
  budget: null
  consumes: []
  emits: []
  state:
    - {name: pressure, bucket: gauge, writable: true, owner: substrate.gauge}
  disclosure:
    - {of: pressure, inputs: published, presentation: band, trigger: hidden}

- module: sm.directive
  parent: settlement_management
  scales: [settlement, territory]
  tier: settlement
  resolver: derivation
  remit: [head, minister]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: [{type: place.directive_issued, terminal: false}]
  state:
    - {name: tag, bucket: tag, writable: true, owner: substrate.ledger}
  disclosure:
    - {of: directive, inputs: published, presentation: exact, trigger: hidden}

- module: sm.respond
  parent: settlement_management
  scales: [settlement]
  tier: settlement
  resolver: d_sigma             # Bargain rolls; Comply, Commute and Defy are gates
  remit: [governor]
  budget: {gauge: accrual.budget, cost: 1}
  consumes: [{type: place.directive_issued, from: [sm.directive]}]
  emits: [{type: place.directive_answered, terminal: false}]
  state:
    - {name: suspicion,          bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: standing,           bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: acceptance.support, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag,                bucket: tag,   writable: true, owner: substrate.ledger}
  disclosure:
    - {of: suspicion, inputs: published, presentation: band, trigger: hidden}
    - {of: response_options, inputs: published, presentation: exact, trigger: hidden}

- module: sm.verb
  parent: settlement_management
  scales: [settlement]
  tier: settlement
  resolver: d_sigma
  remit: [governor]
  budget: {gauge: accrual.budget, cost: 1}       # per-verb cost overrides in the verb row
  consumes: []
  emits: []
  state:
    - {name: condition.order,       bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: condition.prosperity,  bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: condition.defense,     bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: acceptance.support,    bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: accrual.entitlement,   bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag,                   bucket: tag,   writable: true, owner: substrate.ledger}
  disclosure:
    - {of: pool,     inputs: published, presentation: exact, trigger: hidden}
    - {of: obstacle, inputs: published, presentation: exact, trigger: hidden}
```

`sm.business` is a `derivation`, not a `d_sigma`: which items a place presents is a selection over its
own state, and the uncertainty in the season is in how the governor *answers* them, not in what they
are.

---

## 7. Property audit

**Scope.** `sm.gate`, `sm.business` and `sm.directive` do not roll and are diagnosed on P-iii and P-v
only. `sm.respond` (the Bargain branch) and `sm.verb` roll and are diagnosed on all five.

| property | verdict | reasoning |
|---|---|---|
| **P-i** legible odds | pass | Pool is the governor's two named attributes plus the declared base; obstacle is the target quantity halved. Both published exactly. The response options and the business items are published; only the audit's tipping point and the pressure draw threshold are hidden |
| **P-ii** uniform leverage | pass | Every verb resolves at a governor-scale pool inside the calibrated band. Fork choices change *which gauges move*, never the pool or the obstacle. The budget buys attempts. Nothing here is a flat obstacle shift and nothing adds a die |
| **P-iii** bounded, monotonic | pass | Every gauge is floor/ceiling-bounded with geometric decay, checked at load by V-4. Pressure's fixed point is finite for any bounded accrual — the saturating alternative, which is the shape that produces an unrecoverable state from ordinary play, is explicitly the version not built (§5.1). `derive_ob`'s floor prevents a cliff at `OB_MIN` |
| **P-iv** graded, recoverable | pass | Every verb and the Bargain branch are total over the four bands with nothing unique to Partial. Failure is fail-forward — a tag is written, the season is not blank — and **no verb outcome removes the governor's post**. The layer's worst routine outcome is a wasted point and a bad record |
| **P-v** right engine | pass, and it is the point of the response table | Four responses, three resolver kinds, each matched: Comply and Defy are determinate choices (`gate`), Commute is a threshold on the place's own state (`gate`), Bargain is genuinely uncertain (`d_sigma`). The failure this avoids is reaching for the kernel where the answer is on the board — which the precedent survey finds is this tree's most common wrong-engine defect |

**Loops.** Two, both declared. *Verb → gauge → business → verb* is the intended core loop; it is
bounded by the gauge ceilings and damped by geometric decay, so unattended business raises pressure
and attended business lowers it, with a finite fixed point either way. *Facility → accrual → verbs →
facility* is positive and bounded by the per-kind facility ceiling; its **gain is unmeasured** and is
named as such in `07 §9` and `03 §7` from the other two ends.

**N** — four verbs, eight forks, and the fork rule (§4.1) is what stops the ninth from being a
magnitude variant of the first. **R** — the two documented failure directions are closed
structurally: the unrecoverable pressure state by the decay law, and the collapse-to-two-best-options
by the fork rule. **S** — a governance verb and a faction action are the same object at different
tiers, with the same pool shape, the same obstacle owner and the same four primitives. **E** — five
modules, and the one carrying the most weight, `sm.business`, needs no authored content at all
because the ledger is the deck.
