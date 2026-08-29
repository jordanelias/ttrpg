# 08 — Argument, Debate, and Negotiation

## Status: PROPOSED (2026-08-29) — a from-scratch design. Nothing here ratifies on merge.
## Composes on: `01_substrate.md` §3 (claims), §4 (judging sets, offices), §5 (petition, dispensation), §5.3 (standing dates)
## Coordinates with: document 06 (dispensations, treaty breach) — this document produces the *promise* to issue one; 06 owns the issuing and the breach.

---

## 0. The null this document sits on, and where I am inventing

No game models the content of an argument. Burning Wheel abstracts a debate to a scalar Body of
Argument and lets the fiction carry the content; Ace Attorney reduces a trial to one correct
evidence-to-contradiction pair; Victoria 3 substitutes faction arithmetic; Diplomacy declines to
model negotiation at all and is the better for it, because it has players' mouths and we do not.
**We have no GM and no table.** Nothing can be left to the fiction. So the material is historical,
not ludic, and I will say plainly what is adapted and what is invented:

| Component | Adapted from | Invented here |
|---|---|---|
| Stasis ladder as the spine of tactics | Hermagorean stasis theory (fact / definition / quality / jurisdiction) | that descending it **irrevocably concedes** everything above, and that the rung reached **is** the compromise scale |
| Force-close on a named fault | Nyāya *nigrahasthāna*, 22 enumerated defeat conditions | the severity tiers (`strike` / `descend` / `close`), and binding fault 11 to Coherence |
| Graded proof, articles separately proved | the *ordo iudiciarius* | the grade table's derivation **from the substrate's claim sources**, so grade is computed, never authored |
| Scaled compromise | Burning Wheel's Duel of Wits | nothing — I take the rule whole and bind it to the ladder |
| Recorded defeat | *senatus auctoritas* | that a recorded row is an **instrument** and therefore enters later sittings at proof grade G4 |
| Cheap talk as the default | Diplomacy's total absence of enforcement | the binding-instrument menu and its pricing |
| Negotiation as a venue | **nothing. This is invention.** | the reservation set, the *read* of the reservation set, and the fact that a proposal is a telling |

Everything else below is derived from `01_substrate.md` and does not need a precedent.

---

## 1. What an argument is made of

### 1.1 The proposition is already in the substrate

A faction is a proposition plus a commitment map; a petition carries one; a dispensation carries one.
Same object, and this document adds no new one:

```
Proposition = (mood, subject, predicate, value, when, scope)
    mood ∈ { HOLDS, OUGHT }
```

`HOLDS` is claim-shaped without the epistemic fields — *the levy of Grauwald was paid in full, in the
twelfth season*. `OUGHT` names a change in a container's terms — *the fine on Greta of the Einhir
hamlet ought to be remitted*. `when` is a mandatory interval, exactly as in §3's claim identity, so
**assertion and denial collide automatically** and I never need a rule for "these two people
disagree."

### 1.2 A case

An argument is not a scalar and it is not a hand of cards. It is:

```
Case   = (holder, motion, rung, grounds[])
Ground = (proposition, warrant, support[])           # support[] are claim ids from holder's ledger
Motion = (proposition, venue, mover)
```

A **ground** is a proposition offered in support of the motion, plus a **warrant** — the named
inference linking one to the other. Warrants are a closed set of six, because an open set is free text
and free text is a GM:

`instance-of` · `caused-by` · `same-as-precedent` · `authority-said` · `if-then-by-terms` · `absence-implies`

`support[]` are **ids of rows in the holder's own claim ledger**. That is the whole attack surface,
and it is why this design is possible at all: the substrate already made every claim carry
`(source, confidence, when)` with no null source. **An assertion in a chamber is a claim being told to
a room** — `tell(speaker, judging_set, claim, as_asserted)` — so a ground is attackable in exactly the
three places a claim is: its root, its independence, and the gap between what the speaker holds and
what he asserted.

- Closed loop: produced by a person assembling grounds from their ledger under §3.1's salience
  budget; carried as an act (`plead`) at a venue, which deposits claims into every attendee's
  ledger; consumed by the venue's disposition function and by the record.
- **Cut it and you lose:** any argument whose content matters. The debate collapses back to a pool
  contest with flavour text, which is the null this document exists to fill.

### 1.3 What a chamber does not have

A venue holds no opinion. Per §4, containers hold stakes, judging sets and dates and nothing else. A
motion's disposition is a count over **persons**, each computing from **their own view** (§3.1), each
weighing the proposition by their own stance. This is what makes §9's refusal honourable: the side
with worse evidence often wins, because evidence is one input and stance is another.

---

## 2. Stasis as terrain

Before choosing a tactic, a party diagnoses **what the fight is about**. Four rungs, strongest first:

| Rung | Name | The assertion | What it attacks | What it concedes |
|---|---|---|---|---|
| **1** | **Denial** (fact) | it did not happen | the opposition's grounds' **provenance** | nothing |
| **2** | **Definition** | it happened; it is not *that* | the opposition's **predicate** | the act occurred |
| **3** | **Quality** | it happened, it is that, and it was right | offers a **counter-ground** | the act, and its label |
| **4** | **Jurisdiction** | this chamber may not hear it | the venue's **admissibility** | the act, the label, and (usually) that it was wrong |

**Descending is irrevocable and public.** A party begins at the highest rung it is willing to hold.
`descend` moves it down exactly one rung, and everything above the new rung is written into the
record as **conceded**. You cannot go back up in the sitting, and — because the concession is a
record row — you cannot go back up in a *later* sitting either without triggering fault F2
(contradicting your own record).

This is why the ladder is terrain and not a menu. Rung 1 is strongest and most brittle: hold it and
you must survive every challenge to your denial. Rung 4 is nearly always available and nearly always
worth almost nothing, because arriving there has already given away the substance — a party that opens
at rung 4 has conceded the case to buy a delay until the next standing date, which is sometimes
exactly the right trade. That is the fork.

- Closed loop: produced by the party's own `choose(person, view)` at the sitting's open and at each
  `descend`; carried on the case and, on close, into the record row; consumed by the concession
  calculation (§5) and by every future sitting that cites the row.
- **Cut it and you lose:** an option space about the *content* of a disagreement. Without the ladder,
  the only differentiation between debate tactics is how hard they hit, which is the refused design.

---

## 3. Defeat by named condition

Resolution is by **named fault against a checklist**, not by a persuasion threshold. Every fault is
computable from the case state and the ledgers — none requires a judgment call, which is what lets this
run headless (§11).

Severity: **`strike`** (the offending ground is struck and cannot be re-pleaded, at this venue or any
other, by anyone), **`descend`** (the faulting party is forced down one stasis rung immediately, with
all the concession that implies), **`close`** (the sitting force-closes against the faulting party at
whatever rung it currently occupies).

| # | Fault | Trigger, computed | Severity | Cost of removing it |
|---|---|---|---|---|
| **F1** | **Self-contradiction** | a pleaded ground's proposition collides (same subject-predicate, overlapping `when`, opposed value) with one you asserted or conceded earlier in this sitting | close | a party could hold two incompatible positions and be scored on the better one; the ladder stops meaning anything |
| **F2** | **Contradicting the record** | as F1, against a record row in which you are named | descend | recorded defeat becomes inert; nothing accumulates across sittings |
| **F3** | **Silence when pressed** | you were `press`ed on a ground and spent an exchange without answering | close | evasion becomes free and every sitting runs to the exchange budget |
| **F4** | **Shifting the ground** | your answer's proposition does not overlap the challenged one on subject **or** interval | descend | the *cheapest* dodge in the game becomes the best one |
| **F5** | **Repetition** | re-asserting an answered ground with no new `support[]` | strike | the exchange budget can be burned by restating, which advantages whoever has more to lose from a close |
| **F6** | **The quibble** | your challenge turns on an equivocation of the predicate rather than the value — formally: your attack would still stand if the opponent's `value` were reversed | close | this is the self-gate. Remove it and cheap tactics need a rule *each*; keep it and they are disciplined by one line |
| **F7** | **Rootless ground** | challenged at provenance, the ground's `support[]` bottoms out in a synthetic rumour root (§3, one story told three times corroborates once) | strike | common voice becomes proof and the grade table is decorative |
| **F8** | **Conceding and pressing anyway** | you admit the opponent's decisive ground while still moving your motion | close | "agree with everything and win anyway"; the concession loses its price |
| **F9** | **Deficient pleading** | you pleaded fewer grounds than the motion type requires, each separately proved | close | the *ordo*'s articles collapse into one omnibus assertion, and one strong claim carries an arbitrarily large motion |
| **F10** | **Speaking without standing** | you are not in the judging set and hold no leave from a member | strike | jurisdiction stops being a real rung |
| **F11** | **Incoherent assertion** | the speaker's Coherence band is Fractured or Severed | strike (all his grounds) | Coherence stops having a social consequence and becomes a Thread-only stat; also the setting's own claim that Coherence indexes commensurability goes unmodelled |
| **F12** | **Inadmissible challenge** | you press an attack the venue's admissible-proof table does not permit (e.g. impeaching an Archives register in the Doctrinal Dicastery) | descend | venue difference becomes cosmetic; five chambers become one |

**Force-close is the normal ending.** A sitting that runs its full budget without a fault is the
*unusual* case. Most arguments end because somebody was caught doing something that has a name.

- Closed loop: produced by the fault check run after every exchange act; carried into the record row
  as a named fault against a named person; consumed by the disposition, by the concession scale, and
  by every judging-set member's stance toward the faulting person (being caught in F6 costs regard
  with anyone who values Honor or Precedent, and costs *nothing* with the Restoration).
- **Cut it and you lose:** the only resolution in the design that is not a die roll. A threshold roll
  cannot distinguish "he was wrong" from "he was caught lying," and the second is the interesting one.

---

## 4. Graded proof

### 4.1 The grades are computed from claim sources, not authored

Grade is a pure function of the substrate's claim fields. Nothing hand-assigns it.

| Grade | Name | Computed from | Attackable by |
|---|---|---|---|
| **G5** | **Notorious** | a majority of the judging set's own ledgers already hold this proposition with a firsthand root | nothing. Do not attack it; you commit F12 |
| **G4** | **Instrument** | a claim rooted `firsthand(read_of(object))` where the object is a record held in a declared custody | attacking the **custody chain** — i.e. forgery, substitution, or an unattested copy |
| **G3** | **Corroborated** | ≥2 claims whose **firsthand roots differ** (§3's independence-by-ancestry) | breaking one root, or showing the roots are the same root |
| **G2** | **Witnessed** | one claim, `firsthand`, high confidence | the witness's vantage, marks, or stance |
| **G1** | **Told** | `told_by(person, …)` with a findable root | the chain — each `told_by` hop is a person who can be produced, or cannot |
| **G0** | **Common voice** | synthetic-root rumour: many retellings, one root | nothing needs to attack it; it is below most floors. It is *admissible* on questions of reputation and motive |
| **G−** | **Inferred** | `inferred(c₁…cₙ)` → `min(grade(cᵢ)) − 1` | attacking any parent, or attacking the warrant |

**The instrument derivation matters and is not a new object.** Reading the Kettlemakers' register
deposits `firsthand(the register says the fee was paid)` — *not* `firsthand(the fee was paid)`. The
root is about the object, never the underlying fact. Forgery therefore needs no mechanic: a fabricated
edict which, uncontested, reads as genuine until discovered is what you get free when the only route
from a document to a fact is a custody claim that can itself be false. It is also why **the Church's
archival monopoly is the largest single power in the game and needs no rule saying so** — the
Dicastery of Doctrine and Archives holds custody of the instruments everyone else's G4 grounds rest on.

### 4.2 Articles are separately proved

A motion declares a **required article count** — distinct grounds that must *each* independently reach
the venue's floor. A settlement court's fine-remission motion requires 1; a Doctrinal Adjudication 3;
a Crown Succession Contest 5 (descent, deed, consecration consent, no prior conceded record, the
cognatic-senior capacity test). Failing the count is F9; pleading one magnificent ground and two weak
ones fails on the weak ones, because **grade does not average**. That is the *ordo* rule, whole.

- Closed loop: produced by claim-source arithmetic at plead time; carried on the ground; consumed by
  the admission floor, the disposition, and the record row (a struck ground is struck permanently).
- **Cut it and you lose:** any reason to *investigate*. Field investigation (T9) pays out here or
  nowhere — the only thing an investigation produces is a claim with a better root, and grade is what
  converts a better root into political force.

---

## 5. Both outcomes bind

**The winner concedes in proportion to how much of his own position was destroyed** — and this design
already measures that, because it is the stasis rung.

```
concession(winner) = rungs_descended(winner) / 4
```

The motion carries, and the venue simultaneously issues a **rider** amending the motion's `OUGHT`
proposition and scaling the thing allocated:

| rungs descended by the winner | disposition |
|---|---|
| 0 | motion carries whole |
| 1 | carries, with the loser's strongest surviving ground admitted as a proviso |
| 2 | carries at half the stake; the other half is deferred to the next standing date |
| 3 | carries in name only — the terms change, the stake does not move this date |

One rule, not a subsystem. It converts "both roll, one wins" into "both outcomes bind," and it is why
being driven down from rung 1 is materially worse than opening at rung 2 and holding — the tactical
texture the ladder was built to produce.

- Closed loop: produced at close from the case's rung history; carried as the rider clause on the
  disposition; consumed by document 06's dispensation issuance and by the stake allocation at the
  standing date.
- **Cut it and you lose:** any reason for a strong party to argue carefully. Losing costs nothing
  extra, so the dominant play is to open at rung 1 always and shrug.

---

## 6. Recorded defeat

A record row is written for **every** sitting, at close, in these dispositions:

`CARRIED` · `FAILED` · `CARRIED-WITHOUT-FORCE` · `WITHDRAWN` · `CLOSED-ON-FAULT`

**CARRIED-WITHOUT-FORCE** is the *senatus auctoritas*: a motion that got its majority and was then
vetoed, blocked, or issued into a container whose office-holder refused to publish it. **It changes no
terms.** It is fully citable. It is nearly free, and very few games have it.

What it buys:

1. A ground supported by a carried-without-force row enters a later sitting at **G4** — it is an
   instrument, in custody, and its content is *the room agreed*. Not *the thing is true*; the room
   agreed. That distinction is the whole of its honesty.
2. The person who vetoed it is now named in a record row that says he opposed the proposition. Every
   later position he takes runs the **F2** check against it. Vetoing is therefore not free: it banks
   a permanent contradiction hazard against the vetoer's own future arguments.
3. The `pattern` counter (§7.2) increments. A proposition carried-without-force four times is a
   different political object from one raised once, with no decay timer anywhere.

**Compliance with §6 of the substrate, which refuses container memory and world logs agents read.**
The record is not a mind and not a log. It is an **object in the world, in someone's custody** — the
parliament's minute-book, the praefect's roll, the guild register, the Dicastery archive. Knowing what
is in it is a claim in a person's ledger, deposited by `read_of(record)`, which is an act that can be
refused, delayed, or forged. Records burn. Same shape as the granary's grain: a container holds a
stake, not an opinion.

- Closed loop: produced at every sitting's close by the venue's clerk (a named person holding the
  custody office); carried as an object at a place; consumed by `read_of` → a claim → a G4 ground, and
  by the F2 check.
- **Cut it and you lose:** politics with a past. Every sitting starts from zero, a defeated
  proposition evaporates instead of becoming ammunition, and there is no way for an outnumbered party
  to *bank* anything.

---

## 7. What may be argued about

### 7.1 The motion must be somebody's

**Admissibility test at plead time, all three required:**

1. **Held.** Some person holds `motion.proposition` at nonzero stance. The mover need not be that
   person — an advocate may carry another's proposition, as a carrier carries a petition — but a
   proposition nobody holds cannot be moved. No free-text pretexts.
2. **Rooted.** At least one ground's `support[]` has an ancestry terminating in a `firsthand` root,
   i.e. in an occurrence. A motion built entirely from inference and common voice is inadmissible
   everywhere except a Restoration cell, which declares the opposite floor.
3. **Ripe.** Below.

The first two are T7: a motion is a proposition someone holds, traceable to something that happened,
brought before a date at which a prize is allocated.

### 7.2 Freshness without a decay timer

The failure to avoid: a thirty-season-old grievance being exactly as motionable as yesterday's breach.
The trap to avoid: a decay timer, which makes politics forget, which is false about politics.

**Freshness is not a property of the grievance. It is a property of the coupling.**

```
ripe(motion, sitting) ⟺ ∃ chain of shared subjects from motion.proposition
                        to the prize being allocated at sitting.standing_date,
                        of length ≤ venue.coupling_depth
```

The tithe reckoning allocates the tithe. A thirty-season-old breach of the salt terms is not motionable
there **as a motion**; it is fully admissible there **as a ground**, at full grade, supporting a motion
about *this* reckoning, if a chain of shared subjects reaches it. Old material never weakens. It needs
a hook, and a hook is an occurrence sharing a subject.

And the counter-move to decay: **revival compounds.**

```
weight(ground) = grade(ground) × (1 + 0.25 × pattern(subject))
    pattern(subject) = record rows sharing this subject in which the mover's side did not prevail
```

A grievance raised and refused four times, then coupled to a fresh occurrence, is *stronger* than a
fresh one of the same grade, because the record shows a pattern and the judging set can read it. That
is the suppression rule inverted into a virtue: what an institution refuses to hear it makes heavier.

**R check on this fork.** Banking recorded defeats has *compounding* gain and *one-time* cost (regard
lost for pressing a motion that fails, plus the permanent burn of every support-ref that gets struck).
Pressing now has *immediate* gain and *compounding* cost (the pattern counter runs against you too if
you are the side that keeps refusing). Neither shape dominates: banking is worthless if no hook ever
appears, and every banked row is evidence a struck claim can never be re-pleaded. The fork is real.

- Closed loop: produced by the substrate's standing dates plus subject-sharing between propositions;
  carried nowhere (recomputed at plead time); consumed by admissibility and by ground weight.
- **Cut it and you lose:** either a world where nothing ages (every grievance permanently live, so the
  slate is unreadable) or a world that forgets on a clock (so injustice has a half-life, which is the
  falsest thing the design could say).

---

## 8. Negotiation

Designed nowhere before. **It is the same mechanic with different venue parameters**, and I will not
build a second one.

```
Venue(negotiation) :
    container       = none (private)      judging_set   = the parties themselves
    decision_rule   = unanimity           veto_holders  = both
    prize           = a draft instrument   admission_floor = G1
    record_custody  = none, unless a binding instrument is executed
```

### 8.1 Where clauses come from

A **clause** is an `OUGHT` proposition naming a change in the *other* party's terms — exactly a
dispensation the other side would have to issue (document 06 owns the issuing). Clauses are not chosen
from a list; they are **generated from computed needs**. §2's needs routine already produces, each
tick, the gap between a person's situation and what their own acts can reach, and every unmet need
whose closure requires an act by someone outside your reach is a candidate clause. A hearth short of
grain generates a clause about the granary; a cadet with no inheritance generates one about an office.
Nobody authors a negotiation topic.

### 8.2 The counterparty is not an obstacle number

Each party has a **reservation set** — the set of clause-bundles they would accept, computed from
their needs, their stances, and their alternatives (what they get if talks fail). It is never seen by
anyone, including themselves as a set; it is evaluated on demand against a specific bundle.

What a negotiator actually acts on is a **read**: claims in their own ledger of the form

```
(other_party, would_accept, clause_bundle, when, source, confidence)
```

sourced from tellings, from prior sittings' record rows, from what the other side conceded on the
stasis ladder in some earlier chamber, and from **inference off marks** — which is where caste does
its quiet damage, because inferring a Southern Einhir counterparty's reservation set from their marks
is exactly how a Crown negotiator gets it wrong.

**A read can be wrong, and nothing corrects it except collision** (§3.2). There is no cap: a
negotiator who believes the Löwenritter can be bought will spend the whole negotiation offering money.

### 8.3 The exchange

Alternating acts, budget set by the venue:

| Act | Effect on primitives |
|---|---|
| `propose(bundle)` | **deposits claims into the other's ledger** about your position. Offering is informative and therefore costly |
| `counter(bundle)` | as above, plus refuses the prior bundle, which deposits a claim that it is outside your reservation set |
| `press(clause)` | demands an answer on one clause; F3 (silence) applies here as in any sitting |
| `probe(clause)` | you name a clause you do *not* want, to learn its price. Cheap, but it deposits a false claim about your position — a lie, rolled against their credulity and their stance toward you, catchable |
| `withdraw` | ends talks; deposits into their ledger a claim about where your reservation set lies; forecloses re-opening before the next standing date |
| `execute(instrument)` | closes with a binding instrument (§8.4) |

Concession patterns are readable because each proposal is a telling. A party that moves three clauses,
then one, then none has told the other side where its floor is, whether it meant to or not.

### 8.4 Cheap talk is the default

**An accord binds nothing.** It is a pair of intentions, at best G2 (one witness each), with record
custody *none*. Breach costs only what it costs the breacher's regard with those who learn of it —
which may be nobody. That is the Diplomacy steal, and the reason the strategic layer has tension.

Binding is an **expensive exception**, and every instrument is expensive because it costs a real thing:

| Instrument | Cost | What it converts breach into |
|---|---|---|
| **Hostage** | a person's containment address moves. Their hearth loses a member, their needs change, they can be killed | breach is instantly notorious (G5) and the hostage's fate is a fresh occurrence |
| **Consecration** | the Temporal Affairs Dicastery attests; the Church acquires a lever over both parties, and both acquire an obligation to the Church's proposition | breach becomes motionable in the **Doctrinal Adjudication Dicastery**, at floor G3 |
| **Sealed record at a venue** | the accord becomes an instrument in a named custody; both parties are named in a record row and carry the F2 hazard forever | breach is a G4 ground at that venue's next standing date |
| **Bond of holdings** | a hearth's holdings are pledged; the larder shrinks immediately | breach transfers the holding by the venue's ordinary allocation, no new mechanic |
| **Marriage** | two hearths' succession pointers are edited | breach cannot be undone; the tie persists into the next generation |

That table is why Princess Elske's marriage to Doux Alexios Laskaris is a *binding instrument* and the
Almud–Schoenland trade opening is *cheap talk*, and why the second keeps wobbling while the first does
not. Nothing about either was scripted; they are two rows of the same table.

**And why the Restoration Movement cannot be treatied with**: its cells have no record custody and no
office-holder whose decision binds a member (§4 — office is the thing they refuse). No instrument in
that table is executable by a consensus cell except a hostage or a marriage, both of which are
person-level. This is an ideological commitment producing a mechanical fact, with no rule naming the
Restoration.

- Closed loop: clauses produced by computed needs; carried as proposals, which are tellings into the
  counterparty's ledger; consumed by the counterparty's reservation evaluation and, on execution, by
  document 06's dispensation issuance.
- **Cut it and you lose:** every agreement in the game becomes automatic and every alliance becomes a
  set membership. The counterparty stops being a person and becomes a difficulty number, which is the
  precise failure this lane was told to repair.

---

## 9. The playing surface

### 9.1 Every manoeuvre alters a primitive

The refusal is exact: *a manoeuvre must alter a primitive, not just apply a formula.* Duel of Wits
players converged on two moves and stopped, because the moves differed only in output size.


| Manoeuvre | The primitive it alters | Persists outside the sitting? |
|---|---|---|
| `plead(ground)` | deposits claims into every attendee's ledger | **yes** — permanently, in everyone present |
| `strike_at_provenance(support_ref)` | if it lands, the claim is **struck**: nobody may plead it again, anywhere, ever | **yes** — globally, forever |
| `press(ground)` | consumes the opponent's exchange and arms F3 | no, but it is how faults are caused |
| `descend()` | concedes a rung into the record, irrevocably | **yes** — F2 hazard forever |
| `produce(instrument)` | a physical object enters the room; its custody becomes attackable | **yes** — the object is now known to exist |
| `object_to_venue()` | attempts to move the sitting to a different container's standing date | **yes** — changes which judging set decides |
| `yield(rung)` | offers a concession to close early at a known price | **yes** — the rider binds |

Not one of them is "deal 3 damage to the Body of Argument." There is no Body of Argument.

### 9.2 What happens when the sides are not close

Any manoeuvre layer at a large gap degenerates to *the bigger number wins fast*. So the layer switches
itself off:

```
if  |best_grade(A.decisive_ground) − best_grade(B.decisive_ground)| ≥ 3
    → the sitting DISPOSES IMMEDIATELY, no exchanges, at concession 0.
```

A Free Master with the guild's sealed register (G4) against a challenger with common voice (G0) does
not get a debate. He gets a ruling, and the loser gets a record row. **The rich option space earns its
complexity only while the sides are close**, and this is the line that says so. The consequence is
that the interesting political work is not in the chamber — it is in the field, getting your decisive
ground from G1 to G3 before the standing date. That is T9 paying rent.

### 9.3 The two refusals I am honouring explicitly

**Contradiction-matching is not the primary resolution.** Striking provenance is powerful and is not
the win condition. The disposition is a count over the judging set, each member deciding from their own
view under §3.1's salience ranking, in which *stance weight* is a multiplicand — so a member who wants
the motion surfaces the ground supporting it and not the one refuting it, and no rule needs to make him
dishonest. **In a political trial the winner is often the side whose evidence is worse**, and that is a
consequence of the substrate rather than a fudge.

**No relationship modifier large enough to dissolve structural conflict.** Regard toward the mover is
one term in a member's decision. The **admission floor** is not a term at all: a ground below the floor
is not discounted, it is not weighed. Affection cannot buy a G0 into the Doctrinal Dicastery. Some
conflicts must be positional and unbuyable, and the floor is where that is enforced.

---

## 10. The chambers

One mechanic. A venue is a parameter row. **There are no five special cases.**

```
Venue = (container, prize, standing_date, judging_set_rule, decision_rule,
         admission_floor, privileged_custody, exchange_budget, article_count,
         coupling_depth, veto_holders, record_custody)
```

| Venue | Judging set | Decision rule | Floor | Privileged custody | Veto |
|---|---|---|---|---|---|
| **Hafenmark Court Parliament** | seat-holders present | majority of seats | G2 | Crown instruments | the Duchess → `CARRIED-WITHOUT-FORCE` |
| **Doctrinal Adjudication Dicastery** | the Cardinal + assessors | the Cardinal's determination, all articles ≥ floor | **G3** | Doctrine & Archives registers only | the Confessor |
| **Kettlemakers' Masterpiece Examination** | Free Masters present | majority | G4 **on the work**, **G0 on the candidate's fitness** | the guild register | the Warden |
| **Goldenfurt settlement court** | praefect + assessors drawn from each community's judging set | praefect determines; assessors' stances weight it | G1, with oath-helping (n independent G1 roots → G3) | the praefect's roll | none |
| **Restoration consensus cell** | every member present | **no sustained objection** — one member blocks | **G0** | none | everyone |

Read the third row again: **the Masterpiece Examination admits common voice on the candidate's
fitness.** That one parameter is how caste is reproduced by an institution rather than by malice.
Nobody wrote a caste rule. The Row's Free Masters hold stances; those stances *are* what common voice
about a Southern Einhir candidate is; the floor lets it in. Change the Free Masters and it changes;
change the floor and it changes. A per-venue gate is a per-rung gate, which is what the setting says
caste is.

And the last row: a cell whose decision rule is *no sustained objection* and whose record custody is
*none*. It cannot bind, cannot be bound, and can be paralysed by one member — the price of its virtue,
and the mechanical shape of "rejects formal sovereignty and alliances by ideology."

### 10.1 The Baralta Crown Claim, composed

Duchess Inge Baralta holds the proposition *the throne ought to pass to Baralta*. It becomes a motion
when coupled to a standing date whose prize is the throne — a **Crown Succession Contest**, container
the Realm, standing date the consecration.

Article count 5, each separately proved: descent · deed · consecration consent · no prior conceded
record · the cognatic-senior capacity test. The deed-monarchy makes article 1 nearly ungradable for
*everyone*: Altonia destroyed the records, so no claimant holds an instrument and descent grounds
bottom out at G0 for all parties. A setting fact producing a mechanical one.

**The Consecration Crisis is not a scripted event.** Article 3 requires the Church's consent, which is
an instrument in the Church's custody. If the Church's own succession is contested, **there is no
determinate custody**, so no ground can be graded G4, so article 3 cannot reach the floor for any
claimant. The sitting cannot close on the merits. It closes at the exchange budget with the venue's
decision rule producing a majority that cannot be published — **CARRIED-WITHOUT-FORCE**, for whichever
claimant has the seats. Two contested successions compose into a motion that carries and cannot bite,
a record row every party can cite, an F2 hazard on everyone who voted, and a `pattern` counter that
makes the next attempt heavier. Nothing about that was authored. It falls out of §6 meeting §4.2.

---

## 11. Who wins when nobody is playing

The engine resolves everything, so an NPC must argue, and must argue from **what they believe,
including what they wrongly believe.** No procedure below reads world state.

**Case assembly.** `choose(person, view)`. The NPC queries their ledger under §3.1's budget K, ranked
by `recency × confidence × relevance-to-the-motion × stance-weight`, keeps claims whose computed grade
meets the venue floor, and groups them into grounds by warrant. The stance-weight term does motivated
reasoning for free: a Templar assembling a case against an Einhir smith will not surface the exonerating
claim in his own ledger, because it argues against a stance he holds strongly. **No lying required.**

**Rung selection — strongest tenable.** The NPC estimates the opposition's decisive grade from their
*read* of it (claims about what the other side holds), and picks the highest rung it believes it can
survive:

```
believed_gap = my_best_grade − believed_opponent_grade
believed_gap ≥ +1  → rung 1 (Denial)
believed_gap ==  0 → rung 2 (Definition)
believed_gap ≤ −1  → rung 3 (Quality)
no admissible ground at all, or venue hostile → rung 4 (Jurisdiction)
```

**This is where the view bites hardest.** An NPC fed a false claim that the opposition's witness is
dead opens at rung 1, meets the living witness, and is driven down two rungs in one exchange. Planting
that claim is a complete political operation, executable by anyone with a Knot into the right
household, and it needs no rule of its own.

**Manoeuvre priority (first applicable):**

1. If an opponent's ground bottoms out in a synthetic root **that I believe I can name** → `strike_at_provenance`.
2. If an opponent's ground collides with a record row naming him → `press` on it (arming F2).
3. If I hold an unpleaded ground at or above floor and articles remain unproved → `plead`.
4. If pressed and I hold no answer → `descend` before the exchange lapses (a chosen descent costs one
   rung; F3 costs the sitting).
5. If my believed gap has gone to −2 or worse → `yield(current rung)` to close at a known price.
6. Otherwise `press` the opponent's weakest ground.

**Disposition.** Each judging-set member runs `choose(member, view)` over the motion and the record as
it stands *in their own ledger* — a member who arrived late genuinely did not hear the strike. The
venue's decision rule counts. The clerk writes the row.

**Fault checking is arithmetic, not judgment.** Every fault in §3 is a comparison over case state and
ledgers. There is no adjudicator and none is needed, which is what makes T8 reachable: a sitting in a
settlement nobody is watching resolves by the same procedure the player attends, not by a formula
approximating it.

---

## 12. Worked trace A — the Masterpiece Examination of Maret Uln

**Venue.** Kettlemakers' Row, Goldenfurt. Standing date: the guild's examination. Prize: Free Master
grade. Judging set: eleven Free Masters present. Floor: G4 on the work, **G0 on fitness**. Article
count 2 (the work, the fitness). Exchange budget 6.

**Motion.** Free Master **Aldwin Ruthe** moves *that the candidacy of Maret Uln be refused*. Maret's
sponsor, journeyman-warden **Gerik Strand**, defends. Maret is Southern Einhir; the Row is not.

**Aldwin's case, at rung 1 (Denial): the work is not hers.**

- Ground A1: *Maret did not raise the vessel herself* · warrant `caused-by` · support: two claims.
  - `c₁`: told_by Perrin the drayman, who says he saw a stranger at her bench at night.
  - `c₂`: told_by Osred of the Row, same content.
  - Aldwin pleads this as **G3, corroborated**.
- Ground A2: *she is not fit for the Row* · warrant `absence-implies` · support: common voice, **G0** —
  admissible here, and only here, because of this venue's fitness floor.

**Exchange 1.** Gerik `strike_at_provenance(c₂)`. He asks Osred, present, for his root. Osred's claim
is `told_by(Perrin)`. Both of Aldwin's supports therefore share **one** firsthand root. Per §3, one
story told three times corroborates once. Ground A1 falls from claimed-G3 to **G1**.

**Exchange 2.** Gerik `press(A1)` on Perrin's vantage: Perrin's claim is `firsthand`, but its `when`
interval is the night of the tithe reckoning, and Gerik pleads a record row — the praefect's roll,
**G4**, custody the praefect's — showing Perrin was at the reckoning in Goldenfurt, two hours' walk
away. The intervals collide. A1's root fails. **Ground A1 struck (F7, rootless).** Aldwin may never
plead `c₁` again, at any venue, forever.

**Exchange 3.** Aldwin has lost his fact case. He `descend`s to **rung 2 (Definition)**: *the vessel is
not a kettle of the Row's kind*. **This concedes, into the record, that Maret made it.** That
concession is permanent and is the most consequential thing that happens in the sitting.

**Exchange 4.** Gerik `produce`s the vessel. It is in the room. Physical presence gives it
`firsthand(read_of(object))` for every Free Master present → the work's grade is **G5, notorious**.
Article 1 is closed against Aldwin.

**Exchange 5.** Aldwin, holding only A2, attacks the word: he argues *kettle* in the guild's charter
means a vessel of hammered plate and Maret's is raised from a single sheet — an attack that would
stand identically if the vessel were excellent or worthless. That is the formal test for **F6, the
quibble**. Severity: **close**.

**Disposition.** `CLOSED-ON-FAULT` against Aldwin at rung 2. Motion **FAILED**. Maret is admitted Free
Master.

**What binds afterward, all of it computed:**

- `c₁` is struck globally. Perrin's word is worth less everywhere, and Osred's chain is public.
- The record row names Aldwin's conceded rung-1 position. He can never again plead that Maret did not
  make the vessel: **F2**.
- Aldwin's F6 costs him regard with every Free Master whose stance weights Honor or Precedent, and
  nothing with those who weight Community and dislike the admission anyway. Regard moves per person,
  not as a guild scalar — which is why the Row is now split rather than uniformly cooler.
- **Ground A2 was never struck.** It was never reached. Common voice on fitness survives the sitting
  intact, at G0, and `pattern(fitness-of-Southern-Einhir-candidates)` is now **1**. The institution
  lost this examination and its bias is undamaged, because the bias lives in a floor parameter and not
  in a claim anyone had to defend. That is the setting's thesis, produced rather than asserted.

---

## 13. Worked trace B — a negotiation lost to a wrong view

**Parties.** Duchess **Inge Baralta**, who intends the Crown Succession Contest, and Grandmaster
**Sigrid Ehrenwall** of the Löwenritter, whose Order she wants neutral. Private venue, budget 4, no
record custody.

**Inge's read of Sigrid's reservation set** — three claims in Inge's ledger:

- `r₁`: *the Löwenritter's loyalty runs to the bloodline* — `inferred` from her marks-based expectation
  of a military-religious order. Grade **G−**.
- `r₂`: *Sigrid's house wants precedence at court* — `told_by` a Baralta client. **G1**.
- `r₃`: *the Order's houses are short of endowment* — `firsthand`, from the last levy day. **G2**.

Every one of these is about **Sigrid as a person to be paid**. `r₁` is simply false: the Order is loyal
to the Crown *as institution, not bloodline*. Inge has no claim of that in her ledger at all, and per
§3.1 the absence is not a blur — it is nothing, so she acts from her prior.

**Exchange 1.** Inge `propose`s: precedence for Ehrenwall at the Hafenmark court, plus an endowment on
two Baralta holdings, in return for the Order standing aside at the consecration. The proposal is a
telling: it deposits into Sigrid's ledger the claim *Baralta believes the Order can be bought* — at
`firsthand`, **G2**, from Sigrid's own hearing. Sigrid did not have that claim before. She has it now,
permanently, and it is admissible anywhere.

**Sigrid's actual reservation set**, evaluated on demand: any bundle in which **the claimant is
consecrated before the Order is asked to move**. It is not about money and it is not about her house.
Nothing in Inge's bundle touches it.

**Exchange 2.** Sigrid `counter`s with one clause: *Baralta seeks the Doctrinal Adjudication
Dicastery's determination on article 3 before the standing date.* To Sigrid this is her whole position.
Inge reads it through `r₁` — she believes the Order follows blood, so a demand about consecration must
be **a price dressed as a principle**, i.e. a bluff to raise the endowment. She counters by raising the
endowment.

**Exchange 3.** Sigrid `press`es the consecration clause. Inge has no answer that engages it, because
in her view there is nothing there to engage — her answer moves to the endowment again. Her reply's
proposition does not overlap the challenged one on subject: **F4, shifting the ground**, severity
`descend`. In a private venue with no third-party judging set, the descent costs no regard with a room;
it costs the only thing there is to lose here, which is Sigrid's read of *her*.

**Exchange 4.** Inge `withdraw`s, believing the Order's price is above what neutrality is worth.

**What the withdrawal deposits — the expensive part.** `withdraw` writes into Sigrid's ledger, at
`firsthand`, **G2**: *Baralta will not seek consecration before the contest.* Sigrid `tell`s it to
Confessor **Arne Himlensendt**, in good faith, because it is true and because it bears on the Church's
own position. It arrives in Arne's ledger as `told_by(Sigrid)` at **G1** — and Sigrid is a Grandmaster
whose stance-standing with Arne is high, so his credulity roll lands it at high confidence.

**Consequences, none of them scripted:**

- Arne now holds a rooted claim supporting a motion in the **Doctrinal Adjudication Dicastery** that
  the Baralta claim proceeds without consent. Article count 3, floor G3 — so his G1 is not yet enough,
  and he must send someone to root it better. **A negotiation failure has produced a field
  investigation**, which is T9 arriving through T7's door.
- Inge's own case at the Crown Succession Contest is now materially worse on article 3, and she does
  not know it, because nothing has collided with her belief yet. Her `r₁` is untouched. She will
  probably make the same error with the next order she approaches.
- No accord existed, so nothing was breached and nobody defected. **Cheap talk was the default and it
  cost her a duchy's worth of position anyway** — which is the point of making binding expensive.

---

## 14. NERS self-audit

**N.** Every object carries its N-line in place. The one I defend hardest is the stasis ladder: cut it
and the manoeuvre set has nothing to differentiate on but output size — the refused design, and the
observed failure of the only close precedent.

**E as a ratio.** Three fusions, each removing an object without removing a possibility: the
**compromise scale is the stasis rung** (no concession subsystem); the **negotiation venue is a debate
venue with different parameters** (no second mechanic); the **record is an instrument in custody** (no
container memory, no second knowledge model, and forgery for free). Three additions refused: a Body of
Argument or any debate pool, a persuasion threshold, a per-chamber ruleset — each because a parameter
row already reaches it.

**R.** Forks checked for shape, not balance. *Rung 1 vs rung 2 at open*: rung 1's gain is high and its
cost is a cliff; rung 2's gain is capped and its cost is flat. Neither dominates. *Press now vs bank a
recorded defeat*: compounding gain against one-time cost, versus immediate gain against compounding
cost. *Produce an instrument vs hold it*: producing raises your grade now and makes the object's
existence public, arming attacks on its custody forever. *Cheap talk vs a binding instrument*: cost up
front against a benefit contingent on a breach that may never come.

**S-UP.** A person's computed need → petition → carrier → **motion** at a venue with a standing date,
where a named person may press, drop, or descend on it, and where refusal is written into a record that
makes the next attempt heavier. Filtering is a person deciding, at every rung, including in the chamber.

**S-DOWN.** Disposition → rider → document 06's dispensation → changed terms → deposited as claims by
crier, parish, guild notice or Knot → recomputed openings for **a person holding no post**. Trace A's
rider changes what a Southern Einhir journeyman two hamlets away believes about the Row's gate, with
nobody telling him he is now allowed to try.

---

## 15. Challenge to the spine

One, and it is small. §5.3 assigns standing dates to **containers**. Every venue in §10 is a container
plus a prize plus a date plus decision parameters — but a private negotiation is a venue with
`container = none`, which the substrate does not contemplate.

I am flagging rather than diverging. The honest reading is that a private negotiation is **not a rung
mechanism at all**: it is two persons performing `tell` acts at each other under a mutually-known
deadline, and every mechanism I gave it — proposal-as-telling, reservation reads, withdrawal-as-deposit
— is already the substrate's transport layer. The venue framing is presentational, chosen so §8 and
§10's table are visibly one mechanic. If the spine's author disagrees, I will state negotiation purely
in `tell`/`witness` terms with no venue row, and nothing in §12 or §13 changes.
