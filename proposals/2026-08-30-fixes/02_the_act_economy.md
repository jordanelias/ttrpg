# 02 — The Act Economy

## Status: PROPOSED (2026-08-30) — a reconciliation of two existing statements, not a new system. Nothing here ratifies on merge.
## Fixes: `09_GAP_REPORT.md` **D-2**, reached independently by three season lanes.
## Composes on (binding): `09_churning_world.md` §1.1–1.4; `14_office_and_upper_rungs.md` §1, §3.1, §8; `05_up_stroke.md` §3.1; `04_hearth_and_community.md` §1.4; `06_down_stroke.md` §3, §8; `01_substrate.md` §2
## Evidence used as a discriminator: the coverage exercise's 56 probes, `08_coverage_matrix.md` §2 finding 2

**The contradiction, stated once.**

> `09 §1.1`: *"The tick is a season. **Every person and every cohort commits exactly one act per
> season.**"* — with an N-line that says unlimited acts destroy the collision the design exists to
> produce.
>
> `14 §8`: *"**A worked season — Vaynard, one turn, ten acts, no faction verbs.**"*

And `14 §1` forbids the obvious reconciliation before it is offered: *"An office adds **no verb to the
game**… A Duke and a hamlet fisher run the same `choose(person, view)` over the same act vocabulary.
They differ in three quantities and nothing else: **remit**, **reach**, and **binding**."* An office
that adds no verb cannot add an act allowance either; that would be a fourth quantity.

**The answer this document reaches, in one line.** *One act per person per season stands, universal and
unscaled — and the act count in an office-holder's season is not his allowance, it is his **reach**,
because reach was already defined as a roster of persons and every person on it gets an act of their
own.* The fourth quantity is not added. Two of the three that already exist turn out to be the same
list counted twice.

---

## 1. The three readings, each with its real argument

I state all three at their strongest, because the brief is right that two of them have one.

**Reading A — strict one act, everywhere, and `14 §8` is simply wrong.** Attention is genuinely scarce;
the Duke picks one of `convene`, `issue`, `dispatch`, `confer`, `carry`, `commit` and the rest wait. It
is the only reading that follows from a document explicitly owning the tick, and `05 §3.1` already
prices one office operation this way — `compose_agenda` costs *"one of v's own acts for the season"*.
**Its cost:** a duke's season and a fisher's season are the same size. Lane 4 wrote both ducal seasons
on it and reported the result as *"a sharp game, and also close to THIN — four shapes, one pick, two of
them cosmetically different in most seasons."* It also makes the design's rung-ownership argument
hollow: if Duchy-scale play is Settlement-scale play with a bigger stake, `14 §3` has not earned its
rungs.

**Reading B — the act budget scales with office.** It makes an office-holder's breadth real, and it is
what `14 §8` was actually doing. **Its cost is fatal and it is not merely doctrinal.** It contradicts
`14 §1`'s founding claim outright. It reintroduces a scalar that gates options by position, which
`01 §1.3` refuses for factions on exactly this ground. And it removes scarcity from the people whose
attention should be the most fought over: the whole of `09 §1.1`'s N-line is that a Free Master who can
both stand for the guild seat *and* answer his Einhir cousin's petition is never Southern Einhir in any
way that costs — and a Duke who can both hold his territory court *and* commit to breaking the caste
order is never conflicted in any way that costs either. **Reading B deletes the collision from the top
of the ladder, which is where the design most wants it.** Rejected.

**Reading C — the unit is wrong, not the count.** An office-holder's acts are performed by his
**establishment**, and an establishment is a list of persons, each of whom is an actor under `01 §2`
with their own view, their own needs, and their own one act. The count in an office-holder's season is
then **derived** — from how many people serve him and whether they chose to — rather than declared.

---

## 2. The coverage exercise already ran the experiment that discriminates them

This is the decisive argument, and it is not mine: it is 56 probes across six lanes that could not see
each other.

Each reading makes a different prediction about **what should predict a THIN office-holder**.

| reading | predicts a THIN office-holder is one with… |
|---|---|
| **A** — flat one act | nothing in particular; every holder's season is one act, so richness tracks *what his one act can be* — i.e. **remit size** |
| **B** — budget scales with office | a **low office**; richness tracks rank, height, seat |
| **C** — count derived from establishment | an **empty or unreachable establishment**, regardless of remit or rank |

And the measured result, `08_coverage_matrix.md` §2 finding 2, verbatim: *"**Among office-holders: an
empty or unreachable establishment, never a small remit.** Almud has the largest remit in the game and
the thinnest reach. Himlensendt's establishment is `none`. Tormann is RICH precisely because his is the
one Cardinal seat canon fills. **The design prices remit and forgets establishment.**"*

- **A is falsified.** King Almud Almqvist holds the largest remit in the game and is THIN. Cardinal
  Aldric Tormann's remit is smaller and he is the richest churchman in the exercise.
- **B is falsified**, and points the wrong way besides: office-holding runs 32% bad against 47% among
  the postless, while the highest office in the game is THIN and a parliamentary clerk outreaches the
  King.
- **C matches, and matches at 100% within its class.** Tormann is RICH *because his is the only Cardinal
  seat canon fills* — the only Cardinalate whose establishment is non-empty. Confessor Arne Himlensendt
  roots four office clusters with `establishment: none` and is THIN. Voss's establishment is a
  conjunction over two other men's offices and his capacity is a conjunction to match.

**Three readings, three distinct predictions, and one of them is what six lanes measured without
looking for it.** That is the strongest evidence this process produces, and it is why C is not a
compromise between A and B. It is the reading the data already picked.

---

## 3. The ruling

Four statements. Three are restatements of things the suite already says; one is a price that was
missing.

### 3.1 One act per person per season, universal and unscaled

`09 §1.1` stands **exactly as written, with no exception for office.** An act is the one discretionary
commitment. Subsistence, craft and travel-in-progress remain P1 and happen *to* you. A standing date
firing is P0, not an act. `witness` is P6, not an act.

- **Loop:** produced by `choose(person, view)` → carried in the season's act queue → consumed by
  `resolve`. Unchanged.
- **N-line:** cut it and you lose priority, therefore every dilemma — and you lose it *first* at the top
  of the ladder, where Duke Magnus Vaynard's container (Varfell's levy) and his alignment (*the caste
  order ought to be broken*) want the same hour of the same life. That collision is `01`'s stated
  definition of politics, and Reading B is the only one of the three that deletes it.

### 3.2 An establishment member is a person, and gets their own act

`14 §1` defines `establishment(o)` as *"the named persons the office employs."* `01 §2` says persons
act and nothing else does. Put together with 3.1 and it follows with no new rule: **the reeve, the
granary keeper, the ducal proxy, the nine riders and the two watchmen each get one act a season, chosen
from their own view.**

They mostly serve the office, and the reason is already written and needs no standing-order object:
`14 §1.3`'s **upkeep** fills an establishment member's larder from the office's stake, so his own
`need(subsistence)` is answered by the post and threatened by failing it; his `need(standing)` runs
among his siblings-in-establishment; and his stance toward the holder is an ordinary row. **He does his
job because his own computed needs say so** — which means he can stop, and the design already told us
what that looks like: *"an unpaid establishment… does not disperse, it becomes a faction and treats
plunder as wages."* That sentence has had no mechanism producing it. Under C it is produced by
construction.

- **Loop:** produced by each member's own `choose` against their own view → carried as ordinary acts in
  the season's queue → consumed by `resolve`, and by the holder's ledger when the member's tellings
  come back (`14 §3.1`).
- **N-line:** cut it and an establishment is a multiplier on its holder's hours rather than a set of
  people, `14 §3.1`'s reach becomes a number instead of a roster, and the difference between a governor
  who is obeyed and one who is not becomes inexpressible.

### 3.3 `dispatch` is `requisition`, and it costs BOTH parties an act

`14 §1.1` already says `dispatch` *is* `requisition` on an establishment member, and `04 §1.4` owns
requisition as the hearth's obligation edge. The missing price is stated here:

```
dispatch(holder, member, act) :
   costs the HOLDER   one act — his own, for the season
   costs the MEMBER   one act — theirs, for the season
   the member still runs their own choose:  comply_pressure = claim_weight − strain   (04 §1.4)
   one dispatch names ONE person.
```

So a holder may **redirect exactly one of his people by name, per season, and may be refused.**
Everyone else on his roster does what their own view says. This is the one genuinely new sentence in
this document, and it is a price on an existing act rather than a mechanism.

It also retro-prices something the control's season found free. Alvid Bekk requisitioned her sister
Gerd and `07 §II P4` records *"the ask costs her nothing."* Under 3.3 it costs Gerd her season — which
is a real cost, borne by someone, and it partly answers the unpriced `foster out` dominance that
document 01 §8 could name and not close.

### 3.4 An order is a telling; compliance is the hearer's own choose

`14 §1.1` already defines `issue` as *"`tell`, with terms."* `06` already resolves a dispensation's
compliance as a contest read off the persons in scope. Therefore:

**An office-holder's terms reach his own establishment by exactly the mechanism they reach anybody
else** — deposit by presence and channel, distortion in transit, and then each member's own `choose`
over changed terms. `issue` is one act. What happens next is nine people's acts, and `06`'s compliance
machinery — built for subjects — turns out to describe your own staff. That is the post-Secession
Crown's actual problem, and the design gets it without writing a loyalty stat.

### 3.5 The derived count

```
acts_in_an_office_holder's_season
   = 1                                                        # his own, exactly like the fisher's
   + | { m ∈ establishment(o) : m's own choose selected an act serving the office } |
```

The second term is not his to set. **It is nine other people's answer**, and he learns it the way he
learns everything else — as claims deposited by their tellings, one node at a time, coarse where he has
nobody (`14 §3.1`).

- **Closed loop.** Produced by `confer` filling seats and by upkeep filling larders; carried as the
  `Holding` edges and the establishment roster; consumed by every season's act queue, by `14 §3.1`'s
  reach, and by `06`'s `enforcer_presence`.
- **N-line — cut the derivation and you lose:** the difference between a large office and an obeyed one.
  Every governor governs at the size of his warrant, an empty Cardinalate is as effective as a filled
  one, and the whole of the setting's post-Secession problem — a Crown whose praefects answer to their
  provinces — becomes something that must be written into canon by hand rather than something the tick
  produces.

**And the claim `14 §1` was protecting is intact.** No verb was added, no allowance was granted, and the
three quantities are unchanged. What C says is that **the act count *is* reach** — `14 §3.1` already
defined reach as a count of persons and channels with no distance term, and this document observes that
the same roster answers "where do I have someone" and "how much happens in my name." One list, two
questions. Nothing was added to the schema.

---

## 4. Vaynard's season, re-attributed line by line

`14 §8`'s worked season, with every act assigned to the person who actually spends it.

| the passage's act | who spends the act | under the ruling |
|---|---|---|
| `convene`s the Grauwald territory court and puts the levy ahead of the hamlet's grain petition | **the ducal proxy.** `05 §3.1` names the convener of that court as the proxy, not the Duke — *"it is an ordinary office: conferred, revocable, vacant-able"* | the proxy's act, ranked by the proxy's own valuation. The Duke may override by dispatching him — one act, and the proxy still chooses |
| `issue`s a levy dispensation over five territories | **the Duke** | one act. Publication is not further acts of his: `06` deposits by presence and channel through criers, priests, guild notices and the market |
| `dispatch`es two riders | **the Duke, once** | one dispatch, one rider, one act each side. The second rider goes where his own view sends him — or does not go |
| `confer`s a provincial sub-remit on a capable Southern Einhir reeve | **the Duke** | one act, and irreducibly his (§5) |
| `revoke`s a benefice he cannot revoke, so it lands as a `tell` asserting a remit he lacks | **the Duke** | one act |
| `carr`ies one bundled petition into the Realm's standing date | **the Duke** | one act, *and* one of the Realm's seat items — two budgets, two owners (§7) |
| `commit`s at degree 4, avowed, at publicity 2.0 | **the Duke** | one act, and irreducibly his (§5) |

**Six of the seven the passage names are the Duke's own, and he can have one.** That is the correction.
What the passage got right is that Grauwald's season *contains* about ten acts — and under C it still
does. It contains more: the proxy composes the agenda, the reeve collects the levy at Stillhelm, the
herald publishes in four settlements, two riders ride or do not, the granary keeper at Goldenfurt
decides whose sacks move first. Ten acts, nine actors, one Duke.

**And the season is now about the thing it should be about.** `14 §1.2` already told us: *"choosing
which of your people performs the act is the whole of a leader's tactical choice, and it is a choice
between pools, not a purchase of a bonus."* Under Reading A that sentence has nothing to attach to,
because the Duke's one act is usually not a dispatch. Under C it is the governing sentence of the
upper-rung game.

---

## 5. The two acts nobody can perform for you

Falls out, and is worth stating because it is the sharpest thing C produces.

An establishment can `issue` for you (a herald reads your terms), `carry` for you (a proxy holds your
seat), `determine` where the venue's decide rule names your office rather than you personally, and
`convene` for you. It cannot do two things:

- **`confer` / `revoke`**, because the act is the passing of *your* warrant. `14 §1` carries the
  conferrer's name as the source of the `post:` mark; a herald conferring in your name confers his own
  nothing.
- **`commit`**, because a faction edge is a person's own commitment at their own degree. Nobody can
  throw in with the Restoration on your behalf.

**The acts an office-holder cannot delegate are exactly the ones that change who serves him and who he
is.** Everything else about a magnate can be done by somebody else; those two are why he must spend his
own season on them, and why a duke's most consequential turns are the ones where he does something that
looks like a private matter.

---

## 6. Checked against the King's season, and against the control's

### 6.1 King Almud Almqvist — from THIN to CONTESTED, and not to RICH

The exercise found his season THIN by **dominance**, not by count: `issue` structurally dominated,
`confer` moving `sovereign_fraction` by zero, `convene` and `determine` self-referential, `revoke`
near-empty, and *"his one non-dominated act BLOCKED at a venue convened by his rival."*

C does not repair any of that — those are D-8, and this document does not touch them. What C changes is
what the season is *about*. His establishment is the household and the Crown praefects, and under 3.2
each of those praefects spends a season acting from his own view. `02 §1.3` records who they are: cadet
and deed families whose standing came from Secession War service, holding *the post-war settlement is
owed to those who won it* at high weight. Several of them are, in practice, their province's men.

So the King's season becomes: **one act of his own, and nine answers he does not control.** That is a
weak person at the head of a strong position, which is precisely the post-Secession Crown the setting
describes, and the design now says it with the tick rather than with adjectives.

**Honest verdict: C moves Almud from THIN to CONTESTED, not to RICH**, and the thing that would move
him to RICH is filling `sovereign_fraction`'s establishment problem, not raising his act count. This
also diagnoses why Reading B *felt* like it made him rich: it was handing him nine acts that under C
belong to nine people who may not give them. **A ten-act King is not a powerful King. He is a King
whose staff has been deleted and replaced with his own hours.**

### 6.2 Alvid Bekk — unchanged, and that is the point

She holds no office and no establishment. Her season is one act, before and after. C does not touch the
floor, which is why document 01 exists separately.

Three things it does change around her, all in the right direction:

1. **Her `requisition` of Gerd and Vaynard's `dispatch` of a rider are now literally the same call with
   the same price.** `14 §8`'s table asserts that already — *"`requisition` | his brother, claim weight
   2.0 | **`dispatch`** — the same call, on an establishment member"* — and under Reading A or B it is
   not true, because one costs a season and the other costs a tenth of one. Under C it is true.
2. **The ask stops being free.** Gerd spends her season fostering. Document 01 could name the
   unpriced-`foster out` dominance and not close it; C prices half of it.
3. **She is a candidate establishment member**, and so is her husband Nils, a hired carter at the ford
   landing. Under C, institutional throughput is *made of* people like them — which is the same
   conclusion document 01 reaches from the root side. **A design whose ordinary people are thin has thin
   institutions, because institutions are made of ordinary people.** The two fixes are one fix seen from
   two ends.

---

## 7. Three open items this settles in passing, and one it does not

**S1 — `seat_items` has two owners.** `14 §1.3` makes it the holder's hours; `05 §3.1` makes it the
container's standing-date capacity. **Settled: it is the container's.** The standing date belongs to the
container and hears a finite number of items; the holder's own scarcity is his one act. `14 §1.3`'s
conclusion — *"holding two offices does not double a day"* — survives, for a better reason: you still
get one act. The duplicate mechanism goes.

**S9 — does `tell` accept a cohort hearer?** Under C the question dissolves, because it was an
act-budget question wearing an argument-list costume. `tell` is one act by the speaker; **who hears it
is P6's fan-out by presence and channel**, which `04 §4.1`'s `hears()` already computes over persons,
and which `09 §1.2`'s P3 already gives cohorts as *"channel claims at its address."* Askeland teaches
nine children in one act because nine children were in the kitchen, not because the signature takes a
cohort. The Restoration's growth channel keeps its two orders of magnitude and nothing is added.

**The unfilled Cardinalates.** `08_coverage_matrix.md` calls them *"a structural SPECTATOR that is not a
person"* — a season passes, nothing fails, and no act in the design can fill them. C does not fill them
either. What it does is make their emptiness *cost something visible*: under 3.5 a Cardinalate with no
establishment produces one act a season, and the Dicastery it roots produces none. **The vacancy stops
being invisible.** That is a smaller claim than solving it and it is the true one.

**What it does not settle: the conferral cycle (D-6).** C makes establishments load-bearing, and
establishments are filled by `confer`, and `confer` in the Church is a cycle with no external root. So C
raises the price of leaving D-6 open. It does not pay it.

---

## 8. R-criterion check on the ruling itself

Per `14 §9`: an option is structurally dominant when its gain compounds against a cost that decays or is
absent. Under C, an office-holder's fork is `{ issue, dispatch, confer, determine, carry, commit }`.

**`dispatch`.** *Gain compounds* — `14 §3.1`: a dispatched man deposits firsthand claims, so that node
stops being a cohort in your ledger and stays finer for several seasons. *Cost compounds two ways* —
`04 §1.4`'s regard price scales with how unreasonable the demand is and `14 §9` notes that *"loyalty is
regard and regard is spent by every ask"*, so repeatedly dispatching the same man degrades him; and
every node you did **not** reach this season goes coarser. Concentrate and you burn a man; spread and
your fidelity decays everywhere. **Not dominant.**

**`issue` against `dispatch`.** Broad and uncertain against narrow and certain: `issue` reaches
everyone in scope in one act and its compliance is nine people's own choices, resolved by `06`;
`dispatch` reaches one node with near-certainty and nowhere else. Genuinely different shapes.

**`confer`.** Checked already by `14 §9` and unchanged: compounding gain (permanent reach) against
compounding cost (`14 §1.4`'s shadow standing — *a rival you built*). C sharpens it: the man you confer
on is now a person spending his own act every season, so a capable appointee is a capable independent
actor from the day he is signed.

**`commit`.** One-shot, avowed, and paid for in every Crown-Latinate quarter's judging set at once.

Six forks, no dominance, and the fork set is what `08_coverage_matrix.md` §2's finding 1 requires for
RICH: *"three or more live modes or four differently-shaped acts."* **Under C an office-holder passes
the R-check on the strength of his roster, and fails it when his roster is empty.** That is the
behaviour the exercise measured.

---

## 9. What it costs

Stated plainly, because a reconciliation that claims to cost nothing has hidden something.

1. **The player holding a Duke does not get a big turn.** He gets one act and a personnel problem. Some
   of that reads as a demotion, and there is no way to soften it without becoming Reading B.
2. **It converts a roster gap into a mechanical gap.** Under C, an office whose establishment canon does
   not name produces one act a season. That is honest, and it is expensive: `09_GAP_REPORT.md` §5
   records that stats are null for all five churchmen, that canon names no guild warden, and that two
   Cardinalates are unfilled. **Every office in the roster must name its establishment or accept being a
   one-act office.** The mitigation is that this is cheap authoring — a list of names — and not a
   mechanism.
3. **A magnate's throughput is hostage to persons.** Jarl Holdar's overt refusal, Voss's establishment
   being a conjunction over two other men's offices, a rider who does not ride: all of these become
   normal rather than exceptional. Some sessions a Duke will find that nothing he wanted done was done,
   and there will be no roll to blame.
4. **It shifts the upper-rung game from decrees to staff.** If a player came for a strategy layer about
   proclamations, C gives them one about who is reliable in Grauwald this year. I believe that is the
   better game and it is a real change of genre at the top of the ladder.
5. **It costs nothing in compute**, which is worth saying because it looks like it should. Every person
   already receives a `choose` call every season (`09 §1.2` P4, and `09 §10`'s own arithmetic makes a
   fully individuated battle ~9,600 calls and calls it nothing). C spends no additional call. It
   re-attributes calls that were already being made.

---

## WHAT THIS FIX MIGHT BREAK

1. **`14 §8` must be rewritten, not annotated.** The worked ducal season is the document's showcase and
   under C it is wrong as written. Leaving it with a footnote is what produced this defect: a lane
   reading `14` alone will re-derive the ten-act economy from a passage that reads like a demonstration.
   **Rewrite the passage with §4's attributions or delete it.**

2. **`05 §3.1`'s `compose_agenda` price becomes the model rather than an oddity — and it makes the
   convener the most expensive office in the game to hold.** Charging a convener his whole season to
   rank a docket is right under C, but it means the ducal proxy who composes the Grauwald agenda can do
   nothing else all season. The gap report's own convergence list says *"the convener holds the cheapest
   real power in the game"*, found by five lanes. Under C it stops being cheap. That may be a
   correction, and it may erase a finding five lanes independently thought was true; somebody should
   decide which.

3. **`06 §8`'s reach cap and `14 §3.1`'s establishment become the same object, and one of them should
   go.** If the number of nodes reached is the number of persons dispatched or relaying, a separate cap
   is either redundant or contradictory. I have not checked which.

4. **The establishment now needs a defined boundary, and it currently has none.** Are Ivar Holt's two to
   five watchmen his establishment as gate warden, the praefect's as his conferrer, or both? `14 §1.5`
   lists establishments as prose phrases — *"the watch, the granary keeper"*, *"registers, assessors"*,
   *"a Dicastery's whole graph"* — and under Reading A that vagueness was harmless. Under C **every one
   of those phrases is an act count**, and a person appearing in two establishments would be spending
   two acts. The roster must become a set of named persons with exactly one membership, or C
   double-counts.

5. **It puts pressure on D-3 from the opposite side to document 01.** An establishment member's
   willingness to serve is his own computed need — and `need(commitment)` and `need(exposure)` are
   exactly the two terms that have no formula. So C makes the missing half of the motive engine
   load-bearing on **institutional throughput**, not just on individual motivation. A reeve's decision
   whether to collect at Stillhelm this season currently computes from his larder and nothing else.

6. **The `dispatch` refusal needs a public face and may not have one.** Under 3.3 a member may refuse.
   `14 §3.1` gives Jarl Holdar's overt refusal a deposit — *"`(order, was_obeyed, false)` in every
   witness"* — but a quiet non-compliance, the rider who simply does something else, deposits nothing
   into the Duke's coarse ledger. That is arguably correct (it is the same blindness `14 §3.1` prizes)
   and it is arguably a hole: a holder may not be able to distinguish an establishment that failed from
   one that never tried, ever.

7. **It sharpens the Löwenritter and Niflhel asymmetry in a way nobody has priced.** Grandmaster
   Ehrenwall's establishment is *"every chapter's riders"* — the largest roster in the game — while
   Confessor Himlensendt's is `none`. Under C that is not a flavour difference; it is the difference
   between a season with dozens of acts in it and a season with one. **The exercise found Ehrenwall's
   refusal already the most contagious act in the roster.** C makes the body behind it much larger, and
   nothing currently balances that.

8. **Cohorts.** `09 §1.1` gives a cohort one act too. If an establishment is held at cohort fidelity —
   "the watch", eleven men, one record — then under 3.5 it contributes **one** act, not eleven, and a
   holder can buy throughput by individuating his own staff. That is either a fine emergent incentive
   (know your people and they do more) or a fidelity exploit, and I cannot tell which from the spine
   alone. It is the one place where C's derived count interacts with the resolution machinery, and it
   should be tested before C is trusted at scale.
