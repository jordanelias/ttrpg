# 06 — Faction management

## Status: PROPOSED (2026-08-28) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) · [`05_faction_actions.md`](05_faction_actions.md)
## Produces: what a faction *is*, what it is worth, and how it fails

---

## 1. A faction is a composition, not a stat bundle

No surveyed title models a faction as an undifferentiated scalar bundle, and the reason is
structural rather than aesthetic: **a thing with no interior cannot have politics inside it.** Every
faction-scale mechanism worth having — contracts, blocs, coalitions, court positions, competing
ambitions — presupposes *parts*. Without them that whole vocabulary is not merely unbuilt, it is
untypeable.

```
Faction
├── faction_id     : str
├── seat_node      : tier node id     PERMANENT. Not a holding; cannot be lost. See 05 §1.2
├── posts          : [post_id]        the interior — different kinds, different holders,
│                                     different remits, different convictions
├── holdings       : [tier node id]   places whose owning faction is this one
├── ledger         : [Tag]            enmity, obligation, precedent, reputation, leverage
└── policy         : {fiscal_stance, muster_stance, …}   declared rows; see §5
```

**Every quantity a faction has is derived.** There is no `Faction.stat` to write, because the write
rule (`01 §2`) admits exactly four leaves and none of them is a faction scalar.

---

## 2. The four derivations

| derived value | derived from | consumed by |
|---|---|---|
| **`faction.acceptance`** | size-weighted aggregate of each holding's `acceptance.legitimacy` and `acceptance.support` gauges | the deliberative body's vote weight (`09 §3`); the treasury's compliance term |
| **`faction.treasury`** | `Σ_holdings yield(place) · compliance(place)` − `Σ upkeep(units, posts)` | `act.muster.contract`; facility investment |
| **`faction.force`** | aggregate over held unit records (`09 §2`) — size, discipline and experience gauges | the campaign model |
| **`faction.weight`** | `Σ_posts held · weight(post kind)` + `Σ_holdings weight(place kind)` | victory scoring; diplomatic standing |

`faction.weight` is the ruling of 2026-07-13 made arithmetic: *factions do not necessarily need to
hold territory — they need to hold **people**, and it is the number of people and the weight of their
positions that carry the value of that faction.* Posts contribute directly, and they contribute even
where the faction holds no ground. A faction reduced to a seat node and three ministers is small, not
absent.

### 2.1 The naming question this document does not answer (Q-4)

`faction.acceptance` is a **provisional name**. The word this quantity is usually given is live in the
tree under three incompatible readings — a base scalar, a derived aggregate over per-place acceptance,
and a per-post authority. Picking one is a canon act, not a design one. The derivation is specified
here; the name is deferred, and it is deferred *loudly* rather than by picking the most familiar word
and quietly deciding the question.

### 2.2 Yield, and why the economy is a flow

`yield(place)` is a property of the place: its `condition.prosperity` band, its kind, and what is
built there. **Holding pays.** That is the whole of the fix to an economy whose only quantity moves in
one direction, and it is not a balance change — it is closing an open circuit.

`compliance(place)` is a monotone function of the place's `acceptance` band, in `[0, 1]`. It is the
negative feedback term in the fiscal loop: a place that is extracted from loses acceptance, and a
place with low acceptance yields less of what it produces.

---

## 3. The interior: a faction that can disagree with itself

The interior is not a new mechanism. It falls out of posts:

| the interior thing | how it is expressed | resolves through |
|---|---|---|
| a minister who wants a different action from the head | different conviction weights over the same `appeal` function (`05 §3.2`) | whoever holds the head post decides; the minister accrues a `Grudge` |
| a governor who defies a directive | the Defy response (`08 §3`) | a `standing` deposit and a `suspicion` deposit, both gauges |
| a rival claim on a post | `pm.candidates` returns more than one qualified person and the principal must choose | `pm.appoint`, and the passed-over grudge |
| an agent whose interest diverges from the faction's | a `Leverage` tag held by a rival over one of the faction's posts (`04 §8`) | the custody tag entering that holder's `preference` and `appeal` |

The last row is worth naming because it is the case every game with two stances builds deliberately
and this tree has never been able to express: a person acting *on behalf of* a faction at a scale
whose *within*-faction interest points elsewhere. Here it needs no new object — it is a tag on a post,
read by two functions that already exist.

**And there is no `if faction == X` anywhere.** A faction's character is who holds its head post. Swap
the holder and the faction behaves differently; swap two factions' names in the starting data and
nothing else changes, because there is nothing else to change.

---

## 4. Enmity is an edge, and it is what makes the strategic layer have a plot

**A faction's relation to another faction is an `edge` entity** (`01 §1.2`), exactly like a person's
relation to a person: a `disposition` gauge and a tag list, with the same decay and the same
provenance requirement. It is not a special faction-only field, and there is no second relationship
mechanism for the strategic scale.

Its deposits are written by outcomes that already fire: a motion carried against it, a holding taken
from it, an audit that stripped its appointee, a custody attempt on one of its posts. Every one of
those already knows both parties and already emits a Key, so the write is one line at a site that runs
anyway, and the provenance is free.

Target selection for every hostile action reads the edge:

```
hostility(target) = − gauge_value(edge  actor_faction → target)
                  + Σ tag_value(Grudge on that edge)
                  − Σ tag_value(Debt   on that edge)
                  + the acting head's own personal edges toward the target's post-holders
```

The last term is what makes a change of head change a faction's enemies: two heads of the same
faction inherit the same institutional edge and bring different personal ones.

That converts a hostile action from an isolated arithmetic pick into a move in an ongoing quarrel. A
faction that acted against you comes back for you; a faction you took ground from turns on you. It
costs one deposit at four sites that already fire, and a changed sort key.

**Bounded twice, and both bounds are structural** (`01 §2.2`, `01 §4.1`): tags on the edge dedupe on
`(edge, kind, key)` so their count cannot ramp, and the disposition they deposit into decays
geometrically so their magnitude settles at `rest + a/λ`. A counter with no decay feeding a selection
that generates more of it is the unbounded-ramp defect class this suite is most careful about, and it
is closed here by the primitive rather than by a rule someone has to remember.

---

## 5. Policy — declared rows, not subsystems

A policy is a row on the faction that modifies a derivation. It is not a module and it does not roll.

| policy | values | what it changes | what it costs |
|---|---|---|---|
| **fiscal stance** | light · standard · extraction | the `yield` multiplier | extraction deposits into every holding's `acceptance.support` every season it is held |
| **muster stance** | entitlement-first · contract-first | which `act.muster` channel `fa.select` prefers | — |
| **succession rule** | designation · claim-contest | which path `09 §1` takes when the head post falls vacant | — |

Changing a policy costs an action point and writes a `Precedent` tag on the faction with the season it
changed — so a faction that oscillates its fiscal stance has a visible record of doing so, and the
places it extracted from remember.

**Extraction's cost is a per-season deposit, not a threshold.** The subsistence-ethic reading that
grounds this — that what reads as injustice is a *change* in what is taken, not the level of it — is
best expressed as a deposit on the seasons the stance is held rather than a penalty at a level.

---

## 6. Collapse is the gate closing

There is no collapse procedure, no elimination check, and no dissolution routine. A faction fails
like this:

```
head post vacant  ──►  no candidate qualifies  ──►  faction takes no action
                                                     │
                       its posts fall vacant on their own terms
                                                     │
                       its holdings' governance posts are claimable by neighbours
                                                     │
                       its weight falls to whatever its remaining posts carry
```

**Three properties this has that a collapse routine does not:**

1. **It needs no detection.** The gate reads a field; nothing polls for a collapse condition.
2. **It is graded.** A faction does not flip from alive to eliminated. It stops acting, then loses
   posts as they fall vacant, then loses weight as they are claimed. Every stage is visible and
   several are reversible.
3. **It is recoverable.** The head post's demand resolves at the seat node, which cannot be lost
   (§1). A faction that stops acting can always produce a claimant; whether that claimant survives
   the succession contest (`09 §1`) is the game.

Failure that is graded, visible and recoverable is what P-iv asks for at the largest scale in the
game, and this is the one place where getting it wrong would be unrecoverable by construction.

---

## 7. Loops, stated rather than claimed

Three cycles run through this document. Each is named, each has its bound identified, and where the
gain is unmeasured that is said.

| loop | direction | bound | damper | gain |
|---|---|---|---|---|
| **fiscal** — treasury → actions → holdings → yield → treasury | positive | holdings bounded by the map; `compliance ≤ 1` | **yes, real**: extraction lowers acceptance, and low acceptance lowers compliance, which lowers yield | **unmeasured**; campaign-reachable, so a controlled run has two non-degenerate arms |
| **enmity** — grudge → hostile action → grudge | positive | tag dedupe bounds count | **yes, structural**: geometric decay on the gauge the tag value lands in | bounded by `rest + a/λ` for bounded accrual `a` |
| **post** — posts → actions → holdings → posts | positive | post count has a data-computable ceiling; plus `FACTION_ACTION_CEILING`, which does not scale with success | not established | **unmeasured** — see `03 §7` |

**Nothing here is claimed to be damped that has not been shown damped.** Two of the three have a
structural damper and one does not; saying so is more useful than a confident sentence in either
direction, and both unmeasured gains are measurable against a control before the writers that feed
them land.

### 7.1 The open hazard this suite does not resolve (Q-5)

If a down-distributed place delta overlaps the state the up-aggregate reads, one outcome is counted
twice — once as the write that feeds the aggregate on re-derivation, once as the modifier term. This
is flagged as high-priority and explicitly reserved for a ruling.

**What this suite does instead of resolving it:** every wrapper declares, per emission, which of its
two channels carries the magnitude, **and never both** (`01 §7`). That keeps the suite internally
disjoint by convention. It is not a resolution of the general question, and a design that later
routes a magnitude through both channels reintroduces the hazard regardless of what this paragraph
says.

---

## 8. Module contracts

```yaml
- module: fm.derive
  parent: faction_management
  scales: [peninsula]
  tier: null
  resolver: derivation
  remit: []
  budget: null
  consumes: []
  emits: []
  state:
    - {name: faction.acceptance, bucket: gauge, writable: false, owner: fm.derive}
    - {name: faction.treasury,   bucket: gauge, writable: false, owner: fm.derive}
    - {name: faction.force,      bucket: gauge, writable: false, owner: fm.derive}
    - {name: faction.weight,     bucket: gauge, writable: false, owner: fm.derive}
  disclosure:
    - {of: faction.acceptance, inputs: published, presentation: band,  trigger: hidden}
    - {of: faction.treasury,   inputs: published, presentation: exact, trigger: hidden}
    - {of: faction.force,      inputs: published, presentation: band,  trigger: hidden}
    - {of: faction.weight,     inputs: published, presentation: exact, trigger: hidden}

- module: fm.ledger
  parent: faction_management
  scales: [peninsula]
  tier: null
  resolver: derivation
  remit: []
  budget: null
  consumes:
    - {type: post.granted, from: [pm.appoint]}
    - {type: post.revoked, from: [pm.recall, pm.audit]}
  emits: []
  state:
    - {name: tag, bucket: tag, writable: true, owner: substrate.ledger}
  disclosure:
    - {of: tag, inputs: published, presentation: exact, trigger: hidden}

- module: fm.policy
  parent: faction_management
  scales: [peninsula]
  tier: null
  resolver: gate
  remit: [head]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: []
  state:
    - {name: policy, bucket: tag, writable: true, owner: fm.policy}
    - {name: acceptance.support, bucket: gauge, writable: true, owner: substrate.gauge}
  disclosure:
    - {of: policy, inputs: published, presentation: exact, trigger: hidden}
```

`writable: false` on all four derivations is the enforceable form of *no aggregate is ever written*.
A contract row declaring a derived value writable is a defect the shape check catches, without anyone
having to remember the rule.

`fm.derive` and `fm.ledger` have empty `remit` — they are not invocable. Nobody spends an action to
recompute a derivation, and nobody spends one to remember something.

---

## 9. Property audit

**Scope.** `fm.derive` and `fm.ledger` resolve nothing and are diagnosed on their loops and on P-iii;
**no N/R/S/E verdict is offered for them**. `fm.policy` is a gate. Nothing in this document rolls, and
manufacturing a resolution verdict for a set of derivations would be the error the methodology names.

| property | verdict | reasoning |
|---|---|---|
| **P-iii** bounded, monotonic | pass on two loops, **stated open on one** | Enmity is bounded structurally (dedupe on count, geometric decay on magnitude). The fiscal loop has a real negative feedback term in `compliance` and is bounded by the map. The post loop is bounded twice but its gain is unmeasured, and this document says so rather than asserting a damper |
| **P-v** right engine | pass | Everything here is a derivation or a threshold; nothing is uncertain, so nothing rolls. A faction's worth is a computation over state, and rolling for it would be a resolution where the answer already exists |
| **P-iv** (applied to collapse, the one graded output here) | pass | §6 — collapse is a staged, visible, recoverable degradation with no elimination branch. The one path to a faction ceasing to act is the gate, and the gate is recoverable at a node that cannot be lost |

**Necessary.** The four derivations each have a named consumer and no fifth is proposed. **Robust** —
tested at both extremes: a faction with no holdings still has weight from its posts and can still
produce a head; a faction with every holding is bounded by a flat action ceiling that does not scale
with its success. **Smooth** — a faction, a place and a person are the same four primitives at
different owners, and the derivation rule is identical at every scale. **Elegant** — three modules,
no elimination routine, no per-faction branch, and the interior falls out of posts rather than being
authored as a separate court system.
