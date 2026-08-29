# 03 — World population

> ⚠ **ARCHIVED / SUPERSEDED (2026-08-29).** This is the **pre-critique** version. It is retained
> unedited so the adversarial findings against it stay checkable — **do not build from it.** Six of
> its claims are known false; see [`ARCHIVED.md`](ARCHIVED.md). The live suite is
> `proposals/2026-08-29-greenfield-systems-suite-v2/`.


## Status: PROPOSED (2026-08-28) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) · [`02_character_generation.md`](02_character_generation.md)
## Produces: the answer to *how many people exist, where, and when are they created*

---

## 1. The rule

> **Population is a function of posts and places. It is not a function of time.**

There is no birth rate, no spawn queue, no wandering-adventurer tap, no departure percentage, and no
population target. Every person in the world exists because something needed a person, and the count
of things that can need a person is bounded by the map.

This is the answer to the only question in the corpus that a design document *had* to answer before
the engine could run, and it is the answer two independent lines of evidence converge on:

- **The measured failure of the alternative.** The nearest analogue franchise generates on a clock and
  pays for it with five-figure late-campaign character counts, two community mods pulling in opposite
  directions, and a developer fix that throttled the tap at its low-value tail.
- **ED-IN-0201's own consequence.** Under the gate, a faction with no head takes no action. A
  generator that produces people *during* play cannot guarantee a head exists when the season loop
  asks on turn one. Only a demand-driven population, seeded from required posts at world-gen, can
  satisfy the gate at season 1.

---

## 2. World-gen: exactly the people the gate requires, plus a candidate margin

At world creation, in this order, consuming no shared randomness:

| # | step | produces |
|---|---|---|
| 1 | Load the tier registry; validate every place's parent edge resolves to a live node | the map |
| 2 | Instantiate the **required posts**: one `head` per faction; one `governor` per place whose kind declares a governance post; `minister` posts per the faction's declared offices | the demand set |
| 3 | Issue one `cg.demand` per required post; satisfy each authored-first (`02 §3`) | the officeholders |
| 4 | Issue `k` local-actor demands per place, unaffiliated with any faction | the candidate margin |
| 5 | Materialise the edges the generator attached, and validate the graph has no dangling person ids | the relationship graph |

Step 4 is the only place a bare number appears in this document, and it is the one the corpus itself
names as unavoidable. `k` is the per-place candidate margin: the people who are not officeholders and
who are therefore available to be appointed, recruited, married, murdered or ignored. Without it the
world contains exactly as many people as it has posts, and every appointment is uncontested — which
removes the mechanic that `04` exists to be.

`k` is declared in the exported params with a stated reachability bar, not buried: **at the map's
median place, at least two candidates must qualify for the governance post's candidate gate.** A `k`
that fails that bar produces an appointment surface with no decision in it.

---

## 3. The bound, stated arithmetically

```
|persons|  ≤  |required_posts|  +  k · |places|  +  |active_scene_demands|

|required_posts|  =  |factions|                              # one head each
                  +  |places with a governance post|
                  +  Σ_factions |declared minister offices|
                  +  |commander posts raised this season|    # transient; see 09 §2
```

Every term on the right is bounded by the map or by a declared constant:

- `|factions|`, `|places|` — fixed by the tier registry, which is data loaded once.
- `|declared minister offices|` — a per-faction constant in the registry.
- `|commander posts|` — bounded by the faction's action budget, which is bounded by its filled posts.
- `|active_scene_demands|` — bounded by the scene budget per season, a declared constant.

**So the population has a computable ceiling from data alone, without running a campaign.** That is
the property the ambient-spawn model cannot have, and it is checkable as arithmetic.

**Falsifier:** a test computing the ceiling from the registries and asserting the person store never
exceeds it across a seeded campaign. Load-bearing on the game — the failure it catches is the one
that turns a late campaign into an unplayable roster.

---

## 4. Population changes only through named events

Between world-gen and the end of the campaign, the person count moves for exactly four reasons, and
each is a Key with a cause:

| event | direction | raised by |
|---|---|---|
| a post falls vacant and no candidate qualifies | **+1** — a `cg.demand` at that node | `04 pm.vacancy` |
| a scene requires a participant that does not exist | **+1** | the scene dispatcher |
| death | **−1** | a resolution outcome — never a mortality roll on a timer |
| exile or withdrawal | **−1**, reversibly | a resolution outcome |

**There is no season-tick population step.** Nothing in the accounting boundary iterates people to
decide whether more should exist. That absence is the design.

### 4.1 Death is an outcome, never a clock

A mortality clock is a pacing device some political games use deliberately and well. It is refused
here for a specific reason rather than on taste: under ED-IN-0201, a death that empties a head post
stops a faction acting. A death on a timer therefore silently gates the strategic layer on a die roll
nobody made a decision about. Death as an *outcome* of something — a battle, a tribunal, a
succession contest, a scene — keeps the gate coupled to play.

Ageing is not modelled. If it is ever wanted, it enters as a gauge with a band, not as a per-season
elimination check.

---

## 5. Idleness

Four of five surveyed personnel systems punish idleness, and the convergence is unusually clean: an
unassigned person who is simply inert is a person the player has no reason to think about. Valoria
today has no state that degrades from neglect.

**But the naive import is a documented shipped failure.** A game that applied a flat per-turn
loyalty decay to characters — in a world with fewer posts than characters, so that some were
*structurally* idle — produced a bleed the player could not out-invest at any level of play, and the
whole action-currency was scrapped four months after launch.

The reconciliation is a matter of **scope and shape**, and both halves are needed:

> **Idleness applies only to a person who held a post and lost it, and it is a one-time deposit at the
> moment of loss, not a per-season bleed.**

```
on post_revoked(person p, post q):
    gauge_deposit(p.standing, −δ(q), provenance=<the revocation Key>)
```

where `δ(q)` scales with the post's weight. `standing` is a Gauge, so it recovers geometrically
toward `rest` at `λ` per season with no further input. The person is diminished by having been
removed and recovers over time — which is the felt experience the convergence is about — and there is
no term that can accumulate faster than the restoring one, because there is no recurring term at all.

A person who was **never posted** does not decay. They are a candidate, not a failure.

### 5.1 Why the scope test can be run before the writer lands

Take the maximum available per-season mitigation and run it against the maximum accrual: with a
one-time deposit and geometric recovery, the worst case is a single `δ_max` against a recovery of
`λ·(value − rest)` per season, which is recoverable for every `λ > 0`. **The check is arithmetic and
needs no campaign run** — which is exactly the guard the shipped failure lacked.

**And the pathological case is bounded too, which is the version worth checking.** A person churned
through posts — appointed and removed every season — takes a deposit every season, which *is* a
recurring term. It is still bounded: a per-season deposit `δ` against geometric restoring settles at
`rest − δ/λ`, finite for every `λ > 0`, and clamped at the gauge's floor besides. So even the case
the scope rule was written to exclude cannot produce an unrecoverable state — the decay law does that
work, not the scoping. The scoping is what keeps the *ordinary* case from feeling like a bleed.

---

## 6. Determinism and the RNG contract

**P0-2 is a precondition of this document, not a step inside it.** A person store with a per-season
consumer of the shared campaign stream re-phases every downstream draw the moment it stops being
empty — and a population is precisely a store with a per-season consumer.

| rule | statement |
|---|---|
| **R-1** | Person generation draws only from the `cg` substream (`02 §4`), derived from the campaign seed |
| **R-2** | Any per-season iteration over people that draws randomness uses a **population substream**, distinct from both the campaign stream and the `cg` stream |
| **R-3** | Population guards read the **person store**, never a call counter on the generator |
| **R-4** | The substreams land and are proved byte-identical against the existing seeded goldens **before** the first person exists |

R-3 is worth stating as a rule rather than a note: a guard that observes how many times the generator
was called is blind to every other way a person can enter the store — a load, a save restore, a test
fixture — which is to say it cannot observe the very state it exists to bound.

---

## 7. The loop this closes, and what is not claimed about it

Population is not an isolated store; it participates in a cycle:

```
posts filled  ──►  actions available  ──►  holdings and facilities  ──►  more posts
      ▲                                                                       │
      └───────────────────────────────────────────────────────────────────────┘
```

**This is a positive feedback loop and this document does not claim it is damped.**

What can be stated honestly:

- **It is bounded.** Facility tier is capped and place count is fixed, so `|required_posts|` has a
  ceiling computable from data (§3). A bounded loop is not a runaway even if its gain exceeds 1.
- **It has a second, independent bound.** `05 §4` declares a per-faction action ceiling that does not
  scale with post count, so acquiring more posts cannot translate into unbounded action volume.
- **Its per-cycle gain is unmeasured.** Whether holding more places actually returns more posts than
  it costs to hold is a campaign-level balance question with two arms, and asserting either answer
  without a control is precisely what the measurement discipline forbids in both directions.

**What to do about it:** the gain is measurable — the change is campaign-reachable, so a controlled
run has two non-degenerate arms — and it should be measured before the facility writer lands, not
after. That is named as a build-order item in `10 §3`, not resolved here.

---

## 8. Module contracts

```yaml
- module: wp.worldgen
  parent: world_population
  scales: [peninsula]
  tier: null
  resolver: gate
  remit: []
  budget: null
  consumes: []
  emits:
    - {type: person.generated, terminal: false}      # via cg.attach, one per required post
    - {type: post.vacant, terminal: false}           # for any post left unfilled at gen
  state:
    - {name: post, bucket: post, writable: true, owner: substrate.post}
    - {name: entity, bucket: entity, writable: false, owner: substrate.entity}
  disclosure:
    - {of: post, inputs: published, presentation: exact, trigger: hidden}

- module: wp.census
  parent: world_population
  scales: [peninsula]
  tier: null
  resolver: derivation
  remit: []
  budget: null
  consumes: []
  emits: []
  state: []                    # pure read; the ceiling check reads registries, not state
  disclosure:
    - {of: population_ceiling, inputs: published, presentation: exact, trigger: hidden}

- module: wp.displacement
  parent: world_population
  scales: [personal]
  tier: null
  resolver: derivation
  remit: []
  budget: null
  consumes:
    - {type: post.revoked, from: [pm.recall, pm.tenure]}
  emits: []
  state:
    - {name: standing, bucket: gauge, writable: true, owner: substrate.gauge}
  disclosure:
    - {of: standing, inputs: published, presentation: band, trigger: hidden}
```

`wp.displacement` is the whole of the idleness mechanic: one consumer of one Key, one gauge deposit.
That is the compression ratio to aim for — the surveyed franchise that compressed a five-layer morale
stack, a pairwise opinion matrix and a prejudice axis into two one-line rules did not lose the feel,
and it is the ceiling of ambition worth holding a d10 engine to.

---

## 9. Property audit

**Scope.** `wp.worldgen` and `wp.census` resolve nothing — they instantiate and derive. The five-property
test is applied to the loops and gates they create; **no N/R/S/E verdict is offered for the non-rolling
modules**, because manufacturing one for a store is the error the methodology explicitly names.
`wp.displacement` writes a gauge and is diagnosed on P-iii.

| property | verdict | reasoning |
|---|---|---|
| **P-iii** bounded, monotonic | pass | Population has a computable ceiling from data (§3). Displacement is a one-time bounded deposit into a geometrically-restoring gauge (§5), so its worst case is recoverable for every `λ > 0`. No term accumulates faster than the restoring one because there is no recurring term |
| **P-v** right engine | pass | Population is a gate on data, not a contest; displacement is a deposit, not a roll. Both use a threshold where the answer is on the board, which is the resolver kind the precedent survey says this tree under-uses |

**Loops.** One, declared in §7, bounded twice, gain unmeasured and stated as unmeasured.

**Necessary.** Under ED-IN-0201 a campaign with no people performs zero faction actions, so this is
not a feature. **Robust** — the two documented failure directions of the alternatives, unbounded
growth and an unpayable idleness bleed, are each closed by an arithmetic property rather than by
tuning. **Smooth** — one pipeline with `02`, one substream discipline, one Key per event.
**Elegant** — three modules, and the one that carries the whole idleness convergence is four lines.
