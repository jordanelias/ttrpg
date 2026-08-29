# 12 — Coercion, Force, and War

## Status: PROPOSED (2026-08-29) — a from-scratch design. Nothing here ratifies on merge.
## Lane: MB (mass battle) with FA/PC seams · Composes on `01_substrate.md`, which wins on any conflict.
## Method: derived from the substrate's persons-and-two-relations, plus the historical/cross-game precedent set.

**The single structural idea of this document.** There is no coercive apparatus. There are *armed
persons who are standing there and may or may not do what they are told*, and the whole of coercion —
a reeve's seizure, a market beating, a garrison, a siege, a war — is one question asked about them:
**who is willing?** That question is a single function, `will()`, and the entire document is that
function evaluated over different sets. The garrison is `will()` over the armed. The revolt is
`will()` over the aggrieved. The mutiny is `will()` over men whose wages are three seasons late. The
battle line is `will()` over a section that has just lost its officer. Nothing here is a second
model, and there is no meter anywhere that fills up.

**Reading key.** Every object is a closed loop — *producer → carrier → consumer* — and carries an
N-line. §9 runs the R-criterion on every fork.

---

## 1. What coercive capacity actually is

The substrate (§5.1) ends revolt on a comparison: a faction's committed density at a node against
*what the coercive apparatus there can hold*. That phrase is the load-bearing one, and the obvious
implementation — a `Defense` or `Order` stat on the settlement — voids T1 and the whole substrate
with it. A stat cannot refuse.

### 1.1 The Hold is a sum over persons

```
Hold(n, targets, giver) = Σ  reach(p) × will(p, disperse, targets, giver)
                        p ∈ armed_present(n)
```

`armed_present(n)` is not a roster field. It is a query: persons whose address lies inside *n* right
now, who carry arms, computed the same way any set is computed. A merchant's four hired guards, a
Löwenritter chapter quartered in the town, twelve men of the praefecture's watch, and forty
Kettlemakers who own billhooks are all in it, at different reaches and wildly different willingness.

```
reach(p) = 1 + arms(p ∈ 0..2) + mounted(p ∈ 0..1) + drilled(p ∈ 0..1)      →  1..5
```

`reach` is the only number here that is about equipment. It means *how many unarmed, unorganised
persons this one person can face down* — the honest historical quantity, and the reason a garrison of
sixty holds a town of four thousand.

### 1.2 The willingness term is real, and it reads stances

```
will(p, form, targets, giver) = clamp01(
      0.30                                     # baseline: people mostly do as they are told
    + 0.08 × stance(p → giver)                 # −5..+5   →  ±0.40
    + 0.06 × stance(p → proposition)           # −5..+5   →  ±0.30
    + 0.10 × conviction_weight(p, {Authority, Order, Duty-of-post})
    + 0.05 × obeyed_claims(p, giver)           # −3..+3, §6.3
    − 0.55 × sever(p, targets)                 # the neighbour term
    − 0.20 × arrears(p)                        # seasons of unpaid wage, capped at 1.0
    − 0.15 × severity(form)                    # disperse .2 · seize .4 · strike .6 · burn .8 · kill 1.0
)
```

A person acts on the order if `will ≥ 0.50`; between 0.30 and 0.50 they comply *badly* (§6.2);
below 0.30 they refuse.

**The neighbour term is the point of the section.** `sever` is the fraction of the target set the
person cannot separate himself from:

```
sever(p, targets) = max(
    1.00  if any target shares p's hearth, or is a Knot partner of p,
    0.80 × (share of targets inside p's community),
    0.50 × (share of targets bearing p's own heritage mark)
)
```

Max, not sum, so it saturates honestly at 1.

**The worked case the substrate demands.** Praefect Aldwin of Goldenfurt orders his watch to disperse
a gathering in the Southern Einhir hamlet outside the wall.

| watchman | stance→Aldwin | sever | conviction Order | will | outcome |
|---|---|---|---|---|---|
| Bertil, Kettlemakers' Row, no kin outside the wall | +2 | 0.00 | 0.20 | 0.30+0.16+0.02−0.03 = **0.65** | obeys |
| Hakon, levied from the hamlet itself | +1 | 0.80 (community) | 0.10 | 0.30+0.08+0.01−0.44−0.03 = **−0.08 → 0.00** | refuses |
| Karsten, Southern Einhir, quartered from Stillhelm, kin nowhere near | +1 | 0.50 (heritage) | 0.15 | 0.30+0.08+0.015−0.275−0.03 = **0.09** | refuses |
| Sister-Sergeant Ida, Löwenritter, Authority-primary, backs the order's proposition | 0 | 0.00 | 0.60 | 0.30+0.06+0.18−0.03 = **0.51** | obeys |

Twenty men of the watch is not twenty men. Against *that* target set it is Bertil and eleven like
him — Hold = 12 × reach 2 = 24, against a hamlet where two hundred have committed. The same twenty
against a Crown-Latinate grain riot in the market are a Hold near 50, because `sever` runs the other
way. **A garrison drawn from the community it is ordered against is a different quantity from the
same number of outsiders**, and the difference is `0.55 × 0.80 = 0.44` of every man's willingness.

This is also why the setting's two caste-open institutions are the Löwenritter and Niflhel, without
any rule naming them: an order whose targets are Southern Einhir is executed only by persons with low
`sever` or high `conviction_weight(Authority)`, and those are the two bodies that recruit for it.

### 1.3 Revolt is the same function over the other set

```
Press(f, n) = Σ  weight(p) × will(p, strike, office_holders(n), f's proposition)
            p ∈ members(f) ∩ n
```

Same function. `giver` is the proposition rather than a person, which the substrate already supports —
stance toward propositions and stance toward persons are one table (§2).

**Revolt fires when `Press(f, n) > Hold(n, members(f), the office-holder who would give the order)`.**
No threshold, no gauge, no authored trigger — a comparison of two person-sums, both of which move
every time anybody's stance moves.

- Closed loop: produced by the stances and addresses of persons standing at *n*; carried nowhere,
  recomputed on demand; consumed by the resolver whenever a coercive act is attempted at *n* and by
  any person's view as a **band** (§9.3), never as a number.
- **Cut it and you lose:** the garrison that will not fire on its own hamlet — which is the single
  most historically load-bearing fact about coercion, and the reason every ruler in the setting has to
  think about *who* holds the town rather than *how many*.

---

## 2. The muster — raising force from a population

The muster is a canonical down-stroke that produces an up-stroke's fuel, and it runs on the
containment ladder with no new machinery.

### 2.1 Two channels, and the split is load-bearing

The precedent is unambiguous that the strongest evidence favours **splitting a free obligation
channel from a paid professional channel**. They are the same object at different terms:

| | **Levy** | **Retinue** |
|---|---|---|
| authorised by | a `Dispensation(Levy, scope, quota, terms)` | a person's own coin |
| routed through | containment: territory → settlement → community → hearth | alignment: a contract with named persons |
| costs | hearth **hands**, and grievance in the levied node | coin per season, at a standing date |
| `sever` against local targets | **high** — they are the neighbours | **low** — they are outsiders |
| failure mode | refusal at a rung, and hunger next season | **arrears** (§6.4) |

The fork is genuinely two-shaped: the levy is cheap now and expensive later *through the hearth*; the
retinue is expensive now and catastrophic later *through the wage*. And they are not
interchangeable — the cheap force is structurally the one that cannot suppress, because `sever` is
high exactly where the levy was raised. §9.1 runs the R-check.

### 2.2 Apportionment is an act by a named person at every rung

`Levy` enters as an ordinary dispensation and refracts downward the way all dispensations do. At each
rung one person performs `apportion(node, quota) → {child: quota}`. The sums must cover; everything
else is his choice, and his choice reads his own stances against the children's marks.

That is where caste enters, and it enters as nothing. Praefect Aldwin apportioning Goldenfurt's levy
of forty gives twenty-eight to the Einhir hamlet of four hundred and twelve to the Row of nine
hundred, because his stance toward the hamlet is −3 and the Row's burghers judge him. No caste rule
was consulted. The Masterpiece Examination's documented bias is the same one line of code with a
different prize — a committee's stances applied to a candidate's marks — which is what the setting
means by *discrimination reproduced by institutions rather than by malice*.

**Who is taken.** The apportioner names quotas, not persons; the **hearth** chooses which member goes,
unless the apportioner names one (an act that costs him regard with everyone whose stance opposes it,
and is exactly how a grudge gets a man killed at no cost to the man holding the grudge).

**What a hearth loses — bound to the larder.** Each person contributes `hands(p) ∈ 0..3` to their
hearth's production.

```
larder_next = larder_now + Σ hands(members present) − mouths
```

A levy does not take a mouth away; the man still eats, at the Crown's expense, and comes back or
doesn't. It takes his **hands**. The Hearth of Marlen with five members and eleven mouths, losing its
two strongest (hands 3 and 3) to Aldwin's levy, runs `larder_next = larder − 6` against unchanged
mouths and computes a need next season. Need plus capability plus the new terms is an **opening**
(substrate §5.2), and the openings a hungry hearth sees include petition, migration, theft, and
commitment to a faction whose proposition is that the levy was unjust. **The levy is the generator of
the thing the levy exists to suppress**, and that is one subtraction, not a mechanism.

**Refusal.** `refuse_levy(person_or_hearth, quota)` is an ordinary act. The apportioner one rung up
now has a shortfall and exactly three options, all of them acts:

1. **Absorb** — raise another child's quota. Spreads the injury to a community that did comply, which
   is how a levy manufactures a second grievance out of the first.
2. **Coerce** — a `Force` act (§4) against the refusers. This requires `Hold` at that node against
   *his own neighbours*, so `sever` is near 1 for the men he would use. **The levy is enforced by a
   levy, and usually cannot be.**
3. **Report the shortfall** — costs regard with the issuer, and deposits in every witness a claim that
   his order was not obeyed, which is §6.3's contagion.

- Closed loop: produced by an office-holder's dispensation; carried by a named apportioner at every
  rung, who may weight, absorb, coerce or report; consumed by hearths as lost hands and by the field
  as bodies.
- **Cut it and you lose:** the connection between an army existing and a countryside being hungry —
  and with it every peasant revolt that is *about* the war rather than adjacent to it.

### 2.3 Quality is capped, and nobody else caps it

The precedent's null N-8 is exact: four of four surveyed franchises cap force *quantity* by rank or
title and let effectiveness climb open-endedly. That is a gap in the field, not a model to copy. Here
quality is capped, and the cap is not a number:

**A muster's quality is the capabilities of the specific persons in it, and those persons are bounded
by who exists at the nodes it was drawn from.** A hearth sends the member it can spare; a community
sends the households it likes least; a territory of fishers has no cavalry because nobody there owns
a horse. Quality climbs only by **accumulating named persons** — veterans who survived, a Löwenritter
chapter you have paid for — and every one of them is a liability carrying a stance, a hearth, a Knot,
an arrears counter and a `sever` value against your next order. **The cap is that quality is a set of
names, and a set of names is fragile.** A real ceiling with no ceiling number in it.

---

## 3. The battle seam, fixed at the root

The contract is:

```
Battle(field, sideA, sideB)
side = (commander: person, sections: [(officer: person|None, roster: [person|cohort])], supply)
```

**No faction appears in that signature.** Nothing is derived from a Realm's military stat, nothing is
labelled with a faction id. A side is a commander, some officers, and some people. If you cannot name
the commander, there is no side.

### 3.1 The commander changes the option set and the pool source, never a modifier

The precedent's arithmetic is the reason: **a flat shift of size X is worth X / (0.8·√Pool)** standard
deviations.

| Pool | value of a flat +2 |
|---|---|
| 4 | 1.25 σ |
| 9 | 0.83 σ |
| 25 | 0.50 σ |

A commander bonus is therefore worth 2.5× as much to a weak side as to a strong one — backwards from
every intent anyone has when they add it. So commanders add nothing.

What a commander does is choose a **gambit** from `options(commander.view, field, sections)`, and a
gambit does two things: it names *which persons' capability the roll draws from*, and it names *what
is spent*.

| gambit | pool source | spends | available only if |
|---|---|---|---|
| Hold the line | Σ section endurance × cohesion | cohesion | always |
| Break them at dawn | commander's **Acuity** vs enemy commander's **Focus** | commander's own exposure | a claim in his view that the enemy is unready |
| Turn the ford | one section's Agility, unopposed | that section leaves the line for a round | a claim in his view that the ford exists |
| Give ground and bleed them | enemy's supply | your own territory's larder | you are inside your own containment scope |
| Parley | the argument system, not this one | a standing date | both commanders willing |

**The commander acts on his view, never the world** (substrate §3). `Turn the ford` is not in his
option list if nobody told him about the ford, and it *is* in his list, disastrously, if the claim in
his ledger is false — planted by a Niflhel agent, or simply three seasons out of date. That is T4
delivering a lost battle without a single hidden roll.

A brilliant commander with a broken army is therefore not a man with a bigger bonus. He is a man
whose option list contains gambits that route the roll **away from his ranks and onto himself** — and
each of those costs his own exposure, which is how commanders die.

### 3.2 Officers contribute reach, and the gate is role, not biography

A muster resolves in **sections**. The commander's gambit is a dispensation, and like every
dispensation it reaches persons only by travelling through named persons. Here the officer *is* the
channel.

```
transmit(officer) = 0.40 + 0.06 × (Charisma + Focus)      →  0.52 .. 0.94   (attributes 1..7)
transmit(None)    = 0
```

A section with no living officer does not receive the gambit at all. It performs its own default,
chosen by its own cohesion: `C ≥ 0.5 → hold`, `C < 0.5 → break`. **Killing an officer makes a section
deaf**, which is why the enemy shoots at officers, which is why officers die, which is the loop.

**Gate on role, never on biography.** The refusal is explicit and it binds: no capability may be
attached to "the one officer with cavalry history." Any person can be an officer. When an officer
falls, the section promotes the person within it holding the highest regard among his own peers —
computed from the community-style judging set the section already is — at the start of the next
round, with his own transmit. **Losing a person is a promotion opportunity**, and the man promoted is
someone with a name, a hearth, a stance toward the commander, and now a reason to have opinions about
this war.

### 3.3 Individuals in the ranks contribute fractions, never amounts

The corpus's only concrete anti-leverage rule: **a personal→unit effect must be a fraction of the
unit's own size or cohesion, never a flat amount.** It binds absolutely here.

```
Δcohesion(section) = k(p) × cohesion(section)        # never  Δ = +0.1
k(p) = 0.01 × (Charisma + Will)        for a person standing in that section
```

A Löwenritter knight with Charisma 6 and Will 6 gives k = +0.12. In a section at C = 0.90 he is worth
+0.108; in a section at C = 0.30 he is worth +0.036. He is worth the same *proportion* whether the
section is nine men or nine hundred, which is precisely the property the precedent says nobody has
demonstrated from N=1 to N=1000+. It holds here because it is multiplicative by construction, and it
is checkable by inspection rather than by tuning.

**Casualties reach named persons.** A losing section loses a fraction *f* of its strength. Each named
person in it then rolls survival on their own Endurance and armour against *f*: named persons in a
section that broke badly usually die and sometimes don't, and named persons in a section that held
usually live and sometimes don't. Cohorts lose weight. **Losing a specific person matters because of
what that person was attached to elsewhere** — an officer, a Knot partner, a hearth's succession
pointer, the patron of nine clients — and §8 is the whole of that consequence. Battle does not need
its own death rules; it needs to produce deaths of specific people.

### 3.4 The account of a battle is contested

Every participant `witness`es. What Hakon deposits is *the Row's men broke and left us*; what Bertil
deposits is *the hamlet's levy would not close*. Both are in ledgers, both are tellable, and the
version that reaches Goldenfurt is whichever traveller got there first. There is no true battle
report anywhere in the game.

- Closed loop: produced by two commanders choosing gambits from their views; carried by officers into
  sections as fractions; consumed as dead named persons, moved cohesion, and per-witness claims about
  what happened.
- **Cut it and you lose:** any reason a battle is *about* the people in it. Restore a faction-level
  battle and the commander becomes a doorman whose attributes never touch the outcome.

---

## 4. Violence below war

Almost all coercion in this setting is not a battle, and it must be the same primitive.

```
Force(actor, targets, form, warrant)
form    ∈ {seize, restrain, strike, burn, expel, disperse, kill}
warrant ∈ {office(post, dispensation), custom(named), none}
```

Resolution is the ordinary personal-scale contest — the actor's capability plus whoever stands with
him, against the targets' capability plus whoever stands with them, both sides' participation gated by
`will()` from §1.2.

**Warrant changes nothing physical.** It changes what witnesses deposit, and it is a *claim the actor
asserts*, which means it can be false. This is the substrate's divergent-witnessing corollary given a
verb: the same `strike` in the Goldenfurt market deposits *order was restored* in a witness whose
stance backs the praefecture and *a man's arm broken* in his neighbour. A reeve who collects a tithe
that was never levied has performed `seize` with warrant `office`, asserting a dispensation that does
not exist — and he is caught only when someone's investigation reaches the real dispensation.

Everything in the brief's list is this object with parameters:

| act | form | warrant | notes |
|---|---|---|---|
| arrest | restrain | office | requires Hold if the target's community stands with him |
| a reeve's collection | seize | office | falsifiable warrant; the classic petty extortion |
| eviction | expel | office or custom | changes the target's **address**, which is a containment edit — the most severe thing you can do to a person short of killing them |
| the beating in the market | strike | none | judged by the community's judging set, which is the whole punishment |
| burning a barn | burn | none | at night; unwitnessed unless someone was awake, so the substrate's corroboration rule decides whether it is ever attributed |
| a guild's discipline of its own | strike / expel | custom(guild grade) | expulsion revokes the Free Master mark, which is a livelihood |
| Niflhel's waterfront work | kill | none, concealed | "the Burned"; the act carries no warrant claim at all, so witnesses deposit a death with no actor named |
| the duel | strike / kill | custom(named) | consensual: both parties' `will` is a precondition, and the loser's kin deposit *a duel* rather than *a murder* **only if the custom's stated terms held**. Break the terms and every witness deposits murder. |
| the riot | many `Force(none)` acts | none | no riot object exists. A riot is what it looks like when forty people's `will` crossed 0.50 in the same hour. |
| suppression of a gathering | disperse | office | requires Hold; feeds §5 |

**Every Force act deposits a claim naming its perpetrator.** Grievance is a stance toward a referent,
and the referent of a coercive act is *the man who did it*, not the institution. This is why the
Löwenritter are hated in the south as a list of individual names, and it is why §5's structural
finding matters so much: the personal stance is the one you can clear by sacking somebody.

- Closed loop: produced by a person choosing an act; carried by the resolver into an event; consumed
  by every witness as a claim naming a perpetrator and by the target as an address, a body or a mark
  changed.
- **Cut it and you lose:** the entire register between politics and war, which is where this setting
  actually lives — and the possibility of an unwitnessed act, which is where investigations come from.

---

## 5. Suppression makes it worse — the ratchet

A `disperse` with warrant `office` that succeeds does not remove the stances that produced the
gathering. It removes their **expression**.

```
suppress(node, targets):
    for each p in targets with a live grievance stance s toward referent r:
        s.expressed  = False              # p stops acting on it
        s.scars     += 1                  # permanent on the stance row
```

Two consequences, and neither of them is a new object.

### 5.1 The re-arm threshold falls

A person acts on a grievance stance when it exceeds their own arming threshold. Scars lower it:

```
arm_at(p, r) = base_threshold(p) × 0.70 ^ scars(p, r)
```

| scars | threshold |
|---|---|
| 0 | 1.00 |
| 1 | 0.70 |
| 2 | 0.49 |
| 3 | **0.34** |

Three suppressions and it takes a third of the provocation to bring the same people out. **Suppression
works, and it converts a live problem into a dormant one that re-arms lower** — the precedent's rule
stated as one exponent.

### 5.2 Scars transmit through the hearth

The hearth owns transmission across time (substrate §4). A child raised in a hearth whose head
carries scars toward the praefecture inherits `floor(scars / 2)` of them toward the same referent. So
the ratchet decays over roughly two generations if nothing refreshes it — and is *refreshed every
generation* wherever the institution keeps producing the original injury. That is exactly the
setting's claim about Southern Einhir grievance being reproduced by institutions rather than by
malice, and it is a `floor(n/2)` on an inheritance edge.

### 5.3 Strain is derived, and personnel changes do not touch it

```
strain(n) = Σ  scars(p, referent ∈ {n, offices_of(n)})
          p ∈ n
```

**Derived from persons on demand, never stored on the container.** The substrate refuses container-level
unrest gauges (§6) and this obeys that refusal: strain is a readout, and it has properties a stored
gauge would not. It does not reset between crises. It *moves when people move* — a scarred hamlet that
emigrates lowers the node's strain and raises it wherever they land, which is an unpleasant and
correct result nobody has to author. And:

> **Replacing Praefect Aldwin clears every stance toward *Aldwin* and leaves every stance toward *the
> praefecture* exactly where it was.** Personnel changes are cheap and do nothing. Only a
> **structural** act — a dispensation that removes the generator: the levy exemption granted, the
> Examination's committee reconstituted, the hamlet given a seat at the settlement's standing date —
> clears scars, and it clears only the scars whose referent it addresses.

That sentence is the whole of the setting's institutional thesis, expressed as a difference between
two referent values on the same stance table.

- Closed loop: produced by a successful `disperse`; carried on the suppressed person's own stance row
  and inherited at half weight by their hearth's next generation; consumed by that person's arming
  threshold and by any observer's strain readout.
- **Cut it and you lose:** the reason a competent ruler's competence is what destroys him. Without the
  ratchet, suppression is a solved problem and the south is quiet forever.

---

## 6. Who is willing

An order is given by a person to persons, and they may refuse. This section is the deepest one, and
it introduces almost nothing.

### 6.1 An order is a narrow dispensation

`Order(giver, recipients, form, targets, terms)` — a dispensation addressed to named persons rather
than a scope. Each recipient computes `will()` from §1.2. There is no obedience roll and no
discipline stat.

### 6.2 Refusal has three shapes

| `will` | shape | what witnesses see |
|---|---|---|
| ≥ 0.50 | **comply** | the act |
| 0.30–0.50 | **comply badly** | the act performed slowly, partially, or at the wrong address. A compliance roll, not an effect — the precedent names instant-global-decree the single most common error in governance games, and this is where it is refused. |
| < 0.30 | **refuse** | either **overt** (says no, in front of everyone) or **covert** (agrees, does nothing), chosen by the person's own exposure calculus |

### 6.3 What happens to an office-holder whose orders are not obeyed

Nothing special-cased, because there is no authority field to decrement.

Office is a mark plus a binding power (substrate §4), and **binding power is not stored — it is
*observed compliance*.** Every witnessed refusal deposits, in every witness's ledger, a claim of the
form `(order of Aldwin, was_obeyed, false, when, firsthand)`. And `will()` reads that ledger:
`obeyed_claims(p, giver)` is the balance of obeyed-versus-refused claims a person holds about that
giver, from −3 to +3, worth ±0.15 of willingness.

So **refusal is contagious through the claim ledger and nowhere else.** One public refusal in front of
sixty people lowers sixty people's willingness on the next order, which makes the next refusal likelier,
which is witnessed by more people. Authority collapses the way a bank run does, at a speed set by how
many people saw it, and it recovers by the same channel — an order given and obeyed in public is a
claim too.

An office-holder in that spiral has real options, none of them a button: order only where `sever` is
low; order only persons whose stance toward him is high; give small orders certain to be obeyed, to
rebuild the claim balance; hire outsiders (§2.1); or concede at a standing date, paying the prize to
stop the bleeding.

### 6.4 The garrison mutiny, with no mutiny mechanic

A retinue's contract has a standing date each season at which coin is due. A missed payment is an
event. What follows uses only objects that already exist:

1. The garrison **witnesses** the missed date. Claims deposit: *the paymaster did not pay*.
2. Stance toward the paymaster falls; `arrears(p)` rises by 1 per season, subtracting `0.20` from
   every `will()` — after three seasons that is `−0.60`, more than the entire baseline.
3. **Their larder is the wage.** A hired man's hearth produces nothing; his needs are computed from a
   larder that the coin was filling. Unpaid, his computed need spikes.
4. His **openings** are recomputed against unchanged capability, unchanged arms, and a need that is
   now acute. The list of available acts is re-ranked. `Force(seize, warrant none)` against the
   nearest full granary is at the top of it.

They plunder. Nothing named mutiny was consulted, no loyalty meter crossed a line, and the historical
finding — *unpaid garrisons treat plunder as wages* — falls out of a need computation plus an option
re-rank. The same three seasons of arrears have already driven their `will` on any order the paymaster
gives to zero, so he cannot stop them with the men he has.

- Closed loop: produced by a person giving an order; carried as each recipient's own willingness
  computation; consumed as an act performed, botched or refused — and, when witnessed, as a claim
  about this giver's authority that every future recipient reads.
- **Cut it and you lose:** the possibility that having the post is not the same as having the power,
  which is the only thing that makes holding office interesting rather than administrative.

---

## 7. War between realms — deliberately thin

Everything above already exists at every rung, so war adds four things and no new resolver.

**A campaign** is: a muster (§2), a **march**, some battles (§3), and possibly a **siege**.

**The march** is persons moving through containment nodes and eating. An army in friendly territory
draws on a dispensation (requisition, with terms); an army anywhere else **forages**, which is
`Force(seize, warrant none)` against the hearths on the road. Foraging is therefore not a supply
subtraction — it is hundreds of coercive acts against named hearths, each depositing a claim naming a
perpetrator and each subtracting from a larder. **You cannot march through a territory you are
liberating without generating the grievance you came to relieve.** Duke Magnus Vaynard marching an
anti-caste army through Grauwald's Einhir hamlets discovers this in one season.

**A siege** is a Hold contest with the wall as a `reach` multiplier and a clock made of two larders.
It ends when the defenders' larder fails, or when the besieger's does, or — the interesting case —
when **a person opens the gate**. The gate is opened by whoever's `will()` toward the defending
office-holder has fallen below 0.30 and who is standing near it. Sieges are lost by hunger and by
one man.

**What victory changes: offices, and nothing else.** Conquest does not transfer a territory. It
*vacates* the offices at that node and lets the victor install holders whose warrant nobody local has
any reason to accept. Every dispensation those holders issue is a set of compliance computations
against persons whose `stance → giver` is deeply negative and whose `sever` against their own
neighbours is 1. **A conquered territory is one where every order is disobeyed**, and the conqueror's
two paths are the ratchet (§5, which works and gets worse) or a structural concession (which works and
costs him the thing he conquered for). That is an occupation system with no occupation object.

**Keep it thin on purpose.** The peninsula's live politics is mostly fought by other means, and the
design should not pull toward the one activity the throughlines never mention:

- the **Baralta Crown Claim** is a contingent claim banked against a watched vacancy; Duchess Inge
  Baralta's route to it runs through Hafenmark's Parliament and a Motion of No Confidence, both of
  which are argument at a standing date. *A claim with no enforcement resolves to open war* — which
  is what makes war the expensive branch of a political instrument rather than a parallel game.
- **Vaynard's anti-caste programme** is fought by dispensation: changing the terms of the Masterpiece
  Examination and of the Crown's Standing 3+ sponsorship gate. Those cost him no strain. An army
  would.
- **Altonia's leverage over Prince Torben** is a patronage and Knot attack on one person. There is no
  military expression of it at all.

- **Cut it and you lose:** the case where a political problem genuinely has no political solution left.
  Without war available, every fork in the game collapses to negotiation, and the threat that backs
  every negotiation is fictional.

---

## 8. Death

`die(person, cause)` fires a fixed cascade, all of whose parts are existing objects.

1. **The succession pointer fires** (hearth, substrate §4). Name, address, marks and holdings move.
   Whoever it does not reach is now a cadet branch: permanently unsatisfied needs, seeking standing
   through the Church, a guild, the Löwenritter, the Restoration, marriage, or a knife.
2. **The patronage cascade voids.** Every person whose standing source is `patron = deceased` loses
   that source — **one death fanning out into N individual demotions, each a separate event witnessed
   separately.** And it fragments: a client who had clients of his own does not fall, he **spins off**
   as an independent standing-holder. Growth and fission on the same edge.
3. **Offices vacate.** Binding power was observed compliance, so it evaporates the instant there is
   nobody to obey; the container sets a standing date to fill the post. **In that window the record is
   the prize.** Whoever holds the instrument can assert an appointment, and *if uncontested it is
   written into every ledger as genuine until discovered* — and discovery retroactively flips it, which
   is a field investigation with a duchy on it.
4. **Knots rupture.** A partner's death is a named rupture trigger. Close Knots take a Conviction
   Scar; both sides take Coherence −1 and Composure damage, and the drift propagates through the
   survivor's remaining Knots. A powerful person's death is a Coherence event across their whole
   intimate graph, which no political system can see coming and every one of them is deformed by.
5. **Claims about the death propagate, and some are false.** This is the important one. The death is
   an event; its **cause is never a fact anyone can read** — it is a predicate deposited by `witness`,
   per person, and by `tell`, which may assert what the speaker does not hold.

**The 1218-AG hunting "accident."** The first Almqvist dies. The state the setting asks for —
*a probable assassination whose perpetrator is deliberately unresolved* — is not authorial fiat here.
It is a describable configuration of the substrate:

- the true event exists and is `kill` with concealment;
- **no living person holds a firsthand claim of the cause** (the one who did, died, or is silent);
- every existing claim traces through `told_by` to a single synthetic rumour root, so — by the
  substrate's corroboration rule — *a story told three hundred times corroborates exactly once*;
- therefore no amount of political conviction can ever promote it above rumour…
- …until an investigation locates a surviving **firsthand root**: a Niflhel man who was on the ridge,
  a letter whose interval collides with an asserted alibi, a Knot partner who was told.

The revelation is a campaign event because it is a *reachable state change*, not a scripted reveal,
and it is discoverable by exactly the machinery the substrate already built.

- Closed loop: produced by any resolver outcome that kills a person; carried by the succession
  pointer, the patronage edges, the office's standing date, the Knot graph, and per-witness claims
  about the cause; consumed by heirs, clients, rivals, survivors and investigators.
- **Cut it and you lose:** any reason to kill anyone. Death without the cascade is a unit removed;
  death with it is the single highest-leverage act in the game and the one most likely to be
  misattributed.

---

## 9. R-criterion check

### 9.1 The forks, by shape of gain against shape of cost

A fork fails if gain decays while cost compounds. Every fork below is checked over time, not balanced
at a point.

| fork | gain shape | cost shape | verdict |
|---|---|---|---|
| **comply / resist** an order | comply: flat, immediate, *durable* (you keep your address and your hands). resist: a one-off retained good, plus a claim about the giver's authority that **compounds for everyone else** | comply: a scar (§5) that lowers *your own* future threshold — compounding, private. resist: a Force act against you, whose probability is `Hold` — which your resistance itself lowers | **passes.** The classic failure is resist's gain decaying against durable cost. Here resistance's principal gain — the witnessed refusal — compounds through §6.3 and is *collectively* held, while compliance's principal cost is a scar that compounds privately. Neither curve dominates. |
| **levy / hire** | levy: bodies now, free. hire: bodies now, at coin, with **low `sever`** — the only force that can suppress locally | levy: hands lost → hunger next season → petitions → commitment (compounds through the hearth). hire: arrears, which is a cliff, not a slope — three seasons and the men who were your Hold become the thing you needed Hold against | **passes.** Orthogonal failure modes, and the cheap option is structurally the one that cannot do the expensive option's job. |
| **suppress / concede** | suppress: immediate, complete, *reliable* — it works every time you have the Hold. concede: partial, slow, and it costs you the prize | suppress: `0.70^scars` on the re-arm threshold, inherited at half weight, permanent until a structural act — **compounding, and invisible in the season you pay it**. concede: one-time loss of the stake, plus a claim that you concede under pressure | **passes, and it is the sharpest fork here.** Suppression is *dominant in the short run by design*, because that is the historical truth being modelled; it loses over decades. A player who never looks past next season will never see it, which is the correct experience of being a competent ruler in a system that is destroying itself. |
| **fight / treat** | war: offices vacated and filled — durable, and the only way to take a prize somebody will not give. treaty: terms changed, and the other side keeps the ability to break them | war: march grievance along the route, strain in the conquered node, and **casualties among the specific named persons your patronage network runs through** (§8 — the cost is *structural*, not attritional). treaty: cheap talk is the default; binding instruments are the expensive exception | **passes.** War's gain is durable but its cost lands on the graph you govern *through*, which does not recover on a timer. |

**One asymmetry is deliberately left in place and it is not a failure.** `sever` makes locally-raised
force unable to suppress locally. There is no play that removes this — no drill, no bonus, no upgrade.
A ruler who wants to hold his own town must hire outsiders, and that requires coin, and coin requires
a tithe, and a tithe is a `seize`. The constraint is *positional and unbuyable*, which the precedent
set explicitly asks for: some conflicts must not be dissolvable by relationship modifiers.

### 9.2 Maximum mitigation against maximum accrual

The refusal is unambiguous: a mechanism tuned never to reach its failure state is indistinguishable
from one that does not exist. So — can a maximally competent office-holder be driven to revolt?

Maximum mitigation available to Praefect Aldwin: hire only outsiders (`sever = 0`), pay them on every
standing date (`arrears = 0`), never levy locally, carry every petition rather than dropping it,
suppress nothing.

Accrual against him, none of which he controls:

- The **Crown's** levy dispensation still arrives; he must apportion it or report a shortfall (§2.2).
  Apportioning generates hunger; reporting collapses his obeyed-claims balance.
- Paying outsiders requires coin; coin comes from the tithe; the tithe is `seize` with warrant office,
  performed by his reeves against named hearths, each act depositing a claim naming a perpetrator.
- **The scars are already there.** `strain(Goldenfurt)` is not his; it is the sum of stances his three
  predecessors and the Examination committee wrote, inherited at half weight through hearths he has
  never met.
- Every petition he carries costs him regard with the judging set that opposes it. Carrying *all* of
  them costs him all of it.

Net: **his mitigations are mutually exclusive in the same resource.** Paying the garrison requires
seizing; not seizing requires levying; levying requires apportioning; apportioning requires choosing
whom to injure. He can choose which grievance to generate and he cannot choose to generate none, and
the ratchet he inherited means each one arms at 0.49 or 0.34 of base. **The failure state is
reachable under perfect play, and it should be.**

Its mirror is checked too: is it reachable *too easily*? No — Bertil's 0.65 in §1.2 shows an
ordinary, unaggrieved watch holding an ordinary town comfortably. Hold collapses only when the target
set and the armed set overlap, or when the wage stops. Both are things a player does.

### 9.3 The view slice — how any of this is legible with no GM

Publish every input; publish a band; never publish the trigger point.

A person's view of a node they are standing in shows: **who is armed and present** (a list of names
and cohorts, because that is public), **what each of them is owed** (arrears is a fact about a
contract), and a **band** for the comparison — *the watch will hold this · the watch may not hold
this · the watch will not hold this*. It never shows `Hold = 24.3` and it never shows `Press`. The
inputs are all inspectable by investigation — you can go and ask Hakon whether he would strike his own
hamlet, and he will tell you something, and it may not be true.

- **Cut this and you lose:** the player's ability to make any of the forks in §9.1 deliberately, which
  converts the whole document into a system that happens *to* them.

---

## 10. What is refused

Each was considered and cut because a cheaper object already reaches the same emergence.

- **A settlement Order/Defense stat as the coercive apparatus.** It cannot refuse, and refusal is the
  mechanism (§1).
- **A mutiny mechanic, a riot object, a desertion check, a discipline stat.** All four are `will()`
  crossing a line; each as a separate object is a second copy that can disagree with the first.
- **A morale bar on a unit.** Cohesion is a fraction of a *section*, which is a set of persons.
- **A commander bonus, a general's stat line, a leadership modifier.** §3.1, with the arithmetic.
- **Unit tiers, upgrade paths, quality caps by rank.** Quality is a set of names (§2.3).
- **A war-weariness meter.** Hands, larders, scars and dead named persons already say it four times.
- **An occupation or unrest system.** A conquered territory is one where compliance computations
  return low numbers (§7).
- **A second resolver for large N.** The battle is the market beating's contest run over sections.
  Two paths is the field's one unsolved twenty-year divergence; not building it is the first option.
- **A "cause of death" field.** Cause is a claim, per person, or the 1218-AG revelation is not
  expressible (§8).

---

## 11. Refinement of the spine (flagged, not silent)

The substrate calls office "a mark plus a binding power, held by a person, revocable." §6.3 narrows
*binding power* to **observed compliance held in other persons' ledgers** rather than a stored
capability. That keeps office revocable, keeps the write path on persons, and adds no container
state — but it makes one substrate sentence mean something more specific than it says, so it is
flagged rather than applied quietly.

`strain(n)` (§5.3) superficially resembles the container-level unrest gauge the substrate refuses. It
is derived on demand from person state and stored nowhere, which satisfies that refusal — but caching
it into a field would silently void the substrate, and a later reader should know that.
