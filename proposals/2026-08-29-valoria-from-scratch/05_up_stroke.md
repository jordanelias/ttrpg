# 05 — The Up-Stroke: Petition, Aggregation, and Revolt

## Status: PROPOSED (2026-08-29) — from-scratch design. Nothing here ratifies on merge.
## Lane: IN · Composes on `01_substrate.md`, which is binding. Serves T5, T1, T3, T4, T7.
## Scope: everything between one person's unmet need and a duchy changing its terms — including,
## specifically, everything between silence and revolt.

**The single structural idea.** A demand travelling upward is not a message and not a number. It is
**a claim on a named person's hour**, and every rung it crosses is a person deciding whether to spend
that hour. Filtering is therefore not a stage in a pipeline: it is the ordinary act of a man with one
seat and four things he could carry with it. The whole up-stroke is built from that scarcity plus the
substrate's three signatures, and there is no point anywhere at which the engine evaluates whether a
demand is important enough to proceed.

---

## 1. What produces a petition

### 1.1 Shortfall — the one function, and no post appears in it

Each tick, every person (individuated or cohort) computes their needs from their situation, per
substrate §2. A need is a pair `(proposition, urgency)` where the proposition is a *specific change to
some container's terms* that would satisfy it, not a mood. Then:

```
own_acts(p)          = the act menu the ordinary routine already builds for p from
                       capability, marks, ties, and the current terms
reach(p, prop)       = max over a ∈ own_acts(p) of  E[ satisfaction(prop) | a ]
                       — expectation taken over p's VIEW, never the world (§3)
shortfall(p, prop)   = urgency(prop) − reach(p, prop)
```

`petition(prop)` enters `own_acts(p)` when **both** hold:

1. `shortfall(p, prop) > 0` — p's own acts cannot reach it; and
2. p's ledger contains a claim naming some container as holding authority over `prop`.

**There is no threshold constant.** Condition 1 is a comparison of two computed quantities, and
petitioning is then merely *available*: whether p actually does it is decided by the same `choose`
that weighs every other act. A petition nobody bothers to raise is a petition whose expected value
lost to fishing.

Condition 2 is the load-bearing half and it is epistemic. A person who does not know who decides
cannot petition, and a person with a **false** claim about who decides petitions the wrong container —
which is not an error state, it is a common and correct outcome. A Southern Einhir hearth that
petitions the Kettlemakers' hall over a rate the territory court sets has spent a season, spent its
carriers' regard, and produced nothing but a record of asking. That failure mode is free; it comes
from routing the respondent through the ledger instead of through a lookup.

**Same function, both ends of the ladder.**

| | Torvald Aske, hamlet fisher, no post | Duke Magnus Vaynard, Varfell |
|---|---|---|
| proposition | the Goldenfurt granary opens at reckoning rate to hearths outside the wall | the Masterpiece Examination's caste gate is abolished across the realm |
| `own_acts` best reach | 0.31 (fish; sell the boat; requisition a brother) | 0.44 (he can issue a dispensation in scope Varfell — half the guilds sit outside it, and the Church's gate is not his) |
| urgency | 0.78 | 0.91 |
| shortfall | **0.47** | **0.47** |
| respondent | Goldenfurt settlement (praefect) | Realm; and a separate remonstrance to the Dicastery of Doctrinal Adjudication |

Identical computation. The Duke's reach is higher because his act menu is larger, and his act menu is
larger because he holds an office whose dispensations bind others — the only thing office does in this
design. Nothing consults post; post shows up as more entries in `own_acts`.

A **cadet branch** is the case where this runs permanently hot. A cadet hearth's succession pointer
does not lead to the main line's holdings (substrate §4), so its members' standing needs are never
satisfied by inheritance and their shortfall never closes on its own. Cadet sons are therefore the
game's most prolific petitioners — to the Church for a canonry, to a guild for a grade, to the
Löwenritter for a commission, to a house for a marriage — and every one of those petitions is the
same function producing the same object. No ambition trait was required to get them there.

- **Closed loop:** produced by the tick's need computation over larder, standing and terms; carried
  nowhere (recomputed, never stored); consumed by `choose` as one more entry on the act menu.
- **N-line:** cut shortfall and every petition in the game has to be authored by hand, which is the
  failure where a hamlet only wants what a designer decided it wants.

### 1.2 The petition object, and where its truth lives

```
Petition {
  petitioner, proposition, respondent_container,
  backing:  set of (person, mode ∈ {public, concealed}, weight),
  route:    ordered list of (carrier, act ∈ {raise,forward,amend,bundle,drop}, when, proposition_as_carried)
}
```

`route` is **world state, not anybody's knowledge.** No person reads it. A person learns what happened
to a petition only through claims, deposited by witnessing a sitting or by being told. The route
exists because a *field investigation* (T9) is precisely the act of reconstructing it, and because a
remonstrance or an argument (doc 07) needs something citable to attack. Its consumers are the
investigator and the arguer, not a decision function.

- **Closed loop:** produced by each carriage act; carried on the petition; consumed by investigation
  and by argument as the ground truth those two are trying to recover.
- **N-line:** cut the route and a lie about what was carried is unfalsifiable, which makes AMEND
  (§3.2) a free action and kills the whole deception layer of the up-stroke.

---

## 2. Backing is the aggregation

There is no crowd object. "A town's demand" is a petition with four hundred names on it, and the four
hundred got there one act at a time.

### 2.1 Coming to back routes through knowledge

```
back(p, P, mode):
  precondition:  claim(p, "P exists, asking prop", confidence ≥ 0.3) ∈ ledger(p)
  precondition:  stance(p, prop) > 0  OR  stance(p, petitioner) high enough to lend as a favour
  weight(p,P) =  stance(p, prop) × (1 + credibility(p))     # credibility derived from marks + grade
```

The first precondition is the whole of "it routes through the telling machinery." A petition raised at
the hamlet well reaches the hamlet; one raised in the Kettlemakers' hall reaches the Row; one that
crosses between them did so because a named person told someone across the line, and that person's Knot
or trade tie is why the coalition exists. Backing propagation *is* telling propagation.

The second lets a person back what they do not want, for the petitioner's sake — a lend, visible in the
route, and the thing a later betrayal is measured against.

### 2.2 Two modes, two costs, and why neither dominates

**Public backing** puts the name on a roll and deposits a durable claim in every member of the
backer's judging sets:

```
for each j ∈ judging_sets(p):
    Δstance(j, p)  +=  stance(j, prop) × visibility(j, p)
    deposit claim(j, "p backs P", firsthand or told)      ← durable, and read at every later allocation
```

Note the sign: it is *positive* where the judging set agrees. A hamlet fisher backing a hamlet grain
petition pays nothing inside the hamlet, because his judging sets are the hamlet's. Hedda Brann, a
Kettlemakers' journeyman whose Free Master candidacy sits before a committee that reads exactly this
claim, pays enormously. Same act, opposite costs, and no rule mentions caste to produce it.

**Concealed backing** is a single `tell(p, carrier, "I back P")` to the carrier alone. No judging-set
deposit, no exposure claim, no regard gain — and, critically, **no entry on any public roll**. It
counts only toward the carrier's private total.

Dominance check (§9): concealed looks free, but a carrier gains regard only from backers *known* to
have backed, so a petition backed only in secret is one nobody will carry. Safety against carriability.

### 2.3 How backing is read by the person deciding

Three different numbers exist and they routinely disagree.

| number | who has it | how it's obtained |
|---|---|---|
| `true_roll(P)` | nobody | world state; only an investigation approximates it |
| `visible_backing(P, reader)` | each reader, differently | the subset of the roll the reader's own ledger holds claims about |
| `asserted_total` | whatever the carrier says | a `tell`, which may be false and is catchable |

The man who carries the petition is also the man who reports how many wanted it, and his report is a
speech act with a source row in the hearer's ledger. A carrier who inflates a roll to make a
proposition look inevitable is doing something a rival can investigate and expose — and the exposure is
an ordinary claim, not a special event.

- **Closed loop:** produced by `back` acts, which are produced by tellings; carried on the petition
  (truth) and in ledgers (knowledge); consumed by carriers valuing a carriage and by respondents
  valuing a grant.
- **N-line:** cut backing and aggregation has no carrier — individual resentment can only reach the
  political layer through someone who already holds a post, which is the elite-only failure.

---

## 3. Carriage, and the four choices

### 3.1 `carry` and the seat

```
carry(c, P):
  precondition: c holds STANDING at respondent_container(P) — a seat, an office, a right of
                audience, or membership in its judging set
  precondition: claim(c, "P exists") ∈ ledger(c)
  cost:  one ITEM of the container's standing-date capacity  (see below)
  regard_cost(c) = Σ_{j ∈ judging_set(container)} max(0, −stance(j, prop)) × weight(j)
  regard_gain(c) = Σ_{b ∈ backers who LEARN c carried} stance(b, prop) × weight(b)
```

`regard_gain` is over backers who learn — another telling, which may not happen. A carrier who wants
credit must arrange for the credit to be heard, and that is an act.

**Seat scarcity is the reason DROP exists at all.** Every container's standing date (substrate §5.3)
hears a finite number of items — a term of the container, and therefore something a dispensation can
change, which makes procedural reform a real political move. The Grauwald territory court hears eleven
items a sitting; a praefect holds one seat and carries one thing with it. Filtering is not a policy but
arithmetic about hours — the same arithmetic that makes a fisher choose between the tide and the chapel.

### 3.2 FORWARD / AMEND / BUNDLE / DROP

**FORWARD.** Proposition unchanged; the respondent becomes the container one rung up. The roll travels
intact — but every reader at the new rung reads it through their own ledger, so a roll of four hundred
nobody upstream has heard of reads as a roll of nine. The cheapest act, and what an honest carrier with
no ambition does.

**AMEND.** `amend(c, P, prop')` replaces the proposition and keeps the roll.

```
distance(prop, prop') = |{ fields of the proposition tuple (subject, action, object, scope, terms)
                           that differ }|
```

**The backers are not notified. Ever.** Notification is a telling, and the carrier chooses whether to
perform it and what to assert. Three consequences:

- A backer who **learns** and finds `stance(backer, prop') < 0` may `withdraw` — but only at the next
  standing date, frequently after the decision, and withdrawal carries its own exposure.
- A backer who **never learns** stays on the roll of a proposition he never wanted: refused, he takes
  grievance for something he did not ask for; granted, he is on record as having wanted it.
- A carrier who amends and tells the backers a false version — `tell(c, backer, "I carried your grain
  petition")` while `proposition_as_carried` reads *the hamlet's fishing right is commuted to a cash
  levy* — has told an ordinary lie against an ordinary route record. Catchable by investigation,
  citable forever.

Amendment is where a carrier converts other people's grievance into his own instrument. It costs
nothing at the moment of performance, which is why it must be discoverable rather than penalised.

**BUNDLE.** `bundle(c, [P₁..Pₙ]) → P*`, one item of seat capacity for n constituencies. Two shapes,
and they are not the same move:

| shape | proposition | effect on the roll | effect on grantability |
|---|---|---|---|
| **conjunctive** | prop₁ ∧ … ∧ propₙ, terms preserved | union of rolls | unchanged; each part still grantable by grace |
| **generalizing** | one general term replacing n particulars — *"the granary prices grain at the reckoning rate to every hearth in the territory, irrespective of wall"* | union of rolls, and the constituencies are now co-signatories on one thing | **changes PRIVATE to COMMON** (§6.2): no longer grantable by grace, only by a dispensation |

The generalizing bundle is how a rung genuinely aggregates rather than merely relaying, and it is how
a coalition forms across a caste line without any rule about caste: four Southern Einhir hamlet asks
and sixty-seven Central Einhir apprentices' bread-price asks have the same general form, so one carrier
who notices can put them under one proposition.

It is also double-edged in exactly the way the R criterion demands. The composite is refused as a
whole; all n backing sets take grievance simultaneously, at the same named person, on the same day. A
competent aggregator manufactures, in one act, the coalition that will destroy him.

**DROP.** `drop(c, P, publicity ∈ {stated, silent})`. The petition does not advance. Nothing whatever
happens at the container. This is §4.

---

## 4. Dropping is the filter, and it is a man with a seat

Praefect **Aldwin Storr**, Crown post at Goldenfurt, holds one of Goldenfurt's two seats at the
Grauwald territory court. Four candidates for the sitting. He runs the ordinary valuation — the same
`choose(person, view)` a fisher runs — and here is what is actually in it:

| candidate item | regard w/ judging set | regard cost | own need relief | **V** |
|---|---|---|---|---|
| the bundled grain proposition (COMMON; 111 public backers, of whom Aldwin's ledger names 41) | +0.4 | −2.1 (the Row's burghers; Free Master Bergthor Kelm) | 0 | **−1.7** |
| the Kettlemakers' second market day | +1.6 | −0.2 | 0 | +1.4 |
| the Löwenritter requisition of the south road | +0.3 | −0.4 | +0.2 (Grandmaster Ehrenwall's regard) | +0.1 |
| his own supplication that his son **Ansgar** be admitted to the Masterpiece Examination out of order | 0 | −0.6 (spends Kelm's goodwill) | **+2.9** | **+2.3** |

He carries Ansgar's. He drops the grain bundle. What he weighed:

1. **Seat scarcity** — one item, four candidates. Binding.
2. **The judging set of the container he sits in**, which is the Row's burghers and the Free Masters,
   not the hamlet. Their stances toward the proposition are negative and their regard is what his
   post rests on.
3. **The backers he can see.** He names 41 of 111. Backing he does not know about has, by
   construction, no weight in his valuation. This is not a discount — it is absence.
4. **His own computed need**, which is his son's standing, and which is a shortfall exactly like
   Torvald's, resolved by a supplication exactly like Torvald's.
5. **His belief about consequence.** His ledger holds *no claim* that the Southern Einhir hamlet can
   hurt him.

Point 5 is the payload. **Aldwin is not accepting a risk. He cannot see one.** The cell in the hamlet
is concealed alignment; concealed alignment deposits no claims; a person with no claims about a danger
acts from ignorance, not uncertainty (substrate §3.1). A relevance score would make this a tuning
question. A man's valuation over his own ledger makes it a *mistake he had every reason to make* — the
only version of filtering that produces politics rather than friction.

**Stated versus silent.** Aldwin drops **silent**. A stated drop declares the refusal to the judging
set — cheap with them, and it reaches the backers eventually with his name on it. Silent tells no one,
and the sixty-seven apprentices go on believing it pending. He chooses silence because the apprentices
sit inside the Row and he may want their backing one day, while the hamlet's forty-four are people he
does not need. A legible human reason, and no rule produced it.

**Lapse.** At the container's next standing date, a petition neither heard nor forwarded has lapsed.
Lapse is not an act by anybody — it is the date passing. Whether the backers learn that it lapsed, or
that it was refused, or that it was traded, depends entirely on who tells them.

### 4.1 The deposit, and where the grudge lands

When a backer learns:

```
m = shortfall_at_raising(p, prop) × weight(p, P) × amplification(chain)
amplification(chain) = Π over retellings (1 + bias(teller, referent))
Δstance(p → named_person) = m × names_person(claim)
Δstance(p → container)    = m × (1 − names_person(claim))
```

**The telling's grammar decides where the grudge lands.** A claim whose predicate names an actor —
*"Aldwin carried his son's name instead of our grain"* — deposits on Aldwin. One naming only the
container — *"the court heard no grain item"* — deposits on the praefecture. That matters downstream:
a grudge at a person is discharged by removing the person, a grudge at a container is not (§8.2).
Nothing was designed to produce the asymmetry; it follows from stance rows having referents.

**Distortion is self-limiting without a cap.** Each retelling raises `amplification` and lowers
confidence, and confidence is a salience term in view assembly (substrate §3.1) — so the angriest
version of a story is the least likely to surface in a decision, *unless* the hearer's stance weight on
the referent is already high, in which case it surfaces anyway. Motivated reasoning producing
radicalisation with no radicalisation mechanic, for one multiplication that already existed.

- **Closed loop:** produced by `drop`/lapse plus a telling; carried as ordinary stance rows in the
  backers' tables; consumed by every subsequent valuation the backer makes, including `commit`.
- **N-line:** cut the conditional deposit and refusal becomes either instantly and uniformly felt (a
  broadcast, which the substrate refuses) or never felt (filtering with no consequence, which is the
  prior attempt's failure).

---

## 5. Grievance, and the road to revolt

### 5.1 There is no revolt object

Grievance is not a new type. It is a stance row with a negative attitude toward a container or a
person. Its only special property is what it does to a valuation: a person weighing
`commit(p, f, +Δ)` toward a faction whose proposition *opposes the referent they hold grievance
toward* values that commitment by their grievance magnitude. Grievance makes commitment cheap. That is
its whole mechanical role.

**Spontaneous emergence needs no recruiter.** A proposition is a *claim*, and claims travel by telling
independently of any member travelling. A hamlet with no cell, holding Yrsa Vossen's proposition at
confidence 0.4 plus a fresh grievance whose referent that proposition addresses, produces commits. The
setting's requirement that the Restoration Movement can emerge spontaneously from territorial neglect
is satisfied by two mechanisms that already exist.

### 5.2 The coercive computation

```
force(f, n)  = Σ_{p ∈ members(f) inside n}  degree(p,f) × martial(p) × willing(p, act)
hold(n, tgt) = Σ_{p ∈ armed(n)} martial(p) × readiness(p) × compliance(p, order_against(tgt))

compliance(p, o) = the output of choose(p, view(p)) with o on the menu — a DECISION, not a stat
```

Note `presence`, not density. Density is what a stranger reads off a faction (substrate §1.3) and it
still gates nothing; force is an absolute weighted count of persons who would fight.

The critical term is `compliance`. Coercive capacity is made of persons, each with a stance toward the
order and toward the people they would be ordered against. Gate warden **Ivar Holt**, whose wife's kin
live in the hamlet, computes `compliance ≈ 0.2` against an order to clear it and `1.0` against an
order to clear the wharf. So the *paper* capacity at Goldenfurt is seventeen armed persons and the
actual capacity against this particular target is nearer seven — and **nobody can read that off a
roster**, because it is not on the roster. It is the output of seventeen private decisions.

Both sides move, and they move from the same cause: grievance that raises `force` lowers `hold`
through the same stance rows, because the watch lives in the town.

**The two evaluations, which are not the same evaluation.** This is the distinction the whole section
turns on, and conflating them is how a threshold sneaks back in.

| | **at DECISION** | **at RESOLUTION** |
|---|---|---|
| who computes | each person, inside `choose(p, view(p))` | the resolver, inside `resolve(act, world)` |
| what it reads | that person's **estimated profile** — the memberships and rosters their own ledger names (substrate §1.3) | true state: who actually turned out, whose compliance actually held |
| what it produces | one person's act | the event, and what the square looked like |
| can it be wrong | constantly, and that is the point | no — it is the world |

The substrate is right that the comparison is a fact about the world and not about anyone's estimate.
It is a fact **evaluated after the acts are taken**, by the function whose signature already takes the
world. What it is never allowed to be is an input to anybody's decision to rise, because no decision
function may take `world` at all.

### 5.3 Why the density formulation is not a threshold in disguise

A threshold is a **precondition**: state is measured, a line is crossed, and something is caused. The
density formulation is a **postcondition**: acts are chosen for other reasons, and the comparison
describes how they came out. The difference is not rhetorical, and here are three falsifiers that make
it checkable rather than asserted.

1. **No signature anywhere in the engine has return type "revolt," and no function is named for it.**
   What the world records is acts: five persons forced the granary's south door, and four of seventeen
   armed men stood. Whether that was a riot, a revolt, or a food theft is a predicate that *witnesses
   deposit*, and different witnesses deposit different ones (substrate §3.3). "The Grauwald rising" is
   a name applied afterwards by people, in claims, and two of them will disagree about when it began.
2. **`force` and `hold` never appear in a precondition.** The resolver computes them over true state
   to settle a fight that is already happening — that is what a resolver is for and it takes `world`
   by signature. What may not exist is any place where those quantities are read *before* an act, to
   decide whether persons rise. A person deciding to rise reads their own **estimated** profile and
   their own claims about the garrison. If a comparison of true `force` to true `hold` ever appears on
   the left of a branch that produces acts rather than resolving them, that is the bug.
3. **The band is publishable and the trigger point does not exist.** A player or an investigating NPC
   can see every input to their own estimate — the committed persons they know of, the hamlet's
   population, the roll of the failed petition, the watch's roster — and read a coarse band. There is
   no line under the band, because there is nothing for a line to gate.

The behavioural consequence, and it is the one worth having: **people rise when they believe they can
win, and the world then tells them whether they were right.** A cell rising on a false claim about the
garrison's size, and being destroyed, is a first-class outcome. So is a garrison that surrenders to
nine men because its commander's estimate of the crowd came from a frightened runner. Neither is
reachable in a design where the rising is caused by the true numbers crossing.

And the people rising have names, hearths, and a specific man they blame — because the grievance rows
that made their commitments cheap carry referents, and the referents are Aldwin and the praefecture.
The targeting follows: a dearth rising goes to the **granary keeper** first, then the buyers who
forestalled, then the post. It reaches the praefect last if at all, because the persons in the rising
value acts against referents they hold claims about, and the granary keeper is the man they can see.

- **N-line:** cut the person-level force computation and revolt becomes a number crossing a line,
  which is the design where the world revolts without anyone having decided to — refused by the
  substrate's §6 and by this section independently.

---

## 6. The ladder of instruments

Between silence and revolt there must be a **legitimate form of opposition that affirms the authority
it opposes**. Without it, the only expressible mass act is a completed revolt, which was the prior
attempt's structural failure.

### 6.1 Two instruments

**SUPPLICATION** (`form = supplication`). Petitioner → office-holder, seeking **grace**: an exception
to terms, for named persons, leaving the terms intact. Available across any rank gap. The ask
presupposes the giver's right to give, so it is an act of submission and read as such by the judging
set. Refusal deposits grievance on the *person*, the request having been framed as personal. No ladder
follows; a second supplication is a second ask, valued lower by a man who already said no.

**REMONSTRANCE** (`form = remonstrance`). Requires the petitioner to hold **standing at an institution
with a registered right of remonstrance** — the Hafenmark Parliament, a guild's Free Masters in
assembly, one of the Church's four Dicasteries, a duchy's court. It contests a named **dispensation**
on one of three grounds — *outside the issuer's scope* / *unlawful in its terms* / *harmful in its
operation* — and it enters the record whether or not it succeeds. A recorded remonstrance has no force
and full citability, forever. That is nearly free and it is what a later argument (doc 07) or a later
investigation attacks with.

**The caste consequence, from one precondition and no caste rule.** Remonstrance requires standing at
an institution, and the setting's institutions rank-gate standing individually: the Crown behind public
deeds or inner-circle sponsorship, the Church strongly (a Southern Einhir Canon is a scandal), the
guilds through the Masterpiece Examination. So a Southern Einhir person is ordinarily confined to
supplication — able to beg for grace, unable to contest a measure — and the two caste-open
institutions, the Löwenritter and Niflhel, are the *only* routes by which a Southern Einhir voice
reaches the ladder. Caste reproduced by institutions rather than malice, out of a precondition, with no
rule naming a heritage.

### 6.2 COMMON versus PRIVATE — computed, not declared

```
form(P) = COMMON   if scope(proposition) is a container (all persons at n)
          PRIVATE  if the proposition names specific persons
```

| | PRIVATE | COMMON |
|---|---|---|
| satisfiable by | grace — one person's discretionary act | only by a **dispensation** changing terms |
| cost to respondent | low, invisible | high, visible, and it manufactures new shortfalls in whoever the old terms favoured |
| grievance on refusal | petitioner and a few backers | every backer, and every person in scope who learns |
| conversion | — | **the generalizing bundle converts PRIVATE → COMMON** |

A carrier who generalizes four grain supplications into one common proposition has taken four things
cheap to grant and made one thing expensive to grant — raising the refusal rate and broadening the
grievance in the same act. Aggregation is not free, which is why an aggregator is a dangerous person
rather than a helpful one.

### 6.3 The escalation ladder

A remonstrance that the issuer resists runs a real four-step ladder. `step` is a small integer on the
`(institution, proposition)` pair — the only new state in this section.

| step | act | performer | effect |
|---|---|---|---|
| 1 | **remonstrance** | the assembly | the dispensation is **suspended in that scope** until answered |
| 2 | **letter of command** | the issuer | orders registration regardless; suspension lifts |
| 3 | **iterated remonstrance** | the assembly again | suspension resumes; the record now carries two objections, both citable, and the assembly's members are named |
| 4 | **session of enforcement** | the issuer, **in person, at the institution's own seat** | registration is compelled; the assembly's right of remonstrance on this proposition is spent for the term |

The costs are asymmetric, which makes the ladder a fork rather than a countdown.

- Step 2 is cheap for the issuer and buys a season.
- Step 4 is expensive and **structural**: he must be bodily present in a room full of persons whose
  stance he has just overridden — a witnessed event depositing a high-salience claim in every
  attendee's ledger. Δstance per attendee scales with `step`, so the fourth step after two iterations
  costs far more than the same act at the first.
- Step 3 costs the assembly **exposure**: iterating names them, readable by anyone who later wants to
  know who opposed the Crown.

The gift is that a duchess remonstrating against a Crown levy is *not rebelling*. Duchess Inge Baralta,
whose Crown claim makes every act of hers readable as preparation, can contest a measure in a form that
publicly performs the Crown's right to levy — acquiring a record of loyal opposition and a citable
grievance at once. That is the space between silence and revolt, and, because the record is citable and
the ladder public, the visible approach march to a Crown Succession Contest nobody can name as treason.

### 6.4 Rank-indexed form, and the insult

Rank is **derived from marks**, not a new field:

```
rank(p) = max over standings p holds:
   office     praefect 4 · magistrate 4 · burgher 3 · gate warden 2
   guild      Free Master 3 · journeyman 2 · apprentice 1
   Church     Cardinal 6 · Canon 4 · parish priest 3
   house      ducal 6 · cadet 4 · landed 3
   default    1
gap = rank(respondent) − rank(petitioner)
```

Heritage does not appear in `rank`. It appears in the gates on *acquiring* each standing, per
institution, which is where the setting puts it.

```
gap ≤ 1   any form; direct address permitted
gap = 2   supplication or remonstrance; must be CARRIED — no direct address
gap ≥ 3   supplication only; must be carried; AND requires an INTERCESSOR whose own gap
          to the respondent is ≤ 2
```

**A petition in the wrong form is not rejected. It is received as an insult.** The respondent's stance
toward the petitioner moves negative, and the judging set witnesses a man who does not know his place,
depositing a claim that *confirms the mark*: "Southern Einhir do not know the forms." The protocol
table reproduces caste with no rule mentioning caste — and the wrong form is always the *faster* route,
so it stays permanently tempting.

**Intercession.** The outcome is modified by the intercessor's standing with the respondent, not the
petitioner's. A fisher's realistic route at gap 3 is therefore *finding someone who can speak to the
man*, and that search — through Knots, the parish, a trade tie — is the up-stroke's gameplay at long
rank gaps.

- **N-line:** cut rank-indexed form and caste becomes a difficulty modifier on a roll instead of a
  structure a person can be trapped by, mis-navigate, or learn to route around.

---

## 7. Aggregate low-rank leverage

Both halves of this fall out of the seat, which is the same scarce object as §3.1.

### 7.1 Coalescing mid-rank mass

```
carriage_mass(P, n) = Σ_{c ∈ seatholders(n)} seat_weight(c) × [ c carried or PUBLICLY backed P ]
```

A container's terms change when carriage mass exceeds the seat weight of seatholders who publicly
oppose. Both sides are counts of persons who chose, so this is a vote, not a gauge.

Grauwald territory court seat weights: ducal proxy 5 · praefects 2 each (four of them) · Free Masters
1 each (eleven) · Church 3. Eleven Free Masters coalescing = **11**, against ducal proxy + two
praefects = **9**. Mid-rank mass forces exactly the shift a single top-rank defector would, and the
equivalence is arithmetic a player can count rather than a rule that asserts it.

### 7.2 Rank is secession blast radius, and the radius is thinness

```
thinness(n)            = 1 / |carriers available for n → parent(n)|
propagation_depth(p)   = consecutive rungs upward, from p's container, at which p is the SOLE
                         available carrier
blast_radius(p)        = the subtree rooted at the highest such rung
```

| defector | seats above him | thinness | depth | blast radius |
|---|---|---|---|---|
| Praefect Aldwin | Goldenfurt holds 2 seats at the territory court | 1/2 | 0 | Goldenfurt's own petitions stall. A nuisance. |
| Free Master Bergthor Kelm | eleven Free Master seats | 1/11 | 0 | nothing. One vote. |
| Duke Magnus Vaynard | **Varfell holds one seat at the Realm, and it is his** | 1/1 | 1 | **all of Varfell severed from realm decision-making, in one act** |

A duke's defection is a secession and a praefect's is an inconvenience, and the difference is not a
rank number — it is how thin the layer above him is. Change the Realm's charter to seat two proxies
per duchy and Magnus's defection stops being a secession, by arithmetic.

### 7.3 Where the two meet, which is the point

Low-rank mass propagates upward **exactly as far as the first thin layer it reaches.** Eleven Free
Masters coalescing at Goldenfurt sever nothing, because the layer above them is thick with eleven
equivalent seats. But eleven Free Masters coalescing to *deny Aldwin the regard his carriage depends
on* make his carriage impossible — and **Aldwin is the thin layer.** Same formula, opposite
consequence, depending only on where the thinness sits.

It is also why the leverage works at a territory court and is unavailable at the Realm, whose seats are
three ducal proxies, four Cardinals and the Crown: there is no mid-rank mass to coalesce, so a demand
that must reach the Realm has no route but through one of eight persons. The containment axiom and T5
together are why the peninsula's politics look the way they do.

- **N-line:** cut thinness and every defection is worth its holder's rank, which makes reforming a
  charter meaningless and makes the question "who is irreplaceable here?" unaskable.

---

## 8. The instability ratchet

### 8.1 Dormant grievance

Suppression is an act that ends a set of persons' acts **without changing the terms that produced
their need**: a clearing, a proscription, a hanging, a coercive dispensation.

```
suppress(actor, targets, force):
  the targets' acts toward the proposition end (dispersed, imprisoned, dead)
  for every person p' who witnesses or is told, with stance(p', prop) > 0:
      the active grievance row is flagged DORMANT
      its magnitude is PRESERVED, not reduced
      its RE-ARM PREDICATE is recorded: (proposition, named actor, container)
```

Dormant rows:

- **do not enter valuation** while dormant — so nothing happens, and the suppression genuinely
  "worked";
- **are inherited.** On a hearth's succession the row transmits to the heir at reduced magnitude,
  using the substrate's existing succession pointer. Generational, with no generational mechanism;
- **re-arm** the moment a claim satisfying the predicate enters any holder's ledger — the same
  proposition raised again, the same container refusing again, the named actor's name surfacing;
- **re-arm at magnitude.** The person's shortfall-to-act is therefore crossed on the *first* refusal
  rather than the fourth. Each collision fires lower than the last. **The accumulator does not reset,
  because nothing resets it.**

This is not a settlement gauge. There is no number on Goldenfurt. There are rows in the stance tables
of named persons in Goldenfurt, and if those persons die without heirs the rows die with them.

### 8.2 What clears a dormant row, and what does not

**Only the terms actually changing.** A dispensation satisfying the original proposition clears every
dormant row referencing that proposition, at every holder, everywhere. A structural fix is a
structural fix.

**Killing the man does not.** Removing Aldwin clears rows whose *referent is Aldwin* — forty-four of
them, because §4.1's telling named him — and touches no row whose referent is the praefecture. The
personnel fix works exactly on the part it addresses and fails exactly on the rest, and which part is
larger was decided seasons earlier by the grammar of a rumour. Nothing asserts that structural fixes
are better. It is computed.

**Suppression does not require a cruel man.** `suppress` names no intent. Confessor Arne Himlensendt of
the Church of Solmund, sincerely devout and pastorally compassionate, ends a hamlet's Thread practice
by absorbing it into orthodox observance and believes he has healed something. The acts stop; the terms
that produced the need are untouched; the rows go dormant at full magnitude with his name in their
re-arm predicate. Two generations on, a Dicastery of Defense of the Faith inquest into the same hamlet
re-arms four hundred of them at once, and nobody involved did anything but their office. Institutional
harm nobody intends is the setting's stated model, and it is what this mechanism produces by default.

**Bound to the setting.** Southern Einhir grievance is precisely a body of dormant rows: the
Catastrophe's blame, exclusion from the Secession War coalition leadership, and every subsequent
suppression, held per-person across generations and re-arming on each new institutional refusal. The
Restoration Movement's spontaneous emergence from territorial neglect (§5.1) is those rows re-arming
where the proposition happened to arrive by telling. Neither needed authoring.

- **Closed loop:** produced by `suppress`; carried as flagged stance rows, transmitted by succession;
  consumed by the re-arm check on every incoming claim, and cleared only by a satisfying dispensation.
- **N-line:** cut the dormant flag and suppression is either free (grievance evaporates, so violence
  always works) or permanent (grievance never abates, so nothing recovers). Both are dead worlds.

---

## 9. R-criterion check on this design

Every fork: shape of gain against shape of cost over time. Decaying gain against compounding cost is a
structural failure, not a tuning note.

| fork | shape of gain | shape of cost | verdict |
|---|---|---|---|
| (a) petition vs act alone | competes on expected value like any act | one hour | live. A person for whom it never pays has no political voice — true of hamlet fishers, not a flaw |
| (b) **repeated petitioning** | `P(grant)·U`, decaying geometrically per refusal | exposure claims, durable and accumulating | **would be dominated — fixed below** |
| (c) revolt vs petition | step function | catastrophic, personal, non-repeatable | **hazard runs the other way — fixed below** |
| (d) carrier: drop vs carry | immediate regard, non-decaying | delayed, conditional grievance | **would be dominant — fixed below** |
| (e) public vs concealed backing | concealed avoids all exposure | concealed yields the carrier no regard, so nobody carries it | live. Safety against carriability |
| (f) stated vs silent drop | silent buys delay and personal cover today | silent deposits on the *person* when it breaks; stated deposits on the container now | live, different shapes |
| (g) supplication vs remonstrance | grace: cheap, private, immediate | remonstrance: suspends the measure for everyone and spends the institution's right for the term | live, and only a fork for persons with standing |
| (h) **suppress vs concede** | suppression's gain decays as rows re-arm | durable, compounding | **would be dominated both ways — fixed below** |

**(b) Repeated petitioning — the named hazard, and it was real.** Gain per attempt is `P(grant) × U`.
Each refusal deposits grievance and lowers the respondent's stance toward the petitioner, so `P(grant)`
falls geometrically on repetition while the exposure claims are durable and accumulate. **That is
exactly the shape Jordan condemned in the Comply/Defy fork, and left unfixed it makes petitioning
dominated by not petitioning.** The fix is structural, not a constant: refusal produces an **asset**.

```
value(attempt) = P(grant)·U  +  (1 − P(grant))·G
```

`G` is the grievance capital deposited in the backers — the input to commitment (§5.1), to carriage
mass (§7.1) and to the citable record (§6.1). As `P(grant)` decays the second term *rises*, in
proportion to how publicly the refusal happened, and the sum does not decay. A petition campaign that
never wins anything is building the thing that wins without petitioning, and a respondent who refuses
cheaply every time is manufacturing his own opposition.

**(c) Revolt versus petition.** The dominance hazard runs backwards here: if suppression's ratchet
makes each subsequent attempt easier, a patient faction should always wait rather than rise. Fixed
structurally — the ratchet operates on the **container**, while the persons who rise and lose are
removed, and their dormant rows pass to heirs and strangers. The payoff of your failed revolt accrues
to your children, and a person choosing to rise values that only through their stance toward their
hearth and toward the proposition. A genuine non-dominant choice, and the honest explanation of why
doomed risings happen.

**(d) Is DROP dominant?** It looks it. The counterweight is the carrier's **own shortfall**: standing
at a container is contested (substrate §4.1) and claimants' capacity routes through the persons who
back them, so a seatholder who carries nothing accumulates regard only with a judging set that already
likes him and acquires no new backing anywhere. A perpetual dropper ends as a man with a seat and no
constituency, and loses the seat at the next contest. The field that types his rise types his
vulnerability.

**(h) Suppress versus concede — the fork the ratchet could have broken.** Suppression's gain is
immediate and large and *decays* as rows re-arm; its cost is durable and compounds. Read naively that
is dominated, i.e. a mechanism engineered never to fire. It is not, because suppression correctly buys
**a window**, and its value depends on what the ruler does inside it: suppress-then-concede-structurally
clears the rows and is the strongest line available, while suppress-and-do-nothing is dominated and
should be. Concede is not dominant either — the settlement stake is zero-sum between the communities
inside it (substrate §4), so granting a COMMON proposition manufactures a fresh shortfall in whoever
the old terms favoured. Conceding to the hamlet produces the Row's petition.

**(i) Maximum mitigation against maximum accrual.** Required, because a mechanism tuned never to reach
its failure state is indistinguishable from one that does not exist. Run a ruler who suppresses every
event and concedes nothing for four generations: rows accrue and are inherited, re-arm thresholds fall,
and eventually every hearth holds an armed dormant row while `hold(n, ·)` has decayed because the watch
lives in the town. **Recoverable?** Yes, expensively, by exactly two routes — the satisfying
dispensation is available at *every* accrual level and clears every row referencing its proposition in
one stroke; and inheritance transmits at reduced magnitude, so a lineage's grievance decays
geometrically absent re-arm, which a reformed container does not supply. Maximum accrual is recoverable
by one costly structural act plus a generation of not re-offending. It is not recoverable cheaply, and
it is not recoverable at all by removing people.

---

## 10. One trace: three rungs, a named man dropping it

**Season 1.** Torvald Aske's hearth: four mouths, eleven weeks of grain, nineteen to harvest.
Need: *(the Goldenfurt granary opens at reckoning rate to hearths outside the wall, urgency 0.78)*.
Reach 0.31 — fishing covers five weeks, selling the boat covers fourteen and destroys next year, his
brother's larder is thinner. **Shortfall 0.47.** Respondent from a claim told him by Sister Marte Ohl:
the praefect opens the granary at the reckoning date. `gap = 3`, so: supplication, carried, through an
intercessor with gap ≤ 2. Marte's gap to Aldwin is 2. The legal route exists and it runs through her.

Torvald tells it at the well and at the chapel. 61 hearths hear it within the season; **44 back
publicly** — cheap, because their judging set is the hamlet and it agrees — and **9 back concealed**,
including Hedda Brann, journeyman Kettlemaker, whose Free Master candidacy sits before a committee
that reads exactly such claims. Public roll 44. Marte's private total 53.

**Rung 1 works.** Marte carries as supplication, correct form. Aldwin grants **partially**, by grace:
reckoning rate for six weeks to hearths of more than three mouths. PRIVATE-shaped, cheap, invisible.
Urgency falls 0.78 → 0.41, shortfall to 0.10. No grievance is deposited anywhere. Torvald's stance
toward Aldwin goes **up**. *The up-stroke must be able to succeed, or it is a grievance factory rather
than a political system.*

**Season 3.** Almud's Schoenland trade opening raises the reckoning rate. The six-week grace expires
with the season and Aldwin does not renew it; the granary is now contested by the Row's apprentices,
whose bread price rose. Torvald's shortfall returns at 0.63. Marte, who has learned, **bundles
generalizing**: four hamlet supplications plus the apprentices' bread-price ask, under
*"the granary prices grain at the reckoning rate to every hearth in the settlement's territory,
irrespective of wall."* Roll: **111 public** (44 hamlet + 67 apprentices), 14 concealed. The bundle
has crossed the caste line because the need was identical on both sides of the wall.

It is now COMMON. It cannot be granted by grace. It exceeds Aldwin's scope — the reckoning rate is set
at the territory court — so it must be carried up, and carrying needs a seat.

**Rung 2. The drop.** §4's table. Aldwin carries his son Ansgar's admission and drops the grain bundle
**silent**, because the sixty-seven apprentices are backing he may want and the forty-four are not. He
holds no claim that the hamlet can hurt him; the cell there is concealed. At the next sitting the
petition lapses.

**Rung 3. What does not travel.** Duke Magnus Vaynard, three rungs up, wants the caste order broken
and would have granted this on sight. He never hears of it. It died one rung below the man who wanted
it, and no one planned that.

**Season 4. The learning.** Hedda hears at the guild hall that the sitting heard no grain item —
firsthand, one root. She tells her brother-in-law; he tells Torvald. The third telling asserts that
Aldwin *traded* the grain for his son's place: true in effect, unwitnessed as a causal link,
amplification 1.4, confidence 0.7, source `told_by(Sigurd Aske)`, ancestry rooting in Hedda's single
firsthand. Told twelve more times, it still corroborates once.

Deposit: `Δstance(Torvald → Aldwin) = −(0.63 × 1.0 × 1.4) ≈ −0.88`;
`Δstance(Torvald → the praefecture) = −0.31`. The claim named a man, so the man takes most of it.
Twenty-nine of the forty-four public backers learn this season, each through their own channel, at
their own time, with their own distortion. Fifteen do not learn at all.

**Commitment.** Torvald has held the Restoration proposition as a claim since season 1 at confidence
0.4 and stance +1. It opposes the referent he now holds grievance toward, so it revalues: `commit`
0 → 2, sympathiser. No recruiter was present. Twenty-two others in the hamlet do the same over two
seasons, at different degrees, for individually computed reasons. True presence at the hamlet node:
31 of 240 — 12.9%. **Aldwin's estimated profile, rolled up from the memberships his own ledger names,
is 3 of 240 — 1.25%**, and the three are the ones who were loud. He is not underestimating a number he
can see. He is computing correctly over a ledger that is missing twenty-eight rows, and no
investigation will add them because he holds no claim prompting one.

**What happens.** Nothing fires. Torvald's cousin and four others force the granary's south door at
the reckoning date, because their ledgers say the watch will not stand — and they are two-thirds
right: Ivar Holt does not, four Crown watchmen do. They go to the granary keeper first. A Templar and
a neighbour witness the same minute and deposit different predicates.

**The political consequence.** The Löwenritter chapter is called; Grandmaster Sigrid Ehrenwall's order
is caste-open and its members' compliance computes differently than the Crown watch's, which is itself
a fact three factions will now argue about. The incident's claims reach Varfell. Duke Magnus hears —
for the first time, through a broken door rather than through a petition — the proposition he would
have granted in season 3, and issues a dispensation setting the reckoning rate for every hearth in the
territory.

Every dormant and active row referencing **that proposition** clears, everywhere, in one stroke.

Every row referencing **Aldwin Storr** remains, in forty-four stance tables, inherited, and untouchable
by any dispensation ever issued.

---

## 11. Note on the spine

**No challenge stands.** The spine's §1.3 was amended while this document was being written, and the
amendment answers the one objection I had drafted — that §5.1's *"until density crosses what the
coercive apparatus can hold"* reads threshold-shaped against §6's explicit refusal of a
grievance-to-revolt threshold. §1.3 now states the resolution directly: scale determines no option,
and outcomes still depend on how many people are really standing there.

I have built on that reading and made it sharper in §5.2–§5.3: the comparison is real and reads true
state, but it is evaluated **at resolution, by the function that already takes `world`**, and it may
never appear as a precondition on anybody's decision to rise. That keeps both halves — no threshold
causes a revolt, and a rising is still settled by who actually turned out. I use **presence** for
force throughout and reserve **density** for perception, and every profile a person reads is the
**estimated** one built from their own ledger, per the amended §1.3.

One clarification, not a disagreement: a person petitioning their own container carries it himself,
since he is a person at that container. §5.1's rule that a petition cannot enter a container by itself
is satisfied trivially at the first rung and only bites from the second rung up — which is where it
was always doing the work, and where §4's drop lives.
