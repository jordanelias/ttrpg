# 01 — Substrate: four primitives, a form bucket, four write leaves, one wrapper shape

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · `engine/substrate/{descriptors,composition,keys}.py` ·
## `engine/autoload/dice_engine.py` · `systems/fieldwork/knots_v30.md` (canon, cited not copied)

Everything in this suite is a composition of what is on this page. If a later document needs a fifth
kind of stored thing, that is a defect in this page, not a licence to add a field somewhere else.

**Everything on this page is `substrate`** in the sense of `00 §2.1`, without exception. §11 is the
whole player-facing surface of this document, and it is three read-only affordances and zero verbs.

## Overrides

Every override is listed, tiered and argued, per the suite's one hard rule: **a silent override is
the corpus disease this suite exists to stop.** `00 §5.3` collects these with the rest of the
suite's so Jordan can veto them individually.

| # | What is overridden | Tier | Why |
|---|---|---|---|
| **O-1** | **v1 `01 §1`'s "identity is immutable and carries `place.kind` / `person.capability`"** | this suite's own v1 | it made settlements ungrowable and characters unprogressable. Corrected by the form bucket (§1, §2), not loosened |
| **O-2** | **v1 `01 §1.2`'s closed six-member `relation` enum, and this suite's own draft eight-kind table** | this suite's own v1 and draft | **cut, superseded by `systems/npcs/npc_relational_graph_v30.md` (PP-724)**, which already ships six NPC↔NPC edge types with per-type semantics and a decision log. §7.2 |
| **O-3** | **v1 `01 §1.2`'s `disposition` Gauge on every edge** | this suite's own v1 | for NPC↔NPC pairs that stores an aggregate over edge strengths, which v1's own write rule forbids. PP-724 `:331-345` derives it. §7.3 |
| **O-4** | **PP-724 §13's "relational edges file (separate)" storage decision** | ratified-adjacent (Class A, **PROVISIONAL**) | edges become entities in the general store rather than an NPC-only file, so one provenance rule, one disclosure contract and **one Key surface** cover every binding kind — which is what Part VI asks for. **Only storage moves; every per-kind semantic stays where PP-724 put it.** §7.3 |
| **O-5** | **v1 `01 §7`'s "distributor" framing of the subsystem wrapper** | this suite's own v1 | reframed to Part III's herald criterion; the wrapper populates `targets[]` and routes nothing. §9.1 |

**Not overridden, and deliberately so:** ED-POL-11 (patronage ≠ Knot), PP-724 §0 (PC↔NPC and NPC↔NPC
do not collapse), PP-724 §3.3 (strain counters never aggregate) — all three are *preserved by
construction* in §7.3, not merely respected. Part VI's unified-bond prohibition is **weighed and
partly adopted**: its taxonomy concern is honoured, its converter requirement is built (§7.4), and
its storage concern is the one point of disagreement, argued at O-4.

---

**v2 delta against v1 `01`:** the entity gains a **form** bucket (change A); the write rule gains a
**fourth leaf** and hysteresis becomes mandatory; the edge becomes a **shared container with per-kind
semantics and explicit converters**, adopting canon's existing taxonomy rather than inventing one, and
the Knot is held **outside** it (change E, §7); Tag gains **Memory**; the wrapper is reframed as a
**herald** (§9). Everything else on this page — the decay law, `derive_ob`, the disclosure contract,
the player model, the relational-share cap — survived the critique and is carried across with its
reasoning.

---

## 1. P-1 — Entity: identity is immutable, form is not

One identity primitive with **declared kinds**. A person, a place, a faction, a unit, a relation and
a bloc are the same shape. Making Person a primitive while Place was something else would put two
containers with identical structure into two taxonomies — the shape-divergence failure this suite is
supposed to be immune to.

```
Entity
├── entity_id : str
├── kind      : person | place | faction | unit | edge | bloc      ← SIX (bloc is new; 06 §3)
├── identity  : IMMUTABLE. Only what makes this the same thing over its whole life.
├── form      : MUTABLE, but ONLY through a declared form transition (§2)
├── gauges    : {gauge_id: Gauge}
├── tags      : [Tag]
└── posts     : [post_id]      for kinds that site or hold posts
```

### 1.1 The per-kind split — normative

| kind | identity (immutable) | form (declared transitions only) |
|---|---|---|
| **person** | `origin_node`, `birth_season`, **`caste`**, **`heritage`**, `lineage_ref`, `capability_provenance` | `life_stage`, `capability {attr: int}`, `traits {virtues, flaws}` |
| **place** | `site_id`, `founding_season`, `terrain` | `kind`, `tier`, `facilities[]`, `presences{}` |
| **faction** | `seat_node`, `charter_season`, **`ethos {conviction: weight}`** | `posture` (a small declared enum) |
| **edge** | `endpoints (a, b)`, `relation` | `state` — from the set its relation kind admits (§7.2) |
| **unit** | `home_node`, `raised_season` | `unit_kind`, `assignment` |
| **bloc** | `faction_ref`, `formed_season` | `members[post_id]`, `state` |

**v1's error, corrected.** v1 put `place.kind` and `person.capability` in identity and then forbade
writing identity, so settlements could not grow and characters could not progress. The bucket was
wrong, not the rule.

**Caste and heritage are IDENTITY, deliberately.** In this setting they are ascribed at birth and are
not something a person changes — *that is the point of a caste system*, and making them mutable would
quietly abolish the mechanic. What is mutable is how institutions **treat** them, which is the gating
matrix in `04`, and that lives in a registry where it can be read, argued with and reformed.

**Ethos is identity; practice is not.** A faction's ethos is what the institution is *for*. It does
not drift with whoever holds the head post — that was v1's error (root cause C). What moves is the
aggregate conviction of its post-holders, and the distance between the two is `divergence` (`06 §2`),
a **derivation**, never a stored value.

### 1.2 Capability reads the registry; it does not restate it

`engine/substrate/descriptors.py` owns the attribute roster, its scale, and the fact that the roster
is **incomplete by ruling** — nine defined, a tenth ruled and unnamed, exposed as
`ATTRIBUTES_PENDING_TENTH`. A person's capability map is keyed on `descriptors.ATTRIBUTES` and
**nothing in this suite names an attribute literally**. When the tenth is named, every person gains
it by regeneration and no design changes.

The same binds convictions: names resolve through `descriptors.resolve_conviction`, which **raises**
on an unknown name rather than silently scoring zero. That raise is load-bearing history, not
pedantry: `systems/fieldwork/sim/knots.py` scarred `conviction='Loyalty'`, a name the conviction
module had never heard of, so a ruled Close-Knot consequence returned magnitude 0 forever while its
caller reported success (`engine/substrate/descriptors.py:155-172`). **This suite names no conviction
literally either.**

### 1.3 Capability is form, not a gauge

An attribute that decays toward a rest value means **skills rot every season**, which is a different
game. Capability **ratchets**: it moves only through a life-path transition (`02 §4`), it is bounded
by `descriptors.ATTRIBUTE_FLOOR`/`ATTRIBUTE_CEILING`, and it never decays. This is the sharpest line
between the form bucket and the gauge, and it is the reason both exist.

### 1.4 `posts` is derived, and that is the whole answer to the vocabulary collision

*Officer* means a mass-battle unit commander. *Governor* means the holder of a settlement's
governance post. *Companion* is a relationship, not an office. All three compose on one person
because **`posts` is a derived set, not a `role` string**. There is no field to collide in, and
nothing here coins a new word for a rank-holder: a person **holds a post**.

⚠ **`seat` is not available as a synonym for post.** It is already a settlement type. Use *post*.

---

## 2. Form transitions — the fourth write leaf

### 2.1 The one write rule (v2)

> Every write terminates at exactly one of four leaves: **1.** a Gauge deposit · **2.** a Tag append ·
> **3.** a Post grant/revoke · **4.** a **form transition**.
>
> **Identity is never written. No aggregate is ever written.**

That is `propagation_spec_v1` §2's AU-1 made structural rather than a discipline: an aggregate has no
setter because the primitives it derives from are the only things with one.

**The fourth leaf is narrower than the three it joins, not wider.** A gauge deposit needs only
provenance; a form transition needs a declared row, a gate over readable state, a cost, an emission,
and — if reversible — a hysteresis band.

### 2.2 The transition row

Declared in `references/form_registry.yaml` (`00 §9`), cooked, read at runtime.

```yaml
transition: <id>
entity_kind: <kind>
field: <the form field it moves>
from: <form value or *>
to: <form value>
gate: <predicate over gauges, tags, form and identity>   # a GATE, never a roll
cost: <deposits>                                          # what it spends, as gauge deposits
emits: form.transitioned                                  # always; see 00 §9.2
reversible: true | false
hysteresis: {band: <float>, dwell: <int seasons>}         # REQUIRED when reversible
class: substrate                                          # every transition in this suite
```

Three properties, all normative.

**Gated, never rolled.** A village becomes a town because its condition gauges *sustained* a band,
not because someone rolled well. **The uncertainty was in getting the gauges there**, and re-rolling
at the threshold would charge for the same uncertainty twice. This is `00 §6` principle 4 at its
sharpest, and it is why every transition's resolver is `gate`.

**Emitting a CROSSING FACT, never a forecast.** Every transition emits `form.transitioned`, carrying
the gate's inputs and what actually changed. The world can therefore notice a growth, a demotion, a
rupture or a career step, and the Slate (`10`) can rank it. A silent form change is indistinguishable
from a bug.

⚠ **No emitter in this suite publishes a forecast.** `audit/2026-08-08-world-churn-audit/06_master_synthesis.md:565`
(Part VI, held) prohibits a world-visible imminence Key: *"`threshold_crossed` carries crossing
**facts**, never forecasts."* This suite adopts that without reservation — it is also §8's disclosure
contract read from the other side, since a forecast is a trigger point published in instalments. A
transition emits **after** its gate held, never that a gate is *about to* hold.

**Hysteresis is required on any reversible pair.** State the band explicitly.

### 2.3 The hysteresis arithmetic, and why a naive threshold fails

Let a reversible pair be `A→B` gated at `g ≥ θ↑` and `B→A` gated at `g ≤ θ↓` on gauge `g`. Require:

```
θ↑ − θ↓  ≥  H_MIN(g)          and       dwell ≥ D ≥ 1 seasons
H_MIN(g) =  the largest single-season swing g can reach
         =  max_seasonal_deposit(g)  +  λ_g · (ceiling_g − rest_g)
```

The second term is the decay contribution: from the ceiling, one season of decay alone moves the
gauge by `λ(ceiling − rest)`. A gauge sitting on a single threshold with no band **oscillates every
season** under ordinary play — grow, decay, grow — emitting a `form.transitioned` Key each time, each
of which is a Slate candidate. That is not a tuning problem; it is a property of the shape.

`H_MIN` is computable **at declaration time from the descriptor registry alone**, with no campaign
run: `max_seasonal_deposit` is the sum of the declared depositors' per-season caps. This makes the
guard cheap and total.

> **Falsifier.** A load-time test asserting that for every `reversible: true` transition pair,
> `θ↑ − θ↓ ≥ H_MIN(gauge)` and `dwell ≥ 1`. Load-bearing on the game: it is the difference between a
> settlement that grows and one that flickers between village and town forever. (`CLAUDE.md` §0.1
> point 5 — its output crosses into the engine and the exported params.)

**`dwell` is not redundant with the band.** The band bounds a *single-season* excursion; dwell bounds
a *sustained* one that happens to reverse. Both are cheap; only one is checkable arithmetically, and
the document says which.

### 2.4 What form transitions may not do

| forbidden | because |
|---|---|
| transition a field the invoking module does not declare in `form:` (`00 §7`) | the set of modules that can change a place's tier must be a grep over one field |
| roll for the transition | §2.2; the uncertainty was upstream |
| transition on a *derived* value alone with no gauge in the gate | a derivation has no history, so the transition would have no auditable cause |
| a reversible pair with `hysteresis: null` | §2.3 |
| transition identity | there is no such thing; identity has no transitions |

*Emergent possibility lost if the form bucket and its transitions were cut:* places and people would
be frozen at creation — no growth, no decline, no career, no ruin.

---

## 3. P-2 — Tag

Durable, discrete memory on **any** entity. Six otherwise-unrelated requirements land here: a
faction's grudge, a place's precedent, a person's obligation, a body's record of a defeated motion, a
fiscal claim that outlives its season, and the demoted officeholder's residual.

```
Tag
├── owner_ref     : (entity_kind, entity_id)   person | faction | place | post | edge | bloc
├── kind          : Precedent | Grudge | Debt | Reputation | Leverage | Memory   ← SIX (§3.1)
├── key           : str          what specifically; the dedupe axis
├── value         : float
├── created_season: int
├── ttl           : int | None   None = durable; durable tags survive succession
└── provenance    : key_id       REQUIRED, NON-EMPTY — the Key that caused this tag
```

### 3.1 Memory is the sixth kind, and the argument for opening a closed enum

v1 closed the enum at five and was right to: a mechanic must not be smuggled in as a tag family.
Opening it costs something real, so the argument has to be made rather than asserted.

**The five are third-person institutional record.** A Grudge is *what the faction holds against you*;
a Reputation is *what is said of you*; a Precedent is *what was done here*. Each is a claim whose
value is the claim's **magnitude**, and each dedupes to one row per `(owner, kind, key)`.

**A Memory is first-person and perceptual.** It belongs to a person, it is about an event **they
perceived**, and its `value` is not a magnitude — it is **salience**. Two properties make it
inexpressible inside the five:

1. **Its existence is conditioned on perception, not on the event.** A Grudge exists because
   something happened; a Memory exists because someone *saw* it. That distinction is the entire
   mechanic — nobody can act on a false or partial picture unless what a person knows is a separate
   object from what is true.
2. **`Reputation` is single-valued per owner by dedupe rule** (`§3.3`), so expressing memory as
   `Reputation(owner=perceiver, key=event)` would either break that rule or collapse every memory a
   person has into one row. The collision is structural, not stylistic.

So: **six kinds, and the enum closes again at six.** `00 §6` principle 6 binds — a seventh needs the
same two-part argument, and "a mechanic wants somewhere to live" is not it.

*Emergent possibility lost if Memory were cut:* nobody could act on a false or partial picture, so
deception, rumour and misjudgement would all be impossible.

### 3.2 Salience decay without a second decay law — a deliberate decision

A Tag's `value` does not decay; decay is a Gauge property. A Memory's salience must decay. Three
options were available and two were rejected:

| option | verdict |
|---|---|
| give the Memory tag a Gauge | **rejected** — one gauge per memory per person; the gauge count grows with everything anyone ever saw |
| add a decay field to Tag | **rejected** — a second decay law in the substrate, and five kinds that never use it |
| **derive salience at read** | **taken** |

```
salience(memory, t)  =  value · (1 − λ_mem)^(t − created_season)
```

Same geometric law as §6.1, **one owner, no setter, no new stored field, and no write** — it is a
derivation over data the tag already carries. `λ_mem` is declared once in the descriptor registry as
a suite-level constant, not per memory.

**The bound this needs.** Memories per person are capped at `MEMORY_CAP`, retained **top-K by
derived salience** at the sweep. Without it the tag list is an unbounded ramp on a person's whole
observed history, and every selection function that reads memory gets slower and noisier forever.
The cap is declared in the exported params with a reachability bar: **at `MEMORY_CAP`, a memory of
the maximum reachable salience must still displace the weakest retained one** — otherwise the cap is
a first-come lock rather than a relevance filter.

### 3.3 Provenance is required, dedupe is the bound, and the sweep is the release

**A tag with an empty `provenance` cannot be appended.** The failure it prevents is documented and
severe: a convenience path producing a relational outcome the history does not justify corrodes the
system *for players who never use it*. Binding every durable tag to the Key that caused it makes the
history queryable and makes `Key.causes[]` a biography rather than a write-only chain.

**`tag_append` dedupes on `(owner_ref, kind, key)` and refreshes in place.** That is not
housekeeping. A contested post generates one Grudge per passed-over candidate *per post*, refreshed —
not one per attempt, stacked. Without dedupe a popular post is an unbounded ramp on tag count, and
those values feed selection. With it, count is bounded by `candidates × posts`.

**At the accounting boundary every ledger drops its expired tags.** Durable tags (`ttl=None`) survive
sweeps **and survive succession** — a place remembers what was done to it after the officeholder is
gone, which is the residual the genre's best-documented demotion failure lacks.

> **Falsifier.** A test asserting no reachable tag in a seeded campaign has empty provenance, and no
> person exceeds `MEMORY_CAP`. Load-bearing on the game — the mechanic is *why did this actor turn on
> me* — not on the repository.

### 3.4 A tag may bias a decision; it may never substitute for one

**Binding on every selection function in this suite.** Wherever a decision function sums a relational
or leverage term alongside structural terms — a candidate's fitness, an action's appeal, a target's
hostility, a Slate item's salience — the relational term's contribution is **capped as a fraction of
the function's structural range**:

```
|relational terms|  ≤  RELATION_SHARE_MAX · (max structural term − min structural term)
```

The failure this prevents is documented and specific: relationship modifiers large enough to dissolve
structural conflict produce a game in which *you can generally succeed at things rulers historically
wanted to do and could not*, because opinion bonuses paper over the positional facts. **Some
conflicts must be positional and unbuyable.**

It binds hardest on custody (§5.2): a `Leverage` tag biases a holder toward the controller's
preferences; it never replaces them. A custodian who fully determined a holder's choices would make
custody strictly better than holding the post at a fraction of the exposure — the mechanic eating
itself.

**Memory is inside the cap, not beside it.** A person's misperception shifts their weighting; it
never overrides the board. `RELATION_SHARE_MAX` is declared in the exported params. **Reachability
bar: at the maximum reachable relational total, the structurally-worst option must still be unable to
outrank the structurally-best one.**

---

## 4. P-3 — Post

The delegation object. Acting *on behalf of* something at a tier requires a post that can be granted
and revoked; acting *within* is a claim on someone else's. Both stances need this object; neither
needs a second one.

```
Post
├── post_id       : str
├── kind          : head | governor | minister | commander | envoy | clerk   ← closed at six
├── tier_node     : the tier node where this post has authority
├── principal     : faction_id | post_id      who granted it, and who may revoke it
├── holder_id     : person_id | None          None = VACANT, and a vacancy is first-class
├── remit         : [module_id]               the option set this post unlocks
├── granted_season: int | None
├── term          : int | None                None = at pleasure
└── budget        : Gauge                     (P-4) — action count per season; §6.3
```

### 4.1 A vacancy is a state, not an absence

`holder_id = None` is the object that closes ED-IN-0201's gate. It is queryable, it is a demand
signal for generation, and it is why a faction that cannot find a head **stops acting** rather than
acting badly. That is a better failure state than any collapse procedure and needs no detection
mechanism: the gate reads the field.

**Recoverability is carried from v1 `05 §1.2` unchanged:** a seat node that cannot be lost means the
gate is always re-satisfiable, so a vacancy is a pause, not a death spiral.

**v2 addition:** the gate applies **per tier** (`05 §3`). A faction with a governor in one settlement
and no national post is a *local* faction — it acts at the settlement tier and not above. v1's single
peninsula-scale gate made every faction national or nothing.

### 4.2 Custody is a tag, not a field

Controlling a post-holder without deposing them is a five-source convergence in the precedent survey.
It is **not** a second identity field.

`Leverage(owner_ref=(post, post_id), key=<controller person_id>, provenance=<the Key that established it>)`

carries exactly what a `custodian_id` field would, plus a ttl, a provenance chain and a decay the
field would not have. Establishing custody is a contested action (`12 §3`); losing it is the tag
expiring or being stripped. **No new field.**

### 4.3 `remit` is how a person changes the option set

ED-IN-0201 clause 2 says the person shapes *which* action is chosen from the same option set with the
same information — and its own NERS constraint says that must not be a flat trait bonus on a
selection roll, because a flat shift is worth systematically more to a small pool than a large one.

`remit` satisfies both. A module is invocable only by a post whose remit names it. Two holders of the
same post get the same remit; two different post kinds get different remits; a holder's **convictions
and beliefs** rank the remit's contents (`05 §3`). Nothing adds a die; nothing shifts an obstacle.
**The choice differs; the odds do not.**

### 4.4 The player holds a post — and that is the entire player model

There is no player entity, no player faction flag and no player-only module anywhere in this suite.
**The player is a person, and they act by holding posts.**

| | |
|---|---|
| **What the player may do this season** | exactly the modules in the remit of the posts they hold, exactly as for any other holder — **filtered by the Slate** (`10`) to the scene budget |
| **What the player spends** | the `budget` gauge on those posts, exactly as for any other holder |
| **An unattended post** | the same module runs, with the holder's own `appeal`/preference supplying the choice |
| **How reach is gained** | by being appointed to, or claiming, more posts — routed through `04` like everyone else's |
| **How reach is lost** | audit, recall, succession, or the gate closing — the same four paths |

Three properties follow, and the third is the one worth the design:

1. **No special-casing.** A player-only branch is scripting drift by definition, and the surest way
   to grow one is to give the player a different object to act through.
2. **Delegation is free.** A player who holds three posts and attends to one has not lost the other
   two. That is the auto-resolution tier, and it is **the same module run headless**.
3. **One engine, several entry points.** The surveyed franchise whose fast path is a *different
   algorithm* from its played path spent two decades with a divergence exploited in both directions;
   the one whose three fidelities are the same engine resolving the same fixture did not. Because a
   played action and an unattended action here are the same module with the same pool, obstacle and
   ladder, **there is no divergence to calibrate** — only the *choice* differs, and that difference
   is the point. `10`'s below-the-line auto-resolution inherits this rule verbatim.

---

## 5. P-4 — Gauge

Every continuous quantity in the game. A Key is a typed one-shot emission — right for a flag,
structurally wrong for a value read continuously between emissions and decaying. Acceptance, order,
pressure, disposition, standing, exposure, **edge strain**, **Thread Sensitivity**, an accrual, a
budget: none of these *emit*, they *are*.

```
Gauge   (declared in references/descriptor_registry.yaml; instantiated per owner)
├── gauge_id   : str
├── owner_ref  : (entity_kind, entity_id)      including edge and bloc
├── scale      : one of the runtime four
├── floor, ceiling : float
├── lambda     : float in (0, 1]     the geometric decay coefficient
├── rest       : float               the value it decays toward
├── bands      : [(threshold, label)]  what the player is shown (E-2)
└── history    : [(season, delta, provenance_key_id)]
```

Three functions, deliberately: `gauge_deposit(gauge, delta, provenance)` — appends, **provenance
required**; `gauge_value(gauge, season)`; `gauge_band(gauge, season)` — **this is what a player
sees**. **There is no setter.**

### 5.1 Decay is geometric, never a saturating additive step

```
value(t+1) = rest + (value(t) − rest)·(1 − λ)  +  Σ deposits(t)
```

**The single most load-bearing arithmetic choice in the suite**, chosen against a measured failure. A
restoring term that saturates — one pulling back by *at most* a fixed step per season — is bounded
above by that step, so **any accrual larger than it pins the value at its ceiling and holds it
there**. That is not a tuning problem; it is a property of the shape, and it produces an
unrecoverable state from ordinary play.

A geometric restoring term has no such ceiling on its own strength. For a bounded per-season accrual
`a`, the fixed point is `rest + a/λ` — **finite for every λ ∈ (0,1] and every bounded `a`**. No value
of `a` pins the gauge, and settling time is `≈1/λ` seasons regardless of magnitude.

Consequences for free:

- **Contractivity is structural.** `propagation_spec_v1` AU-4 requires `decay()` to be a pure
  function of elapsed time for determinism, and §4.3 makes cross-tick convergence conditional on it
  being *strictly contractive*. `(1 − λ)` with `λ ∈ (0,1]` is strictly contractive by construction.
- **Every gauge is bounded** by `[floor, ceiling]`, clamped on read.
- **Monotonic response.** More deposit is never less value.
- **§2.3's `H_MIN` is computable from these fields alone**, which is why the hysteresis guard needs
  no campaign run.

> **Falsifier.** An arithmetic test, no campaign run, asserting for every declared gauge that
> `rest + max_seasonal_accrual/λ ≤ ceiling`. A gauge whose declared accrual sources exceed that fails
> **at declaration time**. Load-bearing on the game: it is the difference between a settlement that
> can recover and one that cannot.

### 5.2 Where gauges are used, and what each one retires

| Gauge instance | Owner | Retires (as a separate mechanism) |
|---|---|---|
| `disposition` | edge | a bespoke loyalty scalar per subsystem |
| **`strain`** *(v2)* | edge | a bespoke wear counter per relationship kind (§7.3) |
| `standing` | person | the public half of nine parallel personal meters |
| `exposure` | person | the private half — everything accrued by acting covertly |
| **`thread_sensitivity`** *(v2)* | person | a per-subsystem TS field; canon scales it 0–100 (`systems/overview/clock_registry_v30.md:72`) |
| `acceptance.legitimacy`, `acceptance.support` | place | per-settlement political acceptance |
| `condition.order`, `condition.prosperity`, `condition.defense` | place | the settlement stat block |
| `pressure` | place | the candidate-emission driver (`10`) |
| **`presence.<institution>`** *(v2)* | place | a bespoke Church/Guild/Warden reach field (`07 §4`) |
| `accrual.entitlement` | place | the levy channel's supply |
| **`progress`** *(v2)* | any project owner | a bespoke timer per ambition (`09 §2`) |
| **`cohesion`** *(v2)* | bloc | any second faction-like stat block on a bloc (`06 §3`) |
| `budget` | post | every proposed action economy in the corpus |

**Two personal meters, not nine.** One public (`standing`), one private (`exposure`). Nine bounded
meters differing only in their trigger lists is nine bars a player watches; the triggers were the
design, the meters were duplication. `thread_sensitivity` is a third **only because canon already
scales and gates on it** (§7.3) — it is cited, not invented.

### 5.3 Budget is a gauge, and it buys actions — never modifiers

A budget is an accrual with a spender. Making it the same primitive closes the *three rival accrual
clocks* problem structurally: one rate, one cap, one bifurcation analysis, several typed consumers.

**One budget point buys one attempt at one module.** It never converts into dice and never into an
obstacle shift.

The arithmetic that forces this: in the continuous engine an added die at a balanced check is worth
`≈0.204σ` at pool 5 against `≈0.115σ` at pool 18 — and the value is obstacle-dependent too, ranging
roughly `0.107σ`–`0.302σ` at pool 5 alone. A single currency spendable as a modifier is therefore
worth **about twice as much** on a small pool as a large one, and more once the obstacle varies. A
player who notices routes their budget wherever it pays. Buying *actions* keeps the budget out of the
resolution arithmetic entirely, which is also the simpler design.

> **Falsifier.** A test asserting no module contract declares a `budget:` whose cost is consumed
> inside a pool or obstacle expression. Load-bearing on the game: the difference between a budget and
> an exploit.

**v2 note:** the budget is **per post**, not per faction (`05 §3`). A faction's total action capacity
is therefore the sum over the posts it actually staffs, which is Jordan's 2026-07-13 ruling —
factions hold people, and it is the number of people and the weight of their positions that carry a
faction's value — expressed as arithmetic rather than as a sentence.

---

---


---

## 6. E-1 — `derive_ob`, the obstacle's owner

```python
def derive_ob(target_score: float, modifiers: float = 0.0) -> float:
    """The obstacle. Jordan, 2026-08-14: an obstacle rolled against a character or faction is
    their corresponding score/2 plus whatever specific modifiers exist for them in that instance."""
    return max(OB_MIN, target_score / 2.0 + modifiers)
```

It belongs beside `roll_pool` in `engine/autoload/dice_engine.py`, for a reason the corpus already
measured: the margin ladder is single-owned and guarded (`degree_from_net`), while the obstacle is
derived locally in most resolving subsystems and arrives at the roller as a bare parameter. **Ruling
the obstacle without giving it an owner predicts the same fork recurring**, and there is a measured
precedent in six private roll/degree implementations.

Three properties, each a defect avoided rather than a feature added:

1. **The result is fractional and stays fractional.** The ladder's contract says both operands may be
   fractional; every existing derivation site rounds or floors, against a ladder built to consume
   fractions. Producers correct when written stopped being correct when the ladder moved beneath
   them. A single owner cannot drift that way.
2. **Modifiers are σ-space, not obstacle-space.** A modifier reaches the roll through
   `sigma_leverage.net_boost` — a μ-shift scaled by `σ_N = 0.8·√Pool` — never as a flat addition to
   `derive_ob`'s output. A flat obstacle shift is worth more to a small pool than a large one, the
   same non-uniformity §5.3 rules out one level down. The `modifiers` argument is reserved for terms
   genuinely *properties of the target* — a fortification, a legal protection, **an incumbent's
   presence level** (`05 §4`) — not for the actor's advantages.
3. **The floor is `OB_MIN`**, so an advantage cannot drive the obstacle below the ruled minimum and
   create a cliff at the floor.

**It adds to the engine and repoints nothing.** The three existing obstacle-derivation sites whose
reconciliation is suspended are a different lane's question, and a greenfield module has no ratified
canon to overwrite.

**One leverage note, because it is the obvious objection.** Raising an attribute adds a die, worth
`≈0.204σ` at pool 5 against `≈0.115σ` at pool 18 — so capability investment is worth about 1.8× as
much to a weak actor as a strong one. That is **non-uniform in the correct direction**: self-damping,
and the shape a bounded system wants. It is a property of the continuous engine, recorded here so a
later reader does not mistake it for an unnoticed P-ii defect.

---

## 7. Edges: a shared container with per-kind semantics (change E, redesigned)

### 7.1 The prohibition this section was written against, and the three rulings on disk

`audit/2026-08-08-world-churn-audit/06_master_synthesis.md:552` (Part VI, **HELD not ratified** —
`:4`) prohibits **"a unified bond primitive"**: *"Three anti-unification rulings already on disk. The
real gap is **converters** (marriage-as-treaty, retainer-ripening) and a **shared Key surface**."*

The three, found and read rather than taken on summary:

| # | ruling | what it forbids |
|---|---|---|
| **R-1** | **ED-POL-11** — *"Patronage vs. Knot distinction. **Maintained.** Patronage is political/institutional; Knot is spiritual/personal. Use in separate contexts; **do not conflate**."* (`systems/factions/faction_politics_v30.md:1093`) | treating a Knot as a strong patronage tie, or either as a magnitude of the other |
| **R-2** | **PP-724 §0 Scope** — *"PC-NPC and NPC-NPC ties compose through shared participation in scenes but **do not collapse into one mechanic**."* (`systems/npcs/npc_relational_graph_v30.md:22`) | one mechanic spanning the PC↔NPC and NPC↔NPC layers |
| **R-3** | **PP-724 §3.3** — *"**Knot strain (PC-NPC) and edge strain (NPC-NPC) do not aggregate into one counter** — they are distinct state and resolved separately."* …*"Each relational edge (Knot or NPC-edge) is a **distinct binding**; events that affect a node propagate independently along each binding."* (`:162`, `:167`) | a single strain axis, or a single break rule, across binding kinds |

**All three forbid unifying *semantics*. None forbids sharing *storage*.** That distinction is what
§7.2 is built on, and it is the whole of the argument.

### 7.2 What is cut, and what is adopted — "may the best ideas win"

**v1's six-kind `relation` enum and this suite's own draft eight-kind table are CUT, superseded by
`systems/npcs/npc_relational_graph_v30.md` (PP-724, Class A, PROVISIONAL).** That document already
ships what change E was reaching for, and ships it better: **six canonical NPC↔NPC edge types**, each
with its own formation conditions, strain sources, capacity, break and rupture rules, decay, and
period precedent — plus a decision log arguing the taxonomy's closure on elegance grounds (`:669`).
Re-deriving a worse taxonomy to keep authorship is exactly the failure `00 §1` names.

| adopted from PP-724, cited not restated | `:46-56` |
|---|---|
| `sworn-bond` (symmetric) · `liege-vassal` (liege→vassal) · `kinship` (symmetric; asymmetric parent→child) · `patronage` (patron→client) · `rivalry` (negative valence) · `feud` (negative valence, hereditary) | the six types, strengths 1–3 |
| **kinship does not break by strain**; severance is an institutional act, and the *historical* kinship survives it | `:334-340` |
| **rivalry and feud are escalation tracks, not strain tracks** — they intensify or de-intensify, they do not "fail" | `:674` |
| **NPC↔NPC Disposition is DERIVED from edge state, never stored** — *"storing both edges + Disposition risks divergence"* | `:331-345`, `:675` |

**Two kinds are added, in a scope PP-724 does not cover** (it is explicitly NPC↔NPC only, `:22`):
`treaty` (faction ↔ faction) and `charter` (faction → place). These are *extensions into an
unoccupied scope*, not overrides. `treaty` replaces v1's `Debt`-tag-pair representation, which was
two representations of one relationship while faction enmity was already an edge.

**`client` is not shipped.** Endpoints are ordered, so `patronage(a→b)` read from b's end *is* the
client relation; a `client` row would be a perspective variant, which is `00 §1`'s under-distilled
failure. It is a query helper, never a row. Nothing is lost: every relationship a `client` row could
express is the `patronage` row it duplicates. PP-724 agrees — it ships `patronage` with a direction,
not a pair.

### 7.3 The container, and exactly what it does and does not unify

```
identity(edge)
├── endpoints : (entity_id, entity_id)   ORDERED where the kind is asymmetric
└── relation  : declared in references/form_registry.yaml, ONE ROW PER KIND

form(edge)
└── state     : from the set THIS KIND admits — declared per kind, never globally

gauges        : declared PER KIND. A kind that has no strain axis has no strain gauge.
tags          : what has passed between them, each with provenance — including a treaty's terms
```

| the container supplies | the container does NOT supply |
|---|---|
| an id, so an edge is a tag owner and a Key target like any entity | formation gates — **each kind's are its own** |
| one **provenance** rule and one **disclosure** contract | strain sources — **each kind's are its own, and they never sum** (R-3) |
| one **Key surface** — `edge.formed` / `edge.transitioned` — which is what Part VI says the real gap is | break and rupture rules — **each kind's are its own** |
| one **store**, so `causes[]` chains cross relationship kinds without a join table | a shared strain counter, a shared capacity, or a shared disposition derivation |

**The test the coordinator set: does a shared container make a Knot look like a strong `sworn`
edge?** No, and here is why it cannot.

| | `sworn-bond` (PP-724) | `knot` (canon, §7.4) |
|---|---|---|
| scope | NPC ↔ NPC | PC ↔ NPC — **a different layer** (R-2) |
| formation gate | edge formation conditions, PP-724 §3 | Disposition +5 **and** TS ≥ 30 **and** Bonds ≥ 5 **and** capacity **and** a roll |
| strain counter | edge strain, capacity 3/5/7 by strength | **its own** −5…+5 bond-strain gauge, tiered |
| do the two counters ever sum? | **never** (R-3, `:162`) | **never** |
| disposition | **derived** from edge state (`:331`) | **stored** — canon tracks PC↔NPC Disposition as a live track, and the formation gate reads it at +5 |
| end state | break, or escalate | **rupture**, Thread-structural, irreversible |
| is it in the taxonomy? | yes, type 1 of six | **NO. A Knot is a distinct binding kind and is not a row in PP-724's six.** |

The last two rows are the answer. A kind whose disposition is *stored* while another's is *derived*,
whose strain gauge is a different object with different bounds, and whose end state is a different
transition, is not a magnitude of the other. **The container holds them; it does not equate them.**

⚠ **This corrects a v1 defect, found by taking PP-724 seriously.** v1 put a `disposition` **Gauge on
every edge**. For NPC↔NPC pairs that stores a value PP-724 derives — and deriving it is not merely
PP-724's preference, it is **this suite's own write rule**: a stored NPC↔NPC disposition is an
aggregate over edge strengths, and no aggregate is ever written (§2.1, AU-1). **v1 violated its own
rule and PP-724 caught it.** Disposition is therefore stored for PC↔NPC (canon owns that track) and
derived for NPC↔NPC (`:331-345`). Per-kind semantics, in the substrate, doing real work.

### 7.4 Converters — the gap Part VI actually names

*"The real gap is **converters** (marriage-as-treaty, retainer-ripening)."* Agreed, and it is the one
place this design adds machinery rather than adopting it.

**A converter is a form transition (§2) that CREATES an edge of another kind. It never merges two
kinds and never moves state between them.**

```yaml
converter: marriage_to_treaty
source_kind: kinship            # the marriage edge
creates_kind: treaty            # between the two houses' factions
gate: <both endpoints hold posts in distinct factions AND the kinship edge is cooperative>
source_after: unchanged         # THE SOURCE EDGE PERSISTS. Nothing is consumed.
emits: edge.formed
reversible: false               # a treaty is ended by its own rules, not by un-converting
```

| converter | source | creates | why it is a conversion and not a merge |
|---|---|---|---|
| `marriage_to_treaty` | `kinship` | `treaty` | the kin tie and the treaty then have **separate strain, separate break rules and separate parties**. The marriage surviving a denounced treaty is the interesting case, and only separate objects can express it |
| `retainer_ripening` | `patronage` at sustained strength | `sworn-bond` | PP-724 ships both types with different semantics; ripening is the *transition between them*, which neither type owns |
| `rivalry_to_feud` | `rivalry` | `feud` | PP-724 §2.6 already owns the escalation; the converter names it as one, so it is not re-implemented |

**A converter may not produce a `knot`.** Knot formation is canon's procedure (§7.5) with its own
gates and its own roll. Ripening a patronage into a Knot would be exactly the conflation R-1
forbids.

### 7.5 The Knot — canon, cited, not designed here

**A Knot is not a strong relationship and must not be modelled as one.** It is Thread-constituted:
gated on Thread Sensitivity, carrying its own strain axis, and **rupturing rather than breaking**.
*Knots are constitutive, not contractual.* Everything below is **read from canon and cited**; this
suite designs none of it, invents no number, and adds it to no taxonomy.

| canon fact | value | citation |
|---|---|---|
| formation gate — disposition | Disposition **+5** with the target | `systems/fieldwork/knots_v30.md:68` (§3.1 item 1) |
| formation gate — Thread contact | **either party TS ≥ 30** | `knots_v30.md:69`; scale 0–100 hard cap per `systems/overview/clock_registry_v30.md:72` |
| formation gate — capacity | **current Knot count < `floor(Bonds/2) + 1`** | `knots_v30.md:70`, restated `:31` and `:38` (PP-632) — **this is the canonical cap on Knots per person** |
| formation gate — uniqueness | no existing Knot with this NPC | `knots_v30.md:71` |
| formation gate — Bonds | **PC Bonds ≥ 5** (Bonds is an attribute 1–7; it does *not* cap Disposition) | `knots_v30.md:72` (ED-912); `:28`, `:40` |
| formation roll | **Spirit × 2 + History (Relationships), TN 7, Ob 2** | `knots_v30.md:76` (§3.2) |
| outcome by degree | Overwhelming → Close tier, strain −2 · Success → Distant, strain 0 · Partial → no Knot, Disposition holds +5 · Failure → no Knot, Disposition drops to +4 | `knots_v30.md:78-83` |
| tiers | **Distant** (strain −2…+5, starts 0) · **Close** (strain −5…+5, starts −2) | `knots_v30.md:49-52` (ED-912) |
| rupture threshold | **strain +5, both tiers**, checked at Accounting | `knots_v30.md:54`, `:180` |
| tempered | **strain −5, Close only** — absorbs the next rupture trigger once, then resets to 0 | `knots_v30.md:54`, `:180` |
| strain decay | at Accounting, **−1 if no strain was added that season AND Disposition ≥ +3** | `knots_v30.md:170` |
| strain sources | remote Thread-Read **+1/use** · Composure buffer **+1/use** · counsel re-query **+1** (first free) · FR Lock/Dissolution near a partner **+1** · witnessing a Conviction Scar fire in the partner **+1 at Accounting** · Disposition < +3 for two consecutive seasons **+1 at Accounting** · each opposing-operations event **+1** | `knots_v30.md:160-168` (§5) |
| break consequence | Disposition → **−3** (floor −5) · **both partners take 4 Composure** · all Knot-mediated benefits cease · the capacity slot frees | `knots_v30.md:184-188` |
| **conviction scar** | a **Close** Knot that broke **from positive strain** → **Conviction Scar +1 to both partners** | `knots_v30.md:189` |
| rupture triggers (bypass strain) | public citation of private counsel · partner's death · FR Dissolution targeting the partner (**+1 Wound, no armour**) · permanent Conviction shift to an opposing Conviction · player dissolution at Accounting (**2 Composure**) | `knots_v30.md:193-201` |
| ⚠ **not settled** | mandatory **−1 Coherence on rupture** is flagged **[UNVERIFIED post-ED-912]** — its source PP-632 was struck and ED-912 did not restate it | `knots_v30.md:203`; the sim carries the same warning at `systems/fieldwork/sim/knots.py:53-56` |

**How it lands on the container with no new primitive and no shared semantics:**

| canon element | where it lands |
|---|---|
| the Knot itself | an **edge**, `relation: knot`, **its own registry row**, outside PP-724's six |
| Distant / Close | a `tier` value in the edge's **form**, exactly as a place carries one; the row declares the strain range each tier admits |
| strain | **a Gauge private to this kind**, `λ` chosen so canon's "−1 per quiet season at Disposition ≥ +3" *is* the decay rather than a special case. It never sums with edge strain (R-3) |
| rupture at +5 | a **form transition** `intact → ruptured`, `gate: strain ≥ 5`, `reversible: false` — canon's own irreversibility is why no hysteresis is required |
| tempered at −5 | `intact → tempered`, and `tempered → intact` on absorbing a trigger — **a reversible pair, therefore requiring a declared hysteresis band** (§2.3). Canon states the reset (`:54`) and **states no band**. **v2 records this as a gap and does not fill it** — the band is an FI-lane canon question, not a number this suite may invent |
| the capacity cap | a **gate** reading `floor(Bonds/2) + 1`, counted from the person's `knot` edges — no stored counter |
| conviction scar | a **Tag** on the person, `kind: Precedent`, provenance = the rupture Key; the conviction name resolves through `descriptors.resolve_conviction` and **raises** on an unknown name (§1.2) |
| a Knot's disposition | **stored**, not derived — canon's PC↔NPC Disposition track, read by the formation gate at +5 |

**Q-6 stands open** (`00 §5.1`): nothing here depends on the unverified −1 Coherence rule.

*Emergent possibility lost if the shared container were cut and each kind given its own store:*
`causes[]` could not chain across relationship kinds, so a treaty denounced because of a feud
inherited through a marriage would be three unlinked records — and that chain is the mechanism the
whole suite calls a biography.
---

## 8. E-2 — The disclosure block

There is no GM. Nobody narrates why a candidate was passed over, why a faction declined to act, or
why a place's pressure rose. The only surveyed evidence bearing on that constraint is a game whose
social layer was loved and whose tactical math was resented *in the same title*, separated by nothing
but whether the model was visible — and whose community fix **exposed the models rather than changing
them**.

> **Publish every input. Publish a band, never a number. Never publish the trigger point.**

Asymmetric on purpose. Five independent sources keep the threshold hidden; four say legibility is
what separates a celebrated system from a resented one. Publishing the trigger destroys the mechanic;
publishing the inputs is what makes the outcome feel principled rather than arbitrary.

```yaml
disclosure:
  - of: pressure
    inputs: published          # every deposit and its provenance is inspectable
    presentation: band         # the player sees "strained", not 6.4
    trigger: hidden            # the player is never told the draw threshold
```

**It is a registry field, not documentation.** A state row without a `disclosure:` block fails the
contract check.

**Three v2 consequences.** (1) A **form transition's gate is a trigger**, so its threshold is hidden
while its inputs are published — the player can see every gauge feeding a settlement's growth and
cannot see the number. (2) **A forecast is a trigger published in instalments** (§2.2), which is why
the imminence-Key prohibition and this contract are the same rule seen from two sides. (3) **The
caste gate is the one ruled exception** (`00 §6` principle 5, `04`): it is an *input*, published in
full, because concealing it would make the system's central injustice invisible.

> **Falsifier.** A test asserting every state row carries a disclosure block, none sets
> `trigger: published`, and no emitted key type carries a field whose value is a future state — with
> the caste-gate row as the single declared, named exemption.

---

## 9. The wrapper — a herald that populates `targets[]`, not a distributor

### 9.1 Why this is not the prohibited "world director"

Part VI's strongest negative (`06_master_synthesis.md:551`, **held not ratified**) is *"a distributor
wrapper or 'world director'. Distribution is `targets[]` data plus subscription; a router module is
the god-loop with better PR."* Part III of the same document answers the wrapper-vs-mesh fork and
**refutes both pure forms**, leaving one criterion (`:394`):

> **Aggregate-crossing detection belongs to the aggregator; effect magnitude belongs to the effect's
> owner.**

**This suite adopts that criterion, and the wrapper is reframed to it rather than defended.** Three
assignments follow, and they are what the wrapper is:

1. **The boundary is a herald.** It publishes what it **already computes**. It decides nothing and
   routes nothing. A per-subsystem wrapper is not a central router because there is no central one:
   each wrapper sees only Keys addressed to its own modules, holds no map of other subsystems, and
   cannot reach one — cross-subsystem needs go through `composition.require(role)` (W-2), which is a
   registry lookup, not a dispatch table.
2. **Every effect rule stays local.** Whether a fact scars a person depends on that person's
   convictions; whether a place complies depends on its own acceptance. **The wrapper computes no
   effect magnitude.** It never holds a rule that belongs to a receiver, which is the property that
   separates it from a director.
3. **Distribution is data, not code.** The router a wrapper would centralise **already exists as
   schema** — the five-role `targets[]` vocabulary. **One Key whose `targets[]` names every affected
   place *is* the distribution mechanism.** v1's W-3 was already exactly this; what changes is that
   it is now the wrapper's *definition* rather than one of its rules.

**So the wrapper's whole job is: drain, invoke, and populate `targets[]`.** If a future version of
this document describes it as routing, deciding, or holding a receiver's rule, that version has built
the prohibited thing and this paragraph is the falsifier.

### 9.2 Shape

```
                 engine_clock.run_tick
                          │
        SEASON_TICK ── ACTION ── ACCOUNTING_BOUNDARY
                          │
                    subsystem wrapper          ← resolved by composition role, never imported
                     ├── in:   drain the Keys addressed to this subsystem's modules
                     ├── run:  invoke modules; modules touch primitives and NOTHING else
                     └── out:  publish — at most one Key per resolved module, causes[] cited
                               honestly, targets[] populated at the granularity of each receiver
```

| # | Rule | The failure it prevents |
|---|---|---|
| W-1 | A module never publishes. It returns a result; the wrapper publishes. | Emission scattered across a subsystem is how `causes[]` chains get fabricated or dropped |
| W-2 | A module never imports another subsystem. Cross-subsystem needs resolve through `composition.require(role)`. | The package cycle a function-local import hides from the interpreter without removing |
| W-3 | Fan-out is **one Key with N populated targets, never N Keys** — this *is* the distribution mechanism (§9.1.3). | The re-entrancy meter counts *responses*, not target-array width, so wide legitimate delivery must not look like runaway |
| W-4 | Any Key naming a derived aggregate in `targets[]` carries `stat_deltas: {}` for that target. | Writing an aggregate, which the write rule forbids and the generic per-observer path would do silently |
| **W-5** *(v2)* | A module's result may name a form transition; the wrapper applies it and publishes `form.transitioned`. A module never mutates `form` itself. | Otherwise the fourth write leaf is the one leaf with no single owner, and §2.4's "grep over one field" stops being true |
| **W-6** *(v2)* | **A subscription with no rule content is not declared.** A `consumes:` row must name what the consumer *does* with the Key. | Part VI `:412` — *"a subscription with no rule content is decoration"*. It is also how a `consumes:` list becomes a fiction nobody executes |

**Populating `targets[]` is where granularity increases.** A peninsula-scale Key addressed to eight
places carries eight `targets[]` entries, each with the deltas *that place* receives — not one delta
the receiver must interpret. A sparse `targets[]` delivers blind, the documented failure of the eight
declared down-seams that populate nothing.

⚠ **The double-count hazard is open and this suite does not resolve it** (`00` Q-5). Every wrapper
here declares, per emission, **which of its two channels carries the magnitude — and never both.**

### 9.3 ⚠ The substrate supplies NO LATENCY — binding on everything downstream

Verified against the tree by that audit's adversarial review and **filed as open ruling J-N**
(`06_master_synthesis.md:532`, `:637`):

- `schedule_emission` increments depth **only when already draining**; `drain_tick` has **zero
  production callers**; the live loop calls `accounting_boundary()` then `next_tick()` directly.
- `next_tick` **raises `TerminationBreach` if the queue is non-empty** — there is **no cross-season
  carry**.
- `DEFAULT_CASCADE_DEPTH_MAX = 0` is a **provisional safety bound**, self-labelled, sized to the
  single current emitter.

> **The guard prevents cascades outright; it does not schedule them late.** One-hop-per-season
> latency is **not a property this design has** — it is a mechanism someone would have to build.

**What that forbids, on this page and every page after it:**

| forbidden | the correct shape |
|---|---|
| a module reacting to a Key by publishing a Key that **lands next season** | there is no such transport |
| a form transition, project or event designed as "posted to, fires later" | it **reads state at the boundary** and fires because the world *is* a certain way |
| describing the wrapper as providing propagation over time | it propagates **within a tick**, and nothing else |

**Anything that spans seasons does so by reading state, never by carrying an emission.** That is why
every gauge decays on a *pure function of elapsed time* (§5.1) and why every form gate reads current
state (§2.2): those are the only two cross-season channels the substrate actually has. **J-N is the
ruling that would change this**, and if it rules for reactive chains, this section is what to revisit.

### 9.4 ⚠ This page leans on Key consumption — J-O

`06_master_synthesis.md:533` files **J-O**: *does the Key mesh deserve promotion from telemetry spine
to churn engine at all*, the alternative being **Keys as an append-only telemetry and causality log,
with churn driven at the boundary directly**. The audit records that the alternative *"is never
weighed anywhere"*, and that J-O can invalidate a whole programme rather than one item.

**Stated so the affected parts are identifiable if J-O rules the other way:**

| what depends on Key **consumption** | survives J-O ruling "telemetry only"? |
|---|---|
| `consumes:` rows in every module contract; the wrapper's `in:` drain (§9.2) | **no** — these become boundary reads |
| `causes[]` as the provenance chain, and `Tag.provenance` pointing at a Key | **yes** — that is telemetry and causality, which is what the alternative keeps |
| every **form transition** (§2.2) — gated on *state*, not on a received Key | **yes** |
| every **gauge** deposit and its decay (§5.1) | **yes** |
| the emission side (`form.transitioned`, `edge.formed`, …) | **yes** as a log; only the *reaction* half is at risk |

**The substrate is therefore robust to J-O and the module wiring is not.** That is worth stating
plainly: four primitives, four write leaves and the decay law would all survive a ruling that
retires the consumer mesh; §12's `consumes:` lists would be rewritten as boundary reads. **J-O is
not resolved here and this suite takes no position on it.**

---

## 10. What is deliberately not a primitive, and what was cut

A cut list is only credible next to what it refuses to add — and under *"may the best ideas win"* it
must also record what was cut because something on disk beat it.

| Considered | Verdict | Why |
|---|---|---|
| a separate **Accrual** primitive | folded into Gauge | an accrual is a gauge with a positive rest and a rate; a budget is an accrual with a spender |
| a separate **Standing/rank** primitive | folded into Gauge | a rank ladder is a bounded personal meter with bands; keeping it separate produced nine parallel meters |
| `custodian_id` as a **field on Post** | folded into Tag | §4.2 — a field carries less (no ttl, no provenance, no decay) at the same conceptual cost |
| a **role** string on Person | rejected | §1.4 — `posts` is derived; there is no field to collide in |
| a **Compact** tag family | rejected | a recurring term-limited claim is `Debt(recurs=True, ttl=term)` |
| a **Knot** primitive | rejected | §7.5 — it is an edge with its own registry row, its own gates and its own private strain gauge. A sixth stored kind for one canon mechanic is how a substrate stops being one |
| **a v2-invented relation taxonomy** | **CUT, superseded by PP-724** | §7.2. Six period-grounded NPC↔NPC types with per-type semantics and a decision log already exist on disk. Rebuilding a worse one to keep authorship is the elegance failure, whoever wrote it |
| a **`client`** relation kind | rejected | §7.2 — a reading direction, not a row. PP-724 agrees: `patronage` ships with a direction, not a pair |
| a **stored NPC↔NPC disposition** | **CUT** | §7.3 — it is an aggregate over edge strengths, and no aggregate is ever written. PP-724 `:331-345` derives it, and v1 violated its own rule here |
| a **Memory** primitive | rejected; it is a **Tag kind** | §3.1 — a primitive would need its own store, sweep and provenance rule, all of which Tag already has |
| a **salience** stored field | rejected | §3.2 — derived at read from `value`, `created_season` and one declared `λ_mem` |
| a **second decay law** | rejected | §3.2, §5.1 — one geometric law, several consumers |
| a **cross-season emission carry** | **rejected as non-existent, not as unwanted** | §9.3 — the transport is not in the tree. Designing on it would be designing on a mechanism nobody built (**J-N**) |
| a **second resolver** | rejected | the only surveyed franchise with two resolution paths is also the only one with a two-decade unfixed divergence, exploited in both directions |
| a **view** primitive | rejected | disclosure stores nothing and resolves nothing; it is a declaration attached to state (E-2), which is what makes it checkable |
| a **central distributor / world director** | rejected, and the wrapper reframed | §9.1 — the wrapper populates `targets[]` and holds no receiver's rule |

---

## 11. What the player actually touches at this layer

**Almost nothing, and that is the design** (`00 §2`). This document is the richest layer in the suite
and the thinnest surface. Everything below is **read-only**; the substrate exposes **zero verbs**.

| what the player touches | how it reaches them | how often |
|---|---|---|
| a gauge's **band** — never its number | `gauge_band`, on a Slate item or a place summary | whenever the item they chose is on screen |
| the **posts they hold**, their remit and their remaining **budget** — disclosed `exact`, because these are inputs to a decision they are making now | the post list | once a season |
| a tag's **existence and provenance** — *why did this actor turn on me* | inspection from a Slate item | on demand, never pushed |

| what the player never touches |
|---|
| creating, editing or deleting an **entity**, an **edge** or a **bloc** |
| firing a **form transition** — every one is a gate the engine evaluates |
| running a **converter** (§7.4) — a marriage becoming a treaty is something they *learn about* |
| appending a **tag** or depositing into a **gauge** directly |
| a gauge's exact **value**, any transition's **threshold**, or any **forecast** of either (§8) |
| **strain**, **salience**, **divergence**, **presence levels** — substrate, surfaced only as a situation |

**Substrate objects on this page: 6 entity kinds · 6 tag kinds · 6 adopted relation kinds + 2 scope
extensions + Knot held separately · 3 converters · 4 primitives · 2 extensions. Surface affordances:
3 reads, 0 verbs.** If a later document's surface table is longer than its substrate table, that
document has the ratio backwards.

---

## 12. Module contracts — the substrate's own

Per W-6, **every `consumes:` row below names what the consumer does with the Key**; the substrate's
own modules consume nothing, and none is declared speculatively.

```yaml
- module: substrate.entity
  parent: substrate
  class: substrate
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: derivation
  remit: []                      # not invocable; a store
  budget: null
  consumes: []
  emits: [{type: person.generated, terminal: false}]
  state:
    - {name: entity, bucket: entity, writable: false, owner: substrate.entity}
  form: []                       # the store declares the buckets; it transitions nothing
  transitions: []
  disclosure:
    - {of: entity, inputs: published, presentation: exact, trigger: hidden}

- module: substrate.form
  parent: substrate
  class: substrate
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: gate                 # every transition is a gate; §2.2
  remit: []                      # applied by the wrapper (W-5), never invoked by a post
  budget: null
  consumes: []                   # gates read STATE, never a received Key (§9.3)
  emits: [{type: form.transitioned, terminal: false}]   # a crossing FACT, never a forecast
  state:
    - {name: form, bucket: entity, writable: true, owner: substrate.form}
  form:
    - {entity_kind: person,  field: life_stage}
    - {entity_kind: person,  field: capability}
    - {entity_kind: person,  field: traits}
    - {entity_kind: place,   field: kind}
    - {entity_kind: place,   field: tier}
    - {entity_kind: place,   field: facilities}
    - {entity_kind: place,   field: presences}
    - {entity_kind: faction, field: posture}
    - {entity_kind: edge,    field: state}
    - {entity_kind: edge,    field: tier}      # Knot Distant/Close only; §7.5
    - {entity_kind: unit,    field: unit_kind}
    - {entity_kind: unit,    field: assignment}
    - {entity_kind: bloc,    field: members}
    - {entity_kind: bloc,    field: state}
  transitions: [ALL declared rows in references/form_registry.yaml]
  disclosure:
    - {of: form, inputs: published, presentation: exact, trigger: hidden}

- module: substrate.ledger
  parent: substrate
  class: substrate
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: derivation
  remit: []
  budget: null
  consumes: []
  emits: []
  state:
    - {name: tag, bucket: tag, writable: true, owner: substrate.ledger}
  form: []
  transitions: []
  disclosure:
    - {of: tag, inputs: published, presentation: exact, trigger: hidden}

# ONE container, PER-KIND semantics. Every field below that varies by kind is declared in the
# kind's own registry row, NOT here. §7.3.
- module: substrate.edge
  parent: substrate
  class: substrate
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: gate
  remit: []
  budget: null
  consumes: []
  emits:
    - {type: edge.formed, terminal: false}
    - {type: edge.transitioned, terminal: false}
  state:
    # strain is declared PER KIND. A kind with no strain axis (kinship, per PP-724 :334) has none,
    # and no two kinds' strain ever sums into one counter (PP-724 :162).
    - {name: edge.strain.<kind>, bucket: gauge, writable: true, owner: substrate.edge}
    # PC<->NPC disposition is STORED (canon's track). NPC<->NPC disposition is DERIVED from edge
    # state and is NOT a state row here (PP-724 :331-345; O-3).
    - {name: edge.disposition.pc_npc, bucket: gauge, writable: true, owner: substrate.edge}
  form:
    - {entity_kind: edge, field: state}
    - {entity_kind: edge, field: tier}
  transitions:
    - knot.intact_to_ruptured        # gate: strain >= 5; reversible: false  (knots_v30 :180)
    - knot.intact_to_tempered        # gate: strain <= -5, Close only        (knots_v30 :54)
    - knot.tempered_to_intact        # reversible pair -> hysteresis REQUIRED; band UNSTATED in canon
    - kinship.cooperative_to_strained
    - kinship.to_severed             # institutional act, not strain        (PP-724 :334-340)
    - patronage.to_sworn_bond        # converter: retainer_ripening         (§7.4)
    - kinship.to_treaty              # converter: marriage_to_treaty        (§7.4)
    - rivalry.to_feud                # converter: PP-724 §2.6 escalation    (§7.4)
  disclosure:
    - {of: edge.strain.<kind>, inputs: published, presentation: band, trigger: hidden}
    - {of: edge.disposition.pc_npc, inputs: published, presentation: band, trigger: hidden}

- module: substrate.post
  parent: substrate
  class: substrate
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
  form: []
  transitions: []
  disclosure:
    - {of: post, inputs: published, presentation: exact, trigger: hidden}
    - {of: post.budget, inputs: published, presentation: exact, trigger: hidden}

- module: substrate.gauge
  parent: substrate
  class: substrate
  scales: [personal, settlement, territory, peninsula]
  tier: null
  resolver: accrual
  remit: []
  budget: null
  consumes: []
  emits: []
  state:
    - {name: gauge, bucket: gauge, writable: true, owner: substrate.gauge}
  form: []
  transitions: []
  disclosure:
    - {of: gauge, inputs: published, presentation: band, trigger: hidden}
```

`substrate.post`'s two rows disclose **exact**, not band: a post's holder and a budget's remaining
points are things the player acts on directly this season, and hiding them would obscure an input
rather than a threshold. Bands are for values whose precise magnitude is not a decision the player
makes.

**Note what is absent from `substrate.edge`:** a shared strain counter, a shared capacity, a shared
break rule, and any NPC↔NPC disposition row. Their absence is the container's compliance with R-1,
R-2 and R-3, expressed in the contract rather than promised in prose.

---

## 13. Property audit

**Scope, and the honest limit.** **Nothing in this document rolls.** `substrate.entity`,
`substrate.ledger` and `substrate.gauge` are stores; `substrate.form`, `substrate.edge` and
`substrate.post` are gates; `derive_ob` is a derivation *consumed by* rollers elsewhere and is not
itself a resolution. **No N/R/S/E verdict is offered for a store or a gate** — manufacturing one for
state with no draw is the error the methodology explicitly names, and v1 was right to refuse it.
What is offered instead is the two properties that *do* apply, plus every loop and gate stated with
its bound. (Canon's Knot **formation** rolls — `Spirit × 2 + History (Relationships)`, TN 7, Ob 2 —
but that roll is canon's, at `knots_v30.md:76`, and auditing it is the FI lane's job, not this
page's.)

Above that sits `00 §0.1`: **a resolution-scoped audit cannot ask whether a design expresses the
game.** This page could pass every property below and still be the wrong substrate. The instrument
for that question is the elegance criterion, and its answers here are the one-line loss statements,
the §10 cut list and the `## Overrides` block — judgments, not checks.

| property | verdict | reasoning |
|---|---|---|
| **P-iii** bounded, monotonic | **pass, and it is the strongest claim in the suite** | every gauge is bounded by declared floor and ceiling and restores geometrically, so the fixed point `rest + a/λ` is finite for every bounded accrual and every `λ ∈ (0,1]`. Checked **at load time** against the registry with no campaign run (§5.1). Monotone response is structural: more deposit is never less value. Form is bounded because every form field's value set is enumerated in the registry |
| **P-v** right engine | **pass** | four resolvers, and every module here is `gate`, `accrual` or `derivation`. Nothing on this page is uncertain and nothing on this page rolls. **Every form transition is a gate on purpose** (§2.2): the uncertainty was in getting the gauges to the threshold, and re-rolling at the threshold charges for it twice |

### 13.1 Loops, each with its bound

| loop | sign | bound | gain |
|---|---|---|---|
| gauge deposit → band → module gating → deposit | positive | the fixed point `rest + a/λ`, checked at declaration (§5.1) | **unmeasured**; campaign-reachable, so measurable with a control, and it should be measured before any writer lands |
| form transition ↔ its reverse | oscillatory | **`θ↑ − θ↓ ≥ H_MIN` plus `dwell ≥ D`, checked at load (§2.3)** | **bounded arithmetically** — the only loop on this page with a proved bound, and the reason hysteresis is mandatory rather than advised |
| Knot strain → rupture → conviction scar → conviction weight → behaviour → strain | positive | **terminating**: rupture is `reversible: false`, so the edge leaves the loop permanently. Strain is gauge-bounded −5…+5 per tier (`knots_v30.md:49-52`) | **unmeasured**, and it is **canon's loop, not this suite's** — the FI lane inherits the measurement obligation |
| NPC↔NPC edge strain → derived disposition → behaviour → strain | positive | per-kind capacity (PP-724 `:673`); kinship cannot break by strain at all (`:334`); rivalry/feud escalate rather than accumulate toward break (`:674`) | **unmeasured** — and note that the three kinds are bounded by **three different mechanisms**, which is the per-kind semantics doing its job rather than a gap |
| **do the two strain loops above ever couple?** | — | **no. By R-3 they never sum.** A node in both loops takes both effects independently (PP-724 `:162-167`) | **not a loop** — this row exists because a reader will ask, and the answer is the anti-unification property, verified in §12's contract by the absence of a shared counter |
| memory salience → weighting → behaviour → new perception → memory | positive | **`MEMORY_CAP` top-K at the sweep, plus geometric salience decay, plus `RELATION_SHARE_MAX`** (§3.2, §3.4) | **unmeasured**. Three independent bounds is not a measured gain, and this page does not claim it is |
| tag append → selection → outcome → tag append | positive | dedupe on `(owner, kind, key)` bounds count by `candidates × posts`; magnitude bounded by the gauge the value deposits into (§3.3) | **unmeasured** |
| **a Key-driven cascade within a season** | — | **`DEFAULT_CASCADE_DEPTH_MAX = 0`** — the guard **prevents cascades outright** rather than pacing them (§9.3) | **not a loop today.** If **J-N** rules for reactive chains, this row becomes a real loop with no bound yet, and §9.3 is what to revisit |

### 13.2 Gates, each with what it reads

| gate | reads | fails to |
|---|---|---|
| tag provenance non-empty | the append call | a refusal at append time |
| form transition gate | gauges, tags, form, identity — **never a roll, never a received Key** | no transition; the entity stays as it is |
| hysteresis band | the registry, at load | **load failure**, not a runtime surprise |
| vacancy (`holder_id is None`) | the post | the faction does not act at that tier (`05 §1`) |
| `remit` | the post's remit list | the module is not in the option set — not a penalty, an absence |
| Knot capacity `< floor(Bonds/2) + 1` | the person's `knot` edges, counted (no stored counter) | formation is unavailable (`knots_v30.md:70`) |
| Knot Thread contact `TS ≥ 30` (either party) | the person gauge, 0–100 | formation is unavailable (`knots_v30.md:69`) |
| converter gate (§7.4) | both endpoints' posts, factions and the source edge's state | no new edge; the source edge is untouched either way |
| disclosure block present | the registry, at contract check | the contract check fails |
| `consumes:` row has rule content (W-6) | the contract | the row is not declared |

### 13.3 The four qualitative verdicts, applied to the substrate rather than to a resolver

**Necessary** — four primitives, six entity kinds, six tag kinds. The relation taxonomy is **adopted,
not invented**, so its necessity argument is PP-724's own decision log (`:669`) rather than a claim
this page has to make; the two additions (`treaty`, `charter`) occupy a scope PP-724 declares out of
bounds. §10 records nine candidates refused, three of them cut because something on disk beat them.
**Robust** — the two failure directions the corpus measured are closed by arithmetic: an
unrecoverable pinned gauge by the geometric law, and a flickering threshold by the hysteresis band.
Both are load-time checks. A third, the substrate quietly acquiring a latency it does not have, is
closed by §9.3 stating the absence rather than assuming the presence. **Smooth** — one decay law, one
obstacle owner, one disclosure contract, one write rule with four leaves, one registry for the
mutable-shape axis, one Key surface for every binding kind. **Elegant** — six modules, one new
registry from this page, no branch on any entity's identity anywhere, and a player surface of three
reads and zero verbs. The honest deduction: **the edge container is the one object on this page whose
elegance is contested**, and §7 argues it rather than assuming it.
