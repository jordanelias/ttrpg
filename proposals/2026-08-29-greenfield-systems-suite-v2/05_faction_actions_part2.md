# 05 (part 2) — Faction actions: the action set, resolution, contracts and the audit

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`05_faction_actions.md`](05_faction_actions.md) — **part 1 first; this continues it**
## Part 1: §§0–4 (the playing surface, the per-tier gate, the per-post budget, `appeal`,
## `act.contest_influence`) — and the `## Overrides` block, which governs both parts
## Part 2: §§5–10 (the eight action rows, the resolution shape, the two effects constraints,
## J-N and J-O, the module contracts, the property audit)

---

## 5. The action set — eight rows, one shape

An action is a **row, never a branch.** Adding one is a registry edit.

```yaml
- action: <id>
  remit_kinds: [<post kinds whose remit may contain this>]
  tiers: [<rungs at which it is available>]              # NEW (v2) — §1.1
  binds: {<slot>: <registry id>}                          # NEW (v2) — §4.5
  attrs: [<attr_a>, <attr_b>]                             # keys on descriptors.ATTRIBUTES; never literal
  target: <what supplies target_score for derive_ob>
  ob_site: {target: <gauge id>, modifier_max: <int>, pool_max: <int>}   # NEW (v2) — 01 §6's
                                          # obstacle-reachability gate. `pool_max` is 18 for
                                          # every row by §6's pool shape; `modifier_max` is
                                          # the row's own ceiling on POSITIVE Ob modifiers
  symbolic_vector: {hierarchical: ±, sacred: ±, instrumental: ±, traditional: ±}
  signal_weight: {<world signal>: <weight>}
  cost: {budget: 1, gauge_deposits: [...]}
  effects: {overwhelming: [...], success: [...], partial: [...], failure: [...]}   # TOTAL over four
```

| family | what it does | shape | `derive_ob` target |
|---|---|---|---|
| **`act.muster`** | raise a unit at a place (§5.2) | **gate** | — |
| **`act.govern`** | deposit into a held place's `acceptance` and `condition` gauges | **U** | the place's own condition |
| **`act.campaign`** | declare a campaign against an adjacent holding (§5.1) | gate, then a declared seam | — |
| **`act.motion`** | raise a motion in the deliberative body on a named subject (`12`) | **DO** | the opposing coalition |
| **`act.treat`** | offer a bilateral agreement — **creates a `treaty` edge with its terms in its tags** (O-5.5; `12` owns the kind) | **SO** | the counterparty's `acceptance` |
| **`act.commission`** | appoint, recall, or attempt custody — routes to `04` | gate / **SO** | per `04` |
| **`act.inquire`** | spend an action to learn (§5.3) | **U** | the concealing party's relevant score, where one exists |
| **`act.contest_influence`** *(v2)* | raise presence at a place you do not hold (§4) | **DO + lead Ob** | the defending institution's presence **lead** over the challenger's (§4.1) |

### 5.1 `act.campaign` is a gate over a declared seam, not a stub

Force-on-force resolution is out of this suite's scope, and saying so **with a specified seam** is
different from leaving a hole.

| | |
|---|---|
| **the gate** (here) | the target is adjacent to a held node; a `commander` post is filled; the committed units exist and are assigned to the field |
| **the seam** | `resolve_force(attacker_units, defender_units, place) → Degree` — one call, one return, on the single-owned ladder |
| **the consumption** (here) | the degree drives an Entry Terms fork: on a lesser margin the taken place keeps its arrangements and seeds `acceptance.legitimacy` high; on a decisive one it does not and seeds low |

Its interface is fully specified in both directions, so the caller is complete and testable against a
stand-in, and the seam returns a `Degree` — the same currency every other action consumes — so whatever
implements it cannot introduce a second degree semantics for one event class.

### 5.2 `act.muster` — two economies, separated at birth

Four of four surveyed franchises implement the levy and the professional soldier as **different
economies, not different tiers.** Building one muster now and splitting it later means splitting a
mechanic that has already accreted grounding, effects and goldens; building two channels from the start
costs one extra registry row.

| | **`act.muster.levy`** | **`act.muster.contract`** |
|---|---|---|
| pays with | the place's `accrual.entitlement` gauge | the faction's derived treasury |
| rationed by | how fast entitlement accrues — a property of the place | how much money there is |
| upkeep | none | recurring, larger when assigned to the field |
| quality | bounded by the place's `condition` band | bounded by price |
| consent cost | a deposit into `acceptance.support`, scaled by the unit's quality tier | the same deposit at the same scale |

Recruitment is coercive in both channels: the per-unit consent deposit is the live dial, and separately
and rarely a **gate** — a place whose `acceptance.support` band is at *revolt* supplies no soldiers in
either channel. Scoping the gate to the revolt band is what keeps it from double-counting the dial.
`act.muster` is a **`gate`, not a `d_sigma`**: whether you can afford a unit is a question whose answer
is on the board, and rolling for it is the wrong-engine defect this tree is most prone to.

**Muster raises no aggregate.** It produces a unit record (`12`). Faction military weight is *derived*
from units held; building it the other way — mustering raising the number that gates what mustering can
produce — is a loop with no external term in it at all.

### 5.3 `act.inquire` — information **gates**, it never adds dice

Information determining *which arguments you may attempt* is a mechanic worth having; its hard form —
the wrong choice flatly fails — is a special case bolted into a continuous system, which is scripting
drift. The soft form is already a built primitive. `act.inquire` deposits into an information gauge on
the target, and that gauge's band does exactly two things:

1. **It gates the option set.** Rows declaring `requires_information: <band>` are unavailable below it —
   a gate, on the board, published.
2. **Acting against an uninvestigated target declares a `BandExtension` that vetoes Overwhelming**
   (`dice_engine.py:95`, ED-SC-0032). Your ceiling drops; your odds of Success are untouched.

Neither adds a die, shifts an obstacle, or touches the Partial or Failure boundaries. An extension's
only power is to veto the top band — the return channel is structurally bounded to `3 → 2` — and the
seam refuses undeclared context keys rather than swallowing them.

---

## 6. Resolution — one pool shape, one obstacle owner

Every action here that rolls, rolls the same way.

| element | rule |
|---|---|
| **actor** | the post-holder invoking the module — **never "the faction"** |
| **pool** | `attr[a] + attr[b] + POOL_BASE`, `[a, b]` the row's declared attribute pair, keyed on `descriptors.ATTRIBUTES` |
| **obstacle** | `derive_ob(target_score, target_modifiers)` — E-1 and nowhere else. **In the DO shape, the differential is the `net` and the entrenchment is the `ob`** (§4.1) |
| **modifiers** | σ-space μ-shifts via `sigma_leverage.net_boost`; never extra dice. **One exception, argued and listed at O-5.7:** a *contested* quantity's obstacle derives from the lead, inside `derive_ob` (§4.1) |
| **degree** | `degree_from_net`, unmodified, with an extension only where §5.3 declares one |
| **TN** | never named. `_require_tn7` raises (`dice_engine.py:182`) |

**The pool arithmetic, because P-v turns on it.** Attributes are 1–7, so `attr[a] + attr[b]` spans 2–14
and the pool spans `2 + POOL_BASE … 14 + POOL_BASE`. With `POOL_BASE = 4` — **a shape proposal, the one
bare number on this page, declared in the exported params with this justification attached** — the pool
spans **6–18**, inside the band the continuous engine is calibrated for at both ends. Reachability bar:
*the weakest possible actor on the least-suited pair must still produce a pool inside the calibrated
band.* At `attr = 1, 1` that is pool 6 — satisfied.

**This is also why the pool is one person's score and never an aggregate over a roster.** A
roster-sized pool grows `μ` linearly in roster size while `σ` grows only as `√size`, so `z` grows
without ceiling and the roll becomes decorative for a large faction — and it would put the same action
on two different engines depending on how many people a faction has. **The roster buys actions; it
never buys dice.** That is §2.4's restriction reached from a different direction.

---

## 7. Two constraints binding on every effects table

- **Total over the four bands.** Every action declares an outcome for Overwhelming, Success, Partial and
  Failure, and **no effect is unique to Partial** (P0-3), so a change to the Partial band's width
  degrades the ladder gracefully rather than deleting a mechanic.
- **No Failure branch removes a post or eliminates a faction.** Failure deposits, writes tags and costs
  the budget point. Elimination is only ever the gate closing for want of a candidate, and that is
  recoverable by producing one (§1.2). An irreversible outcome on a routinely-reached roll is exactly
  what P-iv exists to catch, **and a faction takes one of these every season, at every rung.** The
  per-tier gate makes this *more* load-bearing than in v1, not less: there are now more of these rolls
  per season, so a single irreversible branch would fire that much sooner.

---

## 8. What this page assumes about the substrate — J-N and J-O, stated once each

### 8.1 ⚠ J-N — the substrate supplies NO cross-season latency

Verified against the tree by `audit/2026-08-08-world-churn-audit` and reproduced at `01 part 2 §9.3`:
`drain_tick` has zero production callers, `next_tick` **raises `TerminationBreach`** on a non-empty
queue, and `DEFAULT_CASCADE_DEPTH_MAX = 0` is a self-labelled provisional bound. **The guard prevents
cascades outright; it does not schedule them late.** One-hop-per-season latency is not a property this
design has — it is a mechanism someone would have to build.

**What that forbids on this page, concretely:**

| forbidden | the correct shape |
|---|---|
| a contest that "posts a challenge" resolving next season | it resolves **within the tick**, or not at all |
| a multi-season influence campaign carried by an emission | it advances because **presence is a certain way at the accounting boundary** — a gauge read, not a message |
| `fa.gate` reacting next season to a `post.vacant` raised this season | the gate **reads `holder_id`** at the boundary; it does not wait to be told |
| an action whose consequence "arrives later" | its deposits land now and **decay geometrically**, which is the only cross-season channel the substrate has besides reading state |

**J-N is the ruling that would change this.** If it rules for reactive chains, this section is what to
revisit; nothing else on this page depends on the answer.

### 8.2 ⚠ J-O — what here leans on Key *consumption*

`00 §5.1` files J-O: whether the Key substrate deserves promotion from telemetry spine to churn engine
at all, the alternative being an append-only telemetry/causality log with churn driven at the boundary
directly. **Stated so the affected parts stay identifiable if J-O rules the other way:**

| depends on Key **consumption** | survives a "telemetry only" ruling? |
|---|---|
| `fa.gate`'s `consumes: [post.vacant]` | **no** — it becomes a boundary read of `holder_id`, which is what §8.1 says it already is in substance. **One line of contract, no design change** |
| everything else on this page — `appeal` (reads state), the budget (reads a gauge), `act.contest_influence` (reads presence, rolls, deposits), every effects table | **yes** |
| the emission side (`faction.action_declined`, and the action rows' own emissions through the herald) | **yes** as a log |

**This page is nearly robust to J-O**, and deliberately so: the per-tier gate was written as a *state
read* rather than a *Key reaction* precisely because §8.1 says the transport for the latter does not
exist. That is one constraint doing two jobs.

---

## 9. Module contracts

Shape per `00 §7`. Per W-6, every `consumes:` row names what the consumer does with the Key; none is
declared speculatively.

```yaml
- module: fa.gate
  parent: faction_actions
  class: substrate
  scales: [settlement, territory, peninsula]     # v2: no longer [peninsula] — O-5.1
  tier: null                                     # runs at EVERY declared rung; §1.1
  resolver: gate
  remit: []                                      # not invocable; the boundary runs it
  budget: null
  consumes: [{type: post.vacant, from: [pm.vacancy]}]   # rule content: re-evaluates the rung's
                                                        # acting_posts set. See §8.2 — this is the
                                                        # ONE J-O-fragile row on the page.
  emits: [{type: faction.action_declined, terminal: true}]   # carries faction, tier, reason
  state: []
  form: []
  transitions: []
  disclosure: [{of: decline_reason, inputs: published, presentation: exact, trigger: hidden}]

- module: fa.select
  parent: faction_actions
  class: substrate                               # the RANKING is substrate; the player's pick is 10's
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: derivation                           # a ranking over declared inputs; consumes no RNG
  remit: [head, governor, minister, commander, envoy]
  budget: null
  consumes: []
  emits: []
  state: []
  form: []
  transitions: []
  disclosure: [{of: appeal, inputs: published, presentation: band, trigger: hidden}]

- module: fa.resolve
  parent: faction_actions
  class: substrate
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: d_sigma
  remit: [head, governor, minister, envoy, commander]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  ob_sites: []            # DELIBERATELY EMPTY. fa.resolve is a dispatcher: the obstacle's target is
                          # the RESOLVED ROW's `target`, so each action row carries its own `ob_site`
                          # (§5) and 01 §6's gate evaluates rows, not this module. Declaring a site
                          # here would name a target this module does not have.
  emits: []                                      # the herald emits per the resolved row (W-1)
  state:
    - {name: gauge, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag,   bucket: tag,   writable: true, owner: substrate.ledger}
  form: []
  transitions: []
  disclosure:
    - {of: pool,     inputs: published, presentation: exact, trigger: hidden}
    - {of: obstacle, inputs: published, presentation: exact, trigger: hidden}

- module: fa.contest_influence                   # NEW (v2)
  parent: faction_actions
  class: substrate
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: d_sigma                              # DO; the UNDEFENDED path is a gate, §4.2
  remit: [head, governor, minister, envoy]
  budget: {gauge: post.budget, cost: 1}
  consumes: []                                   # reads presence at the boundary; §8.1
  ob_sites:                                      # NEW — 01 §6's obstacle-reachability gate. §4.1a
    - target: presence.<institution>             #   ceiling UNDECLARED (07's) -> site UNVERIFIABLE
      modifier_max: 2                            #   positive `place_terms` only; the challenger's
                                                 #   lead term is strictly non-positive (O-5.7) and
                                                 #   so cannot threaten band reachability
      pool_max: 18                               #   §6: attr 1-7 twice + POOL_BASE 4. Site-local.
      shape: DO                                  #   ⚠ the gate must use the DIFFERENTIAL's moments,
                                                 #   mu=0.4(Nc-Nd), sigma=0.8*sqrt(Nc+Nd) -- STRICTER
                                                 #   than one-sided (Ob<=8.247 vs 9.783). §4.1a
  emits: []                                      # the herald emits; a band crossing is 07's
                                                 # form.transitioned, not a second emission here
  state:
    - {name: presence.<institution>, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: exposure,               bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag,                    bucket: tag,   writable: true, owner: substrate.ledger}
  form: []                                       # 07 owns place.presences transitions, NOT this module
  transitions: []
  disclosure:
    - {of: presence.<institution>, inputs: published, presentation: band,  trigger: hidden}
    - {of: pool,                   inputs: published, presentation: exact, trigger: hidden}
    - {of: obstacle,               inputs: published, presentation: exact, trigger: hidden}

- module: fa.muster
  parent: faction_actions
  class: substrate
  scales: [settlement, territory]
  tier: settlement
  resolver: gate                                 # affordability is a threshold, not a contest
  remit: [head, governor, commander]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: []
  state:
    - {name: accrual.entitlement, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: acceptance.support,  bucket: gauge, writable: true, owner: substrate.gauge}
  form: []
  transitions: []
  disclosure:
    - {of: accrual.entitlement, inputs: published, presentation: exact, trigger: hidden}
    - {of: acceptance.support,  inputs: published, presentation: band,  trigger: hidden}

- module: fa.inquire
  parent: faction_actions
  class: substrate
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: d_sigma
  remit: [head, governor, minister, envoy, clerk]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  ob_sites: []            # DELIBERATELY EMPTY, and NOT because there is no site. fa.inquire rolls
                          # against "the concealing party's relevant score, WHERE ONE EXISTS" (§5.3)
                          # -- the target is row-declared and, for some rows, absent. Each row that
                          # declares a target declares its own `ob_site`; a row with no target does
                          # not roll. Naming a single target here would fabricate one.
  emits: []
  state:
    - {name: information, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: exposure,    bucket: gauge, writable: true, owner: substrate.gauge}
  form: []
  transitions: []
  disclosure: [{of: information, inputs: published, presentation: band, trigger: hidden}]
```

**Note what is absent.** No module here declares `form:` or `transitions:` — **this page changes no
entity's shape.** Presence band crossings are `07`'s transition rows, posture is `06`'s, and appointment
is `04`'s. A faction action deposits, tags and spends; it does not reshape the world directly. That
absence is `01 §2.4`'s "grep over one field" staying true, expressed in the contracts rather than
promised in prose.

---

## 10. Property audit

**Scope, honestly.** `fa.gate` and `fa.muster` are **gates**; `fa.select` is a **derivation**. `00 §10`
and the methodology's own rule forbid manufacturing a NERS verdict for a module that does not roll, so
**no N/R/S/E verdict is offered for those three** — their loops and gates are §10.2 instead. The audit
below is of `fa.resolve`, `fa.contest_influence` and `fa.inquire`, which roll.

### 10.1 The properties, each with the falsifier that would show it wrong

| property | verdict | falsifier |
|---|---|---|
| **P-i** legible odds | **pass, and still the strongest in the suite.** Pool is a named person's two named attributes plus a declared constant; obstacle is the target's score halved; **the DO differential is two published nets minus a published obstacle.** Selection is a published ranking rather than a draw, so a player can read *why this action and not that one* | A test asserting every rolling module's `disclosure:` publishes `pool` and `obstacle` at `exact`, and that `fa.select` publishes every `appeal` term. **If any input to a roll or a ranking is unpublished, P-i is false** |
| **P-ii** uniform leverage | pass, **with one recorded non-uniformity in the correct direction** (§4.1) | A test asserting no module contract declares a `budget:` whose cost is consumed inside a pool or obstacle expression (`01 §5.3`'s falsifier, applied here), **plus**: no action row's modifier reaches the roll except through `sigma_leverage.net_boost` **or** `derive_ob`'s declared instance term, and no row declares both for the same quantity. A modifier applied twice through two channels — the defect the two-channel draft of §4.1 would have shipped — falsifies it |
| **P-iii** bounded, monotonic | pass, **with two loops stated and both gains unmeasured** (§2.3, §4.4) | `01 §5.1`'s declaration-time check — `rest + max_seasonal_accrual/λ ≤ ceiling` — applied to `presence.<institution>` with `act.contest_influence` counted among its depositors. **A controlled campaign pair on `tools/balance_oracle.py` showing presence share diverging without bound falsifies it** |
| **P-iv** graded, recoverable | pass | A test asserting every action row's `effects` map is **total over the four `Degree` members** and that **no `failure` branch revokes a post or removes a faction**. A row with a Partial-only effect, or an empty Failure branch, falsifies it |
| **P-vi** *(new)* **reachable bands** | ⚠ **UNVERIFIABLE for `act.contest_influence`; declared for the rest** | `01 §6`'s obstacle-reachability gate: `derive_ob(S_max, M_max) + 3 ≤ 0.4·N_max + z·0.8·√N_max`, `z = 1.645`, **per site**, evaluated for a DO site on the differential's moments (§4.1a). The test that would show this site wrong: **assert the top band is reachable at the site's most favourable configuration** — at `N_c = 18` against `N_d = 6` the envelope is `11.247`, so `derive_ob(presence_ceiling, 2) ≤ 8.247`, which requires `presence.<institution>`'s ceiling `≤ 12`. **It cannot be run today**: that ceiling is `07`'s and is undeclared, and an undeclared ceiling is not a passing one. The worked failure the gate exists to catch is real and in this tree — a 0–100 gauge yields `P(Overwhelming) = 0` |
| **P-v** right engine | pass | Three questions, three tools: selection is a **derivation** (a decision, not an uncertainty); affordability and eligibility are **gates**; contested outcomes are `d_sigma` at pools 6–18. **A test asserting every `resolver:` matches `00 §7`'s table** — in particular that nothing determinate rolls. `fa.muster` declared `d_sigma` would falsify it |

**N** — under ED-IN-0201 this is the layer the ruling is *about*; it is not optional. No roll here is
redundant: every `d_sigma` module resolves something genuinely uncertain and everything determinate is a
`gate`. **R** — the extremes are the weakest possible actor (pool 6, inside the calibrated band) and the
largest possible faction (flat ceiling; pool unchanged, because pools are person-scale at every rung).
**S** — the same pool shape, the same obstacle owner and the same four primitives as `04` and `08`; **a
faction action at the peninsula rung and a settlement verb are the same object at different rungs**, which
is what per-tier makes literally true rather than merely analogous. **E** — eight rows, one contract
shape, **no per-faction branch anywhere**, and five would-be verbs collapsed into one binding slot (§4.5).

### 10.2 The non-rolling modules — loops, gates, and what each reads

| module | kind | reads | bound |
|---|---|---|---|
| `fa.gate` | gate | `post.holder_id`, `post.remit`, the declared rungs | none needed; it is a predicate. **Recoverable by construction** (§1.2) |
| `fa.select` | derivation | `faction.identity.ethos`, holder convictions, world signals, `Leverage` tags | `custody_bias` clamped to `±RELATION_SHARE_MAX · structural_range`; no other term is unbounded because each is a bounded projection |
| `fa.muster` | gate | `accrual.entitlement`, treasury, `acceptance.support` band | the entitlement accrual rate is a property of the place; the revolt gate is a hard floor |
| the budget | derivation over gauges | `post.budget` per held post | `FACTION_ACTION_CEILING`, flat and non-scaling (§2.2), **with a stated reachability bar** |

### 10.3 The four claims across both parts that are weakest, named rather than buried

1. **`FACTION_ACTION_CEILING`, `POOL_BASE`, `SHORTLIST_K`, `d₁…d₃` and `e₁…e₂` are
   shape proposals, not ledger constants.** None is cited to a `PP-NNN` or an `ED-NNN`, because none has
   one. They are declared with justifications and reachability bars so that tuning them is an act with a
   named target, not a preference.
2. **Both loops' per-cycle gains are unmeasured** (§2.3, §4.4) and are stated as unmeasured. They are
   campaign-reachable, so the instrument exists; running it with a control is work this page does not do.
3. **The DO-plus-lead-obstacle shape is the page's most contestable design call** (§4.1). It is argued,
   listed at O-5.4 and O-5.7, and each half is *reversible in one line*: dropping `net_d` from the
   differential returns the SO the delta spec named, and dropping the negative instance term returns the
   absolute-presence obstacle — with every other part of the action unchanged either way.
4. **`act.contest_influence` depends on a gauge ceiling that does not exist yet, and the dependency is
   now exact rather than general.** `01 §6`'s gate is built; this site declares `pool_max: 18` and
   `modifier_max: 2`; the third field, `presence.<institution>`'s ceiling, is `07`'s and is undeclared.
   The constraint handed to `07` is **`ceiling ≤ 12`** (§4.1a). Until it lands the site's status is
   **unverifiable, not passing** — picking a ceiling here to turn the row green would be exactly the
   confounded measurement `CLAUDE.md §0.1` was written about. **This page's own first form of that gate
   was wrong** (2.57× too permissive at pool 5), which is the strongest argument available that the
   check belongs at one owner and not restated per document.
