# 03 — World population: who exists, how many, at what stage

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) ·
## [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) ·
## `systems/settlements/settlement_layer_v30.md` §4.5 · `systems/npcs/npc_relational_graph_v30.md` (PP-724)
## `audit/2026-08-08-world-churn-audit/06_master_synthesis.md` (J-M)
## Produces: the answer to *how many people exist, where, when they are created, at what life stage,
## and how their kinship composes into a lineage* — never *what a person is generated as* (`02`) or
## *who holds which office* (`04`)

**This document mostly carries v1 `03` forward.** Population-as-a-function-of-posts-and-places, the
computable bound, the idleness rule and the RNG determinism rules survived the 2026-08-29 critique
untouched (`ARCHIVED.md`) and are **carried with their reasoning, not silently reproduced** — §§1, 4,
5, 6 say explicitly what changed (one bound term) and what did not (everything else). §§7–8 are the
two additions this suite's delta spec assigns here: **life-stage** and **lineage**.

**Scope boundary, stated once.** `02` owns *what a person is generated as* — the layered
condition-then-reify pipeline, the life-*path* stages that grant capability/traits/edges/convictions
during generation, caste/heritage assignment, beliefs. `04` owns *who holds which office* — the
candidate gate, the caste gating matrix, appointment. **This document owns the population as a
whole**: the count, the bound, the life-*stage* field's population-level vocabulary and its
transition timing, and how kinship composes into lineage at read. Where `02`'s and `04`'s machinery
is what a paragraph here depends on, it is cited, not re-derived.

---

## Overrides

**Note on authority (amended mid-session, Jordan-directed, 2026-08-29):** tier below states *what
kind of prior work* is being overridden, not a licence gate — nothing in the tree is out of bounds,
including a Jordan ruling, provided the argument is stated and is strong enough for its tier. Every
row states the merit case independently of who or what decided the prior version, per Jordan:
*"I just want the best possible proposal."* Where I evaluated an alternative and chose **not** to
override, that evaluation is recorded too (§8.2a) — silence is what is forbidden, not agreement.

| # | What is overridden | Tier | Why |
|---|---|---|---|
| **O-7** | v1 `03 §2`'s flat per-place candidate margin `k`, and its own reachability-bar justification for `k` | Jordan ruling (J-M, 2026-08-09) + ratified canon (`settlement_layer_v30.md:858`) | **Merit case, not just citation:** a flat `k` this document invented was always going to be a worse number than one the map already fixes per place kind — a Seat and an Outpost have no business generating the same margin, and `k` had to pretend they did. The ratified per-type table also closes the two-tier bug the audit found (Local Actors and NPE NPCs as separate stores) at zero cost to this document, since it was never this document's job to own that split. **Where the ratified version is worse, and I say so rather than papering over it:** it drops v1's stated reachability bar (≥2 qualified candidates at the median place) with nothing to replace it — Town/Fortress/Cathedral/Mine ship exactly one Local Actor, so single-candidate governance appointments are now reachable at those kinds where v1's own number would have forbidden it by construction. §2.2 states this cost and declines to patch it with an invented number, because inventing one back would just be O-7 in reverse with worse provenance. **Net verdict: adopt the table for the count, keep the reachability concern open and explicit rather than resolved by either the old `k` or a new fabricated term.** |

**Not an override, a correction of scope:** v1 `03 §4.1` said *"ageing is not modelled. If it is ever
wanted, it enters as a gauge with a band, not as a per-season elimination check."* v2 change A now
wants it, and §7 below is the answer — **as a form value, not a gauge**, which is a stronger claim
than v1's speculative parenthetical and is argued in §7.1 rather than merely asserted.

---

## 1. The rule — unchanged, carried forward

> **Population is a function of posts and places. It is not a function of time.**

There is no birth rate, no spawn queue, no wandering-adventurer tap, no departure percentage, and no
population target. Every person in the world exists because something needed a person, and the count
of things that can need a person is bounded by the map. Two lines of evidence converged on this in v1
and neither has moved: the measured failure of clock-driven generation in the nearest analogue
franchise (five-figure late-campaign character counts, a throttled tap), and ED-IN-0201's own
consequence — a generator that produces people *during* play cannot guarantee a head post is filled
when the season loop asks on turn one, so only demand-driven seeding at world-gen satisfies the gate
at season 1. **Unchanged; carried with its reasoning.**

---

## 2. World-gen: exactly the people the gate requires, plus a ratified margin

At world creation, in this order, consuming no shared randomness beyond the substreams named in §6:

| # | step | produces |
|---|---|---|
| 1 | Load the tier registry; validate every place's parent edge resolves to a live node | the map |
| 2 | Instantiate the **required posts**: one `head` per faction; one `governor` per place whose kind declares a governance post; `minister` posts per the faction's declared offices | the demand set |
| 3 | Issue one `cg.demand` per required post; satisfy each authored-first (`02`) | the officeholders |
| 4 | Issue **Local Actor** demands per place, **per the ratified per-type table below**, unaffiliated with any faction, `life_stage: adult` by default | the candidate margin |
| 5 | Materialise the edges the generator attached (including `kinship`, `02`'s stage-1 seed), and validate the graph has no dangling person ids **and no kinship edge whose endpoint was not independently demanded by steps 2–4** (§8.3) | the relationship graph |

### 2.1 Step 4 is no longer a bare number (O-7)

v1 declared a flat per-place `k` with its own reachability-bar justification. **This suite's delta
spec strikes it**: J-M, RULED by Jordan 2026-08-09, *"local actors should be NPCs."* The `§4.5` Local
Actor and the NPE NPC are the **same entity class**, seeded through the NPC path into the person
store — not a second, lightweight tier. `settlement_layer_v30.md` supplies the count and the profile
directly, so the margin is no longer a tuning parameter this document invents:

| place kind | count | | place kind | count |
|---|---|---|---|---|
| Seat | 2 | | Cathedral | 1 |
| City | 2 | | Mine | 1 |
| Town | 1 | | Outpost | 0 |
| Fortress | 1 | | Port | 2 |

*(`settlement_layer_v30.md:858`, ~45–50 across 36 settlements. Ratified, not a shape proposal — this
is the one number in this document that is not mine to propose.)* Each Local Actor carries the
profile canon already declares: Role (Elder / Magistrate / Merchant / Priest / Artisan / Farmer /
Fisher / Miner / Scholar / Healer), one Conviction — resolved through
`descriptors.resolve_conviction`, which **raises** on an unknown name (`01 §1.2`); this document names
no conviction literally — and a starting Disposition (`+1` toward governor, `0` elsewhere).
`life_stage` is not part of canon's profile; **this document assigns `adult`** at generation, since
none of the ten listed roles reads as a role a minor would hold (§7.2).

### 2.2 An honest cost of the correction

v1's `k` carried a **stated reachability bar**: at the median place, at least two candidates must
qualify for the governance post's gate, so appointment was never uncontested by construction. The
ratified table does not carry an equivalent guarantee — **Town, Fortress, Cathedral and Mine generate
exactly one Local Actor**, so at those place kinds the unaffiliated candidate pool for a contested
governance appointment can be a single name at world-gen. This is not a defect this document can fix
by inventing a second margin term without re-committing O-7's error. **Named as a residual for `04`**:
a governance appointment's real candidate pool is not only Local Actors — displaced officeholders
(`04 pm.recall`/`pm.tenure` leaving a person available), a place's own post-holders' kin (§8), and
scene-generated participants (§4) all also qualify against the same gate. Whether that composite pool
clears two qualified candidates at every place kind is a `04`-lane question this document does not
resolve, and it should not be asserted clear without checking.

---

## 3. The bound, stated arithmetically — survives, and gets stronger

```
|persons|  ≤  |required_posts|  +  Σ_places local_actor_count(place.kind)  +  |active_scene_demands|

|required_posts|  =  |factions|                              # one head each
                  +  |places with a governance post|
                  +  Σ_factions |declared minister offices|
                  +  |commander posts raised this season|    # transient; see `12_adjacent_systems.md`
```

Every term on the right is bounded by the map or by a declared constant, exactly as v1 argued:
`|factions|`, `|places|` fixed by the tier registry (loaded once); `|declared minister offices|` a
per-faction registry constant; `|commander posts|` bounded by a faction's action budget, itself
bounded by its filled posts; `|active_scene_demands|` bounded by the scene budget per season (`10`).
**What changed:** the margin term is now `Σ_places local_actor_count(place.kind)` — a **ratified
per-type sum fixed by the tier registry**, not a tuning parameter this document chose. That is
strictly stronger than v1's bound: the margin term used to be *a number this document had to defend*;
it is now *a number the map already fixes*, so the whole right-hand side is computable from the tier
registry and the faction charter alone, with nothing this document contributes to the arithmetic
except the sum operator.

**Kinship does not add a term.** §8.3's world-gen invariant — no kinship edge may name an endpoint
outside the already-bounded store — means the relationship graph never becomes a second population
source. An edge is a separate primitive with its own store; `|persons|` cannot be inflated by walking
it.

**Falsifier — unchanged in shape, updated in formula.** A test computing the ceiling from the
registries (now including the per-type Local Actor table) and asserting the person store never
exceeds it across a seeded campaign. Load-bearing on the game — the failure it catches is the one
that turns a late campaign into an unplayable roster.

---

## 4. Population changes only through named events — unchanged

Between world-gen and the end of the campaign, the person count moves for exactly four reasons, and
each is a Key with a cause:

| event | direction | raised by |
|---|---|---|
| a post falls vacant and no candidate qualifies | **+1** — a `cg.demand` at that node | `04 pm.vacancy` |
| a scene requires a participant that does not exist | **+1** | the scene dispatcher |
| death | **−1** | a resolution outcome — never a mortality roll on a timer |
| exile or withdrawal | **−1**, reversibly | a resolution outcome |

**There is no season-tick population step.** Nothing at the accounting boundary iterates people to
decide whether more should exist. **§7's life-stage transitions are not a fifth event**: a `minor →
adult` transition is a form change on a person who already exists, exactly as `07`'s village-to-town
transition changes a place's `form.tier` without changing `|places|`. Population count and population
*composition* are different questions, and this table answers only the first.

### 4.1 Death is an outcome, never a clock — unchanged

Refused on the same specific ground as v1: under ED-IN-0201, a death that empties a head post stops a
faction acting, so a death on a timer would silently gate the strategic layer on a die roll nobody
decided to make. Death as an outcome of something — a battle, a tribunal, a succession contest, a
scene — keeps the gate coupled to play. **§7 does not reopen this.** Life-stage is gated on elapsed
seasons, never on a survival roll; nothing in this document adds age-based mortality.

---

## 5. Idleness — unchanged, carried forward

> **Idleness applies only to a person who held a post and lost it, and it is a one-time deposit at the
> moment of loss, not a per-season bleed.**

```
on post_revoked(person p, post q):
    gauge_deposit(p.standing, −δ(q), provenance=<the revocation Key>)
```

`standing` is a Gauge (`01 §5`), so it recovers geometrically toward `rest` at `λ` per season with no
further input; a person never posted does not decay — they are a candidate, not a failure. The
arithmetic argument (a one-time deposit against geometric restoring is recoverable for every `λ > 0`,
and even the pathological churned-every-season case settles at a finite `rest − δ/λ`) is v1's and is
unweakened by anything in this document. **Carried verbatim in substance; no change.**

---

## 6. Determinism and the RNG contract — unchanged, carried forward

| rule | statement |
|---|---|
| **R-1** | Person generation draws only from the `cg` substream (`02`), derived from the campaign seed |
| **R-2** | Any per-season iteration over people that draws randomness uses a **population substream**, distinct from both the campaign stream and the `cg` stream |
| **R-3** | Population guards read the **person store**, never a call counter on the generator |
| **R-4** | The substreams land and are proved byte-identical against the existing seeded goldens **before** the first person exists |

**This is `00`'s P0-2 stated as a precondition of the whole suite, not a step inside this document.**
R-3 stays worth stating separately: a guard counting generator calls is blind to every other way a
person can enter the store — a load, a save restore, a test fixture — which is to say it cannot
observe the state it exists to bound.

**§7 needs no new rule here, and that is worth stating rather than leaving implicit.** A life-stage
transition is a **gate** (`01 §2.2`): every transition in this suite's fourth write leaf resolves as
`gate`, never as a roll, so it consumes no randomness and touches no substream. The only draws
associated with a person's life course are the ones `02`'s generation-stage pipeline already makes
from the `cg` substream at creation time; nothing in this document adds a second draw site.

---

## 7. Life-stage (new) — an Entity `form` value, not a stored age bucket

### 7.1 Why this is a form value and not a gauge, and not a setter

v1 speculated ageing would "enter as a gauge with a band, if ever wanted." **It is wanted, and a gauge
is the wrong primitive for it**, for the same reason `01 §1.3` gives for capability: a gauge decays
toward a rest value, and life stage does not rest anywhere — nobody reverts from `adult` to `minor`.
The correct primitive is change A's form bucket (`01 §1`, `01 §2`): `life_stage` is declared as a
transitionable field on `person` identity/form split (`01 §1.1`), and this document supplies the
vocabulary and the transition rows the field needs to do anything.

**The vocabulary is deliberately coarse, and narrower than `02`'s generation pipeline — stated so a
reader does not conflate the two.** `02`'s life-*path* (Origin → Childhood → Formation → Entry →
Career) is the **content-generation walk**: it decides what capability, traits, edges and
convictions a person is generated with, and it runs once, at creation, gated by the person's age at
that instant. It is not a persistent field — nothing reads "which generation stage did this person
stop at" after generation completes. **`life_stage` is the persistent field population and `04` need
for an ongoing question — is this person old enough to hold a post — and it needs exactly two values
to answer it:**

```yaml
form_field: life_stage
entity_kind: person
values: [minor, adult]
```

*Emergent possibility lost if cut:* a candidate pool would contain the same interchangeable adult in
every slot, and there would be no way to express an heir who exists, is known, and cannot yet be
appointed — a shape several of the setting's succession and dynastic mechanics assume.

**A third value (`elder`) was considered and cut.** Nothing in this document, `04`, or the idleness
rule needs it: there is no forced retirement, no age-based mortality (§4.1), and no mechanic gated on
being old rather than merely adult. An unconsumed form value is apparatus a player never perceives —
exactly `00 §1`'s under-distilled failure — so it is refused here. If `04` or a later document finds a
real consequence for "elder" (a succession-pressure gate, say), that document adds the value and the
transition row; this one does not add it speculatively.

### 7.2 The transition, and why it needs a gate but no hysteresis band

```yaml
transition: lifestage.minor_to_adult
entity_kind: person
field: life_stage
from: minor
to: adult
gate: (current_season - person.birth_season) >= AGE_MAJORITY_SEASONS   # shape proposal, not a ledger constant
cost: none
emits: form.transitioned
reversible: false
class: substrate
```

**Gated, per `01 §2.2`'s rule that every transition is a gate: the uncertainty here is nil, which is
the degenerate but still-correct case of "gate where the answer is on the board."** There is no
sense in which a person's age is uncertain given `birth_season` and the current season — both are
already-written, readable state — so a gate is not merely permitted here, it is the *only* resolver
kind that could apply; rolling for majority would be `00 §6` principle 4's violation in its clearest
possible form.

**No hysteresis band, and this is a property of the gate's input, not an exception to `01 §2.3`'s
rule.** `01 §2.3` requires a band **only when `reversible: true`** — the rule is conditional, not
universal, and this transition satisfies it by not qualifying rather than by being excused. The
reason it does not qualify is worth stating precisely, because it is the general argument for *why
age-gated transitions never need one*: hysteresis exists to stop a **gauge** that can rise and fall
from flickering across a single shared threshold (`01 §2.3`'s worked failure: grow, decay, grow,
oscillating every season). `life_stage`'s gate reads `current_season − birth_season`, and `birth_season`
is **identity — immutable** while `current_season` is monotonically non-decreasing. **The gate's own
input cannot move backward across its threshold, because nothing in the substrate can decrement a
season or rewrite a birth date.** Once `minor_to_adult` fires, no future season state can make it
fire in reverse, so there is no reverse row to declare, and a band would be defending against an
oscillation that the input's own monotonicity has already made impossible. This is the general
shape: any transition gated purely on elapsed time since an immutable identity field is irreversible
by construction, and `01`'s hysteresis requirement — correctly — does not ask for a band it cannot
use.

> **Falsifier.** A load-time test asserting `lifestage.minor_to_adult` declares `reversible: false`
> and that `references/form_registry.yaml` contains no `adult → minor` row for any gate expressed
> purely over `(current_season − birth_season)`. Load-bearing on the game: the difference between an
> heir who grows up once and a form field that requires a band this document would otherwise have to
> invent a fake reverse case to justify.

**Timing ties to J-N without needing anything from it.** Per `01 §9.3`, the substrate supplies no
cross-season emission carry — a gate must read *current* state, never react to something posted
earlier. `lifestage.minor_to_adult` already does exactly this: it is evaluated by re-reading
`birth_season` against `current_season` at the accounting boundary, every season, for every `minor`
in the store — never by scheduling a future "become adult" emission at generation time. This document
depends on nothing from J-N resolving either way.

### 7.3 Where the check runs

```yaml
- module: wp.lifecourse
  parent: world_population
  class: substrate
  scales: [personal]
  tier: null
  resolver: gate
  remit: []                 # applied at the accounting boundary; not invoked by any post (01 §9.2 W-5)
  budget: null
  consumes: []               # reads state, never a received Key (01 §9.3)
  emits:
    - {type: form.transitioned, terminal: false}
  state: []                  # the write is substrate.form's; this module names the gate, not the leaf
  form:
    - {entity_kind: person, field: life_stage}
  transitions:
    - lifestage.minor_to_adult
  disclosure:
    - {of: life_stage, inputs: published, presentation: exact, trigger: hidden}
```

Disclosed **exact**, not band: `01 §11` discloses a post-holder's own posts and budget exact because
they are inputs to a decision the player is making now, and a candidate's life stage is exactly that
kind of input for whoever is choosing among candidates (`04`) — concealing whether a named heir is
eligible yet would hide an input, not a threshold, which is the E-2 contract's one hard line
(`01 §8`).

*Player-facing surface: none.* `life_stage` is read wherever a candidate or a person is inspected
(`04`'s candidate list, a Slate item's detail), never operated. It is `substrate` under `00 §2.1` by
the classification's own test — a player could not "set" a life stage, could not skip one, and the
game changes because of *who is eligible*, never because of a menu choice about ageing.

---

## 8. Lineage (new) — derived by walking `kinship` edges, never stored

### 8.1 What `01` already declares, and what this section adds

`01 §1.1` already reserves `lineage_ref` as **person identity** — immutable, written once at
generation (`02`'s job). This document does not redefine it. **`lineage_ref` and "lineage" are not
the same object, and conflating them would be exactly the under-distilled failure `00 §1` warns
against**: `lineage_ref` is a fixed pointer set at birth (e.g. to a founding or house-anchor entity,
`02`'s call how it is populated); **lineage — the actual chain of who descends from whom — is a
*graph fact*, and a graph fact is read, never stored**, under this suite's own write rule (`01 §2.1`,
AU-1: *no aggregate is ever written*). A stored "lineage" object recording an ancestry chain would be
exactly the aggregate-over-edges the write rule forbids — the same defect `01 §7.3` (O-3) found and
struck for NPC↔NPC disposition, one layer up.

### 8.2 The derivation

Lineage composes on the `kinship` edge kind this suite adopts from PP-724 (`01 §7.2`,
`npc_relational_graph_v30.md:52`, `:85-93`): *symmetric, with a special asymmetric parent→child case*.
PP-724 already gives the two facts this derivation needs and nothing this document has to invent:
**"parental kinship has direction-of-authority semantics"** (`:91`, the asymmetric edge is directed
parent→child, so a walk can distinguish ancestor from descendant) and **kinship is authored, not
formed in play**, except through a marriage mechanic not yet in canon (`:288-290`) — so at world-gen
the graph a lineage-walk reads is exactly the graph `02`'s stage-1 seed and PP-724's NPC-sheet
authoring produced, with no separate lineage-authoring step for this document to design.

```
ancestors(person, depth)     : walk directed parent→child kinship edges backward, ≤ depth hops
descendants(person, depth)   : walk them forward, ≤ depth hops
siblings(person)             : persons sharing an incoming parent→child edge from the same source
lineage(person)              : the connected component reachable by any of the above — a VIEW, not a store
```

Each is a **derivation** (`00 §7`'s resolver table: *"a read-only aggregate … including divergence
and salience"* — lineage joins that list): no gauge, no tag, no cache with a write path. `depth` is a
caller-supplied bound so a query over a long-lived campaign's graph stays bounded cost; it is a query
parameter, not stored state, and nothing about correctness depends on its value beyond how far back
or forward the caller chose to look.

**Severance does not delete the edge, so lineage does not need a second rule for it.** PP-724 §3.4
(`:175`): a formally severed kinship edge transitions to `severed` state, but *"the historical
kinship remains canonical."* A lineage walk over `kinship` edges regardless of `state` therefore
still finds a disinherited line; a walk that wants only *currently cooperative* kin filters on
`state: cooperative`. Both are the same derivation reading a different filter — not two mechanisms.

*Emergent possibility lost if this were stored instead of derived, or cut entirely:* a stored
aggregate would drift from the edge graph the moment a kinship edge transitioned (exactly the
staleness `01 §7.3`'s O-3 found), and cutting the derivation entirely would mean a feud transmitting
along kinship (PP-724 `:196-205`, already canon) has no way to ask "who are this person's kin" at
all — the whole multigenerational mechanic PP-724 calls load-bearing would have no query surface.

### 8.2a A fork evaluated and not taken: in-play birth as a population event

Per the amended authority model, a canon gap is not automatically the right answer just because
nothing forbids filling it — so this is argued on merit, not left as a silent inheritance.
`npc_relational_graph_v30.md:288-290` defers child-of-marriage kinship to a future, not-yet-written
`marriage_v30`, which leaves an obvious-looking gap: should this document add "a child is born" as a
fifth population-count event, alongside §4's four? **No, and not merely because canon has not built
it yet — because building it would break this document's one load-bearing property.**

The J-M ruling's own argument (`06_master_synthesis.md:539`) and this document's whole §3 rest on one sentence from v1 §1 that
nothing in this suite has touched: **population is a function of posts and places, never of time.**
A birth event fires on a clock — marriage happens in a season, gestation and childhood elapse in
seasons, and a person appears in the store because time passed, not because a post or a place
demanded one. That is a *fifth* growth channel with no post or place behind it, and unlike §4's four
named events — each traceable to a vacancy, a scene, or a resolved contest — a birth traces to
nothing but the calendar. Adding it would reopen exactly the failure mode §1 cites the analogue
franchise for: population growth decoupled from anything the player did or the map demanded, with no
symmetric event that removes a person for the same reason. **The argument against holds even if
`marriage_v30` ships tomorrow**: that document can make marriage a `kinship`-forming converter
(`01 §7.4`'s pattern) without population needing to grow at all, by having the *children* it wants to
express enter the store the way every other person does — as a Local Actor demand, a scene demand, or
a future post's candidate — with the marriage's kinship edge attached after the fact, not as the
person's cause of existing.

**So: this document declines to add a birth event, on the merits, and names the constraint a future
marriage design must respect** — a wedding may create a `treaty` or strengthen a `kinship` edge
between two already-existing persons; it may not, by itself, be why a new person exists.

### 8.3 The invariant that keeps lineage from becoming a second population source

**A kinship edge's endpoints must both already be members of the demand-bounded store (§3).** An
authored backstory that names a relative who is not independently demanded by a required post, a
Local Actor slot, or a scene (§4) is represented as a **Tag** (`kind: Precedent`, e.g. "mother,
deceased, unrepresented") on the person, **never as a new Entity created solely to hold the other end
of an edge**. This is the population-side half of `01 §7`'s edge design: the edge container can hold
a `kinship` relation between any two entities, but nothing about the container *creates* the entities
it relates, and this document is where that boundary has to be stated, because population — not the
edge substrate — is what owns the bound the boundary protects (§3).

> **Falsifier.** Extend v1 §2 step 5's existing graph validation (already checked at world-gen): for
> every `kinship` edge, both `entity_id`s resolve to a person present in the bounded store computed by
> §3 before edge materialisation. A violation is a world-gen defect, caught at load, never a playtest
> surprise — the same standard §3's own falsifier holds itself to.

### 8.4 Where the player touches this

**Nowhere, directly.** A player never opens a family tree screen or a lineage query tool — this is
`00 §2.1`'s substrate by the classification's own test: removing the ability to *invoke* a lineage
query changes nothing about how the game behaves, because nothing here fires from a player request.
What the player experiences is downstream and already owned elsewhere: a feud transmitting to a
newly-relevant heir (PP-724, canon), a candidate list that explains *why this name* by citing a
kinship tie (`04`'s job to surface, this document's job only to make the fact derivable), an
inspection panel showing a tag's provenance (`01 §11`'s existing three-read surface — lineage adds no
fourth).

---

## 9. The loop this closes, and what is not claimed about it — carried forward, one note added

```
posts filled  ──►  actions available  ──►  holdings and facilities  ──►  more posts
      ▲                                                                       │
      └───────────────────────────────────────────────────────────────────────┘
```

**Unchanged from v1: a positive feedback loop, not claimed to be damped.** It is bounded twice —
`|required_posts|` has a data-computable ceiling (§3), and `05`'s per-faction action ceiling does not
scale with post count — and its per-cycle gain is **unmeasured**, named as a build-order item rather
than resolved here (`13`).

**One addition.** Kinship and life-stage do not participate in this loop's growth term. A kinship
edge never creates a post, a place, or a person (§8.3), and a life-stage transition never creates
anything at all — it is a form change on a person who was already counted. **Both additions are
inert with respect to the one loop this document has ever had to bound.**

---

## 10. Player-facing surface — this document's whole contribution is near-zero

Per `00 §2.3` rule 4: this table must not be longer than the substrate table above it, and it is not.

| what the player is actually asked | how often |
|---|---|
| *(nothing this document adds)* | — |

| substrate this document introduces, never operated directly |
|---|
| the Local Actor margin (§2) — a fixed, data-driven count, not authored per playthrough |
| the population bound (§3) — a load-time check, invisible unless it fails |
| the `life_stage` field and its one transition (§7) — read on a candidate list, never set |
| the `lineage` derivation (§8) — read wherever a kinship fact is surfaced, never queried by the player directly |

**Per `00 §2.3` rule 5** (*could this be removed from the player's hands entirely and still change
the game?*): everything in this document already lives entirely outside the player's hands. The test
is satisfied trivially, because this document was never a candidate for surface — it is population
accounting, and accounting has no verbs.

---

## 11. Module contracts

```yaml
- module: wp.worldgen
  parent: world_population
  class: substrate
  scales: [peninsula]
  tier: null
  resolver: gate
  remit: []
  budget: null
  consumes: []
  emits:
    - {type: person.generated, terminal: false}      # via cg.attach, one per required post + Local Actor
    - {type: post.vacant, terminal: false}            # for any post left unfilled at gen
  state:
    - {name: post, bucket: post, writable: true, owner: substrate.post}
    - {name: entity, bucket: entity, writable: false, owner: substrate.entity}
  form: []          # worldgen assigns initial form values via substrate.entity at creation, not a transition
  transitions: []
  disclosure:
    - {of: post, inputs: published, presentation: exact, trigger: hidden}

- module: wp.census
  parent: world_population
  class: substrate
  scales: [peninsula]
  tier: null
  resolver: derivation
  remit: []
  budget: null
  consumes: []
  emits: []
  state: []                    # pure read; the ceiling check reads registries, not state
  form: []
  transitions: []
  disclosure:
    - {of: population_ceiling, inputs: published, presentation: exact, trigger: hidden}

- module: wp.displacement
  parent: world_population
  class: substrate
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
  form: []
  transitions: []
  disclosure:
    - {of: standing, inputs: published, presentation: band, trigger: hidden}

- module: wp.lifecourse            # NEW (§7)
  parent: world_population
  class: substrate
  scales: [personal]
  tier: null
  resolver: gate
  remit: []
  budget: null
  consumes: []
  emits:
    - {type: form.transitioned, terminal: false}
  state: []
  form:
    - {entity_kind: person, field: life_stage}
  transitions:
    - lifestage.minor_to_adult
  disclosure:
    - {of: life_stage, inputs: published, presentation: exact, trigger: hidden}

- module: wp.lineage                # NEW (§8)
  parent: world_population
  class: substrate
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: derivation
  remit: []
  budget: null
  consumes: []                      # reads the edge store directly; nothing here reacts to a Key
  emits: []
  state: []                         # a pure view over substrate.edge; owns nothing
  form: []
  transitions: []
  disclosure:
    - {of: lineage, inputs: published, presentation: exact, trigger: hidden}
```

`wp.lifecourse` and `wp.lineage` are both zero-state modules — one names a gate over data the
substrate already owns, the other names a read over data the substrate already owns. Neither adds a
stored field beyond what `01` already declared (`life_stage` in the form split; the `kinship` edge
kind in the edge registry). That is the compression this addition should be held to: two new module
rows, zero new primitives.

---

## 12. Property audit

**Scope.** `wp.worldgen` and `wp.census` resolve nothing — they instantiate and derive; no N/R/S/E
verdict is offered for them, unchanged from v1. `wp.lifecourse` is a **gate**: diagnosed on P-v and
on P-iii's monotonicity clause. `wp.lineage` is a **derivation** with no draw and no write: the same
scope limit `01 §13` applies to `divergence` and `salience` applies here — no verdict manufactured for
state with no draw. `wp.displacement` writes a gauge and is diagnosed on P-iii, unchanged from v1.

| property | verdict | reasoning |
|---|---|---|
| **P-iii** bounded, monotonic | **pass** | Population has a computable ceiling from data (§3), now strictly stronger than v1's since the margin term is a ratified sum rather than a chosen constant. Displacement is a one-time bounded deposit into a geometrically-restoring gauge (§5), recoverable for every `λ > 0`. `life_stage`'s transition is monotone by construction (§7.2): the gate's input, elapsed seasons since an immutable birth date, cannot move backward, so the field can only ever hold `minor` then `adult`, never oscillate |
| **P-v** right engine | **pass** | Population is a gate on data, not a contest; displacement is a deposit, not a roll; `life_stage`'s transition is a gate for the degenerate-but-correct reason that its answer has zero uncertainty given already-written state (§7.2) — rolling for it would be `00 §6` principle 4's violation in its clearest form. `lineage` rolls nothing and is not scored against this table, per the scope note above |

### 12.1 Loops, each with its bound

| loop | bound | gain |
|---|---|---|
| posts filled → actions available → holdings/facilities → more posts (§9) | `|required_posts|`'s data-computable ceiling (§3) and `05`'s flat per-faction action ceiling, independently | **unmeasured**, named as a build-order item (`13`), unchanged from v1 |
| `lifestage.minor_to_adult` re-evaluated every season for every `minor` | **not a loop** — the gate is idempotent once fired (`reversible: false`), so re-checking an already-`adult` person is a no-op forever, and a `minor` who has not crossed the threshold is checked again next season with no accumulated effect | **terminating per person**, and bounded in aggregate by the number of `minor`s the store ever contains, itself bounded by §3 |
| kinship edge → lineage derivation → a downstream decision (e.g. feud transmission, PP-724 canon) → a new edge or edge-state change → lineage re-derived | **not a write-back loop from this document's side**: `wp.lineage` never writes, so it cannot be the loop's amplifying term. Whatever writes the new edge state is canon's feud-transmission rule, and its bound is that rule's, not this document's | **not this document's loop to bound** — cited so a reader does not mistake a read-only derivation for a feedback term |

### 12.2 Gates, each with what it reads

| gate | reads | fails to |
|---|---|---|
| population ceiling (§3) | the tier registry, the faction charter, the scene budget constant — all load-time data | a load-time failure, never a runtime surprise |
| `lifestage.minor_to_adult` | `person.birth_season` (identity), `current_season` (world state) | the person stays `minor`; re-checked next season |
| world-gen kinship-endpoint invariant (§8.3) | every `kinship` edge's two endpoints against the §3-bounded store | a load-time failure — a dangling or phantom endpoint blocks world-gen, never surfaces mid-campaign |

### 12.3 The four qualitative verdicts

**Necessary.** Under ED-IN-0201 a campaign with no people performs zero faction actions — v1's
argument, unweakened. Life-stage is necessary in the narrow sense §7.1 argues: without it, a
generated heir and a fully seasoned officeholder are the same object, and several of the setting's
succession mechanics assume they are not. Lineage is necessary in the sense §8.2 argues: PP-724's
feud-transmission mechanic already needs a "who are this person's kin" query and had no owner before
this document supplied one as a derivation. **Robust.** The two documented failure directions of the
alternatives — unbounded growth and an unpayable idleness bleed — are each closed by an arithmetic
property, unchanged from v1; life-stage adds a third closed direction, a flickering age gate, closed
not by a band but by the gate's own input being unable to reverse (§7.2), which is a stronger closure
than a tuned band would have been. **Smooth.** One pipeline with `02`, one substream discipline, one
Key per population-count event, one new form field with one transition row, one derivation with no
write path. **Elegant.** Five modules, two of them ("lifecourse", "lineage") contributing zero new
stored state between them — the whole of change A and change E's population-facing footprint is one
form value and one graph-walk function. §2.2 names the one place this document's elegance is bought
at a cost: the contestedness guarantee v1's `k` carried is not reproduced by the ratified table, and
this document says so rather than asserting a guarantee it cannot check.
