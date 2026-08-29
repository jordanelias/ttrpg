# 07 — Alignment: Factions That Scale Continuously

## Status: PROPOSED (2026-08-29) — a from-scratch design. Nothing here ratifies on merge.
## Lane: FA (alignment) · Composes on: `01_substrate.md` §1.2, §1.3, §1.4, §2, §3, §4.1
## Method: derived from Jordan's A-2/A-4 and the substrate's two relations. No prior faction document constrains it.

**The single structural idea of this lane.** A faction is a *proposition* plus a *map from persons
to a degree of commitment*, and that is the whole object — there is no tier, no level, no size class,
no scale field, and no verb. Everything a faction appears to do is a person doing it and saying who
for. Everything a faction appears to *be* — national, local, dangerous, spent — is recomputed from
the commitment map by observers who may be wrong about it. Growth and collapse are the same
operation, `commit(person, faction, Δdegree)`, run with different signs, and the reason a faction can
grow from two brothers to a realm-scale body without an authoring act is that **there is no size at
which any reader of the object changes what it reads.**

The prior failure this lane exists to escape made faction a *tier*. A tier has boundaries; a boundary
needs a crossing act; a crossing act has to be authored; and once one is authored, the world can only
contain the factions somebody wrote. Here the world contains every faction any two people have ever
sworn anything about, most of them tiny, most of them never noticed, and the interesting ones are
interesting because of *where their members stand*, never because of how many there are.

---

## 1. The faction object, completely

```
Faction  := Proposition                                  # the identity. nothing else identifies it.
Edge     := (person, faction, degree, avowal, since, cause)
```

There is no member list held on the faction. Edges live on persons, exactly like every other thing a
person carries, and the "membership" of a faction is a query over persons — which is what makes the
object cheap enough to have ten thousand of them.

### 1.1 The proposition — the same object an argument can attack

A proposition is a claim tuple in the **deontic mood**. The substrate's memory rows are
`(subject, predicate, value, when, source, confidence)` in the indicative — *the granary is full*. A
proposition is `(subject, predicate, value, when, mood)` with `mood ∈ {is, ought, will}`, and a
faction's identity is a proposition in `ought`:

| faction | proposition |
|---|---|
| Halvar and Odd Uln, sworn over their sister's refused Masterpiece | *(Reeve Bertold of Grauwald, answers-for, the Uln barn, before next levy day, **ought**)* |
| The Kettlemakers of Goldenfurt | *(the Free Master gate, admits, only examined hands, all-time, **ought**)* |
| The Church of Solmund | *(the peninsula, holds, Solmundan Orthodoxy, all-time, **ought**)* |
| The Dicastery for the Defense of the Faith | *(heterodox practice, is-suppressed-by, force where persuasion fails, all-time, **ought**)* |
| The Restoration Movement | *(Einhir communities, govern, themselves by consensus, all-time, **ought**)* |
| The Baralta Crown Claim | *(Inge Baralta, holds, the Valorian throne, on the next vacancy, **will**)* |

This matters for exactly one reason and it is the reason the whole lane holds together: **an argument
attacks a proposition, and a faction *is* a proposition, so attacking a faction and attacking a claim
are the same operation with the same moves.** The fallback ladder — deny the act, deny the label,
admit and justify, challenge the venue — runs against *(Bertold answers-for the barn)* exactly as it
runs against *(the granary is full)*. Nothing in this lane needs an argument subsystem written for
factions; it needs the argument lane to accept a mood field, and this document is the request.

Because identity is the proposition, **there is no found-a-faction operation.** Two persons in Oastad
who independently hold a strong stance toward *(Einhir communities govern themselves by consensus)*
are not yet a faction — a stance is not a commitment. The faction begins when one of them performs
`commit` for the first time: takes an oath, hides a cell courier, hands over grain. That is one
person's act, at a place, at a time, witnessable. This is the whole of "the Restoration Movement can
emerge spontaneously from territorial neglect": repeated dropped petitions write grievance stances
toward the container into hundreds of ledgers; the stances converge on one proposition because the
proposition is the obvious negation of the thing that was refused; and then somebody acts.

- **Closed loop.** Produced by grievance and by tellings that name the proposition; carried as a
  stance-table referent on each person and as the identity of any edges pointing at it; consumed by
  the argument system, by requisition, and by every profile roll-up.
- **N-line.** Cut the proposition and a faction becomes a bag of names — nothing to argue against,
  nothing to schism over, and no way for two strangers to discover they are already on the same side.

### 1.2 The commitment degree, and what each degree licenses

| d | name | weight `w(d)` | what it licenses (and nothing beyond) |
|---|---|---|---|
| 0 | none | 0 | — (an edge at 0 is a deleted edge; departure needs no operation) |
| 1 | sympathy | 0.15 | will not testify against a member; may be told cell-safe claims; stance weight toward the proposition applies at view assembly |
| 2 | sympathiser | 0.40 | may be asked for material, shelter, or carriage at low cost; may `carry` a petition whose proposition is the faction's |
| 3 | member | 1.00 | may be *requisitioned* for acts inside their ordinary capability; may `avow`; counts in the faction's judging weight |
| 4 | sworn | 1.60 | may be requisitioned for acts **against their own container's interest**; refusal is witnessed by every d≥3 member and costs regard with all of them |
| 5 | constitutive | 2.20 | the proposition occupies a Conviction-primary slot; no regard offer and no material offer enters the refusal check at all; refusal is a Coherence event |

Degree 5 is where the refusal *"relationship modifiers large enough to dissolve structural conflict"*
is paid for. A rival cannot buy Odd Uln off his oath, because at d=5 the offer term is not in the
formula. That is not a big number resisting a big number; it is a term that is absent.

**Requisition** is the only channel from a faction to an act, and it is an ask between two persons:

```
requisition(asker, member, act, node)
  obstacle = base(act) + burden(member, act) − 2·w(d) − regard(member→asker)/2 − conviction_bonus
  burden   = cost to the member's own computed need
           + 2 · (harm to the member's container's stake)
           + 3 · (marks the act collides with)
```

Refuse with low burden and the edge loses a degree; refuse with high burden and it does not — a
faction that asks the impossible loses nobody, and a faction that asks the trivial and is refused
learns something true. `conviction_bonus` is the substrate's Momentum term: acting on a
Conviction-primary is what Momentum is for, so a d=5 requisition is the cheapest ask in the game and
also the one that spends a person's whole position.

- **Closed loop.** Produced by `commit` acts (oath, shelter, payment, betrayal); carried as edges on
  persons; consumed by requisition, by capacity, by the profile roll-up, and by the judging sets that
  punish or reward discovered membership.
- **N-line.** Cut the degree and every member is either in or out, so a Restoration sympathiser who
  slips bread cannot exist, informers cannot be recruited from the shallow end, and a faction cannot
  be *hollowed* — only shattered.

### 1.3 Secrecy is not a property of the secret

Each edge carries `avowal ∈ {avowed, private, covert}`.

- **Avowed** — an act was performed that deposits the claim `(person, member-of, faction, …)` into
  the judging set of the person's community by the ordinary witnessing path.
- **Private** — no public claim exists. Discoverable by anyone who witnesses a requisition being
  honoured, or who is told.
- **Covert** — members additionally perform concealment acts, and may `tell` a *cover claim*: an
  assertion of a different edge, or of none. Niflhel's dockworkers and the Burned run every edge
  covert by construction, and Niflhel is caste-open *because* covert work at the Baralta waterfront
  requires Southern Einhir members whose marks let them stand there unremarked — the caste-openness
  is a consequence of the operational requirement, not a policy.

There is **no "known %" on a membership**, because there is no knower on such a number. Who knows is
a row in a knower's ledger, discovered by the ordinary investigation path: an investigator
accumulates claims about a person's acts and deposits an *inference* claim about the edge, whose
confidence comes from corroboration — and corroboration fails closed, so one rumour retold three
times through Riverside supports the inference exactly once.

**Exposure is derived, never stored:**

```
exposure(edge) = Σ over persons q holding a claim about the edge of
                 confidence(q's claim) · hostility(q → faction's proposition)
```

It rises when an investigation actually spends acts, because that is the only thing that puts claims
into ledgers. It cannot rise on a clock.

**What a discovered covert membership costs is computed from the observers, not from the secret.**
The claim enters the judging set; each member applies their own stance toward the proposition and
their own stance toward the discovered person's marks. So the identical discovery — *this man is
Restoration at degree 3* — costs a Goldenfurt Free Master his committee seat, because the
Kettlemakers' committee holds strong stances against the proposition and against Southern Einhir
hands both; costs an Oastad fisherman nothing, because his neighbours are already sympathisers; and
makes a Southern Einhir Canon a scandal at Himmelenger, because the Church's standing marks and the
proposition collide in every observer's table at once. One mechanism, three outcomes, no
faction-wide reputation number anywhere.

- **Closed loop.** Produced by concealment and by investigation acts; carried in observers' ledgers;
  consumed by judging sets, by requisition (you cannot ask a man to act openly for a faction he must
  hide), and by threat assessment.
- **N-line.** Cut avowal and every faction is public, which deletes infiltration, informers, the
  Burned, cover identities, and the entire reason a Restoration cell is organised as a cell.

---

## 2. Capacity routes through persons — a faction has no verbs

This is the sharpest claim in the lane and the one that makes size stop mattering.

```
capacity(f, node, act) = ∃ P ⊆ members(f) with address ⊆ node such that
                           requires(act, P) is satisfied
                         and ∀p ∈ P : eligible(p, act, node)
                         and ∀p ∈ P : requisition(asker, p, act, node) succeeds
```

Three things to notice.

**It is an existential over persons, not a sum over size.** `presence` does not appear. A faction
with two members and one of them a gate warden has capacity to open a gate; a faction with nine
thousand members and none of them a gate warden does not, and no amount of growth changes that,
because growth changes `presence` and `presence` is not in the formula.

**`eligible` is the substrate's ordinary per-person act eligibility and it never consults the
faction.** Faction membership does not unlock an act. This is what keeps the game from acquiring a
second, faction-shaped action economy sitting parallel to the person one.

**`requires(act, P)` is a predicate over person-*sets*, which is how multi-person acts work without a
faction ever getting an action-point pool.** The tithe reckoning at Goldenfurt requires the praefect,
the parish priest and the guild burgher to sit together; a levy exemption requires a majority of the
Free Masters present at the standing date; a night raid requires one person who holds the keys and
one who holds the door. A faction performs such an act only if it holds *enough different persons in
enough different posts*, all of whom pass requisition in the same season — and any one of them can
simply not turn up.

**Attribution is a separate, contestable claim.** When a person acts, they may attach
`for(faction)`. That attachment is an assertion, and like every assertion it can be false, denied, or
manufactured. A Niflhel operative burning a warehouse and leaving a Restoration marker is one act and
two claims, and the second one is what everybody's threat assessment will read.

- **Closed loop.** Produced by requisition succeeding on a person who is eligible at a node; carried
  as an ordinary act with an attribution claim; consumed by the resolver, and by every witness whose
  ledger now holds *this faction did that here.*
- **N-line.** Cut person-routed capacity and factions get verbs; the moment they do, a faction with
  a big number can act anywhere, T1 dies, and the strategic layer detaches from the people in it.

---

## 3. The derived profile, which gates nothing and changes everything

```
presence(f, n)  = Σ over p ∈ members(f) with address(p) ⊆ n of w(degree(p,f))
density(f, n)   = presence(f, n) / weighted_population(n)
footprint(f)    = { n : presence(f, n) > 0 }        # upward-closed in the containment tree
```

Roll-up is one pass up the tree: each node sums its children. Nothing is stored; the profile is
recomputed and can never be stale.

**What reads the profile:**

| reader | what it does with it |
|---|---|
| perception | how loudly a faction registers to a person standing at a node |
| reputation | how strangers price a person's known membership |
| threat assessment | who bothers to oppose you, and with what |
| recruitment salience | whether the proposition is even *available* as a stance referent to a person here |

**What does not read it:** capacity, eligibility, requisition, contest resolution, the argument
system. Nothing that decides an outcome reads a scale number, ever.

And the profile a decision-maker actually acts on is not the true one:

```
perceived_presence(f, n | observer o) =
    Σ over p ∈ n for whom o's ledger holds a membership claim about (p, f)
      of w(claimed degree) · confidence(that claim)
```

Covert edges contribute zero until discovered. So underestimation and overestimation are free, and
both are wrong in the direction the observer's evidence is thin.

*Underestimated:* Duke Magnus Vaynard reads the Restoration in Grauwald at perceived density 0.02
because two men have been caught. The true figure is 0.19 across four hamlets, and it is spread
across sympathisers who have never been asked to do anything visible. He allocates one Knight of the
Peace.

*Feared before it acts:* the Kettlemakers of Goldenfurt are 140 avowed persons at density 0.31 in one
community. Everyone can count them. They have not moved on anything for eleven seasons and their
capacity at the Court Parliament is zero, because their one burgher's seat lapsed. The praefect
negotiates with them anyway, because his threat assessment reads density and his ledger holds no
claim about the lapsed seat.

- **Closed loop.** Produced by the roll-up over the commitment map each tick; carried nowhere (true
  profile) and in observers' ledgers (perceived); consumed by perception, reputation and threat
  assessment only.
- **N-line.** Cut the profile and a small faction cannot be underestimated and a large one cannot be
  feared before it acts — every faction is exactly as frightening as what it has already done.

---

## 4. POWER_BASE: the shape of a support set, and its paired cut

Standing is **one shared rank space**, `standing(p, n) ∈ 0..7`, per person per node. There is no
second seat-space and no faction rank ladder.

Standing is **computed, never stored**, from a **support set** `S(p, n)` — the named persons whose
compliance or regard is what makes the standing real:

```
standing(p, n) = clamp₀₇ ( Σ over q ∈ S(p,n) of contribution(q, p, n) )
contribution(q, p, n) = f( standing(q, n), regard(q → p), compliance(q, p) )
```

Because it is computed, there is **no scheduled recovery tick**: standing moves when and only when
something happens to a member of `S`. A person whose support set is untouched does not decay, and a
person whose patron dies does not need a timer to fall.

`power_base(p, n)` is the **topology of S** — a distribution of mass over seven shapes. It is not an
eligibility filter and it gates no action, because gating capability on biography is refused: gate on
a class and losing a person is a promotion opportunity; gate on "the one with the cavalry history"
and losing one person costs you cavalry forever. What the basis types is not what you may do. **It
types how your standing can be taken away.**

| basis | shape of S | how standing rises | the characteristic cut | what an investigator must learn to find the cut | cost / cadence of the cut |
|---|---|---|---|---|---|
| **patronage** | a rooted tree; every contribution conditioned on the root's | the patron sponsors, appoints, vouches | remove the root — every conditioned contribution voids in one event, fanning into N simultaneous demotions | *who sponsored whom, in what order* — a chain of witnessed admission and appointment acts | one act against one person, who is usually the best-defended person available |
| **merit / credential** | the body holding the criterion, plus everyone who defers to the credential | pass the gate (the Masterpiece Examination is exactly this) | rewrite the criterion, or void a specific examination — retroactive, because the credential's force lives as a claim in *other people's* ledgers about what it means | who sits the committee now, what the criterion currently says, and which sitting holders would fail a rewritten one | cheap in violence, expensive in the committee's regard, and slow: it needs a standing date |
| **kinship** | living kin plus the hearth's succession pointer | birth, marriage, fostering, legitimation | break the pointer (disinherit, legitimate a rival) — or simply outlast it: failing to place a child for one generation decays the precedent by demography, with no violence at all | the hearth's marriages, the pointer's current target, which kin are of an age, and who has no heirs | free if you can wait; a generation is the cadence |
| **bureaucratic** | the persons who *must route through* p to reach something | volume filtered, not rank — a clerk with standing 1 who reads every petition outranks a minister | a single bypass, used publicly once. S empties, because its members were never loyal — only routed | what actually routes through p, and whether an alternative route exists that nobody has used yet | near-free once found; the entire difficulty is finding it |
| **military** | armed persons whose larders p fills | pay, plunder, victory | interrupt the larder. Unpaid armed men do not disperse — they become their own faction and treat plunder as wages | the pay cadence, the arrears, and *who physically hands out the coin* | cheap if a revenue stream is cuttable; dangerous, because the cut manufactures a hostile faction with military capacity |
| **purchased** | holders of a transferable instrument — a charter, a farmed levy, a debt | buy it | outbid, or devalue the instrument with a dispensation that changes its terms | what the instrument is, who holds it, its price, and its written terms | money; the only basis whose cut is symmetrically available to any rich rival, which is why it never consolidates far |
| **ideological** | persons whose Conviction-primary matches the proposition | the proposition spreads by tellings | a hypocrisy: a witnessed act by p contradicting the proposition, deposited into S's ledgers. It fires on everyone holding that Conviction *simultaneously* | what p actually did, and a witness who will `tell` it credibly into the right ledgers | hardest to obtain, cheapest to fire, and irreversible — obstinacy resists re-opening |

**Every one of those "what an investigator must learn" cells is a claim tuple the investigation lane
already produces.** None of them is a hidden die roll. That is the discipline the precedent demands:
a vulnerability the player cannot read is a coin-flip wearing a mechanic's clothes.

### 4.1 Consolidation is self-limiting by construction

A person who consolidates does not replace one basis with another; they **add** bases. Duchess Inge
Baralta's claim rests on kinship (a cadet deed-family's proximity), purchased instruments (Hafenmark
charters), bureaucratic position (the Parliament's business routes through her people), and — since
the Almud–Schoenland trade opening — ideological mass among merchants who read the Crown as having
sold the peninsula. Four bases. Four independent cuts, none of which the others protect against:

```
cuts_available(p, n) = |{ b : mass_b(p, n) > 0 }|      # monotone non-decreasing in consolidation
```

The more a person consolidates, the more distinct ways there are to take them apart. No balance patch
is doing this; it is a property of the object.

### 4.2 The coalition threshold, and who pays for waiting

A single challenger can execute at most one basis-cut inside one standing-date window. Therefore:

```
unwind_cost(p, n) = Σ over bases b of mass_b · cut_cost_b(|S_b|)
single_handed  iff  ∃b : mass_b ≥ 0.8
otherwise the challenge requires a coalition able to land ⌈k⌉ cuts inside one window,
where k = the number of bases carrying mass ≥ 0.2
```

**Published to the player as a band, never as a number**, with all inputs visible: the bases, their
rough masses, the named persons in each S the player has claims about, and a verdict of
`SINGLE-HANDED` / `NEEDS ALLIES` / `NEEDS A COALITION OF THREE OR MORE`. The player can see everything
feeding the judgement and cannot see the trigger point. That is the substitute for a GM, and it costs
no mechanics.

**The R-check on the fork this creates.** The player's fork is *challenge now* against *wait and
investigate*.

- Waiting **gains**: each season of investigation may convert an unknown basis into a readable cut,
  which can collapse `k` from 3 to 1. Gain grows, then saturates when the cuts are all found.
- Waiting **costs**: `k` rises as the target consolidates, and each new basis adds a new S to
  penetrate. Cost grows.
- Challenging now **gains**: the target's S is smaller and the coalition is cheaper.
- Challenging now **costs**: acting on unread bases means cutting the wrong one, which is witnessed,
  which raises the target's ideological mass (a survived attack is a proof of enemies).

Both arms have growing gain and growing cost, and they cross at a point that depends on how fast the
player can investigate versus how fast the target can consolidate. Neither arm is structurally
dominant. **Power in this design is never invulnerable — it is expensive to unwind, and the bill is
paid by whoever waited too long.**

- **Closed loop.** Produced by the acts that place persons into support sets — sponsorship, payment,
  marriage, appointment, conversion; carried as the support-set edges plus each member's regard;
  consumed by `standing`, by `unwind_cost`, and by every investigation that asks *how do I take this
  person down.*
- **N-line.** Cut power_base and every rise is the same rise and every fall is a generic contest
  roll; you lose the entire class of play where the way somebody got where they are *is* the way to
  remove them, and you lose the reason investigation matters to the strategic layer at all.

---

## 5. Growth and shrink as one operation

There is one operation: `commit(person, faction, Δdegree)`.

| the thing it looks like | what it actually is |
|---|---|
| **schism** | a subset of members whose degree toward proposition A falls to 0 while their degree toward a rival proposition B rises. The Restoration fracturing over whether Einhir practice is political inheritance or Thread inheritance is two propositions and a few dozen commits. |
| **merger** | members of A committing to B. A does not disappear; it becomes a proposition with no edges, which is indistinguishable from a proposition nobody has sworn to yet. |
| **growth into a national body** | many commits, over seasons, in many places. The profile changes continuously as they land. |
| **collapse** | many commits with negative Δ. Same op, same tick, same readers. |
| **founding** | the first commit. |

### 5.1 The continuity lemma, stated so it can be falsified

*Claim:* there is no size at which any consumer of the faction object changes behaviour in kind.

*Proof shape:* enumerate the consumers. `presence` and `density` are sums of `w(d)`, continuous in
the map. `capacity` is an existential over persons — one commit can flip it, but it flips on *which
person*, not on how many. `requisition` reads one edge. `contest` (§8) resolves through named
persons. `standing` reads support sets, which are person sets. `unwind_cost` is a sum over bases. The
argument system reads the proposition, which does not change with membership at all.

Every one of those is either a per-person read or a monotone function of `Σ w(d)`. **No consumer
contains a term of the form `if |members| > K then <different object>`.** The only thresholds in the
entire lane are (a) band thresholds on published readouts, which change what a player is *told*, and
(b) the coalition threshold, which changes the *option set* rather than the object type. A design
that later adds a size-conditioned branch anywhere in that list breaks this lemma, and that is the
falsifier: grep the consumers for a comparison against a member count.

### 5.2 Shadow standing — derived by subtraction, not a new track

```
shadow(p, n) = standing(p, n) − licensed_standing(office(p, n))
```

What your support set actually delivers, minus what your post entitles you to. It is a subtraction of
two already-computed quantities; it is not a meter and nothing writes it.

When `shadow(p, n) > 0` and the formal office-holder `h` attempts an act whose `requires` predicate
includes persons in `S(p, n)`, `h`'s capacity computation returns **zero** — not a penalty, an empty
existential. Repeat that two or three times and `h`'s own best available act is **legalisation**:
issue a dispensation naming `p`'s function. This costs nothing coercive, converts `p`'s shadow into
licensed standing, and `h` keeps the post.

That is dual legitimacy rather than replacement, and it is how the Uln brothers become a house
becomes a faction without the object ever changing type: at no point did anyone promote anything.
`shadow` crept above zero, and the man with the seal found that the cheapest thing he could do was
write it down.

### 5.3 Fragmentation on death — nothing implements it

Patronage support sets are rooted. When the root dies, every contribution conditioned on it voids in
one event. Each former client who has a nonzero support set of their own at some node keeps their
standing *there* and is now a root. The graph lost one vertex; nobody ran a spin-off routine. When
the first Almqvist died in the 1218-AG hunting accident, this is the shape that fired, and the
question of who fired it is still open in every ledger that holds a claim about that day.

### 5.4 Recognition-fission — a charter moves no edges, because it cannot

A negotiated charter is a **dispensation** naming a subset predicate: *the parishes north of the
Grauwald ridge are of the new Dicastery.* It moves no commitment edge, because there is no set
operation in this design that could move one. What it does is deposit a claim into every person in
scope, changing what each person's own commit is worth to them.

Then the long tail: each person individually decides, as tellings reach them and as requisitions
arrive, whose asks they honour. Persons who honour both sides are not an error state — they are the
most interesting persons in the period, and they are also the ones whose double edge will eventually
be discovered by somebody. Contested allegiance ends when requisition conflicts stop occurring, which
may be never, and there is no tick that resolves it.

- **Closed loop (all of §5).** Produced by `commit`, an act by one person; carried as edges; consumed
  by profile, capacity, requisition and standing — all of which are continuous or per-person.
- **N-line.** Cut single-operation growth and every faction is the size somebody wrote it at; you
  lose schisms, defections, hollowing, spontaneous emergence from neglect, and the possibility that
  the Duke discovers a faction he had no reason to think existed.

---

## 6. Why a guild, a church and two brothers are one object

| | **Halvar & Odd Uln** | **Kettlemakers of Goldenfurt** | **Church of Solmund** | **Restoration Movement** |
|---|---|---|---|---|
| proposition | Bertold answers for the barn | the Free Master gate admits only examined hands | the peninsula holds Solmundan Orthodoxy | Einhir communities govern themselves by consensus |
| edges | 2 at d=5 | 140 avowed, mostly d=3, committee at d=4 | ~9,000 across the realm, d=1..5 | ~2,400, most at d=1–2, cells at d=3–4 |
| presence at its home node | 2.2·2 = 4.4 in one hearth | 140 in one community | 4 in that same hamlet | 19 across four hamlets |
| footprint | 1 node | 1 community, upward-closed | every settlement with a parish | scattered, no realm-level post |
| power_base mass | kinship 1.0 | merit 0.7, purchased 0.2, kinship 0.1 | ideological 0.4, purchased 0.3 (the Altonian containment grant's tax exemption and the education monopoly), bureaucratic 0.2, patronage 0.1 | ideological 1.0 |
| how it acts | Odd sets a fire | the committee sits at the examination | a priest performs a catechesis; a Cardinal issues a dispensation | a cell member carries a petition; a member avows at a market |
| its characteristic cut | one brother's death, or the other's fire being witnessed | rewrite the examination criterion | a hypocrisy witnessed and told; or the grant revoked | a hypocrisy — and nothing else, because it holds no coin and no swords |

Four rows of the same table. The Kettlemakers' membership nearly coincides with a community node,
and that coincidence is a fact about who lives on that street — the code contains no guild type. The
Church has four Dicasteries, and those are **four factions with four propositions and heavy
membership overlap**, not four sub-tiers: nearly every Dicastery member is also a Church member at
d≥3, which is a set inclusion that happens to hold rather than a containment relation that is
enforced. The Dicastery for Temporal Affairs wants the Baralta tithe exemption preserved; the
Dicastery for the Defense of the Faith wants a purge in Grauwald that will cost exactly that
exemption. Two propositions, jointly unsatisfiable over one stake at one standing date, with the same
persons committed to both. That is an institution at war with itself, and it needed no institutional
machinery.

The Restoration has no Mandate, no military and no wealth by ideology, and this is not a handicap in
the formulas — it is a power_base mass of 1.0 ideological, which means it has exactly one
vulnerability and it is the cheapest one to fire and the hardest one to obtain. Its **presence
markers** are the `avow` act used deliberately: converting covert edges to avowed raises
`perceived_presence` for every observer at a node, which changes threat assessment without changing
capacity by one point. That is a real fork with a real cost — avowed members lose standing wherever
their marks collide with the proposition, and there is no way to un-avow.

Two hundred years of institutional build shows up in exactly one place: the Church's support sets are
*old*, which means most of the persons in them were placed there by persons who are dead, which means
its patronage mass is low and its bureaucratic and ideological mass are high. The cage became a
school, and mechanically that means the education monopoly is a bureaucratic chokepoint — every
literate person in three duchies routed through it — which is the basis a single bypass empties.

---

## 7. Institutions that cause harm nobody intends

The Church of Solmund is canonically the **unwitting** suppressor of Thread Sensitivity: its
essentialist theology forecloses the perceptual preconditions for sensitivity, and this is emergent,
not designed. If that is a scripted institutional effect, the setting's central irony is a cutscene.
Here is the mechanism, composed entirely from the substrate.

**The precondition.** TS grows from *unresolved anomalous witnessing*. At view assembly, a claim `c`
is **unresolved** for person `p` if `p`'s ledger holds no explanation claim `e` with
`confidence(e) > confidence(c)` that entails `c`'s predicate. Then:

```
ts_gain(p, season) = κ(p) · Σ over unresolved anomalous claims c of
                              confidence(c) · seasons_unresolved(c)
```

Once a higher-confidence explanation arrives, `c` resolves and stops contributing — and obstinacy
resists re-opening it, so it does not come back.

**The act.** Catechesis is an ordinary `tell`, performed by a person, at a parish, to a child:

```
e = (the world, is-of-kind, essence-fixed-and-given, all-time,
     told_by(priest), confidence = credulity(child) · regard(child → priest))
```

Children have high credulity and high regard toward the priest who buried their grandmother. So `e`
lands **early**, at **high confidence**, and — this is the whole of it — it is **general**. One
general explanation of high confidence resolves an unbounded family of specific anomalies in advance.
The child who sees something at the edge of the water does not accumulate an unresolved claim; she
accumulates a resolved one, filed under a predicate that entails it.

**The consequence, which nobody chose.**

```
E[ts_gain] at node n falls with parish density(n) and with mean regard toward priests at n
```

No rule anywhere names the Church. No member's stance table contains "Thread Sensitivity" as a
referent — Confessor Arne Himlensendt's stance table does not have that row. He is sincerely devout
and completely wrong, and his acts are pastoral: he comforts frightened children. A neighbour
witnessing him do it deposits *he consoled her*. The child's own ledger deposits *the thing I saw was
a sin of the eye*. One act, two predicates, and the substrate's divergent witnessing produces both
without a special case. Pastoral compassion and ethnic suppression are the same act because they are
literally the same call to `tell`.

**The geography falls out rather than being authored.** Southern Einhir have lower Church
penetration; lower parish density means fewer early general explanations; the model predicts higher
TS emergence in Grauwald, Stillhelm, Oastad and the western-fjord pockets. Canon's map is the model's
output, which is the only kind of agreement worth having.

**It is playable in both directions, and that is the test.** If Duke Magnus Vaynard succeeds at Path
B and expels the Church's residue from Varfell, parish density falls, and TS emergence in Varfell
rises over a generation. He did not intend that either. An institution that produces outcomes no
member chose is not a Church rule; it is the general shape:

> **Any faction whose implementation acts deposit an early, general, high-confidence explanation into
> the ledgers of persons within its scope forecloses whatever inferences that explanation
> pre-empts — including inferences no member has ever considered.**

The Kettlemakers do it too, at a smaller scale, and it is the same three lines. Committee members
performing an ordinary examination deposit `(Southern hands, produce, coarse work, all-time)` into
apprentices' ledgers as a general explanation of a specific failed piece. Twenty years later a
committee that holds no malice at all fails Maret Uln, because the explanation was already resolved
before she walked in. Caste reproduced by institutions rather than by individual malice, which the
setting says explicitly is the intent, and which here is one mechanism running at two scales.

- **Closed loop.** Produced by every `tell` performed by any member implementing the proposition —
  catechesis, confession, examination feedback, parish schooling; carried in the hearer's claim
  ledger; consumed by the unresolved-anomaly count at view assembly, which the TS check and every
  subsequent inference read.
- **N-line.** Cut this and every harm in the game is somebody's plan. You lose the institution that
  destroys the thing it never noticed, the sincere man whose kindness is the mechanism, and any
  possibility that the player's own successful reform produces a consequence nobody in the world
  wanted.

---

## 8. What is refused here, and what replaces each refusal

- **A faction tier, level, or scale field.** Replaced by §3's recomputed profile. Declaring scale is
  what makes growth discontinuous.
- **A faction-wide reputation scalar.** Replaced by per-person regard toward a referent. The Church
  is loved in Himmelenger and hated three valleys south, and one number cannot hold both.
- **Merge / split / promote / found-at-size operations.** Replaced by `commit` run in two directions
  (§5), and by proposition-identity, which means founding is one person's act.
- **A faction action-point pool or any faction verb.** Replaced by `requisition`, whose cost is paid
  in the *member's* time, the member's regard, and the member's exposure.
- **Relationship modifiers large enough to dissolve structural conflict.** Two propositions are
  **positionally opposed** when they are jointly unsatisfiable over the same stake at the same
  standing date. The satisfiability test contains no regard term. Regard decides who carries a
  petition and who is believed; it never decides whether both sides can win, because sometimes they
  cannot and no amount of liking anybody changes it. At d=5 the offer term is absent from the
  refusal check entirely.
- **Parallel rank tracks.** One shared rank space, `standing(p, n) ∈ 0..7`, plus exactly four named
  auxiliary meters, each substituting in at exactly one named gate:

  | meter | range | the *only* gate it substitutes at |
  |---|---|---|
  | commitment degree | 0–5 | the requisition check |
  | regard / disposition | −5..+5 | the carry check and the telling-credence check |
  | support-set mass | derived | the unwind check |
  | shadow | derived | the legalisation check |

  There is no fifth, and `presence`/`density` are not meters — they are reads.
- **A leader as a flat bonus on a roll.** A flat shift of size X is worth `X / (0.8·√Pool)`, so it is
  worth systematically *more* to a weak faction than a strong one — which is backwards. The in-band
  form: **a leader changes the option set and the pool source, never a modifier.** Concretely, Yrsa
  Vossen contributes three things and none of them is a number added to a die roll: (1) she is a
  person whose eligibility makes certain acts *exist* at nodes where she stands; (2) a contest
  resolved through her draws its pool from *her* capability rather than another member's — choosing
  which member acts is choosing a different pool, not buying a bonus; (3) her regard with d≥3 members
  lowers their requisition obstacles, which changes *who will act*, not how well they roll.
- **A scheduled recovery tick on standing.** Standing is computed from support sets, so it moves on
  events and cannot drift back on a cadence.
- **A "known %" on a membership, and a stored exposure counter.** Both replaced by claims in knowers'
  ledgers and a derived exposure read.
- **Gating capability on power_base.** Considered — the precedent literature proposes power_base as
  an eligibility filter on scale-actions — and **refused**, because gating on biography means losing
  one person costs a faction a capability permanently. `power_base` types the *cut*, not the *act*.
- **A grievance-to-revolt threshold.** Revolt is a density of commitments to a rival proposition
  crossing what a settlement's coercive apparatus can hold, and every person in it has a name, a
  hearth, and a specific man they blame.

---

## 9. Contested rather than owned

**No object in this lane has an `owner` field of faction type.** Offices are held by persons.
Holdings have *claimants* — a set of `(person, claim, basis)` triples. Institutions are containers
with judging sets and standing dates. The word "control" never appears as state.

So what does it mean for the Kettlemakers to control Kettlemakers' Row? It means: of the persons
holding the Row's posts, four are Kettlemakers at d≥3. Contesting the Row is contesting *those four
persons* — by cutting the merit basis that put them there, by outbidding the purchased one, by
turning one of them, or by getting a fifth post created and filled by someone else. Nothing changes a
control field, because there is no control field to change. A faction can lose an institution without
losing a single contest: three persons' commitment edges moved and the fourth retired.

And the substrate's `contest(container, prize, claimants)` composes here with one required binding,
which this document supplies: **claimants are factions, but resolution runs through each claimant's
best-placed member**, selected by the capacity existential of §2. A faction with realm-scale presence
and no eligible person at the node enters the contest with an empty set and does not resolve — it is
not defeated, it is *absent*, and everyone can see it was absent.

The genre solved shared control decades ago by declining to make ownership a scalar. Applied here:
the tithe reckoning at Goldenfurt is `requires(P)` where P must contain a Crown praefect, a parish
priest, and a guild burgher. Those are three persons in three posts, each committed to two or three
different factions at different degrees, and none of the factions can perform the act alone. When the
Baralta Crown Claim reaches a standing date and the Church's own succession is contested at the same
season, the same handful of persons are required at two overlapping `requires` predicates, and the
consecration crisis is a **capacity conflict** — not a scripted event, just two acts asking for the
same three men in the same month.

---

## 10. Two worked traces

### 10.1 A two-person grudge becoming realm-scale, with no discontinuity anywhere

**Season 1.** Maret Uln, Southern Einhir, is failed at the Masterpiece Examination in Goldenfurt.
Her brothers Halvar and Odd each `commit` to *(Reeve Bertold answers-for the Uln barn, before levy
day)* at d=5. Faction exists; edges 2; `presence = 4.4` at Hearth of Uln; `footprint` = 1 hearth;
`power_base` kinship 1.0; `capacity(f, Goldenfurt, arson) = 1` because Odd is eligible and, at d=5,
passes his own requisition trivially.

**Season 3.** Odd burns Bertold's outbuilding. Two witnesses deposit different predicates: a Knight
of the Peace deposits *arson*; four hamlet neighbours deposit *the Ulns answered for the barn.* The
second predicate is a telling that spreads. Nineteen hamlet persons acquire a stance toward the
proposition. **No commits yet** — a stance is not a commitment.

**Season 5.** The neighbours raise a petition to remit Maret's examination fee. The guild burgher
whose seat it would cost drops it publicly, because the Kettlemakers' judging set would punish him
for carrying an Einhir grievance. Grievance stances deposit toward the container and toward him
personally.

**Season 6.** A Restoration cell member, hearing the story third-hand and angrier than it happened,
performs `tell` naming *(Einhir communities govern themselves by consensus)* to eleven of those
nineteen. Six `commit` at d=1, two at d=2. The Uln faction still has two members; the Restoration's
`presence` at the Einhir hamlet moves from 3.0 to 4.5. Nothing crossed a boundary.

**Seasons 7–14.** The same shape runs at Stillhelm and two western-fjord pockets, because the same
petitions are being dropped by different burghers for the same structural reason. Restoration
`presence` in Grauwald reaches 61; `density` 0.19; `footprint` now includes Grauwald and, by
upward-closure, Varfell and the Realm. `perceived_presence` for Duke Magnus Vaynard is 6 — two men
caught, at claimed d=3, confidence 1.0.

**Season 15.** Halvar Uln, now d=3 Restoration as well as d=5 in his own two-man faction, is admitted
to a cell that includes a Vaynard household clerk. Vaynard's proposition — expel the Church and
Altonian residue, break the caste system — is not the Restoration's proposition and never becomes it.
But it is *not jointly unsatisfiable* with it over the Grauwald stake, which means the two factions
can each requisition the same persons for the same act without either absorbing the other.

**Season 19.** The Baralta Crown Claim creates a realm standing date. The Restoration's capacity at
the Court Parliament is still zero — it holds no one there — but Vaynard's is not, and the clerk who
is d=3 in both is the person through whom the demand travels. It reaches the Parliament as Vaynard's
proposition, amended, with the Restoration's backing invisible in the record. Realm-scale.

At no point in nineteen seasons did any operation other than `commit` run, and at no point did any
reader of the faction object behave differently because the faction had become larger.

### 10.2 A large faction that cannot act

**The setup.** The Dicastery for the Defense of the Faith wants a man arrested in Riverside, the
dock district of Baralta. Its realm `presence` is 3,100; `density` at the realm 0.06; `footprint`
includes every settlement with a parish. By every number anyone can read, it is one of the four most
powerful factions in Valoria.

**The computation.** `capacity(Dicastery, Riverside, arrest)`. `requires(arrest, P)` needs a person
holding a binding post at that node plus two persons able to lay hands on a man in a crowd.

Members of the Dicastery whose address falls inside Riverside: **one** — a parish priest, d=3, who
holds a post that binds nobody and commands no armed persons. `eligible(priest, arrest, Riverside)` =
false. The harbour warden holds the binding post; he is a Crown officer, his regard toward the
Dicastery is −2, and he is d=2 in Niflhel. He is not a member, so requisition is not even available —
there is no edge to read. **The existential is empty. Capacity is zero.**

Not "reduced". Not "at a penalty". Zero, in a district three streets long, for a faction with three
thousand members.

**Meanwhile.** Niflhel's realm `presence` is 84 — under three percent of the Dicastery's, invisible
in any threat assessment that reads density. Its members inside Riverside: the harbour warden at
d=2, two dockworkers at d=3, one of the Burned at d=4. `capacity(Niflhel, Riverside, arrest) = 1`,
and it will happen the same night if anyone asks.

**What the Dicastery can actually do**, and every option is a person-placement act, slow and visible:
send a priest with a post (seasons, and it must be admitted); requisition a Templar from the Defense
of the Faith's military basis at a node two rungs up and march him in (visible, and it converts a
police problem into a caste incident on a waterfront that is caste-open by design); commit the
harbour warden by raising his regard or finding what he wants (this is the only fast option and it is
an investigation, not a decree); or issue a dispensation and discover that a dispensation is a
telling and a telling is not an arrest.

**The lesson the trace exists to make unarguable.** Size buys you *being noticed*, and nothing else.
Capacity is a question about persons and posts, and the answer at any given street corner is
frequently no. A faction that has confused its profile for its reach finds out at the moment it
needs the reach, and the finding-out is the scene.

---

## CHALLENGE — where I diverge, and one coordination request

**1. A numbering collision, not a disagreement.** The spine's §5.3 forward-references "document 07"
as the argument system that composes on the standing-date hook. This lane is assigned document 07.
Both cannot be 07; I have written to my lane assignment and flag the collision rather than silently
renumbering somebody else's reference.

**2. A binding I am adding to the spine's `contest`, which the spine leaves ambiguous.** §4.1 states
that `contest(container, prize, claimants)` takes *factions* as claimants, while §1.3 and §2 state
that capacity routes through *persons*. Read literally together, a faction with realm presence and no
person at the node is a valid claimant, which would reintroduce scale as a gate through the back
door. §9 above resolves it: **claimants are factions, resolution runs through each claimant's
best-placed member, and a claimant with an empty capacity existential is absent rather than
defeated.** I believe this is what the spine intends; it does not say so, and the difference is
load-bearing.

**3. One place I think the spine's wording undersells itself.** §1.3 says the derived profile "gates
nothing," which is true and which I have held to — no resolution path reads it. But the profile is
not therefore inert: it is the input to every other person's threat assessment, so it determines who
is opposed, who is ignored, and who is negotiated with before acting. The honest statement is that it
gates no *outcome* while being one of the most causally potent quantities in the game, and a later
reader who takes "gates nothing" to mean "is decorative" will delete the wrong thing.

**4. A degree scale is a composition, not a divergence.** §1.2 of the spine says the difference
between a sympathiser and a member is "a number on one edge." §1.2 above makes that number an ordinal
0–5 with a licence table, because requisition needs to know what may be asked. If the spine intends
that number to be continuous rather than ordinal, the licence table becomes a set of bands over it
and nothing else in this document changes.
