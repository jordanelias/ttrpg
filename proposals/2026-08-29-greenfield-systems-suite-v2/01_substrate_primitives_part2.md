# 01 (part 2) — Substrate: disclosure, the herald, the contracts and the audit

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`01_substrate_primitives.md`](01_substrate_primitives.md) — **part 1 first; this continues it**
## Part 1: §§1–8 (the four primitives, form transitions, `derive_ob`, edges and the Knot, disclosure)
## Part 2: §§9–13 (the herald, the cut list, the player surface, the module contracts, the audit)

Section numbering continues from part 1 without a break, and every `§n` cross-reference resolves across
both parts. Split under `CLAUDE.md` §4's sequential-parts rule (`_part2` in reading order, never
index+infill) because the single file exceeded the 15k-token compliance cap.

**Everything in this part is `substrate`** in the sense of `00 §2.1`. §11 is the whole player-facing
surface of both parts, and it is three read-only affordances and zero verbs.

## 9. The herald — one per subsystem, populating `targets[]`

### 9.1 Why this is not the prohibited "world director"

Part VI's strongest negative (`06_master_synthesis.md:551`, **held not ratified**) is *"a distributor
wrapper or 'world director'. Distribution is `targets[]` data plus subscription; a router module is the
god-loop with better PR."* Part III of the same document answers the wrapper-vs-mesh fork and **refutes
both pure forms**, leaving one criterion (`:394`):

> **Aggregate-crossing detection belongs to the aggregator; effect magnitude belongs to the effect's
> owner.**

**This suite adopts that criterion and reframes the wrapper to it rather than defending the wrapper.**

1. **The boundary is a herald.** It publishes what it **already computes**. It decides nothing and
   routes nothing. A per-subsystem herald is not a central router because there is no central one: each
   sees only Keys addressed to its own modules, holds no map of other subsystems, and cannot reach one —
   cross-subsystem needs go through `composition.require(role)` (W-2), a registry lookup, not a dispatch
   table.
2. **Every effect rule stays local.** Whether a fact scars a person depends on that person's convictions;
   whether a place complies depends on its own acceptance. **The herald computes no effect magnitude and
   never holds a rule belonging to a receiver** — the property that separates it from a director.
3. **Distribution is data, not code.** The router a wrapper would centralise **already exists as
   schema**: the five-role `targets[]` vocabulary. **One Key whose `targets[]` names every affected place
   *is* the distribution mechanism.** v1's W-3 was already exactly this; what changes is that it is now
   the herald's *definition* rather than one of its rules.

**So the herald's whole job is: drain, invoke, populate `targets[]`.** If a future version of this
document describes it as routing, deciding, or holding a receiver's rule, that version has built the
prohibited thing, and this paragraph is the falsifier.

### 9.2 Shape and rules

```
engine_clock.run_tick →  SEASON_TICK ── ACTION ── ACCOUNTING_BOUNDARY
   subsystem herald (resolved by composition role, never imported)
     in:   drain the Keys addressed to this subsystem's modules
     run:  invoke modules; modules touch primitives and NOTHING else
     out:  publish at most one Key per resolved module, causes[] cited honestly,
           targets[] populated at the granularity of each receiver
```

| # | Rule | The failure it prevents |
|---|---|---|
| W-1 | A module never publishes. It returns a result; the herald publishes. | Emission scattered across a subsystem is how `causes[]` chains get fabricated or dropped |
| W-2 | A module never imports another subsystem; needs resolve through `composition.require(role)`. | The package cycle a function-local import hides from the interpreter without removing |
| W-3 | Fan-out is **one Key with N populated targets, never N Keys** — this *is* the distribution mechanism. | The re-entrancy meter counts *responses*, not target-array width, so wide legitimate delivery must not look like runaway |
| W-4 | Any Key naming a derived aggregate in `targets[]` carries `stat_deltas: {}` for that target. | Writing an aggregate, which the write rule forbids and the generic per-observer path would do silently |
| **W-5** *(v2)* | A module's result may *name* a form transition; the herald applies it and publishes `form.transitioned`. A module never mutates `form`. | Otherwise the fourth write leaf is the one leaf with no single owner, and §2.4's "grep over one field" stops being true |
| **W-6** *(v2)* | **A subscription with no rule content is not declared.** A `consumes:` row must name what the consumer *does* with the Key. | Part VI `:412` — *"a subscription with no rule content is decoration"*, and it is how a `consumes:` list becomes a fiction nobody executes |

**Populating `targets[]` is where granularity increases.** A peninsula-scale Key addressed to eight
places carries eight entries, each with the deltas *that place* receives — not one delta the receiver
must interpret. A sparse `targets[]` delivers blind, the documented failure of the eight declared
down-seams that populate nothing. ⚠ **The double-count hazard is open** (`00` Q-5): every herald here
declares, per emission, **which of its two channels carries the magnitude — and never both.**

### 9.3 ⚠ The substrate supplies NO LATENCY — binding on everything downstream

Verified against the tree by that audit's adversarial review, **filed as open ruling J-N**
(`06_master_synthesis.md:532`, `:637`): `schedule_emission` increments depth **only when already
draining**; `drain_tick` has **zero production callers**; the live loop calls `accounting_boundary()`
then `next_tick()` directly; **`next_tick` raises `TerminationBreach` if the queue is non-empty**, so
there is **no cross-season carry**; and `DEFAULT_CASCADE_DEPTH_MAX = 0` is a **provisional** safety
bound, self-labelled, sized to the single current emitter.

> **The guard prevents cascades outright; it does not schedule them late.** One-hop-per-season latency
> is **not a property this design has** — it is a mechanism someone would have to build.

| forbidden | the correct shape |
|---|---|
| a module reacting to a Key by publishing a Key that **lands next season** | there is no such transport |
| a transition, project or event designed as "posted to, fires later" | it **reads state at the boundary** and fires because the world *is* a certain way |
| describing the herald as providing propagation over time | it propagates **within a tick**, and nothing else |

**Anything spanning seasons does so by reading state, never by carrying an emission.** That is why every
gauge decays on a *pure function of elapsed time* (§5.1) and every form gate reads current state (§2.2):
those are the only two cross-season channels the substrate actually has. **J-N is the ruling that would
change this**, and if it rules for reactive chains, this section is what to revisit.

### 9.4 ⚠ This page leans on Key consumption — J-O

`06_master_synthesis.md:533` files **J-O**: *does the Key mesh deserve promotion from telemetry spine to
churn engine at all*, the alternative being **Keys as an append-only telemetry and causality log with
churn driven at the boundary directly** — an alternative the audit records as *"never weighed anywhere"*,
and one that can invalidate a whole programme rather than one item. Stated so the affected parts are
identifiable:

| depends on Key **consumption** | survives a "telemetry only" ruling? |
|---|---|
| `consumes:` rows in every module contract; the herald's `in:` drain | **no** — these become boundary reads |
| `causes[]` as the provenance chain, and `Tag.provenance` pointing at a Key | **yes** — that is telemetry and causality, which the alternative keeps |
| every **form transition** (gated on *state*, not on a received Key) and every **gauge** deposit and decay | **yes** |
| the emission side (`form.transitioned`, `edge.formed`, …) | **yes** as a log; only the *reaction* half is at risk |

**The substrate is robust to J-O; the module wiring is not.** Four primitives, four write leaves and the
decay law would all survive a ruling that retires the consumer mesh; §12's `consumes:` lists would be
rewritten as boundary reads. **J-O is not resolved here and this suite takes no position on it.**

---

## 10. What is deliberately not a primitive, and what was cut

A cut list is only credible next to what it refuses to add — and under *"may the best ideas win"* it
must also record what was cut because something on disk beat it.

| Considered | Verdict | Why |
|---|---|---|
| a separate **Accrual** or **Standing/rank** primitive | folded into Gauge | an accrual is a gauge with a positive rest and a rate; a budget is an accrual with a spender; a rank ladder is a bounded meter with bands. Keeping them separate produced nine parallel meters and three rival clocks |
| `custodian_id` as a **field on Post** | folded into Tag | §4.2 — a field carries less (no ttl, no provenance, no decay) at the same conceptual cost |
| a **role** string on Person | rejected | §1.4 — `posts` is derived; there is no field to collide in |
| a **Compact** tag family | rejected | a recurring term-limited claim is `Debt(recurs=True, ttl=term)` |
| a **Knot** primitive | rejected | §7.5 — an edge with its own registry row, its own gates and its own private strain gauge. A sixth stored kind for one canon mechanic is how a substrate stops being one |
| **a v2-invented relation taxonomy** | **CUT, superseded by PP-724** | §7.2. Six period-grounded types with per-type semantics and a decision log already exist on disk. Rebuilding a worse one to keep authorship is the elegance failure, whoever wrote it |
| a **`client`** relation kind | rejected | §7.2 — a reading direction, not a row |
| a **stored NPC↔NPC disposition** | **CUT** | §7.3 — an aggregate over edge strengths, and no aggregate is ever written. v1 violated its own rule; PP-724 caught it |
| a **Memory** primitive | rejected; it is a **Tag kind** | §3.1 — a primitive would need its own store, sweep and provenance rule, all of which Tag already has |
| a **salience** stored field, or a **second decay law** | rejected | §3.2 — derived at read from `value`, `created_season` and one declared `λ_mem` |
| a **cross-season emission carry** | **rejected as non-existent, not as unwanted** | §9.3 — the transport is not in the tree; designing on it would be designing on a mechanism nobody built (**J-N**) |
| a **second resolver** | rejected | the only surveyed franchise with two resolution paths is also the only one with a two-decade unfixed divergence, exploited in both directions |
| a **view** primitive | rejected | disclosure stores nothing and resolves nothing; it is a declaration attached to state (E-2), which is what makes it checkable |
| a **central distributor / world director** | rejected, and the wrapper reframed | §9.1 — the herald populates `targets[]` and holds no receiver's rule |

---

## 11. What the player actually touches at this layer

**Almost nothing, and that is the design** (`00 §2`). This document is the richest layer in the suite
and the thinnest surface. Everything below is **read-only**; the substrate exposes **zero verbs**.

| what the player touches | how it reaches them | how often |
|---|---|---|
| a gauge's **band** — never its number | `gauge_band`, on a Slate item or a place summary | whenever the item they chose is on screen |
| the **posts they hold**, their remit and remaining **budget** — disclosed `exact`, because these are inputs to a decision they are making now | the post list | once a season |
| a tag's **existence and provenance** — *why did this actor turn on me* | inspection from a Slate item | on demand, never pushed |

| what the player never touches |
|---|
| creating, editing or deleting an **entity**, an **edge** or a **bloc** |
| firing a **form transition**, or running a **converter** — a marriage becoming a treaty is something they *learn about* |
| appending a **tag** or depositing into a **gauge** directly |
| a gauge's exact **value**, any transition's **threshold**, or any **forecast** of either (§8) |
| **strain**, **salience**, **divergence**, **presence levels** — substrate, surfaced only as a situation |

**Substrate objects here: 6 entity kinds · 6 tag kinds · 6 adopted relation kinds + 2 scope extensions +
Knot held separately · 3 converters · 4 primitives · 2 extensions. Surface affordances: 3 reads, 0
verbs.** If a later document's surface table is longer than its substrate table, that document has the
ratio backwards.

---

## 12. Module contracts — the substrate's own

Per W-6, every `consumes:` row names what the consumer does with the Key; the substrate's own modules
consume nothing, and none is declared speculatively. Three pure stores share one shape and are given
once rather than three times.

```yaml
# substrate.entity | substrate.ledger | substrate.gauge — the three pure stores.
# Identical but for the row marked *; all: parent: substrate · class: substrate · remit: [] (not
# invocable) · budget: null · consumes: [] · form: [] · transitions: [] · scales: all four · tier: null
- module: substrate.entity
  resolver: derivation
  emits: [{type: person.generated, terminal: false}]
  state: [{name: entity, bucket: entity, writable: false, owner: substrate.entity}]      # *
  disclosure: [{of: entity, inputs: published, presentation: exact, trigger: hidden}]
- module: substrate.ledger
  resolver: derivation      emits: []
  state: [{name: tag, bucket: tag, writable: true, owner: substrate.ledger}]             # *
  disclosure: [{of: tag, inputs: published, presentation: exact, trigger: hidden}]
- module: substrate.gauge
  resolver: accrual         emits: []
  state: [{name: gauge, bucket: gauge, writable: true, owner: substrate.gauge}]          # *
  disclosure: [{of: gauge, inputs: published, presentation: band, trigger: hidden}]

- module: substrate.form
  parent: substrate         class: substrate
  scales: [personal, settlement, territory, peninsula]      tier: null
  resolver: gate            # every transition is a gate; §2.2
  remit: []                 # applied by the herald (W-5), never invoked by a post
  budget: null
  consumes: []              # gates read STATE, never a received Key (§9.3)
  emits: [{type: form.transitioned, terminal: false}]       # a crossing FACT, never a forecast
  state: [{name: form, bucket: entity, writable: true, owner: substrate.form}]
  form:
    - {entity_kind: person,  field: life_stage}     - {entity_kind: person,  field: capability}
    - {entity_kind: person,  field: traits}         - {entity_kind: place,   field: kind}
    - {entity_kind: place,   field: tier}           - {entity_kind: place,   field: facilities}
    - {entity_kind: place,   field: presences}      - {entity_kind: faction, field: posture}
    - {entity_kind: edge,    field: state}          - {entity_kind: edge,    field: tier}  # knot only
    - {entity_kind: unit,    field: unit_kind}      - {entity_kind: unit,    field: assignment}
    - {entity_kind: bloc,    field: members}        - {entity_kind: bloc,    field: state}
  transitions: [ALL declared rows in references/form_registry.yaml]
  disclosure: [{of: form, inputs: published, presentation: exact, trigger: hidden}]

# ONE container, PER-KIND semantics. Everything below that varies by kind is declared in the KIND's
# own registry row, never here. §7.3.
- module: substrate.edge
  parent: substrate         class: substrate
  scales: [personal, settlement, territory, peninsula]      tier: null
  resolver: gate            remit: []        budget: null      consumes: []
  emits: [{type: edge.formed, terminal: false}, {type: edge.transitioned, terminal: false}]
  state:
    # strain is declared PER KIND; a kind with no strain axis (kinship, PP-724 :334) has none, and no
    # two kinds' strain ever sums into one counter (PP-724 :162).
    - {name: edge.strain.<kind>, bucket: gauge, writable: true, owner: substrate.edge}
    # PC<->NPC disposition is STORED (canon's track). NPC<->NPC disposition is DERIVED from edge state
    # and is deliberately NOT a state row here (PP-724 :331-345; O-3).
    - {name: edge.disposition.pc_npc, bucket: gauge, writable: true, owner: substrate.edge}
  form: [{entity_kind: edge, field: state}, {entity_kind: edge, field: tier}]
  transitions:
    - knot.intact_to_ruptured     # gate: strain >= 5; reversible: false      (knots_v30 :180)
    - knot.intact_to_tempered     # gate: strain <= -5, Close only            (knots_v30 :54)
    - knot.tempered_to_intact     # reversible pair -> hysteresis REQUIRED; band UNSTATED in canon
    - kinship.cooperative_to_strained
    - kinship.to_severed          # institutional act, not strain            (PP-724 :334-340)
    - patronage.to_sworn_bond     # converter: retainer_ripening             (§7.4)
    - kinship.to_treaty           # converter: marriage_to_treaty            (§7.4)
    - rivalry.to_feud             # converter: PP-724 §2.6 escalation        (§7.4)
  disclosure:
    - {of: edge.strain.<kind>, inputs: published, presentation: band, trigger: hidden}
    - {of: edge.disposition.pc_npc, inputs: published, presentation: band, trigger: hidden}

- module: substrate.post
  parent: substrate         class: substrate
  scales: [settlement, territory, peninsula]                tier: null
  resolver: gate            remit: []        budget: null      consumes: []
  emits: [{type: post.granted, terminal: false}, {type: post.revoked, terminal: false},
          {type: post.vacant, terminal: false}]
  state:
    - {name: post, bucket: post, writable: true, owner: substrate.post}
    - {name: post.budget, bucket: gauge, writable: true, owner: substrate.post}
  form: []      transitions: []
  disclosure:
    - {of: post, inputs: published, presentation: exact, trigger: hidden}
    - {of: post.budget, inputs: published, presentation: exact, trigger: hidden}
```

`substrate.post`'s two rows disclose **exact**, not band: a post's holder and a budget's remaining
points are things the player acts on directly this season, and hiding them would obscure an input rather
than a threshold. **Note what is absent from `substrate.edge`:** a shared strain counter, a shared
capacity, a shared break rule, and any NPC↔NPC disposition row. Their absence is the container's
compliance with R-1, R-2 and R-3, expressed in the contract rather than promised in prose.

---

## 13. Property audit

**Scope, and the honest limit. Nothing in this document rolls.** `substrate.entity`, `substrate.ledger`
and `substrate.gauge` are stores; `substrate.form`, `substrate.edge` and `substrate.post` are gates;
`derive_ob` is a derivation *consumed by* rollers elsewhere and is not itself a resolution. **No N/R/S/E
verdict is offered for a store or a gate** — manufacturing one for state with no draw is the error the
methodology explicitly names, and v1 was right to refuse it. What follows instead is the two properties
that *do* apply, plus every loop and gate with its bound. (Canon's Knot *formation* does roll — `Spirit
× 2 + History (Relationships)`, TN 7, Ob 2 — but that roll is canon's, at `knots_v30.md:76`, and
auditing it is the FI lane's job, not this page's.)

Above that sits `00 §0.1`: **a resolution-scoped audit cannot ask whether a design expresses the game.**
This page could pass every property below and still be the wrong substrate. The instrument for that
question is the elegance criterion, and its answers here are the one-line loss statements, the §10 cut
list and the `## Overrides` block — judgments, not checks.

| property | verdict | reasoning |
|---|---|---|
| **P-iii** bounded, monotonic | **pass, and the strongest claim in the suite** | every gauge is bounded by declared floor and ceiling and restores geometrically, so the fixed point `rest + a/λ` is finite for every bounded accrual and every `λ ∈ (0,1]`, checked **at load time** against the registry with no campaign run (§5.1). Monotone response is structural. Form is bounded because every form field's value set is enumerated in the registry |
| **P-v** right engine | **pass** | every module here is `gate`, `accrual` or `derivation`. Nothing on this page is uncertain and nothing on this page rolls. **Every form transition is a gate on purpose** (§2.2): the uncertainty was in getting the gauges to the threshold, and re-rolling there charges for it twice |

### 13.1 Loops, each with its bound

| loop | bound | gain |
|---|---|---|
| gauge deposit → band → module gating → deposit | the fixed point `rest + a/λ`, checked at declaration (§5.1) | **unmeasured**; campaign-reachable, so measurable with a control, and it should be measured before any writer lands |
| form transition ↔ its reverse | **`θ↑ − θ↓ ≥ H_MIN` plus `dwell ≥ D`, checked at load** (§2.3) | **bounded arithmetically** — the only loop here with a proved bound, and why hysteresis is mandatory rather than advised |
| Knot strain → rupture → conviction scar → conviction weight → behaviour → strain | **terminating**: rupture is `reversible: false`, so the edge leaves the loop permanently; strain is gauge-bounded −5…+5 per tier (`knots_v30.md:49-52`) | **unmeasured**, and it is **canon's loop, not this suite's** — the FI lane inherits the measurement obligation |
| NPC↔NPC edge strain → derived disposition → behaviour → strain | per-kind capacity (PP-724 `:673`); kinship cannot break by strain at all (`:334`); rivalry and feud escalate rather than accumulate toward break (`:674`) | **unmeasured** — and the three kinds are bounded by **three different mechanisms**, which is the per-kind semantics doing its job rather than a gap |
| **do the two strain loops couple?** | **no. By R-3 they never sum.** A node in both takes both effects independently (PP-724 `:162-167`) | **not a loop** — the row exists because a reader will ask, and the answer is the anti-unification property, verified by the *absence* of a shared counter in §12 |
| memory salience → weighting → behaviour → new perception → memory | **`MEMORY_CAP` top-K at the sweep, geometric salience decay, and `RELATION_SHARE_MAX`** (§3.2, §3.4) | **unmeasured**. Three independent bounds is not a measured gain, and this page does not claim it is |
| tag append → selection → outcome → tag append | dedupe on `(owner, kind, key)` bounds count by `candidates × posts`; magnitude bounded by the gauge the value deposits into (§3.3) | **unmeasured** |
| **a Key-driven cascade within a season** | **`DEFAULT_CASCADE_DEPTH_MAX = 0`** — the guard **prevents cascades outright** rather than pacing them (§9.3) | **not a loop today.** If **J-N** rules for reactive chains this becomes a real loop with no bound yet, and §9.3 is what to revisit |

### 13.2 Gates, each with what it reads

| gate | reads | fails to |
|---|---|---|
| tag provenance non-empty | the append call | a refusal at append time |
| form transition gate | gauges, tags, form, identity — **never a roll, never a received Key** | no transition; the entity stays as it is |
| hysteresis band | the registry, at load | **load failure**, not a runtime surprise |
| vacancy (`holder_id is None`) | the post | the faction does not act at that tier (`05 §1`) |
| `remit` | the post's remit list | the module is not in the option set — not a penalty, an absence |
| Knot capacity `< floor(Bonds/2) + 1` | the person's `knot` edges, counted; no stored counter | formation unavailable (`knots_v30.md:70`) |
| Knot Thread contact `TS ≥ 30` (either party) | the person gauge, 0–100 | formation unavailable (`knots_v30.md:69`) |
| converter gate (§7.4) | both endpoints' posts and factions, and the source edge's state | no new edge; the source edge is untouched either way |
| disclosure block present · `consumes:` row has rule content (W-6) | the contract, at check time | the contract check fails · the row is not declared |

### 13.3 The four qualitative verdicts, applied to the substrate rather than to a resolver

**Necessary** — four primitives, six entity kinds, six tag kinds. The relation taxonomy is **adopted,
not invented**, so its necessity argument is PP-724's own decision log (`:669`) rather than a claim this
page has to make; the two additions occupy a scope PP-724 declares out of bounds. §10 records fourteen
candidates refused, three of them cut because something on disk beat them. **Robust** — the two failure
directions the corpus measured are closed by arithmetic: an unrecoverable pinned gauge by the geometric
law, and a flickering threshold by the hysteresis band, both load-time checks. A third — the substrate
quietly acquiring a latency it does not have — is closed by §9.3 stating the absence rather than
assuming the presence. **Smooth** — one decay law, one obstacle owner, one disclosure contract, one write
rule with four leaves, one registry for the mutable-shape axis, one Key surface for every binding kind.
**Elegant** — six modules, one new registry from this page, no branch on any entity's identity anywhere,
and a player surface of three reads and zero verbs. The honest deduction: **the edge container is the
one object on this page whose elegance is contested**, and §7 argues it rather than assuming it.
