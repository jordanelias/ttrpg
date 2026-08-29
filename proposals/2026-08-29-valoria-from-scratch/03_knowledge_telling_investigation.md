# 03 — Knowledge, Telling, and Field Investigation

## Status: PROPOSED (2026-08-29) — a from-scratch design. Nothing here ratifies on merge.
## Lane: FI · Composes on: `01_substrate.md` (binding). Throughlines: T3, T4, T9 (with T2, T7 by consequence).
## Standing on a null: no surveyed game ships an NPC acting on knowingly false political information (N-9), and no game has an expression channel for interior state (N-2). Where this document invents rather than adapts, it says so.

The substrate fixed three signatures and asserted that a claim is
`(subject, predicate, value, when, source, confidence)`. This document builds the entire knowledge
layer on those and adds no fourth signature. Investigation, in particular, is **not a subsystem**: it
is a handful of ordinary acts plus one query over your own ledger, and if it needed a score of its own
that would be evidence the substrate was wrong.

Every object is stated as **producer → carrier → consumer** with an **N-line**. Objects that could be
merged have been; §11 lists what was cut.

---

## 1. The claim

```
Claim = (subject, predicate, value, when, source, confidence, visibility)
```

**Subject** is any referent the world already names — a person, a cohort, a containment node, a
faction, an office, a holding, a proposition, a place, an event, or **another claim**. That last is
not decoration: it is what lets `SAID(Aldwin, C, season 12)` exist, and §3 shows that row is the
load-bearing object of the whole document.

**`when` is a mandatory closed interval `[t₀, t₁]`, and it is universal, never existential** — a claim
asserts its value held *throughout*. The derivation: if intervals were existential, denial would
require a universal over the complement, and the engine would carry two claim logics with two
collision rules. One logic. A speaker who means "at some point" deposits the narrowest interval he can
support; standing facts carry `t₁ = ∞`.

So *"Torben was at the mill in the twelfth season"* is `LOCATED(Torben, mill)@[12,12]` and *"Torben was
at the mill"* — spoken now, meaning habitually — is `LOCATED(Torben, mill)@[10,∞)`: **the same
predicate over overlapping intervals**, so assert and deny collide by computation rather than by a
coincidence of naming.

- **Collision rule.** Claims C and D collide iff same subject, same predicate form, same arguments,
  `when` intervals intersect, and values are incompatible. Collision is a computed relation, run at
  deposit time, in one ledger at a time.
- Closed loop: produced by `witness` / `tell` / `reconstruct`; carried in one person's ledger;
  consumed by view assembly (§4) at every decision.
- **Cut the mandatory interval and you lose:** detected disagreement. A denial becomes a second row
  rather than an argument, and nobody in the world can be *contradicted*.

### 1.1 The predicate vocabulary is CLOSED. The referent space is OPEN.

Getting this wrong turns the game into a scripting language, so here is the derivation.

Claims must support exactly three operations: **collision** (does A contradict B), **entailment**
(does A imply B at coarser grain), and **relevance** (does A bear on decision D). All three are
functions of the predicate's *form*, not its arguments. Open forms mean each operation is authored per
form — a scripting language with a rules engine attached, where every new mechanic ships a new
inference rule. Closed forms mean each is one table of size |forms|, written once.

The objection is that a closed set cannot express the setting. It can, because **expressiveness lives
in the arguments**, and the argument space is the world's own object namespace, which is open because
the world generates persons, places, factions and propositions continuously. The forms are finite
because *decisions read a finite number of kinds of thing* — enumerated by asking what any `choose`
reads:

| Form | Shape | What it lets a decision do |
|---|---|---|
| `LOCATED` | (subject, place) | place someone, alibi someone |
| `DID` | (actor, act_kind, object) | attribute an act; `act_kind` is the game's existing act list |
| `HOLDS` | (person, office \| holding \| mark) | know who has what, who has a warrant |
| `MARKED` | (person, mark) | caste, heritage, guild grade, Church standing, visible sensitivity |
| `CONDITION` | (subject, condition) | dead, injured, ill, Coherence band, Knot-bound |
| `ALIGNED` | (person, faction, degree_band) | who has thrown in with whom |
| `TIED` | (person, person, tie_kind) | kin, patron, Knot |
| `QUANTITY` | (container, stake, band) | the granary, the levy, the tithe |
| `IN_FORCE` | (container, proposition) | dispensations, prohibitions, treaty clauses |
| `INTENDS` | (person, proposition) | motive, and `INTENDS(p, deceive)` — see §3 |
| `SAID` | (speaker, claim, when, place) | the provenance graph |
| `CAUSED` | (event\|act, event\|act\|condition) | the only constructed form; §6's product |

Twelve forms, and they close one loop the spine leaves open. The substrate's *estimated profile* of a
faction — the only profile any decision function may read — is computed by an observer rolling up
memberships **in their own ledger**. Those memberships are `ALIGNED` claims, deposited by `witness`,
`tell` and `reconstruct` like everything else. So a covert commitment is absent from an estimate until
somebody's claim names it, underestimation is the default rather than a special case, and the whole of
§§2–6 below is also the machinery by which factions are misjudged.

**Value** is typed by form (a polarity, a band, or a referent), so negation is a value,
not a form — which is why assert and deny land on the same row. **Entailment** is one table: `LOCATED`
at a district entails `LOCATED` at its settlement; `ALIGNED` at member entails `ALIGNED` at
sympathiser; a narrower interval entails nothing about a wider one but is *contradicted* by a wider
denial. Twelve forms, one entailment table, no grammar.

- **Cut the closure and you lose:** nothing at first, and then everything — because within three
  mechanics someone writes a predicate whose contradiction rule is a special case, and after that no
  two claims in the game can be automatically found to disagree.

---

## 2. Witness — how one event becomes genuinely different claims

`witness(person, event) -> claim*`

The temptation is to give the event one true predicate and hand each witness a noised copy. That is
consensus broadcast with jitter: every witness is arranged around the truth and the town's mean is
correct. Divergence must come from **selection among readings the event actually offers**, never from
error on a single reading.

So `resolve` emits, alongside the event, a set of **facets** — atomic claims in the twelve forms that
the event makes available, each with a `persists` window and a retention curve. `persists = [t,t]` is a
moment; `[t, t+2 seasons]` is what §6's `examine` reads off the scene later. **Facet and residue are
one object at two persistences.**

Witnessing then runs in two stages, different in kind.

**Stage 1 — registration (what you were positioned to perceive).** Per facet:

```
P(register f) = vantage_factor(person, event) × capability_factor(person, f)
vantage_factor:   present_at 1.0 | present_in_place 0.7 | arrived_after 0.4 | heard_of_the_noise 0.2
capability_factor = 0.60 + 0.05 × Acuity            (Acuity 1..7 → 0.65..0.95)
                    for rendering-side facets, see §9 — a hard floor, not a factor
deposit_confidence(f) = 0.9 × vantage_factor × capability_factor
```

An unregistered facet is **absent from the ledger**, not stored blurred. A witness who arrived on the
noise does not hold a fuzzy version of who struck first; he holds nothing, and §4 tells us exactly what
he does then.

**Stage 2 — construal (what you made of it).** Each `act_kind` carries a small closed set of
**construals**: readings of the act, each a `CAUSED` or `HOLDS` claim plus the Conviction it appeals
to. Construals are indexed **by act kind, never by entity** — a table naming a person would be a
script; one naming `strike_by_officer` is the same sort of object as the act list itself.

For `strike_by_officer`, four:

| id | claim produced | appeals to | requires facet |
|---|---|---|---|
| c1 `order_restored` | CAUSED(E, IN_FORCE(node, order)) | Order | — |
| c2 `unprovoked_harm` | CAUSED(E, CONDITION(target, injured)) | Equity | injury facet |
| c3 `lawful_correction` | HOLDS(actor, warrant) ∧ CAUSED(provocation, E) | Precedent | the provocation facet |
| c4 `caste_violence` | CAUSED(MARKED(target, m), E) | Identity | the mark facet |

Selection:

```
score(c) = ConvW(witness, c.conviction)                                   # 0..3
         + 0.5 × Σ_{r ∈ {actor, target}} favour(c, r) × stance(witness → r)   # stance −5..+5
         + 1.0 × marks_kinship(witness, target) × adverse(c)

construals requiring an UNREGISTERED facet are excluded outright, not down-weighted.
witness deposits argmax score(c), with confidence = softmax_share(c) × mean deposit_confidence
```

Three properties fall out that the assertion alone would not give you:

1. **Two honest witnesses can agree on every fact and disagree on every conclusion.** Registered facets
   deposit identically; only the construal differs. §12 shows it happening.
2. **Construals deposit with source `inferred(...)`, never `firsthand`** — so a hundred people
   construing alike corroborate *nothing* (§5). Public opinion is structurally not evidence.
3. **Vantage does real work through the exclusion rule.** A witness who missed the provocation cannot
   reach `lawful_correction` at all — not at low weight, not ever, until someone tells him.

**Cohorts.** `witness` runs once per cohort; if its Conviction spread gives two construals comparable
share, the cohort **individuates along that line**, and the market crowd fissions into those who saw
order restored and those who saw an arm broken — the substrate's existing operation, at any rung.

- Closed loop: produced by `resolve` emitting facets; carried through `witness` into one ledger per
  person; consumed by view assembly.
- **Cut the construal table and you lose:** perspective. Divergence collapses to noise, and the town's
  average opinion becomes the truth, which is the exact defect this document exists to prevent.

---

## 3. Telling — the lie as something a person does in a place at a time

`tell(speaker, hearer, content, as_asserted) -> event`

Telling is an act. It occupies the speaker's hour, happens at a place, and emits facets, so **third
parties witness it by the ordinary §2 path** with no new machinery.

`content` is `(subject, predicate, value, when)`; `as_asserted` is the `(value, confidence,
asserted_provenance)` the speaker *performs*; `held` is the speaker's own claim on that content, if
any. The **deception delta** δ = distance(as_asserted, held):

| δ | name | held |
|---|---|---|
| 0 | sincere | matches |
| value flipped | **lie** | opposite |
| confidence inflated | **overclaim** | same value, lower confidence |
| provenance inflated | **false witness** | "I saw it" when source is `told_by` |
| content absent from ledger | **invention** | none |

One act, one delta, four behaviours. No liar flag, no deception stat.

**Resolution.**

```
Speaker pool = Charisma + practice(Bearing|Persuasion)
             + 1 per corroborating claim the HEARER already holds
             − 2 × δ_visible                      # the bigger the lie, the harder the tell
             + Momentum spend

Hearer pool  = (8 − credulity) + Acuity
             − stance(hearer → speaker)           # I believe my friends
             + obstinacy × |stance(hearer → nearest referent of content)|
             + 1 per contradicting claim held
```

Outcome by margin (the dice resolver is document 02's; only the ladder is specified here):

| margin | hearer deposits |
|---|---|
| speaker +3 or better | content at `as_asserted.confidence`, source `told_by(speaker, handle)`; contradicting claims lose 0.2 confidence |
| speaker +1..+2 | content at 0.6 × asserted |
| within 1 | content at 0.15 — believed by nobody, retrievable by nobody |
| hearer +1..+2 | content at 0.15; stance(→speaker) −1 |
| hearer +3 or better | content at 0.15; **`INTENDS(speaker, deceive)` at 0.5** |

**On every outcome without exception, the hearer also deposits `SAID(speaker, content, when, place)`
at 0.9 × their own vantage.** Disbelieving a man does not unhear him. This unconditional row is the
document's single most important object: the traceable source row the substrate promised, what makes
lying catchable, and the entire raw material of investigation (§6).

### 3.1 How a lie is caught

Three channels, all of them the collision rule (§1) firing in somebody's ledger. There is no
lie-detection mechanic.

1. **At the telling, by a third party.** Anyone with vantage deposits SAID; one who *already holds a
   firsthand claim colliding with the content* deposits `INTENDS(speaker, deceive)` immediately, no
   roll, because the contradiction is computed. This is why you do not lie in a full market.
2. **Later, by collision on arrival.** When claim C enters a ledger and collides with D:
   ```
   reconcile(C, D):
     losing = the one with lower live confidence (§4)
     losing.confidence ×= 0.6
     if roots(C) ≠ roots(D):  deposit CONTRADICTED(source(C), source(D))     # someone lied; unknown who
     if one is firsthand and it wins over a told_by(S):
         deposit INTENDS(S, deceive) at conf ∝ margin
         ...UNLESS stance(holder → S) ≥ +3, in which case deposit CONDITION(S, mistaken) instead
   ```
   The last line is not a special case — it is obstinacy applied to attributing motive. **Motivated
   reasoning about who lied to you falls out of the same term as motivated reasoning about what
   happened.**
3. **By reconstruction.** §6's `reconstruct` over accumulated SAID rows finds that three
   independent-sounding stories share one origin, or that a man's asserted provenance was elsewhere.

### 3.2 What it costs to be caught

Nothing is deducted. `INTENDS(S, deceive)` is a claim about S like any other claim about anyone, and
its consequences are exactly the consequences of being in ledgers:

- it enters view assembly whenever anyone weighs a telling from S, cutting the `stance(hearer → speaker)`
  term;
- it enters the judging set's view when S seeks admission, an office, a marriage, or carries a petition;
- it can be **told**, which is how it spreads, which means it spreads at the speed of the channel and
  arrives distorted like everything else.

So the cost of being caught is *how many persons hold the claim, weighted by their stance* — which
makes lying to a stranger with no Knots nearly free and lying at the tithe reckoning in the
Kettlemakers' hall ruinous, with no reputation scalar anywhere. The substrate refused a faction-wide
reputation number; this is why it did not need one.

**R-check on the lying fork.** A successful lie's gain does not decay: the substrate refused a belief
cap, so it is a full-value outcome change every time. Its cost is probabilistic and rises with the
number of witnesses and the checkability of the content. The fork is *small quiet lies about
uncheckable things* (cheap, low reach) against *large public lies about checkable things* (expensive,
high reach), and neither dominates, because gain and cost scale with the same quantity. Had the gain
been capped, honesty would dominate and this whole document would be flavour.

- Closed loop: produced by a person choosing to speak; carried as an event witnessed by hearer and
  bystanders; consumed as ledger rows in each of them.
- **Cut the unconditional SAID row and you lose:** investigation entirely. Also propaganda, testimony,
  and any possibility of catching anyone at anything.

---

## 4. View assembly — the budget, and motivated reasoning for one multiplication

`view(person, question) -> at most K claims`

```
K = 7 + Focus                                    # Focus 1..7 → 8..14
  + 2 per Knot consulted on this question         # consulting is the act `counsel`; costs Knot strain
  − Coherence penalty: Dissonant 1, Fragmented 2, Fractured 3, Severed 5
```

Tying K to Coherence costs nothing and buys a great deal: a Fractured person cannot hold enough of
their situation in mind at once, so Coherence-drift propagating through Knots (P-12) becomes
*epistemically* contagious rather than merely socially penalising.

```
salience(c) = recency(c) × confidence_live(c) × relevance(c, q) × stanceweight(c, person)

recency(c)          = 2^(−age_seasons / halflife)
                      halflife = 4; 12 if the subject is a Knot partner, a hearth member,
                      or the referent of a Conviction-primary
confidence_live(c)  = deposit_confidence × corroboration_multiplier(c)        # §5
relevance(c, q)     = 1.0  if (subject, predicate) is in q's read-set
                      0.3  if c's subject is within two graph edges of a read-set referent
                      0    otherwise
stanceweight(c)     = clamp( 1 + λ · agreement(c), 0.05, 2.0 )
                      agreement ∈ [−1,+1]: does believing c support or undermine the person's
                                            most-weighted stance that c touches?
                      λ = obstinacy / 5
```

**The stance-weight term is the whole of T3 and it is one multiplication.** For a Templar with
obstinacy 5 (λ = 1) holding the exonerating claim about a Southern Einhir smith: agreement = −1,
stanceweight = 0.05. The claim is in his ledger, at high confidence, and its salience is one twentieth
of what an agreeing claim of the same strength would have. It does not enter the top-K. **He is not
hiding it and he is not lying; he is not thinking of it.**

The floor of 0.05 rather than 0 is deliberate and is an R decision, not a softening: it means a
*devastating* firsthand contradiction — recent, high confidence, perfectly relevant — can still cross,
so a person can be argued out of a stance, but it takes roughly twenty times the evidence. That is
motivated reasoning, not a wall. And note precisely what is being attenuated: **retrieval, not value.**
Once a claim is retrieved, its value enters the decision unattenuated. This is not the capped-bias trap
the substrate refused (F-7); a claim that surfaces decides the same way a true one would.

**Ties** break deterministically: firsthand > told_by > inferred, then more recent, then lower claim
id. No randomness, because randomness here would make a person's beliefs shimmer between two decisions
in the same hour.

### 4.1 The empty view — ignorance, not uncertainty

If no claim has relevance > 0 for the question, the person does **not** act uncertainly. In order:

1. **Marks-based expectation.** A default value read off the subject's visible marks through the
   asker's own stance table, deposited at confidence 0.35 with source `inferred(MARKED(subject, m))`.
   Asked whether the Southern Einhir journeyman took the tin, a person with a negative stance on that
   mark answers *yes*. **This is prejudice as the literal default of an empty ledger** — which is the
   setting's own claim that caste is reproduced by institutions and by people who have never met you,
   made mechanical rather than asserted. Crucially it is deposited **with its root**, so it is a claim
   with a findable origin and can be refuted by investigation like any other.
2. **Rumour draw.** If the place holds an ambient claim on this subject/predicate, draw it at 0.2,
   source `told_by(unknown, σ)` — see §5.
3. **Container norm.** The aggregate stance of the person's community on the proposition, computed on
   demand (the substrate's §4 already supplies it), at 0.25.
4. If all three are silent, **the option leaves the person's act list.** They act on a question their
   view can answer.

That fourth rule is the sharp edge and it is worth stating as a law of the engine:

> **Ignorance narrows the option set. Uncertainty widens the outcome distribution. The engine must
> never substitute one for the other.**

- Closed loop: produced by the ledger at decision time; carried nowhere (recomputed per question);
  consumed by `choose`.
- **Cut the stance-weight term and you lose:** every character becomes a fair-minded Bayesian with a
  memory limit, and no one in the game can be wilfully, sincerely, ruinously wrong.

---

## 5. Corroboration that fails closed

Every claim's source is `firsthand(event_id)`, `told_by(person, handle)`, or `inferred(claim_id…)`.
There is no null source, and there is no operation anywhere in the game that mints a root token except
**`witness`**. That sentence is the whole proof; the rest is bookkeeping.

**Root sets.**

```
roots( firsthand(e) )        = { e }
roots( told_by(p, h) )       = h.rootprint                      # opaque tokens, asserted by the speaker
roots( inferred(c₁…cₙ) )     = ⋃ roots(cᵢ)                      # union, never fresh
```

**The rootprint.** When p tells h, the telling carries p's *asserted* root-set as opaque tokens. The
hearer learns **that** two of their claims share an origin, never **what** the origin was. This is
epistemically exact: you can tell that two men are repeating the same story without knowing whose story
it was, and finding out whose is the investigative act `reconstruct` (§6). It also means asserting a
false provenance is part of δ (§3) and is caught the same way as any other lie.

**Unverified roots fail closed.** If the hearer wins the telling contest, the rootprint is stored
`unverified`, and every unverified token is replaced, for independence purposes, by `⊥_content` — **one
token per content**, shared by everything unverified about that content. Doubt therefore collapses
independence rather than preserving it.

**Synthetic roots.** A claim that first appears with no assertable origin — overheard in the market,
current in the quarter — is assigned

```
σ = σ( subject, predicate, value, when_bucket, place_cluster )
```

a **pure function of the content**, not a fresh id. Every independent retelling of the same rumour
therefore hashes to the same σ.

**Support and the multiplier.**

```
support(C)  = | distinct root tokens across ⋃ roots(c), c ∈ C on the same content |
corroboration_multiplier = min( 1 + 0.35 · log₂(support), 2.0 )
```

**Proof that correlated rumour cannot be laundered into corroboration.** Support counts *distinct
tokens*. Three routes exist to add a token and no others: (a) `firsthand`, which requires an actual
event and an actual witness with vantage — the only minting operation in the game; (b) `told_by`, which
copies tokens and cannot create them; (c) `inferred`, which unions premises and, if the union is empty,
**refuses the inference**. A rumour told three times supplies σ, σ, σ, so |{σ}| = 1 and the multiplier
is 1.0. A chain of ten inferences from one observation supplies one token. The F-14 failure — empty
ancestries being pairwise disjoint, so three retellings counted as three supports — is unreachable,
because there is no path to an empty ancestry: every constructor either mints, inherits, or is refused.

The ×2.0 cap exists so that a genuinely large crowd of independent witnesses cannot make a claim
unfalsifiable. Sixteen independent roots and sixteen hundred give the same multiplier.

- Closed loop: produced by `witness` minting and `tell` copying; carried in the source field; consumed
  by `confidence_live` in view assembly and by `reconstruct`.
- **Cut the synthetic root and you lose:** the distinction between a town that knows something and a
  town that has been saying something. Rumour becomes proof by repetition, and every conspiracy in the
  game becomes true.

---

## 6. Field investigation as first-class — and what the GM was doing

The canon investigation text is GM-mediated: *the GM sets the threshold*, *the GM may offer a
misleading clue*. There is no GM. Those are two distinct jobs and each gets a mechanical owner that is
strictly better than a person's whim.

**Setting the threshold → the world sets it, as facet retention.** Every event writes facets with a
persistence window and a decay. `examine` rolls against

```
retention(f) = base(facet_kind) × 2^(−age / halflife(facet_kind)) × (1 − concealment_spend)
```

A struggle leaves marks; a poisoning leaves few; a forged edict leaves the forgery's own physical
facets and nothing of the issuing it purports to record. Nobody adjudicates difficulty. The world
already emitted what it emitted, and time is eating it.

**Offering a misleading clue → a person does it, in a place, at a time, and can be caught.** The GM was
doing two things at once: injecting a false claim, and choosing whom to inject it into. Both already
exist as acts. Injection into a person is a **lie** (§3). Injection into a scene is

```
plant(actor, place | object, facet, when_asserted)
```

which writes a facet whose **root token is minted by the planting act**, not by the event it purports
to evidence. A sufficient `reconstruct` therefore finds that the root of the "evidence" is a person's
act at a later hour. The misleading clue now has a liar with a motive, and it required no new object —
`plant` is also how a **forged succession edict** is made, which is §7.

### 6.1 The acts

Every one is available to any person; the substrate's rule that action eligibility never consults
office binds here without exception.

| act | pool | produces | cost / risk |
|---|---|---|---|
| **examine**(place\|object\|body) | Acuity + practice, vs `retention` | `firsthand` facets still persisting | time; you are witnessed examining |
| **interview**(person, question) | Charisma\|Attunement vs their obstinacy and stance | their `SAID` row — i.e. a `told_by` claim, which may be a lie | **they learn what you are asking**: deposits `INTENDS(you, investigate X)` in their ledger, tellable onward |
| **research**(archive, question) | Focus + literacy practice | `told_by(record, …)` with **verified** rootprints and old `when` — archives are the only non-person root-bearers | access is an **admission** gate held by persons with stances |
| **surveil**(person\|place, duration) | Agility\|Focus, opposed by the target's concealment | `firsthand` LOCATED / DID / SAID over the whole interval at good vantage | duration; **exposure** (§7) accrues to *you* |
| **reconstruct**(claim-set) | Acuity + Will | `inferred` claims: CAUSED, CONTRADICTED, INTENDS(deceive), and **root identification** — resolving an opaque token or a σ to a named person | no world risk; the risk is that a *wrong* reconstruction deposits at real confidence and is acted on |
| **Thread-Read**(person\|place\|object) | Thread Pool (⌊TS/10⌋) + Attunement | `firsthand` **rendering-side** facets: prior configurations at a place, a person's Conviction-primary, the **orphaned configuration** left by memory-pulling (P-09), Knot residue | Coherence risk; Knot strain if remote; detectable by other sensitives; and it produces claims most people cannot be told (§9) |

**Investigation's currency is the SAID row, which is why it needs no score.** Because §3 deposits SAID
unconditionally, a diligent interviewer accumulates a graph of who said what to whom. The "score" is how
many rows you hold and whether their rootprints collapse. There is no clue counter, no case object, no
investigation skill, and no threshold anyone sets.

The one derived query is **`trace(person, claim)`** — the provenance tree that person can currently
reconstruct from the SAID rows, rootprints and collision records already in their ledger. It is a
*view*, not a store, and it is only as good as what they went and got.

### 6.2 Playable with no office

`research` is the only gated act, and its gate is an admission act at a community — the Church's
archives are a community with a gate, held by persons. A hamlet fisher routes around it three ways:
interview an archivist (a person with a stance and a price), use a **Knot** to a person who has access
(`counsel`, at strain), or steal. Every gate in this document is a person, so every gate has a price
and a grievance.

**R-check on the investigative fork.** `interview` is cheap, fast, and leaks — its gain decays sharply
as `INTENDS(you, investigate)` spreads and people close up, while its cost stays flat. `surveil` is
slow and quiet — its cost compounds through exposure, while its gain (firsthand root tokens) is
permanent and is the only thing that raises support in §5. `research` is gated but yields **verified**
rootprints, which nothing else does. `reconstruct` costs nothing in the world and risks your own
ledger. Four different shapes of gain against four different shapes of cost; none dominates, and the
right choice depends on whether you are racing a rival, hiding from one, or already have the rows.

- Closed loop: produced by a person spending acts; carried as ordinary claims in that person's ledger;
  consumed by `reconstruct` and then by every subsequent decision and telling.
- **Cut `reconstruct` and you lose:** the ability to ever find out *who* lied, as opposed to *that*
  someone did. Investigation stops being a discipline and becomes an accumulation of gossip.

---

## 7. Concealment and counter-investigation

**Visibility** is a field on every act and every claim: `open | discreet | concealed`. It is chosen at
performance and it costs — a concealed act rolls a reduced pool and takes longer. A concealed act emits
no facets to witnesses below a vantage-and-capability threshold. **One operation, two application
sites**: applied to an act it hides the deed; applied by an office-holder to the *channel their office
is the normal carrier for*, it is `withhold` — the regent who delays emitting the death-notice, the
praefect who does not read out the assize. The event happened; the channel did not carry it.

**Exposure** is the paired hidden counter, per (actor, operation):

```
exposure += extraction_weight            each tick you take value out of the concealment
exposure −= cover_value                  each `cover` act you spend instead of extracting
```

Discovery is **proportional to a rival's actual investigation spend, never automatic**:

```
for each investigator I who spent acts on subject S this tick:
    pressure(I,S) = Σ act_weight(a) × vantage(I, S)
    P(discover | I) = 1 − exp( − pressure(I,S) × exposure(S) / θ )        θ ≈ 40
```

Both terms are necessary and this is the point of the pairing. **Exposure 0 → P = 0 at any spend**: a
concealment you never extract from is never found, so patience is genuinely safe. **Spend 0 → P = 0 at
any exposure**: a conspiracy nobody is investigating is never found, so the world does not audit you
for free. This clears both of the precedent's failure poles at once — it is not a mechanism engineered
never to fire (a rival who spends will find you), and it does not bleed regardless of play (an idle
rival finds nothing).

The precedent's test — run maximum mitigation against maximum accrual and check the net is recoverable
— passes with a real price: `cover` reduces exposure by a flat amount per act, so a conspirator can
always drive exposure back down, **at the cost of the tempo the conspiracy existed to gain**. The fork
is extract-fast-and-be-found against extract-slow-and-be-late, and both are live.

**Withhold makes its own evidence.** While the death-notice is withheld, everyone in scope acts on
stale claims. When it finally lands, each of them runs `reconcile` against what they were fed in the
interim — producing a *mass of collisions with a common source*. `reconstruct` over that mass resolves
to the withholder with unusual ease. Delay buys a window and pays for it with a signature.

**The forged instrument.** `plant(actor, instrument, facet, when_asserted)` produces a document whose
root token was minted by the planting act but which asserts the root of a genuine issuing. **Until
discovered it is true for every purpose that reads claims** — offices bind, legitimacy computes,
sworn orders obey — because there is no true-state path in `choose(person, view)`. This is the cleanest
possible statement of "the world believes a false thing," and the substrate's signature rule is what
makes it free.

Discovery is `reconstruct` succeeding on the forged root and depositing `CAUSED(plant_act, instrument)`.
Then every holder of a claim sourced to that root re-runs §5 with the token marked ⊥, and their
corroboration collapses. **Legitimacy flips retroactively for exactly the people who learn, at the speed
the news travels** — not as a global flag. A Crown claim resting on a forged instrument therefore
unravels province by province, and a duchy that has not heard yet is still, for its own purposes,
obedient to a fiction. If that vacancy coincides with a contested Church succession, the two
unravellings interleave through the four Dicastery channels of §8, and nobody had to author a
consecration crisis.

- Closed loop: produced by a person choosing concealed visibility; carried as exposure on the actor and
  as absent facets in the world; consumed by rival investigation spend and by `reconstruct`.
- **Cut the exposure/spend pairing and you lose:** the whole game of counter-intelligence. Discovery
  becomes either a timer (so concealment is pointless) or impossible (so concealment is dominant).

---

## 8. Correspondence filtering — the servant who outranks the ministers

Every container holding an office carries a **channel**: an ordered list of persons through whom a
petition, a report, or a telling must pass to reach the office-holder. A channel is not a rank list. It
is whoever actually handles the traffic.

Each channel-holder, on receiving an item, chooses a **disposition**:

- **approve** — pass it on, with the holder's own endorsement attached as a claim: `SAID(holder, "this
  merits attention")`. Endorsement is why the intercessor's standing modifies the outcome.
- **suppress** — drop it. The petitioner is **not told**. Nothing reaches the principal. A record of the
  suppression is deposited **in the holder's own ledger**, which makes it findable by §6 and is the only
  reason suppression is risky at all.
- **surface** — pass it on *framed*: the holder attaches their own construal, which the principal reads
  at the top of their view because a household intimate's claims carry high recency and high stance
  weight. Surfacing is more powerful than suppressing and leaves less trace.

**Influence is volume filtered, and it is derived, not stored:**

```
filter_share(p) = items p dispositioned this season / items reaching the office this season
```

No power stat. A Southern Einhir under-steward with filter_share 0.6 in a ducal household determines
what the Duke *knows*, and therefore what the Duke *chooses*, because `choose(person, view)` has no
world argument. **He structurally outranks ministers while holding no standing whatever.** This is the
largest single dividend the substrate's signature rule pays, and it costs one field and one derived
ratio.

**Bindings, all by composition, none by exception:**

- **The Church's four Dicasteries are four parallel channels to four Cardinals, and the channel an item
  enters is determined by its proposition's subject — which makes routing itself contestable.** A
  denunciation of a Southern Einhir Canon can be routed to *Defense of the Faith* (a heresy matter,
  ruinous), to *Doctrinal Adjudication* (a question of interpretation, survivable), or to *Temporal
  Affairs* (a jurisdiction question, deferrable). Whoever holds the routing seat holds the outcome, and
  no rule anywhere names the Dicasteries — they are four channels with different Cardinals' stances at
  the end. A Confessor is the channel to a monarch's conscience: sincerity is not a mitigation, because
  his construal selection (§2) runs on a Conviction-primary of Faith, and the reading he attaches is the
  one under which suppression *is* pastoral care. An institution causing harm nobody intends, as one
  construal table and one channel.
- **A ducal household** is chamberlain → steward → the Duke: three seats, three sets of stances. A
  duchy that retains a Parliament has a **second, competing** channel with different filter-holders, so
  a petition can be tabled instead of carried. That structural difference — two channels versus one —
  is the entire reason two duchies' politics feel different, and nothing was scripted to make it so.
- **The Crown** is reached by the household channel, by a military-religious order's Grandmaster
  reporting directly on the order's own matters, and by the Confessor. Three channels, three
  filter-holders, and a dynastic claim's whole fight is over which channel a given claim about an heir
  travels down.

**Counter-play (R).** A petitioner routes around a channel three ways, with three cost shapes: find a
person holding a **Knot** to the principal, since a Knot is a channel with bandwidth and bypasses
correspondence entirely (cost: strain, and the partner's own stance); make the item **public**, so the
principal witnesses it directly (cost: publicity binds the principal to respond and courts a hostile
construal); or suborn the channel-holder (cost: a person who now holds something on you). None
dominates. And suppression is not free — the suppressed petition writes grievance into its backers *if
and when they learn*, and whether they learn is a telling, so a channel-holder's real exposure is one
backer with an `interview` act.

- Closed loop: produced by petitions and tellings arriving at a container; carried by named persons in
  the channel, each of whom disposes; consumed by the principal's view — or by nobody, which writes
  grievance back into the backers.
- **Cut the channel and you lose:** the possibility that a person with no rank determines a realm's
  policy, and the possibility that a principal is not lied to but simply never told.

---

## 9. The setting's own epistemics, made mechanical

**P-03 — asymmetry between the sensitive and the non-sensitive is the core mechanic.** Events emit
**rendering-side facets** alongside ordinary ones. Registration of a rendering-side facet is a **hard
floor, not a factor**:

```
P(register rendering facet f) = 0        if TS < floor(f)
                              = g(TS − floor(f)) × admitting_share(witness)   otherwise

admitting_share(w) = ConvW over the witness's Convictions whose construal sets contain a
                     rendering-side reading, ÷ total ConvW
```

A non-sensitive standing at perfect vantage registers strictly fewer facets than a sensitive across the
square. Not a penalty on a roll — an absence in the ledger, which §4 then treats as ignorance.

**The `admitting_share` term is where an institution suppresses without suppressing.** An essentialist
theology's catechesis raises concentration in Convictions whose construal sets are rendering-blind. As
concentration rises, share falls, and registration falls with it. Nobody prohibited anything; the
Church is the unwitting suppressor of sensitivity because catechesis is a *witness-time* term. This is
the same construal weighting used for the broken arm in §2, pointed at a different facet class — a
composition, not a special case. Delete the theology and the mechanism is still there, waiting for
whatever else concentrates Conviction.

**P-08 — the barrier is INACCESSIBILITY, not suppression.** The trap the brief names is real: a barrier
implemented as an empty channel is institutional, because an institution could open it. So the barrier
must live in `witness`, not in `tell`.

Mechanism: a rendering-side claim's subject is a **configuration**, a referent for which a
non-sensitive's ledger has no address. When such a claim is told to a non-sensitive, `tell` cannot
deposit the content — there is no representable subject. What deposits is a **degraded claim**: subject
replaced by the nearest referent the hearer does have (the person, the place), predicate replaced by the
nearest of the twelve forms, value collapsed to a band. `SAW(configuration κ at the mill, torn)` arrives
as `CONDITION(the mill, wrong)` at 0.2.

**That is "religious poetry", and it is produced with no suppression anywhere in the pipeline.** The
speaker did not lie: δ = 0. The hearer did not disbelieve: the roll was won. The information did not
survive the type conversion.

And this is the exact test P-08 demands: **study cannot cross it**, because study operates on claims,
and the claim that arrives is already degraded. Raise the hearer's Focus, literacy, archive access and
patronage to the ceiling and nothing changes, because degradation happened at deposit, before any of
those terms are read. The only thing that changes it is TS crossing the floor — the hearer becoming able
to **witness**, not to **learn**.

**The falsifier for the institutional reading:** delete every institution in the peninsula and the
degradation is identical. If removing institutions changed the barrier, it was suppression. It does not,
so it is not.

**P-13 — Southernmost knowledge is untransmittable to non-sensitives** is the same mechanism with the
floor set highest, and it carries the corollary the setting needs: **between sensitives it transmits
perfectly.** Communities with higher baseline sensitivity therefore hold knowledge the rest of the
peninsula cannot audit — not because they conceal it, but because every attempt to share it arrives as
poetry. That is a caste's epistemic position derived from one floor, and it is why the stigma is
self-reinforcing: the untransmittable thing looks exactly like a lie.

**P-09 — memory-pulling.** Pulling a claim deletes the row and writes an **orphaned configuration**: a
rendering-side facet with high retention on both the person and the place. It is findable two ways.
A sensitive finds it by Thread-Read. **And a non-sensitive finds it by bookkeeping**, because the SAID
rows that pointed at the deleted claim now point at nothing, and `reconstruct` reports a dangling
reference in the provenance graph. Two independent detection channels, one supernatural and one purely
clerical, and the second is free — it falls straight out of "no null source."

- **Cut the registration floor and you lose:** the setting's central asymmetry, and with it any
  structural reason a caste with more perception has less standing.

---

## 10. Disclosure to the player

The rule, which costs zero mechanics: **publish every input, publish a band, never publish the trigger
point.**

**Your own view.** The player sees their ledger in full: every claim, its source row, its live
confidence as a *number* (it is theirs; there is no reason to hide it), every collision flagged, and the
top-K that will actually be consulted for the pending decision, shown as the top-K with the four
salience factors listed beside each.

And, greyed out beneath it: **the claims you hold that were crowded out by stance weight**, labelled
*you know this and you are not thinking about it.*

That one panel is this document's answer to N-2. The field's failures all narrowed scope — a facet band
with templated text, a closed trait vocabulary, hand-written variants — because they tried to *describe*
interior state. This does not describe anything. The interior state already **is** a ranked list of
claims with named multipliers over a closed set of twelve predicate forms and thirteen Convictions, so
rendering it is a table, and it stays legible at any content volume because the vocabulary is finite
while the referents are not. Whether that counts as expression rather than tracking is a fair question;
what is certain is that it does not narrow as the world grows, which every prior attempt did.

**Other people.** Inputs and a band, never the value and never the threshold.

- The inputs shown about another person are **the claims the player holds about them** — "you have seen
  him take the guild's side twice; he holds Order at primary; his obstinacy reads high" — each of which
  is a row in the player's own ledger and is therefore **falsifiable, and possibly wrong**. The
  player's read of an NPC is itself a view, subject to §4 including its stance weighting. The interface
  is not a truth window; it is a rendering of the player's claims, and it lies to the player exactly
  when and as their own ledger does.
- Bands, always words: stance as *hostile / cold / neutral / warm / bound*; exposure as *unnoticed /
  murmured / watched / hunted*; filter share as *he sees little / he sees much / nothing reaches the
  Duke but through him*; corroboration as *one story / two stories / many mouths, one root*.
- Never shown: any stance integer, θ, K's exact value, the discovery probability, or the point at which
  a backer tips into commitment.
- And the interface obeys §4.1: if the player holds no claim about a person's Convictions, they see
  **"you do not know what he believes"** — not a greyed meter, not a question mark on a scale.
  Ignorance, not uncertainty, in the interface too.

- **Cut the band discipline and you lose:** the no-GM answer. Either the player is handed truth the
  engine's own agents cannot see, or they are handed nothing and cannot plan.

---

## 11. What is refused

- **An information or "known %" gauge on the thing known.** No knower, so it cannot be interrogated,
  planted, or refuted, and one person's inquiry raises everybody's knowledge.
- **A clue object, a case file, an investigation score, a detective aptitude.** §6 is acts plus one
  derived query. Anything more is a second resolver for a thing the ledger already resolves.
- **A liar flag, deception stat, or reputation scalar.** §3.2 shows the emergent cost is the correct
  one and is already computed.
- **Any function returning a claim's true value to any agent.** There is no truth channel, for NPCs or
  for the player.
- **A global rumour-spread percentage.** Rumour is claims moving through tellings between named people,
  or it is a weather system.
- **Free provenance queries.** `trace` reads only what the person went and got. A free query is
  omniscience with an extra step.
- **A confidence floor high enough to make a claim unfalsifiable.** Hence §5's ×2.0 cap.
- **Separate objects for facet and residue** (merged: one facet with a persistence window),
  **for forgery and planting** (merged: `plant`), and **for withholding and concealment** (merged: one
  visibility field, applied to an act or to a channel).
- **An open predicate grammar.** §1.1.
- **Per-NPC authored knowledge tables.** What a person knows is what `witness` and `tell` put there.

---

## 12. Worked trace — two people who agree on the facts and act against each other

*Goldenfurt, in Grauwald: a Southern Einhir hamlet outside the wall and the Kettlemakers' Row inside
it, at the tithe reckoning of the twelfth season.*

**E1.** A serjeant of the Löwenritter, Brother Halvard, breaks the arm of **Gerik Strand**, a Southern
Einhir journeyman smith, in the Marktplatz. `resolve` emits facets:

| | facet | persists |
|---|---|---|
| F1 | DID(Halvard, strike, Gerik) | [12,12] |
| F2 | CONDITION(Gerik, arm_broken) | [12,14] |
| F3 | DID(Gerik, refuse_measure, tithe_officer) | [12,12] — *it happened; he did refuse* |
| F4 | MARKED(Gerik, southern_einhir) | standing |
| F5 | rendering-side: Knot-strain flare on Halvard | [12,13], floor TS 25 |

**Maret Uln**, Southern Einhir, Free Master candidate with her Masterpiece Examination pending; Acuity
5, TS 38, Focus 5, obstinacy 3; Convictions Equity 3, Identity 2, Precedent 1. She is at the far end of
the square: `present_in_place` (0.70). She registers F1, F2, F4 at 0.9×0.70×0.85 = **0.54**, and — TS 38
over the floor of 25, her Convictions admitting — **F5 at 0.54**. She does not register F3: it was a
quiet exchange at the measuring table. **It is not in her ledger at all.**

**Praefect Aldwin**, Conviction Order 3, Precedent 2, obstinacy 4, Focus 4, Acuity 4, TS 0. He is
overseeing the reckoning: `present_at` (1.00). He registers F1, F2, F3, F4 at **0.72**. F5 is not
blurred for him; it is absent.

**Construal.** stance(Maret→Halvard) = −2, stance(Maret→Gerik) = +3, marks_kinship = 1.
stance(Aldwin→Halvard) = +2, stance(Aldwin→Gerik) = −1, marks_kinship = 0.

| | c1 order_restored | c2 unprovoked_harm | c3 lawful_correction | c4 caste_violence |
|---|---|---|---|---|
| Maret | 0 + (−1.0) = **−1.0** | 3 + 1.0 + 1.5 + 1.0 = **6.5** | *excluded — F3 unregistered* | 2 + 2.5 + 1.0 = **5.5** |
| Aldwin | 3 + 1.0 = **4.0** | 0 − 1.0 − 0.5 = **−1.5** | 2 + 1.0 = **3.0** | **−1.5** |

Maret deposits **c2** at share 0.73 → confidence 0.39. Aldwin deposits **c1** at share 0.62 →
confidence 0.45.

**Note what is and is not in conflict.** F1, F2 and F4 are identical in both ledgers, same values, same
intervals. *They agree on everything that happened.* The disagreement is entirely in construals, which
are `inferred`, which means they never corroborate and never collide as testimony. Two honest witnesses,
no lie anywhere, and an unbridgeable difference. Consensus broadcast cannot produce this; noise on a
single truth cannot either.

**Maret acts.** She raises a petition that the reckoning-warrant be withdrawn from Halvard, backed by
forty-one persons of the hamlet and the Row whose own witnessing ran like hers. It must be carried:
praefecture → ducal steward → the Duke.

**Aldwin acts.** His view for *should I carry this?* has K = 7 + 4 = 11. c1 sits at recency 1.0 ×
confidence 0.45 × relevance 1.0 × stanceweight (1 + 0.8) = **0.81**, near the top.

And in his ledger, from the ninth season, is F0: he **firsthand witnessed Halvard strike a
Crown-Latinate carter with no provocation at all**, confidence 0.78. Its salience:

```
recency 2^(−3/4) = 0.59  ×  0.78  ×  relevance 0.3 (adjacent subject)  ×  stanceweight (1 − 0.8) = 0.2
= 0.028      → rank 19 of his relevant rows. K = 11. He never thinks of it.
```

He **suppresses** the petition. Nothing reaches the steward. A record deposits in his own ledger.
exposure(Aldwin, praefecture_channel) += 3. He is not lying to anyone; his view says the petition is
frivolous, and his view is what `choose` reads.

**Maret investigates.** Six weeks on she performs `interview(Bo, ducal under-steward, "did it reach the
Duke?")`. Bo holds **no claim** — it never arrived. Empty view, rung 1: marks-based expectation, read
off Maret's own visible mark through his mildly negative stance on it. He answers, sincerely, δ = 0,
*"it was frivolous and was dropped properly"*, confidence 0.35, source `inferred(MARKED(Maret,
southern_einhir))`. Maret wins the hearing roll narrowly: she deposits the content at 0.15 and
`SAID(Bo, …)` at 0.85. No `INTENDS(deceive)` — she holds nothing that collides yet.

She performs `research` at the praefecture register, gated by a clerk; she spends one strain on a
Distant Knot for `counsel` and is admitted. The register yields `told_by(register,
¬RECEIVED(steward, petition))` with a **verified** rootprint.

She performs `reconstruct` over three rows: `SAID(Bo, dropped_properly)`, `told_by(register,
not_received)`, and `SAID(Aldwin, "I carried it")` — spoken publicly at the standing date. The register's
verified root and Aldwin's asserted one differ; one is verified. She deposits **`INTENDS(Aldwin,
deceive)` at 0.66** and `CAUSED(Aldwin.suppress, petition_death)`.

**She tells it, in the Kettlemakers' hall, at the reckoning.** Sixty-odd persons witness the telling.
Every one deposits `SAID(Maret, INTENDS(Aldwin, deceive))` at their own vantage. Then each runs their
own contest against their own credulity and their own stance toward Aldwin: those with Order at primary
and warm stance toward the praefect deposit the SAID row and the content at 0.15 — they *heard* her and
do not believe her. **The town does not reach consensus, and that is correct.**

**The consequences are the substrate's, not this document's.** Twenty-three persons' stance toward
Aldwin falls. Nine of them `commit` to a cell whose proposition is that the praefecture's channel be
replaced by a consensus assembly — which is a petition about a *channel*, the most dangerous kind. The
cell's density at Goldenfurt rises. Maret's Masterpiece Examination committee, whose members' stances
have now moved because she made trouble in their hall, will apply those stances to her marks at the
gate — the Free Master gate doing caste work through no rule that mentions caste.

And when the Duke's own investigator finally reaches Aldwin and interviews him, Aldwin will say the
petition was frivolous, **sincerely, δ = 0**, and pass the roll. The investigation is real, the
suppression is real, the town is right, and the culprit is honest. That is what an epistemic engine with
no GM in it should produce, and nothing in the paragraph above was authored.

---

## 13. CHALLENGE — three places I have widened the spine, marked rather than smuggled

**(a) `witness` returns a set, not a claim.** The spine writes `witness(person, event) -> claim`. §2
needs `-> claim*`: one event yields several registered facets plus at most one construal. This is a
signature change, small but real, and I am flagging it rather than quietly pluralising it. Nothing else
in the spine depends on the arity.

**(b) A telling carries a rootprint, which is the one thing a hearer learns about a speaker's ledger.**
The architecture forbids a module reading a sibling's state, and §5 requires the hearer to be able to
compute independence. My resolution: the rootprint is **opaque and asserted**, not read — the hearer
learns that two claims share an origin, never what it was, and the speaker can assert a false one at
the usual cost. But it is a widening of the interface between two persons and it should be examined,
not assumed. The alternative — computing independence globally — reintroduces `world` into a place it
must never be, so I take this one deliberately.

**(c) Convictions weight construal selection, and the spine cut trait vectors.** The spine keeps only
credulity and obstinacy and refuses "a personality trait vector," while §2 and §9 lean hard on the
setting's thirteen Convictions. My defence, and I think it holds: **a Conviction is not a trait, it is a
stance toward a proposition of maximal generality**, and the spine explicitly keeps stance as one table
whose referents include propositions. `ConvW(person, Order)` *is* `stance(person → "order is worth its
cost")`. No new field, no second copy that can disagree with the first. If that reading is rejected,
§2's construal selection needs a different weighting term and the rest of the document is unaffected.

One thing I did **not** challenge and want to record as deliberate: §4's stanceweight floor of 0.05 is
not the belief cap the spine refused. It attenuates **retrieval**, not value. A claim that surfaces
enters the decision at full strength, and a lie that surfaces can still move a duchy.
