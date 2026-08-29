# 01 — The Substrate

## Status: PROPOSED (2026-08-29) — a from-scratch design. Nothing here ratifies on merge.
## Lane: IN (cross-cutting) · Reads: the nine throughlines, Jordan's containment axiom, the NERS charter
## Method: derived, not adapted. No prior design document, ruling, or existing module constrains it.

**The single structural idea.** There is exactly one kind of actor — a person — and exactly two
relations laid over the set of persons: **containment**, a strict tree that answers *where you stand
and whose jurisdiction your voice falls into by default*, and **alignment**, an unconstrained
set-system that answers *who you have thrown in with*. Every other structure in the game — noble
houses, guilds, the Church of Solmund, the Restoration Movement, a settlement's council, two
brothers with a grudge, a peninsula-wide caste order — is derived from persons plus those two
relations, and nothing anywhere is allowed to declare its own scale, its own tier, or its own
opinion. Politics is what happens when a person's container and a person's alignment want different
things from the same hour of their life, and the substrate exists to make that collision the
cheapest thing in the engine to express.

**Reading key.** Every object below is stated as a closed loop — *producer → carrier → consumer* —
and carries an N-line: what emergent possibility is lost if it is cut. Anything without an N-line is
in §6, cut.

---

## 1. The two structures

### 1.1 Containment is a tree, and single-parent on purpose

Containment nodes: **Person → Hearth → Community → Settlement → Territory → Province → Realm**,
extended upward or sideways as the world needs. Every person has exactly one parent hearth; every
hearth exactly one community; and so on. A person's **address** is their path to the root:
*Torben / Hearth of Marlen / Kettlemakers' Row / Goldenfurt / Grauwald / Varfell*.

The interesting design question is why containment is single-parent, because the setting immediately
supplies a counterexample: an Einhir-heritage smith belongs to the Kettlemakers' guild *and* to the
Einhir hamlet outside the wall. Multi-parent containment would represent that in one line.

It is refused, and this is the derivation the whole substrate rests on. If a person can be contained
twice, divided loyalty becomes a set membership and evaporates. Making containment single-parent
forces the second belonging into **alignment**, where it is a commitment the person made, can be
seen to have made, can conceal, can betray, and can be punished for. The smith is *contained* in
Kettlemakers' Row — that is where he sleeps, where the settlement counts him for the tithe, and
whose norms judge his conduct — and *aligned* with the Einhir kinfolk. The friction between his
container's interest and his alignment's interest is not a modelling awkwardness; it is the game.

- Closed loop: written by birth, marriage, admission, migration and death acts (§4); carried on the
  person; read by every aggregation, every judging set, every stake allocation.
- **Cut it and you lose:** a defined "one rung up," therefore any meaning for filtering,
  jurisdiction, or being an outsider anywhere.

### 1.2 Alignment is a set-system with no tier field

A **faction** is a proposition plus a map from persons to a *degree of commitment*. That is the
entire object. It is not a level, a rank, or a class of thing. Two brothers who have sworn to burn
out the reeve who took their barn are a faction. The Church of Solmund is a faction. The
Kettlemakers' guild is a faction whose membership happens to coincide almost exactly with a
community node, and that coincidence is a fact about the world, not a special case in the code.

Membership is per-person, may be secret, and is held at a degree — a Restoration sympathiser who
slips bread to a cell is not a cell member, and the difference is a number on one edge.

### 1.3 Scale is derived, and it is a profile, not a number

Roll member addresses up the containment tree. For any node *n* this yields, with no declaration
anywhere:

- **presence(f, n)** — how many of *f*'s members, weighted by commitment, lie inside *n*;
- **density(f, n)** — that presence over *n*'s weighted population;
- **footprint(f)** — the set of nodes where presence is nonzero.

An earlier hypothesis proposed scale = the lowest containment node spanning all members. It is
rejected for two reasons. First it is brittle: one member who takes ship for Almaic Kyriakos
promotes a village conspiracy to realm scale, which is false about the world. Second, and more
seriously, **nothing important should ever read a scalar scale at all.** A faction's capacity to act
at a node is not a property of its size; it is the question *does this faction contain a person who
can act at that node?* — an office-holder, a burgher with a seat, a Free Master with a vote, or
simply someone whose neighbours' regard is high enough that they will be listened to in the market
square. Capacity routes through persons (T1), and scale is left as what it honestly is: a
**perceptual and reputational profile**. Density is what a stranger reads off you. It sets how loudly
you register, who bothers to oppose you, and what the Inquisitors think they are dealing with. It
gates nothing.

- Closed loop: produced by rolling up member addresses each tick; carried nowhere (recomputed);
  consumed by perception, reputation and threat assessment.
- **Cut it and you lose:** the ability for a small faction to be underestimated and a large one to be
  feared before it acts.

### 1.4 Growth and shrink are one operation

There is exactly one membership operation: `commit(person, faction, Δdegree)`. Degree to zero is
departure. There is no merge, no split, no promote-to-tier, no found-a-national-organisation.

- A **schism** is a subset of members whose commitment migrates to a faction with a rival
  proposition — the Restoration Movement fracturing over whether Einhir practice is political
  inheritance or Thread inheritance is exactly this, and needs no schism mechanic.
- A **merger** is members of A committing to B.
- **Growth into a national body** is many commits, and the profile in §1.3 changes continuously as
  they land.

Jordan's A-4 is satisfied because there is nothing to be discontinuous: the same op, the same
aggregation, the same read. This is also the answer to the prior failure that conflated containment
and alignment by making "faction" a tier, at which point a faction could not grow across a tier
boundary without an authoring act. Here it cannot fail to.

- **Cut it and you lose:** organic factional life — every faction becomes something an author had to
  create at the size it was born at.

---

## 2. The person is the only actor

Persons act. Nothing else does. Containers do not decide, factions do not decide, settlements do not
decide. Where the setting says "the Crown resolved," the substrate says: a person with a post,
holding a view, chose an act, and other persons complied or did not.

The minimum a person must carry is derived by asking which throughline becomes unreachable without
each field.

| Field | Why it cannot be cut |
|---|---|
| **Address** | Without it there is no rung, no jurisdiction, no aggregation. |
| **Marks** | Ascribed, publicly-read attributes: heritage (Northern / Central / Southern Einhir, Crown-Latinate), caste standing, guild grade, house name, Church standing, visible Thread sensitivity. These are what make *the same act by two persons produce different results*. Without marks, caste is a difficulty slider rather than a structure. |
| **Capability** | Aptitudes and practices — the pool the resolver rolls. Without it a person cannot attempt anything. |
| **Stance** | One table, from *referent* → attitude, where referents are persons, factions, propositions and places. Feelings and beliefs-about-value both live here. |
| **Memory** | The claim ledger of §3. |
| **Ties** | Ordinary contacts, plus **Knots** — a person's few deep bindings, typed differently because a Knot is a *channel with bandwidth*: it carries states and tellings that ordinary acquaintance does not, and it is how a person with no post gets news, opportunity and obligation. |

Six fields, and two deliberate fusions. Feelings toward people and stances toward propositions are
**one table**, because both are read by the same routine — how much weight do I give this, how much
do I want it — and splitting them buys nothing. Personality is **two scalars inside that table**
(credulity: how far a telling moves me; obstinacy: how hard my existing stance resists
contradiction) and nothing more; §6 says why the rest is cut.

**Needs are not a field.** They are computed each tick from the person's situation: their hearth's
larder against its mouths, their standing against their siblings-in-container, their unmet
stance-commitments, their exposure to a dispensation's terms. Storing them would be a second copy of
the world that can go stale. Computing them means a person's wants change the instant the world does.

**A person with no office can still act.** Action eligibility never consults office. Every act is
offered to every person; office changes only whether your decision *binds others*, and marks and
regard change only your odds. A hamlet fisher with no post can petition, tell, lie, carry, join,
refuse, conceal, migrate, and kill. What he cannot do is *decide for the settlement* — and even that
he can attempt, by getting a person who can to carry his petition.

**Populations are persons at coarse fidelity, not a second model.** Persons who share an address,
marks and stance are held as a **cohort** — one record with a weight, evaluated once and applied to
all. When an event names one of them, or when a cohort's stance spread widens past the point where
one answer is honest, the cohort **individuates**: it splits into a person and a smaller cohort, same
schema, same fields. Nothing in the game is written for elites-only, because the elite and the cohort
are the same type at different resolutions.

---

## 3. The signature rule

Decision functions of the shape `choose(actor, world)` make every belief system built on top of them
decoration, because the true state is in the argument list. So the substrate fixes the *types* first:

```
choose(person, view)    -> act      # agents. no world argument. ever.
resolve(act, world)     -> event    # the world. no agent argument.
witness(person, event)  -> claim    # the only bridge, and it is per-person
```

Agents read views and write acts. The world reads acts and writes events. Events reach persons only
through `witness`, one person at a time. There is no path by which any decision function can see true
state, and this holds for NPCs and for the player symmetrically: the player's interface *is* their
view, rendered. The player has no extra function.

### 3.1 The view is assembled, not filtered

A view is not a masked copy of the world. A filter can only subtract from truth, which means the
truth is still the thing being operated on; the result is always truth-shaped. Instead:

A person's memory is a ledger of **claims**: `(subject, predicate, value, when, source, confidence)`.
A claim exists only because something put it there — a witnessed event, a **telling** by another
person, or an inference the person drew. If nobody told Torben the granary was full, his ledger holds
no row, and his view does not contain a blurred version of "full." It contains nothing, and he acts
from his prior, his marks-based expectation, or a rumour. That is the difference between a view and a
rendering filter, and it is why absence of knowledge behaves like ignorance rather than like
uncertainty.

**Cost.** Views are built by query with a budget: a person considers at most *K* claims, ranked by
salience = recency × confidence × relevance to the pending decision × **stance weight**. That last
term is not an extra system; it is motivated reasoning falling out of the ranking for free. A
Templar's ledger may contain the claim that exonerates the Einhir smith, and he may never surface it,
because it argues against a stance he holds strongly. T3 costs one multiplication.

### 3.2 Why belief is not capped

A design that adds belief as a bounded modifier to a true value lets a false belief decide only
near-ties — a lie that cannot change any outcome. Here **the true value is not in the decision path
at all.** If the Praefect believes the levy was paid, then for the purpose of his choice it was paid;
there is no −2 and no cap. A well-placed lie can move a duchy.

Correction comes from feedback, not from a ceiling: the resolver produces events from acts taken
against the real world, `witness` deposits contradicting claims, and the person's obstinacy
determines how many contradictions it takes. Beliefs are corrected by *collision with the world*,
which is slow, uneven, and dramatic — exactly the behaviour the setting wants.

### 3.3 Three corollaries the substrate must state

**Divergent witnessing.** `witness` takes the person first. Its output reads the person's vantage,
marks, stance and priors. Two people watching a Templar break a man's arm in the Goldenfurt market
deposit different predicates — *order restored* and *a man's arm broken* — with different
confidences. Consensus deposit is structurally unavailable because there is no function whose
signature permits it.

**Telling is an act.** `tell(speaker, hearer, claim, as_asserted)`, where `as_asserted` need not equal
what the speaker holds. That divergence *is* the lie: it is performed, it is rolled against the
hearer's credulity and their stance toward the speaker, it can be witnessed by a third party, and it
leaves a traceable row in the hearer's ledger naming the speaker as source. Lying is not a flag on a
row; it is something a person does in a place at a time and can be caught doing.

- Closed loop: produced by `tell` / `witness` / inference; carried in the hearer's ledger; consumed by
  view assembly at every decision.
- **Cut it and you lose:** deception, rumour, propaganda, testimony, and every field investigation,
  since an investigation is the act of reconstructing whose claim came from where.

**Corroboration fails closed.** Every claim's source is one of `firsthand(event)`,
`told_by(person, their_claim)`, or `inferred(claims…)`. There is no null source and no untraceable
claim. Two claims are independent only if their firsthand roots differ. A rumour with no findable
origin is given a single synthetic root shared by *every* retelling of it, so one story told three
times corroborates exactly once. Independence is measured on non-empty ancestry by construction.

**Claim identity is a tuple, never a string.** `when` is a mandatory interval. *"Torben was at the
mill in the twelfth season"* and *"Torben was at the mill"* are the same predicate over overlapping
intervals, so assertion and denial collide automatically and disagreement is a computed relation
rather than a coincidence of naming.

---

## 4. The rungs, and what each one owns

A rung is a **role, not a class**: any containment node that holds a shared stake, has a judging set,
and can be addressed. That is what lets the ladder continue upward past Settlement without new
machinery. The four lower rungs are the ones the setting fills.

**Individual — owns the only write path.** Acts, claims, stance. Nothing else in the game can
originate anything.

**Hearth (Family) — owns transmission across time and the claim kin have on each other.** Three
mechanisms live here and nowhere else: the **larder** (a household's material position, the principal
generator of needs), the **succession pointer** (where a name, an address, marks and holdings go on
death), and the **obligation edge** (kin may requisition each other's acts, at a cost in regard that
scales with how unreasonable the demand is).

Cadet branches are not authored; they *fall out*. A cadet branch is a hearth whose succession pointer
does not lead to the main line's holdings. Its members' needs are therefore permanently unsatisfied
by inheritance, so they must seek standing elsewhere — through the Church, through a guild, through
the Löwenritter, through the Restoration, through marriage, through a knife. Every noble-house
intrigue in Varfell and Hafenmark is that one sentence run forward. Fostering, dowry, disinheritance
and legitimation are all edits to the same two mechanisms.

- **Cut it and you lose:** intergenerational pressure. No cadet ambition, no inherited caste standing,
  no succession crises, no reason anyone plans past their own lifetime.

**Community — owns peer judgment and the admission gate.** Two mechanisms. The **judging set**: the
persons who hear about your act by default and apply their stance to it, converting one act into many
small regard changes. And **admission**: an act, performed by persons who already hold standing in the
community, that changes another person's address and confers a mark. The Masterpiece Examination is an
admission act, and the fact that its committee can reject Einhir candidates is not a caste rule bolted
on — it is the committee members' stances applied to the candidate's marks, and it therefore changes
when *they* change.

Crucially, a community holds **no state of its own**. A "norm" is the aggregate of member stances on a
proposition, computed on demand. There is no council brain and no community memory. When the
Kettlemakers disapprove of something, that is a number derived from the persons who make it up, and it
moves when they do.

Setting content at this rung: craft guilds and their grades (apprentice, journeyman, Free Master,
burgher status), Einhir hamlets and Crown-Latinate quarters as ethnic communities inside the same
wall, parish congregations as the Church's presence at the rung where it actually touches people, and
Restoration consensus cells — which are communities whose admission gate is consensus rather than a
masters' vote, and are otherwise the same object.

- **Cut it and you lose:** exclusion. Caste stops being enforceable by anybody, guilds become labels,
  and there is no rung between the hearth and the town where an outsider can be kept out by people who
  know his face.

**Settlement — owns the contested material stake and the first office.** The granary, the wall, the
market, the court, the tithe. This is the first rung whose stake is genuinely zero-sum between the
communities inside it: the granary opens for the hamlet or for the Row, not both. It is also where
**office** first exists — a post whose holder's decision binds persons who never agreed to it
(praefect, magistrate, gate warden). Office is a mark plus a binding power, held by a person,
revocable.

- **Cut it and you lose:** forced competition. Nothing makes guild and hamlet fight over the same
  object, and there is no prize worth the politics.

### 4.1 Sibling competition is one function

At every rung, peers inside a shared container compete for exactly three prizes: **the stake** (the
granary's grain, the levy's exemption), **the regard of the container's members**, and **the
container's offices**. One routine, `contest(container, prize, claimants)`, where claimants are
*factions* — and factions need not be siblings in the tree. The hearths of a community compete for
precedence and marriages; the communities of a settlement compete for grain and seats; and a
Restoration cell whose members are drawn from three hamlets and two guilds competes for the same seat,
through the same function, with the same person-derived capacity. That is Jordan's A-2 and A-3 doing
work in the same line of code, and it is the reason a faction must not be a tier.

---

## 5. The up-stroke and the down-stroke

An earlier hypothesis said these are one object — a "stake" moving in two directions. It fails, but so
does the naive two-object answer, and the reason is instructive.

The two strokes have different truth conditions and different failure modes. The up-object is **a
claim on someone else's action**: it names a respondent, it is adversarial, and its characteristic
failure is being ignored — which must *accumulate*. The down-object is **a change in the world's
terms**: it names no respondent, it cannot fail, and its characteristic failure is not being noticed.
Unify them and one of the two carries a permanently null field — a demand with no respondent, or an
opportunity with a grievance counter that never increments.

But the genuine shared substrate exists, and it is not that both are stakes; it is that **both are
propositions, and the machinery that moves propositions between persons already exists** — the claim
and the telling of §3. So: two objects, one transport layer, and the down-stroke needs almost no new
mechanism at all.

### 5.1 Petition (up)

`Petition(petitioner, proposition, respondent_container, backing)`.

Produced by a person whose computed need exceeds what their own acts can reach. **Backing** is the set
of persons who have lent their stance to it — this is the aggregation, and it is why there is no
separate crowd object: "a town's demand" is a petition with four hundred backers.

A petition **cannot enter a container by itself.** Some person at that container must perform
`carry(person, petition)` — an act, costing the carrier regard with everyone whose stance opposes it,
and gaining regard with the backers. At the rung above, that carrier chooses: **forward** it,
**amend** it (change the proposition, which the backers may or may not learn about), **bundle** it with
others into one composite proposition, or **drop** it.

Dropping is an act, by a named person, at a named time. That is the whole of "a town's demand is
filtered out as irrelevant one rung up" — not a threshold, not a relevance score, but Praefect Aldwin
deciding that the Southern Einhir hamlet's grain petition is not worth the seat he would spend
carrying it into the Court Parliament. The dropped petition does not vanish. It deposits — *if and
when the backers learn of it, which is itself a telling that may never happen or may arrive
distorted* — a grievance stance toward the container and toward Aldwin personally. Grievance is what
makes a person willing to `commit` to a faction whose proposition opposes the container.

Revolt is therefore never a meter. It is many persons committing to a rival proposition until that
faction's density at a node crosses what the settlement's coercive apparatus can hold, and the people
doing it have names, hearths, and a specific man they blame.

- Closed loop: produced by a person's unmet need; carried by named persons rung by rung, each of whom
  may amend, bundle or drop; consumed by a decision at some container — or consumed by no one, which
  writes grievance back into the backers.
- **Cut it and you lose:** everything between silence and revolt. The specific injury of being *heard
  and refused* — which is the injury that actually makes politics — becomes inexpressible.

### 5.2 Dispensation (down)

`Dispensation(issuer, proposition, scope, terms)` — a change to a container's terms: a price, a
prohibition, a levy, an exemption, a blockade, a treaty clause, an excommunication, an ordenanza's
entry standard.

It does not travel by being handed down a chain of posts. It travels by being **noticed**: publishing
a dispensation is a telling, and it deposits claims into the ledgers of persons within scope through
the ordinary channels — the crier, the priest at the parish, the guild notice, the market, a Knot. A
person with no post receives it because deposit is by *presence and channel*, never by post.
Distortion in transit is free: what reaches the hamlet is often not what the Duke signed.

Then nothing further is needed. The person's own need plus capability plus this new claim yields an
**opening** — computed, not stored, by the same routine that lists any person's available acts, now
evaluated over changed terms. A blockade raises the price of salt; the fisher's son who owns a boat
and has a Knot with a smuggler cousin sees a run worth making, and no one authored an opportunity for
him.

- Closed loop: produced by a person holding office (or by treaty, which is two such persons); carried
  by tellings along channels, distorting; consumed by every person in scope, as a claim that changes
  what their own options are worth.
- **Cut it and you lose:** the strategic layer's contact with anybody. Treaties become numbers no one
  feels, and a blockade is a modifier rather than a reason a specific man buys a second boat.

### 5.3 The minimum hook for debate

Containers carry **standing dates**: scheduled moments at which a prize is allocated — the court's
sitting, the tithe reckoning, the levy day, the guild's examination, a truce's expiry. A standing date
makes a proposition contestable, because petitions and dispensations addressing the same proposition
before the same date are in conflict with each other and both sides know when the argument ends. That
is all the substrate provides; the argument system composes on top of it (document 07), and it needs a
*proposition* to attack — which the substrate now supplies.

---

## 6. What is refused, under E-as-a-ratio

Each was considered and cut because no N-line could be written for it, or because a cheaper object
already reaches the same emergence.

- **A faction tier, level, or scale field.** Derivable (§1.3), and declaring it is what makes growth
  discontinuous.
- **A faction-wide reputation scalar.** Regard is per-person toward a referent. A single number
  destroys the case where the Church is loved in Himmelstift and hated three valleys south — which is
  most of the setting.
- **An unrest, loyalty or morale gauge on a settlement.** Derived from the grievance stances of the
  persons in it, or it is dead state that reads as mechanism.
- **A "known %" on a secret.** Knowledge is a row in a knower's ledger. A gauge on the thing known has
  no knower and cannot be interrogated, planted, or refuted.
- **A world event log agents can read.** Events exist for the resolver. Agents receive claims, one
  witness at a time. Anything else reintroduces `world` into the choosing signature by the back door.
- **Any broadcast that deposits the same value into many persons.**
- **A separate population or mass model.** Cohorts are persons at coarse fidelity and individuate on
  demand. Two models means a mechanism that works for a Duke and cannot express the same dynamic for a
  quarter.
- **A confidence cap on belief in decisions.** Correction is by collision with the world, not by
  ceiling. A capped lie is flavour text.
- **Faction merge, split, promote, or found-at-size operations.** One person-level commit, run in two
  directions.
- **A quest or opportunity object.** The down-stroke reaches a person as a changed term, and their
  options are recomputed. Authoring per-person opportunities is how a churning world turns back into
  content.
- **Container-level memory, ledgers, or councils that think.** Containers hold stakes, judging sets and
  dates. Persons hold everything else.
- **A personality trait vector.** Two scalars survive — credulity and obstinacy — because each names a
  distinct emergent possibility (who can be lied to; who can be argued out of a stance). Bravery,
  greed, ambition and the rest are already expressible as stance toward referents plus computed need,
  and a trait that duplicates a stance is a second copy that can disagree with the first.
- **A grievance-to-revolt threshold.** Revolt is a density of commitments to a rival proposition. A
  threshold would let the world revolt without anyone having decided to.

---

## 7. One trace, both directions

Greta is Southern Einhir, contained in the Einhir hamlet outside Goldenfurt, aligned at low degree
with a Restoration cell whose members come from three hamlets and one guild. Varfell's Duke signs a
treaty; a **dispensation** changes the salt price in scope Grauwald; the claim reaches Greta from the
crier, distorted, three days late, and reaches her cousin intact through a **Knot**. Her hearth's
larder plus the new terms compute a need; her capability and her cousin's boat compute an opening; she
runs salt. A Knight of the Peace witnesses it — and what he deposits is *smuggling*, while what her
neighbours deposit is *she fed the Row*. She is fined at the settlement's standing date, and raises a
**petition** that the fine be remitted, backed by forty hamlet neighbours whose stances the case has
moved. The guild burgher whose seat it would cost **drops** it, and says so publicly, because the
Kettlemakers' judging set would punish him for carrying an Einhir grievance. Greta learns of the drop
from her cousin, at second hand, in a version that is angrier than what happened. Her commitment to
the cell goes from sympathiser to member. Thirty others do the same. The cell's density at Goldenfurt
crosses what the praefecture can hold — and the Duke, reading only the *profile*, discovers a faction
he had no reason to think existed.

Nothing in that paragraph was authored. Every step is one of the six person fields, the two relations,
the three signatures, and the two stroke objects.
