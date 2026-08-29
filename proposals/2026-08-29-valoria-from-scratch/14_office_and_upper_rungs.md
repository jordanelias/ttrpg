# 14 — Office, and the Rungs Above Settlement

## Status: PROPOSED (2026-08-29) — a from-scratch design. Nothing here ratifies on merge.
## Lane: GO/IN · Composes on: `01_substrate.md` §2, §4, §5; `04_hearth_and_community.md` §1.3, §4.2, §6, §8; `07_alignment.md` §2, §4, §5.2
## Coordinates with: 05 (carriage, seats), 06 (publication, reach, treaties), 08 (what happens inside a venue)

**What this document owns.** The substrate names Settlement as the rung where **office** first exists —
*a post whose holder's decision binds persons who never agreed to it* — and then does not build it.
Nobody owns office as an object; nobody owns Territory, Province, Duchy or Realm; nobody owns the
Crown, the rooms arguments happen in, or what happens the morning after a praefect dies. That is this
document.

**The one claim everything else follows from.** An office adds **no verb to the game**. It supplies a
**remit**, which makes five ordinary acts *eligible* at nodes where they otherwise are not, and it
supplies an **establishment**, which is where the pool for those acts comes from. A Duke and a hamlet
fisher run the same `choose(person, view)` over the same act vocabulary. They differ in three
quantities and nothing else: **remit** (which acts exist for me here), **reach** (which nodes I have a
person at), and **binding** (whose options my decisions change). Everything below is those three
quantities carried up four rungs.

**Reading key**, inherited: every object is *producer → carrier → consumer* and carries an N-line.

---

## 1. Office as an object

```
Office := (post, node, remit, conferral, revocation, establishment, seat_items, upkeep)
remit  := (acts[], scope_node, binds)
binds  ∈ { members-by-admission, persons-by-presence }
Holding := (person, office, since, conferrer)          # an edge on the PERSON, like every faction edge
```

There is no office object holding a person. `Holding` lives on the person exactly as commitment edges
do, and "who holds the praefecture of Goldenfurt" is a query, not a field. Nothing anywhere stores
*control*.

### 1.1 The remit is what an office is

`remit.acts` is drawn from a closed set of **five**, and each one is an ordinary act the substrate
already has, made eligible somewhere it otherwise is not:

| remit act | what it actually is | already owned by |
|---|---|---|
| **issue** | `tell`, with terms — a Dispensation | substrate §5.2, doc 06 |
| **determine** | one person's decision at a venue whose `decide_rule` names him | doc 08 |
| **confer / revoke** | `admit()` and its negation, over an office rather than a community | doc 04 §4.2 |
| **dispatch** | `requisition` on a member of the establishment | doc 04 §1.4, doc 07 §1.2 |
| **convene** | setting a standing date, and ordering its items | substrate §5.3, doc 05 §3.1 |

`remit.binds` is the field that answers the substrate's "first office at Settlement." A guild warden's
decisions bind only persons who walked through the Masterpiece Examination — **members by admission**,
who consented at a gate. A praefect's decisions bind the Einhir hamlet outside the wall, which admitted
him to nothing — **persons by presence**. Settlement is where office *first* exists in the substrate's
sense because it is the first rung whose stake is zero-sum across communities that did not admit each
other, which is the first place `binds = persons-by-presence` is a coherent thing to want.

- **Closed loop.** Produced by a `confer` act naming a person; carried as a `Holding` edge on that
  person plus a `post:` mark with the conferrer as source; consumed by `eligible()` at every act, by
  every venue's decide rule, and by 06's compliance contest, which reads the issuer.
- **N-line.** Cut office and no decision reaches a person who did not agree to it. Every dispensation
  becomes a request, the strategic layer has no downward channel that is not consent, and the entire
  difference between a settlement and a large family disappears.

### 1.2 Office changes the option set and the pool source — never a modifier

A flat shift of size X on a pool roll is worth `X / (0.671·√Pool)` — doc 10 §6 owns the constant —
which means it helps a weak side
*more* than a strong one — backwards from what "a leader" is supposed to mean. So no office anywhere
adds a number to a roll. Two substitutions instead:

**Option set.** `eligible(p, act, n)` consults `remit`. Praefect Aldwin Storr can `issue` at Goldenfurt.
Torben the fisher cannot. Neither of them rolls differently for anything.

**Pool source.** When an act is performed **by remit**, the pool is drawn from the *establishment* — the
named persons the office employs — and not from the holder's own capability:

```
pool(act by remit) = capability of the dispatched establishment member(s) actually performing it
```

Duke Magnus Vaynard's Focus is irrelevant to whether the Grauwald levy is collected. The pool is the
reeve's, and the reeve is a person with a larder, a stance toward Vaynard, and kin in the hamlet he is
collecting from. **Choosing which of your people performs the act is the whole of a leader's tactical
choice**, and it is a choice between pools, not a purchase of a bonus.

### 1.3 What it costs to hold

Three costs, all in currencies that already exist.

1. **Seat items.** An office's standing dates consume the holder's own hours: `seat_items` is how many
   things he can hear or carry in a sitting (05 §3.1). Holding two offices does not double a day.
2. **Publicity, which is not optional.** Every act by remit is performed at `venue_factor ≥ 1.0`
   (04 §4.1), so an office-holder's judging set is the whole settlement and `mark_salience` is high.
   **An office-holder cannot act quietly.** This is the real price, and it is why Niflhel's recruiters
   hold no office and the Burned hold no post: a covert edge (07 §1.3) and a remit are close to
   incompatible.
3. **Upkeep.** The establishment eats. Its members' larders are filled from the office's stake — the
   tithe share, the levy, the gate's fees. An unpaid establishment is 07's military-basis cut fired
   against yourself: armed persons whose larders you stopped filling do not disperse, they become a
   faction and treat plunder as wages.

### 1.4 What it gives — licensed standing, which doc 07 needed and did not have

07 §5.2 computes `shadow(p,n) = standing(p,n) − licensed_standing(office(p,n))` and leaves the second
term undefined. It is defined here, and it is a partition of the support set rather than a new number:

```
S(p,n)  partitions into
  S_post   — persons whose contribution is compliance routed through the remit (the establishment,
             and everyone whose compliance reads "he holds the seal")
  S_regard — persons whose contribution is regard toward p personally

licensed_standing(p,n) = clamp₀₇ Σ_{q ∈ S_post}   contribution(q,p,n)
shadow(p,n)            = standing(p,n) − licensed_standing(p,n)
```

Two consequences worth the formula. A man with a large office and no personal following has
`shadow ≈ 0` and cannot survive losing the post. A man with a small office and a large following has
positive shadow, and 07's legalisation pressure fires: the person above him finds that writing down
what he already does is cheaper than fighting him. **Reeve to territory governor is that subtraction
crossing zero**, and nobody promoted anybody.

### 1.5 The post roster

| post | node | binds | conferred by | conferral basis (07 §4) | establishment | revocable by |
|---|---|---|---|---|---|---|
| **guild warden** (Kettlemakers) | community | members-by-admission | the Free Masters at a sitting | merit | the guild's beadles | the same sitting |
| **parish priest** | community | members-by-admission | a Cardinal, via benefice | patronage | none — he dispatches nobody | his Cardinal |
| **gate warden** (Ivar Holt) | settlement | persons-by-presence | the praefect | patronage | 2–5 watchmen | the praefect |
| **reeve** | settlement/territory | persons-by-presence | the territory office | patronage / purchased | collectors, a cart, a scale | his conferrer |
| **magistrate** | settlement | persons-by-presence | the settlement court's own sitting | merit | the court's bailiffs | that sitting |
| **praefect** (Aldwin Storr) | settlement | persons-by-presence | the Crown | patronage | the watch, the granary keeper | the Crown |
| **Canon** | province / cathedral | members-by-admission | a Cardinal | patronage + merit | registers, assessors | his Cardinal |
| **Cardinal** | realm-scope cluster root | members-by-admission | the Confessor | patronage | a Dicastery's whole graph | the Confessor, at a Dicastery venue |
| **Confessor** (Arne Himlensendt) | realm | members-by-admission | the Cardinals in conclave | merit / ideological | **none of his own** | conclave, contested |
| **Grandmaster** (Sigrid Ehrenwall) | realm-scope cluster root | members-by-admission | the chapters' sworn brothers | deed | every chapter's riders | a chapter sitting |
| **Duke** (Magnus Vaynard, Inge Baralta) | duchy | persons-by-presence | **nobody living** — deed at the Secession War | deed + kinship | household, provincial appointees | *not revocable* — only contested at a venue |
| **King** (Almud Almqvist) | realm | persons-by-presence | **nobody living** — deed, consecrated | deed + kinship | household, Crown praefects | *not revocable* — §6 |

Read the last two rows against the rest. Every post above them names a **living conferrer** who can
revoke it. The ducal and royal offices name a war whose witnesses are dying. That single column is §6.

---

## 2. Vacancy, succession, revocation

Doc 04 owns the *hearth's* seat: the succession pointer, the vacancy standing date, the three branches
of `contest`. Office succession is a different animal, because **an office is a stake of its container,
not of a hearth** — except where the conferral basis is kinship, in which case it is attached to the
hearth's seat and 04's machinery applies unchanged. That is the whole difference between an appointed
praefecture and a heritable duchy, and it is one field, not two systems.

### 2.1 What happens the moment an office empties

```
vacate(office, cause)   cause ∈ { death, revocation, resignation, incapacity, abandonment }
```

Nothing is written to the world. Four things become true by computation:

1. **Every standing dispensation the holder issued keeps its terms and loses its complier.** 06's
   compliance contest reads the local stance toward *the issuer*. The issuer is now a dead man toward
   whom nobody is forming a new stance. Compliance across the whole scope drops in the same tick, with
   no decree and no event. **The interregnum is abolished by arithmetic**, exactly as doc 04 found for
   hearth seats: a *normal* conferral hands the successor a stance inherited through the `post:` mark
   and the conferrer's name; a *contested* one leaves the stance column empty everywhere at once, which
   is precisely "every settlement's acceptance re-opens for renegotiation."
2. **`S_post` empties and `licensed_standing` goes to zero.** The establishment's compliance was
   routed through a remit that now has no holder. Their own needs and their own faction edges are what
   remain. This is the akıncı case in domestic miniature: the corps outlives the bey and stops being
   his.
3. **The office's seat items go unspent.** Goldenfurt's two seats at the Grauwald territory court
   become one. Every petition queued behind that seat waits a full standing date, and 05's grievance
   deposit fires on backers who were not refused — they were simply not heard.
4. **A conferral standing date opens** at the horizon the container carries (1 season for a wardenship,
   2 for a praefecture, 4 for a consecrated office, because a consecration needs a consecrator).

### 2.2 There is no interim, and no regent object

Between the vacancy and the date, the office has no holder and the remit is unexercised. What exists
instead is a computed fact:

```
exercise(o, claimant) = Σ_{n ∈ scope(o)} compliance_share(n, terms issued by claimant)
de_facto(o)           = argmax over claimants of exercise(o)      # may be nobody, and often is
```

And here is the part that needs no new machinery at all. **Nothing stops a man from sealing a paper
and having a crier read it.** That act is `tell`, which every person is eligible for, with
`as_asserted = "by remit of the praefecture"` while the speaker holds no such remit. The substrate
already calls that a **lie**, performed at a place, at a time, witnessable, traceable to a source row
in every hearer's ledger. Whether it *works* is 06's compliance contest, which does not check a
registry — it reads what people believe and what they think it costs them.

So the forged succession edict is not a mechanic. It is one lie plus one compliance contest, and if
uncontested it is deposited into every ledger as genuine until a contradicting claim arrives, and its
discovery flips legitimacy retroactively because the ledger row names its source. Prince Torben, if he
is ever moved from Alexios Laskaris's court in a Crown vacancy, will be moved by exactly this.

### 2.3 Conferral is `admit()` — reused, not reinvented

I reuse doc 04 §4.2's shape whole. Conferring an office is an admission act with the same four
coefficients and the same rule that **α, β, γ, δ are weights and never signs**:

```
support(m, candidate) = α·Σ_marks stance(m→referent) + β·performance + γ·Σ_sponsors + δ·stance(m→candidate)
```

with one placement difference I am flagging rather than hiding (§11): the vector is held at the
**conferring office**, not at the container, because a Cardinal confers a Canon at a cathedral he does
not live in and a King confers a praefect in a settlement he has never seen.

| conferral | committee | α | β | γ | δ | rule |
|---|---|---|---|---|---|---|
| praefecture, by the Crown | the King, or two of the inner circle | 0.8 | 2.0 | 2.0 | 0.5 | either term alone clears |
| benefice, by a Cardinal | the Cardinal alone | **1.5** | 0.5 | 1.0 | 0.3 | his determination |
| Löwenritter chapter master | three sworn brothers | 0.2 | **3.0** | 0.3 | 0.3 | any two of three |
| gate wardenship, by a praefect | the praefect alone | 0.5 | 1.0 | 0.5 | **1.5** | his determination |
| Confessor, in conclave | the four Cardinals | 1.0 | 1.0 | **2.0** | 1.0 | three of four |

Caste needs no rule here for the same reason it needed none at the guild: a single-assessor conferral
with α = 1.5 makes a Southern Einhir Canon **one man's attributable exception**, and an exception
attributable to a named man is the definition of a scandal.

### 2.4 Revocation, and revocation-in-fact

`revoke(r, office, holder)` requires that `office` lie in `r`'s **conferral subtree**. The conferral
relation is a *graph*, not the containment tree, and this is the single most load-bearing structural
fact in the document: a Duke cannot revoke a benefice, a Cardinal cannot revoke a gate wardenship, and
the King cannot revoke a duchy. Revocation is contestable at a venue (§5), and a revocation the loser
refuses to comply with is 04's third branch: held by whoever physically holds it, re-opening at every
standing date.

There is also **revocation in fact**, which nobody performs. An office whose `exercise` is zero across
its whole scope for two standing dates is vacant in the only sense that matters, and the world will
have noticed before any venue has.

- **N-line (all of §2).** Cut office vacancy and a death is a name change. You lose the window where a
  lie about who you are is worth telling, the collapse of compliance that makes a succession dangerous
  rather than administrative, and any reason at all to care who dies.

---

## 3. Territory, Province, Duchy, Realm

A rung is a role, not a class. So each rung above Settlement must own a mechanism the rung below does
not — otherwise it is a filing level and should be cut.

### 3.1 Territory owns reach, and reach is a fidelity property of a view

Settlement office acts **where the holder stands**. Territory office acts **where it sends someone**.
That is the whole distinction, and it makes the Territory's stake a roster of persons rather than a
thing in a place.

```
establishment(o) = the named persons the office employs
reached(o, n, season) ⟸ a dispatched member of establishment(o) is present at n this season
                       ∨ a relay hop terminates at n through an institution with presence there
```

Reach is a count of persons and channels. **There is no distance term anywhere.** Grauwald's outer
hamlets are unreached not because they are far but because Vaynard does not have thirty-five riders.

Now the part I think is the best idea in this document, because it makes the Territory Reach Cap stop
being a rule. **A node nobody reports from produces no firsthand claims in the office-holder's ledger.**
Substrate §2: persons who share an address, marks and stance are held as a **cohort**, and a cohort
individuates when an event names one of them. So a settlement with no dispatched person, no relay, and
no petitioner who got through is *literally a cohort in the Duke's view* — one row, coarse, stale,
carrying nobody's name.

> **The aggregate is not a modelling shortcut for the governor. It is what his ledger contains.**

Past the reach cap, the territory genuinely *is* an aggregate to him, and it stops being one the moment
he sends a man or a petitioner arrives. Fidelity is bought with establishment, one node at a time, and
the same mechanism that keeps the population model cheap is the mechanism that models an administrator's
blindness. This is also the honest answer to the appointed-governor problem that three implementations
in twenty years could not settle: the governor is not a feature to toggle. He is what you buy when your
ledger has gone coarse.

- **Closed loop.** Produced by `dispatch` and by relay hops with institutional presence; carried as
  firsthand claims deposited into the office-holder's ledger by the dispatched person's tellings;
  consumed by the holder's own `choose(person, view)` — which now sees names instead of a cohort — and
  by 06's `enforcer_presence` term.
- **N-line.** Cut reach-as-persons and a Duke governs thirty-five settlements as easily as one, the
  periphery stops being peripheral, and the caste geography of the western fjords becomes decorative.

### 3.2 Province and Duchy are the same rung with one field different

Both are **delegation rungs**. A delegation rung exists so that an office may carve a **sub-remit** — a
proper subset of its acts over a proper subset of its scope — and confer it, with the sub-holder
binding by the parent office's authority.

```
subremit(parent, acts' ⊆ acts, scope' ⊆ scope) -> a new Office whose conferrer is parent
```

Delegation buys reach and manufactures shadow standing in the same act: the sub-holder's `S_post` is
his own, so his establishment's compliance reads *him*, not you.

The one field that differs:

| | **Province** | **Duchy** |
|---|---|---|
| conferral basis | patronage / merit — **appointed** | kinship + deed — **attached to a hearth seat** |
| vacancy resolves by | a conferral standing date at the parent office | doc 04's succession pointer and `contest` |
| revocable by the parent | **yes** | **no — the parent did not confer it** |
| exists when | the parent's establishment cannot reach the children directly | always; a hearth does not dissolve when reach improves |

That last row is why the setting has three duchies and fourteen provinces that canon itself calls
conditional and emergent. **A province is instantiated when reach fails and dissolved when reach
recovers**, because it is nothing but a carved remit, and a carved remit that is no longer needed is
revoked by the office that carved it. A duchy cannot be dissolved that way because there is no living
conferrer to revoke it, and its holder's hearth would still be there.

- **N-line.** Cut delegation and the reach cap has no counter-move, so the upper rungs are a hard
  ceiling instead of a fork. Cut the appointed/heritable distinction and either every governorship is
  a dynasty or the Crown can fire a Duke, and both delete the game's central asymmetry.

### 3.3 Realm owns the root of the conferral graph, and therefore owns nothing

The Realm rung's distinctive property is a lack. Every office in the world names a conferrer; the
conferral graph must terminate; and at the root there is an office **whose own remit no one inside the
world conferred**. That office therefore requires an *external warrant*, and in Valoria the external
warrant is Church consecration — an instrument in somebody else's custody.

The Realm also owns the **general-scope dispensation**: an instrument whose scope is the root node,
exercisable only by an office whose remit covers it. And the irony is arithmetic rather than authored:
the largest remit in the peninsula has the thinnest reach per node, because the establishment is finite
and the scope is 35 settlements plus Himmelenger and Schoenland. **A King's decree is the least enforced
instrument in the game.**

---

## 4. The two container axes

Two objects, orthogonal, and neither is a new tier.

|  | **Territory** (containment) | **Office cluster** (alignment + conferral) |
|---|---|---|
| what it is | a containment node; a place-cluster held as one aggregate | a set of offices at many nodes whose conferral paths share a root |
| membership | persons, by address | **none.** It has offices and holders, not members |
| reach | the establishment of the office at that node | the union of its offices' establishments and channels |
| distinctive power | binds persons by presence | the root can `revoke` down the whole graph — a power no container has |
| distinctive vulnerability | its stake can be physically taken | 07's patronage cut: remove the root and every conditioned contribution voids, fanning out per 06 §6 |

```
OfficeCluster(root) = { o : conferral_path(o) reaches root }        # a query, never a stored set
```

**The sanjak and the akıncı, on the same ground.** The bey is an office at a Territory node, binding by
presence, with an establishment of his own. The corps is an office cluster whose conferral root sits
elsewhere entirely and whose establishment is armed persons. The corps starts an international incident
the bey never ordered, and three existing mechanisms produce it with nothing added: (a) capacity is an
existential over persons (07 §2), and the corps' persons are not in the bey's establishment, so his
`requires` predicate cannot reach them; (b) their compliance reads their stance toward *their*
conferrer; (c) foreign witnesses attach an attribution claim naming the realm, and attribution is a
separate contestable assertion. The bey is answerable for an act he had no capacity to prevent.

Valoria's clusters: the four **Dicasteries** (roots: four Cardinals); the **Löwenritter** (root:
Grandmaster Sigrid Ehrenwall, warrant from Crown-as-institution rather than from the King personally,
which is why she may lawfully refuse him); a guild present in Goldenfurt, Stillhelm and Oastad (root:
the mother chapter's warden); **Niflhel**, whose conferral graph is itself concealed, so that
discovering *who appointed whom* is the investigation that unmakes it.

And the jurisdictional politics falls out for free: a cluster office sitting at a containment node whose
own office-holder did not confer it is exactly 08's stasis rung 4 — *this chamber may not hear it*.
Nobody wrote a jurisdiction system.

- **N-line.** Cut the office cluster and the Church, the Löwenritter and every trans-settlement guild
  must either become a second containment tree — which single-parent containment forbids — or dissolve
  into a faction with no internal structure, which deletes benefices, chapters, and the possibility of
  an institution acting where its faction is not.

---

## 5. Venues — the three gates

Doc 08 owns what happens inside the room and already defines
`Venue = (container, prize, standing_date, judging_set_rule, decision_rule, admission_floor,
privileged_custody, exchange_budget, article_count, coupling_depth, veto_holders, record_custody)`.
I adopt that tuple whole and add the door, which it assumes and does not state:

```
+ (convener, enter, speak, admissible_source, attendance_cost)
enter / speak : predicates over (marks, office held, standing at container, commitment degree)
```

**I am deliberately not reusing doc 04's coefficient vector here, and the reason is a design claim:** a
door is a predicate and a verdict is a weighting. 04's `support()` is right for conferral (§2.3) because
a committee weighs a candidate. A venue's entry rule is boolean — you are inside or you are not — and
08 already owns the weighing that happens after.

| venue | convener | ENTER | SPEAK | DECIDE | admissible source | standing dates |
|---|---|---|---|---|---|---|
| **Hafenmark Court Parliament** | Duchess Inge Baralta | seat-holders + their attendants | seat-holders only | majority of seats | instruments and sworn testimony | quarterly; extraordinary on a Crown vacancy |
| **Goldenfurt settlement court** | Praefect Aldwin Storr | anyone present | office-holders, and any person **carrying** a petition | the praefect determines; assessors' stances weight it | firsthand, plus oath-helping | the levy day, the tithe reckoning |
| **Dicastery of Doctrinal Adjudication** | its Cardinal | clerics in orders | Canons and assessors | the Cardinal; the Confessor holds a veto | its own registers only | the visitation |
| **Dicastery of the Defense of the Faith** | its Cardinal | the accused, if summoned | the assessor and the accuser | the Cardinal | firsthand testimony and confession | on summons, unscheduled |
| **Dicastery of Temporal Affairs** | its Cardinal | benefice-holders and Crown envoys | the same | the Cardinal | account rolls | the tithe reckoning |
| **Dicastery of Doctrine and Archives** | its Cardinal | anyone with a register petition | Canons | the Cardinal | **instruments only** | on demand |
| **Masterpiece Examination** | the guild warden | the Row | Free Masters — and **common voice on the candidate's fitness** | majority | the work itself, plus common voice | the examination |
| **Löwenritter chapter sitting** | the chapter master | sworn brothers | sworn brothers | any two of three who witnessed | **witnessed deed only** | the chapter's sitting |
| **the Crown's council** | King Almud Almqvist | those the King summons | those the King names | the King determines | whatever he will hear | at the King's convening |

Three things this table is for.

**Exclusion in Valoria is at the second gate, not the first.** A Southern Einhir fisher may walk into
the Goldenfurt court. He may not speak unless a person with standing **carries** his petition (05 §3.1).
Caste is not a locked door; it is a room you may stand in silently. That is a far more accurate and far
more playable shape than a ban, and it is one column.

**The convener holds the cheapest real power in the game.** Setting a standing date and ordering its
items is `convene`, and a convener who puts three items ahead of yours has spent nothing and killed
your petition, because seat capacity is finite. Influence measured in volume of things filtered, held
by a person with no binding power at all — which is why the guild warden and the Dicastery's clerk
matter more than their remits suggest.

**`admissible_source` is a door for evidence, not a grade.** 08 owns grading. A venue that hears
instruments only cannot be reached by forty hamlet witnesses, however good their testimony; the chapter
sitting that hears witnessed deed only cannot be reached by a document, which is why the Löwenritter is
caste-open in fact and not by policy.

- **N-line.** Cut the venue parameterisation and either every argument happens in the same room — which
  deletes jurisdiction, forum-shopping, and the whole reason to challenge a venue — or every institution
  needs its own hand-written procedure, which is six special cases.

---

## 6. The Crown, and why it is weak

Valoria is a **deed-monarchy**. The first Almqvist earned the throne by Secession War command with no
blood claim; Altonia destroyed the records, so ancient-blood claims bottom out at no grade for
*everyone*; the ducal houses are cadet and deed families. Doc 04 §3.4 derives the consequence: the deed
presumption's weight is proportional to **living firsthand witnesses**, so it decays every season as
veterans die and cannot be renewed, because you cannot manufacture a firsthand root for a finished war.

Carried up to the office layer, that yields four statements, all computed.

**What the Crown actually controls.** Its own household establishment; the conferral of **appointed**
offices — praefectures, provincial governorships, its own reeves; the realm's standing dates; and the
general-scope dispensation with the thinnest reach in the game.

**What it must ask for.** Levies, because the territories' stakes are held by ducal offices the Crown
did not confer. Consecration, because the root office's warrant is external and sits in Church custody.
Hafenmark, because that Parliament's decision rule is a majority of seats and the Crown holds none of
them. Soldiers, because the Löwenritter's conferral root is Sigrid Ehrenwall and its oath is to
Crown-as-institution — an office cluster the King may petition and may not command.

**Why it is weak, in one line.** *A Crown that conferred few offices can revoke few offices.* The
patronage cut — 07's cheapest and most decisive instrument — is unavailable to the King against exactly
the persons who matter, because their conferral source names a war rather than a king. Everything below
the ducal line he can dismiss with a sentence; the ducal line he can only take to a venue.

**Peninsular Sovereignty is a fraction, not a flag.**

```
sovereign_fraction(root) = |offices in scope whose conferral path reaches root| / |offices in scope|
```

Nothing stores it. It is a query over a graph that exists anyway, and it is currently low: four
Dicastery clusters root at Cardinals, the Löwenritter roots at its Grandmaster, guild wardenships root
at their own chapters, Himmelenger's offices root wholly in the Church, and Schoenland's root outside
the peninsula entirely. Raising it is an act — converting one office's conferral root, at a venue,
against a holder who will contest it — and every faction's stated goal is a different operation on the
same fraction:

| faction | operation on the fraction |
|---|---|
| **Crown** — Peninsular Sovereignty | raise the numerator: convert conferral roots to itself, one office at a time |
| **Church** — Solmundan Orthodoxy | raise the numerator **for the Confessor's root** — the same operation, a different root |
| **Hafenmark / Baralta** — Dynastic Assertion | replace the person at the root and keep the graph |
| **Varfell / Vaynard** — Path B | delete a whole cluster from the scope: expel the Church's offices, shrinking the denominator and the numerator together |
| **Restoration Movement** — Communal Sovereignty | shrink the denominator to nothing: dissolve offices with binding power so that no root can hold them. Rejecting formal sovereignty is not a flavour of ideology; it is the only operation available to a faction with no Mandate, no wealth and no soldiers |

One ratified victory condition, five genuinely different operations, no victory-point counter anywhere.

- **N-line.** Cut the deed-monarchy's decaying warrant and the Crown is either legitimate forever or
  illegitimate from the start; the Baralta Crown Claim has no *timing*, and a succession contest becomes
  a fight rather than a clock nobody can stop.

---

## 7. The Church across rungs, without a second tree

This is the sharpest test of the architecture, because the Church reaches from the Realm rung to a
hamlet chapel and must do it without being a containment tree. Three different objects wear the name:

| the fiction says | the engine holds |
|---|---|
| the Church of Solmund | a **faction** — a proposition plus commitment edges on persons |
| a parish | a **community** — a containment node with an admission gate and a judging set |
| a Dicastery | an **office cluster** — offices at many nodes rooted at one Cardinal |

Confessor Arne Himlensendt sits at the root of all four clusters and holds **no establishment of his
own**. He binds nobody by presence. His entire power is conferral plus a veto at one venue — which is
exactly why "sincerely devout and completely wrong" is structurally dangerous rather than merely sad:
he cannot enforce anything and he can confer everything.

A parish priest is one man in three relations at once, and this is the demonstration that no second tree
is needed: he **holds an office** in the Dicastery of Temporal Affairs' cluster (his benefice, conferred
by a Cardinal, revocable by that Cardinal), he is a **member of the Church faction** at some degree, and
he sits in the **judging set of the parish community** every week. Three relations, one person, one
containment tree.

**The unwitting suppression, and what this document adds to it.** 07 §7 owns the mechanism: catechesis is
an ordinary `tell` depositing an early, general, high-confidence explanation into a child's ledger,
which resolves an unbounded family of anomalies in advance, and Thread Sensitivity grows from
*unresolved* anomalous witnessing. My contribution is one sentence about the delivery network:

> **The catechesis is performed by whoever holds the benefice. Parish density is the leaf count of the
> Dicastery's conferral graph. And no office in that graph has a remit that mentions Thread
> Sensitivity — the remit says catechise, bury, register.**

So the harm is a function of the **act the remit requires**, not of the remit's purpose, and it scales
with an establishment count that the Church tracks for entirely fiscal reasons. Southern Einhir
territories have lower Church penetration, which is fewer filled benefices, which is fewer early general
explanations, which is exactly canon's map of higher sensitivity in Grauwald, Stillhelm, Oastad and the
western fjords — as the model's *output*. And it runs backwards: if Duke Vaynard's Path B expels the
Church's residue from Varfell, benefices go unfilled, and TS emergence there rises over a generation.
He did not intend that either, and neither did the Cardinal whose graph he pruned.

---

## 8. What an office-holder does each season

The act vocabulary is identical at every rung. Here it is, once, with the only three columns that
differ:

| act | Torben, fisher, Einhir hamlet | Duke Magnus Vaynard, Varfell |
|---|---|---|
| `tell` / `lie` | to his cousin, over a boat | to the Court Parliament, at publicity 2.0 |
| `carry` a petition | into his own hamlet's elders' sitting, free | into the Realm's standing date, one of his four seat items |
| `drop` / `amend` / `bundle` | he holds no seat; he cannot | four times a sitting, and each one deposits grievance with a name on it |
| `commit` to a faction | at degree 1, covertly | at degree 4, and it is witnessed by everyone |
| `requisition` | his brother, claim weight 2.0 | **`dispatch`** — the same call, on an establishment member |
| `admit` | he sits on no committee | **`confer`** — the same call, over an office |
| `issue` | not eligible: no remit | eligible over Varfell, subject to reach |
| `determine` | not eligible | at any venue whose decide rule names him |
| `convene` | he can call his kin to a table | he sets the province's standing dates and orders their items |
| take an opening | run salt | reallocate a province's establishment |

**A worked season — Vaynard, one turn, ten acts, no faction verbs.** He `convene`s the Grauwald
territory court and puts the levy ahead of the hamlet's grain petition (killing it with seat capacity
rather than a refusal). He `issue`s a levy dispensation over five territories; his establishment is
nine, so four settlements get publication without enforcement and 06's compliance craters there
structurally. He `dispatch`es two riders to the two settlements he actually cares about — which also
buys him **fidelity**, because those two stop being cohorts in his ledger. He `confer`s a provincial
sub-remit on a capable Southern Einhir reeve, which is Path B expressed as an appointment rather than a
speech, and which raises that man's shadow standing from the day it is signed. He `revoke`s a benefice
he cannot revoke — the conferral path runs to a Cardinal, not to him — so the act is instead a `tell`
asserting a remit he lacks, and the parish's compliance decides whether it was a decree or a crime.
He `carr`ies one bundled petition into the Realm's standing date. He `commit`s at degree 4 to
*(the caste order ought to be broken)*, avowedly, at publicity 2.0, and pays for it in every Crown-Latinate
quarter's judging set at once.

Every one of those is a call the fisher can make or a call whose only difference is a remit and a
roster.

---

## 9. R-criterion check

Every fork below is checked for **shape of gain against shape of cost over time**. Decaying gain against
compounding cost is structural dominance and a design failure.

**Enforce or tolerate.** *Enforce:* gain is compliance at that node this season — real, but it **decays**,
because an enforced levy resets arrears once and the grievance it deposits goes dormant and re-arms at a
lower trigger. Cost is one establishment member consumed for the season — which **compounds**, because
the node you did not reach this season is coarser in your ledger next season. *Tolerate:* gain is the
establishment member spent somewhere that mattered — **compounding**, because fidelity accumulates.
Cost is arrears compounding toward the next standing date, plus the inference every witness draws that
terms are not enforced here — which is 07's general-explanation mechanism running *against* the office.
Both arms compound on both sides. Neither dominates; the crossing point is how contested the node is.

**Appoint the capable or the loyal.** *Capable:* gain compounds — he does the job, and his `act_reach`
raises your capacity in every contest at his node. Cost compounds — his shadow standing rises, and 07's
legalisation pressure means the cheapest thing you can eventually do is write down what he already
does. *Loyal:* gain is compliance certainty, and it **decays**, because loyalty is regard and regard is
spent by every ask. Cost is low capacity, so you must dispatch more establishment, and the reach cap
bites. Both arms have a real failure mode; the fork is between *a rival you built* and *a cap you hit*.

**Centralise or delegate.** *Centralise:* gain is `sovereign_fraction` rising and offices you can
actually revoke — compounding. Cost is seat items and reach, both hard-capped and both worsening with
every node added — compounding faster. *Delegate:* gain is reach, compounding with node count. Cost is
sub-remits whose holders build their own `S_post` and their own conferral subtrees, so that on your
death each of them keeps their standing and becomes a root. Neither arm is free; the empire that
delegated fragments and the empire that did not never reached its edges.

**Spend the deed presumption or hoard it.** This is the one that looks broken and is not. *Hoarding*
has **zero cost and a gain that decays to zero with certainty**, because the numerator is living
witnesses and they are dying. That is not a dominant option — it is a guaranteed total loss.
*Spending* uses the presumption as an `authority-said` warrant at a venue, and converts a decaying
asset into a permanent one if it carries: a record row, citable forever as `same-as-precedent`. If it
is rebutted, it converts into a permanent liability that every future opponent can cite, and it costs
a seat item and raises 08's pattern counter. So the fork is a genuine timing problem — spend while the
witnesses live and the venue is favourable — and it explains Duchess Inge Baralta's entire strategy
without her needing a plan: she does not need a new claim, she needs the last men who saw the Secession
War to die.

**The refusal, honoured explicitly: maximum mitigation against maximum accrual.** A mechanism tuned
never to reach its failure state is indistinguishable from one that does not exist; its mirror bleeds
regardless of play. Run both ends on the reach cap. *Maximum accrual:* Varfell, twelve settlements, a
ducal household of nine dispatchable persons, a coastal blockade requiring Cordon-Complete across four
ports, and a contested succession. *Maximum mitigation:* delegate five territory sub-remits with three
dispatchable persons each (15 + 9 = 24 > 12), use Löwenritter relays to reset distortion at every node
with a chapter, and appoint capable men everywhere. Coverage is achieved. **And the cap has fired
anyway, in a different currency**: five men now hold establishments whose compliance reads *them*, the
duke's own `licensed_standing` at those nodes has fallen, and an order against any of the five returns
an empty existential. Meanwhile a praefect governing one settlement never touches the cap at all.
Reachable failure state, reachable safe state, and a mitigation curve whose top produces the next
problem rather than a flat line. That is the test passed in both directions.

---

## 10. What this document refuses

- **A regent, an interim, or a caretaker object.** `de_facto` is an argmax over compliance, and the
  vacancy window's characteristic act is a lie about who you are — which the substrate already has.
- **A legitimacy, authority, or mandate meter.** Legitimacy is the compliance term reading the issuer,
  plus a deed presumption whose numerator is living witnesses. A meter would have no holder of an
  opinion and could not be argued with at a venue.
- **A control or ownership field on any container.** Offices are held by persons; stakes have
  claimants; the word *control* names no state.
- **An office rank ladder.** One shared rank space, `standing(p,n) ∈ 0..7`, partitioned into licensed
  and shadow. A second ladder is a second seat-space.
- **An office XP, competence or administration stat.** Competence is the establishment's capability,
  which is persons. An office stat would be a leader bonus with a different name.
- **A hierarchy of command as a tree.** Conferral is a **graph**, and the fact that it is not the
  containment tree is what produces jurisdiction, the akıncı case, and the Crown's weakness.
- **An automatic succession for office.** Vacancy opens a conferral date; a conferral is `admit()`; a
  contested one is 04's third branch. Automatic resolution deletes the only interesting case, exactly
  as an automatically-binding treaty does.
- **A per-faction verb at the strategic layer.** There is no menu of domain actions. There are five
  remit-eligible acts, all of which are ordinary person acts, and a faction has no verbs of its own.

---

## 11. CHALLENGE — where I have strained the substrate and the two binding lanes

1. **The substrate says office first exists at Settlement; I have made office a general object with a
   `binds` field, which places guild wardens and benefices at the Community rung.** I believe this is a
   refinement rather than a divergence — the substrate's claim is true of `binds = persons-by-presence`,
   which is what makes a praefect different in kind from a guild warden. If it is rejected and office is
   held to begin strictly at Settlement, then the guild warden and the parish priest become *conveners*
   with agenda power and no remit, which I can write, but the Church then has no office below the
   cathedral and §7's demonstration loses its best case.

2. **I hold the conferral coefficient vector at the conferring office, not at the container — which
   diverges from doc 04's placement of the admission vector at the community.** The reason is that a
   Cardinal confers a Canon at a cathedral he does not live in. 04 flagged the same question in its own
   challenge and offered the office as its fallback; I have taken the fallback for conferral only and
   left 04's community placement untouched for admission. If both must sit in the same place, one of the
   two cases breaks and it should be decided once rather than twice.

3. **Doc 07 §5.2 uses `licensed_standing(office(p,n))` and does not define it. I have defined it** as a
   partition of the support set into post-routed and regard-routed contributions. This is a supply, not
   a disagreement, but 07's `shadow` now depends on a definition written in another lane and should be
   read together with it.

4. **Doc 08 already defines `Venue` and I have extended its tuple rather than written my own.** The
   three added fields — `enter`, `speak`, `admissible_source` — are the door; 08 owns the room. If 08
   would rather own the door too, delete §5's tuple extension and keep only the table and the convener's
   agenda power, which is the part that is genuinely mine.

5. **The substrate's ladder is Settlement → Territory → Province → Realm; the architecture note's is
   Settlement → Territory → Duchy → Realm. Neither has both.** I have resolved it by taking the
   substrate at its word that a rung is a role rather than a class: Province and Duchy are the same
   delegation role differing in one field (appointed versus heritable), which is why canon has three
   fixed duchies and fourteen conditional provinces. If the ladder is meant to be a fixed list, this
   section is wrong and the setting's own "conditional/emergent" province note has no mechanism.

6. **One thing I could not close.** An office held by a cohort is meaningless, so `confer` must
   individuate. The substrate's persistence rule already says a person holding an office does not
   re-merge, so the two agree — but a cohort that is *conferred* an office (a village that appoints "its
   elders" with no named person) has no mechanism here, and I have simply required that conferral names
   a person. I think that is right and I cannot derive it from the spine.
