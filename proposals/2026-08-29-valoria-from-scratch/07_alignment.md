# 07 — Alignment: Factions That Scale Continuously

## Status: PROPOSED (2026-08-29) — a from-scratch design. Nothing here ratifies on merge.
## Lane: FA (alignment) · Composes on `01_substrate.md` §1.2–1.4, §2, §3, §4, §4.1
## Answers the question §4 delegates here: whether offices + alignment suffice for the Church's four Dicasteries and the guilds' grade ladders.

**The single structural idea.** A faction is a *proposition* plus a *map from persons to a degree of
commitment*. No tier, no level, no size class, no scale field, and **no verb**. Everything a faction
appears to do is a person doing it and saying who for; everything it appears to *be* is recomputed by
observers from their own incomplete ledgers. Growth and collapse are one operation,
`commit(person, faction, Δdegree)`, run with different signs, and two brothers reach realm scale without
an authoring act because **no consumer of the object changes what it reads at any size.**

The prior failure made faction a tier. A tier has boundaries; a boundary needs a crossing act; a
crossing act must be authored; and then the world holds only the factions somebody wrote. Here it holds
every faction any two people ever swore anything about, and the interesting ones are interesting for
*where their members stand*.

---

## 1. The faction object, completely

```
Faction := Proposition                                   # the identity. nothing else identifies it.
Edge    := (person, faction, degree, avowal, since, cause)
```

No member list is held on the faction. Edges live on persons; "membership" is a query.

### 1.1 The proposition — the same object an argument attacks

The substrate's memory rows are `(subject, predicate, value, when, source, confidence)` in the
indicative. A proposition is the same tuple with a mood field, `mood ∈ {is, ought, will}`, and a
faction's identity is a proposition in `ought` or `will`:

| faction | proposition |
|---|---|
| Halvar and Odd Uln, sworn over their sister's refused Masterpiece | *(Reeve Bertold, answers-for, the Uln barn, before levy day, **ought**)* |
| The Kettlemakers of Goldenfurt | *(the Free Master gate, admits, only examined hands, all-time, **ought**)* |
| The Church of Solmund | *(the peninsula, holds, Solmundan Orthodoxy, all-time, **ought**)* |
| The party of the Defense of the Faith | *(heterodox practice, is-suppressed-by, force where persuasion fails, all-time, **ought**)* |
| The Restoration Movement | *(Einhir communities, govern, themselves by consensus, all-time, **ought**)* |
| The Baralta Crown Claim | *(Inge Baralta, holds, the throne, on the next vacancy, **will**)* |

This is what holds the lane together: **an argument attacks a proposition, and a faction *is* a
proposition, so attacking a faction and attacking a claim are one operation with the same moves.** The
fallback ladder — deny the act, deny the label, admit and justify, challenge the venue — runs against
*(Bertold answers-for the barn)* exactly as against *(the granary is full)*. This lane needs no
faction-specific argument machinery; it needs the argument lane to accept a mood field.

Because identity *is* the proposition, **there is no found-a-faction operation.** Two people in Oastad
independently holding the same stance are not yet a faction — a stance is not a commitment. The faction
begins at the first `commit`: an oath taken, a courier hidden, grain handed over. That is the whole of
"the Restoration can emerge spontaneously from territorial neglect": dropped petitions write grievance
into hundreds of ledgers, the stances converge on one proposition because it is the obvious negation of
what was refused, and then somebody acts.

- **Loop.** Produced by grievance and by tellings that name it; carried as a stance-table referent and
  as the identity of edges; consumed by the argument system, requisition, and every roll-up.
- **N-line.** Cut it and a faction is a bag of names — nothing to argue against, nothing to schism
  over, no way for two strangers to discover they were already on the same side.

### 1.2 The commitment degree, and what each licenses

| d | name | `w(d)` | licenses — and nothing beyond |
|---|---|---|---|
| 0 | none | 0 | — (degree 0 *is* deletion; departure needs no operation) |
| 1 | sympathy | 0.15 | will not testify against a member; may be told cell-safe claims; stance weight applies at view assembly |
| 2 | sympathiser | 0.40 | may be asked for material, shelter, carriage at low cost; may `carry` a petition of the faction's proposition |
| 3 | member | 1.00 | may be **requisitioned** for acts inside their ordinary capability; may `avow` |
| 4 | sworn | 1.60 | may be requisitioned for acts **against their own container's interest**; refusal is witnessed by every d≥3 member |
| 5 | constitutive | 2.20 | the proposition holds a Conviction-primary slot; **no offer term enters the refusal check at all**; refusal is a Coherence event |

Degree 5 is where *"relationship modifiers large enough to dissolve structural conflict"* is refused
concretely. Nobody buys Odd Uln off his oath — not because the number is large, but because the offer
term is absent from the formula.

**Requisition** is the only channel from a faction to an act, and it is an ask between two persons:

```
requisition(asker, member, act, node)
  obstacle = base(act) + burden − 2·w(d) − regard(member→asker)/2 − conviction_bonus
  burden   = cost to the member's computed need
           + 2 · harm to the member's container's stake
           + 3 · marks the act collides with
```

Refuse at low burden and the edge drops a degree; refuse at high burden and it does not — a faction
asking the impossible loses nobody, and one asking the trivial and refused has learned something true.
`conviction_bonus` is the substrate's Momentum term, so a d=5 ask is the cheapest in the game and the
one that spends a person's whole position.

- **Loop.** Produced by `commit` acts; carried as edges on persons; consumed by requisition, capacity,
  the roll-ups, and the judging sets that punish or reward discovery.
- **N-line.** Cut degree and everyone is in or out: no sympathiser slipping bread, no shallow end to
  recruit informers from, and no way to *hollow* a faction rather than shatter it.

### 1.3 Secrecy is not a property of the secret

Each edge carries `avowal ∈ {avowed, private, covert}`.

- **Avowed** — an act deposited the membership claim into the person's community judging set by the
  ordinary witnessing path.
- **Private** — no public claim. Discoverable by witnessing a requisition honoured, or by being told.
- **Covert** — members additionally perform concealment acts and may `tell` a *cover claim*: an
  assertion of a different edge, or of none. Niflhel runs every edge covert and is caste-open *because*
  covert work at the Baralta waterfront needs Southern Einhir members whose marks let them stand there
  unremarked — a consequence of the operational requirement, not a policy anyone wrote.

There is **no "known %" on a membership** — no knower on such a number. Who knows is a row in a
knower's ledger, deposited as an `inferred` claim whose confidence comes from corroboration. That fails
closed, so one rumour retold three times through Riverside supports the inference exactly once.

**Exposure is derived, never stored:**

```
exposure(edge) = Σ over persons q holding a claim about it of
                 confidence(q's claim) · hostility(q → the proposition)
```

It rises only when an investigation spends acts, because acts are the only thing that puts claims in
ledgers. It cannot rise on a clock.

**What a discovered covert membership costs is computed from the observers, not from the secret.** The
claim enters a judging set; each member applies their own stance toward the proposition *and* toward
the person's marks. One identical discovery — *this man is Restoration at degree 3* — costs a
Goldenfurt Free Master his committee seat, because that committee holds stances against both the
proposition and Southern Einhir hands; costs an Oastad fisherman nothing, his neighbours being
sympathisers already; and makes a Southern Einhir Canon a scandal at Himmelenger, where marks and
proposition collide in every observer's table at once. One mechanism, three outcomes, no faction-wide
reputation number anywhere.

- **N-line.** Cut avowal and every faction is public: no infiltration, no informers, no Burned, no
  cover identities, and no reason a Restoration cell is organised as a cell.

---

## 2. Capacity routes through persons — a faction has no verbs

```
capacity(f, node, act) = ∃ P ⊆ members(f) with address ⊆ node such that
                           requires(act, P) holds,
                           ∀p ∈ P: eligible(p, act, node),
                           ∀p ∈ P: requisition(asker, p, act, node) succeeds
```

**An existential over persons, not a sum over size.** `presence` does not appear. Two members, one a
gate warden, opens a gate. Nine thousand and no gate warden does not, and growth changes only a
quantity the formula never reads.

**`eligible` is the substrate's ordinary per-person eligibility and never consults the faction.**
Membership unlocks no act — which is what stops a second, faction-shaped action economy growing beside
the person one.

**`requires(act, P)` is a predicate over person-*sets*, which is how multi-person acts work without a
faction ever getting an action-point pool.** The tithe reckoning at Goldenfurt needs the praefect, the
parish priest and the guild burgher sitting together; a levy exemption needs a majority of Free Masters
present at the standing date; a night entry needs one who holds the keys and one who holds the door. A
faction performs such an act only if it holds enough *different persons in different posts*, all passing
requisition in one season — and any one can simply not turn up.

**Nobody, the faction's own leader included, computes true capacity.** A leader decides from a view, so
what they act on is an *estimate* of who will comply; discovering that a sworn member refuses is a
normal and dramatic event.

**Attribution is a separate contestable claim.** A person may attach `for(faction)` to an act — an
assertion, falsifiable, deniable and forgeable. A Niflhel operative burning a warehouse and leaving a
Restoration marker is one act and two claims, and the second is what everyone's threat assessment
reads.

- **Loop.** Produced by requisition succeeding on an eligible person at a node; carried as an ordinary
  act plus an attribution claim; consumed by the resolver and by every witness.
- **N-line.** Cut person-routed capacity and factions get verbs; then a faction with a big number acts
  anywhere, T1 dies, and the strategic layer detaches from the people in it.

---

## 3. The two profiles

The substrate splits these and this lane holds the split, because the obvious implementation is a back
door wide enough to void the signature rule.

```
presence(f, n)  = Σ over members inside n of w(degree)
density(f, n)   = presence(f, n) / weighted_population(n)
footprint(f)    = { n : presence(f, n) > 0 }     # upward-closed in the containment tree
```

| | computed from | consumed by |
|---|---|---|
| **true profile** | actual memberships, covert included | **exactly one consumer: `resolve`.** Revolt is a comparison between how many people are really committed at a node and what the coercive apparatus can hold — a fact about the world, resolver-side. **No `choose` may take it.** |
| **estimated profile** | one observer's own claim ledger | that observer, inside their view: perception, reputation, threat assessment, recruitment salience |

```
estimate(f, n | observer o) = Σ over persons p in n for whom o holds a membership claim
                                of w(claimed degree) · confidence(that claim)
```

Every observer holds a different estimate of the same faction; covert edges are absent until somebody's
claim names them, so misjudgement is the default rather than a special case. **Nothing that decides an
outcome reads either profile** — capacity, eligibility, requisition, contest and argument are all
person-reads. Size buys being *noticed*.

*Underestimated:* Vaynard's estimate of the Restoration in Grauwald is density 0.02 — two men caught.
The truth is 0.19 across four hamlets, spread over sympathisers never asked to do anything visible. He
sends one Knight of the Peace.

*Feared before acting:* the Kettlemakers are 140 avowed at density 0.31 in one community, and anyone
can count them. They have moved on nothing for eleven seasons and their capacity at the Court Parliament
is zero, their burgher's seat having lapsed. The praefect negotiates anyway: his estimate reads density,
and his ledger holds no claim about the seat.

- **N-line.** Cut the estimated profile and a conspiracy of nine cannot be read as a rabble, or a
  rabble as a conspiracy — and every act taken against a wrong estimate goes with it.

---

## 4. POWER_BASE: the shape of a support set, and its paired cut

Standing is **one shared rank space**, `standing(p, n) ∈ 0..7`. There is no faction rank ladder and no
second seat-space.

Standing is **computed, never stored**, from a **support set** `S(p, n)` — the named persons whose
compliance or regard makes the standing real:

```
standing(p, n) = clamp₀₇ Σ over q ∈ S(p,n) of contribution( standing(q,n), regard(q→p), compliance(q,p) )
```

Because it is computed, there is **no scheduled recovery tick**: standing moves when and only when
something happens to a member of `S`. A person whose support set is untouched does not decay; a person
whose patron dies needs no timer to fall.

`power_base(p, n)` is the **topology of S** — mass distributed over seven shapes. It is **not an
eligibility filter and gates no action**: gating capability on biography means losing one person costs
a faction a capability permanently. What the basis types is not what you may do. It types **how your
standing can be taken away.**

| basis | shape of S | how it rises | the characteristic cut | what an investigator must learn to find the cut | cost / cadence |
|---|---|---|---|---|---|
| **patronage** | a rooted tree; every contribution conditioned on the root's | the patron sponsors, appoints, vouches | remove the root — every conditioned contribution voids in one event, fanning into N simultaneous demotions | *who sponsored whom, in what order* — a chain of witnessed admission and appointment acts | one act against one person, usually the best-defended person available |
| **merit / credential** | the body holding the criterion, plus everyone deferring to the credential | pass the gate — the Masterpiece Examination is exactly this | rewrite the criterion, or void a specific examination. Retroactive, because the credential's force lives as claims in *other people's* ledgers about what it means | who sits the committee now, what the criterion says, and which sitting holders would fail a rewritten one | cheap in violence, expensive in the committee's regard, slow: it needs a standing date |
| **kinship** | living kin plus the hearth's succession pointer | birth, marriage, fostering, legitimation | break the pointer (disinherit, legitimate a rival) — or outlast it: failing to place a child for one generation decays the precedent by demography, with no violence at all | the hearth's marriages, the pointer's target, which kin are of an age, who has no heir | free if you can wait; the cadence is a generation |
| **bureaucratic** | the persons who *must route through* p | volume filtered, not rank — a clerk at standing 1 who reads every petition outranks a minister | a single bypass, used publicly once. S empties, because its members were never loyal — only routed | what actually routes through p, and whether an unused alternative route exists | near-free once found; the whole difficulty is finding it |
| **military** | armed persons whose larders p fills | pay, plunder, victory | interrupt the larder. Unpaid armed men do not disperse — they become their own faction and treat plunder as wages | the pay cadence, the arrears, and who physically hands out the coin | cheap if a revenue stream is cuttable; dangerous, because the cut manufactures a hostile faction that has military capacity |
| **purchased** | holders of a transferable instrument — a charter, a farmed levy, a debt | buy it | outbid, or devalue the instrument with a dispensation changing its terms | what the instrument is, who holds it, its price, its written terms | money — the only basis whose cut is symmetrically available to any rich rival, which is why it never consolidates far |
| **ideological** | persons whose Conviction-primary matches the proposition | the proposition spreads by tellings | a hypocrisy: a witnessed act by p contradicting the proposition, deposited into S's ledgers. Fires on everyone holding that Conviction *simultaneously* | what p actually did, and a witness who will `tell` it credibly into the right ledgers | hardest to obtain, cheapest to fire, irreversible — obstinacy resists re-opening |

**Every "what an investigator must learn" cell is a claim tuple the investigation lane already
produces.** None is a hidden roll. That is the discipline: a vulnerability the player cannot read is a
coin-flip wearing a mechanic's clothes.

### 4.1 Consolidation is self-limiting by construction

Consolidating does not replace one basis with another; it **adds** them. Duchess Inge Baralta's claim
rests on kinship (a cadet deed-family's earned proximity), purchased instruments (Hafenmark charters),
bureaucratic position (Parliament's business routes through her people), and — since Almud's Schoenland
opening — ideological mass among merchants who read the Crown as having sold the peninsula. Four bases,
four independent cuts, none protecting against the others.

```
cuts_available(p, n) = |{ b : mass_b(p, n) > 0 }|      # monotone non-decreasing in consolidation
```

No balance patch is doing this. It is a property of the object.

### 4.2 The coalition threshold, and who pays for waiting

A single challenger can execute at most one basis-cut inside one standing-date window.

```
single-handed  iff  ∃b : mass_b ≥ 0.8
otherwise the challenge needs a coalition landing ⌈k⌉ cuts inside one window,
where k = |{ b : mass_b ≥ 0.2 }|
```

**Published as a band with every input visible, and never as a number**: the bases, their rough
masses, the named persons in each `S` the player holds claims about, and a verdict of
`SINGLE-HANDED` / `NEEDS ALLIES` / `NEEDS A COALITION OF THREE OR MORE`. The player sees everything
feeding the judgement and never the trigger point. That is the substitute for a GM and it costs no
mechanics.

**R-check on the fork it creates** — *challenge now* against *wait and investigate*:

- Waiting **gains**: each season of investigation may convert an unread basis into a readable cut,
  collapsing `k` from 3 to 1. Gain grows, then saturates when the cuts are found.
- Waiting **costs**: `k` rises as the target consolidates, and each new basis is a new `S` to
  penetrate. Cost grows.
- Acting now **gains**: `S` is smaller, the coalition cheaper.
- Acting now **costs**: cutting an unread basis is cutting the wrong one, which is witnessed — and a
  survived attack *raises* ideological mass, because it is proof of enemies.

Both arms have growing gain and growing cost, crossing at a point set by how fast the player can
investigate against how fast the target can consolidate. Neither is structurally dominant. **Power is
never invulnerable — only expensive to unwind, and the bill is paid by whoever waited too long.**

- **N-line.** Cut power_base and every rise is the same rise and every fall a generic contest roll.
  You lose the whole class of play where *how somebody got where they are* is the way to remove them,
  and with it the reason investigation matters to the strategic layer.

---

## 5. Growth and shrink as one operation

| what it looks like | what it is |
|---|---|
| **schism** | a subset whose degree toward A falls to 0 while degree toward a rival proposition B rises. The Restoration fracturing over political-inheritance versus Thread-inheritance is two propositions and a few dozen commits. |
| **merger** | members of A committing to B. A becomes a proposition with no edges — indistinguishable from one nobody has sworn to yet. |
| **growth into a national body** | many commits over seasons in many places. |
| **collapse** | many commits with negative Δ. Same op, same tick, same readers. |
| **founding** | the first commit. |

### 5.1 The continuity lemma, stated so it can be falsified

Enumerate the consumers. `presence`/`density` are sums of `w(d)`, continuous in the map. `capacity` is
an existential over persons — one commit can flip it, but on *which person*, never how many.
`requisition` reads one edge; `contest` resolves through named persons (§9); `standing` reads support
sets; `unwind_cost` sums over bases; the argument system reads only the proposition, which does not
change with membership at all.

**No consumer contains a term of the form `if |members| > K then <different object>`.** The only
thresholds in the lane are band thresholds on published readouts, which change what a player is *told*,
and the coalition threshold, which changes an *option set* rather than an object type. The falsifier is
mechanical: any later size-conditioned branch in that list breaks the lemma.

### 5.2 Shadow standing — a subtraction, not a track

```
shadow(p, n) = standing(p, n) − licensed_standing(office(p, n))
```

What your support set delivers, minus what your post entitles you to. Two already-computed quantities;
nothing writes it.

When `shadow > 0` and the formal holder `h` attempts an act whose `requires` predicate includes persons
in `S(p, n)`, `h`'s capacity returns **zero** — not a penalty, an empty existential. Repeat twice and
`h`'s cheapest remaining act is **legalisation**: a dispensation naming `p`'s function. Nothing
coercive, shadow becomes licensed standing, `h` keeps the post. Dual legitimacy, not replacement — and
it is how the Ulns become a house becomes a faction without the object changing type. Nobody promoted
anything; `shadow` crept above zero and the man with the seal found writing it down cheaper than
fighting it.

### 5.3 Fragmentation on death — nothing implements it

Patronage support sets are rooted. When the root dies, every conditioned contribution voids in one
event, and each former client with a support set of their own keeps their standing *there* and is now a
root. The graph lost a vertex; no spin-off routine ran. The 1218-AG hunting accident is this shape, and
who caused it is still an open claim in every ledger holding one.

### 5.4 Recognition-fission — a charter moves no edges, because it cannot

A negotiated charter is a **dispensation** naming a subset predicate — *the parishes north of the
Grauwald ridge are of the new see.* It moves no commitment edge, because no set operation exists that
could; it deposits a claim into everyone in scope, changing what each person's own commit is worth to
them. Then the long tail: each person decides individually, as tellings arrive and requisitions land,
whose asks to honour. People who honour both are not an error state — they are the most interesting
persons of the period, and eventually somebody discovers the double edge. Contested allegiance ends
when requisition conflicts stop, which may be never, and no tick resolves it.

- **N-line (all of §5).** Cut single-operation growth and every faction is the size somebody wrote it
  at: no schisms, no defections, no hollowing, no spontaneous emergence from neglect, and no Duke
  discovering a faction he had no reason to think existed.

---

## 6. Why a guild, a church and two brothers are one object

| | **Halvar & Odd Uln** | **Kettlemakers of Goldenfurt** | **Church of Solmund** | **Restoration Movement** |
|---|---|---|---|---|
| proposition | Bertold answers for the barn | the gate admits only examined hands | the peninsula holds Solmundan Orthodoxy | Einhir communities govern themselves by consensus |
| edges | 2 at d=5 | 140 avowed, mostly d=3 | ~9,000 realm-wide, d=1..5 | ~2,400, most at d=1–2 |
| presence at home node | 4.4, one hearth | 140, one community | 4 in that same hamlet | 19 across four hamlets |
| footprint | 1 node | 1 community, upward-closed | every settlement with a parish | scattered; no realm post |
| power_base mass | kinship 1.0 | merit 0.7, purchased 0.2, kinship 0.1 | ideological 0.4, purchased 0.3 (the Altonian grant's tax exemption and the education monopoly), bureaucratic 0.2, patronage 0.1 | ideological 1.0 |
| how it acts | Odd sets a fire | the committee sits at the examination | a priest performs a catechesis; a Cardinal issues a dispensation | a member carries a petition; a member avows at a market |
| its cut | one brother dead, or the other's fire witnessed | rewrite the examination criterion | a hypocrisy told; or the grant revoked | a hypocrisy — and nothing else, holding neither coin nor swords |

Four rows of one table. The Kettlemakers' membership nearly coincides with a community node; that is a
fact about who lives on that street, not a guild type in the code. Two hundred years of institutional
build shows up in exactly one place: the Church's support sets are *old*, so most persons in them were
placed by persons now dead — patronage mass low, bureaucratic and ideological high. The cage became a
school, and mechanically the education monopoly is a bureaucratic chokepoint, the basis a single bypass
empties.

The Restoration's poverty is no handicap in any formula: ideological mass 1.0 means one vulnerability,
cheapest to fire and hardest to obtain. Its **presence markers** are `avow` used deliberately —
converting covert edges to avowed raises every observer's *estimate* at a node without changing capacity
by one point. A real fork with a real cost, since avowed members lose standing wherever their marks
collide with the proposition, and there is no un-avow.

### 6.1 The question §4 delegates here: a Dicastery is an office cluster, and that suffices

The substrate rules that the Church is a faction, a parish is a community, and a Dicastery is
*neither* — an office cluster — then asks whether offices plus alignment carry it. **They do, and here
is the decomposition.** An office cluster is:

1. **a named set of offices**, each of which is already containment-rung state — a mark plus a binding
   power, held by a person, revocable, sitting on whatever node owns it;
2. **a proposition** — what the cluster is *for* — which is a faction identity like any other; and
3. **the appointment acts** that fill those offices, performed by persons who hold others in the set —
   which is precisely a patronage-topology support set.

Nothing else is required. Test it against what a Dicastery has: the seal is an instrument, a mark on a
person; the archive a holding at Himmelenger with claimants; the right to adjudicate a binding power on
the Cardinal's office; the Cardinalate's succession that office's appointment rule, held on the node
owning it. **None of it needs a second tree.** Guild grade ladders resolve identically and settle the
no-parallel-tracks refusal into the bargain: apprentice, journeyman, Free Master and burgher are **marks
conferred by admission acts at a community**, not a rank space. They gate nothing directly, entering
play through other persons' stances and through `requires` predicates that name them (*a majority of
Free Masters present*).

**The honest cost, stated rather than discovered later.** An office cluster spanning different
containment nodes has no node that owns it, so *"the Dicastery decided"* is never expressible — only
*"the four persons holding these posts each did something."* You cannot address a petition to a
Dicastery; you address it to a person holding one of its offices, and that person can drop it. I take
this as the correct cost — T1 refusing to be talked around — but it means the fiction must never render
an institution as a speaker.

It buys something large immediately. Because the *party* is a faction and the *Dicastery* an office
cluster, four clusters can be at war inside one Church with no institutional machinery at all. The party
holding Temporal Affairs wants the Baralta tithe exemption preserved; the party holding the Defense of
the Faith wants a Grauwald purge that costs exactly that exemption. Two propositions, jointly
unsatisfiable over one stake at one standing date, many of the same persons committed to both.

---

## 7. Institutions that cause harm nobody intends

The Church is canonically the **unwitting** suppressor of Thread Sensitivity — emergent, not designed.
If that is a scripted institutional effect, the setting's central irony is a cutscene. Here is the
mechanism, composed entirely from the substrate.

**The precondition.** TS grows from *unresolved anomalous witnessing*. At view assembly, a claim `c` is
**unresolved** for `p` if `p` holds no explanation claim `e` with `confidence(e) > confidence(c)` that
entails `c`'s predicate.

```
ts_gain(p, season) = κ(p) · Σ over unresolved anomalous claims c of confidence(c) · seasons_unresolved(c)
```

Once a higher-confidence explanation arrives, `c` resolves and stops contributing — and obstinacy
resists re-opening it, so it does not come back.

**The act.** Catechesis is an ordinary `tell`, performed by a person, at a parish, to a child:

```
e = (the world, is-of-kind, essence-fixed-and-given, all-time,
     told_by(priest), confidence = credulity(child) · regard(child → priest))
```

Children have high credulity and high regard toward the priest who buried their grandmother, so `e`
lands **early**, at **high confidence**, and — this is the whole of it — it is **general**. One general
explanation resolves an unbounded family of specific anomalies *in advance*. The girl who sees something
at the edge of the water does not accumulate an unresolved claim; she accumulates a resolved one, filed
under a predicate that entails it.

**The consequence nobody chose.** `E[ts_gain]` at a node falls with parish density and with mean regard
toward priests. No rule names the Church, and no member's stance table contains "Thread Sensitivity" as
a referent — Confessor Arne Himlensendt's does not. He is sincerely devout and completely wrong, and his
acts are pastoral: he comforts frightened children. A neighbour watching deposits *he consoled her*; the
child's ledger deposits *the thing I saw was a sin of the eye*. One act, two predicates, from the
substrate's divergent witnessing with no special case. Pastoral compassion and ethnic suppression are
the same act because they are the same call to `tell`.

**The geography is output, not authorship.** Lower Church penetration in the south means fewer early
general explanations, so the model predicts higher TS emergence in Grauwald, Stillhelm, Oastad and the
western-fjord pockets: canon's map is what the model produces. It runs backwards too — if Vaynard
succeeds at expelling Church and Altonian residue from Varfell, parish density falls and TS emergence
rises over a generation. He did not intend that either.

**The general shape, so this is not a Church rule:** *any faction whose implementation acts deposit an
early, general, high-confidence explanation into the ledgers of persons in its scope forecloses whatever
inferences that explanation pre-empts — including inferences no member has ever considered.*

The Kettlemakers do it too, smaller and identically. Committee members performing an ordinary
examination deposit *(Southern hands, produce, coarse work, all-time)* as a general explanation of one
failed piece. Twenty years on, a committee holding no malice fails Maret Uln, because the explanation
resolved before she walked in. Caste reproduced by institutions rather than individual malice — the
setting's stated intent — is one mechanism at two scales.

- **Loop.** Produced by every `tell` performed by any member implementing the proposition — catechesis,
  confession, examination feedback, parish schooling; carried in the hearer's ledger; consumed by the
  unresolved-anomaly count at view assembly, which the TS check and every later inference read.
- **N-line.** Cut this and every harm in the game is somebody's plan. You lose the institution that
  destroys the thing it never noticed, the sincere man whose kindness is the mechanism, and any chance
  that the player's own successful reform produces a consequence nobody wanted.

---

## 8. What is refused here, and what replaces it

| refused | replaced by |
|---|---|
| a faction tier, level, or scale field | §3's two recomputed profiles |
| a faction-wide reputation scalar | per-person regard toward a referent — the Church is loved in Himmelenger and hated three valleys south, and one number cannot hold both |
| merge / split / promote / found-at-size | `commit` in two directions, plus proposition-identity, which makes founding one person's act |
| a faction action-point pool, or any faction verb | `requisition`, paid in the member's time, regard and exposure |
| a "known %" on a secret, a stored exposure counter | claims in knowers' ledgers; exposure derived |
| a scheduled recovery tick on standing | standing computed from support sets, so it moves on events and cannot drift back on a cadence |
| power_base as an eligibility filter | considered and refused — gating on biography means losing one person costs a capability permanently. It types the cut, not the act. |
| a grievance-to-revolt threshold | a true-profile density crossing what the coercive apparatus holds, with everyone in it holding a name, a hearth, and a specific man they blame |

Four refusals carry mechanism rather than a back-reference, and they are stated in full.

**Relationship modifiers large enough to dissolve structural conflict.** Two propositions are
**positionally opposed** when jointly unsatisfiable over one stake at one standing date, and the
satisfiability test contains **no regard term**. Regard decides who carries and who is believed; it
never decides whether both can win. At d=5 the offer term is absent from the refusal check entirely.

**Parallel rank tracks.** One shared rank space, `standing ∈ 0..7`, plus exactly four auxiliary meters,
each substituting at exactly one gate:

  | meter | range | its *only* gate |
  |---|---|---|
  | commitment degree | 0–5 | the requisition check |
  | regard | −5..+5 | the carry check and the telling-credence check |
  | support-set mass | derived | the unwind check |
  | shadow | derived | the legalisation check |

There is no fifth. Guild grades are marks, not a track (§6.1); presence and density are reads.

**A leader as a flat bonus on a roll.** A flat shift of X is worth `X / (0.8·√Pool)`, so it is worth
systematically *more* to a weak faction than a strong one — backwards. The in-band form: **the leader
changes the option set and the pool source, never a modifier.** Yrsa Vossen contributes three things,
none of them a number added to a die: (1) she is a person whose eligibility makes certain acts *exist*
at nodes where she stands; (2) a contest resolved through her draws its pool from *her* capability, so
choosing which member acts is choosing a different pool rather than buying a bonus; (3) her regard with
d≥3 members lowers their requisition obstacles, changing *who will act*, not how well.

---

## 9. Contested rather than owned

**No object in this lane has an `owner` field of faction type.** Offices are held by persons; holdings
have *claimants*, a set of `(person, claim, basis)`; institutions are containers with judging sets and
standing dates. The word "control" never appears as state.

So what does it mean for the Kettlemakers to control the Row? That of the persons holding the Row's
posts, four are Kettlemakers at d≥3. Contesting the Row is contesting *those four persons* — cutting the
merit basis that put them there, outbidding the purchased one, turning one, or getting a fifth post
created and filled otherwise. A faction can lose an institution without losing one contest: three edges
moved and the fourth man retired.

The substrate's `contest(container, prize, claimants)` composes here with one binding this document
supplies: **claimants are factions, resolution runs through each claimant's best-placed member as
selected by §2's existential, and a claimant with an empty existential is *absent* rather than
defeated** — and everyone can see it was absent.

Applied: the tithe reckoning at Goldenfurt is `requires(P)` for a Crown praefect, a parish priest and a
guild burgher — three persons in three posts, each committed to two or three factions at different
degrees, and no faction can perform the act alone. When the Baralta Crown Claim reaches a standing date
while the Church's own succession is contested, the same handful of persons are required by two
overlapping `requires` predicates at once. The consecration crisis is a **capacity conflict**, not a
scripted event: two acts asking for the same three men in the same month.

---

## 10. Two worked traces

### 10.1 A two-person grudge reaching realm scale, with no discontinuity anywhere

**S1.** Maret Uln, Southern Einhir, is failed at the Masterpiece Examination. Her brothers Halvar and
Odd each `commit` at d=5. Faction exists; presence 4.4 at one hearth; power_base kinship 1.0;
`capacity(f, Goldenfurt, arson) = 1`, because Odd is eligible and at d=5 passes his own requisition.

**S3.** Odd burns Bertold's outbuilding. A Knight of the Peace deposits *arson*; four neighbours deposit
*the Ulns answered for the barn.* The second predicate spreads, and nineteen persons acquire a stance
toward the proposition — **and no commits yet**, because a stance is not a commitment.

**S5.** The neighbours petition for Maret's fee to be remitted. The guild burgher whose seat it would
cost drops it publicly: the Kettlemakers' judging set would punish him for carrying an Einhir grievance.
Grievance deposits toward the container and toward him personally.

**S6.** A Restoration cell member, hearing it third-hand and angrier than it happened, `tell`s the
consensus proposition to eleven of the nineteen. Six commit at d=1, two at d=2. The Uln faction still
has two members; Restoration presence at the hamlet moves 3.0 → 4.5. Nothing crossed anything.

**S7–14.** The same shape at Stillhelm and two fjord pockets, because the same petitions are dropped by
different burghers for the same structural reason. Restoration presence in Grauwald reaches 61, density
0.19, footprint upward-closed to Varfell and the Realm. Vaynard's estimate is 6.

**S15.** Halvar, now d=3 Restoration as well as d=5 in his own two-man faction, joins a cell containing a
Vaynard household clerk. Vaynard's proposition — expel Church and Altonian residue, break the caste
system — never becomes the Restoration's, but it is *not jointly unsatisfiable* with it over the Grauwald
stake, so both can requisition the same persons without either absorbing the other.

**S19.** The Baralta Crown Claim creates a realm standing date. Restoration capacity at the Court
Parliament is still zero — it holds no one there — but Vaynard's is not, and the clerk who is d=3 in both
is who the demand travels through. It arrives as Vaynard's proposition, amended, the Restoration's
backing invisible in the record. Nineteen seasons, one operation, and not one reader of the object
behaved differently because the faction had got larger.

### 10.2 A large faction that cannot act

**Setup.** The party of the Defense of the Faith wants a man arrested in Riverside, the dock district
of Baralta. Realm presence 3,100; footprint every settlement with a parish. By every number anyone can
read, one of the four most powerful factions in Valoria.

**Computation.** `requires(arrest, P)` needs a person holding a binding post at that node plus two who
can lay hands on a man in a crowd. Members addressed inside Riverside: **one** — a parish priest, d=3,
holding a post that binds nobody and commanding no armed persons, so `eligible` is false. The harbour
warden holds the binding post; he is a Crown officer, his regard toward the party is −2, and he is d=2
in Niflhel. He is not a member, so requisition is not even available — no edge to read. **The
existential is empty. Capacity is zero.** Not reduced, not penalised: zero, in a district three streets
long, for a faction of three thousand. And the Dicastery owns no office at Riverside at all — an office
cluster is a set of posts, and none of these are in it.

**Meanwhile.** Niflhel's realm presence is 84, under three percent, invisible to any threat assessment
reading density. Inside Riverside: the harbour warden at d=2, two dockworkers at d=3, one of the Burned
at d=4. `capacity(Niflhel, Riverside, arrest) = 1`, and it happens tonight if anyone asks.

**What the party can actually do**, every option a person-placement act, slow and visible: send a priest
holding a binding post (seasons, and he must be admitted); requisition a Templar from its military basis
two rungs up and march him in (visible, and it converts a police matter into a caste incident on a
waterfront that is caste-open by design); or commit the harbour warden by finding what he wants — the
only fast option, and an investigation rather than a decree. Issuing a dispensation discovers that a
dispensation is a telling, and a telling is not an arrest.

**The point.** Size buys being noticed. Capacity is a question about persons and posts, and at any given
street corner the answer is frequently no. A faction that has confused its profile for its reach finds
out at the moment it needs the reach, and the finding-out is the scene.

---

## CHALLENGE — one divergence, one binding, one coordination note

**1. The binding I add to `contest`, which the spine leaves ambiguous.** §4.1 says claimants are
*factions*; §1.3 and §2 say capacity routes through *persons*. Read literally together, a faction with
realm presence and nobody at the node is a valid claimant — which readmits scale as a gate through the
back door. §9 resolves it: resolution runs through the best-placed member, and an empty existential is
absence, not defeat. I believe this is what the spine intends; it does not say so, and the difference
is load-bearing.

**2. The delegated question, answered with its price named.** The spine's §4 leaves open whether offices
plus alignment suffice for the Dicasteries and the grade ladders. §6.1 answers **yes** and pays out
loud: an office cluster has no owning node, so *"the Dicastery decided"* is permanently inexpressible,
and the fiction must never render an institution as a speaker. If that cost is judged too high, the only
alternative I can see is a second tree for institutional internal structure — which I recommend against,
because it reintroduces the multi-parent containment §1.1 refuses and would let an institution acquire a
verb.

**3. A numbering collision, not a disagreement.** The spine references "document 07" twice — §5.3 for
the argument system, §4 for the institutional question this lane answers. Both cannot be 07; I have
written to my lane assignment rather than renumber another lane's reference.

**4. The degree scale is composition, not divergence.** The spine calls the sympathiser/member
difference "a number on one edge." §1.2 makes it an ordinal 0–5 with a licence table, because
requisition must know what may be asked. If the intent is a continuous number, the licence table becomes
bands over it and nothing else here changes.
