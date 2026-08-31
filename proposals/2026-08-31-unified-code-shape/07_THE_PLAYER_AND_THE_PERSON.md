# 07 · THE PLAYER AND THE PERSON — one function, one budget, one camera

## Status: PROPOSED (2026-08-31). **HELD BACK. Nothing here ratifies on merge.**
## Layer: **L3.** This is DELIBERATE (`04` §3), elaborated — and it is the document where the
## throughline stops being a principle and becomes a call signature.

---

## §1 · THERE IS NO PLAYER MODEL

> **The player supplies one Act, for one Person, through the same `choose` every other person goes
> through. There is no player-only mechanism in this shape, and no NPC-only mechanism either.**

| | the player | anyone else |
|---|---|---|
| function | `choose(person, view, sensation) -> Act` | the same function |
| world access | **none** | none |
| budget | one act per season | one act per season |
| attention | a cast and a rank over candidates | a ledger and a rank over claims — **the same mechanism, different fidelity** |
| what they may attempt | `opening_set(person, view)` | the same |
| **the advantage** | **deliberation time, and nothing else** | — |

**This is not asceticism. It is the only arrangement in which the world is worth inhabiting**, because
every advantage the player could be given is an advantage the world's other people do not have — and a
world whose other people are less real than you is a world in which nothing they do can surprise you.

---

## §2 · FIDELITY IS A CAMERA, NEVER A FORMULA

```
played     : the player supplies the Act at each decision point
witnessed  : the engine supplies the Act; the player observes the trace
auto       : the engine supplies the Act; no trace is retained
```

**Identical `resolve`. Identical rolls. Identical seeds.** The fidelity parameter controls **who is
asked to choose** — never **how the outcome is computed.**

> **A code path that computes an outcome without running the same resolver is a second resolver
> whatever it is called, and it will diverge.** A played path is a **process**; a fast path is a
> **formula**; two different kinds of thing cannot be calibrated to agree, only made to agree on
> average — which is why the one surveyed franchise with two resolution paths is also the one with a
> twenty-year unsolved divergence between them.

**And the test that matters is a distribution-shape test, not a mean test.** The right question is
whether `auto` ever produces a result a player who played it out would call **unrecognisable**. **A
passing mean is not evidence.**

**Three invariance properties, and they are what "camera" means concretely:**

| | property |
|---|---|
| **P-A** | the same world, the same seed and the same choices produce the same outcome **at every fidelity** |
| **P-B** | **showing the player a possibility cannot change what happens** — a preview is computed analytically, never rolled |
| **P-C** | **switching fidelity mid-campaign changes nothing about the world**, only about what is retained |

**P-B is the one that gets violated by accident.** A preview that rolls consumes a draw; a consumed draw
shifts every downstream draw; **and then looking at a thing changed it.** Previews are computed from the
distribution, never sampled from it.

---

## §3 · `choose` — the whole of decision

```
choose : (Person, View, Sensation) -> Act
```

**Three arguments and no fourth, and each one is a refusal:**

| argument | what it is | what its presence refuses |
|---|---|---|
| `Person` | the actor themselves — marks, capability, stance, remits | a decision made by an institution |
| `View` | **at most K claims from their OWN ledger** — built, never filtered | a decision made against the world |
| `Sensation` | **exactly two scalars**, computed this step, stored nowhere | a decision made against needs that went stale |

**And the absent fourth argument is the enforcement.** There is no `World` — not masked, not read-only,
not behind an accessor. Every resolver-side Query takes `World` **first**, so calling one from inside
`choose` **fails at the call site for want of an argument.**

### §3.1 `Sensation` — the two scalars, and why there are two rather than four

```
Sensation := (subsistence, standing)
sense : (Person, frozen_world) -> Sensation        # NOT a decision function, so it MAY take a world
```

**The problem it solves is a real gap, not a tidiness one.** Subsistence and standing read *the world*;
needs are pure and never stored; the View is assembled from claims only. **There was no legal path from
a need to the function that uses it.**

**Two scalars, not four**, because **commitment and exposure read the VIEW** and are computed inside
`choose` from what the person already holds:

```
need(p, COMMITMENT):
  for each commit edge (p, prop, degree) with degree > 0:
    u = w(degree)/w(max)  x  stance(p, prop).weight/5  x  unmet(p, prop)
    unmet = 1                                if p's ledger holds NO row unifying with prop
          = 1 - confidence(c) * agree(c, prop)   for the highest-confidence unifying row c

need(p, EXPOSURE):
  for each hazard h that p's OWN ledger names:
    u = clamp(0, 1,  p_hat(h) * loss(h) / worth(p) )
    p_hat  = p's OWN believed probability that h lands           -- ledger rows only
    loss   = EV(opening_set | claims) - EV(opening_set | claims + h)
    worth  = max( EV(opening_set | claims), subsistence_floor(p) )
```

**Rows are RANKED, never summed.** Each edge and each proposition emits its own row and they compete for
the same act slot. **Summing would make a man with six sympathies more driven than a sworn brother**,
which is false about people and false about the setting.

**Three consequences fall out, none authored:**

- **A lie can discharge a need** (`06` §3).
- **The two multipliers are not a double count.** Stance is *what he wants*; degree is *what he has
  undertaken*. A man may hold a stance at maximum with no edge, or an edge at maximum with a decayed
  stance. **The product makes both small and only the conjunction large** — which is the mechanical
  shape of **the sworn man who no longer acts and does not leave either.**
- **Normalising exposure by `worth(p)` is the design decision.** The same seizure terrifies a man with
  one boat and barely moves a duke. **Exposure is structurally the poor person's need and commitment is
  structurally the committed person's**, so the two are not on one scale and neither can dominate the
  other from above.

**`subsistence_floor(p)` is the person's own body and labour, which is never zero while they live** —
without it the denominator vanishes at the exact bottom of the ladder, which is where the design must
work hardest.

> **A Sensation is un-nameable, therefore undisputable.** No person can hold a claim about another's
> hunger. **Claims reach the larder and the body, and stop there.**

### §3.2 `opening_set` is BELIEF, and that is the whole of discovery

```
opening_set : (Person, View) -> Act[]        # person-side Query: takes no World, ever
```

**A person may attempt what is not in fact available.** The harbour silted last season; nobody told the
merchant; he declares a shipping act; **it resolves as a discovery.**

> **THE INTERFACE MUST NOT GREY OUT A REMOVED VERB.** `opening_set` is belief and `verbs(w, site, c)` is
> truth, and **an interface that greys out the second has handed the player the world's state.** That is
> omniscience re-entering through the one door the signatures cannot close.

---

## §4 · THE ACT ECONOMY — one act, universally, and why it is the whole political economy

> **ONE ACT PER PERSON OR COHORT PER SEASON. UNIVERSALLY. No office, rank or holding changes it, ever.**

**An act is the one discretionary commitment.** Subsistence, craft and travel-in-progress happen *to* you
at MATTER. A standing date firing is CALENDAR. `witness` is WITNESS. **None is an act.**

**The fork was false because one word was doing two jobs:**

| | scarce how? |
|---|---|
| **personal attention** — what you do with your season | **identically at every rung.** A Duke has the same hours as a fisher |
| **institutional throughput** — what your office does | **scales with the establishment, not with the holder** |

> **If the POOL for an act by remit comes from the establishment, the ACT does too.** The design already
> moved the dice off the holder and left the act on him. Moving both is the whole ruling.

```
acts in an office-holder's season
   = 1                                              # his own, exactly like the fisher's
   + | { m in establishment(o) : m's own choose selected an act serving the office } |
```

**The second term is not his to set. It is nine other people's answer**, and he learns it the way he
learns everything else — as claims deposited by their tellings, **coarse where he has nobody.**

**Why they mostly serve, with no standing-order object and no loyalty stat:** `upkeep` fills an
establishment member's larder from the office's stake, so **his own `need(subsistence)` is answered by
the post and threatened by failing it**; his `need(standing)` runs among his siblings-in-establishment;
his stance toward the holder is an ordinary row. **He does his job because his own computed needs say
so — which means he can stop**, and the design already told us what that looks like: *an unpaid
establishment does not disperse; it becomes a faction and treats plunder as wages.* **Under this rule
that sentence is produced by construction rather than asserted.**

**`dispatch` costs BOTH parties an act, and names ONE person.** A holder may redirect exactly one of his
people, per season, **and may be refused.** Everyone else on his roster does what their own view says.

**An order is a telling, and compliance is the hearer's own `choose`.** `issue` is one act; what happens
next is nine people's acts, through the same compliance machinery built for subjects. **That is the
post-Secession Crown's actual problem, obtained without writing a loyalty stat.**

**The Duke's leverage was never more hours.** It is that **his one act moves other people's acts.** A
fisher's act moves a boat; a Duke's `dispatch` moves thirty-five seasons. **Same allowance, incomparable
reach.**

**And the cohort exploit is priced rather than forbidden.** Individuate your cohort to farm acts and you
get eleven **persons** — each with a ledger, a stance toward you, needs of their own, and the ability to
refuse. **You did not buy eleven acts; you created eleven people who might hate you.** No rule forbids
it and none needs to — **which matters, because a special case is a forbidden shape.**

**One allowance: the act. One cap: items a sitting processes.** `seat_items` and `capacity(date)` were
one quantity seen from two sides, which is why the second was found **double-counted**.

---

## §5 · THE PERSON WITH NO POST — the design's real test

> **A person holding no office can act, petition, investigate and receive an opportunity. Office changes
> whether a decision BINDS OTHERS — never whether you may act.**

**This has a falsifier that runs** (`12_TESTS.md`, T3), and it is the one criterion the executing tree
fails today for a reason that is not subtle: **there are no people in it at all.**

### §5.1 What an ordinary person holds that is scarce — and it is not skill

**Measured across fifty-five characters and six independent season lanes**, three things predict a rich
season and three things do not.

| **predicts nothing** | **predicts everything** |
|---|---|
| rung | **mode count** — every rich character cites three or more live modes, or four differently-shaped acts |
| office (it points slightly the **wrong** way) | **an empty establishment, never a small remit** — the largest remit in the setting has the thinnest reach |
| caste exclusion | **a channel, a custody, a gate, or a unique root** — everyone holding one is rich; everyone holding none is thin |

> **Dominance, not scarcity, is what makes a season thin.** A character with one act that is always
> right has nothing to decide; a character with four differently-shaped acts has a season.

**And one non-monotone finding nothing in the design anticipates:** the deep informal channel is gated
**at both ends**. Below the gate you cannot hold it at all; far above the rendering floor **you hold
content nobody can receive.** The most sensitive person alive and the least sensitive are both
structurally inaudible, **for opposite reasons.**

### §5.2 The floor — the most important defect in the play-space measurement, and its fix

**The control character — an unremarkable person with no marks, no rank, no office and no alignment —
measured THIN, for two mechanical reasons:**

1. **Ordinary capability was an empty verb set, not a smaller pool.** Verbs gated on a practice rank, so
   a person holding none got **no acts** rather than worse odds at the same acts.
2. **An unmarked person was inaudible in both directions**: their acts did not propagate and news did not
   seek them.

**Both fixes are subtractions.**

```
EDIT 1 — rank supplies dice, and gates no verb.
   Every act formerly "added at rank 3" folds back into its base act as a declared STANDARD
   that anyone may declare and almost nobody can meet. THE ACT VOCABULARY GETS SHORTER.

EDIT 2 — publicity and attention read the STANCE TABLE, not the actor's marks.
   referents(act) = marks(actor) + { proposition(act) } + objects touched + { place }
   act_salience(act) = 1 + 0.2 x |{ r in referents : some hearer holds |valence(r)| >= 3 }|
   publicity(act)    = venue_factor x sqrt(witnesses) x act_salience(act)
   theta(p, act)     = theta(p) / (1 + 0.2 x |{ r in referents : |stance(p,r).valence| >= 3 }|)
```

**One change, two directions, and both are the removal of a special case:** publicity was reading **one
referent kind out of four**, and attention was reading **none**.

**Worked, and the first case is the fix arguing against itself.** The control's most private act — she
fosters a child to kin — touches referents nobody holds a strong stance toward. `act_salience = 1.0`;
publicity falls below the floor. **The most consequential act of her life still reaches nobody, and if it
did not, the fix would be a notability stat in disguise.**

**Her telling about the ford is the other case.** It touches a contested proposition, a named man and a
disputed place — **three strong referents**. `act_salience = 1.6`; publicity reaches the top band.
**The unmarked woman is heard across the town, because of what her act was ABOUT and not because of who
she is.**

**And the price arrives with the audibility, out of the same term.** The magistrate who hates the
subject is inside that band too. **She does not get amplification; she gets exposure** — because judging
sets deposit divergently by construction, the same publicity that carries one man's approval carries the
magistrate's hostility, **and hands a woman previously beneath notice a named enemy holding an office.**
No new cost mechanism was needed: **publicity was never a gain. It is an amplifier of an act's own sign.**

**The caste effect the original term existed for is unharmed** — a stigmatised person's transgression
still travels twice as far as a neighbour's, because the mark is a referent half the region holds a
strong stance toward. **It enters the sum as a mark, in the first clause, unchanged. What changes is that
a mark is no longer the only way in.**

> ⊕ **AND IT CORRECTS A SELECTION PRESSURE NOBODY DESIGNED.** Under the old term, an ordinary person's
> only route to publicity was **witness count and venue** — a crime in a square. **The cheapest way to
> stay a person was to do something people talk about, and what people talk about is transgression.**
> Under this one, **charity at the granary during the reckoning is as audible as theft from it**, because
> both touch the same contested proposition. **The selection pressure goes to neutral without anyone
> adding a rule about virtue.**

### §5.3 The blocked core — a rich option set against an unreachable want

**Nineteen of fifty-five characters had live acts and a stated want with no act whose object it was, and
eleven of the nineteen scored RICH.** A rich option set against an unreachable want was **the single
most common result of the measurement.**

> **It is not a balance problem. It is what happens when a design specifies HOW people act with great
> care and never checks that the things they are canonically trying to do are REACHABLE BY ANY ACT IT
> DEFINES.**

**And the sentence that joins this to the narrative layer:**

> **A blocked core does not stop an arc from running. It stops it from TERMINATING.**

Twelve of one lane's twenty-two arcs run on such a character. **Combined with the threshold refusal
(`06` §6), the result is arcs that continue indefinitely** — and that is why the disposition matters more
than its small backlog suggests.

**The honest sizing, after adjudication:** of nineteen, **ten are the design working** (the want is out
of the character's power, and that is correct and interesting), **one is a canon artefact**, **three were
already answered by standing rulings**, and **the genuine backlog is four characters behind three small
edits — three of which widen an existing field and one of which drops a precondition. Zero new objects.**

**The rule this yields, and it belongs in the shape rather than in a report:** for every character whose
want is unreachable, **either supply an act whose object is that want, or state explicitly in canon that
the want is unreachable. Do not leave it implicit — that is how a rich option set hides an unplayable
character.**

---

## §6 · WHAT THE PLAYER ACTUALLY TOUCHES

| surface | what it is | what it is NOT |
|---|---|---|
| **the slate** | 4–9 candidates, cast then ranked, per season | not everything that happened; **about 3% of it** |
| **the response set** | 3–5 responses per situation, from the resolver's **declared** option set | not a generated menu; a candidate cannot invent a response |
| **the act** | **one**, per season | not a turn's worth of actions |
| **the view** | at most `K` claims, ranked by salience | not the world; **not a blurred world either** |
| **inputs** | **published** — which channel carried an item, what a roll's factors were | — |
| **the trigger** | **hidden** — scores, thresholds, budget arithmetic | — |

**Publish every input; never publish the trigger.** A player must be able to reason about **what they
lack** — *I have no one in that province, so I hear nothing from it* — without being handed the
threshold that would tell them what the world is about to do.

---

## §7 · WHAT THIS DOCUMENT REFUSES

| refused | because |
|---|---|
| a player-only mechanism of any kind | there is no player model; a player is a person |
| an NPC-only mechanism of any kind | the same rule, in the direction people forget |
| a fast path, an auto-resolve formula, a summary resolver | fidelity is a camera; two kinds of thing cannot be calibrated to agree |
| a preview that rolls | it consumes a draw and shifts every downstream draw — **looking at it changed it** |
| more acts for the powerful | scarcity at every rung is what makes the low end playable **and** the high end political |
| a flat modifier from anyone onto anyone's roll | worth `X / (0.800 x sqrt(Pool))` — **backwards** |
| greying out an unavailable verb in the interface | hands the player the world's state through the one door the signatures cannot close |
| a rank gate on a verb | a second class gate in a design that declares exactly one |
| a notability or fame stat | publicity is an amplifier of an act's **own sign**, computed from what the act is about |
