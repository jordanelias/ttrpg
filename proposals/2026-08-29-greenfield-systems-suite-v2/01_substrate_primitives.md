# 01 — Substrate: four primitives, a form bucket, four write leaves, one herald shape

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · `engine/substrate/{descriptors,composition,keys}.py` ·
## `engine/autoload/dice_engine.py` · `systems/npcs/npc_relational_graph_v30.md` (PP-724) ·
## `systems/fieldwork/knots_v30.md` · `audit/2026-08-08-world-churn-audit/06_master_synthesis.md`
## Continues in: [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) — §§7–13

Everything in this suite is a composition of what is on this page. If a later document needs a fifth
kind of stored thing, that is a defect in this page, not a licence to add a field somewhere else.

**Everything on this page is `substrate`** in the sense of `00 §2.1`, without exception. §11 (part 2)
is the whole player-facing surface of both parts: three read-only affordances and zero verbs.

**This document is in two parts, in reading order** (`CLAUDE.md` §4): **part 1** — the four
primitives, the form bucket and its transitions, and `derive_ob` with its commensurability gate
(§§1–6). **[Part 2](01_substrate_primitives_part2.md)** — the edge container and the Knot, disclosure,
the herald, the cut list, the player surface, the module contracts and the property audit (§§7–13).
Section numbers run continuously across both.

## Overrides

Listed, tiered and argued, per the suite's one hard rule: **a silent override is the corpus disease
this suite exists to stop.** `00 §5.3` collects these so Jordan can veto them individually.

| # | What is overridden | Tier | Why |
|---|---|---|---|
| **O-1** | v1 `01 §1`'s "identity is immutable **and carries** `place.kind` / `person.capability`" | this suite's own v1 | it made settlements ungrowable and characters unprogressable. Corrected by the form bucket (§1–§2), not loosened |
| **O-2** | v1's closed six-member `relation` enum, **and this suite's own draft eight-kind table** | this suite's own v1 and draft | **cut, superseded by PP-724** (`systems/npcs/npc_relational_graph_v30.md`), which already ships six NPC↔NPC edge types with per-type semantics and a decision log. §7.2 |
| **O-3** | v1's `disposition` **Gauge on every edge** | this suite's own v1 | for NPC↔NPC pairs that stores an aggregate over edge strengths, which v1's own write rule forbids. PP-724 `:331-345` derives it. §7.3 |
| **O-4** | PP-724 §13's *"relational edges file (separate)"* storage decision | ratified-adjacent (Class A, **PROVISIONAL**) | edges become entities in the general store rather than an NPC-only file, so one provenance rule, one disclosure contract and **one Key surface** cover every binding kind — which is what Part VI asks for. **Only storage moves; every per-kind semantic stays where PP-724 put it.** §7.3 |
| **O-5** | v1 `01 §7`'s **"distributor"** framing of the subsystem wrapper | this suite's own v1 | reframed to Part III's herald criterion: it populates `targets[]` and routes nothing. §9.1 |
| **O-6** | **this document's own v2 draft `Memory` tag kind** | this suite's own v2 draft | **cut, and `Holding` admitted in its place.** A Memory is a Holding field-for-field, and the one thing `Memory` was justified by — carrying a **false picture** — is the one thing `key`+`value` cannot express, because neither slot can say *what* is misremembered. A `prop_id` whose proposition fails to obtain can. Adopted from `proposals/2026-08-18-epistemic-propositions-and-provenance.md`, whose **five design calls are Jordan-ruled** (its §10) though the design itself is PROPOSED. Enum count is unchanged. §3.1 |
| **O-7** | **this document's own v2 draft edge roster**, which shipped two scope extensions | this suite's own v2 draft | **a third, `allegiance` (person → faction), is added.** A scope extension, not an override of PP-724: person↔faction is outside its NPC↔NPC scope (`:18`), so R-1/R-2/R-3 are untouched — an allegiance is neither a Knot nor an NPC↔NPC tie. §7.2 |

**Two downstream overrides are ABSORBED here rather than left standing against a document that no
longer says what they override:** `09`'s **O-A1** (the tag enum opens to seven for `Ambition`) and
**O-A2** (the `progress` gauge row is cut as an AU-1 violation) are **executed in this text** — §3 and
§5.2. `09`'s own falsifier is *"no contract declares a state row named `progress`"*, and this document,
built first in Phase 1, was the one place that still would have. An append against `01`-as-drafted
would have raised on the seventh kind; it no longer does.

**Not overridden, deliberately:** ED-POL-11, PP-724 §0 and PP-724 §3.3 (§7.1's R-1/R-2/R-3) are
**preserved by construction** in §7.3, not merely respected. Part VI's unified-bond prohibition is
**weighed and partly adopted** — its taxonomy concern is honoured, its converter requirement is built
(§7.4), and its storage concern is the one point of disagreement, argued at O-4.

**v2 delta against v1 `01`:** the entity gains a **form** bucket (change A); the write rule gains a
**fourth leaf** and hysteresis becomes mandatory; the edge becomes a **shared container with per-kind
semantics and explicit converters**, adopting canon's taxonomy rather than inventing one, with the
Knot held **outside** it (change E, §7); Tag gains **`Holding`** (§3.1 — a v2 draft `Memory` kind was
written here and is **cut for it**, O-6); the edge gains an **`allegiance`** kind (§7.2, O-7); the
wrapper is reframed as a **herald** (§9). The decay law, `derive_ob`, the disclosure contract, the
player model and the relational-share cap survived the critique and are carried with their reasoning.

---

## 1. P-1 — Entity: identity is immutable, form is not

One identity primitive with **declared kinds**. A person, a place, a faction, a unit, a relation and a
bloc are the same shape; making Person a primitive while Place was something else would put two
identically-structured containers into two taxonomies, which is the shape-divergence failure this
suite is supposed to be immune to.

```
Entity
├── entity_id : str
├── kind      : person | place | faction | unit | edge | bloc      ← SIX (bloc is new; 06 §3)
├── identity  : IMMUTABLE. Only what makes this the same thing over its whole life.
├── form      : MUTABLE, but ONLY through a declared form transition (§2)
├── gauges / tags / posts
```

### 1.1 The per-kind split — normative

| kind | identity (immutable) | form (declared transitions only) |
|---|---|---|
| **person** | `origin_node`, `birth_season`, **`caste`**, **`heritage`**, `lineage_ref`, `capability_provenance` | `life_stage`, `capability {attr: int}`, `traits {virtues, flaws}` |
| **place** | `site_id`, `founding_season`, `terrain` | `kind`, `tier`, `facilities[]`, `presences{}` |
| **faction** | `seat_node`, `charter_season`, **`ethos {conviction: weight}`** | `posture` (a small declared enum) |
| **edge** | `endpoints (a, b)`, `relation` | `state` — from the set its relation kind admits (§7.3); `tier` for `knot` only |
| **unit** | `home_node`, `raised_season` | `unit_kind`, `assignment` |
| **bloc** | `faction_ref`, `formed_season` | `members[post_id]`, `state` |

**v1's error, corrected (O-1).** v1 put `place.kind` and `person.capability` in identity and then
forbade writing identity. The bucket was wrong, not the rule.

**Caste and heritage are IDENTITY, deliberately.** In this setting they are ascribed at birth and are
not something a person changes — *that is the point of a caste system*, and making them mutable would
quietly abolish the mechanic. What is mutable is how institutions **treat** them: the gating matrix in
`04`, living in a registry where it can be read, argued with and reformed.

**Ethos is identity; practice is not.** A faction's ethos is what the institution is *for*. It does
not drift with whoever holds the head post — v1's root cause C. What moves is the aggregate conviction
of its post-holders, and the distance between the two is `divergence` (`06 §2`), a **derivation**.

### 1.2 Capability reads the registry; it does not restate it

`engine/substrate/descriptors.py` owns the attribute roster, its scale, and the fact that the roster is
**incomplete by ruling** — nine defined, a tenth ruled and unnamed, exposed as
`ATTRIBUTES_PENDING_TENTH`. Capability is keyed on `descriptors.ATTRIBUTES` and **nothing in this suite
names an attribute literally**; when the tenth is named, every person gains it by regeneration and no
design changes. The same binds convictions through `descriptors.resolve_conviction`, which **raises** on
an unknown name rather than silently scoring zero. That raise is load-bearing history: `knots.py`
scarred `conviction='Loyalty'`, a name the conviction module had never heard of, so a ruled Close-Knot
consequence returned magnitude 0 forever while its caller reported success
(`engine/substrate/descriptors.py:155-172`). **This suite names no conviction literally either.**

### 1.3 Capability is form, not a gauge

An attribute decaying toward a rest value means **skills rot every season**, which is a different game.
Capability **ratchets**: it moves only through a life-path transition (`02 §4`), is bounded by
`descriptors.ATTRIBUTE_FLOOR`/`ATTRIBUTE_CEILING`, and never decays. This is the sharpest line between
the form bucket and the gauge, and the reason both exist.

### 1.4 `posts` is derived, which is the whole answer to the vocabulary collision

*Officer* means a mass-battle unit commander; *governor* the holder of a settlement's governance post;
*companion* a relationship, not an office. All three compose on one person because **`posts` is a
derived set, not a `role` string** — there is no field to collide in, and nothing here coins a new word
for a rank-holder: a person **holds a post**. ⚠ `seat` is not a synonym; it is already a settlement
type.

---

## 2. Form transitions — the fourth write leaf

### 2.1 The one write rule (v2)

> Every write terminates at exactly one of four leaves: **1.** a Gauge deposit · **2.** a Tag append ·
> **3.** a Post grant/revoke · **4.** a **form transition**.
> **Identity is never written. No aggregate is ever written.**

That is `propagation_spec_v1` §2's AU-1 made structural rather than a discipline: an aggregate has no
setter because the primitives it derives from are the only things with one. **The fourth leaf is
narrower than the three it joins, not wider** — a gauge deposit needs only provenance; a form
transition needs a declared row, a gate over readable state, a cost, an emission, and, if reversible, a
hysteresis band.

**An aggregate is not a stock, and AU-1 forbids only the first.** The rule is stated here in the one
form that stops the mislabel, because the mislabel has already happened twice in this suite.

| | **aggregate** | **stock** |
|---|---|---|
| definition | a value **current state can recompute** | a value with a **spend history**, so it is **path-dependent** |
| test | recompute it from the primitives; do you get it back? | two owners with identical current holdings and different spending are **different states**, and only the history separates them |
| examples | `faction.divergence`, NPC↔NPC disposition (§7.3), a project's `progress` (`09` O-A2) | `accrual.entitlement`, spent directly at place scale (`07 §8.3`, `:537`) — **already shipped** — and `post.budget` (§5.3) |
| how it is written | **never.** No setter exists | **leaf 1, twice**: a Gauge deposited into and drawn down |

⚠ **The test is "can current state recompute it?", never "does it look like a total?"** A quantity that
is **spent** cannot be a derivation, and declaring one `writable: false, owner: <x>.derive` is not a
filing choice — it is a defect that makes **every spend a silent no-op**, since there is no setter to
decrement. That is exactly the read/write asymmetry `CLAUDE.md §0.1` point 1 names as the hazard, and
the guard it asks for is a grep over the field's **assignments**, not its readers. **A stock is a
faction-, place- or post-owned Gauge**, deposited at the accounting boundary and drawn down by the
verbs that spend it. It is not an exception to AU-1; it was never in AU-1's scope.

### 2.2 The transition row

Declared in `references/form_registry.yaml` (`00 §9`), cooked, read at runtime.

```yaml
transition: <id>          entity_kind: <kind>      field: <the form field it moves>
from: <form value or *>   to: <form value>
gate: <predicate over gauges, tags, form and identity>   # a GATE, never a roll
cost: <deposits>          emits: form.transitioned       # always
reversible: true | false  hysteresis: {band: <float>, dwell: <int seasons>}   # REQUIRED if reversible
class: substrate
```

**Gated, never rolled.** A village becomes a town because its condition gauges *sustained* a band, not
because someone rolled well. **The uncertainty was in getting the gauges there**, and re-rolling at the
threshold charges for it twice. This is `00 §6` principle 4 at its sharpest, and why every transition's
resolver is `gate`.

**Emitting a CROSSING FACT, never a forecast.** Every transition emits `form.transitioned` carrying the
gate's inputs and what changed, so the world can notice a growth, a demotion, a rupture or a career
step, and the Slate (`10`) can rank it. A silent form change is indistinguishable from a bug.
⚠ **No emitter in this suite publishes a forecast.** `06_master_synthesis.md:565` (Part VI, held)
prohibits a world-visible imminence Key: *"`threshold_crossed` carries crossing **facts**, never
forecasts."* Adopted without reservation — it is also §8's disclosure contract read from the other
side, since a forecast is a trigger point published in instalments. **A transition emits after its gate
held, never that a gate is about to hold.**

**Hysteresis is required on any reversible pair. State the band explicitly.**

### 2.3 The hysteresis arithmetic, and why a naive threshold fails

For a reversible pair `A→B` gated at `g ≥ θ↑` and `B→A` at `g ≤ θ↓`:

```
θ↑ − θ↓  ≥  H_MIN(g)                       and       dwell ≥ D ≥ 1 seasons
H_MIN(g) =  max_seasonal_deposit(g) + λ_g·(ceiling_g − rest_g)     # the largest single-season swing
```

The second term is decay's own contribution: from the ceiling, one quiet season moves the gauge by
`λ(ceiling − rest)`. **A gauge sitting on a single threshold with no band oscillates every season**
under ordinary play — grow, decay, grow — emitting a Key each time, each of which is a Slate candidate.
Not a tuning problem; a property of the shape.

`H_MIN` is computable **at declaration time from the descriptor registry alone**, since
`max_seasonal_deposit` is the sum of the declared depositors' per-season caps. That makes the guard
cheap and total.

> **Falsifier.** A load-time test asserting that for every `reversible: true` pair,
> `θ↑ − θ↓ ≥ H_MIN(gauge)` and `dwell ≥ 1`. Load-bearing on the game: the difference between a
> settlement that grows and one that flickers between village and town forever.

**`dwell` is not redundant with the band.** The band bounds a *single-season* excursion; dwell bounds a
*sustained* one that happens to reverse. Only one is checkable arithmetically, and the row says which.

### 2.4 What a form transition may not do

| forbidden | because |
|---|---|
| transition a field the invoking module does not declare in `form:` (`00 §7`) | the set of modules that can change a place's tier must be a grep over one field |
| roll for the transition | §2.2 — the uncertainty was upstream |
| gate on a *derived* value alone, with no gauge | a derivation has no history, so the transition would have no auditable cause |
| a reversible pair with `hysteresis: null` | §2.3 |
| transition identity | there is no such thing |

*Emergent possibility lost if the form bucket and its transitions were cut:* places and people would be
frozen at creation — no growth, no decline, no career, no ruin.

---

## 3. P-2 — Tag

Durable, discrete memory on **any** entity. Six otherwise-unrelated requirements land here: a faction's
grudge, a place's precedent, a person's obligation, a body's record of a defeated motion, a fiscal
claim outliving its season, and the demoted officeholder's residual.

```
Tag: owner_ref (person|faction|place|post|edge|bloc) · kind · key (the dedupe axis) · value
     created_season · ttl (None = durable) · provenance : key_id  REQUIRED, NON-EMPTY
kind : Precedent | Grudge | Debt | Reputation | Leverage | Memory      ← SIX (§3.1)
```

### 3.1 Memory is the sixth kind, and the argument for opening a closed enum

v1 closed the enum at five and was right to: a mechanic must not be smuggled in as a tag family.
Opening it costs something real, so the argument is made rather than asserted.

**The five are third-person institutional record** — what the faction holds against you, what is said
of you, what was done here. Each is a claim whose `value` is the claim's **magnitude**, deduped to one
row per `(owner, kind, key)`. **A Memory is first-person and perceptual**: it belongs to a person, it is
about an event **they perceived**, and its `value` is **salience**. Two properties make it
inexpressible inside the five:

1. **Its existence is conditioned on perception, not on the event.** A Grudge exists because something
   happened; a Memory because someone *saw* it. That distinction is the entire mechanic — nobody can act
   on a false picture unless what a person knows is a separate object from what is true.
2. **`Reputation` is single-valued per owner by the dedupe rule**, so `Reputation(owner=perceiver,
   key=event)` would either break that rule or collapse every memory a person has into one row. The
   collision is structural, not stylistic.

**Six kinds, and the enum closes again at six.** A seventh needs the same two-part argument; "a
mechanic wants somewhere to live" is not it.

*Emergent possibility lost if Memory were cut:* nobody could act on a false or partial picture, so
deception, rumour and misjudgement would all be impossible.

### 3.2 Salience decay without a second decay law — a decision, not an oversight

A Tag's `value` does not decay; decay is a Gauge property. Salience must decay. Giving each Memory a
Gauge means one gauge per memory per person — the count grows with everything anyone ever saw. Adding a
decay field to Tag means a second decay law in the substrate and five kinds that never use it. So:

```
salience(memory, t) = value · (1 − λ_mem)^(t − created_season)        # derived at read
```

Same geometric law as §5.1, **one owner, no setter, no new stored field, no write** — a derivation over
data the tag already carries. `λ_mem` is one suite-level constant in the descriptor registry.

**The bound this needs.** Memories per person are capped at `MEMORY_CAP`, retained **top-K by derived
salience** at the sweep; without it the tag list is an unbounded ramp on a person's whole observed
history and every selection function reading memory gets slower and noisier forever. Reachability bar:
**at `MEMORY_CAP`, a memory of the maximum reachable salience must still displace the weakest retained
one** — otherwise the cap is a first-come lock, not a relevance filter.

### 3.3 Provenance is required, dedupe is the bound, the sweep is the release

**A tag with empty `provenance` cannot be appended.** The failure it prevents is documented and severe:
a convenience path producing a relational outcome the history does not justify corrodes the system *for
players who never use it*. Binding every durable tag to its causing Key makes the history queryable and
makes `Key.causes[]` a biography rather than a write-only chain.

**`tag_append` dedupes on `(owner_ref, kind, key)` and refreshes in place.** Not housekeeping: a
contested post generates one Grudge per passed-over candidate *per post*, refreshed — not one per
attempt, stacked. Without dedupe a popular post is an unbounded ramp on tag count, and those values feed
selection. With it, count is bounded by `candidates × posts`.

**At the accounting boundary every ledger drops its expired tags.** Durable tags survive sweeps **and
survive succession** — a place remembers what was done to it after the officeholder is gone, the
residual the genre's best-documented demotion failure lacks.

> **Falsifier.** A test asserting no reachable tag in a seeded campaign has empty provenance, and no
> person exceeds `MEMORY_CAP`. Load-bearing on the game — the mechanic is *why did this actor turn on
> me*.

### 3.4 A tag may bias a decision; it may never substitute for one

**Binding on every selection function in this suite.** Wherever a decision function sums a relational or
leverage term alongside structural terms — a candidate's fitness, an action's appeal, a target's
hostility, a Slate item's salience — the relational contribution is capped as a fraction of the
function's structural range:

```
|relational terms|  ≤  RELATION_SHARE_MAX · (max structural term − min structural term)
```

The failure prevented is documented and specific: relationship modifiers large enough to dissolve
structural conflict produce a game in which *you can generally succeed at things rulers historically
wanted to do and could not*, because opinion bonuses paper over positional facts. **Some conflicts must
be positional and unbuyable.**

It binds hardest on custody (§4.2): a `Leverage` tag biases a holder toward the controller's
preferences; it never replaces them. A custodian who fully determined a holder's choices would make
custody strictly better than holding the post at a fraction of the exposure — the mechanic eating
itself. **Memory is inside the cap, not beside it**: misperception shifts weighting, never the board.
**Reachability bar: at the maximum reachable relational total, the structurally-worst option must still
be unable to outrank the structurally-best one.**

---

## 4. P-3 — Post

The delegation object. Acting *on behalf of* something at a tier requires a post that can be granted
and revoked; acting *within* is a claim on someone else's. Both stances need this object; neither needs
a second one.

```
Post: post_id · kind (head|governor|minister|commander|envoy|clerk, closed at six) · tier_node
      principal (who granted it, and may revoke it) · holder_id (None = VACANT, and first-class)
      remit [module_id] · granted_season · term (None = at pleasure) · budget : Gauge (§5.3)
```

### 4.1 A vacancy is a state, not an absence

`holder_id = None` is the object that closes ED-IN-0201's gate. It is queryable, it is a demand signal
for generation, and it is why a faction that cannot find a head **stops acting** rather than acting
badly — a better failure state than any collapse procedure, needing no detection mechanism because the
gate reads the field. **Recoverability is carried from v1 unchanged:** a seat node that cannot be lost
means the gate is always re-satisfiable, so a vacancy is a pause, not a death spiral. **v2 addition:**
the gate applies **per tier** (`05 §3`) — a faction with a governor in one settlement and no national
post is a *local* faction. v1's single peninsula-scale gate made every faction national or nothing.

### 4.2 Custody is a tag, not a field

Controlling a post-holder without deposing them is a five-source convergence in the precedent survey. It
is **not** a second identity field:
`Leverage(owner_ref=(post, post_id), key=<controller>, provenance=<the establishing Key>)` carries what
a `custodian_id` field would, plus a ttl, a provenance chain and a decay the field would not have.
Establishing custody is a contested action (`12 §3`); losing it is the tag expiring or being stripped.
**No new field.**

### 4.3 `remit` is how a person changes the option set

ED-IN-0201 clause 2 says the person shapes *which* action is chosen from the same option set with the
same information — and its own NERS constraint says that must not be a flat trait bonus on a selection
roll, because a flat shift is worth systematically more to a small pool than a large one. `remit`
satisfies both: a module is invocable only by a post whose remit names it. Two holders of the same post
get the same remit; two different post kinds get different remits; a holder's convictions and beliefs
rank the remit's contents (`05 §3`). **The choice differs; the odds do not.**

### 4.4 The player holds a post — and that is the entire player model

There is no player entity, no player faction flag and no player-only module anywhere in this suite.
**The player is a person, and they act by holding posts.**

| | |
|---|---|
| what the player may do this season | exactly the modules in the remit of the posts they hold, as for any other holder — **filtered by the Slate** (`10`) to the scene budget |
| what they spend | the `budget` gauge on those posts, as for any other holder |
| an unattended post | the same module runs, with the holder's own preference supplying the choice |
| how reach is gained / lost | appointment or claim, routed through `04`; audit, recall, succession, or the gate closing |

1. **No special-casing.** A player-only branch is scripting drift by definition, and the surest way to
   grow one is to give the player a different object to act through.
2. **Delegation is free.** A player holding three posts and attending to one has not lost the other two.
3. **One engine, several entry points.** The surveyed franchise whose fast path is a *different
   algorithm* from its played path spent two decades with a divergence exploited in both directions; the
   one whose three fidelities are the same engine resolving the same fixture did not. A played action and
   an unattended action here are the same module with the same pool, obstacle and ladder, so **there is
   no divergence to calibrate** — only the *choice* differs, and that difference is the point. `10`'s
   below-the-line auto-resolution inherits this verbatim.

---

## 5. P-4 — Gauge

Every continuous quantity in the game. A Key is a typed one-shot emission — right for a flag,
structurally wrong for a value read continuously between emissions and decaying. Acceptance, order,
pressure, disposition, standing, exposure, edge strain, Thread Sensitivity, an accrual, a budget: none
of these *emit*, they *are*.

```
Gauge (declared in references/descriptor_registry.yaml; instantiated per owner)
  gauge_id · owner_ref (incl. edge and bloc) · scale · floor, ceiling
  lambda ∈ (0,1] · rest · bands [(threshold, label)] · history [(season, delta, provenance)]
```

Three functions: `gauge_deposit(g, delta, provenance)` — appends, **provenance required**;
`gauge_value(g, season)`; `gauge_band(g, season)` — **what a player sees**. **There is no setter.**

### 5.1 Decay is geometric, never a saturating additive step

```
value(t+1) = rest + (value(t) − rest)·(1 − λ)  +  Σ deposits(t)
```

**The single most load-bearing arithmetic choice in the suite**, chosen against a measured failure. A
restoring term that saturates — pulling back by *at most* a fixed step per season — is bounded above by
that step, so **any accrual larger than it pins the value at its ceiling and holds it there**. Not a
tuning problem; a property of the shape, producing an unrecoverable state from ordinary play.

A geometric restoring term has no such ceiling on its own strength. For a bounded per-season accrual
`a` the fixed point is `rest + a/λ` — **finite for every λ ∈ (0,1] and every bounded `a`** — and
settling time is `≈1/λ` seasons regardless of magnitude. Consequences for free: **contractivity is
structural** (`propagation_spec_v1` AU-4 requires `decay()` to be a pure function of elapsed time, and
§4.3 makes cross-tick convergence conditional on strict contractivity; `(1 − λ)` is strictly contractive
by construction); **every gauge is bounded**, clamped on read; **monotonic response** — more deposit is
never less value; and **§2.3's `H_MIN` is computable from these fields alone**, which is why the
hysteresis guard needs no campaign run.

> **Falsifier.** An arithmetic test, no campaign run, asserting for every declared gauge that
> `rest + max_seasonal_accrual/λ ≤ ceiling`. A gauge whose declared accrual sources exceed that fails
> **at declaration time**. Load-bearing on the game: the difference between a settlement that can
> recover and one that cannot.

### 5.2 Where gauges are used, and what each retires

| Gauge | Owner | Retires |
|---|---|---|
| `disposition.pc_npc` | edge (PC↔NPC only — NPC↔NPC is **derived**, §7.3) | a bespoke loyalty scalar per subsystem |
| **`strain.<kind>`** *(v2)* | edge, **declared per relation kind; the kinds never sum** (§7.3) | a bespoke wear counter per relationship kind |
| `standing` · `exposure` | person | the public and private halves of nine parallel personal meters |
| **`thread_sensitivity`** *(v2)* | person | a per-subsystem TS field; canon scales it 0–100 (`systems/overview/clock_registry_v30.md:72`) |
| `acceptance.{legitimacy,support}` | place | per-settlement political acceptance |
| `condition.{order,prosperity,defense}` | place | the settlement stat block |
| `pressure` | place | the candidate-emission driver (`10`) |
| **`presence.<institution>`** *(v2)* | place | a bespoke Church/Guild/Warden reach field (`07 §4`) |
| `accrual.entitlement` | place | the levy channel's supply |
| **`progress`** *(v2)* | any project owner | a bespoke timer per ambition (`09 §2`) |
| **`cohesion`** *(v2)* | bloc | any second faction-like stat block on a bloc (`06 §3`) |
| `budget` | post | every proposed action economy in the corpus |

**Two personal meters, not nine.** Nine bounded meters differing only in their trigger lists is nine
bars a player watches; the triggers were the design, the meters were duplication.
`thread_sensitivity` is a third **only because canon already scales and gates on it** (§7.5) — cited,
not invented.

### 5.3 Budget is a gauge, and it buys actions — never modifiers

A budget is an accrual with a spender; making it the same primitive closes the *three rival accrual
clocks* problem structurally — one rate, one cap, one bifurcation analysis, several typed consumers.
**One budget point buys one attempt at one module.** It never converts into dice and never into an
obstacle shift.

The arithmetic that forces this: in the continuous engine an added die at a balanced check is worth
`≈0.204σ` at pool 5 against `≈0.115σ` at pool 18, and is obstacle-dependent too — roughly
`0.107σ`–`0.302σ` at pool 5 alone. A currency spendable as a modifier is therefore worth **about twice
as much** on a small pool as a large one, and more once the obstacle varies; a player who notices routes
their budget wherever it pays. Buying *actions* keeps the budget out of the resolution arithmetic
entirely, which is also the simpler design.

> **Falsifier.** A test asserting no module contract declares a `budget:` whose cost is consumed inside
> a pool or obstacle expression. Load-bearing on the game: the difference between a budget and an
> exploit.

**v2 note:** the budget is **per post**, not per faction (`05 §3`), so a faction's total action capacity
is the sum over the posts it actually staffs — Jordan's 2026-07-13 ruling that factions hold people, and
that the number of people and the weight of their positions carry a faction's value, expressed as
arithmetic rather than as a sentence.

---

## 6. E-1 — `derive_ob`, the obstacle's owner

```python
def derive_ob(target_score: float, modifiers: float = 0.0) -> float:
    """Jordan, 2026-08-14: an obstacle rolled against a character or faction is their corresponding
    score/2 plus whatever specific modifiers exist for them in that instance."""
    return max(OB_MIN, target_score / 2.0 + modifiers)
```

**`OB_MIN` is `1`** — pinned, canonically tagged and guarded: `engine/autoload/sigma_leverage.py:108`
(`# [canonical: params/core.md §Obstacle Scale]`), applied at `:177`, with
`test_sigma_leverage_parity.py:355-357` asserting the floor holds at extreme leverage. ⚠ **It lives in
`sigma_leverage`, not in `dice_engine`, so `derive_ob` must IMPORT it, never restate it.** A second
copy of a pinned constant beside the function that floors on it is exactly the §8 "never re-implement a
rule" violation, and it would be invisible until the two drifted.

It belongs beside `roll_pool` in `engine/autoload/dice_engine.py`, for a reason the corpus measured: the
margin ladder is single-owned and guarded (`degree_from_net`) while the obstacle is derived locally in
most resolving subsystems and arrives at the roller as a bare parameter. **Ruling the obstacle without
giving it an owner predicts the same fork recurring**, and there is a measured precedent in six private
roll/degree implementations.

1. **The result is fractional and stays fractional.** The ladder's contract says both operands may be
   fractional; every existing derivation site rounds or floors against a ladder built to consume
   fractions. Producers correct when written stopped being correct when the ladder moved beneath them. A
   single owner cannot drift that way.
2. **Modifiers are σ-space, not obstacle-space.** A modifier reaches the roll through
   `sigma_leverage.net_boost` — a μ-shift scaled by `σ_N = 0.8·√Pool` — never as a flat addition to
   `derive_ob`'s output, which would be worth more to a small pool than a large one (§5.3's
   non-uniformity, one level down). The `modifiers` argument is reserved for terms genuinely *properties
   of the target* — a fortification, a legal protection, **an incumbent's presence level** (`05 §4`).
3. **The floor is `OB_MIN`**, so an advantage cannot drive the obstacle below the ruled minimum.

**It adds to the engine and repoints nothing.** The three existing derivation sites whose reconciliation
is suspended are a different lane's question, and a greenfield module has no ratified canon to overwrite.

**One leverage note, because it is the obvious objection.** Raising an attribute adds a die, worth
`≈0.204σ` at pool 5 against `≈0.115σ` at pool 18 — so capability investment is worth about 1.8× as much
to a weak actor as a strong one. That is **non-uniform in the correct direction**: self-damping, and the
shape a bounded system wants. It is a property of the continuous engine, recorded so a later reader does
not mistake it for an unnoticed P-ii defect.


### 6.1 The commensurability gate — a target score must live on the pool's scale

**Found by `05`'s author, who correctly refused to fix it locally.** `derive_ob` has no check that the
target score's scale is commensurate with the net's, and `score/2` is meaningful only if it is.

**The arithmetic, verified against the engine rather than taken on report.** `net ~ Normal(0.4·N,
0.8·√N)` — `_MU_PER_DIE = 0.40`, `_SIGMA_PER_DIE = 0.800`, applied in `continuous_engine_sample`
(`engine/autoload/dice_engine.py:174-175`, `:209-224`). The ladder reads the margin: Overwhelming
`≥ 3`, Success `≥ 1`, Partial `[0,1)`, Failure `< 0`. So at pool 18, μ = 7.2 and σ = 3.394, and:

| target gauge | ceiling | `derive_ob` | P(Overwhelming) at pool 18 |
|---|---|---|---|
| a `0–7` stat | 7 | 3.5 | 0.58 |
| **Thread Sensitivity** | **100** | **50** | **0.000000** |

**Every band but Failure becomes unreachable, and nothing currently catches it.** The gauge exists,
the obstacle derives, the roll resolves, and the site returns one degree forever — *a mechanic that
looks live and is dead*, the worst failure class in the suite because it passes every structural
check.

**The gate, checked at declaration time, per call site.** The envelope on the right-hand side is **the
distribution of whatever quantity the site passes to `degree_from_net` as `net`** — which is not the
same quantity for every shape. So the site's declared **shape** selects the form.

```
                     ONE-SIDED  (U · SO · GATE — the site rolls one pool against a static Ob)
  top band:      derive_ob(S_max, M_max) + 3  ≤  0.4·N_max + z·0.8·√N_max
  bottom band:   derive_ob(S_min, M_min)      >  0.4·N_min − z·0.8·√N_min

                     DIFFERENTIAL  (DO · BI — the ladder reads net_c − net_d)
  top band:      derive_ob(S_max, M_max) + 3  ≤  0.4·(N_max − D_min) + z·0.8·√(N_max + D_min)
  bottom band:   derive_ob(S_min, M_min)      >  0.4·(N_min − D_max) − z·0.8·√(N_min + D_max)

  z = 1.645  (ε = 5%, declared, not folded in).   N = the acting pool, D = the opposing pool.
```

Both must hold, or the row is rejected when it is written rather than discovered in a playtest.

⚠ **The two bands use opposite corners, each being the one where that band is hardest to reach.**
Overwhelming is hardest against the largest obstacle, so the top band pairs `S_max, M_max` with the
*strongest* actor; Failure is hardest against the smallest, so the bottom band pairs `S_min, M_min`
with the *weakest*. **An earlier draft used `N_max` in both** — asking whether the strongest actor can
still fail the easiest task, which has no design content and rejects sound sites: a `0–10` target
floors at `derive_ob = 1`, and `1 > 1.617` is false at `N_max = 18` but `1 > −0.943` is true at
`N_min = 5`. The DO form was written with the right corners, so **the two disagreed, which is what
exposed it.**

### 6.1.1 Three corrections to the form the finding proposed

The finding's shape is right and its diagnosis is right. Its expression is not, in three ways, and
since this is the single owner's page the corrected version is the one that binds.

**1. It must carry the σ term.** The proposal was `ceiling / 2 < 0.4 · POOL_MAX + 3`. That has no
width term, so it is not a reachability condition at any pool except by coincidence — and it has the
band offset's sign backwards, since Overwhelming needs `net ≥ ob + 3`, which pushes the bound *down*
by 3 and back up by `z·σ`:

| N_max | correct | as proposed | ratio |
|---|---|---|---|
| 5 | 1.94 | 5.00 | **2.57×** too permissive |
| 10 | 5.16 | 7.00 | 1.36× |
| 18 | 9.78 | 10.20 | 1.04× |

The two agree to 4% at pool 18 **by accident** — `+3` happens to approximate `z·σ − 3 = 2.58` there —
and diverge badly below it. A check that is only correct at one pool size is not a check.

**2. `POOL_MAX` does not exist.** No such constant is in `engine/`; `roll_pool` enforces only a pool
*minimum* of 1 (`:202`). **The bound is per-site**, and has to be: a site's maximum pool is a property
of the pool expression its own module declares. Where a figure is needed this document uses the **practical range 5–18**
that §5.3's σ arithmetic already stands over, rather than minting a constant.

**3. It must check the post-modifier obstacle.** `derive_ob`'s `modifiers` argument is **unbounded in
the signature**, so checking a bare ceiling is meaningless if a site may add +10. Hence `M_max`, and
hence a new obligation: **a module contract declaring a `derive_ob` site must declare its modifier
bound.** Without it the gate is unevaluable — the same defect one level up.


### 6.1.2 The opposed form, and why the one-sided form false-passes without it

**Found by `05`'s author against this gate — its own failure class, one level up.** §6.1's first
version carried only the one-sided envelope; applied to a **DO** site it admits obstacles the
differential cannot reach — a **false pass**, exactly what §6.1 exists to catch.

**Verified in the kernel, not taken on report.** `05 §4.1` passes `net_c − net_d` as the ladder's
`net` and the entrenchment lead as its `ob`, and `degree_from_net` reads `margin = net − ob` and
nothing else (`engine/autoload/dice_engine.py:279`). So the envelope must describe the **difference of
two independently rolled pools**:

- **The per-die moments are EXACT, not fitted.** `_die_result` maps `1 → −1`, `2–6 → 0`, `7–9 → +1`,
  `10 → +2` (`:153-161`), giving `μ = 0.400000` and `Var = 0.640000` by direct computation over the ten
  faces — precisely `_MU_PER_DIE` and `_SIGMA_PER_DIE` (`:174-175`). Variance-addition below is
  therefore exact arithmetic, not an approximation.
- **Independence holds.** The two sides are separate `roll_pool` / `continuous_engine_sample` calls
  drawing independently (`:202-205`, `:218-224`); no term is shared. Hence `Var(net_c − net_d) =
  0.64·N_c + 0.64·N_d`, giving **`μ_diff = 0.4(N_c − N_d)`** and **`σ_diff = 0.8·√(N_c + N_d)`**.
- **Normality is better here, not worse.** A difference of two independent normals is exactly normal,
  so `z` is exact in the continuous engine and a CLT approximation only in the discrete one.

| | envelope | `Ob_max` |
|---|---|---|
| one-sided, `N = 18` | 12.783 | **9.783** |
| differential, `N_c = 18` vs `N_d = 6` | 11.247 | **8.247** |

**The differential is stricter**, so evaluating an opposed site one-sidedly admits `Ob ∈ (8.247,
9.783]` that cannot in fact reach Overwhelming. The finding's arithmetic reproduces exactly.

**Which corner to evaluate — proved, so the check is two evaluations, not a search.** The top-band
envelope's derivative in `D` is `−0.4 + 0.4·z/√(N + D)`, zero only at `N + D = z² = 2.706`, so for any
real pool the envelope **strictly decreases in `D`** and its maximum sits at `D = D_min`. Hence the
form takes `D_min`, not a nominal opposing pool: **`N_d = 6` is right only if 6 is that site's declared
minimum** — at `D_min = 1` the bound is `9.536`. The gate reads the corner from the registry.

**The bottom band rarely binds on a DO site.** With `N_min = 5` against `D_max = 18`,
`μ_diff − z·σ_diff = −11.5`, while `derive_ob` floors at **`OB_MIN = 1`**
(`sigma_leverage.py:108`) — so the inequality clears by more than twelve, and Failure is reachable by
construction whenever the defender can match the challenger. It is kept because a site with
`D_max < N_min` — a permanently outmatched defender — is expressible, and there it bites.

**Why this belongs here and not in `05`.** `05`'s author found the hole and declined to patch it
locally, which was correct. The stronger argument is what these passes demonstrate: **this page
identified the hazard and still got the arithmetic wrong twice — the one-sided envelope, then the
bottom-band corner — and so did the reader relaying it.** A rule three readers derive differently is
exactly the rule that must have one owner and one expression; restating it per document multiplies the
surfaces on which it can be got wrong. That is a better justification for E-1's single ownership than
"the obstacle had a ruling and no owner".

**What the module contract must carry.** A site declaring a `derive_ob` call declares
`shape`, `pool_max`, `pool_min`, `ob_modifier_max`, `ob_modifier_min`, and — **for `DO`/`BI` only** —
`pool_opposed_min` and `pool_opposed_max`. Without the last two an opposed site is unevaluable, which
is the §6.1.1 point-3 defect recurring at the shape level.

### 6.2 What fails the gate today

**The pattern is not a coincidence.** Canon's **`0–7` stat family** — attributes, all six faction
stats, the settlement stats — is **pool-commensurate by construction**: `ceiling/2 ≤ 3.5`, so
`Ob + 3 ≤ 6.5` clears the envelope from about `N_max = 8` upward. It is *not* unconditional — a site
declaring `N_max = 5` cannot overwhelm a score-7 target (`6.5 > 4.94`), which is a true design fact
rather than a defect — so **every site is still checked on its own `N_max`.** Everything that fails
below is from another family and was never a "score" in the sense Jordan's ruling means.

| gauge | scale, and its source | verdict as a `derive_ob` target |
|---|---|---|
| attributes; `fac.*`; `set.legitimacy/popular_support`; `set.prosperity/defense/order`; `terr.fort_level` | 1–7 / 0–7 / 0–5 / 0–4, `engine/engine_params/descriptors.json` | **pass** |
| `disposition.pc_npc`, `strain.<kind>` | −5…+5; PP-724 capacity 3/5/7 | **pass** |
| Piety Track 0–5 · Truth 0–5 · Momentum 0–4 | `systems/overview/clock_registry_v30.md` | **pass** |
| Coherence 0–10 · Persuasion Track 0–10 · Church Attention Pool 0–10 | same | **borderline** — ob 5, P(Overwhelming) ≈ 0.41 at pool 18 and ≈ 0.001 at pool 5. Passes at a large `N_max`, fails at a small one. **Site-dependent, so the per-site form of the gate is what decides it** |
| **Composure 3–21 · Concentration 5–35 · Stamina 5–47 · Health 13–55** | `derived_stats_v30.md` via `clock_registry_v30.md` | **FAIL.** These are damage and resource pools, not scores. Nothing in this suite targets them, and this row exists so nothing later does |
| **Thread Sensitivity 0–100 (hard cap)** | `systems/overview/clock_registry_v30.md:72` | **FAIL, catastrophically** — ob 50 against μ 7.2. **It is a gate target, not an obstacle target**, and canon already uses it as exactly that: `TS ≥ 30` (§7.5). The failure is not in the gauge; it is in ever passing it to `derive_ob` |
| **`prac.thread_sensitivity`** | **floor 0, ceiling `None`** in `engine/engine_params/descriptors.json` | **UNEVALUABLE — a second, independent defect.** The cooked registry declares *no ceiling*, while canon declares a 0–100 hard cap. A gauge with no ceiling cannot be checked by this gate, by §5.1's fixed-point falsifier, or by §2.3's `H_MIN`. **Three declaration-time guards are silently inert on it.** Recorded, not fixed here: the registry row is the FI/IN lane's to correct |
| `standing`, `exposure`, `pressure`, `acceptance.*`, `accrual.entitlement` | **scale undeclared in this suite** | **unverifiable today.** Each must declare a ceiling before it can be a target |
| `presence.<institution>` | **0–7**, declared by `07 §4.2` after this gate was raised | **pass, and it is the gate's first live use.** `05 §4.1` is the suite's only opposed site: `shape: DO`, `Ob = derive_ob(presence_defender, −presence_challenger/2 + place_terms)`, modifier bound 2, so `Ob_max = 7/2 + 2 = 5.5` against the **differential** envelope `8.247` (§6.1.2). Passes with room. Under the one-sided form the admissible ceiling was `12.49`; under the correct opposed form it is **`≤ 12`** — `07` chose 7 deliberately, so the tightening did not bite |

**Re-checked against `OB_MIN = 1`; no verdict moved — recorded because a re-check that changes nothing
is still a check.** The floor cannot touch the top band: at any `S_max` worth gating `S_max/2 + M_max >
1`, so the `max()` is inactive. It touches only the bottom band, where a *higher* floor makes Failure
**easier** to reach — every bottom-band verdict is strengthened, not narrowed. The **borderline** row
checked explicitly: a `0–10` gauge gives `derive_ob(0) = 1`, and `1 > −0.943` holds at `N_min = 5`, so
it passes on the corrected corner; Coherence, the Persuasion Track and the Church Attention Pool stay
borderline for the *same* reason as before — `Ob = 5` is site-dependent at the top, not the bottom.
**One real consequence:** with a floor of 1 a target scoring `≤ 2` yields the same obstacle as one
scoring `0`, so **the bottom two points of every gauge are not discriminable as obstacle targets.** No
site here reads a target in that band, and one that did would be measuring nothing.

**The opposed form flipped no verdict here.** The suite's only opposed site (`05 §4.1`, targeting
`presence`) still passes, because `07` declared `0–7` rather than spending the headroom the looser form
allowed. That is a **near miss, not a clean bill**: had `07` taken the `12.49` the one-sided form
permitted, this correction would have invalidated an already-propagated ceiling.

**Nothing in this suite currently targets a failing gauge.** The gate's value is mostly prospective: it
makes the failure impossible to introduce rather than expensive to discover.

*Emergent possibility lost if the gate were cut:* none — it removes no possibility, it removes a class
of silently-dead mechanic. It is the one addition on this page that is pure subtraction of failure,
and by `00 §1`'s own test that is what a distillation looks like.
