# 15 — The Adjudication Register

## Status: PROPOSED (2026-08-29) — rulings made during the design, recorded so they can be attacked.
## Method: each lane was instructed to raise a CHALLENGE rather than silently diverge from the spine.
## This is what was raised and how it was decided. A challenge answered by "the spine wins" is not a
## win for the spine — three of the first seven went the other way and the spine was amended.

**Why this document exists.** A design written by many hands diverges silently unless divergence is
made expensive and disagreement is made cheap. Every lane was told: if the substrate strains under
what you need, say so in a marked section — do not quietly work around it. Seven challenges came
back. Four amended the spine. Recording the losers matters as much as the winners, because a
challenge that was rejected for a bad reason is the thing a later reader most needs to re-open.

---

## A. Challenges that AMENDED the spine

### A-1 · Needs must read the VIEW for the polity terms — ACCEPTED, spine amended
*Raised by 02 (the person).*

The substrate said needs are computed rather than stored, so "a person's wants change the instant the
world does." That is right for the body and **wrong for the polity**. Left standing it breaks T4
inside the needs function: a treaty would change the wants of every person in its scope before any of
them had heard of it — no lie, no telling, no channel, and the signature rule defeated by a helper.

**Ruling: split by source.** Subsistence and standing read the world (you feel hunger; their faces
are in front of you). Commitment and exposure read the view (you must believe the proposition unmet;
you must have heard of the decree, in whatever version reached you). The corrected claim is stronger
than the original: **needs are never stale relative to the person's view, and are supposed to be
stale relative to the world.**

*Why this is the most important ruling in the register:* it shows the signature rule can be defeated
by a function that never takes a `World` parameter, merely by reading one transitively. The type
discipline is necessary and not sufficient, and every derived quantity has to be audited for the same
leak.

### A-2 · The faction profile was a back door — ACCEPTED, spine amended
*Raised by the adversarial pass, not by a lane.*

The substrate computed a faction's presence/density/footprint by rolling up **actual** membership —
including the secret commitments it explicitly permits — and fed the result to perception and threat
assessment, which are decision inputs. That is a derivation of true state reaching a decision without
passing through `witness`: the substrate's own banned object, in aggregate form. Its N-line was false
too: a small faction being underestimated *emerges from* incomplete ledgers, and a true-state profile
makes underestimation harder rather than possible.

**Ruling: two profiles, one readable.** The **true profile** is readable by nobody — it exists for
bookkeeping and tests. Each observer holds an **estimated profile** built from their own claim
ledger. Covert membership is absent from an estimate until somebody's claim names it, so
underestimation becomes the default rather than a special case.

### A-3 · Individuation had no inverse — ACCEPTED, spine amended
*Raised by 02.*

Cohorts individuate into persons; nothing turned persons back. A long campaign therefore accumulates
persons monotonically — the unbounded-population failure, reached by a different route than the one
the design already refused.

**Ruling, adopted as stated because the formulation is better than the problem required:** a person
re-merges when they hold no Knot, no office, no live petition, and **no other person's ledger names
them**. That is: *a person persists exactly as long as somebody remembers them.* The survivors of a
hundred-year campaign are precisely the ones who mattered to someone, arrived at by reference-counting
the world's memory rather than by a cull or an authoring budget.

### A-4 · The Knot's Thread-Sensitivity gate is a deliberate caste asymmetry — ACCEPTED, spine amended
*Raised by 02.*

The substrate names the Knot as how a person with no post gets news — but the setting gates Knots on
TS ≥ 30, so roughly half the peninsula cannot form one.

**Ruling: keep the gate and state it, because the asymmetry is the design.** Every formal institution
gates Southern Einhir *out*; the deepest informal channel, being TS-gated and TS being
heritage-correlated, gates them *in*. That is why Niflhel recruits on the waterfront and why the
Restoration's weaving functions with no wealth and no soldiers. It is now written down specifically so
that a later reader does not "fix" the gate and delete the reason.

---

## B. Challenges DECIDED, spine unchanged

### B-1 · The admission parameter vector is container state — ALLOWED, as a stake
*Raised by 04 (hearth and community).*

04 holds `(α, β, γ, δ, aggregation_rule)` at the community, while the substrate's list of what a
container may hold is "stakes, judging sets and dates."

**Ruling: it is a stake, and the test is met on all three counts** — it is contested, it is allocated
at standing dates, and factions fight over it exactly as they fight over grain. Duke Magnus Vaynard's
entire anti-caste programme is, mechanically, a dispensation editing β for the guilds of Varfell.

The decisive evidence that the object is real rather than a filing convenience is what 04 found
falling out of it unbidden: **raising β changes nobody's stance**, so a committee that wants to
exclude routes the same exclusion through γ (no Free Master will sponsor him) and δ (personal dislike,
unfalsifiable). *A caste-breaking law is evadable through the terms it does not name.* A parameter that
generates that is not bookkeeping.

The proposed fallback — holding the vector on an office instead — is **rejected**, because the
caste-open institutions that matter most (a Restoration cell, a Niflhel recruiter) have no single
office-holder, and the fallback would make them inexpressible.

### B-2 · Standing is community-relative — ALLOWED, and it belongs to 04
*Raised by 04.*

Marks are a person's field; standing is not, and 04 needed one. Its derivation makes standing a
*reading* of marks under a particular community's admission rule, so the same man is Standing 3 in his
hamlet and Standing 0 across the wall.

**Ruling: correct, and the relativity is load-bearing rather than incidental.** A single global
standing number would make migration an escape from caste, which the setting explicitly denies —
marks travel and standing does not. Keep it derived; do not promote it to a stored field, or it
becomes a second copy of the marks that can disagree with them.

### B-3 · `mark_salience` gives marks a second effect — ALLOWED
*Raised by 04.*

Marks affect how an act is *judged* (through the judging set's reading) and, in 04, additionally how
far word of the act *travels*.

**Ruling: allowed, because the second effect is not a duplicate of the first.** Without it a house
name changes how you are judged but not how much you are talked about — and half the observable
behaviour of an aristocracy is the second thing. It also produces a real structural effect for free:
a marked person's charity propagates exactly as far as their transgression.

### B-4 · Per-hearth standing dates may not be standing dates at all — SPLIT
*Raised by 04, flagged rather than hidden, and the flag was correct.*

A seasonal larder reckoning on every hearth means the number of "standing dates" scales with the
number of hearths, which strains the substrate's account of a standing date as a *scheduled
contestable moment*.

**Ruling: they are two different things and the word was doing double duty.** A contestable moment is
one where a **prize is allocated among claimants** — the examination, the court's sitting, the tithe
reckoning, a vacancy, a truce's expiry. A larder reckoning allocates nothing and has no claimants; it
is bookkeeping, and it ticks **once per cohort**, with only an individuated hearth carrying its own.
The distinguishing test, which is now the rule: *if it has no claimants, it is not a standing date.*

### B-5 · A private negotiation is a venue with no container — ALLOWED as presentation, and the
### writer's own reading is adopted
*Raised by 08 (argument and negotiation).*

Every venue in 08 is a container plus a prize plus a date plus decision parameters — but a private
negotiation has no container, which the substrate does not contemplate.

**Ruling: the venue framing is presentational and is kept, because the presentation is an elegance
win rather than a fiction.** 08's own honest reading is correct and is adopted: a private negotiation
is *not* a rung mechanism. It is two persons performing `tell` acts at each other under a
mutually-known deadline, and every mechanism 08 gives it — a proposal that deposits claims, a
reservation set read from one's own ledger, a withdrawal that deposits where your floor lies — is
already the substrate's transport layer doing its ordinary job.

Keeping the venue row is what makes 08 §10's table *visibly one mechanic* across a parliament, a
Dicastery, a guild board, a settlement court, a consensus cell and a private negotiation. Collapsing
it would hide that unity behind two vocabularies for one thing, which costs more than the row does.

**The condition on the ruling:** because it is presentational, nothing may *depend* on a negotiation
having a container. If a later mechanism reads a negotiation's container, that mechanism is wrong,
not the framing.

### B-6 · `witness` returns a set, not a single claim — ACCEPTED
*Raised by 03 (knowledge).* One event yields several registered facets plus at most one construal, so
the signature is `witness(person, event) -> claim*`. Small, real, correctly flagged rather than
quietly pluralised. Nothing in the spine depended on the arity.

### B-7 · A telling carries a rootprint — ACCEPTED, and the reasoning is the ruling
*Raised by 03.* Independence (does this claim share an origin with that one?) must be computable by
the hearer, but a module may not read another person's state.

**Ruling: the rootprint is OPAQUE AND ASSERTED, not read.** The hearer learns *that* two of their
claims share an origin, never *what* it was — which is epistemically exact (you can tell two men are
repeating one story without knowing whose), and the speaker may assert a false one at the usual cost
of any lie. The alternative — computing independence globally — reintroduces `world` into a place it
must never be. Taking the widening deliberately is correct; taking the global computation would have
been the same failure as A-1 and A-2 in a third disguise.

### B-8 · Convictions weight construal, and the spine refused trait vectors — ACCEPTED
*Raised by 03, and independently derived by 02.*

**Ruling: a Conviction is not a trait. It is a stance toward a proposition of maximal generality**,
and the spine already keeps stance as one table whose referents include propositions. So
`ConvW(person, Order)` *is* `stance(person -> "order is worth its cost")` — no new field, and no
second copy that can disagree with the first.

**What makes this bankable rather than merely defensible:** 02 and 03 reached it separately, without
sight of each other's work, and built the same object — 02 as "Convictions are priors that seed a
stance row", 03 as "a Conviction is a stance at maximal generality". Independent rediscovery is the
strongest signal available in this process, and two lanes converging on one derivation is better
evidence than either lane's argument.

### B-9 · Office's "binding power" is observed compliance, not a field — ACCEPTED as a strengthening
*Raised by 12 (coercion and force) as a refinement rather than a divergence.*

The spine says office is "a mark plus a binding power." 12 narrows *binding power* to **observed
compliance**: an order binds exactly insofar as the persons receiving it comply, and a witnessed
refusal deposits a claim — *an order of X was not obeyed* — which then feeds every later willingness
computation.

**Ruling: accepted, and it strengthens the spine rather than straining it.** A stored authority field
would be a container-level scalar of exactly the kind the design refuses everywhere else, and it
would make authority immune to the thing that actually destroys authority. Under 12's reading,
**refusal is contagious through the ledger and authority collapses like a bank run** — which is both
truer and cheaper than any legitimacy meter.

The condition, which 12 states itself: derived strain must stay derived. Caching it would void the
substrate's refusal of container gauges.

### A-5 · `resolve` takes an act SET, not one act — ACCEPTED, spine amended
*Raised by 09 (churn).* Conflict resolution is impossible under a singular signature: to know two
acts touch the same granary, the world must see both.

**Ruling: amended to `resolve(acts, world) -> events`.** This weakens nothing. The constraint the
signature rule enforces is that *agents* cannot see true state; the world seeing everything is what
the world is for. And the reason to make it explicit is exact: a singular signature pushes conflict
handling into a per-act pre-pass, **which is where a hidden turn order gets born.**

### A-6 · The salience floor — TWO LANES DISAGREED, AND THE RESOLUTION KEPT ONE OF THEM
*Raised by 09 against 03's design. This is the only direct conflict between two lanes in the suite,
and it is worth the space because both arguments are right about different claims.*

⚠ **RETRACTED IN PART by A-6b below (audit 16 §3.2).** This row's heading read *"AND THE RESOLUTION
KEEPS BOTH"*, and it does not: the firsthand half was fixed, the testimony half — the case 09 actually
raised — was left clamped, and the gloss below is unsatisfiable under a finite claim budget. Read A-6b
before citing anything here.

**03's position.** Motivated reasoning is a multiplicative stance weight clamped to a floor of 0.05.
A Templar's exonerating claim is retrievable, at roughly twenty times the evidence. Attenuation is on
**retrieval, not value** — once retrieved, a claim decides at full strength.

**09's objection.** If the stance weight can be strong enough, a person with a hard stance can never
surface the claim that argues against it, at any confidence. Obstinacy is then never tested, and the
spine's promise that *"correction comes from collision with the world"* cannot be kept — the
collision happens and the claim never enters a view. 09 needs this: a false claim about an ally must
be correctable, and a sixty-year-old revelation must move people who do not want to be moved.

**Ruling: both, and they compose cleanly because they govern different sources.**

| claim source | rule | why |
|---|---|---|
| `firsthand` | **09's floor.** salience ≥ `recency × confidence`. *(The gloss that stood here — "a thing you saw yourself, recently, with high confidence ALWAYS makes your working set" — is retracted by A-6b: a floor on salience is a floor on the ranking, not a guarantee of inclusion.)* | You may refuse to believe your own eyes — that is obstinacy's job, and obstinacy is the right place for the resistance. You may not fail to *consider* them. |
| `told_by`, `inferred` | **03's clamp.** Stance weight applies, floored at 0.05. | This is where motivated reasoning belongs. What you were *told* is exactly what a committed person should be able to not think about. |

The composition is not a compromise; it is the correct division. **Motivated reasoning stays a
strong bias over testimony and stops being an epistemic prison over experience**, for the cost of one
`max` on one source class. Without it, 03's own Templar could never be corrected by walking into the
room and seeing the thing — which neither lane wants.

### B-10 · An empty existential is ABSENCE, not defeat — ACCEPTED
*Raised by 07.* The spine says contest claimants are factions while capacity routes through persons;
read literally, a faction with realm presence and nobody at the node is a valid claimant, which
readmits scale as a gate through the back door.

**Ruling: resolution runs through the claimant's best-placed member, and a claimant with no such
member is ABSENT rather than defeated — and everyone can see it was absent.** This is the spine's
intent; it did not say so, and the difference is load-bearing.

### B-11 · An office cluster has no owning node — ACCEPTED, with the cost stated
*Raised by 07, answering a question the spine delegated to it.* Offices plus alignment DO suffice for
the Church's four Dicasteries and the guilds' grade ladders: an office cluster is a named set of
offices, plus a proposition, plus the appointment acts that fill them — which is a patronage-topology
support set. No second tree.

**The price, accepted deliberately rather than discovered later: "the Dicastery decided" is
permanently inexpressible.** Only "the four persons holding these posts each did something." You
cannot address a petition to a Dicastery; you address it to a person, and that person can drop it.
That is T1 refusing to be talked around, and **the fiction must never render an institution as a
speaker.** The alternative — a second tree for institutional structure — is rejected: it reintroduces
the multi-parent containment the spine refuses and would let an institution acquire a verb.

### A-1b · A-1 NARROWED — standing reads the peer SET from the world and the regard VALUES from a ledger
*Forced by the audit (16 §3.1) and by the correction pass, which had to split the formula to fix it.*

A-1 ruled that the standing need reads the world. The audit showed the formula reads peers' **true
stance rows**, concealed contempt included, so a secretly hostile burgher moves your need before any
act expresses it — and that its input is another agent's *interior*, which is neither the world nor
the observer's view.

**Narrowed: the peer set is a world read (who is contained alongside you is a fact about the world);
the regard values are a ledger read (only regard you hold a claim about).** The register should have
drawn a THREE-WAY distinction from the start — **world / view / another agent's interior** — and the
third is readable by nobody except through a claim. A-1 as originally written is superseded by this
row on the standing term only; its split of the other three need terms stands.

### A-6b · A-6 RETRACTED IN PART — the firsthand floor stands but is unimplemented; the testimony half is UNRESOLVED
*Forced by the audit (16 §3.2). Recorded here rather than left in the audit because THIS register is
what a later session reads to learn what was decided — and until this row existed it asserted the
opposite of the finding.*

**The firsthand floor stands as a ruling — but it has not reached the document that owns the formula,
and this row will not repeat the mistake of saying otherwise.** `salience ≥ recency × confidence` on
`firsthand` claims is the half of 09's objection the ruling did reach, and nothing below disturbs it.
It is nonetheless **unimplemented**: doc 03 §4's salience is still the flat product
`recency × confidence_live × relevance × stanceweight`, with the 0.05 clamp and no `max`, and its own
prose runs the other way — *"a devastating firsthand contradiction … can still cross, but it takes
roughly twenty times the evidence"*, and *"it does not enter the top-K."* The only place the floor is
written as a formula is 09's original challenge, which proposed it. So the accepted half of A-6 is a
ruling with no owner in the design, and a session implementing salience from doc 03 would build the
clamp and never see this row. Carrying it into 03 is outstanding work, not a settled fact.

**The testimony half is NOT resolved.** 09's stated need was that *a sixty-year-old revelation must move
people who do not want to be moved* — and a revelation arrives as `told_by`, which this ruling left
under 03's stance-weight clamp. The case that motivated the objection is precisely the case the ruling
did not reach. What it fixed is *walk into the room and see it*, which neither lane was arguing about.

**The gloss is unsatisfiable, and that is not a wording problem.** *"Always makes your working set"*
cannot hold under a finite claim budget `K` for a person holding more than `K` recent high-confidence
firsthand claims — which is precisely the investigator this game is about. A floor on **salience** is a
floor on the ranking; **inclusion is decided by the budget.** So the formula and the gloss diverge
exactly where the game is most active, and the divergence widens the more the person has seen.

**Held open, not patched — and the likely shape is named so the next session does not re-derive it.**
The testimony half needs a mechanism, and the one it most likely wants is that a claim's
**corroboration** lifts it past a hostile stance weight: corroboration is what distinguishes a
revelation from a rumour, and it is already computable by the hearer without reading anyone's interior
(B-7's opaque rootprints). Naming the shape is not adopting it. Nothing here rules.

A-6 as originally written is **superseded by this row on the testimony half and on the gloss**; its
firsthand floor stands unchanged.

### B-12 · `chain` owns command reach; `transmit` is an INPUT to it, not a parallel mechanism
*Raised by the correction pass, which declined to invent a resolution — correctly.*

Two mechanisms governed whether an order reaches a subordinate body, by different arithmetic, with no
cross-reference: `chain(C)` (the fraction of a body whose command path reaches an occupied role,
requiring the subordinate to hold a **current claim naming their superior**) and
`transmit(officer)` (a per-officer channel quality derived from capability). That is the
three-leader-formulas defect one rung down.

**Ruling: `chain` is the single owner of command reach, and `transmit` feeds it.** They are not
rivals because they answer different questions, and the composition is the honest one:

- **`chain` answers WHETHER** — is there a path, and does the subordinate currently believe who
  commands them? That is a claim question, and claims are already how everything else in this design
  propagates.
- **`transmit` answers HOW RELIABLY THAT CLAIM STAYS CURRENT** — a capable officer keeps his people
  knowing who they answer to; an incapable one lets it decay. So `transmit` is the rate at which an
  officer refreshes the naming claim, and it enters the model **only through `chain`**.

This preserves the property that makes the succession rule good — a commander killed in a wood at
dusk leaves his share unallocated until a runner is chosen, survives, and is *believed* — and it
stops a second arithmetic from deciding the same thing.

---

## C. The orchestrator's own error, recorded because it is the most instructive one here

### C-1 · The architecture note contradicted the spine, and both were declared binding
Nine lanes were told to compose on the substrate **and** on an architecture note written by the
orchestrator. The note asserted that a faction's scale is "the smallest containment node spanning its
members" — the exact hypothesis the substrate rejects by name, and rejects correctly. It also said a
rung module "receives aggregates," which imports a per-tick push flow the design does not have and
would have re-created the stored aggregate state the whole architecture exists to abolish.

**Ruling: the spine wins on any conflict, and the note was corrected in place.** Aggregates are
computed on demand; a module may compute over its descendants when asked and may not receive pushes.

**Why it is recorded rather than quietly fixed:** the failure mode is specific and it will recur. An
orchestrator who writes a synthesis document *and* dispatches work against it has manufactured a
second source of truth, and the lanes cannot tell which one is wrong. The mitigation is not "be more
careful" — it is that **the spine is a file the lanes read and the orchestrator's notes are not
binding on anyone.** Any future note of this kind should say, in its own first line, that it loses
every conflict.

---

## D. Two decisions taken by the design that a prior process had escalated to Jordan

These are recorded because the earlier critique had marked them as needing a human ruling, and this
design decides them structurally instead. They should be re-opened if either decision is wrong; they
should not be re-opened merely because they were once escalated.

| question, as escalated | how the design answers it |
|---|---|
| **May a false belief ever determine an outcome outright, or only bias weighting inside a cap?** | It determines outcomes outright, and no cap exists, because there is nothing to cap: `choose(person, view)` never sees true state, so a belief is not a bias term added to a real value — it *is* the value the decision reads. Correction comes from collision with the world. The question dissolves rather than being answered. |
| **Is "community" a required rung?** | Answered by Jordan directly this session, and further than the question asked: community *and* family are first-class rungs. Recorded here only so a reader of the old escalation finds its disposition. |

The third escalated question — whether an off-board polity may act through an actorless world event —
is **not** decided here and is genuinely open. The design's answer would be that it may not, because
every agentive pressure must trace to a person; but the setting's Altonia and Schoenland exert real
pressure from off the map, and "generate a person to carry it" and "allow an actorless pressure" are
materially different games. That is a live design choice, not an oversight.
