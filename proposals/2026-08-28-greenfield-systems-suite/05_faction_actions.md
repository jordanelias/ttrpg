# 05 — Faction actions

> ⚠ **ARCHIVED / SUPERSEDED (2026-08-29).** This is the **pre-critique** version. It is retained
> unedited so the adversarial findings against it stay checkable — **do not build from it.** Six of
> its claims are known false; see [`ARCHIVED.md`](ARCHIVED.md). The live suite is
> `proposals/2026-08-29-greenfield-systems-suite-v2/`.


## Status: PROPOSED (2026-08-28) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) · [`04_personnel_management.md`](04_personnel_management.md)
## Executes: **ED-IN-0201** (Jordan, 2026-08-28) — both clauses

---

## 1. C1 — the gate

> *"We do not allow the game to perform faction actions if there is no leader of that faction."*

```yaml
module: fa.gate
resolver: gate
```

Before a faction's action phase runs:

```
head = post_of(faction, kind="head")
if head.holder_id is None:
    emit faction.action_declined(faction, reason="vacant_head")
    return                     # the faction takes no action this season
```

**It is a precondition, not a penalty.** Nothing resolves, no roll is made at a disadvantage, and no
stat is docked. The faction simply does not act, and a Key says so with a reason.

### 1.1 Why it emits rather than returning silently

There is no GM. A faction that stops acting with no visible cause is the single most confusing thing a
strategic layer can do to a player. `faction.action_declined` carries the reason, and under the
disclosure contract the reason is published. The player sees *the Crown took no action: no head.*

### 1.2 A closed gate is always recoverable

`fa.gate` closing raises a `post.vacant`, which raises a `cg.demand`, which is **total** (`02 §5`) —
so a head can always be produced. A faction cannot be permanently dead because generation failed.

⚠ **One dead-end this design closes deliberately.** The head post's demand resolves at the **faction's
own seat node**, which is a permanent property of the faction declared in the tier registry — *not* at
one of its holdings. A faction that has lost every holding can still produce a claimant to its own
headship. Without that, a faction reduced to zero territory has no node at which to generate, the head
post can never be filled, and the gate closes forever with no recovery — an elimination mechanism
nobody designed, arriving as a side effect of where generation is anchored.

---

## 2. The budget — actions, never dice

```
actions_this_season(faction)
    = min(  |posts held by this faction whose remit contains ≥1 action module|,
            FACTION_ACTION_CEILING  )
```

**Two bounds, and the second is independent of the first.**

The first is the ruling made mechanical: *factions hold people, and it is the number of people and
the weight of their positions that carry the value of that faction.* More filled posts is literally
more the faction can do in a season.

The second exists because the first is a positive feedback term. More actions buys more holdings,
which support more posts, which buy more actions. That cycle is bounded — post count has a ceiling
computable from the tier registry (`03 §3`) — but bounded is not the same as damped, and a bound that
scales with success is a weak one. `FACTION_ACTION_CEILING` is a flat cap that does not scale with
post count at all, which is the shape every mature franchise's anti-micromanagement guardrail takes,
and it is cheap now and expensive to retrofit.

**Its reachability bar is stated, because a cap that never binds is indistinguishable from no cap.**
The canonical failure of a well-motivated, legible mechanic tuned so its threshold is never reached is
that it becomes decorative while everyone assumes it is load-bearing. So: **the ceiling must bind for
the leading faction in a stated fraction of controlled campaigns.** If it does not, it is not
protecting the loop and should either be lowered or dropped — not left in place as reassurance.

### 2.1 The restriction that makes the budget safe

**One action point buys one attempt at one module. It never converts into a die and never into an
obstacle shift.** The arithmetic is in `01 §4.3`: a currency spendable as a modifier across two
engines with different leverage curves is worth roughly twice as much on a small pool as a large one,
and a player who notices routes it wherever it pays. Buying attempts keeps the budget out of the
resolution arithmetic entirely — which also means it is not a resolution object at all, and the
question of its leverage stops existing.

---

## 3. C2 — the decider, as a gate on the option set

> *"…that leader themselves is going to influence what choices are made for available faction actions
> in the same way that the person(s) who are governing a settlement or conducting a battle may make
> different choices with the same information and options."*

The ruling's own constraint is that this must **not** be a flat trait bonus on the selection roll: a
flat shift of size `X` is worth `X / (0.8·√Pool)` in σ-space, so a leader trait implemented as a bonus
would be worth systematically more to a weak faction than a strong one. Two mechanisms satisfy the
ruling without touching a roll.

### 3.1 The head's post changes *which actions exist*

The option set is `remit(head_post) ∩ available(world_state)`. A post kind's remit is declared data.
Two factions whose heads hold differently-typed head posts have different actions available — not
different odds on the same actions.

### 3.2 The head's convictions rank the option set

```
appeal(action) = Σ_axis  head.conviction_projection[axis] · action.symbolic_vector[axis]     # structural
               + Σ_signal  action.signal_weight[s] · signal(s, world)                        # structural
               + custody_bias(action)                                                        # relational, CAPPED
```

where the custody term is the controller's *own* appeal for that action, scaled by the leverage
they hold and **bounded by `RELATION_SHARE_MAX`** (`01 §2.4`):

```
custody_bias(action) = clamp( Σ_c  leverage(c) · appeal_structural(action | c),
                              ±RELATION_SHARE_MAX · structural_range )
```

The cap is not a nicety. An uncapped custody term makes controlling a head strictly better than being
one — the controller gets the decisions without the exposure — and it dissolves exactly the
positional conflicts that should be unbuyable. Custody biases; it never substitutes.

`symbolic_vector` projects the action onto the four canonical symbolic axes the Key substrate already
carries — hierarchical, sacred, instrumental, traditional — so an action's character is data on the
action, and a person's response to it is data on the person. The faction picks the highest-appeal
available action.

**Three properties this has and a probability model would not:**

- **It consumes no randomness.** Selection is a decision, not an uncertain outcome; putting a draw
  here would be the wrong tool and would also re-phase every downstream consumer for no gain.
- **It replaces faction personality entirely.** There is no per-faction branch anywhere in this suite.
  A faction's character is who holds its head post — which means the character changes when the
  holder does, which is the thing the ruling is actually asking for.
- **The state signals survive.** The world reads that inform the choice — is there a weak neighbour,
  is my military ahead, is my ground ungoverned — are the *information* the ruling says the leader
  decides with. They stay; what changes is that a person weighs them.

### 3.3 Disclosure

Each term of `appeal` is published **per available action as a band**: the player sees that their head
strongly favours a martial option on conviction, mildly disfavours a conciliatory one, and is under
some leverage from a rival. The resolved ordering's margin and the tie-break are not published.
Publish the reasons; never the trigger.

---

## 4. Resolution: one pool shape, one obstacle owner

Every action in this suite that rolls, rolls the same way.

| element | rule |
|---|---|
| **actor** | the post-holder invoking the module — never "the faction" |
| **pool** | `attr[a] + attr[b] + POOL_BASE`, where `[a, b]` is the module's declared attribute pair |
| **obstacle** | `derive_ob(target_score, target_modifiers)` — E-1 and nowhere else |
| **modifiers** | σ-space μ-shifts via `net_boost`; never obstacle shifts, never extra dice |
| **degree** | the single-owned margin ladder, unmodified |

### 4.1 The pool arithmetic, because P-v turns on it

Attributes are 1–7, so `attr[a] + attr[b]` spans 2–14 and the pool spans `2 + POOL_BASE` …
`14 + POOL_BASE`. With `POOL_BASE = 4` the pool spans **6–18**, which sits inside the band the
continuous engine is calibrated for at both ends: the floor is above the region where the Normal
model needs a continuity correction to stay faithful, and the ceiling is at the top of the calibrated
range rather than past it.

`POOL_BASE` is the one bare number in this document. It is declared in the exported params with that
justification attached, and its reachability bar is stated: **the weakest possible actor on the least
suited attribute pair must still produce a pool inside the calibrated band.** At `attr = 1, 1` that is
pool 6 — satisfied.

**This is also why the pool is one person's score and not an aggregate over a roster.** A roster-sized
pool grows `μ` linearly in roster size while `σ` grows only as `√size`, so `z` grows without ceiling
and the roll becomes decorative for a large faction — and it would put the same action on two
different engines depending on how many people a faction has. **The roster buys actions; it never
buys dice.** That is the same restriction as §2.1, reached from a different direction.

---

## 5. The action set — seven families, all data rows

An action is a row, never a branch. Adding one is a registry edit.

```yaml
- action: <id>
  remit_kinds: [<post kinds whose remit may contain this>]
  attrs: [<attr_a>, <attr_b>]
  target: <what supplies target_score for derive_ob>
  symbolic_vector: {hierarchical: ±, sacred: ±, instrumental: ±, traditional: ±}
  signal_weight: {<world signal>: <weight>}
  cost: {budget: 1, gauge_deposits: [...]}
  effects: {overwhelming: [...], success: [...], partial: [...], failure: [...]}
```

| family | what it does | shape | target of `derive_ob` |
|---|---|---|---|
| **`act.muster`** | raise a unit at a place (§6) | gate + accrual, or gate + cost | — |
| **`act.govern`** | deposit into a held place's `acceptance` and `condition` gauges | **U** | the place's own condition |
| **`act.campaign`** | declare a campaign against an adjacent holding (§5.1) | gate, then a declared seam | — |
| **`act.motion`** | raise a motion in the deliberative body **on a named subject** (`09 §3`) | **DO** | the opposing coalition |
| **`act.treat`** | offer a bilateral agreement, written as paired `Debt` tags with terms and an exit | **SO** | the counterparty's `acceptance` |
| **`act.commission`** | appoint, recall, or attempt custody — routes to `04` | gate / **SO** | per `04` |
| **`act.inquire`** | spend an action to learn (§7) | **U** | the concealing party's relevant score, where one exists |

### 5.1 `act.campaign` is a gate over a declared seam, not a stub

Force-on-force resolution is **out of this suite's scope**, and saying so with a specified seam is
different from leaving a hole. `act.campaign` owns everything on this side of the boundary and
nothing on the other:

| | |
|---|---|
| **the gate** (this suite) | the target is adjacent to a held node (`07 §7`); a `commander` post is filled (`09 §2.3`); the committed units exist and are assigned to the field |
| **the seam** | `resolve_force(attacker_units, defender_units, place) → Degree` — one call, one return, on the single-owned margin ladder |
| **the consumption** (this suite) | the degree drives an Entry Terms fork: on a lesser margin the taken place keeps its arrangements and seeds `acceptance.legitimacy` high; on a decisive one it does not and seeds low. Unit gauges take their deposits per `09 §2.5` |

**Two properties make this a seam rather than a stub.** Its interface is fully specified in both
directions, so the caller is complete and testable against a stand-in; and the seam returns a
`Degree`, which is the same currency every other action in this suite consumes — so whatever
implements it cannot introduce a second degree semantics for one event class, which is the divergence
the surveyed two-path franchise never fixed.

**Faction-unique actions are the same rows with a narrower `remit_kinds`.** A row invocable only by a
head post of a kind that only one faction's registry declares is unique to that faction, with no
branch anywhere and no stub module. A faction with no unique action has one fewer row available, not
a typed no-op.

### 5.2 Two constraints on every effects table

- **Total over the four bands.** Every action declares an outcome for Overwhelming, Success, Partial
  and Failure. No effect is unique to Partial, so a change to the Partial band's width degrades the
  ladder gracefully rather than deleting a mechanic (P0-3).
- **No Failure branch removes a post or eliminates a faction.** Failure deposits, writes tags and
  costs the budget point. Elimination is only ever the gate closing for want of a candidate, which is
  recoverable by producing one. An irreversible outcome on a routinely-reached roll is exactly what
  P-iv exists to catch, and a faction takes one of these every season.

---

## 6. `act.muster` — two economies, separated at birth

Four of four surveyed franchises implement the levy and the professional soldier as **different
economies, not different tiers**. The entitlement channel is rationed politically and temporally and
costs no treasury; the contract channel costs money to raise, carries upkeep even when idle, and
multiplies when fielded.

Building one muster now and splitting it later means splitting a mechanic that has already accreted
grounding, effects and goldens. Building two channels from the start costs one extra registry row.

| | **`act.muster.levy`** | **`act.muster.contract`** |
|---|---|---|
| pays with | the place's `accrual.entitlement` gauge | the faction's derived treasury |
| gated on | entitlement ≥ the unit's size cost | treasury ≥ price |
| rationed by | how fast entitlement accrues, which is a property of the place | how much money there is |
| upkeep | none | a recurring treasury deposit, larger when the unit is assigned to the field |
| quality | bounded by the place's `condition` band | bounded by price |
| consent cost | a deposit into the place's `acceptance.support`, **scaled by the unit's quality tier** | the same deposit, at the same scale |

### 6.1 Consent is charged per unit, and the floor is a separate, rare gate

Recruitment is a coercive act in both channels. The per-unit `acceptance.support` deposit is the live
mechanic that shapes every decision: raising better troops costs more consent per head, and quality
and consent move together rather than trading off.

Separately and rarely, a **gate**: a place whose `acceptance.support` band is at *revolt* does not
supply soldiers at all, in either channel. That is a different claim from *you govern badly here* —
which the per-unit cost already expresses — and scoping it to the revolt band is what keeps the two
from double-counting. It will fire seldom; it is the hard edge under a soft dial.

### 6.2 Muster does not raise an aggregate

`act.muster` produces a **unit record** (`09 §2`). It does not deposit into any faction-scale
military value, because faction-scale values have no setter: the faction's military weight is derived
from the units it holds. Building it the other way — mustering raising the number that gates what
mustering can produce — is a loop with no external term in it at all.

---

## 7. `act.inquire` — information gates, it does not add dice

Information gathered beforehand determining *which arguments you may attempt* is a mechanic one
surveyed title builds and this design wants. Its hard form — the wrong choice flatly fails — is a
special case bolted into a continuous system, which is scripting drift.

The soft form is already a built primitive. `dice_engine.BandExtension` declares a named policy whose
**only** power is to veto an Overwhelming; the ladder's single-owner test enrols every extension, and
the seam refuses undeclared context keys rather than swallowing them.

So: `act.inquire` deposits into an information gauge on the target. The gauge's band does two things
and no third:

1. **It gates the option set.** Actions declaring `requires_information: <band>` are unavailable below
   that band. That is a gate, on the board, published.
2. **Acting against a target you have not investigated declares a `BandExtension` that vetoes
   Overwhelming.** Your ceiling drops; your odds of Success are untouched.

Neither adds a die, shifts an obstacle, or touches the Partial or Failure boundaries. It is in-idiom,
uses machinery that already exists, and rewards the legwork a political game should reward.

---

## 8. Module contracts

```yaml
- module: fa.gate
  parent: faction_actions
  scales: [peninsula]
  tier: null
  resolver: gate
  remit: []
  budget: null
  consumes: [{type: post.vacant, from: [pm.vacancy]}]
  emits: [{type: faction.action_declined, terminal: true}]
  state: []
  disclosure: [{of: decline_reason, inputs: published, presentation: exact, trigger: hidden}]

- module: fa.select
  parent: faction_actions
  scales: [peninsula]
  tier: null
  resolver: derivation                 # a ranking over declared inputs; consumes no RNG
  remit: [head]
  budget: null
  consumes: []
  emits: []
  state: []
  disclosure: [{of: appeal, inputs: published, presentation: band, trigger: hidden}]

- module: fa.resolve
  parent: faction_actions
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: d_sigma
  remit: [head, minister, envoy, commander]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: []                            # the wrapper emits per the resolved action's row
  state:
    - {name: gauge, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag,   bucket: tag,   writable: true, owner: substrate.ledger}
  disclosure:
    - {of: pool,     inputs: published, presentation: exact, trigger: hidden}
    - {of: obstacle, inputs: published, presentation: exact, trigger: hidden}

- module: fa.muster
  parent: faction_actions
  scales: [settlement, territory]
  tier: settlement
  resolver: gate                       # entitlement or price is a threshold, not a contest
  remit: [head, commander]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: []
  state:
    - {name: accrual.entitlement,  bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: acceptance.support,   bucket: gauge, writable: true, owner: substrate.gauge}
  disclosure:
    - {of: accrual.entitlement, inputs: published, presentation: exact, trigger: hidden}
    - {of: acceptance.support,  inputs: published, presentation: band,  trigger: hidden}

- module: fa.inquire
  parent: faction_actions
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: d_sigma
  remit: [head, minister, envoy, clerk]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: []
  state:
    - {name: information, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: exposure,    bucket: gauge, writable: true, owner: substrate.gauge}
  disclosure:
    - {of: information, inputs: published, presentation: band, trigger: hidden}
```

`fa.muster` is a `gate`, not a `d_sigma`. Whether you can afford a unit is a budget decision whose
answer is on the board; rolling for it makes a determinate question uncertain, which is the
wrong-engine defect the precedent survey finds this tree most prone to — and it is most visible at
exactly this action.

---

## 9. Property audit

| property | verdict | reasoning |
|---|---|---|
| **P-i** legible odds | **pass, and it is the strongest in the suite.** Pool is a named person's two named attributes plus a declared constant; obstacle is the target's score halved. Both are published exactly. A player can read their chance off the board, and — because selection is a published ranking rather than a draw — can also read *why this action and not that one* |
| **P-ii** uniform leverage | pass | Every modifier is a σ-space μ-shift scaled by `σ_N`; nothing is a flat obstacle shift and nothing adds a die. The budget buys attempts, so it is not in the leverage question at all. Information gates and vetoes; it never scales |
| **P-iii** bounded, monotonic | pass, with the loop stated | Pools are bounded 6–18 by the attribute scale; obstacles are floored at `OB_MIN` so an advantage cannot create a cliff at the floor. The action-count loop (§2) is bounded twice — once by post count, which has a data-computable ceiling, and once by a flat ceiling that does not scale with success. **The per-cycle gain is unmeasured and is stated as unmeasured**; it is campaign-reachable and should be measured with a control before the facility writer that feeds it lands |
| **P-iv** graded, recoverable | pass | Every effects table is total over the four bands with nothing unique to Partial (§5.1), and no Failure branch removes a post or eliminates a faction. The gate is the only path to a faction ceasing to act, and it is recoverable by construction (§1.2) |
| **P-v** right engine | pass | Selection is a ranking over declared inputs — no draw, because the answer is a decision. Affordability is a gate. Contested outcomes roll on the continuous engine at pools inside its calibrated band (§4.1). Three questions, three tools |

**N** — under ED-IN-0201 this is the layer the ruling is about; it is not optional. No roll here is
redundant: every `d_sigma` module resolves something genuinely uncertain, and everything determinate
is a `gate`. **R** — the extremes are the weakest possible actor (pool 6, inside the band) and the
largest possible faction (action ceiling flat, pool unchanged because pools are person-scale).
**S** — the same pool shape, the same obstacle owner and the same four primitives as `04` and `08`;
a faction action and a settlement verb are the same object at different tiers. **E** — seven action
families, one contract shape, no per-faction branch anywhere in the design.
