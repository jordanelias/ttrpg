# 02 · THE ONTOLOGY — every type, every field, every closed set

## Status: PROPOSED (2026-08-31). **HELD BACK. Nothing here ratifies on merge.**
## Under `CLAUDE.md` §0.05 this document is **REFERENCE, never mechanism.** No behaviour is correct
## because a row here says so. Under §0.2, **almost none of this runs**, and §5 of this document says
## exactly which parts do.
## Layer: **L2 — the granular type layer.** Read `00_INDEX.md` (L0) and `01_LAWS.md` (L1) first.

**Citation key.** A bare repo path resolves at the working tree (`CLAUDE.md` §2) and was opened during
this pass. `[engine]` marks a claim about published Godot behaviour, not about this repository.
`[LANE x]` marks a finding contributed by one of the six read-only adjudication lanes of `15_PROVENANCE.md`.

---

## §1 · THE SHAPE OF THIS LAYER

There are **five identity-bearing kinds, four of them carriers**; **one edge with seven kinds**; **one
state change with three modes and two drivers**; **one query category with two sides**; and **six
non-identity records** that exist only inside a season.

```
IDENTITY-BEARING, MUTABLE      Person · Rung · Office · Site              -- the four carriers
IDENTITY-BEARING, IMMUTABLE    Proposition                                -- fixed at utterance
THE ONE EDGE                   Tenure(kind ∈ hold commit contain succeed tie knot oblige)
THE ONE STATE CHANGE           StateChange(subject, mode, driver, field?, delta?, spec?)
THE QUERY CATEGORY             Query -- never stored, always recomputed, two sides
SEASON-LOCAL RECORDS           Act · Event · Claim · View · Sensation · Candidate
PERSISTENT NON-CARRIERS        Date · DocketItem · Petition · Record · Dispensation · Venue
```

**Why this exact count, and the test that keeps it honest.** Every type below carries an **N-line** —
*state the emergent possibility lost if this is cut.* A type that cannot name one is E-surplus and is
cut here rather than shipped (`NERS.md` Rule 1). Six candidate types were cut on that test during this
pass and are listed with their false N-lines at §9.

---

## §2 · THE FOUR CARRIERS

A **carrier** is an identity-bearing record with **mutable** state. There are four. `Proposition` is
identity-bearing and immutable and is therefore the fifth kind and not a carrier (§3).

### §2.1 `Person`

```
Person := (id, weight, marks[], capability, stance[], convictions, beliefs[], ledger, ties_index)
```

| field | type | domain | owner | notes |
|---|---|---|---|---|
| `id` | id | `H(world_seed, tick, subject_id, purpose)` | minted once | §6 |
| `weight` | int | `>= 1`, default `1` | Person | **a cohort IS a Person at weight > 1** |
| `marks[]` | list of mark rows | heritage · grade · Church standing · office · residence | Person | the stance table's first referent kind |
| `capability` | map practice -> rank | rank `0..5` | Person | **rank supplies dice; it gates no verb** (§2.1.3) |
| `stance[]` | list of stance rows | `(referent, valence -5..+5, weight 0..5)` | Person | referent ∈ `Person \| Proposition \| Place` |
| `convictions` | weights over the closed 13 | 1–3 primary + distributed | Person | **the moral axes.** §5.5.1 |
| `beliefs[]` | moral commitments | position ∈ strong/wavering/revised | Person | **about MORALS, never veracity.** §5.5.2 |
| `ledger` | packed claim rows | cap `L` rows, evicted on `confidence_live × recency` | Person | **what they hold TRUE.** §5.3 |
| `ties_index` | derived | — | **Nobody** | the inverse index over `tie`/`knot` Tenures; **stored nowhere** |

**Three fields that are deliberately absent, each with the mechanism that replaces it:**

| absent | replaced by | ground |
|---|---|---|
| `address` | the `contain` Tenure whose subject is this Person | one home, one writer (§4.5) |
| `needs` | `Sensation` (two scalars) + `need(p, ·)` rows, recomputed | a need cannot go stale against its own inputs |
| `occupation` | a stance row whose referent is the Proposition *"p is a fisher of Hafenmark"* | it is a thing you say you are, that others hold claims about, that can be false and contested |

#### §2.1.1 A cohort is a Person at weight > 1, and there is no conversion operation

One type. Not a subclass, not a variant record, not a flag. **This is what prevents elite-only politics
by construction:** a design with a separate cohort type gets every mechanism written for one of them
and not the other, and acquires an elite-only politics by accident.

**N-line.** Cut the unification and a mechanism written for officers does not exist for populations;
`R-4` (a system instantiated at a rung must be instantiable at *every* rung it claims) stops being
structural and becomes a review item.

> ⚠ **THE ONE ROW THAT PASSED EVERY OTHER GUARD.** A deposit into a cohort **carries a construal
> DISTRIBUTION, never a value.** One sign and one magnitude into hundreds of people is consensus
> broadcast laundered through the cohort type, and the type checker sees a single legal write. An
> individuating member **draws** from the distribution; it never inherits it.

#### §2.1.2 `weight` is the compute dial, and it is demand-driven in both directions

**Individuation** (weight `n` -> a Person at weight 1 plus a cohort at weight `n-1`) fires when an
Event names a member, or when the cohort's stance spread exceeds the bound at which one answer is
honest. **De-individuation** returns weight when **no other person's ledger names them.**

> ⚠ **THE NAMED-BY COUNT IS ONE INTEGER PER PERSON, MAINTAINED AT DEPOSIT AND EVICTION.** Evaluating
> *"no other person's ledger names them"* by scanning is `N` persons × `N` ledgers × `L` claims. At the
> design's own `L = 200` that is 200·N² claim comparisons per season. **This is not an optimisation; at
> any interesting N it is the difference between CENSUS running and not running**, and it costs nothing
> because WITNESS already visits every deposit and every eviction.

#### §2.1.3 `capability` supplies dice and gates no verb

```
option_list(p, n) = { a in ACTS : eligible(p, a, n) }

eligible(p, a, n) consults   remit                (office)
                             marks                (grade, house, Church standing, office, residence)
                             place                (presence)
                             the claims p holds   (you cannot act on what you do not know of)
                             class gates          -- of which there is EXACTLY ONE: Thread Sensitivity
                     and NOT practice rank.

pool(p, a) = attr[triad_axis(a)] + capability[a].rank + thread_pool
```

**Every act formerly "added at rank 3" folds back into its base act as a declared STANDARD** that
anyone may declare and almost nobody can meet. The act vocabulary gets **shorter**, not longer.

**Why this matters beyond tidiness.** A rank gate is a second class gate in a design that declares it
has exactly one; it is a cliff in a substrate that refuses cliffs; and it makes the design's own
advancement rule unreachable, because advancement requires *an attempt at a standard above your rank*
and the gate forbids the attempt. **Your option set is shaped by your social position — marks, remit,
where you stand, what you have been told — and not by how good you are.**

**N-line.** Cut it and the unmarked, unranked, postless person has an **empty verb set** rather than
worse odds at the same verbs, and a political design that only works for the marked, the officed and
the aligned is what remains.

#### §2.1.4 The attribute roster, and the tenth

Nine attributes on `1..7` — **Body:** Strength · Endurance · Agility · **Mind:** Focus · Acuity · Will ·
**Social:** Attunement · Charisma · Bonds. **Jordan ruled ten; the registry ships nine and the tenth is
unnamed.** `references/descriptor_registry.yaml` marks the roster IN FLUX and attribute keys `warn`,
not `block`.

> **This shape does not name the tenth attribute.** It declares the roster **a registry read at load
> time, not a literal in any source file**, so that naming it is a one-row registry edit and not a
> code change. The precedent is executing: `engine/substrate/descriptors.py` cooks bounds from the
> registry and `engine/autoload/game_state.py` asserts the roster at import, halting the engine on
> registry/dataclass drift.

Thread Sensitivity is separate and continuous, `0..100+`, `thread_pool = floor(TS/10)`. **It is the one
class gate the design declares** and it stays.

### §2.2 `Rung`

```
Rung := (id, kind, stake[], judging_set_rule, dates[], matter, envelope)
```

| field | type | owner | notes |
|---|---|---|---|
| `kind` | enum | — | the ladder, §2.2.1 |
| `stake[]` | list of stake rows | Rung | what is contested here and allocated at its dates |
| `judging_set_rule` | rule | Rung | who hears what happens here |
| `dates[]` | list of `Date` ids | Rung | the standing dates it holds |
| `matter` | typed sub-record | Rung | §2.2.2 |
| `envelope` | packed per-band counts | Rung | the demographic envelope: matter, not an actor |

**A Rung owns NO social aggregate.** No norms, no densities, no reputation, no unrest, no legitimacy.
Every one of those is a `Query` (§5.1). This is the row the whole ownership table is built to protect.

#### §2.2.1 The ladder — one type, a `kind` enum, and the naming ruled

```
Rung.kind in { person, hearth, community, settlement, territory, province, duchy, realm }
```

**`Rung` is the name.** `Node` and `Container` are both refused, and **the second refusal corrects an
earlier choice that landed on a worse collision**: [engine] `Container` is a Godot built-in — the
`Control`-derived base of `VBoxContainer` — so `class_name Container` collides *and shadows a UI type
silently*, where `Node` would have failed loudly at once.

> ⊕ **AMENDMENT — the ladder carries BOTH `province` AND `duchy`, and `hearth` is the code-side name
> for Jordan's `family`.** [LANE A, LANE C, independently]
>
> Jordan's containment axiom rules the four rungs **below settlement** — Individual, Family,
> Community, Settlement — and defers upward. The ruled hierarchy of 2026-07-13 runs
> Settlement -> Territory -> Province -> Duchy -> Country, and the shipped world data carries both
> ("3 duchies -> 14 provinces -> 35 settlements"). An architecture doc that renders the upper ladder
> as `Territory -> Duchy -> Realm` **drops Province and renames Country**, which is an adjudicator's
> extension over a verbatim ruling.
>
> **So: eight kinds, both `province` and `duchy` present.** `family` is recorded as Jordan's word for
> `hearth` in `references/names_index.yaml` using its existing `context:` precedent, because every
> shipped formula in the corpus reads `stores(h)`, `hearth(giver)` and `succeed` on hearths — a rename
> would churn hundreds of citations to gain nothing. **Both words, one object, the alias registered
> where a session meets it.**

**`person` is a Rung kind and a carrier type at once, and that is deliberate.** The ladder's bottom
rung is the person; `contain` edges terminate there. Nothing about this makes `Person` a `Rung` — the
`Rung` of kind `person` is the *address slot*, and the `Person` is who stands in it.

#### §2.2.2 `Rung.matter` is typed, one sub-record per kind

An unstructured field cannot be indexed, and four things are addressed by name inside this one.

```
Rung.matter := ( stores      : map MatterKind -> int         -- whole units, no fractional matter
               , sites       : list of Site ids              -- the Sites beneath this Rung
               , records     : list of Record ids            -- what is kept here (§7.4)
               , transmission: Tenure id | null )            -- the succeed pointer for a hearth
```

**`MatterKind` is open and correctly so** — it is a type parameter, not an enumeration. Grain, salt,
timber, ore and coin are rows in a registry, not members of a closed set in a source file.

#### §2.2.3 `envelope` is matter and does not act

```
Envelope := PackedInt32Array, one count per age band
```

Births add weight at the youngest band; deaths remove it. **Birth is envelope weight, not a `create`.**
The envelope is written at MATTER (an Event) and reconciled at CENSUS. **It has no ledger, no stance
and no act.** The cohort acts; the envelope does not. Conflating them is what produced a design in
which demography could choose.

### §2.3 `Office`

```
Office := (id, post, rung?, remit, conferral, revocation, establishment[], dates[], upkeep)
remit  := (acts[], scope_rung, binds)
binds  in { members_by_admission, persons_by_presence }
```

| field | notes |
|---|---|
| `rung?` | **optional; null is the office-cluster case.** A Dicastery, a chivalric order and a trans-settlement guild have no containment node |
| `remit.acts[]` | drawn from a **closed five**: `issue` · `determine` · `confer`/`revoke` · `dispatch` · `convene` |
| `conferral` | **the basis, PER OFFICE** — §2.3.2 |
| `revocation` | who may revoke, and at what venue. **Retained.** An earlier form silently dropped it |
| `establishment[]` | *the named persons the office employs.* Finite, contested, durable |
| `upkeep` | what the post pays its establishment out of the office's stake |

**An office adds NO verb.** It makes ordinary acts eligible where they otherwise are not, and it
substitutes the **pool source**: `pool(act by remit) = capability of the dispatched establishment
member(s) actually performing it`. **Neither the holder nor anyone else rolls differently for anything.**

> **WHY NEVER A MODIFIER — one line of arithmetic, and the constant in circulation is wrong.**
> A flat shift of size `X` on a pool roll is worth `X / (sigma_per_die · sqrt(Pool))`, which is worth
> **more to a small pool than a large one** — backwards from every intent anyone has when adding one.
>
> ⊕ **CORRECTION, found independently by two lanes that could not see each other** [LANE A C7, LANE B
> D2]. The constant quoted across the design corpus is `0.671`, derived from a die model with **no
> botch face**. The executing owner is `engine/autoload/dice_engine.py:175`: `_SIGMA_PER_DIE = 0.800`,
> because face 1 scores **−1**, not 0. Under `CLAUDE.md` §0.05 the code is the formula.
> **The correct figure is `X / (0.800 · sqrt(Pool))`.** The *rule* survives unchanged — the direction
> holds for any sigma > 0 — but the number is wrong wherever it is quoted, including in the binding
> forbidden-shapes table, and it must be corrected at adoption rather than propagated again.

#### §2.3.1 `establishment` is the office's throughput, and it is people

Under the one-act ruling (§8.1) **an office's throughput is its establishment's acts.** Every member is
a named Person with one act, their own ledger, their own stance toward the holder, and the standing
option to refuse, comply badly or defect. `upkeep` fills their larder from the office's stake, so their
own `need(subsistence)` is answered by the post and threatened by failing it.

**N-line.** Cut it and an establishment is a multiplier on its holder's hours rather than a set of
people; reach becomes a number instead of a roster; and *"an unpaid establishment does not disperse, it
becomes a faction and treats plunder as wages"* has no mechanism producing it.

#### §2.3.2 `Office.conferral` names the basis PER OFFICE — the fork dissolves, and so does one escalation

```
Office.conferral := (basis, conferrer_ref, rule)
   basis in { person_rooted, office_rooted, external }
```

A warband's oath to its captain is `person_rooted` and dies with him. A praefecture is `office_rooted`
and survives its holder. **Both ship in one primitive, and which one an office uses is world-authoring —
a fact about that institution, not a law of physics.**

> ⊕ **AND THIS RETIRES AN ESCALATION AS AN ARCHITECTURE QUESTION.** *"Is ecclesiastical office
> person-rooted, office-rooted, or rooted off-map in a Holy See?"* was escalated as a live fork on the
> ground that *the code is nearly identical and the game is not.* With `basis` typed as a three-value
> enum including `external`, **all three options are expressible with no new object and no code
> difference at all.** The choice stops being an architecture decision and becomes **one registry row
> per Church office**, which is exactly what it always was.
>
> **The game question remains Jordan's and this shape does not take it.** What changes is that
> nothing is blocked on the answer. Fiction-side evidence favours `office_rooted` for the Valorian
> offices (five independent succession and coup arcs require it; none requires `person_rooted`), and
> the shape records that as a recommendation on the *data*, not a ruling on the architecture.
>
> **Cost, stated:** `sovereign_fraction(root)` is **total only over the `office_rooted` subgraph**.
> `person_rooted` chains genuinely terminate at dead conferrers and `external` roots genuinely leave
> the peninsula. **Every caller must handle a partial answer**, and the Query's signature says so by
> returning a `(fraction, undetermined_count)` pair rather than a bare float.
> **Falsifier:** if any caller needs a total sovereignty answer over ALL offices, this fails and one
> global basis is forced.

#### §2.3.3 A conferral cycle is a first-class political condition, not an error

The Church's conferral graph cycles. **Rule the cycle intended.** A contested Church succession means
no determinate custody, which means the deciding article is ungradable for every claimant, which means
the sitting closes carried-without-force. **That is the Consecration Crisis**, and it is one arc's
Branch A and another's second act. `sovereign_fraction` returning `undetermined` over Church offices is
the mechanism producing it.

### §2.4 `Site`

```
Site := (id, rung, kind, condition, drawers[])
```

**`Site` is a carrier and `condition` is PRIMARY STATE on it.** The argument is short and decisive:

1. An accumulator that reads its own previous value **is** primary state, so `condition` cannot be a Query.
2. A draw-weighted mean over child sites has **no base case** and is not total at a leaf.
3. **Node-keying destroys site identity and yields two wrong answers at once.** A settlement holding a
   silted harbour at `0.1` and a healthy seam at `0.9` collapses to one scalar near `0.5`, which keeps
   the bulk-shipping verbs the harbour should have closed and closes the mining verbs the seam should
   have kept.

> **BASE CASE, STATED:** at a Rung with **no Sites beneath it**, `condition` is **undefined** and the
> verb gate does not fire. Not zero, not a default — undefined, and the gate does not run.

**`condition` is a fixed-point integer on `COND_SCALE`, and `COND_SCALE` is an exported params row, not
a literal in a source file.** §8.4 owns the representation.

#### §2.4.1 The world-substrate hole closes here, with zero new objects

The single confirmed omission in the design corpus — found by **three independent arc lanes by three
different routes** — is that **there is no world-substrate quantity**: nothing representing the state
of the Thread substrate the setting's metaphysics rests on. It is an *omission*, not a refusal: every
other absence in the design is argued for by name, and this one has a broken cross-reference pointing at
where it was supposed to be.

> ⊕ **RULING: a Thread seam is a `Site` of a `Site.kind` naming it, and its `condition` is the
> substrate quantity.** No new type, no new field, no new write class, no new step.
>
> **The argument the arc lane supplied and this shape accepts:** the spine refuses gauges on containers
> *because they are social*. A substrate's condition is **the same class as larders and harvests**,
> which the design already ticks at MATTER. *The shelf exists; nobody wrote the object.*
>
> **It satisfies P-5 exactly** — the fix that adds a system has failed, and this adds none. It is one
> row in the `Site.kind` registry and one `wear` row in the params table.
>
> **N-line.** Cut it and *the world is not dying, it is only being misunderstood* — and the one arc the
> corpus itself calls *the arc that must fire* is unreachable, along with five of the seven arcs
> recorded LOST.
>
> **Falsifier.** Wrong if any Thread-substrate mechanic requires a quantity that is **not** per-place —
> a single global scalar with no site identity. If the metaphysics needs one number for the whole
> peninsula, this is the wrong object and a genuinely new one is owed.

---

## §3 · THE FIFTH IDENTITY-BEARING KIND — `Proposition`

```
Proposition := (id, mood, subject, predicate, value, when, scope)
   mood in { HOLDS, OUGHT }
   when  is a MANDATORY interval
```

> **A carrier is identity-bearing and MUTABLE. `Proposition` is the one identity-bearing IMMUTABLE
> record — fixed at utterance, never destroyed. Five identity-bearing kinds. Four carriers.**

This costs one sentence and closes a real seam: it is why **a faction can be fully derived from a
Proposition plus its `commit` edges without the Proposition being a fifth owner.**

>  ⊕ **AND THE UNIFICATION THAT MAKES THE POLITICS PERSONAL.** A `Proposition` of mood **`OUGHT`** is
> **an uttered `Belief`** (§5.5.2). A Belief is the private moral commitment; saying it aloud makes a
> Proposition, which other people can then `commit` to, argue against, and collide with.
>
> **So a faction is somebody's morals, said out loud, that other people signed** — and that is the type,
> not a metaphor. `Proposition` + `commit` edges **is** the faction (§3.1); the Proposition **is** the
> uttered Belief; the Belief **is** one person's account of what ought to be. **The whole political layer
> is grounded in a single person having said what they think is right.**
>
> **N-line.** Cut the identification and a faction's proposition is an authored banner rather than
> somebody's conviction — **nobody can be a hypocrite, and a movement cannot be discredited by what its
> founder does.**

**`when` being mandatory is what makes collision free.** Two propositions with intersecting scope and
incompatible values **collide automatically**, computed at deposit time, in one ledger at a time. There
is no consensus object and no signature that could build one.

**Falsifier.** Wrong if any Proposition field is ever mutated after utterance.

### §3.1 A faction IS a Proposition plus its `commit` edges

**The Faction row is deleted from the ownership table, and the deletion is stated as an amendment
because the row existed.** Membership is `commit`; leadership, presence, density and footprint are
Queries; the persistent part is the immutable Proposition.

| what a faction "has" | where it actually is |
|---|---|
| members | the `commit` Tenure set |
| leadership | `leaders(prop, rung)` — a Query. **Deposition is this query returning somebody else** |
| scale | **derived as a presence/density/footprint profile**, never a `tier`, `level` or `scale` field |
| footprint, density | Queries |
| its identity | the immutable Proposition |
| institutional memory | Records kept at a Rung (§7.4) |

**A faction has no verbs of its own.** It acts by acting through the persons it contains, at whatever
rungs they sit.

> ⚠ **WHERE THIS COLLIDES WITH RUNNING CODE, AND IT DOES.** `engine/autoload/game_state.py:109-137`
> ships `Faction` as a stat-bag: six stored floats (`L`, `Sta`, `W`, `I`, `Mil`, `intel`) plus stored
> `standing`, `territories` and per-arc flags, written by **31 non-test `.adjust()` sites, of which 20
> write `L`** [LANE D, counted independently; matches the AST count the module itself carries].
>
> **And a second fact that matters more than the first:** **30 of those 31 sites bypass the Key
> substrate entirely.** Only `engine/cross_scale/echo_transport.py` is Key-mediated. So *"all state
> change flows through the event channel"* is **false of the executing tree**, and any plan written as
> though it were true is planning against a repository that does not exist.
>
> **This is not a base to refactor and it is not a thing to delete on a Tuesday.** `09_PYTHON_ORACLE.md`
> §4 sequences it as **build-beside, flag-gate, golden-control, cut over** — the repository's own
> established path — because adopting the ownership table day-one invalidates the entire executing game
> at once, unattributably, which is precisely what `CLAUDE.md` §0.1 point 4 forbids.

---

## §4 · THE ONE EDGE — `Tenure`

**This is the record every disputable political fact is made of.**

```
Tenure := (id, subject, object, kind, since, until?, conferrer?, degree?, payload?)
   subject   in Person | Rung | Proposition
   object    in Person | Rung | Office | Site | Proposition
   conferrer in Person | Office | null
   kind      in hold | commit | contain | succeed | tie | knot | oblige
```

### §4.1 The seven kinds, with cardinality declared on the schema

| kind | subject -> object | what it is | created by | destroyed by | **cardinality** |
|---|---|---|---|---|---|
| `hold` | Person -> Office | office | `confer` | `revoke` | **1 per Office** |
| `hold` | Person \| Proposition -> Site \| Rung | enfeoffment, lordship, **annexation** | `confer` | `revoke` | **1 per object** |
| `commit` | Person -> Proposition | faction membership at a degree | `commit(+d)` | degree -> 0 | 1 per (subject, object) |
| `contain` | Person -> Rung, Rung -> Rung | address; the containment tree | `admit`, `migrate` | **never bare** | **1 per subject** |
| `succeed` | Rung -> Person | the hearth's succession pointer | a naming act | re-naming | **1 per Rung** |
| `tie` | Person -> Person | ordinary contact | co-presence | decay | 1 per unordered pair |
| `knot` | Person -> Person | the deep channel | `form_knot` | rupture | 1 per unordered pair |
| `oblige` | Person -> Person | kin obligation | kinship, admission, oath | discharge, death, repudiation | 1 per (subject, object) |

> **CARDINALITY IS DECLARED PER KIND, ON THE SCHEMA, AND THE CONFLICT RULE READS IT.** Two acts
> conflict if they both `create` edges that jointly break a declared cardinality.
>
> **Without this, the invariant breaks only after both acts resolve.** Two `succeed` edges on one
> hearth, two `hold` edges on one office and two `contain` edges on one person are **each individually
> legal**, no conflict fires, and nothing errors — while single-parent containment, the derivation the
> whole design rests on, evaporates silently. `presence` and `sovereign_fraction` leave `[0,1]`,
> `draw_share` stops summing to 1, and a judging set votes one person twice.

### §4.2 `payload?` per kind — the kind's own record

| kind | `payload` |
|---|---|
| `commit` | `(avowal in { avowed, private, covert })` — **a three-state domain, never an `avowed?` boolean** |
| `knot` | `(depth in {1,2}, strain)` — **one shared `strain`**, stored once |
| `tie` | `(familiarity, last_contact, channel_class)` |
| `hold` | `(scope_note)` where the remit is narrowed below the Office's own |
| others | null |

### §4.3 `tie` and `knot` are stored ONCE, on the endpoint with the lower id

A shared `strain` gauge on a directed record otherwise has **two homes and can disagree with itself.**
The other endpoint reads it through the derived inverse index.

### §4.4 `until?` is what makes a destroyed tenure a fact

A revoked tenure is a **historical claim subject** — argued over, read for entrenchment, cited in a
succession dispute. Without it, re-conferral after revocation is indistinguishable from an unbroken
tenure and `entrenchment(h, H) = min(1, seasons_held / 60)` has nothing to read.

**Cascade on destruction is declared, not discovered:** `destroy` sets `until = tick` on every Tenure
whose subject or object is the destroyed id, **and destroys nothing else.**

### §4.5 `contain` is never destroyed by a bare `revoke`

A person's address is their path to the root. Revoking their `contain` edge orphans them; revoking a
Rung's orphans a subtree. **Migration and secession are `confer` to a different parent, atomically, in
one act.** There is no operation that leaves a subject unparented, and destroying a Rung additionally
requires its `contain` children to have been re-parented **in the same act**.

### §4.6 `annex` and `secede` are not verbs and are deleted from the vocabulary

**Annexation is a `hold` Tenure over a Rung changing hands. The tree does not move.** This is Jordan's
own ontology — *the tree is geography, allegiance lives in factions, a hamlet does not move because a
King won a war.*

`secede` is additionally **barred as a word**, because the corpus already ships *secession* for a duke's
**defection**, which is a `commit` moving away. **A duke defects (`commit`); a territory changes hands
(`hold`); a hearth moves parents (`confer` on `contain`). Three operations, three words, no collision.**

### §4.7 EVERY TENURE IS OWNED BY ITS SUBJECT, WHICHEVER CARRIER THAT IS

> **One home, one writer, no reach-through. The object side is a derived index, never stored.**

Stating this only on the Person row leaves `succeed` (a Rung subject) and `hold` (which permits a
Proposition subject) unowned, and the Rung and Office rows silent about Tenures altogether.

**Falsifier.** Wrong if any Tenure kind needs to be stored on its object for a real access pattern.

### §4.8 The `hold` collision, recorded and disarmed — five meanings, one in running code

| meaning | spelling that survives |
|---|---|
| the Tenure kind | `Tenure(kind=hold)`; exported `tenure.hold`; **never a bare `kind: hold`** |
| the Proposition mood | `HOLDS`, capitalised |
| the predicate form | `HOLDS(p, x)`, **always written with its arguments** |
| the coercion quantity | `Hold(n, targets, giver)`, capitalised, **banned from act preconditions** |
| ⚠ **a mass-battle unit's tactical stance — LIVE CODE**, `systems/mass_battle/sim/config.py` | the bare string stays **inside that module** and is never exported |

**A meaning in executing code outranks a meaning in prose** (`CLAUDE.md` §0.05), so the disambiguation
had to survive the fifth one, and the register that first ruled on `hold` did not know it existed.

---

## §5 · THE ONE STATE CHANGE, AND THE QUERY CATEGORY

### §5.1 `StateChange`, and Jordan's Partition as a schema column

```
StateChange := (subject, mode, driver, field?, delta?, spec?)
   mode   in { create, alter, destroy }     -- CLOSED: begins to exist / changes / ceases to exist
   driver in { Act, Event }              -- CLOSED: the Partition is total on the schema column
```

> **PARTITION EVERY STATE CHANGE BY ITS SUBJECT.** A change whose subject is peninsular human society —
> polities, institutions, offices, organizations, occupations, religion, settlements, marriage — is
> **driven by a character's choice, always.** A change whose subject is anything else — weather, the
> non-peninsular, tears in the metaphysical substrate — is **an event acting on the world.**
> **Creation and destruction included.**

> ⊕ **AND THE MEMBERSHIP TEST IS A STATIC SCHEMA COLUMN, NOT A JUDGMENT.**
>
> **`social` IS A STATIC BOOLEAN ON THE `(record-kind, field)` PAIR, DECLARED IN THE EXPORTED SCHEMA
> AND READ BY THE RESOLVER — AND THE RULE IS ASYMMETRIC.**
>
> ```
> social: true   =>  ACT-DRIVEN ONLY.  An Event may never write this row.
> social: false  =>  EITHER DRIVER.    An Event may write it, and so may an act.
> ```
>
> ⚠ **Stating this as a biconditional is FALSE, and an earlier draft of this section did.** A
> restoration **act** writes `(Site, condition)` — a `social: false` row — every season it is performed.
> **`wear` and a tending act land on the same field by design**, and that is the whole flux model.
> **The row does not say who may act. It says what an EVENT may not touch.**
>
> A predicate a programmer must adjudicate per instance is a convention, not a mechanism, and it drifts
> at the first hard case. As a column the test is decidable **at the call site and at load time**.
>
> **And it reproduces Jordan's own worked example exactly:** `(Site, condition)` is `social: false`, so
> a plague or `wear` may move it; `(Rung, exists)` is `social: true`, so **a plague may kill every body
> in a village and may not destroy the village.** The village empties and still legally exists until an
> office strikes it from the roll.
>
> ⊕ **AND `exists` IS A RESERVED PSEUDO-FIELD, KEYED BY MODE — because a create/destroy row has no
> `field` at all.** `StateChange.field?` is absent on `create` and `destroy`, so `(Rung, exists)` has
> **no lookup key** unless one is declared. **Declare it: `mode in {create, destroy}` resolves to the
> reserved field name `exists` for the subject's record-kind.** Without it the Partition's entire
> creation-and-destruction half — the half carrying *a plague may not destroy a village* — **has nothing
> to look up.**
>
> ⚠ **THE CONCESSION THE SOURCE MAKES, AND WHY THE KEY IS THE FIELD RATHER THAN THE SUBJECT.** Stated
> over *subjects*, the Partition concedes a mixed class in its own worked cases — *a plague is biology
> but it empties institutions; a famine is weather times tending* — and the ruling there reads
> **event · both · choice**. **"Both" is not a partition.** Keyed on `(record-kind, field)`, a plague is
> not one change with a disputable subject but **several, each writing a different field**, each
> answered separately. **The mixed class dissolves because there was never one change to classify.**
>
> **Falsifier.** Wrong if any state change's driver depends on the *instance* rather than on the
> `(record-kind, field)` pair — or if any single field genuinely needs an Event to write a
> `social: true` row.

**`read` and `exclude` are NOT modes.** They live on the Act: `reads[]` declares what the act consulted
(so the conflict graph can see it) and `contests[]` declares what it disputes (so the contest router
can). Folding them into `mode` was what made the conflict rule quantify over a field the record did not
carry.

> ⊕ **RULED — the modes are `create` · `alter` · `destroy`, and the coinages are dropped.**
>
> The design line carried `mint` and `efface`, kept under protest on a **collision-avoidance** ground:
> that `create`/`destroy` are near-universal identifiers likely to collide in GDScript.
>
> **That ground does not survive inspection, on two counts.** First, the collision argument is about
> *method names*; these are **enum values on `StateChange.mode`**, written `Mode.CREATE`, and they
> collide with nothing. Second, the one live "mint" occurrence a lane offered as evidence of an
> existing token turned out to be an **English comment**, not an identifier [LANE F B3].
>
> So `CLAUDE.md` §4's two tests decide it unopposed. **Idiomatic in choosing:** `create` and `destroy`
> are the words ordinary usage supplies. **Idempotent in meaning:** a later session reading `efface`
> cold will not reliably recover *delete* — and there is no context between sessions, which is the
> whole reason the rule exists.
>
> **`mint` survives in exactly one place, because there it is the right word and names something
> `create` does not:** `witness` **mints a root token**. That is a minting — a new, authoritative,
> traceable origin brought into existence — and it is the one operation in the design that does it.
> **Three modes, one reserved verb, no coinage.**

### §5.2 `Query` — never stored, always recomputed

**The rename off `Derived` is not cosmetic and was verified necessary.** `references/glossary.md`,
`references/descriptor_registry.yaml` and the params capture all use *Derived* for **stored**
per-character values in a flat global namespace — the exact opposite meaning. [engine] And a prose
qualifier does not travel into GDScript's flat, global `class_name` namespace.

| class | takes | may read | examples |
|---|---|---|---|
| **resolver-side** | **`World` as the FIRST parameter** | world truth | `leaders`, `presence`, `density`, `footprint`, `verbs(w, site, c)`, `condition` at a rung, `sovereign_fraction`, `filter_share`, `judging_set`, `draw_share` |
| **person-side** | the asker | **the asker's own interior only** — ledger, stance, capability, remits, and the `Sensation` computed this step | `opening_set(person, view)`, `entrenchment`, `norm_as_claimed`, `address`, `trace(person, claim)` |

> **PUTTING `World` FIRST ON EVERY RESOLVER-SIDE QUERY IS THE ENFORCEMENT.** Calling one from inside
> `choose` then **fails at the call site for want of an argument.**
>
> **This suite's own catalogue is 25 rows — 18 resolver-side and 7 person-side**
> (`08_FUNCTION_SURFACE.md` §2). With the three top-level signatures that is **21 call sites that fail
> for want of an argument**; the 7 person-side rows are enforced by the opposite omission — they take no
> world and cannot acquire one.
>
> ⚠ **DO NOT QUOTE AN ADDITIVE TOTAL.** A *"23"* circulates in three places over a differently-scoped
> table of 20 rows, and it is `3 + 20` — **a sum that names nothing.** Adding this suite's 25 to 3 would
> re-mint the identical error with a new number.

> ⊕ **AND A CACHE RULE, WITHOUT WHICH THE PARALLELISM LICENCE IS A DATA RACE.**
>
> **A Query MAY be cached. The cache is built AT A BARRIER, is READ-ONLY until the next barrier, and is
> DISCARDED there. NOTHING INSIDE A MAP BUILDS ONE.**
>
> A barrier-scoped rebuild from primary state is compute-on-demand at barrier granularity: it stores no
> state that can go stale, because it does not survive the barrier. **A cache built inside the map is
> both a race and a stored aggregate**, and *"compute-on-demand, never push, never store"* reads to most
> engineers as licensing exactly that.
>
> **This is not an optimisation note.** Six operations are O(N²) without it — de-individuation,
> `presence`/`density`/`footprint`, `judging_set`, `draw_share`, WITNESS fan-out, and the coarse
> `condition` read — and **the population ceiling is then set by CENSUS's scan rather than by anything
> the designer chose.**

**Executable precedent exists and should be copied, not re-derived:** `canon_buckets.canonical_accord`
and `descriptors.faction_bounds` are already Query-shaped — computed, not stored.

### §5.3 `Claim` and the ledger

```
Claim  := (id, holder, subject, predicate, value, when, source, confidence, visibility)
source in { firsthand(event_id)
          , told_by(person | record, handle)
          , inferred(claim_id...)
          , firsthand_via_knot(event_id) }        -- CLOSED at four
```

**The predicate vocabulary is CLOSED at fourteen forms and the referent space is OPEN**, because
collision, entailment and relevance are all functions of the predicate's *form*:

`LOCATED · DID · HOLDS · MARKED · CONDITION · ALIGNED · TIED · QUANTITY · IN_FORCE · INTENDS · SAID ·
CAUSED · CONTRADICTED · HOLDS_STANCE`

**A fifth claim source was proposed and correctly withdrawn.** `research(archive, question)` already
produces `told_by(record, ...)` with **verified** rootprints, and *archives are the only non-person
root-bearers.* **A record is a speaker that cannot lie and cannot be interviewed** — its rootprint is
*verified* where a person's is *asserted*, and that is the entire difference.

**`witness` is the only operation that MINTS a root token.** `examine`, `surveil` and `Thread-Read`
register **facets** that `resolve` emitted and `witness` turned into tokens; `reconstruct` **unions**
existing roots and refuses an inference over an empty union; `interview` and `research` produce
`told_by`, which **copies** tokens. **Four constructors, no fifth, and no path to a fresh token outside
`witness`.**

**Eviction ranks on `confidence_live × recency` ONLY, never on salience** — otherwise motivated
retrieval becomes motivated deletion. Retrieval is a different function and ranks differently (§5.4).

### §5.4 `View`, `Sensation`, and how anything reaches a decider

```
View      := PackedInt64Array of claim ids            -- ids, never references
Sensation := (subsistence, standing)                  -- EXACTLY two scalars
```

**`View` is built, not filtered.** It is assembled from the person's own ledger by a bounded query. It
is *smaller than* the truth the way an **empty room** is smaller than a furnished one — not blurrier.
**Absence of a claim produces absence in the view, never a widened interval**, because a widened interval
is uncertainty and the design needs ignorance.

```
view(person, question) -> at most K claims,   K = 7 + Focus + 2 per Knot consulted - Coherence penalty

salience(c) = recency(c) x confidence_live(c) x relevance(c, q) x stanceweight(c, person)
stanceweight(c) = clamp(1 + lambda * agreement(c), 0.05, 2.0),   lambda = obstinacy / 5
```

**What is attenuated is RETRIEVAL, not value.** This is why eviction must rank on a different function.

> ⊕ **THE SLATE IS THIS SAME MECHANISM AT PLAYER FIDELITY, NOT A SECOND ONE.** [LANE B A9/B13]
>
> The most-worked treatment of *how anything is put in front of a decider* in the corpus is the Slate:
> a candidate contract, a **cast gate** and a **rank**, composed as `gate THEN rank` and **never summed**.
> It has been read as a player-facing module. **Under `R-4` — a system instantiated at a rung must be
> instantiable at every rung it claims — a player-only attention module is forbidden.**
>
> **So there is one attention mechanism, and `view()` and the Slate are its two fidelities:**
>
> | | NPC fidelity | player fidelity |
> |---|---|---|
> | gate | the claim is in the ledger | `witness.channel` is one of five, non-empty |
> | rank | `salience(c)` | `cast_score(c)` = meaningfulness x inertia x scale_weight |
> | budget | `K = 7 + Focus + ...` | `B` opportunities, canon, per difficulty |
> | depth | n/a | `depth_score` — **decides render depth among the cast, NEVER entry** |
>
> **The severance is load-bearing and is carried:** casting keys on the tie-graph and **realized** state
> only; forecast and imminence govern render depth and may never impel a future at the player.
>
> **A candidate may not be cast on the strength of its salience alone**, and no term in either score may
> raise a candidate over the gate. **A barred candidate is not suppressed; it arrives thinner** — a
> Thread-constituted situation reaching a non-sensitive is cast through its surface effects with the
> Thread-level payload absent. That is inaccessibility, not suppression, which is what P-08 asks for.
>
> ⊕ **AND ONE TERM IS CUT ON ITS OWN N-LINE.** `forecast_mass` **has no producer anywhere in the
> corpus.** Under `NERS.md` Rule 1 an object that cannot name what is lost by cutting it is surplus:
> **cut it, or produce it, and this shape cuts it.** `depth_score` reduces to
> `cast_score x imminence(horizon.band)` until something produces the term.

**`Sensation` is exactly two scalars and it exists because there was no legal path from a need to the
function that uses it.** Subsistence and standing read *the world*; needs are pure and never stored; the
View is assembled from claims only. `Sensation` is computed inside DELIBERATE by `sense(person,
frozen_world)` — **which is not a decision function and may therefore take a World** — is never stored,
carries no references, and answers no query.

**Two scalars, not four:** commitment and exposure read the *view* and are computed inside `choose` from
what the person already holds. **Their formulas are in `05_FUNCTION_SURFACE.md` §4** and they are the
half of the motive engine that was measured absent — *for a magnate the other two return zero, so 100%
of a duke's motivation was uncomputed.*

**A Sensation is un-nameable, therefore undisputable.** No person can hold a claim about another's
hunger. Claims reach the larder and the body and stop there.

### §5.5 THE MORAL LAYER — `Conviction`, `Belief`, `Duty`, and why none of them is a Claim

> ⚠ **THE COLLISION THIS SECTION EXISTS TO PREVENT, AND IT IS THE MOST DANGEROUS ONE IN THE SUITE.**
>
> **A `Belief` in this game is about MORALS. It is NOT about the veracity of information.** [Jordan,
> this session.] Every earlier draft of this suite used *belief* as the ordinary English word for
> *what a person holds true* — which is **`Claim`** — and that usage is purged, because it collides
> head-on with a shipped game object meaning something else entirely.
>
> **What a person holds TRUE is a `Claim`. What a person holds RIGHT is the moral layer below.**

```
Conviction  -- a moral AXIS. Thirteen, canonical, closed, registry-owned.
Belief      -- a moral COMMITMENT: this person's own statement of what ought to be,
               backed by Convictions, revisable under SOCIAL pressure and never by evidence.
Duty        -- an OBLIGATION owed to a faction, a kin group or a culture. Not chosen; borne.
```

| | `Conviction` | `Belief` | `Duty` | vs. `Claim` |
|---|---|---|---|---|
| **what it is** | a moral axis a person weights | a person's own moral statement | an obligation owed | **a proposition held true** |
| **who authors it** | canon — a closed roster | **the person** (the player, for a player character) | the institution or kin that binds them | the world, via `witness` |
| **what moves it** | slowly, by scar and crisis | **social pressure**, at RESOLVE | conferral, oath, kinship | **evidence**, at WITNESS |
| **what refutes it** | **nothing refutes an axis** | **nothing REFUTES it — it is CHALLENGED and may be revised** | discharge, death, repudiation | **a colliding claim** |
| **write class** | INTERIOR | ACTS | ACTS | **INTERIOR** |

> **THE LINE, STATED ONCE SO IT CANNOT DRIFT: EVIDENCE MOVES CLAIMS. ARGUMENT AND CONSEQUENCE MOVE
> BELIEFS.** A man shown proof the harbour is silted has a new **claim**. A man shown that his own
> position cost his neighbours their livelihoods has a **belief under revision pressure**. **The first
> is discovery; the second is a moral crisis, and no amount of the first produces the second.**

#### §5.5.1 `Conviction` — the axis roster

**Thirteen, closed, canonical:** Faith · Authority · Order · Scholastic · Utility · Equity · Liberty ·
Precedent · Community · Identity · Warden · Virtue · Honor. **A person carries one to three PRIMARY
convictions plus distributed weight** — the primaries are what they will pay for; the distribution is
what they will notice.

> ⊕ **THE ROSTER IS A REGISTRY READ AT LOAD TIME, NEVER A LITERAL — for a reason the tree paid for.**
> Two modules shipped **rival rosters of nine and eight names, overlapping in three.** The cost was **a
> silent no-op**: the one live caller passed a name present in one roster and absent from the other, **so
> the effect never landed while the caller reported that it had.** That is the read/write asymmetry
> hazard exactly, and it is why the roster resolves through the registry, is exported behind a blocking
> round-trip, and **raises on a non-member** rather than returning nothing.

#### §5.5.2 `Belief` — a moral commitment, and the one record the PLAYER authors

```
Belief := (id, holder, statement, position, underlying_convictions[], revision_pressure, history[])
          position in { strong, wavering, revised }
```

**It is the one record in this shape a player writes directly**, and that is deliberate: **a player
authors what their character stands for, and the engine authors everything else.**

- **It is not a stat and grants no bonus.** It grants **Momentum** for aligned action — spendable,
  capped, per-scene — which is **a choice**, where a bonus is arithmetic. **Acting on principle gives
  you something to spend, not a better chance at things.**
- **It is CHALLENGED, never refuted.** A social success adds **revision pressure**; revision is **its
  own act, taken by the holder.** *Nobody argues you out of your morals in one exchange, and a design
  where they can is one where morals are hit points.*
- **It is backed by Convictions**, so revising one is a tremor in the axis beneath it — which is where
  the setting's coherence machinery already lives.

**N-line.** Cut `Belief` and a character has appetites and obligations and **nothing they would refuse
an advantage over.** Every dilemma reduces to cost-benefit, because nothing records what this person
will not do. **The moral fork has no carrier at all.**

#### §5.5.3 `Duty` — the obligation you did not choose

**Borne, not authored** — and its mechanism is already here: an **`oblige` Tenure**, plus the `commit`
degree that prices a requisition. **`Duty` needs no new record**, and this shape adds none. It is named
because **leaving it unnamed is how it gets re-invented as a stat**, and because the distinction only
works with all three terms on the page: *what you hold right, what you weigh, what you owe — and,
separately from all three, what you hold true.*

#### §5.5.4 Where the moral layer meets the loop

| step | what the moral layer does there |
|---|---|
| **CALENDAR** | nothing |
| **MATTER** | nothing — **morals are not metabolism** |
| **DELIBERATE** | Convictions weight the option ranking; **a Belief is what makes a costly option choosable at all** |
| **RESOLVE** | Momentum gained for aligned action and spent; a challenging outcome adds **revision pressure**; revision is an act |
| **WITNESS** | **nothing.** Witnessing deposits **claims** |
| **CENSUS** | nothing |

> **The WITNESS row is load-bearing.** If evidence could move a Belief, **investigation becomes moral
> re-engineering** and the epistemic layer becomes a persuasion system. **They are separate layers, they
> meet only inside `choose`, and `choose` is where a person decides what to do about the gap between what
> they hold true and what they hold right.**

---

## §6 · IDENTITY

> **IDS ARE MINTED FROM THE DETERMINISM SUBSTREAM AND FROM NOTHING ELSE.**
> ```
> id(x) = H(world_seed, tick, subject_id, purpose)
> ```

> ⚠ **THE EVENT-CREATE CASE HAS NO SUBJECT TO KEY FROM, AND NEEDS STATING.** When an **event** creates
> something — a landslide exposes a seam — there is no acting subject and the created object does not
> exist yet, so `subject_id` is undefined on both sides. **Key it from the LOCUS: the id of the Rung or
> Site the change lands at, plus a `purpose` naming the event row and its slot.** Every event has a
> place; nothing in this design creates something nowhere.

`purpose` is a short discriminator naming the operation and, for a multi-`create` act, its slot:
`create:0`, `create:1`, `yield`, `festering`, `ageing`, `attempt:2`. **Its domain is open and its stability
across runs is the determinism requirement** — changing a `purpose` string changes every id downstream
of it.

**One mechanism closes two problems filed separately.** Ids are deterministic, order-independent and
unique **without a shared allocator** — and a shared allocator is exactly the mutable global that would
break the per-person parallelism licence. **There is no id service, no counter, and nothing to
serialise on.**

**This is copied from the executing substrate, not re-derived.** `engine/substrate/keys.py` carries
`Key.id: str`, enforces id-uniqueness as invariant 1, **raises** on a `causes` entry naming an unknown
id (invariant 3), is cycle-free by construction for an append-only log, and exposes
`KeyLog.content_hash()`. All six invariants were read this pass.

> ### STANDING NOTE — DO NOT "FIX" IDS INTO POINTERS
>
> Storing ids and resolving them looks like avoidable indirection to anyone who knows the engine.
> **It is load-bearing for a reason the design did not originally know it had: [engine] Godot has no
> cycle collector.** `RefCounted` is reference-counted only, so a reference cycle is a permanent leak.
>
> **And this reference graph is cyclic by construction.** `succeed ∘ contain` — Rung -> Person -> Rung —
> is the *normal* case, because the heir lives in the hearth. Ties and knots are symmetric. Claims cite
> claims. Conferral paths may cycle.
>
> **Ids break every one of those cycles at the storage layer.** Anyone proposing typed object references
> instead is proposing an unbounded leak in the object graph the game is made of.

**`H` is an owned, versioned mix — never the engine's built-in `hash()`.** [engine] GDScript integers
are signed 64-bit and `<<` on a high bit produces a negative number, and
`RandomNumberGenerator.seed` takes an unsigned 64-bit value, so the mix must be written with explicit
masking **and the same masking must exist in the Python oracle**. **Ids are save-critical: a hash that
differs between the two languages silently forks every id in the game.**

**[engine] JSON loses integer precision above 2^53.** Ids cross between the two repositories as
**strings**, never as JSON numbers.

---

## §7 · THE PERSISTENT NON-CARRIERS

These have ids and persist; none is a carrier, because none owns mutable state that anything else reads
as truth.

### §7.1 `Date`, `DocketItem`, `Petition` — the up-stroke's spine

```
Date       := (id, holder, form, when, capacity, convener_office?, docket[])
              holder in Rung | Office
DocketItem := (id, date, matter, placed_by, placed_at)
              matter in Petition | Motion | Report | Conferral | Determination
Petition   := (id, petitioner, proposition, respondent_venue, backing[])
```

> **A DOCKET ITEM IS A FIRST-CLASS OBJECT CREATED BY AN ACT.** `carry(person, petition, date)` creates a
> DocketItem on that Date's `docket[]` and `alter`s the Date. **That is what gives a matter a clock**,
> and it is what makes lapse computable: a petition lapses when the Date its item sits on passes without
> the item being reached.

> ⊕ **AMENDMENT — the addressable thing is a VENUE, not a container.**
>
> `Petition.respondent` naming a Rung or Office makes **every office cluster in Valoria politically
> unaddressable** — four Dicasteries, the chivalric order, every trans-settlement guild, the covert
> body — because a cluster has no containment node. That was accepted as the price of the correct rule
> *an institution must never be rendered as a speaker*; **the second half does not follow from the
> first.**
>
> **A cluster has no container. It has a date and a door.** `respondent_venue` is a `Venue` whose
> `container` field may be a Rung, an Office, or **NONE** — and the containerless venue is not new: a
> private negotiation was already ruled to be exactly that.
>
> **The price survives exactly.** You still address a person — the convener — and he can still drop you.
> What changes is that the petition has somewhere legal to be filed, so **being refused becomes
> distinguishable from having nowhere to ask**, which is the whole of the up-stroke: *the specific
> injury of being heard and refused.*

**Backing is the aggregation, and it is why there is no crowd object:** *a town's demand* is a petition
with four hundred backers.

**`compose_agenda` is an ACT** costing the convener one of his acts, ranking the items *he holds a claim
of* by his own valuation and admitting the top `capacity(date)` — **and an omitted petition is a DROP
and deposits exactly as one, when its backers learn of it.** Burial is not free; it is merely safe.
**The convener holds the cheapest real power in the game** — five independent season lanes found this
separately — and this is the object that makes it so.

### §7.2 `Venue` and `door`

```
Venue := (container?, prize, standing_date, judging_set_rule, decision_rule, admission_floor,
          privileged_custody, exchange_budget, article_count, coupling_depth, veto_holders,
          record_custody)
door  := (convener, enter, speak, admissible_source, attendance_cost)
```

**Exclusion is at the second gate, not the first.** A fisher may walk into the court; he may not *speak*
unless a person with standing carries his petition. **Caste is not a locked door; it is a room you may
stand in silently.**

> ⊕ **A COUNCIL IS A VENUE WHOSE DOOR PREDICATE READS AN OFFICE.** The most populous character type in
> the setting — the councillor — appeared in no venue table, and the fix is **four table rows, not a
> mechanism.** A council is not a community (its members live elsewhere; no address changes, no mark is
> conferred) and not a faction (a faction *is* a proposition; a council's members disagree, and that
> disagreement is its function — a body whose identity was a proposition could not hear a motion against
> itself).
>
> **And reading two rows against each other makes a whole duchy's character arithmetic.** A duke who did
> not confer his council's seats — they are heritable deed-seats with no living conferrer — **holds
> neither item order nor a veto over his own council**, while a duchess who summons hers holds both. One
> heritable-versus-appointed field, two duchies that play completely differently, **no special case
> anywhere.**

### §7.3 `Dispensation` — the down-stroke's object

```
Dispensation := (id, issuer, proposition, scope, terms[])     -- NINE typed terms, no bare effect field
```

**It travels by being noticed, not down a chain of posts.** Publishing is a `tell`, so it distorts in
transit, and what reaches the hamlet is often not what the Duke signed.

**Then nothing further is needed:** the person's own need plus capability plus this new claim yields an
opening through the same `opening_set(person, view)` any act comes through, now evaluated over changed
**claimed** terms. **No one authored an opportunity for anybody.**

**A published dispensation does not apply — it lands as a compliance contest**, per relevant Rung,
through `contest`, and **scope enumerates EXECUTORS, not places.** Delivery is not assumed, and an
executor who never received it is **distinct from one who received it and refused.**

### §7.4 `Record` — the only non-person root-bearer

```
Record := (id, rung, kind, forgery_quality, subject_matter)
          kind in { register, charter, deed, roll, letter }
```

It earns its place twice in shipped text: `admissible_source` is a Venue door (*a venue that hears
instruments only cannot be reached by forty hamlet witnesses*), and a document's `forgery_quality` is a
named resistance pool.

> **IDEAS ARE PURGED AT THE VENUE, NOT IN THE LEDGER.** You cannot delete another person's memory and
> the design is right to forbid it. What can be destroyed is an **idea's STANDING**, and `strike` already
> does it — *it kills the ground at every venue for everyone*, publicly, by a named person, on a named
> fault. Which is how heresy, attainder and the discrediting of a witness actually work.

**And burning the archive drops confidence only for claims that actually cited it — gated on a claim
reaching the holder.** Without the gate, a burned register drops a fjord fisher's confidence in the same
tick, six weeks before news of the fire could reach him. **Arson's effect maps onto the news map**,
exactly as a death does.

**Forgery is `plant`, and it is shipped.** It produces a document whose root token was minted by the
planting act but which asserts the root of a genuine issuing. **Until discovered it is true for every
purpose that reads claims**, because there is no true-state path in `choose`. Discovery is `reconstruct`
succeeding on the forged root; then **legitimacy flips retroactively for exactly the people who learn,
at the speed the news travels** — never as a global flag.

### §7.5 `Candidate` — the emitter contract

A candidate is **derived, never stored**: a value an emitter returns at the accounting boundary. Six
rules, all normative, and each names the failure it prevents.

| # | rule | the failure it prevents |
|---|---|---|
| **C-1** | `provenance` is **required and non-empty** — the id of the Key that caused it | a situation appearing for no reason. **In a game with no GM this is the property that makes the layer trustworthy** |
| **C-2** | `witness` is **required and non-empty**, one of five channels | a salient thing the player cannot know about leaking through |
| **C-3** | an emitter supplies **realized-state terms only** | world-visible imminence; *never publish the trigger* |
| **C-4** | `resolver_ref` names a module that already exists and resolves it **at both fidelities** | **a second, cheaper resolution path** — the seam every community in the genre finds and exploits |
| **C-5** | `responses` are 3–5 ids drawn from `resolver_ref`'s **declared** option set | verb creep: a candidate that could invent its own responses routes around the cap |
| **C-6** | an emitter **emits**; it never presents, ranks, or checks the budget | the reason this is one function and not eight competing ones |

`informational: true` is the exemption from C-4/C-5 and only that: **news, not a situation** — rendered
and never resolved.

---

## §8 · THE CLOSED SETS, EACH JUDGED

**A set declared closed that is in fact open is a fence someone will climb.**

| set | members | genuinely closed? |
|---|---|---|
| `Tenure.kind` | `hold, commit, contain, succeed, tie, knot, oblige` | **YES** — each carries a distinct cardinality rule, and a new kind needs a new rule, which is the right friction |
| `StateChange.mode` | `create, alter, destroy` | **YES** — exhaustive over begins/changes/ceases to exist |
| `StateChange.driver` | `Act, Event` | **YES** — the Partition is a total function on the schema column |
| `Claim.source` | four constructors | **YES**, and the proposed fifth was correctly withdrawn as already covered |
| predicate forms | fourteen | **closed with a stated test for a fifteenth** — the honest form |
| write classes | `CALENDAR, MATTER, ACTS, INTERIOR` | **YES** — the write matrix is total |
| loop steps | six | **YES** |
| `remit.acts` | five | **YES** as a set of *modes*; **the verb space it makes eligible is OPEN** |
| degree bands | **four** | **YES — and this is the row where a design collided with running code**, §8.2 |
| `Rung.kind` | eight | **YES** for the ladder; the ladder itself is world-authoring |
| ledger tag kinds | `Precedent, Grudge, Debt, Reputation, Leverage` | **YES**, ruled; a Compact is `Debt(recurs=True)`, **never a sixth family** |
| `MatterKind` | — | **open, correctly** — a type parameter, not an enumeration |
| stance referents | `Person, Proposition, Place` | **YES**, with `Place := Rung \| Site` defined |

### §8.1 One act per person or cohort per season, universally

**No office, rank or holding changes it, ever.** An act is the one discretionary commitment; subsistence,
craft and travel-in-progress happen *to* you at MATTER; a standing date firing is CALENDAR; `witness` is
WITNESS. None is an act.

**The fork was false because one word was doing two jobs.** *Personal attention* is scarce identically
at every rung — a Duke has the same hours as a fisher. *Institutional throughput* scales with the
**establishment**, not with the holder. The design already moved the dice off the holder and left the
act on him: **if the POOL for an act by remit comes from the establishment, the ACT does too.**

```
dispatch(holder, member, act):
    costs the HOLDER one act    -- his own, for the season
    costs the MEMBER one act    -- theirs, for the season
    the member still runs their own choose
    one dispatch names ONE person
```

**A holder may redirect exactly one of his people by name, per season, and may be refused.** Everyone
else on his roster does what their own view says.

**And an order is a telling; compliance is the hearer's own `choose`.** `issue` is one act; what happens
next is nine people's acts through the same compliance machinery built for subjects. **That is the
post-Secession Crown's actual problem, obtained without writing a loyalty stat.**

**The cohort exploit is priced rather than forbidden.** Individuating your cohort to farm acts gives you
eleven *persons* — each with a ledger, a stance toward you, needs of their own, and the ability to
refuse. **You did not buy eleven acts; you created eleven people who might hate you.** No rule forbids
it and none needs to, which matters because a special case is a forbidden shape.

**`seat_items` is deleted, deliberately, not dropped.** It and `capacity(date)` are one quantity seen
from two sides, which is why it was found double-counted — spent at `carry`, then used again as the
admission cap at `compose_agenda`. **One allowance: the act. One cap: items a sitting processes.**

### §8.2 The degree ladder is FOUR bands, and the design's five-band ladder is an amendment or nothing

> ⚠ **THE COLLISION NEITHER TRACE LOG RECORDED, FOUND BY TWO LANES INDEPENDENTLY** [LANE B C4/D3,
> LANE C B6/D2].
>
> The design corpus carries a five-band ladder (Disaster · Failure · Costed · Clean · Overwhelming) and
> describes it as shipped. **The executing single owner is `engine/autoload/dice_engine.py`, and it
> implements four margin-based bands** — Overwhelming at `margin >= 3`, Success at `margin >= 1`, Partial
> on `[0,1)`, Failure below zero — under a Jordan ruling of 2026-08-14 that **explicitly ruled out** the
> Ob-scaled Overwhelming, the separate `net >= 3` floor and the Ob-20 exception.
>
> **Under `CLAUDE.md` §0.05 the code is the formula.** A Disaster split is an **amendment to
> `degree_from_net`, made once, in that file, with a ledger row — never a parallel enum**, and
> `f(degree)` keys to the owner's enum. `DEGREE_LABEL` is the string map and `BandExtension` is the one
> declared seam: a subsystem's wrapper may **veto an Overwhelming and can do nothing else.**
>
> **This is also the exact hazard `CLAUDE.md` §5 records:** the frozen params capture still shows the
> pre-ruling bands, and a reader following it in good faith gets a retracted model.

**And the resolution kernel beneath it, verified this pass:** `TN` is **7, always** — the owner *raises*
on any other value, on a Jordan ruling. **A varying difficulty is an Ob, not a TN.** Face 1 scores −1;
`mu = 0.40`, `sigma = 0.800` per die. The continuous engine accepts fractional pools (the rounding
defect two logs report as live was fixed on 2026-08-21; both logs are stale on it).

**`derive_ob` does not exist and is owed.** The 2026-08-14 ruling — *the obstacle is their corresponding
score/2 plus whatever specific modifiers exist for them in that instance* — is quoted inside the owner
with its own **"IMPLEMENTED NOWHERE"** warning. Two independent design lines converge on the same
formula. **Build `derive_ob(target_score, modifiers) = max(OB_MIN, target_score/2 + modifiers)` beside
`roll_pool`, as the owner for NEW obstacle sites only** — the three divergent existing sites stay frozen,
because Jordan suspended their reconciliation and one of them is stated as canon.

**An uncontested attempt routes to a GATE, never to an `Ob = 0` roll.** `OB_MIN` is pinned at 1 and
stays pinned.

---

## §9 · WHAT IS EXCLUDED, AND WHAT COVERS IT

Every exclusion names what covers it, per `CLAUDE.md` §0's bottom-up rule.

| excluded | covered by | ground |
|---|---|---|
| `Entity` with a closed `kind` enum | four typed carriers | a closed kind enum on one struct froze what must grow — its own archival lesson |
| `Tag` (5, then 7 kinds) | `Claim` + `stance` + `Tenure` + `until?`-as-history | a tag family is a claim vocabulary wearing a struct |
| `Gauge` (bounded, decaying, no setter) | `Query` for every aggregate; primary state only on `Site.condition` and `stores` | the refusal of scheduled social recovery. The decay law survives narrowly, in claim confidence and recency |
| a `Faction` carrier | Proposition + `commit` Tenures | §3.1 |
| a second resolver | one `resolve` for all fidelities | **fidelity controls who supplies the act, never how the outcome is computed** |
| post budget / `seat_items` | one act + `capacity(date)` | §8.1 |
| `annex`/`secede` verbs | `confer` on `hold` | §4.6 |
| a fifth `Claim` source | `research -> told_by(record, ...)` | §5.3 |

### §9.1 The six FALSE N-LINES — objects whose claimed loss survives the cut

**The highest-value finding available to a NERS pass is an object whose claimed lost possibility
actually survives its cut, because something else already provides it.** Six were found. [LANE B B1–B6]

| # | cut object | its claimed N-line | why the possibility survives the cut |
|---|---|---|---|
| 1 | an `information` gauge | *inquiry needs a target* | knowledge stored on the thing known — **two owners, no knower.** The claim ledger plus the per-observer estimated profile already provide it, and only they can be planted or refuted |
| 2 | `credence.<proposition>` deposits | *holding-something-true needs a carrier* | the ghost: the target was cut by its own suite, found by three independent routes. `Claim.confidence` is the carrier |
| 3 | a `rising` auto-declared project kind | *the only route by which control changes with no post-holder* | **survives its cut** — `Press(f,n) > Hold(n,...)` with suppression scars provides it, with real producers, **and the alternative required a registry table plus an acyclicity check that does not exist** |
| 4 | `act.charter` generating a faction entity | *a schism needs a founding act* | **survives** — a faction is a proposition plus commitments, so founding is `commit` migration plus recognition-fission; a dispensation moves no edges |
| 5 | an `allegiance` edge kind with a stored −5..+5 gauge | *person-to-faction feeling needs a home* | commitment **degree** plus a **stance row** already carry it; a second stored carrier is pure E-surplus |
| 6 | `forecast_mass` in the depth score | *depth needs a forecast term* | **it has no producer anywhere in the corpus.** An object with no producer cannot have an N-line |

**Every one of these was proposed by a competent pass with a plausible argument.** The pattern is
uniform: a mechanism was named, a store was proposed for it, and **the store's job was already being
done by an object the design had already ruled in.**

---

## §10 · WHAT IS CARRIED AS OPEN

Stated so no later document can cite this one as though these were closed.

1. **The `wear` : restoration ratio.** *"If the world is not tended to by anyone, it will die"* costs
   exactly one constant, `wear`, per site kind — and **its ratio to a restoration act's effect sets the
   entire difficulty curve.** Too high and the world dies whatever anyone does; too low and tending is
   decoration. **This is a measurement, not a ruling, and nothing has been run.**
2. **`leaders`' comparator.** *commitment degree × backing raisable* is the proposal on file. Adopt and
   record rather than escalate; it is answered by the architecture.
3. **Where the channel store lives** — a newly created person's *plausible past*. Ruled against in three
   placements. Character generation works without it; the plausible-past property does not.
4. **The cohort's construal spread** — where it lives, what produces it, what an individuating member
   draws from. §2.1.1 states the *rule*; the distribution's representation is unspecified.
5. **`World`'s record.** Every refusal in this shape is written against it. **It is the first thing the
   typed port declares**, and `08_GODOT_4_6.md` §2 declares it first for exactly that reason.
6. **The agentive/non-agentive split on actorless rows.** An off-board polity's pressure is an Event
   source. **No criterion currently stops any actor being reclassified as weather**, and until one
   exists, an agentive actorless row is blocked. This is a real gate, not a caveat.
7. **The testimony half of the salience floor.** A firsthand claim gets a floor; testimony stays clamped.
   A sixty-year-old revelation out of the archives **arrives as testimony**, so this bears on the entire
   epistemic column at the top of the ladder.
8. ⚠ **`destroy` IS NOT CLEARED against the refusal rows, and this shape inherits the hole rather than
   closing it.** The unbounded discrete-destruction limb — one act removing an object others depended
   on, with no fractional-effect bound — was admitted open for arson, and extending `destroy` to a Rung,
   an Office, a Person or a Site **widens it by four object classes.** `create` is clear; `destroy` is
   not. **Do not cite this suite as having closed it.**
9. **Age-band boundaries; channel latency values; `season_factor`'s distribution.** Three numbers with no
   home; the third may already be answered by the world-events rate bounds.
