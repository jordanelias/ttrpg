# THE IDEALIZED SHAPE, v2 — Fable-5 synthesis brief
# Read-only synthesis. Inputs: 10_SUPERSEDING.md (what survived), 20_FABLE5_ADVERSARIAL_REVIEW.md
# (what broke), CODE_SHAPE_ABSTRACT.md (the inventory), and Jordan's stated demands this session.
# NOTHING HERE EXECUTES. Every claim is an argument about text.

## 0 · WHAT THIS EXERCISE MAY AND MAY NOT DO

**May:** unify primitives, delete categories, restate the loop, close the review's confirmed gaps.
**May NOT:** rule D-2 (act economy), conferral basis, `stores`-as-denominator, S19, the Coherence-0
ontology, or off-board polities. §16 reserved those and the review's M6 records what happens when an
audit answers a reserved fork from "architecture". They are INPUTS with both branches carried.

**Scope (Jordan):** the seasonal loop. Mass battle, personal combat and social contest are DEFERRED —
they attach at ONE seam (§5's `resolve`) and this document specifies the seam, not the subsystems.

## 1 · THE DIAGNOSIS THAT SHAPES THE ARCHITECTURE

The review's surviving verdict: **the design can change the STATE of what exists and cannot change
WHICH things exist or who holds them.** Confirmed absent: creation/destruction of Site, Container,
Office; tenure over sites and nodes; birth; character generation; caused advancement.

Jordan's loop demands the opposite of that, in five paired flows — built/destroyed · born/die ·
disseminated/purged · demands up · directives down — plus: the world churns with or without the
player · every active decision is a character's · power is not static · royal factions may collapse
and be replaced by dynamically generated ones.

**So the architecture's organising question is: what is the smallest set of primitives under which
EXISTENCE, TENURE and STATE are the same kind of change?** Answer: three, below.

## 2 · THE PRIMITIVE SET — three carriers, one edge, one act

### 2.1 The three carriers (things that exist)

```
Person   := (address, marks, capability, stance, ledger, ties)        -- the only actor
Node     := (kind, stake[], judging_set_rule, dates[], matter)        -- a rung of containment
Office   := (post, node?, remit, conferral, establishment, dates[], upkeep)
```
`Site` is NOT a fourth carrier — it is **matter held by a Node** (`condition ∈ [0,1]`), which is what
§4.2's amended Container row already licenses. This deletes one object from the review's own fix list.

`Faction` is NOT a carrier. A faction is **a Proposition plus the set of Tenures of kind `commit`
pointing at it** — i.e. it is entirely derived (§2.4). This is the largest deletion in the document
and it is what makes "dynamically generated factions" fall out rather than be built.

### 2.2 The one edge — `Tenure`

```
Tenure := (subject, object, kind, since, conferrer, degree?, avowed?)
   subject ∈ Person | Node | Faction
   object  ∈ Person | Node | Office | Site | Proposition
   kind    ∈ hold | commit | contain | succeed | tie | knot
```
**One record shape; six relation kinds; each kind carries its own rules.** Membership is NOT holding —
Jordan's distinction — but they share a representation, which is uniformity without conflation.

| kind | subject → object | what it is | created by | destroyed by |
|---|---|---|---|---|
| `hold` | Person → Office \| Site \| Node | office, fief, lordship | `confer` | `revoke` |
| `commit` | Person → Proposition | faction membership at a degree | `commit(+Δ)` | degree → 0 |
| `contain` | Node → Node, Person → Node | the containment tree; a person's address | `admit`, `annex` | `secede`, `migrate` |
| `succeed` | Node → Person | the hearth's succession pointer | a naming act | re-naming |
| `tie` / `knot` | Person → Person | ordinary contact; deep channel | co-presence, `form_knot` | decay, rupture |

**What this buys, in one line each.** Annexation is `confer` on a `contain` edge. Confiscation is
`revoke` on a `hold` edge. Deposition is not an operation at all (§2.4). Secession is `revoke` on
`contain`. All four were unreachable; none needs a verb that does not already exist in `remit.acts`.

⚠ **`contain` must stay single-parent for Persons** (§1.2's derivation) — enforced as an invariant on
the edge kind, not by a separate tree structure.

### 2.3 The one act

```
Act := (actor, verb, touches[], payload)
touches := (object, mode)
mode ∈ read | alter | exclude | mint | efface
```
**`mint` and `efface` are the review's rank-1 fix and they close existence.** `mint` a Site is
building; `mint` a Node is founding a settlement; `mint` an Office is establishment; `mint` a
Proposition is founding a faction; `mint` a Person is birth (§4.3); `efface` is each one's inverse.

⚠ **`efface` may NOT target a Claim in another person's ledger** — R-2 forbids reaching through a
person. The purge limb is therefore NOT closed by `efface` and is specified separately at §5.4.

⚠ **`alter` carries per-FIELD commutativity**, declared on the field, not the act:
`additive` (all writers apply, order-independent — `condition`, `stores`) vs `exclusive` (contested —
a succession pointer, an office's remit). This is the review's B1 fix and it makes the conflict rule
shorter: two acts conflict iff they share an object and either mode is `exclude`/`efface`, or both
`alter` an `exclusive` field.

### 2.4 Derived — the category that replaces stored aggregates

A **Derived** is a named pure function over state, never stored, recomputed on demand. This is the
formal version of §4.2's "Nobody" row, and it is what makes several "missing objects" disappear.

| derived | signature | replaces |
|---|---|---|
| `faction(p)` | Proposition → {commit Tenures} | a stored faction object |
| `principals(f, n)` | (Proposition, Node) → ranked [Person] | a faction leader field. **Deposition = this returning someone else** |
| `presence/density/footprint` | (Proposition, Node) → scalar | faction scale |
| `sovereign_fraction(root)` | Node → [0,1] | stored control |
| `condition(n)` | Node → [0,1], draw-weighted mean of children | a stored coarse condition |
| `norm(n, prop)` | (Node, Proposition) → scalar | a stored norm/unrest/reputation |
| `opening_set(p)` | Person → [Act] | an authored opportunity |
| `occupation(p)` | Person → (Practice, Site) | **a new answer**: the practice a person draws subsistence from, plus the site they draw it at. Not a field — the review's transition 7 closes here with no object added |
| `estimated_profile(p, f)` | (Person, Proposition) → profile | reading true state |

**Nothing stores an aggregate. Every one of these is a query, and that is why power is not static.**

## 3 · THE SIGNATURES — one change, and it is forced

```
choose  : (Person, View, Sensation) -> Act        # NO World, ever
resolve : (Act[], World)            -> Event[]    # NO Person
witness : (Person, Event)           -> Claim[]    # per-person; a collection is a type error
```
⚠ **`Sensation` is new and it is the review's A5 fix, corrected.** §2 says subsistence and standing
read **the world**; P2 forbids storing needs; View is assembled from claims only. There was no legal
path. The prior fix (needs as claims) broke `witness`'s monopoly on root tokens and made hunger
evictable. So: **`Sensation` is a closed record of exactly the four need scalars**, computed in P2,
never stored, carrying no references and answering no query. `choose` still cannot see the world —
it sees what a body reports. The type now tells the truth the design already stated in prose.

## 4 · WHAT THE REVIEW LEFT OPEN, CLOSED HERE

### 4.1 Advancement — restored from #342 `02:186-189`, not invented
`mint` on a practice rank, gated exactly as shipped: a practice gains a rank when an attempt at a
standard above its rank resolves AND (it was witnessed by someone holding the practice higher, OR it
failed at a cost the person actually paid). **No experience clock** — the §14 row-12 refusal at
person scale.

### 4.2 Population inflow — restored from #342 `09:528-548`
Each Node carries a **demographic envelope** (counts by age band, marks bundle, capability
distribution) as matter, not as a social aggregate. **Births and deaths move weights.** A Person
record is minted on any of five triggers (named, telling, role/office, knot, decisive-in-contest);
minting draws address/marks/capability/stance from the envelope plus its dispersion.

### 4.3 The channel store — #342's placement, restored
Tellings are stored **at the channel**, not per person, until individuation; a minted person is
handed the claims their address's channels would have deposited, and **draws** from a construal
distribution rather than inheriting a value. ⚠ The review's M1 objected that a channel is not one of
the five owners. **Resolution: the channel store is matter on the Node the channel runs through**,
which §4.2's Container row already licenses, so no sixth owner is created.

### 4.4 The purge limb — specified, not hand-waved
`efface` cannot reach another ledger. What CAN be done, and is enough: `efface` a **record** (matter
at a Node — a register, a charter, a deed), which removes the *corroborating source* and drops
confidence for everyone whose claim cites it; and **`SAID` claims** already make a recantation a new
claim colliding with the old. **Suppression is a confidence attack, not a deletion**, and that is
both R-2-legal and truer to how ideas are actually suppressed.

### 4.5 Field investigation — the detective seat, from existing parts
`investigate := (actor, question, site|person, spend)` — an ordinary act whose obstacle is composed
per §5.2 and whose OUTPUT is claims with `firsthand` source into the actor's own ledger. It needs no
new machinery; it is the one verb the epistemics layer was built for and never given.

## 5 · THE LOOP — three global barriers, two per-person maps

The review's C13: the eight phases conflate *barrier* with *step*. Restated:

| | what | writes | class |
|---|---|---|---|
| **B1 CALENDAR** | advance date; fire due dates; evaluate convening conditions | dates, dockets | **calendar** |
| **B2 MATTER** | larders, bodies, travel, `yield`, envelope weights | matter | **matter** |
| **M1 DELIBERATE** *(per person, pure)* | sensation → view → choose | nothing but the returned Act | — |
| **B3 RESOLVE** | `resolve(acts, world)` | everything else | **acts** |
| **M2 RECKON** *(per person)* | witness; confidence decay; eviction; individuation | own ledger only | — |

**Three barriers, three write classes, exactly.** The per-person maps write nothing global, which is
what licenses running them in any order and in parallel — and `resolve`'s order-independence is
already required by §5.5. This is strictly cheaper than eight barriers and it makes the write-class
argument structural rather than asserted.

⚠ **Eviction ranks on `confidence_live × recency` only** (review B6) — never on stance-weighted
salience, or motivated *retrieval* silently becomes motivated *deletion*. And `salience`'s
`relevance(c, q)` term is undefined with no question `q`, which is why the eviction ranking must be a
different function from the retrieval ranking.

## 6 · DETERMINISM
Substream per operation from `(world_seed, tick, subject_id, purpose)` — generalised from the shipped
`(…, actor_id, attempt)` so that P1's actorless rolls (`yield`, festering, ageing) are covered.
Two die readings exist and are DECLARED: a **pool** (count 7-9→1, 10→2) for anything with a performer,
and a **magnitude** (`(3+d10)/8.5`) for nature, which has no skill.

## 7 · WHAT MUST BE CARRIED AS OPEN, NOT ANSWERED
D-2 (act economy) · conferral basis · `stores` as denominator · S19 · Coherence-0 · off-board
polities · the closed predicate vocabulary's actual membership · `season_factor`'s distribution ·
the `Venue` tuple's 17 parameters, of which 8 appear once and carry no value.
